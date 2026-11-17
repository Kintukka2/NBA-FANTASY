# News watch: 17 Nov 2026

- Generated 2026-11-17 21:18 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 52 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 98 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 41 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

**Moves recorded by the ESPN sync (17 Nov):** Trey Murphy III dropped, Mo Bamba added. 2 of 7 adds used.

**Our players:**
- **Trey Murphy III** (now a free agent): ruled out for 18 Nov vs DET, his sixth straight ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-another-absence-coming-539612)). No timetable reported; *ESPN est.* 20 Nov.
- **Saddiq Bey:** starts while Murphy is out, at 33–41 min ([CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)). Role row: 34 min to 24 Nov.
- **Daniss Jenkins:** projected starter tonight at SA ([DBB via Yahoo, 17 Nov](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html)). Role row: 35 min to 22 Nov.
- **Jalen Duren** (IR): re-evaluated about 22 Nov ([Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)); *ESPN est.* 24 Nov. His return is what ends Jenkins's start.
- **Scottie Barnes:** a late addition as questionable tonight (17 Nov vs NY) with an illness ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/scottie-barnes-injury-late-addition-to-injury-report-539587)). No timetable reported; *ESPN est.* 17 Nov.
- **Jalen Smith:** took a head knock on 16 Nov but is not on Chicago's 18 Nov report.
- **Paul George:** no rest announced. He played both nights of 15–16 Nov, and 22 Nov (the second night) is a pattern risk only.
- **Kawhi Leonard:** out tonight, his 12th straight. The update the Raptors promised for about 17 Nov has not come ([Yahoo, 11 Nov](https://sports.yahoo.com/articles/kawhi-leonards-knee-keeps-raptors-200300316.html)); *ESPN est.* 23 Nov.
- **Yves Missi:** still about 22–23 min; no end date for the limit.

**Snow Time Lakers:**
- **Kyrie Irving:** *ESPN est.* 18 Nov holds. He sat two of three second nights this season, so Sun 22 Nov is a pattern risk; no source has said he will sit.
- **Jaylen Brown:** day-to-day with hamstring tightness. The 18 Nov decision at ORL waits on an evaluation; *ESPN est.* 18 Nov.
- **Tyler Herro:** his 20-minute game on 15 Nov was a benching for poor play, not an injury.

**Overrides:**
- **Added:** Murphy sits 18 Nov; Bey role 34 min (to 24 Nov); Jenkins role 35 min (to 22 Nov); Suggs role 25 min (minutes limit, to 22 Nov); Quentin Grimes role 35 min (17 Nov, Reaves out).
- **Removed:** Raynaud and Claxton (expired).
- **Notes updated:** Nurkic (re-evaluated Fri 20 Nov) and Dejounte Murray (away from the team).
- **Not added:**
  - Kevin Huerter's role: no minutes given.
  - Caleb Wilson's 4 Dec floor, and Ja Morant's 28 Nov floor: both earlier than ESPN, and no source names a return.
  - Kelly Oubre Jr.'s role: barely moves his rate.
  - Mo Bamba's role: conditional on Jaxson Hayes, whose status for 18 Nov is not yet out.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Jalen Duren | return | 2026-11-23 | — | [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) | in force |
| Scotty Pippen Jr. | return | 2026-11-22 | — | [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html) | in force |
| Dejounte Murray | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) | in force |
| Maxime Raynaud | return | 2026-11-16 | — | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline) | expired: remove it |
| Nic Claxton | role | 18 | 2026-11-16 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Jalen Smith** | CHI | us | injury, rest | 43.7 | — | active |
| **Saddiq Bey** | NO | us | role, minutes | 34.6 | 35.5 | active |
| **Daniss Jenkins** | DET | us | role, minutes | 30.0 | 38.6 | active |
| **Yves Missi** | NO | us | minutes | 35.4 | — | active |
| **Scottie Barnes** | TOR | us | rest | 54.2 | — | day-to-day, ESPN est. 17 Nov |
| **Paul George** | BOS | us | rest | 40.2 | — | active |
| **Kawhi Leonard** | TOR | us | gap | 41.7 † | — | out, ESPN est. 23 Nov |
| **Jusuf Nurkic** | UTAH | free agent | injury, gap | 36.7 | — | out, ESPN est. 20 Nov |
| **Dejounte Murray** | NO | free agent | injury, minutes | 22.5 | 24.0 | out, ESPN est. 20 Nov |
| **Jalen Suggs** | ORL | free agent | role, minutes | 34.9 | — | active |
| **Mo Bamba** | UTAH | free agent | role | 30.5 | 54.1 | active |
| **Aday Mara** | OKC | free agent | role | 30.0 | 32.2 | active |
| **Tyrese Proctor** | CLE | free agent | role, minutes | 29.7 | 33.4 | active |
| **Grayson Allen** | CHA | free agent | role | 27.7 | 29.7 | active |
| **Quentin Grimes** | LAL | free agent | role | 27.3 | 24.8 | active |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 20.5 | 25.8 | day-to-day, ESPN est. 18 Nov |
| **Isaiah Stewart** | MEM | free agent | role | 20.4 | 23.1 | day-to-day, ESPN est. 18 Nov |
| **Caleb Wilson** | CHI | free agent | minutes | 29.9 | 26.1 | out, ESPN est. 13 Dec |
| **Kevin Huerter** | DET | free agent | minutes | 29.6 | 31.6 | active |
| **Collin Murray-Boyles** | TOR | free agent | minutes | 27.3 | 31.5 | active |
| **Kelly Oubre Jr.** | IND | free agent | minutes, rest | 27.3 | 26.9 | active |
| **Zach Edey** | MEM | free agent | rest | 27.4 | — | active |
| **Neemias Queta** | BOS | free agent | rest | 27.4 | — | day-to-day, ESPN est. 18 Nov |
| **Myles Turner** | MIL | free agent | rest | 26.7 | — | active |
| **Santi Aldama** | DAL | free agent | rest | 15.2 | — | day-to-day, ESPN est. 18 Nov |
| **Ja Morant** | POR | free agent | gap | 34.1 | — | out, ESPN est. 01 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 41.6 | — | day-to-day, ESPN est. 18 Nov |
| **De'Aaron Fox** | SA | Matt Wright's Foxies | injury | 30.4 | — | active |
| **Norman Powell** | CHI | Matt Wright's Foxies | minutes, rest | 37.0 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | minutes | 18.8 | 20.2 | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 42.8 | — | day-to-day, ESPN est. 18 Nov |
| **Cooper Flagg** | DAL | Matt Wright's Foxies | rest | 40.6 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 39.0 | — | active |
| **Tyler Herro** | MIL | Snow Time Lakers | rest | 35.4 | — | active |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | rest | 32.6 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 31.2 | — | day-to-day, ESPN est. 18 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 60.9 † | — | out, ESPN est. 22 Nov |
| **Bam Adebayo** | MIA | Lauri Birds | injury | 44.7 | — | day-to-day, ESPN est. 18 Nov |
| **Julius Randle** | BKN | Dr White Slong | injury | 37.8 | — | active |
| **Joel Embiid** | PHI | Dr White Slong | injury | 35.3 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - The Pistons said on 8 Nov that Duren will be re-evaluated in about two more weeks and has been cleared for on-court basketball activity. Bickerstaff: "It's a slow process … We're not going to rush him." Source: [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/). AP had "will miss at least two more weeks" and "expected to miss at least six more" games: [NBA.com/AP, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring).
  - Still out. He is listed **Out, right hamstring strain** for tonight (17 Nov) at SAS on the [NBA injury report, 17 Nov 4:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf). Detroit's report for 18 Nov at NO was not yet submitted.
  - The Pistons' Spurs-game injury write-up says he "has resumed on-court activities and could be cleared to return later this month": [Yahoo Sports, 17 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-065639408.html). I found no practice or contact update after 8 Nov.
  - Verdict: ESPN confirmed. The earliest supported return is the first game after the ~22 Nov re-evaluation, which is 24 Nov.

### Jalen Smith (CHI, PF/C, us)

- Rate **43.7** · season 36.2 (12) → 38.6 (11) · L7 50.3 (3) · L15 40.2 (6) → 46.2 (5) · L30 36.2 (12) → 38.6 (11) · projected 22.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Smith (head) exited in the fourth quarter of Monday's 126-115 loss to the Cavaliers and did not return."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (17 Nov): Smith (head) isn't listed on the injury report for Wednesday's game against Brooklyn.
- News (16 Nov): Smith (head) exited in the fourth quarter of Monday's 126-115 loss to the Cavaliers and did not return.
- **Research:**
  - He is **not on the Bulls' 18 Nov (at BKN) list** on the [NBA injury report, 17 Nov 4:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf). Chicago listed only Awaka, O. Robinson, Sellers and Patrick Williams (probable, finger). ESPN's 17 Nov note agrees ("isn't listed on the injury report").
  - After the game Smith said "I'm good", with only a bump on the back of his head. Watson caught him on the chin and he hit the back of his head when he landed. Sources: [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-jalen-smith-update-scary-fall-cavs) and [Joel Lorenzi (The Athletic) on X, 16 Nov](https://x.com/JoelXLorenzi/status/2122530901733134678). No report mentions concussion protocol. Expect him to play 18 Nov.
  - The 14 Nov absence was an **injury, not rest**. He was downgraded to out for the Wolves game with a sprained left finger, his first missed game of the season. Source: [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/jalen-smith-finger-downgraded-to-out-vs-wolves), via K.C. Johnson. He returned 16 Nov (28 min, 62 FP).
  - Verdict: ESPN confirmed (active, no injury listing, no rest signal).

### Saddiq Bey (NO, SF/PF, us)

- Rate **34.6** · role rate 35.5 · season 30.7 (15) · L7 39.8 (4) · L15 33.4 (9) · L30 30.7 (15) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 33.2 min in his starts, against 28.7 for the season
- **Role:** news on 13 Nov: "Bey will start Friday's game against the Grizzlies, Rod Walker of The Times-Picayune reports."
- **Minutes:** 36.3 min over his last 3 games against 28.7 for the season (+7.6)
- News (17 Nov): Bey finished with 23 points (8-15 FG, 5-8 3Pt, 2-2 FT), six rebounds, three assists, one steal and one block across 33 minutes in Monday's 115-94 win over Golden State.
- News (13 Nov): Bey notched 30 points (11-20 FG, 6-9 3Pt, 2-3 FT), 10 rebounds and one block across 35 minutes in Friday's 142-111 loss to the Grizzlies.
- **Research:**
  - Verdict: ESPN confirmed. Status is active, and the starting role is real and ongoing while Murphy is out.

### Daniss Jenkins (DET, PG, us)

- Rate **30.0** · role rate 38.6 · season 28.7 (12) · L7 31.5 (2) · L15 32.3 (6) · L30 28.7 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 10 before; 37.8 min in his starts, against 28.0 for the season
- **Minutes:** 37.7 min over his last 3 games against 28.0 for the season (+9.7)
- News (12 Nov): Jenkins had 21 points (6-11 FG, 3-5 3Pt, 6-6 FT), six rebounds and two steals in 42 minutes before fouling out of Thursday's 144-140 double-overtime victory over Washington.
- News (10 Nov): Jenkins notched 22 points (7-16 FG, 2-6 3Pt, 6-6 FT), six rebounds, eight assists and four steals over 36 minutes during Monday's 122-111 win over Washington.
- **Research:**
  - Verdict: ESPN confirmed. Status is active, and he is a starter for now. Risk to the role: Duren's re-evaluation about 22 Nov.

### Yves Missi (NO, C, us)

- Rate **35.4** · season 36.8 (4) → 44.0 (3) · L7 32.0 (2) · L15 32.0 (2) · L30 36.8 (4) → 44.0 (3) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:**
  - He returned 14 Nov after 11 missed games "under a minutes restriction". Rod Walker of the Times-Picayune reported the restriction; Jim Eichenhofer of Pelicans.com reported he was cleared ([RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-officially-active-539138)). The restriction "limited him to 22 minutes" that night. Neither source gave a cap or a length. RotoWire's own analysis says he "will likely take on a heavier workload once he's gotten a few more games under his belt", but that is RotoWire's view, not a team statement.
  - On 16 Nov vs GS he started again and played **23 minutes**: 6 pts, 14 reb, 3 stl, 1 blk ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/yves-missi-produces-14-rebounds-three-steals)). No report says the restriction was lifted or extended. An [SI/Pelicans Scoop piece](https://www.si.com/nba/pelicans/onsi/2-effects-yves-missi-s-return-is-already-having-on-the-pelicans-01m7nfdsnk3s) (Terry Kimble, page date not shown, after 16 Nov) confirms he is back in the starting role, with no coach comment on minutes.
  - He is **not on New Orleans' 18 Nov (vs DET) list** ([NBA injury report, 17 Nov 4:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf)). The cause of the low minutes is a ramp-up after an injury, not the rotation or blowouts. It should ease over the coming games, but no source gives a date. New Orleans has a back-to-back on 20–21 Nov, which is a mild risk for a big just back from a knee injury. No rest has been announced.
  - Verdict: nothing new found. The restriction is confirmed at about 22–23 minutes, with no lift reported.

### Scottie Barnes (TOR, SG/SF, us)

- Rate **54.2** · season 47.6 (9) → 52.0 (8) · L7 61.0 (1) · L15 50.0 (3) · L30 47.6 (9) → 52.0 (8) · projected 43.7
- ESPN: day-to-day, ESPN est. 17 Nov (Illness, updated 2026-11-17)
- **Rest:** back-to-back Tue 17–Wed 18 Nov; news on 17 Nov: "Barnes was a late addition to the injury report and could sit out the front end of this back-to-back set."
- News (17 Nov): Barnes (illness) has been downgraded to questionable for Tuesday's game against the Knicks, Blake Murphy of Sportsnet.ca reports.
- News (16 Nov): Barnes finished with 30 points (13-27 FG, 4-8 3Pt, 0-3 FT), nine rebounds, four assists, two blocks and one steal across 36 minutes during Sunday's 112-108 overtime loss to New York.
- **Research:**
  - Verdict: ESPN confirmed. He is day-to-day and questionable tonight. Nothing says he will sit Wednesday, and he has no rest pattern.

### Paul George (BOS, SF/PF, us)

- Rate **40.2** · season 41.3 (12) · L7 41.3 (3) · L15 38.3 (6) · L30 41.3 (12) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- News (11 Nov): George (illness) has been ruled out for Wednesday's game against Toronto, Taylor Snow of the Celtics' official site reports.
- **Research:**
  - Verdict: nothing new found. He is active, with no announced sit.

### Kawhi Leonard (TOR, SF/PF, us)

- Rate **41.7** (small sample) · season 40.0 (2) · L7 — · L15 — · L30 40.0 (2) · projected 45.8
- ESPN: out, ESPN est. 23 Nov (Left Knee Inflammation, updated 2026-11-11)
- **Gap:** listed out, and no news in 5 days (ESPN est. 23 Nov)
- News (11 Nov): Head coach Darko Rajakovic said Wednesday that Leonard (knee) is doing individual on-court work and is progressing well, Michael Grange of Sportsnet.ca reports.
- News (10 Nov): Leonard (knee) is continuing the reconditioning process, and another update will be provided in one week, Blake Murphy of Sportsnet.ca reports.
- **Research:**
  - He is **out tonight vs NYK**, his 12th straight game ([ClutchPoints, 17 Nov](https://clutchpoints.com/nba/nba-stories/knicks-vs-raptors-injury-report-is-kawhi-leonard-back-yet)). The NBA lists him as Out (Left Knee Injury Management) on the [17 Nov 4:15 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf). Toronto's list for 18 Nov vs WAS was not yet submitted. That game is the second night of a back-to-back.
  - On 10 Nov the Raptors said he is "continuing the reconditioning process" and that another update would come in about one week, around 17 Nov ([HEAVY via Yahoo, 10 Nov](https://sports.yahoo.com/articles/raptors-latest-kawhi-leonard-raises-203907902.html); [ESPN, 10 Nov](https://www.espn.com/nba/story/_/id/50444283/raptors-kawhi-leonard-least-1-more-week-due-knee): "at least 1 more week"). On 11 Nov Rajakovic said he was doing individual on-court work and progressing well, but was still limited to individual work ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/kawhi-leonard-knee-limited-to-individual-work), via Michael Grange). **I found no report of the promised ~17 Nov update** as of 4:30 PM ET, and no report of contact or team practice.
  - Context: on 29 Oct Chris Haynes reported he was expected to miss at least 3–4 weeks, which puts a return no earlier than about 19–26 Nov ([Basketnews, 29 Oct](https://basketnews.com/news-258440-kawhi-leonard-injury-timeline-gets-worse-worrying-update-emerges.html)). ESPN's 23 Nov falls inside that window.
  - Verdict: nothing new found. ESPN's 23 Nov estimate is consistent with every source but is not confirmed.

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 20 Nov (Right Foot Strain, updated 2026-11-06)
- **Injury:** ESPN est. 20 Nov (Out, Right Foot Strain, updated 06 Nov), but the news said on 06 Nov: "He will be re-evaluated in two weeks, the Jazz announced Friday."
- **Gap:** listed out, and no news in 5 days (ESPN est. 20 Nov)
- News (06 Nov): Nurkic (toe) has begun participating in on-court activities as he continues recovering from a right foot injury sustained during an Oct. 4 preseason game against Denver. He will be re-evaluated in two weeks, the Jazz announced Friday.
- News (03 Nov): Nurkic (foot) is out for Wednesday's game against the Pelicans.
- **Research:**
  - Jazz official update, 6 Nov 2026: he "is making progress and beginning to participate in on-court activities and will be re-evaluated in two weeks." That puts the re-evaluation on about 20 Nov. Source: [nba.com/jazz, 6 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) and [Utah Jazz On SI, 6 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-announce-new-timeline-for-jusuf-nurkic-s-return).
  - Shreyas Laddha (Salt Lake Tribune) saw him doing on-court drills before the 15 Nov game against San Antonio. He is "expected to be reevaluated this coming Friday" (20 Nov). Source: [Hoops Rumors, 15 Nov](https://hoopsrumors.com/2026/11/injury-notes-clippers-miller-barnes-nurkic-b-williams.html).
  - Still out on the 15 Nov Jazz injury report ("has yet to make his season debut"): [Utah Jazz On SI, 15 Nov](https://si.com/nba/jazz/onsi/jazz-vs-spurs-injury-report-reveals-major-problem-for-utah-rotation). There is no return timeline as of 16 Nov ([Utah Jazz On SI, 16 Nov](https://si.com/nba/jazz/onsi/utah-jazz-sign-familiar-center-as-frontcourt-injuries-pile-up)).
  - Verdict: ESPN corrected. The first possible date is 21 Nov, the day after the 20 Nov re-evaluation. The first game is 22 Nov vs DAL.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.5** · role rate 24.0 · season 30.6 (9) · L7 13.0 (1) · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 20 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 20 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - Shams Charania (ESPN) on NBA Today, 13 Nov: Murray "will NOT play another minute for the New Orleans Pelicans this season" and will sit until his trade request is met. Source: [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html). The Pelicans confirmed the request and will "evaluate potential trade opportunities." Mosley said Murray was "not in the building" on 13 Nov. Source: [NBA.com/AP, 14 Nov](https://www.nba.com/news/dejounte-murray-requests-trade-pelicans-confirm).
  - He was listed out (left ankle sprain) again for 16 Nov vs Golden State ([ClutchPoints, 16 Nov](https://clutchpoints.com/nba/new-orleans-pelicans/warriors-vs-pelicans-injury-report-dejounte-murray-listed-requesting-trade)). Marc J. Spears (ESPN, NBA Today) reported that he is not with the team, is not practicing, and that the ankle will "take some time." Spears called the trade market weak: Phoenix's interest is "mild at best," and "teams typically don't make trades in November and December." Source: [Basketnews, 17 Nov](https://basketnews.com/news-259630-dejounte-murray-gets-horrible-trade-update-with-pelicans.html).
  - The drop comes mostly from 9 Nov at Golden State: 17:33 in a 138-87 loss, trailing 72-43 at half ([CBS gametracker, 9 Nov](https://www.cbssports.com/nba/gametracker/recap/NBA_20261109_NO@GS/)). That was a blowout, not a role change. It no longer matters, because he is not playing.
  - Verdict: ESPN corrected. He is out indefinitely until traded, with no timetable. The floor is 7 days after the latest out report (16 Nov).

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **34.9** · season 24.2 (5) → 29.2 (4) · L7 21.0 (2) → 38.0 (1) · L15 21.0 (2) → 38.0 (1) · L30 24.2 (5) → 29.2 (4) · projected 29.2
- ESPN: active
- **Role:** news on 16 Nov: "Suggs will start Monday's game against the Celtics."
- **Minutes:** news on 17 Nov: "His presence is key for the Magic, meaning his playing time should continue to ramp up over the next few games."
- News (17 Nov): Suggs accumulated 12 points (5-8 FG, 2-4 3Pt), six rebounds, four assists and two blocks across 25 minutes during Monday's 115-105 win over the Celtics.
- News (16 Nov): Suggs will start Monday's game against the Celtics.
- **Research:**
  - **Ongoing.** He came off the bench in his first game back on 13 Nov and rejoined the starting five on 16 Nov at BOS, with Tristan da Silva moving to the bench ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter); [RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/jalen-suggs-news-starting-monday-539472)). He is a healthy starter, so no teammate's return ends this.
  - **Healthy.** Orlando's report for Wed 18 vs PHI lists Banchero, Isaac and Nelson as out. Suggs is not on it at all ([NBA injury report, 17 Nov 4:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf)).
  - **Still limited.** After the 16 Nov game, NBC Sports said he "will likely remain on a minutes restriction for some time". It also said that "as the minutes increase, the fantasy production should too" ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter)). Coach Sean Sweeney said the staff treated his return as "a 40-minute game instead of a 48-minute game" and that he was "excited for him to keep ramping up" ([ClutchPoints, 14 Nov](https://clutchpoints.com/nba/orlando-magic/magic-news-sean-sweeney-jalen-suggs-return-injury-bucks)).
  - Verdict: *ESPN confirmed* on status: active, starting, no injury designation for Wednesday. The rate overstates him while the minutes limit lasts, so a role row is proposed.

### Mo Bamba (UTAH, C, free agent)

- Rate **30.5** · role rate 54.1 · season 29.6 (10) · L7 34.8 (4) · L15 30.6 (7) · L30 29.6 (10)
- ESPN: active
- **Role:** started 1 of his last 2 games after 0 of 8 before; 36.0 min in his starts, against 19.7 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- News (15 Nov): Bamba will start in Sunday's game against San Antonio.
- **Research:**
  - **Ongoing while Hayes is out, and Hayes's return ends it.** RotoWire, 17 Nov: Hayes (left knee strain) is out Tue 17 at LAC, "with his next chance to suit up coming Wednesday in the second half of the Jazz's back-to-back". It adds: "Mo Bamba is likely to remain in the starting lineup" ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/jaxson-hayes-injury-remaining-out-tuesday-539488)). NBC Sports, 16 Nov: he "should get another start and is worth streaming until Utah's frontcourt gets healthier" ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jaxson-hayes-knee-remains-out-tuesday-vs-lac)).
  - Jusuf Nurkic: out, right second-toe plantar plate tear. The Jazz said on 6 Nov he will be re-evaluated in two weeks, about 20 Nov ([Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)). *ESPN est.* 20 Nov. The existing override row floors his return at 21 Nov.
  - Jaren Jackson Jr.: out, right MCL tear, "expected to be sidelined until December" ([SI, 16 Nov](https://si.com/nba/jazz/onsi/utah-jazz-sign-familiar-center-as-frontcourt-injuries-pile-up)). *ESPN est.* 14 Dec.
  - Verdict: *ESPN confirmed*: active, and starting while Hayes is out. The role can end as soon as Wed 18, and Utah's Wednesday report wasn't filed at 4:15 PM ET.

### Aday Mara (OKC, C, free agent)

- Rate **30.0** · role rate 32.2 · season 26.6 (14) · L7 32.0 (4) · L15 31.9 (8) · L30 26.6 (14)
- ESPN: active
- **Role:** started 1 of his last 2 games after 3 of 12 before; 26.2 min in his starts, against 21.6 for the season
- News (16 Nov): Mara closed with 16 points (8-11 FG), 13 rebounds and three assists across 26 minutes off the bench during Sunday's 125-103 win over Sacramento.
- News (15 Nov): Mara will come off the bench during Sunday's game against the Kings, Sean Cunningham of Fox 40 Sacramento reports.
- **Research:**
  - **The starts were situational.** He started alongside Isaiah Hartenstein on 7, 11 and 13 Nov, when OKC was short of guards. He went back to the bench on 15 Nov at SAC as Ajay Mitchell returned from a two-game ankle absence ([ClutchPoints, 16 Nov](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-aday-maras-double-double-night-mark-daigneault-eye-opening-take) on Mitchell's return; the bench move itself is from the batch's 16 Nov ESPN note citing Sean Cunningham of Fox 40). With Mitchell back, expect the bench, though a size matchup or another guard absence can bring a spot start.
  - Jaylin Williams: back spasms, out since 2 Nov. RotoWire said on 11 Nov he "remains out indefinitely", treat as week-to-week ([RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jaylin-williams-injury-remains-out-indefinitely-538633)). He was still out on 15 Nov ([Yahoo, 15 Nov](https://sports.yahoo.com/articles/full-injury-report-sundays-thunder-140133905.html)). No timetable reported; *ESPN est.* 18 Nov. OKC's Wednesday report wasn't filed at 4:15 PM ET.
  - Chet Holmgren: minor right patellar tendon tear, "return to play in 8-to-10 weeks" from 30 Oct, so late December to early January ([Thunder medical update, 30 Oct](https://www.nba.com/thunder/news/medical-update-261030)). *ESPN est.* 2 Jan 2027.
  - Verdict: *ESPN confirmed*: active. The start was a one-off tied to OKC's guard injuries, and his minutes hold either way. Three games this week (Wed, Fri, Sun).

### Tyrese Proctor (CLE, SG, free agent)

- Rate **29.7** · role rate 33.4 · season 23.2 (14) · L7 41.2 (4) · L15 28.3 (9) · L30 23.2 (14)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 12 before; 28.3 min in his starts, against 19.9 for the season
- **Role:** news on 14 Nov: "Proctor will start in Saturday's game versus the Mavericks."
- **Minutes:** 30.0 min over his last 3 games against 19.9 for the season (+10.1)
- News (17 Nov): Proctor had 17 points (6-13 FG, 2-6 3Pt, 3-5 FT), three rebounds, two assists, two steals and one block over 29 minutes during Monday's 126-115 victory over the Bulls.
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- **Research:**
  - The 14 Nov start against Dallas was a **one-off**. After a travel disruption (an FAA ground stop left the team stuck in Miami) and on a back-to-back, Cleveland ruled out eight players, including the whole starting five ([News 5 Cleveland, 14 Nov](https://www.news5cleveland.com/sports/basketball/cavaliers/cavs-rule-out-8-players-for-game-against-mavericks-including-entire-starting-lineup); [Hoops Wire via Yardbarker, 15 Nov](https://www.yardbarker.com/nba/articles/tyrese_proctor_gives_cavs_a_rotation_question_worth_answering/s1_17038_44563735)).
  - The 16 Nov start against Chicago, next to Mitchell, Harden, Watson and Allen, filled in for injured players. Evan Mobley (left great toe sprain) will be re-evaluated in 7-10 days, so he misses at least three more games (ESPN est. 29 Nov). Jaylon Tyson (right ankle) is day-to-day, with no timetable reported (ESPN est. 18 Nov). Cavaliers Nation says the start "does not establish a permanent starting role" ([Cavaliers Nation, 16 Nov](https://cavaliersnation.com/2026/11/16/evan-mobley-faces-longer-absence-as-cavs-announce-reevaluation-plan/); [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-tyrese-proctor-remains-productive-monday/)).
  - He has played 23+ minutes in 6 straight games (26.5 min/g, per CBS, 17 Nov), and he played 27 minutes on 13 Nov even with Mitchell and Harden available. Merrill has been out since 6 Nov, and Proctor has taken the bench wing minutes. Atkinson called him "a changed man" ([Cavaliers Nation, 15 Nov](https://cavaliersnation.com/2026/11/15/kenny-atkinson-calls-tyrese-proctor-a-changed-man-after-cavs-breakout/)).
  - Verdict: ESPN confirmed (active). The start is a stopgap for injuries, and the minutes bump should hold until Merrill, Tyson or Mobley returns.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **27.7** · role rate 29.7 · season 26.8 (13) · L7 27.5 (2) · L15 28.2 (6) · L30 26.8 (13) · projected 26.6
- ESPN: active
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (15 Nov): Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports.
- News (13 Nov): Allen logged 14 points (5-11 FG, 4-8 3Pt), four rebounds, six assists and one steal over 34 minutes during Thursday's 101-96 loss to Phoenix.
- **Research:**
  - Brandon Miller (right hip/groin strain) was cleared and returned on 15 Nov after missing two games, and Allen went back to the bench after three straight starts. RotoWire: he "should remain a key part of the rotation." He played 25 minutes (26 FP) off the bench in the 113-105 loss ([RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/grayson-allen-news-not-starting-sunday-539277); [Heavy, 15 Nov](https://heavy.com/sports/nba/charlotte-hornets/hornets-brandon-miller-cleared-return-clippers/)). He took a bloodied nose in a collision in the third quarter ([AOL, 16 Nov](https://www.aol.com/articles/offensive-foul-announcers-fume-hornets-113000000.html)), but he is not on the injury report for 17 Nov at the Lakers. Miller is not listed either ([iHeart/Fox Sports 104.9, 17 Nov](https://1049foxsports.iheart.com/content/2026-11-17-hornets-vs-lakers-injury-report-nov-17/)).
  - The bench role is **ongoing** while Miller stays healthy. Kon Knueppel (left hamstring strain) will be re-evaluated four weeks from about 8 Nov (ESPN est. 12 Dec). Dennis Schroder (left hamstring strain) will be re-evaluated two weeks from about 8 Nov (ESPN est. 25 Nov) ([Fadeaway World via Yardbarker, 8 Nov](https://www.yardbarker.com/nba/articles/hornets_injury_update_latest_on_brandon_miller_expected_timelines_for_kon_knueppel_dennis_schroder/s1_16751_44534895)). Both are out again on 17 Nov. Allen should hold a mid-20s bench role until Schroder is back. Schroder's return would cut his minutes further, and Knueppel's would cut them more. No source gives a minutes figure, so no role row.
  - Verdict: nothing new found. He is a bench sixth man at about 25 minutes now that Miller is back. That rests on one game and is a small sample.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **27.3** · role rate 24.8 · season 18.8 (12) · L7 42.0 (1) · L15 20.0 (5) · L30 18.8 (12) · projected 28.1
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 35.7 min in his starts, against 27.0 for the season
- **Role:** news on 15 Nov: "Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports."
- News (15 Nov): Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports.
- News (14 Nov): Grimes (finger) is available to play in Sunday's game against the Suns.
- **Research:**
  - This is a fill-in for Austin Reaves (left heel contusion / bone bruise). Reaves is OUT again tonight (17 Nov vs CHA) per the [official 4 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_00PM.pdf). NBC Sports (16 Nov): "Until he's back, Quentin Grimes will continue to start", after 22 points and five threes in 37 minutes ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/austin-reaves-heel-remains-out-vs-charlotte)). The note adds "there isn't a clear timeline" for Reaves.
  - Reaves' return ends the role, and it could be close. Lakers Nation (16 Nov) says Reaves could return Wed 18 Nov vs UTA, the second night of a back-to-back. Redick described the bruise as improving day by day, with X-rays negative and Reaves day-to-day ([Lakers Nation, 16 Nov](https://lakersnation.com/lakers-injury-report-walker-kessler-austin-reaves-out-vs-hornets/)). His earlier starts were also fill-ins. He started 8 Nov at DET, then was expected "to head back to the bench" once Reaves was available (ESPN news note, 10 Nov, in the batch). Expect about 35 minutes while Reaves sits, then a bench role in the mid-20s (27.0 season).
  - Verdict: ESPN confirmed (active and available). The starting role is tied to Reaves and is confirmed only through tonight.

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **20.5** · role rate 25.8 · season 19.2 (8) · L7 20.3 (3) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: day-to-day, ESPN est. 18 Nov (Right Ankle, updated 2026-11-17)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Role:** news on 13 Nov: "Tyson will start Friday's game against Miami, Serena Winters of FanDuel Sports Network Ohio reports."
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (16 Nov): Tyson (ankle) has been ruled out for Monday's game against Chicago.
- News (16 Nov): Tyson (ankle) has been downgraded to doubtful for Monday's game against the Bulls.
- **Research:**
  - Out Mon 16 Nov vs CHI for "right ankle injury management" after a downgrade to doubtful. He had played 64 minutes over the Fri-Sat back-to-back ([CBS Sports / RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-officially-out-monday/); [official 16 Nov 8 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_08_00PM.pdf): Out, right ankle injury management).
  - No status for Wed 18 Nov vs MEM yet. The Cavaliers' 18 Nov report was "NOT YET SUBMITTED" at 4 PM ET on 17 Nov ([official report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_00PM.pdf)). The AP preview (17 Nov) lists him as out, but that looks carried over from Monday's report ([ABC News / AP, 17 Nov](https://abcnews.com/Sports/wireStory/memphis-faces-cleveland-3-game-win-streak-138201498)). The Beacon Journal's post-game piece gives no Wednesday status ([Akron Beacon Journal via Yahoo, 17 Nov](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html)). ESPN's 18 Nov estimate is neither confirmed nor contradicted. Re-check Wednesday's report.
  - Both starts filled in for Evan Mobley (left great toe sprain). RotoWire (13 Nov): "With Evan Mobley (toe) sidelined, Tyson will join the first unit" (batch news). On 16 Nov the Cavs said Mobley will have "treatment and rehabilitation over the next seven to 10 days before being reevaluated" (about 23-26 Nov) ([Akron Beacon Journal via Yahoo, 17 Nov](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html); [Yahoo, 16 Nov](https://sports.yahoo.com/articles/cavaliers-star-forward-7-10-221034351.html)). The opening stays open until Mobley returns. No source says Tyson keeps the starting job, though. Tyrese Proctor started Monday in his place, and the Beacon Journal calls Tyson one of the backups "part of Atkinson's normal rotation".
  - Verdict: Nothing new found. ESPN's day-to-day / 18 Nov estimate stands pending Wednesday's report. The role is not reported as ongoing.

### Isaiah Stewart (MEM, PF/C, free agent)

- Rate **20.4** · role rate 23.1 · season 21.6 (10) · L7 18.7 (3) · L15 19.8 (5) · L30 21.6 (10) · projected 25.3
- ESPN: day-to-day, ESPN est. 18 Nov (Illness, updated 2026-11-17)
- **Role:** started 2 of his last 2 games after 1 of 8 before; 19.0 min in his starts, against 18.1 for the season
- **Role:** news on 13 Nov: "Stewart will start Friday's game against the Pelicans."
- News (16 Nov): Stewart is out for Monday's game against the Wizards due to an illness.
- News (15 Nov): Stewart is questionable for Monday's game against the Wizards due to an illness.
- **Research:**
  - Ruled out Mon 16 Nov at WAS with an illness, after starting as questionable ([Roundtable Sports via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-rule-isaiah-stewart-vs-181202853.html); [official 16 Nov 8 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_08_00PM.pdf)). RotoWire called him "day-to-day ahead of Wednesday's meeting in Cleveland" ([CBS Sports / RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-isaiah-stewart-out-sick-monday/)).
  - Field Level Media (17 Nov, 10:51 AM): "backup center Isaiah 'Beef' Stewart (illness) [is] questionable for Wednesday's game" at CLE ([Field Level Media, 17 Nov](https://fieldlevelmedia.com/nba/travel-proven-grizzlies-chase-franchise-road-mark-at-cleveland/)). The AP preview lists him as out, probably carried over from Monday ([ABC News / AP, 17 Nov](https://abcnews.com/Sports/wireStory/memphis-faces-cleveland-3-game-win-streak-138201498)). The official MEM report for 18 Nov was not yet submitted at 4 PM ET. ESPN's 18 Nov estimate matches "questionable".
  - One-off. Both starts (13 Nov vs NOP, 14 Nov vs BKN) came while Zach Edey sat both halves of a back-to-back for left ankle injury management (ESPN news note, 14 Nov, in the batch; [Roundtable Sports via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-rule-isaiah-stewart-vs-181202853.html)). Edey returned 16 Nov at WAS with 23 points and 10 rebounds in 21 minutes ([FantasyPros, 16-17 Nov](https://www.fantasypros.com/nba/news/620738/zach-edey-logs-double-double-win-monday.php); [Memphis Flyer](https://www.memphisflyer.com/grizzlies-beat-wizards-stay-perfect-on-the-road/)). That ended it. RotoWire (14 Nov) expects Stewart "back on the bench, flirting with minutes in the low-20s" once Edey plays (batch news). He even averaged only 19.0 minutes in his starts.
  - Verdict: ESPN confirmed (day-to-day, questionable 18 Nov). The start was a one-off for Edey's rest.

### Caleb Wilson (CHI, SF, free agent)

- Rate **29.9** · role rate 26.1 · season 34.9 (10) · L7 26.0 (1) · L15 27.2 (4) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - The drop is the injury plus one benching. He left the 11 Nov game vs SAS in the third quarter after 15 minutes with the right hand fracture ([Chicago Sun-Times, 11 Nov](https://chicago.suntimes.com/bulls/2026/11/11/bulls-rookie-caleb-wilson-answers-bell-sore-hip)). His 22 minutes in the 4 Nov loss to New York came after coach Tiago Splitter benched him, citing body language and resiliency (same Sun-Times piece). It does not matter now that he is out for weeks.
  - The Bulls' official update (12 Nov, 3:57 PM CST): Wilson "underwent successful surgery today and will be re-evaluated in three weeks", which is about 3 Dec ([Bulls / NBA.com, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). The official 17 Nov report lists him OUT with a right metacarpal fracture ([official report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_00PM.pdf)).
  - Shams Charania (ESPN, 12 Nov) reports 4-6 weeks, which works out to about 10-24 Dec ([CBS Sports, 12 Nov](https://www.cbssports.com/nba/news/caleb-wilson-injury-update-bulls-rookie-of-the-year/); [NBA.com, 13 Nov](https://www.nba.com/news/bulls-caleb-wilson-hand-injury)). Bulls On SI puts the absence at 13 to 20 games, with a return shortly after Christmas at the long end ([SI, 12 Nov](https://www.si.com/nba/bulls/onsi/caleb-wilson-to-undergo-hand-surgery-when-will-the-bulls-get-him-back-12)). Nothing newer has been reported since 13 Nov.
  - Verdict: ESPN corrected (floor only). Per the brief's rule, the team's re-evaluation date (3 Dec) moves the earliest possible return ahead of ESPN's 13 Dec. ESPN's date remains the more likely return, within Charania's 4-6 weeks.

### Kevin Huerter (DET, SG/SF, free agent)

- Rate **29.6** · role rate 31.6 · season 24.2 (12) · L7 33.0 (2) · L15 33.5 (6) · L30 24.2 (12) · projected 22.9
- ESPN: active
- **Minutes:** 31.7 min over his last 3 games against 24.4 for the season (+7.2)
- News (14 Nov): Huerter posted 20 points (9-15 FG, 2-6 3Pt), four rebounds, seven assists, a steal and three blocks across 38 minutes in Saturday's 137-117 loss to Miami.
- News (09 Nov): Huerter recorded 24 points (9-14 FG, 4-8 3Pt, 2-3 FT), five rebounds, five assists, five blocks and two steals in 35 minutes during Sunday's 121-116 loss to the Lakers.
- **Research:**
  - Detroit's wing depth is gutted. The official 17 Nov report for DET@SAS lists five Pistons out ([official report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_00PM.pdf)):
  - Duncan Robinson, left quadriceps strain. No timetable beyond re-evaluation; the Pistons plan to "reevaluate Robinson in one week" ([Hoops Rumors, 17 Nov](https://www.hoopsrumors.com/2026/11/pistons-duncan-robinson-quad-out-at-least-one-week.html)), about 24 Nov, so he misses SAS 17 Nov, NOP 18 Nov, TOR 20 Nov and ATL 22 Nov.
  - Ron Holland II, left knee contusion / bone bruise, day-to-day ([Heavy, 17 Nov](https://heavy.com/sports/nba/detroit-pistons/pistons-duncan-robinson-ron-holland-injuries/)).
  - Verdict: ESPN confirmed (active). The minutes bump is real and should last while Robinson is out (re-evaluation about 24 Nov).

### Collin Murray-Boyles (TOR, PF, free agent)

- Rate **27.3** · role rate 31.5 · season 25.2 (12) · L7 27.3 (3) · L15 30.5 (6) · L30 25.2 (12) · projected 24.8
- ESPN: active
- **Minutes:** 30.7 min over his last 3 games against 24.3 for the season (+6.3)
- News (12 Nov): Murray-Boyles ended with 14 points (5-9 FG, 1-1 3Pt, 3-4 FT), four assists, five blocks and one steal over 32 minutes during Thursday's 123-112 loss to the 76ers.
- News (11 Nov): Murray-Boyles posted five points (1-9 FG, 1-5 3Pt, 2-4 FT), four rebounds, three assists and one block over 20 minutes during the Raptors' 98-93 loss to the Celtics on Wednesday.
- **Research:**
  - **Barnes's absence, now over.** Barnes (groin) missed four games, and the 32 minutes on 12 Nov came while he was out. Barnes came back on 15 Nov. Before that, RotoWire said Murray-Boyles "will likely be a fixture on the second unit when Barnes and Jakob Poeltl are both healthy" ([CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-strong-showing-at-both-ends-of-court/)).
  - **Overtime and a matchup start.** The 40 minutes on 15 Nov came in an overtime game ([CBS box score, 15 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261115_NY@TOR/)). Murray-Boyles also started at center over Poeltl that night: "Quickley, Walter, Barrett, Barnes, and Murray-Boyles." The writer expects him to keep that spot, with Poeltl moving to the bench ([Raptors Republic via Yardbarker, 15 Nov](https://www.yardbarker.com/nba/articles/raptors_barnes_set_to_return_against_the_new_york_knicks/s1_17733_44566341)). The recap says the Raptors "opted for a different front court to matchup with the Knicks," meaning against Karl-Anthony Towns ([Raptors Republic, 15 Nov](https://raptorsrepublic.com/2026/11/15/raptors-fall-in-overtime-to-knicks-in-scottie-barnes-return/)). That makes the start a matchup choice.
  - **Tonight (Tue 17 Nov vs NYK, same opponent).** He is again the projected starting center ([Raptors Republic, 17 Nov](https://raptorsrepublic.com/2026/11/17/gameday-knicks-raptors-november-17th/)). Scottie Barnes (illness) is questionable: he was a late addition to the report and "could sit out the front end of this back-to-back set" ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/scottie-barnes-injury-late-addition-to-injury-report-539587)). Barnes: questionable tonight, no timetable reported; *ESPN est.* 17 Nov.
  - Verdict: *ESPN confirmed* (active). The minutes bump is mostly temporary: Barnes is back, the 40 came in overtime, and the start was matchup-driven. Leonard's open-ended absence supports the higher floor.

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **27.3** · role rate 26.9 · season 21.3 (12) · L7 34.0 (3) · L15 26.0 (5) · L30 21.3 (12) · projected 23.2
- ESPN: active
- **Minutes:** 31.0 min over his last 3 games against 24.6 for the season (+6.4)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 13 Nov: "Oubre's fantasy arrow is beginning to point up, as he's now drawn back-to-back starts for the Pacers while pushing previous starter Braden Smith from the rotation entirely."
- News (15 Nov): Oubre notched 16 points (6-11 FG, 2-5 3Pt, 2-2 FT), four rebounds, two assists, one block and one steal over 29 minutes during Sunday's 131-124 loss to Philadelphia.
- News (13 Nov): Oubre ended Friday's 106-104 win over the Knicks with 16 points (5-13 FG, 1-4 3Pt, 5-6 FT), five rebounds, one block and two steals in 30 minutes.
- **Research:**
  - "Oubre will move into the starting lineup as the Pacers continue without the injured Tyrese Haliburton (hamstring)." Rookie Braden Smith, who had started the previous four games, went to the bench ([NBC Sports/Rotoworld, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/ind-starts-nembhard-oubre-nesmith-siakam-zubac)). RotoWire added that he has pushed Smith "from the rotation entirely" ([CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-kelly-oubre-another-positive-showing/)).
  - He is a probable starter for Wed 18 Nov vs HOU, alongside Quenton Jackson, Nesmith, Siakam and Zubac. The preview calls him "Indiana's second-best scorer over the last four games" ([NBA.com Pacers preview, 17 Nov](https://www.nba.com/pacers/news/preview-pacers-rockets-261118)). Andrew Nembhard (hip) is questionable: no timetable reported; *ESPN est.* 18 Nov.
  - **What ends it: Haliburton's return.** Carlisle said on 17 Nov that Haliburton is "getting there," but "there's no definite timeline on him." He did not rule out a November return, but Haliburton could miss HOU (18 Nov), at CLE (20 Nov) and at NY (22 Nov) ([CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-firm-timetable-for-return/); [Yardbarker, 17 Nov](https://www.yardbarker.com/nba/articles/pacers_announce_tyrese_haliburton_injury_update/s1_17355_44575841)). On 11 Nov, Carlisle said the next update would come in about 10 days, so around 20 to 21 Nov. Haliburton: no timetable reported; *ESPN est.* 28 Nov.
  - Verdict: *ESPN confirmed* (active, no rest news). The minutes increase is real and should last while Haliburton is out, at least through 20 Nov at CLE.

### Zach Edey (MEM, C, free agent)

- Rate **27.4** · season 25.1 (11) · L7 28.0 (2) · L15 26.7 (6) · L30 25.1 (11) · projected 33.2
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; news on 14 Nov: "Edey sat out Memphis' game Friday due to an ankle injury, and he is now at risk of missing both legs of this back-to-back set."; sat the first night of the 25–26 Oct back-to-back, playing the games either side
- News (17 Nov): Edey provided 23 points (10-15 FG, 3-3 FT), 10 rebounds, one assist and one block across 21 minutes during Monday's 136-120 victory over the Wizards.
- News (16 Nov): Edey (ankle) is available for Monday's game against the Wizards.
- **Research:**
  - **No word yet on this back-to-back.** He came back on 16 Nov at WSH after missing 13 and 14 Nov with the left ankle. The official 16 Nov report listed him "Available" for left ankle injury management ([NBA injury report, 16 Nov 7:00 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_07_00PM.pdf); [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/zach-edey-ankle-upgraded-to-available-monday)). Memphis hadn't filed Wednesday's report at 4:15 PM ET, and I found no team or beat statement about 18–19 Nov.
  - 25–26 Oct: he sat the first night at SAC for "left ankle injury management" and played the second at UTA ([NBC Sports, 24 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/zach-edey-ankle-ruled-out-vs-sacramento)).
  - 13–14 Nov: he missed both, the first for injury management and the second after a downgrade from questionable ([Yahoo, 14 Nov](https://sports.yahoo.com/articles/grizzlies-zach-edey-jerami-grant-010359185.html)).
  - Verdict: *nothing new found*. ESPN lists him as active, which is right for Wednesday as far as anyone knows. The risk to watch is the back-to-back.

### Neemias Queta (BOS, C, free agent)

- Rate **27.4** · season 25.6 (13) · L7 27.7 (3) · L15 27.9 (7) · L30 25.6 (13) · projected 27.2
- ESPN: day-to-day, ESPN est. 18 Nov (Rest, updated 2026-11-17)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 16 Nov: "Queta (rest) won't play in Monday's game against the Magic, Taylor Snow of the Celtics' official site reports."
- News (16 Nov): Queta (rest) won't play in Monday's game against the Magic, Taylor Snow of the Celtics' official site reports.
- News (16 Nov): Queta (rest) is questionable for Monday's game against the Magic.
- **Research:**
  - **The rest was a one-night, back-to-back decision.** He sat the second night of the 15–16 Nov set, and RotoWire, citing Taylor Snow of the Celtics' official site, said "he should be good to go for Wednesday's showdown in Denver" ([RotoWire via CBS Sports, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-neemias-queta-sitting-out-monday-539449/)). Boston hadn't filed Wednesday's report at 4:15 PM ET ([NBA injury report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf)).
  - The AP preview on Fox Sports (17 Nov, 2:03 AM ET) still lists him "out (rest)" for Denver ([Fox Sports](https://www.foxsports.com/articles/nba/boston-takes-road-win-streak-into-matchup-with-denver)). That looks carried over from Monday's report, before Boston filed for Wednesday. Treat the beat note as the stronger source and check the filed report.
  - **Rest pattern:** he has played both nights of 3 of Boston's 4 back-to-backs (26–27 Oct, 1–2 Nov, 10–11 Nov) and sat 1 (16 Nov). The Celtics "have managed their centers on back-to-backs before this season": Mitchell Robinson sat the 1 Nov game, with Queta starting ([Yahoo, 16 Nov](https://sports.yahoo.com/articles/celtics-starter-injury-report-ahead-193514066.html)). Nothing has been said about Sat 21–Sun 22. Both games are late West Coast tips, so there is some risk he sits one night, but nothing supports a `sit` row.
  - Verdict: *ESPN confirmed*: the 18 Nov return estimate holds. The Sat–Sun back-to-back plan is not announced.

### Myles Turner (MIL, C, free agent)

- Rate **26.7** · season 26.5 (13) · L7 25.0 (3) · L15 28.6 (7) · L30 26.5 (13) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (14 Nov): Turner recorded 14 points (5-9 FG, 4-7 3Pt), 11 rebounds, three assists and two steals across 31 minutes during Friday's 107-99 loss to the Magic.
- News (12 Nov): Turner (rest) isn't listed on the injury report ahead of Friday's game against Orlando.
- **Research:**
  - **Last back-to-back.** He was ruled out for the second night (11 Nov vs LAL) "due to rest" ([CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-myles-turner-resting-wednesday/)). Taylor Jenkins: "The Myles Turner rest decision is to give him a mental and physical break on the second night on a back-to-back" ([SI All Bucks, 14 Nov](https://www.si.com/nba/bucks/onsi/3-losers-1-surprising-winner-as-bucks-fall-to-the-magic-01m7bp7yx577)). The rest came after he shot 2-for-22 over three games. SI called it "an odd reason" only 11 games in, and the team gave no wider policy ([SI All Bucks, 11 Nov](https://www.si.com/nba/bucks/onsi/kel-el-ware-must-capitalize-on-a-big-opportunity-against-the-los-angeles-lakers-01m769zw3txe)). RotoWire called it "his first breather of the season."
  - Verdict: *nothing new found*. There is no announced rest for 19 Nov. He is a coin-flip risk for the second night, but without a team or beat statement no `sit` row is supported. Re-check the Bucks' report on Wednesday afternoon.

### Santi Aldama (DAL, SF/PF, free agent)

- Rate **15.2** · season 14.8 (5) · L7 12.5 (2) · L15 14.8 (5) · L30 14.8 (5) · projected 25.0
- ESPN: day-to-day, ESPN est. 18 Nov (Left Ankle Sprain, updated 2026-11-17)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 15 Nov: "Aldama will miss Sunday's game with an ankle injury, which is not surprising given it is the second half of a back-to-back set."
- News (17 Nov): Aldama (ankle) was a full participant in Tuesday's practice, Mike Curtis of The Dallas Morning News reports.
- News (15 Nov): Aldama (ankle) is out for Sunday's game against the Celtics.
- **Research:**
  - He was a full participant in Tuesday's practice ([NBC Sports/Rotoworld citing Mike Curtis, DMN, 17 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/max-christie-santi-aldama-get-in-full-practice)). Dusty May said he was "full go at practice Tuesday." Dallas had not yet released its injury report for Wed 18 Nov vs GSW ([Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)).
  - The 15 Nov absence (at BOS, the second night of a back-to-back) was the ankle sprain. The NBA's 4:30 PM CT report moved him from questionable to out ([Dallas Sports Journal, 15 Nov](https://dallassportsjournal.com/daniel-gafford-available-santi-aldama-out-mavericks-celtics/)). That was not a planned rest.
  - He was cleared for his first back-to-back after the knee surgery and played both nights of 8 to 9 Nov, BKN then IND (15 and 19 minutes) ([Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)). The team has said nothing about sitting him on 21 or 22 Nov.
  - Verdict: *ESPN confirmed*. The 18 Nov estimate fits the full practice, and there is no rest pattern or announcement.

### Ja Morant (POR, PG, free agent)

- Rate **34.1** · season 33.8 (4) · L7 — · L15 — · L30 33.8 (4) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:**
  - **Status now.** He is still listed "Out (Hamstring)" on Portland's report for Tue 17 Nov at MIN ([KFAN, 17 Nov](https://kfan.iheart.com/content/2026-11-17-trail-blazers-vs-timberwolves-injury-report-nov-17/)). The only new item is Morant himself telling Deni Avdija "I'm on my way back" after Monday's game. That is not a timeline ([ClutchPoints, 17 Nov](https://clutchpoints.com/nba/nba-stories/blazers-news-ja-morant-all-smiles-deni-avdija-injury-return-tease-timberwolves-beatdown)).
  - **Team timeline.** Portland announced on 30 Oct a Grade 2 left hamstring strain and said he "will be re-evaluated in four weeks," which is about 27 Nov ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). On 7 Nov, Nori said he "may not be out for as long as we thought" after a positive opinion from a doctor in Los Angeles, but declined to change the timetable ([NBC Sports/Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/nori-morant-could-be-back-sooner-than-expected)). As of 16 Nov, the four-week re-evaluation was still set for late November with the official timeline unchanged ([FantasyAlarm, 16 Nov](https://fantasyalarm.com/articles/nba/fantasy-basketball-injury-report/nba-injury-report-week-5-2026-fantasy-basketball/198796)). No source reports him practicing.
  - Verdict: *ESPN confirmed* in substance. He is still out, and nothing contradicts the 1 Dec estimate. The re-evaluation rule (day after the re-evaluation date) gives a slightly earlier floor, one game sooner, so the row below is proposed as a floor.

## Opponents: this week and next

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **41.6** · season 40.8 (14) · L7 39.2 (4) · L15 44.6 (8) · L30 40.8 (14) · projected 38.6
- ESPN: day-to-day, ESPN est. 18 Nov (Left Hamstring, updated 2026-11-17)
- **Injury:** ESPN est. 18 Nov (Day-To-Day, Left Hamstring, updated 17 Nov), but the news said on 16 Nov: "Brown (hamstring/head) will undergo further evaluation Tuesday and could receive an MRI, Kris Rhim of ESPN reports."
- News (16 Nov): Brown (hamstring/head) will undergo further evaluation Tuesday and could receive an MRI, Kris Rhim of ESPN reports.
- News (16 Nov): Brown amassed 31 points (9-19 FG, 3-8 3Pt, 10-13 FT), 13 rebounds, four assists, one steal and one block in 33 minutes during Monday's 135-123 win over Brooklyn.
- **Research:**
  - He left with 1:44 to go in the 16 Nov win at Brooklyn (31 pts, 13 reb). Nurse called it left hamstring "tightness" and a precaution. Brown said, "I don't think it's concerning," and that he has had "a lot of hamstring stuff" before. He will be checked again Tuesday, an MRI is "a possibility," and his status for Wednesday at Orlando is "to be determined" ([Philadelphia Inquirer, Gina Mizell, 17 Nov](https://www.inquirer.com/sixers/jaylen-brown-injury-update-nets-score-highlights-20261117.html); [NBA.com/AP, 17 Nov](https://www.nba.com/news/sixers-jaylen-brown-says-head-injury-is-ok-will-find-out-more-about-hamstring)). He says his head is fine.
  - As of about 4:30 PM ET Tuesday, no result from the evaluation or MRI has been reported. RotoWire's latest (9:53 AM, 17 Nov) still reads "will undergo further evaluation Tuesday" ([RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/jaylen-brown-injury-set-for-further-evaluation-tuesday-539522)). Previews list him as a game-time decision for 18 Nov ([Sports Mole, 17 Nov](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/philadelphia-76ers-vs-orlando-magic-player-props-injury-report-and-prediction--nba_609259.html)). One fan-site writer called it "extremely doubtful" he plays Wednesday, but that was opinion, not reporting, and I could not open the page to link it. The official injury report for 18 Nov (due about 5 PM ET) had not been found.
  - Verdict: nothing new found. ESPN's day-to-day status and 18 Nov estimate match the reporting, and the outcome hangs on Tuesday's evaluation. Re-check the 76ers' 17 Nov injury report and any MRI news before Wednesday's lineup lock.

### De'Aaron Fox (SA, PG/SG, Matt Wright's Foxies)

- Rate **30.4** · season 32.7 (13) · L7 29.5 (2) · L15 27.0 (7) · L30 32.7 (13) · projected 38.2
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 15 Nov: "Fox (hip) has been ruled out for Sunday's game against the Jazz."
- News (16 Nov): Fox (hip) is not listed on the injury report for Tuesday's game against the Pistons.
- News (15 Nov): Fox (hip) has been ruled out for Sunday's game against the Jazz.
- **Research:**
  - Fox is **not on the official NBA injury report** for tonight, Tue 17 Nov vs DET. The Spurs list only Brown, Gillespie, Harris and Quaintance ([NBA injury report, 17 Nov 4:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_30PM.pdf)).
  - Rotoworld, citing the NBA injury report, says Fox is "not on the injury report" for Tuesday after sitting Sunday's win at Utah ([NBC Sports/Rotoworld, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/deaaron-fox-hip-removed-from-injury-report)).
  - BasketNews says he had played through the tightness in recent games, so Sunday's absence came during a weekend break, and that he is cleared for Detroit ([BasketNews, 16 Nov](https://basketnews.com/news-259619-spurs-make-critical-deaaron-fox-injury-status-update-vs-pistons.html)).
  - Verdict: *ESPN confirmed.* ESPN's "active" is right, and nothing points to more missed time. The hip has now shown up in three straight reports, so watch tonight's minutes.

### Norman Powell (CHI, SG/SF, Matt Wright's Foxies)

- Rate **37.0** · season 30.5 (11) → 33.1 (10) · L7 41.7 (3) · L15 30.4 (5) → 37.0 (4) · L30 30.5 (11) → 33.1 (10) · projected 36.0
- ESPN: active
- **Minutes:** news on 13 Nov: "Powell led all scorers with 33 points in his return to action, showing no signs of limitations after being cleared to play without a minutes restriction."
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 14 Nov: "Powell was questionable to play Saturday due to lower-back injury management, but he'll fight through it and suit up for the second leg of Chicago's back-to-back set."
- News (16 Nov): Powell tallied 27 points (10-18 FG, 0-6 3Pt, 7-11 FT), two rebounds, six assists and one steal across 33 minutes during Monday's 126-115 loss to Cleveland.
- News (16 Nov): Powell (undisclosed) has been cleared to return to Monday's game against the Cavaliers, K.C. Johnson of Chicago Sports Network reports.
- **Research:**
  - reported: 4–6 weeks after hand surgery ([Chicago Sun-Times, 12 Nov](https://chicago.suntimes.com/bulls/2026/11/12/bulls-losing-demoralizing-understanding-process))
  - Coach Tiago Splitter said Powell "will not have a minutes limit" on his return from a two-game absence (back spasms). Rotoworld adds that Chicago needs his scoring while Wilson is out ([NBC Sports/Rotoworld, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/norman-powell-has-33-points-in-win-over-hawks-friday)).
  - Monday's scare was minor. He left in the 4th quarter with an undisclosed lower-body issue and was cleared back in at 8:44 (K.C. Johnson via [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-news-cleared-to-return-539493)).
  - Verdict: *ESPN confirmed.* He is active, has no minutes limit and is off the 18 Nov report. Mon 23 Nov carries some back-management risk, but nothing has been announced.

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **18.8** · role rate 20.2 · season 28.7 (11) · L7 11.0 (1) · L15 12.0 (4) · L30 28.7 (11) · projected 37.4
- ESPN: active
- **Minutes:** 21.3 min over his last 3 games against 30.4 for the season (−9.0)
- News (16 Nov): Miller finished Sunday's 113-105 loss to the Clippers with five points (1-10 FG, 1-6 3Pt, 2-3 FT), four assists, two rebounds and one steal over 24 minutes.
- News (14 Nov): Miller (groin) is not listed on the injury report for Sunday's game against the Clippers.
- **Research:**
  - 6 Nov: 14 minutes. He left in the 2nd quarter with right groin soreness and did not return ([ClutchPoints, 6 Nov](https://clutchpoints.com/nba/charlotte-hornets/hornets-news-brandon-miller-exits-celtics-clash-groin-soreness)).
  - He missed 9 Nov and 12 Nov. Coach Charles Lee called it day-to-day and said he "isn't expected to be out long" ([Yahoo/All Hornets, 12 Nov](https://sports.yahoo.com/articles/hornets-injury-diabat-trending-miller-130048683.html)).
  - No minutes restriction was reported for the return. RotoWire's 16 Nov recap mentions none ([CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-struggles-in-return/)). Rotoworld's 14 Nov note had him back "following a two-game absence" ([NBC Sports/Rotoworld, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/brandon-miller-hip-off-injury-report-vs-lac)). That note calls the injury a hip strain, while every other source says groin.
  - Verdict: *ESPN confirmed.* He is active with no reported restriction. The low rate (18.8) leans on one rusty return game and an injury-shortened one, and probably understates him next week. Tonight's minutes at LAL are the test.

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **42.8** · season 41.5 (11) · L7 45.5 (2) · L15 40.8 (6) · L30 41.5 (11) · projected 44.2
- ESPN: day-to-day, ESPN est. 18 Nov (Left Knee, updated 2026-11-16)
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 15 Nov: "He will, however, sit out the second leg of the back-to-back for Dallas, which will likely send Cooper Flagg's usage to the moon."; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (15 Nov): Irving (knee) has been ruled out for Sunday's game against the Celtics.
- News (15 Nov): Irving (knee) is questionable to play in Sunday's game against the Celtics.
- **Research:**
  - Verdict: ESPN confirmed for the 18 Nov return estimate. Nothing new on 21–22 Nov. The risk that he sits Sun 22 Nov is high on pattern alone (2 of 3 second nights), but no team or beat source has said so, so no `sit` row.

### Cooper Flagg (DAL, SF/PF, Matt Wright's Foxies)

- Rate **40.6** · season 49.2 (13) · L7 29.3 (3) · L15 43.5 (8) · L30 49.2 (13) · projected 45.4
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (16 Nov): Flagg contributed 17 points (5-15 FG, 2-6 3Pt, 5-5 FT), three rebounds, four assists, one block and one steal in 27 minutes during Sunday's 131-94 loss to the Celtics.
- News (13 Nov): Flagg chipped in 12 points (5-12 FG, 1-2 3Pt, 1-2 FT), seven rebounds, three assists and two steals over 27 minutes during Thursday's 133-94 loss to the Timberwolves.
- **Research:**
  - So two of the three were blowouts with cut minutes. He also played the Boston game sick. He said he played through a mild illness and sounded congested afterwards ([Dallas Morning News via Yahoo, 16 Nov](https://sports.yahoo.com/articles/cooper-flagg-looks-mavericks-veterans-211854890.html)). On Tue 17 Nov he told Dusty May it was the first morning he had woken up feeling good; May said "he was good today" ([Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)).
  - **The 24 Oct absence was an injury, not rest.** An MRI showed a mild left shoulder sprain from the 23 Oct game at Indiana, and he was "listed as out … and re-evaluated next week" ([Dallas News, 24 Oct](https://www.dallasnews.com/sports/mavericks/article/cooper-flagg-injury-update-mavericks-spurs-pacers-22492135.php); [Yardbarker/Heavy, 24 Oct](https://www.yardbarker.com/nba/articles/cooper_flagg_injury_update_mavericks_star_set_to_miss_at_least_one_week_after_latest_setback/s1_16751_44469302)). He returned on 26 Oct with 40 minutes.
  - Dallas had not yet filed its report for 18 Nov ("NOT YET SUBMITTED" on the [17 Nov 4:30 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_30PM.pdf)).
  - Verdict: *ESPN confirmed.* He is active, the illness is clearing, and he has no rest pattern. The L7 slump comes from two blowouts and the illness.

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **39.0** · season 39.1 (13) · L7 35.3 (3) · L15 42.8 (6) · L30 39.1 (13) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (15 Nov): Siakam recorded 31 points (12-19 FG, 0-3 3Pt, 7-8 FT), two rebounds, two assists and one steal across 34 minutes during Sunday's 131-124 loss to Philadelphia.
- News (13 Nov): Siakam posted 19 points (5-13 FG, 2-4 3Pt, 7-12 FT), three rebounds and two assists across 32 minutes in Friday's 106-104 win over the Knicks.
- **Research:**
  - reported: no definite timeline, next update about 20 Nov per Carlisle ([Forbes, 17 Nov](https://forbes.com/sites/tonyeast/2026/11/17/pacers-miss-tyrese-haliburton-more-than-just-on-court-lebron-james-knows-why))
  - On 2 Nov, the second night after 1 Nov vs BKN (36 min), the injury report listed him out "for rest purposes" against Atlanta. Indiana sat three starters that night ([IndyStar via Yahoo, 2 Nov](https://sports.yahoo.com/articles/pacers-resting-pascal-siakam-could-183414092.html); [FantasyPros, 2 Nov](https://www.fantasypros.com/nba/news/617291/pascal-siakam-rest-ruled-out-monday.php)). ClutchPoints called the rest "curious", since he was not hurt ([ClutchPoints, 2 Nov](https://clutchpoints.com/nba/indiana-pacers/pacers-news-pascal-siakam-injury-update-vs-hawks-entire-starting-lineup-out)).
  - Last season the NBA fined Indiana $100,000 for resting Siakam and two other starters on the second night of a back-to-back (3 Feb 2026) ([SI, 24 Feb 2026](https://www.si.com/nba/rick-carlisle-calls-out-nba-for-ridiculous-process-behind-pacers-tanking-fine)).
  - Verdict: *Nothing new found.* ESPN's "active" stands, and no sit has been announced. There is a pattern risk on Mon 23 and Sat 28 Nov, but it is not confirmed, so no `sit` row.

### Tyler Herro (MIL, PG/SG, Snow Time Lakers)

- Rate **35.4** · season 33.7 (13) → 36.2 (12) · L7 24.0 (3) → 34.5 (2) · L15 30.6 (7) → 35.2 (6) · L30 33.7 (13) → 36.2 (12) · projected 38.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the first night of the 10–11 Nov back-to-back, playing the games either side
- News (13 Nov): Herro had 18 points (5-17 FG, 2-7 3Pt, 6-7 FT), two assists, two steals, one rebound and one block across 34 minutes in Friday's 107-99 loss to the Magic.
- News (11 Nov): Herro had 27 points (8-16 FG, 2-7 3Pt, 9-10 FT), seven assists, two rebounds and one block across 35 minutes in Wednesday's 123-112 loss to the Lakers.
- **Research:**
  - His absence on 10 Nov, the first night of the 10–11 Nov back-to-back, was an injury: **Questionable, "Right [Knee] Contusion"**, later downgraded to out ([NBA injury report, 10 Nov 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-10_06_00PM.pdf)). He took a knee hit against Boston on 8 Nov, then played 35 minutes on 11 Nov. That gives no rest pattern.
  - Wednesday is his return to Miami, with a tribute video planned ([Yahoo Sports, 14 Nov 2026](https://sports.yahoo.com/articles/tyler-herro-returns-miami-night-171100292.html)). The Bucks' official 18 Nov report was not yet submitted at 4:30 PM. No source says he will sit on 18 or 19 Nov.
  - Verdict: nothing new found. The earlier absence was a knee contusion, not rest, and nobody has said he will sit 18 or 19 Nov.

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **32.6** · season 35.4 (12) · L7 29.7 (3) · L15 33.4 (7) · L30 35.4 (12) · projected 30.8
- ESPN: active
- **Rest:** back-to-back Wed 18–Thu 19 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (17 Nov): Podziemski recorded 15 points (3-8 FG, 3-7 3Pt, 6-7 FT), six rebounds, three assists, one steal and two blocks across 30 minutes in Monday's 115-94 loss to the Pelicans.
- News (12 Nov): Podziemski had 22 points (7-15 FG, 4-11 3Pt, 4-5 FT), six rebounds, four assists and two steals across 37 minutes during Wednesday's 115-108 loss to the Rockets.
- **Research:**
  - His only back-to-back absence was injury-related. It was not scheduled rest. On 24 Oct, the second night of the 23–24 Oct back-to-back, the official report listed him **Out, "Bilateral Low Back Injury Management"** ([NBA injury report, 24 Oct 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-24_06_00PM.pdf)). He had tweaked his back against Memphis the night before: "Just tweaked it a little bit, nothing too serious … No, I won't play tomorrow" ([Heavy, updated 24 Oct 2026](https://heavy.com/sports/nba/golden-state-warriors/warriors-curry-podziemski-injury-update-suns/)). He has had no back listing since early November.
  - He is not on the Warriors' list for Wed 18 Nov at Dallas. That list shows Curry (right oblique tear), Butler, Moody, B. Williams and Porzingis out ([NBA.com Warriors gameday preview, 17 Nov 2026](https://www.nba.com/warriors/news/gameday-preview-20261118)). The back-to-back is at Dallas and Memphis on 18–19 Nov ([Newsweek, c. 12 Nov 2026](https://www.newsweek.com/sports/nba/warriors-rocked-by-major-stephen-curry-injury-news-after-8-4-start-12707048)). The team has said nothing about sitting him on Thursday. With Curry out, he is a primary ball-handler, which makes a planned rest less likely. A back flare-up is the only known risk.
  - Verdict: nothing new found. There is no rest pattern, because the one back-to-back absence was back management. The Warriors' official 18 Nov report was not yet submitted.

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **31.2** · season 33.2 (11) · L7 28.0 (2) · L15 31.8 (5) · L30 33.2 (11) · projected 28.2
- ESPN: day-to-day, ESPN est. 18 Nov (Left Hip Soreness, updated 2026-11-15)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (15 Nov): Nembhard (hip) has been ruled out for Sunday's game against the 76ers, Tony East of Forbes.com reports.
- News (14 Nov): Nembhard is questionable for Sunday's game against the 76ers due to left hip soreness.
- **Research:**
  - Both of his earlier back-to-back second-night absences were listed as neck management, not rest. On 26 Oct (IND@MIL) he was **Questionable, "Neck Stiffness / Soreness"** at 6 PM and did not play ([NBA injury report, 26 Oct 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-26_06_00PM.pdf)). On 2 Nov vs ATL the Pacers listed him **"Out (cervical injury management)"**, and Siakam sat that same night as "Out (rest)" ([Pacers on X, 2 Nov 2026](https://x.com/Pacers/status/2117316824090247455)). Indiana manages its heavy-minutes players on second nights, so the pattern is real, even though it appears under injury labels.
  - His current status is **Questionable (sore left hip)** for Wed 18 Nov vs Houston ([NBA.com Pacers preview, 17 Nov 2026 11:03 AM ET](https://www.nba.com/pacers/news/preview-pacers-rockets-261118)). He missed 15 Nov at PHI as "Out (sore left hip)" ([Pacers on X, 15 Nov 2026](https://x.com/Pacers/status/2122014534764319109)). The Pacers' official 18 Nov report was not yet submitted at 4:30 PM. The same preview lists the schedule as road games at Cleveland and New York, then home vs OKC on Mon 23 Nov. Nobody has said he will sit 22 or 23 Nov. The new hip problem adds risk for the second night (23 Nov vs OKC).
  - Verdict: ESPN confirmed. *ESPN est.* 18 Nov matches the questionable tag for 18 Nov. On rest, nothing new was found: no team statement on 22–23 Nov, but he has a two-for-two history of sitting the second night under neck labels.

## Other rosters: injury flags only

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 22 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 22 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 22 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - The team has given no new timeline since the original report. On 24 Oct an MRI confirmed a **low-grade high ankle sprain**, and the Magic said they would "provide updates as appropriate." Banchero said he could miss "at least a month" ([Heavy, updated 25 Oct 2026](https://heavy.com/sports/nba/orlando-magic/paolo-banchero-injury-return-timeline/)). I found no report of practice or contact work since.
  - ESPN's 22 Nov sits at the **early end** of the 4–6 week window (24 Oct + 4 weeks = 21 Nov). It is defensible as a floor. With no progress reports and a high-ankle injury, it is more likely to be too early than too late, but no source gives a later date. Previews still repeat "est. return Nov. 22," which is an aggregator estimate, not a team statement ([Yahoo Sports, 17 Nov 2026](https://sports.yahoo.com/articles/magic-vs-76ers-watch-injury-173700538.html)). No source gives a first game.
  - His status now: **Out, "Right High Ankle Sprain"** for Wed 18 Nov vs Philadelphia ([NBA injury report, 17 Nov 2026 4:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_30PM.pdf)). He was also out on 16 Nov at Boston. Nothing new has come from Orlando.
  - Verdict: nothing new found. ESPN's 22 Nov matches the early end of the reported 4–6 weeks and is unconfirmed by the team. Expect slippage toward late November or early December unless a practice report appears. The 4-week floor has not passed yet, so the "7 days after the latest out report" rule does not apply.

### Bam Adebayo (MIA, PF/C, Lauri Birds)

- Rate **44.7** · season 44.1 (14) · L7 43.8 (4) · L15 47.1 (8) · L30 44.1 (14) · projected 39.6
- ESPN: day-to-day, ESPN est. 18 Nov (Right Hip, updated 2026-11-17)
- **Injury:** ESPN est. 18 Nov (Day-To-Day, Right Hip, updated 17 Nov), but the news said on 16 Nov: "Miami will presumably re-evaluate Adebayo over the next few days to determine whether he'll be able to suit up for Wednesday's game against Milwaukee."
- News (16 Nov): Coach Erik Spoelstra stated after Monday's 128-110 win over Houston that the team held Adebayo (hip) out of the second half in an effort to be proactive, and the injury isn't expected to be a long-term issue, Anthony Chiang of the Miami Herald reports.
- News (16 Nov): Adebayo (hip) has been ruled out for the remainder of Monday's game against the Rockets, Eric Nehm of The Athletic reports. He'll end with four points (1-3 FG, 0-1 3Pt, 2-4 FT), one rebound, two assists and two steals in 16 minutes.
- **Research:**
  - The official report lists him **Probable, "Right Hip Impingement"** for Wed 18 Nov vs Milwaukee ([NBA injury report, 17 Nov 2026 4:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_30PM.pdf)). That replaces the "re-evaluate over the next few days" speculation in the flag.
  - Spoelstra said holding him out of the second half on 16 Nov was "proactive" and that he doesn't expect "a long-term issue" ([NBC Sports / Rotoworld, 16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/spoelstra-heat-proactive-in-sitting-bam-hip)). He also said "let's sit him down and evaluate him tomorrow" ([Bleacher Report, 17 Nov 2026](https://bleacherreport.com/articles/25534495-bam-adebayo-injured-latest-heat-stars-timeline-return-ahead-game-vs-tyler-herro-bucks)). His first expected game is **Wed 18 Nov vs MIL**.
  - Verdict: ESPN confirmed. *ESPN est.* 18 Nov matches the official Probable tag for 18 Nov.

### Julius Randle (BKN, PF, Dr White Slong)

- Rate **37.8** · season 35.2 (13) · L7 41.7 (3) · L15 35.9 (7) · L30 35.2 (13) · projected 37.0
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Randle exited Monday's game against the 76ers during the fourth quarter to get stitches in his mouth but returned with 5:01 remaining in the period, Chris Hine of The Philly Inquirer reports."
- News (16 Nov): Randle collected 33 points (13-20 FG, 2-4 3Pt, 5-5 FT), six rebounds, one assist, two steals and one block in 33 minutes during Monday's 135-123 loss to the 76ers.
- News (16 Nov): Randle exited Monday's game against the 76ers during the fourth quarter to get stitches in his mouth but returned with 5:01 remaining in the period, Chris Hine of The Philly Inquirer reports.
- **Research:**
  - RotoWire, updated 17 Nov 2026: Randle left in the 4th quarter after a collision with Jaylen Brown to get stitches in his mouth, then returned with 5:01 left and finished with 33 points in 33 minutes. Headline: "Cleared to return after getting stitches." [RotoWire](https://www.rotowire.com/basketball/headlines/julius-randle-news-cleared-to-return-after-getting-stitches-539506)
  - AP/Fox Sports preview of Wed 18 Nov vs CHI, published 17 Nov 2026, 2:03 AM ET: the Nets' only listed injury is Michael Porter Jr. (day-to-day, personal). Randle is not listed. [Fox Sports](https://www.foxsports.com/articles/nba/randle-and-the-nets-host-conference-foe-chicago)
  - Verdict: ESPN confirmed. He is active, and the mouth cut needed only a few minutes of treatment.

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **35.3** · season 36.0 (12) · L7 34.3 (3) · L15 32.9 (7) · L30 36.0 (12) · projected 45.4
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 16 Nov: "Embiid (foot) is questionable for Monday's game against the Nets."
- News (16 Nov): Embiid provided 37 points (13-22 FG, 2-4 3Pt, 9-10 FT), five rebounds, one assist, one steal and two blocks in 32 minutes during Monday's 135-123 win over the Nets.
- News (16 Nov): Embiid (foot) is available for Monday's game against Brooklyn.
- **Research:**
  - Heavy via Yahoo, 16 Nov 2026: Nick Nurse called Sunday's 15 Nov rest (vs IND) "part of the plan of the management." The team chose that night as the rest day of the 15-16 Nov back-to-back. No new setback was reported. [Yahoo/Heavy](https://sports.yahoo.com/articles/76ers-joel-embiid-gets-encouraging-222340817.html). He was then upgraded and played 16 Nov at BKN: a season-high 37 points in 32 minutes.
  - Sportsmole preview of Wed 18 Nov at ORL, 17 Nov 2026: Embiid "carries no current injury designation." The Sixers' listed injuries are Jaylen Brown (hamstring and head), LeBron James (back), Dominick Barlow (back), Adem Bona (back) and Ariel Hukporti (Achilles). [Sportsmole](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/philadelphia-76ers-vs-orlando-magic-player-props-injury-report-and-prediction--nba_609259.html)
  - FanDuel Research, 17 Nov 2026 03:32 UTC, lists him "day-to-day" for 18 Nov at ORL. That is an automated (Data Skrive) carry-over from the 16 Nov questionable tag, and no beat source repeats it. [FanDuel](https://www.fanduel.com/research/nba/player-news/injuries/joel-embiid-dtd-november-18-2026-against-magic-foot)
  - Verdict: ESPN confirmed. He is active for 18 Nov at ORL with no new designation found. The foot management is ongoing and points to a missed night in each upcoming back-to-back (27-28 Nov, 1-2 Dec). Re-check once the team names the night.

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-17 21:18 UTC.
- [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-another-absence-coming-539612)
- [CBS/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)
- [DBB via Yahoo, 17 Nov](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html)
- [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)
- [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/scottie-barnes-injury-late-addition-to-injury-report-539587)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/kawhi-leonards-knee-keeps-raptors-200300316.html)
- [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466)
- [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)
- [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html)
- [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)
- [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)
- [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/nic-claxton-scores-17-points-in-16-minutes)
- [NBA.com/AP, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring)
- [NBA injury report, 17 Nov 4:15 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_15PM.pdf)
- [Yahoo Sports, 17 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-065639408.html)
- [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/chicago-bulls/bulls-news-jalen-smith-update-scary-fall-cavs)
- [Joel Lorenzi (The Athletic) on X, 16 Nov](https://x.com/JoelXLorenzi/status/2122530901733134678)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/jalen-smith-finger-downgraded-to-out-vs-wolves)
- [RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-officially-active-539138)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/yves-missi-produces-14-rebounds-three-steals)
- [SI/Pelicans Scoop piece](https://www.si.com/nba/pelicans/onsi/2-effects-yves-missi-s-return-is-already-having-on-the-pelicans-01m7nfdsnk3s)
- [ClutchPoints, 17 Nov](https://clutchpoints.com/nba/nba-stories/knicks-vs-raptors-injury-report-is-kawhi-leonard-back-yet)
- [HEAVY via Yahoo, 10 Nov](https://sports.yahoo.com/articles/raptors-latest-kawhi-leonard-raises-203907902.html)
- [ESPN, 10 Nov](https://www.espn.com/nba/story/_/id/50444283/raptors-kawhi-leonard-least-1-more-week-due-knee)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/kawhi-leonard-knee-limited-to-individual-work)
- [Basketnews, 29 Oct](https://basketnews.com/news-258440-kawhi-leonard-injury-timeline-gets-worse-worrying-update-emerges.html)
- [Utah Jazz On SI, 6 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-announce-new-timeline-for-jusuf-nurkic-s-return)
- [Hoops Rumors, 15 Nov](https://hoopsrumors.com/2026/11/injury-notes-clippers-miller-barnes-nurkic-b-williams.html)
- [Utah Jazz On SI, 15 Nov](https://si.com/nba/jazz/onsi/jazz-vs-spurs-injury-report-reveals-major-problem-for-utah-rotation)
- [Utah Jazz On SI, 16 Nov](https://si.com/nba/jazz/onsi/utah-jazz-sign-familiar-center-as-frontcourt-injuries-pile-up)
- [NBA.com/AP, 14 Nov](https://www.nba.com/news/dejounte-murray-requests-trade-pelicans-confirm)
- [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/new-orleans-pelicans/warriors-vs-pelicans-injury-report-dejounte-murray-listed-requesting-trade)
- [Basketnews, 17 Nov](https://basketnews.com/news-259630-dejounte-murray-gets-horrible-trade-update-with-pelicans.html)
- [CBS gametracker, 9 Nov](https://www.cbssports.com/nba/gametracker/recap/NBA_20261109_NO@GS/)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter)
- [RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/jalen-suggs-news-starting-monday-539472)
- [ClutchPoints, 14 Nov](https://clutchpoints.com/nba/orlando-magic/magic-news-sean-sweeney-jalen-suggs-return-injury-bucks)
- [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/jaxson-hayes-injury-remaining-out-tuesday-539488)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jaxson-hayes-knee-remains-out-tuesday-vs-lac)
- [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)
- [ClutchPoints, 16 Nov](https://clutchpoints.com/nba/oklahoma-city-thunder/thunder-news-aday-maras-double-double-night-mark-daigneault-eye-opening-take)
- [RotoWire, 11 Nov](https://www.rotowire.com/basketball/headlines/jaylin-williams-injury-remains-out-indefinitely-538633)
- [Yahoo, 15 Nov](https://sports.yahoo.com/articles/full-injury-report-sundays-thunder-140133905.html)
- [Thunder medical update, 30 Oct](https://www.nba.com/thunder/news/medical-update-261030)
- [News 5 Cleveland, 14 Nov](https://www.news5cleveland.com/sports/basketball/cavaliers/cavs-rule-out-8-players-for-game-against-mavericks-including-entire-starting-lineup)
- [Hoops Wire via Yardbarker, 15 Nov](https://www.yardbarker.com/nba/articles/tyrese_proctor_gives_cavs_a_rotation_question_worth_answering/s1_17038_44563735)
- [Cavaliers Nation, 16 Nov](https://cavaliersnation.com/2026/11/16/evan-mobley-faces-longer-absence-as-cavs-announce-reevaluation-plan/)
- [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-tyrese-proctor-remains-productive-monday/)
- [Cavaliers Nation, 15 Nov](https://cavaliersnation.com/2026/11/15/kenny-atkinson-calls-tyrese-proctor-a-changed-man-after-cavs-breakout/)
- [RotoWire, 15 Nov](https://www.rotowire.com/basketball/headlines/grayson-allen-news-not-starting-sunday-539277)
- [Heavy, 15 Nov](https://heavy.com/sports/nba/charlotte-hornets/hornets-brandon-miller-cleared-return-clippers/)
- [AOL, 16 Nov](https://www.aol.com/articles/offensive-foul-announcers-fume-hornets-113000000.html)
- [iHeart/Fox Sports 104.9, 17 Nov](https://1049foxsports.iheart.com/content/2026-11-17-hornets-vs-lakers-injury-report-nov-17/)
- [Fadeaway World via Yardbarker, 8 Nov](https://www.yardbarker.com/nba/articles/hornets_injury_update_latest_on_brandon_miller_expected_timelines_for_kon_knueppel_dennis_schroder/s1_16751_44534895)
- [official 4 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_00PM.pdf)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/austin-reaves-heel-remains-out-vs-charlotte)
- [Lakers Nation, 16 Nov](https://lakersnation.com/lakers-injury-report-walker-kessler-austin-reaves-out-vs-hornets/)
- [CBS Sports / RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-officially-out-monday/)
- [official 16 Nov 8 PM report](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_08_00PM.pdf)
- [ABC News / AP, 17 Nov](https://abcnews.com/Sports/wireStory/memphis-faces-cleveland-3-game-win-streak-138201498)
- [Akron Beacon Journal via Yahoo, 17 Nov](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html)
- [Yahoo, 16 Nov](https://sports.yahoo.com/articles/cavaliers-star-forward-7-10-221034351.html)
- [Roundtable Sports via Yahoo, 16 Nov](https://sports.yahoo.com/articles/grizzlies-rule-isaiah-stewart-vs-181202853.html)
- [CBS Sports / RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-isaiah-stewart-out-sick-monday/)
- [Field Level Media, 17 Nov](https://fieldlevelmedia.com/nba/travel-proven-grizzlies-chase-franchise-road-mark-at-cleveland/)
- [FantasyPros, 16-17 Nov](https://www.fantasypros.com/nba/news/620738/zach-edey-logs-double-double-win-monday.php)
- [Memphis Flyer](https://www.memphisflyer.com/grizzlies-beat-wizards-stay-perfect-on-the-road/)
- [Chicago Sun-Times, 11 Nov](https://chicago.suntimes.com/bulls/2026/11/11/bulls-rookie-caleb-wilson-answers-bell-sore-hip)
- [Bulls / NBA.com, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)
- [CBS Sports, 12 Nov](https://www.cbssports.com/nba/news/caleb-wilson-injury-update-bulls-rookie-of-the-year/)
- [NBA.com, 13 Nov](https://www.nba.com/news/bulls-caleb-wilson-hand-injury)
- [SI, 12 Nov](https://www.si.com/nba/bulls/onsi/caleb-wilson-to-undergo-hand-surgery-when-will-the-bulls-get-him-back-12)
- [Hoops Rumors, 17 Nov](https://www.hoopsrumors.com/2026/11/pistons-duncan-robinson-quad-out-at-least-one-week.html)
- [Heavy, 17 Nov](https://heavy.com/sports/nba/detroit-pistons/pistons-duncan-robinson-ron-holland-injuries/)
- [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-collin-murray-boyles-strong-showing-at-both-ends-of-court/)
- [CBS box score, 15 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261115_NY@TOR/)
- [Raptors Republic via Yardbarker, 15 Nov](https://www.yardbarker.com/nba/articles/raptors_barnes_set_to_return_against_the_new_york_knicks/s1_17733_44566341)
- [Raptors Republic, 15 Nov](https://raptorsrepublic.com/2026/11/15/raptors-fall-in-overtime-to-knicks-in-scottie-barnes-return/)
- [Raptors Republic, 17 Nov](https://raptorsrepublic.com/2026/11/17/gameday-knicks-raptors-november-17th/)
- [NBC Sports/Rotoworld, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/ind-starts-nembhard-oubre-nesmith-siakam-zubac)
- [CBS/RotoWire, 13 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-kelly-oubre-another-positive-showing/)
- [NBA.com Pacers preview, 17 Nov](https://www.nba.com/pacers/news/preview-pacers-rockets-261118)
- [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-firm-timetable-for-return/)
- [Yardbarker, 17 Nov](https://www.yardbarker.com/nba/articles/pacers_announce_tyrese_haliburton_injury_update/s1_17355_44575841)
- [NBA injury report, 16 Nov 7:00 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-16_07_00PM.pdf)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/zach-edey-ankle-upgraded-to-available-monday)
- [NBC Sports, 24 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/zach-edey-ankle-ruled-out-vs-sacramento)
- [Yahoo, 14 Nov](https://sports.yahoo.com/articles/grizzlies-zach-edey-jerami-grant-010359185.html)
- [RotoWire via CBS Sports, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/celtics-neemias-queta-sitting-out-monday-539449/)
- [Fox Sports](https://www.foxsports.com/articles/nba/boston-takes-road-win-streak-into-matchup-with-denver)
- [Yahoo, 16 Nov](https://sports.yahoo.com/articles/celtics-starter-injury-report-ahead-193514066.html)
- [CBS/RotoWire, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-myles-turner-resting-wednesday/)
- [SI All Bucks, 14 Nov](https://www.si.com/nba/bucks/onsi/3-losers-1-surprising-winner-as-bucks-fall-to-the-magic-01m7bp7yx577)
- [SI All Bucks, 11 Nov](https://www.si.com/nba/bucks/onsi/kel-el-ware-must-capitalize-on-a-big-opportunity-against-the-los-angeles-lakers-01m769zw3txe)
- [NBC Sports/Rotoworld citing Mike Curtis, DMN, 17 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/max-christie-santi-aldama-get-in-full-practice)
- [Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)
- [Dallas Sports Journal, 15 Nov](https://dallassportsjournal.com/daniel-gafford-available-santi-aldama-out-mavericks-celtics/)
- [KFAN, 17 Nov](https://kfan.iheart.com/content/2026-11-17-trail-blazers-vs-timberwolves-injury-report-nov-17/)
- [ClutchPoints, 17 Nov](https://clutchpoints.com/nba/nba-stories/blazers-news-ja-morant-all-smiles-deni-avdija-injury-return-tease-timberwolves-beatdown)
- [KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)
- [NBC Sports/Rotoworld, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/nori-morant-could-be-back-sooner-than-expected)
- [FantasyAlarm, 16 Nov](https://fantasyalarm.com/articles/nba/fantasy-basketball-injury-report/nba-injury-report-week-5-2026-fantasy-basketball/198796)
- [Philadelphia Inquirer, Gina Mizell, 17 Nov](https://www.inquirer.com/sixers/jaylen-brown-injury-update-nets-score-highlights-20261117.html)
- [NBA.com/AP, 17 Nov](https://www.nba.com/news/sixers-jaylen-brown-says-head-injury-is-ok-will-find-out-more-about-hamstring)
- [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/jaylen-brown-injury-set-for-further-evaluation-tuesday-539522)
- [Sports Mole, 17 Nov](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/philadelphia-76ers-vs-orlando-magic-player-props-injury-report-and-prediction--nba_609259.html)
- [NBA injury report, 17 Nov 4:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-17_04_30PM.pdf)
- [NBC Sports/Rotoworld, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/deaaron-fox-hip-removed-from-injury-report)
- [BasketNews, 16 Nov](https://basketnews.com/news-259619-spurs-make-critical-deaaron-fox-injury-status-update-vs-pistons.html)
- [Chicago Sun-Times, 12 Nov](https://chicago.suntimes.com/bulls/2026/11/12/bulls-losing-demoralizing-understanding-process)
- [NBC Sports/Rotoworld, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/norman-powell-has-33-points-in-win-over-hawks-friday)
- [RotoWire, 17 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-news-cleared-to-return-539493)
- [ClutchPoints, 6 Nov](https://clutchpoints.com/nba/charlotte-hornets/hornets-news-brandon-miller-exits-celtics-clash-groin-soreness)
- [Yahoo/All Hornets, 12 Nov](https://sports.yahoo.com/articles/hornets-injury-diabat-trending-miller-130048683.html)
- [CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-struggles-in-return/)
- [NBC Sports/Rotoworld, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/brandon-miller-hip-off-injury-report-vs-lac)
- [Dallas Morning News via Yahoo, 16 Nov](https://sports.yahoo.com/articles/cooper-flagg-looks-mavericks-veterans-211854890.html)
- [Dallas News, 24 Oct](https://www.dallasnews.com/sports/mavericks/article/cooper-flagg-injury-update-mavericks-spurs-pacers-22492135.php)
- [Yardbarker/Heavy, 24 Oct](https://www.yardbarker.com/nba/articles/cooper_flagg_injury_update_mavericks_star_set_to_miss_at_least_one_week_after_latest_setback/s1_16751_44469302)
- [Forbes, 17 Nov](https://forbes.com/sites/tonyeast/2026/11/17/pacers-miss-tyrese-haliburton-more-than-just-on-court-lebron-james-knows-why)
- [IndyStar via Yahoo, 2 Nov](https://sports.yahoo.com/articles/pacers-resting-pascal-siakam-could-183414092.html)
- [FantasyPros, 2 Nov](https://www.fantasypros.com/nba/news/617291/pascal-siakam-rest-ruled-out-monday.php)
- [ClutchPoints, 2 Nov](https://clutchpoints.com/nba/indiana-pacers/pacers-news-pascal-siakam-injury-update-vs-hawks-entire-starting-lineup-out)
- [SI, 24 Feb 2026](https://www.si.com/nba/rick-carlisle-calls-out-nba-for-ridiculous-process-behind-pacers-tanking-fine)
- [NBA injury report, 10 Nov 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-10_06_00PM.pdf)
- [Yahoo Sports, 14 Nov 2026](https://sports.yahoo.com/articles/tyler-herro-returns-miami-night-171100292.html)
- [NBA injury report, 24 Oct 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-24_06_00PM.pdf)
- [Heavy, updated 24 Oct 2026](https://heavy.com/sports/nba/golden-state-warriors/warriors-curry-podziemski-injury-update-suns/)
- [NBA.com Warriors gameday preview, 17 Nov 2026](https://www.nba.com/warriors/news/gameday-preview-20261118)
- [Newsweek, c. 12 Nov 2026](https://www.newsweek.com/sports/nba/warriors-rocked-by-major-stephen-curry-injury-news-after-8-4-start-12707048)
- [NBA injury report, 26 Oct 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-10-26_06_00PM.pdf)
- [Pacers on X, 2 Nov 2026](https://x.com/Pacers/status/2117316824090247455)
- [Pacers on X, 15 Nov 2026](https://x.com/Pacers/status/2122014534764319109)
- [Heavy, updated 25 Oct 2026](https://heavy.com/sports/nba/orlando-magic/paolo-banchero-injury-return-timeline/)
- [Yahoo Sports, 17 Nov 2026](https://sports.yahoo.com/articles/magic-vs-76ers-watch-injury-173700538.html)
- [NBC Sports / Rotoworld, 16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/spoelstra-heat-proactive-in-sitting-bam-hip)
- [Bleacher Report, 17 Nov 2026](https://bleacherreport.com/articles/25534495-bam-adebayo-injured-latest-heat-stars-timeline-return-ahead-game-vs-tyler-herro-bucks)
- [RotoWire](https://www.rotowire.com/basketball/headlines/julius-randle-news-cleared-to-return-after-getting-stitches-539506)
- [Fox Sports](https://www.foxsports.com/articles/nba/randle-and-the-nets-host-conference-foe-chicago)
- [Yahoo/Heavy](https://sports.yahoo.com/articles/76ers-joel-embiid-gets-encouraging-222340817.html)
- [FanDuel](https://www.fanduel.com/research/nba/player-news/injuries/joel-embiid-dtd-november-18-2026-against-magic-foot)
