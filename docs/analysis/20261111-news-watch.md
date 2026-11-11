# News watch: 11 Nov 2026

- Generated 2026-11-11 21:10 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 50 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 98 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 27 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Yves Missi | return | 2026-11-12 | — | [link](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://cbssports.com/fantasy/basketball/news/hawks-cj-mccollum-continues-in-bench-role) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Trey Murphy III** | NO | us | rest | 34.6 | — | day-to-day, ESPN est. 11 Nov |
| **Yves Missi** | NO | free agent | injury, gap | 60.4 † | — | out, ESPN est. 16 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 15 Nov |
| **Jalen Suggs** | ORL | free agent | injury | 27.7 | — | out, ESPN est. 16 Nov |
| **Daniss Jenkins** | DET | free agent | role | 31.5 | 40.1 | active |
| **Aday Mara** | OKC | free agent | role | 30.0 | 32.4 | active |
| **CJ McCollum** | ATL | free agent | role | 29.7 | 24.5 | active |
| **Grayson Allen** | CHA | free agent | role | 29.4 | 28.0 | active |
| **Collin Murray-Boyles** | TOR | free agent | role, minutes | 28.7 | 30.9 | day-to-day, ESPN est. 11 Nov |
| **Saddiq Bey** | NO | free agent | role | 28.4 | 24.7 | active |
| **Quentin Grimes** | LAL | free agent | role | 15.4 | 22.3 | out, ESPN est. 15 Nov |
| **Kevin Huerter** | DET | free agent | minutes | 28.3 | 28.7 | active |
| **T.J. McConnell** | IND | free agent | minutes | 9.6 † | — | day-to-day, ESPN est. 11 Nov |
| **Rudy Gobert** | MIN | free agent | rest | 30.4 | — | active |
| **Robert Williams III** | POR | free agent | rest | 28.1 | — | active |
| **Jamal Shead** | TOR | Lauri Birds | role, minutes | 31.7 | 37.7 | active |
| **Stephen Curry** | GS | Lauri Birds | rest | 50.4 | — | active |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 49.2 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 41.0 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 40.7 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 35.0 | — | day-to-day, ESPN est. 11 Nov |
| **Fred VanVleet** | HOU | Snow Time Lakers | rest | 28.2 | — | active |
| **Jaxson Hayes** | UTAH | Snow Time Lakers | rest | 24.3 | — | active |
| **Giannis Antetokounmpo** | MIA | Dr White Slong | injury | 59.2 | — | active |
| **Austin Reaves** | LAL | Cream Abdul-Yammar | injury | 41.7 | — | active |
| **Zion Williamson** | NO | Melbourne poopoo | injury | 40.7 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Trey Murphy III (NO, SG/SF, us)

- Rate **34.6** · season 31.0 (9) · L7 38.5 (2) · L15 32.5 (6) · L30 31.0 (9) · projected 36.8
- ESPN: day-to-day, ESPN est. 11 Nov (Knee Tendinitis, updated 2026-11-11)
- **Rest:** back-to-back Fri 13–Sat 14 Nov; news on 11 Nov: "If the sharpshooter is ruled out, it'll be his third absence over the past five games, with only one of them coming during a back-to-back set."
- News (11 Nov): Murphy (knee) is doubtful for Wednesday's game against the Nets.
- News (10 Nov): Murphy (knee) is probable for Wednesday's game against the Nets.
- **Research:** _pending_

## Free agents and waivers

### Yves Missi (NO, C, free agent)

- Rate **60.4** (small sample) · season 41.5 (2) → 68.0 (1) · L7 — · L15 — · L30 41.5 (2) → 68.0 (1) · projected 24.7
- ESPN: out, ESPN est. 16 Nov (Left Knee Bruise, updated 2026-11-05)
- **Injury:** ESPN est. 16 Nov (Out, Left Knee Bruise, updated 05 Nov), but the news said on 05 Nov: "He remains without a timetable to return and can be considered week-to-week moving forward."
- **Gap:** listed out, and no news in 5 days (ESPN est. 16 Nov)
- News (05 Nov): Missi (knee) is out for Friday's game against Minnesota.
- News (30 Oct): Missi (knee) won't play in Saturday's game against Atlanta.
- **Research:** _pending_

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 15 Nov (Right Knee Dislocated, updated 2026-11-10)
- **Injury:** ESPN est. 15 Nov (Out, Right Knee Dislocated, updated 10 Nov), but the news said on 09 Nov: "Raynaud is expected to be re-evaluated soon, though he can be considered week-to-week until the Kings offer an update on his status."
- News (09 Nov): Raynaud (knee) has been ruled out for Tuesday's game against Orlando.
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- **Research:** _pending_

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **27.7** · season 26.3 (3) · L7 — · L15 — · L30 26.3 (3) · projected 29.2
- ESPN: out, ESPN est. 16 Nov (Right Knee, updated 2026-11-09)
- **Injury:** ESPN est. 16 Nov (Out, Right Knee, updated 09 Nov), but the news said on 09 Nov: "The Magic said that Suggs' return will depend on how his knee responds to increased on-court activities, so he can be considered week-to-week until the the team provides another update on his progress."
- News (09 Nov): Suggs (knee) has been ruled out for Tuesday's game against the Kings.
- News (26 Oct): Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports.
- **Research:** _pending_

### Daniss Jenkins (DET, PG, free agent)

- Rate **31.5** · role rate 40.1 · season 28.1 (10) · L7 40.0 (3) · L15 27.9 (7) · L30 28.1 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 8 before; 37.0 min in his starts, against 25.9 for the season
- **Role:** news on 09 Nov: "Jenkins is in the starting lineup for Monday's game against the Wizards."
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- News (09 Nov): Jenkins is in the starting lineup for Monday's game against the Wizards.
- **Research:** _pending_

### Aday Mara (OKC, C, free agent)

- Rate **30.0** · role rate 32.4 · season 25.4 (11) · L7 34.2 (4) · L15 30.5 (8) · L30 25.4 (11)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 9 before; 26.0 min in his starts, against 20.4 for the season
- **Role:** news on 10 Nov: "Mara is not listed in the starting lineup for Tuesday's game against the Trail Blazers, Brandon Rahbar of DailyThunder.com reports."
- News (11 Nov): Mara had 10 points (5-9 FG, 0-1 FT), 10 rebounds, two assists and one block in 26 minutes during Tuesday's 123-103 loss to Portland.
- News (10 Nov): Mara is not listed in the starting lineup for Tuesday's game against the Trail Blazers, Brandon Rahbar of DailyThunder.com reports.
- **Research:** _pending_

### CJ McCollum (ATL, PG/SG, free agent)

- Rate **29.7** · role rate 24.5 · season 26.3 (12) → 28.3 (11) · L7 24.2 (4) → 30.7 (3) · L15 26.9 (9) → 29.6 (8) · L30 26.3 (12) → 28.3 (11) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 10; 22.5 min in those 2, against 25.6 for the season
- News (10 Nov): McCollum supplied 21 points (8-15 FG, 3-5 3Pt, 2-2 FT), four assists and one block in 24 minutes during Monday's 124-114 loss to the Lakers.
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **29.4** · role rate 28.0 · season 26.7 (11) · L7 34.3 (3) · L15 26.0 (8) · L30 26.7 (11) · projected 26.6
- ESPN: active
- **Role:** started 2 of his last 2 games after 0 of 9 before; 28.0 min in his starts, against 26.7 for the season
- News (09 Nov): Allen finished with 27 points (8-14 FG, 6-12 3Pt, 5-6 FT), four rebounds, six assists and two steals across 34 minutes during Monday's 124-112 win over Cleveland.
- News (06 Nov): Allen will start in Friday's game against the Celtics
- **Research:** _pending_

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **28.7** · role rate 30.9 · season 24.4 (9) · L7 36.0 (2) · L15 25.7 (6) · L30 24.4 (9) · projected 24.8
- ESPN: day-to-day, ESPN est. 11 Nov (Illness, updated 2026-11-10)
- **Role:** started 2 of his last 2 games after 1 of 7 before; 28.3 min in his starts, against 22.2 for the season
- **Minutes:** 28.3 min over his last 3 games against 22.2 for the season (+6.1)
- News (10 Nov): Murray-Boyles (illness) is questionable for Wednesday's game against the Celtics.
- News (09 Nov): Murray-Boyles (illness) is out for Monday's game against the Grizzlies, Esfandiar Baraheni of The Athletic reports.
- **Research:** _pending_

### Saddiq Bey (NO, SF/PF, free agent)

- Rate **28.4** · role rate 24.7 · season 27.5 (11) · L7 28.0 (4) · L15 28.9 (8) · L30 27.5 (11) · projected 25.9
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 9 before; 24.0 min in his starts, against 26.6 for the season
- **Role:** news on 09 Nov: "Bey will start Monday's game against the Warriors, Rod Walker of The Times-Picayune reports."
- News (09 Nov): Bey will start Monday's game against the Warriors, Rod Walker of The Times-Picayune reports.
- News (07 Nov): Bey recorded 17 points (5-13 FG, 3-6 3Pt, 4-4 FT), five rebounds, four assists and one block over 31 minutes off the bench during Friday's 115-109 loss to the Timberwolves.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **15.4** · role rate 22.3 · season 16.6 (11) · L7 12.7 (3) · L15 14.5 (8) · L30 16.6 (11) · projected 28.1
- ESPN: out, ESPN est. 15 Nov (Finger, updated 2026-11-11)
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 26.1 for the season
- **Role:** news on 08 Nov: "Grimes will start Sunday's game against the Pistons."
- News (11 Nov): Grimes (finger) has been ruled out for Wednesday's game against the Bucks.
- News (10 Nov): Grimes (finger) is listed as questionable for Wednesday's game in Milwaukee.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.3** · role rate 28.7 · season 22.5 (10) · L7 37.0 (3) · L15 26.0 (7) · L30 22.5 (10) · projected 22.9
- ESPN: active
- **Minutes:** 29.3 min over his last 3 games against 23.1 for the season (+6.2)
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- News (05 Nov): Huerter supplied eight points (3-8 FG, 2-6 3Pt) and two blocks over 20 minutes during Wednesday's 112-106 loss to the 76ers.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **9.6** (small sample) · season 8.5 (2) · L7 8.5 (2) · L15 8.5 (2) · L30 8.5 (2) · projected 24.4
- ESPN: day-to-day, ESPN est. 11 Nov (Hamstring, updated 2026-11-10)
- **Minutes:** news on 08 Nov: "The veteran floor general played limited minutes but was productive."
- News (10 Nov): McConnell is questionable for Wednesday's game against the Wizards due to a strained right hamstring.
- News (09 Nov): McConnell (hamstring) is available for Monday's game against Dallas, Dustin Dopirak of The Indianapolis Star reports.
- **Research:** _pending_

### Rudy Gobert (MIN, C, free agent)

- Rate **30.4** · season 26.9 (10) · L7 33.7 (3) · L15 28.6 (7) · L30 26.9 (10) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:** _pending_

### Robert Williams III (POR, C, free agent)

- Rate **28.1** · season 26.2 (8) · L7 31.0 (3) · L15 27.3 (6) · L30 26.2 (8) · projected 26.9
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 09 Nov: "Williams (rest) isn't listed on the injury report ahead of Tuesday's game against the Thunder."; sat the second night of the 06–07 Nov back-to-back, playing the games either side
- News (09 Nov): Williams (rest) isn't listed on the injury report ahead of Tuesday's game against the Thunder.
- News (07 Nov): Williams (rest) won't play in Saturday's game against the Spurs.
- **Research:** _pending_

## Opponents: this week and next

### Jamal Shead (TOR, PG, Lauri Birds)

- Rate **31.7** · role rate 37.7 · season 26.1 (10) · L7 39.0 (3) · L15 32.4 (7) · L30 26.1 (10) · projected 20.7
- ESPN: active
- **Role:** started 2 of his last 2 games after 0 of 8 before; 35.0 min in his starts, against 24.2 for the season
- **Minutes:** 30.0 min over his last 3 games against 24.2 for the season (+5.8)
- News (09 Nov): Shead delivered 20 points (6-17 FG, 4-10 3Pt, 4-4 FT), two rebounds, 11 assists and two steals across 36 minutes during Monday's 118-102 loss to the Grizzlies.
- News (06 Nov): Shead delivered 10 points (4-10 FG, 1-5 3Pt, 1-2 FT), three rebounds, 16 assists and two steals in Friday's 121-107 win over the Bucks.
- **Research:** _pending_

### Stephen Curry (GS, PG, Lauri Birds)

- Rate **50.4** · season 49.2 (9) · L7 50.0 (3) · L15 54.0 (7) · L30 49.2 (9) · projected 43.0
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (10 Nov): Curry ended Monday's 138-87 victory over New Orleans with 25 points (6-10 FG, 4-7 3Pt, 9-9 FT), five rebounds and two assists across 21 minutes.
- News (07 Nov): Curry popped off for 41 points (13-19 FG, 5-10 3Pt, 10-10 FT), six rebounds and six assists over 36 minutes in Saturday's 126-119 overtime win over Orlando.
- **Research:** _pending_

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **49.2** · season 47.0 (12) → 50.2 (11) · L7 50.5 (4) · L15 46.9 (9) · L30 47.0 (12) → 50.2 (11) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 10 Nov: "He scored at least 20 points for the third time this year and the first time since back-to-back such performances to begin the campaign."
- News (10 Nov): Kessler recorded 21 points (8-12 FG, 5-6 FT), 10 rebounds, four assists, one block and one steal in 30 minutes during Monday's 124-114 victory over the Hawks.
- News (09 Nov): Kessler supplied 12 points (5-10 FG, 2-3 FT), 16 rebounds, four assists, three blocks and one steal over 29 minutes during Sunday's 121-116 win over the Pistons.
- **Research:** _pending_

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **41.0** · season 40.0 (11) · L7 40.5 (4) · L15 41.7 (7) · L30 40.0 (11) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- News (08 Nov): Brown totaled 29 points (11-22 FG, 2-6 3Pt, 5-8 FT), seven rebounds, four assists and one steal across 35 minutes during Sunday's 127-121 victory over the Bulls.
- **Research:** _pending_

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **40.7** · season 40.6 (9) · L7 38.5 (4) · L15 42.9 (7) · L30 40.6 (9) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 14–Sun 15 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (10 Nov): Irving delivered 35 points (11-18 FG, 7-10 3Pt, 6-7 FT) and four assists across 38 minutes in Monday's 125-122 win over the Pacers.
- News (09 Nov): Irving delivered 21 points (9-15 FG, 2-7 3Pt, 1-1 FT), three rebounds, four assists and one steal across 29 minutes in Sunday's 130-93 win over the Nets.
- **Research:** _pending_

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.0** · season 36.6 (10) · L7 32.7 (3) · L15 35.9 (7) · L30 36.6 (10) · projected 38.8
- ESPN: day-to-day, ESPN est. 11 Nov (Right Knee Bruise, updated 2026-11-11)
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 09 Nov: "If the veteran guard is ultimately ruled out for the front end of this back-to-back set, Brayden Burries and Ryan Rollins would likely see expanded roles."
- News (11 Nov): Herro (knee) is listed as questionable for Wednesday's game against the Lakers.
- News (10 Nov): Herro (knee) is listed as out for Tuesday's game against New York.
- **Research:** _pending_

### Fred VanVleet (HOU, PG/SG, Snow Time Lakers)

- Rate **28.2** · season 31.1 (9) · L7 24.7 (3) · L15 27.9 (7) · L30 31.1 (9) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (10 Nov): VanVleet finished with 12 points (4-9 FG, 3-6 3Pt, 1-2 FT), a rebound and two assists across 30 minutes in Monday's 110-100 win over the Nuggets.
- News (08 Nov): VanVleet tallied 16 points (6-12 FG, 4-9 3Pt), three rebounds, four assists and a block across 31 minutes in Saturday's 102-99 loss to the Suns.
- **Research:** _pending_

### Jaxson Hayes (UTAH, C, Snow Time Lakers)

- Rate **24.3** · season 27.5 (10) · L7 22.2 (4) · L15 24.0 (7) · L30 27.5 (10) · projected 16.5
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 09 Nov: "On that note, he's played at least 28 minutes in back-to-back games, so his playing time seems to be trending up."; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (09 Nov): Hayes posted 18 points (6-6 FG, 6-7 FT), six rebounds, an assist and a block across 29 minutes in Sunday's 115-100 loss to the Timberwolves.
- News (05 Nov): Hayes closed with two points (1-2 FG), seven rebounds, one assist and one block in 21 minutes before fouling out of Wednesday's 120-113 overtime loss to New Orleans.
- **Research:** _pending_

## Other rosters: injury flags only

### Giannis Antetokounmpo (MIA, PF/C, Dr White Slong)

- Rate **59.2** · season 58.4 (11) → 61.9 (10) · L7 55.0 (4) · L15 62.5 (8) · L30 58.4 (11) → 61.9 (10) · projected 57.6
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 10 Nov: "Antetokounmpo (wrist) is questionable for Tuesday's game against the Jazz."
- News (10 Nov): Antetokounmpo racked up 30 points (12-21 FG, 1-2 3Pt, 5-9 FT), 11 rebounds and four assists over 31 minutes in Tuesday's 115-109 win over the Jazz.
- News (10 Nov): Antetokounmpo (wrist) is available for Tuesday's game against Utah.
- **Research:** _pending_

### Austin Reaves (LAL, PG/SG, Cream Abdul-Yammar)

- Rate **41.7** · season 38.8 (11) → 41.8 (10) · L7 44.0 (3) · L15 35.0 (8) → 38.7 (7) · L30 38.8 (11) → 41.8 (10) · projected 43.3
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 09 Nov: "Reaves (illness) has been ruled out for Monday's game against Atlanta, Benjamin Royer of The Orange County Register reports."
- News (10 Nov): Reaves (illness) is off the injury report for Wednesday's game against the Bucks, Ryan Ward of SI.com reports.
- News (09 Nov): Reaves (illness) has been ruled out for Monday's game against Atlanta, Benjamin Royer of The Orange County Register reports.
- **Research:** _pending_

### Zion Williamson (NO, PF/C, Melbourne poopoo)

- Rate **40.7** · season 42.3 (10) · L7 37.0 (3) · L15 43.9 (7) · L30 42.3 (10) · projected 40.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 09 Nov: "Williamson (rest) is out for Monday's game against the Warriors."
- News (10 Nov): Williamson (rest) is off the injury report for Wednesday's game against the Nets.
- News (09 Nov): Williamson (rest) is out for Monday's game against the Warriors.
- **Research:** _pending_

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-11 21:10 UTC.
