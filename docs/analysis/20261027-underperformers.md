# Underperformers review: every roster, 27 Oct 2026

- Prepared 27 Oct 2026, 01:30 UTC, by Claude. This is **a report, not a council verdict**.
- **Question asked:** for every team in the league, which of its best players are averaging **10 or more fantasy points per game below their projected average**?
- **Data:** all 111 rostered players, read live from league 423671879 through the ESPN fantasy API (`council/espn_sync.py`'s endpoint, `mRoster` view). This covers games through Mon 26 Oct (US). Teams have played **2 to 4 games**.
  - *Current* is ESPN's 2027 season split (`002027`).
  - *Projected* is ESPN's 2027 season projection (`102027`), which is the "projected average" ESPN shows on the player card.
  - *2026* is last season's actual average (`002026`).
- **Scoring check:** every current, projected and 2026 average was re-scored with `scripts/league_scoring.py` and **matches ESPN's league-scored totals exactly** (0 mismatches across 111 players).
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`, the same omission `README.md` documents for the workbook. The current average does carry them. Every gap below is therefore *smaller* than a like-for-like gap. The difference is largest for bigs: Gobert **4.5**, Wembanyama **4.3**, Zubac **3.7** and Davis **2.8** FP/g.
- **Sample:** at 2 to 4 games, one bad night moves an average by 5 to 10 points. Read the minutes column first.

## Headline

**19 rostered players are 10+ FP/g under projection, and every team has at least one.** Four of them are their fantasy team's **#1 player by projection**:

- **Wembanyama** (Cream Abdul-Yammar): 47.7 against 60.5
- **Gilgeous-Alexander** (Matt Wright's Foxies): 43.8 against 56.8
- **Anthony Davis** (Melbourne poopoo): 39.0 against 49.6
- **Bane** is ours, but he is #8 on our roster.

Cream Abdul-Yammar and Lauri Birds have four each. Cream's #1, #2 and #3 are all on the list: Wembanyama, LaMelo Ball and Giddey.

| Team | Flagged | Their top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | **4** | Wembanyama 47.7/60.5 · LaMelo 31.5/46.4 · Giddey 23.5/46.2 |
| Lauri Birds | **4** | Jokić 60.0/67.2 · Haliburton 48.0/48.6 · Curry 32.5/43.0 |
| Matt Wright's Foxies | 3 | Gilgeous-Alexander 43.8/56.8 · Flagg 50.3/45.4 · Mobley 40.0/43.3 |
| Melbourne poopoo | 3 | Davis 39.0/49.6 · Edwards 48.0/47.2 · Towns 46.7/44.1 |
| Dr White Slong | 2 | Giannis 50.5/57.6 · Mitchell 46.0/46.5 · Avdija 43.0/40.4 |
| Come-in Cider (us) | 1 | Cunningham 45.0/50.4 · Leonard 40.0/45.7 · Jamal Murray 38.0/43.9 |
| Snow Time Lakers | 1 | Jalen Johnson 48.8/50.0 · Tatum 45.7/48.1 · Embiid 46.3/45.4 |
| Team Nic Kerr | 1 | Dončić 55.3/60.6 · Sabonis 60.3/46.7 · Maxey 50.8/45.1 |

## By team

Columns: **Rank** = the player's rank on his fantasy roster by projection. **Min** = current / projected minutes. **Gap** = current minus projected FP/g. The *driver* line splits the gap into minutes and category shortfalls, in fantasy points per game.

### Cream Abdul-Yammar: 4

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 4 | 25.8 / 35.5 | 23.5 | 46.2 | **−22.7** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 4 | 23.8 / 32.9 | 31.5 | 46.4 | **−14.9** | 41.1 | Active |
| Victor Wembanyama | SA | #1 | 3 | 31.7 / 32.5 | 47.7 | 60.5 | **−12.8** | 59.5 | Active |
| Rudy Gobert | MIN | #10 | 4 | 31.2 / 32.5 | 22.0 | 34.3 | **−12.3** | 38.2 | Active |

- **Giddey** has the league's largest gap. **Minutes** are 10 below projection and **efficiency** is down too: 0.91 FP/min against 1.30. He is shooting 2.8-of-8.2 for 7.0 points. New coach Tiago Splitter has been cutting his minutes at the point, and he has been benched in late-game stretches. One game was 1-of-10 from the field in 24 minutes.
- **LaMelo** is a **minutes** problem only. His FP/min is 1.33 against 1.41, but he is playing 23.8 minutes against 32.9. Chris Finch wants him at about 30, and has been held back by foul trouble and caution after injury. He played 16–17 minutes on 25 Oct.
- **Wembanyama** is an **efficiency** problem. His minutes are intact, but he is shooting 6.3-of-17.3 and scoring 20.0 points against 26.9, which costs 13.6 FP/g on scoring alone. His blocks are on projection (4.0 against 3.5).
- **Gobert** is an **efficiency** problem. His minutes are intact, but his stocks are worth −7.6: 0.0 steals and 0.5 blocks against 0.7 and 1.7. He is shooting 2.5-of-5.5 and 3-of-6 at the line. His 13.5 rebounds, 4.5 of them offensive, are above projection.

### Lauri Birds: 4

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Lauri Markkanen | UTAH | #7 | 4 | 28.5 / 34.0 | 25.5 | 38.7 | **−13.2** | 44.4 | Day-to-day |
| Stephen Curry | GS | #3 | 2 | 25.5 / 32.0 | 32.5 | 43.0 | **−10.5** | 43.5 | Active |
| Ivica Zubac | IND | #8 | 3 | 21.7 / 31.1 | 25.3 | 35.5 | **−10.1** | 36.3 | **Out** |
| Bam Adebayo | MIA | #6 | 4 | 29.0 / 32.4 | 29.5 | 39.6 | **−10.1** | 42.7 | Active |

- **Markkanen** has both problems. He is 5.5 minutes under projection, and his scoring is worth −9.5 (4.8-of-12.0). ESPN lists him day-to-day; no public report of the reason was found.
- **Curry** has played only 2 of Golden State's games. He sprained his right ankle in an 18 Oct scrimmage and was due back Mon 26 Oct. His FP/min is close to projection (1.27 against 1.35), so this is **minutes and availability**.
- **Zubac** sprained his left ankle on 25 Oct at Brooklyn. He left in the first quarter, which drags his minutes average down. X-rays were negative, he was ruled out on 26 Oct, and **no return date** has been set. His FP/min is on projection.
- **Adebayo** is an **efficiency** problem. He is scoring 10.8 points against 20.2 (−11.1) and taking 6.2 rebounds against 10.0, while his stocks are above projection (+3.4).

### Matt Wright's Foxies: 3

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Shai Gilgeous-Alexander | OKC | **#1** | 4 | 32.2 / 33.8 | 43.8 | 56.8 | **−13.1** | 56.4 | Active |
| Miles Bridges | PHX | #11 | 3 | 27.0 / 33.1 | 21.0 | 33.9 | **−12.9** | 32.2 | Active |
| Jaren Jackson Jr. | UTAH | #8 | 4 | 25.0 / 31.4 | 26.2 | 38.1 | **−11.9** | 35.9 | Active |

- **Gilgeous-Alexander** is a **production** problem. His minutes are intact, but he is at 24.2 points against 31.2 and 3.2-of-3.8 at the line against 7.8-of-8.8. His assists are 3.5 against 6.4 (−5.8 FP).
- **Bridges** has both problems. He is 6 minutes light in a new Phoenix starting role, and his scoring is worth −9.2.
- **Jackson** has a **minutes** problem that is already fixing itself. Fouling out of the opener in 28 minutes, plus a light game, pulls his average down. His next two games were 33 minutes each, 24 and 20 points. His stocks are worth −5.2.

### Melbourne poopoo: 3

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| DeMar DeRozan | DEN | #11 | 2 | 26.0 / 28.9 | 11.0 | 29.8 | **−18.8** | 32.7 | Active |
| Jalen Brunson | NY | #4 | 3 | 34.3 / 35.3 | 29.3 | 43.8 | **−14.5** | 43.1 | Active |
| Anthony Davis | WSH | **#1** | 4 | 33.2 / 32.2 | 39.0 | 49.6 | **−10.6** | 48.5 | Active |

- **DeRozan** is an **efficiency** problem in a new role. He is Denver's sixth man, confirmed by David Adelman, and has played 24–28 minutes. In 2 games he is at 0.42 FP/min against 1.03, with 0 steals, 0 blocks and 3.0 turnovers.
- **Brunson** is an **efficiency** problem at full minutes. He is shooting 8.3-of-21.3, with 3.7 assists against 6.9 (−6.5 FP). The Knicks are 0-3, and he has publicly taken the blame. He went 12-of-28 on 25 Oct.
- **Davis** is a **production** problem. His minutes are on projection, but his blocks are 0.8 against 2.1 and his rebounds 9.2 against 11.4.

### Dr White Slong: 2

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Keegan Murray | SAC | #10 | 2 | 27.0 / 34.1 | 12.0 | 29.3 | **−17.3** | 31.6 | **Out** |
| Matas Buzelis | CHI | #9 | 4 | 24.2 / 30.5 | 19.0 | 32.5 | **−13.5** | 32.7 | Active |

- **Murray** is **injured**. He has left ankle capsulitis in a surgically repaired ankle, and on 26 Oct the Kings set a re-evaluation in **10–14 days**.
- **Buzelis** has both problems. He is 6 minutes light under Splitter's rotation and is shooting 3.2-of-8.8. His stocks are worth −4.2.

### Come-in Cider (us): 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Desmond Bane | ORL | #8 | 3 | 31.7 / 33.7 | 21.0 | 38.2 | **−17.2** | 36.9 | Active (bench slot) |

- **Bane** is an **efficiency** problem. His minutes are intact, but his FP/min is 0.66 against 1.14. His assists are 1.3 against 4.8 (−6.9 FP) and his scoring is worth −10.1. Against Minnesota on 23 Oct he went 0-for-5 and fouled out in 27 minutes.

### Snow Time Lakers: 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Kyrie Irving | DAL | #4 | 3 | 25.0 / 34.6 | 32.7 | 44.2 | **−11.5** | — | Active |

- **Irving** is **minutes only**. His FP/min of 1.31 is *above* projection (1.28). He is on a minutes restriction in his return from a torn left ACL (March 2025), and sat out 24 Oct for knee management. He has no 2026 line because he missed that season.

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 3 | 33.3 / 33.6 | 31.0 | 42.1 | **−11.1** | 45.1 | Active |

- **Harden** is an **efficiency** problem at full minutes. He is shooting 4.3-of-12.0 for 15.0 points against 20.6. He has 4.0 turnovers against 3.4 and 6.7 assists against 8.1.

## What is driving the gaps

| Driver | Players | What it means |
|---|---|---|
| **Minutes only**, with FP/min at or above projection | Irving, LaMelo, Curry, Zubac | The per-minute production is intact. The gap closes when the minutes return: Irving's restriction lifting, Finch's target of about 30 for LaMelo, Curry healthy. Zubac's depends on the ankle. |
| **Efficiency at full minutes** | Wembanyama, Gilgeous-Alexander, Brunson, Harden, Davis, Gobert, Bane, Adebayo, DeRozan | The role is unchanged and the shots are not falling. At 2–4 games this is the noisiest part of any line. |
| **Both** | Giddey, Markkanen, Buzelis, Bridges, Jackson | Part role and part shooting. Giddey's minute cut comes from a coaching decision, which makes it the most structural on the list. |
| **Injured now** | Keegan Murray (re-evaluation in 10–14 days), Zubac (no timeline) | ESPN status OUT. |

Players on rosters who have **not played yet**: AJ Dybantsa (Snow Time Lakers, projected 32.9), Kon Knueppel (Team Nic Kerr, 35.2) and Brandon Ingram (Melbourne poopoo, 38.5). All three are listed OUT.

## Below the line on last season, not on projection

These players are **10+ under their 2026 average** but within 10 of ESPN's projection. Three of them are ours.

| Player | Team | GP | Min | Current | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|
| Scottie Barnes | **us** | 3 | 30.3 / 33.8 | 36.0 | 43.7 | 47.3 |
| Jalen Duren | **us** (IR) | 2 | 19.0 / 31.0 | 33.5 | 42.2 | 44.3 |
| Trey Murphy III | **us** | 3 | 33.3 / 32.5 | 28.0 | 36.8 | 41.6 |
| Nikola Jokić | Lauri Birds | 2 | 39.5 / 35.6 | 60.0 | 67.2 | 74.9 |
| Kevin Durant | Lauri Birds | 4 | 31.8 / 34.6 | 34.5 | 42.9 | 44.6 |
| Zach Edey | Lauri Birds | 3 | 15.7 / 26.4 | 26.0 | 33.2 | 39.5 |
| Alex Sarr | Team Nic Kerr | 4 | 24.5 / 28.6 | 27.5 | 36.6 | 39.4 |

## Context for our pending trade

The open offer to Melbourne poopoo sends VanVleet and Leonard for Brunson and Castle. Here is where all four stand:

| Player | Side | GP | Min | Current | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---|
| Jalen Brunson | we receive | 3 | 34.3 / 35.3 | 29.3 | 43.8 | **−14.5** | Active |
| Stephon Castle | we receive | 3 | 29.7 / 32.7 | 37.3 | 36.9 | +0.5 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | 45.7 | −5.7 | Day-to-day |
| Fred VanVleet | we send | 3 | 24.3 / 32.2 | 29.0 | 33.4 | −4.4 | Active |

- Brunson's shortfall comes at full minutes, so it is a shooting slump and not a role change.
- Leonard and VanVleet are both *above* projection per minute (1.54 against 1.39, and 1.19 against 1.04). Their gaps are minutes.

## Sources

- ESPN fantasy API, league 423671879, `mRoster`, `mTeam` and `mSettings` views, read 27 Oct 2026 01:30 UTC.
- Irving: [CBS Sports, minutes restriction](https://www.cbssports.com/fantasy/basketball/news/mavericks-kyrie-irving-will-be-on-minutes-restriction-friday/); [NBC Sports, 23 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-23/kyrie-irving-to-be-under-minutes-limit-friday); [Dallas Sports Journal, out vs Spurs](https://dallassportsjournal.com/kyrie-irving-out-morez-johnson-minutes-restriction-mavericks-spurs/)
- Giddey and Buzelis: [Yahoo Sports](https://sports.yahoo.com/articles/josh-giddey-playing-tonight-why-044402357.html); [Yahoo Sports, Splitter's rotation](https://sports.yahoo.com/articles/first-bulls-win-told-us-205314450.html); [RotoWire](https://www.rotowire.com/basketball/player/josh-giddey-5366)
- LaMelo Ball: [Star Tribune](https://www.startribune.com/minnesota-timberwolves-toronto-raptors-target-center-lamelo-ball-stats-anthony-edwards-chris-finch/601902946); [ESPN recap, 25 Oct](https://www.espn.com/nba/recap/_/gameId/401909864)
- Zubac: [iPacers, 26 Oct](https://ipacers.com/2026/10/26/indiana-pacers-injury-report-ivica-zubac-leaves-on-crutches-after-pacers-win-in-brooklyn/); [Basketnews](https://basketnews.com/news-258127-ivica-zubac-injury-pacers-coach-drops-encouraging-news-after-exit-vs-nets.html); [Yahoo Sports](https://sports.yahoo.com/articles/pacers-confirm-bad-injury-news-182427619.html)
- Keegan Murray: [HoopsHype, 26 Oct](https://www.hoopshype.com/story/sports/nba/rumors/2026/10/26/sacramento-kings-say-keegan-murray-left-ankle/92451271007/); [The Kings Herald](https://kingsherald.com/articles/kings-provide-medical-update-on-keegan-murray-maxime-raynaud-and-dylan-cardwell/)
- Curry: [HoopsHype, 25 Oct](https://hoopshype.com/story/sports/nba/rumors/2026/10/25/stephen-curry-set-to-return-monday-for-struggling-warriors/92436269007); [SF Chronicle](https://www.sfchronicle.com/sports/warriors/article/warriors-steph-curry-suffers-apparent-injury-22482932.php)
- DeRozan: [Heavy, Adelman on his role](https://heavy.com/sports/nba/denver-nuggets/david-adelman-confirms-demar-derozan-role/); [NBC Sports, debut](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-23/demar-derozan-scores-13-points-in-nuggets-debut)
- Brunson: [Yahoo Sports, 0-3 start](https://sports.yahoo.com/articles/knicks-jalen-brunson-makes-honest-203044292.html); [Hoops Rumors](https://www.hoopsrumors.com/2026/10/knicks-notes-brunson-drummond-brown-knecht-mccullar.html)
- Bane: [CBS Sports, fouls out in 27 minutes](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-fouls-out-in-27-minutes/); [Yahoo Sports](https://sports.yahoo.com/articles/desmond-bane-playing-tonight-why-031020637.html)
- Jackson: [Salt Lake Tribune, 22 Oct](https://www.sltrib.com/sports/jazz/2026/10/22/jaren-jackson-jr-returned-memphis/); [NBC Sports, 24 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/jaren-jackson-with-24-point-double-double-in-win)
- Bridges: [NBC Sports, 25 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/miles-bridges-scores-16-points-in-suns-home-debut); [RotoWire](https://www.rotowire.com/basketball/headlines/miles-bridges-news-solid-in-suns-debut-533337)
- Markkanen: no public report found explaining ESPN's day-to-day tag.
