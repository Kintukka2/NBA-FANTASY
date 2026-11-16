# Injury Watch: 16 Nov 2026

- Generated 2026-11-16 04:42 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 102 players in ESPN's injury feed. 30 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 17 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (09 Nov–15 Nov) / next week (16 Nov–22 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Daniss Jenkins 28.7 (L7 44.5), Saddiq Bey 29.4 (L7 29.2), Trey Murphy III 31.0 (L7 44.0), Isaiah Hartenstein 32.7 (L7 40.5), Jalen Duren 33.5 (L7 —). A pickup at or above **33.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Gary Trent Jr.** | MIL | Ousmane Dieng (14 Dec) | 1 | 30.0 | +22.2 | **35.0** | 10.2 | 12.8 (4) | 11.6 (5) | 10.2 (6) | Free agent | 0% | 0 / 3 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 3 | 31.0 | +8.6 | **34.7** | 21.8 | 22.2 (5) | 25.2 (9) | 21.8 (14) | Free agent | 7% | 0 / 3 |
| **Brandon Williams** (out, ESPN est. back 22 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +10.7 | **33.0** | 18.8 | 5.0 (1) | 19.5 (4) | 18.8 (10) | Free agent | 1% | 0 / 4 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 24.4 | — | **30.5** | 26.6 | 32.0 (4) | 32.3 (9) | 26.6 (14) | Free agent | 23% | 0 / 3 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 2 | 22.5 | +10.0 | **30.0** | 16.1 | 30.0 (2) | 23.0 (4) | 16.1 (10) | Free agent | 1% | 0 / 4 |
| **Duncan Robinson** (day to day, ESPN est. back 17 Nov) | DET | Jalen Duren (24 Nov) | 10 | 31.1 | +4.9 | **29.9** | 29.8 | 19.8 (4) | 29.5 (6) | 29.8 (12) | Free agent | 56% | 0 / 4 |
| **Mo Bamba** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (20 Nov) | 6 | 20.7 | +6.0 | **29.8** | 29.6 | 32.0 (5) | 28.9 (8) | 29.6 (10) | Free agent | 5% | 0 / 4 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 9 | 28.6 | +3.2 | **28.0** | 28.7 | 27.5 (4) | 27.0 (6) | 28.7 (11) | Free agent | 14% | 0 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 20.2 | — | **27.8** | 26.5 | 30.0 (3) | 25.8 (4) | 26.5 (8) | Free agent | 3% | 0 / 3 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 3 | 19.3 | +5.0 | **27.3** | 17.7 | 21.8 (4) | 15.8 (8) | 17.7 (13) | Free agent | 1% | 0 / 3 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 10 | 26.4 | +4.4 | **26.8** | 28.1 | 18.0 (4) | 24.9 (7) | 28.1 (12) | Free agent | 33% | 0 / 3 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan); also out: Tyrese Haliburton (22 Nov) | 10 | 23.2 | — | **26.4** | 23.8 | 25.0 (4) | 26.1 (8) | 23.8 (14) | Free agent | 4% | 0 / 3 |
| **Collin Murray-Boyles** | TOR | Kawhi Leonard (23 Nov) | 9 | 26.1 | +3.2 | **26.0** | 25.2 | 27.3 (3) | 28.4 (7) | 25.2 (12) | Free agent | 14% | 0 / 3 |
| **De'Andre Hunter** (out, ESPN est. back 18 Nov) | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (18 Nov) | 8 | 35.4 | +7.8 | **25.6** | 21.6 | 27.7 (3) | 21.5 (6) | 21.6 (11) | Free agent | 8% | 0 / 3 |
| **Ryan Kalkbrenner** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 4 | 22.5 | +6.7 | **24.5** | 21.1 | 30.0 (3) | 22.9 (7) | 21.1 (13) | Free agent | 2% | 0 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 2 | 36.0 | +17.9 | **24.5** | 12.6 | 18.5 (4) | 14.3 (6) | 12.6 (12) | Free agent | 0% | 0 / 4 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (18 Nov) | 8 | 21.8 | — | **23.6** | 21.0 | 21.5 (4) | 25.3 (7) | 21.0 (9) | Free agent | 0% | 0 / 3 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 2 | 20.0 | +8.5 | **23.0** | 20.4 | 24.7 (3) | 25.6 (7) | 20.4 (11) | Free agent | 1% | 0 / 4 |
| **Sion James** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 4 | 30.2 | +5.1 | **20.2** | 15.8 | 21.0 (3) | 18.9 (7) | 15.8 (13) | Free agent | 1% | 0 / 2 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Zach Edey** | MEM | Left Ankle | 16 Nov | 1 | 22.8 | 14.0 (2) | 20.2 (6) | 22.8 (10) | 33.2 | 39.5 | Free agent | 41% | 0 / 4 |
| **Dejounte Murray** | NO | Ankle | 20 Nov | 5 | 30.6 | 13.7 (3) | 20.8 (5) | 30.6 (9) | 39.0 | 36.5 | Free agent | 81% | 0 / 4 |
| **Ryan Rollins** | MIL | Illness | 18 Nov | 3 | 23.3 | 24.0 (4) | 23.0 (8) | 23.3 (13) | 31.9 | 37.5 | Free agent | 49% | 0 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 5 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 0 / 4 |
| **Santi Aldama** | DAL | Left Ankle Sprain | 18 Nov | 3 | 14.8 | 14.0 (4) | 14.8 (5) | 14.8 (5) | 25.0 | 32.4 | Free agent | 6% | 0 / 3 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 21 Nov | 6 | 14.2 | — | — | 14.2 (5) | 30.6 | 27.1 | Free agent | 9% | 0 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 4 | — | — | — | — | 30.1 | 28.0 | Free agent | 42% | 0 / 3 |
| **Duncan Robinson** | DET | Left Thigh Soreness | 17 Nov | 2 | 29.8 | 19.8 (4) | 29.5 (6) | 29.8 (12) | 21.6 | 23.1 | Free agent | 56% | 0 / 4 |
| **Peyton Watson** | CLE | Right Abdomen Soreness | 16 Nov | 1 | 24.9 | 16.0 (3) | 23.3 (6) | 24.9 (11) | 29.3 | 29.8 | Waivers | 40% | 0 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 16 Nov | 1 | 19.2 | 20.3 (3) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 3% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 18 Nov | 3 | — | — | — | — | — | 28.1 | Free agent | 2% | 0 / 3 |
| **Precious Achiuwa** | SAC | Left Ankle Soreness | 18 Nov | 3 | 28.0 | 20.0 (2) | 22.7 (6) | 28.0 (11) → 30.5 (10) | 24.1 | 27.0 | Free agent | 17% | 0 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 18 Nov | 3 | 8.8 | 3.7 (3) | 5.0 (7) | 8.8 (12) | 25.1 | 27.6 | Free agent | 7% | 0 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 3 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 0 / 3 |
| **Jaxson Hayes** | UTAH | Left Knee Strain | 17 Nov | 2 | 27.2 | 25.8 (4) | 23.8 (8) | 27.2 (12) | 16.5 | 20.2 | Free agent | 11% | 0 / 4 |
| **Jock Landale** | ATL | Right Hip Inflammation | 18 Nov | 3 | 16.8 | 18.0 (2) | 12.0 (3) → 18.0 (2) | 16.8 (9) → 18.9 (8) | — | 25.8 | Free agent | 0% | 0 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 14 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 0 / 3 |
| **Isaiah Stewart** | MEM | Illness | 16 Nov | 1 | 21.6 | 18.7 (3) | 22.8 (6) | 21.6 (10) | 25.3 | 25.1 | Free agent | 4% | 0 / 4 |
| **Pelle Larsson** | MIA | Illness | 16 Nov | 1 | 25.1 | 28.0 (2) | 21.8 (5) | 25.1 (11) | — | 23.7 | Free agent | 9% | 0 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 33.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 3 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 18 Nov | 3 | — (—) | 28.1 (74) | Free agent | 2% | 0 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 19 Nov | 4 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 0 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 4 | 30.1 (30.5) | 28.0 (63) | Free agent | 42% | 0 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 5 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 0 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 14 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 0 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 48 | 38.8 (32.4) | 41.6 (38) | Free agent | 28% | 0 / 4 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 48 | 36.9 (27.7) | 32.3 (32) | Free agent | 32% | 0 / 4 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 80 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 0 / 3 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 107 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 0 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 138 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 0 / 4 |

## Our injured players

- **Jalen Smith** (CHI): Day-To-Day, Left Finger Sprain; ESPN est. back 16 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Out, Knee Tendinitis; ESPN est. back 18 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 1 | 25.0 | +10.7 | 0 | **33.0** | 13.8 | 5.0 (1) | 19.5 (4) | 18.8 (10) | Free agent | 1% |
| Charles Bassey | C | 2 | 20.0 | +8.5 | 1 | **23.0** | 18.8 | 24.7 (3) | 25.6 (7) | 20.4 (11) | Free agent | 1% |
| LJ Cryer | PG | 2 | 13.0 | +5.8 | 0 | **20.5** | 8.0 | 25.3 (3) | 12.3 (6) | 10.8 (10) | Waivers | 0% |
| Will Richard | SG/SF | 2 | 26.0 | +9.7 | 1 | **10.5** | 11.6 | 14.0 (2) | 13.3 (6) | 12.7 (12) | Free agent | 0% |
| 4897449 |  | 1 | 14.0 | +10.0 | 0 | **7.0** | 3.0 | — | — | — | — | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 24.4 | — | 4 | **30.5** | — | 32.0 (4) | 32.3 (9) | 26.6 (14) | Free agent | 23% |
| Kenrich Williams | SF | 10 | 23.9 | +8.5 | 9 | **19.8** | 14.2 | 21.5 (4) | 20.9 (9) | 16.8 (14) | Free agent | 1% |
| Bennett Stirtz | PG | 10 | 21.3 | — | 0 | **19.2** | — | 14.2 (4) | 19.4 (9) | 14.2 (14) | Free agent | 1% |
| Micah Peavy | SF | 9 | 16.4 | — | 0 | **10.1** | — | 6.0 (3) | 11.4 (8) | 10.1 (9) | Free agent | 0% |
| Nikola Topic | PG | 2 | 14.5 | — | 0 | **8.5** | — | 8.5 (2) | 8.5 (2) | 8.5 (2) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 5 | 25.2 | +5.0 | 3 | **18.2** | 15.8 | 20.3 (3) | 17.4 (8) | 18.2 (12) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 17 Nov) | SG | 3 | 18.3 | +9.7 | 0 | **16.7** | 4.3 | 14.0 (1) | 10.5 (6) | 10.5 (6) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 9 | 33.3 | +7.3 | 9 | **42.0** | 12.0 | 36.0 (3) | 43.1 (7) | 37.0 (13) | Cream Abdul-Yammar | 83% |
| Bones Hyland | PG | 9 | 16.3 | +11.3 | 0 | **26.9** | 4.0 | 32.7 (3) | 25.9 (7) | 21.4 (13) | Free agent | 6% |
| Trey Lyles | PF | 9 | 20.1 | +7.1 | 0 | **16.1** | 8.0 | 13.0 (3) | 15.1 (7) | 14.5 (13) | Free agent | 0% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 9 | 16.9 | +3.8 | 0 | **14.6** | 9.4 | 12.0 (3) | 14.7 (7) | 11.9 (12) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 10 games: 6 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 20 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 6 | 20.7 | +6.0 | 1 | **29.8** | 23.7 | 32.0 (5) | 28.9 (8) | 29.6 (10) | Free agent | 5% |
| Brice Sensabaugh | SG/SF | 6 | 20.8 | +7.1 | 0 | **18.7** | 10.0 | 17.2 (5) | 14.0 (9) | 14.7 (14) | Free agent | 1% |
| Isaiah Collier | PG | 5 | 18.4 | +6.4 | 0 | **15.4** | 10.2 | 16.2 (4) | 13.2 (8) | 14.6 (13) | Free agent | 3% |
| Josh Green | SG | 6 | 22.8 | +6.8 | 5 | **10.3** | 6.2 | 9.2 (5) | 7.9 (9) | 8.5 (12) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ryan Kalkbrenner | C | 4 | 22.5 | +6.7 | 2 | **24.5** | 16.3 | 30.0 (3) | 22.9 (7) | 21.1 (13) | Free agent | 2% |
| Sion James | SF | 4 | 30.2 | +5.1 | 3 | **20.2** | 16.3 | 21.0 (3) | 18.9 (7) | 15.8 (13) | Free agent | 1% |
| Hannes Steinbach | PF | 2 | 20.0 | +14.5 | 0 | **18.0** | 0.5 | 5.0 (1) | 12.7 (3) | 10.0 (5) | Free agent | 1% |
| Christian Anderson | PG | 4 | 19.2 | +9.1 | 0 | **17.2** | 8.6 | 21.3 (3) | 14.8 (6) | 9.8 (12) | Free agent | 0% |
| Royce O'Neale | SF/PF | 4 | 22.5 | +3.0 | 0 | **16.0** | 10.5 | 13.3 (3) | 14.3 (7) | 12.4 (13) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 19 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Derrick Jones Jr. | SF/PF | 9 | 28.6 | +3.2 | 9 | **28.0** | 21.1 | 27.5 (4) | 27.0 (6) | 28.7 (11) | Free agent | 14% |
| Kris Dunn | PG/SG | 10 | 26.4 | +4.4 | 10 | **26.8** | 20.0 | 18.0 (4) | 24.9 (7) | 28.1 (12) | Free agent | 33% |
| Kobe Sanders | SG | 10 | 24.0 | — | 2 | **19.5** | — | 15.2 (4) | 18.6 (7) | 18.8 (12) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.1 | +4.7 | 10 | **37.2** | 30.2 | 28.2 (4) | 38.9 (8) | 34.6 (14) | Snow Time Lakers | 77% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Tyrese Haliburton (left hamstring strain; ESPN est. 22 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard (day to day, ESPN est. back 18 Nov) | PG/SG | 8 | 33.9 | +3.2 | 8 | **34.1** | 28.2 | 32.3 (3) | 31.5 (6) | 33.2 (11) | Matt Wright's Foxies | 72% |
| Quenton Jackson | PG/SG | 10 | 23.2 | — | 2 | **26.4** | — | 25.0 (4) | 26.1 (8) | 23.8 (14) | Free agent | 4% |
| Jay Huff | C | 9 | 17.0 | — | 4 | **16.1** | — | 17.3 (3) | 15.7 (7) | 16.2 (12) | Free agent | 1% |
| Jalen Slawson | SF | 9 | 15.9 | — | 1 | **15.1** | — | 14.0 (3) | 16.4 (7) | 14.2 (12) | Free agent | 0% |
| Braden Smith | PG | 7 | 15.1 | — | 4 | **14.4** | — | 4.0 (1) | 19.2 (5) | 12.6 (8) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 10 | 34.6 | +3.8 | 10 | **36.1** | 32.6 | 35.2 (4) | 36.8 (8) | 36.1 (13) | Dr White Slong | 84% |
| Collin Murray-Boyles | PF | 9 | 26.1 | +3.2 | 6 | **26.0** | 24.8 | 27.3 (3) | 28.4 (7) | 25.2 (12) | Free agent | 14% |
| Ja'Kobe Walter | SG | 10 | 32.1 | +10.5 | 10 | **19.2** | 17.6 | 15.8 (4) | 17.2 (8) | 22.8 (13) | Free agent | 10% |
| Alijah Martin | SG | 9 | 14.9 | — | 0 | **16.7** | — | 14.5 (4) | 17.5 (8) | 12.9 (12) | Free agent | 0% |
| Jamison Battle | SF | 10 | 20.4 | — | 0 | **15.4** | — | 18.8 (4) | 17.5 (8) | 15.1 (13) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Josh Giddey | PG/SG | 2 | 32.5 | +4.0 | 2 | **47.5** | 32.6 | 41.0 (4) | 37.3 (6) | 31.8 (12) | Cream Abdul-Yammar | 93% |
| Jalen Smith (day to day, ESPN est. back 16 Nov) | PF/C | 1 | 32.0 | +7.5 | 1 | **41.0** | 31.1 | 46.0 (3) | 35.8 (5) → 42.2 (4) | 33.9 (11) → 36.3 (10) | **us** | 35% |
| Buddy Hield | SG/SF | 2 | 22.5 | +10.0 | 0 | **30.0** | 12.7 | 30.0 (2) | 23.0 (4) | 16.1 (10) | Free agent | 1% |
| Leonard Miller | SF | 1 | 17.0 | +3.7 | 0 | **29.0** | 12.7 | 14.5 (2) | 15.0 (4) | 15.7 (10) | Free agent | 0% |
| Isaac Okoro | SG/SF | 2 | 36.0 | +17.9 | 2 | **24.5** | 9.5 | 18.5 (4) | 14.3 (6) | 12.6 (12) | Free agent | 0% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Paul Reed | PF/C | 10 | 27.8 | +14.0 | 7 | **31.1** | 20.4 | 27.8 (4) | 28.7 (6) | 31.2 (12) | Lauri Birds | 34% |
| Daniss Jenkins | PG | 10 | 29.9 | — | 4 | **30.2** | — | 44.5 (4) | 32.3 (6) | 28.7 (12) | **us** | 32% |
| Duncan Robinson (day to day, ESPN est. back 17 Nov) | SG/SF | 10 | 31.1 | +4.9 | 10 | **29.9** | 21.6 | 19.8 (4) | 29.5 (6) | 29.8 (12) | Free agent | 56% |
| Javonte Green | SF | 10 | 17.2 | — | 0 | **12.2** | — | 13.8 (4) | 12.0 (6) | 13.8 (12) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 20.2 | — | 0 | **27.8** | — | 30.0 (3) | 25.8 (4) | 26.5 (8) | Free agent | 3% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 18 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.0 | +6.4 | 10 | **42.7** | 30.4 | 38.0 (4) | 41.9 (8) | 38.6 (13) | Team Nic Kerr | 90% |
| De'Andre Hunter (out, ESPN est. back 18 Nov) | SF/PF | 8 | 35.4 | +7.8 | 8 | **25.6** | 23.9 | 27.7 (3) | 21.5 (6) | 21.6 (11) | Free agent | 8% |
| Leaky Black | SF | 8 | 21.8 | — | 1 | **23.6** | — | 21.5 (4) | 25.3 (7) | 21.0 (9) | Free agent | 0% |
| Dylan Cardwell | C | 6 | 17.8 | — | 2 | **20.8** | — | 20.5 (4) | 20.8 (6) | 20.8 (6) | Free agent | 1% |
| Emanuel Sharp | SG | 10 | 18.2 | — | 0 | **10.9** | — | 11.2 (4) | 12.6 (8) | 10.6 (13) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Gary Trent Jr. | SG/SF | 1 | 30.0 | +22.2 | 0 | **35.0** | 5.2 | 12.8 (4) | 11.6 (5) | 10.2 (6) | Free agent | 0% |
| Brayden Burries | SG | 3 | 31.0 | +8.6 | 3 | **34.7** | 20.1 | 22.2 (5) | 25.2 (9) | 21.8 (14) | Free agent | 7% |
| Kasparas Jakucionis | PG | 3 | 19.3 | +5.0 | 0 | **27.3** | 8.8 | 21.8 (4) | 15.8 (8) | 17.7 (13) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 33.8 | +6.3 | 10 | **32.7** | 23.1 | 33.7 (3) | 28.2 (6) | 31.1 (11) | Team Nic Kerr | 40% |
| Trevon Brazile | SF/PF | 10 | 19.4 | — | 1 | **18.2** | — | 10.3 (3) | 14.2 (6) | 17.7 (11) | Free agent | 2% |
| Spencer Jones | SF/PF | 4 | 17.2 | — | 0 | **12.2** | — | 6.3 (3) | 12.2 (4) | 12.2 (4) | Free agent | 1% |
| Bryce Hopkins | SF | 6 | 16.3 | — | 2 | **10.2** | — | 2.0 (1) | 12.3 (3) | 9.0 (7) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.2 | +4.9 | 0 | **24.0** | 19.2 | 16.7 (3) | 22.6 (8) | 26.1 (14) | Lauri Birds | 39% |
| Zuby Ejiofor | PF | 6 | 13.5 | — | 0 | **17.7** | — | 8.0 (2) | 17.7 (6) | 13.6 (8) | Free agent | 0% |
| Jock Landale (out, ESPN est. back 18 Nov) | C | 5 | 13.0 | — | 0 | **14.2** | — | 18.0 (2) | 12.0 (3) → 18.0 (2) | 16.8 (9) → 18.9 (8) | Free agent | 0% |

## Every injury

All 102 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 320 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 320 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 228 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 138 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 138 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 107 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 107 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 107 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 107 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 102 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 80 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 58 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 50 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 48 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 48 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 48 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 48 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 48 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 36 | Melbourne poopoo |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 29 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 29 | Matt Wright's Foxies |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 28 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 27 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 27 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 27 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 18 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 18 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 16 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 16 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 16 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 14 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 14 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 14 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 10 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 9 | **us** |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 8 | — |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 8 | **us** |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 22 Nov | 7 | Lauri Birds |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 7 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 22 Nov | 7 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring | 22 Nov | 7 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 21 Nov | 6 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 20 Nov | 5 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 5 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 20 Nov | 5 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 20 Nov | 5 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 19 Nov | 4 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 19 Nov | 4 | Melbourne poopoo |
| Zach LaVine | SAC | Out | Illness | 18 Nov | 3 | Team Nic Kerr |
| Ty Jerome | MEM | Out | Right Hip Soreness | 18 Nov | 3 | Melbourne poopoo |
| Trey Murphy III | NO | Out | Knee Tendinitis | 18 Nov | 3 | **us** |
| Trendon Watford | NO | Out | Right Ankle Sprain | 18 Nov | 3 | Free agent |
| Tobe Awaka | CHI | Out | Back | 18 Nov | 3 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 18 Nov | 3 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 18 Nov | 3 | Free agent |
| Santi Aldama | DAL | Out | Left Ankle Sprain | 18 Nov | 3 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 18 Nov | 3 | Free agent |
| Ryan Rollins | MIL | Out | Illness | 18 Nov | 3 | Free agent |
| Precious Achiuwa | SAC | Out | Left Ankle Soreness | 18 Nov | 3 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 18 Nov | 3 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 18 Nov | 3 | Free agent |
| Max Christie | DAL | Out | Left Ankle Sprain | 18 Nov | 3 | Free agent |
| Marcus Smart | HOU | Suspension | Suspension | 18 Nov | 3 | Free agent |
| Kyrie Irving | DAL | Out | Left Knee | 18 Nov | 3 | Snow Time Lakers |
| Kingston Flemings | ATL | Out | Back Strain | 18 Nov | 3 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 18 Nov | 3 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 18 Nov | 3 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 18 Nov | 3 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 3 | Free agent |
| GG Jackson | MEM | Out | Left Foot | 18 Nov | 3 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 18 Nov | 3 | Matt Wright's Foxies |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 3 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 18 Nov | 3 | Free agent |
| De'Andre Hunter | SAC | Out | Left Hip Soreness | 18 Nov | 3 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 18 Nov | 3 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 18 Nov | 3 | Free agent |
| Andrew Nembhard | IND | Day-To-Day | Left Hip Soreness | 18 Nov | 3 | Matt Wright's Foxies |
| Adem Bona | PHI | Out | Back Sprain | 18 Nov | 3 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 17 Nov | 2 | Free agent |
| Jaxson Hayes | UTAH | Out | Left Knee Strain | 17 Nov | 2 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 17 Nov | 2 | Free agent |
| Duncan Robinson | DET | Day-To-Day | Left Thigh Soreness | 17 Nov | 2 | Free agent |
| De'Aaron Fox | SA | Out | Left Hip | 17 Nov | 2 | Matt Wright's Foxies |
| Chris Youngblood | POR | Out | Right Foot Bruise | 17 Nov | 2 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 17 Nov | 2 | Cream Abdul-Yammar |
| Zach Edey | MEM | Day-To-Day | Left Ankle | 16 Nov | 1 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 16 Nov | 1 | Free agent |
| Trey Alexander | UTAH | Out | Right Ankle Sprain | 16 Nov | 1 | Free agent |
| Tre Johnson | WSH | Out | Back | 16 Nov | 1 | Free agent |
| Quinten Post | MEM | Out | Concussion | 16 Nov | 1 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Right Abdomen Soreness | 16 Nov | 1 | Waivers |
| Pelle Larsson | MIA | Day-To-Day | Illness | 16 Nov | 1 | Free agent |
| Kevin McCullar Jr. | TOR | Day-To-Day | Illness | 16 Nov | 1 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Right Foot | 16 Nov | 1 | Dr White Slong |
| Jaylon Tyson | CLE | Day-To-Day | Right Ankle | 16 Nov | 1 | Free agent |
| Jalen Smith | CHI | Day-To-Day | Left Finger Sprain | 16 Nov | 1 | **us** |
| Isaiah Stewart | MEM | Day-To-Day | Illness | 16 Nov | 1 | Free agent |
| Gui Santos | GS | Day-To-Day | Right Ankle Inflammation | 16 Nov | 1 | Free agent |
| Fred VanVleet | HOU | Out | Right Knee | 16 Nov | 1 | Snow Time Lakers |
| Clint Capela | HOU | Out | Right Ankle Sprain | 16 Nov | 1 | Free agent |
| Drew Timme | PHX | Day-To-Day | Right Hand | 15 Nov | 0 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 14 Nov | -1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-16 04:42 UTC.
