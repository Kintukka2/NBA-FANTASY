# News watch: 15 Nov 2026

- Generated 2026-11-16 04:42 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 53 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 39 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

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
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, us)

- Rate **30.6** · role rate 34.3 · season 29.4 (14) · L7 29.2 (5) · L15 33.3 (9) · L30 29.4 (14) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 12 before; 33.3 min in his starts, against 28.4 for the season
- **Role:** news on 13 Nov: "Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports."
- **Minutes:** 35.0 min over his last 3 games against 28.4 for the season (+6.6)
- News (13 Nov): Bey notched 30 points (11-20 FG, 6-9 3Pt, 2-3 FT), 10 rebounds and one block across 35 minutes in Friday's 142-111 loss to the Grizzlies.
- News (13 Nov): Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports.
- **Research:** _pending_

### Yves Missi (NO, C, us)

- Rate **32.0** (small sample) · season 36.0 (3) → 46.5 (2) · L7 25.0 (1) · L15 25.0 (1) · L30 36.0 (3) → 46.5 (2) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **41.0** · season 41.3 (11) · L7 42.7 (3) · L15 39.7 (6) · L30 41.3 (11) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov, Sat 21–Sun 22 Nov; news on 11 Nov: "George will sit out the second leg of this back-to-back set due to an illness, and his next opportunity to play will come Sunday against the Mavericks."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- **Research:** _pending_

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:** _pending_

## Free agents and waivers

### Norman Powell (CHI, SG/SF, free agent)

- Rate **38.2** · season 30.0 (10) → 32.9 (9) · L7 45.0 (2) · L15 29.2 (4) → 37.7 (3) · L30 30.0 (10) → 32.9 (9) · projected 36.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Powell (back) is listed as questionable for Saturday's game against Minnesota."
- **Minutes:** news on 13 Nov: "Powell led all scorers with 33 points in his return to action, showing no signs of limitations after being cleared to play without a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 14 Nov: "Powell was questionable to play Saturday due to lower-back injury management, but he'll fight through it and suit up for the second leg of Chicago's back-to-back set."
- News (14 Nov): Powell finished with 23 points (10-19 FG, 3-5 3Pt), five rebounds, three assists, a steal and two blocks across 30 minutes in Saturday's 117-106 victory over the Timberwolves.
- News (14 Nov): Powell (back) is available for Saturday's game against the Timberwolves, K.C. Johnson of Chicago Sports Network reports.
- **Research:** _pending_

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Injury:** ESPN est. 20 Nov (Out, Right Foot Strain, updated 06 Nov), but the news said on 06 Nov: "He will be re-evaluated in two weeks, the Jazz announced Friday."
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:** _pending_

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **27.7** · season 20.8 (4) → 26.3 (3) · L7 4.0 (1) → — · L15 4.0 (1) → — · L30 20.8 (4) → 26.3 (3) · projected 29.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 13 Nov: "Suggs (knee) participated in the Magic's morning shootaround and remains questionable for Friday's game against the Bucks, Jason Beede of the Orlando Sentinel reports."
- News (13 Nov): Suggs notched three points (1-8 FG, 1-6 3Pt), two rebounds and three assists across 21 minutes during Friday's 107-99 win over the Bucks.
- News (13 Nov): Suggs (knee) will come off the bench Friday against the Bucks.
- **Research:** _pending_

### Jerami Grant (MEM, PF, free agent)

- Rate **26.6** · season 21.8 (12) → 23.6 (11) · L7 31.0 (3) · L15 24.4 (7) · L30 21.8 (12) → 23.6 (11) · projected 27.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Grant (head) is out for Saturday's game against the Nets."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Grant will miss the second leg of Memphis' back-to-back set due to a head injury."
- News (15 Nov): Grant (head) is off the injury report ahead of Monday's game against the Wizards.
- News (14 Nov): Grant (head) is out for Saturday's game against the Nets.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.7** · role rate 24.0 · season 30.6 (9) · L7 13.7 (3) · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 20 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 20 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:** _pending_

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **16.3** · season 14.2 (5) · L7 — · L15 — · L30 14.2 (5) · projected 30.6
- ESPN: out, ESPN est. 21 Nov (Back Soreness, updated 2026-11-10)
- **Injury:** ESPN est. 21 Nov (Out, Back Soreness, updated 10 Nov), but the news said on 10 Nov: "He has now been sidelined for six straight contests due to the back issue and can be considered week-to-week until Memphis offers an update on his recovery."
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- News (08 Nov): Pippen (back) won't play in Monday's game versus the Raptors.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **31.5** · role rate 29.7 · season 26.8 (13) · L7 36.0 (3) · L15 31.7 (7) · L30 26.8 (13) · projected 26.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (15 Nov): Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports.
- News (13 Nov): Allen logged 14 points (5-11 FG, 4-8 3Pt), four rebounds, six assists and one steal over 34 minutes during Thursday's 101-96 loss to Phoenix.
- **Research:** _pending_

### Aday Mara (OKC, C, free agent)

- Rate **30.2** · role rate 32.2 · season 26.6 (14) · L7 32.0 (4) · L15 32.3 (9) · L30 26.6 (14)
- ESPN: active
- **Role:** started 1 of his last 2 games after 3 of 12 before; 26.2 min in his starts, against 21.6 for the season
- **Role:** news on 11 Nov: "Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports."
- News (15 Nov): Mara will come off the bench during Sunday's game against the Kings, Sean Cunningham of Fox 40 Sacramento reports.
- News (14 Nov): Mara amassed 10 points (5-6 FG), three rebounds and three blocks across 21 minutes during Friday's 113-112 loss to the Clippers.
- **Research:** _pending_

### Mo Bamba (UTAH, C, free agent)

- Rate **29.1** · role rate 54.1 · season 29.6 (10) · L7 32.0 (5) · L15 28.9 (8) · L30 29.6 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 8 before; 36.0 min in his starts, against 19.7 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- News (15 Nov): Bamba will start in Sunday's game against San Antonio.
- **Research:** _pending_

### Tyrese Proctor (CLE, SG, free agent)

- Rate **28.7** · role rate 33.8 · season 22.9 (13) · L7 38.5 (4) · L15 28.3 (9) · L30 22.9 (13)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 11 before; 28.0 min in his starts, against 19.2 for the season
- **Role:** news on 14 Nov: "Proctor will start in Saturday's game versus the Mavericks."
- **Minutes:** 28.0 min over his last 3 games against 19.2 for the season (+8.8)
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- News (14 Nov): Proctor will start in Saturday's game versus the Mavericks.
- **Research:** _pending_

### Meleek Thomas (CLE, SG, free agent)

- Rate **27.9** · role rate 30.2 · season 25.3 (11) · L7 32.2 (4) · L15 25.7 (9) · L30 25.3 (11)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 9 before; 28.0 min in his starts, against 23.5 for the season
- **Role:** news on 14 Nov: "Thomas will start in Saturday's game against Dallas."
- News (14 Nov): Thomas will start in Saturday's game against Dallas.
- News (09 Nov): Thomas tallied 18 points (7-12 FG, 4-6 3Pt), three rebounds, three assists, two steals and two blocks across 27 minutes in Monday's 124-112 loss to the Hornets.
- **Research:** _pending_

### Isaiah Stewart (MEM, PF/C, free agent)

- Rate **21.2** · role rate 23.1 · season 21.6 (10) · L7 18.7 (3) · L15 22.8 (6) · L30 21.6 (10) · projected 25.3
- ESPN: day-to-day, ESPN est. 16 Nov (Illness, updated 2026-11-15)
- **Role:** started 2 of his last 2 games after 1 of 8 before; 19.0 min in his starts, against 18.1 for the season
- **Role:** news on 13 Nov: "Stewart will start Friday's game against the Pelicans."
- News (15 Nov): Stewart is questionable for Monday's game against the Wizards due to an illness.
- News (14 Nov): Stewart chipped in 12 points (5-7 FG, 0-2 3Pt, 2-2 FT), five rebounds and four blocks across 20 minutes during Friday's 142-111 win over the Pelicans.
- **Research:** _pending_

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **20.5** · role rate 25.8 · season 19.2 (8) · L7 20.3 (3) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: day-to-day, ESPN est. 16 Nov (Right Ankle, updated 2026-11-15)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Role:** news on 13 Nov: "Tyson will start Friday's game against Miami, Serena Winters of FanDuel Sports Network Ohio reports."
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (15 Nov): Tyson (ankle) is questionable for Monday's game against the Bulls.
- News (14 Nov): Tyson closed with 16 points (6-11 FG, 4-7 3Pt), three rebounds, one assist and one steal over 30 minutes during Friday's 133-121 loss to Miami.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **32.0** · role rate 31.6 · season 24.2 (12) · L7 40.2 (4) · L15 33.5 (6) · L30 24.2 (12) · projected 22.9
- ESPN: active
- **Minutes:** 31.7 min over his last 3 games against 24.4 for the season (+7.2)
- News (14 Nov): Huerter posted 20 points (9-15 FG, 2-6 3Pt), four rebounds, seven assists, a steal and three blocks across 38 minutes in Saturday's 137-117 loss to Miami.
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **29.6** · role rate 26.1 · season 34.9 (10) · L7 25.0 (2) · L15 27.2 (4) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Toumani Camara (POR, SF/PF, free agent)

- Rate **27.1** · role rate 30.9 · season 25.8 (12) · L7 31.7 (3) · L15 22.6 (8) · L30 25.8 (12) · projected 23.8
- ESPN: active
- **Minutes:** 34.7 min over his last 3 games against 29.1 for the season (+5.6)
- News (14 Nov): Camara contributed 14 points (5-7 FG, 2-4 3Pt, 2-2 FT), two rebounds, one assist, one block and two steals across 36 minutes during Friday's 120-107 victory over Sacramento.
- News (07 Nov): Camara accumulated 18 points (7-12 FG, 4-8 3Pt), six rebounds and one assist in 30 minutes during Friday's 124-118 loss to the Lakers.
- **Research:** _pending_

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **26.8** · role rate 31.5 · season 25.2 (12) · L7 27.3 (3) · L15 28.4 (7) · L30 25.2 (12) · projected 24.8
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 24.3 for the season (+6.3)
- News (12 Nov): Murray-Boyles ended with 14 points (5-9 FG, 1-1 3Pt, 3-4 FT), four assists, five blocks and one steal over 32 minutes during Thursday's 123-112 loss to the 76ers.
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- **Research:** _pending_

### Bones Hyland (MIN, PG, free agent)

- Rate **26.1** · role rate 29.5 · season 21.4 (13) · L7 32.7 (3) · L15 25.9 (7) · L30 21.4 (13) · projected 17.1
- ESPN: active
- **Minutes:** 19.0 min over his last 3 games against 13.8 for the season (+5.2)
- News (13 Nov): Hyland produced 24 points (7-10 FG, 5-6 3Pt, 5-6 FT), three rebounds, eight assists and two steals across 23 minutes during Thursday's 133-94 victory over Dallas.
- News (09 Nov): Hyland notched 14 points (4-8 FG, 1-5 3Pt, 5-6 FT), two rebounds, two assists and one block across 13 minutes in Sunday's 115-100 win over the Jazz.
- **Research:** _pending_

### Rudy Gobert (MIN, C, free agent)

- Rate **27.8** · season 26.4 (12) · L7 26.0 (3) · L15 29.0 (6) · L30 26.4 (12) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:** _pending_

### Myles Turner (MIL, C, free agent)

- Rate **26.2** · season 26.5 (13) · L7 23.0 (4) · L15 29.2 (8) · L30 26.5 (13) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 12 Nov: "Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando."; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): Turner recorded 14 points (5-9 FG, 4-7 3Pt), 11 rebounds, three assists and two steals across 31 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando.
- **Research:** _pending_

### Zach Edey (MEM, C, free agent)

- Rate **20.3** · season 22.8 (10) · L7 14.0 (2) · L15 20.2 (6) · L30 22.8 (10) · projected 33.2
- ESPN: day-to-day, ESPN est. 16 Nov (Left Ankle, updated 2026-11-15)
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Edey sat out Memphis' game Friday due to an ankle injury, and he is now at risk of missing both legs of this back-to-back set."; sat the first night of the 25–26 Oct back-to-back, playing the games either side
- News (15 Nov): Edey (ankle) is questionable for Monday's game against Washington.
- News (14 Nov): Edey (ankle) is listed as out for Saturday's game against the Nets.
- **Research:** _pending_

## Opponents: this week and next

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **42.3** · season 41.5 (11) · L7 44.0 (4) · L15 40.8 (6) · L30 41.5 (11) · projected 44.2
- ESPN: out, ESPN est. 18 Nov (Left Knee, updated 2026-11-15)
- **Injury:** ESPN est. 18 Nov (Out, Left Knee, updated 15 Nov), but the news said on 14 Nov: "The 34-year-old veteran had a slow start to the 2026-27 campaign after missing last season while recovering from knee surgery."
- News (15 Nov): Irving (knee) has been ruled out for Sunday's game against the Celtics.
- News (15 Nov): Irving (knee) is questionable to play in Sunday's game against the Celtics.
- **Research:** _pending_

### Cam Spencer (MEM, PG/SG, Lauri Birds)

- Rate **28.9** · role rate 38.3 · season 27.5 (13) · L7 29.5 (4) · L15 30.0 (8) · L30 27.5 (13)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 11 before; 29.5 min in his starts, against 20.9 for the season
- **Role:** news on 14 Nov: "Spencer will start in Saturday's game against the Nets."
- **Minutes:** 26.0 min over his last 3 games against 20.9 for the season (+5.1)
- News (14 Nov): Spencer finished with 17 points (6-10 FG, 3-3 3Pt, 2-2 FT), one rebound, eight assists and two steals across 34 minutes in Saturday's 129-110 win over the Nets.
- News (14 Nov): Spencer will start in Saturday's game against the Nets.
- **Research:** _pending_

### Jaime Jaquez Jr. (MIL, SG/SF, Lauri Birds)

- Rate **28.2** · role rate 29.8 · season 28.7 (14) · L7 27.8 (5) · L15 27.3 (9) · L30 28.7 (14) · projected 28.2
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 11 of 12; 29.0 min in those 2, against 27.9 for the season
- News (13 Nov): Jaquez chipped in 22 points (8-15 FG, 5-7 3Pt, 1-3 FT), six rebounds and four assists in 28 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Jaquez registered 25 points (7-16 FG, 2-7 3Pt, 9-9 FT), five rebounds, three assists and two steals across 30 minutes during Wednesday's 123-112 loss to the Lakers.
- **Research:** _pending_

### Deni Avdija (POR, SF/PF, Snow Time Lakers)

- Rate **48.0** · season 42.8 (12) → 45.2 (11) · L7 54.0 (3) · L15 41.8 (8) → 45.3 (7) · L30 42.8 (12) → 45.2 (11) · projected 40.4
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 14 Nov: "They'll need more of the same in back-to-back games at Minnesota on Monday and Tuesday."
- News (14 Nov): Avdija finished Friday's 120-107 win over the Kings with 34 points (11-13 FG, 3-5 3Pt, 9-9 FT), six rebounds, four assists and one block across 35 minutes.
- News (12 Nov): Avdija tallied 28 points (9-20 FG, 4-13 3Pt, 6-6 FT), three rebounds, six assists, four steals and two blocks across 35 minutes in Wednesday's 118-108 win over the Thunder.
- **Research:** _pending_

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **38.4** · season 39.1 (13) · L7 35.2 (4) · L15 39.9 (8) · L30 39.1 (13) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (15 Nov): Brown tallied 31 points (12-18 FG, 3-6 3Pt, 4-6 FT), two rebounds, two assists and one steal across 32 minutes during Sunday's 131-124 win over Indiana.
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- **Research:** _pending_

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **32.6** · season 33.7 (13) → 36.2 (12) · L7 21.8 (4) → 28.0 (3) · L15 29.2 (8) → 33.0 (7) · L30 33.7 (13) → 36.2 (12) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (13 Nov): Herro had 18 points (5-17 FG, 2-7 3Pt, 6-7 FT), two assists, two steals, one rebound and one block across 34 minutes in Friday's 107-99 loss to the Magic.
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- **Research:** _pending_

### Ajay Mitchell (OKC, PG/SG, Lauri Birds)

- Rate **31.1** · season 33.7 (12) · L7 29.5 (2) · L15 30.6 (7) · L30 33.7 (12) · projected 32.8
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 11 Nov: "Mitchell won't play in the second leg of the Thunder's back-to-back set after apparently injuring his ankle Tuesday."
- News (15 Nov): Mitchell (ankle) is available for Sunday's game against the Kings, Clemente Almanza of USA Today reports.
- News (14 Nov): Mitchell (ankle) is questionable to suit up for Sunday's game against the Kings.
- **Research:** _pending_

### Ivica Zubac (IND, C, Lauri Birds)

- Rate **29.9** · season 26.7 (9) → 29.2 (8) · L7 31.2 (4) · L15 27.3 (6) · L30 26.7 (9) → 29.2 (8) · projected 35.5
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 13 Nov: "That's now back-to-back double-doubles for Zubac, who appears to be just about all the way back from a recent extended absence due to an ankle sprain."
- News (13 Nov): Zubac supplied 12 points (6-12 FG), 13 rebounds, one assist and one block in 26 minutes during Friday's 106-104 win over the Knicks.
- News (10 Nov): Zubac posted 16 points (5-7 FG, 6-8 FT) and three rebounds across 28 minutes in Monday's 125-122 loss to the Mavericks.
- **Research:** _pending_

## Other rosters: injury flags only

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 22 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

### Donovan Mitchell (CLE, PG/SG, Dr White Slong)

- Rate **39.9** · season 41.5 (13) · L7 36.3 (3) · L15 40.4 (8) · L30 41.5 (13) · projected 46.5
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Mitchell (knee) has been ruled out for Saturday's game against the Mavericks."
- News (15 Nov): Mitchell (knee) is not listed on the injury report for Monday's game against the Bulls.
- News (14 Nov): Mitchell (knee) has been ruled out for Saturday's game against the Mavericks.
- **Research:** _pending_

### James Harden (CLE, PG/SG, Team Nic Kerr)

- Rate **37.2** · season 33.0 (13) · L7 41.7 (3) · L15 35.0 (8) · L30 33.0 (13) · projected 42.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Harden (calf) has been ruled out for Saturday's game against Dallas."
- News (15 Nov): Harden (calf) is not listed on the injury report for Monday's tilt against the Bulls.
- News (14 Nov): Harden (calf) has been ruled out for Saturday's game against Dallas.
- **Research:** _pending_

### Jarrett Allen (CLE, C, Dr White Slong)

- Rate **36.7** · season 34.2 (11) → 37.6 (10) · L7 34.7 (3) · L15 31.7 (6) → 38.0 (5) · L30 34.2 (11) → 37.6 (10) · projected 36.9
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Allen (knee) has been ruled out for Saturday's game against the Mavericks."
- News (15 Nov): Allen (knee) is not listed on the injury report for Monday's game against the Bulls.
- News (14 Nov): Allen (knee) has been ruled out for Saturday's game against the Mavericks.
- **Research:** _pending_

### Michael Porter Jr. (BKN, SF/PF, Team Nic Kerr)

- Rate **36.0** · season 36.2 (11) → 38.8 (10) · L7 33.5 (2) · L15 34.2 (6) · L30 36.2 (11) → 38.8 (10) · projected 38.9
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 14 Nov: "Porter (personal) is out for Saturday's game against the Grizzlies, Brian Lewis of the New York Post reports."
- News (15 Nov): Porter (personal) is off the injury report ahead of Monday's game against the 76ers.
- News (14 Nov): Porter (personal) is out for Saturday's game against the Grizzlies, Brian Lewis of the New York Post reports.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-16 04:42 UTC.
