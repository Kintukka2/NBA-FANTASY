# Injury Watch: 29 Oct 2026

- Generated 2026-10-29 05:38 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 86 players in ESPN's injury feed. 30 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 16 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1099 pool players re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **Games** is games left this week (26 Oct–01 Nov) / next week (02 Nov–08 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Since the last Injury Watch

Against `docs/analysis/20261027-injury-watch.md` (27 Oct). The dates are ESPN's estimates from the two reports.

- **New long absences:**
  - Anthony Edwards (MIN, 21 Dec)
  - **Kawhi Leonard (TOR, ours, 23 Nov)**
  - Jaren Jackson Jr. (UTAH, 14 Dec)
  - Tyrese Haliburton (IND, 13 Nov)
  - Justin Champagnie (WSH, 25 Feb). He was a pickup candidate on 27 Oct, as day-to-day.
  - Ben Sheppard's estimate moved from 1 Dec to 2 Jan.
- **No longer a long absence:**
  - Santi Aldama, Dereck Lively II, Nic Claxton, Jusuf Nurkic and Yves Missi are now inside the 7-day window, and most sit in *back soon*.
  - The Dallas, Chicago and New Orleans sections dropped out.
- **Pickups who joined:**
  - Ja'Kobe Walter (40.0), Tristan da Silva (32.0), De'Andre Hunter (29.0)
  - Brice Sensabaugh and Josh Okogie (26.0 each), Joan Beringer (25.0)
  - Aaron Nesmith (24.0), Kelly Oubre Jr. and Terrence Shannon Jr. (23.0 each)
  - Trey Lyles (22.0), Allen Graves (21.5)
- **Pickups who left:**
  - Mo Bamba, Precious Achiuwa (now rostered), Naji Marshall, P.J. Washington, Zaccharie Risacher
  - DeAndre Jordan, Jordan Poole, Ronald Holland II, Justin Champagnie, Bennedict Mathurin
  - Bilal Coulibaly, Jaylin Williams, Jock Landale
- **Pickups still listed, with lower figures:**
  - Hartenstein 46.0 → 40.5
  - Daniss Jenkins 44.0 → 30.3
  - Jaxson Hayes 35.7 → 30.0
  - Duncan Robinson 32.0 → 27.7
  - Aday Mara 32.0 → 23.0
  - Jared McCain 35.0 → 22.0
- **Back soon:**
  - Joined: Egor Demin, Ziaire Williams.
  - Left: Jaxson Hayes (now playing), Scoot Henderson, Justin Champagnie.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Desmond Bane 24.0, Trey Murphy III 24.8, CJ McCollum 27.2, Jalen Duren 33.5, Fred VanVleet 35.5. A pickup at or above **35.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| **Isaiah Hartenstein** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 26.0 | +3.7 | **40.5** | 29.6 | Free agent | 40% | 1 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 2 | 29.5 | +6.0 | **40.0** | 34.0 | Free agent | 16% | 2 / 3 |
| **Derrick Jones Jr.** | LAC | Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov), Jordan Miller (02 Mar) | 4 | 29.8 | +4.3 | **33.5** | 33.5 | Free agent | 5% | 2 / 3 |
| **Tristan da Silva** | ORL | Jalen Suggs (10 Nov), Paolo Banchero (22 Nov) | 1 | 31.0 | +3.0 | **32.0** | 27.5 | Free agent | 7% | 2 / 3 |
| **Daniss Jenkins** | DET | Jalen Duren (09 Nov) | 3 | 28.7 | +10.2 | **30.3** | 26.6 | Free agent | 9% | 1 / 3 |
| **Jaxson Hayes** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 37.0 | +13.3 | **30.0** | 34.2 | Free agent | 16% | 1 / 4 |
| **De'Andre Hunter** | SAC | Dylan Cardwell (06 Nov), Maxime Raynaud (10 Nov), Keegan Murray (06 Nov), Ben Simmons (01 Oct 2027) | 2 | 31.0 | +8.5 | **29.0** | 20.0 | Free agent | 5% | 2 / 4 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 5 | 26.8 | +6.5 | **28.6** | 28.6 | Free agent | 25% | 2 / 4 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 4 | 35.8 | +8.2 | **28.5** | 28.5 | Free agent | 17% | 1 / 3 |
| **Duncan Robinson** | DET | Jalen Duren (09 Nov) | 3 | 32.3 | +4.3 | **27.7** | 28.4 | Free agent | 29% | 1 / 3 |
| **Brice Sensabaugh** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 18.0 | +4.0 | **26.0** | 16.0 | Free agent | 2% | 1 / 4 |
| **Josh Okogie** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Lauri Markkanen (31 Oct), Jusuf Nurkic (04 Nov) | 1 | 28.0 | +15.0 | **26.0** | 9.0 | Free agent | 0% | 1 / 4 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 20.0 | +5.2 | **25.0** | 21.2 | Free agent | 1% | 2 / 4 |
| **Isaiah Jackson** | LAC | Max Strus (08 Nov), Brandon Ingram (08 Nov), Bradley Beal (08 Nov), Jordan Miller (02 Mar) | 4 | 21.5 | +3.1 | **24.5** | 25.0 | Free agent | 5% | 2 / 3 |
| **Aaron Nesmith** | IND | Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov), Johnny Furphy (02 Jan); also out: Ivica Zubac (30 Oct), T.J. McConnell (02 Nov) | 1 | 27.0 | +7.0 | **24.0** | 18.2 | Free agent | 3% | 2 / 3 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 3 | 19.7 | — | **24.0** | 24.0 | Free agent | 0% | 1 / 4 |
| **Kelly Oubre Jr.** | IND | Ben Sheppard (02 Jan), Tyrese Haliburton (13 Nov), Johnny Furphy (02 Jan); also out: Ivica Zubac (30 Oct), T.J. McConnell (02 Nov) | 1 | 30.0 | +7.2 | **23.0** | 17.8 | Free agent | 5% | 2 / 3 |
| **Terrence Shannon Jr.** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 27.0 | +4.8 | **23.0** | 23.0 | Free agent | 14% | 2 / 4 |
| **Aday Mara** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 20.5 | +7.5 | **23.0** | 16.2 | Free agent | 10% | 1 / 4 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (02 Nov) | 4 | 23.8 | — | **22.5** | 22.5 | Free agent | 5% | 1 / 3 |
| **Trey Lyles** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 1 | 22.0 | +8.0 | **22.0** | 13.2 | Free agent | 0% | 2 / 4 |
| **Jared McCain** | OKC | Jalen Williams (02 Mar), Cason Wallace (02 Mar); also out: Chet Holmgren (31 Oct), Nikola Topic (04 Nov) | 2 | 29.5 | +9.2 | **22.0** | 16.2 | Free agent | 38% | 1 / 4 |
| **Allen Graves** | TOR | Kawhi Leonard (23 Nov) | 2 | 19.0 | +6.5 | **21.5** | 20.2 | Free agent | 1% | 2 / 3 |
| **Sidy Cissoko** | POR | Shaedon Sharpe (02 Mar) | 3 | 23.7 | +7.5 | **20.7** | 20.7 | Free agent | 2% | 2 / 4 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 02 Nov | 4 | 41.5 | 24.7 | 22.5 | Free agent | 16% | 2 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 6 | — | 27.6 | 36.7 | Free agent | 7% | 1 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 12 | 26.3 | 29.1 | 34.7 | Free agent | 19% | 2 / 3 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 6 | — | 30.3 | 33.3 | Free agent | 43% | 1 / 3 |
| **Coby White** | CHA | Left Calf Strain | 02 Nov | 4 | — | 32.9 | 26.5 | Free agent | 66% | 2 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 30 Oct | 1 | — | 25.0 | 32.4 | Free agent | 6% | 1 / 4 |
| **Naji Marshall** | DAL | Illness | 30 Oct | 1 | 31.3 | 22.4 | 29.1 | Free agent | 13% | 1 / 4 |
| **Alex Caruso** | OKC | Right Ankle | 04 Nov | 6 | 30.8 | 24.0 | 18.0 | Free agent | 21% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 31 Oct | 2 | — | 30.1 | 28.0 | Free agent | 48% | 1 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 30 Oct | 1 | 15.0 | 30.0 | 22.2 | Free agent | 38% | 2 / 4 |
| **Ziaire Williams** | LAL | Foot | 30 Oct | 1 | 28.2 | 19.7 | 20.1 | Free agent | 6% | 2 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 12 | — | — | 28.1 | Free agent | 1% | 2 / 4 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 02 Nov | 4 | — | 27.4 | 21.3 | Free agent | 5% | 1 / 4 |
| **Dylan Cardwell** | SAC | Left Calf Strain | 06 Nov | 8 | — | — | 26.6 | Free agent | 0% | 2 / 4 |
| **Cameron Johnson** | DEN | Right Ankle Sprain | 30 Oct | 1 | 11.0 | 26.1 | 25.9 | Free agent | 9% | 1 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 10 | — | 25.6 | 10.5 | Free agent | 2% | 2 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 02 Nov | 4 | — | 24.4 | 25.5 | Free agent | 9% | 2 / 3 |
| **Oso Ighodaro** | PHX | Oblique Strain | 30 Oct | 1 | 18.0 | 25.3 | 22.4 | Free agent | 16% | 1 / 4 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

**Reported timeline:**

- **Jalen Duren:** strained right hamstring (23 Oct), out at least two weeks from 25 Oct (about 8 Nov); ESPN est. 9 Nov [CBS Detroit / AP](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/).
- **Kawhi Leonard:** left knee swelling, with no structural damage on the MRI.
  - The Raptors said on 27 Oct he will be re-evaluated in one week (about 3 Nov); Charania reports he will miss "a period of weeks".
  - ESPN est. 23 Nov [Yahoo Sports](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html).
  - Duren holds our only IR slot, so Leonard takes an active roster spot until one of them returns.

## Who takes the minutes, team by team

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Brandon Ingram | Right Achilles Surgery | 08 Nov | 35.3 | 36.5 | Melbourne poopoo |
| Max Strus | Right Foot Plantar Fasciitis | 08 Nov | 25.9 | 22.4 | Free agent |
| Bradley Beal | Right Knee Inflammation | 08 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

**Reported timeline:**

- **Max Strus:** Partial plantar fascia tear in his right foot (5 Oct preseason opener), with re-evaluation set for four weeks; on 28 Oct the Clippers said he is progressing but will stay in LA for the MIN/GSW trip and is out at least another week; ESPN est. 8 Nov. [Yahoo Sports](https://sports.yahoo.com/articles/clippers-injury-woes-pile-latest-005153258.html) [Basketnews](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html)
- **Brandon Ingram:** Partially torn Achilles, found during his May heel surgery; on 28 Oct the Clippers said he is progressing but will not travel for the MIN/GSW games and is out at least another week; ESPN est. 8 Nov. [Basketnews](https://basketnews.com/news-258395-la-clippers-provide-new-huge-injury-updates-on-brandon-ingram-others.html) [Hoops Rumors](https://www.hoopsrumors.com/2026/10/brandon-ingram-returns-to-on-court-work.html)
- **Bradley Beal:** Right knee inflammation, being managed for pain; still no timetable reported as of 25 Oct; ESPN est. 8 Nov. [SI](https://www.si.com/nba/clippers/onsi/clippers-injury-report-thunder-latest-brandon-ingram-bradley-beal-01m5t411kj1v)
- **Jordan Miller:** Torn left rotator cuff, repaired surgically on 26 Aug; expected to be re-evaluated in about six months (late Feb); ESPN est. 2 Mar. [Hoops Rumors](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 4 | 30.2 | +8.2 | 4 | **36.2** | 20.0 | Dr White Slong | 43% |
| Derrick Jones Jr. | SF/PF | 4 | 29.8 | +4.3 | 4 | **33.5** | 21.1 | Free agent | 5% |
| Isaiah Jackson | PF/C | 4 | 21.5 | +3.1 | 4 | **24.5** | 20.6 | Free agent | 5% |
| Kobe Sanders | SG | 4 | 21.2 | — | 1 | **19.2** | — | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Keegan Murray | Ankle | 06 Nov | 34.6 | 12.0 | Dr White Slong |
| Maxime Raynaud | Right Knee Dislocated | 10 Nov | 26.6 | 28.1 | Free agent |
| Ben Simmons | Right Achilles Surgery | 01 Oct 2027 | 21.2 | — | Free agent |
| Dylan Cardwell | Left Calf Strain | 06 Nov | 20.7 | 26.6 | Free agent |

**Reported timeline:**

- **Dylan Cardwell:** Left calf strain (8 Oct preseason); began on-court activities and will be re-evaluated about seven days from 26 Oct (about 2 Nov); ESPN est. 6 Nov. [Hoops Rumors](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
- **Maxime Raynaud:** Right patellar subluxation (10 Oct preseason at GSW); progressing well, to be checked again about two weeks from 26 Oct (about 9 Nov); ESPN est. 10 Nov. [Hoops Rumors](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
- **Keegan Murray:** Capsulitis in his surgically repaired left ankle; to be re-evaluated 10-14 days from 26 Oct (about 5-9 Nov); ESPN est. 6 Nov. [Hoops Rumors](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
- **Ben Simmons:** Torn right Achilles at practice on 18 Oct, surgically repaired 20 Oct; out for the 2026-27 season with no official timetable; ESPN est. Oct 2027. [NBC Sports](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season) [RotoWire](https://www.rotowire.com/basketball/headlines/ben-simmons-injury-undergoes-successful-surgery-tuesday-535308)

Last 4 games: 2 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| De'Andre Hunter | SF/PF | 2 | 31.0 | +8.5 | 2 | **29.0** | 11.0 | Free agent | 5% |
| Jonathan Mogbo | PF | 2 | 18.0 | +10.0 | 0 | **13.5** | -2.0 | Free agent | 0% |

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

**Reported timeline:**

- **Jimmy Butler III:** Torn right ACL (19 Jan 2026), reconstructed on 9 Feb; still sidelined and observing at training camp; no official timetable; ESPN est. 2 Jan. [Yahoo Sports](https://sports.yahoo.com/articles/warriors-star-jimmy-butler-undergoes-011844268.html) [SF Chronicle](https://www.sfchronicle.com/sports/warriors/article/warriors-jimmy-butler-though-injured-makes-22461500.php)
- **Kristaps Porzingis:** Undisclosed health matter; the Warriors list him out indefinitely, with an update "when available and appropriate"; no timetable reported; ESPN est. 1 Dec. [ESPN](https://www.espn.com/nba/story/_/id/50184641/warriors-kristaps-porzingis-indefinitely-team) [CBS Sports](https://www.cbssports.com/nba/news/warriors-kristaps-porzingis-mysterious-health-issues-timeline/)
- **Moses Moody:** Torn left patellar tendon (March 2026), surgically repaired; light on-court work since late September, and the team hopes for a return in early 2027; no official timetable; ESPN est. 1 Dec. [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-09-29/moses-moody-knee-limited-to-light-on-court-work)

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 5 | 33.6 | +9.0 | 5 | **43.8** | 23.5 | **us** | 85% |
| Graham Ike | PF | 4 | 13.2 | — | 2 | **20.8** | — | Free agent | 0% |
| Brandon Williams | PG/SG | 5 | 16.0 | — | 1 | **19.2** | — | Free agent | 1% |
| Georges Niang | PF | 5 | 19.4 | — | 1 | **12.4** | — | Free agent | 0% |
| Will Richard | SG/SF | 5 | 16.0 | — | 1 | **12.2** | — | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

**Reported timeline:**

- **Ben Sheppard:** Torn left meniscus (21 Oct opener at NOP); the surgery turned out to need a full repair, and on 28 Oct Carlisle said he will miss multiple months, revising an earlier "a few weeks"; no timetable; ESPN est. 2 Jan. [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months) [Hoops Rumors](https://www.hoopsrumors.com/2026/10/pacers-ben-sheppard-suffers-torn-left-meniscus.html)
- **Tyrese Haliburton:** Mild left hamstring strain (reported 28 Oct), four games into his return from a torn Achilles; Carlisle calls him week-to-week, gives the next update in two weeks (about 11 Nov) and doesn't expect him to play before then; ESPN est. 13 Nov. [Hoops Wire](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/)
- **Johnny Furphy:** Torn right ACL (8 Feb 2026), surgically repaired; on 25 Sep the Pacers said he has hit every benchmark and the original timeline points to midseason, without naming a date; ESPN est. 2 Jan. [Yahoo Sports](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html)
- **Ivica Zubac:** Left ankle sprain (25 Oct at BKN), with negative X-rays but swelling; Carlisle hoped it would be day-to-day, and he was ruled out for 27 Oct at MIL; no timetable reported; ESPN est. 30 Oct. [iPacers](https://ipacers.com/2026/10/26/indiana-pacers-injury-report-ivica-zubac-leaves-on-crutches-after-pacers-win-in-brooklyn/) [Yahoo Sports](https://sports.yahoo.com/articles/long-ivica-zubac-pacers-latest-192453932.html)
- **T.J. McConnell:** Right hamstring strain from the preseason and has not played this season; on 28 Oct Carlisle said he is "getting closer" but gave no date; ESPN est. 2 Nov. [RotoWire](https://www.rotowire.com/basketball/headlines/tj-mcconnell-injury-getting-closer-to-return-536530)

Last 5 games: 1 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Ivica Zubac (left ankle sprain; ESPN est. 30 Oct), T.J. McConnell (right hamstring strain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard | PG/SG | 1 | 35.0 | +3.0 | 1 | **39.0** | 31.3 | Matt Wright's Foxies | 61% |
| Aaron Nesmith | SG/SF | 1 | 27.0 | +7.0 | 1 | **24.0** | 16.3 | Free agent | 3% |
| Kelly Oubre Jr. | SG/SF | 1 | 30.0 | +7.2 | 1 | **23.0** | 16.5 | Free agent | 5% |
| Larry Nance Jr. | PF | 1 | 23.0 | +11.2 | 0 | **12.0** | 6.5 | Free agent | 0% |
| Jalen Slawson | SF | 1 | 12.0 | +3.0 | 0 | **11.0** | 11.3 | Free agent | 0% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |
| Jalen Suggs | Right Knee | 10 Nov | 33.3 | 26.3 | Free agent |

**Reported timeline:**

- **Jalen Suggs:** Mild right knee bone bruise with no structural damage (25 Oct vs NYK); to be re-evaluated in two weeks from 26 Oct (about 9 Nov); ESPN est. 10 Nov. [Yahoo Sports](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html)
- **Paolo Banchero:** Low-grade right high ankle sprain (23 Oct vs MIN); Charania reported the usual recovery is four to six weeks (about 20 Nov to 4 Dec), which the team has not confirmed; ESPN est. 22 Nov. [Yahoo Sports](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html)

Last 4 games: 1 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Tristan da Silva | SF/PF | 1 | 31.0 | +3.0 | 0 | **32.0** | 26.0 | Free agent | 7% |
| Nikola Vucevic | C | 1 | 16.0 | +8.0 | 0 | **14.0** | 8.0 | Free agent | 43% |
| Jevon Carter | PG | 1 | 22.0 | +9.0 | 0 | **10.0** | 9.0 | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

**Reported timeline:**

- **Anthony Edwards:** Right knee problem that the team says is not the meniscus; arthroscopic cleanup surgery set for 29 Oct; reports say he will miss around two months and "could be out until the calendar flips to 2027", and the team gave no specific timeline; ESPN est. 21 Dec. [Yahoo Sports / USA Today](https://uk.sports.yahoo.com/news/anthony-edwards-injury-timberwolves-star-230840389.html) [NY1 / AP](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/28/timberwolves-say-anthony-edwards-will-be-good-as-new-with-no-long-term-concern-after-knee-surgery)
- **Donte DiVincenzo:** Torn right Achilles (25 Apr, playoffs), surgery in late April; Windhorst reported Minnesota is cautiously optimistic he returns near the end of the 2026-27 season, with no timetable set; ESPN est. 2 Apr. [RotoWire](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)

Last 5 games: 1 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 1 | 32.0 | +5.8 | 1 | **47.0** | 25.8 | Cream Abdul-Yammar | 64% |
| Jaden McDaniels | SF/PF | 1 | 35.0 | +3.2 | 1 | **30.0** | 36.8 | Melbourne poopoo | 87% |
| Joan Beringer | C | 1 | 20.0 | +5.2 | 0 | **25.0** | 20.2 | Free agent | 1% |
| Terrence Shannon Jr. | SG | 1 | 27.0 | +4.8 | 0 | **23.0** | 23.0 | Free agent | 14% |
| Trey Lyles | PF | 1 | 22.0 | +8.0 | 0 | **22.0** | 11.0 | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Cason Wallace | Left Shoulder | 02 Mar | 26.6 | 18.7 | Free agent |

**Reported timeline:**

- **Jalen Williams:** Fractured left fibula and dislocated left ankle on 25 Oct vs LAC; had surgery in New York on 28 Oct and will be re-evaluated before the end of the regular season, expected to miss most if not all of it; ESPN est. 2 Mar. [Yahoo Sports](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
- **Cason Wallace:** Torn left shoulder labrum on 25 Oct, needs surgery; Presti said on 26 Oct there is no timeline and the team will reassess after surgery, while Brett Siegel reported a 5-6 month recovery; ESPN est. 2 Mar. [SI](https://www.si.com/nba/thunder/onsi/okc-thunder-guard-cason-wallace-will-require-surgery-for-labrum-tear) [ClutchPoints](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-cason-wallace-miss-significant-time-shoulder-injury)
- **Chet Holmgren:** Right knee patellar tendinitis; missed 26 Oct vs PHX and was ruled out for 28 Oct at DAL; no timetable reported; ESPN est. 31 Oct. [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/chet-holmgren-knee-remains-out-wednesday-vs-dal)
- **Nikola Topic:** Recovering from a June lumbar microdiscectomy. CBS reported on 26 Oct that he was off the injury report and ready to debut, but he was inactive that night and was listed out (lower back surgery) for 28 Oct at DAL; no timetable reported; ESPN est. 4 Nov. [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-ready-for-season-debut/) [Basketball-Reference](https://www.basketball-reference.com/boxscores/202610260OKC.html) [SI](https://si.com/nba/mavericks/onsi/kyrie-irving-injury-status-dallas-mavericks-get-set-battered-okc-thunder-)

Last 5 games: 2 game(s) without them, 3 with them.

Also out in those games, so part of the gain is theirs: Chet Holmgren (right knee; ESPN est. 31 Oct), Nikola Topic (back; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Isaiah Hartenstein | C | 2 | 26.0 | +3.7 | 2 | **40.5** | 22.3 | Free agent | 40% |
| Aday Mara | C | 2 | 20.5 | +7.5 | 0 | **23.0** | 11.7 | Free agent | 10% |
| Jared McCain | PG/SG | 2 | 29.5 | +9.2 | 2 | **22.0** | 12.3 | Free agent | 38% |
| Kenrich Williams | SF | 2 | 20.5 | +13.8 | 2 | **13.0** | 7.0 | Free agent | 0% |
| Jaylin Williams | PF/C | 2 | 23.0 | +10.7 | 0 | **13.0** | 7.0 | Free agent | 2% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

**Reported timeline:**

- **Jamir Watkins:** Torn left ACL in Summer League (9 Jul), reconstructed on 30 Jul; no timetable reported, and he could miss the season; ESPN est. 2 Apr. [RotoWire](https://www.rotowire.com/basketball/headlines/jamir-watkins-injury-undergoes-surgery-for-torn-acl-532251)
- **Justin Champagnie:** Fractured right foot on 26 Oct at Charlotte, surgery on 28 Oct; expected to miss several months, and Washington hopes he is back by the All-Star break (19–24 Feb); ESPN est. 25 Feb. [Josh Robbins](https://x.com/JoshuaBRobbins/status/2115511438341185737) [Yahoo Sports](https://sports.yahoo.com/articles/justin-champagnie-gets-injury-timeline-195034430.html)

Last 5 games: 1 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Tre Johnson (right achilles soreness; ESPN est. 30 Oct).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 1 | 38.0 | +8.0 | 1 | **34.0** | 29.8 | Snow Time Lakers | 47% |
| Khris Middleton | SF/PF | 1 | 23.0 | +9.3 | 0 | **5.0** | 4.7 | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

**Reported timeline:**

- **Kawhi Leonard:** Left knee swelling, and the MRI showed no structural damage; the Raptors said on 27 Oct he begins a treatment and rehab program and will be re-evaluated in one week (about 3 Nov), and Charania reports he will miss "a period of weeks"; ESPN est. 23 Nov. [Yahoo Sports](https://sports.yahoo.com/articles/kawhi-leonard-injury-latest-news-160039647.html)

Last 4 games: 2 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Ja'Kobe Walter | SG | 2 | 29.5 | +6.0 | 2 | **40.0** | 28.0 | Free agent | 16% |
| Allen Graves | SF | 2 | 19.0 | +6.5 | 0 | **21.5** | 19.0 | Free agent | 1% |
| Trayce Jackson-Davis | PF | 2 | 13.0 | +7.5 | 0 | **20.5** | 7.0 | Free agent | 0% |
| Jamison Battle | SF | 2 | 16.5 | +5.0 | 0 | **10.5** | 17.0 | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

**Reported timeline:**

- **Jaren Jackson Jr.:** Torn right MCL (26 Oct vs MEM); the team says at least six weeks and ESPN sources say six to eight with no surgery (about 7-21 Dec); ESPN est. 14 Dec. [Salt Lake Tribune](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
- **Lauri Markkanen:** Right wrist sprain (26 Oct vs MEM), day-to-day; downgraded to out for 28 Oct vs SAS; no timetable reported; ESPN est. 31 Oct. [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/jazzs-lauri-markkanen-wont-play-wednesday-536560/)
- **Jusuf Nurkic:** Partial plantar plate tear in the second toe of his right foot (4 Oct preseason); re-evaluation in four weeks from the 7 Oct announcement (about 4 Nov); ESPN est. 4 Nov. [NBA.com](https://www.nba.com/news/jazz-jusuf-nurkic-foot-injury)

Last 5 games: 1 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Lauri Markkanen (right wrist; ESPN est. 31 Oct), Jusuf Nurkic (right foot strain; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Keyonte George | PG/SG | 1 | 37.0 | +5.2 | 1 | **31.0** | 40.5 | Cream Abdul-Yammar | 88% |
| Jaxson Hayes | C | 1 | 37.0 | +13.3 | 1 | **30.0** | 35.7 | Free agent | 16% |
| Ace Bailey | SF/PF | 1 | 40.0 | +12.8 | 1 | **26.0** | 38.8 | Dr White Slong | 63% |
| Brice Sensabaugh | SG/SF | 1 | 18.0 | +4.0 | 0 | **26.0** | 13.5 | Free agent | 2% |
| Josh Okogie | SF | 1 | 28.0 | +15.0 | 0 | **26.0** | 3.3 | Free agent | 0% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 09 Nov | 31.0 | 33.5 | **us** |

**Reported timeline:**

- **Jalen Duren:** Strained right hamstring (23 Oct vs MIA); announced on 25 Oct as out at least two weeks (about 8 Nov); ESPN est. 9 Nov. [CBS Detroit / AP](https://www.cbsnews.com/detroit/news/pistons-center-jalen-duren-strained-hamstring/)

Last 5 games: 3 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Cade Cunningham | PG | 3 | 36.0 | +3.5 | 3 | **50.3** | 39.0 | **us** | 100% |
| Paul Reed | PF/C | 3 | 29.0 | +7.5 | 3 | **40.0** | 33.5 | **us** | 30% |
| Daniss Jenkins | PG | 3 | 28.7 | +10.2 | 1 | **30.3** | 21.0 | Free agent | 9% |
| Duncan Robinson | SG/SF | 3 | 32.3 | +4.3 | 3 | **27.7** | 29.5 | Free agent | 29% |
| Ronald Holland II | SF/PF | 3 | 15.7 | +3.2 | 0 | **14.3** | 16.0 | Free agent | 1% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |

**Reported timeline:**

- **Shaedon Sharpe:** Torn right meniscus in an offseason workout, with surgery in late Aug; the team said he will be re-evaluated in six months (about 27 Feb); ESPN est. 2 Mar. [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)

Last 3 games: 3 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 3 | 23.7 | +7.5 | 0 | **20.7** | 10.6 | Free agent | 2% |
| Micah Potter | C | 1 | 12.0 | — | 0 | **6.0** | — | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

**Reported timeline:**

- **Mark Williams:** Torn left shoulder labrum, surgically repaired 10 Sep; the Suns have set no timetable, and Arizona Sports' John Gambadoro reported a five-month minimum (about 10 Feb at the earliest); ESPN est. 3 Feb. [Yahoo Sports](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html)

Last 3 games: 3 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 3 | 19.7 | — | 0 | **24.0** | — | Free agent | 0% |

### BOS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Devin Carter | Illness | 08 Nov | 18.4 | 18.9 | Free agent |

**Reported timeline:**

- **Devin Carter:** Mononucleosis, diagnosed after he missed the last three preseason games; still out on 27 Oct with no timetable reported; ESPN est. 8 Nov. [Yahoo Sports](https://sports.yahoo.com/articles/celtics-injury-report-two-way-193259841.html)

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

No teammate has gained 3+ minutes in those games.

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

**Reported timeline:**

- **Julian Strawther:** Left knee sprain (14 Oct preseason vs LAC); to be re-evaluated in six weeks (late Nov); ESPN est. 29 Nov. [NBC Sports](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain)
- **Spencer Jones:** Hamstring injury from the preseason (listed as bilateral hamstring injury management) and has not played this season; on 27 Oct the Denver Gazette said he could be back within the next three games, but there is no firm timetable; ESPN est. 2 Nov. [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-nearing-return-to-action/) [RotoWire](https://www.rotowire.com/basketball/headlines/spencer-jones-injury-remains-out-for-wednesday-536395)

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Jamal Murray | PG | 4 | 38.5 | +3.5 | 4 | **43.8** | 43.9 | **us** | 99% |
| Christian Braun | SG/SF | 4 | 35.8 | +8.2 | 4 | **28.5** | 23.1 | Free agent | 17% |
| Trevon Brazile | SF/PF | 4 | 23.8 | — | 1 | **22.5** | — | Free agent | 5% |
| Alpha Diallo (out, ESPN est. back 30 Oct) | SF | 1 | 22.0 | — | 0 | **13.0** | — | Free agent | 0% |
| Bryce Hopkins | SF | 4 | 16.5 | — | 2 | **6.5** | — | Free agent | 0% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

**Reported timeline:**

- **Mouhamed Gueye:** Fractured left foot, surgically repaired 14 Jul; the team said he would be reassessed in three to four months (mid-Oct to mid-Nov), and he is still listed out with no update since; ESPN est. 20 Nov. [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/hawks-mouhamed-gueye-out-3-to-4-months-with-foot-injury/)

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 5 | 26.8 | +6.5 | 0 | **28.6** | 19.2 | Free agent | 25% |
| Jock Landale | C | 5 | 18.2 | — | 0 | **19.0** | — | Free agent | 1% |

## Every injury

All 86 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct 2027 | 337 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct 2027 | 337 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 245 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 155 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 155 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 124 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 124 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 124 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder | 02 Mar | 124 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 119 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 97 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 65 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 65 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 65 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 53 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 46 | Matt Wright's Foxies |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 35 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 33 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 33 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 31 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 25 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 24 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 22 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 20 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 20 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 15 | Lauri Birds |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 12 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 12 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 11 | **us** |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 10 | Free agent |
| Max Strus | LAC | Out | Right Foot Plantar Fasciitis | 08 Nov | 10 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 10 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 10 | Melbourne poopoo |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 08 Nov | 10 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 06 Nov | 8 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 06 Nov | 8 | Dr White Slong |
| Dylan Cardwell | SAC | Out | Left Calf Strain | 06 Nov | 8 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 04 Nov | 6 | Free agent |
| Tacko Fall | PHI | Out | Left Quadriceps Strain | 04 Nov | 6 | Free agent |
| Nikola Topic | OKC | Out | Back | 04 Nov | 6 | Free agent |
| Nic Claxton | CHI | Out | Hamstring | 04 Nov | 6 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 04 Nov | 6 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 04 Nov | 6 | Free agent |
| Alex Caruso | OKC | Out | Right Ankle | 04 Nov | 6 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 02 Nov | 4 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 02 Nov | 4 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 02 Nov | 4 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 02 Nov | 4 | Free agent |
| Spencer Jones | DEN | Out | Hamstring | 02 Nov | 4 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 02 Nov | 4 | — |
| Kylan Boswell | CHA | Out | Right Knee Surgery | 02 Nov | 4 | — |
| Kon Knueppel | CHA | Out | Left Hamstring | 02 Nov | 4 | Team Nic Kerr |
| Grant Williams | CHA | Out | Right Hamstring | 02 Nov | 4 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 02 Nov | 4 | Free agent |
| Coby White | CHA | Out | Left Calf Strain | 02 Nov | 4 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 31 Oct | 2 | Free agent |
| Lauri Markkanen | UTAH | Day-To-Day | Right Wrist | 31 Oct | 2 | Lauri Birds |
| Chet Holmgren | OKC | Day-To-Day | Right Knee | 31 Oct | 2 | Team Nic Kerr |
| Ziaire Williams | LAL | Day-To-Day | Foot | 30 Oct | 1 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 30 Oct | 1 | Free agent |
| Tre Johnson | WSH | Day-To-Day | Right Achilles Soreness | 30 Oct | 1 | Free agent |
| Tobe Awaka | CHI | Day-To-Day | Ankle | 30 Oct | 1 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 30 Oct | 1 | Free agent |
| Simone Fontecchio | MIA | Day-To-Day | Illness | 30 Oct | 1 | Free agent |
| Sergio de Larrea | DAL | Day-To-Day | Right Knee Strain | 30 Oct | 1 | Free agent |
| Santi Aldama | DAL | Out | Right Knee Surgery | 30 Oct | 1 | Free agent |
| Rui Hachimura | LAC | Day-To-Day | Left Quadriceps Soreness | 30 Oct | 1 | Free agent |
| Patrick Williams | CHI | Out | Right Groin Soreness | 30 Oct | 1 | Free agent |
| Oso Ighodaro | PHX | Day-To-Day | Oblique Strain | 30 Oct | 1 | Free agent |
| Naji Marshall | DAL | Day-To-Day | Illness | 30 Oct | 1 | Free agent |
| Marcus Smart | HOU | Out | Left Forearm Strain | 30 Oct | 1 | Free agent |
| Luka Doncic | LAL | Day-To-Day | Back | 30 Oct | 1 | Team Nic Kerr |
| Jose Alvarado | NY | Out | Left Ankle Sprain | 30 Oct | 1 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 30 Oct | 1 | Free agent |
| Jabari Walker | PHI | Day-To-Day | Left Knee Soreness | 30 Oct | 1 | Free agent |
| Ivica Zubac | IND | Day-To-Day | Left Ankle Sprain | 30 Oct | 1 | Lauri Birds |
| Isaiah Joe | DET | Day-To-Day | Right Hip Bruise | 30 Oct | 1 | Free agent |
| Gui Santos | GS | Day-To-Day | Left Knee Tendinitis | 30 Oct | 1 | Free agent |
| Egor Demin | BKN | Day-To-Day | Right Leg Bruise | 30 Oct | 1 | Free agent |
| Cameron Johnson | DEN | Out | Right Ankle Sprain | 30 Oct | 1 | Free agent |
| Cameron Carr | LAL | Out | Right Oblique Strain | 30 Oct | 1 | Free agent |
| Alpha Diallo | DEN | Out | Right Personal | 30 Oct | 1 | Free agent |
| Alperen Sengun | HOU | Day-To-Day | Back Soreness | 30 Oct | 1 | Cream Abdul-Yammar |
| Adou Thiero | LAL | Out | Left Knee Inflammation | 30 Oct | 1 | Free agent |
| Jordan Poole | NO | Day-To-Day | Left Ankle | 29 Oct | 0 | Free agent |
| Chris Youngblood | POR | Out | Left Ankle Soreness | 29 Oct | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-10-29 05:38 UTC.
