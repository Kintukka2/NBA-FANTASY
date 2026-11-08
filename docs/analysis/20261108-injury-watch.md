# Injury Watch: 08 Nov 2026

- Generated 2026-11-08 05:58 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 88 players in ESPN's injury feed. 26 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 15 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (02 Nov–08 Nov) / next week (09 Nov–15 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Since the last Injury Watch

Against `docs/analysis/20261106-injury-watch.md` (05:40 UTC Fri 6).

- **Pickups:**
  - **Joined:** Spencer Jones, Jamal Shead, Jared McCain, Collin Murray-Boyles, Leaky Black and Jarace Walker.
  - **Left:** Aday Mara (now ours), Joan Beringer and Dean Wade.
  - Desmond Bane is still listed but now out (*ESPN est.* 10 Nov).
- **Our five lowest** are now Mara, Murphy, Hartenstein, Gafford and P.J. Washington. The floor fell from 33.5 to 30.8.
- **Ours:**
  - Scottie Barnes is day-to-day with left groin soreness (*ESPN est.* 9 Nov).
  - Duren (*ESPN est.* 9 Nov) and Kawhi (*ESPN est.* 23 Nov) are unchanged.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Aday Mara 24.4 (L7 32.6), Trey Murphy III 29.4 (L7 34.0), Isaiah Hartenstein 29.6 (L7 29.6), Daniel Gafford 30.1 (L7 24.7), P.J. Washington 30.8 (L7 37.3). A pickup at or above **30.8** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Desmond Bane** (out, ESPN est. back 10 Nov) | ORL | Paolo Banchero (22 Nov) | 6 | 36.0 | +6.0 | **32.7** | 27.8 | 28.0 (3) | 27.9 (7) | 27.8 (8) | Free agent | 91% | 0 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 8 | 34.2 | +6.8 | **30.1** | 30.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 42% | 0 / 3 |
| **Spencer Jones** | DEN | Julian Strawther (29 Nov) | 1 | 21.0 | — | **30.0** | 30.0 | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 0% | 0 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (10 Nov) | 7 | 30.0 | +4.6 | **29.4** | 29.4 | 26.0 (2) | 29.3 (6) | 29.4 (7) | Free agent | 11% | 1 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 10 | 25.7 | +5.4 | **28.8** | 28.7 | 26.2 (5) | 28.8 (10) | 28.7 (11) | Free agent | 34% | 0 / 3 |
| **Jamal Shead** | TOR | Kawhi Leonard (23 Nov) | 7 | 23.7 | +3.7 | **27.3** | 23.7 | 30.8 (4) | 25.6 (8) | 23.7 (9) | Free agent | 3% | 0 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 7 | 30.7 | +7.2 | **25.3** | 25.9 | 18.8 (4) | 25.2 (8) | 25.9 (9) | Free agent | 13% | 0 / 4 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 7 | 27.3 | +7.0 | **24.6** | 20.9 | 25.6 (5) | 21.8 (8) | 20.9 (10) | Free agent | 30% | 0 / 4 |
| **Jordan Goodwin** (out, ESPN est. back 09 Nov) | PHX | Mark Williams (03 Feb) | 5 | 18.8 | — | **24.4** | 24.4 | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% | 0 / 4 |
| **Collin Murray-Boyles** | TOR | Kawhi Leonard (23 Nov) | 7 | 23.1 | +4.1 | **24.0** | 24.4 | 29.2 (4) | 24.0 (8) | 24.4 (9) | Free agent | 11% | 0 / 4 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 22.0 | +6.0 | **23.0** | 23.3 | 27.2 (4) | 23.0 (9) | 23.3 (10) | Free agent | 7% | 0 / 4 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (10 Nov) | 5 | 19.0 | — | **20.6** | 20.6 | 30.3 (3) | 20.6 (5) | 20.6 (5) | Free agent | 0% | 1 / 3 |
| **Jarace Walker** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 24.1 | +5.1 | **20.6** | 19.1 | 22.2 (4) | 20.6 (9) | 19.1 (10) | Free agent | 1% | 0 / 4 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (10 Nov) | 8 | 24.4 | — | **20.5** | 20.5 | 23.0 (3) | 21.3 (7) | 20.5 (8) | Free agent | 1% | 1 / 3 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov) | 8 | 21.1 | — | **20.5** | 20.5 | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% | 0 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 09 Nov | 1 | 41.5 | — | 15.0 (1) | 41.5 (2) | 24.7 | 22.5 | Free agent | 15% | 1 / 4 |
| **Desmond Bane** | ORL | Illness | 10 Nov | 2 | 27.8 | 28.0 (3) | 27.9 (7) | 27.8 (8) | 38.2 | 36.9 | Free agent | 91% | 0 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 12 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 1 / 4 |
| **Kon Knueppel** | CHA | Left Hamstring Strain | 09 Nov | 1 | -2.0 | -2.0 (1) | -2.0 (1) | -2.0 (1) | 35.2 | 34.1 | Free agent | 87% | 0 / 3 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 2 | 26.3 | — | 29.5 (2) | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 0 / 3 |
| **Nic Claxton** | CHI | Left Hamstring Strain | 08 Nov | 0 | — | — | — | — | 30.3 | 33.3 | Free agent | 42% | 1 / 3 |
| **Deandre Ayton** | WSH | Leg | 09 Nov | 1 | 16.9 | 19.0 (4) | 15.8 (9) | 16.9 (10) | 25.3 | 31.6 | Free agent | 10% | 0 / 4 |
| **Keegan Murray** | SAC | Left Ankle | 08 Nov | 0 | 12.0 | — | 18.0 (1) | 12.0 (2) | 29.3 | 31.6 | Free agent | 32% | 1 / 3 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 09 Nov | 1 | 14.2 | — | 11.0 (4) | 14.2 (5) | 30.6 | 27.1 | Free agent | 10% | 0 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 1 | — | — | — | — | 30.1 | 28.0 | Free agent | 44% | 0 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 11 Nov | 3 | 15.0 | — | 18.0 (3) | 15.0 (4) | 30.0 | 22.2 | Free agent | 29% | 1 / 2 |
| **Jalen Smith** | CHI | Left Finger Sprain | 08 Nov | 0 | 29.4 | 20.5 (2) | 29.0 (7) | 29.4 (8) | 22.4 | 25.5 | Free agent | 15% | 1 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 09 Nov | 1 | 18.6 | — | 18.8 (4) | 18.6 (5) | 25.6 | 28.3 | Free agent | 2% | 0 / 4 |
| **Robert Williams III** | POR | Rest | 10 Nov | 2 | 28.1 | 26.0 (4) | 29.5 (6) | 28.1 (7) | 26.9 | 26.6 | Free agent | 6% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 2 | — | — | — | — | — | 28.1 | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 4 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 1 / 4 |
| **Isaiah Jackson** | LAC | Left Groin Soreness | 10 Nov | 2 | 26.8 | 20.3 (3) | 27.1 (7) | 26.8 (8) | 20.6 | 20.9 | Free agent | 7% | 1 / 3 |
| **Jock Landale** | ATL | Left Hip | 09 Nov | 1 | 16.4 | 0.0 (1) | 14.8 (6) | 16.4 (7) | — | 25.8 | Free agent | 0% | 0 / 3 |
| **Isaiah Stewart** | MEM | Right Knee Bruise | 09 Nov | 1 | 22.9 | 27.0 (3) | 22.9 (7) | 22.9 (7) | 25.3 | 25.1 | Free agent | 4% | 0 / 4 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 30.8.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Nic Claxton** | CHI | Left Hamstring Strain | 08 Nov | 0 | 30.3 (27.8) | 33.3 (69) | Free agent | 42% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 09 Nov | 1 | 30.1 (30.5) | 28.0 (63) | Free agent | 44% | 0 / 4 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 10 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 1 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 2 | — (—) | 28.1 (74) | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 4 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 12 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 1 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 21 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 1 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 55 | 38.8 (32.4) | 41.6 (38) | Free agent | 29% | 0 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 55 | 36.9 (27.7) | 32.3 (32) | Free agent | 36% | 0 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 87 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 114 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 0 / 3 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 145 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 2 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Left Groin Soreness; ESPN est. back 09 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ajay Mitchell | PG/SG | 7 | 28.3 | +3.6 | 7 | **36.6** | 29.7 | 31.0 (5) | 37.6 (8) | 34.5 (10) | Lauri Birds | 73% |
| Aday Mara | C | 7 | 22.7 | +9.7 | 2 | **29.9** | 11.7 | 32.6 (5) | 27.0 (8) | 24.4 (10) | **us** | 18% |
| Jared McCain | PG/SG | 7 | 27.3 | +7.0 | 4 | **24.6** | 12.3 | 25.6 (5) | 21.8 (8) | 20.9 (10) | Free agent | 30% |
| Bennett Stirtz | PG | 7 | 23.7 | +19.0 | 0 | **19.7** | 2.0 | 24.0 (5) | 18.1 (8) | 14.4 (10) | Free agent | 1% |
| Kenrich Williams | SF | 7 | 23.4 | +16.8 | 7 | **18.3** | 7.0 | 20.4 (5) | 16.8 (8) | 14.9 (10) | Free agent | 1% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 10 | 32.2 | +3.6 | 10 | **40.7** | 33.7 | 47.5 (4) | 42.7 (9) | 40.7 (10) | **us** | 93% |
| Brandin Podziemski | PG/SG | 8 | 34.0 | +3.1 | 8 | **35.9** | 30.8 | 35.0 (4) | 35.9 (8) | 35.9 (8) | Matt Wright's Foxies | 76% |
| Brandon Williams | PG/SG | 9 | 17.8 | — | 1 | **20.3** | — | 24.3 (3) | 19.2 (8) | 20.3 (9) | Free agent | 2% |
| Georges Niang | PF | 10 | 20.6 | — | 2 | **16.9** | — | 19.8 (4) | 17.1 (9) | 16.9 (10) | Free agent | 1% |
| Will Richard | SG/SF | 10 | 17.1 | — | 3 | **12.5** | — | 13.0 (4) | 11.0 (9) | 12.4 (10) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 02 Jan | 25.7 | 7.0 | Free agent |

Last 9 games: 2 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Micah Potter | C | 1 | 14.0 | +7.2 | 0 | **22.0** | 3.2 | 10.7 (3) | 7.2 (4) | 7.0 (5) | Free agent | 0% |
| Chris Youngblood | SG | 2 | 20.5 | +11.8 | 0 | **18.0** | 4.3 | 9.8 (5) | 9.8 (5) | 9.8 (5) | Free agent | 0% |
| Yang Hansen | C | 2 | 14.5 | +6.5 | 0 | **14.0** | 8.2 | 10.5 (4) | 11.0 (5) | 10.2 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | +5.0 | 0 | **12.0** | -2.0 | — | — | — | — | 0% |
| Branden Carlson | C | 1 | 12.0 | +5.7 | 0 | **7.0** | 5.3 | 4.7 (3) | 5.8 (4) | 5.8 (4) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 6 | 35.0 | +8.8 | 6 | **45.0** | 25.8 | 48.5 (4) | 38.3 (9) | 37.3 (10) | Cream Abdul-Yammar | 79% |
| Jaden McDaniels | SF/PF | 6 | 35.5 | +3.8 | 6 | **37.2** | 36.8 | 34.0 (4) | 36.3 (9) | 37.0 (10) | Melbourne poopoo | 89% |
| LaMelo Ball | PG | 6 | 29.3 | +4.3 | 6 | **37.0** | 30.8 | 38.5 (4) | 33.7 (9) | 34.5 (10) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 6 | 15.0 | +7.0 | 0 | **24.0** | 9.0 | 20.8 (4) | 19.4 (9) | 18.0 (10) | Free agent | 3% |
| Trey Lyles | PF | 6 | 21.0 | +7.0 | 0 | **17.7** | 11.0 | 16.8 (4) | 16.7 (9) | 15.0 (10) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |
| Jusuf Nurkic | Right Foot Strain | 20 Nov | 26.4 | 36.7 | Free agent |

Last 9 games: 5 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Lauri Markkanen (day to day, ESPN est. back 08 Nov) | SF/PF | 4 | 33.2 | +4.8 | 4 | **39.5** | 25.5 | 39.5 (4) | 33.4 (7) | 32.5 (8) | Lauri Birds | 90% |
| Ace Bailey | SF/PF | 5 | 33.0 | +5.8 | 5 | **21.8** | 38.8 | 20.8 (4) | 28.5 (8) | 29.3 (9) | Dr White Slong | 60% |
| Josh Okogie | SF | 5 | 22.2 | +9.2 | 0 | **15.8** | 3.3 | 13.2 (4) | 12.7 (7) | 11.1 (8) | Free agent | 0% |
| Josh Green | SG | 5 | 17.6 | +3.6 | 1 | **8.2** | 7.5 | 6.2 (4) | 8.0 (7) | 8.0 (7) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 8 | 30.5 | +8.5 | 8 | **33.4** | 20.0 | 34.0 (3) | 31.6 (7) | 33.1 (8) | Lauri Birds | 39% |
| Derrick Jones Jr. | SF/PF | 7 | 30.0 | +4.6 | 7 | **29.4** | 21.1 | 26.0 (2) | 29.3 (6) | 29.4 (7) | Free agent | 11% |
| Kobe Sanders | SG | 8 | 24.4 | — | 2 | **20.5** | — | 23.0 (3) | 21.3 (7) | 20.5 (8) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 6 | 35.2 | +5.2 | 6 | **43.2** | 29.8 | 49.0 (4) | 37.6 (9) | 37.0 (10) | Snow Time Lakers | 67% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 9 | 22.0 | +6.0 | 1 | **23.0** | 26.0 | 27.2 (4) | 23.0 (9) | 23.3 (10) | Free agent | 7% |
| Jarace Walker | SF/PF | 9 | 24.1 | +5.1 | 2 | **20.6** | 6.0 | 22.2 (4) | 20.6 (9) | 19.1 (10) | Free agent | 1% |
| Jay Huff | C | 9 | 18.3 | — | 5 | **15.9** | — | 14.5 (4) | 15.9 (9) | 15.9 (9) | Free agent | 1% |
| Larry Nance Jr. | PF | 8 | 17.0 | +12.0 | 0 | **15.1** | -1.0 | 16.3 (3) | 15.1 (8) | 13.3 (9) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 14.9 | — | 1 | **14.2** | — | 18.2 (4) | 14.2 (9) | 14.2 (9) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 7 | 38.0 | +7.0 | 7 | **44.7** | 30.0 | 48.5 (4) | 42.2 (8) | 41.4 (9) | Cream Abdul-Yammar | 91% |
| Desmond Bane (out, ESPN est. back 10 Nov) | SG/SF | 6 | 36.0 | +6.0 | 6 | **32.7** | 13.0 | 28.0 (3) | 27.9 (7) | 27.8 (8) | Free agent | 91% |
| Wendell Carter Jr. | C | 7 | 34.4 | +4.4 | 7 | **32.0** | 46.5 | 35.2 (4) | 33.9 (8) | 35.2 (9) | Dr White Slong | 56% |
| Jamal Cain | SF | 7 | 21.4 | +8.9 | 1 | **15.9** | -5.0 | 16.5 (4) | 13.5 (8) | 11.2 (9) | Free agent | 0% |
| Jase Richardson | SG | 7 | 25.0 | +11.0 | 7 | **15.4** | 14.5 | 15.8 (4) | 15.0 (8) | 15.2 (9) | Free agent | 1% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 7 | 33.9 | +3.9 | 7 | **35.7** | 39.0 | 38.8 (4) | 37.8 (8) | 36.7 (9) | Dr White Slong | 82% |
| Immanuel Quickley (day to day, ESPN est. back 09 Nov) | PG/SG | 6 | 32.8 | +4.3 | 6 | **35.2** | 35.0 | 34.3 (3) | 32.6 (7) | 35.1 (8) | Cream Abdul-Yammar | 77% |
| Jamal Shead | PG | 7 | 23.7 | +3.7 | 1 | **27.3** | 11.0 | 30.8 (4) | 25.6 (8) | 23.7 (9) | Free agent | 3% |
| Ja'Kobe Walter | SG | 7 | 30.7 | +7.2 | 7 | **25.3** | 28.0 | 18.8 (4) | 25.2 (8) | 25.9 (9) | Free agent | 13% |
| Collin Murray-Boyles | PF | 7 | 23.1 | +4.1 | 3 | **24.0** | 25.0 | 29.2 (4) | 24.0 (8) | 24.4 (9) | Free agent | 11% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin (out, ESPN est. back 09 Nov) | PG/SG | 5 | 18.8 | — | 0 | **24.4** | — | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% |

### PHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dominick Barlow | Back Fracture | 18 Nov | 23.7 | 22.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaylen Brown | SG/SF | 9 | 36.0 | +3.6 | 9 | **40.8** | 38.6 | 44.5 (4) | 41.0 (7) | 40.8 (9) | Snow Time Lakers | 100% |
| Dean Wade | PF | 8 | 25.6 | +4.1 | 4 | **19.5** | 16.3 | 20.8 (4) | 19.5 (8) | 19.5 (8) | Free agent | 1% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 9 | 36.8 | +6.2 | 9 | **39.3** | 30.4 | 45.8 (4) | 42.6 (8) | 38.9 (9) | Team Nic Kerr | 86% |
| Dylan Cardwell | C | 2 | 14.0 | — | 0 | **21.5** | — | 21.5 (2) | 21.5 (2) | 21.5 (2) | Free agent | 0% |
| Leaky Black | SF | 5 | 19.0 | — | 1 | **20.6** | — | 30.3 (3) | 20.6 (5) | 20.6 (5) | Free agent | 0% |
| De'Andre Hunter | SF/PF | 8 | 31.2 | +3.6 | 8 | **19.5** | 23.9 | 15.3 (3) | 20.9 (7) | 19.4 (8) | Free agent | 6% |
| Jonathan Mogbo | PF | 4 | 17.2 | +4.7 | 0 | **13.2** | 11.3 | 28.0 (1) | 18.3 (3) | 13.2 (4) | Free agent | 0% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 8 | 34.2 | +6.8 | 8 | **30.1** | 23.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 42% |
| Spencer Jones | SF/PF | 1 | 21.0 | — | 0 | **30.0** | — | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 0% |
| Trevon Brazile | SF/PF | 8 | 21.1 | — | 1 | **20.5** | — | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% |
| Bryce Hopkins | SF | 6 | 16.2 | — | 2 | **10.2** | — | 17.5 (2) | 11.8 (5) | 10.2 (6) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.7 | +5.4 | 0 | **28.8** | 19.2 | 26.2 (5) | 28.8 (10) | 28.7 (11) | Free agent | 34% |
| Zuby Ejiofor | PF | 6 | 12.3 | — | 0 | **15.5** | — | 22.5 (4) | 15.5 (6) | 15.5 (6) | Free agent | 0% |
| Jock Landale (out, ESPN est. back 09 Nov) | C | 6 | 14.7 | — | 0 | **14.8** | — | 0.0 (1) | 14.8 (6) | 16.4 (7) | Free agent | 0% |

## Every injury

All 88 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 327 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 327 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 235 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 145 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 145 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 114 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 114 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 114 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 114 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 109 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 87 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 02 Jan | 55 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 55 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 55 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 55 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 55 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 55 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 43 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 36 | Matt Wright's Foxies |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 25 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 25 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 23 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 23 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 23 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 21 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 21 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 15 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 14 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 12 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 12 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 10 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 10 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 10 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 5 | Lauri Birds |
| Thomas Sorber | OKC | Out | Knee | 13 Nov | 5 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 4 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 12 Nov | 4 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 4 | Free agent |
| Zach Collins | CHI | Out | Illness | 11 Nov | 3 | Free agent |
| Mikel Brown Jr. | BKN | Out | Rest | 11 Nov | 3 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 11 Nov | 3 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 10 Nov | 2 | Free agent |
| Robert Williams III | POR | Out | Rest | 10 Nov | 2 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 2 | Free agent |
| Josh Hart | NY | Out | Ankle | 10 Nov | 2 | Dr White Slong |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 2 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 10 Nov | 2 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 2 | Free agent |
| Isaiah Jackson | LAC | Out | Left Groin Soreness | 10 Nov | 2 | Free agent |
| Desmond Bane | ORL | Out | Illness | 10 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 10 Nov | 2 | Melbourne poopoo |
| Adem Bona | PHI | Out | Back Sprain | 10 Nov | 2 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 09 Nov | 1 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 09 Nov | 1 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 09 Nov | 1 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 09 Nov | 1 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 09 Nov | 1 | Free agent |
| Scottie Barnes | TOR | Day-To-Day | Left Groin Soreness | 09 Nov | 1 | **us** |
| Sam Merrill | CLE | Out | Right Elbow | 09 Nov | 1 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 09 Nov | 1 | — |
| Moussa Diabate | CHA | Day-To-Day | Quadriceps | 09 Nov | 1 | Team Nic Kerr |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 09 Nov | 1 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 09 Nov | 1 | — |
| Jordan Goodwin | PHX | Out | Left Calf | 09 Nov | 1 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 09 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 09 Nov | 1 | Free agent |
| Jarrett Allen | CLE | Out | Right Knee | 09 Nov | 1 | Dr White Slong |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 1 | **us** |
| Isaiah Stewart | MEM | Out | Right Knee Bruise | 09 Nov | 1 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 09 Nov | 1 | Free agent |
| Immanuel Quickley | TOR | Day-To-Day | Right Hamstring | 09 Nov | 1 | Cream Abdul-Yammar |
| Grant Williams | CHA | Out | Right Hamstring | 09 Nov | 1 | Free agent |
| Dennis Schroder | CHA | Out | Thigh | 09 Nov | 1 | Free agent |
| Deandre Ayton | WSH | Out | Leg | 09 Nov | 1 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 09 Nov | 1 | Free agent |
| Brandon Miller | CHA | Day-To-Day | Right Groin Soreness | 09 Nov | 1 | Matt Wright's Foxies |
| Asa Newell | ATL | Out | Left Toe | 09 Nov | 1 | Free agent |
| Anthony Davis | WSH | Out | Right Ankle Sprain | 09 Nov | 1 | Melbourne poopoo |
| Tobe Awaka | CHI | Day-To-Day | Left Knee Sprain | 08 Nov | 0 | Free agent |
| Nic Claxton | CHI | Out | Left Hamstring Strain | 08 Nov | 0 | Free agent |
| Luka Doncic | LAL | Day-To-Day | Back | 08 Nov | 0 | Team Nic Kerr |
| Lauri Markkanen | UTAH | Day-To-Day | Right Wrist Sprain | 08 Nov | 0 | Lauri Birds |
| Keegan Murray | SAC | Out | Left Ankle | 08 Nov | 0 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Right Foot Plantar Fasciitis | 08 Nov | 0 | Dr White Slong |
| Joan Beringer | MIN | Day-To-Day | Fracture | 08 Nov | 0 | Free agent |
| Jalen Smith | CHI | Day-To-Day | Left Finger Sprain | 08 Nov | 0 | Free agent |
| Isaac Jones | DET | Day-To-Day | Not Injury Related | 08 Nov | 0 | Free agent |
| Elijah Harkless | DET | Day-To-Day | Not Injury Related | 08 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-08 05:58 UTC.
