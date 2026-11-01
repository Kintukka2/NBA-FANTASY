# Research briefing: For matchup 3 (Mon 2 to Sun 8 Nov, against Melbourne poopoo) we stream Fred VanVleet's slot. Which second player's slot should we also stream, dropping him: Desmond Bane, Yaxel Lendeborg, Anthony Black, Trey Murphy III, or none?

- Searched: 2026-11-01T04:00Z (searches and page fetches ran from about 03:50 to 04:45 UTC; the US Saturday 31 Oct slate was final)
- Players and teams covered: Fred VanVleet (HOU), Desmond Bane (ORL), Anthony Black (ORL), Yaxel Lendeborg (GS), Trey Murphy III (NO), Dejounte Murray (NO). Streamers: Collin Gillespie (PHX), Dillon Brooks (PHX), Daniel Gafford (DAL), Peyton Watson (CLE), Alex Caruso (OKC), Yves Missi (NO), Christian Braun (DEN). Context: Paolo Banchero, Jalen Suggs (ORL); Jordan Poole, Herb Jones, Jeremiah Fears (NO); Marcus Smart, Reed Sheppard (HOU); Dereck Lively II (DAL).
- **Budget:** 22 web searches. Team game notes (nba.com/gamenotes PDFs) and RotoWire/CBS team pages were opened directly, without searching.
- **ESPN est.** dates come from the repo's `docs/analysis/20261101-injury-watch.md` (ESPN feed read 1 Nov 2026). The researcher has no shell and did not run `council/injuries.py`.
- **Recent form (L7/L15/L30):** see `docs/research/20261101-0400-second-stream-slot-form.md` (generated 03:46 UTC by `council/form.py`). This briefing computes no FP figures. Shooting splits marked "researcher's arithmetic" are sums of the game lines quoted.

## Matchup-week schedules (2 to 8 Nov), as read

| Team | Games, 2 to 8 Nov | Source |
|---|---|---|
| HOU | 3: Mon 2 v BOS, Wed 4 v MIN, Sat 7 at PHX. No back-to-back. | https://www.cbssports.com/nba/teams/HOU/houston-rockets/schedule/ (fetched 1 Nov 2026) |
| ORL | 3: Mon 2 v WSH, Thu 5 at PHX, Sat 7 at GS. Sun 1 Nov v BOS falls in matchup 2. | https://www.cbssports.com/nba/teams/ORL/orlando-magic/schedule/ (fetched 1 Nov); Magic game notes, 1 Nov, https://www.nba.com/gamenotes/magic.pdf |
| NO | 4: Mon 2 at MEM, Wed 4 v UTA, Fri 6 v MIN, Sun 8 at LAC | https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/schedule/ (fetched 1 Nov); Pelicans game notes, 31 Oct, https://www.nba.com/gamenotes/pelicans.pdf |
| GS | 3: Mon 2 v PHX, Thu 5 v MIA, Sat 7 v ORL. Sun 1 and Mon 2 Nov are a back-to-back. | https://www.cbssports.com/nba/teams/GS/golden-state-warriors/schedule/ (fetched 1 Nov) |
| PHX | 4: Mon 2 at GS, Wed 4 v POR, Thu 5 v ORL, Sat 7 v HOU (4 and 5 Nov are a back-to-back) | Suns game notes, 30 Oct, https://www.nba.com/gamenotes/suns.pdf |
| DEN | 3: Mon 2 v POR, Wed 4 v TOR, Sat 7 at IND | Nuggets game notes, 30 Oct, https://www.nba.com/gamenotes/nuggets.pdf |
| DAL | 4: Mon 2 v SAC, Wed 4 at SAS, Fri 6 v UTA, Sun 8 v BKN | Mavericks game notes, 30 Oct, https://www.nba.com/gamenotes/mavericks.pdf |
| CLE | Mon 2 v OKC, Wed 4 at OKC. The rest of the week was not legible in the PDF. | Cavaliers game notes, 31 Oct, https://www.nba.com/gamenotes/cavaliers.pdf |

## Findings

### Fred VanVleet (HOU, our roster)
- **Status:** **Out Sat 31 Oct v OKC**, listed as "right knee injury management." It was the second night of a back-to-back: he played Fri 30 Oct at Dallas. RotoWire calls it a "standard maintenance day" and says he "should return for Monday's meeting with the Celtics." ESPN est. 2 Nov. CBS: "out until at least Nov 2" (updated 31 Oct).
  - Sources:
    - https://www.rotowire.com/basketball/headlines/fred-vanvleet-injury-ruled-out-for-saturday-536969 (31 Oct 2026)
    - https://sports.yahoo.com/articles/rockets-vs-thunder-injury-report-221521504.html (Laci Watson, Roundtable via Yahoo, 31 Oct 2026 22:15 UTC): "Newly listed after playing last night."
    - https://www.cbssports.com/nba/injuries/ (fetched 1 Nov 2026)
  - Rotoworld: managing the knee "likely won't be the last time he does so this season." Source: https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/fred-vanvleet-knee-out-saturday-vs-thunder (Nick Shlain, 31 Oct 2026)
- **Same knee as October: yes.**
  - **Sat 24 Oct at ATL:** ruled out, second leg of a back-to-back, also listed as "right knee injury management." He was expected back for Monday's rematch with Atlanta, and he played on 26 Oct. Source: https://www.rotowire.com/basketball/headlines/fred-vanvleet-injury-officially-ruled-out-saturday-535849 (24 Oct 2026)
  - **The underlying injury:** a torn right ACL in an offseason workout or minicamp in the Bahamas. He was expected to miss 2025-26. Source: https://nba.com/news/rockets-fred-vanvleet-tears-acl (22 Sep 2025; older than 14 days)
  - **Pattern:** both 2026-27 absences (24 Oct, 31 Oct) fell on the second night of a back-to-back. No diagnosis of any new injury was found. Houston has **no back-to-back from 2 to 8 Nov** (schedule above).
  - Preseason reporting, already in the repo: no minutes restriction, but managed on back-to-backs. Source: `docs/research/20261019-0745-preseason-west.md`, citing RotoWire HOU (18 Oct 2026).
- **Recent games:**
  - 26 Oct v ATL: 29 min, 5 pts (2-7 FG), 4 reb, 5 ast. Source: `docs/research/20261030-0600-trade-offers.md` (RotoWire, 26 Oct)
  - 28 Oct v MIL: 29 min, 24 pts (7-14 FG, 4-9 3P, 6-6 FT), 6 reb, 5 ast, 2 stl. Source: https://www.rotowire.com/basketball/news.php?team=HOU (fetched 1 Nov 2026; item dated 28 Oct)
  - 30 Oct at DAL (L 111-116): 16 pts on 6-17 FG, 6 ast, 5 reb; minutes not shown. Source: Rotoworld related items, NBC page above (31 Oct 2026)
- **Who started in his place, 31 Oct:** Marcus Smart, Amen Thompson, Kevin Durant, Jabari Smith Jr., Alperen Şengün. Reed Sheppard (low back soreness) was also out; ESPN est. 2 Nov. Houston won 119-98.
  - Sources: https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-31/hou-starts-smart-thompson-durant-smith-sengun (31 Oct 2026); Yahoo/Roundtable (31 Oct, above); CBS HOU schedule (above)

### Desmond Bane (ORL, our roster)
- **Status:** healthy. No injury item in 2026-27. Source: https://www.rotowire.com/basketball/player/desmond-bane-5159 (fetched 1 Nov 2026)
- **Game lines** (same RotoWire page; game dates from the Magic's notes):

  | Date | Result | Min | Line |
  |---|---|---|---|
  | 21 Oct v ATL | L 125-132 | 33 | 18 pts, 5-15 FG, 3-10 3P, 5-7 FT, 5 reb, 2 ast, 3 stl |
  | 23 Oct v MIN | L 93-115 | 27 (fouled out) | 5 pts, 2-11 FG, 1-9 3P, 2 reb, 1 stl |
  | 25 Oct at NYK | W 111-102 | 35 | 22 pts, 6-13 FG, 4-9 3P, 6-8 FT, 6 reb, 2 ast, 2 blk |
  | 28 Oct at TOR | L 99-129 | 34 | 13 pts, 3-14 FG, 2-8 3P, 5-5 FT, 5 reb, 4 ast, 2 blk, 1 stl |
  | 30 Oct at TOR | W 121-114 | 39 | 28 pts, 8-18 FG, 6-12 3P, 6-6 FT, 2 reb, 6 ast, 1 blk |

  - The 30 Oct game was his season high. AP: he made his first four threes. Source: https://www.cbssports.com/nba/gametracker/recap/NBA_20261030_ORL@TOR/ (AP, 30 Oct 2026)
- **What changed (researcher's arithmetic from the lines above):**
  - **Shot volume is steady:** 11 to 18 FGA and 8 to 12 3PA in every game.
  - **The change is accuracy:**
    - First two games: 7-26 FG and 4-19 3P.
    - Last three games: 17-45 FG and 12-29 3P.
    - The 23 Oct game was a 27-minute foul-out.
  - **Minutes:** 35, 34 and 39 in the last three games, all after Banchero's injury. That compares with 33 and 27 before it.
- **Context, Banchero and Suggs:**
  - "Through two games, Bane averaged 11.5 points on 26.9% shooting and 21.1% from three." A Roundtable host says Bane and Franz Wagner must step up with Banchero out; no usage figures are given. Source: https://sports.yahoo.com/articles/two-players-must-step-paolo-160042726.html (Don Strouble, Roundtable via Yahoo, 26 Oct 2026 16:00 UTC)
  - Orlando Magic On SI grades him B-: "started 4-for-19 from three after two games." Orlando "will need him to be a reliable spark in Suggs and Banchero's absence." Source: https://sports.yahoo.com/articles/grading-every-orlando-magic-player-222407119.html (Matt Hanifan, Magic On SI via Yahoo, 31 Oct 2026 22:24 UTC)
  - Magic notes for 1 Nov: Bane is a probable starter. Season line 17.2 pts, 4.0 reb, 2.8 ast, 1.00 blk. Source: https://www.nba.com/gamenotes/magic.pdf (game notes for Sun 1 Nov 2026 v BOS)
  - **No usage rate, touches figure or coach quote on Bane's role was found.**
- **Paolo Banchero** (ORL):
  - Injury: low-grade right high ankle sprain on Fri 23 Oct v Minnesota. The team announced it on 24 Oct.
  - Timeline: "typically carries a four-to-six-week timetable" (Charania). ESPN est. 22 Nov. CBS: out until at least 22 Nov.
  - Before the injury he averaged 24.5 pts, 7.5 ast and 6.5 reb.
  - Sources: https://www.tsn.ca/nba/article/report-magics-banchero-out-multiple-weeks-with-low-grade-high-ankle-sprain-n1-50266620/ (ESPN/AP via TSN, 24 Oct 2026 12:53 EDT); CBS injuries (fetched 1 Nov)
- **Jalen Suggs** (ORL):
  - Injury: right knee injury on 25 Oct at New York; "mild bone bruise," to be re-evaluated in two weeks (Charania). That puts the re-evaluation about 9 Nov.
  - ESPN est. 10 Nov. CBS: out until at least 10 Nov.
  - Sources: https://www.rotowire.com/basketball/news.php?team=ORL (fetched 1 Nov; items dated 25 to 26 Oct); CBS injuries (fetched 1 Nov)

### Anthony Black (ORL, our roster)
- **Status:** active.
  - He sprained his right ankle in preseason, missed all of preseason and the first two games, and debuted 25 Oct.
  - He missed shootaround on 28 Oct for a personal matter, was listed questionable, then played.
  - Sources:
    - https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-28/orl-starts-richardson-bane-black-wagner-carter (Raphielle Johnson, Rotoworld, 28 Oct 2026, with related items dated 18 to 30 Oct)
    - RotoWire ORL (fetched 1 Nov)
- **Role and minutes (last 7 days):**
  - **25 Oct at NYK:** off the bench. 26 min, 18 pts, 5 3PM, 5 ast. Fouled out.
  - **28 Oct at TOR:** first start of the season, in Suggs' place. 22 min, 8 pts. The projected five was Jase Richardson, Bane, Black, Wagner, Wendell Carter Jr.
  - **30 Oct at TOR:** 31 min, 17 pts, 10 ast, 6 reb. He hit a three with 6:56 left that started a 13-4 run.
  - **Was 30 Oct a start?** No opened source states it outright.
  - **1 Nov v BOS:** the Magic's notes list him as a probable starter, at forward, beside Richardson and Bane at guard. Season line: 14.3 pts, 5.3 ast, 3.7 reb, 1.00 stl.
  - Sources: RotoWire ORL (items 26, 28, 31 Oct); Rotoworld (28 Oct, above); AP recap via CBS (30 Oct, above); https://www.nba.com/gamenotes/magic.pdf (1 Nov 2026)
- **Shooting:** 53.1% FG and 57.1% 3P (8-14) over three games. Magic On SI grades him A-. Source: Hanifan, Magic On SI via Yahoo (31 Oct 2026, above)
- **Who takes minutes when Suggs and Banchero return:**
  - Rotoworld (28 Oct): Black "expected to start at point guard for the foreseeable future." If Black is out, Richardson gains minutes and Franz Wagner could handle point guard duties. Rotoworld's 30 Oct note: worth holding in redraft "until Suggs returns." Both are analysis, not team statements. Source: Rotoworld (above)
  - **No coach or team statement on the rotation after Suggs returns was found.**
  - Both return windows fall after 8 Nov: Suggs ESPN est. 10 Nov (re-evaluation about 9 Nov); Banchero ESPN est. 22 Nov.

### Yaxel Lendeborg (GS, our roster)
- **Status:** active.
  - He was listed questionable (foot) for 28 Oct, took part in shootaround, was cleared, and played. Source: https://www.rotowire.com/basketball/news.php?team=GSW (fetched 1 Nov 2026; items dated 27 to 28 Oct)
  - **No foot item after 28 Oct was found.**
- **Role (last 7 days):**
  - **Started 30 Oct v LAL** (W 112-95). The starters were Gui Santos, Lendeborg, Draymond Green, Brandin Podziemski and Stephen Curry; that lineup is 2-0.
  - Golden State has used five different starting lineups this season.
  - Line on 30 Oct: **6 pts, 1 reb, 0 ast, 1 3PM**. Season line: 19.8 pts, 7.8 reb, 3.3 ast.
  - Source: Warriors game notes for Sun 1 Nov v LAC, https://www.nba.com/gamenotes/warriors.pdf (1 Nov 2026)
  - **28 Oct at MIN (W 119-114):** 35 min, 26 pts (11-20 FG, 2-5 3P, 2-4 FT), 9 reb, 1 ast, 1 stl, 1 blk. Georges Niang started that game, with Santos out (left knee tendinitis). Source: RotoWire GSW (above)
  - **26 Oct at DEN:** a CBS headline reads "Erupts for 31-point night." The line itself was not opened. Source: https://www.cbssports.com/fantasy/basketball/news/warriors-yaxel-lendeborg-confirmed-as-starter/ ("More News" list, fetched 1 Nov 2026)
- **Workload, through five games:**
  - He leads Golden State in minutes (33.6 mpg), made shots and attempted shots.
  - He is second in points (22.6 ppg) and leads the team in turnovers (18, about 3.6 per game).
  - Kerr after the Minnesota win: "He tried to force a bunch of plays tonight; it's his fifth game in the NBA." Kerr also says he "needs to learn the value of just making the simple play."
  - Source: https://sfstandard.com/2026/10/29/yaxel-lendeborg-warriors-rookie-golden-state-future/ (Tim Kawakami, SF Standard, 29 Oct 2026 16:05)
  - Kerr on 95.7 The Game: he does not want Lendeborg to change his approach, and he needs to avoid reach-in fouls. Source: https://www.nbcsportsbayarea.com/nba/golden-state-warriors/steve-kerr-yaxel-lendeborg-luka-doncic/1975661/ (Dylan Grausz, 30 Oct 2026)
- **Teammate status:**
  - Curry and Green: ruled out to rest Sun 1 Nov v LAC (Green listed back/rest). That game is the front end of a back-to-back.
  - Gui Santos (knee): probable for 1 Nov. ESPN est. 1 Nov.
  - Kristaps Porziņģis (personal/illness): away from the team indefinitely, and Golden State is "exploring" trades (Slater, 28 Oct). ESPN est. 1 Dec.
  - Jimmy Butler (right ACL): ESPN est. 2 Jan; CBS at least 2 Jan.
  - Moses Moody (left patellar tendon): ESPN est. 1 Dec; CBS at least 1 Dec.
  - Sources: RotoWire GSW (fetched 1 Nov); CBS injuries (fetched 1 Nov); Warriors game notes (1 Nov)

### Trey Murphy III (NO, our roster)
- **Status:** healthy. No 2026-27 injury designation. Source: https://www.rotowire.com/basketball/player/trey-murphy-5401 (fetched 1 Nov 2026)
- **Role:** started all five games through 29 Oct (5 GP, 5 GS), averaging 14.2 pts, 4.4 reb, 2.8 ast, 1.0 stl in 32.4 mpg. Source: Pelicans game notes for 31 Oct v ATL, https://www.nba.com/gamenotes/pelicans.pdf
- **Last 7 days:**
  - **28 Oct v DEN:** 30 min, 6 pts (2-7 FG, 2-7 3P).
  - **29 Oct v SAC:** 32 min, 19 pts (6-12 FG, 2-7 3P, 5-8 FT), 5 reb, 3 ast, 1 stl.
  - **31 Oct v ATL (W 121-99):** started, 15 pts. Minutes not found.
    - Mosley changed the lineup: Matković, Herb Jones, Williamson, Murphy, Fears. Saddiq Bey scored 25 off the bench.
    - Source: https://www.cbssports.com/nba/gametracker/recap/NBA_20261031_ATL@NO/ (AP, 31 Oct 2026)
  - Earlier games: 21 Oct, 32 min, 11 pts; 23 Oct at UTA, 9 pts, 6 reb, 3 ast (Rotoworld recap, undated, minutes not shown); 24 Oct at DEN, 37 min, 26 pts.
  - Sources: RotoWire player page (above); https://www.nbcsports.com/nba/trey-murphy-iii/11154/news (fetched 1 Nov 2026)
- **Usage, already in the repo:** 14.6% through two games, against 22.9% in 2025-26. He was in Mosley's 28 Oct closing five. Source: `docs/research/20261030-0600-trade-offers.md` (Pelicans On SI, 24 and 29 Oct). **No newer usage figure was found.**
- **Effect of Murray and Poole returning:**
  - RotoWire (30 Oct): Murray's return was expected to move **Herb Jones**, not Murphy, out of the starting five.
  - Poole is a bench guard. RotoWire (30 Oct) expected him back Mon 2 Nov at Memphis.
  - Sources: https://www.cbssports.com/nba/teams/NO/new-orleans-pelicans/ (RotoWire items dated 29 to 31 Oct, fetched 1 Nov 2026); https://www.cbssports.com/fantasy/basketball/news/pelicans-dejounte-murray-absent-from-injury-report/ (RotoWire via CBS, 30 Oct 2026 5:19 pm ET)
  - **No coach statement on Murphy's role once both return was found.**

### Dejounte Murray (NO, our roster)
- **Status:** out 29 Oct and 31 Oct for the birth of his son. ESPN est. 2 Nov. CBS: "out until at least Nov 2" (updated 31 Oct).
  - **29 Oct v SAC:** late scratch. Mosley attributed it to the birth.
  - **30 Oct:** RotoWire said he was off the injury report for Saturday and would resume starting at point guard.
  - **31 Oct v ATL:** ruled out anyway, his "second straight absence" for the birth.
  - Sources:
    - https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-29/herb-jones-starting-in-place-of-dejounte-murray (Rotoworld related items, 29 to 31 Oct 2026)
    - CBS NO team page (above)
    - CBS injuries (fetched 1 Nov)
- **Expected back Monday at Memphis?** **No report was found that confirms it.** The only Monday return report found is for Jordan Poole.
- **Jordan Poole:** sprained left ankle on 28 Oct v DEN, out 29 and 31 Oct, "expected to return Monday at Memphis" (RotoWire, 30 Oct). ESPN est. 2 Nov. Source: CBS NO team page (above)

### Streamers named by the matchup script

**Collin Gillespie (PHX)**
- **Status:** healthy; no injury item.
- **Role:** bench. He is not in Phoenix's starting five, which was Dillon Brooks, Miles Bridges, Khaman Maluach, Jalen Green and Devin Booker (3 GS each through 26 Oct). Source: Suns game notes, 30 Oct, https://www.nba.com/gamenotes/suns.pdf
- **30 Oct v DEN (L 120-127):** 33 min, 16 pts, 3 reb, 10 ast, 4 stl, 1 blk. Arizona Sports calls him "the star" of the second unit.
  - Sources:
    - https://arizonasports.com/nba/phoenix-suns/suns-building-block-nuggets-loss (Kellan Olson, 30 Oct 2026 23:31, updated 31 Oct 14:10)
    - https://www.rotowire.com/basketball/news.php?team=PHX (fetched 1 Nov; item dated 31 Oct)
- Phoenix injuries: Oso Ighodaro questionable (right oblique strain), no ESPN est. found in the repo; Mark Williams out (left shoulder surgery), ESPN est. 3 Feb. Source: Suns game notes (30 Oct)

**Dillon Brooks (PHX)**
- **Role:** starter, 3 GS, 31.0 mpg through 26 Oct. Source: Suns game notes (30 Oct)
- **Ejected 30 Oct v DEN:** Flagrant 2, with 8:05 left in the third quarter. He kicked Jamal Murray low on a turnaround. At that point he had a season-high 22 pts on 9-12 FG in 21 min.
  - Murray: he didn't think Brooks was "really trying to kick me."
  - **As of Saturday morning (31 Oct), no fine or suspension had been announced**; the play is under league review.
  - Sources:
    - https://sports.yahoo.com/articles/dillon-brooks-faces-nba-scrutiny-171500542.html (Eman Zahra, Lindy's Sports via Yahoo, 31 Oct 2026 17:15 UTC)
    - Arizona Sports (above)
    - RotoWire PHX (item dated 30 Oct)
- 27 Oct at OKC: 33 min, 19 pts, 5 reb, 5 ast, 3 stl, 1 blk. Source: RotoWire PHX

**Daniel Gafford (DAL)**
- **Role:** starting centre. 5 GP and 5 GS through 28 Oct: 6.6 pts, 7.0 reb, 2.0 blk, 22.3 mpg. Source: Mavericks game notes, 30 Oct, https://www.nba.com/gamenotes/mavericks.pdf
- **Recent games:**
  - 28 Oct v OKC: 27 min, 7 pts, 11 reb, 2 ast, 2 blk.
  - 30 Oct v HOU (W 116-111): 29 min, 18 pts (6-7 FG, 6-9 FT), 7 reb, 2 ast, 2 blk. Whether he started is not stated.
  - Source: https://www.rotowire.com/basketball/news.php?team=DAL (fetched 1 Nov 2026)
- **Dereck Lively II:** not cleared for camp as of 23 Sep. CBS now lists him as a **game-time decision** (foot, updated 31 Oct). ESPN est. 2 Nov. **No report of his season debut was found.**
  - Sources: https://www.tsn.ca/nba/article/report-mavs-lively-ii-foot-not-cleared-for-camp-n1-50016983/ (Tim MacMahon, 23 Sep 2026; older than 14 days); CBS injuries (fetched 1 Nov)

**Peyton Watson (CLE)**
- **Status:** not on CBS's Cleveland injury list (fetched 1 Nov).
- **Role:** starting small forward. 5 GP and 5 GS: 12.0 pts, 4.4 reb, 2.4 ast, 1.2 stl, 1.8 blk, 29.8 mpg. The last starting five was Harden, Mitchell, Watson, Mobley, Allen. Source: Cavaliers game notes for 31 Oct at MIL, https://www.nba.com/gamenotes/cavaliers.pdf
- **Recent games** (RotoWire CLE, fetched 1 Nov 2026):
  - 26 Oct v MIN (OT): 37 min, 15 pts, 8 reb, 4 blk, 3 stl.
  - 28 Oct v WSH: 28 min, 22 pts (9-17 FG), 6 reb.
  - His 31 Oct line was not found.
- Cleveland injuries:
  - Jaylon Tyson (ankle): out 31 Oct. ESPN est. 2 Nov.
  - Meleek Thomas (foot): available 31 Oct.

**Alex Caruso (OKC)**
- **Status:** **out**, right ankle sprain. ESPN est. 4 Nov. CBS: out until at least 4 Nov (updated 28 Oct).
  - Hurt in the second quarter on 26 Oct v PHX (9 pts in 9 min). Daigneault: a sprain and "nothing else" (via ESPN, per search summary; that page was not opened).
  - USA Today's Clemente Almanza (28 Oct): "expected to miss time." He was out again on 31 Oct at HOU.
  - Sources: https://www.rotowire.com/basketball/news.php?team=OKC (fetched 1 Nov; items dated 26 to 28 Oct); Yahoo/Roundtable (31 Oct, above); CBS injuries (fetched 1 Nov)
- **Thunder backcourt and frontcourt absences:**
  - Jalen Williams: dislocated left ankle and fractured fibula, surgery 28 Oct. ESPN est. 2 Mar.
  - Cason Wallace: left shoulder labrum surgery 30 Oct. ESPN est. 2 Mar.
  - Chet Holmgren: small patellar tendon tear, "at least 8-10 weeks" (Slam, 30 Oct). ESPN est. 2 Jan.
  - Source: RotoWire OKC (above)

**Yves Missi (NO)**
- **Status:** **out**, left knee bone bruise. ESPN est. 8 Nov. CBS: out until at least 8 Nov (updated 30 Oct).
  - Hurt 23 Oct at Utah when Zion Williamson fell into his leg. He was carried off.
  - RotoWire (30 Oct): "week-to-week."
  - Sources: https://www.tsn.ca/nba/article/pelicans-missi-injures-left-knee-against-jazz/ (Matthew Coles, AP via TSN, 23 Oct 2026 23:16 EDT); CBS NO team page (RotoWire item dated 30 Oct); CBS injuries
- **Who plays centre:** DeAndre Jordan started the two games after the injury. Karlo Matković has started since 29 Oct, including 31 Oct. Sources: CBS NO team page; AP recap (31 Oct, above)

**Christian Braun (DEN)**
- **Status:** healthy; no injury item.
- **Role:** starter. 4 GP and 4 GS through 28 Oct: 11.5 pts, 4.5 reb, 2.3 ast, 2.3 stl, 35.8 mpg. The starting five was Trevon Brazile, Aaron Gordon, Nikola Jokić, Braun, Jamal Murray. Source: Nuggets game notes, 30 Oct, https://www.nba.com/gamenotes/nuggets.pdf
- **Recent games:**
  - 28 Oct at NO: 36 min, 15 pts, 3 stl, 1 blk.
  - **30 Oct at PHX: 37 min, 31 pts** (11-16 FG, 7-9 3P), 3 stl. That includes 6-6 from three in the first half.
  - Sources: https://www.rotowire.com/basketball/news.php?team=DEN (fetched 1 Nov 2026); https://www.cbssports.com/nba/gametracker/recap/NBA_20261030_DEN@PHO/ (AP, 31 Oct 2026)
- Denver injuries: Julian Strawther (left knee sprain), ESPN est. 29 Nov.

## Conflicts with the repo

- **`data/processed/players_scored.csv` Injury column against the web, 1 Nov:**

  | Player | CSV | Web, 1 Nov |
  |---|---|---|
  | Paolo Banchero | `ACTIVE` | Out (high ankle sprain, 4 to 6 weeks from 23 Oct; ESPN est. 22 Nov) |
  | Dejounte Murray | `ACTIVE` | Out (personal; ESPN est. 2 Nov) |
  | Yves Missi | `ACTIVE` | Out (left knee bone bruise; ESPN est. 8 Nov) |
  | Anthony Black | `DAY_TO_DAY` | Active, three games played, probable starter on 1 Nov |
  | Peyton Watson | `DAY_TO_DAY` | 5/5 starts; not on CBS's injury list |
  | Yaxel Lendeborg | `DAY_TO_DAY` | Foot questionable 27 Oct, played 28 and 30 Oct |
  | Alex Caruso | `DAY_TO_DAY` | Out (ankle sprain; ESPN est. 4 Nov) |
  | Jalen Suggs | `DAY_TO_DAY` | Out (bone bruise, re-evaluation about 9 Nov; ESPN est. 10 Nov) |
  | Fred VanVleet | `DAY_TO_DAY` | Out 31 Oct for scheduled knee management only; expected back 2 Nov |

  The repo's 1 Nov form file and injury watch match the web on all of these.
- **`docs/offseason-impact.md`:**
  - **Golden State preseason five** "Curry – Podziemski – Lendeborg – Green – Horford." The 30 Oct starters were Santos, Lendeborg, Green, Podziemski and Curry. Al Horford came off the bench. Source: Warriors game notes (1 Nov)
  - **"Anthony Black's preseason status unresolved."** Now resolved: right ankle sprain, debuted 25 Oct, started 28 Oct. Source: Rotoworld (28 Oct)
  - **Gillespie, "Bridges in, Green starting."** Consistent with the web: Gillespie comes off the bench and played 33 min on 30 Oct. Note the repo writes "Bridges"; the Phoenix player is **Miles** Bridges. Source: Suns game notes (30 Oct)
  - **Gafford "functional opening-night starter with Lively out."** Consistent: 5/5 starts through 28 Oct. New detail: Lively is now a game-time decision (CBS, 31 Oct).
  - **"Missi is the one clear buy."** New detail: out since 23 Oct with a left knee bone bruise (ESPN est. 8 Nov).
  - **Houston five with VanVleet.** Consistent. New detail: he has sat both second nights of back-to-backs so far (24 and 31 Oct).
- **The question's premise that Dejounte Murray and Jordan Poole "return."** Only Poole has a reported Monday return (RotoWire, 30 Oct). Murray's 31 Oct absence followed a report that he was off the injury report. No Monday report for him was found.

## Could not confirm

- **Murray's availability for Mon 2 Nov at Memphis.** No report after his 31 Oct scratch was found.
- **Minutes:**
  - Murphy on 31 Oct and 23 Oct.
  - Lendeborg on 30 Oct. A search summary credited him with 24:14 and a late foul-out, citing an SF Chronicle box score that did not load; CBS's box score was cut off.
  - VanVleet on 30 Oct.
  - Watson's 31 Oct line.
- **Whether Black started on 30 Oct.** Only the projection for 1 Nov and Rotoworld's "foreseeable future" note were found.
- **Any Sweeney quote** on the guard rotation once Suggs returns, or on Bane's role.
- **Bane's and Murphy's usage rates** newer than 24 Oct.
- **Brooks: a league fine or suspension** for the 30 Oct Flagrant 2 had not been announced as of 31 Oct.
- **Lively's 2026-27 debut** and whether it would affect Gafford's minutes.
- **Daigneault's "nothing else" quote on Caruso.** It came from a search summary; the ESPN page was not opened.
- **The NBA's official 1 Nov injury report.** The PDF (12:00 a.m. ET) timed out twice.
- **Trade, extension or suspension news in the last 14 days** for Bane, Black, Lendeborg, Murphy or VanVleet. None was found. The only related item is Golden State "exploring" a Porziņģis trade (Slater via RotoWire, 28 Oct).
