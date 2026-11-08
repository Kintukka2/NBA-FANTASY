#!/usr/bin/env python3
"""Opponent factors: how many fantasy points each NBA team gives up, by position, and an audit of them.

Stdlib only and read-only. Every completed game this season is read from ESPN's
box scores (cached in council/.cache/box) and league-scored. For each team,
every opponent's game against it is set against that opponent's own average:

    factor = FP scored against the team / what those players average

A factor of 1.06 means players score 6% more than their own average against
that team: a soft matchup. 0.94 is a tough one. It is split by position (PG,
SG, SF, PF, C; a player eligible at two positions counts half at each), so a
team that stops guards but leaks to centers shows both.

The method keeps it fair:

- **Averages:** each player's average leaves out his outlier games (the bad-game
  and short-game rules in council/gamelog.py). Those games are left out of the
  sums too, so an injury exit does not count as defence.
- **Sample:** only players with 3+ such games count.
- **Shrinkage:** early-season samples are small. Each factor is pulled toward
  1.00 as if the team had also played SHRINK games of exactly league-average
  defence. It is capped at +/-CAP.

**Not in the projections yet.** council/matchup.py shows the factor beside
each game but values games at the plain rate. Its `--opp` option applies the
factor as a what-if. The factor goes into the projections only once the audit
certifies it.

**The audit** (`--audit`) replays the season one game day at a time. For each
day, it rebuilds the factors and each player's average from the games played
before that day only, which is what this logic would have said at the time.
It then predicts every player-game on that day two ways:

    plain:  his average
    factor: his average x the opponent factor at his positions

and compares both with what he scored. It counts players with 3+ earlier
games, facing a team with AUDIT_TEAM_GAMES+ earlier games, who played 10+
minutes.

The factor is **certified** when all three hold:
- AUDIT_MIN+ player-games;
- it lowers the mean absolute error by a clear margin: the paired gain in
  absolute error is at least AUDIT_T standard errors above zero;
- soft and tough matchups (5%+ either way) both move the way it predicted.

The audit also tries other shrink settings, as evidence for tuning.

Usage:
  python council/opponents.py                  # every team, softest first
  python council/opponents.py --audit          # replay the season: does the factor beat the plain average?
  python council/opponents.py --audit --out docs/analysis/20261108-opponent-audit.md
"""
import argparse
import datetime as dt
import math
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from slump_watch import ET, FANTASY, get  # noqa: E402

POSITIONS = ("PG", "SG", "SF", "PF", "C")
SHRINK = 5     # games of league-average defence mixed into every factor
CAP = 0.15     # factors stay within 1 +/- CAP
MIN_GAMES = 3  # a player needs this many games (outliers left out) to count

AUDIT_MIN = 1000       # player-games the audit needs before it can certify
AUDIT_T = 2.0          # the factor's gain in absolute error must be this many standard errors above zero
AUDIT_TEAM_GAMES = 5   # an opponent needs this many earlier games for its factor to be tested
AUDIT_MINUTES = 10     # player-games under this many minutes (injury exits, garbage time) are not scored
BUCKETS = ((-1, -0.05, "tough (5%+ under)"), (-0.05, -0.02, "slightly tough"), (-0.02, 0.02, "even (within 2%)"),
           (0.02, 0.05, "slightly soft"), (0.05, 1, "soft (5%+ over)"))


def positions(r):
    """A pool row's eligible positions among PG, SG, SF, PF, C."""
    return [p for p in (r.get("pos") or "").split("/") if p in POSITIONS]


def load_games(now=None):
    """[(ET date, {team id: {player id: [min, FP, started]}})] for every final game, oldest first."""
    from injury_watch import box
    now = now or dt.datetime.now(dt.timezone.utc)
    stamp = now.timestamp() * 1000
    games = {g["id"]: g["date"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
             for gs in t.get("proGamesByScoringPeriod", {}).values() for g in gs if g["date"] < stamp}
    with ThreadPoolExecutor(8) as ex:
        boxes = dict(zip(games, ex.map(box, games)))
    out = [(dt.datetime.fromtimestamp(games[gid] / 1000, ET).date(), b["lines"])
           for gid, b in boxes.items() if b.get("final") and len(b["lines"]) == 2]
    return sorted(out, key=lambda g: g[0])


def averages(games):
    """({player id: average FP, outlier games out, MIN_GAMES+ games}, {player id: dropped game keys})."""
    from gamelog import outliers
    logs = {}
    for i, (day, lines) in enumerate(games):
        for team in lines.values():
            for pid, (minutes, fp, _) in team.items():
                logs.setdefault(int(pid), []).append((day, minutes, fp, i))
    base, drops = {}, {}
    for pid, log in logs.items():
        drops[pid] = set(outliers(log))
        kept = [g[2] for g in log if g[3] not in drops[pid]]
        if len(kept) >= MIN_GAMES:
            base[pid] = sum(kept) / len(kept)
    return base, drops


def compute(games, pool, shrink=SHRINK, cap=CAP):
    """{pro team id: {'PG'..'C', 'ALL': factor, 'games': n}} from the given games."""
    base, drops = averages(games)
    keys = POSITIONS + ("ALL",)
    fp_vs, team_games = {}, {}  # team -> key -> [FP scored against it, those players' averages]
    for i, (_, lines) in enumerate(games):
        (ta, la), (tb, lb) = lines.items()
        for team_lines, opp in ((la, int(tb)), (lb, int(ta))):
            team_games[opp] = team_games.get(opp, 0) + 1
            for pid, (minutes, fp, _) in team_lines.items():
                pid, r = int(pid), pool.get(int(pid))
                if pid not in base or i in drops[pid] or r is None:
                    continue
                pos = positions(r)
                cell = fp_vs.setdefault(opp, {k: [0.0, 0.0] for k in keys})
                cell["ALL"][0] += fp
                cell["ALL"][1] += base[pid]
                for p in pos:
                    cell[p][0] += fp / len(pos)
                    cell[p][1] += base[pid] / len(pos)
    n_all = sum(team_games.values()) or 1
    league = {k: sum(c[k][1] for c in fp_vs.values()) / n_all for k in keys}  # expected FP per team-game
    out = {}
    for team, cell in fp_vs.items():
        out[team] = {"games": team_games.get(team, 0)}
        for k in keys:
            got, exp = cell[k]
            prior = shrink * league[k]
            f = (got + prior) / (exp + prior) if exp + prior else 1.0
            out[team][k] = min(1 + cap, max(1 - cap, f))
    return out


def factors(pool, now=None, shrink=SHRINK, cap=CAP):
    """The factors from every final game this season (see compute)."""
    return compute(load_games(now), pool, shrink, cap)


def game_factor(fac, opp, pos):
    """The factor for a player with eligible positions `pos` ('PG/SG') facing team `opp`, or 1.0."""
    f = fac.get(opp) if fac else None
    if not f:
        return 1.0
    ps = [p for p in (pos or "").split("/") if p in POSITIONS]
    return sum(f[p] for p in ps) / len(ps) if ps else f["ALL"]


def pct(f):
    """'+6%' / '−4%' / '±0%' for a factor."""
    d = round((f - 1) * 100)
    return "±0%" if d == 0 else f"{d:+d}%".replace("-", "−")


def audit(pool, games=None, shrink=SHRINK, cap=CAP):
    """Replay the season day by day; score the plain average against average x factor. Returns a summary dict."""
    games = games if games is not None else load_games()
    days = sorted({d for d, _ in games})
    rows = []  # (actual, plain, factor)
    for day in days:
        before = [g for g in games if g[0] < day]
        if not before:
            continue
        fac = compute(before, pool, shrink, cap)
        base, _ = averages(before)
        for d, lines in games:
            if d != day:
                continue
            (ta, la), (tb, lb) = lines.items()
            for team_lines, opp in ((la, int(tb)), (lb, int(ta))):
                if fac.get(opp, {}).get("games", 0) < AUDIT_TEAM_GAMES:
                    continue
                for pid, (minutes, fp, _) in team_lines.items():
                    r = pool.get(int(pid))
                    if int(pid) not in base or minutes < AUDIT_MINUTES or r is None:
                        continue
                    f = game_factor(fac, opp, r.get("pos"))
                    rows.append((fp, base[int(pid)], base[int(pid)] * f, f))
    n = len(rows)
    out = {"n": n, "days": len(days), "shrink": shrink}
    if not n:
        return dict(out, verdict="not certified: no player-games to test yet", certified=False)
    gain = [abs(a - p) - abs(a - q) for a, p, q, _ in rows]  # > 0 when the factor was closer
    mean = sum(gain) / n
    sd = math.sqrt(sum((g - mean) ** 2 for g in gain) / (n - 1)) if n > 1 else 0.0
    t = mean / (sd / math.sqrt(n)) if sd else 0.0
    out.update(mae_plain=sum(abs(a - p) for a, p, _, _ in rows) / n,
               mae_factor=sum(abs(a - q) for a, _, q, _ in rows) / n,
               rmse_plain=math.sqrt(sum((a - p) ** 2 for a, p, _, _ in rows) / n),
               rmse_factor=math.sqrt(sum((a - q) ** 2 for a, _, q, _ in rows) / n),
               gain=mean, t=t)
    out["buckets"] = []
    for lo, hi, name in BUCKETS:
        b = [(a, p, f) for a, p, _, f in rows if lo <= f - 1 < hi]
        if b:
            out["buckets"].append({"name": name, "n": len(b),
                                   "predicted": sum(p * f for _, p, f in b) / sum(p for _, p, _ in b) - 1,
                                   "actual": sum(a for a, _, _ in b) / sum(p for _, p, _ in b) - 1})
    soft = next((b for b in out["buckets"] if b["name"].startswith("soft")), None)
    tough = next((b for b in out["buckets"] if b["name"].startswith("tough")), None)
    checks = [(n >= AUDIT_MIN, f"{n} player-games (needs {AUDIT_MIN})"),
              (t >= AUDIT_T, f"gain in absolute error {mean:+.3f} FP a game, t = {t:.2f} (needs {AUDIT_T:g})"),
              (bool(soft and soft["actual"] > 0), "soft matchups scored above average" if soft and soft["actual"] > 0
               else "soft matchups did not score above average"),
              (bool(tough and tough["actual"] < 0), "tough matchups scored below average"
               if tough and tough["actual"] < 0 else "tough matchups did not score below average")]
    out["checks"] = checks
    out["certified"] = all(ok for ok, _ in checks)
    out["verdict"] = ("certified" if out["certified"] else "not certified: "
                      + "; ".join(why for ok, why in checks if not ok))
    return out


def audit_line(a):
    """One line for a report header."""
    if not a.get("n"):
        return f'**Opponent factor audit:** {a["verdict"]}.'
    return (f'**Opponent factor audit** (`python council/opponents.py --audit`): over {a["n"]} player-games replayed '
            f'with only earlier games, mean absolute error {a["mae_plain"]:.2f} FP for the plain average and '
            f'{a["mae_factor"]:.2f} with the factor (t = {a["t"]:.2f}): **{a["verdict"]}**.')


def audit_report(pool, now):
    games = load_games(now)
    main = audit(pool, games)
    out = [f"# Opponent factor audit: {now.astimezone(ET):%d %b %Y}", "",
           f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/opponents.py --audit`. The season is replayed one game "
           f"day at a time ({main['days']} days). Each day's factors and player averages are rebuilt from earlier "
           "games only, then every player-game that day is predicted two ways: **plain** (his average, outlier games "
           "out) and **factor** (his average × the opponent factor at his positions).",
           f"- Counted: players with {MIN_GAMES}+ earlier games, facing a team with {AUDIT_TEAM_GAMES}+ earlier games, "
           f"who played {AUDIT_MINUTES}+ minutes. Factor settings: shrink {SHRINK}, cap ±{CAP:.0%}.",
           f"- **Certified** needs {AUDIT_MIN}+ player-games, a gain in absolute error at least {AUDIT_T:g} standard "
           "errors above zero, and soft and tough matchups both moving the predicted way.", ""]
    if not main.get("n"):
        return "\n".join(out + [f"**Verdict:** {main['verdict']}.", ""])
    out += [f"## Verdict: {main['verdict']}", ""]
    out += [f"- {'✓' if ok else '✗'} {why}" for ok, why in main["checks"]]
    out += ["", "## Errors", "", "| Prediction | Mean absolute error | Root mean square error |", "|---|---:|---:|",
            f'| Plain average | {main["mae_plain"]:.2f} | {main["rmse_plain"]:.2f} |',
            f'| Average × factor | {main["mae_factor"]:.2f} | {main["rmse_factor"]:.2f} |', "",
            "## Does the factor point the right way?", "",
            "Actual is what players scored against their own averages in those games; predicted is what the factor said.",
            "", "| Matchup | Player-games | Predicted | Actual |", "|---|---:|---:|---:|"]
    sign = lambda x: f"{x:+.1%}".replace("-", "\u2212")
    out += [f'| {b["name"]} | {b["n"]} | {sign(b["predicted"])} | {sign(b["actual"])} |' for b in main["buckets"]]
    out += ["", "## Other shrink settings", "",
            "More shrink pulls every factor harder toward even. The gain is in FP a game; positive means the factor "
            "beat the plain average.", "",
            "| Shrink (games) | Mean absolute error | Gain | t |", "|---:|---:|---:|---:|"]
    for s in (0, 3, SHRINK, 8, 12, 20):
        a = main if s == SHRINK else audit(pool, games, shrink=s)
        out.append(f'| {s}{" (in use)" if s == SHRINK else ""} | {a["mae_factor"]:.3f} | {a["gain"]:+.3f} | {a["t"]:.2f} |')
    out += ["", f'The plain average\'s mean absolute error is {main["mae_plain"]:.3f} at every setting.', "",
            "## Sources", "", f"- ESPN box scores (cached in `council/.cache/box`) and league 423671879 "
            f"(`kona_player_info`, `proTeamSchedules_wl`), read {now:%Y-%m-%d %H:%M} UTC.", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--shrink", type=float, default=SHRINK, help=f"games of league-average defence mixed in (default {SHRINK})")
    ap.add_argument("--audit", action="store_true", help="replay the season and test the factor against real results")
    ap.add_argument("--out", help="write the report here instead of stdout")
    args = ap.parse_args()
    from injury_watch import player_pool
    pool, _ = player_pool()
    now = dt.datetime.now(dt.timezone.utc)
    if args.audit:
        text = audit_report(pool, now)
    else:
        abbrev = {t["id"]: t["abbrev"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]}
        fac = factors(pool, shrink=args.shrink)
        lines = [f"# Opponent factors: {now.astimezone(ET):%d %b %Y}", "",
                 f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/opponents.py`. FP opponents score against each "
                 f"team, over those players' own averages (outlier games out, {MIN_GAMES}+ games), by position. Shrunk "
                 f"toward even with {args.shrink:g} games of league-average defence and capped at ±{CAP:.0%}. "
                 "Positive = soft matchup.",
                 "- **Not in the projections** until `--audit` certifies it; `matchup.py --opp` applies it as a what-if.",
                 "", "| Team | GP | All | PG | SG | SF | PF | C |", "|---|---:|---:|---:|---:|---:|---:|---:|"]
        for team, f in sorted(fac.items(), key=lambda kv: -kv[1]["ALL"]):
            lines.append(f'| {abbrev.get(team, team)} | {f["games"]} | **{pct(f["ALL"])}** | '
                         + " | ".join(pct(f[p]) for p in POSITIONS) + " |")
        text = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
