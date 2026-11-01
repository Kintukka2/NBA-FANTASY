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

## Shortlist

Our five lowest are Bane 27.6 (L7 37.3 (3)), Murphy 27.7 (L7 32.0 (4)), Hartenstein 28.7 (L7 34.8 (4)), Duren 33.5 (IR) and VanVleet 35.4 (L7 31.3 (3)), so the floor is 35.4. Nobody on the list clears it, but three come close:

| Player | NBA | Opening and its window | FP/g without | Season | L7 / L15 / L30 | Min without | Games this / next week |
|---|---|---|---:|---:|---|---:|---|
| **Christian Braun** | DEN | Starter, not tied to an injury | 34.6 | 34.6 | 39.5 (4) / 34.6 (5) / 34.6 (5) | 36.0 | 0 / 3 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard: 3–4 weeks (Haynes); *ESPN est.* 23 Nov | 34.0 | 31.6 | 34.0 (3) / 31.6 (5) / 31.6 (5) | 30.3 | 1 / 3 |
| **Paul Reed** | DET | Jalen Duren: possible return about 9 Nov; *ESPN est.* 9 Nov | 34.8 | 33.7 | 33.8 (4) / 33.7 (6) / 33.7 (6) | 29.5 | 0 / 3 |
| Aday Mara | OKC | Holmgren: 8–10 weeks; *ESPN est.* 2 Jan | 27.3 | 19.5 | 22.2 (4) / 19.5 (6) / 19.5 (6) | 23.0 | 0 / 4 |
| Derrick Jones Jr. | LAC | Ingram and Strus at least another week; *ESPN est.* 8 Nov | 30.8 | 30.8 | 30.0 (3) / 30.8 (5) / 30.8 (5) | 29.0 | 1 / 3 |

- **Braun** has the steadiest role, but his L7 rests on a 31-point night and a run of steals that should regress.
- **Walter** is the longest-lasting opening, and he is on waivers after we dropped him.
- **Reed** has about a week of starts left.
- **Mara**'s role lasts two months, but at 23 minutes he scores below our floor.
- **Back-soon stash:** **Yves Missi** (NO; 41.5 in 2 games, projected 24.7; no timetable reported; *ESPN est.* 8 Nov). The matchup plan adds him for Sunday 8 Nov. Our IR slot holds Duren.

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

### Notes

- **Paul Reed** starts at center while Duren is out: 12 points on 30 Oct, and 22-9-3 on 27 Oct. Duren's possible return around 9 Nov leaves about a week of starts [Yahoo Sports, 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html). We dropped him on 31 Oct, and he is on waivers.
- **Christian Braun** is an entrenched starter. He scored 31 with seven threes at Phoenix on 30 Oct [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/christian-braun-with-31-points-hits-7-3-pointers). His L7 (+4.9, just under the flag) comes from that shooting night and three steals in each of his last three games against a career 0.7; expect the steals to regress. No injury ties to his role.
- **Ja'Kobe Walter** keeps starting in Leonard's place: 32 minutes and 9 points on 30 Oct [Yahoo Sports game log](https://sports.yahoo.com/nba/players/10278/). The start lasts until Leonard returns, mid-to-late November.
- **Derrick Jones Jr.** starts while Ingram and Strus are out at least another week and Beal has no timetable [Yahoo Sports game log](https://sports.yahoo.com/nba/players/5747/). Lauri Birds dropped him.
- **Aday Mara** played 27:43 with 4 blocks at Houston, and Holmgren's 8–10 week absence makes the role last [Yahoo Sports box score, 31 Oct](https://sports.yahoo.com/nba/oklahoma-city-thunder-houston-rockets-2026103110/). RotoWire says he needs about 32 minutes for points-league value [RotoWire, 31 Oct](https://www.rotowire.com/basketball/article/fantasy-basketball-waiver-wire-oct-31-mara-fears-simons-144777).
- **Jordan Goodwin** played 25 minutes off the bench on 30 Oct, but no injury ties to his role [Arizona Sports, 30 Oct](https://arizonasports.com/nba/phoenix-suns/suns-building-block-nuggets-loss).
- **Jaxson Hayes** starts until Nurkic, who is re-evaluated about 4 Nov, comes back [Deseret News, 31 Oct](https://www.deseret.com/sports/2026/10/31/three-takeaways-from-the-jazzs-halloween-horror-show-against-the-blazers/).
- **Daniss Jenkins:** no new reporting. Isaiah Joe's return is the bigger threat to his minutes.

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

### Notes

- **Yves Missi:** out again 31 Oct; no timetable reported [Yahoo Sports, 31 Oct](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-vs-130042729.html).
- **Rudy Gobert:** new lower-back spasms. He was a late scratch on 31 Oct and could miss Monday; no timetable reported [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday).
- **Jusuf Nurkic:** re-evaluated about 4 Nov and takes the starting center job back from Hayes [Deseret News, 31 Oct](https://www.deseret.com/sports/2026/10/31/three-takeaways-from-the-jazzs-halloween-horror-show-against-the-blazers/).
- **Nic Claxton** has started conditioning and should take the starting job back once healthy [Gameday Chitown via Yahoo, 31 Oct](https://sports.yahoo.com/articles/bulls-face-celtics-again-nba-184144436.html).
- **Coby White:** still no timeline; out 31 Oct [Heavy, 31 Oct](https://heavy.com/sports/nba/charlotte-hornets/kon-knueppel-injury-sixers).
- **Alex Caruso** is "likely to be out for several games"; no timetable reported [Yahoo Sports, 31 Oct](https://sports.yahoo.com/nba/article/thunders-chet-holmgren-will-miss-8-10-weeks-after-undergoing-treatment-on-patellar-tendon-tear-010736245.html).
- **Reed Sheppard:** back soreness, out 30 and 31 Oct; no timetable reported. He started when VanVleet rested on 24 Oct [NBC Sports](https://www.nbcsports.com/nba/reed-sheppard/207423/news).
- **Tobias Harris:** out 31 Oct; "getting closer" but the Spurs are "conservative"; no timetable reported [Air Alamo, 31 Oct](https://airalamo.com/spurs-timberwolves-injury-report-stephon-castle-s-migraine-rudy-gobert-s-status-more).
- **Keegan Murray:** re-evaluated about 5–9 Nov [SactownSports, 26 Oct](https://sactownsports.com/nba/sacramento-kings/kings-raynaud-cardwell-murray).
- **Santi Aldama** is "very close"; his next chance is Monday against Sacramento [Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/santi-aldama-close-mavericks-debut-stay-ready-game/).

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Fred VanVleet** (HOU): Out, Right Knee; ESPN est. back 02 Nov.
- **Dejounte Murray** (NO): Out, Personal; ESPN est. back 02 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Fred VanVleet is not hurt.** He sat Saturday for rest on the second night of a back-to-back; Field Level Media lists "rest" [Field Level Media, 31 Oct](https://fieldlevelmedia.com/nba/jabari-smith-jr-rockets-overwhelm-undermanned-thunder/). ESPN files it as right knee because Udoka sits him one game of every back-to-back on his return from the ACL tear [CBS Sports, 20 Oct](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/). He plays Monday.
- **Dejounte Murray** missed a second game for the birth of his son; no timetable reported [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/dejounte-murray-personal-out-saturday-vs-atl).
- **Kawhi Leonard:** the Raptors' one-week re-evaluation, about 3 Nov, is pending. Haynes reports "a three-to-four-week timetable" [Basketnews, 29 Oct](https://basketnews.com/news-258440-kawhi-leonard-injury-timeline-gets-worse-worrying-update-emerges.html).
- **Jalen Duren:** no update; a possible return around 9 Nov [Yahoo Sports, 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html).

## Who takes the minutes, team by team

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Brandon Ingram | Right Achilles Surgery | 08 Nov | 35.3 | 36.5 | Melbourne poopoo |
| Max Strus | Right Foot Plantar Fasciitis | 08 Nov | 25.9 | 22.4 | Free agent |
| Bradley Beal | Right Knee Inflammation | 08 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Ingram (partially torn right Achilles, light on-court work only), Strus (partial plantar fascia tear) and Beal (right knee inflammation, not cleared for 5-on-5) stay in LA and are out at least another week as of 28 Oct, no date set; Jordan Miller (rotator cuff surgery 26 Aug) is re-evaluated about late Feb [Basketnews, 29 Oct](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html) [iHeart, 30 Oct](https://sportssd.iheart.com/content/2026-10-30-clippers-vs-timberwolves-injury-report-oct-30/) [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html).

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

**Reported timeline:** Jalen Williams (fibula fracture, surgery 28 Oct): re-evaluated "before the end of the regular season". Wallace's labrum surgery is done, and he is re-evaluated late in the season. **Holmgren** has a small right patellar tendon tear: he had a "biological treatment" on 30 Oct and is out 8–10 weeks, about 25 Dec to 8 Jan [Yahoo Sports, 31 Oct](https://sports.yahoo.com/nba/article/thunders-chet-holmgren-will-miss-8-10-weeks-after-undergoing-treatment-on-patellar-tendon-tear-010736245.html). *Also out:* Topic (back surgery), week-to-week, no timetable reported [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/).

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

**Reported timeline:** Butler (torn ACL, Jan 2026): no official timeline, the team hopes for early 2027 [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/). Porzingis: out indefinitely with a private health issue and not with the team; there is "an extreme level of pessimism" that he plays for Golden State again [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html). Moody (patellar tendon): a December–January return reported on 16 Oct [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/).

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

**Reported timeline:** Haliburton (mild left hamstring strain): week-to-week, next update about 11 Nov [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/). Sheppard (meniscus repair): out "months" [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months). Furphy (ACL): "middle of the year" [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html). *Also out:* Zubac is ruled out Sunday against Brooklyn, his fourth straight miss, and McConnell is still out; neither has a timetable reported [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain) [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/).

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

**Reported timeline:** Banchero (low-grade right high ankle sprain): four to six weeks from 23 Oct, about 20 Nov to 4 Dec [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html). Suggs (mild right knee bone bruise): re-evaluated about 9 Nov [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html).

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

**Reported timeline:** Edwards had a right knee arthroscopic debridement on 29 Oct and is "expected to miss up to two months"; Krawczynski has early-to-mid January in play [KSTP, 29 Oct](https://kstp.com/minnesota-sports/timberwolves-star-anthony-edwards-officially-undergoes-successful-surgery/) [Yahoo Sports, 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html). DiVincenzo (Achilles): targeting late in the season [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214).

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

**Reported timeline:** Morant has a Grade 2 left hamstring strain. He is re-evaluated in four weeks (about 27 Nov) and could be back "not long after Thanksgiving"; Jrue Holiday starts in his place [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain). Sharpe (meniscus surgery): re-evaluated about 27 Feb [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next).

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

**Reported timeline:** Raynaud (patellar subluxation): checked again about 9 Nov. Cardwell (calf): re-examined about 2 Nov [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html). Simmons (Achilles surgery 20 Oct): expected to miss the season [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season).

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

**Reported timeline:** Watkins: out after ACL surgery announced 30 Jul [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary). Champagnie and Tre Johnson: no timetable reported.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 2 | 35.0 | +5.0 | 2 | **30.5** | 29.8 | 34.5 (4) | 29.7 (6) | 29.7 (6) | Snow Time Lakers | 49% |
| Alex Sarr | PF/C | 2 | 27.5 | +3.0 | 2 | **25.0** | 27.5 | 27.8 (4) | 26.7 (6) | 26.7 (6) | Team Nic Kerr | 77% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 5 games: 3 game(s) without them, 2 with them.

**Reported timeline:** Kawhi Leonard (left knee swelling, MRI clean): the Raptors re-evaluate him about 3 Nov. Chris Haynes reports he is "expected to be sidelined for at least 3-4 weeks", which means mid-to-late November [Yahoo Sports, 27 Oct](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html) [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535).

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

**Reported timeline:** Jackson Jr. (torn right MCL, no surgery): at least six weeks, six to eight reported [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/). *Also out:* Markkanen (right wrist sprain) is a game-time decision for Saturday against Portland [Basketnews, 29 Oct](https://basketnews.com/news-258391-will-lauri-markkanen-play-jazz-announce-final-status-vs-spurs.html); Nurkic (plantar plate) is re-evaluated about 4 Nov and back at practice "in some capacity" [SI, 25 Oct](https://www.si.com/nba/jazz/onsi/jazz-vs-lakers-injury-report-latest-updates-on-jusuf-nurkic-others).

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

**Reported timeline:** Duren (strained right hamstring, 23 Oct): out at least two weeks, re-evaluated about 6–8 Nov; no progress update since [CBS Detroit / AP, 25 Oct](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/).

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

**Reported timeline:** Missi (left knee bone bruise from a hyperextension on 23 Oct): out again 31 Oct, no timetable reported; Karlo Matkovic starts at center [Yahoo Sports, 31 Oct](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-vs-130042729.html).

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

**Reported timeline:** Mark Williams (labrum surgery 10 Sep): a five-month minimum, around the All-Star break [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 4 | 21.0 | — | 0 | **27.2** | — | 32.0 (3) | 27.2 (4) | 27.2 (4) | Free agent | 1% |

### BOS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Devin Carter | Illness | 08 Nov | 18.4 | 18.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Devin Carter (mononucleosis): rejoined the team 28 Oct but still unavailable; no timetable reported [Hoops Rumors, 28 Oct](https://www.hoopsrumors.com/2026/10/celtics-note-carter-pritchard-tatum-brown.html).

No teammate has gained 3+ minutes in those games.

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Strawther (left knee sprain): re-evaluated about 29 Nov [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain). *Also out:* Spencer Jones (hamstrings) is ruled out again for Friday against Phoenix, with no firm timetable [Yahoo Sports / HoopsHype, 29 Oct](https://sports.yahoo.com/articles/cam-johnson-questionable-nuggets-tomorrow-001458305.html).

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

**Reported timeline:** Gueye (foot surgery 14 Jul): reassessment was due mid-Oct to mid-Nov; no result reported, and he was still out 29 Oct [Last Word on Sports, 29 Oct](https://lastwordonsports.com/basketball/2026/10/29/cavs-vs-hawks).

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
- News, opened and checked 1 Nov 2026:
  - [Yahoo Sports, 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html)
  - [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/christian-braun-with-31-points-hits-7-3-pointers)
  - [Yahoo Sports game log](https://sports.yahoo.com/nba/players/10278/)
  - [Yahoo Sports game log](https://sports.yahoo.com/nba/players/5747/)
  - [Yahoo Sports box score, 31 Oct](https://sports.yahoo.com/nba/oklahoma-city-thunder-houston-rockets-2026103110/)
  - [RotoWire, 31 Oct](https://www.rotowire.com/basketball/article/fantasy-basketball-waiver-wire-oct-31-mara-fears-simons-144777)
  - [Arizona Sports, 30 Oct](https://arizonasports.com/nba/phoenix-suns/suns-building-block-nuggets-loss)
  - [Deseret News, 31 Oct](https://www.deseret.com/sports/2026/10/31/three-takeaways-from-the-jazzs-halloween-horror-show-against-the-blazers/)
  - [Yahoo Sports, 31 Oct](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-vs-130042729.html)
  - [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday)
  - [Gameday Chitown via Yahoo, 31 Oct](https://sports.yahoo.com/articles/bulls-face-celtics-again-nba-184144436.html)
  - [Heavy, 31 Oct](https://heavy.com/sports/nba/charlotte-hornets/kon-knueppel-injury-sixers)
  - [Yahoo Sports, 31 Oct](https://sports.yahoo.com/nba/article/thunders-chet-holmgren-will-miss-8-10-weeks-after-undergoing-treatment-on-patellar-tendon-tear-010736245.html)
  - [NBC Sports](https://www.nbcsports.com/nba/reed-sheppard/207423/news)
  - [Air Alamo, 31 Oct](https://airalamo.com/spurs-timberwolves-injury-report-stephon-castle-s-migraine-rudy-gobert-s-status-more)
  - [SactownSports, 26 Oct](https://sactownsports.com/nba/sacramento-kings/kings-raynaud-cardwell-murray)
  - [Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/santi-aldama-close-mavericks-debut-stay-ready-game/)
  - [Field Level Media, 31 Oct](https://fieldlevelmedia.com/nba/jabari-smith-jr-rockets-overwhelm-undermanned-thunder/)
  - [CBS Sports, 20 Oct](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/)
  - [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/dejounte-murray-personal-out-saturday-vs-atl)
  - [Basketnews, 29 Oct](https://basketnews.com/news-258440-kawhi-leonard-injury-timeline-gets-worse-worrying-update-emerges.html)
  - [Basketnews, 29 Oct](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html)
  - [iHeart, 30 Oct](https://sportssd.iheart.com/content/2026-10-30-clippers-vs-timberwolves-injury-report-oct-30/)
  - [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
  - [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/)
  - [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/)
  - [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html)
  - [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)
  - [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months)
  - [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html)
  - [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain)
  - [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/)
  - [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html)
  - [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html)
  - [KSTP, 29 Oct](https://kstp.com/minnesota-sports/timberwolves-star-anthony-edwards-officially-undergoes-successful-surgery/)
  - [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
  - [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain)
  - [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)
  - [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
  - [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary)
  - [Yahoo Sports, 27 Oct](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html)
  - [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535)
  - [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
  - [Basketnews, 29 Oct](https://basketnews.com/news-258391-will-lauri-markkanen-play-jazz-announce-final-status-vs-spurs.html)
  - [SI, 25 Oct](https://www.si.com/nba/jazz/onsi/jazz-vs-lakers-injury-report-latest-updates-on-jusuf-nurkic-others)
  - [CBS Detroit / AP, 25 Oct](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/)
  - [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html)
  - [Hoops Rumors, 28 Oct](https://www.hoopsrumors.com/2026/10/celtics-note-carter-pritchard-tatum-brown.html)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain)
  - [Yahoo Sports / HoopsHype, 29 Oct](https://sports.yahoo.com/articles/cam-johnson-questionable-nuggets-tomorrow-001458305.html)
  - [Last Word on Sports, 29 Oct](https://lastwordonsports.com/basketball/2026/10/29/cavs-vs-hawks)
