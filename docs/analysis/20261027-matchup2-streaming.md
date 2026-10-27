# Matchup 2 streaming plan: Come-in Cider vs Team Nic Kerr

- Prepared 27 Oct 2026, 09:00 UTC, by Claude. This is **a report, not a council verdict**.
- **Matchup 2** runs Mon 26 Oct to Sun 1 Nov (US dates). After Monday we trail **229 to 270**.
- **Rules that shape it:**
  - 10 starters a day: PG, SG, SF, PF, C, G, F and 3 UTIL.
  - The bench is 3 deep, and IR holds 1 (Duren).
  - Adds are capped at 1 per scoring period, so 7 this matchup. We have used 1 (Pritchard), which leaves **6**.
  - Free agents can be added at once. Waiver players take 24 hours.
- **Method:** for each remaining day, an exact lineup optimiser fills the 10 slots from the players with a game that day.
  - Rate per game: 70% this season's FP/g and 30% last season's (or ESPN's projection) once a player has 3 or more games. With fewer games, it is 50/50.
  - Every FP/g is re-scored with `scripts/league_scoring.py` (0 mismatches across 1,099 pool players).
  - A player listed OUT is left out until ESPN's estimated return date.
  - The value of a streamer is the change in the optimised lineup total.

## The week, day by day

Players with a game each day (US date / Melbourne date). There are 10 slots.

| Day (US) | Melbourne | Ours | Theirs | What it means for us |
|---|---|---:|---:|---|
| Tue 27 | Wed 28 | 4 | 5 | 6 open slots |
| Wed 28 | Thu 29 | **11** | 9 | **overfull: one of ours sits, so a streamer adds ~0** |
| Thu 29 | Fri 30 | **2** | 5 | **8 open slots** |
| Fri 30 | Sat 31 | **11** | 7 | overfull: one sits |
| Sat 31 | Sun 1 | **3** | 9 | **7 open slots** |
| Sun 1 | Mon 2 | 6 | 2 | 4 open slots |

Our players' remaining games (x = plays):

| Player | NBA | Rate | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|
| Cade Cunningham | DET | 47.5 | x | x |  | x |  |  |
| Kawhi Leonard (day-to-day, left knee inflammation, no timetable reported; ESPN est. 28 Oct) | TOR | 45.0 |  | x |  | x |  | x |
| Dejounte Murray | NO | 44.8 |  | x | x |  | x |  |
| Jamal Murray | DEN | 44.4 |  | x |  | x |  |  |
| Scottie Barnes | TOR | 39.4 |  | x |  | x |  | x |
| Paul George | BOS | 39.3 | x |  |  | x |  | x |
| Yaxel Lendeborg | GS | 39.2 |  | x |  | x |  | x |
| Caleb Wilson | CHI | 36.4 |  | x |  | x |  |  |
| Fred VanVleet | HOU | 32.4 |  | x |  | x | x |  |
| Trey Murphy III | NO | 32.1 |  | x | x |  | x |  |
| Payton Pritchard | BOS | 30.2 | x |  |  | x |  | x |
| Paul Reed | DET | 28.9 | x | x |  | x |  |  |
| Desmond Bane | ORL | 25.8 |  | x |  | x |  | x |
| *Jalen Duren (IR)* | DET | — | out: hamstring, re-evaluated in 2 weeks; ESPN est. 9 Nov | | | | | |

**Projection as rostered:** we score about 1,324 more and they score about 1,528, for a final of **~1,553 to ~1,798**. Their Saturday (9 playing) and Wednesday (9) are their big days.

## Pritchard's slot

Boston plays Tue, Fri and Sun.

| Day | Pritchard's value |
|---|---:|
| Tue | 30 |
| Wed | — (Boston idle) |
| Thu | — (Boston idle) |
| Fri | 4 (we are overfull) |
| Sat | — (Boston idle) |
| Sun | 30 |
| **Week** | **≈ 65** |

**A streamer for Wed 28 and Thu 29 only gains on Thursday.** On Wednesday we already have 11 players for 10 slots. Streaming is worth most on a team that plays **Thu 29 and Sat 31**, our two emptiest days. Sacramento and Portland also play Tue 27, which is a third light day.

| Free agent | NBA | Games left | Now: GP, min, FP/g | 2026 FP/g | Owned | vs keeping Pritchard |
|---|---|---|---|---:|---:|---:|
| **Precious Achiuwa** | SAC | Tue, Thu, Sat | 3, 31.3, 36.7 | 27.0 | 23% | **+36.5** |
| Toumani Camara | POR | Tue, Thu, Sat | 2, 25.0, 36.0 | 28.8 | 35% | +32.4 |
| Jrue Holiday | POR | Tue, Thu, Sat | 2, 23.5, 29.5 | 34.9 | 29% | +31.8 |
| Jaylen Wells | MEM | Thu, Sat | 4, 29.0, 31.8 | 21.7 | 21% | −7.4 |
| Aaron Wiggins | ATL | Wed, Thu, Sat | 4, 27.5, 31.5 | 19.4 | 24% | −9.1 |
| CJ McCollum | ATL | Wed, Thu, Sat | 4, 26.8, 28.2 | 32.7 | 76% | −5.7 |

- **Achiuwa** has started since Keegan Murray went out. Murray (left ankle capsulitis) is re-evaluated in 10–14 days from 26 Oct (ESPN est. 6 Nov), and Raynaud is re-evaluated in two weeks (ESPN est. 10 Nov). His role should outlast this week, and Sacramento plays 4 games next week.
- **The players who lose to Pritchard** do so because two-game teams can't replace both of his Tue and Sun games.
- **Julian Reese** (NO) looked good on paper, from last season only. He has not played this season.
- **Jaxson Hayes** (right shoulder soreness, next chance Wed; ESPN est. 28 Oct): Utah plays Wed and Sat only.

## Plan

**1. Now: drop Pritchard, add Achiuwa (+36.5, 1 add).**

- Do it before Sacramento's Tuesday tip-off: 8:00 pm ET, which is **11:00 am Wed 28 in Melbourne**.
- Achiuwa's Tuesday game replaces Pritchard's, and Achiuwa then covers Thursday and Saturday.

| Day (US) | Lineup total | Playing | Sits |
|---|---:|---:|---|
| Tue 27 | 149 | 4 | — |
| Wed 28 | 390 | 11 | **Bane** (if Leonard plays) |
| Thu 29 | 111 | 3 | — |
| Fri 30 | 378 | 10 | — |
| Sat 31 | 143 | 4 | — |
| Sun 1 | 189 | 5 | — |

**2. Optional, for about +30 more: after Reed's Friday game, drop Reed for a Sunday streamer.**

| Sunday streamer | NBA | Now: GP, min, FP/g | Sunday tip-off (ET / Melbourne) |
|---|---|---|---|
| Ja'Kobe Walter | TOR | 3, 26.0, 34.7 | 9:00 pm / 1:00 pm Mon 2 |
| Obi Toppin | IND | 4, 23.2, 31.5 | 5:00 pm / 9:00 am Mon 2 |
| Derrick Jones Jr. | LAC | 3, 30.3, 28.7 | 8:30 pm / 12:30 pm Mon 2 |
| Isaiah Jackson | LAC | 3, 22.3, 29.3 | 8:30 pm / 12:30 pm Mon 2 |

- Detroit's last game this week is Friday, so Reed has nothing left to give this matchup after it.
- The cost is next week. Duren (ESPN est. 9 Nov) isn't back, so Achiuwa would be our only C-eligible player until he is.
- Cutting Achiuwa instead after Saturday scores the same this week, but throws away his next week.

**With both moves:** about 1,619 for us against about 1,798 for them. The plan narrows the gap. On current rates it does not close it.

What would swing it:

- Leonard's knee: day-to-day, no timetable reported; ESPN est. 28 Oct. He has Wed, Fri and Sun games.
- Chet Holmgren for Team Nic Kerr: patellar tendinitis, next chance Wed vs DAL; ESPN est. 28 Oct.
- Kon Knueppel for Team Nic Kerr: left hamstring, no timetable reported; ESPN est. 31 Oct.

Caleb Wilson and Bane add the least *this* week, because all their games fall on our full days. They are long-term pieces, not streaming fodder.

## Sources

- ESPN fantasy API, league 423671879 (`mRoster`, `mTeam`, `mSettings`, `mMatchupScore`, `kona_player_info`, `proTeamSchedules_wl`), and ESPN's NBA injury feed, read 27 Oct 2026 08:50 UTC.
- Murray, Raynaud and Cardwell: [HoopsHype, 26 Oct](https://hoopshype.com/story/sports/nba/rumors/2026/10/26/sacramento-kings-say-keegan-murray-left-ankle/92451271007)
- Achiuwa's start: [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/precious-achiuwa-posts-double-double-in-spot-start)
- Holmgren: [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/chet-holmgren-knee-out-monday-vs-suns)
- Duren: [ESPN](https://www.espn.com/nba/story/_/id/50277066/pistons-jalen-duren-hamstring-strain-least-2-weeks)
- Hayes: [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/jazzs-jaxson-hayes-wont-play-monday/)
