#!/usr/bin/env python3
"""Opponent factors: how many fantasy points each NBA team gives up, by position.

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

council/matchup.py multiplies each player's rate by his opponent's factor for
that game: the mean of the factors at his eligible positions.

Usage:
  python council/opponents.py            # every team, softest first
  python council/opponents.py --shrink 8 # pull harder toward 1.00
"""
import argparse
import datetime as dt
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


def positions(r):
    """A pool row's eligible positions among PG, SG, SF, PF, C."""
    return [p for p in (r.get("pos") or "").split("/") if p in POSITIONS]


def factors(pool, now=None, shrink=SHRINK, cap=CAP):
    """{pro team id: {'PG'..'C', 'ALL': factor, 'games': n}} from this season's final box scores."""
    from gamelog import outliers
    from injury_watch import box
    now = now or dt.datetime.now(dt.timezone.utc)
    stamp = now.timestamp() * 1000
    games = {g["id"]: g["date"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
             for gs in t.get("proGamesByScoringPeriod", {}).values() for g in gs if g["date"] < stamp}
    with ThreadPoolExecutor(8) as ex:
        boxes = [b for b in ex.map(box, games) if b.get("final") and len(b["lines"]) == 2]

    logs = {}  # player id -> [(game key, min, FP, game key)], the shape council/gamelog.py's outliers() reads
    played = []  # (opponent team id, player id, minutes, FP, game key)
    for i, b in enumerate(boxes):
        (ta, la), (tb, lb) = b["lines"].items()
        for team, lines, opp in ((ta, la, tb), (tb, lb, ta)):
            for pid, (minutes, fp, _) in lines.items():
                logs.setdefault(int(pid), []).append((i, minutes, fp, i))
                played.append((int(opp), int(pid), minutes, fp, i))

    base, drops = {}, {}
    for pid, log in logs.items():
        drops[pid] = set(outliers(log))
        kept = [g[2] for g in log if g[3] not in drops[pid]]
        if len(kept) >= MIN_GAMES:
            base[pid] = sum(kept) / len(kept)

    keys = POSITIONS + ("ALL",)
    fp_vs = {}   # team -> key -> [FP scored against it, those players' averages]
    team_games = {}
    for opp, pid, minutes, fp, gkey in played:
        team_games.setdefault(opp, set()).add(gkey)
        r = pool.get(pid)
        if pid not in base or gkey in drops[pid] or r is None:
            continue
        pos = positions(r)
        cell = fp_vs.setdefault(opp, {k: [0.0, 0.0] for k in keys})
        cell["ALL"][0] += fp
        cell["ALL"][1] += base[pid]
        for p in pos:
            cell[p][0] += fp / len(pos)
            cell[p][1] += base[pid] / len(pos)

    n_all = sum(len(g) for g in team_games.values()) or 1
    league = {k: sum(c[k][1] for c in fp_vs.values()) / n_all for k in keys}  # expected FP per team-game
    out = {}
    for team, cell in fp_vs.items():
        out[team] = {"games": len(team_games.get(team, ()))}
        for k in keys:
            got, exp = cell[k]
            prior = shrink * league[k]
            f = (got + prior) / (exp + prior) if exp + prior else 1.0
            out[team][k] = min(1 + cap, max(1 - cap, f))
    return out


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


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--shrink", type=float, default=SHRINK, help=f"games of league-average defence mixed in (default {SHRINK})")
    args = ap.parse_args()
    from injury_watch import player_pool
    pool, _ = player_pool()
    abbrev = {t["id"]: t["abbrev"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]}
    fac = factors(pool, shrink=args.shrink)
    now = dt.datetime.now(dt.timezone.utc)
    print(f"# Opponent factors: {now.astimezone(ET):%d %b %Y}\n")
    print(f"- Generated {now:%Y-%m-%d %H:%M} UTC by `council/opponents.py`. FP opponents score against each team, "
          f"over those players' own averages (outlier games out, {MIN_GAMES}+ games), by position. Shrunk toward even "
          f"with {args.shrink:g} games of league-average defence and capped at ±{CAP:.0%}. Positive = soft matchup.\n")
    print("| Team | GP | All | PG | SG | SF | PF | C |\n|---|---:|---:|---:|---:|---:|---:|---:|")
    for team, f in sorted(fac.items(), key=lambda kv: -kv[1]["ALL"]):
        print(f'| {abbrev.get(team, team)} | {f["games"]} | **{pct(f["ALL"])}** | '
              + " | ".join(pct(f[p]) for p in POSITIONS) + " |")


if __name__ == "__main__":
    main()
