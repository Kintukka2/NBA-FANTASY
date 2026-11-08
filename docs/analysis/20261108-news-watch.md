# News watch: 08 Nov 2026

- Generated 2026-11-08 20:14 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 51 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 96 on other teams' rosters (injury flags only, except this week's and next week's opponents: Melbourne poopoo, Lauri Birds). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 23 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Jalen Duren (ours): out until at least Sun 22 Nov.** The Pistons cleared him for on-court work on 8 Nov and will re-evaluate him in two weeks ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work); [Hunter Patterson of The Athletic via CBS, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)). Detroit plays at ATL that day, so his first possible game is **Tue 24 Nov at ORL**; *ESPN est.* 24 Nov (it said 9 Nov this morning).
  - He misses all of matchup 4 (9–15 Nov) and matchup 5 (16–22 Nov). This morning's matchup 4 report counted him for 132.2 FP; tonight's run gives him 0.0 and projects **1639 to 1637**.
  - He keeps a bench slot, because Kawhi Leonard holds our only IR slot. His rate (44.1) is a small sample.
  - No override: ESPN's date gives the same first game as the source.
- **Scottie Barnes (ours):** limited in Sunday's practice and **questionable for Mon 9 Nov vs MEM** with left adductor soreness, after missing Friday ([CBS/RotoWire, citing Michael Grange, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/); [HoopsHype, 8 Nov](https://hoopshype.com/story/sports/nba/rumors/2026/11/08/scottie-barnes-immanuel-quickley-to-return-against-grizzlies/92678359007)). No timetable reported beyond Monday; *ESPN est.* 9 Nov.
  - Rate **48.6** · season 45.9 (8) → 50.7 (7) · L7 44.3 (3) · L15 45.2 (6) → 51.8 (5) · L30 45.9 (8) → 50.7 (7) · projected 43.7 (`council/form.py`).
  - Matchup 4 counts all 4 of his games (194.6 FP added), and Monday is one of them. Monday's official reports were not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
- **Kawhi Leonard (ours, IR):** finished treatment for left knee swelling on 3 Nov and began a return-to-play process. The Raptors' next update is due about Tue 10 Nov, with no timetable ([TSN, 3 Nov](https://www.tsn.ca/nba/article/raptors-leonard-completes-knee-swelling-treatment-will-be-evaluated-in-one-week/)). RotoWire: unlikely back before the end of November ([CBS/RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)). *ESPN est.* 23 Nov.
  - Rate **41.7** · season 40.0 (2) · L7 — · L15 — · L30 40.0 (2) · projected 45.8: small sample.
  - No row: a re-evaluation is not a return, and ESPN's date fits the reporting.
- **Anthony Black (ours since 8 Nov, for Aday Mara):** nothing new since Saturday's cramps; Orlando is off until Tue 10 Nov ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)). **Wed 11 Nov at UTAH** is still a rest risk: he sat the second night of the last back-to-back ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)).
- **Paul George (ours):** not on Boston's report for tonight at MIL ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). **Wed 11 Nov at TOR** is still a rest risk, not announced: he sat the second night of the last road–road back-to-back ([NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)).
- **Pickup targets:**
  - **Nic Claxton:** debuts tonight off the bench, held to 16–20 minutes; how long that lasts has not been reported ([ClutchPoints, 8 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-tiago-splitter-nic-claxton-plan-debut-76ers)). His rate (33.3) is last season's, with no games yet.
  - **Robert Williams III:** healthy; ESPN's "rest" label is Saturday's night off on a back-to-back ([RotoWire, 7 Nov](https://rotowire.com/basketball/headlines/robert-williams-news-resting-versus-spurs-538018)). Wed 11 Nov vs OKC is a rest risk.
  - **Kobe Sanders, Deandre Ayton, Mitchell Robinson:** their lineup changes were one-offs or not settled, so their value has not moved ([RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/kobe-sanders-news-headed-to-bench-537595); [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/wizards-start-trae-george-aj-sarr-and-ayton); [Heavy, 8 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-provide-concerning-update-on-mitchell-robinsons-availability-ahead-of-bucks-game/)). Ayton has a left lower-leg injury (no diagnosis, no timetable reported ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday)); *ESPN est.* 9 Nov). Robinson is questionable tonight with an illness (no timetable reported ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday)); *ESPN est.* 8 Nov).
  - **Aday Mara** is on waivers after our drop. Nothing new.
- **ESPN dates corrected this morning still stand,** with no new report on any of them: **Kon Knueppel** back 13 Nov at the earliest ([Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/)), **Yves Missi** 12 Nov ([RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)), **Tobias Harris** 14 Nov ([Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip)); *ESPN est.* 9 Nov for all three.
- **Overrides:** none added or removed tonight. All 5 rows stay in force and none has expired. Duren, Barnes, Leonard, Claxton, Williams, Robinson, Ayton, Davis, Miller and Sanders get no row: their sources match ESPN's date or report no ongoing change.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Kon Knueppel | return | 2026-11-13 | — | [link](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/) | in force |
| Yves Missi | return | 2026-11-12 | — | [link](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773) | in force |
| Tobias Harris | return | 2026-11-14 | — | [link](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Anthony Black** | ORL | us | injury, rest | 42.1 | — | active |
| **Jalen Duren** | DET | us | minutes | 44.1 † | — | out, ESPN est. 24 Nov |
| **Paul George** | BOS | us | rest | 38.1 | — | active |
| **Yves Missi** | NO | free agent | injury | 60.4 † | — | out, ESPN est. 09 Nov |
| **Nic Claxton** | CHI | free agent | injury | 33.3 | — | active |
| **Maxime Raynaud** | SAC | free agent | injury, gap | 28.1 | — | out, ESPN est. 10 Nov |
| **Tobias Harris** | SA | free agent | injury, gap | 28.0 | — | out, ESPN est. 09 Nov |
| **Jalen Suggs** | ORL | free agent | injury, gap | 25.8 | — | out, ESPN est. 10 Nov |
| **Kon Knueppel** | CHA | free agent | injury | 0.4 † | — | out, ESPN est. 09 Nov |
| **CJ McCollum** | ATL | waivers | role | 31.0 | 23.5 | active |
| **Aday Mara** | OKC | waivers | role | 27.8 | 32.0 | active |
| **Kobe Sanders** | LAC | free agent | role, minutes | 27.5 | 30.3 | active |
| **Deandre Ayton** | WSH | free agent | role, rest | 18.3 | 26.1 | day-to-day, ESPN est. 09 Nov |
| **Mitchell Robinson** | BOS | free agent | role, rest | 17.4 | 16.1 | day-to-day, ESPN est. 08 Nov |
| **Spencer Jones** | DEN | free agent | minutes | 29.1 † | — | active |
| **Fred VanVleet** | HOU | free agent | rest | 30.7 | — | active |
| **Robert Williams III** | POR | free agent | rest | 29.3 | — | day-to-day, ESPN est. 10 Nov |
| **Jeremiah Fears** | NO | Melbourne poopoo | minutes | 32.0 | 37.0 | active |
| **Klay Thompson** | MIA | Melbourne poopoo | minutes | 25.2 | 25.4 | active |
| **Anthony Davis** | WSH | Melbourne poopoo | rest | 50.7 | — | day-to-day, ESPN est. 09 Nov |
| **VJ Edgecombe** | PHI | Melbourne poopoo | rest | 35.7 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | injury | 26.0 | — | day-to-day, ESPN est. 09 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Anthony Black (ORL, PG/SG, us)

- Rate **42.1** · season 38.5 (6) → 44.0 (5) · L7 41.0 (3) · L15 38.5 (6) → 44.0 (5) · L30 38.5 (6) → 44.0 (5) · projected 28.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 08 Nov: "Black exited Saturday's 126-119 overtime loss to the Warriors with left leg cramps and did not return, Jason Beede of the Orlando Sentinel reports"
- **Rest:** back-to-back Tue 10–Wed 11 Nov; news on 06 Nov: "Black returned to the starting lineup after sitting out Monday's contest against Washington for ankle injury management"; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Black exited Saturday's 126-119 overtime loss to the Warriors with left leg cramps and did not return, Jason Beede of the Orlando Sentinel reports.
- News (06 Nov): Black ended Thursday's 117-104 loss to the Suns with 10 points (3-8 FG, 1-3 3Pt, 3-4 FT), seven rebounds, six assists and one steal in 31 minutes.
- **Research:**
  - **Since this morning:** no new report. Orlando is off until Tue 10 Nov at SAC, and Saturday's overtime cramps brought no injury designation ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping); [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/anthony-black-news-exits-game-with-cramps-538080)).
  - He is ours from 8 Nov, added for Aday Mara (`council/espn_sync.py`).
  - **Rest:** he sat 2 Nov, the second night of a back-to-back, for "right ankle injury management" ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)), and was off the injury report by 4 Nov.
  - **Tue 10–Wed 11 Nov** (at SAC, at UTAH): **Wed 11 Nov is a rest risk**, not announced.
  - **Verdict:** nothing new found. Active is right. No sit row.

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Minutes:** news on 08 Nov: "23, though he'll remain on the inactive list for at least the next two weeks while ramping up toward a return to game action"
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - **Pistons, Sun 8 Nov:** he "has been cleared to begin on-court activities" and "will be re-evaluated in two weeks" ([NBC Sports, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work)). He stays on the inactive list for at least two more weeks ([CBS/RotoWire, citing Hunter Patterson of The Athletic, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)).
  - Omari Sankofa II (Detroit Free Press): at least another two weeks, so at least a month out in all ([Yahoo, 8 Nov](https://sports.yahoo.com/articles/jalen-duren-miss-least-two-160459329.html)). The update "does not establish a specific return date" ([Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/detroit-pistons-jalen-duren-injury-update-november-8/ddrysdale/detroit-pistons/11/08/2026/505667/)).
  - He is out tonight vs LAL ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - **Dates:** two weeks from 8 Nov is **Sun 22 Nov**, when Detroit plays at ATL. Detroit's next game is **Tue 24 Nov at ORL** (ESPN schedule).
  - **Expected return:** re-evaluation 22 Nov, no return date reported; first possible game 24 Nov; *ESPN est.* 24 Nov.
  - **The minutes flag is a misread:** the "23" the script quotes comes from "a right hamstring strain Oct. 23", his injury date, not a minutes figure.
  - **Verdict:** ESPN confirmed. No override: the rule's date (the day after the re-evaluation, 23 Nov) has no Detroit game, so a row would give the same first game as ESPN. His rate (44.1) is a small sample.

### Paul George (BOS, SF/PF, us)

- Rate **38.1** · season 40.8 (8) · L7 36.7 (3) · L15 37.0 (6) · L30 40.8 (8) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Tue 10–Wed 11 Nov, Sun 15–Mon 16 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (07 Nov): George registered eight points (3-11 FG, 2-5 3Pt), five rebounds, an assist, a steal and two blocks across 22 minutes in Friday's 119-80 win over the Hornets.
- News (04 Nov): George produced 25 points (8-18 FG, 5-9 3Pt, 4-7 FT), three rebounds, five assists and four steals over 35 minutes in Wednesday's 109-102 win over the Bucks.
- **Research:**
  - **Since this morning:** he is not on Boston's list for tonight at MIL ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). No rest has been announced for this week.
  - **2 Nov:** a "planned maintenance day" with no injury ([NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)). It was the second night of a road–road back-to-back (at ORL, at HOU).
  - On more rest days he said "we'll get to that when the time is there" ([Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)).
  - **Tue 10–Wed 11 Nov** (at PHI, at TOR) is road–road again, so **Wed 11 Nov is a rest risk**. 15–16 Nov is at home.
  - **Verdict:** nothing new found. No sit row: nothing has been announced.

## Free agents and waivers

### Yves Missi (NO, C, free agent)

- Rate **60.4** (small sample) · season 41.5 (2) → 68.0 (1) · L7 — · L15 — · L30 41.5 (2) → 68.0 (1) · projected 24.7
- ESPN: out, ESPN est. 09 Nov (Left Knee Bruise, updated 2026-11-05)
- **Injury:** ESPN est. 09 Nov (Out, Left Knee Bruise, updated 05 Nov), but the news said on 05 Nov: "He remains without a timetable to return and can be considered week-to-week moving forward"
- News (05 Nov): Missi (knee) is out for Friday's game against Minnesota.
- News (30 Oct): Missi (knee) won't play in Saturday's game against Atlanta.
- **Research:**
  - **Since this morning:** out tonight at LAC with a left knee contusion and bone bruise ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). No timetable since.
  - Week-to-week with no timetable as of 5 Nov ([RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)).
  - **Expected return:** no timetable reported (week-to-week); *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override (kept):** return 2026-11-12, a floor. His rate rests on one 68-FP game: small sample.

### Nic Claxton (CHI, C, free agent)

- Rate **33.3** · season — · L7 — · L15 — · L30 — · projected 30.3
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 07 Nov: "Claxton (hamstring) has been downgraded to questionable for Sunday's game against the 76ers"
- News (08 Nov): Claxton (hamstring) is available for Sunday's game against Philadelphia and will be limited to 16-20 minutes off the bench, Will Gotlieb of CHGO reports.
- News (07 Nov): Claxton (hamstring) has been downgraded to questionable for Sunday's game against the 76ers.
- **Research:**
  - **Sunday's plan:** Tiago Splitter said Claxton will not start and will play 16–20 minutes in his season debut, with Jalen Smith starting at center ([ClutchPoints, 8 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-tiago-splitter-nic-claxton-plan-debut-76ers)). Will Gotlieb (CHGO) reported the same limit ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-nic-claxton-available-coming-off-bench-sunday/)).
  - The official report lists him **available** for tonight vs PHI ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)), so the 7 Nov questionable tag is out of date.
  - How long the limit and the bench role last has not been reported. RotoWire expects him to take the starting job from Smith "at some point" ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-nic-claxton-available-coming-off-bench-sunday/)).
  - **Verdict:** ESPN confirmed (active). No role row: the 16–20 minutes are a debut limit, not a reported ongoing role, and with no games this season there is no FP-per-minute figure for a role rate. His rate (33.3) is last season's average: no games yet this season.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 10 Nov (Right Knee Dislocated, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee Dislocated, updated 26 Oct), but the news said on 26 Oct: "Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports"
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- News (15 Oct): Raynaud (knee) is expected to miss at least the first five or six games of the regular season, and potentially longer, Frankie Cartoscelli of KHTK Sactown Sports 1140 reports.
- **Research:**
  - **Since this morning:** out tonight vs MIA with a right patella subluxation ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). No report on the re-evaluation yet.
  - The re-evaluation is now "next week" (9–15 Nov) ([Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap); [AP preview, 8 Nov](https://www.1075thegame.com/2026/11/08/heat-look-to-reverse-course-vs-struggling-kings/)).
  - **Expected return:** re-evaluation in the week of 9 Nov, no return date reported; *ESPN est.* 10 Nov, probably early.
  - **Verdict:** ESPN confirmed, as a floor. No row: no source gives a later date.

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 09 Nov (Left Calf Strain, updated 2026-10-30)
- **Injury:** ESPN est. 09 Nov (Out, Left Calf Strain, updated 30 Oct), but the news said on 30 Oct: "The veteran is slowly making progress toward a return, though he should be considered week-to-week until more information is released"
- **Gap:** listed out, and no news in 5 days (ESPN est. 09 Nov)
- News (30 Oct): Harris (calf) is listed as out for Saturday's game against Minnesota.
- News (28 Oct): Harris (calf) is out for Wednesday's game against Utah, Paul Garcia of ProjectSpurs.com reports.
- **Research:**
  - **Since this morning:** nothing new. San Antonio is off tonight, and its report for Mon 9 Nov at PHX was not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - He did an on-court workout, and the staff is "unfortunately conservative", with no timetable ([Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html)). Mitch Johnson: "very, very methodically" ([Heavy, 2 Nov](https://heavy.com/sports/nba/san-antonio-spurs/tobias-harris-gets-disappointing-injury-update/)).
  - Out on 6 and 7 Nov with no timetable ([Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip)).
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override (kept):** return 2026-11-14, a floor 7 days after the latest out report.

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **25.8** · season 26.3 (3) · L7 — · L15 23.0 (1) · L30 26.3 (3) · projected 29.2
- ESPN: out, ESPN est. 10 Nov (Right Knee, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee, updated 26 Oct), but the news said on 26 Oct: "Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports"
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports.
- News (25 Oct): Suggs (knee) did not return to Sunday's game against the Knicks.
- **Research:**
  - **Since this morning:** no report on his two-week re-evaluation, due about 9 Nov; the last report has him out on 7 Nov ([SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)). Orlando's next game is Tue 10 Nov at SAC (ESPN schedule).
  - Mild right knee bone bruise, re-evaluated in two weeks from 26 Oct ([Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html)).
  - He was out on 7 Nov at GSW ([SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)).
  - **Expected return:** re-evaluation about 9 Nov, no return date reported; *ESPN est.* 10 Nov.
  - **Verdict:** ESPN confirmed, as a floor. No row. His L15 rests on one game: noise.

### Kon Knueppel (CHA, SG/SF, free agent)

- Rate **0.4** (small sample) · season -2.0 (1) · L7 -2.0 (1) · L15 -2.0 (1) · L30 -2.0 (1) · projected 35.2
- ESPN: out, ESPN est. 09 Nov (Left Hamstring Strain, updated 2026-11-05)
- **Injury:** ESPN est. 09 Nov (Out, Left Hamstring Strain, updated 05 Nov), but the news said on 05 Nov: "The Hornets haven't yet indicated whether the sharpshooter is facing a multi-week absence, but they'll likely proceed with caution"
- News (05 Nov): Knueppel (hamstring) is out for Friday's game against the Celtics.
- News (04 Nov): Knueppel exited Wednesday's game against the Nets after experiencing soreness in his left leg, and he will not return, Brett Siegel of ClutchPoints.com reports.
- **Research:**
  - **Since this morning:** nothing new. Charlotte's report for Mon 9 Nov vs CLE was not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - Charles Lee (6 Nov): "it's going to take a little bit of time". He would not call it day-to-day or week-to-week ([HoopsHype via Yahoo, 6 Nov](https://sports.yahoo.com/articles/hornets-not-sure-kon-knueppel-231248943.html)).
  - Beat writer Rod Boone: "more than just a few days or even a week before Knueppel is able to go" ([Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/); [HoopsHype via Yahoo, 6 Nov](https://sports.yahoo.com/articles/hornets-not-sure-kon-knueppel-231248943.html)).
  - **Expected return:** no timetable reported, more than a week per the beat writer; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override (kept):** return 2026-11-13, a floor; his first possible game is Sun 15 Nov at LAC.
  - His rate (0.4) rests on one 6-minute game: small sample.

### CJ McCollum (ATL, PG/SG, waivers)

- Rate **31.0** · role rate 23.5 · season 25.9 (11) → 28.0 (10) · L7 27.8 (4) → 35.3 (3) · L15 26.1 (9) → 28.8 (8) · L30 25.9 (11) → 28.0 (10) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 9; 22.0 min in those 2, against 25.7 for the season
- **Role:** news on 04 Nov: "McCollum is not listed in the starting lineup for Wednesday's game against Washington, Brad Rowland of the Locked On Podcast Network reports"
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- News (04 Nov): McCollum is not listed in the starting lineup for Wednesday's game against Washington, Brad Rowland of the Locked On Podcast Network reports.
- **Research:**
  - **Since this morning:** nothing new. No change to the bench role has been reported.
  - He asked Quin Snyder to start rookie Kingston Flemings on 4 Nov ([Heavy, 5 Nov](https://heavy.com/sports/nba/atlanta-hawks/kingston-flemings-first-nba-start-delivers-instant-spark-after-veteran-gesture/); [AJC, Nov](https://www.ajc.com/sports/2026/11/hawks-bump-rookie-flemings-to-starting-lineup-down-wizards/)).
  - He has come off the bench 3 straight games (25, 23 and 21 min) ([RotoWire via CBS, 8 Nov](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role)), and stayed there when Jalen Johnson returned on 7 Nov ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury)).
  - Snyder: "roles change not just game to game" ([Roundtable, 8 Nov](https://roundtable.io/sports/nba/hawks/opinion/4-takeaways-from-hawks-124-121-comeback-win-over-nets)).
  - **L7:** 27.8 (4) → 35.3 (3) is 5+ over his season 25.9 (11) → 28.0 (10) once the 5-FP game of 6 Nov is dropped. The reason is two strong games: 45 FP in his last start on 2 Nov (12 assists in 32 minutes; ESPN's news feed, 3 Nov) and 36 in his first bench game on 4 Nov.
  - **Verdict:** the bench role is ongoing. **Override (kept):** role, 23 min until 22 Nov, so tonight's matchup 4 run uses a role rate of **24.6 ‡** instead of his rate of 31.0.

### Aday Mara (OKC, C, waivers)

- Rate **27.8** · role rate 32.0 · season 24.4 (10) · L7 31.8 (4) · L15 27.0 (8) · L30 24.4 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 8 before; 26.0 min in his starts, against 19.8 for the season
- **Role:** news on 07 Nov: "Mara will start Saturday against the Wizards, Rylan Stiles of SI"
- News (08 Nov): Mara registered 18 points (8-10 FG, 1-1 3Pt, 1-2 FT), eight rebounds, three assists and three blocks in Saturday's 114-75 win over the Wizards.
- News (07 Nov): Mara will start Saturday against the Wizards, Rylan Stiles of SI.com reports.
- **Research:**
  - **Since this morning:** we dropped him on 8 Nov for Anthony Black, so he is on waivers. No new lineup news.
  - **Wed 4 Nov:** he started for Jaylin Williams (back spasms) ([NBC, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/aday-mara-to-make-first-career-start-wednesday)).
  - **Fri 6 Nov:** OKC went small with McCain, and Mara went back to backup center ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/thunder-start-shai-mccain-ajay-kenrich-i-hart)).
  - **Sat 7 Nov:** OKC used a "bigger lineup" and Mara replaced McCain ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart)).
  - So his starts depend on the lineup OKC picks each game, not only on Jaylin Williams being out.
  - **Jaylin Williams:** has missed 3 straight games; his next chance is Tue 10 Nov at POR, and no timetable has been reported ([CBS, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/)); *ESPN est.* 10 Nov.
  - **Minutes:** with Chet Holmgren out ([8–10 weeks from 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan), Mara's backup minutes (18–28) hold, and he plays 25–27 when he starts.
  - **L7:** 31.8 (4) is 5+ over his season 24.4 (10). The reason is his two starts (26.0 min in them, 19.8 for the season), including the 18-point, 8-10 FG game on 7 Nov (News line above).
  - **Verdict:** nothing new found. No role row: his rate stays 27.8, and the role rate (32.0) is the value of a night he starts.

### Kobe Sanders (LAC, SG, free agent)

- Rate **27.5** · role rate 30.3 · season 20.5 (8) → 23.6 (7) · L7 23.0 (3) → 35.0 (2) · L15 21.7 (6) → 26.2 (5) · L30 20.5 (8) → 23.6 (7)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 6 before; 32.5 min in his starts, against 24.4 for the season
- **Minutes:** 30.7 min over his last 3 games against 25.3 for the season (+5.4)
- News (04 Nov): Sanders will come off the bench in Wednesday's game versus Miami, Law Murray of The Athletic reports.
- News (03 Nov): Sanders registered 26 points (8-17 FG, 5-11 3Pt, 5-5 FT), four rebounds, three assists and one block in 38 minutes during Monday's 125-118 loss to Toronto.
- **Research:**
  - **Role:** his 2 Nov start was a spot start for Rui Hachimura (quadriceps), and Hachimura was off the report by 4 Nov ([RotoBaller, Nov](https://www.rotoballer.com/?p=1983441)). On 4 Nov he went back to the bench when Derrick Jones returned ([RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/kobe-sanders-news-headed-to-bench-537595)).
  - Max Strus (foot) made his season debut on 2 Nov ([The Sports Leader, 2 Nov](https://www.thesportsleader.com/2026/11/02/clippers-g-max-strus-foot-set-to-make-season-debut/)). The Clippers list Sanders with Strus and Keaton Wagler as their top bench options for tonight vs NO ([Roundtable via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-injury-report-rules-five-181158053.html)).
  - **Minutes:** the 30.7 leave out his 4 Nov game (dropped as an outlier) and come from 24 min on 30 Oct, 30 on 1 Nov with Strus and Jones out (ESPN's news feed, 2 Nov) and 38 in the spot start. Back on the bench on 4 Nov he played 18.
  - **L7:** 23.0 (3) → 35.0 (2) is a small sample, and half of it is the 26-point spot start.
  - **Verdict:** nothing new found. The start was a one-off and the extra minutes ended with Jones and Strus back. No row.

### Deandre Ayton (WSH, C, free agent)

- Rate **18.3** · role rate 26.1 · season 16.9 (10) · L7 19.0 (4) · L15 16.0 (8) · L30 16.9 (10) · projected 25.3
- ESPN: day-to-day, ESPN est. 09 Nov (Leg, updated 2026-11-08)
- **Role:** started 1 of his last 2 games after 1 of 8 before; 23.5 min in his starts, against 15.1 for the season
- **Role:** news on 06 Nov: "Ayton will start Friday against the Hawks"
- **Rest:** back-to-back Wed 11–Thu 12 Nov, Sun 15–Mon 16 Nov; news on 06 Nov: "Washington will face Oklahoma City on Saturday on the second night of a back-to-back"
- News (07 Nov): Ayton won't return to Saturday's game against the Thunder due to a lower leg injury.
- News (07 Nov): Ayton will come off the bench in Saturday's game against the Thunder.
- **Research:**
  - **Injury:** he left Saturday after 7 minutes, seen grabbing his left calf, and was ruled out with a lower left leg injury. No MRI result or diagnosis has been reported ([NBC/Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday); [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/wizards-deandre-ayton-wont-return-saturday/)). RotoWire calls him questionable for Mon 9 Nov at DET; Washington's report for Monday was not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - In February 2025 a left calf strain cost him at least four weeks ([KNBR](https://www.knbr.com/news/blazers-c-deandre-ayton-calf-strain-out-at-least-4-weeks/)).
  - **Role:** the 6 Nov start was a one-off for Anthony Davis ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/wizards-start-trae-george-aj-sarr-and-ayton)). On 7 Nov Coulibaly started ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/was-starts-young-george-dybantsa-bilal-sarr)). Davis has a right ankle sprain, no timetable reported; *ESPN est.* 9 Nov.
  - **Rest:** a false alarm. The 6 Nov note was about Washington's back-to-back, not about resting Ayton.
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** nothing new found. Healthy, he is a bench player (about 14 min). No row.

### Mitchell Robinson (BOS, C, free agent)

- Rate **17.4** · role rate 16.1 · season 17.2 (8) · L7 15.7 (3) · L15 17.0 (6) · L30 17.2 (8) · projected 30.3
- ESPN: day-to-day, ESPN est. 08 Nov (Illness, updated 2026-11-08)
- **Role:** came off the bench in his last 2 games after starting 5 of 6; 17.5 min in those 2, against 18.8 for the season
- **Rest:** back-to-back Tue 10–Wed 11 Nov, Sun 15–Mon 16 Nov; news on 05 Nov: "After opening the year as a starter, Robinson has now come off the bench in back-to-back games"; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Robinson (illness) is questionable for Sunday's game versus Milwaukee, Bobby Krivitsky of Forbes.com reports.
- News (05 Nov): Robinson provided three points (1-8 FG, 1-2 FT), 10 rebounds, one assist, one block and one steal over 20 minutes during Wednesday's 109-102 victory over the Bucks.
- **Research:**
  - **Injury:** added late as questionable for tonight at MIL with an illness ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday); [Heavy, 8 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-provide-concerning-update-on-mitchell-robinsons-availability-ahead-of-bucks-game/)), and still questionable at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)). No timetable reported beyond tonight; *ESPN est.* 8 Nov.
  - **Role:** Neemias Queta took the starting job on 1 Nov and kept it when Robinson came back; Robinson has played 15, 20 and 15 minutes off the bench since ([Heavy, 8 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-provide-concerning-update-on-mitchell-robinsons-availability-ahead-of-bucks-game/); [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday)).
  - **Rest:** he sat 1 Nov at ORL, the first night of a road back-to-back, to rest ([NBC, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/mitchell-robinson-rest-downgraded-to-out-sunday)); in late October he played both nights of back-to-backs ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday)). Nothing is announced for Tue 10–Wed 11 Nov (at PHI, at TOR) or 15–16 Nov.
  - **Verdict:** nothing new found. No role row: no source calls the bench role settled, and his role rate (16.1) is close to his rate (17.4). No sit row.

### Spencer Jones (DEN, SF/PF, free agent)

- Rate **29.1** (small sample) · season 30.0 (1) · L7 30.0 (1) · L15 30.0 (1) · L30 30.0 (1)
- ESPN: active
- **Minutes:** news on 06 Nov: "He'll challenge Bryce Hopkins and Alpha Diallo for playing time, but Jones is likely to have a minutes cap early on"
- News (08 Nov): Jones had 13 points (5-6 FG, 3-3 3Pt), six rebounds and one block across 21 minutes during Saturday's 114-102 win over the Pacers.
- News (06 Nov): Jones (hamstring) is off the injury report for Saturday's game against Indiana.
- **Research:**
  - **Since this morning:** nothing new.
  - The "minutes cap" was RotoWire's expectation, not a team figure ([CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/)).
  - His debut: 21 min, 13 points on 5-6 FG ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)). One game is a small sample.
  - **Verdict:** the cap is not confirmed. No row.

### Fred VanVleet (HOU, PG/SG, free agent)

- Rate **30.7** · season 32.9 (8) · L7 28.7 (3) · L15 30.0 (6) · L30 32.9 (8) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (08 Nov): VanVleet tallied 16 points (6-12 FG, 4-9 3Pt), three rebounds, four assists and a block across 31 minutes in Saturday's 102-99 loss to the Suns.
- News (01 Nov): VanVleet (knee) isn't listed on the injury report for Monday's game against the Celtics.
- **Research:**
  - **Since this morning:** nothing new. Houston hosts DEN on Mon 9 Nov.
  - He "will sit out one game of back-to-back sets to open the season" (Will Guillory, The Athletic), and Udoka confirmed it ([RotoWire via CBS, 20 Oct](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/)). The plan still stood on 2 Nov ([KMJ, 2 Nov](https://www.kmjnow.com/2026/11/02/fred-vanvleet-expected-to-return-to-lineup-as-rockets-host-celtics/)).
  - The policy follows his September 2025 ACL tear. Both sits were listed as right knee injury management ([NBC, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/fred-vanvleet-knee-removed-from-injury-report)).
  - **Verdict:** confirmed policy. **Override (kept):** sit 2026-11-16, the second night, as on 24 and 31 Oct. It falls in matchup 5, so matchup 4 keeps all 4 of his games.

### Robert Williams III (POR, C, free agent)

- Rate **29.3** · season 28.1 (7) · L7 30.3 (3) · L15 30.2 (5) · L30 28.1 (7) · projected 26.9
- ESPN: day-to-day, ESPN est. 10 Nov (Rest, updated 2026-11-08)
- **Rest:** back-to-back Tue 10–Wed 11 Nov; news on 07 Nov: "Williams (rest) won't play in Saturday's game against the Spurs"
- News (07 Nov): Williams (rest) won't play in Saturday's game against the Spurs.
- News (05 Nov): Williams closed Wednesday's 132-119 victory over the Suns with nine points (4-8 FG, 1-1 FT), eight rebounds, one assist, three blocks and two steals over 16 minutes.
- **Research:**
  - **Rest:** he sat Sat 7 Nov vs SA "to rest", the second night of a back-to-back, after 16 minutes on 6 Nov ([RotoWire, 7 Nov](https://rotowire.com/basketball/headlines/robert-williams-news-resting-versus-spurs-538018); [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs)). No policy for this season has been announced.
  - On 29 Oct he sat vs MEM as a precaution for left knee soreness ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs)). Last season Portland rested him on the second night of back-to-backs for left knee management ([CBS/RotoWire, 1 Mar 2026](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-robert-williams-resting-sunday/)).
  - **Tue 10–Wed 11 Nov** (OKC at home twice): **Wed 11 Nov is a rest risk**, not announced. ESPN's "rest, 10 Nov" label is Saturday's night off; he is healthy for Tuesday.
  - **Verdict:** nothing new found: ESPN's date (his next game) is right. No sit row: nothing has been announced.

## Opponents: this week and next

### Jeremiah Fears (NO, PG/SG, Melbourne poopoo)

- Rate **32.0** · role rate 37.0 · season 29.7 (9) · L7 32.0 (3) · L15 36.3 (7) · L30 29.7 (9) · projected 27.3
- ESPN: active
- **Minutes:** 36.0 min over his last 3 games against 28.9 for the season (+7.1)
- News (06 Nov): Fears finished with 24 points (9-16 FG, 0-1 3Pt, 6-7 FT), five rebounds, five assists and two steals over 36 minutes in Friday's 115-109 loss to Minnesota.
- News (03 Nov): Fears contributed 12 points (5-17 FG, 0-6 3Pt, 2-2 FT), four rebounds and seven assists over 38 minutes during Monday's 135-134 overtime victory over Memphis.
- **Research:**
  - **Since this morning:** nothing new. He plays tonight at LAC, the last day of matchup 3.
  - His recent minutes: 38 on 2 Nov (overtime, Dejounte Murray away), 34 on 4 Nov (Trey Murphy out), and 36 on 6 Nov with both back ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/nor-starts-fears-murray-murphy-zion-matkovic)). Rotoworld: "playing time won't be an issue" ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/jeremiah-fears-scores-team-high-24-points-vs-min)).
  - Only 2 of those games had the full lineup: small sample.
  - **Verdict:** nothing new found. No row: the source is a fantasy analyst, not the team.

### Klay Thompson (MIA, SG/SF, Melbourne poopoo)

- Rate **25.2** · role rate 25.4 · season 20.9 (9) · L7 31.3 (3) · L15 24.4 (7) · L30 20.9 (9) · projected 19.5
- ESPN: active
- **Minutes:** 28.3 min over his last 3 games against 23.3 for the season (+5.0)
- News (06 Nov): Thompson closed with 11 points (3-10 FG, 2-7 3Pt, 3-3 FT), three assists and two blocks over 23 minutes during Thursday's 120-100 loss to the Warriors.
- News (05 Nov): Thompson notched 30 points (11-22 FG, 8-17 3Pt), five rebounds, three assists and one block across 35 minutes during Wednesday's 117-116 overtime win over the Clippers.
- **Research:**
  - **Since this morning:** nothing new. He plays tonight at SAC, the last day of matchup 3.
  - His 35-minute game was the 4 Nov overtime win ([Hot Hot Hoops, 5 Nov](https://hothothoops.com/2026/11/05/heat-complete-20-point-comeback-in-overtime-courtesy-of-a-klay-thompson-game-winner/)). The other two were 27 and 23 min in 20+ point losses.
  - No bigger role has been reported ([Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-thompson-wiggins-larsson-hardaway-conwell-giannis.html)). Expect 23–27 min.
  - **L7:** 31.3 (3) is 5+ over his season 20.9 (9): the overtime game (30 points, 8-17 from three, 35 min; News line above) and 19 points on 7-11 FG on 2 Nov (ESPN's news feed, 3 Nov).
  - **Verdict:** nothing new found. No row.

### Anthony Davis (WSH, PF/C, Melbourne poopoo)

- Rate **50.7** · season 45.9 (8) · L7 58.5 (2) · L15 47.7 (6) · L30 45.9 (8) · projected 49.6
- ESPN: day-to-day, ESPN est. 09 Nov (Right Ankle Sprain, updated 2026-11-08)
- **Rest:** back-to-back Wed 11–Thu 12 Nov, Sun 15–Mon 16 Nov; news on 07 Nov: "After missing Friday's 139-132 loss to Atlanta, Davis is questionable to suit up on the second night of Washington's back-to-back due to a sprained right ankle"
- News (07 Nov): Davis (ankle) won't play Saturday against the Thunder.
- News (07 Nov): Davis (ankle) is questionable for Saturday's game against the Thunder.
- **Research:**
  - **Ankle:** a right ankle sprain from 4 Nov, which he played through ([BasketNews, 5 Nov](https://basketnews.com/news-258907-anthony-davis-injury-update-raises-concerns-for-washington-wizards.html)). He missed 6 and 7 Nov ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/anthony-davis-ankle-downgraded-to-out-saturday); [Wizards on X, 6 Nov](https://x.com/WashWizards/status/2118836740555468813)).
  - His next chance is Mon 9 Nov at DET. There is no Sunday update, and Washington's report for Monday was not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - **Rest:** a false alarm. The note was about his ankle on the second night of Washington's back-to-back, not rest. Nothing is announced for 11–12 or 15–16 Nov.
  - **For us:** Melbourne poopoo is matchup 3's opponent, which ends tonight, and Washington has no game tonight.
  - **L7:** 58.5 (2) is a 2-game window, a small sample: 12-17 and 12-19 shooting nights on 2 and 4 Nov (ESPN's news feed, 3 and 5 Nov).
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** nothing new found. No row.

### VJ Edgecombe (PHI, SG, Melbourne poopoo)

- Rate **35.7** · season 32.9 (9) · L7 39.3 (3) · L15 34.6 (7) · L30 32.9 (9) · projected 33.7
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 24–25 Oct back-to-back, playing the games either side
- News (06 Nov): Edgecombe recorded 19 points (8-13 FG, 3-5 3Pt), three rebounds, two assists and four steals over 32 minutes in Friday's 119-95 loss to the Cavs.
- News (03 Nov): Edgecombe notched 21 points (9-12 FG, 2-4 3Pt, 1-3 FT), three rebounds, five assists, a steal and a block across 33 minutes in Monday's 126-107 win over the Bulls.
- **Research:**
  - **Since this morning:** he is not on Philadelphia's list for tonight at CHI ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - The 25 Oct absence was an abdominal contusion, not rest ([BasketNews, 25 Oct](https://basketnews.com/news-258120-vj-edgecombe-final-status-for-76ers-vs-pistons-revealed.html); [The Sixer Sense, 28 Oct](https://thesixersense.com/76ers-starting-five-will-reunite-vj-edgecombe-dodged-real-setback)).
  - No rest plan has been reported for 15–16 Nov.
  - **L7:** 39.3 (3) is 5+ over his season 32.9 (9). The reason is shooting, not minutes: 8-13 FG with four steals on 6 Nov and 9-12 FG on 2 Nov (News lines above), in his usual 32–35 minutes.
  - **Verdict:** the rest flag is a false alarm.

## Other rosters: injury flags only

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **26.0** · season 30.5 (10) · L7 12.3 (3) · L15 35.0 (8) · L30 30.5 (10) · projected 37.4
- ESPN: day-to-day, ESPN est. 09 Nov (Right Groin Soreness, updated 2026-11-07)
- **Injury:** ESPN est. 09 Nov (Day-To-Day, Right Groin Soreness, updated 07 Nov), but the news said on 06 Nov: "Head coach Charles Lee said Miller (groin) will be re-evaluated over the weekend, and they expect to have more information by Monday, Steve Reed of The Associated Press reports"
- News (06 Nov): Head coach Charles Lee said Miller (groin) will be re-evaluated over the weekend, and they expect to have more information by Monday, Steve Reed of The Associated Press reports.
- News (06 Nov): Miller (groin) won't return to Friday's game against the Celtics, Brett Siegel of ClutchPoints.com reports.
- **Research:**
  - **Since this morning:** no Monday update yet. The Hornets were to evaluate him over the weekend and expected more information on Monday, when they host CLE at 7 p.m. ET ([Here Rock Hill, 8 Nov](https://www.hererockhill.com/2026/11/08/hornets-brandon-miller-groin-injury-evaluation-monday/)). Charlotte's report for Monday was not yet submitted at 3:15 PM ET ([NBA injury report, 8 Nov 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf)).
  - Charles Lee (6 Nov): evaluated over the weekend, with more information Monday ([Yahoo, 7 Nov](https://sports.yahoo.com/articles/charles-lee-provides-discouraging-injury-170413283.html); [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-will-be-re-evaluated-over-the-weekend/)).
  - **L7:** 12.3 (3) is 5+ under his season 30.5 (10): a 2-15 shooting night on 4 Nov (ESPN's news feed, 5 Nov) and the 14-minute groin exit on 6 Nov.
  - **Expected return:** no timetable reported, more information Monday; *ESPN est.* 9 Nov.
  - **Verdict:** nothing new found. ESPN's date is the earliest. No row.

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - **Since this morning:** nothing new.
  - Low-grade right high-ankle sprain, "typically" 4–6 weeks ([Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html)). Banchero himself: "at least a month" ([Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182)).
  - He was out on 7 Nov at GSW ([Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)).
  - **Expected return:** 4–6 weeks from 24 Oct (21 Nov to 5 Dec); *ESPN est.* 22 Nov, the earliest end.
  - **Verdict:** nothing new found. No row. His rate is a small sample.

## Sources

- Research checked on 8 Nov 2026, about 20:30 UTC. Players researched this morning (08:40 UTC) were re-checked for news since then; their earlier links are kept.
- Official: [NBA injury report, 8 Nov 2026, 3:15 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-08_03_15PM.pdf) (Monday's games not yet submitted).
- **Jalen Duren:** [NBC Sports, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) · [Yahoo, 8 Nov](https://sports.yahoo.com/articles/jalen-duren-miss-least-two-160459329.html) · [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/detroit-pistons-jalen-duren-injury-update-november-8/ddrysdale/detroit-pistons/11/08/2026/505667/)
- **Scottie Barnes:** [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/) · [HoopsHype, 8 Nov](https://hoopshype.com/story/sports/nba/rumors/2026/11/08/scottie-barnes-immanuel-quickley-to-return-against-grizzlies/92678359007)
- **Kawhi Leonard:** [TSN, 3 Nov](https://www.tsn.ca/nba/article/raptors-leonard-completes-knee-swelling-treatment-will-be-evaluated-in-one-week/) · [CBS/RotoWire, 3 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-kawhi-leonard-to-be-re-evaluated-in-one-week/)
- **Anthony Black:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping) · [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/anthony-black-news-exits-game-with-cramps-538080) · [Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)
- **Paul George:** [NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets) · [Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)
- **Yves Missi:** [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)
- **Nic Claxton:** [ClutchPoints, 8 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-tiago-splitter-nic-claxton-plan-debut-76ers) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-nic-claxton-available-coming-off-bench-sunday/)
- **Maxime Raynaud:** [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap) · [AP preview, 8 Nov](https://www.1075thegame.com/2026/11/08/heat-look-to-reverse-course-vs-struggling-kings/)
- **Tobias Harris:** [Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html) · [Heavy, 2 Nov](https://heavy.com/sports/nba/san-antonio-spurs/tobias-harris-gets-disappointing-injury-update/) · [Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip)
- **Jalen Suggs:** [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html) · [SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)
- **Kon Knueppel:** [Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/) · [HoopsHype via Yahoo, 6 Nov](https://sports.yahoo.com/articles/hornets-not-sure-kon-knueppel-231248943.html)
- **CJ McCollum:** [Heavy, 5 Nov](https://heavy.com/sports/nba/atlanta-hawks/kingston-flemings-first-nba-start-delivers-instant-spark-after-veteran-gesture/) · [AJC, Nov](https://www.ajc.com/sports/2026/11/hawks-bump-rookie-flemings-to-starting-lineup-down-wizards/) · [RotoWire via CBS, 8 Nov](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury) · [Roundtable, 8 Nov](https://roundtable.io/sports/nba/hawks/opinion/4-takeaways-from-hawks-124-121-comeback-win-over-nets)
- **Aday Mara:** [NBC, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/aday-mara-to-make-first-career-start-wednesday) · [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/thunder-start-shai-mccain-ajay-kenrich-i-hart) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart) · [CBS, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/) · [NBA.com, Holmgren](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear)
- **Kobe Sanders:** [RotoBaller, Nov](https://www.rotoballer.com/?p=1983441) · [RotoWire, 4 Nov](https://www.rotowire.com/basketball/headlines/kobe-sanders-news-headed-to-bench-537595) · [The Sports Leader, 2 Nov](https://www.thesportsleader.com/2026/11/02/clippers-g-max-strus-foot-set-to-make-season-debut/) · [Roundtable via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-injury-report-rules-five-181158053.html)
- **Deandre Ayton:** [NBC/Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday) · [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/wizards-deandre-ayton-wont-return-saturday/) · [KNBR, Feb 2025](https://www.knbr.com/news/blazers-c-deandre-ayton-calf-strain-out-at-least-4-weeks/) · [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/wizards-start-trae-george-aj-sarr-and-ayton) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/was-starts-young-george-dybantsa-bilal-sarr)
- **Mitchell Robinson:** [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/mitchell-robinson-illness-questionable-sunday) · [Heavy, 8 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-provide-concerning-update-on-mitchell-robinsons-availability-ahead-of-bucks-game/) · [NBC, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/mitchell-robinson-rest-downgraded-to-out-sunday)
- **Spencer Jones:** [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)
- **Fred VanVleet:** [RotoWire via CBS, 20 Oct](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) · [KMJ, 2 Nov](https://www.kmjnow.com/2026/11/02/fred-vanvleet-expected-to-return-to-lineup-as-rockets-host-celtics/) · [NBC, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/fred-vanvleet-knee-removed-from-injury-report)
- **Robert Williams III:** [RotoWire, 7 Nov](https://rotowire.com/basketball/headlines/robert-williams-news-resting-versus-spurs-538018) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs) · [CBS/RotoWire, 1 Mar 2026](https://www.cbssports.com/fantasy/basketball/news/trail-blazers-robert-williams-resting-sunday/)
- **Jeremiah Fears:** [NBC, 6 Nov (lineup)](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/nor-starts-fears-murray-murphy-zion-matkovic) · [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/jeremiah-fears-scores-team-high-24-points-vs-min)
- **Klay Thompson:** [Hot Hot Hoops, 5 Nov](https://hothothoops.com/2026/11/05/heat-complete-20-point-comeback-in-overtime-courtesy-of-a-klay-thompson-game-winner/) · [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-thompson-wiggins-larsson-hardaway-conwell-giannis.html)
- **Anthony Davis:** [BasketNews, 5 Nov](https://basketnews.com/news-258907-anthony-davis-injury-update-raises-concerns-for-washington-wizards.html) · [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/anthony-davis-ankle-downgraded-to-out-saturday) · [Wizards on X, 6 Nov](https://x.com/WashWizards/status/2118836740555468813)
- **VJ Edgecombe:** [BasketNews, 25 Oct](https://basketnews.com/news-258120-vj-edgecombe-final-status-for-76ers-vs-pistons-revealed.html) · [The Sixer Sense, 28 Oct](https://thesixersense.com/76ers-starting-five-will-reunite-vj-edgecombe-dodged-real-setback)
- **Brandon Miller:** [Here Rock Hill, 8 Nov](https://www.hererockhill.com/2026/11/08/hornets-brandon-miller-groin-injury-evaluation-monday/) · [Yahoo, 7 Nov](https://sports.yahoo.com/articles/charles-lee-provides-discouraging-injury-170413283.html) · [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-will-be-re-evaluated-over-the-weekend/)
- **Paolo Banchero:** [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html) · [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182) · [Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)
- Forms for Barnes and Leonard: `python council/form.py "Scottie Barnes" "Kawhi Leonard"`, read 2026-11-08 20:31 UTC. Matchup figures: tonight's `council/matchup.py` run (20:14 UTC) and this morning's `docs/analysis/20261108-matchup4.md`.
- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-08 20:14 UTC.
