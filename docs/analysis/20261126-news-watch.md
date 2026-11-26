# News watch: 26 Nov 2026

- Generated 2026-11-26 06:13 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Matt Wright's Foxies, Dr White Slong). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 41 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Aday Mara | role | 27 | 2026-12-05 | [link](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) | in force |
| Scotty Pippen Jr. | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) | in force |
| Jusuf Nurkic | return | 2026-11-28 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) | in force |
| Maxime Raynaud | return | 2026-12-02 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf) | in force |
| Dejounte Murray | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf) | in force |
| Charles Bassey | role | 24 | 2026-12-08 | [link](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html) | in force |
| Buddy Hield | role | 30 | 2026-11-27 | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_03_30AM.pdf) | in force |
| Daniss Jenkins | role | 37 | 2026-11-27 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/daniss-jenkins-dishes-out-10-assists-vs-orlando) | in force |
| Paolo Banchero | return | 2026-12-01 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_05_30PM.pdf) | in force |
| Ja Morant | return | 2026-11-28 | — | [link](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury | 44.1 † | — | out, ESPN est. 30 Nov |
| **Kawhi Leonard** | TOR | us | injury | 43.3 † | — | out, ESPN est. 03 Dec |
| **Cade Cunningham** | DET | us | rest | 46.7 | — | day-to-day, ESPN est. 27 Nov |
| **Paul George** | BOS | us | rest | 42.1 | — | active |
| **Neemias Queta** | BOS | us | rest | 33.3 | — | active |
| **Trey Murphy III** | NO | us | rest | 32.3 | — | active |
| **Myles Turner** | MIL | us | rest | 32.1 | — | active |
| **Anthony Black** | ORL | us | rest | 30.9 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury, gap | 36.7 | — | out, ESPN est. 29 Nov |
| **Norman Powell** | CHI | free agent | injury | 32.2 | — | out, ESPN est. 28 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 02 Dec |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 21.5 | 24.0 | out, ESPN est. 27 Nov |
| **Bennedict Mathurin** | NO | free agent | injury, gap | 5.3 | — | out, ESPN est. 27 Nov |
| **Saddiq Bey** | NO | free agent | role, minutes | 34.2 | 40.6 | active |
| **Charles Bassey** | GS | free agent | role, minutes | 27.8 | 33.5 | active |
| **Kenrich Williams** | OKC | free agent | role | 27.4 | — | active |
| **Grayson Allen** | CHA | free agent | role | 27.4 | 29.7 | out, ESPN est. 28 Nov |
| **P.J. Washington** | DAL | free agent | minutes | 34.0 | 23.6 | active |
| **De'Andre Hunter** | SAC | free agent | minutes | 32.2 | 30.1 | active |
| **Jakob Poeltl** | TOR | free agent | minutes | 32.2 | 33.6 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 30.9 | 26.1 | out, ESPN est. 13 Dec |
| **Daniss Jenkins** | DET | free agent | minutes | 30.4 | 36.7 | active |
| **Daniel Gafford** | DAL | free agent | minutes | 29.7 | 36.7 | active |
| **Kelly Oubre Jr.** | IND | free agent | minutes | 28.6 | — | active |
| **Rui Hachimura** | LAC | free agent | rest | 29.4 | — | active |
| **Rudy Gobert** | MIN | free agent | rest | 27.7 | — | active |
| **Zach Edey** | MEM | free agent | rest | 25.7 | — | day-to-day, ESPN est. 27 Nov |
| **T.J. McConnell** | IND | free agent | rest | 21.6 | — | day-to-day, ESPN est. 27 Nov |
| **Julian Reese** | NO | free agent | rest | 8.0 | — | day-to-day, ESPN est. 25 Nov |
| **Ja Morant** | POR | free agent | gap | 31.2 | — | out, ESPN est. 01 Dec |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 03 Dec |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 56.8 † | — | out, ESPN est. 29 Nov |
| **Evan Mobley** | CLE | Matt Wright's Foxies | injury, gap | 34.4 | — | out, ESPN est. 29 Nov |
| **Josh Hart** | NY | Dr White Slong | minutes | 29.5 | 32.5 | active |
| **Joel Embiid** | PHI | Dr White Slong | rest | 47.5 | — | day-to-day, ESPN est. 27 Nov |
| **Amen Thompson** | HOU | Matt Wright's Foxies | rest | 39.3 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 39.0 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 29.1 | — | active |
| **Derrick White** | BOS | Dr White Slong | rest | 28.1 | — | active |
| **Jonathan Kuminga** | MIN | Dr White Slong | rest | 26.3 | — | active |
| **Jalen Brunson** | NY | Melbourne poopoo | injury | 39.9 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 — · projected 42.2
- ESPN: out, ESPN est. 30 Nov (Right Hamstring Strain, updated 2026-11-24)
- **Injury:** ESPN est. 30 Nov (Out, Right Hamstring Strain, updated 24 Nov), but the news said on 23 Nov: "Duren hasn't played since Oct. 23 due to a right hamstring strain, though he's expected to be re-evaluated soon."
- News (24 Nov): Duren (hamstring) is being assigned to the Motor City Cruise on Wednesday for practice as he ramps up for a potential return, Eric Vincent of ClutchPoints.com reports.
- News (23 Nov): Duren (hamstring) has been ruled out for Tuesday's game against the Magic.
- **Research:**
  - He practised with the Pistons on Tue 24, then went to the Motor City Cruise on Wed 25 for practice as part of his return to play ([AP via NBA.com, 25 Nov](https://www.nba.com/news/jalen-duren-hamstring-practices-with-pistons-ahead-of-rehab-stint)). On Wed 25 he was "practicing with the Cruise" and "appears close to returning". Bickerstaff: "We're looking forward to getting him back" ([Hoops Rumors citing the Free Press, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)). The Free Press calls the step "a significant injury milestone" but gives no target game ([Free Press via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/cade-cunningham-injury-dulls-hope-101021863.html)). The Pistons have still not set a date, and Siegel's "imminent" is the latest word ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/detroit-pistons/pistons-news-jalen-duren-g-league-move)).
  - Nothing reported since Wed 25's practice. At 1:00 AM ET Thu 26, Detroit's report for Fri 27 vs MIL was "not yet submitted" ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)). No source names Fri 27 or Sun 29 vs ORL. Sun 29 is the likelier of the two because Fri 27 comes after only one G League practice and the Thanksgiving day off. ESPN's 30 Nov points to Mon 30 vs DEN, which is next week. His rate of 44.1 rests on 1 game after his 10-min injury exit was dropped (small sample). He has no L7, L15 or L30 games because he has not played since 23 Oct.
  - **Expected return:** no timetable reported. Return "imminent". Sun 29 is possible, Fri 27 less likely, and neither is confirmed. *ESPN est.* 30 Nov.
  - **Verdict:** ESPN confirmed as the latest date a source supports, though it may be one game late (Sun 29). Unchanged since 25 Nov apart from the Cruise practice taking place. Check DET's Thu 26 report (for Fri) and Sat 28 report (for Sun).

### Kawhi Leonard (TOR, SF/PF, us)

- Rate **43.3** (small sample) · season 40.0 (2) · L7 — · L15 — · L30 — · projected 45.8
- ESPN: out, ESPN est. 03 Dec (Left Knee Inflammation, updated 2026-11-24)
- **Injury:** ESPN est. 03 Dec (Out, Left Knee Inflammation, updated 24 Nov), but the news said on 24 Nov: "Leonard has begun individual on-court workouts following treatment to address swelling in his left knee, and he will be re-evaluated in one week, Marc J."
- News (24 Nov): Leonard has begun individual on-court workouts following treatment to address swelling in his left knee, and he will be re-evaluated in one week, Marc J. Spears of ESPN.com reports.
- News (20 Nov): Leonard (knee) could return in the next few weeks, per Shams Charania of ESPN.
- **Research:**
  - Unchanged since 24 Nov. He has begun individual on-court workouts after treatment for left knee swelling. The Raptors say he is out "at least another week" and will give the next update in a week, about Tue 1 Dec ([CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/); [NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week)). Nothing new on 25 or 26 Nov. He has done no contact work or team practice yet.
  - He is out for Fri 27 vs BKN and Sun 29 vs DEN. Going by the re-evaluation date (about 1 Dec, so a first possible date of 2 Dec), his first possible game is Thu 3 Dec at SA, the same as ESPN's date. Tue 1 Dec at HOU would need a same-day clearance. Season 40.0 (2) and rate 43.3 are small samples (2 games, the last on 23 Oct).
  - **Expected return:** out at least until the next update, about 1 Dec ([CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/)). *ESPN est.* 3 Dec.
  - **Verdict:** ESPN confirmed. Following the re-evaluation rule gives the same first game (3 Dec at SA), so no row is needed.

### Cade Cunningham (DET, PG, us)

- Rate **46.7** · season 48.8 (15) · L7 36.5 (2) · L15 54.6 (5) · L30 49.8 (12) · projected 50.4
- ESPN: day-to-day, ESPN est. 27 Nov (Knee, updated 2026-11-25)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 17–18 Nov back-to-back, playing the games either side
- News (24 Nov): Cunningham (knee) is listed as out for Tuesday's game against Orlando.
- News (23 Nov): Cunningham (knee) is probable for Tuesday's game against the Orlando.
- **Research:**
  - He was a late scratch at ORL on Tue 24 with right knee soreness, his second miss in about a week (the first was 18 Nov at NOP). Bickerstaff: "He's battling through a lot, and I'll leave it at that." The Free Press says more missed time is possible ([Free Press via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/cade-cunningham-injury-dulls-hope-101021863.html)). He is day-to-day, and Fri 27 vs MIL is his next chance to play ([BasketballNews, 25 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-hes-fighting-through-a-lot-all-star-candidate-cade-cunninghams-injury-update-sparks-concern/)). No report says he practised on Wed 25. Thu 26 is Thanksgiving. Detroit's Fri 27 report was "not yet submitted" at 1:00 AM ET Thu 26 ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)).
  - Rest: Detroit's back-to-back is Sun 29 vs ORL, then Mon 30 vs DEN. Sun 29 is the first night, so no rest risk falls in our week. Mon 30 (next week) carries the risk: his only second-night miss (18 Nov) was listed as knee soreness, not rest. Nothing has been announced, so there is no sit row.
  - Form: L7 36.5 (2) is a small sample and sits 12.3 under his 48.8 (15) season average. The cause is the knee soreness plus a 5-point, 15-assist game on 22 Nov in early foul trouble. L15 54.6 (5), L30 49.8 (12), rate 46.7.
  - **Expected return:** no timetable reported; day-to-day, Fri 27 vs MIL his next chance. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed (day-to-day, est. 27 Nov), with a real risk of another miss on Fri 27. Nothing new since 25 Nov. Check DET's Thu 26 afternoon report.

### Paul George (BOS, SF/PF, us)

- Rate **42.1** · season 41.9 (15) · L7 44.0 (3) · L15 42.7 (6) · L30 40.3 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports."; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 21–22 Nov back-to-back, playing the games either side
- News (25 Nov): George closed Tuesday's 131-116 victory over the Wizards with 28 points (11-20 FG, 6-9 3Pt), four rebounds, nine assists and one steal in 33 minutes.
- News (23 Nov): George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports.
- **Research:**
  - Unchanged since 25 Nov. He is healthy after 60 FP at WSH on Tue 24 (28 pts, 6-9 3Pt, 9 ast, 33 min) ([Yahoo Sports player ratings, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-player-ratings-tatum-drops-051608071.html)). Mitchell Robinson was the only Celtic listed going into Friday ([Sports Mole, 25 Nov](https://www.sportsmole.co.uk/basketball/boston-celtics/preview/atlanta-hawks-vs-boston-celtics-player-props-injury-report-and-prediction--nba-cup_609820.html)). Boston's Fri 27 report was not yet submitted at 1:00 AM ET Thu 26.
  - Rest: Boston plays Fri 27 vs ATL (NBA Cup), Sun 29 at SA and Mon 30 at DAL. Sun 29 is the first night of the back-to-back, so he should play both games this week. He sat the second night of 3 back-to-backs (2 Nov rest, 11 Nov illness, 22 Nov rest), which makes **Mon 30 at DAL** (next week) a strong pattern risk. Nothing has been announced, so there is no sit row.
  - Form: L7 44.0 (3), L15 42.7 (6), L30 40.3 (13), season 41.9 (15), rate 42.1. None is 5+ off.
  - **Verdict:** ESPN confirmed: active, plays Fri 27 and Sun 29.

### Neemias Queta (BOS, C, us)

- Rate **33.3** · season 28.5 (17) · L7 37.8 (4) · L15 33.4 (7) · L30 28.7 (15) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (25 Nov): Queta ended Tuesday's 131-116 victory over Washington with 21 points (9-11 FG, 3-3 FT), five rebounds, two assists, two blocks and one steal across 25 minutes.
- News (22 Nov): Queta notched 15 points (5-9 FG, 1-1 3Pt, 4-10 FT), seven rebounds, one assist and two blocks over 30 minutes during Saturday's 97-96 loss to the Kings.
- **Research:**
  - Mitchell Robinson has **not** returned. He was out with an illness on Tue 24 at WSH, his third straight miss ([NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf)). Since then: "no update", status for Friday unconfirmed, and he is still the only Celtic listed ([Sports Mole, 25 Nov](https://www.sportsmole.co.uk/basketball/boston-celtics/preview/atlanta-hawks-vs-boston-celtics-player-props-injury-report-and-prediction--nba-cup_609820.html)). Boston's Fri 27 vs ATL report was not yet submitted at 1:00 AM ET Thu 26 ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)). Expected return for **Mitchell Robinson**: no timetable reported, *ESPN est.* 27 Nov.
  - Role: Queta has started every November game. Without Robinson he played 30, 30 and 25 min, the 25 coming in a blowout in which he scored 48 FP on 21 pts (9-11 FG) ([Yahoo Sports player ratings, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-player-ratings-tatum-drops-051608071.html)). With Robinson he played 23–27. Rest: Sun 29 at SA is the first night, and Mon 30 at DAL (next week) is the second. His only rest night was the second night of a back-to-back on 16 Nov. Nothing has been announced.
  - Form: L7 37.8 (4) is 9.3 over his 28.5 (17) season average, from the extra minutes with Robinson out and Tuesday's shooting. L15 33.4 (7), L30 28.7 (15), rate 33.3.
  - **Verdict:** ESPN confirmed: active starter for Fri 27 and Sun 29. There is no role row because no source gives Robinson's Friday status. Check BOS's Thu 26 report.

### Trey Murphy III (NO, SG/SF, us)

- Rate **32.3** · season 31.1 (11) · L7 31.5 (2) · L15 31.5 (2) · L30 32.2 (8) · projected 36.8
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "Murphy was deployed off the bench Friday against the Thunder in his first action since Nov. 8 but was then held out Saturday in San Antonio for the second half of a back-to-back in an effort to ease him back into action following a six-game absence due to bilateral patellar tendinopathy."; sat the second night of the 20–21 Nov back-to-back, playing the games either side
- News (24 Nov): Murphy totaled nine points (4-14 FG, 1-6 3Pt), nine rebounds, two assists and two steals across 35 minutes during Monday's 123-119 overtime loss to the Suns.
- News (23 Nov): Murphy is starting Monday's game against Phoenix.
- **Research:** _pending_

### Myles Turner (MIL, C, us)

- Rate **32.1** · season 28.6 (17) · L7 35.8 (4) · L15 31.1 (7) · L30 30.6 (14) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (24 Nov): Turner closed with 27 points (9-12 FG, 5-6 3Pt, 4-5 FT), 11 rebounds, one assist and two blocks over 28 minutes before fouling out of Monday's 116-111 victory over Toronto.
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- **Research:** _pending_

### Anthony Black (ORL, PG/SG, us)

- Rate **30.9** · season 35.3 (14) · L7 25.5 (4) · L15 32.9 (8) · L30 34.6 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (25 Nov): Black finished with five points (2-8 FG, 0-2 3Pt, 1-3 FT), four rebounds, two assists and one block over 28 minutes during Tuesday's 104-86 loss to the Pistons.
- News (23 Nov): Black chipped in 14 points (5-12 FG, 2-4 3Pt, 2-2 FT), five rebounds, two assists and two steals in 35 minutes during Sunday's 116-96 loss to the Wizards.
- **Research:** _pending_

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:**
  - Unchanged since 25 Nov. The Jazz's latest word is still from 20 Nov: cleared for on-court work and "will be re-evaluated in one week" ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). His last listing was Out on 23 Nov at LAL ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). Through 26 Nov I found no report of contact or 5-on-5 work. UTA had not yet filed its report for Fri 27 vs DEN ([NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)).
  - Gap: Statz says the Jazz report has him back 29 Nov, but that looks like a copy of ESPN's estimate, so I did not use it ([Statz, 23 Nov](https://statz.ai/nba/news/jusuf-nurkic-injury-update)). The re-evaluation is due about 27 Nov, and it is a check-up, not a return date.
  - **Expected return:** the re-evaluation is due about 27 Nov, so he should miss Fri 27 vs DEN. His first possible game is Sun 29 vs PHX, but he still has to clear full-contact work. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. 29 Nov fits the one-week re-evaluation. The 28 Nov row has the same effect, because UTA has no game on 28 Nov.
  - Override proposed: return 2026-11-28

### Norman Powell (CHI, SG/SF, free agent)

- Rate **32.2** · season 30.1 (13) → 32.2 (12) · L7 28.0 (2) · L15 36.2 (5) · L30 30.7 (10) → 33.7 (9) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:**
  - No re-evaluation result had been reported by 26 Nov, about 1:30 AM ET. He was inactive Wed 25 at CHA, his third straight miss, and the Bulls won 107-105 without him ([Roundtable, 26 Nov](https://roundtable.io/sports/nba/bulls/game-day/bulls-close-out-nba-cup-slate-with-road-win-against-charlotte-hornets); [NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). The only team word is still the 22 Nov "mild" strain, "re-evaluated later this week" ([Bulls/NBA.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)). Hoops Rumors expected him to miss DEN, CLE and CHA before a recheck, which makes Sat 28 vs IND the first game after it ([Hoops Rumors, 22 Nov](https://www.hoopsrumors.com/2026/11/bulls-norman-powell-suffers-mild-right-hamstring-strain.html)).
  - Sat 28 vs IND: no source says he will play. CHI does not play Fri, and its first report for Sat 28 should come Fri 27 afternoon ET. For comparison, his March 2025 right hamstring strain cost him 7 games over 14 days ([Hoops Rumors, 16 Mar 2025](https://www.hoopsrumors.com/2025/03/clippers-norman-powell-returning-from-hamstring-injury.html)). The add deadline for Sat 28 is that day's first tip-off, ORL@WSH at 5:00 PM ET (9:00 AM Sun 29 Melbourne). That is 2 hours before CHI tips off, so a game-time decision would come after the deadline.
  - **Expected return:** to be re-evaluated "later this week", with no date given. Sat 28 vs IND is the earliest possible game, not a reported target. *ESPN est.* 28 Nov.
  - **Verdict:** ESPN confirmed as a floor. Unchanged since 25 Nov, and Sat 28 stays unconfirmed until the re-evaluation result is reported, so I added no row.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 02 Dec (Right Knee Dislocated, updated 2026-11-25)
- **Injury:** ESPN est. 02 Dec (Out, Right Knee Dislocated, updated 25 Nov), but the news said on 25 Nov: "He's recovering from a right patellar subluxation and remains without a timetable to return, and while it's encouraging that he's getting reps with Stockton, the big man can be considered week-to-week until the Kings offer another update on his status."
- News (25 Nov): Raynaud (knee) was recalled from the G League's Stockton Kings on Wednesday, Marc J. Spears of ESPN.com reports.
- News (25 Nov): Raynaud (knee) was assigned to the G League's Stockton Kings on Wednesday, James Ham of ESPN 1320 Sacramento reports.
- **Research:**
  - He was Out Wed 25 Nov at GS with a right patella subluxation ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). New on 25 Nov: the Kings assigned him to Stockton for practice and recalled him the same day ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-reaves-redick-reynaud-green.html)). A league source told James Ham "He was a full participant, including 5v5" ([Kings On SI, 25 Nov](https://www.si.com/nba/kings/onsi/kings-maxime-raynaud-gets-promising-injury-update-after-17-game-absence)). RotoWire still has no timetable and calls him week-to-week ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-recalled-to-nba-540983/)).
  - **Expected return:** no timetable reported. The floor is 2 Dec @PHX, 7 days after his 25 Nov out listing. Full 5v5 work makes Sun 29 vs MIN possible, and SAC's report for 29 Nov, due Sat 28, will settle it. *ESPN est.* 2 Dec.
  - **Verdict:** ESPN confirmed as a floor. 2 Dec follows the rule, but his first 5v5 practice means he may come back sooner.
  - Override proposed: return 2026-12-02

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **21.5** · role rate 24.0 · season 30.6 (9) · L7 — · L15 13.0 (1) · L30 21.7 (6) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - Unchanged since 25 Nov. He is sitting until he is traded and has not been to the Smoothie King Center since his request. He "almost certainly won't ever wear a Pelicans uniform again", and NOP "aren't going to be in a hurry" (Rod Walker via [Bleacher Report, 22 Nov](https://bleacherreport.com/articles/25536410-dejounte-murray-hasnt-been-pelicans-arena-trade-request-latest-nba-rumors-suns-talks)). Gambadoro denied any Suns talks ([BasketballNews, 23 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-absolutely-untrue-suns-insider-john-gambadoro-dismisses-dejounte-murray-update-amid-trade-rumor/)). I found no trade and no new report on 25 or 26 Nov.
  - Gap: the standoff continues. The minutes flag (his 8–11 Nov games) does not matter while he is not playing. NOP had not yet filed its report for Fri 27 @LAC ([NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)).
  - **Expected return:** no timetable reported. He is out until he is traded, which means out Fri 27 @LAC and Sun 29 @POR. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is a placeholder, and the 30 Nov row stays.
  - Override proposed: return 2026-11-30

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **5.3** · season 8.8 (12) · L7 — · L15 -3.0 (1) · L30 6.6 (9) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - Unchanged since 25 Nov. He was last listed Out on 23 Nov vs PHX with left plantar fasciitis ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). NOP has given no timeline, and "week-to-week" is RotoWire's own view ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). I found no news since then.
  - Gap: NOP has not played since 23 Nov, and its report for Fri 27 @LAC was not yet filed at 26 Nov 1:15 AM ET ([NBA injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)).
  - **Expected return:** no timetable reported. The week-to-week floor is 26 Nov, so his first chance is Fri 27 @LAC. If NOP lists him out for 27 Nov, the floor becomes 4 Dec. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed as a floor. Nothing new was found, so I added no row.

### Saddiq Bey (NO, SF/PF, free agent)

- Rate **34.2** · role rate 40.6 · season 29.6 (19) → 31.3 (18) · L7 25.5 (4) → 34.0 (3) · L15 32.6 (8) → 37.3 (7) · L30 30.8 (16) → 32.8 (15) · projected 25.9
- ESPN: active
- **Role:** news on 23 Nov: "Bey is not listed in the starting lineup for Monday's game against the Suns."
- **Minutes:** 39.7 min over his last 3 games against 30.6 for the season (+9.1)
- News (23 Nov): Bey is not listed in the starting lineup for Monday's game against the Suns.
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- **Research:** _pending_

### Charles Bassey (GS, C, free agent)

- Rate **27.8** · role rate 33.5 · season 23.3 (16) · L7 35.2 (4) · L15 26.7 (7) · L30 23.0 (15) · projected 14.5
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 14 before; 23.0 min in his starts, against 16.0 for the season
- **Minutes:** 24.3 min over his last 3 games against 16.0 for the season (+8.3)
- News (23 Nov): Bassey recorded 13 points (6-7 FG, 1-2 FT), nine rebounds, three assists and three steals across 26 minutes during Sunday's 88-87 victory over the Celtics.
- News (20 Nov): Bassey ended with 16 points (6-7 FG, 4-5 FT), 13 rebounds, one assist, two blocks and one steal across 25 minutes during Thursday's 126-98 loss to the Grizzlies.
- **Research:** _pending_

### Kenrich Williams (OKC, SF, free agent)

- Rate **27.4** · season 21.3 (19) · L7 33.8 (5) · L15 28.3 (9) · L30 23.9 (16) · projected 14.2
- ESPN: active
- **Role:** news on 22 Nov: "Williams will start Sunday's game against the Heat, Clemente Almanza of USA Today reports."
- News (24 Nov): Williams finished with 20 points (8-13 FG, 4-6 3Pt), nine rebounds, two assists, one block and one steal across 26 minutes during Monday's 125-120 loss to Indiana.
- News (23 Nov): Williams will come off the bench in Monday's matchup with the Pacers, Clemente Almanza of USA Today reports.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.4** · role rate 29.7 · season 26.8 (13) · L7 — · L15 27.5 (2) · L30 26.3 (10) · projected 26.6
- ESPN: out, ESPN est. 28 Nov (Concussion, updated 2026-11-25)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (25 Nov): Allen (concussion) has been ruled out for Wednesday's game against Chicago.
- News (24 Nov): Allen (concussion) is listed as questionable for Wednesday's game versus Chicago.
- **Research:** _pending_

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **34.0** · role rate 23.6 · season 28.6 (16) · L7 46.0 (2) · L15 26.6 (5) · L30 28.8 (13) · projected 26.9
- ESPN: active
- **Minutes:** 25.0 min over his last 3 games against 30.6 for the season (−5.6)
- News (25 Nov): Washington chipped in 14 points (6-11 FG, 1-3 3Pt, 1-2 FT), six rebounds, one block and two steals across 25 minutes during Tuesday's 120-101 win over the Nuggets.
- News (24 Nov): Washington (illness) is available for Tuesday's game in Denver.
- **Research:** _pending_

### De'Andre Hunter (SAC, SF/PF, free agent)

- Rate **32.2** · role rate 30.1 · season 26.1 (16) · L7 36.0 (5) · L15 35.1 (7) · L30 29.6 (13) · projected 23.9
- ESPN: active
- **Minutes:** 39.3 min over his last 3 games against 34.2 for the season (+5.1)
- News (24 Nov): Hunter ended Monday's 123-107 loss to the Spurs with 15 points (7-12 FG, 1-3 3Pt, 0-1 FT), seven rebounds, eight assists and one steal across 38 minutes.
- News (21 Nov): Hunter posted 30 points (12-16 FG, 5-6 3Pt, 1-1 FT), six rebounds, two assists and one block across 37 minutes during Friday's 106-104 loss to the Lakers.
- **Research:** _pending_

### Jakob Poeltl (TOR, C, free agent)

- Rate **32.2** · role rate 33.6 · season 27.4 (15) · L7 38.7 (3) · L15 27.9 (7) · L30 30.8 (12) · projected 31.7
- ESPN: active
- **Minutes:** 29.7 min over his last 3 games against 24.2 for the season (+5.5)
- News (24 Nov): Poeltl recorded 15 points (5-10 FG, 5-6 FT), 10 rebounds, three assists, one block and one steal in 28 minutes before fouling out of Monday's 116-111 loss to the Bucks.
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, free agent)

- Rate **30.9** · role rate 26.1 · season 34.9 (10) · L7 — · L15 26.0 (1) · L30 33.3 (7) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, free agent)

- Rate **30.4** · role rate 36.7 · season 30.2 (17) · L7 30.2 (4) · L15 33.1 (7) · L30 30.5 (14)
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.7 for the season (+6.6)
- News (24 Nov): Jenkins registered 15 points (6-16 FG, 1-6 3Pt, 2-2 FT), four rebounds, 10 assists and two steals in 35 minutes during Tuesday's 104-86 win over the Magic.
- News (23 Nov): Jenkins logged 11 points (4-12 FG, 1-6 3Pt, 2-2 FT), four rebounds, three assists and one steal over 38 minutes during Sunday's 107-97 loss to the Hawks.
- **Research:** _pending_

### Daniel Gafford (DAL, C, free agent)

- Rate **29.7** · role rate 36.7 · season 28.8 (18) · L7 33.5 (4) · L15 26.3 (7) · L30 28.9 (15) · projected 29.3
- ESPN: active
- **Minutes:** 28.7 min over his last 3 games against 22.5 for the season (+6.2)
- News (25 Nov): Gafford had 13 points (6-8 FG, 1-4 FT), six rebounds, three assists, two blocks and one steal in 27 minutes during Tuesday's 120-101 win over the Nuggets.
- News (23 Nov): Gafford notched 10 points (5-8 FG), four rebounds, four assists and two steals over 28 minutes during Sunday's 116-114 win over the Jazz.
- **Research:** _pending_

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **28.6** · season 23.5 (16) · L7 30.0 (4) · L15 31.7 (7) · L30 25.3 (13) · projected 23.2
- ESPN: active
- **Minutes:** news on 24 Nov: "Oubre scored at least 15 points for the sixth straight game, continuing to ramp up after a slow start to the season."
- News (24 Nov): Oubre racked up 20 points (8-13 FG, 4-7 3Pt), four rebounds, two assists and two blocks over 28 minutes during Monday's 125-120 win over Oklahoma City.
- News (23 Nov): Oubre recorded 15 points (4-10 FG, 0-4 3Pt, 7-9 FT) and five rebounds in 27 minutes during Sunday's 113-106 loss to the Knicks.
- **Research:** _pending_

### Rui Hachimura (LAC, SF/PF, free agent)

- Rate **29.4** · season 25.9 (15) · L7 34.2 (4) · L15 27.8 (8) · L30 28.8 (12) · projected 24.0
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (24 Nov): Hachimura logged 19 points (7-10 FG, 2-4 3Pt, 3-3 FT), three rebounds, three assists and one block across 29 minutes during Monday's 116-104 loss to the Rockets.
- News (20 Nov): Hachimura contributed 17 points (7-13 FG, 2-4 3Pt, 1-1 FT), seven rebounds, two assists and one steal in 32 minutes during Thursday's 124-112 loss to the Spurs.
- **Research:** _pending_

### Rudy Gobert (MIN, C, free agent)

- Rate **27.7** · season 26.3 (18) · L7 28.5 (4) · L15 25.5 (8) · L30 26.9 (15) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (21 Nov): Gobert accumulated seven points (2-2 FG, 3-4 FT), 11 rebounds, two assists, three blocks and one steal over 32 minutes during Saturday's 104-95 victory over the Grizzlies.
- News (20 Nov): Gobert posted nine points (4-6 FG, 1-2 FT), seven rebounds and two steals over 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:** _pending_

### Zach Edey (MEM, C, free agent)

- Rate **25.7** · season 24.9 (15) · L7 24.5 (4) · L15 25.7 (6) · L30 23.5 (13) · projected 33.2
- ESPN: day-to-day, ESPN est. 27 Nov (Left Ankle Soreness, updated 2026-11-26)
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the first night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (25 Nov): Edey (ankle) did not return to Wednesday's 115-97 win over the Clippers. He finished with seven points (3-4 FG, 1-1 FT), four rebounds, two assists and two blocks across nine minutes.
- News (25 Nov): Edey (ankle) is doubtful to return to Wednesday's game against the Clippers.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **21.6** · season 20.0 (7) · L7 20.0 (2) · L15 24.6 (5) · L30 20.0 (7) · projected 24.4
- ESPN: day-to-day, ESPN est. 27 Nov (Left Hamstring, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "The veteran floor general is missing both ends of this back-to-back set, but he'll have some extra time to heal up ahead of Friday's tilt against the 76ers."
- News (24 Nov): McConnell (hamstring) was recalled from the G League's Noblesville Boom on Tuesday, Shams Charania of ESPN reports.
- News (24 Nov): McConnell (hamstring) was assigned to the G League's Noblesville Boom on Tuesday.
- **Research:** _pending_

### Julian Reese (NO, PF, free agent)

- Rate **8.0** · season 4.3 (6) · L7 — · L15 6.0 (3) · L30 4.3 (6)
- ESPN: day-to-day, ESPN est. 25 Nov (Right Knee, updated 2026-11-25)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (16 Nov): The Pelicans transferred Reese from the G League's Laketown Squadron, and he will be available for New Orleans' game against the Warriors on Monday.
- News (24 Sep): Reese agreed to a two-way contract with the Pelicans on Thursday, Keith Smith of Spotrac.com reports.
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

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **34.4** · season 39.9 (12) · L7 — · L15 26.0 (1) · L30 38.6 (10) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:** _pending_

### Josh Hart (NY, SG/SF, Dr White Slong)

- Rate **29.5** · role rate 32.5 · season 27.5 (15) · L7 35.5 (4) · L15 24.9 (8) · L30 25.4 (12) · projected 33.0
- ESPN: active
- **Minutes:** 36.7 min over his last 3 games against 31.1 for the season (+5.6)
- News (25 Nov): Hart compiled 15 points (6-14 FG, 1-5 3Pt, 2-3 FT), seven rebounds, 11 assists, three steals and one block in 36 minutes during Wednesday's 121-102 win over Cleveland.
- News (25 Nov): Hart (shoulder) is available for Wednesday's game against the Cavaliers, Steve Popper of Newsday reports.
- **Research:** _pending_

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **47.5** · season 39.4 (14) · L7 59.5 (2) · L15 44.4 (5) · L30 37.5 (11) · projected 45.4
- ESPN: day-to-day, ESPN est. 27 Nov (Illness, updated 2026-11-26)
- **Rest:** back-to-back Fri 27–Sat 28 Nov, Tue 01–Wed 02 Dec; sat the second night of the 24–25 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side; sat the first night of the 15–16 Nov back-to-back, playing the games either side
- News (25 Nov): Embiid (illness) is out for Wednesday's game against Miami, Ira Winderman of the South Florida Sun Sentinel reports.
- News (24 Nov): Embiid (illness) is listed as doubtful for Wednesday's game versus Miami.
- **Research:** _pending_

### Amen Thompson (HOU, SG/SF, Matt Wright's Foxies)

- Rate **39.3** · season 37.5 (18) · L7 39.0 (4) · L15 42.4 (7) · L30 35.2 (15) · projected 40.0
- ESPN: active
- **Rest:** back-to-back Mon 30–Tue 01 Dec; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (24 Nov): Thompson ended Monday's 116-104 victory over the Clippers with 20 points (9-12 FG, 1-1 3Pt, 1-2 FT), four rebounds, five assists and one block over 28 minutes.
- News (21 Nov): Thompson chipped in 22 points (10-12 FG, 0-1 3Pt, 2-6 FT), six rebounds and one steal in 26 minutes during Friday's 133-124 loss to the Nuggets.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **39.0** · season 39.1 (17) · L7 39.2 (4) · L15 37.6 (7) · L30 39.8 (14) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "After carrying a questionable tag ahead of both parts of this back-to-back, Siakam is suiting up Monday despite dealing with a left hip injury."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Siakam (hip) will play in Monday's game against the Thunder, Justin Martinez of The Oklahoman reports.
- News (23 Nov): Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **29.1** · season 31.8 (14) · L7 26.7 (3) · L15 27.2 (5) · L30 31.9 (11) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Nembhard produced 16 points (5-13 FG, 2-3 3Pt, 4-7 FT), two rebounds and eight assists in 32 minutes during Sunday's 113-106 loss to the Knicks.
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- **Research:** _pending_

### Derrick White (BOS, PG/SG, Dr White Slong)

- Rate **28.1** · season 29.5 (17) · L7 25.7 (3) · L15 27.1 (7) · L30 29.0 (15) · projected 37.0
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the first night of the 21–22 Nov back-to-back, playing the games either side
- News (25 Nov): White notched six points (2-10 FG, 2-6 3Pt), seven rebounds, five assists and one steal across 30 minutes during Tuesday's 131-116 victory over Washington.
- News (23 Nov): White amassed 14 points (6-21 FG, 2-12 3Pt), three rebounds, five assists and one steal over 32 minutes during Sunday's 88-87 loss to the Warriors.
- **Research:** _pending_

### Jonathan Kuminga (MIN, SF/PF, Dr White Slong)

- Rate **26.3** · season 27.9 (18) · L7 26.5 (4) · L15 25.9 (7) · L30 26.7 (15) · projected 26.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 16–17 Nov back-to-back, playing the games either side
- News (24 Nov): Kuminga contributed 15 points (5-12 FG, 1-5 3Pt, 4-6 FT), five rebounds, four assists and one steal in 26 minutes during Monday's 142-116 win over the Nets.
- News (19 Nov): Kuminga totaled 23 points (7-13 FG, 2-4 3Pt, 7-7 FT), three rebounds, three assists and three blocks in 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:** _pending_

## Other rosters: injury flags only

### Jalen Brunson (NY, PG, Melbourne poopoo)

- Rate **39.9** · season 40.5 (18) · L7 36.0 (4) · L15 41.6 (9) · L30 42.7 (15) · projected 43.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 25 Nov: "Brunson (illness) has been downgraded to questionable for Wednesday's game against the Cavaliers."
- News (25 Nov): Brunson finished with 19 points (6-22 FG, 2-8 3Pt, 5-6 FT), three rebounds and five assists over 36 minutes during Wednesday's 121-102 victory over the Cavaliers.
- News (25 Nov): Brunson (illness) is available for Wednesday's game against the Cavaliers, Ian Begley of SportsNet New York reports.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-26 06:13 UTC.
