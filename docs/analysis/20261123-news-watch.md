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
- **Research:**
  - He was out again Sun 22 Nov at ATL with the right hamstring strain [NBA injury report, 22 Nov 11:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf). That was his 14th straight missed game. The two-week re-evaluation set on 8 Nov has now passed with no update from the team [Detroit Jock City, 22 Nov](https://detroitjockcity.com/pistons-injury-report-hawks-cade-cunningham-jalen-duren-playing-01m823m27vfp); [NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring). Detroit lost 107-97 at ATL, and SB Nation's recap ends "Please, Jalen Duren, come back soon" [Yahoo/SB Nation, 22 Nov](https://sports.yahoo.com/articles/pistons-hawks-final-score-detroit-231826185.html).
  - Gap: no result of the re-evaluation has been reported, and Detroit's report for Tue 24 at ORL is not out yet (it comes Monday afternoon ET). Detroit plays only three games this week: Tue 24 at ORL, Fri 27 vs MIL and Sun 29 vs ORL.
  - **Expected return:** no game date reported. Tue 24 Nov at ORL is the earliest he could play, and only if the re-evaluation clears him. *ESPN est.* 24 Nov.
  - **Verdict:** ESPN confirmed, but only as a floor: 24 Nov is the first game after the check, not a reported return. If Monday's report lists him out for Tue 24, move the row to 2026-12-01 (7 days after that out report).
  - Override proposed: return 2026-11-24

### Kevin Huerter (DET, SG/SF, us)

- Rate **22.2** · role rate 28.7 · season 22.3 (16) · L7 16.5 (4) · L15 28.4 (8) · L30 23.2 (15) · projected 22.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 14 before; 34.5 min in his starts, against 26.9 for the season
- **Minutes:** 34.0 min over his last 3 games against 26.9 for the season (+7.1)
- News (21 Nov): Huerter chipped in 20 points (7-15 FG, 4-8 3Pt, 2-3 FT), three rebounds, three assists and one steal across 36 minutes during Friday's 105-102 loss to Toronto.
- News (19 Nov): Huerter had 11 points (2-9 FG, 1-4 3Pt, 6-7 FT), one rebound, seven assists, one block and one steal across 36 minutes during Wednesday's 122-109 victory over New Orleans.
- **Research:**
  - Role: he started Sun 22 at ATL, his fourth straight start in Duncan Robinson's spot (17, 18, 20, 22 Nov), and played 30 min. He went 1-of-8 for 2 points and finished −28 (−1 FP) [ESPN box score, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029); [Yahoo/SB Nation, 22 Nov](https://sports.yahoo.com/articles/pistons-hawks-final-score-detroit-231826185.html). Before Robinson's injury, Robinson started beside Jenkins and Huerter came off the bench (24–38 min) [ESPN box score, 14 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909982). So Robinson's return should end the start.
  - Robinson (left quad strain) is still out. He was to be re-evaluated in one week from 17 Nov, so about 24 Nov, and his earliest possible game is Tue 24 at ORL [Detroit Jock City, 22 Nov](https://detroitjockcity.com/pistons-injury-report-hawks-cade-cunningham-jalen-duren-playing-01m823m27vfp); [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-duncan-robinson-to-be-re-evaluated-in-one-week/). No timetable reported; *ESPN est.* 27 Nov.
  - Minutes: 36, 36, 36, then 30 min in his starts. Isaiah Joe has climbed to 16, 18 and 26 min off the bench since he returned on 18 Nov, and scored 19 on Sunday. That is cutting into Huerter's minutes. L7 16.5 (4) is 5.8 under his 22.3 average because of his shooting (11 FP on 17 Nov, −1 on 22 Nov), not his minutes.
  - **Verdict:** ESPN confirmed: active. He should start Tue 24 at ORL at about 34 min. The start ends when Robinson returns: the first game after his re-evaluation is Fri 27, and Tue 24 is possible.
  - Override proposed: role 34

### Jalen Smith (CHI, PF/C, us)

- Rate **45.7** · season 37.9 (14) → 40.0 (13) · L7 52.3 (3) · L15 49.2 (6) · L30 38.3 (13) → 40.7 (12) · projected 22.4
- ESPN: active
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (22 Nov): Smith (illness) is available for Sunday's game against the Nuggets.
- News (22 Nov): Smith (illness) has been upgraded to probable for Sunday's game against the Nuggets.
- **Research:**
  - He played Sun 22 vs DEN after the illness, which had made him questionable. He started at center because Nic Claxton was out (illness; no timetable reported; *ESPN est.* 23 Nov). He scored a career-high 26 on 10-of-14 FG and 6-of-7 3PT, with 4 rebounds, 2 steals and 2 blocks, in 34 min before fouling out in overtime of a 151-145 loss [ESPN box score, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032); [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/jalen-smith-hits-six-three-pointers-scores-26).
  - Minutes and role vs Claxton: Rotoworld says the Bulls "have kept Smith in the starting center role even when Claxton plays," with Zach Collins the primary backup [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/jalen-smith-hits-six-three-pointers-scores-26). Claxton only started on Fri 20, when Smith was out. His minutes run 30, 32, 28, 21 (a blowout) and 34 (OT). L7 52.3 (3) is about 14 over his season average, from the starting role and hot shooting.
  - Rest: Chicago's report for Mon 23 vs CLE was "not yet submitted" at 11:15 PM ET [NBA injury report, 22 Nov 11:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf). His 14 Nov absence was a finger sprain, not rest (unchanged since 22 Nov), and the team has said nothing about resting him.
  - **Verdict:** ESPN confirmed: active. He is the starting center whether or not Claxton plays. The rest flag is a false alarm.

### Trey Murphy III (NO, SG/SF, us)

- Rate **37.3** · season 31.7 (10) · L7 38.0 (1) · L15 41.0 (2) · L30 33.4 (9) · projected 36.8
- ESPN: day-to-day, ESPN est. 23 Nov (Knee, updated 2026-11-22)
- **Minutes:** news on 21 Nov: "Expect his minutes to ramp up quickly, and once he's fully back, he should rejoin a starting lineup that has struggled to find consistent scoring."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 21 Nov: "He'll sit for the second leg of a back-to-back set, which means more minutes will be available for Jordan Poole, Herbert Jones and Derik Queen."
- News (22 Nov): Murphy (knees) is listed as probable for Monday's game against the Suns.
- News (21 Nov): Murphy (knee) has been ruled out for Saturday's game against the Spurs.
- **Research:**
  - He is **probable** for Mon 23 vs PHX (bilateral patellar tendinopathy) [NBA injury report, 22 Nov 11:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/trey-murphy-knee-probable-vs-phoenix-on-monday). He played 29 min off the bench on a minutes limit Fri 20 at OKC. No limit has been reported for Monday; RotoWire says only that he "could remain restricted." If he starts, Saddiq Bey or Herbert Jones goes to the bench (NBC, 22 Nov). L7 38.0 (1) is a small sample.
  - Rest: he sat Sat 21 at SA, the second night of the 20–21 Nov back-to-back, listed as "injury maintenance" [Yahoo/HoopsHype, 21 Nov](https://sports.yahoo.com/articles/pelicans-rest-trey-murphy-against-182359369.html). New Orleans plays only three games this week: Mon 23 vs PHX, Fri 27 at LAC and Sun 29 at POR. Sun 29 is the first night of the back-to-back, so it is not a rest-risk night. He is likely to sit Mon 30 at SAC, which falls next week. The team has not announced that, so there is no sit row.
  - **Expected return:** probable for Mon 23 vs PHX. *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed: day-to-day and due back Monday. His minutes may still be managed, and the Mon 30 rest risk is a pattern, not an announcement.

### Daniss Jenkins (DET, PG, us)

- Rate **32.7** · role rate 36.7 · season 29.7 (16) · L7 32.8 (4) · L15 38.6 (8) · L30 30.9 (15)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 30.4 for the season (+7.2)
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- **Research:**
  - Minutes: he started Sun 22 at ATL and played 38 min (11 pts, 4-of-12 FG, 24 FP), so his last four starts ran 38, 36, 39 and 38 min [ESPN box score, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029). He moved into the first unit on 9 Nov, with Paul Reed going to the bench and Duren out, and he started beside Robinson [ESPN box score, 9 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909954). So Duren's return, not Robinson's, is the likely end of his start. Robinson's return should cost Huerter, not Jenkins. No source has said how Bickerstaff will set the lineup.
  - Duren (right hamstring; no timetable reported; *ESPN est.* 24 Nov) has no update after his re-evaluation [Detroit Jock City, 22 Nov](https://detroitjockcity.com/pistons-injury-report-hawks-cade-cunningham-jalen-duren-playing-01m823m27vfp). The 37-min row ends 23 Nov, which matches Duren's floor of 24 Nov, so no new row is added. If Monday's report rules Duren out for Tue 24 at ORL, extend Jenkins' role to 37 min through 24 Nov.
  - **Verdict:** ESPN confirmed: active. He keeps the starting role and about 37 min until Duren returns, Tue 24 at the earliest.

### Cade Cunningham (DET, PG, us)

- Rate **46.0** · season 48.8 (15) · L7 39.0 (3) · L15 48.7 (7) · L30 49.5 (14) · projected 50.4
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Cunningham's status is uncertain for the second half of Detroit's back-to-back set after he played 37 minutes in Tuesday's win over San Antonio."; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (22 Nov): Cunningham (knee) is available for Sunday's game against the Hawks.
- News (21 Nov): Cunningham (knee) is probable to play Sunday in Atlanta.
- **Research:**
  - Knee: he played Sun 22 at ATL through the right knee soreness. He was probable, then listed available ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf)). He started and played 33 min. Foul trouble (three fouls by early in the 2nd quarter) held him to 14 first-half minutes, and he scored a season-low 5 pts on 2-of-9 shooting with a season-high 15 ast, for 31 FP. Before the game Bickerstaff said the team must protect him "at all costs" ([FOX 2 Detroit/AP, 22 Nov](https://www.fox2detroit.com/sports/alexander-walker-has-27-points-hawks-roll-107-97-win-over-pistons-off-game-cunningham); [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). His L7 of 39.0 (3) is 9.8 under his 48.8 season average. The cause is shooting and Sunday's foul trouble, not minutes (36 and 33 in his last two games).
  - Rest: Detroit plays Tue 24 at ORL, Fri 27 vs MIL and Sun 29 vs ORL, so there is no back-to-back before Sun 29. Mon 30 vs DEN, the second night, falls in next week. He played both nights of 27–28 Oct and 8–9 Nov, and sat only the second night on 18 Nov, listed with knee soreness. No source has said he will sit 29 or 30 Nov. Detroit's report for Tue 24 has not been filed. Unchanged since 22 Nov.
  - **Verdict:** ESPN confirmed. He is active. His rest risk this week is low and sits mainly on Mon 30, which is next week.

### Anthony Black (ORL, PG/SG, us)

- Rate **37.5** · season 37.8 (13) · L7 36.5 (4) · L15 40.1 (8) · L30 37.8 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- News (19 Nov): Black totaled 15 points (6-16 FG, 2-5 3Pt, 1-3 FT), two rebounds, six assists, one block and one steal in 37 minutes during Wednesday's 121-116 loss to the 76ers.
- **Research:**
  - He started Sun 22 at WAS and played 35 min: 14 pts, 5 reb, 2 ast, 2 stl, 31 FP in a 116-96 loss ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/anthony-black-records-14-5-2-2-line-vs-wizards); [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031)). Paolo Banchero is still out with a right high ankle sprain, so Black's starting role holds this week. For Banchero, no timetable has been reported (Sweeney, 18 Nov, [Orlando Sentinel via Yahoo](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html)); *ESPN est.* 29 Nov.
  - Rest: Orlando plays Tue 24 vs DET, Sat 28 at WSH and Sun 29 at DET. He sat the second night on 2 Nov, listed as left ankle injury management ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/)), but played both nights of 10–11 Nov. Nobody has said he will sit 28 or 29 Nov. Unchanged since 22 Nov.
  - **Verdict:** nothing new found. He is healthy and starting, and his rest risk is Sun 29 only, with no announced plan.

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:**
  - Unchanged since 22 Nov. On 20 Nov the Jazz said he had been cleared for on-court work and would be re-evaluated in one week, which puts the re-evaluation around 27 Nov ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3); [Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/jazzs-jusuf-nurkic-toe-out-at-least-one-more-week.html)). He was Out for Sun 22 Nov vs DAL with the right 2nd plantar plate tear ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [SI/Jazz On SI, 22 Nov](https://www.si.com/nba/jazz/onsi/jazz-vs-mavericks-injury-report-latest-updates-on-both-teams)). Utah's report for Mon 23 Nov @LAL was still "not yet submitted". I found no report that he has done contact or 5-on-5 work.
  - **Expected return:** the re-evaluation is due about 27 Nov, so his first possible game is Sun 29 Nov vs PHX. Utah plays 23 Nov @LAL and 27 Nov vs DEN before that. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date fits the team's one-week re-evaluation. The 28 Nov row stays, since Utah has no game on 28 Nov and it counts the same as 29 Nov.

### Norman Powell (CHI, SG/SF, waivers)

- Rate **32.9** · season 30.1 (13) → 32.2 (12) · L7 30.3 (3) · L15 36.2 (5) · L30 30.7 (12) → 33.1 (11) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:**
  - He did not play Sun 22. He was ruled out against DEN (NBA report: Out, right hamstring strain), and Hield started in his place ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf); [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032)). An MRI showed a mild strain, and he "will be re-evaluated later this week" ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-to-be-re-evaluated-later-this-week/); [Chicago Sun-Times, 22 Nov](https://chicago.suntimes.com/bulls/2026/11/22/bulls-veteran-norman-powell-sidelined-tweaked-hamstring)). K.C. Johnson: "Hamstrings are tricky. Team hopes to have more definitive timeline later in week" ([K.C. Johnson on X, 22 Nov](https://x.com/KCJHoop/status/2124522701285187925)).
  - This week: NBC says he "will likely miss" Mon 23 vs CLE and Wed 25 at CHA ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/powell-hamstring-to-be-re-evaluated-this-week)). Bulls On SI says the re-evaluation could also cost him Sat 28 vs IND, the fourth game ([SI, 22 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-update-bad-news-on-norman-powell-jalen-smith-still-questionable-22)). Chicago's report for Mon 23 had not been filed by 11 PM ET.
  - **Expected return:** re-evaluation later this week. He is not expected Mon 23 or Wed 25, and Sat 28 vs IND is the earliest he could play. *ESPN est.* 28 Nov.
  - **Verdict:** ESPN confirmed. 28 Nov matches the earliest game the sources leave open, but it is a floor, not a target.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:**
  - He is Out for Mon 23 Nov vs SAS with a right patella subluxation ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). Otherwise unchanged since 22 Nov. RotoWire has called him "week-to-week" since 18 Nov ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)), and James Ham reported that he is progressing with no timeline ([NBC, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)). I found no practice report.
  - **Expected return:** no timetable reported. The week-to-week floor is 25 Nov (SAC @GS), and Sacramento's next game after that is 29 Nov vs MIN. *ESPN est.* 25 Nov.
  - **Verdict:** ESPN confirmed, but only as a floor. The floor has not passed and SAC plays on 25 Nov, which will bring a fresh report, so the 25 Nov row stays.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **23.4** · role rate 24.0 · season 30.6 (9) · L7 — · L15 13.7 (3) · L30 27.4 (8) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - He is Out for Mon 23 Nov vs PHX with a left ankle sprain ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [Pelicans, 22 Nov](https://www.nba.com/pelicans/news/pelicans-vs-suns-injury-report-game-preview-11-23-2026)). He is sitting until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)).
  - New on 22 Nov: per Rod Walker, he has not "set foot in the Smoothie King Center" since his trade request. Phoenix is the only team in real talks, and the Pelicans "aren't going to be in a hurry to make a trade" ([Bleacher Report, 22 Nov](https://bleacherreport.com/articles/25536410-dejounte-murray-hasnt-been-pelicans-arena-trade-request-latest-nba-rumors-suns-talks)). Gap: no news beyond this standoff. Minutes: they do not matter while he is not playing.
  - **Expected return:** no timetable reported. He is out until he is traded. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is only a placeholder. NOP is off 24–26 Nov, so the 26 Nov floor passes before the Pelicans' next game (27 Nov @LAC). I propose rolling the floor now to 7 days after the 23 Nov out listing. This takes him out of the 27 and 29 Nov games, and the next NOP game is 30 Nov @SAC.
  - Override proposed: return 2026-11-30

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **14.8** · season 14.2 (5) · L7 — · L15 — · L30 11.0 (4) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:**
  - He is Out for Mon 23 Nov @CHA with a lumbar disc herniation, his 13th straight miss ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). He has been "week-to-week" since 16 Nov with no re-evaluation date ([Grizzlies via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html)). I found no report that he has practiced.
  - Gap: he is Out, and there is no news beyond the injury report.
  - **Expected return:** no timetable reported. The 23 Nov floor has passed with him listed Out, so the new floor is 30 Nov, 7 days after the latest out listing. Memphis's first game after that is Tue 1 Dec @PHI, so he misses MEM's 25, 27 and 29 Nov games. *ESPN est.* 25 Nov.
  - **Verdict:** ESPN corrected. Nothing supports 25 Nov, and he is still out with no timetable, so the row moves from 23 Nov to 30 Nov.
  - Override proposed: return 2026-11-30

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.3** · season 8.8 (12) · L7 — · L15 3.7 (3) · L30 7.6 (11) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - He is Out for Mon 23 Nov vs PHX with left plantar fasciitis ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/bennedict-mathurin-foot-remains-out-monday)). No timeline has been given. "Week-to-week" is RotoWire's own assessment, not the team's ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). Otherwise unchanged since 22 Nov.
  - **Expected return:** no timetable reported. The week-to-week floor is 26 Nov, and NOP's first game after it is 27 Nov @LAC. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date matches the floor. No source puts him out longer, so a row would change nothing and I added none.

---
**Summary**
- Pippen was listed Out for Mon 23 Nov, so his floor moves from 23 Nov to 30 Nov. That rules him out of all of Memphis's games this week (25, 27, 29 Nov).
- I propose moving Murray from 26 Nov to 30 Nov. He is sitting until he is traded, the Pelicans are "in no hurry" (22 Nov), and NOP plays no games between his 23 Nov out listing and the old floor. This rules him out of NOP's 27 and 29 Nov games.
- Nurkic (28 Nov row, re-evaluation ~27 Nov) and Raynaud (25 Nov floor) are unchanged. Mathurin (*ESPN est.* 27 Nov) still has no row. All five were listed Out on the 22 Nov 11:15 PM ET report.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **29.2** · role rate 29.7 · season 26.8 (13) · L7 26.0 (1) · L15 36.0 (3) · L30 26.4 (12) · projected 26.6
- ESPN: out, ESPN est. 25 Nov (Concussion, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (22 Nov): Allen (concussion) has been ruled out for Monday's game against the Grizzlies.
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- **Research:**
  - Injury: still in the concussion protocol and ruled out for Mon 23 Nov vs MEM, which will be his third straight miss. The reports give no progress or timeline ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-missing-third-straight-game-monday/); [NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). He has to pass the protocol's checkpoints symptom-free before he plays ([Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html)).
  - Role: the change is not ongoing. He started only while Brandon Miller was out. Miller started 20 Nov at ATL (33 min) and is listed probable for Monday, and Sion James keeps the other starting spot ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909305); [CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-missing-third-straight-game-monday/)). Kon Knueppel's hamstring injury keeps Allen's minutes up (re-evaluation about 6 Dec, *ESPN est.* 12 Dec). Once he is cleared, expect about 25 min off the bench. This week he can play at most Wed 25 vs CHI and Sat 28 vs BKN.
  - **Expected return:** no timetable reported (concussion protocol). *ESPN est.* 25 Nov, which is just Charlotte's next game after Monday, not a reported date.
  - **Verdict:** nothing new found. He is out Monday, as ESPN says, and no source backs 25 Nov.

### Jakob Poeltl (TOR, C, free agent)

- Rate **28.4** · season 26.4 (14) · L7 28.5 (4) · L15 29.7 (7) · L30 27.2 (13) · projected 31.7
- ESPN: active
- **Role:** news on 18 Nov: "Poeltl will start Wednesday's game against the Wizards."
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:**
  - Role: he started 18 Nov (29 min), when RJ Barrett and Scottie Barnes were out, beside Collin Murray-Boyles. He started again 20 Nov (32 min) beside rookie Allen Graves, with Murray-Boyles out. On 15 and 17 Nov all three were active and Poeltl came off the bench (17 and 18 min) ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308); [17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002)).
  - Murray-Boyles (concussion protocol, *ESPN est.* 23 Nov) is probable for Mon vs MIL, and Rajakovic is "very confident" he plays ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [BVM Sports, 22 Nov](https://bvmsports.com/2026/11/22/raptors-rajakovic-very-confident-murray-boyles-will-return-vs-bucks/)). NBC expects Graves, not Poeltl, to go to the bench when Murray-Boyles returns ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl)). That would leave Poeltl starting beside Murray-Boyles, as on 18 Nov. CBS says it is unclear who keeps the spot ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-expected-to-play-monday/)).
  - Barrett's return would end the start. He has a mild hamstring strain and is to be re-evaluated in two weeks from 19 Nov, about 3 Dec (*ESPN est.* 13 Dec) ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks)). Expect about 27–30 min if Poeltl starts and about 18 if he doesn't. Toronto plays Mon 23, Fri 27 and Sun 29.
  - **Verdict:** ESPN confirmed (active). The start likely lasts while Barrett is out, but no source says Poeltl keeps it, so I added no row. Monday's lineup (7:30 PM ET) will settle it.

### Ryan Rollins (MIL, PG/SG, free agent)

- Rate **26.9** · season 24.0 (15) · L7 28.5 (2) · L15 25.5 (6) · L30 24.4 (14) · projected 31.9
- ESPN: active
- **Role:** news on 21 Nov: "Rollins is in the starting lineup for Saturday's game against the 76ers."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 19 Nov: "Rollins is off the injury report after missing back-to-back contests with an illness."
- News (21 Nov): Rollins provided eight points (4-9 FG, 0-1 3Pt), six rebounds, one assist and one block in 28 minutes during Saturday's 132-129 loss to Philadelphia.
- News (21 Nov): Rollins is in the starting lineup for Saturday's game against the 76ers.
- **Research:**
  - Role: he started Sat 21 Nov at PHI (28 min, 19 FP) in place of Brayden Burries, who had started 10 straight games. It was a coach's decision with no injury behind it, and Jaquez also rejoined the starting five ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-coming-off-bench-saturday/); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/mil-starts-rollins-herro-jaquez-kuzma-turner); [ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401910023)). Burries scored 26 off the bench, and RotoWire wrote that Rollins's spot "likely won't be very secure" ([ESPN/RotoWire news, 22 Nov](https://www.espn.com/nba/player/_/id/4591725/ryan-rollins)). The lineup is an experiment by a losing team, not a lasting role. He is not on Monday's report ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). Expect 21–28 min, about 25, whether he starts or not.
  - Rest: the team has said nothing about the Fri 27 / Sat 28 back-to-back. He played both nights of the 10–11 Nov back-to-back (24 and 24 min), and his 15 and 18 Nov absences were for illness, not rest. Nothing shows a rest pattern.
  - **Verdict:** ESPN confirmed (active). The start is a coach's choice that may not last, and no rest signal was found.

### Pelle Larsson (MIA, SG/SF, free agent)

- Rate **26.7** · role rate 21.9 · season 25.5 (13) · L7 27.5 (2) · L15 27.8 (4) · L30 26.0 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 11 before; 24.5 min in his starts, against 28.5 for the season
- News (19 Nov): Larsson ended with four points (1-2 FG, 1-2 3Pt, 1-2 FT), two rebounds, two assists and one steal across 15 minutes during Wednesday's 137-130 victory over the Bucks.
- News (17 Nov): Larsson (illness) is available for Wednesday's game against Milwaukee, Ira Winderman of the South Florida Sun Sentinel reports.
- **Research:**
  - Role: the change is ongoing. He has started every game he has played since 8 Nov, when Spoelstra moved him into Andrew Wiggins's spot ([Hoops Rumors, 9 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-larsson-wiggins-conwell-hardaway-giannis.html)). Myron Gardner started only during Larsson's illness (13–16 Nov), and NBC expected him back on the bench once Larsson was healthy ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/pelle-larsson-scores-season-high-21-in-victory)). Larsson started again Sun 22 vs OKC and had 21 pts, 5 ast and 3 stl in 30 min ([ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401910030)). His 15-min start on 18 Nov was his first game back from the illness.
  - Giannis's absence does not drive the start: Portis took Giannis's spot on 22 Nov ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/mia-starts-mitchell-klay-larsson-portis-bam)). Giannis has right groin tendinitis. Spoelstra puts the concern at "not super high" and is "optimistic" for Wed 25 at PHI (*ESPN est.* 25 Nov) ([Basketnews, 23 Nov](https://basketnews.com/news-260047-erik-spoelstra-offers-concern-level-on-giannis-new-alarming-injury-for-heat.html)). No player's return from injury ends Larsson's start. Only a coaching move back to Wiggins would, and Hot Hot Hoops (17 Nov) wrote that the spot "may change again". Expect about 28–30 min (22, 31 and 30 in his full starts; 28.5 for the season). Miami plays Wed 25, Fri 27 and Sun 29.
  - **Verdict:** ESPN confirmed (active). The starting role is ongoing, but his minutes as a starter match his season average (a 29-min role rate, about 26, is close to his 26.7 rate), so I added no row.

### Nic Claxton (CHI, C, free agent)

- Rate **23.7** · role rate 32.7 · season 23.3 (6) · L7 22.3 (3) · L15 23.3 (6) · L30 23.3 (6) · projected 30.3
- ESPN: out, ESPN est. 23 Nov (Illness, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 0 of 4 before; 29.0 min in his starts, against 20.7 for the season
- **Role:** news on 20 Nov: "Claxton will start Friday's game against Washington, K.C."
- News (22 Nov): Claxton (illness) won't play in Sunday's game against the Nuggets.
- News (22 Nov): Claxton (illness) is questionable to play in Sunday's game against the Nuggets.
- **Research:**
  - Sun 22: he did not start. He was ruled out with an illness shortly before tip-off, and Jalen Smith, back from his own illness, started at center and played 34 min of the 151–145 overtime loss to Denver ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-nic-claxton-not-playing-sunday/); [ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401910032)).
  - Role: the change is not ongoing. His only start (20 Nov, 29 min) came because Smith was ill ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-nic-claxton-not-playing-sunday/); [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/nic-claxton-with-11-and-7-rebounds-in-start)). With Smith healthy, Claxton goes back to the bench at about 17–22 min, his range as a reserve. Chicago had not filed its report for Mon 23 vs CLE, the second night of a back-to-back ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). He sat the second night of the 13–14 Nov back-to-back for hamstring management ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/nic-claxton-hamstring-absent-from-injury-report)). Chicago also plays Wed 25 at CHA and Sat 28 vs IND.
  - **Expected return:** no timetable reported (illness, day-to-day; Monday not yet filed). *ESPN est.* 23 Nov.
  - **Verdict:** nothing new found on his return. ESPN's 23 Nov estimate fits a one-day illness, but Monday is uncertain. His start ended when Smith returned.

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
- **Research:**
  - Austin Reaves (left heel bruise) is **out Mon 23 vs UTA**, his fifth straight missed game, per Jovan Buha. His next chance is Fri 27 at SAS. Grimes "should remain in the starting lineup versus Utah" ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/lakers-austin-reaves-remains-out-monday/); [NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf)). Reaves practised fully on Sunday, with no live play. Expected return for Reaves: Fri 27 at the earliest (CBS, 22 Nov); *ESPN est.* 27 Nov.
  - Role once Reaves returns: Redick has not said whether Grimes keeps the start. "We're going to be able to be flexible with the starting lineup" ([Lakers Nation, 22 Nov](https://lakersnation.com/jj-redick-discusses-plan-to-keep-quentin-grimes-involved-when-austin-reaves-returns/)). NBC expects lower usage for Grimes ([NBC Sports, 19 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-minutes-report-how-injuries-to-austin-reaves-alperen-sengun-shake-up-two-contenders)). Lakers games this week: Mon 23 vs UTA, Fri 27 at SAS, Sun 29 at MEM.
  - **Verdict:** ESPN confirmed: active. The starting role is confirmed for Mon 23 only. I added no role row because it would cover one game. Its role rate (about 30 at 36 min, from his season FP/min, which includes bench games) would also replace a rate of 35.3 that already reflects his four starts.

Summary:
- Powell did not play Sun 22. He is expected out Mon 23 and Wed 25, and Sat 28 vs IND is the earliest he could return (*ESPN est.* 28 Nov is confirmed as a floor), so he is worth one game this week at most.
- Reaves is out Mon 23, so Grimes starts against UTA. Reaves's next chance is Fri 27 (*ESPN est.* 27 Nov), after which Grimes's role is undecided. With Murphy and Zion both probable Mon 23, Bey may lose his start and drop from about 37 to about 25 min.
- Cunningham played through his knee soreness (33 min, foul trouble). Detroit has no back-to-back until Sun 29–Mon 30, and Black's only rest risk is Sun 29. No rest has been announced for either, so there are no override rows.

### Saddiq Bey (NO, SF/PF, waivers)

- Rate **34.5** · role rate 38.6 · season 29.4 (18) → 31.1 (17) · L7 29.5 (4) → 39.0 (3) · L15 29.3 (9) → 32.9 (8) · L30 30.2 (17) → 32.1 (16) · projected 25.9
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.0 for the season (+7.3)
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- **Research:**
  - Minutes: his recent 37-min games came as a starter. On 20 Nov Murphy came off the bench on a minutes restriction (29 min), and Bey started beside Zion Williamson (37 min each) ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310); [SI, 21 Nov](https://www.si.com/nba/pelicans/onsi/5-things-we-learned-pelicans-wasted-opportunity-vs-thunder-01m7y37xfj8q)). He started again 21 Nov with Murphy resting and Zion out. Before this run of starts, he played 22–26 min off the bench.
  - Mon 23 vs PHX: Trey Murphy III (bilateral patellar tendinopathy) and Zion (left thigh contusion) are both probable (*ESPN est.* 23 Nov for each) ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf); [Pelicans.com, 22 Nov](https://www.nba.com/pelicans/news/pelicans-vs-suns-injury-report-game-preview-11-23-2026)). NBC: "if [Murphy] returns to the starting unit, Saddiq Bey or Herbert Jones will return to the bench" ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/trey-murphy-knee-probable-vs-phoenix-on-monday)). No starting lineup has been announced. Murray and Mathurin remain out (*ESPN est.* 27 Nov each; their timelines were not checked in this batch), which leaves wing minutes open.
  - **Verdict:** ESPN confirmed: active. His 37-min role depends on Murphy staying on the bench or restricted. If Murphy starts, Bey is likely back to about 25 min, so no row.

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
- **Research:**
  - New since 22 Nov: he was a late scratch Sun 22 Nov at MIA with a right shin contusion (the NBC note says left; the official report says right). OKC's report for Mon 23 Nov at IND, the second night of the back-to-back, was "not yet submitted" ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf); [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/aday-mara-shin-ruled-out-sunday-vs-miami)). No coach comment on him. OKC had only nine players available Sunday, and SGA is "up in the air" for Monday ([Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/thunder-falls-heat-injury-report-012807030.html)).
  - Role: unchanged since 22 Nov. He has started with Holmgren out (8–10 weeks from 30 Oct, *ESPN est.* 2 Jan), playing 26, 27 and 29 min in his last three games ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/)). Kenrich Williams started in his place Sunday. His L7 of 47.7 (3 games) runs 18 over his 29.5 season average because of the starting role.
  - **Expected return:** no timetable reported. He is day-to-day with a bruise, and Mon 23 at IND is the first possible game. *ESPN est.* 23 Nov.
  - **Verdict:** nothing new found on timing. ESPN's 23 Nov estimate is unconfirmed until OKC files Monday's report. The existing role row (27 min to 5 Dec) stays as it is.

### Dyson Daniels (ATL, PG/SG, Snow Time Lakers)

- Rate **45.9** · role rate 50.1 · season 42.9 (17) · L7 48.2 (4) · L15 48.3 (7) · L30 42.6 (16) · projected 35.7
- ESPN: active
- **Minutes:** 37.0 min over his last 3 games against 31.6 for the season (+5.4)
- News (22 Nov): Daniels finished Sunday's 107-97 win over the Pistons with five points (2-9 FG, 0-3 3Pt, 1-2 FT), 14 rebounds, eight assists, five steals and two blocks in 39 minutes.
- News (20 Nov): Daniels posted 11 points (5-10 FG, 1-3 3Pt), 10 assists, eight rebounds and four steals over 35 minutes during the Hawks' 111-97 win over the Hornets on Friday.
- **Research:**
  - Minutes: since CJ McCollum went out he has played 37, 35 and 39 min, against 31.6 for the season. McCollum has a left calf strain from 15 Nov and will be re-evaluated in about four weeks, around mid-December ([NBA.com, 18 Nov](https://www.nba.com/news/hawks-cj-mccollum-to-miss-at-least-four-weeks-with-left-calf-strain)). Kingston Flemings (lumbar strain) also missed 15–20 Nov, then returned and started at point guard on 22 Nov ([Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/kingston-flemings-returns-hawks-starting-214942398.html)).
  - Even with Flemings back, Daniels played 39 min in the 107-97 comeback win over DET on 22 Nov (5 pts, 14 reb, 8 ast, 5 stl, 2 blk) ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-dyson-daniels-stuffs-stat-sheet-in-win-540552/)). His L7 of 48.2 (4 games) is 5.3 above his 42.9 season average, and the reason is the extra minutes. Flemings' return may trim a little, but McCollum's minutes stay open until mid-December. No source gives a minutes figure for Daniels.
  - **Verdict:** ESPN corrected (rate understates him). The extra minutes are tied to McCollum's absence, which runs past 7 Dec. I set 35 min, below the 37-min average of the last three games, to allow for Flemings.
  - Override proposed: role 35

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
- **Research:**
  - He returned on 22 Nov at GS after resting the first night of the 21–22 Nov back-to-back, and played 38 min (48 FP) ([CBS Sports, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-jayson-tatum-off-injury-report-sunday/)). Boston also rested Paul George on 22 Nov ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf)).
  - Rest risk for Sun 29–Mon 30 Nov: Boston has now rested him twice, on 4 Nov (not a back-to-back) and on 21 Nov, the first night of a back-to-back. He played both nights of the four earlier back-to-backs. Nothing has been said about 29–30 Nov ([Heavy, 22 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-good-news-after-nightmare-loss/)). If Boston repeats what it did on 21 Nov, he would sit Sun 29 Nov, which is in our week. That is a risk, not a report, so there is no sit row.
  - **Verdict:** ESPN confirmed. He is active, and Boston has said nothing about 29–30 Nov.

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **44.4** · season 40.8 (14) · L7 50.5 (2) · L15 40.8 (5) · L30 40.9 (12) · projected 38.6
- ESPN: day-to-day, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-22)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (22 Nov): Brown (hamstring) is listed as probable for Monday's game versus Portland.
- News (20 Nov): Brown (hamstring) went through individual work during Friday's practice, Tony Jones of The Athletic reports.
- **Research:**
  - Re-evaluation: he was upgraded to probable for Mon 23 Nov vs POR (left hamstring strain) ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf); [NBC Sports Philadelphia, 22 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-injury-update-jaylen-brown-dean-wade-adem-bona/768823/)). The MRI ruled out a tear or severe strain. He returned to full practice Saturday, but the staff held him back from a heavy workload. No minutes limit has been reported for Monday ([Heavy, 22 Nov](https://heavy.com/sports/nba/philadelphia-76ers/76ers-jaylen-brown-injury/)). He is expected to start, and ESPN's note says Kentavious Caldwell-Pope goes back to the bench.
  - Rest flag (Fri 27–Sat 28 Nov): his 30 Oct absence was an injury, not rest. He was ruled out with left knee patellar tendinopathy after missing shootaround ([NBC Philadelphia, 30 Oct](https://www.nbcphiladelphia.com/nba/philadelphia-76ers/jaylen-brown-injury-update-sixers-vs-knicks-nba-cup/4488823/)). So he has no rest pattern, and nothing has been said about 27–28 Nov. His first back-to-back after the hamstring strain is a mild risk. His L7 of 50.5 rests on 2 games (small sample).
  - **Expected return:** probable for Mon 23 Nov vs POR (official report, 22 Nov). *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. He is due back Monday, with no reported minutes limit and no rest pattern.

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **42.1** · season 44.9 (16) · L7 38.3 (3) · L15 42.7 (6) · L30 44.4 (15) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Kessler will return to action after being held out of the front end of this back-to-back set."; sat the first night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Kessler notched 15 points (7-11 FG, 1-1 3Pt, 0-2 FT), seven rebounds, two assists, three blocks and one steal in 30 minutes during Friday's 106-104 win over Sacramento.
- News (19 Nov): Kessler notched 10 points (3-7 FG, 4-10 FT), 11 rebounds and one assist in 31 minutes during Wednesday's 109-97 loss to the Jazz.
- **Research:**
  - Unchanged since 22 Nov. LAL had no game 21–22 Nov. He is not on the Lakers' report for Mon 23 Nov vs UTA, which lists only Grimes (available) and Reaves (out) ([NBA injury report, 22 Nov 11:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_00PM.pdf)).
  - Rest flag (Sun 29–Mon 30 Nov): his 17 Nov absence was right lower-leg soreness, not rest ([NBA.com, 17 Nov](https://www.nba.com/news/lakers-rule-out-reaves-kessler-vs-hornets); [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/walker-kessler-leg-off-injury-report-wednesday)). He played both nights of LAL's 27–28 Oct, 1–2 Nov and 8–9 Nov back-to-backs. Nothing has been said about 29–30 Nov.
  - **Verdict:** ESPN confirmed. He is active with no rest pattern.

Summary:
- Brown was upgraded to probable for Mon 23 Nov vs POR (MRI clean, full practice; no minutes limit reported), and his 30 Oct absence was a knee injury, not rest.
- Mara (right shin bruise, no timetable, *ESPN est.* 23 Nov) missed Sunday, and OKC has not filed Monday's report. Daniels' minutes (37/35/39) follow McCollum's calf injury, out to about mid-December, so I added a 35-min role row to 7 Dec.
- Tatum played Sunday after a first-night rest, and Boston has said nothing yet about Sun 29 Nov. Kessler is clean, with no rest pattern.

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
