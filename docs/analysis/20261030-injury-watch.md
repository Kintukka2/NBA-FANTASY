# Injury Watch: 30 Oct 2026

- Generated 2026-10-30 05:58 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 96 players in ESPN's injury feed. 29 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 17 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1099 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L15 and L30 cover every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (26 Oct–01 Nov) / next week (02 Nov–08 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

The droppable slot is CJ McCollum's (25.2 FP/g, L7 24.2 (5)). Our five-lowest floor is 35.5, which only the first two below clear in the games without the absentee.

| Player | NBA | Opening and its window | FP/g without | Season | L7 / L15 / L30 | Min without | Games this / next week |
|---|---|---|---:|---:|---|---:|---|
| **Ja'Kobe Walter** | TOR | Kawhi Leonard: re-evaluated about 3 Nov, "at least 3-4 weeks" (Haynes); *ESPN est.* 23 Nov | 40.0 | 34.0 | 35.0 (3) / 34.0 (4) / 34.0 (4) | 29.5 | 2 / 3 |
| **Precious Achiuwa** | SAC | Keegan Murray (reassessed about 5–9 Nov; *ESPN est.* 6 Nov) and Raynaud (about 9 Nov; *ESPN est.* 10 Nov) | 34.4 | 34.4 | 34.2 (4) / 34.4 (5) / 34.4 (5) | 29.8 | 1 / 4 |
| **Aaron Wiggins** | ATL | Bench role not tied to Gueye's absence, so it lasts | 30.8 | 30.8 | 31.4 (5) / 30.8 (6) / 30.8 (6) | 26.3 | 1 / 4 |
| **Isaiah Hartenstein** | OKC | Short-term: Holmgren is day-to-day for Saturday, no timetable reported; *ESPN est.* 31 Oct | 40.5 | 29.6 | 32.5 (4) / 29.6 (5) / 29.6 (5) | 26.0 | 1 / 4 |
| **Jaxson Hayes** | UTAH | Short-term: Nurkic is re-evaluated about 4 Nov; *ESPN est.* 4 Nov | 30.0 | 34.2 | 30.7 (3) / 34.2 (4) / 34.2 (4) | 37.0 | 1 / 4 |

- **Walter** is the add whose role outlasts this week. He starts while Leonard is out, and Leonard's absence runs into mid-to-late November. That cuts both ways for us: Leonard is our player.
- **Achiuwa** has four games next week and a start until Murray returns, likely in the second half of next week.
- **Back-soon stash:** **Nic Claxton** (CHI; projected 30.3, 2026 33.3; *ESPN est.* 4 Nov) is expected back at practice next week and takes the center job back. Our IR slot holds Duren, so a stash costs a bench spot.
- None of the five shows an L7 5+ FP/g off its season average, except Hartenstein's 40.5 in the games without the absentees, which rests on 2 games.

## Since the last Injury Watch

Against `docs/analysis/20261029-injury-watch.md`.

- **New long absence:** Egor Demin (BKN, right leg bone bruise, re-evaluated about 5 Nov; *ESPN est.* 7 Nov).
- **No longer long absences:** ESPN now expects Keegan Murray (6 Nov) and Dylan Cardwell (6 Nov) back within 7 days.
- **Back from injury:** Luka Doncic (Team Nic Kerr) has left ESPN's injury feed.
- **New in the feed:**
  - Ja Morant (Team Nic Kerr) left Thursday's game with a left hamstring injury; no timetable reported [ClutchPoints, 30 Oct](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-ja-morant-exits-grizzlies-game-hamstring-injury). *ESPN est.* 31 Oct.
  - Dejounte Murray (ours): personal, back Saturday at the earliest.
  - Jaylen Brown (Snow Time Lakers) and Andrew Nembhard (Matt Wright's Foxies) are day-to-day: no timetable reported, *ESPN est.* in the table below.
- **Pickups:**
  - Joined: Precious Achiuwa.
  - Left: Derrick Jones Jr., now rostered by Lauri Birds. De'Andre Hunter and Sidy Cissoko left once Keegan Murray stopped counting as a long absence.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Desmond Bane 24.0 (L7 23.0), CJ McCollum 25.2 (L7 24.2), Trey Murphy III 26.6 (L7 29.2), Jalen Duren 33.5 (L7 23.0), Fred VanVleet 35.5 (L7 32.7). A pickup at or above **35.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Isaiah Hartenstein** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 26.0 | +3.7 | **40.5** | 29.6 | 32.5 (4) | 29.6 (5) | 29.6 (5) | Free agent | 40% | 1 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 2 | 29.5 | +6.0 | **40.0** | 34.0 | 35.0 (3) | 34.0 (4) | 34.0 (4) | Free agent | 18% | 2 / 3 |
| **Precious Achiuwa** | SAC | Maxime Raynaud (10 Nov), Ben Simmons (01 Oct 2027); also out: Dylan Cardwell (06 Nov) | 5 | 29.8 | +5.5 | **34.4** | 34.4 | 34.2 (4) | 34.4 (5) | 34.4 (5) | Free agent | 24% | 1 / 4 |
| **Tristan da Silva** | ORL | Jalen Suggs (10 Nov), Paolo Banchero (22 Nov) | 1 | 31.0 | +3.0 | **32.0** | 27.5 | 26.7 (3) | 27.5 (4) | 27.5 (4) | Free agent | 8% | 2 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 6 | 26.3 | +6.0 | **30.8** | 30.8 | 31.4 (5) | 30.8 (6) | 30.8 (6) | Free agent | 28% | 1 / 4 |
| **Daniss Jenkins** | DET | Jalen Duren (09 Nov) | 3 | 28.7 | +10.2 | **30.3** | 26.6 | 30.5 (4) | 26.6 (5) | 26.6 (5) | Free agent | 8% | 1 / 3 |
| **Jaxson Hayes** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 37.0 | +13.3 | **30.0** | 34.2 | 30.7 (3) | 34.2 (4) | 34.2 (4) | Free agent | 16% | 1 / 4 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 4 | 35.8 | +8.2 | **28.5** | 28.5 | 28.5 (4) | 28.5 (4) | 28.5 (4) | Free agent | 18% | 1 / 3 |
| **Duncan Robinson** | DET | Jalen Duren (09 Nov) | 3 | 32.3 | +4.3 | **27.7** | 28.4 | 28.5 (4) | 28.4 (5) | 28.4 (5) | Free agent | 29% | 1 / 3 |
| **Brice Sensabaugh** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 18.0 | +4.0 | **26.0** | 16.0 | 20.0 (4) | 16.0 (5) | 16.0 (5) | Free agent | 1% | 1 / 4 |
| **Josh Okogie** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 28.0 | +15.0 | **26.0** | 9.0 | 12.0 (3) | 9.0 (4) | 9.0 (4) | Free agent | 0% | 1 / 4 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 20.0 | +5.2 | **25.0** | 21.2 | 24.5 (4) | 21.2 (5) | 21.2 (5) | Free agent | 1% | 2 / 4 |
| **Isaiah Jackson** | LAC | Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov), Jordan Miller (02 Mar) | 4 | 21.5 | +3.1 | **24.5** | 25.0 | 25.3 (3) | 25.0 (4) | 25.0 (4) | Free agent | 4% | 2 / 3 |
| **Aaron Nesmith** (day to day, ESPN est. back 30 Oct) | IND | Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov), Johnny Furphy (02 Jan); also out: Ivica Zubac (01 Nov), T.J. McConnell (02 Nov) | 1 | 27.0 | +7.0 | **24.0** | 18.2 | 18.2 (4) | 18.2 (4) | 18.2 (4) | Free agent | 3% | 2 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 3 | 19.7 | — | **24.0** | 24.0 | 29.5 (2) | 24.0 (3) | 24.0 (3) | Free agent | 1% | 1 / 4 |
| **Kelly Oubre Jr.** | IND | Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov), Johnny Furphy (02 Jan); also out: Ivica Zubac (01 Nov), T.J. McConnell (02 Nov) | 1 | 30.0 | +7.2 | **23.0** | 17.8 | 18.0 (4) | 17.8 (5) | 17.8 (5) | Free agent | 5% | 2 / 3 |
| **Terrence Shannon Jr.** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 27.0 | +4.8 | **23.0** | 23.0 | 26.5 (4) | 23.0 (5) | 23.0 (5) | Free agent | 15% | 2 / 4 |
| **Aday Mara** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 20.5 | +7.5 | **23.0** | 16.2 | 16.5 (4) | 16.2 (5) | 16.2 (5) | Free agent | 10% | 1 / 4 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 4 | 23.8 | — | **22.5** | 22.5 | 22.5 (4) | 22.5 (4) | 22.5 (4) | Free agent | 5% | 1 / 3 |
| **Trey Lyles** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 22.0 | +8.0 | **22.0** | 13.2 | 16.5 (4) | 13.2 (5) | 13.2 (5) | Free agent | 0% | 2 / 4 |
| **Jared McCain** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 29.5 | +9.2 | **22.0** | 16.2 | 11.0 (4) | 16.2 (5) | 16.2 (5) | Free agent | 36% | 1 / 4 |
| **Allen Graves** | TOR | Kawhi Leonard (23 Nov) | 2 | 19.0 | +6.5 | **21.5** | 20.2 | 17.7 (3) | 20.2 (4) | 20.2 (4) | Free agent | 1% | 2 / 3 |

### Notes

- **Isaiah Hartenstein** starts and has three straight double-doubles, the last 10 and 14 in 26 minutes at Dallas on 28 Oct [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-isaiah-hartenstein-double-double-in-wednesdays-loss/). The bump could end within days: Chet Holmgren (patellar tendinitis) is day-to-day for Saturday at Houston, with no timetable reported [FanDuel Research, 29 Oct](https://www.fanduel.com/research/nba/player-news/injuries/chet-holmgren-dtd-october-31-2026-against-rockets-knee).
- **Ja'Kobe Walter** has started both games since Kawhi Leonard went out. Rajakovic said he "will definitely get more playing time" but would not commit to starting him every night [Last Word On Basketball, 28 Oct](https://lastwordonsports.com/basketball/2026/10/28/raptors-starting-spot/). RotoWire calls the start temporary until Leonard is back [CBS Sports, 25 Oct](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/). Leonard is re-evaluated about 3 Nov and reported out "at least 3-4 weeks" [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535).
- **Precious Achiuwa** made his third straight start at power forward in place of Keegan Murray. He set season highs on 29 Oct: 24 points (12-of-17), 9 rebounds and 3 steals in 41 minutes [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/precious-achiuwa-scores-season-high-24-points). Murray's reassessment, about 5–9 Nov, should end the start [SactownSports, 26 Oct](https://sactownsports.com/nba/sacramento-kings/kings-raynaud-cardwell-murray). Sacramento plays four games next week.
- **Tristan da Silva** is still the sixth man; Anthony Black took the open start. He scored 20 in 31 minutes at Toronto [Orlando Sentinel via Yahoo, 29 Oct](https://sports.yahoo.com/articles/minus-banchero-suggs-magic-fall-022900015.html).
- **Aaron Wiggins** comes off the bench and had a season-high 20 against Cleveland on 29 Oct. No source ties his role to Gueye, a big who has not played, so it should last [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/aaron-wiggins-scores-20-points-off-bench-vs-cavs).
- **Daniss Jenkins** is a reserve. His one start filled in for Ausar Thompson, and Isaiah Joe's return, not Duren's, is the bigger threat to his minutes [PistonPowered, 28 Oct](https://pistonpowered.com/daniss-jenkins-creating-pistons-position-battle-must-improve-win) [Yahoo Sports, 28 Oct](https://sports.yahoo.com/articles/detroit-pistons-injury-report-delivers-175551062.html).
- **Jaxson Hayes** is Utah's starting center (37 minutes on 28 Oct). His value is "tied to Nurkic's return": Nurkic is re-evaluated about 4 Nov [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/jaxson-hayes-shoulder-upgraded-to-available) [Deseret News, 27 Oct](https://deseret.com/sports/2026/10/27/utah-jazz-injury-update-jaren-jackson-jr-lauri-markkanen).
- **Christian Braun** and **Duncan Robinson** are settled starters whose roles do not depend on Strawther or Duren. Duren's minutes went to Paul Reed [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-goes-for-15-points-wednesday/) [SI Pistons, c. 29 Oct](https://www.si.com/nba/pistons/onsi/stock-up-stock-down-report-from-pistons-first-five-games-01m646yggprc).
- **Brice Sensabaugh** is the backup shooting guard (16 points in 18 minutes). Hardy trusted him in overtime [Salt Lake Tribune, 29 Oct](https://www.sltrib.com/sports/jazz/2026/10/29/why-darryn-peterson-sat-out/).

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 02 Nov | 3 | 41.5 | 15.0 (1) | 41.5 (2) | 41.5 (2) | 24.7 | 22.5 | Free agent | 16% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 5 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 1 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 11 | 26.3 | 29.5 (2) | 26.3 (3) | 26.3 (3) | 29.1 | 34.7 | Free agent | 19% | 2 / 3 |
| **Jalen Smith** | CHI | Left Finger | 30 Oct | 0 | 34.0 | 34.5 (4) | 34.0 (5) | 34.0 (5) | 22.4 | 25.5 | Free agent | 19% | 1 / 3 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 5 | — | — | — | — | 30.3 | 33.3 | Free agent | 43% | 1 / 3 |
| **Coby White** | CHA | Left Calf Strain | 02 Nov | 3 | — | — | — | — | 32.9 | 26.5 | Free agent | 65% | 2 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 30 Oct | 0 | — | — | — | — | 25.0 | 32.4 | Free agent | 6% | 1 / 4 |
| **Keegan Murray** | SAC | Ankle | 06 Nov | 7 | 12.0 | 18.0 (1) | 12.0 (2) | 12.0 (2) | 29.3 | 31.6 | Waivers | 37% | 1 / 4 |
| **Naji Marshall** | DAL | Illness | 30 Oct | 0 | 31.3 | 30.5 (2) | 31.3 (3) | 31.3 (3) | 22.4 | 29.1 | Free agent | 12% | 1 / 4 |
| **Robert Williams III** | POR | Left Knee | 31 Oct | 1 | 31.0 | 36.5 (2) | 31.0 (3) | 31.0 (3) | 26.9 | 26.6 | Free agent | 9% | 1 / 4 |
| **Alex Caruso** | OKC | Right Ankle | 04 Nov | 5 | 30.8 | 33.0 (3) | 30.8 (4) | 30.8 (4) | 24.0 | 18.0 | Free agent | 19% | 1 / 4 |
| **Reed Sheppard** | HOU | Back | 31 Oct | 1 | 26.8 | 31.7 (3) | 26.8 (4) | 26.8 (4) | 29.9 | 30.1 | Free agent | 62% | 2 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 31 Oct | 1 | — | — | — | — | 30.1 | 28.0 | Free agent | 48% | 1 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 07 Nov | 8 | 15.0 | 18.0 (3) | 15.0 (4) | 15.0 (4) | 30.0 | 22.2 | Free agent | 36% | 2 / 4 |
| **Ziaire Williams** | LAL | Foot | 30 Oct | 0 | 28.2 | 30.0 (3) | 28.2 (4) | 28.2 (4) | 19.7 | 20.1 | Free agent | 5% | 2 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 11 | — | — | — | — | — | 28.1 | Free agent | 1% | 1 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 02 Nov | 3 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 1 / 4 |
| **Dylan Cardwell** | SAC | Left Calf Strain | 06 Nov | 7 | — | — | — | — | — | 26.6 | Free agent | 0% | 1 / 4 |
| **Cameron Johnson** | DEN | Right Ankle Sprain | 30 Oct | 0 | 11.0 | 11.0 (1) | 11.0 (1) | 11.0 (1) | 26.1 | 25.9 | Free agent | 8% | 1 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 9 | — | — | — | — | 25.6 | 10.5 | Free agent | 2% | 2 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 02 Nov | 3 | — | — | — | — | 24.4 | 25.5 | Free agent | 9% | 2 / 3 |
| **Oso Ighodaro** | PHX | Oblique Strain | 30 Oct | 0 | 18.0 | 18.0 (1) | 18.0 (1) | 18.0 (1) | 25.3 | 22.4 | Free agent | 15% | 1 / 4 |

### Notes

- **Yves Missi:** no timetable reported; still out 29 Oct [CBS Sports, 24 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/).
- **Jusuf Nurkic:** re-evaluated about 4 Nov, and back at practice "in some capacity" [SI, 25 Oct](https://www.si.com/nba/jazz/onsi/jazz-vs-lakers-injury-report-latest-updates-on-jusuf-nurkic-others).
- **Jalen Suggs:** re-evaluated about 9 Nov [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html).
- **Jalen Smith:** a new left finger sprain; questionable Friday at Boston. He has started all five games at center [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/jalen-smith-finger-questionable-friday-vs-bos).
- **Nic Claxton:** expected to rejoin practice next week and likely to travel on the trip that starts Friday. He takes the center job back once ready [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/nic-claxton-hamstring-remains-out).
- **Coby White:** "remains without a timeline" per Charles Lee on 26 Oct; nothing newer [RotoWire, 26 Oct](https://www.rotowire.com/basketball/headlines/coby-white-injury-wont-return-during-road-trip-536205).
- **Santi Aldama:** doubtful Friday; his next chance is Monday, so ESPN's 30 Oct is early [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/santi-aldama-knee-doubtful-vs-houston).
- **Keegan Murray:** left ankle capsulitis, reassessed about 5–9 Nov. He is on waivers in our league, not waived by the Kings [SactownSports, 26 Oct](https://sactownsports.com/nba/sacramento-kings/kings-raynaud-cardwell-murray).
- **Naji Marshall:** questionable Friday with an illness [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/mavericks-naji-marshall-questionable-with-illness/).
- **Robert Williams III:** rested his left knee on 29 Oct; his next chance is Saturday [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/robert-williams-knee-officially-out-vs-memphis).
- **Alex Caruso:** day-to-day for Saturday at Houston; no timetable reported [FanDuel Research, 29 Oct](https://www.fanduel.com/research/nba/player-news/injuries/alex-caruso-dtd-october-31-2026-against-rockets-ankle).
- **Reed Sheppard:** back soreness, out Friday; his next chance is Saturday [RotoWire, 29 Oct](https://www.rotowire.com/basketball/headlines/reed-sheppard-injury-ruled-out-for-friday-536734).
- **Tobias Harris:** "getting closer", but the Spurs will be "conservative"; no timetable reported [San Antonio Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html).
- **Egor Demin:** a right leg bone bruise, re-evaluated about 5 Nov; his earliest game is 7 Nov [Hoops Rumors, 29 Oct](https://www.hoopsrumors.com/2026/10/nets-demin-bone-bruise-out-at-least-one-week.html).
- **Ziaire Williams:** questionable Friday; Redick called his absence "overly cautious" [Heavy, 29 Oct](https://heavy.com/sports/nba/los-angeles-lakers/injury-report-vs-warriors-october-30/).
- **Maxime Raynaud:** checked again about 9 Nov. **Dylan Cardwell:** re-examined about 2 Nov [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html).
- **Dereck Lively II:** ruled out again Friday, with no timetable reported; ESPN's 2 Nov looks optimistic [Dallas Sports Journal, 29 Oct](https://dallassportsjournal.com/mavericks-injury-report-rockets-caleb-martin-naji-marshall-aldama/).
- **Cameron Johnson:** upgraded to questionable for Friday at Phoenix [SI Nuggets, 29 Oct](https://www.si.com/nba/nuggets/onsi/nuggets-update-cameron-johnson-injury-status-before-suns-game).
- **Bradley Beal:** out at least another week as of 28 Oct, and not cleared for 5-on-5 [Basketnews, 29 Oct](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html).
- **T.J. McConnell:** "doing better" but out Friday at Miami [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-mcconnell-hamstring-doing-better).
- **Oso Ighodaro:** questionable Friday and "trending in a good direction"; a start is a "big possibility" [Suns On SI via Yahoo, 29 Oct](https://sports.yahoo.com/articles/suns-center-trending-play-vs-203029020.html).

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Dejounte Murray** (NO): Day-To-Day, Personal; ESPN est. back 31 Oct.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Jalen Duren:** out at least two weeks from 25 Oct and re-evaluated about 6–8 Nov; no progress update since [CBS Detroit / AP, 25 Oct](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/).
- **Dejounte Murray:** not an injury. He missed Thursday for the birth of his son and is a game-time decision for Saturday against Atlanta; no timetable reported [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-late-scratch-thursday/) [RotoBaller, 29 Oct](https://www.rotoballer.com/player-news/dejounte-murray-out-thursday-for-birth-of-son/1978907).
- **Kawhi Leonard:** re-evaluated about 3 Nov per the Raptors, and "at least 3-4 weeks" per Chris Haynes [Yahoo Sports, 27 Oct](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html) [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535).

## Who takes the minutes, team by team

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Brandon Ingram | Right Achilles Surgery | 08 Nov | 35.3 | 36.5 | Melbourne poopoo |
| Max Strus | Right Foot Plantar Fasciitis | 08 Nov | 25.9 | 22.4 | Free agent |
| Bradley Beal | Right Knee Inflammation | 08 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Ingram (partially torn right Achilles, light on-court work only), Strus (partial plantar fascia tear) and Beal (right knee inflammation, not cleared for 5-on-5) stay in LA and are out at least another week as of 28 Oct, no date set; Jordan Miller (rotator cuff surgery 26 Aug) is re-evaluated about late Feb [Basketnews, 29 Oct](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html) [iHeart, 30 Oct](https://sportssd.iheart.com/content/2026-10-30-clippers-vs-timberwolves-injury-report-oct-30/) [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 4 | 30.2 | +8.2 | 4 | **36.2** | 20.0 | 33.0 (3) | 35.8 (4) | 35.8 (4) | Dr White Slong | 40% |
| Derrick Jones Jr. | SF/PF | 4 | 29.8 | +4.3 | 4 | **33.5** | 21.1 | 34.7 (3) | 33.5 (4) | 33.5 (4) | Lauri Birds | 8% |
| Isaiah Jackson | PF/C | 4 | 21.5 | +3.1 | 4 | **24.5** | 20.6 | 25.3 (3) | 25.0 (4) | 25.0 (4) | Free agent | 4% |
| Kobe Sanders | SG | 4 | 21.2 | — | 1 | **19.2** | — | 20.7 (3) | 19.2 (4) | 19.2 (4) | Free agent | 0% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Butler (torn ACL, Jan 2026): no official timeline, the team hopes for early 2027 [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/). Porzingis: out indefinitely with a private health issue and not with the team; there is "an extreme level of pessimism" that he plays for Golden State again [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html). Moody (patellar tendon): a December–January return reported on 16 Oct [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 5 | 33.6 | +9.0 | 5 | **43.8** | 23.5 | 49.0 (4) | 43.8 (5) | 43.8 (5) | **us** | 87% |
| Graham Ike | PF | 4 | 13.2 | — | 2 | **20.8** | — | 20.3 (3) | 20.8 (4) | 20.8 (4) | Free agent | 0% |
| Brandon Williams | PG/SG | 5 | 16.0 | — | 1 | **19.2** | — | 16.8 (4) | 19.2 (5) | 19.2 (5) | Free agent | 1% |
| Georges Niang | PF | 5 | 19.4 | — | 1 | **12.4** | — | 11.8 (4) | 12.4 (5) | 12.4 (5) | Free agent | 0% |
| Will Richard | SG/SF | 5 | 16.0 | — | 1 | **12.2** | — | 9.0 (4) | 12.2 (5) | 12.2 (5) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 5 games: 1 game(s) without them, 4 with them.

**Reported timeline:** Haliburton (mild left hamstring strain): week-to-week, next update about 11 Nov [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/). Sheppard (meniscus repair): out "months" [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months). Furphy (ACL): "middle of the year" [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html). *Also out:* Zubac and McConnell are both out Friday at Miami; neither has a timetable reported [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain) [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/).

Also out in those games, so part of the gain is theirs: Ivica Zubac (left ankle sprain; ESPN est. 01 Nov), T.J. McConnell (right hamstring strain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard (day to day, ESPN est. back 30 Oct) | PG/SG | 1 | 35.0 | +3.0 | 1 | **39.0** | 31.3 | 31.3 (3) | 33.2 (4) | 33.2 (4) | Matt Wright's Foxies | 62% |
| Aaron Nesmith (day to day, ESPN est. back 30 Oct) | SG/SF | 1 | 27.0 | +7.0 | 1 | **24.0** | 16.3 | 18.2 (4) | 18.2 (4) | 18.2 (4) | Free agent | 3% |
| Kelly Oubre Jr. | SG/SF | 1 | 30.0 | +7.2 | 1 | **23.0** | 16.5 | 18.0 (4) | 17.8 (5) | 17.8 (5) | Free agent | 5% |
| Larry Nance Jr. | PF | 1 | 23.0 | +11.2 | 0 | **12.0** | 6.5 | 9.8 (4) | 7.6 (5) | 7.6 (5) | Free agent | 0% |
| Jalen Slawson | SF | 1 | 12.0 | +3.0 | 0 | **11.0** | 11.3 | 11.2 (4) | 11.2 (4) | 11.2 (4) | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |
| Jalen Suggs | Right Knee | 10 Nov | 33.3 | 26.3 | Free agent |

Last 4 games: 1 game(s) without them, 3 with them.

**Reported timeline:** Banchero (low-grade right high ankle sprain): four to six weeks from 23 Oct, about 20 Nov to 4 Dec [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html). Suggs (mild right knee bone bruise): re-evaluated about 9 Nov [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Tristan da Silva | SF/PF | 1 | 31.0 | +3.0 | 0 | **32.0** | 26.0 | 26.7 (3) | 27.5 (4) | 27.5 (4) | Free agent | 8% |
| Nikola Vucevic | C | 1 | 16.0 | +8.0 | 0 | **14.0** | 8.0 | 11.7 (3) | 9.5 (4) | 9.5 (4) | Free agent | 42% |
| Jevon Carter | PG | 1 | 22.0 | +9.0 | 0 | **10.0** | 9.0 | 9.5 (2) | 9.5 (2) | 9.5 (2) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 5 games: 1 game(s) without them, 4 with them.

**Reported timeline:** Edwards had a right knee arthroscopic debridement on Thu 29 Oct at Mayo Clinic. The team expects a full recovery but has given no official timetable. KSTP was told "around two months"; The Athletic's Jon Krawczynski says it could be more, possibly early-to-mid January [KSTP, 29 Oct](https://kstp.com/minnesota-sports/timberwolves-star-anthony-edwards-officially-undergoes-successful-surgery/) [Yahoo Sports, 29 Oct](https://sports.yahoo.com/articles/anthony-edwards-undergoes-arthroscopic-knee-185106176.html). DiVincenzo (Achilles): targeting late in the season [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 1 | 32.0 | +5.8 | 1 | **47.0** | 25.8 | 30.5 (4) | 30.0 (5) | 30.0 (5) | Cream Abdul-Yammar | 66% |
| Jaden McDaniels | SF/PF | 1 | 35.0 | +3.2 | 1 | **30.0** | 36.8 | 33.5 (4) | 35.4 (5) | 35.4 (5) | Melbourne poopoo | 87% |
| Joan Beringer | C | 1 | 20.0 | +5.2 | 0 | **25.0** | 20.2 | 24.5 (4) | 21.2 (5) | 21.2 (5) | Free agent | 1% |
| Terrence Shannon Jr. | SG | 1 | 27.0 | +4.8 | 0 | **23.0** | 23.0 | 26.5 (4) | 23.0 (5) | 23.0 (5) | Free agent | 15% |
| Trey Lyles | PF | 1 | 22.0 | +8.0 | 0 | **22.0** | 11.0 | 16.5 (4) | 13.2 (5) | 13.2 (5) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Cason Wallace | Left Shoulder | 02 Mar | 26.6 | 18.7 | Free agent |

Last 5 games: 2 game(s) without them, 3 with them.

**Reported timeline:** Jalen Williams (fibula fracture, surgery 28 Oct): re-evaluated "before the end of the regular season" [Yahoo Sports, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html). Wallace (labrum, surgery pending): five to six months reported [ClutchPoints, 26 Oct](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-cason-wallace-miss-significant-time-shoulder-injury). *Also out:* Holmgren (patellar tendinitis) is day-to-day and a game-time decision for Saturday at Houston, with no timetable reported [FanDuel Research, 29 Oct](https://www.fanduel.com/research/nba/player-news/injuries/chet-holmgren-dtd-october-31-2026-against-rockets-knee); Topic (back surgery) is week-to-week, with no timetable reported [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/).

Also out in those games, so part of the gain is theirs: Chet Holmgren (right knee; ESPN est. 31 Oct), Nikola Topic (back; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Isaiah Hartenstein | C | 2 | 26.0 | +3.7 | 2 | **40.5** | 22.3 | 32.5 (4) | 29.6 (5) | 29.6 (5) | Free agent | 40% |
| Aday Mara | C | 2 | 20.5 | +7.5 | 0 | **23.0** | 11.7 | 16.5 (4) | 16.2 (5) | 16.2 (5) | Free agent | 10% |
| Jared McCain | PG/SG | 2 | 29.5 | +9.2 | 2 | **22.0** | 12.3 | 11.0 (4) | 16.2 (5) | 16.2 (5) | Free agent | 36% |
| Kenrich Williams | SF | 2 | 20.5 | +13.8 | 2 | **13.0** | 7.0 | 9.8 (4) | 9.4 (5) | 9.4 (5) | Free agent | 0% |
| Jaylin Williams | PF/C | 2 | 23.0 | +10.7 | 0 | **13.0** | 7.0 | 10.0 (4) | 9.4 (5) | 9.4 (5) | Free agent | 2% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Maxime Raynaud | Right Knee Dislocated | 10 Nov | 26.6 | 28.1 | Free agent |
| Ben Simmons | Right Achilles Surgery | 01 Oct 2027 | 21.2 | — | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Raynaud (patellar subluxation): checked again about 9 Nov. Cardwell (calf): re-examined about 2 Nov [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html). Simmons (Achilles surgery 20 Oct): expected to miss the season [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season).

Also out in those games, so part of the gain is theirs: Dylan Cardwell (left calf strain; ESPN est. 06 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Zach LaVine | SG/SF | 5 | 36.6 | +3.8 | 5 | **39.2** | 32.0 | 40.0 (4) | 38.8 (5) | 38.8 (5) | Cream Abdul-Yammar | 82% |
| Precious Achiuwa | PF/C | 5 | 29.8 | +5.5 | 3 | **34.4** | 24.1 | 34.2 (4) | 34.4 (5) | 34.4 (5) | Free agent | 24% |
| Darius Acuff Jr. | PG | 5 | 36.4 | +5.8 | 5 | **34.2** | 30.4 | 40.5 (4) | 34.2 (5) | 34.2 (5) | Team Nic Kerr | 74% |
| Daeqwon Plowden | SG | 4 | 16.5 | — | 0 | **9.0** | — | 7.7 (3) | 9.0 (4) | 9.0 (4) | Free agent | 0% |
| Emanuel Sharp | SG | 5 | 16.6 | — | 0 | **6.8** | — | 5.8 (4) | 7.2 (5) | 7.2 (5) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 5 games: 1 game(s) without them, 4 with them.

**Reported timeline:** Watkins: out after ACL surgery announced 30 Jul [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary). Champagnie and Tre Johnson: no timetable reported.

Also out in those games, so part of the gain is theirs: Tre Johnson (right achilles soreness; ESPN est. 30 Oct).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 1 | 38.0 | +8.0 | 1 | **34.0** | 29.8 | 29.8 (4) | 30.2 (5) | 30.2 (5) | Snow Time Lakers | 48% |
| Khris Middleton | SF/PF | 1 | 23.0 | +9.3 | 0 | **5.0** | 4.7 | 5.3 (3) | 4.8 (4) | 4.8 (4) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 4 games: 2 game(s) without them, 2 with them.

**Reported timeline:** Kawhi Leonard (left knee swelling, MRI clean): the Raptors re-evaluate him about 3 Nov. Chris Haynes reports he is "expected to be sidelined for at least 3-4 weeks", which means mid-to-late November [Yahoo Sports, 27 Oct](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html) [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ja'Kobe Walter | SG | 2 | 29.5 | +6.0 | 2 | **40.0** | 28.0 | 35.0 (3) | 34.0 (4) | 34.0 (4) | Free agent | 18% |
| Allen Graves | SF | 2 | 19.0 | +6.5 | 0 | **21.5** | 19.0 | 17.7 (3) | 20.2 (4) | 20.2 (4) | Free agent | 1% |
| Trayce Jackson-Davis | PF | 2 | 13.0 | +7.5 | 0 | **20.5** | 7.0 | 13.7 (3) | 13.8 (4) | 13.8 (4) | Free agent | 0% |
| Jamison Battle | SF | 2 | 16.5 | +5.0 | 0 | **10.5** | 17.0 | 10.7 (3) | 13.8 (4) | 13.8 (4) | Free agent | 0% |

### BKN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Egor Demin | Right Leg Bruise | 07 Nov | 32.3 | 15.0 | Free agent |

Last 4 games: 0 game(s) without them, 4 with them.

No game yet without them. Same-position teammates by current minutes: Keon Ellis (SG/SF, 26.0 min, 24.0 FP/g, Free agent), Mikel Brown Jr. (PG, 22.7 min, 19.3 FP/g, Free agent), Nolan Traore (PG, 17.5 min, 17.5 FP/g, Free agent), Drake Powell (SG, 12.0 min, 6.0 FP/g, Free agent).

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 5 games: 1 game(s) without them, 4 with them.

**Reported timeline:** Jackson Jr. (torn right MCL, no surgery): at least six weeks, six to eight reported [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/). *Also out:* Markkanen (right wrist sprain) is a game-time decision for Saturday against Portland [Basketnews, 29 Oct](https://basketnews.com/news-258391-will-lauri-markkanen-play-jazz-announce-final-status-vs-spurs.html); Nurkic (plantar plate) is re-evaluated about 4 Nov and back at practice "in some capacity" [SI, 25 Oct](https://www.si.com/nba/jazz/onsi/jazz-vs-lakers-injury-report-latest-updates-on-jusuf-nurkic-others).

Also out in those games, so part of the gain is theirs: Lauri Markkanen (right wrist; ESPN est. 31 Oct), Jusuf Nurkic (right foot strain; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Keyonte George | PG/SG | 1 | 37.0 | +5.2 | 1 | **31.0** | 40.5 | 38.5 (4) | 38.6 (5) | 38.6 (5) | Cream Abdul-Yammar | 89% |
| Jaxson Hayes | C | 1 | 37.0 | +13.3 | 1 | **30.0** | 35.7 | 30.7 (3) | 34.2 (4) | 34.2 (4) | Free agent | 16% |
| Ace Bailey | SF/PF | 1 | 40.0 | +12.8 | 1 | **26.0** | 38.8 | 36.2 (4) | 36.2 (5) | 36.2 (5) | Dr White Slong | 64% |
| Brice Sensabaugh | SG/SF | 1 | 18.0 | +4.0 | 0 | **26.0** | 13.5 | 20.0 (4) | 16.0 (5) | 16.0 (5) | Free agent | 1% |
| Josh Okogie | SF | 1 | 28.0 | +15.0 | 0 | **26.0** | 3.3 | 12.0 (3) | 9.0 (4) | 9.0 (4) | Free agent | 0% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 09 Nov | 31.0 | 33.5 | **us** |

Last 5 games: 3 game(s) without them, 2 with them.

**Reported timeline:** Duren (strained right hamstring, 23 Oct): out at least two weeks, re-evaluated about 6–8 Nov; no progress update since [CBS Detroit / AP, 25 Oct](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cade Cunningham | PG | 3 | 36.0 | +3.5 | 3 | **50.3** | 39.0 | 47.5 (4) | 45.8 (5) | 45.8 (5) | **us** | 100% |
| Paul Reed | PF/C | 3 | 29.0 | +7.5 | 3 | **40.0** | 33.5 | 41.0 (4) | 36.6 (5) | 36.6 (5) | **us** | 36% |
| Daniss Jenkins | PG | 3 | 28.7 | +10.2 | 1 | **30.3** | 21.0 | 30.5 (4) | 26.6 (5) | 26.6 (5) | Free agent | 8% |
| Duncan Robinson | SG/SF | 3 | 32.3 | +4.3 | 3 | **27.7** | 29.5 | 28.5 (4) | 28.4 (5) | 28.4 (5) | Free agent | 29% |
| Ronald Holland II | SF/PF | 3 | 15.7 | +3.2 | 0 | **14.3** | 16.0 | 17.5 (4) | 15.0 (5) | 15.0 (5) | Free agent | 1% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Sharpe (torn right meniscus, surgery late Aug): re-evaluated about 27 Feb [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 4 | 22.5 | +6.3 | 0 | **19.8** | 10.6 | 21.7 (3) | 19.8 (4) | 19.8 (4) | Free agent | 2% |
| Branden Carlson | C | 1 | 12.0 | — | 0 | **9.0** | — | 9.0 (1) | 9.0 (1) | 9.0 (1) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 3 games: 3 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Mark Williams (labrum surgery 10 Sep): a five-month minimum, around the All-Star break [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 3 | 19.7 | — | 0 | **24.0** | — | 29.5 (2) | 24.0 (3) | 24.0 (3) | Free agent | 1% |

### BOS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Devin Carter | Illness | 08 Nov | 18.4 | 18.9 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Devin Carter (mononucleosis): rejoined the team 28 Oct but still unavailable; no timetable reported [Hoops Rumors, 28 Oct](https://www.hoopsrumors.com/2026/10/celtics-note-carter-pritchard-tatum-brown.html).

No teammate has gained 3+ minutes in those games.

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Strawther (left knee sprain): re-evaluated about 29 Nov [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain). *Also out:* Spencer Jones (hamstrings) is ruled out again for Friday against Phoenix, with no firm timetable [Yahoo Sports / HoopsHype, 29 Oct](https://sports.yahoo.com/articles/cam-johnson-questionable-nuggets-tomorrow-001458305.html).

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jamal Murray | PG | 4 | 38.5 | +3.5 | 4 | **43.8** | 43.9 | 43.8 (4) | 43.8 (4) | 43.8 (4) | **us** | 99% |
| Christian Braun | SG/SF | 4 | 35.8 | +8.2 | 4 | **28.5** | 23.1 | 28.5 (4) | 28.5 (4) | 28.5 (4) | Free agent | 18% |
| Trevon Brazile | SF/PF | 4 | 23.8 | — | 1 | **22.5** | — | 22.5 (4) | 22.5 (4) | 22.5 (4) | Free agent | 5% |
| Alpha Diallo (out, ESPN est. back 30 Oct) | SF | 1 | 22.0 | — | 0 | **13.0** | — | 13.0 (1) | 13.0 (1) | 13.0 (1) | Free agent | 0% |
| Bryce Hopkins | SF | 4 | 16.5 | — | 2 | **6.5** | — | 6.5 (4) | 6.5 (4) | 6.5 (4) | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

**Reported timeline:** Gueye (foot surgery 14 Jul): reassessment was due mid-Oct to mid-Nov; no result reported, and he was still out 29 Oct [Last Word on Sports, 29 Oct](https://lastwordonsports.com/basketball/2026/10/29/cavs-vs-hawks).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 6 | 26.3 | +6.0 | 0 | **30.8** | 19.2 | 31.4 (5) | 30.8 (6) | 30.8 (6) | Free agent | 28% |
| Jock Landale | C | 6 | 17.7 | — | 0 | **19.2** | — | 17.8 (5) | 19.2 (6) | 19.2 (6) | Free agent | 1% |

## Every injury

All 96 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct 2027 | 336 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct 2027 | 336 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 244 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 154 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 154 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 123 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 123 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 123 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder | 02 Mar | 123 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 118 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 96 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 64 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 64 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 64 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 52 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 45 | Matt Wright's Foxies |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 34 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 32 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 32 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 30 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 24 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 23 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 21 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 19 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 19 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 14 | Lauri Birds |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 11 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 11 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 11 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 10 | **us** |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 9 | Free agent |
| Max Strus | LAC | Out | Right Foot Plantar Fasciitis | 08 Nov | 9 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 9 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 9 | Melbourne poopoo |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 08 Nov | 9 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 07 Nov | 8 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 06 Nov | 7 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 06 Nov | 7 | Waivers |
| Dylan Cardwell | SAC | Out | Left Calf Strain | 06 Nov | 7 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 04 Nov | 5 | Free agent |
| Tacko Fall | PHI | Out | Left Quadriceps Strain | 04 Nov | 5 | Free agent |
| Nikola Topic | OKC | Out | Back | 04 Nov | 5 | Free agent |
| Nic Claxton | CHI | Out | Hamstring | 04 Nov | 5 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 04 Nov | 5 | Free agent |
| Jose Alvarado | NY | Out | Left Ankle Sprain | 04 Nov | 5 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 04 Nov | 5 | Free agent |
| Alex Caruso | OKC | Out | Right Ankle | 04 Nov | 5 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 02 Nov | 3 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 02 Nov | 3 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 02 Nov | 3 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 02 Nov | 3 | Free agent |
| Spencer Jones | DEN | Out | Hamstring | 02 Nov | 3 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 02 Nov | 3 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 02 Nov | 3 | — |
| Kylan Boswell | CHA | Out | Right Knee Surgery | 02 Nov | 3 | — |
| Kon Knueppel | CHA | Out | Left Hamstring | 02 Nov | 3 | Team Nic Kerr |
| Grant Williams | CHA | Out | Right Hamstring | 02 Nov | 3 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 02 Nov | 3 | Free agent |
| Coby White | CHA | Out | Left Calf Strain | 02 Nov | 3 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 01 Nov | 2 | Free agent |
| Ivica Zubac | IND | Out | Left Ankle Sprain | 01 Nov | 2 | Lauri Birds |
| Cameron Carr | LAL | Out | Right Oblique Strain | 01 Nov | 2 | Free agent |
| Adou Thiero | LAL | Out | Left Knee Inflammation | 01 Nov | 2 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 31 Oct | 1 | Free agent |
| Robert Williams III | POR | Day-To-Day | Left Knee | 31 Oct | 1 | Free agent |
| Reed Sheppard | HOU | Out | Back | 31 Oct | 1 | Free agent |
| Quinten Post | MEM | Day-To-Day | Right Ankle | 31 Oct | 1 | Free agent |
| Meleek Thomas | CLE | Day-To-Day | Foot | 31 Oct | 1 | Free agent |
| Lauri Markkanen | UTAH | Day-To-Day | Right Wrist | 31 Oct | 1 | Lauri Birds |
| Jordan Poole | NO | Day-To-Day | Left Ankle | 31 Oct | 1 | Free agent |
| Jabari Walker | PHI | Out | Left Knee Soreness | 31 Oct | 1 | Free agent |
| Ja Morant | POR | Day-To-Day | Left Hamstring | 31 Oct | 1 | Team Nic Kerr |
| Dejounte Murray | NO | Day-To-Day | Personal | 31 Oct | 1 | **us** |
| Chris Youngblood | POR | Out | Left Ankle Soreness | 31 Oct | 1 | Free agent |
| Chet Holmgren | OKC | Day-To-Day | Right Knee | 31 Oct | 1 | Team Nic Kerr |
| Ziaire Williams | LAL | Day-To-Day | Foot | 30 Oct | 0 | Free agent |
| Tre Johnson | WSH | Day-To-Day | Right Achilles Soreness | 30 Oct | 0 | Free agent |
| Tobe Awaka | CHI | Day-To-Day | Ankle | 30 Oct | 0 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 30 Oct | 0 | Free agent |
| Simone Fontecchio | MIA | Day-To-Day | Illness | 30 Oct | 0 | Free agent |
| Santi Aldama | DAL | Out | Right Knee Surgery | 30 Oct | 0 | Free agent |
| Rui Hachimura | LAC | Day-To-Day | Left Quadriceps Soreness | 30 Oct | 0 | Free agent |
| Patrick Williams | CHI | Out | Right Groin Soreness | 30 Oct | 0 | Free agent |
| Oso Ighodaro | PHX | Day-To-Day | Oblique Strain | 30 Oct | 0 | Free agent |
| Naji Marshall | DAL | Day-To-Day | Illness | 30 Oct | 0 | Free agent |
| Marcus Smart | HOU | Out | Left Forearm Strain | 30 Oct | 0 | Free agent |
| Jaylen Brown | PHI | Day-To-Day | Knee | 30 Oct | 0 | Snow Time Lakers |
| Jalen Smith | CHI | Day-To-Day | Left Finger | 30 Oct | 0 | Free agent |
| Isaiah Joe | DET | Day-To-Day | Right Hip Bruise | 30 Oct | 0 | Free agent |
| Gui Santos | GS | Day-To-Day | Left Knee Tendinitis | 30 Oct | 0 | Free agent |
| Dennis Schroder | CHA | Day-To-Day | Foot | 30 Oct | 0 | Free agent |
| Cameron Johnson | DEN | Out | Right Ankle Sprain | 30 Oct | 0 | Free agent |
| Andrew Nembhard | IND | Day-To-Day | Neck Soreness | 30 Oct | 0 | Matt Wright's Foxies |
| Alpha Diallo | DEN | Out | Right Personal | 30 Oct | 0 | Free agent |
| Alperen Sengun | HOU | Day-To-Day | Back Soreness | 30 Oct | 0 | Cream Abdul-Yammar |
| Aaron Nesmith | IND | Day-To-Day | Hamstring | 30 Oct | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-10-30 05:58 UTC.
- News, opened and checked 30 Oct 2026:
  - [ClutchPoints, 30 Oct](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-ja-morant-exits-grizzlies-game-hamstring-injury)
  - [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-isaiah-hartenstein-double-double-in-wednesdays-loss/)
  - [FanDuel Research, 29 Oct](https://www.fanduel.com/research/nba/player-news/injuries/chet-holmgren-dtd-october-31-2026-against-rockets-knee)
  - [Last Word On Basketball, 28 Oct](https://lastwordonsports.com/basketball/2026/10/28/raptors-starting-spot/)
  - [CBS Sports, 25 Oct](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/)
  - [Yardbarker, 29 Oct](https://www.yardbarker.com/nba/articles/worrisome_update_in_toronto_kawhi_leonard_sidelined_3_4_weeks_as_knee_swelling_worsens/s1_17810_44489535)
  - [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/precious-achiuwa-scores-season-high-24-points)
  - [SactownSports, 26 Oct](https://sactownsports.com/nba/sacramento-kings/kings-raynaud-cardwell-murray)
  - [Orlando Sentinel via Yahoo, 29 Oct](https://sports.yahoo.com/articles/minus-banchero-suggs-magic-fall-022900015.html)
  - [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/aaron-wiggins-scores-20-points-off-bench-vs-cavs)
  - [PistonPowered, 28 Oct](https://pistonpowered.com/daniss-jenkins-creating-pistons-position-battle-must-improve-win)
  - [Yahoo Sports, 28 Oct](https://sports.yahoo.com/articles/detroit-pistons-injury-report-delivers-175551062.html)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/jaxson-hayes-shoulder-upgraded-to-available)
  - [Deseret News, 27 Oct](https://deseret.com/sports/2026/10/27/utah-jazz-injury-update-jaren-jackson-jr-lauri-markkanen)
  - [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-goes-for-15-points-wednesday/)
  - [SI Pistons, c. 29 Oct](https://www.si.com/nba/pistons/onsi/stock-up-stock-down-report-from-pistons-first-five-games-01m646yggprc)
  - [Salt Lake Tribune, 29 Oct](https://www.sltrib.com/sports/jazz/2026/10/29/why-darryn-peterson-sat-out/)
  - [CBS Sports, 24 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/)
  - [SI, 25 Oct](https://www.si.com/nba/jazz/onsi/jazz-vs-lakers-injury-report-latest-updates-on-jusuf-nurkic-others)
  - [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html)
  - [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/jalen-smith-finger-questionable-friday-vs-bos)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/nic-claxton-hamstring-remains-out)
  - [RotoWire, 26 Oct](https://www.rotowire.com/basketball/headlines/coby-white-injury-wont-return-during-road-trip-536205)
  - [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/santi-aldama-knee-doubtful-vs-houston)
  - [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/mavericks-naji-marshall-questionable-with-illness/)
  - [NBC Sports, 29 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/robert-williams-knee-officially-out-vs-memphis)
  - [FanDuel Research, 29 Oct](https://www.fanduel.com/research/nba/player-news/injuries/alex-caruso-dtd-october-31-2026-against-rockets-ankle)
  - [RotoWire, 29 Oct](https://www.rotowire.com/basketball/headlines/reed-sheppard-injury-ruled-out-for-friday-536734)
  - [San Antonio Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html)
  - [Hoops Rumors, 29 Oct](https://www.hoopsrumors.com/2026/10/nets-demin-bone-bruise-out-at-least-one-week.html)
  - [Heavy, 29 Oct](https://heavy.com/sports/nba/los-angeles-lakers/injury-report-vs-warriors-october-30/)
  - [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
  - [Dallas Sports Journal, 29 Oct](https://dallassportsjournal.com/mavericks-injury-report-rockets-caleb-martin-naji-marshall-aldama/)
  - [SI Nuggets, 29 Oct](https://www.si.com/nba/nuggets/onsi/nuggets-update-cameron-johnson-injury-status-before-suns-game)
  - [Basketnews, 29 Oct](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-mcconnell-hamstring-doing-better)
  - [Suns On SI via Yahoo, 29 Oct](https://sports.yahoo.com/articles/suns-center-trending-play-vs-203029020.html)
  - [CBS Detroit / AP, 25 Oct](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/)
  - [CBS Sports, 29 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-late-scratch-thursday/)
  - [RotoBaller, 29 Oct](https://www.rotoballer.com/player-news/dejounte-murray-out-thursday-for-birth-of-son/1978907)
  - [Yahoo Sports, 27 Oct](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html)
  - [iHeart, 30 Oct](https://sportssd.iheart.com/content/2026-10-30-clippers-vs-timberwolves-injury-report-oct-30/)
  - [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
  - [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/)
  - [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html)
  - [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)
  - [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months)
  - [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html)
  - [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain)
  - [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/)
  - [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html)
  - [KSTP, 29 Oct](https://kstp.com/minnesota-sports/timberwolves-star-anthony-edwards-officially-undergoes-successful-surgery/)
  - [Yahoo Sports, 29 Oct](https://sports.yahoo.com/articles/anthony-edwards-undergoes-arthroscopic-knee-185106176.html)
  - [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
  - [Yahoo Sports, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
  - [ClutchPoints, 26 Oct](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-cason-wallace-miss-significant-time-shoulder-injury)
  - [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
  - [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary)
  - [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
  - [Basketnews, 29 Oct](https://basketnews.com/news-258391-will-lauri-markkanen-play-jazz-announce-final-status-vs-spurs.html)
  - [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)
  - [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html)
  - [Hoops Rumors, 28 Oct](https://www.hoopsrumors.com/2026/10/celtics-note-carter-pritchard-tatum-brown.html)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain)
  - [Yahoo Sports / HoopsHype, 29 Oct](https://sports.yahoo.com/articles/cam-johnson-questionable-nuggets-tomorrow-001458305.html)
  - [Last Word on Sports, 29 Oct](https://lastwordonsports.com/basketball/2026/10/29/cavs-vs-hawks)
