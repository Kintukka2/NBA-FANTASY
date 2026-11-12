# News watch: 12 Nov 2026

- Generated 2026-11-12 06:05 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 49 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 98 on other teams' rosters (injury flags only, except this week's and next week's opponents: Lauri Birds, Snow Time Lakers). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 31 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

**Our players:**
- **Caleb Wilson:** left 11 Nov with a right hand injury; no diagnosis yet. No timetable reported; *ESPN est.* 13 Nov, a placeholder.
- **Dejounte Murray:** his minutes fell in three blowout losses; it is not a role change.
- **Paul George:** next game Sunday (illness); *ESPN est.* 15 Nov. The second night, 16 Nov, is a rest risk.
- **Trey Murphy III:** next chance 13 Nov. The 14 Nov second night is a high risk.
- **Scottie Barnes:** "progressing well", still day-to-day. No timetable reported; *ESPN est.* 12 Nov.
- **Isaiah Hartenstein:** played 34 min on 11 Nov (20 pts, 11 reb, 6 ast) with Ajay Mitchell out (ankle).
- **Jalen Smith:** keeps the start while Nic Claxton's limit lasts.

**Lauri Birds:**
- **Stephen Curry:** left 11 Nov after 6 minutes with right abdominal soreness. An MRI is pending, and RotoWire calls him "highly questionable" for 13 Nov. No timetable reported; *ESPN est.* 13 Nov.
- **Jamal Shead:** back to the bench now that Quickley has returned.

**Snow Time Lakers (next week):**
- Herro played 11 Nov.
- Kessler is wearing a finger splint.
- VanVleet's sit on 16 Nov stands.

**Overrides:**
- Added: Nic Claxton role 18 until 16 Nov; Jusuf Nurkic return 21 Nov (a floor).
- Removed: the expired Murphy sit row (11 Nov).
- Unchanged: Missi 18 Nov, Raynaud 16 Nov, McCollum 23 min, VanVleet 16 Nov.

**Our planned streamers:**
- **Devin Vassell (SA):** out 11 Nov, his second straight (left adductor tightness) ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/devin-vassell-groin-downgraded-to-out-wednesday)); Mitch Johnson: "I don't think it's anything hopefully long term" ([Express-News via Yahoo, 10 Nov](https://sports.yahoo.com/articles/vassell-julian-champagnie-seizes-shot-205353349.html)). No timetable reported; *ESPN est.* 13 Nov.
- **Norman Powell (CHI):** out 11 Nov (back spasms); Splitter expects him back 13 Nov vs ATL at "probably 70 percent" ([ClutchPoints, 11 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-tiago-splitter-target-date-norman-powell-return); [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-ruled-out-wednesday-538653)).
- **P.J. Washington (DAL):** not on the injury report for 12 Nov at MIN ([Dallas Sports Journal, 11 Nov](https://dallassportsjournal.com/mavericks-timberwolves-injury-report-morez-johnson-anthony-edwards/)).
- **Day'Ron Sharpe (BKN):** played 11 Nov in the 145–111 win at NOP (15 pts, 5 ast, 4 blk; [NetsDaily, 12 Nov](https://netsdaily.com/nets-scores-results/116020/nets-vs-pelicans-145-111-egor-demin-michael-porter-jr)).
- **Jordan Goodwin (PHX):** back from a calf injury on 10 Nov, 18 pts in 14 min; minutes "should increase" ([NBC Sports, 10 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-10/jordan-goodwin-calf-hits-six-triples-in-return)).
- **Trey Murphy III (ours):** out 11 Nov; next chance 13 Nov vs MEM ([CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-out-again-wednesday/)); 14 Nov (second night) is a high risk; no timetable reported; *ESPN est.* 13 Nov.
- **Scottie Barnes (ours):** Rajakovic, 11 Nov: "reconditioning, still day-to-day, but he's progressing well and feeling better" (Josh Lewenberg via [HoopsHype, 11 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/11/rajakovic-says-that-barnes-groin-is-in-the-process/92734026007/)). No timetable reported; *ESPN est.* 12 Nov.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Yves Missi | return | 2026-11-18 | — | [link](https://www.nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand) | in force |
| Fred VanVleet | sit | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-to-miss-back-to-backs/) | in force |
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-for-tuesday/) | in force |
| Trey Murphy III | sit | 2026-11-11 | — | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/trey-murphy-knee-now-doubtful-vs-brooklyn) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Caleb Wilson** | CHI | us | minutes | 28.8 | 26.1 | day-to-day, ESPN est. 13 Nov |
| **Dejounte Murray** | NO | us | minutes | 25.3 | 24.0 | active |
| **Paul George** | BOS | us | rest | 41.7 | — | day-to-day, ESPN est. 15 Nov |
| **Yves Missi** | NO | free agent | injury, gap | 60.4 † | — | out, ESPN est. 16 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 15 Nov |
| **Jalen Suggs** | ORL | free agent | injury | 27.7 | — | out, ESPN est. 16 Nov |
| **Daniss Jenkins** | DET | free agent | role | 31.5 | 40.1 | active |
| **Grayson Allen** | CHA | free agent | role | 29.8 | 28.0 | active |
| **CJ McCollum** | ATL | free agent | role | 29.3 | 24.5 | active |
| **Aday Mara** | OKC | free agent | role, minutes | 29.1 | 33.2 | active |
| **Saddiq Bey** | NO | free agent | role | 27.5 | 24.0 | active |
| **Ryan Rollins** | MIL | free agent | role | 24.7 | — | day-to-day, ESPN est. 13 Nov |
| **Quentin Grimes** | LAL | free agent | role | 15.4 | 22.3 | out, ESPN est. 15 Nov |
| **Nic Claxton** | CHI | free agent | minutes | 29.3 † | — | active |
| **Kevin Huerter** | DET | free agent | minutes | 28.3 | 28.7 | active |
| **Rudy Gobert** | MIN | free agent | rest | 30.3 | — | active |
| **Draymond Green** | GS | free agent | rest | 27.7 | — | active |
| **Robert Williams III** | POR | free agent | rest | 27.3 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Stephen Curry** | GS | Lauri Birds | injury, rest | 50.7 | — | day-to-day, ESPN est. 13 Nov |
| **Tyler Herro** | MIL | Snow Time Lakers | injury, rest | 35.5 | — | active |
| **Jamal Shead** | TOR | Lauri Birds | role, minutes | 28.5 | 36.3 | active |
| **Walker Kessler** | LAL | Snow Time Lakers | rest | 48.0 | — | active |
| **Jaylen Brown** | PHI | Snow Time Lakers | rest | 41.0 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 40.8 | — | active |
| **Fred VanVleet** | HOU | Snow Time Lakers | rest | 32.6 | — | active |
| **Jaxson Hayes** | UTAH | Snow Time Lakers | rest | 24.6 | — | active |
| **Giannis Antetokounmpo** | MIA | Dr White Slong | injury | 58.9 | — | active |
| **Karl-Anthony Towns** | NY | Melbourne poopoo | injury | 51.3 | — | active |
| **Keyonte George** | UTAH | Cream Abdul-Yammar | injury | 36.2 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 22 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Caleb Wilson (CHI, SF, us)

- Rate **28.8** · role rate 26.1 · season 34.9 (10) · L7 17.7 (3) · L15 33.5 (6) · L30 34.9 (10) · projected 34.9
- ESPN: day-to-day, ESPN est. 13 Nov (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- News (11 Nov): Wilson exited to the locker room in the third quarter of Wednesday's game against San Antonio due to an apparent hand injury, K.C. Johnson of Chicago Sports Network reports.
- **Research:**
  - Hurt his right hand going for the ball against Wembanyama and left with 9:21 left in the third on 11 Nov; Splitter had no update and expects more Thursday ([ESPN, 11 Nov](https://www.espn.com/nba/story/_/id/50458612/bulls-rookie-caleb-wilson-leaves-game-right-hand-injury)). No imaging or diagnosis published as of 1 AM ET 12 Nov ([Yahoo, 12 Nov](https://sports.yahoo.com/articles/caleb-wilson-injury-chicago-bulls-054028606.html); [Basketnews, 12 Nov](https://basketnews.com/news-259311-caleb-wilson-injury-latest-updates-as-bulls-rookie-exits-spurs-game.html)). He also played through right hip soreness ([Sun-Times, 11 Nov](https://chicago.suntimes.com/bulls/2026/11/11/bulls-rookie-caleb-wilson-answers-bell-sore-hip)); he has a history of hand fractures ([Tar Heel Tribune, 11 Nov](https://tarheeltribune.com/2026/11/11/tar-heels-in-pros-wilson-suffers-another-hand-injury-ingram-produces-third-career-g-league-triple-double/)).
  - Minutes: the drop is two games, 22 min in a 30-point loss on 4 Nov and the 15-min exit on 11 Nov; 31–34 min otherwise, still starting.
  - Verdict: *nothing new found*; no timetable reported; *ESPN est.* 13 Nov is a placeholder.

### Dejounte Murray (NO, PG/SG, us)

- Rate **25.3** · role rate 24.0 · season 30.6 (9) · L7 20.8 (5) · L15 21.7 (6) · L30 30.6 (9) · projected 39.0
- ESPN: active
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (09 Nov): Murray registered six points (1-6 FG, 0-1 3Pt, 4-4 FT), three rebounds and three assists across 28 minutes during Sunday's 139-123 loss to the Clippers.
- News (05 Nov): Murray ended Wednesday's 120-113 overtime win over Utah with 20 points (4-7 FG, 1-3 3Pt, 11-11 FT), eight rebounds, four assists and four steals across 44 minutes.
- **Research:**
  - No restriction, injury or benching; he started 11 Nov ([NBC Sports, 11 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-11/pelicans-start-fears-murray-jones-zion-karlo)). His minutes fell in three blowout losses: 28 at LAC, 18 at GS ([ESPN, 9 Nov](https://www.espn.com/nba/recap?gameId=401909959)), about 27 vs BKN ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/dejounte-murray-scores-5-points-in-27-minutes)), with poor shooting (1-6, 2-6). A column argues Herb Jones should start instead, with no sign the team will ([Yahoo, 11 Nov](https://sports.yahoo.com/articles/orleans-pelicans-dejounte-murray-problem-025055794.html)).
  - Verdict: *nothing new found*: blowout minutes and shooting, not a role change.

### Paul George (BOS, SF/PF, us)

- Rate **41.7** · season 42.7 (10) · L7 40.2 (4) · L15 43.6 (7) · L30 42.7 (10) · projected 38.5
- ESPN: day-to-day, ESPN est. 15 Nov (Illness, updated 2026-11-12)
- **Rest:** back-to-back Sun 15–Mon 16 Nov; news on 11 Nov: "George will sit out the second leg of this back-to-back set due to an illness, and his next opportunity to play will come Sunday against the Mavericks."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- News (10 Nov): George tallied 36 points (14-22 FG, 6-11 3Pt, 2-2 FT), five rebounds and one assist across 30 minutes during Tuesday's 123-101 win over Philadelphia.
- **Research:**
  - Ruled out 11 Nov at TOR; next chance Sunday vs DAL ([CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-paul-george-out-wednesday/)); the illness is not long-term (unconfirmed, [Heavy, 11 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-raptors-game-decision/)).
  - Rest: Boston rested him on the second night of a back-to-back on 2 Nov but he played both nights of an October set ([Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)); 16 Nov (second night of 15–16 Nov) is a risk, not announced.
  - Verdict: *ESPN confirmed* (15 Nov).

## Free agents and waivers

### Yves Missi (NO, C, free agent)

- Rate **60.4** (small sample) · season 41.5 (2) → 68.0 (1) · L7 — · L15 — · L30 41.5 (2) → 68.0 (1) · projected 24.7
- ESPN: out, ESPN est. 16 Nov (Left Knee Bruise, updated 2026-11-05)
- **Injury:** ESPN est. 16 Nov (Out, Left Knee Bruise, updated 05 Nov), but the news said on 05 Nov: "He remains without a timetable to return and can be considered week-to-week moving forward."
- **Gap:** listed out, and no news in 5 days (ESPN est. 16 Nov)
- News (05 Nov): Missi (knee) is out for Friday's game against Minnesota.
- News (30 Oct): Missi (knee) won't play in Saturday's game against Atlanta.
- **Research:**
  - Out 11 Nov vs BKN, no timeline ([Pelicans, 11 Nov](https://nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand); [FLM, 11 Nov](https://fieldlevelmedia.com/nba/nets-romp-as-slumping-pelicans-sustain-another-heavy-defeat/)); no practice news.
  - Verdict: *nothing new found*; the 18 Nov floor stands. Small sample (one 68-FP game).

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 15 Nov (Right Knee Dislocated, updated 2026-11-10)
- **Injury:** ESPN est. 15 Nov (Out, Right Knee Dislocated, updated 10 Nov), but the news said on 09 Nov: "Raynaud is expected to be re-evaluated soon, though he can be considered week-to-week until the Kings offer an update on his status."
- News (09 Nov): Raynaud (knee) has been ruled out for Tuesday's game against Orlando.
- News (26 Oct): Raynaud (knee) is progressing in his rehabilitation and will be re-evaluated in approximately two weeks, Brenden Nunes of KHTK Sactown Sports 1140 reports.
- **Research:**
  - "Will be re-evaluated next week" (right patellar subluxation; [Sactown Sports, 10 Nov](https://sactownsports.com/nba/sacramento-kings/magic-loss)), the same words as an 8 Nov note ([FLM](https://fieldlevelmedia.com/nba/heat-look-to-reverse-course-vs-struggling-kings)), so "next week" is unclear. No result reported.
  - Verdict: *nothing new found*; the 16 Nov floor stands.

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **27.7** · season 26.3 (3) · L7 — · L15 — · L30 26.3 (3) · projected 29.2
- ESPN: out, ESPN est. 16 Nov (Right Knee, updated 2026-11-09)
- **Injury:** ESPN est. 16 Nov (Out, Right Knee, updated 09 Nov), but the news said on 09 Nov: "The Magic said that Suggs' return will depend on how his knee responds to increased on-court activities, so he can be considered week-to-week until the the team provides another update on his progress."
- News (09 Nov): Suggs (knee) has been ruled out for Tuesday's game against the Kings.
- News (26 Oct): Suggs has been diagnosed with a mild bone bruise in his right knee and will be re-evaluated in two weeks, Shams Charania of ESPN reports.
- **Research:**
  - Missed 11 Nov at UTA ([Yahoo, 11 Nov](https://sports.yahoo.com/articles/magic-overpower-jazz-finish-2-045500670.html)); nothing newer than the 9 Nov court-work report.
  - Verdict: *ESPN confirmed* (16 Nov floor).

### Daniss Jenkins (DET, PG, free agent)

- Rate **31.5** · role rate 40.1 · season 28.1 (10) · L7 40.0 (3) · L15 27.9 (7) · L30 28.1 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 8 before; 37.0 min in his starts, against 25.9 for the season
- **Role:** news on 09 Nov: "Jenkins is in the starting lineup for Monday's game against the Wizards."
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- News (09 Nov): Jenkins is in the starting lineup for Monday's game against the Wizards.
- **Research:**
  - 58 and 57 FP in his last two games on 32 and 36 min; the fifth starter is still picked game by game until Duren returns ([Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html)). Duren re-evaluated about 22 Nov ([Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)); Isaiah Joe out 12 Nov at WSH, no timetable reported ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/isaiah-joe-hip-remains-out-thursday-vs-was)).
  - Verdict: *nothing new found*. No row.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **29.8** · role rate 28.0 · season 26.7 (11) · L7 34.3 (3) · L15 27.6 (7) · L30 26.7 (11) · projected 26.6
- ESPN: active
- **Role:** started 2 of his last 2 games after 0 of 9 before; 28.0 min in his starts, against 26.7 for the season
- News (09 Nov): Allen finished with 27 points (8-14 FG, 6-12 3Pt, 5-6 FT), four rebounds, six assists and two steals across 34 minutes during Monday's 124-112 win over Cleveland.
- News (06 Nov): Allen will start in Friday's game against the Celtics
- **Research:**
  - Knueppel, Schröder and Brandon Miller (hip, short-term) are all out 12 Nov at PHX ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/brandon-miller-hip-remains-out-thursday-vs-phx); [SI, 11 Nov](https://www.si.com/nba/suns/onsi/phoenix-suns-reveal-encouraging-injury-report-charlotte-hornets)); Allen is "likely to continue seeing a heavy workload" ([CBS/RotoWire, 10 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-pours-in-27-points-six-triples-in-win/)). L7 34.3 (3) is 7.6 over, on starter minutes.
  - Verdict: *ESPN confirmed*. No row: no source states his minutes, and the two-start average (28) would sit under his rate.

### CJ McCollum (ATL, PG/SG, free agent)

- Rate **29.3** · role rate 24.5 · season 26.3 (12) → 28.3 (11) · L7 24.2 (4) → 30.7 (3) · L15 25.1 (8) → 28.0 (7) · L30 26.3 (12) → 28.3 (11) · projected 32.4
- ESPN: active
- **Role:** came off the bench in his last 2 games after starting 8 of 10; 22.5 min in those 2, against 25.6 for the season
- News (10 Nov): McCollum supplied 21 points (8-15 FG, 3-5 3Pt, 2-2 FT), four assists and one block in 24 minutes during Monday's 124-114 loss to the Lakers.
- News (08 Nov): McCollum contributed nine points (4-14 FG, 1-6 3Pt), four rebounds, three assists, two blocks and two steals across 21 minutes during Saturday's 124-121 win over the Nets.
- **Research:**
  - ATL idle 10–12 Nov; next 13 Nov vs CHI. Latest is still the bench note ([RotoWire, 10 Nov](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466)).
  - Verdict: *nothing new found*; the 23-minute row stands.

### Aday Mara (OKC, C, free agent)

- Rate **29.1** · role rate 33.2 · season 25.3 (12) · L7 32.4 (5) · L15 29.6 (8) · L30 25.3 (12)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 10 before; 28.0 min in his starts, against 21.3 for the season
- **Role:** news on 11 Nov: "Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports."
- **Minutes:** 28.3 min over his last 3 games against 21.3 for the season (+7.0)
- News (11 Nov): Mara is in the starting lineup for Wednesday's matchup with the Trail Blazers, Clemente Almanza of USA Today reports.
- News (11 Nov): Mara had 10 points (5-9 FG, 0-1 FT), 10 rebounds, two assists and one block in 26 minutes during Tuesday's 123-103 loss to Portland.
- **Research:**
  - Started 11 Nov and played a season-high 32 min (11 pts, 6 reb) after Ajay Mitchell was ruled out late with a left ankle sprain ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/aday-mara-plays-season-high-32-minutes-vs-por); [Heavy, 11 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/ajay-mitchell-injury-update-thunder-blazers-rematch)); no timetable reported for Mitchell. Jaylin Williams (back spasms) missed his fifth straight ([SI, 11 Nov](https://www.si.com/nba/thunder/onsi/injury-report-okc-thunder-list-six-players-against-trail-blazers)). His L7 is 7.1 over on more minutes; about 25+ minutes should last until Jaylin Williams returns.
  - Verdict: *nothing new found*. No row: the starts are tied to injuries.

### Saddiq Bey (NO, SF/PF, free agent)

- Rate **27.5** · role rate 24.0 · season 26.9 (12) · L7 26.6 (5) · L15 28.0 (9) · L30 26.9 (12) · projected 25.9
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 10 before; 24.0 min in his starts, against 26.8 for the season
- **Role:** news on 09 Nov: "Bey will start Monday's game against the Warriors, Rod Walker of The Times-Picayune reports."
- News (11 Nov): Bey won't start Wednesday's game against the Nets.
- News (09 Nov): Bey will start Monday's game against the Warriors, Rod Walker of The Times-Picayune reports.
- **Research:**
  - Correction to 11 Nov: his 9 Nov start was in Zion Williamson's spot. Zion returned 11 Nov, Bey went back to the bench (29 min, 21 FP) and Herbert Jones started for Murphy ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/pelicans-start-fears-murray-jones-zion-karlo)).
  - Verdict: *nothing new found*; 24–31 min either way.

### Ryan Rollins (MIL, PG/SG, free agent)

- Rate **24.7** · season 23.7 (12) · L7 25.4 (5) · L15 22.0 (8) · L30 23.7 (12) · projected 31.9
- ESPN: day-to-day, ESPN est. 13 Nov (Head, updated 2026-11-12)
- **Role:** news on 10 Nov: "Rollins will start in Tuesday's game against New York."
- News (11 Nov): Rollins (head) exited to the locker room in the fourth quarter of Wednesday's 123-112 loss to the Lakers and did not return, finishing with eight points (3-10 FG, 2-6 3Pt), seven rebounds, four assists and one steal across 24 minutes.
- News (11 Nov): Rollins exited to the locker room in the fourth quarter of Wednesday's game against the Lakers due to an apparent head injury, per the broadcast.
- **Research:**
  - His 10 Nov start was a one-off; back to the bench when Herro returned on 11 Nov, then left in the fourth quarter after hitting heads with Collin Sexton ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/ryan-rollins-injury-doesnt-return-wednesday-538705); [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/ryan-rollins-head-exits-during-fourth-quarter)). No timetable reported; ESPN est. 13 Nov.
  - Verdict: *nothing new found*.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **15.4** · role rate 22.3 · season 16.6 (11) · L7 12.7 (3) · L15 14.5 (8) · L30 16.6 (11) · projected 28.1
- ESPN: out, ESPN est. 15 Nov (Finger, updated 2026-11-11)
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 26.1 for the season
- **Role:** news on 08 Nov: "Grimes will start Sunday's game against the Pistons."
- News (11 Nov): Grimes (finger) has been ruled out for Wednesday's game against the Bucks.
- News (10 Nov): Grimes (finger) is listed as questionable for Wednesday's game in Milwaukee.
- **Research:**
  - Out 11 Nov, second straight; the swelling is on his shooting hand, assessed before 15 Nov vs PHX ([Basketnews, 12 Nov](https://basketnews.com/news-259304-jj-redick-drops-huge-quentin-grimes-injury-update-as-lakers-guard-still-out.html)). *ESPN est.* 15 Nov.
  - Verdict: *ESPN confirmed*.

### Nic Claxton (CHI, C, free agent)

- Rate **29.3** (small sample) · season 29.0 (2) · L7 29.0 (2) · L15 29.0 (2) · L30 29.0 (2) · projected 30.3
- ESPN: active
- **Minutes:** news on 09 Nov: "The big man is working under a minutes restriction, so fantasy managers will have to temper expectations initially."
- News (11 Nov): Claxton finished with 17 points (5-6 FG, 7-9 FT), six rebounds, one assist and one block in 16 minutes during Wednesday's 124-119 loss to the Spurs.
- News (09 Nov): Claxton provided four points (2-3 FG), four rebounds, four assists and two blocks across 18 minutes during Sunday's 127-121 loss to the 76ers.
- **Research:**
  - Still on the minutes limit: 17 pts in 16 min off the bench on 11 Nov; the roles with Jalen Smith reverse "not until Claxton's minutes restriction is lifted" ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes)). The limit is about 16–20 minutes ([K.C. Johnson, 8 Nov](https://x.com/KCJHoop/status/2119502033992458384)); Splitter said "small" minutes for "a few games" and may later start him beside Smith rather than in place of him ([Yahoo, 6 Nov](https://sports.yahoo.com/articles/nic-claxton-return-poses-lineup-201100231.html); [Hoops Rumors, 7 Nov](https://www.hoopsrumors.com/2026/11/bulls-notes-claxton-smith-buzelis-powell-trade-season.html)). Small sample (2 games).
  - Verdict: *ESPN confirmed*. Override: role 18 until 16 Nov (re-check; no end date set).

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.3** · role rate 28.7 · season 22.5 (10) · L7 37.0 (3) · L15 26.0 (7) · L30 22.5 (10) · projected 22.9
- ESPN: active
- **Minutes:** 29.3 min over his last 3 games against 23.1 for the season (+6.2)
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- News (05 Nov): Huerter supplied eight points (3-8 FG, 2-6 3Pt) and two blocks over 20 minutes during Wednesday's 112-106 loss to the 76ers.
- **Research:**
  - Isaiah Joe is out again 12 Nov at WSH; "Huerter and Javonte Green should continue to play additional minutes" ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/isaiah-joe-hip-remains-out-thursday-vs-was)).
  - Verdict: *nothing new found*.

### Rudy Gobert (MIN, C, free agent)

- Rate **30.3** · season 26.9 (10) · L7 33.7 (3) · L15 28.5 (6) · L30 26.9 (10) · projected 34.3
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (09 Nov): Gobert ended Sunday's 115-100 victory over Utah with 10 points (4-4 FG, 2-4 FT), 15 rebounds and two assists over 31 minutes.
- News (05 Nov): Gobert ended Wednesday's 117-107 victory over the Rockets with eight points (3-7 FG, 2-6 FT), 11 rebounds, two assists, four blocks and one steal over 33 minutes.
- **Research:**
  - MIN idle 9–11 Nov, hosts DAL 12 Nov; no injury listing found.
  - Verdict: *nothing new found*.

### Draymond Green (GS, PF/C, free agent)

- Rate **27.7** · season 25.0 (10) · L7 30.0 (4) · L15 28.4 (7) · L30 25.0 (10) · projected 28.5
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 08 Nov: "His season-high 13 assists and four combined defensive stats provided substantial category-league value, and it's worth noting he's now dished out double-digit assists in back-to-back games."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (08 Nov): Green recorded two points (1-5 FG, 0-1 3Pt, 0-2 FT), six rebounds, 13 assists, two steals and two blocks across 34 minutes in Saturday's 126-119 overtime win over the Magic.
- News (07 Nov): Green (elbow) is available for Saturday's game against the Magic.
- **Research:**
  - He sat one night of each back-to-back so far (24 Oct; 1 Nov, "low back management") ([Yahoo, 31 Oct](https://sports.yahoo.com/articles/steph-curry-draymond-green-ruled-144308312.html)). The next is 18–19 Nov; nothing announced.
  - Verdict: *nothing new found*.

### Robert Williams III (POR, C, free agent)

- Rate **27.3** · season 26.0 (9) · L7 29.2 (4) · L15 26.9 (7) · L30 26.0 (9) · projected 26.9
- ESPN: active
- **Rest:** back-to-back Mon 16–Tue 17 Nov; news on 09 Nov: "Williams (rest) isn't listed on the injury report ahead of Tuesday's game against the Thunder."; sat the second night of the 06–07 Nov back-to-back, playing the games either side
- News (09 Nov): Williams (rest) isn't listed on the injury report ahead of Tuesday's game against the Thunder.
- News (07 Nov): Williams (rest) won't play in Saturday's game against the Spurs.
- **Research:**
  - He did not sit: 15 min on 10 Nov and 17 min (24 FP) on 11 Nov ([AP via KRMG, 11 Nov](https://krmg.com/2026/11/11/trail-blazers-sweep-the-thunder-with-a-118-108-win/)). Yesterday's "almost assuredly sits" did not hold.
  - Verdict: *ESPN confirmed* (active); back-to-back calls are made on the day.

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:**
  - Partial plantar plate tear (right second toe); on-court work, re-evaluated in two weeks from 6 Nov, about 20 Nov ([Jazz, 6 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)). Nothing newer.
  - Verdict: *ESPN corrected* (est. 20 Nov is the re-evaluation, not a return). Override: return 21 Nov, a floor.

## Opponents: this week and next

### Stephen Curry (GS, PG, Lauri Birds)

- Rate **50.7** · season 44.4 (10) → 49.2 (9) · L7 37.8 (4) → 50.0 (3) · L15 47.6 (7) → 55.3 (6) · L30 44.4 (10) → 49.2 (9) · projected 43.0
- ESPN: day-to-day, ESPN est. 13 Nov (Right Abdomen Soreness, updated 2026-11-12)
- **Injury:** ESPN est. 13 Nov (Day-To-Day, Right Abdomen Soreness, updated 12 Nov), but the news said on 12 Nov: "Steve Kerr told reporters Wednesday that Curry said he tweaked something in his abdominal area and "had never done it before." Kerr added that the concern level is high, but they will await the MRI results, Kelly Iko of Yahoo Sports reports."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the first night of the 01–02 Nov back-to-back, playing the games either side
- News (12 Nov): Steve Kerr told reporters Wednesday that Curry said he tweaked something in his abdominal area and "had never done it before." Kerr added that the concern level is high, but they will await the MRI results, Kelly Iko of Yahoo Sports reports.
- News (11 Nov): Curry won't return to Wednesday's game against the Rockets due to right abdominal soreness, Anthony Slater of ESPN.com reports. He'll finish with three points (1-3 FG, 1-2 3Pt) across six minutes.
- **Research:**
  - Left 11 Nov vs HOU in the first quarter (6 min, 1 FP) with right abdominal soreness; Kerr: "concern is high, but I have no idea the extent of the injury"; MRI results pending ([Anthony Slater, 11 Nov](https://x.com/anthonyVslater/status/2120749228259700970); [Heavy, 12 Nov](https://heavy.com/sports/nba/golden-state-warriors/stephen-curry-injury-update-kerr-warriors-mri/)). RotoWire calls him "highly questionable" for 13 Nov at SA ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/stephen-curry-injury-headed-for-mri-538725)).
  - Rest: he sat one night of each earlier back-to-back; the next is 18–19 Nov ([Yahoo, 16 Oct](https://sports.yahoo.com/articles/tickets-see-steph-curry-steve-012901781.html); [The Sports Leader, 2 Nov](https://www.thesportsleader.com/2026/11/02/steph-curry-draymond-green-to-return-as-warriors-host-suns/)).
  - Verdict: *nothing new found* on a timeline; no timetable reported until the MRI. *ESPN est.* 13 Nov is unconfirmed.

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.5** · season 37.1 (11) · L7 35.0 (4) · L15 34.1 (7) · L30 37.1 (11) · projected 38.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Herro (knee) is listed as questionable for Wednesday's game against the Lakers."
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 09 Nov: "If the veteran guard is ultimately ruled out for the front end of this back-to-back set, Brayden Burries and Ryan Rollins would likely see expanded roles."; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- News (11 Nov): Herro (knee) is listed as available for Wednesday's game against the Lakers.
- **Research:**
  - Played 11 Nov vs LAL after missing 10 Nov with a right knee contusion: 35 min, 27 pts, 42 FP, no setback ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tyler-herro-knee-scores-27-points-in-return)). No rest plan reported; next back-to-back 18–19 Nov.
  - Verdict: *ESPN confirmed* (active).

### Jamal Shead (TOR, PG, Lauri Birds)

- Rate **28.5** · role rate 36.3 · season 24.9 (11) · L7 32.5 (4) · L15 30.0 (8) · L30 24.9 (11) · projected 20.7
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 9 before; 35.0 min in his starts, against 24.0 for the season
- **Minutes:** 30.7 min over his last 3 games against 24.0 for the season (+6.7)
- News (11 Nov): Shead won't start Wednesday's game against Boston, Sean Grande of NBC Sports Boston reports.
- News (09 Nov): Shead delivered 20 points (6-17 FG, 4-10 3Pt, 4-4 FT), two rebounds, 11 assists and two steals across 36 minutes during Monday's 118-102 loss to the Grizzlies.
- **Research:**
  - Quickley was cleared and started 11 Nov (28 min); Shead went back to the bench, 22 min, 13 FP ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jamal-shead-news-not-starting-wednesday-538655); [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/raptors-start-quickley-walter-rj-collin-poeltl)). His starting stint is over unless Quickley sits 12 Nov at PHI, the second night of a back-to-back ([Yahoo, 11 Nov](https://sports.yahoo.com/articles/raptors-major-lebron-james-joel-032900296.html)).
  - Verdict: *ESPN confirmed* (active, bench).

### Walker Kessler (LAL, C, Snow Time Lakers)

- Rate **48.0** · season 46.5 (13) → 49.3 (12) · L7 48.4 (5) · L15 46.2 (10) · L30 46.5 (13) → 49.3 (12) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 10 Nov: "He scored at least 20 points for the third time this year and the first time since back-to-back such performances to begin the campaign."
- News (10 Nov): Kessler recorded 21 points (8-12 FG, 5-6 FT), 10 rebounds, four assists, one block and one steal in 30 minutes during Monday's 124-114 victory over the Hawks.
- News (09 Nov): Kessler supplied 12 points (5-10 FG, 2-3 FT), 16 rebounds, four assists, three blocks and one steal over 29 minutes during Sunday's 121-116 win over the Pistons.
- **Research:**
  - Available 11 Nov with a left finger splint ([ClutchPoints, 11 Nov](https://clutchpoints.com/nba/los-angeles-lakers/lakers-news-walker-kessler-quentin-grimes-playing-bucks-injury-report)); 10 pts, 11 reb in 29 min ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/walker-kessler-records-10-11-3-1-1-line-vs-bucks)).
  - Verdict: *ESPN confirmed*.

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **41.0** · season 40.0 (11) · L7 40.5 (4) · L15 41.7 (7) · L30 40.0 (11) · projected 38.6
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the first night of the 30–31 Oct back-to-back, playing the games either side
- News (11 Nov): Brown ended Tuesday's 123-101 loss to the Celtics with 13 points (4-9 FG, 1-4 3Pt, 4-6 FT), five rebounds, two assists, one block and two steals in 26 minutes.
- News (08 Nov): Brown totaled 29 points (11-22 FG, 2-6 3Pt, 5-8 FT), seven rebounds, four assists and one steal across 35 minutes during Sunday's 127-121 victory over the Bulls.
- **Research:**
  - 26 min on 10 Nov from "foul trouble and the lopsided result", no injury ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jaylen-brown-news-struggles-vs-former-team-538576)).
  - Verdict: *nothing new found*.

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **40.8** · season 40.6 (9) · L7 38.5 (4) · L15 43.0 (6) · L30 40.6 (9) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 14–Sun 15 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (10 Nov): Irving delivered 35 points (11-18 FG, 7-10 3Pt, 6-7 FT) and four assists across 38 minutes in Monday's 125-122 win over the Pacers.
- News (09 Nov): Irving delivered 21 points (9-15 FG, 2-7 3Pt, 1-1 FT), three rebounds, four assists and one steal across 29 minutes in Sunday's 130-93 win over the Nets.
- **Research:**
  - Played both nights of 8–9 Nov (29 and 38 min) after a call made on the day ([SI, 9 Nov](https://www.si.com/nba/mavericks/onsi/kyrie-irving-injury-status-second-night-back-against-indiana-pacers-dallas-mavericks-)); nothing new for 14–15 Nov.
  - Verdict: *nothing new found*.

### Fred VanVleet (HOU, PG/SG, Snow Time Lakers)

- Rate **32.6** · season 33.1 (10) · L7 31.2 (4) · L15 33.6 (7) · L30 33.1 (10) · projected 33.4
- ESPN: active
- **Rest:** back-to-back Sun 15–Mon 16 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side
- News (10 Nov): VanVleet finished with 12 points (4-9 FG, 3-6 3Pt, 1-2 FT), a rebound and two assists across 30 minutes in Monday's 110-100 win over the Nuggets.
- News (08 Nov): VanVleet tallied 16 points (6-12 FG, 4-9 3Pt), three rebounds, four assists and a block across 31 minutes in Saturday's 102-99 loss to the Suns.
- **Research:**
  - Played 11 Nov vs GS: 18 pts, 6 ast, 3 stl in about 30 min ([NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/fred-vanvleet-tallies-18-points-six-assists)).
  - Verdict: *nothing new found*; the 16 Nov sit row stands.

### Jaxson Hayes (UTAH, C, Snow Time Lakers)

- Rate **24.6** · season 27.4 (11) · L7 23.0 (5) · L15 24.2 (8) · L30 27.4 (11) · projected 16.5
- ESPN: active
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 09 Nov: "On that note, he's played at least 28 minutes in back-to-back games, so his playing time seems to be trending up."; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (09 Nov): Hayes posted 18 points (6-6 FG, 6-7 FT), six rebounds, an assist and a block across 29 minutes in Sunday's 115-100 loss to the Timberwolves.
- News (05 Nov): Hayes closed with two points (1-2 FG), seven rebounds, one assist and one block in 21 minutes before fouling out of Wednesday's 120-113 overtime loss to New Orleans.
- **Research:**
  - Started on the second night of Utah's 10–11 Nov back-to-back ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/jazz-to-start-george-darryn-green-bailey-hayes)), playing both nights; his only absence was a shoulder injury.
  - Verdict: *ESPN confirmed*.

## Other rosters: injury flags only

### Giannis Antetokounmpo (MIA, PF/C, Dr White Slong)

- Rate **58.9** · season 58.4 (11) → 61.9 (10) · L7 55.0 (4) · L15 61.3 (7) · L30 58.4 (11) → 61.9 (10) · projected 57.6
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 10 Nov: "Antetokounmpo (wrist) is questionable for Tuesday's game against the Jazz."
- News (10 Nov): Antetokounmpo racked up 30 points (12-21 FG, 1-2 3Pt, 5-9 FT), 11 rebounds and four assists over 31 minutes in Tuesday's 115-109 win over the Jazz.
- News (10 Nov): Antetokounmpo (wrist) is available for Tuesday's game against Utah.
- **Research:**
  - Playing through the wrist sprain; Spoelstra: "something that he's able to play through right now" ([Miami Herald via Yahoo, 11 Nov](https://sports.yahoo.com/articles/heat-giannis-antetokounmpo-ready-move-180255826.html)). MIA back-to-back 13–14 Nov.
  - Verdict: *nothing new found*.

### Karl-Anthony Towns (NY, C, Melbourne poopoo)

- Rate **51.3** · season 48.4 (11) → 50.2 (10) · L7 53.5 (4) · L15 49.0 (8) → 51.7 (7) · L30 48.4 (11) → 50.2 (10) · projected 44.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "Towns (calf) is listed as questionable for Wednesday's game against Cleveland."
- News (11 Nov): Towns racked up 21 points (7-11 FG, 2-5 3Pt, 5-5 FT), 11 rebounds, eight assists and one block over 34 minutes in Wednesday's 115-107 loss to the Cavs.
- News (11 Nov): Towns (calf) is available for Wednesday's game against the Cavaliers, James L. Edwards III of The Athletic reports.
- **Research:**
  - Cleared from left calf soreness and played 11 Nov, 34 min, 56 FP ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/karl-anthony-towns-calf-available-wednesday)).
  - Verdict: *ESPN confirmed* (active).

### Keyonte George (UTAH, PG/SG, Cream Abdul-Yammar)

- Rate **36.2** · season 34.2 (11) · L7 42.0 (4) · L15 30.6 (7) · L30 34.2 (11) · projected 36.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 11 Nov: "George (ankle) is questionable for Wednesday's game against Orlando."
- News (11 Nov): George (ankle) is available for Wednesday's game against the Magic.
- News (11 Nov): George (ankle) is questionable for Wednesday's game against Orlando.
- **Research:**
  - Upgraded to available and started 11 Nov vs ORL after the right ankle sprain, 33 min, 23 FP ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/keyonte-george-ankle-upgraded-to-available-weds)).
  - Verdict: *ESPN confirmed* (active).

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Still out 11 Nov at UTA ([Magic, 11 Nov](https://www.nba.com/magic/news/orlando-magic-utah-jazz-game-preview-injury-report-20261111)); the only timeline is 4–6 weeks from 24 Oct ([ESPN](https://www.espn.com/nba/story/_/id/50266620/sources-magic-banchero-multiple-weeks-ankle-sprain)), about 21 Nov to 5 Dec.
  - Verdict: *nothing new found*; *ESPN est.* 22 Nov is the early end.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-12 06:05 UTC.
- [ESPN, 11 Nov](https://www.espn.com/nba/story/_/id/50458612/bulls-rookie-caleb-wilson-leaves-game-right-hand-injury)
- [Yahoo, 12 Nov](https://sports.yahoo.com/articles/caleb-wilson-injury-chicago-bulls-054028606.html)
- [Basketnews, 12 Nov](https://basketnews.com/news-259311-caleb-wilson-injury-latest-updates-as-bulls-rookie-exits-spurs-game.html)
- [Sun-Times, 11 Nov](https://chicago.suntimes.com/bulls/2026/11/11/bulls-rookie-caleb-wilson-answers-bell-sore-hip)
- [Tar Heel Tribune, 11 Nov](https://tarheeltribune.com/2026/11/11/tar-heels-in-pros-wilson-suffers-another-hand-injury-ingram-produces-third-career-g-league-triple-double/)
- [NBC Sports, 11 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-11/pelicans-start-fears-murray-jones-zion-karlo)
- [ESPN, 9 Nov](https://www.espn.com/nba/recap?gameId=401909959)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/dejounte-murray-scores-5-points-in-27-minutes)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/orleans-pelicans-dejounte-murray-problem-025055794.html)
- [CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-paul-george-out-wednesday/)
- [Heavy, 11 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-raptors-game-decision/)
- [Heavy, 2 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-paul-george-decision-rockets-game/)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes)
- [K.C. Johnson, 8 Nov](https://x.com/KCJHoop/status/2119502033992458384)
- [Yahoo, 6 Nov](https://sports.yahoo.com/articles/nic-claxton-return-poses-lineup-201100231.html)
- [Hoops Rumors, 7 Nov](https://www.hoopsrumors.com/2026/11/bulls-notes-claxton-smith-buzelis-powell-trade-season.html)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/aday-mara-plays-season-high-32-minutes-vs-por)
- [Heavy, 11 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/ajay-mitchell-injury-update-thunder-blazers-rematch)
- [SI, 11 Nov](https://www.si.com/nba/thunder/onsi/injury-report-okc-thunder-list-six-players-against-trail-blazers)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/ryan-rollins-injury-doesnt-return-wednesday-538705)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/ryan-rollins-head-exits-during-fourth-quarter)
- [Jazz, 6 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)
- [Yahoo, 31 Oct](https://sports.yahoo.com/articles/steph-curry-draymond-green-ruled-144308312.html)
- [Anthony Slater, 11 Nov](https://x.com/anthonyVslater/status/2120749228259700970)
- [Heavy, 12 Nov](https://heavy.com/sports/nba/golden-state-warriors/stephen-curry-injury-update-kerr-warriors-mri/)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/stephen-curry-injury-headed-for-mri-538725)
- [Yahoo, 16 Oct](https://sports.yahoo.com/articles/tickets-see-steph-curry-steve-012901781.html)
- [The Sports Leader, 2 Nov](https://www.thesportsleader.com/2026/11/02/steph-curry-draymond-green-to-return-as-warriors-host-suns/)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jamal-shead-news-not-starting-wednesday-538655)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/raptors-start-quickley-walter-rj-collin-poeltl)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/raptors-major-lebron-james-joel-032900296.html)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tyler-herro-knee-scores-27-points-in-return)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/karl-anthony-towns-calf-available-wednesday)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/keyonte-george-ankle-upgraded-to-available-weds)
- [Pelicans, 11 Nov](https://nba.com/pelicans/news/pelicans-shootaround-update-nets-tip-off-important-five-game-new-orleans-homestand)
- [FLM, 11 Nov](https://fieldlevelmedia.com/nba/nets-romp-as-slumping-pelicans-sustain-another-heavy-defeat/)
- [Sactown Sports, 10 Nov](https://sactownsports.com/nba/sacramento-kings/magic-loss)
- [FLM](https://fieldlevelmedia.com/nba/heat-look-to-reverse-course-vs-struggling-kings)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/magic-overpower-jazz-finish-2-045500670.html)
- [Hoops Rumors, 10 Nov](https://www.hoopsrumors.com/2026/11/pistons-notes-jenkins-lineup-collins-duren-okorie.html)
- [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/isaiah-joe-hip-remains-out-thursday-vs-was)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/brandon-miller-hip-remains-out-thursday-vs-phx)
- [SI, 11 Nov](https://www.si.com/nba/suns/onsi/phoenix-suns-reveal-encouraging-injury-report-charlotte-hornets)
- [CBS/RotoWire, 10 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-pours-in-27-points-six-triples-in-win/)
- [RotoWire, 10 Nov](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/pelicans-start-fears-murray-jones-zion-karlo)
- [Basketnews, 12 Nov](https://basketnews.com/news-259304-jj-redick-drops-huge-quentin-grimes-injury-update-as-lakers-guard-still-out.html)
- [AP via KRMG, 11 Nov](https://krmg.com/2026/11/11/trail-blazers-sweep-the-thunder-with-a-118-108-win/)
- [ClutchPoints, 11 Nov](https://clutchpoints.com/nba/los-angeles-lakers/lakers-news-walker-kessler-quentin-grimes-playing-bucks-injury-report)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/walker-kessler-records-10-11-3-1-1-line-vs-bucks)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jaylen-brown-news-struggles-vs-former-team-538576)
- [SI, 9 Nov](https://www.si.com/nba/mavericks/onsi/kyrie-irving-injury-status-second-night-back-against-indiana-pacers-dallas-mavericks-)
- [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/fred-vanvleet-tallies-18-points-six-assists)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/jazz-to-start-george-darryn-green-bailey-hayes)
- [Miami Herald via Yahoo, 11 Nov](https://sports.yahoo.com/articles/heat-giannis-antetokounmpo-ready-move-180255826.html)
- [Magic, 11 Nov](https://www.nba.com/magic/news/orlando-magic-utah-jazz-game-preview-injury-report-20261111)
- [ESPN](https://www.espn.com/nba/story/_/id/50266620/sources-magic-banchero-multiple-weeks-ankle-sprain)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/devin-vassell-groin-downgraded-to-out-wednesday)
- [Express-News via Yahoo, 10 Nov](https://sports.yahoo.com/articles/vassell-julian-champagnie-seizes-shot-205353349.html)
- [ClutchPoints, 11 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-tiago-splitter-target-date-norman-powell-return)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-ruled-out-wednesday-538653)
- [Dallas Sports Journal, 11 Nov](https://dallassportsjournal.com/mavericks-timberwolves-injury-report-morez-johnson-anthony-edwards/)
- [NetsDaily, 12 Nov](https://netsdaily.com/nets-scores-results/116020/nets-vs-pelicans-145-111-egor-demin-michael-porter-jr)
- [NBC Sports, 10 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-10/jordan-goodwin-calf-hits-six-triples-in-return)
- [CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-out-again-wednesday/)
- [HoopsHype, 11 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/11/rajakovic-says-that-barnes-groin-is-in-the-process/92734026007/)
