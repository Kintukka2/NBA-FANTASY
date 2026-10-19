# Preseason review: 10 players set to start 2026-27 fast

- Prepared 19 Oct 2026, the day before the opener, by Claude. This is **analysis, not a council verdict**: the council has not voted on it.
- Built from Wire's two preseason briefings, [`docs/research/20261019-0750-preseason-east.md`](../research/20261019-0750-preseason-east.md) and [`docs/research/20261019-0745-preseason-west.md`](../research/20261019-0745-preseason-west.md), plus `data/processed/players_scored.csv`, `council/taken.txt` and `council/roster.csv`.

## Method

1. **Preseason points in our scoring.** Every Eastern stat table (148 players, CBS preseason totals) was scored with `scripts/league_scoring.py` and turned into fantasy points per 36 minutes (**preFP36**).
   - The West has no full tables. Its standouts' best single-game lines were scored the same way.
   - Both feeds lack offensive rebounds and double-double bonuses, so big men read slightly low.
2. **Compared with last season.** preFP36 is set against each player's 2026 league-scored rate per 36 minutes (**FP36 '26** = `FP_ACT_PG / A_MIN × 36`). The gap is the **lift**.
3. **Kept only players with a fast-start setup.** Each one had to meet all three conditions:
   - a starting or locked rotation role, per the briefings
   - no injury going into the opener
   - production that holds up across more than one game
4. **Left out the obvious first-rounders.** Jokic, Giannis, Wembanyama and the like will start fast and are all rostered. The list targets players likely to beat their draft price in the first two to three weeks.
5. **Availability.** "Undrafted" means not in `council/taken.txt`. Other teams may have claimed players since 8 Oct, so check ESPN before acting.

**Sample warning:** preseason minutes were about 15-25 a game, often for a half, over 2-5 games. Treat the numbers as role and form signals, not projections.

## The top 10

| # | Player | Team | Ours? | Role going in | Preseason | Lift vs '26 | Why a fast start |
|---|---|---|---|---|---|---|---|
| 1 | **Jalen Duren** | DET | **Ours** | Starting C | 2 GP, 17.5 min, 19.0 pts, 14-18 FG, 4 stl, 2 blk. **preFP36 67.9** | +11.5 (56.4 '26) | Efficient (78% FG) and active on defence, coming off a planned ramp-up. Detroit has no injuries and opens Tue 20 Oct vs BOS. |
| 2 | **Scottie Barnes** | TOR | **Ours** | Starter, all 4 GP | 21.3 min, 16.3 pts, 26-46 FG, 5 stl, **5 blk**. **preFP36 60.9** | +10.1 (50.8) | Steals and blocks at 4 points each, on a full 80-game base. Toronto lists no rotation injuries. |
| 3 | **Ryan Rollins** | MIL | **Ours** | Starter, 4 of 4 | 18.5 min, 11.8 pts, 15 ast, 5 stl, 4 blk, **2 TO**. **preFP36 59.9** | +17.8 (42.1) | Starting next to Herro, with very few turnovers. **He is the player the waiver plan drops.** See below. |
| 4 | **Jeremiah Fears** | NO | Undrafted | Starting in the preseason | 13.3 pts as a starter. **3 stl in each of his last two games** (scored 38 and 44). Single-game FP36 62-79 | '26: 26.4 FP in 82 GP | Dejounte Murray (toe) is questionable for 21 Oct, and Fears ran the offence in his absence. *(Murray is also ours.)* |
| 5 | **Kyshawn George** | WSH | Undrafted | Starter, 4 of 4, 24 min | 15.3 pts, **19-29 FG**, 5 stl, **6 blk**, 10 ast. **preFP36 51.4** | +11.2 (40.2) | Highest-minute starter on his team, with defensive stats in a league that pays 4 for each. Dybantsa's ankle could add touches. |
| 6 | **Andrew Wiggins** | MIA | Undrafted | Starter, 4 of 4 | 16.3 min, 14.3 pts, **20-33 FG**, 5 stl, 2 TO. **preFP36 57.0** | +16.9 (40.1) | Efficient scoring next to Giannis. The CSV's DAY_TO_DAY tag has no source, so he is healthy. |
| 7 | **Day'Ron Sharpe** | BKN | Undrafted | Starting C, 3 of 3 | 18.7 min, 15 reb, **10 ast, 5 stl, 4 blk** in 3 GP. **preFP36 57.2** | +6.8 (50.4) | Last season he produced 50 per 36 as a backup. Starting minutes are what he was missing. |
| 8 | **Yaxel Lendeborg** | GS | Undrafted | Rookie starter (Kerr "leaning toward" him) | Finale: 26 min, 17 pts, 6-9 FG, 4 reb, 5 ast, 2 stl, 1 blk = **46 FP** | rookie | Starting forward on a team missing Butler, Moody and Porziņģis. Curry's ankle sprain adds usage if he sits. |
| 9 | **Draymond Green** | GS | Undrafted | Starter, expected 25-30 min | Finale: 24 min, 7 pts, 8 reb, **10 ast, 3 stl** = **49 FP** | '26: 26.5 FP in 68 GP | His assists and steals score heavily here, and Golden State needs him to create. Low '26 baseline, so this is a short-term pick. |
| 10 | **Devin Vassell** | SA | Undrafted | **Announced** opening-night starter | 14 Oct: 25 min, 12 pts, 6 reb, 2 ast, **3 stl**, 1 blk = 39 FP | '26: 27.3 FP in 67 GP | One of the few players whose start Tuesday was officially confirmed (Mitch Johnson, 17 Oct). |

### Next in line

- **Mitchell Robinson** (BOS, undrafted): started 2 of 2, 8-10 FG, 3 blk, preFP36 56.9. Neemias Queta could take the job instead.
- **Nikola Jović** (MIA, undrafted): preFP36 52.6 with 28 reb and 5 blk. He starts at C only if Adebayo (groin, questionable) sits.
- **Tristan da Silva** (ORL, undrafted): preFP36 50.2. He is the favourite to start if Franz Wagner (shoulder) misses time.
- **Jock Landale** (ATL) and **Leonard Miller** (CHI): preFP36 64.6 and 61.3, but both are bench players under 20 minutes.

## What it means for our roster

- **Rollins vs Ware.** The 8 Oct waiver plan drops Rollins. The preseason now points the other way.
  - **Rollins** started all four games at 59.9 per 36 (+17.8 on '26).
  - **Kel'el Ware** started 1 of 5 at **36.0 per 36 (−16.7 on '26)**, while Myles Turner started all four with **11 blocks**. Rotowire calls Ware's role "unclear".
  - **Worth a council re-vote before Sunday's waivers.**
- **Paul George** (the planned add) read 41.9 per 36, level with last season's 42.3. He had **7 steals in 2 games** but shot **5-20**. The case for him is unchanged.
- **Watch these early:**
  - **Kawhi** played under a minutes restriction and left the 15 Oct game with no reason given.
  - **Dejounte Murray** is questionable with his toe.
  - **Caleb Wilson** started 5 of 5 but committed 17 turnovers on 30-69 FG, for 30.3 per 36.
  - **Cade** (43.9) is no concern on 3 games.
