# Slump Watch: 20 Nov 2026

- Generated 2026-11-20 03:47 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 31. Teams have played **2 to 16 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 31 (Thu 19 Nov US) re-scored from ESPN's final NBA box scores: all 24 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**3 rostered players are 10+ FP/g under projection, on 2 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 69.1/60.5 · LaMelo Ball 34.2/46.4 · Josh Giddey 32.4/46.2 |
| Come-in Cider (us) | 1 | Cade Cunningham 50.7/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.3/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 43.5/46.5 · Joel Embiid 37.5/45.4 |
| Lauri Birds | 0 | Nikola Jokic 64.5/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 47.5/56.8 · Cooper Flagg 51.0/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 49.3/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 51.1/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 43.4/50.0 · Jayson Tatum 45.9/48.1 · Kyrie Irving 41.8/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 63.4/60.6 · Domantas Sabonis 43.6/46.7 · Tyrese Maxey 46.8/45.1 |

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 14 | 28.1 / 35.5 | 0.88 | 32.4 (14) | 41.5 (4) | 36.1 (7) | 32.4 (14) | 46.2 | **−13.8** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 16 | 28.2 / 32.9 | 0.86 | 34.2 (16) | 32.6 (5) | 34.9 (8) | 34.2 (16) | 46.4 | **−12.2** | 41.1 | Active |

- **Josh Giddey** (minutes): scoring −8.4, reb −3.3, ast −2.2, stocks −3.2, TO +0.9; bonus +2.5.
  - Current: 28.1 min, 10.5 pts, 4.0-9.3 FG, 1.3-2.0 FT, 5.9 reb, 8.5 ast, 0.4 stl, 0.6 blk, 3.4 TO
  - Last 7 days (4 GP): 29.2 min, 11.2 pts, 4.2-9.2 FG, 1.0-2.0 FT, 9.0 reb, 9.0 ast, 0.2 stl, 1.2 blk, 3.8 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
- **LaMelo Ball** (minutes): scoring −6.4, reb −1.3, ast −5.2, stocks +0.5, TO −0.4; bonus +0.7.
  - Current: 28.2 min, 17.6 pts, 6.2-15.4 FG, 1.6-2.1 FT, 4.3 reb, 5.7 ast, 1.8 stl, 0.1 blk, 3.5 TO
  - Last 7 days (5 GP): 29.0 min, 16.0 pts, 6.0-18.0 FG, 0.4-0.8 FT, 6.6 reb, 5.0 ast, 1.8 stl, 0.0 blk, 2.4 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Near the line:** Desmond Bane −6.5 (#8, efficiency, L7 43.0).

### Come-in Cider (us): 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Kel'el Ware | MIL | #8 | 16 | 18.6 / 26.6 | 0.97 | 22.9 (16) | 26.8 (4) | 19.3 (9) | 22.9 (16) | 33.8 | **−10.8** | 32.5 | Active |

- **Kel'el Ware** (minutes): scoring −6.5, reb −4.2, ast −0.2, stocks −2.1, TO −1.0; bonus +3.1.
  - Current: 18.6 min, 8.9 pts, 3.3-7.8 FG, 1.5-1.9 FT, 6.4 reb, 0.8 ast, 0.6 stl, 1.1 blk, 1.5 TO
  - Last 7 days (4 GP): 21.2 min, 10.0 pts, 3.8-7.0 FG, 1.0-1.5 FT, 6.2 reb, 1.0 ast, 1.0 stl, 1.0 blk, 1.5 TO
  - Projected: 26.6 min, 13.0 pts, 5.3-9.9 FG, 1.1-1.5 FT, 10.6 reb, 0.9 ast, 0.9 stl, 1.3 blk, 1.0 TO
- **Near the line:** Rudy Gobert −8.9 (#7, both, L7 22.4), Jalen Duren −8.7 (#5, minutes, L7 —), Kawhi Leonard −5.8 (#2, minutes, L7 —).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −8.8 (#9, efficiency, L7 15.2), Joel Embiid −7.8 (#3, efficiency, L7 47.7), Derrick White −6.6 (#6, minutes, L7 27.3).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Ivica Zubac −9.7 (#7, minutes, L7 25.0), Kevin Durant −7.2 (#4, efficiency, L7 34.8), Darius Garland −6.9 (#5, efficiency, L7 42.5).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** Shai Gilgeous-Alexander −9.3 (#1, efficiency, L7 53.0), De'Aaron Fox −8.0 (#7, efficiency, L7 12.7), Brandon Miller −7.9 (#8, minutes, L7 24.5), Damian Lillard −7.7 (#6, efficiency, L7 30.2), Norman Powell −5.1 (#9, minutes, L7 40.0).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.6 (#1, efficiency, L7 46.7), Tyler Herro −6.4 (#6, minutes, L7 19.5).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** James Harden −8.9 (#5, efficiency, L7 40.3), Trae Young −8.3 (#4, efficiency, L7 34.5), Alex Sarr −5.4 (#7, efficiency, L7 42.2).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | Josh Giddey, LaMelo Ball, Kel'el Ware |
| efficiency | — |
| both | — |

- **Flagged and not active on ESPN:** none.
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 21 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** Kel'el Ware (Come-in Cider (us), L7 26.8 in 4 vs projected 33.8, season gap −10.8), Josh Giddey (Cream Abdul-Yammar, L7 41.5 in 4 vs projected 46.2, season gap −13.8).
- **Not flagged, but 10+ under projection over the last 7 days:** Rudy Gobert (Come-in Cider (us), L7 22.4 in 5 vs projected 34.3, L7 gap −11.9, season gap −8.9), De'Aaron Fox (Matt Wright's Foxies, L7 12.7 in 3 vs projected 38.2, L7 gap −25.5, season gap −8.0), Tyler Herro (Snow Time Lakers, L7 19.5 in 4 vs projected 38.8, L7 gap −19.3, season gap −6.4), Josh Hart (Dr White Slong, L7 15.2 in 4 vs projected 33.0, L7 gap −17.8, season gap −8.8), Michael Porter Jr. (Team Nic Kerr, L7 26.0 in 2 vs projected 38.9, L7 gap −12.9, season gap −4.3), Brandon Miller (Matt Wright's Foxies, L7 24.5 in 2 vs projected 37.4, L7 gap −12.9, season gap −7.9), Luka Doncic (Team Nic Kerr, L7 49.3 in 3 vs projected 60.6, L7 gap −11.3, season gap 2.8), Ivica Zubac (Lauri Birds, L7 25.0 in 3 vs projected 35.5, L7 gap −10.5, season gap −9.7), Brandin Podziemski (Matt Wright's Foxies, L7 20.5 in 4 vs projected 30.8, L7 gap −10.3, season gap 2.2).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Rudy Gobert | Come-in Cider (us) | 15 | 29.3 / 32.5 | 25.4 | 22.4 (5) | 26.6 (8) | 25.4 (15) | 34.3 | 38.2 |
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| James Harden | Team Nic Kerr | 15 | 33.1 / 33.6 | 33.1 | 40.3 (3) | 34.8 (8) | 33.1 (15) | 42.1 | 45.1 |
| Ivica Zubac | Lauri Birds | 10 | 23.4 / 31.1 | 25.8 | 25.0 (3) | 26.0 (7) | 25.8 (10) → 28.0 (9) | 35.5 | 36.3 |
| Nikola Jokic | Lauri Birds | 13 | 36.7 / 35.6 | 64.5 | 61.0 (3) | 67.3 (7) | 64.5 (13) → 67.8 (12) | 67.2 | 74.9 |

## Our pending trades

With **Melbourne poopoo**, proposed by us, expires 22 Nov 03:13 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Stephon Castle | we receive | 16 | 29.5 / 32.7 | 34.8 | 48.0 (4) | 36.7 (9) | 34.8 (16) | 36.9 | −2.0 | Active |
| Anthony Black | we send | 11 | 32.7 / 28.9 | 38.3 | 29.7 (3) | 39.4 (7) | 38.3 (11) | 28.2 | +10.1 | Active |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-20 03:47 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
