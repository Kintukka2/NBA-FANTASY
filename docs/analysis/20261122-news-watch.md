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
- **Research:**
  - He is out again for Sun 22 Nov at ATL (right hamstring strain) [NBA injury report, 22 Nov 2:00 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_00AM.pdf). Heavy says he and Duncan Robinson are "closer to returning, possibly later this week depending on their re-evaluations" [Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22/).
  - No result from the re-evaluation has been reported yet. It is the two-week check set on 8 Nov, so it falls about 22 Nov [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/); [NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring). Bickerstaff: "We're not going to rush him." Otherwise unchanged since 21 Nov.
  - **Expected return:** no game date reported. The earliest game he could play is Tue 24 Nov at ORL, and only if the re-evaluation clears him. *ESPN est.* 24 Nov.
  - **Verdict:** ESPN confirmed, with 24 Nov as a floor. He is out Sunday, and the re-evaluation is a check-up, not a return date.
  - Override proposed: return 2026-11-24

### Jalen Smith (CHI, PF/C, us)

- Rate **43.0** · season 36.1 (13) → 38.3 (12) · L7 48.0 (2) · L15 46.8 (5) · L30 36.4 (12) → 38.8 (11) · projected 22.4
- ESPN: day-to-day, ESPN est. 22 Nov (Illness, updated 2026-11-21)
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (20 Nov): Smith (illness) is out for Friday's game against the Wizards, Joel Lorenzi of The Athletic reports.
- News (20 Nov): Smith (illness) has been downgraded to questionable for Friday's game against the Wizards.
- **Research:**
  - He is still **questionable** for Sun 22 Nov vs DEN with a gastrointestinal illness, after missing Fri 20 vs WAS [NBA injury report, 22 Nov 2:00 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_00AM.pdf); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jalen-smith-illness-questionable-sunday-vs-den). Chicago was off Saturday, so no game-day update exists yet. It is a game-time call.
  - Minutes: Rotoworld says that if he plays, Claxton likely returns to the bench and Zach Collins drops out of the rotation. If he sits, expect Friday's setup again: Claxton started and Collins played 15 min [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jalen-smith-illness-questionable-sunday-vs-den). The Sun-Times' Joe Cowley thinks Claxton is "likely headed for the starting lineup on a permanent basis" [Sun-Times, 20 Nov](https://chicago.suntimes.com/bulls/2026/11/20/bulls-fall-nba-cup-play-added-new-starter-to-lineup). That is a risk to Smith's role, but the team has not said it.
  - Rest: his 14 Nov absence, on the second night of the 13–14 Nov back-to-back, was for a left finger sprain, not rest [NBA injury report, 14 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-14_05_30PM.pdf). He has no pattern of resting on back-to-backs, and the team has said nothing about Mon 23 vs CLE.
  - **Expected return:** no timetable reported; questionable for Sun 22. *ESPN est.* 22 Nov.
  - **Verdict:** ESPN confirmed: day-to-day and a game-time decision. The rest flag is a false alarm.

### Saddiq Bey (NO, SF/PF, us)

- Rate **33.8** · role rate 38.6 · season 29.4 (18) → 31.1 (17) · L7 29.6 (5) → 36.8 (4) · L15 29.9 (10) → 33.1 (9) · L30 30.2 (17) → 32.1 (16) · projected 25.9
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.0 for the season (+7.3)
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- **Research:**
  - Sat 21 Nov at SA (1 FP): he started in place of the resting Murphy and played a normal 32 min. He scored 2 pts on 1-of-12 FG (0-of-7 3PT) and finished a team-worst −26 in a 114-91 blowout. No injury was mentioned. It was his shooting, not his minutes [SI, 22 Nov](https://www.si.com/nba/pelicans/onsi/4-things-we-learned-from-pelicans-blowout-loss-to-spurs); [CBS box score, 21 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261121_NO@SA/). `gamelog.py` drops it as an outlier: L7 29.6 (5) → 36.8 (4).
  - Minutes: the +7 comes from starting. He started 20 Nov with Murphy on the bench, and again 21 Nov with Murphy out [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio). Murray, Mathurin and Zion Williamson (left thigh contusion) were also out 21 Nov [NBA injury report, 21 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_07_30PM.pdf). No source says the 37-min role lasts once Murphy is back. New Orleans does not play Sun 22. Its next game is Mon 23 vs PHX.
  - **Verdict:** ESPN confirmed: active and healthy. Saturday was a bad shooting night in a blowout, not an injury.

### Daniss Jenkins (DET, PG, us)

- Rate **33.3** · role rate 37.8 · season 30.1 (15) · L7 32.2 (4) · L15 40.7 (7) · L30 31.4 (14)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 29.9 for the season (+7.7)
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- **Research:**
  - Rest: he is not on Detroit's report for Sun 22 Nov at ATL, and Detroit is not on a back-to-back (it last played Fri 20). He has no rest risk Sunday. Duren and Duncan Robinson are out again, Ron Holland is questionable, and Cunningham is probable [NBA injury report, 22 Nov 2:00 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_00AM.pdf); [Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22/).
  - Minutes: unchanged since 21 Nov. He started Fri 20 with Cunningham back and played 39 min [ESPN box score, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308). The role is tied to Duren's absence, and Duren can return 24 Nov at the earliest.
  - **Verdict:** ESPN confirmed: active. The starting role and about 37 min hold for Sun 22.
  - Override proposed: role 37

### Cade Cunningham (DET, PG, us)

- Rate **50.1** · season 50.1 (14) · L7 47.7 (3) · L15 51.7 (6) · L30 50.9 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 22 Nov (Right Knee Soreness, updated 2026-11-21)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Cunningham's status is uncertain for the second half of Detroit's back-to-back set after he played 37 minutes in Tuesday's win over San Antonio."; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Cunningham (knee) is probable to play Sunday in Atlanta.
- News (20 Nov): Cunningham recorded 23 points (10-22 FG, 2-7 3Pt, 1-4 FT), five rebounds, nine assists and one steal over 36 minutes in Friday's 105-102 loss to the Raptors.
- **Research:**
  - He is **probable** for Sun 22 Nov at ATL (right knee soreness) [NBA injury report, 22 Nov 2:00 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_00AM.pdf). RotoWire: "probable to play Sunday in Atlanta" [RotoWire, 21 Nov](https://rotowire.com/basketball/headlines/cade-cunningham-injury-probable-for-sunday-540377); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/cade-cunningham-knee-probable-sunday-vs-atl). Heavy expects him to be upgraded to available before the 3:30 PM ET tip [Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22/).
  - Rest: Sunday is not a back-to-back. He sat the second night of the 17–18 Nov back-to-back, listed with right knee soreness [NBA injury report, 18 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-18_05_30PM.pdf). Rotoworld called that "presumably... a maintenance day" [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/cade-cunningham-knee-probable-sunday-vs-atl). Nothing has been said yet about the Sun 29–Mon 30 Nov back-to-back. He could sit one of those nights.
  - **Expected return:** expected to play Sun 22 (probable, minor soreness). *ESPN est.* 22 Nov.
  - **Verdict:** ESPN confirmed. He should play Sunday, and the rest risk applies to 29–30 Nov, not this week.

### Anthony Black (ORL, PG/SG, us)

- Rate **38.6** · season 38.3 (12) · L7 38.3 (3) · L15 41.4 (7) · L30 38.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- News (19 Nov): Black totaled 15 points (6-16 FG, 2-5 3Pt, 1-3 FT), two rebounds, six assists, one block and one steal in 37 minutes during Wednesday's 121-116 loss to the 76ers.
- **Research:**
  - Orlando plays Sunday at Washington (7 PM ET), not Miami. Orlando had no game Saturday, so Sunday is not a back-to-back. Its Sunday report lists only Banchero (right high ankle sprain; no timetable reported, Sweeney 18 Nov, [Orlando Sentinel via Yahoo, 18 Nov](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html); *ESPN est.* 29 Nov), Isaac, Nelson and Penda as out. Black is not listed. [NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf) · [iHeart, 22 Nov](https://969thegame.iheart.com/content/2026-11-22-magic-vs-wizards-injury-report-nov-22/)
  - Rest flag (28 Nov at WAS, 29 Nov at DET): unchanged since 21 Nov. His only rest this season (2 Nov) was listed as left ankle injury management [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/). Nobody has said he will sit either night.
  - **Verdict:** nothing new found. He is available Sunday at WAS, and his starting role holds while Banchero is out.

### Paul George (BOS, SF/PF, us)

- Rate **37.1** · season 40.6 (14) · L7 35.2 (4) · L15 37.1 (7) · L30 38.2 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (19 Nov): George supplied 10 points (3-12 FG, 1-7 3Pt, 3-3 FT), four rebounds, one assist, one block and three steals across 23 minutes before fouling out of Wednesday's 105-101 loss to Denver.
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - On Saturday at SAC he played 37 min: 19 pts, 8 reb, 5 ast and 4 stl on 6-21 FG (45 FP). Tatum (rest), White (left AC joint; no timetable reported; *ESPN est.* 22 Nov) and Mitchell Robinson (illness; no timetable reported; *ESPN est.* 22 Nov) were all out. [AP via WRAL, 22 Nov](https://www.wral.com/news/ap/7bdcc-murrays-putback-with-5-seconds-left-lifts-kings-to-97-96-win-over-celtics-and-end-8-game-skid/) · [Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/kings_beat_celtics_97_96_as_acuff_scores_21/s1_17668_44599904) For the first time this season, Boston rested Tatum on the first night of a back-to-back instead of the second. Tatum said "we just kind of figure it out as we go." [Yahoo, 21 Nov](https://sports.yahoo.com/articles/celtics-without-3-key-players-233409522.html)
  - Sunday at GSW (8:30 PM ET): Boston's entry was still "not yet submitted" at 2:30 AM ET on 22 Nov [NBA injury report, 22 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf). Neither the team nor the beat has said anything about George for Sunday. His record over 4 earlier back-to-backs: 1 rest ([2 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)) and 1 illness ([11 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_06_00PM.pdf)). Boston's first word on its last two second nights came about 1 PM ET on game day, so Sunday's call could come near or after the 3:30 PM ET add deadline (Mon 7:30 AM Melbourne). No word on 29–30 Nov.
  - Form: L7 35.2 (4 games) is 5.4 under his 40.6 average. The reasons are a 23-min foul-out on 18 Nov, a 25-min blowout on 15 Nov and 6-21 shooting on 21 Nov.
  - **Verdict:** nothing new found. No source says he sits Sunday, so there is no sit row. The 37 min on Saturday keep a rest a real but unconfirmed risk. Check Boston's Sunday report before the deadline.

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:**
  - Unchanged since 21 Nov. The Jazz said on 20 Nov that he has been cleared for on-court work and will be re-evaluated in one week, about 27 Nov ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3); [Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/jazzs-jusuf-nurkic-toe-out-at-least-one-more-week.html)). He is Out for Sun 22 Nov vs DAL with the right 2nd plantar plate tear ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)). I found no report of contact or 5-on-5 work yet.
  - **Expected return:** re-evaluation about 27 Nov, so the first possible game is Sun 29 Nov vs PHX. Utah plays 23 Nov @LAL and 27 Nov vs DEN before that. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date matches the team's one-week re-evaluation, and the 28 Nov row stays as it is.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:**
  - Unchanged since 21 Nov. He was Out again Sat 21 Nov vs BOS with a right patella subluxation ([NBA injury report, 21 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_11_45PM.pdf)). He is "week-to-week" ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)) and progressing with no timeline, per James Ham ([NBC, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)). A French outlet's headline says he has resumed individual training and is "on the right track" ([BeBasket](https://www.bebasket.fr/il-est-sur-le-bon-chemin-un-mois-apres-sa-blessure-maxime-raynaud-a-repris-l-entrainement-individuel); I could read only the headline, so the date is unverified). Sacramento's report for Mon 23 Nov vs SAS is not yet submitted.
  - **Expected return:** no timetable reported. The week-to-week floor is 25 Nov (SAC @GS). *ESPN est.* 25 Nov.
  - **Verdict:** ESPN confirmed, as a floor only. The floor has not passed yet, so the 25 Nov row stays.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **23.8** · role rate 24.0 · season 30.6 (9) · L7 — · L15 14.5 (4) · L30 27.4 (8) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - He was Out again Sat 21 Nov at SAS with a left ankle sprain ([NBA injury report, 21 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_11_45PM.pdf); [Pelicans, 21 Nov](https://www.nba.com/pelicans/news/pelicans-vs-spurs-injury-report-game-preview-11-21-2026)). He sits until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)). The Suns had one five-minute call with "zero traction" and "nothing even remotely close to a deal", per Sam Amick ([Bleacher Report, 20 Nov](https://bleacherreport.com/articles/25535652-new-dejounte-murray-trade-rumors-suns-doing-background-work-amid-jalen-green-links)). Trades are not expected before 15 Dec ([Yahoo, 20 Nov](https://sports.yahoo.com/articles/nba-trade-rumors-2026-27-183612093.html)). I found no trade news after 20 Nov.
  - Gap: he is still listed Out, and the only news is the injury report. Minutes: the drop does not matter while he is not playing.
  - **Expected return:** no timetable reported. He is out until traded. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is a placeholder. The 26 Nov floor row stays because it has not passed (NOP's next game after it is 27 Nov @LAC). Once it passes with him still out, move it to 7 days after the latest out report.

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **14.8** · season 14.2 (5) · L7 — · L15 — · L30 11.0 (4) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:**
  - He was Out again Sat 21 Nov at MIN with a lumbar disc herniation, his 12th straight miss ([NBA injury report, 21 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_11_45PM.pdf); [Heavy, 21 Nov](https://heavy.com/sports/nba/memphis-grizzlies/injury-reprot-vs-timberwolves-november-21)). He is still "week-to-week" with no re-evaluation date ([Grizzlies via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html)). I found no report of practice. Memphis's report for Mon 23 Nov @CHA is not yet submitted.
  - Gap: he is Out, with no news beyond the injury report.
  - **Expected return:** no timetable reported. The week-to-week floor is 23 Nov (MEM @CHA). *ESPN est.* 25 Nov.
  - **Verdict:** nothing new found. The 23 Nov row stays until the floor passes. If he is listed Out for 23 Nov, move it to 7 days after that report (about 30 Nov).

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.1** · season 8.8 (12) · L7 — · L15 3.2 (4) · L30 7.6 (11) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - He was Out Sat 21 Nov at SAS with left plantar fasciitis, his 5th straight miss ([NBA injury report, 21 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_11_45PM.pdf); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/bennedict-mathurin-foot-remains-out-saturday)). There is no timeline. "Week-to-week" is RotoWire's own assessment ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). New Orleans's report for Mon 23 Nov vs PHX is not yet submitted.
  - **Expected return:** no timetable reported. The week-to-week floor is 26 Nov, and NOP's first game after it is 27 Nov @LAC. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date matches the floor. A row would change nothing, so I added none.

---
**Summary**
- Nothing changed availability or role since 21 Nov. All five were Out on 21–22 Nov, and no team gave a new timeline. All four existing return rows stay unchanged (Nurkic 28 Nov, Raynaud 25 Nov, Murray 26 Nov, Pippen 23 Nov).
- Murray is still sitting until he is traded, with "zero traction" on a Suns deal (20 Nov). ESPN's 27 Nov is a placeholder, and the 26 Nov floor moves once it passes.
- Pippen's 23 Nov floor is unsupported by any practice news. If Memphis lists him Out for Mon 23 Nov @CHA, move the row to about 30 Nov. Nurkic stays effectively 29 Nov (re-evaluation about 27 Nov), and Mathurin stays at 27 Nov (ESPN, no row).

### Brayden Burries (MIL, SG, free agent)

- Rate **30.1** · season 24.5 (17) · L7 36.2 (4) · L15 30.9 (9) · L30 25.0 (16) · projected 22.2
- ESPN: active
- **Role:** news on 21 Nov: "Burries is not in the Bucks' starting lineup against the 76ers on Saturday."
- News (21 Nov): Burries ended with 26 points (12-20 FG, 2-6 3Pt, 0-1 FT), eight rebounds, four assists and one block over 26 minutes off the bench during Saturday's 132-129 loss to the 76ers.
- News (21 Nov): Burries is not in the Bucks' starting lineup against the 76ers on Saturday.
- **Research:**
  - Sat 21 Nov at PHI: he came off the bench after 10 straight starts. Ryan Rollins, back from an illness that cost him two games, moved into the starting five with Jaquez ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/mil-starts-rollins-herro-jaquez-kuzma-turner)). Burries still played 26 min, his 26.5-min starter average, and scored a career-high 26 pts (12-20 FG, 8 reb, 4 ast). He also played the whole fourth quarter ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-pours-in-career-high-26-on-saturday/); [Behind the Buck Pass, 21 Nov](https://behindthebuckpass.com/blown-call-tyler-herros-eruption-overshadow-brayden-burries-breakout)).
  - Ongoing or one-off is unclear. RotoWire says Jenkins "might continue to mix and match" next to Herro during a 12-game losing streak, and no source says who starts next. His minutes held up either way. Milwaukee is idle Sunday and next plays Mon 23 Nov at TOR.
  - **Verdict:** ESPN confirmed. He moved to the bench but kept his minutes, so I added no row.

### Jaxson Hayes (UTAH, C, free agent)

- Rate **29.7** · season 28.3 (14) · L7 34.5 (2) · L15 28.7 (7) · L30 27.0 (13) · projected 16.5
- ESPN: active
- **Role:** news on 20 Nov: "Hayes is listed in the starting lineup for Friday's game against the Suns."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (21 Nov): Hayes produced 18 points (7-8 FG, 4-8 FT) and 14 rebounds in 28 minutes during Friday's 111-101 loss to Phoenix.
- News (20 Nov): Hayes is listed in the starting lineup for Friday's game against the Suns.
- **Research:**
  - Utah's Sunday report (vs DAL) lists Jackson Jr. (MCL; mid-December; *ESPN est.* 14 Dec), Markkanen (hand fracture; *ESPN est.* 4 Jan), Nurkic and three two-way players as out. Hayes is not on it, so his 20 Nov hip knock has not cost him Sunday. Utah had no game Saturday. [NBA injury report, 22 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)
  - Role: the start goes on while Nurkic is out (re-evaluated 27 Nov [Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3); *ESPN est.* 29 Nov) [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jazz-start-keyonte-darryn-green-ace-hayes). Expect about 26 min. Sunday's starters are not announced yet.
  - Rest: Sunday is the first night of the 22–23 Nov back-to-back, and Monday at LAL falls after our matchup. He has no rest pattern; his 26 Oct absence was shoulder soreness [NBC Sports, 27 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/jaxson-hayes-shoulder-questionable-wednesday).
  - Form: L7 34.5 rests on 2 games (small sample) and is 6.2 over his 28.3 average. He is back in the starting five, with 18 pts and 14 reb on 20 Nov [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jaxson-hayes-with-18-and-14-rebounds-in-loss).
  - **Verdict:** ESPN confirmed. He is available Sunday and expected to start.

---
**Summary**
1. George and Queta have no Sunday status yet. Boston's GSW report was not submitted as of 2:30 AM ET, and neither the team nor the beat has said anything. Boston rested Tatum on Saturday (the first night), and George played 37 min. A rest is possible for either but unannounced, and the call may land near or after the 3:30 PM ET deadline (Mon 7:30 AM Melbourne).
2. Black is clear for Sunday at Washington (not Miami). Hayes is clear vs DAL: he is not on Utah's report despite the hip knock, and he is starting.
3. Huerter keeps the start Sunday at ATL with Duncan Robinson listed out (re-eval about 24 Nov; *ESPN est.* 27 Nov). Our Jalen Duren is also out Sunday (*ESPN est.* 24 Nov).
  - Override proposed: role 26

### Jakob Poeltl (TOR, C, free agent)

- Rate **29.4** · season 26.4 (14) · L7 28.5 (4) · L15 33.4 (8) · L30 27.2 (13) · projected 31.7
- ESPN: active
- **Role:** news on 18 Nov: "Poeltl will start Wednesday's game against the Wizards."
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:**
  - Unchanged since 21 Nov. He started 18 and 20 Nov (32 min, 10 pts, 9 reb at DET) while Collin Murray-Boyles was in the concussion protocol ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl); [NBA.com, 20 Nov](https://www.nba.com/news/raptors-updates-barrett-murray-boyles)).
  - I found no clearance news for Murray-Boyles (*ESPN est.* 23 Nov, day-to-day; the Raptors gave no timetable, only a return-to-participation process) ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-lands-in-concussion-protocol/)). Toronto is idle Saturday and Sunday and next plays Mon 23 Nov vs MIL. Expect about 30 min while Murray-Boyles is out and about 18 off the bench once he's back.
  - **Verdict:** ESPN confirmed. The start lasts only while Murray-Boyles is out, so I added no row.

Summary:
1. Pritchard started Sat (34 min, 22 FP) with Tatum and White out. Sunday at GS hinges on White (*ESPN est.* 22 Nov, no timetable reported; Boston not filed as of 2:15 AM ET), and the call may come after Sunday's 3:30 PM ET first tip-off. Tatum is expected back.
2. Washington (illness, plus left shoulder impingement) missed Sat. Dallas had not filed for Sun at UTA as of 2:15 AM ET, so he is a game-day call (*ESPN est.* 22 Nov, no timetable reported).
3. Burries (bench, still 26 min), Queen (one start while Zion is out, *ESPN est.* 23 Nov) and Poeltl (starts until Murray-Boyles is cleared, *ESPN est.* 23 Nov) are all idle Sunday. No override rows.

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.4** · role rate 32.2 · season 23.9 (15) · L7 30.0 (4) · L15 32.6 (7) · L30 24.9 (14) · projected 22.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 13 before; 36.0 min in his starts, against 26.7 for the season
- **Minutes:** 36.0 min over his last 3 games against 26.7 for the season (+9.3)
- News (21 Nov): Huerter chipped in 20 points (7-15 FG, 4-8 3Pt, 2-3 FT), three rebounds, three assists and one steal across 36 minutes during Friday's 105-102 loss to Toronto.
- News (19 Nov): Huerter had 11 points (2-9 FG, 1-4 3Pt, 6-7 FT), one rebound, seven assists, one block and one steal across 36 minutes during Wednesday's 122-109 victory over New Orleans.
- **Research:**
  - Duncan Robinson (left quad strain) is listed out for Sunday at ATL (3:30 PM ET). Huerter is not on the report, and Detroit had no game Saturday. [NBA injury report, 22 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf) Heavy says Robinson and Duren are "closer to returning, possibly later this week depending on their re-evaluations" [Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22/). Huerter should make a fourth straight start; he played 36, 36 and 36 min in the first three [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kevin-huerter-scores-20-points-as-starter).
  - Robinson's return ends the role. He is re-evaluated about 24 Nov [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-duncan-robinson-to-be-re-evaluated-in-one-week/) (*ESPN est.* 27 Nov). Detroit next plays Tue 24 at ORL. Jalen Duren (ours; right hamstring; "possibly later this week", Heavy; *ESPN est.* 24 Nov) is also out Sunday. Cunningham is probable (right knee soreness).
  - Form: L7 30.0 (4 games) is 6.1 over his 23.9 average, from the starting role at 36 min.
  - **Verdict:** ESPN confirmed. He starts Sunday at ATL and keeps the role until Robinson returns, 24 Nov at the earliest.
  - Override proposed: role 35

### Derik Queen (NO, PF/C, free agent)

- Rate **28.2** · role rate 43.2 · season 26.9 (18) → 28.3 (17) · L7 29.6 (5) · L15 23.6 (10) → 25.9 (9) · L30 26.6 (17) → 28.1 (16) · projected 30.5
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 16 before; 35.0 min in his starts, against 22.2 for the season
- **Role:** news on 21 Nov: "Queen will start Saturday against the Spurs."
- News (21 Nov): Queen will start Saturday against the Spurs.
- News (17 Nov): Queen delivered 17 points (6-9 FG, 4-5 3Pt, 1-2 FT), 10 rebounds and one block across 20 minutes in Monday's 115-94 win over the Warriors.
- **Research:**
  - Sat 21 Nov at SA: he made his first start of the season because Zion Williamson was a late scratch (left thigh contusion) on the second night of a back-to-back ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/nor-starts-fears-jones-bey-queen-missi); [CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-zion-williamson-not-playing-saturday/)). He had 15 pts and 15 reb in 35 min in the 114-91 loss ([ClutchPoints, 21 Nov](https://clutchpoints.com/nba/san-antonio-spurs/spurs-news-victor-wembanyama-joins-historic-company-50-point-statement-win-pelicans)).
  - The start is tied to Zion. The Pelicans gave no timetable (*ESPN est.* 23 Nov). FanDuel Research lists Zion out for Mon 23 Nov vs PHX but names no source ([FanDuel, 22 Nov](https://www.fanduel.com/research/nba/player-news/injuries/zion-williamson-out-november-23-2026-against-suns-thigh)). If that holds, Queen likely starts again Monday. Zion's return ends it, and Queen then goes back to about 20 min off the bench. New Orleans is idle Sunday.
  - **Verdict:** ESPN confirmed. The start is a one-off while Zion is out, and no source calls it ongoing, so I added no row.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.3** · role rate 29.7 · season 26.8 (13) · L7 26.0 (1) · L15 29.0 (4) · L30 26.4 (12) · projected 26.6
- ESPN: day-to-day, ESPN est. 23 Nov (Concussion, updated 2026-11-21)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- News (17 Nov): Allen (concussion-like symptoms) has been ruled out for Tuesday's game against the Lakers.
- **Research:**
  - Injury: unchanged since 21 Nov. He is in the NBA's concussion protocol after missing 17 and 20 Nov. He "will have to pass a series of checkpoints and show he's symptom-free" before he is cleared, and no timeline has been given ([Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html); [NBA injury report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_30PM.pdf)). ESPN changed his tag from Out to Day-To-Day on 21 Nov, but I found no report that he has cleared a step. Charlotte has no game on 21 or 22 Nov, and its report for Mon 23 Nov vs MEM was not yet submitted ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)).
  - Role: his starts came while Miller (groin) was out, and he went back to the bench on 15 Nov. On 17 Nov Charlotte started big with Grant Williams, who NBC expects to "move back to the bench when Allen returns" ([NBC Sports, 19 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-minutes-report-how-injuries-to-austin-reaves-alperen-sengun-shake-up-two-contenders)). Knueppel (hamstring) is out at least four weeks from 8 Nov, so a re-evaluation about 6 Dec (*ESPN est.* 12 Dec) ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/)). Once he is cleared, expect about 25–27 min, mostly off the bench.
  - **Expected return:** no timetable reported (concussion protocol). *ESPN est.* 23 Nov, which is Charlotte's next game (vs MEM), not a reported date.
  - **Verdict:** nothing new found. No report supports the Day-To-Day tag or 23 Nov, and he still has to clear the protocol.

### Payton Pritchard (BOS, PG/SG, free agent)

- Rate **27.3** · role rate 32.0 · season 26.0 (16) · L7 27.2 (4) · L15 27.2 (8) · L30 26.1 (15) · projected 31.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 14 before; 34.0 min in his starts, against 27.6 for the season
- **Role:** news on 21 Nov: "Pritchard will start in Saturday's game against the Kings."
- News (21 Nov): Pritchard will start in Saturday's game against the Kings.
- News (19 Nov): Pritchard had 15 points (6-11 FG, 3-6 3Pt), one rebound and two assists over 30 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:**
  - Role (Sat 21 Nov): he started at SAC, his first start of 2026-27. Tatum (rest), Derrick White (left AC joint contusion) and Mitchell Robinson (illness) were out, and Pritchard and Hauser took the two open spots ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/bos-starts-pritchard-hugo-george-hauser-queta); [Boston.com, 21 Nov](https://boston.com/sports/boston-celtics/2026/11/21/3-celtics-including-jayson-tatum-ruled-out-ahead-of-matchup-with-kings)). He played 34 min for 22 FP and went 0-8 from three in the 97-96 loss. He hit the go-ahead shot with 11.8 s left and missed at the buzzer ([CBS Sports, 22 Nov](https://www.cbssports.com/nba/news/kings-edge-celtics-to-snap-8-game-skid-on-keegan-murrays-putback/); [NBC Sports Boston, 22 Nov](https://www.nbcsportsboston.com/nba/boston-celtics/live-updates-kings-highlights-score-sacramento/815068/)).
  - Sun 22 Nov at GS (8:30 PM ET): RotoWire says Tatum "should be back" ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/jayson-tatum-news-wont-play-saturday-540368)). If Tatum returns, the start rides entirely on White (*ESPN est.* 22 Nov, no timetable reported; the team gave no update after Saturday). Boston had not filed for Sunday as of 2:15 AM ET ([NBA injury report, 22 Nov 2:15 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)). Sunday's first tip-off is 3:30 PM ET (DET@ATL), so the White call could come after the add deadline. If White plays, expect Pritchard back on the bench at about 27–28 min. If White sits, he likely starts at about 32–34 min.
  - **Verdict:** ESPN confirmed. The start is a one-off tied to Tatum's and White's absences, and no source calls it ongoing, so I added no row.

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **22.4** · role rate 25.8 · season 19.2 (8) · L7 26.0 (1) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-19)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- News (18 Nov): Tyson (ankle) has been ruled out for Wednesday's game against Memphis.
- **Research:**
  - Injury: unchanged since 21 Nov. He missed 16, 18 and 20 Nov with "Right Ankle Injury Management" ([NBA injury report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_30PM.pdf)), and the Cavs have given no timetable ([Heavy, 20 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/injury-report-pacers-game-november-20)). Cleveland had the weekend off, and its next game is Mon 23 Nov at CHI ([Cavaliers, 20 Nov](https://www.nba.com/cavaliers/news/preview-indcle-261120)). Its report for that game was not yet submitted ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)). I found no practice news from 21–22 Nov.
  - Role and minutes: his two starts (30 and 34 min) came "sans Mobley" ([NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/cle-starts-harden-mitchell-tyson-watson-allen)). Evan Mobley (left great toe) is re-evaluated after 7–10 days of rehab from 16 Nov ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116); *ESPN est.* 29 Nov). The start ends when Mobley returns. No source gives Tyson's minutes when he comes back.
  - **Expected return:** no timetable reported. His next chance is Mon 23 Nov at CHI. *ESPN est.* 23 Nov.
  - **Verdict:** nothing new found. 23 Nov is only his next chance, and no source confirms or contradicts it.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **33.8** · role rate 31.0 · season 24.1 (15) · L7 44.8 (4) · L15 34.5 (6) · L30 23.8 (14) · projected 28.1
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 29.1 for the season (+8.3)
- News (21 Nov): Grimes logged 13 points (2-7 FG, 1-5 3Pt, 8-9 FT), five rebounds and seven assists in 35 minutes during Friday's 106-104 victory over the Kings.
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- **Research:**
  - Minutes: these still come from the starting role he took while Reaves is out. Austin Reaves (left heel contusion/bone bruise) missed his fourth straight game on 20 Nov. Redick: "Hopefully he'll be back in one of the next two games", meaning Mon 23 Nov vs UTA or Fri 27 Nov at SAS ([ClutchPoints, 20 Nov](https://clutchpoints.com/nba/los-angeles-lakers/lakers-news-jj-redick-optimistic-update-austin-reaves-injury-return-timetable); [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/lakers-austin-reaves-expected-to-return-monday-or-friday/)). A 21 Nov LA Sports Report piece repeats this but calls the Spurs game Wednesday. ESPN's schedule has LAL at SAS on Fri 27 Nov ([Yahoo/LA Sports Report, 21 Nov](https://sports.yahoo.com/articles/austin-reaves-given-return-timeline-220000816.html)). The Lakers' report for 23 Nov was not yet submitted ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)).
  - Role once Reaves returns: NBC expects Reaves's return to "push Matisse Thybulle to the bench and limit usage for Quentin Grimes" ([NBC Sports, 19 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-minutes-report-how-injuries-to-austin-reaves-alperen-sengun-shake-up-two-contenders)). Lakers Nation sees him as a key piece "coming off the bench" ([Lakers Nation, 16 Nov](https://lakersnation.com/quentin-grimes-embraced-bigger-offensive-role-with-austin-reaves-out/)). Sources disagree on whether he keeps the start, but they agree his usage falls. LAL has no game on 21 or 22 Nov.
  - **Expected return (Reaves):** hoped for 23 Nov or 27 Nov (Redick, 20 Nov). *ESPN est.* 23 Nov.
  - **Verdict:** nothing new found. The big role lasts only until Reaves returns, possibly Mon 23 Nov, so no row.

### Caleb Wilson (CHI, SF, free agent)

- Rate **31.6** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 37.2 (9) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Injury: the Bulls say his 12 Nov hand surgery was successful and that he "will be re-evaluated in three weeks", which is about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). New: an AP story on 21 Nov says he is still expected to miss four to six weeks. He is running and working on his left hand, and he said "I'll play again in a couple weeks" ([AP via Yahoo, 21 Nov](https://sports.yahoo.com/articles/bulls-rookie-caleb-wilson-looking-012217305.html)). SI expects the next real update at the re-evaluation on 3 Dec ([SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20)). He is Out for Sun 22 Nov vs DEN with a right metacarpal fracture ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)).
  - Minutes flag: the 23.0-min L3 figure reflects his 15-min injury exit on 11 Nov. It does not matter while he is out.
  - **Expected return:** at least four to six weeks from 12 Nov, so 10–24 Dec, with a re-evaluation about 3 Dec. Chicago plays 3 Dec vs CLE and then not again until 13 Dec vs HOU. *ESPN est.* 13 Dec.
  - **Verdict:** ESPN confirmed. "A couple weeks" is the player's own view, and the team's timeline has not changed.

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **29.0** · role rate 23.4 · season 28.2 (15) · L7 29.3 (3) · L15 28.3 (7) · L30 29.2 (14) · projected 26.9
- ESPN: out, ESPN est. 22 Nov (Illness, updated 2026-11-21)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (21 Nov): Washington (illness/shoulder) is listed as out for Saturday's game against the Clippers.
- News (21 Nov): Washington (illness/shoulder) has been downgraded from questionable to doubtful ahead of Saturday's game against the Clippers.
- **Research:**
  - He missed Sat 21 Nov vs LAC, his first absence of the season. Friday's report had him questionable with left shoulder impingement. Saturday he was downgraded to doubtful, then out, with an illness ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-p-j-washington-downgraded-to-out-540388/); [Dallas Sports Journal, 21 Nov](https://dallassportsjournal.com/pj-washington-out-walter-clayton-available-mavericks-clippers/)). Risacher started in his place in the 110-100 win ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/dal-start-irving-flagg-martin-risacher-gafford); [ESPN recap, 21 Nov](https://www.espn.com/nba/recap?gameId=401910025)).
  - Sun 22 Nov at UTA (7:00 PM ET, second night of a back-to-back): Dallas had not filed as of 2:15 AM ET ([NBA injury report, 22 Nov 2:15 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)). No source says whether he will play. He played both nights of the 14–15 Nov back-to-back.
  - Minutes flag: unchanged since 21 Nov. The dip came from blowouts and foul trouble, not a role change ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/p-j-washington-shoulder-questionable-vs-lac)).
  - **Expected return:** no timetable reported; Sunday at UTA is a game-day call. *ESPN est.* 22 Nov.
  - **Verdict:** nothing new found. ESPN's 22 Nov estimate is plausible but unconfirmed, with both the illness and the shoulder in play.

### Dean Wade (PHI, PF, free agent)

- Rate **27.1** · role rate 27.1 · season 21.5 (13) · L7 39.5 (2) · L15 21.0 (6) · L30 21.5 (13) · projected 16.3
- ESPN: out, ESPN est. 23 Nov (Left Hamstring Soreness, updated 2026-11-20)
- **Minutes:** 33.7 min over his last 3 games against 26.7 for the season (+7.0)
- News (20 Nov): Wade (hamstring) won't play Saturday against the Bucks.
- News (20 Nov): Wade (hamstring) participated in Friday morning's practice without restrictions, an encouraging sign for his availability for Saturday's game against the Bucks, per Tony Jones of The Athletic.
- **Research:**
  - Injury: he was Out Sat 21 Nov vs MIL with left hamstring tightness/soreness, his second straight miss ([NBA injury report, 21 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_11_45PM.pdf); [Yahoo, 21 Nov](https://sports.yahoo.com/articles/bucks-vs-76ers-injury-report-155845075.html)). He practised fully on 20 Nov, but the medical staff was "not quite ready to clear him". His next chance is Mon 23 Nov vs POR ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/dean-wade-injury-ruled-out-for-saturday-540198)). I found no update after Saturday's game. Philadelphia's report for 23 Nov was not yet submitted ([NBA injury report, 22 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_15AM.pdf)). PHI has no game on Sun 22 Nov.
  - Minutes: unchanged since 21 Nov. His 32–35 min games were spot starts for LeBron James, and Rotoworld advises streaming him mainly when he starts ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/dean-wade-hamstring-remains-out-vs-milwaukee)). No source calls the bigger role ongoing. L7 39.5 rests on 2 games (small sample).
  - **Expected return:** his next chance is Mon 23 Nov vs POR (RotoWire, 20 Nov), with no firm timetable. *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. A full practice and "next chance Monday" fit 23 Nov, but he has not been cleared yet.

---
**Summary**
- No availability or role change since 21 Nov. None of the five can play Sun 22 Nov: CHA, CLE, LAL and PHI are idle, and Wilson is Out for CHI vs DEN. The 23 Nov reports for CHA, CLE, LAL and PHI were not yet submitted.
- Allen's ESPN tag moved from Out to Day-To-Day on 21 Nov with no reported news, and he still has to clear the concussion protocol. Tyson and Wade both aim for Mon 23 Nov with no confirmation. If Tyson is out again on 23 Nov, the Tyrese Proctor role row, which ends 22 Nov, would need extending.
- Grimes keeps the starting role only until Reaves returns. Redick hopes for 23 Nov or 27 Nov (*ESPN est.* 23 Nov), and NBC expects Grimes' usage to drop afterwards. Wilson's timeline is unchanged: re-evaluation about 3 Dec, first realistic game 13 Dec (*ESPN est.* 13 Dec). No override rows.

### Neemias Queta (BOS, C, free agent)

- Rate **30.9** · season 27.4 (15) · L7 35.0 (3) · L15 29.3 (7) · L30 27.9 (14) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- News (17 Nov): Queta (rest) is available for Wednesday's game against the Nuggets, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - On Saturday at SAC he started and scored 15 pts in 30 min (29 FP), with Mitchell Robinson (illness; no timetable reported; *ESPN est.* 22 Nov) out [640 WXSM/AP, 22 Nov](https://www.640wxsm.com/2026/11/22/keegan-murray-plays-hero-to-lead-kings-past-celtics-for-first-home-win/) · [AP via WRAL, 22 Nov](https://www.wral.com/news/ap/7bdcc-murrays-putback-with-5-seconds-left-lifts-kings-to-97-96-win-over-celtics-and-end-8-game-skid/).
  - Sunday at GSW: Boston's entry was "not yet submitted" at 2:30 AM ET on 22 Nov [NBA injury report, 22 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf), and neither the team nor the beat has said anything. His only rest came on the second night of 15–16 Nov, "as Boston manages his workload" [NESN, 16 Nov](https://nesn.com/boston-celtics/news/why-neemias-queta-isnt-playing-tonight-vs-magic/4d25961bd26a8a5079076ef0). He played both nights of the other back-to-backs. If Robinson is still ill, Garza is Boston's only other center. That call usually comes about 1 PM ET on game day, near the 3:30 PM ET deadline. No word on 29–30 Nov.
  - Form: L7 35.0 (3 games) is 7.6 over his 27.4 average, from 27–30 min starts with Robinson out. Three games is a short window.
  - **Verdict:** nothing new found. He is a possible but unannounced Sunday rest (1 rest in 5 back-to-backs), so there is no sit row.

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
- **Research:**
  - Healthy. He is not on OKC's official report for Sun 22 Nov at MIA (6:00 PM ET). Jaylin Williams (low back spasms; no timetable reported, *ESPN est.* 23 Nov) is out again, as are Caruso and Holmgren ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf); [Heavy, 21 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-heat-november-22/)). SGA is questionable (back contusion and neck strain, *ESPN est.* 22 Nov). Mara's spot does not depend on SGA.
  - Role: unchanged since 21 Nov. He is a "fixture in the starting lineup with Chet Holmgren (knee) sidelined," and he started on 18 and 20 Nov (22 pts, 16 reb, 29 min on 20 Nov) ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/); [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/thunder-start-shai-ajay-mccain-peavy-i-hart)). He played 26, 27 and 29 min in his last three games, starting or off the bench. Holmgren is out 8–10 weeks from 30 Oct ([AP/NBA.com, 31 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan). His return ends the role. OKC also plays Mon 23 at IND, the second night of a back-to-back.
  - **Verdict:** ESPN confirmed. He is active and expected to start Sunday. The existing role row of 27 min stands unchanged.
  - Override proposed: role 27

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **28.1** · season 32.6 (14) · L7 21.3 (3) · L15 30.4 (7) · L30 32.6 (14) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (20 Nov): Podziemski closed with 15 points (5-12 FG, 0-5 3Pt, 5-6 FT), three rebounds, two assists and one steal in 32 minutes during Thursday's 126-98 loss to the Grizzlies.
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- **Research:**
  - He is not on Golden State's official report for Sun 22 Nov vs BOS (8:30 PM ET) ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). GS has not played since 19 Nov.
  - Minutes: unchanged since 21 Nov. His one short game (22 min, 13 Nov) came in a 123-85 blowout at SA ([StatMuse box, 13 Nov](https://www.statmuse.com/nba/game/11-13-2026-gsw-at-sas-78603)). He has played "roughly 30 minutes per game recently" ([CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-three-point-drought-extends-in-loss/)), and he played both nights of the 18–19 Nov back-to-back (29, 32 min). The dip in output comes from his shooting (0-10 from three in his last two games), not his minutes.
  - Curry (oblique tear) is to be re-evaluated two weeks after his 12–13 Nov MRI, so about 26 Nov ([NBA.com, 13 Nov](https://www.nba.com/news/stephen-curry-out-abdominal-soreness); *ESPN est.* 12 Dec). Podziemski's extra usage lasts until Curry is back.
  - **Verdict:** nothing new found. He is active, with steady minutes of about 30 and no role row.

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **42.2** · season 44.9 (16) · L7 38.3 (3) · L15 42.9 (7) · L30 44.4 (15) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 18 Nov: "Kessler will return to action after being held out of the front end of this back-to-back set."; sat the first night of the 17–18 Nov back-to-back, playing the games either side
- News (21 Nov): Kessler notched 15 points (7-11 FG, 1-1 3Pt, 0-2 FT), seven rebounds, two assists, three blocks and one steal in 30 minutes during Friday's 106-104 win over Sacramento.
- News (19 Nov): Kessler notched 10 points (3-7 FG, 4-10 FT), 11 rebounds and one assist in 31 minutes during Wednesday's 109-97 loss to the Jazz.
- **Research:**
  - He plays for the Lakers. LAL had no game Sat 21 and has none Sun 22. Their next game is Mon 23 Nov vs UTA (10:00 PM ET), which is on the 23 Nov slate of the [NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf). So he has no game left in this matchup week. His latest game was 15 pts, 7 reb and 3 blk in 30 min on 20 Nov, with no injury mentioned ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/walker-kessler-with-15-and-three-blocks-in-win)).
  - Rest flag: the 17 Nov absence was an injury (right lower-leg soreness), not rest. It was his first absence after playing all of his first 14 games ([NBA.com, 17 Nov](https://www.nba.com/news/lakers-rule-out-reaves-kessler-vs-hornets)), and he was off the report on 18 Nov ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/walker-kessler-leg-off-injury-report-wednesday)). That means he played both nights of LAL's back-to-backs on 27–28 Oct, 1–2 Nov and 8–9 Nov. Nothing has been said about Sun 29–Mon 30 Nov.
  - **Verdict:** ESPN confirmed. He is active with no rest pattern, and he does not play Sunday because LAL has no game.

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **41.5** · season 36.3 (16) → 38.5 (15) · L7 36.5 (4) → 47.7 (3) · L15 34.5 (8) → 39.0 (7) · L30 36.0 (15) → 38.4 (14) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (21 Nov): Herro recorded 50 points (15-23 FG, 7-12 3Pt, 13-13 FT), 11 rebounds, seven assists and one steal over 40 minutes during the Bucks' 132-129 loss to the 76ers on Saturday.
- News (20 Nov): Herro totaled 19 points (7-13 FG, 4-7 3Pt, 1-3 FT), four rebounds, three assists and one steal over 31 minutes during Thursday's 124-114 loss to Portland.
- **Research:**
  - On 21 Nov at PHI he had a career-high 50 pts (15-23 FG, 7-12 3Pt, 13-13 FT), 11 reb and 7 ast in 40 min, a 132-129 loss. No injury or physical issue was reported ([Yahoo/AP, 21 Nov](https://sports.yahoo.com/articles/tyler-herro-career-high-50-210608557.html)). The L7 jump rests on this one game.
  - Milwaukee is not on the Sunday 22 Nov slate. Their next game is Mon 23 at TOR, 7:30 PM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). Saturday was his last game of this matchup week.
  - Rest flag: unchanged since 21 Nov. The 10 Nov absence was a right knee contusion ([SI, 9 Nov](https://www.si.com/nba/bucks/onsi/the-latest-on-tyler-herro-before-bucks-face-new-york-knicks-01m7151s3wta)). He played both nights of the 23–24 Oct and 18–19 Nov back-to-backs (24 and 31 min on the second). Nothing has been said about 27–28 Nov.
  - **Verdict:** ESPN confirmed. He is healthy, has no rest pattern, and has no game Sunday.

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.5** · season 39.2 (15) · L7 41.0 (3) · L15 41.6 (7) · L30 39.1 (14) · projected 41.1
- ESPN: day-to-day, ESPN est. 22 Nov (Left Hip Soreness, updated 2026-11-21)
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Siakam (hip) is listed as questionable for Sunday's game against New York.
- News (18 Nov): Siakam chipped in 24 points (10-17 FG, 2-2 3Pt, 2-2 FT), four rebounds, three assists, one block and three steals across 33 minutes during Wednesday's 119-104 loss to the Rockets.
- **Research:**
  - He is questionable for Sun 22 Nov at NYK (8:00 PM ET) with left hip soreness/tightness. The listing first appeared on Saturday's report and was unchanged at 2:30 AM ET Sunday ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf); [IndyStar via Yahoo, 21 Nov](https://sports.yahoo.com/articles/pacers-more-bad-news-injury-223350334.html)). No coach or team update and no cause have been given. He played 30 min on 20 Nov. If he sits, Obi Toppin may start ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-pascal-siakam-questionable-versus-knicks/)).
  - Rest flag: IND plays Sun 22 at NYK and Mon 23 vs OKC. He sat for rest on 2 Nov, the second night of a back-to-back ([Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/pacers-resting-pascal-siakam-could-183414500.html)), and he played both nights of 25–26 Oct. No sit has been announced for 23 Nov or 27–28 Nov. The hip adds risk on Monday, but no source says so.
  - **Expected return:** no timetable reported. Sunday at NYK is a game-day call. *ESPN est.* 22 Nov.
  - **Verdict:** ESPN confirmed. Day-to-day matches the official questionable listing, and nothing has been announced for Monday.

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
