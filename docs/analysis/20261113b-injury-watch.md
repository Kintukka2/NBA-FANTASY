# Injury Watch: 13 Nov 2026

- Generated 2026-11-13 21:42 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 104 players in ESPN's injury feed. 33 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (09 Nov–15 Nov) / next week (16 Nov–22 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Research

No NBA games have been played since the morning run, so the tables match [20261113-injury-watch.md](20261113-injury-watch.md) and its research still holds. New since then:
- **Dejounte Murray** (ours): out 13 Nov (left ankle sprain) and sitting out until traded, per Shams ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)); *ESPN est.* 20 Nov.
- **Trey Murphy III** (ours): ruled out 13 Nov, aiming for 14 Nov ([CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-friday-538912/)); *ESPN est.* 14 Nov.
- **Maxime Raynaud:** out 13 Nov ([Yahoo, 13 Nov](https://sports.yahoo.com/articles/kings-injury-report-every-status-150005259.html)); our floor is 16 Nov.
- **Zach Edey:** resting 13 Nov ([CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-ruled-out-for-friday/)); *ESPN est.* 14 Nov.
- **Pending trades (new):**
  - We offered Dr White Slong **Hartenstein + Murphy for RJ Barrett**, expiring 15 Nov 08:21 UTC. Barrett: rate 36.5; season 37.2 (12), L7 37.2 (4), L15 35.5 (8). Hartenstein's rate is 33.2 and Murphy's 35.5.
  - Snow Time Lakers offered **Kyrie + Jalen Johnson for Lendeborg + Jamal Murray**, expiring 15 Nov 09:27 UTC.
  - The earlier Herro + Kyrie for Cade offer is gone.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Daniel Gafford 29.1 (L7 24.0), Daniss Jenkins 29.3 (L7 52.0), Dejounte Murray 30.6 (L7 14.5), Trey Murphy III 31.0 (L7 38.5), Isaiah Hartenstein 31.5 (L7 35.0). A pickup at or above **31.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Duncan Robinson** | DET | Jalen Duren (24 Nov) | 9 | 32.7 | +4.7 | **31.8** | 31.4 | 22.0 (3) | 33.8 (6) | 31.4 (11) | Waivers | 61% | 1 / 4 |
| **Grayson Allen** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 30.0 | +3.0 | **30.0** | 26.9 | 30.0 (3) | 28.7 (7) | 26.9 (12) | Free agent | 28% | 1 / 2 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 9 | 24.1 | +10.1 | **29.9** | 25.3 | 32.5 (4) | 31.9 (7) | 25.3 (12) | Free agent | 24% | 2 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 10 | 34.3 | +6.8 | **29.5** | 29.5 | 22.0 (3) | 30.2 (6) | 29.5 (10) | Free agent | 35% | 1 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 18.3 | — | **28.2** | 26.0 | 30.0 (2) | 27.5 (4) | 26.0 (7) | Free agent | 3% | 1 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (12 Dec) | 10 | 25.8 | +5.5 | **27.6** | 28.2 | 32.0 (3) | 27.9 (7) | 28.2 (12) | Free agent | 41% | 2 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 9 | 29.2 | +3.8 | **27.6** | 27.6 | 21.0 (2) | 22.8 (5) | 27.6 (9) | Free agent | 10% | 2 / 3 |
| **Jaxson Hayes** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (20 Nov) | 4 | 28.2 | +6.2 | **26.8** | 27.4 | 26.5 (4) | 23.4 (7) | 27.4 (11) | Waivers | 14% | 2 / 4 |
| **Ryan Kalkbrenner** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 24.0 | +7.1 | **25.3** | 21.0 | 25.3 (3) | 21.7 (7) | 21.0 (12) | Free agent | 3% | 1 / 2 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 9 | 28.1 | +7.1 | **24.4** | 21.4 | 35.0 (4) | 25.1 (7) | 21.4 (12) | Free agent | 36% | 2 / 3 |
| **Kevin Huerter** | DET | Jalen Duren (24 Nov) | 9 | 24.1 | +4.1 | **23.7** | 21.6 | 36.0 (3) | 27.0 (6) | 21.6 (11) | Free agent | 6% | 1 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 10 | 31.6 | +10.0 | **23.3** | 24.1 | 18.0 (4) | 19.1 (8) | 24.1 (12) | Free agent | 12% | 1 / 3 |
| **Dylan Cardwell** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 4 | 18.8 | — | **21.8** | 21.8 | 22.7 (3) | 21.8 (4) | 21.8 (4) | Free agent | 1% | 2 / 3 |
| **Sion James** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 3 | 28.7 | +3.4 | **21.3** | 15.7 | 21.3 (3) | 19.4 (7) | 15.7 (12) | Free agent | 1% | 1 / 2 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 4 | 25.0 | +3.8 | **21.0** | 19.2 | 21.0 (4) | 18.6 (8) | 19.2 (11) | Free agent | 1% | 1 / 4 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (15 Nov) | 9 | 32.8 | +5.2 | **20.8** | 19.5 | 20.0 (2) | 19.3 (6) | 19.5 (10) | Free agent | 6% | 2 / 3 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 8 | 18.0 | +3.0 | **20.6** | 20.6 | 17.7 (3) | 20.0 (7) | 20.6 (12) | Free agent | 1% | 1 / 4 |
| **Kobe Sanders** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 10 | 24.3 | — | **20.4** | 20.0 | 18.0 (2) | 20.5 (6) → 24.8 (5) | 20.0 (10) → 22.3 (9) | Free agent | 1% | 2 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 14 Nov | 1 | 41.5 | — | — | 41.5 (2) → 68.0 (1) | 24.7 | 22.5 | Free agent | 15% | 2 / 4 |
| **Zach Edey** | MEM | Left Ankle | 14 Nov | 1 | 22.8 | 16.3 (3) | 21.1 (7) | 22.8 (10) | 33.2 | 39.5 | Free agent | 43% | 2 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 7 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 2 / 4 |
| **Norman Powell** | CHI | Right Shoulder Inflammation | 13 Nov | 0 | 26.2 | — | 16.3 (3) → 22.5 (2) | 26.2 (8) → 29.4 (7) | 36.0 | 33.0 | Free agent | 74% | 2 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 13 Nov | 0 | 26.3 | — | — | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 1 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 21 Nov | 8 | 14.2 | — | 3.0 (1) | 14.2 (5) | 30.6 | 27.1 | Free agent | 9% | 2 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 6 | — | — | — | — | 30.1 | 28.0 | Free agent | 42% | 2 / 3 |
| **Collin Sexton** | LAL | Head | 15 Nov | 2 | 17.7 | 17.8 (4) | 17.6 (8) | 17.7 (12) | 28.8 | 26.6 | Free agent | 21% | 1 / 3 |
| **Devin Vassell** | SA | Left Groin | 13 Nov | 0 | 28.3 | 37.0 (2) | 27.2 (5) | 28.3 (10) | 26.8 | 27.3 | Free agent | 37% | 2 / 3 |
| **Quentin Grimes** | LAL | Finger | 15 Nov | 2 | 16.6 | 14.0 (2) | 11.7 (6) | 16.6 (11) | 28.1 | 25.8 | Free agent | 26% | 1 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 2 | — | — | — | — | — | 28.1 | Free agent | 2% | 2 / 3 |
| **Precious Achiuwa** | SAC | Left Ankle Soreness | 15 Nov | 2 | 28.0 | 20.7 (3) | 27.9 (7) | 28.0 (11) → 30.5 (10) | 24.1 | 27.0 | Free agent | 20% | 2 / 3 |
| **Bennedict Mathurin** | NO | Right Thumb Sprain | 13 Nov | 0 | 9.8 | 5.3 (3) | 7.7 (7) | 9.8 (11) | 25.1 | 27.6 | Free agent | 7% | 2 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 5 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 2 / 3 |
| **Nolan Traore** | BKN | Right Calf Soreness | 14 Nov | 1 | 26.6 | 33.0 (2) | 32.7 (6) | 26.6 (10) → 29.2 (9) | 21.6 | 17.5 | Free agent | 12% | 1 / 3 |
| **Tristan da Silva** | ORL | Left Calf Strain | 13 Nov | 0 | 25.9 | 35.0 (1) | 24.6 (5) | 25.9 (9) | 17.2 | 21.2 | Free agent | 9% | 1 / 4 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 13 Nov | 0 | 15.3 | 15.3 (3) | 15.3 (3) | 15.3 (3) | 24.4 | 25.5 | Free agent | 8% | 2 / 3 |
| **Pelle Larsson** | MIA | Illness | 13 Nov | 0 | 25.1 | 28.0 (2) | 23.3 (6) | 25.1 (11) | — | 23.7 | Free agent | 11% | 2 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 15 Nov | 2 | — (—) | 28.1 (74) | Free agent | 2% | 2 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 5 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 2 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 19 Nov | 6 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 2 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 19 Nov | 6 | 30.1 (30.5) | 28.0 (63) | Free agent | 42% | 2 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 7 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 2 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 16 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 2 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 50 | 38.8 (32.4) | 41.6 (38) | Free agent | 28% | 1 / 4 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 50 | 36.9 (27.7) | 32.3 (32) | Free agent | 33% | 1 / 4 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 82 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 1 / 3 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 109 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 1 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 140 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 4 |

## Our injured players

- **Paul George** (BOS): Day-To-Day, Illness; ESPN est. back 15 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Dejounte Murray** (NO): Out, Ankle; ESPN est. back 20 Nov.
- **Trey Murphy III** (NO): Out, Knee Tendinitis; ESPN est. back 14 Nov.
- **Scottie Barnes** (TOR): Out, Left Groin Soreness; ESPN est. back 15 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |
| Brandon Williams | Left Hamstring | 22 Nov | 22.2 | 18.8 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection. Split on Jimmy Butler III alone: the others still played in those games.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 10 | 31.9 | +3.3 | 10 | **42.6** | 33.7 | 44.0 (3) | 39.7 (7) → 46.7 (6) | 41.4 (12) → 45.4 (11) | **us** | 95% |
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 8 | 16.9 | — | 1 | **19.1** | — | 10.5 (2) | 18.4 (5) | 18.8 (10) | Free agent | 1% |
| Georges Niang | PF | 10 | 21.1 | — | 2 | **17.1** | — | 17.3 (3) | 19.3 (7) | 16.4 (12) | Free agent | 1% |
| Will Richard | SG/SF | 9 | 18.6 | — | 3 | **12.6** | — | 12.5 (2) | 13.2 (6) | 12.7 (11) | Free agent | 0% |
| Gary Payton II | SG | 8 | 13.1 | — | 0 | **10.2** | — | 9.0 (1) | 11.6 (5) | 9.9 (10) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 9 | 24.1 | +10.1 | 3 | **29.9** | 7.0 | 32.5 (4) | 31.9 (7) | 25.3 (12) | Free agent | 24% |
| Jared McCain | PG/SG | 9 | 28.1 | +7.1 | 6 | **24.4** | 2.0 | 35.0 (4) | 25.1 (7) | 21.4 (12) | Free agent | 36% |
| Bennett Stirtz | PG | 9 | 23.2 | +12.2 | 0 | **19.8** | 7.0 | 22.8 (4) | 22.6 (7) | 15.2 (12) | Free agent | 2% |
| Kenrich Williams | SF | 9 | 23.2 | +16.2 | 8 | **16.8** | 6.0 | 14.0 (4) | 17.9 (7) | 14.3 (12) | Free agent | 1% |
| Jaylin Williams (out, ESPN est. back 15 Nov) | PF/C | 4 | 23.0 | +18.0 | 1 | **10.8** | -1.0 | — | 8.5 (2) | 9.1 (7) | Free agent | 1% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 4 | 25.0 | +3.8 | 2 | **21.0** | 18.8 | 21.0 (4) | 18.6 (8) | 19.2 (11) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 16 Nov) | SG | 3 | 18.3 | +9.7 | 0 | **16.7** | 4.3 | 16.7 (3) | 10.5 (6) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | — | 0 | **12.0** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 22 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard | PG/SG | 7 | 33.9 | +3.9 | 7 | **37.3** | 25.0 | 36.0 (3) | 36.7 (6) | 35.3 (10) | Matt Wright's Foxies | 74% |
| Ivica Zubac | C | 4 | 24.2 | +17.2 | 4 | **26.8** | 6.0 | 35.3 (3) | 26.8 (4) | 26.1 (7) → 29.5 (6) | Lauri Birds | 72% |
| Aaron Nesmith (day to day, ESPN est. back 13 Nov) | SG/SF | 7 | 27.3 | +7.3 | 7 | **18.4** | 20.0 | 12.0 (3) | 17.3 (6) | 17.7 (10) | Free agent | 3% |
| Jalen Slawson | SF | 7 | 17.0 | +11.5 | 1 | **15.0** | 2.5 | 12.5 (2) | 15.7 (6) | 13.9 (10) | Free agent | 0% |
| Braden Smith | PG | 7 | 15.1 | +15.1 | 4 | **14.4** | 0.0 | 4.0 (2) | 16.5 (6) | 12.6 (8) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 8 | 33.4 | +8.9 | 8 | **42.2** | 11.0 | 36.3 (3) | 41.6 (7) | 36.8 (12) | Cream Abdul-Yammar | 82% |
| LaMelo Ball | PG | 8 | 28.9 | +4.9 | 8 | **39.1** | 26.0 | 42.3 (3) | 42.4 (7) | 36.3 (12) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 8 | 15.8 | +5.8 | 0 | **28.2** | 12.5 | 27.3 (3) | 29.3 (7) | 21.8 (12) | Free agent | 3% |
| Joan Beringer | C | 8 | 18.0 | +3.0 | 1 | **20.6** | 26.5 | 17.7 (3) | 20.0 (7) | 20.6 (12) | Free agent | 1% |
| Trey Lyles | PF | 8 | 20.2 | +6.8 | 0 | **16.6** | 11.5 | 21.0 (3) | 15.9 (7) | 14.8 (12) | Free agent | 1% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 10 games: 4 game(s) without them, 6 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 20 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 4 | 34.5 | +3.2 | 4 | **34.5** | 31.7 | 32.5 (4) | 27.7 (7) | 31.2 (12) | Dr White Slong | 65% |
| Jaxson Hayes | C | 4 | 28.2 | +6.2 | 4 | **26.8** | 22.2 | 26.5 (4) | 23.4 (7) | 27.4 (11) | Waivers | 14% |
| Brice Sensabaugh | SG/SF | 4 | 17.0 | +3.5 | 0 | **20.2** | 12.0 | 14.5 (4) | 13.6 (7) | 14.6 (12) | Free agent | 1% |
| Isaiah Collier | PG | 4 | 19.0 | +5.3 | 0 | **16.8** | 13.7 | 16.2 (4) | 13.7 (7) | 15.0 (12) | Free agent | 3% |
| Kyle Filipowski | PF/C | 2 | 15.0 | +9.2 | 0 | **12.5** | 2.5 | 8.3 (3) | 8.2 (5) | 5.0 (8) | Free agent | 3% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Grayson Allen | PG/SG | 3 | 30.0 | +3.0 | 3 | **30.0** | 26.3 | 30.0 (3) | 28.7 (7) | 26.9 (12) | Free agent | 28% |
| Ryan Kalkbrenner | C | 3 | 24.0 | +7.1 | 2 | **25.3** | 17.7 | 25.3 (3) | 21.7 (7) | 21.0 (12) | Free agent | 3% |
| Sion James | SF | 3 | 28.7 | +3.4 | 2 | **21.3** | 15.4 | 21.3 (3) | 19.4 (7) | 15.7 (12) | Free agent | 1% |
| Hannes Steinbach | PF | 2 | 20.0 | +14.5 | 0 | **18.0** | 0.5 | 18.0 (2) | 9.2 (4) | 10.0 (5) | Free agent | 1% |
| Royce O'Neale | SF/PF | 3 | 23.7 | +5.4 | 0 | **17.7** | 9.0 | 17.7 (3) | 13.9 (7) | 12.5 (12) | Free agent | 1% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 19 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 28.7 | +6.7 | 10 | **30.7** | 20.0 | 20.0 (2) | 27.0 (6) | 30.5 (10) | Team Nic Kerr | 37% |
| Derrick Jones Jr. | SF/PF | 9 | 29.2 | +3.8 | 9 | **27.6** | 21.1 | 21.0 (2) | 22.8 (5) | 27.6 (9) | Free agent | 10% |
| Kobe Sanders | SG | 10 | 24.3 | — | 2 | **20.4** | — | 18.0 (2) | 20.5 (6) → 24.8 (5) | 20.0 (10) → 22.3 (9) | Free agent | 1% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 9 | 34.6 | +5.6 | 9 | **37.8** | 29.0 | 37.6 (5) | 37.8 (8) | 34.8 (13) | Snow Time Lakers | 76% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 9 | 38.1 | +5.1 | 9 | **46.8** | 25.0 | 56.3 (3) | 50.4 (7) | 43.7 (11) | Cream Abdul-Yammar | 93% |
| Desmond Bane | SG/SF | 8 | 35.8 | +8.8 | 8 | **32.2** | -1.0 | 31.0 (2) | 31.3 (6) | 28.4 (10) → 31.7 (9) | Cream Abdul-Yammar | 90% |
| Wendell Carter Jr. | C | 9 | 33.6 | +4.6 | 9 | **31.6** | 47.0 | 33.7 (3) | 33.9 (7) | 34.3 (11) | Dr White Slong | 61% |
| Jase Richardson | SG | 9 | 23.3 | +9.3 | 7 | **15.4** | 12.0 | 11.7 (3) | 17.1 (7) | 15.3 (11) | Free agent | 0% |
| Jamal Cain (day to day, ESPN est. back 13 Nov) | SF | 8 | 21.2 | +10.2 | 2 | **15.4** | -3.0 | 27.5 (2) | 16.5 (6) | 11.3 (10) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 10 | 34.1 | +3.3 | 10 | **36.8** | 32.6 | 37.2 (4) | 35.5 (8) | 37.2 (12) | Dr White Slong | 83% |
| Ja'Kobe Walter | SG | 10 | 31.6 | +10.0 | 10 | **23.3** | 17.6 | 18.0 (4) | 19.1 (8) | 24.1 (12) | Free agent | 12% |
| Alijah Martin | SG | 9 | 14.3 | — | 0 | **17.0** | — | 26.5 (4) | 19.6 (7) | 13.8 (11) | Free agent | 0% |
| Jamison Battle | SF | 10 | 20.9 | — | 0 | **16.1** | — | 20.0 (4) | 17.5 (8) | 16.2 (12) | Free agent | 0% |
| Allen Graves | SF | 10 | 13.8 | — | 0 | **11.7** | — | 10.0 (4) | 9.4 (8) | 13.0 (12) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Waivers |

Last 10 games: 0 game(s) without them, 10 with them.

No game yet without them. Same-position teammates by current minutes: Norman Powell (SG/SF, 28.9 min, 26.2 FP/g, Free agent), Matas Buzelis (SF/PF, 26.3 min, 20.4 FP/g, Free agent), Isaac Okoro (SG/SF, 19.1 min, 10.2 FP/g, Free agent), Leonard Miller (SF, 15.9 min, 14.2 FP/g, Free agent).

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cade Cunningham | PG | 9 | 35.1 | +5.1 | 9 | **53.3** | 39.0 | 55.7 (3) | 54.8 (6) | 50.7 (11) | **us** | 100% |
| Ausar Thompson | SF/PF | 8 | 29.4 | +10.4 | 8 | **36.8** | 18.0 | 42.7 (3) | 39.7 (6) | 34.8 (10) | Lauri Birds | 78% |
| Duncan Robinson | SG/SF | 9 | 32.7 | +4.7 | 9 | **31.8** | 31.0 | 22.0 (3) | 33.8 (6) | 31.4 (11) | Waivers | 61% |
| Daniss Jenkins | PG | 9 | 29.3 | +7.3 | 3 | **31.1** | 31.0 | 52.0 (3) | 31.5 (6) | 29.3 (11) | **us** | 31% |
| Kevin Huerter | SG/SF | 9 | 24.1 | +4.1 | 0 | **23.7** | 17.0 | 36.0 (3) | 27.0 (6) | 21.6 (11) | Free agent | 6% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Scotty Pippen Jr. | Back Soreness | 21 Nov | 25.1 | 14.2 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Javon Small | PG | 4 | 20.0 | — | 0 | **16.2** | — | 17.0 (3) | 16.2 (4) | 16.2 (4) | Free agent | 0% |
| Kris Murray | PF | 5 | 13.8 | +5.8 | 0 | **9.0** | 5.0 | 2.5 (2) | 7.7 (6) | 7.9 (7) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 18.3 | — | 0 | **28.2** | — | 30.0 (2) | 27.5 (4) | 26.0 (7) | Free agent | 3% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 15 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.5 | +6.9 | 10 | **45.0** | 30.4 | 50.3 (3) | 50.1 (7) | 41.4 (11) → 44.6 (10) | Team Nic Kerr | 90% |
| Dylan Cardwell | C | 4 | 18.8 | — | 1 | **21.8** | — | 22.7 (3) | 21.8 (4) | 21.8 (4) | Free agent | 1% |
| De'Andre Hunter | SF/PF | 9 | 32.8 | +5.2 | 9 | **20.8** | 23.9 | 20.0 (2) | 19.3 (6) | 19.5 (10) | Free agent | 6% |
| Leaky Black | SF | 7 | 19.0 | — | 1 | **19.1** | — | 23.0 (3) | 24.4 (5) | 19.1 (7) | Free agent | 1% |
| Jonathan Mogbo | PF | 4 | 15.8 | +3.2 | 0 | **13.8** | 11.3 | 0.0 (1) | 14.0 (2) | 10.6 (5) | Free agent | 0% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 34.3 | +6.8 | 10 | **29.5** | 23.1 | 22.0 (3) | 30.2 (6) | 29.5 (10) | Free agent | 35% |
| Trevon Brazile | SF/PF | 10 | 19.6 | — | 1 | **19.1** | — | 13.0 (3) | 16.8 (6) | 19.1 (10) | Free agent | 2% |
| Spencer Jones | SF/PF | 3 | 19.0 | — | 0 | **13.3** | — | 13.3 (3) | 13.3 (3) | 13.3 (3) | Free agent | 1% |
| Bryce Hopkins | SF | 7 | 14.3 | — | 2 | **9.0** | — | 3.0 (2) | 12.3 (3) | 9.0 (7) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.8 | +5.5 | 0 | **27.6** | 19.2 | 32.0 (3) | 27.9 (7) | 28.2 (12) | Free agent | 41% |
| Jock Landale | C | 6 | 14.0 | — | 0 | **12.8** | — | 17.0 (1) | 12.3 (3) → 18.5 (2) | 16.5 (8) → 18.9 (7) | Free agent | 0% |

## Every injury

All 104 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 322 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 322 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 230 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 140 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 140 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 109 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 109 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 109 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 109 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 104 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 82 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 60 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 52 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 50 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 50 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 50 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 50 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 50 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 38 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 31 | Matt Wright's Foxies |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 30 | Waivers |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 29 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 29 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 29 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 20 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 20 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 18 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 18 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 18 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 16 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 16 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 12 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 11 | **us** |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 10 | **us** |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 22 Nov | 9 | Lauri Birds |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 9 | Dr White Slong |
| Brandon Williams | GS | Out | Left Hamstring | 22 Nov | 9 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 21 Nov | 8 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 20 Nov | 7 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 20 Nov | 7 | — |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 7 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 20 Nov | 7 | **us** |
| Asa Newell | ATL | Out | Left Toe | 20 Nov | 7 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 19 Nov | 6 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 19 Nov | 6 | Melbourne poopoo |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 18 Nov | 5 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 18 Nov | 5 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 5 | Free agent |
| Marcus Smart | HOU | Suspension | Suspension | 18 Nov | 5 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 5 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 5 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 18 Nov | 5 | Free agent |
| Adem Bona | PHI | Out | Back Sprain | 18 Nov | 5 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 17 Nov | 4 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 17 Nov | 4 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 16 Nov | 3 | Free agent |
| Trey Alexander | UTAH | Out | Right Ankle Sprain | 16 Nov | 3 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 16 Nov | 3 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 16 Nov | 3 | Free agent |
| Chris Youngblood | POR | Out | Right Foot Bruise | 16 Nov | 3 | Free agent |
| Trayce Jackson-Davis | TOR | Day-To-Day | Illness | 15 Nov | 2 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 15 Nov | 2 | Free agent |
| Scottie Barnes | TOR | Out | Left Groin Soreness | 15 Nov | 2 | **us** |
| Quentin Grimes | LAL | Day-To-Day | Finger | 15 Nov | 2 | Free agent |
| Precious Achiuwa | SAC | Out | Left Ankle Soreness | 15 Nov | 2 | Free agent |
| Paul George | BOS | Day-To-Day | Illness | 15 Nov | 2 | **us** |
| Nate Bittle | TOR | Out | Right Foot Fracture | 15 Nov | 2 | — |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 15 Nov | 2 | Free agent |
| Luka Doncic | LAL | Day-To-Day | Right Ankle | 15 Nov | 2 | Team Nic Kerr |
| LeBron James | PHI | Day-To-Day | Back | 15 Nov | 2 | Cream Abdul-Yammar |
| Jaylin Williams | OKC | Out | Back Spasms | 15 Nov | 2 | Free agent |
| Drew Timme | PHX | Day-To-Day | Right Hand | 15 Nov | 2 | Free agent |
| Collin Sexton | LAL | Day-To-Day | Head | 15 Nov | 2 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 15 Nov | 2 | Free agent |
| Bub Carrington | WSH | Day-To-Day | Chest | 15 Nov | 2 | Free agent |
| Brandon Miller | CHA | Day-To-Day | Right Groin Soreness | 15 Nov | 2 | Matt Wright's Foxies |
| Austin Reaves | LAL | Day-To-Day | Left Heel | 15 Nov | 2 | Cream Abdul-Yammar |
| Zach Edey | MEM | Out | Left Ankle | 14 Nov | 1 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 14 Nov | 1 | Free agent |
| Trey Murphy III | NO | Out | Knee Tendinitis | 14 Nov | 1 | **us** |
| Trendon Watford | NO | Out | Right Ankle Sprain | 14 Nov | 1 | Free agent |
| Tobe Awaka | CHI | Out | Back | 14 Nov | 1 | Free agent |
| Quinten Post | MEM | Out | Concussion | 14 Nov | 1 | Free agent |
| Nolan Traore | BKN | Day-To-Day | Right Calf Soreness | 14 Nov | 1 | Free agent |
| Mikel Brown Jr. | BKN | Day-To-Day | Illness | 14 Nov | 1 | Free agent |
| Kevin McCullar Jr. | TOR | Day-To-Day | Illness | 14 Nov | 1 | Free agent |
| Evan Mobley | CLE | Out | Toe | 14 Nov | 1 | Matt Wright's Foxies |
| Bryce McGowens | NO | Out | Left Elbow Infection | 14 Nov | 1 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 13 Nov | 0 | Free agent |
| Tristan da Silva | ORL | Day-To-Day | Left Calf Strain | 13 Nov | 0 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Right Hamstring Strain | 13 Nov | 0 | Free agent |
| Pelle Larsson | MIA | Day-To-Day | Illness | 13 Nov | 0 | Free agent |
| Norman Powell | CHI | Day-To-Day | Right Shoulder Inflammation | 13 Nov | 0 | Free agent |
| Klay Thompson | MIA | Day-To-Day | Left Ankle Soreness | 13 Nov | 0 | Melbourne poopoo |
| Kingston Flemings | ATL | Day-To-Day | Back | 13 Nov | 0 | Free agent |
| Jamal Cain | ORL | Day-To-Day | Left Shoulder Bruise | 13 Nov | 0 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 13 Nov | 0 | Free agent |
| Devin Vassell | SA | Day-To-Day | Left Groin | 13 Nov | 0 | Free agent |
| De'Aaron Fox | SA | Day-To-Day | Left Hip Soreness | 13 Nov | 0 | Matt Wright's Foxies |
| Dailyn Swain | CHI | Day-To-Day | Right Back | 13 Nov | 0 | Free agent |
| Charles Bassey | GS | Day-To-Day | Left Toe Soreness | 13 Nov | 0 | Free agent |
| Bennedict Mathurin | NO | Day-To-Day | Right Thumb Sprain | 13 Nov | 0 | Free agent |
| Ajay Mitchell | OKC | Day-To-Day | Left Ankle Sprain | 13 Nov | 0 | Lauri Birds |
| Aaron Nesmith | IND | Day-To-Day | Right Knee Soreness | 13 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-13 21:42 UTC.
- [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)
- [CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-friday-538912/)
- [Yahoo, 13 Nov](https://sports.yahoo.com/articles/kings-injury-report-every-status-150005259.html)
- [CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-ruled-out-for-friday/)
