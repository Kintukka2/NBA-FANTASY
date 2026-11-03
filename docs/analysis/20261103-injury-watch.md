# Injury Watch: 02 Nov 2026

- Generated 2026-11-02 23:01 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 99 players in ESPN's injury feed. 27 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 15 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L15 and L30 cover every game so far for every player listed, so they equal the season average for now.
- **Games** is games left this week (02 Nov–08 Nov) / next week (09 Nov–15 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

Our five lowest are Murphy 27.7 (L7 27.3 (3)), Hartenstein 28.7 (L7 35.0 (3)), Bane 29.0 (L7 37.0 (3)), Duren 33.5 (out) and VanVleet 35.4 (L7 31.3 (3)). That puts the floor at 35.4, and no pickup clears it. Our IR slot holds Kawhi Leonard, so a stash costs a bench spot.

| Player | NBA | Opening and its window | FP/g without | Season | L7 / L15 / L30 | Min without | Games this / next week |
|---|---|---|---:|---:|---|---:|---|
| **Christian Braun** | DEN | Starter, not tied to an injury (Strawther re-evaluated about 29 Nov; *ESPN est.* 29 Nov) | 34.6 | 34.6 | 40.3 (3) / 34.6 (5) / 34.6 (5) | 36.0 | 3 / 3 |
| **Naji Marshall** | DAL | Lively out (no timetable reported; *ESPN est.* 12 Nov); Aldama's debut is the threat | 31.3 | 31.3 | — / 31.3 (3) / 31.3 (3) | 27.7 | 4 / 4 |
| **De'Andre Hunter** | SAC | Keegan Murray out (re-evaluated about 5–9 Nov; *ESPN est.* 10 Nov), so the window is short | 28.0 | 22.2 | 33.3 (3) / 22.2 (6) / 22.2 (6) | 32.8 | 4 / 3 |
| **Aday Mara** | OKC | Holmgren out to about 25 Dec–8 Jan (*ESPN est.* 2 Jan); a long window at a low rate, still off the bench | 27.3 | 19.5 | 27.3 (3) / 19.5 (6) / 19.5 (6) | 23.0 | 4 / 4 |

- **Back-soon stash candidates:**
  - **Jusuf Nurkic** (UTAH): 36.7 over 41 games in 2026. He was out again Monday. His re-evaluation is due about 4 Nov, with no result or minutes limit reported (*ESPN est.* 4 Nov). The starting centre job that Hayes holds is waiting for him. Games: 4 this week, 4 next. He is Sunday's add in the matchup plan.
  - **Nic Claxton** (CHI): 33.3 over 69 games. He practised fully on Sunday but "isn't ready to appear in games yet". No timetable reported (*ESPN est.* 4 Nov). The starting centre job is waiting for him. Games: 3 and 3.
- **L7 notes:** Braun's L7 rests on one 31-point, seven-three night, and RotoWire calls him a sell-high. Hunter's L7 comes from 32–37 minutes while Murray is out. Mara's L7 comes from more minutes since Holmgren's injury.

## Since the last Injury Watch

Against `docs/analysis/20261102-injury-watch.md` (this morning). No NBA game was played in between, so the changes are status changes.

- **New absences:**
  - Jalen Johnson (ATL; Snow Time Lakers): out Monday, left ankle sprain, no timetable reported; *ESPN est.* 4 Nov.
  - Derrick Jones Jr. (LAC): now out, right knee soreness; *ESPN est.* 4 Nov.
  - Rui Hachimura (LAC): left quadriceps bruise; *ESPN est.* 4 Nov.
  - Reece Beekman (WSH): shoulder; *ESPN est.* 3 Dec.
  - Our own players: Dejounte Murray (personal), and rest days for Paul George and Anthony Black.
- **ESPN estimates pushed back:**
  - Keegan Murray: 6 → 10 Nov.
  - Ivica Zubac: 2 → 9 Nov.
  - T.J. McConnell: 2 → 9 Nov.
  - Nate Bittle: 2 → 9 Nov.
- **Off the injury feed:** Trey Murphy III (ours), Max Strus (debuts Monday), Draymond Green and Stephen Curry (rest days over), Mitchell Robinson, Mikel Brown Jr., Tim Hardaway Jr., Tobe Awaka and Ziaire Williams.
- **Pickups:**
  - **Left:** Zaccharie Risacher, who is now rostered by Snow Time Lakers, and Precious Achiuwa.
  - **Joined:** De'Andre Hunter, because Keegan Murray is now among Sacramento's absentees.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Trey Murphy III 27.7 (L7 27.3), Isaiah Hartenstein 28.7 (L7 35.0), Desmond Bane 29.0 (L7 37.0), Jalen Duren 33.5 (L7 —), Fred VanVleet 35.4 (L7 31.3). A pickup at or above **35.4** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Christian Braun** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (04 Nov) | 5 | 36.0 | +8.5 | **34.6** | 34.6 | 40.3 (3) | 34.6 (5) | 34.6 (5) | Free agent | 35% | 3 / 3 |
| **Naji Marshall** | DAL | Dereck Lively II (12 Nov); also out: Santi Aldama (02 Nov) | 3 | 27.7 | +3.5 | **31.3** | 31.3 | — | 31.3 (3) | 31.3 (3) | Free agent | 11% | 4 / 4 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 7 | 25.9 | +5.6 | **28.9** | 28.9 | 25.5 (4) | 28.9 (7) | 28.9 (7) | Waivers | 32% | 4 / 3 |
| **De'Andre Hunter** | SAC | Maxime Raynaud (10 Nov), Keegan Murray (10 Nov), Ben Simmons (01 Oct); also out: Dylan Cardwell (02 Nov) | 4 | 32.8 | +10.2 | **28.0** | 22.2 | 33.3 (3) | 22.2 (6) | 22.2 (6) | Free agent | 8% | 4 / 3 |
| **Derrick Jones Jr.** (out, ESPN est. back 04 Nov) | LAC | Jordan Miller (02 Mar); also out: Brandon Ingram (08 Nov), Bradley Beal (08 Nov) | 6 | 28.8 | +3.4 | **27.8** | 27.8 | 27.0 (3) | 27.8 (6) | 27.8 (6) | Free agent | 13% | 3 / 3 |
| **P.J. Washington** | DAL | Dereck Lively II (12 Nov); also out: Santi Aldama (02 Nov) | 6 | 33.7 | +4.7 | **27.5** | 27.5 | 27.7 (3) | 27.5 (6) | 27.5 (6) | Free agent | 24% | 4 / 4 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 23.0 | +10.0 | **27.3** | 19.5 | 27.3 (3) | 19.5 (6) | 19.5 (6) | Free agent | 16% | 4 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 4 | 21.0 | — | **27.2** | 27.2 | 32.0 (2) | 27.2 (4) | 27.2 (4) | Free agent | 2% | 4 / 4 |
| **Toumani Camara** | POR | Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 1 | 31.0 | +6.0 | **27.0** | 31.0 | 28.3 (3) | 31.0 (5) | 31.0 (5) | Free agent | 42% | 4 / 3 |
| **Jaxson Hayes** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 28.5 | +4.8 | **27.0** | 32.2 | 27.0 (2) | 32.2 (5) | 32.2 (5) | Free agent | 16% | 4 / 4 |
| **Jamal Shead** | TOR | Kawhi Leonard (23 Nov) | 4 | 23.0 | +3.0 | **25.5** | 20.7 | 30.0 (3) | 20.7 (6) | 20.7 (6) | Free agent | 3% | 3 / 4 |
| **Joan Beringer** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 3 | 24.0 | +9.2 | **23.0** | 21.6 | 26.5 (4) | 21.6 (7) | 21.6 (7) | Free agent | 2% | 4 / 2 |
| **Scoot Henderson** | POR | Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 1 | 31.0 | +12.0 | **22.0** | 9.6 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% | 4 / 3 |
| **Brice Sensabaugh** | UTAH | Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (04 Nov) | 2 | 18.5 | +4.5 | **22.0** | 16.3 | 19.3 (3) | 16.3 (6) | 16.3 (6) | Free agent | 2% | 4 / 4 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov); also out: Spencer Jones (04 Nov) | 5 | 22.8 | — | **22.0** | 22.0 | 19.3 (3) | 22.0 (5) | 22.0 (5) | Free agent | 4% | 3 / 3 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar); also out: Nikola Topic (04 Nov) | 3 | 29.0 | +8.7 | **20.0** | 16.2 | 20.0 (3) | 16.2 (6) | 16.2 (6) | Free agent | 32% | 4 / 4 |
| **Kobe Sanders** | LAC | Jordan Miller (02 Mar); also out: Brandon Ingram (08 Nov), Bradley Beal (08 Nov) | 6 | 23.2 | — | **20.0** | 20.0 | 22.0 (3) | 20.0 (6) | 20.0 (6) | Free agent | 1% | 3 / 3 |

### Notes

#### Christian Braun (DEN). L7 40.3 (3) against a season of 34.6, so 5+ above.
- **Role:** entrenched starter, listed in the starting five on 28 Oct and 30 Oct. RotoWire's expected lineup has him starting at SG Mon vs POR (9:00 pm ET). [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/spencer-jones-hamstring-remains-out-monday) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Why L7 is above his average:** shooting, not role. On 30 Oct at PHX he made a career-high seven threes for 31 points, after going 5-of-21 from three in his first four games. Adelman praised his "floor game in general along with the shot making." Cam Johnson's return to the lineup the same night did not cost Braun his start. [Denver Gazette, 30 Oct](https://gazette.com/2026/10/30/christian-braun-catches-fire-as-nuggets-rally-past-suns-127-120/) NBC also expects his three-game steals run to regress. (unchanged since 2 Nov) [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/christian-braun-with-31-points-hits-7-3-pointers)
- **Does a return end it?** No. No source ties his start to Strawther (re-evaluated about 29 Nov) or Spencer Jones. NBC says Jones's absence feeds Brazile's minutes instead. [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/spencer-jones-hamstring-remains-out-monday)

#### Naji Marshall (DAL). No L7: no game in the last 7 days. L15 31.3 (3).
- **Status:** off the injury report for Mon vs SAC after an illness. May: "Naji's feeling much, much better. He looks good. He looks ready to go." An illness kept him out of the previous two games, and he was available on Friday but did not play. [Yardbarker / Dallas Sports Journal, 2 Nov](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904) He practised on Sunday. (unchanged since 2 Nov) [Dallas Sports Journal, 1 Nov](https://dallassportsjournal.com/kyrie-irving-questionable-mavericks-injury-report-kings/)
- **Role:** with Kyrie Irving doubtful, NBC says Marshall "could replace him in the starting lineup." RotoWire's *expected* DAL five is Sasser, Christie, Flagg, P.J. Washington and Gafford, which leaves Marshall on the bench. Treat the start as unconfirmed. [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/kyrie-irving-knee-doubtful-monday-vs-sac) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php) The DMN calls him one of Dallas's three lead initiators. (unchanged since 2 Nov) [Dallas Morning News via Yahoo, 2 Nov](https://sports.yahoo.com/articles/mavericks-october-highs-lows-flagg-011945935.html)
- **Does a return end it?** Lively's return does not touch his wing and playmaking role directly. Irving's return trims his ball-handling load. Aldama's debut is the frontcourt threat. No source ties a return to Marshall's minutes.

#### Aaron Wiggins (ATL). L7 25.5 (4) against a season of 28.9, not 5+ off.
- **Role: projected starter Monday.** Jalen Johnson was ruled out at 6:00 PM, and RotoWire's expected ATL five is McCollum, Alexander-Walker, Daniels, **Wiggins** and Okongwu. CBS named Wiggins and Dort as the top candidates. This is expected, not confirmed. [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php) [CBS Sports/RotoWire, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-jalen-johnson-questionable-to-suit-up-monday/)
- **Minutes so far:** 23-28 off the bench. RotoWire notes he "hasn't offered much value in other categories" beyond scoring. (unchanged since 2 Nov) [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3042491/aaron-wiggins/fantasy/)
- **Does a return end it?** Johnson's return (no timetable; ESPN est. 4 Nov) ends the start. The report's opening, Gueye, is a big who has not played. No source ties Wiggins's minutes to him. (unchanged since 2 Nov) [Hoops Rumors, 15 Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html)

#### De'Andre Hunter (SAC). L7 33.3 (3) against a season of 22.2, so 5+ above.
- **Role:** starter since the opener, a spot that opened with Ben Simmons's season-ending Achilles tear. RotoWire's expected lineup has him starting Mon at DAL. [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2268641/deandre-hunter/fantasy) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Why L7 is above his average:** more minutes and better scoring. He played 26 and 29 minutes (4 and 7 points) on 23-25 Oct, then 33 (24 points), 37 (24) and 32 (19) in the three games in the L7 window. RotoWire (1 Nov): "He'll continue to operate in an elevated role for as long as Keegan Murray (ankle) is out of action." [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2268641/deandre-hunter/fantasy)
- **Does a return end it?** Murray's return (re-evaluation about 5-9 Nov; ESPN est. 10 Nov) should cut the elevated minutes. His start dates from the Simmons injury, and no source says it ends.

#### Derrick Jones Jr. (LAC). Himself OUT Mon. L7 27.0 (3) against a season of 27.8.
- **Status:** out Mon vs TOR with right knee soreness on the second night of a back-to-back. No diagnosis or timetable has been reported (ESPN est. 4 Nov). The six-week MCL story belongs to an earlier injury (see Part 1, LAC). [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/derrick-jones-jr-knee-out-monday-vs-raptors)
- **Role when back:** he started all six games so far. Max Strus's debut is a new threat to his wing minutes, since RotoWire's expected lineup has Strus at SF Mon. NBC says Keaton Wagler "could start" in Jones's absence. [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php) [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/max-strus-foot-off-the-injury-report-monday)
- **Do returns hurt him?** Ingram (G League stint, no date; ESPN est. 8 Nov) and Beal (no timetable; ESPN est. 8 Nov) are the bigger returns that would shrink his role. [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)

#### P.J. Washington (DAL). L7 27.7 (3) against a season of 27.5.
- **Role:** locked-in starter, and RotoWire's expected lineup has him starting at PF Mon vs SAC. Over his first six games he played 27-41 minutes. No injury. [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php) (game log unchanged since 2 Nov) [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2892549/pj-washington/fantasy)
- **Does a return end it?** No. Aldama's debut (doubtful Mon) could take some frontcourt minutes, but no source says it costs Washington his start.

#### Aday Mara (OKC). L7 27.3 (3) against a season of 19.5, so 5+ above.
- **Role:** bench. RotoWire's expected OKC five Mon at CLE is SGA, McCain, Mitchell, K. Williams and Hartenstein. [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php) Thunder On SI says Mara "is set to step into quite a big role with Chet Holmgren out for 8-10 weeks." Through six games he averaged 5.8 points, 5 rebounds and 1.8 blocks. No Daigneault comment was found. [Thunder On SI (Grayson Buchanan), viewed 2 Nov](https://www.si.com/nba/thunder/onsi/aday-mara-looks-to-pursue-all-rookie-team-with-more-minutes)
- **Why L7 is above his average:** more minutes since Holmgren's knee flared after 25 Oct. He had 11 points and 10 rebounds "in extended action" vs PHX [SI Fantasy, 31 Oct](https://www.si.com/onsi/fantasy/injuries/fantasy-basketball-injury-impact-who-will-benefit-the-most-from-chet-holmgren-s-absence), then 27:43 on 31 Oct at HOU (7 points, 9 rebounds, 3 assists, 4 blocks). (unchanged since 2 Nov) [Yahoo Sports box score, 31 Oct](https://sports.yahoo.com/nba/oklahoma-city-thunder-houston-rockets-2026103110/)
- **Does a return end it?** Holmgren's return (about 25 Dec to 8 Jan; ESPN est. 2 Jan) ends it. Topic, Sorber and Caruso are guards or wings and should not hit his minutes. RotoWire's caveat stands: he needs about 32 minutes to matter in points leagues. (unchanged since 2 Nov) [RotoWire, 31 Oct](https://www.rotowire.com/basketball/article/fantasy-basketball-waiver-wire-oct-31-mara-fears-simons-144777)

#### Jordan Goodwin (PHX). L7 32.0 (2) against a season of 27.2, not 5+ off, and 2 games is noise.
- **Role:** bench combo guard averaging 8.8 points, 3.8 rebounds, 2.8 assists, 2.3 threes and 1.8 steals in 21 minutes. Yahoo's Titus (2 Nov) calls him a "deep cut" stream for Thursday and Saturday and a "top-90 player in 9-cat." [Yahoo Sports (Dan Titus), 2 Nov](https://sports.yahoo.com/fantasy/article/fantasy-basketball-waiver-wire-the-playlist-for-your-week-3-lineup-160632625.html) The newest RotoWire item is from 25 Oct (20 minutes, 3 steals), which expects "a steady bench role." [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2893060/jordan-goodwin)
- **Does a return end it?** No source ties his minutes to an injury. The report's opening, Mark Williams, is a center out until at least February. No coach comment was found.

#### Toumani Camara (POR). L7 28.3 (3) against a season of 31.0, not 5+ off.
- **Role:** entrenched starter. RotoWire: "should remain entrenched as a starter." The expected lineup has him at SF Mon at DEN. Last five games: 23, 27, 24, 26 and 31 minutes, with 3-5 threes in each. The newest item is from 1 Nov (14 points, 4 threes in 31 minutes vs UTA). [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3141429/toumani-camara/) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Does a return end it?** No. His start predates Morant's injury (re-evaluated about 27 Nov). Morant's absence has not visibly raised his usage.

#### Jaxson Hayes (UTAH). L7 27.0 (2) against a season of 32.2, so 5+ below, but **2 games is noise**.
- **Role:** starting center while Nurkic is out. Jazz On SI (2 Nov): "Jaxson Hayes should still be expected to run Utah's starting center role." RotoWire's expected lineup agrees for Mon at SA. [Jazz On SI, 2 Nov](https://www.si.com/nba/jazz/onsi/jazz-injury-report-vs-spurs-latest-intel-as-utah-looks-to-snap-4-game-skid) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Why L7 trails his average:** low scoring and one short night. On 28 Oct he played 37 minutes with 2 points, 11 rebounds and 4 assists, and RotoWire warns that his "limited scoring chances" make production inconsistent. On 31 Oct he played 20 minutes (7 points, 7 rebounds) in a 112-90 loss to Portland. He missed 26 Oct with right shoulder soreness and has been cleared since 28 Oct. No other cause was found. [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3041402/jaxson-hayes/fantasy/)
- **Does a return end it?** **Yes.** Nurkic's return (re-evaluation about 4 Nov) ends the start. Rotoworld tied Hayes's value to Nurkic's absence. (unchanged since 2 Nov) [Deseret News, 31 Oct](https://www.deseret.com/sports/2026/10/31/three-takeaways-from-the-jazzs-halloween-horror-show-against-the-blazers/)

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 08 Nov | 6 | 41.5 | — | 41.5 (2) | 41.5 (2) | 24.7 | 22.5 | Free agent | 14% | 4 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 2 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 4 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 8 | 26.3 | — | 26.3 (3) | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 3 / 3 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 2 | — | — | — | — | 30.3 | 33.3 | Free agent | 42% | 3 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 02 Nov | 0 | — | — | — | — | 25.0 | 32.4 | Free agent | 6% | 4 / 4 |
| **Jakob Poeltl** | TOR | Left Shoulder Inflammation | 02 Nov | 0 | 16.8 | 21.5 (2) | 16.8 (5) | 16.8 (5) | 31.7 | 30.3 | Free agent | 38% | 3 / 4 |
| **Keegan Murray** | SAC | Ankle | 10 Nov | 8 | 12.0 | — | 12.0 (2) | 12.0 (2) | 29.3 | 31.6 | Free agent | 35% | 4 / 3 |
| **Alex Caruso** | OKC | Right Ankle | 04 Nov | 2 | 30.8 | 21.0 (1) | 30.8 (4) | 30.8 (4) | 24.0 | 18.0 | Free agent | 17% | 4 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 02 Nov | 0 | 14.2 | 9.5 (2) | 14.2 (5) | 14.2 (5) | 30.6 | 27.1 | Free agent | 12% | 3 / 4 |
| **Reed Sheppard** | HOU | Back | 02 Nov | 0 | 26.8 | 23.0 (2) | 26.8 (4) | 26.8 (4) | 29.9 | 30.1 | Free agent | 58% | 3 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 06 Nov | 4 | — | — | — | — | 30.1 | 28.0 | Free agent | 45% | 4 / 4 |
| **Egor Demin** | BKN | Right Leg Bruise | 07 Nov | 5 | 15.0 | 8.0 (1) | 15.0 (4) | 15.0 (4) | 30.0 | 22.2 | Free agent | 32% | 4 / 2 |
| **Peyton Watson** | CLE | Right Hamstring Soreness | 02 Nov | 0 | 27.0 | 31.0 (4) | 27.0 (6) | 27.0 (6) | 29.3 | 29.8 | Free agent | 47% | 4 / 4 |
| **Obi Toppin** | IND | Back Soreness | 02 Nov | 0 | 29.0 | 24.5 (2) | 29.0 (5) | 29.0 (5) | 21.9 | 22.4 | Free agent | 12% | 3 / 4 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 04 Nov | 2 | 18.6 | 16.0 (3) | 18.6 (5) | 18.6 (5) | 25.6 | 28.3 | Free agent | 3% | 4 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 8 | — | — | — | — | — | 28.1 | Free agent | 1% | 4 / 3 |
| **Derrick Jones Jr.** | LAC | Right Knee Soreness | 04 Nov | 2 | 27.8 | 27.0 (3) | 27.8 (6) | 27.8 (6) | 21.1 | 24.2 | Free agent | 13% | 3 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 10 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 4 / 4 |
| **Dylan Cardwell** | SAC | Left Calf Strain | 02 Nov | 0 | — | — | — | — | — | 26.6 | Free agent | 0% | 4 / 3 |
| **Jock Landale** | ATL | Left Hip | 04 Nov | 2 | 16.4 | 15.5 (4) | 16.4 (7) | 16.4 (7) | — | 25.8 | Free agent | 1% | 4 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 6 | — | — | — | — | 25.6 | 10.5 | Free agent | 2% | 3 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 09 Nov | 7 | — | — | — | — | 24.4 | 25.5 | Free agent | 8% | 3 / 4 |
| **Al Horford** | GS | Rest | 05 Nov | 3 | 13.8 | 14.8 (4) | 13.8 (6) | 13.8 (6) | 25.1 | 25.1 | Free agent | 1% | 3 / 3 |

### Notes

- **Jusuf Nurkic (UTAH): did not play Monday, officially OUT at SA.** Partial plantar plate tear of the right second toe (4 Oct). The team set re-evaluation at four weeks from 7 Oct, about **4 Nov**. Jazz On SI (2 Nov) says he "still isn't ready to go" but "you'd have to assume that the Jazz will be able to get their veteran big man back relatively soon." No practice report and no minutes limit have been reported. CBS/RotoWire's newest item is from 7 Oct. No return date reported (ESPN est. 4 Nov). The role waiting is the starting center job Hayes holds. [Jazz On SI, 2 Nov](https://www.si.com/nba/jazz/onsi/jazz-injury-report-vs-spurs-latest-intel-as-utah-looks-to-snap-4-game-skid) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [CBS Sports/RotoWire Nurkic page, viewed 2 Nov](https://www.cbssports.com/nba/players/2135553/jusuf-nurkic/fantasy/)
- **Nic Claxton (CHI): did not play Monday, downgraded from doubtful to OUT** at PHI on the 6:00 PM report. He has a left hamstring strain and has missed all six Bulls games. NBC: "While Claxton fully participated in Sunday's practice, he isn't ready to appear in games yet. Jalen Smith will continue to start until that changes." Splitter wanted to see two straight practices. No minutes limit reported, and no timetable reported (ESPN est. 4 Nov). The role waiting is the starting center job. [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/nic-claxton-hamstring-downgraded-to-out-monday) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Yves Missi (NO):** out Mon at MEM with a left knee contusion/bone bruise from a hyperextension on 23 Oct. The team has set no projection. No timetable reported (ESPN est. 8 Nov). (unchanged since 2 Nov) [CBS Sports, 24 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Jalen Suggs (ORL):** mild right knee bone bruise (26 Oct), out at least two weeks with re-evaluation about 9 Nov (ESPN est. 10 Nov). Out Mon vs WSH. FantasyPros (1 Nov) says "another week." No minutes limit reported. (unchanged since 2 Nov) [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html) [FantasyPros, 1 Nov](https://www.fantasypros.com/2026/11/fantasy-basketball-waiver-wire-pickups-advice-week-3-2026/)
- **Santi Aldama (DAL):** doubtful, so he did not return Monday (see Part 1, DAL).
- **Jakob Poeltl (TOR):** questionable Mon (see Part 1, TOR). The role waiting is the starting center job, which Rajakovic confirmed on 30 Oct: "Yak is our starter." [Eurohoops, 30 Oct](https://www.eurohoops.net/en/nba-news/2028242/darko-rajakovic-talks-kawhi-leonard-jakob-poeltl-toronto-raptors-nba/)
- **Keegan Murray (SAC):** out Mon, with re-evaluation about 5-9 Nov (see Part 1, SAC). He takes back the minutes Hunter has been playing.
- **Alex Caruso (OKC):** out Mon (see Part 1, OKC). No return date. With five OKC guards and wings out, a larger bench role is likely when he returns. That is our inference, not a report.
- **Scotty Pippen Jr. (MEM): doubtful** Mon vs NO with low back soreness. No timetable reported (ESPN est. 2 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Reed Sheppard (HOU): questionable** Mon vs BOS with a low back strain. No timetable reported (ESPN est. 2 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Tobias Harris (SA):** out Mon vs UTA with a left calf strain from camp. He has not debuted, and Mitch Johnson is being "very, very methodical." No timetable reported (ESPN est. 6 Nov, likely early). The role waiting could push Harper or Vassell to the bench, per speculation. (unchanged since 2 Nov) [NBC Sports/Rotoworld, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/spurs-taking-very-methodical-approach-to-harris) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Egor Demin (BKN):** right leg bone bruise from 27 Oct, re-evaluation Thu **5 Nov**. He misses through Wed vs CHA. Fernandez: "we're not concerned with anything long term." Out Mon at NYK (ESPN est. 7 Nov). [Yahoo Sports / NY Daily News, 29 Oct](https://sports.yahoo.com/articles/nets-egor-d-min-miss-195100943.html)
- **Peyton Watson (CLE): questionable** Mon vs OKC with right hamstring tightness/soreness. RotoWire still lists him as an expected starter (marked questionable). No timetable reported (ESPN est. 2 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Obi Toppin (IND): downgraded from questionable to OUT** Mon vs ATL with a lumbar sprain. Indiana needed him or Nance active just to reach the eight-player minimum. No timetable reported (ESPN est. 2 Nov). [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Jaylon Tyson (CLE):** right ankle sprain, out Mon for a second straight game. "His next chance to suit up will come Wednesday against the Thunder." No longer timeline reported (ESPN est. 4 Nov). [RotoWire, 1 Nov](https://www.rotowire.com/basketball/headlines/jaylon-tyson-injury-out-again-monday-537104)
- **Maxime Raynaud (SAC):** out Mon, with re-evaluation about 9 Nov (see Part 1, SAC).
- **Derrick Jones Jr. (LAC):** out Mon with no diagnosis (see Part 1, LAC).
- **Dereck Lively II (DAL):** out with no timetable (see Part 1, DAL).
- **Dylan Cardwell (SAC):** doubtful Mon at 6:00 PM after a status flip-flop (see Part 1, SAC). The role waiting is backup center minutes while Raynaud is out. [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/dylan-cardwell-injury-upgraded-to-probable-537214)
- **Jock Landale (ATL):** left hip strain, out (see Part 1, ATL). The role waiting is backup center behind Okongwu.
- **Bradley Beal (LAC):** out with no timetable (see Part 1, LAC).
- **T.J. McConnell (IND):** out Mon with a right hamstring strain. He has not debuted, and CBS/RotoWire's newest headline (2 Nov) is "Remains week-to-week." No timetable reported (ESPN est. 9 Nov). [CBS Sports/RotoWire, McConnell news, viewed 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-another-absence-coming-536374/) [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)
- **Al Horford (GS):** out Mon vs PHX. The official reason is "bilateral low back injury management," while ESPN's feed says Rest. No timetable reported (ESPN est. 5 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 35.4.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dylan Cardwell** | SAC | Left Calf Strain | 02 Nov | 0 | — (—) | 26.6 (44) | Free agent | 0% | 4 / 3 |
| **Santi Aldama** | DAL | Right Knee Surgery | 02 Nov | 0 | 25.0 (23.7) | 32.4 (43) | Free agent | 6% | 4 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 04 Nov | 2 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 4 / 4 |
| **Nic Claxton** | CHI | Hamstring | 04 Nov | 2 | 30.3 (27.8) | 33.3 (69) | Free agent | 42% | 3 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 06 Nov | 4 | 30.1 (30.5) | 28.0 (63) | Free agent | 45% | 4 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 08 Nov | 6 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 3 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 08 Nov | 6 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 65% | 3 / 3 |
| **Kon Knueppel** | CHA | Left Hamstring | 09 Nov | 7 | 35.2 (34.2) | 34.1 (81) | Team Nic Kerr | 90% | 3 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 09 Nov | 7 | 24.4 (17.8) | 25.5 (56) | Free agent | 8% | 3 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 8 | — (—) | 28.1 (74) | Free agent | 1% | 4 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 10 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 4 / 4 |
| **Kristaps Porzingis** | GS | Illness | 01 Dec | 29 | 36.9 (27.7) | 32.3 (32) | Free agent | 41% | 3 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 61 | 38.8 (32.4) | 41.6 (38) | Free agent | 30% | 3 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 93 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 4 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 120 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 4 / 3 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 151 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 4 / 2 |

### Notes

- **Jusuf Nurkic** and **Nic Claxton:** see the notes under *Injured and available, back soon*.
- **Kristaps Porzingis (GS):** officially "Not With Team" Mon. Basketnews (30 Oct), citing unnamed "recent reports," says the Warriors do not expect him to play for them again and are exploring the market, and names POTS as the health issue. Kerr: "things went south" at camp. No timetable reported (ESPN est. 1 Dec). [Basketnews, 30 Oct](https://basketnews.com/news-258546-steve-kerr-calls-out-kristaps-porzingis-as-warriors-absence-continues.html) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Jimmy Butler III (GS):** torn right ACL (19 Jan), surgery in early Feb. "Does not yet have a target date" (29 Sep). On 16 Oct he told ESPN's Slater: "We know. Y'all just find out whenever y'all find out." No timetable reported (ESPN est. 2 Jan). [SF Standard, 29 Sep](https://sfstandard.com/2026/09/29/jimmy-butler-acl-recovery-warriors-timeline/) [Bleacher Report, 16 Oct](https://bleacherreport.com/articles/25512071-jimmy-butler-teases-target-date-return-knee-injury-updates-warriors-contract-talks)
- **Mark Williams (PHX), Shaedon Sharpe (POR) and Donte DiVincenzo (MIN):** see Part 1. All are long-term.
- **Not covered:** Brandon Ingram (Melbourne poopoo) and Kon Knueppel (Team Nic Kerr) are rostered, so they are not pickups. Ingram is in Part 1, LAC.

## Our injured players

- **Paul George** (BOS): Out, Rest; ESPN est. back 04 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 09 Nov.
- **Dejounte Murray** (NO): Out, Personal; ESPN est. back 04 Nov.
- **Anthony Black** (ORL): Out, Rest; ESPN est. back 05 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Left Hip Soreness; ESPN est. back 02 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.


### Notes

- **Paul George:** rest on the second night of a back-to-back. He played 33 minutes on Sunday ([NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)). No timetable reported beyond Monday; *ESPN est.* 4 Nov.
- **Jalen Duren:** no update ([RotoWire DET](https://www.rotowire.com/basketball/news.php?team=DET)). Right hamstring strain, re-evaluated about two weeks after 25 Oct; *ESPN est.* 9 Nov. He is on our bench while Kawhi holds the IR slot.
- **Dejounte Murray:** away after the birth of his son, with his "next opportunity to return" on Wednesday against Utah ([CBS Sports/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-listed-out-monday/)); *ESPN est.* 4 Nov.
- **Anthony Black:** "right ankle injury management" on the second night of a back-to-back, which RotoWire and FSR Orlando call rest ([Athlon via Yardbarker, 2 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_wizards_magic_will_alex_sarr_anthony_black_play/s1_17615_44507641)). No timetable reported beyond Monday; *ESPN est.* 5 Nov.
- **Scottie Barnes:** new left hip tightness, questionable Monday at LAC on a back-to-back. It "doesn't sound overly serious" ([NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/scottie-barnes-hip-questionable-monday-vs-lac)). No timetable reported; *ESPN est.* 2 Nov.
- **Kawhi Leonard:** left knee effusion. Rajakovic says he is "doing well", with the next update on Tue 3 Nov ([Basketnews, 2 Nov](https://basketnews.com/news-258646-kawhi-leonard-injury-update-raptors-coach-offers-promising-news.html)). Haynes: "at least three to four weeks"; *ESPN est.* 23 Nov.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 6 games: 3 game(s) without them, 3 with them.

Also out in those games, so part of the gain is theirs: Nikola Topic (back; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Isaiah Hartenstein | C | 3 | 25.7 | +3.3 | 3 | **35.0** | 22.3 | 35.0 (3) | 28.7 (6) | 28.7 (6) | **us** | 46% |
| Aday Mara | C | 3 | 23.0 | +10.0 | 0 | **27.3** | 11.7 | 27.3 (3) | 19.5 (6) | 19.5 (6) | Free agent | 16% |
| Jared McCain | PG/SG | 3 | 29.0 | +8.7 | 3 | **20.0** | 12.3 | 20.0 (3) | 16.2 (6) | 16.2 (6) | Free agent | 32% |
| Kenrich Williams | SF | 3 | 20.7 | +14.0 | 3 | **16.7** | 7.0 | 16.7 (3) | 11.8 (6) | 11.8 (6) | Free agent | 0% |
| Bennett Stirtz | PG | 3 | 26.3 | +21.7 | 0 | **12.3** | 2.0 | 12.3 (3) | 7.2 (6) | 7.2 (6) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Chet Holmgren:** small right patellar tendon tear, out 8-10 weeks from 30 Oct, so about 25 Dec to 8 Jan. Out Mon at CLE (ESPN est. 2 Jan). [SI Fantasy, 31 Oct](https://www.si.com/onsi/fantasy/injuries/fantasy-basketball-injury-impact-who-will-benefit-the-most-from-chet-holmgren-s-absence) [Yahoo Sports / OKC Thunder Wire, 2 Nov](https://sports.yahoo.com/articles/full-injury-report-mondays-thunder-140157560.html)
- **Jalen Williams:** fractured left fibula and dislocated left ankle (25 Oct), surgery 28 Oct, re-evaluation "before the end of the regular season" (ESPN est. 2 Mar). (unchanged since 2 Nov) [Yahoo Sports, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
- **Cason Wallace:** torn left shoulder labrum, surgery done, re-evaluation before the end of the regular season (ESPN est. 2 Mar). (unchanged since 2 Nov) [Yahoo Sports, 31 Oct](https://sports.yahoo.com/nba/article/thunders-chet-holmgren-will-miss-8-10-weeks-after-undergoing-treatment-on-patellar-tendon-tear-010736245.html)
- **Nikola Topic:** low back surgery, out Mon. He has not played this season, and the Thunder do not release rehab updates. **No timetable reported** (ESPN est. 4 Nov). [Yahoo Sports / OKC Thunder Wire, 2 Nov](https://sports.yahoo.com/articles/full-injury-report-mondays-thunder-140157560.html) [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/) (unchanged since 2 Nov)
- **Thomas Sorber:** right knee (minor arthroscopic procedure in the offseason, after a torn right ACL in Sept 2025). Out Mon. Rotoworld says there is "no concrete return timeline" and treats him as out indefinitely (ESPN est. 4 Nov). [NBC Sports/Rotoworld, Sorber news page, viewed 2 Nov](https://www.nbcsports.com/nba/thomas-sorber/258283/news)
- **Alex Caruso:** right ankle sprain from 26 Oct, out Mon at CLE. No return date reported (ESPN est. 4 Nov). [Yahoo Sports / OKC Thunder Wire, 2 Nov](https://sports.yahoo.com/articles/full-injury-report-mondays-thunder-140157560.html)


### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 01 Dec | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 7 | 32.3 | +3.7 | 7 | **40.6** | 33.7 | 39.8 (4) | 40.6 (7) | 40.6 (7) | **us** | 90% |
| Brandon Williams (day to day, ESPN est. back 02 Nov) | PG/SG | 7 | 17.4 | — | 1 | **20.4** | — | 17.8 (4) | 20.4 (7) | 20.4 (7) | Free agent | 2% |
| Georges Niang | PF | 7 | 19.6 | — | 2 | **13.0** | — | 15.5 (4) | 13.0 (7) | 13.0 (7) | Free agent | 0% |
| Will Richard | SG/SF | 7 | 16.4 | — | 1 | **11.6** | — | 7.5 (4) | 11.6 (7) | 11.6 (7) | Free agent | 0% |
| Gary Payton II | SG | 7 | 13.0 | — | 0 | **10.0** | — | 12.5 (4) | 10.0 (7) | 10.0 (7) | Free agent | 0% |

**Reported timeline (2 Nov morning, not re-checked tonight):** Butler (torn ACL, Jan 2026): no official timeline, the team hopes for early 2027 [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/). Porzingis: out indefinitely with a private health issue and not with the team; there is "an extreme level of pessimism" that he plays for Golden State again [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html). Moody (patellar tendon): a December–January return reported on 16 Oct [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/).


### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Keegan Murray | Ankle | 10 Nov | 34.6 | 12.0 | Free agent |
| Maxime Raynaud | Right Knee Dislocated | 10 Nov | 26.6 | 28.1 | Free agent |
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 6 games: 4 game(s) without them, 2 with them.

Also out in those games, so part of the gain is theirs: Dylan Cardwell (left calf strain; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| De'Andre Hunter | SF/PF | 4 | 32.8 | +10.2 | 4 | **28.0** | 11.0 | 33.3 (3) | 22.2 (6) | 22.2 (6) | Free agent | 8% |
| Jonathan Mogbo | PF | 3 | 20.3 | +12.3 | 0 | **18.3** | -2.0 | 18.5 (2) | 13.2 (4) | 13.2 (4) | Free agent | 0% |
| Emanuel Sharp | SG | 4 | 19.0 | +3.5 | 0 | **4.5** | 10.0 | 4.0 (3) | 6.7 (6) | 6.7 (6) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Keegan Murray:** left ankle capsulitis, out Mon. The 26 Oct timeline was at least 10-14 days with re-evaluation then, which means about 5-9 Nov. No result has been reported (ESPN est. 10 Nov). (unchanged since 2 Nov) [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html) [Yahoo Sports / Kings On SI, 2 Nov](https://sports.yahoo.com/articles/kings-vs-mavericks-injury-report-145905500.html)
- **Maxime Raynaud:** right patellar subluxation (10 Oct), out Mon. He is due to be re-evaluated about two weeks from 26 Oct, so about 9 Nov (ESPN est. 10 Nov). (unchanged since 2 Nov) [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
- **Ben Simmons:** torn right Achilles (18 Oct), surgically repaired 20 Oct, and expected to miss the season (ESPN est. 1 Oct 2027). (unchanged since 2 Nov) [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
- **Dylan Cardwell: still no debut, and his status flip-flopped all day.** Left calf strain, and he has missed all six Kings games. The official status was questionable from 8:30 AM to 1:30 PM, **probable at 2:30 PM**, questionable again from 3:30 to 5:30 PM, and **doubtful at 6:00 PM**. RotoWire (12:58 pm) had him probable and likely to debut. No timetable reported (ESPN est. 2 Nov). [NBA injury report, 2 Nov 2:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_02_30PM.pdf) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [RotoWire, 2 Nov 12:58 pm](https://www.rotowire.com/basketball/headlines/dylan-cardwell-injury-upgraded-to-probable-537214)
- **Zach LaVine (Cream Abdul-Yammar):** questionable Mon with right elbow inflammation/soreness, his first injury designation this season. No timetable reported (ESPN est. 2 Nov). [Yahoo Sports / Kings On SI, 2 Nov](https://sports.yahoo.com/articles/kings-vs-mavericks-injury-report-145905500.html)


### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: T.J. McConnell (right hamstring strain; ESPN est. 09 Nov), Ivica Zubac (left ankle sprain; ESPN est. 09 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Nesmith (out, ESPN est. back 04 Nov) | SG/SF | 3 | 26.0 | +6.0 | 3 | **19.3** | 16.3 | 20.2 (4) | 17.8 (6) | 17.8 (6) | Free agent | 3% |
| Larry Nance Jr. (day to day, ESPN est. back 02 Nov) | PF | 3 | 22.3 | +10.6 | 0 | **18.7** | 6.5 | 16.2 (4) | 11.7 (7) | 11.7 (7) | Free agent | 0% |
| Kobe Brown | PF | 2 | 17.5 | +17.0 | 0 | **12.5** | -0.5 | 8.0 (3) | 6.0 (4) | 6.0 (4) | Free agent | 0% |
| Jalen Slawson | SF | 3 | 16.0 | +7.0 | 0 | **9.3** | 11.3 | 7.8 (4) | 10.3 (6) | 10.3 (6) | Free agent | 0% |

**Reported timeline (2 Nov morning, not re-checked tonight):** Haliburton (mild left hamstring strain): week-to-week, next update about 11 Nov [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/). Sheppard (meniscus repair): out "months" [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months). Furphy (ACL): "middle of the year" [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html). *Also out:* Zubac missed Sunday, his fourth straight game, and a preview lists him out Monday, and McConnell is still out; neither has a timetable reported [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain) [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/).


### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |
| Jalen Suggs | Right Knee | 10 Nov | 33.3 | 26.3 | Free agent |

Last 6 games: 3 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Desmond Bane | SG/SF | 3 | 37.7 | +6.0 | 3 | **37.0** | 21.0 | 37.0 (3) | 29.0 (6) | 29.0 (6) | **us** | 93% |
| Franz Wagner | SF/PF | 3 | 37.7 | +4.7 | 3 | **34.7** | 36.3 | 34.7 (3) | 35.5 (6) | 35.5 (6) | Cream Abdul-Yammar | 90% |
| Jase Richardson | SG | 3 | 24.3 | +9.3 | 3 | **16.0** | 11.0 | 16.0 (3) | 13.5 (6) | 13.5 (6) | Free agent | 0% |
| Jevon Carter | PG | 1 | 22.0 | +9.0 | 0 | **10.0** | 9.0 | 10.0 (1) | 9.5 (2) | 9.5 (2) | Free agent | 0% |

**Reported timeline (2 Nov morning, not re-checked tonight):** Banchero (low-grade right high ankle sprain): four to six weeks from 23 Oct, about 20 Nov to 4 Dec [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html). Suggs (mild right knee bone bruise): re-evaluated about 9 Nov [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html).


### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 7 games: 3 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 3 | 33.3 | +7.1 | 3 | **44.3** | 25.8 | 36.2 (4) | 33.7 (7) | 33.7 (7) | Cream Abdul-Yammar | 72% |
| Jaden McDaniels | SF/PF | 3 | 35.7 | +3.9 | 3 | **39.3** | 36.8 | 37.8 (4) | 37.9 (7) | 37.9 (7) | Melbourne poopoo | 88% |
| Bones Hyland | PG | 3 | 16.7 | +8.7 | 0 | **27.0** | 9.0 | 21.2 (4) | 16.7 (7) | 16.7 (7) | Free agent | 2% |
| Joan Beringer | C | 3 | 24.0 | +9.2 | 1 | **23.0** | 20.2 | 26.5 (4) | 21.6 (7) | 21.6 (7) | Free agent | 2% |
| Jaylen Clark | SG | 3 | 14.7 | +11.0 | 0 | **16.0** | 4.0 | 16.0 (3) | 10.0 (6) | 10.0 (6) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Anthony Edwards (Melbourne poopoo):** right knee arthroscopic debridement on 29 Oct, "expected to miss up to two months" (ESPN est. 21 Dec). Out Mon vs MIL. (unchanged since 2 Nov) [Yahoo Sports (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html)
- **Donte DiVincenzo:** torn right Achilles, surgery 26 Apr, with a return hoped for near the end of the season (ESPN est. 2 Apr). (unchanged since 2 Nov) [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
- **LaMelo Ball (Cream Abdul-Yammar)** has a right wrist contusion and **Terrence Shannon Jr.** a left hip contusion. Both are questionable Mon, with no timetable reported (ESPN est. 2 Nov for both). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Rudy Gobert is back.** He missed 31 Oct with lower back spasms and is off the injury report for Monday, so **Joan Beringer returns to the bench** after his one start (12 points, 6 rebounds in 34 minutes). [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/rudy-gobert-back-removed-from-injury-report)


### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |

Last 5 games: 1 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Toumani Camara | SF/PF | 1 | 31.0 | +6.0 | 1 | **27.0** | 32.5 | 28.3 (3) | 31.0 (5) | 31.0 (5) | Free agent | 42% |
| Scoot Henderson | PG/SG | 1 | 31.0 | +12.0 | 1 | **22.0** | 6.5 | 9.3 (3) | 9.6 (5) | 9.6 (5) | Free agent | 8% |
| Yang Hansen | C | 1 | 13.0 | +4.5 | 0 | **16.0** | 9.5 | 14.5 (2) | 11.7 (3) | 11.7 (3) | Free agent | 0% |
| Vit Krejci | PG | 1 | 24.0 | +15.8 | 0 | **16.0** | 4.0 | 7.0 (3) | 6.4 (5) | 6.4 (5) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Ja Morant:** Grade 2 left hamstring strain, re-evaluation in four weeks from 30 Oct, so about 27 Nov (ESPN est. 1 Dec). Out Mon at DEN. (unchanged since 2 Nov) [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Shaedon Sharpe:** torn right meniscus with surgery in late Aug, re-evaluation in six months (about 27 Feb; ESPN est. 2 Mar). The official report lists "right meniscus surgery." (unchanged since 2 Nov) [SI Trail Blazers On SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)


### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Anthony Gill (back spasms; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 2 | 35.0 | +5.0 | 2 | **30.5** | 29.8 | 28.7 (3) | 29.0 (6) | 29.0 (6) | Snow Time Lakers | 49% |
| Alex Sarr (out, ESPN est. back 04 Nov) | PF/C | 2 | 27.5 | +3.0 | 2 | **25.0** | 27.5 | 27.0 (3) | 26.7 (6) | 26.7 (6) | Team Nic Kerr | 75% |

**Reported timeline (2 Nov morning, not re-checked tonight):** Watkins: out after ACL surgery announced 30 Jul [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary). Champagnie and Tre Johnson: no timetable reported.


### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 6 games: 4 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Immanuel Quickley | PG/SG | 4 | 31.8 | +3.2 | 4 | **34.8** | 35.0 | 36.7 (3) | 34.8 (6) | 34.8 (6) | Cream Abdul-Yammar | 79% |
| Ja'Kobe Walter | SG | 4 | 31.0 | +7.5 | 4 | **31.8** | 28.0 | 26.3 (3) | 30.5 (6) | 30.5 (6) | Lauri Birds | 23% |
| Jamal Shead | PG | 4 | 23.0 | +3.0 | 0 | **25.5** | 11.0 | 30.0 (3) | 20.7 (6) | 20.7 (6) | Free agent | 3% |
| Jamison Battle | SF | 4 | 17.2 | +5.8 | 0 | **13.2** | 17.0 | 15.0 (3) | 14.5 (6) | 14.5 (6) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Kawhi Leonard (ours):** left knee swelling, and the MRI showed no structural damage. He is out Mon at LAC (officially "left knee injury management"). Rajakovic on 29-30 Oct: "Exactly seven days from now, we're going to review where he's at," so about 5-6 Nov. "We don't have an exact date, we don't have an exact timeline." Before Sunday's game he said Leonard is "doing well," with a more detailed update due **Tuesday 3 Nov**. Haynes reports "three to four weeks" (ESPN est. 23 Nov). [Basketnews, 2 Nov](https://basketnews.com/news-258646-kawhi-leonard-injury-update-raptors-coach-offers-promising-news.html) [Eurohoops, 30 Oct](https://www.eurohoops.net/en/nba-news/2028242/darko-rajakovic-talks-kawhi-leonard-jakob-poeltl-toronto-raptors-nba/)
- **Jakob Poeltl:** left shoulder bursitis, a late scratch on 1 Nov, and **questionable** Mon on the 6:00 PM report. RotoWire's expected lineup has him starting. If he sits, Collin Murray-Boyles and Trayce Jackson-Davis get more minutes. No timetable reported (ESPN est. 2 Nov). [RotoWire, 2 Nov 3:06 pm](https://www.rotowire.com/basketball/headlines/jakob-poeltl-injury-iffy-to-play-monday-537219) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Scottie Barnes (ours):** left hip soreness/tightness, **questionable** Mon. No timetable reported (ESPN est. 2 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Nate Bittle:** right foot avulsion fracture, out. No timetable reported (ESPN est. 9 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)


### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |

Last 6 games: 2 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ace Bailey | SF/PF | 2 | 38.5 | +11.2 | 2 | **28.5** | 38.8 | 37.3 (3) | 35.3 (6) | 35.3 (6) | Dr White Slong | 66% |
| Jaxson Hayes | C | 2 | 28.5 | +4.8 | 2 | **27.0** | 35.7 | 27.0 (2) | 32.2 (5) | 32.2 (5) | Free agent | 16% |
| Brice Sensabaugh | SG/SF | 2 | 18.5 | +4.5 | 0 | **22.0** | 13.5 | 19.3 (3) | 16.3 (6) | 16.3 (6) | Free agent | 2% |
| Isaiah Collier | PG | 2 | 22.0 | +5.0 | 0 | **15.0** | 18.0 | 18.0 (3) | 17.0 (6) | 17.0 (6) | Free agent | 3% |
| Josh Okogie | SF | 2 | 21.0 | +8.0 | 0 | **12.0** | 3.3 | 8.3 (3) | 6.8 (5) | 6.8 (5) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Jaren Jackson Jr. (Matt Wright's Foxies):** torn right MCL (26 Oct). The team says at least six weeks, and ESPN sources say six to eight without surgery, about 7-21 Dec (ESPN est. 14 Dec). On 2 Nov he "continues to rehab." (unchanged since 2 Nov) [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/) [Jazz On SI, 2 Nov](https://www.si.com/nba/jazz/onsi/jazz-injury-report-vs-spurs-latest-intel-as-utah-looks-to-snap-4-game-skid)
- **Jusuf Nurkic:** see Part 3. Out Mon at SA.
- **Trey Alexander:** listed out under "G League - Two-Way" on the official report (ESPN: left knee bruise). No timetable reported (ESPN est. 6 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)


### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 4 games: 4 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 4 | 21.0 | — | 0 | **27.2** | — | 32.0 (2) | 27.2 (4) | 27.2 (4) | Free agent | 2% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Mark Williams:** torn left shoulder labrum, repaired 10 Sep. The Suns will set a timetable later, and Gambadoro estimated five months at minimum (ESPN est. 3 Feb). He is out Mon at GSW, and nothing new has been reported. (unchanged since 2 Nov) [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)


### DAL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dereck Lively II | Right Foot Surgery | 12 Nov | 23.6 | 21.3 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Santi Aldama (right knee surgery; ESPN est. 02 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Zaccharie Risacher | SF | 6 | 29.7 | +6.9 | 1 | **32.0** | 20.3 | 33.3 (3) | 32.0 (6) | 32.0 (6) | Snow Time Lakers | 18% |
| Naji Marshall | SF/PF | 3 | 27.7 | +3.5 | 1 | **31.3** | 22.4 | — | 31.3 (3) | 31.3 (3) | Free agent | 11% |
| P.J. Washington | SF/PF | 6 | 33.7 | +4.7 | 6 | **27.5** | 26.9 | 27.7 (3) | 27.5 (6) | 27.5 (6) | Free agent | 24% |
| Marcus Sasser | PG | 6 | 19.2 | +6.1 | 0 | **14.3** | 12.4 | 4.7 (3) | 14.3 (6) | 14.3 (6) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Santi Aldama: did not return Monday.** He is officially **doubtful** for Mon vs SAC on every edition from 8:30 AM to 6:00 PM. RotoWire's lineup page and NBC both list him out. He had arthroscopic right knee surgery on 17 Mar with Memphis, and has not played since 4 Feb or debuted for Dallas. Dusty May: "Santi's very close. He's practiced with the Legends a couple times." No timetable reported. ESPN's 2 Nov estimate is now stale. No minutes limit has been reported. [Yardbarker / Dallas Sports Journal, updated 2 Nov 3:55 PM ET](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/kyrie-irving-knee-doubtful-monday-vs-sac)
- **Dereck Lively II:** out Mon after his third right foot surgery. He has not played since 21 Nov 2025. On 30 Oct May said he is "making major progress" and "looks great" but did not know his timetable. No timetable reported (ESPN est. 12 Nov). No minutes limit has been reported. [Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/) [Yardbarker / DSJ, 2 Nov](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904)
- **Kyrie Irving (Snow Time Lakers): NEW downgrade.** Left knee injury management. He went from questionable to **doubtful** for Monday, and RotoWire's expected lineup lists him out. No timetable reported (ESPN est. 2 Nov). [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/kyrie-irving-knee-doubtful-monday-vs-sac) [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)
- **Tarik Biberovic:** right heel bursitis, out Mon. He has not appeared in an NBA regular-season game. No timetable reported (ESPN est. 12 Nov). [Yardbarker / DSJ, 2 Nov](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904)
- **Sergio de Larrea:** right knee sprain, out Mon. He is "to be reevaluated this week." No date given (ESPN est. 4 Nov). [Yardbarker / DSJ, 2 Nov](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904)
- **Caleb Martin:** available, playing with a splint on his right thumb. [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)


### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 6 games: 6 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 08 Nov), Bradley Beal (right knee inflammation; ESPN est. 08 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 6 | 29.8 | +7.8 | 6 | **36.5** | 20.0 | 29.0 (3) | 36.2 (6) | 36.2 (6) | Dr White Slong | 41% |
| Derrick Jones Jr. (out, ESPN est. back 04 Nov) | SF/PF | 6 | 28.8 | +3.4 | 6 | **27.8** | 21.1 | 27.0 (3) | 27.8 (6) | 27.8 (6) | Free agent | 13% |
| Isaiah Jackson | PF/C | 6 | 21.7 | +3.3 | 6 | **27.7** | 20.6 | 26.0 (3) | 28.0 (6) | 28.0 (6) | Team Nic Kerr | 13% |
| Kobe Sanders | SG | 6 | 23.2 | — | 1 | **20.0** | — | 22.0 (3) | 20.0 (6) | 20.0 (6) | Free agent | 1% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Derrick Jones Jr.: OUT Mon vs TOR. "Right knee soreness" is the only diagnosis given.** He left the 1 Nov game at GSW in the third quarter. The Clippers first appear on the official report at 4:30 PM, with Jones out. **The "MCL sprain, six weeks" claim from 2 Nov appears to be recycled.** The six-week Grade 2 MCL item on Rotoworld's page is Law Murray's report from an earlier injury, his second MCL sprain of a past season, both against Boston. The current 2 Nov item says only "sore knee." No timetable reported (ESPN est. 4 Nov). [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/derrick-jones-jr-knee-out-monday-vs-raptors) [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)
- **Max Strus: NEW, back.** Partial plantar fascia tear in his right foot from the preseason opener. He is **off the injury report** and set to debut Mon after missing six games, following a 5-on-5 practice with San Diego (G League) on Sunday. NBC: "the Clippers may exercise caution with his workload." RotoWire's expected lineup has him starting at SF. [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/max-strus-foot-off-the-injury-report-monday) [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html) [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
- **Brandon Ingram (Melbourne poopoo):** partial Achilles tear (the official report says "right heel surgery"). He was assigned to San Diego (G League) on Sat 31 Oct, has since been recalled, and is out Mon (Law Murray via Hoops Rumors). RotoWire (1 Nov) said he would "likely spend a few days with the G League team." No debut date reported (ESPN est. 8 Nov). [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html) [RotoWire, 1 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-assigned-to-g-league-537060)
- **Bradley Beal:** out Mon with "right knee injury management." As of 25 Oct he was being managed for pain and had not been cleared for 5-on-5. No timetable reported (ESPN est. 8 Nov). [SI Clippers On SI, 25 Oct](https://www.si.com/nba/clippers/onsi/clippers-injury-report-thunder-latest-brandon-ingram-bradley-beal-01m5t411kj1v) (unchanged since 2 Nov) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Rui Hachimura: NEW.** Quadriceps soreness: the official report says left, Hoops Rumors says right. Out Mon. No timetable reported (ESPN est. 4 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)
- **Jordan Miller:** torn left rotator cuff, repaired 26 Aug, with re-evaluation in about six months (late Feb; ESPN est. 2 Mar). (unchanged since 2 Nov) [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
- **Yanic Konan Niederhauser:** right Lisfranc surgery (March), with the hardware removed this offseason. Law Murray "wouldn't be surprised" if he does not play until after Christmas, which the outlet calls informed speculation. No official timetable (ESPN est. 8 Nov). [Yardbarker / Hoops Rumors, 10 Jul](https://www.yardbarker.com/nba/articles/yanic_konan_niederhauser_underwent_follow_up_procedure_on_foot/s1_14822_44046850)


### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 5 games: 5 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Spencer Jones (hamstring; ESPN est. 04 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jamal Murray | PG | 5 | 38.2 | +3.2 | 5 | **47.6** | 43.9 | 54.0 (3) | 47.6 (5) | 47.6 (5) | **us** | 99% |
| Christian Braun | SG/SF | 5 | 36.0 | +8.5 | 5 | **34.6** | 23.1 | 40.3 (3) | 34.6 (5) | 34.6 (5) | Free agent | 35% |
| Trevon Brazile | SF/PF | 5 | 22.8 | — | 1 | **22.0** | — | 19.3 (3) | 22.0 (5) | 22.0 (5) | Free agent | 4% |
| Alpha Diallo (out, ESPN est. back 02 Nov) | SF | 1 | 22.0 | — | 0 | **13.0** | — | — | 13.0 (1) | 13.0 (1) | Free agent | 0% |
| Bryce Hopkins | SF | 4 | 16.5 | — | 2 | **6.5** | — | 9.0 (2) | 6.5 (4) | 6.5 (4) | Free agent | 0% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Julian Strawther:** left knee sprain from the 14 Oct preseason game. On 18 Oct the team said he would be re-evaluated in six weeks, about 29 Nov. He is out Mon vs POR (ESPN est. 29 Nov). No source ties Braun's start to him. (unchanged since 2 Nov) [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Spencer Jones:** listed out for Mon vs POR with "bilateral hamstring injury management." He has not played this season, and NBC (1 Nov) says that "won't change on Monday." No timetable reported (ESPN est. 4 Nov). Rookie Trevon Brazile holds the backup role. [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/spencer-jones-hamstring-remains-out-monday) [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Alpha Diallo:** right wrist sprain, questionable Mon. If he plays it would be his first game since opening night. No timetable reported (ESPN est. 2 Nov). [Nuggets On SI (Logan Struck), 2 Nov](https://www.si.com/nba/nuggets/onsi/nuggets-injury-report-denver-trends-up-for-trail-blazers-game)
- **Context:** Cam Johnson (right ankle sprain) returned to the starting lineup on 30 Oct after missing three games, and he is off the report. [Denver Gazette, 30 Oct](https://gazette.com/2026/10/30/christian-braun-catches-fire-as-nuggets-rally-past-suns-127-120/)


### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 7 games: 7 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 7 | 25.9 | +5.6 | 0 | **28.9** | 19.2 | 25.5 (4) | 28.9 (7) | 28.9 (7) | Waivers | 32% |
| Jock Landale (out, ESPN est. back 04 Nov) | C | 7 | 15.3 | — | 0 | **16.4** | — | 15.5 (4) | 16.4 (7) | 16.4 (7) | Free agent | 1% |

**Reported timeline (2 Nov, pregame reports to 6:00 pm ET):**

- **Jalen Johnson (Snow Time Lakers): NEW, OUT Monday at IND.** Left ankle sprain from the third quarter of the 121-99 loss to New Orleans on 31 Oct. He was questionable on every edition through 5:30 PM and changed to out on the 6:00 PM report. CBS also posted "Ruled out Monday." No timetable reported (ESPN est. 4 Nov). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) [NBA injury report, 2 Nov 4:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_04_30PM.pdf) [CBS Sports/RotoWire, 1 Nov (page viewed 2 Nov)](https://www.cbssports.com/fantasy/basketball/news/hawks-jalen-johnson-questionable-to-suit-up-monday/)
- **Jock Landale:** left hip strain, out Mon. He played only 1:22 against New Orleans on 31 Oct before leaving. No timetable reported (ESPN est. 4 Nov). Asa Newell, Zuby Ejiofor or Lu Dort could cover center minutes. [Yahoo Sports / Gameday Atlanta, 2 Nov](https://sports.yahoo.com/articles/hawks-frontcourt-depth-crumbles-landale-225007268.html)
- **Mouhamed Gueye:** left foot fracture, operated on 14 Jul, with a three-to-four-month reassessment (mid-Oct to mid-Nov). No reassessment result has been reported, and he is out Mon (ESPN est. 20 Nov). (unchanged since 2 Nov) [CBS Sports, 15 Jul](https://www.cbssports.com/fantasy/basketball/news/hawks-mouhamed-gueye-out-3-to-4-months-with-foot-injury/) [Yahoo Sports / Gameday Atlanta, 2 Nov](https://sports.yahoo.com/articles/hawks-frontcourt-depth-crumbles-landale-225007268.html)
- **Henri Veesaar:** right ACL tear, out. No timetable reported (ESPN est. 1 Jul). [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
- **Kingston Flemings:** a one-game suspension for an elbow to Bryce McGowens's head on 31 Oct, served Monday (ESPN est. 4 Nov). [Yahoo Sports / ClutchPoints, 2 Nov](https://sports.yahoo.com/articles/jalen-johnson-playing-tonight-hawks-153329005.html)

## Every injury

All 99 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Jalen Smith | CHI | Day-To-Day | — | — | — | Free agent |
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 333 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 333 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 241 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 151 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 151 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 120 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 120 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 120 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 120 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 115 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 93 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 61 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 61 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 61 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 61 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 49 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 42 | Matt Wright's Foxies |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 31 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 31 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 29 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 01 Dec | 29 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 29 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 27 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 21 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 20 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 18 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 16 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 16 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 11 | Lauri Birds |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 10 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 10 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 8 | Free agent |
| Keegan Murray | SAC | Out | Ankle | 10 Nov | 8 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 8 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 8 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 09 Nov | 7 | Free agent |
| T.J. McConnell | IND | Out | Right Hamstring Strain | 09 Nov | 7 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 09 Nov | 7 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 09 Nov | 7 | — |
| Kon Knueppel | CHA | Out | Left Hamstring | 09 Nov | 7 | Team Nic Kerr |
| Jalen Duren | DET | Out | Right Hamstring Strain | 09 Nov | 7 | **us** |
| Ivica Zubac | IND | Out | Left Ankle Sprain | 09 Nov | 7 | Lauri Birds |
| Grant Williams | CHA | Out | Right Hamstring | 09 Nov | 7 | Free agent |
| Adou Thiero | LAL | Out | Left Knee Inflammation | 09 Nov | 7 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 08 Nov | 6 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 08 Nov | 6 | Free agent |
| Devin Carter | BOS | Out | Illness | 08 Nov | 6 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 08 Nov | 6 | Melbourne poopoo |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 08 Nov | 6 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 07 Nov | 5 | Free agent |
| Tyler Bilodeau | BKN | Out | Right Shoulder Sprain | 06 Nov | 4 | Free agent |
| Trey Alexander | UTAH | Out | Left Knee Bruise | 06 Nov | 4 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 06 Nov | 4 | Free agent |
| Gui Santos | GS | Out | Knee | 05 Nov | 3 | Free agent |
| Anthony Black | ORL | Out | Rest | 05 Nov | 3 | **us** |
| Al Horford | GS | Out | Rest | 05 Nov | 3 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 04 Nov | 2 | Free agent |
| Spencer Jones | DEN | Out | Hamstring | 04 Nov | 2 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 04 Nov | 2 | Free agent |
| Rui Hachimura | LAC | Out | Left Quadriceps Bruise | 04 Nov | 2 | Free agent |
| Paul George | BOS | Out | Rest | 04 Nov | 2 | **us** |
| Pascal Siakam | IND | Out | Rest | 04 Nov | 2 | Matt Wright's Foxies |
| Nikola Topic | OKC | Out | Back | 04 Nov | 2 | Free agent |
| Nic Claxton | CHI | Out | Hamstring | 04 Nov | 2 | Free agent |
| Kingston Flemings | ATL | Suspension | Suspension | 04 Nov | 2 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 04 Nov | 2 | Free agent |
| Jordan Poole | NO | Out | Left Ankle Sprain | 04 Nov | 2 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 04 Nov | 2 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 04 Nov | 2 | Free agent |
| Jalen Johnson | ATL | Day-To-Day | Left Ankle | 04 Nov | 2 | Snow Time Lakers |
| Isaiah Joe | DET | Out | Right Hip Bruise | 04 Nov | 2 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 04 Nov | 2 | Free agent |
| Derrick Jones Jr. | LAC | Out | Right Knee Soreness | 04 Nov | 2 | Free agent |
| Dejounte Murray | NO | Out | Personal | 04 Nov | 2 | **us** |
| Clint Capela | HOU | Out | Right Ankle Sprain | 04 Nov | 2 | Free agent |
| Anthony Gill | WSH | Out | Back Spasms | 04 Nov | 2 | Free agent |
| Andrew Nembhard | IND | Out | Neck | 04 Nov | 2 | Matt Wright's Foxies |
| Alex Sarr | WSH | Out | Left Knee Soreness | 04 Nov | 2 | Team Nic Kerr |
| Alex Caruso | OKC | Out | Right Ankle | 04 Nov | 2 | Free agent |
| Aaron Nesmith | IND | Out | Rest | 04 Nov | 2 | Free agent |
| Zach LaVine | SAC | Day-To-Day | Right Elbow Soreness | 02 Nov | 0 | Cream Abdul-Yammar |
| Terrence Shannon Jr. | MIN | Day-To-Day | Left Hip | 02 Nov | 0 | Free agent |
| Scotty Pippen Jr. | MEM | Day-To-Day | Back Soreness | 02 Nov | 0 | Free agent |
| Scottie Barnes | TOR | Day-To-Day | Left Hip Soreness | 02 Nov | 0 | **us** |
| Santi Aldama | DAL | Out | Right Knee Surgery | 02 Nov | 0 | Free agent |
| Reed Sheppard | HOU | Day-To-Day | Back | 02 Nov | 0 | Free agent |
| Quinten Post | MEM | Day-To-Day | Right Ankle | 02 Nov | 0 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Right Hamstring Soreness | 02 Nov | 0 | Free agent |
| Obi Toppin | IND | Day-To-Day | Back Soreness | 02 Nov | 0 | Free agent |
| Larry Nance Jr. | IND | Day-To-Day | Illness | 02 Nov | 0 | Free agent |
| LaMelo Ball | MIN | Day-To-Day | Right Wrist | 02 Nov | 0 | Cream Abdul-Yammar |
| Kyrie Irving | DAL | Day-To-Day | Left Knee | 02 Nov | 0 | Snow Time Lakers |
| Jose Alvarado | NY | Out | Left Ankle Sprain | 02 Nov | 0 | Free agent |
| Joel Embiid | PHI | Day-To-Day | Right Foot | 02 Nov | 0 | Snow Time Lakers |
| Jakob Poeltl | TOR | Day-To-Day | Left Shoulder Inflammation | 02 Nov | 0 | Free agent |
| Dylan Cardwell | SAC | Out | Left Calf Strain | 02 Nov | 0 | Free agent |
| Brandon Williams | GS | Day-To-Day | Left Quadriceps Bruise | 02 Nov | 0 | Free agent |
| Alpha Diallo | DEN | Out | Right Wrist Sprain | 02 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-02 23:01 UTC.
- News opened 2 Nov 2026 (US) for this run:
  - [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/spencer-jones-hamstring-remains-out-monday)
  - [RotoWire lineups, viewed 2 Nov](https://www.rotowire.com/basketball/nba-lineups.php)
  - [Denver Gazette, 30 Oct](https://gazette.com/2026/10/30/christian-braun-catches-fire-as-nuggets-rally-past-suns-127-120/)
  - [NBC Sports, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/christian-braun-with-31-points-hits-7-3-pointers)
  - [Yardbarker / Dallas Sports Journal, 2 Nov](https://www.yardbarker.com/nba/articles/mavericks_downgrade_kyrie_irving_to_doubtful_clear_naji_marshall_ahead_of_kings_game/s1_17810_44506904)
  - [Dallas Sports Journal, 1 Nov](https://dallassportsjournal.com/kyrie-irving-questionable-mavericks-injury-report-kings/)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/kyrie-irving-knee-doubtful-monday-vs-sac)
  - [Dallas Morning News via Yahoo, 2 Nov](https://sports.yahoo.com/articles/mavericks-october-highs-lows-flagg-011945935.html)
  - [CBS Sports/RotoWire, 1 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-jalen-johnson-questionable-to-suit-up-monday/)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3042491/aaron-wiggins/fantasy/)
  - [Hoops Rumors, 15 Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2268641/deandre-hunter/fantasy)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/derrick-jones-jr-knee-out-monday-vs-raptors)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/max-strus-foot-off-the-injury-report-monday)
  - [Hoops Rumors, 2 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-pacers-strus-clippers-kyrie-sarr-beekman.html)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2892549/pj-washington/fantasy)
  - [Thunder On SI (Grayson Buchanan), viewed 2 Nov](https://www.si.com/nba/thunder/onsi/aday-mara-looks-to-pursue-all-rookie-team-with-more-minutes)
  - [SI Fantasy, 31 Oct](https://www.si.com/onsi/fantasy/injuries/fantasy-basketball-injury-impact-who-will-benefit-the-most-from-chet-holmgren-s-absence)
  - [Yahoo Sports box score, 31 Oct](https://sports.yahoo.com/nba/oklahoma-city-thunder-houston-rockets-2026103110/)
  - [RotoWire, 31 Oct](https://www.rotowire.com/basketball/article/fantasy-basketball-waiver-wire-oct-31-mara-fears-simons-144777)
  - [Yahoo Sports (Dan Titus), 2 Nov](https://sports.yahoo.com/fantasy/article/fantasy-basketball-waiver-wire-the-playlist-for-your-week-3-lineup-160632625.html)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/2893060/jordan-goodwin)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3141429/toumani-camara/)
  - [Jazz On SI, 2 Nov](https://www.si.com/nba/jazz/onsi/jazz-injury-report-vs-spurs-latest-intel-as-utah-looks-to-snap-4-game-skid)
  - [CBS Sports/RotoWire player page, viewed 2 Nov](https://www.cbssports.com/nba/players/3041402/jaxson-hayes/fantasy/)
  - [Deseret News, 31 Oct](https://www.deseret.com/sports/2026/10/31/three-takeaways-from-the-jazzs-halloween-horror-show-against-the-blazers/)
  - [NBA injury report, 2 Nov 6:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)
  - [CBS Sports/RotoWire Nurkic page, viewed 2 Nov](https://www.cbssports.com/nba/players/2135553/jusuf-nurkic/fantasy/)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/nic-claxton-hamstring-downgraded-to-out-monday)
  - [CBS Sports, 24 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-without-timetable-for-return/)
  - [Yahoo Sports, 26 Oct](https://sports.yahoo.com/articles/jalen-suggs-injury-magic-announce-195344477.html)
  - [FantasyPros, 1 Nov](https://www.fantasypros.com/2026/11/fantasy-basketball-waiver-wire-pickups-advice-week-3-2026/)
  - [Eurohoops, 30 Oct](https://www.eurohoops.net/en/nba-news/2028242/darko-rajakovic-talks-kawhi-leonard-jakob-poeltl-toronto-raptors-nba/)
  - [NBC Sports/Rotoworld, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/spurs-taking-very-methodical-approach-to-harris)
  - [Yahoo Sports / NY Daily News, 29 Oct](https://sports.yahoo.com/articles/nets-egor-d-min-miss-195100943.html)
  - [RotoWire, 1 Nov](https://www.rotowire.com/basketball/headlines/jaylon-tyson-injury-out-again-monday-537104)
  - [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/dylan-cardwell-injury-upgraded-to-probable-537214)
  - [CBS Sports/RotoWire, McConnell news, viewed 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-another-absence-coming-536374/)
  - [Basketnews, 30 Oct](https://basketnews.com/news-258546-steve-kerr-calls-out-kristaps-porzingis-as-warriors-absence-continues.html)
  - [SF Standard, 29 Sep](https://sfstandard.com/2026/09/29/jimmy-butler-acl-recovery-warriors-timeline/)
  - [Bleacher Report, 16 Oct](https://bleacherreport.com/articles/25512071-jimmy-butler-teases-target-date-return-knee-injury-updates-warriors-contract-talks)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)
  - [RotoWire DET](https://www.rotowire.com/basketball/news.php?team=DET)
  - [CBS Sports/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-listed-out-monday/)
  - [Athlon via Yardbarker, 2 Nov](https://www.yardbarker.com/nba/articles/final_injury_report_for_wizards_magic_will_alex_sarr_anthony_black_play/s1_17615_44507641)
  - [NBC Sports/Rotoworld, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/scottie-barnes-hip-questionable-monday-vs-lac)
  - [Basketnews, 2 Nov](https://basketnews.com/news-258646-kawhi-leonard-injury-update-raptors-coach-offers-promising-news.html)
  - [Yahoo Sports / OKC Thunder Wire, 2 Nov](https://sports.yahoo.com/articles/full-injury-report-mondays-thunder-140157560.html)
  - [Yahoo Sports, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
  - [Yahoo Sports, 31 Oct](https://sports.yahoo.com/nba/article/thunders-chet-holmgren-will-miss-8-10-weeks-after-undergoing-treatment-on-patellar-tendon-tear-010736245.html)
  - [CBS Sports, 27 Oct](https://www.cbssports.com/fantasy/basketball/news/thunders-nikola-topic-wont-play-wednesday/)
  - [NBC Sports/Rotoworld, Sorber news page, viewed 2 Nov](https://www.nbcsports.com/nba/thomas-sorber/258283/news)
  - [CBS Sports, 2 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-jimmy-butler-still-months-away-from-returning/)
  - [Basketnews, 28 Oct](https://basketnews.com/news-258337-warriors-reportedly-extremely-pessimistic-on-porzingis-playing-for-them-again.html)
  - [CBS Sports, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)
  - [Hoops Rumors, 26 Oct](https://www.hoopsrumors.com/2026/10/kings-announce-injury-updates-on-murray-raynaud-cardwell.html)
  - [Yahoo Sports / Kings On SI, 2 Nov](https://sports.yahoo.com/articles/kings-vs-mavericks-injury-report-145905500.html)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
  - [NBA injury report, 2 Nov 2:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_02_30PM.pdf)
  - [Hoops Wire, 28 Oct](https://hoopswire.com/pacers-tyrese-haliburton-unlikely-to-return-before-two-week-injury-update/)
  - [NBC Sports, 28 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/carlisle-ben-sheppard-knee-out-for-months)
  - [Yahoo Sports, 25 Sep](https://sports.yahoo.com/articles/pacers-johnny-furphy-hit-benchmarks-083112900.html)
  - [CBS Sports, 29 Oct](https://cbssports.com/fantasy/basketball/news/pacers-ivica-zubac-still-out-with-ankle-sprain)
  - [Heat Nation, 29 Oct](https://heatnation.com/team-news/heat-vs-pacers-injury-report-haliburton-zubac-out-for-nba-cup-opener/)
  - [Yahoo Sports, 24 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-paolo-banchero-suffers-high-ankle-sprain-in-loss-to-timberwolves-reportedly-could-be-out-4-6-weeks-173753794.html)
  - [Yahoo Sports (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html)
  - [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
  - [NBC Sports/Rotoworld, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/rudy-gobert-back-removed-from-injury-report)
  - [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain)
  - [SI Trail Blazers On SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)
  - [ESPN](https://www.espn.com/nba/team/injuries/_/name/was/salary)
  - [RotoWire, 2 Nov 3:06 pm](https://www.rotowire.com/basketball/headlines/jakob-poeltl-injury-iffy-to-play-monday-537219)
  - [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
  - [Yahoo Sports, 26 Sep](https://sports.yahoo.com/articles/phoenix-suns-mark-williams-injury-152918092.html)
  - [Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/)
  - [RotoWire, 1 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-assigned-to-g-league-537060)
  - [SI Clippers On SI, 25 Oct](https://www.si.com/nba/clippers/onsi/clippers-injury-report-thunder-latest-brandon-ingram-bradley-beal-01m5t411kj1v)
  - [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
  - [Yardbarker / Hoops Rumors, 10 Jul](https://www.yardbarker.com/nba/articles/yanic_konan_niederhauser_underwent_follow_up_procedure_on_foot/s1_14822_44046850)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain)
  - [Nuggets On SI (Logan Struck), 2 Nov](https://www.si.com/nba/nuggets/onsi/nuggets-injury-report-denver-trends-up-for-trail-blazers-game)
  - [NBA injury report, 2 Nov 4:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_04_30PM.pdf)
  - [Yahoo Sports / Gameday Atlanta, 2 Nov](https://sports.yahoo.com/articles/hawks-frontcourt-depth-crumbles-landale-225007268.html)
  - [CBS Sports, 15 Jul](https://www.cbssports.com/fantasy/basketball/news/hawks-mouhamed-gueye-out-3-to-4-months-with-foot-injury/)
  - [Yahoo Sports / ClutchPoints, 2 Nov](https://sports.yahoo.com/articles/jalen-johnson-playing-tonight-hawks-153329005.html)
