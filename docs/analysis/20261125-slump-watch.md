# Slump Watch: 25 Nov 2026

- Generated 2026-11-25 09:06 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 37. Teams have played **1 to 19 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 36 (Tue 24 Nov US) re-scored from ESPN's final NBA box scores: all 20 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**3 rostered players are 10+ FP/g under projection, on 2 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.1/60.5 · LaMelo Ball 33.9/46.4 · Josh Giddey 34.2/46.2 |
| Melbourne poopoo | 1 | Anthony Davis 50.4/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 53.0/44.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 48.8/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.0/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 42.8/46.5 · Joel Embiid 39.4/45.4 |
| Lauri Birds | 0 | Nikola Jokic 64.6/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.9/56.8 · Cooper Flagg 49.4/45.4 · Evan Mobley 39.9/43.3 |
| Snow Time Lakers | 0 | Jalen Johnson 43.7/50.0 · Jayson Tatum 47.6/48.1 · Kyrie Irving 39.9/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 60.6/60.6 · Domantas Sabonis 44.0/46.7 · Tyrese Maxey 44.6/45.1 |

## Since the last Slump Watch

Against [20261124-slump-watch.md](20261124-slump-watch.md). Only three NBA games were played on Tue 24 Nov: DET at ORL, BOS at WSH and DAL at DEN ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)). Most changes below come from games rolling out of the 7-day window, not from new games.

- **Joined the flagged list:** nobody.
- **Left it:** nobody. LaMelo Ball (−12.5), Josh Giddey (−11.9) and Brandon Ingram (−15.5) are still flagged, with the same gaps as yesterday. MIN, CHI and LAC did not play on Tuesday.
- **Gaps that moved 3+ FP/g:** none in either report's tables. The largest moves:
  - Anthony Black (us, trade tables), +9.6 → +7.1;
  - Alex Sarr, −6.2 → −7.1;
  - Trae Young, −8.2 → −7.5;
  - Derrick White, −7.1 → −7.5.
- **Drivers:** unchanged. Giddey is under *minutes*; Ball and Ingram are under *both*.
- **Last 7 days lists:**
  - *Not flagged, but 10+ under over the last 7 days:* nobody joined. Damian Lillard left: his L7 went from 27.8 (5) to 31.2 (4) against a projection of 38.6. The biggest moves among the names still listed:
    - Tyrese Maxey, 34.3 (3) → 28.0 (2);
    - Michael Porter Jr., 24.5 (4) → 18.0 (3);
    - Derrick White, 22.0 (3) → 25.7 (3).
  - *Flagged, but within 10 over the last 7 days:* Josh Giddey is still the only name. His L7 went from 40.0 (5) to 46.8 (4), against a projection of 46.2.
- **Near the line:** nobody joined or left.
- **Under 2026, not under projection:** Nikola Jokic (Lauri Birds) joined, at 64.6 against 74.9 last season. Jalen Duren and Trey Murphy III (both us) are still listed.
- **ESPN status:** Jalen Smith (us) and Karl-Anthony Towns (in our offers) moved from Active to day-to-day, *ESPN est.* 25 Nov for both. Duren (30 Nov), Kawhi Leonard (3 Dec) and Anthony Edwards (21 Dec) are unchanged.
- **Our pending trades:** there were 12 offers yesterday and there are 16 today.
  - Five are new. We proposed all five, and all expire on 27 Nov:
    - Zion Williamson (Melbourne poopoo), for Black and Leonard;
    - LaMelo Ball and Jeremiah Fears (Cream Abdul-Yammar), for Murphy, Black and Leonard;
    - Jaden McDaniels (Melbourne poopoo), for Black and Leonard;
    - Josh Giddey (Cream Abdul-Yammar), for Leonard and Black;
    - Julius Randle and Derrick White (Dr White Slong), for Buzelis, Black and Leonard.
  - Anthony Black is in all five new offers, and in 6 of the 16 overall. Kawhi Leonard is in all 14 offers we proposed.
  - One offer is gone: Dr White Slong's Mitchell and White for Black, Murphy and Leonard expired at 04:05 UTC on 25 Nov.
  - Cream Abdul-Yammar's two offers to us, both for Paul George, expire today at 11:54 and 12:11 UTC.

## Research

**Flagged:**

- **LaMelo Ball (MIN, Cream Abdul-Yammar):** MIN did not play on Tuesday ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)), and I found no new news since 24 Nov.
  - His L7 rose from 25.6 (5) to 29.8 (4) because his 9-FP game of 16 Nov rolled out (`gamelog.py`). It is now 4.1 under his season average, under the 5-point flag.
  - The reason is still shooting, and his minutes are up (32.0 over L7, 28.5 for the season) ([Dunking With Wolves, 21 Nov](https://dunkingwithwolves.com/lamelo-ball-s-defensive-improvement-is-helping-the-timberwolves-survive-his-slump)).
  - Anthony Edwards: The Athletic's Jon Krawczynski said "I think we're talking into January before we see Anthony Edwards on the court" ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-rumors-insider-anthony-edwards-injury-return-prediction-looking-like-2027)); *ESPN est.* 21 Dec.
  - From `form.py`: season 33.9 (18), L7 29.8 (4), L15 32.1 (7), L30 33.7 (16), Rate 32.5, projected 46.4.
  - MIN plays at OKC on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **Josh Giddey (CHI, Cream Abdul-Yammar):** CHI did not play on Tuesday ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)).
  - His L7 rose from 40.0 (5) to 46.8 (4) because his 13-FP game of 16 Nov rolled out. It is now 12.5 over his season average. That rests on two games, 58 FP (18 Nov) and 89 FP (22 Nov), beside 16 and 24 FP (`gamelog.py`). His minutes are normal (28.5 over L7, 28.2 for the season).
  - Bleacher Nation calls Monday's late benching situational, tied to the second night of a back-to-back, and reports no role change. Splitter: "I'm here to coach this basketball team, not to make them happy…" ([Bleacher Nation, 24 Nov](https://www.bleachernation.com/bulls/2026/11/24/bulls-bullets-nov-24/)).
  - Norman Powell (right hamstring strain) is due to be re-evaluated later this week ([Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329)); *ESPN est.* 28 Nov.
  - From `form.py`: season 34.2 (17), L7 46.8 (4), L15 38.2 (8), L30 36.8 (14), Rate 40.8, projected 46.2.
  - CHI plays at CHA on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **Brandon Ingram (LAC, Melbourne poopoo):** He has played no game since his debut on Mon 23 Nov, so the flag still rests on one game: a small sample, and noise.
  - New since yesterday: Reuters reports that he "will initially be on a minutes limit." No number was given ([Reuters via Galveston County Daily News, 24 Nov](https://www.galvnews.com/news_reuters/sports/surging-grizzlies-deal-with-key-injuries-as-skidding-clippers-await/article_456dedd3-dd4d-50c5-aef3-d4072f712b69.html)). That firms up yesterday's ClutchPoints view that LAC would "manage" his time.
  - Tyronn Lue says Ingram takes pressure off Darius Garland ([Hoops Rumors, citing Clippers.com, 24 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-ingram-vincent-monk-lakers-dunn.html)).
  - From `form.py`: season, L7, L15 and L30 are all 23.0 (1), small sample; Rate 23.9, small sample; projected 38.5.
  - LAC plays at MEM on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).

**New to the Last 7 days lists:**

- **Nobody:** no player joined either list. Only DET, ORL, BOS, WSH, DAL and DEN played on Tuesday ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)). Lillard's exit and Jokic's entry into the *Under 2026* table are under *Updates* below.

**Updates since 24 Nov:**

- **Cade Cunningham (DET, us, Out):** He was a late scratch on Tue 24 Nov at ORL with right knee soreness. He was listed as probable until the Pistons downgraded him at 6:30 pm ET.
  - It is his second missed game in about a week; he also sat 18 Nov at NO. Bickerstaff: "He's battling through a lot, and I'll leave it at that" ([Detroit Free Press via Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/cade-cunningham-injury-pistons-pg-000304132.html)). That morning he had taken part in shootaround and was called probable ([Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/pistons-issue-health-updates-on-duren-prince-others.html)).
  - No timetable has been reported; *ESPN est.* 27 Nov. DET's next game is Fri 27 Nov vs MIL. Thursday is Thanksgiving, with no games ([ESPN scoreboard, 27 Nov](https://www.espn.com/nba/scoreboard/_/date/20261127)).
  - Without him, Isaiah Joe started and scored 21, and Daniss Jenkins had 15 pts and 10 ast in a 104-86 win ([Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/breaking-news/article/nba-cup-2026-celtics-avert-disaster-mavs-roll-listless-nuggets-pistons-deny-magic-without-cade-cunningham-054349785.html); [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)).
  - His last game, 22 Nov vs ATL: 5 pts (2-9), 4 reb, 15 ast and 6 TO in 33 min, 31 FP, in a 107-97 loss ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)).
  - From `form.py`: season 48.8 (15), L7 39.0 (3), L15 51.5 (6), L30 50.3 (13), Rate 46.9, projected 50.4. His L7 is 9.8 under his season average.
    - The window holds 44, 42 and 31 FP (`gamelog.py`); his 99- and 57-FP games have rolled out.
    - The knee has cost him two of DET's last five games, and his coach says he is playing through it. His minutes are normal when he plays (35.7 over L7, 34.9 for the season).
- **Nikola Jokic (DEN, Lauri Birds, new to the *Under 2026* table):** On Tue 24 Nov vs DAL he had 18 pts (6-14, 1-4 3PT, 5-5 FT), 11 reb, 5 ast, 1 stl and 5 TO in 33 min, 37 FP, in a 120-101 loss ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316)).
  - RotoWire: it was his fifth game this season under 20 points, Dallas clogged the paint against him, and it expects a bounce-back on Fri vs UTA ([RotoWire via CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-nikola-jokic-double-doubles-in-loss-540897/)). No injury was reported.
  - From `form.py`: season 64.6 (16) → 67.2 (15), after dropping his 25-FP game of 22 Oct. L7 62.2 (4), L15 64.8 (8), L30 65.2 (14), Rate 65.0, projected 67.2, 2026 74.9.
- **De'Aaron Fox (SA, Matt Wright's Foxies):** SA did not play on Tuesday. He is questionable for Wed vs POR with a right shin contusion, and Air Alamo expects him back ([Air Alamo, 24 Nov](https://airalamo.com/spurs-vs-trail-blazers-injury-report-wembanyama-and-fox-s-status-plus-why-portland-wants-this-one)); *ESPN est.* 25 Nov.
  - From `form.py`: season 29.5 (16), L7 15.7 (3), L15 24.0 (6), L30 26.1 (13), Rate 23.3. His L7 is unchanged and 13.8 under his season average, from games of 10, 17 and 20 FP (`gamelog.py`).
- **Luka Doncic (LAL, Team Nic Kerr):** LAL did not play on Tuesday, and his L7 is unchanged at 41.0 (4).
  - Austin Reaves (left heel bruise): JJ Redick said "We're optimistic for the rest of this week" after a stay-ready game. LAL's next game is Fri 27 Nov at SA ([SB Nation via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/lakers-optimistic-austin-reaves-return-172225359.html)); *ESPN est.* 27 Nov.
  - From `form.py`: season 60.6 (16) → 63.3 (15), L15 50.6 (7), L30 64.1 (14), Rate 52.6.
- **Tyrese Maxey (PHI, Team Nic Kerr):** PHI has not played since Monday. His L7 fell from 34.3 (3) to 28.0 (2) because his 47-FP game of 16 Nov rolled out (`gamelog.py`). It now rests on two games, a small sample and noise.
  - Joel Embiid is doubtful for Wed vs MIA with an illness, per ESPN's Kris Rhim ([Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-cunningham-antetokounmpo-embiid-williams-anunoby-lendeborg-caruso.html)). No timetable has been reported; *ESPN est.* 27 Nov.
  - From `form.py`: season 44.6 (17), L15 40.3 (6), L30 43.5 (14), Rate 38.3.
- **Michael Porter Jr. (BKN, Team Nic Kerr):** BKN has not played since Monday. His L7 fell from 24.5 (4) to 18.0 (3) because his 44-FP game of 16 Nov rolled out. The window holds 8, 32 and 14 FP (`gamelog.py`), and it is 15.1 under his season average.
  - The reason is production, not minutes (30.7 over L7, 32.7 for the season). No injury has been reported.
  - He told the New York Post, "It's really hard for me right now." Hoops Rumors says he "feels a little lost on the court," and he cites frequent lineup changes and is still adjusting to Julius Randle. He has averaged 10.7 pts on 35.7% shooting over his last three games ([Hoops Rumors, citing the New York Post, 24 Nov](https://www.hoopsrumors.com/2026/11/eastern-notes-michael-porter-jr-vukcevic-joe-black-kevin-porter-jr.html)).
  - From `form.py`: season 33.1 (15), L15 27.8 (5), L30 30.2 (13), Rate 26.6. BKN plays at MIL on Wed 25 Nov.
- **Derrick White (BOS, Dr White Slong, in our pending trades):** On Tue 24 Nov at WSH he had 6 pts (2-10, 2-6 3PT), 7 reb, 5 ast, 1 stl and 0 TO in 30 min, 23 FP, in a 131-116 win ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909315); [FanDuel Research, 25 Nov](https://www.fanduel.com/research/nba/player-news/game-recaps/derrick-white-scores-6-points-in-win-over-wizards-nov-24-2026)).
  - He did not score until late in the second quarter ([SB Nation via Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-survive-scare-nba-cup-034252604.html)). The cause is still the shooting slump in earlier notes.
  - His L7 rose from 22.0 (3) to 25.7 (3) as his 12-FP game of 16 Nov rolled out. His season gap widened from −7.1 to −7.5.
  - From `form.py`: season 29.5 (17), L15 27.1 (7), L30 29.0 (15), Rate 28.1.
- **Alex Sarr (WSH, Team Nic Kerr):** On Tue 24 Nov vs BOS he had 7 pts (3-6, 1-3 3PT), 2 reb, 0 ast and 1 blk in 24 min, 15 FP. Anthony Davis had 33 pts and 13 reb in 37 min ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909315)).
  - His gap widened from −6.2 to −7.1, and his L7 went from 24.5 to 25.2 (4).
  - His minutes are down (23.0 over L7, 26.6 for the season). No injury and no role change has been reported.
  - From `form.py`: season 29.6 (18), L15 29.0 (9), L30 30.2 (15), Rate 28.8.
- **Trae Young (WSH, Team Nic Kerr, near the line):** On Tue 24 Nov vs BOS he had 17 pts (4-9, 8-9 FT), 0 reb, 12 ast, 2 stl and 1 TO in 35 min, 49 FP ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909315)).
  - His gap narrowed from −8.2 to −7.5. From `form.py`: season 36.8 (19), L7 36.0 (4), L15 36.1 (9), L30 35.3 (16), Rate 36.0.
- **Ajay Mitchell (OKC, Lauri Birds):** OKC did not play on Tuesday. His L7 is 22.0 (4), 8.6 under his season average, for the shooting reasons in yesterday's notes.
  - RotoWire tied his larger role to OKC's injuries ([RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/)). Alex Caruso is available for Wed vs MIN after missing three games with a right hip impingement ([The Oklahoman via Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/alex-caruso-injury-okc-thunder-233820218.html)).
  - From `form.py`: season 30.6 (16), L15 24.2 (6), L30 31.9 (14), Rate 26.1.
- **Brandin Podziemski (GS, Matt Wright's Foxies):** GS has not played since 22 Nov, and I found no new news. His L7 fell from 20.8 (4) to 19.0 (3) because his 32-FP game of 16 Nov rolled out (`gamelog.py`).
  - His minutes are normal (33.0 over L7, 32.4 for the season), so the drop is production; no reason was found.
  - From `form.py`: season 31.7 (15), L15 27.0 (7), L30 31.6 (14), Rate 26.0. GS hosts SAC on Wed 25 Nov ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)).
- **Damian Lillard (POR, Matt Wright's Foxies, left the list):** POR did not play on Tuesday ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)). His L7 rose from 27.8 (5) to 31.2 (4) because his 14-FP game of 16 Nov rolled out (`gamelog.py`).
  - From `form.py`: season 30.4 (17), L15 30.2 (8), L30 29.1 (15), Rate 28.4. POR hosts SA on Wed 25 Nov.

**Our near-the-line players:**

- **Jalen Duren (DET, Out):** He was inactive for Tue 24 Nov at ORL. The Pistons assigned him to the Motor City Cruise to practice on Wed 25 Nov, as part of his return to play. They have set no target date ([Hoops Rumors, citing Pistons PR, 24 Nov](https://www.hoopsrumors.com/2026/11/pistons-issue-health-updates-on-duren-prince-others.html)).
  - Brett Siegel called his return "imminent" ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/detroit-pistons/pistons-news-jalen-duren-g-league-move)). No timetable has been reported; *ESPN est.* 30 Nov. The news-watch override (return 1 Dec) stays in force.
  - Paul Reed played 22 min off the bench behind starter John Collins, with 9 pts and 6 reb ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)).
  - From `form.py`: season 33.5 (2) → 44.0 (1), small sample; Rate 44.1, small sample.
- **Matas Buzelis (CHI):** CHI did not play on Tuesday. On the late benching on 23 Nov he said: "As a competitor, I always think I should play. But we won the game, so I don't really care…" Bleacher Nation reports no role change ([Bleacher Nation, 24 Nov](https://www.bleachernation.com/bulls/2026/11/24/bulls-bullets-nov-24/)).
  - Jalen Smith is questionable for Wednesday; if he sits, RotoWire expects Nic Claxton to start ([RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jalen-smith-injury-iffy-for-wednesday-540841)).
  - From `form.py`: season 25.7 (17), L7 33.0 (4), L15 30.2 (8), L30 26.7 (14), Rate 30.0, projected 32.5.
    - His L7 is 7.3 over his season average, from the 54-FP (18 Nov) and 39-FP (22 Nov) games and more minutes (30.0 over L7, 27.8 for the season).
    - It slipped from 33.4 (5) to 33.0 (4) as his 33-FP game of 16 Nov rolled out.
- **Kawhi Leonard (TOR, Out):** The Raptors' promised update came on Tue 24 Nov. He has begun individual on-court workouts while being treated for swelling in his left knee, and will be re-evaluated in one week. That puts the re-evaluation around 1 Dec ([RotoWire, citing ESPN's Marc J. Spears, 24 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-to-be-re-evaluated-in-one-week-540857)).
  - He will miss the games against BKN (Fri 27 Nov) and DEN. Hoops Rumors' writer would be "surprised if he's cleared to return next Tuesday in Houston." That is the writer's view, not the team's ([Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/raptors-rule-out-kawhi-leonard-another-week.html)).
  - Reported timeline: re-evaluation in one week; *ESPN est.* 3 Dec.
  - From `form.py`: season 40.0 (2), small sample; Rate 43.3, small sample.
- **Trey Murphy III (NO):** NO has not played since Mon 23 Nov, and its next game is Fri 27 Nov at LAC ([ESPN scoreboard, 27 Nov](https://www.espn.com/nba/scoreboard/_/date/20261127)). I found no news dated after 23 Nov.
  - The news watch still flags a rest risk on the second night of the Sun 29–Mon 30 Nov back-to-back. He sat the second night of the 20–21 Nov back-to-back ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns)).
  - From `form.py`: season 31.1 (11), L7 31.5 (2, small sample, noise), L15 31.5 (2, small sample), L30 32.2 (8), Rate 32.3, projected 36.8. His L15 fell from 35.7 (3) because his 44-FP game of 8 Nov rolled out (`gamelog.py`).

**Our pending trades:**

These are the players new to the offers or with news since yesterday. Each one's windows are in the trade tables. Ball, Giddey and Ingram are under *Flagged*; Buzelis, Duren, Murphy and Leonard are under *Our near-the-line players*; Derrick White is under *Updates*.

- **Zion Williamson (NO, we receive, new):** He missed Sat 21 Nov at SA with a left thigh contusion and was listed probable for Monday ([Suns On SI via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/zion-williamson-highlights-suns-pelicans-235713521.html)).
  - He started Mon 23 Nov vs PHX: 25 pts (10-18, 5-5 FT), 4 reb, 0 ast, 1 stl and 6 TO in 40 min, 25 FP, in a 123-119 overtime loss ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)). ESPN lists him active.
  - From `form.py`: season 40.7 (17), L7 35.0 (3), L15 38.4 (7), L30 41.1 (14), Rate 38.1, projected 40.0, 2026 37.9.
    - His L7 is 5.7 under his season average. The window holds 32, 48 and 25 FP (`gamelog.py`); his 36-FP game of 16 Nov rolled out.
    - Monday's six turnovers and no assists are the reason; his minutes are up (36.3 over L7, 32.9 for the season).
  - NO plays next on Fri 27 Nov at LAC.
- **Anthony Black (ORL, we send; in 6 of 16 offers, all five new ones):** On Tue 24 Nov vs DET he had 5 pts (2-8, 0-2 3PT, 1-3 FT), 4 reb, 2 ast, 1 blk and 5 TO in 28 min, 3 FP, in a 104-86 loss ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)).
  - Black and Jalen Suggs "looked overmatched by the Pistons' pressure defense" ([Orlando Magic Daily, 24 Nov](https://orlandomagicdaily.com/orlando-magic-let-another-chance-advance-past-detroit-pistons-slip-away-01m8823dzz3j)). No injury was reported.
  - Hoops Rumors calls it one of his roughest outings of the season. It also notes that free agent Kevin Porter Jr. met with Orlando on Monday. The Stein Line reported the meeting, and the Orlando Sentinel's Jason Beede confirmed it. That could mean more competition at point guard, but no deal has been reported ([Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/eastern-notes-michael-porter-jr-vukcevic-joe-black-kevin-porter-jr.html)).
  - From `form.py`: season 35.3 (14), L7 25.5 (4), L15 32.9 (8), L30 35.3 (14), Rate 31.1, projected 28.2.
    - His L7 is 9.8 under his season average: Tuesday's 3-FP game came in, and his 47-FP game of 16 Nov rolled out (`gamelog.py`).
    - His minutes are normal (34.2 over L7, 32.9 for the season), so it is one bad game, not a role change.
- **Paul George (BOS, we send in Cream Abdul-Yammar's two offers):** On Tue 24 Nov at WSH he had 28 pts (11-20, 6-9 3PT), 4 reb, 9 ast, 1 stl and 1 TO in 33 min, 60 FP ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909315)). He became the eighth player with 2,500 career threes ([ClutchPoints via Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-paul-george-hits-rare-044233951.html)).
  - His gap rose from +2.1 to +3.4. From `form.py`: season 41.9 (15), L7 44.0 (3), L15 42.7 (6), L30 40.3 (13), Rate 42.1.
- **Jalen Smith (CHI, we send, day-to-day):** He is questionable for Wed at CHA with a gastrointestinal illness, which he played through on Monday ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/jalen-smith-tummy-bug-questionable-wednesday); [RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jalen-smith-injury-iffy-for-wednesday-540841)).
  - Reported timeline: questionable for Wednesday; *ESPN est.* 25 Nov.
  - From `form.py`: season 37.4 (15) → 39.4 (14), L7 42.0 (3), L15 46.2 (6), L30 38.4 (12) → 41.0 (11), Rate 41.5.
- **Karl-Anthony Towns (NY, we receive, day-to-day):** He is questionable for Wed vs CLE with right knee inflammation. If he sits, Andre Drummond starts ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/karl-anthony-towns-knee-questionable-wednesday)).
  - No timetable beyond Wednesday has been reported; *ESPN est.* 25 Nov.
  - From `form.py`: season 53.0 (16) → 54.5 (15), L7 65.3 (3), L15 60.0 (7), L30 54.3 (14) → 56.2 (13), Rate 59.3.
- **Anthony Edwards (MIN, we receive, Out):** The new reported timeline is "into January," from The Athletic's Jon Krawczynski ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-rumors-insider-anthony-edwards-injury-return-prediction-looking-like-2027)); *ESPN est.* 21 Dec. From `form.py`: season 52.5 (4), L30 51.5 (2, small sample), Rate 51.0.
- **Everyone else in the offers:** Castle, Fears, Dosunmu, Quickley, Diabate, Harden, McDaniels, Alexander-Walker, Randle, Lopez, Brunson and Mitchell have nothing new. None of their teams played on Tuesday ([ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124)), and yesterday's notes stand.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| LaMelo Ball | MIN | #2 | 18 | 28.5 / 32.9 | 0.84 | 33.9 (18) | 29.8 (4) | 32.1 (7) | 33.7 (16) | 46.4 | **−12.5** | 41.1 | Active |
| Josh Giddey | CHI | #3 | 17 | 28.2 / 35.5 | 0.93 | 34.2 (17) | 46.8 (4) | 38.2 (8) | 36.8 (14) | 46.2 | **−11.9** | 46.2 | Active |

- **LaMelo Ball** (both): scoring −6.9, reb −1.4, ast −5.4, stocks +0.6, TO −0.1; bonus +0.6.
  - Current: 28.5 min, 17.2 pts, 6.2-15.1 FG, 1.7-2.2 FT, 4.2 reb, 5.6 ast, 1.7 stl, 0.2 blk, 3.3 TO
  - Last 7 days (4 GP): 32.0 min, 15.5 pts, 6.0-16.0 FG, 1.2-1.5 FT, 6.0 reb, 5.0 ast, 0.8 stl, 0.5 blk, 2.5 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Josh Giddey** (minutes): scoring −8.8, reb −3.1, ast −0.5, stocks −3.2, TO +0.9; bonus +2.8.
  - Current: 28.2 min, 10.4 pts, 4.1-9.6 FG, 1.1-1.8 FT, 6.1 reb, 9.4 ast, 0.4 stl, 0.6 blk, 3.4 TO
  - Last 7 days (4 GP): 28.5 min, 11.8 pts, 5.2-11.5 FG, 0.5-0.8 FT, 9.0 reb, 12.2 ast, 0.5 stl, 0.5 blk, 3.5 TO
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

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −6.8 (#9, efficiency, L7 33.0), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.7 (#7, efficiency, L7 31.5).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −7.5 (#9, efficiency, L7 26.2), Derrick White −7.5 (#6, minutes, L7 25.7), Joel Embiid −6.0 (#3, efficiency, L7 59.5).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Darius Garland −6.8 (#5, efficiency, L7 38.8), Kevin Durant −6.6 (#4, efficiency, L7 38.3), Ivica Zubac −6.2 (#7, minutes, L7 35.2).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** De'Aaron Fox −8.7 (#7, efficiency, L7 15.7), Damian Lillard −8.2 (#6, efficiency, L7 31.2), Shai Gilgeous-Alexander −8.0 (#1, efficiency, L7 55.7), Brandon Miller −7.4 (#8, minutes, L7 34.7).

### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.3 (#1, efficiency, L7 48.7).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −7.5 (#4, efficiency, L7 36.0), Alex Sarr −7.1 (#7, efficiency, L7 25.2), James Harden −6.8 (#5, efficiency, L7 47.0), Michael Porter Jr. −5.9 (#6, efficiency, L7 18.0).

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

- **Flagged, but within 10 of projection over the last 7 days:** Josh Giddey (Cream Abdul-Yammar, L7 46.8 in 4 vs projected 46.2, season gap −11.9).
- **Not flagged, but 10+ under projection over the last 7 days:** Cade Cunningham (Come-in Cider (us), L7 39.0 in 3 vs projected 50.4, L7 gap −11.4, season gap −1.6), De'Aaron Fox (Matt Wright's Foxies, L7 15.7 in 3 vs projected 38.2, L7 gap −22.5, season gap −8.7), Michael Porter Jr. (Team Nic Kerr, L7 18.0 in 3 vs projected 38.9, L7 gap −20.9, season gap −5.9), Luka Doncic (Team Nic Kerr, L7 41.0 in 4 vs projected 60.6, L7 gap −19.6, season gap −0.1), Tyrese Maxey (Team Nic Kerr, L7 28.0 in 2 vs projected 45.1, L7 gap −17.1, season gap −0.5), Brandin Podziemski (Matt Wright's Foxies, L7 19.0 in 3 vs projected 30.8, L7 gap −11.8, season gap 0.9), Alex Sarr (Team Nic Kerr, L7 25.2 in 4 vs projected 36.6, L7 gap −11.4, season gap −7.1), Derrick White (Dr White Slong, L7 25.7 in 3 vs projected 37.0, L7 gap −11.3, season gap −7.5), Ajay Mitchell (Lauri Birds, L7 22.0 in 4 vs projected 32.8, L7 gap −10.8, season gap −2.2).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | — | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | 41.6 |
| Nikola Jokic | Lauri Birds | 16 | 36.9 / 35.6 | 64.6 | 62.2 (4) | 64.8 (8) | 65.2 (14) | 67.2 | 74.9 |

## Our pending trades

With **Team Nic Kerr**, proposed by us, expires 26 Nov 02:41 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Moussa Diabate | we receive | 14 | 30.0 / 24.6 | 36.9 | 43.3 (3) | 40.2 (5) | 38.2 (11) | 24.0 | +12.9 | Active |
| James Harden | we receive | 17 | 33.7 / 33.6 | 35.3 | 47.0 (3) | 42.3 (7) | 36.8 (15) | 42.1 | −6.8 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 01:35 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jaden McDaniels | we receive | 18 | 34.0 / 31.7 | 41.0 | 53.5 (4) | 47.9 (7) | 41.1 (16) | 29.7 | +11.3 | Active |
| Stephon Castle | we receive | 18 | 29.9 / 32.7 | 36.3 | 42.8 (4) | 41.1 (8) | 36.1 (15) | 36.9 | −0.6 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |

With **Melbourne poopoo**, proposed by us, expires 27 Nov 01:47 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Zion Williamson | we receive | 17 | 32.9 / 30.9 | 40.7 | 35.0 (3) | 38.4 (7) | 41.1 (14) | 40.0 | +0.7 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed by us, expires 27 Nov 01:52 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| LaMelo Ball | we receive | 18 | 28.5 / 32.9 | 33.9 | 29.8 (4) | 32.1 (7) | 33.7 (16) | 46.4 | −12.5 | Active |
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 36.8 (4) | 35.0 (9) | 37.8 (16) | 27.3 | +6.1 | Active |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed by us, expires 26 Nov 02:45 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | we receive | 17 | 28.2 / 35.5 | 34.2 | 46.8 (4) | 38.2 (8) | 36.8 (14) | 46.2 | −11.9 | Active |
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 36.8 (4) | 35.0 (9) | 37.8 (16) | 27.3 | +6.1 | Active |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed to us, expires 25 Nov 11:54 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Immanuel Quickley | we receive | 15 | 32.1 / 31.4 | 34.1 | 31.2 (4) | 33.0 (7) | 34.0 (13) | 34.9 | −0.8 | Active |
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 36.8 (4) | 35.0 (9) | 37.8 (16) | 27.3 | +6.1 | Active |
| Paul George | we send | 15 | 30.3 / 33.2 | 41.9 | 44.0 (3) | 42.7 (6) | 40.3 (13) | 38.5 | +3.4 | Active |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 02:52 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Karl-Anthony Towns | we receive | 16 | 32.5 / 32.7 | 53.0 | 65.3 (3) | 60.0 (7) | 54.3 (14) → 56.2 (13) | 44.1 | +8.9 | Day-to-day, ESPN est. back 25 Nov |
| Jalen Duren | we send | 2 | 19.0 / 31.0 | 33.5 | — | — | — | 42.2 | −8.7 | **Out**, ESPN est. back 30 Nov |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Dr White Slong**, proposed by us, expires 26 Nov 01:38 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Donovan Mitchell | we receive | 17 | 33.2 / 33.9 | 42.8 | 40.3 (3) | 42.4 (7) | 42.4 (15) | 46.5 | −3.7 | Active |
| Derrick White | we receive | 17 | 30.0 / 34.3 | 29.5 | 25.7 (3) | 27.1 (7) | 29.0 (15) | 37.0 | −7.5 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |

With **Cream Abdul-Yammar**, proposed to us, expires 25 Nov 12:11 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jeremiah Fears | we receive | 19 | 30.8 / 26.4 | 33.4 | 36.8 (4) | 35.0 (9) | 37.8 (16) | 27.3 | +6.1 | Active |
| Ayo Dosunmu | we receive | 18 | 31.7 / 29.4 | 34.9 | 33.2 (4) | 31.1 (7) | 34.2 (16) | 30.4 | +4.5 | Active |
| Paul George | we send | 15 | 30.3 / 33.2 | 41.9 | 44.0 (3) | 42.7 (6) | 40.3 (13) | 38.5 | +3.4 | Active |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 03:28 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Brandon Ingram | we receive | 1 | 27.0 / 35.3 | 23.0 | 23.0 (1) | 23.0 (1) | 23.0 (1) | 38.5 | −15.5 | Active |
| Stephon Castle | we receive | 18 | 29.9 / 32.7 | 36.3 | 42.8 (4) | 41.1 (8) | 36.1 (15) | 36.9 | −0.6 | Active |
| Matas Buzelis | we send | 17 | 27.8 / 30.5 | 25.7 | 33.0 (4) | 30.2 (8) | 26.7 (14) | 32.5 | −6.8 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |

With **Melbourne poopoo**, proposed by us, expires 27 Nov 01:52 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jaden McDaniels | we receive | 18 | 34.0 / 31.7 | 41.0 | 53.5 (4) | 47.9 (7) | 41.1 (16) | 29.7 | +11.3 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Dr White Slong**, proposed by us, expires 26 Nov 01:49 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Nickeil Alexander-Walker | we receive | 17 | 31.6 / 32.3 | 34.6 | 31.7 (3) | 35.3 (6) | 33.1 (14) | 34.1 | +0.6 | Active |
| Julius Randle | we receive | 16 | 33.1 / 34.3 | 36.2 | 40.3 (3) | 41.0 (6) | 35.0 (14) | 37.0 | −0.9 | Active |
| Derrick White | we receive | 17 | 30.0 / 34.3 | 29.5 | 25.7 (3) | 27.1 (7) | 29.0 (15) | 37.0 | −7.5 | Active |
| Matas Buzelis | we send | 17 | 27.8 / 30.5 | 25.7 | 33.0 (4) | 30.2 (8) | 26.7 (14) | 32.5 | −6.8 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |
| Brook Lopez | we send | 16 | 24.4 / 26.2 | 29.8 | 30.8 (4) | 31.1 (7) | 27.9 (14) | 26.2 | +3.6 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 00:57 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Anthony Edwards | we receive | 4 | 33.8 / 35.8 | 52.5 | — | — | 51.5 (2) | 47.2 | +5.3 | **Out**, ESPN est. back 21 Dec |
| Trey Murphy III | we send | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | −5.7 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Cream Abdul-Yammar**, proposed by us, expires 27 Nov 01:49 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | we receive | 17 | 28.2 / 35.5 | 34.2 | 46.8 (4) | 38.2 (8) | 36.8 (14) | 46.2 | −11.9 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |

With **Dr White Slong**, proposed by us, expires 27 Nov 01:17 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Julius Randle | we receive | 16 | 33.1 / 34.3 | 36.2 | 40.3 (3) | 41.0 (6) | 35.0 (14) | 37.0 | −0.9 | Active |
| Derrick White | we receive | 17 | 30.0 / 34.3 | 29.5 | 25.7 (3) | 27.1 (7) | 29.0 (15) | 37.0 | −7.5 | Active |
| Matas Buzelis | we send | 17 | 27.8 / 30.5 | 25.7 | 33.0 (4) | 30.2 (8) | 26.7 (14) | 32.5 | −6.8 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 35.3 (14) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 26 Nov 03:02 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jalen Brunson | we receive | 17 | 34.2 / 35.3 | 41.7 | 43.2 (4) | 44.2 (8) | 44.0 (15) | 43.8 | −2.1 | Active |
| Jalen Smith | we send | 15 | 25.3 / 19.5 | 37.4 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | 22.4 | +15.0 | Day-to-day, ESPN est. back 25 Nov |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-25 09:06 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research links:** [ESPN scoreboard, 24 Nov](https://www.espn.com/nba/scoreboard/_/date/20261124) · [Dunking With Wolves, 21 Nov](https://dunkingwithwolves.com/lamelo-ball-s-defensive-improvement-is-helping-the-timberwolves-survive-his-slump) · [ClutchPoints, 24 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-rumors-insider-anthony-edwards-injury-return-prediction-looking-like-2027) · [ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125) · [Bleacher Nation, 24 Nov](https://www.bleachernation.com/bulls/2026/11/24/bulls-bullets-nov-24/) · [Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329) · [Reuters via Galveston County Daily News, 24 Nov](https://www.galvnews.com/news_reuters/sports/surging-grizzlies-deal-with-key-injuries-as-skidding-clippers-await/article_456dedd3-dd4d-50c5-aef3-d4072f712b69.html) · [Hoops Rumors, citing Clippers.com, 24 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-ingram-vincent-monk-lakers-dunn.html) · [Detroit Free Press via Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/cade-cunningham-injury-pistons-pg-000304132.html) · [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/pistons-issue-health-updates-on-duren-prince-others.html) · [ESPN scoreboard, 27 Nov](https://www.espn.com/nba/scoreboard/_/date/20261127) · [Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/breaking-news/article/nba-cup-2026-celtics-avert-disaster-mavs-roll-listless-nuggets-pistons-deny-magic-without-cade-cunningham-054349785.html) · [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029) · [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316) · [RotoWire via CBS Sports, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-nikola-jokic-double-doubles-in-loss-540897/) · [Air Alamo, 24 Nov](https://airalamo.com/spurs-vs-trail-blazers-injury-report-wembanyama-and-fox-s-status-plus-why-portland-wants-this-one) · [SB Nation via Yahoo Sports, 24 Nov](https://sports.yahoo.com/articles/lakers-optimistic-austin-reaves-return-172225359.html) · [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-cunningham-antetokounmpo-embiid-williams-anunoby-lendeborg-caruso.html) · [Hoops Rumors, citing the New York Post, 24 Nov](https://www.hoopsrumors.com/2026/11/eastern-notes-michael-porter-jr-vukcevic-joe-black-kevin-porter-jr.html) · [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909315) · [FanDuel Research, 25 Nov](https://www.fanduel.com/research/nba/player-news/game-recaps/derrick-white-scores-6-points-in-win-over-wizards-nov-24-2026) · [SB Nation via Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-survive-scare-nba-cup-034252604.html) · [RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/) · [The Oklahoman via Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/alex-caruso-injury-okc-thunder-233820218.html) · [ClutchPoints, 24 Nov](https://clutchpoints.com/nba/detroit-pistons/pistons-news-jalen-duren-g-league-move) · [RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jalen-smith-injury-iffy-for-wednesday-540841) · [RotoWire, citing ESPN's Marc J. Spears, 24 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-to-be-re-evaluated-in-one-week-540857) · [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/raptors-rule-out-kawhi-leonard-another-week.html) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns) · [Suns On SI via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/zion-williamson-highlights-suns-pelicans-235713521.html) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042) · [Orlando Magic Daily, 24 Nov](https://orlandomagicdaily.com/orlando-magic-let-another-chance-advance-past-detroit-pistons-slip-away-01m8823dzz3j) · [ClutchPoints via Yahoo Sports, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-paul-george-hits-rare-044233951.html) · [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/jalen-smith-tummy-bug-questionable-wednesday) · [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/karl-anthony-towns-knee-questionable-wednesday)
