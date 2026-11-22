# Slump Watch: 22 Nov 2026

- Generated 2026-11-22 07:27 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 33. Teams have played **2 to 18 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 33 (Sat 21 Nov US) re-scored from ESPN's final NBA box scores: all 34 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**2 rostered players are 10+ FP/g under projection, on 1 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.2/60.5 · LaMelo Ball 34.2/46.4 · Josh Giddey 31.3/46.2 |
| Come-in Cider (us) | 0 | Cade Cunningham 50.1/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 47.5/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 42.4/46.5 · Joel Embiid 39.4/45.4 |
| Lauri Birds | 0 | Nikola Jokic 64.1/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.4/56.8 · Cooper Flagg 50.1/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 49.7/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 51.1/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 44.9/50.0 · Jayson Tatum 45.9/48.1 · Kyrie Irving 41.0/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 62.1/60.6 · Domantas Sabonis 43.3/46.7 · Tyrese Maxey 45.6/45.1 |

## Since the last Slump Watch

Against [20261121-slump-watch.md](20261121-slump-watch.md):
- **Joined the flagged list:** nobody.
- **Left it:** nobody. Josh Giddey and LaMelo Ball are still flagged.
- **Gaps that moved 3+ FP/g:** none.
- **New to the Last 7 days lists:** Damian Lillard. Tyler Herro, Brandin Podziemski, Kevin Durant and Brandon Miller left them.
- **Our pending trade** with Melbourne poopoo (Castle for Black) is no longer listed.

## Research

**Flagged:**

- **Josh Giddey (CHI):** Nothing new from a game since 21 Nov. CHI had no game on Saturday and hosts DEN on Sun 22 Nov ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121); [ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122)). Tiago Splitter has now explained why he benched Giddey and Matas Buzelis for the close of the 20 Nov loss to WSH: "I thought they didn't have a good game." Tre Jones, Norman Powell, Isaac Okoro, Buddy Hield and Nic Claxton closed that game ([Chicago Bulls On SI via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/3-bulls-takeaways-giddey-buzelis-043005109.html)). His L7 is now 28.5 (4), so he has left the "flagged, but within 10 over the last 7 days" list.
- **LaMelo Ball (MIN):** On Sat 21 Nov he had 12 pts (5-10 FG, 1-4 3PT), 5 reb, 7 ast, 1 stl, 1 blk and 3 TO in 32 min in a 104-95 win over MEM ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910026)). He came in 13-for-50 from three over his previous five games. This time he "did not try to shoot himself out of it". Chris Finch praised him for "not, like, chasing shots tonight" and "running the offense too", and said he was "over the moon" with Ball's defense. Minnesota outscored MEM by 12 in his minutes. With Anthony Edwards "out for at least another month" (*ESPN est.* 21 Dec), Ball is the primary offensive option ([SI / OnSI, 22 Nov](https://www.si.com/nba/timberwolves/onsi/three-lamelo-ball-questions-timberwolves-win-grizzlies-01m80pwxp43s)). Rotoworld called it his second full stat line of the season and noted that MIN plays four games next week, starting Mon 23 Nov vs BKN ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/lamelo-ball-dishes-out-seven-assists-vs-memphis)). His L7 of 29.0 (5) is 5.2 under his season average of 34.2. The reason is his shooting; his minutes held up (30.4 over L7 against 28.4 for the season, per `form.py`).

**New to the Last 7 days lists:**

- **Damian Lillard (POR, not MIL):** His minutes are normal (L7 30.8 against 29.8 for the season). The drop comes from two bad shooting nights and thin peripheral stats:
  - 16 Nov at MIN: 9 pts on 2-15 FG in 24 min ([ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909999)), "easily Lillard's worst performance of the season" ([Rip City Project, 17 Nov](https://ripcityproject.com/trail-blazers-finally-built-survive-occasional-damian-lillard-slump)).
  - 17 Nov at MIN: 25 pts (8-19, 5-11 3PT) in 31 min ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910003)).
  - 19 Nov at MIL: 33 pts (10-18) in 35 min ([ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910020)).
  - 21 Nov at NY: 15 pts (5-16, 1-9 3PT), 3 reb and 3 ast in 33 min in a 97-96 loss ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910024)). He missed his first eight threes before hitting the tying three with 1:04 left.

  Rotoworld has him at 40.9% from the field over the last three weeks and says "things could be much better for those rostering him" ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/damian-lillard-goes-cold-from-three-scores-15)). SI calls his 40.9% the lowest of his career outside 2021-22. It puts him at 35.8% from three and notes that he missed all of last season rehabbing a torn Achilles and plays in "an offense he's not the focus of" ([SI / OnSI, 22 Nov](https://www.si.com/nba/trailblazers/onsi/3-missteps-in-blazers-loss-vs-jalen-brunson-and-the-knicks)). Deni Avdija runs Portland's offense as a point-forward, and Lillard is "the cherry on top" ([Rip City Project, 17 Nov](https://ripcityproject.com/trail-blazers-finally-built-survive-occasional-damian-lillard-slump)). No injury was reported. From `form.py`: season 30.4 (16), L7 27.0 (4), L15 28.8 (9), L30 29.0 (15), Rate 26.5, projected 38.6. Most of his gap to projection is season-long. His L7 is only 3.4 under his season average.

**Updates since 21 Nov:**

- **De'Aaron Fox (SA):** On Sat 21 Nov he had 5 pts (1-4 FG, 0-3 3PT, 3-3 FT), 10 ast, 2 reb and 3 TO in 26 min. The 114-91 win over NO was a blowout, and he was +33 ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910027)). He has taken only nine shots in the two games since Dylan Harper's injury (Harper: 2–3 weeks reported, [ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html); *ESPN est.* 13 Dec). Asked whether he needs to look for his own shot more, Fox said: "I definitely don't look at it that way." The Express-News writes that the Spurs "need Fox to remain aggressive" with Harper out ([San Antonio Express-News via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/3-takeaways-wembanyamas-50-point-063130094.html)). No new injury was reported. His L7 of 15.7 (3) is 13.8 under his season average of 29.5. The causes are low shot volume and the short minutes of a blowout.
- **Trae Young (WSH):** Nothing new since 21 Nov. WSH had no game on Saturday and hosts ORL on Sun 22 Nov ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121); [ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122)).
- **Josh Hart (NY):** He started and was scoreless again on Sat 21 Nov: 0 pts (0-7 FG, 0-4 3PT), 8 reb, 6 ast, 2 stl and 1 TO in 35 min in the 97-96 win over POR ([ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910024)). He came in averaging 5.0 pts in November, and his last assist set up Mikal Bridges' buzzer-beater ([NY Daily News via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/mikal-bridges-buzzer-beater-lifts-035800035.html)). His minutes rose because Karl-Anthony Towns (illness) and OG Anunoby (left calf tightness) sat for the first time this season. Andre Drummond and Landry Shamet started in their place (same source). Towns and Anunoby: no timetable reported; *ESPN est.* 22 Nov for both, day-to-day. NY hosts IND on Sun 22 Nov, the second night of a back-to-back ([ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122)). His L7 of 17.8 (4) is 6.1 under his season average of 23.8. The reason is his shooting; his minutes are normal (30.0 over L7).
- **Luka Doncic (LAL):** LAL had no game on Saturday ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121)). Not in yesterday's notes: Keegan Murray accidentally poked him in the right eye with 2:19 left on 20 Nov. He stayed in and said "I'm good … It's just a head, you know, but I'll be fine". The eye will be monitored before Mon 23 Nov vs UTA ([Basketnews, 21 Nov](https://basketnews.com/news-259955-luka-doncic-shares-critical-lakers-update-on-alarming-eye-injury.html)). He is not on ESPN's injury list, and no absence has been reported.
- **Michael Porter Jr. (BKN):** Nothing new since 21 Nov. BKN had no game on Saturday and next plays Mon 23 Nov at MIN ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121); [ESPN schedule, read 22 Nov](https://www.espn.com/nba/team/schedule/_/name/bkn/brooklyn-nets)).
- **Brandon Miller (CHA):** Nothing new since 21 Nov. CHA had no game on Saturday and next plays Mon 23 Nov vs MEM ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121)). Rotoworld describes his brief first-quarter exit at ATL on 20 Nov as a knee hyperextension, where Basketnews reported a rolled ankle. He returned to start the second quarter, and Rotoworld saw "no reason to think his status for their next game on Monday will be in question" ([NBC Sports, 20 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-20/brandon-miller-scores-19-points-with-five-triples)). No timetable reported, and none appears needed. He is not on ESPN's injury list, so there is no ESPN est.

**Our near-the-line players:**

- **Trey Murphy III (NO):** His 0 FP on Sat 21 Nov was a planned rest, not a new injury. The Pelicans held him out of the second night of a back-to-back at SA to manage patellar tendinopathy in both knees ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-wont-play-saturday-540349); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio)). The night before, he had returned from a six-game absence with 17 pts (5-10, 3-8 3PT), 4 reb, 2 stl and 1 blk in 29 min at OKC ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310)). RotoWire gives his next game as Mon 23 Nov vs PHX. No timetable beyond that has been reported; *ESPN est.* 23 Nov (ESPN lists him Out, knee). NO's next back-to-back is Sun 29 Nov at POR and Mon 30 Nov at SAC ([ESPN schedule, read 22 Nov](https://www.espn.com/nba/team/schedule/_/name/no/new-orleans-pelicans)). Our inference: he may sit 30 Nov the same way. From `form.py`: season 31.7 (10), L7 38.0 (1, small sample, so noise), L15 38.3 (3), L30 33.4 (9), Rate 36.6, projected 36.8. His L7 is 6.3 over his season average only because the one 20 Nov game is the whole sample.
- **Matas Buzelis (CHI):** Nothing new since 21 Nov. CHI had no game on Saturday ([ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121)). Splitter's reason for the 20 Nov late benching was "I thought they didn't have a good game" ([Chicago Bulls On SI via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/3-bulls-takeaways-giddey-buzelis-043005109.html)). CHI hosts DEN on Sun 22 Nov. Norman Powell is questionable with a right hamstring strain (no timetable reported; *ESPN est.* 22 Nov, day-to-day). If Powell sits, RotoWire expects Buddy Hield and Tre Jones, not Buzelis, to get the extra minutes ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-questionable-to-play-sunday-540393)). From `form.py`: season 24.8 (15), L7 33.5 (4), L15 30.6 (7), L30 25.2 (14), Rate 29.8, projected 32.5. His L7 is 8.7 over his season average because of his shooting in two big games: 23 pts (8-14) at CLE on 16 Nov ([ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909995)) and 25 pts (9-16) at BKN on 18 Nov ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910011)).
- **Kawhi Leonard (TOR, Out):** Shams Charania reported on 20 Nov that the Raptors are optimistic he will return "in the next few weeks". TSN reports the knee issue as left patellar tendinopathy ([Basketnews, 20 Nov](https://basketnews.com/news-259937-kawhi-leonard-injury-return-gets-huge-latest-timeline-for-raptors.html)). *ESPN est.* 3 Dec.
- **Jalen Duren (DET, Out):** Right hamstring strain. On 8 Nov the Pistons said he would miss at least two more weeks ([Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)). As of the 20 Nov injury report he "is set to be re-evaluated next week" ([HEAVY via Yahoo Sports, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html)). No return date has been reported. *ESPN est.* 24 Nov.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 15 | 27.8 / 35.5 | 0.86 | 31.3 (15) | 28.5 (4) | 35.9 (7) | 33.3 (14) | 46.2 | **−14.9** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 17 | 28.4 / 32.9 | 0.85 | 34.2 (17) | 29.0 (5) | 34.0 (8) | 33.7 (16) | 46.4 | **−12.2** | 41.1 | Active |

- **Josh Giddey** (minutes): scoring −9.2, reb −3.3, ast −2.4, stocks −3.5, TO +1.1; bonus +2.5.
  - Current: 27.8 min, 9.9 pts, 3.8-9.1 FG, 1.2-1.9 FT, 5.9 reb, 8.4 ast, 0.4 stl, 0.5 blk, 3.3 TO
  - Last 7 days (4 GP): 25.2 min, 8.0 pts, 3.2-8.2 FG, 0.5-0.8 FT, 8.0 reb, 7.2 ast, 0.2 stl, 0.5 blk, 3.2 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
- **LaMelo Ball** (minutes): scoring −6.8, reb −1.2, ast −5.1, stocks +0.5, TO −0.4; bonus +0.6.
  - Current: 28.4 min, 17.2 pts, 6.2-15.1 FG, 1.6-2.1 FT, 4.4 reb, 5.8 ast, 1.7 stl, 0.1 blk, 3.5 TO
  - Last 7 days (5 GP): 30.4 min, 14.0 pts, 5.4-17.2 FG, 0.6-1.2 FT, 7.0 reb, 4.6 ast, 1.6 stl, 0.2 blk, 2.2 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −7.7 (#9, minutes, L7 33.5), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.1 (#7, efficiency, L7 38.0).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −9.2 (#9, efficiency, L7 17.8), Derrick White −6.6 (#6, minutes, L7 27.3), Joel Embiid −6.0 (#3, efficiency, L7 58.3).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Kevin Durant −7.8 (#4, efficiency, L7 33.2), Darius Garland −7.5 (#5, efficiency, L7 38.2), Ivica Zubac −7.0 (#7, minutes, L7 29.7).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** De'Aaron Fox −8.7 (#7, efficiency, L7 15.7), Shai Gilgeous-Alexander −8.4 (#1, efficiency, L7 55.0), Damian Lillard −8.2 (#6, efficiency, L7 27.0), Brandon Miller −7.6 (#8, minutes, L7 27.3), Norman Powell −5.9 (#9, minutes, L7 33.2).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −5.1 (#1, efficiency, L7 47.7).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −8.2 (#4, efficiency, L7 28.8), Alex Sarr −6.7 (#7, efficiency, L7 28.2), James Harden −6.0 (#5, efficiency, L7 49.3).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | Josh Giddey, LaMelo Ball |
| efficiency | — |
| both | — |

- **Flagged and not active on ESPN:** none.
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 23 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** none.
- **Not flagged, but 10+ under projection over the last 7 days:** De'Aaron Fox (Matt Wright's Foxies, L7 15.7 in 3 vs projected 38.2, L7 gap −22.5, season gap −8.7), Trae Young (Team Nic Kerr, L7 28.8 in 4 vs projected 44.4, L7 gap −15.6, season gap −8.2), Josh Hart (Dr White Slong, L7 17.8 in 4 vs projected 33.0, L7 gap −15.3, season gap −9.2), Luka Doncic (Team Nic Kerr, L7 47.8 in 4 vs projected 60.6, L7 gap −12.9, season gap 1.4), Damian Lillard (Matt Wright's Foxies, L7 27.0 in 4 vs projected 38.6, L7 gap −11.6, season gap −8.2), Michael Porter Jr. (Team Nic Kerr, L7 28.0 in 3 vs projected 38.9, L7 gap −10.9, season gap −4.5), Brandon Miller (Matt Wright's Foxies, L7 27.3 in 3 vs projected 37.4, L7 gap −10.1, season gap −7.6).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 23.0 (1) → — | 42.2 | 44.3 |
| Nikola Jokic | Lauri Birds | 14 | 36.8 / 35.6 | 64.1 | 60.8 (4) | 63.0 (7) | 64.1 (14) → 67.2 (13) | 67.2 | 74.9 |
| Josh Hart | Dr White Slong | 13 | 30.1 / 31.5 | 23.8 | 17.8 (4) | 16.0 (6) | 23.2 (12) | 33.0 | 34.0 |
| Jalen Suggs | Lauri Birds | 7 | 29.6 / 26.3 | 24.7 | 30.0 (3) | 23.5 (4) | 25.5 (6) | 29.2 | 34.7 |

## Our pending trades

None.

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-22 07:27 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research, 22 Nov:** [ESPN scoreboard, 21 Nov](https://www.espn.com/nba/scoreboard/_/date/20261121) · [ESPN scoreboard, 22 Nov](https://www.espn.com/nba/scoreboard/_/date/20261122) · [Chicago Bulls On SI via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/3-bulls-takeaways-giddey-buzelis-043005109.html) · [ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910026) · [SI / OnSI, 22 Nov](https://www.si.com/nba/timberwolves/onsi/three-lamelo-ball-questions-timberwolves-win-grizzlies-01m80pwxp43s) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/lamelo-ball-dishes-out-seven-assists-vs-memphis) · [ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909999) · [Rip City Project, 17 Nov](https://ripcityproject.com/trail-blazers-finally-built-survive-occasional-damian-lillard-slump) · [ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910003) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910020) · [ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910024) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/damian-lillard-goes-cold-from-three-scores-15) · [SI / OnSI, 22 Nov](https://www.si.com/nba/trailblazers/onsi/3-missteps-in-blazers-loss-vs-jalen-brunson-and-the-knicks) · [ESPN box, 21 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910027) · [ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html) · [San Antonio Express-News via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/3-takeaways-wembanyamas-50-point-063130094.html) · [NY Daily News via Yahoo Sports, 22 Nov](https://sports.yahoo.com/articles/mikal-bridges-buzzer-beater-lifts-035800035.html) · [Basketnews, 21 Nov](https://basketnews.com/news-259955-luka-doncic-shares-critical-lakers-update-on-alarming-eye-injury.html) · [ESPN schedule, read 22 Nov](https://www.espn.com/nba/team/schedule/_/name/bkn/brooklyn-nets) · [NBC Sports, 20 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-20/brandon-miller-scores-19-points-with-five-triples) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-wont-play-saturday-540349) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310) · [ESPN schedule, read 22 Nov](https://www.espn.com/nba/team/schedule/_/name/no/new-orleans-pelicans) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-questionable-to-play-sunday-540393) · [ESPN box, 16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909995) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910011) · [Basketnews, 20 Nov](https://basketnews.com/news-259937-kawhi-leonard-injury-return-gets-huge-latest-timeline-for-raptors.html) · [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/) · [HEAVY via Yahoo Sports, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html)
