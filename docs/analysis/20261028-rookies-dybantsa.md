# Rookies against projection

- Generated 2026-10-28 01:59 UTC by `council/rookies.py`. This is **a report, not a council verdict**.
- **Rookies:** 69 players with 0 years' experience on ESPN's NBA rosters, 59 of them in the league's player pool. Draft picks come from ESPN's core API.
- **Actual:** this season's FP/g in our scoring. **Projected:** ESPN's 2027 projection re-scored with `scripts/league_scoring.py`. The projection leaves out OREB, DREB, DD and TD, so it reads low for everyone; the veterans' ratio is the baseline for that.
- **Preseason FP/36:** league-scored from ESPN's preseason box scores (67 games), for players with 20+ preseason minutes.
- **Ratios** use players with 3+ games and 20+ projected minutes.
- **Checks:** **games were live** (--allow-live). All 1099 pool players re-score with `scripts/league_scoring.py` (0 mismatches).

## Verdict

**Dybantsa should score about 27 to 32 FP/g now** (*Estimate*, below).
- The three methods give 26.8, 28.8 and 32.2.
- The middle half of lottery rookies would put him at 20.0–33.0.
- Against our flexible slots: Pritchard's rate is 27.2 and VanVleet's is 32.4 (`council/matchup.py`, 28 Oct).

**35+ is the upside case, not the expectation.**
- Of the 23 rookies with 3+ games, 2 are at 35+ FP/g: Lendeborg (46.0) and Caleb Wilson (37.0), both ours. Only Lendeborg is at 40+.
- The top-5 picks are close to their projections, at a median 0.98. The lottery as a whole is at 0.82, and veterans are at 0.91.
- Per minute, rookies sit close to ESPN's projection (median FP/36 ratio 0.97). Where they fall short, it's minutes.
  - Dybantsa's projection already gives him 32.2 minutes, a starter's load.

**Why he could beat it:**
- His preseason FP/36 of 41.0 tops Wilson (31.4), Peterson (34.9) and Acuff (37.1). Only Boozer (46.2) and Lendeborg (62.1) are higher among the top picks.
- He's slated to start at small forward.

**Why he could fall short:**
- This scoring punishes misses. In preseason he shot 18 of 41 from the field and 13 of 21 at the line (CBS, in `docs/research/20261019-0750-preseason-east.md`).
- He is coming off an ankle sprain that has cost him the first four games.
- Rookies as a group start colder than their preseason: the median rookie keeps 0.78× of his preseason FP/36.

## The move

- **He is on waivers, not a free agent.**
  - Snow Time Lakers dropped him on 27 Oct, and claims process **Thu 29 Oct at 3:00 am ET, which is 6:00 pm Thursday in Melbourne** (ESPN `kona_player_info`).
  - A claim counts as one of our 6 adds.
- **We are last in the waiver order, 8 of 8.**
  - Any other team's claim wins.
  - If he debuts Wednesday at Cleveland, that game won't count for anyone, and a good one will draw claims.
- **Washington's games:**
  - this week: Fri 30 only, a day our lineup is already full
  - next week: Mon 2, Wed 4, Fri 6 and Sat 7
  - the week after: four more
- **The claim needs its drop player on the roster when it processes.**
  - Whoever you name stays until Thursday 3:00 am ET.
  - If the claim fails, he stays for good.

What the stash costs this week, from three `council/matchup.py` runs at 01:55 UTC (`--rotate`, with `--sit` for the slot Dybantsa would hold):

| Option | Our lineup, Wed–Sun | Moves |
|---|---:|---|
| No Dybantsa: stream both slots | **1,205** | the 6-add plan in `20261028-matchup2-rotation.md` |
| Claim him for **Pritchard**, then stream VanVleet's slot from Thursday | **1,093** (721 Thu–Sun, plus Wednesday's 372 as rostered) | Thu VanVleet → McCollum; Fri → Powell; Sat → Hayes; Sun → Walter |
| Claim him for **VanVleet**, then stream Pritchard's slot from Wednesday | **1,098** | Wed Pritchard → P.J. Washington; Thu → McCollum; Fri → Powell; Sat → Hayes; Sun → Walter |

- **The stash costs about 110 points this week, whichever slot holds him.**
  - Both runs score his slot at nothing: his one game is Friday, when we're full.
  - As rostered we project 1,463 to their 1,750 (same runs), and the full plan adds +115.1. We're behind with or without him.
- **Claim him for Pritchard,** as you planned.
  - The two options are level this week, and VanVleet carries the higher rate (32.4 against 27.2).
  - If the claim fails, Pritchard plays Friday and Sunday.
- **Streaming VanVleet's slot from Thursday is optional.**
  - It is worth +56.7 this week (the Pritchard-claim run), and it costs VanVleet.
- **Injury timelines:**
  - **Dybantsa** (left ankle sprain): questionable for Wednesday at CLE, no timetable reported; ESPN est. 28 Oct.
  - **Hayes** (right shoulder soreness, Saturday's add): questionable for Wednesday, no timetable reported; ESPN est. 28 Oct.
  - **Lendeborg** (left foot soreness): questionable for Wednesday, no timetable reported; ESPN est. 28 Oct.

## Actual against projected

| Group | Players | Median actual ÷ projected FP/g | Middle half | Median minutes ratio | Median FP/36 ratio |
|---|---:|---:|---|---:|---:|
| Rookies, picks 1–14 | 10 | **0.82** | 0.61–1.00 | 0.96 | 0.97 |
| Rookies, picks 1–5 | 4 | **0.98** | 0.85–1.04 | 1.01 | 0.97 |
| Veterans (baseline) | 203 | **0.91** | 0.72–1.08 | 0.93 | 0.99 |

Against the veterans' baseline, lottery rookies are running at **0.89×** what ESPN projected for them.

Rookies with 3+ games at **35+ FP/g: 2**; at **40+: 1** (of 23).

## The rookie class

Sorted by current FP/g. Draft pick is overall for the first round.

| Pick | Player | NBA | Pos | GP | Min | Started | FP/g | Projected FP/g (min) | Actual ÷ projected | Preseason FP/36 | FP/36 now | League | Status |
|---:|---|---|---|---:|---:|---|---:|---:|---:|---:|---:|---|---|
| 11 | **Yaxel Lendeborg** | GS | SF/PF | 4 | 33.2 | 4 of 4 | **46.0** | 23.5 (24.6) | 1.96 | 62.1 | 49.8 | Come-in Cider | day-to-day, foot, ESPN est. 28 Oct |
| 4 | **Caleb Wilson** | CHI | SF | 4 | 33.8 | 4 of 4 | **37.0** | 34.9 (32.1) | 1.06 | 31.4 | 39.5 | Come-in Cider |  |
| 3 | **Cameron Boozer** | MEM | PF | 4 | 33.0 | 4 of 4 | **33.2** | 34.3 (31.7) | 0.97 | 46.2 | 36.3 | Lauri Birds |  |
| 19 | **Allen Graves** | TOR | SF | 3 | 15.0 | 0 of 3 | **26.0** | — (—) | — | 30.3 | 62.4 | free agent |  |
| R2 #34 | **Meleek Thomas** | CLE | SG | 1 | 19.0 | 0 of 1 | **25.0** | — (—) | — | 46.7 | 47.4 | free agent |  |
| 7 | **Darius Acuff Jr.** | SAC | PG | 4 | 33.5 | 3 of 3 | **24.8** | 30.4 (30.6) | 0.81 | 37.1 | 26.6 | Team Nic Kerr |  |
| 5 | **Keaton Wagler** | LAC | PG/SG | 3 | 26.3 | 0 of 3 | **24.0** | 24.4 (28.1) | 0.99 | 30.7 | 32.8 | free agent |  |
| 2 | **Darryn Peterson** | UTAH | PG/SG | 4 | 29.2 | 4 of 4 | **23.8** | 29.1 (29.7) | 0.82 | 34.9 | 29.2 | free agent |  |
| undrafted | **Tobe Awaka** | CHI | PF | 2 | 13.0 | 0 of 2 | **21.5** | — (—) | — | 38.4 | 59.5 | free agent | day-to-day, ankle, ESPN est. 28 Oct |
| undrafted | **Graham Ike** | GS | PF | 4 | 13.2 | 2 of 4 | **20.8** | — (—) | — | 41.0 | 56.4 | waivers |  |
| R2 #35 | **Trevon Brazile** | DEN | SF/PF | 3 | 21.0 | 0 of 3 | **20.3** | — (—) | — | 43.7 | 34.9 | free agent |  |
| 6 | **Mikel Brown Jr.** | BKN | PG | 3 | 21.0 | 0 of 2 | **17.3** | 24.0 (30.2) | 0.72 | — | 29.7 | free agent |  |
| 12 | **Aday Mara** | OKC | C | 4 | 14.8 | 0 of 4 | **16.8** | — (—) | — | 55.2 | 40.9 | free agent |  |
| 10 | **Brayden Burries** | MIL | SG | 4 | 14.2 | 0 of 4 | **14.5** | 22.2 (25.8) | 0.65 | 49.3 | 36.6 | free agent |  |
| 14 | **Hannes Steinbach** | CHA | PF | 1 | 12.0 | 0 of 1 | **13.0** | 17.5 (17.9) | 0.74 | 49.2 | 39.0 | free agent |  |
| undrafted | **Alpha Diallo** | DEN | SF | 1 | 22.0 | 0 of 1 | **13.0** | — (—) | — | 29.5 | 21.3 | free agent | out, right personal, ESPN est. 30 Oct |
| 8 | **Kingston Flemings** | ATL | PG/SG | 4 | 18.2 | 0 of 4 | **10.5** | 22.3 (24.8) | 0.47 | 37.3 | 20.7 | free agent |  |
| 9 | **Morez Johnson Jr.** | DAL | PF/C | 4 | 14.5 | 0 of 4 | **10.0** | 23.5 (24.7) | 0.43 | 38.8 | 24.8 | free agent |  |
| R2 #49 | **Bryce Hopkins** | DEN | SF | 3 | 17.3 | 2 of 3 | **9.7** | — (—) | — | 16.9 | 20.1 | free agent |  |
| 25 | **Sergio de Larrea** | DAL | PG | 4 | 11.8 | 0 of 4 | **9.0** | — (—) | — | 38.5 | 27.6 | free agent | out, right knee strain, ESPN est. 30 Oct |
| 15 | **Dailyn Swain** | CHI | SF | 1 | 12.0 | 0 of 1 | **7.0** | — (—) | — | 29.3 | 21.0 | free agent |  |
| R2 #48 | **Tobi Lawal** | DAL | SF | 2 | 2.5 | 0 of 2 | **7.0** | — (—) | — | 47.6 | 100.8 | free agent |  |
| R2 #45 | **Emanuel Sharp** | SAC | SG | 4 | 15.0 | 0 of 3 | **6.8** | — (—) | — | 24.6 | 16.2 | free agent |  |
| 13 | **Nate Ament** | MIL | SF | 2 | 12.5 | 0 of 2 | **6.5** | 13.5 (17.7) | 0.48 | 30.0 | 18.7 | free agent |  |
| 27 | **Chris Cenac Jr.** | BOS | PF/C | 1 | 5.0 | 0 of 1 | **5.0** | — (—) | — | 49.7 | 36.0 | free agent |  |

Rookies yet to play who project for 20+ FP/g: AJ Dybantsa (WSH, pick 1, projected 32.9, out, left ankle sprain, ESPN est. 28 Oct).

### Notes

- **Dybantsa's ankle:** he sprained his left ankle in the 16 Oct preseason finale and has missed Washington's first four games.
  - He was upgraded to questionable for Wednesday at Cleveland and did on-court work on Tuesday.
  - Coach Brian Keefe would not say whether he'll play [Bullets Forever](https://www.bulletsforever.com/washington-wizards-news/73685/aj-dybantsa-ankle-upgraded-to-questionable-vs-cavs) [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/wizards-aj-dybantsa-questionable-for-wednesday/).
  - No timetable reported; ESPN est. 28 Oct.
- **His role:** he was slated to start at small forward, and Coulibaly would move back to a rotation role when he returns [Yahoo Sports](https://sports.yahoo.com/articles/wizards-rookie-aj-dybantsa-listed-002442684.html) [Yahoo Sports](https://sports.yahoo.com/articles/wizards-aj-dybantsa-ranked-among-213637301.html).
- **The rest of the class:**
  - Caleb Wilson leads the rookies in scoring, with a 30-point, 14-rebound game against Washington.
  - Lendeborg had 31 and 12 against Denver while starting for Golden State with Jimmy Butler out.
  - Boozer is shooting about 28%, and Peterson is scoring about 11 a game [NBA.com](https://www.nba.com/news/nba-fantasy-week-2-fantasy-rookie-power-rankings) [Legion Report](https://legionreport.com/nba-rookie-stats/).

## Preseason to regular season

Rookies with 3+ games and 20+ preseason minutes: **21**. The median rookie is scoring **0.78×** his preseason FP/36 in the regular season.

## Estimate: AJ Dybantsa

- **AJ Dybantsa** (WSH, SF, pick 1): waivers, out, left ankle sprain, ESPN est. 28 Oct.
- **ESPN projects** 32.9 FP/g in 32.2 minutes (36.8 FP/36).
- **Preseason:** 41.0 FP/36 over 86 minutes.

| Method | Estimate FP/g | Range |
|---|---:|---|
| Projection × lottery rookies' median ratio (0.82) | **26.8** | 20.0–33.0 (middle half of lottery rookies) |
| Projection × top-5 picks' median ratio (0.98) | **32.2** | — |
| Preseason FP/36 × rookies' carry-over (0.78) at 32.2 min | **28.8** | — |

## Sources

- ESPN fantasy API, league 423671879 (`kona_player_info`, `mTeam`), ESPN's NBA rosters, schedules, box scores and core athlete API, and ESPN's injury feed, read 2026-10-28 01:59 UTC.
- `council/matchup.py --rotate` runs for the stash costs, 28 Oct 2026 01:55 UTC (games live).
- Research, 28 Oct 2026: [Bullets Forever](https://www.bulletsforever.com/washington-wizards-news/73685/aj-dybantsa-ankle-upgraded-to-questionable-vs-cavs); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/wizards-aj-dybantsa-questionable-for-wednesday/); [Yahoo Sports](https://sports.yahoo.com/articles/wizards-rookie-aj-dybantsa-listed-002442684.html); [Yahoo Sports](https://sports.yahoo.com/articles/wizards-aj-dybantsa-ranked-among-213637301.html); [NBA.com](https://www.nba.com/news/nba-fantasy-week-2-fantasy-rookie-power-rankings); [Legion Report](https://legionreport.com/nba-rookie-stats/).
