#!/usr/bin/env python3
"""Trade watch: NBA trades that change a player's opportunity, on the team he left and the team he joined.

Stdlib only and read-only. It reads ESPN's NBA transactions feed for trades in
the last --days days. For every traded player in league 423671879's pool
(rostered, free agent or waivers), it reports two sides:

  Team he left: the role he vacated (minutes, starts, FP/g with that team), and
      who has taken his minutes in the games since. That is a with/without
      split from ESPN's box scores, as in council/injury_watch.py. Before the
      old team has played without him, it lists the teammates at his
      positions, the likeliest heirs.
  Team he joined: the gap he can fill. That is the new team's long absences
      (ESPN's injury feed, out more than --min-days days) at his positions and
      the minutes they leave, the current depth at those positions, his role
      so far, and whose minutes he is taking.

Waived rotation players (--min-minutes or more a game this season) are listed
too: a release also opens minutes.

Fantasy flags mark free agents and waiver players who gain, and our players
whose role is at risk. Every flag is a question for the research step
(.claude/skills/trade-watch/SKILL.md), not a verdict.

It refuses to run while games are live (ESPN's averages would include
half-played games); --allow-live overrides that.

Usage:
  python council/trade_watch.py
  python council/trade_watch.py --days 60 --out docs/analysis/20261110-trade-watch.md --json trades.json
"""
import argparse
import datetime as dt
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from slump_watch import ET, FANTASY, LEAGUE, TEAM_ID, get, live_games, season_cell, window_cells  # noqa: E402

TX = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions?limit=100&page={page}"
TRADE = re.compile(r"\b(traded|acquired)\b", re.I)
WAIVED = re.compile(r"\bwaived\b", re.I)
POSITIONS = ("PG", "SG", "SF", "PF", "C")


def transactions():
    """Every transaction ESPN lists this season: [{date, team, team_id, text}], newest first."""
    out, page = [], 1
    while True:
        d = get(TX.format(page=page))
        for t in d.get("transactions", []):
            out.append({"date": dt.datetime.fromisoformat(t["date"].replace("Z", "+00:00")).astimezone(ET).date(),
                        "team": t["team"]["abbreviation"], "team_id": int(t["team"]["id"]),
                        "text": t["description"]})
        if page >= d.get("pageCount", 1):
            return out
        page += 1


def positions(r):
    return {p for p in (r.get("pos") or "").split("/") if p in POSITIONS}


def mean(xs):
    return sum(xs) / len(xs) if xs else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--days", type=int, default=30, help="trades this many days old or newer (default 30)")
    ap.add_argument("--games", type=int, default=10, help="recent team games read for depth and splits (default 10)")
    ap.add_argument("--min-days", type=int, default=7, help="an injury counts as a gap when ESPN expects it to last "
                    "longer than this (default 7)")
    ap.add_argument("--min-minutes", type=float, default=15, help="a waived player is listed when he averaged this many "
                    "minutes (default 15)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--json", help="also write the trades, with their splits, to this JSON file")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")
    from injuries import injuries as injury_feed
    from injury_watch import box, league_label, player_pool, team_split

    now = dt.datetime.now(dt.timezone.utc)
    today = now.astimezone(ET).date()
    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches[:20]))
    feed = injury_feed()
    teams = {t["id"]: t["name"].strip() for t in get(f"{LEAGUE}?view=mTeam", cookies=True)["teams"]}
    pro = get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
    abbrev = {t["id"]: t["abbrev"] for t in pro}
    stamp = now.timestamp() * 1000
    played = {t["id"]: sorted((dt.datetime.fromtimestamp(g["date"] / 1000, ET).date(), g["id"])
                              for gs in t.get("proGamesByScoringPeriod", {}).values() for g in gs if g["date"] < stamp)
              for t in pro}

    def team_games(tid):
        """[(ET date, game id, {team id: {player id: [min, FP, started]}})] for a team's final games, oldest first."""
        with ThreadPoolExecutor(8) as ex:
            boxes = list(ex.map(box, [gid for _, gid in played.get(tid, [])]))
        return [(d, gid, b["lines"]) for (d, gid), b in zip(played.get(tid, []), boxes) if b.get("final")]

    since = today - dt.timedelta(days=args.days)
    tx = [t for t in transactions() if t["date"] >= since]
    by_name = {}
    for r in pool.values():
        by_name.setdefault(r["player"], r)
    label = lambda r: league_label(r, teams).replace("**", "")
    cache = {}

    def games_of(tid):
        if tid not in cache:
            cache[tid] = team_games(tid)
        return cache[tid]

    # players named in trades: who moved, from where, to where, when
    moved = {}
    for t in tx:
        if not TRADE.search(t["text"]):
            continue
        for name, r in by_name.items():
            if name in t["text"] and r["id"] not in moved:
                new = r["pro"]
                before = [(d, lines) for d, _, lines in games_of(t["team_id"]) if d <= t["date"]]
                old = t["team_id"] if t["team_id"] != new else None
                if old is None:  # the new team's entry: find the team he played for before
                    for tid in played:
                        if tid != new and any(str(r["id"]) in lines.get(str(tid), {})
                                              for d, _, lines in games_of(tid) if d <= t["date"]):
                            old = tid
                moved[r["id"]] = {"r": r, "date": t["date"], "old": old, "new": new, "text": t["text"]}

    def role(pid, tid, after=None, before=None):
        """{gp, min, fp, starts} of a player's games for a team, optionally only after/before a date."""
        lines = [lines[str(tid)][str(pid)] for d, _, lines in games_of(tid)
                 if str(tid) in lines and str(pid) in lines[str(tid)]
                 and (after is None or d > after) and (before is None or d <= before)]
        return {"gp": len(lines), "min": mean([x[0] for x in lines]), "fp": mean([x[1] for x in lines]),
                "starts": sum(x[2] for x in lines)} if lines else {"gp": 0}

    fmt_role = lambda s: (f'{s["gp"]} GP, {s["min"]:.1f} min, {s["fp"]:.1f} FP/g, started {s["starts"]}'
                          if s.get("gp") else "no games")
    status = lambda r: (f'{feed[r["id"]]["status"].lower()}' + (f', ESPN est. {feed[r["id"]]["return"]:%d %b}'
                        if feed[r["id"]]["return"] else "") if r["id"] in feed else "active")
    out = [f"# Trade watch: {today:%d %b %Y}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/trade_watch.py`. This is **data, not a verdict**: "
           "each trade is a question for the research step.",
           f"- **Trades read:** ESPN's NBA transactions feed, {since:%d %b} to {today:%d %b} ({args.days} days). "
           f"{len(moved)} traded player{' is' if len(moved) == 1 else 's are'} in the league pool (rostered, free agent or "
           "waivers).",
           "- **Team he left:** his role there, and who has taken his minutes since (games without him against "
           "games with him, from ESPN's box scores). **Team he joined:** long absences at his positions "
           f"(ESPN expects them out more than {args.min_days} days), the depth there, and whose minutes he takes.",
           "- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g "
           "over the last 7, 15 and 30 days, games in brackets.", ""]
    dump = []
    if not moved:
        out += ["No trade in the window involves a player in the league pool.", ""]
    else:
        out += ["## Summary", "", "| Date | Player | From → To | Role before | Role since | Rate | League |",
                "|---|---|---|---|---|---:|---|"]
        for m in sorted(moved.values(), key=lambda m: m["date"], reverse=True):
            r = m["r"]
            m["before"] = role(r["id"], m["old"], before=m["date"]) if m["old"] else {"gp": 0}
            m["after"] = role(r["id"], m["new"], after=m["date"])
            out.append(f'| {m["date"]:%d %b} | **{r["player"]}** | {abbrev.get(m["old"], "?")} → {abbrev.get(m["new"])} | '
                       f'{fmt_role(m["before"])} | {fmt_role(m["after"])} | {r.get("wrate") or 0:.1f}'
                       f'{" †" if r.get("small") else ""} | {label(r)} |')
        out.append("")

    for m in sorted(moved.values(), key=lambda m: m["date"], reverse=True):
        r, old, new = m["r"], m["old"], m["new"]
        pos = positions(r)
        l7, l15, l30 = window_cells(r)
        out += [f'## {r["player"]}: {abbrev.get(old, "?")} → {abbrev.get(new)} ({m["date"]:%d %b})', "",
                f'- ESPN: "{m["text"]}"',
                f'- {r["pos"]} · {label(r)} · rate **{r.get("wrate") or 0:.1f}**'
                + (" (small sample)" if r.get("small") else "")
                + f' · season {season_cell(r)} · L7 {l7} · L15 {l15} · L30 {l30}'
                + (f' · projected {r["projected"]["fpg"]:.1f}' if r.get("projected") else "")
                + f' · {status(r)}',
                f'- With {abbrev.get(old, "?")}: {fmt_role(m["before"])}. With {abbrev.get(new)}: {fmt_role(m["after"])}.',
                ""]
        entry = {"player": r["player"], "id": r["id"], "date": str(m["date"]), "from": abbrev.get(old),
                 "to": abbrev.get(new), "text": m["text"], "pos": r["pos"], "league": label(r),
                 "rate": round(r.get("wrate") or 0, 1), "before": m["before"], "after": m["after"],
                 "windows": {"season": season_cell(r), "l7": l7, "l15": l15, "l30": l30}}

        # the team he left: who takes his minutes
        out += [f"### The team he left: {abbrev.get(old, '?')}", ""]
        if old is None:
            out += ["- ESPN's feed does not show which team he left, and he has no game for another team this season.", ""]
        else:
            g = games_of(old)[-args.games:]
            since_n = sum(1 for d, _, _ in g if d > m["date"])
            vac = m["before"]
            out.append(f'- **Role vacated:** {fmt_role(vac)}.'
                       + (" A small role: little opportunity opens." if vac.get("gp") and vac["min"] < args.min_minutes
                          else ""))
            if since_n:
                n_wo, n_w, mates, _ = team_split([{"lines": lines} for _, _, lines in g], {r["id"]}, old, pool)
                gainers = sorted((x for x in mates if x.get("gain") is not None), key=lambda x: -x["gain"])[:8]
                out += [f"- **Since the trade** ({n_wo} games without him, against {n_w} with him):", "",
                        "| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |",
                        "|---|---|---|---|---|---:|---:|"]
                out += [f'| {x["player"]} | {x["pos"]} | {label(x)} | {x["wo_min"]:.1f} / {x["base_min"]:.1f} | '
                        f'{x["wo_fp"]:.1f} / {x["base_fp"]:.1f} | {x["wo_starts"]} of {x["n_wo"]} | '
                        f'{x.get("wrate") or 0:.1f} |' for x in gainers]
                entry["old_team_gainers"] = [{"player": x["player"], "league": label(x), "min_without": round(x["wo_min"], 1),
                                              "min_with": round(x["base_min"], 1), "fp_without": round(x["wo_fp"], 1)}
                                             for x in gainers]
            else:
                heirs = []
                for x in pool.values():
                    if x["pro"] == old and x["id"] != r["id"] and positions(x) & pos:
                        s = role(x["id"], old, after=(g[0][0] - dt.timedelta(days=1)) if g else None)
                        if s.get("gp"):
                            heirs.append((x, s))
                heirs.sort(key=lambda h: -h[1]["min"])
                out += [f"- No game yet since the trade. His teammates at {'/'.join(sorted(pos))}, last {len(g)} games:", "",
                        "| Teammate | Pos | League | Role | Rate |", "|---|---|---|---|---:|"]
                out += [f'| {x["player"]} | {x["pos"]} | {label(x)} | {fmt_role(s)} | {x.get("wrate") or 0:.1f} |'
                        for x, s in heirs[:8]]
                entry["old_team_heirs"] = [{"player": x["player"], "league": label(x), "min": round(s["min"], 1)}
                                           for x, s in heirs[:8]]
            out.append("")

        # the team he joined: the gap he fills
        out += [f"### The team he joined: {abbrev.get(new)}", ""]
        gap = []
        for pid, i in feed.items():
            x = pool.get(pid)
            long = i["status"].lower() == "out" and (i["return"] is None or (i["return"] - today).days > args.min_days)
            if x and x["pro"] == new and long and positions(x) & pos:
                gap.append((x, i))
        if gap:
            out += [f"- **Long absences at his positions** ({'/'.join(sorted(pos))}):", "",
                    "| Player | Pos | Injury | ESPN est. | Min/g this season | FP/g |", "|---|---|---|---|---:|---:|"]
            for x, i in sorted(gap, key=lambda t: -((t[0].get("current") or t[0].get("last") or {}).get("min") or 0)):
                c = x.get("current") or x.get("last") or {}
                ret = f'{i["return"]:%d %b}' if i["return"] else "—"
                out.append(f'| {x["player"]} | {x["pos"]} | {i["injury"]} | {ret} | {c.get("min", 0):.1f} | '
                           f'{c.get("fpg", 0):.1f} |')
            freed = sum(((x.get("current") or x.get("last") or {}).get("min") or 0) for x, _ in gap)
            out += ["", f"- About **{freed:.0f} minutes a game** at his positions are out long-term (their season "
                    "or last-season minutes)."]
        else:
            out.append(f"- No long absence at his positions ({'/'.join(sorted(pos)) or '?'}).")
        g = games_of(new)[-args.games:]
        depth = []
        for x in pool.values():
            if x["pro"] == new and x["id"] != r["id"] and positions(x) & pos and x["id"] not in {y["id"] for y, _ in gap}:
                s = role(x["id"], new, after=(g[0][0] - dt.timedelta(days=1)) if g else None)
                if s.get("gp"):
                    depth.append((x, s))
        depth.sort(key=lambda h: -h[1]["min"])
        out += [f"- **Depth at his positions**, last {len(g)} games:", "",
                "| Player | Pos | League | Role | Rate |", "|---|---|---|---|---:|"]
        out += [f'| {x["player"]} | {x["pos"]} | {label(x)} | {fmt_role(s)} | {x.get("wrate") or 0:.1f} |'
                for x, s in depth[:8]]
        out.append("")
        if m["after"].get("gp"):
            n_wo, n_w, mates, _ = team_split([{"lines": lines} for _, _, lines in g], {r["id"]}, new, pool)
            losers = sorted((x for x in mates if x.get("gain") is not None and x["base"] == "with"),
                            key=lambda x: x["gain"], reverse=True)[:6]
            out += [f"- **Whose minutes he takes** ({n_w} games with him, {n_wo} before him): minutes before / with him.", ""]
            out += [f'  - {x["player"]} ({label(x)}): {x["wo_min"]:.1f} → {x["base_min"]:.1f} min' for x in losers
                    if x["gain"] > 1]
            out.append("")
        entry["new_team_gap"] = [{"player": x["player"], "injury": i["injury"], "return": str(i["return"]),
                                  "min": ((x.get("current") or x.get("last") or {}).get("min"))} for x, i in gap]
        entry["new_team_depth"] = [{"player": x["player"], "league": label(x), "min": round(s["min"], 1),
                                    "starts": s["starts"], "gp": s["gp"]} for x, s in depth[:8]]
        out += ["### Research", "", "- _pending_", ""]
        dump.append(entry)

    # waived rotation players
    waived = []
    for t in tx:
        if WAIVED.search(t["text"]):
            for name, r in by_name.items():
                if name in t["text"]:
                    s_ = role(r["id"], t["team_id"], before=t["date"])  # his role with the team that waived him
                    if s_.get("gp") and s_["min"] >= args.min_minutes:
                        waived.append((t, r, s_))
    if waived:
        out += ["## Waived rotation players", "",
                f"Released after playing {args.min_minutes:g}+ minutes a game for the team that waived them: those "
                "minutes are open.", "", "| Date | Player | Team | Role there | Now |", "|---|---|---|---|---|"]
        out += [f'| {t["date"]:%d %b} | {r["player"]} | {t["team"]} | {fmt_role(s_)} | '
                f'{abbrev.get(r["pro"], "?")}, {label(r)} |' for t, r, s_ in waived]
        out.append("")

    out += ["## Sources", "",
            f"- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), "
            f"ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 "
            f"(`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read {now:%Y-%m-%d %H:%M} UTC.", ""]
    text = "\n".join(out)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}: {len(moved)} traded players.")
    else:
        print(text)
    if args.json:
        Path(args.json).write_text(json.dumps(dump, indent=1, default=str), encoding="utf-8")


if __name__ == "__main__":
    main()
