# News watch: 22 Nov 2026

- Generated 2026-11-23 04:12 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 45 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jalen Suggs | role | 30 | 2026-11-22 | [link](https://www.cbssports.com/fantasy/basketball/news/magics-jalen-suggs-hot-shooting-not-enough-in-loss/) | in force |
| Tyrese Proctor | role | 27 | 2026-11-22 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylon-tyson-ankle-out-wednesday-vs-grizzlies) | in force |
| Jalen Duren | return | 2026-11-24 | — | [link](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html) | in force |
| Daniss Jenkins | role | 37 | 2026-11-23 | [link](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-pours-in-25-points/) | in force |
| Aday Mara | role | 27 | 2026-12-05 | [link](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) | in force |
| Maxime Raynaud | return | 2026-11-25 | — | [link](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/) | in force |
| Dejounte Murray | return | 2026-11-26 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf) | in force |
| Scotty Pippen Jr. | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html) | in force |
| Mo Bamba | role | 20 | 2026-11-27 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jusuf-nurkic-toe-to-be-re-evaluated-in-one-week) | in force |
| Jaxson Hayes | role | 26 | 2026-11-27 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jazz-start-keyonte-darryn-green-ace-hayes) | in force |
| Kevin Huerter | role | 35 | 2026-11-24 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kevin-huerter-scores-20-points-as-starter) | in force |
| Jusuf Nurkic | return | 2026-11-28 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) | in force |
| Ja Morant | return | 2026-11-28 | — | [link](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Kevin Huerter** | DET | us | role, minutes | 22.2 | 28.7 | active |
| **Jalen Smith** | CHI | us | minutes, rest | 45.7 | — | active |
| **Trey Murphy III** | NO | us | minutes, rest | 37.3 | — | day-to-day, ESPN est. 23 Nov |
| **Daniss Jenkins** | DET | us | minutes | 32.7 | 36.7 | active |
| **Cade Cunningham** | DET | us | rest | 46.0 | — | active |
| **Anthony Black** | ORL | us | rest | 37.5 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury | 36.7 | — | out, ESPN est. 29 Nov |
| **Norman Powell** | CHI | waivers | injury | 32.9 | — | out, ESPN est. 28 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 25 Nov |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 23.4 | 24.0 | out, ESPN est. 27 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury, gap | 14.8 | — | out, ESPN est. 25 Nov |
| **Bennedict Mathurin** | NO | free agent | injury | 8.3 | — | out, ESPN est. 27 Nov |
| **Grayson Allen** | CHA | free agent | role | 29.2 | 29.7 | out, ESPN est. 25 Nov |
| **Jakob Poeltl** | TOR | free agent | role | 28.4 | — | active |
| **Ryan Rollins** | MIL | free agent | role, rest | 26.9 | — | active |
| **Pelle Larsson** | MIA | free agent | role | 26.7 | 21.9 | active |
| **Nic Claxton** | CHI | free agent | role | 23.7 | 32.7 | out, ESPN est. 23 Nov |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 20.6 | 25.8 | out, ESPN est. 23 Nov |
| **Quentin Grimes** | LAL | free agent | minutes | 35.3 | 31.0 | active |
| **Saddiq Bey** | NO | waivers | minutes | 34.5 | 38.6 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 31.6 | 26.1 | out, ESPN est. 13 Dec |
| **Neemias Queta** | BOS | free agent | minutes, rest | 30.6 | 34.0 | active |
| **P.J. Washington** | DAL | free agent | minutes | 30.1 | 23.4 | out, ESPN est. 24 Nov |
| **Daniel Gafford** | DAL | free agent | minutes | 28.3 | 35.4 | active |
| **Dean Wade** | PHI | free agent | minutes | 28.1 | 27.1 | day-to-day, ESPN est. 23 Nov |
| **Myles Turner** | MIL | free agent | rest | 27.8 | — | active |
| **Ja Morant** | POR | free agent | gap | 31.1 | — | out, ESPN est. 01 Dec |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 03 Dec |
| **Evan Mobley** | CLE | Matt Wright's Foxies | injury, gap | 34.8 | — | out, ESPN est. 29 Nov |
| **Aday Mara** | OKC | Snow Time Lakers | role | 39.4 | — | out, ESPN est. 23 Nov |
| **Dyson Daniels** | ATL | Snow Time Lakers | minutes | 45.9 | 50.1 | active |
| **Darryn Peterson** | UTAH | Matt Wright's Foxies | minutes | 30.0 | 26.4 | active |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | minutes | 27.2 | — | active |
| **Jayson Tatum** | BOS | Snow Time Lakers | rest | 45.3 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 44.4 | — | day-to-day, ESPN est. 23 Nov |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 42.1 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 41.2 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 40.0 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 28.0 | — | active |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | rest | 24.1 | — | day-to-day, ESPN est. 23 Nov |
| **Victor Wembanyama** | SA | Cream Abdul-Yammar | injury | 74.7 | — | active |
| **Karl-Anthony Towns** | NY | Melbourne poopoo | injury | 58.4 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 56.8 † | — | out, ESPN est. 29 Nov |
| **Tyrese Maxey** | PHI | Team Nic Kerr | injury | 43.5 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 23.0 (1) → — · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, us)

- Rate **22.2** · role rate 28.7 · season 22.3 (16) · L7 16.5 (4) · L15 28.4 (8) · L30 23.2 (15) · projected 22.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 14 before; 34.5 min in his starts, against 26.9 for the season
- **Minutes:** 34.0 min over his last 3 games against 26.9 for the season (+7.1)
- News (21 Nov): Huerter chipped in 20 points (7-15 FG, 4-8 3Pt, 2-3 FT), three rebounds, three assists and one steal across 36 minutes during Friday's 105-102 loss to Toronto.
- News (19 Nov): Huerter had 11 points (2-9 FG, 1-4 3Pt, 6-7 FT), one rebound, seven assists, one block and one steal across 36 minutes during Wednesday's 122-109 victory over New Orleans.
- **Research:** _pending_

### Jalen Smith (CHI, PF/C, us)

- Rate **45.7** · season 37.9 (14) → 40.0 (13) · L7 52.3 (3) · L15 49.2 (6) · L30 38.3 (13) → 40.7 (12) · projected 22.4
- ESPN: active
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (22 Nov): Smith (illness) is available for Sunday's game against the Nuggets.
- News (22 Nov): Smith (illness) has been upgraded to probable for Sunday's game against the Nuggets.
- **Research:** _pending_

### Trey Murphy III (NO, SG/SF, us)

- Rate **37.3** · season 31.7 (10) · L7 38.0 (1) · L15 41.0 (2) · L30 33.4 (9) · projected 36.8
- ESPN: day-to-day, ESPN est. 23 Nov (Knee, updated 2026-11-22)
- **Minutes:** news on 21 Nov: "Expect his minutes to ramp up quickly, and once he's fully back, he should rejoin a starting lineup that has struggled to find consistent scoring."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 21 Nov: "He'll sit for the second leg of a back-to-back set, which means more minutes will be available for Jordan Poole, Herbert Jones and Derik Queen."
- News (22 Nov): Murphy (knees) is listed as probable for Monday's game against the Suns.
- News (21 Nov): Murphy (knee) has been ruled out for Saturday's game against the Spurs.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, us)

- Rate **32.7** · role rate 36.7 · season 29.7 (16) · L7 32.8 (4) · L15 38.6 (8) · L30 30.9 (15)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 30.4 for the season (+7.2)
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- **Research:** _pending_

### Cade Cunningham (DET, PG, us)

- Rate **46.0** · season 48.8 (15) · L7 39.0 (3) · L15 48.7 (7) · L30 49.5 (14) · projected 50.4
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Cunningham's status is uncertain for the second half of Detroit's back-to-back set after he played 37 minutes in Tuesday's win over San Antonio."; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (22 Nov): Cunningham (knee) is available for Sunday's game against the Hawks.
- News (21 Nov): Cunningham (knee) is probable to play Sunday in Atlanta.
- **Research:** _pending_

### Anthony Black (ORL, PG/SG, us)

- Rate **37.5** · season 37.8 (13) · L7 36.5 (4) · L15 40.1 (8) · L30 37.8 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- News (19 Nov): Black totaled 15 points (6-16 FG, 2-5 3Pt, 1-3 FT), two rebounds, six assists, one block and one steal in 37 minutes during Wednesday's 121-116 loss to the 76ers.
- **Research:** _pending_

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:** _pending_

### Norman Powell (CHI, SG/SF, waivers)

- Rate **32.9** · season 30.1 (13) → 32.2 (12) · L7 30.3 (3) · L15 36.2 (5) · L30 30.7 (12) → 33.1 (11) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:** _pending_

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **23.4** · role rate 24.0 · season 30.6 (9) · L7 — · L15 13.7 (3) · L30 27.4 (8) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:** _pending_

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **14.8** · season 14.2 (5) · L7 — · L15 — · L30 11.0 (4) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:** _pending_

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.3** · season 8.8 (12) · L7 — · L15 3.7 (3) · L30 7.6 (11) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **29.2** · role rate 29.7 · season 26.8 (13) · L7 26.0 (1) · L15 36.0 (3) · L30 26.4 (12) · projected 26.6
- ESPN: out, ESPN est. 25 Nov (Concussion, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (22 Nov): Allen (concussion) has been ruled out for Monday's game against the Grizzlies.
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- **Research:** _pending_

### Jakob Poeltl (TOR, C, free agent)

- Rate **28.4** · season 26.4 (14) · L7 28.5 (4) · L15 29.7 (7) · L30 27.2 (13) · projected 31.7
- ESPN: active
- **Role:** news on 18 Nov: "Poeltl will start Wednesday's game against the Wizards."
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:** _pending_

### Ryan Rollins (MIL, PG/SG, free agent)

- Rate **26.9** · season 24.0 (15) · L7 28.5 (2) · L15 25.5 (6) · L30 24.4 (14) · projected 31.9
- ESPN: active
- **Role:** news on 21 Nov: "Rollins is in the starting lineup for Saturday's game against the 76ers."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 19 Nov: "Rollins is off the injury report after missing back-to-back contests with an illness."
- News (21 Nov): Rollins provided eight points (4-9 FG, 0-1 3Pt), six rebounds, one assist and one block in 28 minutes during Saturday's 132-129 loss to Philadelphia.
- News (21 Nov): Rollins is in the starting lineup for Saturday's game against the 76ers.
- **Research:** _pending_

### Pelle Larsson (MIA, SG/SF, free agent)

- Rate **26.7** · role rate 21.9 · season 25.5 (13) · L7 27.5 (2) · L15 27.8 (4) · L30 26.0 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 11 before; 24.5 min in his starts, against 28.5 for the season
- News (19 Nov): Larsson ended with four points (1-2 FG, 1-2 3Pt, 1-2 FT), two rebounds, two assists and one steal across 15 minutes during Wednesday's 137-130 victory over the Bucks.
- News (17 Nov): Larsson (illness) is available for Wednesday's game against Milwaukee, Ira Winderman of the South Florida Sun Sentinel reports.
- **Research:** _pending_

### Nic Claxton (CHI, C, free agent)

- Rate **23.7** · role rate 32.7 · season 23.3 (6) · L7 22.3 (3) · L15 23.3 (6) · L30 23.3 (6) · projected 30.3
- ESPN: out, ESPN est. 23 Nov (Illness, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 0 of 4 before; 29.0 min in his starts, against 20.7 for the season
- **Role:** news on 20 Nov: "Claxton will start Friday's game against Washington, K.C."
- News (22 Nov): Claxton (illness) won't play in Sunday's game against the Nuggets.
- News (22 Nov): Claxton (illness) is questionable to play in Sunday's game against the Nuggets.
- **Research:** _pending_

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **20.6** · role rate 25.8 · season 19.2 (8) · L7 — · L15 20.3 (3) · L30 19.4 (7) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-22)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (22 Nov): Tyson (ankle) is probable for Monday's game against the Bulls.
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **35.3** · role rate 31.0 · season 24.1 (15) · L7 44.8 (4) · L15 40.0 (5) · L30 23.8 (14) · projected 28.1
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 29.1 for the season (+8.3)
- News (21 Nov): Grimes logged 13 points (2-7 FG, 1-5 3Pt, 8-9 FT), five rebounds and seven assists in 35 minutes during Friday's 106-104 victory over the Kings.
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, waivers)

- Rate **34.5** · role rate 38.6 · season 29.4 (18) → 31.1 (17) · L7 29.5 (4) → 39.0 (3) · L15 29.3 (9) → 32.9 (8) · L30 30.2 (17) → 32.1 (16) · projected 25.9
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.0 for the season (+7.3)
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **31.6** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 37.2 (9) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Neemias Queta (BOS, C, free agent)

- Rate **30.6** · role rate 34.0 · season 27.2 (16) · L7 32.5 (4) · L15 31.3 (7) · L30 27.7 (15) · projected 27.2
- ESPN: active
- **Minutes:** 29.0 min over his last 3 games against 23.2 for the season (+5.8)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (22 Nov): Queta notched 15 points (5-9 FG, 1-1 3Pt, 4-10 FT), seven rebounds, one assist and two blocks over 30 minutes during Saturday's 97-96 loss to the Kings.
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:** _pending_

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **30.1** · role rate 23.4 · season 28.2 (15) · L7 35.5 (2) · L15 25.0 (6) · L30 29.2 (14) · projected 26.9
- ESPN: out, ESPN est. 24 Nov (Illness, updated 2026-11-22)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (22 Nov): Washington (illness) has been ruled out for Sunday's game against the Jazz.
- News (22 Nov): Washington (illness) is doubtful to play Sunday's game against the Jazz.
- **Research:** _pending_

### Daniel Gafford (DAL, C, free agent)

- Rate **28.3** · role rate 35.4 · season 28.4 (17) · L7 29.2 (4) · L15 26.5 (8) · L30 29.2 (16) · projected 29.3
- ESPN: active
- **Minutes:** 27.7 min over his last 3 games against 22.2 for the season (+5.4)
- News (15 Nov): Gafford (shoulder) is available for Sunday's game against Boston.
- News (15 Nov): Gafford (shoulder) is probable to play in Sunday's game against the Celtics.
- **Research:** _pending_

### Dean Wade (PHI, PF, free agent)

- Rate **28.1** · role rate 27.1 · season 21.5 (13) · L7 39.5 (2) · L15 24.6 (5) · L30 21.5 (13) · projected 16.3
- ESPN: day-to-day, ESPN est. 23 Nov (Left Hamstring Soreness, updated 2026-11-22)
- **Minutes:** 33.7 min over his last 3 games against 26.7 for the season (+7.0)
- News (22 Nov): Wade (hamstring) is listed as probable for Monday's game against Portland.
- News (20 Nov): Wade (hamstring) won't play Saturday against the Bucks.
- **Research:** _pending_

### Myles Turner (MIL, C, free agent)

- Rate **27.8** · season 27.2 (15) · L7 29.7 (3) · L15 26.0 (6) · L30 27.4 (14) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- News (20 Nov): Turner (shoulder) is off the injury report for Saturday's game against the 76ers.
- **Research:** _pending_

### Ja Morant (POR, PG, free agent)

- Rate **31.1** · season 33.8 (4) · L7 — · L15 — · L30 27.7 (3) · projected 37.5
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

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **34.8** · season 39.9 (12) · L7 — · L15 25.3 (3) · L30 40.7 (11) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:** _pending_

### Aday Mara (OKC, C, Snow Time Lakers)

- Rate **39.4** · season 29.5 (16) · L7 47.7 (3) · L15 39.7 (7) · L30 31.7 (14)
- ESPN: out, ESPN est. 23 Nov (Right Lower Leg Bruise, updated 2026-11-22)
- **Role:** news on 20 Nov: "Mara is now listed in the starting lineup for Friday's matchup with the Pelicans, Brandon Rahbar of DailyThunder.com reports."
- News (22 Nov): Mara (shin) is listed as out for Sunday's game versus Miami.
- News (20 Nov): Mara posted 22 points (11-15 FG), 16 rebounds, two assists and two blocks across 29 minutes during Friday's 126-120 win over the Pelicans.
- **Research:** _pending_

### Dyson Daniels (ATL, PG/SG, Snow Time Lakers)

- Rate **45.9** · role rate 50.1 · season 42.9 (17) · L7 48.2 (4) · L15 48.3 (7) · L30 42.6 (16) · projected 35.7
- ESPN: active
- **Minutes:** 37.0 min over his last 3 games against 31.6 for the season (+5.4)
- News (22 Nov): Daniels finished Sunday's 107-97 win over the Pistons with five points (2-9 FG, 0-3 3Pt, 1-2 FT), 14 rebounds, eight assists, five steals and two blocks in 39 minutes.
- News (20 Nov): Daniels posted 11 points (5-10 FG, 1-3 3Pt), 10 assists, eight rebounds and four steals over 35 minutes during the Hawks' 111-97 win over the Hornets on Friday.
- **Research:** _pending_

### Darryn Peterson (UTAH, PG/SG, Matt Wright's Foxies)

- Rate **30.0** · role rate 26.4 · season 31.6 (18) · L7 25.6 (5) · L15 33.1 (9) · L30 32.6 (17) · projected 29.1
- ESPN: active
- **Minutes:** 25.3 min over his last 3 games against 30.3 for the season (−5.0)
- News (21 Nov): Peterson produced 20 points (7-20 FG, 0-7 3Pt, 6-8 FT), 10 rebounds, eight assists, two steals and one block over 32 minutes in Friday's 111-101 loss to the Suns.
- News (19 Nov): Peterson ended Wednesday's 109-97 win over the Lakers with 11 points (3-5 FG, 1-3 3Pt, 4-6 FT), one rebound and three assists over 19 minutes.
- **Research:** _pending_

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **27.2** · season 31.7 (15) · L7 20.8 (4) · L15 29.0 (8) · L30 31.7 (15) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (20 Nov): Podziemski closed with 15 points (5-12 FG, 0-5 3Pt, 5-6 FT), three rebounds, two assists and one steal in 32 minutes during Thursday's 126-98 loss to the Grizzlies.
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- **Research:** _pending_

### Jayson Tatum (BOS, SF/PF, Snow Time Lakers)

- Rate **45.3** · season 46.0 (15) · L7 45.2 (4) · L15 43.6 (7) · L30 47.3 (14) · projected 48.1
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 22 Nov: "Tatum (rest) is not listed on the injury report for Sunday's game against the Warriors, Justin Turpin of WEEI.com reports."
- News (22 Nov): Tatum (rest) is not listed on the injury report for Sunday's game against the Warriors, Justin Turpin of WEEI.com reports.
- News (21 Nov): Tatum (rest) has been ruled out for Saturday's game against the Kings.
- **Research:** _pending_

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **44.4** · season 40.8 (14) · L7 50.5 (2) · L15 40.8 (5) · L30 40.9 (12) · projected 38.6
- ESPN: day-to-day, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-22)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (22 Nov): Brown (hamstring) is listed as probable for Monday's game versus Portland.
- News (20 Nov): Brown (hamstring) went through individual work during Friday's practice, Tony Jones of The Athletic reports.
- **Research:** _pending_

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **42.1** · season 44.9 (16) · L7 38.3 (3) · L15 42.7 (6) · L30 44.4 (15) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Kessler will return to action after being held out of the front end of this back-to-back set."; sat the first night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Kessler notched 15 points (7-11 FG, 1-1 3Pt, 0-2 FT), seven rebounds, two assists, three blocks and one steal in 30 minutes during Friday's 106-104 win over Sacramento.
- News (19 Nov): Kessler notched 10 points (3-7 FG, 4-10 FT), 11 rebounds and one assist in 31 minutes during Wednesday's 109-97 loss to the Jazz.
- **Research:** _pending_

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **41.2** · season 36.3 (16) → 38.5 (15) · L7 36.5 (4) → 47.7 (3) · L15 32.9 (7) → 37.8 (6) · L30 36.0 (15) → 38.4 (14) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (21 Nov): Herro recorded 50 points (15-23 FG, 7-12 3Pt, 13-13 FT), 11 rebounds, seven assists and one steal over 40 minutes during the Bucks' 132-129 loss to the 76ers on Saturday.
- News (20 Nov): Herro totaled 19 points (7-13 FG, 4-7 3Pt, 1-3 FT), four rebounds, three assists and one steal over 31 minutes during Thursday's 124-114 loss to Portland.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.0** · season 39.1 (16) · L7 40.0 (4) · L15 41.0 (8) · L30 38.9 (15) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (22 Nov): Siakam (hip) is available for Sunday's game against the Knicks.
- News (21 Nov): Siakam (hip) is listed as questionable for Sunday's game against New York.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **28.0** · season 31.7 (13) · L7 23.5 (2) · L15 27.8 (6) · L30 31.1 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- News (19 Nov): Nembhard (hip) is questionable for Friday's game in Cleveland.
- **Research:** _pending_

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **24.1** · season 29.5 (16) · L7 15.7 (3) · L15 24.7 (7) · L30 29.0 (15) · projected 38.2
- ESPN: day-to-day, ESPN est. 23 Nov (Right Lower Leg Bruise, updated 2026-11-23)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Fox has been held in check in back-to-back appearances, and he never found a rhythm against Detroit's physical perimeter defense."
- News (22 Nov): Fox is questionable for Monday's game against the Kings due to a right shin contusion, Jared Weiss of The Athletic reports.
- News (22 Nov): Fox racked up five points (1-4 FG, 0-3 3Pt, 3-3 FT), two rebounds and 10 assists across 26 minutes during Saturday's 114-91 win over the Pelicans.
- **Research:** _pending_

## Other rosters: injury flags only

### Victor Wembanyama (SA, C, Cream Abdul-Yammar)

- Rate **74.7** · season 72.2 (17) · L7 79.0 (4) · L15 74.8 (8) · L30 74.0 (16) · projected 60.5
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "Wembanyama (back) is questionable for Monday's game against the Kings, Jared Weiss of The Athletic reports."
- News (22 Nov): Wembanyama (back) is questionable for Monday's game against the Kings, Jared Weiss of The Athletic reports.
- News (21 Nov): Wembanyama finished with 50 points (20-29 FG, 5-11 3Pt, 5-6 FT), 19 rebounds, one assist, four steals and five blocks across 32 minutes in Saturday's 114-91 win over the Pelicans.
- **Research:** _pending_

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **58.4** · season 53.0 (16) → 54.5 (15) · L7 62.8 (4) · L15 60.9 (8) · L30 53.5 (15) → 55.1 (14) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "Towns (illness) is questionable to play in Sunday's game against the Pacers."
- News (22 Nov): Towns (illness) is available to play in Sunday's game against Indiana, Jared Schwartz of the New York Post reports.
- News (22 Nov): Towns (illness) is questionable to play in Sunday's game against the Pacers.
- **Research:** _pending_

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 29.0 (1) → — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

### Tyrese Maxey (PHI, PG/SG, Team Nic Kerr)

- Rate **43.5** · season 45.6 (16) · L7 40.7 (3) · L15 43.5 (6) · L30 43.8 (14) · projected 45.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 21 Nov: "Maxey (foot) will be a true game-time decision for Saturday's game against the Bucks, head coach Nick Nurse told Ky Carlin of USA Today."
- News (21 Nov): Maxey produced 17 points (4-11 FG, 0-3 3Pt, 9-10 FT), four rebounds, four assists and one block in 36 minutes during Saturday's 132-129 victory over the Bucks.
- News (21 Nov): Maxey (foot) is available for Saturday's game against the Bucks, Austin Krell of OnPattison.com reports.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-23 04:12 UTC.
