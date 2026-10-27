# Underperformers review: every roster, 27 Oct 2026

- Prepared 27 Oct 2026, 04:55 UTC, by Claude. This is **a report, not a council verdict**.
- **Question asked:** for every team in the league, which of its best players are averaging **10 or more fantasy points per game below their projected average**?
- **Data:** all 111 rostered players, read live from league 423671879 through the ESPN fantasy API (`council/espn_sync.py`'s endpoint, `mRoster` view).
  - Read **after all nine games of Mon 26 Oct (US) went final**, per ESPN's scoreboard. No Tuesday game had started.
  - Teams have played **2 to 4 games**.
  - *Current* is ESPN's 2027 season split (`002027`).
  - *Projected* is ESPN's 2027 season projection (`102027`), which is the "projected average" ESPN shows on the player card.
  - *2026* is last season's actual average (`002026`).
- **Re-run:** the first version of this report was read at 01:30 UTC. At that point seven of Monday's nine games were in progress and GS @ DEN had not started. That read counted half-finished games as games played and missed the Denver game entirely, which put **45 players** on the wrong average. Every figure below comes from the final read. The section *What changed from the first read* lists who moved.
- **Scoring check:**
  - Every current, projected and 2026 average was re-scored with `scripts/league_scoring.py` and **matches ESPN's league-scored totals exactly** (0 mismatches across 111 players).
  - Every rostered player's Monday fantasy line was also re-scored from ESPN's **final NBA box scores**. All **59 of 59** match.
- **Projection gap:** ESPN's projection carries no `OREB`, `DREB`, `DD` or `TD`, the same omission `README.md` documents for the workbook. The current average does carry them. Every gap below is therefore *smaller* than a like-for-like gap. The difference is largest for bigs: Gobert **5.0**, Wembanyama **4.3**, Zubac **3.7** and Davis **2.8** FP/g.
- **Sample:** at 2 to 4 games, one bad night moves an average by 5 to 10 points. Read the minutes column first.

## Headline

**12 rostered players are 10+ FP/g under projection, spread across 7 of the 8 teams.** The Snow Time Lakers have none; Kyrie Irving is their closest, at −8.5.

Two of the 12 are their fantasy team's **#1 player by projection**:

- **Wembanyama** (Cream Abdul-Yammar): 47.7 against 60.5
- **Anthony Davis** (Melbourne poopoo): 39.0 against 49.6

Cream Abdul-Yammar's #1, #2 and #3 are all on the list: Wembanyama, LaMelo Ball and Giddey. **Gilgeous-Alexander** is no longer on it: after his 26-point final on Monday he sits at −9.1.

| Team | Flagged | Their top 3 by projection (current / projected) |
|---|---:|---|
| Cream Abdul-Yammar | **3** | Wembanyama 47.7/60.5 · LaMelo 30.8/46.4 · Giddey 23.5/46.2 |
| Dr White Slong | 2 | Giannis 53.2/57.6 · Mitchell 49.0/46.5 · Avdija 43.0/40.4 |
| Lauri Birds | 2 | Jokić 61.7/67.2 · Haliburton 53.2/48.6 · Curry 37.0/43.0 |
| Melbourne poopoo | 2 | Davis 39.0/49.6 · Edwards 52.5/47.2 · Towns 46.7/44.1 |
| Come-in Cider (us) | 1 | Cunningham 45.0/50.4 · Leonard 40.0/45.7 · Jamal Murray 43.0/43.9 |
| Matt Wright's Foxies | 1 | Gilgeous-Alexander 47.8/56.8 · Flagg 60.3/45.4 · Mobley 46.7/43.3 |
| Team Nic Kerr | 1 | Dončić 55.3/60.6 · Sabonis 60.3/46.7 · Maxey 50.8/45.1 |
| Snow Time Lakers | 0 | Jalen Johnson 52.8/50.0 · Tatum 46.7/48.1 · Embiid 46.3/45.4 |

## By team

Columns: **Rank** = the player's rank on his fantasy roster by projection. **Min** = current / projected minutes. **Gap** = current minus projected FP/g. The *driver* line splits the gap into minutes and category shortfalls, in fantasy points per game. **Near the line** lists rostered players 5 to 10 under projection.

### Cream Abdul-Yammar: 3

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Josh Giddey | CHI | #3 | 4 | 25.8 / 35.5 | 23.5 | 46.2 | **−22.7** | 46.2 | Active |
| LaMelo Ball | MIN | #2 | 4 | 25.0 / 32.9 | 30.8 | 46.4 | **−15.7** | 41.1 | Active |
| Victor Wembanyama | SA | #1 | 3 | 31.7 / 32.5 | 47.7 | 60.5 | **−12.8** | 59.5 | Active |

- **Giddey** has the league's largest gap.
  - **Minutes** are 10 below projection and **efficiency** is down too: 0.91 FP/min against 1.30. He is shooting 2.8-of-8.2 for 7.0 points.
  - New coach Tiago Splitter has been cutting his minutes at the point, and he has been benched in late-game stretches.
  - Monday at Boston: 24 minutes, 11 points.
- **LaMelo** is mostly a **minutes** problem. His FP/min is 1.23 against 1.41, and he is playing 25.0 minutes against 32.9.
  - Chris Finch wants him at about 30, and has been held back by foul trouble and caution after injury.
  - Monday at Cleveland he played 31 minutes, his most since the opener, but committed **7 turnovers** (−14 FP).
- **Wembanyama** is an **efficiency** problem. His minutes are intact, but he is shooting 6.3-of-17.3 and scoring 20.0 points against 26.9, which costs 13.6 FP/g on scoring alone. His blocks are on projection (4.0 against 3.5).
- **Near the line:** Gobert −9.8, LeBron James −5.5.
  - Gobert went 0-of-9 with 20 rebounds on Monday. His −6.6 FP/g in steals and blocks is the main drag.

### Dr White Slong: 2

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Keegan Murray | SAC | #10 | 2 | 27.0 / 34.1 | 12.0 | 29.3 | **−17.3** | 31.6 | **Out** |
| Matas Buzelis | CHI | #9 | 4 | 24.8 / 30.5 | 20.2 | 32.5 | **−12.3** | 32.7 | Active |

- **Murray** is **injured**. He has left ankle capsulitis in a surgically repaired ankle, and on 26 Oct the Kings set a re-evaluation in **10–14 days**.
- **Buzelis** has both problems. He is 6 minutes light under Splitter's rotation (22 on Monday), and his steals and blocks are worth −4.2.
- **Near the line:** Derrick White −6.0.

### Lauri Birds: 2

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Lauri Markkanen | UTAH | #7 | 4 | 28.5 / 34.0 | 25.5 | 38.7 | **−13.2** | 44.4 | Day-to-day |
| Ivica Zubac | IND | #8 | 3 | 21.7 / 31.1 | 25.3 | 35.5 | **−10.1** | 36.3 | Day-to-day |

- **Markkanen** left Monday's game at Memphis after **6 minutes with a right wrist injury** and did not return. That 2-point game drags both his minutes and his average. No diagnosis has been reported. Before Monday he was already short on scoring.
- **Zubac** sprained his left ankle on 25 Oct at Brooklyn after 7 minutes, which drags his minutes average.
  - X-rays were negative, and he was ruled out on 26 Oct.
  - Rick Carlisle says he is improving and walked in without a boot, but there is no timetable.
  - ESPN has moved him from OUT to day-to-day. His FP/min is on projection.
- **Near the line:**
  - Darius Garland −7.7, Adebayo −7.1, Edey −6.5, Jokić −5.5.
  - **Curry −6.0**: he went 8-of-8 for 24 points on Monday, and his FP/min (1.42) is now *above* projection. His remaining gap is minutes: 26.0 against 32.0, back from his ankle sprain.

### Melbourne poopoo: 2

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Jalen Brunson | NY | #4 | 3 | 34.3 / 35.3 | 29.3 | 43.8 | **−14.5** | 43.1 | Active |
| Anthony Davis | WSH | **#1** | 4 | 33.2 / 32.2 | 39.0 | 49.6 | **−10.6** | 48.5 | Active |

- **Brunson** is an **efficiency** problem at full minutes. He is shooting 8.3-of-21.3, with 3.7 assists against 6.9 (−6.5 FP). The Knicks are 0-3, and he has publicly taken the blame. He went 12-of-28 on 25 Oct.
- **Davis** is a **production** problem. His minutes are on projection, but his blocks are 0.8 against 2.1 and his assists 2.0 against 3.2. Monday: 29 points and 10 rebounds, but 0 assists and 0 blocks.
- **Near the line:** DeRozan −8.8. He had 21 points on Monday, up from −18.8 in the first read.

### Come-in Cider (us): 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Desmond Bane | ORL | #8 | 3 | 31.7 / 33.7 | 21.0 | 38.2 | **−17.2** | 36.9 | Active (bench slot) |

- **Bane** is an **efficiency** problem. His minutes are intact, but his FP/min is 0.66 against 1.14. His assists are 1.3 against 4.8 (−6.9 FP) and his scoring is worth −10.1. Against Minnesota on 23 Oct he went 0-for-5 and fouled out in 27 minutes.
- **Near the line:** Murphy −8.8, Duren −8.7 (IR), Barnes −7.7, Leonard −5.7, Cunningham −5.4.

### Matt Wright's Foxies: 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| Jaren Jackson Jr. | UTAH | #8 | 4 | 26.0 / 31.4 | 27.0 | 38.1 | **−11.1** | 35.9 | Day-to-day |

- **Jackson** left Monday's game at Memphis after **10 minutes with a right knee injury**, when Ty Jerome fell into his knee, and did not return. No diagnosis has been reported.
  - Two of his four games are short ones: he fouled out in 28 minutes in the opener, then had Monday's 10. The two in between were 33 minutes each.
  - His steals and blocks are worth −5.2.
- **Near the line:** **Gilgeous-Alexander −9.1** (#1 on the roster), Miles Bridges −6.9.
  - Gilgeous-Alexander's minutes are intact (34.2). His shortfall is at the line (3.8-of-4.5 against 7.8-of-8.8) and in assists (3.8 against 6.4).

### Team Nic Kerr: 1

| Player | NBA | Rank | GP | Min | Current | Projected | Gap | 2026 | ESPN status |
|---|---|---:|---:|---|---:|---:|---:|---:|---|
| James Harden | CLE | #5 | 3 | 35.0 / 33.6 | 31.0 | 42.1 | **−11.1** | 45.1 | Active |

- **Harden** is an **efficiency** problem at full minutes. He is shooting 4.3-of-12.3 for 15.7 points against 20.6, with 4.3 turnovers against 3.4. Monday: 39 minutes, 7-of-17, 9 assists, 3 turnovers.
- **Near the line:** Alex Sarr −9.1, Dončić −5.3.

### Snow Time Lakers: 0

- **Near the line:** Kyrie Irving −8.5.
  - His FP/min (1.30) is *above* projection (1.28), so the whole gap is minutes: 27.3 against 34.6.
  - He is on a minutes restriction in his return from a torn left ACL (March 2025). On Monday he played 33 minutes, his most so far.

## What is driving the gaps

| Driver | Players | What it means |
|---|---|---|
| **Efficiency at full minutes** | Wembanyama, Brunson, Harden, Davis, Bane | The role is unchanged and the shots are not falling. At 2–4 games this is the noisiest part of any line. |
| **Minutes**, with FP/min near projection | LaMelo, Zubac | The per-minute production holds. LaMelo's minutes have Finch's target of about 30; Zubac's depend on his ankle. |
| **Both** | Giddey, Buzelis | Part role and part shooting. Both minute cuts come from Splitter's rotation in Chicago, which makes them the most structural on the list. |
| **Injured**, or hurt on Monday | Keegan Murray (re-evaluation in 10–14 days), Zubac (no timetable), Markkanen (right wrist, 26 Oct), Jackson (right knee, 26 Oct) | Markkanen's and Jackson's averages each include a game cut short by injury. |

Players on rosters who have **not played yet**: AJ Dybantsa (Snow Time Lakers, projected 32.9), Kon Knueppel (Team Nic Kerr, 35.2) and Brandon Ingram (Melbourne poopoo, 38.5). All three are listed OUT.

## What changed from the first read

The 01:30 UTC read caught seven of Monday's games in progress and came before GS @ DEN tipped off, so Curry's and DeRozan's Monday games were missing from it completely. **Seven players dropped below the 10-point line** once the games finished:

| Player | Team | First read | Final | Monday final line |
|---|---|---:|---:|---|
| DeMar DeRozan | Melbourne poopoo | −18.8 | **−8.8** | 29 min, 21 pts, 7-15 FG |
| Miles Bridges | Matt Wright's Foxies | −12.9 | **−6.9** | 32 min, 17 pts, 8 reb |
| Stephen Curry | Lauri Birds | −10.5 | **−6.0** | 27 min, 24 pts, 8-8 FG |
| Shai Gilgeous-Alexander | Matt Wright's Foxies | −13.1 | **−9.1** | 30 min, 26 pts, 11-18 FG |
| Kyrie Irving | Snow Time Lakers | −11.5 | **−8.5** | 33 min, 18 pts, 6 reb, 6 ast |
| Bam Adebayo | Lauri Birds | −10.1 | **−7.1** | 30 min, 8 pts, 8 reb, 2 stl, 2 blk |
| Rudy Gobert | Cream Abdul-Yammar | −12.3 | **−9.8** | 36 min, 5 pts, 0-9 FG, 20 reb |

Two players who stayed on the list moved:

- **LaMelo** got worse, from −14.9 to −15.7, on Monday's 7 turnovers.
- **Buzelis** improved slightly, from −13.5 to −12.3.

## Below the line on last season, not on projection

These players are **10+ under their 2026 average** but within 10 of ESPN's projection. Three of them are ours.

| Player | Team | GP | Min | Current | Projected | 2026 |
|---|---|---:|---|---:|---:|---:|
| Scottie Barnes | **us** | 3 | 30.3 / 33.8 | 36.0 | 43.7 | 47.3 |
| Jalen Duren | **us** (IR) | 2 | 19.0 / 31.0 | 33.5 | 42.2 | 44.3 |
| Trey Murphy III | **us** | 3 | 33.3 / 32.5 | 28.0 | 36.8 | 41.6 |
| Nikola Jokić | Lauri Birds | 3 | 38.0 / 35.6 | 61.7 | 67.2 | 74.9 |
| Bam Adebayo | Lauri Birds | 4 | 30.8 / 32.4 | 32.5 | 39.6 | 42.7 |
| Zach Edey | Lauri Birds | 3 | 21.3 / 26.4 | 26.7 | 33.2 | 39.5 |
| Rudy Gobert | Cream Abdul-Yammar | 4 | 32.5 / 32.5 | 24.5 | 34.3 | 38.2 |
| DeMar DeRozan | Melbourne poopoo | 3 | 27.0 / 28.9 | 21.0 | 29.8 | 32.7 |
| Alex Sarr | Team Nic Kerr | 4 | 24.5 / 28.6 | 27.5 | 36.6 | 39.4 |

## Context for our pending trade

The open offer to Melbourne poopoo sends VanVleet and Leonard for Brunson and Castle. Here is where all four stand:

| Player | Side | GP | Min | Current | Projected | Gap | ESPN status |
|---|---|---:|---|---:|---:|---:|---|
| Jalen Brunson | we receive | 3 | 34.3 / 35.3 | 29.3 | 43.8 | **−14.5** | Active |
| Stephon Castle | we receive | 3 | 29.7 / 32.7 | 37.3 | 36.9 | +0.5 | Active |
| Kawhi Leonard | we send | 2 | 26.0 / 32.8 | 40.0 | 45.7 | −5.7 | Day-to-day |
| Fred VanVleet | we send | 3 | 30.3 / 32.2 | 32.0 | 33.4 | −1.4 | Active |

- Brunson's shortfall comes at full minutes, so it is a shooting slump and not a role change.
- VanVleet's final Monday line moved him from −4.4 in the first read to −1.4, at 30.3 minutes.
- Leonard is *above* projection per minute (1.54 against 1.39); his gap is minutes.

## Sources

- ESPN fantasy API, league 423671879, `mRoster`, `mTeam` and `mSettings` views, read 27 Oct 2026 04:55 UTC. The scoring period 7 split was re-scored against the ESPN NBA box scores for 26 Oct (scoreboard `dates=20261026`; all nine games `STATUS_FINAL`).
- Markkanen and Jackson: [ESPN, 26 Oct](https://www.espn.com/nba/story/_/id/50293720/jazz-lauri-markkanen-jaren-jackson-jr-exit-early-vs-grizzlies); [WTOP/AP](https://wtop.com/sports/2026/10/jazz-forwards-lauri-markkanen-and-jaren-jackson-jr-exit-early-with-injuries-against-grizzlies/); [KSL Sports](https://sports.ksl.com/sports/jaren-jackson-jr-lauri-markkanen-injury/578519); [RotoWire](https://www.rotowire.com/basketball/headlines/jaren-jackson-injury-wont-return-monday-536242)
- Zubac: [NBC Sports, 26 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/ivica-zubac-ankle-with-no-timetable-for-return); [iPacers](https://ipacers.com/2026/10/26/indiana-pacers-injury-report-ivica-zubac-leaves-on-crutches-after-pacers-win-in-brooklyn/); [Basketnews](https://basketnews.com/news-258127-ivica-zubac-injury-pacers-coach-drops-encouraging-news-after-exit-vs-nets.html)
- Keegan Murray: [HoopsHype, 26 Oct](https://www.hoopshype.com/story/sports/nba/rumors/2026/10/26/sacramento-kings-say-keegan-murray-left-ankle/92451271007/); [The Kings Herald](https://kingsherald.com/articles/kings-provide-medical-update-on-keegan-murray-maxime-raynaud-and-dylan-cardwell/)
- Giddey and Buzelis: [Yahoo Sports](https://sports.yahoo.com/articles/josh-giddey-playing-tonight-why-044402357.html); [Yahoo Sports, Splitter's rotation](https://sports.yahoo.com/articles/first-bulls-win-told-us-205314450.html); [RotoWire](https://www.rotowire.com/basketball/player/josh-giddey-5366)
- LaMelo Ball: [Star Tribune](https://www.startribune.com/minnesota-timberwolves-toronto-raptors-target-center-lamelo-ball-stats-anthony-edwards-chris-finch/601902946); [ESPN recap, 25 Oct](https://www.espn.com/nba/recap/_/gameId/401909864)
- Irving: [CBS Sports, minutes restriction](https://www.cbssports.com/fantasy/basketball/news/mavericks-kyrie-irving-will-be-on-minutes-restriction-friday/); [NBC Sports, 23 Oct](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-23/kyrie-irving-to-be-under-minutes-limit-friday)
- Curry: [HoopsHype, 25 Oct](https://hoopshype.com/story/sports/nba/rumors/2026/10/25/stephen-curry-set-to-return-monday-for-struggling-warriors/92436269007); [SF Chronicle](https://www.sfchronicle.com/sports/warriors/article/warriors-steph-curry-suffers-apparent-injury-22482932.php)
- Brunson: [Yahoo Sports, 0-3 start](https://sports.yahoo.com/articles/knicks-jalen-brunson-makes-honest-203044292.html); [Hoops Rumors](https://www.hoopsrumors.com/2026/10/knicks-notes-brunson-drummond-brown-knecht-mccullar.html)
- Bane: [CBS Sports, fouls out in 27 minutes](https://www.cbssports.com/fantasy/basketball/news/magics-desmond-bane-fouls-out-in-27-minutes/); [Yahoo Sports](https://sports.yahoo.com/articles/desmond-bane-playing-tonight-why-031020637.html)
