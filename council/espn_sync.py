#!/usr/bin/env python3
"""Read league 423671879 live from ESPN and compare it with the council files.

Stdlib only. Read-only against ESPN: it calls the lm-api-reads endpoint
and nothing else. The league is private, so it needs two cookies from a
logged-in browser, set as environment variables (never commit them):

  ESPN_S2    the espn_s2 cookie
  ESPN_SWID  the SWID cookie, braces included

Usage:
  python council/espn_sync.py                    # report only
  python council/espn_sync.py --check "Andrew Wiggins" "Yaxel Lendeborg"
  python council/espn_sync.py --write-taken      # rebuild council/taken.txt

The report compares our ESPN roster with council/roster.csv and lists
players whose rostered status differs from council/taken.txt. It never
writes roster.csv: that file records moves the user reports.

Rosters are read for ESPN's transaction scoring period, the one a move made
now lands in. Once a day's games lock, ESPN applies a move from the next
day, so the current period's roster would still show the dropped player.
"""
import argparse
import csv
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

LEAGUE_ID = 423671879
SEASON = 2027
TEAM_ID = 5  # Come-in Cider
URL = (f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/fba/seasons/{SEASON}"
       f"/segments/0/leagues/{LEAGUE_ID}?view=mTeam&view=mRoster&view=mSettings&view=mStatus")
SLOTS = {0: "PG", 1: "SG", 2: "SF", 3: "PF", 4: "C", 5: "G", 6: "F", 11: "UTIL",
         12: "BE", 13: "IR"}
ROOT = Path(__file__).resolve().parent
TAKEN = ROOT / "taken.txt"
ROSTER = ROOT / "roster.csv"


def fetch(period=None):
    s2, swid = os.environ.get("ESPN_S2"), os.environ.get("ESPN_SWID")
    if not s2 or not swid:
        sys.exit("ESPN_S2 and ESPN_SWID must be set (see the docstring).")
    url = URL + (f"&scoringPeriodId={period}" if period else "")
    req = urllib.request.Request(url, headers={"Cookie": f"espn_s2={s2}; SWID={swid}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"ESPN returned HTTP {e.code}. A 401 means the cookies expired: copy fresh ones.")


def rosters(league):
    """{team_id: (team_name, [(player, slot, injury), ...])}"""
    out = {}
    for t in league["teams"]:
        ents = t.get("roster", {}).get("entries", [])
        out[t["id"]] = (t.get("name", "").strip(), [
            (e["playerPoolEntry"]["player"]["fullName"],
             SLOTS.get(e["lineupSlotId"], str(e["lineupSlotId"])),
             e["playerPoolEntry"]["player"].get("injuryStatus", ""))
            for e in ents])
    return out


def read_taken():
    lines = TAKEN.read_text().splitlines() if TAKEN.exists() else []
    header = [l for l in lines if l.startswith("#")]
    names = [l.strip() for l in lines if l.strip() and not l.startswith("#")]
    return header, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", nargs="*", default=[], help="players to look up")
    ap.add_argument("--write-taken", action="store_true",
                    help="rewrite taken.txt as every player on an ESPN roster")
    args = ap.parse_args()

    league = fetch()
    period = league.get("status", {}).get("transactionScoringPeriod")
    if period and period != league.get("scoringPeriodId"):
        league = fetch(period)
    teams = rosters(league)
    owner = {p: (tid, name) for tid, (name, ps) in teams.items() for p, _, _ in ps}

    ours = teams[TEAM_ID][1]
    print(f"Our ESPN roster ({len(ours)}), scoring period {league.get('scoringPeriodId')}:")
    for p, slot, inj in ours:
        print(f"  {slot:<5} {p}  {inj}")
    with ROSTER.open() as f:
        csv_players = {r["player"] for r in csv.DictReader(f)}
    espn_players = {p for p, _, _ in ours}
    if csv_players == espn_players:
        print("roster.csv matches ESPN.")
    else:
        print("roster.csv differs from ESPN:")
        for p in sorted(espn_players - csv_players):
            print(f"  on ESPN, missing from roster.csv: {p}")
        for p in sorted(csv_players - espn_players):
            print(f"  in roster.csv, not on ESPN: {p}")

    header, taken = read_taken()
    gone = sorted(set(taken) - owner.keys())
    new = sorted(owner.keys() - set(taken))
    print(f"taken.txt: {len(gone)} no longer rostered, {len(new)} rostered but missing")
    for p in gone:
        print(f"  free now: {p}")
    for p in new:
        print(f"  rostered: {p} ({owner[p][1]})")

    for name in args.check:
        hit = next((p for p in owner if p.lower() == name.lower()), None)
        print(f"{name}: " + (f"rostered by {owner[hit][1]}" if hit else "not on any roster (free agent or waivers)"))

    if args.write_taken:
        keep = [p for p in taken if p in owner]
        TAKEN.write_text("\n".join(header + keep + new) + "\n")
        print(f"Wrote {TAKEN.name}: {len(keep) + len(new)} players.")


if __name__ == "__main__":
    main()
