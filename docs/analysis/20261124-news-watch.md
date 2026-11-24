# News watch: 24 Nov 2026

- Generated 2026-11-24 07:07 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 51 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Matt Wright's Foxies, Dr White Slong). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 40 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Aday Mara | role | 27 | 2026-12-05 | [link](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) | in force |
| Maxime Raynaud | return | 2026-11-25 | — | [link](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/) | in force |
| Kevin Huerter | role | 35 | 2026-11-24 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kevin-huerter-scores-20-points-as-starter) | in force |
| Jusuf Nurkic | return | 2026-11-28 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) | in force |
| Ja Morant | return | 2026-11-28 | — | [link](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) | in force |
| Dejounte Murray | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) | in force |
| Scotty Pippen Jr. | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) | in force |
| Jalen Duren | return | 2026-11-24 | — | [link](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html) | expired: remove it |
| Daniss Jenkins | role | 37 | 2026-11-23 | [link](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-pours-in-25-points/) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury | 44.1 † | — | out, ESPN est. 30 Nov |
| **Paul George** | BOS | us | injury, rest | 39.0 | — | active |
| **Jalen Smith** | CHI | us | minutes | 42.8 | — | active |
| **Trey Murphy III** | NO | us | minutes, rest | 33.7 | — | active |
| **Neemias Queta** | BOS | us | minutes, rest | 31.1 | 34.0 | active |
| **Cade Cunningham** | DET | us | rest | 46.1 | — | day-to-day, ESPN est. 24 Nov |
| **Anthony Black** | ORL | us | rest | 36.7 | — | active |
| **Myles Turner** | MIL | us | rest | 32.7 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury | 36.7 | — | out, ESPN est. 29 Nov |
| **Norman Powell** | CHI | free agent | injury | 33.0 | — | out, ESPN est. 28 Nov |
| **Maxime Raynaud** | SAC | free agent | injury, gap | 28.1 | — | out, ESPN est. 25 Nov |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 22.9 | 24.0 | out, ESPN est. 27 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury, gap | 13.4 | — | out, ESPN est. 25 Nov |
| **Bennedict Mathurin** | NO | free agent | injury | 8.4 | — | out, ESPN est. 27 Nov |
| **Saddiq Bey** | NO | waivers | role, minutes | 34.3 | 40.5 | active |
| **Grayson Allen** | CHA | free agent | role | 31.1 | 29.7 | out, ESPN est. 25 Nov |
| **Pelle Larsson** | MIA | free agent | role | 27.0 | 21.9 | active |
| **Charles Bassey** | GS | free agent | role, minutes | 26.9 | 34.7 | active |
| **P.J. Washington** | DAL | free agent | minutes | 37.4 | 23.4 | day-to-day, ESPN est. 24 Nov |
| **Daniss Jenkins** | DET | waivers | minutes | 32.7 | 36.7 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 31.6 | 26.1 | out, ESPN est. 13 Dec |
| **Jakob Poeltl** | TOR | free agent | minutes | 30.5 | 33.8 | active |
| **Daniel Gafford** | DAL | free agent | minutes | 29.5 | 35.4 | active |
| **Kelly Oubre Jr.** | IND | free agent | minutes | 28.1 | — | active |
| **Rui Hachimura** | LAC | free agent | rest | 28.6 | — | active |
| **Rudy Gobert** | MIN | free agent | rest | 27.9 | — | active |
| **Zach Edey** | MEM | free agent | rest | 27.2 | — | active |
| **T.J. McConnell** | IND | free agent | rest | 20.7 | — | day-to-day, ESPN est. 27 Nov |
| **Ja Morant** | POR | free agent | gap | 31.2 | — | out, ESPN est. 01 Dec |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 03 Dec |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 56.8 † | — | out, ESPN est. 29 Nov |
| **Pascal Siakam** | IND | Matt Wright's Foxies | injury, rest | 40.0 | — | active |
| **Evan Mobley** | CLE | Matt Wright's Foxies | injury, gap | 34.5 | — | out, ESPN est. 29 Nov |
| **Naz Reid** | CHA | Matt Wright's Foxies | minutes | 35.2 | 39.4 | active |
| **Joel Embiid** | PHI | Dr White Slong | rest | 47.7 | — | day-to-day, ESPN est. 25 Nov |
| **Amen Thompson** | HOU | Matt Wright's Foxies | rest | 38.0 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 29.6 | — | active |
| **Derrick White** | BOS | Dr White Slong | rest | 27.7 | — | active |
| **Jonathan Kuminga** | MIN | Dr White Slong | rest | 26.8 | — | active |
| **Karl-Anthony Towns** | NY | Melbourne poopoo | injury | 59.3 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 — · projected 42.2
- ESPN: out, ESPN est. 30 Nov (Right Hamstring Strain, updated 2026-11-23)
- **Injury:** ESPN est. 30 Nov (Out, Right Hamstring Strain, updated 23 Nov), but the news said on 23 Nov: "Duren hasn't played since Oct. 23 due to a right hamstring strain, though he's expected to be re-evaluated soon."
- News (23 Nov): Duren (hamstring) has been ruled out for Tuesday's game against the Magic.
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **39.0** · season 40.6 (14) · L7 38.0 (3) · L15 40.3 (6) · L30 38.7 (12) · projected 38.5
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "George (rest) has been ruled out for Sunday's game against Golden State, Justin Turpin of WEEI.com reports."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports."; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (23 Nov): George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports.
- News (22 Nov): George (rest) has been ruled out for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:** _pending_

### Jalen Smith (CHI, PF/C, us)

- Rate **42.8** · season 37.4 (15) → 39.4 (14) · L7 47.0 (4) · L15 46.6 (7) · L30 36.8 (13) → 39.0 (12) · projected 22.4
- ESPN: active
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- News (23 Nov): Smith (illness) will play Monday against the Cavaliers, K.C. Johnson of Chicago Sports Network reports.
- News (23 Nov): Smith (illness) is probable for Monday's game against Cleveland.
- **Research:** _pending_

### Trey Murphy III (NO, SG/SF, us)

- Rate **33.7** · season 31.1 (11) · L7 31.5 (2) · L15 35.7 (3) · L30 33.8 (9) · projected 36.8
- ESPN: active
- **Minutes:** news on 21 Nov: "Expect his minutes to ramp up quickly, and once he's fully back, he should rejoin a starting lineup that has struggled to find consistent scoring."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "Murphy was deployed off the bench Friday against the Thunder in his first action since Nov. 8 but was then held out Saturday in San Antonio for the second half of a back-to-back in an effort to ease him back into action following a six-game absence due to bilateral patellar tendinopathy."; sat the second night of the 20–21 Nov back-to-back, playing the games either side
- News (24 Nov): Murphy totaled nine points (4-14 FG, 1-6 3Pt), nine rebounds, two assists and two steals across 35 minutes during Monday's 123-119 overtime loss to the Suns.
- News (23 Nov): Murphy is starting Monday's game against Phoenix.
- **Research:** _pending_

### Neemias Queta (BOS, C, us)

- Rate **31.1** · role rate 34.0 · season 27.2 (16) · L7 34.3 (3) · L15 31.3 (7) · L30 27.4 (14) · projected 27.2
- ESPN: active
- **Minutes:** 29.0 min over his last 3 games against 23.2 for the season (+5.8)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (22 Nov): Queta notched 15 points (5-9 FG, 1-1 3Pt, 4-10 FT), seven rebounds, one assist and two blocks over 30 minutes during Saturday's 97-96 loss to the Kings.
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:** _pending_

### Cade Cunningham (DET, PG, us)

- Rate **46.1** · season 48.8 (15) · L7 39.0 (3) · L15 48.7 (7) · L30 50.3 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 24 Nov (Knee, updated 2026-11-23)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (23 Nov): Cunningham (knee) is probable for Tuesday's game against the Orlando.
- News (23 Nov): Cunningham closed Sunday's 107-97 loss to the Hawks with five points (2-9 FG, 1-3 3Pt), four rebounds, 15 assists, one block and one steal in 33 minutes.
- **Research:** _pending_

### Anthony Black (ORL, PG/SG, us)

- Rate **36.7** · season 37.8 (13) · L7 36.5 (4) · L15 37.1 (7) · L30 37.8 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Black chipped in 14 points (5-12 FG, 2-4 3Pt, 2-2 FT), five rebounds, two assists and two steals in 35 minutes during Sunday's 116-96 loss to the Wizards.
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- **Research:** _pending_

### Myles Turner (MIL, C, us)

- Rate **32.7** · season 28.9 (16) · L7 39.3 (3) · L15 30.0 (7) · L30 28.9 (14) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (24 Nov): Turner closed with 27 points (9-12 FG, 5-6 3Pt, 4-5 FT), 11 rebounds, one assist and two blocks over 28 minutes before fouling out of Monday's 116-111 victory over Toronto.
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- **Research:** _pending_

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:** _pending_

### Norman Powell (CHI, SG/SF, free agent)

- Rate **33.0** · season 30.1 (13) → 32.2 (12) · L7 30.3 (3) · L15 36.2 (5) · L30 31.1 (11) → 33.8 (10) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:** _pending_

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.9** · role rate 24.0 · season 30.6 (9) · L7 — · L15 13.7 (3) · L30 25.6 (7) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:** _pending_

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **13.4** · season 14.2 (5) · L7 — · L15 — · L30 8.3 (3) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:** _pending_

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.4** · season 8.8 (12) · L7 — · L15 3.7 (3) · L30 8.2 (10) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, waivers)

- Rate **34.3** · role rate 40.5 · season 29.7 (19) → 31.3 (18) · L7 30.6 (5) → 38.0 (4) · L15 29.9 (10) → 33.1 (9) · L30 30.4 (17) → 32.2 (16) · projected 25.9
- ESPN: active
- **Role:** news on 23 Nov: "Bey is not listed in the starting lineup for Monday's game against the Suns."
- **Minutes:** 39.7 min over his last 3 games against 30.6 for the season (+9.1)
- News (23 Nov): Bey is not listed in the starting lineup for Monday's game against the Suns.
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **31.1** · role rate 29.7 · season 26.8 (13) · L7 — · L15 36.0 (3) · L30 27.3 (11) · projected 26.6
- ESPN: out, ESPN est. 25 Nov (Concussion, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (22 Nov): Allen (concussion) has been ruled out for Monday's game against the Grizzlies.
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- **Research:** _pending_

### Pelle Larsson (MIA, SG/SF, free agent)

- Rate **27.0** · role rate 21.9 · season 25.5 (13) · L7 27.5 (2) · L15 27.8 (4) · L30 27.5 (11)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 11 before; 24.5 min in his starts, against 28.5 for the season
- News (23 Nov): Larsson finished Sunday's 123-113 win over Oklahoma City with 21 points (9-14 FG, 3-7 3Pt), three rebounds, five assists and three steals across 30 minutes.
- News (19 Nov): Larsson ended with four points (1-2 FG, 1-2 3Pt, 1-2 FT), two rebounds, two assists and one steal across 15 minutes during Wednesday's 137-130 victory over the Bucks.
- **Research:** _pending_

### Charles Bassey (GS, C, free agent)

- Rate **26.9** · role rate 34.7 · season 23.3 (15) · L7 31.2 (4) · L15 28.4 (7) · L30 23.3 (15) · projected 14.5
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 23.2 min in his starts, against 15.6 for the season
- **Minutes:** 24.3 min over his last 3 games against 15.6 for the season (+8.7)
- News (23 Nov): Bassey recorded 13 points (6-7 FG, 1-2 FT), nine rebounds, three assists and three steals across 26 minutes during Sunday's 88-87 victory over the Celtics.
- News (20 Nov): Bassey ended with 16 points (6-7 FG, 4-5 FT), 13 rebounds, one assist, two blocks and one steal across 25 minutes during Thursday's 126-98 loss to the Grizzlies.
- **Research:** _pending_

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **37.4** · role rate 23.4 · season 28.2 (15) · L7 58.0 (1) · L15 25.0 (6) · L30 27.8 (13) · projected 26.9
- ESPN: day-to-day, ESPN est. 24 Nov (Illness, updated 2026-11-23)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (23 Nov): Washington (illness) is questionable for Tuesday's game against the Nuggets.
- News (22 Nov): Washington (illness) has been ruled out for Sunday's game against the Jazz.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, waivers)

- Rate **32.7** · role rate 36.7 · season 29.7 (16) · L7 32.8 (4) · L15 38.6 (8) · L30 30.9 (14)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 30.4 for the season (+7.2)
- News (23 Nov): Jenkins logged 11 points (4-12 FG, 1-6 3Pt, 2-2 FT), four rebounds, three assists and one steal over 38 minutes during Sunday's 107-97 loss to the Hawks.
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **31.6** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 37.1 (8) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Jakob Poeltl (TOR, C, free agent)

- Rate **30.5** · role rate 33.8 · season 27.4 (15) · L7 32.5 (4) · L15 31.1 (8) · L30 28.2 (13) · projected 31.7
- ESPN: active
- **Minutes:** 29.7 min over his last 3 games against 24.2 for the season (+5.5)
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:** _pending_

### Daniel Gafford (DAL, C, free agent)

- Rate **29.5** · role rate 35.4 · season 28.4 (17) · L7 32.7 (3) · L15 26.5 (8) · L30 29.5 (15) · projected 29.3
- ESPN: active
- **Minutes:** 27.7 min over his last 3 games against 22.2 for the season (+5.4)
- News (23 Nov): Gafford notched 10 points (5-8 FG), four rebounds, four assists and two steals over 28 minutes during Sunday's 116-114 win over the Jazz.
- News (15 Nov): Gafford (shoulder) is available for Sunday's game against Boston.
- **Research:** _pending_

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **28.1** · season 23.5 (16) · L7 30.0 (4) · L15 30.2 (8) · L30 25.1 (14) · projected 23.2
- ESPN: active
- **Minutes:** news on 24 Nov: "Oubre scored at least 15 points for the sixth straight game, continuing to ramp up after a slow start to the season."
- News (24 Nov): Oubre racked up 20 points (8-13 FG, 4-7 3Pt), four rebounds, two assists and two blocks over 28 minutes during Monday's 125-120 win over Oklahoma City.
- News (23 Nov): Oubre recorded 15 points (4-10 FG, 0-4 3Pt, 7-9 FT) and five rebounds in 27 minutes during Sunday's 113-106 loss to the Knicks.
- **Research:** _pending_

### Rui Hachimura (LAC, SF/PF, free agent)

- Rate **28.6** · season 25.1 (14) · L7 35.0 (4) · L15 26.5 (8) · L30 25.6 (12) · projected 24.0
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (20 Nov): Hachimura contributed 17 points (7-13 FG, 2-4 3Pt, 1-1 FT), seven rebounds, two assists and one steal in 32 minutes during Thursday's 124-112 loss to the Spurs.
- News (18 Nov): Hachimura finished Tuesday's 132-107 loss to the Jazz with 20 points (7-10 FG, 4-4 3Pt, 2-4 FT), five rebounds, one assist, one block and one steal over 27 minutes.
- **Research:** _pending_

### Rudy Gobert (MIN, C, free agent)

- Rate **27.9** · season 26.7 (17) · L7 27.4 (5) · L15 26.9 (8) · L30 27.6 (15) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (21 Nov): Gobert accumulated seven points (2-2 FG, 3-4 FT), 11 rebounds, two assists, three blocks and one steal over 32 minutes during Saturday's 104-95 victory over the Grizzlies.
- News (20 Nov): Gobert posted nine points (4-6 FG, 1-2 FT), seven rebounds and two steals over 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:** _pending_

### Zach Edey (MEM, C, free agent)

- Rate **27.2** · season 24.9 (14) · L7 30.0 (4) · L15 24.7 (6) · L30 23.3 (12) · projected 33.2
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the first night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (20 Nov): Edey (hip) is not listed on the injury report ahead of Saturday's game versus Minnesota.
- News (19 Nov): Edey (hip) has been ruled out for Thursday's game against the Warriors.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **20.7** · season 20.0 (7) · L7 20.0 (2) · L15 21.2 (6) · L30 20.0 (7) · projected 24.4
- ESPN: day-to-day, ESPN est. 27 Nov (Left Hamstring, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "The veteran floor general is missing both ends of this back-to-back set, but he'll have some extra time to heal up ahead of Friday's tilt against the 76ers."
- News (23 Nov): McConnell is out for Monday's game against the Thunder due to left hamstring soreness.
- News (21 Nov): McConnell (hamstring) is listed as out for Sunday's game in New York.
- **Research:** _pending_

### Ja Morant (POR, PG, free agent)

- Rate **31.2** · season 33.8 (4) · L7 — · L15 — · L30 28.0 (2) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:** _pending_

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 03 Dec (Left Calf Strain, updated 2026-11-16)
- **Gap:** listed out, and no news in 5 days (ESPN est. 03 Dec)
- News (16 Nov): Harris (calf) is likely to be sidelined until early December, per Jeff Garcia of KENS 5 San Antonio.
- News (10 Nov): Harris (calf) is out for Wednesday's game against Chicago, Jared Weiss of The Athletic reports.
- **Research:** _pending_

## Opponents: this week and next

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.0** · season 39.1 (17) · L7 39.2 (4) · L15 41.2 (8) · L30 39.9 (15) · projected 41.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 23 Nov: "Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "After carrying a questionable tag ahead of both parts of this back-to-back, Siakam is suiting up Monday despite dealing with a left hip injury."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Siakam (hip) will play in Monday's game against the Thunder, Justin Martinez of The Oklahoman reports.
- News (23 Nov): Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management.
- **Research:** _pending_

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **34.5** · season 39.9 (12) · L7 — · L15 24.5 (2) · L30 40.7 (11) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:** _pending_

### Naz Reid (CHA, PF/C, Matt Wright's Foxies)

- Rate **35.2** · role rate 39.4 · season 31.5 (16) → 32.6 (15) · L7 38.3 (3) · L15 35.8 (6) · L30 31.2 (14) → 32.5 (13) · projected 35.5
- ESPN: active
- **Minutes:** 39.7 min over his last 3 games against 32.8 for the season (+6.9)
- News (20 Nov): Reid logged 12 points (4-19 FG, 2-10 3Pt, 2-4 FT), 10 rebounds, three assists and one block over 39 minutes during the Hornets' 111-97 loss to the Hawks on Friday.
- News (18 Nov): Reid ended Tuesday's 118-114 overtime loss to the Lakers with 23 points (8-18 FG, 4-10 3Pt, 3-4 FT), 11 rebounds, four assists, two blocks and two steals across 41 minutes.
- **Research:** _pending_

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **47.7** · season 39.4 (14) · L7 58.3 (3) · L15 45.0 (6) · L30 39.5 (12) · projected 45.4
- ESPN: day-to-day, ESPN est. 25 Nov (Illness, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov, Tue 01–Wed 02 Dec; sat the second night of the 24–25 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side; sat the first night of the 15–16 Nov back-to-back, playing the games either side
- News (23 Nov): Embiid (illness) is out for Monday's game against Portland, Austin Krell of OnPattison.com reports.
- News (23 Nov): Embiid (knee) has been downgraded to questionable for Monday's game against Portland.
- **Research:** _pending_

### Amen Thompson (HOU, SG/SF, Matt Wright's Foxies)

- Rate **38.0** · season 37.1 (17) · L7 37.3 (3) · L15 39.9 (7) · L30 35.1 (15) · projected 40.0
- ESPN: active
- **Rest:** back-to-back Mon 30–Tue 01 Dec; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (21 Nov): Thompson chipped in 22 points (10-12 FG, 0-1 3Pt, 2-6 FT), six rebounds and one steal in 26 minutes during Friday's 133-124 loss to the Nuggets.
- News (18 Nov): Thompson recorded 15 points (6-11 FG, 0-1 3Pt, 3-4 FT), nine rebounds, three assists, one steal and one block over 31 minutes during the Rockets' 119-104 win over the Pacers on Wednesday.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **29.6** · season 31.8 (14) · L7 26.7 (3) · L15 29.5 (6) · L30 31.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Nembhard produced 16 points (5-13 FG, 2-3 3Pt, 4-7 FT), two rebounds and eight assists in 32 minutes during Sunday's 113-106 loss to the Knicks.
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- **Research:** _pending_

### Derrick White (BOS, PG/SG, Dr White Slong)

- Rate **27.7** · season 29.9 (16) · L7 22.0 (3) · L15 29.6 (7) · L30 29.4 (14) · projected 37.0
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 21 Nov: "The veteran guard will be in street clothes for the first leg of the Celtics' back-to-back set, but he could make his return Sunday against the Warriors."; sat the first night of the 21–22 Nov back-to-back, playing the games either side
- News (23 Nov): White amassed 14 points (6-21 FG, 2-12 3Pt), three rebounds, five assists and one steal over 32 minutes during Sunday's 88-87 loss to the Warriors.
- News (22 Nov): White (shoulder) is not listed on the injury report for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:** _pending_

### Jonathan Kuminga (MIN, SF/PF, Dr White Slong)

- Rate **26.8** · season 28.7 (17) · L7 28.8 (4) · L15 23.4 (7) · L30 27.8 (15) · projected 26.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 16–17 Nov back-to-back, playing the games either side
- News (19 Nov): Kuminga totaled 23 points (7-13 FG, 2-4 3Pt, 7-7 FT), three rebounds, three assists and three blocks in 35 minutes during Thursday's 102-99 loss to the Knicks.
- News (19 Nov): Kuminga (shoulder) is available for Thursday's game against New York.
- **Research:** _pending_

## Other rosters: injury flags only

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **59.3** · season 53.0 (16) → 54.5 (15) · L7 65.3 (3) · L15 60.0 (7) · L30 54.3 (14) → 56.2 (13) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "Towns (illness) is questionable to play in Sunday's game against the Pacers."
- News (22 Nov): Towns posted 30 points (9-14 FG, 4-4 3Pt, 8-12 FT), 13 rebounds, five assists, three steals and two blocks in 29 minutes during Sunday's 113-106 win over the Pacers.
- News (22 Nov): Towns (illness) is available to play in Sunday's game against Indiana, Jared Schwartz of the New York Post reports.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-24 07:07 UTC.
