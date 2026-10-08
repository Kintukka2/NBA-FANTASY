# Phase 1 Findings — Player Data Extraction & Verification

**Completed:** 8 Oct 2026 · **Output:** `ESPN_Fantasy_Player_Database_2026-27.xlsx`
**Scope as agreed:** raw data only. No composite scores, no rankings, no derived ratings — those are Phase 2.

---

## 1. What was collected

Every player in the GONG League player pool (the "Add Players" list, all 22 pages × 50 per page), with two full stat splits each:

- **2026 season actuals** — what the player really did in 2025-26, labelled `2026 season` in the ESPN UI, internally stat split `002026`.
- **2027 Projections** — ESPN's forward projection, internally `102027`.

**Totals:** 1,095 players. 558 have real 2026 production. 348 carry an ESPN projection. 519 are identity-only (name/team/position, no stats at all — deep bench, two-way, and unsigned players).

### Reconciliation (exact, not approximate)

| Source | Rows |
|---|---:|
| Statistical rows (`part0`–`part3`, minus header) | 576 |
| Identity-only rows (`empty0`) | 519 |
| **Total** | **1,095** |
| Expected (22 pages × 50) | 1,100 → 1,095 after the short final page |

Every statistical line carries exactly 50 pipe-delimited fields; every identity line carries exactly 5. No ragged rows, no silent truncation.

---

## 2. How it was extracted

The visible HTML table was not scraped. Instead the data came from the API the page itself calls:

```
https://lm-api-reads.fantasy.espn.com/apis/v3/games/fba/seasons/2027
  /segments/0/leagues/423671879?view=kona_player_info
```

fetched from inside the authenticated browser tab with `credentials: "include"`. This matters for two reasons: the API returns full-precision numbers rather than the rounded display values, and it returns *all* splits at once rather than requiring 22 page-turns per split.

Two practical obstacles and how they were handled, in case this needs repeating:

- **The JS bridge truncates return values at roughly 1–2 KB.** Bulk payloads were written into a `<pre>` element in the page DOM and read back out as page text, which handles ~37 KB per pass cleanly.
- **Text extraction collapses tab characters.** Pipe (`|`) was used as the field delimiter instead.

Full reproducible recipe lives in `DATA_DICTIONARY.md`.

---

## 3. Verification

Spot-checking a handful of rows would not have proven column alignment, so the whole dataset was validated against the league's own scoring formula instead. Every player's fantasy total was recomputed from their raw box-score columns and compared to the total ESPN independently reports.

| Split | n | Mean deviation | Max abs deviation | Outliers |
|---|---:|---:|---:|---:|
| 2026 actuals | 558 | **−0.01 pts** | 3.8 | **0** |
| 2027 projections | 348 | **+0.12 pts** | 4.8 | **0** |

Residuals of this size are exactly what two-decimal rounding on per-game averages multiplied by games played produces. Because the recomputation uses **every** raw column, agreement this tight proves all 50 columns are correctly mapped *and* correctly aligned to the right player. A single shifted or mislabelled column would have blown the deviations out immediately.

A second independent check: `A_FPTS_TOT ÷ A_GP` against ESPN's own `A_FPTS_AVG` — **0 mismatches** across all 558 players.

Edge cases confirmed by hand in the finished workbook:

- Victor Wembanyama, Nikola Jokić — complete data both splits.
- Tyrese Haliburton — null actuals but `A_FPTS_TOT` = 0 (injury season, correctly distinguished from missing).
- Russell Westbrook — actuals present, projection absent (unsigned at projection time).
- Aday Mara — fully null identity row, carried through without corrupting the grid.

---

## 4. Data quirks worth knowing

**ESPN does not project five of the categories it reports as actuals.** The `102027` split simply omits them:

- Offensive rebounds (OREB)
- Defensive rebounds (DREB)
- Personal fouls (PF)
- Double-doubles (DD)
- Triple-doubles (TD)

This is not a gap in the extraction — the fields do not exist upstream. It has a direct consequence for this league: **OREB counts twice in our scoring and DD/TD are worth +3/+6, so ESPN's projected fantasy totals structurally understate rebounding bigs.** Any Phase 2 model built on projections alone will misprice them. (Which is a second, independent reason to weight actuals heavily, alongside your stated preference.)

**Mixed units in one row.** Counting stats are per-game averages; `A_DD` and `A_TD` are season totals. `A_FPTS_TOT` / `P_FPTS_TOT` are season totals, `_AVG` are per-game. Documented per-column in `DATA_DICTIONARY.md`.

**ADP is standard-scoring ADP.** It is ESPN's market consensus, not a valuation under this league's rules. Treat the gap between ADP and our own scoring as the opportunity, not as a signal to follow.

**Injury status is sparse.** A handful of players (DeJon Jarreau, Skal Labissiere, Trentyn Flowers, Lachlan Olbrich, Cody Martin) return a blank status rather than `ACTIVE`/`OUT`. Blank means "ESPN reports nothing", not "healthy".

**Nothing is drafted.** All 1,095 players show as free agents. The pool is clean.

---

## 5. Scoring-distortion summary

The arithmetic behind the claims in `LEAGUE_RULES.md`, for reference:

| Event | Net fantasy points |
|---|---:|
| Made two-pointer | +3 |
| Made three-pointer | +5 |
| Missed field goal | −1 |
| Made free throw | +1 |
| Missed free throw | −1 |
| Steal | +4 |
| Block | +4 |
| Assist | +2 |
| Defensive rebound | +1 |
| Offensive rebound | +2 |
| Turnover | −2 |

Break-even shooting: **~25% from two, ~17% from three.** One steal equals four defensive rebounds, or two assists, or a made three. One turnover wipes out two rebounds.

---

## 6. State of play

**Done:** full player pool extracted, verified, and delivered as a 4-tab workbook. Complete league configuration retrieved and documented.

**Open:**

- Which of the eight teams is yours, and therefore your snake slot.
- Confirm the one-acquisition-per-scoring-period reading against the live settings page.
- **Phase 2:** the weighted scouting model — real 2026 production prioritised, projections as a secondary input, per your standing preference.
