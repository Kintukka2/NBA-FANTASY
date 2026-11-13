# News watch: 12 Nov 2026

- Generated 2026-11-13 04:38 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 49 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 30 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Yves Missi | return | 2026-11-18 | — | [link](https://www.nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-for-tuesday/) | in force |
| Nic Claxton | role | 18 | 2026-11-16 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Daniss Jenkins** | DET | us | role, minutes | 37.0 | 41.4 | active |
| **Dejounte Murray** | NO | us | minutes | 23.2 | 24.0 | active |
| **Paul George** | BOS | us | rest | 41.5 | — | day-to-day, ESPN est. 15 Nov |
| **Trey Murphy III** | NO | us | rest | 34.6 | — | day-to-day, ESPN est. 13 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 15 Nov |
| **Aday Mara** | OKC | free agent | role, minutes | 29.1 | 33.2 | active |
| **Grayson Allen** | CHA | free agent | role | 28.5 | 29.5 | active |
| **CJ McCollum** | ATL | free agent | role | 28.4 | 24.5 | active |
| **Quentin Grimes** | LAL | free agent | role, rest | 16.3 | 22.3 | day-to-day, ESPN est. 15 Nov |
| **Caleb Wilson** | CHI | waivers | minutes | 31.2 | 26.1 | out, ESPN est. 13 Dec |
| **Collin Murray-Boyles** | TOR | free agent | minutes | 28.2 | 30.8 | active |
| **Kevin Huerter** | DET | free agent | minutes | 27.5 | 28.7 | active |
| **T.J. McConnell** | IND | free agent | minutes | 16.0 | — | day-to-day, ESPN est. 13 Nov |
| **Rudy Gobert** | MIN | free agent | rest | 29.1 | — | active |
| **Draymond Green** | GS | free agent | rest | 27.7 | — | active |
| **Meleek Thomas** | CLE | free agent | rest | 27.0 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Tyler Herro** | MIL | Snow Time Lakers | injury, rest | 35.3 | — | active |
| **Paul Reed** | DET | Lauri Birds | role | 29.4 | 34.9 | active |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 47.8 | — | active |
| **Deni Avdija** | POR | Snow Time Lakers | rest | 45.9 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 38.5 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 37.8 | — | active |
| **Fred VanVleet** | HOU | Snow Time Lakers | rest | 33.2 | — | active |
| **Jaxson Hayes** | UTAH | Snow Time Lakers | rest | 25.8 | — | active |
| **Karl-Anthony Towns** | NY | Melbourne poopoo | injury | 52.4 | — | active |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | injury | 33.9 | — | day-to-day, ESPN est. 13 Nov |
| **Keyonte George** | UTAH | Cream Abdul-Yammar | injury | 32.9 | — | active |
| **Joel Embiid** | PHI | Dr White Slong | injury | 31.1 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Daniss Jenkins (DET, PG, us)

- Rate **37.0** · role rate 41.4 · season 29.3 (11) · L7 52.0 (3) · L15 31.9 (7) · L30 29.3 (11)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 9 before; 38.7 min in his starts, against 27.4 for the season
- **Role:** news on 09 Nov: "Jenkins is in the starting lineup for Monday's game against the Wizards."
- **Minutes:** 36.7 min over his last 3 games against 27.4 for the season (+9.3)
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- News (09 Nov): Jenkins is in the starting lineup for Monday's game against the Wizards.
- **Research:** _pending_

### Dejounte Murray (NO, PG/SG, us)

- Rate **23.2** · role rate 24.0 · season 30.6 (9) · L7 14.5 (4) · L15 21.7 (6) · L30 30.6 (9) · projected 39.0
- ESPN: active
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (09 Nov): Murray registered six points (1-6 FG, 0-1 3Pt, 4-4 FT), three rebounds and three assists across 28 minutes during Sunday's 139-123 loss to the Clippers.
- News (05 Nov): Murray ended Wednesday's 120-113 overtime win over Utah with 20 points (4-7 FG, 1-3 3Pt, 11-11 FT), eight rebounds, four assists and four steals across 44 minutes.
- **Research:** _pending_

### Paul George (BOS, SF/PF, us)

- Rate **41.5** · season 42.7 (10) · L7 39.7 (3) · L15 43.5 (6) · L30 42.7 (10) · projected 38.5
- ESPN: day-to-day, ESPN est. 15 Nov (Illness, updated 2026-11-12)
- **Rest:** back-to-back Sun 15–Mon 16 Nov; news on 11 Nov: "George will sit out the second leg of this back-to-back set due to an illness, and his next opportunity to play will come Sunday against the Mavericks."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- News (10 Nov): George tallied 36 points (14-22 FG, 6-11 3Pt, 2-2 FT), five rebounds and one assist across 30 minutes during Tuesday's 123-101 win over Philadelphia.
- **Research:** _pending_

### Trey Murphy III (NO, SG/SF, us)

- Rate **34.6** · season 31.0 (9) · L7 38.5 (2) · L15 32.5 (6) · L30 31.0 (9) · projected 36.8
- ESPN: day-to-day, ESPN est. 13 Nov (Knee Tendinitis, updated 2026-11-12)
- **Rest:** back-to-back Fri 13–Sat 14 Nov; news on 11 Nov: "If the sharpshooter is ruled out, it'll be his third absence over the past five games, with only one of them coming during a back-to-back set."
- News (12 Nov): Murphy (knees) is listed as doubtful for Friday's game against the Grizzlies.
- News (11 Nov): Murphy (knee) is listed as out for Wednesday's game against the Nets.
- **Research:** _pending_

## Free agents and waivers

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 15 Nov (Right Knee Dislocated, updated 2026-11-10)
- **Injury:** ESPN est. 15 Nov (Out, Right Knee Dislocated, updated 10 Nov), but the news said on 09 Nov: "Raynaud is expected to be re-evaluated soon, though he can be considered week-to-week until the Kings offer an update on his status."
- News (09 Nov): Raynaud (knee) has been ruled out for Tuesday's game against Orlando.
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- **Research:** _pending_

### Aday Mara (OKC, C, free agent)

- Rate **29.1** · role rate 33.2 · season 25.3 (12) · L7 32.5 (4) · L15 29.6 (8) · L30 25.3 (12)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 10 before; 28.0 min in his starts, against 21.3 for the season
- **Role:** news on 11 Nov: "Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports."
- **Minutes:** 28.3 min over his last 3 games against 21.3 for the season (+7.0)
- News (11 Nov): Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports.
- News (11 Nov): Mara had 10 points (5-9 FG, 0-1 FT), 10 rebounds, two assists and one block in 26 minutes during Tuesday's 123-103 loss to Portland.
- **Research:** _pending_

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **28.5** · role rate 29.5 · season 26.9 (12) · L7 30.0 (3) · L15 27.8 (8) · L30 26.9 (12) · projected 26.6
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 30.0 min in his starts, against 27.3 for the season
- News (09 Nov): Allen finished with 27 points (8-14 FG, 6-12 3Pt, 5-6 FT), four rebounds, six assists and two steals across 34 minutes during Monday's 124-112 win over Cleveland.
- News (06 Nov): Allen will start in Friday's game against the Celtics
- **Research:** _pending_

### CJ McCollum (ATL, PG/SG, free agent)

- Rate **28.4** · role rate 24.5 · season 26.3 (12) → 28.3 (11) · L7 20.3 (3) → 28.0 (2) · L15 25.1 (8) → 28.0 (7) · L30 26.3 (12) → 28.3 (11) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 10; 22.5 min in those 2, against 25.6 for the season
- News (10 Nov): McCollum supplied 21 points (8-15 FG, 3-5 3Pt, 2-2 FT), four assists and one block in 24 minutes during Monday's 124-114 loss to the Lakers.
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- **Research:** _pending_

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **16.3** · role rate 22.3 · season 16.6 (11) · L7 14.0 (2) · L15 16.3 (7) · L30 16.6 (11) · projected 28.1
- ESPN: day-to-day, ESPN est. 15 Nov (Finger, updated 2026-11-12)
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 26.1 for the season
- **Role:** news on 08 Nov: "Grimes will start Sunday's game against the Pistons."
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 11 Nov: "However, it appears that absence wasn't simply due to rest during the second night of a back-to-back set, as Grimes will now miss a second straight game after previously being listed as questionable."
- News (11 Nov): Grimes (finger) has been ruled out for Wednesday's game against the Bucks.
- News (10 Nov): Grimes (finger) is listed as questionable for Wednesday's game in Milwaukee.
- **Research:** _pending_

### Caleb Wilson (CHI, SF, waivers)

- Rate **31.2** · role rate 26.1 · season 34.9 (10) · L7 25.0 (2) · L15 33.5 (6) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:** _pending_

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **28.2** · role rate 30.8 · season 24.8 (11) · L7 34.0 (3) · L15 25.9 (8) · L30 24.8 (11) · projected 24.8
- ESPN: active
- **Minutes:** 28.7 min over his last 3 games against 22.9 for the season (+5.8)
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- News (11 Nov): Murray-Boyles (illness) will play in Wednesday's game against the Celtics, Josh Lewenberg of TSN.ca reports.
- **Research:** _pending_

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **27.5** · role rate 28.7 · season 21.6 (11) · L7 36.0 (3) · L15 25.4 (7) · L30 21.6 (11) · projected 22.9
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 23.2 for the season (+7.5)
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- News (05 Nov): Huerter supplied eight points (3-8 FG, 2-6 3Pt) and two blocks over 20 minutes during Wednesday's 112-106 loss to the 76ers.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **16.0** · season 15.3 (3) · L7 15.3 (3) · L15 15.3 (3) · L30 15.3 (3) · projected 24.4
- ESPN: day-to-day, ESPN est. 13 Nov (Right Hamstring Strain, updated 2026-11-12)
- **Minutes:** news on 08 Nov: "The veteran floor general played limited minutes but was productive."
- News (12 Nov): McConnell is probable for Friday's game against the Knicks due to a right hamstring strain.
- News (11 Nov): McConnell (hamstring) is available for Wednesday's game versus Washington.
- **Research:** _pending_

### Rudy Gobert (MIN, C, free agent)

- Rate **29.1** · season 27.3 (11) · L7 29.3 (3) · L15 28.9 (7) · L30 27.3 (11) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:** _pending_

### Draymond Green (GS, PF/C, free agent)

- Rate **27.7** · season 25.0 (10) · L7 30.0 (4) · L15 28.4 (7) · L30 25.0 (10) · projected 28.5
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 08 Nov: "His season-high 13 assists and four combined defensive stats provided substantial category-league value, and it's worth noting he's now dished out double-digit assists in back-to-back games."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Green recorded two points (1-5 FG, 0-1 3Pt, 0-2 FT), six rebounds, 13 assists, two steals and two blocks across 34 minutes in Saturday's 126-119 overtime win over the Magic.
- News (07 Nov): Green (elbow) is available for Saturday's game against the Magic.
- **Research:** _pending_

### Meleek Thomas (CLE, SG, free agent)

- Rate **27.0** · season 25.6 (9) · L7 29.5 (4) · L15 25.6 (8) · L30 25.6 (9)
- ESPN: active
- **Rest:** back-to-back Fri 13–Sat 14 Nov; sat the second night of the 28–29 Oct back-to-back, playing the games either side
- News (09 Nov): Thomas tallied 18 points (7-12 FG, 4-6 3Pt), three rebounds, three assists, two steals and two blocks across 27 minutes in Monday's 124-112 loss to the Hornets.
- News (09 Nov): Thomas won't start Monday's game against the Hornets, Serena Winters of FanDuel Sports Network Ohio reports.
- **Research:** _pending_

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:** _pending_

## Opponents: this week and next

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.3** · season 37.1 (11) · L7 34.3 (3) · L15 34.1 (7) · L30 37.1 (11) · projected 38.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Herro (knee) is listed as questionable for Wednesday's game against the Lakers."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 09 Nov: "If the veteran guard is ultimately ruled out for the front end of this back-to-back set, Brayden Burries and Ryan Rollins would likely see expanded roles."; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- News (11 Nov): Herro (knee) is listed as available for Wednesday's game against the Lakers.
- **Research:** _pending_

### Paul Reed (DET, PF/C, Lauri Birds)

- Rate **29.4** · role rate 34.9 · season 31.7 (11) · L7 28.7 (3) · L15 29.0 (7) · L30 31.7 (11) · projected 20.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 7 of 9; 29.5 min in those 2, against 27.1 for the season
- News (09 Nov): Reed will come off the bench Monday against Washington, Eric Vincent of ClutchPoints.com reports.
- News (09 Nov): Reed produced eight points (4-8 FG, 0-2 FT) and 10 rebounds in 20 minutes during Sunday's 121-116 loss to the Lakers.
- **Research:** _pending_

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **47.8** · season 46.5 (13) → 49.3 (12) · L7 46.2 (4) · L15 48.3 (9) · L30 46.5 (13) → 49.3 (12) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 10 Nov: "He scored at least 20 points for the third time this year and the first time since back-to-back such performances to begin the campaign."
- News (12 Nov): Kessler logged 10 points (5-10 FG), 11 rebounds, three assists, one block and one steal over 29 minutes during Wednesday's 123-112 victory over the Bucks.
- News (10 Nov): Kessler recorded 21 points (8-12 FG, 5-6 FT), 10 rebounds, four assists, one block and one steal in 30 minutes during Monday's 124-114 victory over the Hawks.
- **Research:** _pending_

### Deni Avdija (POR, SF/PF, Snow Time Lakers)

- Rate **45.9** · season 41.5 (11) → 43.9 (10) · L7 41.8 (4) → 50.0 (3) · L15 40.5 (8) → 43.9 (7) · L30 41.5 (11) → 43.9 (10) · projected 40.4
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 12 Nov: "The star forward was coming off another impressive outing in the first leg of this back-to-back set against the Thunder, notching 24 points (8-15 FG, 2-4 3Pt, 6-8 FT), six rebounds, eight assists and one steal in 34 minutes during Tuesday's 123-103 win."
- News (12 Nov): Avdija tallied 28 points (9-20 FG, 4-13 3Pt, 6-6 FT), three rebounds, six assists, four steals and two blocks across 35 minutes in Wednesday's 118-108 win over the Thunder.
- News (11 Nov): Avdija recorded 24 points (8-15 FG, 2-4 3Pt, 6-8 FT), six rebounds, eight assists and one steal in 34 minutes during Tuesday's 123-103 win over the Thunder.
- **Research:** _pending_

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **38.5** · season 39.2 (12) · L7 35.0 (4) · L15 40.2 (8) · L30 39.2 (12) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- News (08 Nov): Brown totaled 29 points (11-22 FG, 2-6 3Pt, 5-8 FT), seven rebounds, four assists and one steal across 35 minutes during Sunday's 127-121 victory over the Bulls.
- **Research:** _pending_

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **37.8** · season 38.8 (10) · L7 33.5 (4) · L15 40.1 (7) · L30 38.8 (10) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 14–Sun 15 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (10 Nov): Irving delivered 35 points (11-18 FG, 7-10 3Pt, 6-7 FT) and four assists across 38 minutes in Monday's 125-122 win over the Pacers.
- News (09 Nov): Irving delivered 21 points (9-15 FG, 2-7 3Pt, 1-1 FT), three rebounds, four assists and one steal across 29 minutes in Sunday's 130-93 win over the Nets.
- **Research:** _pending_

### Fred VanVleet (HOU, PG/SG, Snow Time Lakers)

- Rate **33.2** · season 33.1 (10) · L7 33.0 (3) · L15 33.6 (7) · L30 33.1 (10) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; news on 12 Nov: "VanVleet did get held out for the second game of a back-to-back during that period, something that will likely continue to happen all season."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (12 Nov): VanVleet had 18 points (6-9 FG, 4-7 3Pt, 2-2 FT), two rebounds, six assists and three steals over 30 minutes during Wednesday's 115-108 victory over Golden State.
- News (10 Nov): VanVleet finished with 12 points (4-9 FG, 3-6 3Pt, 1-2 FT), a rebound and two assists across 30 minutes in Monday's 110-100 win over the Nuggets.
- **Research:** _pending_

### Jaxson Hayes (UTAH, C, Snow Time Lakers)

- Rate **25.8** · season 27.4 (11) · L7 26.5 (4) · L15 24.2 (8) · L30 27.4 (11) · projected 16.5
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 09 Nov: "On that note, he's played at least 28 minutes in back-to-back games, so his playing time seems to be trending up."; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (09 Nov): Hayes posted 18 points (6-6 FG, 6-7 FT), six rebounds, an assist and a block across 29 minutes in Sunday's 115-100 loss to the Timberwolves.
- News (05 Nov): Hayes closed with two points (1-2 FG), seven rebounds, one assist and one block in 21 minutes before fouling out of Wednesday's 120-113 overtime loss to New Orleans.
- **Research:** _pending_

## Other rosters: injury flags only

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **52.4** · season 48.4 (11) → 50.2 (10) · L7 57.0 (3) · L15 48.3 (7) → 51.3 (6) · L30 48.4 (11) → 50.2 (10) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Towns (calf) is listed as questionable for Wednesday's game against Cleveland."
- News (11 Nov): Towns racked up 21 points (7-11 FG, 2-5 3Pt, 5-5 FT), 11 rebounds, eight assists and one block over 34 minutes in Wednesday's 115-107 loss to the Cavs.
- News (11 Nov): Towns (calf) is available for Wednesday's game against the Cavaliers, James L. Edwards III of The Athletic reports.
- **Research:** _pending_

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **33.9** · season 34.5 (12) · L7 33.8 (4) · L15 32.4 (8) · L30 34.5 (12) · projected 38.2
- ESPN: day-to-day, ESPN est. 13 Nov (Left Hip Soreness, updated 2026-11-12)
- **Injury:** ESPN est. 13 Nov (Day-To-Day, Left Hip Soreness, updated 12 Nov), but the news said on 12 Nov: "He'll presumably be re-evaluated again at some point before tipoff to determine his availability for Friday."
- News (12 Nov): Fox is questionable for Friday's game against the Warriors due to left hip soreness.
- News (12 Nov): Fox closed Wednesday's 124-119 win over the Bulls with 17 points (7-17 FG, 2-7 3Pt, 1-2 FT), four rebounds, nine assists and three steals over 31 minutes.
- **Research:** _pending_

### Keyonte George (UTAH, PG/SG, Cream Abdul-Yammar)

- Rate **32.9** · season 34.2 (11) · L7 32.0 (3) · L15 30.6 (7) · L30 34.2 (11) · projected 36.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "George (ankle) is questionable for Wednesday's game against Orlando."
- News (11 Nov): George (ankle) is available for Wednesday's game against the Magic.
- News (11 Nov): George (ankle) is questionable for Wednesday's game against Orlando.
- **Research:** _pending_

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **31.1** · season 34.2 (11) · L7 26.2 (4) · L15 29.6 (8) · L30 34.2 (11) · projected 45.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 12 Nov: "Embiid exited to the locker room during the first quarter of Thursday's game against the Raptors due to an apparent right knee injury, Ky Carlin of USA Today reports."
- News (12 Nov): Embiid (knee) returned to Thursday's game against Toronto with 5:26 remaining in the first quarter, Ky Carlin of USA Today reports.
- News (12 Nov): Embiid exited to the locker room during the first quarter of Thursday's game against the Raptors due to an apparent right knee injury, Ky Carlin of USA Today reports.
- **Research:** _pending_

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-13 04:38 UTC.
