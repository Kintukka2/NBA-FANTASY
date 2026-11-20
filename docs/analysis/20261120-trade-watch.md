# Trade watch: 19 Nov 2026

- Generated 2026-11-20 03:47 UTC by `council/trade_watch.py`. This is **data, not a verdict**: each trade is a question for the research step.
- **Trades read:** ESPN's NBA transactions feed, 20 Oct to 19 Nov (30 days). 1 traded player is in the league pool (rostered, free agent or waivers).
- **Team he left:** his role there, and who has taken his minutes since (games without him against games with him, from ESPN's box scores). **Team he joined:** long absences at his positions (ESPN expects them out more than 7 days), the depth there, and whose minutes he takes.
- **Rate** is the weighted, outlier-adjusted rate (`council/gamelog.py`). L7 / L15 / L30 are FP/g over the last 7, 15 and 30 days, games in brackets.

## Summary

| Date | Player | From → To | Role before | Role since | Rate | League |
|---|---|---|---|---|---:|---|
| 08 Nov | **Nique Clifford** | SAC → OKC | 8 GP, 6.2 min, 3.9 FP/g, started 0 | 5 GP, 17.0 min, 8.0 FP/g, started 0 | 7.5 | Free agent |

## Nique Clifford: SAC → OKC (08 Nov)

- ESPN: "Traded G Nique Clifford to the Oklahoma City Thunder."
- SG/SF · Free agent · rate **7.5** · season 5.5 (13) · L7 7.3 (3) · L15 7.4 (7) · L30 5.5 (13) · projected 20.8 · active
- With SAC: 8 GP, 6.2 min, 3.9 FP/g, started 0. With OKC: 5 GP, 17.0 min, 8.0 FP/g, started 0.

### The team he left: SAC

- **Role vacated:** 8 GP, 6.2 min, 3.9 FP/g, started 0. A small role: little opportunity opens.
- **Since the trade** (5 games without him, against 5 with him):

| Teammate | Pos | League | Min without / with | FP/g without / with | Starts without | Rate |
|---|---|---|---|---|---:|---:|
| Alex Karaban | SF/PF | Free agent | 16.5 / 11.0 | 5.0 / 2.7 | 0 of 2 | 4.0 |
| Daeqwon Plowden | SG | Free agent | 8.8 / 3.5 | 5.6 / 2.0 | 0 of 5 | 7.3 |
| Dylan Cardwell | C | Free agent | 18.2 / 14.0 | 19.0 / 21.5 | 2 of 5 | 19.3 |
| Zach LaVine | SG/SF | Team Nic Kerr | 31.5 / 31.6 | 34.2 / 26.4 | 4 of 4 | 33.5 |
| De'Andre Hunter | SF/PF | Free agent | 35.5 / 35.8 | 23.8 / 19.0 | 4 of 4 | 23.4 |
| Malik Monk | PG/SG | Free agent | 18.2 / 18.8 | 16.2 / 20.4 | 1 of 5 | 18.9 |
| Darius Acuff Jr. | PG | Team Nic Kerr | 36.4 / 38.0 | 42.4 / 50.0 | 5 of 5 | 38.9 |
| Emanuel Sharp | SG | Free agent | 14.6 / 20.6 | 12.6 / 11.6 | 0 of 5 | 12.8 |

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
| Ajay Mitchell | PG/SG | Lauri Birds | 8 GP, 29.2 min, 30.8 FP/g, started 8 | 33.0 |
| Jared McCain | PG/SG | Waivers | 10 GP, 28.8 min, 25.4 FP/g, started 7 | 24.5 |
| Kenrich Williams | SF | Free agent | 10 GP, 24.5 min, 22.0 FP/g, started 8 | 23.3 |
| Alex Caruso | PG/SG | Free agent | 8 GP, 19.4 min, 18.2 FP/g, started 1 | 19.4 |
| Micah Peavy | SF | Free agent | 8 GP, 17.9 min, 11.4 FP/g, started 0 | 12.0 |
| Brooks Barnhizer | SF | Free agent | 5 GP, 5.6 min, 7.2 FP/g, started 0 | 5.3 |

- **Whose minutes he takes** (5 games with him, 5 before him): minutes before / with him.

  - Jaylin Williams (Free agent): 23.0 → 16.0 min
  - Bennett Stirtz (Free agent): 22.6 → 17.8 min
  - Micah Peavy (Free agent): 19.4 → 15.3 min
  - Brooks Barnhizer (Free agent): 6.3 → 4.5 min

### Research

- **No new trades.** Nique Clifford (SAC → OKC, 8 Nov) still comes off the bench: 17.0 min and 8.0 FP/g in 5 OKC games. Last run's research still holds ([20261117-trade-watch.md](20261117-trade-watch.md)).
- **Verdict:** opportunity unchanged. No row.

## Sources

- ESPN's NBA transactions feed (`site.api.espn.com/apis/site/v2/sports/basketball/nba/transactions`), ESPN's NBA injury feed, ESPN box scores (cached in `council/.cache/box`), and league 423671879 (`kona_player_info`, `mTeam`, `proTeamSchedules_wl`), read 2026-11-20 03:47 UTC.
