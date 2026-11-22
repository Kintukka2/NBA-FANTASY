# News watch: 22 Nov 2026

- Generated 2026-11-22 07:27 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 51 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 40 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
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
| **Jalen Smith** | CHI | us | minutes, rest | 43.0 | — | day-to-day, ESPN est. 22 Nov |
| **Saddiq Bey** | NO | us | minutes | 33.8 | 38.6 | active |
| **Daniss Jenkins** | DET | us | minutes | 33.3 | 37.8 | active |
| **Cade Cunningham** | DET | us | rest | 50.1 | — | day-to-day, ESPN est. 22 Nov |
| **Anthony Black** | ORL | us | rest | 38.6 | — | active |
| **Paul George** | BOS | us | rest | 37.1 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury | 36.7 | — | out, ESPN est. 29 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 25 Nov |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 23.8 | 24.0 | out, ESPN est. 27 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury, gap | 14.8 | — | out, ESPN est. 25 Nov |
| **Bennedict Mathurin** | NO | free agent | injury | 8.1 | — | out, ESPN est. 27 Nov |
| **Brayden Burries** | MIL | free agent | role | 30.1 | — | active |
| **Jaxson Hayes** | UTAH | free agent | role, rest | 29.7 | — | active |
| **Jakob Poeltl** | TOR | free agent | role | 29.4 | — | active |
| **Kevin Huerter** | DET | free agent | role, minutes | 28.4 | 32.2 | active |
| **Derik Queen** | NO | free agent | role | 28.2 | 43.2 | active |
| **Grayson Allen** | CHA | free agent | role | 27.3 | 29.7 | day-to-day, ESPN est. 23 Nov |
| **Payton Pritchard** | BOS | free agent | role | 27.3 | 32.0 | active |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 22.4 | 25.8 | out, ESPN est. 23 Nov |
| **Quentin Grimes** | LAL | free agent | minutes | 33.8 | 31.0 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 31.6 | 26.1 | out, ESPN est. 13 Dec |
| **P.J. Washington** | DAL | free agent | minutes | 29.0 | 23.4 | out, ESPN est. 22 Nov |
| **Dean Wade** | PHI | free agent | minutes | 27.1 | 27.1 | out, ESPN est. 23 Nov |
| **Neemias Queta** | BOS | free agent | rest | 30.9 | — | active |
| **Myles Turner** | MIL | free agent | rest | 27.2 | — | active |
| **Ja Morant** | POR | free agent | gap | 31.1 | — | out, ESPN est. 01 Dec |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 03 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 44.1 | — | out, ESPN est. 23 Nov |
| **Evan Mobley** | CLE | Matt Wright's Foxies | injury, gap | 37.1 | — | out, ESPN est. 29 Nov |
| **Aday Mara** | OKC | Snow Time Lakers | role | 38.4 | — | active |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | minutes | 28.1 | — | active |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 42.2 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 41.5 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 40.5 | — | day-to-day, ESPN est. 22 Nov |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 30.8 | — | active |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | rest | 23.9 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 56.8 † | — | out, ESPN est. 29 Nov |
| **Tyrese Maxey** | PHI | Team Nic Kerr | injury | 43.0 | — | active |
| **Brandon Ingram** | LAC | Melbourne poopoo | injury | 36.5 | — | out, ESPN est. 23 Nov |

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

### Jalen Smith (CHI, PF/C, us)

- Rate **43.0** · season 36.1 (13) → 38.3 (12) · L7 48.0 (2) · L15 46.8 (5) · L30 36.4 (12) → 38.8 (11) · projected 22.4
- ESPN: day-to-day, ESPN est. 22 Nov (Illness, updated 2026-11-21)
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (20 Nov): Smith (illness) is out for Friday's game against the Wizards, Joel Lorenzi of The Athletic reports.
- News (20 Nov): Smith (illness) has been downgraded to questionable for Friday's game against the Wizards.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, us)

- Rate **33.8** · role rate 38.6 · season 29.4 (18) → 31.1 (17) · L7 29.6 (5) → 36.8 (4) · L15 29.9 (10) → 33.1 (9) · L30 30.2 (17) → 32.1 (16) · projected 25.9
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.0 for the season (+7.3)
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, us)

- Rate **33.3** · role rate 37.8 · season 30.1 (15) · L7 32.2 (4) · L15 40.7 (7) · L30 31.4 (14)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 29.9 for the season (+7.7)
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- **Research:** _pending_

### Cade Cunningham (DET, PG, us)

- Rate **50.1** · season 50.1 (14) · L7 47.7 (3) · L15 51.7 (6) · L30 50.9 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 22 Nov (Right Knee Soreness, updated 2026-11-21)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Cunningham's status is uncertain for the second half of Detroit's back-to-back set after he played 37 minutes in Tuesday's win over San Antonio."; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Cunningham (knee) is probable to play Sunday in Atlanta.
- News (20 Nov): Cunningham recorded 23 points (10-22 FG, 2-7 3Pt, 1-4 FT), five rebounds, nine assists and one steal over 36 minutes in Friday's 105-102 loss to the Raptors.
- **Research:** _pending_

### Anthony Black (ORL, PG/SG, us)

- Rate **38.6** · season 38.3 (12) · L7 38.3 (3) · L15 41.4 (7) · L30 38.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- News (19 Nov): Black totaled 15 points (6-16 FG, 2-5 3Pt, 1-3 FT), two rebounds, six assists, one block and one steal in 37 minutes during Wednesday's 121-116 loss to the 76ers.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **37.1** · season 40.6 (14) · L7 35.2 (4) · L15 37.1 (7) · L30 38.2 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (19 Nov): George supplied 10 points (3-12 FG, 1-7 3Pt, 3-3 FT), four rebounds, one assist, one block and three steals across 23 minutes before fouling out of Wednesday's 105-101 loss to Denver.
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- **Research:** _pending_

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:** _pending_

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **23.8** · role rate 24.0 · season 30.6 (9) · L7 — · L15 14.5 (4) · L30 27.4 (8) · projected 39.0
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

- Rate **8.1** · season 8.8 (12) · L7 — · L15 3.2 (4) · L30 7.6 (11) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:** _pending_

### Brayden Burries (MIL, SG, free agent)

- Rate **30.1** · season 24.5 (17) · L7 36.2 (4) · L15 30.9 (9) · L30 25.0 (16) · projected 22.2
- ESPN: active
- **Role:** news on 21 Nov: "Burries is not in the Bucks' starting lineup against the 76ers on Saturday."
- News (21 Nov): Burries ended with 26 points (12-20 FG, 2-6 3Pt, 0-1 FT), eight rebounds, four assists and one block over 26 minutes off the bench during Saturday's 132-129 loss to the 76ers.
- News (21 Nov): Burries is not in the Bucks' starting lineup against the 76ers on Saturday.
- **Research:** _pending_

### Jaxson Hayes (UTAH, C, free agent)

- Rate **29.7** · season 28.3 (14) · L7 34.5 (2) · L15 28.7 (7) · L30 27.0 (13) · projected 16.5
- ESPN: active
- **Role:** news on 20 Nov: "Hayes is listed in the starting lineup for Friday's game against the Suns."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (21 Nov): Hayes produced 18 points (7-8 FG, 4-8 FT) and 14 rebounds in 28 minutes during Friday's 111-101 loss to Phoenix.
- News (20 Nov): Hayes is listed in the starting lineup for Friday's game against the Suns.
- **Research:** _pending_

### Jakob Poeltl (TOR, C, free agent)

- Rate **29.4** · season 26.4 (14) · L7 28.5 (4) · L15 33.4 (8) · L30 27.2 (13) · projected 31.7
- ESPN: active
- **Role:** news on 18 Nov: "Poeltl will start Wednesday's game against the Wizards."
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.4** · role rate 32.2 · season 23.9 (15) · L7 30.0 (4) · L15 32.6 (7) · L30 24.9 (14) · projected 22.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 13 before; 36.0 min in his starts, against 26.7 for the season
- **Minutes:** 36.0 min over his last 3 games against 26.7 for the season (+9.3)
- News (21 Nov): Huerter chipped in 20 points (7-15 FG, 4-8 3Pt, 2-3 FT), three rebounds, three assists and one steal across 36 minutes during Friday's 105-102 loss to Toronto.
- News (19 Nov): Huerter had 11 points (2-9 FG, 1-4 3Pt, 6-7 FT), one rebound, seven assists, one block and one steal across 36 minutes during Wednesday's 122-109 victory over New Orleans.
- **Research:** _pending_

### Derik Queen (NO, PF/C, free agent)

- Rate **28.2** · role rate 43.2 · season 26.9 (18) → 28.3 (17) · L7 29.6 (5) · L15 23.6 (10) → 25.9 (9) · L30 26.6 (17) → 28.1 (16) · projected 30.5
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 16 before; 35.0 min in his starts, against 22.2 for the season
- **Role:** news on 21 Nov: "Queen will start Saturday against the Spurs."
- News (21 Nov): Queen will start Saturday against the Spurs.
- News (17 Nov): Queen delivered 17 points (6-9 FG, 4-5 3Pt, 1-2 FT), 10 rebounds and one block across 20 minutes in Monday's 115-94 win over the Warriors.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.3** · role rate 29.7 · season 26.8 (13) · L7 26.0 (1) · L15 29.0 (4) · L30 26.4 (12) · projected 26.6
- ESPN: day-to-day, ESPN est. 23 Nov (Concussion, updated 2026-11-21)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- News (17 Nov): Allen (concussion-like symptoms) has been ruled out for Tuesday's game against the Lakers.
- **Research:** _pending_

### Payton Pritchard (BOS, PG/SG, free agent)

- Rate **27.3** · role rate 32.0 · season 26.0 (16) · L7 27.2 (4) · L15 27.2 (8) · L30 26.1 (15) · projected 31.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 14 before; 34.0 min in his starts, against 27.6 for the season
- **Role:** news on 21 Nov: "Pritchard will start in Saturday's game against the Kings."
- News (21 Nov): Pritchard will start in Saturday's game against the Kings.
- News (19 Nov): Pritchard had 15 points (6-11 FG, 3-6 3Pt), one rebound and two assists over 30 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:** _pending_

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **22.4** · role rate 25.8 · season 19.2 (8) · L7 26.0 (1) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-19)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- News (18 Nov): Tyson (ankle) has been ruled out for Wednesday's game against Memphis.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **33.8** · role rate 31.0 · season 24.1 (15) · L7 44.8 (4) · L15 34.5 (6) · L30 23.8 (14) · projected 28.1
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 29.1 for the season (+8.3)
- News (21 Nov): Grimes logged 13 points (2-7 FG, 1-5 3Pt, 8-9 FT), five rebounds and seven assists in 35 minutes during Friday's 106-104 victory over the Kings.
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **31.6** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 37.2 (9) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **29.0** · role rate 23.4 · season 28.2 (15) · L7 29.3 (3) · L15 28.3 (7) · L30 29.2 (14) · projected 26.9
- ESPN: out, ESPN est. 22 Nov (Illness, updated 2026-11-21)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (21 Nov): Washington (illness/shoulder) is listed as out for Saturday's game against the Clippers.
- News (21 Nov): Washington (illness/shoulder) has been downgraded from questionable to doubtful ahead of Saturday's game against the Clippers.
- **Research:** _pending_

### Dean Wade (PHI, PF, free agent)

- Rate **27.1** · role rate 27.1 · season 21.5 (13) · L7 39.5 (2) · L15 21.0 (6) · L30 21.5 (13) · projected 16.3
- ESPN: out, ESPN est. 23 Nov (Left Hamstring Soreness, updated 2026-11-20)
- **Minutes:** 33.7 min over his last 3 games against 26.7 for the season (+7.0)
- News (20 Nov): Wade (hamstring) won't play Saturday against the Bucks.
- News (20 Nov): Wade (hamstring) participated in Friday morning's practice without restrictions, an encouraging sign for his availability for Saturday's game against the Bucks, per Tony Jones of The Athletic.
- **Research:** _pending_

### Neemias Queta (BOS, C, free agent)

- Rate **30.9** · season 27.4 (15) · L7 35.0 (3) · L15 29.3 (7) · L30 27.9 (14) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- News (17 Nov): Queta (rest) is available for Wednesday's game against the Nuggets, Jack Simone of BostonSportsJournal.com reports.
- **Research:** _pending_

### Myles Turner (MIL, C, free agent)

- Rate **27.2** · season 27.2 (15) · L7 29.7 (3) · L15 23.7 (7) · L30 27.4 (14) · projected 28.4
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

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **44.1** · season 40.8 (14) · L7 50.5 (2) · L15 40.2 (6) · L30 40.5 (13) · projected 38.6
- ESPN: out, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-20)
- **Injury:** ESPN est. 23 Nov (Out, Left Hamstring, updated 20 Nov), but the news said on 20 Nov: "Brown is set to be re-evaluated this weekend due to a left hamstring strain, meaning his next chance to play will come Monday against Portland."
- News (20 Nov): Brown (hamstring) went through individual work during Friday's practice, Tony Jones of The Athletic reports.
- News (18 Nov): Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com.
- **Research:** _pending_

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **37.1** · season 39.9 (12) · L7 — · L15 31.8 (4) · L30 39.9 (12) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:** _pending_

### Aday Mara (OKC, C, Snow Time Lakers)

- Rate **38.4** · season 29.5 (16) · L7 47.7 (3) · L15 37.2 (8) · L30 30.5 (15)
- ESPN: active
- **Role:** news on 20 Nov: "Mara is now listed in the starting lineup for Friday's matchup with the Pelicans, Brandon Rahbar of DailyThunder.com reports."
- News (20 Nov): Mara posted 22 points (11-15 FG), 16 rebounds, two assists and two blocks across 29 minutes during Friday's 126-120 win over the Pelicans.
- News (20 Nov): Mara is now listed in the starting lineup for Friday's matchup with the Pelicans, Brandon Rahbar of DailyThunder.com reports.
- **Research:** _pending_

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **28.1** · season 32.6 (14) · L7 21.3 (3) · L15 30.4 (7) · L30 32.6 (14) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (20 Nov): Podziemski closed with 15 points (5-12 FG, 0-5 3Pt, 5-6 FT), three rebounds, two assists and one steal in 32 minutes during Thursday's 126-98 loss to the Grizzlies.
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- **Research:** _pending_

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **42.2** · season 44.9 (16) · L7 38.3 (3) · L15 42.9 (7) · L30 44.4 (15) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Kessler will return to action after being held out of the front end of this back-to-back set."; sat the first night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Kessler notched 15 points (7-11 FG, 1-1 3Pt, 0-2 FT), seven rebounds, two assists, three blocks and one steal in 30 minutes during Friday's 106-104 win over Sacramento.
- News (19 Nov): Kessler notched 10 points (3-7 FG, 4-10 FT), 11 rebounds and one assist in 31 minutes during Wednesday's 109-97 loss to the Jazz.
- **Research:** _pending_

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **41.5** · season 36.3 (16) → 38.5 (15) · L7 36.5 (4) → 47.7 (3) · L15 34.5 (8) → 39.0 (7) · L30 36.0 (15) → 38.4 (14) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (21 Nov): Herro recorded 50 points (15-23 FG, 7-12 3Pt, 13-13 FT), 11 rebounds, seven assists and one steal over 40 minutes during the Bucks' 132-129 loss to the 76ers on Saturday.
- News (20 Nov): Herro totaled 19 points (7-13 FG, 4-7 3Pt, 1-3 FT), four rebounds, three assists and one steal over 31 minutes during Thursday's 124-114 loss to Portland.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.5** · season 39.2 (15) · L7 41.0 (3) · L15 41.6 (7) · L30 39.1 (14) · projected 41.1
- ESPN: day-to-day, ESPN est. 22 Nov (Left Hip Soreness, updated 2026-11-21)
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Siakam (hip) is listed as questionable for Sunday's game against New York.
- News (18 Nov): Siakam chipped in 24 points (10-17 FG, 2-2 3Pt, 2-2 FT), four rebounds, three assists, one block and three steals across 33 minutes during Wednesday's 119-104 loss to the Rockets.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **30.8** · season 32.8 (12) · L7 29.0 (1) · L15 29.8 (5) · L30 32.3 (11) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- News (19 Nov): Nembhard (hip) is questionable for Friday's game in Cleveland.
- **Research:** _pending_

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **23.9** · season 29.5 (16) · L7 15.7 (3) · L15 24.1 (8) · L30 29.0 (15) · projected 38.2
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Fox has been held in check in back-to-back appearances, and he never found a rhythm against Detroit's physical perimeter defense."
- News (20 Nov): Fox ended Thursday's 124-112 win over the Clippers with 10 points (2-5 FG, 0-1 3Pt, 6-6 FT), five assists, two rebounds and one steal across 32 minutes.
- News (18 Nov): Fox contributed six points (3-10 FG, 0-5 3Pt), two rebounds, two assists and two steals in 34 minutes during Tuesday's 105-93 loss to the Pistons.
- **Research:** _pending_

## Other rosters: injury flags only

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 29.0 (1) → — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

### Tyrese Maxey (PHI, PG/SG, Team Nic Kerr)

- Rate **43.0** · season 45.6 (16) · L7 40.7 (3) · L15 41.3 (7) · L30 44.4 (15) · projected 45.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 21 Nov: "Maxey (foot) will be a true game-time decision for Saturday's game against the Bucks, head coach Nick Nurse told Ky Carlin of USA Today."
- News (21 Nov): Maxey produced 17 points (4-11 FG, 0-3 3Pt, 9-10 FT), four rebounds, four assists and one block in 36 minutes during Saturday's 132-129 victory over the Bucks.
- News (21 Nov): Maxey (foot) is available for Saturday's game against the Bucks, Austin Krell of OnPattison.com reports.
- **Research:** _pending_

### Brandon Ingram (LAC, SF/PF, Melbourne poopoo)

- Rate **36.5** · season — · L7 — · L15 — · L30 — · projected 38.5
- ESPN: out, ESPN est. 23 Nov (Right Achilles Surgery, updated 2026-11-20)
- **Injury:** ESPN est. 23 Nov (Out, Right Achilles Surgery, updated 20 Nov), but the news said on 20 Nov: "The star forward is set to make his long-awaited return after undergoing surgery for a partially torn Achilles tendon in May. Ingram, who'll miss Saturday's game in Dallas, is likely to carry a minutes restriction following a lengthy layoff, though his presence is certain to cut into the playing time of the likes of Kris Dunn, Max Strus and Gradey Dick on the wing for the Clippers."
- News (20 Nov): Ingram (Achilles) is expected to make his season and team debut Monday against the Rockets, per Shams Charania of ESPN.
- News (18 Nov): Ingram (heel/Achilles) will remain on the inactive list for Thursday's game in San Antonio.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-22 07:27 UTC.
