#!/usr/bin/env python3
"""Slump Watch: every rostered player in league 423671879 against ESPN's projection.

Stdlib only and read-only against ESPN. It uses the same two cookies as
council/espn_sync.py (ESPN_S2, ESPN_SWID). A player is flagged when his
current FP/g sits --threshold (default 10) or more below ESPN's projected
FP/g. The markdown report covers, per team:
  - the flagged players, their minutes, and the category drivers of each gap
  - every player's FP/g over the last 7, 15 and 30 days (ESPN's rolling
    splits), and who the last 7 days put on the other side of the line
  - the players near the line
  - players under their 2026 average but not under projection
  - our pending trades

Two guards keep the numbers honest:
  - It refuses to run while an NBA game is in progress, because ESPN counts
    a half-played game as a game played. --allow-live overrides this.
  - Every average is re-scored with scripts/league_scoring.py and must
    match ESPN's league-scored total. The latest completed scoring period
    is re-scored again from ESPN's final NBA box scores. Any mismatch exits
    non-zero and writes nothing.

ESPN's projection carries no OREB, DREB, DD or TD. Gaps are therefore
understated for players who earn those, and the report shows how much.

Usage:
  python council/slump_watch.py                       # report to stdout
  python council/slump_watch.py --out docs/analysis/20261027-slump-watch.md
  python council/slump_watch.py --threshold 8 --near 4
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "scripts"))
from league_scoring import per_game, season_total  # noqa: E402
from injuries import injuries as injury_feed  # noqa: E402

LEAGUE_ID = 423671879
SEASON = 2027
TEAM_ID = 5  # Come-in Cider
FANTASY = f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/fba/seasons/{SEASON}"
LEAGUE = f"{FANTASY}/segments/0/leagues/{LEAGUE_ID}"
SITE = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba"
ET = ZoneInfo("America/New_York")

# ESPN stat ids, checked against the league's scoringItems.
STAT = {"PTS": 0, "BLK": 1, "STL": 2, "AST": 3, "OREB": 4, "REB": 6, "TO": 11,
        "FGM": 13, "FGA": 14, "FTM": 15, "FTA": 16, "3PM": 17, "DD": 37, "TD": 38,
        "QD": 39, "MIN": 40, "GP": 42}
SPLIT = {"current": f"00{SEASON}", "projected": f"10{SEASON}", "last": f"00{SEASON - 1}",
         "l7": f"01{SEASON}", "l15": f"02{SEASON}", "l30": f"03{SEASON}"}
# ESPN's rolling splits: games in the last 7, 15 and 30 days. CLAUDE.md makes
# them part of every player analysis.
WINDOWS = {"l7": "L7", "l15": "L15", "l30": "L30"}
# Category groups for the driver line; OREB, DD and TD are reported apart
# because ESPN's projection has none of them.
GROUPS = {"scoring": {"PTS": 1, "FGM": 2, "FGA": -1, "FTM": 1, "FTA": -1, "3PM": 1},
          "reb": {"REB": 1}, "ast": {"AST": 2}, "stocks": {"STL": 4, "BLK": 4}, "TO": {"TO": -2}}
STATUS = {"ACTIVE": "Active", "DAY_TO_DAY": "Day-to-day", "OUT": "**Out**",
          "INJURY_RESERVE": "**IR**", "SUSPENSION": "Suspended"}


def get(url, cookies=False, fantasy_filter=None):
    headers = {}
    if cookies:
        s2, swid = os.environ.get("ESPN_S2"), os.environ.get("ESPN_SWID")
        if not s2 or not swid:
            sys.exit("ESPN_S2 and ESPN_SWID must be set (see council/espn_sync.py).")
        headers["Cookie"] = f"espn_s2={s2}; SWID={swid}"
    if fantasy_filter:
        headers["x-fantasy-filter"] = json.dumps(fantasy_filter)
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{url} returned HTTP {e.code}. A 401 means the cookies expired: copy fresh ones.")


def live_games():
    """Games in progress on yesterday's or today's US slate."""
    today = dt.datetime.now(ET).date()
    live = []
    for day in (today - dt.timedelta(days=1), today):
        for ev in get(f"{SITE}/scoreboard?dates={day:%Y%m%d}").get("events", []):
            if ev["status"]["type"]["state"] == "in":
                live.append(f'{ev["shortName"]} ({ev["status"]["type"]["shortDetail"]})')
    return live


def stat(st, key):
    return float(st.get(str(STAT[key]), 0) or 0)


def fantasy_points(st):
    """League-scored total for an ESPN stat dict of totals."""
    base = per_game(*(stat(st, k) for k in
                      ("PTS", "FGM", "FGA", "FTM", "FTA", "3PM", "REB", "OREB", "AST", "STL", "BLK", "TO")))
    return season_total(base, 1, stat(st, "DD"), stat(st, "TD"), stat(st, "QD"))


def rosters(league):
    """One dict per rostered player with current, projected and last-season splits."""
    rows, mismatches = [], []
    for t in league["teams"]:
        for e in t["roster"]["entries"]:
            p = e["playerPoolEntry"]["player"]
            splits = {s["id"]: s for s in p.get("stats", [])}
            row = {"id": p["id"], "player": p["fullName"], "team": t["name"].strip(),
                   "team_id": t["id"], "pro": p["proTeamId"], "status": p.get("injuryStatus", "")}
            for name, sid in SPLIT.items():
                s = splits.get(sid)
                if not s or not s.get("stats") or stat(s["stats"], "GP") == 0:
                    row[name] = None
                    continue
                total = fantasy_points(s["stats"])
                if abs(total - s["appliedTotal"]) > 0.01:
                    mismatches.append(f'{p["fullName"]} {name}: {total} vs ESPN {s["appliedTotal"]}')
                gp = stat(s["stats"], "GP")
                row[name] = {"gp": int(gp), "fpg": total / gp, "st": s["stats"]}
            rows.append(row)
    return rows, mismatches


def box_check(pro_teams, latest):
    """Re-score the latest completed scoring period from ESPN's final box scores.

    Returns (period, date, matched, mismatches), or None if no completed
    period was found.
    """
    for period in range(latest, 0, -1):
        games = {g["id"]: g["date"] for t in pro_teams
                 for g in t.get("proGamesByScoringPeriod", {}).get(str(period), [])}
        if not games:
            continue
        summaries = [get(f"{SITE}/summary?event={gid}") for gid in games]
        states = {s["header"]["competitions"][0]["status"]["type"]["state"] for s in summaries}
        if states != {"post"}:
            continue
        box = {}
        for s in summaries:
            for team in s["boxscore"]["players"]:
                block = team["statistics"][0]
                for a in block["athletes"]:
                    if a.get("stats"):
                        box[int(a["athlete"]["id"])] = box_points(dict(zip(block["keys"], a["stats"])))
        league = get(f"{LEAGUE}?scoringPeriodId={period}&view=mRoster", cookies=True)
        matched, mismatches = 0, []
        for t in league["teams"]:
            for e in t["roster"]["entries"]:
                p = e["playerPoolEntry"]["player"]
                for s in p.get("stats", []):
                    if s.get("scoringPeriodId") == period and s.get("statSourceId") == 0:
                        espn, ours = s.get("appliedTotal", 0), box.get(p["id"], 0.0)
                        if abs(espn - ours) > 0.01:
                            mismatches.append(f'{p["fullName"]}: ESPN {espn} vs box score {ours}')
                        elif p["id"] in box:
                            matched += 1
        first = dt.datetime.fromtimestamp(min(games.values()) / 1000, ET).date()
        return period, first, matched, mismatches
    return None


def box_points(v):
    """League-scored points for one ESPN box-score line."""
    def made(key):
        m, a = v[key].split("-")
        return float(m), float(a)
    fgm, fga = made("fieldGoalsMade-fieldGoalsAttempted")
    tpm, _ = made("threePointFieldGoalsMade-threePointFieldGoalsAttempted")
    ftm, fta = made("freeThrowsMade-freeThrowsAttempted")
    n = {k: float(v[k]) for k in ("points", "rebounds", "offensiveRebounds", "assists",
                                   "steals", "blocks", "turnovers")}
    tens = sum(n[k] >= 10 for k in ("points", "rebounds", "assists", "steals", "blocks"))
    base = per_game(n["points"], fgm, fga, ftm, fta, tpm, n["rebounds"], n["offensiveRebounds"],
                    n["assists"], n["steals"], n["blocks"], n["turnovers"])
    # A triple-double is also a double-double; the league stacks the bonuses.
    return season_total(base, 1, int(tens >= 2), int(tens >= 3), int(tens >= 4))


def pg(split, key):
    return stat(split["st"], key) / split["gp"]


def analyse(r):
    """Gap, minutes, rate and category drivers for a player with both splits."""
    cur, proj = r["current"], r["projected"]
    r["gap"] = cur["fpg"] - proj["fpg"]
    r["min"], r["pmin"] = pg(cur, "MIN"), pg(proj, "MIN")
    rate = (cur["fpg"] / r["min"]) / (proj["fpg"] / r["pmin"]) if r["min"] and r["pmin"] else 0
    r["rate"] = rate
    r["drivers"] = {g: sum(w * (pg(cur, k) - pg(proj, k)) for k, w in ws.items())
                    for g, ws in GROUPS.items()}
    r["bonus"] = (stat(cur["st"], "OREB") + 3 * stat(cur["st"], "DD") + 6 * stat(cur["st"], "TD")
                  + 40 * stat(cur["st"], "QD")) / cur["gp"]
    short = r["pmin"] - r["min"]
    if short >= 3 and rate >= 0.85:
        r["driver"] = "minutes"
    elif short < 3:
        r["driver"] = "efficiency"
    else:
        r["driver"] = "both"


def signed(x, plus=False):
    """One decimal, with a true minus sign."""
    return (f"{x:+.1f}" if plus else f"{x:.1f}").replace("-", "\u2212")


def window_cells(r):
    """FP/g over the last 7, 15 and 30 days, games in brackets, as table cells."""
    return [f'{r[k]["fpg"]:.1f} ({r[k]["gp"]})' if r.get(k) else "—" for k in WINDOWS]


def windows_note(rows):
    """Header bullet explaining the L7 / L15 / L30 columns for these rows."""
    played = [r for r in rows if r.get("current")]
    whole = [WINDOWS[k] for k in WINDOWS
             if played and all((r.get(k) or {}).get("gp") == r["current"]["gp"] for r in played)]
    note = ("- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's "
            "rolling splits, re-scored with `scripts/league_scoring.py`.")
    if whole:
        note += (f" {' and '.join(whole)} cover{'s' if len(whole) == 1 else ''} every game so far for every "
                 "player listed, so they equal the season average for now.")
    return note


def line(split):
    f = lambda k: pg(split, k)
    return (f'{f("MIN"):.1f} min, {f("PTS"):.1f} pts, {f("FGM"):.1f}-{f("FGA"):.1f} FG, '
            f'{f("FTM"):.1f}-{f("FTA"):.1f} FT, {f("REB"):.1f} reb, {f("AST"):.1f} ast, '
            f'{f("STL"):.1f} stl, {f("BLK"):.1f} blk, {f("TO"):.1f} TO')


def render(rows, teams, pro, args, checks, pending, back):
    """The whole report as markdown."""
    by_team = defaultdict(list)
    for r in rows:
        by_team[r["team_id"]].append(r)
    rank = {}
    for tid, rs in by_team.items():
        ranked = sorted((r for r in rs if r["projected"]), key=lambda r: -r["projected"]["fpg"])
        rank.update({r["id"]: i + 1 for i, r in enumerate(ranked)})
    both = [r for r in rows if r["current"] and r["projected"]]
    for r in both:
        analyse(r)
    flagged = [r for r in both if r["gap"] <= -args.threshold]
    near = [r for r in both if -args.threshold < r["gap"] <= -args.near]
    gps = sorted({r["current"]["gp"] for r in rows if r["current"]})
    def status(r):
        label = STATUS.get(r["status"], r["status"].replace("_", " ").title() or "—")
        if r["status"] not in ("", "ACTIVE") and back.get(r["id"]):
            label += f', ESPN est. back {back[r["id"]]:%d %b}'
        return label
    fmt = lambda x: "—" if x is None else f"{x:.1f}"
    name = lambda tid: teams[tid] + (" (us)" if tid == TEAM_ID else "")

    out = [f"# Slump Watch: {dt.datetime.now(dt.timezone.utc):%d %b %Y}", ""]
    out += [f"- Generated {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC by `council/slump_watch.py`. "
            "This is **a report, not a council verdict**.",
            f"- **Flag:** current FP/g **{args.threshold:g} or more** below ESPN's projected FP/g. "
            f"*Near the line* is {args.near:g} to {args.threshold:g} below.",
            f"- **Data:** all {len(rows)} rostered players in league {LEAGUE_ID}, through scoring period "
            f"{checks['latest']}. Teams have played **{gps[0]} to {gps[-1]} games**.",
            f"- **Checks:** {checks['live']}. Every current, projected, L7, L15, L30 and {SEASON - 1} average "
            "re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). "
            f"{checks['box']}",
            windows_note(rows),
            "- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current "
            "average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure "
            "on each player's driver line.",
            ""]

    out += ["## Headline", "",
            f"**{len(flagged)} rostered players are {args.threshold:g}+ FP/g under projection, on "
            f"{len({r['team_id'] for r in flagged})} of {len(teams)} teams.**", "",
            "| Team | Flagged | Top 3 by projection (current / projected) |", "|---|---:|---|"]
    order = sorted(teams, key=lambda tid: (-sum(r["team_id"] == tid for r in flagged), teams[tid]))
    for tid in order:
        top = sorted((r for r in by_team[tid] if r["projected"]), key=lambda r: -r["projected"]["fpg"])[:3]
        cells = " · ".join(f'{r["player"]} {fmt(r["current"] and r["current"]["fpg"])}/{r["projected"]["fpg"]:.1f}'
                           for r in top)
        out.append(f'| {name(tid)} | {sum(r["team_id"] == tid for r in flagged)} | {cells} |')
    out.append("")

    out += ["## By team", "",
            "**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / "
            "projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line "
            "splits the gap into category shortfalls, in FP/g.", ""]
    for tid in order:
        fl = sorted((r for r in flagged if r["team_id"] == tid), key=lambda r: r["gap"])
        nr = sorted((r for r in near if r["team_id"] == tid), key=lambda r: r["gap"])
        out += [f"### {name(tid)}: {len(fl)}", ""]
        if fl:
            out += ["| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | "
                    f"{SEASON - 1} | ESPN status |", "|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|"]
            for r in fl:
                out.append(f'| {r["player"]} | {pro[r["pro"]]} | #{rank[r["id"]]} | {r["current"]["gp"]} | '
                           f'{r["min"]:.1f} / {r["pmin"]:.1f} | {r["rate"]:.2f} | {r["current"]["fpg"]:.1f} | '
                           + " | ".join(window_cells(r)) + f' | {r["projected"]["fpg"]:.1f} | **{signed(r["gap"])}** | '
                           f'{fmt(r["last"] and r["last"]["fpg"])} | {status(r)} |')
            out.append("")
            for r in fl:
                d = ", ".join(f"{g} {signed(v, True)}" for g, v in r["drivers"].items())
                out += [f'- **{r["player"]}** ({r["driver"]}): {d}; bonus {signed(r["bonus"], True)}.',
                        f'  - Current: {line(r["current"])}']
                if r["l7"] and r["l7"]["gp"] != r["current"]["gp"]:
                    out.append(f'  - Last 7 days ({r["l7"]["gp"]} GP): {line(r["l7"])}')
                out.append(f'  - Projected: {line(r["projected"])}')
        else:
            out += ["No one flagged.", ""]
        if nr:
            out.append("- **Near the line:** " + ", ".join(
                f'{r["player"]} {signed(r["gap"])} (#{rank[r["id"]]}, {r["driver"]}, L7 {fmt(r["l7"] and r["l7"]["fpg"])})'
                for r in nr) + ".")
        out.append("")

    out += ["## Drivers", "",
            "- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.",
            "- *efficiency*: within 3 minutes of projection, so the shortfall is production.",
            "- *both*: minutes short and the rate down too.", "",
            "| Driver | Flagged players |", "|---|---|"]
    for kind in ("minutes", "efficiency", "both"):
        names = [r["player"] for r in sorted(flagged, key=lambda r: r["gap"]) if r["driver"] == kind]
        out.append(f'| {kind} | {", ".join(names) or "—"} |')
    hurt = [f'{r["player"]} ({status(r)})' for r in flagged if r["status"] not in ("", "ACTIVE")]
    out += ["", f'- **Flagged and not active on ESPN:** {", ".join(hurt) or "none"}.']
    unplayed = [r for r in rows if not r["current"]]
    if unplayed:
        out.append("- **Rostered, no games yet:** " + ", ".join(
            f'{r["player"]} ({r["team"]}, projected {fmt(r["projected"] and r["projected"]["fpg"])}, {status(r)})'
            for r in unplayed) + ".")
    out.append("")

    l7 = lambda r: r["l7"]["fpg"] - r["projected"]["fpg"]
    recent = [r for r in both if r["l7"] and r["l7"]["gp"] >= 2]
    better = [r for r in recent if r in flagged and l7(r) > -args.threshold]
    colder = [r for r in recent if r not in flagged and l7(r) <= -args.threshold]
    out += ["## Last 7 days", "",
            "Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.", "",
            f"- **Flagged, but within {args.threshold:g} of projection over the last 7 days:** " + (", ".join(
                f'{r["player"]} ({name(r["team_id"])}, L7 {r["l7"]["fpg"]:.1f} in {r["l7"]["gp"]} vs projected '
                f'{r["projected"]["fpg"]:.1f}, season gap {signed(r["gap"])})'
                for r in sorted(better, key=lambda r: (r["team_id"] != TEAM_ID, -l7(r)))) or "none") + ".",
            f"- **Not flagged, but {args.threshold:g}+ under projection over the last 7 days:** " + (", ".join(
                f'{r["player"]} ({name(r["team_id"])}, L7 {r["l7"]["fpg"]:.1f} in {r["l7"]["gp"]} vs projected '
                f'{r["projected"]["fpg"]:.1f}, L7 gap {signed(l7(r))}, season gap {signed(r["gap"])})'
                for r in sorted(colder, key=lambda r: (r["team_id"] != TEAM_ID, l7(r)))) or "none") + ".", ""]

    last = [r for r in both if r["last"] and r["current"]["fpg"] - r["last"]["fpg"] <= -args.threshold
            and r["gap"] > -args.threshold]
    out += [f"## Under {SEASON - 1}, not under projection", "",
            f"{args.threshold:g}+ under last season's average, but within {args.threshold:g} of projection.", ""]
    if last:
        out += ["| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | " + str(SEASON - 1) + " |",
                "|---|---|---:|---|---:|---:|---:|---:|---:|---:|"]
        for r in sorted(last, key=lambda r: (r["team_id"] != TEAM_ID, r["current"]["fpg"] - r["last"]["fpg"])):
            out.append(f'| {r["player"]} | {name(r["team_id"])} | {r["current"]["gp"]} | '
                       f'{r["min"]:.1f} / {r["pmin"]:.1f} | {r["current"]["fpg"]:.1f} | '
                       + " | ".join(window_cells(r)) + f' | {r["projected"]["fpg"]:.1f} | {r["last"]["fpg"]:.1f} |')
    else:
        out.append("None.")
    out.append("")

    out += ["## Our pending trades", ""]
    by_id = {r["id"]: r for r in rows}
    if not pending:
        out += ["None.", ""]
    for tx in pending:
        other = next(i["toTeamId"] if i["fromTeamId"] == TEAM_ID else i["fromTeamId"] for i in tx["items"])
        expires = dt.datetime.fromtimestamp(tx["expirationDate"] / 1000, dt.timezone.utc)
        out += [f'With **{teams[other]}**, {"proposed by us" if tx["teamId"] == TEAM_ID else "proposed to us"}, '
                f'expires {expires:%d %b %H:%M} UTC.', "",
                "| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |",
                "|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|"]
        for i in sorted(tx["items"], key=lambda i: i["toTeamId"] != TEAM_ID):
            r = by_id.get(i["playerId"])
            if not r or not r.get("current") or "gap" not in r:
                continue
            side = "we receive" if i["toTeamId"] == TEAM_ID else "we send"
            out.append(f'| {r["player"]} | {side} | {r["current"]["gp"]} | {r["min"]:.1f} / {r["pmin"]:.1f} | '
                       f'{r["current"]["fpg"]:.1f} | ' + " | ".join(window_cells(r))
                       + f' | {r["projected"]["fpg"]:.1f} | {signed(r["gap"], True)} | {status(r)} |')
        out.append("")

    out += ["## Sources", "",
            f"- ESPN fantasy API, league {LEAGUE_ID}: `mRoster`, `mTeam`, `mSettings`, `mStatus` and "
            f"`mPendingTransactions` views, read {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC.",
            "- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the "
            "box-score check.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--threshold", type=float, default=10, help="FP/g under projection to flag (default 10)")
    ap.add_argument("--near", type=float, default=5, help="FP/g under projection for 'near the line' (default 5)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")

    league = get(f"{LEAGUE}?view=mRoster&view=mTeam&view=mSettings&view=mStatus&view=mPendingTransactions",
                 cookies=True)
    pro_teams = get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
    pro = {t["id"]: t["abbrev"] for t in pro_teams}
    teams = {t["id"]: t["name"].strip() for t in league["teams"]}
    latest = league["status"]["latestScoringPeriod"]

    rows, mismatches = rosters(league)
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches))

    checks = {"latest": latest,
              "live": ("**Games were in progress** (--allow-live): " + "; ".join(live)) if live
              else "No NBA game was in progress"}
    if live:
        checks["box"] = "Box-score check skipped while games are live."
    else:
        box = box_check(pro_teams, latest)
        if box is None:
            checks["box"] = "No completed scoring period to check against box scores."
        else:
            period, date, matched, bad = box
            if bad:
                sys.exit(f"Scoring period {period} does not match the final box scores:\n  " + "\n  ".join(bad))
            checks["box"] = (f"Scoring period {period} ({date:%a %d %b} US) re-scored from ESPN's final NBA box "
                             f"scores: all {matched} rostered lines match.")

    pending = [tx for tx in league.get("pendingTransactions", []) or league.get("transactions", [])
               if tx.get("type") == "TRADE_PROPOSAL" and tx.get("status") == "PENDING"
               and any(TEAM_ID in (i["fromTeamId"], i["toTeamId"]) for i in tx.get("items", []))]

    back = {pid: i["return"] for pid, i in injury_feed().items()}
    report = render(rows, teams, pro, args, checks, pending, back)
    if args.out:
        Path(args.out).write_text(report)
        print(f"Wrote {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
