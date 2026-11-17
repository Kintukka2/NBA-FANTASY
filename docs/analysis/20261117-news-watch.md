# News watch: 17 Nov 2026

- Generated 2026-11-17 21:18 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 98 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 41 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Jalen Duren | return | 2026-11-23 | — | [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) | in force |
| Scotty Pippen Jr. | return | 2026-11-22 | — | [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html) | in force |
| Dejounte Murray | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline) | expired: remove it |
| Nic Claxton | role | 18 | 2026-11-16 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Jalen Smith** | CHI | us | injury, rest | 43.7 | — | active |
| **Saddiq Bey** | NO | us | role, minutes | 34.6 | 35.5 | active |
| **Daniss Jenkins** | DET | us | role, minutes | 30.0 | 38.6 | active |
| **Yves Missi** | NO | us | minutes | 35.4 | — | active |
| **Scottie Barnes** | TOR | us | rest | 54.2 | — | day-to-day, ESPN est. 17 Nov |
| **Paul George** | BOS | us | rest | 40.2 | — | active |
| **Kawhi Leonard** | TOR | us | gap | 41.7 † | — | out, ESPN est. 23 Nov |
| **Jusuf Nurkic** | UTAH | free agent | injury, gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Dejounte Murray** | NO | free agent | injury, minutes | 22.5 | 24.0 | out, ESPN est. 20 Nov |
| **Jalen Suggs** | ORL | free agent | role, minutes | 34.9 | — | active |
| **Mo Bamba** | UTAH | free agent | role | 30.5 | 54.1 | active |
| **Aday Mara** | OKC | free agent | role | 30.0 | 32.2 | active |
| **Tyrese Proctor** | CLE | free agent | role, minutes | 29.7 | 33.4 | active |
| **Grayson Allen** | CHA | free agent | role | 27.7 | 29.7 | active |
| **Quentin Grimes** | LAL | free agent | role | 27.3 | 24.8 | active |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 20.5 | 25.8 | day-to-day, ESPN est. 18 Nov |
| **Isaiah Stewart** | MEM | free agent | role | 20.4 | 23.1 | day-to-day, ESPN est. 18 Nov |
| **Caleb Wilson** | CHI | free agent | minutes | 29.9 | 26.1 | out, ESPN est. 13 Dec |
| **Kevin Huerter** | DET | free agent | minutes | 29.6 | 31.6 | active |
| **Collin Murray-Boyles** | TOR | free agent | minutes | 27.3 | 31.5 | active |
| **Kelly Oubre Jr.** | IND | free agent | minutes, rest | 27.3 | 26.9 | active |
| **Zach Edey** | MEM | free agent | rest | 27.4 | — | active |
| **Neemias Queta** | BOS | free agent | rest | 27.4 | — | day-to-day, ESPN est. 18 Nov |
| **Myles Turner** | MIL | free agent | rest | 26.7 | — | active |
| **Santi Aldama** | DAL | free agent | rest | 15.2 | — | day-to-day, ESPN est. 18 Nov |
| **Ja Morant** | POR | free agent | gap | 34.1 | — | out, ESPN est. 01 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 41.6 | — | day-to-day, ESPN est. 18 Nov |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | injury | 30.4 | — | active |
| **Norman Powell** | CHI | Matt Wright's Foxies | minutes, rest | 37.0 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | minutes | 18.8 | 20.2 | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 42.8 | — | day-to-day, ESPN est. 18 Nov |
| **Cooper Flagg** | DAL | Matt Wright's Foxies | rest | 40.6 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 39.0 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 35.4 | — | active |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | rest | 32.6 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 31.2 | — | day-to-day, ESPN est. 18 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 60.9 † | — | out, ESPN est. 22 Nov |
| **Bam Adebayo** | MIA | Lauri Birds | injury | 44.7 | — | day-to-day, ESPN est. 18 Nov |
| **Julius Randle** | BKN | Dr White Slong | injury | 37.8 | — | active |
| **Joel Embiid** | PHI | Dr White Slong | injury | 35.3 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:** _pending_

### Jalen Smith (CHI, PF/C, us)

- Rate **43.7** · season 36.2 (12) → 38.6 (11) · L7 50.3 (3) · L15 40.2 (6) → 46.2 (5) · L30 36.2 (12) → 38.6 (11) · projected 22.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Smith (head) exited in the fourth quarter of Monday's 126-115 loss to the Cavaliers and did not return."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (17 Nov): Smith (head) isn't listed on the injury report for Wednesday's game against Brooklyn.
- News (16 Nov): Smith (head) exited in the fourth quarter of Monday's 126-115 loss to the Cavaliers and did not return.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, us)

- Rate **34.6** · role rate 35.5 · season 30.7 (15) · L7 39.8 (4) · L15 33.4 (9) · L30 30.7 (15) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 33.2 min in his starts, against 28.7 for the season
- **Role:** news on 13 Nov: "Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports."
- **Minutes:** 36.3 min over his last 3 games against 28.7 for the season (+7.6)
- News (17 Nov): Bey finished with 23 points (8-15 FG, 5-8 3Pt, 2-2 FT), six rebounds, three assists, one steal and one block across 33 minutes in Monday's 115-94 win over Golden State.
- News (13 Nov): Bey notched 30 points (11-20 FG, 6-9 3Pt, 2-3 FT), 10 rebounds and one block across 35 minutes in Friday's 142-111 loss to the Grizzlies.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, us)

- Rate **30.0** · role rate 38.6 · season 28.7 (12) · L7 31.5 (2) · L15 32.3 (6) · L30 28.7 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 10 before; 37.8 min in his starts, against 28.0 for the season
- **Minutes:** 37.7 min over his last 3 games against 28.0 for the season (+9.7)
- News (12 Nov): Jenkins had 21 points (6-11 FG, 3-5 3Pt, 6-6 FT), six rebounds and two steals in 42 minutes before fouling out of Thursday's 144-140 double-overtime victory over Washington.
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- **Research:** _pending_

### Yves Missi (NO, C, us)

- Rate **35.4** · season 36.8 (4) → 44.0 (3) · L7 32.0 (2) · L15 32.0 (2) · L30 36.8 (4) → 44.0 (3) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:** _pending_

### Scottie Barnes (TOR, SG/SF, us)

- Rate **54.2** · season 47.6 (9) → 52.0 (8) · L7 61.0 (1) · L15 50.0 (3) · L30 47.6 (9) → 52.0 (8) · projected 43.7
- ESPN: day-to-day, ESPN est. 17 Nov (Illness, updated 2026-11-17)
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 17 Nov: "Barnes was a late addition to the injury report and could sit out the front end of this back-to-back set."
- News (17 Nov): Barnes (illness) has been downgraded to questionable for Tuesday's game against the Knicks, Blake Murphy of Sportsnet.ca reports.
- News (16 Nov): Barnes finished with 30 points (13-27 FG, 4-8 3Pt, 0-3 FT), nine rebounds, four assists, two blocks and one steal across 36 minutes during Sunday's 112-108 overtime loss to New York.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **40.2** · season 41.3 (12) · L7 41.3 (3) · L15 38.3 (6) · L30 41.3 (12) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- **Research:** _pending_

### Kawhi Leonard (TOR, SF/PF, us)

- Rate **41.7** (small sample) · season 40.0 (2) · L7 — · L15 — · L30 40.0 (2) · projected 45.8
- ESPN: out, ESPN est. 23 Nov (Left Knee Inflammation, updated 2026-11-11)
- **Gap:** listed out, and no news in 5 days (ESPN est. 23 Nov)
- News (11 Nov): Head coach Darko Rajakovic said Wednesday that Leonard (knee) is doing individual on-court work and is progressing well, Michael Grange of Sportsnet.ca reports.
- News (10 Nov): Leonard (knee) is continuing the reconditioning process, and another update will be provided in one week, Blake Murphy of Sportsnet.ca reports.
- **Research:** _pending_

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Injury:** ESPN est. 20 Nov (Out, Right Foot Strain, updated 06 Nov), but the news said on 06 Nov: "He will be re-evaluated in two weeks, the Jazz announced Friday."
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.5** · role rate 24.0 · season 30.6 (9) · L7 13.0 (1) · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 20 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 20 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:** _pending_

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **34.9** · season 24.2 (5) → 29.2 (4) · L7 21.0 (2) → 38.0 (1) · L15 21.0 (2) → 38.0 (1) · L30 24.2 (5) → 29.2 (4) · projected 29.2
- ESPN: active
- **Role:** news on 16 Nov: "Suggs will start Monday's game against the Celtics."
- **Minutes:** news on 17 Nov: "His presence is key for the Magic, meaning his playing time should continue to ramp up over the next few games."
- News (17 Nov): Suggs accumulated 12 points (5-8 FG, 2-4 3Pt), six rebounds, four assists and two blocks across 25 minutes during Monday's 115-105 win over the Celtics.
- News (16 Nov): Suggs will start Monday's game against the Celtics.
- **Research:** _pending_

### Mo Bamba (UTAH, C, free agent)

- Rate **30.5** · role rate 54.1 · season 29.6 (10) · L7 34.8 (4) · L15 30.6 (7) · L30 29.6 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 8 before; 36.0 min in his starts, against 19.7 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- News (15 Nov): Bamba will start in Sunday's game against San Antonio.
- **Research:** _pending_

### Aday Mara (OKC, C, free agent)

- Rate **30.0** · role rate 32.2 · season 26.6 (14) · L7 32.0 (4) · L15 31.9 (8) · L30 26.6 (14)
- ESPN: active
- **Role:** started 1 of his last 2 games after 3 of 12 before; 26.2 min in his starts, against 21.6 for the season
- News (16 Nov): Mara closed with 16 points (8-11 FG), 13 rebounds and three assists across 26 minutes off the bench during Sunday's 125-103 win over Sacramento.
- News (15 Nov): Mara will come off the bench during Sunday's game against the Kings, Sean Cunningham of Fox 40 Sacramento reports.
- **Research:** _pending_

### Tyrese Proctor (CLE, SG, free agent)

- Rate **29.7** · role rate 33.4 · season 23.2 (14) · L7 41.2 (4) · L15 28.3 (9) · L30 23.2 (14)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 12 before; 28.3 min in his starts, against 19.9 for the season
- **Role:** news on 14 Nov: "Proctor will start in Saturday's game versus the Mavericks."
- **Minutes:** 30.0 min over his last 3 games against 19.9 for the season (+10.1)
- News (17 Nov): Proctor had 17 points (6-13 FG, 2-6 3Pt, 3-5 FT), three rebounds, two assists, two steals and one block over 29 minutes during Monday's 126-115 victory over the Bulls.
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.7** · role rate 29.7 · season 26.8 (13) · L7 27.5 (2) · L15 28.2 (6) · L30 26.8 (13) · projected 26.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (15 Nov): Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports.
- News (13 Nov): Allen logged 14 points (5-11 FG, 4-8 3Pt), four rebounds, six assists and one steal over 34 minutes during Thursday's 101-96 loss to Phoenix.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **27.3** · role rate 24.8 · season 18.8 (12) · L7 42.0 (1) · L15 20.0 (5) · L30 18.8 (12) · projected 28.1
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 35.7 min in his starts, against 27.0 for the season
- **Role:** news on 15 Nov: "Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports."
- News (15 Nov): Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports.
- News (14 Nov): Grimes (finger) is available to play in Sunday's game against the Suns.
- **Research:** _pending_

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **20.5** · role rate 25.8 · season 19.2 (8) · L7 20.3 (3) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: day-to-day, ESPN est. 18 Nov (Right Ankle, updated 2026-11-17)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Role:** news on 13 Nov: "Tyson will start Friday's game against Miami, Serena Winters of FanDuel Sports Network Ohio reports."
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (16 Nov): Tyson (ankle) has been ruled out for Monday's game against Chicago.
- News (16 Nov): Tyson (ankle) has been downgraded to doubtful for Monday's game against the Bulls.
- **Research:** _pending_

### Isaiah Stewart (MEM, PF/C, free agent)

- Rate **20.4** · role rate 23.1 · season 21.6 (10) · L7 18.7 (3) · L15 19.8 (5) · L30 21.6 (10) · projected 25.3
- ESPN: day-to-day, ESPN est. 18 Nov (Illness, updated 2026-11-17)
- **Role:** started 2 of his last 2 games after 1 of 8 before; 19.0 min in his starts, against 18.1 for the season
- **Role:** news on 13 Nov: "Stewart will start Friday's game against the Pelicans."
- News (16 Nov): Stewart is out for Monday's game against the Wizards due to an illness.
- News (15 Nov): Stewart is questionable for Monday's game against the Wizards due to an illness.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **29.9** · role rate 26.1 · season 34.9 (10) · L7 26.0 (1) · L15 27.2 (4) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **29.6** · role rate 31.6 · season 24.2 (12) · L7 33.0 (2) · L15 33.5 (6) · L30 24.2 (12) · projected 22.9
- ESPN: active
- **Minutes:** 31.7 min over his last 3 games against 24.4 for the season (+7.2)
- News (14 Nov): Huerter posted 20 points (9-15 FG, 2-6 3Pt), four rebounds, seven assists, a steal and three blocks across 38 minutes in Saturday's 137-117 loss to Miami.
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- **Research:** _pending_

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **27.3** · role rate 31.5 · season 25.2 (12) · L7 27.3 (3) · L15 30.5 (6) · L30 25.2 (12) · projected 24.8
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 24.3 for the season (+6.3)
- News (12 Nov): Murray-Boyles ended with 14 points (5-9 FG, 1-1 3Pt, 3-4 FT), four assists, five blocks and one steal over 32 minutes during Thursday's 123-112 loss to the 76ers.
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- **Research:** _pending_

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **27.3** · role rate 26.9 · season 21.3 (12) · L7 34.0 (3) · L15 26.0 (5) · L30 21.3 (12) · projected 23.2
- ESPN: active
- **Minutes:** 31.0 min over his last 3 games against 24.6 for the season (+6.4)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 13 Nov: "Oubre's fantasy arrow is beginning to point up, as he's now drawn back-to-back starts for the Pacers while pushing previous starter Braden Smith from the rotation entirely."
- News (15 Nov): Oubre notched 16 points (6-11 FG, 2-5 3Pt, 2-2 FT), four rebounds, two assists, one block and one steal over 29 minutes during Sunday's 131-124 loss to Philadelphia.
- News (13 Nov): Oubre ended Friday's 106-104 win over the Knicks with 16 points (5-13 FG, 1-4 3Pt, 5-6 FT), five rebounds, one block and two steals in 30 minutes.
- **Research:** _pending_

### Zach Edey (MEM, C, free agent)

- Rate **27.4** · season 25.1 (11) · L7 28.0 (2) · L15 26.7 (6) · L30 25.1 (11) · projected 33.2
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Edey sat out Memphis' game Friday due to an ankle injury, and he is now at risk of missing both legs of this back-to-back set."; sat the first night of the 25–26 Oct back-to-back, playing the games either side
- News (17 Nov): Edey provided 23 points (10-15 FG, 3-3 FT), 10 rebounds, one assist and one block across 21 minutes during Monday's 136-120 victory over the Wizards.
- News (16 Nov): Edey (ankle) is available for Monday's game against the Wizards.
- **Research:** _pending_

### Neemias Queta (BOS, C, free agent)

- Rate **27.4** · season 25.6 (13) · L7 27.7 (3) · L15 27.9 (7) · L30 25.6 (13) · projected 27.2
- ESPN: day-to-day, ESPN est. 18 Nov (Rest, updated 2026-11-17)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 16 Nov: "Queta (rest) won't play in Monday's game against the Magic, Taylor Snow of the Celtics' official site reports."
- News (16 Nov): Queta (rest) won't play in Monday's game against the Magic, Taylor Snow of the Celtics' official site reports.
- News (16 Nov): Queta (rest) is questionable for Monday's game against the Magic.
- **Research:** _pending_

### Myles Turner (MIL, C, free agent)

- Rate **26.7** · season 26.5 (13) · L7 25.0 (3) · L15 28.6 (7) · L30 26.5 (13) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): Turner recorded 14 points (5-9 FG, 4-7 3Pt), 11 rebounds, three assists and two steals across 31 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando.
- **Research:** _pending_

### Santi Aldama (DAL, SF/PF, free agent)

- Rate **15.2** · season 14.8 (5) · L7 12.5 (2) · L15 14.8 (5) · L30 14.8 (5) · projected 25.0
- ESPN: day-to-day, ESPN est. 18 Nov (Left Ankle Sprain, updated 2026-11-17)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 15 Nov: "Aldama will miss Sunday's game with an ankle injury, which is not surprising given it is the second half of a back-to-back set."
- News (17 Nov): Aldama (ankle) was a full participant in Tuesday's practice, Mike Curtis of The Dallas Morning News reports.
- News (15 Nov): Aldama (ankle) is out for Sunday's game against the Celtics.
- **Research:** _pending_

### Ja Morant (POR, PG, free agent)

- Rate **34.1** · season 33.8 (4) · L7 — · L15 — · L30 33.8 (4) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:** _pending_

## Opponents: this week and next

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **41.6** · season 40.8 (14) · L7 39.2 (4) · L15 44.6 (8) · L30 40.8 (14) · projected 38.6
- ESPN: day-to-day, ESPN est. 18 Nov (Left Hamstring, updated 2026-11-17)
- **Injury:** ESPN est. 18 Nov (Day-To-Day, Left Hamstring, updated 17 Nov), but the news said on 16 Nov: "Brown (hamstring/head) will undergo further evaluation Tuesday and could receive an MRI, Kris Rhim of ESPN reports."
- News (16 Nov): Brown (hamstring/head) will undergo further evaluation Tuesday and could receive an MRI, Kris Rhim of ESPN reports.
- News (16 Nov): Brown amassed 31 points (9-19 FG, 3-8 3Pt, 10-13 FT), 13 rebounds, four assists, one steal and one block in 33 minutes during Monday's 135-123 win over Brooklyn.
- **Research:** _pending_

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **30.4** · season 32.7 (13) · L7 29.5 (2) · L15 27.0 (7) · L30 32.7 (13) · projected 38.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 15 Nov: "Fox (hip) has been ruled out for Sunday's game against the Jazz."
- News (16 Nov): Fox (hip) is not listed on the injury report for Tuesday's game against the Pistons.
- News (15 Nov): Fox (hip) has been ruled out for Sunday's game against the Jazz.
- **Research:** _pending_

### Norman Powell (CHI, SG/SF, Matt Wright's Foxies)

- Rate **37.0** · season 30.5 (11) → 33.1 (10) · L7 41.7 (3) · L15 30.4 (5) → 37.0 (4) · L30 30.5 (11) → 33.1 (10) · projected 36.0
- ESPN: active
- **Minutes:** news on 13 Nov: "Powell led all scorers with 33 points in his return to action, showing no signs of limitations after being cleared to play without a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 14 Nov: "Powell was questionable to play Saturday due to lower-back injury management, but he'll fight through it and suit up for the second leg of Chicago's back-to-back set."
- News (16 Nov): Powell tallied 27 points (10-18 FG, 0-6 3Pt, 7-11 FT), two rebounds, six assists and one steal across 33 minutes during Monday's 126-115 loss to Cleveland.
- News (16 Nov): Powell (undisclosed) has been cleared to return to Monday's game against the Cavaliers, K.C. Johnson of Chicago Sports Network reports.
- **Research:** _pending_

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **18.8** · role rate 20.2 · season 28.7 (11) · L7 11.0 (1) · L15 12.0 (4) · L30 28.7 (11) · projected 37.4
- ESPN: active
- **Minutes:** 21.3 min over his last 3 games against 30.4 for the season (−9.0)
- News (16 Nov): Miller finished Sunday's 113-105 loss to the Clippers with five points (1-10 FG, 1-6 3Pt, 2-3 FT), four assists, two rebounds and one steal over 24 minutes.
- News (14 Nov): Miller (groin) is not listed on the injury report for Sunday's game against the Clippers.
- **Research:** _pending_

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **42.8** · season 41.5 (11) · L7 45.5 (2) · L15 40.8 (6) · L30 41.5 (11) · projected 44.2
- ESPN: day-to-day, ESPN est. 18 Nov (Left Knee, updated 2026-11-16)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 15 Nov: "He will, however, sit out the second leg of the back-to-back for Dallas, which will likely send Cooper Flagg's usage to the moon."; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (15 Nov): Irving (knee) has been ruled out for Sunday's game against the Celtics.
- News (15 Nov): Irving (knee) is questionable to play in Sunday's game against the Celtics.
- **Research:** _pending_

### Cooper Flagg (DAL, SF/PF, Matt Wright's Foxies)

- Rate **40.6** · season 49.2 (13) · L7 29.3 (3) · L15 43.5 (8) · L30 49.2 (13) · projected 45.4
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (16 Nov): Flagg contributed 17 points (5-15 FG, 2-6 3Pt, 5-5 FT), three rebounds, four assists, one block and one steal in 27 minutes during Sunday's 131-94 loss to the Celtics.
- News (13 Nov): Flagg chipped in 12 points (5-12 FG, 1-2 3Pt, 1-2 FT), seven rebounds, three assists and two steals over 27 minutes during Thursday's 133-94 loss to the Timberwolves.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **39.0** · season 39.1 (13) · L7 35.3 (3) · L15 42.8 (6) · L30 39.1 (13) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (15 Nov): Siakam recorded 31 points (12-19 FG, 0-3 3Pt, 7-8 FT), two rebounds, two assists and one steal across 34 minutes during Sunday's 131-124 loss to Philadelphia.
- News (13 Nov): Siakam posted 19 points (5-13 FG, 2-4 3Pt, 7-12 FT), three rebounds and two assists across 32 minutes in Friday's 106-104 win over the Knicks.
- **Research:** _pending_

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.4** · season 33.7 (13) → 36.2 (12) · L7 24.0 (3) → 34.5 (2) · L15 30.6 (7) → 35.2 (6) · L30 33.7 (13) → 36.2 (12) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (13 Nov): Herro had 18 points (5-17 FG, 2-7 3Pt, 6-7 FT), two assists, two steals, one rebound and one block across 34 minutes in Friday's 107-99 loss to the Magic.
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- **Research:** _pending_

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **32.6** · season 35.4 (12) · L7 29.7 (3) · L15 33.4 (7) · L30 35.4 (12) · projected 30.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (17 Nov): Podziemski recorded 15 points (3-8 FG, 3-7 3Pt, 6-7 FT), six rebounds, three assists, one steal and two blocks across 30 minutes in Monday's 115-94 loss to the Pelicans.
- News (12 Nov): Podziemski had 22 points (7-15 FG, 4-11 3Pt, 4-5 FT), six rebounds, four assists and two steals across 37 minutes during Wednesday's 115-108 loss to the Rockets.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **31.2** · season 33.2 (11) · L7 28.0 (2) · L15 31.8 (5) · L30 33.2 (11) · projected 28.2
- ESPN: day-to-day, ESPN est. 18 Nov (Left Hip Soreness, updated 2026-11-15)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (15 Nov): Nembhard (hip) has been ruled out for Sunday's game against the 76ers, Tony East of Forbes.com reports.
- News (14 Nov): Nembhard is questionable for Sunday's game against the 76ers due to left hip soreness.
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

### Bam Adebayo (MIA, PF/C, Lauri Birds)

- Rate **44.7** · season 44.1 (14) · L7 43.8 (4) · L15 47.1 (8) · L30 44.1 (14) · projected 39.6
- ESPN: day-to-day, ESPN est. 18 Nov (Right Hip, updated 2026-11-17)
- **Injury:** ESPN est. 18 Nov (Day-To-Day, Right Hip, updated 17 Nov), but the news said on 16 Nov: "Miami will presumably re-evaluate Adebayo over the next few days to determine whether he'll be able to suit up for Wednesday's game against Milwaukee."
- News (16 Nov): Coach Erik Spoelstra stated after Monday's 128-110 win over Houston that the team held Adebayo (hip) out of the second half in an effort to be proactive, and the injury isn't expected to be a long-term issue, Anthony Chiang of the Miami Herald reports.
- News (16 Nov): Adebayo (hip) has been ruled out for the remainder of Monday's game against the Rockets, Eric Nehm of The Athletic reports. He'll end with four points (1-3 FG, 0-1 3Pt, 2-4 FT), one rebound, two assists and two steals in 16 minutes.
- **Research:** _pending_

### Julius Randle (BKN, PF, Dr White Slong)

- Rate **37.8** · season 35.2 (13) · L7 41.7 (3) · L15 35.9 (7) · L30 35.2 (13) · projected 37.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Randle exited Monday's game against the 76ers during the fourth quarter to get stitches in his mouth but returned with 5:01 remaining in the period, Chris Hine of The Philly Inquirer reports."
- News (16 Nov): Randle collected 33 points (13-20 FG, 2-4 3Pt, 5-5 FT), six rebounds, one assist, two steals and one block in 33 minutes during Monday's 135-123 loss to the 76ers.
- News (16 Nov): Randle exited Monday's game against the 76ers during the fourth quarter to get stitches in his mouth but returned with 5:01 remaining in the period, Chris Hine of The Philly Inquirer reports.
- **Research:** _pending_

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **35.3** · season 36.0 (12) · L7 34.3 (3) · L15 32.9 (7) · L30 36.0 (12) · projected 45.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Embiid (foot) is questionable for Monday's game against the Nets."
- News (16 Nov): Embiid provided 37 points (13-22 FG, 2-4 3Pt, 9-10 FT), five rebounds, one assist, one steal and two blocks in 32 minutes during Monday's 135-123 win over the Nets.
- News (16 Nov): Embiid (foot) is available for Monday's game against Brooklyn.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-17 21:18 UTC.
