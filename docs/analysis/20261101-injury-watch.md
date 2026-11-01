# Injury Watch: 01 Nov 2026

- Generated 2026-11-01 03:40 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 90 players in ESPN's injury feed. 31 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 17 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1099 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L15 and L30 cover every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (26 Oct–01 Nov) / next week (02 Nov–08 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Since the last Injury Watch

Against `docs/analysis/20261030-injury-watch.md`.

- **New long absences:**
  - Chet Holmgren (OKC; *ESPN est.* 2 Jan, was 31 Oct).
  - Ja Morant (POR; *ESPN est.* 1 Dec).
  - Yves Missi (NO; *ESPN est.* 8 Nov).
  - Team Nic Kerr dropped Holmgren and Morant.
- **No longer a long absence:** Egor Demin (*ESPN est.* 7 Nov, now inside 7 days).
- **Back from injury** (left ESPN's feed):
  - Lauri Markkanen and Jaylen Brown.
  - Alperen Sengun, Andrew Nembhard, Cameron Johnson, Naji Marshall, Oso Ighodaro, Jalen Smith, Robert Williams III and Meleek Thomas.
- **New in the feed:**
  - **Ours:** Fred VanVleet (right knee).
  - **Other managers' players:** Stephen Curry (Lauri Birds), LeBron James (Cream Abdul-Yammar), Joel Embiid and Jalen Johnson (Snow Time Lakers), Ty Jerome (Melbourne poopoo).
  - **Free agents:** Rudy Gobert.
  - The table below has *ESPN est.* for each.
- **Pickups:**
  - **Joined:** Paul Reed, whom we dropped. Derrick Jones Jr., whom Lauri Birds dropped. Jarace Walker, Larry Nance Jr., Scoot Henderson and Jase Richardson.
  - **Left:**
    - Rostered: Hartenstein (ours), Achiuwa and Isaiah Jackson (Team Nic Kerr), Wiggins (Lauri Birds).
    - Off the list: da Silva, Robinson, Okogie, Shannon, Lyles and Graves.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Desmond Bane 27.6 (L7 37.3), Trey Murphy III 27.7 (L7 32.0), Isaiah Hartenstein 28.7 (L7 34.8), Jalen Duren 33.5 (L7 —), Fred VanVleet 35.4 (L7 31.3). A pickup at or above **35.4** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Paul Reed** | DET | Jalen Duren (09 Nov) | 4 | 29.5 | +8.0 | **34.8** | 33.7 | 33.8 (4) | 33.7 (6) | 33.7 (6) | Waivers | 39% | 0 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 5 | 36.0 | +8.5 | **34.6** | 34.6 | 39.5 (4) | 34.6 (5) | 34.6 (5) | Free agent | 24% | 0 / 3 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 3 | 30.3 | +6.8 | **34.0** | 31.6 | 34.0 (3) | 31.6 (5) | 31.6 (5) | Waivers | 21% | 1 / 3 |
| **Derrick Jones Jr.** | LAC | Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov), Jordan Miller (02 Mar) | 5 | 29.0 | +3.6 | **30.8** | 30.8 | 30.0 (3) | 30.8 (5) | 30.8 (5) | Waivers | 13% | 1 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 23.0 | +10.0 | **27.3** | 19.5 | 22.2 (4) | 19.5 (6) | 19.5 (6) | Free agent | 14% | 0 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 4 | 21.0 | — | **27.2** | 27.2 | 32.0 (3) | 27.2 (4) | 27.2 (4) | Free agent | 1% | 0 / 4 |
| **Jaxson Hayes** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 28.5 | +4.8 | **27.0** | 32.2 | 26.0 (3) | 32.2 (5) | 32.2 (5) | Free agent | 18% | 0 / 4 |
| **Daniss Jenkins** | DET | Jalen Duren (09 Nov) | 4 | 27.5 | +9.0 | **27.0** | 25.0 | 27.0 (4) | 25.0 (6) | 25.0 (6) | Free agent | 7% | 0 / 3 |
| **Jarace Walker** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov); also out: Ivica Zubac (02 Nov), T.J. McConnell (02 Nov) | 2 | 25.0 | +4.0 | **23.5** | 17.0 | 24.5 (4) | 17.0 (6) | 17.0 (6) | Free agent | 1% | 1 / 3 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 3 | 24.0 | +9.2 | **23.0** | 21.6 | 24.6 (5) | 21.6 (7) | 21.6 (7) | Free agent | 2% | 0 / 4 |
| **Larry Nance Jr.** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov); also out: Ivica Zubac (02 Nov), T.J. McConnell (02 Nov) | 2 | 20.5 | +8.8 | **22.5** | 11.8 | 18.0 (4) | 11.8 (6) | 11.8 (6) | Free agent | 0% | 1 / 3 |
| **Scoot Henderson** | POR | Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 1 | 31.0 | +12.0 | **22.0** | 9.6 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% | 0 / 4 |
| **Brice Sensabaugh** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 18.5 | +4.5 | **22.0** | 16.3 | 19.0 (4) | 16.3 (6) | 16.3 (6) | Free agent | 2% | 0 / 4 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 5 | 22.8 | — | **22.0** | 22.0 | 24.2 (4) | 22.0 (5) | 22.0 (5) | Free agent | 4% | 0 / 3 |
| **Kelly Oubre Jr.** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov); also out: Ivica Zubac (02 Nov), T.J. McConnell (02 Nov) | 2 | 26.0 | +3.2 | **21.0** | 18.0 | 20.8 (4) | 18.0 (6) | 18.0 (6) | Free agent | 5% | 1 / 3 |
| **Jase Richardson** | ORL | Jalen Suggs (10 Nov), Paolo Banchero (22 Nov) | 2 | 23.5 | +8.5 | **20.5** | 14.8 | 15.0 (3) | 14.8 (5) | 14.8 (5) | Free agent | 0% | 1 / 3 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 29.0 | +8.7 | **20.0** | 16.2 | 15.5 (4) | 16.2 (6) | 16.2 (6) | Free agent | 35% | 0 / 4 |
| **Aaron Nesmith** (day to day, ESPN est. back 01 Nov) | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov); also out: Ivica Zubac (02 Nov), T.J. McConnell (02 Nov) | 2 | 24.0 | +4.0 | **20.0** | 17.8 | 20.0 (4) | 17.8 (5) | 17.8 (5) | Free agent | 3% | 1 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 08 Nov | 8 | 41.5 | — | 41.5 (2) | 41.5 (2) | 24.7 | 22.5 | Free agent | 15% | 0 / 4 |
| **Rudy Gobert** | MIN | Back Spasms | 02 Nov | 2 | 23.8 | 25.8 (4) | 23.8 (6) | 23.8 (6) | 34.3 | 38.2 | Free agent | 77% | 0 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 4 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 0 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 10 | 26.3 | 23.0 (1) | 26.3 (3) | 26.3 (3) | 29.1 | 34.7 | Free agent | 18% | 1 / 3 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 4 | — | — | — | — | 30.3 | 33.3 | Free agent | 42% | 0 / 3 |
| **Coby White** | CHA | Left Calf Strain | 02 Nov | 2 | — | — | — | — | 32.9 | 26.5 | Free agent | 64% | 0 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 02 Nov | 2 | — | — | — | — | 25.0 | 32.4 | Free agent | 6% | 0 / 4 |
| **Keegan Murray** | SAC | Ankle | 06 Nov | 6 | 12.0 | — | 12.0 (2) | 12.0 (2) | 29.3 | 31.6 | Free agent | 36% | 0 / 4 |
| **Alex Caruso** | OKC | Right Ankle | 04 Nov | 4 | 30.8 | 34.5 (2) | 30.8 (4) | 30.8 (4) | 24.0 | 18.0 | Free agent | 18% | 0 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 02 Nov | 2 | 14.2 | 8.3 (3) | 14.2 (5) | 14.2 (5) | 30.6 | 27.1 | Free agent | 13% | 0 / 3 |
| **Mitchell Robinson** | BOS | Rest | 01 Nov | 1 | 18.2 | 18.3 (3) | 18.2 (5) | 18.2 (5) | 30.3 | 28.2 | Free agent | 15% | 1 / 4 |
| **Reed Sheppard** | HOU | Back | 02 Nov | 2 | 26.8 | 31.7 (3) | 26.8 (4) | 26.8 (4) | 29.9 | 30.1 | Free agent | 60% | 0 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 06 Nov | 6 | — | — | — | — | 30.1 | 28.0 | Free agent | 46% | 0 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 07 Nov | 7 | 15.0 | 18.0 (3) | 15.0 (4) | 15.0 (4) | 30.0 | 22.2 | Free agent | 33% | 1 / 4 |
| **Obi Toppin** | IND | Back Soreness | 01 Nov | 1 | 29.0 | 27.3 (3) | 29.0 (5) | 29.0 (5) | 21.9 | 22.4 | Free agent | 13% | 1 / 3 |
| **Draymond Green** | GS | Rest | 02 Nov | 2 | 23.0 | 25.7 (3) | 23.0 (5) | 23.0 (5) | 28.5 | 26.5 | Free agent | 24% | 1 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 02 Nov | 2 | 18.6 | 18.8 (4) | 18.6 (5) | 18.6 (5) | 25.6 | 28.3 | Free agent | 3% | 0 / 4 |
| **Ziaire Williams** | LAL | Left Foot | 01 Nov | 1 | 28.2 | 26.5 (2) | 28.2 (4) | 28.2 (4) | 19.7 | 20.1 | Free agent | 4% | 1 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 10 | — | — | — | — | — | 28.1 | Free agent | 1% | 0 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 02 Nov | 2 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 0 / 4 |
| **Dylan Cardwell** | SAC | Left Calf Strain | 06 Nov | 6 | — | — | — | — | — | 26.6 | Free agent | 0% | 0 / 4 |
| **Jock Landale** | ATL | Left Hip | 02 Nov | 2 | 16.4 | 12.0 (5) | 16.4 (7) | 16.4 (7) | — | 25.8 | Free agent | 1% | 0 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 8 | — | — | — | — | 25.6 | 10.5 | Free agent | 2% | 1 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 02 Nov | 2 | — | — | — | — | 24.4 | 25.5 | Free agent | 8% | 1 / 3 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Fred VanVleet** (HOU): Out, Right Knee; ESPN est. back 02 Nov.
- **Dejounte Murray** (NO): Out, Personal; ESPN est. back 02 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Brandon Ingram | Right Achilles Surgery | 08 Nov | 35.3 | 36.5 | Melbourne poopoo |
| Max Strus | Right Foot Plantar Fasciitis | 08 Nov | 25.9 | 22.4 | Free agent |
| Bradley Beal | Right Knee Inflammation | 08 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 5 | 30.4 | +8.4 | 5 | **33.0** | 20.0 | 31.3 (3) | 32.6 (5) | 32.6 (5) | Dr White Slong | 38% |
| Derrick Jones Jr. | SF/PF | 5 | 29.0 | +3.6 | 5 | **30.8** | 21.1 | 30.0 (3) | 30.8 (5) | 30.8 (5) | Waivers | 13% |
| Isaiah Jackson | PF/C | 5 | 21.6 | +3.2 | 5 | **30.2** | 20.6 | 31.7 (3) | 30.6 (5) | 30.6 (5) | Team Nic Kerr | 8% |
| Kobe Sanders | SG | 5 | 21.8 | — | 1 | **19.0** | — | 20.3 (3) | 19.0 (5) | 19.0 (5) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Waivers |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 6 games: 3 game(s) without them, 3 with them.

Also out in those games, so part of the gain is theirs: Nikola Topic (back; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Isaiah Hartenstein | C | 3 | 25.7 | +3.3 | 3 | **35.0** | 22.3 | 34.8 (4) | 28.7 (6) | 28.7 (6) | **us** | 46% |
| Aday Mara | C | 3 | 23.0 | +10.0 | 0 | **27.3** | 11.7 | 22.2 (4) | 19.5 (6) | 19.5 (6) | Free agent | 14% |
| Jared McCain | PG/SG | 3 | 29.0 | +8.7 | 3 | **20.0** | 12.3 | 15.5 (4) | 16.2 (6) | 16.2 (6) | Free agent | 35% |
| Kenrich Williams | SF | 3 | 20.7 | +14.0 | 3 | **16.7** | 7.0 | 14.0 (4) | 11.8 (6) | 11.8 (6) | Free agent | 0% |
| Bennett Stirtz | PG | 3 | 26.3 | +21.7 | 0 | **12.3** | 2.0 | 11.0 (4) | 7.2 (6) | 7.2 (6) | Free agent | 0% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 6 | 32.0 | +7.4 | 6 | **36.2** | 23.5 | 36.5 (4) | 36.2 (6) | 36.2 (6) | **us** | 88% |
| Graham Ike | PF | 4 | 13.2 | — | 2 | **20.8** | — | 19.0 (2) | 20.8 (4) | 20.8 (4) | Free agent | 0% |
| Brandon Williams | PG/SG | 6 | 16.2 | — | 1 | **18.3** | — | 18.8 (4) | 18.3 (6) | 18.3 (6) | Free agent | 1% |
| Georges Niang | PF | 6 | 19.3 | — | 1 | **15.0** | — | 16.0 (4) | 15.0 (6) | 15.0 (6) | Free agent | 0% |
| Will Richard | SG/SF | 6 | 15.5 | — | 1 | **12.0** | — | 11.0 (4) | 12.0 (6) | 12.0 (6) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Ivica Zubac (left ankle sprain; ESPN est. 02 Nov), T.J. McConnell (right hamstring strain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jarace Walker | SF/PF | 2 | 25.0 | +4.0 | 0 | **23.5** | 13.8 | 24.5 (4) | 17.0 (6) | 17.0 (6) | Free agent | 1% |
| Larry Nance Jr. | PF | 2 | 20.5 | +8.8 | 0 | **22.5** | 6.5 | 18.0 (4) | 11.8 (6) | 11.8 (6) | Free agent | 0% |
| Kelly Oubre Jr. | SG/SF | 2 | 26.0 | +3.2 | 2 | **21.0** | 16.5 | 20.8 (4) | 18.0 (6) | 18.0 (6) | Free agent | 5% |
| Aaron Nesmith (day to day, ESPN est. back 01 Nov) | SG/SF | 2 | 24.0 | +4.0 | 2 | **20.0** | 16.3 | 20.0 (4) | 17.8 (5) | 17.8 (5) | Free agent | 3% |
| Kobe Brown | PF | 1 | 20.0 | +19.5 | 0 | **19.0** | -0.5 | 9.0 (2) | 6.0 (3) | 6.0 (3) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |
| Jalen Suggs | Right Knee | 10 Nov | 33.3 | 26.3 | Free agent |

Last 5 games: 2 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Desmond Bane | SG/SF | 2 | 36.5 | +4.8 | 2 | **37.5** | 21.0 | 37.3 (3) | 27.6 (5) | 27.6 (5) | **us** | 92% |
| Franz Wagner | SF/PF | 2 | 36.5 | +3.5 | 2 | **35.0** | 36.3 | 39.7 (3) | 35.8 (5) | 35.8 (5) | Cream Abdul-Yammar | 90% |
| Jase Richardson | SG | 2 | 23.5 | +8.5 | 2 | **20.5** | 11.0 | 15.0 (3) | 14.8 (5) | 14.8 (5) | Free agent | 0% |
| Jevon Carter | PG | 1 | 22.0 | +9.0 | 0 | **10.0** | 9.0 | 10.0 (1) | 9.5 (2) | 9.5 (2) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 3 | 33.3 | +7.1 | 3 | **44.3** | 25.8 | 31.0 (5) | 33.7 (7) | 33.7 (7) | Cream Abdul-Yammar | 69% |
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
| Toumani Camara | SF/PF | 1 | 31.0 | +6.0 | 1 | **27.0** | 32.5 | 28.3 (3) | 31.0 (5) | 31.0 (5) | Dr White Slong | 42% |
| Scoot Henderson | PG/SG | 1 | 31.0 | +12.0 | 1 | **22.0** | 6.5 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% |
| Yang Hansen | C | 1 | 13.0 | +4.5 | 0 | **16.0** | 9.5 | 14.5 (2) | 11.7 (3) | 11.7 (3) | Free agent | 0% |
| Vit Krejci | PG | 1 | 24.0 | +15.8 | 0 | **16.0** | 4.0 | 7.0 (3) | 6.4 (5) | 6.4 (5) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Maxime Raynaud | Right Knee Dislocated | 10 Nov | 26.6 | 28.1 | Free agent |
| Ben Simmons | Right Achilles Surgery | 01 Oct 2027 | 21.2 | — | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Dylan Cardwell (left calf strain; ESPN est. 06 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 6 | 36.5 | +5.9 | 6 | **37.7** | 30.4 | 46.2 (4) | 37.7 (6) | 37.7 (6) | Team Nic Kerr | 78% |
| Precious Achiuwa | PF/C | 6 | 29.0 | +4.7 | 4 | **31.3** | 24.1 | 30.0 (4) | 31.3 (6) | 31.3 (6) | Team Nic Kerr | 31% |
| Jonathan Mogbo | PF | 4 | 17.2 | +4.7 | 0 | **13.2** | 11.3 | 18.3 (3) | 13.2 (4) | 13.2 (4) | Free agent | 0% |
| Daeqwon Plowden | SG | 5 | 14.0 | — | 0 | **8.2** | — | 6.7 (3) | 8.2 (5) | 8.2 (5) | Free agent | 0% |
| Emanuel Sharp | SG | 6 | 17.8 | — | 0 | **6.3** | — | 5.0 (4) | 6.7 (6) | 6.7 (6) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 6 games: 2 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 2 | 35.0 | +5.0 | 2 | **30.5** | 29.8 | 34.5 (4) | 29.7 (6) | 29.7 (6) | Snow Time Lakers | 49% |
| Alex Sarr | PF/C | 2 | 27.5 | +3.0 | 2 | **25.0** | 27.5 | 27.8 (4) | 26.7 (6) | 26.7 (6) | Team Nic Kerr | 77% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 5 games: 3 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ja'Kobe Walter | SG | 3 | 30.3 | +6.8 | 3 | **34.0** | 28.0 | 34.0 (3) | 31.6 (5) | 31.6 (5) | Waivers | 21% |
| Allen Graves | SF | 3 | 15.7 | +3.2 | 0 | **20.0** | 19.0 | 20.0 (3) | 19.6 (5) | 19.6 (5) | Free agent | 1% |
| Jamison Battle | SF | 3 | 17.3 | +5.8 | 0 | **7.3** | 17.0 | 7.3 (3) | 11.2 (5) | 11.2 (5) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 2 | 38.5 | +11.2 | 2 | **28.5** | 38.8 | 41.0 (4) | 35.3 (6) | 35.3 (6) | Dr White Slong | 65% |
| Jaxson Hayes | C | 2 | 28.5 | +4.8 | 2 | **27.0** | 35.7 | 26.0 (3) | 32.2 (5) | 32.2 (5) | Free agent | 18% |
| Brice Sensabaugh | SG/SF | 2 | 18.5 | +4.5 | 0 | **22.0** | 13.5 | 19.0 (4) | 16.3 (6) | 16.3 (6) | Free agent | 2% |
| Isaiah Collier | PG | 2 | 22.0 | +5.0 | 0 | **15.0** | 18.0 | 17.8 (4) | 17.0 (6) | 17.0 (6) | Free agent | 4% |
| Josh Okogie | SF | 2 | 21.0 | +8.0 | 0 | **12.0** | 3.3 | 8.5 (4) | 6.8 (5) | 6.8 (5) | Free agent | 0% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 09 Nov | 31.0 | 33.5 | **us** |

Last 6 games: 4 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Paul Reed | PF/C | 4 | 29.5 | +8.0 | 4 | **34.8** | 33.5 | 33.8 (4) | 33.7 (6) | 33.7 (6) | Waivers | 39% |
| Daniss Jenkins | PG | 4 | 27.5 | +9.0 | 1 | **27.0** | 21.0 | 27.0 (4) | 25.0 (6) | 25.0 (6) | Free agent | 7% |
| Ronald Holland II | SF/PF | 4 | 17.2 | +4.8 | 0 | **21.2** | 16.0 | 21.2 (4) | 19.5 (6) | 19.5 (6) | Free agent | 1% |
| Javonte Green | SF | 4 | 20.5 | +5.0 | 0 | **12.5** | 22.0 | 12.5 (4) | 15.7 (6) | 15.7 (6) | Free agent | 1% |

### NO

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Yves Missi | Left Knee Bruise | 08 Nov | 25.1 | 41.5 | Free agent |

Last 6 games: 4 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jeremiah Fears | PG/SG | 4 | 26.8 | +4.2 | 4 | **39.5** | 6.5 | 39.5 (4) | 28.5 (6) | 28.5 (6) | Melbourne poopoo | 44% |
| DeAndre Jordan | C | 2 | 16.5 | — | 2 | **19.5** | — | 19.5 (2) | 19.5 (2) | 19.5 (2) | Free agent | 0% |
| Karlo Matkovic | PF | 4 | 18.0 | +9.0 | 2 | **17.5** | 25.0 | 17.5 (4) | 19.0 (5) | 19.0 (5) | Free agent | 0% |
| Herbert Jones | SF/PF | 4 | 23.0 | +5.5 | 2 | **17.0** | 8.0 | 17.0 (4) | 14.0 (6) | 14.0 (6) | Free agent | 2% |
| Trendon Watford | SF/PF | 2 | 17.5 | — | 0 | **16.5** | — | 16.5 (2) | 16.5 (2) | 16.5 (2) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 4 | 21.0 | — | 0 | **27.2** | — | 32.0 (3) | 27.2 (4) | 27.2 (4) | Free agent | 1% |

### BOS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Devin Carter | Illness | 08 Nov | 18.4 | 18.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

No teammate has gained 3+ minutes in those games.

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jamal Murray | PG | 5 | 38.2 | +3.2 | 5 | **47.6** | 43.9 | 57.8 (4) | 47.6 (5) | 47.6 (5) | **us** | 99% |
| Christian Braun | SG/SF | 5 | 36.0 | +8.5 | 5 | **34.6** | 23.1 | 39.5 (4) | 34.6 (5) | 34.6 (5) | Free agent | 24% |
| Trevon Brazile | SF/PF | 5 | 22.8 | — | 1 | **22.0** | — | 24.2 (4) | 22.0 (5) | 22.0 (5) | Free agent | 4% |
| Alpha Diallo (out, ESPN est. back 02 Nov) | SF | 1 | 22.0 | — | 0 | **13.0** | — | — | 13.0 (1) | 13.0 (1) | Free agent | 0% |
| Bryce Hopkins | SF | 4 | 16.5 | — | 2 | **6.5** | — | 8.0 (3) | 6.5 (4) | 6.5 (4) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 7 | 25.9 | +5.6 | 0 | **28.9** | 19.2 | 28.0 (5) | 28.9 (7) | 28.9 (7) | Lauri Birds | 34% |
| Jock Landale (out, ESPN est. back 02 Nov) | C | 7 | 15.3 | — | 0 | **16.4** | — | 12.0 (5) | 16.4 (7) | 16.4 (7) | Free agent | 1% |

## Every injury

All 90 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct 2027 | 335 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct 2027 | 335 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 243 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 153 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 153 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 122 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 122 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 122 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 122 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 117 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 95 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 63 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 63 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 63 | Waivers |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 63 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 51 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 44 | Matt Wright's Foxies |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 33 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 31 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 31 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 31 | Waivers |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 29 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 23 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 22 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 20 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 18 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 18 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 13 | Lauri Birds |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 10 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 10 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 10 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 9 | **us** |
| Yves Missi | NO | Out | Left Knee Bruise | 08 Nov | 8 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 8 | Free agent |
| Max Strus | LAC | Out | Right Foot Plantar Fasciitis | 08 Nov | 8 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 8 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 8 | Melbourne poopoo |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 08 Nov | 8 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 07 Nov | 7 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 06 Nov | 6 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 06 Nov | 6 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 06 Nov | 6 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 06 Nov | 6 | Free agent |
| Dylan Cardwell | SAC | Out | Left Calf Strain | 06 Nov | 6 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 04 Nov | 4 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 04 Nov | 4 | Free agent |
| Nikola Topic | OKC | Out | Back | 04 Nov | 4 | Free agent |
| Nic Claxton | CHI | Out | Hamstring | 04 Nov | 4 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 04 Nov | 4 | Free agent |
| Jose Alvarado | NY | Out | Left Ankle Sprain | 04 Nov | 4 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 04 Nov | 4 | Free agent |
| Alex Caruso | OKC | Out | Right Ankle | 04 Nov | 4 | Free agent |
| Ty Jerome | MEM | Out | Back Soreness | 02 Nov | 2 | Melbourne poopoo |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 02 Nov | 2 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 02 Nov | 2 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 02 Nov | 2 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 02 Nov | 2 | Free agent |
| Stephen Curry | GS | Out | Rest | 02 Nov | 2 | Lauri Birds |
| Spencer Jones | DEN | Out | Hamstring | 02 Nov | 2 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 02 Nov | 2 | Free agent |
| Santi Aldama | DAL | Out | Right Knee Surgery | 02 Nov | 2 | Free agent |
| Rudy Gobert | MIN | Out | Back Spasms | 02 Nov | 2 | Free agent |
| Reed Sheppard | HOU | Out | Back | 02 Nov | 2 | Free agent |
| Quinten Post | MEM | Out | Right Ankle | 02 Nov | 2 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 02 Nov | 2 | — |
| Mikel Brown Jr. | BKN | Out | Rest | 02 Nov | 2 | Free agent |
| LeBron James | PHI | Out | Back | 02 Nov | 2 | Cream Abdul-Yammar |
| Kylan Boswell | CHA | Out | Right Knee Surgery | 02 Nov | 2 | — |
| Kon Knueppel | CHA | Out | Left Hamstring | 02 Nov | 2 | Team Nic Kerr |
| Jordan Poole | NO | Out | Left Ankle Sprain | 02 Nov | 2 | Free agent |
| Joel Embiid | PHI | Out | Right Foot | 02 Nov | 2 | Snow Time Lakers |
| Jock Landale | ATL | Out | Left Hip | 02 Nov | 2 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 02 Nov | 2 | Free agent |
| Jalen Johnson | ATL | Day-To-Day | Left Ankle | 02 Nov | 2 | Snow Time Lakers |
| Ivica Zubac | IND | Out | Left Ankle Sprain | 02 Nov | 2 | Lauri Birds |
| Isaiah Joe | DET | Out | Right Hip Bruise | 02 Nov | 2 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 02 Nov | 2 | Free agent |
| Fred VanVleet | HOU | Out | Right Knee | 02 Nov | 2 | **us** |
| Draymond Green | GS | Out | Rest | 02 Nov | 2 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 02 Nov | 2 | Free agent |
| Dejounte Murray | NO | Out | Personal | 02 Nov | 2 | **us** |
| Dailyn Swain | CHI | Day-To-Day | Back Soreness | 02 Nov | 2 | Free agent |
| Coby White | CHA | Out | Left Calf Strain | 02 Nov | 2 | Free agent |
| Alpha Diallo | DEN | Out | Right Personal | 02 Nov | 2 | Free agent |
| Ziaire Williams | LAL | Day-To-Day | Left Foot | 01 Nov | 1 | Free agent |
| Obi Toppin | IND | Day-To-Day | Back Soreness | 01 Nov | 1 | Free agent |
| Mitchell Robinson | BOS | Day-To-Day | Rest | 01 Nov | 1 | Free agent |
| Gui Santos | GS | Day-To-Day | Left Knee | 01 Nov | 1 | Free agent |
| Adou Thiero | LAL | Out | Left Knee Inflammation | 01 Nov | 1 | Free agent |
| Aaron Nesmith | IND | Day-To-Day | Left Hamstring Strain | 01 Nov | 1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-01 03:40 UTC.
