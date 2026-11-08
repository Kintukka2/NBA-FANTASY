#!/usr/bin/env python3
"""Game logs from ESPN box scores, the two outlier rules, and the weighted rate.

Stdlib only and read-only. Every completed game this season is read once
from ESPN's box scores (cached in council/.cache/box by injury_watch.box) and
league-scored, which gives each player a game log: date, minutes, FP.

The log is checked against ESPN's own splits: a player's season must hold
the same number of games as ESPN's, or he keeps ESPN's splits and no
outliers. For L7, L15 and L30 the box scores decide which games fall in the
window: ESPN keeps an injured player's last game in his L7 and L15 after he
stops playing, so where ESPN's game count differs, the log's window replaces
ESPN's. Windows are the N
days ending on the last day with a completed game, inclusive, as ESPN counts
them. ESPN's totals stay the source of truth (its later stat corrections can
move a cached box score by a point or two): an adjusted average is ESPN's
window total minus the dropped games' logged FP, over the games left. A
player whose game counts do not match keeps ESPN's splits, with no outliers.

Outlier rules, on the season's games (at most one game each):
  - Bad game: with 3+ games, the worst FP game is dropped when it is 12+ FP
    below the second worst. A single bad night (foul trouble, an off night)
    should not drag the average. Good games are never dropped.
  - Short game: with 2+ games, the game with the fewest minutes is dropped
    when it is more than 10 minutes below the second fewest. It catches early
    injury exits and ejections.
Each window (season, L30, L15, L7) is then averaged again without the dropped
games: the *adjusted* averages. Both are shown; the rate uses the adjusted.

Small sample: a rate whose season part rests on 2 games or fewer (after any
dropped outlier) is flagged, and every report says so beside it.

Weighted rate per game (the projection every report uses):
    last season x1 (ESPN's projection if there is no last season)
    this season x2, last 30 days x3, last 15 days x4, last 7 days x5
using the adjusted averages, and skipping any part with no games. A player
with no game this season is rated on last season, else the projection.

Usage (a player's log, averages and rate):
  python council/gamelog.py "Rui Hachimura"
"""
import datetime as dt
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from slump_watch import ET, FANTASY, get  # noqa: E402

BAD_GAME_FP = 12     # worst game this far below the second worst is dropped
SHORT_GAME_MIN = 10  # fewest minutes more than this below the second fewest is dropped
SMALL_SAMPLE = 2   # a rate whose season part rests on this many games or fewer is flagged
WEIGHTS = {"base": 1, "current": 2, "l30": 3, "l15": 4, "l7": 5}
DAYS = {"l7": 7, "l15": 15, "l30": 30}
FIXED = []  # windows where ESPN's split disagreed with the box scores and the log replaced it


def season_logs(now=None):
    """({player id: [(ET date, minutes, FP, game id)]}, last completed ET date) from final box scores."""
    from injury_watch import box  # imported here: injury_watch imports this module
    now = now or dt.datetime.now(dt.timezone.utc)
    stamp = now.timestamp() * 1000
    games = {g["id"]: g["date"] for t in get(f"{FANTASY}?view=proTeamSchedules_wl")["settings"]["proTeams"]
             for gs in t.get("proGamesByScoringPeriod", {}).values() for g in gs if g["date"] < stamp}
    with ThreadPoolExecutor(8) as ex:
        boxes = dict(zip(games, ex.map(box, games)))
    logs, last = {}, None
    for gid, b in boxes.items():
        if not b.get("final"):
            continue
        day = dt.datetime.fromtimestamp(games[gid] / 1000, ET).date()
        last = max(last or day, day)
        for lines in b["lines"].values():
            for pid, (minutes, fp, _) in lines.items():
                logs.setdefault(int(pid), []).append((day, minutes, fp, gid))
    for v in logs.values():
        v.sort()
    return logs, last


def outliers(log):
    """The games the two rules drop, as {game id: reason}."""
    out = {}
    if len(log) >= 2:
        by_min = sorted(log, key=lambda g: g[1])
        if by_min[1][1] - by_min[0][1] > SHORT_GAME_MIN:
            out[by_min[0][3]] = f"short game: {by_min[0][1]} min against a next-lowest {by_min[1][1]}"
    if len(log) >= 3:
        by_fp = sorted(log, key=lambda g: g[2])
        if by_fp[1][2] - by_fp[0][2] >= BAD_GAME_FP:
            out.setdefault(by_fp[0][3], f"bad game: {by_fp[0][2]:.1f} FP against a next-worst {by_fp[1][2]:.1f}")
    return out


def _avg(games):
    return {"gp": len(games), "fpg": sum(g[2] for g in games) / len(games),
            "min": sum(g[1] for g in games) / len(games)} if games else None


def windows(log, last):
    """{'current', 'l30', 'l15', 'l7': list of games} for one log."""
    w = {"current": list(log)}
    for k, n in DAYS.items():
        lo = last - dt.timedelta(days=n)
        w[k] = [g for g in log if lo <= g[0] <= last]
    return w


def weighted_rate(r, use_adjusted=True):
    """The weighted rate for one pool row (after attach)."""
    base = (r.get("last") or r.get("projected") or {}).get("fpg")
    if not r.get("current"):
        return base or 0.0
    parts = [(WEIGHTS["base"], base)] if base is not None else []
    adj = (r.get("adj") or {}) if use_adjusted else {}
    for k in ("current", "l30", "l15", "l7"):
        s = adj[k] if k in adj else r.get(k)  # a window emptied by its dropped games is skipped
        if s and s.get("gp"):
            parts.append((WEIGHTS[k], s["fpg"]))
    return sum(w * x for w, x in parts) / sum(w for w, _ in parts)


def attach(rows, now=None):
    """Add 'log', 'drops', 'adj' and 'wrate' to each row (an iterable of pool rows). Returns mismatch notes."""
    rows = list(rows)
    logs, last = season_logs(now)
    notes = []
    FIXED.clear()
    for r in rows:
        r["adj"], r["drops"], r["log"] = {}, {}, None
        log = logs.get(r["id"], [])
        if r.get("current") and last:
            w = windows(log, last)
            ok = len(w["current"]) == r["current"]["gp"]
            if not ok:
                notes.append(f'{r["player"]}: {len(w["current"])} games in the box scores, '
                             f'{r["current"]["gp"]} in ESPN\'s season split')
            else:
                for k in DAYS:  # ESPN keeps a stale last game in a window the player has not played in
                    espn = r.get(k)
                    if len(w[k]) != (espn["gp"] if espn else 0):
                        r[k] = _avg(w[k])
                        FIXED.append(f'{r["player"]} {k}')
            if ok:
                r["log"] = log
                r["drops"] = outliers(log)
                for k, games in w.items():
                    out = [g for g in games if g[3] in r["drops"]]
                    if out:
                        espn, left = r[k], len(games) - len(out)
                        r["adj"][k] = ({"gp": left, "fpg": (espn["fpg"] * espn["gp"] - sum(g[2] for g in out)) / left}
                                       if left else None)
        r["wrate"] = weighted_rate(r)
        season = r["adj"]["current"] if "current" in r["adj"] else r.get("current")
        r["small"] = bool(r.get("current")) and (season or {}).get("gp", 0) <= SMALL_SAMPLE
    return notes


def adj_cell(r, k):
    """'23.3 (6)', or '23.3 (6) → 28.6 (5)' when an outlier is dropped from that window."""
    s, a = r.get(k), (r.get("adj") or {}).get(k)
    if not s:
        return "—"
    cell = f'{s["fpg"]:.1f} ({s["gp"]})'
    if k in (r.get("adj") or {}):
        cell += f' → {a["fpg"]:.1f} ({a["gp"]})' if a else " → —"
    return cell


def drops_note(r):
    """One line naming the dropped games, or ''."""
    if not r.get("drops"):
        return ""
    byid = {g[3]: g for g in r.get("log") or []}
    return "; ".join(f'{byid[gid][0]:%d %b} ({why})' for gid, why in r["drops"].items() if gid in byid)


def main():
    from injury_watch import player_pool
    from form import find
    if len(sys.argv) < 2:
        sys.exit(__doc__.split("Usage")[1])
    pool, _ = player_pool()
    for name in sys.argv[1:]:
        for r in find(pool, name):
            print(f'## {r["player"]}')
            for d, m, fp, _ in r.get("log") or []:
                print(f'- {d:%a %d %b}: {fp:.1f} FP in {m} min' + (" (dropped)" if _ in r["drops"] else ""))
            print("- Dropped: " + (drops_note(r) or "none"))
            for k, lab in (("current", "Season"), ("l30", "L30"), ("l15", "L15"), ("l7", "L7")):
                print(f"- {lab}: {adj_cell(r, k)}")
            base = (r.get("last") or r.get("projected") or {}).get("fpg")
            print(f'- Base (last season, else projection): {base:.1f}' if base is not None else "- Base: none")
            print(f'- Weighted rate: {r["wrate"]:.1f} (all games: {weighted_rate(r, False):.1f})'
                  + (" — small sample: the season part rests on 2 games or fewer" if r.get("small") else ""))


if __name__ == "__main__":
    main()
