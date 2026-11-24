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
- **Research:**
  - He is **out** for Tue 24 at ORL (right hamstring strain) on the official report [NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf). He was due a re-evaluation around Sun 22 (two weeks after the 8 Nov update), but "there hasn't been another update to his status" [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/jalen-duren-hamstring-remains-out-vs-orlando). RotoWire calls him week-to-week until the Pistons give an update. The 8 Nov update had cleared him for on-court work, and Bickerstaff said "we're not going to rush him" ([NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring)). No re-evaluation result had been reported by 24 Nov.
  - Detroit's other games this week are Fri 27 vs MIL and Sun 29 vs ORL. No source puts him in line for either game.
  - **Expected return:** no timetable reported (the re-evaluation result is still pending). The floor is 1 Dec, 7 days after the 24 Nov out report. *ESPN est.* 30 Nov.
  - **Verdict:** ESPN confirmed as a floor: he is out at least through Sun 29, so all of this matchup week. The old 24 Nov row has expired. The new row sits one day after ESPN's date, and the two differ only on DET's Mon 30 game, which falls next week.
  - Override proposed: return 2026-12-01

### Paul George (BOS, SF/PF, us)

- Rate **39.0** · season 40.6 (14) · L7 38.0 (3) · L15 40.3 (6) · L30 38.7 (12) · projected 38.5
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "George (rest) has been ruled out for Sunday's game against Golden State, Justin Turpin of WEEI.com reports."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports."; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (23 Nov): George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports.
- News (22 Nov): George (rest) has been ruled out for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:**
  - The "injury" flag is the old rest night, not a new injury. He sat Sun 22 at GSW on the second night of a back-to-back, listed "Rest - OUT" ([Celtics on X, 22 Nov](https://x.com/celtics/status/2124605900090654930)). He is **not on the report** for Tue 24 at WSH ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/paul-george-rest-off-injury-report-vs-wizards)). Sam Hauser goes back to the bench.
  - Rest: Boston plays Tue 24, Fri 27 and Sun 29 this week, with no back-to-back, so he should play all three. Sun 29 is the first night of the 29–30 Nov back-to-back. He has sat the second night of 3 of his 5 back-to-backs (2 Nov rest, 11 Nov illness, 22 Nov rest), so Mon 30 (next week) is a real pattern risk. Nothing has been announced. Form: L7 38.0 (3), season 40.6 (14), not 5+ off.
  - **Verdict:** ESPN confirmed: active, plays Tue 24. The flag repeats the 22 Nov rest night.

### Jalen Smith (CHI, PF/C, us)

- Rate **42.8** · season 37.4 (15) → 39.4 (14) · L7 47.0 (4) · L15 46.6 (7) · L30 36.8 (13) → 39.0 (12) · projected 22.4
- ESPN: active
- **Minutes:** news on 20 Nov: "His absence would leave additional playing time available for Zach Collins and Nic Claxton, though Claxton still appears to be on a minutes restriction."
- News (23 Nov): Smith (illness) will play Monday against the Cavaliers, K.C. Johnson of Chicago Sports Network reports.
- News (23 Nov): Smith (illness) is probable for Monday's game against Cleveland.
- **Research:**
  - He played Mon 23 vs CLE while ill. He was cleared, but Splitter said he would be "cautious" with his minutes after his 34 on Sunday ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-good-to-go-monday/)). He **started at center** and played 25 min, scoring 11 pts on 4-7 FG (31 FP) in a 122-108 win. Nic Claxton (back from illness) came off the bench for 23 min ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-waive-center-after-beating-the-cavs)).
  - Minutes: Monday's 25 came from the illness and a deliberate cut after Sunday's 34-min overtime game, not from a role change. He keeps the starting job with Claxton playing, as Rotoworld reported on 22 Nov (unchanged since 23 Nov). Expect his usual 28–32 when healthy. L7 47.0 (4) is 9.6 over his 37.4 season average, from the starting role and hot 3PT shooting. Chicago's report for Wed 25 at CHA was not yet submitted at 2:00 AM ET 24 Nov.
  - **Verdict:** ESPN confirmed: active and starting. The 25 min on Monday was a one-off.

### Trey Murphy III (NO, SG/SF, us)

- Rate **33.7** · season 31.1 (11) · L7 31.5 (2) · L15 35.7 (3) · L30 33.8 (9) · projected 36.8
- ESPN: active
- **Minutes:** news on 21 Nov: "Expect his minutes to ramp up quickly, and once he's fully back, he should rejoin a starting lineup that has struggled to find consistent scoring."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "Murphy was deployed off the bench Friday against the Thunder in his first action since Nov. 8 but was then held out Saturday in San Antonio for the second half of a back-to-back in an effort to ease him back into action following a six-game absence due to bilateral patellar tendinopathy."; sat the second night of the 20–21 Nov back-to-back, playing the games either side
- News (24 Nov): Murphy totaled nine points (4-14 FG, 1-6 3Pt), nine rebounds, two assists and two steals across 35 minutes during Monday's 123-119 overtime loss to the Suns.
- News (23 Nov): Murphy is starting Monday's game against Phoenix.
- **Research:**
  - He **started** Mon 23 vs PHX, which sent Saddiq Bey back to the bench ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-returning-to-starting-five/)). After shootaround he said he felt "pretty good, ready to go" ([Pelicans.com, 23 Nov](https://nba.com/pelicans/news/pelicans-shootaround-update-three-players-are-probable-for-phoenix-game-who-were-dnps-saturday)). He played 35 min (overtime) with 9 pts (4-14 FG), 9 reb, 2 ast and 2 stl, 25 FP, in a 123-119 OT loss. No minutes limit is mentioned ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-low-usage-continues-monday/)). The minutes ramp is done (29 off the bench, then 35 as a starter). His low usage is the problem, not his minutes. L7 31.5 (2) is a small sample.
  - Rest: New Orleans plays Fri 27 at LAC and Sun 29 at POR this week, with no back-to-back, so he should play both. Sun 29 is the first night of 29–30 Nov. He sat Sat 21 at SA, the second night of the last back-to-back, as "injury maintenance" for bilateral patellar tendinopathy ([Yahoo/HoopsHype, 21 Nov](https://sports.yahoo.com/articles/pelicans-rest-trey-murphy-against-182359369.html)). That makes Mon 30 at SAC (next week) a likely sit, but nothing has been announced, so there is no sit row.
  - **Verdict:** ESPN confirmed: active and back in the starting five. Nothing is announced for this week. Mon 30 is the rest risk.

### Neemias Queta (BOS, C, us)

- Rate **31.1** · role rate 34.0 · season 27.2 (16) · L7 34.3 (3) · L15 31.3 (7) · L30 27.4 (14) · projected 27.2
- ESPN: active
- **Minutes:** 29.0 min over his last 3 games against 23.2 for the season (+5.8)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (22 Nov): Queta notched 15 points (5-9 FG, 1-1 3Pt, 4-10 FT), seven rebounds, one assist and two blocks over 30 minutes during Saturday's 97-96 loss to the Kings.
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:**
  - Mitchell Robinson (illness) is **out** again for Tue 24 at WSH, his third straight absence ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)). Rotoworld says "Queta should continue to take on a few extra minutes at center," with Luka Garza backing up ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mitchell-robinson-illness-out-again-vs-wizards)). Queta started and played 30 min in both games without Robinson (21–22 Nov), so expect about 30 on Tuesday. Robinson's expected return: no timetable reported, *ESPN est.* 27 Nov. When Robinson is back, Queta's starts drop back to 23–27 min.
  - Form: L7 34.3 (3) is 7.1 over his 27.2 season average, from the 30-min games while Robinson is out. Rest: Boston has no back-to-back this week. He has rested only once this season (16 Nov), and nothing is announced for Mon 30 (next week).
  - **Verdict:** ESPN confirmed: active and starting. The 30-min role holds for Tue 24 while Robinson is out.

**Summary**
- Duren is out Tue 24 and the re-evaluation result is still unreported, so he is out at least through Sun 29 (row: return 1 Dec, a floor; *ESPN est.* 30 Nov). The expired 24 Nov row should be removed.
- George is not on the Tue 24 report and plays all three BOS games (Tue, Fri, Sun). His "injury" flag is the Sun 22 rest night. Murphy started Mon (35 min, no limit) and has no back-to-back this week. For both of them, Mon 30 is next week's rest risk.
- Mitchell Robinson is out again Tue 24, so Queta starts at about 30 min (role row 30 until 24 Nov). Jalen Smith's 25 min on Monday was illness caution, and he keeps the starting center job.
  - Override proposed: role 30

### Cade Cunningham (DET, PG, us)

- Rate **46.1** · season 48.8 (15) · L7 39.0 (3) · L15 48.7 (7) · L30 50.3 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 24 Nov (Knee, updated 2026-11-23)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (23 Nov): Cunningham (knee) is probable for Tuesday's game against the Orlando.
- News (23 Nov): Cunningham closed Sunday's 107-97 loss to the Hawks with five points (2-9 FG, 1-3 3Pt), four rebounds, 15 assists, one block and one steal in 33 minutes.
- **Research:**
  - Knee: he is Probable for Tue 24 at ORL with right knee soreness ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)), and he is expected to play through it ([NBC Sports/RotoWire, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/cade-cunningham-knee-probable-tuesday-vs-orl)). Detroit has given no diagnosis or imaging. He wore ice on his knees in Atlanta, and a beat outlet calls the label vague ([Detroit Jock City, 23 Nov](https://detroitjockcity.com/cade-cunningham-dud-hawks-raises-injury-concerns-01m84bvt72ng)). His L7 of 39.0 (3 games) is 9.8 under his 48.8 season average. The causes are shooting and foul trouble on 22 Nov (33 min), not minutes. Unchanged since 23 Nov.
  - Rest: DET plays Tue 24 @ORL, Fri 27 vs MIL and Sun 29 vs ORL. The back-to-back's second night is Mon 30 vs DEN, which falls next week. The one night he sat, 18 Nov, was the second night of a road back-to-back and was listed as knee soreness. He played both nights of 27–28 Oct and 8–9 Nov. No source says he will sit 29 or 30 Nov.
  - **Expected return:** Day-to-day, probable Tue 24. No absence reported. *ESPN est.* 24 Nov.
  - **Verdict:** ESPN confirmed. He is probable for Tuesday, and his rest risk this week is low. It falls mainly on Mon 30, next week.

### Anthony Black (ORL, PG/SG, us)

- Rate **36.7** · season 37.8 (13) · L7 36.5 (4) · L15 37.1 (7) · L30 37.8 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Black chipped in 14 points (5-12 FG, 2-4 3Pt, 2-2 FT), five rebounds, two assists and two steals in 35 minutes during Sunday's 116-96 loss to the Wizards.
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- **Research:**
  - Role: Paolo Banchero is Out again for Tue 24 vs DET (right high ankle sprain) ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)). Orlando has started Suggs, Bane, Black, Wagner and Carter in recent games, and a preview projects the same five on Tuesday ([Yahoo Sports preview, 23 Nov](https://sports.yahoo.com/articles/watch-magic-vs-pistons-injury-030723428.html)). Black has averaged 35.5 min over his last five games. His starting role holds while Banchero is out.
  - Banchero: on 19 Nov he was "targeting a return within the next couple of weeks," about 3 Dec (Jason Beede, Orlando Sentinel, via [RotoBaller, 19 Nov](https://www.rotoballer.com/player-news/paolo-banchero-ankle-targeting-return-within-a-couple-of-weeks/1997928)). Sweeney said on 18 Nov there was "no timeline right now" ([Orlando Sentinel via Yahoo, 18 Nov](https://sports.yahoo.com/articles/still-no-timeline-paolo-banchero-192859712.html)). *ESPN est.* 29 Nov looks early.
  - Rest: ORL's back-to-back is Sat 28 @WSH and Sun 29 @DET. He sat 2 Nov, a second night, listed as left ankle injury management ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/)). He played both nights of 10–11 Nov. No source says he will sit 28 or 29 Nov. Unchanged since 23 Nov.
  - **Verdict:** nothing new found. He is healthy and starting until Banchero returns, likely after this week. His rest risk is Sun 29, with no plan announced.

### Myles Turner (MIL, C, us)

- Rate **32.7** · season 28.9 (16) · L7 39.3 (3) · L15 30.0 (7) · L30 28.9 (14) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (24 Nov): Turner closed with 27 points (9-12 FG, 5-6 3Pt, 4-5 FT), 11 rebounds, one assist and two blocks over 28 minutes before fouling out of Monday's 116-111 victory over Toronto.
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- **Research:**
  - Mon 23 at TOR: he started at center and had a season-high 27 pts (9-12 FG, 5-6 3Pt), 11 reb and 2 blk in 28 min before fouling out. MIL won 116-111 ([NBC Sports/RotoWire, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/myles-turner-posts-27-11-1-line-two-blocked-shots); [AP via Washington Post, 23 Nov](https://www.washingtonpost.com/sports/nba/2026/11/23/bucks-raptors-score/84402c10-e7b5-11f1-8db0-6f1e3c389e7c_story.html)). No injury was reported, and his shoulder is off the report. His L7 of 39.3 (3 games) is 10.4 over his 28.9 season average. The cause is shooting, mostly this one 54-FP game, since his minutes (21–28) are unchanged. Three games is a short window.
  - Rest: MIL plays Wed 25 vs BKN, Fri 27 @DET and Sat 28 vs OKC (the second night). On back-to-backs he played both nights of 23–24 Oct, and he sat 11 Nov for "Rest" ([NBA injury report, 11 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_30PM.pdf)). His 19 Nov absence was a left shoulder contusion, not rest ([NBA injury report, 19 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). That makes one rest sit in three, so Sat 28 is a real risk. The Bucks have said nothing about it.
  - **Verdict:** nothing new found. Healthy and starting, with no announced sit, so there is no sit row. The flag's "sat 18–19 Nov" was an injury, not rest.

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:**
  - Out Mon 23 Nov @LAL with the right 2nd plantar plate tear, as was Jaxson Hayes (left knee strain) ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). A 23 Nov preview says he "will be re-evaluated" "in the coming days" ([Yahoo, 23 Nov](https://sports.yahoo.com/articles/jazz-vs-lakers-injury-report-215805379.html)). Otherwise unchanged since 23 Nov: the Jazz said on 20 Nov he had been cleared for on-court work and would be re-evaluated in one week ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). I found no report of contact or 5-on-5 work.
  - **Expected return:** re-evaluation due about 27 Nov. Utah's first game after that is Sun 29 Nov vs PHX, so he misses 27 Nov vs DEN. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date fits the team's one-week re-evaluation. The 28 Nov row stays: UTA has no game on 28 Nov, so it counts the same as 29 Nov.
  - Override proposed: return 2026-11-28

### Norman Powell (CHI, SG/SF, free agent)

- Rate **33.0** · season 30.1 (13) → 32.2 (12) · L7 30.3 (3) · L15 36.2 (5) · L30 31.1 (11) → 33.8 (10) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:**
  - The Bulls' only official word is still from 22 Nov: a "mild right hamstring strain," and he "will be re-evaluated later this week" ([Bulls/NBA.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)). K.C. Johnson said the team hopes for "more definitive timeline later in week" ([K.C. Johnson on X, 22 Nov](https://x.com/KCJHoop/status/2124522701285187925)). He was Out Mon 23 vs CLE, his second straight miss ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). The Bulls had not filed for Wed 25 at CHA, and no re-evaluation result had been reported as of 24 Nov 2:00 AM ET.
  - CHI plays Wed 25 @CHA, then Sat 28 vs IND. He is expected to miss Wed 25 ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/powell-hamstring-to-be-re-evaluated-this-week)). Sat 28 depends on the re-evaluation ([SI Bulls On SI, 22 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-update-bad-news-on-norman-powell-jalen-smith-still-questionable-22)).
  - **Expected return:** re-evaluation "later this week", no date given. Sat 28 vs IND is the earliest possible game. *ESPN est.* 28 Nov.
  - **Verdict:** ESPN confirmed. 28 Nov matches the earliest open game, but it is a floor, not a target. Unchanged since 23 Nov.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:**
  - Out Mon 23 Nov vs SAS with a right patella subluxation ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). On 23 Nov Roundtable said he "remains sidelined despite recent on-court workouts" and the Kings have given no return timeline ([Roundtable, 23 Nov](https://roundtable.io/sports/nba/kings/players/when-will-kings-raynaud-return-from-right-knee-injury)). RotoWire has called him "week-to-week" since 18 Nov ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)).
  - Gap: Sacramento's report for Wed 25 Nov @GS was "not yet submitted" at 2:00 AM ET on 24 Nov ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)). He has usually been ruled out a day ahead, so Tuesday's report will settle it.
  - **Expected return:** no timetable reported. The week-to-week floor is 25 Nov @GS. *ESPN est.* 25 Nov.
  - **Verdict:** ESPN confirmed, but only as a floor. The floor has not passed yet. If SAC lists him out for 25 Nov, move the row to 2026-12-02 (7 days after). SAC plays 29 Nov vs MIN and 30 Nov vs NOP, then 2 Dec @PHX.
  - Override proposed: return 2026-11-25

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.9** · role rate 24.0 · season 30.6 (9) · L7 — · L15 13.7 (3) · L30 25.6 (7) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - Out Mon 23 Nov vs PHX, listed with a left ankle sprain ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). He is sitting until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)) and has not been to the arena since the request ([Bleacher Report, 22 Nov](https://bleacherreport.com/articles/25536410-dejounte-murray-hasnt-been-pelicans-arena-trade-request-latest-nba-rumors-suns-talks)).
  - Suns talks have "zero traction" after a brief conversation, and Phoenix wants draft compensation ([Amick via Yardbarker, 21 Nov](https://www.yardbarker.com/nba/articles/suns_pelicans_discussed_jalen_green_dejounte_murray_swap_but_zero_traction/s1_17038_44599184)). I found no news dated 23–24 Nov. Gap: still only the standoff. Minutes: moot while he does not play.
  - **Expected return:** no timetable reported. He is out until he is traded. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is a placeholder. The 30 Nov row stays: 7 days after the 23 Nov out listing, and NOP is off 24–26 Nov. It rules him out of 27 Nov @LAC and 29 Nov @POR. His first possible game is 30 Nov @SAC.
  - Override proposed: return 2026-11-30

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **13.4** · season 14.2 (5) · L7 — · L15 — · L30 8.3 (3) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 25 Nov)
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:**
  - Out Mon 23 Nov @CHA with a lumbar disc herniation, his 13th straight miss ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). He has been "week-to-week" since 16 Nov with no re-evaluation date ([Grizzlies via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html)). I found no practice report. The "12 weeks" reports in search results are about his October 2025 toe surgery, not this injury.
  - Gap: Memphis's report for Wed 25 Nov vs LAC was "not yet submitted" at 2:00 AM ET on 24 Nov. Otherwise unchanged since 23 Nov.
  - **Expected return:** no timetable reported. The floor is 30 Nov, 7 days after the latest out listing. Memphis's first game after that is Tue 1 Dec @PHI, so he misses 25 Nov vs LAC, 27 Nov @MIN and 29 Nov vs LAL. *ESPN est.* 25 Nov.
  - **Verdict:** ESPN corrected. Nothing supports 25 Nov. The 30 Nov row stays.
  - Override proposed: return 2026-11-30

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.4** · season 8.8 (12) · L7 — · L15 3.7 (3) · L30 8.2 (10) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - Out Mon 23 Nov vs PHX with left plantar fasciitis ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf); [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/bennedict-mathurin-foot-remains-out-monday)). Hoops Rumors gives no timeline ([Hoops Rumors, 22 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-knicks-hawks-mathurin-murray-boyles.html)). "Week-to-week" is RotoWire's own view ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). Otherwise unchanged since 23 Nov.
  - **Expected return:** no timetable reported. The week-to-week floor is 26 Nov, and NOP's first game after it is 27 Nov @LAC. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed as a floor. No source puts him out longer, so I added no row. If NOP lists him out for 27 Nov, the floor becomes 4 Dec.

---
**Summary**
- No availability changes since 23 Nov. All five were Out on Mon 23 Nov, and the existing rows (Nurkic 28 Nov, Raynaud 25 Nov, Murray 30 Nov, Pippen 30 Nov) all stay, with refreshed sources.
- Raynaud's 25 Nov floor depends on Sacramento's report for Wed 25 Nov @GS, which was not yet submitted at 2:00 AM ET. If he is listed out, his row moves to 2 Dec, which takes him out of SAC's 29 and 30 Nov games.
- Murray is still out until he is traded, and Suns talks have "zero traction". Nurkic's re-evaluation is due about 27 Nov, so 29 Nov vs PHX is his earliest game.

### Saddiq Bey (NO, SF/PF, waivers)

- Rate **34.3** · role rate 40.5 · season 29.7 (19) → 31.3 (18) · L7 30.6 (5) → 38.0 (4) · L15 29.9 (10) → 33.1 (9) · L30 30.4 (17) → 32.2 (16) · projected 25.9
- ESPN: active
- **Role:** news on 23 Nov: "Bey is not listed in the starting lineup for Monday's game against the Suns."
- **Minutes:** 39.7 min over his last 3 games against 30.6 for the season (+9.1)
- News (23 Nov): Bey is not listed in the starting lineup for Monday's game against the Suns.
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- **Research:**
  - Role: the move to the bench is ongoing. On Mon 23 vs PHX, Trey Murphy III rejoined the starting five with Jones, Zion, Missi and Fears, and Bey came off the bench: 21 pts (8-18 FG), 4 reb, 3 ast, 2 stl. NBC: "Bey was pushed to the bench with Trey Murphy returning to the starting lineup… his upside is significantly lower as a reserve" ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/saddiq-bey-scores-21-points-off-bench-in-loss); [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)). Only a Murphy absence (bilateral patellar tendinopathy, which the team manages) would put Bey back in the lineup.
  - Minutes: his 40 min Monday include 5 min of overtime (123-119 OT loss), so about 35 in regulation. Murphy played 35 and Jordan Poole 27 off the bench ([Crescent City Sports, 23 Nov](https://crescentcitysports.com/pelicans-fall-short-to-suns-in-overtime/)). The wing minutes stay open while Bennedict Mathurin (left plantar fasciitis; no timetable reported; *ESPN est.* 27 Nov; [NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)) and Dejounte Murray (sitting until he is traded; override floor 30 Nov; *ESPN est.* 27 Nov) are out. Mathurin's return would cut Bey back toward the 22–29 min he played off the bench earlier this season.
  - This week NOP plays Fri 27 @LAC and Sun 29 @POR (no back-to-back). Expect about 30 min off the bench (28–34). His rate is built partly on starts.
  - **Verdict:** ESPN confirmed (active). The bench role is ongoing, but the 30-min estimate rests on one overtime game, so I added no row.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **31.1** · role rate 29.7 · season 26.8 (13) · L7 — · L15 36.0 (3) · L30 27.3 (11) · projected 26.6
- ESPN: out, ESPN est. 25 Nov (Concussion, updated 2026-11-22)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (22 Nov): Allen (concussion) has been ruled out for Monday's game against the Grizzlies.
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- **Research:**
  - Injury: unchanged since 23 Nov. He was out Mon 23 vs MEM (Concussion Protocol), his third straight miss, and no progress or timeline has been reported ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf); [RotoWire, 22 Nov](https://www.rotowire.com/basketball/headlines/grayson-allen-injury-missing-third-straight-game-monday-540534)). He has to pass the protocol's checkpoints symptom-free before he plays ([Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html)). Charlotte had not filed its report for Wed 25 vs CHI as of 2:00 AM ET Tuesday ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)).
  - Role: unchanged since 23 Nov, and the change is not ongoing. He started only while Brandon Miller was out. Miller is back (probable 23 Nov), and Sion James holds the other spot ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-missing-third-straight-game-monday/)). Kon Knueppel's absence keeps Allen's bench minutes up (re-evaluation about 6 Dec; *ESPN est.* 12 Dec). If he is cleared, expect about 25 min off the bench, and 0 if he is not. CHA plays Wed 25 vs CHI and Sat 28 vs BKN.
  - **Expected return:** no timetable reported (concussion protocol). *ESPN est.* 25 Nov, which is just Charlotte's next game.
  - **Verdict:** nothing new found. No source backs ESPN's 25 Nov.

### Pelle Larsson (MIA, SG/SF, free agent)

- Rate **27.0** · role rate 21.9 · season 25.5 (13) · L7 27.5 (2) · L15 27.8 (4) · L30 27.5 (11)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 11 before; 24.5 min in his starts, against 28.5 for the season
- News (23 Nov): Larsson finished Sunday's 123-113 win over Oklahoma City with 21 points (9-14 FG, 3-7 3Pt), three rebounds, five assists and three steals across 30 minutes.
- News (19 Nov): Larsson ended with four points (1-2 FG, 1-2 3Pt, 1-2 FT), two rebounds, two assists and one steal across 15 minutes during Wednesday's 137-130 victory over the Bucks.
- **Research:**
  - Role: unchanged since 23 Nov, and the change is ongoing. He has started every game he has played since Spoelstra moved him into Wiggins's spot on 8 Nov ([Hoops Rumors, 9 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-larsson-wiggins-conwell-hardaway-giannis.html)). On Sun 22 vs OKC he had 21 pts, 5 ast and 3 stl in 30 min ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/pelle-larsson-scores-season-high-21-in-victory)). Miami has not played since, and I found no news of a lineup change.
  - No player's return ends it. Giannis's absence does not drive the start, since Portis took his spot on 22 Nov ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/mia-starts-mitchell-klay-larsson-portis-bam)). Giannis has right groin tendinitis, and Spoelstra is "optimistic" for Wed 25 ([Basketnews, 23 Nov](https://basketnews.com/news-260047-erik-spoelstra-offers-concern-level-on-giannis-new-alarming-injury-for-heat.html)); *ESPN est.* 25 Nov. Only a coaching move back to Wiggins would end Larsson's start. Expect about 28–30 min in Wed 25 @PHI, Fri 27 @NYK and Sun 29 @CLE.
  - **Verdict:** ESPN confirmed (active). His minutes as a starter match his season average, so no row.

### Charles Bassey (GS, C, free agent)

- Rate **26.9** · role rate 34.7 · season 23.3 (15) · L7 31.2 (4) · L15 28.4 (7) · L30 23.3 (15) · projected 14.5
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 23.2 min in his starts, against 15.6 for the season
- **Minutes:** 24.3 min over his last 3 games against 15.6 for the season (+8.7)
- News (23 Nov): Bassey recorded 13 points (6-7 FG, 1-2 FT), nine rebounds, three assists and three steals across 26 minutes during Sunday's 88-87 victory over the Celtics.
- News (20 Nov): Bassey ended with 16 points (6-7 FG, 4-5 FT), 13 rebounds, one assist, two blocks and one steal across 25 minutes during Thursday's 126-98 loss to the Grizzlies.
- **Research:**
  - Role: the change is ongoing. His 18 and 19 Nov starts came with Al Horford (back) out. On Sun 22 vs BOS, Kerr started him at center with Horford healthy, and Horford played 18 min off the bench ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035)). Kerr wants "to give this lineup a look" going forward, with Draymond Green moving to power forward (Anthony Slater, [X, 22 Nov](https://x.com/anthonyVslater/status/2124653675373375495)). "If all goes well, Bassey will remain the Warriors' starting center the rest of the regular season, barring roster changes," though Kerr would not commit long term ([NBC Sports Bay Area, 22 Nov](https://www.nbcsportsbayarea.com/nba/golden-state-warriors/brandin-podziemski-observations-takeaways-celtics/1982338/)). Another writer calls him "the player for the moment" ([Blue Man Hoop, 23 Nov](https://bluemanhoop.com/charles-bassey-starting-role-makes-warriors-trade-plans-even-clearer)).
  - Minutes: he played 22, 25 and 26 in those three starts, against 15.6 for the season. Only a coaching change or a big-man addition would end the role. Kristaps Porzingis (no timetable reported; *ESPN est.* 2 Jan) is the only center whose return would; Moses Moody (*ESPN est.* 1 Dec) and Stephen Curry (update due 26 Nov; *ESPN est.* 12 Dec) play other positions. GS did not play Mon or Tue. Expect about 24 min in Wed 25 vs SAC, Fri 27 @POR and Sun 29 vs LAC.
  - **Verdict:** ESPN confirmed (active). The start is a coach's choice reported as ongoing.
  - Override proposed: role 24

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **37.4** · role rate 23.4 · season 28.2 (15) · L7 58.0 (1) · L15 25.0 (6) · L30 27.8 (13) · projected 26.9
- ESPN: day-to-day, ESPN est. 24 Nov (Illness, updated 2026-11-23)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (23 Nov): Washington (illness) is questionable for Tuesday's game against the Nuggets.
- News (22 Nov): Washington (illness) has been ruled out for Sunday's game against the Jazz.
- **Research:**
  - Injury: new since 23 Nov. He is **questionable** for Tue 24 @DEN (10:00 PM ET) with an illness ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/p-j-washington-illness-questionable-tuesday)). He missed 21 and 22 Nov, and the Mavericks say he "could be" nearing a return ([Mavs.com, 23 Nov](https://nba.com/mavs/news/mavericks-nuggets-preview-as-nba-cup-play-continues-supporting-cast-is-learning-how-to-mesh)). No practice report was found. Zaccharie Risacher starts again if he sits.
  - Minutes flag: unchanged since 21 Nov. The dip to 25 min came from blowouts and foul trouble, not a role change ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/p-j-washington-shoulder-questionable-vs-lac)). He started all 15 games he played, so expect about 28–31 min once he is back. His L7 58.0 rests on 1 game (small sample). DAL plays only Tue 24 @DEN and Fri 27 @PHX this week.
  - **Expected return:** questionable for Tue 24 @DEN; no timetable reported beyond that. *ESPN est.* 24 Nov.
  - **Verdict:** ESPN confirmed. Questionable for 24 Nov matches ESPN's estimate, but he is not cleared yet.

---
**Summary**
- Bassey: Kerr kept him at center over a healthy Horford on 22 Nov, and the start is reported as ongoing. I propose a role row at 24 min through 8 Dec, for Wed 25, Fri 27 and Sun 29.
- Bey: back on the bench behind Murphy, but he played 40 min in an overtime game. Expect about 30 min in NOP's two games (27, 29 Nov) while Mathurin (*ESPN est.* 27 Nov) and Murray are out. No row.
- Washington is questionable for Tue 24 @DEN (*ESPN est.* 24 Nov), and DAL plays only twice this week. Allen is still in concussion protocol with no timetable reported (*ESPN est.* 25 Nov). Larsson's start is unchanged.

### Daniss Jenkins (DET, PG, waivers)

- Rate **32.7** · role rate 36.7 · season 29.7 (16) · L7 32.8 (4) · L15 38.6 (8) · L30 30.9 (14)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 30.4 for the season (+7.2)
- News (23 Nov): Jenkins logged 11 points (4-12 FG, 1-6 3Pt, 2-2 FT), four rebounds, three assists and one steal over 38 minutes during Sunday's 107-97 loss to the Hawks.
- News (21 Nov): Jenkins closed Friday's 105-102 loss to Toronto with 14 points (5-14 FG, 2-4 3Pt, 2-2 FT), four rebounds, one assist and two steals across 39 minutes.
- **Research:**
  - Minutes: DET had no game Mon 23, so nothing has changed since 23 Nov. His last four starts ran 38, 36, 39 and 38 min ([ESPN box score, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). Duren's return, not Robinson's, would end his start (see 23 Nov research).
  - New: Duren (right hamstring; no timetable reported; *ESPN est.* 30 Nov) is **out Tue 24 at ORL** after a re-evaluation set for Sunday that produced no update ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/jalen-duren-hamstring-remains-out-vs-orlando); [NBA injury report, 24 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf)). Robinson (left quad; *ESPN est.* 27 Nov) is also out, and Isaiah Joe is not on the report. Jenkins is a projected starter at ORL ([Roundtable via Yahoo, 24 Nov](https://sports.yahoo.com/articles/watch-magic-vs-pistons-injury-030723428.html)).
  - **Verdict:** ESPN confirmed: active. He keeps the start and about 37 min on Tue 24. DET's next games are Fri 27 and Sun 29, and he keeps the role on either day if Duren is still out.
  - Override proposed: role 37

### Caleb Wilson (CHI, SF, free agent)

- Rate **31.6** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 37.1 (8) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Injury: unchanged since 23 Nov. He was out Mon 23 vs CLE (right metacarpal fracture) ([NBA injury report, 23 Nov 9:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_09_00PM.pdf)). The Bulls set a re-evaluation three weeks after his 12 Nov surgery, about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). He is running and doing strength work but still needs clearance, and he says he has no timeline in mind ([Bulls On SI via Yahoo, 22 Nov](https://sports.yahoo.com/articles/bulls-caleb-wilson-sounds-optimistic-003142636.html)).
  - Minutes flag: the low L3 comes from his 15-min injury exit on 11 Nov. It does not matter while he is out.
  - **Expected return:** four to six weeks from 12 Nov (10 to 24 Dec), re-evaluated about 3 Dec. He will not play this week. *ESPN est.* 13 Dec.
  - **Verdict:** ESPN confirmed. The team's timeline has not changed.

### Jakob Poeltl (TOR, C, free agent)

- Rate **30.5** · role rate 33.8 · season 27.4 (15) · L7 32.5 (4) · L15 31.1 (8) · L30 28.2 (13) · projected 31.7
- ESPN: active
- **Minutes:** 29.7 min over his last 3 games against 24.2 for the season (+5.5)
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- **Research:**
  - Role: he **started Mon 23 vs MIL** at center beside Scottie Barnes and Allen Graves. Murray-Boyles, back from the concussion protocol, came off the bench (24 min) ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-manning-bench-role-in-return/)). Poeltl played 28 min: 15 pts, 10 reb, 3 ast, 1 stl and 1 blk, 41 FP ([ESPN box score, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/jakob-poeltl-posts-double-double-fouls-out-monday)). That makes three straight starts at 29, 32 and 28 min.
  - The report covers Monday only and does not say the bench role continues. Barrett (right hamstring) is re-evaluated about 3 Dec (*ESPN est.* 13 Dec), and the start likely lasts until he returns. TOR plays Fri 27 vs BKN and Sun 29 vs DEN.
  - **Verdict:** ESPN confirmed: active. He is the starting center for now at about 28 to 32 min. I added no row because no source calls the role ongoing.

### Daniel Gafford (DAL, C, free agent)

- Rate **29.5** · role rate 35.4 · season 28.4 (17) · L7 32.7 (3) · L15 26.5 (8) · L30 29.5 (15) · projected 29.3
- ESPN: active
- **Minutes:** 27.7 min over his last 3 games against 22.2 for the season (+5.4)
- News (23 Nov): Gafford notched 10 points (5-8 FG), four rebounds, four assists and two steals over 28 minutes during Sunday's 116-114 win over the Jazz.
- News (15 Nov): Gafford (shoulder) is available for Sunday's game against Boston.
- **Research:**
  - Minutes: the rise matches P.J. Washington's illness. Washington was out for both of the long games, when Gafford played 31 and 28 min (21 and 22 Nov). In earlier games with Washington playing, Gafford logged 16, 19 and 24 min (12, 15 and 18 Nov; his 17 min on 14 Nov ended in a face-injury exit) ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910025); [22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910033); [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910016)). DAL had no game Mon 23.
  - New: Washington is **questionable Tue 24 at DEN** ([NBA injury report, 24 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/p-j-washington-illness-questionable-tuesday)). Lively (right foot surgery; no timetable reported; *ESPN est.* 27 Nov) is out Tue 24, so Gafford keeps the start.
  - **Verdict:** ESPN confirmed: active and starting. Expect about 22 to 24 min once Washington returns, not 28 to 31. That is inferred from the box scores, not stated by any source.

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **28.1** · season 23.5 (16) · L7 30.0 (4) · L15 30.2 (8) · L30 25.1 (14) · projected 23.2
- ESPN: active
- **Minutes:** news on 24 Nov: "Oubre scored at least 15 points for the sixth straight game, continuing to ramp up after a slow start to the season."
- News (24 Nov): Oubre racked up 20 points (8-13 FG, 4-7 3Pt), four rebounds, two assists and two blocks over 28 minutes during Monday's 125-120 win over Oklahoma City.
- News (23 Nov): Oubre recorded 15 points (4-10 FG, 0-4 3Pt, 7-9 FT) and five rebounds in 27 minutes during Sunday's 113-106 loss to the Knicks.
- **Research:**
  - Mon 23 vs OKC: he started and scored a season-high 20 (8-of-13 FG, 4-of-7 3PT) in 28 min, 41 FP ([ESPN box score, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038); [IndyStar via Yahoo, 24 Nov](https://sports.yahoo.com/articles/3-observations-much-needed-pacers-031212215.html)). Aaron Nesmith (right foot soreness, "banged up" per Carlisle) and T.J. McConnell (left hamstring) were out.
  - The flag is a scoring streak, not a minutes change. He has started every game since 11 Nov, mostly beside Nesmith, and played 23 to 34 min, 23 to 28 in his last four ([ESPN box, 11 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909966); [22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)). His start does not depend on Nesmith's absence. IND plays Fri 27 vs PHI and Sat 28 at CHI (a back-to-back), and no rest has been reported.
  - **Verdict:** ESPN confirmed: active. He is a steady starter at about 25 to 28 min. Nothing new on his role.

### Rui Hachimura (LAC, SF/PF, free agent)

- Rate **28.6** · season 25.1 (14) · L7 35.0 (4) · L15 26.5 (8) · L30 25.6 (12) · projected 24.0
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (20 Nov): Hachimura contributed 17 points (7-13 FG, 2-4 3Pt, 1-1 FT), seven rebounds, two assists and one steal in 32 minutes during Thursday's 124-112 loss to the Spurs.
- News (18 Nov): Hachimura finished Tuesday's 132-107 loss to the Jazz with 20 points (7-10 FG, 4-4 3Pt, 2-4 FT), five rebounds, one assist, one block and one steal over 27 minutes.
- **Research:**
  - Rest: the Clippers have no back-to-back this week (Mon 23 @HOU, Wed 25 @MEM, Fri 27 vs NOP, Sun 29 @GSW). The flagged back-to-back is next week, Tue 1 Dec @PHX and Wed 2 Dec vs MIN, and no sit has been announced. His one back-to-back absence, Mon 2 Nov, was an injury, not rest: he was listed Out with left quadriceps soreness ([NBA injury report, 2 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_08_00PM.pdf)). No rest pattern.
  - Role: he still started on Mon 23 Nov in Brandon Ingram's season debut. Max Strus went to the bench ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/lac-starts-garland-ingram-jones-rui-lopez)). He played 29 min for 36 FP. His L7 of 35.0 (4 games) is about 10 over his season 25.1. The reason is steady minutes (27 to 32 in each of the last four) and better shooting (7-10 FG on 17 Nov, 7-13 on 19 Nov).
  - **Verdict:** nothing new found. He has no back-to-back this week, and his only back-to-back absence was the quad injury.

### Rudy Gobert (MIN, C, free agent)

- Rate **27.9** · season 26.7 (17) · L7 27.4 (5) · L15 26.9 (8) · L30 27.6 (15) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (21 Nov): Gobert accumulated seven points (2-2 FG, 3-4 FT), 11 rebounds, two assists, three blocks and one steal over 32 minutes during Saturday's 104-95 victory over the Grizzlies.
- News (20 Nov): Gobert posted nine points (4-6 FG, 1-2 FT), seven rebounds and two steals over 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:**
  - Rest: Minnesota has no back-to-back this week (Mon 23 vs BKN, Wed 25 @OKC, Fri 27 vs MEM, Sun 29 @SAC). The flagged back-to-back is Tue 1 Dec @POR and Wed 2 Dec @LAC, and no sit has been announced. His 31 Oct absence was an injury: he was listed Questionable with low back spasms, then sat ([NBA injury report, 31 Oct 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-31_06_00PM.pdf)). He played both nights of 16–17 Nov (32 and 22 min). No rest pattern.
  - Mon 23 Nov: he started and played 27 min (33 FP) in a 142-116 blowout of Brooklyn, and he was not on the injury report ([Canis Hoopus, 23 Nov](https://www.canishoopus.com/timberwolves-game-previews/72358/game-recap-minnesota-timberwolves-brooklyn-nets-julius-randle); [NBA injury report, 23 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_30PM.pdf)).
  - **Verdict:** nothing new found. The flag's 31 Oct absence was back spasms, not rest, and he played the 16–17 Nov back-to-back.

### Zach Edey (MEM, C, free agent)

- Rate **27.2** · season 24.9 (14) · L7 30.0 (4) · L15 24.7 (6) · L30 23.3 (12) · projected 33.2
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the first night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (20 Nov): Edey (hip) is not listed on the injury report ahead of Saturday's game versus Minnesota.
- News (19 Nov): Edey (hip) has been ruled out for Thursday's game against the Warriors.
- **Research:**
  - Rest: Memphis has no back-to-back this week (Mon 23 @CHA, Wed 25 vs LAC, Fri 27 @MIN, Sun 29 vs LAL). He played Mon 23 Nov, 23 min for 27 FP. The flagged back-to-back is Tue 1 Dec @PHI and Wed 2 Dec @DET.
  - The pattern is real, and it is ankle management. He was listed Out for "left ankle injury management" on 25 Oct, the first night of that back-to-back ([NBA injury report, 25 Oct 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-25_06_00PM.pdf)), and again on 19 Nov, the second night ([NBA injury report, 19 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). He missed both nights of 13–14 Nov with the ankle. Rotoworld called the 19 Nov absence "the second leg of a back-to-back" ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/zach-edey-ankle-off-injury-report-vs-minnesota)). Expect him to miss one night of 1–2 Dec, but no sit has been announced, so there is no row.
  - Minutes are steady at 20–23. His L7 of 30.0 (4 games) is 5.1 over his season 24.9, mostly from the 48-FP game on 16 Nov (23 pts, 10 reb in 21 min). The minutes did not change.
  - **Verdict:** nothing new found for this week. He has sat one night of every back-to-back he was healthy for (ankle management), which matters for 1–2 Dec.

### T.J. McConnell (IND, PG, free agent)

- Rate **20.7** · season 20.0 (7) · L7 20.0 (2) · L15 21.2 (6) · L30 20.0 (7) · projected 24.4
- ESPN: day-to-day, ESPN est. 27 Nov (Left Hamstring, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "The veteran floor general is missing both ends of this back-to-back set, but he'll have some extra time to heal up ahead of Friday's tilt against the 76ers."
- News (23 Nov): McConnell is out for Monday's game against the Thunder due to left hamstring soreness.
- News (21 Nov): McConnell (hamstring) is listed as out for Sunday's game in New York.
- **Research:**
  - Injury: left hamstring soreness, from leaving the game early on 20 Nov at CLE. He was Out on both nights of the 22–23 Nov back-to-back ([NBA injury report, 23 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_30PM.pdf); [Hoops Rumors, 23 Nov](https://hoopsrumors.com/2026/11/pacers-notes-nesmith-mcconnell-smith-shooting-more.html)). RotoWire says he will "have some extra time to heal up ahead of Friday's tilt against the 76ers" ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-wont-play-monday-540663/)). Carlisle has given no timeline. Indiana next plays Fri 27 vs PHI.
  - Unconfirmed: a HotTakes piece quotes an Underdog NBA post saying Carlisle put him out "at least a month" ([HotTakes, 23 Nov](https://hottakes.com/articles/tj-mcconnells-hamstring-injury-leaves-the-pacers-backcourt-in-shambles-9d54ede8-d757-4b9a-808c-c5b4844b7d1b)). I found no team, beat or RotoWire source for it. The piece names the wrong opponent (Mavericks, not Thunder), and its wording matches the Pacers' October 2025 post about his earlier hamstring. Treat it as a risk only.
  - Rest: no sit has been announced for Fri 27–Sat 28 (@CHI). This would be his first back-to-back since returning on 7 Nov. On 21 Nov RotoWire linked his expected absence to that weekend's back-to-back ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-exits-game-with-hamstring-issue/)), so if he returns Friday, Saturday is a real risk. He is not ruled out for that night.
  - **Expected return:** no timetable reported (RotoWire points to Fri 27 Nov vs PHI). *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. Its estimate (Day-to-Day, 27 Nov) matches RotoWire's Friday target. The one-month report is unverified.

### Ja Morant (POR, PG, free agent)

- Rate **31.2** · season 33.8 (4) · L7 — · L15 — · L30 28.0 (2) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:**
  - Gap: still out. Portland listed him Out (left hamstring strain) for Mon 23 Nov at PHI ([NBA injury report, 23 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_30PM.pdf)). Portland's report for Wed 25 vs SAS was not yet submitted at 2:00 AM ET Tue ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)). The 30 Oct plan to re-evaluate him "in four weeks" (about 27 Nov) still stands ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). He is "projected to return later this month or in early December" ([Heavy, 21 Nov](https://heavy.com/sports/nba/portland-trail-blazers/injury-report-vs-knicks-november-21/)). There is nothing from Nori since 7 Nov and no practice report (unchanged since 23 Nov).
  - **Expected return:** re-evaluation about 27 Nov. His first possible game is Sun 29 Nov vs NOP, or Tue 1 Dec vs MIN if he is not cleared. *ESPN est.* 1 Dec. His L30 of 28.0 rests on 2 games (small sample).
  - **Verdict:** ESPN corrected (unchanged since 23 Nov). The re-evaluation rule puts him one game earlier. This row is the same as the one already in the file and should be kept, not added twice.

**Summary**
- No sit is announced for anyone this week. LAC, MIN and MEM play Mon/Wed/Fri/Sun with no back-to-back. The flagged back-to-back is Tue 1–Wed 2 Dec, and of the three only Edey has a real pattern (ankle management, one night of every healthy back-to-back). Hachimura's and Gobert's back-to-back absences were injuries (quad, back spasms).
- McConnell (left hamstring): no timetable reported. RotoWire points to Fri 27 Nov vs PHI (*ESPN est.* 27 Nov). Sat 28 @CHI is a rest risk on a back-to-back, and an unverified "at least a month" report circulated on 23 Nov.
- Morant is still out (re-evaluation about 27 Nov, first possible game Sun 29 Nov; *ESPN est.* 1 Dec). The existing return row (2026-11-28) stands unchanged.
  - Override proposed: return 2026-11-28

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 03 Dec (Left Calf Strain, updated 2026-11-16)
- **Gap:** listed out, and no news in 5 days (ESPN est. 03 Dec)
- News (16 Nov): Harris (calf) is likely to be sidelined until early December, per Jeff Garcia of KENS 5 San Antonio.
- News (10 Nov): Harris (calf) is out for Wednesday's game against Chicago, Jared Weiss of The Athletic reports.
- **Research:**
  - Gap: he is still out. He was listed Out (left calf strain) for Mon 23 Nov at SAC ([NBA injury report, 23 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_30PM.pdf)). The Spurs had not yet filed a report for Wed 25 at POR. I found no practice report and no team date since Haynes's "as early as early December" ([Roundtable, 17 Nov](https://roundtable.io/sports/nba/spurs/news/return-date-expectations-laid-out-for-spurs-tobias-harris)). Heavy says his debut is due next month, "unclear if it will be before or after Christmas" ([Heavy, 21 Nov](https://heavy.com/sports/nba/san-antonio-spurs/injury-report-vs-pelicans-november-21)). Unchanged since 23 Nov.
  - **Expected return:** early December (Haynes). The team has given no date. *ESPN est.* 3 Dec, which falls on SA's Thu 3 Dec game.
  - **Verdict:** ESPN confirmed. 3 Dec is still the earliest reported target. The 7-day rule would give 30 Nov, earlier than any reporting supports, so there is no row.

## Opponents: this week and next

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Injury/gap: he is Out (right high ankle sprain) for Tue 24 Nov vs DET ([NBA injury report, 24 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf)). The latest team word is still Sweeney's "no timeline right now" ([HoopsHype via Yahoo, 18 Nov](https://sports.yahoo.com/articles/still-no-timeline-paolo-banchero-192859712.html)). Banchero said "hopefully within the next couple of weeks" and that he won't rush it ([Hoops Rumors, 19 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-banchero-kawhi-pacers-edwards-grizzlies.html)). Nothing newer turned up. Previews giving "Nov 29" are repeating ESPN's estimate ([Yahoo, 24 Nov](https://sports.yahoo.com/articles/watch-magic-vs-pistons-injury-030723428.html)).
  - The 4-week end of the 24 Oct "4–6 weeks" estimate (about 20 Nov) has passed, and he is still out with no timetable. Under the brief's rule that gives 7 days after the latest out listing, 1 Dec. ORL plays Sat 28 at WAS and Sun 29 at DET, then next on Wed 2 Dec.
  - **Expected return:** no timetable reported. His own target is about early December (around 3 Dec), and the 6-week end of the estimate is 4 Dec. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN corrected. 29 Nov is now optimistic: it would need him to play the second night of a back-to-back with no team date. The 1 Dec row is a floor, so his first game is Wed 2 Dec. That is next week, and it leaves Dr White Slong's next-week outlook unchanged.
  - Override proposed: return 2026-12-01

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.0** · season 39.1 (17) · L7 39.2 (4) · L15 41.2 (8) · L30 39.9 (15) · projected 41.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 23 Nov: "Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "After carrying a questionable tag ahead of both parts of this back-to-back, Siakam is suiting up Monday despite dealing with a left hip injury."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Siakam (hip) will play in Monday's game against the Thunder, Justin Martinez of The Oklahoman reports.
- News (23 Nov): Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management.
- **Research:**
  - Injury: he was questionable Mon 23 Nov vs OKC (left hip injury management), was upgraded to available, and played 35 min (20 pts, 8 reb, 5 ast, 40 FP), hitting the late jumper and three in the 125-120 win ([NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf); [NBA injury report, 23 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_30PM.pdf); [Heavy, 23 Nov](https://heavy.com/sports/nba/indiana-pacers/pascal-siakam-injury-thunder/); [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038)). The postgame write-ups report no setback, and IND has "a few days off" to practice before Fri 27 ([Circle City Spin, 23 Nov](https://www.circlecityspin.com/pacers-get-huge-clutch-win-vs-okc-thunder-six-things-learned/); [IndyStar via Yahoo, 24 Nov](https://sports.yahoo.com/articles/3-observations-much-needed-pacers-031212946.html)).
  - Rest (Fri 27 vs PHI–Sat 28 at CHI, his only games this week): no sit announced. He played both nights of 22–23 Nov with the hip tag, and both nights of 25–26 Oct. His one rest was 2 Nov (unchanged since 23 Nov). The hip "management" label makes Sat 28 a risk, but no source says he will sit.
  - **Expected return:** active (played 22 and 23 Nov). The left hip is day to day; no timetable needed.
  - **Verdict:** ESPN confirmed. Active and playing full minutes, with no announced sit.

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **34.5** · season 39.9 (12) · L7 — · L15 24.5 (2) · L30 40.7 (11) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:**
  - Injury/gap: still Out (left great toe sprain) for Mon 23 Nov at CHI, a 122-108 loss ([NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf); [Hoops Wire, 23 Nov](https://hoopswire.com/cavs-at-bulls-how-to-watch-injury-report-and-a-chance-to-build-momentum)). The team's 16 Nov plan of 7–10 days of rehab and then a re-evaluation (about 23–26 Nov) still holds. No re-evaluation result, practice report or Atkinson update has appeared since ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)). CLE's report for Wed 25 at NYK was "not yet submitted" ([NBA injury report, 24 Nov 2:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)).
  - The Akron Beacon Journal expects the Cavs to stay conservative: "it's probably more likely Mobley will be out until after Thanksgiving," i.e. Sun 29 vs MIA ([Akron Beacon Journal via Yahoo, 16 Nov](https://sports.yahoo.com/articles/cleveland-cavaliers-announce-evan-mobley-230948119.html)). CLE plays only Wed 25 at NYK and Sun 29 vs MIA this week.
  - **Expected return:** re-evaluation about 23–26 Nov, with no result reported. Sun 29 vs MIA is the likely first game, and Wed 25 at NYK only if he is cleared early. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. Nothing new since 23 Nov. The day after the latest re-evaluation date (27 Nov) lands on CLE's next game, 29 Nov, so no row is needed.

### Naz Reid (CHA, PF/C, Matt Wright's Foxies)

- Rate **35.2** · role rate 39.4 · season 31.5 (16) → 32.6 (15) · L7 38.3 (3) · L15 35.8 (6) · L30 31.2 (14) → 32.5 (13) · projected 35.5
- ESPN: active
- **Minutes:** 39.7 min over his last 3 games against 32.8 for the season (+6.9)
- News (20 Nov): Reid logged 12 points (4-19 FG, 2-10 3Pt, 2-4 FT), 10 rebounds, three assists and one block over 39 minutes during the Hornets' 111-97 loss to the Hawks on Friday.
- News (18 Nov): Reid ended Tuesday's 118-114 overtime loss to the Lakers with 23 points (8-18 FG, 4-10 3Pt, 3-4 FT), 11 rebounds, four assists, two blocks and two steals across 41 minutes.
- **Research:**
  - Minutes: 42 (17 Nov, an overtime game), 39 (20 Nov) and 38 (23 Nov vs MEM: 24 pts on 8-25 FG, 6 reb, 36 FP) ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/naz-reid-scores-24-hornets-lose-fifth-straight)). The rise lines up with forward/wing absences: Grayson Allen (concussion, out since a late scratch 17 Nov; no timetable reported, *ESPN est.* 25 Nov) and Grant Williams (right hamstring management, out 20 and 23 Nov; no timetable reported, *ESPN est.* 25 Nov) ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-missing-third-straight-game-monday/); [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grant-williams-wont-play-against-atlanta/); [Roundtable via Yahoo, 23 Nov](https://sports.yahoo.com/articles/hornets-host-grizzlies-without-grayson-141629315.html)).
  - L7 38.3 (3) is 6.8 above his 31.5 season average, and the reason is the extra minutes. His shooting is poor (below 40% in six of seven games). No source gives him an expected minutes figure, and both absent teammates are day to day (ESPN est. 25 Nov), so the extra minutes may end Wed 25. CHA plays Wed 25 vs CHI and Sat 28 vs BKN; their Wed report was not yet submitted.
  - **Verdict:** nothing new found to support a row. The minutes are real but tied to short absences that may end this week, and no source reports the role as ongoing.

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **47.7** · season 39.4 (14) · L7 58.3 (3) · L15 45.0 (6) · L30 39.5 (12) · projected 45.4
- ESPN: day-to-day, ESPN est. 25 Nov (Illness, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov, Tue 01–Wed 02 Dec; sat the second night of the 24–25 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side; sat the first night of the 15–16 Nov back-to-back, playing the games either side
- News (23 Nov): Embiid (illness) is out for Monday's game against Portland, Austin Krell of OnPattison.com reports.
- News (23 Nov): Embiid (knee) has been downgraded to questionable for Monday's game against Portland.
- **Research:**
  - New since 23 Nov: he was a late scratch Mon 23 Nov vs POR with an illness after missing shootaround ([Inquirer, 23 Nov](https://www.inquirer.com/sixers/joel-embiid-game-status-trail-blazers-20261123.html)). He is day-to-day, and no details of the illness were given. The PHI report for Wed 25 vs MIA had not been filed as of 1:30 AM ET 24 Nov ([NBA injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf)).
  - Rest: the team has said nothing about Fri 27 at IND / Sat 28 at HOU or Tue 1 / Wed 2 Dec. He has sat one leg of all three back-to-backs this season (24–25 Oct, 30–31 Oct, 15–16 Nov). Before the first, he said "I'm not playing both games. I'm playing in 1 of them" ([Yahoo/NBC Sports Philadelphia, 24 Oct](https://sports.yahoo.com/articles/76ers-joel-embiid-makes-major-152111769.html)).
  - **Expected return:** day-to-day (illness), no timetable reported. *ESPN est.* 25 Nov.
  - **Verdict:** nothing new on the back-to-backs. Expect him to sit one night of each, but there is no team statement, so there is no sit row. The illness adds risk for Wed 25.

### Amen Thompson (HOU, SG/SF, Matt Wright's Foxies)

- Rate **38.0** · season 37.1 (17) · L7 37.3 (3) · L15 39.9 (7) · L30 35.1 (15) · projected 40.0
- ESPN: active
- **Rest:** back-to-back Mon 30–Tue 01 Dec; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (21 Nov): Thompson chipped in 22 points (10-12 FG, 0-1 3Pt, 2-6 FT), six rebounds and one steal in 26 minutes during Friday's 133-124 loss to the Nuggets.
- News (18 Nov): Thompson recorded 15 points (6-11 FG, 0-1 3Pt, 3-4 FT), nine rebounds, three assists, one steal and one block over 31 minutes during the Rockets' 119-104 win over the Pacers on Wednesday.
- **Research:**
  - He played 28 min Mon 23 Nov vs LAC (20 pts, 4 reb, 5 ast, 46 FP) with no injury listing ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910043)). HOU plays Wed 25 vs PHX and Sat 28 vs PHI this week, with no back-to-back. The flagged Mon 30–Tue 1 Dec back-to-back is next week.
  - Rest: his 16 Nov absence (second night) was left knee soreness, not rest ([ClutchPoints, 16 Nov](https://clutchpoints.com/nba/houston-rockets/rockets-news-amen-thompson-out-heat-game-concerning-injury-update)), and he returned with no minutes limit on 18 Nov. He played both nights of HOU's 23–24 Oct and 30–31 Oct back-to-backs (box scores). No pattern, and nothing has been said about 30 Nov–1 Dec.
  - **Verdict:** ESPN confirmed. Healthy, with no rest pattern and no rest risk in this matchup week.

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **29.6** · season 31.8 (14) · L7 26.7 (3) · L15 29.5 (6) · L30 31.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Nembhard produced 16 points (5-13 FG, 2-3 3Pt, 4-7 FT), two rebounds and eight assists in 32 minutes during Sunday's 113-106 loss to the Knicks.
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- **Research:**
  - He played both nights of the 22–23 Nov back-to-back: 32 min at NYK, then 38 min vs OKC (15 pts, 6 ast, 33 FP), and he set up Siakam's late three and Zubac's sealing dunk ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038); [Yardbarker, 23 Nov](https://yardbarker.com/nba/articles/pacers_beat_thunder_125_120_as_siakam_scores_20/s1_17668_44609493)). He was not on Monday's injury report. McConnell (left hamstring soreness; no timetable reported, *ESPN est.* 27 Nov) and Haliburton (left hamstring strain; "at least the next couple of weeks" per Charania, *ESPN est.* 13 Dec) stayed out, so he remains the lead guard ([NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf); [Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/pacers-receive-another-disappointing-injury-021425801.html)).
  - Rest (Fri 27–Sat 28): no sit announced. Unchanged since 23 Nov: both earlier second-night absences (26 Oct back, 2 Nov cervical) were filed as injuries. Playing 38 min on Monday's second night argues against a set rest pattern. L7 26.7 (3) is 5.1 under his season average because of his short 26-min return from the hip on 20 Nov and 6 turnovers on 22 Nov.
  - **Verdict:** nothing new found. He is healthy, and neither night of Fri 27–Sat 28 has an announced sit.

Summary:
- No availability changes this week: Siakam (hip) and Nembhard played both nights of 22–23 Nov, and neither has a sit announced for Fri 27–Sat 28. Thompson has no back-to-back until 30 Nov–1 Dec, which is next week.
- Mobley (left toe sprain): still no re-evaluation result. Sun 29 vs MIA is the likely first game (re-evaluation about 23–26 Nov; *ESPN est.* 29 Nov). Wed 25 at NYK only if he is cleared early.
- Reid's extra minutes (39–42) follow the absences of Grayson Allen and Grant Williams, both ESPN est. 25 Nov, so no role row.

### Derrick White (BOS, PG/SG, Dr White Slong)

- Rate **27.7** · season 29.9 (16) · L7 22.0 (3) · L15 29.6 (7) · L30 29.4 (14) · projected 37.0
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 21 Nov: "The veteran guard will be in street clothes for the first leg of the Celtics' back-to-back set, but he could make his return Sunday against the Warriors."; sat the first night of the 21–22 Nov back-to-back, playing the games either side
- News (23 Nov): White amassed 14 points (6-21 FG, 2-12 3Pt), three rebounds, five assists and one steal over 32 minutes during Sunday's 88-87 loss to the Warriors.
- News (22 Nov): White (shoulder) is not listed on the injury report for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:**
  - He is not on Boston's report for Tue 24 Nov at WAS ([NBA injury report, 24 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf)). He has played since returning on 22 Nov from the one-game left AC joint sprain ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/derrick-white-shoulder-off-injury-report-vs-gsw)).
  - Rest: the 21 Nov absence was the shoulder, not rest. He played both nights of BOS's other four back-to-backs (26–27 Oct, 1–2 Nov, 10–11 Nov, 15–16 Nov, from box scores). No sit has been reported for Sun 29 / Mon 30 Nov.
  - **Verdict:** nothing new found. His rest risk for 29–30 Nov is low.

### Jonathan Kuminga (MIN, SF/PF, Dr White Slong)

- Rate **26.8** · season 28.7 (17) · L7 28.8 (4) · L15 23.4 (7) · L30 27.8 (15) · projected 26.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 16–17 Nov back-to-back, playing the games either side
- News (19 Nov): Kuminga totaled 23 points (7-13 FG, 2-4 3Pt, 7-7 FT), three rebounds, three assists and three blocks in 35 minutes during Thursday's 102-99 loss to the Knicks.
- News (19 Nov): Kuminga (shoulder) is available for Thursday's game against New York.
- **Research:**
  - He played Mon 23 Nov: 15 pts in 26 min of a 142-116 rout of BKN, so the blowout explains the low minutes ([Star Tribune, 23 Nov](https://www.startribune.com/minnesota-timberwolves-brooklyn-nets-score-today-lamelo-ball-julius-randle-anthony-edwards-injury/601916745)).
  - Rest: his 17 Nov miss was a right shoulder contusion, not rest ([Roundtable, 17 Nov](https://roundtable.io/sports/nba/timberwolves/news/key-starter-ruled-out-for-timberwolves-against-blazers)). He played both nights of MIN's 25–26 Oct and 30–31 Oct back-to-backs (box scores). Nothing has been said about Tue 1 / Wed 2 Dec.
  - **Verdict:** nothing new found. His rest risk for 1–2 Dec is low.

**Summary**
- Banchero: still out Tue 24 Nov with no team timeline. ESPN's 29 Nov is corrected to a 1 Dec floor, so his first game is Wed 2 Dec.
- Embiid: out Mon 23 Nov with an illness and day-to-day for Wed 25. He has sat one leg of all 3 back-to-backs, so expect one sit on 27–28 Nov and 1–2 Dec. There is no team statement, so there is no row.
- White and Kuminga: low rest risk (their only back-to-back misses were injuries). Harris: unchanged, earliest target early December (*ESPN est.* 3 Dec).

## Other rosters: injury flags only

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **59.3** · season 53.0 (16) → 54.5 (15) · L7 65.3 (3) · L15 60.0 (7) · L30 54.3 (14) → 56.2 (13) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 22 Nov: "Towns (illness) is questionable to play in Sunday's game against the Pacers."
- News (22 Nov): Towns posted 30 points (9-14 FG, 4-4 3Pt, 8-12 FT), 13 rebounds, five assists, three steals and two blocks in 29 minutes during Sunday's 113-106 win over the Pacers.
- News (22 Nov): Towns (illness) is available to play in Sunday's game against Indiana, Jared Schwartz of the New York Post reports.
- **Research:**
  - The flag is the 21–22 Nov illness, not a new injury. He missed only Sat 21 vs POR, his first absence of the season. He was listed available for Sun 22 vs IND ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)) and played 29 min: 30 pts and 13 reb, 82 FP ([AP via La Nación, 23 Nov](https://www.lanacion.com.ar/usa/karl-anthony-towns-has-30-points-and-13-rebounds-as-knicks-beat-pacers-113-106-nid23112026/)).
  - The Knicks were off Mon 23 and Tue 24. Their report for Wed 25 vs CLE had not been filed by 24 Nov 2:00 AM ET ([NBA injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf)). No relapse, restriction or new ailment has been reported. Unchanged since 23 Nov.
  - **Expected return:** already back (played 22 Nov). He is not in ESPN's injury feed, so there is no *ESPN est.*
  - **Verdict:** ESPN confirmed. It was a one-game illness, and he is back at full workload.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-24 07:07 UTC.
