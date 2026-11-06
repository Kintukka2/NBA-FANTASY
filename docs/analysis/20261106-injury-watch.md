# Injury Watch: 06 Nov 2026

- Generated 2026-11-06 05:40 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 94 players in ESPN's injury feed. 25 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 15 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (02 Nov–08 Nov) / next week (09 Nov–15 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Since the last Injury Watch

Against `docs/analysis/20261105-injury-watch.md` (07:34 UTC Thu 5).

- **Pickups:**
  - **Joined:** Desmond Bane (ORL), now a free agent.
  - **Left:** Aaron Nesmith and Jarace Walker.
- **Our five lowest:** Dillon Brooks (30.1) replaces Fred VanVleet. The floor is still 33.5 (Duren).
- **Jarrett Allen:** our waiver claim, dropping Gafford, processes at 08:00 UTC Fri 6. ESPN still lists him day-to-day, *ESPN est.* 6 Nov.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Trey Murphy III 28.9 (L7 34.3), Isaiah Hartenstein 29.8 (L7 30.0), Dillon Brooks 30.1 (L7 33.5), Daniel Gafford 31.6 (L7 31.0), Jalen Duren 33.5 (L7 23.0). A pickup at or above **33.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (11 Nov) | 7 | 35.0 | +7.5 | **32.7** | 32.7 | 38.3 (3) | 32.7 (7) | 32.7 (7) | Free agent | 41% | 1 / 3 |
| **Desmond Bane** | ORL | Paolo Banchero (22 Nov) | 6 | 36.0 | +6.0 | **32.7** | 27.8 | 31.5 (4) | 27.8 (8) | 27.8 (8) | Waivers | 93% | 1 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (08 Nov) | 7 | 30.0 | +4.6 | **29.4** | 29.4 | 24.0 (3) | 29.4 (7) | 29.4 (7) | Free agent | 10% | 1 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (13 Nov) | 5 | 22.8 | +9.8 | **27.8** | 21.8 | 31.0 (3) | 22.7 (7) | 21.8 (8) | Free agent | 16% | 2 / 4 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 9 | 26.0 | +5.7 | **26.9** | 26.9 | 24.8 (4) | 26.9 (9) | 26.9 (9) | Free agent | 29% | 2 / 3 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 6 | 31.0 | +7.5 | **26.8** | 27.1 | 20.2 (4) | 27.1 (8) | 27.1 (8) | Free agent | 17% | 1 / 4 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan); also out: T.J. McConnell (09 Nov) | 8 | 22.6 | +6.6 | **24.5** | 24.7 | 35.5 (4) | 24.7 (9) | 24.7 (9) | Free agent | 4% | 1 / 4 |
| **Jordan Goodwin** (day to day, ESPN est. back 07 Nov) | PHX | Mark Williams (03 Feb) | 5 | 18.8 | — | **24.4** | 24.4 | 25.0 (2) | 24.4 (5) | 24.4 (5) | Free agent | 1% | 1 / 4 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 5 | 19.8 | +5.1 | **22.4** | 21.6 | 21.8 (4) | 21.6 (9) | 21.6 (9) | Free agent | 2% | 2 / 2 |
| **Dean Wade** | PHI | Dominick Barlow (18 Nov) | 7 | 26.3 | +4.8 | **21.9** | 21.9 | 24.0 (4) | 21.9 (7) | 21.9 (7) | Free agent | 1% | 2 / 3 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (11 Nov) | 7 | 22.1 | — | **21.7** | 21.7 | 20.7 (3) | 21.7 (7) | 21.7 (7) | Free agent | 3% | 1 / 3 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (08 Nov) | 8 | 24.4 | — | **20.5** | 20.5 | 21.8 (4) | 20.5 (8) | 20.5 (8) | Free agent | 1% | 1 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 09 Nov | 3 | 41.5 | 15.0 (1) | 41.5 (2) | 41.5 (2) | 24.7 | 22.5 | Free agent | 15% | 2 / 4 |
| **Jarrett Allen** | CLE | Right Knee | 06 Nov | 0 | 34.0 | 30.2 (4) | 34.0 (8) | 34.0 (8) | 36.9 | 36.9 | Waivers | 90% | 2 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 13 Nov | 7 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 2 / 4 |
| **Kon Knueppel** | CHA | Left Hamstring Strain | 09 Nov | 3 | -2.0 | -2.0 (1) | -2.0 (1) | -2.0 (1) | 35.2 | 34.1 | Waivers | 89% | 1 / 3 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 4 | 26.3 | 23.0 (1) | 26.3 (3) | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 1 / 3 |
| **Nic Claxton** | CHI | Left Hamstring Strain | 08 Nov | 2 | — | — | — | — | 30.3 | 33.3 | Free agent | 42% | 1 / 3 |
| **DeMar DeRozan** | DEN | Back Spasms | 07 Nov | 1 | 18.3 | 13.5 (2) | 18.3 (6) | 18.3 (6) | 29.8 | 32.7 | Free agent | 61% | 1 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 06 Nov | 0 | — | — | — | — | 25.0 | 32.4 | Free agent | 6% | 2 / 4 |
| **Keegan Murray** | SAC | Ankle | 10 Nov | 4 | 12.0 | 18.0 (1) | 12.0 (2) | 12.0 (2) | 29.3 | 31.6 | Free agent | 33% | 2 / 3 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 09 Nov | 3 | 14.2 | 3.0 (1) | 14.2 (5) | 14.2 (5) | 30.6 | 27.1 | Free agent | 10% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 3 | — | — | — | — | 30.1 | 28.0 | Free agent | 44% | 2 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 11 Nov | 5 | 15.0 | 8.0 (1) | 15.0 (4) | 15.0 (4) | 30.0 | 22.2 | Free agent | 30% | 2 / 2 |
| **Peyton Watson** | CLE | Right Hamstring Soreness | 06 Nov | 0 | 27.0 | 19.5 (2) | 27.0 (6) | 27.0 (6) | 29.3 | 29.8 | Free agent | 43% | 2 / 4 |
| **Jalen Smith** | CHI | Left Hand | 08 Nov | 2 | 29.4 | 21.7 (3) | 29.4 (8) | 29.4 (8) | 22.4 | 25.5 | Free agent | 17% | 1 / 3 |
| **Kelly Oubre Jr.** | IND | Left Calf Bruise | 07 Nov | 1 | 18.0 | 18.5 (2) | 18.0 (7) | 18.0 (7) | 23.2 | 28.6 | Free agent | 4% | 1 / 4 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 07 Nov | 1 | 18.6 | 7.0 (1) | 18.6 (5) | 18.6 (5) | 25.6 | 28.3 | Free agent | 2% | 2 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 4 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 6 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 2 / 4 |
| **Sandro Mamukelashvili** | LAL | Illness | 06 Nov | 0 | 22.0 | 18.2 (4) | 22.0 (9) | 22.0 (9) | — | 26.2 | Free agent | 5% | 2 / 3 |
| **Jock Landale** | ATL | Left Hip | 07 Nov | 1 | 16.4 | 10.0 (2) | 16.4 (7) | 16.4 (7) | — | 25.8 | Free agent | 1% | 2 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 09 Nov | 3 | — | — | — | — | 24.4 | 25.5 | Free agent | 8% | 1 / 4 |
| **Isaiah Stewart** | MEM | Right Knee Bruise | 09 Nov | 3 | 22.9 | 27.8 (4) | 22.9 (7) | 22.9 (7) | 25.3 | 25.1 | Free agent | 5% | 1 / 4 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 33.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Santi Aldama** | DAL | Right Knee Surgery | 06 Nov | 0 | 25.0 (23.7) | 32.4 (43) | Free agent | 6% | 2 / 4 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 08 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 1 / 3 |
| **Nic Claxton** | CHI | Left Hamstring Strain | 08 Nov | 2 | 30.3 (27.8) | 33.3 (69) | Free agent | 42% | 1 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 09 Nov | 3 | 24.4 (17.8) | 25.5 (56) | Free agent | 8% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 3 | 30.1 (30.5) | 28.0 (63) | Free agent | 44% | 2 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 4 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 6 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 2 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 13 Nov | 7 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 2 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 23 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 1 / 3 |
| **Kristaps Porzingis** | GS | Illness | 01 Dec | 25 | 36.9 (27.7) | 32.3 (32) | Free agent | 40% | 1 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 57 | 38.8 (32.4) | 41.6 (38) | Free agent | 29% | 1 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 89 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 1 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 116 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 2 / 3 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 147 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 2 / 2 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Trey Murphy III** (NO): Day-To-Day, Knee; ESPN est. back 06 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Left Groin Soreness; ESPN est. back 06 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 8 games: 5 game(s) without them, 3 with them.

Also out in those games, so part of the gain is theirs: Nikola Topic (back; ESPN est. 13 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ajay Mitchell | PG/SG | 5 | 29.2 | +4.5 | 5 | **38.0** | 29.7 | 29.7 (3) | 37.7 (7) | 34.9 (8) | Lauri Birds | 70% |
| Isaiah Hartenstein | C | 5 | 26.2 | +3.9 | 5 | **34.2** | 22.3 | 30.0 (3) | 31.4 (7) | 29.8 (8) | **us** | 46% |
| Aday Mara | C | 5 | 22.8 | +9.8 | 1 | **27.8** | 11.7 | 31.0 (3) | 22.7 (7) | 21.8 (8) | Free agent | 16% |
| Kenrich Williams | SF | 5 | 24.4 | +17.7 | 5 | **19.0** | 7.0 | 23.0 (3) | 15.4 (7) | 14.5 (8) | Free agent | 1% |
| Bennett Stirtz | PG | 5 | 22.6 | +17.9 | 0 | **17.0** | 2.0 | 22.3 (3) | 13.0 (7) | 11.4 (8) | Free agent | 0% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 9 | 31.7 | +3.1 | 9 | **40.6** | 33.7 | 36.5 (4) | 40.6 (9) | 40.6 (9) | **us** | 92% |
| Brandon Williams | PG/SG | 8 | 17.9 | — | 1 | **20.9** | — | 23.7 (3) | 20.9 (8) | 20.9 (8) | Free agent | 4% |
| Georges Niang | PF | 9 | 20.1 | — | 2 | **16.1** | — | 20.8 (4) | 16.1 (9) | 16.1 (9) | Free agent | 1% |
| Will Richard | SG/SF | 9 | 17.7 | — | 3 | **12.9** | — | 13.8 (4) | 12.9 (9) | 12.9 (9) | Free agent | 0% |
| Gary Payton II | SG | 9 | 13.4 | — | 0 | **10.0** | — | 12.2 (4) | 10.0 (9) | 10.0 (9) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 02 Jan | 25.7 | 7.0 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them. Split on Ja Morant alone: the others still played in those games.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Toumani Camara | SF/PF | 3 | 31.3 | +6.3 | 3 | **17.0** | 32.5 | 20.8 (4) | 25.6 (7) | 25.6 (7) | Free agent | 37% |
| Scoot Henderson | PG/SG | 3 | 26.3 | +7.3 | 3 | **15.3** | 6.5 | 13.8 (4) | 10.3 (7) | 10.3 (7) | Free agent | 7% |
| Vit Krejci (out, ESPN est. back 02 Jan) | PG | 3 | 12.7 | +4.4 | 0 | **11.0** | 4.0 | 8.8 (4) | 7.0 (7) | 7.0 (7) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 9 games: 5 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 5 | 34.2 | +8.0 | 5 | **45.8** | 25.8 | 45.5 (4) | 36.9 (9) | 36.9 (9) | Cream Abdul-Yammar | 77% |
| LaMelo Ball | PG | 5 | 28.2 | +3.2 | 5 | **37.2** | 30.8 | 42.5 (4) | 34.3 (9) | 34.3 (9) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 5 | 16.0 | +8.0 | 0 | **28.8** | 9.0 | 30.8 (4) | 20.0 (9) | 20.0 (9) | Free agent | 2% |
| Joan Beringer | C | 5 | 19.8 | +5.1 | 1 | **22.4** | 20.2 | 21.8 (4) | 21.6 (9) | 21.6 (9) | Free agent | 2% |
| Jaylen Clark | SG | 5 | 18.0 | +14.3 | 0 | **16.6** | 4.0 | 19.0 (4) | 11.9 (8) | 11.9 (8) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 08 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 8 | 30.5 | +8.5 | 8 | **33.4** | 20.0 | 30.5 (4) | 33.1 (8) | 33.1 (8) | Dr White Slong | 39% |
| Derrick Jones Jr. | SF/PF | 7 | 30.0 | +4.6 | 7 | **29.4** | 21.1 | 24.0 (3) | 29.4 (7) | 29.4 (7) | Free agent | 10% |
| Kobe Sanders | SG | 8 | 24.4 | — | 2 | **20.5** | — | 21.8 (4) | 20.5 (8) | 20.5 (8) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 8 games: 4 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 4 | 35.5 | +5.5 | 4 | **38.0** | 29.8 | 38.0 (3) | 33.1 (8) | 33.1 (8) | Snow Time Lakers | 57% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 9 games: 8 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: T.J. McConnell (right hamstring strain; ESPN est. 09 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 8 | 22.6 | +6.6 | 1 | **24.5** | 26.0 | 35.5 (4) | 24.7 (9) | 24.7 (9) | Free agent | 4% |
| Jarace Walker | SF/PF | 8 | 24.6 | +5.6 | 2 | **19.9** | 6.0 | 23.8 (4) | 18.3 (9) | 18.3 (9) | Free agent | 2% |
| Jay Huff | C | 8 | 19.4 | — | 5 | **17.9** | — | 19.8 (4) | 17.9 (8) | 17.9 (8) | Free agent | 1% |
| Braden Smith | PG | 6 | 14.0 | — | 2 | **15.5** | — | 22.8 (4) | 15.5 (6) | 15.5 (6) | Free agent | 1% |
| Jalen Slawson | SF | 8 | 15.2 | — | 1 | **14.2** | — | 17.2 (4) | 14.2 (8) | 14.2 (8) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 8 games: 6 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 6 | 37.7 | +6.7 | 6 | **42.0** | 30.0 | 46.0 (4) | 39.0 (8) | 39.0 (8) | Cream Abdul-Yammar | 91% |
| Desmond Bane | SG/SF | 6 | 36.0 | +6.0 | 6 | **32.7** | 13.0 | 31.5 (4) | 27.8 (8) | 27.8 (8) | Waivers | 93% |
| Wendell Carter Jr. | C | 6 | 33.5 | +3.5 | 6 | **30.5** | 46.5 | 34.0 (4) | 34.5 (8) | 34.5 (8) | Dr White Slong | 53% |
| Jase Richardson | SG | 6 | 24.2 | +10.2 | 6 | **17.3** | 14.5 | 21.2 (4) | 16.6 (8) | 16.6 (8) | Free agent | 2% |
| Jamal Cain | SF | 6 | 19.0 | +6.5 | 1 | **11.3** | -5.0 | 11.0 (4) | 7.2 (8) | 7.2 (8) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 8 games: 6 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 6 | 33.3 | +3.3 | 6 | **36.5** | 39.0 | 33.8 (4) | 37.1 (8) | 37.1 (8) | Dr White Slong | 82% |
| Immanuel Quickley | PG/SG | 6 | 32.8 | +4.3 | 6 | **35.2** | 35.0 | 36.0 (4) | 35.1 (8) | 35.1 (8) | Cream Abdul-Yammar | 79% |
| Ja'Kobe Walter | SG | 6 | 31.0 | +7.5 | 6 | **26.8** | 28.0 | 20.2 (4) | 27.1 (8) | 27.1 (8) | Free agent | 17% |
| Jamison Battle | SF | 6 | 18.2 | +6.7 | 0 | **13.5** | 17.0 | 15.0 (4) | 14.4 (8) | 14.4 (8) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 8 games: 4 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 13 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Lauri Markkanen | SF/PF | 3 | 33.0 | +4.5 | 3 | **41.0** | 25.5 | 41.0 (3) | 32.1 (7) | 32.1 (7) | Lauri Birds | 90% |
| Ace Bailey | SF/PF | 4 | 34.0 | +6.8 | 4 | **22.5** | 38.8 | 21.3 (3) | 30.6 (8) | 30.6 (8) | Dr White Slong | 63% |
| Josh Okogie | SF | 4 | 21.8 | +8.8 | 0 | **14.0** | 3.3 | 10.0 (3) | 9.4 (7) | 9.4 (7) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin (day to day, ESPN est. back 07 Nov) | PG/SG | 5 | 18.8 | — | 0 | **24.4** | — | 25.0 (2) | 24.4 (5) | 24.4 (5) | Free agent | 1% |

### PHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dominick Barlow | Back Fracture | 18 Nov | 23.7 | 22.0 | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaylen Brown | SG/SF | 8 | 36.2 | +3.9 | 8 | **41.2** | 38.6 | 47.0 (3) | 40.7 (7) | 41.2 (8) | Snow Time Lakers | 100% |
| Dean Wade | PF | 7 | 26.3 | +4.8 | 4 | **21.9** | 16.3 | 24.0 (4) | 21.9 (7) | 21.9 (7) | Free agent | 1% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 8 | 37.2 | +6.6 | 8 | **38.5** | 30.4 | 50.0 (4) | 38.0 (8) | 38.0 (8) | Team Nic Kerr | 84% |
| De'Andre Hunter | SF/PF | 8 | 31.2 | +3.6 | 8 | **19.5** | 23.9 | 19.0 (4) | 19.4 (8) | 19.4 (8) | Free agent | 7% |
| Dylan Cardwell | C | 1 | 13.0 | — | 0 | **19.0** | — | 19.0 (1) | 19.0 (1) | 19.0 (1) | Free agent | 0% |
| Leaky Black | SF | 4 | 13.8 | — | 0 | **16.2** | — | 26.5 (2) | 16.2 (4) | 16.2 (4) | Free agent | 0% |
| Jonathan Mogbo | PF | 4 | 17.2 | +4.7 | 0 | **13.2** | 11.3 | 28.0 (1) | 13.2 (4) | 13.2 (4) | Free agent | 0% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 11 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 7 | 35.0 | +7.5 | 7 | **32.7** | 23.1 | 38.3 (3) | 32.7 (7) | 32.7 (7) | Free agent | 41% |
| Trevon Brazile | SF/PF | 7 | 22.1 | — | 1 | **21.7** | — | 20.7 (3) | 21.7 (7) | 21.7 (7) | Free agent | 3% |
| Bryce Hopkins | SF | 5 | 18.8 | — | 2 | **11.4** | — | 31.0 (1) | 11.4 (5) | 11.4 (5) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 9 | 26.0 | +5.7 | 0 | **26.9** | 19.2 | 24.8 (4) | 26.9 (9) | 26.9 (9) | Free agent | 29% |
| Jock Landale (out, ESPN est. back 07 Nov) | C | 7 | 15.3 | — | 0 | **16.4** | — | 10.0 (2) | 16.4 (7) | 16.4 (7) | Free agent | 1% |

## Every injury

All 94 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 329 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 329 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 237 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 147 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 147 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 116 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 116 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 116 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 116 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 111 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 89 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 02 Jan | 57 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 57 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 57 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 57 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 57 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 45 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 38 | Matt Wright's Foxies |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 27 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 27 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 25 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 25 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 25 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 23 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 23 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 17 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 16 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 14 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 12 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 12 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 12 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 7 | Lauri Birds |
| Thomas Sorber | OKC | Out | Knee | 13 Nov | 7 | Free agent |
| Nikola Topic | OKC | Out | Back | 13 Nov | 7 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 13 Nov | 7 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 6 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 12 Nov | 6 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 6 | Free agent |
| Spencer Jones | DEN | Out | Hamstring | 11 Nov | 5 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 11 Nov | 5 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 4 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 10 Nov | 4 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 4 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 4 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 09 Nov | 3 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 09 Nov | 3 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 09 Nov | 3 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 09 Nov | 3 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 09 Nov | 3 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 09 Nov | 3 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 09 Nov | 3 | — |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 09 Nov | 3 | Waivers |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 3 | **us** |
| Isaiah Stewart | MEM | Out | Right Knee Bruise | 09 Nov | 3 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 09 Nov | 3 | Free agent |
| Zach Collins | CHI | Day-To-Day | Undisclosed | 08 Nov | 2 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 2 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 08 Nov | 2 | Free agent |
| Nic Claxton | CHI | Out | Left Hamstring Strain | 08 Nov | 2 | Free agent |
| Kam Jones | MIL | Out | Right Ankle | 08 Nov | 2 | Free agent |
| Jalen Smith | CHI | Day-To-Day | Left Hand | 08 Nov | 2 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 08 Nov | 2 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 2 | Melbourne poopoo |
| Rasheer Fleming | PHX | Day-To-Day | Left Ankle Sprain | 07 Nov | 1 | Free agent |
| Noah Clowney | BKN | Day-To-Day | Right Knee Soreness | 07 Nov | 1 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 07 Nov | 1 | — |
| Kelly Oubre Jr. | IND | Day-To-Day | Left Calf Bruise | 07 Nov | 1 | Free agent |
| Josh Hart | NY | Day-To-Day | Ankle | 07 Nov | 1 | Dr White Slong |
| Jordan Goodwin | PHX | Day-To-Day | Left Calf | 07 Nov | 1 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 07 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 07 Nov | 1 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 07 Nov | 1 | Free agent |
| Gui Santos | GS | Out | Knee | 07 Nov | 1 | Free agent |
| DeMar DeRozan | DEN | Day-To-Day | Back Spasms | 07 Nov | 1 | Free agent |
| Clint Capela | HOU | Day-To-Day | Right Ankle Sprain | 07 Nov | 1 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 07 Nov | 1 | Free agent |
| Tyrese Proctor | CLE | Day-To-Day | Left Ankle Sprain | 06 Nov | 0 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 06 Nov | 0 | Free agent |
| Trey Murphy III | NO | Day-To-Day | Knee | 06 Nov | 0 | **us** |
| Terrence Shannon Jr. | MIN | Day-To-Day | Left Hip Bruise | 06 Nov | 0 | Free agent |
| Scottie Barnes | TOR | Day-To-Day | Left Groin Soreness | 06 Nov | 0 | **us** |
| Santi Aldama | DAL | Out | Right Knee Surgery | 06 Nov | 0 | Free agent |
| Sandro Mamukelashvili | LAL | Day-To-Day | Illness | 06 Nov | 0 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Right Hamstring Soreness | 06 Nov | 0 | Free agent |
| Payton Pritchard | BOS | Day-To-Day | Right Eye Abrasion | 06 Nov | 0 | Dr White Slong |
| Moussa Diabate | CHA | Day-To-Day | Quadriceps | 06 Nov | 0 | Team Nic Kerr |
| Max Christie | DAL | Day-To-Day | Right Hip | 06 Nov | 0 | Free agent |
| Jarrett Allen | CLE | Day-To-Day | Right Knee | 06 Nov | 0 | Waivers |
| Jalen Johnson | ATL | Day-To-Day | Left Ankle | 06 Nov | 0 | Snow Time Lakers |
| Dennis Schroder | CHA | Day-To-Day | Thigh | 06 Nov | 0 | Free agent |
| Anthony Davis | WSH | Day-To-Day | Right Ankle Sprain | 06 Nov | 0 | Melbourne poopoo |
| Adem Bona | PHI | Day-To-Day | Back Sprain | 06 Nov | 0 | Free agent |
| Day'Ron Sharpe | BKN | Day-To-Day | Undisclosed | 04 Nov | -2 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-06 05:40 UTC.
