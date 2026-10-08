# Scoring — GONG league 423671879, 2026-27

Canonical implementation: `scripts/league_scoring.py`. Import it. Do not
re-derive the formula from prose, including from this file.

## Configured values

| Event | Pts | Event | Pts | Event | Pts |
|---|---:|---|---:|---|---:|
| PTS | +1 | 3PM | +1 | STL | +4 |
| FGM | +2 | REB | +1 | BLK | +4 |
| FGA | **−1** | OREB | **+1 extra** | TO | **−2** |
| FTM | +1 | AST | +2 | PF | 0 |
| FTA | **−1** | DD | +3 | TD | +6 |
| | | | | QD | +40 |

OREB is additive on top of REB: the league scores total rebounds at +1
and then offensive rebounds again at +1. An offensive board is worth 2,
a defensive board 1. QD is configured and never occurs.

## Formula

```
per_game = PTS + 2·FGM − FGA + FTM − FTA + 3PM + REB + OREB
           + 2·AST + 4·STL + 4·BLK − 2·TO

season_total = per_game · GP + 3·DD + 6·TD + 40·QD
```

**ESPN amortises the bonuses into the per-game average.** `A_FPTS_AVG`
is exactly `A_FPTS / A_GP`, and `A_FPTS` already contains the DD/TD
bonuses. So to reproduce ESPN's per-game figure you need

```
espn_per_game = per_game + (3·DD + 6·TD) / GP
```

This is not cosmetic. Jokić carried 55 double-doubles and 34
triple-doubles in 65 games, worth `(3·55 + 6·34)/65 = 5.68` pts/game —
the difference between 69.3 and his actual 74.97. The bare formula
understates every high-rebound playmaker in the pool. `recompute.py`
emits both: `FP_ACT_PG_CORE` without bonuses, `FP_ACT_PG` with them.

## Net value of one event

Derived from the table above, after the attempt penalty.

| Event | Net | Event | Net |
|---|---:|---|---:|
| Made three | **+5** | Steal | **+4** |
| Made two | +3 | Block | **+4** |
| Missed FG | −1 | Assist | +2 |
| Made FT | +1 | Offensive rebound | +2 |
| Missed FT | −1 | Defensive rebound | +1 |
| | | Turnover | −2 |

Three consequences, and they are the whole reason this league does not
play like a standard one:

1. **A steal or a block is worth four defensive rebounds, two assists,
   or a made three.** ESPN's ADP is built for standard scoring, so
   defensive producers are the systematically mispriced asset.
2. **Shooting break-even is low.** A made two nets +3 and a miss −1, so
   two-point attempts pay above **25%** and threes above **16.7%**.
   Volume still pays — but a 3PA is worth ~45% more per attempt than a
   2PA, and high-usage inefficient scorers give back far more here than
   in a normal league.
3. **Turnovers cost double a missed shot.** −2 against −1.

## Roster and draft constraints

Ten starters: PG, SG, SF, PF, C, G, F, UTIL×3. Three bench, one IR.
Maximum four players at the G grouping. Lineups change **daily** and are
unlimited. Acquisitions rescale weekly with the NBA game-day count —
roughly 7 in a normal week, about 4 in a compressed one.

So the binding constraint is **bench spots, not adds**. Picks 1-10 are
the team and deserve the thinking; picks 11-13 are rotating slots where
pure upside is the right bet, because anything that misses is cheap to
replace and there is nowhere to park a prospect anyway.

Snake draft, 13 rounds, 90s per pick, no keepers, 8 teams — **104
players come off the board in total**. Anything past roughly ADP 140 is
in-season waiver material, to be decided later with information nobody
has yet.
