# Opponent factor audit: 08 Nov 2026

- Generated 2026-11-08 09:15 UTC by `council/opponents.py --audit`. The season is replayed one game day at a time (18 days). Each day's factors and player averages are rebuilt from earlier games only, then every player-game that day is predicted two ways: **plain** (his average, outlier games out) and **factor** (his average × the opponent factor at his positions).
- Counted: players with 3+ earlier games, facing a team with 5+ earlier games, who played 10+ minutes. Factor settings: shrink 5, cap ±15%.
- **Certified** needs 1000+ player-games, a gain in absolute error at least 2 standard errors above zero, and soft and tough matchups both moving the predicted way.

## Verdict: not certified: gain in absolute error +0.004 FP a game, t = 0.08 (needs 2); tough matchups did not score below average

- ✓ 1131 player-games (needs 1000)
- ✗ gain in absolute error +0.004 FP a game, t = 0.08 (needs 2)
- ✓ soft matchups scored above average
- ✗ tough matchups did not score below average

## Errors

| Prediction | Mean absolute error | Root mean square error |
|---|---:|---:|
| Plain average | 11.05 | 14.07 |
| Average × factor | 11.04 | 14.12 |

## Does the factor point the right way?

Actual is what players scored against their own averages in those games; predicted is what the factor said.

| Matchup | Player-games | Predicted | Actual |
|---|---:|---:|---:|
| tough (5%+ under) | 191 | −7.8% | +2.1% |
| slightly tough | 231 | −3.4% | −5.9% |
| even (within 2%) | 346 | −0.0% | +2.0% |
| slightly soft | 191 | +3.4% | −3.5% |
| soft (5%+ over) | 172 | +8.2% | +2.2% |

## Other shrink settings

More shrink pulls every factor harder toward even. The gain is in FP a game; positive means the factor beat the plain average.

| Shrink (games) | Mean absolute error | Gain | t |
|---:|---:|---:|---:|
| 0 | 11.094 | -0.048 | -0.72 |
| 3 | 11.055 | -0.009 | -0.19 |
| 5 (in use) | 11.042 | +0.004 | 0.08 |
| 8 | 11.031 | +0.015 | 0.42 |
| 12 | 11.025 | +0.021 | 0.77 |
| 20 | 11.021 | +0.025 | 1.28 |

The plain average's mean absolute error is 11.046 at every setting.

## Sources

- ESPN box scores (cached in `council/.cache/box`) and league 423671879 (`kona_player_info`, `proTeamSchedules_wl`), read 2026-11-08 09:15 UTC.
