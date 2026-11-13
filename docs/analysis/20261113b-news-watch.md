# News watch: 13 Nov 2026

- Generated 2026-11-13 21:42 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 50 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 96 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 29 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Dejounte Murray:** out 13 Nov (ankle). He requested a trade and "will NOT play another minute" for New Orleans (Shams). We are replacing him with Saddiq Bey.
- **Trey Murphy III:** ruled out 13 Nov, aiming for 14 Nov. Override: sit 13 Nov, source refreshed.
- **Lauri Birds** added Cam Spencer, a Memphis bench guard.
- **Overrides:** no new rows. Murphy's source refreshed; the rest unchanged.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Yves Missi | return | 2026-11-18 | — | [link](https://www.nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline) | in force |
| Nic Claxton | role | 18 | 2026-11-16 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Trey Murphy III | sit | 2026-11-13 | — | [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-doubtful-for-friday-538808/) | in force |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Dejounte Murray** | NO | us | injury, minutes | 23.0 | 24.0 | out, ESPN est. 20 Nov |
| **Daniss Jenkins** | DET | us | role, minutes | 36.9 | 41.4 | active |
| **Paul George** | BOS | us | rest | 41.5 | — | day-to-day, ESPN est. 15 Nov |
| **Jusuf Nurkic** | UTAH | free agent | injury, gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 15 Nov |
| **Bennedict Mathurin** | NO | free agent | injury | 8.9 | — | day-to-day, ESPN est. 13 Nov |
| **Aday Mara** | OKC | free agent | role, minutes | 29.8 | 33.2 | active |
| **CJ McCollum** | ATL | free agent | role | 28.8 | 24.5 | active |
| **Grayson Allen** | CHA | free agent | role | 28.7 | 29.5 | active |
| **Tristan da Silva** | ORL | free agent | role | 28.3 | 33.2 | day-to-day, ESPN est. 13 Nov |
| **Quentin Grimes** | LAL | free agent | role, rest | 15.0 | 22.3 | day-to-day, ESPN est. 15 Nov |
| **Caleb Wilson** | CHI | waivers | minutes | 30.7 | 26.1 | out, ESPN est. 13 Dec |
| **Collin Murray-Boyles** | TOR | free agent | minutes | 28.8 | 30.8 | active |
| **Kevin Huerter** | DET | free agent | minutes | 28.0 | 28.7 | active |
| **Zach LaVine** | SAC | waivers | rest | 32.6 | — | active |
| **Rudy Gobert** | MIN | free agent | rest | 30.1 | — | active |
| **Draymond Green** | GS | free agent | rest | 27.7 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | injury, rest | 35.3 | — | active |
| **Paul Reed** | DET | Lauri Birds | role | 29.1 | 34.9 | active |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 48.3 | — | active |
| **Deni Avdija** | POR | Snow Time Lakers | rest | 45.9 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 38.5 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 37.8 | — | active |
| **Fred VanVleet** | HOU | Snow Time Lakers | rest | 32.7 | — | active |
| **Karl-Anthony Towns** | NY | Melbourne poopoo | injury | 52.6 | — | active |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | injury | 33.8 | — | day-to-day, ESPN est. 13 Nov |
| **Keyonte George** | UTAH | Cream Abdul-Yammar | injury | 32.8 | — | active |
| **Joel Embiid** | PHI | Dr White Slong | injury | 30.8 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Dejounte Murray (NO, PG/SG, us)

- Rate **23.0** · role rate 24.0 · season 30.6 (9) · L7 14.5 (4) · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 20 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 20 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - Ruled out 13 Nov vs MEM (left ankle sprain), out indefinitely while New Orleans looks for a trade ([CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-officially-ruled-out-friday/)). Shams: he "will NOT play another minute" for New Orleans and "intends to sit out until his trade request is satisfied" ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)). No trade yet.
  - Verdict: *ESPN corrected* (est. 20 Nov assumes only the ankle). We are dropping him, so no row.

### Daniss Jenkins (DET, PG, us)

- Rate **36.9** · role rate 41.4 · season 29.3 (11) · L7 52.0 (3) · L15 31.5 (6) · L30 29.3 (11)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 9 before; 38.7 min in his starts, against 27.4 for the season
- **Role:** news on 09 Nov: "Jenkins is in the starting lineup for Monday's game against the Wizards."
- **Minutes:** 36.7 min over his last 3 games against 27.4 for the season (+9.3)
- News (12 Nov): Jenkins had 21 points (6-11 FG, 3-5 3Pt, 6-6 FT), six rebounds and two steals in 42 minutes before fouling out of Thursday's 144-140 double-overtime victory over Washington.
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- **Research:**
  - Has "seemingly assumed a starting role" next to Cade ([RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/daniss-jenkins-news-drops-21-points-in-start-538864)).
  - Verdict: *nothing new found*.

### Paul George (BOS, SF/PF, us)

- Rate **41.5** · season 42.7 (10) · L7 39.7 (3) · L15 43.5 (6) · L30 42.7 (10) · projected 38.5
- ESPN: day-to-day, ESPN est. 15 Nov (Illness, updated 2026-11-12)
- **Rest:** back-to-back Sun 15–Mon 16 Nov; news on 11 Nov: "George will sit out the second leg of this back-to-back set due to an illness, and his next opportunity to play will come Sunday against the Mavericks."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- News (10 Nov): George tallied 36 points (14-22 FG, 6-11 3Pt, 2-2 FT), five rebounds and one assist across 30 minutes during Tuesday's 123-101 win over Philadelphia.
- **Research:**
  - Expected back 15 Nov vs DAL; no newer report.
  - Verdict: *nothing new found* (est. 15 Nov).

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Injury:** ESPN est. 20 Nov (Out, Right Foot Strain, updated 06 Nov), but the news said on 06 Nov: "He will be re-evaluated in two weeks, the Jazz announced Friday."
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:**
  - Nothing since the Jazz's 6 Nov update ([Jazz](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)).
  - Verdict: *nothing new found*; the 21 Nov floor stands.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 15 Nov (Right Knee Dislocated, updated 2026-11-10)
- **Injury:** ESPN est. 15 Nov (Out, Right Knee Dislocated, updated 10 Nov), but the news said on 09 Nov: "Raynaud is expected to be re-evaluated soon, though he can be considered week-to-week until the Kings offer an update on his status."
- News (09 Nov): Raynaud (knee) has been ruled out for Tuesday's game against Orlando.
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- **Research:**
  - Out 13 Nov vs POR, no timeline ([Yahoo, 13 Nov](https://sports.yahoo.com/articles/kings-injury-report-every-status-150005259.html)).
  - Verdict: *nothing new found*; floor 16 Nov stands.

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **8.9** · season 9.8 (11) · L7 5.3 (3) · L15 7.7 (7) · L30 9.8 (11) · projected 25.1
- ESPN: day-to-day, ESPN est. 13 Nov (Right Thumb Sprain, updated 2026-11-13)
- **Injury:** ESPN est. 13 Nov (Day-To-Day, Right Thumb Sprain, updated 13 Nov), but the news said on 13 Nov: "The Pelicans are likely to re-evaluate the swingman closer to Friday's tipoff, but his status may not have a major impact on the rotation."
- News (13 Nov): Mathurin (thumb) is listed as questionable for Friday's game against Memphis.
- News (12 Nov): Mathurin (thumb) is listed as doubtful for Friday's game against Memphis.
- **Research:**
  - Upgraded to questionable for 13 Nov (right thumb sprain) ([NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/bennedict-mathurin-thumb-questionable-friday)).
  - Verdict: *ESPN confirmed*.

### Aday Mara (OKC, C, free agent)

- Rate **29.8** · role rate 33.2 · season 25.3 (12) · L7 32.5 (4) · L15 31.9 (7) · L30 25.3 (12)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 10 before; 28.0 min in his starts, against 21.3 for the season
- **Role:** news on 11 Nov: "Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports."
- **Minutes:** 28.3 min over his last 3 games against 21.3 for the season (+7.0)
- News (11 Nov): Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports.
- News (11 Nov): Mara had 10 points (5-9 FG, 0-1 FT), 10 rebounds, two assists and one block in 26 minutes during Tuesday's 123-103 loss to Portland.
- **Research:**
  - Not on the 13 Nov report; Holmgren and Jaylin Williams out; one of four possible starters ([Yahoo, 13 Nov](https://sports.yahoo.com/articles/clippers-vs-thunder-injury-report-145414341.html)).
  - Verdict: *nothing new found*.

### CJ McCollum (ATL, PG/SG, free agent)

- Rate **28.8** · role rate 24.5 · season 26.3 (12) → 28.3 (11) · L7 20.3 (3) → 28.0 (2) · L15 26.0 (7) → 29.5 (6) · L30 26.3 (12) → 28.3 (11) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 10; 22.5 min in those 2, against 25.6 for the season
- News (10 Nov): McCollum supplied 21 points (8-15 FG, 3-5 3Pt, 2-2 FT), four assists and one block in 24 minutes during Monday's 124-114 loss to the Lakers.
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- **Research:**
  - Healthy; Kingston Flemings is questionable 13 Nov (lumbar spasm), and McCollum would likely start if he sits ([ClutchPoints, 13 Nov](https://clutchpoints.com/nba/atlanta-hawks/hawks-vs-bulls-injury-report-caleb-wilson-kingston-flemings-nba-cup-matchup)).
  - Verdict: *nothing new found*; the 23-minute row stands.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **28.7** · role rate 29.5 · season 26.9 (12) · L7 30.0 (3) · L15 28.7 (7) · L30 26.9 (12) · projected 26.6
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 30.0 min in his starts, against 27.3 for the season
- News (13 Nov): Allen logged 14 points (5-11 FG, 4-8 3Pt), four rebounds, six assists and one steal over 34 minutes during Thursday's 101-96 loss to Phoenix.
- News (09 Nov): Allen finished with 27 points (8-14 FG, 6-12 3Pt, 5-6 FT), four rebounds, six assists and two steals across 34 minutes during Monday's 124-112 win over Cleveland.
- **Research:**
  - CHA off tonight; nothing new.
  - Verdict: *nothing new found*.

### Tristan da Silva (ORL, SF/PF, free agent)

- Rate **28.3** · role rate 33.2 · season 25.9 (9) · L7 35.0 (1) · L15 24.6 (5) · L30 25.9 (9) · projected 17.2
- ESPN: day-to-day, ESPN est. 13 Nov (Left Calf Strain, updated 2026-11-13)
- **Role:** started 1 of his last 2 games after 0 of 7 before; 39.0 min in his starts, against 30.4 for the season
- News (13 Nov): Da Silva (calf) participated in the Magic's morning shootaround and remains questionable for Friday's game against Milwaukee, Jason Beede of the Orlando Sentinel reports.
- News (12 Nov): Da Silva (calf) is questionable for Friday's game against Milwaukee.
- **Research:**
  - Game-time decision 13 Nov (left calf strain), went through shootaround, starts if cleared ([CBS/RotoWire, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-tristan-da-silva-game-time-call-for-friday/); [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/tristan-da-silva-calf-questionable-vs-milwaukee)).
  - Verdict: *ESPN confirmed*.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **15.0** · role rate 22.3 · season 16.6 (11) · L7 14.0 (2) · L15 11.7 (6) · L30 16.6 (11) · projected 28.1
- ESPN: day-to-day, ESPN est. 15 Nov (Finger, updated 2026-11-13)
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 26.1 for the season
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 11 Nov: "However, it appears that absence wasn't simply due to rest during the second night of a back-to-back set, as Grimes will now miss a second straight game after previously being listed as questionable."
- News (11 Nov): Grimes (finger) has been ruled out for Wednesday's game against the Bucks.
- News (10 Nov): Grimes (finger) is listed as questionable for Wednesday's game in Milwaukee.
- **Research:**
  - Expects to return 15 Nov vs PHX; could start if Austin Reaves (heel) is not cleared ([RotoWire, 13 Nov](https://www.rotowire.com/basketball/headlines/quentin-grimes-injury-expects-to-return-sunday-538933)).
  - Verdict: *ESPN confirmed*.

### Caleb Wilson (CHI, SF, waivers)

- Rate **30.7** · role rate 26.1 · season 34.9 (10) · L7 25.0 (2) · L15 31.4 (5) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - No games since the morning run. See this player's research in [20261113-news-watch.md](20261113-news-watch.md); no newer news found.

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **28.8** · role rate 30.8 · season 24.8 (11) · L7 34.0 (3) · L15 28.0 (7) · L30 24.8 (11) · projected 24.8
- ESPN: active
- **Minutes:** 28.7 min over his last 3 games against 22.9 for the season (+5.8)
- News (12 Nov): Murray-Boyles ended with 14 points (5-9 FG, 1-1 3Pt, 3-4 FT), four assists, five blocks and one steal over 32 minutes during Thursday's 123-112 loss to the 76ers.
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- **Research:**
  - TOR off tonight; nothing new.
  - Verdict: *nothing new found*.

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.0** · role rate 28.7 · season 21.6 (11) · L7 36.0 (3) · L15 27.0 (6) · L30 21.6 (11) · projected 22.9
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 23.2 for the season (+7.5)
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- News (05 Nov): Huerter supplied eight points (3-8 FG, 2-6 3Pt) and two blocks over 20 minutes during Wednesday's 112-106 loss to the 76ers.
- **Research:**
  - DET off tonight; nothing new.
  - Verdict: *nothing new found*.

### Zach LaVine (SAC, SG/SF, waivers)

- Rate **32.6** · season 32.5 (11) → 35.0 (10) · L7 31.0 (3) · L15 29.1 (7) → 32.7 (6) · L30 32.5 (11) → 35.0 (10) · projected 32.0
- ESPN: active
- **Rest:** back-to-back Fri 20–Sat 21 Nov; news on 11 Nov: "He'll have a full two days to rest up before the Kings' next game Friday against Portland."
- News (11 Nov): LaVine tallied 31 points (10-16 FG, 6-9 3Pt, 5-5 FT), three rebounds, two assists and two steals over 33 minutes in Tuesday's 107-100 loss to the Magic.
- News (07 Nov): LaVine notched 14 points (4-12 FG, 1-6 3Pt, 5-5 FT), four rebounds, three assists and one steal over 35 minutes during Friday's 124-109 loss to the Spurs.
- **Research:**
  - Not on the 13 Nov injury previews ([550 The Zone, 13 Nov](https://550thezone.iheart.com/content/2026-11-13-trail-blazers-vs-kings-injury-report-nov-13/)); nothing on resting.
  - Verdict: *nothing new found*.

### Rudy Gobert (MIN, C, free agent)

- Rate **30.1** · season 27.3 (11) · L7 29.3 (3) · L15 32.7 (6) · L30 27.3 (11) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:**
  - MIN off tonight; nothing new.
  - Verdict: *nothing new found*.

### Draymond Green (GS, PF/C, free agent)

- Rate **27.7** · season 25.0 (10) · L7 29.7 (3) · L15 28.8 (6) · L30 25.0 (10) · projected 28.5
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Green recorded two points (1-5 FG, 0-1 3Pt, 0-2 FT), six rebounds, 13 assists, two steals and two blocks across 34 minutes in Saturday's 126-119 overtime win over the Magic.
- News (07 Nov): Green (elbow) is available for Saturday's game against the Magic.
- **Research:**
  - Not on the report, listed to start; Curry out ([Yahoo, 13 Nov](https://sports.yahoo.com/articles/steph-curry-headlines-10-player-151824578.html)).
  - Verdict: *nothing new found*.

## Opponents: this week and next

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.3** · season 37.1 (11) · L7 34.3 (3) · L15 34.0 (6) · L30 37.1 (11) · projected 38.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Herro (knee) is listed as questionable for Wednesday's game against the Lakers."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 09 Nov: "If the veteran guard is ultimately ruled out for the front end of this back-to-back set, Brayden Burries and Ryan Rollins would likely see expanded roles."; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- News (11 Nov): Herro (knee) is listed as available for Wednesday's game against the Lakers.
- **Research:**
  - The Bucks list no one on their report ([SI, 13 Nov](https://www.si.com/nba/bucks/onsi/bucks-take-healthy-roster-into-nba-cup-matchup-with-magic-preview-starters-injuries-how-to-watch-01m7ar8txtf9)).
  - Verdict: *ESPN confirmed*.

### Paul Reed (DET, PF/C, Lauri Birds)

- Rate **29.1** · role rate 34.9 · season 31.7 (11) · L7 28.7 (3) · L15 27.7 (6) · L30 31.7 (11) · projected 20.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 7 of 9; 29.5 min in those 2, against 27.1 for the season
- News (12 Nov): Reed had 13 points (5-9 FG, 0-1 3Pt, 3-6 FT), 11 rebounds and three assists in 38 minutes during Thursday's 144-140 double-overtime win over the Wizards.
- News (09 Nov): Reed will come off the bench Monday against Washington, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - DET off tonight; nothing new.
  - Verdict: *nothing new found*.

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **48.3** · season 46.5 (13) → 49.3 (12) · L7 46.2 (4) · L15 50.0 (8) · L30 46.5 (13) → 49.3 (12) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 10 Nov: "He scored at least 20 points for the third time this year and the first time since back-to-back such performances to begin the campaign."
- News (12 Nov): Kessler logged 10 points (5-10 FG), 11 rebounds, three assists, one block and one steal over 29 minutes during Wednesday's 123-112 victory over the Bucks.
- News (10 Nov): Kessler recorded 21 points (8-12 FG, 5-6 FT), 10 rebounds, four assists, one block and one steal in 30 minutes during Monday's 124-114 victory over the Hawks.
- **Research:**
  - LAL off tonight; nothing new.
  - Verdict: *nothing new found*.

### Deni Avdija (POR, SF/PF, Snow Time Lakers)

- Rate **45.9** · season 41.5 (11) → 43.9 (10) · L7 41.8 (4) → 50.0 (3) · L15 40.5 (8) → 43.9 (7) · L30 41.5 (11) → 43.9 (10) · projected 40.4
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 12 Nov: "The star forward was coming off another impressive outing in the first leg of this back-to-back set against the Thunder, notching 24 points (8-15 FG, 2-4 3Pt, 6-8 FT), six rebounds, eight assists and one steal in 34 minutes during Tuesday's 123-103 win."
- News (12 Nov): Avdija tallied 28 points (9-20 FG, 4-13 3Pt, 6-6 FT), three rebounds, six assists, four steals and two blocks across 35 minutes in Wednesday's 118-108 win over the Thunder.
- News (11 Nov): Avdija recorded 24 points (8-15 FG, 2-4 3Pt, 6-8 FT), six rebounds, eight assists and one steal in 34 minutes during Tuesday's 123-103 win over the Thunder.
- **Research:**
  - Not on the 13 Nov report.
  - Verdict: *nothing new found*.

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **38.5** · season 39.2 (12) · L7 35.0 (4) · L15 40.1 (7) · L30 39.2 (12) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- News (08 Nov): Brown totaled 29 points (11-22 FG, 2-6 3Pt, 5-8 FT), seven rebounds, four assists and one steal across 35 minutes during Sunday's 127-121 victory over the Bulls.
- **Research:**
  - PHI off tonight; nothing new.
  - Verdict: *nothing new found*.

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **37.8** · season 38.8 (10) · L7 33.5 (4) · L15 40.2 (6) · L30 38.8 (10) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 14–Sun 15 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (13 Nov): Irving accumulated 10 points (4-11 FG, 2-6 3Pt), three rebounds, four assists and one block across 27 minutes during Thursday's 133-94 loss to the Timberwolves.
- News (10 Nov): Irving delivered 35 points (11-18 FG, 7-10 3Pt, 6-7 FT) and four assists across 38 minutes in Monday's 125-122 win over the Pacers.
- **Research:**
  - DAL off tonight; nothing on the 14–15 Nov back-to-back.
  - Verdict: *nothing new found*.

### Fred VanVleet (HOU, PG/SG, Snow Time Lakers)

- Rate **32.7** · season 33.1 (10) · L7 33.0 (3) · L15 31.5 (6) · L30 33.1 (10) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; news on 12 Nov: "VanVleet did get held out for the second game of a back-to-back during that period, something that will likely continue to happen all season."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (12 Nov): VanVleet had 18 points (6-9 FG, 4-7 3Pt, 2-2 FT), two rebounds, six assists and three steals over 30 minutes during Wednesday's 115-108 victory over Golden State.
- News (10 Nov): VanVleet finished with 12 points (4-9 FG, 3-6 3Pt, 1-2 FT), a rebound and two assists across 30 minutes in Monday's 110-100 win over the Nuggets.
- **Research:**
  - "Will likely miss one of" the 15–16 Nov games ([Yahoo, 13 Nov](https://sports.yahoo.com/articles/marcus-smart-suspended-rockets-friday-013657197.html)).
  - Verdict: *nothing new found*; the 16 Nov row stands.

## Other rosters: injury flags only

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **52.6** · season 48.4 (11) → 50.2 (10) · L7 57.0 (3) · L15 48.5 (6) → 52.2 (5) · L30 48.4 (11) → 50.2 (10) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Towns (calf) is listed as questionable for Wednesday's game against Cleveland."
- News (11 Nov): Towns racked up 21 points (7-11 FG, 2-5 3Pt, 5-5 FT), 11 rebounds, eight assists and one block over 34 minutes in Wednesday's 115-107 loss to the Cavs.
- News (11 Nov): Towns (calf) is available for Wednesday's game against the Cavaliers, James L. Edwards III of The Athletic reports.
- **Research:**
  - The Knicks have no one on their report ([SportsBettingDime, 13 Nov](https://www.sportsbettingdime.com/news/nba/knicks-pacers-predictions-props-injuries-nov-13/)).
  - Verdict: *ESPN confirmed*.

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **33.8** · season 34.5 (12) · L7 33.8 (4) · L15 32.1 (7) · L30 34.5 (12) · projected 38.2
- ESPN: day-to-day, ESPN est. 13 Nov (Left Hip Soreness, updated 2026-11-12)
- **Injury:** ESPN est. 13 Nov (Day-To-Day, Left Hip Soreness, updated 12 Nov), but the news said on 12 Nov: "He'll presumably be re-evaluated again at some point before tipoff to determine his availability for Friday."
- News (12 Nov): Fox is questionable for Friday's game against the Warriors due to left hip soreness.
- News (12 Nov): Fox closed Wednesday's 124-119 win over the Bulls with 17 points (7-17 FG, 2-7 3Pt, 1-2 FT), four rebounds, nine assists and three steals over 31 minutes.
- **Research:**
  - Still questionable 13 Nov (left hip soreness) ([CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-deaaron-fox-listed-questionable-for-friday/)).
  - Verdict: *ESPN confirmed*.

### Keyonte George (UTAH, PG/SG, Cream Abdul-Yammar)

- Rate **32.8** · season 34.2 (11) · L7 32.0 (3) · L15 30.5 (6) · L30 34.2 (11) · projected 36.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "George (ankle) is questionable for Wednesday's game against Orlando."
- News (11 Nov): George (ankle) is available for Wednesday's game against the Magic.
- News (11 Nov): George (ankle) is questionable for Wednesday's game against Orlando.
- **Research:**
  - Off the injury report ([SI, 13 Nov](https://www.si.com/nba/jazz/onsi/jazz-vs-rockets-injury-report-latest-for-utah-s-second-nba-cup-game)).
  - Verdict: *ESPN confirmed*.

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **30.8** · season 34.2 (11) · L7 26.2 (4) · L15 28.4 (7) · L30 34.2 (11) · projected 45.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 12 Nov: "Embiid exited to the locker room during the first quarter of Thursday's game against the Raptors due to an apparent right knee injury, Ky Carlin of USA Today reports."
- News (13 Nov): Embiid closed with 20 points (7-17 FG, 0-3 3Pt, 6-7 FT), four rebounds, three assists, one block and one steal in 28 minutes during Thursday's 123-112 win over Toronto.
- News (12 Nov): Embiid (knee) returned to Thursday's game against Toronto with 5:26 remaining in the first quarter, Ky Carlin of USA Today reports.
- **Research:**
  - Nothing new on the 15–16 Nov back-to-back ([Inquirer, 13 Nov](https://www.inquirer.com/sixers/joel-embiid-performance-injury-scare-raptors-20261113.html)).
  - Verdict: *nothing new found*.

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Out 13 Nov; still 4–6 weeks from 23 Oct, no team date ([CBS](https://www.cbssports.com/fantasy/basketball/news/magics-paolo-banchero-no-timetable-for-return)).
  - Verdict: *nothing new found*.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-13 21:42 UTC.
- [CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-officially-ruled-out-friday/)
- [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)
- [Jazz](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)
- [NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/bennedict-mathurin-thumb-questionable-friday)
- [CBS/RotoWire, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-tristan-da-silva-game-time-call-for-friday/)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/tristan-da-silva-calf-questionable-vs-milwaukee)
- [RotoWire, 13 Nov](https://www.rotowire.com/basketball/headlines/quentin-grimes-injury-expects-to-return-sunday-538933)
- [550 The Zone, 13 Nov](https://550thezone.iheart.com/content/2026-11-13-trail-blazers-vs-kings-injury-report-nov-13/)
- [CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-friday-538912/)
- [RotoWire, 12 Nov](https://www.rotowire.com/basketball/headlines/daniss-jenkins-news-drops-21-points-in-start-538864)
- [Yahoo, 13 Nov](https://sports.yahoo.com/articles/kings-injury-report-every-status-150005259.html)
- [Yahoo, 13 Nov](https://sports.yahoo.com/articles/clippers-vs-thunder-injury-report-145414341.html)
- [ClutchPoints, 13 Nov](https://clutchpoints.com/nba/atlanta-hawks/hawks-vs-bulls-injury-report-caleb-wilson-kingston-flemings-nba-cup-matchup)
- [Yahoo, 13 Nov](https://sports.yahoo.com/articles/steph-curry-headlines-10-player-151824578.html)
- [SI, 13 Nov](https://www.si.com/nba/bucks/onsi/bucks-take-healthy-roster-into-nba-cup-matchup-with-magic-preview-starters-injuries-how-to-watch-01m7ar8txtf9)
- [CBS](https://www.cbssports.com/fantasy/basketball/news/magics-paolo-banchero-no-timetable-for-return)
- [Yahoo, 13 Nov](https://sports.yahoo.com/articles/marcus-smart-suspended-rockets-friday-013657197.html)
- [SportsBettingDime, 13 Nov](https://www.sportsbettingdime.com/news/nba/knicks-pacers-predictions-props-injuries-nov-13/)
- [CBS, 12 Nov](https://www.cbssports.com/fantasy/basketball/news/spurs-deaaron-fox-listed-questionable-for-friday/)
- [SI, 13 Nov](https://www.si.com/nba/jazz/onsi/jazz-vs-rockets-injury-report-latest-for-utah-s-second-nba-cup-game)
- [Inquirer, 13 Nov](https://www.inquirer.com/sixers/joel-embiid-performance-injury-scare-raptors-20261113.html)
