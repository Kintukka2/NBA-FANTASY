# Injury Watch: 02 Nov 2026

- Generated 2026-11-02 06:54 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 95 players in ESPN's injury feed. 26 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 15 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1099 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L15 and L30 cover every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (02 Nov–08 Nov) / next week (09 Nov–15 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Trey Murphy III 27.7 (L7 27.3), Isaiah Hartenstein 28.7 (L7 34.8), Desmond Bane 29.0 (L7 37.0), Jalen Duren 33.5 (L7 23.0), Fred VanVleet 35.4 (L7 31.3). A pickup at or above **35.4** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (04 Nov) | 5 | 36.0 | +8.5 | **34.6** | 34.6 | 40.3 (3) | 34.6 (5) | 34.6 (5) | Free agent | 29% | 3 / 3 |
| **Zaccharie Risacher** | DAL | Dereck Lively II (12 Nov); also out: Santi Aldama (04 Nov) | 6 | 29.7 | +6.9 | **32.0** | 32.0 | 33.3 (3) | 32.0 (6) | 32.0 (6) | Free agent | 15% | 4 / 4 |
| **Precious Achiuwa** | SAC | Maxime Raynaud (10 Nov), Ben Simmons (01 Oct); also out: Dylan Cardwell (02 Nov) | 6 | 29.0 | +4.7 | **31.3** | 31.3 | 30.0 (4) | 31.3 (6) | 31.3 (6) | Waivers | 28% | 4 / 3 |
| **Naji Marshall** | DAL | Dereck Lively II (12 Nov); also out: Santi Aldama (04 Nov) | 3 | 27.7 | +3.5 | **31.3** | 31.3 | 23.0 (1) | 31.3 (3) | 31.3 (3) | Free agent | 10% | 4 / 4 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 7 | 25.9 | +5.6 | **28.9** | 28.9 | 25.5 (4) | 28.9 (7) | 28.9 (7) | Waivers | 32% | 4 / 3 |
| **Derrick Jones Jr.** (day to day, ESPN est. back 02 Nov) | LAC | Jordan Miller (02 Mar); also out: Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov) | 6 | 28.8 | +3.4 | **27.8** | 27.8 | 25.8 (4) | 27.8 (6) | 27.8 (6) | Waivers | 16% | 3 / 3 |
| **P.J. Washington** | DAL | Dereck Lively II (12 Nov); also out: Santi Aldama (04 Nov) | 6 | 33.7 | +4.7 | **27.5** | 27.5 | 27.7 (3) | 27.5 (6) | 27.5 (6) | Free agent | 24% | 4 / 4 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 23.0 | +10.0 | **27.3** | 19.5 | 22.2 (4) | 19.5 (6) | 19.5 (6) | Free agent | 15% | 4 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 4 | 21.0 | — | **27.2** | 27.2 | 32.0 (2) | 27.2 (4) | 27.2 (4) | Free agent | 1% | 4 / 4 |
| **Toumani Camara** | POR | Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 1 | 31.0 | +6.0 | **27.0** | 31.0 | 28.3 (3) | 31.0 (5) | 31.0 (5) | Waivers | 41% | 4 / 3 |
| **Jaxson Hayes** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 28.5 | +4.8 | **27.0** | 32.2 | 26.0 (3) | 32.2 (5) | 32.2 (5) | Free agent | 16% | 4 / 4 |
| **Jamal Shead** | TOR | Kawhi Leonard (23 Nov) | 4 | 23.0 | +3.0 | **25.5** | 20.7 | 25.5 (4) | 20.7 (6) | 20.7 (6) | Free agent | 3% | 3 / 4 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 3 | 24.0 | +9.2 | **23.0** | 21.6 | 24.6 (5) | 21.6 (7) | 21.6 (7) | Free agent | 2% | 4 / 2 |
| **Scoot Henderson** | POR | Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 1 | 31.0 | +12.0 | **22.0** | 9.6 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% | 4 / 3 |
| **Brice Sensabaugh** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 18.5 | +4.5 | **22.0** | 16.3 | 19.0 (4) | 16.3 (6) | 16.3 (6) | Free agent | 2% | 4 / 4 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (04 Nov) | 5 | 22.8 | — | **22.0** | 22.0 | 19.3 (3) | 22.0 (5) | 22.0 (5) | Free agent | 4% | 3 / 3 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 29.0 | +8.7 | **20.0** | 16.2 | 15.5 (4) | 16.2 (6) | 16.2 (6) | Free agent | 33% | 4 / 4 |
| **Kobe Sanders** | LAC | Jordan Miller (02 Mar); also out: Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov) | 6 | 23.2 | — | **20.0** | 20.0 | 21.5 (4) | 20.0 (6) | 20.0 (6) | Free agent | 1% | 3 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 08 Nov | 6 | 41.5 | 15.0 (1) | 41.5 (2) | 41.5 (2) | 24.7 | 22.5 | Free agent | 14% | 4 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 2 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 4 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 8 | 26.3 | 23.0 (1) | 26.3 (3) | 26.3 (3) | 29.1 | 34.7 | Free agent | 18% | 3 / 3 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 2 | — | — | — | — | 30.3 | 33.3 | Free agent | 42% | 3 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 04 Nov | 2 | — | — | — | — | 25.0 | 32.4 | Free agent | 6% | 4 / 4 |
| **Jalen Smith** | CHI | Left Finger Sprain | 02 Nov | 0 | 32.3 | 31.3 (3) | 32.3 (6) | 32.3 (6) | 22.4 | 25.5 | Free agent | 19% | 3 / 3 |
| **Jakob Poeltl** | TOR | Left Shoulder Inflammation | 02 Nov | 0 | 16.8 | 13.3 (3) | 16.8 (5) | 16.8 (5) | 31.7 | 30.3 | Free agent | 39% | 3 / 4 |
| **Keegan Murray** | SAC | Ankle | 06 Nov | 4 | 12.0 | 18.0 (1) | 12.0 (2) | 12.0 (2) | 29.3 | 31.6 | Free agent | 35% | 4 / 3 |
| **Alex Caruso** | OKC | Right Ankle | 04 Nov | 2 | 30.8 | 34.5 (2) | 30.8 (4) | 30.8 (4) | 24.0 | 18.0 | Free agent | 17% | 4 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 02 Nov | 0 | 14.2 | 8.3 (3) | 14.2 (5) | 14.2 (5) | 30.6 | 27.1 | Free agent | 12% | 3 / 4 |
| **Mitchell Robinson** | BOS | Rest | 02 Nov | 0 | 18.2 | 18.3 (3) | 18.2 (5) | 18.2 (5) | 30.3 | 28.2 | Free agent | 14% | 4 / 3 |
| **Reed Sheppard** | HOU | Back | 02 Nov | 0 | 26.8 | 23.0 (2) | 26.8 (4) | 26.8 (4) | 29.9 | 30.1 | Free agent | 59% | 3 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 06 Nov | 4 | — | — | — | — | 30.1 | 28.0 | Free agent | 46% | 4 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 07 Nov | 5 | 15.0 | 6.0 (2) | 15.0 (4) | 15.0 (4) | 30.0 | 22.2 | Free agent | 32% | 4 / 2 |
| **Peyton Watson** | CLE | Right Hamstring Soreness | 02 Nov | 0 | 27.0 | 31.0 (4) | 27.0 (6) | 27.0 (6) | 29.3 | 29.8 | Free agent | 48% | 4 / 4 |
| **Obi Toppin** | IND | Back Soreness | 02 Nov | 0 | 29.0 | 27.3 (3) | 29.0 (5) | 29.0 (5) | 21.9 | 22.4 | Free agent | 13% | 3 / 4 |
| **Draymond Green** | GS | Rest | 02 Nov | 0 | 23.0 | 25.7 (3) | 23.0 (5) | 23.0 (5) | 28.5 | 26.5 | Free agent | 24% | 3 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 04 Nov | 2 | 18.6 | 16.0 (3) | 18.6 (5) | 18.6 (5) | 25.6 | 28.3 | Free agent | 3% | 4 / 4 |
| **Ziaire Williams** | LAL | Left Foot | 02 Nov | 0 | 28.2 | 26.5 (2) | 28.2 (4) | 28.2 (4) | 19.7 | 20.1 | Free agent | 4% | 4 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 8 | — | — | — | — | — | 28.1 | Free agent | 1% | 4 / 3 |
| **Derrick Jones Jr.** | LAC | Right Knee | 02 Nov | 0 | 27.8 | 25.8 (4) | 27.8 (6) | 27.8 (6) | 21.1 | 24.2 | Waivers | 16% | 3 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 10 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 4 / 4 |
| **Dylan Cardwell** | SAC | Left Calf Strain | 02 Nov | 0 | — | — | — | — | — | 26.6 | Free agent | 0% | 4 / 3 |
| **Jock Landale** | ATL | Left Hip | 04 Nov | 2 | 16.4 | 15.5 (4) | 16.4 (7) | 16.4 (7) | — | 25.8 | Free agent | 1% | 4 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 6 | — | — | — | — | 25.6 | 10.5 | Free agent | 2% | 3 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 02 Nov | 0 | — | — | — | — | 24.4 | 25.5 | Free agent | 8% | 3 / 4 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 35.4.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dylan Cardwell** | SAC | Left Calf Strain | 02 Nov | 0 | — (—) | 26.6 (44) | Free agent | 0% | 4 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 02 Nov | 0 | 24.4 (17.8) | 25.5 (56) | Free agent | 8% | 3 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 2 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 4 / 4 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 2 | 30.3 (27.8) | 33.3 (69) | Free agent | 42% | 3 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 04 Nov | 2 | 25.0 (23.7) | 32.4 (43) | Free agent | 6% | 4 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 06 Nov | 4 | 30.1 (30.5) | 28.0 (63) | Free agent | 46% | 4 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 6 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 3 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 08 Nov | 6 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 65% | 3 / 3 |
| **Kon Knueppel** | CHA | Left Hamstring | 09 Nov | 7 | 35.2 (34.2) | 34.1 (81) | Team Nic Kerr | 90% | 3 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 8 | — (—) | 28.1 (74) | Free agent | 1% | 4 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 10 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 4 / 4 |
| **Kristaps Porzingis** | GS | Illness | 01 Dec | 29 | 36.9 (27.7) | 32.3 (32) | Free agent | 41% | 3 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 61 | 38.8 (32.4) | 41.6 (38) | Free agent | 30% | 3 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 93 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 4 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 120 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 4 / 3 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 151 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 4 / 2 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Trey Murphy III** (NO): Day-To-Day, Knee; ESPN est. back 02 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 6 games: 3 game(s) without them, 3 with them.

Also out in those games, so part of the gain is theirs: Nikola Topic (back; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Isaiah Hartenstein | C | 3 | 25.7 | +3.3 | 3 | **35.0** | 22.3 | 34.8 (4) | 28.7 (6) | 28.7 (6) | **us** | 46% |
| Aday Mara | C | 3 | 23.0 | +10.0 | 0 | **27.3** | 11.7 | 22.2 (4) | 19.5 (6) | 19.5 (6) | Free agent | 15% |
| Jared McCain | PG/SG | 3 | 29.0 | +8.7 | 3 | **20.0** | 12.3 | 15.5 (4) | 16.2 (6) | 16.2 (6) | Free agent | 33% |
| Kenrich Williams | SF | 3 | 20.7 | +14.0 | 3 | **16.7** | 7.0 | 14.0 (4) | 11.8 (6) | 11.8 (6) | Free agent | 0% |
| Bennett Stirtz | PG | 3 | 26.3 | +21.7 | 0 | **12.3** | 2.0 | 11.0 (4) | 7.2 (6) | 7.2 (6) | Free agent | 0% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 7 | 32.3 | +7.7 | 7 | **40.6** | 23.5 | 39.8 (4) | 40.6 (7) | 40.6 (7) | **us** | 88% |
| Brandon Williams | PG/SG | 7 | 17.4 | — | 1 | **20.4** | — | 17.8 (4) | 20.4 (7) | 20.4 (7) | Free agent | 2% |
| Georges Niang | PF | 7 | 19.6 | — | 2 | **13.0** | — | 15.5 (4) | 13.0 (7) | 13.0 (7) | Free agent | 0% |
| Will Richard | SG/SF | 7 | 16.4 | — | 1 | **11.6** | — | 7.5 (4) | 11.6 (7) | 11.6 (7) | Free agent | 0% |
| Gary Payton II | SG | 7 | 13.0 | — | 0 | **10.0** | — | 12.5 (4) | 10.0 (7) | 10.0 (7) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: T.J. McConnell (right hamstring strain; ESPN est. 02 Nov), Ivica Zubac (left ankle sprain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Nesmith | SG/SF | 3 | 26.0 | +6.0 | 3 | **19.3** | 16.3 | 19.6 (5) | 17.8 (6) | 17.8 (6) | Free agent | 3% |
| Larry Nance Jr. | PF | 3 | 22.3 | +10.6 | 0 | **18.7** | 6.5 | 16.6 (5) | 11.7 (7) | 11.7 (7) | Free agent | 0% |
| Kobe Brown | PF | 2 | 17.5 | +17.0 | 0 | **12.5** | -0.5 | 8.0 (3) | 6.0 (4) | 6.0 (4) | Free agent | 0% |
| Jalen Slawson | SF | 3 | 16.0 | +7.0 | 0 | **9.3** | 11.3 | 6.6 (5) | 10.3 (6) | 10.3 (6) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |
| Jalen Suggs | Right Knee | 10 Nov | 33.3 | 26.3 | Free agent |

Last 6 games: 3 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Desmond Bane | SG/SF | 3 | 37.7 | +6.0 | 3 | **37.0** | 21.0 | 37.0 (4) | 29.0 (6) | 29.0 (6) | **us** | 93% |
| Franz Wagner | SF/PF | 3 | 37.7 | +4.7 | 3 | **34.7** | 36.3 | 38.2 (4) | 35.5 (6) | 35.5 (6) | Cream Abdul-Yammar | 90% |
| Jase Richardson | SG | 3 | 24.3 | +9.3 | 3 | **16.0** | 11.0 | 13.0 (4) | 13.5 (6) | 13.5 (6) | Free agent | 0% |
| Jevon Carter | PG | 1 | 22.0 | +9.0 | 0 | **10.0** | 9.0 | 10.0 (1) | 9.5 (2) | 9.5 (2) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 3 | 33.3 | +7.1 | 3 | **44.3** | 25.8 | 31.0 (5) | 33.7 (7) | 33.7 (7) | Cream Abdul-Yammar | 71% |
| Jaden McDaniels | SF/PF | 3 | 35.7 | +3.9 | 3 | **39.3** | 36.8 | 36.8 (5) | 37.9 (7) | 37.9 (7) | Melbourne poopoo | 88% |
| Bones Hyland | PG | 3 | 16.7 | +8.7 | 0 | **27.0** | 9.0 | 21.2 (5) | 16.7 (7) | 16.7 (7) | Free agent | 2% |
| Joan Beringer | C | 3 | 24.0 | +9.2 | 1 | **23.0** | 20.2 | 24.6 (5) | 21.6 (7) | 21.6 (7) | Free agent | 2% |
| Jaylen Clark | SG | 3 | 14.7 | +11.0 | 0 | **16.0** | 4.0 | 13.8 (4) | 10.0 (6) | 10.0 (6) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Waivers |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |

Last 5 games: 1 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Toumani Camara | SF/PF | 1 | 31.0 | +6.0 | 1 | **27.0** | 32.5 | 28.3 (3) | 31.0 (5) | 31.0 (5) | Waivers | 41% |
| Scoot Henderson | PG/SG | 1 | 31.0 | +12.0 | 1 | **22.0** | 6.5 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% |
| Yang Hansen | C | 1 | 13.0 | +4.5 | 0 | **16.0** | 9.5 | 14.5 (2) | 11.7 (3) | 11.7 (3) | Free agent | 0% |
| Vit Krejci | PG | 1 | 24.0 | +15.8 | 0 | **16.0** | 4.0 | 7.0 (3) | 6.4 (5) | 6.4 (5) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Maxime Raynaud | Right Knee Dislocated | 10 Nov | 26.6 | 28.1 | Free agent |
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Dylan Cardwell (left calf strain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 6 | 36.5 | +5.9 | 6 | **37.7** | 30.4 | 46.2 (4) | 37.7 (6) | 37.7 (6) | Team Nic Kerr | 80% |
| Precious Achiuwa | PF/C | 6 | 29.0 | +4.7 | 4 | **31.3** | 24.1 | 30.0 (4) | 31.3 (6) | 31.3 (6) | Waivers | 28% |
| Jonathan Mogbo | PF | 4 | 17.2 | +4.7 | 0 | **13.2** | 11.3 | 18.3 (3) | 13.2 (4) | 13.2 (4) | Free agent | 0% |
| Daeqwon Plowden | SG | 5 | 14.0 | — | 0 | **8.2** | — | 6.7 (3) | 8.2 (5) | 8.2 (5) | Free agent | 0% |
| Emanuel Sharp | SG | 6 | 17.8 | — | 0 | **6.3** | — | 5.0 (4) | 6.7 (6) | 6.7 (6) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Anthony Gill (back spasms; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 2 | 35.0 | +5.0 | 2 | **30.5** | 29.8 | 30.0 (3) | 29.7 (6) | 29.7 (6) | Snow Time Lakers | 48% |
| Alex Sarr (day to day, ESPN est. back 02 Nov) | PF/C | 2 | 27.5 | +3.0 | 2 | **25.0** | 27.5 | 27.0 (3) | 26.7 (6) | 26.7 (6) | Team Nic Kerr | 76% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 6 games: 4 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Immanuel Quickley | PG/SG | 4 | 31.8 | +3.2 | 4 | **34.8** | 35.0 | 34.8 (4) | 34.8 (6) | 34.8 (6) | Cream Abdul-Yammar | 78% |
| Ja'Kobe Walter | SG | 4 | 31.0 | +7.5 | 4 | **31.8** | 28.0 | 31.8 (4) | 30.5 (6) | 30.5 (6) | Lauri Birds | 24% |
| Jamal Shead | PG | 4 | 23.0 | +3.0 | 0 | **25.5** | 11.0 | 25.5 (4) | 20.7 (6) | 20.7 (6) | Free agent | 3% |
| Jamison Battle | SF | 4 | 17.2 | +5.8 | 0 | **13.2** | 17.0 | 13.2 (4) | 14.5 (6) | 14.5 (6) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 2 | 38.5 | +11.2 | 2 | **28.5** | 38.8 | 41.0 (4) | 35.3 (6) | 35.3 (6) | Dr White Slong | 65% |
| Jaxson Hayes | C | 2 | 28.5 | +4.8 | 2 | **27.0** | 35.7 | 26.0 (3) | 32.2 (5) | 32.2 (5) | Free agent | 16% |
| Brice Sensabaugh | SG/SF | 2 | 18.5 | +4.5 | 0 | **22.0** | 13.5 | 19.0 (4) | 16.3 (6) | 16.3 (6) | Free agent | 2% |
| Isaiah Collier | PG | 2 | 22.0 | +5.0 | 0 | **15.0** | 18.0 | 17.8 (4) | 17.0 (6) | 17.0 (6) | Free agent | 3% |
| Josh Okogie | SF | 2 | 21.0 | +8.0 | 0 | **12.0** | 3.3 | 8.5 (4) | 6.8 (5) | 6.8 (5) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 4 | 21.0 | — | 0 | **27.2** | — | 32.0 (2) | 27.2 (4) | 27.2 (4) | Free agent | 1% |

### DAL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dereck Lively II | Right Foot Surgery | 12 Nov | 23.6 | 21.3 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Santi Aldama (right knee surgery; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Zaccharie Risacher | SF | 6 | 29.7 | +6.9 | 1 | **32.0** | 20.3 | 33.3 (3) | 32.0 (6) | 32.0 (6) | Free agent | 15% |
| Naji Marshall | SF/PF | 3 | 27.7 | +3.5 | 1 | **31.3** | 22.4 | 23.0 (1) | 31.3 (3) | 31.3 (3) | Free agent | 10% |
| P.J. Washington | SF/PF | 6 | 33.7 | +4.7 | 6 | **27.5** | 26.9 | 27.7 (3) | 27.5 (6) | 27.5 (6) | Free agent | 24% |
| Marcus Sasser | PG | 6 | 19.2 | +6.1 | 0 | **14.3** | 12.4 | 4.7 (3) | 14.3 (6) | 14.3 (6) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Max Strus (right foot plantar fasciitis; ESPN est. 08 Nov), Brandon Ingram (right achilles surgery; ESPN est. 08 Nov), Bradley Beal (right knee inflammation; ESPN est. 08 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 6 | 29.8 | +7.8 | 6 | **36.5** | 20.0 | 37.0 (4) | 36.2 (6) | 36.2 (6) | Dr White Slong | 39% |
| Derrick Jones Jr. (day to day, ESPN est. back 02 Nov) | SF/PF | 6 | 28.8 | +3.4 | 6 | **27.8** | 21.1 | 25.8 (4) | 27.8 (6) | 27.8 (6) | Waivers | 16% |
| Isaiah Jackson | PF/C | 6 | 21.7 | +3.3 | 6 | **27.7** | 20.6 | 27.5 (4) | 28.0 (6) | 28.0 (6) | Team Nic Kerr | 14% |
| Kobe Sanders | SG | 6 | 23.2 | — | 1 | **20.0** | — | 21.5 (4) | 20.0 (6) | 20.0 (6) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jamal Murray | PG | 5 | 38.2 | +3.2 | 5 | **47.6** | 43.9 | 54.0 (3) | 47.6 (5) | 47.6 (5) | **us** | 99% |
| Christian Braun | SG/SF | 5 | 36.0 | +8.5 | 5 | **34.6** | 23.1 | 40.3 (3) | 34.6 (5) | 34.6 (5) | Free agent | 29% |
| Trevon Brazile | SF/PF | 5 | 22.8 | — | 1 | **22.0** | — | 19.3 (3) | 22.0 (5) | 22.0 (5) | Free agent | 4% |
| Alpha Diallo (out, ESPN est. back 02 Nov) | SF | 1 | 22.0 | — | 0 | **13.0** | — | 13.0 (1) | 13.0 (1) | 13.0 (1) | Free agent | 0% |
| Bryce Hopkins | SF | 4 | 16.5 | — | 2 | **6.5** | — | 9.0 (2) | 6.5 (4) | 6.5 (4) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 7 | 25.9 | +5.6 | 0 | **28.9** | 19.2 | 25.5 (4) | 28.9 (7) | 28.9 (7) | Waivers | 32% |
| Jock Landale (out, ESPN est. back 04 Nov) | C | 7 | 15.3 | — | 0 | **16.4** | — | 15.5 (4) | 16.4 (7) | 16.4 (7) | Free agent | 1% |

## Every injury

All 95 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 333 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 333 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 241 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 151 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 151 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 120 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 120 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 120 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 120 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 115 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 93 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 61 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 61 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 61 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 61 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 49 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 42 | Matt Wright's Foxies |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 31 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 29 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 29 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 29 | Waivers |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 27 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 21 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 20 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 18 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 16 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 16 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 11 | Lauri Birds |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 10 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 10 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 8 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 8 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 8 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 09 Nov | 7 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 09 Nov | 7 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring | 09 Nov | 7 | Team Nic Kerr |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 7 | **us** |
| Grant Williams | CHA | Out | Right Hamstring | 09 Nov | 7 | Free agent |
| Adou Thiero | LAL | Out | Left Knee Inflammation | 09 Nov | 7 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 08 Nov | 6 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 6 | Free agent |
| Max Strus | LAC | Out | Right Foot Plantar Fasciitis | 08 Nov | 6 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 6 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 6 | Melbourne poopoo |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 08 Nov | 6 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 07 Nov | 5 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 06 Nov | 4 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 06 Nov | 4 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 06 Nov | 4 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 06 Nov | 4 | Free agent |
| Gui Santos | GS | Day-To-Day | Knee | 05 Nov | 3 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 04 Nov | 2 | Free agent |
| Spencer Jones | DEN | Out | Hamstring | 04 Nov | 2 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 04 Nov | 2 | Free agent |
| Santi Aldama | DAL | Out | Right Knee Surgery | 04 Nov | 2 | Free agent |
| Nikola Topic | OKC | Out | Back | 04 Nov | 2 | Free agent |
| Nic Claxton | CHI | Out | Hamstring | 04 Nov | 2 | Free agent |
| Kingston Flemings | ATL | Suspension | Suspension | 04 Nov | 2 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 04 Nov | 2 | Free agent |
| Jordan Poole | NO | Out | Left Ankle Sprain | 04 Nov | 2 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 04 Nov | 2 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 04 Nov | 2 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 04 Nov | 2 | Free agent |
| Alex Caruso | OKC | Out | Right Ankle | 04 Nov | 2 | Free agent |
| Ziaire Williams | LAL | Out | Left Foot | 02 Nov | 0 | Free agent |
| Zach LaVine | SAC | Day-To-Day | Right Elbow Soreness | 02 Nov | 0 | Cream Abdul-Yammar |
| Trey Murphy III | NO | Day-To-Day | Knee | 02 Nov | 0 | **us** |
| Tobe Awaka | CHI | Day-To-Day | Left Ankle Sprain | 02 Nov | 0 | Free agent |
| Tim Hardaway Jr. | MIA | Day-To-Day | Personal | 02 Nov | 0 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 02 Nov | 0 | Free agent |
| Stephen Curry | GS | Out | Rest | 02 Nov | 0 | Lauri Birds |
| Scotty Pippen Jr. | MEM | Day-To-Day | Back Soreness | 02 Nov | 0 | Free agent |
| Reed Sheppard | HOU | Day-To-Day | Back | 02 Nov | 0 | Free agent |
| Quinten Post | MEM | Day-To-Day | Right Ankle | 02 Nov | 0 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Right Hamstring Soreness | 02 Nov | 0 | Free agent |
| Obi Toppin | IND | Day-To-Day | Back Soreness | 02 Nov | 0 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 02 Nov | 0 | — |
| Mitchell Robinson | BOS | Out | Rest | 02 Nov | 0 | Free agent |
| Mikel Brown Jr. | BKN | Day-To-Day | Rest | 02 Nov | 0 | Free agent |
| Kyrie Irving | DAL | Day-To-Day | Left Knee | 02 Nov | 0 | Snow Time Lakers |
| Jose Alvarado | NY | Out | Left Ankle Sprain | 02 Nov | 0 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Right Foot | 02 Nov | 0 | Snow Time Lakers |
| Jalen Smith | CHI | Day-To-Day | Left Finger Sprain | 02 Nov | 0 | Free agent |
| Jalen Johnson | ATL | Day-To-Day | Left Ankle | 02 Nov | 0 | Snow Time Lakers |
| Jakob Poeltl | TOR | Day-To-Day | Left Shoulder Inflammation | 02 Nov | 0 | Free agent |
| Ivica Zubac | IND | Out | Left Ankle Sprain | 02 Nov | 0 | Lauri Birds |
| Isaiah Joe | DET | Out | Right Hip Bruise | 02 Nov | 0 | Free agent |
| Dylan Cardwell | SAC | Out | Left Calf Strain | 02 Nov | 0 | Free agent |
| Draymond Green | GS | Out | Rest | 02 Nov | 0 | Free agent |
| Derrick Jones Jr. | LAC | Day-To-Day | Right Knee | 02 Nov | 0 | Waivers |
| Dailyn Swain | CHI | Day-To-Day | Back Soreness | 02 Nov | 0 | Free agent |
| Clint Capela | HOU | Day-To-Day | Right Ankle Sprain | 02 Nov | 0 | Free agent |
| Anthony Gill | WSH | Day-To-Day | Back Spasms | 02 Nov | 0 | Free agent |
| Alpha Diallo | DEN | Out | Right Wrist Sprain | 02 Nov | 0 | Free agent |
| Alex Sarr | WSH | Day-To-Day | Left Knee Soreness | 02 Nov | 0 | Team Nic Kerr |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-02 06:54 UTC.
