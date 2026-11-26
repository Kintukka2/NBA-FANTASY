# Slump Watch: 26 Nov 2026

- Generated 2026-11-26 06:14 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 37. Teams have played **2 to 19 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 37 (Wed 25 Nov US) re-scored from ESPN's final NBA box scores: all 57 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**3 rostered players are 10+ FP/g under projection, on 2 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.6/60.5 · LaMelo Ball 34.4/46.4 · Josh Giddey 34.6/46.2 |
| Melbourne poopoo | 1 | Anthony Davis 50.4/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 53.0/44.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 48.8/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.0/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 43.7/46.5 · Joel Embiid 39.4/45.4 |
| Lauri Birds | 0 | Nikola Jokic 64.6/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.8/56.8 · Cooper Flagg 49.4/45.4 · Evan Mobley 39.9/43.3 |
| Snow Time Lakers | 0 | Jalen Johnson 43.7/50.0 · Jayson Tatum 47.6/48.1 · Kyrie Irving 39.9/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 60.6/60.6 · Domantas Sabonis 45.1/46.7 · Tyrese Maxey 44.7/45.1 |

## Since the last Slump Watch

Compared with [20261125-slump-watch.md](20261125-slump-watch.md). Nine games were played on Wed 25 Nov, and all were final before this run: MIA–PHI, CHI–CHA, CLE–NY, MIN–OKC, LAC–MEM, BKN–MIL, PHX–HOU, SAC–GS and SA–POR ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)). There are no games on Thu 26 Nov (Thanksgiving).

- **Joined the flagged list:** nobody.
- **Left it:** nobody. All three flagged players played on Wednesday and are still flagged:
  - LaMelo Ball, −12.5 → −12.1;
  - Josh Giddey, −11.9 → −11.6;
  - Brandon Ingram, −15.5 → −17.0.
- **Gaps that moved 3+ FP/g:** none, in the flagged, near-the-line or trade tables. The largest moves:
  - Josh Hart (Dr White Slong), −7.5 → −5.5;
  - Jaden McDaniels (trade tables), +11.3 → +13.1;
  - Brandon Ingram, −15.5 → −17.0;
  - Brandon Miller (Matt Wright's Foxies), −7.4 → −5.9;
  - Damian Lillard (Matt Wright's Foxies), −8.2 → −7.2.
- **Drivers:**
  - Ball moved from *both* to *minutes*: his Rate rose from 0.84 to 0.85, the 85% line.
  - Giddey is still under *minutes*, and Ingram under *both*.
  - Among the near-the-line players, Brandon Miller moved from *minutes* to *efficiency*.
- **Flagged and not active on ESPN:** nobody yesterday. Today it is LaMelo Ball (Day-to-day, ESPN est. back 27 Nov).
- **Last 7 days lists:**
  - *Not flagged, but 10+ under over the last 7 days:*
    - Joined: Jaylen Brown (Snow Time Lakers), L7 22.5 in 2 against a projection of 38.6.
    - Left: Brandin Podziemski, whose L7 rose from 19.0 (3) to 23.8 (4), and Ajay Mitchell, from 22.0 (4) to 25.0 (5) (`form.py`).
    - Names still listed:
      - Cade Cunningham, 39.0 (3) → 36.5 (2);
      - Luka Doncic, 41.0 (4) → 38.0 (3);
      - De'Aaron Fox, 15.7 (3) → 18.5 (2);
      - Michael Porter Jr., 18.0 (3) → 21.2 (4);
      - Tyrese Maxey, 28.0 (2) → 34.0 (3).
      - Alex Sarr (25.2 (4)) and Derrick White (25.7 (3)) are unchanged; WSH and BOS did not play.
  - *Flagged, but within 10 over the last 7 days:* Josh Giddey is still the only name. His L7 went from 46.8 (4) to 45.4 (5), against a projection of 46.2.
- **Near the line:** nobody joined or left. The same 19 names are listed.
- **Under 2026, not under projection:**
  - James Harden (Team Nic Kerr) joined, at 35.0 against 45.1 last season. His current average was 35.3 in yesterday's trade tables.
  - Jalen Duren and Trey Murphy III (both us) and Nikola Jokic are still listed. Jokic's L15 went from 64.8 (8) to 63.7 (7).
- **ESPN status** (each injured player's timeline is under *Research*):
  - **In the report:** LaMelo Ball went from Active to Day-to-day (ESPN est. back 27 Nov) after he hurt his left ankle on Wednesday. Kawhi Leonard is unchanged (Out, 03 Dec).
  - **From `injuries.py` (26 Nov), for players outside today's tables:**
    - Jalen Smith (us): day-to-day, and his ESPN est. moved from 25 Nov to 28 Nov.
    - Cade Cunningham (us): Day-To-Day, ESPN est. 27 Nov. Yesterday's notes had him Out.
    - Jaylen Brown: newly day-to-day, ESPN est. 27 Nov.
    - De'Aaron Fox: still day-to-day, with his ESPN est. moved from 25 Nov to 27 Nov.
    - Jalen Duren (Out, 30 Nov) and Anthony Edwards (Out, 21 Dec) are unchanged.
    - Karl-Anthony Towns is off ESPN's injury list (he played on Wednesday). He is in none of our offers now.
- **Our pending trades:** there were 16 offers yesterday and there are 5 today. We proposed all five.
  - **New (2):**
    - Amen Thompson (Matt Wright's Foxies), for Black and Leonard; expires 28 Nov 03:57 UTC.
    - Josh Giddey (Cream Abdul-Yammar), for Black and Leonard; expires 28 Nov 00:37 UTC. Yesterday's offer with the same players, due to expire 27 Nov 01:49 UTC, is no longer listed.
  - **Still open (3), all expiring 27 Nov:**
    - Julius Randle and Derrick White (Dr White Slong), for Buzelis, Black and Leonard; 01:17 UTC, the first to expire.
    - Zion Williamson (Melbourne poopoo), for Black and Leonard; 01:47 UTC.
    - Jaden McDaniels (Melbourne poopoo), for Black and Leonard; 01:52 UTC.
  - **Gone (13):**
    - Eleven reached their expiry, between 25 Nov 11:54 and 26 Nov 03:28 UTC. Two were Cream Abdul-Yammar's offers to us for Paul George. The other nine were ours:
      - Edwards;
      - McDaniels and Castle;
      - Mitchell and White;
      - Alexander-Walker, Randle and White;
      - Diabate and Harden;
      - Giddey and Fears;
      - Towns;
      - Brunson;
      - Ingram and Castle.
    - Two disappeared before their expiry. One was Ball and Fears (Cream Abdul-Yammar) for Murphy, Black and Leonard, due 27 Nov 01:52 UTC. The other was the earlier Giddey offer above. Our roster (`council/roster.csv`) shows no trade, so neither was accepted.
  - **Who appears most:** Anthony Black and Kawhi Leonard are in all five offers, and Matas Buzelis is in one. Trey Murphy III, Jalen Smith, Jalen Duren, Brook Lopez and Paul George are in none.

## Research

**Flagged:**

- **LaMelo Ball (MIN, Cream Abdul-Yammar, day-to-day):** He had 19 pts (7-18, 5-9 3PT), 7 reb, 8 ast, 1 stl and 3 TO in 29 min, 43 FP (`gamelog.py`), in a 113-106 win at OKC on Wed 25 Nov ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320)).
  - In the final 2:30 he landed on Isaiah Hartenstein's foot in a fight for a rebound and twisted his left ankle. He did not return ([AP via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/timberwolves-beat-thunder-113-106-034107047.html)).
  - Chris Finch: "It looked pretty bad, but I'm not sure" ([Dunking With Wolves, 26 Nov](https://dunkingwithwolves.com/the-latest-lamelo-ball-updates-after-timberwolves-star-suffers-ankle-injury)).
  - The Athletic's Jon Krawczynski: "There is no immediate word on his ankle injury, but judging by the mood, he seems to have avoided a major one." No imaging result has been reported ([The Big Lead via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/lamelo-ball-injury-timberwolves-pg-044753065.html)).
  - **Expected return:** no timetable reported; *ESPN est.* 27 Nov. MIN hosts MEM on Fri 27 Nov ([ESPN scoreboard, 27 Nov](https://www.espn.com/nba/scoreboard/_/date/20261127)).
  - From `form.py`: season 34.4 (19), L7 34.2 (4), L15 33.5 (8), L30 33.8 (16), Rate 34.4, projected 46.4.
    - His L7 rose from 29.8 (4): Wednesday's 43 came in, and his 25-FP game of 17 Nov rolled out (`gamelog.py`).
    - His minutes are up (31.5 over L7, 28.5 for the season), which is why his driver is now *minutes*.
- **Josh Giddey (CHI, Cream Abdul-Yammar, in our offers):** He had 12 pts (5-11, 0-4 3PT), 11 reb, 7 ast and 1 TO in 34 min, 40 FP, in a 107-105 win at CHA on Wed 25 Nov ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - He started and closed. Bleacher Nation calls it "a quietly effective night" ([Bleacher Nation, 25 Nov](https://www.bleachernation.com/bulls/2026/11/25/buzelis-bulls-hornets/)).
  - From `form.py`: season 34.6 (18), L7 45.4 (5), L15 38.4 (9), L30 37.0 (15), Rate 40.5, projected 46.2.
    - His L7 is +10.8 over his season. The window holds his 58-FP (18 Nov) and 89-FP (22 Nov) games and Wednesday's 40 (`gamelog.py`).
    - His minutes are steady (29.6 over L7, 28.6 for the season). The rise is rebounds and assists: 9.4 and 11.2 over L7, against 6.4 and 9.2 for the season.
  - Norman Powell (right hamstring strain) missed Wednesday. He was due to be re-evaluated this week ([Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329)); *ESPN est.* 28 Nov. CHI hosts IND on Sat 28 Nov.
- **Brandon Ingram (LAC, Melbourne poopoo):** In his second game back, Wed 25 Nov at MEM, he had 18 pts (6-19, 2-6 3PT, 4-4 FT), 5 reb, 4 ast, 0 stl and 4 TO in 26 min, 20 FP, in a 115-97 loss ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909321)).
  - RotoWire: he "struggled with his shooting touch again," which it expected after he missed the first 15 games. He has played 26.5 min a game in his two games back ([RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-news-leads-team-in-scoring-wednesday-541013)).
  - NBC's recap gives no minutes limit and no date for full minutes ([NBC Sports, 25 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-25/brandon-ingram-scores-18-in-second-game-back)). The "minutes limit" Reuters reported on 24 Nov still has no number.
  - From `form.py`: season, L7, L15 and L30 are all 21.5 (2), small sample; Rate 22.5, small sample; projected 38.5. His gap widened from −15.5 to −17.0 on two games: noise.
  - LAC hosts NO on Fri 27 Nov.

**New to the lists, or off them:**

- **Jaylen Brown (PHI, Snow Time Lakers, new to the Last 7 days list, day-to-day):** He left Wednesday's 111-104 win over MIA late in the second quarter with left hamstring tightness. He had played 17 min, with 6 pts, 1 reb and 1 ast ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909317)).
  - Nick Nurse said imaging would follow and an update would come on Thursday. Dean Wade started the second half.
  - The hamstring first went on 16 Nov. Brown missed two games and returned on 23 Nov ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/jaylen-brown-to-undergo-imaging-after-leaving-game-with-hamstring-tightness.html)).
  - **Expected return:** no timetable reported (an update is due Thu 26 Nov); *ESPN est.* 27 Nov. PHI plays at IND on Fri 27 Nov.
  - From `form.py`: season 38.5 (16) → 40.7 (15), L7 22.5 (2) → 40.0 (1), L15 33.7 (6) → 39.4 (5), L30 39.0 (12) → 42.1 (11), Rate 40.7.
    - `gamelog.py` dropped Wednesday's 5-FP game as a bad game.
    - His L7 then rests on one game, a small sample. The injury exit is the only reason he is on the list.
- **Brandin Podziemski (GS, Matt Wright's Foxies, left the list):** He had 13 pts (5-9, 3-6 3PT), 2 reb, 6 ast and 0 TO in 32 min, 38 FP, in a 129-110 win over SAC on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)).
  - From `form.py`: season 32.1 (16), L7 23.8 (4), L15 25.4 (7), L30 32.0 (15), Rate 27.4, projected 30.8.
  - His L7 is still 8.4 under his season. His minutes are normal (32.8 over L7, 32.4 for the season), so the shortfall is production. No reason was found.
- **Ajay Mitchell (OKC, Lauri Birds, left the list):** He had 25 pts (11-19), 3 reb and 3 ast in 31 min, 37 FP, against MIN on Wednesday. Alex Caruso was back and played 26 min off the bench ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320); [AP via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/timberwolves-beat-thunder-113-106-034107047.html)).
  - From `form.py`: season 31.0 (17), L7 25.0 (5), L15 26.0 (7), L30 31.3 (14), Rate 27.6.
  - His L7 is 6.0 under his season. The reason is his shooting slump ([RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/)); his minutes are up (30.6 over L7, 28.2 for the season).
- **James Harden (CLE, Team Nic Kerr, new to the *Under 2026* table):** He had 28 pts (7-19, 1-8 3PT, 13-14 FT), 1 reb, 5 ast and 4 TO in 36 min, 30 FP, in a 121-102 loss at NY on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909319)).
  - From `form.py`: season 35.0 (18), L7 42.8 (4), L15 43.9 (7), L30 36.4 (16), Rate 40.9, projected 42.1, 2026 45.1.
  - His L7 is +7.8 over his season, from his 80-FP game of 20 Nov and more minutes (37.2 over L7, 33.8 for the season). He is not on ESPN's injury list.

**Updates since 25 Nov:**

- **Luka Doncic (LAL, Team Nic Kerr):** LAL did not play on Wednesday. His L7 fell from 41.0 (4) to 38.0 (3) because his 50-FP game of 17 Nov rolled out. The window holds 34, 42 and 38 FP (`gamelog.py`).
  - His minutes are normal (35.3 over L7, 36.1 for the season), and no reason was found.
  - Austin Reaves (left heel bruise) returned to practice on Wednesday, but it is uncertain whether he plays Fri at SA ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-reaves-redick-reynaud-green.html)). No timetable reported; *ESPN est.* 27 Nov.
  - From `form.py`: season 60.6 (16) → 63.3 (15), L15 45.3 (6), L30 61.8 (13), Rate 49.7.
- **De'Aaron Fox (SA, Matt Wright's Foxies, day-to-day):** The Spurs ruled him out at POR on Wednesday with a right shin contusion. It was his second straight miss ([KSAT, 25 Nov](https://www.ksat.com/sports/2026/11/26/spurs-list-deaaron-fox-out-against-trail-blazers-victor-wembanyama-returns-after-injury/); [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909325)).
  - **Expected return:** no timetable reported; *ESPN est.* 27 Nov. SA hosts LAL on Fri 27 Nov.
  - From `form.py`: season 29.5 (16), L7 18.5 (2), small sample, L15 21.2 (5), L30 26.1 (13), Rate 23.5.
    - His L7 is 11.0 under his season. The reasons are the shin and his 17- and 20-FP games before it; his minutes are normal (29.0 for both).
    - His L7 rose from 15.7 (3) because his 10-FP game of 17 Nov rolled out.
- **Michael Porter Jr. (BKN, Team Nic Kerr):** He had 12 pts (4-14, 2-6 3PT), 11 reb and 4 ast in 34 min, 31 FP, in a 104-97 win at MIL on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322)).
  - From `form.py`: season 32.9 (16), L7 21.2 (4), L15 28.3 (6), L30 31.8 (13), Rate 28.1.
  - His L7 is 11.7 under his season. The reason is production (4-14 again), not minutes (31.5 over L7, 32.8 for the season).
  - His comment that "It's really hard for me right now" still stands ([Hoops Rumors, citing the New York Post, 24 Nov](https://www.hoopsrumors.com/2026/11/eastern-notes-michael-porter-jr-vukcevic-joe-black-kevin-porter-jr.html)).
- **Tyrese Maxey (PHI, Team Nic Kerr):** He had 30 pts (12-21, 3-5 3PT), 4 reb, 6 ast and 5 TO in 37 min, 46 FP, against MIA on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909317)).
  - From `form.py`: season 44.7 (18), L7 34.0 (3), L15 41.1 (7), L30 42.9 (14), Rate 40.4.
  - His L7 is 10.7 under his season, from games of 27 FP (21 Nov) and 29 FP (23 Nov). His minutes are normal (36.0 over L7, 36.1 for the season), and no reason was found.
- **Alex Sarr (WSH, Team Nic Kerr) and Derrick White (BOS, Dr White Slong, in our offers):** Neither team played on Wednesday ([ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125)), and yesterday's notes stand.
  - Sarr's minutes are down, and White is in a shooting slump.
  - Sarr, from `form.py`: season 29.6 (18), L7 25.2 (4), L15 30.2 (8), L30 30.2 (15), Rate 29.1.
  - White, from `form.py`: season 29.5 (17), L7 25.7 (3), L15 27.1 (7), L30 29.0 (15), Rate 28.1.
- **Near-the-line movers:**
  - **Josh Hart (NY):** 15 pts, 7 reb, 11 ast and 3 stl in 36 min, 56 FP, against CLE ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909319)).
    - From `form.py`: season 27.5 (15), L7 35.5 (4), L15 24.9 (8), L30 25.4 (12), Rate 29.5.
    - His L7 is +8.0 over his season. He scored 47 and 56 FP in his last two games and played more (34.5 min over L7, 31.1 for the season).
  - **Brandon Miller (CHA):** 35 pts (13-25), 3 reb, 1 ast and 3 stl in 34 min, 52 FP, against CHI ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
    - From `form.py`: season 31.5 (15), L7 39.3 (3), L15 33.4 (5), L30 34.1 (12), Rate 35.4.
    - His L7 is +7.9 over his season, on more minutes (34.0 over L7, 31.2 for the season).
  - **Damian Lillard (POR):** 29 pts and 7 ast in 34 min, 49 FP ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909325)).
    - From `form.py`: season 31.4 (18), L7 34.8 (4), L15 32.3 (9), L30 30.3 (16).

**Our players in the report:**

- **Cade Cunningham (DET, day-to-day):** DET did not play on Wednesday.
  - Hoops Rumors calls Tuesday his second miss with right knee soreness. Bickerstaff indicated he is operating at far less than 100 percent. No status for Friday has been given ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)).
  - **Expected return:** no timetable reported; *ESPN est.* 27 Nov. DET hosts MIL on Fri 27 Nov.
  - From `form.py`: season 48.8 (15), L7 36.5 (2), small sample, L15 54.6 (5), L30 49.8 (12), Rate 46.7, projected 50.4.
    - His L7 is 12.3 under his season. One reason is the knee. The other is that his 44-FP game of 17 Nov rolled out, leaving 42 and 31 FP (`gamelog.py`).
    - His minutes are normal when he plays (34.5 over L7, 34.9 for the season).
- **Jalen Duren (DET, Out):** He practiced with the Motor City Cruise on Wednesday, and Hoops Rumors says he seems close to returning. No date has been given.
  - Bickerstaff: "We're really excited" (via the Detroit Free Press's Omari Sankofa II) ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)).
  - **Expected return:** no timetable reported; *ESPN est.* 30 Nov.
  - `council/news_overrides.csv` has no Duren row now; the 1 Dec floor was removed in the 25 Nov run. The matchup therefore uses ESPN's 30 Nov. DET plays Fri 27 (MIL), Sun 29 (ORL) and Mon 30 Nov (DEN) ([ESPN scoreboard, 29 Nov](https://www.espn.com/nba/scoreboard/_/date/20261129)).
  - From `form.py`: season 33.5 (2) → 44.0 (1), small sample; Rate 44.1, small sample. He has no game in his L7, L15 or L30.
- **Matas Buzelis (CHI, in one offer):** He had 24 pts (8-15, 0-5 3PT, 8-9 FT), 5 reb, 0 ast and 0 TO in 34 min, 31 FP, at CHA on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - He started and closed, his fourth 20-point game in his last six ([Bleacher Nation, 25 Nov](https://www.bleachernation.com/bulls/2026/11/25/buzelis-bulls-hornets/)). His gap narrowed from −6.8 to −6.5.
  - From `form.py`: season 26.0 (18), L7 32.6 (5), L15 30.3 (9), L30 27.0 (15), Rate 30.0, projected 32.5.
  - His L7 is +6.6 over his season, from more minutes (30.8 over L7, 28.2 for the season) and his 54-FP (18 Nov) and 39-FP (22 Nov) games.
- **Kawhi Leonard (TOR, Out, in all five offers):** I found nothing new since the 24 Nov update. He has begun individual on-court workouts and will be re-evaluated in one week, around 1 Dec ([RotoWire, citing ESPN's Marc J. Spears, 24 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-to-be-re-evaluated-in-one-week-540857); [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/raptors-rule-out-kawhi-leonard-another-week.html)).
  - **Expected return:** re-evaluation in one week; *ESPN est.* 3 Dec.
  - From `form.py`: season 40.0 (2), small sample; Rate 43.3, small sample. He has no game in his L7, L15 or L30.
- **Trey Murphy III (NO):** NO did not play on Wednesday, and I found no news dated after 23 Nov. NO plays at LAC on Fri 27 Nov.
  - The rest risk on the second night of the Sun 29–Mon 30 Nov back-to-back stands. He sat the second night of the 20–21 Nov back-to-back ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns)).
  - From `form.py`: season 31.1 (11), L7 31.5 (2), small sample, L15 31.5 (2), small sample, L30 32.2 (8), Rate 32.3, projected 36.8.
- **Anthony Black (ORL, in all five offers):** ORL did not play on Wednesday.
  - Orlando signed free agent Kevin Porter Jr. to a two-year minimum deal; it became official at 10:08 pm ET on 25 Nov ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/magic-to-sign-kevin-porter-jr.html)).
  - NBC's Kurt Helin: "While the Magic play Jalen Suggs and Anthony Black for most of the guard minutes," Orlando wants "some scoring off the bench, and Porter can give them that" ([NBC Sports, 25 Nov](https://www.nbcsports.com/nba/news/kevin-porter-jr-reportedly-to-sign-two-year-deal-with-orlando-magic)). No debut date or minutes have been reported; details are in the trade watch.
  - ESPN's Bobby Marks says Black is set to become a restricted free agent next summer, and Brian Windhorst says teams are watching him. That is talk, not a deal ([BasketballNews, 25 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-nba-trade-rumor-espn-insider-pinpoints-anthony-blacks-contract-situation-after-orlando-magic-meet-with-twenty-six-year-old-free-agent/)).
  - From `form.py`: season 35.3 (14), L7 25.5 (4), L15 32.9 (8), L30 34.6 (13), Rate 30.9, projected 28.2.
    - His L7 is 9.8 under his season. The cause is the 3-FP game of 24 Nov (2-8, 5 TO), not minutes (34.2 over L7, 32.9 for the season).
    - His L30 moved from 35.3 (14) to 34.6 (13) as a game rolled out of the 30-day window.
  - ORL plays at WSH on Sat 28 Nov and at DET on Sun 29 Nov ([ESPN scoreboard, 28 Nov](https://www.espn.com/nba/scoreboard/_/date/20261128)).
- **Jalen Smith (CHI, us, not in today's tables, day-to-day):** He missed Wednesday at CHA; Bleacher Nation calls him the "under-the-weather starting center" ([Bleacher Nation, 25 Nov](https://www.bleachernation.com/bulls/2026/11/25/buzelis-bulls-hornets/)).
  - **Expected return:** no timetable reported; *ESPN est.* 28 Nov. CHI hosts IND on Sat 28 Nov.
  - From `form.py`: season 37.4 (15) → 39.4 (14), L7 42.0 (3), L15 46.2 (6), L30 38.4 (12) → 41.0 (11), Rate 41.5.

**Our pending trades (players we would receive):**

- **Amen Thompson (HOU, Matt Wright's Foxies, new offer):** He had 18 pts (7-14), 10 reb, 4 ast, 2 blk and 1 TO in 36 min, 44 FP, in a 116-104 win over PHX on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909323)).
  - He is not on ESPN's injury list.
  - From `form.py`: season 37.5 (18), L7 39.0 (4), L15 42.4 (7), L30 35.2 (15), Rate 39.3, projected 40.0.
- **Jaden McDaniels (MIN, Melbourne poopoo):** He had 32 pts (11-15, 4-5 3PT, 6-6 FT), 10 reb, 5 ast and 0 TO in 37 min, 76 FP, at OKC on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320); [AP via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/timberwolves-beat-thunder-113-106-034107047.html)). His gap rose from +11.3 to +13.1.
  - From `form.py`: season 42.8 (19), L7 58.8 (4), L15 51.4 (8), L30 43.8 (16), Rate 49.9, projected 29.7.
  - His L7 is +15.9 over his season. He scored 77 and 76 FP in his last two games and is playing more (36.5 min over L7, 34.2 for the season).
  - Anthony Edwards is out: "into January," per The Athletic's Jon Krawczynski ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-rumors-insider-anthony-edwards-injury-return-prediction-looking-like-2027)); *ESPN est.* 21 Dec. Ball's ankle is now a question too.
- **Julius Randle (BKN, Dr White Slong):** He had 28 pts (10-16), 9 reb, 3 ast and 4 TO in 39 min, 41 FP, at MIL on Wednesday ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322)).
  - From `form.py`: season 36.5 (17), L7 40.5 (4), L15 41.0 (7), L30 36.1 (14), Rate 39.2.
- **Zion Williamson (NO, Melbourne poopoo):** NO did not play on Wednesday, and his figures are unchanged.
  - From `form.py`: season 40.7 (17), L7 35.0 (3), L15 38.4 (7), L30 41.1 (14), Rate 38.1.
  - His L7 is 5.7 under his season. The cause is his six-turnover, no-assist game on 23 Nov ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)), not minutes (36.3 over L7, 32.9 for the season).
- **Josh Giddey and Derrick White:** see above.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| LaMelo Ball | MIN | #2 | 19 | 28.5 / 32.9 | 0.85 | 34.4 (19) | 34.2 (4) | 33.5 (8) | 33.8 (16) | 46.4 | **−12.1** | 41.1 | Day-to-day, ESPN est. back 27 Nov |
| Josh Giddey | CHI | #3 | 18 | 28.6 / 35.5 | 0.93 | 34.6 (18) | 45.4 (5) | 38.4 (9) | 37.0 (15) | 46.2 | **−11.6** | 46.2 | Active |

- **LaMelo Ball** (minutes): scoring −6.7, reb −1.2, ast −5.1, stocks +0.4, TO −0.0; bonus +0.7.
  - Current: 28.5 min, 17.3 pts, 6.2-15.3 FG, 1.6-2.1 FT, 4.4 reb, 5.7 ast, 1.6 stl, 0.2 blk, 3.3 TO
  - Last 7 days (4 GP): 31.5 min, 15.8 pts, 6.0-16.2 FG, 1.0-1.2 FT, 5.5 reb, 6.5 ast, 0.8 stl, 0.5 blk, 2.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Josh Giddey** (minutes): scoring −8.7, reb −2.8, ast −0.8, stocks −3.5, TO +1.1; bonus +3.0.
  - Current: 28.6 min, 10.4 pts, 4.1-9.7 FG, 1.2-1.8 FT, 6.4 reb, 9.2 ast, 0.4 stl, 0.6 blk, 3.2 TO
  - Last 7 days (5 GP): 29.6 min, 11.8 pts, 5.2-11.4 FG, 0.8-1.0 FT, 9.4 reb, 11.2 ast, 0.4 stl, 0.4 blk, 3.0 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO

### Melbourne poopoo: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Brandon Ingram | LAC | #7 | 2 | 26.5 / 35.3 | 0.74 | 21.5 (2) | 21.5 (2) | 21.5 (2) | 21.5 (2) | 38.5 | **−17.0** | 36.5 | Active |

- **Brandon Ingram** (both): scoring −11.7, reb +0.3, ast −1.6, stocks −6.0, TO +0.6; bonus +1.5.
  - Current: 26.5 min, 17.0 pts, 6.0-18.5 FG, 4.0-4.5 FT, 6.0 reb, 4.0 ast, 0.0 stl, 0.0 blk, 2.5 TO
  - Projected: 35.3 min, 22.6 pts, 8.5-17.6 FG, 3.9-4.8 FT, 5.7 reb, 4.8 ast, 0.8 stl, 0.7 blk, 2.8 TO

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −6.5 (#9, efficiency, L7 32.6), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.7 (#7, efficiency, L7 31.5).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Derrick White −7.5 (#6, minutes, L7 25.7), Joel Embiid −6.0 (#3, efficiency, L7 59.5), Josh Hart −5.5 (#9, efficiency, L7 35.5).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Darius Garland −7.5 (#5, efficiency, L7 34.0), Kevin Durant −6.5 (#4, efficiency, L7 38.2), Ivica Zubac −6.2 (#7, minutes, L7 35.2).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** De'Aaron Fox −8.7 (#7, efficiency, L7 18.5), Shai Gilgeous-Alexander −8.0 (#1, efficiency, L7 53.8), Damian Lillard −7.2 (#6, efficiency, L7 34.8), Brandon Miller −5.9 (#8, efficiency, L7 39.3).

### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −6.3 (#1, efficiency, L7 48.7).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −7.5 (#4, efficiency, L7 36.0), James Harden −7.1 (#5, efficiency, L7 42.8), Alex Sarr −7.1 (#7, efficiency, L7 25.2), Michael Porter Jr. −6.0 (#6, efficiency, L7 21.2).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball, Josh Giddey |
| efficiency | — |
| both | Brandon Ingram |

- **Flagged and not active on ESPN:** LaMelo Ball (Day-to-day, ESPN est. back 27 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** Josh Giddey (Cream Abdul-Yammar, L7 45.4 in 5 vs projected 46.2, season gap −11.6).
- **Not flagged, but 10+ under projection over the last 7 days:** Cade Cunningham (Come-in Cider (us), L7 36.5 in 2 vs projected 50.4, L7 gap −13.9, season gap −1.6), Luka Doncic (Team Nic Kerr, L7 38.0 in 3 vs projected 60.6, L7 gap −22.6, season gap −0.1), De'Aaron Fox (Matt Wright's Foxies, L7 18.5 in 2 vs projected 38.2, L7 gap −19.7, season gap −8.7), Michael Porter Jr. (Team Nic Kerr, L7 21.2 in 4 vs projected 38.9, L7 gap −17.7, season gap −6.0), Jaylen Brown (Snow Time Lakers, L7 22.5 in 2 vs projected 38.6, L7 gap −16.1, season gap −0.1), Alex Sarr (Team Nic Kerr, L7 25.2 in 4 vs projected 36.6, L7 gap −11.4, season gap −7.1), Derrick White (Dr White Slong, L7 25.7 in 3 vs projected 37.0, L7 gap −11.3, season gap −7.5), Tyrese Maxey (Team Nic Kerr, L7 34.0 in 3 vs projected 45.1, L7 gap −11.1, season gap −0.5).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | — | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 11 | 32.6 / 32.5 | 31.1 | 31.5 (2) | 31.5 (2) | 32.2 (8) | 36.8 | 41.6 |
| Nikola Jokic | Lauri Birds | 16 | 36.9 / 35.6 | 64.6 | 62.2 (4) | 63.7 (7) | 65.2 (14) | 67.2 | 74.9 |
| James Harden | Team Nic Kerr | 18 | 33.8 / 33.6 | 35.0 | 42.8 (4) | 43.9 (7) | 36.4 (16) | 42.1 | 45.1 |

## Our pending trades

With **Cream Abdul-Yammar**, proposed by us, expires 28 Nov 00:37 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | we receive | 18 | 28.6 / 35.5 | 34.6 | 45.4 (5) | 38.4 (9) | 37.0 (15) | 46.2 | −11.6 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 34.6 (13) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Matt Wright's Foxies**, proposed by us, expires 28 Nov 03:57 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Amen Thompson | we receive | 18 | 32.6 / 36.5 | 37.5 | 39.0 (4) | 42.4 (7) | 35.2 (15) | 40.0 | −2.5 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 34.6 (13) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 27 Nov 01:47 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Zion Williamson | we receive | 17 | 32.9 / 30.9 | 40.7 | 35.0 (3) | 38.4 (7) | 41.1 (14) | 40.0 | +0.7 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 34.6 (13) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Melbourne poopoo**, proposed by us, expires 27 Nov 01:52 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jaden McDaniels | we receive | 19 | 34.2 / 31.7 | 42.8 | 58.8 (4) | 51.4 (8) | 43.8 (16) | 29.7 | +13.1 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 34.6 (13) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

With **Dr White Slong**, proposed by us, expires 27 Nov 01:17 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Julius Randle | we receive | 17 | 33.4 / 34.3 | 36.5 | 40.5 (4) | 41.0 (7) | 36.1 (14) | 37.0 | −0.6 | Active |
| Derrick White | we receive | 17 | 30.0 / 34.3 | 29.5 | 25.7 (3) | 27.1 (7) | 29.0 (15) | 37.0 | −7.5 | Active |
| Matas Buzelis | we send | 18 | 28.2 / 30.5 | 26.0 | 32.6 (5) | 30.3 (9) | 27.0 (15) | 32.5 | −6.5 | Active |
| Anthony Black | we send | 14 | 32.9 / 28.9 | 35.3 | 25.5 (4) | 32.9 (8) | 34.6 (13) | 28.2 | +7.1 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | — | 45.8 | −5.8 | **Out**, ESPN est. back 03 Dec |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-26 06:14 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research links:** [ESPN scoreboard, 25 Nov](https://www.espn.com/nba/scoreboard/_/date/20261125) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320) · [AP via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/timberwolves-beat-thunder-113-106-034107047.html) · [Dunking With Wolves, 26 Nov](https://dunkingwithwolves.com/the-latest-lamelo-ball-updates-after-timberwolves-star-suffers-ankle-injury) · [The Big Lead via Yahoo Sports, 26 Nov](https://sports.yahoo.com/nba/articles/lamelo-ball-injury-timberwolves-pg-044753065.html) · [ESPN scoreboard, 27 Nov](https://www.espn.com/nba/scoreboard/_/date/20261127) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318) · [Bleacher Nation, 25 Nov](https://www.bleachernation.com/bulls/2026/11/25/buzelis-bulls-hornets/) · [Hoops Rumors via Yardbarker, 22 Nov](https://www.yardbarker.com/nba/articles/bulls_norman_powell_suffers_mild_right_hamstring_strain/s1_14822_44601329) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909321) · [RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-news-leads-team-in-scoring-wednesday-541013) · [NBC Sports, 25 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-25/brandon-ingram-scores-18-in-second-game-back) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909317) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/jaylen-brown-to-undergo-imaging-after-leaving-game-with-hamstring-tightness.html) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324) · [RotoWire via CBS Sports, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-ajay-mitchell-offensive-struggles-continue/) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909319) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pacific-notes-reaves-redick-reynaud-green.html) · [KSAT, 25 Nov](https://www.ksat.com/sports/2026/11/26/spurs-list-deaaron-fox-out-against-trail-blazers-victor-wembanyama-returns-after-injury/) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909325) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322) · [Hoops Rumors, citing the New York Post, 24 Nov](https://www.hoopsrumors.com/2026/11/eastern-notes-michael-porter-jr-vukcevic-joe-black-kevin-porter-jr.html) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html) · [ESPN scoreboard, 29 Nov](https://www.espn.com/nba/scoreboard/_/date/20261129) · [RotoWire, citing ESPN's Marc J. Spears, 24 Nov](https://rotowire.com/basketball/headlines/kawhi-leonard-injury-to-be-re-evaluated-in-one-week-540857) · [Hoops Rumors, 24 Nov](https://www.hoopsrumors.com/2026/11/raptors-rule-out-kawhi-leonard-another-week.html) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/trey-murphy-knee-good-to-go-monday-vs-suns) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/magic-to-sign-kevin-porter-jr.html) · [NBC Sports, 25 Nov](https://www.nbcsports.com/nba/news/kevin-porter-jr-reportedly-to-sign-two-year-deal-with-orlando-magic) · [BasketballNews, 25 Nov](https://www.basketballnews.com/news/basketballnews-nba-active-news-nba-trade-rumor-espn-insider-pinpoints-anthony-blacks-contract-situation-after-orlando-magic-meet-with-twenty-six-year-old-free-agent/) · [ESPN scoreboard, 28 Nov](https://www.espn.com/nba/scoreboard/_/date/20261128) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909323) · [ClutchPoints, 24 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-rumors-insider-anthony-edwards-injury-return-prediction-looking-like-2027) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)
