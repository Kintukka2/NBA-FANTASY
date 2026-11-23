# Slump Watch: 23 Nov 2026

- Generated 2026-11-23 04:12 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 34. Teams have played **2 to 18 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 34 (Sun 22 Nov US) re-scored from ESPN's final NBA box scores: all 46 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**2 rostered players are 10+ FP/g under projection, on 1 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.2/60.5 · LaMelo Ball 34.2/46.4 · Josh Giddey 34.9/46.2 |
| Come-in Cider (us) | 0 | Cade Cunningham 48.8/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 50.3/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 42.4/46.5 · Joel Embiid 39.4/45.4 |
| Lauri Birds | 0 | Nikola Jokic 66.4/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.4/56.8 · Cooper Flagg 49.2/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 49.4/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 53.0/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 43.7/50.0 · Jayson Tatum 46.0/48.1 · Kyrie Irving 40.8/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 62.1/60.6 · Domantas Sabonis 43.3/46.7 · Tyrese Maxey 45.6/45.1 |

## Since the last Slump Watch

Against [20261122-slump-watch.md](20261122-slump-watch.md):
- **Joined the flagged list:** nobody.
- **Left it:** nobody. Josh Giddey and LaMelo Ball are still flagged.
- **Gaps that moved 3+ FP/g:** Josh Giddey, −14.9 → −11.3 (+3.6), after his 89-FP triple-double on Sun 22 Nov. No other gap in either report's tables moved 3 or more.
- **New to the Last 7 days lists:** Josh Giddey joined *flagged, but within 10 over the last 7 days*. Cade Cunningham (us), Derrick White and Brandin Podziemski joined *not flagged, but 10+ under over the last 7 days*. Josh Hart left that list.
- **Near the line:** Jalen Suggs (Lauri Birds, −6.2) joined. Norman Powell (−5.9) left: ESPN now lists him on waivers, out with a hamstring strain.
- **Under 2026, not under projection:** Nikola Jokic and Josh Hart left the table.
- **Our pending trades:** new. We proposed a trade to Dr White Slong: Anthony Black, Trey Murphy III and Kawhi Leonard for Donovan Mitchell and Derrick White. It expires 25 Nov 04:05 UTC.
- **Brandon Ingram** (Melbourne poopoo) is now Active on ESPN (yesterday: Out, ESPN est. 23 Nov). He still has no games.

## Research

**Flagged:**

- **Josh Giddey (CHI):** On Sun 22 Nov he had 23 pts (10-17, 2-5 3PT), 14 reb, a career-high 22 ast, 1 blk and 5 TO in 41 min, an 89-FP night, in a 151-145 overtime loss to DEN ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032)). The 22 assists are the most in any NBA game this season. He scored all seven of the Bulls' fourth-quarter points and tied the game with a layup with 2.1 seconds left in regulation ([SI / OnSI, 22 Nov](https://www.si.com/nba/bulls/onsi/3-takeaways-after-bulls-waste-josh-giddey-s-22-assist-night-in-ot-loss-to-nuggets-22)).
  - The game came two nights after Tiago Splitter benched him and Matas Buzelis late in the 20 Nov loss to WSH. Neither player was happy with the benching, and Giddey at first felt it wasn't warranted. Splitter talked with both on Saturday and said "It's not personal." Giddey said Splitter "doesn't sugarcoat it, he tells you what you need to hear" ([Chicago Sun-Times, 22 Nov](https://chicago.suntimes.com/bulls/2026/11/22/coach-tiago-splitter-bulls-culture-built-accountability)).
  - Norman Powell, CHI's leading scorer, missed the game with a mild right hamstring strain. He will be re-evaluated later this week and is likely to miss at least the DEN, CLE (Mon 23 Nov) and CHA (Wed 25 Nov) games ([Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329)). *ESPN est.* 28 Nov.
  - From `form.py`: season 34.9 (16), L7 44.0 (4), L15 42.5 (8), L30 37.0 (15), Rate 41.1, projected 46.2. His L7 is 9.1 over his season average. That comes from two big nights, 58 FP on 18 Nov and 89 FP on 22 Nov. In between he had 16 FP in 23 min in the benching game. His minutes held steady (29.0 over L7, 28.6 for the season); the 41 minutes on Sunday included overtime.
- **LaMelo Ball (MIN):** Nothing new since 22 Nov. MIN had no game on Sunday and hosts BKN on Mon 23 Nov ([ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122); [ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)). His L7 fell from 29.0 (5) to 24.8 (4), 9.4 under his season average of 34.2. No new game caused it. His 45-FP game of 14 Nov rolled out of the window, and his 9-FP, 24-minute game of 16 Nov is still in it (per `gamelog.py`). The reason is still his shooting, as in yesterday's notes. His minutes are 30.5 over L7. From `form.py`: L15 33.7 (7), L30 33.7 (16), Rate 31.3, projected 46.4.

**New to the Last 7 days lists:**

- **Cade Cunningham (DET, us):** On Sun 22 Nov at ATL he had a season-low 5 pts (2-9 FG, 1-3 3PT), a season-high 15 ast, 4 reb, 1 stl, 1 blk and 6 TO in 33 min in a 107-97 loss. DET was outscored 33-12 in the fourth quarter ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). J.B. Bickerstaff said "I think he made the right basketball play" and that ATL was "putting two bodies on him all the time." Cunningham played through right knee soreness ([Detroit Sports Nation via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/j-b-bickerstaff-explains-cade-010500296.html)).
  - The knee cost him the 18 Nov game at NO ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910013)). Since then he has been listed as probable and has played through what RotoWire calls minor soreness ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/cade-cunningham-injury-probable-for-sunday-540377)). No timetable has been reported, and none appears needed. ESPN lists him active, so there is no ESPN est.
  - Why his L7 dropped: L7 39.0 (3) is 9.8 under his season average of 48.8. Most of the drop is the window. His 99-FP game of 12 Nov and 57-FP game of 14 Nov rolled out. The missed game leaves three games: 44, 42 and 31 FP. His minutes are normal (35.7 over L7, 34.9 for the season). From `form.py`: L15 48.7 (7), L30 49.5 (14), Rate 46.0, projected 50.4. DET next plays Tue 24 Nov at ORL ([ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/det/detroit-pistons)).
- **Derrick White (BOS, in our pending trade):** He missed Sat 21 Nov at SAC with a left AC joint sprain ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910028)). He returned on Sun 22 Nov with 14 pts on 6-21 FG (2-12 3PT), 3 reb, 5 ast, 1 stl and 1 TO in 32 min in an 88-87 loss at GS ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035)). He had an open look on Boston's final possession and passed instead ([NBC Sports Boston, 22 Nov](https://www.nbcsportsboston.com/nba/boston-celtics/warriors-live-updates-jayson-tatum/815226/)).
  - The cause is a three-point slump. His last three games: 1-6 (16 Nov), 0-7 (18 Nov) and 2-12 (22 Nov) from three ([ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909994); [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910015)). Through 15 games he shot 30.6% from three on 5.7 attempts, against 8.3 last season. He is nearly 6 points below his expected rate on tracked attempts, though he "is getting better looks this year" ([NBC Sports Boston, 21 Nov](https://www.nbcsportsboston.com/nba/boston-celtics/celtics-mailbag-mitchell-robinson-derrick-white-jayson-tatum/814956/)). Joe Mazzulla on 20 Nov: "I'm not concerned about him at all … I trust him to make them, and I think he will" ([Heavy, 22 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-joe-mazzulla-delivers-verdict-on-derrick-whites-shooting-struggles/)).
  - From `form.py`: season 29.9 (16), L7 26.2 (4), L15 29.6 (7), L30 29.6 (15), Rate 29.1, projected 37.0. His L7 is 3.7 under his season average, inside the 5-point line; his minutes are normal (30.5 over L7). BOS next plays Tue 24 Nov at WSH ([ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/bos/boston-celtics)).
- **Brandin Podziemski (GS):** His minutes are normal (32.2 over L7, 32.4 for the season), and the drop is shooting and usage.
  - Last three games: 10 pts (0-5 3PT) at DAL on 18 Nov and 15 pts (0-5 3PT) at MEM on 19 Nov ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910016); [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019)). Then 18 pts (5-14, 4-10 3PT), 7 reb, 2 ast and 6 TO in 38 min in the 88-87 win over BOS on 22 Nov, which ended GS's five-game skid ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035)).
  - Before Sunday he had averaged 12.0 pts on 10.8 shots over four games. His usage over that stretch ranked only sixth on the team, below Georges Niang's, even with Stephen Curry out. Podziemski has argued against forcing offense ([EssentiallySports via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/brandin-podziemski-sends-message-locker-015921068.html)).
  - Curry (right oblique tear): Brett Siegel puts typical recovery at 4–6 weeks and expects a return "very likely … sometime before" the 25 Dec game. The Warriors have given no timeline ([Yardbarker, 20 Nov](https://www.yardbarker.com/nba/articles/insider_provides_major_injury_update_on_stephen_curry_as_warriors_losing_streak_continues/s1_17730_44593775)). *ESPN est.* 12 Dec.
  - From `form.py`: season 31.7 (15), L7 20.8 (4), L15 29.0 (8), L30 31.7 (15, equal to the season), Rate 27.2, projected 30.8. His L7 is 11.0 under his season average. GS next plays Wed 25 Nov vs SAC ([ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/gs/golden-state-warriors)).

**Updates since 22 Nov:**

- **De'Aaron Fox (SA):** New: questionable for Mon 23 Nov at SAC with a right shin contusion, likely picked up in Saturday's game vs NO. SA could be short of lead guards ([RotoWire, 22 Nov](https://www.rotowire.com/basketball/headlines/deaaron-fox-injury-questionable-for-monday-540571)). ESPN lists him day-to-day with a right lower leg bruise. No timetable has been reported beyond Monday; *ESPN est.* 23 Nov. SA had no game on Sunday ([ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122)). Dylan Harper is still out (hip): 2–3 weeks reported ([ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html)); *ESPN est.* 13 Dec.
- **Trae Young (WSH):** On Sun 22 Nov he had 11 pts (3-10, 3-7 3PT), 4 reb, 11 ast, 1 stl and 3 TO in 28 min in a 116-96 rout of ORL ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031)). It was WSH's third straight win after an eight-game skid; Kyshawn George scored 24 and Anthony Davis 22 ([AP via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/wizards-rout-magic-116-96-023006979.html)). He came in shooting 36.7% from the field. It was his seventh double-digit assist game, and Rotoworld suggests buying low for assists ([NBC Sports, 22 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-22/trae-young-dishes-out-11-assists-vs-orlando)). From `form.py`: season 36.2 (18), L7 30.4 (5), L15 32.1 (9), L30 35.6 (17), Rate 33.0. His L7 is 5.8 under his season average, for two reasons:
  - shooting;
  - minutes: 30.8 over L7 against 34.6, including 26 on 15 Nov and 28 in Sunday's blowout.
- **Luka Doncic (LAL):** No game since 20 Nov; LAL hosts UTA on Mon 23 Nov ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)). The Lakers' Monday injury report lists only Austin Reaves, out with a left heel bruise. Redick implied Reaves could return "over the next few games" ([Heavy, 22 Nov](https://heavy.com/sports/nba/los-angeles-lakers/lakers-reveal-shocking-update-austin-reaves/)). *ESPN est.* 27 Nov for Reaves. Doncic, poked in the eye on 20 Nov, is not on the report, and Heavy expects him to carry more of the offense without Reaves.
- **Damian Lillard (POR):** Nothing new since 22 Nov. POR had no game on Sunday and plays Mon 23 Nov at PHI ([ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122); [ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)).
- **Michael Porter Jr. (BKN):** Nothing new since 22 Nov. BKN had no game on Sunday and plays Mon 23 Nov at MIN (same sources).
- **Brandon Miller (CHA):** New: ESPN now lists him day-to-day with a right knee bruise; *ESPN est.* 23 Nov. The NBA injury report has him probable for Mon 23 Nov vs MEM with a right knee bone bruise from the 20 Nov loss at ATL, a game he returned to in the second quarter ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/brandon-miller-knee-probable-monday-vs-memphis)). No timetable reported, and none appears needed. CHA had no game on Sunday.
- **Josh Hart (NY, left the Last 7 days list):** On Sun 22 Nov he had a triple-double: 10 pts (5-11, 0-4 3PT), 11 reb, 10 ast and 1 stl in 39 min in a 113-106 win over IND. Karl-Anthony Towns returned from illness with 30 pts and 13 reb ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)). His near-the-line gap narrowed from −9.2 to −7.5.

**Our near-the-line players:**

- **Jalen Duren (DET, Out):** He was still out for the 22 Nov game at ATL with the right hamstring strain ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029)). New since yesterday's notes: HEAVY's 22 Nov injury-report piece says he is "closer to returning, possibly later this week depending on" his re-evaluation ([HEAVY via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/detroit-pistons-announce-injury-report-071434249.html)). No result of the re-evaluation and no return date have been reported. *ESPN est.* 24 Nov. DET's next games are Tue 24 Nov at ORL and Fri 27 Nov vs MIL ([ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/det/detroit-pistons)). From `form.py`: season 33.5 (2) → 44.0 (1), small sample; Rate 44.1, small sample.
- **Matas Buzelis (CHI):** On Sun 22 Nov he had 21 pts (7-17, 4-12 3PT), 5 reb, 3 ast, 2 blk and 1 TO in 38 min against DEN ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032)). He played crunch time, two nights after his late benching. He hit a go-ahead three for 124-121 and found Giddey for the tying layup ([SI / OnSI, 22 Nov](https://www.si.com/nba/bulls/onsi/3-takeaways-after-bulls-waste-josh-giddey-s-22-assist-night-in-ot-loss-to-nuggets-22); [Chicago Sun-Times, 22 Nov](https://chicago.suntimes.com/bulls/2026/11/22/coach-tiago-splitter-bulls-culture-built-accountability)).
  - With Norman Powell out, Buddy Hield started and scored 33 (SI / OnSI, same). Powell: re-evaluation later this week, likely out through at least Wed 25 Nov ([Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329)); *ESPN est.* 28 Nov.
  - From `form.py`: season 25.7 (16), L7 35.2 (4), L15 31.6 (8), L30 26.1 (15), Rate 31.0, projected 32.5. His L7 is 9.6 over his season average. That comes from volume and shooting in big games (16, 18 and 22 Nov), with his minutes up to 31.0 over L7 from 27.9. CHI hosts CLE on Mon 23 Nov.
- **Trey Murphy III (NO, day-to-day):** New: he is probable for Mon 23 Nov vs PHX on the NBA injury report. No minutes limit has been named for Monday; he had "close to a full workload" (29 min) in his 20 Nov return. If he starts, Saddiq Bey or Herbert Jones goes to the bench ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/trey-murphy-knee-probable-vs-phoenix-on-monday)). *ESPN est.* 23 Nov. From `form.py`: season 31.7 (10), L7 38.0 (1, small sample), L15 41.0 (2, small sample), L30 33.4 (9), Rate 37.3. The likely rest on 30 Nov, the second night of a back-to-back, from yesterday's notes still stands.
- **Kawhi Leonard (TOR, Out):** Nothing new since 22 Nov. The last reports have the Raptors ruling him out on Tue 17 Nov for at least one more week, and Shams Charania saying he could return "within the next few weeks" ([RotoWire, 20 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-still-weeks-away-from-returning-540189); [Basketnews, 20 Nov](https://basketnews.com/news-259937-kawhi-leonard-injury-return-gets-huge-latest-timeline-for-raptors.html)). *ESPN est.* 3 Dec. From `form.py`: season 40.0 (2), small sample; Rate 37.2, small sample.

**Our pending trades:**

- **Donovan Mitchell (CLE, we receive):** Nothing new. CLE has not played since 20 Nov, when he had 20 pts (8-17, 2-7 3PT), 3 reb and 3 ast in 29 min in a 128-119 win over IND ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909307)). He is not on ESPN's injury list. CLE plays Mon 23 Nov at CHI ([ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123)). From `form.py`: season 42.4 (16), L7 46.3 (3), L15 43.3 (7), L30 41.5 (15), Rate 44.1, projected 46.5.
- **Derrick White (BOS, we receive):** See *New to the Last 7 days lists* above. He missed 21 Nov (left AC joint sprain), returned 22 Nov, and his three-point slump goes on. Rate 29.1 against a projection of 37.0.
- **Anthony Black (ORL, we send):** On Sun 22 Nov he had 14 pts (5-12, 2-4 3PT), 5 reb, 2 ast, 2 stl and 1 TO in 35 min, 31 FP, in the 116-96 loss at WSH ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031)). From `form.py`: season 37.8 (13), L7 36.5 (4), L15 40.1 (8), L30 37.8 (13, equal to the season), Rate 37.5, projected 28.2. ORL next plays Tue 24 Nov vs DET ([ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/orl/orlando-magic)).
- **Trey Murphy III (NO, we send):** Probable for Mon 23 Nov vs PHX ([NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/trey-murphy-knee-probable-vs-phoenix-on-monday)); *ESPN est.* 23 Nov. See above.
- **Kawhi Leonard (TOR, we send):** Out. Return "within the next few weeks" per Charania ([RotoWire, 20 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-still-weeks-away-from-returning-540189)); *ESPN est.* 3 Dec.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| LaMelo Ball | MIN | #2 | 17 | 28.4 / 32.9 | 0.85 | 34.2 (17) | 24.8 (4) | 33.7 (7) | 33.7 (16) | 46.4 | **−12.2** | 41.1 | Active |
| Josh Giddey | CHI | #3 | 16 | 28.6 / 35.5 | 0.94 | 34.9 (16) | 44.0 (4) | 42.5 (8) | 37.0 (15) | 46.2 | **−11.3** | 46.2 | Active |

- **LaMelo Ball** (minutes): scoring −6.8, reb −1.2, ast −5.1, stocks +0.5, TO −0.4; bonus +0.6.
  - Current: 28.4 min, 17.2 pts, 6.2-15.1 FG, 1.6-2.1 FT, 4.4 reb, 5.8 ast, 1.7 stl, 0.1 blk, 3.5 TO
  - Last 7 days (4 GP): 30.5 min, 12.8 pts, 5.0-15.2 FG, 0.5-1.0 FT, 6.8 reb, 4.2 ast, 1.0 stl, 0.2 blk, 2.5 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Josh Giddey** (minutes): scoring −8.0, reb −2.8, ast −0.7, stocks −3.5, TO +0.8; bonus +2.9.
  - Current: 28.6 min, 10.8 pts, 4.2-9.6 FG, 1.2-1.9 FT, 6.4 reb, 9.2 ast, 0.4 stl, 0.6 blk, 3.4 TO
  - Last 7 days (4 GP): 29.0 min, 11.8 pts, 5.0-10.0 FG, 0.8-1.2 FT, 9.5 reb, 11.5 ast, 0.2 stl, 0.5 blk, 4.2 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −6.9 (#9, efficiency, L7 35.2), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.1 (#7, efficiency, L7 38.0).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −7.5 (#9, efficiency, L7 23.6), Derrick White −7.1 (#6, minutes, L7 26.2), Joel Embiid −6.0 (#3, efficiency, L7 58.3).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Kevin Durant −7.8 (#4, efficiency, L7 33.2), Darius Garland −7.5 (#5, efficiency, L7 38.2), Ivica Zubac −7.0 (#7, minutes, L7 29.5), Jalen Suggs −6.2 (#11, efficiency, L7 25.2).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** De'Aaron Fox −8.7 (#7, efficiency, L7 15.7), Shai Gilgeous-Alexander −8.4 (#1, efficiency, L7 55.0), Damian Lillard −8.2 (#6, efficiency, L7 27.0), Brandon Miller −7.6 (#8, minutes, L7 27.3).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.3 (#1, efficiency, L7 42.8).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −8.2 (#4, efficiency, L7 30.4), Alex Sarr −6.2 (#7, efficiency, L7 30.4), James Harden −6.0 (#5, efficiency, L7 49.3).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball, Josh Giddey |
| efficiency | — |
| both | — |

- **Flagged and not active on ESPN:** none.
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, Active).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** Josh Giddey (Cream Abdul-Yammar, L7 44.0 in 4 vs projected 46.2, season gap −11.3).
- **Not flagged, but 10+ under projection over the last 7 days:** Cade Cunningham (Come-in Cider (us), L7 39.0 in 3 vs projected 50.4, L7 gap −11.4, season gap −1.6), De'Aaron Fox (Matt Wright's Foxies, L7 15.7 in 3 vs projected 38.2, L7 gap −22.5, season gap −8.7), Trae Young (Team Nic Kerr, L7 30.4 in 5 vs projected 44.4, L7 gap −14.0, season gap −8.2), Luka Doncic (Team Nic Kerr, L7 47.8 in 4 vs projected 60.6, L7 gap −12.9, season gap 1.4), Damian Lillard (Matt Wright's Foxies, L7 27.0 in 4 vs projected 38.6, L7 gap −11.6, season gap −8.2), Michael Porter Jr. (Team Nic Kerr, L7 28.0 in 3 vs projected 38.9, L7 gap −10.9, season gap −4.5), Derrick White (Dr White Slong, L7 26.2 in 4 vs projected 37.0, L7 gap −10.8, season gap −7.1), Brandin Podziemski (Matt Wright's Foxies, L7 20.8 in 4 vs projected 30.8, L7 gap −10.1, season gap 0.9), Brandon Miller (Matt Wright's Foxies, L7 27.3 in 3 vs projected 37.4, L7 gap −10.1, season gap −7.6).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 23.0 (1) → — | 42.2 | 44.3 |
| Jalen Suggs | Lauri Birds | 8 | 28.6 / 26.3 | 23.0 | 25.2 (4) | 21.0 (5) | 23.4 (7) | 29.2 | 34.7 |

## Our pending trades

With **Dr White Slong**, proposed by us, expires 25 Nov 04:05 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Donovan Mitchell | we receive | 16 | 32.9 / 33.9 | 42.4 | 46.3 (3) | 43.3 (7) | 41.5 (15) | 46.5 | −4.1 | Active |
| Derrick White | we receive | 16 | 30.0 / 34.3 | 29.9 | 26.2 (4) | 29.6 (7) | 29.6 (15) | 37.0 | −7.1 | Active |
| Anthony Black | we send | 13 | 33.2 / 28.9 | 37.8 | 36.5 (4) | 40.1 (8) | 37.8 (13) | 28.2 | +9.6 | Active |
| Trey Murphy III | we send | 10 | 32.4 / 32.5 | 31.7 | 38.0 (1) | 41.0 (2) | 33.4 (9) | 36.8 | −5.1 | Day-to-day, ESPN est. back 23 Nov |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | 31.0 (1) | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-23 04:12 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research, 23 Nov:** [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032) · [SI / OnSI, 22 Nov](https://www.si.com/nba/bulls/onsi/3-takeaways-after-bulls-waste-josh-giddey-s-22-assist-night-in-ot-loss-to-nuggets-22) · [Chicago Sun-Times, 22 Nov](https://chicago.suntimes.com/bulls/2026/11/22/coach-tiago-splitter-bulls-culture-built-accountability) · [Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329) · [ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122) · [ESPN scoreboard, 23 Nov](https://www.espn.com/nba/scoreboard/_/date/20261123) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910029) · [Detroit Sports Nation via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/j-b-bickerstaff-explains-cade-010500296.html) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910013) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/cade-cunningham-injury-probable-for-sunday-540377) · [ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/det/detroit-pistons) · [ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910028) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910035) · [NBC Sports Boston, 22 Nov](https://www.nbcsportsboston.com/nba/boston-celtics/warriors-live-updates-jayson-tatum/815226/) · [ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909994) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910015) · [NBC Sports Boston, 21 Nov](https://www.nbcsportsboston.com/nba/boston-celtics/celtics-mailbag-mitchell-robinson-derrick-white-jayson-tatum/814956/) · [Heavy, 22 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-joe-mazzulla-delivers-verdict-on-derrick-whites-shooting-struggles/) · [ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/bos/boston-celtics) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910016) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019) · [EssentiallySports via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/brandin-podziemski-sends-message-locker-015921068.html) · [Yardbarker, 20 Nov](https://www.yardbarker.com/nba/articles/insider_provides_major_injury_update_on_stephen_curry_as_warriors_losing_streak_continues/s1_17730_44593775) · [ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/gs/golden-state-warriors) · [RotoWire, 22 Nov](https://www.rotowire.com/basketball/headlines/deaaron-fox-injury-questionable-for-monday-540571) · [ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910031) · [AP via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/wizards-rout-magic-116-96-023006979.html) · [NBC Sports, 22 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-22/trae-young-dishes-out-11-assists-vs-orlando) · [Heavy, 22 Nov](https://heavy.com/sports/nba/los-angeles-lakers/lakers-reveal-shocking-update-austin-reaves/) · [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/brandon-miller-knee-probable-monday-vs-memphis) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034) · [HEAVY via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/detroit-pistons-announce-injury-report-071434249.html) · [NBC Sports, 22 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-22/trey-murphy-knee-probable-vs-phoenix-on-monday) · [RotoWire, 20 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-still-weeks-away-from-returning-540189) · [Basketnews, 20 Nov](https://basketnews.com/news-259937-kawhi-leonard-injury-return-gets-huge-latest-timeline-for-raptors.html) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909307) · [ESPN schedule, read 23 Nov](https://www.espn.com/nba/team/schedule/_/name/orl/orlando-magic)
