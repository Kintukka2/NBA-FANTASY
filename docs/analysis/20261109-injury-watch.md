# Injury Watch: 09 Nov 2026

- Generated 2026-11-09 06:46 UTC by `council/injury_watch.py`. This is **a report, not a council verdict**.
- **Injuries:** 95 players in ESPN's injury feed. 29 are out more than 7 days (ESPN est.) with a role of 15+ minutes, on 17 teams.
- **Method:** each team's last 10 finished games, re-scored from ESPN's box scores. Each teammate's minutes and FP are split into games without the absentees against games with them, or against ESPN's projection when they have been out all season.
  - *Best placed* means 3+ minutes gained, ordered by FP/g in the games without the absentees.
  - A pickup is a free agent or waiver player getting 18+ minutes in those games.
- **Checks:** no NBA game was in progress. All 1100 pool players' current, projected, L7, L15, L30 and 2026 averages re-score with `scripts/league_scoring.py` to ESPN's totals (0 mismatches).
- **L7 / L15 / L30:** FP/g over the last 7, 15 and 30 days, games in brackets, from ESPN's rolling splits, re-scored with `scripts/league_scoring.py`. L30 covers every game so far for every player listed, so they equal the season average for now. **A → B** means `council/gamelog.py` dropped an outlier from that window (a bad game 12+ FP under the next worst, or a short game 10+ minutes under the next fewest); B is the average without it.
- **Games** is games left this week (09 Nov–15 Nov) / next week (16 Nov–22 Nov).
- **ESPN est.** is ESPN's estimated return. The skill adds the reported timeline beside it.

## Shortlist

- **Our five lowest** (script): P.J. Washington 29.5 (L7 32.5), Hartenstein 29.6 (L7 31.0), Murphy 31.0 (L7 37.7), Gafford 31.5 (L7 29.5) and Duren 33.5 (out; re-evaluated about 22 Nov, no return date reported; *ESPN est.* 24 Nov) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/). The floor is **33.5**, set by an injured player, and no pickup clears it. Only Bane (32.7) is above all four healthy ones.
- **What a stash costs:** `council/roster.csv` records Duren moved to IR and Kawhi back to the bench on 9 Nov, after the script read ESPN, so its IR line below still names Kawhi. Kawhi is OUT too (not on court yet, likely to miss all four Toronto games this week; *ESPN est.* 23 Nov) [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html), so any stash costs a healthy player's bench spot.
- **Rate** is `python council/form.py` (09 Nov 06:49 UTC). Braun and Mara are on waivers and clear in 24 hours.

| Player | NBA | Opening and its window | FP/g without | Season | L7 / L15 / L30 | Rate | Min without | Games this / next week |
|---|---|---|---:|---:|---|---:|---:|---|
| **Desmond Bane** (free agent, 90%; in our plan for Tue 10) | ORL | Paolo Banchero: low-grade high-ankle sprain, 4–6 weeks from 24 Oct, so 21 Nov–5 Dec; out again 7 Nov [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html) [Roundtable, 7 Nov](https://roundtable.io/sports/nba/warriors/news/warriors-vs-magic-injury-report-draymond-green-paolo-banchero-statuses); *ESPN est.* 22 Nov. Bane is day-to-day with an illness; next chance Tue 10 at SAC, and no newer status was found [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/) (*ESPN est.* 10 Nov) | 32.7 | 27.8 | 28.0 (3) / 32.7 (6) / 27.8 (8) → 31.9 (7) | 31.1 | 36.0 | 3 / 4 |
| **Christian Braun** (waivers, 39%) | DEN | Julian Strawther: left knee sprain, re-evaluation six weeks from mid-Oct, about 29 Nov, which is not a return date [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html); *ESPN est.* 29 Nov. Braun is questionable Mon at HOU with a left calf contusion and an illness [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou) (no timetable reported; *ESPN est.* 9 Nov) | 30.1 | 30.1 | 22.7 (3) / 32.3 (7) / 30.1 (8) | 28.0 | 34.2 | 3 / 4 |
| **Aday Mara** (waivers, 18%) | OKC | Chet Holmgren: 8–10 weeks from 30 Oct, about 25 Dec–8 Jan [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear); *ESPN est.* 2 Jan. His starts hinge on Jaylin Williams (back spasms; next chance Tue 10 at POR; no timetable reported; *ESPN est.* 10 Nov) [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/) | 29.9 | 24.4 | 31.8 (4) / 27.0 (8) / 24.4 (10) | 27.8 | 22.7 | 4 / 3 |
| **Aaron Wiggins** (free agent, 35%) | ATL | Mouhamed Gueye: foot surgery 14 Jul, re-evaluation in 3–4 months, no result reported [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html); *ESPN est.* 20 Nov. Wiggins's bench minutes are not tied to Gueye [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653) | 28.8 | 28.7 | 28.5 (4) / 28.2 (9) / 28.7 (11) | 27.9 | 25.7 | 3 / 3 |

- **Back-soon stash candidates:**
  - **Yves Missi** (NO, free agent, 15%): left knee bone bruise; he missed his eighth straight game Sunday at LAC and is week-to-week with no timetable reported [Yahoo, 8 Nov](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-los-205416257.html) [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773); *ESPN est.* 9 Nov; news-watch floor 12 Nov. Current 41.5 (2) → 68.0 (1), L7 —, L15 —, L30 41.5 (2) → 68.0 (1), projected 24.7, rate 60.4: all of it a **small sample** (one 68-FP game after a dropped 9-minute exit). Games 4 / 4. Our plan treats him as out Fri 13–Sat 14. If New Orleans lists him questionable or better for Friday, he outranks every Friday streamer (today's matchup report). Cost: a healthy bench spot, because Duren holds IR.
  - **Norman Powell** (CHI, free agent, 78%): right shoulder inflammation, out Sunday; next chance Wed 11 vs SAS [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-out-sunday-538162) [FantasyPros, 8 Nov](https://www.fantasypros.com/nba/news/618532/norman-powell-shoulder-ruled-out-sunday.php). No timetable reported; *ESPN est.* 11 Nov. Current 26.2 (8) → 29.4 (7); L7 13.5 (2) → 23.0 (1), a **small sample** and noise (no report ties the dip to the shoulder); L15 26.8 (6) → 31.4 (5); L30 26.2 (8) → 29.4 (7); projected 36.0; 2026 33.0; rate 28.0. Games 3 / 4. A Wednesday pickup rather than a stash; his rate trails Jalen Smith's 34.9 on the same Chicago nights.
  - **Off the list:** Kon Knueppel, last night's stash candidate, is now out at least four weeks [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html) (*ESPN est.* 12 Dec).
- The add/drop call is yours, or the council's (`/council`).

### Against our streaming plan (Mon 9 – Sun 15 Nov)

The plan adds Bane on Tue 10 (if cleared), then Jalen Smith, Gobert, Peyton Watson, LaVine and Hachimura (`docs/analysis/20261109-matchup4.md`). Rates are `form.py`'s; game days are each team's schedule in that matchup report.

| Day | Plan add | Rate | Best injury-watch candidate that day | Rate |
|---|---|---:|---|---:|
| Tue 10 | Desmond Bane (if cleared) | 31.1 | Robert Williams III (POR) | 29.3 |
| Wed 11 | Jalen Smith (CHI) | 34.9 | Devin Vassell (SA); Norman Powell (CHI, if back) | 29.1; 28.0 |
| Thu 12 | Rudy Gobert (MIN) | 29.6 | Kevin Huerter (DET) | 28.2 |
| Fri 13 | Peyton Watson (CLE), Jalen Smith | 30.2, 34.9 | Yves Missi (NO, if cleared) | 60.4 (small sample) |
| Sat 14 | Peyton Watson, Jalen Smith | 30.2, 34.9 | Yves Missi (if cleared); otherwise Spencer Jones (DEN) | 60.4; 29.1 (both small samples) |
| Sun 15 | Zach LaVine (SAC), Rui Hachimura (LAC) | 30.9, 30.6 | Devin Vassell (SA) | 29.1 |

- **Verdict: no pickup in this report beats the plan's player on any day.** The one exception would be Missi on Fri 13 or Sat 14 if New Orleans clears him, and his rate is a small sample.
- **Plan risks the research found:**
  - **Bane (Tue 10):** no update since his 7 Nov illness scratch [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/); *ESPN est.* 10 Nov. The matchup plan keeps Myles Turner as the fallback.
  - **Hachimura (Sun 15):** his extra minutes ride on Ingram and Beal being out. Ingram has begun 5-on-5 work with no timetable reported (*ESPN est.* 10 Nov) [RealGM, 7 Nov](https://basketball.realgm.com/wiretap/288060/Brandon-Ingram-Ramping-Up-Towards-Clippers-Debut); Beal has no timetable reported (*ESPN est.* 29 Nov) [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). Hachimura scored 14 in Sunday's 139-123 win over NOP [AP via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-beat-pelicans-end-7-044836989.html).
  - **Jalen Smith (Wed 11–Sat 14):** kept the start Sunday, with Nic Claxton off the bench for 18 minutes [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/nic-claxton-hamstring-plays-18-minutes-sunday). Claxton taking the job once his limit lifts is the risk.
  - **Peyton Watson (Fri 13–Sat 14):** off the injury report since 7 Nov after right hamstring tightness, "a full go" [FantasyPros, 7 Nov](https://www.fantasypros.com/nba/news/618370/peyton-watson-hamstring-off-injury-report-saturday.php).
  - **A stale override:** `council/news_overrides.csv` still sets Kon Knueppel back 13 Nov. Charlotte's four-week re-evaluation from 8 Nov [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html) makes ESPN's 12 Dec the better date, so the next news watch should remove the row. It does not touch our plan.

## Since the last Injury Watch

Against last night's `docs/analysis/20261108-injury-watch.md` (20:14 UTC). Sunday's games are in this run.

- **New long absences: Kon Knueppel and Dennis Schroder (CHA, both free agents).** On 8 Nov Charlotte announced left hamstring strains: Knueppel re-evaluated in four weeks (about 6 Dec; *ESPN est.* 12 Dec, from 9 Nov) and Schroder in two (about 22 Nov; *ESPN est.* 25 Nov, from 9 Nov) [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html) [ESPN, 8 Nov](https://espn.com/nba/story/_/id/50425681/kon-knueppel-least-four-weeks-hamstring-strain). CHA joins the team list (29 absences on 17 teams, from 27 on 16).
- **Pickups joined:** Hannes Steinbach and Royce O'Neale (CHA, opened by Knueppel and Schroder; one game each, a small sample, with Grant Williams and Moussa Diabaté also out) and Kevin Huerter (DET, opened by Duren, after Sunday's 24-point game [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/kevin-huerter-posts-22-4-5-2-5-line-vs-lakers)).
- **Pickups left:** Jamal Shead, now on Lauri Birds, our opponent this week; and Kobe Sanders, whose FP/g without the absentees fell to 19.6, under the 20 line. Daniss Jenkins rose from 20.7 to 26.0 after a career-high 31 on Sunday [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/daniss-jenkins-drops-career-high-31-points-in-loss).
- **Our five lowest:** P.J. Washington 29.5, Hartenstein 29.6, Murphy 31.0, Gafford 31.5, Duren 33.5. The floor is unchanged at 33.5.
- **Back soon, joined:** DeMar DeRozan, Aaron Gordon, Cameron Johnson and Christian Braun (all DEN, all questionable Mon at HOU; no timetable reported; *ESPN est.* 9 Nov) [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/) [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets); Devin Vassell (questionable Mon at PHX; *ESPN est.* 9 Nov) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/devin-vassell-groin-questionable-monday-vs-phx); Quentin Grimes (finger, X-rays negative; *ESPN est.* 9 Nov) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger); T.J. McConnell (questionable Mon; *ESPN est.* 9 Nov) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/t-j-mcconnell-hamstring-questionable-monday).
- **Back soon, left:** Knueppel (now beyond 14 days), and Deandre Ayton, Keegan Murray and Mitchell Robinson, all three off ESPN's injury feed.
- **New on the feed, beyond those:** Jamal Murray (ours; questionable Mon at HOU; *ESPN est.* 9 Nov) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets) and Nikola Jokic (Lauri Birds; right elbow sprain, questionable Mon; *ESPN est.* 9 Nov) [Heavy, 8 Nov](https://heavy.com/sports/nba/denver-nuggets/nikola-jokic-elbow-injury-news-rockets/), plus three short listings outside our targets (see *Every injury*).
- **Status changes:** Brandon Miller (Matt Wright's Foxies) went from day-to-day to out, with the groin injury rediagnosed as a right hip strain that may cost a few games (*ESPN est.* 12 Nov) [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/and-lastly-brandon-miller-has-been-diagnosed-with-a/92682399007/) [RotoBaller, 8 Nov](https://www.rotoballer.com/player-news/brandon-miller-sidelined-monday-versus-cavaliers/1987955). Lauri Markkanen (Lauri Birds) went from day-to-day to out, after a questionable tag on the Jazz's 8 Nov report (right wrist sprain; no timetable reported; *ESPN est.* 10 Nov) [Jazz on X, 8 Nov](https://x.com/utahjazz/status/2119463702122434874). Fourteen other short listings moved later, by two to seven days (see *Every injury*).
- **Ours:** Duren is now in IR and Kawhi on the bench (9 Nov, `council/roster.csv`), as last night's report advised. Kawhi is still off the court [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html); Duren's two-week re-evaluation stands [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/).

## Pickups for us

Free agents and waiver players getting 18+ minutes and 20+ FP/g since an absence opened their role, best first. Waiver players clear in 24 hours. *Also out* names short-term absences in the same games, which inflate the gain until those players return.

Our five lowest current FP/g: P.J. Washington 29.5 (L7 32.5), Isaiah Hartenstein 29.6 (L7 31.0), Trey Murphy III 31.0 (L7 37.7), Daniel Gafford 31.5 (L7 29.5), Jalen Duren 33.5 (L7 —). A pickup at or above **33.5** beats all five.

| Player | NBA | Opening | Games without | Min without | Δ min | FP/g without | Season FP/g | L7 | L15 | L30 | League | Owned | Games |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Desmond Bane** (day to day, ESPN est. back 10 Nov) | ORL | Paolo Banchero (22 Nov) | 6 | 36.0 | +6.0 | **32.7** | 27.8 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | Free agent | 90% | 3 / 4 |
| **Hannes Steinbach** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov); also out: Grant Williams (12 Nov), Moussa Diabate (09 Nov) | 1 | 27.0 | +19.3 | **31.0** | 11.2 | 16.5 (2) | 10.7 (3) | 11.2 (4) | Free agent | 1% | 3 / 2 |
| **Christian Braun** (day to day, ESPN est. back 09 Nov) | DEN | Julian Strawther (29 Nov) | 8 | 34.2 | +6.8 | **30.1** | 30.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 39% | 3 / 4 |
| **Spencer Jones** | DEN | Julian Strawther (29 Nov) | 1 | 21.0 | — | **30.0** | 30.0 | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 1% | 3 / 4 |
| **Aday Mara** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 7 | 22.7 | +9.7 | **29.9** | 24.4 | 31.8 (4) | 27.0 (8) | 24.4 (10) | Waivers | 18% | 4 / 3 |
| **Aaron Wiggins** | ATL | Mouhamed Gueye (20 Nov) | 10 | 25.7 | +5.4 | **28.8** | 28.7 | 28.5 (4) | 28.2 (9) | 28.7 (11) | Free agent | 35% | 3 / 3 |
| **Derrick Jones Jr.** | LAC | Bradley Beal (29 Nov), Jordan Miller (02 Mar); also out: Brandon Ingram (10 Nov) | 8 | 29.9 | +4.5 | **27.8** | 27.8 | 22.7 (3) | 26.3 (6) | 27.8 (8) | Free agent | 12% | 3 / 3 |
| **Daniss Jenkins** | DET | Jalen Duren (24 Nov) | 7 | 26.6 | +8.1 | **26.0** | 24.9 | 24.7 (3) | 26.0 (7) | 24.9 (9) | Free agent | 4% | 3 / 4 |
| **Ja'Kobe Walter** | TOR | Kawhi Leonard (23 Nov) | 7 | 30.7 | +7.2 | **25.3** | 25.9 | 18.8 (4) | 25.3 (7) | 25.9 (9) | Free agent | 12% | 4 / 3 |
| **Kevin Huerter** | DET | Jalen Duren (24 Nov) | 7 | 22.9 | +3.9 | **25.3** | 22.4 | 37.3 (3) | 25.1 (7) | 22.4 (9) | Free agent | 2% | 3 / 4 |
| **Jared McCain** | OKC | Cason Wallace (02 Mar), Chet Holmgren (02 Jan), Jalen Williams (02 Mar) | 7 | 27.3 | +7.0 | **24.6** | 20.9 | 28.0 (4) | 21.8 (8) | 20.9 (10) | Free agent | 30% | 4 / 3 |
| **Jordan Goodwin** (out, ESPN est. back 09 Nov) | PHX | Mark Williams (03 Feb) | 5 | 18.8 | — | **24.4** | 24.4 | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% | 4 / 3 |
| **Royce O'Neale** | CHA | Kon Knueppel (12 Dec), Dennis Schroder (25 Nov); also out: Grant Williams (12 Nov), Moussa Diabate (09 Nov) | 1 | 26.0 | +8.0 | **24.0** | 12.1 | 12.3 (3) | 10.9 (8) | 12.1 (10) | Free agent | 1% | 3 / 2 |
| **Collin Murray-Boyles** | TOR | Kawhi Leonard (23 Nov) | 7 | 23.1 | +4.1 | **24.0** | 24.4 | 29.2 (4) | 24.3 (7) | 24.4 (9) | Free agent | 12% | 4 / 3 |
| **Quenton Jackson** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 22.0 | +6.0 | **23.0** | 23.3 | 27.2 (4) | 23.6 (8) | 23.3 (10) | Free agent | 5% | 4 / 3 |
| **Leaky Black** | SAC | Ben Simmons (01 Oct); also out: Maxime Raynaud (10 Nov) | 6 | 19.2 | — | **21.2** | 21.2 | 28.8 (4) | 21.2 (6) → 25.4 (5) | 21.2 (6) → 25.4 (5) | Free agent | 1% | 3 / 3 |
| **Jarace Walker** | IND | Johnny Furphy (02 Jan), Ben Sheppard (02 Jan) | 9 | 24.1 | +5.1 | **20.6** | 19.1 | 22.2 (4) | 23.4 (8) | 19.1 (10) | Free agent | 1% | 4 / 3 |
| **Trevon Brazile** | DEN | Julian Strawther (29 Nov) | 8 | 21.1 | — | **20.5** | 20.5 | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% | 3 / 4 |

### Notes

- **Desmond Bane (ORL):** L7 28.0 (3) against a season of 27.8, not 5+ off. Scratched 7 Nov with an illness; next chance Tue 10 at SAC, with no newer status found [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/). No timetable reported; *ESPN est.* 10 Nov.
  - **Role:** starter. The +6.0 minutes come with Banchero out (4–6 weeks from 24 Oct) [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html), so they should shrink when he returns, 21 Nov at the earliest.
- **Hannes Steinbach (CHA):** his 31.0 rests on one game without the absentees, a **small sample**, and his L7 16.5 (2) is a small sample too, so the gap to his season 11.2 is noise; rate 13.3 (`form.py`).
  - That game was 6 Nov vs BOS: 27 minutes, the team's most, with 11 rebounds and 3 blocks [Yahoo, Nov](https://sports.yahoo.com/articles/hannes-steinbach-calls-extended-hornets-171704327.html). Diabaté and Grant Williams were out as well.
  - **Does it last?** Diabaté is questionable Mon vs CLE (right quadriceps tendinopathy; no timetable reported; *ESPN est.* 9 Nov), and Grant Williams is out (right hamstring strain; no timetable reported; *ESPN est.* 12 Nov) [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-injury-latest-brandon-miller-011009724.html) [Sports Mole, 8 Nov](https://www.sportsmole.co.uk/basketball/cleveland-cavaliers/preview/cleveland-cavaliers-vs-charlotte-hornets-player-props-injury-report-and-prediction--nba_608728.html). Basketnews names Coby White, Sion James and Grayson Allen for the bigger roles, not Steinbach [Basketnews, 8 Nov](https://basketnews.com/news-259083-kon-knueppel-injury-hornets-announce-new-devastating-update-and-recovery-timeline.html). Not a pickup.
- **Christian Braun (DEN):** L7 22.7 (3) against a season of 30.1, more than 5 under. The reason is shooting: 6 points on 2-of-8 in 29 minutes on 7 Nov [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-passive-performance-in-win/).
  - Questionable Mon at HOU (left calf contusion and illness); Spencer Jones could start if he sits [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-questionable-for-monday-538201/). No timetable reported; *ESPN est.* 9 Nov.
  - **Role:** starter; Strawther (about 29 Nov) is a bench wing, and no source ties Braun's start to him [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html).
- **Spencer Jones (DEN):** one game, a **small sample** (30.0; rate 29.1). He had 13 points in 21 minutes in his 7 Nov debut [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/), and could start Monday if Braun sits [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou). All five Denver starters and DeRozan are questionable for Monday [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/).
- **Aday Mara (OKC):** L7 31.8 (4) against a season of 24.4, more than 5 above: his starts, the latest on 7 Nov in OKC's bigger lineup [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart).
  - Jaylin Williams (back spasms) has missed three straight; next chance Tue 10 at POR; no timetable reported; *ESPN est.* 10 Nov [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/). Nothing newer was found. His return would likely end Mara's starts (inference); Holmgren's absence keeps the backup minutes.
- **Aaron Wiggins (ATL):** L7 28.5 (4) against 28.7, not 5+ off. Bench role, the most minutes of Atlanta's reserves [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653). No newer report found.
- **Derrick Jones Jr. (LAC):** L7 22.7 (3) against 27.8, 5.1 under; no report explaining the dip was found. He has started since returning from knee soreness on 4 Nov [NBC, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/derrick-jones-jr-knee-absent-from-injury-report), and the Clippers listed him to start Sunday's win over NOP [NBA.com, 8 Nov](https://www.nba.com/pelicans/news/gameday-update-pelicans-at-clippers-11-8-2026).
  - **Does it last?** Ingram (no timetable reported; *ESPN est.* 10 Nov) has begun 5-on-5 work [RealGM, 7 Nov](https://basketball.realgm.com/wiretap/288060/Brandon-Ingram-Ramping-Up-Towards-Clippers-Debut); his debut would cut Jones's minutes (inference). Beal has no timetable reported (*ESPN est.* 29 Nov) [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans).
- **Daniss Jenkins (DET):** L7 24.7 (3) against 24.9, not 5+ off. Career-high 31 points off the bench Sunday (8-of-15 from three in 32 minutes) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/daniss-jenkins-drops-career-high-31-points-in-loss) [CBS box score, 8 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261108_LAL@DET/).
  - Isaiah Joe was out too (right hip contusion, sixth straight miss; no timetable reported; *ESPN est.* 9 Nov) [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-joe-hip-remains-out-sunday-vs-lakers). Duren's minutes go to Paul Reed at center [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/), not to a guard. One hot shooting night; rate 24.8.
- **Ja'Kobe Walter (TOR):** L7 18.8 (4) against a season of 25.9, more than 5 under. The reason is shooting: 2-of-12 on 6 Nov [Raptors Republic, 6 Nov](https://raptorsrepublic.com/2026/11/06/quick-reaction-raptors-121-bucks-107/).
  - **Role:** he starts in Kawhi's place [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl), and Kawhi is likely to miss all four Toronto games this week [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html), so the start should hold through Sun 15. Rate 22.8.
- **Kevin Huerter (DET):** L7 37.3 (3) against a season of 22.4, more than 5 above: Sunday's 24 points, 5 blocks and 2 steals in 35 minutes off the bench [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/kevin-huerter-posts-22-4-5-2-5-line-vs-lakers).
  - With Isaiah Joe out, Huerter, Javonte Green and Ron Holland have had bigger roles [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-isaiah-joe-another-absence-coming/). Joe's return (*ESPN est.* 9 Nov) and Duren's (re-evaluated about 22 Nov) should trim them (inference). NBC sees little fantasy appeal in a bench role unless his three-point shooting holds [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/kevin-huerter-posts-22-4-5-2-5-line-vs-lakers). Rate 28.2.
- **Jared McCain (OKC):** L7 28.0 (4) against a season of 20.9, more than 5 above: minutes, 25+ in six straight, and a 21-point start on 6 Nov [NBC, 6 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-06/jared-mccain-drops-21-points-in-lopsided-win). He went back to the bench on 7 Nov [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jared-mccain-news-returns-to-bench-saturday-538052). Rate 23.1.
- **Jordan Goodwin (PHX):** L7 13.0 (1) is one game, noise (he left it after 10 minutes with the calf injury). Upgraded to questionable Mon vs SAS after three straight misses (right calf) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jordan-goodwin-calf-questionable-monday-vs-sas) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/suns-jordan-goodwin-iffy-for-monday/). No timetable reported; *ESPN est.* 9 Nov.
- **Royce O'Neale (CHA):** his 24.0 rests on one game, a **small sample**, against a season of 12.1 (rate 12.7). Same Charlotte confounds as Steinbach; no report of a bigger role was found, and Basketnews names others for it [Basketnews, 8 Nov](https://basketnews.com/news-259083-kon-knueppel-injury-hornets-announce-new-devastating-update-and-recovery-timeline.html).
- **Collin Murray-Boyles (TOR):** L7 29.2 (4) against 24.4, under 5 off. He gets more minutes if Barnes sits Monday [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html). Rate 26.1.
- **Quenton Jackson and Jarace Walker (IND):** L7 27.2 (4) against 23.3, and 22.2 (4) against 19.1; neither 5+ off. T.J. McConnell debuted 7 Nov with 9 minutes on an apparent restriction and is questionable Monday [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-strikes-for-six-points-in-season-debut/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/t-j-mcconnell-hamstring-questionable-monday); Haliburton still has no timetable reported (*ESPN est.* 13 Nov) [Roundtable, Nov](https://roundtable.io/sports/nba/pacers/news/pacers-still-have-no-timeline-for-tyrese-haliburton-s-return). McConnell's ramp-up should trim Jackson's minutes (inference).
- **Leaky Black (SAC):** L7 28.8 (4) against a season of 21.2 (6) → 25.4 (5), more than 5 above the plain average: his 40-minute fill-in start on 6 Nov. De'Andre Hunter was cleared for Sunday and reclaimed the start, sending Black back to the bench [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/kings-leaky-black-steady-in-fill-in-role/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/sac-acuff-lavine-hunter-achiuwa-cardwell). The gain is over.
- **Trevon Brazile (DEN):** the backup four; Spencer Jones's return threatens his minutes [Yahoo, Nov](https://sports.yahoo.com/articles/nuggets-better-options-cutting-trevon-160004870.html). Rate 19.9.

## Injured and available, back soon

Free agents and waiver players ESPN expects back within 14 days, worth 25+ FP/g on their current, projected or last-season average.

- **Our IR slot:** taken by Kawhi Leonard. A stash costs a bench spot until it frees up.
- **Since the script ran:** `council/roster.csv` records Duren in IR and Kawhi on the bench (9 Nov). Both are OUT, so a stash still costs a healthy bench spot [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html).

| Player | NBA | Injury | ESPN est. | Days | Current FP/g | L7 | L15 | L30 | Projected | 2026 | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| **Yves Missi** | NO | Left Knee Bruise | 09 Nov | 0 | 41.5 | — | — | 41.5 (2) → 68.0 (1) | 24.7 | 22.5 | Free agent | 15% | 4 / 4 |
| **Desmond Bane** | ORL | Illness | 10 Nov | 1 | 27.8 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | 38.2 | 36.9 | Free agent | 90% | 3 / 4 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 11 | — | — | — | — | 27.6 | 36.7 | Free agent | 7% | 4 / 4 |
| **Norman Powell** | CHI | Right Shoulder Inflammation | 11 Nov | 2 | 26.2 | 13.5 (2) → 23.0 (1) | 26.8 (6) → 31.4 (5) | 26.2 (8) → 29.4 (7) | 36.0 | 33.0 | Free agent | 78% | 3 / 4 |
| **Jalen Suggs** | ORL | Right Knee | 10 Nov | 1 | 26.3 | — | 23.0 (1) | 26.3 (3) | 29.2 | 34.7 | Free agent | 17% | 3 / 4 |
| **DeMar DeRozan** | DEN | Back Spasms | 09 Nov | 0 | 18.9 | 16.0 (2) | 21.3 (6) | 18.9 (7) | 29.8 | 32.7 | Free agent | 58% | 3 / 4 |
| **Aaron Gordon** | DEN | Lower Body | 09 Nov | 0 | 25.6 | 21.7 (3) | 23.0 (7) | 25.6 (8) | 28.9 | 31.0 | Free agent | 47% | 3 / 4 |
| **Scotty Pippen Jr.** | MEM | Back Soreness | 11 Nov | 2 | 14.2 | — | 8.3 (3) | 14.2 (5) | 30.6 | 27.1 | Free agent | 10% | 4 / 4 |
| **Christian Braun** | DEN | Left Calf Bruise | 09 Nov | 0 | 30.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | 23.1 | 26.3 | Waivers | 39% | 3 / 4 |
| **Tobias Harris** | SA | Left Calf Strain | 11 Nov | 2 | — | — | — | — | 30.1 | 28.0 | Free agent | 44% | 4 / 3 |
| **Egor Demin** | BKN | Right Leg Bruise | 11 Nov | 2 | 15.0 | — | 18.0 (3) | 15.0 (4) | 30.0 | 22.2 | Free agent | 29% | 2 / 3 |
| **Jaylon Tyson** | CLE | Right Ankle Sprain | 11 Nov | 2 | 18.6 | — | 18.8 (4) | 18.6 (5) | 25.6 | 28.3 | Free agent | 2% | 4 / 3 |
| **Devin Vassell** | SA | Left Groin | 09 Nov | 0 | 28.3 | 28.2 (4) | 31.6 (8) | 28.3 (10) | 26.8 | 27.3 | Free agent | 41% | 4 / 3 |
| **Robert Williams III** | POR | Rest | 10 Nov | 1 | 28.1 | 30.3 (3) | 30.2 (5) | 28.1 (7) | 26.9 | 26.6 | Free agent | 5% | 3 / 4 |
| **Quentin Grimes** | LAL | Finger | 09 Nov | 0 | 16.6 | 12.6 (5) | 13.4 (9) | 16.6 (11) | 28.1 | 25.8 | Free agent | 30% | 3 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 1 | — | — | — | — | — | 28.1 | Free agent | 2% | 3 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 3 | — | — | — | — | 27.4 | 21.3 | Free agent | 5% | 4 / 3 |
| **Isaiah Jackson** | LAC | Left Groin Soreness | 10 Nov | 1 | 26.8 | 20.3 (3) | 26.0 (6) | 26.8 (8) | 20.6 | 20.9 | Free agent | 6% | 3 / 3 |
| **Cameron Johnson** | DEN | Lower Body | 09 Nov | 0 | 22.0 | 24.0 (3) | 24.8 (4) | 22.0 (5) → 24.8 (4) | 26.1 | 25.9 | Free agent | 9% | 3 / 4 |
| **Jock Landale** | ATL | Left Hip | 09 Nov | 0 | 16.4 | — | 12.0 (5) → 15.0 (4) | 16.4 (7) → 19.2 (6) | — | 25.8 | Free agent | 0% | 3 / 3 |
| **T.J. McConnell** | IND | Right Hamstring Strain | 09 Nov | 0 | 13.0 | 13.0 (1) | 13.0 (1) | 13.0 (1) | 24.4 | 25.5 | Free agent | 8% | 4 / 3 |
| **Isaiah Stewart** | MEM | Right Knee Bruise | 11 Nov | 2 | 22.9 | 21.5 (2) | 25.5 (6) | 22.9 (7) | 25.3 | 25.1 | Free agent | 4% | 4 / 4 |

### Notes

- **Yves Missi (NO):** see the shortlist. Out Sunday at LAC, his eighth straight miss [Yahoo, 8 Nov](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-los-205416257.html); week-to-week, no timetable reported [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773); *ESPN est.* 9 Nov; news-watch floor 12 Nov. Small sample.
- **Desmond Bane (ORL):** see the pickup notes [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/).
- **Jusuf Nurkic (UTAH):** partial plantar plate tear; began on-court work 6 Nov and is re-evaluated in two weeks, about 20 Nov; nothing newer found [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html). *ESPN est.* 20 Nov. No games this season; rate 36.7 is last season's. A re-evaluation is not a return.
- **Norman Powell (CHI):** see the shortlist [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-out-sunday-538162); no timetable reported; *ESPN est.* 11 Nov.
- **Jalen Suggs (ORL):** mild right knee bone bruise, re-evaluated two weeks from 26 Oct, about 9 Nov [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html); out 7 Nov [SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm); no result reported yet. *ESPN est.* 10 Nov. His L15 23.0 (1) is a small sample.
- **DeMar DeRozan (DEN):** back spasms, questionable Mon at HOU after missing Wednesday [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/). No timetable reported; *ESPN est.* 9 Nov. L7 16.0 (2) is a small sample.
- **Aaron Gordon and Cameron Johnson (DEN):** both questionable Mon at HOU for "lower body injury management" [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/aaron-gordon-lower-body-questionable-monday). No timetable reported; *ESPN est.* 9 Nov for both.
- **Scotty Pippen Jr. and Isaiah Stewart (MEM):** both listed day-to-day for Mon at TOR in Fox's preview [Fox Sports, Nov](https://www.foxsports.com/articles/nba/memphis-faces-toronto-looks-to-break-3game-slide), after a report that both would miss time [RealGM, Nov](https://basketball.realgm.com/wiretap/288056/Scotty-Pippen-Jr-Isaiah-Stewart-To-Miss-Time-For-Grizzlies). Pippen has a lumbar disc herniation; Stewart a right knee bone bruise that "avoided anything major" [Yahoo, 5 Nov](https://sports.yahoo.com/articles/grizzlies-isaiah-stewart-avoided-anything-001100081.html). No timetable reported; *ESPN est.* 11 Nov for both. Stewart's L7 21.5 (2) is a small sample.
- **Christian Braun (DEN):** see the pickup notes [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou).
- **Tobias Harris (SA):** left calf strain; still out Mon at PHX [Air Alamo, 8 Nov](https://airalamo.com/spurs-suns-injury-report-what-devin-vassell-s-questionable-tag-means-for-san-antonio). No timetable reported; *ESPN est.* 11 Nov; news-watch floor 14 Nov. No games this season; rate 28.0 is last season's.
- **Egor Demin (BKN):** right leg bone bruise, out Sunday at DAL, his sixth straight miss; re-evaluated this week, "progressing well" [Dallas Sports Journal, 8 Nov](https://dallassportsjournal.com/brooklyn-nets-egor-demin-mikel-brown-jr-out-vs-mavericks) [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/demin-leg-progressing-out-at-least-two-games). No timetable reported; *ESPN est.* 11 Nov.
- **Jaylon Tyson (CLE):** right ankle sprain, ruled out Mon at CHA, a sixth straight miss [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jaylon-tyson-ankle-ruled-out-monday-vs-hornets). No timetable reported; *ESPN est.* 11 Nov.
- **Devin Vassell (SA):** left adductor tightness, questionable Mon at PHX; Julian Champagnie would start if he sits [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/devin-vassell-groin-questionable-monday-vs-phx) [Air Alamo, 8 Nov](https://airalamo.com/spurs-suns-injury-report-what-devin-vassell-s-questionable-tag-means-for-san-antonio). No timetable reported; *ESPN est.* 9 Nov. Rate 29.1.
- **Robert Williams III (POR):** not hurt; ESPN's "rest" is his 7 Nov night off on a back-to-back [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs). *ESPN est.* 10 Nov. Rate 29.3.
- **Quentin Grimes (LAL):** started Sunday at DET (12 points in 31 minutes), left in the fourth with a right-hand finger injury; X-rays negative; questionable at best Mon vs ATL [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/lakers-quentin-grimes-doesnt-return-sunday/). No timetable reported; *ESPN est.* 9 Nov.
- **Maxime Raynaud (SAC):** right patellar subluxation; re-evaluation "next week" (9–15 Nov), no result yet [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap). *ESPN est.* 10 Nov, probably early.
- **Dereck Lively II (DAL):** right foot surgery; Dusty May sees "major progress" but gives no timetable, and he is not practising [Dallas Sports Journal, Nov](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/) [The Smoking Cuban, Nov](https://thesmokingcuban.com/dereck-lively-ii-extended-absence-putting-his-mavericks-future-in-jeopardy). No timetable reported; *ESPN est.* 12 Nov, likely early.
- **Isaiah Jackson (LAC):** left groin soreness, out Sunday; travels for Tue 10 at PHX, and the team expects no extended absence [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday). No timetable reported; *ESPN est.* 10 Nov.
- **Jock Landale (ATL):** left hip strain, four straight missed; questionable Mon vs LAL [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-iffy-for-monday-538185) [Yahoo, 8 Nov](https://sports.yahoo.com/articles/jock-landale-questionable-vs-lakers-221750590.html). No timetable reported; *ESPN est.* 9 Nov.
- **T.J. McConnell (IND):** right hamstring strain; 9 minutes in his 7 Nov debut on an apparent restriction, questionable Mon [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-strikes-for-six-points-in-season-debut/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/t-j-mcconnell-hamstring-questionable-monday). No timetable reported; *ESPN est.* 9 Nov. His 13.0 (1) is a small sample.

## Yet to play this season

Injured players with no game yet this season, worth 25+ FP/g on ESPN's projection or last season, by expected return. None has played this season, so none has an L7, L15 or L30. Their value is last season and the projection. Our five-lowest floor is 33.5.

| Player | NBA | Injury | ESPN est. | Days | Projected FP/g (min) | 2026 FP/g (GP) | League | Owned | Games |
|---|---|---|---|---:|---:|---:|---|---:|---|
| **Brandon Ingram** | LAC | Right Achilles Surgery | 10 Nov | 1 | 38.5 (35.3) | 36.5 (77) | Melbourne poopoo | 66% | 3 / 3 |
| **Maxime Raynaud** | SAC | Right Knee Dislocated | 10 Nov | 1 | — (—) | 28.1 (74) | Free agent | 2% | 3 / 3 |
| **Tobias Harris** | SA | Left Calf Strain | 11 Nov | 2 | 30.1 (30.5) | 28.0 (63) | Free agent | 44% | 4 / 3 |
| **Dereck Lively II** | DAL | Right Foot Surgery | 12 Nov | 3 | 27.4 (23.6) | 21.3 (7) | Free agent | 5% | 4 / 3 |
| **Jusuf Nurkic** | UTAH | Right Foot Strain | 20 Nov | 11 | 27.6 (23.1) | 36.7 (41) | Free agent | 7% | 4 / 4 |
| **Bradley Beal** | LAC | Right Knee Inflammation | 29 Nov | 20 | 25.6 (25.3) | 10.5 (6) | Free agent | 2% | 3 / 3 |
| **Jimmy Butler III** | GS | Right Knee Surgery | 02 Jan | 54 | 38.8 (32.4) | 41.6 (38) | Free agent | 29% | 3 / 4 |
| **Kristaps Porzingis** | GS | Illness | 02 Jan | 54 | 36.9 (27.7) | 32.3 (32) | Free agent | 36% | 3 / 4 |
| **Mark Williams** | PHX | Left Shoulder Surgery | 03 Feb | 86 | 31.0 (24.9) | 31.9 (60) | Free agent | 6% | 4 / 3 |
| **Shaedon Sharpe** | POR | Right Knee Surgery | 02 Mar | 113 | 24.8 (25.4) | 31.2 (50) | Free agent | 7% | 3 / 4 |
| **Donte DiVincenzo** | MIN | Right Achilles Surgery | 02 Apr | 144 | 23.0 (24.1) | 29.4 (82) | Free agent | 2% | 2 / 4 |

### Notes

- **Brandon Ingram (Melbourne poopoo; also out behind the LAC pickups):** right heel surgery and a partial Achilles tear; back in 5-on-5 work, with no defined timetable [RealGM, 7 Nov](https://basketball.realgm.com/wiretap/288060/Brandon-Ingram-Ramping-Up-Towards-Clippers-Debut) [Heavy, Nov](https://heavy.com/sports/nba/los-angeles-clippers/brandon-ingram-practice-achilles-return-soon/). *ESPN est.* 10 Nov.
- **Maxime Raynaud, Tobias Harris, Dereck Lively II and Jusuf Nurkic:** see *Injured and available, back soon* [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap) [Air Alamo, 8 Nov](https://airalamo.com/spurs-suns-injury-report-what-devin-vassell-s-questionable-tag-means-for-san-antonio) [Dallas Sports Journal, Nov](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/) [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html).
- **Bradley Beal (LAC):** right knee injury management; has not played; no timetable reported [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 29 Nov.
- **Jimmy Butler III (GS):** torn right ACL, back around the one-year mark, about Jan–Feb 2027 (unchanged since 8 Nov) [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/). *ESPN est.* 2 Jan.
- **Kristaps Porzingis (GS):** stepping away from basketball for his health (6 Nov); no timetable reported (unchanged since 8 Nov) [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball). *ESPN est.* 2 Jan. Not a stash.
- **Mark Williams (PHX):** torn left labrum, repaired 10 Sep, at least five months, so about mid-Feb (unchanged since 8 Nov) [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery) [SI](https://www.si.com/nba/suns/onsi/insider-reveals-when-phoenix-suns-center-mark-williams-should-return-from-injury). *ESPN est.* 3 Feb.
- **Shaedon Sharpe (POR):** right meniscus surgery, re-evaluation about late Feb (unchanged since 2 Nov) [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next). *ESPN est.* 2 Mar.
- **Donte DiVincenzo (MIN):** torn right Achilles, targeting a late-season return (unchanged since 2 Nov) [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214). *ESPN est.* 2 Apr.

## Our injured players

- **Jamal Murray** (DEN): Day-To-Day, Left Lower Leg Bruise; ESPN est. back 09 Nov.
- **Jalen Duren** (DET): Out, Right Hamstring Strain; ESPN est. back 24 Nov.
- **Scottie Barnes** (TOR): Day-To-Day, Left Groin Soreness; ESPN est. back 09 Nov.
- **Kawhi Leonard** (TOR): Out, Left Knee Inflammation; ESPN est. back 23 Nov.

### Notes

- **Jamal Murray:** questionable Mon at HOU with a left shin (tibia) contusion; all five Denver starters are questionable [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets) [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/jamal-murray-injury-questionable-against-houston-538199) [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/). No timetable reported; *ESPN est.* 9 Nov.
  - Form (`form.py`): season 46.1 (8) → 51.7 (7), L7 43.7 (3), L15 51.7 (7), L30 46.1 (8) → 51.7 (7), projected 43.9, rate 48.8. L7 is within 5 of the season.
- **Jalen Duren (IR):** cleared for on-court work 8 Nov, re-evaluated in two weeks (about 22 Nov) and inactive until then [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work). Detroit's first game after that is Tue 24 Nov at ORL. No return date reported; *ESPN est.* 24 Nov. Nothing newer found.
  - Form (`form.py`): season 33.5 (2) → 44.0 (1), L7 —, L15 —, L30 33.5 (2) → 44.0 (1), projected 42.2, rate 44.1. All of it a **small sample**.
- **Scottie Barnes:** limited in Sunday's practice, questionable Mon vs MEM with left adductor soreness [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/) [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/scottie-barnes-immanuel-quickley-to-return-against-grizzlies/92678359007/). If he sits, his next chance is Wed 11 vs BOS [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html). No timetable reported; *ESPN est.* 9 Nov.
  - Form (`form.py`): season 45.9 (8) → 50.7 (7), L7 44.3 (3), L15 45.2 (6) → 51.8 (5), L30 45.9 (8) → 50.7 (7), projected 43.7, rate 48.6. L7 is within 5 of the plain season.
- **Kawhi Leonard (bench):** Rajaković on 8 Nov: "He's still not participating in the team activities and on the court," though his body "reacted well to the treatment"; he is likely to miss at least all four games this week [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html). The team's next update was due about 10 Nov [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process). No return date reported; *ESPN est.* 23 Nov.
  - Form (`form.py`): season 40.0 (2), L7 —, L15 —, L30 40.0 (2), projected 45.8, rate 41.7. A **small sample**.
- **The IR slot: keep Duren there.** Neither he nor Kawhi plays this week. Duren is ruled inactive to about 22 Nov with a first possible game on 24 Nov [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/). Kawhi's return-to-play has no date but could end sooner, and from the bench he can be activated without a move [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html). Kawhi is in both of our pending offers (for Jalen Brunson, expiring 10 Nov 02:55 UTC; for Josh Giddey, expiring 11 Nov 00:38 UTC; today's `council/slump_watch.py` run). If either is accepted, Duren keeps the slot anyway.

## Who takes the minutes, team by team

### OKC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Williams | Left Leg Fracture | 02 Mar | 32.8 | 26.3 | Free agent |
| Chet Holmgren | Right Knee | 02 Jan | 30.0 | 40.0 | Free agent |
| Cason Wallace | Left Shoulder Surgery | 02 Mar | 26.6 | 18.7 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ajay Mitchell | PG/SG | 7 | 28.3 | +3.6 | 7 | **36.6** | 29.7 | 34.0 (4) | 37.6 (8) | 34.5 (10) | Lauri Birds | 72% |
| Aday Mara | C | 7 | 22.7 | +9.7 | 2 | **29.9** | 11.7 | 31.8 (4) | 27.0 (8) | 24.4 (10) | Waivers | 18% |
| Jared McCain | PG/SG | 7 | 27.3 | +7.0 | 4 | **24.6** | 12.3 | 28.0 (4) | 21.8 (8) | 20.9 (10) | Free agent | 30% |
| Bennett Stirtz | PG | 7 | 23.7 | +19.0 | 0 | **19.7** | 2.0 | 25.2 (4) | 18.1 (8) | 14.4 (10) | Free agent | 1% |
| Kenrich Williams | SF | 7 | 23.4 | +16.8 | 7 | **18.3** | 7.0 | 19.5 (4) | 16.8 (8) | 14.9 (10) | Free agent | 1% |

**Reported timeline:**

- **Chet Holmgren:** small right patellar tendon tear, treated 30 Oct, out 8–10 weeks, so about 25 Dec–8 Jan; no newer update found [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear) [AP via ClickOnDetroit, 31 Oct](https://www.clickondetroit.com/sports/2026/10/31/chet-holmgren-out-at-least-2-months-with-knee-injury-and-cason-wallace-has-shoulder-surgery/). *ESPN est.* 2 Jan.
- **Jalen Williams** (fractured left fibula, surgery 28 Oct) and **Cason Wallace** (left shoulder surgery): both re-evaluated before the end of the regular season (unchanged since 2 Nov) [Yahoo, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html) [AP via ClickOnDetroit, 31 Oct](https://www.clickondetroit.com/sports/2026/10/31/chet-holmgren-out-at-least-2-months-with-knee-injury-and-cason-wallace-has-shoulder-surgery/). *ESPN est.* 2 Mar for both.
- **Jaylin Williams** (not in the table): back spasms, three straight missed, next chance Tue 10 at POR; no timetable reported; *ESPN est.* 10 Nov [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/). His return decides Mara's starts.

### GS

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jimmy Butler III | Right Knee Surgery | 02 Jan | 32.4 | 41.6 | Free agent |
| Kristaps Porzingis | Illness | 02 Jan | 27.7 | 32.3 | Free agent |
| Moses Moody | Left Knee Surgery | 01 Dec | 25.7 | 24.8 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Yaxel Lendeborg | SF/PF | 10 | 32.2 | +3.6 | 10 | **40.7** | 33.7 | 47.5 (4) | 42.0 (8) → 48.3 (7) | 40.7 (10) → 45.4 (9) | **us** | 94% |
| Brandin Podziemski | PG/SG | 8 | 34.0 | +3.1 | 8 | **35.9** | 30.8 | 35.0 (4) | 36.1 (7) | 35.9 (8) | Matt Wright's Foxies | 76% |
| Brandon Williams | PG/SG | 9 | 17.8 | — | 1 | **20.3** | — | 24.3 (3) | 21.1 (7) | 20.3 (9) | Free agent | 2% |
| Georges Niang | PF | 10 | 20.6 | — | 2 | **16.9** | — | 19.8 (4) | 17.9 (8) | 16.9 (10) | Free agent | 1% |
| Will Richard (out, ESPN est. back 11 Nov) | SG/SF | 10 | 17.1 | — | 3 | **12.5** | — | 13.0 (4) | 12.0 (8) | 12.4 (10) | Free agent | 0% |

**Reported timeline:**

- (No pickup here; Yaxel Lendeborg is ours. Not re-checked since 8 Nov.)
- **Jimmy Butler III:** torn right ACL, back around the one-year mark, about Jan–Feb 2027 [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/). *ESPN est.* 2 Jan.
- **Kristaps Porzingis:** stepping away for his health (6 Nov); no timetable reported [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball). *ESPN est.* 2 Jan.
- **Moses Moody:** left patellar tendon surgery in March; hoped back in December or January, no official timetable [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/). *ESPN est.* 1 Dec.

### POR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ja Morant | Left Hamstring | 01 Dec | 29.5 | 33.8 | Free agent |
| Shaedon Sharpe | Right Knee Surgery | 02 Mar | 29.4 | 31.2 | Free agent |
| Vit Krejci | Left Ankle | 02 Jan | 25.7 | 7.0 | Free agent |

Last 9 games: 2 game(s) without them, 7 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Micah Potter | C | 1 | 14.0 | +7.2 | 0 | **22.0** | 3.2 | 14.0 (2) | 7.2 (4) | 7.0 (5) | Free agent | 0% |
| Chris Youngblood | SG | 2 | 20.5 | +11.8 | 0 | **18.0** | 4.3 | 11.8 (4) | 9.8 (5) | 9.8 (5) | Free agent | 0% |
| Yang Hansen | C | 2 | 14.5 | +6.5 | 0 | **14.0** | 8.2 | 8.7 (3) | 11.0 (5) | 10.2 (6) | Free agent | 0% |
| 4703889 |  | 1 | 12.0 | +5.0 | 0 | **12.0** | -2.0 | — | — | — | — | 0% |
| Branden Carlson | C | 1 | 12.0 | +5.7 | 0 | **7.0** | 5.3 | 5.0 (2) | 5.8 (4) | 5.8 (4) | Free agent | 0% |

**Reported timeline:**

- (No pickup or player of ours here; not re-checked since 8 Nov.)
- **Ja Morant:** Grade 2 left hamstring strain, re-evaluation four weeks from 30 Oct, about 27 Nov [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain). *ESPN est.* 1 Dec.
- **Shaedon Sharpe:** right meniscus surgery, re-evaluation about late Feb [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next). *ESPN est.* 2 Mar.
- **Vit Krejci:** hurt 5 Nov vs PHX (ankle, or a lower-left-leg fracture by another report); no timetable reported [ClutchPoints, 5 Nov](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-portland-loses-guard-to-painful-injury-in-win-vs-suns). *ESPN est.* 2 Jan.

### MIN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Anthony Edwards | Right Knee Surgery | 21 Dec | 35.8 | 52.5 | Melbourne poopoo |
| Donte DiVincenzo | Right Achilles Surgery | 02 Apr | 30.5 | 29.4 | Free agent |

Last 10 games: 7 game(s) without them, 3 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Ayo Dosunmu | PG/SG | 7 | 34.3 | +9.0 | 7 | **43.9** | 25.0 | 43.5 (4) | 36.6 (9) | 37.3 (11) | Cream Abdul-Yammar | 80% |
| LaMelo Ball | PG | 7 | 29.4 | +5.8 | 7 | **37.4** | 27.0 | 42.2 (4) | 34.9 (9) | 35.0 (11) | Cream Abdul-Yammar | 100% |
| Bones Hyland | PG | 7 | 14.7 | +5.4 | 0 | **24.1** | 10.3 | 22.0 (4) | 21.6 (9) | 18.6 (11) | Free agent | 3% |
| Trey Lyles | PF | 7 | 21.0 | +6.3 | 0 | **18.6** | 14.7 | 23.0 (4) | 17.0 (9) | 15.8 (11) | Free agent | 0% |
| Jaylen Clark | SG | 7 | 18.6 | +14.6 | 0 | **15.1** | 5.5 | 14.5 (4) | 14.1 (8) | 11.8 (10) | Free agent | 0% |

**Reported timeline:**

- (No pickup or player of ours here; not re-checked since 8 Nov.)
- **Anthony Edwards (Melbourne poopoo):** right knee arthroscopic debridement 29 Oct, up to two months [Yahoo (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html). *ESPN est.* 21 Dec.
- **Donte DiVincenzo:** torn right Achilles, targeting a late-season return [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214). *ESPN est.* 2 Apr.

### CHA

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kon Knueppel | Left Hamstring Strain | 12 Dec | 34.2 | -2.0 | Free agent |
| Dennis Schroder | Left Hamstring Strain | 25 Nov | 30.0 | 19.1 | Free agent |

Last 10 games: 1 game(s) without them, 9 with them.

Also out in those games, so part of the gain is theirs: Grant Williams (right hamstring; ESPN est. 12 Nov), Moussa Diabate (right quadriceps; ESPN est. 09 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Hannes Steinbach | PF | 1 | 27.0 | +19.3 | 0 | **31.0** | 4.7 | 16.5 (2) | 10.7 (3) | 11.2 (4) | Free agent | 1% |
| Royce O'Neale | SF/PF | 1 | 26.0 | +8.0 | 0 | **24.0** | 10.8 | 12.3 (3) | 10.9 (8) | 12.1 (10) | Free agent | 1% |
| Tidjane Salaun | PF | 1 | 23.0 | +9.1 | 0 | **13.0** | 13.4 | 14.3 (3) | 11.4 (8) | 13.3 (9) | Free agent | 0% |
| Liam McNeeley | SF | 1 | 19.0 | +12.2 | 0 | **13.0** | 0.5 | 6.5 (2) | 5.3 (3) | 3.0 (5) | Free agent | 0% |
| Ryan Kalkbrenner | C | 1 | 21.0 | +4.2 | 1 | **8.0** | 19.6 | 14.3 (3) | 16.5 (8) | 18.4 (10) | Free agent | 2% |

**Reported timeline:**

- **Kon Knueppel:** left hamstring strain, re-aggravated in his 4 Nov debut; on 8 Nov the Hornets said he will be re-evaluated in four weeks, so about 6 Dec, and Basketnews has him out until December [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html) [ESPN, 8 Nov](https://espn.com/nba/story/_/id/50425681/kon-knueppel-least-four-weeks-hamstring-strain) [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/) [Basketnews, 8 Nov](https://basketnews.com/news-259083-kon-knueppel-injury-hornets-announce-new-devastating-update-and-recovery-timeline.html). *ESPN est.* 12 Dec. The news-watch override (back 13 Nov) is now out of date.
- **Dennis Schroder:** left hamstring strain from the 4 Nov game at BKN, re-evaluated in two weeks, so about 22 Nov [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html) [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/dennis-schroeder-will-miss-at-least-two-weeks/92682400007/). *ESPN est.* 25 Nov.
- **Also out, Grant Williams:** right hamstring strain, out Mon vs CLE; no timetable reported; *ESPN est.* 12 Nov [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-injury-latest-brandon-miller-011009724.html) [Sports Mole, 8 Nov](https://www.sportsmole.co.uk/basketball/cleveland-cavaliers/preview/cleveland-cavaliers-vs-charlotte-hornets-player-props-injury-report-and-prediction--nba_608728.html).
- **Also out, Moussa Diabaté (Team Nic Kerr):** right quadriceps tendinopathy, questionable Mon vs CLE; no timetable reported; *ESPN est.* 9 Nov [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-injury-latest-brandon-miller-011009724.html) [Sports Mole, 8 Nov](https://www.sportsmole.co.uk/basketball/cleveland-cavaliers/preview/cleveland-cavaliers-vs-charlotte-hornets-player-props-injury-report-and-prediction--nba_608728.html). His return would cut Steinbach's minutes (inference).
- **Brandon Miller (Matt Wright's Foxies; not in the table):** right hip strain, out Mon and possibly a few games; no timetable reported; *ESPN est.* 12 Nov [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/and-lastly-brandon-miller-has-been-diagnosed-with-a/92682399007/) [RotoBaller, 8 Nov](https://www.rotoballer.com/player-news/brandon-miller-sidelined-monday-versus-cavaliers/1987955). RotoBaller names Tidjane Salaun and Sion James for the wing minutes.
- **Who gains:** Coby White, Sion James and Grayson Allen, per Basketnews [Basketnews, 8 Nov](https://basketnews.com/news-259083-kon-knueppel-injury-hornets-announce-new-devastating-update-and-recovery-timeline.html). None of the three is in the table.

### UTAH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jaren Jackson Jr. | Right Knee | 14 Dec | 31.4 | 27.0 | Matt Wright's Foxies |
| Jusuf Nurkic | Right Foot Strain | 20 Nov | 26.4 | 36.7 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Lauri Markkanen (out, ESPN est. back 10 Nov) | SF/PF | 4 | 33.2 | +4.8 | 4 | **39.5** | 25.5 | 44.0 (3) | 33.2 (6) → 39.8 (5) | 32.5 (8) → 37.1 (7) | Lauri Birds | 89% |
| Ace Bailey | SF/PF | 6 | 32.8 | +5.6 | 6 | **22.5** | 38.8 | 19.5 (4) | 30.2 (8) | 29.0 (10) | Dr White Slong | 59% |
| Josh Okogie | SF | 6 | 21.3 | +8.3 | 0 | **13.3** | 3.3 | 14.2 (4) | 11.4 (8) | 10.1 (9) | Free agent | 0% |
| Josh Green | SG | 6 | 19.3 | +5.3 | 2 | **8.7** | 7.5 | 9.0 (4) | 8.4 (8) | 8.4 (8) | Free agent | 0% |

**Reported timeline:**

- **Jaren Jackson Jr. (Matt Wright's Foxies):** torn right MCL (26 Oct), at least six weeks, about 7–21 Dec (unchanged since 2 Nov) [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/). *ESPN est.* 14 Dec.
- **Jusuf Nurkic:** began on-court work; re-evaluated two weeks from 6 Nov, about 20 Nov [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html). *ESPN est.* 20 Nov.
- **Lauri Markkanen (Lauri Birds, our opponent this week):** right wrist sprain, questionable on the Jazz's 8 Nov report and now listed out; no timetable reported; *ESPN est.* 10 Nov [Jazz on X, 8 Nov](https://x.com/utahjazz/status/2119463702122434874).

### LAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Bradley Beal | Right Knee Inflammation | 29 Nov | 25.3 | 10.5 | Free agent |
| Jordan Miller | Left Shoulder Surgery | 02 Mar | 22.0 | 20.4 | Free agent |

Last 9 games: 9 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Brandon Ingram (right achilles surgery; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kris Dunn | PG/SG | 9 | 29.8 | +7.8 | 9 | **33.4** | 20.0 | 34.0 (4) | 32.9 (7) | 33.2 (9) | Lauri Birds | 41% |
| Derrick Jones Jr. | SF/PF | 8 | 29.9 | +4.5 | 8 | **27.8** | 21.1 | 22.7 (3) | 26.3 (6) | 27.8 (8) | Free agent | 12% |
| Kobe Sanders | SG | 9 | 24.1 | — | 2 | **19.6** | — | 20.2 (4) → 27.3 (3) | 20.3 (7) → 23.8 (6) | 19.6 (9) → 22.1 (8) | Free agent | 1% |

**Reported timeline:**

- **Jordan Miller:** torn left rotator cuff, repaired 26 Aug, re-evaluation about late Feb (unchanged since 8 Nov) [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html). *ESPN est.* 2 Mar.
- **Bradley Beal:** right knee injury management; has not played; no timetable reported [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans). *ESPN est.* 29 Nov.
- **Brandon Ingram (also out; Melbourne poopoo):** right heel surgery and partial Achilles tear; in 5-on-5 work with no defined timetable [RealGM, 7 Nov](https://basketball.realgm.com/wiretap/288060/Brandon-Ingram-Ramping-Up-Towards-Clippers-Debut) [Heavy, Nov](https://heavy.com/sports/nba/los-angeles-clippers/brandon-ingram-practice-achilles-return-soon/) [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-returns-from-g-league-assignment-537174). *ESPN est.* 10 Nov. His debut would cut Jones Jr.'s and Hachimura's minutes (inference).
- **Isaiah Jackson** (not in the table): see *Injured and available, back soon* [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday).

### WSH

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jamir Watkins | Left Knee Surgery | 02 Apr | 20.6 | 19.4 | Free agent |
| Justin Champagnie | Right Foot | 25 Feb | 20.0 | 25.0 | Free agent |

Last 10 games: 6 game(s) without them, 4 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Kyshawn George | SG/SF | 6 | 35.2 | +5.2 | 6 | **43.2** | 29.8 | 49.5 (4) | 41.5 (8) | 37.2 (10) → 40.4 (9) | Snow Time Lakers | 69% |

**Reported timeline:**

- (No pickup or player of ours here; not re-checked since 8 Nov.)
- **Jamir Watkins:** torn left ACL in July, likely out for the season [RotoWire, Jul](https://www.rotowire.com/basketball/headlines/jamir-watkins-injury-undergoes-surgery-for-torn-acl-532251). *ESPN est.* 2 Apr.
- **Justin Champagnie:** right foot fracture, surgery 28 Oct, hoping for a return by the All-Star break [NBA.com, 28 Oct](https://www.nba.com/news/washington-wizards-justin-champagnie-foot-surgery). *ESPN est.* 25 Feb.

### IND

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Sheppard | Left Knee | 02 Jan | 21.4 | 5.0 | Free agent |
| Johnny Furphy | Right Knee Surgery | 02 Jan | 18.3 | 14.2 | Free agent |

Last 10 games: 9 game(s) without them, 1 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Quenton Jackson | PG/SG | 9 | 22.0 | +6.0 | 1 | **23.0** | 26.0 | 27.2 (4) | 23.6 (8) | 23.3 (10) | Free agent | 5% |
| Jarace Walker | SF/PF | 9 | 24.1 | +5.1 | 2 | **20.6** | 6.0 | 22.2 (4) | 23.4 (8) | 19.1 (10) | Free agent | 1% |
| Jay Huff | C | 9 | 18.3 | — | 5 | **15.9** | — | 14.5 (4) | 17.8 (8) | 15.9 (9) | Free agent | 1% |
| Larry Nance Jr. | PF | 8 | 17.0 | +12.0 | 0 | **15.1** | -1.0 | 16.3 (3) | 17.3 (7) | 13.3 (9) | Free agent | 0% |
| Jalen Slawson | SF | 9 | 14.9 | — | 1 | **14.2** | — | 18.2 (4) | 12.4 (8) | 14.2 (9) | Free agent | 0% |

**Reported timeline:**

- **Johnny Furphy:** torn right ACL (Feb 2026), targeting "the middle of the season", no date (unchanged since 5 Nov) [Roundtable, 25 Sep](https://roundtable.io/sports/nba/pacers/news/pacers-give-johnny-furphy-acl-rehab-update-before-camp). *ESPN est.* 2 Jan.
- **Ben Sheppard:** full left meniscus repair 28 Oct; Carlisle: months, "I don't know how many" (unchanged since 8 Nov) [Forbes, 6 Nov](https://www.forbes.com/sites/tonyeast/2026/11/06/ben-sheppard-longer-absence-is-bad-news-for-indiana-pacers/). No timetable reported; *ESPN est.* 2 Jan.
- **Guards behind the pickups:** T.J. McConnell debuted 7 Nov on a minutes limit and is questionable Monday [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-strikes-for-six-points-in-season-debut/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/t-j-mcconnell-hamstring-questionable-monday) (*ESPN est.* 9 Nov); Tyrese Haliburton (Lauri Birds) has no timetable reported [Roundtable, Nov](https://roundtable.io/sports/nba/pacers/news/pacers-still-have-no-timeline-for-tyrese-haliburton-s-return) (*ESPN est.* 13 Nov).

### ORL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Paolo Banchero | Right Ankle Sprain | 22 Nov | 35.2 | 47.0 | Dr White Slong |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Franz Wagner | SF/PF | 7 | 38.0 | +7.0 | 7 | **44.7** | 30.0 | 48.5 (4) | 44.7 (7) | 41.4 (9) | Cream Abdul-Yammar | 91% |
| Desmond Bane (day to day, ESPN est. back 10 Nov) | SG/SF | 6 | 36.0 | +6.0 | 6 | **32.7** | 13.0 | 28.0 (3) | 32.7 (6) | 27.8 (8) → 31.9 (7) | Free agent | 90% |
| Wendell Carter Jr. | C | 7 | 34.4 | +4.4 | 7 | **32.0** | 46.5 | 35.2 (4) | 32.0 (7) | 35.2 (9) | Dr White Slong | 55% |
| Jamal Cain | SF | 7 | 21.4 | +8.9 | 1 | **15.9** | -5.0 | 16.5 (4) | 15.9 (7) | 11.2 (9) | Free agent | 0% |
| Jase Richardson | SG | 7 | 25.0 | +11.0 | 7 | **15.4** | 14.5 | 15.8 (4) | 15.4 (7) | 15.2 (9) | Free agent | 1% |

**Reported timeline:**

- **Paolo Banchero (Dr White Slong):** low-grade right high-ankle sprain (23 Oct), 4–6 weeks from 24 Oct, so 21 Nov–5 Dec; he said "at least a month" [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html) [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182). Out 7 Nov at GSW [Roundtable, 7 Nov](https://roundtable.io/sports/nba/warriors/news/warriors-vs-magic-injury-report-draymond-green-paolo-banchero-statuses). *ESPN est.* 22 Nov.
- **Desmond Bane and Jalen Suggs:** see *Injured and available, back soon* [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/) [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html). Anthony Black (ours) had cramps on 7 Nov and no injury designation [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping).

### TOR

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Kawhi Leonard | Left Knee Inflammation | 23 Nov | 32.8 | 40.0 | **us** |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| RJ Barrett | SG/SF | 7 | 33.9 | +3.9 | 7 | **35.7** | 39.0 | 38.2 (4) | 35.7 (7) → 39.5 (6) | 36.4 (9) → 39.4 (8) | Dr White Slong | 82% |
| Immanuel Quickley (day to day, ESPN est. back 09 Nov) | PG/SG | 6 | 32.8 | +4.3 | 6 | **35.2** | 35.0 | 34.3 (3) | 35.2 (6) | 35.1 (8) → 37.7 (7) | Cream Abdul-Yammar | 77% |
| Jamal Shead | PG | 7 | 23.7 | +3.7 | 1 | **27.3** | 11.0 | 30.8 (4) | 27.3 (7) | 23.7 (9) | Lauri Birds | 4% |
| Ja'Kobe Walter | SG | 7 | 30.7 | +7.2 | 7 | **25.3** | 28.0 | 18.8 (4) | 25.3 (7) | 25.9 (9) | Free agent | 12% |
| Collin Murray-Boyles | PF | 7 | 23.1 | +4.1 | 3 | **24.0** | 25.0 | 29.2 (4) | 24.3 (7) | 24.4 (9) | Free agent | 12% |

**Reported timeline:**

- **Kawhi Leonard (ours):** not yet doing team or on-court work as of 8 Nov, likely out all four games this week [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html); update due about 10 Nov [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process). No return date reported; *ESPN est.* 23 Nov.
- **Short absences behind the gains:** Scottie Barnes (ours; adductor) and Immanuel Quickley (Cream Abdul-Yammar; hamstring) are questionable Mon vs MEM; no timetable reported; *ESPN est.* 9 Nov for both [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/) [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html). Murray-Boyles gains if Barnes sits [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html). Jamal Shead, a former pickup here, is now on Lauri Birds.

### DET

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Jalen Duren | Right Hamstring Strain | 24 Nov | 31.0 | 33.5 | **us** |

Last 9 games: 7 game(s) without them, 2 with them.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Duncan Robinson | SG/SF | 7 | 31.3 | +3.3 | 7 | **33.4** | 29.5 | 37.3 (3) | 33.4 (7) | 32.6 (9) | Team Nic Kerr | 59% |
| Paul Reed | PF/C | 7 | 28.0 | +6.5 | 7 | **31.4** | 33.5 | 27.0 (3) | 30.9 (7) | 31.4 (9) | Lauri Birds | 41% |
| Daniss Jenkins | PG | 7 | 26.6 | +8.1 | 1 | **26.0** | 21.0 | 24.7 (3) | 26.0 (7) | 24.9 (9) | Free agent | 4% |
| Kevin Huerter | SG/SF | 7 | 22.9 | +3.9 | 0 | **25.3** | 13.0 | 37.3 (3) | 25.1 (7) | 22.4 (9) | Free agent | 2% |
| Ronald Holland II | SF/PF | 7 | 16.4 | +3.9 | 0 | **16.9** | 16.0 | 11.0 (3) | 16.9 (7) | 16.7 (9) | Free agent | 1% |

**Reported timeline:**

- **Jalen Duren (ours, IR):** cleared for on-court work 8 Nov, re-evaluated in two weeks (about 22 Nov), inactive until then [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work). *ESPN est.* 24 Nov. Paul Reed (Lauri Birds) stays the starting center.
- **Isaiah Joe** (not in the table): right hip contusion, out Sunday, his sixth straight miss; no timetable reported; *ESPN est.* 9 Nov [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-joe-hip-remains-out-sunday-vs-lakers). His absence, not only Duren's, fed Huerter's and Jenkins's minutes [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-isaiah-joe-another-absence-coming/).

### PHX

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mark Williams | Left Shoulder Surgery | 03 Feb | 24.9 | 31.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jordan Goodwin (out, ESPN est. back 09 Nov) | PG/SG | 5 | 18.8 | — | 0 | **24.4** | — | 13.0 (1) | 27.2 (4) | 24.4 (5) | Free agent | 1% |

**Reported timeline:**

- **Mark Williams:** torn left labrum, repaired 10 Sep, at least five months, about mid-Feb (unchanged since 8 Nov) [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery). *ESPN est.* 3 Feb. Goodwin's guard minutes are not tied to him.
- **Jordan Goodwin:** questionable Mon vs SAS [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jordan-goodwin-calf-questionable-monday-vs-sas); see the pickup notes.

### PHI

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Dominick Barlow | Back Fracture | 18 Nov | 23.7 | 22.0 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Jaylen Brown | SG/SF | 9 | 36.0 | +3.6 | 9 | **41.0** | 38.6 | 50.0 (4) | 41.8 (8) | 41.4 (10) | Snow Time Lakers | 100% |
| Dean Wade | PF | 9 | 24.8 | +3.3 | 4 | **17.8** | 16.3 | 11.5 (4) | 17.8 (9) | 17.8 (9) | Free agent | 1% |
| Jabari Walker | PF | 6 | 12.2 | — | 0 | **14.0** | — | 13.3 (3) | 15.8 (5) | 12.3 (7) | Free agent | 0% |

**Reported timeline:**

- (No pickup or player of ours here; not re-checked since 8 Nov.)
- **Dominick Barlow:** lumbar bone stress response; on 4 Nov Nurse said at least 10–12 more days, about 14–16 Nov [Inquirer, 4 Nov](https://www.inquirer.com/sixers/dominick-barlow-injury-update-76ers-lebron-james-joel-embiid-20261104.html). *ESPN est.* 18 Nov.

### SAC

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Ben Simmons | Right Achilles Surgery | 01 Oct | 21.2 | — | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

Also out in those games, so part of the gain is theirs: Maxime Raynaud (right knee dislocated; ESPN est. 10 Nov).

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Darius Acuff Jr. | PG | 10 | 37.0 | +6.4 | 10 | **41.2** | 30.4 | 46.5 (4) | 45.9 (8) | 40.8 (10) → 44.3 (9) | Team Nic Kerr | 87% |
| Precious Achiuwa | PF/C | 10 | 27.6 | +3.3 | 8 | **29.0** | 24.1 | 25.5 (4) | 27.8 (8) → 31.3 (7) | 29.0 (10) → 31.9 (9) | Team Nic Kerr | 27% |
| Dylan Cardwell | C | 3 | 15.3 | — | 1 | **22.0** | — | 22.0 (3) | 22.0 (3) | 22.0 (3) | Free agent | 0% |
| Leaky Black | SF | 6 | 19.2 | — | 1 | **21.2** | — | 28.8 (4) | 21.2 (6) → 25.4 (5) | 21.2 (6) → 25.4 (5) | Free agent | 1% |
| De'Andre Hunter | SF/PF | 9 | 31.2 | +3.6 | 9 | **19.2** | 23.9 | 13.0 (3) | 21.4 (7) | 19.1 (9) | Free agent | 6% |

**Reported timeline:**

- **Ben Simmons:** torn right Achilles, out for the season (unchanged since 2 Nov) [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season). *ESPN est.* 1 Oct 2027.
- **Maxime Raynaud (also out):** re-evaluation in the week of 9 Nov, no result yet [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap). *ESPN est.* 10 Nov. His return takes backup-center minutes, not Leaky Black's wing minutes (inference).
- **De'Andre Hunter** returned from his illness Sunday and started, which sent Black back to the bench [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/kings-leaky-black-steady-in-fill-in-role/) [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/sac-acuff-lavine-hunter-achiuwa-cardwell).

### DEN

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Julian Strawther | Left Knee Sprain | 29 Nov | 16.0 | 12.9 | Free agent |

Last 8 games: 8 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Christian Braun (day to day, ESPN est. back 09 Nov) | SG/SF | 8 | 34.2 | +6.8 | 8 | **30.1** | 23.1 | 22.7 (3) | 32.3 (7) | 30.1 (8) | Waivers | 39% |
| Spencer Jones | SF/PF | 1 | 21.0 | — | 0 | **30.0** | — | 30.0 (1) | 30.0 (1) | 30.0 (1) | Free agent | 1% |
| Trevon Brazile | SF/PF | 8 | 21.1 | — | 1 | **20.5** | — | 18.0 (3) | 21.6 (7) | 20.5 (8) | Free agent | 3% |
| Bryce Hopkins | SF | 6 | 16.2 | — | 2 | **10.2** | — | 17.5 (2) | 11.8 (5) | 10.2 (6) | Free agent | 0% |

**Reported timeline:**

- **Julian Strawther:** left knee sprain (14 Oct preseason), re-evaluation six weeks later, about 29 Nov; nothing newer found [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html) [TSN, Oct](https://www.tsn.ca/nba/article/nuggets-strawther-out-with-knee-sprain-will-be-reevaluated-in-six-weeks-n1-50199062/). *ESPN est.* 29 Nov.
- **Monday at HOU:** Jamal Murray (ours; left shin contusion), Nikola Jokic (Lauri Birds; right elbow sprain), Christian Braun (calf contusion, illness), Aaron Gordon and Cameron Johnson (lower-body management) and DeMar DeRozan (back) are all questionable; no timetable reported; *ESPN est.* 9 Nov for each [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/) [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets) [Heavy, 8 Nov](https://heavy.com/sports/nba/denver-nuggets/nikola-jokic-elbow-injury-news-rockets/). Spencer Jones could start if Braun sits [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou).

### ATL

| Out | Injury | ESPN est. | Min left | Season FP/g | League |
|---|---|---|---:|---:|---|
| Mouhamed Gueye | Left Foot Fracture | 20 Nov | 15.4 | 15.3 | Free agent |

Last 10 games: 10 game(s) this season, all without them; compared with ESPN's projection.

| Replacement | Pos | Games | Min without | Δ min | Starts | FP/g without | Baseline FP/g | L7 | L15 | L30 | League | Owned |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Aaron Wiggins | SG/SF | 10 | 25.7 | +5.4 | 0 | **28.8** | 19.2 | 28.5 (4) | 28.2 (9) | 28.7 (11) | Free agent | 35% |
| Zuby Ejiofor | PF | 6 | 12.3 | — | 0 | **15.5** | — | 22.5 (4) | 18.0 (5) | 15.5 (6) | Free agent | 0% |
| Jock Landale (out, ESPN est. back 09 Nov) | C | 6 | 14.7 | — | 0 | **14.8** | — | — | 12.0 (5) → 15.0 (4) | 16.4 (7) → 19.2 (6) | Free agent | 0% |

**Reported timeline:**

- **Mouhamed Gueye:** left foot fracture, surgery 14 Jul, re-evaluation in three to four months; no result reported [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html) [Fox Sports](https://www.foxsports.com/nba/mouhamed-gueye-player). *ESPN est.* 20 Nov.
- **Jock Landale:** questionable Mon vs LAL; see *Injured and available, back soon* [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-iffy-for-monday-538185).

## Every injury

All 95 players in ESPN's injury feed, longest expected absence first.

| Player | NBA | Status | Injury | ESPN est. | Days | League |
|---|---|---|---|---|---:|---|
| Ben Simmons | SAC | Out | Right Achilles Surgery | 01 Oct | 326 | Free agent |
| Ariel Hukporti | PHI | Out | Right Achilles Surgery | 01 Oct | 326 | Free agent |
| Henri Veesaar | ATL | Out | Right Knee | 01 Jul | 234 | Free agent |
| Jamir Watkins | WSH | Out | Left Knee Surgery | 02 Apr | 144 | Free agent |
| Donte DiVincenzo | MIN | Out | Right Achilles Surgery | 02 Apr | 144 | Free agent |
| Shaedon Sharpe | POR | Out | Right Knee Surgery | 02 Mar | 113 | Free agent |
| Jordan Miller | LAC | Out | Left Shoulder Surgery | 02 Mar | 113 | Free agent |
| Jalen Williams | OKC | Out | Left Leg Fracture | 02 Mar | 113 | Free agent |
| Cason Wallace | OKC | Out | Left Shoulder Surgery | 02 Mar | 113 | Free agent |
| Justin Champagnie | WSH | Out | Right Foot | 25 Feb | 108 | Free agent |
| Mark Williams | PHX | Out | Left Shoulder Surgery | 03 Feb | 86 | Free agent |
| Vit Krejci | POR | Out | Left Ankle | 02 Jan | 54 | Free agent |
| Kristaps Porzingis | GS | Out | Illness | 02 Jan | 54 | Free agent |
| Johnny Furphy | IND | Out | Right Knee Surgery | 02 Jan | 54 | Free agent |
| Jimmy Butler III | GS | Out | Right Knee Surgery | 02 Jan | 54 | Free agent |
| Chet Holmgren | OKC | Out | Right Knee | 02 Jan | 54 | Free agent |
| Ben Sheppard | IND | Out | Left Knee | 02 Jan | 54 | Free agent |
| Anthony Edwards | MIN | Out | Right Knee Surgery | 21 Dec | 42 | Melbourne poopoo |
| Jaren Jackson Jr. | UTAH | Out | Right Knee | 14 Dec | 35 | Matt Wright's Foxies |
| Kon Knueppel | CHA | Out | Left Hamstring Strain | 12 Dec | 33 | Free agent |
| Reece Beekman | WSH | Out | Shoulder | 03 Dec | 24 | Free agent |
| Jayden Quaintance | SA | Out | Right Knee Surgery | 03 Dec | 24 | Free agent |
| Richie Saunders | MEM | Out | Right Knee Surgery | 01 Dec | 22 | Free agent |
| Moses Moody | GS | Out | Left Knee Surgery | 01 Dec | 22 | Free agent |
| Ja Morant | POR | Out | Left Hamstring | 01 Dec | 22 | Free agent |
| Julian Strawther | DEN | Out | Left Knee Sprain | 29 Nov | 20 | Free agent |
| Bradley Beal | LAC | Out | Right Knee Inflammation | 29 Nov | 20 | Free agent |
| Dennis Schroder | CHA | Out | Left Hamstring Strain | 25 Nov | 16 | Free agent |
| Jalen Duren | DET | Out | Right Hamstring Strain | 24 Nov | 15 | **us** |
| Kawhi Leonard | TOR | Out | Left Knee Inflammation | 23 Nov | 14 | **us** |
| Paolo Banchero | ORL | Out | Right Ankle Sprain | 22 Nov | 13 | Dr White Slong |
| Mouhamed Gueye | ATL | Out | Left Foot Fracture | 20 Nov | 11 | Free agent |
| Jusuf Nurkic | UTAH | Out | Right Foot Strain | 20 Nov | 11 | Free agent |
| Noah Penda | ORL | Out | Right Hamstring Strain | 18 Nov | 9 | Free agent |
| Izaiyah Nelson | ORL | Out | Left Ankle Surgery | 18 Nov | 9 | Free agent |
| Dominick Barlow | PHI | Out | Back Fracture | 18 Nov | 9 | Free agent |
| Tristan Vukcevic | WSH | Out | Left Hip Pinched Nerve | 16 Nov | 7 | Free agent |
| Nate Bittle | TOR | Out | Right Foot Fracture | 15 Nov | 6 | — |
| Tyrese Haliburton | IND | Out | Left Hamstring Strain | 13 Nov | 4 | Lauri Birds |
| Thomas Sorber | OKC | Out | Knee | 13 Nov | 4 | Free agent |
| Keshon Gilbert | ATL | Out | Left Knee Inflammation | 13 Nov | 4 | — |
| Asa Newell | ATL | Out | Left Toe | 13 Nov | 4 | Free agent |
| Tarik Biberovic | DAL | Out | Right Heel Inflammation | 12 Nov | 3 | Free agent |
| Sergio de Larrea | DAL | Out | Right Knee Strain | 12 Nov | 3 | Free agent |
| Grant Williams | CHA | Out | Right Hamstring | 12 Nov | 3 | Free agent |
| Dereck Lively II | DAL | Out | Right Foot Surgery | 12 Nov | 3 | Free agent |
| Brandon Miller | CHA | Out | Right Groin Soreness | 12 Nov | 3 | Matt Wright's Foxies |
| Zach Collins | CHI | Out | Illness | 11 Nov | 2 | Free agent |
| Will Richard | GS | Out | Left Thumb | 11 Nov | 2 | Free agent |
| Tobias Harris | SA | Out | Left Calf Strain | 11 Nov | 2 | Free agent |
| Steven Adams | HOU | Out | Right Calf Strain | 11 Nov | 2 | Free agent |
| Scotty Pippen Jr. | MEM | Out | Back Soreness | 11 Nov | 2 | Free agent |
| Sam Merrill | CLE | Out | Right Elbow | 11 Nov | 2 | Free agent |
| Norman Powell | CHI | Out | Right Shoulder Inflammation | 11 Nov | 2 | Free agent |
| Mikel Brown Jr. | BKN | Out | Rest | 11 Nov | 2 | Free agent |
| Jaylon Tyson | CLE | Out | Right Ankle Sprain | 11 Nov | 2 | Free agent |
| Isaiah Stewart | MEM | Out | Right Knee Bruise | 11 Nov | 2 | Free agent |
| Egor Demin | BKN | Out | Right Leg Bruise | 11 Nov | 2 | Free agent |
| Clint Capela | HOU | Out | Right Ankle Sprain | 11 Nov | 2 | Free agent |
| Yanic Konan Niederhauser | LAC | Out | Right Foot Surgery | 10 Nov | 1 | Free agent |
| Robert Williams III | POR | Day-To-Day | Rest | 10 Nov | 1 | Free agent |
| Maxime Raynaud | SAC | Out | Right Knee Dislocated | 10 Nov | 1 | Free agent |
| Lauri Markkanen | UTAH | Out | Right Wrist Sprain | 10 Nov | 1 | Lauri Birds |
| Keyonte George | UTAH | Day-To-Day | Right Ankle | 10 Nov | 1 | Cream Abdul-Yammar |
| Josh Hart | NY | Day-To-Day | Ankle | 10 Nov | 1 | Dr White Slong |
| Jonathan Isaac | ORL | Out | Left Knee | 10 Nov | 1 | Free agent |
| Jaylin Williams | OKC | Out | Back Spasms | 10 Nov | 1 | Free agent |
| Jalen Suggs | ORL | Out | Right Knee | 10 Nov | 1 | Free agent |
| Isaiah Jackson | LAC | Out | Left Groin Soreness | 10 Nov | 1 | Free agent |
| Grant Nelson | BKN | Day-To-Day | Left Knee | 10 Nov | 1 | — |
| Gary Trent Jr. | MIL | Out | Illness | 10 Nov | 1 | Free agent |
| Domantas Sabonis | SAC | Out | Left Knee Soreness | 10 Nov | 1 | Team Nic Kerr |
| Desmond Bane | ORL | Day-To-Day | Illness | 10 Nov | 1 | Free agent |
| Brandon Ingram | LAC | Out | Right Achilles Surgery | 10 Nov | 1 | Melbourne poopoo |
| Adem Bona | PHI | Out | Back Sprain | 10 Nov | 1 | Free agent |
| Yves Missi | NO | Out | Left Knee Bruise | 09 Nov | 0 | Free agent |
| T.J. McConnell | IND | Day-To-Day | Right Hamstring Strain | 09 Nov | 0 | Free agent |
| Scottie Barnes | TOR | Day-To-Day | Left Groin Soreness | 09 Nov | 0 | **us** |
| Quentin Grimes | LAL | Day-To-Day | Finger | 09 Nov | 0 | Free agent |
| Nikola Jokic | DEN | Day-To-Day | Right Elbow Sprain | 09 Nov | 0 | Lauri Birds |
| Moussa Diabate | CHA | Day-To-Day | Right Quadriceps | 09 Nov | 0 | Team Nic Kerr |
| Luka Doncic | LAL | Out | Back Soreness | 09 Nov | 0 | Team Nic Kerr |
| Jordan Goodwin | PHX | Out | Right Calf | 09 Nov | 0 | Free agent |
| Jock Landale | ATL | Out | Left Hip | 09 Nov | 0 | Free agent |
| Jarrett Allen | CLE | Day-To-Day | Right Knee | 09 Nov | 0 | Dr White Slong |
| Jamal Murray | DEN | Day-To-Day | Left Lower Leg Bruise | 09 Nov | 0 | **us** |
| Isaiah Joe | DET | Out | Right Hip Bruise | 09 Nov | 0 | Free agent |
| Immanuel Quickley | TOR | Day-To-Day | Right Hamstring | 09 Nov | 0 | Cream Abdul-Yammar |
| Gui Santos | GS | Day-To-Day | Left Knee Tendinitis | 09 Nov | 0 | Free agent |
| Devin Vassell | SA | Day-To-Day | Left Groin | 09 Nov | 0 | Free agent |
| DeMar DeRozan | DEN | Day-To-Day | Back Spasms | 09 Nov | 0 | Free agent |
| Christian Braun | DEN | Day-To-Day | Left Calf Bruise | 09 Nov | 0 | Waivers |
| Cameron Johnson | DEN | Day-To-Day | Lower Body | 09 Nov | 0 | Free agent |
| Anthony Davis | WSH | Day-To-Day | Right Ankle Sprain | 09 Nov | 0 | Melbourne poopoo |
| Aaron Gordon | DEN | Day-To-Day | Lower Body | 09 Nov | 0 | Free agent |

## Sources

- ESPN NBA injury feed and box scores (`site.api.espn.com`); ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`, `mRoster`, `proTeamSchedules_wl`), read 2026-11-09 06:46 UTC.
- Research for this run (web, 8–9 Nov 2026, US time; checked about 07:00 UTC 9 Nov), plus carry-over links marked *unchanged since*:
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-jalen-duren-to-miss-at-least-two-more-weeks/)
  - [Yahoo Canada, 8 Nov](https://ca.news.yahoo.com/raptors-offer-insight-return-timeline-214519543.html)
  - [Yahoo, 24 Oct](https://sports.yahoo.com/articles/magic-star-paolo-banchero-injury-175842373.html)
  - [Roundtable, 7 Nov](https://roundtable.io/sports/nba/warriors/news/warriors-vs-magic-injury-report-draymond-green-paolo-banchero-statuses)
  - [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-ruled-out-saturday/)
  - [Hoops Rumors, Oct](https://www.hoopsrumors.com/2026/10/nuggets-julian-strawther-out-at-least-six-weeks-with-knee-sprain.html)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/christian-braun-calf-questionable-monday-vs-hou)
  - [NBA.com, 30 Oct](https://www.nba.com/news/chet-holmgren-out-8-10-weeks-with-patellar-tendon-tear)
  - [CBS/RotoWire, 7 Nov](https://www.cbssports.com/fantasy/basketball/news/thunders-jaylin-williams-out-against-wizards/)
  - [Hoops Rumors, Jul](https://www.hoopsrumors.com/2026/07/mouhamed-gueye-has-surgery-out-three-to-four-months-with-fractured-foot.html)
  - [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/aaron-wiggins-news-provides-spark-off-bench-537653)
  - [Yahoo, 8 Nov](https://sports.yahoo.com/articles/game-preview-orleans-pelicans-los-205416257.html)
  - [RotoWire, 5 Nov](https://www.rotowire.com/basketball/headlines/yves-missi-injury-remains-on-shelf-537773)
  - [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/norman-powell-injury-out-sunday-538162)
  - [FantasyPros, 8 Nov](https://www.fantasypros.com/nba/news/618532/norman-powell-shoulder-ruled-out-sunday.php)
  - [Hoops Rumors, 8 Nov](https://www.hoopsrumors.com/2026/11/hornets-knueppel-schroder-out-multiple-weeks-with-hamstring-strains.html)
  - [RealGM, 7 Nov](https://basketball.realgm.com/wiretap/288060/Brandon-Ingram-Ramping-Up-Towards-Clippers-Debut)
  - [Roundtable, 8 Nov](https://roundtable.io/sports/nba/clippers/news/clippers-injury-report-rules-out-five-players-vs-pelicans)
  - [AP via Yahoo, 8 Nov](https://sports.yahoo.com/articles/clippers-beat-pelicans-end-7-044836989.html)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/nic-claxton-hamstring-plays-18-minutes-sunday)
  - [FantasyPros, 7 Nov](https://www.fantasypros.com/nba/news/618370/peyton-watson-hamstring-off-injury-report-saturday.php)
  - [ESPN, 8 Nov](https://espn.com/nba/story/_/id/50425681/kon-knueppel-least-four-weeks-hamstring-strain)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/kevin-huerter-posts-22-4-5-2-5-line-vs-lakers)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/daniss-jenkins-drops-career-high-31-points-in-loss)
  - [Denver Gazette, 8 Nov](https://www.denvergazette.com/2026/11/08/nuggets-starters-questionable-for-mondays-game-against-rockets/)
  - [Roundtable, 9 Nov](https://roundtable.io/sports/nba/rockets/game-day/november-9th-injury-report-for-houston-rockets-vs-denver-nuggets)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/devin-vassell-groin-questionable-monday-vs-phx)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/x-rays-negative-for-quentin-grimes-finger)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/t-j-mcconnell-hamstring-questionable-monday)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jamal-murray-contusion-questionable-vs-rockets)
  - [Heavy, 8 Nov](https://heavy.com/sports/nba/denver-nuggets/nikola-jokic-elbow-injury-news-rockets/)
  - [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/and-lastly-brandon-miller-has-been-diagnosed-with-a/92682399007/)
  - [RotoBaller, 8 Nov](https://www.rotoballer.com/player-news/brandon-miller-sidelined-monday-versus-cavaliers/1987955)
  - [Jazz on X, 8 Nov](https://x.com/utahjazz/status/2119463702122434874)
  - [Yahoo, Nov](https://sports.yahoo.com/articles/hannes-steinbach-calls-extended-hornets-171704327.html)
  - [Yahoo, 8 Nov](https://sports.yahoo.com/articles/hornets-injury-latest-brandon-miller-011009724.html)
  - [Sports Mole, 8 Nov](https://www.sportsmole.co.uk/basketball/cleveland-cavaliers/preview/cleveland-cavaliers-vs-charlotte-hornets-player-props-injury-report-and-prediction--nba_608728.html)
  - [Basketnews, 8 Nov](https://basketnews.com/news-259083-kon-knueppel-injury-hornets-announce-new-devastating-update-and-recovery-timeline.html)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-passive-performance-in-win/)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-christian-braun-questionable-for-monday-538201/)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/nuggets-spencer-jones-scores-13-points-in-season-debut/)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/okc-starts-sga-mitchell-kenrich-mara-ihart)
  - [NBC, 3 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-03/derrick-jones-jr-knee-absent-from-injury-report)
  - [NBA.com, 8 Nov](https://www.nba.com/pelicans/news/gameday-update-pelicans-at-clippers-11-8-2026)
  - [CBS box score, 8 Nov](https://www.cbssports.com/nba/gametracker/boxscore/NBA_20261108_LAL@DET/)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/isaiah-joe-hip-remains-out-sunday-vs-lakers)
  - [Raptors Republic, 6 Nov](https://raptorsrepublic.com/2026/11/06/quick-reaction-raptors-121-bucks-107/)
  - [NBC, 6 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-06/raptors-to-start-shead-walter-rj-collin-poeltl)
  - [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/pistons-isaiah-joe-another-absence-coming/)
  - [NBC, 6 Nov](https://nbcsports.com/fantasy/basketball/player-news/2026-11-06/jared-mccain-drops-21-points-in-lopsided-win)
  - [RotoWire, 7 Nov](https://www.rotowire.com/basketball/headlines/jared-mccain-news-returns-to-bench-saturday-538052)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jordan-goodwin-calf-questionable-monday-vs-sas)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/suns-jordan-goodwin-iffy-for-monday/)
  - [Basketnews, 8 Nov](https://basketnews.com/news-259069-scottie-barnes-raptors-guard-get-status-updates-before-grizzlies-game.html)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/pacers-t-j-mcconnell-strikes-for-six-points-in-season-debut/)
  - [Roundtable, Nov](https://roundtable.io/sports/nba/pacers/news/pacers-still-have-no-timeline-for-tyrese-haliburton-s-return)
  - [CBS/RotoWire, Nov](https://www.cbssports.com/fantasy/basketball/news/kings-leaky-black-steady-in-fill-in-role/)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/sac-acuff-lavine-hunter-achiuwa-cardwell)
  - [Yahoo, Nov](https://sports.yahoo.com/articles/nuggets-better-options-cutting-trevon-160004870.html)
  - [Hoops Rumors, 6 Nov](https://www.hoopsrumors.com/2026/11/jazz-center-jusuf-nurkic-out-at-least-two-more-weeks.html)
  - [Shams Charania via Yahoo, 26 Oct](https://sports.yahoo.com/nba/breaking-news/article/magics-jalen-suggs-diagnosed-with-bone-bruise-in-right-knee-will-be-re-evaluated-in-2-weeks-184734151.html)
  - [SI, 7 Nov](https://www.si.com/nba/magic/onsi/orlando-magic-down-another-starter-against-warriors-preview-injuries-starters-how-to-watch-01m6vzmr2fpm)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/aaron-gordon-lower-body-questionable-monday)
  - [Fox Sports, Nov](https://www.foxsports.com/articles/nba/memphis-faces-toronto-looks-to-break-3game-slide)
  - [RealGM, Nov](https://basketball.realgm.com/wiretap/288056/Scotty-Pippen-Jr-Isaiah-Stewart-To-Miss-Time-For-Grizzlies)
  - [Yahoo, 5 Nov](https://sports.yahoo.com/articles/grizzlies-isaiah-stewart-avoided-anything-001100081.html)
  - [Air Alamo, 8 Nov](https://airalamo.com/spurs-suns-injury-report-what-devin-vassell-s-questionable-tag-means-for-san-antonio)
  - [Dallas Sports Journal, 8 Nov](https://dallassportsjournal.com/brooklyn-nets-egor-demin-mikel-brown-jr-out-vs-mavericks)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/demin-leg-progressing-out-at-least-two-games)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jaylon-tyson-ankle-ruled-out-monday-vs-hornets)
  - [NBC, 7 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-07/robert-williams-rest-out-saturday-vs-spurs)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/lakers-quentin-grimes-doesnt-return-sunday/)
  - [Sactown Sports, 6 Nov](https://sactownsports.com/nba/sacramento-kings/spurs-recap)
  - [Dallas Sports Journal, Nov](https://dallassportsjournal.com/dereck-lively-ii-injury-update-dusty-may-mavericks-rockets/)
  - [The Smoking Cuban, Nov](https://thesmokingcuban.com/dereck-lively-ii-extended-absence-putting-his-mavericks-future-in-jeopardy)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/isaiah-jackson-groin-to-travel-with-lac-monday)
  - [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/jock-landale-injury-iffy-for-monday-538185)
  - [Yahoo, 8 Nov](https://sports.yahoo.com/articles/jock-landale-questionable-vs-lakers-221750590.html)
  - [Heavy, Nov](https://heavy.com/sports/nba/los-angeles-clippers/brandon-ingram-practice-achilles-return-soon/)
  - [Heavy](https://heavy.com/sports/nba/golden-state-warriors/jimmy-butler-return-update-steve-kerr/)
  - [NBA.com, 6 Nov](https://www.nba.com/news/kristaps-porzingis-stepping-away-from-basketball)
  - [ESPN, Sep](https://www.espn.com/nba/story/_/id/49904356/sources-suns-mark-williams-miss-shoulder-surgery)
  - [SI](https://www.si.com/nba/suns/onsi/insider-reveals-when-phoenix-suns-center-mark-williams-should-return-from-injury)
  - [SI](https://www.si.com/nba/trailblazers/onsi/portland-trail-blazers-shaedon-sharpe-undergoes-surgery-whats-next)
  - [RotoWire, 5 Oct](https://www.rotowire.com/basketball/headlines/donte-divincenzo-injury-targeting-late-season-return-533214)
  - [RotoWire, 8 Nov](https://www.rotowire.com/basketball/headlines/jamal-murray-injury-questionable-against-houston-538199)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/jalen-duren-hamstring-cleared-for-on-court-work)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/raptors-scottie-barnes-questionable-for-monday/)
  - [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/scottie-barnes-immanuel-quickley-to-return-against-grizzlies/92678359007/)
  - [ESPN, 3 Nov](https://www.espn.com/nba/story/_/id/50373620/kawhi-leonard-finishes-knee-treatment-begins-return-process)
  - [AP via ClickOnDetroit, 31 Oct](https://www.clickondetroit.com/sports/2026/10/31/chet-holmgren-out-at-least-2-months-with-knee-injury-and-cason-wallace-has-shoulder-surgery/)
  - [Yahoo, 28 Oct](https://sports.yahoo.com/nba/breaking-news/article/thunders-jalen-williams-has-surgery-on-ankle-fractured-fibula-will-be-reevaluated-before-end-of-season-011001403.html)
  - [CBS/RotoWire](https://www.cbssports.com/fantasy/basketball/news/warriors-moses-moody-could-return-by-december/)
  - [NBC Sports, 30 Oct](https://www.nbcsports.com/nba/news/portlands-ja-morant-to-miss-at-least-a-month-with-left-hamstring-strain)
  - [ClutchPoints, 5 Nov](https://clutchpoints.com/nba/portland-trail-blazers/blazers-news-portland-loses-guard-to-painful-injury-in-win-vs-suns)
  - [Yahoo (Titus), 30 Oct](https://sports.yahoo.com/fantasy/article/nba-injury-report-who-to-add-with-anthony-edwards-tyrese-haliburton-ja-morant-and-other-stars-sidelined-210351864.html)
  - [CBS/RotoWire, 8 Nov](https://www.cbssports.com/fantasy/basketball/news/hornets-kon-knueppel-out-at-least-four-weeks/)
  - [HoopsHype, 8 Nov](https://www.hoopshype.com/story/sports/nba/rumors/2026/11/08/dennis-schroeder-will-miss-at-least-two-weeks/92682400007/)
  - [Salt Lake Tribune, 27 Oct](https://www.sltrib.com/sports/jazz/2026/10/27/utah-jazz-forward-jaren-jackson-jr/)
  - [Hoops Rumors, 26 Aug](https://www.hoopsrumors.com/2026/08/clippers-jordan-miller-out-at-least-six-months-following-shoulder-surgery.html)
  - [RotoWire, 2 Nov](https://www.rotowire.com/basketball/headlines/brandon-ingram-injury-returns-from-g-league-assignment-537174)
  - [RotoWire, Jul](https://www.rotowire.com/basketball/headlines/jamir-watkins-injury-undergoes-surgery-for-torn-acl-532251)
  - [NBA.com, 28 Oct](https://www.nba.com/news/washington-wizards-justin-champagnie-foot-surgery)
  - [Roundtable, 25 Sep](https://roundtable.io/sports/nba/pacers/news/pacers-give-johnny-furphy-acl-rehab-update-before-camp)
  - [Forbes, 6 Nov](https://www.forbes.com/sites/tonyeast/2026/11/06/ben-sheppard-longer-absence-is-bad-news-for-indiana-pacers/)
  - [Yardbarker, 25 Oct](https://www.yardbarker.com/nba/articles/paolo_banchero_expects_to_miss_at_least_a_month_with_ankle_injury/s1_14822_44473182)
  - [NBC, 8 Nov](https://www.nbcsports.com/fantasy/basketball/player-news/2026-11-08/anthony-black-exits-during-ot-due-to-cramping)
  - [Inquirer, 4 Nov](https://www.inquirer.com/sixers/dominick-barlow-injury-update-76ers-lebron-james-joel-embiid-20261104.html)
  - [NBC Sports, 18 Oct](https://www.nbcsports.com/nba/news/kings-ben-simmons-suffers-torn-achilles-at-practice-sunday-will-miss-entire-season)
  - [TSN, Oct](https://www.tsn.ca/nba/article/nuggets-strawther-out-with-knee-sprain-will-be-reevaluated-in-six-weeks-n1-50199062/)
  - [Fox Sports](https://www.foxsports.com/nba/mouhamed-gueye-player)
- Our roster and IR moves: `council/roster.csv`. Pending offers: today's `council/slump_watch.py` run (06:47 UTC). Streaming plan: `docs/analysis/20261109-matchup4.md`. Form and rates: `python council/form.py`, run 2026-11-09 06:49 UTC.
