# News watch: 09 Nov 2026

- Generated 2026-11-09 06:47 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 53 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Melbourne poopoo, Lauri Birds). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 20 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Jamal Murray (ours): questionable Mon 9 Nov at HOU** with a left shin/tibia contusion ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). When or how he was hurt has not been reported ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets); [Gazette, 8 Nov](https://gazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/)). No timetable reported; *ESPN est.* 9 Nov.
  - Plane trouble kept Denver in Mexico City until about 4 p.m. Sunday, after Saturday's win over Indiana. The team cancelled Monday's shootaround and listed all five starters questionable ([Anthony Slater, ESPN via TSN, 8 Nov](https://www.tsn.ca/nba/article/nuggets-starters-all-questionable-vs-rockets-after-delays-leaving-mexico-n1-50426497/); [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets)). Denver has not said the tags are precautionary.
  - Rate **48.8** · season 46.1 (8) → 51.7 (7) · L7 43.7 (3) · L15 51.7 (7) · L30 46.1 (8) → 51.7 (7) · projected 43.9 (`council/form.py`). L30 covers every game so far, so it equals the season average.
  - **L7** 43.7 (3) is 8.0 under his outlier-adjusted season 51.7 (7), and 2.5 under the raw 46.1. The cause is two quieter games: 31 FP in 28 minutes on 4 Nov and 37 in 34 on 7 Nov, against 36.5 min for the season (box scores). No reason has been reported for the 28-minute night.
  - He has 3 games this week (Mon, Wed, Sat), worth 146.3 FP to our lineups in this morning's run ([matchup 4, 9 Nov](20261109-matchup4.md)). Tip-off Monday is 8:30 PM ET (12:30 PM Tue Melbourne). No row: ESPN's date is his next game.
- **Scottie Barnes (ours): questionable Mon 9 Nov vs MEM**, now listed with a **left groin strain** ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). He missed Friday with left adductor/groin soreness and was limited in Sunday's practice (Michael Grange of Sportsnet via [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/barnes-quickley-limited-at-sunday-practice) and [BVM Sports, 8 Nov](https://bvmsports.com/2026/11/08/raptors-scottie-barnes-immanuel-quickley-questionable-vs-grizzlies/)). No timetable reported; *ESPN est.* 9 Nov.
  - He was seen protecting his hip in the third quarter on 4 Nov vs DEN ([BVM Sports, 8 Nov](https://bvmsports.com/2026/11/08/raptors-scottie-barnes-immanuel-quickley-questionable-vs-grizzlies/)). BasketNews says he and Quickley "might remain" inactive ([BasketNews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html)).
  - Rate **48.6** · season 45.9 (8) → 50.7 (7) · L7 44.3 (3) · L15 45.2 (6) → 51.8 (5) · L30 45.9 (8) → 50.7 (7) · projected 43.7 (`council/form.py`).
  - **L7** 44.3 (3) is 6.4 under his outlier-adjusted season 50.7 (7), and 1.6 under the raw 45.9. The cause is his 36 FP in 32 minutes on 4 Nov, the night he was favouring the hip (box scores), followed by the missed game.
  - He has 4 games this week (Mon, Wed, Thu, Sun), worth 194.6 FP to our lineups ([matchup 4, 9 Nov](20261109-matchup4.md)). Tip-off Monday is 7:30 PM ET (11:30 AM Tue Melbourne). No row.
- **Desmond Bane (Tue pickup target): no update since his illness scratch on Saturday.** He was ruled out on 7 Nov at GSW, and RotoWire gave Tue 10 Nov at SAC as his next chance to play ([CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/); [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/desmond-bane-injury-ruled-out-saturday-538008)). Jason Beede of the Orlando Sentinel (8 Nov): the Magic are "hoping" he gets over it soon, with no return given ([Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html)). Orlando's report for Tuesday had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). No timetable reported; *ESPN est.* 10 Nov.
  - Rate **31.1** · season 27.8 (8) → 31.9 (7) · L7 28.0 (3) · L15 32.7 (6) · L30 27.8 (8) → 31.9 (7) · projected 38.2 (`council/form.py`).
  - The plan's condition stands: add him Tuesday (by 10:00 PM ET / 2:00 PM Wed Melbourne) only if Orlando lists him available, otherwise Myles Turner ([matchup 4, 9 Nov](20261109-matchup4.md)). Wed 11 Nov at UTAH, the second night of a back-to-back, is still a rest risk; nothing has been announced.
- **Jalen Duren (ours, IR):** nothing new since 8 Nov. He was cleared for on-court work and will be re-evaluated in two weeks, about **Sun 22 Nov** ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work); [CBS, citing Hunter Patterson of The Athletic, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)). His first possible game is Tue 24 Nov at ORL; *ESPN est.* 24 Nov.
  - Rate **44.1** · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2: small sample.
  - Today's ESPN sync moved him into our IR slot and Kawhi Leonard to the bench ([matchup 4, 9 Nov](20261109-matchup4.md)). No row.
- **Kawhi Leonard (ours, bench):** out Mon vs MEM, listed as "left knee injury management" ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). The Raptors' one-week update is due about 10–11 Nov. NBA.com put his earliest game at Wed 11 Nov vs BOS ([NBA.com, 4 Nov](https://www.nba.com/news/kawhi-leonards-knee-swelling-has-been-treated-and-hell-start-return-to-play-process-raptors-say)); RotoWire thinks he is unlikely back before the end of November ([CBS/RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)). No timetable reported; *ESPN est.* 23 Nov.
  - Rate **41.7** · season 40.0 (2) · L7 — · L15 — · L30 40.0 (2) · projected 45.8: small sample. No row.
- **Anthony Black and Paul George (ours):** nothing new. Wed 11 Nov is the second night of a back-to-back for both, and a rest risk for both; nothing has been announced. George played Sunday at MIL (46 FP in 28 minutes, box score).
- **This week's opponent, Lauri Birds:**
  - **Nikola Jokic** is questionable Mon at HOU with a right elbow sprain, his first injury listing of the season, after the travel delay ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf); [Heavy, 8 Nov](https://heavy.com/sports/nba/denver-nuggets/nikola-jokic-elbow-injury-news-rockets/)). No timetable reported; *ESPN est.* 9 Nov.
  - **Jamal Shead** starts again only if Immanuel Quickley sits. Quickley is questionable Mon with right hamstring tightness ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)); no timetable reported; *ESPN est.* 9 Nov.
- **Pickup targets:**
  - **Rudy Gobert (Thu 12 Nov stream): the rest flag is a false alarm.** His 31 Oct absence was low back spasms, not rest ([NBC, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday)). Thursday is not a back-to-back night. Minnesota's 16–17 Nov back-to-back falls in matchup 5, and nothing has been announced for it.
  - **Brook Lopez:** has started 3 straight, and Rotoworld thinks the job may be his "for the foreseeable future" ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/brook-lopez-finishes-victory-with-20-points)). No coach has said so, and Isaiah Jackson is due back soon (left groin soreness; "not expected to cause an extended absence" ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday)); *ESPN est.* 10 Nov). No row: his rate stays 27.5, with a role rate of 33.3.
  - **Tobias Harris:** RotoWire says he is "almost cleared to suit up", with his first chance on Wed 11 Nov at CHI ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-tobias-harris-unavailable-against-phoenix/)). He is out Monday; *ESPN est.* 11 Nov. Only RotoWire reports this, not the team.
  - Quentin Grimes's start and T.J. McConnell's minutes do not move their value: the start was a one-off for Luka Doncic (lower-back tightness; no timetable reported; *ESPN est.* 9 Nov), and McConnell is questionable again with the same hamstring.
- **Overrides: 2 removed, none added.**
  - **Kon Knueppel** (row: back 13 Nov) is **removed**. The Hornets diagnosed a left hamstring strain on 8 Nov; he is out Monday and will be re-evaluated in four weeks, about Sun 6 Dec ([Hornets PR on X, 8 Nov](https://x.com/HornetsPR/status/2119552085154828648); [ESPN via TSN, 8 Nov](https://www.tsn.ca/nba/article/hornets-knueppel-out-at-least-four-weeks-with-latest-hamstring-strain-n1-50425681/)).
    - ESPN now estimates 12 Dec, which is Charlotte's first game after 6 Dec on the current schedule (ESPN schedule). A row at the day after the re-evaluation (7 Dec) would give that same first game, so ESPN's date stands.
    - matchup.py no longer treats him as playable from 13 Nov.
  - **Tobias Harris** (row: back 14 Nov, a floor) is **removed**. The floor rested on "no timetable", and RotoWire's 8 Nov note now replaces that. ESPN's 11 Nov matches it. If he is out on Wednesday, the next run should flag him again.
  - **Kept:** Yves Missi back 12 Nov (no news since 5 Nov, out 8 Nov), Fred VanVleet sits 16 Nov, and CJ McCollum at 23 min until 22 Nov.
  - **Effect on matchup 4:** neither removed player is on a matchup-4 roster, so no rostered projection moves. Harris (SA plays 11, 13, 15 Nov) becomes a streaming candidate from Wednesday. Re-run `/matchup` once Monday's final reports (Murray, Barnes) and Orlando's Tuesday report (Bane) are out.
- **Melbourne poopoo** were our matchup 3 opponent, and that matchup ended Sunday. The script still lists them as an opponent because ESPN had not rolled over to matchup 4 when it ran: the header puts them ahead of Lauri Birds, this week's opponent ([matchup 4, 9 Nov](20261109-matchup4.md)). Their flags (Thompson, Davis, Edgecombe) do not affect matchup 4.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Kon Knueppel | return | 2026-11-13 | — | [link](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/) | in force |
| Yves Missi | return | 2026-11-12 | — | [link](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773) | in force |
| Tobias Harris | return | 2026-11-14 | — | [link](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role) | in force |

**Research changes** (the table above is the script's read, before research): the **Kon Knueppel** and **Tobias Harris** rows are removed. ESPN's dates now match the newest reporting (see What changed for us). The other three rows stay in force, and none has expired.

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Anthony Black** | ORL | us | rest | 42.1 | — | active |
| **Paul George** | BOS | us | rest | 39.4 | — | active |
| **Kawhi Leonard** | TOR | us | gap | 41.7 † | — | out, ESPN est. 23 Nov |
| **Yves Missi** | NO | free agent | injury | 60.4 † | — | out, ESPN est. 09 Nov |
| **Maxime Raynaud** | SAC | free agent | injury, gap | 28.1 | — | out, ESPN est. 10 Nov |
| **Jalen Suggs** | ORL | free agent | injury, gap | 25.8 | — | out, ESPN est. 10 Nov |
| **CJ McCollum** | ATL | waivers | role | 31.0 | 23.5 | active |
| **Aday Mara** | OKC | waivers | role | 27.8 | 32.0 | active |
| **Brook Lopez** | LAC | free agent | role | 27.5 | 33.3 | active |
| **Quentin Grimes** | LAL | free agent | role | 15.1 | 22.3 | day-to-day, ESPN est. 09 Nov |
| **Spencer Jones** | DEN | free agent | minutes | 29.1 † | — | active |
| **T.J. McConnell** | IND | free agent | minutes | 13.8 † | — | day-to-day, ESPN est. 09 Nov |
| **Rudy Gobert** | MIN | free agent | rest | 29.6 | — | active |
| **Robert Williams III** | POR | free agent | rest | 29.3 | — | day-to-day, ESPN est. 10 Nov |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 11 Nov |
| **Jamal Shead** | TOR | Lauri Birds | role | 26.8 | 35.2 | active |
| **Klay Thompson** | MIA | Melbourne poopoo | minutes | 28.4 | 29.4 | active |
| **Anthony Davis** | WSH | Melbourne poopoo | rest | 50.7 | — | day-to-day, ESPN est. 09 Nov |
| **VJ Edgecombe** | PHI | Melbourne poopoo | rest | 36.2 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Anthony Black (ORL, PG/SG, us)

- Rate **42.1** · season 38.5 (6) → 44.0 (5) · L7 41.0 (3) · L15 38.5 (6) → 44.0 (5) · L30 38.5 (6) → 44.0 (5) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Tue 10–Wed 11 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- **Research:**
  - **Since last night:** no new report. Orlando was off Sunday and is off Monday. Its report for Tue at SAC had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - Saturday's overtime cramps brought no injury designation ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)). Jason Beede: he left with 2:47 left in overtime with a cramp, and had his left leg worked on at the bench ([Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html)).
  - **Rest:** he sat 2 Nov, the second night of a back-to-back, for right ankle injury management ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)). **Wed 11 Nov at UTAH**, the night after Tue at SAC, is a rest risk; nothing has been announced.
  - **Verdict:** nothing new found. Active is right. No sit row.

### Paul George (BOS, SF/PF, us)

- Rate **39.4** · season 41.3 (9) · L7 39.0 (4) · L15 38.3 (7) · L30 41.3 (9) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Tue 10–Wed 11 Nov, Sun 15–Mon 16 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (07 Nov): George registered eight points (3-11 FG, 2-5 3Pt), five rebounds, an assist, a steal and two blocks across 22 minutes in Friday's 119-80 win over the Hornets.
- News (04 Nov): George produced 25 points (8-18 FG, 5-9 3Pt, 4-7 FT), three rebounds, five assists and four steals over 35 minutes in Wednesday's 109-102 win over the Bucks.
- **Research:**
  - **Since last night:** he played Sunday at MIL (46 FP in 28 minutes, ESPN box score). No rest has been announced. Boston's report for Tue at PHI had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - **Rest:** 2 Nov was a "planned maintenance day" on the second night of a road–road back-to-back ([NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)). Asked about more rest days, he said "we'll get to that when the time is there" ([Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)).
  - **Tue 10–Wed 11 Nov** (at PHI, at TOR) is road–road again, so **Wed 11 Nov is a rest risk**. 15–16 Nov is at home.
  - **Verdict:** nothing new found. No sit row: nothing has been announced.

### Kawhi Leonard (TOR, SF/PF, us)

- Rate **41.7** (small sample) · season 40.0 (2) · L7 — · L15 — · L30 40.0 (2) · projected 45.8
- ESPN: out, ESPN est. 23 Nov (Left Knee Inflammation, updated 2026-11-04)
- **Gap:** listed out, and no news in 5 days (ESPN est. 23 Nov)
- News (03 Nov): Leonard has completed treatment to reduce swelling in his left knee and he will be re-evaluated in one week, Brett Siegel of ClutchPoints.com reports.
- News (29 Oct): Leonard (knee) is expected to be sidelined for at least three to four weeks, Chris Haynes of NBA TV reports.
- **Research:**
  - **Status:** out Mon vs MEM with "left knee injury management" ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). No new report since 3 Nov.
  - On 3 Nov the Raptors said he had finished treatment for knee swelling and begun a "return to play" process, with an update in about a week ([TSN, 3 Nov](https://www.tsn.ca/nba/article/raptors-leonard-completes-knee-swelling-treatment-will-be-evaluated-in-one-week/)). NBA.com put his earliest game at Wed 11 Nov vs BOS ([NBA.com, 4 Nov](https://www.nba.com/news/kawhi-leonards-knee-swelling-has-been-treated-and-hell-start-return-to-play-process-raptors-say)).
  - Imaging showed no new injury. TSN's Josh Lewenberg reports a chronic condition the Raptors will have to manage ([Fadeaway World via Yahoo, 6 Nov](https://sports.yahoo.com/articles/kawhi-leonard-details-reveal-true-025731396.html)). RotoWire thinks he is unlikely back before the end of November ([CBS/RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)).
  - **Gap flag:** there has been no news because the next update is not due until about 10–11 Nov.
  - **Expected return:** no timetable reported. His earliest game is 11 Nov per NBA.com; *ESPN est.* 23 Nov.
  - **Verdict:** nothing new found. No row: a re-evaluation is not a return, and ESPN's date fits RotoWire's reading. His rate (41.7) rests on 2 games: small sample. Since today's sync he is on our bench, with Duren in IR.

## Free agents and waivers

### Yves Missi (NO, C, free agent)

- Rate **60.4** (small sample) · season 41.5 (2) → 68.0 (1) · L7 — · L15 — · L30 41.5 (2) → 68.0 (1) · projected 24.7
- ESPN: out, ESPN est. 09 Nov (Left Knee Bruise, updated 2026-11-05)
- **Injury:** ESPN est. 09 Nov (Out, Left Knee Bruise, updated 05 Nov), but the news said on 05 Nov: "He remains without a timetable to return and can be considered week-to-week moving forward."
- News (05 Nov): Missi (knee) is out for Friday's game against Minnesota.
- News (30 Oct): Missi (knee) won't play in Saturday's game against Atlanta.
- **Research:**
  - **Since last night:** nothing new. He was out 8 Nov at LAC with a left knee contusion and bone bruise ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). New Orleans' report for Mon at GSW had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - Week-to-week with no timetable as of 5 Nov ([RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)). The bone bruise dates from 23 Oct, and there has been no timeframe since ([ClutchPoints, citing Brett Siegel, 24 Oct](https://clutchpoints.com/nba/new-orleans-pelicans/pelicans-news-yves-missi-unfortunate-injury-update); [CBS/RotoWire, 30 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-ruled-out-saturday-as-expected/)).
  - **Expected return:** no timetable reported (week-to-week); *ESPN est.* 9 Nov, too early.
  - **Verdict:** ESPN corrected. **Override (kept):** return 2026-11-12, a floor. New Orleans plays 11, 13 and 14 Nov, so his first possible game is Fri 13 Nov. This morning's matchup plan also treats him as out on 13 and 14 Nov as a what-if ([matchup 4, 9 Nov](20261109-matchup4.md)).
  - His rate (60.4) rests on one 68-FP game after his 9-minute exit was dropped: small sample.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 10 Nov (Right Knee Dislocated, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee Dislocated, updated 26 Oct), but the news said on 26 Oct: "Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- News (15 Oct): Raynaud (knee) is expected to miss at least the first five or six games of the regular season, and potentially longer, Frankie Cartoscelli of KHTK Sactown Sports 1140 reports.
- **Research:**
  - **Since last night:** no report yet on the re-evaluation, which was due "next week", the week of 9 Nov ([Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap); [AP preview, 8 Nov](https://www.1075thegame.com/2026/11/08/heat-look-to-reverse-course-vs-struggling-kings/)). Sacramento's report for Tue vs ORL had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - The injury is a right patella subluxation, not a dislocation, so ESPN's "dislocated" label overstates it ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - **Gap flag:** there has been no news because the re-evaluation is due this week.
  - **Expected return:** re-evaluation this week, no return date reported; *ESPN est.* 10 Nov, probably early.
  - **Verdict:** ESPN confirmed, as a floor. No row: no source gives a later date. No games this season, so his rate (28.1) is last season's or the projection.

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **25.8** · season 26.3 (3) · L7 — · L15 23.0 (1) · L30 26.3 (3) · projected 29.2
- ESPN: out, ESPN est. 10 Nov (Right Knee, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee, updated 26 Oct), but the news said on 26 Oct: "Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports.
- News (25 Oct): Suggs (knee) did not return to Sunday's game against the Knicks.
- **Research:**
  - **Since last night:** Jason Beede (Orlando Sentinel, 8 Nov): Monday ends the two-week re-evaluation window, but that "doesn't necessarily mean" he plays on the road trip (Tue at SAC, Wed at UTAH). The team is expected to give more clarity ([Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html)).
  - Orlando's report for Tuesday had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - Mild right knee bone bruise; to be re-evaluated two weeks from 26 Oct ([Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html)).
  - **Expected return:** re-evaluation 9 Nov, no return date reported; *ESPN est.* 10 Nov, which Beede's note makes optimistic.
  - **Verdict:** ESPN confirmed as the earliest date. No row: the rule's date (the day after the re-evaluation) is ESPN's, and no source gives a later one. His L15 23.0 (1) is one game: small sample, noise.

### CJ McCollum (ATL, PG/SG, waivers)

- Rate **31.0** · role rate 23.5 · season 25.9 (11) → 28.0 (10) · L7 27.8 (4) → 35.3 (3) · L15 26.1 (9) → 28.8 (8) · L30 25.9 (11) → 28.0 (10) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 9; 22.0 min in those 2, against 25.7 for the season
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- News (04 Nov): McCollum is not listed in the starting lineup for Wednesday's game against Washington, Brad Rowland of the Locked On Podcast Network reports.
- **Research:**
  - **Since last night:** nothing new. Atlanta did not play Sunday and hosts the Lakers on Monday. No change to the bench role has been reported.
  - **Role:** off the bench 3 straight games (25, 23 and 21 min) after giving his start to Kingston Flemings, and still there when Jalen Johnson returned on 7 Nov ([RotoWire via CBS, 8 Nov](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role); [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury)). Quin Snyder: "roles change not just game to game" ([Roundtable, 8 Nov](https://roundtable.io/sports/nba/hawks/opinion/4-takeaways-from-hawks-124-121-comeback-win-over-nets)).
  - **L7:** 27.8 (4) → 35.3 (3) is 7.3 over his season 25.9 (11) → 28.0 (10) once the 5-FP game of 6 Nov is dropped. The cause is 45 FP in his last start on 2 Nov and 36 in his first bench game on 4 Nov (box scores).
  - **Verdict:** the bench role is ongoing. **Override (kept):** role, 23 min until 22 Nov. The matchup run uses a role rate of **24.6 ‡** at 23 min in place of his rate of 31.0 ([matchup 4, 9 Nov](20261109-matchup4.md)); at the 22.0 min of his last 2 games, this report's role rate is 23.5.

### Aday Mara (OKC, C, waivers)

- Rate **27.8** · role rate 32.0 · season 24.4 (10) · L7 31.8 (4) · L15 27.0 (8) · L30 24.4 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 8 before; 26.0 min in his starts, against 19.8 for the season
- **Role:** news on 07 Nov: "Mara will start Saturday against the Wizards, Rylan Stiles of SI.com reports."
- News (08 Nov): Mara registered 18 points (8-10 FG, 1-1 3Pt, 1-2 FT), eight rebounds, three assists and three blocks in Saturday's 114-75 win over the Wizards.
- News (07 Nov): Mara will start Saturday against the Wizards, Rylan Stiles of SI.com reports.
- **Research:**
  - **Since last night:** nothing new. OKC did not play Sunday, and its report for Tue at POR had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). He is on waivers after we dropped him on 8 Nov.
  - **Role:** his starts follow the lineup OKC picks each game:
    - 4 Nov: started for Jaylin Williams, out with back spasms ([NBC, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/aday-mara-to-make-first-career-start-wednesday)).
    - 6 Nov: back to the bench when OKC went small ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/thunder-start-shai-mccain-ajay-kenrich-i-hart)).
    - 7 Nov: started in a "bigger lineup" ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart)).
  - **Injured teammates:**
    - Jaylin Williams has missed 3 straight games; no timetable reported ([CBS, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/)); *ESPN est.* 10 Nov.
    - Chet Holmgren is out 8–10 weeks from 30 Oct ([NBA.com](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear)); *ESPN est.* 2 Jan.
  - **L7:** 31.8 (4) is 7.4 over his season 24.4 (10). The cause is his two starts (26.0 min in them, against 19.8 for the season), including 50 FP on 7 Nov (box scores).
  - **Verdict:** nothing new found. No role row: his rate stays 27.8, and the role rate (32.0) is the value of a start, not of a settled role.

### Brook Lopez (LAC, C, free agent)

- Rate **27.5** · role rate 33.3 · season 28.8 (9) · L7 29.8 (4) · L15 24.7 (7) · L30 28.8 (9) · projected 26.2
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 7 before; 27.7 min in his starts, against 23.9 for the season
- News (05 Nov): Lopez logged 20 points (8-11 FG, 2-5 3Pt, 2-5 FT), eight rebounds, one assist and two blocks across 35 minutes during Wednesday's 117-116 overtime loss to the Heat.
- News (02 Nov): Lopez will start Monday's game against the Raptors, NBA writer Justin Russo reports.
- **Research:**
  - **Role:** he has started 3 straight games:
    - 2 Nov vs TOR, with Isaiah Jackson moved to the bench ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-isaiah-jackson-heading-to-bench-monday/)).
    - 4 Nov vs MIA, 35 minutes in overtime ([CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-brook-lopez-scores-20-as-starter/)).
    - 8 Nov vs NO, with Jackson out (left groin soreness). He was "the only healthy center" and was to play "as many minutes as he can handle" ([Clippers On SI via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-injury-report-vs-pelicans-224719276.html); [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-jackson-groin-out-sunday-vs-pelicans)). He scored 20 on 8-11 shooting in 26 minutes ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/brook-lopez-finishes-victory-with-20-points)).
  - **Will it last?** No coach has said:
    - Rotoworld's analyst (5 Nov) says he "may have the starting center job for the foreseeable future" ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/brook-lopez-finishes-victory-with-20-points)).
    - RotoWire warns that "Jackson's emergence could make the center minutes a timeshare" ([CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-brook-lopez-scores-20-as-starter/)).
    - In October, Tyronn Lue named Jackson the starter ([NBC, 17 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-17/lue-jackson-to-begin-season-as-starting-center)).
  - **Jackson:** travels for Tue at PHX, and the groin is "not expected to cause an extended absence" (Joey Linn via [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday)). No timetable reported; *ESPN est.* 10 Nov.
  - **Minutes:** 22, 35 (overtime) and 26 in his starts. The 27.7 average behind the role rate includes the overtime game.
  - **Verdict:** the start should hold while Jackson is out, but no source calls it settled. No role row: his rate stays 27.5, and the role rate (33.3) is the value of a starting night. LAC plays Tue 10, Fri 13 and Sun 15 Nov.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **15.1** · role rate 22.3 · season 16.6 (11) · L7 12.6 (5) · L15 13.4 (9) · L30 16.6 (11) · projected 28.1
- ESPN: day-to-day, ESPN est. 09 Nov (Finger, updated 2026-11-09)
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 26.1 for the season
- **Role:** news on 08 Nov: "Grimes will start in Sunday's game against the Pistons."
- News (08 Nov): Grimes (finger) did not return to Sunday's game against the Pistons.
- News (08 Nov): Grimes went back to the locker room during Sunday's game against the Pistons, Dave McMenamin of ESPN.com reports.
- **Research:**
  - **Role:** a one-off. He started Sunday at DET only because Luka Doncic sat with lower-back tightness, and his only other start (28 Oct) was also for Doncic (ESPN's news feed, 29 Oct and 8 Nov). He goes back to the bench when Doncic returns ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger)).
  - Doncic: out Sunday with lower-back tightness, his second such absence this season. His Monday status has not been reported; no timetable reported; *ESPN est.* 9 Nov.
  - **Injury:** he left in the fourth quarter Sunday after banging a finger on his right hand. JJ Redick: "X-ray is negative, nothing beyond that" (Dan Woike on X, via [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger); [BasketNews, 8 Nov](https://basketnews.com/news-259092-what-happened-to-quentin-grimes-jj-redick-gives-crucial-injury-update-after-lakers-win.html)).
    - RotoWire calls him questionable at best for Mon at ATL (ESPN's news feed, 9 Nov). The Lakers' report for Monday had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
    - No timetable reported; *ESPN est.* 9 Nov.
  - **Minutes:** 32 Sunday, with 35.0 the average across his 2 starts, against 26.1 for the season. He played 20–26 off the bench in his other recent games (box scores).
  - **Verdict:** ESPN confirmed (day-to-day). No row: the start was tied to Doncic. His rate stays 15.1; the role rate (22.3) applies only on a night Doncic sits.

### Spencer Jones (DEN, SF/PF, free agent)

- Rate **29.1** (small sample) · season 30.0 (1) · L7 30.0 (1) · L15 30.0 (1) · L30 30.0 (1)
- ESPN: active
- **Minutes:** news on 06 Nov: "He'll challenge Bryce Hopkins and Alpha Diallo for playing time, but Jones is likely to have a minutes cap early on."
- News (08 Nov): Jones had 13 points (5-6 FG, 3-3 3Pt), six rebounds and one block across 21 minutes during Saturday's 114-102 win over the Pacers.
- News (06 Nov): Jones (hamstring) is off the injury report for Saturday's game against Indiana.
- **Research:**
  - **Since last night:** Denver did not play Sunday, stranded in Mexico City by plane trouble ([ESPN via TSN, 8 Nov](https://www.tsn.ca/nba/article/nuggets-starters-all-questionable-vs-rockets-after-delays-leaving-mexico-n1-50426497/)). He is not on Denver's report for Mon at HOU ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - All five Denver starters are questionable. If a forward sits, more minutes open up, and Heavy names Trevon Brazile as the likely fill-in for Aaron Gordon ([Heavy, 8 Nov](https://heavy.com/sports/nba/denver-nuggets/nuggets-mexico-city-travel-nikola-jokic-questionable/)). Gordon is questionable with lower-body injury management ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)); no timetable reported; *ESPN est.* 9 Nov.
  - The "minutes cap" was RotoWire's expectation, not a team figure ([CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/)). In his debut he had 13 points on 5-6 FG in 21 minutes ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)).
  - **Verdict:** the cap is not confirmed. No row. His rate (29.1) rests on one game: small sample.

### T.J. McConnell (IND, PG, free agent)

- Rate **13.8** (small sample) · season 13.0 (1) · L7 13.0 (1) · L15 13.0 (1) · L30 13.0 (1) · projected 24.4
- ESPN: day-to-day, ESPN est. 09 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Minutes:** news on 08 Nov: "The veteran floor general played limited minutes but was productive."
- News (08 Nov): McConnell is questionable for Monday's game against the Mavericks due to a right hamstring strain.
- News (08 Nov): McConnell ended Saturday's 114-102 loss to the Nuggets with six points (3-5 FG), two rebounds, one assist and one block across nine minutes.
- **Research:**
  - **Minutes:** the 9 minutes on 7 Nov were his season debut, after a right hamstring strain kept him out of the first nine games. Rick Carlisle cleared him that day and named no limit ([Roundtable via Yahoo, 7 Nov](https://sports.yahoo.com/articles/t-j-mcconnell-cleared-season-203829170.html)). "Limited minutes" is RotoWire's description, not a team restriction.
  - **Injury:** questionable Mon at DAL with the same right hamstring strain ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-questionable-for-monday-538210/); [NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). No timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN confirmed. No row: no restriction has been reported. His rate (13.8) and every window rest on one 9-minute game: small sample.

### Rudy Gobert (MIN, C, free agent)

- Rate **29.6** · season 26.9 (10) · L7 31.5 (4) · L15 28.6 (8) · L30 26.9 (10) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- News (01 Nov): Gobert (back) is not listed on the injury report for Monday's game against Milwaukee.
- **Research:**
  - **Rest:** a false alarm. He missed 31 Oct at SA, the second night of a back-to-back, with low back spasms: listed questionable, then downgraded to out ([NBC, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday)). He was off the report for the next game (ESPN's news feed, 1 Nov). No back-to-back rest plan has been reported this season.
  - **Form:** 10 points (4-4 FG), 15 rebounds and 2 assists in 31 minutes in Sunday's win over Utah ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/rudy-gobert-posts-15-rebounds-in-win-over-jazz)). Started 10 of 10.
  - **For us:** Minnesota plays 12, 14, 16 and 17 Nov (ESPN schedule), so Thursday, his planned stream day, is not a back-to-back night. The 16–17 Nov back-to-back falls in matchup 5, and nothing has been announced for it.
  - **Verdict:** nothing new found. No sit row. The Thu 12 Nov stream stands.

### Robert Williams III (POR, C, free agent)

- Rate **29.3** · season 28.1 (7) · L7 30.3 (3) · L15 30.2 (5) · L30 28.1 (7) · projected 26.9
- ESPN: day-to-day, ESPN est. 10 Nov (Rest, updated 2026-11-08)
- **Rest:** back-to-back Tue 10–Wed 11 Nov, Mon 16–Tue 17 Nov; news on 07 Nov: "Williams (rest) won't play in Saturday's game against the Spurs."
- News (07 Nov): Williams (rest) won't play in Saturday's game against the Spurs.
- News (05 Nov): Williams closed Wednesday's 132-119 victory over the Suns with nine points (4-8 FG, 1-1 FT), eight rebounds, one assist, three blocks and two steals over 16 minutes.
- **Research:**
  - **Since last night:** nothing new. Portland's report for Tue vs OKC had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - **Rest:** he sat Sat 7 Nov "to rest", the second night of a back-to-back ([RotoWire, 7 Nov](https://rotowire.com/basketball/headlines/robert-williams-news-resting-versus-spurs-538018); [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs)). Last season Portland rested him on second nights for left knee management ([CBS/RotoWire, 1 Mar 2026](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-robert-williams-resting-sunday/)).
  - **Wed 11 Nov** (the second of two home games vs OKC) and **Tue 17 Nov** are rest risks; neither has been announced. ESPN's "rest" label (*ESPN est.* 10 Nov) is Saturday's night off, and he is healthy for Tuesday.
  - **Verdict:** nothing new found. ESPN's date (his next game) is right. No sit row.

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 11 Nov (Left Calf Strain, updated 2026-11-09)
- **Gap:** listed out, and no news in 5 days (ESPN est. 11 Nov)
- **Research:**
  - **Since last night:** out Mon at PHX ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
    - RotoWire (8 Nov, 7:27 PM ET): "Harris is almost cleared to suit up", and his next chance to debut is **Wed 11 Nov at CHI** ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-tobias-harris-unavailable-against-phoenix/); [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/tobias-harris-injury-unavailable-against-phoenix-538223)).
    - No team or beat source has said so yet.
  - **Before that:**
    - He was doing on-court work, and the staff was "unfortunately conservative" ([Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html)).
    - Mitch Johnson: "very, very methodically" ([Hoops Rumors, 1 Nov, citing Tom Orsborn of the Express-News](https://www.hoopsrumors.com/2026/11/spurs-notes-harris-wembanyama-castle-fox.html)).
  - **Gap flag:** the 8 Nov note fills the gap.
  - **Expected return:** no team timetable. His first possible game is Wed 11 Nov per RotoWire; *ESPN est.* 11 Nov.
  - **Verdict:** ESPN confirmed. **Override removed:** the 14 Nov floor rested on "no timetable", which the newer report replaces, and ESPN's 11 Nov matches that report. San Antonio plays 11, 13 and 15 Nov. If he is out on Wednesday, the next run should flag him again. No games this season, so his rate (28.0) is last season's.

## Opponents: this week and next

### Jamal Shead (TOR, PG, Lauri Birds)

- Rate **26.8** · role rate 35.2 · season 23.7 (9) · L7 30.8 (4) · L15 27.3 (7) · L30 23.7 (9) · projected 20.7
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 7 before; 34.0 min in his starts, against 22.9 for the season
- **Role:** news on 06 Nov: "Shead will start Friday against the Bucks, Esfandiar Baraheni of The Athletic reports."
- News (06 Nov): Shead delivered 10 points (4-10 FG, 1-5 3Pt, 1-2 FT), three rebounds, 16 assists and two steals in Friday's 121-107 win over the Bucks.
- News (06 Nov): Shead will start Friday against the Bucks, Esfandiar Baraheni of The Athletic reports.
- **Research:**
  - **Role:** a one-off. He started 6 Nov only because Immanuel Quickley (right hamstring) was out, and had 16 assists ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl); [RotoWire, 6 Nov](https://www.rotowire.com/basketball/headlines/jamal-shead-news-starting-friday-537893)). If Quickley returns soon, Shead goes back to a reserve role ([Last Word on Sports, 7 Nov](https://lastwordonsports.com/basketball/2026/11/07/raptors-reserves-shead)).
  - Quickley is questionable Mon vs MEM after a limited Sunday practice (Michael Grange via [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/barnes-quickley-limited-at-sunday-practice); [NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)). No timetable reported; *ESPN est.* 9 Nov. Rotoworld expects Shead to take his role again if he sits.
  - **Minutes:** 34 in the start, against 22.9 for the season. He played under 25 in all but two of his nine games ([Last Word on Sports, 7 Nov](https://lastwordonsports.com/basketball/2026/11/07/raptors-reserves-shead)).
  - **L7:** 30.8 (4) is 7.1 over his season 23.7 (9). The cause is the 52-FP start on 6 Nov (box scores).
  - **For us:** he is on Lauri Birds, this week's opponent. Toronto plays Mon, Wed, Thu and Sun. Each game Quickley misses lifts Shead from his rate (26.8) toward the role rate (35.2).
  - **Verdict:** a one-off, tied to Quickley. No role row.

### Klay Thompson (MIA, SG/SF, Melbourne poopoo)

- Rate **28.4** · role rate 29.4 · season 23.7 (10) · L7 35.8 (4) · L15 27.5 (8) · L30 23.7 (10) · projected 19.5
- ESPN: active
- **Minutes:** 30.0 min over his last 3 games against 24.2 for the season (+5.8)
- News (06 Nov): Thompson closed with 11 points (3-10 FG, 2-7 3Pt, 3-3 FT), three assists and two blocks over 23 minutes during Thursday's 120-100 loss to the Warriors.
- News (05 Nov): Thompson notched 30 points (11-22 FG, 8-17 3Pt), five rebounds, three assists and one block across 35 minutes during Wednesday's 117-116 overtime win over the Clippers.
- **Research:**
  - **Since last night:** 23 points with seven 3-pointers (7-13), four assists and two blocks in Sunday's win at SAC ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/klay-thompson-sinks-seven-three-pointers-vs-sac); [ESPN recap, 8 Nov](https://www.espn.com/nba/recap?gameId=401909951)). He has scored 19+ in three of the four games on Miami's road trip (Rotoworld, same note).
  - **Minutes:** 35 (the 4 Nov overtime), 23 and 32 in his last 3 games. No bigger role has been reported ([Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-thompson-wiggins-larsson-hardaway-conwell-giannis.html)).
  - **L7:** 35.8 (4) is 12.1 over his season 23.7 (10). The cause is shooting, eight 3-pointers on 4 Nov and seven on Sunday (News line above; [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/klay-thompson-sinks-seven-three-pointers-vs-sac)), plus the overtime minutes.
  - **For us:** Melbourne poopoo were our matchup 3 opponent, and that matchup ended Sunday (see What changed for us).
  - **Verdict:** nothing new found. No row.

### Anthony Davis (WSH, PF/C, Melbourne poopoo)

- Rate **50.7** · season 45.9 (8) · L7 58.5 (2) · L15 47.7 (6) · L30 45.9 (8) · projected 49.6
- ESPN: day-to-day, ESPN est. 09 Nov (Right Ankle Sprain, updated 2026-11-08)
- **Rest:** back-to-back Wed 11–Thu 12 Nov, Sun 15–Mon 16 Nov; news on 07 Nov: "After missing Friday's 139-132 loss to Atlanta, Davis is questionable to suit up on the second night of Washington's back-to-back due to a sprained right ankle."
- News (08 Nov): Davis (ankle) is listed as questionable for Monday's game in Detroit.
- News (07 Nov): Davis (ankle) won't play Saturday against the Thunder.
- **Research:**
  - **Since last night:** still questionable Mon at DET with a right ankle sprain ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf); [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-davis-ankle-questionable-monday-vs-det)). He missed the last two games, and the team is reportedly optimistic ([BasketNews, 8 Nov](https://basketnews.com/news-259082-will-anthony-davis-finally-play-latest-injury-status-revealed-by-wizards.html)).
  - He sprained the ankle on 4 Nov and played through it ([BasketNews, 5 Nov](https://basketnews.com/news-258907-anthony-davis-injury-update-raises-concerns-for-washington-wizards.html)), then missed 6 and 7 Nov ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/anthony-davis-ankle-downgraded-to-out-saturday)).
  - **Rest:** a false alarm. The note was about his ankle on the second night of a back-to-back, not about rest. Nothing has been announced for 11–12 or 15–16 Nov.
  - **L7:** 58.5 (2) is a 2-game window: small sample (12-17 and 12-19 shooting on 2 and 4 Nov).
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** nothing new found. No row. He is not on a matchup-4 roster.

### VJ Edgecombe (PHI, SG, Melbourne poopoo)

- Rate **36.2** · season 33.6 (10) · L7 39.5 (4) · L15 35.2 (8) · L30 33.6 (10) · projected 33.7
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 24–25 Oct back-to-back, playing the games either side
- News (06 Nov): Edgecombe recorded 19 points (8-13 FG, 3-5 3Pt), three rebounds, two assists and four steals over 32 minutes in Friday's 119-95 loss to the Cavs.
- News (03 Nov): Edgecombe notched 21 points (9-12 FG, 2-4 3Pt, 1-3 FT), three rebounds, five assists, a steal and a block across 33 minutes in Monday's 126-107 win over the Bulls.
- **Research:**
  - **Since last night:** he played Sunday at CHI (40 FP in 35 minutes, ESPN box score). No rest plan has been reported for Sun 15–Mon 16 Nov.
  - His 25 Oct absence was an abdominal contusion, not rest ([BasketNews, 25 Oct](https://basketnews.com/news-258120-vj-edgecombe-final-status-for-76ers-vs-pistons-revealed.html); [The Sixer Sense, 28 Oct](https://thesixersense.com/76ers-starting-five-will-reunite-vj-edgecombe-dodged-real-setback)).
  - **L7:** 39.5 (4) is 5.9 over his season 33.6 (10). The cause is shooting in his usual 32–35 minutes: 8-13 FG on 6 Nov and 9-12 on 2 Nov (News lines above).
  - **Verdict:** the rest flag is a false alarm. No row.

## Other rosters: injury flags only

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - **Since last night:** nothing new. Orlando's report for Tuesday had not been submitted at 1:45 AM ET ([NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf)).
  - Low-grade right high-ankle sprain, "typically" 4–6 weeks ([Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html)). Banchero himself: "at least a month" ([Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182)). He was out 7 Nov at GSW ([Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)).
  - **Gap flag:** no news, because no update is due before the four-week mark (about 21 Nov).
  - **Expected return:** 4–6 weeks from 24 Oct (21 Nov to 5 Dec); *ESPN est.* 22 Nov, the early end.
  - **Verdict:** nothing new found. No row. His rate (60.9) is a small sample.

## Sources

- Research checked on 9 Nov 2026, about 06:50–07:30 UTC. Players researched last night were re-checked for Sunday's results and Monday's injury report; their earlier links are kept.
- Official: [NBA injury report, 9 Nov 1:45 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-09_01_45AM.pdf) (Monday's games; the Lakers, Pistons, Mavericks and Pelicans had not submitted, and no team had submitted for Tuesday) · [NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf).
- **Jamal Murray:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets) · [Gazette, 8 Nov](https://gazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/) · [ESPN via TSN, 8 Nov](https://www.tsn.ca/nba/article/nuggets-starters-all-questionable-vs-rockets-after-delays-leaving-mexico-n1-50426497/) · [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets) · [Heavy, 8 Nov (Jokic)](https://heavy.com/sports/nba/denver-nuggets/nikola-jokic-elbow-injury-news-rockets/) · [Heavy, 8 Nov (travel)](https://heavy.com/sports/nba/denver-nuggets/nuggets-mexico-city-travel-nikola-jokic-questionable/)
- **Scottie Barnes:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/barnes-quickley-limited-at-sunday-practice) · [BVM Sports/Sportsnet, 8 Nov](https://bvmsports.com/2026/11/08/raptors-scottie-barnes-immanuel-quickley-questionable-vs-grizzlies/) · [BasketNews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html)
- **Desmond Bane:** [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/) · [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/desmond-bane-injury-ruled-out-saturday-538008) · [Jason Beede via Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html)
- **Jalen Duren:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work) · [CBS, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)
- **Kawhi Leonard:** [TSN, 3 Nov](https://www.tsn.ca/nba/article/raptors-leonard-completes-knee-swelling-treatment-will-be-evaluated-in-one-week/) · [NBA.com, 4 Nov](https://www.nba.com/news/kawhi-leonards-knee-swelling-has-been-treated-and-hell-start-return-to-play-process-raptors-say) · [CBS/RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/) · [Fadeaway World via Yahoo, 6 Nov](https://sports.yahoo.com/articles/kawhi-leonard-details-reveal-true-025731396.html)
- **Kon Knueppel:** [Hornets PR on X, 8 Nov](https://x.com/HornetsPR/status/2119552085154828648) · [ESPN via TSN, 8 Nov](https://www.tsn.ca/nba/article/hornets-knueppel-out-at-least-four-weeks-with-latest-hamstring-strain-n1-50425681/)
- **Anthony Black:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping) · [Jason Beede via Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html) · [Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)
- **Paul George:** [NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets) · [Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)
- **Yves Missi:** [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773) · [ClutchPoints, 24 Oct](https://clutchpoints.com/nba/new-orleans-pelicans/pelicans-news-yves-missi-unfortunate-injury-update) · [CBS/RotoWire, 30 Oct](https://www.cbssports.com/fantasy/basketball/news/pelicans-yves-missi-ruled-out-saturday-as-expected/)
- **Maxime Raynaud:** [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap) · [AP preview, 8 Nov](https://www.1075thegame.com/2026/11/08/heat-look-to-reverse-course-vs-struggling-kings/)
- **Jalen Suggs:** [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html) · [Jason Beede via Yahoo, 8 Nov](https://sports.yahoo.com/articles/no-magic-margin-error-loss-214900681.html)
- **CJ McCollum:** [RotoWire via CBS, 8 Nov](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury) · [Roundtable, 8 Nov](https://roundtable.io/sports/nba/hawks/opinion/4-takeaways-from-hawks-124-121-comeback-win-over-nets)
- **Aday Mara:** [NBC, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/aday-mara-to-make-first-career-start-wednesday) · [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/thunder-start-shai-mccain-ajay-kenrich-i-hart) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart) · [CBS, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/) · [NBA.com, Holmgren](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear)
- **Brook Lopez:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/brook-lopez-finishes-victory-with-20-points) · [CBS/RotoWire, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-brook-lopez-scores-20-as-starter/) · [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-isaiah-jackson-heading-to-bench-monday/) · [Clippers On SI via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-injury-report-vs-pelicans-224719276.html) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-jackson-groin-out-sunday-vs-pelicans) · [NBC, 8 Nov (Jackson)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday) · [NBC, 17 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-17/lue-jackson-to-begin-season-as-starting-center)
- **Quentin Grimes:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger) · [BasketNews, 8 Nov](https://basketnews.com/news-259092-what-happened-to-quentin-grimes-jj-redick-gives-crucial-injury-update-after-lakers-win.html) · [Dan Woike on X, 8 Nov](https://x.com/DanWoikeSports/status/2119609546716889447)
- **Spencer Jones:** [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)
- **T.J. McConnell:** [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-questionable-for-monday-538210/) · [Roundtable via Yahoo, 7 Nov](https://sports.yahoo.com/articles/t-j-mcconnell-cleared-season-203829170.html)
- **Rudy Gobert:** [NBC, 31 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/rudy-gobert-back-downgraded-to-out-saturday) · [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/rudy-gobert-posts-15-rebounds-in-win-over-jazz)
- **Robert Williams III:** [RotoWire, 7 Nov](https://rotowire.com/basketball/headlines/robert-williams-news-resting-versus-spurs-538018) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs) · [CBS/RotoWire, 1 Mar 2026](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-robert-williams-resting-sunday/)
- **Tobias Harris:** [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-tobias-harris-unavailable-against-phoenix/) · [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/tobias-harris-injury-unavailable-against-phoenix-538223) · [Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html) · [Hoops Rumors, 1 Nov](https://www.hoopsrumors.com/2026/11/spurs-notes-harris-wembanyama-castle-fox.html)
- **Jamal Shead:** [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl) · [RotoWire, 6 Nov](https://www.rotowire.com/basketball/headlines/jamal-shead-news-starting-friday-537893) · [Last Word on Sports, 7 Nov](https://lastwordonsports.com/basketball/2026/11/07/raptors-reserves-shead) · [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/barnes-quickley-limited-at-sunday-practice)
- **Klay Thompson:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/klay-thompson-sinks-seven-three-pointers-vs-sac) · [ESPN recap, 8 Nov](https://www.espn.com/nba/recap?gameId=401909951) · [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-thompson-wiggins-larsson-hardaway-conwell-giannis.html)
- **Anthony Davis:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-davis-ankle-questionable-monday-vs-det) · [BasketNews, 8 Nov](https://basketnews.com/news-259082-will-anthony-davis-finally-play-latest-injury-status-revealed-by-wizards.html) · [BasketNews, 5 Nov](https://basketnews.com/news-258907-anthony-davis-injury-update-raises-concerns-for-washington-wizards.html) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/anthony-davis-ankle-downgraded-to-out-saturday)
- **VJ Edgecombe:** [BasketNews, 25 Oct](https://basketnews.com/news-258120-vj-edgecombe-final-status-for-76ers-vs-pistons-revealed.html) · [The Sixer Sense, 28 Oct](https://thesixersense.com/76ers-starting-five-will-reunite-vj-edgecombe-dodged-real-setback)
- **Paolo Banchero:** [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html) · [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182) · [Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)
- Forms for Murray, Barnes, Bane, Duren, Leonard and the new flags: `python council/form.py --ours "Desmond Bane" ...`, read 2026-11-09 06:48 UTC. *ESPN est.* dates: `python council/injuries.py --details`, read 2026-11-09 06:49 UTC. Team game dates: ESPN's `proTeamSchedules_wl`. Matchup figures: [matchup 4, 9 Nov](20261109-matchup4.md).
- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-09 06:47 UTC.
