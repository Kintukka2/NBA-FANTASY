# Recent form: 14 Nov 2026

- Generated 2026-11-14 01:03 UTC by `council/form.py`. This is **data, not a verdict**.
- **Checks:** **games were live** (--allow-live): NY @ IND (4:27 - 2nd); MIL @ ORL (23.9 - 2nd). All 1100 pool players' current, L7, L15, L30, projected and 2026 averages re-score with `scripts/league_scoring.py` (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **L7 − season** is the last 7 days' FP/g minus the season's. ESPN's projection leaves out OREB, DREB, DD and TD, so it reads low for players who earn them.
- **Rate** is the weighted, outlier-adjusted rate the matchup plans use (`council/gamelog.py`): last season ×1 (or the projection), season ×2, L30 ×3, L15 ×4, L7 ×5.
- **Game logs:** 42 pool players' box-score logs do not match ESPN's season splits; they keep ESPN's averages and no outliers.

| Player | NBA | League | Season FP/g (GP) | L7 | L15 | L30 | L7 − season | Min: season / L7 | Projected | 2026 | Rate | ESPN status |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---|
| **Cade Cunningham** | DET | Come-in Cider (us) | 50.7 (11) | 55.7 (3) | 54.8 (6) | 50.7 (11) | +4.9 | 34.6 / 37.7 | 50.4 | 53.3 | **53.6** | active |
| **Jamal Murray** | DEN | Come-in Cider (us) | 49.9 (10) → 54.7 (9) | 55.7 (3) | 54.0 (6) | 49.9 (10) → 54.7 (9) | +5.8 | 36.3 / 35.0 | 43.9 | 47.8 | **54.4** | active |
| **Scottie Barnes** | TOR | Come-in Cider (us) | 45.9 (8) → 50.7 (7) | — | 48.8 (4) | 45.9 (8) → 50.7 (7) | — | 33.4 / — | 43.7 | 47.3 | **49.6** | out, ESPN est. 15 Nov |
| **Paul George** | BOS | Come-in Cider (us) | 42.7 (10) | 39.7 (3) | 43.5 (6) | 42.7 (10) | −3.0 | 30.1 / 26.7 | 38.5 | 36.0 | **41.5** | day-to-day, ESPN est. 15 Nov |
| **Yaxel Lendeborg** | GS | Come-in Cider (us) | 41.4 (12) → 45.4 (11) | 44.0 (3) | 39.7 (7) → 46.7 (6) | 41.4 (12) → 45.4 (11) | +2.6 | 32.1 / 33.3 | 33.7 | — | **44.5** | active |
| **Kawhi Leonard** | TOR | Come-in Cider (us) | 40.0 (2) | — | — | 40.0 (2) | — | 26.0 / — | 45.8 | 50.0 | **41.7** (small sample) | out, ESPN est. 23 Nov |
| **Anthony Black** | ORL | Come-in Cider (us) | 38.0 (9) | 43.0 (4) | 41.0 (7) | 38.0 (9) | +5.0 | 29.8 / 31.2 | 28.2 | 30.7 | **40.0** | active |
| **Jalen Duren** | DET | Come-in Cider (us) | 33.5 (2) → 44.0 (1) | — | — | 33.5 (2) → 44.0 (1) | — | 19.0 / — | 42.2 | 44.3 | **44.1** (small sample) | out, ESPN est. 24 Nov |
| **Jalen Smith** | CHI | Come-in Cider (us) | 33.2 (10) → 35.8 (9) | 48.5 (2) | 32.4 (5) → 38.0 (4) | 33.2 (10) → 35.8 (9) | +15.3 | 23.9 / 30.0 | 22.4 | 25.5 | **39.9** | active |
| **Isaiah Hartenstein** | OKC | Come-in Cider (us) | 31.5 (12) | 35.0 (4) | 32.9 (7) | 31.5 (12) | +3.5 | 25.0 / 25.5 | 30.5 | 34.0 | **33.2** | active |
| **Trey Murphy III** | NO | Come-in Cider (us) | 31.0 (9) | 38.5 (2) | 36.0 (5) | 31.0 (9) | +7.5 | 32.8 / 32.0 | 36.8 | 41.6 | **35.5** | out, ESPN est. 14 Nov |
| **Daniss Jenkins** | DET | Come-in Cider (us) | 29.3 (11) | 52.0 (3) | 31.5 (6) | 29.3 (11) | +22.7 | 27.4 / 36.7 | — | 20.6 | **36.9** | active |
| **Daniel Gafford** | DAL | Come-in Cider (us) | 29.1 (12) | 24.0 (4) | 27.0 (7) | 29.1 (12) | −5.1 | 21.6 / 18.2 | 29.3 | 28.2 | **26.8** | active |
| **Saddiq Bey** | NO | Come-in Cider (us) | 26.9 (12) | 23.2 (4) | 29.0 (8) | 26.9 (12) | −3.7 | 26.8 / 27.5 | 25.9 | 32.6 | **26.6** | active |
| **Jalen Johnson** | ATL | Snow Time Lakers | 42.3 (9) | 39.5 (2) | 33.8 (4) | 42.3 (9) | −2.8 | 33.7 / 37.0 | 50.0 | 53.1 | **39.8** | active |
| **Devin Booker** | PHX | Snow Time Lakers | 41.5 (11) | 44.0 (4) | 41.6 (8) | 41.5 (11) | +2.5 | 33.9 / 33.0 | 43.2 | 40.2 | **42.3** | active |
| **Donovan Clingan** | POR | Snow Time Lakers | 37.6 (11) | 33.5 (4) | 40.5 (8) | 37.6 (11) | −4.1 | 25.4 / 26.5 | 33.9 | 41.1 | **37.2** | active |

## Outlier games dropped

- **Jamal Murray:** 22 Oct (bad game: 7.0 FP against a next-worst 31.0).
- **Scottie Barnes:** 25 Oct (bad game: 12.0 FP against a next-worst 34.0).
- **Yaxel Lendeborg:** 30 Oct (bad game: -2.0 FP against a next-worst 23.0).
- **Jalen Duren:** 23 Oct (short game: 10 min against a next-lowest 28).
- **Jalen Smith:** 04 Nov (short game: 7 min against a next-lowest 19).

## Sources

- ESPN fantasy API, league 423671879 (`kona_player_info` with ESPN's season, last-7, last-15 and last-30-day splits, `mTeam`, `proTeamSchedules_wl`) and ESPN's NBA injury feed, read 2026-11-14 01:03 UTC.
