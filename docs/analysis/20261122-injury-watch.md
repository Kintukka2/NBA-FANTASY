# Injury Watch: 22 Nov 2026

- Generated 2026-11-22 07:27 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 110 players in ESPN's injury feed. 33 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 18 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

Pickups with a game on Sunday 22 Nov, the last day of this matchup (one add left):
- **Kevin Huerter** (DET, free agent): starting at 36 min while Duncan Robinson is out (re-evaluation about 24 Nov; *ESPN est.* 27 Nov). Season 23.9 (15), L7 30.0 (4), L15 32.6 (7), L30 24.9 (14); role rate 31.3 ‡. Sun at ATL. **This week's pick.**
- **Jaxson Hayes** (UTAH, free agent): off Utah's Sunday report and starting until Jusuf Nurkic is re-evaluated about 27 Nov (*ESPN est.* 29 Nov). Season 28.3 (14), L7 34.5 (2, small sample), L15 28.7 (7), L30 27.0 (13); role rate 30.2 ‡. Sun vs DAL.
- **Neemias Queta** (BOS, free agent): season 27.4 (15), L7 35.0 (3), L15 29.3 (7), L30 27.9 (14); rate 30.9. Sunday at GS is the second night of a back-to-back.

For next week:
- **Christian Braun** (DEN): a secure starter at 32–33 min (see the 21 Nov report).
- **Brayden Burries** (MIL): lost his start to Ryan Rollins on Saturday but kept his minutes.

## Research

Earlier notes still hold ([20261121-injury-watch.md](20261121-injury-watch.md)). New since then:

New since 21 Nov. The yesterday notes still hold where this says "unchanged". Sunday's first tip-off is DET@ATL at 3:30 PM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)), so a Sunday add must be in by **Mon 23 Nov 7:30 AM Melbourne**. No new name reached the top 10 of "Pickups for us": all ten were in the 21 Nov report.

**Absentees**

- **Jalen Duren (us, DET):** Out again Sun at ATL ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). Heavy says he and Duncan Robinson "are closer to returning, possibly later this week depending on their re-evaluations", with no date ([Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22)). The re-evaluation is still "next week" ([Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html)). No timetable reported. *ESPN est.* 24 Nov. The `return` floor of 24 Nov (first DET game Tue 24 at ORL) still holds.
- **Cade Cunningham (us, DET):** **Probable** for Sun at ATL with right knee soreness ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). He came back Fri 20 vs TOR after missing one game: 36 min, 23 pts (10-22 FG), 5 reb, 9 ast. Rotoworld expects a similar minutes load Sunday ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/cade-cunningham-knee-probable-sunday-vs-atl)). *ESPN est.* 22 Nov.
- **Duncan Robinson (DET):** **Out Sun at ATL** ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)), so his one game this week is gone. He is "closer to returning, possibly later this week", depending on the re-evaluation ([Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22)). The one-week re-evaluation from 17 Nov falls about 24 Nov ([HoopsHype via Yahoo, 17 Nov](https://sports.yahoo.com/articles/duncan-robinson-left-quad-strain-172952431.html)). *ESPN est.* 27 Nov.
- **Jalen Smith (us, CHI):** **Questionable** for Sun vs DEN with a gastrointestinal illness. He missed Fri ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf); [Heavy, 21 Nov](https://heavy.com/sports/nba/chicago-bulls/all-star-guard-bulls-nuggets-injury-report/)). No timetable reported. *ESPN est.* 22 Nov. If he sits, Nic Claxton is the likely starter at C, as on Fri ([On Tap Sports Net, 20 Nov](https://ontapsportsnet.com/nba/chicago-bulls/bulls-wizards-recap-november-20-2026/)).
- **Trey Murphy III (us, NO):** He came back Fri 20 at OKC from a six-game absence and played close to a full load: 29 min off the bench, 17 pts (5-10 FG), 4 reb, 2 stl, 1 blk. He then sat Sat vs SA, the second night of the back-to-back, with patellar tendinopathy in both knees. Saddiq Bey (us) is expected back in the starting five while he is out ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio)). No timetable reported. NO has no game Sun, and PHX, LAC and POR are next week (same source). *ESPN est.* 23 Nov.
- **Kawhi Leonard (us, IR):** Unchanged since 21 Nov. Charania reported at least two more weeks from 20 Nov, so about 4 Dec ([TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/)). The Raptors' next weekly update is due about 24 Nov ([Heavy via Yahoo, 18 Nov](https://sports.yahoo.com/articles/raptors-announce-kawhi-leonard-injury-013202112.html)). *ESPN est.* 3 Dec.
- **Kingston Flemings (ATL):** **Questionable** for Sun vs DET with a lumbar strain after three straight absences ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). RotoWire: if he is cleared, Aaron Wiggins "would likely go back to the second unit" ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/kingston-flemings-injury-questionable-for-sunday-540375)). *ESPN est.* 22 Nov.
- **Jock Landale (ATL):** Out Sun vs DET, now listed with a **right great toe sprain**. He missed Fri with right hip inflammation, the injury ESPN still lists ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf); [Roundtable via Yahoo, 22 Nov](https://sports.yahoo.com/articles/hawks-kingston-flemings-questionable-against-002113594.html)). No timetable reported. *ESPN est.* 27 Nov.
- **Collin Murray-Boyles (TOR):** Unchanged since 21 Nov. He is in concussion protocol with no timetable reported ([TSN, 19 Nov](https://www.tsn.ca/nba/article/raptors-barrett-hamstring-out-at-least-two-weeks-murray-boyles-enters-concussion-protocol/)). TOR's next game is Mon 23 vs MIL, and Toronto had not filed a report for it by 2:30 AM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). *ESPN est.* 23 Nov. His return is the first threat to Allen Graves's start.
- **Stephen Curry (GS):** Out Sun vs BOS with a right oblique tear ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). Kerr says he is back with the team and "in good spirits" but not cleared. An update is expected on Thanksgiving (26 Nov), and the consensus is that he will be out longer than the first two weeks ([Heavy via Yahoo, 22 Nov](https://sports.yahoo.com/articles/warriors-good-stephen-curry-news-043445397.html)). *ESPN est.* 12 Dec.
- **Brandon Williams (GS):** Saturday's re-evaluation did not clear him. He is **out Sun vs BOS**, and his next chance is Wed 25 Nov vs SAC ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brandon-williams-injury-wont-play-sunday-540428); [NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). His one game this week is gone. *ESPN est.* 25 Nov, which agrees.
- **Austin Reaves (LAL):** Unchanged since 21 Nov. Redick hopes he returns Mon 23 vs UTAH or Fri 27 at SA, but he has not been cleared ([Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/lakers-coach-jj-redick-reveals-043347864.html)). The Lakers had not filed for Monday by 2:30 AM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). *ESPN est.* 23 Nov.
- **Ousmane Dieng (MIL):** Unchanged. He is out after finger surgery on 16 Nov, and "there is no timetable for his return" ([Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/bucks-vs-76ers-injury-report-155845075.html)). No timetable reported. *ESPN est.* 14 Dec.
- **Caleb Wilson (CHI):** Out Sun vs DEN ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). Unchanged: he was doing cardio at shootaround, and the next update is expected 3 Dec ([Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20)). *ESPN est.* 13 Dec.
- **Evan Mobley (CLE):** Unchanged since 21 Nov. He gets 7–10 days of treatment from 16 Nov, then a re-evaluation about 23–26 Nov ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/mobley-toe-to-be-re-evaluated-in-7-10-days)). No result has been reported. CLE has no Sunday game. *ESPN est.* 29 Nov.

**Pickups with a Sunday game**

- **Aaron Wiggins (ATL, Sun vs DET, 1 / 2):** He started Wed and Fri, with 19 pts (7-12 FG, 4 3PM) Fri vs CHA ([NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/aaron-wiggins-scores-19-points-as-starter)). The start depends on Flemings, who is questionable Sunday (*ESPN est.* 22 Nov). If Flemings plays, Wiggins "would likely go back to the second unit" ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/kingston-flemings-injury-questionable-for-sunday-540375)).
  - **Form:** season 26.7, L7 24.3 (3), L15 26.4 (7), L30 26.6 (15). His 30.5 FP/g without the absentees rests on 2 games (**small sample**). After Sunday, ATL is idle until Fri 27 at BOS ([ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/atl)).
- **Isaac Okoro (CHI, Sun vs DEN, 1 / 3):** Still the starting SF. Fri vs WSH: started, 29 min, 9 pts, 7 reb ([NBA.com box, 20 Nov](https://www.nba.com/bulls/game/0022600047-wizards-vs-bulls-chicago-il-11-20-2026)). He holds the job until Caleb Wilson returns in December (*ESPN est.* 13 Dec) ([Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html)). No news since.
  - **Sunday:** Norman Powell is questionable with a right hamstring strain (no timetable reported, *ESPN est.* 22 Nov). If he sits, RotoWire names Buddy Hield and Tre Jones, not Okoro, for the extra time ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-questionable-to-play-sunday/)).
  - **Form:** season 16.6, L7 29.8 (4), L15 24.6 (7), L30 17.4 (14). L7 is +13.2 because of the starter's minutes: 31.6 in games without Wilson, +11.2 on the games with him (the report's split).
- **Quenton Jackson (IND, Sun at NYK, 1 / 3):** T.J. McConnell is out Sunday (*ESPN est.* 23 Nov) and Pascal Siakam is questionable with hip soreness (no timetable reported, *ESPN est.* 22 Nov) ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). Rotoworld says Jackson's minutes "should increase while McConnell is out". Andrew Nembhard returned 20 Nov, so Jackson stays a bench guard ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/t-j-mcconnell-hamstring-out-sunday-vs-new-york)).
  - **Form:** season 23.8, L7 28.0 (3), L15 22.6 (7), L30 23.6 (15). IND also hosts OKC Mon 23.
- **Brice Sensabaugh (UTAH, Sun vs DAL, 1 / 3):** Bench scorer. Fri vs PHX: 18 pts (6-13 FG, 5-7 3PT) in 26 min off the bench ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brice-sensabaugh-news-drop-18-points-with-second-unit-540292)).
  - **Form:** season 18.8, L7 35.0 (4), L15 22.6 (9), L30 20.0 (16). L7 is +16.2, and most of it is his 40-point game on 17 Nov. His bench minutes grew with Markkanen (*ESPN est.* 4 Jan) and Jaren Jackson Jr. (*ESPN est.* 14 Dec) out ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-brice-sensabaugh-dazzles-with-4011-double-double/)). His minutes swing from 14 to 35.
- **Charles Bassey (GS, Sun vs BOS, 1 / 3):** 16 pts and 13 reb at MEM on 19 Nov ([CBS Sports, 19 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261119_GS@MEM/)). Draymond Green is off the injury report for Sunday. Rotoworld suggests Bassey could start in place of Gui Santos so that Green guards true centres less ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/draymond-green-elbow-removed-from-injury-report)).
  - **Form:** season 21.6, L7 26.0 (3), L15 24.1 (7), L30 21.6 (14).
- **Buddy Hield (CHI, Sun vs DEN, 1 / 3):** If Powell sits (questionable, *ESPN est.* 22 Nov), "Buddy Hield and Tre Jones could see more playing time" ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-questionable-to-play-sunday/)).
  - **Form:** season 16.8, L7 21.8 (4), L15 23.4 (5), L30 18.2 (12). L7 is +5.0. The report's split shows +8.9 min since Wilson's injury, but no news report on his form was found.
- **Nic Claxton (CHI, Sun vs DEN, 1 / 3):** He started at C on Fri while Jalen Smith was out ([On Tap Sports Net, 20 Nov](https://ontapsportsnet.com/nba/chicago-bulls/bulls-wizards-recap-november-20-2026/)). Smith is questionable again Sunday (*ESPN est.* 22 Nov) ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)).
  - **Form:** season 23.3, L7 22.3 (3), L15 23.3 (6), L30 23.3 (6). L15 and L30 equal the season because he has played 6 games.
- **Bennett Stirtz (OKC, Sun at MIA, 1 / 3):** He scored 18 pts Fri vs NO with Alex Caruso out. Caruso is out again Sunday with hip soreness (no timetable reported, *ESPN est.* 23 Nov) ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/alex-caruso-hip-remains-out-sunday-vs-miami)). Shai Gilgeous-Alexander is questionable with a low back contusion and neck strain (*ESPN est.* 22 Nov) ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)).
  - **Form:** season 15.5, L7 19.7 (3), L15 19.6 (8), L30 16.5 (15).
- **Kenrich Williams (OKC, Sun at MIA, 1 / 3):** He is not on OKC's injury report. Heavy lists him with Stirtz and Nique Clifford as players who "have also stepped up when needed" ([Heavy, 21 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-heat-november-22/)).
  - **Form:** season 18.6, L7 30.0 (3), L15 22.6 (8), L30 19.3 (15). L7 is +11.4 on 3 games, and no report explaining it was found.
- **Will Richard (GS, Sun vs BOS, 1 / 3):** 15 pts at MEM on 19 Nov ([CBS Sports, 19 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261119_GS@MEM/)).
  - **Form:** season 16.1, L7 30.0 (3), L15 21.2 (6), L30 15.5 (14). L7 is +13.9. Curry and B. Williams being out opened 25.8 min (+7.1) for him, but no role report was found. Green, who sat that game, is back Sunday ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/draymond-green-elbow-removed-from-injury-report)).

**Named pickups with no Sunday game** (MIL, SAC and PHX have 0 games left this week, so these are for next week)

- **Brayden Burries (MIL, 0 / 4):** **He lost his start on Sat at PHI.** Ryan Rollins started, ending Burries's run of 10 straight starts. Burries scored a career-high 26 pts (12-20 FG), with 8 reb, 4 ast and 1 blk, in 26 min off the bench. Rollins had 8 pts in 28 min. RotoWire expects Taylor Jenkins to keep trying "mix and match" lineups beside Tyler Herro ([RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brayden-burries-news-pours-in-career-high-26-on-saturday-540394); [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/brayden-burries-records-26-8-4-stat-line-vs-76ers)).
  - **Form:** season 24.5, L7 36.2 (4), L15 30.9 (9), L30 25.0 (16). L7 is +11.7. The cause is shot volume (second on the team in attempts Sat) and steals ([CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-defensive-activity-offsets-cold-shooting/)), not more minutes: he played 26–29. His next game is Mon 23 at TOR.
- **Kasparas Jakucionis (MIL, 0 / 4):** Only **10 min** Sat at PHI: 2 pts (1-6 FG, 0-4 3PT), 3 reb, 3 ast, 3 TO off the bench ([FS Roundup box, 21 Nov](https://www.fsroundup.com/nba/game/milwaukee-bucks-at-philadelphia-76ers-2026-11-21)).
  - **Form:** season 19.2, L7 34.0 (4), L15 21.8 (8), L30 18.6 (15). L7 is +14.8 from bigger bench minutes, including 25 pts in 26 min vs ATL on 15 Nov. That game came with Rollins out ill ([NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kasparas-jakucionis-scores-career-high-25-in-loss)). With Rollins back and starting, his minutes fell.
- **De'Andre Hunter (SAC, 0 / 3):** Started Sat vs BOS and scored 20 pts with 6 reb in a 97-96 win ([VAVEL, 22 Nov](https://www.vavel.com/en-us/nba/2026/11/21/1280226-celtics-vs-kings-live-score-updates-stream-info-and-results-in-nba-regular-season.html)). Fri at LAL: 30 pts (12-16 FG, 5-6 3PT) and 6 reb in 37 min ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-hits-for-season-high-30-points/)).
  - **Form:** season 24.4, L7 34.7 (3), L15 31.2 (6), L30 25.6 (13). L7 is +10.3 from heavy minutes (36.8 in games without the absentees, the report's split) and Friday's shooting. SAC's next game is Mon 23 vs SA ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)).
- **Jordan Goodwin (PHX, 0 / 4):** Bench guard who has not started in November. Fri at UTA: 28 min, 5 pts, 9 reb, 4 ast, 2 stl ([Basketball-Reference game log, read 22 Nov](https://www.basketball-reference.com/players/g/goodwjo01/gamelog/2027)).
  - **Form:** season 26.6, L7 27.8 (4), L15 28.5 (6), L30 28.0 (10). His next game is Mon 23 at NO ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)).

**Back soon**

- **P.J. Washington (DAL, 1 / 2):** He was listed with a shoulder issue, then ruled out Sat vs LAC with an illness, his first missed game. His next chance is Sun at UTA ([CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-p-j-washington-downgraded-to-out-540388/)). Dallas had not filed its Sunday report by 2:30 AM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). No timetable reported. *ESPN est.* 22 Nov.
  - **Form:** current 28.2, L7 29.3 (3), L15 28.3 (7), L30 29.2 (14).
- **Mitchell Robinson (BOS, 1 / 3):** A late addition to the report, out Sat at SAC with an illness ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/mitchell-robinson-illness-out-saturday-vs-sac)). Boston had not filed for Sun at GS by 2:30 AM ET ([NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf)). No timetable reported. *ESPN est.* 22 Nov.
  - **Form:** current 18.6, L7 15.7 (3), L15 20.3 (7), L30 18.6 (13). That is far below his 30.3 projection.
- **T.J. McConnell (IND):** Out Sun at NYK with soreness in the left hamstring, the other leg from the injury that delayed his season. Rotoworld expects the Pacers to be cautious ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/t-j-mcconnell-hamstring-out-sunday-vs-new-york)). No timetable reported. IND hosts OKC Mon 23. *ESPN est.* 23 Nov.
- **Dejounte Murray (NO):** No timetable reported, and ESPN's date is not a return. Charania reports he "will NOT play another minute" for New Orleans this season and will sit until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)). Nothing newer was found. *ESPN est.* 27 Nov.
- **Ja Morant (POR):** Still out on 21 Nov vs NYK. Heavy projects a return "later this month or in early December" ([Heavy, 21 Nov](https://heavy.com/sports/nba/portland-trail-blazers/injury-report-vs-knicks-november-21/)). The team's four-week re-evaluation falls about 27 Nov ([KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/)). The existing `return` row (28 Nov) holds. *ESPN est.* 1 Dec.
- **Grayson Allen (CHA):** He has concussion-like symptoms and was out Fri at ATL, his second straight absence. He is out until "cleared to return" ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/)). No timetable reported. CHA's next game is Mon 23 vs MEM. *ESPN est.* 23 Nov. His L7 of 26.0 rests on 1 game (**small sample**).
- **Scotty Pippen Jr. (MEM):** Out Sat at MIN with a lumbar disc herniation. He is "considered week-to-week" and has no re-evaluation date ([Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/11-players-listed-timberwolves-vs-180558689.html)). *ESPN est.* 25 Nov.
- **Bennedict Mathurin (NO):** Left plantar fasciitis, "week-to-week" after his fourth straight absence on 20 Nov ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)). No timetable reported. *ESPN est.* 27 Nov.
- **Maxime Raynaud (SAC):** Out again Sat vs BOS ([VAVEL, 22 Nov](https://www.vavel.com/en-us/nba/2026/11/21/1280226-celtics-vs-kings-live-score-updates-stream-info-and-results-in-nba-regular-season.html)). He is still week-to-week with no timeline ([CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)). *ESPN est.* 25 Nov.

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Matas Buzelis 24.8 (L7 33.5), Yves Missi 29.0 (L7 24.0), Saddiq Bey 29.4 (L7 29.6), Daniss Jenkins 30.1 (L7 32.2), Trey Murphy III 31.7 (L7 38.0). A pickup at or above **31.7** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Allen Graves** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 32.0 | +18.2 | **40.0** | 16.4 | 26.5 (4) | 18.2 (8) | 15.6 (15) | Free agent | 1% | 0 / 3 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 5 | 29.2 | +5.4 | **40.0** | 24.5 | 36.2 (4) | 30.9 (9) | 25.0 (16) | Free agent | 11% | 0 / 4 |
| **Jakob Poeltl** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 30.5 | +5.8 | **37.5** | 26.4 | 28.5 (4) | 33.4 (8) | 27.2 (13) | Free agent | 37% | 0 / 3 |
| **Duncan Robinson** (out, ESPN est. back 27 Nov) | DET | Taurean Prince (13 Dec); also out: Jalen Duren (24 Nov) | 6 | 32.8 | +15.8 | **33.8** | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 39% | 1 / 3 |
| **Brandon Williams** (out, ESPN est. back 25 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +11.7 | **33.0** | 18.8 | — | 10.5 (2) | 17.7 (9) | Free agent | 1% | 1 / 3 |
| **Aaron Wiggins** | ATL | CJ McCollum (19 Dec), Mouhamed Gueye (12 Dec); also out: Kingston Flemings (22 Nov), Jock Landale (27 Nov) | 2 | 30.0 | +4.5 | **30.5** | 26.7 | 24.3 (3) | 26.4 (7) | 26.6 (15) | Free agent | 34% | 1 / 2 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 5 | 31.6 | +11.2 | **29.4** | 16.6 | 29.8 (4) | 24.6 (7) | 17.4 (14) | Free agent | 2% | 1 / 3 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 5 | 18.8 | +7.3 | **29.0** | 19.2 | 34.0 (4) | 21.8 (8) | 18.6 (15) | Free agent | 8% | 0 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 22.3 | — | **28.5** | 26.6 | 27.8 (4) | 28.5 (6) | 28.0 (10) | Free agent | 2% | 0 / 4 |
| **De'Andre Hunter** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 8 | 36.8 | +9.1 | **26.1** | 24.4 | 34.7 (3) | 31.2 (6) | 25.6 (13) | Free agent | 8% | 0 / 3 |
| **Jamison Battle** | TOR | Kawhi Leonard (03 Dec), RJ Barrett (13 Dec) | 2 | 26.5 | +7.1 | **26.0** | 15.4 | 13.0 (4) | 16.5 (8) | 14.9 (15) | Free agent | 0% | 0 / 3 |
| **Quenton Jackson** | IND | Tyrese Haliburton (13 Dec), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 23.4 | — | **25.6** | 23.8 | 28.0 (3) | 22.6 (7) | 23.6 (15) | Free agent | 5% | 1 / 3 |
| **Brice Sensabaugh** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (29 Nov) | 8 | 22.8 | +11.8 | **25.0** | 18.8 | 35.0 (4) | 22.6 (9) | 20.0 (16) | Free agent | 6% | 1 / 3 |
| **Charles Bassey** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 20.6 | +4.8 | **24.8** | 21.6 | 26.0 (3) | 24.1 (7) | 21.6 (14) | Free agent | 2% | 1 / 3 |
| **Javon Small** (out, ESPN est. back 23 Nov) | MEM | GG Jackson (18 Jan); also out: Scotty Pippen Jr. (25 Nov) | 4 | 24.0 | +3.0 | **24.2** | 23.4 | 30.0 (4) | 24.6 (8) | 23.4 (9) | Free agent | 2% | 0 / 4 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 5 | 21.2 | +8.9 | **23.4** | 16.8 | 21.8 (4) | 23.4 (5) | 18.2 (12) | Free agent | 1% | 1 / 3 |
| **Kel'el Ware** | MIL | Ousmane Dieng (14 Dec) | 5 | 20.6 | +4.2 | **23.2** | 23.4 | 27.0 (4) | 21.8 (9) | 24.0 (16) | Free agent | 51% | 0 / 4 |
| **Terrence Shannon Jr.** | MIN | Anthony Edwards (21 Dec), Donte DiVincenzo (02 Apr) | 7 | 23.9 | +3.2 | **23.0** | 21.4 | 27.2 (5) | 22.9 (7) | 22.4 (13) | Free agent | 7% | 0 / 4 |
| **Kenrich Williams** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 25.2 | +9.8 | **22.6** | 18.6 | 30.0 (3) | 22.6 (8) | 19.3 (15) | Free agent | 2% | 1 / 3 |
| **Will Richard** | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 5 | 25.8 | +7.1 | **22.2** | 16.1 | 30.0 (3) | 21.2 (6) | 15.5 (14) | Free agent | 1% | 1 / 3 |
| **Pete Nance** | MIL | Ousmane Dieng (14 Dec) | 1 | 28.0 | +24.0 | **22.0** | 13.5 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% | 0 / 4 |
| **Bennett Stirtz** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 20.1 | — | **20.7** | 15.5 | 19.7 (3) | 19.6 (8) | 16.5 (15) | Free agent | 1% | 1 / 3 |
| **Nic Claxton** | CHI | Caleb Wilson (13 Dec) | 4 | 22.5 | +5.5 | **20.5** | 23.3 | 22.3 (3) | 23.3 (6) | 23.3 (6) | Free agent | 40% | 1 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (25 Nov) | 10 | 20.6 | — | **20.4** | 18.0 | 19.5 (4) | 18.9 (8) | 18.0 (12) | Free agent | 0% | 0 / 3 |
| **Sidy Cissoko** | POR | Vit Krejci (12 Jan), Ja Morant (01 Dec), Shaedon Sharpe (02 Mar) | 9 | 26.7 | +5.7 | **20.2** | 19.3 | 22.8 (4) | 20.2 (9) | 19.7 (15) | Free agent | 1% | 0 / 4 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 27 Nov | 5 | 30.6 | — | 14.5 (4) | 27.4 (8) | 39.0 | 36.5 | Free agent | 75% | 0 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 9 | 33.8 | — | — | 27.7 (3) | 37.5 | 36.0 | Free agent | 80% | 0 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 7 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 1 / 3 |
| **Grayson Allen** | CHA | Concussion | 23 Nov | 1 | 26.8 | 26.0 (1) | 29.0 (4) | 26.4 (12) | 26.6 | 31.2 | Free agent | 20% | 0 / 3 |
| **P.J. Washington** | DAL | Illness | 22 Nov | 0 | 28.2 | 29.3 (3) | 28.3 (7) | 29.2 (14) | 26.9 | 30.6 | Free agent | 33% | 1 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 3 | 14.2 | — | — | 11.0 (4) | 30.6 | 27.1 | Free agent | 8% | 0 / 4 |
| **Mitchell Robinson** | BOS | Illness | 22 Nov | 0 | 18.6 | 15.7 (3) | 20.3 (7) | 18.6 (13) | 30.3 | 28.2 | Free agent | 11% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 11 | — | — | — | — | 30.1 | 28.0 | Free agent | 40% | 0 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 5 | 29.8 | 13.0 (1) | 19.8 (4) | 30.0 (11) | 21.6 | 23.1 | Free agent | 39% | 1 / 3 |
| **Jerami Grant** | MEM | Left Calf | 23 Nov | 1 | 20.3 | 14.3 (3) → 20.5 (2) | 21.7 (7) → 25.0 (6) | 20.1 (14) → 21.5 (13) | 27.0 | 28.8 | Free agent | 9% | 0 / 4 |
| **Jaylon Tyson** | CLE | Right Ankle | 23 Nov | 1 | 19.2 | 26.0 (1) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 2% | 0 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 3 | — | — | — | — | — | 28.1 | Free agent | 2% | 0 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 27 Nov | 5 | 8.8 | — | 3.2 (4) | 7.6 (11) | 25.1 | 27.6 | Free agent | 6% | 0 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 5 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 1 / 2 |
| **Jock Landale** | ATL | Right Hip Inflammation | 27 Nov | 5 | 16.8 | — | 18.0 (2) | 15.6 (8) → 17.9 (7) | — | 25.8 | Free agent | 0% | 1 / 2 |
| **Collin Murray-Boyles** | TOR | Concussion | 23 Nov | 1 | 24.0 | 21.0 (3) | 27.5 (6) | 23.7 (13) | 24.8 | 25.6 | Free agent | 12% | 0 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 7 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 0 / 4 |
| **T.J. McConnell** | IND | Left Hamstring | 23 Nov | 1 | 20.0 | 23.3 (3) | 20.0 (7) | 20.0 (7) | 24.4 | 25.5 | Free agent | 8% | 1 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 31.7.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Brandon Ingram** | LAC | Right Achilles Surgery | 23 Nov | 1 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 67% | 0 / 4 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 25 Nov | 3 | — (—) | 28.1 (74) | Free agent | 2% | 0 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 27 Nov | 5 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 1 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 7 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 0 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 29 Nov | 7 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 1 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 11 | 30.1 (30.5) | 28.0 (63) | Free agent | 40% | 0 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 41 | 38.8 (32.4) | 41.6 (38) | Free agent | 27% | 1 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 41 | 36.9 (27.7) | 32.3 (32) | Free agent | 31% | 1 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 73 | 31.0 (24.9) | 31.9 (60) | Free agent | 5% | 0 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 100 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 0 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 131 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 0 / 4 |

## Our injured players

- **Jalen Smith** (CHI): Day-To-Day, Illness; ESPN est. back 22 Nov.
- **Cade Cunningham** (DET): Day-To-Day, Right Knee Soreness; ESPN est. back 22 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Out, Knee; ESPN est. back 23 Nov.
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
| Brandon Williams (out, ESPN est. back 25 Nov) | PG/SG | 1 | 25.0 | +11.7 | 0 | **33.0** | 15.0 | — | 10.5 (2) | 17.7 (9) | Free agent | 1% |
| Charles Bassey | C | 5 | 20.6 | +4.8 | 3 | **24.8** | 26.6 | 26.0 (3) | 24.1 (7) | 21.6 (14) | Free agent | 2% |
| Will Richard | SG/SF | 5 | 25.8 | +7.1 | 1 | **22.2** | 15.0 | 30.0 (3) | 21.2 (6) | 15.5 (14) | Free agent | 1% |
| LJ Cryer | PG | 5 | 16.2 | +6.2 | 2 | **14.8** | 8.2 | 11.0 (3) | 18.2 (6) | 10.3 (12) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 25.1 | — | 6 | **35.5** | — | 47.7 (3) | 37.2 (8) | 30.5 (15) | Snow Time Lakers | 33% |
| Kenrich Williams | SF | 10 | 25.2 | +9.8 | 7 | **22.6** | 14.2 | 30.0 (3) | 22.6 (8) | 19.3 (15) | Free agent | 2% |
| Bennett Stirtz | PG | 10 | 20.1 | — | 0 | **20.7** | — | 19.7 (3) | 19.6 (8) | 16.5 (15) | Free agent | 1% |
| Micah Peavy | SF | 8 | 17.2 | — | 0 | **11.6** | — | 9.5 (2) | 10.2 (6) | 9.6 (10) | Free agent | 0% |
| 5105800 |  | 5 | 13.0 | — | 0 | **6.4** | — | — | — | — | — | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 9 | 26.7 | +5.7 | 7 | **20.2** | 28.0 | 22.8 (4) | 20.2 (9) | 19.7 (15) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 27 Nov) | SG | 3 | 18.3 | +14.3 | 0 | **16.7** | 0.0 | — | 16.7 (3) | 10.5 (6) | Free agent | 0% |
| 4703889 |  | 6 | 13.5 | — | 2 | **9.2** | — | — | — | — | — | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 13 Dec | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 10 | 23.4 | — | 3 | **25.6** | — | 28.0 (3) | 22.6 (7) | 23.6 (15) | Free agent | 5% |
| Braden Smith | PG | 7 | 16.9 | — | 4 | **21.0** | — | 25.5 (2) | 14.8 (4) | 15.2 (10) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.4 | — | 1 | **17.1** | — | 23.0 (3) | 15.8 (6) | 14.9 (14) | Free agent | 0% |
| Jay Huff | C | 9 | 14.9 | — | 2 | **13.8** | — | 13.0 (3) | 11.0 (6) | 14.9 (14) | Free agent | 0% |

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| RJ Barrett | Right Hamstring Strain | 13 Dec | 34.1 | 36.4 | Dr White Slong |
| Kawhi Leonard | Left Knee Inflammation | 03 Dec | 32.8 | 40.0 | **us** |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Allen Graves | SF | 2 | 32.0 | +18.2 | 1 | **40.0** | 10.0 | 26.5 (4) | 18.2 (8) | 15.6 (15) | Free agent | 1% |
| Jakob Poeltl | C | 2 | 30.5 | +5.8 | 2 | **37.5** | 30.4 | 28.5 (4) | 33.4 (8) | 27.2 (13) | Free agent | 37% |
| Jamison Battle | SF | 2 | 26.5 | +7.1 | 1 | **26.0** | 13.5 | 13.0 (4) | 16.5 (8) | 14.9 (15) | Free agent | 0% |
| Trayce Jackson-Davis | PF | 2 | 16.5 | +9.8 | 0 | **21.0** | 12.3 | 21.0 (2) | 22.3 (3) | 13.7 (10) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 10 | 33.5 | +4.1 | 10 | **35.2** | 30.4 | 29.6 (5) | 32.1 (8) | 35.1 (16) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga | SF/PF | 9 | 31.6 | +4.3 | 9 | **26.9** | 26.3 | 26.0 (4) | 23.4 (7) | 28.0 (15) | Dr White Slong | 60% |
| Terrence Shannon Jr. | SG | 7 | 23.9 | +3.2 | 0 | **23.0** | 14.9 | 27.2 (5) | 22.9 (7) | 22.4 (13) | Free agent | 7% |
| Joan Beringer | C | 10 | 15.6 | — | 0 | **17.6** | — | 16.0 (5) | 16.6 (8) | 19.9 (16) | Free agent | 2% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 6 | 18.0 | +4.9 | 0 | **13.8** | 9.4 | 3.0 (1) | 12.0 (4) | 12.9 (11) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Free agent |

Last 10 games: 8 game(s) without them, 2 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 8 | 22.8 | +7.8 | 3 | **30.6** | 28.0 | 36.5 (4) | 30.6 (8) | 29.3 (13) | Team Nic Kerr | 18% |
| Brice Sensabaugh | SG/SF | 8 | 22.8 | +11.8 | 0 | **25.0** | 7.5 | 35.0 (4) | 22.6 (9) | 20.0 (16) | Free agent | 6% |
| Svi Mykhailiuk | SG | 8 | 21.2 | +5.8 | 0 | **15.0** | 5.0 | 24.5 (4) | 13.2 (9) | 10.2 (16) | Free agent | 0% |
| Isaiah Collier | PG | 5 | 15.6 | +7.6 | 0 | **14.4** | 5.0 | 7.0 (1) | 13.7 (6) | 14.4 (13) | Free agent | 2% |

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dylan Harper | Hip Soreness | 13 Dec | 31.7 | 36.4 | Melbourne poopoo |
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Victor Wembanyama | C | 2 | 32.5 | +3.6 | 2 | **90.5** | 76.4 | 79.0 (4) | 73.0 (9) | 74.0 (16) | Cream Abdul-Yammar | 100% |
| Jordan McLaughlin | PG | 2 | 14.5 | +3.5 | 0 | **16.5** | 14.7 | 19.0 (3) | 15.1 (8) | 11.9 (11) | Free agent | 0% |
| Carter Bryant | SF | 2 | 16.5 | +5.8 | 0 | **8.5** | 8.7 | 4.0 (4) | 8.7 (9) | 7.3 (15) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Free agent |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Kingston Flemings (back strain; ESPN est. 22 Nov), Jock Landale (right hip inflammation; ESPN est. 27 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Dyson Daniels | PG/SG | 2 | 36.0 | +4.5 | 2 | **49.0** | 42.6 | 43.7 (3) | 48.1 (7) | 41.3 (15) | Snow Time Lakers | 96% |
| Onyeka Okongwu | C | 2 | 35.0 | +3.0 | 2 | **35.5** | 40.8 | 37.3 (3) | 41.0 (7) | 37.7 (15) | Cream Abdul-Yammar | 87% |
| Aaron Wiggins | SG/SF | 2 | 30.0 | +4.5 | 2 | **30.5** | 22.6 | 24.3 (3) | 26.4 (7) | 26.6 (15) | Free agent | 34% |
| Corey Kispert | SG/SF | 2 | 16.5 | +3.9 | 0 | **17.0** | 14.4 | 20.3 (3) | 18.0 (4) | 14.9 (9) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.7 | +5.3 | 10 | **36.6** | 30.2 | 33.8 (4) | 35.9 (9) | 34.8 (16) | Snow Time Lakers | 80% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Miller | SG/SF | 7 | 29.1 | +3.1 | 7 | **28.0** | 2.0 | 27.3 (3) | 23.5 (4) | 30.8 (12) | Matt Wright's Foxies | 86% |
| Royce O'Neale | SF/PF | 9 | 22.6 | +4.6 | 0 | **14.7** | 9.0 | 14.7 (3) | 16.2 (6) | 12.3 (14) | Free agent | 1% |
| Dennis Schroder (out, ESPN est. back 25 Nov) | PG | 3 | 29.0 | +9.0 | 2 | **14.0** | 17.0 | — | — | 17.8 (8) | Free agent | 3% |
| Christian Anderson | PG | 9 | 15.9 | — | 0 | **13.4** | — | 19.3 (3) | 15.2 (6) | 10.2 (13) | Free agent | 0% |
| Tidjane Salaun | PF | 9 | 13.3 | +3.3 | 0 | **10.4** | 13.0 | 3.7 (3) | 9.3 (6) | 11.6 (14) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Norman Powell (day to day, ESPN est. back 22 Nov) | SG/SF | 5 | 30.6 | +3.3 | 5 | **36.2** | 16.3 | 33.2 (4) | 36.2 (5) | 30.7 (12) → 33.1 (11) | Matt Wright's Foxies | 81% |
| Isaac Okoro | SG/SF | 5 | 31.6 | +11.2 | 5 | **29.4** | 10.4 | 29.8 (4) | 24.6 (7) | 17.4 (14) | Free agent | 2% |
| Buddy Hield | SG/SF | 5 | 21.2 | +8.9 | 0 | **23.4** | 15.7 | 21.8 (4) | 23.4 (5) | 18.2 (12) | Free agent | 1% |
| Nic Claxton | C | 4 | 22.5 | +5.5 | 1 | **20.5** | 29.0 | 22.3 (3) | 23.3 (6) | 23.3 (6) | Free agent | 40% |
| Zach Collins | C | 3 | 18.0 | +10.8 | 1 | **18.0** | 6.0 | 18.7 (3) | 15.5 (4) | 9.8 (9) | Free agent | 0% |

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 22.3 | — | 0 | **28.5** | — | 27.8 (4) | 28.5 (6) | 28.0 (10) | Free agent | 2% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Taurean Prince | Right Knee Surgery | 13 Dec | 23.6 | 5.3 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

Also out in those games, so part of the gain is theirs: Jalen Duren (right hamstring strain; ESPN est. 24 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ausar Thompson | SF/PF | 9 | 30.8 | +12.8 | 9 | **41.8** | 45.0 | 45.8 (4) | 44.4 (7) | 38.1 (13) | Lauri Birds | 83% |
| Duncan Robinson (out, ESPN est. back 27 Nov) | SG/SF | 6 | 32.8 | +15.8 | 6 | **33.8** | 13.0 | 13.0 (1) | 19.8 (4) | 30.0 (11) | Free agent | 39% |
| Paul Reed | PF/C | 9 | 26.8 | +3.8 | 4 | **31.4** | 25.0 | 35.5 (4) | 32.6 (7) | 33.7 (14) | Lauri Birds | 37% |
| Javonte Green | SF | 9 | 20.1 | +8.1 | 1 | **17.6** | 5.0 | 19.0 (4) | 18.0 (7) | 14.9 (14) | Free agent | 1% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

Also out in those games, so part of the gain is theirs: Scotty Pippen Jr. (back soreness; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Cam Spencer | PG/SG | 5 | 27.4 | +3.6 | 3 | **33.2** | 30.8 | 39.0 (5) | 31.6 (9) | 31.2 (16) | Lauri Birds | 37% |
| Javon Small (out, ESPN est. back 23 Nov) | PG | 4 | 24.0 | +3.0 | 0 | **24.2** | 25.0 | 30.0 (4) | 24.6 (8) | 23.4 (9) | Free agent | 2% |
| Isaiah Stewart | PF/C | 2 | 19.5 | +3.8 | 0 | **19.5** | 16.2 | 17.7 (3) | 19.0 (5) | 21.2 (12) | Free agent | 3% |
| Olivier-Maxence Prosper | PF | 5 | 18.0 | +10.5 | 0 | **12.8** | 10.2 | 17.0 (5) | 11.8 (8) | 10.5 (11) | Free agent | 0% |
| Jahmai Mashack | SG | 5 | 13.4 | +11.4 | 1 | **6.8** | 0.0 | 6.6 (5) | 5.7 (6) | 5.4 (8) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 23 Nov), Bradley Beal (right knee inflammation; ESPN est. 29 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yanic Konan Niederhauser | C | 2 | 13.5 | — | 0 | **17.0** | — | 17.0 (2) | 17.0 (2) | 17.0 (2) | Free agent | 1% |
| Kobe Sanders | SG | 10 | 22.0 | — | 1 | **16.8** | — | 12.5 (4) | 13.6 (7) | 17.4 (14) | Free agent | 1% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 25 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.0 | +6.4 | 10 | **40.5** | 30.4 | 35.5 (4) | 40.4 (8) | 41.2 (15) | Team Nic Kerr | 91% |
| De'Andre Hunter | SF/PF | 8 | 36.8 | +9.1 | 8 | **26.1** | 23.9 | 34.7 (3) | 31.2 (6) | 25.6 (13) | Free agent | 8% |
| Leaky Black | SF | 10 | 20.6 | — | 1 | **20.4** | — | 19.5 (4) | 18.9 (8) | 18.0 (12) | Free agent | 0% |
| Dylan Cardwell | C | 9 | 15.0 | — | 2 | **16.6** | — | 11.8 (4) | 16.2 (8) | 16.6 (9) | Free agent | 0% |
| Emanuel Sharp | SG | 10 | 16.0 | — | 0 | **12.2** | — | 10.0 (4) | 10.5 (8) | 10.0 (15) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 5 game(s) without them, 5 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brayden Burries | SG | 5 | 29.2 | +5.4 | 4 | **40.0** | 19.4 | 36.2 (4) | 30.9 (9) | 25.0 (16) | Free agent | 11% |
| Kasparas Jakucionis | PG | 5 | 18.8 | +7.3 | 0 | **29.0** | 9.0 | 34.0 (4) | 21.8 (8) | 18.6 (15) | Free agent | 8% |
| Kel'el Ware | C | 5 | 20.6 | +4.2 | 1 | **23.2** | 17.8 | 27.0 (4) | 21.8 (9) | 24.0 (16) | Free agent | 51% |
| Pete Nance | PF | 1 | 28.0 | +24.0 | 1 | **22.0** | 5.0 | 22.0 (1) | 13.5 (2) → 22.0 (1) | 13.5 (2) → 22.0 (1) | Free agent | 0% |
| Gary Trent Jr. | SG/SF | 3 | 17.7 | +9.0 | 0 | **13.0** | 5.3 | 13.0 (3) | 9.2 (6) | 8.1 (8) | Free agent | 0% |

## Every injury

All 110 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 313 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 313 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 221 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 131 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 131 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 17 Mar | 115 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 100 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 100 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 100 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 100 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 95 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 73 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 31 Jan | 70 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 57 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 51 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 43 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 41 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 41 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 41 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 41 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 41 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 29 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 27 | Free agent |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 22 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 22 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Dec | 21 | Lauri Birds |
| Taurean Prince | DET | Out | Right Knee Surgery | 13 Dec | 21 | Free agent |
| RJ Barrett | TOR | Out | Right Hamstring Strain | 13 Dec | 21 | Dr White Slong |
| Dylan Harper | SA | Out | Hip Soreness | 13 Dec | 21 | Melbourne poopoo |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 21 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 20 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 20 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 20 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 11 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 11 | Free agent |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 03 Dec | 11 | **us** |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 11 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 9 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 9 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 9 | Free agent |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 29 Nov | 7 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 29 Nov | 7 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 29 Nov | 7 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 29 Nov | 7 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 7 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 7 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 29 Nov | 7 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 7 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 7 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 28 Nov | 6 | Free agent |
| Trendon Watford | NO | Out | Right Ankle Sprain | 27 Nov | 5 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 27 Nov | 5 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 27 Nov | 5 | Free agent |
| Jock Landale | ATL | Out | Right Hip Inflammation | 27 Nov | 5 | Free agent |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 5 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 27 Nov | 5 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 27 Nov | 5 | Free agent |
| Chris Youngblood | POR | Out | Right Heel Bruise | 27 Nov | 5 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 27 Nov | 5 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 27 Nov | 5 | Free agent |
| Tobe Awaka | CHI | Out | Back | 25 Nov | 3 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 3 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 25 Nov | 3 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 3 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring Strain | 25 Nov | 3 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 2 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 2 | **us** |
| Ebuka Okorie | DET | Out | Left Oblique Strain | 24 Nov | 2 | Free agent |
| Zion Williamson | NO | Out | Left Thigh Bruise | 23 Nov | 1 | Melbourne poopoo |
| Trey Murphy III | NO | Out | Knee | 23 Nov | 1 | **us** |
| T.J. McConnell | IND | Out | Left Hamstring | 23 Nov | 1 | Free agent |
| Ryan Dunn | PHX | Day-To-Day | Right Quadriceps | 23 Nov | 1 | Free agent |
| Nolan Traore | BKN | Day-To-Day | Right Hamstring | 23 Nov | 1 | Free agent |
| Nikola Topic | OKC | Out | Left Hip Soreness | 23 Nov | 1 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 1 | — |
| Jerami Grant | MEM | Out | Left Calf | 23 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle | 23 Nov | 1 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 23 Nov | 1 | Free agent |
| Jaylen Brown | PHI | Out | Left Hamstring | 23 Nov | 1 | Snow Time Lakers |
| Javon Small | MEM | Out | Personal | 23 Nov | 1 | Free agent |
| Grayson Allen | CHA | Day-To-Day | Concussion | 23 Nov | 1 | Free agent |
| Grant Williams | CHA | Day-To-Day | Right Hamstring | 23 Nov | 1 | Free agent |
| Grant Nelson | BKN | Day-To-Day | Right Ankle Sprain | 23 Nov | 1 | — |
| Dean Wade | PHI | Out | Left Hamstring Soreness | 23 Nov | 1 | Free agent |
| Collin Murray-Boyles | TOR | Day-To-Day | Concussion | 23 Nov | 1 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 23 Nov | 1 | Free agent |
| Cameron Boozer | MEM | Out | Ankle | 23 Nov | 1 | Lauri Birds |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 23 Nov | 1 | Melbourne poopoo |
| Austin Reaves | LAL | Out | Left Heel Bruise | 23 Nov | 1 | Cream Abdul-Yammar |
| Alex Caruso | OKC | Out | Right Hip Soreness | 23 Nov | 1 | Free agent |
| Adem Bona | PHI | Out | Back Sprain | 23 Nov | 1 | Free agent |
| Tobi Lawal | DAL | Out | Right Groin | 22 Nov | 0 | Free agent |
| Shai Gilgeous-Alexander | OKC | Day-To-Day | Back Bruise | 22 Nov | 0 | Matt Wright's Foxies |
| Ronald Holland II | DET | Out | Left Knee Bruise | 22 Nov | 0 | Free agent |
| Patrick Williams | CHI | Day-To-Day | Left Thumb | 22 Nov | 0 | Free agent |
| Pascal Siakam | IND | Day-To-Day | Left Hip Soreness | 22 Nov | 0 | Matt Wright's Foxies |
| P.J. Washington | DAL | Out | Illness | 22 Nov | 0 | Free agent |
| OG Anunoby | NY | Day-To-Day | Calf | 22 Nov | 0 | Cream Abdul-Yammar |
| Norman Powell | CHI | Day-To-Day | Right Hamstring | 22 Nov | 0 | Matt Wright's Foxies |
| Myron Gardner | MIA | Day-To-Day | Hamstring | 22 Nov | 0 | Free agent |
| Mitchell Robinson | BOS | Out | Illness | 22 Nov | 0 | Free agent |
| Kingston Flemings | ATL | Out | Back Strain | 22 Nov | 0 | Free agent |
| Karl-Anthony Towns | NY | Day-To-Day | Illness | 22 Nov | 0 | Melbourne poopoo |
| Jordan Clarkson | NY | Day-To-Day | Right Foot Plantar Fasciitis | 22 Nov | 0 | Free agent |
| Jayson Tatum | BOS | Out | Rest | 22 Nov | 0 | Snow Time Lakers |
| Jalen Smith | CHI | Day-To-Day | Illness | 22 Nov | 0 | **us** |
| Giannis Antetokounmpo | MIA | Day-To-Day | Groin | 22 Nov | 0 | Dr White Slong |
| Derrick White | BOS | Out | Left Shoulder | 22 Nov | 0 | Dr White Slong |
| Cade Cunningham | DET | Day-To-Day | Right Knee Soreness | 22 Nov | 0 | **us** |
| Ugonna Onyenso | DET | Day-To-Day | Left Foot | 21 Nov | -1 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-22 07:27 UTC.
- **Research, 22 Nov:** [NBA injury report, 22 Nov 2:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_02_30AM.pdf) · [Heavy, 21 Nov](https://heavy.com/sports/nba/detroit-pistons/injury-report-vs-hawks-november-22) · [Heavy via Yahoo, 20 Nov](https://sports.yahoo.com/articles/detroit-pistons-release-injury-report-082256509.html) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/cade-cunningham-knee-probable-sunday-vs-atl) · [HoopsHype via Yahoo, 17 Nov](https://sports.yahoo.com/articles/duncan-robinson-left-quad-strain-172952431.html) · [Heavy, 21 Nov](https://heavy.com/sports/nba/chicago-bulls/all-star-guard-bulls-nuggets-injury-report/) · [On Tap Sports Net, 20 Nov](https://ontapsportsnet.com/nba/chicago-bulls/bulls-wizards-recap-november-20-2026/) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio) · [TSN, 20 Nov](https://www.tsn.ca/nba/article/report-raptors-leonard-to-miss-two-more-weeks-with-knee-swelling/) · [Heavy via Yahoo, 18 Nov](https://sports.yahoo.com/articles/raptors-announce-kawhi-leonard-injury-013202112.html) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/kingston-flemings-injury-questionable-for-sunday-540375) · [Roundtable via Yahoo, 22 Nov](https://sports.yahoo.com/articles/hawks-kingston-flemings-questionable-against-002113594.html) · [TSN, 19 Nov](https://www.tsn.ca/nba/article/raptors-barrett-hamstring-out-at-least-two-weeks-murray-boyles-enters-concussion-protocol/) · [Heavy via Yahoo, 22 Nov](https://sports.yahoo.com/articles/warriors-good-stephen-curry-news-043445397.html) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brandon-williams-injury-wont-play-sunday-540428) · [Heavy via Yahoo, 21 Nov](https://sports.yahoo.com/articles/lakers-coach-jj-redick-reveals-043347864.html) · [Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/bucks-vs-76ers-injury-report-155845075.html) · [Bulls On SI, 20 Nov](https://www.si.com/nba/bulls/onsi/bulls-injury-report-not-the-game-to-be-without-a-big-man-a-peek-at-caleb-wilson-20) · [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/mobley-toe-to-be-re-evaluated-in-7-10-days) · [NBC Sports, 20 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-20/aaron-wiggins-scores-19-points-as-starter) · [ESPN schedule, read 21 Nov](https://www.espn.com/nba/team/schedule/_/name/atl) · [NBA.com box, 20 Nov](https://www.nba.com/bulls/game/0022600047-wizards-vs-bulls-chicago-il-11-20-2026) · [Chicago Tribune via Yahoo, 18 Nov](https://sports.yahoo.com/articles/isaac-okoro-pestering-presence-lifted-120000884.html) · [CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-questionable-to-play-sunday/) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/t-j-mcconnell-hamstring-out-sunday-vs-new-york) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brice-sensabaugh-news-drop-18-points-with-second-unit-540292) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/jazzs-brice-sensabaugh-dazzles-with-4011-double-double/) · [CBS Sports, 19 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261119_GS@MEM/) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/draymond-green-elbow-removed-from-injury-report) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/alex-caruso-hip-remains-out-sunday-vs-miami) · [Heavy, 21 Nov](https://heavy.com/sports/nba/oklahoma-city-thunder/injury-report-vs-heat-november-22/) · [RotoWire, 21 Nov](https://www.rotowire.com/basketball/headlines/brayden-burries-news-pours-in-career-high-26-on-saturday-540394) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/brayden-burries-records-26-8-4-stat-line-vs-76ers) · [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-defensive-activity-offsets-cold-shooting/) · [FS Roundup box, 21 Nov](https://www.fsroundup.com/nba/game/milwaukee-bucks-at-philadelphia-76ers-2026-11-21) · [NBC Sports, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/kasparas-jakucionis-scores-career-high-25-in-loss) · [VAVEL, 22 Nov](https://www.vavel.com/en-us/nba/2026/11/21/1280226-celtics-vs-kings-live-score-updates-stream-info-and-results-in-nba-regular-season.html) · [CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-hits-for-season-high-30-points/) · [Basketball-Reference game log, read 22 Nov](https://www.basketball-reference.com/players/g/goodwjo01/gamelog/2027) · [CBS/RotoWire, 21 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-p-j-washington-downgraded-to-out-540388/) · [NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/mitchell-robinson-illness-out-saturday-vs-sac) · [HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html) · [Heavy, 21 Nov](https://heavy.com/sports/nba/portland-trail-blazers/injury-report-vs-knicks-november-21/) · [KPTV, 30 Oct](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-out-for-friday/) · [Roundtable via Yahoo, 21 Nov](https://sports.yahoo.com/articles/11-players-listed-timberwolves-vs-180558689.html) · [CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/) · [CBS/RotoWire, 18 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/)
