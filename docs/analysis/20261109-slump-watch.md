# Slump Watch: 09 Nov 2026

- Generated 2026-11-09 06:47 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 110 rostered players in league 423671879, through scoring period 20. Teams have played **2 to 11 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 20 (Sun 08 Nov US) re-scored from ESPN's final NBA box scores: all 47 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**5 rostered players are 10+ FP/g under projection, on 4 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 68.3/60.5 · LaMelo Ball 35.0/46.4 · Josh Giddey 30.7/46.2 |
| Lauri Birds | 1 | Nikola Jokic 64.4/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 50.6/43.0 |
| Matt Wright's Foxies | 1 | Shai Gilgeous-Alexander 48.1/56.8 · Cooper Flagg 51.8/45.4 · Evan Mobley 43.0/43.3 |
| Team Nic Kerr | 1 | Luka Doncic 68.3/60.6 · Domantas Sabonis 48.6/46.7 · Tyrese Maxey 46.9/45.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 47.0/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 46.1/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 59.0/57.6 · Donovan Mitchell 43.0/46.5 · Joel Embiid 36.6/45.4 |
| Melbourne poopoo | 0 | Anthony Davis 45.9/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 47.6/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 44.1/50.0 · Jayson Tatum 47.4/48.1 · Kyrie Irving 39.5/44.2 |

- **Injured players named in the table** (reported timeline, then *ESPN est.*):
  - **Nikola Jokic** (DEN, Lauri Birds): right elbow sprain, new on Denver's report. He is questionable for Monday at HOU. All five Nuggets starters are listed after plane trouble kept the team in Mexico City after Saturday's game ([Gazette, 8 Nov](https://gazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - **Tyrese Haliburton** (IND, Lauri Birds): left hamstring strain. He is progressing but still has no timetable ([CBS Sports / RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-timetable-to-return/)), and he is out Monday at DAL ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). *ESPN est.* 13 Nov.
  - **Luka Doncic** (LAL, Team Nic Kerr): low back tightness. He sat Sunday at DET, his second missed game this season ([NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)). His status for Monday at ATL, the second night of a back-to-back, "likely won't be known until Monday afternoon" ([Yahoo Sports, 8 Nov](https://sports.yahoo.com/articles/lakers-luka-doncic-sitting-against-213409924.html)). No timetable reported; *ESPN est.* 9 Nov.
  - **Domantas Sabonis** (SAC, Team Nic Kerr): left knee soreness. He was a late addition to the report and sat Sunday against MIA, his first missed game ([RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/domantas-sabonis-injury-out-sunday-538225); [NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)). No timetable reported; *ESPN est.* 10 Nov. Sacramento next plays Tuesday against ORL ([ESPN scoreboard, 10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)).
  - **Anthony Davis** (WSH, Melbourne poopoo): right ankle sprain. He is questionable for Monday at DET, the same tag he carried before each of the two games he missed ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-davis-ankle-questionable-monday-vs-det); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - **Anthony Edwards** (MIN, Melbourne poopoo): arthroscopic right knee surgery on 29 Oct, out "up to two months" per reports ([NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)). *ESPN est.* 21 Dec.
  - **Jamal Murray** and **Kawhi Leonard** (ours): see *Come-in Cider* below. *ESPN est.* 9 Nov and 23 Nov.

## Since the last Slump Watch

This compares with last night's `docs/analysis/20261108-slump-watch.md` (20:14 UTC). Sunday's seven games (scoring period 20) finished in between ([ESPN scoreboard, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261108)). The headline went from 7 flagged on 5 teams to 5 on 4.

- **Joined:** none.
- **Left:**
  - **Darius Garland** (Lauri Birds), −11.8 → −9.6, now near the line. On Sunday he had 24 points and 10 assists against NOP ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909950)).
  - **Joel Embiid** (Dr White Slong), −10.2 → −8.8, now near the line. On Sunday he had 18 points and 10 rebounds at CHI ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945)).
- **Moved 3+ FP/g:** Josh Giddey, −18.9 → −15.5. On Sunday he had 19 points, 7 rebounds and 15 assists against PHI ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945)).
  - LaMelo Ball went −11.9 → −11.4.
  - Ivica Zubac, Jaren Jackson Jr. and James Harden did not play Sunday, and their gaps are unchanged.
- **Near the line:**
  - Garland and Embiid joined.
  - Austin Reaves (Cream Abdul-Yammar, −6.6 last night) left after scoring 43 at DET ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909946)).
  - Trey Murphy III went −7.4 → −5.8, and Derrick White −6.8 → −5.8.
- **Last 7 days lists:**
  - Giddey joined *flagged, but within 10*, with an L7 of 39.3 in 3.
  - Dejounte Murray (ours) and Joel Embiid joined *not flagged, but 10+ under*. Austin Reaves and LeBron James left it.
- **Ours:** none flagged.
  - ESPN sync: Jalen Duren moved to IR and Kawhi Leonard came back to the bench, both on 9 Nov (`council/roster.csv`).
  - Cade Cunningham's season average went from 48.9 to 47.0.
  - Murphy's season went from 29.4 (8) to 31.0 (9), and his L7 from 34.5 (2) to 37.7 (3).
- **Pending trades:**
  - There is a new offer to Cream Abdul-Yammar, proposed by us: Kawhi Leonard + Murphy for Josh Giddey. It expires 11 Nov 00:38 UTC.
  - It sends the same two players as the Melbourne poopoo offer for Jalen Brunson, which still expires 10 Nov 02:55 UTC (see *Our pending trades*).

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 9 | 28.0 / 35.5 | 0.84 | 30.7 (9) → 34.1 (8) | 39.3 (3) | 35.7 (7) | 30.7 (9) → 34.1 (8) | 46.2 | **−15.5** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 11 | 27.8 / 32.9 | 0.89 | 35.0 (11) | 42.2 (4) | 34.9 (9) | 35.0 (11) | 46.4 | **−11.4** | 41.1 | Active |

- **Josh Giddey** (both): scoring −9.0, reb −4.3, ast −2.3, stocks −3.7, TO +2.0; bonus +1.8.
  - Current: 28.0 min, 10.3 pts, 3.9-9.3 FG, 1.6-2.2 FT, 4.9 reb, 8.4 ast, 0.6 stl, 0.3 blk, 2.8 TO
  - Last 7 days (3 GP): 31.0 min, 14.0 pts, 5.3-11.3 FG, 2.0-3.0 FT, 4.0 reb, 10.3 ast, 0.7 stl, 0.7 blk, 3.7 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
  - **What explains the season gap:** Splitter's rebuild moved the offense away from him.
    - Through eight games he took 9.0 shots a game, against 16.4 at the same point last season, in about seven fewer minutes.
    - His defensive rebounds fell as Chicago crashes the offensive glass, and the Bulls' league-worst three-point shooting has cut his assists ([Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)).
  - **The last 7 days:** L7 39.3 (3), 8.7 over his season of 30.7 (9) (`form.py`). His minutes are up, 31.0 over the last 7 days against 28.0 for the season.
    - Sunday against PHI: 19 points on 7-of-12, 7 rebounds, a season-high 15 assists and 5 turnovers in 34 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945)).
    - He said he "needed to play more downhill, rather than laterally". Splitter: "He was the Josh that we know" ([Chicago Sun-Times, 8 Nov](https://chicago.suntimes.com/bulls/2026/11/08/josh-giddey-chicago-bulls-tiago-splitter-isaac-okoro-norman-powell-matas-buzelis-caleb-wilson-jalen-smith-philadelphia-76ers)).
  - **Status:** healthy. Chicago manages a left wrist sprain from preseason, which Splitter says has not affected his play ([Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)).
  - He is the player we would receive in the new Cream Abdul-Yammar offer (see *Our pending trades*).
- **LaMelo Ball** (minutes): scoring −4.4, reb −2.3, ast −4.6, stocks +0.5, TO −1.4; bonus +0.8.
  - Current: 27.8 min, 18.3 pts, 6.4-14.2 FG, 2.2-2.7 FT, 3.3 reb, 6.0 ast, 1.7 stl, 0.1 blk, 4.0 TO
  - Last 7 days (4 GP): 32.2 min, 25.0 pts, 8.8-16.8 FG, 3.2-3.8 FT, 3.2 reb, 5.5 ast, 1.5 stl, 0.2 blk, 4.5 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
  - **What explains the season gap:** minutes, 27.8 a game against 32.9 projected. Early on he had foul trouble and turnovers ([CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/)).
  - **The last 7 days:** L7 42.2 (4), 7.2 over his season of 35.0 (11) (`form.py`). His minutes are 32.2 over the last 7 days.
    - With Anthony Edwards out, he is "continuing to assume a larger offensive role". He has scored 20+ in five of his last six games ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/lamelo-ball-tallies-24-points-in-win-over-jazz)).
    - Sunday against UTAH: 24 points on 10-of-20, 5 assists, 2 steals and 5 turnovers in 30 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909947)).
  - **Status:** healthy. Edwards is out "up to two months" after knee surgery on 29 Oct ([NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)); *ESPN est.* 21 Dec.

### Lauri Birds: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Ivica Zubac | IND | #8 | 5 | 20.6 / 31.1 | 0.98 | 23.0 (5) → 27.2 (4) | 19.5 (2) | 15.0 (3) → 19.5 (2) | 23.0 (5) → 27.2 (4) | 35.5 | **−12.5** | 36.3 | Active |

- **Ivica Zubac** (minutes): scoring −9.3, reb −2.7, ast −0.0, stocks −4.0, TO −0.4; bonus +4.0.
  - Current: 20.6 min, 7.6 pts, 3.2-6.0 FG, 1.2-2.0 FT, 8.6 reb, 2.2 ast, 0.0 stl, 0.6 blk, 1.8 TO
  - Last 7 days (2 GP): 19.0 min, 5.5 pts, 2.0-5.0 FG, 1.5-2.0 FT, 8.0 reb, 3.5 ast, 0.0 stl, 0.0 blk, 2.0 TO
  - Projected: 31.1 min, 14.9 pts, 6.4-10.3 FG, 2.0-2.9 FT, 11.3 reb, 2.2 ast, 0.5 stl, 1.1 blk, 1.6 TO
  - **What explains it:** minutes since he came back from a left ankle sprain that cost him five games.
    - Wednesday at MEM, his first game back, he played 18:47 and went 0-of-5 ([RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/ivica-zubac-news-returning-versus-memphis-537562)).
    - Saturday against DEN: 10 points, 12 rebounds and 5 assists in 19 minutes, with foul trouble ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909938)).
    - RotoWire expects him to get "closer to 30 minutes per game in the not too distant future" ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-double-doubles-despite-loss/)).
  - **Status:** healthy, and no game since Saturday. He is not on Indiana's list for Monday at DAL ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).
  - His L7 and his outlier-adjusted L15 rest on 2 games: small sample. Our offer for him was canceled on 8 Nov.
- **Near the line:** Darius Garland −9.6 (#5, efficiency, L7 32.2), Kevin Durant −6.9 (#4, efficiency, L7 32.0), Lauri Markkanen −6.2 (#7, minutes, L7 44.0).
  - **Darius Garland** (off the flagged list): `form.py` gives L7 32.2 (4), L15 30.1 (7), L30 30.8 (9), season 30.8 (9), projected 40.4.
    - Sunday against NOP: 24 points on 6-of-11 (9-of-12 FT) and 10 assists in 32 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909950)).
    - His 2 turnovers were his fewest in a game this season. Turnovers were the biggest item on his driver line last night (TO −4.8) ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/darius-garland-drops-24-points-10-assists-sunday); `docs/analysis/20261108-slump-watch.md`).
  - **Lauri Markkanen:** right wrist sprain, from his 6-minute exit on 26 Oct.
    - He was out Sunday at MIN ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/lauri-markkanen-wrist-out-sunday-vs-min); [NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)). No timetable reported; *ESPN est.* 10 Nov.
    - Utah next plays Tuesday against MIA ([ESPN scoreboard, 10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)).
    - `form.py`: L7 44.0 (3), L15 33.2 (6) → 39.8 (5), L30 32.5 (8) → 37.1 (7), season 32.5 (8) → 37.1 (7), projected 38.7.
    - His L7 is 11.5 over his season. His minutes were back up before the injury (34.7 over the last 7 days, 30.9 for the season), and the 26 Oct exit is dropped from his season as a short game.
  - **Kevin Durant:** see *Last 7 days*.

### Matt Wright's Foxies: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jaren Jackson Jr. | UTAH | #8 | 4 | 26.0 / 31.4 | 0.86 | 27.0 (4) → 32.3 (3) | — | 13.5 (2) → 16.0 (1) | 27.0 (4) → 32.3 (3) | 38.1 | **−11.1** | 35.9 | **Out**, ESPN est. back 14 Dec |

- **Jaren Jackson Jr.** (minutes): scoring −5.4, reb −0.7, ast −0.2, stocks −5.1, TO −1.4; bonus +1.8.
  - Current: 26.0 min, 16.2 pts, 5.5-11.0 FG, 4.0-5.2 FT, 5.0 reb, 2.0 ast, 0.2 stl, 1.2 blk, 3.0 TO
  - Projected: 31.4 min, 21.9 pts, 7.8-16.7 FG, 4.3-5.4 FT, 5.7 reb, 2.1 ast, 1.2 stl, 1.6 blk, 2.3 TO
  - **Status:** torn right MCL on 26 Oct, in the 10-minute game dropped from his windows. No surgery needed.
    - Six to eight weeks reported, with a re-evaluation at about six weeks, around 8 Dec ([NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)). *ESPN est.* 14 Dec.
    - He was out Sunday at MIN ([NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)). No newer update was found.
  - His L15 rests on 2 games, and 1 after the dropped game: small sample.
- **Near the line:** Shai Gilgeous-Alexander −8.7 (#1, efficiency, L7 55.0), Damian Lillard −8.1 (#6, efficiency, L7 31.5), Brandon Miller −6.9 (#9, minutes, L7 12.3), Naz Reid −6.6 (#10, efficiency, L7 29.7), De'Aaron Fox −5.4 (#7, efficiency, L7 23.0).
  - **Brandon Miller** (out Monday with a right hip strain, [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf); no timetable reported, *ESPN est.* 12 Nov) and **De'Aaron Fox:** see *Last 7 days*.

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 10 | 33.3 / 33.6 | 0.73 | 30.4 (10) | 29.8 (4) | 31.4 (9) | 30.4 (10) | 42.1 | **−11.7** | 45.1 | Active |

- **James Harden** (efficiency): scoring −6.4, reb +0.0, ast −4.6, stocks −2.0, TO +1.0; bonus +0.3.
  - Current: 33.3 min, 15.7 pts, 4.5-12.3 FG, 4.2-5.0 FT, 5.0 reb, 5.8 ast, 0.7 stl, 0.6 blk, 2.9 TO
  - Last 7 days (4 GP): 33.0 min, 14.2 pts, 4.0-11.5 FG, 3.8-4.5 FT, 5.2 reb, 5.0 ast, 0.5 stl, 1.0 blk, 2.2 TO
  - Projected: 33.6 min, 20.6 pts, 6.1-14.3 FG, 5.6-6.4 FT, 5.0 reb, 8.1 ast, 1.2 stl, 0.6 blk, 3.4 TO
  - **What explains it:** scoring and assists. His minutes are on projection.
    - Saturday against NYK: 7 points on 2-of-9, 5 assists and 2 blocks in 34 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940)).
    - Over his last five games he averaged 14.0 points and 5.4 assists in 31.6 minutes ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-james-harden-struggles-in-loss/)).
  - **The last 7 days:** L7 29.8 (4), within 5 of his season 30.4 (10).
  - **Status:** no injury reported, and no game since Saturday. He is not on Cleveland's list for Monday at CHA ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).
- **Near the line:** Trae Young −6.9 (#4, efficiency, L7 29.5), Alex Sarr −6.5 (#7, efficiency, L7 37.0).
  - **Trae Young:** see *Last 7 days*.

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.8 (#8, efficiency, L7 37.7).
  - **Jalen Duren** (now in our IR slot): right hamstring strain.
    - On 8 Nov he was cleared for on-court work, with a re-evaluation in two weeks, about 22 Nov. Paul Reed stays the starting center ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work); [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)). *ESPN est.* 24 Nov.
    - He sat Sunday's loss to LAL, in which Walker Kessler had 12 points and 16 rebounds. SI: "The absence of Duren was huge once again" ([SI Pistons On SI, 8 Nov](https://www.si.com/nba/pistons/onsi/3-takeaways-from-pistons-stunning-loss-to-luka-less-lakers-01m6yze5022p)).
    - His season rests on 2 games, and 1 after his 10-minute exit is dropped: small sample.
  - **Kawhi Leonard** (back on our bench from IR): left knee.
    - Treatment for the swelling is finished, and he is in the return-to-play process ([Raptors Republic, 3 Nov](https://raptorsrepublic.com/2026/11/03/raptors-announce-update-on-kawhi-leonards-health/)).
    - He is due a re-evaluation by about 10 Nov, and RotoWire calls a return before the end of November unlikely ([CBS Sports / RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)). *ESPN est.* 23 Nov.
    - He is out Monday against MEM ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No newer update was found.
    - He has no games in his L7 or L15, and his season of 40.0 rests on 2 games: small sample.
  - **Trey Murphy III:**
    - Sunday at LAC: 26 points on 9-of-17 (4 threes, 4-of-4 FT), 7 rebounds and 3 assists in 30 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909950)). That matches his season high and came after 12-of-28 shooting in his previous three games ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/trey-murphy-hits-four-triples-scores-26-points)).
    - His L7 37.7 (3) is 6.7 over his season of 31.0 (9) (`form.py`). The reasons are more minutes (34.7 over the last 7 days, 32.8 for the season) and Sunday's shooting.
    - He has played through bilateral patella tendinopathy ([NBA injury report, 8 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_01_00AM.pdf)). The Pelicans' report for Monday at GS was not yet submitted at 1:00 AM ET ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).
  - **Dejounte Murray** (on the *Last 7 days* list): see *Last 7 days*.
  - **Jamal Murray** (not near the line): left shin/tibia contusion.
    - He is questionable for Monday at HOU. All five Denver starters are listed after plane trouble kept the team in Mexico City, and the reports do not say when he was hurt ([Gazette, 8 Nov](https://gazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/); [NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
    - `form.py`: L7 43.7 (3), L15 51.7 (7), L30 46.1 (8) → 51.7 (7), season 46.1 (8) → 51.7 (7), projected 43.9.
  - **Scottie Barnes** (not near the line): left adductor, listed as a left groin strain.
    - He missed Friday at MIL. He was limited in Sunday's practice and is questionable for Monday against MEM ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
    - `form.py`: L7 44.3 (3), L15 45.2 (6) → 51.8 (5), L30 45.9 (8) → 50.7 (7), season 45.9 (8) → 50.7 (7), projected 43.7.
  - **Caleb Wilson** (not near the line): `form.py` gives L7 27.7 (3), L15 38.7 (7), L30 35.9 (9), season 35.9 (9), projected 34.9.
    - His L7 is 8.2 under his season, with fewer minutes (29.3 over the last 7 days, 32.4 for the season).
    - 4 Nov at NYK: 5 points on 2-of-12 in 22 minutes ([ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909926)). Splitter benched him from midway through the third quarter over his shot selection, defense and body language ([Chicago Sun-Times, 4 Nov](https://chicago.suntimes.com/bulls/2026/11/04/bulls-embarrassed-new-york-rookie-caleb-wilson-soft-benching)).
    - Sunday against PHI: 18 points on 7-of-18, 5 rebounds, 0 assists and 3 turnovers in 32 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945); [NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/caleb-wilson-finishes-loss-with-18-points)). No injury reported.
  - **Cade Cunningham** (not near the line): `form.py` gives L7 55.3 (3), L15 49.3 (7), L30 47.0 (9), season 47.0 (9), projected 50.4.
    - His L7 is 8.3 over his season, with steady minutes (35.0 over the last 7 days, 34.0 for the season). No role change was found. The window rests on 3 games.
    - 4 Nov against PHI: 26 points, 7 rebounds and 11 assists in 40 minutes ([ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909922)).
    - Sunday against LAL: 14 points on 6-of-15 (1-of-6 from three), with no field goal in the first half, plus 8 assists, 4 turnovers and 5 fouls in 38 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909946); [NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/cade-cunningham-held-to-14-points-against-lakers)). No injury reported.
  - **Yaxel Lendeborg** (not near the line): `form.py` gives L7 47.5 (4), L15 42.0 (8) → 48.3 (7), L30 40.7 (10) → 45.4 (9), season 40.7 (10) → 45.4 (9), projected 33.7.
    - His L7 is 6.8 over his raw season. The reason is one game: the raw season includes his −2.0 FP game on 30 Oct, which `gamelog.py` drops (`form.py` outlier list, 06:48 UTC). Against the adjusted 45.4, his L7 is within 5. His minutes are steady (32.5 over the last 7 days, 32.2 for the season).
    - No injury or role news was found. His last three games ran 29 to 37 minutes ([ESPN box score, 2 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909919); [5 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909937); [7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909942)).
  - **Anthony Black** (added for Aday Mara):
    - He left Saturday's overtime loss at GSW with left leg cramps, after 18 points, 8 rebounds, 6 assists, 4 steals and 3 blocks. He has no injury designation, and Orlando next plays Tuesday at SAC ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)). No newer report was found.
    - Tuesday at SAC and Wednesday at UTAH are a back-to-back. He sat the second night of the last one, on 2 Nov, for right ankle management ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)).
    - `form.py`: L7 41.0 (3), L15 38.5 (6) → 44.0 (5), L30 38.5 (6) → 44.0 (5), season 38.5 (6) → 44.0 (5), projected 28.2.

### Dr White Slong: 0

No one flagged.

- **Near the line:** Joel Embiid −8.8 (#3, efficiency, L7 31.8), Derrick White −5.8 (#6, minutes, L7 32.6), AJ Dybantsa −5.1 (#10, efficiency, L7 28.2).
  - **Joel Embiid** (off the flagged list): see *Last 7 days*.

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −5.9 (#1, minutes, L7 51.0).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | Ivica Zubac, LaMelo Ball, Jaren Jackson Jr. |
| efficiency | James Harden |
| both | Josh Giddey |

- **Flagged and not active on ESPN:** Jaren Jackson Jr. (**Out**, ESPN est. back 14 Dec).
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 10 Nov).
  - **Brandon Ingram:** recovering from heel surgery in May, during which a partially torn Achilles was found and treated. After a G League stint he said on Friday, "I'm pretty close" ([Yahoo Sports / USA Today, 7 Nov](https://sports.yahoo.com/articles/brandon-ingram-pretty-close-making-014045418.html)).
    - He was out Sunday against NOP ([NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)). The Clippers next play Tuesday at PHX ([ESPN scoreboard, 10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)).
    - No return date reported; *ESPN est.* 10 Nov.

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** LaMelo Ball (Cream Abdul-Yammar, L7 42.2 in 4 vs projected 46.4, season gap −11.4), Josh Giddey (Cream Abdul-Yammar, L7 39.3 in 3 vs projected 46.2, season gap −15.5).
- **Not flagged, but 10+ under projection over the last 7 days:** Dejounte Murray (Come-in Cider (us), L7 24.7 in 3 vs projected 39.0, L7 gap −14.4, season gap −4.0), Brandon Miller (Matt Wright's Foxies, L7 12.3 in 3 vs projected 37.4, L7 gap −25.1, season gap −6.9), Jarrett Allen (Dr White Slong, L7 15.5 in 2 vs projected 36.9, L7 gap −21.4, season gap −2.9), De'Aaron Fox (Matt Wright's Foxies, L7 23.0 in 4 vs projected 38.2, L7 gap −15.2, season gap −5.4), Trae Young (Team Nic Kerr, L7 29.5 in 4 vs projected 44.4, L7 gap −14.9, season gap −6.9), Joel Embiid (Dr White Slong, L7 31.8 in 4 vs projected 45.4, L7 gap −13.6, season gap −8.8), Amen Thompson (Matt Wright's Foxies, L7 28.7 in 3 vs projected 40.0, L7 gap −11.3, season gap −4.9), Kevin Durant (Lauri Birds, L7 32.0 in 3 vs projected 42.9, L7 gap −10.9, season gap −6.9), Domantas Sabonis (Team Nic Kerr, L7 36.3 in 3 vs projected 46.7, L7 gap −10.4, season gap 1.9), Cameron Boozer (Lauri Birds, L7 24.3 in 3 vs projected 34.3, L7 gap −10.0, season gap 0.0).

### Notes

L7, L15 and L30 for players outside the tables come from `python council/form.py`, run 06:48 UTC. Only Embiid and Dejounte Murray on this list played Sunday; the other entries carry over last night's research, with new status lines where there was news.

- **LaMelo Ball** and **Josh Giddey:** see *Cream Abdul-Yammar*. Ball's minutes are up with Anthony Edwards out. Giddey had 15 assists on Sunday.
- **Dejounte Murray (NO, ours):** `form.py` gives L7 24.7 (3), L15 29.8 (5), L30 35.0 (7), season 35.0 (7), projected 39.0.
  - **The last 7 days:** 10.3 under his season (`form.py`), with more minutes (36.0 over the last 7 days, 33.9 for the season), so the cause is shooting.
    - Friday against MIN: 7 points on 3-of-11 in 35 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909293)).
    - Sunday at LAC: 6 points on 1-of-6, 3 rebounds and 3 assists in 28 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909950)).
    - SI graded Sunday a D: "far too often he seems to be playing a different game" than his teammates ([SI Pelicans On SI, 8 Nov](https://www.si.com/nba/pelicans/onsi/grading-every-pelicans-player-after-loss-vs-clippers)).
  - The window also holds 4 Nov against UTAH, his first game back from three games of paternity leave: 20 points, 8 rebounds and 4 steals in 45 minutes ([RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/dejounte-murray-news-removed-from-injury-report-537484); [ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909928)). The leave is why his L15 has only 5 games.
  - No injury found.
- **Brandon Miller (CHA):** `form.py` gives L7 12.3 (3), L15 35.0 (8), L30 30.5 (10), season 30.5 (10), projected 37.4.
  - **The last 7 days:** 18.2 under his season (`form.py`), with 23.7 minutes over the last 7 days against 31.0 for the season. He left Friday's game against BOS in the second quarter: 8 points on 3-of-10 in 14 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909288)).
  - **Status:** the groin soreness has been diagnosed as a right hip strain, and he is out Monday against CLE ([Yahoo Sports / HoopsHype, 8 Nov](https://sports.yahoo.com/articles/lastly-brandon-miller-diagnosed-223257025.html); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 12 Nov.
- **Jarrett Allen (CLE):** `form.py` gives L7 15.5 (2) → 31.0 (1), L15 34.6 (7) → 40.3 (6), L30 34.0 (8) → 38.9 (7), season 34.0 (8) → 38.9 (7), projected 36.9.
  - His L7 rests on 2 games, and 1 after the drop: noise and a small sample. The dropped game is his 7-minute exit on 4 Nov after a knee-to-knee collision ([Heavy, 7 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/jarrett-allen-injury-knicks/)).
  - **Status:** right knee contusion. He has missed two games and is questionable for Monday at CHA ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jarrett-allen-knee-questionable-monday-vs-cha); [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
- **De'Aaron Fox (SA):** `form.py` gives L7 23.0 (4), L15 31.1 (8), L30 32.8 (10), season 32.8 (10), projected 38.2.
  - **The last 7 days:** 9.8 under his season (`form.py`), with fewer minutes: 25.8 over the last 7 days against 29.5 for the season.
  - Friday at SAC he played 26 minutes and scored 9 points. Saturday at POR he played 22 minutes: 8 points on 1-of-3 and 6 assists ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909295); [ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909944)).
  - No injury or role report found. He is not on San Antonio's list for Monday at PHX ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).
- **Trae Young (WSH):** `form.py` gives L7 29.5 (4), L15 35.8 (8), L30 37.5 (10), season 37.5 (10), projected 44.4.
  - **The last 7 days:** 8.0 under his season (`form.py`).
    - Friday at ATL: 23 points and 10 assists, but 9 turnovers ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909287)).
    - Saturday at OKC: 4 points on 1-of-6 in 28 minutes in a 114-75 loss ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/wizards-trae-young-shooting-woes-in-blowout-loss/)).
  - Anthony Davis sat both games and is questionable for Monday at DET (see the headline). No injury found for Young.
- **Joel Embiid (PHI):** `form.py` gives L7 31.8 (4) → 39.0 (3), L15 36.0 (7) → 40.3 (6), L30 36.6 (9) → 39.9 (8), season 36.6 (9) → 39.9 (8), projected 45.4.
  - **The last 7 days:** the dropped game explains his L7. On 6 Nov at CLE he went 0-of-9 from the field for 6 points ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289)). Without that game, his L7 is 39.0 (3).
  - Sunday at CHI: 18 points on 7-of-19, 10 rebounds (8 offensive), 5 assists and 2 steals in 29 minutes ([ESPN box score, 8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945); [NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/joel-embiid-records-18-10-5-2-line-vs-chicago)).
  - **Status:** he is managing plantar fasciitis in his right foot. He had a 25-minute limit on 2 Nov, and he sits back-to-backs ([Philadelphia Inquirer, 3 Nov](https://www.inquirer.com/sixers/joel-embiid-philadelphia-76ers-plantar-fasciitis-nick-nurse-injuries-20261103.html)).
- **Amen Thompson (HOU):** `form.py` gives L7 28.7 (3), L15 30.9 (8), L30 35.1 (10), season 35.1 (10), projected 40.0.
  - **The last 7 days:** 6.4 under his season (`form.py`). Wednesday against MIN he scored 11 points on 3-of-9 ([ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909930)). Saturday at PHX he had 17 points, 7 rebounds and 4 blocks in 39 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943)).
  - No injury found.
- **Kevin Durant (HOU):** `form.py` gives L7 32.0 (3), L15 35.1 (8), L30 36.0 (10), season 36.0 (10), projected 42.9. His L7 is within 5 of his season.
  - Saturday at PHX: 21 points on 5-of-14 (1-of-7 from three) and 10 rebounds in 38 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943)). No injury found.
- **Domantas Sabonis (SAC):** `form.py` gives L7 36.3 (3), L15 43.3 (7), L30 48.6 (9), season 48.6 (9), projected 46.7.
  - **The last 7 days:** 12.2 under his season (`form.py`), with fewer minutes: 32.3 over the last 7 days against 35.6 for the season. NBC wrote that "he isn't getting the ball much" ([NBC Sports / Rotoworld, 7 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-07/domantas-sabonis-with-17-12-in-loss-to-the-spurs)).
  - **Status:** left knee soreness. He sat Sunday against MIA, a late addition to the report ([RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/domantas-sabonis-injury-out-sunday-538225)). No timetable reported; *ESPN est.* 10 Nov.
- **Cameron Boozer (MEM):** `form.py` gives L7 24.3 (3), L15 34.3 (7), L30 34.3 (9), season 34.3 (9), projected 34.3.
  - **The last 7 days:** 10.0 under his season (`form.py`). His minutes held (34.0 over the last 7 days, 32.0 for the season), so the cause is shooting.
  - Friday against OKC: 8 points on 2-of-14 (0-of-8 from three) and 12 rebounds in 31 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909291)). No injury found.

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 9 | 32.8 / 32.5 | 31.0 | 37.7 (3) | 34.4 (7) | 31.0 (9) | 36.8 | 41.6 |
| Lauri Markkanen | Lauri Birds | 8 | 30.9 / 34.0 | 32.5 | 44.0 (3) | 33.2 (6) → 39.8 (5) | 32.5 (8) → 37.1 (7) | 38.7 | 44.4 |
| Nikola Jokic | Lauri Birds | 8 | 35.9 / 35.6 | 64.4 | 72.0 (3) | 70.0 (7) | 64.4 (8) → 70.0 (7) | 67.2 | 74.9 |

- **Jalen Duren** (out; re-evaluated about 22 Nov, *ESPN est.* 24 Nov) and **Trey Murphy III:** see *Come-in Cider*. Duren's season rests on 2 games, and 1 after the drop: small sample.
- **Lauri Markkanen** (out Sunday with a right wrist sprain; no timetable reported, *ESPN est.* 10 Nov): see *Lauri Birds*.
- **Nikola Jokic** (questionable Monday with a right elbow sprain; no timetable reported, *ESPN est.* 9 Nov): see the headline ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).

## Our pending trades

With **Cream Abdul-Yammar**, proposed by us, expires 11 Nov 00:38 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | we receive | 9 | 28.0 / 35.5 | 30.7 | 39.3 (3) | 35.7 (7) | 30.7 (9) → 34.1 (8) | 46.2 | −15.5 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | 40.0 (2) | 45.8 | −5.8 | **Out**, ESPN est. back 23 Nov |
| Trey Murphy III | we send | 9 | 32.8 / 32.5 | 31.0 | 37.7 (3) | 34.4 (7) | 31.0 (9) | 36.8 | −5.8 | Active |

With **Melbourne poopoo**, proposed by us, expires 10 Nov 02:55 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jalen Brunson | we receive | 9 | 33.9 / 35.3 | 39.4 | 45.3 (3) | 43.7 (7) | 39.4 (9) | 43.8 | −4.4 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | 40.0 (2) | 45.8 | −5.8 | **Out**, ESPN est. back 23 Nov |
| Trey Murphy III | we send | 9 | 32.8 / 32.5 | 31.0 | 37.7 (3) | 34.4 (7) | 31.0 (9) | 36.8 | −5.8 | Active |

### Notes

- **Two offers, the same two players.** Both pending offers send Kawhi Leonard + Trey Murphy III. The Melbourne poopoo offer for Jalen Brunson expires first, at 02:55 UTC Tue 10 Nov (9:55 pm ET Mon 9). The Cream Abdul-Yammar offer for Josh Giddey is new since last night and expires at 00:38 UTC Wed 11 Nov (ESPN `mPendingTransactions`, read by the script at 06:47 UTC).
- **Josh Giddey:** see *Cream Abdul-Yammar*.
  - `form.py` gives L7 39.3 (3), L15 35.7 (7), L30 30.7 (9) → 34.1 (8), projected 46.2.
  - He had a season-high 15 assists on Sunday and is healthy ([Chicago Sun-Times, 8 Nov](https://chicago.suntimes.com/bulls/2026/11/08/josh-giddey-chicago-bulls-tiago-splitter-isaac-okoro-norman-powell-matas-buzelis-caleb-wilson-jalen-smith-philadelphia-76ers)).
  - Chicago does not play again until after Tuesday ([ESPN scoreboard, 9 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261109); [10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)).
- **Jalen Brunson:** his L7 45.3 (3) is 5.9 over his season of 39.4 (`form.py`). The reason is shot volume:
  - 4 Nov against CHI: 33 points on 10-of-17 in 28 minutes ([ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909926)).
  - Saturday at CLE: 31 points on 12-of-25, 9 assists and 1 turnover in 34 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940)).
  - He did not play Sunday. New York next plays Tuesday against MIL, after the offer expires ([ESPN scoreboard, 10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)). No in-season injury news was found.
- **Kawhi Leonard:** out Monday against MEM ([NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)).
  - His re-evaluation is due by about 10 Nov ([CBS Sports / RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)), and it may come after the Brunson offer expires.
  - *ESPN est.* 23 Nov. His season of 40.0 rests on 2 games: small sample.
- **Trey Murphy III:** see *Come-in Cider*.
  - He scored 26 on Sunday ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/trey-murphy-hits-four-triples-scores-26-points)).
  - The Pelicans play at GS at 03:00 UTC Tue 10 Nov, five minutes after the Brunson offer expires ([ESPN scoreboard, 9 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261109)).

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-09 06:47 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- `python council/form.py` (06:48 UTC) for L7, L15 and L30 of players outside the tables and for the outlier list. `python council/injuries.py --rostered --details` (06:49 UTC) for *ESPN est.* `council/roster.csv` (written by `council/espn_sync.py`) for our roster moves.
- Last night's report, `docs/analysis/20261108-slump-watch.md`, for the comparison and the carried-over research.
- Official NBA injury reports:
  - [NBA injury report, 9 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_00AM.pdf)
  - [NBA injury report, 8 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_08_00PM.pdf)
  - [NBA injury report, 8 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_01_00AM.pdf)
- ESPN scoreboards: [8 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261108), [9 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261109), [10 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261110)
- News opened or found on 9 Nov:
  - [Gazette, 8 Nov](https://gazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/)
  - [Yahoo Sports, 8 Nov (Doncic)](https://sports.yahoo.com/articles/lakers-luka-doncic-sitting-against-213409924.html)
  - [RotoWire, 8 Nov (Sabonis)](https://www.rotowire.com/basketball/headlines/domantas-sabonis-injury-out-sunday-538225)
  - [NBC Sports / Rotoworld, 8 Nov (Davis)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-davis-ankle-questionable-monday-vs-det)
  - [CBS Sports / RotoWire, 7 Nov (Haliburton)](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-timetable-to-return/)
  - [Chicago Sun-Times, 8 Nov (Giddey)](https://chicago.suntimes.com/bulls/2026/11/08/josh-giddey-chicago-bulls-tiago-splitter-isaac-okoro-norman-powell-matas-buzelis-caleb-wilson-jalen-smith-philadelphia-76ers)
  - [NBC Sports / Rotoworld, 8 Nov (Ball)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/lamelo-ball-tallies-24-points-in-win-over-jazz)
  - [NBC Sports / Rotoworld, 8 Nov (Garland)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/darius-garland-drops-24-points-10-assists-sunday)
  - [NBC Sports / Rotoworld, 8 Nov (Markkanen)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/lauri-markkanen-wrist-out-sunday-vs-min)
  - [SI Pistons On SI, 8 Nov](https://www.si.com/nba/pistons/onsi/3-takeaways-from-pistons-stunning-loss-to-luka-less-lakers-01m6yze5022p)
  - [NBC Sports / Rotoworld, 8 Nov (Murphy)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/trey-murphy-hits-four-triples-scores-26-points)
  - [NBC Sports / Rotoworld, 8 Nov (Jamal Murray)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets)
  - [Chicago Sun-Times, 4 Nov (Wilson)](https://chicago.suntimes.com/bulls/2026/11/04/bulls-embarrassed-new-york-rookie-caleb-wilson-soft-benching)
  - [NBC Sports / Rotoworld, 8 Nov (Wilson)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/caleb-wilson-finishes-loss-with-18-points)
  - [NBC Sports / Rotoworld, 8 Nov (Cunningham)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/cade-cunningham-held-to-14-points-against-lakers)
  - [SI Pelicans On SI, 8 Nov](https://www.si.com/nba/pelicans/onsi/grading-every-pelicans-player-after-loss-vs-clippers)
  - [RotoWire, 4 Nov (Dejounte Murray)](https://www.rotowire.com/basketball/headlines/dejounte-murray-news-removed-from-injury-report-537484)
  - [Yahoo Sports / HoopsHype, 8 Nov (Miller)](https://sports.yahoo.com/articles/lastly-brandon-miller-diagnosed-223257025.html)
  - [NBC Sports / Rotoworld, 8 Nov (Allen)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jarrett-allen-knee-questionable-monday-vs-cha)
  - [NBC Sports / Rotoworld, 8 Nov (Embiid)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/joel-embiid-records-18-10-5-2-line-vs-chicago)
- News carried over from last night's report (and earlier Slump, Injury and News Watch reports):
  - [NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)
  - [NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)
  - [Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)
  - [CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/)
  - [RotoWire, 4 Nov (Zubac)](https://www.rotowire.com/basketball/headlines/ivica-zubac-news-returning-versus-memphis-537562)
  - [CBS Sports / RotoWire, 8 Nov (Zubac)](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-double-doubles-despite-loss/)
  - [CBS Sports / RotoWire, 8 Nov (Harden)](https://www.cbssports.com/fantasy/basketball/news/cavaliers-james-harden-struggles-in-loss/)
  - [NBC Sports / Rotoworld, 8 Nov (Duren)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work)
  - [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)
  - [Raptors Republic, 3 Nov](https://raptorsrepublic.com/2026/11/03/raptors-announce-update-on-kawhi-leonards-health/)
  - [CBS Sports / RotoWire, 3 Nov (Leonard)](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)
  - [CBS Sports / RotoWire, 8 Nov (Barnes)](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/)
  - [NBC Sports / Rotoworld, 8 Nov (Black)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)
  - [Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)
  - [Yahoo Sports / USA Today, 7 Nov](https://sports.yahoo.com/articles/brandon-ingram-pretty-close-making-014045418.html)
  - [Heavy, 7 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/jarrett-allen-injury-knicks/)
  - [CBS Sports / RotoWire, 8 Nov (Young)](https://www.cbssports.com/fantasy/basketball/news/wizards-trae-young-shooting-woes-in-blowout-loss/)
  - [Philadelphia Inquirer, 3 Nov](https://www.inquirer.com/sixers/joel-embiid-philadelphia-76ers-plantar-fasciitis-nick-nurse-injuries-20261103.html)
  - [NBC Sports / Rotoworld, 7 Nov (Sabonis)](https://nbcsports.com/fantasy/basketball/player-news/2026-11-07/domantas-sabonis-with-17-12-in-loss-to-the-spurs)
- ESPN box scores:
  - 8 Nov: [PHI at CHI](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909945), [LAL at DET](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909946), [UTAH at MIN](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909947), [NO at LAC](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909950)
  - 7 Nov: [DEN vs IND](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909938), [NY at CLE](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940), [HOU at PHX](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943), [SA at POR](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909944), [ORL at GS](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909942)
  - 6 Nov: [WSH at ATL](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909287), [BOS at CHA](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909288), [PHI at CLE](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289), [OKC at MEM](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909291), [MIN at NO](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909293), [SA at SAC](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909295)
  - 5 Nov: [MIA at GS](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909937)
  - 4 Nov: [PHI at DET](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909922), [CHI at NY](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909926), [UTAH at NO](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909928), [MIN at HOU](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909930)
  - 2 Nov: [PHX at GS](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909919)
