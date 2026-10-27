#!/usr/bin/env python3
"""Every injured NBA player, with ESPN's estimated return and their status in league 423671879.

Stdlib only, read-only. The injury feed is public. The fantasy status column
(our team, another team, free agent, waivers) needs the same cookies as
council/espn_sync.py (ESPN_S2, ESPN_SWID); without them that column is left
blank.

ESPN's return date is an estimate, often a placeholder:
  - day-to-day players get the next game day
  - long absences get ESPN's own guess
Where team or beat reporting gives a timeline, that wins. CLAUDE.md asks for
the reported timeline next to ESPN's estimate in every reply.

Usage:
  python council/injuries.py                    # markdown table, longest absence first
  python council/injuries.py --min-days 7       # only expected back more than 7 days from now
  python council/injuries.py --details          # add ESPN's latest note for each player
  python council/injuries.py --rostered         # only players on a team in our league
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

LEAGUE_ID = 423671879
SEASON = 2027
TEAM_ID = 5  # Come-in Cider
FEED = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/injuries"
LEAGUE = (f"https://lm-api-reads.fantasy.espn.com/apis/v3/games/fba/seasons/{SEASON}"
          f"/segments/0/leagues/{LEAGUE_ID}")


def get(url, headers=None):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers or {}), timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"{url} returned HTTP {e.code}.")


def injuries():
    """One dict per injured player in ESPN's feed, keyed by ESPN athlete id."""
    out = {}
    for team in get(FEED)["injuries"]:
        for x in team["injuries"]:
            det = x.get("details", {})
            pid = int(x["athlete"]["links"][0]["href"].split("/id/")[1].split("/")[0])
            what = " ".join(v for v in (det.get("side"), det.get("type"), det.get("detail"))
                            if v and v != "Not Specified")
            ret = det.get("returnDate")
            out[pid] = {"id": pid, "player": x["athlete"]["displayName"], "nba": team["displayName"],
                        "team_id": int(team["id"]),
                        "status": x["status"], "injury": what or "—",
                        "return": dt.date.fromisoformat(ret) if ret else None,
                        "updated": x["date"][:10], "note": x.get("shortComment", "")}
    return out


def fantasy_status():
    """{player id: (label, percent owned)} for the league, or {} without cookies."""
    s2, swid = os.environ.get("ESPN_S2"), os.environ.get("ESPN_SWID")
    if not s2 or not swid:
        return {}
    cookie = {"Cookie": f"espn_s2={s2}; SWID={swid}"}
    teams = {t["id"]: t["name"].strip() for t in get(f"{LEAGUE}?view=mTeam", cookie)["teams"]}
    filt = {"players": {"filterStatus": {"value": ["FREEAGENT", "WAIVERS", "ONTEAM"]}, "limit": 1000,
                        "sortPercOwned": {"sortPriority": 1, "sortAsc": False}}}
    pool = get(f"{LEAGUE}?view=kona_player_info", {**cookie, "x-fantasy-filter": json.dumps(filt)})
    out = {}
    for e in pool["players"]:
        if e["status"] == "ONTEAM":
            label = "**us**" if e["onTeamId"] == TEAM_ID else teams.get(e["onTeamId"], "rostered")
        else:
            label = e["status"].title().replace("Freeagent", "Free agent")
        out[e["id"]] = (label, (e["player"].get("ownership") or {}).get("percentOwned", 0))
    return out


def report(rows, owners, details, today):
    out = [f"# NBA injuries: {today:%d %b %Y}", "",
           f"{len(rows)} players. *ESPN est.* is ESPN's estimated return; day-to-day players get the "
           "next game day. Team or beat reporting overrides it.", "",
           "| Player | NBA | Status | Injury | ESPN est. | Days | Updated | League | Owned |",
           "|---|---|---|---|---|---:|---|---|---:|"]
    for r in rows:
        label, owned = owners.get(r["id"], ("—", None))
        days = (r["return"] - today).days if r["return"] else None
        out.append(f'| {r["player"]} | {r["nba"]} | {r["status"]} | {r["injury"]} | '
                   f'{r["return"]:%d %b %Y} | {days} | {r["updated"]} | {label} | '
                   f'{"" if owned is None else f"{owned:.0f}%"} |' if r["return"] else
                   f'| {r["player"]} | {r["nba"]} | {r["status"]} | {r["injury"]} | — | — | '
                   f'{r["updated"]} | {label} | {"" if owned is None else f"{owned:.0f}%"} |')
    if details:
        out += ["", "## ESPN notes", ""]
        out += [f'- **{r["player"]}** ({r["updated"]}): {r["note"]}' for r in rows if r["note"]]
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--min-days", type=int, help="only players expected back more than N days from now")
    ap.add_argument("--rostered", action="store_true", help="only players on a team in our league")
    ap.add_argument("--details", action="store_true", help="add ESPN's latest note for each player")
    args = ap.parse_args()

    today = dt.datetime.now(dt.timezone.utc).date()
    owners = fantasy_status()
    rows = sorted(injuries().values(), key=lambda r: (r["return"] or dt.date.max, r["player"]), reverse=True)
    if args.min_days is not None:
        rows = [r for r in rows if r["return"] and (r["return"] - today).days > args.min_days]
    if args.rostered:
        rows = [r for r in rows if r["id"] in owners and owners[r["id"]][0] not in ("Free agent", "Waivers")]
    print(report(rows, owners, args.details, today), end="")


if __name__ == "__main__":
    main()
