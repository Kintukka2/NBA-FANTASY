# Slump Watch: 08 Nov 2026

- Generated 2026-11-08 20:14 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 110 rostered players in league 423671879, through scoring period 20. Teams have played **2 to 11 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 19 (Sat 07 Nov US) re-scored from ESPN's final NBA box scores: all 47 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**7 rostered players are 10+ FP/g under projection, on 5 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 68.3/60.5 · LaMelo Ball 34.5/46.4 · Josh Giddey 27.2/46.2 |
| Lauri Birds | 2 | Nikola Jokic 64.4/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 50.6/43.0 |
| Dr White Slong | 1 | Giannis Antetokounmpo 58.9/57.6 · Donovan Mitchell 43.0/46.5 · Joel Embiid 35.1/45.4 |
| Matt Wright's Foxies | 1 | Shai Gilgeous-Alexander 48.1/56.8 · Cooper Flagg 50.6/45.4 · Evan Mobley 43.0/43.3 |
| Team Nic Kerr | 1 | Luka Doncic 68.3/60.6 · Domantas Sabonis 48.6/46.7 · Tyrese Maxey 46.8/45.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 48.9/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 46.1/43.9 |
| Melbourne poopoo | 0 | Anthony Davis 45.9/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 47.6/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 44.1/50.0 · Jayson Tatum 48.1/48.1 · Kyrie Irving 40.0/44.2 |

- **Injured players named in the table** (reported timeline, then *ESPN est.*):
  - **Anthony Davis** (WSH, Melbourne poopoo): right ankle sprain. He sat Friday at ATL and Saturday at OKC ([HoopsHype, 6 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/06/anthony-davis-right-ankle-sprain-is-now-out-for/92649819007/); [NBA injury report, 7 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-07_07_00PM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - **Anthony Edwards** (MIN, Melbourne poopoo): arthroscopic right knee surgery on 29 Oct, out "up to two months" per reports ([NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)). *ESPN est.* 21 Dec.
  - **Tyrese Haliburton** (IND, Lauri Birds): left hamstring strain. Carlisle says he is making progress but the timetable is uncertain; a fuller update is due next week ([NBC Sports / Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/carlisle-tyrese-haliburton-hammy-making-progress)). *ESPN est.* 13 Nov.
  - **Luka Doncic** (LAL, Team Nic Kerr): out tonight at DET with low back tightness. The Lakers hope it is one game and will check him before Monday at ATL, the second night of a back-to-back ([Lakers Nation, 8 Nov](https://lakersnation.com/lakers-injury-update-luka-doncic-out-vs-pistons/); [NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - **Kawhi Leonard** (ours): see *Come-in Cider* below. *ESPN est.* 23 Nov.

## Since the last Slump Watch

Against this morning's `docs/analysis/20261108-slump-watch.md` (07:44 UTC). No game finished in between: Sunday's first game had not tipped off when this ran. Every flagged player's season average and gap is unchanged. The L7 and L15 windows moved as the oldest day fell out, and a few near-the-line gaps moved slightly: Brandon Miller −6.5 → −6.9, Trae Young −6.7 → −6.9, Derrick White −6.9 → −6.8.

- **Joined:** none. **Left:** none. **Moved 3+ FP/g:** none.
- **Outlier rule:** a bad game is now dropped at 12+ FP under the next worst (15+ this morning).
  - Joel Embiid's 0-of-9 night on 6 Nov is now dropped: current 35.1 (8) → 38.7 (7), L7 26.3 (3) → 34.5 (2).
  - His ESPN status went from day-to-day to Active, and he is available today at CHI.
- **Windows:**
  - LaMelo Ball's L7 went from 38.5 (4) to 43.0 (3).
  - Brandon Miller's L7 went from 22.5 (4) to 12.3 (3).
- **Last 7 days list:** Jalen Johnson left it (L7 now 51.0). Jarrett Allen, Kevin Durant, Domantas Sabonis and Cameron Boozer joined.
- **Near the line:** CJ McCollum (Lauri Birds) is gone from the list; he is now on waivers.
- **Ours:** none flagged.
  - Anthony Black was added off waivers for Aday Mara.
  - Jalen Duren will be re-evaluated in two more weeks. His *ESPN est.* moved from 9 Nov to 24 Nov.
  - Trey Murphy III's L7 went from 34.0 (3) to 34.5 (2).
- **Pending trades:**
  - The Lauri Birds offer for Ivica Zubac was canceled (ESPN's transaction log).
  - The Melbourne poopoo offer, Kawhi Leonard + Murphy for Jalen Brunson, still expires 02:55 UTC Tue 10.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 8 | 27.2 / 35.5 | 0.77 | 27.2 (8) → 30.7 (7) | 30.0 (2) | 32.0 (6) | 27.2 (8) → 30.7 (7) | 46.2 | **−18.9** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 10 | 27.6 / 32.9 | 0.89 | 34.5 (10) | 43.0 (3) | 34.2 (8) | 34.5 (10) | 46.4 | **−11.9** | 41.1 | Active |

- **Josh Giddey** (both): scoring −10.5, reb −4.6, ast −4.0, stocks −3.7, TO +2.6; bonus +1.2.
  - Current: 27.2 min, 9.2 pts, 3.5-9.0 FG, 1.2-1.9 FT, 4.6 reb, 7.6 ast, 0.5 stl, 0.4 blk, 2.5 TO
  - Last 7 days (2 GP): 29.5 min, 11.5 pts, 4.5-11.0 FG, 1.0-2.0 FT, 2.5 reb, 8.0 ast, 0.5 stl, 1.0 blk, 3.0 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
  - **What explains it:** Splitter's rebuild moved the offense away from him.
    - Through eight games he took 9.0 shots a game, against 16.4 at the same point last season, and played about seven fewer minutes.
    - His defensive rebounds fell from 7.1 to 4.1 a game as Chicago crashes the offensive glass.
    - The Bulls' league-worst 27.2% from three has cut his assists ([Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)).
  - **Status:** a left wrist sprain from preseason that Chicago manages; Splitter says it has not affected his play ([Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)). He is not on Chicago's list for today's home game against PHI ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
  - His L7 rests on 2 games: noise.
- **LaMelo Ball** (minutes): scoring −5.3, reb −2.3, ast −4.4, stocks +0.4, TO −1.2; bonus +0.8.
  - Current: 27.6 min, 17.7 pts, 6.0-13.6 FG, 2.4-3.0 FT, 3.3 reb, 6.1 ast, 1.7 stl, 0.1 blk, 3.9 TO
  - Last 7 days (3 GP): 33.0 min, 25.3 pts, 8.3-15.7 FG, 4.3-5.0 FT, 3.3 reb, 5.7 ast, 1.3 stl, 0.3 blk, 4.3 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
  - **What explains the season gap:** minutes, 27.6 a game against 32.9 projected. Early on he had foul trouble and turnovers ([CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/)).
  - **The last 7 days:** L7 43.0 (3) against a season 34.5.
    - His minutes are up: 33.0 over the last 7 days, 27.6 for the season.
    - He has had "a little more shot volume" since Anthony Edwards went down ([CBS Sports / RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-drops-22-in-fridays-win/)).
    - Friday at NO: 22 points on 7-of-15 and 8 assists in 35 minutes ([CBS Sports / RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-drops-22-in-fridays-win/); [ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909293)).
  - **Status:** healthy.
    - The right wrist contusion from 2 Nov is off the reports ([NBC Sports / Rotoworld, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/lamelo-ball-records-20-points-vs-houston)).
    - He is not on Minnesota's list for tonight against UTAH ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
    - Edwards is out "up to two months" after knee surgery on 29 Oct ([NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)); *ESPN est.* 21 Dec.
- **Near the line:** Austin Reaves −6.6 (#4, efficiency, L7 32.8).

### Lauri Birds: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Ivica Zubac | IND | #8 | 5 | 20.6 / 31.1 | 0.98 | 23.0 (5) → 27.2 (4) | 19.5 (2) | 15.0 (3) → 19.5 (2) | 23.0 (5) → 27.2 (4) | 35.5 | **−12.5** | 36.3 | Active |
| Darius Garland | LAC | #5 | 8 | 33.8 / 35.2 | 0.74 | 28.6 (8) | 27.0 (3) | 27.2 (6) | 28.6 (8) | 40.4 | **−11.8** | 35.3 | Active |

- **Ivica Zubac** (minutes): scoring −9.3, reb −2.7, ast −0.0, stocks −4.0, TO −0.4; bonus +4.0.
  - Current: 20.6 min, 7.6 pts, 3.2-6.0 FG, 1.2-2.0 FT, 8.6 reb, 2.2 ast, 0.0 stl, 0.6 blk, 1.8 TO
  - Last 7 days (2 GP): 19.0 min, 5.5 pts, 2.0-5.0 FG, 1.5-2.0 FT, 8.0 reb, 3.5 ast, 0.0 stl, 0.0 blk, 2.0 TO
  - Projected: 31.1 min, 14.9 pts, 6.4-10.3 FG, 2.0-2.9 FT, 11.3 reb, 2.2 ast, 0.5 stl, 1.1 blk, 1.6 TO
  - **What explains it:** minutes since his return from a left ankle sprain that cost him five games.
    - Wednesday at MEM: 18:47 and 0-of-5 in his first game back ([RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/ivica-zubac-news-returning-versus-memphis-537562)).
    - Saturday against DEN in Mexico City: 10 points, 12 rebounds and 5 assists in 19 minutes, with foul trouble ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909938); [CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-double-doubles-despite-loss/)).
    - RotoWire expects him to get "closer to 30 minutes per game in the not too distant future" ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-double-doubles-despite-loss/)).
  - **Status:** healthy, no injury reported. Indiana plays at DAL on Monday ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
  - His L7 and his outlier-adjusted L15 rest on 2 games: small sample. Our offer for him has been canceled (see *Our pending trades*).
- **Darius Garland** (efficiency): scoring −1.1, reb −1.4, ast −1.6, stocks −3.5, TO −4.8; bonus +0.6.
  - Current: 33.8 min, 20.9 pts, 7.5-16.1 FG, 3.4-4.0 FT, 1.6 reb, 6.6 ast, 0.6 stl, 0.0 blk, 5.5 TO
  - Last 7 days (3 GP): 36.0 min, 19.0 pts, 6.3-13.3 FG, 4.3-4.7 FT, 1.7 reb, 7.3 ast, 0.3 stl, 0.0 blk, 5.3 TO
  - Projected: 35.2 min, 21.6 pts, 7.8-17.0 FG, 3.0-3.5 FT, 3.0 reb, 7.4 ast, 1.3 stl, 0.2 blk, 3.1 TO
  - **What explains it:** turnovers. He had 7 Monday against TOR ([NBC Sports / Rotoworld, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/darius-garland-records-eight-assists-seven-tos)), and 6 Wednesday against MIA, when he scored 26 on 10-of-14 ([NBC Sports / Rotoworld, 5 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-05/darius-garland-scores-team-high-26-points-vs-mia)).
  - **Status:** no game since Wednesday. He is not on the Clippers' list for tonight against NOP, and there is nothing new on his earlier back tightness ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
- **Near the line:** Kevin Durant −6.9 (#4, efficiency, L7 32.0), Lauri Markkanen −6.2 (#7, minutes, L7 44.0).
  - **Lauri Markkanen:** right wrist sprain, from his 6-minute exit on 26 Oct ([NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)).
    - He is questionable tonight at MIN ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf); [NBC Sports / Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/lauri-markkanen-wrist-questionable-sunday)). No timetable reported; *ESPN est.* 8 Nov.
    - `form.py`: L7 44.0 (3), L15 33.2 (6) → 39.8 (5), L30 32.5 (8) → 37.1 (7), season 32.5 (8) → 37.1 (7), projected 38.7.
    - His L7 is 11.5 over the season (`form.py`). His minutes are back up (34.7 over the last 7 days, 30.9 for the season), and the 26 Oct exit is dropped from the season figure as a short game.
  - **Kevin Durant:** see *Last 7 days*.

### Dr White Slong: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Joel Embiid | PHI | #3 | 8 | 32.2 / 31.6 | 0.76 | 35.1 (8) → 38.7 (7) | 26.3 (3) → 34.5 (2) | 34.0 (6) → 38.8 (5) | 35.1 (8) → 38.7 (7) | 45.4 | **−10.2** | 46.4 | Active |

- **Joel Embiid** (efficiency): scoring −13.1, reb +1.4, ast −0.4, stocks −1.6, TO −0.5; bonus +4.0.
  - Current: 32.2 min, 17.9 pts, 5.6-14.8 FG, 6.2-7.0 FT, 9.6 reb, 4.0 ast, 0.6 stl, 0.9 blk, 3.2 TO
  - Last 7 days (3 GP): 27.7 min, 15.7 pts, 4.3-12.7 FG, 7.0-7.3 FT, 10.0 reb, 2.0 ast, 0.3 stl, 0.7 blk, 3.0 TO
  - Projected: 31.6 min, 27.4 pts, 9.1-18.5 FG, 7.9-9.2 FT, 8.2 reb, 4.2 ast, 0.7 stl, 1.2 blk, 3.0 TO
  - **What explains it:** shooting.
    - Friday at CLE he went 0-of-9 from the field, scoring 6 points, all from the line, in 25 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289)). That is the outlier dropped from his windows.
    - Two nights earlier at DET he had 26 points and 15 rebounds in 33 minutes ([ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909922)).
    - He is managing plantar fasciitis in his right foot: a 25-minute limit on 2 Nov, and he sits back-to-backs ([Philadelphia Inquirer, 3 Nov](https://www.inquirer.com/sixers/joel-embiid-philadelphia-76ers-plantar-fasciitis-nick-nurse-injuries-20261103.html)).
  - **The last 7 days:** the 6 Nov game explains his L7 26.3 (3), against a season 35.1. Without it, his L7 is 34.5 (2): small sample.
  - **Status:** Available for today at CHI, listed for "plantar fascia injury management" ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf); [CBS Sports / RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/76ers-joel-embiid-probable-for-sunday/)).
- **Near the line:** Derrick White −6.8 (#6, minutes, L7 30.8), AJ Dybantsa −5.1 (#10, efficiency, L7 28.2).

### Matt Wright's Foxies: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jaren Jackson Jr. | UTAH | #8 | 4 | 26.0 / 31.4 | 0.86 | 27.0 (4) → 32.3 (3) | — | 13.5 (2) → 16.0 (1) | 27.0 (4) → 32.3 (3) | 38.1 | **−11.1** | 35.9 | **Out**, ESPN est. back 14 Dec |

- **Jaren Jackson Jr.** (minutes): scoring −5.4, reb −0.7, ast −0.2, stocks −5.1, TO −1.4; bonus +1.8.
  - Current: 26.0 min, 16.2 pts, 5.5-11.0 FG, 4.0-5.2 FT, 5.0 reb, 2.0 ast, 0.2 stl, 1.2 blk, 3.0 TO
  - Projected: 31.4 min, 21.9 pts, 7.8-16.7 FG, 4.3-5.4 FT, 5.7 reb, 2.1 ast, 1.2 stl, 1.6 blk, 2.3 TO
  - **Status:** torn right MCL on 26 Oct, in the 10-minute game dropped from his windows. No surgery needed.
    - Six to eight weeks reported, with a re-evaluation at about six weeks, around 8 Dec ([NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)). *ESPN est.* 14 Dec.
    - Out tonight at MIN; nothing new found ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
  - His L15 rests on 2 games, and 1 after the dropped game: small sample.
- **Near the line:** Shai Gilgeous-Alexander −8.7 (#1, efficiency, L7 55.0), Damian Lillard −8.1 (#6, efficiency, L7 31.5), Brandon Miller −6.9 (#9, minutes, L7 12.3), Naz Reid −6.6 (#10, efficiency, L7 29.7), De'Aaron Fox −5.4 (#7, efficiency, L7 23.0).

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 10 | 33.3 / 33.6 | 0.73 | 30.4 (10) | 29.8 (4) | 31.4 (9) | 30.4 (10) | 42.1 | **−11.7** | 45.1 | Active |

- **James Harden** (efficiency): scoring −6.4, reb +0.0, ast −4.6, stocks −2.0, TO +1.0; bonus +0.3.
  - Current: 33.3 min, 15.7 pts, 4.5-12.3 FG, 4.2-5.0 FT, 5.0 reb, 5.8 ast, 0.7 stl, 0.6 blk, 2.9 TO
  - Last 7 days (4 GP): 33.0 min, 14.2 pts, 4.0-11.5 FG, 3.8-4.5 FT, 5.2 reb, 5.0 ast, 0.5 stl, 1.0 blk, 2.2 TO
  - Projected: 33.6 min, 20.6 pts, 6.1-14.3 FG, 5.6-6.4 FT, 5.0 reb, 8.1 ast, 1.2 stl, 0.6 blk, 3.4 TO
  - **What explains it:** scoring and assists. His minutes are on projection.
    - Saturday against NYK: 7 points on 2-of-9, 5 assists and 2 blocks in 34 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940)).
    - Over his last five games: 14.0 points and 5.4 assists in 31.6 minutes ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-james-harden-struggles-in-loss/)).
    - Friday against PHI: 17 points and 3 assists in 30 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289)).
  - **Status:** no injury reported. Cleveland plays at CHA on Monday ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
- **Near the line:** Trae Young −6.9 (#4, efficiency, L7 29.5), Alex Sarr −6.5 (#7, efficiency, L7 37.0).

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Trey Murphy III −7.4 (#8, efficiency, L7 34.5), Kawhi Leonard −5.8 (#2, minutes, L7 —).
  - **Jalen Duren:** right hamstring strain.
    - The Pistons said Sunday that he is cleared for on-court work and will be re-evaluated in two weeks, about 22 Nov. Paul Reed stays the starting center ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work); [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)). *ESPN est.* 24 Nov.
    - He is out tonight against LAL ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
    - His season rests on 2 games, and 1 after his 10-minute exit is dropped: small sample.
  - **Trey Murphy III:** not on the Pelicans' list for tonight at LAC ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
    - He has played through bilateral patella tendinopathy ([NBA injury report, 8 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_01_00AM.pdf)).
    - Friday against MIN: 10 points on 3-of-7, 4 rebounds, 5 assists and 2 steals in 34 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909293)).
    - His L7 34.5 is 5.1 over his season (`form.py`), with more minutes: 37.0 over the last 7 days, 33.1 for the season. It rests on 2 games: noise.
  - **Kawhi Leonard:** left knee. Treatment for the swelling is finished and he is in the return-to-play process ([Raptors Republic, 3 Nov](https://raptorsrepublic.com/2026/11/03/raptors-announce-update-on-kawhi-leonards-health/)).
    - He is re-evaluated by 10 Nov, and RotoWire calls a return before the end of November unlikely ([CBS Sports / RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)). *ESPN est.* 23 Nov.
    - His season rests on 2 games: small sample.
  - **Scottie Barnes** (not near the line): left adductor soreness.
    - He missed Friday at MIL. He was limited in Sunday's practice and will be listed as questionable for Monday against MEM ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/)). No timetable reported; *ESPN est.* 9 Nov.
    - `form.py`: L7 44.3 (3), L15 45.2 (6) → 51.8 (5), L30 45.9 (8) → 50.7 (7), season 45.9 (8) → 50.7 (7), projected 43.7.
  - **Anthony Black** (added for Aday Mara, not near the line):
    - He left Saturday's overtime loss at GSW with left leg cramps, after 18 points, 8 rebounds, 6 assists, 4 steals and 3 blocks. There is no injury designation, and Orlando next plays Tuesday at SAC ([NBC Sports / Rotoworld, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)).
    - Tuesday at SAC and Wednesday at UTAH are a back-to-back. He sat the second night of the last one, on 2 Nov, for right ankle management ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)).
    - `form.py`: L7 41.0 (3), L15 38.5 (6) → 44.0 (5), L30 38.5 (6) → 44.0 (5), season 38.5 (6) → 44.0 (5), projected 28.2.

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −5.9 (#1, minutes, L7 51.0).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | Ivica Zubac, LaMelo Ball, Jaren Jackson Jr. |
| efficiency | Darius Garland, James Harden, Joel Embiid |
| both | Josh Giddey |

- **Flagged and not active on ESPN:** Jaren Jackson Jr. (**Out**, ESPN est. back 14 Dec).
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 10 Nov).
  - **Brandon Ingram:** recovering from heel surgery in May, during which a partially torn Achilles was found and treated. After a G League stint he said on Friday, "I'm pretty close" ([Yahoo Sports / USA Today, 7 Nov](https://sports.yahoo.com/articles/brandon-ingram-pretty-close-making-014045418.html)).
    - He is out tonight against NOP ([NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)).
    - No return date reported; *ESPN est.* 10 Nov.

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** LaMelo Ball (Cream Abdul-Yammar, L7 43.0 in 3 vs projected 46.4, season gap −11.9).
- **Not flagged, but 10+ under projection over the last 7 days:** Brandon Miller (Matt Wright's Foxies, L7 12.3 in 3 vs projected 37.4, L7 gap −25.1, season gap −6.9), Jarrett Allen (Dr White Slong, L7 15.5 in 2 vs projected 36.9, L7 gap −21.4, season gap −2.9), De'Aaron Fox (Matt Wright's Foxies, L7 23.0 in 4 vs projected 38.2, L7 gap −15.2, season gap −5.4), Trae Young (Team Nic Kerr, L7 29.5 in 4 vs projected 44.4, L7 gap −14.9, season gap −6.9), Amen Thompson (Matt Wright's Foxies, L7 28.7 in 3 vs projected 40.0, L7 gap −11.3, season gap −4.9), Kevin Durant (Lauri Birds, L7 32.0 in 3 vs projected 42.9, L7 gap −10.9, season gap −6.9), Austin Reaves (Cream Abdul-Yammar, L7 32.8 in 4 vs projected 43.3, L7 gap −10.6, season gap −6.6), LeBron James (Cream Abdul-Yammar, L7 32.0 in 3 vs projected 42.5, L7 gap −10.5, season gap −3.6), Domantas Sabonis (Team Nic Kerr, L7 36.3 in 3 vs projected 46.7, L7 gap −10.4, season gap 1.9), Cameron Boozer (Lauri Birds, L7 24.3 in 3 vs projected 34.3, L7 gap −10.0, season gap 0.0).

### Notes

L7, L15 and L30 for players outside the tables come from `python council/form.py`, run 20:27 UTC.

- **LaMelo Ball:** see *Cream Abdul-Yammar*. His minutes are up with Anthony Edwards out.
- **Brandon Miller (CHA):** L7 12.3 (3), L15 35.0 (8), L30 30.5 (10), season 30.5 (10), projected 37.4.
  - **The last 7 days:** 18.2 under his season (`form.py`), with 23.7 minutes over the last 7 days against 31.0 for the season.
  - Friday against BOS he left in the second quarter with right groin soreness: 8 points on 3-of-10 in 14 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909288)).
  - Through nine games he shot 35.6% from the field ([Here Rock Hill, 8 Nov](https://www.hererockhill.com/2026/11/08/hornets-brandon-miller-groin-injury-evaluation-monday/)).
  - **Status:** Charles Lee said he would be re-evaluated over the weekend, with more news by Monday, when Charlotte hosts CLE ([Here Rock Hill, 8 Nov](https://www.hererockhill.com/2026/11/08/hornets-brandon-miller-groin-injury-evaluation-monday/)). No timetable reported; *ESPN est.* 9 Nov.
- **Jarrett Allen (CLE):** L7 15.5 (2) → 31.0 (1), L15 34.6 (7) → 40.3 (6), L30 34.0 (8) → 38.9 (7), season 34.0 (8) → 38.9 (7), projected 36.9.
  - His L7 rests on 2 games, and 1 after the drop: noise and a small sample.
  - The dropped game is his 7-minute exit on 4 Nov against OKC, after a knee-to-knee collision with Jared McCain ([Heavy, 7 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/jarrett-allen-injury-knicks/)).
  - **Status:** right knee contusion. He sat Friday against PHI and Saturday against NYK. No return date reported, and Cleveland plays at CHA on Monday ([Heavy, 7 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/jarrett-allen-injury-knicks/); [NBA injury report, 7 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-07_07_00PM.pdf)). *ESPN est.* 9 Nov.
- **De'Aaron Fox (SA):** L7 23.0 (4), L15 31.1 (8), L30 32.8 (10), season 32.8 (10), projected 38.2.
  - **The last 7 days:** 9.8 under his season (`form.py`), with fewer minutes: 25.8 over the last 7 days against 29.5 for the season.
  - Friday at SAC he played 26 minutes (9 points, +13). Saturday at POR he played 22 minutes (8 points on 1-of-3, 6 assists, +23) ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909295); [ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909944)).
  - No injury or role report found.
- **Trae Young (WSH):** L7 29.5 (4), L15 35.8 (8), L30 37.5 (10), season 37.5 (10), projected 44.4.
  - **The last 7 days:** 8.0 under his season (`form.py`).
    - Friday at ATL: 23 points and 10 assists, but 9 turnovers ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909287)).
    - Saturday at OKC: 4 points on 1-of-6 in 28 minutes, his lowest total since 4 Nov 2024, in a 114-75 loss ([CBS Sports / RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/wizards-trae-young-shooting-woes-in-blowout-loss/); [ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909941)).
    - Anthony Davis (right ankle sprain) sat both games ([HoopsHype, 6 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/06/anthony-davis-right-ankle-sprain-is-now-out-for/92649819007/); [NBA injury report, 7 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-07_07_00PM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - No injury found for Young.
- **Amen Thompson (HOU):** L7 28.7 (3), L15 30.9 (8), L30 35.1 (10), season 35.1 (10), projected 40.0.
  - **The last 7 days:** 6.4 under his season (`form.py`). The cause is shooting and one short night.
    - Monday: 25 minutes. Wednesday against MIN: 11 points on 3-of-9 ([SI Rockets On SI, 4 Nov](https://www.si.com/nba/rockets/onsi/best-in-west-rockets-take-on-timberwolves-preview-injuries-starters-how-to-watch-01m6kjmaqtvt); [ESPN box score, 4 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909930)).
    - Saturday at PHX he bounced back with 17 points, 7 rebounds and 4 blocks in 39 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943)).
  - No injury found.
- **Kevin Durant (HOU):** L7 32.0 (3), L15 35.1 (8), L30 36.0 (10), season 36.0 (10), projected 42.9. His L7 is within 5 of his season.
  - Saturday at PHX: 21 points on 5-of-14 (1-of-7 from three) and 10 rebounds in 38 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943)).
  - No injury found.
- **Austin Reaves (LAL):** L7 32.8 (4), L15 33.5 (8) → 37.0 (7), L30 36.7 (10) → 39.8 (9), season 36.7 (10) → 39.8 (9), projected 43.3.
  - The cause is shooting. Friday against POR: 25 points on 8-of-22 (1-of-8 from three) and 4 steals in 38 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909294)).
  - No injury found. Luka Doncic is out tonight at DET (see the headline).
- **LeBron James (PHI):** L7 32.0 (3) → 40.0 (2), L15 38.2 (6) → 42.6 (5), L30 38.9 (8) → 42.1 (7), season 38.9 (8) → 42.1 (7), projected 42.5.
  - The gap comes from one game. Friday at CLE: 8 points on 3-of-12 (0-of-4 from three) and 6 turnovers in 32 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289)).
  - That game is dropped as an outlier. Without it, his L7 is 40.0 (2): small sample.
  - No injury found.
- **Domantas Sabonis (SAC):** L7 36.3 (3), L15 43.3 (7), L30 48.6 (9), season 48.6 (9), projected 46.7.
  - **The last 7 days:** 12.2 under his season (`form.py`), with fewer minutes: 32.3 over the last 7 days against 35.6 for the season.
  - Friday against SA: 17 points on 8-of-12 and 12 rebounds in 31 minutes, at −22 ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909295)).
  - NBC: "he isn't getting the ball much", though his role is not expected to change ([NBC Sports / Rotoworld, 7 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-07/domantas-sabonis-with-17-12-in-loss-to-the-spurs)).
  - No injury found.
- **Cameron Boozer (MEM):** L7 24.3 (3), L15 34.3 (7), L30 34.3 (9), season 34.3 (9), projected 34.3.
  - **The last 7 days:** 10.0 under his season (`form.py`). His minutes held (34.0 over the last 7 days, 32.0 for the season), so the cause is shooting.
  - Friday against OKC: 8 points on 2-of-14 (0-of-8 from three), 12 rebounds and 4 assists in 31 minutes ([ESPN box score, 6 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909291); [NBC Sports / Rotoworld, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/cameron-boozer-grabs-12-boards-in-blowout-loss)).
  - No injury found.

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Trey Murphy III | Come-in Cider (us) | 8 | 33.1 / 32.5 | 29.4 | 34.5 (2) | 32.8 (6) | 29.4 (8) | 36.8 | 41.6 |
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| Lauri Markkanen | Lauri Birds | 8 | 30.9 / 34.0 | 32.5 | 44.0 (3) | 33.2 (6) → 39.8 (5) | 32.5 (8) → 37.1 (7) | 38.7 | 44.4 |
| Nikola Jokic | Lauri Birds | 8 | 35.9 / 35.6 | 64.4 | 72.0 (3) | 70.0 (7) | 64.4 (8) → 70.0 (7) | 67.2 | 74.9 |

## Our pending trades

With **Melbourne poopoo**, proposed by us, expires 10 Nov 02:55 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Jalen Brunson | we receive | 9 | 33.9 / 35.3 | 39.4 | 45.3 (3) | 43.7 (7) | 39.4 (9) | 43.8 | −4.4 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | — | — | 40.0 (2) | 45.8 | −5.8 | **Out**, ESPN est. back 23 Nov |
| Trey Murphy III | we send | 8 | 33.1 / 32.5 | 29.4 | 34.5 (2) | 32.8 (6) | 29.4 (8) | 36.8 | −7.4 | Active |

### Notes

- **Lauri Birds offer for Ivica Zubac:** canceled. ESPN's transaction log lists it as `CANCELED`, so only this offer remains.
- **Jalen Brunson:** his L7 45.3 (3) is 5.9 over his season 39.4 (`form.py`), on shot volume.
  - Saturday at CLE: 31 points on 12-of-25, 9 assists and 1 turnover in 34 minutes ([ESPN box score, 7 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940)).
  - No in-season injury news found.
- **Kawhi Leonard:** re-evaluated by 10 Nov ([CBS Sports / RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)).
  - That update may come after this offer expires at 02:55 UTC Tue 10 (9:55 pm ET Mon 9).
  - *ESPN est.* 23 Nov. His season 40.0 rests on 2 games: small sample.
- **Trey Murphy III:** see *Come-in Cider*. He is off tonight's injury report, and his L7 34.5 (2) is noise.

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-08 20:14 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- ESPN fantasy API `mTransactions2` view (scoring periods 19–20), read 2026-11-08 20:35 UTC, for the canceled Lauri Birds offer.
- `python council/form.py` (20:27 and 20:34 UTC) for L7, L15 and L30 of players outside the tables, and `python council/injuries.py` for *ESPN est.*
- News cited in this run (opened on 8 Nov, or carried over from earlier Slump, Injury and News Watch reports):
  - [NBA injury report, 8 Nov 3:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_00PM.pdf)
  - [NBA injury report, 8 Nov 1:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_01_00AM.pdf)
  - [NBA injury report, 7 Nov 7:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-07_07_00PM.pdf)
  - [HoopsHype, 6 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/06/anthony-davis-right-ankle-sprain-is-now-out-for/92649819007/)
  - [NBA.com / AP, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)
  - [NBC Sports / Rotoworld, 7 Nov (Haliburton)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/carlisle-tyrese-haliburton-hammy-making-progress)
  - [Lakers Nation, 8 Nov](https://lakersnation.com/lakers-injury-update-luka-doncic-out-vs-pistons/)
  - [Basketball Australia, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)
  - [CBS Sports / AP, 1 Nov](https://www.cbssports.com/nba/news/timberwolves-host-bucks-with-lamelo-ball-in-the-spotlight/)
  - [CBS Sports / RotoWire, 7 Nov (Ball)](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-drops-22-in-fridays-win/)
  - [NBC Sports / Rotoworld, 4 Nov (Ball)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/lamelo-ball-records-20-points-vs-houston)
  - [RotoWire, 4 Nov (Zubac)](https://www.rotowire.com/basketball/headlines/ivica-zubac-news-returning-versus-memphis-537562)
  - [CBS Sports / RotoWire, 8 Nov (Zubac)](https://www.cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-double-doubles-despite-loss/)
  - [NBC Sports / Rotoworld, 3 Nov (Garland)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/darius-garland-records-eight-assists-seven-tos)
  - [NBC Sports / Rotoworld, 5 Nov (Garland)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-05/darius-garland-scores-team-high-26-points-vs-mia)
  - [Philadelphia Inquirer, 3 Nov](https://www.inquirer.com/sixers/joel-embiid-philadelphia-76ers-plantar-fasciitis-nick-nurse-injuries-20261103.html)
  - [CBS Sports / RotoWire, 7 Nov (Embiid)](https://www.cbssports.com/fantasy/basketball/news/76ers-joel-embiid-probable-for-sunday/)
  - [NBA.com / AP, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)
  - [CBS Sports / RotoWire, 8 Nov (Harden)](https://www.cbssports.com/fantasy/basketball/news/cavaliers-james-harden-struggles-in-loss/)
  - [NBC Sports / Rotoworld, 7 Nov (Markkanen)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/lauri-markkanen-wrist-questionable-sunday)
  - [NBC Sports / Rotoworld, 8 Nov (Duren)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work)
  - [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)
  - [Raptors Republic, 3 Nov](https://raptorsrepublic.com/2026/11/03/raptors-announce-update-on-kawhi-leonards-health/)
  - [CBS Sports / RotoWire, 3 Nov (Leonard)](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)
  - [CBS Sports / RotoWire, 8 Nov (Barnes)](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/)
  - [NBC Sports / Rotoworld, 8 Nov (Black)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)
  - [Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)
  - [Yahoo Sports / USA Today, 7 Nov](https://sports.yahoo.com/articles/brandon-ingram-pretty-close-making-014045418.html)
  - [Here Rock Hill, 8 Nov](https://www.hererockhill.com/2026/11/08/hornets-brandon-miller-groin-injury-evaluation-monday/)
  - [Heavy, 7 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/jarrett-allen-injury-knicks/)
  - [CBS Sports / RotoWire, 8 Nov (Young)](https://www.cbssports.com/fantasy/basketball/news/wizards-trae-young-shooting-woes-in-blowout-loss/)
  - [SI Rockets On SI, 4 Nov](https://www.si.com/nba/rockets/onsi/best-in-west-rockets-take-on-timberwolves-preview-injuries-starters-how-to-watch-01m6kjmaqtvt)
  - [NBC Sports / Rotoworld, 7 Nov (Sabonis)](https://nbcsports.com/fantasy/basketball/player-news/2026-11-07/domantas-sabonis-with-17-12-in-loss-to-the-spurs)
  - [NBC Sports / Rotoworld, 6 Nov (Boozer)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/cameron-boozer-grabs-12-boards-in-blowout-loss)
  - ESPN box scores: [4 Nov PHI at DET](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909922), [4 Nov MIN at HOU](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909930), [6 Nov WSH at ATL](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909287), [6 Nov BOS at CHA](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909288), [6 Nov PHI at CLE](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909289), [6 Nov OKC at MEM](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909291), [6 Nov MIN at NO](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909293), [6 Nov POR at LAL](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909294), [6 Nov SA at SAC](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909295), [7 Nov DEN vs IND](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909938), [7 Nov NY at CLE](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909940), [7 Nov WSH at OKC](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909941), [7 Nov HOU at PHX](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909943), [7 Nov SA at POR](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/summary?event=401909944)
