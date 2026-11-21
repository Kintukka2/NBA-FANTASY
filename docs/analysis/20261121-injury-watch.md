# Injury Watch: 21 Nov 2026

- Generated 2026-11-21 07:21 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 107 players in ESPN's injury feed. 39 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 21 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

Pickups whose gain should last through this week (21–22 Nov), with one add left:
- **Aday Mara** (OKC, free agent): a fixture in the starting lineup at about 27 min with Chet Holmgren out (8–10 weeks from 30 Oct; *ESPN est.* 2 Jan). FP/g without the absentees 35.5. Rate 36.4 ‡ role row; season 29.5 (16), L7 42.0 (4), L15 37.2 (8), L30 30.5 (15). Games 1 / 3 (Sun at MIA). **This week's Sunday pick.**
- **Jaxson Hayes** (UTAH, free agent): starting center until Jusuf Nurkic is re-evaluated about 27 Nov (*ESPN est.* 29 Nov). Season 28.3 (14), L7 31.7 (3), L15 28.7 (7), L30 28.3 (14); rate 29.0; projected 16.5. Games 1 / 3. He fell on his hip on 20 Nov, so check Utah's Sunday report.
- **Kevin Huerter** (DET, free agent): starting at 36 min while Duncan Robinson is out (re-evaluation about 24 Nov; *ESPN est.* 27 Nov). Season 23.9 (14), L7 30.0 (4), L15 32.6 (7), L30 24.9 (14); rate 28.4; projected 22.9. L7 is +6.1 because his minutes went from 26.7 to 36.5. Games 1 / 3.
- **Christian Braun** (DEN, waivers): a secure starter at 32–33 min, but he clears waivers in 24 hours, too late for this week. Season 32.8 (14), L7 41.0 (4), L15 32.9 (7), L30 32.8 (14); rate 35.1. L7 is +8.2 from shooting and steals; his minutes are slightly down. A target for next week.

Not shortlisted:
- **Allen Graves** (TOR) and **Tyrese Proctor** (CLE): their numbers overstate them. Graves' 40.0 FP/g without the absentees rests on 2 games (small sample) and a start that lasts only while Collin Murray-Boyles is in concussion protocol (*ESPN est.* 23 Nov). Proctor's minutes are already shrinking. Neither team plays again this week.

## Research

Earlier notes still hold ([20261120-injury-watch.md](20261120-injury-watch.md)). New since then:

**TOR**
- **Kawhi Leonard (us, IR):** He has left patellar tendinopathy, the recurring tendon condition the Raptors managed in 2019. On 18 Nov he had reached on-court loading work, with live contact next and a return "around the end of the month" as the target ([TSN, 18 Nov](https://www.tsn.ca/nba/article/raptors-leonard-dealing-with-left-patellar-tendinopathy/)).
  - That target has slipped. Shams Charania now reports **at least two more weeks**, so about 4 Dec. He has been out since 23 Oct, and the Raptors expect him to stay in the lineup once he is back ([TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/); [Sportsnet via BVM Sports, 20 Nov](https://bvmsports.com/2026/11/20/report-raptors-kawhi-leonard-out-at-least-two-more-weeks/)). *ESPN est.* 3 Dec, which agrees.
- **RJ Barrett:** Nothing new since 19 Nov. He is out at least two weeks with a right hamstring strain, and the re-evaluation falls about 3 Dec. That is a check-up, not a return date ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks)). He was listed out on 20 Nov ([NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)). *ESPN est.* 13 Dec.
- **Allen Graves:** He made his first career start on Fri 20 Nov at DET, in Collin Murray-Boyles's spot, and scored 20 pts (6-9 FG) with 10 reb, 3 stl and 1 blk in 33 min ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl); [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-allen-graves-records-first-career-double-double/)). Before that he averaged 4.6 pts in 14.9 min ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/allen-graves-news-earns-first-career-start-friday-540227)).
  - **Role:** RotoWire says he "could continue to start" while Barrett, Leonard and Murray-Boyles have no return dates, and that he should keep extra minutes even if he goes back to the bench ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-allen-graves-records-first-career-double-double/)).
  - **Risk:** Murray-Boyles is the first threat to the start. He is in concussion protocol with no timeline, *ESPN est.* 23 Nov ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/collin-murray-boyles-placed-in-concussion-protocol)). The returns of Leonard and Barrett, early Dec at the soonest, end the bigger role.
  - **Form:** L7 26.5 (4) against a season of 16.4 (+10.1). The reason is minutes: 16.0 for the season, 23.2 over L7 (`form.py`). His 40.0 FP/g without Leonard and Barrett rests on 2 games (**small sample**). TOR has no game left this week (0 / 3). ([NBC Sports, 20 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-20/allen-graves-records-double-double-in-first-start))

**OKC**
- **Chet Holmgren:** He has a small tear in his right patellar tendon. He had a nonsurgical biological treatment on 30 Oct and is out **8–10 weeks**, so about 25 Dec to 8 Jan ([AP via Yahoo, 31 Oct](https://sports.yahoo.com/articles/chet-holmgren-least-2-months-011311180.html)). He was still out on 20 Nov, with no setback or new timeline reported ([Heavy, 20 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-pelicans-november-20/)). *ESPN est.* 2 Jan, inside the window.
- **Jalen Williams:** He had surgery for a fractured left fibula and a dislocated ankle. The team says he will be re-evaluated "before the end of the 2026-27 regular season" and has given no date ([OKC Thunder Wire via Yahoo, 28 Oct](https://sports.yahoo.com/articles/jalen-williams-leg-surgery-evaluated-234119739.html)).
  - Heavy puts that re-evaluation in late March to early April ([Heavy, 20 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-pelicans-november-20/)). *ESPN est.* 2 Mar, which looks early.
- **Cason Wallace:** A labral tear in his left shoulder was repaired on 30 Oct. He will be re-evaluated before the end of the regular season ([AP via Yahoo, 31 Oct](https://sports.yahoo.com/articles/chet-holmgren-least-2-months-011311180.html)). He has not been ruled out for the season, and there is no new timeline ([Heavy, 20 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-pelicans-november-20/)). *ESPN est.* 2 Mar.

**DEN**
- **Julian Strawther:** He sprained his left knee in a preseason game at the Clippers, and the team said he would be re-evaluated in **six weeks**, about 27 Nov. The Gazette said it "might be December" before he plays ([Denver Gazette, 16 Oct](https://www.denvergazette.com/2026/10/16/nuggets-provide-update-on-julian-strawthers-knee-injury-5/); [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain)).
  - He was still out vs HOU on 20 Nov and has not played this season. No result from the re-evaluation has been reported ([Nuggets On SI, 20 Nov](https://www.si.com/nba/nuggets/onsi/nuggets-could-get-huge-boost-vs-rockets-with-lopsided-injury-report)). *ESPN est.* 29 Nov: treat it as the check-up, not a first game.
- **Christian Braun (waivers):** He is the starting shooting guard, and his minutes are steady: 32.0, 33.1 and 33.3 over his last 3, 5 and 10 games. NBC calls Denver's rotation "pretty locked in" ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - **Role:** It does not depend on Strawther, who was slotted in as a second-unit shooter in Tim Hardaway Jr.'s old bench spot ([Denver Gazette, 16 Oct](https://www.denvergazette.com/2026/10/16/nuggets-provide-update-on-julian-strawthers-knee-injury-5/)). Strawther's return should not cut it.
  - **Form:** L7 41.0 (4) against a season of 32.8 (+8.2). Minutes do not explain it (33.6 for the season, 31.8 over L7, `form.py`). Shooting and steals do: on 20 Nov vs HOU he scored 19 on 7-10 FG with 4 stl and 0 TO in 31+ min. Adelman on his defense: "that's his role on this team" ([Denver Gazette, 20 Nov](https://www.denvergazette.com/2026/11/20/christian-braun-comes-up-big-on-both-ends-as-nuggets-beat-rockets/)). Expect him to drift back toward his ~33 season level. DEN has 1 game left this week, Sun 22 at CHI.

**DET**
- **Jalen Duren (us):** He was still out on 20 Nov and is "set to be re-evaluated next week" ([Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html)). He has resumed basketball activities, but no return date has been given ([MLive via Yahoo, 20 Nov](https://sports.yahoo.com/articles/pistons-veteran-undergoes-knee-surgery-233137937.html)). *ESPN est.* 24 Nov.
- **Duncan Robinson:** He strained his left quad on 14 Nov vs MIA. The Pistons said on 17 Nov that he would be re-evaluated in one week, about 24 Nov ([HoopsHype via Yahoo, 17 Nov](https://sports.yahoo.com/articles/duncan-robinson-left-quad-strain-172952431.html)).
  - On 20 Nov he was "still another few days away from an update" ([MLive via Yahoo, 20 Nov](https://sports.yahoo.com/articles/pistons-veteran-undergoes-knee-surgery-233137937.html)). Rotoworld's 20 Nov note expects him to miss at least 1–2 more games, with Kevin Huerter starting in his place ([NBC Sports player news, 17–20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week)). *ESPN est.* 27 Nov. His L7 of 13.0 rests on 1 game, which is noise.
- **Taurean Prince:** He had right knee surgery "to address lingering issues" and has "no timeline for a return" ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/taurean-prince-injury-has-no-return-timeline-540207)). Bickerstaff: "some stuff that had been lingering." He is out for the foreseeable future ([MLive via Yahoo, 20 Nov](https://sports.yahoo.com/articles/pistons-veteran-undergoes-knee-surgery-233137937.html)). **No timetable reported.** *ESPN est.* 13 Dec.

**CLE**
- **Evan Mobley:** Nothing has changed since the 16 Nov update. He has a left great toe sprain, gets 7–10 days of treatment, and is then re-evaluated, about 23–26 Nov ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/mobley-toe-to-be-re-evaluated-in-7-10-days)).
  - NBC's minutes report expects him back about the end of next week, so around 27–29 Nov ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)). He was out again on 20 Nov ([NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)). *ESPN est.* 29 Nov, which agrees.
- **Nae'Qwan Tomlin:** **No timetable reported.** He has a low back stress reaction, was inactive again on 18 Nov ([CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-naeqwan-tomlin-still-out-wednesday/)) and was out on 20 Nov ([NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)). *ESPN est.* 29 Nov, with no team news behind it.
- **Jaylon Tyson:** He has a right ankle injury and was ruled out on Fri 20 Nov, his third straight game. His next chance to play is Mon 23 Nov at CHI ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-out-for-friday/)). *ESPN est.* 23 Nov.
- **Tyrese Proctor:** He has started four straight games, and his minutes are 29.6, 27.8 and 24.4 over his last 3, 5 and 10 games ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - **Trend:** He is fading. On Fri 20 Nov he played 24 min for 5 pts (2-6 FG), his second straight single-digit game. RotoWire says his opportunities are beginning to shrink, even though he is still starting ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/tyrese-proctor-news-downward-trend-continues-540279)).
  - **Form:** L7 33.4 (5) against a season of 21.8 (+11.6). The reason is minutes: 20.6 for the season, 28.0 over L7 (`form.py`), from starts with Tyson and Mobley out. RotoWire names him among the players gaining from their absence ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-out-for-friday/)).
  - **Risk:** Tyson's return, as soon as 23 Nov, is the first threat to the start, and Mobley's return trims the rotation again ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-out-for-friday/); [NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)). CLE has no game left this week (0 / 3).

**GS**
- **Stephen Curry:** He tore his right oblique on 11 Nov at HOU. The team said he would be re-evaluated in two weeks, about 26 Nov, while Shams Charania reports closer to a month, about 11 Dec ([Heavy via Yahoo, 13 Nov](https://sports.yahoo.com/articles/warriors-announce-official-stephen-curry-203906999.html)). He missed his fourth straight game on 19 Nov ([AP via ABC News, 19 Nov](https://abcnews.com/Sports/wireStory/grizzlies-roll-past-short-handed-warriors-126-98-138311394)). *ESPN est.* 12 Dec, in line with the one-month report.
- **Kristaps Porzingis:** **No timetable reported.** He is out indefinitely with an undisclosed health matter, and the team says an update will come "when available" ([Heavy via Yahoo, 22 Oct](https://sports.yahoo.com/articles/kristaps-porzingis-coming-back-warriors-035243404.html)). As of 19 Nov he was not with the team ([Roundtable via Yahoo, 19 Nov](https://sports.yahoo.com/articles/warriors-vs-grizzlies-injury-report-193903602.html)). *ESPN est.* 2 Jan is a placeholder.
- **Moses Moody:** He ruptured his left patellar tendon in March. Slater reported him progressing toward a return in December or January, with no official timetable ([CBS/RotoWire, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)). He was still out on 19 Nov, hoping to return in late 2026 or early 2027 ([Roundtable via Yahoo, 19 Nov](https://sports.yahoo.com/articles/warriors-vs-grizzlies-injury-report-193903602.html)). *ESPN est.* 1 Dec looks early, since no practice has been reported.
- **Jimmy Butler III:** He is recovering from ACL surgery. Kerr: "a year or so like most ACL's," with no date given ([Heavy via Yahoo, 5 Nov](https://sports.yahoo.com/articles/jimmy-butler-return-steve-kerr-143904723.html)). He hopes to return in early 2027 ([Roundtable via Yahoo, 19 Nov](https://sports.yahoo.com/articles/warriors-vs-grizzlies-injury-report-193903602.html)). *ESPN est.* 2 Jan.
- **Draymond Green:** He played through right elbow soreness on 18 Nov ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-draymond-green-available-wednesday/)). He sat out on 19 Nov at MEM, the second night of a back-to-back, with "right elbow injury management" ([Roundtable via Yahoo, 19 Nov](https://sports.yahoo.com/articles/warriors-vs-grizzlies-injury-report-193903602.html)).
  - **No timetable reported** beyond that. ESPN lists him day-to-day ("Rest"), *ESPN est.* 22 Nov. GS's injury report for Sun 22 vs BOS had not been filed yet ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)).
- **Brandon Williams:** He strained his left hamstring on 9 Nov and has moved on to court work. He is re-evaluated on Sat 21 Nov, and his next chance to play is Sun 22 Nov vs BOS ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandon-williams-advances-to-on-court-activities/)). GS had not filed its report for Sunday by 2:15 AM ET on 21 Nov, so no result has been reported yet ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). No minutes limit has been mentioned ([Warriors On SI, 18 Nov](https://www.si.com/nba/warriors/onsi/warriors-announce-injury-update-on-brandon-williams-hamstring-01m7qtgye3c1)). *ESPN est.* 22 Nov.
  - **Role:** He was the reserve guard before the injury, at 10.4 pts in 16.4 min ([Heavy via Yahoo, 11 Nov](https://sports.yahoo.com/articles/warriors-encouraging-brandon-williams-injury-010221980.html)). He has played most of his minutes in Curry's place at point guard. SI's writer argues that Kerr should start him when he returns, but that is opinion, not a plan ([Warriors On SI, 18 Nov](https://www.si.com/nba/warriors/onsi/warriors-announce-injury-update-on-brandon-williams-hamstring-01m7qtgye3c1)). De'Anthony Melton has not filled the gap ([NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html)).
  - **Form:** His 33.0 FP/g without Curry and the others rests on 1 game (**small sample**), and he has no L7. His first game back from a hamstring injury could be managed. Curry's return, likely about mid-Dec, ends the bigger role ([Heavy via Yahoo, 13 Nov](https://sports.yahoo.com/articles/warriors-announce-official-stephen-curry-203906999.html)).

**CHI**
- **Jalen Smith (us):** He was a late scratch on Fri 20 Nov vs WSH with illness, and Nic Claxton was the likelier starter at C ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-out-sick-friday/)). The league report lists it as a gastrointestinal illness ([NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf)).
  - **No timetable reported.** CHI's report for Sun 22 vs DEN had not been filed by 2:15 AM ET on 21 Nov ([NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf)). *ESPN est.* 22 Nov.
- **Caleb Wilson:** He had surgery on his fractured right hand on 12 Nov and was given 4–6 weeks. He is now running, working on his left hand and attending practice. Wilson: "I'll play again in a couple weeks" ([AP via Yahoo, 21 Nov](https://sports.yahoo.com/articles/bulls-rookie-caleb-wilson-looking-012217305.html)). The team's re-evaluation is still about 3 Dec (earlier notes). *ESPN est.* 13 Dec, at the early end of the 4–6 weeks.

**MIL**

- **Ousmane Dieng:** No update since his finger surgery on 16 Nov. **No timetable reported** (*ESPN est.* 14 Dec). He is listed out for Sat 21 Nov at PHI ([iHeart/Fox Sports 1070, 21 Nov](https://foxsports1070.iheart.com/content/2026-11-21-bucks-vs-76ers-injury-report-nov-21/)).
- **Brayden Burries:** He started again on Thu 19 Nov vs POR: 28 min, 14 pts (5-13 FG), 3 reb, 3 ast, 2 stl. Ryan Rollins came off the bench for 21 min ([FS Roundup box, 19 Nov](https://www.fsroundup.com/nba/game/portland-trail-blazers-at-milwaukee-bucks-2026-11-19)). RotoWire notes multiple steals in 4 of his last 5 games and 9+ shots in 3 straight, but says cold shooting and a crowded backcourt cap his upside ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-defensive-activity-offsets-cold-shooting/)). Form: L7 26.5 (4 g), L15 28.2 (8), L30 22.8 (16), season 22.8.
  - He has held the starting job since early November, before Dieng was hurt. Dieng's return does not end the role; Rollins is the threat ([RotoWire, 9 Nov](https://www.rotowire.com/basketball/headlines/brayden-burries-news-holding-down-starting-job-538340)). He is not on the injury report for Sat at PHI, MIL's only game left this week ([iHeart, 21 Nov](https://foxsports1070.iheart.com/content/2026-11-21-bucks-vs-76ers-injury-report-nov-21/)).

**UTAH**

- **Lauri Markkanen:** Two nondisplaced fractures in his right hand, suffered 6 Nov at DAL and announced 11 Nov. He is **re-evaluated in four weeks**, about 9 Dec ([Deseret News, 11 Nov](https://www.deseret.com/sports/2026/11/11/lauri-markkanen-diagnosed-with-two-nondisplaced-fractures-in-his-right-hand/)). No update since. *ESPN est.* 4 Jan is almost four weeks after the re-evaluation.
- **Jaren Jackson Jr.:** Torn right MCL (26 Oct vs MEM), no surgery. He is **re-evaluated six weeks** after 27 Oct, about 8 Dec ([NBA.com, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026)). No November update found. *ESPN est.* 14 Dec.
- **Jusuf Nurkic:** The Jazz re-evaluated his partial plantar plate tear (right second toe) on 20 Nov. He "is continuing to make progress and participate in team on-court activities and will be re-evaluated in one week", about 27 Nov ([Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). *ESPN est.* 29 Nov. After 27 Nov, UTAH's games are Fri 27 vs DEN and Sun 29 vs PHX.
  - For `news_overrides.csv`: the current `return` floor of 26 Nov came from the 19 Nov note. It is a day before this re-evaluation, so the floor could move to 27 Nov ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-jusuf-nurkic-will-be-re-evaluated-in-one-week/)).
- **Brice Sensabaugh:** L7 **29.0 (5 g)** vs season 18.8, **+10.2**. L15 22.6 (9), L30 18.8 (17). **What changed:** his bench minutes grew with Markkanen and Jackson out. He played 30 min on 15 Nov, then had 40 pts (16-21 FG, 8-11 3PT), 11 reb and 5 ast in 35 min **off the bench** on 17 Nov at LAC. RotoWire ties the bigger role to Markkanen's absence ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-brice-sensabaugh-dazzles-with-4011-double-double/)).
  - Since then he played 14 min for 8 pts on 18 Nov at LAL and 26 min for 18 pts on 20 Nov vs PHX ([CBS Sports game log, 20 Nov](https://www.cbssports.com/nba/players/28951832/brice-sensabaugh/fantasy/)). The 40-point game carries much of the L7, and his minutes range from 14 to 35. The role should last at least until Markkanen's re-evaluation (about 9 Dec).

**ORL**

- **Paolo Banchero:** Right high ankle sprain from late October. Sean Sweeney said on 18 Nov he is progressing, with "no timeline right now". Banchero hopes to be back "hopefully within the next couple of weeks". 18 Nov was his 12th straight absence ([Orlando Sentinel via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-banchero-shares-110000466.html)). The first reported estimate was 4–6 weeks (Shams Charania), which runs to about 4 Dec ([Heavy, 24 Oct](https://heavy.com/sports/nba/orlando-magic/orlando-magic-concerning-update-paolo-banchero/)). *ESPN est.* 29 Nov.

**SA**

- **Dylan Harper:** The Spurs' official diagnosis on 19 Nov is a left hip external rotator strain. He is out **2–3 weeks**, depending on how he responds to treatment, with more details "at a later date". There is no re-evaluation date ([ClutchPoints via Yahoo, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html)). That puts his return at about 3–10 Dec. *ESPN est.* 13 Dec.
- **Tobias Harris:** New since the 17 Nov notes: asked about a debut before Christmas, Mitch Johnson would not commit: "For his sake, I hope so." He added that "it'll be later than he wanted and later than he probably could", and said there have been no setbacks ([San Antonio Express-News via Yahoo, 17 Nov](https://sports.yahoo.com/articles/mitch-johnson-reiterates-spurs-taking-030657990.html)). Chris Haynes's "early December" is still the only reported target. *ESPN est.* 3 Dec looks optimistic.
- **Julian Champagnie:** He took Harper's starting spot on 19 Nov vs LAC: 29 min, 20 pts (8-14 FG, 4 3PM), 4 reb, 1 ast. NBC Sports expects him to stay in the lineup while Harper is out ([NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/julian-champagnie-has-20-points-four-threes-in-win)). Form: L7 21.8 (4 g), L15 23.0 (8), L30 23.2 (15), season 23.9. His 29.0 FP/g without the absentees rests on that one game (**small sample**).
  - Harper's return (about 3–10 Dec) ends the start. Harris is likely to come off the bench when he returns ([Heavy via Yahoo, 18 Nov](https://sports.yahoo.com/articles/spurs-coach-mitch-johnson-shares-052207832.html)).

**ATL**

- **CJ McCollum:** Left calf strain from 15 Nov at MIL. The Hawks said he "will be re-evaluated in approximately four weeks", about 15 Dec ([NBA.com, 18 Nov](https://www.nba.com/news/hawks-cj-mccollum-to-miss-at-least-four-weeks-with-left-calf-strain)). *ESPN est.* 19 Dec.
- **Mouhamed Gueye:** Fractured left foot, with surgery in July. In the Hawks' 13 Nov update he had progressed to on-court activities and will be re-evaluated in four weeks, about 11 Dec ([Last Word on Sports via Yahoo, 13 Nov](https://sports.yahoo.com/articles/atlanta-hawks-mouhamed-gueye-4-130022920.html)). *ESPN est.* 12 Dec.
- **Kingston Flemings:** Back (lumbar) strain. He was out Fri 20 Nov vs CHA, his third straight absence, and is **questionable for Sun 22 Nov vs DET** ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/kingston-flemings-injury-ruled-out-for-friday-540201)). *ESPN est.* 22 Nov.
- **Jock Landale:** Right hip inflammation. He was out again Fri 20 Nov vs CHA ([Roundtable via Yahoo, 20 Nov](https://sports.yahoo.com/articles/hornets-visit-hawks-nba-cup-162833711.html)). No timetable reported. *ESPN est.* 22 Nov.
- **Aaron Wiggins:** He started on 18 Nov at OKC, his first start of the season, with McCollum and Flemings out ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-aaron-wiggins-entering-starting-lineup-wednesday/)). He started again Fri vs CHA: 19 pts (7-12 FG, 4 3PM), 2 reb, 3 ast, 1 stl. NBC Sports calls him "worth streaming until Flemings returns", after which he likely goes back to the bench ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/aaron-wiggins-scores-19-points-as-starter)). Form: L7 22.2 (4 g), L15 26.4 (7), L30 26.7 (16), season 26.7.
  - The start depends on Flemings (questionable Sun), not McCollum. His split without the absentees covers only 2 games (**small sample**). After Sun vs DET, ATL does not play until Fri 27 at BOS ([ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/atl)).

**LAL**

- **Austin Reaves:** He **did not play Fri 20 Nov** vs SAC, his fourth straight absence, with a left heel contusion and bone bruise from 11 Nov vs MIL ([Roundtable via Yahoo, 20 Nov](https://sports.yahoo.com/articles/lakers-vs-kings-injury-report-212255329.html)). The Lakers have **no weekend game**. Redick had a "great day" report from his on-court work and hopes he returns **Mon 23 vs UTAH** or Fri 27 at SA, but he has not been cleared ([Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/lakers-coach-jj-redick-reveals-043347864.html)). *ESPN est.* 23 Nov.

**CHI**

- **Isaac Okoro:** L7 **29.4 (5 g)** vs season 16.6, **+12.8**. L15 24.6 (7), L30 16.6 (15). **What changed:** he has started at SF since Caleb Wilson's hand injury (back in December per the Tribune; *ESPN est.* 13 Dec), playing 31.6 min in those games against 22.8 on the season. He holds the job "until Wilson returns in December". After that, Powell or Buzelis would have to sit for him to keep starting. Tiago Splitter calls him "our best point-of-attack defender" ([Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html)).
  - Fri 20 Nov vs WSH: he started and played 29 min for 9 pts, 7 reb, 1 ast, 1 stl ([NBA.com box, 20 Nov](https://www.nba.com/bulls/game/0022600047-wizards-vs-bulls-chicago-il-11-20-2026)). Our Jalen Smith sat with an illness (no timetable reported, *ESPN est.* 22 Nov), and Nic Claxton started at C ([On Tap Sports Net, 20 Nov](https://ontapsportsnet.com/nba/chicago-bulls/bulls-wizards-recap-november-20-2026/)).

**Back soon and yet to play**

- **Jusuf Nurkic** (re-evaluated about 27 Nov, *ESPN est.* 29 Nov): No minutes limit reported yet. He still has to get through full-contact 5-on-5 work before he plays ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-jusuf-nurkic-will-be-re-evaluated-in-one-week/)). **Role waiting:** the starting centre job. Jazz On SI called him a "major addition" as a starter ([Jazz On SI via Yahoo, 4 Nov](https://sports.yahoo.com/articles/latest-jusuf-nurkic-status-good-193548714.html)). Mo Bamba's minutes are the ones at risk.
- **Tobias Harris** (early December per Chris Haynes, no date from the team; *ESPN est.* 3 Dec): A minutes restriction is possible but not confirmed. He was signed to start at PF, but the Spurs' four-guard lineup around Wembanyama points to a **bench role** ([Heavy via Yahoo, 18 Nov](https://sports.yahoo.com/articles/spurs-coach-mitch-johnson-shares-052207832.html)).
- **Jerami Grant:** Left calf strain. He left on 19 Nov vs GS after about 5 minutes and is **out Sat 21 Nov at MIN**. No timetable reported. "Calf strains are tricky, so expect the Grizzlies to be careful" ([Yahoo Sports, 20 Nov](https://sports.yahoo.com/articles/grizzlies-cam-boozer-jerami-grant-000744742.html)). ESPN still lists him day-to-day (*ESPN est.* 21 Nov), which the news contradicts. MEM's next game is Mon 23 at CHA. Taylor Hendricks and Olivier-Maxence Prosper take his minutes ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jerami-grant-out-with-calf-strain-against-t-wolves)).
- **Dereck Lively II:** Right foot surgery. On 20 Nov Dusty May said he is "moving well". Lively told him he is "close", and May said "I'm not sure what close is" ([SI All Mavericks, 20 Nov](https://www.si.com/nba/mavericks/onsi/dusty-may-provides-much-needed-injury-update-dallas-mavericks-center-dereck-lively-ii-)). No timetable reported. *ESPN est.* 27 Nov looks early. **Role waiting:** backup C. RotoWire says Daniel Gafford is "locked in" as the top centre, with Morez Johnson, Santi Aldama and Moussa Cisse also taking centre minutes. No November minutes limit is reported; a September note flagged a possible restriction ([CBS/RotoWire player news, 17–20 Nov](https://www.cbssports.com/nba/players/28951880/dereck-lively-ii/)).
- **Collin Murray-Boyles:** In concussion protocol since 19 Nov. He left on 18 Nov vs WSH after 4:54, first called an illness, and must finish the return-to-participation process. He missed Fri at DET ([TSN, 19 Nov](https://www.tsn.ca/nba/article/raptors-barrett-hamstring-out-at-least-two-weeks-murray-boyles-enters-concussion-protocol/)). No timetable reported. TOR's next game is Mon 23 vs MIL (*ESPN est.* 23 Nov). **Role waiting:** he started at PF beside Poeltl on 18 Nov ([NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/raptors-start-iq-walter-battle-collin-poeltl)).
- **Bradley Beal:** Right knee. He is out Sat 21 Nov at DAL, with no timetable reported because the knee swells when he tries three practices in a row ([Heavy, 20 Nov](https://heavy.com/sports/nba/los-angeles-clippers/injury-report-vs-mavericks-november-21/)). *ESPN est.* 29 Nov has no report behind it. His role shrinks further once Ingram debuts Monday (same source).
- **T.J. McConnell:** New injury. He played Fri 20 Nov at CLE and **left with a left hamstring issue**; he missed the start of the season with the right one. Rick Carlisle would not guess how serious it is. RotoWire does not expect him Sun 22 at NY, the first night of a back-to-back, and Quenton Jackson gets more minutes ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/tj-mcconnell-injury-exits-game-with-hamstring-issue-540267)). No timetable reported. *ESPN est.* 22 Nov.
- **Brandon Ingram** (rostered by Melbourne poopoo): Expected to make his season and Clippers debut **Mon 23 Nov at HOU** (Shams Charania). He is out Sat at DAL and is "likely to carry a minutes restriction". Kris Dunn, Max Strus and Gradey Dick lose minutes ([RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-set-for-season-debut-monday-540187); [Fadeaway World, 20 Nov](https://fadeawayworld.net/nba/la-clippers/brandon-ingram-will-make-his-clippers-debut-next-week-after-achilles-surgery-recovery)). That matches *ESPN est.* 23 Nov.
- **Jimmy Butler III:** New: the plan is a G League (Santa Cruz) rehab stint. Butler told The Athletic on 13 Nov he is "definitely coming down there to play", and Steve Kerr said it "makes such perfect sense". As of 19 Nov there was no assignment and no NBA return date ([Stadium Rant via Yahoo, 20 Nov](https://sports.yahoo.com/articles/jimmy-butler-g-league-plan-024212960.html)). The January–February target stands. *ESPN est.* 2 Jan.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 24.7 (L7 33.2), Yves Missi 28.0 (L7 21.2), Daniss Jenkins 30.1 (L7 32.2), Saddiq Bey 31.1 (L7 41.0), Trey Murphy III 31.7 (L7 38.0). A pickup at or above **31.7** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 32.0 | +18.2 | **40.0** | 16.4 | 26.5 (4) | 18.2 (8) | 16.4 (16) | Free agent | 1% | 0 / 3 |
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 30.5 | +5.8 | **37.5** | 26.4 | 28.5 (4) | 33.4 (8) | 26.4 (14) | Free agent | 37% | 0 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.1 | — | **35.5** | 29.5 | 42.0 (4) | 37.2 (8) | 30.5 (15) | Free agent | 27% | 1 / 3 |
| **Christian Braun** | DEN | Julian Strawther (29 Nov) | 10 | 32.7 | +5.2 | **34.5** | 32.8 | 41.0 (4) | 32.9 (7) | 32.8 (14) | Waivers | 46% | 1 / 3 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (13 Dec); also out: Jalen Duren (24 Nov) | 6 | 32.8 | +15.8 | **33.8** | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 40% | 1 / 3 |
| **Tyrese Proctor** | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 5 | 28.0 | +6.0 | **33.4** | 21.8 | 33.4 (5) | 27.0 (9) | 21.8 (16) | Free agent | 10% | 0 / 3 |
| **Brandon Williams** (out, ESPN est. back 22 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +11.7 | **33.0** | 18.8 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% | 1 / 3 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 5 | 29.2 | +5.4 | **32.8** | 22.8 | 26.5 (4) | 28.2 (8) | 22.8 (16) | Free agent | 10% | 1 / 4 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 5 | 21.2 | +9.7 | **31.6** | 20.4 | 44.7 (3) | 24.6 (7) | 20.4 (15) | Free agent | 10% | 1 / 4 |
| **Mo Bamba** | UTAH | Jusuf Nurkic (29 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 8 | 22.8 | +7.8 | **30.6** | 29.3 | 35.8 (5) | 30.6 (8) | 29.3 (13) | Waivers | 21% | 1 / 3 |
| **Aaron Wiggins** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Kingston Flemings (22 Nov), Jock Landale (22 Nov) | 2 | 30.0 | +4.5 | **30.5** | 26.7 | 22.2 (4) | 26.4 (7) | 26.7 (16) | Free agent | 34% | 1 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 5 | 31.6 | +11.2 | **29.4** | 16.6 | 29.4 (5) | 24.6 (7) | 16.6 (15) | Free agent | 2% | 1 / 3 |
| **Julian Champagnie** | SA | Dylan Harper (13 Dec), Tobias Harris (03 Dec) | 1 | 29.0 | +4.0 | **29.0** | 23.9 | 21.8 (4) | 23.0 (8) | 23.2 (15) | Free agent | 41% | 1 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 22.3 | — | **28.5** | 26.6 | 27.8 (4) | 28.5 (6) | 26.6 (11) | Free agent | 3% | 0 / 4 |
| **Jaylon Tyson** (out, ESPN est. back 23 Nov) | CLE | Nae'Qwan Tomlin (29 Nov), Evan Mobley (29 Nov) | 2 | 32.0 | +9.0 | **28.0** | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% | 0 / 3 |
| **Jamison Battle** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 26.5 | +7.1 | **26.0** | 15.4 | 13.0 (4) | 16.5 (8) | 15.4 (16) | Free agent | 0% | 0 / 3 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 23.4 | — | **25.6** | 23.8 | 25.8 (4) | 22.6 (7) | 23.8 (16) | Free agent | 5% | 1 / 3 |
| **Brice Sensabaugh** | UTAH | Jusuf Nurkic (29 Nov), Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec) | 8 | 22.8 | +11.8 | **25.0** | 18.8 | 29.0 (5) | 22.6 (9) | 18.8 (17) | Free agent | 6% | 1 / 3 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 35.6 | +8.0 | **25.0** | 23.8 | 38.0 (3) | 30.8 (5) | 23.8 (13) | Free agent | 6% | 1 / 3 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 20.6 | +4.8 | **24.8** | 21.6 | 23.8 (4) | 24.4 (8) | 21.6 (14) | Free agent | 1% | 1 / 3 |
| **Tristan da Silva** | ORL | Paolo Banchero (29 Nov) | 8 | 31.1 | +9.7 | **24.8** | 24.7 | 22.0 (4) | 23.5 (6) | 24.7 (13) | Free agent | 10% | 1 / 3 |
| **Javon Small** (out, ESPN est. back 23 Nov) | MEM | GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 4 | 24.0 | +3.0 | **24.2** | 23.4 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 2% | 1 / 4 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 5 | 21.2 | +8.9 | **23.4** | 16.8 | 23.4 (5) | 23.4 (5) | 16.8 (13) | Free agent | 1% | 1 / 3 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (23 Nov) | 10 | 25.0 | +3.0 | **23.3** | 26.9 | 17.8 (4) | 18.5 (6) | 26.9 (14) | Free agent | 27% | 1 / 4 |
| **Kenrich Williams** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.2 | +9.8 | **22.6** | 18.6 | 31.2 (4) | 22.6 (8) | 19.3 (15) | Free agent | 1% | 1 / 3 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 25.8 | +7.1 | **22.2** | 16.1 | 25.5 (4) | 21.0 (7) | 16.1 (15) | Free agent | 1% | 1 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 9 | 22.4 | — | **22.0** | 19.1 | 19.0 (4) | 20.7 (7) | 19.1 (11) | Free agent | 0% | 1 / 3 |
| **Pete Nance** | MIL | Ousmane Dieng (14 Dec) | 1 | 28.0 | +24.0 | **22.0** | 13.5 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% | 1 / 4 |
| **Bennett Stirtz** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 20.1 | — | **20.7** | 15.5 | 16.5 (4) | 19.6 (8) | 16.5 (15) | Free agent | 1% | 1 / 3 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 8 | 27.1 | +5.6 | **20.5** | 19.4 | 20.0 (4) | 20.5 (8) | 19.4 (15) | Free agent | 1% | 1 / 4 |
| **Nic Claxton** | CHI | Caleb Wilson (13 Dec) | 4 | 22.5 | +5.5 | **20.5** | 23.3 | 20.5 (4) | 23.3 (6) | 23.3 (6) | Free agent | 40% | 1 / 3 |
| **Kel'el Ware** | MIL | Ousmane Dieng (14 Dec) | 5 | 19.6 | +3.2 | **20.2** | 22.9 | 26.8 (4) | 20.6 (8) | 22.9 (16) | Free agent | 52% | 1 / 4 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 6 | 30.6 | — | 14.5 (4) | 30.6 (9) | 39.0 | 36.5 | Free agent | 76% | 1 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 10 | 33.8 | — | — | 33.8 (4) | 37.5 | 36.0 | Free agent | 80% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 8 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 1 / 3 |
| **Grayson Allen** | CHA | Concussion | 23 Nov | 2 | 26.8 | 26.0 (1) | 29.0 (4) | 26.8 (13) | 26.6 | 31.2 | Free agent | 21% | 0 / 3 |
| **P.J. Washington** | DAL | Shoulder | 21 Nov | 0 | 28.2 | 29.3 (3) | 28.3 (7) | 28.2 (15) | 26.9 | 30.6 | Free agent | 33% | 2 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 4 | 14.2 | — | — | 14.2 (5) | 30.6 | 27.1 | Free agent | 8% | 1 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 12 | — | — | — | — | 30.1 | 28.0 | Free agent | 40% | 1 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 6 | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | 21.6 | 23.1 | Free agent | 40% | 1 / 3 |
| **Jerami Grant** | MEM | Left Calf | 21 Nov | 0 | 20.3 | 18.2 (4) → 23.7 (3) | 21.7 (7) → 25.0 (6) | 20.3 (15) → 21.6 (14) | 27.0 | 28.8 | Free agent | 9% | 1 / 4 |
| **Draymond Green** | GS | Rest | 22 Nov | 1 | 24.0 | 20.7 (3) | 26.0 (7) | 24.0 (13) | 28.5 | 26.5 | Free agent | 23% | 1 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 23 Nov | 2 | 19.2 | 28.0 (2) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 2% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 4 | — | — | — | — | — | 28.1 | Free agent | 2% | 1 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 6 | 8.8 | -3.0 (1) | 3.2 (4) | 8.8 (12) | 25.1 | 27.6 | Free agent | 6% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 6 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 2 / 2 |
| **Precious Achiuwa** | SAC | Left Lower Leg Bruise | 21 Nov | 0 | 25.4 | -3.0 (1) | 14.8 (4) | 25.4 (12) | 24.1 | 27.0 | Free agent | 14% | 1 / 3 |
| **Jock Landale** | ATL | Right Hip Inflammation | 22 Nov | 1 | 16.8 | 19.0 (1) | 18.0 (2) | 16.8 (9) → 18.9 (8) | — | 25.8 | Free agent | 0% | 1 / 2 |
| **Collin Murray-Boyles** | TOR | Concussion | 23 Nov | 2 | 24.0 | 21.0 (3) | 27.5 (6) | 24.0 (14) | 24.8 | 25.6 | Free agent | 12% | 0 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 8 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 1 / 4 |
| **T.J. McConnell** | IND | Left Hamstring | 22 Nov | 1 | 20.0 | 23.5 (4) | 20.0 (7) | 20.0 (7) | 24.4 | 25.5 | Free agent | 8% | 1 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.7.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Brandon Ingram** | LAC | Right Achilles Surgery | 23 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 67% | 1 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 4 | — (—) | 28.1 (74) | Free agent | 2% | 1 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 6 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 2 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 8 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 1 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 8 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 12 | 30.1 (30.5) | 28.0 (63) | Free agent | 40% | 1 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 42 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 1 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 42 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 1 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 74 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 101 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 1 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 132 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 1 / 4 |

## Our injured players

- **Jalen Smith** (CHI): Out, Illness; ESPN est. back 22 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 03 Dec.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 1 | 25.0 | +11.7 | 0 | **33.0** | 15.0 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% |
| Charles Bassey | C | 5 | 20.6 | +4.8 | 3 | **24.8** | 26.6 | 23.8 (4) | 24.4 (8) | 21.6 (14) | Free agent | 1% |
| Will Richard | SG/SF | 5 | 25.8 | +7.1 | 1 | **22.2** | 15.0 | 25.5 (4) | 21.0 (7) | 16.1 (15) | Free agent | 1% |
| LJ Cryer | PG | 5 | 16.2 | +6.2 | 2 | **14.8** | 8.2 | 18.8 (4) | 15.6 (7) | 10.8 (13) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |
| Jusuf Nurkic | Right Foot Strain | 29 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 8 | 22.8 | +7.8 | 3 | **30.6** | 28.0 | 35.8 (5) | 30.6 (8) | 29.3 (13) | Waivers | 21% |
| Brice Sensabaugh | SG/SF | 8 | 22.8 | +11.8 | 0 | **25.0** | 7.5 | 29.0 (5) | 22.6 (9) | 18.8 (17) | Free agent | 6% |
| Svi Mykhailiuk | SG | 8 | 21.2 | +5.8 | 0 | **15.0** | 5.0 | 19.8 (5) | 13.2 (9) | 11.5 (17) | Free agent | 0% |
| Isaiah Collier | PG | 5 | 15.6 | +7.6 | 0 | **14.4** | 5.0 | 8.5 (2) | 13.7 (6) | 14.1 (14) | Free agent | 2% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 25.1 | — | 6 | **35.5** | — | 42.0 (4) | 37.2 (8) | 30.5 (15) | Free agent | 27% |
| Kenrich Williams | SF | 10 | 25.2 | +9.8 | 7 | **22.6** | 14.2 | 31.2 (4) | 22.6 (8) | 19.3 (15) | Free agent | 1% |
| Bennett Stirtz | PG | 10 | 20.1 | — | 0 | **20.7** | — | 16.5 (4) | 19.6 (8) | 16.5 (15) | Free agent | 1% |
| Micah Peavy | SF | 8 | 17.2 | — | 0 | **11.6** | — | 9.5 (2) | 10.2 (6) | 9.6 (10) | Free agent | 0% |
| 5105800 |  | 5 | 13.0 | — | 0 | **6.4** | — | — | — | — | — | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 8 | 27.1 | +5.6 | 6 | **20.5** | 20.5 | 20.0 (4) | 20.5 (8) | 19.4 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | +8.8 | 0 | **16.7** | 5.5 | — | 16.7 (3) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 5 | 15.6 | — | 2 | **10.8** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 23.4 | — | 3 | **25.6** | — | 25.8 (4) | 22.6 (7) | 23.8 (16) | Free agent | 5% |
| Braden Smith | PG | 7 | 16.9 | — | 4 | **21.0** | — | 25.5 (2) | 14.8 (4) | 15.2 (10) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.4 | — | 1 | **17.1** | — | 17.5 (4) | 15.8 (6) | 14.9 (14) | Free agent | 0% |
| Jay Huff | C | 9 | 14.9 | — | 2 | **13.8** | — | 13.8 (4) | 11.0 (6) | 14.9 (14) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Allen Graves | SF | 2 | 32.0 | +18.2 | 1 | **40.0** | 10.0 | 26.5 (4) | 18.2 (8) | 16.4 (16) | Free agent | 1% |
| Jakob Poeltl | C | 2 | 30.5 | +5.8 | 2 | **37.5** | 30.4 | 28.5 (4) | 33.4 (8) | 26.4 (14) | Free agent | 37% |
| Jamison Battle | SF | 2 | 26.5 | +7.1 | 1 | **26.0** | 13.5 | 13.0 (4) | 16.5 (8) | 15.4 (16) | Free agent | 0% |
| Trayce Jackson-Davis | PF | 2 | 16.5 | +9.8 | 0 | **21.0** | 12.3 | 21.0 (2) | 22.3 (3) | 13.7 (11) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaden McDaniels | SF/PF | 10 | 34.7 | +3.0 | 10 | **38.3** | 29.7 | 44.8 (4) | 42.3 (7) | 38.6 (16) | Melbourne poopoo | 91% |
| Ayo Dosunmu | PG/SG | 10 | 33.9 | +4.5 | 10 | **37.7** | 30.4 | 29.0 (4) | 32.1 (7) | 34.8 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 31.9 | +4.6 | 9 | **28.0** | 26.3 | 26.0 (3) | 23.0 (6) | 28.9 (15) | Dr White Slong | 60% |
| Joan Beringer | C | 10 | 17.4 | — | 1 | **18.8** | — | 15.5 (4) | 16.4 (7) | 19.3 (16) | Free agent | 2% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 7 | 18.3 | +5.2 | 0 | **14.7** | 9.4 | 3.0 (1) | 12.0 (4) | 11.9 (12) | Free agent | 0% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 1 | 33.0 | +4.7 | 1 | **59.0** | 72.0 | 60.0 (4) | 66.9 (8) | 70.8 (15) | Cream Abdul-Yammar | 100% |
| Stephon Castle | PG/SG | 1 | 33.0 | +3.8 | 1 | **59.0** | 34.0 | 48.0 (4) | 37.8 (8) | 35.1 (15) | Melbourne poopoo | 96% |
| Devin Vassell | SG/SF | 1 | 32.0 | +3.4 | 1 | **42.0** | 24.9 | 25.8 (4) | 29.5 (6) | 29.0 (13) | Team Nic Kerr | 40% |
| Julian Champagnie | SF/PF | 1 | 29.0 | +4.0 | 1 | **29.0** | 19.7 | 21.8 (4) | 23.0 (8) | 23.2 (15) | Free agent | 41% |
| De'Aaron Fox | PG/SG | 1 | 32.0 | +5.2 | 1 | **17.0** | 24.9 | 12.7 (3) | 24.7 (7) | 29.6 (14) | Matt Wright's Foxies | 94% |

### CLE

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Evan Mobley | Left Toe Sprain | 29 Nov | 33.3 | 39.9 | Matt Wright's Foxies |
| Nae'Qwan Tomlin | Back | 29 Nov | 15.7 | 15.5 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| James Harden | PG/SG | 4 | 36.2 | +4.9 | 4 | **50.2** | 30.6 | 50.2 (4) | 39.2 (8) | 36.1 (16) | Team Nic Kerr | 99% |
| Jarrett Allen | C | 4 | 30.8 | +11.4 | 4 | **34.0** | 25.0 | 34.0 (4) | 35.2 (6) | 34.5 (14) → 37.2 (13) | Dr White Slong | 89% |
| Tyrese Proctor | SG | 5 | 28.0 | +6.0 | 4 | **33.4** | 19.0 | 33.4 (5) | 27.0 (9) | 21.8 (16) | Free agent | 10% |
| Jaylon Tyson (out, ESPN est. back 23 Nov) | SG/SF | 2 | 32.0 | +9.0 | 2 | **28.0** | 5.0 | 28.0 (2) | 20.3 (3) | 19.2 (8) | Free agent | 2% |
| Thomas Bryant | C | 5 | 17.8 | +3.1 | 1 | **24.2** | 16.8 | 24.2 (5) | 22.8 (8) | 19.1 (11) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 23 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 10 | 25.0 | +3.0 | 9 | **23.3** | 20.0 | 17.8 (4) | 18.5 (6) | 26.9 (14) | Free agent | 27% |
| Kobe Sanders | SG | 10 | 22.5 | — | 1 | **17.2** | — | 11.2 (4) | 13.5 (6) | 17.5 (14) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Kingston Flemings (back strain; ESPN est. 22 Nov), Jock Landale (right hip inflammation; ESPN est. 22 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 2 | 36.0 | +4.5 | 2 | **49.0** | 42.6 | 40.8 (4) | 48.1 (7) | 41.8 (16) | Snow Time Lakers | 96% |
| Onyeka Okongwu | C | 2 | 35.0 | +3.0 | 2 | **35.5** | 40.8 | 38.2 (4) | 41.0 (7) | 36.8 (16) | Cream Abdul-Yammar | 87% |
| Aaron Wiggins | SG/SF | 2 | 30.0 | +4.5 | 2 | **30.5** | 22.6 | 22.2 (4) | 26.4 (7) | 26.7 (16) | Free agent | 34% |
| Corey Kispert | SG/SF | 2 | 16.5 | +3.9 | 0 | **17.0** | 14.4 | 20.3 (3) | 18.0 (4) | 14.9 (9) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.7 | +5.3 | 10 | **36.6** | 30.2 | 33.8 (4) | 35.9 (9) | 34.6 (17) | Snow Time Lakers | 80% |

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 29 Nov | 35.2 | 47.0 | Dr White Slong |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 10 | 37.9 | +3.9 | 10 | **55.6** | 38.6 | 63.5 (4) | 60.2 (8) | 49.0 (15) | Cream Abdul-Yammar | 96% |
| Anthony Black | PG/SG | 9 | 35.3 | +6.4 | 9 | **39.1** | 28.2 | 32.0 (4) | 39.4 (8) | 38.3 (12) | **us** | 69% |
| Wendell Carter Jr. | C | 10 | 32.9 | +7.5 | 10 | **30.9** | 23.0 | 27.0 (4) | 33.9 (8) | 32.3 (15) | Dr White Slong | 57% |
| Tristan da Silva | SF/PF | 8 | 31.1 | +9.7 | 2 | **24.8** | 17.2 | 22.0 (4) | 23.5 (6) | 24.7 (13) | Free agent | 10% |
| Jase Richardson | SG | 6 | 24.3 | +13.4 | 4 | **15.7** | 8.6 | — | 16.2 (4) | 15.3 (11) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Miller | SG/SF | 7 | 29.1 | +3.1 | 7 | **28.0** | 2.0 | 27.3 (3) | 23.5 (4) | 29.8 (13) | Matt Wright's Foxies | 86% |
| Royce O'Neale | SF/PF | 9 | 22.6 | +4.6 | 0 | **14.7** | 9.0 | 14.7 (3) | 16.2 (6) | 12.9 (15) | Free agent | 1% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 3 | 29.0 | +9.0 | 2 | **14.0** | 17.0 | — | — | 19.1 (9) | Free agent | 3% |
| Christian Anderson | PG | 9 | 15.9 | — | 0 | **13.4** | — | 19.3 (3) | 15.2 (6) | 10.0 (14) | Free agent | 0% |
| Tidjane Salaun | PF | 9 | 13.3 | +3.3 | 0 | **10.4** | 13.0 | 3.7 (3) | 9.3 (6) | 11.6 (14) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Norman Powell | SG/SF | 5 | 30.6 | +3.3 | 5 | **36.2** | 16.3 | 36.2 (5) | 36.2 (5) | 30.1 (13) → 32.2 (12) | Matt Wright's Foxies | 81% |
| Isaac Okoro | SG/SF | 5 | 31.6 | +11.2 | 5 | **29.4** | 10.4 | 29.4 (5) | 24.6 (7) | 16.6 (15) | Free agent | 2% |
| Buddy Hield | SG/SF | 5 | 21.2 | +8.9 | 0 | **23.4** | 15.7 | 23.4 (5) | 23.4 (5) | 16.8 (13) | Free agent | 1% |
| Nic Claxton | C | 4 | 22.5 | +5.5 | 1 | **20.5** | 29.0 | 20.5 (4) | 23.3 (6) | 23.3 (6) | Free agent | 40% |
| Zach Collins | C | 3 | 18.0 | +10.8 | 1 | **18.0** | 6.0 | 18.7 (3) | 15.5 (4) | 9.4 (10) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 22.3 | — | 0 | **28.5** | — | 27.8 (4) | 28.5 (6) | 26.6 (11) | Free agent | 3% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 24 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 30.8 | +12.8 | 9 | **41.8** | 45.0 | 45.8 (4) | 44.4 (7) | 38.1 (13) | Lauri Birds | 83% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 6 | 32.8 | +15.8 | 6 | **33.8** | 13.0 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 40% |
| Paul Reed | PF/C | 9 | 26.8 | +3.8 | 4 | **31.4** | 25.0 | 35.5 (4) | 32.6 (7) | 33.7 (14) | Lauri Birds | 36% |
| Javonte Green | SF | 9 | 20.1 | +8.1 | 1 | **17.6** | 5.0 | 19.0 (4) | 18.0 (7) | 14.9 (14) | Free agent | 0% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cam Spencer | PG/SG | 4 | 26.8 | +3.8 | 3 | **33.2** | 29.8 | 37.6 (5) | 31.4 (8) | 29.9 (16) | Lauri Birds | 36% |
| Javon Small (out, ESPN est. back 23 Nov) | PG | 4 | 24.0 | +3.0 | 0 | **24.2** | 25.0 | 29.2 (5) | 24.6 (8) | 23.4 (9) | Free agent | 2% |
| Olivier-Maxence Prosper | PF | 4 | 16.8 | +9.2 | 0 | **13.2** | 10.2 | 16.0 (5) | 11.9 (7) | 10.4 (10) | Free agent | 0% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 36.7 | +6.1 | 10 | **42.8** | 30.4 | 35.0 (4) | 41.6 (7) | 39.7 (15) | Team Nic Kerr | 91% |
| De'Andre Hunter | SF/PF | 8 | 35.6 | +8.0 | 8 | **25.0** | 23.9 | 38.0 (3) | 30.8 (5) | 23.8 (13) | Free agent | 6% |
| Leaky Black | SF | 9 | 22.4 | — | 1 | **22.0** | — | 19.0 (4) | 20.7 (7) | 19.1 (11) | Free agent | 0% |
| Dylan Cardwell | C | 8 | 16.1 | — | 2 | **18.5** | — | 15.2 (4) | 18.4 (7) | 18.5 (8) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 16.8 | — | 0 | **12.2** | — | 11.8 (4) | 11.4 (7) | 10.6 (15) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brayden Burries | SG | 5 | 29.2 | +5.4 | 5 | **32.8** | 19.4 | 26.5 (4) | 28.2 (8) | 22.8 (16) | Free agent | 10% |
| Kasparas Jakucionis | PG | 5 | 21.2 | +9.7 | 0 | **31.6** | 9.0 | 44.7 (3) | 24.6 (7) | 20.4 (15) | Free agent | 10% |
| Pete Nance | PF | 1 | 28.0 | +24.0 | 1 | **22.0** | 5.0 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% |
| Kel'el Ware | C | 5 | 19.6 | +3.2 | 1 | **20.2** | 17.8 | 26.8 (4) | 20.6 (8) | 22.9 (16) | Free agent | 52% |
| AJ Green | SG | 4 | 17.0 | +4.6 | 0 | **14.2** | 6.8 | 5.7 (3) | 7.6 (7) | 11.0 (15) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 32.7 | +5.2 | 10 | **34.5** | 23.1 | 41.0 (4) | 32.9 (7) | 32.8 (14) | Waivers | 46% |
| Trevon Brazile | SF/PF | 10 | 16.2 | — | 0 | **14.4** | — | 10.8 (4) | 11.7 (7) | 16.7 (14) | Free agent | 2% |
| Spencer Jones | SF/PF | 7 | 17.9 | — | 0 | **10.1** | — | 7.8 (4) | 10.1 (7) | 10.1 (7) | Free agent | 0% |

## Every injury

All 107 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 314 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 314 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 222 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 132 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 132 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 116 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 101 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 101 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 101 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 101 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 96 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 74 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 71 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 58 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 52 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 44 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 42 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 42 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 42 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 42 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 42 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 30 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 28 | Free agent |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 23 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 23 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 22 | Lauri Birds |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 22 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 22 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 22 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 22 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 21 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 21 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 21 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 12 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 12 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 12 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 12 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 10 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 10 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 10 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 8 | Dr White Slong |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 8 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 8 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 8 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 8 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 8 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 8 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 8 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 6 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 6 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 6 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 6 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 6 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 6 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 6 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 27 Nov | 6 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 6 | Free agent |
| Tobe Awaka | CHI | Out | Back | 25 Nov | 4 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 4 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 4 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 4 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 3 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 3 | **us** |
| Ryan Dunn | PHX | Out | Right Quadriceps | 23 Nov | 2 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 2 | — |
| Jaylon Tyson | CLE | Out | Right Ankle | 23 Nov | 2 | Free agent |
| Jaylen Brown | PHI | Out | Left Hamstring | 23 Nov | 2 | Snow Time Lakers |
| Javon Small | MEM | Out | Personal | 23 Nov | 2 | Free agent |
| Grayson Allen | CHA | Out | Concussion | 23 Nov | 2 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 23 Nov | 2 | Free agent |
| Grant Nelson | BKN | Out | Right Ankle Sprain | 23 Nov | 2 | — |
| Dean Wade | PHI | Out | Left Hamstring Soreness | 23 Nov | 2 | Free agent |
| Collin Murray-Boyles | TOR | Out | Concussion | 23 Nov | 2 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 23 Nov | 2 | Free agent |
| Cameron Boozer | MEM | Out | Ankle | 23 Nov | 2 | Lauri Birds |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 23 Nov | 2 | Melbourne poopoo |
| Austin Reaves | LAL | Out | Left Heel Bruise | 23 Nov | 2 | Cream Abdul-Yammar |
| Adem Bona | PHI | Out | Back Sprain | 23 Nov | 2 | Free agent |
| T.J. McConnell | IND | Out | Left Hamstring | 22 Nov | 1 | Free agent |
| Ronald Holland II | DET | Out | Left Knee Bruise | 22 Nov | 1 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 22 Nov | 1 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Soreness | 22 Nov | 1 | Free agent |
| Myron Gardner | MIA | Day-To-Day | Hamstring | 22 Nov | 1 | Free agent |
| Kingston Flemings | ATL | Out | Back Strain | 22 Nov | 1 | Free agent |
| Jordan Clarkson | NY | Out | Right Foot Plantar Fasciitis | 22 Nov | 1 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 22 Nov | 1 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 22 Nov | 1 | Free agent |
| Jalen Smith | CHI | Out | Illness | 22 Nov | 1 | **us** |
| Felix Okpara | WSH | Out | Back Strain | 22 Nov | 1 | Free agent |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 22 Nov | 1 | Free agent |
| Draymond Green | GS | Day-To-Day | Rest | 22 Nov | 1 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring Strain | 22 Nov | 1 | Free agent |
| Alex Caruso | OKC | Out | Right Hip Soreness | 22 Nov | 1 | Free agent |
| Walter Clayton Jr. | DAL | Day-To-Day | Knee | 21 Nov | 0 | Free agent |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 21 Nov | 0 | Free agent |
| Tyrese Maxey | PHI | Day-To-Day | Right Foot Soreness | 21 Nov | 0 | Team Nic Kerr |
| Ty Jerome | MEM | Out | Right Hip | 21 Nov | 0 | Melbourne poopoo |
| Tobi Lawal | DAL | Day-To-Day | Right Groin | 21 Nov | 0 | Free agent |
| Precious Achiuwa | SAC | Out | Left Lower Leg Bruise | 21 Nov | 0 | Free agent |
| P.J. Washington | DAL | Day-To-Day | Shoulder | 21 Nov | 0 | Free agent |
| OG Anunoby | NY | Day-To-Day | Calf | 21 Nov | 0 | Cream Abdul-Yammar |
| Jerami Grant | MEM | Day-To-Day | Left Calf | 21 Nov | 0 | Free agent |
| Jayson Tatum | BOS | Day-To-Day | Rest | 21 Nov | 0 | Snow Time Lakers |
| Dominick Barlow | PHI | Out | Back Fracture | 21 Nov | 0 | Free agent |
| Derrick White | BOS | Day-To-Day | Left Shoulder | 21 Nov | 0 | Dr White Slong |
| Deni Avdija | POR | Day-To-Day | Foot | 21 Nov | 0 | Snow Time Lakers |
| Nolan Traore | BKN | Out | Right Hamstring | 20 Nov | -1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-21 07:21 UTC.
- **Research, 21 Nov:** [TSN, 18 Nov](https://www.tsn.ca/nba/article/raptors-leonard-dealing-with-left-patellar-tendinopathy/) · [TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/) · [Sportsnet via BVM Sports, 20 Nov](https://bvmsports.com/2026/11/20/report-raptors-kawhi-leonard-out-at-least-two-more-weeks/) · [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/rj-barrett-hamstring-out-at-least-two-weeks) · [NBA injury report, 20 Nov 7:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-20_07_30PM.pdf) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/raptors-start-iq-walter-barnes-graves-poeltl) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-allen-graves-records-first-career-double-double/) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/allen-graves-news-earns-first-career-start-friday-540227) · [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/collin-murray-boyles-placed-in-concussion-protocol) · [NBC Sports, 20 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-20/allen-graves-records-double-double-in-first-start) · [AP via Yahoo, 31 Oct](https://sports.yahoo.com/articles/chet-holmgren-least-2-months-011311180.html) · [Heavy, 20 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-pelicans-november-20/) · [OKC Thunder Wire via Yahoo, 28 Oct](https://sports.yahoo.com/articles/jalen-williams-leg-surgery-evaluated-234119739.html) · [Denver Gazette, 16 Oct](https://www.denvergazette.com/2026/10/16/nuggets-provide-update-on-julian-strawthers-knee-injury-5/) · [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/nuggets-wing-julian-strawther-out-indefinitely-due-to-left-knee-sprain) · [Nuggets On SI, 20 Nov](https://www.si.com/nba/nuggets/onsi/nuggets-could-get-huge-boost-vs-rockets-with-lopsided-injury-report) · [NBC Sports via Yahoo, 19 Nov](https://sports.yahoo.com/articles/2026-27-nba-minutes-report-161955518.html) · [Denver Gazette, 20 Nov](https://www.denvergazette.com/2026/11/20/christian-braun-comes-up-big-on-both-ends-as-nuggets-beat-rockets/) · [Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html) · [MLive via Yahoo, 20 Nov](https://sports.yahoo.com/articles/pistons-veteran-undergoes-knee-surgery-233137937.html) · [HoopsHype via Yahoo, 17 Nov](https://sports.yahoo.com/articles/duncan-robinson-left-quad-strain-172952431.html) · [NBC Sports player news, 17–20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/taurean-prince-injury-has-no-return-timeline-540207) · [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/mobley-toe-to-be-re-evaluated-in-7-10-days) · [CBS/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-naeqwan-tomlin-still-out-wednesday/) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jaylon-tyson-out-for-friday/) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/tyrese-proctor-news-downward-trend-continues-540279) · [Heavy via Yahoo, 13 Nov](https://sports.yahoo.com/articles/warriors-announce-official-stephen-curry-203906999.html) · [AP via ABC News, 19 Nov](https://abcnews.com/Sports/wireStory/grizzlies-roll-past-short-handed-warriors-126-98-138311394) · [Heavy via Yahoo, 22 Oct](https://sports.yahoo.com/articles/kristaps-porzingis-coming-back-warriors-035243404.html) · [Roundtable via Yahoo, 19 Nov](https://sports.yahoo.com/articles/warriors-vs-grizzlies-injury-report-193903602.html) · [CBS/RotoWire, 16 Oct](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/) · [Heavy via Yahoo, 5 Nov](https://sports.yahoo.com/articles/jimmy-butler-return-steve-kerr-143904723.html) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-draymond-green-available-wednesday/) · [NBA injury report, 21 Nov 2:15 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-21_02_15AM.pdf) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/warriors-brandon-williams-advances-to-on-court-activities/) · [Warriors On SI, 18 Nov](https://www.si.com/nba/warriors/onsi/warriors-announce-injury-update-on-brandon-williams-hamstring-01m7qtgye3c1) · [Heavy via Yahoo, 11 Nov](https://sports.yahoo.com/articles/warriors-encouraging-brandon-williams-injury-010221980.html) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-jalen-smith-out-sick-friday/) · [AP via Yahoo, 21 Nov](https://sports.yahoo.com/articles/bulls-rookie-caleb-wilson-looking-012217305.html) · [iHeart/Fox Sports 1070, 21 Nov](https://foxsports1070.iheart.com/content/2026-11-21-bucks-vs-76ers-injury-report-nov-21/) · [FS Roundup box, 19 Nov](https://www.fsroundup.com/nba/game/portland-trail-blazers-at-milwaukee-bucks-2026-11-19) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-defensive-activity-offsets-cold-shooting/) · [RotoWire, 9 Nov](https://www.rotowire.com/basketball/headlines/brayden-burries-news-holding-down-starting-job-538340) · [Deseret News, 11 Nov](https://www.deseret.com/sports/2026/11/11/lauri-markkanen-diagnosed-with-two-nondisplaced-fractures-in-his-right-hand/) · [NBA.com, 27 Oct](https://www.nba.com/news/jaren-jackson-jr-torn-mcl-october-2026) · [Utah Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-jusuf-nurkic-will-be-re-evaluated-in-one-week/) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-brice-sensabaugh-dazzles-with-4011-double-double/) · [CBS Sports game log, 20 Nov](https://www.cbssports.com/nba/players/28951832/brice-sensabaugh/fantasy/) · [Orlando Sentinel via Yahoo, 19 Nov](https://sports.yahoo.com/articles/magic-star-paolo-banchero-shares-110000466.html) · [Heavy, 24 Oct](https://heavy.com/sports/nba/orlando-magic/orlando-magic-concerning-update-paolo-banchero/) · [ClutchPoints via Yahoo, 19 Nov](https://sports.yahoo.com/articles/spurs-official-dylan-harper-injury-211450331.html) · [San Antonio Express-News via Yahoo, 17 Nov](https://sports.yahoo.com/articles/mitch-johnson-reiterates-spurs-taking-030657990.html) · [NBC Sports, 19 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-19/julian-champagnie-has-20-points-four-threes-in-win) · [Heavy via Yahoo, 18 Nov](https://sports.yahoo.com/articles/spurs-coach-mitch-johnson-shares-052207832.html) · [NBA.com, 18 Nov](https://www.nba.com/news/hawks-cj-mccollum-to-miss-at-least-four-weeks-with-left-calf-strain) · [Last Word on Sports via Yahoo, 13 Nov](https://sports.yahoo.com/articles/atlanta-hawks-mouhamed-gueye-4-130022920.html) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/kingston-flemings-injury-ruled-out-for-friday-540201) · [Roundtable via Yahoo, 20 Nov](https://sports.yahoo.com/articles/hornets-visit-hawks-nba-cup-162833711.html) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/hawks-aaron-wiggins-entering-starting-lineup-wednesday/) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/aaron-wiggins-scores-19-points-as-starter) · [ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/atl) · [Roundtable via Yahoo, 20 Nov](https://sports.yahoo.com/articles/lakers-vs-kings-injury-report-212255329.html) · [Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/lakers-coach-jj-redick-reveals-043347864.html) · [Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html) · [NBA.com box, 20 Nov](https://www.nba.com/bulls/game/0022600047-wizards-vs-bulls-chicago-il-11-20-2026) · [On Tap Sports Net, 20 Nov](https://ontapsportsnet.com/nba/chicago-bulls/bulls-wizards-recap-november-20-2026/) · [Jazz On SI via Yahoo, 4 Nov](https://sports.yahoo.com/articles/latest-jusuf-nurkic-status-good-193548714.html) · [Yahoo Sports, 20 Nov](https://sports.yahoo.com/articles/grizzlies-cam-boozer-jerami-grant-000744742.html) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/jerami-grant-out-with-calf-strain-against-t-wolves) · [SI All Mavericks, 20 Nov](https://www.si.com/nba/mavericks/onsi/dusty-may-provides-much-needed-injury-update-dallas-mavericks-center-dereck-lively-ii-) · [CBS/RotoWire player news, 17–20 Nov](https://www.cbssports.com/nba/players/28951880/dereck-lively-ii/) · [TSN, 19 Nov](https://www.tsn.ca/nba/article/raptors-barrett-hamstring-out-at-least-two-weeks-murray-boyles-enters-concussion-protocol/) · [NBC Sports, 18 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-18/raptors-start-iq-walter-battle-collin-poeltl) · [Heavy, 20 Nov](https://heavy.com/sports/nba/los-angeles-clippers/injury-report-vs-mavericks-november-21/) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/tj-mcconnell-injury-exits-game-with-hamstring-issue-540267) · [RotoWire, 20 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-set-for-season-debut-monday-540187) · [Fadeaway World, 20 Nov](https://fadeawayworld.net/nba/la-clippers/brandon-ingram-will-make-his-clippers-debut-next-week-after-achilles-surgery-recovery) · [Stadium Rant via Yahoo, 20 Nov](https://sports.yahoo.com/articles/jimmy-butler-g-league-plan-024212960.html)
