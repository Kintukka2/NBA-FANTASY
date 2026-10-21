# Opening night report: Tue 20 Oct 2026 (Wed 21 Oct in Australia)

- Prepared 21 Oct 2026, 07:30 UTC, by Claude. This is **a report, not a council verdict**.
- **Sources:**
  - League 423671879 read live through `council/espn_sync.py` and the ESPN fantasy API for scoring period 1.
  - ESPN NBA box scores for the three games.
- **Scoring check:** every player line below was re-scored with `scripts/league_scoring.py`, including the DD/TD bonuses, and **matches ESPN's fantasy points exactly**.

## Matchup 1 after day 1

| Matchup | Score |
|---|---|
| **Come-in Cider (us) vs Cream Abdul-Yammar** | **155 – 132** |
| Team Nic Kerr vs Melbourne poopoo | 104 – 168 |
| Matt Wright's Foxies vs Snow Time Lakers | 106 – 120 |
| Lauri Birds vs Dr White Slong | 51 – 85 |

We lead by 23. Our 155 was the second-highest score in the league after Melbourne's 168. Only three of our players had a game, and all three started.

## Our players

| Slot | Player | Line | FP |
|---|---|---|---:|
| SF | **Paul George** (BOS) | 31 min, 38 pts, 12-21 FG, **7-12 3P**, 7-8 FT, 5 reb, 3 ast, **5 stl**, 0 blk, 3 TO | **72** |
| C | Jalen Duren (DET) | 28 min, 22 pts, 8-13 FG, 6-7 FT, 9 reb (3 off), 1 ast, 1 stl, 1 blk, 1 TO | 44 |
| PG | Cade Cunningham (DET) | 35 min, 22 pts, 8-18 FG, 1-6 3P, 5-5 FT, 4 reb, 8 ast, 1 stl, 1 blk, **5 TO** | 39 |

- **Paul George had the best fantasy line of the night across the whole league (72).** That beat Shai Gilgeous-Alexander's 69 and Tyrese Maxey's 63. His 5 steals alone were worth 20 points.
  - He is the same player the council voted on 20 Oct to package to the Snow Time Lakers for Clingan. That trade was not made, and George stays.
- **Duren** was efficient: 8-13 from the field, 3 offensive rebounds, and only 1 turnover.
- **Cade's** 5 turnovers cost 10 points. Detroit beat Boston 121-113.

## Cream Abdul-Yammar's players (our opponent)

| Slot | Player | Line | FP |
|---|---|---|---:|
| C | Victor Wembanyama (SA) | 34 min, 12 pts, **1-13 FG**, 10-12 FT, 13 reb, 3 ast, 1 stl, **6 blk**, 4 TO | 43 |
| SF | LeBron James (PHI) | 34 min, 14 pts, 5-13 FG, 4-6 FT, 9 reb, 7 ast, 1 stl, 1 blk, 1 TO | 39 |
| PG | Payton Pritchard (BOS) | 28 min, 17 pts, 4-9 FG, 2-5 3P, 7-8 FT, 4 reb, 1 ast | 25 |
| PF | OG Anunoby (NY) | 32 min, 10 pts, 3-12 FG, 1-9 3P, 5 reb, 1 stl, 1 blk, 2 TO | 15 |
| SG | Mikal Bridges (NY) | 33 min, 4 pts, 2-8 FG, 3 reb, 1 ast, 1 blk | 10 |

- Wembanyama shot 1 for 13 and still scored 43. Six blocks at 4 points each carried him.
- After the game, Cream **dropped Pritchard and added Zach LaVine**.

## The NBA games

| Final | Fantasy notes |
|---|---|
| **DET 121, BOS 113** | George 72 (BOS), Duren 44, Cade 39. Free agents Javonte Green (19 pts, 5-8 3P) and Duncan Robinson (21 pts) came off Detroit's bench. |
| **PHI 106, NY 100** | Maxey 63 (Team Nic Kerr), Embiid 47 and Brown 45 (Snow Time), Towns 46 (Melbourne). LeBron 39 in his Philadelphia debut. Free agent Andre Drummond had **14 reb (7 off)**. |
| **OKC 116, SA 104** | Gilgeous-Alexander 69 (Foxies), Holmgren 41 (Team Nic Kerr), Wembanyama 43. Free agent Jared McCain shot 6-8 from three for 20 points. |

No rostered fantasy player missed a game. All 16 DNPs were coach's decisions on undrafted players.

### Top fantasy lines of the night

1. Paul George (us): 72
2. Shai Gilgeous-Alexander (Foxies): 69
3. Tyrese Maxey (Team Nic Kerr): 63
4. Andre Drummond (**free agent**): 51
5. Joel Embiid (Snow Time): 47
6. Karl-Anthony Towns (Melbourne): 46
7. Jaylen Brown (Snow Time): 45
8. Jalen Duren (us): 44

## Waiver watch: free agents who played

| Player | Team | FP | Line |
|---|---|---:|---|
| Andre Drummond | NY | **51** | 24 min, 12 pts, **14 reb (7 off)**, 4 ast, 1 stl, 2 blk, 0 TO |
| Jared McCain | OKC | 37 | 22 min, 20 pts, 7-9 FG, 6-8 3P, 1 stl |
| Julian Champagnie | SA | 34 | 30 min, 8 pts, 2 stl, **3 blk**, 0 TO |
| Javonte Green | DET | 29 | 18 min, 19 pts, 5-8 3P |
| Duncan Robinson | DET | 28 | 28 min, 21 pts, 5-9 3P |

- These are single-game lines, not evidence of a role. Drummond's line came in 24 minutes behind Towns.
- Andrew Wiggins (MIA) and Kyshawn George (WSH) have not played yet. Andrew Nembhard has since been picked up by Matt Wright's Foxies.

## Roster sync

- **`council/roster.csv` matches ESPN.** No trades or adds were made, and Butler is still on IR.
- **Moves across the league, now reflected in `council/taken.txt`:**

  | Team | Added | Dropped |
  |---|---|---|
  | Cream Abdul-Yammar | Zach LaVine | Payton Pritchard |
  | Matt Wright's Foxies | Andrew Nembhard | |
  | Melbourne poopoo | CJ McCollum | |
  | Team Nic Kerr | Jalen Green | |
  | Snow Time Lakers | Peyton Watson | |

## Rest of the week

This assumes ESPN's standard Monday-to-Sunday week, so matchup 1 ends Sun 25 Oct (scoring periods 1-6).

- **Today's lineup is set correctly.** All 9 of our players with a game on Wed 21 Oct are in starting slots. Cade, Duren, Jamal Murray and George have no game today.
- **Games per day:**

| Day | Our players with a game | Cream's players with a game |
|---|---:|---:|
| Wed 21 | 9 | 9 |
| Thu 22 | 1 | 1 |
| Fri 23 | 12 (10 can start) | 12 (10 can start) |
| Sat 24 | **7** | 4 |
| Sun 25 | **5** | **10** |

- **Projection:**
  - Method: each player's 2026 FP/g, or projection plus blind spot for players with under 20 games, times the starts available each day, ignoring position eligibility.
  - Result: **about 1,470 for us against about 1,525 for Cream**. That would be a roughly 55-point deficit despite today's lead.
- **Sunday decides the week.**
  - Cream has 10 players with games on Sun 25: LaMelo Ball, Reaves, LeBron, Bridges, Franz Wagner, Keyonte George, Gobert, Anunoby, Quickley and LaVine.
  - We have 5: Cade, Barnes, Duren, Kawhi and Bane, which leaves **five starting slots empty**.
  - We are ahead on Saturday, 7 to 4.
  - Our Sunday gap is the main lever for any streaming adds this week. Whether to use an add, and who to drop, is a decision for you or the council.
