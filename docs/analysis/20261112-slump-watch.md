# Slump Watch: 12 Nov 2026

- Generated 2026-11-12 06:05 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 112 rostered players in league 423671879, through scoring period 23. Teams have played **2 to 13 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 23 (Wed 11 Nov US) re-scored from ESPN's final NBA box scores: all 69 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**7 rostered players are 10+ FP/g under projection, on 5 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 72.4/60.5 · LaMelo Ball 35.0/46.4 · Josh Giddey 28.7/46.2 |
| Matt Wright's Foxies | 2 | Shai Gilgeous-Alexander 46.2/56.8 · Cooper Flagg 55.2/45.4 · Evan Mobley 39.9/43.3 |
| Dr White Slong | 1 | Giannis Antetokounmpo 58.4/57.6 · Donovan Mitchell 41.8/46.5 · Joel Embiid 34.5/45.4 |
| Lauri Birds | 1 | Nikola Jokic 65.5/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Team Nic Kerr | 1 | Luka Doncic 67.3/60.6 · Domantas Sabonis 44.5/46.7 · Tyrese Maxey 46.0/45.1 |
| Come-in Cider (us) | 0 | Cade Cunningham 45.9/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.9/43.9 |
| Melbourne poopoo | 0 | Anthony Davis 49.0/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 48.4/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 42.3/50.0 · Jayson Tatum 46.3/48.1 · Kyrie Irving 40.6/44.2 |

## Since the last Slump Watch (9 Nov)

- **Joined (5 → 7 flagged):** Shai Gilgeous-Alexander (−10.7), Joel Embiid (−10.9), Darius Garland (−10.6).
- **Left:** Ivica Zubac, now −9.3 (near the line).
- **Gap moved by 3 or more:** none. Giddey moved −15.5 → −17.5, Harden −11.7 → −10.7, and Ball and Jackson Jr. are unchanged.

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 10 | 27.7 / 35.5 | 0.80 | 28.7 (10) | 29.0 (3) | 32.2 (6) | 28.7 (10) | 46.2 | **−17.5** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 11 | 27.8 / 32.9 | 0.89 | 35.0 (11) | 38.7 (3) | 37.4 (7) | 35.0 (11) | 46.4 | **−11.4** | 41.1 | Active |

- **Josh Giddey** (both): scoring −9.0, reb −4.6, ast −2.6, stocks −4.0, TO +1.2; bonus +1.6.
  - Current: 27.7 min, 10.2 pts, 3.9-9.3 FG, 1.4-2.0 FT, 4.6 reb, 8.3 ast, 0.5 stl, 0.3 blk, 3.2 TO
  - Last 7 days (3 GP): 28.7 min, 12.7 pts, 5.0-9.3 FG, 1.7-2.3 FT, 3.3 reb, 9.3 ast, 0.3 stl, 0.0 blk, 5.0 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
  - **News:** Splitter has taken the offence away from him: about 7 fewer minutes than last season, shot attempts down from 16.4 to 9.0 ([basketball.com.au, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)); 16.2% usage behind Caleb Wilson and Buzelis ([Yahoo, 31 Oct](https://sports.yahoo.com/articles/bulls-schedule-hardens-giddey-usage-173402853.html)). A preseason left-wrist injury is being managed; he is not on the report ([basketball.com.au, 9 Nov](https://www.basketball.com.au/news/aussies-in-nba-results-november-9-2026-josh-giddey)).
  - L7 29.0 (3) equals his season.
- **LaMelo Ball** (minutes): scoring −4.4, reb −2.3, ast −4.6, stocks +0.5, TO −1.4; bonus +0.8.
  - Current: 27.8 min, 18.3 pts, 6.4-14.2 FG, 2.2-2.7 FT, 3.3 reb, 6.0 ast, 1.7 stl, 0.1 blk, 4.0 TO
  - Last 7 days (3 GP): 32.0 min, 22.0 pts, 7.7-15.3 FG, 3.0-3.3 FT, 2.3 reb, 6.3 ast, 1.7 stl, 0.3 blk, 5.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
  - **News:** Minutes: foul trouble cut two October games to 17 and 20 minutes ([Sportsnaut, 26 Oct](https://sportsnaut.com/nba/chris-finchs-trust-in-lamelo-ball-faced-an-early-test)); 30–35 minutes in November with Anthony Edwards out after knee surgery ("sometime in December", [Bleacher Report, 29 Oct](https://bleacherreport.com/articles/25521213-anthony-edwards-knee-injury-recovery-timeline-detailed-wolves-connelly-new-video); *ESPN est.* 21 Dec).
  - L7 38.7 (3), 3.7 over his season.
- **Near the line:** Desmond Bane −9.9 (#8, efficiency, L7 26.7), Jakob Poeltl −5.5 (#13, minutes, L7 37.8), LeBron James −5.3 (#6, efficiency, L7 30.5).

### Matt Wright's Foxies: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Jaren Jackson Jr. | UTAH | #8 | 4 | 26.0 / 31.4 | 0.86 | 27.0 (4) → 32.3 (3) | — | — | 27.0 (4) → 32.3 (3) | 38.1 | **−11.1** | 35.9 | **Out**, ESPN est. back 14 Dec |
| Shai Gilgeous-Alexander | OKC | #1 | 12 | 32.8 / 33.8 | 0.84 | 46.2 (12) | 45.0 (5) | 45.4 (8) | 46.2 (12) | 56.8 | **−10.7** | 56.4 | Active |

- **Jaren Jackson Jr.** (minutes): scoring −5.4, reb −0.7, ast −0.2, stocks −5.1, TO −1.4; bonus +1.8.
  - Current: 26.0 min, 16.2 pts, 5.5-11.0 FG, 4.0-5.2 FT, 5.0 reb, 2.0 ast, 0.2 stl, 1.2 blk, 3.0 TO
  - Projected: 31.4 min, 21.9 pts, 7.8-16.7 FG, 4.3-5.4 FT, 5.7 reb, 2.1 ast, 1.2 stl, 1.6 blk, 2.3 TO
  - **News:** Torn right MCL on 26 Oct, no surgery, re-evaluated six weeks after, about 7–8 Dec ([KSL, 27 Oct](https://sports.ksl.com/nba/utah-jazz/jazz-injury-update-markkanen-jackson-jr/578523); [Yahoo, 27 Oct](https://sports.yahoo.com/articles/jazz-star-jaren-jackson-jr-200126696.html)). *ESPN est.* 14 Dec. Most of the gap is the game he left injured.
- **Shai Gilgeous-Alexander** (efficiency): scoring −4.6, reb −0.6, ast −3.8, stocks −2.7, TO +0.3; bonus +0.8.
  - Current: 32.8 min, 29.7 pts, 10.3-22.8 FG, 6.8-7.8 FT, 4.2 reb, 4.5 ast, 0.9 stl, 1.0 blk, 2.2 TO
  - Last 7 days (5 GP): 31.8 min, 31.4 pts, 10.0-22.0 FG, 9.2-10.6 FT, 4.2 reb, 5.2 ast, 0.4 stl, 0.8 blk, 2.8 TO
  - Projected: 33.8 min, 31.2 pts, 10.9-20.3 FG, 7.8-8.8 FT, 4.9 reb, 6.4 ast, 1.7 stl, 0.9 blk, 2.3 TO
  - **News:** Production, not minutes: he sat the fourth quarter of two blowout wins ([Yardbarker, 8 Nov](https://www.yardbarker.com/nba/articles/thunder_keep_finding_help_give_shai_gilgeous_alexander_another_early_finish/s1_17038_44531413)) and of the 10 Nov loss ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-sits-in-final-stanza/)); 31 in 36 min with 2 assists and 0-for-7 from three on 11 Nov ([Oklahoman via Yahoo, 12 Nov](https://sports.yahoo.com/articles/shai-gilgeous-alexander-okc-thunder-054238258.html)). No injury.
  - L7 45.0 (5), in line with his season.
- **Near the line:** Damian Lillard −7.4 (#6, efficiency, L7 31.0), Brandon Miller −6.9 (#9, minutes, L7 7.0).

### Dr White Slong: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Joel Embiid | PHI | #3 | 10 | 31.8 / 31.6 | 0.76 | 34.5 (10) | 30.0 (4) | 29.4 (7) | 34.5 (10) | 45.4 | **−10.9** | 46.4 | Day-to-day, ESPN est. back 12 Nov |

- **Joel Embiid** (efficiency): scoring −13.6, reb +1.1, ast −0.8, stocks −2.0, TO +0.0; bonus +4.5.
  - Current: 31.8 min, 17.7 pts, 5.4-14.6 FG, 6.5-7.3 FT, 9.3 reb, 3.8 ast, 0.7 stl, 0.7 blk, 3.0 TO
  - Last 7 days (4 GP): 29.5 min, 16.5 pts, 4.2-13.8 FG, 7.8-8.2 FT, 9.5 reb, 2.2 ast, 0.8 stl, 0.5 blk, 2.5 TO
  - Projected: 31.6 min, 27.4 pts, 9.1-18.5 FG, 7.9-9.2 FT, 8.2 reb, 4.2 ast, 0.7 stl, 1.2 blk, 3.0 TO
  - **News:** Questionable 12 Nov vs TOR, "right foot plantar fascia injury management" ([NBC Sports Philadelphia, 11 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-injury-report-lebron-james-joel-embiid-sixers-vs-raptors/766323/)); rolled an ankle on 10 Nov and finished ([Sixers Wire via Yahoo, 11 Nov](https://sports.yahoo.com/articles/joel-embiid-addresses-injury-shooting-174030268.html)). No timetable reported; *ESPN est.* 12 Nov. The gap is a shooting slump: 3-for-28 from three through six games ([PhillyVoice, 7 Nov](https://www.phillyvoice.com/sixers-news-76ers-analysis-joel-embiid-shooting-stats-tyrese-maxey-nick-nurse-nba-rumors-cle/)).
  - L7 30.0 (4), 4.5 under his season.
- **Near the line:** AJ Dybantsa −6.2 (#10, efficiency, L7 24.4), Derrick White −5.8 (#6, minutes, L7 38.0).

### Lauri Birds: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Darius Garland | LAC | #5 | 10 | 32.7 / 35.2 | 0.79 | 29.8 (10) | 36.0 (3) | 28.6 (7) | 29.8 (10) | 40.4 | **−10.6** | 35.3 | Active |

- **Darius Garland** (efficiency): scoring −1.7, reb −1.2, ast −1.0, stocks −3.6, TO −3.8; bonus +0.8.
  - Current: 32.7 min, 20.4 pts, 7.1-15.2 FG, 3.8-4.6 FT, 1.8 reb, 6.9 ast, 0.6 stl, 0.0 blk, 5.0 TO
  - Last 7 days (3 GP): 32.0 min, 21.0 pts, 7.0-12.3 FG, 4.3-5.3 FT, 2.0 reb, 7.7 ast, 0.3 stl, 0.0 blk, 4.0 TO
  - Projected: 35.2 min, 21.6 pts, 7.8-17.0 FG, 3.0-3.5 FT, 3.0 reb, 7.4 ast, 1.3 stl, 0.2 blk, 3.1 TO
  - **News:** No injury news; the gap is turnovers (5.0 a game against 3.1 projected) and defence; his true shooting fell from 60.2% to 56% ([On SI via Yahoo, 2 Nov](https://sports.yahoo.com/articles/clippers-darius-garland-problem-163001016.html)).
  - L7 36.0 (3) is 6.2 over his season: shooting, no role change: 26 on 10-14 in an overtime loss ([CBS, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-efficient-26-points-in-close-loss/)), 24 and 10 assists ([CBS, 9 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-big-double-double-in-sundays-win/)), 24 min in a 23-point loss ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-quiet-in-blowout-loss/)).
- **Near the line:** Ivica Zubac −9.3 (#7, minutes, L7 26.8), Kevin Durant −6.8 (#4, efficiency, L7 35.2).

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 12 | 32.6 / 33.6 | 0.77 | 31.3 (12) | 31.4 (5) | 31.4 (9) | 31.3 (12) | 42.1 | **−10.7** | 45.1 | Active |

- **James Harden** (efficiency): scoring −4.6, reb −0.4, ast −5.0, stocks −1.9, TO +1.0; bonus +0.2.
  - Current: 32.6 min, 16.7 pts, 4.8-12.2 FG, 4.5-5.3 FT, 4.6 reb, 5.6 ast, 0.8 stl, 0.5 blk, 2.9 TO
  - Last 7 days (5 GP): 31.4 min, 17.2 pts, 4.6-11.8 FG, 5.2-5.8 FT, 4.4 reb, 4.6 ast, 0.8 stl, 0.8 blk, 2.8 TO
  - Projected: 33.6 min, 20.6 pts, 6.1-14.3 FG, 5.6-6.4 FT, 5.0 reb, 8.1 ast, 1.2 stl, 0.6 blk, 3.4 TO
  - **News:** 15.3 points on 36.4% shooting before 11 Nov, a career low; normal minutes, no injury; then a season-high 32 (9-14, 5-7 from three) vs NY on 11 Nov ([AP via Yahoo, 12 Nov](https://sports.yahoo.com/articles/james-harden-scores-season-high-024929489.html)). Sixth-man talk is outside commentary ([SB Nation via Yahoo, 12 Nov](https://sports.yahoo.com/articles/diving-deeper-cavs-115-107-040256732.html)).
  - L7 31.4 (5) equals his season: no change found beyond one hot game.
- **Near the line:** Alex Sarr −9.4 (#7, efficiency, L7 27.8), Trae Young −7.8 (#4, efficiency, L7 30.0), Payton Pritchard −6.0 (#9, minutes, L7 26.2).

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Dejounte Murray −8.5 (#6, efficiency, L7 20.8), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.8 (#8, efficiency, L7 38.5).

### Melbourne poopoo: 0

No one flagged.

- **Near the line:** Stephon Castle −6.4 (#8, minutes, L7 27.8).

### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −7.7 (#1, minutes, L7 39.5).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball, Jaren Jackson Jr. |
| efficiency | Joel Embiid, James Harden, Shai Gilgeous-Alexander, Darius Garland |
| both | Josh Giddey |

- **Flagged and not active on ESPN:** Joel Embiid (Day-to-day, ESPN est. back 12 Nov), Jaren Jackson Jr. (**Out**, ESPN est. back 14 Dec).
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 13 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** Darius Garland (Lauri Birds, L7 36.0 in 3 vs projected 40.4, season gap −10.6), LaMelo Ball (Cream Abdul-Yammar, L7 38.7 in 3 vs projected 46.4, season gap −11.4).
- **Not flagged, but 10+ under projection over the last 7 days:** Dejounte Murray (Come-in Cider (us), L7 20.8 in 5 vs projected 39.0, L7 gap −18.2, season gap −8.5), Caleb Wilson (Come-in Cider (us), L7 17.7 in 3 vs projected 34.9, L7 gap −17.2, season gap −0.0), Brandon Miller (Matt Wright's Foxies, L7 7.0 in 2 vs projected 37.4, L7 gap −30.4, season gap −6.9), Domantas Sabonis (Team Nic Kerr, L7 29.7 in 3 vs projected 46.7, L7 gap −17.0, season gap −2.2), Trae Young (Team Nic Kerr, L7 30.0 in 5 vs projected 44.4, L7 gap −14.4, season gap −7.8), LeBron James (Cream Abdul-Yammar, L7 30.5 in 4 vs projected 42.5, L7 gap −12.0, season gap −5.3), Jarrett Allen (Dr White Slong, L7 25.0 in 3 vs projected 36.9, L7 gap −11.9, season gap −2.2), Desmond Bane (Cream Abdul-Yammar, L7 26.7 in 3 vs projected 38.2, L7 gap −11.6, season gap −9.9), Ty Jerome (Melbourne poopoo, L7 32.8 in 4 vs projected 43.5, L7 gap −10.8, season gap −2.5), Jalen Johnson (Snow Time Lakers, L7 39.5 in 2 vs projected 50.0, L7 gap −10.5, season gap −7.7).

### Notes

- **Dejounte Murray** (us): his minutes fell in three blowout losses, and he shot 1-6 and 2-6. No role change, injury or restriction reported ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/dejounte-murray-scores-5-points-in-27-minutes); [Yahoo, 11 Nov](https://sports.yahoo.com/articles/orleans-pelicans-dejounte-murray-problem-025055794.html)).
- **Caleb Wilson** (us): the window includes his 15-minute exit with a right hand injury on 11 Nov, and 22 min in a 30-point loss on 4 Nov ([ESPN, 11 Nov](https://www.espn.com/nba/story/_/id/50458612/bulls-rookie-caleb-wilson-leaves-game-right-hand-injury)). No timetable reported; *ESPN est.* 13 Nov.
- **Brandon Miller:** a 14-minute injury exit on 6 Nov, then out with a right hip strain. Small sample (2 games). No timetable reported; *ESPN est.* 15 Nov ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-out-again-thursday/)).
- **Domantas Sabonis:** mostly one 0-point game on 10 Nov, after a left knee issue ([CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-domantas-sabonis-fails-to-score-in-loss/)).
- **Trae Young** (WSH; traded to Washington in January): turnovers and shooting, 39.3% FG and 28.8% from three ([Wiz of Awes, 10 Nov](https://wizofawes.com/washington-wizards-trae-young-inability-make-shots-creating-problems)). No injury listing.
- **LeBron James** (PHI): shooting, 3-12 and 4-12 in two of four games. Questionable 12 Nov with sciatica; no timetable reported; *ESPN est.* 12 Nov ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/lebron-james-sciatica-questionable-thursday)).
- **Jarrett Allen** (CLE): a right knee contusion. He left 4 Nov early and returned on 9 Nov for 19 min ([CBS/RotoWire, 9 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jarrett-allen-cleared-to-play/)), then had 11 pts and 14 reb on 11 Nov ([Yahoo/AP, 12 Nov](https://sports.yahoo.com/articles/cavaliers-score-vs-knicks-james-044615777.html)).
- **Desmond Bane** (ORL): cold shooting (5-19 on 10 Nov; [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-endures-cold-shooting-in-win/)) and an illness absence, then 25 pts with 7 threes on 11 Nov ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/desmond-bane-with-25-points-with-7-3-pointers)).
- **Ty Jerome** (MEM): no injury or role change found. His scoring held (21–27 pts) but the rest of his line was thin ([NBC Sports, 9 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-09/ty-jerome-stays-hot-with-27-points-vs-raptors)).
- **Jalen Johnson** (ATL): 2 games right after returning from a left ankle sprain, a small sample ([Heavy, 8 Nov](https://heavy.com/sports/nba/atlanta-hawks/hawks-star-returns-from-ankle-injury-with-30-points-and-zero-rust/)).
- **Garland** and **Ball:** see their driver lines above.

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 9 | 32.8 / 32.5 | 31.0 | 38.5 (2) | 32.5 (6) | 31.0 (9) | 36.8 | 41.6 |
| Alex Sarr | Team Nic Kerr | 11 | 25.8 / 28.6 | 27.2 | 27.8 (5) | 27.0 (7) | 27.2 (11) | 36.6 | 39.4 |
| Jalen Johnson | Snow Time Lakers | 9 | 33.7 / 36.7 | 42.3 | 39.5 (2) | 35.2 (5) | 42.3 (9) | 50.0 | 53.1 |
| Ivica Zubac | Lauri Birds | 7 | 23.1 / 31.1 | 26.1 | 26.8 (4) | 26.8 (4) | 26.1 (7) → 29.5 (6) | 35.5 | 36.3 |

## Our pending trades

With **Snow Time Lakers**, proposed to us, expires 13 Nov 09:44 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Tyler Herro | we receive | 11 | 31.1 / 34.0 | 37.1 | 35.0 (4) | 34.1 (7) | 37.1 (11) | 38.8 | −1.7 | Active |
| Kyrie Irving | we receive | 9 | 30.6 / 34.6 | 40.6 | 38.5 (4) | 43.0 (6) | 40.6 (9) | 44.2 | −3.6 | Active |
| Cade Cunningham | we send | 10 | 33.3 / 34.8 | 45.9 | 42.3 (3) | 46.3 (7) | 45.9 (10) | 50.4 | −4.5 | Active |

With **Team Nic Kerr**, proposed by us, expires 13 Nov 08:07 UTC.

| Player | Side | GP | Min | Current | L7 | L15 | L30 | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| James Harden | we receive | 12 | 32.6 / 33.6 | 31.3 | 31.4 (5) | 31.4 (9) | 31.3 (12) | 42.1 | −10.7 | Active |
| Jrue Holiday | we send | 11 | 26.2 / 28.2 | 29.5 | 23.0 (5) | 29.4 (9) | 29.5 (11) | 28.1 | +1.4 | Active |
| Isaiah Hartenstein | we send | 12 | 25.0 / 25.0 | 31.5 | 34.2 (5) | 33.1 (8) | 31.5 (12) | 30.5 | +1.0 | Active |

### Notes

- **Holiday + Hartenstein for Harden (Team Nic Kerr):** dropping either player cancels the offer, and an accepted trade sits in a 48-hour review. The matchup plan (`20261112-matchup4.md`) holds both players until the answer.
  - By rate, Harden (32.3) is below Hartenstein (33.0) and Holiday (27.7). His projection is 42.1 and his 2026 average 45.1. He scored a season-high 32 on 11 Nov ([AP via Yahoo, 12 Nov](https://sports.yahoo.com/articles/james-harden-scores-season-high-024929489.html)).
- **Herro + Kyrie for Cade (Snow Time Lakers):** rates 35.5 and 40.8 against Cade's 45.3. A two-for-one would need a drop.
  - Herro played 11 Nov after a knee contusion ([NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tyler-herro-knee-scores-27-points-in-return)).
  - Kyrie's back-to-back calls are made on the day ([SI, 9 Nov](https://www.si.com/nba/mavericks/onsi/kyrie-irving-injury-status-second-night-back-against-indiana-pacers-dallas-mavericks-)).
- These are reports, not verdicts; a trade decision is the council's (`/council`).

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-12 06:05 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- [basketball.com.au, 6 Nov](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)
- [Yahoo, 31 Oct](https://sports.yahoo.com/articles/bulls-schedule-hardens-giddey-usage-173402853.html)
- [basketball.com.au, 9 Nov](https://www.basketball.com.au/news/aussies-in-nba-results-november-9-2026-josh-giddey)
- [Sportsnaut, 26 Oct](https://sportsnaut.com/nba/chris-finchs-trust-in-lamelo-ball-faced-an-early-test)
- [Bleacher Report, 29 Oct](https://bleacherreport.com/articles/25521213-anthony-edwards-knee-injury-recovery-timeline-detailed-wolves-connelly-new-video)
- [KSL, 27 Oct](https://sports.ksl.com/nba/utah-jazz/jazz-injury-update-markkanen-jackson-jr/578523)
- [Yahoo, 27 Oct](https://sports.yahoo.com/articles/jazz-star-jaren-jackson-jr-200126696.html)
- [Yardbarker, 8 Nov](https://www.yardbarker.com/nba/articles/thunder_keep_finding_help_give_shai_gilgeous_alexander_another_early_finish/s1_17038_44531413)
- [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-sits-in-final-stanza/)
- [Oklahoman via Yahoo, 12 Nov](https://sports.yahoo.com/articles/shai-gilgeous-alexander-okc-thunder-054238258.html)
- [NBC Sports Philadelphia, 11 Nov](https://www.nbcsportsphiladelphia.com/nba/philadelphia-76ers/sixers-injury-report-lebron-james-joel-embiid-sixers-vs-raptors/766323/)
- [Sixers Wire via Yahoo, 11 Nov](https://sports.yahoo.com/articles/joel-embiid-addresses-injury-shooting-174030268.html)
- [PhillyVoice, 7 Nov](https://www.phillyvoice.com/sixers-news-76ers-analysis-joel-embiid-shooting-stats-tyrese-maxey-nick-nurse-nba-rumors-cle/)
- [On SI via Yahoo, 2 Nov](https://sports.yahoo.com/articles/clippers-darius-garland-problem-163001016.html)
- [CBS, 5 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-efficient-26-points-in-close-loss/)
- [CBS, 9 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-big-double-double-in-sundays-win/)
- [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/clippers-darius-garland-quiet-in-blowout-loss/)
- [AP via Yahoo, 12 Nov](https://sports.yahoo.com/articles/james-harden-scores-season-high-024929489.html)
- [SB Nation via Yahoo, 12 Nov](https://sports.yahoo.com/articles/diving-deeper-cavs-115-107-040256732.html)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/dejounte-murray-scores-5-points-in-27-minutes)
- [Yahoo, 11 Nov](https://sports.yahoo.com/articles/orleans-pelicans-dejounte-murray-problem-025055794.html)
- [ESPN, 11 Nov](https://www.espn.com/nba/story/_/id/50458612/bulls-rookie-caleb-wilson-leaves-game-right-hand-injury)
- [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-brandon-miller-out-again-thursday/)
- [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/kings-domantas-sabonis-fails-to-score-in-loss/)
- [Wiz of Awes, 10 Nov](https://wizofawes.com/washington-wizards-trae-young-inability-make-shots-creating-problems)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/lebron-james-sciatica-questionable-thursday)
- [CBS/RotoWire, 9 Nov](https://www.cbssports.com/fantasy/basketball/news/cavaliers-jarrett-allen-cleared-to-play/)
- [Yahoo/AP, 12 Nov](https://sports.yahoo.com/articles/cavaliers-score-vs-knicks-james-044615777.html)
- [CBS, 11 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-endures-cold-shooting-in-win/)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/desmond-bane-with-25-points-with-7-3-pointers)
- [NBC Sports, 9 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-09/ty-jerome-stays-hot-with-27-points-vs-raptors)
- [Heavy, 8 Nov](https://heavy.com/sports/nba/atlanta-hawks/hawks-star-returns-from-ankle-injury-with-30-points-and-zero-rust/)
- [NBC Sports, 11 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-11/tyler-herro-knee-scores-27-points-in-return)
- [SI, 9 Nov](https://www.si.com/nba/mavericks/onsi/kyrie-irving-injury-status-second-night-back-against-indiana-pacers-dallas-mavericks-)
