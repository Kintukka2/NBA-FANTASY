# News watch: 19 Nov 2026

- Generated 2026-11-20 03:47 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 53 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Snow Time Lakers, Matt Wright's Foxies). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 37 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## What changed for us

**Moves recorded by the ESPN sync:** none since 19 Nov, when Kel'el Ware came in for Mo Bamba. 3 of 7 adds used.

**Our players:**
- **Cade Cunningham:** probable Fri vs TOR after sitting 18 Nov with knee soreness ([RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/cade-cunningham-injury-expected-to-play-friday-540045)); *ESPN est.* 20 Nov.
- **Scottie Barnes:** off the injury report. His 18 Nov absence was planned groin management.
- **Jalen Duren** (IR): out Fri. Re-evaluated about 22 Nov ([AP via NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring)); *ESPN est.* 24 Nov.
- **Kel'el Ware:** his 19 Nov start was a one-off. Myles Turner is expected back Sat 21 Nov ([RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/myles-turner-injury-sidelined-by-left-shoulder-contusion-540024)); *ESPN est.* 21 Nov.
- **Saddiq Bey:** his start lasts only while Trey Murphy III sits.
- **Daniss Jenkins:** "should remain a starter until Jalen Duren returns" (NBC Sports, 18 Nov).
- **Yves Missi:** still on a minutes limit of about 22.
- **Paul George:** sat both earlier road second nights. Sun 22 at GS is a road second night, a pattern risk only.

**Free agents in the plan:**
- **Trey Murphy III** is **questionable** for Fri at OKC, upgraded from out ([NBA injury report, 19 Nov 10:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)); *ESPN est.* 20 Nov.
- **Quentin Grimes** keeps starting with Austin Reaves out Fri ([RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/austin-reaves-injury-still-out-friday-540088)); Reaves *ESPN est.* 23 Nov.
- **Aday Mara** plays about 26 min whether or not he starts. **Neemias Queta** rested 1 of 4 back-to-backs, so Sun 22 is his risk night.
- **Derik Queen** plays about 21 min with or without Murphy. **Matas Buzelis** has played every Bulls game.

**Snow Time Lakers:**
- **Jaylen Brown** is re-evaluated before Sat vs MIL and could be cleared; *ESPN est.* 23 Nov.
- **Kyrie Irving** sat 2 of 3 second nights. Sun 22 at UTAH is one.

**Overrides:**
- **Added:**
  - Quentin Grimes, role 36 (20 Nov).
  - Tyrese Proctor, role 27 (to 22 Nov).
  - Jalen Suggs, role 30, replacing the 25-minute row.
- **Updated:**
  - Jusuf Nurkic, return 26 Nov (week-to-week, out Fri; the old 21 Nov row would have counted him on Sunday).
  - Scotty Pippen Jr., return 23 Nov.
  - Dejounte Murray, return 26 Nov.
- **Removed:** the expired Murphy sit and Grimes role rows.
- **Not added:**
  - Brandon Miller's role (next week's opponent; his minutes are still ramping).
  - Ja Morant's and Brandon Ingram's return floors (earlier than ESPN, or based on a coach's expectation).
  - Maxime Raynaud's floor (the same as ESPN).
  - Mo Bamba's role (on waivers).
  - Missi's minutes limit (it would raise his projection).

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| CJ McCollum | role | 23 | 2026-11-22 | [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466) | in force |
| Jusuf Nurkic | return | 2026-11-21 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2) | in force |
| Jalen Duren | return | 2026-11-23 | — | [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/) | in force |
| Scotty Pippen Jr. | return | 2026-11-22 | — | [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html) | in force |
| Dejounte Murray | return | 2026-11-23 | — | [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) | in force |
| Saddiq Bey | role | 34 | 2026-11-24 | [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/) | in force |
| Daniss Jenkins | role | 35 | 2026-11-22 | [link](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html) | in force |
| Jalen Suggs | role | 25 | 2026-11-22 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter) | in force |
| Trey Murphy III | sit | 2026-11-18 | — | [link](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-another-absence-coming-539612) | expired: remove it |
| Quentin Grimes | role | 35 | 2026-11-17 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/austin-reaves-heel-remains-out-vs-charlotte) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Scottie Barnes** | TOR | us | injury | 48.0 | — | active |
| **Jalen Duren** | DET | us | injury, gap | 44.1 † | — | out, ESPN est. 24 Nov |
| **Saddiq Bey** | NO | us | role, minutes | 34.8 | 36.0 | active |
| **Kel'el Ware** | MIL | us | role | 23.9 | 30.2 | active |
| **Cade Cunningham** | DET | us | minutes | 57.2 | 58.9 | day-to-day, ESPN est. 20 Nov |
| **Daniss Jenkins** | DET | us | minutes | 33.8 | 37.8 | active |
| **Yves Missi** | NO | us | minutes | 27.6 | — | active |
| **Jalen Smith** | CHI | us | rest | 42.2 | — | active |
| **Paul George** | BOS | us | rest | 36.3 | — | active |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 25 Nov |
| **Robert Williams III** | POR | free agent | injury | 23.2 | — | out, ESPN est. 21 Nov |
| **Scotty Pippen Jr.** | MEM | free agent | injury | 16.3 | — | out, ESPN est. 25 Nov |
| **Jalen Suggs** | ORL | free agent | role, minutes | 35.8 | — | active |
| **Quentin Grimes** | LAL | free agent | role, minutes | 35.2 | 30.8 | active |
| **Mo Bamba** | UTAH | waivers | role, minutes | 34.3 | 44.6 | active |
| **Aday Mara** | OKC | free agent | role | 31.4 | — | active |
| **Tyrese Proctor** | CLE | free agent | role, minutes | 28.8 | 31.2 | active |
| **Grayson Allen** | CHA | free agent | role | 28.6 | 29.7 | out, ESPN est. 23 Nov |
| **Jaylon Tyson** | CLE | free agent | role, minutes | 23.1 | 25.8 | out, ESPN est. 23 Nov |
| **Kasparas Jakucionis** | MIL | free agent | minutes | 28.7 | 26.3 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 28.0 | 26.1 | out, ESPN est. 13 Dec |
| **P.J. Washington** | DAL | free agent | minutes | 27.6 | 23.4 | active |
| **Dejounte Murray** | NO | free agent | minutes, gap | 27.2 | 24.0 | out, ESPN est. 27 Nov |
| **T.J. McConnell** | IND | free agent | minutes | 25.1 | — | day-to-day, ESPN est. 20 Nov |
| **Precious Achiuwa** | SAC | free agent | minutes | 13.5 | 19.8 | day-to-day, ESPN est. 20 Nov |
| **Neemias Queta** | BOS | free agent | rest | 32.1 | — | active |
| **Ja Morant** | POR | free agent | gap | 34.1 | — | out, ESPN est. 01 Dec |
| **Jaylen Brown** | PHI | Snow Time Lakers | injury | 42.4 | — | out, ESPN est. 23 Nov |
| **Brandin Podziemski** | GS | Matt Wright's Foxies | minutes | 28.0 | — | active |
| **Brandon Miller** | CHA | Matt Wright's Foxies | minutes | 24.6 | 22.6 | active |
| **Cooper Flagg** | DAL | Matt Wright's Foxies | rest | 46.8 | — | active |
| **Kyrie Irving** | DAL | Snow Time Lakers | rest | 43.0 | — | active |
| **Pascal Siakam** | IND | Matt Wright's Foxies | rest | 40.4 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 25.9 | — | day-to-day, ESPN est. 20 Nov |
| **Jalen Brunson** | NY | Melbourne poopoo | injury | 46.2 | — | active |
| **Brandon Ingram** | LAC | Melbourne poopoo | injury | 36.5 | — | out, ESPN est. 21 Nov |
| **Paolo Banchero** | ORL | Dr White Slong | gap | 60.9 † | — | out, ESPN est. 29 Nov |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Scottie Barnes (TOR, SG/SF, us)

- Rate **48.0** · season 46.5 (10) → 50.3 (9) · L7 49.0 (2) · L15 44.0 (3) · L30 46.5 (10) → 50.3 (9) · projected 43.7
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 18 Nov: "Barnes (injury management) has been ruled out for Wednesday's game against Washington, Esfandiar Baraheni of The Athletic reports."
- News (19 Nov): Barnes (groin) will play in Friday's game against the Pistons, Blake Murphy of Sportsnet.ca reports.
- News (18 Nov): Barnes (injury management) has been ruled out for Wednesday's game against Washington, Esfandiar Baraheni of The Athletic reports.
- **Research:**
  - On 18 Nov he sat the second leg of the Knicks/Wizards back-to-back for **left groin injury management**. Rajakovic said this was planned, with three games in four nights. Sources: [Canadian Press via Yahoo, 18 Nov](https://ca.sports.yahoo.com/news/raptors-forward-barnes-against-wizards-183808081.html) and [NBC Sports (Zak Hanshew), 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/scottie-barnes-groin-out-wednesday). It was a one-night precaution after his four-game groin absence, not a new injury.
  - He is **off the injury report and will play Fri 20 Nov at DET**, per Blake Murphy of Sportsnet via [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/scottie-barnes-news-removed-from-injury-report-540046). The NBA report of 19 Nov 10:45 PM ([PDF](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)) lists Barrett, Leonard, Murray-Boyles and three G-League players for TOR, but not Barnes. Jamison Battle goes back to the bench.
  - Verdict: ESPN confirmed (active, plays Friday).

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 33.5 (2) → 44.0 (1) · projected 42.2
- ESPN: out, ESPN est. 24 Nov (Right Hamstring Strain, updated 2026-11-08)
- **Injury:** ESPN est. 24 Nov (Out, Right Hamstring Strain, updated 08 Nov), but the news said on 08 Nov: "Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 24 Nov)
- News (08 Nov): Duren (hamstring) has begun on-court activity and will be re-evaluated in two weeks, Hunter Patterson of The Athletic reports.
- News (25 Oct): Duren will be re-evaluated in two weeks due to a right hamstring strain, Eric Vincent of ClutchPoints.com reports.
- **Research:**
  - The latest team word is still 8 Nov. He will "miss at least two more weeks" and has been "cleared for full basketball participation", per [AP via NBA.com (Dave Hogg), 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring). Bickerstaff said they won't rush him, per [Detroit Sports Nation, 8 Nov](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/). On that timeline the re-evaluation falls about **Sun 22 Nov at ATL**, per [Yahoo (Teddy Ricketson), 8 Nov](https://sports.yahoo.com/nba/article/pistons-say-c-jalen-duren-will-miss-at-least-another-two-weeks-due-to-hamstring-strain-165124644.html). That is an inference from "two weeks", not a team date.
  - He is listed **Out (right hamstring strain) for Fri 20 Nov vs TOR** on the NBA report of 19 Nov 10:45 PM ([PDF](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)). I found no practice report or Bickerstaff update since 8 Nov. The next news should be the ~22 Nov re-evaluation.
  - Verdict: ESPN confirmed (nothing new since 8 Nov).

### Saddiq Bey (NO, SF/PF, us)

- Rate **34.8** · role rate 36.0 · season 30.4 (16) · L7 41.0 (4) · L15 33.0 (9) · L30 30.4 (16) · projected 25.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 14 before; 35.0 min in his starts, against 29.6 for the season
- **Minutes:** 38.7 min over his last 3 games against 29.6 for the season (+9.1)
- News (19 Nov): Bey logged 10 points (3-13 FG, 2-7 3Pt, 2-2 FT), eight rebounds, six assists and one steal across 42 minutes during Wednesday's 122-109 loss to the Pistons.
- News (17 Nov): Bey finished with 23 points (8-15 FG, 5-8 3Pt, 2-2 FT), six rebounds, three assists, one steal and one block across 33 minutes in Monday's 115-94 win over Golden State.
- **Research:**
  - The role depends entirely on **Trey Murphy's absence**. "Bey will keep starting if Murphy stays out", and he will likely head back to the bench once Murphy is available, per [NBC Sports (Nick Shlain), 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/trey-murphy-knee-questionable-friday-vs-thunder). Murphy is **questionable for Fri 20 Nov at OKC** on the NBA report of 19 Nov 10:45 PM ([PDF](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)). Saturday at SA (second leg of a back-to-back) has no report yet.
  - Off the bench this season he averaged 26.9 min over 10 games, per RotoWire on 12 Nov (in the batch JSON). That is the fallback if Murphy returns. [Pelicans On SI via Yahoo (David Grubb), 19 Nov](https://sports.yahoo.com/articles/jamahl-mosley-gets-f-pelicans-170006841.html) argues he is better off the bench. That is opinion, not a team decision.
  - The cause is a rotation gap, not blowouts. Murphy, Dejounte Murray, Mathurin (left plantar fasciitis), Watford (right ankle sprain) and McGowens are all out, per the [NBA report, 19 Nov](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf). The 41-minute game (14 Nov) came on a back-to-back. The 42 minutes on 18 Nov came on 3-of-13 shooting in a 13-point loss. The minutes last only as long as Murphy sits.
  - Verdict: ESPN confirmed (active; the role is still conditional on Murphy).

### Kel'el Ware (MIL, C, us)

- Rate **23.9** · role rate 30.2 · season 22.9 (16) · L7 26.8 (4) · L15 19.3 (9) · L30 22.9 (16) · projected 33.8
- ESPN: active
- **Role:** started 1 of his last 2 games after 1 of 14 before; 24.5 min in his starts, against 18.6 for the season
- News (19 Nov): Ware is starting Thursday's game against Portland.
- News (13 Nov): Ware won't start Friday's game against the Magic.
- **Research:**
  - This was a **one-off injury fill-in**. He started Thu 19 Nov vs POR with Burries, Herro, Ament and Nance, per [NBC Sports (Nick Shlain), 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/kelel-ware-nate-amnet-larry-nance-start-vs-por). Myles Turner was out with a **left shoulder contusion** and Kuzma with a right shoulder contusion, on the second night of a back-to-back. Turner's "next opportunity to return will come Saturday against Philadelphia", per [RotoWire, 19 Nov 12:32 PM](https://www.rotowire.com/basketball/headlines/myles-turner-injury-sidelined-by-left-shoulder-contusion-540024). ESPN has Turner back 21 Nov. The same thing happened before: Ware started 11 Nov when Turner rested and went back to the bench on 13 Nov when Turner returned (batch JSON news).
  - Ware played 26 minutes for 18 FP in that start. Turner's return ends the role. Only if Turner is also out Sat 21 Nov at PHI (1 PM ET) would Ware likely start again. A "Ware should start" column ([Behind the Buck Pass, 15 Nov](https://behindthebuckpass.com/kelel-ware-rejoining-bucks-starting-five-inevitable-next-step)) is opinion, with no coach quote. Bench minutes are about 17–25.
  - Verdict: nothing new found. No ongoing role change is reported.

### Cade Cunningham (DET, PG, us)

- Rate **57.2** · role rate 58.9 · season 50.7 (13) · L7 66.7 (3) · L15 54.5 (6) · L30 50.7 (13) · projected 50.4
- ESPN: day-to-day, ESPN est. 20 Nov (Right Knee Soreness, updated 2026-11-19)
- **Minutes:** 40.7 min over his last 3 games against 35.0 for the season (+5.7)
- News (19 Nov): Cunningham (knee) is expected to play in Friday's game against the Raptors, Blake Murphy of Sportsnet.ca reports.
- News (18 Nov): Cunningham (knee) won't play in Wednesday's game against New Orleans.
- **Research:**
  - He is **Probable for Fri 20 Nov vs TOR** on the NBA report of 19 Nov 10:45 PM ([PDF](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)). He is "expected to play" per Blake Murphy of Sportsnet via [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/cade-cunningham-injury-expected-to-play-friday-540045). Bickerstaff called the 18 Nov absence mainly precautionary and the injury not serious, per [Detroit News (Coty M. Davis) via Yahoo, 19 Nov](https://sports.yahoo.com/articles/cunningham-less-pistons-end-road-033244487.html). ESPN's 20 Nov is right.
  - The figure is inflated by the **48-minute double-overtime game** against WSH on 12 Nov ([ESPN recap](https://africa.espn.com/nba/recap/_/gameId/401909977)). His regulation games since were 36 and 38 minutes. The soreness began after his ~38 minutes at SA on 17 Nov, per [Heavy (Erik C. Anderson), 19 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-raptors/). The rotation is thin: Duren, Duncan Robinson (left quad strain), Holland (left knee bone bruise), Okorie and Prince are all out on the NBA report.
  - Verdict: ESPN confirmed.

### Daniss Jenkins (DET, PG, us)

- Rate **33.8** · role rate 37.8 · season 30.5 (14) · L7 36.5 (4) · L15 38.0 (7) · L30 30.5 (14)
- ESPN: active
- **Minutes:** 36.3 min over his last 3 games against 29.3 for the season (+7.0)
- News (19 Nov): Jenkins amassed 17 points (7-16 FG, 3-5 3Pt), four rebounds and nine assists over 36 minutes during Wednesday's 122-109 win over New Orleans.
- News (18 Nov): Jenkins closed Tuesday's 105-93 win over the Spurs with 25 points (11-21 FG, 3-7 3Pt), five rebounds, five assists and one steal over 38 minutes.
- **Research:**
  - Ongoing starting role. Jenkins started in place of Paul Reed from 9 Nov, and Rotoworld (NBC Sports, 18 Nov) writes that he "should remain a starter until Jalen Duren returns" from his hamstring strain ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/pistons-start-daniss-kevin-green-ausar-collins)). RotoWire says he is "performing well enough to lock down that role as long as he stays healthy" ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-hands-nine-assists-in-win/)).
  - **Jalen Duren** (right hamstring strain) is re-evaluated about Sun 22 Nov. The Pistons said on 8 Nov that he would be re-evaluated in two more weeks ([Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)). ESPN est.: 24 Nov.
  - **Duncan Robinson** (left quad strain) is out at least a week, with a re-evaluation about 23–24 Nov ([Detroit Sports Nation citing The Detroit News, 17 Nov](https://detroitsportsnation.com/duncan-robinson-injury-pistons-espn-first-month/gkaplan/detroit-pistons/11/17/2026/508470/)). ESPN est.: 27 Nov.
  - Verdict: *ESPN confirmed* (active, starting). The existing override (role 35 until 2026-11-22) holds. Below it is refreshed with the newer source. Re-check on 22 Nov after Duren's re-evaluation.

### Yves Missi (NO, C, us)

- Rate **27.6** · season 32.0 (5) · L7 25.7 (3) · L15 25.7 (3) · L30 32.0 (5) · projected 24.7
- ESPN: active
- **Minutes:** news on 15 Nov: "He was placed on a minutes restriction, limiting him to just 22 minutes of playing time."
- News (15 Nov): Missi notched three points (1-4 FG, 1-4 FT), eight rebounds, one assist and four blocks over 22 minutes during Saturday's 116-108 loss to the Nuggets.
- News (14 Nov): Missi (knee) will be available for Saturday's game against Denver, Jim Eichenhofer of the Pelicans' official site reports.
- **Research:**
  - **The restriction is still in place.** He returned on 14 Nov under a minutes restriction, per Rod Walker of the Times-Picayune ([RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-blocks-four-shots-in-return-539214); [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/yves-missi-knee-will-play-on-minutes-restriction)). He played 22 min on 14 Nov and 23 min on 16 Nov ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/yves-missi-produces-14-rebounds-three-steals)). ClutchPoints (19 Nov) still describes him as "currently on a minutes restriction". It also warns against pushing him in the Pelicans' road back-to-back at OKC and SA ([ClutchPoints, 19 Nov](https://clutchpoints.com/nba/new-orleans-pelicans/shorthanded-pelicans-prioritize-7-games-before-christmas-day)). That warning is the writer's opinion, not a team statement. No source gives a date for lifting the restriction.
  - **The 17 min on 18 Nov came from foul trouble, not a tighter cap.** He picked up two early fouls and sat much of the first half ([Pelicans On SI via Yahoo, 19 Nov](https://sports.yahoo.com/articles/jamahl-mosley-gets-f-pelicans-170006841.html)).
  - Verdict: *ESPN confirmed* (active). The restriction of about 22 min is still in place, with no date to lift it.

### Jalen Smith (CHI, PF/C, us)

- Rate **42.2** · season 36.1 (13) → 38.3 (12) · L7 45.7 (3) · L15 40.7 (6) → 46.8 (5) · L30 36.1 (13) → 38.3 (12) · projected 22.4
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 13–14 Nov back-to-back, playing the games either side
- News (19 Nov): Smith recorded 14 points (6-11 FG, 2-5 3Pt), six rebounds, three assists and one steal in 21 minutes during Wednesday's 137-107 win over the Nets.
- News (17 Nov): Smith (head) isn't listed on the injury report for Wednesday's game against Brooklyn.
- **Research:**
  - **The 14 Nov absence was an injury, not rest.** He missed Sat 14 Nov @MIN with a sprained finger and was "back from a one-game absence due to a sprained finger" on 16 Nov ([CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-will-play-monday-539454/)).
  - **Status now:** he left the 16 Nov game in the fourth quarter after a collision ([CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-doesnt-return-to-mondays-loss/)). ESPN's news feed (RotoWire, 17 Nov) adds that he told Joel Lorenzi of The Athletic he was fine. He played on 18 Nov, his 21 min cut short by a 30-point blowout ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-offensive-glass-fuels-solid-outing/)). He is not on the NBA's official report for Fri 20 vs WSH.
  - Verdict: *ESPN confirmed* (active). The rest flag rests on an injury absence. Expect him on both nights, 22 and 23 Nov.

### Paul George (BOS, SF/PF, us)

- Rate **36.3** · season 40.2 (13) · L7 32.0 (3) · L15 36.7 (7) · L30 40.2 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side
- News (19 Nov): George supplied 10 points (3-12 FG, 1-7 3Pt, 3-3 FT), four rebounds, one assist, one block and three steals across 23 minutes before fouling out of Wednesday's 105-101 loss to Denver.
- News (14 Nov): George (illness) isn't listed on the injury report for Sunday's game against Dallas, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - **His pattern says he sits Sun 22.** MassLive (18 Nov) reports he has played both games of a back-to-back only twice. "In the other two back-to-backs, both on the road, he sat out the second game" ([MassLive via Yahoo, 18 Nov](https://sports.yahoo.com/articles/paul-george-delivers-good-news-110100607.html)). The box scores agree:
  - He sat 2 Nov @HOU, listed as rest: "PG will sit this one out" ([NBC Sports, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)).
  - He sat 11 Nov @TOR, listed as illness ([NBA official injury report, 11 Nov, 5 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_00PM.pdf)). MassLive still counts it among his back-to-back sits.
  - Verdict: *nothing new found*. ESPN shows him active. No team or beat-writer statement exists yet, so the brief allows no `sit` row. Plan as if he misses Sun 22 @GS: he sat the second night of both earlier road back-to-backs. Expect him to play Sat 21 @SAC. Re-check the Celtics' Sun 22 report, usually out the afternoon before.

## Free agents and waivers

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 25 Nov (Right Knee Dislocated, updated 2026-11-18)
- **Injury:** ESPN est. 25 Nov (Out, Right Knee Dislocated, updated 18 Nov), but the news said on 18 Nov: "He should be considered week-to-week moving forward."
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- News (14 Nov): Raynaud (knee) has been ruled out for Sunday's game against the Thunder.
- **Research:**
  - Verdict: *ESPN confirmed* (as a floor; no team timetable).

### Robert Williams III (POR, C, free agent)

- Rate **23.2** · season 24.4 (12) · L7 19.7 (3) · L15 25.1 (7) · L30 24.4 (12) · projected 26.9
- ESPN: out, ESPN est. 21 Nov (Rest, updated 2026-11-18)
- **Injury:** ESPN est. 21 Nov (Out, Rest, updated 18 Nov), but the news said on 17 Nov: "For the season, Williams has averaged 6.5 points, 6.5 rebounds and 1.1 blocks per contest in 11 games while shooting 63.3 percent from the floor."
- News (18 Nov): Williams (rest) is listed as out for Thursday's game versus the Bucks.
- News (18 Nov): Williams chipped in six points (2-2 FG, 2-2 FT), eight rebounds and four assists across 16 minutes during Tuesday's 106-105 loss to Minnesota.
- **Research:**
  - Verdict: *ESPN confirmed*.

### Scotty Pippen Jr. (MEM, PG/SG, free agent)

- Rate **16.3** · season 14.2 (5) · L7 — · L15 — · L30 14.2 (5) · projected 30.6
- ESPN: out, ESPN est. 25 Nov (Back Soreness, updated 2026-11-16)
- **Injury:** ESPN est. 25 Nov (Out, Back Soreness, updated 16 Nov), but the news said on 16 Nov: "Pippen (back) is progressing in his recovery but is still considered week-to-week."
- News (16 Nov): Pippen (back) is progressing in his recovery but is still considered week-to-week.
- News (10 Nov): Pippen (back) remains out for Wednesday's game against Denver, Michael Wallace of the Grizzlies' official site reports.
- **Research:**
  - Verdict: *ESPN confirmed* (week-to-week, no timetable; the sourced floor is 23 Nov).

### Jalen Suggs (ORL, PG/SG, free agent)

- Rate **35.8** · season 26.7 (6) → 31.2 (5) · L7 27.0 (3) → 38.5 (2) · L15 27.0 (3) → 38.5 (2) · L30 26.7 (6) → 31.2 (5) · projected 29.2
- ESPN: active
- **Role:** news on 16 Nov: "Suggs will start Monday's game against the Celtics."
- **Minutes:** news on 17 Nov: "His presence is key for the Magic, meaning his playing time should continue to ramp up over the next few games."
- News (19 Nov): Suggs registered 18 points (5-10 FG, 5-6 3Pt, 3-6 FT), eight rebounds, four assists, one block and two steals over 31 minutes during Wednesday's 121-116 loss to the 76ers.
- News (17 Nov): Suggs accumulated 12 points (5-8 FG, 2-4 3Pt), six rebounds, four assists and two blocks across 25 minutes during Monday's 115-105 win over the Celtics.
- **Research:**
  - He is **not on Orlando's injury report** for Fri @ BKN. The Magic list four players out: Penda, Isaac, Banchero and Nelson ([iHeart / NBA report, 20 Nov](https://957wdae.iheart.com/content/2026-11-20-magic-vs-nets-injury-report-nov-20/)).
  - **Paolo Banchero** is still out, which keeps Suggs's usage up. Banchero has a low-grade right high ankle sprain (since about 23 Oct), reported as several weeks with no formal timetable ([TSN, Oct](https://www.tsn.ca/nba/article/report-magics-banchero-out-multiple-weeks-with-low-grade-high-ankle-sprain-n1-50266620/)). He is out Friday. *ESPN est. 29 Nov.*
  - "His playing time should continue to ramp up over the next few games." ([RotoWire, 17 Nov, via CBS player page](https://www.cbssports.com/nba/players/3177410/jalen-suggs/))
  - Verdict: ESPN confirmed (active). Our override is stale. The 25-minute row gives a role rate of about 25.0 (season FP/min 1.00), well under what he is now playing.

### Quentin Grimes (LAL, SG/SF, free agent)

- Rate **35.2** · role rate 30.8 · season 24.0 (14) · L7 51.0 (3) · L15 31.8 (6) · L30 24.0 (14) · projected 28.1
- ESPN: active
- **Role:** started 2 of his last 2 games after 3 of 12 before; 36.8 min in his starts, against 28.6 for the season
- **Role:** news on 15 Nov: "Grimes will start in Sunday's game versus the Suns, Law Murray of The Athletic reports."
- **Minutes:** 38.0 min over his last 3 games against 28.6 for the season (+9.4)
- News (19 Nov): Grimes ended with 20 points (8-20 FG, 4-10 3Pt), seven rebounds and four assists over 35 minutes during Wednesday's 109-97 loss to Utah.
- News (18 Nov): Grimes closed with 47 points (16-24 FG, 10-14 3Pt, 5-6 FT), six rebounds, three assists and one steal across 42 minutes during Tuesday's 118-114 overtime win over the Hornets.
- **Research:**
  - "Grimes is expected to remain in the starting lineup while Reaves is out." ([RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/austin-reaves-injury-still-out-friday-540088))
  - On Wednesday, Redick said Reaves's workout went "well," but he had no insight into his availability beyond that night. Grimes is listed **available** for Friday despite the splint on his right finger. ([Heavy, 19 Nov, 8:16 PM](https://heavy.com/sports/nba/los-angeles-lakers/lakers-austin-reaves-injury-kings-update/))
  - **What ends it:** Reaves's return, Mon 23 Nov at the earliest. After that, his usage "won't be the same," and he becomes a points-and-threes streamer only. ([NBC Sports, 19 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-19/quentin-grimes-puts-up-20-7-4-in-loss-to-the-jazz))
  - Verdict: ESPN confirmed (active). The starting role is confirmed for Fri 20 Nov.

### Mo Bamba (UTAH, C, waivers)

- Rate **34.3** · role rate 44.6 · season 31.1 (12) · L7 42.8 (4) · L15 33.1 (8) · L30 31.1 (12)
- ESPN: active
- **Role:** started 2 of his last 2 games after 1 of 10 before; 30.0 min in his starts, against 20.9 for the season
- **Role:** news on 15 Nov: "Bamba will start in Sunday's game against San Antonio."
- **Minutes:** 30.0 min over his last 3 games against 20.9 for the season (+9.1)
- News (18 Nov): Bamba had 15 points (6-7 FG, 1-2 3Pt, 2-2 FT), 10 rebounds, three assists and one block across 31 minutes during Tuesday's 132-107 victory over the Clippers.
- News (15 Nov): Bamba recorded 26 points (10-13 FG, 6-6 3Pt, 0-3 FT), five rebounds, four assists, two steals and a block in 35 minutes during Sunday's 110-102 loss to the Spurs.
- **Research:**
  - Verdict: *ESPN corrected*. The 30-minute role and the 44.6 role rate are out of date since Hayes returned on 18 Nov. The ongoing role is about 20 minutes, shared with Hayes.

### Aday Mara (OKC, C, free agent)

- Rate **31.4** · season 27.1 (15) · L7 34.3 (3) · L15 33.1 (8) · L30 27.1 (15)
- ESPN: active
- **Role:** news on 18 Nov: "Mara will start in Wednesday's game versus Atlanta."
- News (18 Nov): Mara will start in Wednesday's game versus Atlanta.
- News (16 Nov): Mara closed with 16 points (8-11 FG), 13 rebounds and three assists across 26 minutes off the bench during Sunday's 125-103 win over Sacramento.
- **Research:**
  - On 18 Nov vs ATL he started in place of Kenrich Williams ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/aday-mara-records-10-points-eight-assists)). The starters were Gilgeous-Alexander, Ajay Mitchell, McCain, Mara and Hartenstein ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/thunder-to-start-shai-ajay-mccain-mara-i-hart)).
  - The center minutes stay open while **Chet Holmgren** is out. Holmgren has a small right patellar tendon tear; the Thunder said 8–10 weeks, with an expected return in January ([CBS Sports, 31 Oct](https://www.cbssports.com/nba/news/chet-holmgren-injury-how-can-thunder-survive-trade-rumors/)). *ESPN est. 2 Jan 2027.*
  - Verdict: Nothing new found. ESPN lists him active, and no source reports the starting role as ongoing.

### Tyrese Proctor (CLE, SG, free agent)

- Rate **28.8** · role rate 31.2 · season 22.6 (15) · L7 39.5 (4) · L15 27.7 (9) · L30 22.6 (15)
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 27.8 min in his starts, against 20.3 for the season
- **Minutes:** 29.7 min over his last 3 games against 20.3 for the season (+9.3)
- News (17 Nov): Proctor had 17 points (6-13 FG, 2-6 3Pt, 3-5 FT), three rebounds, two assists, two steals and one block over 29 minutes during Monday's 126-115 victory over the Bulls.
- News (14 Nov): Proctor posted 24 points (10-19 FG, 4-13 3Pt), 11 rebounds and 10 assists across 34 minutes during Saturday's 127-117 win over Dallas.
- **Research:**
  - **Jaylon Tyson** (right ankle) is out again Fri vs IND, his third straight miss ([NBC Sports / NBA report, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/jaylon-tyson-ankle-remains-out-friday-vs-pacers)). No timetable reported. *ESPN est. 23 Nov.*
  - "Tyrese Proctor should continue to log additional minutes while Tyson is out" ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylon-tyson-ankle-out-wednesday-vs-grizzlies)). "He'll likely head back to the bench when Tyson returns" ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/tyrese-proctor-scores-17-points-as-starter)). **Tyson's return ends the role.**
  - **Evan Mobley** has a great-toe sprain confirmed by MRI and will be re-evaluated in 7–10 days ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)). *ESPN est. 29 Nov.*
  - Verdict: ESPN confirmed (active). The starting role is confirmed for Fri 20 Nov, his only game in the window. His role rate at 27 minutes is about 30.4, against a rate of 28.8.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **28.6** · role rate 29.7 · season 26.8 (13) · L7 27.5 (2) · L15 31.6 (5) · L30 26.8 (13) · projected 26.6
- ESPN: out, ESPN est. 23 Nov (Concussion, updated 2026-11-19)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- **Role:** news on 15 Nov: "Allen is not listed in the starting lineup for Sunday's game against the Clippers, Tomer Azarly of ClutchPoints.com reports."
- News (19 Nov): Allen (concussion) has been ruled out for Friday's game against Atlanta.
- News (17 Nov): Allen (concussion-like symptoms) has been ruled out for Tuesday's game against the Lakers.
- **Research:**
  - Verdict: *nothing new found* on the role. ESPN's "Out" listing is confirmed, and its 23 Nov date is an unsupported placeholder.

### Jaylon Tyson (CLE, SG/SF, free agent)

- Rate **23.1** · role rate 25.8 · season 19.2 (8) · L7 28.0 (2) · L15 20.3 (3) · L30 19.2 (8) · projected 25.6
- ESPN: out, ESPN est. 23 Nov (Right Ankle, updated 2026-11-19)
- **Role:** started 2 of his last 2 games after 0 of 6 before; 32.0 min in his starts, against 23.9 for the season
- **Minutes:** 29.0 min over his last 3 games against 23.9 for the season (+5.1)
- News (19 Nov): Tyson (ankle) has been ruled out for Friday's game against Indiana.
- News (18 Nov): Tyson (ankle) has been ruled out for Wednesday's game against Memphis.
- **Research:**
  - **13 Nov @MIA:** he filled the spot of **Evan Mobley**, who was out (left great toe sprain). The Cavaliers said on 16 Nov that Mobley will be re-evaluated after 7 to 10 days of treatment, which means about 23–26 Nov ([Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)). *ESPN est.* 29 Nov.
  - **The spot has moved on since he got hurt.** Tyrese Proctor started on 16 Nov. Mario Hezonja started on 18 Nov, with **Peyton Watson** out (low back contusion; questionable Fri 20 on the official report, no timetable reported; *ESPN est.* 20 Nov). NBA.com projects Harden, Mitchell, Proctor, Hezonja and Allen to start on Friday ([NBA.com Pacers preview, 19 Nov](https://www.nba.com/pacers/news/preview-pacers-cavaliers-261120)).
  - Verdict: ESPN confirmed. He is out, with no timetable reported. 23 Nov is the earliest supported date.

### Kasparas Jakucionis (MIL, PG, free agent)

- Rate **28.7** · role rate 26.3 · season 20.4 (15) · L7 44.7 (3) · L15 22.4 (8) · L30 20.4 (15) · projected 20.2
- ESPN: active
- **Minutes:** 24.7 min over his last 3 games against 19.1 for the season (+5.5)
- News (19 Nov): Jakucionis produced 20 points (6-8 FG, 3-5 3Pt, 5-6 FT), three rebounds, five assists and two steals over 26 minutes during Wednesday's 137-130 loss to Miami.
- News (16 Nov): Jakucionis finished with 25 points (9-16 FG, 4-10 3Pt, 3-3 FT), five rebounds, five assists and three steals across 26 minutes off the bench during Sunday's 113-106 loss to Atlanta.
- **Research:**
  - **15 and 18 Nov:** Ryan Rollins was out with an illness. NBC Sports' minutes report says "Ryan Rollins has been out with an illness" and "Kasparas Jakučionis has picked up extra minutes off the bench" ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)). RotoWire tied the 25-point game to Rollins' absence too: "Sunday's opportunity came with Ryan Rollins (illness) unavailable" (RotoWire in ESPN's feed, 16 Nov).
  - **19 Nov vs POR:** Rollins was back and played 21 min. Jakucionis still got 22 min (18 pts), but **Kyle Kuzma** and **Myles Turner** sat the second night of the back-to-back with shoulder contusions ([Bucks On SI, 19 Nov](https://www.si.com/nba/bucks/onsi/bucks-will-have-new-look-lineup-as-lillard-returns-to-town-with-blazers-preview-starters-injuries-how-to-watch-01m7ty7gkrqg); [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/kyle-kuzma-shoulder-out-thursday-vs-portland); [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910020)). For both, no timetable is reported; *ESPN est.* 21 Nov.
  - **With the full roster, his role has been unstable.** He played 4 min on 11 Nov and was a DNP-CD on 13 Nov @ORL. Behind the Buck Pass calls his minutes ones that "change constantly" ([15 Nov](https://behindthebuckpass.com/bucks-risk-stunting-kasparas-jakucionis-growth-rapid-rotation-changes)).
  - Verdict: nothing new found. ESPN's "active" is right. The minutes gain was circumstantial, and no source reports an ongoing role.

### Caleb Wilson (CHI, SF, free agent)

- Rate **28.0** · role rate 26.1 · season 34.9 (10) · L7 — · L15 17.7 (3) · L30 34.9 (10) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - **4 Nov:** 22 min in a 30-point loss at NY ([ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401909926)).
  - **11 Nov vs SA:** 15 min ([ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401909969)). He left in the third quarter with the hand fracture (K.C. Johnson, Chicago Sports Network, via RotoWire in ESPN's feed, 12 Nov).
  - The Bulls' release (12 Nov) says the surgery went well and he "will be re-evaluated in three weeks" ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)).
  - Verdict: ESPN confirmed.

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **27.6** · role rate 23.4 · season 28.2 (15) · L7 24.8 (4) · L15 29.8 (8) · L30 28.2 (15) · projected 26.9
- ESPN: active
- **Minutes:** 25.3 min over his last 3 games against 30.9 for the season (−5.6)
- News (19 Nov): Washington posted 21 points (7-10 FG, 5-7 3Pt, 2-2 FT), five rebounds, two assists, three blocks and one steal over 25 minutes during Wednesday's 116-94 win over the Warriors.
- News (13 Nov): Washington accumulated 10 points (4-7 FG, 1-4 3Pt, 1-1 FT) and three rebounds over 16 minutes during Thursday's 133-94 loss to Minnesota.
- **Research:**
  - **He still starts every game.** ESPN box scores show him in the starting five in all of his last 6 games, including 18 Nov vs GS. NBC's minutes report says he "played 27 minutes off the bench" on 18 Nov ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)). The box score contradicts that: he started and played 25 min ([ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910016)).
  - Verdict: nothing new found. He is active and starting. The drop comes from game script, and no role change is reported.

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **27.2** · role rate 24.0 · season 30.6 (9) · L7 — · L15 20.8 (5) · L30 30.6 (9) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - **Latest report: out again for Fri 20 Nov @OKC.** The NBA's official report of 19 Nov 10:45 PM lists "Left Ankle Sprain" ([PDF](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)). That makes five straight absences (13, 14, 16, 18 and 20 Nov). He does not appear in the box scores at all, not even as a DNP.
  - NBC Sports' minutes report (19 Nov) says: "Dejounte Murray has demanded a trade and won't play until that demand is satisfied" ([via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - That matches Charania on 13 Nov: he "will NOT play another minute for the New Orleans Pelicans" ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)).
  - Verdict: ESPN confirmed. ESPN's 27 Nov date holds as a floor. Replace the stale CSV row.

### T.J. McConnell (IND, PG, free agent)

- Rate **25.1** · season 22.5 (6) · L7 29.7 (3) · L15 22.5 (6) · L30 22.5 (6) · projected 24.4
- ESPN: day-to-day, ESPN est. 20 Nov (Right Hamstring Strain, updated 2026-11-19)
- **Minutes:** news on 17 Nov: "McConnell's minutes have been steadily ramping up since he made his regular-season debut Nov. 7, and he had his best game yet in Sunday's 131-124 loss to the 76ers, finishing with 12 points, five rebounds, five assists and one steal in 19 minutes off the bench."
- News (19 Nov): McConnell (hamstring) is listed as probable for Friday's game in Cleveland.
- News (18 Nov): McConnell recorded 14 points (7-10 FG), five assists, two rebounds and two steals over 18 minutes during the Packers' 119-104 loss to the Rockets on Wednesday.
- **Research:**
  - RotoWire said on 18 Nov that he "will likely continue operating under a minutes restriction", with no number given ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-cleared-for-action-wednesday/)).
  - Nembhard has a left hip sprain and is **questionable** for Fri 20. Carlisle said he "wouldn't be out long" ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-could-miss-another-game-friday/)) and "hopes he'll be ready" ([NBA.com, 19 Nov](https://www.nba.com/pacers/news/preview-pacers-cavaliers-261120)). *ESPN est.* 20 Nov.
  - RotoWire wrote that McConnell's "role would shrink" if Nembhard is cleared ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-chips-in-14-points-vs-houston/)). NBC agrees he "figures to see more action as long as Nembhard is out" ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - Verdict: ESPN confirmed. He is probable on Friday. His role grows only while Nembhard sits, at about 18 min.

### Precious Achiuwa (SAC, PF/C, free agent)

- Rate **13.5** · role rate 19.8 · season 25.4 (12) · L7 -3.0 (1) · L15 15.8 (5) · L30 25.4 (12) · projected 24.1
- ESPN: day-to-day, ESPN est. 20 Nov (Left Lower Leg Bruise, updated 2026-11-20)
- **Minutes:** 19.3 min over his last 3 games against 24.8 for the season (−5.5)
- News (19 Nov): Achiuwa is doubtful for Friday's game against the Lakers due to a left lower leg bruise.
- News (18 Nov): Achiuwa (lower leg) is available for Wednesday's game against the Suns.
- **Research:**
  - **10 Nov vs ORL:** his 14 min were an injury exit; he left with the leg contusion ([CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/kings-precious-achiuwa-exits-game-with-leg-contusion/)).
  - **18 Nov vs PHX:** Keegan Murray and Sabonis started ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/sac-starts-acuff-lavine-hunter-murray-sabonis)), and Achiuwa played 8 min off the bench ([ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910018)).
  - NBC's minutes report: "Precious Achiuwa has seemingly fallen out of the rotation and played eight minutes on Wednesday" ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - Verdict: ESPN corrected (minutes). ESPN's day-to-day label is right, and its 20 Nov date is likely a day early, given the doubtful tag. The low minutes are a role cut, not only the bruise. Plan him out on Friday.

### Neemias Queta (BOS, C, free agent)

- Rate **32.1** · season 27.3 (14) · L7 38.0 (2) · L15 30.4 (7) · L30 27.3 (14) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "Back in action after getting a breather Monday in the second half of a back-to-back, Queta delivered his second double-double of the season while setting a new season-high scoring mark."; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- News (17 Nov): Queta (rest) is available for Wednesday's game against the Nuggets, Jack Simone of BostonSportsJournal.com reports.
- **Research:**
  - He rested on the second night of the 15–16 Nov home back-to-back, according to Taylor Snow of the Celtics' official site ([RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/neemias-queta-news-sitting-out-monday-539449)). Heavy called it "load management, not a new injury" and noted it was Boston's third back-to-back of November ([Heavy, 16 Nov](https://heavy.com/sports/nba/boston-celtics/neemias-queta-injury-update-celtics-streak/)).
  - Verdict: Nothing new found. ESPN lists him active.

### Ja Morant (POR, PG, free agent)

- Rate **34.1** · season 33.8 (4) · L7 — · L15 — · L30 33.8 (4) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:**
  - Team statement (30 Oct): "Imaging revealed a grade two left hamstring strain. Morant will be re-evaluated in four weeks." [nba.com/blazers, 30 Oct](https://www.nba.com/blazers/news/ja-morant-injury-update). Four weeks from 30 Oct is about 27 Nov.
  - Coach Micah Nori (7 Nov): a Los Angeles doctor gave a positive outlook, and Morant "may not be out for as long as we thought." Nori did not change the timetable, and the re-evaluation is still set for late November ([Yahoo/Heavy, 8 Nov](https://sports.yahoo.com/articles/trail-blazers-announce-encouraging-ja-045805609.html); [NBC Sports, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/nori-morant-could-be-back-sooner-than-expected)). The latest item found is Donovan Clingan saying Morant has "been working hard" (Heavy, 11 Nov), with no new timeline ([Heavy, 11 Nov](https://heavy.com/sports/nba/portland-trail-blazers/good-ja-morant-news-amid-injury-recovery/)). No on-court work or practice has been reported.
  - Verdict: - Verdict: ESPN corrected (slightly late against the team's own re-evaluation date).

## Opponents: this week and next

### Jaylen Brown (PHI, SG/SF, Snow Time Lakers)

- Rate **42.4** · season 40.8 (14) · L7 43.7 (3) · L15 41.9 (7) · L30 40.8 (14) · projected 38.6
- ESPN: out, ESPN est. 23 Nov (Left Hamstring, updated 2026-11-18)
- **Injury:** ESPN est. 23 Nov (Out, Left Hamstring, updated 18 Nov), but the news said on 18 Nov: "Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com."
- News (18 Nov): Brown (hamstring) will be re-evaluated at some point this weekend, per Kris Rihm of ESPN.com.
- News (17 Nov): Brown is out for Wednesday's game against the Magic with a left hamstring strain.
- **Research:**
  - Brown was ruled out for Wed 18 Nov at ORL with a left hamstring strain. A source told ESPN's Kris Rhim that he "will be re-evaluated ahead of Saturday's home game against the Milwaukee Bucks." The re-evaluation "does not guarantee Brown will return Saturday" ([Heavy via Yahoo, 17 Nov ET / 18 Nov 01:39 UTC](https://sports.yahoo.com/articles/espn-insider-drops-latest-jaylen-013927700.html)). Rhim repeated this on NBA Today: re-evaluated "this weekend ahead of the Sixers game against the Milwaukee Bucks", and the exact timeline will be set after that. "Brown didn't sound too concerned after the game, but of course things can change" ([BasketNews, 18 Nov](https://basketnews.com/news-259795-76ers-earn-massive-jaylen-brown-update-amid-troubling-hamstring-injury.html)).
  - Nick Nurse said in Orlando that Brown would be re-evaluated once the team got back to Philadelphia ([NBC Sports Philadelphia, 18 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-magic-live-updates-lebron-james-joel-embiid-tyrese-maxey/767473/)). Nurse called the absences "an abundance of caution", not injuries that kept them from playing. OnSI notes Brown has had four full days off and argues Nurse could still hold him out Saturday ([SI / All 76ers, ~19 Nov](https://www.si.com/nba/76ers/onsi/76ers-injury-situation-is-already-looking-up-in-magic-win-aftermath-01m7t920zvk4)). The opposite reading is in ESPN's own news blurb (18 Nov): the 76ers are "bracing for Brown ... to be sidelined for multiple games." No MRI result has been published. No newer report was found as of Thursday night ET. The first injury report for the Saturday game should come out Friday evening ET ([Northeast Times, 19 Nov](https://northeasttimes.com/2026/11/19/sixers-injury-report-maxey-brown-next-three-games-november-2026/), seen in search results only; the page returned 403).
  - Verdict: ESPN confirmed. The 23 Nov estimate matches the reported weekend re-evaluation. Applying the brief's rule (day after the re-evaluation, about 22 Nov) gives the same first game, Mon 23, because PHI does not play Sun 22. Matchup risk this week: he could play Sat 21 if cleared. Check Friday evening's report. Teammate Tyrese Maxey (right foot soreness, late scratch 18 Nov; no timetable reported, day-to-day) — *ESPN est.* 21 Nov.

### Brandin Podziemski (GS, PG/SG, Matt Wright's Foxies)

- Rate **28.0** · season 33.1 (14) · L7 20.5 (4) · L15 30.6 (8) · L30 33.1 (14) · projected 30.8
- ESPN: active
- **Minutes:** news on 19 Nov: "His consistent offensive involvement provides fantasy appeal, though poor shooting and fluctuating minutes limit his reliability."
- News (19 Nov): Podziemski accumulated 10 points (5-13 FG, 0-5 3Pt, 0-2 FT), three rebounds and four assists over 29 minutes during Wednesday's 116-94 loss to the Mavericks.
- News (17 Nov): Podziemski recorded 15 points (3-8 FG, 3-7 3Pt, 6-7 FT), six rebounds, three assists, one steal and two blocks across 30 minutes in Monday's 115-94 loss to the Pelicans.
- **Research:**
  - 22 min, 2-10 FG, −24 in the 13 Nov NBA Cup loss at SAS, a blowout ([NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/brandin-podziemski-limited-to-eight-points-friday)).
  - 29 min in the 22-point loss at DAL on 18 Nov ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-goes-cold-from-deep-in-dallas/)).
  - 31:40 in the 126-98 loss at MEM on 19 Nov (15 pts, 5-12 FG, 0-5 3PT, −27) ([Covers box score, 19 Nov](https://www.covers.com/sport/basketball/nba/matchup/388758)). He started at DAL and was listed first among GS players at MEM.
  - Verdict: nothing new found (no role or minutes change; ESPN's "active" stands).

### Brandon Miller (CHA, SG/SF, Matt Wright's Foxies)

- Rate **24.6** · role rate 22.6 · season 29.5 (12) · L7 24.5 (2) · L15 15.8 (4) · L30 29.5 (12) · projected 37.4
- ESPN: active
- **Minutes:** 23.3 min over his last 3 games against 30.5 for the season (−7.2)
- News (18 Nov): Miller amassed 28 points (10-19 FG, 5-12 3Pt, 3-3 FT), two rebounds, four assists and one block in 32 minutes during Tuesday's 118-114 overtime loss to the Lakers.
- News (16 Nov): Miller finished Sunday's 113-105 loss to the Clippers with five points (1-10 FG, 1-6 3Pt, 2-3 FT), four assists, two rebounds and one steal over 24 minutes.
- **Research:**
  - 14 min on 6 Nov: left in the second quarter vs BOS with right groin soreness ([Hoops Rumors, 7 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-injuries-miller-knueppel-williams-offseason.html)).
  - **The restriction is ongoing.** Charles Lee kept Miller (and Coby White) out of overtime on 17 Nov because of it: "as they've been coming back from injury, we've been trying to build them up ... being mindful of where they are." Lee also said "we have a big picture in mind and it's a long year" ([Fadeaway World via Yahoo, 18 Nov](https://sports.yahoo.com/articles/hornets-coach-explains-why-brandon-104117242.html)). SI confirms the minutes-restriction reason and that no cap or end date was given ([SI, 19 Nov](https://www.si.com/nba/hornets-bizarre-decision-rest-starters-ot-nba-injury-problem)). ClutchPoints: "still on minutes restrictions" ([ClutchPoints, 18 Nov](https://clutchpoints.com/nba/charlotte-hornets/hornets-news-why-didnt-brandon-miller-coby-white-play-ot-lakers-collapse)).
  - **Will it last?** His minutes are climbing (24, then 32 in regulation), and the cap is loosening. Expect about 32 min, rising toward his healthy ~33 to 36 (36 to 38 in late October). Blowouts are a risk: CHA had lost 8 of 9 before 17 Nov. With Kon Knueppel out (hamstring; "will miss another four weeks" per [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-deliver-devastating-kon-knueppel-224941481.html) — *ESPN est.* 12 Dec), Miller stays CHA's focal scorer. Nothing was found about his status for Fri 20 Nov at ATL; he is not on any report seen.
  - Verdict: ESPN corrected (minutes). ESPN's "active" is right, but the low minutes come from a reported, loosening restriction after the groin/hip injury, not a role cut. He played 32 min in his second game back.

### Cooper Flagg (DAL, SF/PF, Matt Wright's Foxies)

- Rate **46.8** · season 51.0 (14) · L7 40.5 (4) · L15 50.8 (8) · L30 51.0 (14) · projected 45.4
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; sat the second night of the 23–24 Oct back-to-back, playing the games either side
- News (19 Nov): Flagg chipped in 33 points (11-15 FG, 3-5 3Pt, 8-8 FT), five rebounds, nine assists and four steals across 34 minutes during Wednesday's 116-94 victory over the Warriors.
- News (16 Nov): Flagg contributed 17 points (5-15 FG, 2-6 3Pt, 5-5 FT), three rebounds, four assists, one block and one steal in 27 minutes during Sunday's 131-94 loss to the Celtics.
- **Research:**
  - **False positive.** He did not sit 24 Oct to rest. He sprained his left shoulder (mild sprain, MRI) on a Flagrant-1 foul by Aaron Nesmith on 23 Oct at IND, and was ruled out vs SAS the next night for that injury ([Heavy via Yahoo, 24 Oct](https://sports.yahoo.com/articles/dallas-mavericks-announce-concerning-injury-220756066.html)).
  - Since then he has **played the second night of both DAL back-to-backs**: 8–9 Nov (28 then 39 min, 86 FP) and 14–15 Nov at CLE then BOS (38 then 27 min). He played the Boston game while ill: "I try to play every game ... I'm always trying to play, no matter what. If I'm not feeling well or just an ankle, whatever it is" ([Dallas Sports Journal, 16 Nov](https://dallassportsjournal.com/cooper-flagg-new-england-maine-fans-back-to-back-celtics/)). The illness: "Flagg picked up an illness on the trip and wasn't feeling right for at least the final two games" ([Mavs.com, Eddie Sefko, 16 Nov](https://www.nba.com/mavs/news/flaggs-growing-leadership-skills-will-be-helpful-in-reversing-recent-trend)). No load-management plan has been reported, and he was not on the 19 Nov report.
  - Verdict: ESPN confirmed (active; no rest signal).

### Kyrie Irving (DAL, PG, Snow Time Lakers)

- Rate **43.0** · season 41.8 (12) · L7 45.3 (3) · L15 41.4 (7) · L30 41.8 (12) · projected 44.2
- ESPN: active
- **Rest:** back-to-back Sat 21–Sun 22 Nov; news on 19 Nov: "After sitting out the second game of a weekend back-to-back set, Irving returned to action and delivered decent numbers."; sat the second night of the 23–24 Oct back-to-back, playing the games either side; sat the second night of the 14–15 Nov back-to-back, playing the games either side
- News (19 Nov): Irving supplied 17 points (7-15 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists and two steals over 29 minutes during Wednesday's 116-94 win over Golden State.
- News (17 Nov): Irving (knee) is not listed on the injury report ahead of Wednesday's game against the Warriors.
- **Research:**
  - 24 Oct vs SA, "officially OUT due to rest" tied to "ongoing left knee injury management" ([ClutchPoints, 24 Oct](https://clutchpoints.com/nba/dallas-mavericks/mavericks-news-kyrie-irvings-status-spurs-game-up-in-air-cooper-flagg-injury)).
  - 15 Nov @BOS, "(left knee injury management) is unavailable" ([BasketNews, 15 Nov](https://basketnews.com/news-259537-why-kyrie-irving-will-not-play-vs-celtics-mavs-announce-huge-injury-update.html); [Dallas Morning News via Yahoo, 15 Nov](https://sports.yahoo.com/articles/kyrie-irving-sits-mavericks-vs-222607808.html)).
  - The one back-to-back he played in full was 8–9 Nov, both at home, after a 37-point blowout held him to 29 min ([Yardbarker, 10 Nov](https://www.yardbarker.com/nba/articles/kyrie_irving_explains_decision_to_play_mavericks_back_to_back_after_acl_tear/s1_17810_44540702)).
  - Verdict: *nothing new found*. ESPN shows him active. No `sit` row, because the team has not said. Plan for the opponent to be without Irving on Sun 22 @UTAH, the likelier outcome. Expect him to play Sat 21 vs LAC.

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.4** · season 40.1 (14) · L7 37.3 (3) · L15 44.4 (7) · L30 40.1 (14) · projected 41.1
- ESPN: active
- **Rest:** back-to-back Sun 22–Mon 23 Nov; news on 18 Nov: "He's been locked in over the past two games, totaling 55 points, five assists and four steals on 61.1 percent shooting from the field and 90.0 percent at the line, but despite his efforts, Indiana has suffered back-to-back losses."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (18 Nov): Siakam chipped in 24 points (10-17 FG, 2-2 3Pt, 2-2 FT), four rebounds, three assists, one block and three steals across 33 minutes during Wednesday's 119-104 loss to the Rockets.
- News (15 Nov): Siakam recorded 31 points (12-19 FG, 0-3 3Pt, 7-8 FT), two rebounds, two assists and one steal across 34 minutes during Sunday's 131-124 loss to Philadelphia.
- **Research:**
  - **Pattern: real but partial.** On 2 Nov 2026 he was ruled out on the day "due to rest" for the second night of IND's back-to-back vs ATL ([ClutchPoints via Yahoo, 2 Nov](https://sports.yahoo.com/articles/pacers-pascal-siakam-injury-vs-225410478.html); [ClutchPoints via Yahoo, 3 Nov](https://sports.yahoo.com/articles/pacers-down-7-players-vs-010520478.html): "given a rest day"; [NBC Sports, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/pascal-siakam-rest-removed-from-injury-report)). He did play the second night on 26 Oct 2026 (37 min).
  - Last season he also rested second nights: "Siakam will sit out the second leg of Indiana's back-to-back set" on 9 Nov 2025 ([CBS/RotoWire, 9 Nov 2025](https://www.cbssports.com/fantasy/basketball/news/pacers-pascal-siakam-resting-sunday)), and "Siakam will be sidelined for the second leg of the Indiana Pacers' back-to-back" on 17 Jan 2026 ([FantasyPros, 17 Jan 2026](https://www.fantasypros.com/nba/news/566128/pascal-siakam-rest-ruled-out-saturday.php)).
  - Context: Siakam is IND's main scorer while Tyrese Haliburton is out (left hamstring). Carlisle, 17 Nov: "There's no definite timeline on him ... I don't think it's out of the question [this month], but ... there's nothing happening in the near term" ([Yahoo, 17 Nov](https://sports.yahoo.com/articles/rick-carlisle-no-definite-timeline-174500355.html)) — *ESPN est.* 28 Nov.
  - Verdict: nothing new found. No team or beat word on sitting. There is a rest risk on Mon 23 and Sat 28: the 2 Nov 2026 rest day fits a habit from last season, but he played the 26 Oct second night.

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **25.9** · season 33.2 (11) · L7 12.0 (1) · L15 31.8 (5) · L30 33.2 (11) · projected 28.2
- ESPN: day-to-day, ESPN est. 20 Nov (Left Hip Soreness, updated 2026-11-19)
- **Rest:** back-to-back Sun 22–Mon 23 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (19 Nov): Nembhard (hip) is questionable for Friday's game in Cleveland.
- News (18 Nov): Nembhard (hip) won't play in Wednesday's game against the Rockets, Tony East of Forbes.com reports.
- **Research:**
  - Pacers game preview (NBA.com, 19 Nov): "Andrew Nembhard - questionable (left hip sprain)". He "was sidelined for the second straight game on Wednesday, though coach Rick Carlisle hopes he'll be ready to play in Friday's matchup." [nba.com/pacers, 19 Nov](https://www.nba.com/pacers/news/preview-pacers-cavaliers-261120)
  - Hoops Rumors (19 Nov): Carlisle "isn't planning for a long absence" and said Nembhard could return as soon as Friday. [hoopsrumors.com, 19 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-banchero-kawhi-pacers-edwards-grizzlies.html). RotoWire says the same: Carlisle "indicated that the 26-year-old wouldn't be out long." [rotowire.com, 19 Nov](https://www.rotowire.com/basketball/headlines/andrew-nembhard-injury-could-miss-another-game-friday-540057)
  - **25–26 Oct:** He sat 26 Oct at MIL with a neck/back injury picked up the night before against Brooklyn. Carlisle said it was a back issue. This was an injury absence, not a scheduled rest. Sources: [NBC Sports, 26 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/andrew-nembhard-neck-downgraded-to-out-monday) and [RotoWire, Oct](https://www.rotowire.com/basketball/headlines/andrew-nembhard-injury-out-vs-bucks-536206) (Dopirak, IndyStar).
  - Verdict: - Verdict: ESPN confirmed (DTD, questionable Fri 20 Nov). Rest flag: nothing new found, meaning no announced sit.

## Other rosters: injury flags only

### Jalen Brunson (NY, PG, Melbourne poopoo)

- Rate **46.2** · season 41.9 (15) · L7 50.0 (4) · L15 47.6 (8) · L30 41.9 (15) · projected 43.8
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 19 Nov: "Brunson exited to the locker room in the first quarter of Thursday's game against Minnesota due to an apparent facial injury, Jared Schwartz of the New York Post reports."
- News (19 Nov): Brunson (face) returned to Thursday's game against the Timberwolves with 2:47 remaining in the first quarter, per the broadcast.
- News (19 Nov): Brunson exited to the locker room in the first quarter of Thursday's game against Minnesota due to an apparent facial injury, Jared Schwartz of the New York Post reports.
- **Research:**
  - He took a hit to the face from LaMelo Ball and went to the locker room with 9:19 left in the 1st quarter ([Heavy, 19 Nov](https://heavy.com/sports/nba/new-york-knicks/jalen-brunson-injury-knicks-timberwolves-update/)). He came back into the game with 2:47 left in the 1st and "appears to be good to go for the remainder of the contest" ([CBS Sports/RotoWire, 19 Nov 8:32 PM ET](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-returns-thursday/)).
  - He finished the game: 21 pts (8-20 FG, 4 3PM), 2 reb, 7 ast, 2 stl in the 102-99 win, with 35 min per our log ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/jalen-brunson-has-21-points-four-threes-in-win); [Bleacher Report, 19 Nov](https://bleacherreport.com/articles/25535537-brunson-kat-carry-knicks-win-over-wolves-box-score-stats-highlights-lamelo-top-players)). No diagnosis or post-game medical update was found. Nothing points to a missed game.
  - Next games: "Brunson and the Knicks begin a home back-to-back against the Trail Blazers and Pacers on Saturday" (Sat 21 / Sun 22 Nov) ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/jalen-brunson-has-21-points-four-threes-in-win)). The same NBC page also noted he "did appear to be bothered by his left ankle" on 17 Nov at TOR. He did not miss time for it. Check the Knicks' Saturday injury report.
  - Verdict: - Verdict: ESPN confirmed (active, not on the injury feed).

### Brandon Ingram (LAC, SF/PF, Melbourne poopoo)

- Rate **36.5** · season — · L7 — · L15 — · L30 — · projected 38.5
- ESPN: out, ESPN est. 21 Nov (Right Achilles Surgery, updated 2026-11-18)
- **Injury:** ESPN est. 21 Nov (Out, Right Achilles Surgery, updated 18 Nov), but the news said on 18 Nov: "Ingram was cleared for full-contact work Nov. 6, and he's been playing 5-on-5 for the past couple of weeks."
- News (18 Nov): Ingram (heel/Achilles) will remain on the inactive list for Thursday's game in San Antonio.
- News (12 Nov): Ingram (Achilles) won't play in Friday's game against the Thunder, per Law Murray of The Athletic.
- **Research:**
  - Out again for 19 Nov at SAS. He was cleared for full contact on 6 Nov and has been playing 5-on-5 for about two weeks. Lue "was hopeful Ingram would make his Clippers debut" on the four-game road trip, "so ... there's a chance he could play Saturday in Dallas" ([RotoWire, 18 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-ruled-out-for-thursday-539822)). He is traveling with the team ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/brandon-ingram-achilles-out-thursday-vs-spurs)).
  - Lue's actual words (15 Nov, before the CHA game) were more cautious: "I hope but don't expect" that Ingram returns on the trip ([ClutchPoints, 15 Nov](https://clutchpoints.com/nba/los-angeles-clippers/clippers-brandon-ingram-injury-update-teases-return-coming-very-soon)). The trip runs 19 Nov at SAS to 25 Nov at MEM ([Hoops Rumors, 15 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-clippers-miller-barnes-nurkic-b-williams.html)). RotoBaller has the same: Lue "hopes Ingram can return before the trip ends Nov. 25, but doesn't expect that" ([RotoBaller, 15 Nov](https://www.rotoballer.com/player-news/brandon-ingram-close-to-returning/1994624)). Ingram himself has said "Whenever I feel ready" and gave no timeline ([NBC Sports, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/brandon-ingram-achilles-out-thursday-vs-spurs)).
  - Verdict: - Verdict: ESPN corrected (likely too early). The correction is soft: it rests on the coach's "hope but don't expect", not on a team timetable.

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **60.9** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 47.0 (2) → 65.0 (1) · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:**
  - Coach Sean Sweeney: "No timeline right now." Banchero is "doing good" and doing some on-court work, including shooting. It is unclear whether he is running. He has missed 12 straight games ([Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4); [Hoops Rumors, 19 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-banchero-kawhi-pacers-edwards-grizzlies.html)).
  - Banchero to Jason Beede (Orlando Sentinel): "I'm not playing right now so I don't know when. But hopefully within the next couple of weeks." He also said he does not want to rush it or let it "linger" ([Basketnews, 19 Nov](https://basketnews.com/news-259854-paolo-banchero-shares-major-update-on-his-recovery-from-ankle-injury.html); [RotoBaller, 19 Nov](https://www.rotoballer.com/player-news/paolo-banchero-ankle-targeting-return-within-a-couple-of-weeks/1997928)).
  - Verdict: - Verdict: ESPN confirmed (no contradiction; lean later).

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-20 03:47 UTC.
- [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/cade-cunningham-injury-expected-to-play-friday-540045)
- [AP via NBA.com, 9 Nov](https://www.nba.com/news/detroit-pistons-jalen-duren-two-weeks-hamstring)
- [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/myles-turner-injury-sidelined-by-left-shoulder-contusion-540024)
- [NBA injury report, 19 Nov 10:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_10_45PM.pdf)
- [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/austin-reaves-injury-still-out-friday-540088)
- [link](https://www.rotowire.com/basketball/headlines/cj-mccollum-news-leads-hawks-bench-with-21-points-538466)
- [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-2)
- [link](https://detroitsportsnation.com/jb-bickerstaff-jalen-duren-hamstring-update/gkaplan/detroit-pistons/11/08/2026/505901/)
- [link](https://sports.yahoo.com/articles/grizzlies-list-zach-edey-quinten-221551360.html)
- [link](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)
- [link](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-wont-play-monday/)
- [link](https://sports.yahoo.com/articles/pistons-vs-spurs-preview-no-165600772.html)
- [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/jalen-suggs-tallies-12-7-4-line-as-starter)
- [link](https://www.rotowire.com/basketball/headlines/trey-murphy-injury-another-absence-coming-539612)
- [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/austin-reaves-heel-remains-out-vs-charlotte)
- [Canadian Press via Yahoo, 18 Nov](https://ca.sports.yahoo.com/news/raptors-forward-barnes-against-wizards-183808081.html)
- [NBC Sports (Zak Hanshew), 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/scottie-barnes-groin-out-wednesday)
- [RotoWire, 19 Nov](https://www.rotowire.com/basketball/headlines/scottie-barnes-news-removed-from-injury-report-540046)
- [Yahoo (Teddy Ricketson), 8 Nov](https://sports.yahoo.com/nba/article/pistons-say-c-jalen-duren-will-miss-at-least-another-two-weeks-due-to-hamstring-strain-165124644.html)
- [NBC Sports (Nick Shlain), 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/trey-murphy-knee-questionable-friday-vs-thunder)
- [Pelicans On SI via Yahoo (David Grubb), 19 Nov](https://sports.yahoo.com/articles/jamahl-mosley-gets-f-pelicans-170006841.html)
- [NBC Sports (Nick Shlain), 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/kelel-ware-nate-amnet-larry-nance-start-vs-por)
- [Behind the Buck Pass, 15 Nov](https://behindthebuckpass.com/kelel-ware-rejoining-bucks-starting-five-inevitable-next-step)
- [Detroit News (Coty M. Davis) via Yahoo, 19 Nov](https://sports.yahoo.com/articles/cunningham-less-pistons-end-road-033244487.html)
- [ESPN recap](https://africa.espn.com/nba/recap/_/gameId/401909977)
- [Heavy (Erik C. Anderson), 19 Nov](https://heavy.com/sports/nba/detroit-pistons/cade-cunningham-injury-update-raptors/)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/pistons-start-daniss-kevin-green-ausar-collins)
- [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-daniss-jenkins-hands-nine-assists-in-win/)
- [Detroit News, 8 Nov](https://www.detroitnews.com/story/sports/nba/pistons/2026/11/08/pistons-all-star-jalen-duren-out-another-two-weeks-with-hamstring-strain/92677147007/)
- [Detroit Sports Nation citing The Detroit News, 17 Nov](https://detroitsportsnation.com/duncan-robinson-injury-pistons-espn-first-month/gkaplan/detroit-pistons/11/17/2026/508470/)
- [RotoWire, 14 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-news-blocks-four-shots-in-return-539214)
- [NBC Sports, 14 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/yves-missi-knee-will-play-on-minutes-restriction)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/yves-missi-produces-14-rebounds-three-steals)
- [ClutchPoints, 19 Nov](https://clutchpoints.com/nba/new-orleans-pelicans/shorthanded-pelicans-prioritize-7-games-before-christmas-day)
- [CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-will-play-monday-539454/)
- [CBS/RotoWire, 16 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-doesnt-return-to-mondays-loss/)
- [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-offensive-glass-fuels-solid-outing/)
- [MassLive via Yahoo, 18 Nov](https://sports.yahoo.com/articles/paul-george-delivers-good-news-110100607.html)
- [NBC Sports, 2 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-02/paul-george-rest-out-monday-vs-rockets)
- [NBA official injury report, 11 Nov, 5 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_00PM.pdf)
- [iHeart / NBA report, 20 Nov](https://957wdae.iheart.com/content/2026-11-20-magic-vs-nets-injury-report-nov-20/)
- [TSN, Oct](https://www.tsn.ca/nba/article/report-magics-banchero-out-multiple-weeks-with-low-grade-high-ankle-sprain-n1-50266620/)
- [RotoWire, 17 Nov, via CBS player page](https://www.cbssports.com/nba/players/3177410/jalen-suggs/)
- [Heavy, 19 Nov, 8:16 PM](https://heavy.com/sports/nba/los-angeles-lakers/lakers-austin-reaves-injury-kings-update/)
- [NBC Sports, 19 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-19/quentin-grimes-puts-up-20-7-4-in-loss-to-the-jazz)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/aday-mara-records-10-points-eight-assists)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/thunder-to-start-shai-ajay-mccain-mara-i-hart)
- [CBS Sports, 31 Oct](https://www.cbssports.com/nba/news/chet-holmgren-injury-how-can-thunder-survive-trade-rumors/)
- [NBC Sports / NBA report, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/jaylon-tyson-ankle-remains-out-friday-vs-pacers)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/jaylon-tyson-ankle-out-wednesday-vs-grizzlies)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/tyrese-proctor-scores-17-points-as-starter)
- [Cavaliers, 16 Nov](https://www.nba.com/cavaliers/news/releases-evan-mobley-261116)
- [NBA.com Pacers preview, 19 Nov](https://www.nba.com/pacers/news/preview-pacers-cavaliers-261120)
- [NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)
- [Bucks On SI, 19 Nov](https://www.si.com/nba/bucks/onsi/bucks-will-have-new-look-lineup-as-lillard-returns-to-town-with-blazers-preview-starters-injuries-how-to-watch-01m7ty7gkrqg)
- [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/kyle-kuzma-shoulder-out-thursday-vs-portland)
- [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910020)
- [15 Nov](https://behindthebuckpass.com/bucks-risk-stunting-kasparas-jakucionis-growth-rapid-rotation-changes)
- [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401909926)
- [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401909969)
- [Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)
- [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910016)
- [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-cleared-for-action-wednesday/)
- [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-andrew-nembhard-could-miss-another-game-friday/)
- [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-chips-in-14-points-vs-houston/)
- [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/kings-precious-achiuwa-exits-game-with-leg-contusion/)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/sac-starts-acuff-lavine-hunter-murray-sabonis)
- [ESPN box score](https://www.espn.com/nba/boxscore/_/gameId/401910018)
- [RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/neemias-queta-news-sitting-out-monday-539449)
- [Heavy, 16 Nov](https://heavy.com/sports/nba/boston-celtics/neemias-queta-injury-update-celtics-streak/)
- [nba.com/blazers, 30 Oct](https://www.nba.com/blazers/news/ja-morant-injury-update)
- [Yahoo/Heavy, 8 Nov](https://sports.yahoo.com/articles/trail-blazers-announce-encouraging-ja-045805609.html)
- [NBC Sports, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/nori-morant-could-be-back-sooner-than-expected)
- [Heavy, 11 Nov](https://heavy.com/sports/nba/portland-trail-blazers/good-ja-morant-news-amid-injury-recovery/)
- [Heavy via Yahoo, 17 Nov ET / 18 Nov 01:39 UTC](https://sports.yahoo.com/articles/espn-insider-drops-latest-jaylen-013927700.html)
- [BasketNews, 18 Nov](https://basketnews.com/news-259795-76ers-earn-massive-jaylen-brown-update-amid-troubling-hamstring-injury.html)
- [NBC Sports Philadelphia, 18 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-magic-live-updates-lebron-james-joel-embiid-tyrese-maxey/767473/)
- [SI / All 76ers, ~19 Nov](https://www.si.com/nba/76ers/onsi/76ers-injury-situation-is-already-looking-up-in-magic-win-aftermath-01m7t920zvk4)
- [Northeast Times, 19 Nov](https://northeasttimes.com/2026/11/19/sixers-injury-report-maxey-brown-next-three-games-november-2026/)
- [NBC Sports, 13 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-14/brandin-podziemski-limited-to-eight-points-friday)
- [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandin-podziemski-goes-cold-from-deep-in-dallas/)
- [Covers box score, 19 Nov](https://www.covers.com/sport/basketball/nba/matchup/388758)
- [Hoops Rumors, 7 Nov](https://www.hoopsrumors.com/2026/11/hornets-notes-injuries-miller-knueppel-williams-offseason.html)
- [Fadeaway World via Yahoo, 18 Nov](https://sports.yahoo.com/articles/hornets-coach-explains-why-brandon-104117242.html)
- [SI, 19 Nov](https://www.si.com/nba/hornets-bizarre-decision-rest-starters-ot-nba-injury-problem)
- [ClutchPoints, 18 Nov](https://clutchpoints.com/nba/charlotte-hornets/hornets-news-why-didnt-brandon-miller-coby-white-play-ot-lakers-collapse)
- [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-deliver-devastating-kon-knueppel-224941481.html)
- [Heavy via Yahoo, 24 Oct](https://sports.yahoo.com/articles/dallas-mavericks-announce-concerning-injury-220756066.html)
- [Dallas Sports Journal, 16 Nov](https://dallassportsjournal.com/cooper-flagg-new-england-maine-fans-back-to-back-celtics/)
- [Mavs.com, Eddie Sefko, 16 Nov](https://www.nba.com/mavs/news/flaggs-growing-leadership-skills-will-be-helpful-in-reversing-recent-trend)
- [ClutchPoints, 24 Oct](https://clutchpoints.com/nba/dallas-mavericks/mavericks-news-kyrie-irvings-status-spurs-game-up-in-air-cooper-flagg-injury)
- [BasketNews, 15 Nov](https://basketnews.com/news-259537-why-kyrie-irving-will-not-play-vs-celtics-mavs-announce-huge-injury-update.html)
- [Dallas Morning News via Yahoo, 15 Nov](https://sports.yahoo.com/articles/kyrie-irving-sits-mavericks-vs-222607808.html)
- [Yardbarker, 10 Nov](https://www.yardbarker.com/nba/articles/kyrie_irving_explains_decision_to_play_mavericks_back_to_back_after_acl_tear/s1_17810_44540702)
- [ClutchPoints via Yahoo, 2 Nov](https://sports.yahoo.com/articles/pacers-pascal-siakam-injury-vs-225410478.html)
- [ClutchPoints via Yahoo, 3 Nov](https://sports.yahoo.com/articles/pacers-down-7-players-vs-010520478.html)
- [NBC Sports, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/pascal-siakam-rest-removed-from-injury-report)
- [CBS/RotoWire, 9 Nov 2025](https://www.cbssports.com/fantasy/basketball/news/pacers-pascal-siakam-resting-sunday)
- [FantasyPros, 17 Jan 2026](https://www.fantasypros.com/nba/news/566128/pascal-siakam-rest-ruled-out-saturday.php)
- [Yahoo, 17 Nov](https://sports.yahoo.com/articles/rick-carlisle-no-definite-timeline-174500355.html)
- [hoopsrumors.com, 19 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-banchero-kawhi-pacers-edwards-grizzlies.html)
- [rotowire.com, 19 Nov](https://www.rotowire.com/basketball/headlines/andrew-nembhard-injury-could-miss-another-game-friday-540057)
- [NBC Sports, 26 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/andrew-nembhard-neck-downgraded-to-out-monday)
- [RotoWire, Oct](https://www.rotowire.com/basketball/headlines/andrew-nembhard-injury-out-vs-bucks-536206)
- [Heavy, 19 Nov](https://heavy.com/sports/nba/new-york-knicks/jalen-brunson-injury-knicks-timberwolves-update/)
- [CBS Sports/RotoWire, 19 Nov 8:32 PM ET](https://www.cbssports.com/fantasy/basketball/news/knicks-jalen-brunson-returns-thursday/)
- [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/jalen-brunson-has-21-points-four-threes-in-win)
- [Bleacher Report, 19 Nov](https://bleacherreport.com/articles/25535537-brunson-kat-carry-knicks-win-over-wolves-box-score-stats-highlights-lamelo-top-players)
- [RotoWire, 18 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-ruled-out-for-thursday-539822)
- [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/brandon-ingram-achilles-out-thursday-vs-spurs)
- [ClutchPoints, 15 Nov](https://clutchpoints.com/nba/los-angeles-clippers/clippers-brandon-ingram-injury-update-teases-return-coming-very-soon)
- [Hoops Rumors, 15 Nov](https://www.hoopsrumors.com/2026/11/injury-notes-clippers-miller-barnes-nurkic-b-williams.html)
- [RotoBaller, 15 Nov](https://www.rotoballer.com/player-news/brandon-ingram-close-to-returning/1994624)
- [Orlando Magic Daily, 19 Nov](https://orlandomagicdaily.com/paolo-banchero-taking-different-approach-orlando-magic-return-01m7ta5knyg4)
- [Basketnews, 19 Nov](https://basketnews.com/news-259854-paolo-banchero-shares-major-update-on-his-recovery-from-ankle-injury.html)
- [RotoBaller, 19 Nov](https://www.rotoballer.com/player-news/paolo-banchero-ankle-targeting-return-within-a-couple-of-weeks/1997928)
