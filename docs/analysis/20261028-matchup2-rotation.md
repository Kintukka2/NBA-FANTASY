# Matchup 2: Come-in Cider vs Team Nic Kerr

- Generated 2026-10-28 01:02 UTC by `council/matchup.py`. This is **a report, not a council verdict**.
- **Score:** 229 to 270 (down 41). The matchup runs Mon 26 Oct to Sun 01 Nov (US dates), with 6 days left.
- **Adds:** 1 used this matchup of 7, so **6 left**. Free agents arrive at once; waiver players take 24 hours.
- **Method:** an exact optimiser fills the 10 starting slots each day. Rate per game: 70% this season's FP/g and 30% last season's (or ESPN's projection) at 3+ games, otherwise 50/50. A player listed OUT is left out until ESPN's estimated return. Streamers need 18+ minutes this season.
- **Checks:** **games were live** (--allow-live). All 1099 pool players re-score with `scripts/league_scoring.py` (0 mismatches).
- Times are ET and Melbourne.

## Plan

The rotation runs through **Pritchard's slot**, one add a day. **VanVleet stays, unless Houston rests him on Saturday.**

| US day | Deadline, Melbourne (ET) | Move | Why |
|---|---|---|---|
| Wed 28 | **10:00 am Thu 29** (7:00 pm Wed) | Drop Pritchard, add **CJ McCollum** (ATL) | He covers Thursday, our emptiest day (2 of ours play). |
| Thu 29 | — | none | Thursday's add stays spare. |
| Fri 30 | **11:00 am Sat 31** (8:00 pm Fri) | Drop McCollum, add **Reed Sheppard** (HOU) | He plays Fri and Sat. He started the last game VanVleet rested. |
| Sat 31 | Houston's report lands by **5:00 am Sun 1** (2:00 pm Sat); Hayes tips **6:00 am Sun 1** (3:00 pm Sat) | **Only if VanVleet is ruled out:** drop VanVleet, add **Jaxson Hayes** (UTAH) | Worth **+31.0** on its own (*What-if*, one-add row). |
| Sun 1 | **1:00 pm Mon 2** (9:00 pm Sun) | Drop Sheppard, add **Ja'Kobe Walter** (TOR) | Toronto's starter while Kawhi is out. |

- **If VanVleet plays Saturday,** this is the script's 3-add plan: **+68.2** against keeping both slots.
  - The 5-add maximum is +72.9. It spends Saturday's add on Powell → Hayes, which would leave nothing for VanVleet's rest.
  - The Sheppard route settles for +68.2 instead of +72.9 to keep that option open.
- **If he rests,** this is the *What-if*'s 4-add plan: **+99.2**, against a maximum of +101.0.
- **His Milwaukee game doesn't decide it.**
  - Keeping him beats streaming his slot while his rate stays above **29.9**. It is 32.4 now.
  - Only a game **under 17 FP** against Milwaukee takes him below that (*Break-even*).
  - Saturday's rest is what decides it.
- **Cost of the Saturday drop:** VanVleet himself. He has 3 games next week (Mon 2, Wed 4, Sat 7), none of them a back-to-back.
- **Add limit:** the league allows 1 add per scoring period. This plan never uses more than one add on a US day, so it is legal whether that cap runs daily or weekly.
- **Lineups:**
  - On Wednesday, 11 of ours play with McCollum, so **Bane sits**.
  - If Lendeborg sits Wednesday, Bane starts instead.
- **Where it leaves us:**
  - As rostered, the projected final is **1,441 to 1,727**.
  - The plan adds +68.2, or +99.2 if VanVleet rests.
  - Their Saturday is the big swing: 9 of theirs play.
  - This read came while three games were live. The plan's gains compare like with like, so they barely move; the projected totals will.
- **Swing factors:**
  - **Hayes** (right shoulder soreness): questionable Wednesday, no timetable reported; ESPN est. 28 Oct. If he is out Saturday, Kel'el Ware (MIL, +31) is the next-best Saturday add.
  - **Lendeborg** (left foot soreness): questionable Wednesday, no timetable reported; ESPN est. 28 Oct.
  - **Kawhi Leonard** (left knee swelling): out at least a week per the Raptors and several weeks per Shams; ESPN est. 23 Nov. While he is out, Walter starts.
  - **Duren** (IR, hamstring): re-evaluated in 2 weeks; ESPN est. 9 Nov.

## The rest of the week

| Day (US) | Melbourne | Ours playing | Open slots | Our lineup | Theirs playing | Their lineup |
|---|---|---:|---:|---:|---:|---:|
| Tue 27 Oct | Wed 28 | 4 | 6 | 136 | 5 | 206 |
| Wed 28 Oct | Thu 29 | 10 | 0 | 369 | 8 | 329 |
| Thu 29 Oct | Fri 30 | 2 | 8 | 77 | 5 | 185 |
| Fri 30 Oct | Sat 31 | 10 | 0 | 354 | 7 | 293 |
| Sat 31 Oct | Sun 01 | 3 | 7 | 109 | 9 | 351 |
| Sun 01 Nov | Mon 02 | 5 | 5 | 166 | 2 | 93 |

**Projection:** 1211 more for us and 1458 for them, for a final of **1440 to 1728**.

## Our roster

x = plays, o = has a game but is listed out.

| Player | NBA | Rate | Tue 27 | Wed 28 | Thu 29 | Fri 30 | Sat 31 | Sun 01 | Status |
|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| Kawhi Leonard | TOR | 45.0 |  | o |  | o |  | o | out, ESPN est. 23 Nov |
| Cade Cunningham | DET | 44.9 | x | x |  | x |  |  |  |
| Dejounte Murray | NO | 44.8 |  | x | x |  | x |  |  |
| Jamal Murray | DEN | 44.4 |  | x |  | x |  |  |  |
| Scottie Barnes | TOR | 39.4 |  | x |  | x |  | x |  |
| Yaxel Lendeborg | GS | 39.2 |  | x |  | x |  | x | day-to-day, ESPN est. 28 Oct |
| Caleb Wilson | CHI | 36.4 |  | x |  | x |  |  |  |
| Paul George | BOS | 34.9 | x |  |  | x |  | x |  |
| Fred VanVleet | HOU | 32.4 |  | x |  | x | x |  |  |
| Trey Murphy III | NO | 32.1 |  | x | x |  | x |  |  |
| Paul Reed | DET | 29.2 | x | x |  | x |  |  |  |
| Payton Pritchard | BOS | 27.0 | x |  |  | x |  | x |  |
| Desmond Bane | ORL | 25.8 |  | x |  | x |  | x |  |

IR: Jalen Duren (cannot score while in the IR slot).

What each player adds this week: our lineup total with him, minus without him. Low numbers mean his games fall on days we are already full.

| Player | Adds this week |
|---|---:|
| Kawhi Leonard | 0.0 |
| Caleb Wilson | 72.7 |
| Desmond Bane | 77.3 |
| Payton Pritchard | 81.0 |
| Paul Reed | 87.5 |
| Jamal Murray | 88.9 |
| Trey Murphy III | 96.3 |
| Fred VanVleet | 97.3 |
| Paul George | 104.8 |
| Yaxel Lendeborg | 117.7 |
| Scottie Barnes | 118.1 |
| Dejounte Murray | 134.3 |
| Cade Cunningham | 134.6 |

## Team Nic Kerr

| Player | NBA | Rate | Tue 27 | Wed 28 | Thu 29 | Fri 30 | Sat 31 | Sun 01 | Status |
|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| Luka Doncic | LAL | 57.4 | x | x |  | x |  | x |  |
| Tyrese Maxey | PHI | 51.4 |  | x |  | x | x |  |  |
| Domantas Sabonis | SAC | 48.6 | x |  | x |  | x |  |  |
| Trae Young | WSH | 42.6 |  | x |  | x |  |  |  |
| Chet Holmgren | OKC | 40.3 |  | o |  |  | x |  | out, ESPN est. 31 Oct |
| Ja Morant | POR | 37.8 | x |  | x |  | x |  |  |
| Jabari Smith Jr. | HOU | 37.6 |  | x |  | x | x |  |  |
| Moussa Diabate | CHA | 37.5 |  | x |  | x | x |  |  |
| Jarrett Allen | CLE | 36.5 |  | x | x |  | x |  |  |
| Michael Porter Jr. | BKN | 35.8 | x |  |  | x |  | x |  |
| James Harden | CLE | 35.2 |  | x | x |  | x |  |  |
| Alex Sarr | WSH | 31.1 |  | x |  | x |  |  |  |
| Darius Acuff Jr. | SAC | 26.6 | x |  | x |  | x |  |  |

## Streaming Payton Pritchard's slot

Keeping Payton Pritchard (BOS) is worth **54.0** this week: Tue 27 0, Fri 30 27, Sun 01 27.

### One add, now

| Free agent | NBA | Games | Now: GP, min, FP/g | Started | 2026 FP/g | Owned | vs keeping |
|---|---|---|---|---|---:|---:|---:|
| **Ja'Kobe Walter** | TOR | Wed, Fri, Sun | 3, 26.0, 34.7 | 1 of 3 | 17.7 | 10% | **+9.0** |
| **Reed Sheppard** | HOU | Wed, Fri, Sat | 3, 23.3, 29.3 | 1 of 3 | 30.1 | 64% | **+9.0** |
| **CJ McCollum** | ATL | Wed, Thu, Sat | 4, 26.8, 28.2 | 4 of 4 | 32.7 | 76% | **+9.0** |
| **Onyeka Okongwu** | ATL | Wed, Thu, Sat | 4, 26.5, 25.2 | 4 of 4 | 37.6 | 79% | **+7.2** |
| **Obi Toppin** (day-to-day, ESPN est. 28 Oct) | IND | Wed, Fri, Sun | 4, 23.2, 31.5 | 0 of 4 | 22.4 | 15% | **+6.6** |
| **Peyton Watson** | CLE | Wed, Thu, Sat | 3, 32.7, 28.0 | 3 of 3 | 29.8 | 45% | **+5.9** |
| **Aaron Wiggins** (day-to-day, ESPN est. 28 Oct) | ATL | Wed, Thu, Sat | 4, 27.5, 31.5 | 0 of 4 | 19.4 | 24% | **+3.9** |
| **Jaylen Wells** | MEM | Thu, Sat | 4, 29.0, 31.8 | 4 of 4 | 21.7 | 21% | **+3.5** |

### Best streamer each day

If the slot turns over daily, these are the best adds for each day alone.

- **Tue 27 Oct:** no streamer adds anything
- **Wed 28 Oct:** Norman Powell (CHI, +6), P.J. Washington (DAL, +5), Jaxson Hayes (UTAH, +5), Kel'el Ware (MIL, +5)
- **Thu 29 Oct:** CJ McCollum (ATL, +30), Onyeka Okongwu (ATL, +29), Jaylen Wells (MEM, +29), Peyton Watson (CLE, +29)
- **Fri 30 Oct:** Norman Powell (CHI, +31), P.J. Washington (DAL, +31), Naji Marshall (DAL, +31), Daniel Gafford (DAL, +30)
- **Sat 31 Oct:** Jaxson Hayes (UTAH, +31), Kel'el Ware (MIL, +31), Ryan Rollins (MIL, +30), Isaiah Hartenstein (OKC, +30)
- **Sun 01 Nov:** Ja'Kobe Walter (TOR, +30), Obi Toppin (IND, +29), Derrick Jones Jr. (LAC, +27), Isaiah Jackson (LAC, +27)

### Two adds in the slot

The first streamer comes in now and is swapped out before the second one's first game.

| First add | Until | Second add | From | vs keeping |
|---|---|---|---|---:|
| CJ McCollum (ATL) | Thu 29 Oct | Ja'Kobe Walter (TOR) | Fri 30 Oct | **+38.6** |
| Reed Sheppard (HOU) | Sat 31 Oct | Ja'Kobe Walter (TOR) | Sun 01 Nov | **+38.6** |
| CJ McCollum (ATL) | Thu 29 Oct | Reed Sheppard (HOU) | Fri 30 Oct | **+38.6** |
| Reed Sheppard (HOU) | Sat 31 Oct | Obi Toppin (IND) | Sun 01 Nov | **+37.8** |
| CJ McCollum (ATL) | Sat 31 Oct | Obi Toppin (IND) | Sun 01 Nov | **+37.8** |

### Lineup with Ja'Kobe Walter in the slot

| Day | Lineup | Playing | Sits |
|---|---:|---:|---|
| Tue 27 Oct | 136 | 4 | — |
| Wed 28 Oct | 372 | 11 | Desmond Bane |
| Thu 29 Oct | 77 | 2 | — |
| Fri 30 Oct | 356 | 10 | — |
| Sat 31 Oct | 109 | 3 | — |
| Sun 01 Nov | 169 | 5 | — |

## Rotating Payton Pritchard's and Fred VanVleet's slots

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, at most 1 per scoring period (US day) as the league is set, so 5 usable over these 5 days.
- Streamers considered: the 21 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1075** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+29.6** | Sun 01: VanVleet → Ja'Kobe Walter (TOR) |
| 2 | **+38.6** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Ja'Kobe Walter (TOR) |
| 3 | **+68.2** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 4 | **+71.4** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Norman Powell (CHI); Sat 31: Powell → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |
| 5 | **+72.9** | Wed 28: Pritchard → P.J. Washington (DAL); Thu 29: Washington → CJ McCollum (ATL); Fri 30: McCollum → Norman Powell (CHI); Sat 31: Powell → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |

### Keep one, rotate the other

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 5 | +72.9 |
| Keep Payton Pritchard, rotate the rest | 4 | +56.7 |
| Keep Fred VanVleet, rotate the rest | 5 | +72.9 |

### Break-even

The rate a player needs for keeping him to beat streaming his slot, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.0): keep him while his rate is above **35.2**.
- **Fred VanVleet** (rate 32.4): keep him while his rate is above **29.9**. His Wed 28 game moves it: under **17 FP** (he averages 32.0) takes it below.

### Best plan: 5 adds, +72.9

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | P.J. Washington (DAL) plays | Fred VanVleet (HOU) plays | 374 | +5.3 | Desmond Bane |
| Thu 29 Oct | Fri 30 | CJ McCollum (ATL) plays | Fred VanVleet (HOU), idle | 106 | +29.6 | — |
| Fri 30 Oct | Sat 31 | Norman Powell (CHI) plays | Fred VanVleet (HOU) plays | 358 | +4.4 | — |
| Sat 31 Oct | Sun 01 | Jaxson Hayes (UTAH) plays | Fred VanVleet (HOU) plays | 140 | +31.0 | — |
| Sun 01 Nov | Mon 02 | Ja'Kobe Walter (TOR) plays | Fred VanVleet (HOU), idle | 169 | +2.6 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **P.J. Washington** (DAL; GP, min, FP/g 4, 35.2, 31.2; started 4 of 4). By 09:30PM ET / Thu 29 12:30PM.
2. **Thu 29 Oct:** drop P.J. Washington, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM.
3. **Fri 30 Oct:** drop CJ McCollum, add **Norman Powell** (CHI; GP, min, FP/g 4, 28.0, 30.8; started 4 of 4). By 07:30PM ET / Sat 31 10:30AM.
4. **Sat 31 Oct:** drop Norman Powell, add **Jaxson Hayes** (UTAH; GP, min, FP/g 3, 23.7, 35.7; started 1 of 3; day-to-day, ESPN est. 28 Oct). By 03:00PM ET / Sun 01 06:00AM.
5. **Sun 01 Nov:** drop Jaxson Hayes, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.

Left holding at the end of the week: Ja'Kobe Walter (TOR, 3 games next week), Fred VanVleet (HOU, 3 games next week).

### Notes

- **Roles come from ESPN's box scores** (the *Started* column).
  - McCollum has started all 4 of Atlanta's games, in the same five that closed last season [AJC](https://www.ajc.com/sports/2026/10/hawks-roster/) [Brad Rowland](https://x.com/BTRowland/status/2113035852196757766).
  - The 28 Oct report said he was "coming off the bench". That was wrong, and it is corrected there.
- **VanVleet rested on 24 Oct, the second night of a back-to-back,** as knee load management in his return from a torn ACL. Sheppard started in his place.
  - He returned on Monday: 5 points in 29 minutes [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/fred-vanvleet-knee-out-saturday-vs-hawks) [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-quiet-in-return-monday/).
  - He was off the injury report for that game [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-not-listed-on-injury-report-536038/).
  - Houston's next back-to-back is Fri 30 at DAL, then Sat 31 vs OKC.
- **Injury-report deadline:** for the second game of a back-to-back, teams must file by 1 p.m. local time on game day [NBA](https://official.nba.com/nba-injury-report-2025-26/).
  - For Houston on Saturday, that is 2:00 pm ET, or 5:00 am Sun in Melbourne.
- **Sheppard** comes off the bench behind VanVleet [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-reed-sheppard-logs-28-minutes-off-bench).
- **Hayes:** questionable Wednesday vs SA with right shoulder soreness. No timetable reported; ESPN est. 28 Oct.
  - He should start when available, with Nurkić and Jaren Jackson out [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/jaxson-hayes-shoulder-questionable-wednesday) [Rotowire](https://www.rotowire.com/basketball/headlines/jaxson-hayes-injury-questionable-versus-spurs-536399).
- **Walter** has started since Kawhi Leonard went out: 22 points in 31 minutes on 25 Oct [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/jakobe-walter-replaces-kawhi-knee-in-starting-5) [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/).
  - Kawhi Leonard (left knee swelling) is out at least a week per the Raptors and several weeks per Shams; ESPN est. 23 Nov [ESPN](https://www.espn.com/nba/story/_/id/50298441/raptors-kawhi-leonard-weeks-due-knee-sources-say).
- **P.J. Washington** (the 5-add plan's Wednesday add) starts in Dallas's frontcourt [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/p-j-washington-scores).

## What-if: VanVleet rests Sat 31

A second run at 2026-10-28 01:02 UTC with `--sit "Fred VanVleet@2026-10-31"`, the second night of Houston's Fri–Sat back-to-back. Everything else is unchanged.

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, at most 1 per scoring period (US day) as the league is set, so 5 usable over these 5 days.
- Streamers considered: the 21 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1042** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+31.0** | Sat 31: VanVleet → Jaxson Hayes (UTAH) |
| 2 | **+60.6** | Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |
| 3 | **+85.9** | Thu 29: VanVleet → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 4 | **+99.2** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 5 | **+101.0** | Wed 28: Pritchard → Norman Powell (CHI); Thu 29: Powell → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |

### Keep one, rotate the other

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 5 | +101.0 |
| Keep Payton Pritchard, rotate the rest | 4 | +89.2 |
| Keep Fred VanVleet, rotate the rest | 5 | +72.9 |

### Break-even

The rate a player needs for keeping him to beat streaming his slot, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.0): keep him while his rate is above **33.0**.
- **Fred VanVleet** (rate 32.4): streaming his slot wins at any rate.

### Best plan: 5 adds, +101.0

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | Norman Powell (CHI) plays | Fred VanVleet (HOU) plays | 374 | +5.7 | Desmond Bane |
| Thu 29 Oct | Fri 30 | CJ McCollum (ATL) plays | Fred VanVleet (HOU), idle | 106 | +29.6 | — |
| Fri 30 Oct | Sat 31 | Reed Sheppard (HOU) plays | Fred VanVleet (HOU) plays | 356 | +2.6 | — |
| Sat 31 Oct | Sun 01 | Reed Sheppard (HOU) plays | Jaxson Hayes (UTAH) plays | 137 | +60.6 | — |
| Sun 01 Nov | Mon 02 | Reed Sheppard (HOU), idle | Ja'Kobe Walter (TOR) plays | 169 | +2.6 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **Norman Powell** (CHI; GP, min, FP/g 4, 28.0, 30.8; started 4 of 4). By 08:00PM ET / Thu 29 11:00AM.
2. **Thu 29 Oct:** drop Norman Powell, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM.
3. **Fri 30 Oct:** drop CJ McCollum, add **Reed Sheppard** (HOU; GP, min, FP/g 3, 23.3, 29.3; started 1 of 3). By 08:00PM ET / Sat 31 11:00AM.
4. **Sat 31 Oct:** drop Fred VanVleet, add **Jaxson Hayes** (UTAH; GP, min, FP/g 3, 23.7, 35.7; started 1 of 3; day-to-day, ESPN est. 28 Oct). By 03:00PM ET / Sun 01 06:00AM.
5. **Sun 01 Nov:** drop Jaxson Hayes, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.

Left holding at the end of the week: Reed Sheppard (HOU, 3 games next week), Ja'Kobe Walter (TOR, 3 games next week).

## Tip-off times

For the teams named above. Times are ET / Melbourne.

- **ATL:** Wed 28 07:00PM / Thu 29 10:00AM; Thu 29 08:00PM / Fri 30 11:00AM; Sat 31 07:00PM / Sun 01 10:00AM
- **BOS:** Tue 27 07:30PM / Wed 28 10:30AM; Fri 30 07:30PM / Sat 31 10:30AM; Sun 01 03:30PM / Mon 02 07:30AM
- **CHI:** Wed 28 08:00PM / Thu 29 11:00AM; Fri 30 07:30PM / Sat 31 10:30AM
- **CLE:** Wed 28 07:00PM / Thu 29 10:00AM; Thu 29 08:00PM / Fri 30 11:00AM; Sat 31 08:00PM / Sun 01 11:00AM
- **DAL:** Wed 28 09:30PM / Thu 29 12:30PM; Fri 30 08:00PM / Sat 31 11:00AM
- **HOU:** Wed 28 08:00PM / Thu 29 11:00AM; Fri 30 08:00PM / Sat 31 11:00AM; Sat 31 08:30PM / Sun 01 11:30AM
- **IND:** Wed 28 07:00PM / Thu 29 10:00AM; Fri 30 08:00PM / Sat 31 11:00AM; Sun 01 05:00PM / Mon 02 09:00AM
- **MEM:** Thu 29 10:00PM / Fri 30 01:00PM; Sat 31 08:00PM / Sun 01 11:00AM
- **TOR:** Wed 28 07:30PM / Thu 29 10:30AM; Fri 30 07:30PM / Sat 31 10:30AM; Sun 01 09:00PM / Mon 02 01:00PM
- **UTAH:** Wed 28 09:00PM / Thu 29 12:00PM; Sat 31 03:00PM / Sun 01 06:00AM

## Sources

- ESPN fantasy API, league 423671879 (`mRoster`, `mTeam`, `mMatchupScore`, `mSettings`, `mStatus`, `kona_player_info`, `proTeamSchedules_wl`) and ESPN's NBA injury feed, read 2026-10-28 01:02 UTC.
- Research, 28 Oct 2026: [AJC](https://www.ajc.com/sports/2026/10/hawks-roster/); [Brad Rowland](https://x.com/BTRowland/status/2113035852196757766); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/fred-vanvleet-knee-out-saturday-vs-hawks); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-quiet-in-return-monday/); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-fred-vanvleet-not-listed-on-injury-report-536038/); [NBA](https://official.nba.com/nba-injury-report-2025-26/); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-reed-sheppard-logs-28-minutes-off-bench); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/jaxson-hayes-shoulder-questionable-wednesday); [Rotowire](https://www.rotowire.com/basketball/headlines/jaxson-hayes-injury-questionable-versus-spurs-536399); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/jakobe-walter-replaces-kawhi-knee-in-starting-5); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/); [ESPN](https://www.espn.com/nba/story/_/id/50298441/raptors-kawhi-leonard-weeks-due-knee-sources-say); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-26/p-j-washington-scores); Lendeborg [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/yaxel-lendeborg-foot-questionable-wednesday); Duren [ESPN](https://www.espn.com/nba/story/_/id/50277066/pistons-jalen-duren-hamstring-strain-least-2-weeks).
