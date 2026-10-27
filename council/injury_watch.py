#!/usr/bin/env python3
"""Injury Watch: who is out, who takes their minutes, and who we could add.

Stdlib only and read-only against ESPN. It uses the same two cookies as
council/espn_sync.py.

It looks at every NBA player out longer than --min-days (default 7) who has a
real role. For each one it reads the team's last --games box scores and splits
every teammate's minutes, league-scored FP and starts into two groups:
  - games without the absentees
  - games with them
When the absence predates the season, there are no games with them, so the
comparison is against ESPN's projection instead. From that split it reports:
  - the best-placed replacements on each team
  - free agents and waiver players among them, set against our weakest players
  - injured free agents and waiver players due back within --soon days (default 14)
  - our own injured players
  - every injury in the league, with ESPN's estimated return

Guards, as in slump_watch.py:
  - It refuses to run while NBA games are live. --allow-live overrides this.
  - Every season average must re-score with scripts/league_scoring.py to
    ESPN's total.
Finished box scores never change, so they are cached in council/.cache/box/
(gitignored).

ESPN's return date is an estimate. The skill adds the reported timeline
beside it (CLAUDE.md).

Usage:
  python council/injury_watch.py
  python council/injury_watch.py --out docs/analysis/20261027-injury-watch.md
  python council/injury_watch.py --min-days 7 --soon 14 --games 10
"""
import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from injuries import injuries as injury_feed  # noqa: E402
from slump_watch import (ET, FANTASY, LEAGUE, SITE, SPLIT, TEAM_ID, box_points,  # noqa: E402
                         fantasy_points, get, live_games, signed, stat)

CACHE = ROOT / ".cache" / "box"
POS = {0: "PG", 1: "SG", 2: "SF", 3: "PF", 4: "C"}
ROLE_MIN = 15    # minutes a game that make an absence matter
PICKUP_MIN = 18  # minutes a game a pickup must be getting without the absentees
GAIN_MIN = 3     # minutes gained that count as a bigger role


def player_pool():
    """Every player in the league pool with league-scored splits and league status."""
    filt = {"players": {"filterStatus": {"value": ["FREEAGENT", "WAIVERS", "ONTEAM"]}, "limit": 1500,
                        "sortPercOwned": {"sortPriority": 1, "sortAsc": False},
                        "filterStatsForTopScoringPeriodIds": {"value": 2, "additionalValue": list(SPLIT.values())}}}
    data = get(f"{LEAGUE}?view=kona_player_info", cookies=True, fantasy_filter=filt)
    rows, mismatches = {}, []
    for e in data["players"]:
        p = e["player"]
        splits = {s["id"]: s for s in p.get("stats", [])}
        r = {"id": p["id"], "player": p["fullName"], "pro": p["proTeamId"], "league": e["status"],
             "owner": e.get("onTeamId") if e["status"] == "ONTEAM" else None,
             "owned": (p.get("ownership") or {}).get("percentOwned", 0), "status": p.get("injuryStatus", ""),
             "pos": "/".join(POS[s] for s in sorted(p.get("eligibleSlots", [])) if s in POS)}
        for name, sid in SPLIT.items():
            s = splits.get(sid)
            if not s or stat(s["stats"], "GP") == 0:
                r[name] = None
                continue
            total = fantasy_points(s["stats"])
            if s.get("appliedTotal") is not None and abs(total - s["appliedTotal"]) > 0.01:
                mismatches.append(f'{p["fullName"]} {name}: {total} vs ESPN {s["appliedTotal"]}')
            gp = stat(s["stats"], "GP")
            r[name] = {"gp": int(gp), "fpg": total / gp, "min": stat(s["stats"], "MIN") / gp}
        rows[p["id"]] = r
    return rows, mismatches


def box(gid):
    """{team id: {player id: [minutes, FP, started]}} for one game, cached once final."""
    path = CACHE / f"{gid}.json"
    if path.exists():
        return json.loads(path.read_text())
    s = get(f"{SITE}/summary?event={gid}")
    final = s["header"]["competitions"][0]["status"]["type"]["state"] == "post"
    lines = {}
    for team in s.get("boxscore", {}).get("players", []):
        block, played = team["statistics"][0], {}
        for a in block["athletes"]:
            v = dict(zip(block["keys"], a.get("stats") or []))
            if str(v.get("minutes", "")).isdigit():  # DNPs carry no stats, or "--"
                played[str(a["athlete"]["id"])] = [int(v["minutes"]), box_points(v), bool(a.get("starter"))]
        lines[str(team["team"]["id"])] = played
    out = {"final": final, "lines": lines}
    if final:
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(out))
    return out


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def team_split(games, absentees, team_id, pool):
    """Each teammate's role in games without every absentee, against games with any (or projection)."""
    without, with_ = [], []
    for g in games:
        lines = g["lines"].get(str(team_id), {})
        (without if all(str(a) not in lines for a in absentees) else with_).append(lines)
    seen = defaultdict(lambda: {"wo": [], "w": []})
    for key, group in (("wo", without), ("w", with_)):
        for lines in group:
            for pid, line in lines.items():
                seen[int(pid)][key].append(line)
    mates = []
    missing = lambda pid: all(str(pid) not in lines for lines in without)
    for pid, s in seen.items():
        if pid in absentees or not s["wo"]:
            continue
        r = pool.get(pid, {"id": pid, "player": str(pid), "league": "?", "owner": None, "owned": 0,
                           "status": "", "pos": "", "current": None, "projected": None, "last": None})
        wo_min, wo_fp = mean([x[0] for x in s["wo"]]), mean([x[1] for x in s["wo"]])
        if s["w"]:
            base, base_min, base_fp = "with", mean([x[0] for x in s["w"]]), mean([x[1] for x in s["w"]])
        elif r.get("projected"):
            base, base_min, base_fp = "projection", r["projected"]["min"], r["projected"]["fpg"]
        else:
            base, base_min, base_fp = None, None, None
        mates.append({**r, "n_wo": len(s["wo"]), "wo_min": wo_min, "wo_fp": wo_fp,
                      "wo_starts": sum(x[2] for x in s["wo"]), "base": base, "base_min": base_min,
                      "base_fp": base_fp, "gain": None if base_min is None else wo_min - base_min})
    return len(without), len(with_), mates, missing


def available(r):
    return r.get("league") in ("FREEAGENT", "WAIVERS")


def league_label(r, teams):
    if r.get("league") == "ONTEAM":
        return "**us**" if r["owner"] == TEAM_ID else teams.get(r["owner"], "rostered")
    return {"FREEAGENT": "Free agent", "WAIVERS": "Waivers"}.get(r.get("league"), "—")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--min-days", type=int, default=7, help="an absence counts when ESPN's return is further out (default 7)")
    ap.add_argument("--soon", type=int, default=14, help="'back soon' window in days (default 14)")
    ap.add_argument("--games", type=int, default=10, help="recent team games to read (default 10)")
    ap.add_argument("--pickup-fp", type=float, default=20, help="FP/g without the absentees a pickup needs (default 20)")
    ap.add_argument("--value", type=float, default=25, help="FP/g that makes a returning player worth listing (default 25)")
    ap.add_argument("--absent", nargs="*", default=[], metavar="NAME",
                    help="treat these injured players as long absences whatever ESPN estimates "
                         "(for reported 'no timetable' cases)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")

    now = dt.datetime.now(dt.timezone.utc)
    today = now.astimezone(ET).date()
    feed = injury_feed()
    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches[:20]))
    league = get(f"{LEAGUE}?view=mTeam&view=mRoster", cookies=True)
    teams = {t["id"]: t["name"].strip() for t in league["teams"]}
    ours = next(t for t in league["teams"] if t["id"] == TEAM_ID)["roster"]["entries"]
    ir_used = [e["playerPoolEntry"]["player"]["fullName"] for e in ours if e["lineupSlotId"] == 13]
    pro_teams = get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
    abbrev = {t["id"]: t["abbrev"] for t in pro_teams}
    schedule = {t["id"]: sorted({(g["date"], g["id"]) for gs in t.get("proGamesByScoringPeriod", {}).values()
                                 for g in gs}) for t in pro_teams}

    monday = today - dt.timedelta(days=today.weekday())
    weeks = [(monday, monday + dt.timedelta(days=7)), (monday + dt.timedelta(days=7), monday + dt.timedelta(days=14))]
    stamp = now.timestamp() * 1000
    left = {tid: tuple(sum(1 for d, _ in games if d > stamp and a <= dt.datetime.fromtimestamp(d / 1000, ET).date() < b)
                       for a, b in weeks) for tid, games in schedule.items()}

    def back(i):
        return (i["return"] - today).days if i["return"] else None

    def role(pid):
        r = pool.get(pid) or {}
        return max([r[k]["min"] for k in ("current", "projected", "last") if r.get(k)] or [0])

    forced = {n.lower() for n in args.absent}
    unknown = forced - {i["player"].lower() for i in feed.values()}
    if unknown:
        sys.exit("Not in ESPN's injury feed: " + ", ".join(sorted(unknown)))
    out_long = {pid: i for pid, i in feed.items() if role(pid) >= ROLE_MIN and (
                i["player"].lower() in forced
                or ((back(i) is None or back(i) > args.min_days) and i["status"].lower() != "day-to-day"))}
    by_team = defaultdict(list)
    for pid, i in out_long.items():
        by_team[i["team_id"]].append(pid)

    recent = {tid: [gid for d, gid in schedule.get(tid, []) if d < stamp][-args.games:] for tid in by_team}
    gids = sorted({g for gs in recent.values() for g in gs})
    with ThreadPoolExecutor(8) as ex:
        boxes = dict(zip(gids, ex.map(box, gids)))

    our = sorted((r for r in pool.values() if r["owner"] == TEAM_ID and r["current"]), key=lambda r: r["current"]["fpg"])
    floor = our[min(4, len(our) - 1)]["current"]["fpg"] if our else 0
    fmt = lambda x: "—" if x is None else f"{x:.1f}"
    est = lambda i: "—" if not i["return"] else f'{i["return"]:%d %b}' + (
        f' {i["return"].year}' if i["return"].year != today.year and i["return"].month >= today.month else "")
    status = lambda r: {"ACTIVE": "", "": ""}.get(r["status"], f' ({r["status"].replace("_", " ").lower()}'
                                                  + (f', ESPN est. back {est(feed[r["id"]])}' if r["id"] in feed else "") + ")")

    sections, pickups = [], []
    for tid in sorted(by_team, key=lambda t: -sum(role(p) for p in by_team[t])):
        absent = by_team[tid]
        games = [boxes[g] for g in recent[tid] if boxes[g]["final"]]
        split_on, note = absent, ""
        n_wo, n_w, mates, missing = team_split(games, set(absent), tid, pool)
        if not n_wo and len(absent) > 1:
            for pid in sorted(absent, key=role, reverse=True):
                n_wo, n_w, mates, missing = team_split(games, {pid}, tid, pool)
                if n_wo:
                    split_on = [pid]
                    note = f' Split on {feed[pid]["player"]} alone: the others still played in those games.'
                    break
        also = [i for p, i in feed.items() if i["team_id"] == tid and p not in absent and role(p) >= ROLE_MIN
                and n_wo and missing(p)]
        sec = [f"### {abbrev.get(tid, tid)}", "",
               "| Out | Injury | ESPN est. | Min left | Season FP/g | League |", "|---|---|---|---:|---:|---|"]
        for pid in sorted(absent, key=role, reverse=True):
            i, r = feed[pid], pool.get(pid, {})
            sec.append(f'| {i["player"]} | {i["injury"]} | {est(i)} | {role(pid):.1f} | '
                       f'{fmt((r.get("current") or r.get("last") or {}).get("fpg"))} | {league_label(r, teams)} |')
        basis = (f"{n_wo} game(s) without them, {n_w} with them" if n_w else
                 f"{n_wo} game(s) this season, all without them; compared with ESPN's projection")
        sec += ["", f"Last {len(games)} games: {basis}.{note}"]
        if also:
            sec += ["", "Also out in those games, so part of the gain is theirs: " + ", ".join(
                f'{i["player"]} ({i["injury"].lower()}; ESPN est. {est(i)})' for i in also) + "."]
        sec.append("")
        best = sorted((m for m in mates if m["wo_min"] >= 12 and (m["gain"] is None or m["gain"] >= GAIN_MIN)),
                      key=lambda m: -m["wo_fp"])[:5]
        if not n_wo:
            same = {p for pid in absent for p in (pool.get(pid, {}).get("pos") or "").split("/") if p}
            inline = sorted((r for r in pool.values() if r["pro"] == tid and r["id"] not in absent and r["current"]
                             and same & set(r["pos"].split("/"))), key=lambda r: -r["current"]["min"])[:4]
            sec.append("No game yet without them. Same-position teammates by current minutes: "
                       + ", ".join(f'{r["player"]} ({r["pos"]}, {r["current"]["min"]:.1f} min, '
                                   f'{r["current"]["fpg"]:.1f} FP/g, {league_label(r, teams)})' for r in inline) + ".")
        elif best:
            sec += ["| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |",
                    "|---|---|---:|---:|---:|---:|---:|---:|---|---:|"]
            for m in best:
                sec.append(f'| {m["player"]}{status(m)} | {m["pos"]} | {m["n_wo"]} | {m["wo_min"]:.1f} | '
                           f'{"—" if m["gain"] is None else signed(m["gain"], True)} | {m["wo_starts"]} | '
                           f'**{m["wo_fp"]:.1f}** | {fmt(m["base_fp"])} | {league_label(m, teams)} | {m["owned"]:.0f}% |')
                if available(m) and m["wo_min"] >= PICKUP_MIN and m["wo_fp"] >= args.pickup_fp:
                    pickups.append({**m, "team": tid, "absent": split_on, "also": also})
        else:
            sec.append("No teammate has gained 3+ minutes in those games.")
        sections += sec + [""]

    soon = sorted((({**pool[pid], "inj": i}) for pid, i in feed.items() if pid in pool and available(pool[pid])
                   and back(i) is not None and 0 <= back(i) <= args.soon
                   and max([pool[pid][k]["fpg"] for k in ("current", "projected", "last") if pool[pid].get(k)] or [0]) >= args.value),
                  key=lambda r: -max(r[k]["fpg"] for k in ("current", "projected", "last") if r.get(k)))

    hdr = [f"# Injury Watch: {now:%d %b %Y}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.",
           f"- **Injuries:** {len(feed)} players in ESPN's injury feed. {len(out_long)} are out more than "
           f"{args.min_days} days (ESPN est.) with a role of {ROLE_MIN}+ minutes, on {len(by_team)} teams"
           + (f"; {', '.join(sorted(args.absent))} included as long absences on reported timelines." if args.absent else "."),
           f"- **Method:** each team's last {args.games} finished games, re-scored from ESPN's box scores. Each "
           "teammate's minutes and FP are split into games without the absentees against games with them, or "
           "against ESPN's projection when they have been out all season.",
           f"  - *Best placed* means {GAIN_MIN}+ minutes gained, ordered by FP/g in the games without the absentees.",
           f"  - A pickup is a free agent or waiver player getting {PICKUP_MIN}+ minutes in those games.",
           f"- **Checks:** {'**games were live** (--allow-live): ' + '; '.join(live) if live else 'no NBA game was in progress'}. "
           f"All {len(pool)} pool players re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).",
           f"- **Games** is games left this week ({weeks[0][0]:%d %b}–{weeks[0][1] - dt.timedelta(days=1):%d %b}) / "
           f"next week ({weeks[1][0]:%d %b}–{weeks[1][1] - dt.timedelta(days=1):%d %b}).",
           "- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.", ""]

    body = ["## Pickups for us", "",
            f"Free agents and waiver players getting {PICKUP_MIN}+ minutes and {args.pickup_fp:g}+ FP/g since an absence "
            "opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences "
            "in the same games, which inflate the gain until those players return.", "",
            f"Our five lowest current FP/g: " + ", ".join(f'{r["player"]} {r["current"]["fpg"]:.1f}' for r in our[:5])
            + f". A pickup at or above **{floor:.1f}** beats all five.", ""]
    if pickups:
        body += ["| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | League | Owned | Games |",
                 "|---|---|---|---:|---:|---:|---:|---:|---|---:|---|"]
        for m in sorted(pickups, key=lambda m: -m["wo_fp"]):
            opening = ", ".join(f'{feed[p]["player"]} ({est(feed[p])})' for p in m["absent"])
            if m["also"]:
                opening += "; also out: " + ", ".join(f'{i["player"]} ({est(i)})' for i in m["also"])
            body.append(f'| **{m["player"]}**{status(m)} | {abbrev.get(m["team"])} | {opening} | {m["n_wo"]} | '
                        f'{m["wo_min"]:.1f} | {"—" if m["gain"] is None else signed(m["gain"], True)} | '
                        f'**{m["wo_fp"]:.1f}** | {fmt(m["current"] and m["current"]["fpg"])} | '
                        f'{league_label(m, teams)} | {m["owned"]:.0f}% | {left[m["team"]][0]} / {left[m["team"]][1]} |')
    else:
        body.append("None this time.")
    body += ["", "## Injured and available, back soon", "",
             f"Free agents and waiver players ESPN expects back within {args.soon} days, worth {args.value:g}+ FP/g "
             "on their current, projected or last-season average.", "",
             f'- **Our IR slot:** {"taken by " + ", ".join(ir_used) if ir_used else "free"}. '
             + ("A stash costs a bench spot until it frees up." if ir_used else "A stash can go straight to IR."), ""]
    if soon:
        body += ["| Player | NBA | Injury | ESPN est. | Days | Current FP/g | Projected | 2026 | League | Owned | Games |",
                 "|---|---|---|---|---:|---:|---:|---:|---|---:|---|"]
        for r in soon:
            i = r["inj"]
            body.append(f'| **{r["player"]}** | {abbrev.get(r["pro"])} | {i["injury"]} | {est(i)} | {back(i)} | '
                        f'{fmt(r["current"] and r["current"]["fpg"])} | {fmt(r["projected"] and r["projected"]["fpg"])} | '
                        f'{fmt(r["last"] and r["last"]["fpg"])} | {league_label(r, teams)} | {r["owned"]:.0f}% | '
                        f'{left[r["pro"]][0]} / {left[r["pro"]][1]} |')
    else:
        body.append("None this time.")

    mine = [(pool[pid], i) for pid, i in feed.items() if pid in pool and pool[pid]["owner"] == TEAM_ID]
    body += ["", "## Our injured players", ""]
    body += [f'- **{r["player"]}** ({abbrev.get(r["pro"])}): {i["status"]}, {i["injury"]}; ESPN est. back {est(i)}.'
             for r, i in mine] or ["None."]
    body += ["", "## Who takes the minutes, team by team", ""] + sections

    body += ["## Every injury", "", f"All {len(feed)} players in ESPN's injury feed, longest expected absence first.", "",
             "| Player | NBA | Status | Injury | ESPN est. | Days | League |", "|---|---|---|---|---|---:|---|"]
    for i in sorted(feed.values(), key=lambda i: (i["return"] or dt.date.max, i["player"]), reverse=True):
        r = pool.get(i["id"], {})
        body.append(f'| {i["player"]} | {abbrev.get(i["team_id"], i["nba"])} | {i["status"]} | {i["injury"]} | '
                    f'{est(i)} | {"—" if back(i) is None else back(i)} | {league_label(r, teams)} |')
    body += ["", "## Sources", "",
             f"- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 "
             f"(`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read {now:%Y-%m-%d %H:%M} UTC.", ""]

    report = "\n".join(hdr + body)
    if args.out:
        Path(args.out).write_text(report)
        print(f"Wrote {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
