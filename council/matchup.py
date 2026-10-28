#!/usr/bin/env python3
"""Matchup prep: the rest of this week, day by day, and the best streams for us.

Stdlib only and read-only against ESPN. It uses the same two cookies as
council/espn_sync.py. It reads our current matchup in league 423671879:
  - the score
  - both rosters
  - every remaining game
  - our adds used against the limit

For each remaining day, an exact optimiser fills the 10 starting slots (PG,
SG, SF, PF, C, G, F and 3 UTIL) from the players with a game. That gives each
team's projected total, the open slots each day, and the value of any roster
change. A streamer is worth the change in our optimised total, not his
average: a game on a day our slots are full adds nothing.

Rate per game:
  - 3+ games this season: 70% this season's FP/g, 30% last season's (or
    ESPN's projection when there is no last season)
  - 1–2 games: 50/50
  - none: last season's, else the projection
A player listed OUT is left out until ESPN's estimated return date.

Matchups are taken as weeks running Monday to Sunday (US time), because
ESPN publishes no matchup calendar. --end overrides the last day, for
example in two-week playoff rounds.

Guards, as in slump_watch.py:
  - It refuses to run while NBA games are live. --allow-live overrides this.
  - Every season average must re-score with scripts/league_scoring.py to
    ESPN's total.

Usage:
  python council/matchup.py                              # drop candidate: our lowest-rate player
  python council/matchup.py --drop "Payton Pritchard"    # the slot we stream with
  python council/matchup.py --drop "Payton Pritchard" "Paul Reed" --out docs/analysis/20261027-matchup2.md
  python council/matchup.py --rotate "Payton Pritchard" "Fred VanVleet@2026-10-29"   # two slots, VanVleet's from Thu
"""
import argparse
import datetime as dt
import itertools
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from injuries import injuries as injury_feed  # noqa: E402
from injury_watch import box, player_pool  # noqa: E402
from slump_watch import ET, FANTASY, LEAGUE, TEAM_ID, get, live_games, signed  # noqa: E402

SLOTS = (0, 1, 2, 3, 4, 5, 6, 11, 11, 11)  # PG SG SF PF C G F UTIL UTIL UTIL
FITS = {"PG": {0, 5, 11}, "SG": {1, 5, 11}, "SF": {2, 6, 11}, "PF": {3, 6, 11}, "C": {4, 11}}
IR_SLOT = 13


def rate(r):
    if "rate" in r:  # a what-if override (--rotate's break-even search)
        return r["rate"]
    cur, other = r["current"], (r["last"] or r["projected"] or {}).get("fpg")
    if cur and cur["gp"] >= 3:
        return 0.7 * cur["fpg"] + 0.3 * (cur["fpg"] if other is None else other)
    if cur:
        return 0.5 * cur["fpg"] + 0.5 * (cur["fpg"] if other is None else other)
    return other or 0.0


def slots_for(r):
    fits = [FITS[p] for p in (r["pos"] or "").split("/") if p in FITS]
    return frozenset(set().union(*fits)) if fits else frozenset({11})


@lru_cache(maxsize=None)
def best_lineup(players):
    """Highest total rate the 10 slots can hold. players: tuple of (rate, frozenset of slots)."""
    @lru_cache(maxsize=None)
    def fill(i, used):
        if i == len(SLOTS):
            return 0.0
        top = fill(i + 1, used)
        for j, (value, fits) in enumerate(players):
            if not used >> j & 1 and SLOTS[i] in fits:
                top = max(top, value + fill(i + 1, used | 1 << j))
        return top
    return fill(0, 0)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--drop", nargs="*", default=None, metavar="NAME",
                    help="our players to test as the streaming slot (default: our lowest-rate player)")
    ap.add_argument("--top", type=int, default=12, help="streamers listed per drop candidate (default 12)")
    ap.add_argument("--min-minutes", type=float, default=12, help="current minutes a streamer needs (default 12)")
    ap.add_argument("--tz", default="Australia/Melbourne", help="second time zone shown beside ET")
    ap.add_argument("--end", help="last day of the matchup, YYYY-MM-DD (US date); default: this Sunday")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--rotate", nargs="+", metavar="NAME[@YYYY-MM-DD]",
                    help="our flexible slots: the best sequence of streamers through them for the rest of the week. "
                         "A date is the first US day the slot may change (default: the first day his game hasn't started)")
    ap.add_argument("--sit", nargs="+", default=[], metavar="NAME@YYYY-MM-DD",
                    help="treat a player as not playing on that US date, e.g. a planned rest on a back-to-back")
    ap.add_argument("--pool", type=int, default=14, help="free agents --rotate considers (default 14, plus each day's top 3)")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()
    local = ZoneInfo(args.tz)

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")

    now = dt.datetime.now(dt.timezone.utc)
    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches[:20]))
    feed = injury_feed()
    league = get(f"{LEAGUE}?view=mTeam&view=mRoster&view=mMatchupScore&view=mSettings&view=mStatus", cookies=True)
    teams = {t["id"]: t for t in league["teams"]}
    matchup = league["status"]["currentMatchupPeriod"]
    game = next(m for m in league["schedule"] if m["matchupPeriodId"] == matchup
                and TEAM_ID in (m["home"]["teamId"], m["away"]["teamId"]))
    us, them = (game["home"], game["away"]) if game["home"]["teamId"] == TEAM_ID else (game["away"], game["home"])
    opp = them["teamId"]

    pro_teams = get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
    abbrev = {t["id"]: t["abbrev"] for t in pro_teams}
    tips = {}  # (pro team, period) -> tip-off (UTC)
    first = {}  # period -> first tip-off
    tipped = {}  # pro team -> ids of games that have tipped
    for t in pro_teams:
        for p, gs in t.get("proGamesByScoringPeriod", {}).items():
            for g in gs:
                when = dt.datetime.fromtimestamp(g["date"] / 1000, dt.timezone.utc)
                tips[(t["id"], int(p))] = when
                if when <= now:
                    tipped.setdefault(t["id"], []).append(g["id"])
                first[int(p)] = min(first.get(int(p), when), when)
    today = now.astimezone(ET).date()
    monday = today - dt.timedelta(days=today.weekday())
    end = dt.date.fromisoformat(args.end) if args.end else monday + dt.timedelta(days=6)
    in_matchup = [p for p, w in first.items() if monday <= w.astimezone(ET).date() <= end]
    days = sorted(p for p in in_matchup if any(w > now for (tid, q), w in tips.items() if q == p))
    if not days:
        sys.exit("No games left in this matchup.")
    label = lambda p: (f'{first[p].astimezone(ET):%a %d %b}', f'{first[p].astimezone(local):%a %d}')

    sits_out = set()
    for spec in args.sit:
        name, _, when = spec.rpartition("@")
        sits_out.add((name.strip().lower(), dt.date.fromisoformat(when)))

    def plays(r, p):
        if (r["pro"], p) not in tips or (r["player"].lower(), first[p].astimezone(ET).date()) in sits_out:
            return False
        i = feed.get(r["id"])
        if i and i["status"].lower() == "out":
            return bool(i["return"]) and i["return"] <= first[p].astimezone(ET).date()
        return True

    def total(roster, p):
        return best_lineup(tuple(sorted((rate(r), slots_for(r)) for r in roster if plays(r, p))))

    def roster(tid):
        return [pool[e["playerPoolEntry"]["player"]["id"]] for e in teams[tid]["roster"]["entries"]
                if e["lineupSlotId"] != IR_SLOT and e["playerPoolEntry"]["player"]["id"] in pool]

    ours, theirs = roster(TEAM_ID), roster(opp)
    ir = [e["playerPoolEntry"]["player"]["fullName"] for e in teams[TEAM_ID]["roster"]["entries"]
          if e["lineupSlotId"] == IR_SLOT]
    ours_by = {p: total(ours, p) for p in days}
    theirs_by = {p: total(theirs, p) for p in days}

    acq = league["settings"]["acquisitionSettings"]
    per = acq.get("matchupAcquisitionLimit", -1)
    limit = (per * len(in_matchup) if acq.get("matchupLimitPerScoringPeriod") else per) if per >= 0 else None
    used = (teams[TEAM_ID].get("transactionCounter") or {}).get("matchupAcquisitionTotals", {}).get(str(matchup), 0)

    names = {r["player"].lower(): r for r in ours}
    drops = ([names[n.lower()] for n in args.drop if n.lower() in names] if args.drop
             else [min(ours, key=rate)])
    missing = [n for n in (args.drop or []) if n.lower() not in names]
    if missing:
        sys.exit("Not on our active roster: " + ", ".join(missing))

    fa = [r for r in pool.values() if r["league"] == "FREEAGENT" and r["current"]
          and r["current"]["min"] >= args.min_minutes]
    fmt = lambda x: "—" if x is None else f"{x:.1f}"
    est = lambda r: (f'{feed[r["id"]]["status"].lower()}, ESPN est. {feed[r["id"]]["return"]:%d %b}'
                     if r["id"] in feed and feed[r["id"]]["return"] else
                     (feed[r["id"]]["status"].lower() if r["id"] in feed else ""))
    grid = lambda r: " | ".join("x" if plays(r, p) else ("o" if (r["pro"], p) in tips else "") for p in days)
    line = lambda r: (f'{r["current"]["gp"]}, {r["current"]["min"]:.1f}, {r["current"]["fpg"]:.1f}'
                      if r["current"] else "—")
    owner = lambda r: teams[r["owner"]]["name"].strip() if r.get("owner") else ""

    @lru_cache(maxsize=None)
    def team_boxes(tid):
        with ThreadPoolExecutor(8) as ex:
            return tuple(b["lines"].get(str(tid), {}) for b in ex.map(box, tipped.get(tid, [])))

    def starts(r):
        """Games started of games played this season, from ESPN's box scores."""
        games = [g[str(r["id"])] for g in team_boxes(r["pro"]) if str(r["id"]) in g]
        return f'{sum(g[2] for g in games)} of {len(games)}' if games else "—"

    out = [f"# Matchup {matchup}: {teams[TEAM_ID]['name'].strip()} vs {teams[opp]['name'].strip()}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/matchup.py`. This is **a report, not a council verdict**.",
           f"- **Score:** {us['totalPoints']:.0f} to {them['totalPoints']:.0f} "
           f"({'up' if us['totalPoints'] >= them['totalPoints'] else 'down'} "
           f"{abs(us['totalPoints'] - them['totalPoints']):.0f}). The matchup runs {monday:%a %d %b} to "
           f"{end:%a %d %b} (US dates), with {len(days)} days left.",
           f"- **Adds:** {used} used this matchup"
           + (f" of {limit:g}, so **{limit - used:g} left**." if limit is not None else ", no limit.")
           + " Free agents arrive at once; waiver players take 24 hours.",
           f"- **Method:** an exact optimiser fills the 10 starting slots each day. Rate per game: 70% this "
           "season's FP/g and 30% last season's (or ESPN's projection) at 3+ games, otherwise 50/50. A player "
           f"listed OUT is left out until ESPN's estimated return. Streamers need {args.min_minutes:g}+ minutes this season.",
           f"- **Checks:** {'**games were live** (--allow-live)' if live else 'no NBA game was in progress'}. "
           f"All {len(pool)} pool players re-score with `scripts/league_scoring.py` (0 mismatches).",
           f"- Times are ET and {args.tz.split('/')[-1].replace('_', ' ')}."]
    out += ([f"- **What-if:** treated as sitting: {', '.join(args.sit)}."] if args.sit else []) + [""]

    out += ["## The rest of the week", "",
            f"| Day (US) | {args.tz.split('/')[-1]} | Ours playing | Open slots | Our lineup | Theirs playing | Their lineup |",
            "|---|---|---:|---:|---:|---:|---:|"]
    for p in days:
        n_us = sum(plays(r, p) for r in ours)
        n_them = sum(plays(r, p) for r in theirs)
        a, b = label(p)
        out.append(f"| {a} | {b} | {n_us} | {max(0, len(SLOTS) - n_us)}{' (overfull)' if n_us > len(SLOTS) else ''} | "
                   f"{ours_by[p]:.0f} | {n_them} | {theirs_by[p]:.0f} |")
    rest_us, rest_them = sum(ours_by.values()), sum(theirs_by.values())
    out += ["", f"**Projection:** {rest_us:.0f} more for us and {rest_them:.0f} for them, for a final of "
            f"**{us['totalPoints'] + rest_us:.0f} to {them['totalPoints'] + rest_them:.0f}**.", ""]

    head = "| Player | NBA | Rate | " + " | ".join(label(p)[0][:6] for p in days) + " | Status |"
    rule = "|---|---|---:|" + ":-:|" * len(days) + "---|"
    out += ["## Our roster", "", "x = plays, o = has a game but is listed out.", "", head, rule]
    out += [f'| {r["player"]} | {abbrev.get(r["pro"])} | {rate(r):.1f} | {grid(r)} | {est(r)} |'
            for r in sorted(ours, key=rate, reverse=True)]
    if ir:
        out += ["", f"IR: {', '.join(ir)} (cannot score while in the IR slot)."]
    out += ["", "What each player adds this week: our lineup total with him, minus without him. Low numbers "
            "mean his games fall on days we are already full.", "",
            "| Player | Adds this week |", "|---|---:|"]
    adds = {r["player"]: sum(ours_by[p] - total([x for x in ours if x is not r], p) for p in days) for r in ours}
    out += [f"| {n} | {v:.1f} |" for n, v in sorted(adds.items(), key=lambda kv: kv[1])]
    out += ["", f"## {teams[opp]['name'].strip()}", "", head, rule]
    out += [f'| {r["player"]} | {abbrev.get(r["pro"])} | {rate(r):.1f} | {grid(r)} | {est(r)} |'
            for r in sorted(theirs, key=rate, reverse=True)]
    out.append("")

    shown = set()
    # A game that has already tipped can't be gained or lost by a roster move:
    # the dropped player keeps it, and a streamer added now can't get it.
    # ESPN won't drop a player once his game has started, so while the drop
    # candidate is locked, no streamer can arrive that day either.
    started = lambda r, p: (r["pro"], p) in tips and tips[(r["pro"], p)] <= now
    for d in drops:
        base = [r for r in ours if r is not d]
        stays = lambda p: ours if started(d, p) else base
        base_by = {p: total(stays(p), p) for p in days}
        keep = {p: ours_by[p] - base_by[p] for p in days}
        gain = {}
        for x in fa:
            m = {p: (total(stays(p) + [x], p) - base_by[p])
                 if plays(x, p) and not started(x, p) and not started(d, p) else 0.0 for p in days}
            if sum(m.values()) > 0:
                gain[x["id"]] = (x, m)
        ranked = sorted(gain.values(), key=lambda g: -sum(g[1].values()))
        out += [f"## Streaming {d['player']}'s slot", "",
                f"Keeping {d['player']} ({abbrev.get(d['pro'])}) is worth **{sum(keep.values()):.1f}** this week: "
                + ", ".join(f"{label(p)[0][:6]} {keep[p]:.0f}" for p in days if (d['pro'], p) in tips) + ".", "",
                "### One add, now", "",
                "| Free agent | NBA | Games | Now: GP, min, FP/g | Started | 2026 FP/g | Owned | vs keeping |",
                "|---|---|---|---|---|---:|---:|---:|"]
        for x, m in ranked[:args.top]:
            shown.add(x["pro"])
            gd = ", ".join(label(p)[0][:3] for p in days if plays(x, p) and not started(x, p) and not started(d, p))
            out.append(f'| **{x["player"]}**{" (" + est(x) + ")" if est(x) else ""} | {abbrev.get(x["pro"])} | {gd} | '
                       f'{line(x)} | {starts(x)} | {fmt(x["last"] and x["last"]["fpg"])} | {x["owned"]:.0f}% | '
                       f'**{signed(sum(m.values()) - sum(keep.values()), True)}** |')
        out += ["", "### Best streamer each day", "",
                "If the slot turns over daily, these are the best adds for each day alone.", ""]
        for p in days:
            top = sorted(gain.values(), key=lambda g: -g[1][p])[:4]
            out.append(f"- **{label(p)[0]}:** " + (", ".join(f'{x["player"]} ({abbrev.get(x["pro"])}, +{m[p]:.0f})'
                                                         for x, m in top if m[p] > 0.5) or "no streamer adds anything"))
        chains = []
        top_by = lambda span: sorted(gain.values(), key=lambda g: -sum(g[1][p] for p in span))[:25]
        for s in range(1, len(days)):
            a_span, b_span = days[:s], days[s:]
            for x, mx in top_by(a_span):
                for y, my in top_by(b_span):
                    if x is not y:
                        v = sum(mx[p] for p in a_span) + sum(my[p] for p in b_span) - sum(keep.values())
                        chains.append((v, x, y, b_span[0]))
        chains.sort(key=lambda c: -c[0])
        seen, picked = set(), []
        for c in chains:
            if (c[1]["id"], c[2]["id"]) not in seen:
                seen.add((c[1]["id"], c[2]["id"]))
                picked.append(c)
            if len(picked) == 5:
                break
        out += ["", "### Two adds in the slot", "",
                "The first streamer comes in now and is swapped out before the second one's first game.", "",
                "| First add | Until | Second add | From | vs keeping |", "|---|---|---|---|---:|"]
        for v, x, y, start in picked:
            shown.update({x["pro"], y["pro"]})
            prev = days[days.index(start) - 1]
            out.append(f'| {x["player"]} ({abbrev.get(x["pro"])}) | {label(prev)[0]} | {y["player"]} '
                       f'({abbrev.get(y["pro"])}) | {label(start)[0]} | **{signed(v, True)}** |')
        if ranked:
            x = ranked[0][0]
            plan = base + [x]
            out += ["", f"### Lineup with {x['player']} in the slot", "", "| Day | Lineup | Playing | Sits |", "|---|---:|---:|---|"]
            for p in days:
                day_roster = ours if started(d, p) else plan
                live_ = [r for r in day_roster if plays(r, p)]
                v = total(day_roster, p)
                sits = [r["player"] for r in live_ if len(live_) > len(SLOTS)
                        and abs(total([q for q in day_roster if q is not r], p) - v) < 1e-6]
                out.append(f'| {label(p)[0]} | {v:.0f} | {len(live_)} | {", ".join(sits) or "—"} |')
        out.append("")

    if args.rotate:
        origs, frees = [], []
        for spec in args.rotate:
            name, _, when = spec.partition("@")
            r = names.get(name.strip().lower())
            if r is None:
                sys.exit(f"Not on our active roster: {name}")
            on = dt.date.fromisoformat(when) if when else None
            free = next((p for p in days if (first[p].astimezone(ET).date() >= on if on else not started(r, p))), None)
            if free is None:
                sys.exit(f"No day left in this matchup when {name}'s slot can change.")
            origs.append(r)
            frees.append(free)
        n = len(origs)
        budget = int(limit - used) if limit is not None else len(days) * n
        rdays = [p for p in days if p >= min(frees)]
        empty = [r for r in ours if all(r is not o for o in origs)]
        counts = lambda r, p: plays(r, p) and not started(r, p)
        solo = {x["id"]: {p: total(empty + [x], p) - total(empty, p) if counts(x, p) else 0.0 for p in rdays}
                for x in fa}
        cands = sorted(fa, key=lambda x: -sum(solo[x["id"]].values()))[:args.pool]
        for p in rdays:  # one-day specialists, so a single big day is never missed
            cands += [x for x in sorted(fa, key=lambda x: -solo[x["id"]][p])[:3]
                      if solo[x["id"]][p] > 0 and all(x is not c for c in cands)]

        def rotate(origs, frees, keep=6):
            """Best moves through the slots at each add count: {adds: (total, moves)}, and keeping all.

            A slot changes only from its free day, and only before its occupant's game
            that day. A streamer scores games that haven't tipped. Nobody is added twice."""
            people = origs + cands
            rank = lambda v, moves: (round(v, 6), -sum(m[2] in origs for m in moves), -len(moves))
            @lru_cache(maxsize=None)
            def value(p, occ):
                return total(empty + [people[i] for i in occ if i < n or counts(people[i], p)], p)
            start = tuple(range(n))
            states = {(start, 0): [(0.0, frozenset(), ())]}
            for p in rdays:
                movers = [i for i in range(n, len(people)) if counts(people[i], p)]
                nxt = {}
                for (occ, adds), entries in states.items():
                    choices = [[occ[s]] + (movers if frees[s] is not None and p >= frees[s]
                                           and not started(people[occ[s]], p) else []) for s in range(n)]
                    for new in itertools.product(*choices):
                        changed = [s for s in range(n) if new[s] != occ[s]]
                        k = len(changed)
                        if adds + k > budget or len(set(new)) < n:
                            continue
                        day = value(p, tuple(sorted(new)))
                        for v, done, moves in entries:
                            if not any(new[s] in done for s in changed):
                                nxt.setdefault((new, adds + k), []).append(
                                    (v + day, done | {new[s] for s in changed},
                                     moves + tuple((p, s, people[occ[s]], people[new[s]]) for s in changed)))
                states = {}
                for key, entries in nxt.items():
                    entries.sort(key=lambda e: rank(e[0], e[2]), reverse=True)
                    seen, kept = set(), []
                    for e in entries:
                        if e[1] not in seen and len(kept) < keep:
                            seen.add(e[1])
                            kept.append(e)
                    states[key] = kept
            best = {}
            for (occ, adds), entries in states.items():
                for b in range(adds, budget + 1):
                    if b not in best or rank(*entries[0][::2]) > rank(*best[b]):
                        best[b] = (entries[0][0], entries[0][2])
            return best, sum(value(p, start) for p in rdays)

        best, hold = rotate(origs, frees)
        short = lambda r: r["player"].split(" ", 1)[-1]
        when = lambda p: f'{label(p)[0][:6]}'
        summary = lambda moves: "; ".join(f'{when(p)}: {short(a)} → {x["player"]} ({abbrev.get(x["pro"])})'
                                          for p, s, a, x in moves) or "keep"
        title = " and ".join(f"{o['player']}'s" for o in origs)
        out += [f"## Rotating {title} slot{'s' if n > 1 else ''}", "",
                "- Free from: " + ", ".join(f"{o['player']} {label(f)[0]}" for o, f in zip(origs, frees))
                + ". A slot can change from that US day, before its occupant's game that day.",
                f"- Each change is one add. {budget} left this matchup, usable on any day: the limit is a "
                "matchup total, not a daily cap.",
                f"- Streamers considered: the {len(cands)} free agents worth most to an empty slot over these days "
                f"(with {args.min_minutes:g}+ minutes), plus the top three for each day.",
                f"- Keeping {'both' if n == 2 else 'them'} scores **{hold:.0f}** in our lineup over "
                f"{label(rdays[0])[0]} to {label(rdays[-1])[0]}.", "",
                f"| Adds | vs keeping | Moves |", "|---:|---:|---|"]
        prev = None
        for b in range(1, budget + 1):
            if b in best and (prev is None or best[b][0] > prev + 0.05):
                out.append(f"| {len(best[b][1])} | **{signed(best[b][0] - hold, True)}** | {summary(best[b][1])} |")
                prev = best[b][0]
        top_total, top_moves = best[budget]
        for x in {id(x): x for _, _, _, x in top_moves}.values():
            shown.add(x["pro"])

        nxt_week = [q for q in first if end < first[q].astimezone(ET).date() <= end + dt.timedelta(days=7)]
        later = lambda r: sum((r["pro"], q) in tips for q in nxt_week)
        finale = {s: max((p for p in rdays if plays(o, p)), default=None) for s, o in enumerate(origs)}

        def kept(s):
            """The slots' free days with slot s held through its player's last game this week."""
            after = next((p for p in rdays if finale[s] is None or p > finale[s]), None)
            return [after if t == s else f for t, f in enumerate(frees)]

        out += ["", "Every drop of a player below is permanent: after his last game this week, dropping him still "
                "gains this week but costs his games next week ("
                + ", ".join(f"{o['player']} {later(o)}" for o in origs) + ").", ""]
        if n > 1:
            out += ["### Keep one, rotate the other", "",
                    "Keeping a player here means through his last game this week; his slot can still turn over after it.", "",
                    "| Scenario | Adds | vs keeping both |", "|---|---:|---:|"]
            out.append(f"| Rotate both | {len(top_moves)} | {signed(top_total - hold, True)} |")
            for s, o in enumerate(origs):
                alone, _ = rotate(origs, kept(s))
                until = f" through {label(finale[s])[0]}" if finale[s] is not None else ""
                out.append(f"| Keep {o['player']}{until}, rotate the rest | {len(alone[budget][1])} | "
                           f"{signed(alone[budget][0] - hold, True)} |")
                if kept(s)[s] is not None:
                    never, _ = rotate(origs, [None if t == s else f for t, f in enumerate(frees)])
                    out.append(f"| Keep {o['player']} all week (never drop), rotate the rest | {len(never[budget][1])} | "
                               f"{signed(never[budget][0] - hold, True)} |")
            out.append("")
        out += ["### Break-even", "",
                "The rate a player needs for keeping him through his last game this week to beat dropping him "
                "sooner, with the other slots rotating as above.", ""]
        for s, o in enumerate(origs):
            if kept(s)[s] is not None and kept(s)[s] <= frees[s]:
                out.append(f"- **{o['player']}**: no game left after his slot frees up, so there is nothing to weigh.")
                continue

            def moved(R, s=s):
                trial = [dict(q, rate=R) if t == s else q for t, q in enumerate(origs)]
                return rotate(trial, frees)[0][budget][0] > rotate(trial, kept(s))[0][budget][0] + 0.05
            lo, hi = 0.0, 90.0
            if not moved(lo):
                out.append(f"- **{o['player']}** (rate {rate(o):.1f}): keeping him wins at any rate.")
                continue
            if moved(hi):
                out.append(f"- **{o['player']}** (rate {rate(o):.1f}): streaming his slot wins at any rate.")
                continue
            for _ in range(8):
                mid = (lo + hi) / 2
                lo, hi = (mid, hi) if moved(mid) else (lo, mid)
            line_ = f"- **{o['player']}** (rate {rate(o):.1f}): keep him while his rate is above **{hi:.1f}**."
            before = [p for p in days if p < frees[s] and counts(o, p)]
            if before and o["current"]:
                c = o["current"]
                after = lambda g: rate(dict(o, current=dict(c, gp=c["gp"] + 1, fpg=(c["fpg"] * c["gp"] + g) / (c["gp"] + 1))))
                g_lo, g_hi = -20.0, 150.0
                if after(g_lo) >= hi:
                    line_ += f" No single game on {when(before[0])} takes him below it."
                elif after(g_hi) < hi:
                    line_ += f" No single game on {when(before[0])} lifts him above it."
                else:
                    for _ in range(30):
                        g = (g_lo + g_hi) / 2
                        g_lo, g_hi = (g, g_hi) if after(g) < hi else (g_lo, g)
                    line_ += (f" His {when(before[0])} game moves it: under **{g_hi:.0f} FP** "
                              f"(he averages {c['fpg']:.1f}) takes it below.")
            out.append(line_)

        occupants = list(origs)
        out += ["", f"### Best plan: {len(top_moves)} adds, {signed(top_total - hold, True)}", "",
                "| Day (US) | " + args.tz.split("/")[-1] + " | " + " | ".join(f"Slot {s + 1}" for s in range(n))
                + " | Our lineup | vs keeping | Sits |",
                "|---|---|" + "---|" * n + "---:|---:|---|"]
        for p in rdays:
            for q, s, a, x in top_moves:
                if q == p:
                    occupants[s] = x
            scoring = [r for r in empty if plays(r, p)] + [o for t, o in enumerate(occupants)
                                                         if (counts(o, p) if o is not origs[t] else plays(o, p))]
            v = best_lineup(tuple(sorted((rate(r), slots_for(r)) for r in scoring)))
            k = best_lineup(tuple(sorted((rate(r), slots_for(r)) for r in empty + origs if plays(r, p))))
            sits = [r["player"] for r in scoring if len(scoring) > len(SLOTS) and abs(best_lineup(tuple(sorted(
                (rate(q), slots_for(q)) for q in scoring if q is not r))) - v) < 1e-6]
            cell = lambda o, t: (f'{o["player"]} ({abbrev.get(o["pro"])})'
                                 + (" plays" if (counts(o, p) if o is not origs[t] else plays(o, p)) else ", idle"))
            out.append(f"| {label(p)[0]} | {label(p)[1]} | " + " | ".join(cell(o, t) for t, o in enumerate(occupants))
                       + f" | {v:.0f} | {signed(v - k, True)} | {', '.join(sits) or '—'} |")
        out += ["", "Moves, each made before the earlier tip-off of the two players that day:", ""]
        for i, (p, s, a, x) in enumerate(top_moves, 1):
            by = min(tips[(r["pro"], p)] for r in (a, x) if (r["pro"], p) in tips)
            out.append(f'{i}. **{label(p)[0]}:** drop {a["player"]}, add **{x["player"]}** ({abbrev.get(x["pro"])}; '
                       f'GP, min, FP/g {line(x)}; started {starts(x)}{"; " + est(x) if est(x) else ""}). By {by.astimezone(ET):%I:%M%p} ET / '
                       f'{by.astimezone(local):%a %d %I:%M%p}.'
                       + (f' Losing {a["player"]} also costs his {later(a)} games next week.' if any(a is o for o in origs) else ''))
        out += ["", "Left holding at the end of the week: " + ", ".join(
            f'{o["player"]} ({abbrev.get(o["pro"])}, {later(o)} games next week)'
            for o in occupants) + ".", ""]

    out += ["## Tip-off times", "", f"For the teams named above. Times are ET / {args.tz.split('/')[-1].replace('_', ' ')}.", ""]
    for tid in sorted(shown | {d["pro"] for d in drops}, key=lambda t: abbrev.get(t, "")):
        out.append(f"- **{abbrev.get(tid)}:** " + "; ".join(
            f'{tips[(tid, p)].astimezone(ET):%a %d %I:%M%p} / {tips[(tid, p)].astimezone(local):%a %d %I:%M%p}'
            for p in days if (tid, p) in tips))
    out += ["", "## Sources", "",
            f"- ESPN fantasy API, league 423671879 (`mRoster`, `mTeam`, `mMatchupScore`, `mSettings`, `mStatus`, "
            f"`kona_player_info`, `proTeamSchedules_wl`) and ESPN's NBA injury feed, read {now:%Y-%m-%d %H:%M} UTC.", ""]

    report = "\n".join(out)
    if args.out:
        Path(args.out).write_text(report)
        print(f"Wrote {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
