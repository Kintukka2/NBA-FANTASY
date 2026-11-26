# Trade watch: 26 Nov 2026

- Generated 2026-11-26 06:13 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 27 Oct to 26 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 9 GP, 16.0 min, 8.2 FP/g, started 0 | 8.3 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **8.3** · season 6.2 (17) · L7 8.4 (5) · L15 8.2 (9) · L30 6.3 (15) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 9 GP, 16.0 min, 8.2 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (9 games without him, against 1 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| De'Andre Hunter | SF/PF | Free agent | 37.1 / 27.6 | 32.9 / 23.9 | 8 of 8 | 32.2 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 36.4 / 33.0 | 36.0 / 46.0 | 9 of 9 | 35.3 |
| Domantas Sabonis | PF/C | Team Nic Kerr | 31.1 / 31.0 | 41.2 / 40.0 | 8 of 8 | 46.1 |
| Keegan Murray | SF/PF | Free agent | 33.3 / 34.1 | 26.3 / 29.3 | 7 of 9 | 26.9 |
| Dylan Cardwell | C | Free agent | 14.1 / 15.0 | 13.4 / 24.0 | 2 of 9 | 12.6 |
| Alex Karaban | SF/PF | Free agent | 9.0 / 11.0 | 2.5 / 2.0 | 0 of 4 | 1.6 |
| Malik Monk | PG/SG | Free agent | 15.8 / 18.0 | 15.0 / 24.0 | 1 of 9 | 15.4 |
| Zach LaVine | SG/SF | Dr White Slong | 32.1 / 35.0 | 33.0 / 25.0 | 7 of 7 | 32.4 |

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
| Jared McCain | PG/SG | Free agent | 10 GP, 30.2 min, 24.5 FP/g, started 8 | 21.8 |
| Ajay Mitchell | PG/SG | Lauri Birds | 8 GP, 28.8 min, 24.5 FP/g, started 8 | 27.6 |
| Kenrich Williams | SF | Free agent | 10 GP, 25.0 min, 27.4 FP/g, started 5 | 27.4 |
| Alex Caruso | PG/SG | Free agent | 7 GP, 20.1 min, 21.4 FP/g, started 1 | 22.8 |
| Micah Peavy | SF | Free agent | 8 GP, 19.8 min, 12.0 FP/g, started 3 | 11.8 |
| Brooks Barnhizer | SF | Free agent | 5 GP, 9.0 min, 11.8 FP/g, started 0 | 10.9 |

- **Whose minutes he takes** (9 games with him, 1 before him): minutes before / with him.

  - Bennett Stirtz (Free agent): 29.0 → 21.0 min
  - Micah Peavy (Free agent): 23.0 → 19.3 min

### Research

- _pending_

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-26 06:13 UTC.
