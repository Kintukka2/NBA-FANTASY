# Slump Watch: 02 Nov 2026

- Generated 2026-11-02 23:01 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 14. Teams have played **2 to 7 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 13 (Sun 01 Nov US) re-scored from ESPN's final NBA box scores: all 26 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L15 and L30 cover every game so far for every player listed, so they equal the season average for now.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**8 rostered players are 10+ FP/g under projection, on 4 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Lauri Birds | 3 | Nikola Jokic 59.8/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 47.8/43.0 |
| Cream Abdul-Yammar | 2 | Victor Wembanyama 67.0/60.5 · LaMelo Ball 30.9/46.4 · Josh Giddey 26.3/46.2 |
| Matt Wright's Foxies | 2 | Shai Gilgeous-Alexander 43.5/56.8 · Cooper Flagg 58.4/45.4 · Evan Mobley 44.8/43.3 |
| Team Nic Kerr | 1 | Luka Doncic 65.5/60.6 · Domantas Sabonis 54.7/46.7 · Tyrese Maxey 49.0/45.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 42.8/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 47.6/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.0/57.6 · Donovan Mitchell 40.3/46.5 · Deni Avdija 42.0/40.4 |
| Melbourne poopoo | 0 | Anthony Davis 41.7/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 48.0/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 43.1/50.0 · Jayson Tatum 47.5/48.1 · Joel Embiid 40.4/45.4 |

## Since the last Slump Watch

Against `docs/analysis/20261102-slump-watch.md` (06:54 UTC this morning). No NBA game was played in between.

- **Joined:** none. **Left:** none. **Moved 3+ FP/g:** none.
- **The L7 window moved forward a day,** so games on 25 and 26 Oct dropped out of it. Anthony Black (ours) is now L7 33.7 (3), against 36.2 (4), and Cade Cunningham is 40.7 (3), against 44.8 (4). Their season averages did not change.
- **ESPN status changes:**
  - Anthony Black (ours): now **Out** (rest), *ESPN est.* 5 Nov.
  - Ivica Zubac: *ESPN est.* moved from 2 Nov to 9 Nov.
  - LaMelo Ball: now day-to-day.
- **Small stat corrections:** LaMelo Ball 30.7 → 30.9, Anthony Davis 41.5 → 41.7, Jayson Tatum 47.8 → 47.5.
- **Pending trades** (ESPN `mTransactions2`):
  - **Snow Time Lakers declined all three of our offers** (Jaylen Brown, Devin Booker, Dyson Daniels) at 19:44 UTC on 2 Nov.
  - **Lauri Birds withdrew Edey for Hartenstein** at 18:48 UTC, then dropped Edey, who is now a free agent.
  - **Four Black offers remain:** Jabari Smith Jr. and James Harden (Team Nic Kerr), Jalen Brunson (Melbourne poopoo) and Amen Thompson (Matt Wright's Foxies). The council's verdict to keep Thompson only stands (`council/sessions/20261102-070000-black-offers.json`).

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Lauri Birds: 3

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Lauri Markkanen | UTAH | #7 | 5 | 28.6 / 34.0 | 0.79 | 25.6 | 13.0 (2) | 25.6 (5) | 25.6 (5) | 38.7 | **−13.1** | 44.4 | Active |
| Darius Garland | LAC | #5 | 6 | 32.5 / 35.2 | 0.77 | 28.7 | 24.7 (3) | 28.7 (6) | 28.7 (6) | 40.4 | **−11.7** | 35.3 | Active |
| Ivica Zubac | IND | #8 | 3 | 21.7 / 31.1 | 1.03 | 25.3 | — | 25.3 (3) | 25.3 (3) | 35.5 | **−10.1** | 36.3 | **Out**, ESPN est. back 09 Nov |

- **Lauri Markkanen** (both): scoring −11.5, reb −1.6, ast −0.6, stocks −0.8, TO +0.2; bonus +1.2.
  - Current: 28.6 min, 15.4 pts, 4.4-12.4 FG, 4.2-4.8 FT, 5.6 reb, 1.6 ast, 0.6 stl, 0.6 blk, 1.4 TO
  - Last 7 days (2 GP): 17.5 min, 7.5 pts, 1.5-8.0 FG, 3.5-4.0 FT, 3.0 reb, 0.5 ast, 1.0 stl, 1.0 blk, 1.0 TO
  - Projected: 34.0 min, 23.8 pts, 8.0-17.3 FG, 4.7-5.3 FT, 7.2 reb, 1.9 ast, 0.9 stl, 0.5 blk, 1.5 TO
  - **2 Nov:** he returned on 31 Oct from the right wrist sprain: 13 points on 3-of-14 in 29 minutes before fouling out [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/lauri-markkanen-wrist-returns-to-lineup-saturday). The 6-minute injury exit on 26 Oct is still in his average. **Status:** active.
  - **Update 2 Nov:** not on Utah's report for Monday at San Antonio; the wrist is "no longer a concern" [Sports Mole, 2 Nov](https://www.sportsmole.co.uk/basketball/utah-jazz/preview/utah-jazz-vs-san-antonio-spurs-player-props-injury-report-and-prediction--nba_608201.html). The gameday preview has him "struggling from three-point range" [Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/spurs-vs-jazz-gameday-betting-153428767.html). His L7 is 13.0 (2), noise.
- **Darius Garland** (efficiency): scoring −1.9, reb −1.7, ast −2.1, stocks −2.7, TO −4.1; bonus +0.8.
  - Current: 32.5 min, 20.8 pts, 7.5-16.8 FG, 3.3-4.0 FT, 1.3 reb, 6.3 ast, 0.8 stl, 0.0 blk, 5.2 TO
  - Last 7 days (3 GP): 30.0 min, 17.7 pts, 6.0-15.3 FG, 3.7-3.7 FT, 1.0 reb, 5.7 ast, 1.0 stl, 0.0 blk, 4.3 TO
  - Projected: 35.2 min, 21.6 pts, 7.8-17.0 FG, 3.0-3.5 FT, 3.0 reb, 7.4 ast, 1.3 stl, 0.2 blk, 3.1 TO
  - **What explains it:** turnovers, with 5 or more in four straight games [HoopsHabit, 31 Oct](https://hoopshabit.com/darius-garland-s-turnover-problems-are-a-cause-for-concern-for-the-clippers-01m6adnqymke). In Sunday's loss to Golden State he scored 15 on 4-of-12 but had only 3 turnovers. **Status:** playing through minor back tightness.
  - **Update 2 Nov:** he will play Monday against Toronto after being "noticeably banged up over the last few games" [Roundtable, 2 Nov](https://roundtable.io/sports/nba/clippers/news/la-clippers-vs-toronto-raptors-injury-report-is-kawhi-leonard-playing).
- **Ivica Zubac** (minutes): scoring −7.2, reb −2.3, ast −1.7, stocks −2.4, TO −0.1; bonus +3.7.
  - Current: 21.7 min, 9.0 pts, 4.0-6.7 FG, 1.0-2.0 FT, 9.0 reb, 1.3 ast, 0.0 stl, 1.0 blk, 1.7 TO
  - Projected: 31.1 min, 14.9 pts, 6.4-10.3 FG, 2.0-2.9 FT, 11.3 reb, 2.2 ast, 0.5 stl, 1.1 blk, 1.6 TO
  - **Status:** left ankle sprain. He missed Sunday's 98-90 loss to Brooklyn, his fourth straight absence, and Monday against Atlanta is his next chance; no timetable reported [CBS Sports / AP, 1 Nov](https://cbssports.com/nba/news/nets-hold-off-pacers-98-90-for-first-win-of-the-season) [CBS Sports, 31 Oct](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-ruled-out-for-sunday/). *ESPN est.* then 2 Nov.
  - **Update 2 Nov:** out Monday against Atlanta, a fifth straight miss. RotoWire now treats him as "week-to-week"; no team timetable reported [CBS Sports / RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-remains-out-indefinitely/). *ESPN est.* 9 Nov.
- **Near the line:** Nikola Jokic −7.4 (#1, efficiency, L7 59.7), Kevin Durant −5.2 (#4, efficiency, L7 37.8).

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 6 | 26.5 / 35.5 | 0.76 | 26.3 | 30.3 (3) | 26.3 (6) | 26.3 (6) | 46.2 | **−19.8** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 7 | 25.3 / 32.9 | 0.86 | 30.9 | 26.0 (4) | 30.9 (7) | 30.9 (7) | 46.4 | **−15.6** | 41.1 | Day-to-day, ESPN est. back 02 Nov |

- **Josh Giddey** (both): scoring −11.3, reb −3.9, ast −4.2, stocks −4.6, TO +2.9; bonus +1.2.
  - Current: 26.5 min, 8.5 pts, 3.2-8.3 FG, 1.3-1.8 FT, 5.3 reb, 7.5 ast, 0.5 stl, 0.2 blk, 2.3 TO
  - Last 7 days (3 GP): 26.7 min, 11.3 pts, 4.0-8.0 FG, 2.0-2.3 FT, 4.3 reb, 6.7 ast, 0.7 stl, 0.3 blk, 2.7 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
  - **What explains it:** Splitter's deep rotation caps his minutes. He scored a season-high 13 in 25 minutes at Boston on 30 Oct [Basketball Australia, 31 Oct](https://www.basketball.com.au/news/aussies-in-nba-results-october-31-2026-kyrie-irving). **Status:** a managed wrist sprain; no games missed [Hoops Rumors, 23 Oct](https://www.hoopsrumors.com/2026/10/bulls-notes-wilson-jones-giddey-buzelis-essengue-swain.html).
  - **Update 2 Nov:** not on Chicago's Monday report. RotoWire: "Giddey's usage is down 7 percentage points" [RotoWire, 2 Nov](https://www.rotowire.com/basketball/article/fantasy-basketball-buy-low-sell-high-week-3-trade-drop-targets-145002).
- **LaMelo Ball** (minutes): scoring −10.1, reb −2.3, ast −4.0, stocks +0.7, TO −0.8; bonus +1.0.
  - Current: 25.3 min, 14.4 pts, 5.0-12.7 FG, 1.6-2.1 FT, 3.3 reb, 6.3 ast, 1.9 stl, 0.0 blk, 3.7 TO
  - Last 7 days (4 GP): 27.0 min, 13.2 pts, 4.8-12.8 FG, 1.5-2.0 FT, 3.8 reb, 6.2 ast, 1.8 stl, 0.0 blk, 5.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
  - **What explains it:** foul trouble and turnovers. He shot 2-of-10 with 5 turnovers on Saturday, and Finch called the turnovers "unnecessary" [CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/). **Status:** healthy.
  - **Update 2 Nov:** new right wrist contusion; questionable Monday against Milwaukee, added hours before tip. Hyland and Dosunmu would gain minutes; no timetable reported [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/lamelo-ball-injury-iffy-with-wrist-issue-537212) [Yahoo Sports / ClutchPoints, 2 Nov](https://sports.yahoo.com/articles/timberwolves-lamelo-ball-lands-injury-220814099.html). *ESPN est.* 2 Nov.
- **Near the line:** Austin Reaves −6.5 (#4, efficiency, L7 27.8).

### Matt Wright's Foxies: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Shai Gilgeous-Alexander | OKC | #1 | 6 | 32.7 / 33.8 | 0.79 | 43.5 | 36.3 (3) | 43.5 (6) | 43.5 (6) | 56.8 | **−13.3** | 56.4 | Active |
| Jaren Jackson Jr. | UTAH | #8 | 4 | 26.0 / 31.4 | 0.86 | 27.0 | 11.0 (1) | 27.0 (4) | 27.0 (4) | 38.1 | **−11.1** | 35.9 | **Out**, ESPN est. back 14 Dec |

- **Shai Gilgeous-Alexander** (efficiency): scoring −7.6, reb −0.4, ast −6.1, stocks −1.0, TO +0.9; bonus +0.8.
  - Current: 32.7 min, 26.0 pts, 10.0-21.5 FG, 4.0-4.7 FT, 4.5 reb, 3.3 ast, 1.2 stl, 1.2 blk, 1.8 TO
  - Last 7 days (3 GP): 29.7 min, 24.3 pts, 9.3-19.0 FG, 4.0-4.7 FT, 4.3 reb, 2.7 ast, 0.7 stl, 0.7 blk, 2.3 TO
  - Projected: 33.8 min, 31.2 pts, 10.9-20.3 FG, 7.8-8.8 FT, 4.9 reb, 6.4 ast, 1.7 stl, 0.9 blk, 2.3 TO
  - **What explains it:** career-low assists on a gutted roster: 26 points but 3 assists at Houston on Saturday. Holmgren is out 8–10 weeks [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-scores-26-points-in-loss/). **Status:** healthy.
  - **Update 2 Nov:** healthy for Monday at Cleveland, with six Thunder players out (Caruso, Holmgren, Jalen Williams, Wallace, Topic, Sorber) [Cavaliers Nation, 2 Nov](https://cavaliersnation.com/2026/11/02/cavs-release-full-injury-report-ahead-of-mondays-matchup-vs-thunder/).
- **Jaren Jackson Jr.** (minutes): scoring −5.4, reb −0.7, ast −0.2, stocks −5.1, TO −1.4; bonus +1.8.
  - Current: 26.0 min, 16.2 pts, 5.5-11.0 FG, 4.0-5.2 FT, 5.0 reb, 2.0 ast, 0.2 stl, 1.2 blk, 3.0 TO
  - Last 7 days (1 GP): 10.0 min, 6.0 pts, 2.0-5.0 FG, 2.0-3.0 FT, 3.0 reb, 2.0 ast, 0.0 stl, 0.0 blk, 0.0 TO
  - Projected: 31.4 min, 21.9 pts, 7.8-16.7 FG, 4.3-5.4 FT, 5.7 reb, 2.1 ast, 1.2 stl, 1.6 blk, 2.3 TO
  - **Status:** torn right MCL; re-evaluated about 8 Dec, six to eight weeks reported; nothing new [Hoops Rumors, 27 Oct](https://www.hoopsrumors.com/2026/10/jaren-jackson-jr-to-miss-6-8-weeks-due-to-torn-mcl.html). *ESPN est.* 14 Dec.
  - **Update 2 Nov:** out Monday at San Antonio, as expected; the six-week re-evaluation (about 8 Dec) stands [Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/spurs-vs-jazz-gameday-betting-153428767.html) [NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026). *ESPN est.* 14 Dec.
- **Near the line:** Damian Lillard −8.8 (#6, efficiency, L7 22.7), Naz Reid −6.9 (#10, efficiency, L7 21.5), Pascal Siakam −5.3 (#4, efficiency, L7 35.8).

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 6 | 33.5 / 33.6 | 0.73 | 30.8 | 34.2 (4) | 30.8 (6) | 30.8 (6) | 42.1 | **−11.2** | 45.1 | Active |

- **James Harden** (efficiency): scoring −5.3, reb −0.2, ast −3.5, stocks −2.6, TO +0.1; bonus +0.2.
  - Current: 33.5 min, 16.7 pts, 4.8-12.8 FG, 4.5-5.3 FT, 4.8 reb, 6.3 ast, 0.8 stl, 0.3 blk, 3.3 TO
  - Last 7 days (4 GP): 33.8 min, 18.0 pts, 5.8-14.2 FG, 3.8-4.2 FT, 4.5 reb, 6.5 ast, 1.0 stl, 0.0 blk, 2.5 TO
  - Projected: 33.6 min, 20.6 pts, 6.1-14.3 FG, 5.6-6.4 FT, 5.0 reb, 8.1 ast, 1.2 stl, 0.6 blk, 3.4 TO
  - **2 Nov:** 13 points and 7 assists in 26 minutes of a blowout on Saturday. His L7 of 34.2 (4) is +3.4 over his season, under the flag; no new news. **Status:** healthy.
  - **Update 2 Nov:** healthy and a projected starter Monday against OKC [Cavaliers Nation, 2 Nov](https://cavaliersnation.com/2026/11/02/cavs-release-full-injury-report-ahead-of-mondays-matchup-vs-thunder/).
- **Near the line:** Alex Sarr −9.9 (#8, both, L7 27.0).

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Desmond Bane −9.2 (#8, efficiency, L7 37.0), Trey Murphy III −9.1 (#9, efficiency, L7 27.3), Jalen Duren −8.7 (#5, minutes, L7 —), Cade Cunningham −7.6 (#1, efficiency, L7 40.7), Kawhi Leonard −5.8 (#2, minutes, L7 —).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Derrick White −7.7 (#5, minutes, L7 27.2), Donovan Mitchell −6.1 (#2, efficiency, L7 37.8), AJ Dybantsa −5.9 (#8, minutes, L7 27.0).

### Melbourne poopoo: 0

No one flagged.

- **Near the line:** Anthony Davis −7.9 (#1, efficiency, L7 47.0), Jalen Brunson −7.3 (#4, efficiency, L7 43.7), Norman Powell −5.5 (#9, minutes, L7 33.0).

### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.8 (#1, minutes, L7 33.2), Devin Booker −5.2 (#5, efficiency, L7 22.0).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball, Jaren Jackson Jr., Ivica Zubac |
| efficiency | Shai Gilgeous-Alexander, Darius Garland, James Harden |
| both | Josh Giddey, Lauri Markkanen |

- **Flagged and not active on ESPN:** LaMelo Ball (Day-to-day, ESPN est. back 02 Nov), Ivica Zubac (**Out**, ESPN est. back 09 Nov), Jaren Jackson Jr. (**Out**, ESPN est. back 14 Dec).
- **Rostered, no games yet:** Kon Knueppel (Team Nic Kerr, projected 35.2, **Out**, ESPN est. back 09 Nov), Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 08 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** James Harden (Team Nic Kerr, L7 34.2 in 4 vs projected 42.1, season gap −11.2).
- **Not flagged, but 10+ under projection over the last 7 days:** Ty Jerome (Melbourne poopoo, L7 21.0 in 2 vs projected 43.5, L7 gap −22.5, season gap −0.7), Devin Booker (Snow Time Lakers, L7 22.0 in 2 vs projected 43.2, L7 gap −21.2, season gap −5.2), Jalen Johnson (Snow Time Lakers, L7 33.2 in 4 vs projected 50.0, L7 gap −16.7, season gap −6.8), Damian Lillard (Matt Wright's Foxies, L7 22.7 in 3 vs projected 38.6, L7 gap −15.9, season gap −8.8), Austin Reaves (Cream Abdul-Yammar, L7 27.8 in 4 vs projected 43.3, L7 gap −15.6, season gap −6.5), Naz Reid (Matt Wright's Foxies, L7 21.5 in 4 vs projected 35.5, L7 gap −14.0, season gap −6.9), Joel Embiid (Snow Time Lakers, L7 31.5 in 2 vs projected 45.4, L7 gap −13.9, season gap −5.0), Brook Lopez (Team Nic Kerr, L7 13.7 in 3 vs projected 26.2, L7 gap −12.5, season gap −0.7), Dyson Daniels (Snow Time Lakers, L7 25.0 in 4 vs projected 35.7, L7 gap −10.7, season gap 0.9), Derik Queen (Matt Wright's Foxies, L7 20.0 in 3 vs projected 30.5, L7 gap −10.5, season gap −3.8), Amen Thompson (Matt Wright's Foxies, L7 29.5 in 4 vs projected 40.0, L7 gap −10.5, season gap −2.1), Keyonte George (Cream Abdul-Yammar, L7 26.7 in 3 vs projected 36.8, L7 gap −10.1, season gap −2.8), Nickeil Alexander-Walker (Dr White Slong, L7 24.0 in 4 vs projected 34.1, L7 gap −10.1, season gap −2.3), VJ Edgecombe (Melbourne poopoo, L7 23.7 in 3 vs projected 33.7, L7 gap −10.0, season gap −4.0), Josh Hart (Dr White Slong, L7 23.0 in 3 vs projected 33.0, L7 gap −10.0, season gap −3.5).


### Notes

- **Ty Jerome** (opponent this week): missed 31 Oct with back soreness and is off the report for Monday against New Orleans [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/ty-jerome-back-removed-from-injury-report). His L7 is 21.0 (2), noise.
- **Devin Booker:** L7 22.0 (2), noise. He scored 3 on 26 Oct with no injury reported [Arizona Sports, 26 Oct](https://arizonasports.com/nba/phoenix-suns/devin-booker-scores-3-suns-vulnerable-thunder). Snow Time Lakers declined our Black offer for him.
- **Jalen Johnson** (2 Nov): sprained his left ankle on 31 Oct and was questionable for Monday at Indiana; no timetable reported [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-jalen-johnson-questionable-to-suit-up-monday/). *ESPN est.* 4 Nov.
- **Damian Lillard** (2 Nov): two cold shooting nights and blowout minutes, then 22 at Utah on 31 Oct [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-damian-lillard-drops-22-points-in-utah/).
- **Dyson Daniels:** no double-figure scoring in four games on unchanged minutes; no injury found [RotoWire ATL](https://www.rotowire.com/basketball/news.php?team=ATL) [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-dyson-daniels-active-defensively-in-loss/). Snow Time Lakers declined our Black offer for him.
- **Amen Thompson** (our pending target): in his L7 games he averaged 3.75 rebounds against 6.6 for the season, three of them were wins by 10 or more, and no injury or benching was found (`docs/research/20261102-0700-black-offers.md`). Only HotTakes reports an eye knock on 31 Oct, with no missed time; treat it as unconfirmed [HotTakes, 31 Oct](https://hottakes.com/articles/amen-thompson-heads-to-locker-room-with-eye-injury-as-rockets-keep-rolli-ce6532f8-5b8a-492e-bcee-1f930198a956) [RotoWire HOU, 2 Nov](https://www.rotowire.com/basketball/news.php?team=HOU).
- **VJ Edgecombe** (opponent): no report found [RotoWire PHI, 2 Nov](https://www.rotowire.com/basketball/news.php?team=PHI).
- **Not researched in this run:** Austin Reaves, Naz Reid, Joel Embiid, Brook Lopez, Derik Queen, Keyonte George, Nickeil Alexander-Walker, Josh Hart.

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Trey Murphy III | Come-in Cider (us) | 6 | 31.8 / 32.5 | 27.7 | 27.3 (3) | 27.7 (6) | 27.7 (6) | 36.8 | 41.6 |
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | 33.5 (2) | 33.5 (2) | 42.2 | 44.3 |
| Cade Cunningham | Come-in Cider (us) | 6 | 33.5 / 34.8 | 42.8 | 40.7 (3) | 42.8 (6) | 42.8 (6) | 50.4 | 53.3 |
| Nikola Jokic | Lauri Birds | 5 | 37.0 / 35.6 | 59.8 | 59.7 (3) | 59.8 (5) | 59.8 (5) | 67.2 | 74.9 |
| Alex Sarr | Team Nic Kerr | 6 | 25.5 / 28.6 | 26.7 | 27.0 (3) | 26.7 (6) | 26.7 (6) | 36.6 | 39.4 |

## Our pending trades

With **Team Nic Kerr**, proposed by us, expires 04 Nov 05:49 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jabari Smith Jr. | we receive | 7 | 34.3 / 32.1 | 39.1 | 40.5 (4) | 39.1 (7) | 39.1 (7) | 27.6 | +11.5 | Active |
| Anthony Black | we send | 4 | 28.0 / 28.9 | 36.2 | 33.7 (3) | 36.2 (4) | 36.2 (4) | 28.2 | +8.1 | **Out**, ESPN est. back 05 Nov |
| Fred VanVleet | we send | 5 | 30.6 / 32.2 | 35.4 | 31.3 (3) | 35.4 (5) | 35.4 (5) | 33.4 | +2.0 | Active |

With **Team Nic Kerr**, proposed by us, expires 04 Nov 06:18 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| James Harden | we receive | 6 | 33.5 / 33.6 | 30.8 | 34.2 (4) | 30.8 (6) | 30.8 (6) | 42.1 | −11.2 | Active |
| Anthony Black | we send | 4 | 28.0 / 28.9 | 36.2 | 33.7 (3) | 36.2 (4) | 36.2 (4) | 28.2 | +8.1 | **Out**, ESPN est. back 05 Nov |

With **Melbourne poopoo**, proposed by us, expires 04 Nov 06:29 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jalen Brunson | we receive | 6 | 34.8 / 35.3 | 36.5 | 43.7 (3) | 36.5 (6) | 36.5 (6) | 43.8 | −7.3 | Active |
| Anthony Black | we send | 4 | 28.0 / 28.9 | 36.2 | 33.7 (3) | 36.2 (4) | 36.2 (4) | 28.2 | +8.1 | **Out**, ESPN est. back 05 Nov |
| Fred VanVleet | we send | 5 | 30.6 / 32.2 | 35.4 | 31.3 (3) | 35.4 (5) | 35.4 (5) | 33.4 | +2.0 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | 40.0 (2) | 40.0 (2) | 45.8 | −5.8 | **Out**, ESPN est. back 23 Nov |

With **Matt Wright's Foxies**, proposed by us, expires 04 Nov 06:33 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Amen Thompson | we receive | 7 | 33.7 / 36.5 | 37.9 | 29.5 (4) | 37.9 (7) | 37.9 (7) | 40.0 | −2.1 | Active |
| Fred VanVleet | we send | 5 | 30.6 / 32.2 | 35.4 | 31.3 (3) | 35.4 (5) | 35.4 (5) | 33.4 | +2.0 | Active |
| Anthony Black | we send | 4 | 28.0 / 28.9 | 36.2 | 33.7 (3) | 36.2 (4) | 36.2 (4) | 28.2 | +8.1 | **Out**, ESPN est. back 05 Nov |


### Notes

- **Anthony Black** (we send): out Monday against Washington with "right ankle injury management" on the second night of a back-to-back. RotoWire and FSR Orlando call it rest [Athlon via Yardbarker, 2 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_wizards_magic_will_alex_sarr_anthony_black_play/s1_17615_44507641) [FSR Orlando, 2 Nov](https://fsrorlando.iheart.com/content/2026-11-02-wizards-vs-magic-injury-report-nov-2/).
  - No timetable reported beyond Monday; *ESPN est.* 5 Nov.
  - His last game was Sunday against Boston: a season-high 23 points, 8 rebounds, 3 assists and 2 steals in 33 minutes [RotoWire ORL](https://www.rotowire.com/basketball/news.php?team=ORL).
  - His L7 dropped from 36.2 (4) to 33.7 (3) only because his 25 Oct game left the window.
- **Kawhi Leonard** (in the Brunson offer): out Monday at LAC with left knee effusion. Rajakovic says he is "doing well", with the next update Tue 3 Nov [Basketnews, 2 Nov](https://basketnews.com/news-258646-kawhi-leonard-injury-update-raptors-coach-offers-promising-news.html). Haynes's "at least three to four weeks" stands; *ESPN est.* 23 Nov.
- **Fred VanVleet** (we send in three offers): off Houston's report for Monday [RotoWire HOU](https://www.rotowire.com/basketball/news.php?team=HOU). The owner gives him no weight in trades.
- **Amen Thompson** and **James Harden:** see the notes above.
- **Council verdict (2 Nov):** keep only the Thompson offer and withdraw the rest; 17 of 19 (`council/sessions/20261102-070000-black-offers.json`). Snow Time Lakers have since declined their three. Smith Jr., Harden and Brunson are still pending.

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-02 23:01 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- News opened 2 Nov 2026 (US) for this run:
  - [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/lauri-markkanen-wrist-returns-to-lineup-saturday)
  - [Sports Mole, 2 Nov](https://www.sportsmole.co.uk/basketball/utah-jazz/preview/utah-jazz-vs-san-antonio-spurs-player-props-injury-report-and-prediction--nba_608201.html)
  - [Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/spurs-vs-jazz-gameday-betting-153428767.html)
  - [HoopsHabit, 31 Oct](https://hoopshabit.com/darius-garland-s-turnover-problems-are-a-cause-for-concern-for-the-clippers-01m6adnqymke)
  - [Roundtable, 2 Nov](https://roundtable.io/sports/nba/clippers/news/la-clippers-vs-toronto-raptors-injury-report-is-kawhi-leonard-playing)
  - [CBS Sports / AP, 1 Nov](https://cbssports.com/nba/news/nets-hold-off-pacers-98-90-for-first-win-of-the-season)
  - [CBS Sports, 31 Oct](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-ruled-out-for-sunday/)
  - [CBS Sports / RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-remains-out-indefinitely/)
  - [Basketball Australia, 31 Oct](https://www.basketball.com.au/news/aussies-in-nba-results-october-31-2026-kyrie-irving)
  - [Hoops Rumors, 23 Oct](https://www.hoopsrumors.com/2026/10/bulls-notes-wilson-jones-giddey-buzelis-essengue-swain.html)
  - [RotoWire, 2 Nov](https://www.rotowire.com/basketball/article/fantasy-basketball-buy-low-sell-high-week-3-trade-drop-targets-145002)
  - [CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/)
  - [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/lamelo-ball-injury-iffy-with-wrist-issue-537212)
  - [Yahoo Sports / ClutchPoints, 2 Nov](https://sports.yahoo.com/articles/timberwolves-lamelo-ball-lands-injury-220814099.html)
  - [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-scores-26-points-in-loss/)
  - [Cavaliers Nation, 2 Nov](https://cavaliersnation.com/2026/11/02/cavs-release-full-injury-report-ahead-of-mondays-matchup-vs-thunder/)
  - [Hoops Rumors, 27 Oct](https://www.hoopsrumors.com/2026/10/jaren-jackson-jr-to-miss-6-8-weeks-due-to-torn-mcl.html)
  - [NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)
  - [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/ty-jerome-back-removed-from-injury-report)
  - [Arizona Sports, 26 Oct](https://arizonasports.com/nba/phoenix-suns/devin-booker-scores-3-suns-vulnerable-thunder)
  - [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-jalen-johnson-questionable-to-suit-up-monday/)
  - [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-damian-lillard-drops-22-points-in-utah/)
  - [RotoWire ATL](https://www.rotowire.com/basketball/news.php?team=ATL)
  - [CBS Sports, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-dyson-daniels-active-defensively-in-loss/)
  - [HotTakes, 31 Oct](https://hottakes.com/articles/amen-thompson-heads-to-locker-room-with-eye-injury-as-rockets-keep-rolli-ce6532f8-5b8a-492e-bcee-1f930198a956)
  - [RotoWire HOU, 2 Nov](https://www.rotowire.com/basketball/news.php?team=HOU)
  - [RotoWire PHI, 2 Nov](https://www.rotowire.com/basketball/news.php?team=PHI)
  - [Athlon via Yardbarker, 2 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_wizards_magic_will_alex_sarr_anthony_black_play/s1_17615_44507641)
  - [FSR Orlando, 2 Nov](https://fsrorlando.iheart.com/content/2026-11-02-wizards-vs-magic-injury-report-nov-2/)
  - [RotoWire ORL](https://www.rotowire.com/basketball/news.php?team=ORL)
  - [Basketnews, 2 Nov](https://basketnews.com/news-258646-kawhi-leonard-injury-update-raptors-coach-offers-promising-news.html)
