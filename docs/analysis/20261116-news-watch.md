# News watch: 15 Nov 2026

- Generated 2026-11-16 04:42 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 53 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 39 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

**Our players:**
- Missi was added for Gafford.
- Bey keeps the start while Murphy is out ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)).
- Jenkins keeps starting, picked game by game, until Duren returns.
- Paul George is a rest risk on 16 and 22 Nov.
- **Trey Murphy III:** out 16 Nov vs GS, his fifth straight game (bilateral patellar tendinopathy); next chance 18 Nov vs DET ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)). No timetable reported; *ESPN est.* 18 Nov.
- **Jalen Smith:** questionable 16 Nov vs CLE with a left finger sprain after missing 14 Nov ([NBC Sports, 15 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-15/jalen-smith-finger-questionable-vs-cleveland)). No timetable reported; *ESPN est.* 16 Nov.
- **Scottie Barnes:** back on 15 Nov with 30 pts in an overtime loss to NY ([NBC Sports, 15 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-15/scottie-barnes-scores-game-high-30-in-ot-defeat)). Healthy.
- **Kawhi Leonard:** out at least another week from 10 Nov, not yet on court; update about 17 Nov ([Yahoo, 11 Nov](https://sports.yahoo.com/articles/kawhi-leonards-knee-keeps-raptors-200300316.html)). *ESPN est.* 23 Nov.
- **Fred VanVleet (Snow Time Lakers):** sat 15 Nov (the first night, right knee management), next chance 16 Nov at MIA ([RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/fred-vanvleet-injury-ruled-out-for-sunday-539130)); no other HOU back-to-back this week. **Override removed:** the "sits 16 Nov" row was wrong.

**Snow Time Lakers:**
- Kyrie is back 18 Nov; 22 Nov (the second night) is at risk.
- Herro's L7 dip is one 2-of-13 game.
- Avdija is carrying Portland's offence.
- VanVleet sat 15 Nov, not 16.

**Overrides:**
- Added: Duren return 23 Nov, Pippen Jr. return 22 Nov, Dejounte Murray return 23 Nov (all floors).
- Removed: Murphy sit 13 Nov (expired), VanVleet sit 16 Nov (wrong night).
- Raynaud's floor (16 Nov) and Claxton's role (to 16 Nov) end today.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline) | in force |
| Nic Claxton | role | 18 | 2026-11-16 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Trey Murphy III | sit | 2026-11-13 | — | [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-friday-538912/) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Daniss Jenkins** | DET | us | role, minutes | 34.4 | 38.6 | active |
| **Saddiq Bey** | NO | us | role, minutes | 30.6 | 34.3 | active |
| **Yves Missi** | NO | us | minutes | 32.0 † | — | active |
| **Paul George** | BOS | us | rest | 41.0 | — | active |
| **Jalen Duren** | DET | us | gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Norman Powell** | CHI | free agent | injury, minutes, rest | 38.2 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury, gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Jalen Suggs** | ORL | free agent | injury | 27.7 | — | active |
| **Jerami Grant** | MEM | free agent | injury, rest | 26.6 | — | active |
| **Dejounte Murray** | NO | free agent | injury, minutes | 22.7 | 24.0 | out, ESPN est. 20 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury | 16.3 | — | out, ESPN est. 21 Nov |
| **Grayson Allen** | CHA | free agent | role | 31.5 | 29.7 | active |
| **Aday Mara** | OKC | free agent | role | 30.2 | 32.2 | active |
| **Mo Bamba** | UTAH | free agent | role | 29.1 | 54.1 | active |
| **Tyrese Proctor** | CLE | free agent | role, minutes | 28.7 | 33.8 | active |
| **Meleek Thomas** | CLE | free agent | role | 27.9 | 30.2 | active |
| **Isaiah Stewart** | MEM | free agent | role | 21.2 | 23.1 | day-to-day, ESPN est. 16 Nov |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 20.5 | 25.8 | day-to-day, ESPN est. 16 Nov |
| **Kevin Huerter** | DET | free agent | minutes | 32.0 | 31.6 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 29.6 | 26.1 | out, ESPN est. 13 Dec |
| **Toumani Camara** | POR | free agent | minutes | 27.1 | 30.9 | active |
| **Collin Murray-Boyles** | TOR | free agent | minutes | 26.8 | 31.5 | active |
| **Bones Hyland** | MIN | free agent | minutes | 26.1 | 29.5 | active |
| **Rudy Gobert** | MIN | free agent | rest | 27.8 | — | active |
| **Myles Turner** | MIL | free agent | rest | 26.2 | — | active |
| **Zach Edey** | MEM | free agent | rest | 20.3 | — | day-to-day, ESPN est. 16 Nov |
| **Kyrie Irving** | DAL | Snow Time Lakers | injury | 42.3 | — | out, ESPN est. 18 Nov |
| **Cam Spencer** | MEM | Lauri Birds | role, minutes | 28.9 | 38.3 | active |
| **Jaime Jaquez Jr.** | MIL | Lauri Birds | role | 28.2 | 29.8 | active |
| **Deni Avdija** | POR | Snow Time Lakers | rest | 48.0 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 38.4 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 32.6 | — | active |
| **Ajay Mitchell** | OKC | Lauri Birds | rest | 31.1 | — | active |
| **Ivica Zubac** | IND | Lauri Birds | rest | 29.9 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 60.9 † | — | out, ESPN est. 22 Nov |
| **Donovan Mitchell** | CLE | Dr White Slong | injury | 39.9 | — | active |
| **James Harden** | CLE | Team Nic Kerr | injury | 37.2 | — | active |
| **Jarrett Allen** | CLE | Dr White Slong | injury | 36.7 | — | active |
| **Michael Porter Jr.** | BKN | Team Nic Kerr | injury | 36.0 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Daniss Jenkins (DET, PG, us)

- Rate **34.4** · role rate 38.6 · season 28.7 (12) · L7 44.5 (4) · L15 32.3 (6) · L30 28.7 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 10 before; 37.8 min in his starts, against 28.0 for the season
- **Minutes:** 37.7 min over his last 3 games against 28.0 for the season (+9.7)
- News (12 Nov): Jenkins had 21 points (6-11 FG, 3-5 3Pt, 6-6 FT), six rebounds and two steals in 42 minutes before fouling out of Thursday's 144-140 double-overtime victory over Washington.
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- **Research:**
  - Started again 14 Nov at MIA ([ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909982)); the fifth starter is picked game by game until Duren returns ([Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html)). About 35 min a game. Duncan Robinson (left thigh soreness; no timetable reported; ESPN est. 17 Nov) is "not a lock" for 17 Nov ([Detroit Sports Nation, 14 Nov](https://detroitsportsnation.com/duncan-robinson-injury-update-pistons-heat/ddrysdale/detroit-pistons/11/14/2026/507834)); Isaiah Joe is still out.
  - Verdict: *ESPN confirmed*. No row: the start is game by game.

### Saddiq Bey (NO, SF/PF, us)

- Rate **30.6** · role rate 34.3 · season 29.4 (14) · L7 29.2 (5) · L15 33.3 (9) · L30 29.4 (14) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 12 before; 33.3 min in his starts, against 28.4 for the season
- **Role:** news on 13 Nov: "Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports."
- **Minutes:** 35.0 min over his last 3 games against 28.4 for the season (+6.6)
- News (13 Nov): Bey notched 30 points (11-20 FG, 6-9 3Pt, 2-3 FT), 10 rebounds and one block across 35 minutes in Friday's 142-111 loss to the Grizzlies.
- News (13 Nov): Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports.
- **Research:**
  - "Expected to keep his starting role for as long as Murphy is sidelined" ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)); started 13 and 14 Nov with Zion playing ([NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/nor-starting-fears-herb-bey-zion-missi)). Mathurin is out 16 Nov too ([CBS, 15 Nov](https://cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-out-again-vs-warriors)).
  - Verdict: *ESPN confirmed*. No row: no source states his minutes.

### Yves Missi (NO, C, us)

- Rate **32.0** (small sample) · season 36.0 (3) → 46.5 (2) · L7 25.0 (1) · L15 25.0 (1) · L30 36.0 (3) → 46.5 (2) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:**
  - Returned 14 Nov, started, 22 min on a restriction ([NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/yves-missi-logs-22-minutes-in-return-to-lineup)); playing time expected to rise "over the next few games" ([RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-blocks-four-shots-in-return-539214)). Small sample (2 games).
  - Verdict: *nothing new found*. No row.

### Paul George (BOS, SF/PF, us)

- Rate **41.0** · season 41.3 (11) · L7 42.7 (3) · L15 39.7 (6) · L30 41.3 (11) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov, Sat 21–Sun 22 Nov; news on 11 Nov: "George will sit out the second leg of this back-to-back set due to an illness, and his next opportunity to play will come Sunday against the Mavericks."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- **Research:**
  - Played 25 min in the 131–94 rout of DAL on 15 Nov ([CelticsBlog, 15 Nov](https://celticsblog.com/celtics-highlights/150272/celtics-mavericks)); nothing said about 16 Nov (the second night); he sat the second night on 2 Nov ([RotoBaller, 2 Nov](https://www.rotoballer.com/?p=1982197)).
  - Verdict: *nothing new found*; a rest risk, not announced.

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - Nothing new since the 8 Nov update: on-court work, re-evaluated in two weeks ([Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)).
  - Verdict: *ESPN corrected* by a day (est. 24 Nov). Override: return 23 Nov (a floor).

## Free agents and waivers

### Norman Powell (CHI, SG/SF, free agent)

- Rate **38.2** · season 30.0 (10) → 32.9 (9) · L7 45.0 (2) · L15 29.2 (4) → 37.7 (3) · L30 30.0 (10) → 32.9 (9) · projected 36.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Powell (back) is listed as questionable for Saturday's game against Minnesota."
- **Minutes:** news on 13 Nov: "Powell led all scorers with 33 points in his return to action, showing no signs of limitations after being cleared to play without a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 14 Nov: "Powell was questionable to play Saturday due to lower-back injury management, but he'll fight through it and suit up for the second leg of Chicago's back-to-back set."
- News (14 Nov): Powell finished with 23 points (10-19 FG, 3-5 3Pt), five rebounds, three assists, a steal and two blocks across 30 minutes in Saturday's 117-106 victory over the Timberwolves.
- News (14 Nov): Powell (back) is available for Saturday's game against the Timberwolves, K.C. Johnson of Chicago Sports Network reports.
- **Research:**
  - Back from back spasms on 13 Nov with no minutes limit ([CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-will-play-saturday/)); questionable for back management on 14 Nov but played ([NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/norman-powell-back-available-vs-minnesota)); 31 and 30 min. With Caleb Wilson out, Chicago's scoring "falls entirely on Norman Powell" ([Yahoo](https://sports.yahoo.com/articles/bulls-injury-report-first-game-181313737.html)). No rest statement; CHI's back-to-back is 22–23 Nov.
  - Verdict: *ESPN confirmed* (active).

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Injury:** ESPN est. 20 Nov (Out, Right Foot Strain, updated 06 Nov), but the news said on 06 Nov: "He will be re-evaluated in two weeks, the Jazz announced Friday."
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:**
  - Still out 15 Nov, no timeline ([SI, 15 Nov](https://www.si.com/nba/jazz/onsi/jazz-vs-spurs-injury-report-reveals-major-problem-for-utah-rotation)); re-evaluation about 20 Nov ([Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)). Jaxson Hayes is also out (left knee strain).
  - Verdict: *ESPN corrected* by a day; the 21 Nov floor stands.

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **27.7** · season 20.8 (4) → 26.3 (3) · L7 4.0 (1) → — · L15 4.0 (1) → — · L30 20.8 (4) → 26.3 (3) · projected 29.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 13 Nov: "Suggs (knee) participated in the Magic's morning shootaround and remains questionable for Friday's game against the Bucks, Jason Beede of the Orlando Sentinel reports."
- News (13 Nov): Suggs notched three points (1-8 FG, 1-6 3Pt), two rebounds and three assists across 21 minutes during Friday's 107-99 win over the Bucks.
- News (13 Nov): Suggs (knee) will come off the bench Friday against the Bucks.
- **Research:**
  - Returned 13 Nov, 21 min off the bench ([RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/jalen-suggs-news-logs-21-minutes-in-return-538990)); Sweeney is managing his minutes and wants him to "keep ramping up" ([ClutchPoints, 14 Nov](https://clutchpoints.com/nba/orlando-magic/magic-news-sean-sweeney-jalen-suggs-return-injury-bucks)).
  - Verdict: *ESPN confirmed* (active). No row: no minutes target reported.

### Jerami Grant (MEM, PF, free agent)

- Rate **26.6** · season 21.8 (12) → 23.6 (11) · L7 31.0 (3) · L15 24.4 (7) · L30 21.8 (12) → 23.6 (11) · projected 27.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Grant (head) is out for Saturday's game against the Nets."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Grant will miss the second leg of Memphis' back-to-back set due to a head injury."
- News (15 Nov): Grant (head) is off the injury report ahead of Monday's game against the Wizards.
- News (14 Nov): Grant (head) is out for Saturday's game against the Nets.
- **Research:**
  - Head injury kept him out 14 Nov; off the report for 16 Nov at WSH ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/jerami-grant-head-removed-from-injury-report)); 22.8 min off the bench over his last five.
  - Verdict: *ESPN confirmed*.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.7** · role rate 24.0 · season 30.6 (9) · L7 13.7 (3) · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 20 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 20 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - No trade yet ([Hoops Rumors](https://www.hoopsrumors.com/transactions)); sitting until traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html); [NBA.com, 14 Nov](https://www.nba.com/news/dejounte-murray-requests-trade-pelicans-confirm)); out again 16 Nov.
  - Verdict: *ESPN corrected* (est. 20 Nov assumes only the ankle). Override: return 23 Nov (a floor; remove if traded).

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **16.3** · season 14.2 (5) · L7 — · L15 — · L30 14.2 (5) · projected 30.6
- ESPN: out, ESPN est. 21 Nov (Back Soreness, updated 2026-11-10)
- **Injury:** ESPN est. 21 Nov (Out, Back Soreness, updated 10 Nov), but the news said on 10 Nov: "He has now been sidelined for six straight contests due to the back issue and can be considered week-to-week until Memphis offers an update on his recovery."
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- News (08 Nov): Pippen (back) won't play in Monday's game versus the Raptors.
- **Research:**
  - Lumbar disc herniation (3 Nov), "day-to-day or week-to-week" (Iisalo, [NBC Sports, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/iisalo-pippen-back-day-to-day-or-week-to-week)); still out 16 Nov on the Grizzlies' 15 Nov report ([Yahoo, 15 Nov](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html)).
  - Verdict: *ESPN corrected* (est. 21 Nov). Override: return 22 Nov (a floor).

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **31.5** · role rate 29.7 · season 26.8 (13) · L7 36.0 (3) · L15 31.7 (7) · L30 26.8 (13) · projected 26.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (15 Nov): Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports.
- News (13 Nov): Allen logged 14 points (5-11 FG, 4-8 3Pt), four rebounds, six assists and one steal over 34 minutes during Thursday's 101-96 loss to Phoenix.
- **Research:**
  - Back to the bench on 15 Nov when Brandon Miller was cleared; still 25 min ([RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/grayson-allen-news-not-starting-sunday-539277); [Heavy, 15 Nov](https://heavy.com/sports/hornets-brandon-miller-cleared-return-clippers/)). Knueppel re-evaluated in four weeks (ESPN est. 12 Dec); Schröder no timetable reported (ESPN est. 25 Nov). Only 2 games this week (17, 20 Nov).
  - Verdict: *ESPN confirmed*; his starts were injury cover.

### Aday Mara (OKC, C, free agent)

- Rate **30.2** · role rate 32.2 · season 26.6 (14) · L7 32.0 (4) · L15 32.3 (9) · L30 26.6 (14)
- ESPN: active
- **Role:** started 1 of his last 2 games after 3 of 12 before; 26.2 min in his starts, against 21.6 for the season
- **Role:** news on 11 Nov: "Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports."
- News (15 Nov): Mara will come off the bench during Sunday's game against the Kings, Sean Cunningham of Fox 40 Sacramento reports.
- News (14 Nov): Mara amassed 10 points (5-6 FG), three rebounds and three blocks across 21 minutes during Friday's 113-112 loss to the Clippers.
- **Research:**
  - Back on the bench since Ajay Mitchell returned, still 26 min, 16 pts, 13 reb on 15 Nov ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-back-to-bench/); [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/okc-starts-sga-mccain-mitchell-kenrich-ihart)). Holmgren out 8–10 weeks (ESPN est. 2 Jan); Jaylin Williams missed a seventh straight, no timetable reported (ESPN est. 18 Nov).
  - Verdict: *ESPN confirmed*; 21–32 min off the bench.

### Mo Bamba (UTAH, C, free agent)

- Rate **29.1** · role rate 54.1 · season 29.6 (10) · L7 32.0 (5) · L15 28.9 (8) · L30 29.6 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 8 before; 36.0 min in his starts, against 19.7 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- News (15 Nov): Bamba will start in Sunday's game against San Antonio.
- **Research:**
  - Started 15 Nov (35 min, 61 FP, one game) with Jaxson Hayes out (left knee strain; no timetable reported; ESPN est. 17 Nov) ([CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-jaxson-hayes-ruled-out-for-sunday/); [SI, 15 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-provide-more-clarity-on-jaxson-hayes-latest-injury)). His role rate rests on one game, a small sample.
  - Verdict: *ESPN confirmed*; the role lasts only while Hayes is out.

### Tyrese Proctor (CLE, SG, free agent)

- Rate **28.7** · role rate 33.8 · season 22.9 (13) · L7 38.5 (4) · L15 28.3 (9) · L30 22.9 (13)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 11 before; 28.0 min in his starts, against 19.2 for the season
- **Role:** news on 14 Nov: "Proctor will start in Saturday's game versus the Mavericks."
- **Minutes:** 28.0 min over his last 3 games against 19.2 for the season (+8.8)
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- News (14 Nov): Proctor will start in Saturday's game versus the Mavericks.
- **Research:**
  - His 14 Nov start was a one-off: Cleveland rested its starters after a delayed flight ([107.5 The Game, 14 Nov](https://www.1075thegame.com/2026/11/14/tyrese-proctor-has-first-triple-double-as-cavs-rest-starters-top-mavs/)); the starters are off Monday's report ([Heavy, 15 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/cavaliers-hit-with-brutal-injury-news-ahead-of-bulls-game/)). Mobley, Merrill and Watson are out or questionable, so 20–27 min off the bench.
  - Verdict: *ESPN confirmed*.

### Meleek Thomas (CLE, SG, free agent)

- Rate **27.9** · role rate 30.2 · season 25.3 (11) · L7 32.2 (4) · L15 25.7 (9) · L30 25.3 (11)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 9 before; 28.0 min in his starts, against 23.5 for the season
- **Role:** news on 14 Nov: "Thomas will start in Saturday's game against Dallas."
- News (14 Nov): Thomas will start in Saturday's game against Dallas.
- News (09 Nov): Thomas tallied 18 points (7-12 FG, 4-6 3Pt), three rebounds, three assists, two steals and two blocks across 27 minutes in Monday's 124-112 loss to the Hornets.
- **Research:**
  - Same one-off rest-night start on 14 Nov ([107.5 The Game, 14 Nov](https://www.1075thegame.com/2026/11/14/tyrese-proctor-has-first-triple-double-as-cavs-rest-starters-top-mavs/)); more minutes while Mobley is out ([Heavy, 15 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/cavaliers-hit-with-brutal-injury-news-ahead-of-bulls-game/)).
  - Verdict: *ESPN confirmed*.

### Isaiah Stewart (MEM, PF/C, free agent)

- Rate **21.2** · role rate 23.1 · season 21.6 (10) · L7 18.7 (3) · L15 22.8 (6) · L30 21.6 (10) · projected 25.3
- ESPN: day-to-day, ESPN est. 16 Nov (Illness, updated 2026-11-15)
- **Role:** started 2 of his last 2 games after 1 of 8 before; 19.0 min in his starts, against 18.1 for the season
- **Role:** news on 13 Nov: "Stewart will start Friday's game against the Pelicans."
- News (15 Nov): Stewart is questionable for Monday's game against the Wizards due to an illness.
- News (14 Nov): Stewart chipped in 12 points (5-7 FG, 0-2 3Pt, 2-2 FT), five rebounds and four blocks across 20 minutes during Friday's 142-111 win over the Pelicans.
- **Research:**
  - Started 13 and 14 Nov for Zach Edey; Edey is questionable 16 Nov ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/zach-edey-ankle-questionable-monday-vs-wizards)); Stewart is questionable too, with an illness ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/isaiah-stewart-illness-questionable-monday)).
  - Verdict: *ESPN confirmed*; day-to-day cover.

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **20.5** · role rate 25.8 · season 19.2 (8) · L7 20.3 (3) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: day-to-day, ESPN est. 16 Nov (Right Ankle, updated 2026-11-15)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Role:** news on 13 Nov: "Tyson will start Friday's game against Miami, Serena Winters of FanDuel Sports Network Ohio reports."
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (15 Nov): Tyson (ankle) is questionable for Monday's game against the Bulls.
- News (14 Nov): Tyson closed with 16 points (6-11 FG, 4-7 3Pt), three rebounds, one assist and one steal over 30 minutes during Friday's 133-121 loss to Miami.
- **Research:**
  - Started 13 and 14 Nov for Mobley, who is out again 16 Nov ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-evan-mobley-ruled-out-for-monday/)); Tyson is questionable 16 Nov with right ankle management ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-questionable-for-monday/)).
  - Verdict: *ESPN confirmed*.

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **32.0** · role rate 31.6 · season 24.2 (12) · L7 40.2 (4) · L15 33.5 (6) · L30 24.2 (12) · projected 22.9
- ESPN: active
- **Minutes:** 31.7 min over his last 3 games against 24.4 for the season (+7.2)
- News (14 Nov): Huerter posted 20 points (9-15 FG, 2-6 3Pt), four rebounds, seven assists, a steal and three blocks across 38 minutes in Saturday's 137-117 loss to Miami.
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- **Research:**
  - 38 min, 20 pts on 14 Nov after Duncan Robinson left; he "would start" if Robinson misses time ([NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/kevin-huerter-puts-up-20-4-7-1-3-line-off-bench)). Robinson: "It was a quad", no timetable reported ([Heavy, 15 Nov](https://heavy.com/sports/nba/detroit-pistons/duncan-robinson-injury-addressed-miami-heat-loss/)); ESPN est. 17 Nov. His L7 is 16.0 over on 32.5 min against 24.4.
  - Verdict: *ESPN confirmed*; the minutes last while Joe and Robinson are out.

### Caleb Wilson (CHI, SF, free agent)

- Rate **29.6** · role rate 26.1 · season 34.9 (10) · L7 25.0 (2) · L15 27.2 (4) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Surgery 12 Nov, re-evaluated in three weeks, about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)); 4–6 weeks per Charania.
  - Verdict: *ESPN confirmed* (est. 13 Dec).

### Toumani Camara (POR, SF/PF, free agent)

- Rate **27.1** · role rate 30.9 · season 25.8 (12) · L7 31.7 (3) · L15 22.6 (8) · L30 25.8 (12) · projected 23.8
- ESPN: active
- **Minutes:** 34.7 min over his last 3 games against 29.1 for the season (+5.6)
- News (14 Nov): Camara contributed 14 points (5-7 FG, 2-4 3Pt, 2-2 FT), two rebounds, one assist, one block and two steals across 36 minutes during Friday's 120-107 victory over Sacramento.
- News (07 Nov): Camara accumulated 18 points (7-12 FG, 4-8 3Pt), six rebounds and one assist in 30 minutes during Friday's 124-118 loss to the Lakers.
- **Research:**
  - 30, 38 and 36 min in his last three; "with Portland down two key guards, his minutes should stay high" ([CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-toumani-camara-posts-14-points-in-decisive-win/)). Morant re-evaluated about 27 Nov ([NBA.com, 30 Oct](https://www.nba.com/news/ja-morant-hamstring-injury-october-2026)); Nori may manage players across 16–17 Nov ([SI](https://www.si.com/nba/trailblazers/onsi/4-blazers-ruled-out-vs-wolves-means-depth-chart-will-be-tested)).
  - Verdict: *ESPN confirmed*.

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **26.8** · role rate 31.5 · season 25.2 (12) · L7 27.3 (3) · L15 28.4 (7) · L30 25.2 (12) · projected 24.8
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 24.3 for the season (+6.3)
- News (12 Nov): Murray-Boyles ended with 14 points (5-9 FG, 1-1 3Pt, 3-4 FT), four assists, five blocks and one steal over 32 minutes during Thursday's 123-112 loss to the 76ers.
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- **Research:**
  - Started again on 15 Nov with Barnes back, Poeltl to the bench ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/tor-starts-quickley-walter-barrett-barnes-cmb)); 40 min in overtime ([ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909990)).
  - Verdict: *nothing new found*; one game with Barnes, no reason given.

### Bones Hyland (MIN, PG, free agent)

- Rate **26.1** · role rate 29.5 · season 21.4 (13) · L7 32.7 (3) · L15 25.9 (7) · L30 21.4 (13) · projected 17.1
- ESPN: active
- **Minutes:** 19.0 min over his last 3 games against 13.8 for the season (+5.2)
- News (13 Nov): Hyland produced 24 points (7-10 FG, 5-6 3Pt, 5-6 FT), three rebounds, eight assists and two steals across 23 minutes during Thursday's 133-94 victory over Dallas.
- News (09 Nov): Hyland notched 14 points (4-8 FG, 1-5 3Pt, 5-6 FT), two rebounds, two assists and one block across 13 minutes in Sunday's 115-100 win over the Jazz.
- **Research:**
  - 13, 23 and 21 min in his last three against 13.8 for the season: Jaylen Clark (hamstring) is out at least two to three weeks, re-evaluated 29 Nov ([Yahoo, 15 Nov](https://sports.yahoo.com/articles/timberwolves-lose-jaylen-clark-least-235639664.html); [CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-jaylen-clark-wont-return-saturday/)). Edwards out until late December.
  - Verdict: *ESPN confirmed*; the bump should last the week.

### Rudy Gobert (MIN, C, free agent)

- Rate **27.8** · season 26.4 (12) · L7 26.0 (3) · L15 29.0 (6) · L30 26.4 (12) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:**
  - His 31 Oct absence was back spasms ([NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday)); he played both nights of 25–26 Oct; not on the 16 Nov report.
  - Verdict: *nothing new found*; expect him 16 and 17 Nov.

### Myles Turner (MIL, C, free agent)

- Rate **26.2** · season 26.5 (13) · L7 23.0 (4) · L15 29.2 (8) · L30 26.5 (13) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 12 Nov: "Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando."; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): Turner recorded 14 points (5-9 FG, 4-7 3Pt), 11 rebounds, three assists and two steals across 31 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando.
- **Research:**
  - His only rest was the second night of 10–11 Nov ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/myles-turner-rest-ruled-out-vs-los-angeles)); he played both nights of 23–24 Oct. MIL's back-to-back this week is 18–19 Nov.
  - Verdict: *nothing new found*; 19 Nov is a risk, not announced.

### Zach Edey (MEM, C, free agent)

- Rate **20.3** · season 22.8 (10) · L7 14.0 (2) · L15 20.2 (6) · L30 22.8 (10) · projected 33.2
- ESPN: day-to-day, ESPN est. 16 Nov (Left Ankle, updated 2026-11-15)
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Edey sat out Memphis' game Friday due to an ankle injury, and he is now at risk of missing both legs of this back-to-back set."; sat the first night of the 25–26 Oct back-to-back, playing the games either side
- News (15 Nov): Edey (ankle) is questionable for Monday's game against Washington.
- News (14 Nov): Edey (ankle) is listed as out for Saturday's game against the Nets.
- **Research:**
  - Questionable 16 Nov at WSH, "left ankle return from injury management" ([Yahoo, 15 Nov](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html)); "Zach Edey doesn't play back to backs at this point" (Rotoworld via [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/zach-edey-ankle-questionable-monday-vs-wizards)). MEM's back-to-back is 18–19 Nov. L7 14.0 (2) is a small sample.
  - Verdict: *ESPN confirmed* (est. 16 Nov); expect him to sit one of 18–19 Nov, night not named.

## Opponents: this week and next

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **42.3** · season 41.5 (11) · L7 44.0 (4) · L15 40.8 (6) · L30 41.5 (11) · projected 44.2
- ESPN: out, ESPN est. 18 Nov (Left Knee, updated 2026-11-15)
- **Injury:** ESPN est. 18 Nov (Out, Left Knee, updated 15 Nov), but the news said on 14 Nov: "The 34-year-old veteran had a slow start to the 2026-27 campaign after missing last season while recovering from knee surgery."
- News (15 Nov): Irving (knee) has been ruled out for Sunday's game against the Celtics.
- News (15 Nov): Irving (knee) is questionable to play in Sunday's game against the Celtics.
- **Research:**
  - Out 15 Nov (second night) with left knee injury management after 37 min on 14 Nov ([Dallas Sports Journal, 15 Nov](https://dallassportsjournal.com/kyrie-irving-max-christie-out-mavericks-celtics/); [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kyrie-irving-knee-downgraded-to-out-sunday)); DAL next plays 18 Nov. He sat the second night of 2 of 3 back-to-backs; this week's is 21–22 Nov, so 22 Nov is at risk (May: "let's not make any decisions in advance", [Yardbarker, 24 Oct](https://www.yardbarker.com/nba/articles/dusty_may_addresses_kyrie_irving_playing_both_nights_of_mavericks_back_to_backs/s1_17810_44470036)).
  - Verdict: *ESPN confirmed* (est. 18 Nov).

### Cam Spencer (MEM, PG/SG, Lauri Birds)

- Rate **28.9** · role rate 38.3 · season 27.5 (13) · L7 29.5 (4) · L15 30.0 (8) · L30 27.5 (13)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 11 before; 29.5 min in his starts, against 20.9 for the season
- **Role:** news on 14 Nov: "Spencer will start in Saturday's game against the Nets."
- **Minutes:** 26.0 min over his last 3 games against 20.9 for the season (+5.1)
- News (14 Nov): Spencer finished with 17 points (6-10 FG, 3-3 3Pt, 2-2 FT), one rebound, eight assists and two steals across 34 minutes in Saturday's 129-110 win over the Nets.
- News (14 Nov): Spencer will start in Saturday's game against the Nets.
- **Research:**
  - Started for Ty Jerome (hip; out 16 Nov, next chance 18 Nov; [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ty-jerome-hip-remains-out-monday-vs-washington)), 34 min ([NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/cam-spencer-starting-in-place-of-ty-jerome)).
  - Verdict: *nothing new found*.

### Jaime Jaquez Jr. (MIL, SG/SF, Lauri Birds)

- Rate **28.2** · role rate 29.8 · season 28.7 (14) · L7 27.8 (5) · L15 27.3 (9) · L30 28.7 (14) · projected 28.2
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 11 of 12; 29.0 min in those 2, against 27.9 for the season
- News (13 Nov): Jaquez chipped in 22 points (8-15 FG, 5-7 3Pt, 1-3 FT), six rebounds and four assists in 28 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Jaquez registered 25 points (7-16 FG, 2-7 3Pt, 9-9 FT), five rebounds, three assists and two steals across 30 minutes during Wednesday's 123-112 loss to the Lakers.
- **Research:**
  - Off the bench amid the Bucks' lineup changes; minutes held at 28–30 ([NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/mil-starts-burries-herro-dieng-kuzma-turner)).
  - Verdict: *nothing new found*.

### Deni Avdija (POR, SF/PF, Snow Time Lakers)

- Rate **48.0** · season 42.8 (12) → 45.2 (11) · L7 54.0 (3) · L15 41.8 (8) → 45.3 (7) · L30 42.8 (12) → 45.2 (11) · projected 40.4
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 14 Nov: "They'll need more of the same in back-to-back games at Minnesota on Monday and Tuesday."
- News (14 Nov): Avdija finished Friday's 120-107 win over the Kings with 34 points (11-13 FG, 3-5 3Pt, 9-9 FT), six rebounds, four assists and one block across 35 minutes.
- News (12 Nov): Avdija tallied 28 points (9-20 FG, 4-13 3Pt, 6-6 FT), three rebounds, six assists, four steals and two blocks across 35 minutes in Wednesday's 118-108 win over the Thunder.
- **Research:**
  - Played both nights of all three POR back-to-backs; not on the 16 Nov report. His L7 54.0 (3) is about 9 over: he carries the offence with Morant and Sharpe out ([Sports Mole, 15 Nov](https://www.sportsmole.co.uk/basketball/portland-trail-blazers/preview/trail-blazers-vs-timberwolves-player-props-injury-report-and-prediction--nba_609140.html)).
  - Verdict: *nothing new found*.

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **38.4** · season 39.1 (13) · L7 35.2 (4) · L15 39.9 (8) · L30 39.1 (13) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (15 Nov): Brown tallied 31 points (12-18 FG, 3-6 3Pt, 4-6 FT), two rebounds, two assists and one steal across 32 minutes during Sunday's 131-124 win over Indiana.
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- **Research:**
  - His 30 Oct absence was patellar tendinopathy, not rest; he played both nights of 24–25 Oct and 32 min on 15 Nov ([NBC Sports](https://www.nbcsports.com/nba/jaylen-brown/10472/news)). PHI's report for 16 Nov was not yet filed.
  - Verdict: *nothing new found*.

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **32.6** · season 33.7 (13) → 36.2 (12) · L7 21.8 (4) → 28.0 (3) · L15 29.2 (8) → 33.0 (7) · L30 33.7 (13) → 36.2 (12) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (13 Nov): Herro had 18 points (5-17 FG, 2-7 3Pt, 6-7 FT), two assists, two steals, one rebound and one block across 34 minutes in Friday's 107-99 loss to the Magic.
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- **Research:**
  - No rest pattern: the 10 Nov absence was a knee contusion; he played both nights of 23–24 Oct. His L7 21.8 (4) → 28.0 (3) is more than 5 under: 2-of-13 in 20 min on 15 Nov during Taylor Jenkins' lineup experiments ([Journal Sentinel via Yahoo, 16 Nov](https://sports.yahoo.com/articles/bucks-coach-taylor-jenkins-tinkers-035758071.html)); no injury reported.
  - Verdict: *nothing new found*.

### Ajay Mitchell (OKC, PG/SG, Lauri Birds)

- Rate **31.1** · season 33.7 (12) · L7 29.5 (2) · L15 30.6 (7) · L30 33.7 (12) · projected 32.8
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 11 Nov: "Mitchell won't play in the second leg of the Thunder's back-to-back set after apparently injuring his ankle Tuesday."
- News (15 Nov): Mitchell (ankle) is available for Sunday's game against the Kings, Clemente Almanza of USA Today reports.
- News (14 Nov): Mitchell (ankle) is questionable to suit up for Sunday's game against the Kings.
- **Research:**
  - Returned 15 Nov from the ankle sprain, 27 min ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ajay-mitchell-ankle-scores-14-points-in-return)).
  - Verdict: *nothing new found*.

### Ivica Zubac (IND, C, Lauri Birds)

- Rate **29.9** · season 26.7 (9) → 29.2 (8) · L7 31.2 (4) · L15 27.3 (6) · L30 26.7 (9) → 29.2 (8) · projected 35.5
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 13 Nov: "That's now back-to-back double-doubles for Zubac, who appears to be just about all the way back from a recent extended absence due to an ankle sprain."
- News (13 Nov): Zubac supplied 12 points (6-12 FG), 13 rebounds, one assist and one block in 26 minutes during Friday's 106-104 win over the Knicks.
- News (10 Nov): Zubac posted 16 points (5-7 FG, 6-8 FT) and three rebounds across 28 minutes in Monday's 125-122 loss to the Mavericks.
- **Research:**
  - 22 min on 15 Nov, no injury listed (search snippet of a Pacers recap only).
  - Verdict: *nothing new found*.

## Other rosters: injury flags only

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 22 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Out 16 Nov; still only 4–6 weeks from 24 Oct ([Magic, 24 Oct](https://www.nba.com/magic/news/paolo-banchero-injury-update-low-grade-high-ankle-sprain-20261024)); no update since ([FantasyAlarm, 9 Nov](https://www.fantasyalarm.com/articles/nba/fantasy-basketball-injury-report/nba-injury-report-week-4-2026-fantasy-basketball/198451)).
  - Verdict: *nothing new found*; ESPN est. 22 Nov is the early edge.

### Donovan Mitchell (CLE, PG/SG, Dr White Slong)

- Rate **39.9** · season 41.5 (13) · L7 36.3 (3) · L15 40.4 (8) · L30 41.5 (13) · projected 46.5
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Mitchell (knee) has been ruled out for Saturday's game against the Mavericks."
- News (15 Nov): Mitchell (knee) is not listed on the injury report for Monday's game against the Bulls.
- News (14 Nov): Mitchell (knee) has been ruled out for Saturday's game against the Mavericks.
- **Research:**
  - Off the 16 Nov report; the 14 Nov absence was a rest night ([Heavy, 15 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/cavaliers-hit-with-brutal-injury-news-ahead-of-bulls-game/)).
  - Verdict: *ESPN confirmed*.

### James Harden (CLE, PG/SG, Team Nic Kerr)

- Rate **37.2** · season 33.0 (13) · L7 41.7 (3) · L15 35.0 (8) · L30 33.0 (13) · projected 42.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Harden (calf) has been ruled out for Saturday's game against Dallas."
- News (15 Nov): Harden (calf) is not listed on the injury report for Monday's tilt against the Bulls.
- News (14 Nov): Harden (calf) has been ruled out for Saturday's game against Dallas.
- **Research:**
  - Off the 16 Nov report; rested 14 Nov ([Heavy, 15 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/cavaliers-hit-with-brutal-injury-news-ahead-of-bulls-game/)).
  - Verdict: *ESPN confirmed*.

### Jarrett Allen (CLE, C, Dr White Slong)

- Rate **36.7** · season 34.2 (11) → 37.6 (10) · L7 34.7 (3) · L15 31.7 (6) → 38.0 (5) · L30 34.2 (11) → 37.6 (10) · projected 36.9
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Allen (knee) has been ruled out for Saturday's game against the Mavericks."
- News (15 Nov): Allen (knee) is not listed on the injury report for Monday's game against the Bulls.
- News (14 Nov): Allen (knee) has been ruled out for Saturday's game against the Mavericks.
- **Research:**
  - Removed from the injury report for 16 Nov ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/jarrett-allen-knee-removed-from-injury-report)).
  - Verdict: *ESPN confirmed*.

### Michael Porter Jr. (BKN, SF/PF, Team Nic Kerr)

- Rate **36.0** · season 36.2 (11) → 38.8 (10) · L7 33.5 (2) · L15 34.2 (6) · L30 36.2 (11) → 38.8 (10) · projected 38.9
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Porter (personal) is out for Saturday's game against the Grizzlies, Brian Lewis of the New York Post reports."
- News (15 Nov): Porter (personal) is off the injury report ahead of Monday's game against the 76ers.
- News (14 Nov): Porter (personal) is out for Saturday's game against the Grizzlies, Brian Lewis of the New York Post reports.
- **Research:**
  - The 14 Nov absence was personal; available 16 Nov vs PHI ([Nets Wire via Yahoo, 15 Nov](https://sports.yahoo.com/articles/nets-michael-porter-jr-personal-025125034.html)).
  - Verdict: *ESPN confirmed*.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-16 04:42 UTC.
- [ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909982)
- [Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html)
- [Detroit Sports Nation, 14 Nov](https://detroitsportsnation.com/duncan-robinson-injury-update-pistons-heat/ddrysdale/detroit-pistons/11/14/2026/507834)
- [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/nor-starting-fears-herb-bey-zion-missi)
- [CBS, 15 Nov](https://cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-out-again-vs-warriors)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/yves-missi-logs-22-minutes-in-return-to-lineup)
- [RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-blocks-four-shots-in-return-539214)
- [CelticsBlog, 15 Nov](https://celticsblog.com/celtics-highlights/150272/celtics-mavericks)
- [RotoBaller, 2 Nov](https://www.rotoballer.com/?p=1982197)
- [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)
- [CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-will-play-saturday/)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/norman-powell-back-available-vs-minnesota)
- [Yahoo](https://sports.yahoo.com/articles/bulls-injury-report-first-game-181313737.html)
- [SI, 15 Nov](https://www.si.com/nba/jazz/onsi/jazz-vs-spurs-injury-report-reveals-major-problem-for-utah-rotation)
- [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)
- [RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/jalen-suggs-news-logs-21-minutes-in-return-538990)
- [ClutchPoints, 14 Nov](https://clutchpoints.com/nba/orlando-magic/magic-news-sean-sweeney-jalen-suggs-return-injury-bucks)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/jerami-grant-head-removed-from-injury-report)
- [NBC Sports, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/iisalo-pippen-back-day-to-day-or-week-to-week)
- [Yahoo, 15 Nov](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html)
- [RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/grayson-allen-news-not-starting-sunday-539277)
- [Heavy, 15 Nov](https://heavy.com/sports/hornets-brandon-miller-cleared-return-clippers/)
- [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-back-to-bench/)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/okc-starts-sga-mccain-mitchell-kenrich-ihart)
- [CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-jaxson-hayes-ruled-out-for-sunday/)
- [SI, 15 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-provide-more-clarity-on-jaxson-hayes-latest-injury)
- [107.5 The Game, 14 Nov](https://www.1075thegame.com/2026/11/14/tyrese-proctor-has-first-triple-double-as-cavs-rest-starters-top-mavs/)
- [Heavy, 15 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/cavaliers-hit-with-brutal-injury-news-ahead-of-bulls-game/)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/zach-edey-ankle-questionable-monday-vs-wizards)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/isaiah-stewart-illness-questionable-monday)
- [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-evan-mobley-ruled-out-for-monday/)
- [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-questionable-for-monday/)
- [CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-toumani-camara-posts-14-points-in-decisive-win/)
- [NBA.com, 30 Oct](https://www.nba.com/news/ja-morant-hamstring-injury-october-2026)
- [SI](https://www.si.com/nba/trailblazers/onsi/4-blazers-ruled-out-vs-wolves-means-depth-chart-will-be-tested)
- [Yahoo, 15 Nov](https://sports.yahoo.com/articles/timberwolves-lose-jaylen-clark-least-235639664.html)
- [CBS/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-jaylen-clark-wont-return-saturday/)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/myles-turner-rest-ruled-out-vs-los-angeles)
- [Dallas Sports Journal, 15 Nov](https://dallassportsjournal.com/kyrie-irving-max-christie-out-mavericks-celtics/)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kyrie-irving-knee-downgraded-to-out-sunday)
- [Yardbarker, 24 Oct](https://www.yardbarker.com/nba/articles/dusty_may_addresses_kyrie_irving_playing_both_nights_of_mavericks_back_to_backs/s1_17810_44470036)
- [Journal Sentinel via Yahoo, 16 Nov](https://sports.yahoo.com/articles/bucks-coach-taylor-jenkins-tinkers-035758071.html)
- [Sports Mole, 15 Nov](https://www.sportsmole.co.uk/basketball/portland-trail-blazers/preview/trail-blazers-vs-timberwolves-player-props-injury-report-and-prediction--nba_609140.html)
- [NBC Sports](https://www.nbcsports.com/nba/jaylen-brown/10472/news)
- [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ty-jerome-hip-remains-out-monday-vs-washington)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/cam-spencer-starting-in-place-of-ty-jerome)
- [NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/mil-starts-burries-herro-dieng-kuzma-turner)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ajay-mitchell-ankle-scores-14-points-in-return)
- [Magic, 24 Oct](https://www.nba.com/magic/news/paolo-banchero-injury-update-low-grade-high-ankle-sprain-20261024)
- [FantasyAlarm, 9 Nov](https://www.fantasyalarm.com/articles/nba/fantasy-basketball-injury-report/nba-injury-report-week-4-2026-fantasy-basketball/198451)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/jarrett-allen-knee-removed-from-injury-report)
- [Nets Wire via Yahoo, 15 Nov](https://sports.yahoo.com/articles/nets-michael-porter-jr-personal-025125034.html)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/kevin-huerter-puts-up-20-4-7-1-3-line-off-bench)
- [Heavy, 15 Nov](https://heavy.com/sports/nba/detroit-pistons/duncan-robinson-injury-addressed-miami-heat-loss/)
- [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/tor-starts-quickley-walter-barrett-barnes-cmb)
- [ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909990)
- [Hoops Rumors](https://www.hoopsrumors.com/transactions)
- [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)
- [NBA.com, 14 Nov](https://www.nba.com/news/dejounte-murray-requests-trade-pelicans-confirm)
- [Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)
- [NBC Sports, 15 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-15/jalen-smith-finger-questionable-vs-cleveland)
- [NBC Sports, 15 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-15/scottie-barnes-scores-game-high-30-in-ot-defeat)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/kawhi-leonards-knee-keeps-raptors-200300316.html)
- [RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/fred-vanvleet-injury-ruled-out-for-sunday-539130)
