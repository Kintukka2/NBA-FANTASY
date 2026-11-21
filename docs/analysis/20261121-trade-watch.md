# Trade watch: 21 Nov 2026

- Generated 2026-11-21 07:20 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 22 Oct to 21 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 6 GP, 16.7 min, 9.5 FP/g, started 0 | 9.3 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **9.3** · season 6.3 (14) · L7 9.8 (4) · L15 9.9 (7) · L30 6.3 (14) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 6 GP, 16.7 min, 9.5 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (6 games without him, against 4 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| Alex Karaban | SF/PF | Free agent | 16.5 / 10.5 | 5.0 / 0.5 | 0 of 2 | 4.0 |
| Daeqwon Plowden | SG | Free agent | 8.8 / 3.5 | 5.6 / 2.0 | 0 of 5 | 7.3 |
| Zach LaVine | SG/SF | Team Nic Kerr | 33.0 / 29.8 | 36.2 / 23.0 | 5 of 5 | 35.5 |
| Dylan Cardwell | C | Free agent | 16.8 / 14.0 | 17.5 / 21.5 | 2 of 6 | 17.9 |
| De'Andre Hunter | SF/PF | Free agent | 35.8 / 35.3 | 30.8 / 15.3 | 5 of 5 | 30.2 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 36.3 / 37.2 | 40.8 / 45.8 | 6 of 6 | 38.0 |
| Precious Achiuwa | PF/C | Free agent | 19.3 / 22.8 | 12.3 / 24.0 | 2 of 3 | 13.2 |
| Domantas Sabonis | PF/C | Team Nic Kerr | 30.0 / 33.8 | 34.8 / 39.5 | 5 of 5 | 43.0 |

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
| Ajay Mitchell | PG/SG | Lauri Birds | 8 GP, 29.9 min, 29.9 FP/g, started 8 | 29.1 |
| Jared McCain | PG/SG | Free agent | 10 GP, 29.0 min, 26.5 FP/g, started 7 | 25.2 |
| Kenrich Williams | SF | Free agent | 10 GP, 25.2 min, 22.6 FP/g, started 7 | 23.8 |
| Alex Caruso | PG/SG | Free agent | 8 GP, 19.4 min, 18.2 FP/g, started 1 | 19.5 |
| Micah Peavy | SF | Free agent | 8 GP, 17.2 min, 11.6 FP/g, started 0 | 9.8 |
| Brooks Barnhizer | SF | Free agent | 4 GP, 5.5 min, 6.0 FP/g, started 0 | 5.4 |

- **Whose minutes he takes** (6 games with him, 4 before him): minutes before / with him.

  - Jaylin Williams (Free agent): 20.0 → 12.5 min
  - Micah Peavy (Free agent): 20.8 → 13.8 min
  - Bennett Stirtz (Free agent): 21.8 → 19.0 min
  - Brooks Barnhizer (Free agent): 6.5 → 4.5 min

### Research

- _pending_

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-21 07:20 UTC.
