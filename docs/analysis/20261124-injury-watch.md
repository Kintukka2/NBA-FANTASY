# Injury Watch: 24 Nov 2026

- Generated 2026-11-24 07:07 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 92 players in ESPN's injury feed. 33 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1102 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (23 Nov–29 Nov) / next week (30 Nov–06 Dec).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

These five pickups' gains should last through Sun 29 Nov. Monday 23 Nov games are final, and no NBA team plays Thu 26. The next add deadlines (each US day's first tip-off, Melbourne time) are: Tue 24 by **Wed 25 Nov 11:00 AM** (DET@ORL), Wed 25 by **Thu 26 Nov 9:00 AM** (MIA@PHI), Fri 27 by **Sat 28 Nov 11:00 AM** (MIA@NY), Sat 28 by **Sun 29 Nov 9:00 AM** (ORL@WSH) and Sun 29 by **Mon 30 Nov 7:30 AM** (MIA@CLE) ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124)). The Rates come from `council/form.py` (24 Nov 07:11 UTC). Our five-lowest floor is **31.1**.

- **De'Andre Hunter** (SAC, free agent, 15%):
  - **Opening:** Ben Simmons tore his right Achilles, which ends his season ([AP via NY1, 18 Oct](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/18/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice)); *ESPN est.* 1 Oct, a stale date. Maxime Raynaud was out again Mon vs SA ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)) and is still week-to-week with no timeline ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)); *ESPN est.* 25 Nov.
  - **Window:** reported, the rest of the season for Simmons ([AP via NY1, 18 Oct](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/18/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice)). Raynaud's return (no timeline, [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/); *ESPN est.* 25 Nov) is the only risk to Hunter's minutes.
  - **Numbers:** FP/g without the absentees 30.5 (8 g, 37.0 min). Season 25.6 (15), L7 36.5 (4), L15 32.7 (7), L30 27.8 (13). **Rate 31.3**, the only healthy one here above our 31.1 floor; ESPN proj. 23.9. Minutes 33.9 for the season, 37.8 over L7. ([Injury Watch, 24 Nov](20261124-injury-watch.md); Rate from `form.py`, 24 Nov)
  - **Monday:** started and had 15 pts (7-12 FG), 7 reb and 8 ast in 38 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045); [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/deandre-hunter-dishes-out-eight-assists-vs-spurs)).
  - **Games:** 2 (Wed @GS, Sun vs MIN). For Wednesday, add by Thu 26 Nov 9:00 AM Melbourne. ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124))
- **Jakob Poeltl** (TOR, free agent, 38%):
  - **Opening:**
    - Kawhi Leonard (us) was out Mon. He did shooting work Sunday but must scrimmage with teammates before he returns ([Roundtable via Yahoo, 23 Nov](https://sports.yahoo.com/articles/darko-rajakovic-gives-raptors-forward-194758381.html)). He is out at least two more weeks from 20 Nov, so to about 4 Dec ([TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/)); *ESPN est.* 3 Dec.
    - RJ Barrett was out Mon ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)), with a re-evaluation about 3 Dec ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks)); *ESPN est.* 13 Dec.
  - **Window:** both absentees miss the rest of this week: Leonard about 4 Dec ([TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/); *ESPN est.* 3 Dec), Barrett's re-evaluation about 3 Dec ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks); *ESPN est.* 13 Dec).
  - **Role:** the starting C since Barrett's injury: starts on 18, 20 and 23 Nov. Monday he had 15 pts, 10 reb and 3 ast in 28 min before fouling out ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
    - **Risk:** on 17 Nov, with Barrett healthy, Toronto started Collin Murray-Boyles at C and brought Poeltl off the bench for 18 min ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002)). Rotoworld thinks this week's four days off "may be enough time to get Murray-Boyles back into the starting lineup" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)). If he does start, Graves or Poeltl goes to the bench.
  - **Numbers:** FP/g without the absentees 38.7 (3 g, 29.7 min). Season 27.4 (15), L7 32.5 (4), L15 31.1 (8), L30 28.2 (13). Rate 30.5; ESPN proj. 31.7. Minutes 24.2 for the season, 26.8 over L7. ([Injury Watch, 24 Nov](20261124-injury-watch.md); Rate from `form.py`, 24 Nov)
  - **Games:** 2 (Fri vs BKN, Sun vs DEN). For Friday, add by Sat 28 Nov 11:00 AM Melbourne. ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124))
- **Ja'Kobe Walter** (TOR, free agent, 13%):
  - **Opening:** the same as Poeltl's. Walter started 17 Nov in Leonard's place while Barrett was still healthy ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002)), and has started every game since Barrett's injury.
  - **Window:** the start is tied to Leonard (about 4 Dec, [TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/); *ESPN est.* 3 Dec) and Barrett (re-evaluation about 3 Dec, [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks); *ESPN est.* 13 Dec). Both are out all week.
  - **Monday:** started and had 15 pts, 6 reb and 2 ast in 36 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Numbers:** FP/g without the absentees 32.0 (3 g, 35.7 min). Season 25.5 (17), L7 34.5 (4), L15 25.1 (8), L30 25.2 (15). Rate 27.8; ESPN proj. 17.6. Minutes 31.7 for the season, 35.0 over L7. ([Injury Watch, 24 Nov](20261124-injury-watch.md); Rate from `form.py`, 24 Nov)
  - **Games:** 2 (Fri vs BKN, Sun vs DEN). ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124))
- **Charles Bassey** (GS, free agent, 4%):
  - **Opening:**
    - Kristaps Porzingis: no timetable reported ([Heavy via Yahoo, 22 Oct](https://sports.yahoo.com/articles/kristaps-porzingis-coming-back-warriors-035243404.html)); *ESPN est.* 2 Jan.
    - Stephen Curry: the next update is due about Thanksgiving, 26 Nov ([Heavy via Yahoo, 22 Nov](https://sports.yahoo.com/articles/warriors-good-stephen-curry-news-043445397.html)); *ESPN est.* 12 Dec.
  - **Window:** both are out past Sunday. Al Horford, the C Bassey replaced in the lineup, is healthy and came off the bench for 18 min on 22 Nov ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035)). So the start depends on Kerr's choice, not on an injury.
  - **Role:** started 18, 19 and 22 Nov (22, 25 and 26 min). He "could potentially remain in the starting lineup for the foreseeable future" ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/gsw-starts-melton-podz-yaxel-green-bassey)). GS has not played since 22 Nov.
  - **Numbers:** FP/g without the absentees 28.4 (5 g, 21.8 min). Season 23.3 (15), L7 31.2 (4), L15 28.4 (7), L30 23.3 (15). Rate 26.9; ESPN proj. 14.5. Minutes 15.6 for the season, 22.2 over L7. ([Injury Watch, 24 Nov](20261124-injury-watch.md); Rate from `form.py`, 24 Nov)
  - **Games:** **3** (Wed vs SAC, Fri @POR, Sun vs LAC), the most in this group. For Wednesday, add by Thu 26 Nov 9:00 AM Melbourne. ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124))
- **Buddy Hield** (CHI, free agent, 5%):
  - **Opening:** Caleb Wilson is out with a right metacarpal fracture ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). His next update is about 3 Dec ([Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20)); *ESPN est.* 13 Dec. Norman Powell is also out; his re-evaluation is due "sometime this week" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday)); *ESPN est.* 28 Nov.
  - **Window:** Wilson's absence (next update about 3 Dec, [Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20); *ESPN est.* 13 Dec) keeps Hield's extra bench minutes going past Sunday. The start lasts only until Powell returns (re-evaluation this week, [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday); *ESPN est.* 28 Nov), and Powell's earliest game is Sat vs IND.
  - **Monday:** his second straight start, with 17 pts (4 3PT), 5 reb and 2 stl in 27 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)). "Until Powell is cleared to play, Hield is worth streaming" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday)).
  - **Numbers:** FP/g without Wilson 30.6 (7 g, 24.7 min). Season 21.0 (15), L7 30.8 (5), L15 30.6 (7), L30 22.3 (13). Rate 26.7; ESPN proj. 16.9. Minutes 18.5 for the season, 25.6 over L7. ([Injury Watch, 24 Nov](20261124-injury-watch.md); Rate from `form.py`, 24 Nov)
  - **Games:** 2 (Wed @CHA, Sat vs IND). Wednesday's start is the secure part. ([ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124))

Not shortlisted:
- **Norman Powell** (Rate 33.0) and **Duncan Robinson** (Rate 25.1) are both still out, and neither re-evaluation has a result yet ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday); [NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/duncan-robinson-quad-remains-out-tuesday-vs-orl)). Powell can play one game this week at most (Sat), and Robinson two (Fri, Sun). See the absentee bullets below.
- **Allen Graves** (Rate 20.6): he started Monday, but his start may end Friday if Collin Murray-Boyles rejoins the lineup ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)).
- **Mikel Brown Jr.** (Rate 18.9): 3 games, but Fri and Sat are a back-to-back, and he had not been cleared for back-to-backs as of 6 Nov ([NBC Sports, 23 Nov page, 6 Nov note](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mikel-brown-jr-posts-17-5-7-line-in-first-start)). His 32.0 FP/g without Traoré rests on one game (**small sample**).
- **Isaac Okoro** (Rate 23.4): a secure start until Wilson returns ([Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html)), but a low rate.

## Research

New since 23 Nov. Notes in [20261123-injury-watch.md](20261123-injury-watch.md) still hold where this says "unchanged". All Monday 23 Nov games are final. The official report cited is [NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf), which covers Mon 23 and Tue 24 Nov.

**Absentees**

- **Jalen Duren (us, DET):**
  - **Status:** out Tue at ORL ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). He "was set to be re-evaluated on Sunday", with no update since. John Collins starts at C again ([NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/jalen-duren-hamstring-remains-out-vs-orlando)).
  - **Timeline:** no timetable reported. *ESPN est.* 30 Nov (was 24 Nov). DET has two games left after Tuesday: Fri vs MIL and Sun vs ORL.
  - **Override:** his `return` row (24 Nov) has now expired.
- **Cade Cunningham (us, DET):** **New on the injury list.** He is **probable** Tue at ORL with right knee soreness ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf); [Heavy, 23 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-pistons-magic/)). He played through the soreness Sunday at ATL, with 33 min: 5 pts (2-9 FG), 15 ast ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). No timetable reported, as he is day-to-day. *ESPN est.* 24 Nov.
- **Kawhi Leonard (us, IR, TOR):** Out Mon vs MIL with "Left Knee Injury Management" ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)).
  - **New detail:** he took mid-range and three-point shots on the court Sunday, but he still has to scrimmage with teammates before he can return ([Roundtable via Yahoo, 23 Nov](https://sports.yahoo.com/articles/darko-rajakovic-gives-raptors-forward-194758381.html)).
  - **Timeline:** at least two more weeks from 20 Nov, so about 4 Dec ([TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/)). *ESPN est.* 3 Dec.
- **Duncan Robinson (DET, free agent):** Out Tue at ORL ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)).
  - **Re-evaluation:** due "sometime this week", with no result reported. "Kevin Huerter has moved into the starting lineup and should remain there until Robinson is available" ([NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/duncan-robinson-quad-remains-out-tuesday-vs-orl)).
  - **Timeline:** no timetable reported. *ESPN est.* 27 Nov, so Fri vs MIL would be his first game.
- **Austin Reaves (LAL):** Out Mon vs UTA, his fifth straight absence ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)).
  - **New:** Redick called Monday's stay-ready game a "big step" and said the Lakers are "optimistic for the rest of this week" ([Heavy, 23 Nov](https://heavy.com/sports/nba/los-angeles-lakers/austin-reaves-injury-update-lakers-big-step/)).
  - **Timeline:** McMenamin reports the team hopes he returns Fri at SA (same Heavy article). *ESPN est.* 27 Nov, which matches.
- **Stephen Curry (GS):** Unchanged since 23 Nov. GS did not play Mon or Tue, and no new report was found. The next update is due about Thanksgiving, 26 Nov ([Heavy via Yahoo, 22 Nov](https://sports.yahoo.com/articles/warriors-good-stephen-curry-news-043445397.html)). *ESPN est.* 12 Dec.
- **Collin Murray-Boyles (TOR):** **Back.** He was available Mon ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)) but came off the bench: 6 pts, 10 reb and 3 stl in 24 min. Allen Graves started instead ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Ahead:** Rotoworld says "CMB was the player on the court in crunch time", and that four days off "may be enough time to get Murray-Boyles back into the starting lineup" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)).
  - He is no longer in ESPN's injury feed.
- **Paolo Banchero (ORL):** Out Tue vs DET with a right high ankle sprain ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)).
  - **Timeline:** Sweeney: "no timeline right now" ([HoopsHype via Yahoo, 18 Nov](https://sports.yahoo.com/articles/still-no-timeline-paolo-banchero-192859712.html)). Banchero hopes to be back "within the next couple of weeks", so about 3 Dec, and has begun light shooting ([Heavy via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-bachero-reveals-190941314.html)).
  - *ESPN est.* 29 Nov, earlier than his own estimate. ORL plays Tue vs DET, Sat @WSH and Sun @DET.
- **Caleb Wilson (CHI):** Unchanged since 23 Nov. He was out Mon vs CLE with a right metacarpal fracture ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). The next update is about 3 Dec ([Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20)). *ESPN est.* 13 Dec.
- **Norman Powell (CHI, now a free agent):** Out Mon vs CLE ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). His re-evaluation is due "sometime this week", with no result reported ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday)). Earlier notes had him likely to miss Wednesday too (same page, 22 Nov notes). *ESPN est.* 28 Nov, so Sat vs IND at the earliest.
- **Evan Mobley (CLE):** No re-evaluation result reported. He was out Mon at CHI with a left great toe sprain ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). The 7–10-day window from 16 Nov ends about 26 Nov ([SB Nation via Yahoo, 17 Nov](https://sports.yahoo.com/articles/cavs-announce-injury-evan-mobley-001945601.html)). *ESPN est.* 29 Nov. CLE plays Wed at NY and Sun vs MIA.
- **RJ Barrett (TOR):** Unchanged since 23 Nov. He was out Mon ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)), with a re-evaluation about 3 Dec ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks)). *ESPN est.* 13 Dec.
- **Brandon Williams (GS):** Unchanged. Kerr says he will "most likely" play Wed vs SAC ([Warriors On SI, 21 Nov](https://www.si.com/nba/warriors/onsi/steve-kerr-announces-likely-return-date-for-warriors-pg-brandon-williams-01m805axs0q9)). *ESPN est.* 25 Nov. He plays guard and does not touch Bassey's role.
- **Nolan Traoré (BKN):** **New long absence.** A right hamstring strain from Friday; he "will be re-evaluated in 8-10 weeks", so between mid-January and early February. Egor Dëmin and Danny Wolf are the likeliest new starters, and Mikel Brown Jr.'s minutes restriction is lifted: Fernández says he can play "starters' minutes" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/nolan-traore-hamstring-out-8-10-weeks)). *ESPN est.* 27 Jan.
- **Cameron Boozer (MEM, Lauri Birds):** **New long absence.** A moderate-grade medial right ankle sprain, structurally stable. He "will be re-evaluated in four weeks", about 21 Dec ([NBA.com, 23 Nov](https://www.nba.com/news/memphis-cameron-boozer-to-miss-at-least-a-month-with-sprained-right-ankle)). *ESPN est.* 21 Dec.
  - **Pickup angle:** Kris Murray (free agent, 0%) started Monday at CHA and had 9 pts, 4 stl and 1 blk in 32 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036)).
  - His 25.5 FP/g without the absentees rests on 2 games (**small sample**). Season 10.3, L7 12.6 (5). MEM has 3 games left (Wed vs LAC, Fri @MIN, Sun vs LAL).

**Pickups for us**

- **Jakob Poeltl (TOR, 2 games):** See the shortlist. He is the starting C, but Murray-Boyles's return to the lineup could cost him the start, as it did on 17 Nov ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002)).
  - **Form:** L7 32.5 (4) against a season of 27.4, +5.1.
  - **Why:** minutes, 24.2 for the season and 26.8 over L7, from starts on 18, 20 and 23 Nov (29, 32 and 28 min) ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308); [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Ends:** when Leonard (*ESPN est.* 3 Dec) or Barrett (*ESPN est.* 13 Dec) returns, both after this week.
- **Norman Powell (CHI, 2 games, out):** His re-evaluation is due this week, with no result yet ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday)). *ESPN est.* 28 Nov. At best he plays Sat vs IND.
  - **Form:** season 30.1 (13) → 32.2 (12), L7 30.3 (3), L15 36.2 (5), L30 31.1 (11) → 33.8 (10). Rate 33.0.
- **Duncan Robinson (DET, 3 games, out):** Out Tue at ORL, with a re-evaluation "sometime this week" ([NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/duncan-robinson-quad-remains-out-tuesday-vs-orl)). *ESPN est.* 27 Nov. That leaves at most 2 games (Fri vs MIL, Sun vs ORL).
  - **Form:** season 29.8 (12), no L7 (injured), L15 19.8 (4), L30 29.9 (10). Rate 25.1.
  - Jalen Duren (us; *ESPN est.* 30 Nov) was also out in his "without" games.
- **Ja'Kobe Walter (TOR, 2 games):** See the shortlist. He started all four of his last games, at 33, 38, 33 and 36 min ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002); [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308); [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Form:** L7 34.5 (4) against a season of 25.5, +9.0.
  - **Why:** minutes (31.7 for the season, 35.0 over L7) and two big games: 25 pts on 7-12 3PT on 17 Nov, and 18 pts, 7 reb and 6 ast in 38 min on 18 Nov (same box scores). He went 2-11 FG on 20 Nov.
  - **Ends:** when Leonard or Barrett returns, both after this week.
- **Mikel Brown Jr. (BKN, 3 games):** He made his first career start Mon at MIN: 17 pts (4 3PT), 5 reb, 7 ast and 6 TO in 29 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mikel-brown-jr-posts-17-5-7-line-in-first-start)).
  - **Role:** "no longer under a minutes restriction", and there is "certainly room for Brown to play heavy minutes" while Traoré is out (same NBC page).
  - **Back-to-backs:** a 6 Nov note on that page said he had not yet been cleared to play both halves of a back-to-back, and no update has been found. BKN plays Wed @MIL, then Fri @TOR and Sat @CHA, a back-to-back.
  - **Ends:** when Traoré returns (*ESPN est.* 27 Jan).
  - **Form:** season 19.0 (12), L7 18.0 (4), L15 18.0 (5), L30 19.7 (11). L7 is within 5 of the season. Rate 18.9. His 32.0 FP/g without Traoré rests on 1 game (**small sample**).
- **Allen Graves (TOR, 2 games):** He started again Monday but had only 7 pts and 2 reb in 31 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Ends:** his start may end Fri if Murray-Boyles rejoins the lineup ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)).
  - **Form:** L7 26.0 (4) against a season of 16.2, +9.8.
  - **Why:** minutes (16.9 for the season, 27.0 over L7) and one 60-FP game: 20 pts, 10 reb and 3 stl in his first start on 20 Nov ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308)).
  - **Rate:** 20.6.
- **Buddy Hield (CHI, 2 games):** See the shortlist. He started Monday in Powell's place ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)) and is "worth streaming" until Powell is cleared ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday)).
  - **Form:** L7 30.8 (5) against a season of 21.0, +9.8.
  - **Why:** minutes, 18.5 for the season and 25.6 over L7. They grew off the bench after Wilson's injury, then came starts in Powell's place on 22 Nov (33 pts, 40 min, with overtime) and 23 Nov (17 pts, 27 min) ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032); [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)).
  - **Ends:** the start ends when Powell returns (*ESPN est.* 28 Nov). The bench minutes last until Wilson returns (*ESPN est.* 13 Dec).
- **De'Andre Hunter (SAC, 2 games):** See the shortlist. Rotoworld: "Hunter's inability to provide defensive stats keeps his fantasy value low" ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/deandre-hunter-dishes-out-eight-assists-vs-spurs)). Our scoring rewards his points, rebounds and assists all the same.
  - **Form:** L7 36.5 (4) against a season of 25.6, +10.9.
  - **Why:** minutes (33.9 for the season, 37.8 over L7) and a 30-pt game on 20 Nov ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909313)), then 38 min Monday ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045)).
  - **Ends:** Simmons is out for the season. Raynaud's return (*ESPN est.* 25 Nov) is the risk.
- **Charles Bassey (GS, 3 games):** See the shortlist. Unchanged since 23 Nov, as GS has not played since 22 Nov. He "could potentially remain in the starting lineup for the foreseeable future" ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/gsw-starts-melton-podz-yaxel-green-bassey)).
  - **Form:** L7 31.2 (4) against a season of 23.3, +8.0.
  - **Why:** minutes, 15.6 for the season and 22.2 over L7, from starts on 18, 19 and 22 Nov ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910016); [19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019); [22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035)).
  - **Ends:** with Porzingis's return (*ESPN est.* 2 Jan), or if Kerr goes back to Horford, who is healthy and coming off the bench.
- **Isaac Okoro (CHI, 2 games):** Still the starting SF. Monday: 12 pts (3-5 3PT), 4 reb and 3 ast in 27 min, in a 122-108 win ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)).
  - **Form:** L7 29.0 (5) against a season of 17.4, +11.6.
  - **Why:** the starter's minutes since Wilson's injury, 24.6 for the season and 31.0 over L7. He holds the job "until Wilson returns in December" ([Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html)). Wilson: *ESPN est.* 13 Dec.
  - **Rate:** 23.4.

**Back soon**

- **Mitchell Robinson (BOS):** **Out again Tue at WSH** with an illness, his third straight absence ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mitchell-robinson-illness-out-again-vs-wizards)). No timetable reported. *ESPN est.* 27 Nov (was 24 Nov). BOS then plays Fri vs ATL and Sun at SA.
- **P.J. Washington (DAL):** **Questionable** Tue at DEN with an illness, after missing two games ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/p-j-washington-illness-questionable-tuesday)). No timetable reported. *ESPN est.* 24 Nov.
- **Jaxson Hayes (UTAH):** Out Mon at LAL with a left knee strain ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). No timetable reported. Mo Bamba started at C, with 29 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910044)). *ESPN est.* 27 Nov, now listed day-to-day.
- **Jusuf Nurkic (UTAH):** Unchanged. The official report now names the injury as a right second-toe plantar plate tear ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). The re-evaluation is still about 27 Nov ([Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). *ESPN est.* 29 Nov.
- **Ja Morant (POR):** Unchanged. Out Mon at PHI ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). The four-week re-evaluation falls about 27 Nov ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)), and no result has been reported. *ESPN est.* 1 Dec.
- **Grayson Allen (CHA):** Still in concussion protocol and out Mon vs MEM ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). No timetable reported. *ESPN est.* 25 Nov. CHA plays Wed vs CHI and Sat vs BKN.
- **Maxime Raynaud (SAC):** Out Mon vs SA with right patella subluxation ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)), still week-to-week ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)). *ESPN est.* 25 Nov. The `return` floor of 25 Nov holds.
- **Dejounte Murray (NO):** Unchanged. Out Mon vs PHX with a left ankle sprain ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)). He is sitting until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)), and no deal has been reported. No timetable reported. *ESPN est.* 27 Nov.
- **Others listed out again, all unchanged since 23 Nov** ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)):

  | Player | Out | *ESPN est.* |
  |---|---|---|
  | Scotty Pippen Jr. (MEM) | Mon @CHA | 25 Nov |
  | Tobias Harris (SA) | Mon @SAC | 3 Dec |
  | Bennedict Mathurin (NO) | Mon vs PHX | 27 Nov |
  | T.J. McConnell (IND) | Mon vs OKC | 27 Nov |
  | Bradley Beal (LAC) | Mon @HOU | 29 Nov |
  | Dereck Lively II (DAL) | Tue @DEN | 27 Nov |

  - Each is "no timetable reported", except Harris, whose debut is "expected to be next month" ([Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/san-antonio-spurs-release-injury-190006533.html)).
  - Jock Landale (ATL) has not had a game since he sat out Sun 22 Nov ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)). No timetable reported. *ESPN est.* 27 Nov.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 25.7 (L7 33.4), Neemias Queta 27.2 (L7 34.3), Myles Turner 28.9 (L7 39.3), Brook Lopez 29.8 (L7 30.8), Trey Murphy III 31.1 (L7 31.5). A pickup at or above **31.1** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 29.7 | +5.0 | **38.7** | 27.4 | 32.5 (4) | 31.1 (8) | 28.2 (13) | Free agent | 38% | 2 / 2 |
| **Norman Powell** (out, ESPN est. back 28 Nov) | CHI | Caleb Wilson (13 Dec) | 5 | 30.6 | +8.6 | **36.2** | 30.1 | 30.3 (3) | 36.2 (5) | 31.1 (11) → 33.8 (10) | Free agent | 77% | 2 / 2 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (13 Dec); also out: Jalen Duren (30 Nov) | 5 | 34.2 | +17.2 | **32.8** | 29.8 | — | 19.8 (4) | 29.9 (10) | Free agent | 37% | 3 / 2 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 35.7 | +3.4 | **32.0** | 25.5 | 34.5 (4) | 25.1 (8) | 25.2 (15) | Free agent | 13% | 2 / 2 |
| **Mikel Brown Jr.** | BKN | Nolan Traore (27 Jan) | 1 | 29.0 | +6.0 | **32.0** | 19.0 | 18.0 (4) | 18.0 (5) | 19.7 (11) | Free agent | 6% | 3 / 2 |
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 31.7 | +17.0 | **31.3** | 16.2 | 26.0 (4) | 19.6 (8) | 15.9 (15) | Free agent | 1% | 2 / 2 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 7 | 24.7 | +16.7 | **30.6** | 21.0 | 30.8 (5) | 30.6 (7) | 22.3 (13) | Free agent | 5% | 2 / 2 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 37.0 | +9.4 | **30.5** | 25.6 | 36.5 (4) | 32.7 (7) | 27.8 (13) | Free agent | 15% | 2 / 2 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov), Moses Moody (01 Dec) | 5 | 21.8 | +6.0 | **28.4** | 23.3 | 31.2 (4) | 28.4 (7) | 23.3 (15) | Free agent | 4% | 3 / 1 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 7 | 32.4 | +11.4 | **27.7** | 17.4 | 29.0 (5) | 24.3 (9) | 18.0 (15) | Free agent | 2% | 2 / 2 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 7 | 21.7 | — | **27.6** | 26.2 | 25.8 (4) | 27.6 (7) | 27.5 (11) | Free agent | 3% | 3 / 2 |
| **Jaxson Hayes** (day to day, ESPN est. back 27 Nov) | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 7 | 22.0 | +5.2 | **26.0** | 27.1 | 26.3 (3) | 26.0 (7) | 24.8 (13) | Free agent | 11% | 2 / 2 |
| **Kris Murray** | MEM | Cameron Boozer (21 Dec), Jerami Grant (12 Dec), GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 2 | 22.0 | +14.9 | **25.5** | 10.3 | 12.6 (5) | 11.1 (8) | 10.4 (13) | Free agent | 0% | 3 / 2 |
| **Kenrich Williams** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 24.4 | +9.0 | **25.4** | 20.6 | 33.8 (4) | 27.6 (8) | 22.2 (16) | Free agent | 2% | 2 / 2 |
| **Luguentz Dort** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 3 | 28.3 | +4.0 | **24.7** | 20.0 | 24.7 (3) | 19.7 (6) | 20.5 (15) | Free agent | 3% | 2 / 2 |
| **Terrence Shannon Jr.** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 8 | 23.9 | +3.2 | **24.0** | 22.1 | 30.4 (5) | 23.9 (8) | 23.1 (13) | Free agent | 7% | 3 / 2 |
| **Kingston Flemings** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 1 | 27.0 | +3.8 | **24.0** | 19.9 | 24.0 (1) | 14.3 (3) | 20.4 (11) | Free agent | 4% | 2 / 2 |
| **Bennett Stirtz** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 21.8 | — | **22.9** | 17.7 | 29.8 (4) | 22.0 (8) | 19.9 (16) | Free agent | 2% | 2 / 2 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov), Moses Moody (01 Dec) | 5 | 24.8 | +6.1 | **21.6** | 15.5 | 24.0 (4) | 20.7 (6) | 15.7 (14) | Free agent | 1% | 3 / 1 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 21.2 | — | **21.4** | 22.5 | 18.0 (4) | 21.5 (8) | 22.6 (16) | Free agent | 5% | 2 / 2 |
| **Isaiah Stewart** | MEM | Cameron Boozer (21 Dec), Jerami Grant (12 Dec), GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 2 | 21.0 | +3.2 | **21.0** | 21.0 | 19.0 (3) | 18.8 (6) | 22.2 (12) | Free agent | 3% | 3 / 2 |
| **Coby White** | CHA | Kon Knueppel (12 Dec) | 8 | 21.5 | +3.5 | **20.4** | 19.0 | 31.0 (3) | 26.3 (6) | 19.0 (9) | Free agent | 59% | 2 / 2 |
| **Luke Kornet** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 3 | 18.0 | +3.3 | **20.3** | 14.8 | 18.8 (4) | 17.5 (8) | 15.1 (16) | Free agent | 1% | 3 / 2 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 3 | 30.6 | — | 13.7 (3) | 25.6 (7) | 39.0 | 36.5 | Free agent | 73% | 2 / 2 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 7 | 33.8 | — | — | 28.0 (2) | 37.5 | 36.0 | Free agent | 80% | 3 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 5 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 2 |
| **Norman Powell** | CHI | Right Hamstring Strain | 28 Nov | 4 | 30.1 | 30.3 (3) | 36.2 (5) | 31.1 (11) → 33.8 (10) | 36.0 | 33.0 | Free agent | 77% | 2 / 2 |
| **Grayson Allen** | CHA | Concussion | 25 Nov | 1 | 26.8 | — | 36.0 (3) | 27.3 (11) | 26.6 | 31.2 | Free agent | 19% | 2 / 2 |
| **P.J. Washington** | DAL | Illness | 24 Nov | 0 | 28.2 | 58.0 (1) | 25.0 (6) | 27.8 (13) | 26.9 | 30.6 | Free agent | 31% | 2 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 1 | 14.2 | — | — | 8.3 (3) | 30.6 | 27.1 | Free agent | 8% | 3 / 2 |
| **Mitchell Robinson** | BOS | Illness | 27 Nov | 3 | 18.6 | 13.0 (2) | 20.3 (6) | 18.7 (12) | 30.3 | 28.2 | Free agent | 10% | 3 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 9 | — | — | — | — | 30.1 | 28.0 | Free agent | 39% | 3 / 2 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 3 | 29.8 | — | 19.8 (4) | 29.9 (10) | 21.6 | 23.1 | Free agent | 37% | 3 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 1 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 2 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 3 | 8.8 | — | 3.7 (3) | 8.2 (10) | 25.1 | 27.6 | Free agent | 6% | 2 / 2 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 3 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 2 / 2 |
| **Jaxson Hayes** | UTAH | Left Knee | 27 Nov | 3 | 27.1 | 26.3 (3) | 26.0 (7) | 24.8 (13) | 16.5 | 20.2 | Free agent | 11% | 2 / 2 |
| **Jock Landale** | ATL | Right Hip Inflammation | 27 Nov | 3 | 16.8 | — | 18.0 (2) | 13.7 (7) → 16.0 (6) | — | 25.8 | Free agent | 0% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 5 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 3 / 2 |
| **T.J. McConnell** | IND | Left Hamstring | 27 Nov | 3 | 20.0 | 20.0 (2) | 21.2 (6) | 20.0 (7) | 24.4 | 25.5 | Free agent | 7% | 2 / 2 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.1.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 1 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 2 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 3 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 5 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 3 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 5 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 9 | 30.1 (30.5) | 28.0 (63) | Free agent | 39% | 3 / 2 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 39 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 3 / 1 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 39 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 3 / 1 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 71 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 3 / 2 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 98 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 3 / 2 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 129 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 3 / 2 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 30 Nov.
- **Cade Cunningham** (DET): Day-To-Day, Knee; ESPN est. back 24 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 03 Dec.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

Also out in those games, so part of the gain is theirs: Brandon Williams (left hamstring strain; ESPN est. 25 Nov), Moses Moody (left knee surgery; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Charles Bassey | C | 5 | 21.8 | +6.0 | 3 | **28.4** | 26.6 | 31.2 (4) | 28.4 (7) | 23.3 (15) | Free agent | 4% |
| Will Richard | SG/SF | 5 | 24.8 | +6.1 | 1 | **21.6** | 15.0 | 24.0 (4) | 20.7 (6) | 15.7 (14) | Free agent | 1% |
| Gui Santos | SF | 5 | 20.6 | +5.6 | 1 | **19.4** | 6.7 | 20.8 (4) | 16.3 (7) | 14.3 (12) | Free agent | 1% |
| LJ Cryer | PG | 5 | 18.0 | +8.0 | 2 | **16.4** | 8.2 | 10.0 (4) | 16.6 (7) | 10.1 (13) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara (day to day, ESPN est. back 25 Nov) | C | 8 | 25.8 | — | 5 | **37.2** | — | 50.0 (2) | 38.0 (6) | 31.7 (14) | Snow Time Lakers | 33% |
| Kenrich Williams | SF | 10 | 24.4 | +9.0 | 6 | **25.4** | 14.2 | 33.8 (4) | 27.6 (8) | 22.2 (16) | Free agent | 2% |
| Bennett Stirtz | PG | 10 | 21.8 | — | 0 | **22.9** | — | 29.8 (4) | 22.0 (8) | 19.9 (16) | Free agent | 2% |
| 5105800 |  | 5 | 20.2 | — | 0 | **13.0** | — | — | — | — | — | 0% |
| Micah Peavy | SF | 8 | 18.9 | — | 2 | **12.9** | — | 15.7 (3) | 10.8 (6) | 11.5 (12) | Free agent | 0% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Cameron Boozer | Right Ankle Sprain | 21 Dec | 31.7 | 38.9 | Lauri Birds |
| Jerami Grant | Left Calf | 12 Dec | 29.8 | 20.3 | Free agent |
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Murray | PF | 2 | 22.0 | +14.9 | 1 | **25.5** | 6.1 | 12.6 (5) | 11.1 (8) | 10.4 (13) | Free agent | 0% |
| Isaiah Stewart | PF/C | 2 | 21.0 | +3.2 | 0 | **21.0** | 17.8 | 19.0 (3) | 18.8 (6) | 22.2 (12) | Free agent | 3% |
| Jahmai Mashack | SG | 1 | 22.0 | +12.6 | 1 | **11.0** | 4.6 | 8.2 (4) | 6.6 (5) | 5.4 (8) | Free agent | 0% |
| Olivier-Maxence Prosper | PF | 2 | 21.0 | +8.1 | 0 | **9.0** | 11.9 | 13.6 (5) | 12.2 (8) | 10.2 (12) | Free agent | 0% |
| Taylor Hendricks | PF | 2 | 25.5 | +8.1 | 0 | **7.0** | 24.4 | 18.8 (5) | 22.6 (9) | 16.8 (13) | Free agent | 2% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 21.2 | — | 2 | **21.4** | — | 18.0 (4) | 21.5 (8) | 22.6 (16) | Free agent | 5% |
| Jalen Slawson | SF | 9 | 12.7 | — | 0 | **21.1** | — | 31.5 (4) | 24.0 (7) | 17.8 (15) | Free agent | 0% |
| Braden Smith | PG | 7 | 16.7 | — | 4 | **18.3** | — | 22.0 (4) | 18.4 (5) | 15.8 (12) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Scottie Barnes | SG/SF | 2 | 37.5 | +3.5 | 2 | **61.5** | 44.7 | 53.3 (3) | 55.2 (4) | 49.2 (10) → 53.3 (9) | **us** | 99% |
| Jakob Poeltl | C | 3 | 29.7 | +5.0 | 3 | **38.7** | 30.4 | 32.5 (4) | 31.1 (8) | 28.2 (13) | Free agent | 38% |
| Ja'Kobe Walter | SG | 3 | 35.7 | +3.4 | 3 | **32.0** | 19.0 | 34.5 (4) | 25.1 (8) | 25.2 (15) | Free agent | 13% |
| Allen Graves | SF | 3 | 31.7 | +17.0 | 2 | **31.3** | 10.9 | 26.0 (4) | 19.6 (8) | 15.9 (15) | Free agent | 1% |
| Trayce Jackson-Davis | PF | 3 | 12.7 | +3.7 | 0 | **16.0** | 18.5 | 16.0 (3) | 18.2 (4) | 14.3 (10) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.9 | +3.2 | 10 | **45.1** | 29.7 | 50.4 (5) | 46.0 (8) | 41.1 (16) | Melbourne poopoo | 92% |
| Ayo Dosunmu | PG/SG | 10 | 32.8 | +3.4 | 10 | **33.6** | 30.4 | 29.2 (5) | 31.9 (8) | 34.2 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 30.8 | +3.5 | 9 | **26.2** | 26.3 | 28.8 (4) | 23.4 (7) | 27.8 (15) | Dr White Slong | 61% |
| Terrence Shannon Jr. | SG | 8 | 23.9 | +3.2 | 0 | **24.0** | 14.9 | 30.4 (5) | 23.9 (8) | 23.1 (13) | Free agent | 7% |
| Joan Beringer | C | 10 | 16.1 | — | 0 | **18.4** | — | 21.2 (5) | 20.0 (8) | 21.0 (16) | Free agent | 1% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 10 | 23.4 | — | 4 | **28.3** | — | 24.6 (5) | 28.3 (10) | 27.9 (15) | Team Nic Kerr | 16% |
| Jaxson Hayes (day to day, ESPN est. back 27 Nov) | C | 7 | 22.0 | +5.2 | 6 | **26.0** | 16.5 | 26.3 (3) | 26.0 (7) | 24.8 (13) | Free agent | 11% |
| Svi Mykhailiuk | SG | 10 | 22.7 | — | 0 | **17.8** | — | 28.2 (5) | 17.8 (10) | 12.5 (17) | Free agent | 2% |
| Josh Green | SG | 10 | 22.5 | +4.2 | 9 | **13.4** | 11.4 | 16.8 (5) | 13.0 (10) | 10.9 (17) | Free agent | 0% |
| Josh Okogie | SF | 10 | 17.9 | — | 2 | **11.4** | — | 9.2 (5) | 11.4 (10) | 12.0 (17) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama (day to day, ESPN est. back 25 Nov) | C | 2 | 32.5 | +4.4 | 2 | **90.5** | 68.6 | 80.7 (3) | 77.7 (7) | 75.7 (15) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 3 | 33.0 | +4.1 | 3 | **51.7** | 34.9 | 42.8 (4) | 41.1 (8) | 36.8 (16) | Melbourne poopoo | 96% |
| Luke Kornet | C | 3 | 18.0 | +3.3 | 1 | **20.3** | 15.4 | 18.8 (4) | 17.5 (8) | 15.1 (16) | Free agent | 1% |
| Ja'Kobi Gillespie | PG | 1 | 15.0 | — | 0 | **18.0** | — | 18.0 (1) | 18.0 (1) | 11.0 (2) | Free agent | 0% |
| Jordan McLaughlin | PG | 3 | 14.3 | +3.3 | 0 | **14.3** | 14.7 | 14.3 (3) | 16.1 (7) | 11.8 (12) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Ja Morant (left hamstring; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 10 | 26.4 | +10.2 | 8 | **19.6** | 10.6 | 21.0 (5) | 20.8 (8) | 18.3 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | — | 0 | **16.7** | — | — | 14.0 (1) | 10.5 (6) | Free agent | 0% |
| Jayson Kent | PF | 7 | 13.6 | — | 2 | **10.3** | — | 10.8 (5) | 10.0 (6) | 10.3 (7) | Waivers | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Jock Landale (right hip inflammation; ESPN est. 27 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 3 | 37.0 | +4.9 | 3 | **53.3** | 44.9 | 53.3 (3) | 46.5 (6) | 41.1 (15) | Snow Time Lakers | 97% |
| Luguentz Dort | SG/SF | 3 | 28.3 | +4.0 | 0 | **24.7** | 21.4 | 24.7 (3) | 19.7 (6) | 20.5 (15) | Free agent | 3% |
| Kingston Flemings | PG/SG | 1 | 27.0 | +3.8 | 1 | **24.0** | 18.2 | 24.0 (1) | 14.3 (3) | 20.4 (11) | Free agent | 4% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.8 | +5.4 | 10 | **36.4** | 30.2 | 36.0 (4) | 32.1 (8) | 36.8 (16) | Snow Time Lakers | 81% |
| AJ Dybantsa | SF | 10 | 35.2 | +3.0 | 10 | **31.6** | 32.9 | 43.0 (4) | 32.1 (8) | 30.3 (14) | Dr White Slong | 86% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Coby White | PG/SG | 8 | 21.5 | +3.5 | 8 | **20.4** | 8.0 | 31.0 (3) | 26.3 (6) | 19.0 (9) | Free agent | 59% |
| Christian Anderson | PG | 9 | 17.1 | — | 0 | **18.2** | — | 25.0 (3) | 23.2 (6) | 14.2 (13) | Free agent | 0% |
| Royce O'Neale | SF/PF | 9 | 22.1 | +4.1 | 0 | **13.9** | 9.0 | 11.3 (3) | 12.3 (6) | 11.5 (14) | Free agent | 1% |
| Tidjane Salaun | PF | 9 | 14.2 | +4.2 | 0 | **11.2** | 13.0 | 9.0 (3) | 10.3 (6) | 10.9 (14) | Free agent | 0% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 2 | 29.0 | +9.0 | 1 | **5.5** | 17.0 | — | — | 19.3 (7) | Free agent | 3% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jalen Smith | PF/C | 5 | 28.0 | +5.7 | 5 | **45.8** | 35.7 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | **us** | 53% |
| Norman Powell (out, ESPN est. back 28 Nov) | SG/SF | 5 | 30.6 | +8.6 | 5 | **36.2** | 4.0 | 30.3 (3) | 36.2 (5) | 31.1 (11) → 33.8 (10) | Free agent | 77% |
| 4898010 |  | 1 | 22.0 | +14.0 | 0 | **31.0** | 22.0 | — | — | — | — | 0% |
| Buddy Hield | SG/SF | 7 | 24.7 | +16.7 | 2 | **30.6** | 16.0 | 30.8 (5) | 30.6 (7) | 22.3 (13) | Free agent | 5% |
| Isaac Okoro | SG/SF | 7 | 32.4 | +11.4 | 7 | **27.7** | 12.3 | 29.0 (5) | 24.3 (9) | 18.0 (15) | Free agent | 2% |

### BKN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Nolan Traore | Right Hamstring Strain | 27 Jan | 25.0 | 24.9 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mikel Brown Jr. | PG | 1 | 29.0 | +6.0 | 1 | **32.0** | 18.1 | 18.0 (4) | 18.0 (5) | 19.7 (11) | Free agent | 6% |
| Keon Ellis | SG/SF | 2 | 21.0 | +7.0 | 0 | **18.5** | 11.4 | 11.5 (4) | 13.3 (7) | 14.7 (14) | Free agent | 1% |
| Chaney Johnson | SF | 1 | 15.0 | +3.7 | 0 | **14.0** | 7.4 | 6.0 (2) | 7.4 (5) | 11.5 (13) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 7 | 21.7 | — | 0 | **27.6** | — | 25.8 (4) | 27.6 (7) | 27.5 (11) | Free agent | 3% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 30 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 32.1 | +14.1 | 9 | **43.6** | 45.0 | 48.8 (4) | 46.0 (8) | 41.1 (13) | Lauri Birds | 84% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 5 | 34.2 | +17.2 | 5 | **32.8** | 13.0 | — | 19.8 (4) | 29.9 (10) | Free agent | 37% |
| Paul Reed | PF/C | 9 | 26.2 | +3.2 | 3 | **32.8** | 25.0 | 37.0 (4) | 32.4 (8) | 32.5 (14) | Lauri Birds | 40% |
| Javonte Green | SF | 9 | 19.7 | +7.7 | 1 | **16.7** | 5.0 | 20.8 (4) | 17.2 (8) | 14.6 (14) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Bradley Beal (right knee inflammation; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kobe Sanders | SG | 10 | 20.2 | — | 1 | **15.6** | — | 11.8 (4) | 13.5 (8) | 17.0 (14) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 36.6 | +6.0 | 10 | **38.4** | 30.4 | 35.0 (4) | 36.5 (8) | 40.1 (15) | Team Nic Kerr | 92% |
| De'Andre Hunter | SF/PF | 8 | 37.0 | +9.4 | 8 | **30.5** | 23.9 | 36.5 (4) | 32.7 (7) | 27.8 (13) | Free agent | 15% |
| Leaky Black | SF | 10 | 19.4 | — | 1 | **18.0** | — | 10.5 (4) | 16.0 (8) | 17.8 (13) | Free agent | 0% |
| Dylan Cardwell | C | 10 | 14.6 | — | 2 | **15.8** | — | 8.2 (4) | 14.4 (8) | 15.8 (10) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 15.3 | — | 0 | **9.5** | — | 6.5 (4) | 8.9 (8) | 9.6 (15) | Free agent | 0% |

## Every injury

All 92 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 311 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 311 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 219 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 129 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 129 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 113 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 98 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 98 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 98 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 98 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 93 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 71 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 68 | Free agent |
| Nolan Traore | BKN | Out | Right Hamstring Strain | 27 Jan | 64 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 55 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 49 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 41 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 39 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 39 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 39 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 39 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 39 | Free agent |
| Cameron Boozer | MEM | Out | Right Ankle Sprain | 21 Dec | 27 | Lauri Birds |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 27 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 25 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 20 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 19 | Lauri Birds |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 19 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 19 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 19 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 19 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 18 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 18 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 18 | Free agent |
| Jerami Grant | MEM | Out | Left Calf | 12 Dec | 18 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 9 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 9 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 9 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 9 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 7 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 7 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 7 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 30 Nov | 6 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 30 Nov | 6 | **us** |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 30 Nov | 6 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 5 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 29 Nov | 5 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 5 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 5 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 29 Nov | 5 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 5 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 5 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 5 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 5 | Free agent |
| Norman Powell | CHI | Out | Right Hamstring Strain | 28 Nov | 4 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 3 | Free agent |
| Tobi Lawal | DAL | Out | Right Groin | 27 Nov | 3 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 3 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Left Hamstring | 27 Nov | 3 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 3 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 27 Nov | 3 | — |
| Mitchell Robinson | BOS | Out | Illness | 27 Nov | 3 | Free agent |
| Larry Nance Jr. | IND | Day-To-Day | Right Ankle Soreness | 27 Nov | 3 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 27 Nov | 3 | Free agent |
| Jaxson Hayes | UTAH | Day-To-Day | Left Knee | 27 Nov | 3 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 3 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 3 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 3 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 3 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 3 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 27 Nov | 3 | Cream Abdul-Yammar |
| Aaron Nesmith | IND | Day-To-Day | Foot | 27 Nov | 3 | Free agent |
| Victor Wembanyama | SA | Day-To-Day | Back | 25 Nov | 1 | Cream Abdul-Yammar |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 1 | Free agent |
| Ryan Kalkbrenner | CHA | Day-To-Day | Left Hip Soreness | 25 Nov | 1 | Free agent |
| OG Anunoby | NY | Day-To-Day | Left Calf Soreness | 25 Nov | 1 | Cream Abdul-Yammar |
| Nikola Topic | OKC | Out | Left Hip Strain | 25 Nov | 1 | Free agent |
| Miles McBride | NY | Day-To-Day | Left Abdomen | 25 Nov | 1 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 1 | Free agent |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 25 Nov | 1 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Illness | 25 Nov | 1 | Dr White Slong |
| Jaylin Williams | OKC | Day-To-Day | Back Spasms | 25 Nov | 1 | Free agent |
| Grayson Allen | CHA | Out | Concussion | 25 Nov | 1 | Free agent |
| Grant Williams | CHA | Day-To-Day | Right Hamstring | 25 Nov | 1 | Free agent |
| Giannis Antetokounmpo | MIA | Day-To-Day | Groin | 25 Nov | 1 | Dr White Slong |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 1 | Free agent |
| De'Aaron Fox | SA | Day-To-Day | Right Lower Leg Bruise | 25 Nov | 1 | Matt Wright's Foxies |
| Brandon Williams | GS | Out | Left Hamstring Strain | 25 Nov | 1 | Free agent |
| Alex Caruso | OKC | Out | Right Hip Soreness | 25 Nov | 1 | Free agent |
| Aday Mara | OKC | Day-To-Day | Right Lower Leg Bruise | 25 Nov | 1 | Snow Time Lakers |
| P.J. Washington | DAL | Day-To-Day | Illness | 24 Nov | 0 | Free agent |
| Cade Cunningham | DET | Day-To-Day | Knee | 24 Nov | 0 | **us** |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-24 07:07 UTC.
- **Research, 24 Nov:** [ESPN schedule, read 24 Nov](https://www.espn.com/nba/schedule/_/date/20261124) · [AP via NY1, 18 Oct](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/18/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice) · [NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045) · [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/deandre-hunter-dishes-out-eight-assists-vs-spurs) · [Roundtable via Yahoo, 23 Nov](https://sports.yahoo.com/articles/darko-rajakovic-gives-raptors-forward-194758381.html) · [TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/) · [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039) · [ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes) · [Heavy via Yahoo, 22 Oct](https://sports.yahoo.com/articles/kristaps-porzingis-coming-back-warriors-035243404.html) · [Heavy via Yahoo, 22 Nov](https://sports.yahoo.com/articles/warriors-good-stephen-curry-news-043445397.html) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035) · [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/gsw-starts-melton-podz-yaxel-green-bassey) · [Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041) · [NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/duncan-robinson-quad-remains-out-tuesday-vs-orl) · [NBC Sports, 23 Nov page, 6 Nov note](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mikel-brown-jr-posts-17-5-7-line-in-first-start) · [Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html) · [NBC Sports, 23 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-23/jalen-duren-hamstring-remains-out-vs-orlando) · [Heavy, 23 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-pistons-magic/) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029) · [Heavy, 23 Nov](https://heavy.com/sports/nba/los-angeles-lakers/austin-reaves-injury-update-lakers-big-step/) · [HoopsHype via Yahoo, 18 Nov](https://sports.yahoo.com/articles/still-no-timeline-paolo-banchero-192859712.html) · [Heavy via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-bachero-reveals-190941314.html) · [SB Nation via Yahoo, 17 Nov](https://sports.yahoo.com/articles/cavs-announce-injury-evan-mobley-001945601.html) · [Warriors On SI, 21 Nov](https://www.si.com/nba/warriors/onsi/steve-kerr-announces-likely-return-date-for-warriors-pg-brandon-williams-01m805axs0q9) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/nolan-traore-hamstring-out-8-10-weeks) · [NBA.com, 23 Nov](https://www.nba.com/news/memphis-cameron-boozer-to-miss-at-least-a-month-with-sprained-right-ankle) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012) · [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909313) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910016) · [19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mitchell-robinson-illness-out-again-vs-wizards) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/p-j-washington-illness-questionable-tuesday) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910044) · [Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) · [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) · [Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/san-antonio-spurs-release-injury-190006533.html) · [NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)
