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

## Shortlist

These five pickups should hold their roles through Sun 29 Nov. Wednesday 25 Nov games are final, and no NBA team plays Thu 26. We have open lineup slots on Fri (1), Sat (6) and Sun (1). Saturday has only five games: ORL@WSH, BKN@CHA, IND@CHI, OKC@MIL and PHI@HOU ([ESPN scoreboard, 28 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261128)). The shortlist therefore has two Fri+Sun options (take one, for the single Fri and Sun slots) and three Saturday players.

The add deadlines (each US day's first tip-off, Melbourne time) are: Fri 27 by **Sat 28 Nov 11:00 AM** (MIA@NY), Sat 28 by **Sun 29 Nov 9:00 AM** (ORL@WSH) and Sun 29 by **Mon 30 Nov 7:30 AM** (MIA@CLE) ([ESPN scoreboard, 27 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261127); [29 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261129)). Take adds left from `matchup.py`.

The Rates come from `council/form.py` (26 Nov 06:16 UTC). Our five-lowest floor is **31.1**. Wednesday's statuses come from the [NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf). At 1:15 AM ET on 26 Nov, no team had submitted its Friday report yet ([NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf)).

- **Jakob Poeltl** (TOR, C, free agent, 37%): Fri + Sun.
  - **Opening:**
    - Kawhi Leonard (us) is out "at least another week" from 24 Nov, with the next update in a week ([CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/); [NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week)); *ESPN est.* 3 Dec.
    - RJ Barrett will be re-evaluated about 3 Dec ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks)); *ESPN est.* 13 Dec.
  - **Window:** both absentees are out all week.
  - **Role:** the starting C since Barrett's injury, with starts on 18, 20 and 23 Nov ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
    - **Risk (unchanged):** Rotoworld thinks the days off "may be enough time to get Murray-Boyles back into the starting lineup" ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)).
    - TOR has not played since 23 Nov, and no lineup news has come out since.
  - **Numbers:** FP/g without the absentees 38.7 (3 g, 29.7 min). Season 27.4 (15), L7 38.7 (3), L15 27.9 (7), L30 30.8 (12). **Rate 32.2**, the best here; ESPN proj. 31.7. Minutes 24.2 for the season, 29.7 over L7. ([Injury Watch, 26 Nov](20261126-injury-watch.md); Rate from `form.py`, 26 Nov)
  - **L7 +11.3:** minutes, from the three starts. The L7 is those 3 games.
  - **Games:** 2 (Fri vs BKN, Sun vs DEN). For Friday, add by Sat 28 Nov 11:00 AM Melbourne.
- **Charles Bassey** (GS, C, free agent, 7%): Fri + Sun, the alternative to Poeltl.
  - **Opening:**
    - Stephen Curry will be re-evaluated Fri 27 Nov ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-stephen-curry-to-be-re-evaluated-friday/)). A re-evaluation is not a return date; *ESPN est.* 12 Dec.
    - Kristaps Porzingis is "Not With Team" ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)); no timetable reported; *ESPN est.* 2 Jan.
  - **Window:** both are out past Sunday.
  - **Role:** Kerr on keeping Bassey with the starters: "can't predict how long, but hopefully for the season" ([Yahoo, 24 Nov](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html)).
    - He started again Wed vs SAC: 10 pts, 7 reb and 2 blk in 22 min. Horford came off the bench for 13 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)).
    - Yaxel Lendeborg (us) played Wednesday after all, so Bassey's start did not depend on him.
  - **Numbers:** FP/g without the absentees 27.7 (6 g, 21.8 min). Season 23.3 (16), L7 35.2 (4), L15 26.7 (7), L30 23.0 (15). Rate 27.8; **role rate 33.5 ‡** (news override, 24 min until 8 Dec, in force). ESPN proj. 14.5. Minutes 16.0 for the season, 23.8 over L7. ([Injury Watch, 26 Nov](20261126-injury-watch.md); Rate from `form.py`, 26 Nov)
  - **L7 +11.9:** minutes, from his starts on 18, 19, 22 and 25 Nov.
  - **Games:** 2 (Fri @POR, Sun vs LAC). For Friday, add by Sat 28 Nov 11:00 AM Melbourne.
- **Buddy Hield** (CHI, SG/SF, free agent, 7%): Sat.
  - **Opening:**
    - Caleb Wilson (right metacarpal fracture): next update about 3 Dec ([Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20)); *ESPN est.* 13 Dec.
    - Norman Powell was out Wed, his third straight absence ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)). The Bulls said only that he "will be re-evaluated later this week" ([Bulls.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)). No result has been reported; *ESPN est.* 28 Nov, which is Saturday.
  - **Window:** Wilson's absence keeps Hield's bench minutes going past Sunday. The start lasts until Powell is back.
  - **Role:** he started Wed at CHA in Powell's place, beside Giddey, Okoro, Buzelis and Claxton ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/bulls-start-giddey-hield-okoro-buzelis-claxton)). He had 9 pts, 4 reb, 4 ast and 3-6 3PT in 27 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - **Numbers:** FP/g without Wilson 29.8 (8 g, 25.0 min). Season 21.2 (16), L7 33.0 (5), L15 29.8 (8), L30 23.0 (13). Rate 27.4; ESPN proj. 16.9. Minutes 19.0 for the season, 27.2 over L7. ([Injury Watch, 26 Nov](20261126-injury-watch.md); Rate from `form.py`, 26 Nov)
  - **L7 +11.8:** minutes, from starts on 22, 23 and 25 Nov ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032); [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041); [25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - **Games:** 1 (Sat vs IND). Add by Sun 29 Nov 9:00 AM Melbourne. Powell's Saturday status should be on CHI's official report before then.
- **Kenrich Williams** (OKC, SF, free agent, 4%): Sat.
  - **Opening:**
    - Jalen Williams and Cason Wallace have no timeline, and it is "unlikely either of them plays again this season" ([NBC Sports, 2 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-news-injury-updates-nov-2-injuries-hit-jalen-williams-cason-wallace-chet-holmgren-in-okc)); *ESPN est.* 2 Mar for both.
    - Chet Holmgren: 8–10 weeks from 30 Oct (same article); *ESPN est.* 2 Jan.
    - Aday Mara (shin contusion) and Jaylin Williams (back spasms) were out Wed. RotoWire says it is "unclear when he will be available" (Jaylin Williams), and Kenrich "should... see more action" with both out ([RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jaylin-williams-injury-still-out-wednesday-540874)). No timetable reported for Mara; *ESPN est.* 28 Nov for both.
  - **Window:** the long absences last all season. The extra small-ball minutes shrink when Mara or Jaylin Williams returns, possibly at Saturday's game.
  - **Role:** a bench forward since Shai Gilgeous-Alexander returned ([CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-kenrich-williams-headed-to-bench-540713/); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/kenrich-williams-scores-20-points-off-bench)).
    - 20 pts and 9 reb in 26 min on 23 Nov ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038)).
    - 13 pts, 5 reb and 3 stl in 25 min Wed vs MIN ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320)).
  - **Numbers:** FP/g without the absentees 27.4 (10 g, 25.0 min). Season 21.3 (19), L7 33.8 (5), L15 28.3 (9), L30 23.9 (16). Rate 27.4; ESPN proj. 14.2. Minutes 21.6 for the season, 25.6 over L7. ([Injury Watch, 26 Nov](20261126-injury-watch.md); Rate from `form.py`, 26 Nov)
  - **L7 +12.5:** minutes, and a 20-point game on 23 Nov (box above).
  - **Games:** 1 (Sat @MIL). Add by Sun 29 Nov 9:00 AM Melbourne.
- **Coby White** (CHA, PG/SG, free agent, 60%): Sat.
  - **Opening:**
    - Dennis Schroder is out indefinitely, possibly until mid-December ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-dennis-schroder-remains-out-indefinitely/)); *ESPN est.* 12 Dec.
    - Kon Knueppel is out at least four weeks from 8 Nov ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/)); *ESPN est.* 12 Dec.
    - Grayson Allen missed Wednesday, his fourth straight game in the concussion protocol ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf); [FantasyPros, 25 Nov](https://www.fantasypros.com/nba/news/622560/grayson-allen-concussion-ruled-out-wednesday.php)). No timetable reported; *ESPN est.* 28 Nov.
  - **Window:** Schroder and Knueppel are out past Sunday.
  - **Role:** he started Wed vs CHI: 11 pts (3-13 FG), 5 reb and 6 ast in 25 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)). He played 28 min with 21 pts on 23 Nov ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036)).
    - He has been on a minutes limit since his 2 Nov debut ([Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html)). No report says it has been lifted.
  - **Numbers:** FP/g without the absentees 24.0 (8 g, 22.6 min). Season 20.3 (10), L7 30.3 (3), L15 28.7 (6), L30 20.3 (10). L30 equals the season, as he debuted on 2 Nov. Rate 26.3; ESPN proj. 32.9. Minutes 21.5 for the season, 26.3 over L7. ([Injury Watch, 26 Nov](20261126-injury-watch.md); Rate from `form.py`, 26 Nov)
  - **L7 +10.0:** minutes rising under the limit (28 and 25 min in his last two) and the 21-point game on 23 Nov.
  - **Games:** 1 (Sat vs BKN). Add by Sun 29 Nov 9:00 AM Melbourne.

Not shortlisted:
- **Norman Powell** (CHI, Rate 32.2): the best Saturday add if CHI clears him, but nothing points that way yet.
  - **Status:** no re-evaluation result has been reported ([Bulls.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)). *ESPN est.* 28 Nov.
  - **Form:** L7 28.0 (2), **small sample**.
  - **Cost:** his return ends Hield's start.
- **Grayson Allen** (CHA, Rate 27.4, role rate 29.7, not applied): add for Saturday only if he is cleared. He is still in the protocol after four missed games (see Coby White).
  - **Form:** L15 27.5 (2), **small sample**.
- **De'Andre Hunter** (SAC, Rate 32.2): plays only Sun vs MIN, where Poeltl or Bassey takes our single open slot.
  - **Raynaud risk:** Maxime Raynaud practiced fully with Stockton on Wednesday, "including 5v5" ([Kings On SI via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/kings-maxime-raynaud-gets-promising-230723065.html)). He has no timetable and is week-to-week ([RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/maxime-raynaud-injury-recalled-to-nba-540983)); *ESPN est.* 2 Dec.
  - **Opening:** Ben Simmons is out for the season ([AP via NY1, 18 Oct](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/18/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice)); *ESPN est.* 1 Oct, a stale date.
  - **Wednesday:** 15 pts and 7 reb in 39 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)).
- **Christian Anderson** (CHA, Rate 24.1): the next Saturday option.
  - **Form:** L7 30.7 (3) against a season of 14.1 (+16.6), from minutes: 25 pts in 25 min on 23 Nov and 15 pts in 28 min Wed ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036); [25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - **Opening:** the same as White's.
- **Nic Claxton** (CHI, Rate 25.4): he started Wed only because Jalen Smith (us) was out ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/bulls-start-giddey-hield-okoro-buzelis-claxton)). See Smith under Absentees.
- **Kelly Oubre Jr.** (IND, Rate 28.6; Fri + Sat): outside the injury angle, as he started on 22 Nov with Nesmith playing ([ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034)). He is the strongest Fri+Sat player found here, and the matchup's stream list should weigh him.
- **Daniss Jenkins** (DET, Rate 30.4; role rate 36.7 ‡, override until 27 Nov): the hedge if Cade Cunningham (us) sits. He plays only Fri and Sun, where Poeltl or Bassey fills our single slot.
- **Noah Clowney** (BKN, Rate 20.2) and **Jalen Slawson** (IND, Rate 24.9): Fri+Sat, but low rates. Clowney had 17 pts in 27 min Wed after Moritz Wagner left with knee soreness (see Absentees).
- **Tristan da Silva** (ORL, Rate 22.2): Sat+Sun, about 30 min while Paolo Banchero is out (see Back soon). Low rate.
- **Ja'Kobe Walter** (Rate 26.6) and **Allen Graves** (Rate 22.5): Fri+Sun, below Poeltl and Bassey.

## Research

New since 25 Nov. Notes in [20261125-injury-watch.md](20261125-injury-watch.md) still hold where this says "unchanged". Wednesday 25 Nov games are final. The official reports cited are [NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf) (Wednesday's final statuses) and [NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf) (Friday's games, all "not yet submitted"). No Thursday team news had come out at the time of writing (about 1:30 AM ET, 26 Nov).

**Absentees**

- **Cade Cunningham (us, DET):** Day-to-day with right knee soreness, after the late scratch Tue at ORL. Bickerstaff says he is "far less than 100 percent". It is the second time this season the knee has cost him a game ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)). DET did not play Wednesday.
  - **Timeline:** no timetable reported. *ESPN est.* 27 Nov, so Fri vs MIL would be his next game. DET then plays Sun vs ORL.
  - Daniss Jenkins started in his place Tuesday: 15 pts and 10 ast in 35 min ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)).
- **Jalen Duren (us, DET):** **Changed.** He practiced with the G League Motor City Cruise on Wednesday and "seems close to returning". Bickerstaff: "We're looking forward to getting him back" ([Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html)).
  - **Timeline:** the Pistons "haven't provided a return timeline" ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-practicing-in-g-league/)), so no timetable reported. *ESPN est.* 30 Nov, which would mean missing Fri and Sun. Watch DET's Friday report.
- **Kawhi Leonard (us, IR, TOR):** Unchanged since 24 Nov. He has begun on-court workouts but is out "at least another week", with the next update in a week ([CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/); [NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week)).
  - **Timeline:** not before about 1 Dec. *ESPN est.* 3 Dec. He misses all of this week.
- **Jalen Smith (us, CHI):** **Changed.** He was downgraded from questionable to **out** Wed at CHA with a gastrointestinal illness ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jalen-smith-illness-downgraded-to-out-wednesday); [NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)). Nic Claxton started in his place.
  - **Timeline:** no timetable reported. *ESPN est.* 28 Nov, which is CHI's only remaining game this week (Sat vs IND).
- **Yaxel Lendeborg (us, GS):** **Back.** Listed available ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)), he started Wed vs SAC: 15 pts, 8 reb, 3 stl and 1 blk in 31 min ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)). He is out of ESPN's injury feed. GS plays Fri @POR and Sun vs LAC.
- **Norman Powell (CHI, free agent):** Out Wed at CHA, his third straight absence ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)). On 22 Nov SI noted that a re-evaluation "does not guarantee Powell will get the green light to return later this week or next week" ([Bulls On SI, 22 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-update-bad-news-on-norman-powell-jalen-smith-still-questionable-22)). No result has been reported.
  - **Timeline:** no timetable reported. *ESPN est.* 28 Nov, so at most 1 game (Sat vs IND).
  - **Form:** season 30.1 (13) → 32.2 (12), L7 28.0 (2) (**small sample**), L15 36.2 (5), L30 30.7 (10) → 33.7 (9). Rate 32.2.
- **Grayson Allen (CHA, free agent):** **Changed.** He was ruled out Wed vs CHI, his fourth straight game in the concussion protocol ([FantasyPros, 25 Nov](https://www.fantasypros.com/nba/news/622560/grayson-allen-concussion-ruled-out-wednesday.php); [NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)).
  - **Timeline:** no timetable reported. *ESPN est.* 28 Nov (was 25 Nov). CHA plays only Sat vs BKN.
  - **Form:** season 26.8 (13), no L7 (injured), L15 27.5 (2) (**small sample**), L30 26.3 (10). Rate 27.4.
- **Stephen Curry (GS):** Unchanged. He is to be re-evaluated Fri 27 Nov, with updates "following the holiday" ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-stephen-curry-to-be-re-evaluated-friday/); [Yardbarker/Ball Exclusives, 25 Nov](https://www.yardbarker.com/nba/articles/warriors_stephen_curry_to_be_re_evaluated_friday_for_oblique_tear/s1_17668_44615539)). A re-evaluation is not a return date. *ESPN est.* 12 Dec.
- **Maxime Raynaud (SAC):** **Changed.** He practiced with Stockton on Wednesday: "He was a full participant, including 5v5", and "continues to make progress towards his return" ([Kings On SI via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/kings-maxime-raynaud-gets-promising-230723065.html)). He was then recalled.
  - **Timeline:** no timetable, week-to-week ([RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/maxime-raynaud-injury-recalled-to-nba-540983)). *ESPN est.* 2 Dec. His return is the risk to Hunter's minutes, and Sunday vs MIN is SAC's only game left this week.
- **Zach Edey (MEM, free agent):** **New.** He left Wed vs LAC in the second quarter with left ankle soreness (7 pts, 4 reb, 2 blk in 9 min). CBS/RotoWire calls him "at least questionable" for Fri at MIN, and notes he has had two procedures on that ankle since June 2025 ([CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-does-not-return-wednesday/); [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909321)).
  - **Timeline:** no timetable reported. *ESPN est.* 27 Nov.
  - **Pickup angle:** if he sits, Isaiah Stewart (Rate 21.6) and Taylor Hendricks (Rate 19.0) gain minutes (same CBS note). Both rates are too low to matter. Edey's own Rate is 25.7.
- **Moritz Wagner (BKN):** **New.** He left Wed at MIL after 4 min with left knee soreness ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/moritz-wagner-knee-will-not-return-wednesday)).
  - **Timeline:** no timetable reported. *ESPN est.* 27 Nov.
  - Noah Clowney played 27 min off the bench with 17 pts, and Day'Ron Sharpe (rostered) had 11 pts and 14 reb ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322)).
- **Jaylen Brown (PHI):** **New.** He left Wed vs MIA with soreness in the same left hamstring that cost him two games last week. He "will receive imaging, with an update to come on Thursday", and Dean Wade would likely start if he misses time ([NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jaylen-brown-hamstring-to-receive-imaging)).
  - **Timeline:** no timetable reported until the imaging. *ESPN est.* 27 Nov.
  - **Pickup angle:** PHI's Fri–Sat back-to-back is a risk for Brown even if he is cleared. Wade is no pickup: Rate 15.7, L7 7.0 (2) (**small sample**).
- **Aday Mara and Jaylin Williams (OKC):** Both were out Wed vs MIN ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)). It is "unclear when [Jaylin Williams] will be available to return" ([RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jaylin-williams-injury-still-out-wednesday-540874)).
  - **Timeline:** no timetable reported for either. *ESPN est.* 28 Nov for both (OKC plays Sat @MIL).
  - Their return would trim Kenrich Williams's small-ball minutes.
- **Duncan Robinson (DET, free agent):** Unchanged since 24 Nov. Day-to-day, "progressing in his rehabilitation" ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/duncan-robinson-quad-considered-day-to-day)). DET has not played since, and no practice report was found.
  - **Timeline:** no timetable reported. *ESPN est.* 27 Nov.
  - **Form:** season 29.8 (12), no L7 (injured), L15 16.0 (2) (**small sample**), L30 29.7 (9). Rate 23.6.

**Pickups for us**

- **Jakob Poeltl (TOR, 2 games: Fri, Sun):** See the shortlist. TOR has not played since 23 Nov, so nothing has changed.
  - **Form:** L7 38.7 (3) against a season of 27.4, +11.3.
  - **Why:** minutes, 24.2 for the season and 29.7 over L7, from starts on 18, 20 and 23 Nov ([ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012); [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308); [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)).
  - **Ends:** not with Leonard's return (*ESPN est.* 3 Dec) or Barrett's (*ESPN est.* 13 Dec), both after this week. Murray-Boyles rejoining the lineup is the risk ([NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes)).
- **Charles Bassey (GS, 2 games: Fri, Sun):** **Changed.** He started again Wed (22 min, 10 pts, 7 reb, 2 blk; [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)). Kerr hopes the lineup lasts "for the season" ([Yahoo, 24 Nov](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html)).
  - **Form:** L7 35.2 (4) against a season of 23.3, +11.9.
  - **Why:** minutes, 16.0 for the season and 23.8 over L7.
  - **Ends:** Porzingis's return (*ESPN est.* 2 Jan), or a change of heart by Kerr. Curry's Friday re-evaluation is no return date (*ESPN est.* 12 Dec).
  - **Rate:** 27.8, role rate 33.5 ‡.
- **Buddy Hield (CHI, 1 game: Sat):** **Changed.** He started Wed at CHA (27 min, 9 pts, 3-6 3PT; [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - **Form:** L7 33.0 (5) against a season of 21.2, +11.8.
  - **Why:** minutes, 19.0 for the season and 27.2 over L7, from three starts in Powell's place.
  - **Ends:** the start ends with Powell's return (*ESPN est.* 28 Nov). The bench role lasts until Wilson's (*ESPN est.* 13 Dec).
- **Kenrich Williams (OKC, 1 game: Sat):** **New to the shortlist.** He played 25–26 min off the bench in each of his last two games ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038); [25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320)).
  - **Form:** L7 33.8 (5) against a season of 21.3, +12.5.
  - **Why:** minutes, 21.6 for the season and 25.6 over L7, plus a 20-pt, 9-reb game on 23 Nov.
  - **Ends:** the long OKC absences outlast the season ([NBC Sports, 2 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-news-injury-updates-nov-2-injuries-hit-jalen-williams-cason-wallace-chet-holmgren-in-okc)). The small-ball bump ends when Mara or Jaylin Williams returns (*ESPN est.* 28 Nov for both).
- **Coby White (CHA, 1 game: Sat):** **New to the shortlist.** He started his last two games, at 28 and 25 min ([ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036); [25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318)).
  - **Form:** L7 30.3 (3) against a season of 20.3, +10.0.
  - **Why:** minutes, rising under the limit in place since 2 Nov ([Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html)).
  - **Ends:** with Schroder's or Knueppel's return (*ESPN est.* 12 Dec for both). If Allen is cleared, he takes a guard start but not White's role.
- **Christian Anderson (CHA, 1 game: Sat):** 25 pts (6-8 3PT) in 25 min on 23 Nov, then 15 pts in 28 min Wed, both off the bench (same box scores).
  - **Form:** season 14.1 (16), L7 30.7 (3), L15 26.3 (6), L30 16.8 (13), +16.6.
  - **Why:** minutes (15.5 for the season, 24.7 over L7) and the hot shooting. Rate 24.1.
- **De'Andre Hunter (SAC, 1 game: Sun):** 15 pts and 7 reb in 39 min Wed ([ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324)).
  - **Form:** L7 36.0 (5) against a season of 26.1, +9.9.
  - **Why:** minutes, 34.2 for the season and 38.0 over L7.
  - **Ends:** Raynaud's return (above) is closer after Wednesday's full practice. Rate 32.2.
- **Noah Clowney (BKN, 2 games: Fri @TOR, Sat @CHA):** 17 pts in 27 min Wed (box above). His 29.3 FP/g without Nolan Traoré rests on 3 games.
  - **Traoré:** re-evaluation in 8–10 weeks ([NY Post via Yahoo, 23 Nov](https://sports.yahoo.com/articles/nets-gets-crushing-injury-nolan-180410690.html)); *ESPN est.* 27 Jan.
  - **Form:** season 17.2 (17), L7 18.8 (4), L15 24.4 (7), L30 18.0 (14). L7 is within 5 of the season. Rate 20.2.
- **Tristan da Silva (ORL, 2 games: Sat @WSH, Sun @DET):** 33 min and 16 pts Tue vs DET ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)).
  - **Opening:** Paolo Banchero hoped to be back "within the next couple of weeks", so about 3 Dec ([Heavy via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-bachero-reveals-190941314.html)); *ESPN est.* 29 Nov.
  - **Form:** season 24.6 (15), L7 19.8 (4), L15 22.7 (6), L30 24.2 (12). L7 is within 5 of the season. Rate 22.2.

**Back soon**

- **Ja Morant (POR):** **Changed.** Nori said Wednesday: "He's starting to participate a little bit in the 5-on-5 stuff... I'll go out on a limb and say we'll see him on this home stand". POR's home stand runs through 3 Dec, and the four-week checkpoint falls Fri 27 Nov ([Blazers Edge, 25 Nov](https://www.blazersedge.com/trail-blazers-news/118895/portland-trail-blazers-ja-morant-nba-injury-news-return-micah-nori-spurs-grizzlies)). He was out Wed vs SA ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)).
  - **Timeline:** reported, by 3 Dec. *ESPN est.* 1 Dec.
  - **Value:** POR plays Fri vs GS and Sun vs NO, so a weekend debut is possible but not signalled. Form: season 33.8 (4), L30 28.0 (2) (**small sample**). Rate 31.2. 80% owned. Our IR slot is taken by Leonard.
- **Jusuf Nurkic (UTAH):** Unchanged. Re-evaluation about 27 Nov ([Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). *ESPN est.* 29 Nov.
  - **Rate 36.7:** last season only, with no game this season.
- **Grayson Allen (CHA), Norman Powell (CHI), Duncan Robinson (DET), Zach Edey (MEM):** see Absentees.
- **Others, all unchanged since 25 Nov** (no new report found):

  | Player | Last note | *ESPN est.* |
  |---|---|---|
  | Tobias Harris (SA) | out Wed at POR ([NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf)); debut "expected to be next month" ([Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/san-antonio-spurs-release-injury-190006533.html)) | 3 Dec |
  | Bradley Beal (LAC) | out Wed at MEM, "Right Knee Injury Management" (same report) | 29 Nov |
  | Dejounte Murray (NO) | sitting until traded, no deal reported ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)) | 27 Nov |
  | Dereck Lively II (DAL) | out Tue at DEN ([NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf)); DAL plays only Fri @PHX | 27 Nov |
  | Mitchell Robinson (BOS) | out Tue at WSH, illness (same report) | 27 Nov |
  | Jaxson Hayes (UTAH) | out Mon at LAL ([NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf)) | 27 Nov |
  | Bennedict Mathurin (NO) | out Mon vs PHX (same report) | 27 Nov |
  | T.J. McConnell (IND) | out Mon vs OKC (same report) | 27 Nov |
  | Jock Landale (ATL) | out Sun 22 Nov ([NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)) | 27 Nov |

  - Each is "no timetable reported", except Harris's "next month".

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
- **Research links:** [ESPN scoreboard, 28 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261128) · [ESPN scoreboard, 27 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261127) · [29 Nov](https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20261129) · [NBA injury report, 25 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_11_45PM.pdf) · [NBA injury report, 26 Nov 1:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-26_01_15AM.pdf) · [CP24, 24 Nov](https://www.cp24.com/news/sports/2026/11/24/kawhi-leonard-out-at-least-another-week-as-he-recovers-from-knee-swelling/) · [NBA.com, 25 Nov](https://www.nba.com/news/kawhi-leonard-begins-on-court-workouts-out-at-least-another-week) · [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/collin-murray-boyles-concussion-plays-24-minutes) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-stephen-curry-to-be-re-evaluated-friday/) · [Yahoo, 24 Nov](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909324) · [Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20) · [Bulls.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/bulls-start-giddey-hield-okoro-buzelis-claxton) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909318) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910032) · [23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041) · [NBC Sports, 2 Nov](https://www.nbcsports.com/nba/news/2026-27-nba-news-injury-updates-nov-2-injuries-hit-jalen-williams-cason-wallace-chet-holmgren-in-okc) · [RotoWire, 24 Nov](https://www.rotowire.com/basketball/headlines/jaylin-williams-injury-still-out-wednesday-540874) · [CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-kenrich-williams-headed-to-bench-540713/) · [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/kenrich-williams-scores-20-points-off-bench) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910038) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909320) · [CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-dennis-schroder-remains-out-indefinitely/) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/) · [FantasyPros, 25 Nov](https://www.fantasypros.com/nba/news/622560/grayson-allen-concussion-ruled-out-wednesday.php) · [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910036) · [Hoops Rumors, 20 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-white-james-allen-steinbach.html) · [Kings On SI via Yahoo, 25 Nov](https://sports.yahoo.com/nba/articles/kings-maxime-raynaud-gets-promising-230723065.html) · [RotoWire, 25 Nov](https://www.rotowire.com/basketball/headlines/maxime-raynaud-injury-recalled-to-nba-540983) · [AP via NY1, 18 Oct](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/10/18/kings-guard-ben-simmons-tears-his-achilles-tendon-in-practice) · [ESPN box, 22 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910034) · [Hoops Rumors, 25 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-cunningham-duren-nba-cup-vinson-thompson.html) · [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314) · [CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-practicing-in-g-league/) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jalen-smith-illness-downgraded-to-out-wednesday) · [Bulls On SI, 22 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-update-bad-news-on-norman-powell-jalen-smith-still-questionable-22) · [Yardbarker/Ball Exclusives, 25 Nov](https://www.yardbarker.com/nba/articles/warriors_stephen_curry_to_be_re_evaluated_friday_for_oblique_tear/s1_17668_44615539) · [CBS/RotoWire, 25 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-does-not-return-wednesday/) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909321) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/moritz-wagner-knee-will-not-return-wednesday) · [ESPN box, 25 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909322) · [NBC Sports, 25 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-25/jaylen-brown-hamstring-to-receive-imaging) · [NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/duncan-robinson-quad-considered-day-to-day) · [ESPN box, 18 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910012) · [20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308) · [NY Post via Yahoo, 23 Nov](https://sports.yahoo.com/articles/nets-gets-crushing-injury-nolan-180410690.html) · [Heavy via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-bachero-reveals-190941314.html) · [Blazers Edge, 25 Nov](https://www.blazersedge.com/trail-blazers-news/118895/portland-trail-blazers-ja-morant-nba-injury-news-return-micah-nori-spurs-grizzlies) · [Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/san-antonio-spurs-release-injury-190006533.html) · [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) · [NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf) · [NBA injury report, 23 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_15PM.pdf) · [NBA injury report, 22 Nov 11:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf)
