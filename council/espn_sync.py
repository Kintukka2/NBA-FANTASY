#!/usr/bin/env python3
"""Sync the council files with league 423671879 on ESPN, the source of truth for rosters.

Stdlib only. Read-only against ESPN: it calls the lm-api-reads endpoint
and nothing else. The league is private, so it needs two cookies from a
logged-in browser, set as environment variables (never commit them):

  ESPN_S2    the espn_s2 cookie
  ESPN_SWID  the SWID cookie, braces included

Usage:
  python council/espn_sync.py                    # sync roster.csv and taken.txt to ESPN
  python council/espn_sync.py --dry-run          # report the differences, write nothing
  python council/espn_sync.py --check "Andrew Wiggins" "Yaxel Lendeborg"

It writes council/roster.csv to match our ESPN roster:
- a player added on ESPN gets a row: team, positions, slot, how he came (free
  agent, waivers, trade), the date, and who he replaced;
- a dropped player's row goes;
- a move into or out of the IR slot updates `slot` and adds a note.
It also rewrites council/taken.txt as every player on an ESPN roster. No
confirmation is needed: the ESPN app is the record, and the moves it made
are printed so the reply can name them.

Rosters are read for ESPN's transaction scoring period, the one a move made
now lands in. Once a day's games lock, ESPN applies a move from the next
day, so the current period's roster would still show the dropped player.
"""
import argparse
import csv
import datetime as dt
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


KIND = {"WAIVER": "waivers", "FREEAGENT": "free agent", "TRADE_ACCEPT": "trade", "TRADE": "trade",
        "DRAFT": "draft"}
POS = {0: "PG", 1: "SG", 2: "SF", 3: "PF", 4: "C"}
FIELDS = ["player", "team", "pos", "slot", "acquired", "acquired_on", "notes"]


def pro_abbrevs():
    """{pro team id: 'DET'} from ESPN's public schedule view."""
    url = URL.split("/segments/")[0] + "?view=proTeamSchedules_wl"
    with urllib.request.urlopen(url, timeout=30) as r:
        return {t["id"]: t["abbrev"] for t in json.load(r)["settings"]["proTeams"]}


def our_adds():
    """{player id: (how, [dropped player ids])} for our executed adds in ESPN's recent transactions."""
    try:
        data = fetch_view("mTransactions2")
    except SystemExit:
        return {}
    out = {}
    for t in data.get("transactions", []):
        if t.get("teamId") != TEAM_ID or t.get("status") != "EXECUTED":
            continue
        drops = [i["playerId"] for i in t.get("items", []) if i.get("type") == "DROP"]
        for i in t.get("items", []):
            if i.get("type") == "ADD":
                out[i["playerId"]] = (KIND.get(t.get("type"), (t.get("type") or "add").lower()), drops)
    return out


def fetch_view(view):
    s2, swid = os.environ.get("ESPN_S2"), os.environ.get("ESPN_SWID")
    req = urllib.request.Request(URL.split("?")[0] + f"?view={view}", headers={"Cookie": f"espn_s2={s2}; SWID={swid}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"ESPN returned HTTP {e.code} for {view}.")


def sync_roster(entries, today):
    """Rewrite roster.csv to match our ESPN roster entries. Returns the lines describing what changed."""
    with ROSTER.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    espn = {e["playerPoolEntry"]["player"]["fullName"]: e for e in entries}
    dropped = [r["player"] for r in rows if r["player"] not in espn]
    added = [n for n in espn if n not in {r["player"] for r in rows}]
    abbrev = pro_abbrevs() if added or rows else {}
    how = our_adds() if added else {}
    changes = []
    kept = []
    for r in rows:
        e = espn.get(r["player"])
        if e is None:
            changes.append(f"dropped {r['player']}")
            continue
        slot = "IR" if e["lineupSlotId"] == 13 else "roster"
        if slot != r["slot"]:
            note = f"moved to IR {today}" if slot == "IR" else f"back from IR {today}"
            r["notes"] = f'{r["notes"]}; {note}' if r.get("notes") else note
            changes.append(f"{r['player']}: {note}")
            r["slot"] = slot
        team = abbrev.get(e["playerPoolEntry"]["player"].get("proTeamId"))
        if team and team != r["team"]:
            r["notes"] = (f'{r["notes"]}; ' if r.get("notes") else "") + f"now {team} (was {r['team']}) {today}"
            r["team"] = team
        kept.append(r)
    for n in added:
        e, p = espn[n], espn[n]["playerPoolEntry"]["player"]
        kind, _ = how.get(p["id"], (KIND.get(e.get("acquisitionType"), "added"), []))
        if e.get("acquisitionType") == "ADD" and p["id"] not in how:
            kind = "free agent or waivers"
        when = dt.datetime.fromtimestamp(e.get("acquisitionDate", 0) / 1000, dt.timezone.utc).date() \
            if e.get("acquisitionDate") else today
        others = [d for d in dropped]
        note = (f"added for {others[0]} (dropped {when})" if len(added) == 1 and len(others) == 1
                else (f"added; dropped in the same sync: {', '.join(others)}" if others else "added"))
        kept.append({"player": n, "team": abbrev.get(p.get("proTeamId"), ""),
                     "pos": "/".join(POS[s] for s in sorted(p.get("eligibleSlots", [])) if s in POS),
                     "slot": "IR" if e["lineupSlotId"] == 13 else "roster", "acquired": kind,
                     "acquired_on": str(when), "notes": note})
        changes.append(f"added {n} ({kind}, {when})")
    if changes:
        with ROSTER.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator="\r\n")
            w.writeheader()
            w.writerows({k: r.get(k, "") for k in FIELDS} for r in kept)
    return changes


def read_taken():
    lines = TAKEN.read_text().splitlines() if TAKEN.exists() else []
    header = [l for l in lines if l.startswith("#")]
    names = [l.strip() for l in lines if l.strip() and not l.startswith("#")]
    return header, names


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", nargs="*", default=[], help="players to look up")
    ap.add_argument("--dry-run", action="store_true", help="report the differences only; write nothing")
    ap.add_argument("--write-taken", action="store_true", help=argparse.SUPPRESS)  # kept for old commands; the default now
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
    with ROSTER.open(newline="", encoding="utf-8") as f:
        csv_rows = {r["player"]: r for r in csv.DictReader(f)}
    espn_players = {p for p, _, _ in ours}
    ir_now = {p for p, slot, _ in ours if slot == "IR"}
    differs = (set(csv_rows) != espn_players
               or any((r["slot"] == "IR") != (p in ir_now) for p, r in csv_rows.items() if p in espn_players))
    if not differs:
        print("roster.csv matches ESPN.")
    elif args.dry_run:
        print("roster.csv differs from ESPN (--dry-run, nothing written):")
        for p in sorted(espn_players - set(csv_rows)):
            print(f"  on ESPN, missing from roster.csv: {p}")
        for p in sorted(set(csv_rows) - espn_players):
            print(f"  in roster.csv, not on ESPN: {p}")
    else:
        entries = next(t for t in league["teams"] if t["id"] == TEAM_ID)["roster"]["entries"]
        changes = sync_roster(entries, dt.datetime.now(dt.timezone.utc).date())
        print("roster.csv synced to ESPN: " + "; ".join(changes) + ".")

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

    if (gone or new) and not args.dry_run:
        keep = [p for p in taken if p in owner]
        TAKEN.write_text("\n".join(header + keep + new) + "\n")
        print(f"Wrote {TAKEN.name}: {len(keep) + len(new)} players.")


if __name__ == "__main__":
    main()
