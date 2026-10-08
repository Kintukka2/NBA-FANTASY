# Data dictionary

## Provenance

The player pool came from ESPN's private league endpoint, read through
an authenticated browser session:

```
BASE = https://lm-api-reads.fantasy.espn.com/apis/v3/games/fba
       /seasons/2027/segments/0/leagues/423671879
views  kona_player_info          player pool + stats
       mSettings&view=mTeam      league config + teams
splits 002026                    2026 actuals
       102027                    2027 projections
```

That JSON **cannot be refetched from a shell** — it needs session
cookies. The workbook `data/raw/ESPN_Fantasy_Player_Database_2026-27.xlsx`
is therefore the upstream-most artefact available in this repo, and it
is committed for exactly that reason. `scripts/export_raw.py` transcribes
its tabs to CSV with no cleaning, so `data/raw/*.csv` can always be
regenerated from the workbook and checked against the committed copies.

Extraction date: 7 October 2026. 1,095 players; 558 carry a 2026 sample;
348 carry a 2027 projection.

## Pipeline

```
data/raw/ESPN_...xlsx  --export_raw.py-->  data/raw/*.csv
data/raw/master.csv    --recompute.py-->   data/processed/players_scored.csv
                                           data/processed/verification.csv
```

Both scripts are deterministic: floats rounded to 4 dp, stable sort
keys, LF endings. Regenerate and `git diff` to audit. Non-empty diff
means something upstream moved.

## Naming

`A_` = 2026 **actual**. `P_` = 2027 ESPN **projection**. `FP_` = computed
by this repo. Counting stats are **per game**; `A_DD`, `A_TD`, `A_FPTS`,
`P_FPTS` and `FP_*_TOT` are **season totals**. Percentages are fractions
(0.482, not 48.2).

## Identity and market columns

| Column | Meaning |
|---|---|
| `PlayerID` | ESPN player ID. Stable join key; prefer it over `Player`. |
| `Player` `Team` `Pos` | Name, team abbreviation, ESPN's primary position. |
| `Injury` | `ACTIVE`, `DAY_TO_DAY`, `OUT`. Live as of 7 Oct 2026. |
| `%Own` | Share of ESPN leagues rostering him. Market consensus. |
| `ADP` | **Standard-scoring** average draft position. A read on *where a player will go*, not on what he is worth here. The gap between ADP and `FP_ACT_PG` is the entire opportunity. |

## Box-score columns

`GP MIN PTS FGM FGA FG% FTM FTA FT% 3PM 3PA 3P% OREB DREB REB AST STL
BLK TO PF DD TD FPTS FPTS_AVG`, each prefixed `A_` or `P_`.

**ESPN projects no `OREB`, `DREB`, `PF`, `DD` or `TD`.** The projection
set is 26 columns against the actuals' 31. So `P_FPTS_AVG` omits the
OREB double-count *and* both bonuses, and structurally understates
rebounding bigs by roughly 2-5 pts/game. This is a hole in the source,
not in the scoring. It is measured, not patched — see
`PROJ_BLIND_SPOT_PG`.

## Computed columns

| Column | Definition |
|---|---|
| `FP_ACT_PG_CORE` | Per-game formula on 2026 actuals, bonuses excluded. |
| `FP_ACT_BONUS_PG` | `(3·A_DD + 6·A_TD) / A_GP`. The amortised bonus. |
| `FP_ACT_PG` | `CORE + BONUS_PG`. **The headline number.** Reproduces `A_FPTS_AVG`. |
| `FP_ACT_PG_ESPN` | ESPN's own `A_FPTS_AVG`, carried for comparison. |
| `FP_ACT_PG_DELTA` | Ours minus ESPN's. Should be within ±0.07 — see tolerance below. |
| `FP_ACT_TOT` | `CORE·GP + 3·DD + 6·TD`. Season total. |
| `FP_ACT_PER36` | `FP_ACT_PG / A_MIN · 36`. **Meaningless on a thin sample** — always read `A_GP` first. |
| `FP_PROJ_PG_CORE` | Per-game formula on projections. `_CORE` because the OREB term is forced to 0 and there are no bonuses: ESPN does not project those inputs. |
| `FP_PROJ_PG_ESPN` | ESPN's `P_FPTS_AVG`. |
| `FP_PROJ_PG_DELTA` | Ours minus ESPN's. |
| `FP_PROJ_TOT_CORE` | `FP_PROJ_PG_CORE · P_GP`. |
| `FP_PROJ_PER36` | Projected per-36. |
| `OREB_SHARE_ACT` | `A_OREB / A_REB`. Who rebounds on the offensive glass, where boards score double. |
| `DD_PER_GP_ACT` | `A_DD / A_GP`. |
| `TD_PER_GP_ACT` | `A_TD / A_GP`. |
| `PROJ_BLIND_SPOT_PG` | `A_OREB + FP_ACT_BONUS_PG`. The points per game that `FP_PROJ_PG_CORE` structurally cannot see, sized from the player's **own observed 2026 line**. Arithmetic on measured data, not a forecast. Add it to a projection only if you accept last year's OREB and DD rates carry forward — that judgement is yours, not the pipeline's. |
| `SAMPLE_FLAG` | `NO_SAMPLE` if `A_GP = 0`; `THIN` if `A_GP ≤ 20`; blank otherwise. Threshold is arbitrary and documented here so you can change it. |

## Verification

`recompute.py` rebuilds every fantasy figure from raw box-score columns
and cross-checks it against ESPN's. Current state, all 558 players with
a sample:

```
mean delta  +0.0002 pts/game
max |delta|  0.0645 pts/game
outliers          0
```

The tolerance is **0.15 pts/game**, and the residual is pure source
precision: per-game averages are stored to 2 dp, so each of ~12 inputs
carries ±0.005, which weighted by the scoring values sums to a worst
case of `(1+2+1+1+1+1+1+1+2+4+4+2)·0.005 = 0.105`. The script exits
non-zero if any row breaches tolerance, so a silent formula regression
cannot ship.

## Known traps

1. **`ADP` is standard-scoring.** It is market data, never valuation.
2. **`A_GP` before anything else.** Six names that look like buys rest
   on ≤20 games: Edey 11, Lively 7, Jerome 15, Trae Young 15, Looney 21,
   Sabonis 19. A per-36 extrapolation from seven games is not evidence.
3. **`P_FPTS_AVG` understates bigs** and is also *stale on injuries in
   at least one case*: ESPN encodes absences into `P_GP` for Butler
   (39), Mark Williams (24), Sharpe (27) and Moody (12) — but projects
   Brandon Ingram for 67 games while listing him `OUT`.
4. **Projections are the secondary input by standing instruction.** 2026
   actuals lead; `P_*` columns inform, they do not decide.
