# Trade watch: 12 Nov 2026

- Generated 2026-11-12 06:05 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 13 Oct to 12 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 2 GP, 18.0 min, 9.0 FP/g, started 0 | 6.7 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **6.7** · season 4.9 (10) · L7 7.5 (4) · L15 4.8 (8) · L30 4.9 (10) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 2 GP, 18.0 min, 9.0 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (3 games without him, against 7 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| Dylan Cardwell | C | Free agent | 23.5 / 14.0 | 22.0 / 21.5 | 1 of 2 | 22.1 |
| Precious Achiuwa | PF/C | Waivers | 29.7 / 24.6 | 27.3 / 27.3 | 3 of 3 | 26.2 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 38.3 / 37.1 | 47.7 / 43.9 | 3 of 3 | 45.8 |
| Zach LaVine | SG/SF | Team Nic Kerr | 32.7 / 32.6 | 41.0 / 28.4 | 3 of 3 | 32.3 |
| Daeqwon Plowden | SG | Free agent | 10.0 / 11.0 | 5.3 / 4.2 | 0 of 3 | 5.0 |
| De'Andre Hunter | SF/PF | Free agent | 31.3 / 33.5 | 17.3 / 22.5 | 3 of 3 | 20.2 |
| Keegan Murray | SF/PF | Free agent | 23.5 / 26.0 | 25.0 / 18.0 | 0 of 2 | 24.7 |
| Emanuel Sharp | SG | Free agent | 15.0 / 19.6 | 8.3 / 10.1 | 0 of 3 | 10.5 |

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
| Ajay Mitchell | PG/SG | Lauri Birds | 9 GP, 28.2 min, 36.1 FP/g, started 8 | 32.8 |
| Jared McCain | PG/SG | Free agent | 10 GP, 27.4 min, 22.2 FP/g, started 6 | 24.0 |
| Kenrich Williams | SF | Free agent | 10 GP, 21.6 min, 15.7 FP/g, started 8 | 15.5 |
| Alex Caruso | PG/SG | Free agent | 7 GP, 18.9 min, 23.1 FP/g, started 1 | 20.4 |
| Micah Peavy | SF | Free agent | 8 GP, 16.9 min, 9.6 FP/g, started 0 | 10.4 |
| Brooks Barnhizer | SF | Free agent | 6 GP, 6.8 min, 5.8 FP/g, started 0 | 6.9 |

- **Whose minutes he takes** (2 games with him, 8 before him): minutes before / with him.

  - Brooks Barnhizer (Free agent): 7.2 → 5.0 min

### Research

- _pending_

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-12 06:05 UTC.
