# Injury Watch: 17 Nov 2026

- Generated 2026-11-17 21:18 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 107 players in ESPN's injury feed. 35 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 19 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1101 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (16 Nov–22 Nov) / next week (23 Nov–29 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

Pickups whose gain should last through this week (16–22 Nov):
- **Derik Queen** (NO): Murphy is out again on 18 Nov (no timetable reported; *ESPN est.* 20 Nov), and Dejounte Murray is away from the team until he is traded.
- **Aday Mara** (OKC): about 25 min while Chet Holmgren is out (patellar tear, 8–10 weeks from 30 Oct; *ESPN est.* 2 Jan).
- **Tyrese Proctor** (CLE): started for Evan Mobley, who is re-evaluated about 23–26 Nov (*ESPN est.* 29 Nov). The 48.0 FP/g without Mobley includes the 14 Nov game Cleveland played without its whole starting five.
- **Derrick Jones Jr.** (LAC): a starter with Bradley Beal out (no timetable reported; *ESPN est.* 29 Nov). Brandon Ingram has no firm return date (*ESPN est.* 19 Nov).
- **Neemias Queta** (BOS): "good to go" for 18 Nov at Denver.

The plan that uses them is in the 17 Nov matchup report.

## Research

Earlier notes still hold ([20261116-injury-watch.md](20261116-injury-watch.md)). New since then:

**Cleveland, Chicago and Milwaukee:**
- **Evan Mobley:** Left great toe sprain from the 11 Nov win at New York, confirmed by MRI. The Cavs say he will get 7 to 10 days of treatment and rehab before he is **re-evaluated**, so the check lands around 23-26 Nov and is not a return date. He has missed three straight games (MIA, DAL, CHI). Atkinson: "we don't expect it to be a long-term thing at all." No first game has been named. ([HEAVY, 16 Nov 2026](https://heavy.com/sports/nba/cleveland-cavaliers/evan-mobley-injury-update-cavaliers-return-timeline/); [Hoops Wire, 16 Nov 2026](https://hoopswire.com/cavs-evan-mobley-out-at-least-another-week-with-toe-injury/))
  - The Akron Beacon Journal says he is "out at least one more week." No minutes limit has been reported. His starting power forward job is waiting for him, and the frontcourt minutes are being covered by Thomas Bryant, Norchad Omier and Mario Hezonja. ESPN's 29 Nov estimate sits just after the re-evaluation window. ([Akron Beacon Journal via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html))
- **Sam Merrill:** Out for six straight games with "right elbow injury management." He hurt it in the first half against Philadelphia on 6 Nov, and he was out again on 16 Nov against Chicago. **No timetable reported.** RotoWire expects Tyrese Proctor and Meleek Thomas to take most of his backcourt minutes. ([Akron Beacon Journal via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html); [CBS/RotoWire, 15 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/cavaliers-sam-merrill-missing-sixth-straight-game-monday/))
  - Atkinson on 8 Nov: "Of course there's a level of concern there… hopefully it won't be too long." No update has come since, so ESPN's 18 Nov estimate is unconfirmed. ([Fear the Sword via Yahoo, 8 Nov 2026](https://sports.yahoo.com/articles/cavs-level-concern-sam-merrill-003658864.html))
- **Nae'Qwan Tomlin:** Lower back stress reaction, confirmed by MRI. The team said it would **re-evaluate him in about 3 to 4 weeks** from 20 Oct, which means roughly 10-17 Nov, and gave no return-to-basketball timeline. ([Cavaliers release, 20 Oct 2026](https://www.nba.com/cavaliers/news/releases-naeqwan-tomlin-261020))
  - No result from that re-evaluation has been reported. On 11 Nov he had been out about three weeks, and his return depends on medical clearance. ESPN's 18 Nov estimate is not backed by any team news. If he comes back, he is a fringe rotation forward (5.8 points in 2025-26). ([Cavaliers On SI via Yahoo, 11 Nov 2026](https://sports.yahoo.com/articles/3-young-cavaliers-could-earn-192714593.html))
- **Peyton Watson:** Head injury: he fell hard and hit his head after colliding with Jalen Smith in the 4th quarter on 16 Nov against Chicago. He walked off and did not return, after 14 points and 4 rebounds in 22 minutes. Atkinson had no update after the game. The Cavs have not confirmed concussion protocol. **No timetable reported.** ([CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/cavaliers-peyton-watson-does-not-return-monday/); [Akron Beacon Journal via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html))
  - He already had a hamstring issue (sat out DAL on 14 Nov) and abdominal soreness (questionable before CHI). If he enters concussion protocol, ESPN's 18 Nov estimate is likely too early. ([TSN, 14 Nov 2026](https://www.tsn.ca/nba/article/cavaliers-without-starting-five-vs-mavericks-after-flight-delay-n1-50485303/))
- **Norchad Omier:** He is a **two-way** forward, called a "rebounding revelation." He played 27 minutes (13 points, 8 rebounds) on 14 Nov against Dallas, a game the Cavs played without their whole starting five, then 13 minutes (4 points, 6 rebounds, 1 block) on 16 Nov against Chicago once the starters were back. Atkinson: "I know it's two games, but pretty impressed." ([Akron Beacon Journal via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html))
  - His 20 min and 30.0 FP/g (2 games, **small sample**) lean on the Dallas game with no starters. With the starters back, his role is about 13 bench minutes. Mobley's return, and a two-way contract's game limit, would shrink it further. ([SB Nation grades via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/player-grades-cavs-vs-bulls-023420546.html))
- **Thomas Bryant:** He started on 14 Nov against Dallas only because Mitchell, Harden, Allen, Watson and Mobley all sat after an FAA ground stop kept the team in Miami. He scored 19 points. ([TSN, 14 Nov 2026](https://www.tsn.ca/nba/article/cavaliers-without-starting-five-vs-mavericks-after-flight-delay-n1-50485303/))
  - On 16 Nov against Chicago, with Jarrett Allen back (13 points, 14 rebounds), he came off the bench: 9 points, 5 rebounds, 4 assists, graded A. He is the backup center. His 28.3 FP/g over 3 games is inflated by the starters-out game, and Mobley's return cuts the frontcourt minutes. ([SB Nation grades via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/player-grades-cavs-vs-bulls-023420546.html))
- **Caleb Wilson:** He fractured his right hand on 11 Nov against San Antonio and had surgery on 12 Nov. The Bulls will **re-evaluate him in three weeks** (about 3 Dec), and the full recovery is **4 to 6 weeks**, so 10-24 Dec. No return date has been given. ESPN's 13 Dec estimate is at the early end. ([Bulls On SI, 13 Nov 2026](https://www.si.com/nba/bulls/onsi/bulls-injury-report-first-game-without-caleb-wilson-will-norman-powell-return-13); [Chicago Tribune via Yahoo, 13 Nov 2026](https://sports.yahoo.com/articles/chicago-bulls-matas-buzelis-step-210500659.html))
  - A starting role is waiting for him: he led the team with 16.2 FGA per game. This is his third significant hand injury of 2026. No minutes limit on his return has been reported yet. ([Bulls On SI, 13 Nov 2026](https://www.si.com/nba/bulls/onsi/what-caleb-wilson-s-injury-means-for-the-bulls-rotation-who-can-fill-the-void-12))
- **Matas Buzelis:** He has started all three games without Wilson, as the power forward in a Giddey / Powell / Okoro / Buzelis / Smith lineup. He scored 18 points with 9 rebounds against Minnesota on 14 Nov and a season-high 23 points (8-14 FG, 3-6 3PT) at Cleveland on 16 Nov. Bulls On SI called it "one of the best Matas Buzelis games yet." ([NBC Sports/Rotoworld, 13 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/bulls-start-giddey-powell-okoro-buzelis-smith); [Bulls On SI grades, 17 Nov 2026](https://www.si.com/nba/bulls/onsi/7-bulls-player-grades-giddey-doesn-t-close-vs-cavs-buzelis-takes-a-step-16))
  - Wilson's 16.2 FGA have opened up, after Buzelis's slow start (13.5 points, 2.8 turnovers through 10 games). The Tribune notes that Splitter had sometimes used him as the first player off the bench while Wilson was healthy, so Wilson's return could cut his role. ([Chicago Tribune via Yahoo, 13 Nov 2026](https://sports.yahoo.com/articles/chicago-bulls-matas-buzelis-step-210500659.html))
- **Isaac Okoro:** **What changed:** Wilson's injury moved Okoro into the starting five at small forward from 13 Nov, with Powell back at the 2. His minutes jumped: a season-high 41 in the OT win over Atlanta (15 points, 3 rebounds, 1 steal, 1 block). Before that he had averaged 6.1 points, and RotoWire calls him a deep-league streamer with limited upside. ([CBS/RotoWire, 14 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bulls-isaac-okoro-stuffs-stat-sheet-friday/); [NBC Sports/Rotoworld, 13 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/bulls-start-giddey-powell-okoro-buzelis-smith))
  - On 16 Nov at Cleveland he had 13 points, 6 rebounds, 2 assists and 4 steals, called the "best two-way basketball of his career." He is projected to start again at Brooklyn on 18 Nov. Wilson's return would likely send him back to the bench, as before 13 Nov apart from his 8 Nov spot start. Norman Powell limped off on 16 Nov but returned to the game. ([Bulls On SI grades, 17 Nov 2026](https://www.si.com/nba/bulls/onsi/7-bulls-player-grades-giddey-doesn-t-close-vs-cavs-buzelis-takes-a-step-16); [CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-heads-to-locker-room/))
- **Ousmane Dieng:** He broke a finger on his left hand (his non-shooting hand), probably in his first start on 13 Nov at Orlando. It was first listed as a sprain. Surgery was set for 16 Nov. The team has given **no firm timeline**. Dieng himself hopes to be back "within a couple of weeks": "I was scared at first, that it would be longer than that." ([Milwaukee Journal Sentinel via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/milwaukee-bucks-ousmane-dieng-surgery-004603339.html))
  - Jenkins said there would be no update until after the procedure, and none has been reported yet. NBC Sports lists him as out indefinitely. Gary Trent Jr., Nate Ament and AJ Green are named as the players likely to take his minutes. ESPN's 14 Dec estimate is longer than Dieng's own two-week hope. ([NBC Sports/Rotoworld, 15 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ousmane-dieng-finger-to-undergo-surgery-monday))
- **Ryan Rollins:** Illness: he was a late addition as questionable on 15 Nov, then ruled out against Atlanta, his first absence of the season. He had played 30 minutes off the bench on 13 Nov at Orlando. ([NBC Sports/Rotoworld, 15 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ryan-rollins-illness-downgraded-to-out-sunday))
  - He is listed day-to-day for Wednesday's game at Miami (18 Nov). **No timetable reported** beyond that. His return is the main threat to the Trent and Jakucionis minutes. ([FOX Sports/AP preview, 17 Nov 2026](https://www.foxsports.com/articles/nba/milwaukee-takes-on-miami-on-10game-skid))
- **Gary Trent Jr.:** He scored 18 points (4-12 3PT, 3 steals) in a season-high 30 minutes **off the bench** on 15 Nov against Atlanta, with both Dieng and Rollins out. RotoWire warns he may not keep that usage once Rollins returns. ([RotoWire, 16 Nov 2026](https://www.rotowire.com/basketball/headlines/gary-trent-news-strikes-for-18-off-bench-sunday-539360))
  - Before this he had mostly played mop-up minutes, with DNPs for about the first dozen games and 16 minutes / 1 point on 13 Nov. Jenkins moved him into the main bench unit and wants to give it "some runway." His 35.0 FP/g rests on **1 game (small sample)**. ([Behind the Buck Pass, 13 Nov 2026](https://behindthebuckpass.com/taylor-jenkins-finally-gary-trent-jr-chance-backfired); [Milwaukee Journal Sentinel via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/bucks-coach-taylor-jenkins-tinkers-035758327.html))
- **Brayden Burries:** The rookie has been the starting point guard since early November, ahead of Ryan Rollins, and he started again on 15 Nov: 13 points, 8 rebounds, 4 assists, 2 steals in 29 minutes. His role does not depend on Dieng. As a starter he averages 9.9 points, 6.6 rebounds and 3.1 assists, but shoots 38.4% FG and 25% 3PT. ([CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-solid-effort-in-sundays-loss/))
  - RotoWire describes a "heated battle" with Rollins for the job, so Rollins's return is the risk, not Dieng's. Jenkins has used five different starting lineups in five games. No source ties his 31 minutes to Dieng's absence. ([RotoWire, 9 Nov 2026](https://www.rotowire.com/basketball/headlines/brayden-burries-news-holding-down-starting-job-538340); [Milwaukee Journal Sentinel via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/bucks-coach-taylor-jenkins-tinkers-035758327.html))
- **Kasparas Jakucionis:** **What changed:** with Rollins out sick, he played backup point guard on 15 Nov and set a career high: 25 points (9-16 FG, 4-10 3PT), 5 rebounds, 5 assists and 3 steals in 26 minutes. His previous best was 16. RotoWire says he "has struggled to get consistent minutes when the roster is healthy." ([CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bucks-kasparas-jakucionis-career-night-in-losing-effort/); [Bucks On SI via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/lineup-shifting-bucks-start-fast-035646209.html))
  - His minutes before that game: 22.4 per game over the first 7 games, then 11, 10, 7, 23 (Knicks), 4 (Lakers) and a DNP at Orlando on 13 Nov. His L7 of 29.3 against a season of 17.7 is driven by Rollins's absence. A healthy Rollins, possibly back on 18 Nov, puts the role at risk. ([Behind the Buck Pass, 15 Nov 2026](https://behindthebuckpass.com/bucks-risk-stunting-kasparas-jakucionis-growth-rapid-rotation-changes))

**Back soon, yet to play, and other pickups:**
- **Brandon Williams:** **Timeline:** He has a mild left hamstring strain from 9 Nov. The MRI showed no tear, and the team set a one-week re-evaluation ([Warriors.com, 10 Nov](https://www.nba.com/warriors/news/brandon-williams-injury-update-20261110)). Kerr says he will likely miss all three remaining road games: Mon at NOP, Wed at DAL and Thu at MEM. He gave no return date. The next game is at home vs BOS on Sun 22 Nov, which matches ESPN's estimate ([Yahoo Sports, 16 Nov](https://sports.yahoo.com/articles/steve-kerr-gives-injury-key-202942500.html)). No minutes restriction has been reported.
  - **Role waiting:** He averaged 10.4 pts in 16.1 min as the backup guard ([AP via NBA.com, 11 Nov](https://www.nba.com/news/warriors-reserve-guard-brandon-williams-strains-left-hamstring-and-will-miss-at-least-a-week)). Stephen Curry tore an oblique and is out at least two weeks before re-evaluation ([AP via NY1, 12 Nov](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/11/12/warriors-star-stephen-curry-suffers-torn-oblique-muscle-and-will-be-sidelined-at-least-two-weeks)). Williams should come back to a bigger guard role than the one he left.
- **Dereck Lively II:** **Timeline: no timetable reported.** On 11 Nov he was listed out vs MIN. RotoWire called his rehab "trending favorably" but still week-to-week, with Daniel Gafford expected to keep starting. In September it warned of a possible heavy minutes restriction on his return ([CBS Sports/RotoWire player news, 11 Nov](https://www.cbssports.com/nba/players/28951880/dereck-lively-ii/)). Dusty May said "major progress" but did not know a timetable ([Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/)).
  - **ESPN's date looks optimistic.** The Wed 18 Nov preview vs GS still describes him as out after foot surgery on the team's latest reports ([Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)). No source reports him practising.
- **Maxime Raynaud:** **Timeline:** He suffered a right patellar subluxation in the preseason ([Kings.com, 11 Oct](https://www.nba.com/kings/news/maxime-raynaud-medical-update)). He was ruled out vs OKC on 15 Nov, his 13th straight missed game. RotoWire says he is "getting closer" to his debut, and his next chance is Wed 18 Nov vs PHX ([CBS Sports/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-wont-play-sunday/)). The team has given no official timeline; James Ham reports he is progressing ([NBC Sports/Rotoworld, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)).
  - **Role waiting:** He would be the backup centre. Sabonis starts at C, and Dylan Cardwell and Precious Achiuwa have covered the frontcourt minutes ([NBC Sports, 15 Nov lineup](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/sac-starts-acuff-monk-murray-cardwell-sabonis); [NBC Sports, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)). No minutes restriction has been reported.
- **Brandon Ingram:** **Timeline: no firm date reported.** He travels with the team on the coming road trip through Texas. Asked about a return during the trip, Ty Lue said: "I hope but don't expect" ([ClutchPoints, 15 Nov](https://clutchpoints.com/nba/los-angeles-clippers/clippers-brandon-ingram-injury-update-teases-return-coming-very-soon)). He is listed OUT (right heel surgery) for Tue 17 Nov vs UTA and has not debuted ([SI Jazz On SI, 17 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-vs-la-clippers-injury-report-who-s-trending-to-miss-game)). ESPN's 19 Nov is earlier than anything reported. No minutes restriction has been reported yet.
  - **Role waiting:** He is expected to move into a starting forward spot when he returns ([Yahoo Sports, 1 Oct](https://sports.yahoo.com/articles/ty-lue-reveals-clippers-still-100038552.html)).
- **Bradley Beal:** **Timeline: no timetable reported.** Lue on 12 Nov: "Every time we get him on the court to do something three days in a row, then it's like, it's not good results." The hip is cleared, and the knee is the problem ([USA Today via Yahoo, 13 Nov](https://sports.yahoo.com/articles/clippers-bradley-beal-still-sidelined-071547162.html)).
  - He is listed OUT (right knee injury management) for 17 Nov vs UTA. He has not played since 8 Nov 2025 ([SI Jazz On SI, 17 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-vs-la-clippers-injury-report-who-s-trending-to-miss-game)). No role for his return has been reported. A setback in the ramp-up makes ESPN's 29 Nov a soft date.
- **Tobias Harris:** **Timeline:** Chris Haynes reports he should start on-court practice work next week (week of 16 Nov) and could debut as early as early December. The team has given no official date ([ClutchPoints, 14 Nov](https://clutchpoints.com/nba/san-antonio-spurs/spurs-news-tobias-harris-gets-crucial-injury-update-after-warriors-game); [Heavy, 15 Nov](https://heavy.com/sports/nba/san-antonio-spurs/tobias-harris-injury-update-return-timeline/)). That matches ESPN's 3 Dec.
  - **Role waiting:** He was signed as the starting PF, but the Spurs start Fox, Castle, Harper, Vassell and Wembanyama. Harris and Champagnie come off the bench, so his role is likely smaller than expected ([Air Alamo, 20 Oct](https://airalamo.com/spurs-lineup-shakeup-creates-tobias-harris-sized-problem-they-cant-ignore)).
- **Duncan Robinson:** **Timeline:** He left the 14 Nov game at MIA in the second quarter. Pistons PR says he will be re-evaluated in a week, which points to about 24 Nov. Rotoworld says the strain could cost him multiple games depending on its grade ([NBC Sports/Rotoworld, 17 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week)). He is ruled out for Tue 17 Nov at SAS ([NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/duncan-robinson-quad-ruled-out-tuesday-vs-sas)).
  - **Role waiting:** He was a starter, averaging a career-high 17.4 pts on 43.1% from three ([BVM Sports, 17 Nov](https://bvmsports.com/2026/11/17/duncan-robinson-injury-pistons-star-out-at-least-one-week/)). Kevin Huerter replaced him in the second half on 14 Nov and is the main beneficiary while he is out: 16.8 pts over his last four games, "worth adding in all formats" ([NBC Sports/Rotoworld, 17 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week)).
- **Tyrese Haliburton:** **Timeline: no timetable reported.** Rick Carlisle on 17 Nov: "There's no definite timeline on him… He's getting there." On a November return: "I don't think it's out of the question, but we're not in any position to put a hard date on anything… There's nothing happening in the near term." He has not played since 26 Oct ([IndyStar via Yahoo, 17 Nov](https://sports.yahoo.com/articles/rick-carlisle-no-definite-timeline-174500802.html)).
  - **Role waiting:** He returns to his full starting PG role. Until then Andrew Nembhard takes on more of the ball-handling and Quenton Jackson gets more minutes ([CBS Sports/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-firm-timetable-for-return/)). ESPN's 28 Nov fits Carlisle's "not out of the question" but is not a reported date.
- **Javon Small:** **Why his L7 is up:** Ty Jerome (right hip) missed the 14 and 16 Nov games. Small then played 29+ min in two straight games: 19 pts vs BKN, then 12 pts, 5 reb and 12 ast in 29 min off the bench at WAS on 16 Nov (his first career double-double). RotoWire: "a useful add, even in standard leagues" while Jerome sits, but the two-way contract caps his games ([CBS Sports/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-javon-small-first-career-double-double/)). Before that he averaged 18.8 min over four games ([CBS Sports/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-javon-small-productive-in-blowout-win/)).
  - **Does it end?** Jerome's return is the main threat. His next chance is Wed 18 Nov at CLE ([CBS Sports/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-ty-jerome-listed-out-for-monday/)). Scotty Pippen Jr. (lumbar disc herniation, out since 29 Oct) is still week-to-week with no firm timetable. RotoWire says Cam Spencer and Small keep the extra minutes while he is out ([RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/scotty-pippen-injury-still-viewed-as-week-to-week-539414)).
- **Jordan Goodwin:** **Role:** He comes off the bench. Back from a calf injury on 10 Nov, he scored 18 pts (6-7 from three) in 14 min. RotoWire calls him a deeper-league streamer whose minutes "could fluctuate" with Kennard, Gillespie and Dunn ([Fox Sports/RotoWire, 10–11 Nov](https://www.foxsports.com/nba/jordan-goodwin-player)). His 31 min (14 pts, 7 reb, 6 ast) vs LAL on 15 Nov came partly because Ott left the bench in for the whole fourth quarter of a comeback from 24 down ([Yahoo/Bright Side of the Sun, 16 Nov](https://sports.yahoo.com/articles/game-recap-furious-comeback-suns-004939671.html); [Covers box score, 15 Nov](https://www.covers.com/sport/basketball/nba/matchup/388723)). He came off the bench again at DEN on 16 Nov ([VAVEL, 16 Nov](https://www.vavel.com/en-us/nba/2026/11/16/1279471-nuggets-vs-suns-live-score-updates-and-play-by-play-nba.html)).
  - **Does it end?** Mark Williams (left shoulder labrum surgery) is expected to miss at least five months, about mid-February ([BVM Sports, 11 Sep](https://bvmsports.com/2026/09/11/suns-mark-williams-likely-to-miss-five-months-after-shoulder-surgery/)). His return won't cut into Goodwin's minutes soon, and Williams is a centre anyway. The real limits are the guard competition and blowout or comeback minutes.
- **De'Andre Hunter:** **Status:** He was a late addition to the report and was then ruled out vs OKC on 15 Nov with a hip injury ([CBS Sports/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-downgraded-to-out/)). The team calls it left hip soreness/tightness and lists him day-to-day ([Sactown Sports, 15 Nov](https://sactownsports.com/nba/sacramento-kings/okc-loss)). The Kings' next game is Wed 18 Nov vs PHX, which matches ESPN's estimate. No report on that game yet.
  - **Role:** He is a regular starter, back in the lineup since 8 Nov. He scored 24 pts (7-13 FG) in 41 min vs POR on 14 Nov ([NBC Sports/Rotoworld, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/deandre-hunter-hip-now-questionable-sunday)). LaVine (illness) and Achiuwa (ankle) also sat on 15 Nov, and the extra minutes went to Black, Sharp, Murray and Monk ([CBS Sports/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-downgraded-to-out/)).

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: Rudy Gobert 27.8 (L7 31.0), Daniss Jenkins 28.7 (L7 31.5), Saddiq Bey 30.7 (L7 39.8), Trey Murphy III 31.0 (L7 —), Jalen Duren 33.5 (L7 —). A pickup at or above **33.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Tyrese Proctor** | CLE | Evan Mobley (29 Nov); also out: Sam Merrill (18 Nov), Nae'Qwan Tomlin (18 Nov) | 3 | 30.0 | +9.0 | **48.0** | 23.2 | 41.2 (4) | 28.3 (9) | 23.2 (14) | Free agent | 15% | 2 / 3 |
| **Gary Trent Jr.** | MIL | Ousmane Dieng (14 Dec) | 1 | 30.0 | +22.2 | **35.0** | 10.2 | 12.8 (4) | 12.8 (4) | 10.2 (6) | Free agent | 0% | 3 / 4 |
| **Brayden Burries** | MIL | Ousmane Dieng (14 Dec) | 3 | 31.0 | +8.6 | **34.7** | 21.8 | 19.0 (4) | 25.1 (8) | 21.8 (14) | Free agent | 6% | 3 / 4 |
| **Brandon Williams** (out, ESPN est. back 22 Nov) | GS | Stephen Curry (12 Dec), Kristaps Porzingis (02 Jan), Moses Moody (01 Dec), Jimmy Butler III (02 Jan) | 1 | 25.0 | +10.8 | **33.0** | 18.8 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% | 3 / 3 |
| **Matas Buzelis** | CHI | Caleb Wilson (13 Dec) | 3 | 30.0 | +3.4 | **33.0** | 23.3 | 27.0 (4) | 25.0 (7) | 23.3 (13) | Free agent | 64% | 3 / 3 |
| **Isaac Okoro** | CHI | Caleb Wilson (13 Dec) | 3 | 34.7 | +16.0 | **30.7** | 14.9 | 24.5 (4) | 18.4 (7) | 14.9 (13) | Free agent | 0% | 3 / 3 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 10 | 24.4 | — | **30.5** | 26.6 | 32.0 (4) | 31.9 (8) | 26.6 (14) | Free agent | 23% | 3 / 3 |
| **Norchad Omier** | CLE | Evan Mobley (29 Nov); also out: Sam Merrill (18 Nov), Nae'Qwan Tomlin (18 Nov) | 2 | 20.0 | +12.5 | **30.0** | 17.8 | 30.0 (2) | 17.8 (4) | 17.8 (4) | Free agent | 0% | 2 / 3 |
| **Mo Bamba** | UTAH | Lauri Markkanen (04 Jan), Jaren Jackson Jr. (14 Dec); also out: Jusuf Nurkic (20 Nov) | 6 | 20.7 | +6.0 | **29.8** | 29.6 | 34.8 (4) | 30.6 (7) | 29.6 (10) | Free agent | 16% | 4 / 3 |
| **Thomas Bryant** | CLE | Evan Mobley (29 Nov); also out: Sam Merrill (18 Nov), Nae'Qwan Tomlin (18 Nov) | 3 | 20.3 | +7.8 | **28.3** | 19.3 | 28.3 (3) | 19.2 (8) | 19.3 (9) | Free agent | 0% | 2 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 9 | 28.6 | +3.2 | **28.0** | 28.7 | 31.3 (3) | 29.8 (5) | 28.7 (11) | Free agent | 16% | 3 / 4 |
| **Jordan Goodwin** | PHX | Mark Williams (03 Feb) | 6 | 20.7 | — | **27.8** | 26.6 | 29.2 (4) | 26.0 (5) | 26.6 (9) | Free agent | 3% | 2 / 4 |
| **Kasparas Jakucionis** | MIL | Ousmane Dieng (14 Dec) | 3 | 19.3 | +5.0 | **27.3** | 17.7 | 29.3 (3) | 16.9 (7) | 17.7 (13) | Free agent | 1% | 3 / 4 |
| **Kris Dunn** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (19 Nov) | 10 | 26.4 | +4.4 | **26.8** | 28.1 | 12.7 (3) | 20.0 (6) | 28.1 (12) | Free agent | 31% | 3 / 4 |
| **Quenton Jackson** | IND | Tyrese Haliburton (28 Nov), Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 10 | 23.2 | — | **26.4** | 23.8 | 22.0 (3) | 26.9 (7) | 23.8 (14) | Free agent | 4% | 3 / 3 |
| **Javon Small** | MEM | Scotty Pippen Jr. (25 Nov), GG Jackson (18 Jan); also out: Isaiah Stewart (18 Nov) | 2 | 25.0 | +4.2 | **26.0** | 23.7 | 28.8 (4) | 25.3 (6) | 23.7 (7) | Free agent | 1% | 3 / 4 |
| **De'Andre Hunter** (day to day, ESPN est. back 18 Nov) | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (18 Nov) | 8 | 35.4 | +7.8 | **25.6** | 21.6 | 33.0 (2) | 21.0 (5) | 21.6 (11) | Free agent | 6% | 3 / 3 |
| **Ryan Kalkbrenner** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 4 | 22.5 | +6.7 | **24.5** | 21.1 | 19.0 (2) | 22.2 (6) | 21.1 (13) | Free agent | 2% | 2 / 3 |
| **Buddy Hield** | CHI | Caleb Wilson (13 Dec) | 3 | 21.3 | +9.5 | **24.3** | 15.8 | 24.3 (3) | 21.0 (5) | 15.8 (11) | Free agent | 1% | 3 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (12 Dec) | 10 | 25.2 | +4.9 | **24.0** | 26.1 | 14.0 (2) | 23.4 (7) | 26.1 (14) | Free agent | 35% | 3 / 2 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (18 Nov) | 8 | 21.8 | — | **23.6** | 21.0 | 20.7 (3) | 25.3 (7) | 21.0 (9) | Free agent | 0% | 3 / 3 |
| **Sion James** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov) | 4 | 30.2 | +5.1 | **20.2** | 15.8 | 15.0 (2) | 21.0 (6) | 15.8 (13) | Free agent | 1% | 2 / 3 |

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Jalen Duren. A stash costs a bench spot until it frees up.

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Dejounte Murray** | NO | Ankle | 20 Nov | 3 | 30.6 | 13.0 (1) | 20.8 (5) | 30.6 (9) | 39.0 | 36.5 | Free agent | 79% | 3 / 3 |
| **Ja Morant** | POR | Left Hamstring | 01 Dec | 14 | 33.8 | — | — | 33.8 (4) | 37.5 | 36.0 | Free agent | 80% | 3 / 4 |
| **Ryan Rollins** | MIL | Illness | 18 Nov | 1 | 23.3 | 24.0 (3) | 22.7 (7) | 23.3 (13) | 31.9 | 37.5 | Free agent | 46% | 3 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 3 | — | — | — | — | 27.6 | 36.7 | Free agent | 6% | 4 / 3 |
| **Neemias Queta** | BOS | Rest | 18 Nov | 1 | 25.6 | 27.7 (3) | 27.9 (7) | 25.6 (13) | 27.2 | 33.4 | Free agent | 22% | 3 / 3 |
| **Santi Aldama** | DAL | Left Ankle Sprain | 18 Nov | 1 | 14.8 | 12.5 (2) | 14.8 (5) | 14.8 (5) | 25.0 | 32.4 | Free agent | 5% | 3 / 2 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 25 Nov | 8 | 14.2 | — | — | 14.2 (5) | 30.6 | 27.1 | Free agent | 8% | 3 / 4 |
| **Duncan Robinson** | DET | Left Quadriceps Strain | 27 Nov | 10 | 29.8 | 16.0 (2) | 29.5 (6) | 29.8 (12) | 21.6 | 23.1 | Free agent | 49% | 4 / 3 |
| **Peyton Watson** | CLE | Head | 18 Nov | 1 | 24.2 | 16.3 (3) | 21.3 (6) | 24.2 (12) | 29.3 | 29.8 | Free agent | 38% | 2 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle | 18 Nov | 1 | 19.2 | 20.3 (3) | 20.3 (3) | 19.2 (8) | 25.6 | 28.3 | Free agent | 2% | 2 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 18 Nov | 1 | — | — | — | — | — | 28.1 | Free agent | 2% | 3 / 3 |
| **Precious Achiuwa** | SAC | Left Ankle Soreness | 18 Nov | 1 | 28.0 | 18.0 (1) | 24.0 (5) | 28.0 (11) → 30.5 (10) | 24.1 | 27.0 | Free agent | 16% | 3 / 3 |
| **Bennedict Mathurin** | NO | Left Foot Plantar Fasciitis | 20 Nov | 3 | 8.8 | -3.0 (1) | 4.5 (6) | 8.8 (12) | 25.1 | 27.6 | Free agent | 6% | 3 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 1 | — | — | — | — | 27.4 | 21.3 | Free agent | 4% | 3 / 2 |
| **Jaxson Hayes** | UTAH | Left Knee Strain | 18 Nov | 1 | 27.2 | 23.3 (3) | 23.7 (7) | 27.2 (12) | 16.5 | 20.2 | Free agent | 9% | 4 / 3 |
| **Jock Landale** | ATL | Right Hip Inflammation | 18 Nov | 1 | 16.8 | 19.0 (1) | 18.0 (2) | 16.8 (9) → 18.9 (8) | — | 25.8 | Free agent | 0% | 3 / 2 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 12 | — | — | — | — | 25.6 | 10.5 | Free agent | 1% | 3 / 4 |
| **Isaiah Stewart** | MEM | Illness | 18 Nov | 1 | 21.6 | 18.7 (3) | 19.8 (5) | 21.6 (10) | 25.3 | 25.1 | Free agent | 4% | 3 / 4 |
| **Pelle Larsson** | MIA | Illness | 18 Nov | 1 | 25.1 | 28.0 (1) | 21.8 (5) | 25.1 (11) | — | 23.7 | Free agent | 8% | 2 / 3 |

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 33.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Dereck Lively II** | DAL | Right Foot Surgery | 18 Nov | 1 | 27.4 (23.6) | 21.3 (7) | Free agent | 4% | 3 / 2 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 18 Nov | 1 | — (—) | 28.1 (74) | Free agent | 2% | 3 / 3 |
| **Brandon Ingram** | LAC | Right Achilles Surgery | 19 Nov | 2 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 3 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 3 | 27.6 (23.1) | 36.7 (41) | Free agent | 6% | 4 / 3 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 12 | 25.6 (25.3) | 10.5 (6) | Free agent | 1% | 3 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 03 Dec | 16 | 30.1 (30.5) | 28.0 (63) | Free agent | 41% | 3 / 4 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 46 | 38.8 (32.4) | 41.6 (38) | Free agent | 28% | 3 / 3 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 46 | 36.9 (27.7) | 32.3 (32) | Free agent | 32% | 3 / 3 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 78 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 2 / 4 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 105 | 24.8 (25.4) | 31.2 (50) | Free agent | 6% | 3 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 136 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 3 / 4 |

## Our injured players

- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Trey Murphy III** (NO): Out, Knee Tendinitis; ESPN est. back 20 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Illness; ESPN est. back 17 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

## Who takes the minutes, team by team

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Stephen Curry | Right Abdomen | 12 Dec | 32.0 | 44.4 | Lauri Birds |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Brandon Williams (out, ESPN est. back 22 Nov) | PG/SG | 1 | 25.0 | +10.8 | 0 | **33.0** | 14.2 | — | 15.0 (3) | 18.8 (10) | Free agent | 1% |
| Charles Bassey | C | 3 | 18.7 | +5.8 | 1 | **18.0** | 21.3 | 15.3 (3) | 22.6 (7) | 19.3 (12) | Free agent | 1% |
| LJ Cryer | PG | 3 | 16.7 | +8.7 | 1 | **16.0** | 7.0 | 22.7 (3) | 13.7 (6) | 10.5 (11) | Free agent | 0% |
| Will Richard | SG/SF | 3 | 25.0 | +6.5 | 1 | **15.0** | 13.5 | 17.3 (3) | 15.8 (6) | 13.5 (13) | Free agent | 0% |

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aday Mara | C | 10 | 24.4 | — | 4 | **30.5** | — | 32.0 (4) | 31.9 (8) | 26.6 (14) | Free agent | 23% |
| Kenrich Williams | SF | 10 | 23.9 | +8.5 | 9 | **19.8** | 14.2 | 21.5 (4) | 20.5 (8) | 16.8 (14) | Free agent | 1% |
| Bennett Stirtz | PG | 10 | 21.3 | — | 0 | **19.2** | — | 14.2 (4) | 19.5 (8) | 14.2 (14) | Free agent | 1% |
| Micah Peavy | SF | 9 | 16.4 | — | 0 | **10.1** | — | 6.0 (3) | 12.6 (7) | 10.1 (9) | Free agent | 0% |
| Nikola Topic | PG | 2 | 14.5 | — | 0 | **8.5** | — | 8.5 (2) | 8.5 (2) | 8.5 (2) | Free agent | 0% |

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 12 Jan | 25.7 | 7.0 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Sidy Cissoko | SG | 6 | 25.7 | +5.4 | 4 | **17.0** | 16.2 | 18.0 (4) | 17.9 (8) | 17.6 (13) | Free agent | 1% |
| Chris Youngblood (out, ESPN est. back 19 Nov) | SG | 3 | 18.3 | +9.7 | 0 | **16.7** | 4.3 | 14.0 (1) | 12.2 (5) | 10.5 (6) | Free agent | 0% |

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tyrese Haliburton | Left Hamstring Strain | 28 Nov | 33.1 | 53.2 | Lauri Birds |
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Andrew Nembhard (day to day, ESPN est. back 18 Nov) | PG/SG | 8 | 33.9 | +3.2 | 8 | **34.1** | 28.2 | 28.0 (2) | 31.8 (5) | 33.2 (11) | Matt Wright's Foxies | 70% |
| Quenton Jackson | PG/SG | 10 | 23.2 | — | 2 | **26.4** | — | 22.0 (3) | 26.9 (7) | 23.8 (14) | Free agent | 4% |
| Jay Huff | C | 9 | 17.0 | — | 4 | **16.1** | — | 17.3 (3) | 17.5 (6) | 16.2 (12) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 15.9 | — | 1 | **15.1** | — | 14.0 (3) | 18.0 (6) | 14.2 (12) | Free agent | 0% |
| Braden Smith | PG | 7 | 15.1 | — | 4 | **14.4** | — | — | 24.0 (4) | 12.6 (8) | Free agent | 0% |

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 10 | 33.0 | +3.6 | 10 | **39.1** | 30.4 | 28.3 (3) | 37.0 (7) | 35.4 (14) | Cream Abdul-Yammar | 84% |
| Jonathan Kuminga (out, ESPN est. back 19 Nov) | SF/PF | 10 | 30.6 | +3.3 | 10 | **26.3** | 26.3 | 25.0 (3) | 25.4 (7) | 28.3 (14) | Dr White Slong | 63% |
| Joan Beringer | C | 10 | 17.3 | — | 1 | **18.4** | — | 17.3 (3) | 16.4 (7) | 19.0 (14) | Free agent | 2% |
| Jaylen Clark (out, ESPN est. back 29 Nov) | SG | 9 | 16.9 | +3.8 | 0 | **14.6** | 9.4 | 12.5 (2) | 13.8 (6) | 11.9 (12) | Free agent | 0% |

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Lauri Markkanen | Right Hand Fracture | 04 Jan | 34.4 | 32.5 | Free agent |
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Waivers |

Last 10 games: 6 game(s) without them, 4 with them.

Also out in those games, so part of the gain is theirs: Jusuf Nurkic (right foot strain; ESPN est. 20 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Mo Bamba | C | 6 | 20.7 | +6.0 | 1 | **29.8** | 23.7 | 34.8 (4) | 30.6 (7) | 29.6 (10) | Free agent | 16% |
| Brice Sensabaugh | SG/SF | 6 | 20.8 | +7.1 | 0 | **18.7** | 10.0 | 20.8 (4) | 13.5 (8) | 14.7 (14) | Free agent | 2% |
| Isaiah Collier | PG | 5 | 18.4 | +6.4 | 0 | **15.4** | 10.2 | 18.3 (3) | 12.6 (7) | 14.6 (13) | Free agent | 2% |
| Josh Green | SG | 6 | 22.8 | +6.8 | 5 | **10.3** | 6.2 | 8.8 (4) | 8.9 (8) | 8.5 (12) | Free agent | 0% |

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 4 game(s) without them, 6 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ryan Kalkbrenner | C | 4 | 22.5 | +6.7 | 2 | **24.5** | 16.3 | 19.0 (2) | 22.2 (6) | 21.1 (13) | Free agent | 2% |
| Sion James | SF | 4 | 30.2 | +5.1 | 3 | **20.2** | 16.3 | 15.0 (2) | 21.0 (6) | 15.8 (13) | Free agent | 1% |
| Hannes Steinbach | PF | 2 | 20.0 | +14.5 | 0 | **18.0** | 0.5 | — | 12.7 (3) | 10.0 (5) | Free agent | 1% |
| Christian Anderson | PG | 4 | 19.2 | +9.1 | 0 | **17.2** | 8.6 | 25.5 (2) | 17.2 (5) | 9.8 (12) | Free agent | 0% |
| Royce O'Neale | SF/PF | 4 | 22.5 | +3.0 | 0 | **16.0** | 10.5 | 9.5 (2) | 12.8 (6) | 12.4 (13) | Free agent | 1% |

### MEM

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Scotty Pippen Jr. | Back Soreness | 25 Nov | 25.1 | 14.2 | Free agent |
| GG Jackson | Left Foot Surgery | 18 Jan | 23.0 | 12.4 | Free agent |

Last 10 games: 2 game(s) without them, 8 with them.

Also out in those games, so part of the gain is theirs: Isaiah Stewart (illness; ESPN est. 18 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Javon Small | PG | 2 | 25.0 | +4.2 | 0 | **26.0** | 22.8 | 28.8 (4) | 25.3 (6) | 23.7 (7) | Free agent | 1% |
| Olivier-Maxence Prosper | PF | 2 | 13.5 | +7.3 | 0 | **11.0** | 8.7 | 16.3 (3) | 10.3 (6) | 9.1 (8) | Free agent | 0% |
| Quinten Post | PF/C | 2 | 12.0 | +5.3 | 0 | **3.0** | 8.0 | 7.0 (1) | 2.8 (4) | 9.3 (9) | Free agent | 0% |

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 19 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Derrick Jones Jr. | SF/PF | 9 | 28.6 | +3.2 | 9 | **28.0** | 21.1 | 31.3 (3) | 29.8 (5) | 28.7 (11) | Free agent | 16% |
| Kris Dunn | PG/SG | 10 | 26.4 | +4.4 | 10 | **26.8** | 20.0 | 12.7 (3) | 20.0 (6) | 28.1 (12) | Free agent | 31% |
| Kobe Sanders | SG | 10 | 24.0 | — | 2 | **19.5** | — | 16.3 (3) | 17.5 (6) | 18.8 (12) | Free agent | 1% |

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| CJ McCollum | Left Calf Strain | 19 Dec | 30.2 | 28.9 | Snow Time Lakers |
| Mouhamed Gueye | Left Foot Fracture | 12 Dec | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection. Split on Mouhamed Gueye alone: the others still played in those games.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.2 | +4.9 | 0 | **24.0** | 19.2 | 14.0 (2) | 23.4 (7) | 26.1 (14) | Free agent | 35% |
| Zuby Ejiofor | PF | 6 | 13.5 | — | 0 | **17.7** | — | 12.0 (1) | 17.7 (6) | 13.6 (8) | Free agent | 0% |
| Jock Landale (day to day, ESPN est. back 18 Nov) | C | 5 | 13.0 | — | 0 | **14.2** | — | 19.0 (1) | 18.0 (2) | 16.8 (9) → 18.9 (8) | Free agent | 0% |

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 10 | 34.1 | +4.7 | 10 | **37.2** | 30.2 | 32.5 (4) | 38.3 (9) | 34.6 (15) | Snow Time Lakers | 78% |

### CLE

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Evan Mobley | Left Toe Sprain | 29 Nov | 33.3 | 39.9 | Matt Wright's Foxies |

Last 10 games: 3 game(s) without them, 7 with them.

Also out in those games, so part of the gain is theirs: Sam Merrill (right elbow; ESPN est. 18 Nov), Nae'Qwan Tomlin (back; ESPN est. 18 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Tyrese Proctor | SG | 3 | 30.0 | +9.0 | 2 | **48.0** | 20.3 | 41.2 (4) | 28.3 (9) | 23.2 (14) | Free agent | 15% |
| James Harden | PG/SG | 2 | 34.5 | +3.6 | 2 | **41.5** | 31.9 | 45.3 (3) | 34.2 (8) | 32.8 (14) | Team Nic Kerr | 99% |
| Jarrett Allen | C | 2 | 31.0 | +9.0 | 2 | **36.5** | 32.2 | 40.0 (3) | 29.8 (6) → 35.8 (5) | 35.0 (12) → 38.2 (11) | Dr White Slong | 89% |
| Norchad Omier | PF | 2 | 20.0 | +12.5 | 0 | **30.0** | 5.5 | 30.0 (2) | 17.8 (4) | 17.8 (4) | Free agent | 0% |
| Thomas Bryant | C | 3 | 20.3 | +7.8 | 1 | **28.3** | 14.8 | 28.3 (3) | 19.2 (8) | 19.3 (9) | Free agent | 0% |

### CHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Caleb Wilson | Right Hand | 13 Dec | 32.1 | 34.9 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jalen Smith | PF/C | 2 | 30.0 | +5.4 | 2 | **51.5** | 33.1 | 50.3 (3) | 40.2 (6) → 46.2 (5) | 36.2 (12) → 38.6 (11) | **us** | 38% |
| Matas Buzelis | SF/PF | 3 | 30.0 | +3.4 | 3 | **33.0** | 20.1 | 27.0 (4) | 25.0 (7) | 23.3 (13) | Free agent | 64% |
| Isaac Okoro | SG/SF | 3 | 34.7 | +16.0 | 3 | **30.7** | 11.0 | 24.5 (4) | 18.4 (7) | 14.9 (13) | Free agent | 0% |
| Buddy Hield | SG/SF | 3 | 21.3 | +9.5 | 0 | **24.3** | 12.2 | 24.3 (3) | 21.0 (5) | 15.8 (11) | Free agent | 1% |
| Zach Collins | C | 1 | 28.0 | +21.0 | 1 | **16.0** | 5.2 | 12.0 (2) | 11.2 (4) | 7.0 (8) | Free agent | 0% |

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Duncan Robinson | Left Quadriceps Strain | 27 Nov | 30.6 | 29.8 | Free agent |

Last 10 games: 0 game(s) without them, 10 with them.

No game yet without them. Same-position teammates by current minutes: Ausar Thompson (SF/PF, 27.7 min, 35.7 FP/g, Lauri Birds), Kevin Huerter (SG/SF, 24.4 min, 24.2 FP/g, Free agent), Javonte Green (SF, 16.9 min, 13.8 FP/g, Free agent), Ronald Holland II (SF/PF, 15.9 min, 16.0 FP/g, Free agent).

### SA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Tobias Harris | Left Calf Strain | 03 Dec | 30.5 | 28.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

No teammate has gained 3+ minutes in those games.

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin | PG/SG | 6 | 20.7 | — | 0 | **27.8** | — | 29.2 (4) | 26.0 (5) | 26.6 (9) | Free agent | 3% |

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 18 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.0 | +6.4 | 10 | **42.7** | 30.4 | 31.3 (3) | 40.0 (7) | 38.6 (13) | Team Nic Kerr | 91% |
| De'Andre Hunter (day to day, ESPN est. back 18 Nov) | SF/PF | 8 | 35.4 | +7.8 | 8 | **25.6** | 23.9 | 33.0 (2) | 21.0 (5) | 21.6 (11) | Free agent | 6% |
| Leaky Black | SF | 8 | 21.8 | — | 1 | **23.6** | — | 20.7 (3) | 25.3 (7) | 21.0 (9) | Free agent | 0% |
| Dylan Cardwell | C | 6 | 17.8 | — | 2 | **20.8** | — | 19.7 (3) | 20.8 (6) | 20.8 (6) | Free agent | 1% |
| Emanuel Sharp | SG | 10 | 18.2 | — | 0 | **10.9** | — | 10.3 (3) | 13.9 (7) | 10.6 (13) | Free agent | 0% |

### MIL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ousmane Dieng | Left Finger Surgery | 14 Dec | 19.4 | 7.7 | Free agent |

Last 10 games: 3 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Gary Trent Jr. | SG/SF | 1 | 30.0 | +22.2 | 0 | **35.0** | 5.2 | 12.8 (4) | 12.8 (4) | 10.2 (6) | Free agent | 0% |
| Brayden Burries | SG | 3 | 31.0 | +8.6 | 3 | **34.7** | 20.1 | 19.0 (4) | 25.1 (8) | 21.8 (14) | Free agent | 6% |
| Kasparas Jakucionis | PG | 3 | 19.3 | +5.0 | 0 | **27.3** | 8.8 | 29.3 (3) | 16.9 (7) | 17.7 (13) | Free agent | 1% |

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun | SG/SF | 10 | 33.1 | +5.6 | 10 | **32.1** | 23.1 | 37.3 (3) | 28.6 (7) | 31.1 (12) | Team Nic Kerr | 44% |
| Trevon Brazile | SF/PF | 10 | 18.9 | — | 1 | **16.2** | — | 14.0 (3) | 14.9 (7) | 17.8 (12) | Free agent | 2% |
| Spencer Jones | SF/PF | 5 | 18.0 | — | 0 | **12.8** | — | 10.3 (3) | 12.8 (5) | 12.8 (5) | Free agent | 0% |
| Bryce Hopkins | SF | 6 | 13.8 | — | 1 | **9.2** | — | 0.0 (1) | 9.2 (4) | 7.9 (8) | Free agent | 0% |

## Every injury

All 107 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 318 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 318 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 226 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 136 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 136 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 105 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 105 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 105 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 105 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 100 | Free agent |
| Asa Newell | ATL | Out | Left Toe | 25 Feb | 100 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 78 | Free agent |
| GG Jackson | MEM | Out | Left Foot Surgery | 18 Jan | 62 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 12 Jan | 56 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Hand Fracture | 04 Jan | 48 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 46 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 46 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 46 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 46 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 46 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 34 | Melbourne poopoo |
| CJ McCollum | ATL | Out | Left Calf Strain | 19 Dec | 32 | Snow Time Lakers |
| Ousmane Dieng | MIL | Out | Left Finger Surgery | 14 Dec | 27 | Free agent |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 27 | Waivers |
| Caleb Wilson | CHI | Out | Right Hand | 13 Dec | 26 | Free agent |
| Stephen Curry | GS | Out | Right Abdomen | 12 Dec | 25 | Lauri Birds |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 12 Dec | 25 | Free agent |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 25 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 03 Dec | 16 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 16 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 16 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 14 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 14 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 14 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 12 | Free agent |
| Jaylen Clark | MIN | Out | Right Hamstring | 29 Nov | 12 | Free agent |
| Evan Mobley | CLE | Out | Left Toe Sprain | 29 Nov | 12 | Matt Wright's Foxies |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 12 | Free agent |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 28 Nov | 11 | Lauri Birds |
| Duncan Robinson | DET | Out | Left Quadriceps Strain | 27 Nov | 10 | Free agent |
| Tobe Awaka | CHI | Out | Back | 25 Nov | 8 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 25 Nov | 8 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 8 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 24 Nov | 7 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 7 | **us** |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 23 Nov | 6 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 23 Nov | 6 | — |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 6 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 5 | Dr White Slong |
| Noah Penda | ORL | Out | Right Hamstring Strain | 22 Nov | 5 | Free agent |
| Jonathan Isaac | ORL | Out | Left Knee | 22 Nov | 5 | Free agent |
| Brandon Williams | GS | Out | Left Hamstring | 22 Nov | 5 | Free agent |
| Adem Bona | PHI | Out | Back Sprain | 21 Nov | 4 | Free agent |
| Trey Murphy III | NO | Out | Knee Tendinitis | 20 Nov | 3 | **us** |
| Trendon Watford | NO | Out | Right Ankle Sprain | 20 Nov | 3 | Free agent |
| Thomas Sorber | OKC | Out | Knee | 20 Nov | 3 | Free agent |
| Kevin McCullar Jr. | TOR | Day-To-Day | Illness | 20 Nov | 3 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 3 | Free agent |
| Dejounte Murray | NO | Out | Ankle | 20 Nov | 3 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 20 Nov | 3 | Free agent |
| Bryce McGowens | NO | Out | Left Elbow Infection | 20 Nov | 3 | Free agent |
| Bennedict Mathurin | NO | Out | Left Foot Plantar Fasciitis | 20 Nov | 3 | Free agent |
| Zyon Pullin | MIN | Out | Right Quadriceps Bruise | 19 Nov | 2 | — |
| Jonathan Kuminga | MIN | Out | Right Shoulder | 19 Nov | 2 | Dr White Slong |
| Chris Youngblood | POR | Out | Right Heel Bruise | 19 Nov | 2 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 19 Nov | 2 | Melbourne poopoo |
| Zach LaVine | SAC | Day-To-Day | Illness | 18 Nov | 1 | Team Nic Kerr |
| Walker Kessler | LAL | Out | Right Lower Leg Soreness | 18 Nov | 1 | Snow Time Lakers |
| Ty Jerome | MEM | Day-To-Day | Right Hip Soreness | 18 Nov | 1 | Melbourne poopoo |
| Taurean Prince | DET | Out | Right Knee Soreness | 18 Nov | 1 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 18 Nov | 1 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 18 Nov | 1 | Free agent |
| Santi Aldama | DAL | Day-To-Day | Left Ankle Sprain | 18 Nov | 1 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 18 Nov | 1 | Free agent |
| Ryan Rollins | MIL | Day-To-Day | Illness | 18 Nov | 1 | Free agent |
| Ronald Holland II | DET | Out | Left Knee Bruise | 18 Nov | 1 | Free agent |
| Precious Achiuwa | SAC | Day-To-Day | Left Ankle Soreness | 18 Nov | 1 | Free agent |
| Peyton Watson | CLE | Day-To-Day | Head | 18 Nov | 1 | Free agent |
| Pelle Larsson | MIA | Out | Illness | 18 Nov | 1 | Free agent |
| Patrick Williams | CHI | Day-To-Day | Right Finger Dislocated | 18 Nov | 1 | Free agent |
| Nikola Jovic | MIA | Day-To-Day | Illness | 18 Nov | 1 | Free agent |
| Neemias Queta | BOS | Day-To-Day | Rest | 18 Nov | 1 | Free agent |
| Nae'Qwan Tomlin | CLE | Out | Back | 18 Nov | 1 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 18 Nov | 1 | Free agent |
| Max Christie | DAL | Day-To-Day | Left Ankle Sprain | 18 Nov | 1 | Free agent |
| LeBron James | PHI | Day-To-Day | Back | 18 Nov | 1 | Cream Abdul-Yammar |
| Kyrie Irving | DAL | Day-To-Day | Left Knee | 18 Nov | 1 | Snow Time Lakers |
| Kingston Flemings | ATL | Day-To-Day | Back Strain | 18 Nov | 1 | Free agent |
| Jock Landale | ATL | Day-To-Day | Right Hip Inflammation | 18 Nov | 1 | Free agent |
| Jaylon Tyson | CLE | Day-To-Day | Right Ankle | 18 Nov | 1 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 18 Nov | 1 | Free agent |
| Jaylen Brown | PHI | Day-To-Day | Left Hamstring | 18 Nov | 1 | Snow Time Lakers |
| Jaxson Hayes | UTAH | Out | Left Knee Strain | 18 Nov | 1 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 1 | Free agent |
| Isaiah Stewart | MEM | Day-To-Day | Illness | 18 Nov | 1 | Free agent |
| Isaiah Joe | DET | Out | Right Hip Bruise | 18 Nov | 1 | Free agent |
| Felix Okpara | WSH | Day-To-Day | Back Strain | 18 Nov | 1 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 1 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 18 Nov | 1 | Free agent |
| De'Andre Hunter | SAC | Day-To-Day | Left Hip Soreness | 18 Nov | 1 | Free agent |
| Bam Adebayo | MIA | Day-To-Day | Right Hip | 18 Nov | 1 | Lauri Birds |
| Austin Reaves | LAL | Out | Left Heel Bruise | 18 Nov | 1 | Cream Abdul-Yammar |
| Andrew Nembhard | IND | Day-To-Day | Left Hip Soreness | 18 Nov | 1 | Matt Wright's Foxies |
| Amen Thompson | HOU | Day-To-Day | Left Knee Soreness | 18 Nov | 1 | Matt Wright's Foxies |
| Scottie Barnes | TOR | Day-To-Day | Illness | 17 Nov | 0 | **us** |
| Julian Phillips | HOU | Day-To-Day | Right Wrist | 17 Nov | 0 | Free agent |
| Deni Avdija | POR | Day-To-Day | Foot | 17 Nov | 0 | Snow Time Lakers |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-17 21:18 UTC.
- [HEAVY, 16 Nov 2026](https://heavy.com/sports/nba/cleveland-cavaliers/evan-mobley-injury-update-cavaliers-return-timeline/)
- [Hoops Wire, 16 Nov 2026](https://hoopswire.com/cavs-evan-mobley-out-at-least-another-week-with-toe-injury/)
- [Akron Beacon Journal via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/cavaliers-jolt-injury-scare-ongoing-110547134.html)
- [CBS/RotoWire, 15 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/cavaliers-sam-merrill-missing-sixth-straight-game-monday/)
- [Fear the Sword via Yahoo, 8 Nov 2026](https://sports.yahoo.com/articles/cavs-level-concern-sam-merrill-003658864.html)
- [Cavaliers release, 20 Oct 2026](https://www.nba.com/cavaliers/news/releases-naeqwan-tomlin-261020)
- [Cavaliers On SI via Yahoo, 11 Nov 2026](https://sports.yahoo.com/articles/3-young-cavaliers-could-earn-192714593.html)
- [CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/cavaliers-peyton-watson-does-not-return-monday/)
- [TSN, 14 Nov 2026](https://www.tsn.ca/nba/article/cavaliers-without-starting-five-vs-mavericks-after-flight-delay-n1-50485303/)
- [SB Nation grades via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/player-grades-cavs-vs-bulls-023420546.html)
- [Bulls On SI, 13 Nov 2026](https://www.si.com/nba/bulls/onsi/bulls-injury-report-first-game-without-caleb-wilson-will-norman-powell-return-13)
- [Chicago Tribune via Yahoo, 13 Nov 2026](https://sports.yahoo.com/articles/chicago-bulls-matas-buzelis-step-210500659.html)
- [Bulls On SI, 13 Nov 2026](https://www.si.com/nba/bulls/onsi/what-caleb-wilson-s-injury-means-for-the-bulls-rotation-who-can-fill-the-void-12)
- [NBC Sports/Rotoworld, 13 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-13/bulls-start-giddey-powell-okoro-buzelis-smith)
- [Bulls On SI grades, 17 Nov 2026](https://www.si.com/nba/bulls/onsi/7-bulls-player-grades-giddey-doesn-t-close-vs-cavs-buzelis-takes-a-step-16)
- [CBS/RotoWire, 14 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bulls-isaac-okoro-stuffs-stat-sheet-friday/)
- [CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bulls-norman-powell-heads-to-locker-room/)
- [Milwaukee Journal Sentinel via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/milwaukee-bucks-ousmane-dieng-surgery-004603339.html)
- [NBC Sports/Rotoworld, 15 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ousmane-dieng-finger-to-undergo-surgery-monday)
- [NBC Sports/Rotoworld, 15 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ryan-rollins-illness-downgraded-to-out-sunday)
- [FOX Sports/AP preview, 17 Nov 2026](https://www.foxsports.com/articles/nba/milwaukee-takes-on-miami-on-10game-skid)
- [RotoWire, 16 Nov 2026](https://www.rotowire.com/basketball/headlines/gary-trent-news-strikes-for-18-off-bench-sunday-539360)
- [Behind the Buck Pass, 13 Nov 2026](https://behindthebuckpass.com/taylor-jenkins-finally-gary-trent-jr-chance-backfired)
- [Milwaukee Journal Sentinel via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/bucks-coach-taylor-jenkins-tinkers-035758327.html)
- [CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bucks-brayden-burries-solid-effort-in-sundays-loss/)
- [RotoWire, 9 Nov 2026](https://www.rotowire.com/basketball/headlines/brayden-burries-news-holding-down-starting-job-538340)
- [CBS/RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/bucks-kasparas-jakucionis-career-night-in-losing-effort/)
- [Bucks On SI via Yahoo, 16 Nov 2026](https://sports.yahoo.com/articles/lineup-shifting-bucks-start-fast-035646209.html)
- [Behind the Buck Pass, 15 Nov 2026](https://behindthebuckpass.com/bucks-risk-stunting-kasparas-jakucionis-growth-rapid-rotation-changes)
- [Warriors.com, 10 Nov](https://www.nba.com/warriors/news/brandon-williams-injury-update-20261110)
- [Yahoo Sports, 16 Nov](https://sports.yahoo.com/articles/steve-kerr-gives-injury-key-202942500.html)
- [AP via NBA.com, 11 Nov](https://www.nba.com/news/warriors-reserve-guard-brandon-williams-strains-left-hamstring-and-will-miss-at-least-a-week)
- [AP via NY1, 12 Nov](https://ny1.com/nyc/all-boroughs/ap-top-news/2026/11/12/warriors-star-stephen-curry-suffers-torn-oblique-muscle-and-will-be-sidelined-at-least-two-weeks)
- [CBS Sports/RotoWire player news, 11 Nov](https://www.cbssports.com/nba/players/28951880/dereck-lively-ii/)
- [Dallas Sports Journal, 30 Oct](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/)
- [Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)
- [Kings.com, 11 Oct](https://www.nba.com/kings/news/maxime-raynaud-medical-update)
- [CBS Sports/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-maxime-raynaud-wont-play-sunday/)
- [NBC Sports/Rotoworld, 12 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/maxime-raynaud-knee-progressing-no-timeline)
- [NBC Sports, 15 Nov lineup](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/sac-starts-acuff-monk-murray-cardwell-sabonis)
- [ClutchPoints, 15 Nov](https://clutchpoints.com/nba/los-angeles-clippers/clippers-brandon-ingram-injury-update-teases-return-coming-very-soon)
- [SI Jazz On SI, 17 Nov](https://www.si.com/nba/jazz/onsi/utah-jazz-vs-la-clippers-injury-report-who-s-trending-to-miss-game)
- [Yahoo Sports, 1 Oct](https://sports.yahoo.com/articles/ty-lue-reveals-clippers-still-100038552.html)
- [USA Today via Yahoo, 13 Nov](https://sports.yahoo.com/articles/clippers-bradley-beal-still-sidelined-071547162.html)
- [ClutchPoints, 14 Nov](https://clutchpoints.com/nba/san-antonio-spurs/spurs-news-tobias-harris-gets-crucial-injury-update-after-warriors-game)
- [Heavy, 15 Nov](https://heavy.com/sports/nba/san-antonio-spurs/tobias-harris-injury-update-return-timeline/)
- [Air Alamo, 20 Oct](https://airalamo.com/spurs-lineup-shakeup-creates-tobias-harris-sized-problem-they-cant-ignore)
- [NBC Sports/Rotoworld, 17 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-17/duncan-robinson-quad-out-at-least-a-week)
- [NBC Sports, 16 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/duncan-robinson-quad-ruled-out-tuesday-vs-sas)
- [BVM Sports, 17 Nov](https://bvmsports.com/2026/11/17/duncan-robinson-injury-pistons-star-out-at-least-one-week/)
- [IndyStar via Yahoo, 17 Nov](https://sports.yahoo.com/articles/rick-carlisle-no-definite-timeline-174500802.html)
- [CBS Sports/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-tyrese-haliburton-still-without-firm-timetable-for-return/)
- [CBS Sports/RotoWire, 17 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-javon-small-first-career-double-double/)
- [CBS Sports/RotoWire, 14 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-javon-small-productive-in-blowout-win/)
- [CBS Sports/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/grizzlies-ty-jerome-listed-out-for-monday/)
- [RotoWire, 16 Nov](https://www.rotowire.com/basketball/headlines/scotty-pippen-injury-still-viewed-as-week-to-week-539414)
- [Fox Sports/RotoWire, 10–11 Nov](https://www.foxsports.com/nba/jordan-goodwin-player)
- [Yahoo/Bright Side of the Sun, 16 Nov](https://sports.yahoo.com/articles/game-recap-furious-comeback-suns-004939671.html)
- [Covers box score, 15 Nov](https://www.covers.com/sport/basketball/nba/matchup/388723)
- [VAVEL, 16 Nov](https://www.vavel.com/en-us/nba/2026/11/16/1279471-nuggets-vs-suns-live-score-updates-and-play-by-play-nba.html)
- [BVM Sports, 11 Sep](https://bvmsports.com/2026/09/11/suns-mark-williams-likely-to-miss-five-months-after-shoulder-surgery/)
- [CBS Sports/RotoWire, 15 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-deandre-hunter-downgraded-to-out/)
- [Sactown Sports, 15 Nov](https://sactownsports.com/nba/sacramento-kings/okc-loss)
- [NBC Sports/Rotoworld, 15 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/deandre-hunter-hip-now-questionable-sunday)
