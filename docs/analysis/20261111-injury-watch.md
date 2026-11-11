# Injury Watch: 11 Nov 2026

- Generated 2026-11-11 21:12 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 97 players in ESPN's injury feed. 32 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (09 Nov–15 Nov) / next week (16 Nov–22 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Jrue Holiday 28.7 (L7 19.5), Isaiah Hartenstein 29.7 (L7 30.0), Trey Murphy III 31.0 (L7 38.5), Jalen Smith 31.6 (L7 29.5), Dejounte Murray 32.8 (L7 22.8). A pickup at or above **32.8** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Charles Bassey** | GS | Brandon Williams (22 Nov), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 23.0 | +11.9 | **33.0** | 20.7 | 26.3 (3) | 19.8 (8) | 20.7 (9) | Free agent | 1% | 2 / 4 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (13 Nov) | 10 | 28.7 | +6.7 | **30.7** | 30.5 | 21.7 (3) | 25.0 (7) | 30.5 (10) | Waivers | 39% | 2 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 8 | 23.1 | +9.6 | **30.5** | 25.4 | 34.2 (4) | 30.5 (8) | 25.4 (11) | Free agent | 25% | 3 / 3 |
| **Ryan Kalkbrenner** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov); also out: Moussa Diabate (12 Nov), Grant Williams (12 Nov) | 2 | 28.0 | +10.9 | **30.0** | 21.5 | 25.7 (3) | 19.8 (8) | 21.5 (11) | Free agent | 2% | 2 / 2 |
| **Daniss Jenkins** | DET | Jalen Duren (24 Nov) | 8 | 27.8 | +9.2 | **29.9** | 28.1 | 40.0 (3) | 27.9 (7) | 28.1 (10) | Free agent | 16% | 2 / 4 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 9 | 34.0 | +6.5 | **29.0** | 29.0 | 19.3 (3) | 29.9 (7) | 29.0 (9) | Free agent | 36% | 2 / 4 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 10 | 25.8 | +5.5 | **27.6** | 28.2 | 32.0 (4) | 26.4 (9) | 28.2 (12) | Free agent | 39% | 2 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (13 Nov) | 9 | 29.2 | +3.8 | **27.6** | 27.6 | 27.0 (3) | 27.0 (6) | 27.6 (9) | Free agent | 11% | 2 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 18.0 | — | **26.7** | 26.7 | 38.0 (1) | 28.8 (4) | 26.7 (6) | Free agent | 1% | 2 / 3 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 8 | 27.8 | +8.2 | **25.4** | 21.8 | 32.2 (4) | 25.4 (8) | 21.8 (11) | Free agent | 36% | 3 / 3 |
| **Kevin Huerter** | DET | Jalen Duren (24 Nov) | 8 | 24.1 | +5.1 | **25.0** | 22.5 | 37.0 (3) | 26.0 (7) | 22.5 (10) | Free agent | 3% | 2 / 4 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 22.3 | — | **24.1** | 24.3 | 25.3 (3) | 26.2 (8) | 24.3 (11) | Free agent | 5% | 3 / 3 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 8 | 31.1 | +7.6 | **24.0** | 24.8 | 13.0 (3) | 20.6 (7) | 24.8 (10) | Free agent | 11% | 3 / 3 |
| **Collin Murray-Boyles** (day to day, ESPN est. back 11 Nov) | TOR | Kawhi Leonard (23 Nov) | 7 | 23.1 | +4.1 | **24.0** | 24.4 | 36.0 (2) | 25.7 (6) | 24.4 (9) | Free agent | 13% | 3 / 3 |
| **Royce O'Neale** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov); also out: Moussa Diabate (12 Nov), Grant Williams (12 Nov) | 2 | 24.5 | +6.4 | **22.5** | 12.9 | 18.0 (3) | 13.5 (8) | 12.9 (11) | Free agent | 1% | 2 / 2 |
| **Dylan Cardwell** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 4 | 18.8 | — | **21.8** | 21.8 | 21.8 (4) | 21.8 (4) | 21.8 (4) | Free agent | 1% | 2 / 3 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 9 | 32.8 | +5.2 | **20.8** | 19.5 | 18.3 (3) | 23.1 (7) | 19.5 (10) | Free agent | 6% | 2 / 3 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (13 Nov) | 10 | 24.3 | — | **20.4** | 20.4 | 13.0 (3) → 20.0 (2) | 21.4 (7) → 25.2 (6) | 20.4 (10) → 22.8 (9) | Free agent | 1% | 2 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 16 Nov | 5 | 41.5 | — | — | 41.5 (2) → 68.0 (1) | 24.7 | 22.5 | Free agent | 14% | 3 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 9 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 3 / 4 |
| **Norman Powell** | CHI | Right Shoulder Inflammation | 11 Nov | 0 | 26.2 | 4.0 (1) → — | 25.2 (5) → 30.5 (4) | 26.2 (8) → 29.4 (7) | 36.0 | 33.0 | Free agent | 76% | 3 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 16 Nov | 5 | 26.3 | — | — | 26.3 (3) | 29.2 | 34.7 | Free agent | 16% | 2 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 21 Nov | 10 | 14.2 | — | 9.5 (2) | 14.2 (5) | 30.6 | 27.1 | Free agent | 9% | 3 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 8 | — | — | — | — | 30.1 | 28.0 | Free agent | 43% | 3 / 3 |
| **Myles Turner** | MIL | Rest | 13 Nov | 2 | 25.1 | 21.8 (4) | 27.2 (8) | 25.1 (11) | 28.4 | 28.6 | Free agent | 50% | 3 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 11 Nov | 0 | 18.6 | — | 16.0 (3) | 18.6 (5) | 25.6 | 28.3 | Free agent | 2% | 3 / 3 |
| **Devin Vassell** | SA | Left Groin | 11 Nov | 0 | 28.3 | 32.3 (3) | 31.0 (7) | 28.3 (10) | 26.8 | 27.3 | Free agent | 38% | 3 / 3 |
| **Quentin Grimes** | LAL | Finger | 15 Nov | 4 | 16.6 | 12.7 (3) | 14.5 (8) | 16.6 (11) | 28.1 | 25.8 | Free agent | 27% | 2 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 4 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 3 |
| **Precious Achiuwa** | SAC | Left Lower Leg Bruise | 13 Nov | 2 | 28.0 | 20.5 (4) | 24.8 (8) → 27.9 (7) | 28.0 (11) → 30.5 (10) | 24.1 | 27.0 | Waivers | 23% | 2 / 3 |
| **Bennedict Mathurin** | NO | Right Thumb Sprain | 13 Nov | 2 | 9.8 | 5.5 (4) | 7.8 (8) | 9.8 (11) | 25.1 | 27.6 | Free agent | 7% | 3 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 1 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 3 / 3 |
| **Nolan Traore** | BKN | Right Calf Soreness | 11 Nov | 0 | 26.6 | 35.3 (3) | 32.0 (7) | 26.6 (10) → 29.2 (9) | 21.6 | 17.5 | Free agent | 15% | 2 / 3 |
| **Tristan da Silva** | ORL | Left Calf Strain | 11 Nov | 0 | 25.9 | 26.5 (2) | 25.8 (6) | 25.9 (9) | 17.2 | 21.2 | Free agent | 11% | 2 / 4 |
| **Collin Murray-Boyles** | TOR | Illness | 11 Nov | 0 | 24.4 | 36.0 (2) | 25.7 (6) | 24.4 (9) | 24.8 | 25.6 | Free agent | 13% | 3 / 3 |
| **T.J. McConnell** | IND | Hamstring | 11 Nov | 0 | 8.5 | 8.5 (2) | 8.5 (2) | 8.5 (2) | 24.4 | 25.5 | Free agent | 8% | 3 / 3 |
| **Isaiah Stewart** | MEM | Right Knee Bruise | 11 Nov | 0 | 22.9 | 9.0 (1) | 23.6 (5) | 22.9 (7) | 25.3 | 25.1 | Free agent | 4% | 3 / 4 |

### Notes

- Official report used: [NBA injury report, 11 Nov 4:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_04_15PM.pdf).
- **Dereck Lively II** (DAL): no timetable reported; week-to-week per RotoWire on 1 Nov ([CBS/RotoWire](https://www.cbssports.com/nba/players/28951880/dereck-lively-ii/fantasy/)). Nothing supports *ESPN est.* 12 Nov.
- **Tobias Harris** (SA): no timetable reported; out 11 Nov, "very casual" shots at shootaround ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tobias-harris-calf-seen-at-shootaround)). *ESPN est.* 19 Nov.
- **Jusuf Nurkic** (UTAH): partial plantar plate tear; on-court work, re-evaluated in two weeks from 6 Nov, about 20 Nov ([KSL, 6 Nov](https://sports.ksl.com/nba/utah-jazz/jusuf-nurkic-utah-jazz/578803)). *ESPN est.* 20 Nov is the re-evaluation, not a return.
- **Scotty Pippen Jr.** (MEM): now a lumbar disc herniation, out 11 Nov, no timetable reported ([Hoops Rumors, 7 Nov](https://www.hoopsrumors.com/2026/11/grizzlies-notes-pippen-stewart-losing-streak-jackson.html)); *ESPN est.* 21 Nov is at risk.
- **Myles Turner** (MIL): rest on the second night of a back-to-back; expected back 13 Nov at ORL ([CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-myles-turner-resting-wednesday/)); *ESPN est.* 13 Nov.
- **Precious Achiuwa** (SAC, waivers): left the 10 Nov game with a left lower-leg contusion ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/precious-achiuwa-leg-exits-during-third-quarter)); no timetable reported; *ESPN est.* 13 Nov, in doubt.
- **Nolan Traore** (BKN): questionable 11 Nov with right calf soreness ([NBC Sports, 10 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-10/nolan-traore-calf-questionable-wednesday-vs-nor)); *ESPN est.* 11 Nov.
- **Tristan da Silva** (ORL): left calf strain, questionable 11 Nov ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tristan-da-silva-calf-questionable-vs-utah)); *ESPN est.* 11 Nov.
- **Jaylon Tyson** (CLE): right ankle sprain, six games missed, questionable 11 Nov ([CBS/RotoWire, 10 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-questionable-for-wednesday/)); *ESPN est.* 11 Nov.
- **Bennedict Mathurin** (NO): right thumb sprain, out 11 Nov, described as not serious ([Heavy, 11 Nov](https://heavy.com/sports/nba/new-orleans-pelicans/pelicans-get-concerning-bennedict-mathurin-injury-update/)); no timetable reported; *ESPN est.* 13 Nov.
- **Yves Missi** (NO): out 11 Nov, his 10th straight game, no timetable reported ([Pelicans, 11 Nov](https://www.nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand)); our override puts his floor at 18 Nov; *ESPN est.* 16 Nov.
- **Maxime Raynaud** (SAC): week-to-week pending a re-evaluation ([RotoWire via CBS, 9 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-for-tuesday/)); override floor 16 Nov; *ESPN est.* 15 Nov.
- **Jalen Suggs** (ORL): back to court work, week-to-week ([NBC Sports, 9 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-09/report-suggs-knee-progressing-positively)); *ESPN est.* 16 Nov.
- **Norman Powell** (CHI): questionable 11 Nov, now low back spasms ([Heavy, 11 Nov](https://heavy.com/sports/nba/chicago-bulls/injury-report-vs-spurs-november-11/)); no timetable reported; *ESPN est.* 11 Nov.
- **Devin Vassell** (SA): questionable 11 Nov, left adductor tightness, a game-time decision ([ClutchPoints, 11 Nov](https://clutchpoints.com/nba/nba-stories/spurs-vs-bulls-injury-report-devin-vassell-norman-powell-among-players-listed)); no timetable reported; *ESPN est.* 11 Nov.
- **Quentin Grimes** (LAL): finger sprain, out 11 Nov; LAL next play 15 Nov ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/lakers-quentin-grimes-downgraded-to-out/)); *ESPN est.* 15 Nov.
- **Collin Murray-Boyles** (TOR): questionable (illness) 11 Nov on the [official report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_02_00PM.pdf); *ESPN est.* 11 Nov.
- **T.J. McConnell** (IND): questionable 11 Nov, on a minutes limit since his return ([NBC Sports, 10 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-10/t-j-mcconnell-hamstring-questionable-wednesday)); *ESPN est.* 11 Nov.
- **Isaiah Stewart** (MEM): no news found; *ESPN est.* 11 Nov.

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 32.8.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 1 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 3 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 13 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 2 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 4 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 8 | 30.1 (30.5) | 28.0 (63) | Free agent | 43% | 3 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 9 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 3 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 18 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 2 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 52 | 38.8 (32.4) | 41.6 (38) | Free agent | 29% | 2 / 4 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 52 | 36.9 (27.7) | 32.3 (32) | Free agent | 34% | 2 / 4 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 84 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 2 / 3 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 111 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 2 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 142 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 2 / 4 |

### Notes

- **Jimmy Butler III** (GS): ACL repair; back around the one-year mark of 19 Jan 2026 ([Heavy, 5 Nov](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/)); January–February ([CBS, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-targeting-january-to-february-return/)). *ESPN est.* 2 Jan is optimistic.
- **Kristaps Porzingis** (GS): stepped away from basketball for his health on 6 Nov, "not with team" ([Bleacher Report](https://bleacherreport.com/articles/25529995-kristaps-porzingis-announces-he-will-step-away-warriors-statement-amid-health-issues)); no timetable reported; *ESPN est.* 2 Jan is a placeholder.
- **Shaedon Sharpe** (POR): meniscus repair 26 Aug, re-evaluated in six months ([Blazers, 27 Aug](https://www.nba.com/blazers/news/shaedon-sharpe-injury-update-7)); *ESPN est.* 2 Mar.
- **Donte DiVincenzo** (MIN): Achilles surgery in April; "on schedule, if not… ahead" ([ClutchPoints, 2 Nov](https://clutchpoints.com/nba/minnesota-timberwolves/timberwolves-news-donte-divincenzo-doctor-optimistic-injury-return-this-season)); *ESPN est.* 2 Apr.
- Lively, Raynaud, Harris and Nurkic: see the notes under *Injured and available, back soon*.

## Our injured players

- **Paul George** (BOS): Out, Illness; ESPN est. back 15 Nov.
- **Caleb Wilson** (CHI): Day-To-Day, Right Hip Soreness; ESPN est. back 11 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Day-To-Day, Knee Tendinitis; ESPN est. back 11 Nov.
- **Scottie Barnes** (TOR): Out, Left Groin Soreness; ESPN est. back 12 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Paul George:** out 11 Nov at TOR (illness); "his next opportunity to play will come Sunday" ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-paul-george-out-wednesday/)). *ESPN est.* 15 Nov.
- **Caleb Wilson:** questionable 11 Nov, right hip soreness, a late addition ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-caleb-wilson-late-addition-to-injury-report/)). *ESPN est.* 11 Nov.
- **Jalen Duren:** "at least two more weeks" as of 9 Nov ([Yardbarker](https://www.yardbarker.com/nba/articles/final_injury_report_for_wizards_pistons_will_anthony_davis_isaiah_joe_play/s1_17615_44539104)); re-evaluated about 22 Nov ([Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)). *ESPN est.* 24 Nov.
- **Trey Murphy III:** doubtful 11 Nov (bilateral patellar tendinopathy), "at least one more game" ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/trey-murphy-knee-now-doubtful-vs-brooklyn)); no timetable reported. *ESPN est.* 11 Nov is too early.
- **Scottie Barnes:** out 11 Nov, left groin strain, no timetable reported ([TSN, 11 Nov](https://www.tsn.ca/nba/article/shorthanded-raptors-look-to-turn-fortunes-around-against-celtics-on-tsn/)). *ESPN est.* 12 Nov.
- **Kawhi Leonard:** reconditioning, an update in a week, about 17 Nov ([Yardbarker, 10 Nov](https://www.yardbarker.com/nba/articles/raptors_announce_kawhi_leonard_will_miss_more_time_as_he_recovers_from_left_knee_injury/s1_16751_44544586)); no return date. *ESPN est.* 23 Nov.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |
| Brandon Williams | Left Hamstring | 22 Nov | 22.2 | 18.8 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Stephen Curry | PG | 1 | 33.0 | +3.7 | 1 | **54.0** | 50.9 | 50.0 (3) | 54.0 (7) | 49.2 (9) | Lauri Birds | 100% |
| Charles Bassey | C | 1 | 23.0 | +11.9 | 0 | **33.0** | 19.1 | 26.3 (3) | 19.8 (8) | 20.7 (9) | Free agent | 1% |
| Will Richard (day to day, ESPN est. back 11 Nov) | SG/SF | 1 | 28.0 | +12.6 | 1 | **14.0** | 10.8 | 14.5 (2) | 10.6 (7) | 12.4 (10) | Free agent | 0% |
| De'Anthony Melton | PG/SG | 1 | 28.0 | +6.3 | 0 | **14.0** | 28.0 | 19.3 (3) | 23.6 (8) | 24.6 (11) | Free agent | 8% |
| Gary Payton II (out, ESPN est. back 13 Nov) | SG | 1 | 20.0 | +8.0 | 0 | **5.0** | 10.6 | 12.0 (2) | 11.3 (7) | 9.9 (10) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Waivers |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |
| Jusuf Nurkic | Right Foot Strain | 20 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 3 | 35.7 | +5.7 | 3 | **30.0** | 28.9 | 25.2 (4) | 28.5 (8) | 29.7 (11) | Dr White Slong | 61% |
| Jaxson Hayes | C | 3 | 27.7 | +5.0 | 3 | **27.0** | 24.8 | 22.2 (4) | 24.0 (7) | 27.5 (10) | Snow Time Lakers | 15% |
| Isaiah Collier | PG | 3 | 21.3 | +7.0 | 0 | **18.3** | 14.7 | 13.2 (4) | 15.0 (8) | 15.3 (11) | Free agent | 5% |
| Josh Okogie | SF | 3 | 22.0 | +3.0 | 1 | **14.0** | 10.5 | 12.8 (4) | 12.0 (8) | 10.6 (10) | Free agent | 0% |
| Josh Green | SG | 3 | 27.3 | +12.0 | 3 | **12.7** | 6.7 | 11.0 (4) | 9.5 (8) | 8.7 (9) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 8 | 23.1 | +9.6 | 2 | **30.5** | 10.0 | 34.2 (4) | 30.5 (8) | 25.4 (11) | Free agent | 25% |
| Jared McCain | PG/SG | 8 | 27.8 | +8.2 | 5 | **25.4** | 0.0 | 32.2 (4) | 25.4 (8) | 21.8 (11) | Free agent | 36% |
| Bennett Stirtz | PG | 8 | 23.0 | +16.5 | 0 | **19.8** | 3.0 | 26.2 (4) | 19.8 (8) | 14.7 (11) | Free agent | 3% |
| Kenrich Williams | SF | 8 | 22.9 | +16.4 | 8 | **16.6** | 6.5 | 15.2 (4) | 16.6 (8) | 14.0 (11) | Free agent | 1% |
| Jaylin Williams (out, ESPN est. back 11 Nov) | PF/C | 4 | 23.0 | +13.0 | 1 | **10.8** | 7.0 | — | 10.8 (4) | 9.1 (7) | Free agent | 2% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Chris Youngblood (out) | SG | 3 | 18.3 | +9.7 | 0 | **16.7** | 4.3 | 12.5 (4) | 10.5 (6) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | +5.0 | 0 | **12.0** | -2.0 | — | — | — | — | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 7 | 34.3 | +9.0 | 7 | **43.9** | 25.0 | 39.7 (3) | 39.9 (8) | 37.3 (11) | Cream Abdul-Yammar | 81% |
| LaMelo Ball | PG | 7 | 29.4 | +5.8 | 7 | **37.4** | 27.0 | 38.7 (3) | 34.1 (8) | 35.0 (11) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 7 | 14.7 | +5.4 | 0 | **24.1** | 10.3 | 19.3 (3) | 21.6 (8) | 18.6 (11) | Free agent | 2% |
| Trey Lyles | PF | 7 | 21.0 | +6.3 | 0 | **18.6** | 14.7 | 24.7 (3) | 17.2 (8) | 15.8 (11) | Free agent | 0% |
| Jaylen Clark | SG | 7 | 18.6 | +14.6 | 0 | **15.1** | 5.5 | 16.0 (3) | 15.1 (7) | 11.8 (10) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Moussa Diabate (right quadriceps; ESPN est. 12 Nov), Grant Williams (right hamstring; ESPN est. 12 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ryan Kalkbrenner | C | 2 | 28.0 | +10.9 | 2 | **30.0** | 18.9 | 25.7 (3) | 19.8 (8) | 21.5 (11) | Free agent | 2% |
| Royce O'Neale | SF/PF | 2 | 24.5 | +6.4 | 0 | **22.5** | 9.4 | 18.0 (3) | 13.5 (8) | 12.9 (11) | Free agent | 1% |
| Tidjane Salaun | PF | 2 | 20.5 | +6.6 | 0 | **19.5** | 13.4 | 17.3 (3) | 13.8 (8) | 14.6 (10) | Free agent | 0% |
| Hannes Steinbach | PF | 2 | 20.0 | +12.3 | 0 | **18.0** | 4.7 | 18.0 (2) | 9.2 (4) | 10.0 (5) | Free agent | 1% |
| Liam McNeeley | SF | 2 | 17.5 | +9.5 | 0 | **14.5** | 0.7 | 14.5 (2) | 8.0 (4) | 5.2 (6) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 13 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 28.7 | +6.7 | 10 | **30.7** | 20.0 | 21.7 (3) | 25.0 (7) | 30.5 (10) | Waivers | 39% |
| Derrick Jones Jr. | SF/PF | 9 | 29.2 | +3.8 | 9 | **27.6** | 21.1 | 27.0 (3) | 27.0 (6) | 27.6 (9) | Free agent | 11% |
| Kobe Sanders | SG | 10 | 24.3 | — | 2 | **20.4** | — | 13.0 (3) → 20.0 (2) | 21.4 (7) → 25.2 (6) | 20.4 (10) → 22.8 (9) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 7 | 35.1 | +4.8 | 7 | **39.4** | 29.0 | 41.8 (4) | 38.1 (8) | 35.4 (11) | Snow Time Lakers | 74% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 22.3 | — | 1 | **24.1** | — | 25.3 (3) | 26.2 (8) | 24.3 (11) | Free agent | 5% |
| Jarace Walker | SF/PF | 10 | 22.7 | +4.1 | 2 | **19.1** | 16.5 | 13.7 (3) | 22.0 (8) | 17.9 (11) | Free agent | 1% |
| Jay Huff | C | 9 | 18.3 | — | 5 | **15.9** | — | 8.5 (2) | 14.6 (7) | 15.9 (9) | Free agent | 1% |
| Jalen Slawson | SF | 9 | 14.9 | — | 1 | **14.2** | — | 11.0 (2) | 13.9 (7) | 14.2 (9) | Free agent | 0% |
| Braden Smith | PG | 8 | 13.2 | — | 4 | **12.6** | — | 13.3 (3) | 12.6 (8) | 12.6 (8) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 8 | 38.0 | +7.0 | 8 | **46.2** | 30.0 | 59.0 (3) | 45.9 (7) | 43.0 (10) | Cream Abdul-Yammar | 93% |
| Wendell Carter Jr. | C | 8 | 34.2 | +4.2 | 8 | **32.9** | 46.5 | 47.3 (3) | 33.7 (7) | 35.6 (10) | Dr White Slong | 61% |
| Desmond Bane | SG/SF | 7 | 36.0 | +6.0 | 7 | **30.7** | 13.0 | 18.5 (2) | 29.7 (6) | 26.8 (9) → 30.2 (8) | Cream Abdul-Yammar | 90% |
| Jamal Cain (day to day, ESPN est. back 11 Nov) | SF | 8 | 21.2 | +8.8 | 2 | **15.4** | -5.0 | 19.0 (3) | 16.1 (7) | 11.3 (10) | Free agent | 1% |
| Jase Richardson | SG | 8 | 23.8 | +9.8 | 7 | **15.1** | 14.5 | 15.7 (3) | 16.7 (7) | 15.0 (10) | Free agent | 1% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Immanuel Quickley (day to day, ESPN est. back 11 Nov) | PG/SG | 6 | 32.8 | +4.3 | 6 | **35.2** | 35.0 | 34.0 (1) | 36.4 (5) | 35.1 (8) → 37.7 (7) | Cream Abdul-Yammar | 76% |
| RJ Barrett | SG/SF | 8 | 34.1 | +4.1 | 8 | **33.6** | 39.0 | 27.3 (3) | 34.1 (7) | 34.7 (10) | Dr White Slong | 82% |
| Jamal Shead | PG | 8 | 25.2 | +5.2 | 2 | **29.9** | 11.0 | 39.0 (3) | 32.4 (7) | 26.1 (10) | Lauri Birds | 16% |
| Ja'Kobe Walter | SG | 8 | 31.1 | +7.6 | 8 | **24.0** | 28.0 | 13.0 (3) | 20.6 (7) | 24.8 (10) | Free agent | 11% |
| Collin Murray-Boyles (day to day, ESPN est. back 11 Nov) | PF | 7 | 23.1 | +4.1 | 3 | **24.0** | 25.0 | 36.0 (2) | 25.7 (6) | 24.4 (9) | Free agent | 13% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Duncan Robinson | SG/SF | 8 | 31.6 | +3.6 | 8 | **33.4** | 29.5 | 30.7 (3) | 33.6 (7) | 32.6 (10) | Team Nic Kerr | 60% |
| Paul Reed | PF/C | 8 | 27.1 | +5.6 | 7 | **31.8** | 33.5 | 24.3 (3) | 32.4 (7) | 31.7 (10) | Lauri Birds | 37% |
| Daniss Jenkins | PG | 8 | 27.8 | +9.2 | 2 | **29.9** | 21.0 | 40.0 (3) | 27.9 (7) | 28.1 (10) | Free agent | 16% |
| Kevin Huerter | SG/SF | 8 | 24.1 | +5.1 | 0 | **25.0** | 13.0 | 37.0 (3) | 26.0 (7) | 22.5 (10) | Free agent | 3% |
| Ronald Holland II | SF/PF | 8 | 16.2 | +3.8 | 0 | **15.5** | 16.0 | 7.7 (3) | 13.9 (7) | 15.6 (10) | Free agent | 1% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tobias Harris | Left Calf Strain | 19 Nov | 30.5 | 28.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

No teammate has gained 3+ minutes in those games.

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Scotty Pippen Jr. | Back Soreness | 21 Nov | 25.1 | 14.2 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Javon Small | PG | 3 | 21.7 | — | 0 | **17.0** | — | 18.5 (2) | 17.0 (3) | 17.0 (3) | Free agent | 0% |
| Kris Murray | PF | 5 | 13.8 | +5.8 | 0 | **9.0** | 5.0 | 5.7 (3) | 7.7 (6) | 7.9 (7) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 18.0 | — | 0 | **26.7** | — | 38.0 (1) | 28.8 (4) | 26.7 (6) | Free agent | 1% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 15 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.5 | +6.9 | 10 | **45.0** | 30.4 | 49.2 (4) | 47.0 (8) | 41.4 (11) → 44.6 (10) | Team Nic Kerr | 89% |
| Dylan Cardwell | C | 4 | 18.8 | — | 1 | **21.8** | — | 21.8 (4) | 21.8 (4) | 21.8 (4) | Free agent | 1% |
| De'Andre Hunter | SF/PF | 9 | 32.8 | +5.2 | 9 | **20.8** | 23.9 | 18.3 (3) | 23.1 (7) | 19.5 (10) | Free agent | 6% |
| Leaky Black | SF | 7 | 19.0 | — | 1 | **19.1** | — | 20.8 (4) | 22.3 (6) | 19.1 (7) | Free agent | 1% |
| Jonathan Mogbo | PF | 4 | 15.8 | +3.2 | 0 | **13.8** | 11.3 | 0.0 (1) | 12.3 (3) | 10.6 (5) | Free agent | 0% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 9 | 34.0 | +6.5 | 9 | **29.0** | 23.1 | 19.3 (3) | 29.9 (7) | 29.0 (9) | Free agent | 36% |
| Trevon Brazile | SF/PF | 9 | 20.3 | — | 1 | **19.1** | — | 13.7 (3) | 17.1 (7) | 19.1 (9) | Free agent | 2% |
| Spencer Jones | SF/PF | 2 | 17.5 | — | 0 | **16.5** | — | 16.5 (2) | 16.5 (2) | 16.5 (2) | Free agent | 1% |
| Bryce Hopkins | SF | 7 | 14.3 | — | 2 | **9.0** | — | 12.3 (3) | 11.0 (5) | 9.0 (7) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.8 | +5.5 | 0 | **27.6** | 19.2 | 32.0 (4) | 26.4 (9) | 28.2 (12) | Free agent | 39% |
| Jock Landale | C | 6 | 14.0 | — | 0 | **12.8** | — | 17.0 (1) | 15.8 (5) → 19.8 (4) | 16.5 (8) → 18.9 (7) | Free agent | 0% |

## Every injury

All 97 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 324 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 324 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 232 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 142 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 142 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 111 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 111 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 111 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 111 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 106 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 84 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 62 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 54 | Waivers |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 52 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 52 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 52 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 52 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 52 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 40 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 33 | Matt Wright's Foxies |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 31 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 22 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 22 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 20 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 20 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 20 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 18 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 18 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 14 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 13 | **us** |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 12 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 11 | Dr White Slong |
| Brandon Williams | GS | Out | Left Hamstring | 22 Nov | 11 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 21 Nov | 10 | Free agent |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 9 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 9 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 19 Nov | 8 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 7 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 7 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 7 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 17 Nov | 6 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 17 Nov | 6 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 16 Nov | 5 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 16 Nov | 5 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 16 Nov | 5 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 16 Nov | 5 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 16 Nov | 5 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 15 Nov | 4 | Free agent |
| Quentin Grimes | LAL | Out | Finger | 15 Nov | 4 | Free agent |
| Paul George | BOS | Out | Illness | 15 Nov | 4 | **us** |
| Nate Bittle | TOR | Out | Right Foot Fracture | 15 Nov | 4 | — |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 15 Nov | 4 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 15 Nov | 4 | Free agent |
| Mikel Brown Jr. | BKN | Out | Illness | 14 Nov | 3 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 13 Nov | 2 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 2 | Lauri Birds |
| Trendon Watford | NO | Out | Right Ankle Sprain | 13 Nov | 2 | Free agent |
| Tobe Awaka | CHI | Out | Back | 13 Nov | 2 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 13 Nov | 2 | Free agent |
| Quinten Post | MEM | Out | Head | 13 Nov | 2 | Free agent |
| Precious Achiuwa | SAC | Day-To-Day | Left Lower Leg Bruise | 13 Nov | 2 | Waivers |
| Myles Turner | MIL | Out | Rest | 13 Nov | 2 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 13 Nov | 2 | — |
| Gary Payton II | GS | Out | Left Knee Inflammation | 13 Nov | 2 | Free agent |
| Cam Christie | LAC | Day-To-Day | Ankle | 13 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 13 Nov | 2 | Melbourne poopoo |
| Bennedict Mathurin | NO | Out | Right Thumb Sprain | 13 Nov | 2 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 13 Nov | 2 | Free agent |
| Trayce Jackson-Davis | TOR | Out | Illness | 12 Nov | 1 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 1 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 12 Nov | 1 | Free agent |
| Scottie Barnes | TOR | Out | Left Groin Soreness | 12 Nov | 1 | **us** |
| Moussa Diabate | CHA | Day-To-Day | Right Quadriceps | 12 Nov | 1 | Team Nic Kerr |
| Morez Johnson Jr. | DAL | Day-To-Day | Leg | 12 Nov | 1 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 12 Nov | 1 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 1 | Free agent |
| Brandon Miller | CHA | Day-To-Day | Right Groin Soreness | 12 Nov | 1 | Matt Wright's Foxies |
| Adem Bona | PHI | Out | Back Sprain | 12 Nov | 1 | Free agent |
| Zach Collins | CHI | Day-To-Day | Illness | 11 Nov | 0 | Free agent |
| Will Richard | GS | Day-To-Day | Left Thumb | 11 Nov | 0 | Free agent |
| Tyler Herro | MIL | Day-To-Day | Right Knee Bruise | 11 Nov | 0 | Snow Time Lakers |
| Tristan da Silva | ORL | Day-To-Day | Left Calf Strain | 11 Nov | 0 | Free agent |
| Trey Murphy III | NO | Day-To-Day | Knee Tendinitis | 11 Nov | 0 | **us** |
| T.J. McConnell | IND | Day-To-Day | Hamstring | 11 Nov | 0 | Free agent |
| Norman Powell | CHI | Day-To-Day | Right Shoulder Inflammation | 11 Nov | 0 | Free agent |
| Nolan Traore | BKN | Day-To-Day | Right Calf Soreness | 11 Nov | 0 | Free agent |
| Keyonte George | UTAH | Day-To-Day | Right Ankle Sprain | 11 Nov | 0 | Cream Abdul-Yammar |
| Karl-Anthony Towns | NY | Day-To-Day | Left Calf Soreness | 11 Nov | 0 | Melbourne poopoo |
| Josh Hart | NY | Out | Illness | 11 Nov | 0 | Dr White Slong |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 11 Nov | 0 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 11 Nov | 0 | Free agent |
| Jamal Cain | ORL | Day-To-Day | Left Shoulder Bruise | 11 Nov | 0 | Free agent |
| Isaiah Stewart | MEM | Day-To-Day | Right Knee Bruise | 11 Nov | 0 | Free agent |
| Immanuel Quickley | TOR | Day-To-Day | Right Hamstring | 11 Nov | 0 | Cream Abdul-Yammar |
| Devin Vassell | SA | Day-To-Day | Left Groin | 11 Nov | 0 | Free agent |
| Collin Murray-Boyles | TOR | Day-To-Day | Illness | 11 Nov | 0 | Free agent |
| Caleb Wilson | CHI | Day-To-Day | Right Hip Soreness | 11 Nov | 0 | **us** |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-11 21:12 UTC.
