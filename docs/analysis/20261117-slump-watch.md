# Slump Watch: 17 Nov 2026

- Generated 2026-11-17 21:18 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 112 rostered players in league 423671879, through scoring period 29. Teams have played **2 to 15 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 28 (Mon 16 Nov US) re-scored from ESPN's final NBA box scores: all 58 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**2 rostered players are 10+ FP/g under projection, on 1 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 70.4/60.5 · LaMelo Ball 35.1/46.4 · Josh Giddey 30.4/46.2 |
| Come-in Cider (us) | 0 | Cade Cunningham 51.2/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.2/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 60.8/57.6 · Donovan Mitchell 43.3/46.5 · Joel Embiid 36.0/45.4 |
| Lauri Birds | 0 | Nikola Jokic 65.3/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 47.4/56.8 · Cooper Flagg 49.2/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 48.7/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 50.2/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 42.4/50.0 · Jayson Tatum 47.1/48.1 · Kyrie Irving 41.5/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 67.1/60.6 · Domantas Sabonis 43.9/46.7 · Tyrese Maxey 46.8/45.1 |

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 13 | 28.2 / 35.5 | 0.83 | 30.4 (13) | 29.8 (4) | 33.9 (7) | 30.4 (13) | 46.2 | **−15.8** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 14 | 27.5 / 32.9 | 0.90 | 35.1 (14) | 35.3 (3) | 39.3 (7) | 35.1 (14) | 46.4 | **−11.4** | 41.1 | Active |

- **Josh Giddey** (both): scoring −9.4, reb −4.0, ast −2.3, stocks −3.2, TO +1.0; bonus +2.2.
  - Current: 28.2 min, 9.9 pts, 3.7-9.1 FG, 1.3-2.1 FT, 5.2 reb, 8.5 ast, 0.4 stl, 0.6 blk, 3.3 TO
  - Last 7 days (4 GP): 28.5 min, 9.0 pts, 3.2-8.5 FG, 0.8-1.8 FT, 6.0 reb, 8.5 ast, 0.0 stl, 1.2 blk, 4.5 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
- **LaMelo Ball** (minutes): scoring −5.8, reb −1.9, ast −5.0, stocks +1.2, TO −0.6; bonus +0.7.
  - Current: 27.5 min, 17.7 pts, 6.2-14.9 FG, 1.8-2.4 FT, 3.7 reb, 5.8 ast, 1.9 stl, 0.1 blk, 3.6 TO
  - Last 7 days (3 GP): 26.3 min, 15.7 pts, 5.7-17.3 FG, 0.3-1.0 FT, 5.3 reb, 5.0 ast, 2.7 stl, 0.0 blk, 2.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Near the line:** Desmond Bane −6.3 (#8, efficiency, L7 40.2).

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Rudy Gobert −6.5 (#8, minutes, L7 31.0), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.8 (#7, efficiency, L7 —).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Joel Embiid −9.4 (#3, efficiency, L7 34.3), Josh Hart −7.8 (#9, efficiency, L7 12.7), Derrick White −6.7 (#6, minutes, L7 28.2), AJ Dybantsa −6.3 (#10, efficiency, L7 24.2).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Ivica Zubac −8.8 (#7, minutes, L7 35.7), Darius Garland −8.5 (#5, efficiency, L7 35.3), Kevin Durant −7.0 (#4, efficiency, L7 33.8).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** Shai Gilgeous-Alexander −9.4 (#1, efficiency, L7 45.8), Brandon Miller −8.7 (#8, minutes, L7 11.0), Damian Lillard −8.5 (#6, efficiency, L7 29.2), Naz Reid −5.6 (#10, efficiency, L7 25.5), Norman Powell −5.5 (#9, minutes, L7 41.7), De'Aaron Fox −5.5 (#7, efficiency, L7 29.5).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −7.6 (#1, efficiency, L7 42.5), Tyler Herro −5.1 (#6, minutes, L7 24.0).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** James Harden −9.3 (#5, efficiency, L7 45.3), Trae Young −7.3 (#4, efficiency, L7 37.5), Alex Sarr −5.8 (#7, efficiency, L7 35.2).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball |
| efficiency | — |
| both | Josh Giddey |

- **Flagged and not active on ESPN:** none.
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 19 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** none.
- **Not flagged, but 10+ under projection over the last 7 days:** Josh Hart (Dr White Slong, L7 12.7 in 3 vs projected 33.0, L7 gap −20.3, season gap −7.8), Domantas Sabonis (Team Nic Kerr, L7 30.0 in 3 vs projected 46.7, L7 gap −16.7, season gap −2.8), Cooper Flagg (Matt Wright's Foxies, L7 29.3 in 3 vs projected 45.4, L7 gap −16.0, season gap 3.9), Tyler Herro (Snow Time Lakers, L7 24.0 in 3 vs projected 38.8, L7 gap −14.8, season gap −5.1), Ty Jerome (Melbourne poopoo, L7 32.0 in 2 vs projected 43.5, L7 gap −11.5, season gap −3.4), Shai Gilgeous-Alexander (Matt Wright's Foxies, L7 45.8 in 4 vs projected 56.8, L7 gap −11.1, season gap −9.4), Joel Embiid (Dr White Slong, L7 34.3 in 3 vs projected 45.4, L7 gap −11.0, season gap −9.4), Naz Reid (Matt Wright's Foxies, L7 25.5 in 2 vs projected 35.5, L7 gap −10.0, season gap −5.6).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 9 | 32.8 / 32.5 | 31.0 | — | 37.7 (3) | 31.0 (9) | 36.8 | 41.6 |
| Rudy Gobert | Come-in Cider (us) | 13 | 29.4 / 32.5 | 27.8 | 31.0 (3) | 31.3 (7) | 27.8 (13) | 34.3 | 38.2 |
| James Harden | Team Nic Kerr | 14 | 32.9 / 33.6 | 32.8 | 45.3 (3) | 34.2 (8) | 32.8 (14) | 42.1 | 45.1 |
| Jalen Johnson | Snow Time Lakers | 11 | 34.4 / 36.7 | 42.4 | 42.5 (2) | 41.0 (4) | 42.4 (11) | 50.0 | 53.1 |
| Joel Embiid | Dr White Slong | 12 | 31.5 / 31.6 | 36.0 | 34.3 (3) | 32.9 (7) | 36.0 (12) | 45.4 | 46.4 |

## Our pending trades

None.

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-17 21:18 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
