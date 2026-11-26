# Injury Watch: 26 Nov 2026

- Generated 2026-11-26 06:14 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 93 players in ESPN's injury feed. 32 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1103 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (23 Nov–29 Nov) / next week (30 Nov–06 Dec).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 26.0 (L7 32.6), Neemias Queta 28.5 (L7 37.8), Myles Turner 28.6 (L7 35.8), Brook Lopez 29.1 (L7 23.5), Trey Murphy III 31.1 (L7 31.5). A pickup at or above **31.1** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Jakob Poeltl** | TOR | RJ Barrett (13 Dec); also out: Kawhi Leonard (03 Dec) | 3 | 29.7 | +5.0 | **38.7** | 27.4 | 38.7 (3) | 27.9 (7) | 30.8 (12) | Free agent | 37% | 2 / 2 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (02 Dec) | 8 | 37.1 | +9.5 | **32.9** | 26.1 | 36.0 (5) | 35.1 (7) | 29.6 (13) | Free agent | 21% | 1 / 2 |
| **Allen Graves** | TOR | RJ Barrett (13 Dec); also out: Kawhi Leonard (03 Dec) | 3 | 31.7 | +17.0 | **31.3** | 16.2 | 31.3 (3) | 20.9 (7) | 14.1 (14) | Free agent | 1% | 2 / 2 |
| **Ja'Kobe Walter** | TOR | RJ Barrett (13 Dec); also out: Kawhi Leonard (03 Dec) | 3 | 35.7 | +3.4 | **30.7** | 25.5 | 30.7 (3) | 26.6 (7) | 23.6 (14) | Free agent | 12% | 2 / 2 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 8 | 25.0 | +6.8 | **29.8** | 21.2 | 33.0 (5) | 29.8 (8) | 23.0 (13) | Free agent | 7% | 1 / 2 |
| **Noah Clowney** | BKN | Nolan Traore (27 Jan) | 3 | 24.0 | +3.1 | **29.3** | 17.2 | 18.8 (4) | 24.4 (7) | 18.0 (14) | Free agent | 0% | 2 / 2 |
| **Grayson Allen** (out, ESPN est. back 28 Nov) | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 4 | 28.8 | +5.8 | **29.0** | 26.8 | — | 27.5 (2) | 26.3 (10) | Free agent | 18% | 1 / 2 |
| **Mo Bamba** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 10 | 23.4 | — | **28.3** | 27.9 | 20.0 (4) | 29.1 (9) | 27.9 (15) | Waivers | 13% | 2 / 2 |
| **Julian Champagnie** | SA | Dylan Harper (13 Dec); also out: Tobias Harris (03 Dec) | 4 | 30.2 | +3.6 | **27.8** | 24.4 | 27.8 (4) | 25.1 (8) | 23.2 (16) | Free agent | 43% | 2 / 2 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (26 Dec); also out: Jalen Duren (30 Nov) | 4 | 34.8 | +17.8 | **27.8** | 29.8 | — | 16.0 (2) | 29.7 (9) | Free agent | 36% | 2 / 2 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Moses Moody (01 Dec) | 6 | 21.8 | +7.8 | **27.7** | 23.3 | 35.2 (4) | 26.7 (7) | 23.0 (15) | Free agent | 7% | 2 / 1 |
| **Kenrich Williams** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 25.0 | +9.6 | **27.4** | 21.3 | 33.8 (5) | 28.3 (9) | 23.9 (16) | Free agent | 4% | 1 / 2 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 8 | 21.1 | — | **26.5** | 25.7 | 23.8 (4) | 26.5 (8) | 26.3 (11) | Free agent | 3% | 2 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 8 | 32.2 | +8.2 | **26.4** | 17.4 | 23.8 (5) | 24.1 (9) | 19.2 (15) | Free agent | 2% | 1 / 2 |
| **Jaxson Hayes** (day to day, ESPN est. back 27 Nov) | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 7 | 22.0 | +5.2 | **26.0** | 27.1 | 26.3 (3) | 24.8 (6) | 24.9 (12) | Free agent | 10% | 2 / 2 |
| **Luguentz Dort** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 3 | 28.3 | +4.0 | **24.7** | 20.0 | 24.7 (3) | 20.8 (5) | 20.5 (14) | Free agent | 3% | 2 / 2 |
| **Coby White** | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 8 | 22.6 | +5.6 | **24.0** | 20.3 | 30.3 (3) | 28.7 (6) | 20.3 (10) | Free agent | 60% | 1 / 2 |
| **Kingston Flemings** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 1 | 27.0 | +3.8 | **24.0** | 19.9 | 24.0 (1) | 12.0 (2) | 22.3 (10) | Free agent | 4% | 2 / 2 |
| **Gui Santos** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Moses Moody (01 Dec) | 6 | 21.2 | +6.2 | **23.5** | 17.5 | 26.2 (4) | 19.9 (7) | 17.0 (12) | Free agent | 1% | 2 / 1 |
| **Kris Murray** | MEM | Scotty Pippen Jr. (12 Dec), Cameron Boozer (21 Dec), Jerami Grant (12 Dec), GG Jackson (18 Jan) | 3 | 25.3 | +19.2 | **22.7** | 10.7 | 14.8 (5) | 13.2 (8) | 10.9 (14) | Free agent | 0% | 2 / 2 |
| **Nic Claxton** | CHI | Caleb Wilson (13 Dec) | 6 | 23.7 | +6.7 | **22.3** | 24.0 | 26.2 (4) | 24.0 (7) | 24.0 (8) | Free agent | 38% | 1 / 2 |
| **Christian Anderson** | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 8 | 20.6 | +11.6 | **22.0** | 14.1 | 30.7 (3) | 26.3 (6) | 16.8 (13) | Free agent | 1% | 1 / 2 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Shaedon Sharpe (02 Mar); also out: Ja Morant (01 Dec) | 10 | 27.2 | +11.0 | **21.7** | 20.1 | 27.5 (4) | 22.8 (9) | 19.6 (16) | Free agent | 1% | 2 / 2 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Ben Sheppard (02 Jan) | 10 | 21.2 | — | **21.4** | 22.5 | 18.0 (4) | 19.7 (7) | 23.2 (15) | Free agent | 4% | 2 / 2 |
| **Bennett Stirtz** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 21.8 | — | **21.0** | 17.4 | 26.4 (5) | 21.0 (9) | 20.3 (16) | Free agent | 2% | 1 / 2 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Moses Moody (01 Dec) | 6 | 23.5 | +7.8 | **20.2** | 15.4 | 21.2 (4) | 19.6 (7) | 15.0 (14) | Free agent | 1% | 2 / 1 |
| **Keon Ellis** | BKN | Nolan Traore (27 Jan) | 3 | 21.7 | +9.5 | **20.0** | 15.8 | 11.2 (4) | 14.6 (7) | 13.5 (13) | Free agent | 1% | 2 / 2 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Zach Edey** | MEM | Left Ankle Soreness | 27 Nov | 1 | 24.9 | 24.5 (4) | 25.7 (6) | 23.5 (13) | 33.2 | 39.5 | Free agent | 42% | 2 / 2 |
| **Dejounte Murray** | NO | Ankle | 27 Nov | 1 | 30.6 | — | 13.0 (1) | 21.7 (6) | 39.0 | 36.5 | Free agent | 72% | 2 / 2 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 5 | 33.8 | — | — | 28.0 (2) | 37.5 | 36.0 | Free agent | 80% | 2 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 3 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 2 |
| **Norman Powell** | CHI | Right Hamstring Strain | 28 Nov | 2 | 30.1 | 28.0 (2) | 36.2 (5) | 30.7 (10) → 33.7 (9) | 36.0 | 33.0 | Free agent | 76% | 1 / 2 |
| **Grayson Allen** | CHA | Concussion | 28 Nov | 2 | 26.8 | — | 27.5 (2) | 26.3 (10) | 26.6 | 31.2 | Free agent | 18% | 1 / 2 |
| **Mitchell Robinson** | BOS | Illness | 27 Nov | 1 | 18.6 | 13.0 (1) | 14.2 (5) | 18.7 (12) | 30.3 | 28.2 | Free agent | 10% | 2 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 7 | — | — | — | — | 30.1 | 28.0 | Free agent | 39% | 2 / 2 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 1 | 29.8 | — | 16.0 (2) | 29.7 (9) | 21.6 | 23.1 | Free agent | 36% | 2 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 02 Dec | 6 | — | — | — | — | — | 28.1 | Free agent | 2% | 1 / 2 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 1 | 8.8 | — | -3.0 (1) | 6.6 (9) | 25.1 | 27.6 | Free agent | 6% | 2 / 2 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 1 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 1 / 2 |
| **Jaxson Hayes** | UTAH | Left Knee | 27 Nov | 1 | 27.1 | 26.3 (3) | 24.8 (6) | 24.9 (12) | 16.5 | 20.2 | Free agent | 10% | 2 / 2 |
| **Jock Landale** | ATL | Right Hip Inflammation | 27 Nov | 1 | 16.8 | — | 19.0 (1) | 16.3 (6) → 19.6 (5) | — | 25.8 | Free agent | 0% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 3 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 2 / 2 |
| **T.J. McConnell** | IND | Left Hamstring | 27 Nov | 1 | 20.0 | 20.0 (2) | 24.6 (5) | 20.0 (7) | 24.4 | 25.5 | Free agent | 7% | 2 / 2 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.1.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 1 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 1 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 3 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 2 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 3 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 02 Dec | 6 | — (—) | 28.1 (74) | Free agent | 2% | 1 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 7 | 30.1 (30.5) | 28.0 (63) | Free agent | 39% | 2 / 2 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 37 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 2 / 1 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 37 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 2 / 1 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 03 Jan | 38 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 2 / 2 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 69 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 2 / 2 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 96 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 2 / 2 |

## Our injured players

- **Jalen Smith** (CHI): Day-To-Day, Illness; ESPN est. back 28 Nov.
- **Cade Cunningham** (DET): Day-To-Day, Knee; ESPN est. back 27 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 30 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 03 Dec.

## Who takes the minutes, team by team

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Cameron Boozer | Right Ankle Sprain | 21 Dec | 31.7 | 38.9 | Waivers |
| Jerami Grant | Left Calf | 12 Dec | 29.8 | 20.3 | Free agent |
| Scotty Pippen Jr. | Back Soreness | 12 Dec | 25.1 | 14.2 | Free agent |
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Murray | PF | 3 | 25.3 | +19.2 | 2 | **22.7** | 6.3 | 14.8 (5) | 13.2 (8) | 10.9 (14) | Free agent | 0% |
| Olivier-Maxence Prosper | PF | 3 | 20.3 | +7.2 | 0 | **10.7** | 13.3 | 12.6 (5) | 14.0 (8) | 10.5 (13) | Free agent | 0% |
| Taylor Hendricks | PF | 3 | 25.3 | +6.0 | 0 | **8.3** | 27.0 | 19.0 (5) | 21.4 (9) | 17.8 (13) | Free agent | 1% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Moses Moody (left knee surgery; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Charles Bassey | C | 6 | 21.8 | +7.8 | 4 | **27.7** | 25.0 | 35.2 (4) | 26.7 (7) | 23.0 (15) | Free agent | 7% |
| Gui Santos | SF | 6 | 21.2 | +6.2 | 1 | **23.5** | 6.7 | 26.2 (4) | 19.9 (7) | 17.0 (12) | Free agent | 1% |
| Will Richard | SG/SF | 6 | 23.5 | +7.8 | 1 | **20.2** | 15.0 | 21.2 (4) | 19.6 (7) | 15.0 (14) | Free agent | 1% |
| LJ Cryer | PG | 5 | 18.0 | +5.0 | 2 | **16.4** | 11.3 | 11.0 (3) | 16.8 (6) | 10.8 (12) | Free agent | 0% |
| Gary Payton II | SG | 6 | 15.2 | +3.7 | 0 | **13.7** | 12.0 | 19.5 (4) | 13.7 (6) | 12.4 (13) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara (out, ESPN est. back 28 Nov) | C | 7 | 26.9 | — | 5 | **39.7** | — | 50.0 (2) | 38.0 (6) | 33.6 (13) | Snow Time Lakers | 30% |
| Kenrich Williams | SF | 10 | 25.0 | +9.6 | 5 | **27.4** | 14.2 | 33.8 (5) | 28.3 (9) | 23.9 (16) | Free agent | 4% |
| Bennett Stirtz | PG | 10 | 21.8 | — | 1 | **21.0** | — | 26.4 (5) | 21.0 (9) | 20.3 (16) | Free agent | 2% |
| 5105800 |  | 4 | 21.5 | — | 0 | **12.2** | — | — | — | — | — | 0% |
| Micah Peavy | SF | 8 | 19.8 | — | 3 | **12.0** | — | 13.8 (4) | 10.4 (7) | 11.2 (13) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 03 Jan | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.9 | +3.2 | 10 | **49.3** | 29.7 | 58.8 (4) | 51.4 (8) | 43.8 (16) | Melbourne poopoo | 93% |
| Ayo Dosunmu | PG/SG | 10 | 32.9 | +3.5 | 10 | **32.4** | 30.4 | 28.0 (4) | 30.8 (8) | 35.3 (16) | Cream Abdul-Yammar | 85% |
| Jonathan Kuminga | SF/PF | 9 | 30.8 | +3.5 | 9 | **22.9** | 26.3 | 26.5 (4) | 25.9 (7) | 26.7 (15) | Dr White Slong | 62% |
| Joan Beringer | C | 10 | 16.4 | — | 0 | **19.0** | — | 21.0 (4) | 21.2 (8) | 21.2 (16) | Free agent | 1% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 10 | 23.4 | — | 4 | **28.3** | — | 20.0 (4) | 29.1 (9) | 27.9 (15) | Waivers | 13% |
| Jaxson Hayes (day to day, ESPN est. back 27 Nov) | C | 7 | 22.0 | +5.2 | 6 | **26.0** | 16.5 | 26.3 (3) | 24.8 (6) | 24.9 (12) | Free agent | 10% |
| Svi Mykhailiuk | SG | 10 | 22.7 | — | 0 | **17.8** | — | 28.0 (4) | 20.0 (9) | 13.1 (16) | Free agent | 1% |
| Josh Green | SG | 10 | 22.5 | +4.2 | 9 | **13.0** | 11.4 | 18.5 (4) | 13.2 (9) | 11.5 (16) | Free agent | 0% |
| Josh Okogie | SF | 10 | 17.9 | — | 2 | **11.4** | — | 4.2 (4) | 12.6 (9) | 12.2 (16) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 12 Dec | 30.0 | 19.1 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Moussa Diabate | PF/C | 6 | 33.2 | +6.7 | 6 | **40.8** | 28.5 | 48.0 (3) | 40.8 (6) | 38.7 (12) | Team Nic Kerr | 53% |
| Grayson Allen (out, ESPN est. back 28 Nov) | PG/SG | 4 | 28.8 | +5.8 | 3 | **29.0** | 26.5 | — | 27.5 (2) | 26.3 (10) | Free agent | 18% |
| Coby White | PG/SG | 8 | 22.6 | +5.6 | 8 | **24.0** | 6.5 | 30.3 (3) | 28.7 (6) | 20.3 (10) | Free agent | 60% |
| Christian Anderson | PG | 8 | 20.6 | +11.6 | 0 | **22.0** | 17.0 | 30.7 (3) | 26.3 (6) | 16.8 (13) | Free agent | 1% |
| Sion James | SF | 8 | 29.6 | +3.6 | 6 | **17.4** | 22.5 | 15.3 (3) | 14.7 (6) | 16.9 (14) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Ja Morant (left hamstring; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 10 | 27.2 | +11.0 | 9 | **21.7** | 10.6 | 27.5 (4) | 22.8 (9) | 19.6 (16) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 2 | 22.0 | — | 0 | **19.5** | — | — | 14.0 (1) | 10.5 (6) | Free agent | 0% |
| Jayson Kent | PF | 8 | 12.6 | — | 2 | **9.0** | — | 6.0 (4) | 8.6 (7) | 9.0 (8) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 21.2 | — | 2 | **21.4** | — | 18.0 (4) | 19.7 (7) | 23.2 (15) | Free agent | 4% |
| Jalen Slawson | SF | 9 | 12.7 | — | 0 | **21.1** | — | 31.5 (4) | 24.0 (7) | 18.9 (14) | Free agent | 1% |
| Braden Smith | PG | 7 | 16.7 | — | 4 | **17.7** | — | 22.0 (4) | 22.0 (4) | 15.8 (12) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Jock Landale (right hip inflammation; ESPN est. 27 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 3 | 37.0 | +4.9 | 3 | **52.0** | 44.9 | 53.3 (3) | 45.0 (5) | 41.0 (14) | Snow Time Lakers | 97% |
| Luguentz Dort | SG/SF | 3 | 28.3 | +4.0 | 0 | **24.7** | 21.4 | 24.7 (3) | 20.8 (5) | 20.5 (14) | Free agent | 3% |
| Kingston Flemings | PG/SG | 1 | 27.0 | +3.8 | 1 | **24.0** | 18.2 | 24.0 (1) | 12.0 (2) | 22.3 (10) | Free agent | 4% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.7 | +5.3 | 10 | **34.1** | 30.2 | 38.2 (4) | 35.4 (8) | 36.5 (16) | Snow Time Lakers | 82% |
| AJ Dybantsa | SF | 10 | 35.7 | +3.5 | 10 | **32.4** | 32.9 | 43.2 (4) | 33.8 (8) | 31.1 (15) | Dr White Slong | 86% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Kawhi Leonard (left knee inflammation; ESPN est. 03 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Scottie Barnes | SG/SF | 2 | 37.5 | +3.5 | 2 | **61.5** | 44.0 | 61.5 (2) | 55.2 (4) | 53.3 (9) | **us** | 99% |
| Jakob Poeltl | C | 3 | 29.7 | +5.0 | 3 | **38.7** | 30.1 | 38.7 (3) | 27.9 (7) | 30.8 (12) | Free agent | 37% |
| Allen Graves | SF | 3 | 31.7 | +17.0 | 2 | **31.3** | 11.0 | 31.3 (3) | 20.9 (7) | 14.1 (14) | Free agent | 1% |
| Ja'Kobe Walter | SG | 3 | 35.7 | +3.4 | 3 | **30.7** | 19.0 | 30.7 (3) | 26.6 (7) | 23.6 (14) | Free agent | 12% |
| Trayce Jackson-Davis | PF | 3 | 12.7 | +3.7 | 0 | **16.0** | 18.5 | 16.0 (3) | 16.0 (3) | 15.3 (9) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 4898010 |  | 1 | 22.0 | +20.0 | 0 | **31.0** | 11.0 | — | — | — | — | 0% |
| Buddy Hield | SG/SF | 8 | 25.0 | +6.8 | 3 | **29.8** | 16.9 | 33.0 (5) | 29.8 (8) | 23.0 (13) | Free agent | 7% |
| Isaac Okoro | SG/SF | 8 | 32.2 | +8.2 | 8 | **26.4** | 12.5 | 23.8 (5) | 24.1 (9) | 19.2 (15) | Free agent | 2% |
| Nic Claxton | C | 6 | 23.7 | +6.7 | 2 | **22.3** | 29.0 | 26.2 (4) | 24.0 (7) | 24.0 (8) | Free agent | 38% |
| Zach Collins | C | 5 | 18.0 | +15.0 | 1 | **15.8** | 6.0 | 15.2 (4) | 14.2 (6) | 10.5 (10) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |

Last 10 games: 4 game(s) without them, 6 with them.

Also out in those games, so part of the gain is theirs: Tobias Harris (left calf strain; ESPN est. 03 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 3 | 33.3 | +4.8 | 3 | **87.0** | 70.2 | 87.0 (3) | 74.4 (7) | 77.6 (15) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 4 | 33.2 | +4.2 | 4 | **47.5** | 34.7 | 47.5 (4) | 42.9 (8) | 36.0 (16) | Melbourne poopoo | 97% |
| Devin Vassell | SG/SF | 4 | 32.5 | +4.5 | 4 | **32.0** | 23.8 | 31.8 (4) | 26.9 (7) | 28.9 (14) | Team Nic Kerr | 42% |
| Julian Champagnie | SF/PF | 4 | 30.2 | +3.6 | 4 | **27.8** | 22.5 | 27.8 (4) | 25.1 (8) | 23.2 (16) | Free agent | 43% |
| Harrison Barnes | SF/PF | 4 | 19.5 | +3.2 | 2 | **10.8** | 9.2 | 10.8 (4) | 9.2 (8) | 10.5 (14) | Free agent | 0% |

### BKN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Nolan Traore | Right Hamstring Strain | 27 Jan | 25.0 | 24.9 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Noah Clowney | PF | 3 | 24.0 | +3.1 | 0 | **29.3** | 14.4 | 18.8 (4) | 24.4 (7) | 18.0 (14) | Free agent | 0% |
| Keon Ellis | SG/SF | 3 | 21.7 | +9.5 | 0 | **20.0** | 10.2 | 11.2 (4) | 14.6 (7) | 13.5 (13) | Free agent | 1% |
| Mikel Brown Jr. | PG | 2 | 26.0 | +3.7 | 2 | **19.5** | 18.7 | 17.8 (4) | 16.2 (6) | 18.4 (11) | Free agent | 9% |
| Chaney Johnson | SF | 1 | 15.0 | +6.5 | 0 | **14.0** | 5.8 | 12.0 (1) | 8.8 (4) | 10.1 (11) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 8 | 21.1 | — | 0 | **26.5** | — | 23.8 (4) | 26.5 (8) | 26.3 (11) | Free agent | 3% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 26 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 30 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 32.7 | +14.7 | 9 | **45.9** | 45.0 | 43.5 (4) | 53.3 (7) | 41.8 (14) | Lauri Birds | 85% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 4 | 34.8 | +17.8 | 4 | **27.8** | 13.0 | — | 16.0 (2) | 29.7 (9) | Free agent | 36% |
| Javonte Green | SF | 9 | 20.4 | +8.4 | 1 | **18.0** | 5.0 | 24.5 (4) | 18.3 (7) | 15.9 (14) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Bradley Beal (right knee inflammation; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yanic Konan Niederhauser | C | 4 | 13.2 | — | 0 | **11.8** | — | 11.8 (4) | 11.8 (4) | 11.8 (4) | Free agent | 1% |
| Kobe Sanders | SG | 10 | 16.9 | — | 0 | **10.5** | — | 7.5 (4) | 11.8 (8) | 15.4 (14) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 02 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 36.1 | +5.5 | 10 | **37.0** | 30.4 | 34.4 (5) | 33.2 (8) | 39.7 (15) | Team Nic Kerr | 92% |
| De'Andre Hunter | SF/PF | 8 | 37.1 | +9.5 | 8 | **32.9** | 23.9 | 36.0 (5) | 35.1 (7) | 29.6 (13) | Free agent | 21% |
| Leaky Black | SF | 10 | 19.2 | — | 1 | **17.4** | — | 10.0 (5) | 14.0 (8) | 18.4 (13) | Free agent | 0% |
| Dylan Cardwell | C | 10 | 14.2 | — | 2 | **14.5** | — | 7.8 (5) | 12.2 (8) | 14.9 (11) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 16.8 | — | 1 | **10.3** | — | 8.8 (5) | 9.4 (8) | 10.3 (15) | Free agent | 0% |

## Every injury

All 93 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 309 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 309 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 217 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 127 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 111 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 96 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 96 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 96 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 96 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 91 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 69 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 66 | Free agent |
| Nolan Traore | BKN | Out | Right Hamstring Strain | 27 Jan | 62 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 53 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 47 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 39 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 03 Jan | 38 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 37 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 37 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 37 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 37 | Free agent |
| Taurean Prince | DET | Out | Right Knee Surgery | 26 Dec | 30 | Free agent |
| Cameron Boozer | MEM | Out | Right Ankle Sprain | 21 Dec | 25 | Waivers |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 25 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 23 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 18 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 17 | Lauri Birds |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 17 | Dr White Slong |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 13 Dec | 17 | Free agent |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 17 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 17 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 16 | Lauri Birds |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 12 Dec | 16 | Free agent |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 16 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 16 | Free agent |
| Jerami Grant | MEM | Out | Left Calf | 12 Dec | 16 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 12 Dec | 16 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 7 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 7 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 7 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 7 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 02 Dec | 6 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 5 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 5 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 5 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 30 Nov | 4 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 30 Nov | 4 | **us** |
| Zach LaVine | SAC | Day-To-Day | Right Knee Soreness | 29 Nov | 3 | Dr White Slong |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 3 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 29 Nov | 3 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 3 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 3 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 29 Nov | 3 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 3 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 3 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 3 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 3 | Free agent |
| Ryan Kalkbrenner | CHA | Day-To-Day | Left Hip Soreness | 28 Nov | 2 | Free agent |
| Norman Powell | CHI | Out | Right Hamstring Strain | 28 Nov | 2 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Strain | 28 Nov | 2 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 28 Nov | 2 | Free agent |
| Jalen Smith | CHI | Day-To-Day | Illness | 28 Nov | 2 | **us** |
| Grayson Allen | CHA | Out | Concussion | 28 Nov | 2 | Free agent |
| Aday Mara | OKC | Out | Right Lower Leg Bruise | 28 Nov | 2 | Snow Time Lakers |
| Zach Edey | MEM | Day-To-Day | Left Ankle Soreness | 27 Nov | 1 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 1 | Free agent |
| Tobi Lawal | DAL | Out | Right Groin | 27 Nov | 1 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 1 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Left Hamstring | 27 Nov | 1 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 1 | Free agent |
| OG Anunoby | NY | Out | Left Calf Soreness | 27 Nov | 1 | Cream Abdul-Yammar |
| Nate Bittle | TOR | Out | Right Foot Fracture | 27 Nov | 1 | — |
| Moritz Wagner | BKN | Out | Left Knee Soreness | 27 Nov | 1 | Free agent |
| Mitchell Robinson | BOS | Out | Illness | 27 Nov | 1 | Free agent |
| Miles McBride | NY | Day-To-Day | Left Groin Soreness | 27 Nov | 1 | Free agent |
| Larry Nance Jr. | IND | Day-To-Day | Right Ankle Soreness | 27 Nov | 1 | Free agent |
| LaMelo Ball | MIN | Day-To-Day | Left Ankle | 27 Nov | 1 | Cream Abdul-Yammar |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 27 Nov | 1 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Illness | 27 Nov | 1 | Dr White Slong |
| Jock Landale | ATL | Out | Right Hip Inflammation | 27 Nov | 1 | Free agent |
| Jaylen Brown | PHI | Day-To-Day | Left Hamstring | 27 Nov | 1 | Snow Time Lakers |
| Jaxson Hayes | UTAH | Day-To-Day | Left Knee | 27 Nov | 1 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 1 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 1 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 1 | Free agent |
| De'Aaron Fox | SA | Day-To-Day | Right Lower Leg Bruise | 27 Nov | 1 | Matt Wright's Foxies |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 1 | Free agent |
| Cade Cunningham | DET | Day-To-Day | Knee | 27 Nov | 1 | **us** |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 1 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 27 Nov | 1 | Cream Abdul-Yammar |
| Andre Drummond | NY | Day-To-Day | Head | 27 Nov | 1 | Free agent |
| Aaron Nesmith | IND | Day-To-Day | Foot | 27 Nov | 1 | Free agent |
| Julian Reese | NO | Day-To-Day | Right Knee | 25 Nov | -1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-26 06:14 UTC.
