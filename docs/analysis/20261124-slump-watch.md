# Slump Watch: 24 Nov 2026

- Generated 2026-11-24 07:07 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 35. Teams have played **1 to 19 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 35 (Mon 23 Nov US) re-scored from ESPN's final NBA box scores: all 63 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**3 rostered players are 10+ FP/g under projection, on 2 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.2/60.5 · LaMelo Ball 33.9/46.4 · Josh Giddey 34.2/46.2 |
| Melbourne poopoo | 1 | Anthony Davis 49.4/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 53.0/44.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 48.8/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 50.3/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 42.8/46.5 · Joel Embiid 39.4/45.4 |
| Lauri Birds | 0 | Nikola Jokic 66.4/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.9/56.8 · Cooper Flagg 49.2/45.4 · Evan Mobley 39.9/43.3 |
| Snow Time Lakers | 0 | Jalen Johnson 43.7/50.0 · Jayson Tatum 46.0/48.1 · Kyrie Irving 40.8/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 60.6/60.6 · Domantas Sabonis 44.0/46.7 · Tyrese Maxey 44.6/45.1 |

## Since the last Slump Watch

Against [20261123-slump-watch.md](20261123-slump-watch.md):

- **Joined the flagged list:** Brandon Ingram (Melbourne poopoo, LAC), −15.5. Yesterday he was rostered with no games. His season debut on Mon 23 Nov, 23 FP in 27 min, is his only game, so the gap is a small sample.
- **Left it:** nobody. LaMelo Ball and Josh Giddey are still flagged.
- **Gaps that moved 3+ FP/g:** none in either report's tables. Ball went from −12.2 to −12.5 and Giddey from −11.3 to −11.9. The largest moves among the rest:
  - Kevin Durant, −7.8 → −6.6;
  - Michael Porter Jr., −4.5 → −5.9;
  - James Harden, −6.0 → −6.8.
- **Drivers:** Ball moved from *minutes* to *both*. Ingram enters under *both*. Giddey stays under *minutes*.
- **Last 7 days lists:**
  - *Not flagged, but 10+ under over the last 7 days:* Alex Sarr, Tyrese Maxey and Ajay Mitchell joined. Trae Young (L7 30.4 → 34.5) and Brandon Miller (L7 27.3 → 34.7) left.
  - *Flagged, but within 10 over the last 7 days:* Josh Giddey is still the only name.
- **Near the line:** Michael Porter Jr. (Team Nic Kerr, −5.9) joined. Jalen Suggs (−6.2) left because Lauri Birds dropped him; the ESPN sync recorded it at 04:14 UTC on 23 Nov, two minutes after yesterday's report.
- **Under 2026, not under projection:** Trey Murphy III (us) joined (31.1 against 41.6). Jalen Suggs left.
- **ESPN status:** Jalen Duren's ESPN est. moved from 24 Nov to 30 Nov.
- **Our pending trades:** there was 1 offer yesterday and there are 12 today.
  - We proposed ten: five to Melbourne poopoo, three to Dr White Slong (yesterday's included), one to Team Nic Kerr and one to Cream Abdul-Yammar. Kawhi Leonard is in all ten, and Trey Murphy III is in seven.
  - Cream Abdul-Yammar proposed two to us. Both ask for Paul George, one for Jeremiah Fears and Ayo Dosunmu, the other for Fears and Immanuel Quickley.

## Research

**Flagged:**

- **Brandon Ingram (LAC, Melbourne poopoo, new):** He made his season debut on Mon 23 Nov in a 116-104 loss at HOU and started. His line: 16 pts (6-18, 0-6 3PT, 4-5 FT), 7 reb, 4 ast, 0 stl, 0 blk and 1 TO in 27 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910043)).
  - The injury: he had right heel surgery in May. The operation also found and treated a partially torn Achilles tendon, which the team had not disclosed before ([NBA.com, 24 Nov](https://www.nba.com/news/brandon-ingram-expected-to-make-clippers-debut-monday-in-houston)). He missed LAC's first 15 games.
  - Minutes: no limit was announced. ClutchPoints expects the Clippers to "manage" his time while he regains rhythm and conditioning. That is the outlet's view, not a team statement ([ClutchPoints via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/brandon-ingram-performed-clippers-debut-051216744.html)). ESPN lists him active.
  - From `form.py`: season, L7, L15 and L30 are all 23.0 (1), small sample. Rate 23.9, small sample; projected 38.5. A flag that rests on one game is noise.
  - LAC plays next on Wed 25 Nov at MEM ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **Josh Giddey (CHI):** On Mon 23 Nov vs CLE he had 4 pts (2-11, 0-3 3PT), 2 reb, 11 ast, 1 stl, 1 blk and 3 TO in 22 min, 24 FP (per `gamelog.py`), in a 122-108 win ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)).
  - The benching: CHI led 113-104 when Tiago Splitter pulled him and Matas Buzelis with 4:41 left, after a fast-break turnover (Giddey's third). It was the second time in three games that neither player closed. Splitter said he was "trying to protect him a little bit" on the second night of a back-to-back, after Sunday's 41 minutes. He also told Giddey: "Be aggressive. Be you, but be aggressive. Play simple."
  - Giddey said he has at times been "too unselfish and getting off the ball too soon" ([Chicago Sun-Times, 23 Nov](https://chicago.suntimes.com/bulls/2026/11/23/benching-showcase-bench-win-as-bulls-beat-the-cavs); [HEAVY, 24 Nov](https://heavy.com/sports/nba/chicago-bulls/bulls-josh-giddey-matas-buzelis-frustrated-after-latest-tiago-splitter-decision)).
  - Norman Powell is still out with a right hamstring strain. He is due to be re-evaluated later this week ([Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329)); *ESPN est.* 28 Nov.
  - From `form.py`: season 34.2 (17), L7 40.0 (5), L15 40.4 (9), L30 37.1 (15), Rate 39.2, projected 46.2. His L7 is 5.8 over his season average. That comes from two games, 58 FP on 18 Nov and 89 FP on 22 Nov. His other three games in the window scored 13, 16 and 24 FP. His minutes are normal (27.6 over L7, 28.2 for the season).
  - CHI plays next on Wed 25 Nov at CHA ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **LaMelo Ball (MIN):** On Mon 23 Nov vs BKN he had 17 pts (6-16, 2-10 3PT, 3-3 FT), 2 reb, 3 ast, 1 stl, 1 blk and 1 TO in 30 min, 29 FP, in a 142-116 win. Jaden McDaniels (34) and Ayo Dosunmu (23) led the scoring ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040); [AP via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/jaden-mcdaniels-scores-career-best-034123453.html)).
  - The reason is still shooting. Dunking With Wolves gives his splits:
    - first 12 games: 18.6 pts on 45.9% FG and 40.6% from three;
    - the four games before Monday: 14.5 pts on 28.9% and 26.1%.
  - The same piece credits his facilitating and the best defense of his career. Chris Finch said he is "still competing" and "still guarding." Part of the slump is put on the absence of Anthony Edwards ([Dunking With Wolves, 21 Nov](https://dunkingwithwolves.com/lamelo-ball-s-defensive-improvement-is-helping-the-timberwolves-survive-his-slump)).
  - Edwards had an arthroscopic right knee clean-up in late October. No timeline has been set, and Edwards said he has "no clue" when he will return ([FOX 9, 19 Nov](https://www.fox9.com/news/anthony-edwards-injury-update-no-clue-return-yet-nov-19-2026)); *ESPN est.* 21 Dec.
  - From `form.py`: season 33.9 (18), L7 25.6 (5), L15 33.1 (8), L30 33.7 (16), Rate 31.4, projected 46.4. His L7 is 8.3 under his season average. The window holds a 9-FP game (16 Nov, 24 min) and four games of 25 to 33 FP. His minutes are up (30.4 over L7, 28.5 for the season), so this is not a minutes problem.
  - MIN plays next on Wed 25 Nov at OKC ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).

**New to the Last 7 days lists:**

- **Alex Sarr (WSH, Team Nic Kerr):** WSH did not play on Monday ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)). His L7 of 24.5 (4) is 5.9 under his season average of 30.4.
  - Why it dropped: his 54-FP game of 15 Nov rolled out of the window. The four games left are 12 FP (16 Nov, 31 min), 37 FP (18 Nov, 22 min), 10 FP (20 Nov, 20 min) and 39 FP (22 Nov, 26 min), per `gamelog.py`.
  - On 20 Nov at CHI he had 3 pts (1-3), 3 reb, 1 stl and 1 blk in 20 min, while Anthony Davis had 36 pts and 11 reb in 34 min ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909309)). On 22 Nov vs ORL he had 10 pts (3-5), 9 reb, 2 ast, 2 stl and 1 blk in 26 min ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031)).
  - His minutes are down a little: 24.8 over L7 against 26.7 for the season. He shares the frontcourt with Davis; as of 13 Nov Davis averaged 34.1 min and Sarr 27.2 ([Wiz of Awes, 13 Nov](https://wizofawes.com/washington-wizards-time-remove-deandre-ayton-from-rotation-anthony-davis-alex-sarr)). No injury and no role change has been reported.
  - From `form.py`: L15 30.8 (8), L30 31.2 (15), Rate 29.3, projected 36.6.
  - WSH hosts BOS on Tue 24 Nov ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)).
- **Tyrese Maxey (PHI, Team Nic Kerr):** His L7 of 34.3 (3) is 10.3 under his season average of 44.6.
  - He missed Wed 18 Nov with a "minor foot issue." He returned on Sat 21 Nov with 17 pts (4-11, 0-3 3PT, 9-10 FT), 4 reb, 4 ast and 1 blk in 36 min. It was his first game under 20 points since 6 Nov ([RotoWire via CBS Sports, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/76ers-tyrese-maxey-solid-numbers-in-return-to-lineup/)).
  - On Mon 23 Nov vs POR he had 22 pts (7-16, 2-7 3PT), 2 reb, 5 ast, 0 stl and 3 TO in 35 min, in a 128-111 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910037)). Joel Embiid missed the game with an illness, and LeBron James (23) and Jaylen Brown (20) shared the scoring with Maxey ([Philadelphia Inquirer, 23 Nov](https://www.inquirer.com/sixers/sixers-blazers-score-lebron-james-jaylen-brown-deni-avdija-20261123.html)). No timetable has been reported for Embiid; *ESPN est.* 25 Nov.
  - Why his L7 dropped: the window has three games, 47 FP (16 Nov), 27 FP (21 Nov) and 29 FP (23 Nov). His 48-FP game of 15 Nov rolled out, and the missed game left a gap. The two games since his return are the cause: modest shooting and few rebounds and steals. His minutes are normal (35.3 over L7, 36.1 for the season).
  - From `form.py`: L15 41.4 (7), L30 42.8 (15), Rate 40.5, projected 45.1.
  - PHI hosts MIA on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **Ajay Mitchell (OKC, Lauri Birds):** His L7 of 22.5 (4) is 8.2 under his season average of 30.8.
  - On Mon 23 Nov at IND he had 12 pts (4-14, 2-3 3PT, 2-2 FT), 4 reb, 3 ast, 0 stl and 0 TO in 35 min, in a 125-120 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038)).
  - RotoWire: he has shot 35% or worse in three straight games, and his role has grown because of OKC's injuries. It still calls him a "must-roster player," but says his ceiling has trended down ([RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/)).
  - The 20 Nov game (8 pts on 3-12) was his fifth straight under 15 points, after 18 or more in six of seven. He was "struggling to find his touch on the floater" ([OKC Thunder On SI via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/okc-thunder-more-production-ajay-203000711.html)).
  - The reason is shooting, not minutes: he is at 30.5 over L7 against 28.1 for the season. The window holds 34, 12, 25 and 19 FP (per `gamelog.py`); his 33-FP game of 15 Nov rolled out.
  - From `form.py`: L15 24.5 (6), L30 32.0 (14), Rate 26.4, projected 32.8.
  - OKC hosts MIN on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).

**Updates since 23 Nov:**

- **Cade Cunningham (DET, us):** DET did not play on Monday. The NBA injury report has him probable for Tue 24 Nov at ORL with right knee soreness ([HEAVY, 23 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-pistons-magic/)).
  - ESPN now lists him day-to-day; *ESPN est.* 24 Nov. No timetable has been reported, and none appears needed.
  - From `form.py`: season 48.8 (15), L7 39.0 (3), L15 48.7 (7), L30 50.3 (13), Rate 46.1. His L7 is still 9.8 under his season average, for yesterday's reason: his 99- and 57-FP games rolled out of the window and he missed 18 Nov.
- **De'Aaron Fox (SA):** The Spurs ruled him out of Mon 23 Nov at SAC with a right shin contusion ([KSAT, 23 Nov](https://www.ksat.com/sports/2026/11/24/spurs-rule-out-wembanyama-fox-for-game-at-kings/)).
  - Mitch Johnson said a Pelicans player intentionally tripped him and that he is not expected to miss much time. Jeff McDonald called Fox's and Victor Wembanyama's injuries (low back tightness) "bumps and bruises." Both are expected back for Wed 25 Nov vs POR, but Johnson had not confirmed it ([Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/breaking-news/article/victor-wembanyama-missing-first-game-of-season-due-to-back-tightness-deaaron-fox-also-out-for-game-vs-kings-021655694.html)). *ESPN est.* 25 Nov for both.
  - Without them, Stephon Castle had 28 pts, 8 reb and 11 ast in a 123-107 win ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045)).
  - From `form.py`: season 29.5 (16), L7 15.7 (3), L15 24.0 (6), L30 28.1 (14), Rate 23.7. His L7 is unchanged and 13.8 under his season average, for the reasons in earlier notes.
- **Luka Doncic (LAL):** On Mon 23 Nov vs UTA he had 28 pts (8-24, 3-14 3PT, 9-10 FT), 4 reb, 8 ast, 1 stl and 4 TO in 33 min, 38 FP, in a 109-94 win ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910044); [Yardbarker, 23 Nov](https://www.yardbarker.com/nba/articles/lakers_beat_jazz_109_94_as_doncic_scores_28/s1_17668_44609977)).
  - His L7 fell from 47.8 (4) to 41.0 (4), 19.6 under his season average. His 65-FP game of 15 Nov rolled out, and on Monday he shot 8-24. His minutes are normal (37.0 over L7, 36.1 for the season).
  - Austin Reaves is still out with a left heel bruise. JJ Redick implied he could return "over the next few games" ([Heavy, 22 Nov](https://heavy.com/sports/nba/los-angeles-lakers/lakers-reveal-shocking-update-austin-reaves/)); *ESPN est.* 27 Nov.
  - From `form.py`: season 60.6 (16) → 63.3 (15), L15 50.6 (7), L30 64.1 (14), Rate 52.6.
- **Derrick White (BOS, in our pending trades):** Nothing new since 23 Nov. BOS did not play on Monday ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)) and plays Tue 24 Nov at WSH. He has been off the injury report since 22 Nov, after one game out with the left AC joint sprain ([RotoWire, 22 Nov](https://www.rotowire.com/basketball/headlines/derrick-white-news-off-injury-report-sunday-540521)).
  - His L7 fell from 26.2 (4) to 22.0 (3) with no new game, because his 39-FP game of 15 Nov rolled out (per `gamelog.py`). It is now 7.9 under his season average. The cause is still the three-point slump in yesterday's notes.
  - From `form.py`: L15 29.6 (7), L30 29.4 (14), Rate 27.7.
- **Michael Porter Jr. (BKN):** On Mon 23 Nov at MIN he had 11 pts (3-7, 0-2 3PT, 5-7 FT), 6 reb, 2 ast, 1 stl and 4 TO in 31 min, 14 FP, in a 142-116 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040)).
  - His L7 is 24.5 (4), 8.6 under his season average of 33.1. The window holds 8 FP (18 Nov) and 14 FP (Monday) beside 44 and 32 FP. His minutes are normal (33.0 over L7, 32.7 for the season). No injury and no role change was found; the drop is production.
  - His season gap widened from −4.5 to −5.9, which puts him near the line. Rate 29.1.
- **Damian Lillard (POR):** On Mon 23 Nov at PHI he had 18 pts (4-15, 1-6 3PT, 9-9 FT), 3 reb, 5 ast, 1 stl and 0 TO in 29 min, 31 FP, in a 128-111 win ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910037); [Yardbarker, 23 Nov](https://www.yardbarker.com/nba/articles/trail_blazers_beat_76ers_128_111_as_avdija_scores_31/s1_17668_44609398)).
  - His L7 went from 27.0 (4) to 27.8 (5). From `form.py`: season 30.4 (17), L15 30.2 (8), L30 29.1 (15), Rate 27.2.
- **Brandin Podziemski (GS):** Nothing new since 23 Nov. GS did not play on Monday ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)) and hosts SAC on Wed 25 Nov.
- **Trae Young (WSH, left the list):** WSH did not play on Monday ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)). His L7 rose from 30.4 (5) to 34.5 (4) because his 14-FP, 26-minute game of 15 Nov rolled out (per `gamelog.py`). It is now 1.7 under his season average of 36.2. Rate 34.9.
- **Brandon Miller (CHA, left the list):** He played on Mon 23 Nov vs MEM through the right knee bone bruise he had been listed probable with ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/brandon-miller-knee-probable-monday-vs-memphis)). His line: 20 pts (6-19, 4-8 3PT, 4-4 FT), 3 reb, 5 ast, 3 blk and 5 TO in 35 min, 33 FP, in a 117-111 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036)).
  - ESPN now lists him active. His L7 rose from 27.3 (3) to 34.7 (3): his 11-FP game of 15 Nov rolled out.
  - From `form.py`: season 30.0 (14), L15 28.8 (4), L30 32.9 (12), Rate 32.2.

**Our near-the-line players:**

- **Jalen Duren (DET, Out):** He is ruled out for Tue 24 Nov at ORL. FantasyPros says he "should be re-evaluated soon" and "remains without a clear timetable to return" ([FantasyPros, 23 Nov](https://www.fantasypros.com/nba/news/622235/jalen-duren-hamstring-ruled-out-tuesday.php)). No re-evaluation result has been reported.
  - *ESPN est.* has moved from 24 Nov to 30 Nov.
  - From `form.py`: season 33.5 (2) → 44.0 (1), small sample; Rate 44.1, small sample.
  - DET plays Tue 24 Nov at ORL and Fri 27 Nov vs MIL.
- **Matas Buzelis (CHI):** On Mon 23 Nov vs CLE he had 15 pts (5-10, 4-6 3PT), 6 reb, 0 ast, 1 stl and 1 TO in 27 min, 26 FP ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)).
  - He was pulled with Giddey at 4:41 of the fourth quarter. "As a competitor" he wants to be on the floor, but "we won the game and that's all that matters" ([HEAVY, 24 Nov](https://heavy.com/sports/nba/chicago-bulls/bulls-josh-giddey-matas-buzelis-frustrated-after-latest-tiago-splitter-decision)). Splitter cited the back-to-back after Sunday's heavy minutes ([Chicago Sun-Times, 23 Nov](https://chicago.suntimes.com/bulls/2026/11/23/benching-showcase-bench-win-as-bulls-beat-the-cavs)).
  - From `form.py`: season 25.7 (17), L7 33.4 (5), L15 31.0 (9), L30 27.0 (15), Rate 30.4, projected 32.5. His L7 is 7.7 over his season average, from the 54-FP (18 Nov) and 39-FP (22 Nov) games and more minutes (30.2 over L7, 27.8 for the season).
- **Trey Murphy III (NO):** He was available for Mon 23 Nov vs PHX with no minutes limit, after missing Sat 21 Nov at SA, the second night of a back-to-back ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns)). His line: 9 pts (4-14, 1-6 3PT), 9 reb, 2 ast, 2 stl and 1 TO in 35 min, 25 FP, in a 123-119 overtime loss. Saddiq Bey had 21 off the bench in 40 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)).
  - RotoWire calls him "seemingly underutilized." He ranked top 30 per game in each of the past two seasons and is now well outside the top 50 ([RotoWire, 23 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-news-low-usage-continues-monday-540768)). ESPN lists him active.
  - From `form.py`: season 31.1 (11), L7 31.5 (2, small sample, noise), L15 35.7 (3), L30 33.8 (9), Rate 33.7, projected 36.8. His gap widened from −5.1 to −5.7. He is now in the *Under 2026* table (41.6 last season).
  - His absence on 21 Nov, the second night of a back-to-back, fits yesterday's note that he is likely to sit on 30 Nov, also the second night of a back-to-back.
- **Kawhi Leonard (TOR, Out):** Nothing new found. On 17 Nov the Raptors said he had progressed in his strength and conditioning program and that another update would come in a week ([Bleacher Report, 17 Nov](https://bleacherreport.com/articles/25534761-kawhi-leonard-injury-update-raptors-give-latest-return-timeline-amid-stars-rehab-knee)). No such update had appeared by 24 Nov 07:20 UTC.
  - He missed Mon 23 Nov vs MIL ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)). Shams Charania's "within the next few weeks" is still the latest timeline ([RotoWire, 20 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-still-weeks-away-from-returning-540189)); *ESPN est.* 3 Dec.
  - From `form.py`: season 40.0 (2), small sample; Rate 43.3, small sample.

**Our pending trades:**

These are the players not covered yesterday. Each one's windows are in the trade tables below. Ingram and Giddey are under *Flagged* above; Buzelis, Duren, Murphy and Leonard are under *Our near-the-line players*.

- **Jeremiah Fears (NO, we receive):** On Mon vs PHX he had 7 pts (3-17), 7 reb, 11 ast and a season-high 4 stl in 40 min before fouling out. He is now NO's primary ball-handler. RotoWire flags his inefficient scoring but expects him to stay rostered in all formats ([RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-jeremiah-fears-strong-peripheral-production/)). His L7 is 6.4 over his season average: his minutes are up (34.4 over L7) and his games ran 31 to 52 FP. Rate 36.6, projected 27.3.
- **Ayo Dosunmu (MIN, we receive):** On Mon vs BKN he had 23 pts (8-13, 4-7 3PT), 3 reb, 5 ast and 2 TO in 30 min, 39 FP ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040)). His L7 is 5.7 under his season average because of two 13-FP games (16 and 19 Nov); his minutes are normal and no injury was found. Rate 31.7.
- **Immanuel Quickley (TOR, we receive):** On Mon vs MIL he had 13 pts (5-17, 2-10 3PT), 3 reb, 6 ast and 3 TO in 32 min, in a 116-111 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)). Rate 33.0.
- **Paul George (BOS, we send):** He sat Sun 22 Nov at GS for rest, the second night of a back-to-back ([FantasyPros, 22 Nov](https://www.fantasypros.com/nba/news/621898/paul-george-rest-ruled-out-sunday.php)). On 21 Nov at SAC he had 19 pts (6-21), 8 reb, 5 ast, 4 stl and 1 blk in 37 min ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910028)). Rate 39.0.
- **Stephon Castle (SA, we receive):** On Mon at SAC he had 28 pts (9-23), 8 reb, 11 ast and 2 TO in 37 min, 59 FP, as the main ball-handler with Fox, Wembanyama and Dylan Harper out ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045)). Harper (hip): 2–3 weeks reported ([ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html)); *ESPN est.* 13 Dec. For Fox and Wembanyama, see *Updates* above. Castle's L7 is 6.5 over his season average, from two 59-FP games (19 and 23 Nov). Rate 39.9.
- **Moussa Diabate (CHA, we receive):** On Mon vs MEM he started and had 10 pts (3-4), 10 reb (4 offensive), 3 ast, 2 stl and 2 blk in 35 min, 49 FP ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036)). He had 21 pts and 15 reb on 20 Nov at ATL ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909305)). Those two games are why his L7 is 6.4 over his season average. Rate 39.5, projected 24.0.
- **James Harden (CLE, we receive):** On Mon at CHI he had 21 pts (5-14, 3-8 3PT, 8-8 FT), 6 reb, 5 ast and 7 TO in 37 min, 23 FP, in a 122-108 loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)). His L7 is 7.5 over his season average because of his 80-FP game of 20 Nov (per `gamelog.py`). Rate 40.5.
- **Jalen Smith (CHI, we send):** On Mon vs CLE he started and had 11 pts (4-7), 6 reb and 4 ast in 25 min, 31 FP, while playing through an illness ([ClutchPoints via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/bulls-set-record-bench-scoring-045038931.html)). His L7 is 9.6 over his season average, from his 62-FP (16 Nov) and 61-FP (22 Nov) games. Rate 42.8.
- **Jaden McDaniels (MIN, we receive):** On Mon vs BKN he scored a career-best 34 pts (12-16, 4-4 3PT), with 10 reb, 6 ast and 2 stl in 34 min, 77 FP ([AP via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/jaden-mcdaniels-scores-career-best-034123453.html)). That game, and 55 FP on 17 Nov, are why his L7 is 9.4 over his season average. Rate 44.9, projected 29.7.
- **Nickeil Alexander-Walker (ATL, we receive):** ATL did not play on Monday. On 22 Nov vs DET he had 27 pts (8-18, 6-10 3PT), 2 reb and 1 ast in 28 min ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). Rate 33.8.
- **Julius Randle (BKN, we receive):** On Mon, in his return to Minnesota, he had 29 pts (11-16), 4 reb, 4 ast and 5 TO, his second straight game of 25 or more ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/randle-drops-29-points-in-return-to-minnesota)). His L7 is 9.3 over his season average, from his 61-FP (16 Nov) and 53-FP (20 Nov) games. Rate 39.8.
- **Brook Lopez (LAC, we send):** On Mon at HOU he started beside Ingram and had 3 pts (1-3), 4 reb and 1 ast in 21 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910043)). Rate 29.7.
- **Anthony Edwards (MIN, we receive, Out):** He had an arthroscopic right knee clean-up in late October. No timeline has been set, and he has "no clue" when he will return ([FOX 9, 19 Nov](https://www.fox9.com/news/anthony-edwards-injury-update-no-clue-return-yet-nov-19-2026)); *ESPN est.* 21 Dec. Season 52.5 (4); Rate 51.0.
- **Karl-Anthony Towns (NY, we receive):** NY did not play on Monday. On 22 Nov vs IND he had 30 pts (9-14, 4-4 3PT, 8-12 FT), 13 reb, 5 ast, 3 stl and 2 blk in 29 min, 82 FP ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)). His L7 is 12.3 over his season average, from games of 63, 51 and 82 FP. Rate 59.3. NY hosts CLE on Wed 25 Nov.
- **Jalen Brunson (NY, we receive):** NY did not play on Monday. On 22 Nov vs IND he had 22 pts (8-18, 1-6 3PT), 3 reb, 7 ast and 4 TO in 32 min ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)). Rate 43.4.
- **Already covered on 23 Nov, updated:**
  - **Donovan Mitchell (CLE, we receive):** On Mon at CHI he had 28 pts (8-17, 1-6 3PT, 11-12 FT), 3 reb, 5 ast, 1 stl, 2 blk and 2 TO in 37 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)). His gap narrowed from −4.1 to −3.7. Rate 44.3.
  - **Anthony Black (ORL, we send):** ORL did not play on Monday ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)) and hosts DET on Tue 24 Nov. Rate 36.7.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| LaMelo Ball | MIN | #2 | 18 | 28.5 / 32.9 | 0.84 | 33.9 (18) | 25.6 (5) | 33.1 (8) | 33.7 (16) | 46.4 | **−12.5** | 41.1 | Active |
| Josh Giddey | CHI | #3 | 17 | 28.2 / 35.5 | 0.93 | 34.2 (17) | 40.0 (5) | 40.4 (9) | 37.1 (15) | 46.2 | **−11.9** | 46.2 | Active |

- **LaMelo Ball** (both): scoring −6.9, reb −1.4, ast −5.4, stocks +0.6, TO −0.1; bonus +0.6.
  - Current: 28.5 min, 17.2 pts, 6.2-15.1 FG, 1.7-2.2 FT, 4.2 reb, 5.6 ast, 1.7 stl, 0.2 blk, 3.3 TO
  - Last 7 days (5 GP): 30.4 min, 13.6 pts, 5.2-15.4 FG, 1.0-1.4 FT, 5.8 reb, 4.0 ast, 1.0 stl, 0.4 blk, 2.2 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Josh Giddey** (minutes): scoring −8.8, reb −3.1, ast −0.5, stocks −3.2, TO +0.9; bonus +2.8.
  - Current: 28.2 min, 10.4 pts, 4.1-9.6 FG, 1.1-1.8 FT, 6.1 reb, 9.4 ast, 0.4 stl, 0.6 blk, 3.4 TO
  - Last 7 days (5 GP): 27.6 min, 10.2 pts, 4.4-10.2 FG, 0.6-1.0 FT, 8.0 reb, 11.4 ast, 0.4 stl, 0.6 blk, 4.0 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO

### Melbourne poopoo: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Brandon Ingram | LAC | #7 | 1 | 27.0 / 35.3 | 0.78 | 23.0 (1) | 23.0 (1) | 23.0 (1) | 23.0 (1) | 38.5 | **−15.5** | 36.5 | Active |

- **Brandon Ingram** (both): scoring −13.7, reb +1.3, ast −1.6, stocks −6.0, TO +3.6; bonus +1.0.
  - Current: 27.0 min, 16.0 pts, 6.0-18.0 FG, 4.0-5.0 FT, 7.0 reb, 4.0 ast, 0.0 stl, 0.0 blk, 1.0 TO
  - Projected: 35.3 min, 22.6 pts, 8.5-17.6 FG, 3.9-4.8 FT, 5.7 reb, 4.8 ast, 0.8 stl, 0.7 blk, 2.8 TO

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −6.8 (#9, efficiency, L7 33.4), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.7 (#7, efficiency, L7 31.5).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −7.5 (#9, efficiency, L7 26.2), Derrick White −7.1 (#6, minutes, L7 22.0), Joel Embiid −6.0 (#3, efficiency, L7 58.3).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Darius Garland −6.8 (#5, efficiency, L7 38.8), Kevin Durant −6.6 (#4, efficiency, L7 36.5), Ivica Zubac −6.2 (#7, minutes, L7 35.2).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** De'Aaron Fox −8.7 (#7, efficiency, L7 15.7), Damian Lillard −8.2 (#6, efficiency, L7 27.8), Shai Gilgeous-Alexander −8.0 (#1, efficiency, L7 55.7), Brandon Miller −7.4 (#8, minutes, L7 34.7).

### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.3 (#1, efficiency, L7 48.7).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −8.2 (#4, efficiency, L7 34.5), James Harden −6.8 (#5, efficiency, L7 42.8), Alex Sarr −6.2 (#7, efficiency, L7 24.5), Michael Porter Jr. −5.9 (#6, efficiency, L7 24.5).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | Josh Giddey |
| efficiency | — |
| both | Brandon Ingram, LaMelo Ball |

- **Flagged and not active on ESPN:** none.

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** Josh Giddey (Cream Abdul-Yammar, L7 40.0 in 5 vs projected 46.2, season gap −11.9).
- **Not flagged, but 10+ under projection over the last 7 days:** Cade Cunningham (Come-in Cider (us), L7 39.0 in 3 vs projected 50.4, L7 gap −11.4, season gap −1.6), De'Aaron Fox (Matt Wright's Foxies, L7 15.7 in 3 vs projected 38.2, L7 gap −22.5, season gap −8.7), Luka Doncic (Team Nic Kerr, L7 41.0 in 4 vs projected 60.6, L7 gap −19.6, season gap −0.1), Derrick White (Dr White Slong, L7 22.0 in 3 vs projected 37.0, L7 gap −15.0, season gap −7.1), Michael Porter Jr. (Team Nic Kerr, L7 24.5 in 4 vs projected 38.9, L7 gap −14.4, season gap −5.9), Alex Sarr (Team Nic Kerr, L7 24.5 in 4 vs projected 36.6, L7 gap −12.1, season gap −6.2), Damian Lillard (Matt Wright's Foxies, L7 27.8 in 5 vs projected 38.6, L7 gap −10.8, season gap −8.2), Tyrese Maxey (Team Nic Kerr, L7 34.3 in 3 vs projected 45.1, L7 gap −10.8, season gap −0.5), Ajay Mitchell (Lauri Birds, L7 22.5 in 4 vs projected 32.8, L7 gap −10.3, season gap −2.1), Brandin Podziemski (Matt Wright's Foxies, L7 20.8 in 4 vs projected 30.8, L7 gap −10.1, season gap 0.9).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | — | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | 41.6 |

## Our pending trades

With **Cream Abdul-Yammar**, proposed to us, expires 25 Nov 12:11 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 39.8 (5) | 36.7 (10) | 36.5 (17) | 27.3 | +6.1 | Active |
| Ayo Dosunmu | we receive | 18 | 31.7 / 29.4 | 34.9 | 29.2 (5) | 31.9 (8) | 34.2 (16) | 30.4 | +4.5 | Active |
| Paul George | we send | 14 | 30.1 / 33.2 | 40.6 | 38.0 (3) | 40.3 (6) | 38.7 (12) | 38.5 | +2.1 | Active |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 03:28 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Brandon Ingram | we receive | 1 | 27.0 / 35.3 | 23.0 | 23.0 (1) | 23.0 (1) | 23.0 (1) | 38.5 | −15.5 | Active |
| Stephon Castle | we receive | 18 | 29.9 / 32.7 | 36.3 | 42.8 (4) | 41.1 (8) | 36.8 (16) | 36.9 | −0.6 | Active |
| Matas Buzelis | we send | 17 | 27.8 / 30.5 | 25.7 | 33.4 (5) | 31.0 (9) | 27.0 (15) | 32.5 | −6.8 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |

With **Team Nic Kerr**, proposed by us, expires 26 Nov 02:41 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Moussa Diabate | we receive | 14 | 30.0 / 24.6 | 36.9 | 43.3 (3) | 40.2 (5) | 36.7 (12) | 24.0 | +12.9 | Active |
| James Harden | we receive | 17 | 33.7 / 33.6 | 35.3 | 42.8 (4) | 42.3 (7) | 36.2 (16) | 42.1 | −6.8 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 01:35 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jaden McDaniels | we receive | 18 | 34.0 / 31.7 | 41.0 | 50.4 (5) | 46.0 (8) | 41.1 (16) | 29.7 | +11.3 | Active |
| Stephon Castle | we receive | 18 | 29.9 / 32.7 | 36.3 | 42.8 (4) | 41.1 (8) | 36.8 (16) | 36.9 | −0.6 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |

With **Dr White Slong**, proposed by us, expires 26 Nov 01:49 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Nickeil Alexander-Walker | we receive | 17 | 31.6 / 32.3 | 34.6 | 31.7 (3) | 35.3 (6) | 33.8 (15) | 34.1 | +0.6 | Active |
| Julius Randle | we receive | 16 | 33.1 / 34.3 | 36.2 | 45.5 (4) | 38.1 (7) | 34.9 (15) | 37.0 | −0.9 | Active |
| Derrick White | we receive | 16 | 30.0 / 34.3 | 29.9 | 22.0 (3) | 29.6 (7) | 29.4 (14) | 37.0 | −7.1 | Active |
| Matas Buzelis | we send | 17 | 27.8 / 30.5 | 25.7 | 33.4 (5) | 31.0 (9) | 27.0 (15) | 32.5 | −6.8 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |
| Brook Lopez | we send | 16 | 24.4 / 26.2 | 29.8 | 30.8 (4) | 31.9 (8) | 27.9 (14) | 26.2 | +3.6 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed by us, expires 26 Nov 02:45 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | we receive | 17 | 28.2 / 35.5 | 34.2 | 40.0 (5) | 40.4 (9) | 37.1 (15) | 46.2 | −11.9 | Active |
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 39.8 (5) | 36.7 (10) | 36.5 (17) | 27.3 | +6.1 | Active |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 00:57 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Anthony Edwards | we receive | 4 | 33.8 / 35.8 | 52.5 | — | — | 51.5 (2) | 47.2 | +5.3 | **Out**, ESPN est. back 21 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Anthony Black | we send | 13 | 33.2 / 28.9 | 37.8 | 36.5 (4) | 37.1 (7) | 37.8 (13) | 28.2 | +9.6 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed to us, expires 25 Nov 11:54 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Immanuel Quickley | we receive | 15 | 32.1 / 31.4 | 34.1 | 31.2 (4) | 33.0 (7) | 34.0 (13) | 34.9 | −0.8 | Active |
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 39.8 (5) | 36.7 (10) | 36.5 (17) | 27.3 | +6.1 | Active |
| Paul George | we send | 14 | 30.1 / 33.2 | 40.6 | 38.0 (3) | 40.3 (6) | 38.7 (12) | 38.5 | +2.1 | Active |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 02:52 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Karl-Anthony Towns | we receive | 16 | 32.5 / 32.7 | 53.0 | 65.3 (3) | 60.0 (7) | 54.3 (14) → 56.2 (13) | 44.1 | +8.9 | Active |
| Jalen Duren | we send | 2 | 19.0 / 31.0 | 33.5 | — | — | — | 42.2 | −8.7 | **Out**, ESPN est. back 30 Nov |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Dr White Slong**, proposed by us, expires 25 Nov 04:05 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Donovan Mitchell | we receive | 17 | 33.2 / 33.9 | 42.8 | 47.0 (4) | 42.4 (7) | 42.0 (16) | 46.5 | −3.7 | Active |
| Derrick White | we receive | 16 | 30.0 / 34.3 | 29.9 | 22.0 (3) | 29.6 (7) | 29.4 (14) | 37.0 | −7.1 | Active |
| Anthony Black | we send | 13 | 33.2 / 28.9 | 37.8 | 36.5 (4) | 37.1 (7) | 37.8 (13) | 28.2 | +9.6 | Active |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 03:02 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jalen Brunson | we receive | 17 | 34.2 / 35.3 | 41.7 | 43.2 (4) | 44.2 (8) | 44.0 (15) | 43.8 | −2.1 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Dr White Slong**, proposed by us, expires 26 Nov 01:38 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Donovan Mitchell | we receive | 17 | 33.2 / 33.9 | 42.8 | 47.0 (4) | 42.4 (7) | 42.0 (16) | 46.5 | −3.7 | Active |
| Derrick White | we receive | 16 | 30.0 / 34.3 | 29.9 | 22.0 (3) | 29.6 (7) | 29.4 (14) | 37.0 | −7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 35.7 (3) | 33.8 (9) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 47.0 (4) | 46.6 (7) | 36.8 (13) → 39.0 (12) | 22.4 | +15.0 | Active |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-24 07:07 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research, 24 Nov:** [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910043) · [NBA.com, 24 Nov](https://www.nba.com/news/brandon-ingram-expected-to-make-clippers-debut-monday-in-houston) · [ClutchPoints via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/brandon-ingram-performed-clippers-debut-051216744.html) · [ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041) · [Chicago Sun-Times, 23 Nov](https://chicago.suntimes.com/bulls/2026/11/23/benching-showcase-bench-win-as-bulls-beat-the-cavs) · [HEAVY, 24 Nov](https://heavy.com/sports/nba/chicago-bulls/bulls-josh-giddey-matas-buzelis-frustrated-after-latest-tiago-splitter-decision) · [Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910040) · [AP via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/jaden-mcdaniels-scores-career-best-034123453.html) · [Dunking With Wolves, 21 Nov](https://dunkingwithwolves.com/lamelo-ball-s-defensive-improvement-is-helping-the-timberwolves-survive-his-slump) · [FOX 9, 19 Nov](https://www.fox9.com/news/anthony-edwards-injury-update-no-clue-return-yet-nov-19-2026) · [ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909309) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031) · [Wiz of Awes, 13 Nov](https://wizofawes.com/washington-wizards-time-remove-deandre-ayton-from-rotation-anthony-davis-alex-sarr) · [ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124) · [RotoWire via CBS Sports, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/76ers-tyrese-maxey-solid-numbers-in-return-to-lineup/) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910037) · [Philadelphia Inquirer, 23 Nov](https://www.inquirer.com/sixers/sixers-blazers-score-lebron-james-jaylen-brown-deni-avdija-20261123.html) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038) · [RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/) · [OKC Thunder On SI via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/okc-thunder-more-production-ajay-203000711.html) · [HEAVY, 23 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-pistons-magic/) · [KSAT, 23 Nov](https://www.ksat.com/sports/2026/11/24/spurs-rule-out-wembanyama-fox-for-game-at-kings/) · [Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/breaking-news/article/victor-wembanyama-missing-first-game-of-season-due-to-back-tightness-deaaron-fox-also-out-for-game-vs-kings-021655694.html) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910045) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910044) · [Yardbarker, 23 Nov](https://www.yardbarker.com/nba/articles/lakers_beat_jazz_109_94_as_doncic_scores_28/s1_17668_44609977) · [Heavy, 22 Nov](https://heavy.com/sports/nba/los-angeles-lakers/lakers-reveal-shocking-update-austin-reaves/) · [RotoWire, 22 Nov](https://www.rotowire.com/basketball/headlines/derrick-white-news-off-injury-report-sunday-540521) · [Yardbarker, 23 Nov](https://www.yardbarker.com/nba/articles/trail_blazers_beat_76ers_128_111_as_avdija_scores_31/s1_17668_44609398) · [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/brandon-miller-knee-probable-monday-vs-memphis) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036) · [FantasyPros, 23 Nov](https://www.fantasypros.com/nba/news/622235/jalen-duren-hamstring-ruled-out-tuesday.php) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042) · [RotoWire, 23 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-news-low-usage-continues-monday-540768) · [Bleacher Report, 17 Nov](https://bleacherreport.com/articles/25534761-kawhi-leonard-injury-update-raptors-give-latest-return-timeline-amid-stars-rehab-knee) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039) · [RotoWire, 20 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-still-weeks-away-from-returning-540189) · [RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-jeremiah-fears-strong-peripheral-production/) · [FantasyPros, 22 Nov](https://www.fantasypros.com/nba/news/621898/paul-george-rest-ruled-out-sunday.php) · [ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910028) · [ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909305) · [ClutchPoints via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/bulls-set-record-bench-scoring-045038931.html) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/randle-drops-29-points-in-return-to-minnesota) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)
