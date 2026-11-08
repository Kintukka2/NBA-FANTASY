#!/usr/bin/env python3
"""News Watch: ESPN's player news, checked against its injury labels and the box scores.

Stdlib only and read-only. The rate (council/gamelog.py) is built from games
already played, so it misses what the news knows first. This script reads the
news ESPN's fantasy app shows for each player (RotoWire's notes) and flags:

  injury   ESPN's injury label or return date disagrees with the news: ESPN
           expects him back within a week but the news talks of weeks, no
           timetable, surgery or a re-evaluation; ESPN's date has passed and he
           is still out; he played after being listed out; the news points to a
           return ESPN has not caught up with; or the news names an injury ESPN
           does not list.
  role     the box scores show him moving into or out of the starting lineup,
           or the news announces it.
  minutes  his last 3 games' minutes are 5+ off his season's, or the news
           mentions a minutes limit or a bigger or smaller role.
  rest     his team plays a back-to-back in the days ahead and he has a rest
           signal: the news mentions rest or load management, or he sat one
           night of an earlier back-to-back while playing the other.
  gap      ESPN lists him out with no return date, or with no news for days.

Role rate: FP per minute this season (outlier games left out, as in
council/gamelog.py) times his minutes in the new role (his starts, his bench
games, or his last 3 games). It is shown beside the rate, never in place of
it: council/matchup.py only uses it once the news watch research confirms the
role and records it in council/news_overrides.csv.

council/news_overrides.csv holds what the research confirmed, one row each:
  return  value YYYY-MM-DD: first day he can play. Out before it, whatever ESPN says.
  sit     value YYYY-MM-DD: a day he will not play (rest, suspension, personal).
  role    value minutes: his expected minutes. The plans use his role rate.
          'until' (YYYY-MM-DD) is required: re-check the role by then.
A row stops applying once its date (or 'until') has passed. The matchup plans
read the file; this report lists what is in force and what has expired.

Scope: our roster, every other team's roster, and the top --fa free agents and
waiver players by rate. It refuses to run while games are live (the rate
would include half-played games); --allow-live overrides that.

Usage:
  python council/news_watch.py
  python council/news_watch.py --out docs/analysis/20261108-news-watch.md --json flags.json
  python council/news_watch.py --ours            # our roster only
"""
import argparse
import csv
import datetime as dt
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from slump_watch import (ET, FANTASY, LEAGUE, TEAM_ID, get, live_games, signed,  # noqa: E402
                         window_cells, season_cell)

NEWS = "https://site.api.espn.com/apis/fantasy/v2/games/fba/news/players?limit={n}&playerId={pid}"
OVERRIDES = ROOT / "news_overrides.csv"
FIELDS = ["player", "kind", "value", "until", "source", "note"]

LONG = re.compile(r"multi-week|several weeks|\bweeks\b|week-to-week|indefinite(ly)?|no (set )?(timetable|timeline)|"
                  r"without a (timetable|timeline)|re-?evaluat\w*|surgery|surgical|season-ending|rest of the season|"
                  r"for the season|extended (absence|period)|significant time|\bMRI\b|torn|\btear\b|fracture", re.I)
BACK = re.compile(r"\b(cleared|available|will play|expected to play|probable|upgraded|returns? to action|"
                  r"returned to action|will return|set to return|making his return|good to go|will make his)\b", re.I)
HURT = re.compile(r"\b(ruled out|won't play|will not play|doubtful|questionable|game-time decision|did not return|"
                  r"won't return|will not return|exited|listed as out|is out|will miss|sidelined|day-to-day)\b", re.I)
ROLE = re.compile(r"\b(will start|starting lineup|first unit|starting five|move\w* (back )?to the bench|"
                  r"(enter|join)\w* the starting|replace\w* .{0,60}?in the (starting lineup|first unit)|"
                  r"out of the rotation|coach'?s decision|sixth man|bench role|reserve role)", re.I)
MINUTES = re.compile(r"minutes? (restriction|limit|cap)|limited minutes|on a minutes|ramp(ing)? up", re.I)
BIGGER = re.compile(r"(increased|expanded|bigger|larger|reduced|smaller|diminished) role", re.I)  # headlines only
REST = re.compile(r"\bresting\b|\brested\b|\brest\b(?! of)|load management|back-to-back|maintenance|"
                  r"injury management|night off|second night", re.I)
NEGATION = re.compile(r"(\bnot|n't|\bno|\bun)\s*$", re.I)
OTHER_INJURY = re.compile(r"\b([A-Z][\w'.-]+) \([a-z][^)]{0,30}\)")  # "Quickley (hamstring)": someone's injury
SUFFIXES = {"Jr.", "Sr.", "II", "III", "IV", "V"}


def last_name(name):
    parts = [p for p in name.split() if p not in SUFFIXES]
    return parts[-1] if parts else name


def about(text, last):
    """The sentences of a note that are not about another player's injury."""
    keep = []
    for s in re.split(r"(?<=[.!?])\s+", text or ""):
        others = [m.group(1) for m in OTHER_INJURY.finditer(s) if m.group(1) != last]
        if not others:
            keep.append(s)
    return " ".join(keep)


def hits(rx, text):
    """Snippets around each match of rx in text, skipping negated ones ('not available')."""
    out = []
    for m in rx.finditer(text or ""):
        if NEGATION.search(text[max(0, m.start() - 6):m.start()]):
            continue
        lo, hi = text.rfind(".", 0, m.start()) + 1, text.find(".", m.end())
        out.append(text[lo:hi if hi > 0 else len(text)].strip())
    return list(dict.fromkeys(out))


def news(pid, n=50, keep=12):
    """The RotoWire notes in ESPN's fantasy news for one player, newest first: [{date, headline, story}].

    The feed mixes in highlight clips and ESPN articles, which are left out."""
    try:
        feed = get(NEWS.format(n=n, pid=pid)).get("feed", [])
    except SystemExit:  # one player's feed failing should not end the run
        return []
    clean = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s or "")).strip()
    notes = [{"date": dt.datetime.fromisoformat(x["published"].replace("Z", "+00:00")),
              "headline": clean(x.get("headline")), "story": clean(x.get("story"))}
             for x in feed if x.get("published") and (x.get("type") or "").lower() == "rotowire"]
    return sorted(notes, key=lambda x: x["date"], reverse=True)[:keep]


def load_overrides(today, path=OVERRIDES):
    """(rows in force, rows expired) from council/news_overrides.csv."""
    if not path.exists():
        return [], []
    live, old = [], []
    for row in csv.DictReader(path.open(newline="", encoding="utf-8")):
        row = {k: (v or "").strip() for k, v in row.items()}
        kind = row["kind"].lower()
        try:
            last = dt.date.fromisoformat(row["until"]) if row.get("until") else None
            day = dt.date.fromisoformat(row["value"]) if kind in ("return", "sit") else None
            if kind == "role":
                float(row["value"])
        except ValueError:
            sys.exit(f"news_overrides.csv: bad row {row}")
        if kind not in ("return", "sit", "role") or (kind == "role" and not last):
            sys.exit(f"news_overrides.csv: bad row {row} (kind is return, sit or role; role needs 'until')")
        gone = (kind == "return" and day <= today) or (kind == "sit" and day < today) or (last and last < today)
        (old if gone else live).append(dict(row, kind=kind))
    return live, old


def overrides(today, path=OVERRIDES):
    """{player name, lower case: {'return': date, 'sit': {dates}, 'role': minutes, 'rows': [...]}} in force."""
    out = {}
    for row in load_overrides(today, path)[0]:
        o = out.setdefault(row["player"].lower(), {"sit": set(), "rows": []})
        o["rows"].append(row)
        if row["kind"] == "return":
            o["return"] = max(o.get("return", dt.date.min), dt.date.fromisoformat(row["value"]))
        elif row["kind"] == "sit":
            o["sit"].add(dt.date.fromisoformat(row["value"]))
        else:
            o["role"] = float(row["value"])
    return out


def fp_per_min(r, log):
    """FP per minute this season with the outlier games left out (council/gamelog.py)."""
    from gamelog import outliers
    drops = r.get("drops") if r.get("log") else outliers(log)
    kept = [g for g in log if g[3] not in (drops or {})]
    if kept and sum(g[1] for g in kept):
        return sum(g[2] for g in kept) / sum(g[1] for g in kept)
    cur = r.get("current")
    return cur["fpg"] / cur["min"] if cur and cur.get("min") else None


def role_rate(r, minutes, log=None):
    """FP per minute this season times the given minutes, or None."""
    fpm = fp_per_min(r, log if log is not None else (r.get("log") or []))
    return fpm * minutes if fpm is not None else None


def schedules(now):
    """({pro team: sorted ET dates of its games}, {game id: ET date})."""
    teams, days = {}, {}
    for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]:
        for gs in t.get("proGamesByScoringPeriod", {}).values():
            for g in gs:
                day = dt.datetime.fromtimestamp(g["date"] / 1000, ET).date()
                teams.setdefault(t["id"], set()).add(day)
                days[g["id"]] = day
    return {k: sorted(v) for k, v in teams.items()}, days


def back_to_backs(dates):
    """[(first night, second night)] in a sorted list of dates."""
    return [(a, b) for a, b in zip(dates, dates[1:]) if (b - a).days == 1]


def check(r, items, inj, log, starts, team_days, today, args):
    """The flags for one player: [(kind, signal)], plus his role rate (or None)."""
    flags, rrate, last = [], None, last_name(r["player"])
    day = lambda x: x["date"].astimezone(ET).date()
    recent = [x for x in items if (today - day(x)).days <= args.days]
    head = lambda x: x["headline"]
    body = lambda x: about(f'{x["headline"]} {x["story"]}', last)

    def said(rx, xs, part):
        """'on 05 Nov: "..."' from the newest note in xs whose part matches rx, or ''."""
        for x in xs:  # newest first
            h = hits(rx, part(x))
            if h:
                return f'on {day(x):%d %b}: "{h[0]}"'
        return ""
    played = [g[0] for g in log]

    # injury: ESPN's label and date against its own news
    if inj:
        status, ret = inj["status"].lower(), inj["return"]
        upd = dt.date.fromisoformat(inj["updated"])
        since = [x for x in items if day(x) >= upd - dt.timedelta(days=1)] or recent
        long = said(LONG, since, body)
        if long and (ret is None or (ret - today).days <= args.soon):
            flags.append(("injury", (f"ESPN est. {ret:%d %b}" if ret else "ESPN has no return date")
                          + f' ({inj["status"]}, {inj["injury"]}, updated {upd:%d %b}), but the news said {long}'))
        if status == "out" and ret and ret < today:
            flags.append(("injury", f"ESPN's return date ({ret:%d %b}) has passed and he is still listed out"))
        if status == "out" and played and played[-1] > upd:
            flags.append(("injury", f"listed out since {upd:%d %b}, but he played on {played[-1]:%d %b}"))
        back = said(BACK, [x for x in items if day(x) > upd], head)
        if status == "out" and back:
            flags.append(("injury", (f"listed out (ESPN est. {ret:%d %b})" if ret else "listed out (no ESPN date)")
                          + f", but newer news said {back}"))
        if status == "out" and ret is None:
            flags.append(("gap", "listed out with no ESPN return date"))
        if (status == "out" and (ret is None or (ret - today).days <= 14)
                and not [x for x in items if (today - day(x)).days <= args.stale]):
            flags.append(("gap", f"listed out, and no news in {args.stale} days"
                          + (f" (ESPN est. {ret:%d %b})" if ret else "")))
    else:  # a fresh injury note that ESPN's feed has not caught, and no game since
        fresh = [x for x in items if (today - day(x)).days <= 2 and (not played or day(x) >= played[-1])]
        hurt = said(HURT, fresh, head)
        if hurt:
            flags.append(("injury", f"not in ESPN's injury feed, but the news said {hurt}"))

    # role: into or out of the starting lineup
    if len(starts) >= 4:
        two, before = starts[-2:], starts[:-2]
        share = sum(before) / len(before)
        season_min = sum(g[1] for g in log) / len(log)
        if any(two) and share <= 0.25:
            mins = [g[1] for g, s in zip(log, starts) if s]
            rrate = role_rate(r, sum(mins) / len(mins), log)
            flags.append(("role", f"started {sum(two)} of his last 2 games after {sum(before)} of {len(before)} "
                          f"before; {sum(mins) / len(mins):.1f} min in his starts, against {season_min:.1f} for "
                          "the season"))
        elif not any(two) and share >= 0.75 and len(before) >= 3:
            mins = [g[1] for g in log[-2:]]
            rrate = role_rate(r, sum(mins) / len(mins), log)
            flags.append(("role", f"came off the bench in his last 2 games after starting {sum(before)} of "
                          f"{len(before)}; {sum(mins) / len(mins):.1f} min in those 2, against {season_min:.1f} "
                          "for the season"))
    role = said(ROLE, recent, head)
    if role:
        flags.append(("role", f"news {role}"))

    # minutes: last 3 games against the season, outlier games left out
    if len(log) >= 5:
        from gamelog import outliers
        drops = r.get("drops") if r.get("log") else outliers(log)
        kept = [g for g in log if g[3] not in (drops or {})]
        if len(kept) >= 5:
            m3, ms = sum(g[1] for g in kept[-3:]) / 3, sum(g[1] for g in kept) / len(kept)
            if abs(m3 - ms) >= args.min_change:
                rrate = rrate or role_rate(r, m3, log)
                flags.append(("minutes", f"{m3:.1f} min over his last 3 games against {ms:.1f} for the season "
                              f"({signed(m3 - ms, True)})"))
    mins = said(MINUTES, recent, body) or said(BIGGER, recent, head)
    if mins:
        flags.append(("minutes", f"news {mins}"))

    # rest: a back-to-back ahead, and a reason to think he sits one night of it
    games = team_days.get(r["pro"], [])
    ahead = [(a, b) for a, b in back_to_backs(games) if today <= a <= today + dt.timedelta(days=args.ahead)]
    if ahead and not (inj and inj["status"].lower() == "out"):  # an injured player's absence is the injury's
        signals = []
        rest = said(REST, recent, body)
        if rest:
            signals.append(f"news {rest}")
        done, past = set(played), [d for d in games if d < today]
        for a, b in back_to_backs(past):
            missed = [d for d in (a, b) if d not in done]
            if len(missed) != 1 or not played or played[0] > a:
                continue
            i = past.index(missed[0])  # an isolated miss: he played the team's games either side of it
            if 0 < i < len(past) - 1 and past[i - 1] in done and past[i + 1] in done:
                signals.append(f'sat the {"second" if missed[0] == b else "first"} night of the '
                               f'{a:%d}–{b:%d %b} back-to-back, playing the games either side')
        if signals:
            flags.append(("rest", "back-to-back " + ", ".join(f"{a:%a %d}–{b:%a %d %b}" for a, b in ahead)
                          + "; " + "; ".join(signals)))
    return flags, rrate


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ours", action="store_true", help="our roster only")
    ap.add_argument("--fa", type=int, default=40, help="free agents and waiver players checked, by rate (default 40)")
    ap.add_argument("--value", type=float, default=25, help="injured free agents and waiver players are also checked "
                    "when last season (or the projection) is worth this many FP/g (default 25)")
    ap.add_argument("--days", type=int, default=4, help="news this many days old or newer is read for role, minutes "
                    "and rest (default 4)")
    ap.add_argument("--soon", type=int, default=7, help="an ESPN return within this many days is checked against "
                    "talk of a longer absence (default 7)")
    ap.add_argument("--stale", type=int, default=5, help="days without news that make an 'out' listing a gap (default 5)")
    ap.add_argument("--min-change", type=float, default=5, help="minutes change over the last 3 games that is flagged "
                    "(default 5)")
    ap.add_argument("--ahead", type=int, default=7, help="days ahead to look for back-to-backs (default 7)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--json", help="also write the flagged players, with their full news, to this JSON file")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")
    from injuries import injuries as injury_feed
    from injury_watch import box, player_pool
    from gamelog import season_logs

    now = dt.datetime.now(dt.timezone.utc)
    today = now.astimezone(ET).date()
    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches[:20]))
    feed = injury_feed()
    league = get(f"{LEAGUE}?view=mTeam&view=mMatchupScore&view=mStatus", cookies=True)
    names = {t["id"]: t["name"].strip() for t in league["teams"]}
    period = league["status"]["currentMatchupPeriod"]
    opponents = {}  # this matchup's and the next one's opponents
    for m in league["schedule"]:
        ids = (m["home"]["teamId"], (m.get("away") or {}).get("teamId"))
        if m["matchupPeriodId"] in (period, period + 1) and TEAM_ID in ids:
            opponents[ids[1] if ids[0] == TEAM_ID else ids[0]] = m["matchupPeriodId"] - period
    team_days, _ = schedules(now)
    logs, _ = season_logs(now)

    ours = [r for r in pool.values() if r["owner"] == TEAM_ID]
    others = [] if args.ours else [r for r in pool.values() if r["owner"] not in (None, TEAM_ID)]
    free = [r for r in pool.values() if r["league"] in ("FREEAGENT", "WAIVERS")]
    avail = [] if args.ours else sorted(free, key=lambda r: -(r.get("wrate") or 0))[:args.fa]
    base = lambda r: (r.get("last") or r.get("projected") or {}).get("fpg") or 0
    avail += [] if args.ours else [r for r in free if r["id"] in feed and base(r) >= args.value and r not in avail]
    scope = ours + avail + others
    with ThreadPoolExecutor(8) as ex:
        items = dict(zip((r["id"] for r in scope), ex.map(lambda r: news(r["id"]), scope)))

    def starts_of(r, log):
        out = []
        for g in log:
            lines = box(g[3])["lines"]
            line = next((ls[str(r["id"])] for ls in lines.values() if str(r["id"]) in ls), None)
            out.append(bool(line and line[2]))
        return out

    rows = []
    for r in scope:
        log = logs.get(r["id"], [])
        flags, rrate = check(r, items[r["id"]], feed.get(r["id"]), log, starts_of(r, log), team_days, today, args)
        if r["owner"] not in (None, TEAM_ID) and r["owner"] not in opponents:  # other rosters: injuries only
            flags = [f for f in flags if f[0] in ("injury", "gap")]
            rrate = None
        if flags:
            rows.append((r, flags, rrate, log))

    live_ov, old_ov = load_overrides(today)
    known = {r["player"].lower() for r in pool.values()}
    label = lambda r: ("us" if r["owner"] == TEAM_ID else names.get(r["owner"], "") if r["owner"]
                       else "waivers" if r["league"] == "WAIVERS" else "free agent")
    abbrev = {t["id"]: t["abbrev"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]}
    status = lambda r: (f'{feed[r["id"]]["status"].lower()}' + (f', ESPN est. {feed[r["id"]]["return"]:%d %b}'
                        if feed[r["id"]]["return"] else "") if r["id"] in feed else "active")

    out = [f"# News watch: {today:%d %b %Y}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/news_watch.py`. This is **data, not a verdict**: "
           "each flag is a question for the research step.",
           f"- **Scope:** {len(ours)} on our roster" + ("" if args.ours else
           f", {len(avail)} free agents and waiver players (the top {args.fa} by rate, and injured ones worth "
           f"{args.value:g}+ FP/g last season or on projection), and {len(others)} on other teams' rosters (injury "
           f"flags only, except this week's and next week's opponents: "
           + ", ".join(names[t] for t in sorted(opponents, key=opponents.get)) + ")")
           + f". News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last {args.days} days.",
           f"- **Flags:** {len(rows)} players. *injury*: ESPN's label or date disagrees with the news; *role*: into or "
           f"out of the starting lineup; *minutes*: last 3 games {args.min_change:g}+ min off the season, or a "
           f"minutes limit; *rest*: a back-to-back in the next {args.ahead} days with a rest signal; *gap*: out with "
           f"no date, or no news in {args.stale} days.",
           "- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute "
           "this season (outliers out) times his minutes in the new role. The plans use it only once the research "
           "confirms the role and records it in `council/news_overrides.csv`.", ""]
    link = lambda u: f"[link]({u})" if u.startswith("http") else (u or "—")
    if live_ov or old_ov:
        out += ["## Overrides (`council/news_overrides.csv`)", "",
                "| Player | Kind | Value | Until | Source | State |", "|---|---|---|---|---|---|"]
        for row in live_ov + old_ov:
            state = "expired: remove it" if row in old_ov else ("in force" if row["player"].lower() in known
                                                                else "in force, but no such player in the pool")
            out.append(f'| {row["player"]} | {row["kind"]} | {row["value"]} | {row["until"] or "—"} | '
                       f'{link(row["source"])} | {state} |')
        out.append("")

    order = {"injury": 0, "role": 1, "minutes": 2, "rest": 3, "gap": 4}
    groups = [("Our roster", lambda r: r["owner"] == TEAM_ID),
              ("Free agents and waivers", lambda r: r["owner"] is None),
              ("Opponents: this week and next", lambda r: r["owner"] in opponents),
              ("Other rosters: injury flags only", lambda r: r["owner"] not in (None, TEAM_ID) and r["owner"] not in opponents)]
    rows.sort(key=lambda x: (min(order[k] for k, _ in x[1]), -(x[0].get("wrate") or 0)))
    out += ["## Summary", "", "| Player | NBA | League | Flags | Rate | Role rate | ESPN status |",
            "|---|---|---|---|---:|---:|---|"]
    for title, keep in groups:
        for r, flags, rrate, _ in (x for x in rows if keep(x[0])):
            kinds = ", ".join(sorted({k for k, _ in flags}, key=order.get))
            out.append(f'| **{r["player"]}** | {abbrev.get(r["pro"], "")} | {label(r)} | {kinds} | '
                       f'{r.get("wrate") or 0:.1f}{" †" if r.get("small") else ""} | '
                       f'{"—" if rrate is None else f"{rrate:.1f}"} | {status(r)} |')
    out.append("")
    out.append("† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).")
    out.append("")

    dump = []
    for title, keep in groups:
        chosen = [x for x in rows if keep(x[0])]
        if not chosen:
            continue
        out += [f"## {title}", ""]
        for r, flags, rrate, log in chosen:
            l7, l15, l30 = window_cells(r)
            out.append(f'### {r["player"]} ({abbrev.get(r["pro"], "")}, {r["pos"]}, {label(r)})')
            out.append("")
            out.append(f'- Rate **{r.get("wrate") or 0:.1f}**' + (" (small sample)" if r.get("small") else "")
                       + (f" · role rate {rrate:.1f}" if rrate is not None else "")
                       + f' · season {season_cell(r)} · L7 {l7} · L15 {l15} · L30 {l30}'
                       + (f' · projected {r["projected"]["fpg"]:.1f}' if r.get("projected") else ""))
            out.append(f"- ESPN: {status(r)}" + (f' ({feed[r["id"]]["injury"]}, updated {feed[r["id"]]["updated"]})'
                                                if r["id"] in feed else ""))
            for kind, signal in sorted(flags, key=lambda f: order[f[0]]):
                out.append(f"- **{kind.title()}:** {signal}")
            for x in items[r["id"]][:2]:
                out.append(f'- News ({x["date"].astimezone(ET):%d %b}): {x["headline"]}')
            out.append("- **Research:** _pending_")
            out.append("")
            dump.append({"player": r["player"], "id": r["id"], "nba": abbrev.get(r["pro"], ""), "league": label(r),
                         "rate": round(r.get("wrate") or 0, 1), "small_sample": bool(r.get("small")),
                         "role_rate": None if rrate is None else round(rrate, 1),
                         "windows": {"season": season_cell(r), "l7": l7, "l15": l15, "l30": l30},
                         "espn": ({k: str(v) for k, v in feed[r["id"]].items() if k in ("status", "injury", "return",
                                                                                         "updated", "note")}
                                  if r["id"] in feed else {"status": "active"}),
                         "flags": [{"kind": k, "signal": s} for k, s in flags],
                         "games": [{"date": str(g[0]), "min": g[1], "fp": g[2]} for g in log[-5:]],
                         "news": [{"date": f'{x["date"]:%Y-%m-%d %H:%M}Z', "headline": x["headline"],
                                   "story": x["story"]} for x in items[r["id"]][:6]]})

    out += ["## Sources", "",
            f"- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA "
            f"injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 "
            f"(`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read {now:%Y-%m-%d %H:%M} UTC.", ""]
    text = "\n".join(out)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}: {len(rows)} players flagged.")
    else:
        print(text)
    if args.json:
        Path(args.json).write_text(json.dumps(dump, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
