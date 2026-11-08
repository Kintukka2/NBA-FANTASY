# Injury Watch: 08 Nov 2026

- Generated 2026-11-08 20:14 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 86 players in ESPN's injury feed. 27 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 16 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (02 Nov–08 Nov) / next week (09 Nov–15 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

- **Our five lowest:** Murphy 29.4 (L7 34.5), Hartenstein 29.6 (L7 31.0), Gafford 30.1 (L7 24.7), P.J. Washington 30.8 (L7 37.3) and Duren 33.5 (out; re-evaluated about 22 Nov, no return date reported; *ESPN est.* 24 Nov). The floor is **33.5**, set by an injured player, and no pickup clears it. Only Bane (32.7) is above all four healthy ones.
- **Anthony Black**, added this morning off waivers for Aday Mara, is not among them: season 38.5 (6) → 44.0 (5), L7 41.0 (3), L15 38.5 (6) → 44.0 (5), L30 38.5 (6) → 44.0 (5), projected 28.2, rate 42.1 (`form.py`). He left Saturday's overtime with cramps, with no injury designation, and is expected for Tue 10 Nov [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping).
- **What a stash costs:** our one IR slot holds Kawhi (update due about 10 Nov; *ESPN est.* 23 Nov), and Duren is OUT on the bench, so any stash costs a healthy player. Which of the two should hold IR is under *Our injured players* [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/).

| Player | NBA | Opening and its window | FP/g without | Season | L7 / L15 / L30 | Min without | Games this / next week |
|---|---|---|---:|---:|---|---:|---|
| **Desmond Bane** (free agent, 90%) | ORL | Paolo Banchero: low-grade high-ankle sprain, 4–6 weeks from 24 Oct, so 21 Nov–5 Dec [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html); *ESPN est.* 22 Nov. Bane is day-to-day with an illness; next chance Tue 10 Nov against SAC [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/) (*ESPN est.* 10 Nov) | 32.7 | 27.8 | 28.0 (3) / 32.7 (6) / 27.8 (8) → 31.9 (7) | 36.0 | 0 / 3 |
| **Christian Braun** (waivers, 40%) | DEN | Julian Strawther: left knee sprain, re-evaluated six weeks from mid-Oct, about 29 Nov, which is not a return date [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html); *ESPN est.* 29 Nov. Braun started before; no source ties his start to Strawther | 30.1 | 30.1 | 22.7 (3) / 32.3 (7) / 30.1 (8) | 34.2 | 0 / 3 |
| **Derrick Jones Jr.** (free agent, 13%) | LAC | Jordan Miller: re-evaluation about late Feb (*ESPN est.* 2 Mar); Bradley Beal: no timetable reported (*ESPN est.* 29 Nov). The *also out* confound, Brandon Ingram, has no timetable reported either (*ESPN est.* 10 Nov) [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans) | 29.4 | 29.4 | 26.0 (2, small sample) / 28.4 (5) / 29.4 (7) | 30.0 | 1 / 3 |
| **Aday Mara** (waivers, 18%; our drop this morning) | OKC | Chet Holmgren: 8–10 weeks from 30 Oct, about 25 Dec–8 Jan [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan. His starts depend on OKC's lineup each night and on Jaylin Williams (back spasms; no timetable reported; *ESPN est.* 10 Nov) [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/) | 29.9 | 24.4 | 31.8 (4) / 27.0 (8) / 24.4 (10) | 22.7 | 0 / 4 |

- **Back-soon stash candidates:**
  - **Norman Powell** (CHI, free agent, 79%): added to Sunday's injury report and ruled out with right shoulder inflammation; Isaac Okoro starts in his place, and Powell's next chance is Wed 11 Nov vs SAS [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/norman-powell-shoulder-out-isaac-okoro-to-start) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-out-sunday/). No timetable reported; *ESPN est.* 11 Nov. Current 26.2 (8) → 29.4 (7); L7 13.5 (2) → 23.0 (1), a small sample, so the dip is noise, and no report ties it to the shoulder; L15 26.8 (6) → 31.4 (5); L30 26.2 (8) → 29.4 (7); projected 36.0; 2026 33.0. Games 1 / 3. Cost: a healthy player's spot through Tuesday. He is a short absence, closer to a Wednesday pickup than a stash.
  - **Kon Knueppel** (CHA, free agent, 87%): left hamstring strain, re-aggravated in his 4 Nov debut; beat writer Rod Boone: "more than just a few days or even a week" [Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/). Nothing newer found. No timetable reported; *ESPN est.* 9 Nov, and the news-watch override puts him back 13 Nov at the earliest. Projected 35.2 (above our floor), 2026 34.1; current -2.0 (1), a small sample. Games 0 / 3; his first possible game is Sun 15 Nov at LAC. The starting role waits for him. Cost: a healthy player's spot for about a week, for at most one game next week.
- The add/drop call is yours, or the council's (`/council`).

## Since the last Injury Watch

Against this morning's `docs/analysis/20261108-injury-watch.md` (07:44 UTC).

- **New long absence: Jalen Duren (ours).** *ESPN est.* moved from 9 to 24 Nov after Detroit set a new two-week re-evaluation [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/). DET joins the team list (27 absences on 16 teams, from 26 on 15).
- **Pickups:** joined Aday Mara (our drop this morning, now on waivers) and Daniss Jenkins (DET, opened by Duren). None left. Desmond Bane moved from out to day-to-day.
- **Our five lowest:** Mara (24.4) left the roster, so Duren (33.5) is back in and the floor rose from 30.8 to 33.5.
- **Back soon:** joined Norman Powell (no timetable reported; *ESPN est.* 11 Nov) and Mitchell Robinson (illness; no timetable reported; *ESPN est.* 8 Nov). Nic Claxton and Jalen Smith left: both are off ESPN's feed, and Claxton was set to debut Sunday vs PHI [Basketnews, 8 Nov](https://basketnews.com/news-259075-nic-claxton-set-to-make-bulls-debut-star-guard-out-for-game-vs-76ers.html).
- **Off the feed:** Claxton, Jalen Smith, Joel Embiid, Joan Beringer, Tobe Awaka, Isaac Jones and Elijah Harkless.
- **New on the feed:** Powell and Robinson, plus three short listings outside our targets, all *ESPN est.* 8–10 Nov (see *Every injury*).
- **Status changes:** nine players moved from out to day-to-day, among them Bane (*ESPN est.* 10 Nov), Deandre Ayton (questionable Mon at DET; *ESPN est.* 9 Nov) [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/deandre-ayton-injury-wont-return-saturday-538066) and Robert Williams III (a rest day; *ESPN est.* 10 Nov) [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs). One moved from day-to-day to out. Details are in *Every injury*.
- **Ours:** Kawhi (no return date reported; *ESPN est.* 23 Nov) and Barnes (day-to-day, questionable Monday; *ESPN est.* 9 Nov) are unchanged [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process) [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game).

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Trey Murphy III 29.4 (L7 34.5), Isaiah Hartenstein 29.6 (L7 31.0), Daniel Gafford 30.1 (L7 24.7), P.J. Washington 30.8 (L7 37.3), Jalen Duren 33.5 (L7 —). A pickup at or above **33.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Desmond Bane** (day to day, ESPN est. back 10 Nov) | ORL | Paolo Banchero (22 Nov) | 6 | 36.0 | +6.0 | **32.7** | 27.8 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | Free agent | 90% | 0 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 8 | 34.2 | +6.8 | **30.1** | 30.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 40% | 0 / 3 |
| **Spencer Jones** | DEN | Julian Strawther (29 Nov) | 1 | 21.0 | — | **30.0** | 30.0 | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 0% | 0 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 7 | 22.7 | +9.7 | **29.9** | 24.4 | 31.8 (4) | 27.0 (8) | 24.4 (10) | Waivers | 18% | 0 / 4 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (10 Nov) | 7 | 30.0 | +4.6 | **29.4** | 29.4 | 26.0 (2) | 28.4 (5) | 29.4 (7) | Free agent | 13% | 1 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 10 | 25.7 | +5.4 | **28.8** | 28.7 | 28.5 (4) | 28.2 (9) | 28.7 (11) | Free agent | 34% | 0 / 3 |
| **Jamal Shead** | TOR | Kawhi Leonard (23 Nov) | 7 | 23.7 | +3.7 | **27.3** | 23.7 | 30.8 (4) | 27.3 (7) | 23.7 (9) | Free agent | 3% | 0 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 7 | 30.7 | +7.2 | **25.3** | 25.9 | 18.8 (4) | 25.3 (7) | 25.9 (9) | Free agent | 12% | 0 / 4 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 7 | 27.3 | +7.0 | **24.6** | 20.9 | 28.0 (4) | 21.8 (8) | 20.9 (10) | Free agent | 30% | 0 / 4 |
| **Jordan Goodwin** (out, ESPN est. back 09 Nov) | PHX | Mark Williams (03 Feb) | 5 | 18.8 | — | **24.4** | 24.4 | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% | 0 / 4 |
| **Collin Murray-Boyles** | TOR | Kawhi Leonard (23 Nov) | 7 | 23.1 | +4.1 | **24.0** | 24.4 | 29.2 (4) | 24.3 (7) | 24.4 (9) | Free agent | 11% | 0 / 4 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 22.0 | +6.0 | **23.0** | 23.3 | 27.2 (4) | 23.6 (8) | 23.3 (10) | Free agent | 5% | 0 / 4 |
| **Daniss Jenkins** | DET | Jalen Duren (24 Nov) | 6 | 25.7 | +7.2 | **20.7** | 20.8 | 8.0 (2) | 20.7 (6) | 20.8 (8) | Free agent | 3% | 1 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (10 Nov) | 5 | 19.0 | — | **20.6** | 20.6 | 30.3 (3) | 20.6 (5) → 25.8 (4) | 20.6 (5) → 25.8 (4) | Free agent | 1% | 1 / 3 |
| **Jarace Walker** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 24.1 | +5.1 | **20.6** | 19.1 | 22.2 (4) | 23.4 (8) | 19.1 (10) | Free agent | 1% | 0 / 4 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (10 Nov) | 8 | 24.4 | — | **20.5** | 20.5 | 23.0 (3) → 35.0 (2) | 21.7 (6) → 26.2 (5) | 20.5 (8) → 23.6 (7) | Free agent | 1% | 1 / 3 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov) | 8 | 21.1 | — | **20.5** | 20.5 | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% | 0 / 3 |

### Notes

- **Desmond Bane (ORL):** L7 28.0 (3) against a season of 27.8, not 5+ off [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/).
  - Ruled out Saturday at GSW with an illness; his next chance is Tue 10 Nov against SAC [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/). ESPN now lists him day-to-day; no timetable reported; *ESPN est.* 10 Nov.
  - **Role:** starter. The +6.0 minutes come with Banchero out (4–6 weeks from 24 Oct) [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html), so they should shrink when Banchero returns, about 21 Nov at the earliest. We dropped Bane on 3 Nov for Gafford (`council/roster.csv`).
- **Christian Braun (DEN):** L7 22.7 (3) against a season of 30.1, more than 5 under. The reason is shooting: 6 points on 2-of-8 (0-of-4 from three) in 29 minutes Saturday, his lowest-scoring game of the season [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-passive-performance-in-win/).
  - **Role:** starter. RotoWire: he "should remain a permanent starter", but with Spencer Jones back "playing in excess of 30 minutes every night could be a stretch" [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-passive-performance-in-win/).
  - **Does a return end it?** Strawther (about 29 Nov) is a bench wing; no source ties Braun's start to him [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html).
- **Spencer Jones (DEN):** one game, a small sample. Season debut Saturday: 13 points (5-of-6, 3-of-3 from three) and 6 rebounds in 21 minutes off the bench [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/). The "minutes cap" was RotoWire's expectation, not a team figure [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/). His role does not depend on Strawther.
- **Aday Mara (OKC):** L7 31.8 (4) against a season of 24.4, more than 5 above: his starts [AP via Yahoo, 7 Nov](https://sports.yahoo.com/articles/shai-gilgeous-alexander-okc-thunder-033415032.html).
  - He started Saturday vs WSH, his second career start, with 18 points, 8 rebounds and 3 blocks [AP via Yahoo, 7 Nov](https://sports.yahoo.com/articles/shai-gilgeous-alexander-okc-thunder-033415032.html). OKC went bigger, and McCain went back to the bench [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jared-mccain-news-returns-to-bench-saturday-538052).
  - Jaylin Williams (back spasms) has missed three straight; his next chance is Tue 10 Nov at POR; no timetable reported; *ESPN est.* 10 Nov [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/). His return would likely end the starts (inference). Holmgren's absence keeps the backup minutes.
  - We dropped him this morning for Anthony Black; he is on waivers.
- **Derrick Jones Jr. (LAC):** L7 26.0 (2) against 29.4, not 5+ off, and 2 games is a small sample [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans).
  - **Role:** starter since returning from knee soreness on 4 Nov (37 minutes) [NBC, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/derrick-jones-jr-knee-absent-from-injury-report). He started the Clippers' last game, and Kobe Sanders is a top bench option [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans).
  - **Does a return end it?** Ingram and Beal are both out with no timetable reported [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans), so the gain holds for now.
- **Aaron Wiggins (ATL):** L7 28.5 (4) against 28.7, not 5+ off [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653).
  - **Role:** bench: 29 minutes, the most of Atlanta's reserves, and 15 points in Wednesday's win [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653).
  - **Does a return end it?** Gueye is a big with no re-evaluation result [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html); no source ties Wiggins's minutes to him. Jalen Johnson's return on 7 Nov [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury) is likelier to trim them (inference).
- **Jamal Shead (TOR):** L7 30.8 (4) against a season of 23.7, more than 5 above: starts with Quickley and Barnes out [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl).
  - He started Friday at MIL with 10 points and a career-high 16 assists in 34 minutes [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl) [Raptors Republic, 6 Nov](https://raptorsrepublic.com/2026/11/06/quick-reaction-raptors-121-bucks-107/).
  - **Does a return end it?** Quickley and Barnes are both questionable for Mon 9 Nov vs MEM [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game); either one back should end the start (inference). Without them he is a bench guard (1 start in the 7 games without Kawhi).
- **Ja'Kobe Walter (TOR):** L7 18.8 (4) against a season of 25.9, more than 5 under. The reason is shooting: 2-of-12 (1-of-7 from three) in 29 minutes Friday, graded C- [Raptors Republic, 6 Nov](https://raptorsrepublic.com/2026/11/06/quick-reaction-raptors-121-bucks-107/). He starts in Kawhi's place [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl), and Kawhi's return ends it.
- **Jared McCain (OKC):** L7 28.0 (4) against a season of 20.9, more than 5 above: minutes. He has played 25+ minutes in six straight, scored 21 in his 6 Nov start [NBC, 6 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-06/jared-mccain-drops-21-points-in-lopsided-win), and went back to the bench Saturday [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jared-mccain-news-returns-to-bench-saturday-538052).
- **Jordan Goodwin (PHX):** L7 13.0 (1) is one game, noise: he left it after 10 minutes with the calf injury. Out Saturday vs HOU, his third straight miss (right calf); no timetable reported; *ESPN est.* 9 Nov [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jordan-goodwin-calf-downgraded-to-out-saturday). His bench role is not tied to Mark Williams.
- **Collin Murray-Boyles (TOR):** L7 29.2 (4) against 24.4, under 5 off. He started Friday with a season-high 19 points, 7 rebounds and 4 steals in 34 minutes [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/collin-murray-boyles-posts-19-7-2-4-1-line-vs-bucks). The start came with Barnes out [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl).
- **Quenton Jackson and Jarace Walker (IND):** L7 27.2 (4) against 23.3, and 22.2 (4) against 19.1; neither 5+ off. T.J. McConnell (hamstring) was cleared to make his season debut Saturday in Mexico City, and Haliburton stayed home, "making great progress", with no timetable reported (*ESPN est.* 13 Nov) [Yahoo, 6 Nov](https://sports.yahoo.com/articles/why-tyrese-haliburton-didnt-trip-223312624.html) [Roundtable via Yahoo, Nov](https://sports.yahoo.com/articles/pacers-still-no-timeline-tyrese-203626335.html). Those guard returns, not Furphy's or Sheppard's, decide Jackson's minutes (inference).
- **Daniss Jenkins (DET):** L7 8.0 (2) against 20.8 is 2 games, noise. He had 5 points, 4 turnovers in 21 minutes on 4 Nov, and RotoWire calls him "a fringe option in deeper formats" behind Cunningham [CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-struggles-off-bench/). Duren's minutes go to Paul Reed at center [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/), not to a guard.
- **Leaky Black (SAC):** L7 30.3 (3) against 20.6, more than 5 above: a 40-minute start for the ill De'Andre Hunter on 6 Nov (12 points, 4-of-7 from three) [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/leaky-black-plays-40-minutes-against-the-spurs). Hunter is no longer on ESPN's injury feed, and his return should cut it.
- **Kobe Sanders (LAC):** a top bench option [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). L7 23.0 (3) → 35.0 (2); the B figure is a small sample.
- **Trevon Brazile (DEN):** the backup four behind Aaron Gordon; Spencer Jones's return threatens his minutes [Yahoo, Nov](https://sports.yahoo.com/articles/nuggets-better-options-cutting-trevon-160004870.html).

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 09 Nov | 1 | 41.5 | — | — | 41.5 (2) → 68.0 (1) | 24.7 | 22.5 | Free agent | 15% | 1 / 4 |
| **Desmond Bane** | ORL | Illness | 10 Nov | 2 | 27.8 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | 38.2 | 36.9 | Free agent | 90% | 0 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 12 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 1 / 4 |
| **Norman Powell** | CHI | Right Shoulder Inflammation | 11 Nov | 3 | 26.2 | 13.5 (2) → 23.0 (1) | 26.8 (6) → 31.4 (5) | 26.2 (8) → 29.4 (7) | 36.0 | 33.0 | Free agent | 79% | 1 / 3 |
| **Kon Knueppel** | CHA | Left Hamstring Strain | 09 Nov | 1 | -2.0 | -2.0 (1) | -2.0 (1) | -2.0 (1) | 35.2 | 34.1 | Free agent | 87% | 0 / 3 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 2 | 26.3 | — | 23.0 (1) | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 0 / 3 |
| **Deandre Ayton** | WSH | Leg | 09 Nov | 1 | 16.9 | 19.0 (4) | 16.0 (8) | 16.9 (10) | 25.3 | 31.6 | Free agent | 10% | 0 / 4 |
| **Keegan Murray** | SAC | Left Ankle | 08 Nov | 0 | 12.0 | — | — | 12.0 (2) | 29.3 | 31.6 | Free agent | 32% | 1 / 3 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 09 Nov | 1 | 14.2 | — | 8.3 (3) | 14.2 (5) | 30.6 | 27.1 | Free agent | 10% | 0 / 4 |
| **Mitchell Robinson** | BOS | Illness | 08 Nov | 0 | 17.2 | 15.7 (3) | 17.0 (6) | 17.2 (8) | 30.3 | 28.2 | Free agent | 13% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 1 | — | — | — | — | 30.1 | 28.0 | Free agent | 44% | 0 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 11 Nov | 3 | 15.0 | — | 18.0 (3) | 15.0 (4) | 30.0 | 22.2 | Free agent | 29% | 1 / 2 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 09 Nov | 1 | 18.6 | — | 18.8 (4) | 18.6 (5) | 25.6 | 28.3 | Free agent | 2% | 0 / 4 |
| **Robert Williams III** | POR | Rest | 10 Nov | 2 | 28.1 | 30.3 (3) | 30.2 (5) | 28.1 (7) | 26.9 | 26.6 | Free agent | 5% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 2 | — | — | — | — | — | 28.1 | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 4 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 1 / 4 |
| **Isaiah Jackson** | LAC | Left Groin Soreness | 10 Nov | 2 | 26.8 | 20.3 (3) | 26.0 (6) | 26.8 (8) | 20.6 | 20.9 | Free agent | 6% | 1 / 3 |
| **Jock Landale** | ATL | Left Hip | 09 Nov | 1 | 16.4 | — | 12.0 (5) → 15.0 (4) | 16.4 (7) → 19.2 (6) | — | 25.8 | Free agent | 0% | 0 / 3 |
| **Isaiah Stewart** | MEM | Right Knee Bruise | 09 Nov | 1 | 22.9 | 21.5 (2) | 25.5 (6) | 22.9 (7) | 25.3 | 25.1 | Free agent | 4% | 0 / 4 |

### Notes

- **Yves Missi (NO):** left knee bone bruise; week-to-week with no timetable as of 5 Nov [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773), and out Sunday at LAC [NBA.com, 7 Nov](https://www.nba.com/pelicans/news/pelicans-vs-clippers-injury-report-game-preview-11-8-2026). No timetable reported; *ESPN est.* 9 Nov; the news-watch override says 12 Nov at the earliest. His current 41.5 rests on one 68-FP game after a dropped short game: a small sample. Derik Queen may start while he is out [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/).
- **Desmond Bane (ORL):** see the pickup notes [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/).
- **Jusuf Nurkic (UTAH):** partial plantar plate tear (second toe, right foot). On 6 Nov he began on-court work and will be re-evaluated in two weeks, about 20 Nov [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html) [KSL, 6 Nov](https://sports.ksl.com/nba/utah-jazz/jusuf-nurkic-utah-jazz/578803). *ESPN est.* 20 Nov. A re-evaluation is not a return; Jaxson Hayes and Mo Bamba hold the center minutes.
- **Norman Powell (CHI):** see the shortlist. Right shoulder inflammation, next chance Wed 11 Nov [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/norman-powell-shoulder-out-isaac-okoro-to-start); no timetable reported; *ESPN est.* 11 Nov.
- **Kon Knueppel (CHA):** see the shortlist. Left hamstring strain [CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-with-hamstring-strain/) [Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/); no timetable reported; *ESPN est.* 9 Nov (override 13 Nov).
- **Jalen Suggs (ORL):** mild right knee bone bruise, re-evaluated two weeks from 26 Oct, about 9 Nov [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html). Out Saturday at GSW [SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm); no result yet. *ESPN est.* 10 Nov. No minutes limit reported.
- **Deandre Ayton (WSH):** left lower-leg (calf) injury Saturday vs OKC, did not return. RotoWire: questionable for Mon 9 Nov at DET [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/deandre-ayton-injury-wont-return-saturday-538066) [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday). No timetable reported; *ESPN est.* 9 Nov. Healthy, he is a bench player.
- **Keegan Murray (SAC):** left ankle capsulitis, re-evaluated 10–14 days from 26 Oct, so 5–9 Nov [CBS/RotoWire, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/kings-keegan-murray-to-be-re-evaluated-in-10-to-14-days/). No result reported; *ESPN est.* 8 Nov, likely early.
- **Scotty Pippen Jr. (MEM):** lumbar disc herniation, out Friday vs OKC; Iisalo calls it day-to-day or week-to-week [SI, 6 Nov](https://si.com/nba/grizzlies/onsi/stewart-pippen-jr-s-status-for-grizzlies-thunder-injuries-odds-how-to-watch-01m6smnz7y2r). No timetable reported; *ESPN est.* 9 Nov.
- **Mitchell Robinson (BOS):** a late downgrade to questionable Sunday at MIL with an illness [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday). No timetable reported; *ESPN est.* 8 Nov.
- **Tobias Harris (SA):** left calf strain, out 6 and 7 Nov with no timetable [Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip); Keldon Johnson and Dylan Harper take the minutes [FantasyPros, 6 Nov](https://www.fantasypros.com/nba/news/618154/tobias-harris-calf-remains-out-friday.php). No timetable reported; *ESPN est.* 9 Nov; override 14 Nov at the earliest.
- **Egor Demin (BKN):** right leg bone bruise, "progressing", out Saturday and Sunday, re-evaluated next week; Chaney Johnson starts until he returns [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/demin-leg-progressing-out-at-least-two-games). No timetable reported; *ESPN est.* 11 Nov.
- **Jaylon Tyson (CLE):** right ankle sprain, out Saturday vs NYK [Yardbarker, 7 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_knicks_cavaliers_will_josh_hart_jarrett_allen_play/s1_17615_44530030); Atkinson calls it short-term [Cavs Nation](https://cavsnation.com/news/cavs-news-kenny-atkinson-speaks-up-on-jaylon-tysons-injury-status). Next chance Mon 9 Nov at CHA. No timetable reported; *ESPN est.* 9 Nov.
- **Robert Williams III (POR):** not hurt. He sat Saturday vs SAS for rest, the second night of a back-to-back [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs). *ESPN est.* 10 Nov.
- **Maxime Raynaud (SAC):** right patellar subluxation; the re-evaluation is now "next week" (9–15 Nov) [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap). *ESPN est.* 10 Nov, probably early. He is Sabonis's backup at center.
- **Dereck Lively II (DAL):** right foot surgery; not practising, and "his return still doesn't seem close" [The Smoking Cuban, Nov](https://thesmokingcuban.com/dereck-lively-ii-extended-absence-putting-his-mavericks-future-in-jeopardy). No timetable reported; *ESPN est.* 12 Nov, likely early.
- **Isaiah Jackson (LAC):** left groin soreness, out Sunday vs NOP [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-jackson-groin-out-sunday-vs-pelicans); Brook Lopez and Baba Miller take the center minutes. No timetable reported; *ESPN est.* 10 Nov.
- **Jock Landale (ATL):** left hip strain, four straight games missed; next chance Mon 9 Nov vs LAL [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-out-again-saturday-537992). No timetable reported; *ESPN est.* 9 Nov.
- **Isaiah Stewart (MEM):** right knee bone bruise; Iisalo: "avoided anything major" [Yahoo, 5 Nov](https://sports.yahoo.com/articles/grizzlies-isaiah-stewart-avoided-anything-001100081.html). Out Friday; next chance Mon 9 Nov at TOR [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-isaiah-stewart-ruled-out-for-friday/). No timetable reported; *ESPN est.* 9 Nov.

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 33.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 1 | 30.1 (30.5) | 28.0 (63) | Free agent | 44% | 0 / 4 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 10 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 1 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 2 | — (—) | 28.1 (74) | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 4 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 12 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 1 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 21 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 1 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 55 | 38.8 (32.4) | 41.6 (38) | Free agent | 29% | 0 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 55 | 36.9 (27.7) | 32.3 (32) | Free agent | 36% | 0 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 87 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 114 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 0 / 3 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 145 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 2 |

### Notes

- **Tobias Harris, Maxime Raynaud, Dereck Lively II and Jusuf Nurkic:** see *Injured and available, back soon* [Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip) [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap) [The Smoking Cuban, Nov](https://thesmokingcuban.com/dereck-lively-ii-extended-absence-putting-his-mavericks-future-in-jeopardy) [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html).
- **Brandon Ingram (Melbourne poopoo; also out behind the LAC pickups):** right heel surgery and a partial Achilles tear. He had a G League stint from 31 Oct [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-returns-from-g-league-assignment-537174) and was out Sunday vs NOP, with "no timetable for his return" [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 10 Nov.
- **Bradley Beal (LAC):** right knee injury management, out Sunday, has not played; no timetable reported [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 29 Nov.
- **Jimmy Butler III (GS):** torn right ACL; Kerr expects him back around the one-year mark, so about Jan–Feb 2027, with no firm date [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/) [Bleacher Report, 16 Oct](https://bleacherreport.com/articles/25512071-jimmy-butler-teases-target-date-return-knee-injury-updates-warriors-contract-talks). *ESPN est.* 2 Jan.
- **Kristaps Porzingis (GS):** said on 6 Nov he is stepping away from basketball to focus on his health; he will not be with the team "for the immediate future" [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball) [Forbes, 7 Nov](https://forbes.com/sites/bryantoporek/2026/11/07/why-the-warriors-arent-parting-ways-with-kristaps-porziis-yet). No timetable reported; *ESPN est.* 2 Jan. Not a stash.
- **Mark Williams (PHX):** torn left labrum, repaired 10 Sep; at least five months, so about mid-Feb [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery) [SI](https://www.si.com/nba/suns/onsi/insider-reveals-when-phoenix-suns-center-mark-williams-should-return-from-injury). *ESPN est.* 3 Feb.
- **Shaedon Sharpe (POR):** right meniscus surgery in late Aug, re-evaluation in six months, about late Feb (unchanged since 2 Nov) [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next). *ESPN est.* 2 Mar.
- **Donte DiVincenzo (MIN):** torn right Achilles, surgery 26 Apr, targeting a late-season return (unchanged since 2 Nov) [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214). *ESPN est.* 2 Apr.

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Left Groin Soreness; ESPN est. back 09 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Jalen Duren:** cleared for on-court activity on 8 Nov but not for games. He will be re-evaluated in two weeks and stays inactive for at least that long (The Athletic's Hunter Patterson, via RotoWire) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work) [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/detroit-pistons-jalen-duren-injury-update-november-8/ddrysdale/detroit-pistons/11/08/2026/505667/). Two weeks from 8 Nov is about 22 Nov, and a re-evaluation is not a return. *ESPN est.* 24 Nov. Paul Reed stays the starting center [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work).
  - Form (`form.py`): season 33.5 (2) → 44.0 (1), L7 —, L15 —, L30 33.5 (2) → 44.0 (1), projected 42.2, rate 44.1. All of it is a small sample.
- **Scottie Barnes:** missed Friday at MIL with a left groin injury [Heavy, 6 Nov](https://heavy.com/sports/nba/toronto-raptors/scottie-barnes-injury-update-bucks/) and is questionable for Mon 9 Nov vs MEM [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game). No timetable reported; *ESPN est.* 9 Nov.
  - Form (`form.py`): season 45.9 (8) → 50.7 (7), L7 44.3 (3), L15 45.2 (6) → 51.8 (5), L30 45.9 (8) → 50.7 (7), projected 43.7, rate 48.6.
- **Kawhi Leonard:** nothing newer than 3 Nov, when Toronto said his knee treatment was done and the return-to-play process had begun, with an update in a week (about 10 Nov); ESPN puts his earliest game at 11 Nov vs BOS [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process) [NBA.com, 3 Nov](https://www.nba.com/news/kawhi-leonards-knee-swelling-has-been-treated-and-hell-start-return-to-play-process-raptors-say). He was out again Friday at MIL [Yahoo, 6 Nov](https://sports.yahoo.com/articles/raptors-vs-bucks-injury-report-140945565.html). No return date reported; *ESPN est.* 23 Nov.
  - Form (`form.py`): season 40.0 (2), L7 —, L15 —, L30 40.0 (2), projected 45.8, rate 41.7. A small sample.
- **Who should hold the IR slot, Duren or Kawhi** [ESPN Fan Support: Players on IR](https://support.espn.com/hc/en-us/articles/115003849911-Players-on-Injured-Reserve-IR):
  - **Eligibility:** both qualify. ESPN's help centre says only players tagged (IR), (IL) or (O) can go in the IR slot, and a player in it who loses the OUT tag makes the roster invalid until it is fixed [ESPN Fan Support: Players on IR](https://support.espn.com/hc/en-us/articles/115003849911-Players-on-Injured-Reserve-IR) [ESPN Fan Support: moving players on and off IR](https://support.espn.com/hc/en-us/articles/115003860512-Move-a-Player-On-or-Off-Injured-Reserve-IR). Those pages are written for football, but ESPN took both Duren (25 Oct) and Kawhi (2 Nov) into our basketball IR slot as OUT players (`council/roster.csv`). Both are listed OUT today.
  - **Who returns later:** ESPN's estimates are a day apart (Kawhi 23 Nov, Duren 24 Nov), but the reports are not. Duren's next check is about 22 Nov and he is ruled inactive until then. Kawhi's update is due about 10 Nov and his earliest game is 11 Nov [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process). **Duren is the likelier to return later**, so he is the better IR holder, with Kawhi on the bench, ready to activate without forcing a move. The swap costs no add.
  - **Pending trade:** if the Kawhi + Murphy for Jalen Brunson offer (expires about 03:00 UTC Tue 10; `docs/analysis/20261108-slump-watch.md`) is accepted, Duren takes the slot anyway.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ajay Mitchell | PG/SG | 7 | 28.3 | +3.6 | 7 | **36.6** | 29.7 | 34.0 (4) | 37.6 (8) | 34.5 (10) | Lauri Birds | 72% |
| Aday Mara | C | 7 | 22.7 | +9.7 | 2 | **29.9** | 11.7 | 31.8 (4) | 27.0 (8) | 24.4 (10) | Waivers | 18% |
| Jared McCain | PG/SG | 7 | 27.3 | +7.0 | 4 | **24.6** | 12.3 | 28.0 (4) | 21.8 (8) | 20.9 (10) | Free agent | 30% |
| Bennett Stirtz | PG | 7 | 23.7 | +19.0 | 0 | **19.7** | 2.0 | 25.2 (4) | 18.1 (8) | 14.4 (10) | Free agent | 1% |
| Kenrich Williams | SF | 7 | 23.4 | +16.8 | 7 | **18.3** | 7.0 | 19.5 (4) | 16.8 (8) | 14.9 (10) | Free agent | 1% |

**Reported timeline:**

- **Chet Holmgren:** small right patellar tendon tear, treated 30 Oct, out at least 8–10 weeks, so about 25 Dec–8 Jan; no newer update found [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear). *ESPN est.* 2 Jan.
- **Jalen Williams** (fractured left fibula, surgery 28 Oct) and **Cason Wallace** (left shoulder surgery): both to be re-evaluated before the end of the regular season (unchanged since 2 Nov) [Yahoo, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html) [AP via AJC, 31 Oct](https://www.ajc.com/news/2026/10/chet-holmgren-out-at-least-2-months-with-knee-injury-and-cason-wallace-has-shoulder-surgery/). *ESPN est.* 2 Mar for both.
- **Jaylin Williams** (not in the table): lower back spasms, three straight games missed, next chance Tue 10 Nov at POR; no timetable reported; *ESPN est.* 10 Nov [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/). His return decides Mara's starts.

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 10 | 32.2 | +3.6 | 10 | **40.7** | 33.7 | 47.5 (4) | 42.0 (8) → 48.3 (7) | 40.7 (10) → 45.4 (9) | **us** | 93% |
| Brandin Podziemski | PG/SG | 8 | 34.0 | +3.1 | 8 | **35.9** | 30.8 | 35.0 (4) | 36.1 (7) | 35.9 (8) | Matt Wright's Foxies | 76% |
| Brandon Williams | PG/SG | 9 | 17.8 | — | 1 | **20.3** | — | 24.3 (3) | 21.1 (7) | 20.3 (9) | Free agent | 2% |
| Georges Niang | PF | 10 | 20.6 | — | 2 | **16.9** | — | 19.8 (4) | 17.9 (8) | 16.9 (10) | Free agent | 1% |
| Will Richard | SG/SF | 10 | 17.1 | — | 3 | **12.5** | — | 13.0 (4) | 12.0 (8) | 12.4 (10) | Free agent | 0% |

**Reported timeline:**

- **Jimmy Butler III:** torn right ACL; Kerr expects him back around the one-year mark, about Jan–Feb 2027, with no firm date [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/). *ESPN est.* 2 Jan.
- **Kristaps Porzingis:** stepping away from basketball for his health (6 Nov); no timetable reported [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball). *ESPN est.* 2 Jan.
- **Moses Moody:** left patellar tendon surgery in March; hoped back in December or January, with no official timetable [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/) [FantasyPros](https://www.fantasypros.com/nba/news/614410/moses-moody-knee-could-return-december-or-january.php). *ESPN est.* 1 Dec.

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 02 Jan | 25.7 | 7.0 | Free agent |

Last 9 games: 2 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Micah Potter | C | 1 | 14.0 | +7.2 | 0 | **22.0** | 3.2 | 14.0 (2) | 7.2 (4) | 7.0 (5) | Free agent | 0% |
| Chris Youngblood | SG | 2 | 20.5 | +11.8 | 0 | **18.0** | 4.3 | 11.8 (4) | 9.8 (5) | 9.8 (5) | Free agent | 0% |
| Yang Hansen | C | 2 | 14.5 | +6.5 | 0 | **14.0** | 8.2 | 8.7 (3) | 11.0 (5) | 10.2 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | +5.0 | 0 | **12.0** | -2.0 | — | — | — | — | 0% |
| Branden Carlson | C | 1 | 12.0 | +5.7 | 0 | **7.0** | 5.3 | 5.0 (2) | 5.8 (4) | 5.8 (4) | Free agent | 0% |

**Reported timeline** (no pickup or player of ours here; not re-checked except where noted):

- **Ja Morant:** Grade 2 left hamstring strain, re-evaluation four weeks from 30 Oct, about 27 Nov (unchanged since 2 Nov) [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain). *ESPN est.* 1 Dec.
- **Shaedon Sharpe:** right meniscus surgery, re-evaluation about late Feb (unchanged since 2 Nov) [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next). *ESPN est.* 2 Mar.
- **Vit Krejci:** hurt on 5 Nov vs PHX; ClutchPoints reported an ankle injury, RotoBaller a lower-left-leg fracture. No timetable reported [ClutchPoints, 5 Nov](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-portland-loses-guard-to-painful-injury-in-win-vs-suns) [RotoBaller, 5 Nov](https://www.rotoballer.com/?p=1984362). *ESPN est.* 2 Jan.

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 6 | 35.0 | +8.8 | 6 | **45.0** | 25.8 | 45.7 (3) | 36.5 (8) | 37.3 (10) | Cream Abdul-Yammar | 80% |
| Jaden McDaniels | SF/PF | 6 | 35.5 | +3.8 | 6 | **37.2** | 36.8 | 35.0 (3) | 36.1 (8) | 37.0 (10) | Melbourne poopoo | 89% |
| LaMelo Ball | PG | 6 | 29.3 | +4.3 | 6 | **37.0** | 30.8 | 43.0 (3) | 34.2 (8) | 34.5 (10) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 6 | 15.0 | +7.0 | 0 | **24.0** | 9.0 | 21.0 (3) | 21.1 (8) | 18.0 (10) | Free agent | 3% |
| Trey Lyles | PF | 6 | 21.0 | +7.0 | 0 | **17.7** | 11.0 | 22.7 (3) | 16.1 (8) | 15.0 (10) | Free agent | 0% |

**Reported timeline** (no pickup or player of ours here):

- **Anthony Edwards (Melbourne poopoo):** right knee arthroscopic debridement on 29 Oct, expected to miss up to two months (unchanged since 2 Nov) [Yahoo (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html). *ESPN est.* 21 Dec.
- **Donte DiVincenzo:** torn right Achilles, targeting a late-season return (unchanged since 2 Nov) [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214). *ESPN est.* 2 Apr.

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |
| Jusuf Nurkic | Right Foot Strain | 20 Nov | 26.4 | 36.7 | Free agent |

Last 9 games: 5 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Lauri Markkanen (day to day, ESPN est. back 08 Nov) | SF/PF | 4 | 33.2 | +4.8 | 4 | **39.5** | 25.5 | 44.0 (3) | 33.2 (6) → 39.8 (5) | 32.5 (8) → 37.1 (7) | Lauri Birds | 90% |
| Ace Bailey | SF/PF | 5 | 33.0 | +5.8 | 5 | **21.8** | 38.8 | 17.3 (3) | 30.9 (7) | 29.3 (9) | Dr White Slong | 60% |
| Josh Okogie | SF | 5 | 22.2 | +9.2 | 0 | **15.8** | 3.3 | 18.7 (3) | 12.9 (7) | 11.2 (8) | Free agent | 0% |
| Josh Green | SG | 5 | 17.6 | +3.6 | 1 | **8.2** | 7.5 | 8.3 (3) | 8.0 (7) | 8.0 (7) | Free agent | 0% |

**Reported timeline:**

- **Jaren Jackson Jr. (Matt Wright's Foxies):** torn right MCL (26 Oct), at least six weeks, about 7–21 Dec (unchanged since 2 Nov) [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/). *ESPN est.* 14 Dec.
- **Jusuf Nurkic:** began on-court work; re-evaluated two weeks from 6 Nov, about 20 Nov [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html). *ESPN est.* 20 Nov.

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 8 | 30.5 | +8.5 | 8 | **33.4** | 20.0 | 34.0 (3) | 32.7 (6) | 33.1 (8) | Lauri Birds | 41% |
| Derrick Jones Jr. | SF/PF | 7 | 30.0 | +4.6 | 7 | **29.4** | 21.1 | 26.0 (2) | 28.4 (5) | 29.4 (7) | Free agent | 13% |
| Kobe Sanders | SG | 8 | 24.4 | — | 2 | **20.5** | — | 23.0 (3) → 35.0 (2) | 21.7 (6) → 26.2 (5) | 20.5 (8) → 23.6 (7) | Free agent | 1% |

**Reported timeline:**

- **Jordan Miller:** torn left rotator cuff, repaired 26 Aug, re-evaluation in about six months, so late Feb [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html); out Sunday [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 2 Mar.
- **Bradley Beal:** right knee injury management, out Sunday, has not played; no timetable reported [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 29 Nov.
- **Brandon Ingram (also out; Melbourne poopoo):** right heel surgery and partial Achilles tear; out Sunday with no timetable [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans) [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-returns-from-g-league-assignment-537174). *ESPN est.* 10 Nov. His debut would cut into Jones Jr.'s and Sanders's minutes (inference).

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 6 | 35.2 | +5.2 | 6 | **43.2** | 29.8 | 49.5 (4) | 41.5 (8) | 37.2 (10) → 40.4 (9) | Snow Time Lakers | 68% |

**Reported timeline** (no pickup or player of ours here):

- **Jamir Watkins:** torn left ACL in July, reconstructed; likely out for the season [RotoWire, Jul](https://www.rotowire.com/basketball/headlines/jamir-watkins-injury-undergoes-surgery-for-torn-acl-532251) [NBC, 30 Jul](https://www.nbcsports.com/fantasy/basketball/player-news/2026-07-30/jamir-watkins-tears-acl-during-summer-league). *ESPN est.* 2 Apr.
- **Justin Champagnie:** right foot fracture, surgery 28 Oct; the team hopes for a return by the All-Star break [NBA.com, 28 Oct](https://www.nba.com/news/washington-wizards-justin-champagnie-foot-surgery) [Roundtable, Oct](https://roundtable.io/sports/nba/wizards/players/wizards-justin-champagnie-undergoes-surgery-sidelined-long-term). *ESPN est.* 25 Feb.

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 9 | 22.0 | +6.0 | 1 | **23.0** | 26.0 | 27.2 (4) | 23.6 (8) | 23.3 (10) | Free agent | 5% |
| Jarace Walker | SF/PF | 9 | 24.1 | +5.1 | 2 | **20.6** | 6.0 | 22.2 (4) | 23.4 (8) | 19.1 (10) | Free agent | 1% |
| Jay Huff | C | 9 | 18.3 | — | 5 | **15.9** | — | 14.5 (4) | 17.8 (8) | 15.9 (9) | Free agent | 1% |
| Larry Nance Jr. | PF | 8 | 17.0 | +12.0 | 0 | **15.1** | -1.0 | 16.3 (3) | 17.3 (7) | 13.3 (9) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 14.9 | — | 1 | **14.2** | — | 18.2 (4) | 12.4 (8) | 14.2 (9) | Free agent | 0% |

**Reported timeline:**

- **Johnny Furphy:** torn right ACL (Feb 2026); the target is "the middle of the season", with no date (unchanged since 5 Nov) [Roundtable, 25 Sep](https://roundtable.io/sports/nba/pacers/news/pacers-give-johnny-furphy-acl-rehab-update-before-camp). *ESPN est.* 2 Jan.
- **Ben Sheppard:** full left meniscus repair on 28 Oct; Carlisle says months, "I don't know how many" [Forbes, 6 Nov](https://www.forbes.com/sites/tonyeast/2026/11/06/ben-sheppard-longer-absence-is-bad-news-for-indiana-pacers/). No timetable reported; *ESPN est.* 2 Jan.
- **Guards behind the pickups:** T.J. McConnell was cleared to debut Saturday; Tyrese Haliburton (Lauri Birds) has no timetable reported [Yahoo, 6 Nov](https://sports.yahoo.com/articles/why-tyrese-haliburton-didnt-trip-223312624.html) [Roundtable via Yahoo, Nov](https://sports.yahoo.com/articles/pacers-still-no-timeline-tyrese-203626335.html) (*ESPN est.* 13 Nov). Ivica Zubac, in our pending offer to Lauri Birds, is not on ESPN's injury feed.

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 7 | 38.0 | +7.0 | 7 | **44.7** | 30.0 | 48.5 (4) | 44.7 (7) | 41.4 (9) | Cream Abdul-Yammar | 91% |
| Desmond Bane (day to day, ESPN est. back 10 Nov) | SG/SF | 6 | 36.0 | +6.0 | 6 | **32.7** | 13.0 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | Free agent | 90% |
| Wendell Carter Jr. | C | 7 | 34.4 | +4.4 | 7 | **32.0** | 46.5 | 35.2 (4) | 32.0 (7) | 35.2 (9) | Dr White Slong | 55% |
| Jamal Cain | SF | 7 | 21.4 | +8.9 | 1 | **15.9** | -5.0 | 16.5 (4) | 15.9 (7) | 11.2 (9) | Free agent | 0% |
| Jase Richardson | SG | 7 | 25.0 | +11.0 | 7 | **15.4** | 14.5 | 15.8 (4) | 15.4 (7) | 15.2 (9) | Free agent | 1% |

**Reported timeline:**

- **Paolo Banchero (Dr White Slong):** low-grade right high-ankle sprain (23 Oct), 4–6 weeks from 24 Oct, so 21 Nov–5 Dec; he said "at least a month" [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html) [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182). Out Saturday at GSW [Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html). *ESPN est.* 22 Nov.
- **Desmond Bane and Jalen Suggs:** see *Injured and available, back soon*. Anthony Black (ours) is healthy [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping).

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 7 | 33.9 | +3.9 | 7 | **35.7** | 39.0 | 38.2 (4) | 35.7 (7) → 39.5 (6) | 36.4 (9) → 39.4 (8) | Dr White Slong | 82% |
| Immanuel Quickley (day to day, ESPN est. back 09 Nov) | PG/SG | 6 | 32.8 | +4.3 | 6 | **35.2** | 35.0 | 34.3 (3) | 35.2 (6) | 35.1 (8) → 37.7 (7) | Cream Abdul-Yammar | 77% |
| Jamal Shead | PG | 7 | 23.7 | +3.7 | 1 | **27.3** | 11.0 | 30.8 (4) | 27.3 (7) | 23.7 (9) | Free agent | 3% |
| Ja'Kobe Walter | SG | 7 | 30.7 | +7.2 | 7 | **25.3** | 28.0 | 18.8 (4) | 25.3 (7) | 25.9 (9) | Free agent | 12% |
| Collin Murray-Boyles | PF | 7 | 23.1 | +4.1 | 3 | **24.0** | 25.0 | 29.2 (4) | 24.3 (7) | 24.4 (9) | Free agent | 11% |

**Reported timeline:**

- **Kawhi Leonard (ours):** return-to-play since 3 Nov, update due about 10 Nov, earliest game 11 Nov [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process). No return date reported; *ESPN est.* 23 Nov.
- **Short absences behind the gains:** Scottie Barnes (ours; groin) and Immanuel Quickley (Cream Abdul-Yammar; hamstring) are questionable for Mon 9 Nov vs MEM [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game); no timetable reported; *ESPN est.* 9 Nov for both. Shead's and Murray-Boyles's 6 Nov starts came with both out [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl).

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 8 games: 6 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Duncan Robinson | SG/SF | 6 | 32.0 | +4.0 | 6 | **36.7** | 29.5 | 49.0 (2) | 36.7 (6) | 34.9 (8) | Team Nic Kerr | 59% |
| Paul Reed | PF/C | 6 | 29.3 | +7.8 | 6 | **33.3** | 33.5 | 30.5 (2) | 32.7 (6) | 32.9 (8) | Lauri Birds | 42% |
| Daniss Jenkins | PG | 6 | 25.7 | +7.2 | 1 | **20.7** | 21.0 | 8.0 (2) | 20.7 (6) | 20.8 (8) | Free agent | 3% |
| Ronald Holland II | SF/PF | 6 | 16.8 | +4.3 | 0 | **18.3** | 16.0 | 12.5 (2) | 18.3 (6) | 17.8 (8) | Free agent | 1% |
| Javonte Green | SF | 6 | 19.5 | +4.0 | 0 | **11.2** | 22.0 | 8.5 (2) | 11.2 (6) | 13.9 (8) | Free agent | 1% |

**Reported timeline:**

- **Jalen Duren (ours):** cleared for on-court work on 8 Nov, re-evaluated in two weeks (about 22 Nov), inactive until then [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/). *ESPN est.* 24 Nov. Paul Reed (Lauri Birds) stays the starting center [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work); a guard like Daniss Jenkins does not inherit those minutes (inference).

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin (out, ESPN est. back 09 Nov) | PG/SG | 5 | 18.8 | — | 0 | **24.4** | — | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% |

**Reported timeline:**

- **Mark Williams:** torn left labrum, repaired 10 Sep; at least five months, so about mid-Feb [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery). *ESPN est.* 3 Feb. Goodwin's guard minutes are not tied to him.

### PHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dominick Barlow | Back Fracture | 18 Nov | 23.7 | 22.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaylen Brown | SG/SF | 9 | 36.0 | +3.6 | 9 | **40.8** | 38.6 | 51.0 (3) | 41.0 (7) | 40.8 (9) | Snow Time Lakers | 100% |
| Dean Wade | PF | 8 | 25.6 | +4.1 | 4 | **19.5** | 16.3 | 14.0 (3) | 19.5 (8) | 19.5 (8) | Free agent | 1% |

**Reported timeline** (no pickup or player of ours here):

- **Dominick Barlow:** lumbar spine bone stress response; on 4 Nov Nurse said he needs at least 10–12 more days, so about 14–16 Nov [Inquirer, 4 Nov](https://www.inquirer.com/sixers/dominick-barlow-injury-update-76ers-lebron-james-joel-embiid-20261104.html) [Northeast Times, 5 Nov](https://northeasttimes.com/2026/11/05/sixers-injury-report-bona-barlow-embiid-next-three-games-november-2026/). *ESPN est.* 18 Nov.

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 9 | 36.8 | +6.2 | 9 | **39.3** | 30.4 | 42.7 (3) | 44.1 (7) | 38.9 (9) → 42.6 (8) | Team Nic Kerr | 86% |
| Dylan Cardwell | C | 2 | 14.0 | — | 0 | **21.5** | — | 21.5 (2) | 21.5 (2) | 21.5 (2) | Free agent | 0% |
| Leaky Black | SF | 5 | 19.0 | — | 1 | **20.6** | — | 30.3 (3) | 20.6 (5) → 25.8 (4) | 20.6 (5) → 25.8 (4) | Free agent | 1% |
| De'Andre Hunter | SF/PF | 8 | 31.2 | +3.6 | 8 | **19.5** | 23.9 | 11.0 (2) | 22.2 (6) | 19.4 (8) | Free agent | 6% |
| Jonathan Mogbo | PF | 4 | 17.2 | +4.7 | 0 | **13.2** | 11.3 | — | 18.3 (3) | 13.2 (4) | Free agent | 0% |

**Reported timeline:**

- **Ben Simmons:** torn right Achilles, repaired 20 Oct, out for the season (unchanged since 2 Nov) [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season). *ESPN est.* 1 Oct 2027.
- **Maxime Raynaud (also out):** right patellar subluxation; re-evaluation "next week" (9–15 Nov) [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap) [CBS/RotoWire, 26 Oct](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-to-be-re-evaluated-in-two-weeks-536198/). *ESPN est.* 10 Nov. His return takes backup-center minutes, not Leaky Black's wing minutes (inference).

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 8 | 34.2 | +6.8 | 8 | **30.1** | 23.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 40% |
| Spencer Jones | SF/PF | 1 | 21.0 | — | 0 | **30.0** | — | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 0% |
| Trevon Brazile | SF/PF | 8 | 21.1 | — | 1 | **20.5** | — | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% |
| Bryce Hopkins | SF | 6 | 16.2 | — | 2 | **10.2** | — | 17.5 (2) | 11.8 (5) | 10.2 (6) | Free agent | 0% |

**Reported timeline:**

- **Julian Strawther:** left knee sprain (14 Oct preseason), re-evaluation six weeks from mid-Oct, about 29 Nov [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html); out Saturday vs IND [Roundtable, 7 Nov](https://roundtable.io/sports/nba/nuggets/news/nuggets-vs-pacers-injury-report-tyrese-haliburton-demar-derozan-statuses). *ESPN est.* 29 Nov.
- Spencer Jones (hamstring) debuted Saturday [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/), which matters more to Braun's and Brazile's minutes than Strawther does. Jamal Murray (ours) is healthy.

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.7 | +5.4 | 0 | **28.8** | 19.2 | 28.5 (4) | 28.2 (9) | 28.7 (11) | Free agent | 34% |
| Zuby Ejiofor | PF | 6 | 12.3 | — | 0 | **15.5** | — | 22.5 (4) | 18.0 (5) | 15.5 (6) | Free agent | 0% |
| Jock Landale (out, ESPN est. back 09 Nov) | C | 6 | 14.7 | — | 0 | **14.8** | — | — | 12.0 (5) → 15.0 (4) | 16.4 (7) → 19.2 (6) | Free agent | 0% |

**Reported timeline:**

- **Mouhamed Gueye:** left foot fracture, surgery 14 Jul, re-evaluation in three to four months (mid-Oct to mid-Nov); no result reported [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html). *ESPN est.* 20 Nov.
- **Jock Landale:** see *Injured and available, back soon* [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-out-again-saturday-537992).

## Every injury

All 86 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 327 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 327 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 235 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 145 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 145 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 114 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 114 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 114 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 114 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 109 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 87 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 02 Jan | 55 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 55 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 55 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 55 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 55 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 55 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 43 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 36 | Matt Wright's Foxies |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 25 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 25 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 23 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 23 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 23 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 21 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 21 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 16 | **us** |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 15 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 14 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 12 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 12 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 10 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 10 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 10 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 5 | Lauri Birds |
| Thomas Sorber | OKC | Out | Knee | 13 Nov | 5 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 4 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 12 Nov | 4 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 4 | Free agent |
| Zach Collins | CHI | Out | Illness | 11 Nov | 3 | Free agent |
| Norman Powell | CHI | Out | Right Shoulder Inflammation | 11 Nov | 3 | Free agent |
| Mikel Brown Jr. | BKN | Out | Rest | 11 Nov | 3 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 11 Nov | 3 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 10 Nov | 2 | Free agent |
| Robert Williams III | POR | Day-To-Day | Rest | 10 Nov | 2 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 2 | Free agent |
| Josh Hart | NY | Day-To-Day | Ankle | 10 Nov | 2 | Dr White Slong |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 2 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 10 Nov | 2 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 2 | Free agent |
| Isaiah Jackson | LAC | Out | Left Groin Soreness | 10 Nov | 2 | Free agent |
| Grant Nelson | BKN | Day-To-Day | Left Knee | 10 Nov | 2 | — |
| Desmond Bane | ORL | Day-To-Day | Illness | 10 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 10 Nov | 2 | Melbourne poopoo |
| Adem Bona | PHI | Out | Back Sprain | 10 Nov | 2 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 09 Nov | 1 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 09 Nov | 1 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 09 Nov | 1 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 09 Nov | 1 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 09 Nov | 1 | Free agent |
| Scottie Barnes | TOR | Day-To-Day | Left Groin Soreness | 09 Nov | 1 | **us** |
| Sam Merrill | CLE | Day-To-Day | Right Elbow | 09 Nov | 1 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 09 Nov | 1 | — |
| Moussa Diabate | CHA | Day-To-Day | Quadriceps | 09 Nov | 1 | Team Nic Kerr |
| Luka Doncic | LAL | Out | Back Soreness | 09 Nov | 1 | Team Nic Kerr |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 09 Nov | 1 | Free agent |
| Keshon Gilbert | ATL | Day-To-Day | Left Knee Inflammation | 09 Nov | 1 | — |
| Jordan Goodwin | PHX | Out | Left Calf | 09 Nov | 1 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 09 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 09 Nov | 1 | Free agent |
| Jarrett Allen | CLE | Day-To-Day | Right Knee | 09 Nov | 1 | Dr White Slong |
| Isaiah Stewart | MEM | Out | Right Knee Bruise | 09 Nov | 1 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 09 Nov | 1 | Free agent |
| Immanuel Quickley | TOR | Day-To-Day | Right Hamstring | 09 Nov | 1 | Cream Abdul-Yammar |
| Grant Williams | CHA | Out | Right Hamstring | 09 Nov | 1 | Free agent |
| Dennis Schroder | CHA | Out | Thigh | 09 Nov | 1 | Free agent |
| Deandre Ayton | WSH | Day-To-Day | Leg | 09 Nov | 1 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 09 Nov | 1 | Free agent |
| Brandon Miller | CHA | Day-To-Day | Right Groin Soreness | 09 Nov | 1 | Matt Wright's Foxies |
| Asa Newell | ATL | Day-To-Day | Left Toe | 09 Nov | 1 | Free agent |
| Anthony Davis | WSH | Day-To-Day | Right Ankle Sprain | 09 Nov | 1 | Melbourne poopoo |
| Mitchell Robinson | BOS | Day-To-Day | Illness | 08 Nov | 0 | Free agent |
| Lauri Markkanen | UTAH | Day-To-Day | Right Wrist Sprain | 08 Nov | 0 | Lauri Birds |
| Keyonte George | UTAH | Day-To-Day | Illness | 08 Nov | 0 | Cream Abdul-Yammar |
| Keegan Murray | SAC | Out | Left Ankle | 08 Nov | 0 | Free agent |
| Gary Trent Jr. | MIL | Day-To-Day | Illness | 08 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-08 20:14 UTC.
- Research for this run (web, 8 Nov 2026, US time), plus carry-over links marked *unchanged since*:
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)
  - [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html)
  - [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/)
  - [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html)
  - [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans)
  - [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear)
  - [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/norman-powell-shoulder-out-isaac-okoro-to-start)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-out-sunday/)
  - [Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)
  - [Basketnews, 8 Nov](https://basketnews.com/news-259075-nic-claxton-set-to-make-bulls-debut-star-guard-out-for-game-vs-76ers.html)
  - [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/deandre-ayton-injury-wont-return-saturday-538066)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-passive-performance-in-win/)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)
  - [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/)
  - [AP via Yahoo, 7 Nov](https://sports.yahoo.com/articles/shai-gilgeous-alexander-okc-thunder-033415032.html)
  - [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jared-mccain-news-returns-to-bench-saturday-538052)
  - [NBC, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/derrick-jones-jr-knee-absent-from-injury-report)
  - [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653)
  - [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury)
  - [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl)
  - [Raptors Republic, 6 Nov](https://raptorsrepublic.com/2026/11/06/quick-reaction-raptors-121-bucks-107/)
  - [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game)
  - [NBC, 6 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-06/jared-mccain-drops-21-points-in-lopsided-win)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jordan-goodwin-calf-downgraded-to-out-saturday)
  - [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/collin-murray-boyles-posts-19-7-2-4-1-line-vs-bucks)
  - [Yahoo, 6 Nov](https://sports.yahoo.com/articles/why-tyrese-haliburton-didnt-trip-223312624.html)
  - [Roundtable via Yahoo, Nov](https://sports.yahoo.com/articles/pacers-still-no-timeline-tyrese-203626335.html)
  - [CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-struggles-off-bench/)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/leaky-black-plays-40-minutes-against-the-spurs)
  - [Yahoo, Nov](https://sports.yahoo.com/articles/nuggets-better-options-cutting-trevon-160004870.html)
  - [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)
  - [NBA.com, 7 Nov](https://www.nba.com/pelicans/news/pelicans-vs-clippers-injury-report-game-preview-11-8-2026)
  - [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/)
  - [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)
  - [KSL, 6 Nov](https://sports.ksl.com/nba/utah-jazz/jusuf-nurkic-utah-jazz/578803)
  - [CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-with-hamstring-strain/)
  - [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html)
  - [SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday)
  - [CBS/RotoWire, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/kings-keegan-murray-to-be-re-evaluated-in-10-to-14-days/)
  - [SI, 6 Nov](https://si.com/nba/grizzlies/onsi/stewart-pippen-jr-s-status-for-grizzlies-thunder-injuries-odds-how-to-watch-01m6smnz7y2r)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday)
  - [Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip)
  - [FantasyPros, 6 Nov](https://www.fantasypros.com/nba/news/618154/tobias-harris-calf-remains-out-friday.php)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/demin-leg-progressing-out-at-least-two-games)
  - [Yardbarker, 7 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_knicks_cavaliers_will_josh_hart_jarrett_allen_play/s1_17615_44530030)
  - [Cavs Nation](https://cavsnation.com/news/cavs-news-kenny-atkinson-speaks-up-on-jaylon-tysons-injury-status)
  - [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap)
  - [The Smoking Cuban, Nov](https://thesmokingcuban.com/dereck-lively-ii-extended-absence-putting-his-mavericks-future-in-jeopardy)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-jackson-groin-out-sunday-vs-pelicans)
  - [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-out-again-saturday-537992)
  - [Yahoo, 5 Nov](https://sports.yahoo.com/articles/grizzlies-isaiah-stewart-avoided-anything-001100081.html)
  - [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-isaiah-stewart-ruled-out-for-friday/)
  - [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-returns-from-g-league-assignment-537174)
  - [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/)
  - [Bleacher Report, 16 Oct](https://bleacherreport.com/articles/25512071-jimmy-butler-teases-target-date-return-knee-injury-updates-warriors-contract-talks)
  - [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball)
  - [Forbes, 7 Nov](https://forbes.com/sites/bryantoporek/2026/11/07/why-the-warriors-arent-parting-ways-with-kristaps-porziis-yet)
  - [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery)
  - [SI](https://www.si.com/nba/suns/onsi/insider-reveals-when-phoenix-suns-center-mark-williams-should-return-from-injury)
  - [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)
  - [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work)
  - [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/detroit-pistons-jalen-duren-injury-update-november-8/ddrysdale/detroit-pistons/11/08/2026/505667/)
  - [Heavy, 6 Nov](https://heavy.com/sports/nba/toronto-raptors/scottie-barnes-injury-update-bucks/)
  - [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process)
  - [NBA.com, 3 Nov](https://www.nba.com/news/kawhi-leonards-knee-swelling-has-been-treated-and-hell-start-return-to-play-process-raptors-say)
  - [Yahoo, 6 Nov](https://sports.yahoo.com/articles/raptors-vs-bucks-injury-report-140945565.html)
  - [ESPN Fan Support: Players on IR](https://support.espn.com/hc/en-us/articles/115003849911-Players-on-Injured-Reserve-IR)
  - [ESPN Fan Support: moving players on and off IR](https://support.espn.com/hc/en-us/articles/115003860512-Move-a-Player-On-or-Off-Injured-Reserve-IR)
  - [Yahoo, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
  - [AP via AJC, 31 Oct](https://www.ajc.com/news/2026/10/chet-holmgren-out-at-least-2-months-with-knee-injury-and-cason-wallace-has-shoulder-surgery/)
  - [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)
  - [FantasyPros](https://www.fantasypros.com/nba/news/614410/moses-moody-knee-could-return-december-or-january.php)
  - [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain)
  - [ClutchPoints, 5 Nov](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-portland-loses-guard-to-painful-injury-in-win-vs-suns)
  - [RotoBaller, 5 Nov](https://www.rotoballer.com/?p=1984362)
  - [Yahoo (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html)
  - [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
  - [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
  - [RotoWire, Jul](https://www.rotowire.com/basketball/headlines/jamir-watkins-injury-undergoes-surgery-for-torn-acl-532251)
  - [NBC, 30 Jul](https://www.nbcsports.com/fantasy/basketball/player-news/2026-07-30/jamir-watkins-tears-acl-during-summer-league)
  - [NBA.com, 28 Oct](https://www.nba.com/news/washington-wizards-justin-champagnie-foot-surgery)
  - [Roundtable, Oct](https://roundtable.io/sports/nba/wizards/players/wizards-justin-champagnie-undergoes-surgery-sidelined-long-term)
  - [Roundtable, 25 Sep](https://roundtable.io/sports/nba/pacers/news/pacers-give-johnny-furphy-acl-rehab-update-before-camp)
  - [Forbes, 6 Nov](https://www.forbes.com/sites/tonyeast/2026/11/06/ben-sheppard-longer-absence-is-bad-news-for-indiana-pacers/)
  - [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182)
  - [Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)
  - [Inquirer, 4 Nov](https://www.inquirer.com/sixers/dominick-barlow-injury-update-76ers-lebron-james-joel-embiid-20261104.html)
  - [Northeast Times, 5 Nov](https://northeasttimes.com/2026/11/05/sixers-injury-report-bona-barlow-embiid-next-three-games-november-2026/)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
  - [CBS/RotoWire, 26 Oct](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-to-be-re-evaluated-in-two-weeks-536198/)
  - [Roundtable, 7 Nov](https://roundtable.io/sports/nba/nuggets/news/nuggets-vs-pacers-injury-report-tyrese-haliburton-demar-derozan-statuses)
- Our roster moves and IR history: `council/roster.csv`. Form for Black, Duren, Barnes and Kawhi: `python council/form.py`, run 2026-11-08 20:27 UTC.
