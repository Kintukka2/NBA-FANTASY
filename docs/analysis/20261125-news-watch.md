# News watch: 25 Nov 2026

- Generated 2026-11-25 09:06 UTC by `council/news_watch.py`. This is **data, not a verdict**: each flag is a question for the research step.
- **Scope:** 14 on our roster, 51 free agents and waiver players (the top 40 by rate, and injured ones worth 25+ FP/g last season or on projection), and 97 on other teams' rosters (injury flags only, except this week's and next week's opponents: Matt Wright's Foxies, Dr White Slong). News is ESPN's fantasy feed (RotoWire's notes); role, minutes and rest read the last 4 days.
- **Flags:** 34 players. *injury*: ESPN's label or date disagrees with the news; *role*: into or out of the starting lineup; *minutes*: last 3 games 5+ min off the season, or a minutes limit; *rest*: a back-to-back in the next 7 days with a rest signal; *gap*: out with no date, or no news in 5 days.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). **Role rate** is FP per minute this season (outliers out) times his minutes in the new role. The plans use it only once the research confirms the role and records it in `council/news_overrides.csv`.

## Overrides (`council/news_overrides.csv`)

| Player | Kind | Value | Until | Source | State |
|---|---|---|---|---|---|
| Aday Mara | role | 27 | 2026-12-05 | [link](https://www.cbssports.com/fantasy/basketball/news/thunders-aday-mara-records-2216-double-double/) | in force |
| Jusuf Nurkic | return | 2026-11-28 | — | [link](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3) | in force |
| Ja Morant | return | 2026-11-28 | — | [link](https://www.kptv.com/2026/10/30/blazers-guard-ja-morant-out-least-4-weeks-due-hamstring-injury/) | in force |
| Dejounte Murray | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) | in force |
| Scotty Pippen Jr. | return | 2026-11-30 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-22_11_15PM.pdf) | in force |
| Jalen Duren | return | 2026-12-01 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_02_00AM.pdf) | in force |
| Charles Bassey | role | 24 | 2026-12-08 | [link](https://www.nbcsportsbayarea.com/nba/golden-state-warriors/brandin-podziemski-observations-takeaways-celtics/1982338/) | in force |
| Paolo Banchero | return | 2026-12-01 | — | [link](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_01_30AM.pdf) | in force |
| Maxime Raynaud | return | 2026-11-25 | — | [link](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-still-out-wednesday/) | expired: remove it |
| Neemias Queta | role | 30 | 2026-11-24 | [link](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/mitchell-robinson-illness-out-again-vs-wizards) | expired: remove it |

## Summary

| Player | NBA | League | Flags | Rate | Role rate | ESPN status |
|---|---|---|---|---:|---:|---|
| **Jalen Duren** | DET | us | injury | 44.1 † | — | out, ESPN est. 30 Nov |
| **Trey Murphy III** | NO | us | minutes, rest | 32.3 | — | active |
| **Paul George** | BOS | us | rest | 42.1 | — | active |
| **Myles Turner** | MIL | us | rest | 33.7 | — | active |
| **Neemias Queta** | BOS | us | rest | 33.3 | — | active |
| **Anthony Black** | ORL | us | rest | 31.1 | — | active |
| **Jusuf Nurkic** | UTAH | free agent | injury | 36.7 | — | out, ESPN est. 29 Nov |
| **Norman Powell** | CHI | free agent | injury | 32.2 | — | out, ESPN est. 28 Nov |
| **Maxime Raynaud** | SAC | free agent | injury | 28.1 | — | out, ESPN est. 02 Dec |
| **Dejounte Murray** | NO | free agent | injury, minutes, gap | 22.3 | 24.0 | out, ESPN est. 27 Nov |
| **Bennedict Mathurin** | NO | free agent | injury, gap | 6.5 | — | out, ESPN est. 27 Nov |
| **Saddiq Bey** | NO | free agent | role, minutes | 33.3 | 40.5 | active |
| **Grayson Allen** | CHA | free agent | role | 30.8 | 29.7 | out, ESPN est. 25 Nov |
| **Charles Bassey** | GS | free agent | role, minutes | 29.5 | 34.7 | active |
| **Buddy Hield** | CHI | free agent | role, minutes | 28.3 | 38.1 | active |
| **P.J. Washington** | DAL | free agent | minutes | 34.3 | 23.6 | active |
| **Daniss Jenkins** | DET | free agent | minutes | 32.6 | 36.8 | active |
| **Caleb Wilson** | CHI | free agent | minutes | 30.9 | 26.1 | out, ESPN est. 13 Dec |
| **Jakob Poeltl** | TOR | free agent | minutes | 30.5 | 33.8 | active |
| **Daniel Gafford** | DAL | free agent | minutes | 29.5 | 36.7 | active |
| **Kelly Oubre Jr.** | IND | free agent | minutes | 28.1 | — | active |
| **Rui Hachimura** | LAC | free agent | rest | 28.6 | — | active |
| **T.J. McConnell** | IND | free agent | rest | 20.7 | — | day-to-day, ESPN est. 27 Nov |
| **Ja Morant** | POR | free agent | gap | 31.2 | — | out, ESPN est. 01 Dec |
| **Tobias Harris** | SA | free agent | gap | 28.0 | — | out, ESPN est. 03 Dec |
| **Paolo Banchero** | ORL | Dr White Slong | injury, gap | 56.8 † | — | out, ESPN est. 29 Nov |
| **Pascal Siakam** | IND | Matt Wright's Foxies | injury, rest | 40.0 | — | active |
| **Evan Mobley** | CLE | Matt Wright's Foxies | injury, gap | 33.8 | — | out, ESPN est. 29 Nov |
| **Naz Reid** | CHA | Matt Wright's Foxies | minutes | 35.0 | 39.4 | active |
| **Joel Embiid** | PHI | Dr White Slong | rest | 47.5 | — | day-to-day, ESPN est. 27 Nov |
| **Amen Thompson** | HOU | Matt Wright's Foxies | rest | 37.9 | — | active |
| **Andrew Nembhard** | IND | Matt Wright's Foxies | rest | 29.6 | — | active |
| **Jonathan Kuminga** | MIN | Dr White Slong | rest | 28.6 | — | active |
| **Derrick White** | BOS | Dr White Slong | rest | 28.1 | — | active |

† Small sample: the rate rests on 2 games or fewer this season (after any dropped outlier).

## Our roster

### Jalen Duren (DET, C, us)

- Rate **44.1** (small sample) · season 33.5 (2) → 44.0 (1) · L7 — · L15 — · L30 — · projected 42.2
- ESPN: out, ESPN est. 30 Nov (Right Hamstring Strain, updated 2026-11-24)
- **Injury:** ESPN est. 30 Nov (Out, Right Hamstring Strain, updated 24 Nov), but the news said on 23 Nov: "Duren hasn't played since Oct. 23 due to a right hamstring strain, though he's expected to be re-evaluated soon."
- News (24 Nov): Duren (hamstring) is being assigned to the Motor City Cruise on Wednesday for practice as he ramps up for a potential return, Eric Vincent of ClutchPoints.com reports.
- News (23 Nov): Duren (hamstring) has been ruled out for Tuesday's game against the Magic.
- **Research:**
  - Out again Tue 24 at ORL (right hamstring strain), his 15th straight game ([NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf)). New since 24 Nov: he **practiced with the Pistons on Tue 24** and starts a rehab assignment with the Motor City Cruise on Wed 25, which Bickerstaff called the next step in his return ([AP via NBA.com, 25 Nov](https://www.nba.com/news/jalen-duren-hamstring-practices-with-pistons-ahead-of-rehab-stint)). Detroit PR says he "will practice Wednesday as part of his return to play" ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/jalen-duren-hamstring-assigned-to-g-league)). Brett Siegel called his return "imminent", but "the Pistons have yet to announce a target date" ([ClutchPoints, 24 Nov](https://clutchpoints.com/nba/detroit-pistons/pistons-news-jalen-duren-g-league-move)).
  - Fri 27 vs MIL and Sun 29 vs ORL are both possible, but no source names either game. Sun 29 is likelier than Fri 27, which follows a single G League practice and the Thanksgiving off day. Check DET's report on Thu 26 (for Fri) and Sat 28 (for Sun). Rate 44.1 rests on 1 game after his 10-min injury exit was dropped (small sample).
  - **Expected return:** no timetable reported; return "imminent", Fri 27 or Sun 29 possible but unconfirmed. *ESPN est.* 30 Nov.
  - **Verdict:** ESPN confirmed as the best date a source supports; it may be a game or two late. Remove the 1 Dec floor row: it rested on the week-to-week label, which practice and a G League assignment have replaced. There is no date for a new row.

### Trey Murphy III (NO, SG/SF, us)

- Rate **32.3** · season 31.1 (11) · L7 31.5 (2) · L15 31.5 (2) · L30 32.2 (8) · projected 36.8
- ESPN: active
- **Minutes:** news on 21 Nov: "Expect his minutes to ramp up quickly, and once he's fully back, he should rejoin a starting lineup that has struggled to find consistent scoring."
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "Murphy was deployed off the bench Friday against the Thunder in his first action since Nov. 8 but was then held out Saturday in San Antonio for the second half of a back-to-back in an effort to ease him back into action following a six-game absence due to bilateral patellar tendinopathy."; sat the second night of the 20–21 Nov back-to-back, playing the games either side
- News (24 Nov): Murphy totaled nine points (4-14 FG, 1-6 3Pt), nine rebounds, two assists and two steals across 35 minutes during Monday's 123-119 overtime loss to the Suns.
- News (23 Nov): Murphy is starting Monday's game against Phoenix.
- **Research:**
  - Minutes: unchanged since 24 Nov. He started Mon 23 vs PHX and played 35 min in OT with no limit mentioned (9 pts, 4-14 FG, 25 FP) ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-low-usage-continues-monday/); [CBS/RotoWire, 23 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-trey-murphy-returning-to-starting-five/)). The ramp-up is done; low usage is the issue. NOP has not played since. L7 31.5 (2) is a small sample; season 31.1 (11), L30 32.2 (8), rate 32.3.
  - Rest: NOP plays Fri 27 at LAC and Sun 29 at POR this week, with no back-to-back, so he should play both. He sat Sat 21, the second night of the 20–21 Nov back-to-back, as maintenance for bilateral patellar tendinopathy ([Yahoo/HoopsHype, 21 Nov](https://sports.yahoo.com/articles/pelicans-rest-trey-murphy-against-182359369.html)). That makes Mon 30 at SAC (next week) the rest risk. Nothing has been announced, so there is no sit row.
  - **Verdict:** ESPN confirmed: active starter, unchanged since 24 Nov. Mon 30 is next week's risk.

### Paul George (BOS, SF/PF, us)

- Rate **42.1** · season 41.9 (15) · L7 44.0 (3) · L15 42.7 (6) · L30 40.3 (13) · projected 38.5
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 23 Nov: "George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports."; sat the second night of the 01–02 Nov back-to-back, playing the games either side; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 21–22 Nov back-to-back, playing the games either side
- News (23 Nov): George (rest) isn't listed on the injury report for Tuesday's game against the Wizards, Taylor Snow of the Celtics' official site reports.
- News (22 Nov): George (rest) has been ruled out for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:**
  - New since 24 Nov: back from his Sun 22 rest night, he played 33 min at WSH on Tue 24 with 28 pts (6-9 3Pt), 9 ast, 4 reb, 1 stl (60 FP) in a 131-116 win, and made his 2,500th career three. No injury was reported ([Yahoo Sports player ratings, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-player-ratings-tatum-drops-051608071.html); [Boston Globe, 24 Nov](https://www.bostonglobe.com/2026/11/24/sports/celtics-wizards-game-score/)). Form: L7 44.0 (3), L15 42.7 (6), L30 40.3 (13), season 41.9 (15), rate 42.1, not 5+ off.
  - Rest: Boston plays Fri 27 vs ATL (NBA Cup group finale) and Sun 29, with no back-to-back this week. Sun 29 is the first night of 29–30 Nov. He has sat the second night of 3 of 5 back-to-backs (2 Nov rest, 11 Nov illness, 22 Nov rest), so **Mon 30 (next week)** is a strong pattern risk. Nothing has been announced, so there is no sit row.
  - **Verdict:** ESPN confirmed: active, plays Fri 27 and Sun 29.

### Myles Turner (MIL, C, us)

- Rate **33.7** · season 28.9 (16) · L7 39.3 (3) · L15 32.2 (6) · L30 31.1 (13) · projected 28.4
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 10–11 Nov back-to-back, playing the games either side; sat the second night of the 18–19 Nov back-to-back, playing the games either side
- News (24 Nov): Turner closed with 27 points (9-12 FG, 5-6 3Pt, 4-5 FT), 11 rebounds, one assist and two blocks over 28 minutes before fouling out of Monday's 116-111 victory over Toronto.
- News (21 Nov): Turner ended with five points (1-8 FG, 1-6 3Pt, 2-2 FT), six rebounds, five assists, four blocks and one steal over 26 minutes before fouling out of Saturday's 132-129 loss to the 76ers.
- **Research:**
  - He is **not on the report** for Wed 25 vs BKN. The Bucks list no players, and only Brooklyn appears for that game ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). No news since his 27-pt, 11-reb, 54-FP night at TOR on Mon 23 (28 min, fouled out) ([NBC Sports/RotoWire, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/myles-turner-posts-27-11-1-line-two-blocked-shots)). L7 39.3 (3) is 10.4 over his 28.9 (16) season average. The cause is shooting in that one game; his minutes (21–28) are unchanged. L15 32.2 (6), L30 31.1 (13), rate 33.7.
  - Rest, Sat 28 vs OKC (second night after Fri 27 at DET): no announcement. He played both nights of 23–24 Oct and sat 11 Nov for "Rest" ([NBA injury report, 11 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-11_05_30PM.pdf)). His 19 Nov absence was a left shoulder contusion, not rest ([NBA injury report, 19 Nov 5:30 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-19_05_30PM.pdf)). That makes one rest sit in three back-to-backs, so Sat 28 is a real but unconfirmed risk. MIL's Sat 28 report (out Fri evening ET) will settle it.
  - **Verdict:** nothing new found: healthy and starting. No announced sit, so there is no sit row.

### Neemias Queta (BOS, C, us)

- Rate **33.3** · season 28.5 (17) · L7 37.8 (4) · L15 33.4 (7) · L30 28.7 (15) · projected 27.2
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (22 Nov): Queta notched 15 points (5-9 FG, 1-1 3Pt, 4-10 FT), seven rebounds, one assist and two blocks over 30 minutes during Saturday's 97-96 loss to the Kings.
- News (19 Nov): Queta notched 17 points (8-14 FG, 0-1 3Pt, 1-1 FT), 10 rebounds, three assists and two steals in 27 minutes during Wednesday's 105-101 loss to the Nuggets.
- **Research:**
  - Mitchell Robinson (illness) was **out** again Tue 24 at WSH, his third straight absence ([NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf)). Queta started at center and had a season-high 21 pts (9-11 FG), 5 reb, 2 blk, 2 ast, 1 stl (48 FP) in **25 min**, with Luka Garza at 18. Boston led by 34 in the first half before a 131-116 win ([Yahoo Sports player ratings, 25 Nov](https://sports.yahoo.com/nba/articles/celtics-player-ratings-tatum-drops-051608071.html)). The blowout, not Robinson's return, held him under 30.
  - Role now: Queta has started every November game, Robinson or not. Without Robinson he played 30, 30 and 25 (blowout); with him, 23–27. No source gives Robinson's status for Fri 27 vs ATL. Expected return for **Mitchell Robinson**: no timetable reported, *ESPN est.* 27 Nov. Form: L7 37.8 (4) is 9.3 over his 28.5 (17) season average, from the extra minutes and Tuesday's shooting. L15 33.4 (7), L30 28.7 (15), rate 33.3.
  - Rest: Boston has no back-to-back this week. His only rest was 16 Nov. Mon 30 (next week) has nothing announced.
  - **Verdict:** ESPN confirmed: active starter. The 30-min role row expired 24 Nov and should be removed. No source reports Robinson out for Fri 27, so there is no new row. Check BOS's Thu 26 report.

**Summary**
- Duren practiced with the Pistons Tue 24 and joins the G League Cruise for practice Wed 25. His return is "imminent" with no date, so Fri 27 or Sun 29 is possible. Remove the 1 Dec floor row (*ESPN est.* 30 Nov stands) and check DET's Thu 26 and Sat 28 reports.
- Queta's 30-min role row has expired: Robinson was out Tue 24 (no timetable, *ESPN est.* 27 Nov). Queta started but played 25 min in a blowout, and Robinson's status for Fri 27 is unreported. Turner is off the Wed 25 report; Sat 28 rest is an unannounced risk (one rest sit in three back-to-backs).
- Murphy and George play both of their games this week (no back-to-backs; George had 28 pts and 60 FP Tue). Mon 30, next week, is the rest risk for both, along with Queta on the same BOS back-to-back.

### Anthony Black (ORL, PG/SG, us)

- Rate **31.1** · season 35.3 (14) · L7 25.5 (4) · L15 32.9 (8) · L30 35.3 (14) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Sat 28–Sun 29 Nov; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Black chipped in 14 points (5-12 FG, 2-4 3Pt, 2-2 FT), five rebounds, two assists and two steals in 35 minutes during Sunday's 116-96 loss to the Wizards.
- News (21 Nov): Black finished with 13 points (4-11 FG, 2-6 3Pt, 3-8 FT), seven rebounds, six assists, two blocks and three steals across 37 minutes during Friday's 113-111 win over the Nets.
- **Research:**
  - Rest: unchanged since 24 Nov. ORL plays Sat 28 @WSH (5:00 PM ET) and Sun 29 @DET (6:00 PM ET). He sat 2 Nov, a second night, listed as left ankle injury management ([CBS/RotoWire, 2 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-anthony-black-will-rest-monday/)), and he played both nights of 10–11 Nov. No source says he will sit 28 or 29 Nov.
  - New since 24 Nov: on Tue 24 vs DET he started but played only 28 min: 5 pts (2-8 FG, 1-3 FT), 4 reb, 2 ast, 5 turnovers, −22, in a 104-86 loss with 20 Orlando turnovers. Bane and Wagner played 38 and da Silva 33 off the bench ([ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)). "Both Anthony Black and Jalen Suggs looked overmatched by the Pistons' pressure defense" ([Orlando Magic Daily, 24 Nov](https://orlandomagicdaily.com/orlando-magic-let-another-chance-advance-past-detroit-pistons-slip-away-01m8823dzz3j)). That looks like a one-game benching for poor play. No injury or rotation change was reported.
  - Form: L7 25.5 (4) is 9.8 under his 35.3 season average. The causes are poor shooting and Tuesday's 3-FP game, not lost minutes (33–37 in his previous four games).
  - Role: he keeps his start while Paolo Banchero is out (right high ankle sprain; "targeting a return within the next couple of weeks" on 19 Nov, about 3 Dec, per Beede via [RotoBaller](https://www.rotoballer.com/player-news/paolo-banchero-ankle-targeting-return-within-a-couple-of-weeks/1997928); out again Tue 24, [NBA.com recap](https://www.nba.com/magic/news/turnovers-poor-shooting-trouble-orlando-magic-in-nba-cup-loss-to-detroit-pistons-20261124); override floor 1 Dec; *ESPN est.* 29 Nov).
  - **Verdict:** nothing new found. He is healthy and starting. His rest risk is still Sun 29 @DET, with no plan announced.

## Free agents and waivers

### Jusuf Nurkic (UTAH, C, free agent)

- Rate **36.7** · season — · L7 — · L15 — · L30 — · projected 27.6
- ESPN: out, ESPN est. 29 Nov (Right Foot Strain, updated 2026-11-20)
- **Injury:** ESPN est. 29 Nov (Out, Right Foot Strain, updated 20 Nov), but the news said on 20 Nov: "Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week."
- News (20 Nov): Nurkic (foot) has been cleared for on-court work and will be re-evaluated in one week.
- News (19 Nov): Nurkic (toe) is listed as out for Friday's game against Phoenix.
- **Research:**
  - Unchanged since 24 Nov. The Jazz said on 20 Nov that he was cleared for on-court work and "will be re-evaluated in one week" ([Jazz, 20 Nov](https://www.nba.com/jazz/news/jusuf-nurkic-injury-update-3)). His last listing was Out at LAL on Mon 23 Nov with the right 2nd plantar plate tear ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)). UTA played no games on 24 or 25 Nov, and I found no Jazz update and no report of contact or 5-on-5 work through 25 Nov.
  - **Expected return:** the re-evaluation is due about 27 Nov, so he should miss Fri 27 vs DEN. His first possible game is Sun 29 vs PHX. *ESPN est.* 29 Nov.
  - **Verdict:** ESPN confirmed. 29 Nov fits the one-week re-evaluation, and the 28 Nov row has the same effect because UTA has no game on 28 Nov.
  - Override proposed: return 2026-11-28

### Norman Powell (CHI, SG/SF, free agent)

- Rate **32.2** · season 30.1 (13) → 32.2 (12) · L7 28.0 (2) · L15 36.2 (5) · L30 30.7 (10) → 33.7 (9) · projected 36.0
- ESPN: out, ESPN est. 28 Nov (Right Hamstring Strain, updated 2026-11-22)
- **Injury:** ESPN est. 28 Nov (Out, Right Hamstring Strain, updated 22 Nov), but the news said on 22 Nov: "Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week."
- News (22 Nov): Powell has been diagnosed with a mild right hamstring strain and will be re-evaluated later this week.
- News (21 Nov): Powell is questionable for Sunday's game against the Nuggets due to a right hamstring strain.
- **Research:**
  - Out Wed 25 Nov at CHA with a right hamstring strain, his third straight miss ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf); [Yardbarker, 24 Nov](https://www.yardbarker.com/nba/articles/bulls_take_big_step_ahead_of_game_vs_sinking_hornets/s1_17045_44613849)). The Bulls' only official word is still the 22 Nov "mild" strain, to be "re-evaluated later this week" ([Bulls/NBA.com, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)), and K.C. Johnson said the team hopes for a "more definitive timeline later in week" ([K.C. Johnson on X, 22 Nov](https://x.com/KCJHoop/status/2124522701285187925)).
  - Sat 28 vs IND: no source says he is expected to play. Coverage still frames it as an open question ([Yahoo/Roundtable, 22 Nov](https://sports.yahoo.com/articles/bulls-unfortunate-norman-powell-injury-202437747.html)). No re-evaluation result had been reported by 25 Nov 4:00 AM ET.
  - **Expected return:** re-evaluation "later this week", no date given. Sat 28 vs IND is the earliest possible game, not a reported target. *ESPN est.* 28 Nov.
  - **Verdict:** ESPN confirmed as a floor. Sat 28 is possible but unconfirmed until the re-evaluation is reported, so I added no row.

### Maxime Raynaud (SAC, C, free agent)

- Rate **28.1** · season — · L7 — · L15 — · L30 —
- ESPN: out, ESPN est. 02 Dec (Right Knee Dislocated, updated 2026-11-25)
- **Injury:** ESPN est. 02 Dec (Out, Right Knee Dislocated, updated 25 Nov), but the news said on 24 Nov: "Raynaud should be considered week-to-week."
- News (24 Nov): Raynaud (knee) is out for Wednesday's game against the Warriors.
- News (18 Nov): Raynaud (knee) will remain on the inactive list for Wednesday's game against the Suns.
- **Research:**
  - Sacramento listed him Out for Wed 25 Nov at GS with a right patella subluxation ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). RotoWire says the Kings have given no update and keep ruling him out 24 hours ahead, so he is "still not close" and "week-to-week" ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-ruled-out-for-wednesday/)). On 23 Nov he was reported to have done on-court workouts, with no timeline ([Roundtable, 23 Nov](https://roundtable.io/sports/nba/kings/players/when-will-kings-raynaud-return-from-right-knee-injury)).
  - **Expected return:** no timetable reported. The 25 Nov floor passed with him out, so the new floor is 2 Dec @PHX, which rules out 29 Nov vs MIN and 30 Nov vs NOP. *ESPN est.* 2 Dec.
  - **Verdict:** ESPN confirmed. ESPN moved its estimate to 2 Dec, which matches the 7-days-after rule, and the row moves from 25 Nov to 2 Dec.
  - Override proposed: return 2026-12-02

### Dejounte Murray (NO, PG/SG, free agent)

- Rate **22.3** · role rate 24.0 · season 30.6 (9) · L7 — · L15 15.0 (2) · L30 21.7 (6) · projected 39.0
- ESPN: out, ESPN est. 27 Nov (Ankle, updated 2026-11-13)
- **Injury:** ESPN est. 27 Nov (Out, Ankle, updated 13 Nov), but the news said on 13 Nov: "Shams Charania of ESPN noted Friday that the star guard won't be available for New Orleans for the time being, so Murray can be considered out indefinitely while the team tries to find him another home."
- **Minutes:** 24.7 min over his last 3 games against 31.4 for the season (−6.8)
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (13 Nov): Murray (ankle) is out for Friday's game against Memphis.
- News (13 Nov): Murray (ankle) requested a trade from the Pelicans on Friday, per Shams Charania of ESPN.
- **Research:**
  - He was Out Mon 23 Nov vs PHX with a left ankle sprain ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf); [Pelicans.com, 23 Nov](https://nba.com/pelicans/news/pelicans-shootaround-update-three-players-are-probable-for-phoenix-game-who-were-dnps-saturday)). He is sitting until he is traded ([HoopsHype via Yahoo, 13 Nov](https://sports.yahoo.com/articles/dejounte-murray-sit-until-trade-203559326.html)).
  - New on 24 Nov: he is "currently away from the team". The Warriors have no interest, and his fully guaranteed $32.7M contract limits the market unless NOP adds picks, which it seems unwilling to do ([Siegel via ClutchPoints, 24 Nov](https://clutchpoints.com/nba/new-orleans-pelicans/nba-rumors-warriors-told-rich-paul-came-asking-dejounte-murray-trade)). That answers the gap flag: still a standoff, no deal near. The minutes flag (8–11 Nov games) is moot while he does not play.
  - **Expected return:** no timetable reported. He is out until he is traded. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN corrected. 27 Nov is a placeholder. The 30 Nov row stays: it is 7 days after the 23 Nov out listing and rules him out of 27 Nov @LAC and 29 Nov @POR.
  - Override proposed: return 2026-11-30

### Bennedict Mathurin (NO, SG/SF, free agent)

- Rate **6.5** · season 8.8 (12) · L7 — · L15 0.0 (2) · L30 6.6 (9) · projected 25.1
- ESPN: out, ESPN est. 27 Nov (Left Foot Plantar Fasciitis, updated 2026-11-19)
- **Injury:** ESPN est. 27 Nov (Out, Left Foot Plantar Fasciitis, updated 19 Nov), but the news said on 19 Nov: "Jordan Poole should remain in the backcourt rotation for the undermanned Pelicans moving forward, while Mathurin can be deemed week-to-week."
- **Gap:** listed out, and no news in 5 days (ESPN est. 27 Nov)
- News (19 Nov): Mathurin (foot) has been ruled out for Friday's game against the Thunder.
- News (17 Nov): Mathurin (foot) has been ruled out for Wednesday's game against Detroit.
- **Research:**
  - Unchanged since 24 Nov. He was Out Mon 23 Nov vs PHX with left plantar fasciitis ([NBA injury report, 23 Nov 11:45 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-23_11_45PM.pdf)), and the team's shootaround notes gave no timeline ([Pelicans.com, 23 Nov](https://nba.com/pelicans/news/pelicans-shootaround-update-three-players-are-probable-for-phoenix-game-who-were-dnps-saturday)). "Week-to-week" is RotoWire's own view ([CBS/RotoWire, 19 Nov](https://www.cbssports.com/fantasy/basketball/news/pelicans-bennedict-mathurin-another-absence-coming/)).
  - Gap: NOP has played no games since 23 Nov, so there has been no new listing. Its report for Fri 27 @LAC is due 26 Nov.
  - **Expected return:** no timetable reported. The week-to-week floor is 26 Nov, and NOP's first game after it is 27 Nov @LAC. *ESPN est.* 27 Nov.
  - **Verdict:** ESPN confirmed as a floor. No source puts him out longer, so I added no row. If NOP lists him out for 27 Nov, the floor becomes 4 Dec.

---
**Summary**
- Raynaud: Sacramento listed him out for Wed 25 at GS (official report, 25 Nov 4:00 AM ET), so his row moves from 25 Nov to **2 Dec** and he misses SAC's 29 and 30 Nov games. ESPN's estimate already shows 2 Dec.
- Powell: out Wed 25 at CHA. No source says he is expected Sat 28 vs IND. The Bulls' re-evaluation "later this week" has not been reported, so 28 Nov is a floor only and I added no row.
- Nurkic (28 Nov) and Murray (30 Nov) rows stay. Murray is still away from the team with a thin trade market (Siegel, 24 Nov). Mathurin has nothing new, and NOP files for 27 Nov on 26 Nov.

### Saddiq Bey (NO, SF/PF, free agent)

- Rate **33.3** · role rate 40.5 · season 29.6 (19) → 31.2 (18) · L7 25.5 (4) → 33.7 (3) · L15 30.7 (9) → 34.4 (8) · L30 30.8 (16) → 32.7 (15) · projected 25.9
- ESPN: active
- **Role:** news on 23 Nov: "Bey is not listed in the starting lineup for Monday's game against the Suns."
- **Minutes:** 39.7 min over his last 3 games against 30.6 for the season (+9.1)
- News (23 Nov): Bey is not listed in the starting lineup for Monday's game against the Suns.
- News (21 Nov): Bey finished with 21 points (8-17 FG, 4-9 3Pt, 1-1 FT), six rebounds, three assists and one block across 37 minutes during Friday's 126-120 loss to the Thunder.
- **Research:**
  - Role: unchanged since 24 Nov. NOP has not played since Mon 23. That night Trey Murphy III rejoined the starting five, and Bey came off the bench for 21 pts in 40 min of a 123-119 overtime loss ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/saddiq-bey-scores-21-points-off-bench-in-loss); [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910042)). The bench role lasts while Murphy plays. Murphy has bilateral patellar tendinopathy, which the team manages, and he sat the second night of the 20–21 Nov back-to-back ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/trey-murphy-knee-out-saturday-vs-san-antonio)). NOP has no back-to-back this week: Fri 27 @LAC and Sun 29 @POR.
  - Minutes: the 39.7-min average includes starts and 5 min of overtime. Wing minutes stay open while Bennedict Mathurin (left plantar fasciitis; no timetable reported; *ESPN est.* 27 Nov) and Dejounte Murray (left ankle, sitting until a trade; override floor 30 Nov; *ESPN est.* 27 Nov) are out. No new update on either was found ([NBC Sports, 21 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-21/bennedict-mathurin-foot-remains-out-saturday)). Expect about 30 min off the bench (28–34). NOP's report for Fri 27 is not out yet.
  - **Verdict:** nothing new found (unchanged since 24 Nov). The bench role is ongoing, but the 30-min estimate rests on one overtime game, so no row.

### Grayson Allen (CHA, PG/SG, free agent)

- Rate **30.8** · role rate 29.7 · season 26.8 (13) · L7 — · L15 36.0 (3) · L30 26.3 (10) · projected 26.6
- ESPN: out, ESPN est. 25 Nov (Concussion, updated 2026-11-24)
- **Role:** started 1 of his last 2 games after 2 of 11 before; 30.0 min in his starts, against 27.2 for the season
- News (24 Nov): Allen (concussion) is listed as questionable for Wednesday's game versus Chicago.
- News (22 Nov): Allen (concussion) has been ruled out for Monday's game against the Grizzlies.
- **Research:**
  - Injury: he is now **questionable for Wed 25 vs CHI** (Concussion Protocol) after three straight misses ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). RotoWire says he appears to be working toward a return but is not a lock to play. No report of a clearance or a full practice was found ([CBS/RotoWire, 24 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-might-return-wednesday/)).
  - Role: unchanged since 24 Nov. He started only while Brandon Miller was out. Miller is back, and Sion James (probable, thigh) holds the other starting spot. Two guards are out on Wednesday's report: Knueppel (hamstring; re-evaluation about 6 Dec; *ESPN est.* 12 Dec) and Schroder (hamstring; his two-week re-evaluation from 8 Nov has passed with no update; *ESPN est.* 12 Dec) ([Hornets PR, 8 Nov](https://x.com/HornetsPR/status/2119551984642502912)). That keeps Allen's bench minutes up, at about 25 if he is cleared. CHA plays Wed 25 vs CHI and Sat 28 vs BKN.
  - **Expected return:** no timetable reported (concussion protocol). He is questionable for Wed 25, and Sat 28 vs BKN is next if he sits. *ESPN est.* 25 Nov.
  - **Verdict:** ESPN confirmed. The questionable tag now supports 25 Nov as possible, though he has not been cleared.

### Charles Bassey (GS, C, free agent)

- Rate **29.5** · role rate 34.7 · season 23.3 (15) · L7 39.0 (3) · L15 28.4 (7) · L30 22.9 (14) · projected 14.5
- ESPN: active
- **Role:** started 2 of his last 2 games after 2 of 13 before; 23.2 min in his starts, against 15.6 for the season
- **Minutes:** 24.3 min over his last 3 games against 15.6 for the season (+8.7)
- News (23 Nov): Bassey recorded 13 points (6-7 FG, 1-2 FT), nine rebounds, three assists and three steals across 26 minutes during Sunday's 88-87 victory over the Celtics.
- News (20 Nov): Bassey ended with 16 points (6-7 FG, 4-5 FT), 13 rebounds, one assist, two blocks and one steal across 25 minutes during Thursday's 126-98 loss to the Grizzlies.
- **Research:**
  - Role: still ongoing, with stronger backing since 24 Nov. Asked about keeping Bassey with the starters, Kerr said: "We're definitely going to give it a look, and can't predict how long, but hopefully for the season." Horford has come off the bench in both games since the change (17 and 18 min) ([Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/steve-kerr-addresses-warriors-look-221429191.html)). A Wed 25 preview projects Bassey at center alongside Green and Santos ([Yahoo Sports, 24 Nov](https://sports.yahoo.com/nba/articles/yaxel-lendeborg-gets-surprising-injury-233246217.html)).
  - Availability: neither Bassey nor Horford is on Golden State's report for Wed 25 vs SAC (10:00 PM ET). Curry, Porzingis, Moody and Butler are Out. Lendeborg (illness; *ESPN est.* 25 Nov) and Brandon Williams are Questionable ([NBA injury report, 25 Nov 3:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_03_30AM.pdf)). Lendeborg is on our roster.
  - Minutes: 22, 25 and 26 in his three starts. Expect about 24 in Wed 25 vs SAC, Fri 27 @POR and Sun 29 vs LAC. The only center whose return would end the role is Porzingis (not with team, no timetable reported; *ESPN est.* 2 Jan).
  - **Verdict:** ESPN confirmed (active). The start is expected to continue on Wed 25. The lineup is not yet announced, so recheck it near tip-off. The existing role row (24, until 8 Dec) holds, and this row refreshes its source.
  - Override proposed: role 24

### Buddy Hield (CHI, SG/SF, free agent)

- Rate **28.3** · role rate 38.1 · season 21.0 (15) · L7 35.2 (4) · L15 30.6 (7) · L30 22.9 (12) · projected 16.9
- ESPN: active
- **Role:** started 2 of his last 2 games after 0 of 13 before; 33.5 min in his starts, against 18.5 for the season
- **Role:** news on 22 Nov: "Hield will start Sunday's game against Denver."
- **Minutes:** 30.0 min over his last 3 games against 18.5 for the season (+11.5)
- News (23 Nov): Hield finished Sunday's 151-145 overtime loss to Denver with 33 points (13-19 FG, 7-13 3Pt), seven rebounds, six assists and one steal in 40 minutes.
- News (22 Nov): Hield will start Sunday's game against Denver.
- **Research:**
  - Role: ongoing while Norman Powell is out. Hield started Sun 22 vs DEN (40 min including overtime, 33 pts, 7 threes) and Mon 23 vs CLE (27 min, 17 pts) ([CBS/RotoWire, 22 Nov](https://www.cbssports.com/fantasy/basketball/news/bulls-buddy-hield-starting-versus-nuggets/); [NBC Sports, 23 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-23/buddy-hield-scores-12-fourth-quarter-points-monday); [ESPN box, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910041)). Rotoworld: "worth streaming until Powell is cleared."
  - Powell: mild right hamstring strain on 20 Nov; "Powell will be re-evaluated later this week" ([Bulls, 22 Nov](https://www.nba.com/bulls/news/norman-powell-medical-update)). He is **Out** for Wed 25 @CHA ([NBA injury report, 25 Nov 3:30 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_03_30AM.pdf)). Powell's expected return: re-evaluation later this week, no date reported; *ESPN est.* 28 Nov, which is CHI's next game (Sat 28 vs IND). His return ends Hield's start. Expect about 30 min on Wed 25. Sat 28 is uncertain.
  - Form: L7 35.2 (4) is 14.2 over his 21.0 season average because he is starting.
  - **Verdict:** ESPN confirmed (active). The start holds for Wed 25. The row covers only that night, because Powell could be back Sat 28.
  - Override proposed: role 30

### P.J. Washington (DAL, SF/PF, free agent)

- Rate **34.3** · role rate 23.6 · season 28.6 (16) · L7 46.0 (2) · L15 27.7 (6) · L30 28.8 (13) · projected 26.9
- ESPN: active
- **Minutes:** 25.0 min over his last 3 games against 30.6 for the season (−5.6)
- News (24 Nov): Washington (illness) is available for Tuesday's game in Denver.
- News (23 Nov): Washington (illness) is questionable for Tuesday's game against the Nuggets.
- **Research:**
  - Status: he returned Tue 24 @DEN after missing two games with an illness. He was cleared only after warmups and came **off the bench**: 14 pts, 6 reb, 2 stl, 1 blk on 6-of-11 shooting, +32, in 24:37 of a 120-101 win ([Dallas Sports Journal, 25 Nov](https://dallassportsjournal.com/pj-washington-bench-return-dusty-may-mavericks-nuggets/); [ESPN box, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316)). Zaccharie Risacher kept the start.
  - Role: Dusty May did not commit. He said Dallas "didn't want to rock the boat" and may or may not reshuffle, adding "that'll probably work itself out." He also said Washington looked good with the second unit ([Dallas Sports Journal, 25 Nov](https://dallassportsjournal.com/pj-washington-bench-return-dusty-may-mavericks-nuggets/)).
  - Minutes: the 25-min trend came from blowouts and foul trouble before the illness, and now from the bench role. Expect about 25 min in Fri 27 @PHX, DAL's only other game this week, unless May restores the start. His L7 46.0 rests on 2 games (small sample).
  - **Verdict:** ESPN confirmed (active, illness over). The bench role is not reported as ongoing, so no row. His rate (34.3) leans on games he started. His role rate at 25 min is 23.6.

### Daniss Jenkins (DET, PG, free agent)

- Rate **32.6** · role rate 36.8 · season 30.2 (17) · L7 33.8 (5) · L15 36.1 (8) · L30 31.4 (15)
- ESPN: active
- **Minutes:** 37.3 min over his last 3 games against 30.7 for the season (+6.6)
- News (24 Nov): Jenkins registered 15 points (6-16 FG, 1-6 3Pt, 2-2 FT), four rebounds, 10 assists and two steals in 35 minutes during Tuesday's 104-86 win over the Magic.
- News (23 Nov): Jenkins logged 11 points (4-12 FG, 1-6 3Pt, 2-2 FT), four rebounds, three assists and one steal over 38 minutes during Sunday's 107-97 loss to the Hawks.
- **Research:**
  - Minutes: he started Tue 24 at ORL and ran the point. In 35 min he had 15 pts (6-16 FG), 4 reb, 10 ast, 2 stl and 5 TO for 39 FP in a 104-86 win ([ESPN box score, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909314)). His last five starts ran 38, 36, 39, 38 and 35 min. Cunningham was a late scratch with right knee soreness (no timetable reported; *ESPN est.* 27 Nov). Bickerstaff said he is "battling through a lot" ([Detroit News via Yahoo, 24 Nov](https://sports.yahoo.com/nba/article/pistons-cade-cunningham-out-for-tuesdays-nba-cup-matchup-vs-magic-with-right-knee-soreness-234518276.html)). Isaiah Joe, back from injury, started in Cunningham's place.
  - Duren (right hamstring; no target date; *ESPN est.* 30 Nov) goes to the G League Cruise to practise on Wed 25 as part of his return-to-play process. Robinson (left quad; *ESPN est.* 27 Nov) is now day-to-day ([Yardbarker, Pistons release, 24 Nov](https://www.yardbarker.com/nba/articles/pistons_issue_health_updates_on_duren_prince_others/s1_14822_44612779)). NBC Sports says Jenkins "should be rostered until Jalen Duren returns" ([NBC Sports, 24 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-24/daniss-jenkins-dishes-out-10-assists-vs-orlando)). DET plays Fri 27 vs MIL and Sun 29 vs ORL.
  - **Verdict:** ESPN confirmed: active. He keeps the start and about 37 min at least through Fri 27. Duren's return, which looks close, ends the role. More Cunningham absences would raise it.
  - Override proposed: role 37

### Caleb Wilson (CHI, SF, free agent)

- Rate **30.9** · role rate 26.1 · season 34.9 (10) · L7 — · L15 26.0 (1) · L30 33.3 (7) · projected 34.9
- ESPN: out, ESPN est. 13 Dec (Right Hand, updated 2026-11-12)
- **Minutes:** 23.0 min over his last 3 games against 30.7 for the season (−7.7)
- News (12 Nov): Wilson is undergoing surgery for a fractured right hand and will miss at least four to six weeks, Shams Charania of ESPN reports.
- News (11 Nov): Wilson won't return to Wednesday's game against the Spurs due to a right hand injury. He'll finish with 15 points (5-7 FG, 2-2 3Pt, 3-3 FT), five rebounds and one steal in 15 minutes.
- **Research:**
  - Injury: unchanged since 24 Nov. He is out Wed 25 at CHA (right metacarpal fracture) ([NBA injury report, 25 Nov 4:00 AM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-25_04_00AM.pdf)). The Bulls set a re-evaluation for three weeks after his 12 Nov surgery, about 3 Dec ([Bulls, 12 Nov](https://www.nba.com/bulls/news/caleb-wilson-medical-update)). He is running and doing strength work and has no timeline in mind ([Bulls On SI via Yahoo, 22 Nov](https://sports.yahoo.com/articles/bulls-caleb-wilson-sounds-optimistic-003142636.html)). No newer update was found.
  - Minutes flag: the low L3 comes from his 15-min injury exit on 11 Nov. It does not matter while he is out.
  - **Expected return:** four to six weeks from 12 Nov (10 to 24 Dec), with a re-evaluation about 3 Dec. He will not play this week. *ESPN est.* 13 Dec.
  - **Verdict:** ESPN confirmed. The team's timeline has not changed.

### Jakob Poeltl (TOR, C, free agent)

- Rate **30.5** · role rate 33.8 · season 27.4 (15) · L7 32.5 (4) · L15 31.1 (8) · L30 28.2 (13) · projected 31.7
- ESPN: active
- **Minutes:** 29.7 min over his last 3 games against 24.2 for the season (+5.5)
- News (24 Nov): Poeltl recorded 15 points (5-10 FG, 5-6 FT), 10 rebounds, three assists, one block and one steal in 28 minutes before fouling out of Monday's 116-111 loss to the Bucks.
- News (21 Nov): Poeltl chipped in 10 points (5-7 FG), nine rebounds, three assists and two blocks across 32 minutes during Friday's 105-102 victory over Detroit.
- **Research:**
  - Role: unchanged since 24 Nov. TOR has not played since Mon 23, when he started at center and played 28 min for 41 FP before fouling out ([ESPN box score, 23 Nov](https://www.espn.com/nba/boxscore/_/gameId/401910039)). Murray-Boyles came off the bench in his return from the concussion protocol, but the report covers Monday only ([RotoWire, 23 Nov](https://www.rotowire.com/basketball/headlines/collin-murray-boyles-news-manning-bench-role-in-return-540715)). No lineup news has come out since.
  - Barrett (right hamstring; re-evaluated about 3 Dec; *ESPN est.* 13 Dec) is still out. TOR plays Fri 27 vs BKN and Sun 29 vs DEN.
  - **Verdict:** nothing new found. He is the starting center for now at about 28 to 32 min. No row, because no source calls the role ongoing.

### Daniel Gafford (DAL, C, free agent)

- Rate **29.5** · role rate 36.7 · season 28.8 (18) · L7 33.5 (4) · L15 25.5 (8) · L30 28.9 (15) · projected 29.3
- ESPN: active
- **Minutes:** 28.7 min over his last 3 games against 22.5 for the season (+6.2)
- News (23 Nov): Gafford notched 10 points (5-8 FG), four rebounds, four assists and two steals over 28 minutes during Sunday's 116-114 win over the Jazz.
- News (15 Nov): Gafford (shoulder) is available for Sunday's game against Boston.
- **Research:**
  - Minutes: P.J. Washington returned from illness on Tue 24 at DEN but came off the bench for the first time this season (25 min). May "stuck with his five starters," and the article does not say whether that lineup will stay ([Mavericks.com, 24 Nov](https://www.nba.com/mavs/news/mavericks-knock-out-nuggets-for-fourth-consecutive-win)). Gafford started and played 27 min: 13 pts (6-8 FG), 6 reb, 3 ast, 1 stl and 2 blk for 36 FP in a 120-101 win ([ESPN box score, 24 Nov](https://www.espn.com/nba/boxscore/_/gameId/401909316)). That one game contradicts yesterday's inference that he would drop to 22 to 24 min with Washington back.
  - Lively (right foot surgery; no timetable reported; May said 20 Nov that Lively feels "close"; *ESPN est.* 27 Nov) was out Tue 24 ([NBA injury report, 24 Nov 6:30 PM ET](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-24_06_30PM.pdf); [CBS/RotoWire, 20 Nov](https://www.cbssports.com/fantasy/basketball/news/mavericks-dereck-lively-progressing-in-recovery/)). DAL's only game left this week is Fri 27 at PHX.
  - **Verdict:** ESPN confirmed: active and starting. Expect about 27 min while Washington comes off the bench (one game, a 19-point win). No row, because no source calls the role ongoing.

### Kelly Oubre Jr. (IND, SG/SF, free agent)

- Rate **28.1** · season 23.5 (16) · L7 30.0 (4) · L15 30.2 (8) · L30 25.1 (14) · projected 23.2
- ESPN: active
- **Minutes:** news on 24 Nov: "Oubre scored at least 15 points for the sixth straight game, continuing to ramp up after a slow start to the season."
- News (24 Nov): Oubre racked up 20 points (8-13 FG, 4-7 3Pt), four rebounds, two assists and two blocks over 28 minutes during Monday's 125-120 win over Oklahoma City.
- News (23 Nov): Oubre recorded 15 points (4-10 FG, 0-4 3Pt, 7-9 FT) and five rebounds in 27 minutes during Sunday's 113-106 loss to the Knicks.
- **Research:** _pending_

### Rui Hachimura (LAC, SF/PF, free agent)

- Rate **28.6** · season 25.1 (14) · L7 35.0 (4) · L15 26.6 (7) · L30 25.6 (12) · projected 24.0
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (24 Nov): Hachimura logged 19 points (7-10 FG, 2-4 3Pt, 3-3 FT), three rebounds, three assists and one block across 29 minutes during Monday's 116-104 loss to the Rockets.
- News (20 Nov): Hachimura contributed 17 points (7-13 FG, 2-4 3Pt, 1-1 FT), seven rebounds, two assists and one steal in 32 minutes during Thursday's 124-112 loss to the Spurs.
- **Research:** _pending_

### T.J. McConnell (IND, PG, free agent)

- Rate **20.7** · season 20.0 (7) · L7 20.0 (2) · L15 21.2 (6) · L30 20.0 (7) · projected 24.4
- ESPN: day-to-day, ESPN est. 27 Nov (Left Hamstring, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "The veteran floor general is missing both ends of this back-to-back set, but he'll have some extra time to heal up ahead of Friday's tilt against the 76ers."
- News (24 Nov): McConnell (hamstring) was recalled from the G League's Noblesville Boom on Tuesday, Shams Charania of ESPN reports.
- News (24 Nov): McConnell (hamstring) was assigned to the G League's Noblesville Boom on Tuesday.
- **Research:** _pending_

### Ja Morant (POR, PG, free agent)

- Rate **31.2** · season 33.8 (4) · L7 — · L15 — · L30 28.0 (2) · projected 37.5
- ESPN: out, ESPN est. 01 Dec (Left Hamstring, updated 2026-11-08)
- **Gap:** listed out, and no news in 5 days (ESPN est. 01 Dec)
- News (07 Nov): Head coach Micah Nori said Morant met with a doctor in Los Angeles, who gave him a positive outlook on his recovery from the hamstring injury. While Nori declined to update Morant's timetable, he added Morant "may not be out for as long as we thought," Trail Blazers Insider Sean Highkin reports.
- News (30 Oct): Morant has been diagnosed with a Grade 2 left hamstring strain and is expected to miss four weeks, Portland announced Friday.
- **Research:** _pending_

### Tobias Harris (SA, SF/PF, free agent)

- Rate **28.0** · season — · L7 — · L15 — · L30 — · projected 30.1
- ESPN: out, ESPN est. 03 Dec (Left Calf Strain, updated 2026-11-16)
- **Gap:** listed out, and no news in 5 days (ESPN est. 03 Dec)
- News (16 Nov): Harris (calf) is likely to be sidelined until early December, per Jeff Garcia of KENS 5 San Antonio.
- News (10 Nov): Harris (calf) is out for Wednesday's game against Chicago, Jared Weiss of The Athletic reports.
- **Research:** _pending_

## Opponents: this week and next

### Paolo Banchero (ORL, SF/PF, Dr White Slong)

- Rate **56.8** (small sample) · season 47.0 (2) → 65.0 (1) · L7 — · L15 — · L30 — · projected 39.0
- ESPN: out, ESPN est. 29 Nov (Right Ankle Sprain, updated 2026-10-24)
- **Injury:** ESPN est. 29 Nov (Out, Right Ankle Sprain, updated 24 Oct), but the news said on 24 Oct: "Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (24 Oct): Banchero is expected to be sidelined for the next four-to-six weeks due to a right high-ankle sprain, Shams Charania of ESPN reports.
- News (23 Oct): Banchero didn't check back in during the fourth quarter of Friday's 115-93 loss to the Timberwolves after being deemed doubtful to return. He finished with 14 points (5-11 FG, 0-2 3Pt, 2-4 FT), six rebounds, five assists and one steal across 26 minutes.
- **Research:** _pending_

### Pascal Siakam (IND, PF, Matt Wright's Foxies)

- Rate **40.0** · season 39.1 (17) · L7 39.2 (4) · L15 41.2 (8) · L30 39.9 (15) · projected 41.1
- ESPN: active
- **Injury:** not in ESPN's injury feed, but the news said on 23 Nov: "Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management."
- **Rest:** back-to-back Fri 27–Sat 28 Nov; news on 23 Nov: "After carrying a questionable tag ahead of both parts of this back-to-back, Siakam is suiting up Monday despite dealing with a left hip injury."; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Siakam (hip) will play in Monday's game against the Thunder, Justin Martinez of The Oklahoman reports.
- News (23 Nov): Siakam is questionable for Monday's game against Oklahoma City due to left hip injury management.
- **Research:** _pending_

### Evan Mobley (CLE, PF/C, Matt Wright's Foxies)

- Rate **33.8** · season 39.9 (12) · L7 — · L15 24.5 (2) · L30 38.6 (10) · projected 43.3
- ESPN: out, ESPN est. 29 Nov (Left Toe Sprain, updated 2026-11-16)
- **Injury:** ESPN est. 29 Nov (Out, Left Toe Sprain, updated 16 Nov), but the news said on 16 Nov: "Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days."
- **Gap:** listed out, and no news in 5 days (ESPN est. 29 Nov)
- News (16 Nov): Mobley will receive treatment and participate in rehab after the team confirmed a diagnosis of a left great toe sprain, and he'll be re-evaluated in the next 7-to-10 days.
- News (15 Nov): Mobley (toe) has been ruled out for Monday's game against the Bulls.
- **Research:** _pending_

### Naz Reid (CHA, PF/C, Matt Wright's Foxies)

- Rate **35.0** · role rate 39.4 · season 31.5 (16) → 32.6 (15) · L7 38.3 (3) · L15 35.8 (6) · L30 30.0 (13) → 31.2 (12) · projected 35.5
- ESPN: active
- **Minutes:** 39.7 min over his last 3 games against 32.8 for the season (+6.9)
- News (24 Nov): Reid notched 24 points (8-25 FG, 3-10 3Pt, 5-6 FT), six rebounds, three assists and two steals over 38 minutes during Monday's 117-111 loss to the Grizzlies.
- News (20 Nov): Reid logged 12 points (4-19 FG, 2-10 3Pt, 2-4 FT), 10 rebounds, three assists and one block over 39 minutes during the Hornets' 111-97 loss to the Hawks on Friday.
- **Research:** _pending_

### Joel Embiid (PHI, C, Dr White Slong)

- Rate **47.5** · season 39.4 (14) · L7 59.5 (2) · L15 44.4 (5) · L30 37.5 (11) · projected 45.4
- ESPN: day-to-day, ESPN est. 27 Nov (Illness, updated 2026-11-24)
- **Rest:** back-to-back Fri 27–Sat 28 Nov, Tue 01–Wed 02 Dec; sat the second night of the 24–25 Oct back-to-back, playing the games either side; sat the second night of the 30–31 Oct back-to-back, playing the games either side; sat the first night of the 15–16 Nov back-to-back, playing the games either side
- News (24 Nov): Embiid (illness) is listed as doubtful for Wednesday's game versus Miami.
- News (23 Nov): Embiid (illness) is out for Monday's game against Portland, Austin Krell of OnPattison.com reports.
- **Research:** _pending_

### Amen Thompson (HOU, SG/SF, Matt Wright's Foxies)

- Rate **37.9** · season 37.1 (17) · L7 37.3 (3) · L15 39.9 (7) · L30 34.6 (14) · projected 40.0
- ESPN: active
- **Rest:** back-to-back Mon 30–Tue 01 Dec; sat the second night of the 15–16 Nov back-to-back, playing the games either side
- News (24 Nov): Thompson ended Monday's 116-104 victory over the Clippers with 20 points (9-12 FG, 1-1 3Pt, 1-2 FT), four rebounds, five assists and one block over 28 minutes.
- News (21 Nov): Thompson chipped in 22 points (10-12 FG, 0-1 3Pt, 2-6 FT), six rebounds and one steal in 26 minutes during Friday's 133-124 loss to the Nuggets.
- **Research:** _pending_

### Andrew Nembhard (IND, PG/SG, Matt Wright's Foxies)

- Rate **29.6** · season 31.8 (14) · L7 26.7 (3) · L15 29.5 (6) · L30 31.3 (12) · projected 28.2
- ESPN: active
- **Rest:** back-to-back Fri 27–Sat 28 Nov; sat the second night of the 25–26 Oct back-to-back, playing the games either side; sat the second night of the 01–02 Nov back-to-back, playing the games either side
- News (23 Nov): Nembhard produced 16 points (5-13 FG, 2-3 3Pt, 4-7 FT), two rebounds and eight assists in 32 minutes during Sunday's 113-106 loss to the Knicks.
- News (20 Nov): Nembhard (hip) is available for Friday's game against the Cavaliers, Tony East of Forbes.com reports.
- **Research:** _pending_

### Jonathan Kuminga (MIN, SF/PF, Dr White Slong)

- Rate **28.6** · season 28.7 (17) · L7 30.7 (3) · L15 27.8 (6) · L30 27.8 (15) · projected 26.3
- ESPN: active
- **Rest:** back-to-back Tue 01–Wed 02 Dec; sat the second night of the 16–17 Nov back-to-back, playing the games either side
- News (24 Nov): Kuminga contributed 15 points (5-12 FG, 1-5 3Pt, 4-6 FT), five rebounds, four assists and one steal in 26 minutes during Monday's 142-116 win over the Nets.
- News (19 Nov): Kuminga totaled 23 points (7-13 FG, 2-4 3Pt, 7-7 FT), three rebounds, three assists and three blocks in 35 minutes during Thursday's 102-99 loss to the Knicks.
- **Research:** _pending_

### Derrick White (BOS, PG/SG, Dr White Slong)

- Rate **28.1** · season 29.5 (17) · L7 25.7 (3) · L15 27.1 (7) · L30 29.0 (15) · projected 37.0
- ESPN: active
- **Rest:** back-to-back Sun 29–Mon 30 Nov; news on 21 Nov: "The veteran guard will be in street clothes for the first leg of the Celtics' back-to-back set, but he could make his return Sunday against the Warriors."; sat the first night of the 21–22 Nov back-to-back, playing the games either side
- News (23 Nov): White amassed 14 points (6-21 FG, 2-12 3Pt), three rebounds, five assists and one steal over 32 minutes during Sunday's 88-87 loss to the Warriors.
- News (22 Nov): White (shoulder) is not listed on the injury report for Sunday's game against Golden State, Justin Turpin of WEEI.com reports.
- **Research:** _pending_

## Sources

- ESPN fantasy player news (`site.api.espn.com/apis/fantasy/v2/games/fba/news/players`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-25 09:06 UTC.
