# Injury Watch: 13 Nov 2026

- Generated 2026-11-13 04:38 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 102 players in ESPN's injury feed. 34 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (09 Nov–15 Nov) / next week (16 Nov–22 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

Our pickups for this week are set: Vassell or Mara on 15 Nov (see the matchup report). For later weeks, the openings that last:
- **Aday Mara** (OKC): Holmgren is out 8–10 weeks from 30 Oct, and Jaylin Williams has back spasms with no timetable reported. His L7 32.5 (4) and L15 29.6 (8) come on starter-level minutes.
- **Jared McCain** (OKC): same openings.
- **Christian Braun** (DEN): Strawther's re-evaluation is about 25 Nov.
- **Daniss Jenkins** is ours now; Kalkbrenner's opening has closed.

The add/drop call is yours, or the council's (`/council`).

## Since the last Injury Watch (12 Nov)

- **Pickups joined:** Grayson Allen, Sion James, Joan Beringer.
- **Kalkbrenner:** his opening closed when Diabaté returned.
- **Back soon, joined:** Zach Edey (rest), Pelle Larsson (illness), T.J. McConnell.
- **Back soon, left:** Ryan Rollins.
- **ESPN estimates moved:**
  - Ingram: 13 → 19 Nov.
  - Gueye: 20 Nov → 12 Dec.
  - Caleb Wilson: out to 13 Dec (dropped by us).

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Daniel Gafford 29.1 (L7 24.0), Daniss Jenkins 29.3 (L7 52.0), Dejounte Murray 30.6 (L7 14.5), Trey Murphy III 31.0 (L7 38.5), Isaiah Hartenstein 31.5 (L7 35.0). A pickup at or above **31.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 10 | 28.7 | +6.7 | **30.7** | 30.5 | 20.0 (2) | 25.0 (7) | 30.5 (10) | Waivers | 36% | 2 / 3 |
| **Grayson Allen** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 30.0 | +3.0 | **30.0** | 26.9 | 30.0 (3) | 27.8 (8) | 26.9 (12) | Free agent | 30% | 1 / 2 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 9 | 24.1 | +10.1 | **29.9** | 25.3 | 32.5 (4) | 29.6 (8) | 25.3 (12) | Free agent | 24% | 2 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 10 | 34.3 | +6.8 | **29.5** | 29.5 | 22.0 (3) | 31.1 (7) | 29.5 (10) | Free agent | 36% | 1 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 18.3 | — | **28.2** | 26.0 | 30.0 (2) | 27.5 (4) | 26.0 (7) | Free agent | 4% | 1 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (12 Dec) | 10 | 25.8 | +5.5 | **27.6** | 28.2 | 32.0 (3) | 26.5 (8) | 28.2 (12) | Free agent | 39% | 2 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 9 | 29.2 | +3.8 | **27.6** | 27.6 | 21.0 (2) | 27.0 (6) | 27.6 (9) | Free agent | 10% | 2 / 3 |
| **Ryan Kalkbrenner** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 24.0 | +7.1 | **25.3** | 21.0 | 25.3 (3) | 19.9 (8) | 21.0 (12) | Free agent | 4% | 1 / 2 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 9 | 28.1 | +7.1 | **24.4** | 21.4 | 35.0 (4) | 23.1 (8) | 21.4 (12) | Free agent | 36% | 2 / 3 |
| **Kevin Huerter** | DET | Jalen Duren (24 Nov) | 9 | 24.1 | +4.1 | **23.7** | 21.6 | 36.0 (3) | 25.4 (7) | 21.6 (11) | Free agent | 8% | 1 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 10 | 31.6 | +10.0 | **23.3** | 24.1 | 18.0 (4) | 20.6 (9) | 24.1 (12) | Free agent | 14% | 1 / 3 |
| **Dylan Cardwell** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 4 | 18.8 | — | **21.8** | 21.8 | 22.7 (3) | 21.8 (4) | 21.8 (4) | Free agent | 1% | 2 / 3 |
| **Sion James** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 28.7 | +3.4 | **21.3** | 15.7 | 21.3 (3) | 18.8 (8) | 15.7 (12) | Free agent | 2% | 1 / 2 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 4 | 25.0 | +3.8 | **21.0** | 19.2 | 21.0 (4) | 18.6 (8) | 19.2 (11) | Free agent | 1% | 1 / 4 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 9 | 32.8 | +5.2 | **20.8** | 19.5 | 20.0 (2) | 19.3 (6) | 19.5 (10) | Free agent | 5% | 2 / 3 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 8 | 18.0 | +3.0 | **20.6** | 20.6 | 17.7 (3) | 20.8 (8) | 20.6 (12) | Free agent | 1% | 1 / 4 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 10 | 24.3 | — | **20.4** | 20.0 | 18.0 (2) | 20.9 (7) → 24.5 (6) | 20.0 (10) → 22.3 (9) | Free agent | 1% | 2 / 3 |

### Notes

Earlier notes still hold ([20261112-injury-watch.md](20261112-injury-watch.md), [20261111-injury-watch.md](20261111-injury-watch.md)). New from the 12 Nov games:

- **Grayson Allen** (CHA): third straight start, 34 min and 29 FP in the loss at PHX ([ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909979)). His "without" rate rests on 3 games.
  - Brandon Miller "should return to action during this road trip" (15, 17 and 20 Nov; [Last Word on Basketball, 12 Nov](https://lastwordonsports.com/basketball/2026/11/12/hornets-injury-update/)); *ESPN est.* 15 Nov. His return cuts Allen's and **Sion James's** minutes.
  - Schröder is re-evaluated about 22 Nov and Knueppel about 6 Dec ([Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html)).
- **Joan Beringer** (MIN, new): 22 min and 33 FP off the bench in a 39-point rout, one game and noise. He is Gobert's backup ([NBC Sports, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/joan-beringer-nose-available-sunday-vs-utah)). Edwards is out up to two months ([NBA.com, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)); *ESPN est.* 21 Dec.
- **Ryan Kalkbrenner** (CHA): his opening has closed. Diabaté was cleared and started for 32 min, and Kalkbrenner went to the bench for 16 min ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/moussa-diabate-quad-good-to-go-thursday); [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/ryan-kalkbrenner-news-shifting-to-bench-538850)).
- **Kris Dunn, Derrick Jones Jr. and Kobe Sanders** (LAC): Ingram is ruled out 13 Nov, "close to a return", no timetable reported ([Field Level Media, 12 Nov](https://www.thesportsleader.com/2026/11/12/thunders-visit-to-clippers-inspires-injury-flashbacks/)); *ESPN est.* 19 Nov, moved from 13 Nov.
- **Aaron Wiggins** (ATL): Gueye is doing on-court work, re-evaluated in four weeks, about 10 Dec ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/mouhamed-gueye-foot-out-at-least-four-more-weeks)); *ESPN est.* 12 Dec.
- **Kevin Huerter** (DET): 24 min, 13 FP off the bench in double overtime. Isaiah Joe still out ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/isaiah-joe-hip-remains-out-thursday-vs-was)); *ESPN est.* 17 Nov.

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 13 Nov | 1 | 41.5 | — | — | 41.5 (2) → 68.0 (1) | 24.7 | 22.5 | Free agent | 14% | 2 / 4 |
| **Zach Edey** | MEM | Left Ankle | 14 Nov | 2 | 22.8 | 16.3 (3) | 21.1 (7) | 22.8 (10) | 33.2 | 39.5 | Free agent | 44% | 2 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 8 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 4 |
| **Norman Powell** | CHI | Right Shoulder Inflammation | 13 Nov | 1 | 26.2 | — | 21.8 (4) → 27.7 (3) | 26.2 (8) → 29.4 (7) | 36.0 | 33.0 | Free agent | 74% | 2 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 13 Nov | 1 | 26.3 | — | — | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 1 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 21 Nov | 9 | 14.2 | — | 3.0 (1) | 14.2 (5) | 30.6 | 27.1 | Free agent | 9% | 2 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 7 | — | — | — | — | 30.1 | 28.0 | Free agent | 42% | 2 / 3 |
| **Collin Sexton** | LAL | Head | 15 Nov | 3 | 17.7 | 17.8 (4) | 19.1 (9) | 17.7 (12) | 28.8 | 26.6 | Free agent | 21% | 1 / 3 |
| **Devin Vassell** | SA | Left Groin | 13 Nov | 1 | 28.3 | 37.0 (2) | 29.7 (6) | 28.3 (10) | 26.8 | 27.3 | Free agent | 37% | 2 / 3 |
| **Quentin Grimes** | LAL | Finger | 15 Nov | 3 | 16.6 | 14.0 (2) | 16.3 (7) | 16.6 (11) | 28.1 | 25.8 | Free agent | 26% | 1 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 3 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 3 |
| **Precious Achiuwa** | SAC | Left Ankle Soreness | 13 Nov | 1 | 28.0 | 20.7 (3) | 27.9 (7) | 28.0 (11) → 30.5 (10) | 24.1 | 27.0 | Waivers | 20% | 2 / 3 |
| **Bennedict Mathurin** | NO | Right Thumb Sprain | 13 Nov | 1 | 9.8 | 5.3 (3) | 7.8 (8) | 9.8 (11) | 25.1 | 27.6 | Free agent | 7% | 2 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 6 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 2 / 3 |
| **Nolan Traore** | BKN | Right Calf Soreness | 14 Nov | 2 | 26.6 | 33.0 (2) | 32.7 (6) | 26.6 (10) → 29.2 (9) | 21.6 | 17.5 | Free agent | 12% | 1 / 3 |
| **Tristan da Silva** | ORL | Left Calf Strain | 13 Nov | 1 | 25.9 | 26.5 (2) | 25.8 (6) | 25.9 (9) | 17.2 | 21.2 | Free agent | 9% | 1 / 4 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 13 Nov | 1 | 15.3 | 15.3 (3) | 15.3 (3) | 15.3 (3) | 24.4 | 25.5 | Free agent | 8% | 2 / 3 |
| **Pelle Larsson** | MIA | Illness | 13 Nov | 1 | 25.1 | 27.3 (3) | 26.0 (7) | 25.1 (11) | — | 23.7 | Free agent | 11% | 2 / 3 |

### Notes

- **New:**
  - **Zach Edey** (MEM): out 13 Nov for "left ankle injury management", a planned rest ([CBS/RotoWire, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-ruled-out-for-friday/)); *ESPN est.* 14 Nov.
  - **Pelle Larsson** (MIA): illness, questionable 13 Nov ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/klay-thompson-pelle-larsson-miss-practice-thurs)); *ESPN est.* 13 Nov.
- **T.J. McConnell:** probable 13 Nov, still on a minutes limit ([RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/tj-mcconnell-injury-probable-for-friday-538834)).
- **Ryan Rollins:** off the report for 13 Nov ([RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/ryan-rollins-news-fades-injury-report-538826)).
- **Yves Missi** and our **Trey Murphy III:** both doubtful 13 Nov ([NBC Sports, 12 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-12/trey-murphy-yves-missi-doubtful-friday-vs-mem)). No timetable reported; *ESPN est.* 13 Nov. Our overrides: Missi floor 18 Nov, Murphy sits 13 Nov.
- **Maxime Raynaud:** "progressing", no timetable ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)); floor 16 Nov.
- **Devin Vassell:** questionable 13 Nov ([RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/devin-vassell-injury-questionable-for-friday-538833)).
- **Nolan Traore:** nothing new; *ESPN est.* 14 Nov.

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 3 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 6 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 2 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 19 Nov | 7 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 2 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 7 | 30.1 (30.5) | 28.0 (63) | Free agent | 42% | 2 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 8 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 17 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 2 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 51 | 38.8 (32.4) | 41.6 (38) | Free agent | 28% | 1 / 4 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 51 | 36.9 (27.7) | 32.3 (32) | Free agent | 33% | 1 / 4 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 83 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 1 / 3 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 110 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 1 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 141 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 4 |

## Our injured players

- **Paul George** (BOS): Day-To-Day, Illness; ESPN est. back 15 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Day-To-Day, Knee Tendinitis; ESPN est. back 13 Nov.
- **Scottie Barnes** (TOR): Out, Left Groin Soreness; ESPN est. back 15 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Paul George:** back 15 Nov ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/paul-george-injury-out-wednesday-538595)); *ESPN est.* 15 Nov.
- **Trey Murphy III:** doubtful 13 Nov ([RotoWire via CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-doubtful-for-friday-538808/)); no timetable reported; *ESPN est.* 13 Nov.
- **Scottie Barnes:** out 12 Nov, his fourth straight game ([TSN, 12 Nov](https://www.tsn.ca/nba/article/raptors-barnes-set-to-miss-fourth-straight-game-against-76ers-with-groin-injury/)); no timetable reported; *ESPN est.* 15 Nov.
- **Kawhi Leonard:** update due about 17 Nov; *ESPN est.* 23 Nov.
- **Jalen Duren** (IR): re-evaluated about 22 Nov; *ESPN est.* 24 Nov.
- **Caleb Wilson** (dropped 12 Nov): hand surgery, 4–6 weeks ([ESPN, 12 Nov](https://www.espn.com/nba/story/_/id/50464091/sources-bulls-wilson-surgery-hand-4-6-weeks)); *ESPN est.* 13 Dec.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |
| Brandon Williams | Left Hamstring | 22 Nov | 22.2 | 18.8 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection. Split on Jimmy Butler III alone: the others still played in those games.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 10 | 31.9 | +3.3 | 10 | **42.6** | 33.7 | 44.8 (4) | 39.1 (8) → 45.0 (7) | 41.4 (12) → 45.4 (11) | **us** | 95% |
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 8 | 16.9 | — | 1 | **19.1** | — | 15.0 (3) | 17.3 (6) | 18.8 (10) | Free agent | 1% |
| Georges Niang | PF | 10 | 21.1 | — | 2 | **17.1** | — | 19.5 (4) | 19.6 (8) | 16.4 (12) | Free agent | 1% |
| Will Richard | SG/SF | 9 | 18.6 | — | 3 | **12.6** | — | 15.0 (3) | 12.7 (7) | 12.7 (11) | Free agent | 0% |
| Gary Payton II | SG | 8 | 13.1 | — | 0 | **10.2** | — | 12.0 (2) | 10.8 (6) | 9.9 (10) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Waivers |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |
| Jusuf Nurkic | Right Foot Strain | 20 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 4 | 34.5 | +3.2 | 4 | **34.5** | 31.7 | 32.5 (4) | 27.5 (8) | 31.2 (12) | Dr White Slong | 63% |
| Jaxson Hayes | C | 4 | 28.2 | +6.2 | 4 | **26.8** | 22.2 | 26.5 (4) | 24.2 (8) | 27.4 (11) | Snow Time Lakers | 14% |
| Brice Sensabaugh | SG/SF | 4 | 17.0 | +3.5 | 0 | **20.2** | 12.0 | 14.5 (4) | 15.1 (8) | 14.6 (12) | Free agent | 1% |
| Isaiah Collier | PG | 4 | 19.0 | +5.3 | 0 | **16.8** | 13.7 | 16.2 (4) | 13.5 (8) | 15.0 (12) | Free agent | 3% |
| Kyle Filipowski | PF/C | 2 | 15.0 | +9.2 | 0 | **12.5** | 2.5 | 8.3 (3) | 8.2 (5) | 5.0 (8) | Free agent | 3% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 9 | 24.1 | +10.1 | 3 | **29.9** | 7.0 | 32.5 (4) | 29.6 (8) | 25.3 (12) | Free agent | 24% |
| Jared McCain | PG/SG | 9 | 28.1 | +7.1 | 6 | **24.4** | 2.0 | 35.0 (4) | 23.1 (8) | 21.4 (12) | Free agent | 36% |
| Bennett Stirtz | PG | 9 | 23.2 | +12.2 | 0 | **19.8** | 7.0 | 22.8 (4) | 21.6 (8) | 15.2 (12) | Free agent | 2% |
| Kenrich Williams | SF | 9 | 23.2 | +16.2 | 8 | **16.8** | 6.0 | 14.0 (4) | 16.9 (8) | 14.3 (12) | Free agent | 1% |
| Jaylin Williams (out, ESPN est. back 15 Nov) | PF/C | 4 | 23.0 | +18.0 | 1 | **10.8** | -1.0 | — | 7.3 (3) | 9.1 (7) | Free agent | 1% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 4 | 25.0 | +3.8 | 2 | **21.0** | 18.8 | 21.0 (4) | 18.6 (8) | 19.2 (11) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 16 Nov) | SG | 3 | 18.3 | +9.7 | 0 | **16.7** | 4.3 | 16.7 (3) | 10.5 (6) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | — | 0 | **12.0** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 22 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard | PG/SG | 7 | 33.9 | +3.9 | 7 | **37.3** | 25.0 | 36.0 (3) | 37.0 (7) | 35.3 (10) | Matt Wright's Foxies | 73% |
| Ivica Zubac | C | 4 | 24.2 | +17.2 | 4 | **26.8** | 6.0 | 35.3 (3) | 26.8 (4) | 26.1 (7) → 29.5 (6) | Lauri Birds | 72% |
| Aaron Nesmith (day to day, ESPN est. back 13 Nov) | SG/SF | 7 | 27.3 | +7.3 | 7 | **18.4** | 20.0 | 12.0 (3) | 18.3 (7) | 17.7 (10) | Free agent | 3% |
| Jalen Slawson | SF | 7 | 17.0 | +11.5 | 1 | **15.0** | 2.5 | 12.5 (2) | 15.0 (7) | 13.9 (10) | Free agent | 0% |
| Braden Smith | PG | 7 | 15.1 | +15.1 | 4 | **14.4** | 0.0 | 4.0 (2) | 14.4 (7) | 12.6 (8) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 8 | 33.4 | +8.9 | 8 | **42.2** | 11.0 | 36.3 (3) | 42.2 (8) | 36.8 (12) | Cream Abdul-Yammar | 82% |
| LaMelo Ball | PG | 8 | 28.9 | +4.9 | 8 | **39.1** | 26.0 | 42.3 (3) | 39.1 (8) | 36.3 (12) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 8 | 15.8 | +5.8 | 0 | **28.2** | 12.5 | 27.3 (3) | 28.2 (8) | 21.8 (12) | Free agent | 3% |
| Joan Beringer | C | 8 | 18.0 | +3.0 | 1 | **20.6** | 26.5 | 17.7 (3) | 20.8 (8) | 20.6 (12) | Free agent | 1% |
| Trey Lyles | PF | 8 | 20.2 | +6.8 | 0 | **16.6** | 11.5 | 21.0 (3) | 16.6 (8) | 14.8 (12) | Free agent | 1% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Grayson Allen | PG/SG | 3 | 30.0 | +3.0 | 3 | **30.0** | 26.3 | 30.0 (3) | 27.8 (8) | 26.9 (12) | Free agent | 30% |
| Ryan Kalkbrenner | C | 3 | 24.0 | +7.1 | 2 | **25.3** | 17.7 | 25.3 (3) | 19.9 (8) | 21.0 (12) | Free agent | 4% |
| Sion James | SF | 3 | 28.7 | +3.4 | 2 | **21.3** | 15.4 | 21.3 (3) | 18.8 (8) | 15.7 (12) | Free agent | 2% |
| Hannes Steinbach | PF | 2 | 20.0 | +14.5 | 0 | **18.0** | 0.5 | 18.0 (2) | 9.2 (4) | 10.0 (5) | Free agent | 1% |
| Royce O'Neale | SF/PF | 3 | 23.7 | +5.4 | 0 | **17.7** | 9.0 | 17.7 (3) | 14.4 (8) | 12.5 (12) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 19 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 28.7 | +6.7 | 10 | **30.7** | 20.0 | 20.0 (2) | 25.0 (7) | 30.5 (10) | Waivers | 36% |
| Derrick Jones Jr. | SF/PF | 9 | 29.2 | +3.8 | 9 | **27.6** | 21.1 | 21.0 (2) | 27.0 (6) | 27.6 (9) | Free agent | 10% |
| Kobe Sanders | SG | 10 | 24.3 | — | 2 | **20.4** | — | 18.0 (2) | 20.9 (7) → 24.5 (6) | 20.0 (10) → 22.3 (9) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 9 | 34.6 | +5.6 | 9 | **37.8** | 29.0 | 37.6 (5) | 37.3 (9) | 34.8 (13) | Snow Time Lakers | 76% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 9 | 38.1 | +5.1 | 9 | **46.8** | 25.0 | 57.0 (4) | 46.5 (8) | 43.7 (11) | Cream Abdul-Yammar | 93% |
| Desmond Bane | SG/SF | 8 | 35.8 | +8.8 | 8 | **32.2** | -1.0 | 26.7 (3) | 31.6 (7) | 28.4 (10) → 31.7 (9) | Cream Abdul-Yammar | 90% |
| Wendell Carter Jr. | C | 9 | 33.6 | +4.6 | 9 | **31.6** | 47.0 | 40.8 (4) | 32.1 (8) | 34.3 (11) | Dr White Slong | 61% |
| Jase Richardson | SG | 9 | 23.3 | +9.3 | 7 | **15.4** | 12.0 | 16.2 (4) | 16.9 (8) | 15.3 (11) | Free agent | 0% |
| Jamal Cain (day to day, ESPN est. back 13 Nov) | SF | 8 | 21.2 | +10.2 | 2 | **15.4** | -3.0 | 19.0 (3) | 16.1 (7) | 11.3 (10) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 10 | 34.1 | +3.3 | 10 | **36.8** | 32.6 | 37.2 (4) | 37.6 (9) | 37.2 (12) | Dr White Slong | 83% |
| Ja'Kobe Walter | SG | 10 | 31.6 | +10.0 | 10 | **23.3** | 17.6 | 18.0 (4) | 20.6 (9) | 24.1 (12) | Free agent | 14% |
| Alijah Martin | SG | 9 | 14.3 | — | 0 | **17.0** | — | 26.5 (4) | 18.4 (8) | 13.8 (11) | Free agent | 0% |
| Jamison Battle | SF | 10 | 20.9 | — | 0 | **16.1** | — | 20.0 (4) | 17.0 (9) | 16.2 (12) | Free agent | 1% |
| Allen Graves | SF | 10 | 13.8 | — | 0 | **11.7** | — | 10.0 (4) | 8.7 (9) | 13.0 (12) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Waivers |

Last 10 games: 0 game(s) without them, 10 with them.

No game yet without them. Same-position teammates by current minutes: Norman Powell (SG/SF, 28.9 min, 26.2 FP/g, Free agent), Matas Buzelis (SF/PF, 26.3 min, 20.4 FP/g, Free agent), Isaac Okoro (SG/SF, 19.1 min, 10.2 FP/g, Free agent), Leonard Miller (SF, 15.9 min, 14.2 FP/g, Free agent).

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cade Cunningham | PG | 9 | 35.1 | +5.1 | 9 | **53.3** | 39.0 | 55.7 (3) | 54.9 (7) | 50.7 (11) | **us** | 100% |
| Ausar Thompson | SF/PF | 8 | 29.4 | +10.4 | 8 | **36.8** | 18.0 | 42.7 (3) | 38.4 (7) | 34.8 (10) | Lauri Birds | 77% |
| Duncan Robinson | SG/SF | 9 | 32.7 | +4.7 | 9 | **31.8** | 31.0 | 22.0 (3) | 33.7 (7) | 31.4 (11) | Team Nic Kerr | 62% |
| Daniss Jenkins | PG | 9 | 29.3 | +7.3 | 3 | **31.1** | 31.0 | 52.0 (3) | 31.9 (7) | 29.3 (11) | **us** | 30% |
| Kevin Huerter | SG/SF | 9 | 24.1 | +4.1 | 0 | **23.7** | 17.0 | 36.0 (3) | 25.4 (7) | 21.6 (11) | Free agent | 8% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Scotty Pippen Jr. | Back Soreness | 21 Nov | 25.1 | 14.2 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Javon Small | PG | 4 | 20.0 | — | 0 | **16.2** | — | 17.0 (3) | 16.2 (4) | 16.2 (4) | Free agent | 0% |
| Kris Murray | PF | 5 | 13.8 | +5.8 | 0 | **9.0** | 5.0 | 2.5 (2) | 7.7 (6) | 7.9 (7) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 18.3 | — | 0 | **28.2** | — | 30.0 (2) | 27.5 (4) | 26.0 (7) | Free agent | 4% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 15 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.5 | +6.9 | 10 | **45.0** | 30.4 | 50.3 (3) | 50.1 (7) | 41.4 (11) → 44.6 (10) | Team Nic Kerr | 90% |
| Dylan Cardwell | C | 4 | 18.8 | — | 1 | **21.8** | — | 22.7 (3) | 21.8 (4) | 21.8 (4) | Free agent | 1% |
| De'Andre Hunter | SF/PF | 9 | 32.8 | +5.2 | 9 | **20.8** | 23.9 | 20.0 (2) | 19.3 (6) | 19.5 (10) | Free agent | 5% |
| Leaky Black | SF | 7 | 19.0 | — | 1 | **19.1** | — | 23.0 (3) | 24.4 (5) | 19.1 (7) | Free agent | 0% |
| Jonathan Mogbo | PF | 4 | 15.8 | +3.2 | 0 | **13.8** | 11.3 | 0.0 (1) | 14.0 (2) | 10.6 (5) | Free agent | 0% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 34.3 | +6.8 | 10 | **29.5** | 23.1 | 22.0 (3) | 31.1 (7) | 29.5 (10) | Free agent | 36% |
| Trevon Brazile | SF/PF | 10 | 19.6 | — | 1 | **19.1** | — | 13.0 (3) | 18.6 (7) | 19.1 (10) | Free agent | 2% |
| Spencer Jones | SF/PF | 3 | 19.0 | — | 0 | **13.3** | — | 13.3 (3) | 13.3 (3) | 13.3 (3) | Free agent | 1% |
| Bryce Hopkins | SF | 7 | 14.3 | — | 2 | **9.0** | — | 3.0 (2) | 8.5 (4) | 9.0 (7) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.8 | +5.5 | 0 | **27.6** | 19.2 | 32.0 (3) | 26.5 (8) | 28.2 (12) | Free agent | 39% |
| Jock Landale | C | 6 | 14.0 | — | 0 | **12.8** | — | 17.0 (1) | 13.0 (4) → 17.3 (3) | 16.5 (8) → 18.9 (7) | Free agent | 0% |

## Every injury

All 102 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 323 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 323 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 231 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 141 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 141 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 110 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 110 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 110 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 110 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 105 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 83 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 61 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 53 | Waivers |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 51 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 51 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 51 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 51 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 51 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 39 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 32 | Matt Wright's Foxies |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 31 | Waivers |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 30 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 30 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 30 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 21 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 21 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 19 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 19 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 19 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 17 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 17 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 13 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 12 | **us** |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 11 | **us** |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 22 Nov | 10 | Lauri Birds |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 10 | Dr White Slong |
| Brandon Williams | GS | Out | Left Hamstring | 22 Nov | 10 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 21 Nov | 9 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 20 Nov | 8 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 20 Nov | 8 | — |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 8 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 20 Nov | 8 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 19 Nov | 7 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 19 Nov | 7 | Melbourne poopoo |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 18 Nov | 6 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 18 Nov | 6 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 6 | Free agent |
| Marcus Smart | HOU | Suspension | Suspension | 18 Nov | 6 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 6 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 6 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 18 Nov | 6 | Free agent |
| Adem Bona | PHI | Out | Back Sprain | 18 Nov | 6 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 17 Nov | 5 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 17 Nov | 5 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 16 Nov | 4 | Free agent |
| Trey Alexander | UTAH | Out | Right Ankle Sprain | 16 Nov | 4 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 16 Nov | 4 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 16 Nov | 4 | Free agent |
| Chris Youngblood | POR | Out | Right Foot Bruise | 16 Nov | 4 | Free agent |
| Trayce Jackson-Davis | TOR | Day-To-Day | Illness | 15 Nov | 3 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 15 Nov | 3 | Free agent |
| Scottie Barnes | TOR | Out | Left Groin Soreness | 15 Nov | 3 | **us** |
| Quentin Grimes | LAL | Day-To-Day | Finger | 15 Nov | 3 | Free agent |
| Paul George | BOS | Day-To-Day | Illness | 15 Nov | 3 | **us** |
| Nate Bittle | TOR | Out | Right Foot Fracture | 15 Nov | 3 | — |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 15 Nov | 3 | Free agent |
| Luka Doncic | LAL | Day-To-Day | Right Ankle | 15 Nov | 3 | Team Nic Kerr |
| LeBron James | PHI | Day-To-Day | Back | 15 Nov | 3 | Cream Abdul-Yammar |
| Jaylin Williams | OKC | Out | Back Spasms | 15 Nov | 3 | Free agent |
| Collin Sexton | LAL | Day-To-Day | Head | 15 Nov | 3 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 15 Nov | 3 | Free agent |
| Bub Carrington | WSH | Day-To-Day | Chest | 15 Nov | 3 | Free agent |
| Brandon Miller | CHA | Out | Right Groin Soreness | 15 Nov | 3 | Matt Wright's Foxies |
| Austin Reaves | LAL | Day-To-Day | Left Heel | 15 Nov | 3 | Cream Abdul-Yammar |
| Zach Edey | MEM | Out | Left Ankle | 14 Nov | 2 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 14 Nov | 2 | Free agent |
| Tobe Awaka | CHI | Out | Back | 14 Nov | 2 | Free agent |
| Quinten Post | MEM | Out | Concussion | 14 Nov | 2 | Free agent |
| Nolan Traore | BKN | Day-To-Day | Right Calf Soreness | 14 Nov | 2 | Free agent |
| Mikel Brown Jr. | BKN | Day-To-Day | Illness | 14 Nov | 2 | Free agent |
| Evan Mobley | CLE | Out | Toe | 14 Nov | 2 | Matt Wright's Foxies |
| Yves Missi | NO | Out | Left Knee Bruise | 13 Nov | 1 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 13 Nov | 1 | Free agent |
| Tristan da Silva | ORL | Day-To-Day | Left Calf Strain | 13 Nov | 1 | Free agent |
| Trey Murphy III | NO | Day-To-Day | Knee Tendinitis | 13 Nov | 1 | **us** |
| T.J. McConnell | IND | Day-To-Day | Right Hamstring Strain | 13 Nov | 1 | Free agent |
| Precious Achiuwa | SAC | Day-To-Day | Left Ankle Soreness | 13 Nov | 1 | Waivers |
| Pelle Larsson | MIA | Day-To-Day | Illness | 13 Nov | 1 | Free agent |
| Norman Powell | CHI | Day-To-Day | Right Shoulder Inflammation | 13 Nov | 1 | Free agent |
| Klay Thompson | MIA | Day-To-Day | Left Ankle Soreness | 13 Nov | 1 | Melbourne poopoo |
| Kingston Flemings | ATL | Day-To-Day | Back | 13 Nov | 1 | Free agent |
| Jamal Cain | ORL | Day-To-Day | Left Shoulder Bruise | 13 Nov | 1 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 13 Nov | 1 | Free agent |
| Giannis Antetokounmpo | MIA | Day-To-Day | Wrist | 13 Nov | 1 | Dr White Slong |
| Devin Vassell | SA | Day-To-Day | Left Groin | 13 Nov | 1 | Free agent |
| De'Aaron Fox | SA | Day-To-Day | Left Hip Soreness | 13 Nov | 1 | Matt Wright's Foxies |
| Dailyn Swain | CHI | Day-To-Day | Right Back | 13 Nov | 1 | Free agent |
| Charles Bassey | GS | Day-To-Day | Left Toe Soreness | 13 Nov | 1 | Free agent |
| Bryce McGowens | NO | Day-To-Day | Left Elbow Infection | 13 Nov | 1 | Free agent |
| Bennedict Mathurin | NO | Day-To-Day | Right Thumb Sprain | 13 Nov | 1 | Free agent |
| Ajay Mitchell | OKC | Day-To-Day | Left Ankle Sprain | 13 Nov | 1 | Lauri Birds |
| Aaron Nesmith | IND | Day-To-Day | Right Knee Soreness | 13 Nov | 1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-13 04:38 UTC.
- [ESPN box](https://www.espn.com/nba/boxscore/_/gameId/401909979)
- [Last Word on Basketball, 12 Nov](https://lastwordonsports.com/basketball/2026/11/12/hornets-injury-update/)
- [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html)
- [NBC Sports, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/joan-beringer-nose-available-sunday-vs-utah)
- [NBA.com, 29 Oct](https://www.nba.com/news/reports-anthony-edwards-to-undergo-arthroscopic-procedure-on-right-knee-miss-up-to-two-months)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/moussa-diabate-quad-good-to-go-thursday)
- [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/ryan-kalkbrenner-news-shifting-to-bench-538850)
- [Field Level Media, 12 Nov](https://www.thesportsleader.com/2026/11/12/thunders-visit-to-clippers-inspires-injury-flashbacks/)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/mouhamed-gueye-foot-out-at-least-four-more-weeks)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/isaiah-joe-hip-remains-out-thursday-vs-was)
- [CBS/RotoWire, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-ruled-out-for-friday/)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/klay-thompson-pelle-larsson-miss-practice-thurs)
- [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/tj-mcconnell-injury-probable-for-friday-538834)
- [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/ryan-rollins-news-fades-injury-report-538826)
- [NBC Sports, 12 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-12/trey-murphy-yves-missi-doubtful-friday-vs-mem)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)
- [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/devin-vassell-injury-questionable-for-friday-538833)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/paul-george-injury-out-wednesday-538595)
- [RotoWire via CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-doubtful-for-friday-538808/)
- [TSN, 12 Nov](https://www.tsn.ca/nba/article/raptors-barnes-set-to-miss-fourth-straight-game-against-76ers-with-groin-injury/)
- [ESPN, 12 Nov](https://www.espn.com/nba/story/_/id/50464091/sources-bulls-wilson-surgery-hand-4-6-weeks)
