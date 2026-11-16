# Trade watch: 15 Nov 2026

- Generated 2026-11-16 04:42 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 16 Oct to 15 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## What it means for us

- **Pickups:** none.
- **Threats to our players:** none.
- **Overrides:** Dejounte Murray's floor (23 Nov) is recorded in the news watch.
- **New trades:** none.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 4 GP, 18.0 min, 8.0 FP/g, started 0 | 7.3 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **7.3** · season 5.2 (12) · L7 8.0 (4) · L15 6.1 (8) · L30 5.2 (12) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 4 GP, 18.0 min, 8.0 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (4 games without him, against 6 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| Alex Karaban | SF/PF | Free agent | 29.0 / 11.0 | 10.0 / 2.2 | 0 of 1 | 5.9 |
| Dylan Cardwell | C | Free agent | 19.8 / 14.0 | 20.5 / 21.5 | 2 of 4 | 21.1 |
| Daeqwon Plowden | SG | Free agent | 10.0 / 8.0 | 6.8 / 3.0 | 0 of 4 | 7.2 |
| Precious Achiuwa | PF/C | Free agent | 25.0 / 24.3 | 20.0 / 26.3 | 2 of 2 | 24.7 |
| De'Andre Hunter | SF/PF | Free agent | 35.7 / 35.2 | 27.7 / 24.4 | 3 of 3 | 23.6 |
| Malik Monk | PG/SG | Free agent | 17.8 / 17.8 | 17.0 / 19.2 | 1 of 4 | 18.1 |
| Zach LaVine | SG/SF | Team Nic Kerr | 31.3 / 31.5 | 34.0 / 27.3 | 3 of 3 | 33.1 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 36.8 / 37.2 | 38.0 / 45.8 | 4 of 4 | 38.7 |

### The team he joined: OKC

- **Long absences at his positions** (SF/SG):

| Player | Pos | Injury | ESPN est. | Min/g this season | FP/g |
|---|---|---|---|---:|---:|
| Jalen Williams | SF/PF | Left Leg Fracture | 02 Mar | 31.7 | 26.3 |
| Cason Wallace | PG/SG | Left Shoulder Surgery | 02 Mar | 16.3 | 18.7 |

- About **48 minutes a game** at his positions are out long-term (their season or last-season minutes).
- **Depth at his positions**, last 10 games:

| Player | Pos | League | Role | Rate |
|---|---|---|---|---:|
| Ajay Mitchell | PG/SG | Lauri Birds | 8 GP, 28.5 min, 33.1 FP/g, started 8 | 31.1 |
| Jared McCain | PG/SG | Free agent | 10 GP, 28.4 min, 23.3 FP/g, started 7 | 22.9 |
| Kenrich Williams | SF | Free agent | 10 GP, 23.9 min, 19.8 FP/g, started 9 | 19.3 |
| Alex Caruso | PG/SG | Free agent | 7 GP, 20.9 min, 20.1 FP/g, started 1 | 22.2 |
| Micah Peavy | SF | Free agent | 9 GP, 16.4 min, 10.1 FP/g, started 0 | 9.1 |
| Brooks Barnhizer | SF | Free agent | 6 GP, 7.0 min, 6.5 FP/g, started 0 | 6.0 |

- **Whose minutes he takes** (4 games with him, 6 before him): minutes before / with him.

  - Bennett Stirtz (Free agent): 23.5 → 18.0 min
  - Brooks Barnhizer (Free agent): 8.2 → 4.5 min
  - Micah Peavy (Free agent): 17.0 → 15.3 min
  - Ajay Mitchell (Lauri Birds): 28.8 → 27.5 min

### Research

- **No trades completed since 13 Nov.** The [Hoops Rumors transactions log](https://www.hoopsrumors.com/transactions) still ends at Clifford (8 Nov).
- **Dejounte Murray** (NOP) requested a trade and is sitting out. Phoenix denies talks ([Suns On SI via Yahoo, 14 Nov](https://sports.yahoo.com/articles/insider-downplays-suns-trade-rumors-140009986.html)); Jalen Green is available but no negotiation is reported ([Heavy, 14 Nov](https://heavy.com/sports/nba/new-orleans-pelicans/pelicans-dejounte-murray-jalen-green-trade/)).
- **No rotation releases**, only two-way moves ([Hoops Rumors, 15 Nov](https://www.hoopsrumors.com/2026/11/hawks-to-waive-gilbert-sign-castro-to-two-way-deal.html)).

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-16 04:42 UTC.
- [Hoops Rumors transactions log](https://www.hoopsrumors.com/transactions)
- [Suns On SI via Yahoo, 14 Nov](https://sports.yahoo.com/articles/insider-downplays-suns-trade-rumors-140009986.html)
- [Heavy, 14 Nov](https://heavy.com/sports/nba/new-orleans-pelicans/pelicans-dejounte-murray-jalen-green-trade/)
- [Hoops Rumors, 15 Nov](https://www.hoopsrumors.com/2026/11/hawks-to-waive-gilbert-sign-castro-to-two-way-deal.html)
