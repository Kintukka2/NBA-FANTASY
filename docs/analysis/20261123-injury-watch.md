# Injury Watch: 23 Nov 2026

- Generated 2026-11-23 04:12 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 103 players in ESPN's injury feed. 32 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 17 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1102 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Kevin Huerter 22.3 (L7 16.5), Matas Buzelis 25.7 (L7 35.2), Yves Missi 29.1 (L7 24.0), Daniss Jenkins 29.7 (L7 32.8), Trey Murphy III 31.7 (L7 38.0). A pickup at or above **31.7** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 32.0 | +18.2 | **40.0** | 16.4 | 26.5 (4) | 20.4 (7) | 15.6 (15) | Free agent | 1% | 0 / 3 |
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 30.5 | +5.8 | **37.5** | 26.4 | 28.5 (4) | 29.7 (7) | 27.2 (13) | Free agent | 37% | 0 / 3 |
| **Norman Powell** (out, ESPN est. back 28 Nov) | CHI | Caleb Wilson (13 Dec) | 5 | 30.6 | +5.1 | **36.2** | 30.1 | 30.3 (3) | 36.2 (5) | 30.7 (12) → 33.1 (11) | Waivers | 79% | 0 / 3 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (13 Dec); also out: Jalen Duren (24 Nov) | 5 | 34.2 | +17.2 | **32.8** | 29.8 | — | 19.8 (4) | 30.0 (11) | Free agent | 38% | 0 / 3 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 6 | 24.3 | +14.3 | **30.3** | 20.2 | 30.5 (4) | 30.3 (6) | 21.8 (13) | Free agent | 2% | 0 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 22.3 | — | **28.5** | 26.6 | 27.8 (4) | 28.5 (6) | 28.0 (10) | Free agent | 2% | 0 / 4 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov) | 5 | 21.8 | +6.0 | **28.4** | 23.3 | 31.2 (4) | 27.0 (8) | 23.3 (15) | Free agent | 3% | 0 / 3 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 6 | 33.3 | +12.3 | **27.8** | 16.8 | 29.5 (4) | 24.0 (8) | 17.6 (15) | Free agent | 3% | 0 / 3 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 36.8 | +9.1 | **26.1** | 24.4 | 34.7 (3) | 31.2 (6) | 25.6 (13) | Free agent | 10% | 0 / 3 |
| **Jamison Battle** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 26.5 | +7.1 | **26.0** | 15.4 | 13.0 (4) | 18.0 (7) | 14.9 (15) | Free agent | 0% | 0 / 3 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 22.7 | — | **25.0** | 23.2 | 24.8 (4) | 21.6 (8) | 23.1 (16) | Free agent | 5% | 0 / 3 |
| **Luguentz Dort** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 3 | 28.3 | +4.0 | **24.7** | 20.0 | 19.0 (4) | 17.9 (7) | 20.4 (16) | Free agent | 3% | 0 / 2 |
| **Brice Sensabaugh** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 9 | 22.1 | +12.1 | **24.3** | 18.8 | 31.8 (5) | 24.3 (9) | 19.9 (17) | Free agent | 8% | 0 / 3 |
| **Javon Small** | MEM | GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 4 | 24.0 | +3.0 | **24.2** | 23.4 | 28.3 (3) | 26.4 (7) | 23.4 (9) | Free agent | 2% | 0 / 4 |
| **Kingston Flemings** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (27 Nov) | 1 | 27.0 | +3.8 | **24.0** | 19.9 | 24.0 (1) | 16.5 (4) | 21.1 (12) | Free agent | 4% | 0 / 2 |
| **Braden Smith** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 7 | 19.3 | — | **23.3** | 15.3 | 22.3 (3) | 15.0 (5) | 15.3 (11) | Free agent | 0% | 0 / 3 |
| **Bennett Stirtz** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 22.1 | — | **23.2** | 16.9 | 24.5 (4) | 20.8 (8) | 19.2 (15) | Free agent | 1% | 0 / 3 |
| **Terrence Shannon Jr.** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 7 | 23.9 | +3.2 | **23.0** | 21.4 | 30.2 (4) | 22.9 (7) | 22.4 (13) | Free agent | 7% | 0 / 4 |
| **Kenrich Williams** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 24.7 | +9.3 | **22.5** | 18.7 | 27.8 (4) | 23.2 (8) | 20.2 (15) | Free agent | 2% | 0 / 3 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan); also out: Brandon Williams (25 Nov) | 5 | 24.8 | +6.1 | **21.6** | 15.5 | 24.0 (4) | 19.0 (7) | 14.9 (15) | Free agent | 1% | 0 / 3 |
| **Nic Claxton** (out, ESPN est. back 23 Nov) | CHI | Caleb Wilson (13 Dec) | 4 | 22.5 | +5.5 | **20.5** | 23.3 | 22.3 (3) | 23.3 (6) | 23.3 (6) | Free agent | 40% | 0 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 10 | 20.6 | — | **20.4** | 18.0 | 19.5 (4) | 16.1 (7) | 18.0 (12) | Free agent | 0% | 0 / 3 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 9 | 26.7 | +5.7 | **20.2** | 19.3 | 22.8 (4) | 20.5 (8) | 19.7 (15) | Free agent | 1% | 0 / 4 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 5 | 30.6 | — | 13.7 (3) | 27.4 (8) | 39.0 | 36.5 | Free agent | 74% | 0 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 9 | 33.8 | — | — | 27.7 (3) | 37.5 | 36.0 | Free agent | 80% | 0 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 7 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 0 / 3 |
| **Norman Powell** | CHI | Right Hamstring Strain | 28 Nov | 6 | 30.1 | 30.3 (3) | 36.2 (5) | 30.7 (12) → 33.1 (11) | 36.0 | 33.0 | Waivers | 79% | 0 / 3 |
| **Nic Claxton** | CHI | Illness | 23 Nov | 1 | 23.3 | 22.3 (3) | 23.3 (6) | 23.3 (6) | 30.3 | 33.3 | Free agent | 40% | 0 / 3 |
| **Grayson Allen** | CHA | Concussion | 25 Nov | 3 | 26.8 | 26.0 (1) | 36.0 (3) | 26.4 (12) | 26.6 | 31.2 | Free agent | 20% | 0 / 3 |
| **P.J. Washington** | DAL | Illness | 24 Nov | 2 | 28.2 | 35.5 (2) | 25.0 (6) | 29.2 (14) | 26.9 | 30.6 | Free agent | 32% | 0 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 3 | 14.2 | — | — | 11.0 (4) | 30.6 | 27.1 | Free agent | 8% | 0 / 4 |
| **Mitchell Robinson** | BOS | Illness | 24 Nov | 2 | 18.6 | 15.7 (3) | 20.3 (6) | 18.6 (13) | 30.3 | 28.2 | Free agent | 11% | 0 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 11 | — | — | — | — | 30.1 | 28.0 | Free agent | 40% | 0 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 5 | 29.8 | — | 19.8 (4) | 30.0 (11) | 21.6 | 23.1 | Free agent | 38% | 0 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 23 Nov | 1 | 19.2 | — | 20.3 (3) | 19.4 (7) | 25.6 | 28.3 | Free agent | 2% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 3 | — | — | — | — | — | 28.1 | Free agent | 2% | 0 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 5 | 8.8 | — | 3.7 (3) | 7.6 (11) | 25.1 | 27.6 | Free agent | 6% | 0 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 5 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 0 / 2 |
| **Jaxson Hayes** | UTAH | Left Knee | 23 Nov | 1 | 27.1 | 26.3 (3) | 26.0 (7) | 25.8 (14) | 16.5 | 20.2 | Free agent | 15% | 0 / 3 |
| **Jock Landale** | ATL | Right Hip Inflammation | 27 Nov | 5 | 16.8 | — | 18.0 (2) | 15.6 (8) → 17.9 (7) | — | 25.8 | Free agent | 0% | 0 / 2 |
| **Collin Murray-Boyles** | TOR | Concussion | 23 Nov | 1 | 24.0 | 21.0 (3) | 23.2 (5) | 23.7 (13) | 24.8 | 25.6 | Free agent | 12% | 0 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 7 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 0 / 4 |
| **T.J. McConnell** | IND | Left Hamstring | 23 Nov | 1 | 20.0 | 23.3 (3) | 20.0 (7) | 20.0 (7) | 24.4 | 25.5 | Free agent | 7% | 0 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.7.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 3 | — (—) | 28.1 (74) | Free agent | 2% | 0 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 5 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 0 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 7 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 0 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 7 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 0 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 11 | 30.1 (30.5) | 28.0 (63) | Free agent | 40% | 0 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 41 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 0 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 41 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 0 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 73 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 100 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 0 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 131 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 0 / 4 |

## Our injured players

- **Paul George** (BOS): Out, Rest; ESPN est. back 24 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Day-To-Day, Knee; ESPN est. back 23 Nov.
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

Also out in those games, so part of the gain is theirs: Brandon Williams (left hamstring strain; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Charles Bassey | C | 5 | 21.8 | +6.0 | 3 | **28.4** | 26.6 | 31.2 (4) | 27.0 (8) | 23.3 (15) | Free agent | 3% |
| Will Richard | SG/SF | 5 | 24.8 | +6.1 | 1 | **21.6** | 15.0 | 24.0 (4) | 19.0 (7) | 14.9 (15) | Free agent | 1% |
| Gui Santos | SF | 5 | 20.6 | +5.6 | 1 | **19.4** | 6.7 | 20.8 (4) | 14.6 (8) | 15.1 (13) | Free agent | 1% |
| LJ Cryer | PG | 5 | 18.0 | +8.0 | 2 | **16.4** | 8.2 | 10.0 (4) | 16.6 (7) | 10.1 (13) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara (out, ESPN est. back 23 Nov) | C | 9 | 25.7 | — | 6 | **36.7** | — | 47.7 (3) | 39.7 (7) | 31.7 (14) | Snow Time Lakers | 37% |
| Bennett Stirtz | PG | 10 | 22.1 | — | 0 | **23.2** | — | 24.5 (4) | 20.8 (8) | 19.2 (15) | Free agent | 1% |
| Kenrich Williams | SF | 10 | 24.7 | +9.3 | 7 | **22.5** | 14.2 | 27.8 (4) | 23.2 (8) | 20.2 (15) | Free agent | 2% |
| Micah Peavy | SF | 8 | 19.1 | — | 1 | **13.1** | — | 15.3 (3) | 12.2 (6) | 11.2 (11) | Free agent | 0% |
| 5105800 |  | 5 | 17.0 | — | 0 | **12.0** | — | — | — | — | — | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 9 | 26.7 | +5.7 | 7 | **20.2** | 28.0 | 22.8 (4) | 20.5 (8) | 19.7 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | +14.3 | 0 | **16.7** | 0.0 | — | 19.5 (2) | 10.5 (6) | Free agent | 0% |
| Jayson Kent | PF | 6 | 13.5 | — | 2 | **9.2** | — | 9.2 (4) | 9.2 (6) | 9.2 (6) | Waivers | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 22.7 | — | 3 | **25.0** | — | 24.8 (4) | 21.6 (8) | 23.1 (16) | Free agent | 5% |
| Braden Smith | PG | 7 | 19.3 | — | 4 | **23.3** | — | 22.3 (3) | 15.0 (5) | 15.3 (11) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.0 | — | 1 | **19.6** | — | 24.5 (4) | 17.7 (7) | 15.9 (15) | Free agent | 0% |
| Jay Huff | C | 9 | 13.1 | — | 1 | **13.4** | — | 10.2 (4) | 9.7 (7) | 14.1 (15) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Allen Graves | SF | 2 | 32.0 | +18.2 | 1 | **40.0** | 10.0 | 26.5 (4) | 20.4 (7) | 15.6 (15) | Free agent | 1% |
| Jakob Poeltl | C | 2 | 30.5 | +5.8 | 2 | **37.5** | 30.4 | 28.5 (4) | 29.7 (7) | 27.2 (13) | Free agent | 37% |
| Jamison Battle | SF | 2 | 26.5 | +7.1 | 1 | **26.0** | 13.5 | 13.0 (4) | 18.0 (7) | 14.9 (15) | Free agent | 0% |
| Trayce Jackson-Davis | PF | 2 | 16.5 | +9.8 | 0 | **21.0** | 12.3 | 21.0 (2) | 22.3 (3) | 13.7 (10) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 10 | 33.5 | +4.1 | 10 | **35.2** | 30.4 | 26.8 (4) | 30.9 (7) | 35.1 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 31.6 | +4.3 | 9 | **26.9** | 26.3 | 29.0 (3) | 22.7 (6) | 28.0 (15) | Dr White Slong | 60% |
| Terrence Shannon Jr. | SG | 7 | 23.9 | +3.2 | 0 | **23.0** | 14.9 | 30.2 (4) | 22.9 (7) | 22.4 (13) | Free agent | 7% |
| Joan Beringer | C | 10 | 15.6 | — | 0 | **17.6** | — | 17.2 (4) | 17.6 (7) | 19.9 (16) | Free agent | 1% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 6 | 18.0 | +4.9 | 0 | **13.8** | 9.4 | — | 12.0 (3) | 12.9 (11) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 9 | 22.8 | — | 3 | **28.8** | — | 32.0 (5) | 28.8 (9) | 28.2 (14) | Team Nic Kerr | 17% |
| Brice Sensabaugh | SG/SF | 9 | 22.1 | +12.1 | 0 | **24.3** | 3.0 | 31.8 (5) | 24.3 (9) | 19.9 (17) | Free agent | 8% |
| Svi Mykhailiuk | SG | 9 | 22.4 | +8.4 | 0 | **19.6** | -1.0 | 30.8 (5) | 19.6 (9) | 12.9 (17) | Free agent | 1% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 2 | 32.5 | +3.6 | 2 | **90.5** | 76.4 | 79.0 (4) | 74.8 (8) | 74.0 (16) | Cream Abdul-Yammar | 100% |
| Jordan McLaughlin (day to day, ESPN est. back 23 Nov) | PG | 2 | 14.5 | +3.5 | 0 | **16.5** | 14.7 | 19.0 (3) | 15.6 (7) | 11.9 (11) | Free agent | 0% |
| Carter Bryant | SF | 2 | 16.5 | +5.8 | 0 | **8.5** | 8.7 | 4.0 (4) | 9.9 (8) | 7.3 (15) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Jock Landale (right hip inflammation; ESPN est. 27 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 3 | 37.0 | +4.9 | 3 | **53.3** | 44.9 | 48.2 (4) | 48.3 (7) | 42.6 (16) | Snow Time Lakers | 97% |
| Luguentz Dort | SG/SF | 3 | 28.3 | +4.0 | 0 | **24.7** | 21.4 | 19.0 (4) | 17.9 (7) | 20.4 (16) | Free agent | 3% |
| Kingston Flemings | PG/SG | 1 | 27.0 | +3.8 | 1 | **24.0** | 18.2 | 24.0 (1) | 16.5 (4) | 21.1 (12) | Free agent | 4% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.8 | +5.4 | 10 | **36.4** | 30.2 | 35.2 (5) | 33.1 (9) | 35.1 (17) | Snow Time Lakers | 80% |
| AJ Dybantsa | SF | 10 | 35.2 | +3.0 | 10 | **31.6** | 32.9 | 38.6 (5) | 31.3 (9) | 30.3 (14) | Dr White Slong | 86% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Miller (day to day, ESPN est. back 23 Nov) | SG/SF | 7 | 29.1 | +3.1 | 7 | **28.0** | 2.0 | 27.3 (3) | 27.3 (3) | 30.8 (12) | Matt Wright's Foxies | 86% |
| Royce O'Neale | SF/PF | 9 | 22.6 | +4.6 | 0 | **14.7** | 9.0 | 14.7 (3) | 14.6 (5) | 12.3 (14) | Free agent | 1% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 3 | 29.0 | +9.0 | 2 | **14.0** | 17.0 | — | — | 17.8 (8) | Free agent | 3% |
| Christian Anderson | PG | 9 | 15.9 | — | 0 | **13.4** | — | 19.3 (3) | 17.2 (5) | 10.2 (13) | Free agent | 0% |
| Tidjane Salaun | PF | 9 | 13.3 | +3.3 | 0 | **10.4** | 13.0 | 3.7 (3) | 8.6 (5) | 11.6 (14) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jalen Smith | PF/C | 4 | 28.8 | +5.0 | 4 | **49.5** | 34.5 | 52.3 (3) | 49.2 (6) | 38.3 (13) → 40.7 (12) | **us** | 47% |
| Norman Powell (out, ESPN est. back 28 Nov) | SG/SF | 5 | 30.6 | +5.1 | 5 | **36.2** | 13.5 | 30.3 (3) | 36.2 (5) | 30.7 (12) → 33.1 (11) | Waivers | 79% |
| Buddy Hield | SG/SF | 6 | 24.3 | +14.3 | 1 | **30.3** | 16.0 | 30.5 (4) | 30.3 (6) | 21.8 (13) | Free agent | 2% |
| Isaac Okoro | SG/SF | 6 | 33.3 | +12.3 | 6 | **27.8** | 9.2 | 29.5 (4) | 24.0 (8) | 17.6 (15) | Free agent | 3% |
| Nic Claxton (out, ESPN est. back 23 Nov) | C | 4 | 22.5 | +5.5 | 1 | **20.5** | 29.0 | 22.3 (3) | 23.3 (6) | 23.3 (6) | Free agent | 40% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 22.3 | — | 0 | **28.5** | — | 27.8 (4) | 28.5 (6) | 28.0 (10) | Free agent | 2% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 24 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 32.1 | +14.1 | 9 | **43.6** | 45.0 | 48.8 (4) | 46.0 (8) | 39.4 (14) | Lauri Birds | 83% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 5 | 34.2 | +17.2 | 5 | **32.8** | 13.0 | — | 19.8 (4) | 30.0 (11) | Free agent | 38% |
| Paul Reed | PF/C | 9 | 26.2 | +3.2 | 3 | **32.8** | 25.0 | 37.0 (4) | 32.4 (8) | 33.5 (15) | Lauri Birds | 39% |
| Javonte Green | SF | 9 | 19.7 | +7.7 | 1 | **16.7** | 5.0 | 20.8 (4) | 17.2 (8) | 14.7 (15) | Free agent | 1% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cam Spencer | PG/SG | 5 | 27.4 | +3.6 | 3 | **33.2** | 30.8 | 38.5 (4) | 34.0 (8) | 31.2 (16) | Lauri Birds | 36% |
| Javon Small | PG | 4 | 24.0 | +3.0 | 0 | **24.2** | 25.0 | 28.3 (3) | 26.4 (7) | 23.4 (9) | Free agent | 2% |
| Isaiah Stewart | PF/C | 2 | 19.5 | +3.8 | 0 | **19.5** | 16.2 | 19.5 (2) | 19.0 (5) | 21.2 (12) | Free agent | 3% |
| Olivier-Maxence Prosper | PF | 5 | 18.0 | +10.5 | 0 | **12.8** | 10.2 | 15.2 (4) | 13.0 (7) | 10.5 (11) | Free agent | 0% |
| Jahmai Mashack | SG | 5 | 13.4 | +11.4 | 1 | **6.8** | 0.0 | 8.2 (4) | 6.6 (5) | 5.4 (8) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Bradley Beal (right knee inflammation; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yanic Konan Niederhauser | C | 2 | 13.5 | — | 0 | **17.0** | — | 17.0 (2) | 17.0 (2) | 17.0 (2) | Free agent | 1% |
| Kobe Sanders | SG | 10 | 22.0 | — | 1 | **16.8** | — | 12.5 (4) | 13.6 (7) | 17.4 (14) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.0 | +6.4 | 10 | **40.5** | 30.4 | 35.5 (4) | 39.6 (7) | 41.2 (15) | Team Nic Kerr | 91% |
| De'Andre Hunter | SF/PF | 8 | 36.8 | +9.1 | 8 | **26.1** | 23.9 | 34.7 (3) | 31.2 (6) | 25.6 (13) | Free agent | 10% |
| Leaky Black | SF | 10 | 20.6 | — | 1 | **20.4** | — | 19.5 (4) | 16.1 (7) | 18.0 (12) | Free agent | 0% |
| Dylan Cardwell | C | 9 | 15.0 | — | 2 | **16.6** | — | 11.8 (4) | 15.1 (7) | 16.6 (9) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 16.0 | — | 0 | **12.2** | — | 10.0 (4) | 10.0 (7) | 10.0 (15) | Free agent | 0% |

## Every injury

All 103 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 313 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 313 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 221 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 131 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 131 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 115 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 100 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 100 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 100 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 100 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 95 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 73 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 70 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 57 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 51 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 43 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 41 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 41 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 41 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 41 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 41 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 29 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 27 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 22 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 21 | Lauri Birds |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 21 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 21 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 21 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 21 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 20 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 20 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 20 | Free agent |
| Jerami Grant | MEM | Day-To-Day | Left Calf | 12 Dec | 20 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 11 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 11 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 11 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 11 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 9 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 9 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 9 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 7 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 29 Nov | 7 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 7 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 7 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 7 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 7 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 7 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 7 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 7 | Free agent |
| Norman Powell | CHI | Out | Right Hamstring Strain | 28 Nov | 6 | Waivers |
| Jonathan Isaac | ORL | Out | Left Knee | 28 Nov | 6 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 5 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 5 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 5 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 27 Nov | 5 | — |
| Jock Landale | ATL | Out | Right Hip Inflammation | 27 Nov | 5 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 5 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 5 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 5 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 5 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 5 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 27 Nov | 5 | Cream Abdul-Yammar |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 3 | Free agent |
| OG Anunoby | NY | Out | Left Calf Soreness | 25 Nov | 3 | Cream Abdul-Yammar |
| Nolan Traore | BKN | Out | Right Hamstring Strain | 25 Nov | 3 | Free agent |
| Miles McBride | NY | Out | Left Abdomen | 25 Nov | 3 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 3 | Free agent |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 25 Nov | 3 | Free agent |
| Grayson Allen | CHA | Out | Concussion | 25 Nov | 3 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 25 Nov | 3 | Free agent |
| Giannis Antetokounmpo | MIA | Out | Groin | 25 Nov | 3 | Dr White Slong |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 3 | Free agent |
| Cameron Boozer | MEM | Out | Right Ankle Sprain | 25 Nov | 3 | Lauri Birds |
| Brandon Williams | GS | Out | Left Hamstring Strain | 25 Nov | 3 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 2 | Free agent |
| Tobi Lawal | DAL | Out | Right Groin | 24 Nov | 2 | Free agent |
| Paul George | BOS | Out | Rest | 24 Nov | 2 | **us** |
| P.J. Washington | DAL | Out | Illness | 24 Nov | 2 | Free agent |
| Mitchell Robinson | BOS | Out | Illness | 24 Nov | 2 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 2 | **us** |
| Ebuka Okorie | DET | Day-To-Day | Left Oblique Strain | 24 Nov | 2 | Free agent |
| Zion Williamson | NO | Day-To-Day | Left Thigh Bruise | 23 Nov | 1 | Melbourne poopoo |
| Trey Murphy III | NO | Day-To-Day | Knee | 23 Nov | 1 | **us** |
| T.J. McConnell | IND | Out | Left Hamstring | 23 Nov | 1 | Free agent |
| Shai Gilgeous-Alexander | OKC | Out | Back Bruise | 23 Nov | 1 | Matt Wright's Foxies |
| Ryan Dunn | PHX | Day-To-Day | Right Quadriceps Soreness | 23 Nov | 1 | Free agent |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 23 Nov | 1 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Soreness | 23 Nov | 1 | Free agent |
| Nic Claxton | CHI | Out | Illness | 23 Nov | 1 | Free agent |
| Jordan McLaughlin | SA | Day-To-Day | Left Shoulder Bruise | 23 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle | 23 Nov | 1 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 23 Nov | 1 | Free agent |
| Jaylen Brown | PHI | Day-To-Day | Left Hamstring | 23 Nov | 1 | Snow Time Lakers |
| Jaxson Hayes | UTAH | Out | Left Knee | 23 Nov | 1 | Free agent |
| Grant Nelson | BKN | Day-To-Day | Right Ankle Sprain | 23 Nov | 1 | — |
| Dean Wade | PHI | Day-To-Day | Left Hamstring Soreness | 23 Nov | 1 | Free agent |
| De'Aaron Fox | SA | Day-To-Day | Right Lower Leg Bruise | 23 Nov | 1 | Matt Wright's Foxies |
| Collin Murray-Boyles | TOR | Day-To-Day | Concussion | 23 Nov | 1 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 23 Nov | 1 | Free agent |
| Brandon Miller | CHA | Day-To-Day | Right Knee Bruise | 23 Nov | 1 | Matt Wright's Foxies |
| Alex Caruso | OKC | Out | Right Hip Soreness | 23 Nov | 1 | Free agent |
| Adem Bona | PHI | Out | Back Sprain | 23 Nov | 1 | Free agent |
| Aday Mara | OKC | Out | Right Lower Leg Bruise | 23 Nov | 1 | Snow Time Lakers |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-23 04:12 UTC.
