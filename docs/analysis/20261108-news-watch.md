# News watch: 08 Nov 2026

- Generated 2026-11-08 08:39 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 49 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 96 on other teams' rosters (injury flags only, except this week's and next week's opponents: Melbourne poopoo, Lauri Birds). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 18 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Jalen Duren (ours):** re-evaluated today (The Athletic). ESPN's 9 Nov is the earliest possible date; Thu 12 Nov looks likelier. No timetable reported; *ESPN est.* 9 Nov.
- **Aday Mara (ours):** his starts depend on which lineup OKC picks each game; no source calls the role ongoing.
  - His rate stays **28.1**. A night he starts is worth about **32.0** (role rate).
  - L7 32.6 (5) against a season of 24.4 (10): the two starts.
- **Paul George (ours):** sat 2 Nov as a planned maintenance day. **Wed 11 Nov at TOR** is the same road–road back-to-back: a rest risk, not announced.
- **Pickup targets:**
  - **Anthony Black:** left Saturday with cramps, no injury designation, and is expected for Tue 10 Nov. Wed 11 Nov is a rest risk (he sat 2 Nov for ankle management).
  - **CJ McCollum:** now a bench player (role rate 24.6 ‡, from 29.7). He drops out of contention.
  - **Fred VanVleet:** sits one night of every back-to-back. Matchup 4 keeps all 4 of his games; he sits Mon 16 Nov.
- **ESPN dates corrected:**
  - **Kon Knueppel:** back 13 Nov at the earliest; ESPN said 9 Nov.
  - **Yves Missi:** back 12 Nov at the earliest; ESPN said 9 Nov.
  - **Tobias Harris:** back 14 Nov at the earliest; ESPN said 9 Nov.
  - `matchup.py` now uses these dates.
- **Overrides added:** 5 (table below). None for Duren, Mara, Suggs, Raynaud, Miller or Banchero: their sources confirm ESPN's date as a floor, or report no ongoing change.

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
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 09 Nov |
| **Aday Mara** | OKC | us | role | 28.1 | 32.0 | active |
| **Paul George** | BOS | us | rest | 37.9 | — | active |
| **Yves Missi** | NO | free agent | injury | 60.4 † | — | out, ESPN est. 09 Nov |
| **Anthony Black** | ORL | waivers | injury, rest | 42.1 | — | active |
| **Jalen Suggs** | ORL | free agent | injury, gap | 28.4 | — | out, ESPN est. 10 Nov |
| **Maxime Raynaud** | SAC | free agent | injury, gap | 28.1 | — | out, ESPN est. 10 Nov |
| **Tobias Harris** | SA | free agent | injury, gap | 28.0 | — | out, ESPN est. 09 Nov |
| **Kon Knueppel** | CHA | free agent | injury | 0.4 † | — | out, ESPN est. 09 Nov |
| **CJ McCollum** | ATL | waivers | role | 29.7 | 23.5 | active |
| **Deandre Ayton** | WSH | free agent | role | 18.3 | 26.1 | out, ESPN est. 09 Nov |
| **Spencer Jones** | DEN | free agent | minutes | 29.1 † | — | active |
| **Fred VanVleet** | HOU | free agent | rest | 31.1 | — | active |
| **Jeremiah Fears** | NO | Melbourne poopoo | minutes | 31.9 | 37.0 | active |
| **Klay Thompson** | MIA | Melbourne poopoo | minutes | 24.6 | 25.4 | active |
| **VJ Edgecombe** | PHI | Melbourne poopoo | rest | 34.9 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | injury | 28.2 | — | day-to-day, ESPN est. 09 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 23.0 (1) → — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 09 Nov (Right Hamstring Strain, updated 2026-10-25)
- **Injury:** ESPN est. 09 Nov (Out, Right Hamstring Strain, updated 25 Oct), but the news said on 25 Oct: "Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints"
- **Gap:** listed out, and no news in 5 days (ESPN est. 09 Nov)
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- News (24 Oct): Duren has been ruled out for Sunday's game against the 76ers due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - The Athletic's Hunter Patterson reports that Detroit's medical staff re-evaluates him **Sun 8 Nov**, and stresses that a re-evaluation is not a return ([Detroit Sports Nation, 5 Nov](https://detroitsportsnation.com/jalen-duren-hamstring-checkup-pistons-paul-reed/gkaplan/detroit-pistons/11/05/2026/505091/)).
  - He did dribbling and shooting work on 5 Nov and is "progressing well" ([Detroit News via Yahoo, 5 Nov](https://sports.yahoo.com/articles/watch-pistons-jalen-duren-appears-202712092.html)).
  - He is ruled out for Sunday vs LAL ([Pistons On SI via Yahoo, 7 Nov](https://sports.yahoo.com/articles/pistons-vs-lakers-starting-lineups-230650051.html)). Thu 12 Nov vs WSH looks likelier than Mon 9 Nov.
  - **Expected return:** re-evaluation 8 Nov, no return date reported; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN confirmed, as the earliest date. The gap flag is a false alarm: there was news on 5 and 7 Nov that ESPN's feed did not carry.
  - No override: it would repeat ESPN's date. His rate is a small sample.

### Aday Mara (OKC, C, us)

- Rate **28.1** · role rate 32.0 · season 24.4 (10) · L7 32.6 (5) · L15 27.0 (8) · L30 24.4 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 8 before; 26.0 min in his starts, against 19.8 for the season
- **Role:** news on 07 Nov: "Mara will start Saturday against the Wizards, Rylan Stiles of SI"
- News (07 Nov): Mara will start Saturday against the Wizards, Rylan Stiles of SI.com reports.
- News (06 Nov): Mara isn't listed in the starting lineup for Friday's game against the Grizzlies, Clemente Almanza of USA Today reports.
- **Research:**
  - **Wed 4 Nov:** he started for Jaylin Williams (back spasms) ([NBC, 4 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-04/aday-mara-to-make-first-career-start-wednesday)).
  - **Fri 6 Nov:** OKC went small with McCain, and Mara went back to backup center ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/thunder-start-shai-mccain-ajay-kenrich-i-hart)).
  - **Sat 7 Nov:** OKC used a "bigger lineup" and Mara replaced McCain ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart)).
  - So his starts depend on the lineup OKC picks each game, not only on Jaylin Williams being out.
  - **Jaylin Williams:** has missed 3 straight games; his next chance is Tue 10 Nov at POR, and no timetable has been reported ([CBS, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/)); *ESPN est.* 10 Nov.
  - **Minutes:** with Chet Holmgren out ([8–10 weeks from 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan), Mara's backup minutes (18–28) hold, and he plays 25–27 when he starts.
  - **L7:** 32.6 is 8.2 over his season average. The reason is his two starts and more minutes (26.0 in his starts, 19.8 for the season).
  - **Verdict:** nothing new found. The role is not ongoing, so there is no role row: his rate stays 28.1, and the role rate (32.0) is the value of a night he starts.

### Paul George (BOS, SF/PF, us)

- Rate **37.9** · season 40.8 (8) · L7 36.7 (3) · L15 36.3 (7) · L30 40.8 (8) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Tue 10–Wed 11 Nov, Sun 15–Mon 16 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (07 Nov): George registered eight points (3-11 FG, 2-5 3Pt), five rebounds, an assist, a steal and two blocks across 22 minutes in Friday's 119-80 win over the Hornets.
- News (04 Nov): George produced 25 points (8-18 FG, 5-9 3Pt, 4-7 FT), three rebounds, five assists and four steals over 35 minutes in Wednesday's 109-102 win over the Bucks.
- **Research:**
  - **2 Nov:** a "planned maintenance day" with no injury ([NBC, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)). It was the second night of a road–road back-to-back (at ORL, at HOU).
  - On more rest days he said "we'll get to that when the time is there" ([Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)).
  - **Tue 10–Wed 11 Nov** (at PHI, at TOR) is road–road again, so **Wed 11 Nov is a rest risk**. 15–16 Nov is at home.
  - **Verdict:** nothing new found. No sit row: nothing has been announced.

## Free agents and waivers

### Yves Missi (NO, C, free agent)

- Rate **60.4** (small sample) · season 41.5 (2) → 68.0 (1) · L7 — · L15 15.0 (1) → — · L30 41.5 (2) → 68.0 (1) · projected 24.7
- ESPN: out, ESPN est. 09 Nov (Left Knee Bruise, updated 2026-11-05)
- **Injury:** ESPN est. 09 Nov (Out, Left Knee Bruise, updated 05 Nov), but the news said on 05 Nov: "He remains without a timetable to return and can be considered week-to-week moving forward"
- News (05 Nov): Missi (knee) is out for Friday's game against Minnesota.
- News (30 Oct): Missi (knee) won't play in Saturday's game against Atlanta.
- **Research:**
  - Week-to-week with no timetable as of 5 Nov (left knee bone bruise) ([RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)).
  - The Pelicans' own preview lists him out for Sun 8 Nov at LAC ([NBA.com, 7 Nov](https://www.nba.com/pelicans/news/pelicans-vs-clippers-injury-report-game-preview-11-8-2026)).
  - **Expected return:** no timetable reported (week-to-week); *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override:** return 2026-11-12, a floor. His rate rests on one 68-FP game: small sample.

### Anthony Black (ORL, PG/SG, waivers)

- Rate **42.1** · season 38.5 (6) → 44.0 (5) · L7 41.0 (3) · L15 38.5 (6) → 44.0 (5) · L30 38.5 (6) → 44.0 (5) · projected 28.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 08 Nov: "Black exited Saturday's 126-119 overtime loss to the Warriors with left leg cramps and did not return, Jason Beede of the Orlando Sentinel reports"
- **Rest:** back-to-back Tue 10–Wed 11 Nov; news on 06 Nov: "Black returned to the starting lineup after sitting out Monday's contest against Washington for ankle injury management"; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Black exited Saturday's 126-119 overtime loss to the Warriors with left leg cramps and did not return, Jason Beede of the Orlando Sentinel reports.
- News (06 Nov): Black ended Thursday's 117-104 loss to the Suns with 10 points (3-8 FG, 1-3 3Pt, 3-4 FT), seven rebounds, six assists and one steal in 31 minutes.
- **Research:**
  - He left in overtime with cramping, and no injury designation was given ([NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)). Orlando is off until Tue 10 Nov at SAC ([RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/anthony-black-news-exits-game-with-cramps-538080)).
  - **Rest:** he sat 2 Nov, the second night of a back-to-back, for "right ankle injury management" ([Jason Beede on X, 2 Nov](https://x.com/therealBeede/status/2117301046213066914)), and was off the injury report by 4 Nov.
  - **Tue 10–Wed 11 Nov** (at SAC, at UTAH): **Wed 11 Nov is a rest risk**.
  - **Verdict:** nothing new found. Active is right. No sit row.

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **28.4** · season 26.3 (3) · L7 — · L15 29.5 (2) · L30 26.3 (3) · projected 29.2
- ESPN: out, ESPN est. 10 Nov (Right Knee, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee, updated 26 Oct), but the news said on 26 Oct: "Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports"
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports.
- News (25 Oct): Suggs (knee) did not return to Sunday's game against the Knicks.
- **Research:**
  - Mild right knee bone bruise, re-evaluated in two weeks from 26 Oct ([Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html)).
  - He was out on 7 Nov at GSW ([SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)). There is no report on the re-evaluation yet.
  - **Expected return:** re-evaluation about 9 Nov, no return date reported; *ESPN est.* 10 Nov.
  - **Verdict:** ESPN confirmed, as a floor. No row.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 10 Nov (Right Knee Dislocated, updated 2026-10-26)
- **Injury:** ESPN est. 10 Nov (Out, Right Knee Dislocated, updated 26 Oct), but the news said on 26 Oct: "Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports"
- **Gap:** listed out, and no news in 5 days (ESPN est. 10 Nov)
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- News (15 Oct): Raynaud (knee) is expected to miss at least the first five or six games of the regular season, and potentially longer, Frankie Cartoscelli of KHTK Sactown Sports 1140 reports.
- **Research:**
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
  - He did an on-court workout, and the staff is "unfortunately conservative", with no timetable ([Express-News via Yahoo, 29 Oct](https://sports.yahoo.com/articles/spurs-harris-reaches-benchmark-recovery-132710180.html)). Mitch Johnson: "very, very methodically" ([Heavy, 2 Nov](https://heavy.com/sports/nba/san-antonio-spurs/tobias-harris-gets-disappointing-injury-update/)).
  - Out on 6 and 7 Nov with no timetable ([Air Alamo, 7 Nov](https://airalamo.com/spurs-trail-blazers-injury-report-no-ja-morant-tobias-harris-out-and-more-to-know-before-tip)).
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override:** return 2026-11-14, a floor 7 days after the latest out report.

### Kon Knueppel (CHA, SG/SF, free agent)

- Rate **0.4** (small sample) · season -2.0 (1) · L7 -2.0 (1) · L15 -2.0 (1) · L30 -2.0 (1) · projected 35.2
- ESPN: out, ESPN est. 09 Nov (Left Hamstring Strain, updated 2026-11-05)
- **Injury:** ESPN est. 09 Nov (Out, Left Hamstring Strain, updated 05 Nov), but the news said on 05 Nov: "The Hornets haven't yet indicated whether the sharpshooter is facing a multi-week absence, but they'll likely proceed with caution"
- News (05 Nov): Knueppel (hamstring) is out for Friday's game against the Celtics.
- News (04 Nov): Knueppel exited Wednesday's game against the Nets after experiencing soreness in his left leg, and he will not return, Brett Siegel of ClutchPoints.com reports.
- **Research:**
  - Charles Lee (6 Nov): "it's going to take a little bit of time". He would not call it day-to-day or week-to-week.
  - Beat writer Rod Boone: "more than just a few days or even a week before Knueppel is able to go" ([Heavy, 6 Nov](https://heavy.com/sports/nba/charlotte-hornets/how-long-kon-knueppel-out-injury-return-timeline-after-new-hornets-injury/); [HoopsHype via Yahoo, 6 Nov](https://sports.yahoo.com/articles/hornets-not-sure-kon-knueppel-231248943.html)).
  - **Expected return:** no timetable reported, more than a week per the beat writer; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN corrected. **Override:** return 2026-11-13, a floor; his first possible game is Sun 15 Nov at LAC.
  - His rate (0.4) rests on one 6-minute game: small sample.

### CJ McCollum (ATL, PG/SG, waivers)

- Rate **29.7** · role rate 23.5 · season 25.9 (11) → 28.0 (10) · L7 26.8 (5) → 32.2 (4) · L15 25.5 (10) → 27.8 (9) · L30 25.9 (11) → 28.0 (10) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 9; 22.0 min in those 2, against 25.7 for the season
- **Role:** news on 04 Nov: "McCollum is not listed in the starting lineup for Wednesday's game against Washington, Brad Rowland of the Locked On Podcast Network reports"
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- News (04 Nov): McCollum is not listed in the starting lineup for Wednesday's game against Washington, Brad Rowland of the Locked On Podcast Network reports.
- **Research:**
  - He asked Quin Snyder to start rookie Kingston Flemings on 4 Nov ([Heavy, 5 Nov](https://heavy.com/sports/nba/atlanta-hawks/kingston-flemings-first-nba-start-delivers-instant-spark-after-veteran-gesture/)).
  - He has come off the bench 3 straight games (25, 23 and 21 min) ([RotoWire via CBS, 8 Nov](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role)), and stayed there when Jalen Johnson returned on 7 Nov ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/jalen-johnson-scores-30-in-return-from-injury)).
  - Snyder: "roles change not just game to game" ([Roundtable, 8 Nov](https://roundtable.io/sports/nba/hawks/opinion/4-takeaways-from-hawks-124-121-comeback-win-over-nets)).
  - **Verdict:** the bench role is ongoing. **Override:** role, 23 min until 22 Nov, so the plans use a role rate of **24.6 ‡** instead of his rate of 29.7.

### Deandre Ayton (WSH, C, free agent)

- Rate **18.3** · role rate 26.1 · season 16.9 (10) · L7 19.0 (4) · L15 15.8 (9) · L30 16.9 (10) · projected 25.3
- ESPN: out, ESPN est. 09 Nov (Leg, updated 2026-11-08)
- **Role:** started 1 of his last 2 games after 1 of 8 before; 23.5 min in his starts, against 15.1 for the season
- **Role:** news on 06 Nov: "Ayton will start Friday against the Hawks"
- News (07 Nov): Ayton won't return to Saturday's game against the Thunder due to a lower leg injury.
- News (07 Nov): Ayton will come off the bench in Saturday's game against the Thunder.
- **Research:**
  - He left on 7 Nov after 7 minutes with a left lower-leg (calf) injury and did not return. No diagnosis has been given ([NBC/Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/deandre-ayton-leg-will-not-return-saturday); [Heavy, 7 Nov](https://heavy.com/sports/nba/washington-wizards/bad-injury-news-emerge/)).
  - The 6 Nov start was a one-off for Anthony Davis ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/wizards-start-trae-george-aj-sarr-and-ayton)). Davis has a right ankle sprain, no timetable reported; *ESPN est.* 9 Nov. On 7 Nov Coulibaly started ([NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/was-starts-young-george-dybantsa-bilal-sarr)).
  - **Expected return:** no timetable reported; *ESPN est.* 9 Nov.
  - **Verdict:** nothing new found. Healthy, he is a bench player (about 14 min). No row.

### Spencer Jones (DEN, SF/PF, free agent)

- Rate **29.1** (small sample) · season 30.0 (1) · L7 30.0 (1) · L15 30.0 (1) · L30 30.0 (1)
- ESPN: active
- **Minutes:** news on 06 Nov: "He'll challenge Bryce Hopkins and Alpha Diallo for playing time, but Jones is likely to have a minutes cap early on"
- News (08 Nov): Jones had 13 points (5-6 FG, 3-3 3Pt), six rebounds and one block across 21 minutes during Saturday's 114-102 win over the Pacers.
- News (06 Nov): Jones (hamstring) is off the injury report for Saturday's game against Indiana.
- **Research:**
  - The "minutes cap" was RotoWire's expectation, not a team figure ([CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-absent-from-injury-report/)).
  - His debut: 21 min, 13 points on 5-6 FG ([CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)). One game is a small sample.
  - **Verdict:** the cap is not confirmed. No row.

### Fred VanVleet (HOU, PG/SG, free agent)

- Rate **31.1** · season 32.9 (8) · L7 28.7 (3) · L15 31.3 (7) · L30 32.9 (8) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (01 Nov): VanVleet (knee) isn't listed on the injury report for Monday's game against the Celtics.
- News (31 Oct): VanVleet (knee) won't play Saturday against the Thunder.
- **Research:**
  - He "will sit out one game of back-to-back sets to open the season" (Will Guillory, The Athletic), and Udoka confirmed it ([RotoWire via CBS, 20 Oct](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/)). The plan still stood on 2 Nov ([KMJ, 2 Nov](https://www.kmjnow.com/2026/11/02/fred-vanvleet-expected-to-return-to-lineup-as-rockets-host-celtics/)).
  - The policy follows his September 2025 ACL tear. Both sits were listed as right knee injury management ([NBC, 1 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-01/fred-vanvleet-knee-removed-from-injury-report)).
  - **Verdict:** confirmed policy. **Override:** sit 2026-11-16, the second night, as on 24 and 31 Oct. It falls in matchup 5, so matchup 4 keeps all 4 of his games.

## Opponents: this week and next

### Jeremiah Fears (NO, PG/SG, Melbourne poopoo)

- Rate **31.9** · role rate 37.0 · season 29.7 (9) · L7 34.8 (4) · L15 32.6 (8) · L30 29.7 (9) · projected 27.3
- ESPN: active
- **Minutes:** 36.0 min over his last 3 games against 28.9 for the season (+7.1)
- News (06 Nov): Fears finished with 24 points (9-16 FG, 0-1 3Pt, 6-7 FT), five rebounds, five assists and two steals over 36 minutes in Friday's 115-109 loss to Minnesota.
- News (03 Nov): Fears contributed 12 points (5-17 FG, 0-6 3Pt, 2-2 FT), four rebounds and seven assists over 38 minutes during Monday's 135-134 overtime victory over Memphis.
- **Research:**
  - His recent minutes: 38 on 2 Nov (overtime, Dejounte Murray away), 34 on 4 Nov (Trey Murphy out), and 36 on 6 Nov with both back ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/nor-starts-fears-murray-murphy-zion-matkovic)). Rotoworld: "playing time won't be an issue" ([NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/jeremiah-fears-scores-team-high-24-points-vs-min)).
  - Only 2 of those games had the full lineup: small sample.
  - No row: the source is a fantasy analyst, not the team.

### Klay Thompson (MIA, SG/SF, Melbourne poopoo)

- Rate **24.6** · role rate 25.4 · season 20.9 (9) · L7 31.3 (3) · L15 22.2 (8) · L30 20.9 (9) · projected 19.5
- ESPN: active
- **Minutes:** 28.3 min over his last 3 games against 23.3 for the season (+5.0)
- News (06 Nov): Thompson closed with 11 points (3-10 FG, 2-7 3Pt, 3-3 FT), three assists and two blocks over 23 minutes during Thursday's 120-100 loss to the Warriors.
- News (05 Nov): Thompson notched 30 points (11-22 FG, 8-17 3Pt), five rebounds, three assists and one block across 35 minutes during Wednesday's 117-116 overtime win over the Clippers.
- **Research:**
  - His 35-minute game was the 4 Nov overtime win ([Hot Hot Hoops, 5 Nov](https://hothothoops.com/2026/11/05/heat-complete-20-point-comeback-in-overtime-courtesy-of-a-klay-thompson-game-winner/)). The other two were 27 and 23 min in 20+ point losses.
  - No bigger role has been reported ([Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/heat-notes-thompson-wiggins-larsson-hardaway-conwell-giannis.html)). Expect 23–27 min.
  - **Verdict:** nothing new found. No row.

### VJ Edgecombe (PHI, SG, Melbourne poopoo)

- Rate **34.9** · season 32.9 (9) · L7 37.0 (4) · L15 34.6 (7) · L30 32.9 (9) · projected 33.7
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 24–25 Oct back-to-back, playing the games either side
- News (06 Nov): Edgecombe recorded 19 points (8-13 FG, 3-5 3Pt), three rebounds, two assists and four steals over 32 minutes in Friday's 119-95 loss to the Cavs.
- News (03 Nov): Edgecombe notched 21 points (9-12 FG, 2-4 3Pt, 1-3 FT), three rebounds, five assists, a steal and a block across 33 minutes in Monday's 126-107 win over the Bulls.
- **Research:**
  - The 25 Oct absence was an abdominal contusion, not rest ([BasketNews, 25 Oct](https://basketnews.com/news-258120-vj-edgecombe-final-status-for-76ers-vs-pistons-revealed.html); [The Sixer Sense, 28 Oct](https://thesixersense.com/76ers-starting-five-will-reunite-vj-edgecombe-dodged-real-setback)).
  - No rest plan has been reported for 15–16 Nov.
  - **Verdict:** the rest flag is a false alarm.

## Other rosters: injury flags only

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **28.2** · season 30.5 (10) · L7 21.5 (4) · L15 32.0 (9) · L30 30.5 (10) · projected 37.4
- ESPN: day-to-day, ESPN est. 09 Nov (Right Groin Soreness, updated 2026-11-07)
- **Injury:** ESPN est. 09 Nov (Day-To-Day, Right Groin Soreness, updated 07 Nov), but the news said on 06 Nov: "Head coach Charles Lee said Miller (groin) will be re-evaluated over the weekend, and they expect to have more information by Monday, Steve Reed of The Associated Press reports"
- News (06 Nov): Head coach Charles Lee said Miller (groin) will be re-evaluated over the weekend, and they expect to have more information by Monday, Steve Reed of The Associated Press reports.
- News (06 Nov): Miller (groin) won't return to Friday's game against the Celtics, Brett Siegel of ClutchPoints.com reports.
- **Research:**
  - Charles Lee (6 Nov): he will be evaluated over the weekend, with more information Monday ([Yahoo, 7 Nov](https://sports.yahoo.com/articles/charles-lee-provides-discouraging-injury-170413283.html); [CBS/RotoWire, 6 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-will-be-re-evaluated-over-the-weekend/)). His next game is Mon 9 Nov vs CLE.
  - **Expected return:** re-evaluation this weekend, no return date reported; *ESPN est.* 9 Nov.
  - **Verdict:** ESPN confirmed, as the earliest date. No row.

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 29.0 (1) → — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Low-grade right high-ankle sprain, "typically" 4–6 weeks ([Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html)). Banchero himself: "at least a month" ([Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182)).
  - He was out on 7 Nov at GSW ([Yahoo, 7 Nov](https://sports.yahoo.com/articles/warriors-vs-magic-injury-report-200718919.html)).
  - **Expected return:** 4–6 weeks from 24 Oct (21 Nov to 5 Dec); *ESPN est.* 22 Nov, the earliest end.
  - **Verdict:** nothing new found. No row.

## Sources

- Research links are in each player's **Research** bullets above, collected by four research agents on 8 Nov 2026 and checked against the override sources.
- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-08 08:39 UTC.
