# Trade watch: 25 Nov 2026

- Generated 2026-11-25 09:06 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 26 Oct to 25 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 8 GP, 16.5 min, 9.5 FP/g, started 0 | 9.7 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **9.7** · season 6.7 (16) · L7 11.0 (4) · L15 9.5 (8) · L30 6.9 (14) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 8 GP, 16.5 min, 9.5 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (8 games without him, against 2 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| Dylan Cardwell | C | Free agent | 14.8 / 14.0 | 14.4 / 21.5 | 2 of 8 | 13.3 |
| Alex Karaban | SF/PF | Free agent | 11.3 / 11.0 | 3.3 / 2.0 | 0 of 3 | 1.9 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 36.4 / 37.5 | 36.5 / 46.0 | 8 of 8 | 35.7 |
| De'Andre Hunter | SF/PF | Free agent | 36.9 / 38.0 | 32.7 / 15.0 | 7 of 7 | 32.0 |
| Precious Achiuwa | PF/C | Free agent | 18.0 / 19.5 | 14.6 / 21.0 | 2 of 5 | 16.7 |
| Keegan Murray | SF/PF | Free agent | 32.2 / 34.1 | 26.1 / 29.3 | 6 of 8 | 26.8 |
| Domantas Sabonis | PF/C | Team Nic Kerr | 30.3 / 33.0 | 38.1 / 40.5 | 7 of 7 | 43.8 |
| Zach LaVine | SG/SF | Dr White Slong | 32.1 / 35.0 | 33.0 / 26.5 | 7 of 7 | 32.7 |

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
| Jared McCain | PG/SG | Free agent | 10 GP, 30.3 min, 29.2 FP/g, started 9 | 24.0 |
| Ajay Mitchell | PG/SG | Lauri Birds | 8 GP, 28.6 min, 26.6 FP/g, started 8 | 26.1 |
| Kenrich Williams | SF | Free agent | 10 GP, 24.4 min, 25.4 FP/g, started 6 | 26.8 |
| Alex Caruso | PG/SG | Free agent | 7 GP, 19.3 min, 18.6 FP/g, started 1 | 15.3 |
| Micah Peavy | SF | Free agent | 8 GP, 18.9 min, 12.9 FP/g, started 2 | 12.7 |
| Brooks Barnhizer | SF | Free agent | 6 GP, 8.3 min, 9.2 FP/g, started 0 | 10.9 |

- **Whose minutes he takes** (8 games with him, 2 before him): minutes before / with him.

  - Bennett Stirtz (Free agent): 26.5 → 20.6 min
  - Micah Peavy (Free agent): 20.5 → 18.3 min

### Research

- _pending_

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-25 09:06 UTC.
