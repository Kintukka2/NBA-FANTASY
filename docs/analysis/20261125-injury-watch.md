# Injury Watch: 25 Nov 2026

- Generated 2026-11-25 09:06 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 93 players in ESPN's injury feed. 34 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1102 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (23 Nov–29 Nov) / next week (30 Nov–06 Dec).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 25.7 (L7 33.0), Neemias Queta 28.5 (L7 37.8), Myles Turner 28.9 (L7 39.3), Brook Lopez 29.8 (L7 30.8), Trey Murphy III 31.1 (L7 31.5). A pickup at or above **31.1** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 29.7 | +5.0 | **38.7** | 27.4 | 32.5 (4) | 31.1 (8) | 28.2 (13) | Free agent | 37% | 2 / 2 |
| **Norman Powell** (out, ESPN est. back 28 Nov) | CHI | Caleb Wilson (13 Dec) | 5 | 30.6 | +8.6 | **36.2** | 30.1 | 28.0 (2) | 36.2 (5) | 30.7 (10) → 33.7 (9) | Free agent | 76% | 2 / 2 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 35.7 | +3.4 | **32.0** | 25.5 | 34.5 (4) | 25.1 (8) | 25.2 (15) | Free agent | 12% | 2 / 2 |
| **Mikel Brown Jr.** | BKN | Nolan Traore (27 Jan) | 1 | 29.0 | +6.0 | **32.0** | 19.0 | 21.3 (3) | 18.0 (5) | 19.5 (10) | Free agent | 8% | 3 / 2 |
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 3 | 31.7 | +17.0 | **31.3** | 16.2 | 26.0 (4) | 19.6 (8) | 15.9 (15) | Free agent | 1% | 2 / 2 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 7 | 24.7 | +16.7 | **30.6** | 21.0 | 35.2 (4) | 30.6 (7) | 22.9 (12) | Free agent | 6% | 2 / 2 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (02 Dec) | 8 | 37.0 | +9.4 | **30.5** | 25.6 | 36.5 (4) | 35.3 (6) | 27.8 (13) | Free agent | 18% | 2 / 2 |
| **Grayson Allen** (out, ESPN est. back 25 Nov) | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 4 | 28.8 | +3.4 | **29.0** | 26.8 | — | 36.0 (3) | 26.3 (10) | Free agent | 18% | 2 / 2 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov), Moses Moody (01 Dec) | 5 | 21.8 | +6.0 | **28.4** | 23.3 | 39.0 (3) | 28.4 (7) | 22.9 (14) | Free agent | 5% | 3 / 1 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (26 Dec); also out: Jalen Duren (30 Nov) | 4 | 34.8 | +17.8 | **27.8** | 29.8 | — | 21.7 (3) | 29.9 (10) | Free agent | 36% | 2 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 7 | 32.4 | +11.4 | **27.7** | 17.4 | 25.5 (4) | 25.0 (8) | 19.4 (14) | Free agent | 2% | 2 / 2 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 7 | 21.7 | — | **27.6** | 26.2 | 25.3 (3) | 27.6 (7) | 27.0 (10) | Free agent | 3% | 3 / 2 |
| **Jaxson Hayes** (day to day, ESPN est. back 27 Nov) | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 7 | 22.0 | +5.2 | **26.0** | 27.1 | 26.3 (3) | 24.8 (6) | 24.8 (13) | Free agent | 10% | 2 / 2 |
| **Kris Murray** | MEM | Scotty Pippen Jr. (12 Dec), Cameron Boozer (21 Dec), Jerami Grant (12 Dec), GG Jackson (18 Jan) | 2 | 22.0 | +14.9 | **25.5** | 10.3 | 14.2 (4) | 11.1 (8) | 10.4 (13) | Free agent | 0% | 3 / 2 |
| **Kenrich Williams** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 24.4 | +9.0 | **25.4** | 20.6 | 33.8 (4) | 27.6 (8) | 22.2 (16) | Free agent | 3% | 2 / 2 |
| **Luguentz Dort** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 3 | 28.3 | +4.0 | **24.7** | 20.0 | 24.7 (3) | 19.7 (6) | 20.5 (14) | Free agent | 3% | 2 / 2 |
| **Terrence Shannon Jr.** | MIN | Donte DiVincenzo (03 Jan), Anthony Edwards (21 Dec) | 8 | 23.9 | +3.2 | **24.0** | 22.1 | 24.8 (4) | 26.1 (7) | 23.1 (13) | Free agent | 8% | 3 / 2 |
| **Kingston Flemings** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 1 | 27.0 | +3.8 | **24.0** | 19.9 | 24.0 (1) | 14.3 (3) | 22.3 (10) | Free agent | 4% | 2 / 2 |
| **Bennett Stirtz** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar), Chet Holmgren (02 Jan) | 10 | 21.8 | — | **22.9** | 17.7 | 29.8 (4) | 22.0 (8) | 19.9 (16) | Free agent | 2% | 2 / 2 |
| **Coby White** | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 7 | 22.3 | +5.3 | **22.6** | 19.0 | 31.0 (3) | 26.3 (6) | 19.0 (9) | Free agent | 60% | 2 / 2 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov), Moses Moody (01 Dec) | 5 | 24.8 | +6.1 | **21.6** | 15.5 | 24.0 (3) | 20.7 (6) | 15.2 (13) | Free agent | 1% | 3 / 1 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Ben Sheppard (02 Jan) | 10 | 21.2 | — | **21.4** | 22.5 | 18.0 (4) | 21.5 (8) | 22.6 (16) | Free agent | 4% | 2 / 2 |
| **Isaiah Stewart** | MEM | Scotty Pippen Jr. (12 Dec), Cameron Boozer (21 Dec), Jerami Grant (12 Dec), GG Jackson (18 Jan) | 2 | 21.0 | +3.2 | **21.0** | 21.0 | 19.0 (3) | 18.8 (6) | 22.2 (12) | Free agent | 3% | 3 / 2 |
| **Christian Anderson** | CHA | Dennis Schroder (12 Dec), Kon Knueppel (12 Dec) | 7 | 19.6 | +11.1 | **20.6** | 12.9 | 25.0 (3) | 23.2 (6) | 15.6 (12) | Free agent | 0% | 2 / 2 |
| **Luke Kornet** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 3 | 18.0 | +3.3 | **20.3** | 14.8 | 18.8 (4) | 17.5 (8) | 16.0 (15) | Free agent | 1% | 3 / 2 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 2 | 30.6 | — | 15.0 (2) | 21.7 (6) | 39.0 | 36.5 | Free agent | 73% | 2 / 2 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 6 | 33.8 | — | — | 28.0 (2) | 37.5 | 36.0 | Free agent | 80% | 3 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 4 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 2 |
| **Norman Powell** | CHI | Right Hamstring Strain | 28 Nov | 3 | 30.1 | 28.0 (2) | 36.2 (5) | 30.7 (10) → 33.7 (9) | 36.0 | 33.0 | Free agent | 76% | 2 / 2 |
| **Grayson Allen** | CHA | Concussion | 25 Nov | 0 | 26.8 | — | 36.0 (3) | 26.3 (10) | 26.6 | 31.2 | Free agent | 18% | 2 / 2 |
| **Mitchell Robinson** | BOS | Illness | 27 Nov | 2 | 18.6 | 13.0 (1) | 14.2 (5) | 18.7 (12) | 30.3 | 28.2 | Free agent | 10% | 2 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 8 | — | — | — | — | 30.1 | 28.0 | Free agent | 39% | 3 / 2 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 2 | 29.8 | — | 21.7 (3) | 29.9 (10) | 21.6 | 23.1 | Free agent | 36% | 2 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 02 Dec | 7 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 2 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 2 | 8.8 | — | 0.0 (2) | 6.6 (9) | 25.1 | 27.6 | Free agent | 6% | 2 / 2 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 2 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 1 / 2 |
| **Jaxson Hayes** | UTAH | Left Knee | 27 Nov | 2 | 27.1 | 26.3 (3) | 24.8 (6) | 24.8 (13) | 16.5 | 20.2 | Free agent | 10% | 2 / 2 |
| **Jock Landale** | ATL | Right Hip Inflammation | 27 Nov | 2 | 16.8 | — | 18.0 (2) | 16.3 (6) → 19.6 (5) | — | 25.8 | Free agent | 0% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 4 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 3 / 2 |
| **T.J. McConnell** | IND | Left Hamstring | 27 Nov | 2 | 20.0 | 20.0 (2) | 21.2 (6) | 20.0 (7) | 24.4 | 25.5 | Free agent | 7% | 2 / 2 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.1.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 2 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 1 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 4 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 3 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 4 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 02 Dec | 7 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 2 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 8 | 30.1 (30.5) | 28.0 (63) | Free agent | 39% | 3 / 2 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 38 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 3 / 1 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 38 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 3 / 1 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 03 Jan | 39 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 3 / 2 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 70 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 3 / 2 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 97 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 3 / 2 |

## Our injured players

- **Jalen Smith** (CHI): Day-To-Day, Illness; ESPN est. back 25 Nov.
- **Cade Cunningham** (DET): Out, Knee; ESPN est. back 27 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 30 Nov.
- **Yaxel Lendeborg** (GS): Day-To-Day, Illness; ESPN est. back 25 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 03 Dec.

## Who takes the minutes, team by team

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Cameron Boozer | Right Ankle Sprain | 21 Dec | 31.7 | 38.9 | Lauri Birds |
| Jerami Grant | Left Calf | 12 Dec | 29.8 | 20.3 | Free agent |
| Scotty Pippen Jr. | Back Soreness | 12 Dec | 25.1 | 14.2 | Free agent |
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Murray | PF | 2 | 22.0 | +14.9 | 1 | **25.5** | 6.1 | 14.2 (4) | 11.1 (8) | 10.4 (13) | Free agent | 0% |
| Isaiah Stewart | PF/C | 2 | 21.0 | +3.2 | 0 | **21.0** | 17.8 | 19.0 (3) | 18.8 (6) | 22.2 (12) | Free agent | 3% |
| Jahmai Mashack | SG | 1 | 22.0 | +12.6 | 1 | **11.0** | 4.6 | 11.7 (3) | 6.6 (5) | 5.4 (8) | Free agent | 0% |
| Olivier-Maxence Prosper | PF | 2 | 21.0 | +8.1 | 0 | **9.0** | 11.9 | 12.2 (4) | 12.2 (8) | 10.2 (12) | Free agent | 0% |
| Taylor Hendricks | PF | 2 | 25.5 | +8.1 | 0 | **7.0** | 24.4 | 21.0 (4) | 22.6 (9) | 16.8 (13) | Free agent | 1% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

Also out in those games, so part of the gain is theirs: Brandon Williams (left hamstring strain; ESPN est. 25 Nov), Moses Moody (left knee surgery; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Charles Bassey | C | 5 | 21.8 | +6.0 | 3 | **28.4** | 26.6 | 39.0 (3) | 28.4 (7) | 22.9 (14) | Free agent | 5% |
| Will Richard | SG/SF | 5 | 24.8 | +6.1 | 1 | **21.6** | 15.0 | 24.0 (3) | 20.7 (6) | 15.2 (13) | Free agent | 1% |
| Gui Santos | SF | 5 | 20.6 | +5.6 | 1 | **19.4** | 6.7 | 20.3 (3) | 16.3 (7) | 14.5 (11) | Free agent | 1% |
| LJ Cryer | PG | 5 | 18.0 | +8.0 | 2 | **16.4** | 8.2 | 11.0 (3) | 16.6 (7) | 10.8 (12) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara (out, ESPN est. back 28 Nov) | C | 8 | 25.8 | — | 5 | **37.2** | — | 50.0 (2) | 38.0 (6) | 31.7 (14) | Snow Time Lakers | 31% |
| Kenrich Williams | SF | 10 | 24.4 | +9.0 | 6 | **25.4** | 14.2 | 33.8 (4) | 27.6 (8) | 22.2 (16) | Free agent | 3% |
| Bennett Stirtz | PG | 10 | 21.8 | — | 0 | **22.9** | — | 29.8 (4) | 22.0 (8) | 19.9 (16) | Free agent | 2% |
| 5105800 |  | 5 | 20.2 | — | 0 | **13.0** | — | — | — | — | — | 0% |
| Micah Peavy | SF | 8 | 18.9 | — | 2 | **12.9** | — | 15.7 (3) | 10.8 (6) | 11.5 (12) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Scottie Barnes | SG/SF | 2 | 37.5 | +3.5 | 2 | **61.5** | 44.7 | 53.3 (3) | 55.2 (4) | 49.2 (10) → 53.3 (9) | **us** | 99% |
| Jakob Poeltl | C | 3 | 29.7 | +5.0 | 3 | **38.7** | 30.4 | 32.5 (4) | 31.1 (8) | 28.2 (13) | Free agent | 37% |
| Ja'Kobe Walter | SG | 3 | 35.7 | +3.4 | 3 | **32.0** | 19.0 | 34.5 (4) | 25.1 (8) | 25.2 (15) | Free agent | 12% |
| Allen Graves | SF | 3 | 31.7 | +17.0 | 2 | **31.3** | 10.9 | 26.0 (4) | 19.6 (8) | 15.9 (15) | Free agent | 1% |
| Trayce Jackson-Davis | PF | 3 | 12.7 | +3.7 | 0 | **16.0** | 18.5 | 16.0 (3) | 18.2 (4) | 14.3 (10) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 03 Jan | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.9 | +3.2 | 10 | **45.1** | 29.7 | 53.5 (4) | 47.9 (7) | 41.1 (16) | Melbourne poopoo | 92% |
| Ayo Dosunmu | PG/SG | 10 | 32.8 | +3.4 | 10 | **33.6** | 30.4 | 33.2 (4) | 31.1 (7) | 34.2 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 30.8 | +3.5 | 9 | **26.2** | 26.3 | 30.7 (3) | 27.8 (6) | 27.8 (15) | Dr White Slong | 62% |
| Terrence Shannon Jr. | SG | 8 | 23.9 | +3.2 | 0 | **24.0** | 14.9 | 24.8 (4) | 26.1 (7) | 23.1 (13) | Free agent | 8% |
| Joan Beringer | C | 10 | 16.1 | — | 0 | **18.4** | — | 24.5 (4) | 21.4 (7) | 21.0 (16) | Free agent | 1% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 10 | 23.4 | — | 4 | **28.3** | — | 24.6 (5) | 29.1 (9) | 27.9 (15) | Team Nic Kerr | 14% |
| Jaxson Hayes (day to day, ESPN est. back 27 Nov) | C | 7 | 22.0 | +5.2 | 6 | **26.0** | 16.5 | 26.3 (3) | 24.8 (6) | 24.8 (13) | Free agent | 10% |
| Svi Mykhailiuk | SG | 10 | 22.7 | — | 0 | **17.8** | — | 28.2 (5) | 20.0 (9) | 12.5 (17) | Free agent | 1% |
| Josh Green | SG | 10 | 22.5 | +4.2 | 9 | **13.4** | 11.4 | 16.8 (5) | 13.2 (9) | 10.9 (17) | Free agent | 0% |
| Josh Okogie | SF | 10 | 17.9 | — | 2 | **11.4** | — | 9.2 (5) | 12.6 (9) | 12.0 (17) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 12 Dec | 30.0 | 19.1 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Moussa Diabate | PF/C | 5 | 32.2 | +5.2 | 5 | **40.4** | 31.7 | 43.3 (3) | 40.2 (5) | 38.2 (11) | Team Nic Kerr | 51% |
| Grayson Allen (out, ESPN est. back 25 Nov) | PG/SG | 4 | 28.8 | +3.4 | 3 | **29.0** | 35.3 | — | 36.0 (3) | 26.3 (10) | Free agent | 18% |
| Coby White | PG/SG | 7 | 22.3 | +5.3 | 7 | **22.6** | 6.5 | 31.0 (3) | 26.3 (6) | 19.0 (9) | Free agent | 60% |
| Christian Anderson | PG | 7 | 19.6 | +11.1 | 0 | **20.6** | 10.0 | 25.0 (3) | 23.2 (6) | 15.6 (12) | Free agent | 0% |
| Sion James (day to day, ESPN est. back 25 Nov) | SF | 7 | 30.1 | +6.8 | 5 | **18.3** | 17.0 | 15.7 (3) | 18.3 (6) | 17.4 (13) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama (day to day, ESPN est. back 25 Nov) | C | 2 | 32.5 | +4.4 | 2 | **90.5** | 68.6 | 80.3 (3) | 77.6 (7) | 77.4 (14) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 3 | 33.0 | +4.1 | 3 | **51.7** | 34.9 | 42.8 (4) | 41.1 (8) | 36.1 (15) | Melbourne poopoo | 97% |
| Luke Kornet | C | 3 | 18.0 | +3.3 | 1 | **20.3** | 15.4 | 18.8 (4) | 17.5 (8) | 16.0 (15) | Free agent | 1% |
| Ja'Kobi Gillespie | PG | 1 | 15.0 | — | 0 | **18.0** | — | 18.0 (1) | 18.0 (1) | 18.0 (1) | Free agent | 0% |
| Jordan McLaughlin | PG | 3 | 14.3 | +3.3 | 0 | **14.3** | 14.7 | 14.3 (3) | 16.1 (7) | 12.8 (11) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Ja Morant (left hamstring; ESPN est. 01 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 10 | 26.4 | +10.2 | 8 | **19.6** | 10.6 | 23.5 (4) | 20.8 (8) | 18.3 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | — | 0 | **16.7** | — | — | 14.0 (1) | 10.5 (6) | Free agent | 0% |
| Jayson Kent | PF | 7 | 13.6 | — | 2 | **10.3** | — | 11.0 (4) | 10.0 (6) | 10.3 (7) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 21.2 | — | 2 | **21.4** | — | 18.0 (4) | 21.5 (8) | 22.6 (16) | Free agent | 4% |
| Jalen Slawson | SF | 9 | 12.7 | — | 0 | **21.1** | — | 31.5 (4) | 24.0 (7) | 17.8 (15) | Free agent | 0% |
| Braden Smith | PG | 7 | 16.7 | — | 4 | **18.3** | — | 22.0 (4) | 18.4 (5) | 15.8 (12) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Jock Landale (right hip inflammation; ESPN est. 27 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 3 | 37.0 | +4.9 | 3 | **53.3** | 44.9 | 53.3 (3) | 46.5 (6) | 41.0 (14) | Snow Time Lakers | 97% |
| Luguentz Dort | SG/SF | 3 | 28.3 | +4.0 | 0 | **24.7** | 21.4 | 24.7 (3) | 19.7 (6) | 20.5 (14) | Free agent | 3% |
| Kingston Flemings | PG/SG | 1 | 27.0 | +3.8 | 1 | **24.0** | 18.2 | 24.0 (1) | 14.3 (3) | 22.3 (10) | Free agent | 4% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.7 | +5.3 | 10 | **34.1** | 30.2 | 38.2 (4) | 33.3 (9) | 36.5 (16) | Snow Time Lakers | 81% |
| AJ Dybantsa | SF | 10 | 35.7 | +3.5 | 10 | **32.4** | 32.9 | 43.2 (4) | 33.2 (9) | 31.1 (15) | Dr White Slong | 86% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jalen Smith (day to day, ESPN est. back 25 Nov) | PF/C | 5 | 28.0 | +5.7 | 5 | **45.8** | 35.7 | 42.0 (3) | 46.2 (6) | 38.4 (12) → 41.0 (11) | **us** | 53% |
| Norman Powell (out, ESPN est. back 28 Nov) | SG/SF | 5 | 30.6 | +8.6 | 5 | **36.2** | 4.0 | 28.0 (2) | 36.2 (5) | 30.7 (10) → 33.7 (9) | Free agent | 76% |
| 4898010 |  | 1 | 22.0 | +14.0 | 0 | **31.0** | 22.0 | — | — | — | — | 0% |
| Buddy Hield | SG/SF | 7 | 24.7 | +16.7 | 2 | **30.6** | 16.0 | 35.2 (4) | 30.6 (7) | 22.9 (12) | Free agent | 6% |
| Isaac Okoro | SG/SF | 7 | 32.4 | +11.4 | 7 | **27.7** | 12.3 | 25.5 (4) | 25.0 (8) | 19.4 (14) | Free agent | 2% |

### BKN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Nolan Traore | Right Hamstring Strain | 27 Jan | 25.0 | 24.9 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mikel Brown Jr. | PG | 1 | 29.0 | +6.0 | 1 | **32.0** | 18.1 | 21.3 (3) | 18.0 (5) | 19.5 (10) | Free agent | 8% |
| Keon Ellis | SG/SF | 2 | 21.0 | +7.0 | 0 | **18.5** | 11.4 | 7.3 (3) | 13.2 (6) | 14.8 (13) | Free agent | 1% |
| Chaney Johnson | SF | 1 | 15.0 | +3.7 | 0 | **14.0** | 7.4 | 12.0 (1) | 8.8 (4) | 10.2 (12) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 7 | 21.7 | — | 0 | **27.6** | — | 25.3 (3) | 27.6 (7) | 27.0 (10) | Free agent | 3% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 26 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 30 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 32.7 | +14.7 | 9 | **45.8** | 45.0 | 49.2 (5) | 49.4 (8) | 41.8 (14) | Lauri Birds | 85% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 4 | 34.8 | +17.8 | 4 | **27.8** | 13.0 | — | 21.7 (3) | 29.9 (10) | Free agent | 36% |
| Javonte Green | SF | 9 | 20.4 | +8.4 | 1 | **18.0** | 5.0 | 21.6 (5) | 17.1 (8) | 15.3 (15) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Bradley Beal (right knee inflammation; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kobe Sanders | SG | 10 | 20.2 | — | 1 | **15.6** | — | 11.8 (4) | 13.7 (7) | 17.0 (14) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 02 Dec).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 36.6 | +6.0 | 10 | **38.4** | 30.4 | 35.0 (4) | 33.4 (7) | 40.1 (15) | Team Nic Kerr | 92% |
| De'Andre Hunter | SF/PF | 8 | 37.0 | +9.4 | 8 | **30.5** | 23.9 | 36.5 (4) | 35.3 (6) | 27.8 (13) | Free agent | 18% |
| Leaky Black | SF | 10 | 19.4 | — | 1 | **18.0** | — | 10.5 (4) | 14.9 (7) | 17.8 (13) | Free agent | 0% |
| Dylan Cardwell | C | 10 | 14.6 | — | 2 | **15.8** | — | 8.2 (4) | 13.1 (7) | 15.8 (10) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 15.3 | — | 0 | **9.5** | — | 6.5 (4) | 8.1 (7) | 9.6 (15) | Free agent | 0% |

## Every injury

All 93 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 310 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 310 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 218 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 128 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 112 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 97 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 97 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 97 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 97 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 92 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 70 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 67 | Free agent |
| Nolan Traore | BKN | Out | Right Hamstring Strain | 27 Jan | 63 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 54 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 48 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 40 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 03 Jan | 39 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 38 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 38 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 38 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 38 | Free agent |
| Taurean Prince | DET | Out | Right Knee Surgery | 26 Dec | 31 | Free agent |
| Cameron Boozer | MEM | Out | Right Ankle Sprain | 21 Dec | 26 | Lauri Birds |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 26 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 24 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 19 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 18 | Lauri Birds |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 18 | Dr White Slong |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 13 Dec | 18 | Free agent |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 18 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 18 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 17 | Lauri Birds |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 12 Dec | 17 | Free agent |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 17 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 17 | Free agent |
| Jerami Grant | MEM | Out | Left Calf | 12 Dec | 17 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 12 Dec | 17 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 8 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 8 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 8 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 8 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 02 Dec | 7 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 6 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 6 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 6 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 30 Nov | 5 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 30 Nov | 5 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 4 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 29 Nov | 4 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 4 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 4 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 29 Nov | 4 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 4 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 4 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 4 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 4 | Free agent |
| Norman Powell | CHI | Out | Right Hamstring Strain | 28 Nov | 3 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Strain | 28 Nov | 3 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 28 Nov | 3 | Free agent |
| Aday Mara | OKC | Out | Right Lower Leg Bruise | 28 Nov | 3 | Snow Time Lakers |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 2 | Free agent |
| Tobi Lawal | DAL | Out | Right Groin | 27 Nov | 2 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 2 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Left Hamstring | 27 Nov | 2 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 2 | Free agent |
| OG Anunoby | NY | Out | Left Calf Soreness | 27 Nov | 2 | Cream Abdul-Yammar |
| Nate Bittle | TOR | Out | Right Foot Fracture | 27 Nov | 2 | — |
| Mitchell Robinson | BOS | Out | Illness | 27 Nov | 2 | Free agent |
| Larry Nance Jr. | IND | Day-To-Day | Right Ankle Soreness | 27 Nov | 2 | Free agent |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 27 Nov | 2 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Illness | 27 Nov | 2 | Dr White Slong |
| Jock Landale | ATL | Out | Right Hip Inflammation | 27 Nov | 2 | Free agent |
| Jaxson Hayes | UTAH | Day-To-Day | Left Knee | 27 Nov | 2 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 2 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 2 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 2 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 2 | Free agent |
| Cade Cunningham | DET | Out | Knee | 27 Nov | 2 | **us** |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 2 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 27 Nov | 2 | Cream Abdul-Yammar |
| Aaron Nesmith | IND | Day-To-Day | Foot | 27 Nov | 2 | Free agent |
| Yaxel Lendeborg | GS | Day-To-Day | Illness | 25 Nov | 0 | **us** |
| Victor Wembanyama | SA | Day-To-Day | Back | 25 Nov | 0 | Cream Abdul-Yammar |
| Sion James | CHA | Day-To-Day | Left Undisclosed | 25 Nov | 0 | Free agent |
| Ryan Kalkbrenner | CHA | Day-To-Day | Left Hip Soreness | 25 Nov | 0 | Free agent |
| Miles McBride | NY | Day-To-Day | Left Groin Soreness | 25 Nov | 0 | Free agent |
| Karl-Anthony Towns | NY | Day-To-Day | Knee | 25 Nov | 0 | Melbourne poopoo |
| Josh Hart | NY | Day-To-Day | Right Shoulder Sprain | 25 Nov | 0 | Dr White Slong |
| Jalen Smith | CHI | Day-To-Day | Illness | 25 Nov | 0 | **us** |
| Grayson Allen | CHA | Out | Concussion | 25 Nov | 0 | Free agent |
| Giannis Antetokounmpo | MIA | Day-To-Day | Groin | 25 Nov | 0 | Dr White Slong |
| De'Aaron Fox | SA | Day-To-Day | Right Lower Leg Bruise | 25 Nov | 0 | Matt Wright's Foxies |
| Brandon Williams | GS | Out | Left Hamstring Strain | 25 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-25 09:06 UTC.
