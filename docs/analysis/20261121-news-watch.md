# News watch: 21 Nov 2026

- Generated 2026-11-21 07:20 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 40 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

- **Our players:**
  - **Trey Murphy III** played Fri at OKC: 29 min off the bench, 17 pts, under a minutes restriction with no number given ([ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310)). **Saturday at SA, the second night of a back-to-back, is unannounced,** and he sat the second night of his last back-to-back with this knee. The Pelicans had not filed Saturday's report at 2:15 AM ET ([NBA injury report, 21 Nov 2:15 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)).
  - **Saddiq Bey** started again Fri (37 min). His role row is removed now that Murphy is back; his role rate and rate were the same anyway.
  - **Daniss Jenkins** keeps starting while Duncan Robinson is out (re-evaluation about 24 Nov; *ESPN est.* 27 Nov). His role row is 37 min until 23 Nov.
  - **Jalen Duren:** still out, to be re-evaluated next week; earliest game 24 Nov; *ESPN est.* 24 Nov. Row: return 24 Nov.
  - **Jalen Smith** sat out Fri with a gastrointestinal illness. No timetable reported; *ESPN est.* 22 Nov.
  - **Paul George:** not on Saturday's report. Boston's Sunday report is not filed yet, and he has one rest night in four back-to-backs.
  - **Anthony Black:** nothing new; his next back-to-back is 28–29 Nov.
- **Targets whose value moved:**
  - **Aday Mara** is a fixture in OKC's starting lineup while Chet Holmgren is out (8–10 weeks from 30 Oct; *ESPN est.* 2 Jan). New row: role 27 min until 5 Dec. His only game this week is Sun at MIA.
  - **Jaxson Hayes** has the Utah start back from Mo Bamba until Jusuf Nurkic is re-evaluated about 27 Nov. Rows: Hayes 26 min and Bamba 20 min, until 27 Nov.
  - **Kevin Huerter** starts for Detroit while Robinson is out. Row: 35 min until 24 Nov.
  - **Neemias Queta:** not on Boston's Saturday report. **Sunday at GS is the second night of a back-to-back,** and he rested 1 of 4.
  - **Quentin Grimes:** the Lakers have no game this weekend. Austin Reaves hopes to return Mon 23 Nov (*ESPN est.* 23 Nov).
- **ESPN dates corrected:**
  - **Dejounte Murray** is sitting out until New Orleans trades him (Charania, 13 Nov). ESPN's 27 Nov is a placeholder. The 26 Nov floor stays, with a fresh source.
  - **Ja Morant:** re-evaluated four weeks from 30 Oct ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). New row: return 28 Nov, a floor (*ESPN est.* 1 Dec).
  - **Jusuf Nurkic:** re-evaluated in one week from 20 Nov ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). Row moved from 26 Nov to 28 Nov (*ESPN est.* 29 Nov).
  - **Maxime Raynaud:** week-to-week. New row: return 25 Nov (*ESPN est.* 25 Nov).
- **Our opponent (Snow Time Lakers):**
  - **Jaylen Brown** is out Saturday with a hamstring strain, and Philadelphia has no Sunday game, so he gives them 0 games this week. He is re-evaluated this weekend; *ESPN est.* 23 Nov, a floor.
  - **Jayson Tatum** is questionable for rest Sat at SAC.
  - **Kyrie Irving** is a Sunday rest risk: he sat the second night of 2 of his 3 back-to-backs.
  - **Tyler Herro** (now with Milwaukee) plays only Saturday.
- **Overrides:**
  - **Added:** Mara (role 27), Hayes (role 26), Bamba (role 20), Huerter (role 35), Raynaud (return 25 Nov), Morant (return 28 Nov).
  - **Replaced:** Duren (return 24 Nov), Jenkins (role 37 until 23 Nov), Nurkic (return 28 Nov), Murray and Pippen (same floors, newer sources).
  - **Removed:** Grimes (expired), Bey (Murphy back).
  - **Not added:** Brandon Ingram. His debut is reported for Mon 23 Nov, the same as *ESPN est.* 23 Nov, and the source could not be opened to check it.
- **Re-run the matchup:** yes. The Mara, Hayes, Huerter and Jenkins rows touch this week's Sunday streams.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jusuf Nurkic | return | 2026-11-26 | — | [link](https://www.cbssports.com/fantasy/basketball/news/jazzs-jusuf-nurkic-not-ready-to-return-friday/) | in force |
| Jalen Duren | return | 2026-11-23 | — | [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) | in force |
| Scotty Pippen Jr. | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html) | in force |
| Dejounte Murray | return | 2026-11-26 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf) | in force |
| Saddiq Bey | role | 34 | 2026-11-24 | [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/) | in force |
| Daniss Jenkins | role | 35 | 2026-11-22 | [link](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html) | in force |
| Jalen Suggs | role | 30 | 2026-11-22 | [link](https://www.cbssports.com/fantasy/basketball/news/magics-jalen-suggs-hot-shooting-not-enough-in-loss/) | in force |
| Tyrese Proctor | role | 27 | 2026-11-22 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylon-tyson-ankle-out-wednesday-vs-grizzlies) | in force |
| Quentin Grimes | role | 36 | 2026-11-20 | [link](https://www.rotowire.com/basketball/headlines/austin-reaves-injury-still-out-friday-540088) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Trey Murphy III** | NO | us | minutes | 36.2 | — | active |
| **Saddiq Bey** | NO | us | minutes | 35.0 | 38.6 | active |
| **Daniss Jenkins** | DET | us | minutes | 33.3 | 37.8 | active |
| **Anthony Black** | ORL | us | rest | 36.0 | — | active |
| **Paul George** | BOS | us | rest | 35.5 | — | active |
| **Zach Edey** | MEM | free agent | injury | 29.4 | — | active |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 25 Nov |
| **Myles Turner** | MIL | free agent | injury, rest | 27.4 | — | active |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 24.7 | 24.0 | out, ESPN est. 27 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury | 16.3 | — | out, ESPN est. 25 Nov |
| **Bennedict Mathurin** | NO | free agent | injury | 4.6 | — | out, ESPN est. 27 Nov |
| **Aday Mara** | OKC | free agent | role | 36.4 | — | active |
| **Mo Bamba** | UTAH | waivers | role | 30.7 | 42.2 | active |
| **Jakob Poeltl** | TOR | free agent | role | 29.2 | — | active |
| **Jaxson Hayes** | UTAH | free agent | role, rest | 29.0 | — | active |
| **Kevin Huerter** | DET | free agent | role, minutes | 28.4 | 32.2 | active |
| **Grayson Allen** | CHA | free agent | role | 27.4 | 29.7 | out, ESPN est. 23 Nov |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 23.1 | 25.8 | out, ESPN est. 23 Nov |
| **Quentin Grimes** | LAL | free agent | minutes | 33.9 | 31.0 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 30.9 | 26.1 | out, ESPN est. 13 Dec |
| **De'Andre Hunter** | SAC | free agent | minutes | 30.2 | 27.5 | active |
| **Kasparas Jakucionis** | MIL | free agent | minutes | 29.3 | 26.3 | active |
| **P.J. Washington** | DAL | free agent | minutes | 28.8 | 23.4 | day-to-day, ESPN est. 21 Nov |
| **Dean Wade** | PHI | free agent | minutes | 27.1 | 27.1 | out, ESPN est. 23 Nov |
| **Precious Achiuwa** | SAC | free agent | minutes | 13.2 | 19.8 | out, ESPN est. 21 Nov |
| **Neemias Queta** | BOS | free agent | rest | 31.9 | — | active |
| **Ja Morant** | POR | free agent | gap | 34.1 | — | out, ESPN est. 01 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 44.1 | — | out, ESPN est. 23 Nov |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | minutes | 28.0 | — | active |
| **Cooper Flagg** | DAL | Matt Wright's Foxies | rest | 48.6 | — | active |
| **Jayson Tatum** | BOS | Snow Time Lakers | rest | 45.7 | — | day-to-day, ESPN est. 21 Nov |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 45.7 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 38.4 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 30.1 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 28.1 | — | active |
| **Jalen Brunson** | NY | Melbourne poopoo | injury | 46.4 | — | active |
| **Brandon Ingram** | LAC | Melbourne poopoo | injury | 36.5 | — | out, ESPN est. 23 Nov |
| **Kyle Kuzma** | MIL | Team Nic Kerr | injury | 26.4 | — | active |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 29 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 23.0 (1) → — · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - On 8 Nov the Pistons said he was cleared for on-court basketball work and would be re-evaluated in two weeks, which puts the check-up at about 22 Nov. Bickerstaff said: "We're not going to rush him." [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/); [NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring)
  - He was still out on 20 Nov vs TOR and is "set to be re-evaluated next week" [Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html); [NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf). The Pistons had not yet filed their report for Sun 22 at ATL as of 2:15 AM ET on 21 Nov. Nothing newer has been reported.
  - **Expected return:** no game date reported. The re-evaluation falls on about 22–23 Nov. Detroit plays Sun 22 at ATL and then Tue 24 at ORL, so 24 Nov is the earliest game he could play, and only if he is cleared. *ESPN est.* 24 Nov.
  - **Verdict:** ESPN confirmed, but treat 24 Nov as a floor. The re-evaluation is a check-up, not a return date.
  - Override proposed: return 2026-11-24

### Trey Murphy III (NO, SG/SF, us)

- Rate **36.2** · season 31.7 (10) · L7 38.0 (1) · L15 38.3 (3) · L30 31.7 (10) · projected 36.8
- ESPN: active
- **Minutes:** news on 20 Nov: "Murphy (knee) is available for Friday's game against Oklahoma City but will be under a minutes restriction, Clemente Almanza of USA Today reports."
- News (20 Nov): Murphy (knee) is available for Friday's game against Oklahoma City but will be under a minutes restriction, Clemente Almanza of USA Today reports.
- News (19 Nov): Murphy (knee) is questionable for Friday's game against the Thunder.
- **Research:**
  - He played Fri 20 Nov at OKC off the bench: 29 min, 17 pts (5-10 FG), 4 reb, 2 stl, 1 blk, in his first game since 8 Nov [ESPN box score, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310). Before the game Mosley said he would have a minutes restriction but gave no number [Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/orleans-pelicans-star-trey-murphy-005302582.html). He played 13 minutes in the first half. Rotoworld called it "close to a full workload" [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/trey-murphy-scores-17-against-thunder-in-return), and Roundtable wrote that the restriction was "seemingly thrown out the window" [Yahoo, 21 Nov](https://sports.yahoo.com/articles/orleans-pelicans-collapse-again-sga-041209508.html).
  - Sat 21 Nov at SA is the second night of a back-to-back, and the team has said nothing about it. The Pelicans' report for that game showed "NOT YET SUBMITTED" at 2:15 AM ET [NBA injury report, 21 Nov 2:15 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf). There is a risk he sits. His knee absence began when he missed the second night of the 8–9 Nov back-to-back [RotoWire, 10 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-expected-to-play-wednesday-538479), although he played both nights on 23–24 Oct and 28–29 Oct [ESPN game log](https://www.espn.com/nba/player/gamelog/_/id/4397688/trey-murphy-iii). A Yahoo auto-preview that lists him "inactive" for SA was written before he was upgraded on 20 Nov, so it does not count.
  - **Verdict:** ESPN confirmed: active. The restriction looked loose at 29 min. His Saturday status stays unknown until the Pelicans' game-day report, so check it before Saturday's add deadline.

### Saddiq Bey (NO, SF/PF, us)

- Rate **35.0** · role rate 38.6 · season 31.1 (17) · L7 41.0 (5) · L15 33.1 (9) · L30 31.1 (17) · projected 25.9
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.0 for the season (+7.3)
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- News (17 Nov): Bey finished with 23 points (8-15 FG, 5-8 3Pt, 2-2 FT), six rebounds, three assists, one steal and one block across 33 minutes in Monday's 115-94 win over Golden State.
- **Research:**
  - His minutes jumped because he has started in Murphy's place since 13 Nov. He still started Fri 20 Nov at OKC with Murphy back on the bench, and played 37 min for 21 pts [ESPN box score, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310). Dejounte Murray (ankle) and Bennedict Mathurin (plantar fasciitis) are also out [NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf).
  - No source says his starting role continues. Rotoworld expects him back on the bench once Murphy is fully back, and still a stream when Murphy sits [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/trey-murphy-scores-17-against-thunder-in-return). Before the injury he came off the bench in his first 10 games. If Murphy sits Sat at SA, Bey starts again.
  - **Verdict:** ESPN confirmed: active. The 37-min role was Murphy's absence and should shrink once Murphy's restriction is lifted. The existing Bey role row ("remove as soon as Murphy is cleared") has met its end condition. Remove it, or keep it only for Sat 21 Nov if Murphy is ruled out.

### Daniss Jenkins (DET, PG, us)

- Rate **33.3** · role rate 37.8 · season 30.1 (15) · L7 32.2 (4) · L15 40.7 (7) · L30 31.4 (14)
- ESPN: active
- **Minutes:** 37.7 min over his last 3 games against 29.9 for the season (+7.7)
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- News (18 Nov): Jenkins closed Tuesday's 105-93 win over the Spurs with 25 points (11-21 FG, 3-7 3Pt), five rebounds, five assists and one steal over 38 minutes.
- **Research:**
  - He started Fri 20 Nov vs TOR next to Cade Cunningham, who was back from knee soreness: 39 min, 14 pts. Isaiah Joe has returned but came off the bench (18 min) [ESPN box score, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308). As a starter he has played 42 (2OT), 35, 38, 36 and 39 min.
  - Duncan Robinson (left quad strain) will be re-evaluated one week after 17 Nov. He is expected to miss SA, NO, TOR and ATL and be checked before Tue 24 Nov at ORL [Lineups.com, 17 Nov](https://www.lineups.com/articles/pistons-duncan-robinson-out-at-least-one-week-with-left-quad-strain/); [Yahoo, 17 Nov](https://sports.yahoo.com/nba/breaking-news/article/duncan-robinson-pistons-second-leading-scorer-to-miss-at-least-a-week-with-left-quad-strain-171757062.html). Kevin Huerter, not Jenkins, has started in Robinson's place [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week). Jenkins's spot is tied more to Duren being out, so Duren's return (24 Nov at the earliest) is the likelier end. *ESPN est.* for Robinson: 27 Nov.
  - **Verdict:** ESPN confirmed: active. The starting role and about 37 min should hold for Sun 22 at ATL.
  - Override proposed: role 37

### Anthony Black (ORL, PG/SG, us)

- Rate **36.0** · season 38.3 (12) · L7 32.0 (4) · L15 39.4 (8) · L30 38.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- News (19 Nov): Black totaled 15 points (6-16 FG, 2-5 3Pt, 1-3 FT), two rebounds, six assists, one block and one steal in 37 minutes during Wednesday's 121-116 loss to the 76ers.
- **Research:**
  - Orlando plays at WAS on Sat 28 Nov and at DET on Sun 29 Nov. Nobody from the team or the beat has said he will sit either night. His only rest this season came on the second night of the 1–2 Nov back-to-back, and the team listed it as "left ankle injury management" [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/). He was off the injury report by 4 Nov [CBS/RotoWire, 4 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-removed-from-injury-report/) and played both nights of the 10–11 Nov back-to-back, 33 and 39 min [ESPN game log](https://www.espn.com/nba/player/gamelog/_/id/4712849/anthony-black). He was not on the 20 Nov report and played 37 min that night.
  - His role is safe for now. On 18 Nov Sweeney said Paolo Banchero (high ankle sprain) is "progressing" but has "no timeline right now" [Orlando Sentinel via Yahoo, 18 Nov](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html). *ESPN est.* for Banchero: 29 Nov. Orlando has no back-to-back this week (Sun 22 at WAS, Tue 24 vs DET).
  - **Verdict:** nothing new found. One ankle-management rest is not a pattern, so no sit row. Check the 28 Nov injury report.

### Paul George (BOS, SF/PF, us)

- Rate **35.5** · season 40.2 (13) · L7 32.0 (3) · L15 35.8 (6) · L30 37.6 (12) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (19 Nov): George supplied 10 points (3-12 FG, 1-7 3Pt, 3-3 FT), four rebounds, one assist, one block and three steals across 23 minutes before fouling out of Wednesday's 105-101 loss to Denver.
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - Saturday's official report (2:15 AM ET, 21 Nov) for BOS at SAC does not list George or Queta. Boston lists Tatum questionable (rest) and Derrick White questionable (left AC joint contusion; *ESPN est.* 21 Nov). The Sunday at GSW report is "not yet submitted" ([NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). This is Boston's fifth back-to-back in 17 games. Heavy says Tatum's availability "remains open" for both nights but says nothing of George ([Heavy, 20 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-jayson-tatum-decision-kings-game/)).
  - Rest pattern: George sat 2 Nov at HOU, listed "Rest" ([NBA report, 2 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf); ClutchPoints tied it to his age and injury history, [2 Nov](https://clutchpoints.com/nba/boston-celtics/celtics-news-paul-george-injury-update-rockets-showdown-bummer)). He sat 11 Nov vs TOR, listed "Illness" ([NBA report, 11 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_06_00PM.pdf)). He played both nights of 15–16 Nov (25 and 36 min) and was not on the 16 Nov report ([NBA report, 16 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_06_00PM.pdf)). That makes one true rest night in four back-to-backs. Boston usually decides the second night on game day, so Sunday's call may come after Sunday's add deadline (first tip 3:30 PM ET).
  - Form: L7 32.0 (3 games) is 8.2 under his 40.2 season average. He fouled out in 23 min on 18 Nov, and the 15 Nov game was a blowout (25 min).
  - **Verdict:** nothing new found. He is expected to play Saturday. There is no team or beat word on Sunday, and his record (1 rest, 1 illness in 4 back-to-backs) makes Sunday a real risk but not a confirmed sit.

## Free agents and waivers

### Zach Edey (MEM, C, free agent)

- Rate **29.4** · season 25.0 (12) · L7 36.0 (2) · L15 24.2 (5) · L30 25.0 (12) · projected 33.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Edey (hip) has been ruled out for Thursday's game against the Warriors."
- News (20 Nov): Edey (hip) is not listed on the injury report ahead of Saturday's game versus Minnesota.
- News (19 Nov): Edey (hip) has been ruled out for Thursday's game against the Warriors.
- **Research:**
  - The official report for Thu 19 Nov listed him Out for "Left Ankle Injury Management", not hip, on the second night of a back-to-back ([NBA injury report, 19 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). He is not on the report for Sat 21 Nov at MIN ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-cleared-to-play-saturday/); [NBA injury report, 21 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf)). A FanDuel auto-item from 20 Nov 3:45 AM UTC saying "out Sat" came before the team's report and is out of date.
  - He has missed both nights of the 13–14 Nov back-to-back and the second night of 18–19 Nov for the ankle. Memphis's next back-to-back is 1–2 Dec (@PHI, @DET), which is outside this week.
  - **Verdict:** ESPN confirmed. He is listed active and plays Sat 21 Nov. The "hip" label in the news was wrong.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:**
  - Still Out with a right patella subluxation for Fri 20 Nov at LAL ([NBA injury report, 20 Nov 7:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)). He was ruled out a full day ahead again on 18 Nov, "week-to-week" ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)). Kings insider James Ham says he is "progressing" but has no official timeline ([NBC/Rotoworld, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)). I found no report of team practice or a G League stint.
  - **Expected return:** no timetable reported. He is week-to-week from 18 Nov, so the floor is 25 Nov (SAC @GS). *ESPN est.* 25 Nov.
  - **Verdict:** ESPN confirmed, as a floor only. 25 Nov is 7 days after the week-to-week note, with no ramp-up reported, so it could slip.
  - Override proposed: return 2026-11-25

### Myles Turner (MIL, C, free agent)

- Rate **27.4** · season 26.6 (14) · L7 32.3 (3) · L15 21.8 (6) · L30 26.6 (14) · projected 28.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Turner has been ruled out for Thursday's game against Portland due to a left shoulder contusion."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (20 Nov): Turner (shoulder) is off the injury report for Saturday's game against the 76ers.
- News (19 Nov): Turner has been ruled out for Thursday's game against Portland due to a left shoulder contusion.
- **Research:**
  - He sat Thu 19 Nov vs POR with a left shoulder contusion ([NBA injury report, 19 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). He is off the report for Sat 21 Nov at PHI ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-myles-turner-absent-from-injury-report-540190/); [NBA injury report, 21 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf)).
  - Rest: the Bucks have not said he will sit either night of Fri 27 @DET / Sat 28 Nov vs OKC. Across Milwaukee's three back-to-backs so far, he played both nights of 23–24 Oct, sat 11 Nov for "Rest" ([NBA injury report, 11 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_30PM.pdf)), and missed 19 Nov with the shoulder. That makes two of three second nights missed, one of them for rest. It is a risk for 28 Nov, but not a stated sit.
  - **Verdict:** ESPN confirmed. He is active and plays 21 Nov. No sit row, because the team has said nothing about 28 Nov.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **24.7** · role rate 24.0 · season 30.6 (9) · L7 — · L15 14.5 (4) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - Charania reported he "will not play another minute" for New Orleans and will sit until his trade request is met ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)). There is "no traction" toward a deal, and trades are not expected before 15 Dec ([Yahoo, 20 Nov](https://sports.yahoo.com/articles/nba-trade-rumors-2026-27-183612093.html)).
  - Gap: he was still listed Out (left ankle sprain) for Fri 20 Nov at OKC ([NBA injury report, 20 Nov 7:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)). The Pelicans' report for 21 Nov @SA was not yet submitted. Minutes: the drop to 24.7 min over his last three games no longer matters while he is not playing.
  - **Expected return:** no timetable reported. He is out until traded. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is a placeholder, and he should not be expected back for New Orleans at all. Any return comes after a trade, probably mid-December or later.
  - Override proposed: return 2026-11-26

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **16.3** · season 14.2 (5) · L7 — · L15 — · L30 14.2 (5) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:**
  - The Grizzlies said on 16 Nov that he "continues to progress" from a lumbar disc herniation and is "considered week-to-week", with no re-evaluation date ([Yahoo/Roundtable, 16 Nov](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html)). He is Out again for Sat 21 Nov at MIN, his 12th straight miss ([NBA injury report, 21 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf)). I found no report of practice or a ramp-up.
  - **Expected return:** no timetable reported. The week-to-week floor is 23 Nov (MEM @CHA). *ESPN est.* 25 Nov.
  - **Verdict:** nothing new found. Neither date is backed by a report. The 23 Nov floor has not passed yet, so the row stays.

---
**Summary**
- Edey and Turner are both cleared for Sat 21 Nov. Edey's 19 Nov absence was officially "left ankle injury management", not hip. Turner has missed two of three back-to-back second nights (one for rest), so 28 Nov vs OKC is a risk, but no sit has been announced.
- Murray is out until traded, with "no traction" on a deal (20 Nov) and trades unlikely before 15 Dec. ESPN's 27 Nov is a placeholder; keep the 26 Nov floor row and remove it if he is traded.
- Raynaud (25 Nov floor, matching ESPN) and Pippen (23 Nov floor; ESPN 25 Nov) are both still week-to-week, with no timetable and no reported ramp-up.
  - Override proposed: return 2026-11-23

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **4.6** · season 8.8 (12) · L7 -3.0 (1) · L15 3.2 (4) · L30 8.8 (12) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - Injury: out Fri 20 Nov at OKC, his 4th straight game, with left plantar fasciitis ([NBA injury report, 20 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_11_45PM.pdf)). "Week-to-week" is RotoWire's own assessment, not a team statement ([RotoWire via CBS, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). I found no team or beat-writer timeline and no re-evaluation date. The Pelicans had not submitted their report for Sat 21 Nov at SAS as of 2:15 AM ET.
  - Week-to-week from 19 Nov gives a floor of 26 Nov. There are no NBA games that day (Thanksgiving), so NOP's first game after the floor is Fri 27 Nov at LAC, the same date as ESPN's. A row would change nothing, so I added none.
  - **Expected return:** no timetable reported (week-to-week per RotoWire, 19 Nov; earliest NOP game after the floor is 27 Nov); *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed. 27 Nov matches the week-to-week floor, and nothing newer was found.

### Aday Mara (OKC, C, free agent)

- Rate **36.4** · season 29.5 (16) · L7 42.0 (4) · L15 37.2 (8) · L30 30.5 (15)
- ESPN: active
- **Role:** news on 20 Nov: "Mara is now listed in the starting lineup for Friday's matchup with the Pelicans, Brandon Rahbar of DailyThunder.com reports."
- News (20 Nov): Mara posted 22 points (11-15 FG), 16 rebounds, two assists and two blocks across 29 minutes during Friday's 126-120 win over the Pelicans.
- News (20 Nov): Mara is now listed in the starting lineup for Friday's matchup with the Pelicans, Brandon Rahbar of DailyThunder.com reports.
- **Research:**
  - "The rookie has been a fixture in the starting lineup with Chet Holmgren (knee) sidelined." He posted 22 points and 16 rebounds in 29 min on 20 Nov ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/)). He has started 4 of the last 5 games and 6 of the last 8, with Daigneault back to a two-big lineup with Hartenstein while Holmgren is out. Peavy's listing as a starter was a late error that was corrected ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/thunder-start-shai-ajay-mccain-peavy-i-hart)). Holmgren (small patellar tendon tear) is out 8–10 weeks from 30 Oct, roughly 25 Dec to 8 Jan ([AP/NBA.com, 31 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan). His return ends the role.
  - Clifford: OKC acquired Nique Clifford, a wing, on 8 Nov ([ESPN, 8 Nov](https://www.espn.com/nba/story/_/id/50422647/thunder-get-nique-clifford-trade-kings-sources-say)). Clifford plays off the bench (16.8 min over his last 5), while Mara's minutes rose to 26.4 over his last 5 ([Yahoo/NBC minutes report, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)). So Clifford has had no visible effect on Mara. Mara's only recent bench game (15 Nov) came when Ajay Mitchell returned. Jaylin Williams came back on 18 Nov with 15–16 min off the bench ([NBC, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylin-williams-will-return-against-the-hawks)), and Mara still started 18 and 20 Nov.
  - Minutes in his last three games were 26, 27 and 29, whether he started or came off the bench. OKC's only game this weekend is Sun 22 Nov at MIA.
  - **Verdict:** ESPN corrected. The role is ongoing until Holmgren returns: about 27 min, with a starting spot that has flipped twice.
  - Override proposed: role 27

### Mo Bamba (UTAH, C, waivers)

- Rate **30.7** · role rate 42.2 · season 29.3 (13) · L7 35.8 (5) · L15 30.6 (8) · L30 29.3 (13)
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 20.8 for the season
- **Role:** news on 20 Nov: "Bamba is not listed in the starting lineup for Friday's game against Phoenix."
- News (20 Nov): Bamba is not listed in the starting lineup for Friday's game against Phoenix.
- News (18 Nov): Bamba had 15 points (6-7 FG, 1-2 3Pt, 2-2 FT), 10 rebounds, three assists and one block across 31 minutes during Tuesday's 132-107 victory over the Clippers.
- **Research:**
  - The start has ended. Hayes (knee) came back on 18 Nov and took the start back on 20 Nov vs PHX. Bamba came off the bench for 20 min (8 FP), and NBC says he can be dropped in redraft leagues. [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jazz-start-keyonte-darryn-green-ace-hayes)
  - The bench split is ongoing. The Jazz re-evaluate Nurkic (toe) again on 27 Nov, and NBC says Bamba and Hayes split the center minutes for at least four more games. Jaren Jackson Jr. (MCL) is out until mid-December. [Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jusuf-nurkic-toe-to-be-re-evaluated-in-one-week)
  - Expect about 20 min off the bench: 20 min on 20 Nov, 23 on 18 Nov, under 20 from 27 Oct to 11 Nov. He returns to about 30 only if Hayes sits. Hayes landed on his hip on 20 Nov and stayed in the game. [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jaxson-hayes-with-18-and-14-rebounds-in-loss)
  - **Verdict:** ESPN confirmed. He is back on the bench now that Hayes has returned, and he splits the minutes until Nurkic is back (27 Nov at the earliest).
  - Override proposed: role 20

### Jakob Poeltl (TOR, C, free agent)

- Rate **29.2** · season 26.4 (14) · L7 28.5 (4) · L15 33.4 (8) · L30 26.4 (14) · projected 31.7
- ESPN: active
- **Role:** news on 18 Nov: "Poeltl will start Wednesday's game against the Wizards."
- News (18 Nov): Poeltl will start Wednesday's game against the Wizards.
- News (18 Nov): Poeltl closed Tuesday's 111-102 loss to the Knicks with three points (1-3 FG, 1-2 FT), six rebounds, one assist and one steal over 18 minutes.
- **Research:**
  - He started 18 Nov, when Barrett (hamstring) and Barnes (groin) were out, and again 20 Nov at DET after Barnes returned, because Murray-Boyles is in the concussion protocol. Rookie Allen Graves took Murray-Boyles's spot. Poeltl played 32:13 for 10 pts and 9 reb in the 105-102 win. [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl) · [NBA.com box, 20 Nov](https://www.nba.com/pistons/game/0022600046-raptors-vs-pistons-detroit-mi-11-20-2026)
  - Murray-Boyles's return ends it. The Raptors gave no timeline, only a return-to-participation process, and his next chance is Mon 23 Nov vs MIL. With Murray-Boyles playing on 15 and 17 Nov, Poeltl came off the bench for 17–18 min. Barrett gets an update in two weeks. [NBA.com, 20 Nov](https://www.nba.com/news/raptors-updates-barrett-murray-boyles) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-lands-in-concussion-protocol/)
  - Expected minutes: about 30 while Murray-Boyles is out, about 18 off the bench once he's back.
  - **Verdict:** ESPN confirmed. The start lasts only while Murray-Boyles is out, and he could return 23 Nov, so I added no row.

### Jaxson Hayes (UTAH, C, free agent)

- Rate **29.0** · season 28.3 (14) · L7 31.7 (3) · L15 28.7 (7) · L30 28.3 (14) · projected 16.5
- ESPN: active
- **Role:** news on 20 Nov: "Hayes is listed in the starting lineup for Friday's game against the Suns."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side
- News (20 Nov): Hayes is listed in the starting lineup for Friday's game against the Suns.
- News (18 Nov): Hayes will come off the bench during Wednesday's game against the Lakers.
- **Research:**
  - He started 20 Nov vs PHX and played 28 min for 18 pts and 14 reb (39 FP). That was his 11th start in 13 games, and it came after one game off the bench on his return from the knee strain. [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jazz-start-keyonte-darryn-green-ace-hayes) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jaxson-hayes-with-18-and-14-rebounds-in-loss)
  - The start is ongoing while Nurkic (re-evaluated 27 Nov) and Jackson Jr. (MCL, mid-December) are out, with Bamba splitting the center minutes. Expect about 26 min: 25 off the bench on 18 Nov, 28 as a starter on 20 Nov, 24.4 for the season. [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jusuf-nurkic-toe-to-be-re-evaluated-in-one-week)
  - Rest: the team has said nothing about Sun 22 (vs DAL) or Mon 23 (at LAL). He missed 26 Oct with right shoulder soreness, not rest, and he played the second night of the 17–18 Nov back-to-back, so he has no rest pattern. [NBC Sports, 27 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/jaxson-hayes-shoulder-questionable-wednesday)
  - Watch: he landed on his hip in the 4th quarter on 20 Nov and stayed in. Utah's Sunday entry was still "not yet submitted" at 2:15 AM ET on 21 Nov. [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)
  - **Verdict:** ESPN confirmed. He is the starter, and nothing points to rest.
  - Override proposed: role 26

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **28.4** · role rate 32.2 · season 23.9 (15) · L7 30.0 (4) · L15 32.6 (7) · L30 24.9 (14) · projected 22.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 13 before; 36.0 min in his starts, against 26.7 for the season
- **Role:** news on 17 Nov: "Huerter will start in Tuesday's game against San Antonio."
- **Minutes:** 36.0 min over his last 3 games against 26.7 for the season (+9.3)
- News (19 Nov): Huerter had 11 points (2-9 FG, 1-4 3Pt, 6-7 FT), one rebound, seven assists, one block and one steal across 36 minutes during Wednesday's 122-109 victory over New Orleans.
- News (17 Nov): Huerter will start in Tuesday's game against San Antonio.
- **Research:**
  - He has started all three games since Duncan Robinson strained his left quad, playing 36, 36 and 36 min. That includes 20 Nov at TOR (35:55, 20 pts) with Cunningham (knee) and Isaiah Joe back. NBC says he should keep starting while Robinson is out, and that Robinson should miss at least 1–2 more games. [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kevin-huerter-scores-20-points-as-starter) · [NBA.com box, 20 Nov](https://www.nba.com/pistons/game/0022600046-raptors-vs-pistons-detroit-mi-11-20-2026)
  - Robinson's return ends it. The Pistons re-evaluate him one week from 17 Nov (about 24 Nov). Detroit plays Sun 22 at ATL and Tue 24 at ORL, so Robinson's earliest game is 25 Nov. [CBS/RotoWire (Detroit News), 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-duncan-robinson-to-be-re-evaluated-in-one-week/)
  - Minutes: the jump comes from Robinson's starting role (plus Cunningham missing 18 Nov), not from blowouts. Expect about 35 min through 24 Nov, then his 20–27 min bench role.
  - **Verdict:** ESPN confirmed. He keeps the start until Robinson returns, 25 Nov at the earliest.
  - Override proposed: role 35

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.4** · role rate 29.7 · season 26.8 (13) · L7 26.0 (1) · L15 29.0 (4) · L30 26.8 (13) · projected 26.6
- ESPN: out, ESPN est. 23 Nov (Concussion, updated 2026-11-19)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- News (17 Nov): Allen (concussion-like symptoms) has been ruled out for Tuesday's game against the Lakers.
- **Research:**
  - Injury: he was a late scratch 17 Nov and was out 20 Nov at ATL, listed on the official report as "Concussion Protocol". He has concussion-like symptoms and stays out until cleared, with no timeline given. [NBA injury report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_30PM.pdf) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/)
  - Role: his three starts came while Miller (groin) was out, and he went back to the bench on 15 Nov when Miller returned. Knueppel (hamstring) is re-evaluated about 6 Dec, four weeks from 8 Nov. Expect about 25–27 min off the bench once he is cleared. [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/)
  - **Expected return:** no timetable reported (concussion protocol). *ESPN est.* 23 Nov, which is Charlotte's next game (vs MEM), not a reported date.
  - **Verdict:** nothing new found. Nothing reported confirms 23 Nov, and he still has to clear the protocol.

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **23.1** · role rate 25.8 · season 19.2 (8) · L7 28.0 (2) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-19)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- News (18 Nov): Tyson (ankle) has been ruled out for Wednesday's game against Memphis.
- **Research:**
  - Injury: He has missed three straight games (16, 18 and 20 Nov). The official report lists "Right Ankle Injury Management" ([NBA injury report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_30PM.pdf)). This is the same ankle that cost him six games from 31 Oct to 9 Nov, and the Cavs have given no timetable ([Heavy, 20 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/injury-report-pacers-game-november-20)). Cleveland next plays Mon 23 Nov at CHI.
  - Role and minutes flags: He started 13 Nov at MIA "sans Mobley" (30 min) ([NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/cle-starts-harden-mitchell-tyson-watson-allen)) and again on 14 Nov vs DAL (34 min), the second night of a back-to-back. Evan Mobley (left great toe) is to be re-evaluated after 7–10 days of rehab from 16 Nov, which is about 23–26 Nov ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)). The starting job came with Mobley's absence and ends when Mobley returns. How many minutes Tyson gets when he comes back from the ankle has not been reported.
  - **Expected return:** no timetable reported. His next chance is Mon 23 Nov at CHI. *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. No source contradicts 23 Nov. The starts were tied to Mobley's absence, and no source calls the role ongoing, so no row.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **33.9** · role rate 31.0 · season 24.1 (15) · L7 44.8 (4) · L15 34.5 (6) · L30 24.1 (15) · projected 28.1
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 29.1 for the season (+8.3)
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- News (18 Nov): Grimes closed with 47 points (16-24 FG, 10-14 3Pt, 5-6 FT), six rebounds, three assists and one steal across 42 minutes during Tuesday's 118-114 overtime win over the Hornets.
- **Research:**
  - Austin Reaves (left heel contusion/bone bruise) was out again Friday ([NBA report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_00PM.pdf)). Grimes started with 35 min: 13 points, 5 rebounds, 7 assists and the go-ahead three in the 106-104 win ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/quentin-grimes-with-13-5-7-in-the-win-over-kings)).
  - Reaves expected return: Redick's "hope" is that he returns in one of the next two games, Mon 23 Nov vs UTA or Fri 27 Nov at SAS. NBC: "Grimes' starting time is likely ending" ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/redick-hope-is-reaves-returns-in-next-two-games)). *ESPN est.* 23 Nov.
  - The minutes jump (37.3 over his last 3) is the Reaves-injury starting role, not a lasting change. The Lakers have no game Sat 21 or Sun 22 Nov, so he cannot help this weekend. The 20 Nov role row has expired, and a new row is not warranted because the role may end at Monday's game.
  - **Verdict:** nothing new found. The role continues only until Reaves returns, possibly Mon 23 Nov.

### Caleb Wilson (CHI, SF, free agent)

- Rate **30.9** · role rate 26.1 · season 34.9 (10) · L7 — · L15 25.0 (2) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Injury: The Bulls say he had successful surgery on his fractured right hand on 12 Nov and "will be re-evaluated in three weeks", which is about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). On 20 Nov he joined practice in a hand brace, doing sprints and stretches only. ClutchPoints repeats Charania's report that he "will miss at least four to six weeks" ([ClutchPoints, 20 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-caleb-wilson-returns-to-practice-hand-surgery)).
  - Minutes flag: The 23.0-min L3 figure comes mostly from his 15-min exit with the hand injury on 11 Nov. It does not matter while he is out.
  - **Expected return:** at least 4–6 weeks from 12 Nov, which is 10–24 Dec, with a re-evaluation about 3 Dec. Chicago has no games from 4 to 12 Dec (Cup break), so its first game after the re-evaluation is 13 Dec vs HOU. *ESPN est.* 13 Dec.
  - **Verdict:** ESPN confirmed. 13 Dec sits inside the reported window and is the first Bulls game after the re-evaluation. No row: the re-evaluation rule would give 2026-12-04, but no CHI game falls before 13 Dec anyway, and "at least four weeks" puts the floor at 10 Dec.

### De'Andre Hunter (SAC, SF/PF, free agent)

- Rate **30.2** · role rate 27.5 · season 23.8 (13) · L7 38.0 (3) · L15 30.8 (5) · L30 23.8 (13) · projected 23.9
- ESPN: active
- **Minutes:** 38.0 min over his last 3 games against 33.0 for the season (+5.0)
- News (20 Nov): Hunter (hip) is listed as available for Friday's game against the Lakers.
- News (19 Nov): Hunter (hip) is listed as questionable for Friday's game against the Lakers.
- **Research:**
  - Minutes flag: The rise follows Precious Achiuwa's absence. Achiuwa missed 13 and 15 Nov, lasted 8 min off the bench on 18 Nov before re-injuring his leg, and was ruled out 20 Nov (lower-leg contusion). His next chance to play is Sat vs BOS ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/precious-achiuwa-leg-out-friday-vs-lakers); [SI, 20 Nov](https://www.si.com/nba/kings/onsi/kings-and-lakers-both-list-starters-on-injury-report-for-nba-cup-matchup)). Without Achiuwa, Keegan Murray starts and the Kings shorten the rotation to nine. Their starters played 36–40 min in the 106–104 loss on 20 Nov, with Hunter at 37 (30 pts) ([ESPN box, 20 Nov](https://www.espn.com/nba/game?gameId=401909313)). On 10 Nov, with Achiuwa starting, Hunter played 34.
  - Hunter's left hip soreness has put him on the questionable list three games running. He sat 15 Nov and was upgraded to available on 20 Nov ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-upgraded-to-available/)).
  - **Verdict:** nothing new found. The extra minutes depend on Achiuwa staying out (day-to-day) and on close games. No source calls the role ongoing, and the hip is a recurring risk.

### Kasparas Jakucionis (MIL, PG, free agent)

- Rate **29.3** · role rate 26.3 · season 20.4 (15) · L7 44.7 (3) · L15 24.6 (7) · L30 20.4 (15) · projected 20.2
- ESPN: active
- **Minutes:** 24.7 min over his last 3 games against 19.1 for the season (+5.5)
- News (20 Nov): Jakucionis logged 18 points (6-11 FG, 3-6 3Pt, 3-5 FT), three rebounds, two assists and one steal over 22 minutes during Thursday's 124-114 loss to the Trail Blazers.
- News (19 Nov): Jakucionis produced 20 points (6-8 FG, 3-5 3Pt, 5-6 FT), three rebounds, five assists and two steals over 26 minutes during Wednesday's 137-130 loss to Miami.
- **Research:**
  - Minutes flag: He played 26 min on 15 and 18 Nov while Ryan Rollins was out ill. NBC says Rollins's return "may lead to fewer minutes" for him ([NBC Sports, 15–19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kasparas-jakucionis-scores-career-high-25-in-loss)). On 19 Nov Rollins was back (21 min), but Kyle Kuzma and Myles Turner were out with shoulder contusions on the second night of a back-to-back ([NBA injury report, 19 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_07_30PM.pdf)), and he played 22. Kuzma and Turner are not listed for Sat at PHI ([NBA injury report, 21 Nov 1:30 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf)).
  - With a full rotation he played 4 min on 11 Nov and did not play (coach's decision) on 13 Nov ([ESPN box, 13 Nov](https://www.espn.com/nba/game/_/gameId/401909297)). CBS writes that "getting consistent minutes has been a problem". It also thinks a bigger role could come later, but that is the writer's guess ([CBS, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/week-6-fantasy-basketball-waiver-wire-targets/)).
  - **Verdict:** nothing new found. The bump came from teammates' absences, all of whom are now available, so it is not shown to be lasting.

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **28.8** · role rate 23.4 · season 28.2 (15) · L7 29.3 (3) · L15 28.3 (7) · L30 28.2 (15) · projected 26.9
- ESPN: day-to-day, ESPN est. 21 Nov (Shoulder, updated 2026-11-20)
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (20 Nov): Washington (shoulder) is listed as questionable for Saturday's game versus the Clippers.
- News (19 Nov): Washington posted 21 points (7-10 FG, 5-7 3Pt, 2-2 FT), five rebounds, two assists, three blocks and one steal over 25 minutes during Wednesday's 116-94 win over the Warriors.
- **Research:**
  - He is questionable for Sat 21 Nov vs LAC with a left shoulder impingement ([NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf); [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-p-j-washington-questionable-for-saturday-540205/)). No report says when he got hurt. Dallas plays at UTA on Sun 22 Nov, a back-to-back.
  - The minutes drop is game script, not a role change. He played 16 min in the 133-94 loss on 12 Nov because of foul trouble ([NBC Sports, 20 Nov page](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/p-j-washington-shoulder-questionable-vs-lac)), then 25 in the blowout loss to BOS on 15 Nov and 24:31 as a starter in the 116-94 win on 18 Nov ([Dallas Sports Journal, 20 Nov](https://dallassportsjournal.com/pj-washington-walter-clayton-questionable-mavericks-clippers/)). He is still in Kidd's starting five, so close games should restore about 30 min, but the shoulder now adds risk.
  - **Expected return:** questionable Sat 21 Nov, no timetable reported beyond that. *ESPN est.* 21 Nov.
  - **Verdict:** ESPN confirmed. He is day-to-day, and the minutes dip comes from blowouts and foul trouble.

Summary:
1. George and Queta are not on Boston's Saturday at SAC report. Sunday at GSW is unannounced, and both have rested on a back-to-back once (George 2 Nov, Queta 16 Nov). Expect a game-day call that may come after Sunday's add deadline. Tatum (rest) and White (AC joint) are questionable Saturday.
2. Mara's starting role (about 27 min) is ongoing until Holmgren returns (8–10 weeks from 30 Oct; *ESPN est.* 2 Jan). Clifford, a bench wing, has not cut into it. Role row added through 5 Dec. OKC plays only Sun 22 Nov this weekend.
3. Grimes' role lasts only until Reaves returns (hoped Mon 23 Nov; *ESPN est.* 23 Nov), and LAL has no weekend games. Washington is questionable Sat vs LAC (shoulder), with a Sunday back-to-back at UTA. His minutes drop was blowouts and foul trouble.

### Dean Wade (PHI, PF, free agent)

- Rate **27.1** · role rate 27.1 · season 21.5 (13) · L7 39.5 (2) · L15 21.0 (6) · L30 21.5 (13) · projected 16.3
- ESPN: out, ESPN est. 23 Nov (Left Hamstring Soreness, updated 2026-11-20)
- **Minutes:** 33.7 min over his last 3 games against 26.7 for the season (+7.0)
- News (20 Nov): Wade (hamstring) won't play Saturday against the Bucks.
- News (20 Nov): Wade (hamstring) participated in Friday morning's practice without restrictions, an encouraging sign for his availability for Saturday's game against the Bucks, per Tony Jones of The Athletic.
- **Research:**
  - Minutes: the 34, 35 and 32 min (12–16 Nov) came mostly from spot starts while LeBron James sat: back injury on 12 Nov ([TSN/AP, 12 Nov](https://www.tsn.ca/nba/article/maxey-embiid-lead-76ers-to-win-over-raptors-without-lebron/)) and the second night of a back-to-back on 16 Nov. Rotoworld says Wade "has mostly been a starter when healthy, filling in for LeBron James and Joel Embiid" and advises streaming him mainly when he starts ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/dean-wade-hamstring-remains-out-vs-milwaukee)). No source calls the bigger role ongoing, so no role row. L7 39.5 rests on 2 games (small sample).
  - Injury: out Sat 21 Nov vs MIL with left hamstring tightness/soreness ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). He practised fully on Friday, but the medical staff is "not quite ready to clear him". His next chance is Mon 23 Nov vs POR ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/dean-wade-injury-ruled-out-for-saturday-540198)).
  - **Expected return:** next chance Mon 23 Nov vs POR (RotoWire, 20 Nov), no firm timetable; *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. Out Saturday, aiming for Monday. The minutes spike came from spot starts, not a new role.

### Precious Achiuwa (SAC, PF/C, free agent)

- Rate **13.2** · role rate 19.8 · season 25.4 (12) · L7 -3.0 (1) · L15 14.8 (4) · L30 25.4 (12) · projected 24.1
- ESPN: out, ESPN est. 21 Nov (Left Lower Leg Bruise, updated 2026-11-20)
- **Minutes:** 19.3 min over his last 3 games against 24.8 for the season (−5.5)
- News (20 Nov): Achiuwa (lower leg) has been ruled out for Friday's game against the Lakers.
- News (19 Nov): Achiuwa is doubtful for Friday's game against the Lakers due to a left lower leg bruise.
- **Research:**
  - Minutes: the drop is down to injuries, not a role cut. He left the 10 Nov loss to Orlando in the 3rd quarter with a leg contusion (14 min) ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/precious-achiuwa-leg-exits-during-third-quarter)). He returned 18 Nov vs PHX and "appeared to tweak his leg" after 8 minutes ([Inside the Kings/SI, 20 Nov](https://www.si.com/nba/kings/onsi/kings-and-lakers-both-list-starters-on-injury-report-for-nba-cup-matchup)). He averages 24.8 min this season when healthy.
  - Injury: out Fri 20 Nov at LAL with a left lower leg contusion ([NBA injury report, 20 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_11_45PM.pdf)). His "next chance to play will come against Boston on Saturday" ([RotoWire via CBS, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-precious-achiuwa-ruled-out-friday/)). As of 2:15 AM ET 21 Nov, the Kings had not submitted their report for Saturday. Friday is his third absence in four games.
  - **Expected return:** no timetable reported beyond "next chance Sat 21 Nov vs BOS" (RotoWire, 20 Nov); *ESPN est.* 21 Nov.
  - **Verdict:** ESPN confirmed. ESPN's date is his next chance to play; he has not been cleared yet, and he has had repeated setbacks.

### Neemias Queta (BOS, C, free agent)

- Rate **31.9** · season 27.3 (14) · L7 38.0 (2) · L15 29.3 (6) · L30 27.8 (13) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- News (17 Nov): Queta (rest) is available for Wednesday's game against the Nuggets, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - He is not on Boston's Saturday at SAC report. The Sunday at GSW report is not yet submitted ([NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). There is no team or beat word on either night.
  - Rest pattern: he sat only the second night of 15–16 Nov, listed "Rest" ([NBA report, 16 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_06_00PM.pdf)), "as Boston manages his workload" ([NESN, 16 Nov](https://nesn.com/boston-celtics/news/why-neemias-queta-isnt-playing-tonight-vs-magic/4d25961bd26a8a5079076ef0)). He played both nights of the other three back-to-backs, including 22 and 31 min on 10–11 Nov. He was off the report for 18 Nov ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/neemias-queta-news-off-injury-report-539655)) and started that game, playing 27 min.
  - Form: L7 38.0 rests on 2 games (small sample).
  - **Verdict:** nothing new found. He is expected to play Saturday. Sunday is a possible but unannounced rest (1 rest in 4 back-to-backs), likely decided on game day after the Sunday add deadline.

### Ja Morant (POR, PG, free agent)

- Rate **34.1** · season 33.8 (4) · L7 — · L15 — · L30 33.8 (4) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:**
  - Gap flag: He is still out. He is listed Out (left hamstring strain) for Sat 21 Nov at NYK ([NBA injury report, 21 Nov 1:30 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf)), and Heavy says he is "projected to return later this month or in early December" ([Heavy, 20 Nov](https://heavy.com/sports/nba/portland-trail-blazers/injury-report-vs-knicks-november-21)). Portland's 30 Oct announcement said he "will be re-evaluated in four weeks", which is about 27 Nov ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). The latest team comment is Nori's on 7 Nov, that he "may not be out for as long as we thought", with no new timetable ([Heavy, 7 Nov](https://heavy.com/sports/nba/portland-trail-blazers/trail-blazers-ja-morant-injury-update/)). No reports of practice or on-court work turned up.
  - **Expected return:** re-evaluation about 27 Nov. The first possible game is Sun 29 Nov vs NOP; if he is not cleared then, Tue 1 Dec vs MIN. *ESPN est.* 1 Dec.
  - **Verdict:** ESPN corrected by the re-evaluation rule, one game earlier (29 Nov, not 1 Dec). This is a floor, not a confirmed return.
  - Override proposed: return 2026-11-28

## Opponents: this week and next

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **44.1** · season 40.8 (14) · L7 50.5 (2) · L15 40.2 (6) · L30 40.5 (13) · projected 38.6
- ESPN: out, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-20)
- **Injury:** ESPN est. 23 Nov (Out, Left Hamstring, updated 20 Nov), but the news said on 20 Nov: "Brown is set to be re-evaluated this weekend due to a left hamstring strain, meaning his next chance to play will come Monday against Portland."
- News (20 Nov): Brown (hamstring) went through individual work during Friday's practice, Tony Jones of The Athletic reports.
- News (18 Nov): Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com.
- **Research:**
  - Schedule: Brown plays for PHI, not BOS. PHI hosts MIL on Sat 21 Nov (1:00 PM ET) and has no game on Sun 22 Nov; SAC and GS are Boston's opponents. PHI's next game is Mon 23 Nov vs POR.
  - Injury: out Sat 21 Nov vs MIL with a left hamstring strain ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). He did only individual work at Friday's practice; Saturday will be his second straight missed game ([Sixers Wire via Yahoo, 20 Nov](https://sports.yahoo.com/articles/full-injury-report-jaylen-brown-220359363.html)). The re-evaluation "this weekend" will set his timeline ([Kris Rhim, ESPN, via Heavy/Yahoo, 18 Nov](https://sports.yahoo.com/articles/espn-insider-drops-latest-jaylen-013927700.html)).
  - **Expected return:** no timetable reported; he will be re-evaluated this weekend (Rhim, ESPN), so his earliest game is Mon 23 Nov vs POR; *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. 23 Nov is the day after the weekend re-evaluation; treat it as a floor, not a confirmed return. He has no games left for Snow Time Lakers this week.

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **28.0** · season 33.1 (14) · L7 20.5 (4) · L15 30.6 (8) · L30 33.1 (14) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (20 Nov): Podziemski closed with 15 points (5-12 FG, 0-5 3Pt, 5-6 FT), three rebounds, two assists and one steal in 32 minutes during Thursday's 126-98 loss to the Grizzlies.
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- **Research:**
  - His one low-minutes game (22 min, 13 Nov) came in a 123-85 blowout loss at San Antonio, [StatMuse box, 13 Nov](https://www.statmuse.com/nba/game/11-13-2026-gsw-at-sas-78603). In every other game since 1 Nov he has started and played 26–39 min, including 29 and 32 in his last two. "He's maintained roughly 30 minutes per game recently," [CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-three-point-drought-extends-in-loss/). The weaker output comes from his shooting (0-10 from three in his last two games), not his minutes.
  - Stephen Curry (oblique abdominal tear) will "be re-evaluated in two weeks," which falls about 26 Nov, [NBA.com, 13 Nov](https://www.nba.com/news/stephen-curry-out-abdominal-soreness); *ESPN est.* 12 Dec. Podziemski's extra usage lasts until Curry returns.
  - **Verdict:** nothing new found. His minutes are steady at about 30–33 and the dip was a blowout, so there is no role row.

### Cooper Flagg (DAL, SF/PF, Matt Wright's Foxies)

- Rate **48.6** · season 51.0 (14) · L7 44.3 (3) · L15 52.6 (7) · L30 51.0 (14) · projected 45.4
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (19 Nov): Flagg chipped in 33 points (11-15 FG, 3-5 3Pt, 8-8 FT), five rebounds, nine assists and four steals across 34 minutes during Wednesday's 116-94 victory over the Warriors.
- News (16 Nov): Flagg contributed 17 points (5-15 FG, 2-6 3Pt, 5-5 FT), three rebounds, four assists, one block and one steal in 27 minutes during Sunday's 131-94 loss to the Celtics.
- **Research:**
  - The flag's premise is wrong. On 24 Oct he sat with a mild left shoulder sprain (MRI), not for rest, [Yardbarker, 24 Oct](https://www.yardbarker.com/nba/articles/mavericks_make_2_starting_lineup_changes_with_kyrie_irving_cooper_flagg_out_vs_spurs/s1_17810_44470013). He played both nights of 8–9 Nov (28, 39 min) and 14–15 Nov (38, 27 min) (box scores).
  - He was ill on the road trip, but May said on 17 Nov it was "the first day he's woke up and felt good," [FanSided, 18 Nov](https://thesmokingcuban.com/dusty-may-cooper-flagg-update-gives-mavericks-hope-after-recent-struggles). He is not on the official report for Sat 21 Nov LAC@DAL, [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_00AM.pdf). No rest has been announced for Sun 22 at UTA.
  - **Verdict:** ESPN confirmed. He is active with no rest pattern, and should play both nights.

### Jayson Tatum (BOS, SF/PF, Snow Time Lakers)

- Rate **45.7** · season 45.9 (14) · L7 44.3 (3) · L15 46.4 (7) · L30 47.2 (13) · projected 48.1
- ESPN: day-to-day, ESPN est. 21 Nov (Rest, updated 2026-11-21)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 20 Nov: "Tatum (rest) is listed as questionable for Saturday's game against Sacramento."
- News (20 Nov): Tatum (rest) is listed as questionable for Saturday's game against Sacramento.
- News (19 Nov): Tatum had 24 points (10-22 FG, 3-8 3Pt, 1-2 FT), eight rebounds, three assists and one steal over 37 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:**
  - Rest: listed questionable ("Rest") for Sat 21 Nov at SAC, 10:00 PM ET ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). Boston had not yet filed for Sun 22 Nov at GS (8:30 PM ET). Rotoworld says Boston "may be looking to give Tatum a night off against Sacramento" ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jayson-tatum-rest-questionable-vs-sacramento)). I found no quote from Mazzulla or Stevens.
  - Pattern: he played both ends of all four back-to-backs this season (26–27 Oct, 1–2 Nov, 10–11 Nov, 15–16 Nov; our game log agrees). He said he is "not yet 100 percent" after the Dallas win ([Heavy, 20 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-jayson-tatum-decision-kings-game/)). His only rest game was Wed 4 Nov vs MIL, not on a back-to-back. He was listed questionable (rest) the day before ([NESN, 3 Nov](https://nesn.com/boston-celtics/news/celtics-face-unexpected-jayson-tatum-decision-bucks-game/c93117bec7a0859c91179818)) and then ruled out ([Heavy, 4 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-make-jayson-tatum-decision-ahead-of-bucks-game/)), the same sequence as now. That points to him sitting at SAC and playing at GS, but the team has not said he will sit, so I added no sit row.
  - **Expected return:** not injured, rest only. If he sits Saturday, he is expected back Sun 22 Nov at GS (no team statement); *ESPN est.* 21 Nov.
  - **Verdict:** ESPN confirmed. Questionable for rest on Saturday, the first night; the second night is not flagged.

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **45.7** · season 41.4 (12) · L7 54.5 (2) · L15 40.5 (6) · L30 41.4 (12) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "After sitting out the second game of a weekend back-to-back set, Irving returned to action and delivered decent numbers."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 14–15 Nov back-to-back, playing the games either side
- News (19 Nov): Irving supplied 17 points (7-15 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists and two steals over 29 minutes during Wednesday's 116-94 win over Golden State.
- News (17 Nov): Irving (knee) is not listed on the injury report ahead of Wednesday's game against the Warriors.
- **Research:**
  - Irving is not on the official report for Sat 21 Nov LAC@DAL. The Sun 22 Nov DAL@UTA report was "NOT YET SUBMITTED" at 2:00 AM ET 21 Nov, [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_00AM.pdf). Utah is the first stop of a three-game road trip, [Mavs.com, 20 Nov](https://www.nba.com/mavs/news/mavericks-clippers-preview-mavs-developing-their-identity-every-day-in-practice).
  - Dallas decides on the second night each morning. Dusty May: "play this game, and then let's see where we are tomorrow ... much more fluid on the second day of a back-to-back," [Dallas Sports Journal, 8 Nov](https://dallassportsjournal.com/kyrie-irving-mavericks-nets-pacers-back-to-back-status/).
  - Pattern: he has sat the second night of 2 of 3 back-to-backs, both listed as left knee injury management: 24 Oct ([Yardbarker, 24 Oct](https://www.yardbarker.com/nba/articles/mavericks_make_2_starting_lineup_changes_with_kyrie_irving_cooper_flagg_out_vs_spurs/s1_17810_44470013)) and 15 Nov, after 37 min the night before ([BasketNews, 15 Nov](https://basketnews.com/news-259537-why-kyrie-irving-will-not-play-vs-celtics-mavs-announce-huge-injury-update.html)). He played both nights of 8–9 Nov ([Yardbarker, 10 Nov](https://www.yardbarker.com/nba/articles/kyrie_irving_explains_decision_to_play_mavericks_back_to_back_after_acl_tear/s1_17810_44540702)). He also rested 2 Nov after five games in seven days ([HoopsHype, 2 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/02/mavericks-coach-dusty-may-said-kyrie-irving-is-resting/92576098007/)).
  - **Verdict:** nothing new found. He is expected to play Sat 21. Sun 22 at UTA is a real sit risk (2 of 3 second nights), but the team has made no statement, so there is no sit row.

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **38.4** · season 39.2 (15) · L7 34.5 (4) · L15 41.6 (7) · L30 39.2 (15) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (18 Nov): Siakam chipped in 24 points (10-17 FG, 2-2 3Pt, 2-2 FT), four rebounds, three assists, one block and three steals across 33 minutes during Wednesday's 119-104 loss to the Rockets.
- News (15 Nov): Siakam recorded 31 points (12-19 FG, 0-3 3Pt, 7-8 FT), two rebounds, two assists and one steal across 34 minutes during Sunday's 131-124 loss to Philadelphia.
- **Research:**
  - He sat for rest on 2 Nov, the second night of a back-to-back vs ATL, per the official report, [Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/pacers-resting-pascal-siakam-could-183414500.html). He played both nights of 25–26 Oct (26, 37 min, box scores). That makes 1 rest in 2 back-to-backs.
  - No team statement has been found for 22–23 Nov or 27–28 Nov. The IND@NYK Sun 22 report was "NOT YET SUBMITTED" at 2:00 AM ET 21 Nov, [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_00AM.pdf). If he sits, Mon 23 is the likelier night, but nothing has been announced.
  - **Verdict:** nothing new found. He is active, with a partial rest pattern and no announced sit.

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **30.1** · season 32.4 (15) → 34.5 (14) · L7 19.5 (4) → 25.0 (3) · L15 25.9 (7) → 29.7 (6) · L30 32.4 (15) → 34.5 (14) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (20 Nov): Herro totaled 19 points (7-13 FG, 4-7 3Pt, 1-3 FT), four rebounds, three assists and one steal over 31 minutes during Thursday's 124-114 loss to Portland.
- News (19 Nov): Herro ended Wednesday's 137-130 loss to Miami with eight points (4-11 FG, 0-5 3Pt, 0-1 FT), two rebounds, four assists and one steal over 24 minutes.
- **Research:**
  - Herro now plays for Milwaukee (MIL), not Miami. He is not on the official report for Sat 21 Nov MIL@PHI, 1:00 PM ET, [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_00AM.pdf). He is a projected starter and "not on the Bucks injury report," [Sports Mole, 20 Nov](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/milwaukee-bucks-vs-philadelphia-76ers-player-props-injury-report-and-prediction--nba_609484.html). MIL has no game Sun 22 (none on the 22 Nov report), so Saturday is his only game this weekend.
  - The flag's "rest" absence on 10 Nov was a right knee contusion, not rest, [SI, 9 Nov](https://www.si.com/nba/bucks/onsi/the-latest-on-tyler-herro-before-bucks-face-new-york-knicks-01m7151s3wta). He played both nights of the 23–24 Oct back-to-back (box scores). Nothing has been said about 27–28 Nov.
  - **Verdict:** ESPN confirmed. He is active and has no rest pattern.

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **28.1** · season 32.8 (12) · L7 20.5 (2) · L15 29.8 (5) · L30 32.8 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov, Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- News (19 Nov): Nembhard (hip) is questionable for Friday's game in Cleveland.
- **Research:**
  - Back from a two-game left hip sprain absence: available Fri 20 Nov at CLE ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-available-versus-cleveland/)), where he played 26 min (12 pts, 8 ast). The recap mentions no minutes limit ([IndyStar via Yahoo, 21 Nov](https://sports.yahoo.com/articles/james-harden-turns-back-clock-031319605.html)).
  - Rest: no rest announced for either back-to-back (Sun 22 @NYK–Mon 23 vs OKC; Fri 27 vs PHI–Sat 28 @CHI, per ESPN's schedule). The Pacers had not yet filed Sunday's report as of the 21 Nov 2:15 AM ET official report.
  - Both earlier second-night absences were filed as injuries, not rest: 26 Oct at MIL, "a back issue" per Carlisle after he hurt his neck the night before ([CBS/RotoWire, 26 Oct](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-out-vs-bucks/)); 2 Nov vs ATL, "cervical injury management", with the Pacers sitting several starters on the second leg ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-taking-night-off/); [official report, 2 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf)). Carlisle has said the Pacers won't publicize game-by-game plans ([IndyStar via Yahoo, 13 Mar](https://sports.yahoo.com/articles/rick-carlisle-pacers-rest-players-234624005.html)).
  - **Verdict:** nothing new found. No sit is announced, but he sat both earlier second nights under neck/back labels and is fresh off a hip sprain, so Mon 23 vs OKC and Sat 28 @CHI are real risks.

## Other rosters: injury flags only

### Jalen Brunson (NY, PG, Melbourne poopoo)

- Rate **46.4** · season 41.9 (15) · L7 50.0 (4) · L15 47.1 (7) · L30 43.4 (14) · projected 43.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Brunson exited to the locker room in the first quarter of Thursday's game against Minnesota due to an apparent facial injury, Jared Schwartz of the New York Post reports."
- News (20 Nov): Brunson amassed 21 points (8-20 FG, 4-5 3Pt, 1-1 FT), two rebounds, seven assists and two steals in 35 minutes during Thursday's 102-99 win over the Timberwolves.
- News (19 Nov): Brunson (face) returned to Thursday's game against the Timberwolves with 2:47 remaining in the first quarter, per the broadcast.
- **Research:**
  - He was hit in the face on a LaMelo Ball drive early in the first quarter on 19 Nov and returned with 2:47 left in that quarter. He finished with 35 min, 21 pts and 7 ast in the 102-99 win. No diagnosis was announced ([SportPreferred, 20 Nov](https://www.sportpreferred.com/nba/jalen-brunson-injury-update-knicks-timberwolves-2026/17719); [Bleacher Report](https://bleacherreport.com/articles/25535537-brunson-kat-carry-knicks-win-over-wolves-box-score-stats-highlights-lamelo-top-players)).
  - He is not on the Knicks' official injury report for Sat 21 Nov vs POR. The Knicks list only Anunoby (questionable) and Clarkson (out) ([official report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)).
  - **Verdict:** ESPN confirmed. He missed no time, and his absence from ESPN's injury feed is correct.

### Brandon Ingram (LAC, SF/PF, Melbourne poopoo)

- Rate **36.5** · season — · L7 — · L15 — · L30 — · projected 38.5
- ESPN: out, ESPN est. 23 Nov (Right Achilles Surgery, updated 2026-11-20)
- **Injury:** ESPN est. 23 Nov (Out, Right Achilles Surgery, updated 20 Nov), but the news said on 20 Nov: "The star forward is set to make his long-awaited return after undergoing surgery for a partially torn Achilles tendon in May. Ingram, who'll miss Saturday's game in Dallas, is likely to carry a minutes restriction following a lengthy layoff, though his presence is certain to cut into the playing time of the likes of Kris Dunn, Max Strus and Gradey Dick on the wing for the Clippers."
- News (20 Nov): Ingram (Achilles) is expected to make his season and team debut Monday against the Rockets, per Shams Charania of ESPN.
- News (18 Nov): Ingram (heel/Achilles) will remain on the inactive list for Thursday's game in San Antonio.
- **Research:**
  - He is expected to make his season and Clippers debut Mon 23 Nov vs HOU, per Shams Charania ([ESPN, 20 Nov](https://www.espn.com/nba/story/_/id/50542985/sources-clippers-brandon-ingram-make-season-team-debut); same story [via ABC30](https://abc30.com/post/sources-brandon-ingram-achilles-expected-clippers-debut-rockets/20060407/); [NBC Sports, 20 Nov](https://www.nbcsports.com/nba/news/brandon-ingram-reportedly-set-to-return-to-clippers-monday-against-rockets)). He is listed out for Sat 21 Nov at DAL (right heel surgery) ([official report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)).
  - A minutes restriction is expected ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-brandon-ingram-set-for-season-debut-monday/)), but no source gives a number.
  - **Expected return:** Mon 23 Nov vs HOU, as reported (likely on a minutes limit); *ESPN est.* 23 Nov.
  - **Verdict:** ESPN confirmed. The reported debut date matches ESPN's estimate.
  - Override proposed: return 2026-11-23

### Kyle Kuzma (MIL, SF/PF, Team Nic Kerr)

- Rate **26.4** · season 25.4 (15) · L7 26.7 (3) · L15 27.7 (7) · L30 25.4 (15) · projected 23.3
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Kuzma (shoulder) has been ruled out for Thursday's game against Portland due to a right shoulder contusion."
- News (20 Nov): Kuzma (shoulder) is off the injury report for Saturday's game against the 76ers.
- News (19 Nov): Kuzma (shoulder) has been ruled out for Thursday's game against Portland due to a right shoulder contusion.
- **Research:**
  - He missed Thu 19 Nov vs POR with a right shoulder contusion ([official report, 19 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). He is off the injury report for Sat 21 Nov at PHI ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kyle-kuzma-shoulder-off-injury-report-vs-76ers)). The 21 Nov 2:15 AM ET official report lists only Dieng, Jones and Markovic for the Bucks ([official report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)).
  - **Expected return:** Sat 21 Nov at PHI (cleared); ESPN lists him active, so it gives no estimate.
  - **Verdict:** ESPN confirmed. The miss was one game, and he is cleared for Saturday.

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - He was still out Fri 20 Nov at BKN with a right high ankle sprain ([official report, 20 Nov 8:00 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_00PM.pdf)). Banchero said he hopes to return "within the next couple of weeks." Coach Sweeney said on 18 Nov: "He's progressing… No timeline right now" ([Orlando Sentinel via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-banchero-shares-110000466.html)).
  - His work is behind the scenes, including pool sessions and some shooting, and it is unclear whether he is running. The report says he likely needs several more weeks ([Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4)).
  - **Expected return:** no timetable reported by the team; his own target is about 2 Dec ("next couple of weeks" from 18–19 Nov); *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. 29 Nov falls inside his own two-week hope, but with no team timeline it is optimistic rather than wrong.

Summary:
- Ingram's debut is reported for Mon 23 Nov vs HOU, matching ESPN, probably on a minutes limit (one return row). Brunson (face) and Kuzma (shoulder) are both cleared for Saturday.
- Nembhard is back from his hip sprain (26 min Fri). No rest is announced for Mon 23 or Sat 28, but he sat both earlier second nights under neck/back labels, so treat those nights as at risk.
- Banchero has no team timeline. His own "couple of weeks" target (about 2 Dec) is slightly later than ESPN's 29 Nov estimate, and no row was added.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-21 07:20 UTC.
- **Research, 21 Nov:** [ESPN box, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909310) · [NBA injury report, 21 Nov 2:15 AM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf) · [KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) · [Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) · [link](https://www.cbssports.com/fantasy/basketball/news/jazzs-jusuf-nurkic-not-ready-to-return-friday/) · [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) · [link](https://sports.yahoo.com/articles/grizzlies-gg-jackson-ii-needs-172020038.html) · [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf) · [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/) · [link](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html) · [link](https://www.cbssports.com/fantasy/basketball/news/magics-jalen-suggs-hot-shooting-not-enough-in-loss/) · [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylon-tyson-ankle-out-wednesday-vs-grizzlies) · [link](https://www.rotowire.com/basketball/headlines/austin-reaves-injury-still-out-friday-540088) · [NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring) · [Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html) · [NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf) · [Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/orleans-pelicans-star-trey-murphy-005302582.html) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/trey-murphy-scores-17-against-thunder-in-return) · [Yahoo, 21 Nov](https://sports.yahoo.com/articles/orleans-pelicans-collapse-again-sga-041209508.html) · [RotoWire, 10 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-expected-to-play-wednesday-538479) · [ESPN game log](https://www.espn.com/nba/player/gamelog/_/id/4397688/trey-murphy-iii) · [ESPN box score, 20 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909308) · [Lineups.com, 17 Nov](https://www.lineups.com/articles/pistons-duncan-robinson-out-at-least-one-week-with-left-quad-strain/) · [Yahoo, 17 Nov](https://sports.yahoo.com/nba/breaking-news/article/duncan-robinson-pistons-second-leading-scorer-to-miss-at-least-a-week-with-left-quad-strain-171757062.html) · [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week) · [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/) · [CBS/RotoWire, 4 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-removed-from-injury-report/) · [ESPN game log](https://www.espn.com/nba/player/gamelog/_/id/4712849/anthony-black) · [Orlando Sentinel via Yahoo, 18 Nov](https://sports.yahoo.com/articles/no-timeline-set-magic-paolo-204500820.html) · [Heavy, 20 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-jayson-tatum-decision-kings-game/) · [NBA report, 2 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-02_06_00PM.pdf) · [2 Nov](https://clutchpoints.com/nba/boston-celtics/celtics-news-paul-george-injury-update-rockets-showdown-bummer) · [NBA report, 11 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_06_00PM.pdf) · [NBA report, 16 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_06_00PM.pdf) · [NBA injury report, 19 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-zach-edey-cleared-to-play-saturday/) · [NBA injury report, 21 Nov 1:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_01_30AM.pdf) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/) · [NBC/Rotoworld, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-myles-turner-absent-from-injury-report-540190/) · [NBA injury report, 11 Nov 5:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_30PM.pdf) · [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) · [Yahoo, 20 Nov](https://sports.yahoo.com/articles/nba-trade-rumors-2026-27-183612093.html) · [NBA injury report, 20 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_11_45PM.pdf) · [RotoWire via CBS, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/thunder-start-shai-ajay-mccain-peavy-i-hart) · [AP/NBA.com, 31 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear) · [ESPN, 8 Nov](https://www.espn.com/nba/story/_/id/50422647/thunder-get-nique-clifford-trade-kings-sources-say) · [Yahoo/NBC minutes report, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html) · [NBC, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylin-williams-will-return-against-the-hawks) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jazz-start-keyonte-darryn-green-ace-hayes) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jusuf-nurkic-toe-to-be-re-evaluated-in-one-week) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/jaxson-hayes-with-18-and-14-rebounds-in-loss) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl) · [NBA.com box, 20 Nov](https://www.nba.com/pistons/game/0022600046-raptors-vs-pistons-detroit-mi-11-20-2026) · [NBA.com, 20 Nov](https://www.nba.com/news/raptors-updates-barrett-murray-boyles) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-lands-in-concussion-protocol/) · [NBC Sports, 27 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/jaxson-hayes-shoulder-questionable-wednesday) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kevin-huerter-scores-20-points-as-starter) · [CBS/RotoWire (Detroit News), 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-duncan-robinson-to-be-re-evaluated-in-one-week/) · [NBA injury report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_30PM.pdf) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/) · [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/) · [Heavy, 20 Nov](https://heavy.com/sports/nba/cleveland-cavaliers/injury-report-pacers-game-november-20) · [NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/cle-starts-harden-mitchell-tyson-watson-allen) · [Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116) · [NBA report, 20 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_08_00PM.pdf) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/quentin-grimes-with-13-5-7-in-the-win-over-kings) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/redick-hope-is-reaves-returns-in-next-two-games) · [Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update) · [ClutchPoints, 20 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-caleb-wilson-returns-to-practice-hand-surgery) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/precious-achiuwa-leg-out-friday-vs-lakers) · [SI, 20 Nov](https://www.si.com/nba/kings/onsi/kings-and-lakers-both-list-starters-on-injury-report-for-nba-cup-matchup) · [ESPN box, 20 Nov](https://www.espn.com/nba/game?gameId=401909313) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-upgraded-to-available/) · [NBC Sports, 15–19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kasparas-jakucionis-scores-career-high-25-in-loss) · [NBA injury report, 19 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_07_30PM.pdf) · [ESPN box, 13 Nov](https://www.espn.com/nba/game/_/gameId/401909297) · [CBS, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/week-6-fantasy-basketball-waiver-wire-targets/) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-p-j-washington-questionable-for-saturday-540205/) · [NBC Sports, 20 Nov page](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/p-j-washington-shoulder-questionable-vs-lac) · [Dallas Sports Journal, 20 Nov](https://dallassportsjournal.com/pj-washington-walter-clayton-questionable-mavericks-clippers/) · [TSN/AP, 12 Nov](https://www.tsn.ca/nba/article/maxey-embiid-lead-76ers-to-win-over-raptors-without-lebron/) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/dean-wade-hamstring-remains-out-vs-milwaukee) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/dean-wade-injury-ruled-out-for-saturday-540198) · [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/precious-achiuwa-leg-exits-during-third-quarter) · [RotoWire via CBS, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-precious-achiuwa-ruled-out-friday/) · [NESN, 16 Nov](https://nesn.com/boston-celtics/news/why-neemias-queta-isnt-playing-tonight-vs-magic/4d25961bd26a8a5079076ef0) · [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/neemias-queta-news-off-injury-report-539655) · [Heavy, 20 Nov](https://heavy.com/sports/nba/portland-trail-blazers/injury-report-vs-knicks-november-21) · [Heavy, 7 Nov](https://heavy.com/sports/nba/portland-trail-blazers/trail-blazers-ja-morant-injury-update/) · [Sixers Wire via Yahoo, 20 Nov](https://sports.yahoo.com/articles/full-injury-report-jaylen-brown-220359363.html) · [Kris Rhim, ESPN, via Heavy/Yahoo, 18 Nov](https://sports.yahoo.com/articles/espn-insider-drops-latest-jaylen-013927700.html) · [StatMuse box, 13 Nov](https://www.statmuse.com/nba/game/11-13-2026-gsw-at-sas-78603) · [CBS Sports, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-three-point-drought-extends-in-loss/) · [NBA.com, 13 Nov](https://www.nba.com/news/stephen-curry-out-abdominal-soreness) · [Yardbarker, 24 Oct](https://www.yardbarker.com/nba/articles/mavericks_make_2_starting_lineup_changes_with_kyrie_irving_cooper_flagg_out_vs_spurs/s1_17810_44470013) · [FanSided, 18 Nov](https://thesmokingcuban.com/dusty-may-cooper-flagg-update-gives-mavericks-hope-after-recent-struggles) · [NBA injury report, 21 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_00AM.pdf) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jayson-tatum-rest-questionable-vs-sacramento) · [NESN, 3 Nov](https://nesn.com/boston-celtics/news/celtics-face-unexpected-jayson-tatum-decision-bucks-game/c93117bec7a0859c91179818) · [Heavy, 4 Nov](https://heavy.com/sports/nba/boston-celtics/celtics-make-jayson-tatum-decision-ahead-of-bucks-game/) · [Mavs.com, 20 Nov](https://www.nba.com/mavs/news/mavericks-clippers-preview-mavs-developing-their-identity-every-day-in-practice) · [Dallas Sports Journal, 8 Nov](https://dallassportsjournal.com/kyrie-irving-mavericks-nets-pacers-back-to-back-status/) · [BasketNews, 15 Nov](https://basketnews.com/news-259537-why-kyrie-irving-will-not-play-vs-celtics-mavs-announce-huge-injury-update.html) · [Yardbarker, 10 Nov](https://www.yardbarker.com/nba/articles/kyrie_irving_explains_decision_to_play_mavericks_back_to_back_after_acl_tear/s1_17810_44540702) · [HoopsHype, 2 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/02/mavericks-coach-dusty-may-said-kyrie-irving-is-resting/92576098007/) · [Yahoo Sports, 2 Nov](https://sports.yahoo.com/articles/pacers-resting-pascal-siakam-could-183414500.html) · [Sports Mole, 20 Nov](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/milwaukee-bucks-vs-philadelphia-76ers-player-props-injury-report-and-prediction--nba_609484.html) · [SI, 9 Nov](https://www.si.com/nba/bucks/onsi/the-latest-on-tyler-herro-before-bucks-face-new-york-knicks-01m7151s3wta) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-available-versus-cleveland/) · [IndyStar via Yahoo, 21 Nov](https://sports.yahoo.com/articles/james-harden-turns-back-clock-031319605.html) · [CBS/RotoWire, 26 Oct](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-out-vs-bucks/) · [CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-taking-night-off/) · [IndyStar via Yahoo, 13 Mar](https://sports.yahoo.com/articles/rick-carlisle-pacers-rest-players-234624005.html) · [SportPreferred, 20 Nov](https://www.sportpreferred.com/nba/jalen-brunson-injury-update-knicks-timberwolves-2026/17719) · [Bleacher Report](https://bleacherreport.com/articles/25535537-brunson-kat-carry-knicks-win-over-wolves-box-score-stats-highlights-lamelo-top-players) · [ESPN, 20 Nov](https://www.espn.com/nba/story/_/id/50542985/sources-clippers-brandon-ingram-make-season-team-debut) · [via ABC30](https://abc30.com/post/sources-brandon-ingram-achilles-expected-clippers-debut-rockets/20060407/) · [NBC Sports, 20 Nov](https://www.nbcsports.com/nba/news/brandon-ingram-reportedly-set-to-return-to-clippers-monday-against-rockets) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-brandon-ingram-set-for-season-debut-monday/) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/kyle-kuzma-shoulder-off-injury-report-vs-76ers) · [Orlando Sentinel via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-banchero-shares-110000466.html) · [Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4)
