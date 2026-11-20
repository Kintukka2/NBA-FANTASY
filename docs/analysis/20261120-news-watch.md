# News watch: 19 Nov 2026

- Generated 2026-11-20 03:47 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 53 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 37 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Jalen Duren | return | 2026-11-23 | — | [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) | in force |
| Scotty Pippen Jr. | return | 2026-11-22 | — | [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html) | in force |
| Dejounte Murray | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) | in force |
| Saddiq Bey | role | 34 | 2026-11-24 | [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/) | in force |
| Daniss Jenkins | role | 35 | 2026-11-22 | [link](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html) | in force |
| Jalen Suggs | role | 25 | 2026-11-22 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter) | in force |
| Trey Murphy III | sit | 2026-11-18 | — | [link](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-another-absence-coming-539612) | expired: remove it |
| Quentin Grimes | role | 35 | 2026-11-17 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/austin-reaves-heel-remains-out-vs-charlotte) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Scottie Barnes** | TOR | us | injury | 48.0 | — | active |
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Saddiq Bey** | NO | us | role, minutes | 34.8 | 36.0 | active |
| **Kel'el Ware** | MIL | us | role | 23.9 | 30.2 | active |
| **Cade Cunningham** | DET | us | minutes | 57.2 | 58.9 | day-to-day, ESPN est. 20 Nov |
| **Daniss Jenkins** | DET | us | minutes | 33.8 | 37.8 | active |
| **Yves Missi** | NO | us | minutes | 27.6 | — | active |
| **Jalen Smith** | CHI | us | rest | 42.2 | — | active |
| **Paul George** | BOS | us | rest | 36.3 | — | active |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 25 Nov |
| **Robert Williams III** | POR | free agent | injury | 23.2 | — | out, ESPN est. 21 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury | 16.3 | — | out, ESPN est. 25 Nov |
| **Jalen Suggs** | ORL | free agent | role, minutes | 35.8 | — | active |
| **Quentin Grimes** | LAL | free agent | role, minutes | 35.2 | 30.8 | active |
| **Mo Bamba** | UTAH | waivers | role, minutes | 34.3 | 44.6 | active |
| **Aday Mara** | OKC | free agent | role | 31.4 | — | active |
| **Tyrese Proctor** | CLE | free agent | role, minutes | 28.8 | 31.2 | active |
| **Grayson Allen** | CHA | free agent | role | 28.6 | 29.7 | out, ESPN est. 23 Nov |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 23.1 | 25.8 | out, ESPN est. 23 Nov |
| **Kasparas Jakucionis** | MIL | free agent | minutes | 28.7 | 26.3 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 28.0 | 26.1 | out, ESPN est. 13 Dec |
| **P.J. Washington** | DAL | free agent | minutes | 27.6 | 23.4 | active |
| **Dejounte Murray** | NO | free agent | minutes, gap | 27.2 | 24.0 | out, ESPN est. 27 Nov |
| **T.J. McConnell** | IND | free agent | minutes | 25.1 | — | day-to-day, ESPN est. 20 Nov |
| **Precious Achiuwa** | SAC | free agent | minutes | 13.5 | 19.8 | day-to-day, ESPN est. 20 Nov |
| **Neemias Queta** | BOS | free agent | rest | 32.1 | — | active |
| **Ja Morant** | POR | free agent | gap | 34.1 | — | out, ESPN est. 01 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 42.4 | — | out, ESPN est. 23 Nov |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | minutes | 28.0 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | minutes | 24.6 | 22.6 | active |
| **Cooper Flagg** | DAL | Matt Wright's Foxies | rest | 46.8 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 43.0 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 40.4 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 25.9 | — | day-to-day, ESPN est. 20 Nov |
| **Jalen Brunson** | NY | Melbourne poopoo | injury | 46.2 | — | active |
| **Brandon Ingram** | LAC | Melbourne poopoo | injury | 36.5 | — | out, ESPN est. 21 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 29 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Scottie Barnes (TOR, SG/SF, us)

- Rate **48.0** · season 46.5 (10) → 50.3 (9) · L7 49.0 (2) · L15 44.0 (3) · L30 46.5 (10) → 50.3 (9) · projected 43.7
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 18 Nov: "Barnes (injury management) has been ruled out for Wednesday's game against Washington, Esfandiar Baraheni of The Athletic reports."
- News (19 Nov): Barnes (groin) will play in Friday's game against the Pistons, Blake Murphy of Sportsnet.ca reports.
- News (18 Nov): Barnes (injury management) has been ruled out for Wednesday's game against Washington, Esfandiar Baraheni of The Athletic reports.
- **Research:** _pending_

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, us)

- Rate **34.8** · role rate 36.0 · season 30.4 (16) · L7 41.0 (4) · L15 33.0 (9) · L30 30.4 (16) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 14 before; 35.0 min in his starts, against 29.6 for the season
- **Minutes:** 38.7 min over his last 3 games against 29.6 for the season (+9.1)
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- News (17 Nov): Bey finished with 23 points (8-15 FG, 5-8 3Pt, 2-2 FT), six rebounds, three assists, one steal and one block across 33 minutes in Monday's 115-94 win over Golden State.
- **Research:** _pending_

### Kel'el Ware (MIL, C, us)

- Rate **23.9** · role rate 30.2 · season 22.9 (16) · L7 26.8 (4) · L15 19.3 (9) · L30 22.9 (16) · projected 33.8
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 14 before; 24.5 min in his starts, against 18.6 for the season
- News (19 Nov): Ware is starting Thursday's game against Portland.
- News (13 Nov): Ware won't start Friday's game against the Magic.
- **Research:** _pending_

### Cade Cunningham (DET, PG, us)

- Rate **57.2** · role rate 58.9 · season 50.7 (13) · L7 66.7 (3) · L15 54.5 (6) · L30 50.7 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 20 Nov (Right Knee Soreness, updated 2026-11-19)
- **Minutes:** 40.7 min over his last 3 games against 35.0 for the season (+5.7)
- News (19 Nov): Cunningham (knee) is expected to play in Friday's game against the Raptors, Blake Murphy of Sportsnet.ca reports.
- News (18 Nov): Cunningham (knee) won't play in Wednesday's game against New Orleans.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, us)

- Rate **33.8** · role rate 37.8 · season 30.5 (14) · L7 36.5 (4) · L15 38.0 (7) · L30 30.5 (14)
- ESPN: active
- **Minutes:** 36.3 min over his last 3 games against 29.3 for the season (+7.0)
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- News (18 Nov): Jenkins closed Tuesday's 105-93 win over the Spurs with 25 points (11-21 FG, 3-7 3Pt), five rebounds, five assists and one steal over 38 minutes.
- **Research:** _pending_

### Yves Missi (NO, C, us)

- Rate **27.6** · season 32.0 (5) · L7 25.7 (3) · L15 25.7 (3) · L30 32.0 (5) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:** _pending_

### Jalen Smith (CHI, PF/C, us)

- Rate **42.2** · season 36.1 (13) → 38.3 (12) · L7 45.7 (3) · L15 40.7 (6) → 46.8 (5) · L30 36.1 (13) → 38.3 (12) · projected 22.4
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (19 Nov): Smith recorded 14 points (6-11 FG, 2-5 3Pt), six rebounds, three assists and one steal in 21 minutes during Wednesday's 137-107 win over the Nets.
- News (17 Nov): Smith (head) isn't listed on the injury report for Wednesday's game against Brooklyn.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **36.3** · season 40.2 (13) · L7 32.0 (3) · L15 36.7 (7) · L30 40.2 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (19 Nov): George supplied 10 points (3-12 FG, 1-7 3Pt, 3-3 FT), four rebounds, one assist, one block and three steals across 23 minutes before fouling out of Wednesday's 105-101 loss to Denver.
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- **Research:** _pending_

## Free agents and waivers

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:** _pending_

### Robert Williams III (POR, C, free agent)

- Rate **23.2** · season 24.4 (12) · L7 19.7 (3) · L15 25.1 (7) · L30 24.4 (12) · projected 26.9
- ESPN: out, ESPN est. 21 Nov (Rest, updated 2026-11-18)
- **Injury:** ESPN est. 21 Nov (Out, Rest, updated 18 Nov), but the news said on 17 Nov: "For the season, Williams has averaged 6.5 points, 6.5 rebounds and 1.1 blocks per contest in 11 games while shooting 63.3 percent from the floor."
- News (18 Nov): Williams (rest) is listed as out for Thursday's game versus the Bucks.
- News (18 Nov): Williams chipped in six points (2-2 FG, 2-2 FT), eight rebounds and four assists across 16 minutes during Tuesday's 106-105 loss to Minnesota.
- **Research:** _pending_

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **16.3** · season 14.2 (5) · L7 — · L15 — · L30 14.2 (5) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:** _pending_

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **35.8** · season 26.7 (6) → 31.2 (5) · L7 27.0 (3) → 38.5 (2) · L15 27.0 (3) → 38.5 (2) · L30 26.7 (6) → 31.2 (5) · projected 29.2
- ESPN: active
- **Role:** news on 16 Nov: "Suggs will start Monday's game against the Celtics."
- **Minutes:** news on 17 Nov: "His presence is key for the Magic, meaning his playing time should continue to ramp up over the next few games."
- News (19 Nov): Suggs registered 18 points (5-10 FG, 5-6 3Pt, 3-6 FT), eight rebounds, four assists, one block and two steals over 31 minutes during Wednesday's 121-116 loss to the 76ers.
- News (17 Nov): Suggs accumulated 12 points (5-8 FG, 2-4 3Pt), six rebounds, four assists and two blocks across 25 minutes during Monday's 115-105 win over the Celtics.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **35.2** · role rate 30.8 · season 24.0 (14) · L7 51.0 (3) · L15 31.8 (6) · L30 24.0 (14) · projected 28.1
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 12 before; 36.8 min in his starts, against 28.6 for the season
- **Role:** news on 15 Nov: "Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports."
- **Minutes:** 38.0 min over his last 3 games against 28.6 for the season (+9.4)
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- News (18 Nov): Grimes closed with 47 points (16-24 FG, 10-14 3Pt, 5-6 FT), six rebounds, three assists and one steal across 42 minutes during Tuesday's 118-114 overtime win over the Hornets.
- **Research:** _pending_

### Mo Bamba (UTAH, C, waivers)

- Rate **34.3** · role rate 44.6 · season 31.1 (12) · L7 42.8 (4) · L15 33.1 (8) · L30 31.1 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 30.0 min in his starts, against 20.9 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- **Minutes:** 30.0 min over his last 3 games against 20.9 for the season (+9.1)
- News (18 Nov): Bamba had 15 points (6-7 FG, 1-2 3Pt, 2-2 FT), 10 rebounds, three assists and one block across 31 minutes during Tuesday's 132-107 victory over the Clippers.
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- **Research:** _pending_

### Aday Mara (OKC, C, free agent)

- Rate **31.4** · season 27.1 (15) · L7 34.3 (3) · L15 33.1 (8) · L30 27.1 (15)
- ESPN: active
- **Role:** news on 18 Nov: "Mara will start in Wednesday's game versus Atlanta."
- News (18 Nov): Mara will start in Wednesday's game versus Atlanta.
- News (16 Nov): Mara closed with 16 points (8-11 FG), 13 rebounds and three assists across 26 minutes off the bench during Sunday's 125-103 win over Sacramento.
- **Research:** _pending_

### Tyrese Proctor (CLE, SG, free agent)

- Rate **28.8** · role rate 31.2 · season 22.6 (15) · L7 39.5 (4) · L15 27.7 (9) · L30 22.6 (15)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 27.8 min in his starts, against 20.3 for the season
- **Minutes:** 29.7 min over his last 3 games against 20.3 for the season (+9.3)
- News (17 Nov): Proctor had 17 points (6-13 FG, 2-6 3Pt, 3-5 FT), three rebounds, two assists, two steals and one block over 29 minutes during Monday's 126-115 victory over the Bulls.
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **28.6** · role rate 29.7 · season 26.8 (13) · L7 27.5 (2) · L15 31.6 (5) · L30 26.8 (13) · projected 26.6
- ESPN: out, ESPN est. 23 Nov (Concussion, updated 2026-11-19)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- News (17 Nov): Allen (concussion-like symptoms) has been ruled out for Tuesday's game against the Lakers.
- **Research:** _pending_

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **23.1** · role rate 25.8 · season 19.2 (8) · L7 28.0 (2) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-19)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- News (18 Nov): Tyson (ankle) has been ruled out for Wednesday's game against Memphis.
- **Research:** _pending_

### Kasparas Jakucionis (MIL, PG, free agent)

- Rate **28.7** · role rate 26.3 · season 20.4 (15) · L7 44.7 (3) · L15 22.4 (8) · L30 20.4 (15) · projected 20.2
- ESPN: active
- **Minutes:** 24.7 min over his last 3 games against 19.1 for the season (+5.5)
- News (19 Nov): Jakucionis produced 20 points (6-8 FG, 3-5 3Pt, 5-6 FT), three rebounds, five assists and two steals over 26 minutes during Wednesday's 137-130 loss to Miami.
- News (16 Nov): Jakucionis finished with 25 points (9-16 FG, 4-10 3Pt, 3-3 FT), five rebounds, five assists and three steals across 26 minutes off the bench during Sunday's 113-106 loss to Atlanta.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **28.0** · role rate 26.1 · season 34.9 (10) · L7 — · L15 17.7 (3) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **27.6** · role rate 23.4 · season 28.2 (15) · L7 24.8 (4) · L15 29.8 (8) · L30 28.2 (15) · projected 26.9
- ESPN: active
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (19 Nov): Washington posted 21 points (7-10 FG, 5-7 3Pt, 2-2 FT), five rebounds, two assists, three blocks and one steal over 25 minutes during Wednesday's 116-94 win over the Warriors.
- News (13 Nov): Washington accumulated 10 points (4-7 FG, 1-4 3Pt, 1-1 FT) and three rebounds over 16 minutes during Thursday's 133-94 loss to Minnesota.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **27.2** · role rate 24.0 · season 30.6 (9) · L7 — · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **25.1** · season 22.5 (6) · L7 29.7 (3) · L15 22.5 (6) · L30 22.5 (6) · projected 24.4
- ESPN: day-to-day, ESPN est. 20 Nov (Right Hamstring Strain, updated 2026-11-19)
- **Minutes:** news on 17 Nov: "McConnell's minutes have been steadily ramping up since he made his regular-season debut Nov. 7, and he had his best game yet in Sunday's 131-124 loss to the 76ers, finishing with 12 points, five rebounds, five assists and one steal in 19 minutes off the bench."
- News (19 Nov): McConnell (hamstring) is listed as probable for Friday's game in Cleveland.
- News (18 Nov): McConnell recorded 14 points (7-10 FG), five assists, two rebounds and two steals over 18 minutes during the Packers' 119-104 loss to the Rockets on Wednesday.
- **Research:** _pending_

### Precious Achiuwa (SAC, PF/C, free agent)

- Rate **13.5** · role rate 19.8 · season 25.4 (12) · L7 -3.0 (1) · L15 15.8 (5) · L30 25.4 (12) · projected 24.1
- ESPN: day-to-day, ESPN est. 20 Nov (Left Lower Leg Bruise, updated 2026-11-20)
- **Minutes:** 19.3 min over his last 3 games against 24.8 for the season (−5.5)
- News (19 Nov): Achiuwa is doubtful for Friday's game against the Lakers due to a left lower leg bruise.
- News (18 Nov): Achiuwa (lower leg) is available for Wednesday's game against the Suns.
- **Research:** _pending_

### Neemias Queta (BOS, C, free agent)

- Rate **32.1** · season 27.3 (14) · L7 38.0 (2) · L15 30.4 (7) · L30 27.3 (14) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- News (17 Nov): Queta (rest) is available for Wednesday's game against the Nuggets, Jack Simone of BostonSportsJournal.com reports.
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

- Rate **42.4** · season 40.8 (14) · L7 43.7 (3) · L15 41.9 (7) · L30 40.8 (14) · projected 38.6
- ESPN: out, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-18)
- **Injury:** ESPN est. 23 Nov (Out, Left Hamstring, updated 18 Nov), but the news said on 18 Nov: "Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com."
- News (18 Nov): Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com.
- News (17 Nov): Brown is out for Wednesday's game against the Magic with a left hamstring strain.
- **Research:** _pending_

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **28.0** · season 33.1 (14) · L7 20.5 (4) · L15 30.6 (8) · L30 33.1 (14) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- News (17 Nov): Podziemski recorded 15 points (3-8 FG, 3-7 3Pt, 6-7 FT), six rebounds, three assists, one steal and two blocks across 30 minutes in Monday's 115-94 loss to the Pelicans.
- **Research:** _pending_

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **24.6** · role rate 22.6 · season 29.5 (12) · L7 24.5 (2) · L15 15.8 (4) · L30 29.5 (12) · projected 37.4
- ESPN: active
- **Minutes:** 23.3 min over his last 3 games against 30.5 for the season (−7.2)
- News (18 Nov): Miller amassed 28 points (10-19 FG, 5-12 3Pt, 3-3 FT), two rebounds, four assists and one block in 32 minutes during Tuesday's 118-114 overtime loss to the Lakers.
- News (16 Nov): Miller finished Sunday's 113-105 loss to the Clippers with five points (1-10 FG, 1-6 3Pt, 2-3 FT), four assists, two rebounds and one steal over 24 minutes.
- **Research:** _pending_

### Cooper Flagg (DAL, SF/PF, Matt Wright's Foxies)

- Rate **46.8** · season 51.0 (14) · L7 40.5 (4) · L15 50.8 (8) · L30 51.0 (14) · projected 45.4
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (19 Nov): Flagg chipped in 33 points (11-15 FG, 3-5 3Pt, 8-8 FT), five rebounds, nine assists and four steals across 34 minutes during Wednesday's 116-94 victory over the Warriors.
- News (16 Nov): Flagg contributed 17 points (5-15 FG, 2-6 3Pt, 5-5 FT), three rebounds, four assists, one block and one steal in 27 minutes during Sunday's 131-94 loss to the Celtics.
- **Research:** _pending_

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **43.0** · season 41.8 (12) · L7 45.3 (3) · L15 41.4 (7) · L30 41.8 (12) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "After sitting out the second game of a weekend back-to-back set, Irving returned to action and delivered decent numbers."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 14–15 Nov back-to-back, playing the games either side
- News (19 Nov): Irving supplied 17 points (7-15 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists and two steals over 29 minutes during Wednesday's 116-94 win over Golden State.
- News (17 Nov): Irving (knee) is not listed on the injury report ahead of Wednesday's game against the Warriors.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.4** · season 40.1 (14) · L7 37.3 (3) · L15 44.4 (7) · L30 40.1 (14) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (18 Nov): Siakam chipped in 24 points (10-17 FG, 2-2 3Pt, 2-2 FT), four rebounds, three assists, one block and three steals across 33 minutes during Wednesday's 119-104 loss to the Rockets.
- News (15 Nov): Siakam recorded 31 points (12-19 FG, 0-3 3Pt, 7-8 FT), two rebounds, two assists and one steal across 34 minutes during Sunday's 131-124 loss to Philadelphia.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **25.9** · season 33.2 (11) · L7 12.0 (1) · L15 31.8 (5) · L30 33.2 (11) · projected 28.2
- ESPN: day-to-day, ESPN est. 20 Nov (Left Hip Soreness, updated 2026-11-19)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (19 Nov): Nembhard (hip) is questionable for Friday's game in Cleveland.
- News (18 Nov): Nembhard (hip) won't play in Wednesday's game against the Rockets, Tony East of Forbes.com reports.
- **Research:** _pending_

## Other rosters: injury flags only

### Jalen Brunson (NY, PG, Melbourne poopoo)

- Rate **46.2** · season 41.9 (15) · L7 50.0 (4) · L15 47.6 (8) · L30 41.9 (15) · projected 43.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Brunson exited to the locker room in the first quarter of Thursday's game against Minnesota due to an apparent facial injury, Jared Schwartz of the New York Post reports."
- News (19 Nov): Brunson (face) returned to Thursday's game against the Timberwolves with 2:47 remaining in the first quarter, per the broadcast.
- News (19 Nov): Brunson exited to the locker room in the first quarter of Thursday's game against Minnesota due to an apparent facial injury, Jared Schwartz of the New York Post reports.
- **Research:** _pending_

### Brandon Ingram (LAC, SF/PF, Melbourne poopoo)

- Rate **36.5** · season — · L7 — · L15 — · L30 — · projected 38.5
- ESPN: out, ESPN est. 21 Nov (Right Achilles Surgery, updated 2026-11-18)
- **Injury:** ESPN est. 21 Nov (Out, Right Achilles Surgery, updated 18 Nov), but the news said on 18 Nov: "Ingram was cleared for full-contact work Nov. 6, and he's been playing 5-on-5 for the past couple of weeks."
- News (18 Nov): Ingram (heel/Achilles) will remain on the inactive list for Thursday's game in San Antonio.
- News (12 Nov): Ingram (Achilles) won't play in Friday's game against the Thunder, per Law Murray of The Athletic.
- **Research:** _pending_

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-20 03:47 UTC.
