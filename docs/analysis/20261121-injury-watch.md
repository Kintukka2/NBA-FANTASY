# Injury Watch: 21 Nov 2026

- Generated 2026-11-21 07:21 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 107 players in ESPN's injury feed. 39 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 21 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 24.7 (L7 33.2), Yves Missi 28.0 (L7 21.2), Daniss Jenkins 30.1 (L7 32.2), Saddiq Bey 31.1 (L7 41.0), Trey Murphy III 31.7 (L7 38.0). A pickup at or above **31.7** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 32.0 | +18.2 | **40.0** | 16.4 | 26.5 (4) | 18.2 (8) | 16.4 (16) | Free agent | 1% | 0 / 3 |
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 30.5 | +5.8 | **37.5** | 26.4 | 28.5 (4) | 33.4 (8) | 26.4 (14) | Free agent | 37% | 0 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.1 | — | **35.5** | 29.5 | 42.0 (4) | 37.2 (8) | 30.5 (15) | Free agent | 27% | 1 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 10 | 32.7 | +5.2 | **34.5** | 32.8 | 41.0 (4) | 32.9 (7) | 32.8 (14) | Waivers | 46% | 1 / 3 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (13 Dec); also out: Jalen Duren (24 Nov) | 6 | 32.8 | +15.8 | **33.8** | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 40% | 1 / 3 |
| **Tyrese Proctor** | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 5 | 28.0 | +6.0 | **33.4** | 21.8 | 33.4 (5) | 27.0 (9) | 21.8 (16) | Free agent | 10% | 0 / 3 |
| **Brandon Williams** (out, ESPN est. back 22 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +11.7 | **33.0** | 18.8 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% | 1 / 3 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 5 | 29.2 | +5.4 | **32.8** | 22.8 | 26.5 (4) | 28.2 (8) | 22.8 (16) | Free agent | 10% | 1 / 4 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 5 | 21.2 | +9.7 | **31.6** | 20.4 | 44.7 (3) | 24.6 (7) | 20.4 (15) | Free agent | 10% | 1 / 4 |
| **Mo Bamba** | UTAH | Jusuf Nurkic (29 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 8 | 22.8 | +7.8 | **30.6** | 29.3 | 35.8 (5) | 30.6 (8) | 29.3 (13) | Waivers | 21% | 1 / 3 |
| **Aaron Wiggins** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Kingston Flemings (22 Nov), Jock Landale (22 Nov) | 2 | 30.0 | +4.5 | **30.5** | 26.7 | 22.2 (4) | 26.4 (7) | 26.7 (16) | Free agent | 34% | 1 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 5 | 31.6 | +11.2 | **29.4** | 16.6 | 29.4 (5) | 24.6 (7) | 16.6 (15) | Free agent | 2% | 1 / 3 |
| **Julian Champagnie** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 1 | 29.0 | +4.0 | **29.0** | 23.9 | 21.8 (4) | 23.0 (8) | 23.2 (15) | Free agent | 41% | 1 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 22.3 | — | **28.5** | 26.6 | 27.8 (4) | 28.5 (6) | 26.6 (11) | Free agent | 3% | 0 / 4 |
| **Jaylon Tyson** (out, ESPN est. back 23 Nov) | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 2 | 32.0 | +9.0 | **28.0** | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% | 0 / 3 |
| **Jamison Battle** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 26.5 | +7.1 | **26.0** | 15.4 | 13.0 (4) | 16.5 (8) | 15.4 (16) | Free agent | 0% | 0 / 3 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 23.4 | — | **25.6** | 23.8 | 25.8 (4) | 22.6 (7) | 23.8 (16) | Free agent | 5% | 1 / 3 |
| **Brice Sensabaugh** | UTAH | Jusuf Nurkic (29 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 8 | 22.8 | +11.8 | **25.0** | 18.8 | 29.0 (5) | 22.6 (9) | 18.8 (17) | Free agent | 6% | 1 / 3 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 35.6 | +8.0 | **25.0** | 23.8 | 38.0 (3) | 30.8 (5) | 23.8 (13) | Free agent | 6% | 1 / 3 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 20.6 | +4.8 | **24.8** | 21.6 | 23.8 (4) | 24.4 (8) | 21.6 (14) | Free agent | 1% | 1 / 3 |
| **Tristan da Silva** | ORL | Paolo Banchero (29 Nov) | 8 | 31.1 | +9.7 | **24.8** | 24.7 | 22.0 (4) | 23.5 (6) | 24.7 (13) | Free agent | 10% | 1 / 3 |
| **Javon Small** (out, ESPN est. back 23 Nov) | MEM | GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 4 | 24.0 | +3.0 | **24.2** | 23.4 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 2% | 1 / 4 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 5 | 21.2 | +8.9 | **23.4** | 16.8 | 23.4 (5) | 23.4 (5) | 16.8 (13) | Free agent | 1% | 1 / 3 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (23 Nov) | 10 | 25.0 | +3.0 | **23.3** | 26.9 | 17.8 (4) | 18.5 (6) | 26.9 (14) | Free agent | 27% | 1 / 4 |
| **Kenrich Williams** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.2 | +9.8 | **22.6** | 18.6 | 31.2 (4) | 22.6 (8) | 19.3 (15) | Free agent | 1% | 1 / 3 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 25.8 | +7.1 | **22.2** | 16.1 | 25.5 (4) | 21.0 (7) | 16.1 (15) | Free agent | 1% | 1 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 9 | 22.4 | — | **22.0** | 19.1 | 19.0 (4) | 20.7 (7) | 19.1 (11) | Free agent | 0% | 1 / 3 |
| **Pete Nance** | MIL | Ousmane Dieng (14 Dec) | 1 | 28.0 | +24.0 | **22.0** | 13.5 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% | 1 / 4 |
| **Bennett Stirtz** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 20.1 | — | **20.7** | 15.5 | 16.5 (4) | 19.6 (8) | 16.5 (15) | Free agent | 1% | 1 / 3 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 8 | 27.1 | +5.6 | **20.5** | 19.4 | 20.0 (4) | 20.5 (8) | 19.4 (15) | Free agent | 1% | 1 / 4 |
| **Nic Claxton** | CHI | Caleb Wilson (13 Dec) | 4 | 22.5 | +5.5 | **20.5** | 23.3 | 20.5 (4) | 23.3 (6) | 23.3 (6) | Free agent | 40% | 1 / 3 |
| **Kel'el Ware** | MIL | Ousmane Dieng (14 Dec) | 5 | 19.6 | +3.2 | **20.2** | 22.9 | 26.8 (4) | 20.6 (8) | 22.9 (16) | Free agent | 52% | 1 / 4 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 6 | 30.6 | — | 14.5 (4) | 30.6 (9) | 39.0 | 36.5 | Free agent | 76% | 1 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 10 | 33.8 | — | — | 33.8 (4) | 37.5 | 36.0 | Free agent | 80% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 8 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 1 / 3 |
| **Grayson Allen** | CHA | Concussion | 23 Nov | 2 | 26.8 | 26.0 (1) | 29.0 (4) | 26.8 (13) | 26.6 | 31.2 | Free agent | 21% | 0 / 3 |
| **P.J. Washington** | DAL | Shoulder | 21 Nov | 0 | 28.2 | 29.3 (3) | 28.3 (7) | 28.2 (15) | 26.9 | 30.6 | Free agent | 33% | 2 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 4 | 14.2 | — | — | 14.2 (5) | 30.6 | 27.1 | Free agent | 8% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 12 | — | — | — | — | 30.1 | 28.0 | Free agent | 40% | 1 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 6 | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | 21.6 | 23.1 | Free agent | 40% | 1 / 3 |
| **Jerami Grant** | MEM | Left Calf | 21 Nov | 0 | 20.3 | 18.2 (4) → 23.7 (3) | 21.7 (7) → 25.0 (6) | 20.3 (15) → 21.6 (14) | 27.0 | 28.8 | Free agent | 9% | 1 / 4 |
| **Draymond Green** | GS | Rest | 22 Nov | 1 | 24.0 | 20.7 (3) | 26.0 (7) | 24.0 (13) | 28.5 | 26.5 | Free agent | 23% | 1 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 23 Nov | 2 | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 2% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 4 | — | — | — | — | — | 28.1 | Free agent | 2% | 1 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 6 | 8.8 | -3.0 (1) | 3.2 (4) | 8.8 (12) | 25.1 | 27.6 | Free agent | 6% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 6 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 2 / 2 |
| **Precious Achiuwa** | SAC | Left Lower Leg Bruise | 21 Nov | 0 | 25.4 | -3.0 (1) | 14.8 (4) | 25.4 (12) | 24.1 | 27.0 | Free agent | 14% | 1 / 3 |
| **Jock Landale** | ATL | Right Hip Inflammation | 22 Nov | 1 | 16.8 | 19.0 (1) | 18.0 (2) | 16.8 (9) → 18.9 (8) | — | 25.8 | Free agent | 0% | 1 / 2 |
| **Collin Murray-Boyles** | TOR | Concussion | 23 Nov | 2 | 24.0 | 21.0 (3) | 27.5 (6) | 24.0 (14) | 24.8 | 25.6 | Free agent | 12% | 0 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 8 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 1 / 4 |
| **T.J. McConnell** | IND | Left Hamstring | 22 Nov | 1 | 20.0 | 23.5 (4) | 20.0 (7) | 20.0 (7) | 24.4 | 25.5 | Free agent | 8% | 1 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.7.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Brandon Ingram** | LAC | Right Achilles Surgery | 23 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 67% | 1 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 4 | — (—) | 28.1 (74) | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 6 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 8 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 8 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 12 | 30.1 (30.5) | 28.0 (63) | Free agent | 40% | 1 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 42 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 1 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 42 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 1 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 74 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 101 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 1 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 132 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 4 |

## Our injured players

- **Jalen Smith** (CHI): Out, Illness; ESPN est. back 22 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 03 Dec.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 1 | 25.0 | +11.7 | 0 | **33.0** | 15.0 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% |
| Charles Bassey | C | 5 | 20.6 | +4.8 | 3 | **24.8** | 26.6 | 23.8 (4) | 24.4 (8) | 21.6 (14) | Free agent | 1% |
| Will Richard | SG/SF | 5 | 25.8 | +7.1 | 1 | **22.2** | 15.0 | 25.5 (4) | 21.0 (7) | 16.1 (15) | Free agent | 1% |
| LJ Cryer | PG | 5 | 16.2 | +6.2 | 2 | **14.8** | 8.2 | 18.8 (4) | 15.6 (7) | 10.8 (13) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |
| Jusuf Nurkic | Right Foot Strain | 29 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 8 | 22.8 | +7.8 | 3 | **30.6** | 28.0 | 35.8 (5) | 30.6 (8) | 29.3 (13) | Waivers | 21% |
| Brice Sensabaugh | SG/SF | 8 | 22.8 | +11.8 | 0 | **25.0** | 7.5 | 29.0 (5) | 22.6 (9) | 18.8 (17) | Free agent | 6% |
| Svi Mykhailiuk | SG | 8 | 21.2 | +5.8 | 0 | **15.0** | 5.0 | 19.8 (5) | 13.2 (9) | 11.5 (17) | Free agent | 0% |
| Isaiah Collier | PG | 5 | 15.6 | +7.6 | 0 | **14.4** | 5.0 | 8.5 (2) | 13.7 (6) | 14.1 (14) | Free agent | 2% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 25.1 | — | 6 | **35.5** | — | 42.0 (4) | 37.2 (8) | 30.5 (15) | Free agent | 27% |
| Kenrich Williams | SF | 10 | 25.2 | +9.8 | 7 | **22.6** | 14.2 | 31.2 (4) | 22.6 (8) | 19.3 (15) | Free agent | 1% |
| Bennett Stirtz | PG | 10 | 20.1 | — | 0 | **20.7** | — | 16.5 (4) | 19.6 (8) | 16.5 (15) | Free agent | 1% |
| Micah Peavy | SF | 8 | 17.2 | — | 0 | **11.6** | — | 9.5 (2) | 10.2 (6) | 9.6 (10) | Free agent | 0% |
| 5105800 |  | 5 | 13.0 | — | 0 | **6.4** | — | — | — | — | — | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 8 | 27.1 | +5.6 | 6 | **20.5** | 20.5 | 20.0 (4) | 20.5 (8) | 19.4 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | +8.8 | 0 | **16.7** | 5.5 | — | 16.7 (3) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 5 | 15.6 | — | 2 | **10.8** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 23.4 | — | 3 | **25.6** | — | 25.8 (4) | 22.6 (7) | 23.8 (16) | Free agent | 5% |
| Braden Smith | PG | 7 | 16.9 | — | 4 | **21.0** | — | 25.5 (2) | 14.8 (4) | 15.2 (10) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.4 | — | 1 | **17.1** | — | 17.5 (4) | 15.8 (6) | 14.9 (14) | Free agent | 0% |
| Jay Huff | C | 9 | 14.9 | — | 2 | **13.8** | — | 13.8 (4) | 11.0 (6) | 14.9 (14) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Allen Graves | SF | 2 | 32.0 | +18.2 | 1 | **40.0** | 10.0 | 26.5 (4) | 18.2 (8) | 16.4 (16) | Free agent | 1% |
| Jakob Poeltl | C | 2 | 30.5 | +5.8 | 2 | **37.5** | 30.4 | 28.5 (4) | 33.4 (8) | 26.4 (14) | Free agent | 37% |
| Jamison Battle | SF | 2 | 26.5 | +7.1 | 1 | **26.0** | 13.5 | 13.0 (4) | 16.5 (8) | 15.4 (16) | Free agent | 0% |
| Trayce Jackson-Davis | PF | 2 | 16.5 | +9.8 | 0 | **21.0** | 12.3 | 21.0 (2) | 22.3 (3) | 13.7 (11) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.7 | +3.0 | 10 | **38.3** | 29.7 | 44.8 (4) | 42.3 (7) | 38.6 (16) | Melbourne poopoo | 91% |
| Ayo Dosunmu | PG/SG | 10 | 33.9 | +4.5 | 10 | **37.7** | 30.4 | 29.0 (4) | 32.1 (7) | 34.8 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 31.9 | +4.6 | 9 | **28.0** | 26.3 | 26.0 (3) | 23.0 (6) | 28.9 (15) | Dr White Slong | 60% |
| Joan Beringer | C | 10 | 17.4 | — | 1 | **18.8** | — | 15.5 (4) | 16.4 (7) | 19.3 (16) | Free agent | 2% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 7 | 18.3 | +5.2 | 0 | **14.7** | 9.4 | 3.0 (1) | 12.0 (4) | 11.9 (12) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 1 | 33.0 | +4.7 | 1 | **59.0** | 72.0 | 60.0 (4) | 66.9 (8) | 70.8 (15) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 1 | 33.0 | +3.8 | 1 | **59.0** | 34.0 | 48.0 (4) | 37.8 (8) | 35.1 (15) | Melbourne poopoo | 96% |
| Devin Vassell | SG/SF | 1 | 32.0 | +3.4 | 1 | **42.0** | 24.9 | 25.8 (4) | 29.5 (6) | 29.0 (13) | Team Nic Kerr | 40% |
| Julian Champagnie | SF/PF | 1 | 29.0 | +4.0 | 1 | **29.0** | 19.7 | 21.8 (4) | 23.0 (8) | 23.2 (15) | Free agent | 41% |
| De'Aaron Fox | PG/SG | 1 | 32.0 | +5.2 | 1 | **17.0** | 24.9 | 12.7 (3) | 24.7 (7) | 29.6 (14) | Matt Wright's Foxies | 94% |

### CLE

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Evan Mobley | Left Toe Sprain | 29 Nov | 33.3 | 39.9 | Matt Wright's Foxies |
| Nae'Qwan Tomlin | Back | 29 Nov | 15.7 | 15.5 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| James Harden | PG/SG | 4 | 36.2 | +4.9 | 4 | **50.2** | 30.6 | 50.2 (4) | 39.2 (8) | 36.1 (16) | Team Nic Kerr | 99% |
| Jarrett Allen | C | 4 | 30.8 | +11.4 | 4 | **34.0** | 25.0 | 34.0 (4) | 35.2 (6) | 34.5 (14) → 37.2 (13) | Dr White Slong | 89% |
| Tyrese Proctor | SG | 5 | 28.0 | +6.0 | 4 | **33.4** | 19.0 | 33.4 (5) | 27.0 (9) | 21.8 (16) | Free agent | 10% |
| Jaylon Tyson (out, ESPN est. back 23 Nov) | SG/SF | 2 | 32.0 | +9.0 | 2 | **28.0** | 5.0 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% |
| Thomas Bryant | C | 5 | 17.8 | +3.1 | 1 | **24.2** | 16.8 | 24.2 (5) | 22.8 (8) | 19.1 (11) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 23 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 25.0 | +3.0 | 9 | **23.3** | 20.0 | 17.8 (4) | 18.5 (6) | 26.9 (14) | Free agent | 27% |
| Kobe Sanders | SG | 10 | 22.5 | — | 1 | **17.2** | — | 11.2 (4) | 13.5 (6) | 17.5 (14) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Kingston Flemings (back strain; ESPN est. 22 Nov), Jock Landale (right hip inflammation; ESPN est. 22 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 2 | 36.0 | +4.5 | 2 | **49.0** | 42.6 | 40.8 (4) | 48.1 (7) | 41.8 (16) | Snow Time Lakers | 96% |
| Onyeka Okongwu | C | 2 | 35.0 | +3.0 | 2 | **35.5** | 40.8 | 38.2 (4) | 41.0 (7) | 36.8 (16) | Cream Abdul-Yammar | 87% |
| Aaron Wiggins | SG/SF | 2 | 30.0 | +4.5 | 2 | **30.5** | 22.6 | 22.2 (4) | 26.4 (7) | 26.7 (16) | Free agent | 34% |
| Corey Kispert | SG/SF | 2 | 16.5 | +3.9 | 0 | **17.0** | 14.4 | 20.3 (3) | 18.0 (4) | 14.9 (9) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.7 | +5.3 | 10 | **36.6** | 30.2 | 33.8 (4) | 35.9 (9) | 34.6 (17) | Snow Time Lakers | 80% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 29 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 10 | 37.9 | +3.9 | 10 | **55.6** | 38.6 | 63.5 (4) | 60.2 (8) | 49.0 (15) | Cream Abdul-Yammar | 96% |
| Anthony Black | PG/SG | 9 | 35.3 | +6.4 | 9 | **39.1** | 28.2 | 32.0 (4) | 39.4 (8) | 38.3 (12) | **us** | 69% |
| Wendell Carter Jr. | C | 10 | 32.9 | +7.5 | 10 | **30.9** | 23.0 | 27.0 (4) | 33.9 (8) | 32.3 (15) | Dr White Slong | 57% |
| Tristan da Silva | SF/PF | 8 | 31.1 | +9.7 | 2 | **24.8** | 17.2 | 22.0 (4) | 23.5 (6) | 24.7 (13) | Free agent | 10% |
| Jase Richardson | SG | 6 | 24.3 | +13.4 | 4 | **15.7** | 8.6 | — | 16.2 (4) | 15.3 (11) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Miller | SG/SF | 7 | 29.1 | +3.1 | 7 | **28.0** | 2.0 | 27.3 (3) | 23.5 (4) | 29.8 (13) | Matt Wright's Foxies | 86% |
| Royce O'Neale | SF/PF | 9 | 22.6 | +4.6 | 0 | **14.7** | 9.0 | 14.7 (3) | 16.2 (6) | 12.9 (15) | Free agent | 1% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 3 | 29.0 | +9.0 | 2 | **14.0** | 17.0 | — | — | 19.1 (9) | Free agent | 3% |
| Christian Anderson | PG | 9 | 15.9 | — | 0 | **13.4** | — | 19.3 (3) | 15.2 (6) | 10.0 (14) | Free agent | 0% |
| Tidjane Salaun | PF | 9 | 13.3 | +3.3 | 0 | **10.4** | 13.0 | 3.7 (3) | 9.3 (6) | 11.6 (14) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Norman Powell | SG/SF | 5 | 30.6 | +3.3 | 5 | **36.2** | 16.3 | 36.2 (5) | 36.2 (5) | 30.1 (13) → 32.2 (12) | Matt Wright's Foxies | 81% |
| Isaac Okoro | SG/SF | 5 | 31.6 | +11.2 | 5 | **29.4** | 10.4 | 29.4 (5) | 24.6 (7) | 16.6 (15) | Free agent | 2% |
| Buddy Hield | SG/SF | 5 | 21.2 | +8.9 | 0 | **23.4** | 15.7 | 23.4 (5) | 23.4 (5) | 16.8 (13) | Free agent | 1% |
| Nic Claxton | C | 4 | 22.5 | +5.5 | 1 | **20.5** | 29.0 | 20.5 (4) | 23.3 (6) | 23.3 (6) | Free agent | 40% |
| Zach Collins | C | 3 | 18.0 | +10.8 | 1 | **18.0** | 6.0 | 18.7 (3) | 15.5 (4) | 9.4 (10) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 22.3 | — | 0 | **28.5** | — | 27.8 (4) | 28.5 (6) | 26.6 (11) | Free agent | 3% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 24 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 30.8 | +12.8 | 9 | **41.8** | 45.0 | 45.8 (4) | 44.4 (7) | 38.1 (13) | Lauri Birds | 83% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 6 | 32.8 | +15.8 | 6 | **33.8** | 13.0 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 40% |
| Paul Reed | PF/C | 9 | 26.8 | +3.8 | 4 | **31.4** | 25.0 | 35.5 (4) | 32.6 (7) | 33.7 (14) | Lauri Birds | 36% |
| Javonte Green | SF | 9 | 20.1 | +8.1 | 1 | **17.6** | 5.0 | 19.0 (4) | 18.0 (7) | 14.9 (14) | Free agent | 0% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cam Spencer | PG/SG | 4 | 26.8 | +3.8 | 3 | **33.2** | 29.8 | 37.6 (5) | 31.4 (8) | 29.9 (16) | Lauri Birds | 36% |
| Javon Small (out, ESPN est. back 23 Nov) | PG | 4 | 24.0 | +3.0 | 0 | **24.2** | 25.0 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 2% |
| Olivier-Maxence Prosper | PF | 4 | 16.8 | +9.2 | 0 | **13.2** | 10.2 | 16.0 (5) | 11.9 (7) | 10.4 (10) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 36.7 | +6.1 | 10 | **42.8** | 30.4 | 35.0 (4) | 41.6 (7) | 39.7 (15) | Team Nic Kerr | 91% |
| De'Andre Hunter | SF/PF | 8 | 35.6 | +8.0 | 8 | **25.0** | 23.9 | 38.0 (3) | 30.8 (5) | 23.8 (13) | Free agent | 6% |
| Leaky Black | SF | 9 | 22.4 | — | 1 | **22.0** | — | 19.0 (4) | 20.7 (7) | 19.1 (11) | Free agent | 0% |
| Dylan Cardwell | C | 8 | 16.1 | — | 2 | **18.5** | — | 15.2 (4) | 18.4 (7) | 18.5 (8) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 16.8 | — | 0 | **12.2** | — | 11.8 (4) | 11.4 (7) | 10.6 (15) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brayden Burries | SG | 5 | 29.2 | +5.4 | 5 | **32.8** | 19.4 | 26.5 (4) | 28.2 (8) | 22.8 (16) | Free agent | 10% |
| Kasparas Jakucionis | PG | 5 | 21.2 | +9.7 | 0 | **31.6** | 9.0 | 44.7 (3) | 24.6 (7) | 20.4 (15) | Free agent | 10% |
| Pete Nance | PF | 1 | 28.0 | +24.0 | 1 | **22.0** | 5.0 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% |
| Kel'el Ware | C | 5 | 19.6 | +3.2 | 1 | **20.2** | 17.8 | 26.8 (4) | 20.6 (8) | 22.9 (16) | Free agent | 52% |
| AJ Green | SG | 4 | 17.0 | +4.6 | 0 | **14.2** | 6.8 | 5.7 (3) | 7.6 (7) | 11.0 (15) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 32.7 | +5.2 | 10 | **34.5** | 23.1 | 41.0 (4) | 32.9 (7) | 32.8 (14) | Waivers | 46% |
| Trevon Brazile | SF/PF | 10 | 16.2 | — | 0 | **14.4** | — | 10.8 (4) | 11.7 (7) | 16.7 (14) | Free agent | 2% |
| Spencer Jones | SF/PF | 7 | 17.9 | — | 0 | **10.1** | — | 7.8 (4) | 10.1 (7) | 10.1 (7) | Free agent | 0% |

## Every injury

All 107 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 314 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 314 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 222 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 132 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 132 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 116 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 101 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 101 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 101 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 101 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 96 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 74 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 71 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 58 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 52 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 44 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 42 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 42 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 42 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 42 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 42 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 30 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 28 | Free agent |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 23 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 23 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 22 | Lauri Birds |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 22 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 22 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 22 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 22 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 21 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 21 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 21 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 12 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 12 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 12 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 12 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 10 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 10 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 10 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 8 | Dr White Slong |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 8 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 8 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 8 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 8 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 8 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 8 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 8 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 6 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 6 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 6 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 6 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 6 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 6 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 6 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 27 Nov | 6 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 6 | Free agent |
| Tobe Awaka | CHI | Out | Back | 25 Nov | 4 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 4 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 4 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 4 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 3 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 3 | **us** |
| Ryan Dunn | PHX | Out | Right Quadriceps | 23 Nov | 2 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 2 | — |
| Jaylon Tyson | CLE | Out | Right Ankle | 23 Nov | 2 | Free agent |
| Jaylen Brown | PHI | Out | Left Hamstring | 23 Nov | 2 | Snow Time Lakers |
| Javon Small | MEM | Out | Personal | 23 Nov | 2 | Free agent |
| Grayson Allen | CHA | Out | Concussion | 23 Nov | 2 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 23 Nov | 2 | Free agent |
| Grant Nelson | BKN | Out | Right Ankle Sprain | 23 Nov | 2 | — |
| Dean Wade | PHI | Out | Left Hamstring Soreness | 23 Nov | 2 | Free agent |
| Collin Murray-Boyles | TOR | Out | Concussion | 23 Nov | 2 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 23 Nov | 2 | Free agent |
| Cameron Boozer | MEM | Out | Ankle | 23 Nov | 2 | Lauri Birds |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 23 Nov | 2 | Melbourne poopoo |
| Austin Reaves | LAL | Out | Left Heel Bruise | 23 Nov | 2 | Cream Abdul-Yammar |
| Adem Bona | PHI | Out | Back Sprain | 23 Nov | 2 | Free agent |
| T.J. McConnell | IND | Out | Left Hamstring | 22 Nov | 1 | Free agent |
| Ronald Holland II | DET | Out | Left Knee Bruise | 22 Nov | 1 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 22 Nov | 1 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Soreness | 22 Nov | 1 | Free agent |
| Myron Gardner | MIA | Day-To-Day | Hamstring | 22 Nov | 1 | Free agent |
| Kingston Flemings | ATL | Out | Back Strain | 22 Nov | 1 | Free agent |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 22 Nov | 1 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 22 Nov | 1 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 22 Nov | 1 | Free agent |
| Jalen Smith | CHI | Out | Illness | 22 Nov | 1 | **us** |
| Felix Okpara | WSH | Out | Back Strain | 22 Nov | 1 | Free agent |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 22 Nov | 1 | Free agent |
| Draymond Green | GS | Day-To-Day | Rest | 22 Nov | 1 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring Strain | 22 Nov | 1 | Free agent |
| Alex Caruso | OKC | Out | Right Hip Soreness | 22 Nov | 1 | Free agent |
| Walter Clayton Jr. | DAL | Day-To-Day | Knee | 21 Nov | 0 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 21 Nov | 0 | Free agent |
| Tyrese Maxey | PHI | Day-To-Day | Right Foot Soreness | 21 Nov | 0 | Team Nic Kerr |
| Ty Jerome | MEM | Out | Right Hip | 21 Nov | 0 | Melbourne poopoo |
| Tobi Lawal | DAL | Day-To-Day | Right Groin | 21 Nov | 0 | Free agent |
| Precious Achiuwa | SAC | Out | Left Lower Leg Bruise | 21 Nov | 0 | Free agent |
| P.J. Washington | DAL | Day-To-Day | Shoulder | 21 Nov | 0 | Free agent |
| OG Anunoby | NY | Day-To-Day | Calf | 21 Nov | 0 | Cream Abdul-Yammar |
| Jerami Grant | MEM | Day-To-Day | Left Calf | 21 Nov | 0 | Free agent |
| Jayson Tatum | BOS | Day-To-Day | Rest | 21 Nov | 0 | Snow Time Lakers |
| Dominick Barlow | PHI | Out | Back Fracture | 21 Nov | 0 | Free agent |
| Derrick White | BOS | Day-To-Day | Left Shoulder | 21 Nov | 0 | Dr White Slong |
| Deni Avdija | POR | Day-To-Day | Foot | 21 Nov | 0 | Snow Time Lakers |
| Nolan Traore | BKN | Out | Right Hamstring | 20 Nov | -1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-21 07:21 UTC.
