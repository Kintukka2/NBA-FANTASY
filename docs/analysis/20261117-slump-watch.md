# Slump Watch: 17 Nov 2026

- Generated 2026-11-17 21:18 UTC by `council/slump_watch.py`. This is **a report, not a council verdict**.
- **Flag:** current FP/g **10 or more** below ESPN's projected FP/g. *Near the line* is 5 to 10 below.
- **Data:** all 112 rostered players in league 423671879, through scoring period 29. Teams have played **2 to 15 games**.
- **Checks:** No NBA game was in progress. Every current, projected, L7, L15, L30 and 2026 average re-scored with `scripts/league_scoring.py` matches ESPN's league-scored total (0 mismatches). Scoring period 28 (Mon 16 Nov US) re-scored from ESPN's final NBA box scores: all 58 rostered lines match.
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`; the current average does. Every gap is therefore smaller than a like-for-like gap, by the *bonus* figure on each player's driver line.

## Headline

**2 rostered players are 10+ FP/g under projection, on 1 of 8 teams.**

| Team | Flagged | Top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | 2 | Victor Wembanyama 70.4/60.5 · LaMelo Ball 35.1/46.4 · Josh Giddey 30.4/46.2 |
| Come-in Cider (us) | 0 | Cade Cunningham 51.2/50.4 · Kawhi Leonard 40.0/45.8 · Jamal Murray 49.2/43.9 |
| Dr White Slong | 0 | Giannis Antetokounmpo 60.8/57.6 · Donovan Mitchell 43.3/46.5 · Joel Embiid 36.0/45.4 |
| Lauri Birds | 0 | Nikola Jokic 65.3/67.2 · Tyrese Haliburton 53.2/48.6 · Stephen Curry 44.4/43.0 |
| Matt Wright's Foxies | 0 | Shai Gilgeous-Alexander 47.4/56.8 · Cooper Flagg 49.2/45.4 · Evan Mobley 39.9/43.3 |
| Melbourne poopoo | 0 | Anthony Davis 48.7/49.6 · Anthony Edwards 52.5/47.2 · Karl-Anthony Towns 50.2/44.1 |
| Snow Time Lakers | 0 | Jalen Johnson 42.4/50.0 · Jayson Tatum 47.1/48.1 · Kyrie Irving 41.5/44.2 |
| Team Nic Kerr | 0 | Luka Doncic 67.1/60.6 · Domantas Sabonis 43.9/46.7 · Tyrese Maxey 46.8/45.1 |

## Research

**Flagged:** Josh Giddey and LaMelo Ball are on Cream Abdul-Yammar. **Last 7 days:** Hart, Sabonis, Flagg, Herro, Ty Jerome, Gilgeous-Alexander, Embiid and Naz Reid. None of them is ours, and there are no pending trades.

- **LaMelo Ball (MIN):** **What explains the gap:** Minutes. ESPN's 32.9 projection is above anything he has played lately. He averaged a career-low 28.0 minutes for Charlotte last season, and that lighter load was a main reason he missed only 10 games ([Dunking With Wolves, 29 Sep 2026](https://dunkingwithwolves.com/limiting-lamelo-ball-s-minutes-can-help-chris-finch-come-playoff-time)). Early games were cut short too: 17 minutes in foul trouble on 26 Oct, then fouling out in 20 minutes on 1 Nov ([CBS Sports / RotoWire player news, 26 Oct to 15 Nov 2026](https://www.cbssports.com/nba/players/3149252/lamelo-ball/)). He played 25 minutes in a 133-94 rout of Dallas on 12 Nov ([CBS Sports / RotoWire, 12 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-catches-fire-from-deep/)). His role is bigger with Anthony Edwards out after right knee surgery (no timetable found in this search; *ESPN est.* 21 Dec 2026), so this is not a demotion.
  - **The last 7 days:** Shooting cratered. On 14 Nov vs CHI he had 19 points on 7-25 FG and 4-19 from three in 30 minutes ([NBC Sports, 16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/lamelo-ball-held-to-six-points-in-win-over-blazers)). On 16 Nov vs POR he had 6 points on 2-13 FG and 0 assists in 23:37, with 1 foul in an 8-point win ([Basketball-Reference box score, 16 Nov 2026](https://www.basketball-reference.com/boxscores/202611160MIN.html)). The Wolves sat him late while protecting a big lead ([SI / OnSI, 16–17 Nov 2026](https://www.si.com/nba/timberwolves/onsi/two-studs-one-dud-timberwolves-win-trail-blazers-01m7kr26g28n)). Chris Finch said he got "a lot of really good looks" and "This will turn around, he'll make shots" ([TSN, 17 Nov 2026](https://www.tsn.ca/nba/article/shannon-carries-wolves-with-edwards-out-ball-struggling-in-show-of-versatility-n1-50508081/)). No injury was reported. His right wrist contusion cleared on 2 Nov ([NBC Sports, 16 Nov 2026 page](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/lamelo-ball-held-to-six-points-in-win-over-blazers)).
- **Josh Giddey (CHI):** **What explains the gap:** He fell out of favour under new coach Tiago Splitter. Eight games in, Giddey was playing 27.3 minutes against 34.1 at the same point last season, with 9.3 points on 9.0 shots against 16.4. Splitter closed the Bulls' only win at that point with Tre Jones. Rookie Caleb Wilson had become the top scorer, and Giddey was carrying a left wrist sprain, though Splitter said "I haven't seen it affect his play" ([basketball.com.au, 6 Nov 2026](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)). Giddey himself said "I've probably played the worst eight games that I've played in my career" ([Chicago Sun-Times, 8 Nov 2026](https://chicago.suntimes.com/bulls/2026/11/08/josh-giddey-chicago-bulls-tiago-splitter-isaac-okoro-norman-powell-matas-buzelis-caleb-wilson-jalen-smith-philadelphia-76ers)). Turnovers (3.3 a game) are the "ongoing issue" ([Chicago Sun-Times, 17 Nov 2026](https://chicago.suntimes.com/bulls/2026/11/17/josh-giddey-playing-himself-out-bulls-starting-point-guard)).
  - **The last 7 days:** The window holds both ends. On 13 Nov he had a 15-10-14 triple-double in 39 minutes in an OT win over ATL ([basketball.com.au, 14 Nov 2026 AEDT](https://www.basketball.com.au/news/josh-giddey-triple-double-chicago-bulls-beat-atlanta-hawks-overtime)). On 16 Nov at CLE he had 4 points, 1-5 FG, 8 assists and 6 turnovers in 23:48 ([Basketball-Reference box score, 16 Nov 2026](https://www.basketball-reference.com/boxscores/202611160CLE.html)), and was benched for the final 8:44 while Tre Jones ran the offense ([ClutchPoints, 16 Nov 2026](https://clutchpoints.com/nba/chicago-bulls/bulls-news-josh-giddey-gets-100-real-on-4th-quarter-benching-vs-cavs)). He keeps the starting job for now. Splitter "doesn't intend to change the starting lineup" ([Pippen Ain't Easy, 17 Nov 2026](https://pippenainteasy.com/bulls-benching-josh-giddey-opens-door-tre-jones-sneak-starting-5)) and has "no set number" of games before judging a change ([Chicago Sun-Times, 17 Nov 2026](https://chicago.suntimes.com/bulls/2026/11/17/josh-giddey-playing-himself-out-bulls-starting-point-guard)). Caleb Wilson is out after hand surgery (no timetable found in this search; *ESPN est.* 13 Dec 2026).
- **Josh Hart (NY):** **What explains the gap:** His shot has gone, on top of missed games. In 10 games he is averaging 6.6 points on about 33.8% shooting, and Last Word on Sports argues for starting Landry Shamet instead ([Last Word on Sports, 17 Nov 2026](https://lastwordonsports.com/basketball/2026/11/17/knicks-best-lineup/)). He missed three straight games, 4, 7 and 10 Nov, first with right ankle soreness and then with an illness ([CBS Sports / RotoWire player news, 3–12 Nov 2026](https://www.cbssports.com/nba/players/2105193/josh-hart/)). Mike Brown said he would have played on 10 Nov but for the illness ([Basketnews, 10 Nov 2026](https://basketnews.com/news-259221-knicks-reveal-unfortunate-josh-hart-final-injury-status-vs-bucks.html)).
  - **The last 7 days:** He had 6 points on 3-8 FG in 26 minutes on 11 Nov vs CLE, with early foul trouble, and "looked a bit rusty" ([NBC Sports player news, 11 Nov 2026](https://www.nbcsports.com/nba/josh-hart/10642/news)). He was scoreless on 13 Nov vs IND (0-4) and sat the entire fourth quarter. He was scoreless again on 15 Nov at TOR (0-5 in 26 minutes), nine straight misses. Afterwards he said "Right now I'm not in a good headspace," and Brown answered "we need him" ([Heavy, updated 16 Nov 2026](https://heavy.com/sports/nba/new-york-knicks/mike-brown-josh-hart-knicks-struggles-response/)). Shamet scored 23 off the bench on 15 Nov ([CBS Sports / RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/knicks-landry-shamet-scores-season-high-23-points/)). Status: the Knicks listed no injuries for 17 Nov at TOR, and Hart was named as a starter ([VAVEL preview, 17 Nov 2026](https://www.vavel.com/en-us/nba/2026/11/17/1279612-knicks-vs-raptors-live-score-updates-and-play-by-play-nba.html)).
- **Domantas Sabonis (SAC):** **What explains the gap:** One dud game after a left knee scare. He was a late scratch on 8 Nov vs MIA with left knee soreness ([CBS Sports / RotoWire, 8 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/kings-domantas-sabonis-out-sunday/)). He came back on 10 Nov vs ORL and went scoreless for the first time in 596 games: 0-2 FG, 2 rebounds and 5 assists in 24 minutes, sitting the final 8:02 ([Field Level Media, 11 Nov 2026](https://fieldlevelmedia.com/nba/franz-wagner-pours-in-33-as-magic-end-skid-with-win-over-kings/)). Two days later he said "I'm 100 percent — I feel amazing" ([ClutchPoints, 12 Nov 2026](https://clutchpoints.com/nba/sacramento-kings/kings-news-domantas-sabonis-says-100-despite-recent-knee-injury-concern)).
  - **The last 7 days:** The other two games were normal. He had 21 points, 12 rebounds and 5 assists in 35 minutes on 13 Nov vs POR. On 15 Nov he had 11 points, 13 rebounds and 3 assists in 29 minutes in a 125-103 loss to OKC ([RotoWire player page, read 17 Nov 2026](https://www.rotowire.com/basketball/player/domantas-sabonis-3865); [FantasyPros, 16 Nov 2026](https://www.fantasypros.com/nba/news/620521/domantas-sabonis-delivers-double-double-sundays-loss.php)). No minutes limit was reported. Status: active, not on ESPN's injury list. Sam Amick (The Athletic) names him a potential NBA trade candidate as the 1-12 Kings look at a rebuild ([RotoWire player page, 15 Nov 2026 item](https://www.rotowire.com/basketball/player/domantas-sabonis-3865)).
- **Ty Jerome (MEM):** **What explains the gap:** His L7 covers only two games, a small sample, and then a hip problem. He had 22 points on 9-18 FG with 5 assists in 32 minutes on 11 Nov vs DEN ([RotoWire player page, read 17 Nov 2026](https://www.rotowire.com/basketball/player/ty-jerome-4774)). On 13 Nov vs NOP he had a down game: 17 points on 6-18 FG and 9 assists ([The Commercial Appeal via Yahoo, 14 Nov 2026](https://sports.yahoo.com/articles/grizzlies-guard-ty-jerome-ruled-214116660.html)). He then missed 14 Nov vs BKN, the second night of a back-to-back, and 16 Nov at WAS with right hip soreness. No in-game exit was reported, and no source says when the soreness began. Cam Spencer has started at point guard in his place ([NBC Sports, 15–16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ty-jerome-hip-remains-out-monday-vs-washington)).
  - **The latest status:** Right hip soreness, day-to-day. Reported timeline: his "next opportunity to return" is Wednesday 18 Nov at Cleveland ([CBS Sports / RotoWire, 15 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/grizzlies-ty-jerome-listed-out-for-monday/)). There is no firmer timetable. *ESPN est.* 18 Nov 2026.
- **Shai Gilgeous-Alexander (OKC):** **What explains the gap:** His scoring is intact, but everything else is thin. With Jalen Williams, Chet Holmgren and Cason Wallace all out since late October, "nearly every possession" runs through him ([CBS Sports / RotoWire, 14 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-powers-team-in-narrow-loss/)). He is at a career-high 35.5% usage, has missed 11 of 15 clutch shots and has looked "gassed in the closing minutes" ([Thunderous Intentions, 14 Nov 2026](https://thunderousintentions.com/okc-thunder-sga-looks-like-shell-of-clutch-player-of-the-year-self-losing-streak)). He has averaged 32.4 points over his last 10 games ([AP preview via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/oklahoma-city-takes-home-win-070351601.html)). Timelines for the injured teammates (none found in this search): Jalen Williams, left leg fracture, *ESPN est.* 2 Mar 2027. Cason Wallace, left shoulder surgery, *ESPN est.* 2 Mar 2027. Chet Holmgren, right knee, *ESPN est.* 2 Jan 2027.
  - **The last 7 days:** Blowouts cut his minutes, and his assists dried up. On 10 Nov vs POR he had 26 points on 8-22 FG (0-4 from three), 8 rebounds and 3 assists in 29 minutes, sitting the fourth of a 123-103 loss ([CBS Sports / RotoWire, 11 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-sits-in-final-stanza/)). On 11 Nov at POR he had 31 points (9-20 FG), 4 rebounds and 2 assists ([NBC Sports, 12 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/shai-gilgeous-alexander-scores-game-high-31)). On 13 Nov at LAC he had 40 points, 4 rebounds and 5 assists in 38 minutes ([CBS Sports / RotoWire, 14 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-powers-team-in-narrow-loss/)). On 15 Nov at SAC he had 37 points, 2 rebounds and 2 assists in 29 minutes, again sitting the fourth ([AP via ABC News, 15 Nov 2026](https://abcnews.com/Sports/wireStory/gilgeous-alexander-scores-37-thunder-beat-kings-125-138169198)). He has no injury himself and is not on the Thunder's injury list for 18 Nov vs ATL ([AP preview via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/oklahoma-city-takes-home-win-070351601.html)).
- **Naz Reid (CHA):** **What explains the gap:** Volume shooting at a poor percentage. His prominent role has produced 17.3 points and 8.5 rebounds a game, but his 41.1% shooting has hurt his efficiency ([CBS Sports / RotoWire player news, 13 Nov 2026 item](https://www.cbssports.com/nba/players/3148879/naz-reid/)). His big-usage game fell just outside the L7 window: 25 points and 13 rebounds on 26 shots on Monday 9 Nov vs CLE, with Kon Knueppel, Brandon Miller and Dennis Schroder all out (same source). Timelines for those two (none found in this search): Knueppel, left hamstring strain, *ESPN est.* 12 Dec 2026. Schroder, left hamstring strain, *ESPN est.* 25 Nov 2026.
  - **The last 7 days:** His L7 rests on two games, a small sample, and his usage dipped once Miller returned. On 12 Nov vs PHX he had 16 points on 6-18 FG, 8 rebounds and 3 assists in 34 minutes, in a 27-turnover loss ([CBS Sports / RotoWire player news, 13 Nov 2026 item](https://www.cbssports.com/nba/players/3148879/naz-reid/); [Yahoo Sports, 12–13 Nov 2026](https://sports.yahoo.com/articles/hornets-fall-suns-101-96-053629024.html)). On 15 Nov at LAC he had 17 points on 7-20 FG (3-11 from three), 4 rebounds, 3 assists and 4 fouls in 27:22. He started alongside the returning Miller and Coby White ([Basketball-Reference box score, 15 Nov 2026](https://www.basketball-reference.com/boxscores/202611150LAC.html)). Miller had been cleared after missing two games with a right hip strain ([Heavy, updated 15 Nov 2026](https://heavy.com/sports/nba/charlotte-hornets/hornets-brandon-miller-cleared-return-clippers/)). Reid has no injury reported, and there is NBA trade speculation about him (CBS "landing spots" piece, 12 Nov, per the [CBS player page](https://www.cbssports.com/nba/players/3148879/naz-reid/)). His second-half benching for "standards" was on 28 Oct, outside the window ([Yahoo Sports, 29 Oct 2026](https://sports.yahoo.com/nba/article/hornets-bench-veteran-naz-reid-in-second-half-of-loss-to-pistons-for-not-meeting-team-standards-023242700.html)).
- **Cooper Flagg:** So two of the three were blowouts with cut minutes. He also played the Boston game sick. He said he played through a mild illness and sounded congested afterwards ([Dallas Morning News via Yahoo, 16 Nov](https://sports.yahoo.com/articles/cooper-flagg-looks-mavericks-veterans-211854890.html)). On Tue 17 Nov he told Dusty May it was the first morning he had woken up feeling good; May said "he was good today" ([Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)).
  - **The 24 Oct absence was an injury, not rest.** An MRI showed a mild left shoulder sprain from the 23 Oct game at Indiana, and he was "listed as out … and re-evaluated next week" ([Dallas News, 24 Oct](https://www.dallasnews.com/sports/mavericks/article/cooper-flagg-injury-update-mavericks-spurs-pacers-22492135.php); [Yardbarker/Heavy, 24 Oct](https://www.yardbarker.com/nba/articles/cooper_flagg_injury_update_mavericks_star_set_to_miss_at_least_one_week_after_latest_setback/s1_16751_44469302)). He returned on 26 Oct with 40 minutes.
- **Tyler Herro:** His absence on 10 Nov, the first night of the 10–11 Nov back-to-back, was an injury: **Questionable, "Right [Knee] Contusion"**, later downgraded to out ([NBA injury report, 10 Nov 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-10_06_00PM.pdf)). He took a knee hit against Boston on 8 Nov, then played 35 minutes on 11 Nov. That gives no rest pattern.
  - Wednesday is his return to Miami, with a tribute video planned ([Yahoo Sports, 14 Nov 2026](https://sports.yahoo.com/articles/tyler-herro-returns-miami-night-171100292.html)). The Bucks' official 18 Nov report was not yet submitted at 4:30 PM. No source says he will sit on 18 or 19 Nov.
- **Joel Embiid:** Heavy via Yahoo, 16 Nov 2026: Nick Nurse called Sunday's 15 Nov rest (vs IND) "part of the plan of the management." The team chose that night as the rest day of the 15-16 Nov back-to-back. No new setback was reported. [Yahoo/Heavy](https://sports.yahoo.com/articles/76ers-joel-embiid-gets-encouraging-222340817.html). He was then upgraded and played 16 Nov at BKN: a season-high 37 points in 32 minutes.
  - Sportsmole preview of Wed 18 Nov at ORL, 17 Nov 2026: Embiid "carries no current injury designation." The Sixers' listed injuries are Jaylen Brown (hamstring and head), LeBron James (back), Dominick Barlow (back), Adem Bona (back) and Ariel Hukporti (Achilles). [Sportsmole](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/philadelphia-76ers-vs-orlando-magic-player-props-injury-report-and-prediction--nba_609259.html)

## By team

**Rank** is the player's rank on their fantasy roster by projection. **Min** is current / projected minutes. **Rate** is current FP/min as a share of projected FP/min. The driver line splits the gap into category shortfalls, in FP/g.

### Cream Abdul-Yammar: 2

| Player | NBA | Rank | GP | Min | Rate | Current | L7 | L15 | L30 | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 13 | 28.2 / 35.5 | 0.83 | 30.4 (13) | 29.8 (4) | 33.9 (7) | 30.4 (13) | 46.2 | **−15.8** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 14 | 27.5 / 32.9 | 0.90 | 35.1 (14) | 35.3 (3) | 39.3 (7) | 35.1 (14) | 46.4 | **−11.4** | 41.1 | Active |

- **Josh Giddey** (both): scoring −9.4, reb −4.0, ast −2.3, stocks −3.2, TO +1.0; bonus +2.2.
  - Current: 28.2 min, 9.9 pts, 3.7-9.1 FG, 1.3-2.1 FT, 5.2 reb, 8.5 ast, 0.4 stl, 0.6 blk, 3.3 TO
  - Last 7 days (4 GP): 28.5 min, 9.0 pts, 3.2-8.5 FG, 0.8-1.8 FT, 6.0 reb, 8.5 ast, 0.0 stl, 1.2 blk, 4.5 TO
  - Projected: 35.5 min, 18.5 pts, 6.6-14.5 FG, 3.4-4.4 FT, 9.2 reb, 9.6 ast, 1.2 stl, 0.6 blk, 3.8 TO
- **LaMelo Ball** (minutes): scoring −5.8, reb −1.9, ast −5.0, stocks +1.2, TO −0.6; bonus +0.7.
  - Current: 27.5 min, 17.7 pts, 6.2-14.9 FG, 1.8-2.4 FT, 3.7 reb, 5.8 ast, 1.9 stl, 0.1 blk, 3.6 TO
  - Last 7 days (3 GP): 26.3 min, 15.7 pts, 5.7-17.3 FG, 0.3-1.0 FT, 5.3 reb, 5.0 ast, 2.7 stl, 0.0 blk, 2.0 TO
  - Projected: 32.9 min, 23.9 pts, 8.3-20.5 FG, 2.8-3.2 FT, 5.6 reb, 8.3 ast, 1.4 stl, 0.3 blk, 3.3 TO
- **Near the line:** Desmond Bane −6.3 (#8, efficiency, L7 40.2).

### Come-in Cider (us): 0

No one flagged.

- **Near the line:** Jalen Duren −8.7 (#5, minutes, L7 —), Rudy Gobert −6.5 (#8, minutes, L7 31.0), Kawhi Leonard −5.8 (#2, minutes, L7 —), Trey Murphy III −5.8 (#7, efficiency, L7 —).

### Dr White Slong: 0

No one flagged.

- **Near the line:** Joel Embiid −9.4 (#3, efficiency, L7 34.3), Josh Hart −7.8 (#9, efficiency, L7 12.7), Derrick White −6.7 (#6, minutes, L7 28.2), AJ Dybantsa −6.3 (#10, efficiency, L7 24.2).

### Lauri Birds: 0

No one flagged.

- **Near the line:** Ivica Zubac −8.8 (#7, minutes, L7 35.7), Darius Garland −8.5 (#5, efficiency, L7 35.3), Kevin Durant −7.0 (#4, efficiency, L7 33.8).

### Matt Wright's Foxies: 0

No one flagged.

- **Near the line:** Shai Gilgeous-Alexander −9.4 (#1, efficiency, L7 45.8), Brandon Miller −8.7 (#8, minutes, L7 11.0), Damian Lillard −8.5 (#6, efficiency, L7 29.2), Naz Reid −5.6 (#10, efficiency, L7 25.5), Norman Powell −5.5 (#9, minutes, L7 41.7), De'Aaron Fox −5.5 (#7, efficiency, L7 29.5).

### Melbourne poopoo: 0

No one flagged.


### Snow Time Lakers: 0

No one flagged.

- **Near the line:** Jalen Johnson −7.6 (#1, efficiency, L7 42.5), Tyler Herro −5.1 (#6, minutes, L7 24.0).

### Team Nic Kerr: 0

No one flagged.

- **Near the line:** James Harden −9.3 (#5, efficiency, L7 45.3), Trae Young −7.3 (#4, efficiency, L7 37.5), Alex Sarr −5.8 (#7, efficiency, L7 35.2).

## Drivers

- *minutes*: 3+ minutes short of projection while producing at least 85% of the projected rate.
- *efficiency*: within 3 minutes of projection, so the shortfall is production.
- *both*: minutes short and the rate down too.

| Driver | Flagged players |
|---|---|
| minutes | LaMelo Ball |
| efficiency | — |
| both | Josh Giddey |

- **Flagged and not active on ESPN:** none.
- **Rostered, no games yet:** Brandon Ingram (Melbourne poopoo, projected 38.5, **Out**, ESPN est. back 19 Nov).

## Last 7 days

Players with 2+ games in the last 7 days whose L7 FP/g tells a different story from the season.

- **Flagged, but within 10 of projection over the last 7 days:** none.
- **Not flagged, but 10+ under projection over the last 7 days:** Josh Hart (Dr White Slong, L7 12.7 in 3 vs projected 33.0, L7 gap −20.3, season gap −7.8), Domantas Sabonis (Team Nic Kerr, L7 30.0 in 3 vs projected 46.7, L7 gap −16.7, season gap −2.8), Cooper Flagg (Matt Wright's Foxies, L7 29.3 in 3 vs projected 45.4, L7 gap −16.0, season gap 3.9), Tyler Herro (Snow Time Lakers, L7 24.0 in 3 vs projected 38.8, L7 gap −14.8, season gap −5.1), Ty Jerome (Melbourne poopoo, L7 32.0 in 2 vs projected 43.5, L7 gap −11.5, season gap −3.4), Shai Gilgeous-Alexander (Matt Wright's Foxies, L7 45.8 in 4 vs projected 56.8, L7 gap −11.1, season gap −9.4), Joel Embiid (Dr White Slong, L7 34.3 in 3 vs projected 45.4, L7 gap −11.0, season gap −9.4), Naz Reid (Matt Wright's Foxies, L7 25.5 in 2 vs projected 35.5, L7 gap −10.0, season gap −5.6).

## Under 2026, not under projection

10+ under last season's average, but within 10 of projection.

| Player | Team | GP | Min | Current | L7 | L15 | L30 | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|
| Jalen Duren | Come-in Cider (us) | 2 | 19.0 / 31.0 | 33.5 | — | — | 33.5 (2) → 44.0 (1) | 42.2 | 44.3 |
| Trey Murphy III | Come-in Cider (us) | 9 | 32.8 / 32.5 | 31.0 | — | 37.7 (3) | 31.0 (9) | 36.8 | 41.6 |
| Rudy Gobert | Come-in Cider (us) | 13 | 29.4 / 32.5 | 27.8 | 31.0 (3) | 31.3 (7) | 27.8 (13) | 34.3 | 38.2 |
| James Harden | Team Nic Kerr | 14 | 32.9 / 33.6 | 32.8 | 45.3 (3) | 34.2 (8) | 32.8 (14) | 42.1 | 45.1 |
| Jalen Johnson | Snow Time Lakers | 11 | 34.4 / 36.7 | 42.4 | 42.5 (2) | 41.0 (4) | 42.4 (11) | 50.0 | 53.1 |
| Joel Embiid | Dr White Slong | 12 | 31.5 / 31.6 | 36.0 | 34.3 (3) | 32.9 (7) | 36.0 (12) | 45.4 | 46.4 |

## Our pending trades

None.

## Sources

- ESPN fantasy API, league 423671879: `mRoster`, `mTeam`, `mSettings`, `mStatus` and `mPendingTransactions` views, read 2026-11-17 21:18 UTC.
- ESPN NBA scoreboard and box scores (`site.api.espn.com`) for the live-game guard and the box-score check.
- [Dunking With Wolves, 29 Sep 2026](https://dunkingwithwolves.com/limiting-lamelo-ball-s-minutes-can-help-chris-finch-come-playoff-time)
- [CBS Sports / RotoWire player news, 26 Oct to 15 Nov 2026](https://www.cbssports.com/nba/players/3149252/lamelo-ball/)
- [CBS Sports / RotoWire, 12 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/timberwolves-lamelo-ball-catches-fire-from-deep/)
- [NBC Sports, 16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-16/lamelo-ball-held-to-six-points-in-win-over-blazers)
- [Basketball-Reference box score, 16 Nov 2026](https://www.basketball-reference.com/boxscores/202611160MIN.html)
- [SI / OnSI, 16–17 Nov 2026](https://www.si.com/nba/timberwolves/onsi/two-studs-one-dud-timberwolves-win-trail-blazers-01m7kr26g28n)
- [TSN, 17 Nov 2026](https://www.tsn.ca/nba/article/shannon-carries-wolves-with-edwards-out-ball-struggling-in-show-of-versatility-n1-50508081/)
- [basketball.com.au, 6 Nov 2026](https://www.basketball.com.au/news/josh-giddey-stats-2026-27-vs-2025-26-chicago-bulls)
- [Chicago Sun-Times, 8 Nov 2026](https://chicago.suntimes.com/bulls/2026/11/08/josh-giddey-chicago-bulls-tiago-splitter-isaac-okoro-norman-powell-matas-buzelis-caleb-wilson-jalen-smith-philadelphia-76ers)
- [Chicago Sun-Times, 17 Nov 2026](https://chicago.suntimes.com/bulls/2026/11/17/josh-giddey-playing-himself-out-bulls-starting-point-guard)
- [basketball.com.au, 14 Nov 2026 AEDT](https://www.basketball.com.au/news/josh-giddey-triple-double-chicago-bulls-beat-atlanta-hawks-overtime)
- [Basketball-Reference box score, 16 Nov 2026](https://www.basketball-reference.com/boxscores/202611160CLE.html)
- [ClutchPoints, 16 Nov 2026](https://clutchpoints.com/nba/chicago-bulls/bulls-news-josh-giddey-gets-100-real-on-4th-quarter-benching-vs-cavs)
- [Pippen Ain't Easy, 17 Nov 2026](https://pippenainteasy.com/bulls-benching-josh-giddey-opens-door-tre-jones-sneak-starting-5)
- [Last Word on Sports, 17 Nov 2026](https://lastwordonsports.com/basketball/2026/11/17/knicks-best-lineup/)
- [CBS Sports / RotoWire player news, 3–12 Nov 2026](https://www.cbssports.com/nba/players/2105193/josh-hart/)
- [Basketnews, 10 Nov 2026](https://basketnews.com/news-259221-knicks-reveal-unfortunate-josh-hart-final-injury-status-vs-bucks.html)
- [NBC Sports player news, 11 Nov 2026](https://www.nbcsports.com/nba/josh-hart/10642/news)
- [Heavy, updated 16 Nov 2026](https://heavy.com/sports/nba/new-york-knicks/mike-brown-josh-hart-knicks-struggles-response/)
- [CBS Sports / RotoWire, 16 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/knicks-landry-shamet-scores-season-high-23-points/)
- [VAVEL preview, 17 Nov 2026](https://www.vavel.com/en-us/nba/2026/11/17/1279612-knicks-vs-raptors-live-score-updates-and-play-by-play-nba.html)
- [CBS Sports / RotoWire, 8 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/kings-domantas-sabonis-out-sunday/)
- [Field Level Media, 11 Nov 2026](https://fieldlevelmedia.com/nba/franz-wagner-pours-in-33-as-magic-end-skid-with-win-over-kings/)
- [ClutchPoints, 12 Nov 2026](https://clutchpoints.com/nba/sacramento-kings/kings-news-domantas-sabonis-says-100-despite-recent-knee-injury-concern)
- [RotoWire player page, read 17 Nov 2026](https://www.rotowire.com/basketball/player/domantas-sabonis-3865)
- [FantasyPros, 16 Nov 2026](https://www.fantasypros.com/nba/news/620521/domantas-sabonis-delivers-double-double-sundays-loss.php)
- [RotoWire player page, read 17 Nov 2026](https://www.rotowire.com/basketball/player/ty-jerome-4774)
- [The Commercial Appeal via Yahoo, 14 Nov 2026](https://sports.yahoo.com/articles/grizzlies-guard-ty-jerome-ruled-214116660.html)
- [NBC Sports, 15–16 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-15/ty-jerome-hip-remains-out-monday-vs-washington)
- [CBS Sports / RotoWire, 15 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/grizzlies-ty-jerome-listed-out-for-monday/)
- [CBS Sports / RotoWire, 14 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-powers-team-in-narrow-loss/)
- [Thunderous Intentions, 14 Nov 2026](https://thunderousintentions.com/okc-thunder-sga-looks-like-shell-of-clutch-player-of-the-year-self-losing-streak)
- [AP preview via Yahoo, 17 Nov 2026](https://sports.yahoo.com/articles/oklahoma-city-takes-home-win-070351601.html)
- [CBS Sports / RotoWire, 11 Nov 2026](https://www.cbssports.com/fantasy/basketball/news/thunders-shai-gilgeous-alexander-sits-in-final-stanza/)
- [NBC Sports, 12 Nov 2026](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-12/shai-gilgeous-alexander-scores-game-high-31)
- [AP via ABC News, 15 Nov 2026](https://abcnews.com/Sports/wireStory/gilgeous-alexander-scores-37-thunder-beat-kings-125-138169198)
- [CBS Sports / RotoWire player news, 13 Nov 2026 item](https://www.cbssports.com/nba/players/3148879/naz-reid/)
- [Yahoo Sports, 12–13 Nov 2026](https://sports.yahoo.com/articles/hornets-fall-suns-101-96-053629024.html)
- [Basketball-Reference box score, 15 Nov 2026](https://www.basketball-reference.com/boxscores/202611150LAC.html)
- [Heavy, updated 15 Nov 2026](https://heavy.com/sports/nba/charlotte-hornets/hornets-brandon-miller-cleared-return-clippers/)
- [Yahoo Sports, 29 Oct 2026](https://sports.yahoo.com/nba/article/hornets-bench-veteran-naz-reid-in-second-half-of-loss-to-pistons-for-not-meeting-team-standards-023242700.html)
- [Dallas Morning News via Yahoo, 16 Nov](https://sports.yahoo.com/articles/cooper-flagg-looks-mavericks-veterans-211854890.html)
- [Dallas Sports Journal, 17 Nov](https://dallassportsjournal.com/cooper-flagg-illness-max-christie-santi-aldama-mavericks-practice/)
- [Dallas News, 24 Oct](https://www.dallasnews.com/sports/mavericks/article/cooper-flagg-injury-update-mavericks-spurs-pacers-22492135.php)
- [Yardbarker/Heavy, 24 Oct](https://www.yardbarker.com/nba/articles/cooper_flagg_injury_update_mavericks_star_set_to_miss_at_least_one_week_after_latest_setback/s1_16751_44469302)
- [NBA injury report, 10 Nov 2026 6 PM](https://ak-static.cms.nba.com/referee/injury/Injury-Report_2026-11-10_06_00PM.pdf)
- [Yahoo Sports, 14 Nov 2026](https://sports.yahoo.com/articles/tyler-herro-returns-miami-night-171100292.html)
- [Yahoo/Heavy](https://sports.yahoo.com/articles/76ers-joel-embiid-gets-encouraging-222340817.html)
- [Sportsmole](https://www.sportsmole.co.uk/basketball/philadelphia-76ers/preview/philadelphia-76ers-vs-orlando-magic-player-props-injury-report-and-prediction--nba_609259.html)
