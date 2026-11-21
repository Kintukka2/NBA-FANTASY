# Slump Watch: 21 Nov 2026

- Generated 2026-11-21 07:21 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 111 rostered players in league 423671879, through scoring period 32. Teams have played **2 to 17 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 32 (Fri 20 Nov US) re-scored from ESPN's final NBA box scores: all 61 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**2 rostered players are 10+ FP/g under projection, on 1 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 69.1/60.5 · LaMelo Ball 34.2/46.4 · Josh Giddey 31.3/46.2 |
| Come-in Cider (us) | 0 | Cade Cunningham 50.1/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 47.5/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 61.3/57.6 · Donovan Mitchell 42.4/46.5 · Joel Embiid 37.5/45.4 |
| Lauri Birds | 0 | Nikola Jokic 64.1/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 48.4/56.8 · Cooper Flagg 51.0/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 49.7/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 51.1/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 44.9/50.0 · Jayson Tatum 45.9/48.1 · Kyrie Irving 41.4/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 62.1/60.6 · Domantas Sabonis 43.6/46.7 · Tyrese Maxey 46.8/45.1 |

## Since the last Slump Watch

Against [20261120-slump-watch.md](20261120-slump-watch.md):
- **Joined the flagged list:** nobody.
- **Left it:** Kel'el Ware. We dropped him on 20 Nov, and he is no longer rostered.
- **Gaps that moved 3+ FP/g:** none. Josh Giddey went from −13.8 to −14.9, and LaMelo Ball stayed at −12.2.
- **New to the Last 7 days lists:** Trae Young and Kevin Durant. Rudy Gobert and Ivica Zubac left them; we dropped Gobert on 20 Nov.

## Research

**Flagged:**

- **Josh Giddey (CHI):** His minutes are still 23–28 a game, and he was benched for the closing stretch again. He had 18 pts, 14 reb and 9 ast in 28 min in a 30-point win at BKN on 18 Nov. On 20 Nov he had 2 pts (1-6 FG), 6 reb and 7 ast in 23 min in the 98-94 loss to WSH ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910011); [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909309)). In that loss he had no assists and one shot in the third quarter, then sat the final eight minutes of regulation alongside Matas Buzelis (ours): "This isn't the first time either starter has been benched for the closing stretch" ([Chicago Tribune via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/chicago-bulls-eliminated-advancing-nba-055000339.html)). Rotoworld: "The Bulls closed with Tre Jones over him again" ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/josh-giddey-with-7-assists-on-friday-against-wiz)).
  - **Buzelis** had 9 pts (4-10) in 25 min on 20 Nov, after 25 pts in 30 min on 18 Nov (same ESPN boxes). From `form.py`: season 24.7 (15), L7 33.2 (5), L15 30.3 (7), L30 24.7 (15; equal to the season so far), Rate 29.5, projected 32.5.
- **LaMelo Ball (MIN):** His minutes are up since 17 Nov. He played 31 min vs POR on 17 Nov (18 pts, 7-17 FG) and 35 min vs NY on 19 Nov (15 pts, 6-21 FG, 3-10 3PT, 8 reb, 8 ast). MIN had no game on 20 Nov ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910003); [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910021)). He has scored under 20 in four straight games and is shooting 41.4% in November ([RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-struggles-with-shot-in-defeat/)). After the NY loss Chris Finch said "there was too much kind of hero ball down the stretch" and "He's got to get back to playmaking a little bit more than trying to score in all those situations" ([SI / OnSI, 20 Nov](https://www.si.com/nba/timberwolves/onsi/lamelo-ball-got-wake-up-call-he-needed-timberwolves-loss-01m7xacmqm8s)).

**New to the Last 7 days lists:**

- **Trae Young (WSH, not ATL):** The drop is his shooting. His minutes are normal. He shot 9-37 FG (24%) over his four L7 games:
  - 0-5 in 26 min in a 147-119 home loss to HOU on 15 Nov
  - 3-10 vs MEM on 16 Nov
  - 2-9 at TOR on 18 Nov
  - 4-13 at CHI on 20 Nov

  He played 32–35 min in each of the last three. His assists fell to 5 on 20 Nov ([ESPN box, 15 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909991); [16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909996); [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909309)). Rotoworld says he is neither taking nor making shots at the rate fantasy managers want and is no longer the league's assist leader, and notes no injury or role change ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/trae-young-with-16-and-three-steals-in-win)). No injury report was found. He plays for Washington and returned to Atlanta as a Wizard on 6 Nov ([Washington Post, 6 Nov](https://www.washingtonpost.com/sports/nba/2026/11/06/trae-young-wizards-hawks/69723a16-da5b-11f1-930a-e08f8086f5ac_story.html)).
- **Kevin Durant (HOU):** His scoring held up, but little else did:
  - In his five L7 games he scored 16–25 pts on 9–19 shots.
  - He had only 2–4 reb a game (15 in total), 1 steal and 1 block.
  - Two lopsided games held him to 29–30 min: a 28-point win at WSH on 15 Nov and an 18-point loss at MIA on 16 Nov.

  Box scores: [ESPN, 13 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909301); [15 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909991); [16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909998); [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910008); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909312). On 18 Nov he scored 21 on 7-9 FG with 2 reb, his eighth straight 20-point game ([RotoWire, 18 Nov](https://www.rotowire.com/basketball/headlines/kevin-durant-news-efficient-21-points-in-wednesdays-win-539862)). The run ended with 16 (6-9 FG) in 35 min at DEN on 20 Nov. The lower shot volume is the coach's plan. Ime Udoka said "Not having to rely on one person or play one specific style is beneficial" ([SI / OnSI, 7 Nov](https://www.si.com/nba/rockets/onsi/ime-udoka-explains-why-kevin-durant-is-taking-fewer-shots-with-rockets-01m6v8nzx3ns)). No injury was reported.

**Updates since 20 Nov:**

- **Tyler Herro (MIL, not MIA):** His minutes have swung:
  - 15 Nov loss to ATL: benched for the whole fourth quarter (5 pts, 2-13 FG, 20 min). ClutchPoints wrote that "Herro's playing time may no longer be guaranteed" ([ClutchPoints, 16 Nov](https://clutchpoints.com/nba/milwaukee-bucks/bucks-news-tyler-herros-total-no-show-vs-hawks-comes-complete-with-benching-that-will-ruffle-feathers)).
  - 18 Nov at MIA: 24 min (8 pts, 4-11, 0-5 3PT), graded "awful, yet again" ([SB Nation via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/bucks-vs-heat-player-grades-130000691.html)).
  - 19 Nov vs POR: 31 min (19 pts, 7-13, 4-7 3PT) ([ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910020)).

  No injury. MIL had no game on 20 Nov.
- **De'Aaron Fox (SA):** No new injury, and he started both games since his 15 Nov hip absence. He had 6 pts (3-10, 0-5 3PT) in 34 min vs DET on 17 Nov. On 19 Nov vs LAC he had 10 pts on 2-5 FG (6-6 FT), 5 ast and 4 TO in 32 min. In that game he started next to Castle, and Julian Champagnie took the spot of Dylan Harper ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910004); [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910022)). Harper has a left hip strain; the Spurs expect him to miss 2–3 weeks ([ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html)); *ESPN est.* 13 Dec. RotoWire noted that Fox took fewer than six shots for only the second time this season. Over nine November games he averages 10.4 pts in 27.3 min ([RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-deaaron-fox-scores-10-in-win/)).
- **Josh Hart (NY):** Still starting. He had 5 pts (2-5) in 31 min at TOR on 17 Nov. On 19 Nov at MIN he had 11 pts (4-9, 3-5 3PT) and 6 reb in 28 min, while Landry Shamet played 30 min off the bench ([ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002); [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910021)). NY had no game on 20 Nov. No new injury or lineup change was found.
- **Luka Doncic (LAL):** 25 pts on 9-18 FG (2-9 3PT), 4 reb, 8 ast, 2 stl and 6 TO in 36 min in the 106-104 win over SAC on 20 Nov. That is 50% shooting after 36-90 over his previous three games, but the turnovers stayed high: "Six turnovers also gave Sacramento opportunities to capitalize" ([Fadeaway World via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/lakers-player-ratings-luka-scores-054839704.html)). No injury or minutes news.
- **Michael Porter Jr. (BKN):** He started and had 16 pts (6-14, 3-6 3PT), 4 reb, 5 ast and 2 stl in 34 min in the 113-111 loss to ORL on 20 Nov ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909306)). No injury or role news. The Nets' lineup change that night was Danny Wolf starting in place of Egor Demin ([NY Post via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/nets-shake-everything-outcome-heartbreaking-034116642.html)).
- **Brandin Podziemski (GS):** He started and had 15 pts (5-12, 0-5 3PT), 3 reb and 2 ast in 32 min in the 126-98 loss at MEM on 19 Nov, the second night of a back-to-back ([ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019)). He is 0-for-10 from three over his last two games, and his minutes are steady at about 30 ([RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-three-point-drought-extends-in-loss/)). GS had no game on 20 Nov.
- **Brandon Miller (CHA):** New injury scare. He rolled his right ankle in the first quarter at ATL on 20 Nov when teammate Moussa Cisse landed on it. He left the game and later returned ([Basketnews, 21 Nov](https://basketnews.com/news-259942-what-happened-to-brandon-miller-hornets-star-suffers-alarming-injury-vs-hawks.html)). He finished with 19 pts (7-18, 5-13 3PT), 8 reb and 3 ast in 33 min ([RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-tallies-19-points-vs-atlanta/)). Charles Lee had no update after the game: "Postgame, our guys go in and get evaluated, so I don't have any updates for you" ([SI / OnSI, 20 Nov](https://www.si.com/nba/hornets/onsi/what-charles-lee-said-after-hornets-second-half-struggles-in-loss-to-hawks)). No timetable reported. He is not on ESPN's injury list, so there is no ESPN est. His minutes since returning on 15 Nov are 24, 32 and 33 ([ESPN box, 15 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909987); [17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910005); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909305)).

**Our pending trade:**

- **Stephon Castle (SA, we receive):** Dylan Harper has been out since 17 Nov with a left hip external rotator strain:
  - The Spurs expect him to miss 2–3 weeks, with his return depending on his response to treatment ([ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html)).
  - Shams Charania reported 1–3 weeks, depending on rehab ([MySA via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/shams-dylan-harper-could-miss-212718180.html)).
  - *ESPN est.* 13 Dec.

  In the first game without Harper, 19 Nov vs LAC, Castle had 21 pts, 12 ast, 6 reb, 4 stl and 8 TO in 33 min. He started next to Fox, with Champagnie in Harper's spot ([ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910022)). RotoWire says he could take on more ball-handling duties, which raises his upside as a secondary playmaker ([RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/nba/players/29232429/stephon-castle/fantasy/)). He has played 31–35 min in his last three games.
  - **Back-to-backs:** He has played all 16 Spurs games, including the second night of all three back-to-backs (24 Oct at DAL, 28 Oct at UTA, 7 Nov at POR), so there is no rest pattern ([ESPN game log, read 21 Nov](https://www.espn.com/nba/player/gamelog/_/id/4845367/stephon-castle)). SA's next back-to-back is Sun 29 Nov vs BOS and Mon 30 Nov at MIL ([ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/sa/san-antonio-spurs)).
- **Anthony Black (ORL, we send):** He is still starting and playing heavy minutes with Paolo Banchero out. On 20 Nov he had 13 pts (4-11), 7 reb, 6 ast, 3 stl, 2 blk and 5 TO in 37 min in the 113-111 win at BKN. He started with Suggs, Bane, Wagner and Carter ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909306)), and he has played 37 min in each of his last two games. RotoWire says his efficiency has dipped but his counting stats are strong, and he ranks in the top 10 in steals per game. Its 19 Nov note warned that Banchero's return could cut his opportunities ([RotoWire via CBS Sports, 19–21 Nov](https://www.cbssports.com/nba/players/28955672/anthony-black/fantasy/)).
  - **Banchero** has a right high-ankle sprain from 23 Oct. On 19 Nov he said "I'm not playing right now so I don't know when. But hopefully within the next couple of weeks" ([Basketnews, 19 Nov](https://basketnews.com/news-259854-paolo-banchero-shares-major-update-on-his-recovery-from-ankle-injury.html)). *ESPN est.* 29 Nov. No newer update was found.
  - **Back-to-backs:** He sat the second night of the 1–2 Nov back-to-back for "right ankle injury management" ([FantasyPros, 2 Nov](https://www.fantasypros.com/nba/news/617322/anthony-black-ankle-ruled-out-monday.php)). He played both nights of 10–11 Nov, 33 and 39 min ([ESPN game log, read 21 Nov](https://www.espn.com/nba/player/gamelog/_/id/4712849/anthony-black)). ORL's next back-to-back is Sat 28 Nov at WSH and Sun 29 Nov at DET ([ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/orl/orlando-magic)).

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 15 | 27.8 / 35.5 | 0.86 | 31.3 (15) | 36.4 (5) | 35.9 (7) | 31.3 (15) | 46.2 | **−14.9** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 16 | 28.2 / 32.9 | 0.86 | 34.2 (16) | 28.0 (4) | 34.1 (7) | 34.2 (16) | 46.4 | **−12.2** | 41.1 | Active |

- **Josh Giddey** (minutes): scoring −9.2, reb −3.3, ast −2.4, stocks −3.5, TO +1.1; bonus +2.5.
  - Current: 27.8 min, 9.9 pts, 3.8-9.1 FG, 1.2-1.9 FT, 5.9 reb, 8.4 ast, 0.4 stl, 0.5 blk, 3.3 TO
  - Last 7 days (5 GP): 28.0 min, 9.4 pts, 3.6-8.6 FG, 0.8-1.6 FT, 8.4 reb, 8.6 ast, 0.2 stl, 1.0 blk, 3.4 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
- **LaMelo Ball** (minutes): scoring −6.4, reb −1.3, ast −5.2, stocks +0.5, TO −0.4; bonus +0.7.
  - Current: 28.2 min, 17.6 pts, 6.2-15.4 FG, 1.6-2.1 FT, 4.3 reb, 5.7 ast, 1.8 stl, 0.1 blk, 3.5 TO
  - Last 7 days (4 GP): 30.0 min, 14.5 pts, 5.5-19.0 FG, 0.5-1.0 FT, 7.5 reb, 4.0 ast, 1.8 stl, 0.0 blk, 2.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Matas Buzelis −7.9 (#8, both, L7 33.2), Kawhi Leonard −5.8 (#2, minutes, L7 —).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Josh Hart −8.8 (#9, efficiency, L7 15.2), Joel Embiid −7.8 (#3, efficiency, L7 56.0), Derrick White −6.6 (#6, minutes, L7 27.3).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Kevin Durant −7.8 (#4, efficiency, L7 32.8), Ivica Zubac −7.0 (#7, minutes, L7 32.5), Darius Garland −6.9 (#5, efficiency, L7 42.5).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** Shai Gilgeous-Alexander −8.4 (#1, efficiency, L7 55.2), De'Aaron Fox −8.0 (#7, efficiency, L7 12.7), Damian Lillard −7.7 (#6, efficiency, L7 30.2), Brandon Miller −7.6 (#8, minutes, L7 27.3), Norman Powell −5.9 (#9, minutes, L7 36.2).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Tyler Herro −6.4 (#6, minutes, L7 19.5), Jalen Johnson −5.1 (#1, efficiency, L7 50.8).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** Trae Young −8.2 (#4, efficiency, L7 28.8), Alex Sarr −6.7 (#7, efficiency, L7 28.2), James Harden −6.0 (#5, efficiency, L7 50.2).

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

- **Flagged, but within 10 of projection over the last 7 days:** Josh Giddey (Cream Abdul-Yammar, L7 36.4 in 5 vs projected 46.2, season gap −14.9).
- **Not flagged, but 10+ under projection over the last 7 days:** De'Aaron Fox (Matt Wright's Foxies, L7 12.7 in 3 vs projected 38.2, L7 gap −25.5, season gap −8.0), Tyler Herro (Snow Time Lakers, L7 19.5 in 4 vs projected 38.8, L7 gap −19.3, season gap −6.4), Josh Hart (Dr White Slong, L7 15.2 in 4 vs projected 33.0, L7 gap −17.8, season gap −8.8), Trae Young (Team Nic Kerr, L7 28.8 in 4 vs projected 44.4, L7 gap −15.6, season gap −8.2), Luka Doncic (Team Nic Kerr, L7 47.8 in 4 vs projected 60.6, L7 gap −12.9, season gap 1.4), Michael Porter Jr. (Team Nic Kerr, L7 28.0 in 3 vs projected 38.9, L7 gap −10.9, season gap −4.5), Brandin Podziemski (Matt Wright's Foxies, L7 20.5 in 4 vs projected 30.8, L7 gap −10.3, season gap 2.2), Kevin Durant (Lauri Birds, L7 32.8 in 5 vs projected 42.9, L7 gap −10.1, season gap −7.8), Brandon Miller (Matt Wright's Foxies, L7 27.3 in 3 vs projected 37.4, L7 gap −10.1, season gap −7.6).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 23.0 (1) → — | 42.2 | 44.3 |
| Nikola Jokic | Lauri Birds | 14 | 36.8 / 35.6 | 64.1 | 60.8 (4) | 63.0 (7) | 64.1 (14) → 67.2 (13) | 67.2 | 74.9 |
| Jalen Suggs | Lauri Birds | 7 | 29.6 / 26.3 | 24.7 | 23.5 (4) | 23.5 (4) | 24.7 (7) | 29.2 | 34.7 |

## Our pending trades

With **Melbourne poopoo**, proposed by us, expires 22 Nov 03:13 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Stephon Castle | we receive | 16 | 29.5 / 32.7 | 34.8 | 48.0 (4) | 37.8 (8) | 35.1 (15) | 36.9 | −2.0 | Active |
| Anthony Black | we send | 12 | 33.1 / 28.9 | 38.3 | 32.0 (4) | 39.4 (8) | 38.3 (12) | 28.2 | +10.2 | Active |

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-21 07:21 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- **Research, 21 Nov:** [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910011) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909309) · [Chicago Tribune via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/chicago-bulls-eliminated-advancing-nba-055000339.html) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/josh-giddey-with-7-assists-on-friday-against-wiz) · [ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910003) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910021) · [RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-struggles-with-shot-in-defeat/) · [SI / OnSI, 20 Nov](https://www.si.com/nba/timberwolves/onsi/lamelo-ball-got-wake-up-call-he-needed-timberwolves-loss-01m7xacmqm8s) · [ESPN box, 15 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909991) · [16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909996) · [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/trae-young-with-16-and-three-steals-in-win) · [Washington Post, 6 Nov](https://www.washingtonpost.com/sports/nba/2026/11/06/trae-young-wizards-hawks/69723a16-da5b-11f1-930a-e08f8086f5ac_story.html) · [ESPN, 13 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909301) · [16 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909998) · [18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910008) · [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909312) · [RotoWire, 18 Nov](https://www.rotowire.com/basketball/headlines/kevin-durant-news-efficient-21-points-in-wednesdays-win-539862) · [SI / OnSI, 7 Nov](https://www.si.com/nba/rockets/onsi/ime-udoka-explains-why-kevin-durant-is-taking-fewer-shots-with-rockets-01m6v8nzx3ns) · [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/milwaukee-bucks/bucks-news-tyler-herros-total-no-show-vs-hawks-comes-complete-with-benching-that-will-ruffle-feathers) · [SB Nation via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/bucks-vs-heat-player-grades-130000691.html) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910020) · [ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910004) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910022) · [ClutchPoints via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html) · [RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-deaaron-fox-scores-10-in-win/) · [ESPN box, 17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910002) · [Fadeaway World via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/lakers-player-ratings-luka-scores-054839704.html) · [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909306) · [NY Post via Yahoo Sports, 21 Nov](https://sports.yahoo.com/articles/nets-shake-everything-outcome-heartbreaking-034116642.html) · [ESPN box, 19 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910019) · [RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-three-point-drought-extends-in-loss/) · [Basketnews, 21 Nov](https://basketnews.com/news-259942-what-happened-to-brandon-miller-hornets-star-suffers-alarming-injury-vs-hawks.html) · [RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-tallies-19-points-vs-atlanta/) · [SI / OnSI, 20 Nov](https://www.si.com/nba/hornets/onsi/what-charles-lee-said-after-hornets-second-half-struggles-in-loss-to-hawks) · [ESPN box, 15 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909987) · [17 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910005) · [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909305) · [MySA via Yahoo Sports, 19 Nov](https://sports.yahoo.com/articles/shams-dylan-harper-could-miss-212718180.html) · [RotoWire via CBS Sports, 20 Nov](https://www.cbssports.com/nba/players/29232429/stephon-castle/fantasy/) · [ESPN game log, read 21 Nov](https://www.espn.com/nba/player/gamelog/_/id/4845367/stephon-castle) · [ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/sa/san-antonio-spurs) · [RotoWire via CBS Sports, 19–21 Nov](https://www.cbssports.com/nba/players/28955672/anthony-black/fantasy/) · [Basketnews, 19 Nov](https://basketnews.com/news-259854-paolo-banchero-shares-major-update-on-his-recovery-from-ankle-injury.html) · [FantasyPros, 2 Nov](https://www.fantasypros.com/nba/news/617322/anthony-black-ankle-ruled-out-monday.php) · [ESPN game log, read 21 Nov](https://www.espn.com/nba/player/gamelog/_/id/4712849/anthony-black) · [ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/orl/orlando-magic)
