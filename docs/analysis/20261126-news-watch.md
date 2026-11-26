# News watch: 26 Nov 2026

- Generated 2026-11-26 06:13 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Matt Wright's Foxies, Dr White Slong). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 41 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Our players:**
  - **Jalen Duren:** practised with the Pistons Tue and the G League Cruise Wed. Bickerstaff is "looking forward to getting him back" ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)). No target game: no timetable reported; *ESPN est.* 30 Nov. Sun 29 vs ORL is possible, Fri 27 less likely. His rate (44.1) rests on one game (small sample).
  - **Cade Cunningham:** day-to-day with right knee soreness, "far less than 100 percent" ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)). No timetable reported; *ESPN est.* 27 Nov. Fri vs MIL is his next chance. L7 36.5 (2), a small sample, after the knee and a foul-trouble game on 22 Nov.
  - **Jalen Smith** missed Wed with a stomach illness: no timetable reported; *ESPN est.* 28 Nov, which is Chicago's next game. **Yaxel Lendeborg** started Wed (31 min).
  - **Kawhi Leonard:** out Fri and Sun; the Raptors' next update is about 1 Dec ([NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week)). *ESPN est.* 3 Dec.
  - **Paul George** and **Neemias Queta** play Fri and Sun. Mitchell Robinson is still out (no timetable reported; *ESPN est.* 27 Nov), so Queta keeps the start. Mon 30 (next week) is the rest risk for both.
  - **Myles Turner** played Wed (26 min). Sat 28 vs OKC is the second night of a back-to-back; he rested on one of three. Nothing is announced.
  - **Anthony Black:** Orlando signed Kevin Porter Jr. as a bench scorer ([AP via TSN, 25 Nov](https://www.tsn.ca/nba/article/porter-jr-signs-with-magic-after-getting-waived-by-bucks-before-season/)). No source says Black loses his start. Sun 29 at DET is the second night of Orlando's back-to-back. Banchero: no timetable reported; floor row 1 Dec; *ESPN est.* 29 Nov.
- **Targets:**
  - **Charles Bassey** started again Wed (22 min, 24 FP; Horford 13 min off the bench). His 24-min row stays.
  - **Norman Powell:** no re-evaluation result. He missed Wed, his third straight game. No source says he plays Sat vs IND; *ESPN est.* 28 Nov. Chicago's Saturday report comes Friday afternoon ET, before Saturday's add deadline (9:00 AM Sun Melbourne).
  - **Saddiq Bey** comes off New Orleans' bench at about 30 min Fri and Sun. New Orleans has no back-to-back this week.
  - **De'Andre Hunter** played 39 min Wed with Zach LaVine a late scratch (knee soreness; no timetable reported; *ESPN est.* 29 Nov). His Sunday start holds. Maxime Raynaud practised 5-on-5 in Stockton ([Kings On SI, 25 Nov](https://www.si.com/nba/kings/onsi/kings-maxime-raynaud-gets-promising-injury-update-after-17-game-absence)); his 2 Dec floor row stays (*ESPN est.* 2 Dec).
  - **Daniss Jenkins** starts while Duren is out, with or without Cunningham. His 37-min row stays through Fri.
  - **Kelly Oubre Jr.** likely goes to the bench when Tyrese Haliburton returns, possibly Fri ([IndyStar via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/tyrese-haliburton-provided-good-news-201537475.html)). Haliburton: no timetable reported; *ESPN est.* 13 Dec, which looks late.
  - **Grayson Allen** missed Wed (concussion protocol; no timetable reported; *ESPN est.* 28 Nov).
  - **Zach Edey** left Wed after 9 min with left ankle soreness (day-to-day; *ESPN est.* 27 Nov).
  - **Ja Morant** is doing 5-on-5 and should be back during Portland's home stand, which ends 3 Dec ([Blazer's Edge, 25 Nov](https://www.blazersedge.com/trail-blazers-news/118895/portland-trail-blazers-ja-morant-nba-injury-news-return-micah-nori-spurs-grizzlies)). His 28 Nov floor row stays (*ESPN est.* 1 Dec).
- **This week's opponent (Matt Wright's Foxies):**
  - **Evan Mobley:** first possible game Sun 29 (*ESPN est.* 29 Nov).
  - **Pascal Siakam** and **Andrew Nembhard:** no sit announced for Indiana's Fri–Sat back-to-back. Haliburton's return would cut their share.
  - **Amen Thompson** is healthy and plays only Sat.
- **Next week's opponent (Dr White Slong):** Embiid missed Wed with an illness and may miss part of Philadelphia's Fri–Sat back-to-back (*ESPN est.* 27 Nov). Josh Hart's big minutes last while OG Anunoby is out. Banchero's floor stays 1 Dec.
- **Overrides:**
  - **Re-sourced, same values:** Morant, Bassey, Nurkic, Raynaud, Dejounte Murray, Banchero, Jenkins.
  - **Removed:** Scotty Pippen Jr.'s 30 Nov floor. ESPN moved his estimate to 12 Dec, so the floor was stale.
  - **Not added:** Powell, Duren and Haliburton. No source gives a date for any of them.
- **Re-run the matchup:** yes. Done: the plan uses these rows.

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
- **Research:**
  - Rest: unchanged since 25 Nov. NOP has no back-to-back this week: Fri 27 @LAC (9:30 PM ET), then Sun 29 @POR (6:00 PM ET). The back-to-back is Sun 29 @POR into Mon 30 @SAC, so Sun 29 is the first night and the rest risk falls on Mon 30, next week. He sat Sat 21, the second night of 20–21 Nov, "to ease him back into action" from bilateral patellar tendinopathy ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-returning-to-starting-five/); [Yahoo/HoopsHype, 21 Nov](https://sports.yahoo.com/articles/pelicans-rest-trey-murphy-against-182359369.html)). No news on him since 24 Nov. NOP's Fri 27 report was "not yet submitted" at 1:00 AM ET on 26 Nov ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)).
  - Form: on Mon 23 he started and played 35 min (with OT), no limit mentioned ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-low-usage-continues-monday/)). L7 31.5 (2) and L15 31.5 (2) are small samples. L30 is 32.2 (8), season 31.1 (11), rate 32.3.
  - **Verdict:** nothing new found (unchanged since 25 Nov). He should play Fri 27 and Sun 29. Mon 30 is next week's rest risk, and no sit has been announced, so no row.

### Myles Turner (MIL, C, us)

- Rate **32.1** · season 28.6 (17) · L7 35.8 (4) · L15 31.1 (7) · L30 30.6 (14) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (24 Nov): Turner closed with 27 points (9-12 FG, 5-6 3Pt, 4-5 FT), 11 rebounds, one assist and two blocks over 28 minutes before fouling out of Monday's 116-111 victory over Toronto.
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- **Research:**
  - Wed 25 vs BKN: he started and played 26 min, with 3 pts (1-2 FG), 6 reb, 2 ast, 1 stl, 3 blk and 3 TO (25 FP) in a 104-97 loss. No injury. Kel'el Ware played 22 min off the bench ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322)). MIL listed no players on the report for that game ([NBA injury report, 25 Nov 8:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_08_30PM.pdf)).
  - Rest, Sat 28 vs OKC (8:00 PM ET; second night after Fri 27 @DET, 7:30 PM ET): no announcement. His back-to-back record: he played both nights of 23–24 Oct, sat 11 Nov listed as "rest" ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/myles-turner-rest-ruled-out-vs-los-angeles)), and missed 19 Nov with a left shoulder contusion, not rest ([NBA injury report, 19 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). That is one rest sit in three back-to-backs. MIL's Fri 27 report was not yet submitted at 1:00 AM ET 26 Nov, and the Sat 28 listing comes out Friday afternoon ET.
  - Form: L7 35.8 (4) is 7.1 over his 28.6 (17) season average. The reason is shooting, mainly the 27-pt, 54-FP night at TOR on 23 Nov. His minutes are unchanged (season 26.6, L7 25.2). L15 is 31.1 (7), L30 30.6 (14), rate 32.1.
  - **Verdict:** nothing new found. He is a healthy starter. Sat 28 is a real but unconfirmed rest risk (one in three so far), so no sit row.

### Anthony Black (ORL, PG/SG, us)

- Rate **30.9** · season 35.3 (14) · L7 25.5 (4) · L15 32.9 (8) · L30 34.6 (13) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (25 Nov): Black finished with five points (2-8 FG, 0-2 3Pt, 1-3 FT), four rebounds, two assists and one block over 28 minutes during Tuesday's 104-86 loss to the Pistons.
- News (23 Nov): Black chipped in 14 points (5-12 FG, 2-4 3Pt, 2-2 FT), five rebounds, two assists and two steals in 35 minutes during Sunday's 116-96 loss to the Wizards.
- **Research:**
  - Role: Kevin Porter Jr. signed Wed 25 Nov on a two-year deal for Orlando's 15th roster spot. No debut date has been given ([Orlando Sentinel via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/magic-finalizing-deal-free-agent-190200324.html); [AP via TSN, 25 Nov](https://www.tsn.ca/nba/article/porter-jr-signs-with-magic-after-getting-waived-by-bucks-before-season/)). NBC's Helin: "the Magic play Jalen Suggs and Anthony Black for most of the guard minutes"; they "want some scoring off the bench, and Porter can give them that," so it "can work" "in a backup role" ([NBC Sports via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/kevin-porter-jr-reportedly-sign-204545897.html)). No source says Black loses his start. Porter may trim a few bench-overlap minutes once he plays.
  - Paolo Banchero (right high ankle sprain; no timetable reported, and Sweeney said "No timeline right now" on 18 Nov, [Yahoo, 18 Nov](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html); override floor 1 Dec; *ESPN est.* 29 Nov): no update since he was ruled out on Tue 24. Black keeps his start while Banchero is out.
  - Rest, Sun 29 @DET (6:00 PM ET; second night after Sat 28 @WSH, 5:00 PM ET): unchanged. He sat 2 Nov, a second night, as left ankle injury management ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/)), and played both nights of 10–11 Nov. No sit has been announced.
  - Form: L7 25.5 (4) is 9.8 under his 35.3 (14) season average. The causes are poor shooting and the 3-FP game on Tue 24 (28 min, 5 TO), not lost minutes (season 32.9, L7 34.2). L15 is 32.9 (8), L30 34.6 (13), rate 30.9.
  - **Verdict:** nothing new on his health. He is a healthy starter. Porter joins as a bench scorer, not a threat to Black's start this week. Sun 29 is an unannounced rest risk, so no row.

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
- **Research:**
  - Role: unchanged since 25 Nov. NOP has not played since Mon 23. That night Trey Murphy III rejoined the starters, and Bey scored 21 off the bench in 40 min of a 123-119 OT loss ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/saddiq-bey-scores-21-points-off-bench-in-loss)). The bench role lasts while Murphy plays. Murphy has no back-to-back this week, so expect Bey off the bench on both Fri 27 @LAC and Sun 29 @POR. NOP's Fri 27 report was not yet submitted at 1:00 AM ET 26 Nov.
  - Minutes: the 39.7-min figure includes his starts and 5 min of OT. Wing minutes stay open while Bennedict Mathurin (left plantar fasciitis; no timetable reported; *ESPN est.* 27 Nov) and Dejounte Murray (left ankle, sitting until traded; override floor 30 Nov; *ESPN est.* 27 Nov) are out. No new update was found on either. Expect about 30 min (28–34). Form: L7 25.5 (4) → 34.0 (3), with the 0-FP game on 21 Nov dropped. L15 is 32.6 (8) → 37.3 (7), L30 30.8 (16) → 32.8 (15), season 29.6 (19) → 31.3 (18), rate 34.2. The role rate of 40.6 assumes the 39.7-min role, which no source supports.
  - **Verdict:** nothing new found (unchanged since 25 Nov). The bench role is ongoing, but the 30-min estimate rests on one OT game, so no row.

Summary:
- Bassey started again Wed 25 vs SAC (22 min, 24 FP, Horford bench 13 min). The role row is refreshed at 24 min until 8 Dec.
- Turner (Sat 28) and Black (Sun 29) are unannounced back-to-back rest risks. Turner has sat one second night in three for rest. Black sat one in two (ankle management). Murphy's risk is Mon 30, next week, so Bey stays a bench player for Fri 27 and Sun 29.
- Kevin Porter Jr. signed with ORL on 25 Nov as a bench scorer. Sources say Suggs and Black keep most guard minutes, and Banchero still has no timetable (override floor 1 Dec; *ESPN est.* 29 Nov).

### Charles Bassey (GS, C, free agent)

- Rate **27.8** · role rate 33.5 · season 23.3 (16) · L7 35.2 (4) · L15 26.7 (7) · L30 23.0 (15) · projected 14.5
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 14 before; 23.0 min in his starts, against 16.0 for the season
- **Minutes:** 24.3 min over his last 3 games against 16.0 for the season (+8.3)
- News (23 Nov): Bassey recorded 13 points (6-7 FG, 1-2 FT), nine rebounds, three assists and three steals across 26 minutes during Sunday's 88-87 victory over the Celtics.
- News (20 Nov): Bassey ended with 16 points (6-7 FG, 4-5 FT), 13 rebounds, one assist, two blocks and one steal across 25 minutes during Thursday's 126-98 loss to the Grizzlies.
- **Research:**
  - Role: he started Wed 25 vs SAC (Melton, Podziemski, Lendeborg, Green, Bassey) and played 22 min, with 10 pts (4-9 FG), 7 reb, 1 ast, 2 blk, 2 TO and 3 PF (24 FP) in a 129-110 win. Horford came off the bench for 13 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)). SI says the group "played well together" and that Kerr "might have found a lineup he can turn to until Stephen Curry returns" ([SI, 25 Nov](https://www.si.com/nba/warriors/onsi/takeaways-from-warriors-win-over-kings-why-acuff-lendeborg-have-intriguing-roy-race-01m8b12gmrh7)). Curry has a right oblique tear and is to be re-evaluated Fri 27 ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-stephen-curry-to-be-re-evaluated-friday/); *ESPN est.* 12 Dec). On 24 Nov Kerr said the Bassey start is "hopefully for the season" ([Yahoo, 24 Nov](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html)).
  - Minutes: 22, 25, 26 and 22 in his last four starts, about 24. The rise comes from the starting role, not from blowouts. The only center whose return would end it is Kristaps Porzingis (stepped away, not with team; no timetable reported; *ESPN est.* 2 Jan). GS plays Fri 27 @POR (9:30 PM ET) and Sun 29 vs LAC (8:30 PM ET), not a back-to-back. Form: L7 35.2 (4) is 11.9 over his 23.3 (16) season average because of the starts (minutes 16.0 for the season, 23.8 in L7). L15 is 26.7 (7), L30 23.0 (15), rate 27.8, role rate 33.5.
  - **Verdict:** ESPN confirmed (active). He started a fourth time and played 22 min. The role row (24 min, until 8 Dec) holds, with a refreshed note.
  - Override proposed: role 24

### Kenrich Williams (OKC, SF, free agent)

- Rate **27.4** · season 21.3 (19) · L7 33.8 (5) · L15 28.3 (9) · L30 23.9 (16) · projected 14.2
- ESPN: active
- **Role:** news on 22 Nov: "Williams will start Sunday's game against the Heat, Clemente Almanza of USA Today reports."
- News (24 Nov): Williams finished with 20 points (8-13 FG, 4-6 3Pt), nine rebounds, two assists, one block and one steal across 26 minutes during Monday's 125-120 loss to Indiana.
- News (23 Nov): Williams will come off the bench in Monday's matchup with the Pacers, Clemente Almanza of USA Today reports.
- **Research:**
  - Role: the start on Sun 22 at MIA was a one-off. Gilgeous-Alexander (back/neck), Caruso, Mara and Jaylin Williams were all out ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-kenrich-williams-starting-versus-heat/); [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910030)). He came off the bench on Mon 23 (26 min, 52 FP) and again on Wed 25 vs MIN: 13 pts, 5 reb in 25 min. OKC started SGA, Stirtz, Mitchell, Peavy and Hartenstein ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/thunder-start-shai-stirtz-ajay-peavy-i-hart); [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320)).
  - Why his minutes are up: OKC is short of frontcourt players. Aday Mara (right shin contusion) missed his third straight game Wed; Daigneault said it "acted up before the game", and no timetable has been reported ([Yahoo, 24 Nov](https://sports.yahoo.com/articles/mark-daigneault-provides-nba-injury-190008603.html); *ESPN est.* 28 Nov). Jaylin Williams (low back spasms) is out too, with no timetable reported (*ESPN est.* 28 Nov). Holmgren is out 8 to 10 weeks from 30 Oct (*ESPN est.* 2 Jan) ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf)). Caruso returned Wed (26 min), and Williams still got 25.
  - How long: until Mara or Jaylin Williams returns, possibly as soon as Sat 28 @MIL, OKC's only game left this week. No coach comment on his role was found. L7 33.8 (5) against 21.3 for the season: 25–28 min a night against about 20 before, plus the 52-FP game.
  - **Verdict:** ESPN confirmed (active). He is a bench player for about 25 min while the bigs are out. No row, because neither the start nor the minutes are reported as ongoing.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.4** · role rate 29.7 · season 26.8 (13) · L7 — · L15 27.5 (2) · L30 26.3 (10) · projected 26.6
- ESPN: out, ESPN est. 28 Nov (Concussion, updated 2026-11-25)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (25 Nov): Allen (concussion) has been ruled out for Wednesday's game against Chicago.
- News (24 Nov): Allen (concussion) is listed as questionable for Wednesday's game versus Chicago.
- **Research:**
  - Injury: he did **not** return Wed 25. He was ruled out vs CHI (Concussion Protocol), his fourth straight miss after 17, 20 and 23 Nov ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf); [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-wednesday/)). No clearance or practice report has been found. Charlotte's next game is Sat 28 vs BKN, and its report for that game is not out yet.
  - Role for Sat 28 if cleared: he comes off the bench. His starts came only while Brandon Miller was out ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/)). Wed's starters were Miller (34 min), Sion James (available, thigh), White, Reid and Diabate, and Christian Anderson played 28 min off the bench ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)). Knueppel (hamstring; re-evaluation about 6 Dec; *ESPN est.* 12 Dec) and Schroder (hamstring; no update since his re-evaluation date passed; *ESPN est.* 12 Dec) are still out, which keeps about 25 bench minutes open for him. His L15 of 27.5 rests on 2 games (small sample).
  - **Expected return:** no timetable reported. He is in the concussion protocol, and Sat 28 vs BKN is his next chance to play ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-wednesday/)). *ESPN est.* 28 Nov.
  - **Verdict:** ESPN confirmed. 28 Nov is his next possible game, but he has not been cleared. No row.

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **34.0** · role rate 23.6 · season 28.6 (16) · L7 46.0 (2) · L15 26.6 (5) · L30 28.8 (13) · projected 26.9
- ESPN: active
- **Minutes:** 25.0 min over his last 3 games against 30.6 for the season (−5.6)
- News (25 Nov): Washington chipped in 14 points (6-11 FG, 1-3 3Pt, 1-2 FT), six rebounds, one block and two steals across 25 minutes during Tuesday's 120-101 win over the Nuggets.
- News (24 Nov): Washington (illness) is available for Tuesday's game in Denver.
- **Research:**
  - Role: unchanged since 25 Nov. Dusty May kept Risacher starting Tue at DEN ("didn't want to rock the boat") and said Washington "looked great in that second unit". He made no commitment for Friday ([Dallas Sports Journal, 25 Nov](https://dallassportsjournal.com/pj-washington-bench-return-dusty-may-mavericks-nuggets/); [Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/p-j-washington-return-shows-182629902.html)). Rotoworld says the rotation "could change as soon as Friday's game against the Suns" ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/p-j-washington-illness-scores-14-in-return)). DAL did not play Wed, and its Fri report is not submitted yet ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)).
  - Minutes: 24:37 Tue, only 9 of them in the second half, which looked like easing him back after the illness (Yahoo, above). Expect about 25 min off the bench Fri 27 @PHX, DAL's only game left this week, unless he gets the start back. L7 46.0 rests on 2 games (small sample).
  - **Verdict:** nothing new found. A start or the bench for Friday is undecided. No row, because the bench role is not reported as ongoing. His role rate at 25 min is 23.6, against a rate of 34.0.

### De'Andre Hunter (SAC, SF/PF, free agent)

- Rate **32.2** · role rate 30.1 · season 26.1 (16) · L7 36.0 (5) · L15 35.1 (7) · L30 29.6 (13) · projected 23.9
- ESPN: active
- **Minutes:** 39.3 min over his last 3 games against 34.2 for the season (+5.1)
- News (24 Nov): Hunter ended Monday's 123-107 loss to the Spurs with 15 points (7-12 FG, 1-3 3Pt, 0-1 FT), seven rebounds, eight assists and one steal across 38 minutes.
- News (21 Nov): Hunter posted 30 points (12-16 FG, 5-6 3Pt, 1-1 FT), six rebounds, two assists and one block across 37 minutes during Friday's 106-104 loss to the Lakers.
- **Research:**
  - Role: he started again Wed 25 at GS: 15 pts, 7 reb, 3 ast, 1 stl in 39 min, his fifth straight game at 35 min or more ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/kings-start-acuff-sharp-hunter-murray-sabonis); [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)). He was not on Sacramento's official report Wed ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf)).
  - Minutes: the +5 min comes from a thin roster. Simmons is out for the season with a torn Achilles (*ESPN est.* 1 Oct 2027, a stale date). Raynaud (patella subluxation) is out, with a row to 2 Dec (*ESPN est.* 2 Dec). Zach LaVine (right knee soreness) was a late scratch Wed, with no timetable reported ([Anthony Slater, 25 Nov](https://x.com/anthonyVslater/status/2125723596157026468); *ESPN est.* 29 Nov). Expect a start at 35–40 min Sun 29 vs MIN. The risk is his left hip soreness, which cost him 15 Nov and left him questionable 18 and 20 Nov ([NBA injury report, 20 Nov 1:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_01_00PM.pdf)). L7 36.0 (5) against 26.1 for the season: 37–41 min plus the 59-FP game on 20 Nov.
  - **Verdict:** ESPN confirmed (active). His start for Sunday holds. No row: no source gives a minutes figure, and his rate already counts these games.

### Jakob Poeltl (TOR, C, free agent)

- Rate **32.2** · role rate 33.6 · season 27.4 (15) · L7 38.7 (3) · L15 27.9 (7) · L30 30.8 (12) · projected 31.7
- ESPN: active
- **Minutes:** 29.7 min over his last 3 games against 24.2 for the season (+5.5)
- News (24 Nov): Poeltl recorded 15 points (5-10 FG, 5-6 FT), 10 rebounds, three assists, one block and one steal in 28 minutes before fouling out of Monday's 116-111 loss to the Bucks.
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- **Research:**
  - Role: unchanged since 25 Nov. TOR has not played since Mon 23, when he started at center (28 min, 41 FP, fouled out) and Murray-Boyles came off the bench in his return from the concussion protocol ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039); [CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-manning-bench-role-in-return/)). No practice or lineup news has come out since. Rotoworld still flags that the days off "may be enough time to get Murray-Boyles back into the starting lineup" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)). TOR's Friday report is not submitted yet ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)).
  - Openings: Barrett (hamstring; re-evaluation about 3 Dec; *ESPN est.* 13 Dec) and Leonard ("at least another week" from 24 Nov; *ESPN est.* 3 Dec) are out all week ([NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week)). TOR plays Fri 27 vs BKN and Sun 29 vs DEN. L7 38.7 (3) against 27.4 for the season: 28–32 min as a starter against 17–18 off the bench.
  - **Verdict:** nothing new found. He is the likely starter Fri and Sun at about 28–32 min, but neither start is confirmed. No row.

### Caleb Wilson (CHI, SF, free agent)

- Rate **30.9** · role rate 26.1 · season 34.9 (10) · L7 — · L15 26.0 (1) · L30 33.3 (7) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Injury: unchanged since 25 Nov. The official report listed him out for Wed 25 at CHA with a right metacarpal fracture ([NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf)). The Bulls said he would be re-evaluated three weeks after his 12 Nov surgery, so about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). Charania reported four to six weeks ([ESPN, 12 Nov](https://www.espn.com/nba/story/_/id/50464091/sources-bulls-wilson-surgery-hand-4-6-weeks)). No newer update was found.
  - Minutes flag: the low last-3 figure comes from his 15-min injury exit on 11 Nov. It does not matter while he is out.
  - **Expected return:** four to six weeks from 12 Nov (10 to 24 Dec), with a re-evaluation about 3 Dec. He will not play this week. *ESPN est.* 13 Dec.
  - **Verdict:** ESPN confirmed. The team timeline has not changed, and 13 Dec falls inside the reported range.

### Daniss Jenkins (DET, PG, free agent)

- Rate **30.4** · role rate 36.7 · season 30.2 (17) · L7 30.2 (4) · L15 33.1 (7) · L30 30.5 (14)
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.7 for the season (+6.6)
- News (24 Nov): Jenkins registered 15 points (6-16 FG, 1-6 3Pt, 2-2 FT), four rebounds, 10 assists and two steals in 35 minutes during Tuesday's 104-86 win over the Magic.
- News (23 Nov): Jenkins logged 11 points (4-12 FG, 1-6 3Pt, 2-2 FT), four rebounds, three assists and one steal over 38 minutes during Sunday's 107-97 loss to the Hawks.
- **Research:**
  - Role, Cunningham: DET has not played since Tue 24, so nothing has changed since 25 Nov. Cunningham's return does not end Jenkins's start. Jenkins has started beside Cunningham since 9 Nov and played 35 to 42 min in those games. On 17 Nov, for example, he scored 25 in 38 min while Cunningham scored 27 ([AP via WXYZ, 17 Nov](https://www.wxyz.com/sports/basketball/pistons/cunningham-jenkins-lead-surge-as-pistons-snap-spurs-12-game-winning-streak-with-105-93-victory)). Cunningham (right knee soreness, day-to-day, no timetable reported, *ESPN est.* 27 Nov) is "far less than 100 percent." Friday vs MIL is his next chance to play ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)).
  - Role, Duren: Jenkins took Paul Reed's starting spot on 9 Nov. Bickerstaff picks that fifth starter game by game only until Duren returns ([Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html)). Duren (right hamstring, no target date, *ESPN est.* 30 Nov) practised with the team on 24 Nov and with the Cruise on 25 Nov. NBC says that "doesn't guarantee he'll be back on Friday, but it shouldn't be much longer" ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/news/nba-week-6-injury-report-cameron-boozer-to-miss-at-least-four-weeks-dont-panic-on-cade-cunningham)). Duncan Robinson (left quad, day-to-day, *ESPN est.* 27 Nov) is also close to returning. Off the bench before 9 Nov, Jenkins played 21 to 24 min (ESPN box scores). No source says whether he keeps the start if Duren returns while Cunningham sits. DET had not filed its Fri 27 report as of 26 Nov 1:00 AM ET.
  - **Verdict:** ESPN confirmed: active. He starts at about 37 min while Duren is out, with or without Cunningham. Keep the row through Fri 27 and remove it for Fri if DET lists Duren as available. Do not extend it to Sun 29 unless Duren is ruled out.
  - Override proposed: role 37

### Daniel Gafford (DAL, C, free agent)

- Rate **29.7** · role rate 36.7 · season 28.8 (18) · L7 33.5 (4) · L15 26.3 (7) · L30 28.9 (15) · projected 29.3
- ESPN: active
- **Minutes:** 28.7 min over his last 3 games against 22.5 for the season (+6.2)
- News (25 Nov): Gafford had 13 points (6-8 FG, 1-4 FT), six rebounds, three assists, two blocks and one steal in 27 minutes during Tuesday's 120-101 win over the Nuggets.
- News (23 Nov): Gafford notched 10 points (5-8 FG), four rebounds, four assists and two steals over 28 minutes during Sunday's 116-114 win over the Jazz.
- **Research:**
  - Minutes: DAL has not played since Tue 24, so nothing has changed since 25 Nov. At DEN he started with Risacher, Martin, Irving and Flagg. P.J. Washington, back from illness, came off the bench for the first time this season and had 14 pts and 6 reb. May kept Risacher in the lineup to keep the group's continuity, and the article does not say whether that will last ([Dallas Morning News via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/5-thoughts-mavericks-nuggets-dallas-054348956.html)). Gafford played 27 min for 36 FP ([ESPN box score, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316)).
  - No newer update was found on Lively (right foot surgery, no timetable reported, *ESPN est.* 27 Nov). May said on 20 Nov that Lively feels "close" ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-dereck-lively-progressing-in-recovery/)). DAL had not filed its Fri 27 report as of 26 Nov 1:00 AM ET. Their only game left this week is Fri 27 at PHX.
  - **Verdict:** ESPN confirmed: active and starting. Expect about 27 min on Fri 27 if the lineup holds. No row: it rests on one game, and no source calls the role ongoing.

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **28.6** · season 23.5 (16) · L7 30.0 (4) · L15 31.7 (7) · L30 25.3 (13) · projected 23.2
- ESPN: active
- **Minutes:** news on 24 Nov: "Oubre scored at least 15 points for the sixth straight game, continuing to ramp up after a slow start to the season."
- News (24 Nov): Oubre racked up 20 points (8-13 FG, 4-7 3Pt), four rebounds, two assists and two blocks over 28 minutes during Monday's 125-120 win over Oklahoma City.
- News (23 Nov): Oubre recorded 15 points (4-10 FG, 0-4 3Pt, 7-9 FT) and five rebounds in 27 minutes during Sunday's 113-106 loss to the Knicks.
- **Research:**
  - Role: IND has not played since Mon 23, so nothing has changed since 25 Nov. Oubre has started since 11 Nov and played 23 to 28 min in his last four games. His L7 of 30.0 (4 games) is 6.5 over his season 23.5, because of the start and 15+ points in six straight games.
  - Haliburton (left hamstring strain, no official date, *ESPN est.* 13 Dec) practised with the Boom on 24 Nov and fully with the Pacers on 25 Nov. He wants to be back by next week "at the absolute latest." Asked about Fri 27 vs PHI, Carlisle said "stay tuned" ([IndyStar via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/tyrese-haliburton-provided-good-news-201537475.html)). The signs point to Fri 27 or Sat 28 @CHI, once he is checked after two practices ([Indy Cornrows, 25 Nov](https://www.indycornrows.com/p/pacers-quiet-thunder-face-sixers)). NBC says "His eventual return will push Kelly Oubre Jr. to the bench" and calls Friday the likeliest date ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/news/nba-week-6-injury-report-cameron-boozer-to-miss-at-least-four-weeks-dont-panic-on-cade-cunningham)).
  - In Haliburton's four games (21 to 26 Oct), Oubre played 20 to 28 min and scored 8 to 22 FP (ESPN box scores). Nesmith (right foot soreness, *ESPN est.* 27 Nov) said he will play Fri. IND had not filed its Fri 27 report as of 26 Nov 1:00 AM ET.
  - **Verdict:** ESPN confirmed: active and starting for now. He likely moves to the bench at about 20 to 23 min once Haliburton returns, which could be Fri 27 or Sat 28. No row until IND confirms.

### Rui Hachimura (LAC, SF/PF, free agent)

- Rate **29.4** · season 25.9 (15) · L7 34.2 (4) · L15 27.8 (8) · L30 28.8 (12) · projected 24.0
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (24 Nov): Hachimura logged 19 points (7-10 FG, 2-4 3Pt, 3-3 FT), three rebounds, three assists and one block across 29 minutes during Monday's 116-104 loss to the Rockets.
- News (20 Nov): Hachimura contributed 17 points (7-13 FG, 2-4 3Pt, 1-1 FT), seven rebounds, two assists and one steal in 32 minutes during Thursday's 124-112 loss to the Spurs.
- **Research:**
  - Rest: LAC has no back-to-back this week (Fri 27 vs NOP, Sun 29 @GSW). The flagged back-to-back is Tue 1 and Wed 2 Dec, and no sit has been announced. His one absence on a back-to-back, 2 Nov, was left quad soreness, not rest ([NBA injury report, 2 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_08_00PM.pdf)).
  - Role: he started Wed 25 at MEM and played a team-high 37 min: 14 pts (5-13 FG), a season-high 12 reb and 5 ast for 36 FP ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/rui-hachimura-records-14-12-double-double-in-loss); [Digest Sports box score, 25 Nov](https://digestsports.com/nba/games/clippers-vs-grizzlies-2026-11-25/)). He was not on that night's report ([NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf)). His L7 of 34.2 (4 games) is 8.4 over his season 25.9. He has kept 29 to 37 min as a starter since Ingram's debut, with efficient shooting up to Wednesday and the rebounds on Wednesday.
  - **Verdict:** nothing new found on rest. He is a starter at about 29 to 37 min, with no back-to-back this week and no rest pattern.

### Rudy Gobert (MIN, C, free agent)

- Rate **27.7** · season 26.3 (18) · L7 28.5 (4) · L15 25.5 (8) · L30 26.9 (15) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (21 Nov): Gobert accumulated seven points (2-2 FG, 3-4 FT), 11 rebounds, two assists, three blocks and one steal over 32 minutes during Saturday's 104-95 victory over the Grizzlies.
- News (20 Nov): Gobert posted nine points (4-6 FG, 1-2 FT), seven rebounds and two steals over 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:**
  - Rest: unchanged since 24 Nov. Minnesota has no back-to-back in our week (Fri 27 vs MEM, Sun 29 @SAC). The flagged one is Tue 1 Dec @POR and Wed 2 Dec @LAC, and no sit has been announced. His 31 Oct absence was low back spasms, not rest ([NBA injury report, 31 Oct 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-31_06_00PM.pdf)). He played both nights of 16–17 Nov.
  - Wed 25 @OKC: started and played 32 min (19 FP) in a 113-106 win. He was not on the injury report ([ESPN box, 25 Nov](https://www.espn.com/nba/game/_/gameId/401909320/timberwolves-thunder); [NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf)).
  - **Verdict:** nothing new found. Healthy for Fri 27 and Sun 29. He has no rest pattern, and 1–2 Dec falls outside this week.

### Zach Edey (MEM, C, free agent)

- Rate **25.7** · season 24.9 (15) · L7 24.5 (4) · L15 25.7 (6) · L30 23.5 (13) · projected 33.2
- ESPN: day-to-day, ESPN est. 27 Nov (Left Ankle Soreness, updated 2026-11-26)
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the first night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (25 Nov): Edey (ankle) did not return to Wednesday's 115-97 win over the Clippers. He finished with seven points (3-4 FG, 1-1 FT), four rebounds, two assists and two blocks across nine minutes.
- News (25 Nov): Edey (ankle) is doubtful to return to Wednesday's game against the Clippers.
- **Research:**
  - New injury: he left Wed 25 vs LAC after 9 min with left ankle soreness and did not return. Iisalo said Edey "relayed that message" at halftime and the staff shut him down. No imaging or Friday status was given ([Commercial Appeal via Yahoo, 26 Nov](https://sports.yahoo.com/nba/articles/grizzlies-said-zach-edeys-injury-043856207.html)). RotoWire expects a cautious approach for Fri 27 @MIN ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-not-expected-to-return-wednesday/)). Memphis had not yet filed Friday's report as of 26 Nov 1:00 AM ET ([NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf)). This is the ankle he has had surgery on twice (June 2025, March 2026).
  - Rest: unchanged since 24 Nov. Memphis has no back-to-back in our week (Fri 27 @MIN, Sun 29 vs LAL). He sat one night of each earlier back-to-back for "left ankle injury management" ([NBA injury report, 19 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)), so expect one missed night on 1–2 Dec. Iisalo is holding him to 25 min or fewer to "preserve his future" ([Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/grizzlies-notes-boozer-edey-lineups-jerome.html)). His rate already reflects 21–23 min.
  - **Expected return:** no timetable reported. He is day-to-day, and Fri 27 @MIN is undecided. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. Day-to-day matches the news, but Fri 27 is a real risk given the ankle history, and Sun 29 is safer.

### T.J. McConnell (IND, PG, free agent)

- Rate **21.6** · season 20.0 (7) · L7 20.0 (2) · L15 24.6 (5) · L30 20.0 (7) · projected 24.4
- ESPN: day-to-day, ESPN est. 27 Nov (Left Hamstring, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "The veteran floor general is missing both ends of this back-to-back set, but he'll have some extra time to heal up ahead of Friday's tilt against the 76ers."
- News (24 Nov): McConnell (hamstring) was recalled from the G League's Noblesville Boom on Tuesday, Shams Charania of ESPN reports.
- News (24 Nov): McConnell (hamstring) was assigned to the G League's Noblesville Boom on Tuesday.
- **Research:**
  - Hamstring/rest: he practised with the Noblesville Boom on Tue 24 Nov and was recalled the same day ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-recalled-to-nba/)). Indy Cornrows lists him questionable and writes that "it appears he may be ready to go in at least one of the back-to-back games this weekend" ([Indy Cornrows, 25 Nov](https://www.indycornrows.com/p/pacers-quiet-thunder-face-sixers)). No sit has been announced for Fri 27 vs PHI or Sat 28 @CHI. Indiana had not filed Friday's report as of 26 Nov 1:00 AM ET.
  - Role risk: Haliburton practised with the Pacers on Wed 25, and "indications point toward a return on Friday or Saturday" (same source). That would cut McConnell's backup minutes, which were 11 to 19. His L7 of 20.0 rests on 2 games (small sample).
  - **Expected return:** no timetable reported. He is questionable for Fri 27 vs PHI and may play only one night of Fri 27–Sat 28. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. Friday is plausible, but expect him to miss one night of the back-to-back.

### Julian Reese (NO, PF, free agent)

- Rate **8.0** · season 4.3 (6) · L7 — · L15 6.0 (3) · L30 4.3 (6)
- ESPN: day-to-day, ESPN est. 25 Nov (Right Knee, updated 2026-11-25)
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (16 Nov): The Pelicans transferred Reese from the G League's Laketown Squadron, and he will be available for New Orleans' game against the Warriors on Monday.
- News (24 Sep): Reese agreed to a two-way contract with the Pelicans on Thursday, Keith Smith of Spotrac.com reports.
- **Research:**
  - Injury: he sat out the Laketown Squadron's G League game on Tue 24 Nov with a right knee contusion. RotoWire says it "may not" mean a long absence ([RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/julian-reese-injury-sidelined-due-to-injury-540924)). He is on a two-way deal and was listed Out "G League - Two-Way" on 23 Nov ([NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf)).
  - Rest: the flag is not rest. On 14 Nov, the second night, he was listed Available and simply did not play ([NBA injury report, 14 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-14_06_00PM.pdf)). His NBA minutes have been 3–9 a game, so there is no fantasy role to protect on Sun 29–Mon 30.
  - **Expected return:** no timetable reported (minor knee contusion, mostly with the G League). *ESPN est.* 25 Nov.
  - **Verdict:** nothing new found. Fringe two-way big with no rest pattern. Not a streaming option.

### Ja Morant (POR, PG, free agent)

- Rate **31.2** · season 33.8 (4) · L7 — · L15 — · L30 28.0 (2) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:**
  - Gap: still out. He was listed Out (left hamstring strain) for Wed 25 vs SAS ([NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf)). New on 25 Nov, Nori: "He's starting to participate a little bit in the 5-on-5 stuff … I'll go out on a limb and say we'll see him on this home stand … He is getting close." The home stand runs Fri 27 GSW, Sun 29 NOP, Tue 1 Dec MIN and Thu 3 Dec ([Blazer's Edge, 25 Nov](https://www.blazersedge.com/trail-blazers-news/118895/portland-trail-blazers-ja-morant-nba-injury-news-return-micah-nori-spurs-grizzlies)).
  - The four-week re-evaluation from 30 Oct falls on Fri 27 Nov ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). No game has been named, and no result has been reported yet.
  - **Expected return:** Nori expects him back by Thu 3 Dec. His first possible game is Sun 29 vs NOP after the 27 Nov re-evaluation, but that date is unconfirmed, and Tue 1 Dec vs MIN is at least as likely. *ESPN est.* 1 Dec. His L30 of 28.0 rests on 2 games (small sample).
  - **Verdict:** ESPN corrected, as before. The re-evaluation rule keeps the 28 Nov floor, and Nori's 5-on-5 news supports a return within the week. Keep the existing row with a refreshed note and the new source. Do not add it twice.

Summary:
- Edey is now day-to-day (left ankle soreness, left Wed 25 after 9 min; ESPN est. 27 Nov). Fri 27 @MIN is undecided, and Memphis tends to be cautious with that ankle.
- McConnell (ESPN est. 27 Nov) is questionable for Fri 27 and likely plays only one night of Fri 27–Sat 28. Haliburton's possible return Fri/Sat would cut his minutes. Gobert is healthy, and Reese's flag is not rest.
- Morant (ESPN est. 1 Dec) is doing 5-on-5 work, and Nori expects him back during the home stand that ends Thu 3 Dec. The 28 Nov return row stays as a floor with a refreshed note. Sun 29 vs NOP is possible but unconfirmed.
  - Override proposed: return 2026-11-28

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 03 Dec (Left Calf Strain, updated 2026-11-16)
- **Gap:** listed out, and no news in 5 days (ESPN est. 03 Dec)
- News (16 Nov): Harris (calf) is likely to be sidelined until early December, per Jeff Garcia of KENS 5 San Antonio.
- News (10 Nov): Harris (calf) is out for Wednesday's game against Chicago, Jared Weiss of The Athletic reports.
- **Research:**
  - Gap: still out. He was listed Out (left calf strain) for Wed 25 at POR ([NBA injury report, 25 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_07_00PM.pdf)). There has been no update since Mitch Johnson was asked on 18 Nov about a return before Christmas: "For his sake, I hope so ... whenever he comes back, it'll be later than he wanted" ([Hoops Rumors citing Express-News, 18 Nov](https://www.hoopsrumors.com/2026/11/southwest-notes-harper-harris-johnson-sengun.html)). Haynes reported an early-December debut target ([ClutchPoints, 14 Nov](https://clutchpoints.com/nba/san-antonio-spurs/spurs-news-tobias-harris-gets-crucial-injury-update-after-warriors-game)). SA plays Fri 27 vs LAL and Sun 29 vs BOS this week.
  - **Expected return:** early December at the earliest (Haynes), with no date from the team. *ESPN est.* 3 Dec, which looks optimistic given Johnson's comments.
  - **Verdict:** ESPN confirmed as the earliest reported target, and unchanged since 25 Nov. No row: the 7-day rule (2 Dec) would come earlier than the reporting.

## Opponents: this week and next

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Injury/gap: unchanged since 25 Nov. The most recent official listing is still Out on Tue 24 Nov vs DET with the right high ankle sprain ([NBA injury report, 24 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_05_30PM.pdf)). Sweeney's "No timeline right now" still stands. He has been doing on-court shooting and pool work, and the Magic say he is "still likely a few weeks away" ([Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4)). His own target is "within the next couple of weeks" ([RealGM, 19 Nov](https://basketball.realgm.com/wiretap/288198/Paolo-Banchero-Hopes-To-Return-Within-Next-Couple-Of-Weeks)). Nothing newer was found. Pages that give "29 Nov at DET" are repeating ESPN's estimate. ORL's Sat 28 at WAS report had not been submitted as of 26 Nov 1:15 AM ET.
  - **Expected return:** no timetable reported. The 1 Dec floor stands, so Wed 2 Dec is his first possible game. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN corrected (unchanged since 25 Nov). The team has given no date, and the 29 Nov estimate would mean he returns on the second night of a back-to-back.
  - Override proposed: return 2026-12-01

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **34.4** · season 39.9 (12) · L7 — · L15 26.0 (1) · L30 38.6 (10) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:**
  - Injury/gap: still out. The official report listed him Out (left great toe sprain) for Wed 25 at NYK ([NBA injury report, 25 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_07_00PM.pdf)). That was his seventh straight missed game, and CLE lost 121-102 ([Hoops Wire via Yardbarker, 25 Nov](https://www.yardbarker.com/nba/articles/cavs_looking_an_awful_lot_like_the_team_we_thought_theyd_outgrow/s1_17038_44620752)). The team's 16 Nov plan of 7–10 days of rehab before a re-evaluation ran to 26 Nov. No re-evaluation result or practice report has appeared ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)).
  - Atkinson: "we don't expect it to be a long-term thing at all" ([Yahoo, 14 Nov](https://sports.yahoo.com/articles/cavs-kenny-atkinson-gives-injury-011755667.html)). CLE's next and only game this week is Sun 29 vs MIA (3:30 PM ET), and its report for that game is not out yet. His L15 of 26.0 (1) is a small sample.
  - **Expected return:** re-evaluation due by 26 Nov, with no result reported. Sun 29 vs MIA is his first possible game. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. Unchanged since 25 Nov apart from the seventh missed game. No row: the day after the re-evaluation window (27 Nov) falls before CLE's next game.

### Josh Hart (NY, SG/SF, Dr White Slong)

- Rate **29.5** · role rate 32.5 · season 27.5 (15) · L7 35.5 (4) · L15 24.9 (8) · L30 25.4 (12) · projected 33.0
- ESPN: active
- **Minutes:** 36.7 min over his last 3 games against 31.1 for the season (+5.6)
- News (25 Nov): Hart compiled 15 points (6-14 FG, 1-5 3Pt, 2-3 FT), seven rebounds, 11 assists, three steals and one block in 36 minutes during Wednesday's 121-102 win over Cleveland.
- News (25 Nov): Hart (shoulder) is available for Wednesday's game against the Cavaliers, Steve Popper of Newsday reports.
- **Research:**
  - Minutes: the jump lines up with OG Anunoby's absence. Anunoby has a left calf strain and has missed three straight games (21, 22 and 25 Nov), and Hart played 35, 39 and 36 minutes in them, against 28–31 before. On Wed 25 vs CLE he had 15 pts, 7 reb, 11–12 ast, 3 stl in 36 minutes. He played through a right shoulder sprain that had him listed Probable that afternoon ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf); [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/josh-hart-records-15-7-12-3-2-line-vs-cavaliers)).
  - Anunoby has moved up to individual on-court work and is "considered day-to-day" (Brown via NY Post, [Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/knicks-announce-major-og-anunoby-024000614.html)). His return should bring Hart back toward about 31 minutes. Hart's L7 of 35.5 (4 games) is 8 FP/g over his season average: more minutes and 21 assists across his last two games.
  - **Verdict:** nothing new found on ESPN's label (active). The boost is real while Anunoby is out, but Anunoby is day-to-day, so the role is not reported as ongoing and there is no role row. Watch the shoulder on the Fri 27 vs MIA report.

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **47.5** · season 39.4 (14) · L7 59.5 (2) · L15 44.4 (5) · L30 37.5 (11) · projected 45.4
- ESPN: day-to-day, ESPN est. 27 Nov (Illness, updated 2026-11-26)
- **Rest:** back-to-back Fri 27–Sat 28 Nov, Tue 01–Wed 02 Dec; sat the second night of the 24–25 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side; sat the first night of the 15–16 Nov back-to-back, playing the games either side
- News (25 Nov): Embiid (illness) is out for Wednesday's game against Miami, Ira Winderman of the South Florida Sun Sentinel reports.
- News (24 Nov): Embiid (illness) is listed as doubtful for Wednesday's game versus Miami.
- **Research:**
  - Illness: he was Out Wed 25 vs MIA, his second straight miss ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf)). Nurse: "He's ill. I do not know whether he's going to Indiana yet... we'll find that out late tomorrow afternoon" ([Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/76ers-nick-nurse-cryptic-joel-223852806.html); [NBC Sports Philadelphia, 25 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-heat-nba-cup-live-updates-joel-embiid-lebron-james-tyrese-maxey/769428/)). A FanDuel item lists him "out" for Fri 27, but it is automated (Data Skrive), names no source, and appeared before PHI submitted its Fri 27 report, which was still "not yet submitted" at 26 Nov 1:15 AM ET. Do not rely on it.
  - Rest: no change. Yahoo's writer expects him to miss one of Fri 27 at IND and Sat 28 at HOU because of plantar fascia management ([Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/article/joel-embiid-listed-as-doubtful-for-76ers-nba-cup-matchup-vs-miami-heat-on-wednesday-due-to-illness-225037585.html)). He has sat one leg of all three back-to-backs so far. Nothing has been said about Tue 1 / Wed 2 Dec.
  - **Expected return:** day-to-day (illness), no timetable reported. Travel for Fri 27 is undecided and an update is due Thursday afternoon ET. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed, at risk. 27 Nov is still possible, but between the illness and the back-to-back pattern he is a strong risk to miss Fri 27, Sat 28 or both. With no team statement yet, there is no row.

### Amen Thompson (HOU, SG/SF, Matt Wright's Foxies)

- Rate **39.3** · season 37.5 (18) · L7 39.0 (4) · L15 42.4 (7) · L30 35.2 (15) · projected 40.0
- ESPN: active
- **Rest:** back-to-back Mon 30–Tue 01 Dec; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (24 Nov): Thompson ended Monday's 116-104 victory over the Clippers with 20 points (9-12 FG, 1-1 3Pt, 1-2 FT), four rebounds, five assists and one block over 28 minutes.
- News (21 Nov): Thompson chipped in 22 points (10-12 FG, 0-1 3Pt, 2-6 FT), six rebounds and one steal in 26 minutes during Friday's 133-124 loss to the Nuggets.
- **Research:**
  - Rest: healthy. He played 36 min Wed 25 vs PHX (18 pts, 10 reb, 4 ast, 2 blk; 44 FP) without an injury listing ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/amen-thompson-notches-double-double-in-win); [NBA injury report, 25 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_07_00PM.pdf)). HOU's only game this week is Sat 28 vs PHI. The flagged back-to-back, Mon 30 vs LAL and Tue 1 Dec vs TOR, is next week.
  - His only second-night absence (16 Nov) was for left knee soreness, not rest ([ClutchPoints, 16 Nov](https://clutchpoints.com/nba/houston-rockets/rockets-news-amen-thompson-out-heat-game-concerning-injury-update)). He played both nights of the 23–24 Oct and 30–31 Oct back-to-backs. That is no rest pattern, and no rest has been announced for 30 Nov–1 Dec.
  - **Verdict:** ESPN confirmed. Healthy, with no rest risk this matchup week.

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **39.0** · season 39.1 (17) · L7 39.2 (4) · L15 37.6 (7) · L30 39.8 (14) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "After carrying a questionable tag ahead of both parts of this back-to-back, Siakam is suiting up Monday despite dealing with a left hip injury."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Siakam (hip) will play in Monday's game against the Thunder, Justin Martinez of The Oklahoman reports.
- News (23 Nov): Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management.
- **Research:**
  - Rest (Fri 27 vs PHI, Sat 28 at CHI): unchanged since 25 Nov, with no sit announced. IND did not play Wed. Its Friday injury report was still "not yet submitted" at 1:15 AM ET on 26 Nov ([NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)). He played 35 min Mon 23 vs OKC through a left hip "injury management" tag, with no setback since ([NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf); [Heavy, 23 Nov](https://heavy.com/sports/nba/indiana-pacers/pascal-siakam-injury-thunder/)). He played both nights of 22–23 Nov and 25–26 Oct. His only second-night absence was 2 Nov.
  - Haliburton (left hamstring strain) practiced fully Wed 25, the day after a G League workout. Carlisle said only "stay tuned" about Fri/Sat. Haliburton wants to be back by next week "at the absolute latest" ([IndyStar via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/tyrese-haliburton-provided-good-news-201537475.html); [FantasyPros, 25 Nov](https://www.fantasypros.com/nba/news/622472/tyrese-haliburton-hamstring-could-return-before-end-november.php)). His return would take shots from Siakam, not minutes.
  - **Verdict:** ESPN confirmed. Active. The hip makes Sat 28 a risk, but no source says he will sit.

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **29.1** · season 31.8 (14) · L7 26.7 (3) · L15 27.2 (5) · L30 31.9 (11) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Nembhard produced 16 points (5-13 FG, 2-3 3Pt, 4-7 FT), two rebounds and eight assists in 32 minutes during Sunday's 113-106 loss to the Knicks.
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- **Research:**
  - Rest: unchanged since 25 Nov. He is not on any injury report and played both nights of 22–23 Nov, 32 and 38 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038)). Both of his earlier second-night absences (back on 26 Oct, cervical on 2 Nov) were filed as injuries. No sit is announced for Fri 27 or Sat 28, and IND's Friday report is not yet submitted ([NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)).
  - Role: his lead-guard role is at risk this weekend. Haliburton (no timetable reported, *ESPN est.* 13 Dec) practiced fully Wed 25 and could return Fri or Sat. He says the team has "a plan ... of how we're gonna approach back-to-backs" when he returns ([IndyStar via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/tyrese-haliburton-provided-good-news-201537475.html)). McConnell (left hamstring; no timetable reported, *ESPN est.* 27 Nov) also practiced and is questionable ([Indy Cornrows via BVM Sports, 25 Nov](https://bvmsports.com/2026/11/25/pacers-hold-off-thunder-as-haliburton-nears-return-face-76ers/)). Either return would cut into his assists.
  - His L7 of 26.7 (3) is 5.1 under his 31.8 season average. He played only 26 min in his 20 Nov return from the hip and committed 6 turnovers on 22 Nov.
  - **Verdict:** nothing new found on rest. Haliburton's possible return is the risk to his role.

### Derrick White (BOS, PG/SG, Dr White Slong)

- Rate **28.1** · season 29.5 (17) · L7 25.7 (3) · L15 27.1 (7) · L30 29.0 (15) · projected 37.0
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the first night of the 21–22 Nov back-to-back, playing the games either side
- News (25 Nov): White notched six points (2-10 FG, 2-6 3Pt), seven rebounds, five assists and one steal across 30 minutes during Tuesday's 131-116 victory over Washington.
- News (23 Nov): White amassed 14 points (6-21 FG, 2-12 3Pt), three rebounds, five assists and one steal over 32 minutes during Sunday's 88-87 loss to the Warriors.
- **Research:**
  - Rest: unchanged since 25 Nov. His only miss, on 21 Nov, was the left AC joint sprain, not rest ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/derrick-white-shoulder-off-injury-report-vs-gsw)). He played both nights of BOS's other back-to-backs. He played 30 minutes on Tue 24 and has not been on an injury report since ([NBA injury report, 24 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_05_30PM.pdf)). No sit has been reported for Sun 29 / Mon 30 Nov.
  - **Verdict:** nothing new found. His rest risk for 29–30 Nov is low.

### Jonathan Kuminga (MIN, SF/PF, Dr White Slong)

- Rate **26.3** · season 27.9 (18) · L7 26.5 (4) · L15 25.9 (7) · L30 26.7 (15) · projected 26.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 16–17 Nov back-to-back, playing the games either side
- News (24 Nov): Kuminga contributed 15 points (5-12 FG, 1-5 3Pt, 4-6 FT), five rebounds, four assists and one steal in 26 minutes during Monday's 142-116 win over the Nets.
- News (19 Nov): Kuminga totaled 23 points (7-13 FG, 2-4 3Pt, 7-7 FT), three rebounds, three assists and three blocks in 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:**
  - Rest: he was not on MIN's report for Wed 25 at OKC ([NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf)) and played 32 minutes (14 FP). He is still starting with Anthony Edwards out after knee surgery. His only back-to-back miss, on 17 Nov, was the right shoulder contusion, not rest ([Roundtable, 17 Nov](https://roundtable.io/sports/nba/timberwolves/news/key-starter-ruled-out-for-timberwolves-against-blazers)). Nothing has been said about Tue 1 / Wed 2 Dec.
  - **Verdict:** nothing new found (unchanged since 25 Nov). His rest risk for 1–2 Dec is low.

**Summary**
- Embiid: Out Wed 25 with the illness (second straight). Nurse doesn't know if he travels to IND, with an update due Thu afternoon ET (*ESPN est.* 27 Nov). He is a strong risk to miss Fri 27 and/or Sat 28, but there is no sit row without a team statement.
- Hart: 36.7 minutes over three games with Anunoby (calf strain, day-to-day, no timetable) out. He is a better start while Anunoby sits, but there is no role row because Anunoby could return any day.
- Banchero: no news since 24 Nov, and the 1 Dec floor row stands (first possible game Wed 2 Dec; *ESPN est.* 29 Nov). White and Kuminga: nothing new, low rest risk.

## Other rosters: injury flags only

### Jalen Brunson (NY, PG, Melbourne poopoo)

- Rate **39.9** · season 40.5 (18) · L7 36.0 (4) · L15 41.6 (9) · L30 42.7 (15) · projected 43.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 25 Nov: "Brunson (illness) has been downgraded to questionable for Wednesday's game against the Cavaliers."
- News (25 Nov): Brunson finished with 19 points (6-22 FG, 2-8 3Pt, 5-6 FT), three rebounds and five assists over 36 minutes during Wednesday's 121-102 victory over the Cavaliers.
- News (25 Nov): Brunson (illness) is available for Wednesday's game against the Cavaliers, Ian Begley of SportsNet New York reports.
- **Research:**
  - Injury (illness): a late addition to Wednesday's report, he was downgraded to questionable ([CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-now-questionable-for-wednesday/)), then upgraded to probable ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jalen-brunson-illness-probable-wednesday-vs-cavs)) and cleared to play, per SNY's Ian Begley ([CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-available-to-play-wednesday/)). The official NBA report listed him "Available – Illness" from 8:00 PM ET to the last slot ([NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf)).
  - He played 36 minutes in the 121-102 win over Cleveland: 19 points on 6-22 FG, 5 assists, 20 FP, his worst shooting game of the season ([Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/knicks-blow-cavaliers-fourth-win-031145067.html)). The illness did not cost him minutes. No postgame update on it was found.
  - Next game: Fri 27 Nov vs MIA, 7:00 PM ET, at MSG, the Knicks' last NBA Cup group game ([TickPick listing](https://www.tickpick.com/buy-nba-cup-new-york-knicks-vs-miami-heat-tickets-madison-square-garden-11-27-26-7pm/8200050/)). The Thursday 26 Nov ET injury reports for Friday's games are not out yet (403). There is no sign he will miss Friday, and Thanksgiving gives him a day off to recover.
  - **Expected return:** not out. He played through the illness on 25 Nov and is expected to play Fri 27 Nov. ESPN lists him active and he is not in ESPN's injury feed, so there is no *ESPN est.*
  - **Verdict:** ESPN confirmed. He played 36 minutes through the illness, and no source has him doubtful for Friday.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-26 06:13 UTC.
- **Research links:** [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html) · [NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week) · [AP via TSN, 25 Nov](https://www.tsn.ca/nba/article/porter-jr-signs-with-magic-after-getting-waived-by-bucks-before-season/) · [Kings On SI, 25 Nov](https://www.si.com/nba/kings/onsi/kings-maxime-raynaud-gets-promising-injury-update-after-17-game-absence) · [IndyStar via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/tyrese-haliburton-provided-good-news-201537475.html) · [Blazer's Edge, 25 Nov](https://www.blazersedge.com/trail-blazers-news/118895/portland-trail-blazers-ja-morant-nba-injury-news-return-micah-nori-spurs-grizzlies) · [link](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) · [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf) · [link](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_03_30AM.pdf) · [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/daniss-jenkins-dishes-out-10-assists-vs-orlando) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_05_30PM.pdf) · [link](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) · [AP via NBA.com, 25 Nov](https://www.nba.com/news/jalen-duren-hamstring-practices-with-pistons-ahead-of-rehab-stint) · [Free Press via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/cade-cunningham-injury-dulls-hope-101021863.html) · [ClutchPoints, 24 Nov](https://clutchpoints.com/nba/detroit-pistons/pistons-news-jalen-duren-g-league-move) · [NBA injury report, 26 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_00AM.pdf) · [CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/) · [BasketballNews, 25 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-hes-fighting-through-a-lot-all-star-candidate-cade-cunninghams-injury-update-sparks-concern/) · [Yahoo Sports player ratings, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-player-ratings-tatum-drops-051608071.html) · [Sports Mole, 25 Nov](https://www.sportsmole.co.uk/basketball/boston-celtics/preview/atlanta-hawks-vs-boston-celtics-player-props-injury-report-and-prediction--nba-cup_609820.html) · [NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf) · [CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-returning-to-starting-five/) · [Yahoo/HoopsHype, 21 Nov](https://sports.yahoo.com/articles/pelicans-rest-trey-murphy-against-182359369.html) · [CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-low-usage-continues-monday/) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322) · [NBA injury report, 25 Nov 8:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_08_30PM.pdf) · [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/myles-turner-rest-ruled-out-vs-los-angeles) · [NBA injury report, 19 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf) · [Orlando Sentinel via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/magic-finalizing-deal-free-agent-190200324.html) · [NBC Sports via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/kevin-porter-jr-reportedly-sign-204545897.html) · [Yahoo, 18 Nov](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html) · [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/) · [NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf) · [Statz, 23 Nov](https://statz.ai/nba/news/jusuf-nurkic-injury-update) · [Roundtable, 26 Nov](https://roundtable.io/sports/nba/bulls/game-day/bulls-close-out-nba-cup-slate-with-road-win-against-charlotte-hornets) · [Bulls/NBA.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update) · [Hoops Rumors, 22 Nov](https://www.hoopsrumors.com/2026/11/bulls-norman-powell-suffers-mild-right-hamstring-strain.html) · [Hoops Rumors, 16 Mar 2025](https://www.hoopsrumors.com/2025/03/clippers-norman-powell-returning-from-hamstring-injury.html) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-reaves-redick-reynaud-green.html) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-recalled-to-nba-540983/) · [Bleacher Report, 22 Nov](https://bleacherreport.com/articles/25536410-dejounte-murray-hasnt-been-pelicans-arena-trade-request-latest-nba-rumors-suns-talks) · [BasketballNews, 23 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-absolutely-untrue-suns-insider-john-gambadoro-dismisses-dejounte-murray-update-amid-trade-rumor/) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/) · [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/saddiq-bey-scores-21-points-off-bench-in-loss) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324) · [SI, 25 Nov](https://www.si.com/nba/warriors/onsi/takeaways-from-warriors-win-over-kings-why-acuff-lendeborg-have-intriguing-roy-race-01m8b12gmrh7) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-stephen-curry-to-be-re-evaluated-friday/) · [CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-kenrich-williams-starting-versus-heat/) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910030) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/thunder-start-shai-stirtz-ajay-peavy-i-hart) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320) · [Yahoo, 24 Nov](https://sports.yahoo.com/articles/mark-daigneault-provides-nba-injury-190008603.html) · [NBA injury report, 25 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_05_30PM.pdf) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-wednesday/) · [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318) · [Dallas Sports Journal, 25 Nov](https://dallassportsjournal.com/pj-washington-bench-return-dusty-may-mavericks-nuggets/) · [Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/p-j-washington-return-shows-182629902.html) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/p-j-washington-illness-scores-14-in-return) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/kings-start-acuff-sharp-hunter-murray-sabonis) · [Anthony Slater, 25 Nov](https://x.com/anthonyVslater/status/2125723596157026468) · [NBA injury report, 20 Nov 1:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_01_00PM.pdf) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039) · [CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-manning-bench-role-in-return/) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes) · [NBA injury report, 25 Nov 11:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_30PM.pdf) · [Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update) · [ESPN, 12 Nov](https://www.espn.com/nba/story/_/id/50464091/sources-bulls-wilson-surgery-hand-4-6-weeks) · [AP via WXYZ, 17 Nov](https://www.wxyz.com/sports/basketball/pistons/cunningham-jenkins-lead-surge-as-pistons-snap-spurs-12-game-winning-streak-with-105-93-victory) · [Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/news/nba-week-6-injury-report-cameron-boozer-to-miss-at-least-four-weeks-dont-panic-on-cade-cunningham) · [Dallas Morning News via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/5-thoughts-mavericks-nuggets-dallas-054348956.html) · [ESPN box score, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-dereck-lively-progressing-in-recovery/) · [Indy Cornrows, 25 Nov](https://www.indycornrows.com/p/pacers-quiet-thunder-face-sixers) · [NBA injury report, 2 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_08_00PM.pdf) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/rui-hachimura-records-14-12-double-double-in-loss) · [Digest Sports box score, 25 Nov](https://digestsports.com/nba/games/clippers-vs-grizzlies-2026-11-25/) · [NBA injury report, 31 Oct 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-31_06_00PM.pdf) · [ESPN box, 25 Nov](https://www.espn.com/nba/game/_/gameId/401909320/timberwolves-thunder) · [Commercial Appeal via Yahoo, 26 Nov](https://sports.yahoo.com/nba/articles/grizzlies-said-zach-edeys-injury-043856207.html) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-not-expected-to-return-wednesday/) · [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/grizzlies-notes-boozer-edey-lineups-jerome.html) · [CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-recalled-to-nba/) · [RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/julian-reese-injury-sidelined-due-to-injury-540924) · [NBA injury report, 23 Nov 5:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_05_00PM.pdf) · [NBA injury report, 14 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-14_06_00PM.pdf) · [NBA injury report, 25 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_07_00PM.pdf) · [Hoops Rumors citing Express-News, 18 Nov](https://www.hoopsrumors.com/2026/11/southwest-notes-harper-harris-johnson-sengun.html) · [ClutchPoints, 14 Nov](https://clutchpoints.com/nba/san-antonio-spurs/spurs-news-tobias-harris-gets-crucial-injury-update-after-warriors-game) · [Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4) · [RealGM, 19 Nov](https://basketball.realgm.com/wiretap/288198/Paolo-Banchero-Hopes-To-Return-Within-Next-Couple-Of-Weeks) · [Hoops Wire via Yardbarker, 25 Nov](https://www.yardbarker.com/nba/articles/cavs_looking_an_awful_lot_like_the_team_we_thought_theyd_outgrow/s1_17038_44620752) · [Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116) · [Yahoo, 14 Nov](https://sports.yahoo.com/articles/cavs-kenny-atkinson-gives-injury-011755667.html) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/josh-hart-records-15-7-12-3-2-line-vs-cavaliers) · [Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/knicks-announce-major-og-anunoby-024000614.html) · [Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/76ers-nick-nurse-cryptic-joel-223852806.html) · [NBC Sports Philadelphia, 25 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-heat-nba-cup-live-updates-joel-embiid-lebron-james-tyrese-maxey/769428/) · [Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/article/joel-embiid-listed-as-doubtful-for-76ers-nba-cup-matchup-vs-miami-heat-on-wednesday-due-to-illness-225037585.html) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/amen-thompson-notches-double-double-in-win) · [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/houston-rockets/rockets-news-amen-thompson-out-heat-game-concerning-injury-update) · [Heavy, 23 Nov](https://heavy.com/sports/nba/indiana-pacers/pascal-siakam-injury-thunder/) · [FantasyPros, 25 Nov](https://www.fantasypros.com/nba/news/622472/tyrese-haliburton-hamstring-could-return-before-end-november.php) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038) · [Indy Cornrows via BVM Sports, 25 Nov](https://bvmsports.com/2026/11/25/pacers-hold-off-thunder-as-haliburton-nears-return-face-76ers/) · [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/derrick-white-shoulder-off-injury-report-vs-gsw) · [Roundtable, 17 Nov](https://roundtable.io/sports/nba/timberwolves/news/key-starter-ruled-out-for-timberwolves-against-blazers) · [CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-now-questionable-for-wednesday/) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jalen-brunson-illness-probable-wednesday-vs-cavs) · [CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-available-to-play-wednesday/) · [Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/knicks-blow-cavaliers-fourth-win-031145067.html) · [TickPick listing](https://www.tickpick.com/buy-nba-cup-new-york-knicks-vs-miami-heat-tickets-madison-square-garden-11-27-26-7pm/8200050/)
