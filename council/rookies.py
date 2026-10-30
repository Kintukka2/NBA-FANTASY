#!/usr/bin/env python3
"""Rookie report: what this season's rookies score against ESPN's projection, and an estimate for one.

Stdlib only and read-only against ESPN. It uses the same two cookies as
council/espn_sync.py.

  - Rookies: every player with 0 years' experience on ESPN's NBA rosters, with
    his draft pick from ESPN's core API.
  - Actual: this season's league-scored FP/g and minutes (re-scored with
    scripts/league_scoring.py), and his starts from ESPN's box scores.
  - Projected: ESPN's 2027 projection, re-scored the same way. It leaves out
    OREB, DREB, DD and TD, so it understates every player, bigs most. The
    report sets the rookies' ratio against the same ratio for veterans.
  - Preseason: league-scored FP per 36 minutes from ESPN's preseason box scores.

The estimate for --player uses two methods, and gives both:
  1. Projection: his projected FP/g times the median actual/projected ratio
     of comparable rookies (lottery picks with --min-gp games).
  2. Preseason: his preseason FP/36, times the median ratio of rookies'
     regular-season FP/36 to their preseason FP/36, at his projected minutes.

Guards, as in slump_watch.py:
  - It refuses to run while NBA games are live. --allow-live overrides this.
  - Every season average must re-score with scripts/league_scoring.py to
    ESPN's total.

Usage:
  python council/rookies.py --player "AJ Dybantsa"
  python council/rookies.py --player "AJ Dybantsa" --out docs/analysis/20261028-rookies.md
"""
import argparse
import datetime as dt
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from injuries import injuries as injury_feed  # noqa: E402
from injury_watch import box, player_pool  # noqa: E402
from slump_watch import LEAGUE, SITE, WINDOWS, get, live_games, window_cells, windows_note  # noqa: E402

CORE = "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba"
LOTTERY = 14
TOP = 5


def per36(fp, minutes):
    return fp / minutes * 36 if minutes else None


def median(xs):
    return statistics.median(xs) if xs else None


def quartiles(xs):
    if len(xs) < 4:
        return None, None
    q = statistics.quantiles(xs, n=4)
    return q[0], q[2]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--player", help="the rookie to estimate, e.g. \"AJ Dybantsa\"")
    ap.add_argument("--min-gp", type=int, default=3, help="games a rookie needs to count in the ratios (default 3)")
    ap.add_argument("--min-proj-min", type=float, default=20,
                    help="projected minutes a player needs to count in the ratios (default 20)")
    ap.add_argument("--top", type=int, default=25, help="rookies listed in the main table (default 25)")
    ap.add_argument("--out", help="write the report here instead of stdout")
    ap.add_argument("--allow-live", action="store_true", help="run even while games are in progress")
    args = ap.parse_args()

    live = live_games()
    if live and not args.allow_live:
        sys.exit("Games in progress, so ESPN's averages include half-played games:\n  "
                 + "\n  ".join(live) + "\nRun again once they are final, or pass --allow-live.")

    now = dt.datetime.now(dt.timezone.utc)
    pool, mismatches = player_pool()
    if mismatches:
        sys.exit("league_scoring.py no longer reproduces ESPN:\n  " + "\n  ".join(mismatches[:20]))
    feed = injury_feed()
    league = get(f"{LEAGUE}?view=mTeam", cookies=True)
    owners = {t["id"]: t["name"].strip() for t in league["teams"]}

    nba = [t["team"] for t in get(f"{SITE}/teams")["sports"][0]["leagues"][0]["teams"]]
    abbrev = {int(t["id"]): t["abbreviation"] for t in nba}
    with ThreadPoolExecutor(8) as ex:
        rosters = list(ex.map(lambda t: (int(t["id"]), get(f"{SITE}/teams/{t['id']}/roster")), nba))
        pre_scheds = list(ex.map(lambda t: get(f"{SITE}/teams/{t['id']}/schedule?seasontype=1"), nba))
        reg_scheds = list(ex.map(lambda t: (int(t["id"]), get(f"{SITE}/teams/{t['id']}/schedule?seasontype=2")), nba))
    rookies = {int(a["id"]): tid for tid, r in rosters for a in r["athletes"]
               if (a.get("experience") or {}).get("years") == 0}
    def draft(pid):
        try:
            return get(f"{CORE}/athletes/{pid}").get("draft")
        except SystemExit:  # no core record for this athlete
            return None
    with ThreadPoolExecutor(8) as ex:
        drafts = dict(zip(rookies, ex.map(draft, rookies)))

    done = lambda e: e["competitions"][0]["status"]["type"]["state"] == "post"
    pre_ids = sorted({e["id"] for s in pre_scheds for e in s.get("events", []) if done(e)})
    reg_ids = {tid: [e["id"] for e in s.get("events", []) if done(e)] for tid, s in reg_scheds}
    with ThreadPoolExecutor(8) as ex:
        boxes = dict(zip(pre_ids, ex.map(box, pre_ids)))
        reg = dict(zip(sorted({g for gs in reg_ids.values() for g in gs}),
                       ex.map(box, sorted({g for gs in reg_ids.values() for g in gs}))))

    preseason = {}  # player id -> [minutes, FP]
    for b in boxes.values():
        for lines in b["lines"].values():
            for pid, (m, fp, _) in lines.items():
                t = preseason.setdefault(int(pid), [0, 0.0])
                t[0] += m
                t[1] += fp
    starts = {}
    for tid, gs in reg_ids.items():
        for g in gs:
            for pid, (_, _, s) in reg[g]["lines"].get(str(tid), {}).items():
                t = starts.setdefault(int(pid), [0, 0])
                t[0] += s
                t[1] += 1

    rows = []
    for pid, tid in rookies.items():
        r = pool.get(pid)
        if not r:
            continue
        d = drafts.get(pid) or {}
        pick = (d.get("round"), d.get("selection")) if d.get("year") == 2026 else None
        cur, proj = r["current"], r["projected"]
        pm, pfp = preseason.get(pid, (0, 0.0))
        rows.append({**r, "nba": abbrev.get(tid), "pick": pick,
                     "overall": (pick[0] - 1) * 30 + pick[1] if pick else None,
                     "pre36": per36(pfp, pm) if pm >= 20 else None, "pre_min": pm,
                     "cur36": per36(cur["fpg"], cur["min"]) if cur else None,
                     "proj36": per36(proj["fpg"], proj["min"]) if proj else None,
                     "starts": starts.get(pid)})

    qualifies = lambda r: (r["current"] and r["current"]["gp"] >= args.min_gp and r["projected"]
                           and r["projected"]["min"] >= args.min_proj_min)
    ratio = lambda r: r["current"]["fpg"] / r["projected"]["fpg"]
    groups = {
        f"Rookies, picks 1–{LOTTERY}": [r for r in rows if qualifies(r) and r["overall"] and r["overall"] <= LOTTERY],
        f"Rookies, picks 1–{TOP}": [r for r in rows if qualifies(r) and r["overall"] and r["overall"] <= TOP],
        "Veterans (baseline)": [r for r in pool.values() if r["id"] not in rookies and qualifies(r)],
    }

    fmt = lambda x, d=1: "—" if x is None else f"{x:.{d}f}"
    pick_s = lambda r: (f'{r["overall"]}' if r["pick"] and r["pick"][0] == 1 else
                        f'R{r["pick"][0]} #{r["pick"][1]}' if r["pick"] else "undrafted")
    status = lambda r: (f'{owners.get(r["owner"], "")}' if r["league"] == "ONTEAM" else
                        "waivers" if r["league"] == "WAIVERS" else "free agent")
    injury = lambda r: (f'{feed[r["id"]]["status"].lower()}, {feed[r["id"]]["injury"].lower()}, ESPN est. '
                        f'{feed[r["id"]]["return"]:%d %b}' if r["id"] in feed and feed[r["id"]]["return"] else
                        (feed[r["id"]]["status"].lower() if r["id"] in feed else ""))

    out = ["# Rookies against projection", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/rookies.py`. This is **a report, not a council verdict**.",
           f"- **Rookies:** {len(rookies)} players with 0 years' experience on ESPN's NBA rosters, {len(rows)} of them in "
           "the league's player pool. Draft picks come from ESPN's core API.",
           "- **Actual:** this season's FP/g in our scoring. **Projected:** ESPN's 2027 projection re-scored with "
           "`scripts/league_scoring.py`. The projection leaves out OREB, DREB, DD and TD, so it reads low for "
           "everyone; the veterans' ratio is the baseline for that.",
           f"- **Preseason FP/36:** league-scored from ESPN's preseason box scores ({len(pre_ids)} games), for players "
           "with 20+ preseason minutes.",
           f"- **Ratios** use players with {args.min_gp}+ games and {args.min_proj_min:g}+ projected minutes.",
           f"- **Checks:** {'**games were live** (--allow-live)' if live else 'no NBA game was in progress'}. "
           f"All {len(pool)} pool players' current, L7, L15, L30, projected and 2026 averages re-score with "
           "`scripts/league_scoring.py` (0 mismatches).",
           windows_note(rows), ""]

    out += ["## Actual against projected", "",
            "| Group | Players | Median actual ÷ projected FP/g | Middle half | Median minutes ratio | Median FP/36 ratio |",
            "|---|---:|---:|---|---:|---:|"]
    summary = {}
    for name, g in groups.items():
        rs = sorted(ratio(r) for r in g)
        lo, hi = quartiles(rs)
        summary[name] = (median(rs), lo, hi)
        out.append(f"| {name} | {len(g)} | **{fmt(median(rs), 2)}** | "
                   f"{fmt(lo, 2)}–{fmt(hi, 2)} | {fmt(median([r['current']['min'] / r['projected']['min'] for r in g]), 2)} | "
                   f"{fmt(median([(r['current']['fpg'] / r['current']['min']) / (r['projected']['fpg'] / r['projected']['min']) for r in g]), 2)} |")
    lot, vet = summary[f"Rookies, picks 1–{LOTTERY}"][0], summary["Veterans (baseline)"][0]
    if lot and vet:
        out += ["", f"Against the veterans' baseline, lottery rookies are running at **{lot / vet:.2f}×** what ESPN "
                "projected for them."]
    scored = [r for r in rows if r["current"] and r["current"]["gp"] >= args.min_gp]
    out += ["", f"Rookies with {args.min_gp}+ games at **35+ FP/g: {sum(r['current']['fpg'] >= 35 for r in scored)}**; "
            f"at **40+: {sum(r['current']['fpg'] >= 40 for r in scored)}** (of {len(scored)}).", ""]

    out += ["## The rookie class", "",
            "Sorted by current FP/g. Draft pick is overall for the first round.", "",
            "| Pick | Player | NBA | Pos | GP | Min | Started | FP/g | L7 | L15 | L30 | Projected FP/g (min) | "
            "Actual ÷ projected | Preseason FP/36 | FP/36 now | League | Status |",
            "|---:|---|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|"]
    listed = sorted(rows, key=lambda r: -(r["current"]["fpg"] if r["current"] else -1))
    for r in [r for r in listed if r["current"]][:args.top]:
        c, p = r["current"], r["projected"]
        st = f'{r["starts"][0]} of {r["starts"][1]}' if r["starts"] else "—"
        out.append(f'| {pick_s(r)} | **{r["player"]}** | {r["nba"]} | {r["pos"]} | {c["gp"]} | {c["min"]:.1f} | {st} | '
                   f'**{c["fpg"]:.1f}** | ' + " | ".join(window_cells(r)) + f' | {fmt(p and p["fpg"])} ({fmt(p and p["min"])}) | '
                   f'{fmt(c["fpg"] / p["fpg"] if p and p["fpg"] else None, 2)} | {fmt(r["pre36"])} | {fmt(r["cur36"])} | '
                   f'{status(r)} | {injury(r)} |')
    unplayed = [r for r in rows if not r["current"] and r["projected"] and r["projected"]["fpg"] >= 20]
    if unplayed:
        out += ["", "Rookies yet to play who project for 20+ FP/g: " + "; ".join(
            f'{r["player"]} ({r["nba"]}, pick {pick_s(r)}, projected {r["projected"]["fpg"]:.1f}'
            + (f', {injury(r)}' if injury(r) else "") + ")" for r in sorted(unplayed, key=lambda r: -r["projected"]["fpg"])) + "."]
    out.append("")

    pairs = [r for r in rows if r["pre36"] and r["cur36"] and r["current"]["gp"] >= args.min_gp]
    keep = median([r["cur36"] / r["pre36"] for r in pairs])
    out += ["## Preseason to regular season", "",
            f"Rookies with {args.min_gp}+ games and 20+ preseason minutes: **{len(pairs)}**. The median rookie is "
            f"scoring **{fmt(keep, 2)}×** his preseason FP/36 in the regular season.", ""]

    if args.player:
        target = next((r for r in rows if r["player"].lower() == args.player.lower()), None)
        if target is None:
            sys.exit(f"Not a rookie in the league's player pool: {args.player}")
        p = target["projected"]
        lo_r, hi_r = summary[f"Rookies, picks 1–{LOTTERY}"][1:]
        top = summary[f"Rookies, picks 1–{TOP}"][0]
        est1 = p["fpg"] * lot if p and lot else None
        est3 = p["fpg"] * top if p and top else None
        est2 = target["pre36"] * keep * p["min"] / 36 if target["pre36"] and keep and p else None
        out += [f"## Estimate: {target['player']}", "",
                f"- **{target['player']}** ({target['nba']}, {target['pos']}, pick {pick_s(target)}): "
                f"{status(target)}{', ' + injury(target) if injury(target) else ''}.",
                f"- **ESPN projects** {fmt(p and p['fpg'])} FP/g in {fmt(p and p['min'])} minutes "
                f"({fmt(target['proj36'])} FP/36).",
                f"- **Preseason:** {fmt(target['pre36'])} FP/36 over {target['pre_min']} minutes.",
                f"- **This season:** " + (f"{target['current']['fpg']:.1f} FP/g in {target['current']['gp']} "
                                          f"game{'s' if target['current']['gp'] != 1 else ''}; "
                                          if target["current"] else "no games yet; ")
                + ", ".join(f"{k} {v}" for k, v in zip(WINDOWS.values(), window_cells(target))) + ".", "",
                "| Method | Estimate FP/g | Range |", "|---|---:|---|"]
        if est1:
            out.append(f"| Projection × lottery rookies' median ratio ({lot:.2f}) | **{est1:.1f}** | "
                       + (f"{p['fpg'] * lo_r:.1f}–{p['fpg'] * hi_r:.1f} (middle half of lottery rookies) |" if lo_r else "— |"))
        if est3:
            out.append(f"| Projection × top-{TOP} picks' median ratio ({top:.2f}) | **{est3:.1f}** | — |")
        if est2:
            out.append(f"| Preseason FP/36 × rookies' carry-over ({keep:.2f}) at {p['min']:.1f} min | **{est2:.1f}** | — |")
        out.append("")

    out += ["## Sources", "",
            f"- ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`), ESPN's NBA rosters, schedules, box "
            f"scores and core athlete API, and ESPN's injury feed, read {now:%Y-%m-%d %H:%M} UTC.", ""]
    report = "\n".join(out)
    if args.out:
        Path(args.out).write_text(report)
        print(f"Wrote {args.out}")
    else:
        print(report)


if __name__ == "__main__":
    main()
