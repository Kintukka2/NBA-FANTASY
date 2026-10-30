#!/usr/bin/env python3
"""Recent form: FP/g over the last 7, 15 and 30 days for named players.

Stdlib only and read-only against ESPN. It uses the same two cookies as
council/espn_sync.py. For each player it gives the season, L7, L15 and L30
FP/g (ESPN's rolling splits, games in brackets) beside ESPN's projection and
last season, with minutes for the season and the last 7 days, their league
status, and ESPN's injury status and estimated return.

CLAUDE.md makes these windows part of every player analysis. The council
reads the table this writes beside the research briefing in docs/research/.

Guards, as in slump_watch.py:
  - It refuses to run while NBA games are live. --allow-live overrides this.
  - Every split must re-score with scripts/league_scoring.py to ESPN's total.

Usage:
  python council/form.py "Anthony Edwards" "Cade Cunningham"
  python council/form.py --ours                       # our whole roster
  python council/form.py --team 3 --out docs/research/20261030-0400-form.md
"""
import argparse
import datetime as dt
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from injuries import injuries as injury_feed  # noqa: E402
from injury_watch import player_pool  # noqa: E402
from slump_watch import FANTASY, LEAGUE, TEAM_ID, get, live_games, signed, windows_note  # noqa: E402


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower().replace(".", "").strip()


def find(pool, name):
    """Players matching a name: exact (ignoring accents and dots) first, else every partial match."""
    key = norm(name)
    exact = [r for r in pool.values() if norm(r["player"]) == key]
    return exact or [r for r in pool.values() if key in norm(r["player"])]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("players", nargs="*", help="player names (accents and case ignored)")
    ap.add_argument("--ours", action="store_true", help="add our whole roster")
    ap.add_argument("--team", type=int, nargs="+", default=[], help="add these fantasy teams' rosters (team ids)")
    ap.add_argument("--out", help="write the table here instead of stdout")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()
    if not (args.players or args.ours or args.team):
        ap.error("name at least one player, or pass --ours or --team")

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")

    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches))
    teams = {t["id"]: t["name"].strip() for t in get(f"{LEAGUE}?view=mTeam", cookies=True)["teams"]}
    abbrev = {t["id"]: t["abbrev"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]}
    feed = injury_feed()

    picked, unknown, ambiguous = {}, [], []
    for name in args.players:
        hits = find(pool, name)
        if not hits:
            unknown.append(name)
        elif len(hits) > 5:
            ambiguous.append(f'{name} ({len(hits)} matches)')
        else:
            picked.update({r["id"]: r for r in hits})
    for tid in ([TEAM_ID] if args.ours else []) + args.team:
        picked.update({r["id"]: r for r in pool.values() if r["owner"] == tid})
    if unknown or ambiguous:
        sys.exit("Not found in the league's player pool: " + ", ".join(unknown + ambiguous))

    now = dt.datetime.now(dt.timezone.utc)
    fmt = lambda x: "—" if x is None else f"{x:.1f}"
    cell = lambda s: f'{s["fpg"]:.1f} ({s["gp"]})' if s else "—"
    league = lambda r: (teams.get(r["owner"], "?") + (" (us)" if r["owner"] == TEAM_ID else "")
                        if r["league"] == "ONTEAM" else "waivers" if r["league"] == "WAIVERS" else "free agent")

    def status(r):
        i = feed.get(r["id"])
        if not i:
            return "active"
        return i["status"].lower() + (f', ESPN est. {i["return"]:%d %b}' if i["return"] else "")

    rows = sorted(picked.values(), key=lambda r: (r["owner"] != TEAM_ID, -((r["current"] or {}).get("fpg") or 0)))
    out = [f"# Recent form: {now:%d %b %Y}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/form.py`. This is **data, not a verdict**.",
           f"- **Checks:** {'**games were live** (--allow-live): ' + '; '.join(live) if live else 'no NBA game was in progress'}. "
           f"All {len(pool)} pool players' current, L7, L15, L30, projected and 2026 averages re-score with "
           "`scripts/league_scoring.py` (0 mismatches).",
           windows_note(rows),
           "- **L7 − season** is the last 7 days' FP/g minus the season's. ESPN's projection leaves out OREB, DREB, "
           "DD and TD, so it reads low for players who earn them.", "",
           "| Player | NBA | League | Season FP/g (GP) | L7 | L15 | L30 | L7 − season | Min: season / L7 | "
           "Projected | 2026 | ESPN status |",
           "|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|"]
    for r in rows:
        c, l7 = r["current"], r["l7"]
        trend = signed(l7["fpg"] - c["fpg"], True) if c and l7 else "—"
        mins = f'{fmt(c and c["min"])} / {fmt(l7 and l7["min"])}'
        out.append(f'| **{r["player"]}** | {abbrev.get(r["pro"], "FA")} | {league(r)} | {cell(c)} | {cell(l7)} | '
                   f'{cell(r["l15"])} | {cell(r["l30"])} | {trend} | {mins} | {fmt(r["projected"] and r["projected"]["fpg"])} | '
                   f'{fmt(r["last"] and r["last"]["fpg"])} | {status(r)} |')
    out += ["", "## Sources", "",
            f"- ESPN fantasy API, league 423671879 (`kona_player_info` with ESPN's season, last-7, last-15 and "
            f"last-30-day splits, `mTeam`, `proTeamSchedules_wl`) and ESPN's NBA injury feed, read "
            f"{now:%Y-%m-%d %H:%M} UTC.", ""]
    report = "\n".join(out)
    if args.out:
        Path(args.out).write_text(report)
        print(f"Wrote {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
