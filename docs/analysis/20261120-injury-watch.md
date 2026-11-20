# Injury Watch: 20 Nov 2026

- Generated 2026-11-20 03:47 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 108 players in ESPN's injury feed. 45 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 23 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Kel'el Ware 22.9 (L7 26.8), Rudy Gobert 25.4 (L7 22.4), Saddiq Bey 30.4 (L7 41.0), Daniss Jenkins 30.5 (L7 36.5), Yves Missi 32.0 (L7 25.7). A pickup at or above **32.0** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Ja'Kobe Walter** | TOR | RJ Barrett (13 Dec), Kawhi Leonard (27 Nov) | 1 | 38.0 | +5.3 | **48.0** | 26.0 | 27.5 (4) | 22.6 (8) | 26.0 (15) | Free agent | 12% | 1 / 3 |
| **Devin Vassell** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 1 | 32.0 | +3.4 | **42.0** | 27.6 | 25.8 (4) | 28.6 (7) | 27.6 (14) | Free agent | 40% | 1 / 4 |
| **Tyrese Proctor** | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 4 | 29.0 | +7.5 | **39.5** | 22.6 | 39.5 (4) | 27.7 (9) | 22.6 (15) | Free agent | 12% | 1 / 3 |
| **Jakob Poeltl** | TOR | RJ Barrett (13 Dec), Kawhi Leonard (27 Nov) | 1 | 29.0 | +4.3 | **37.0** | 25.5 | 24.8 (4) | 31.0 (8) | 25.5 (13) | Free agent | 37% | 1 / 3 |
| **Jamison Battle** | TOR | RJ Barrett (13 Dec), Kawhi Leonard (27 Nov) | 1 | 33.0 | +13.9 | **34.0** | 15.3 | 15.8 (4) | 15.9 (8) | 15.3 (15) | Free agent | 0% | 1 / 3 |
| **Mo Bamba** | UTAH | Jusuf Nurkic (27 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 7 | 23.1 | +6.6 | **33.9** | 31.1 | 42.8 (4) | 33.1 (8) | 31.1 (12) | Waivers | 21% | 2 / 3 |
| **Brandon Williams** (out, ESPN est. back 22 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +11.7 | **33.0** | 18.8 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% | 1 / 3 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 5 | 29.2 | +5.4 | **32.8** | 22.8 | 26.5 (4) | 27.2 (9) | 22.8 (16) | Free agent | 12% | 1 / 4 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.0 | — | **32.6** | 27.1 | 34.3 (3) | 33.1 (8) | 27.1 (15) | Free agent | 24% | 2 / 3 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 5 | 21.2 | +9.7 | **31.6** | 20.4 | 44.7 (3) | 22.4 (8) | 20.4 (15) | Free agent | 11% | 1 / 4 |
| **Luguentz Dort** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Jock Landale (22 Nov), Kingston Flemings (20 Nov) | 1 | 31.0 | +6.4 | **31.0** | 19.8 | 20.3 (3) | 22.3 (7) | 19.8 (15) | Free agent | 3% | 2 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 4 | 32.2 | +12.2 | **30.8** | 16.1 | 30.8 (4) | 22.9 (7) | 16.1 (14) | Free agent | 1% | 2 / 3 |
| **Jordan Poole** | NO | Bryce McGowens (27 Nov), Trendon Watford (27 Nov), Bennedict Mathurin (27 Nov), Dejounte Murray (27 Nov); also out: Trey Murphy III (20 Nov) | 3 | 28.3 | +3.0 | **30.0** | 21.0 | 27.8 (4) | 23.5 (6) | 21.0 (10) | Free agent | 13% | 2 / 3 |
| **Julian Champagnie** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 1 | 29.0 | +4.0 | **29.0** | 23.9 | 21.8 (4) | 21.4 (9) | 23.9 (16) | Free agent | 42% | 1 / 4 |
| **Quenton Jackson** | IND | Tyrese Haliburton (28 Nov), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 24.0 | — | **28.9** | 24.6 | 30.7 (3) | 25.4 (7) | 24.6 (15) | Free agent | 4% | 2 / 3 |
| **Jaylon Tyson** (out, ESPN est. back 23 Nov) | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 2 | 32.0 | +9.0 | **28.0** | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% | 1 / 3 |
| **Norchad Omier** | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 3 | 18.7 | +11.2 | **27.3** | 18.6 | 27.3 (3) | 18.6 (5) | 18.6 (5) | Free agent | 0% | 1 / 3 |
| **Javonte Green** | DET | Taurean Prince (13 Dec), Duncan Robinson (27 Nov); also out: Ronald Holland II (22 Nov), Jalen Duren (24 Nov) | 2 | 29.0 | +12.4 | **26.5** | 15.6 | 18.2 (4) | 16.0 (7) | 15.6 (14) | Free agent | 0% | 2 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 19.3 | — | **25.2** | 26.0 | 25.0 (4) | 27.6 (5) | 26.0 (10) | Free agent | 3% | 1 / 4 |
| **Tristan da Silva** | ORL | Paolo Banchero (29 Nov) | 8 | 31.0 | +9.6 | **24.9** | 25.8 | 25.3 (3) | 25.8 (5) | 25.8 (12) | Free agent | 10% | 2 / 3 |
| **Brice Sensabaugh** | UTAH | Jusuf Nurkic (27 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 7 | 22.3 | +10.3 | **24.9** | 18.4 | 29.8 (4) | 21.0 (9) | 18.4 (16) | Free agent | 6% | 2 / 3 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 20.6 | +4.8 | **24.8** | 21.6 | 23.8 (4) | 24.4 (8) | 21.6 (14) | Free agent | 1% | 1 / 3 |
| **Javon Small** | MEM | GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 4 | 24.0 | +3.0 | **24.2** | 23.4 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 4% | 1 / 4 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 4 | 20.8 | +9.2 | **24.0** | 16.4 | 24.0 (4) | 22.4 (5) | 16.4 (12) | Free agent | 1% | 2 / 3 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (21 Nov) | 10 | 25.0 | +3.0 | **23.3** | 26.9 | 17.8 (4) | 19.4 (7) | 26.9 (14) | Free agent | 30% | 1 / 4 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 22.9 | — | **23.2** | 19.8 | 21.3 (3) | 21.0 (7) | 19.8 (10) | Free agent | 0% | 2 / 3 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 25.8 | +7.1 | **22.2** | 16.1 | 25.5 (4) | 21.0 (7) | 16.1 (15) | Free agent | 1% | 1 / 3 |
| **Kenrich Williams** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 24.5 | +9.1 | **22.0** | 17.8 | 31.7 (3) | 21.8 (8) | 17.8 (15) | Free agent | 1% | 2 / 3 |
| **Pete Nance** | MIL | Ousmane Dieng (14 Dec) | 1 | 28.0 | +24.0 | **22.0** | 13.5 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% | 1 / 4 |
| **De'Andre Hunter** (day to day, ESPN est. back 20 Nov) | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 35.6 | +8.0 | **21.4** | 20.8 | 27.5 (2) | 22.0 (5) | 20.8 (12) | Free agent | 6% | 2 / 3 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 8 | 27.1 | +5.6 | **20.5** | 19.4 | 20.0 (4) | 21.3 (9) | 19.4 (15) | Free agent | 1% | 1 / 4 |
| **Allen Graves** | TOR | RJ Barrett (13 Dec), Kawhi Leonard (27 Nov) | 1 | 31.0 | +17.7 | **20.0** | 13.5 | 11.2 (4) | 12.1 (8) | 13.5 (15) | Free agent | 0% | 1 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Trey Murphy III** | NO | Knee Tendinitis | 20 Nov | 1 | 31.0 | — | 38.5 (2) | 31.0 (9) | 36.8 | 41.6 | Free agent | 78% | 2 / 3 |
| **Zach Edey** | MEM | Ankle | 21 Nov | 2 | 25.0 | 36.0 (2) | 26.2 (6) | 25.0 (12) | 33.2 | 39.5 | Free agent | 43% | 1 / 4 |
| **Dejounte Murray** | NO | Ankle | 27 Nov | 8 | 30.6 | — | 20.8 (5) | 30.6 (9) | 39.0 | 36.5 | Free agent | 76% | 2 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 12 | 33.8 | — | — | 33.8 (4) | 37.5 | 36.0 | Free agent | 80% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 27 Nov | 8 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 3 |
| **Grayson Allen** | CHA | Concussion | 23 Nov | 4 | 26.8 | 27.5 (2) | 31.6 (5) | 26.8 (13) | 26.6 | 31.2 | Free agent | 23% | 1 / 3 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 6 | 14.2 | — | — | 14.2 (5) | 30.6 | 27.1 | Free agent | 8% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 14 | — | — | — | — | 30.1 | 28.0 | Free agent | 40% | 1 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 8 | 29.8 | 16.0 (2) | 24.8 (5) | 29.8 (12) | 21.6 | 23.1 | Free agent | 42% | 2 / 3 |
| **Peyton Watson** | CLE | Back Bruise | 20 Nov | 1 | 24.2 | 9.5 (2) | 21.3 (6) | 24.2 (12) | 29.3 | 29.8 | Free agent | 36% | 1 / 3 |
| **Jerami Grant** | MEM | Left Calf | 21 Nov | 2 | 20.3 | 18.2 (4) → 23.7 (3) | 21.4 (8) → 24.1 (7) | 20.3 (15) → 21.6 (14) | 27.0 | 28.8 | Free agent | 11% | 1 / 4 |
| **Myles Turner** | MIL | Left Shoulder Bruise | 21 Nov | 2 | 26.6 | 32.3 (3) | 26.3 (7) | 26.6 (14) | 28.4 | 28.6 | Free agent | 46% | 1 / 4 |
| **Draymond Green** | GS | Rest | 22 Nov | 3 | 24.0 | 20.7 (3) | 26.0 (7) | 24.0 (13) | 28.5 | 26.5 | Free agent | 24% | 1 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 23 Nov | 4 | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 2% | 1 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 6 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 8 | 8.8 | -3.0 (1) | 3.8 (5) | 8.8 (12) | 25.1 | 27.6 | Free agent | 6% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 8 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 2 / 2 |
| **Precious Achiuwa** | SAC | Left Lower Leg Bruise | 20 Nov | 1 | 25.4 | -3.0 (1) | 15.8 (5) | 25.4 (12) | 24.1 | 27.0 | Free agent | 14% | 2 / 3 |
| **Robert Williams III** | POR | Rest | 21 Nov | 2 | 24.4 | 19.7 (3) | 25.1 (7) | 24.4 (12) | 26.9 | 26.6 | Free agent | 4% | 1 / 4 |
| **Jock Landale** | ATL | Right Hip Inflammation | 22 Nov | 3 | 16.8 | 19.0 (1) | 18.0 (2) | 16.8 (9) → 18.9 (8) | — | 25.8 | Free agent | 0% | 2 / 2 |
| **Collin Murray-Boyles** | TOR | Concussion | 23 Nov | 4 | 24.0 | 26.5 (4) | 26.9 (7) | 24.0 (14) | 24.8 | 25.6 | Free agent | 13% | 1 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 10 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 1 / 4 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 20 Nov | 1 | 22.5 | 29.7 (3) | 22.5 (6) | 22.5 (6) | 24.4 | 25.5 | Free agent | 8% | 2 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 32.0.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Brandon Ingram** | LAC | Right Achilles Surgery | 21 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 1 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 6 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 8 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 2 / 2 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 27 Nov | 8 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 10 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 14 | 30.1 (30.5) | 28.0 (63) | Free agent | 40% | 1 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 44 | 38.8 (32.4) | 41.6 (38) | Free agent | 28% | 1 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 44 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 1 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 76 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 1 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 103 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 1 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 134 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 4 |

## Our injured players

- **Cade Cunningham** (DET): Day-To-Day, Right Knee Soreness; ESPN est. back 20 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 27 Nov.

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

### NO

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dejounte Murray | Ankle | 27 Nov | 32.4 | 30.6 | Free agent |
| Bennedict Mathurin | Left Foot Plantar Fasciitis | 27 Nov | 30.0 | 8.8 | Free agent |
| Bryce McGowens | Left Elbow Infection | 27 Nov | 21.0 | 10.0 | Free agent |
| Trendon Watford | Right Ankle Sprain | 27 Nov | 17.8 | 16.5 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Trey Murphy III (knee tendinitis; ESPN est. 20 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Saddiq Bey | SF/PF | 3 | 38.7 | +8.7 | 3 | **35.3** | 31.6 | 41.0 (4) | 33.0 (9) | 30.4 (16) | **us** | 50% |
| Jordan Poole | PG/SG | 3 | 28.3 | +3.0 | 0 | **30.0** | 17.0 | 27.8 (4) | 23.5 (6) | 21.0 (10) | Free agent | 13% |
| Jaron Pierre Jr. | SG | 3 | 19.7 | +14.2 | 0 | **14.7** | 3.5 | 10.8 (4) | 10.2 (5) | 10.2 (5) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |
| Jusuf Nurkic | Right Foot Strain | 27 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 7 | 23.1 | +6.6 | 3 | **33.9** | 27.0 | 42.8 (4) | 33.1 (8) | 31.1 (12) | Waivers | 21% |
| Brice Sensabaugh | SG/SF | 7 | 22.3 | +10.3 | 0 | **24.9** | 7.3 | 29.8 (4) | 21.0 (9) | 18.4 (16) | Free agent | 6% |
| Isaiah Collier | PG | 5 | 15.6 | +6.3 | 0 | **14.4** | 7.7 | 8.5 (2) | 11.7 (7) | 14.1 (14) | Free agent | 2% |
| Svi Mykhailiuk | SG | 7 | 20.3 | +5.3 | 0 | **13.7** | 3.7 | 18.8 (4) | 11.8 (9) | 10.8 (16) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 25.0 | — | 5 | **32.6** | — | 34.3 (3) | 33.1 (8) | 27.1 (15) | Free agent | 24% |
| Kenrich Williams | SF | 10 | 24.5 | +9.1 | 8 | **22.0** | 14.2 | 31.7 (3) | 21.8 (8) | 17.8 (15) | Free agent | 1% |
| Bennett Stirtz | PG | 10 | 20.2 | — | 0 | **19.0** | — | 10.0 (3) | 19.4 (8) | 14.1 (15) | Free agent | 1% |
| Micah Peavy | SF | 8 | 17.9 | — | 0 | **11.4** | — | 14.0 (1) | 12.2 (6) | 10.1 (9) | Free agent | 0% |
| 5105800 |  | 6 | 12.3 | — | 0 | **7.2** | — | — | — | — | — | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 8 | 27.1 | +5.6 | 6 | **20.5** | 20.5 | 20.0 (4) | 21.3 (9) | 19.4 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 21 Nov) | SG | 3 | 18.3 | +8.8 | 0 | **16.7** | 5.5 | — | 12.5 (4) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 5 | 15.6 | — | 2 | **10.8** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 28 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard (day to day, ESPN est. back 20 Nov) | PG/SG | 7 | 33.7 | +3.0 | 7 | **33.4** | 28.2 | 12.0 (1) | 31.8 (5) | 33.2 (11) | Matt Wright's Foxies | 68% |
| Quenton Jackson | PG/SG | 10 | 24.0 | — | 3 | **28.9** | — | 30.7 (3) | 25.4 (7) | 24.6 (15) | Free agent | 4% |
| Braden Smith (day to day, ESPN est. back 20 Nov) | PG | 7 | 17.0 | — | 4 | **18.4** | — | 30.0 (1) | 17.5 (4) | 14.6 (9) | Free agent | 0% |
| Jay Huff | C | 9 | 16.9 | — | 3 | **16.1** | — | 18.3 (3) | 13.8 (6) | 16.1 (13) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.9 | — | 1 | **15.9** | — | 16.3 (3) | 13.7 (6) | 14.5 (13) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 27 Nov | 32.8 | 40.0 | **us** |

Last 10 games: 1 game(s) without them, 9 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ja'Kobe Walter | SG | 1 | 38.0 | +5.3 | 1 | **48.0** | 20.4 | 27.5 (4) | 22.6 (8) | 26.0 (15) | Free agent | 12% |
| Jakob Poeltl | C | 1 | 29.0 | +4.3 | 1 | **37.0** | 30.4 | 24.8 (4) | 31.0 (8) | 25.5 (13) | Free agent | 37% |
| Jamison Battle | SF | 1 | 33.0 | +13.9 | 1 | **34.0** | 15.4 | 15.8 (4) | 15.9 (8) | 15.3 (15) | Free agent | 0% |
| Allen Graves | SF | 1 | 31.0 | +17.7 | 0 | **20.0** | 9.2 | 11.2 (4) | 12.1 (8) | 13.5 (15) | Free agent | 0% |
| Trayce Jackson-Davis | PF | 1 | 17.0 | +9.8 | 0 | **18.0** | 14.5 | 18.0 (1) | 18.3 (3) | 12.7 (10) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.7 | +3.0 | 10 | **38.3** | 29.7 | 42.8 (5) | 41.4 (8) | 38.6 (16) | Melbourne poopoo | 91% |
| Ayo Dosunmu | PG/SG | 10 | 33.9 | +4.5 | 10 | **37.7** | 30.4 | 29.4 (5) | 33.2 (8) | 34.8 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 31.9 | +4.6 | 9 | **28.0** | 26.3 | 28.2 (4) | 26.0 (7) | 28.9 (15) | Dr White Slong | 59% |
| Joan Beringer | C | 10 | 17.4 | — | 1 | **18.8** | — | 19.0 (5) | 16.1 (8) | 19.3 (16) | Free agent | 2% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 7 | 18.3 | +5.2 | 0 | **14.7** | 9.4 | 12.5 (2) | 14.6 (5) | 11.9 (12) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 1 | 33.0 | +4.7 | 1 | **59.0** | 72.0 | 60.0 (4) | 74.0 (9) | 69.1 (16) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 1 | 33.0 | +3.8 | 1 | **59.0** | 34.0 | 48.0 (4) | 36.7 (9) | 34.8 (16) | Melbourne poopoo | 96% |
| Devin Vassell | SG/SF | 1 | 32.0 | +3.4 | 1 | **42.0** | 24.9 | 25.8 (4) | 28.6 (7) | 27.6 (14) | Free agent | 40% |
| Julian Champagnie | SF/PF | 1 | 29.0 | +4.0 | 1 | **29.0** | 19.7 | 21.8 (4) | 21.4 (9) | 23.9 (16) | Free agent | 42% |
| De'Aaron Fox | PG/SG | 1 | 32.0 | +5.2 | 1 | **17.0** | 24.9 | 12.7 (3) | 24.0 (8) | 30.1 (15) | Matt Wright's Foxies | 94% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Duncan Robinson | Left Quadriceps Strain | 27 Nov | 30.6 | 29.8 | Free agent |
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Ronald Holland II (left knee bruise; ESPN est. 22 Nov), Jalen Duren (right hamstring strain; ESPN est. 24 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 2 | 31.5 | +3.0 | 2 | **50.0** | 39.2 | 56.8 (4) | 44.4 (7) | 37.9 (13) | Lauri Birds | 82% |
| Daniss Jenkins | PG | 2 | 37.0 | +7.4 | 2 | **41.5** | 30.6 | 36.5 (4) | 38.0 (7) | 30.5 (14) | **us** | 38% |
| Javonte Green | SF | 2 | 29.0 | +12.4 | 1 | **26.5** | 13.6 | 18.2 (4) | 16.0 (7) | 15.6 (14) | Free agent | 0% |
| Kevin Huerter | SG/SF | 2 | 36.0 | +9.4 | 2 | **18.0** | 29.0 | 25.5 (4) | 30.4 (7) | 23.4 (14) | Free agent | 10% |
| Chaz Lanier | SG | 2 | 20.5 | +16.5 | 0 | **10.0** | 5.3 | 10.0 (2) | 6.7 (3) | 6.5 (6) | Free agent | 0% |

### CLE

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Evan Mobley | Left Toe Sprain | 29 Nov | 33.3 | 39.9 | Matt Wright's Foxies |
| Nae'Qwan Tomlin | Back | 29 Nov | 15.7 | -2.0 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| James Harden | PG/SG | 3 | 35.0 | +3.3 | 3 | **40.3** | 31.2 | 40.3 (3) | 34.8 (8) | 33.1 (15) | Team Nic Kerr | 99% |
| Tyrese Proctor | SG | 4 | 29.0 | +7.5 | 3 | **39.5** | 19.2 | 39.5 (4) | 27.7 (9) | 22.6 (15) | Free agent | 12% |
| Jarrett Allen | C | 3 | 30.7 | +9.2 | 3 | **36.3** | 26.5 | 36.3 (3) | 30.7 (6) → 36.8 (5) | 35.1 (13) → 38.0 (12) | Dr White Slong | 89% |
| Jaylon Tyson (out, ESPN est. back 23 Nov) | SG/SF | 2 | 32.0 | +9.0 | 2 | **28.0** | 5.0 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% |
| Norchad Omier | PF | 3 | 18.7 | +11.2 | 0 | **27.3** | 5.5 | 27.3 (3) | 18.6 (5) | 18.6 (5) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 21 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 25.0 | +3.0 | 9 | **23.3** | 20.0 | 17.8 (4) | 19.4 (7) | 26.9 (14) | Free agent | 30% |
| Kobe Sanders | SG | 10 | 22.5 | — | 1 | **17.2** | — | 11.2 (4) | 11.4 (7) | 17.5 (14) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Waivers |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

Also out in those games, so part of the gain is theirs: Jock Landale (right hip inflammation; ESPN est. 22 Nov), Kingston Flemings (back strain; ESPN est. 20 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 1 | 37.0 | +5.4 | 1 | **42.0** | 40.3 | 35.7 (3) | 45.6 (7) | 40.8 (15) | Snow Time Lakers | 96% |
| Onyeka Okongwu | C | 1 | 36.0 | +3.9 | 1 | **41.0** | 43.7 | 41.0 (3) | 44.3 (7) | 37.2 (15) | Cream Abdul-Yammar | 86% |
| Luguentz Dort | SG/SF | 1 | 31.0 | +6.4 | 0 | **31.0** | 19.9 | 20.3 (3) | 22.3 (7) | 19.8 (15) | Free agent | 3% |
| Corey Kispert | SG/SF | 1 | 17.0 | +4.4 | 0 | **22.0** | 14.4 | 24.5 (2) | 18.2 (4) | 15.2 (8) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.9 | +5.5 | 10 | **38.3** | 30.2 | 34.0 (4) | 37.2 (9) | 34.8 (16) | Snow Time Lakers | 79% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 29 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 10 | 38.2 | +4.2 | 10 | **55.2** | 38.6 | 66.3 (3) | 61.0 (7) | 48.6 (14) | Cream Abdul-Yammar | 95% |
| Anthony Black | PG/SG | 9 | 34.7 | +5.8 | 9 | **40.7** | 28.2 | 29.7 (3) | 39.4 (7) | 38.3 (11) | **us** | 68% |
| Wendell Carter Jr. | C | 10 | 33.3 | +7.9 | 10 | **31.6** | 23.0 | 26.3 (3) | 34.6 (7) | 32.6 (14) | Dr White Slong | 56% |
| Tristan da Silva | SF/PF | 8 | 31.0 | +9.6 | 2 | **24.9** | 17.2 | 25.3 (3) | 25.8 (5) | 25.8 (12) | Free agent | 10% |
| Jase Richardson | SG | 7 | 25.6 | +14.7 | 5 | **17.1** | 8.6 | — | 16.2 (4) | 15.3 (11) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Miller | SG/SF | 7 | 29.9 | +3.9 | 7 | **31.1** | 2.0 | 24.5 (2) | 15.8 (4) | 29.5 (12) | Matt Wright's Foxies | 86% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 4 | 30.2 | +10.2 | 3 | **16.5** | 17.0 | — | 17.0 (1) | 19.1 (9) | Free agent | 3% |
| Royce O'Neale | SF/PF | 9 | 24.0 | +6.0 | 0 | **15.2** | 9.0 | 13.0 (3) | 15.5 (6) | 12.9 (14) | Free agent | 1% |
| Christian Anderson | PG | 9 | 14.6 | — | 0 | **12.7** | — | 22.0 (3) | 16.8 (5) | 10.2 (13) | Free agent | 0% |
| Tidjane Salaun | PF | 9 | 13.2 | +3.2 | 0 | **10.2** | 13.0 | 3.3 (3) | 10.3 (6) | 12.0 (13) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Isaac Okoro | SG/SF | 4 | 32.2 | +12.2 | 4 | **30.8** | 10.3 | 30.8 (4) | 22.9 (7) | 16.1 (14) | Free agent | 1% |
| Buddy Hield | SG/SF | 4 | 20.8 | +9.2 | 0 | **24.0** | 13.2 | 24.0 (4) | 22.4 (5) | 16.4 (12) | Free agent | 1% |
| Nic Claxton | C | 3 | 20.3 | +3.3 | 0 | **19.7** | 29.0 | 19.7 (3) | 23.4 (5) | 23.4 (5) | Free agent | 40% |
| Zach Collins | C | 2 | 19.5 | +12.2 | 1 | **13.0** | 6.0 | 14.0 (2) | 11.2 (4) | 7.3 (9) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 19.3 | — | 0 | **25.2** | — | 25.0 (4) | 27.6 (5) | 26.0 (10) | Free agent | 3% |

### DAL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dereck Lively II | Right Foot Surgery | 27 Nov | 23.6 | 21.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Caleb Martin | SG | 10 | 22.3 | +5.3 | 8 | **18.1** | 12.4 | 32.0 (4) | 20.0 (8) | 18.2 (11) | Free agent | 1% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cam Spencer | PG/SG | 4 | 26.8 | +3.8 | 3 | **33.2** | 29.8 | 37.6 (5) | 31.9 (9) | 29.9 (16) | Lauri Birds | 36% |
| Javon Small | PG | 4 | 24.0 | +3.0 | 0 | **24.2** | 25.0 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 4% |
| Olivier-Maxence Prosper | PF | 4 | 16.8 | +9.2 | 0 | **13.2** | 10.2 | 16.0 (5) | 11.6 (8) | 10.4 (10) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.2 | +6.6 | 10 | **46.2** | 30.4 | 35.7 (3) | 43.4 (7) | 40.1 (14) | Team Nic Kerr | 91% |
| Leaky Black | SF | 8 | 22.9 | — | 1 | **23.2** | — | 21.3 (3) | 21.0 (7) | 19.8 (10) | Free agent | 0% |
| De'Andre Hunter (day to day, ESPN est. back 20 Nov) | SF/PF | 8 | 35.6 | +8.0 | 8 | **21.4** | 23.9 | 27.5 (2) | 22.0 (5) | 20.8 (12) | Free agent | 6% |
| Dylan Cardwell | C | 7 | 17.0 | — | 2 | **19.7** | — | 17.0 (3) | 19.7 (7) | 19.7 (7) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 17.6 | — | 0 | **12.1** | — | 14.7 (3) | 12.4 (7) | 11.1 (14) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brayden Burries | SG | 5 | 29.2 | +5.4 | 5 | **32.8** | 19.4 | 26.5 (4) | 27.2 (9) | 22.8 (16) | Free agent | 12% |
| Kasparas Jakucionis | PG | 5 | 21.2 | +9.7 | 0 | **31.6** | 9.0 | 44.7 (3) | 22.4 (8) | 20.4 (15) | Free agent | 11% |
| Pete Nance | PF | 1 | 28.0 | +24.0 | 1 | **22.0** | 5.0 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% |
| Kel'el Ware | C | 5 | 19.6 | +3.2 | 1 | **20.2** | 17.8 | 26.8 (4) | 19.3 (9) | 22.9 (16) | **us** | 53% |
| AJ Green | SG | 4 | 17.0 | +4.6 | 0 | **14.2** | 6.8 | 5.7 (3) | 8.0 (8) | 11.0 (15) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 33.2 | +5.7 | 10 | **32.5** | 23.1 | 35.7 (3) | 28.4 (7) | 30.9 (13) | Team Nic Kerr | 45% |
| Trevon Brazile | SF/PF | 10 | 18.3 | — | 1 | **15.7** | — | 9.0 (3) | 12.4 (7) | 16.8 (13) | Free agent | 2% |
| Spencer Jones | SF/PF | 6 | 17.8 | — | 0 | **10.8** | — | 8.3 (3) | 10.8 (6) | 10.8 (6) | Free agent | 0% |

## Every injury

All 108 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 316 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 316 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 224 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 134 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 134 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 118 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 103 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 103 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 103 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 103 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 98 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 76 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 73 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 60 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 54 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 46 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 44 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 44 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 44 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 44 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 44 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 32 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 30 | Waivers |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 25 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 25 | Free agent |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 24 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 24 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 24 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 24 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 23 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 23 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 23 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 14 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 14 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 14 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 12 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 12 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 12 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 10 | Dr White Slong |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 10 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 10 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 10 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 10 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 10 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 10 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 28 Nov | 9 | Lauri Birds |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 8 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 8 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 8 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 27 Nov | 8 | **us** |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 27 Nov | 8 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 8 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 8 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 8 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 27 Nov | 8 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 8 | Free agent |
| Tobe Awaka | CHI | Out | Back | 25 Nov | 6 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 6 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 6 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 6 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 5 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 5 | **us** |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 4 | — |
| Jaylon Tyson | CLE | Out | Right Ankle | 23 Nov | 4 | Free agent |
| Jaylen Brown | PHI | Out | Left Hamstring | 23 Nov | 4 | Snow Time Lakers |
| Grayson Allen | CHA | Out | Concussion | 23 Nov | 4 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 23 Nov | 4 | Free agent |
| Grant Nelson | BKN | Out | Right Ankle Sprain | 23 Nov | 4 | — |
| Collin Murray-Boyles | TOR | Out | Concussion | 23 Nov | 4 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 23 Nov | 4 | Free agent |
| Austin Reaves | LAL | Out | Left Heel Bruise | 23 Nov | 4 | Cream Abdul-Yammar |
| Ronald Holland II | DET | Out | Left Knee Bruise | 22 Nov | 3 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 22 Nov | 3 | Free agent |
| Myron Gardner | MIA | Day-To-Day | Hamstring | 22 Nov | 3 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 22 Nov | 3 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 22 Nov | 3 | Free agent |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 22 Nov | 3 | Free agent |
| Draymond Green | GS | Out | Rest | 22 Nov | 3 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring Strain | 22 Nov | 3 | Free agent |
| Zach Edey | MEM | Out | Ankle | 21 Nov | 2 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 21 Nov | 2 | Free agent |
| Tyrese Maxey | PHI | Day-To-Day | Right Foot Soreness | 21 Nov | 2 | Team Nic Kerr |
| Ty Jerome | MEM | Out | Right Hip | 21 Nov | 2 | Melbourne poopoo |
| Tobi Lawal | DAL | Day-To-Day | Right Groin | 21 Nov | 2 | Free agent |
| Robert Williams III | POR | Out | Rest | 21 Nov | 2 | Free agent |
| Myles Turner | MIL | Out | Left Shoulder Bruise | 21 Nov | 2 | Free agent |
| Kyle Kuzma | MIL | Out | Right Shoulder Bruise | 21 Nov | 2 | Team Nic Kerr |
| Jerami Grant | MEM | Day-To-Day | Left Calf | 21 Nov | 2 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 21 Nov | 2 | Free agent |
| Deni Avdija | POR | Out | Foot | 21 Nov | 2 | Snow Time Lakers |
| Dean Wade | PHI | Day-To-Day | Left Hamstring Soreness | 21 Nov | 2 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 21 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 21 Nov | 2 | Melbourne poopoo |
| Adem Bona | PHI | Out | Back Sprain | 21 Nov | 2 | Free agent |
| Trey Murphy III | NO | Out | Knee Tendinitis | 20 Nov | 1 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Right Hamstring Strain | 20 Nov | 1 | Free agent |
| Steven Adams | HOU | Day-To-Day | Right Quadriceps Bruise | 20 Nov | 1 | Free agent |
| Precious Achiuwa | SAC | Day-To-Day | Left Lower Leg Bruise | 20 Nov | 1 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Back Bruise | 20 Nov | 1 | Free agent |
| Noa Essengue | CHI | Day-To-Day | Wrist Soreness | 20 Nov | 1 | Free agent |
| Kingston Flemings | ATL | Day-To-Day | Back Strain | 20 Nov | 1 | Free agent |
| Felix Okpara | WSH | Day-To-Day | Back Strain | 20 Nov | 1 | Free agent |
| De'Andre Hunter | SAC | Day-To-Day | Left Hip Soreness | 20 Nov | 1 | Free agent |
| Cade Cunningham | DET | Day-To-Day | Right Knee Soreness | 20 Nov | 1 | **us** |
| Braden Smith | IND | Day-To-Day | Right Ankle Sprain | 20 Nov | 1 | Free agent |
| Andrew Nembhard | IND | Day-To-Day | Left Hip Soreness | 20 Nov | 1 | Matt Wright's Foxies |
| Alperen Sengun | HOU | Day-To-Day | Eye | 20 Nov | 1 | Cream Abdul-Yammar |
| Alex Caruso | OKC | Day-To-Day | Right Hip Soreness | 20 Nov | 1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-20 03:47 UTC.
