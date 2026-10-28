# Matchup 2: Come-in Cider vs Team Nic Kerr

- Generated 2026-10-28 01:28 UTC by `council/matchup.py`. This is **a report, not a council verdict**.
- **Score:** 229 to 270 (down 41). The matchup runs Mon 26 Oct to Sun 01 Nov (US dates), with 6 days left.
- **Adds:** 1 used this matchup of 7, so **6 left**. Free agents arrive at once; waiver players take 24 hours.
- **Method:** an exact optimiser fills the 10 starting slots each day. Rate per game: 70% this season's FP/g and 30% last season's (or ESPN's projection) at 3+ games, otherwise 50/50. A player listed OUT is left out until ESPN's estimated return. Streamers need 18+ minutes this season.
- **Checks:** **games were live** (--allow-live). All 1099 pool players re-score with `scripts/league_scoring.py` (0 mismatches).
- Times are ET and Melbourne.

## Plan

**The add limit is a matchup total, not a daily cap.**
- ESPN's transaction log shows teams making several adds in one scoring period. We made three in period 5 (Sat 24 Oct at 3:58 pm and 10:13 pm ET, then 12:47 am Sun ET). Melbourne poopoo made four on Mon 26 Oct.
- That leaves **6 adds**, usable on any day.
- *Corrected 28 Oct, 01:30 UTC: an earlier version of this report assumed 1 add per US day.*

**Both slots stream, and VanVleet goes after Milwaukee.**

| # | US day | Deadline, Melbourne (ET) | Move |
|---|---|---|---|
| 1 | Wed 28 | **10:00 am Thu 29** (7:00 pm Wed) | Drop Pritchard, add **Onyeka Okongwu** (ATL) |
| 2 | Thu 29 | **11:00 am Fri 30** (8:00 pm Thu) | Drop VanVleet, add **CJ McCollum** (ATL) |
| 3 | Fri 30 | **10:00 am Sat 31** (7:00 pm Fri) | Drop McCollum, add **Grayson Allen** (CHA) |
| 4 | Fri 30 | **11:00 am Sat 31** (8:00 pm Fri) | Drop Okongwu, add **Reed Sheppard** (HOU) |
| 5 | Sun 1 | **9:00 am Mon 2** (5:00 pm Sun) | Drop Allen, add **Obi Toppin** (IND) |
| 6 | Sun 1 | **1:00 pm Mon 2** (9:00 pm Sun) | Drop Sheppard, add **Ja'Kobe Walter** (TOR) |

What it's worth, against keeping both slots:
- **If Lendeborg plays Wednesday: +114.2.** This is the *Okongwu first* run below.
  - McCollum first is worth +114.8, so taking Okongwu first costs 0.6.
  - Bane sits Wednesday.
- **If Lendeborg sits Wednesday: +139.9.** This is the *Lendeborg sits* run, which finds exactly this plan.
  - Okongwu fills his slot, and nobody sits.
  - That case is why Okongwu goes first: Lendeborg's status may not be known before Atlanta tips off.
- Thursday is where the plan pays off: both Atlanta players play into our open slots, for **+58.5** that day.

VanVleet, against the other options:
- **Keeping him all week is worth +72.6.**
- **Keeping him through Saturday and dropping him Sunday is worth +101.4.**
- **His Milwaukee game barely moves this.**
  - Keeping him past Wednesday beats dropping him only while his rate is above **39.4**. It is 32.4 now.
  - It takes a **72 FP** game against Milwaukee to lift it that high (*Break-even*).
  - Short of that, drop him on Thursday.
- **The Saturday rest stops mattering.**
  - If he would sit Sat 31, dropping him Thursday is worth even more: +147.2 (*VanVleet rests Saturday* run).
- **Cost:** both drops are permanent.
  - VanVleet has 3 games next week, and Pritchard has 4.
  - We end the week holding Walter (3 games next week) and Toppin (3).

**Where it leaves us:**
- As rostered, the projected final is **1,451 to 1,731**. The plan adds +114.2, or +139.9 if Lendeborg sits.
- This read came while three games were live. The gains compare like with like; the totals will move.

**Swing factors:**
- **Lendeborg** (left foot soreness): questionable Wednesday at MIN, no timetable reported; ESPN est. 28 Oct.
- **Toppin** (left hand sprain): probable Wednesday vs PHI, no timetable reported; ESPN est. 28 Oct.
- **Allen's role** lasts while Charlotte is without:
  - Kon Knueppel (left hamstring): no timetable reported; ESPN est. 2 Nov.
  - Coby White (left calf strain): no timetable reported; ESPN est. 2 Nov.
- **Walter starts while Kawhi Leonard is out.** Leonard (left knee swelling) is out at least a week per the Raptors and several weeks per Shams; ESPN est. 23 Nov.
- **Duren** (IR, hamstring): re-evaluated in 2 weeks; ESPN est. 9 Nov.

## The rest of the week

| Day (US) | Melbourne | Ours playing | Open slots | Our lineup | Theirs playing | Their lineup |
|---|---|---:|---:|---:|---:|---:|
| Tue 27 Oct | Wed 28 | 4 | 6 | 140 | 5 | 207 |
| Wed 28 Oct | Thu 29 | 10 | 0 | 371 | 8 | 329 |
| Thu 29 Oct | Fri 30 | 2 | 8 | 77 | 5 | 186 |
| Fri 30 Oct | Sat 31 | 10 | 0 | 357 | 7 | 294 |
| Sat 31 Oct | Sun 01 | 3 | 7 | 109 | 9 | 352 |
| Sun 01 Nov | Mon 02 | 5 | 5 | 167 | 2 | 93 |

**Projection:** 1222 more for us and 1461 for them, for a final of **1451 to 1731**.

## Our roster

x = plays, o = has a game but is listed out.

| Player | NBA | Rate | Tue 27 | Wed 28 | Thu 29 | Fri 30 | Sat 31 | Sun 01 | Status |
|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| Cade Cunningham | DET | 46.3 | x | x |  | x |  |  |  |
| Kawhi Leonard | TOR | 45.0 |  | o |  | o |  | o | out, ESPN est. 23 Nov |
| Dejounte Murray | NO | 44.8 |  | x | x |  | x |  |  |
| Jamal Murray | DEN | 44.4 |  | x |  | x |  |  |  |
| Scottie Barnes | TOR | 39.4 |  | x |  | x |  | x |  |
| Yaxel Lendeborg | GS | 39.2 |  | x |  | x |  | x | day-to-day, ESPN est. 28 Oct |
| Caleb Wilson | CHI | 36.4 |  | x |  | x |  |  |  |
| Paul George | BOS | 35.8 | x |  |  | x |  | x |  |
| Fred VanVleet | HOU | 32.4 |  | x |  | x | x |  |  |
| Trey Murphy III | NO | 32.1 |  | x | x |  | x |  |  |
| Paul Reed | DET | 30.4 | x | x |  | x |  |  |  |
| Payton Pritchard | BOS | 27.2 | x |  |  | x |  | x |  |
| Desmond Bane | ORL | 25.8 |  | x |  | x |  | x |  |

IR: Jalen Duren (cannot score while in the IR slot).

What each player adds this week: our lineup total with him, minus without him. Low numbers mean his games fall on days we are already full.

| Player | Adds this week |
|---|---:|
| Kawhi Leonard | 0.0 |
| Caleb Wilson | 72.7 |
| Desmond Bane | 77.3 |
| Payton Pritchard | 81.5 |
| Jamal Murray | 88.9 |
| Paul Reed | 91.2 |
| Trey Murphy III | 96.3 |
| Fred VanVleet | 97.3 |
| Paul George | 107.5 |
| Yaxel Lendeborg | 117.7 |
| Scottie Barnes | 118.1 |
| Dejounte Murray | 134.4 |
| Cade Cunningham | 138.8 |

## Team Nic Kerr

| Player | NBA | Rate | Tue 27 | Wed 28 | Thu 29 | Fri 30 | Sat 31 | Sun 01 | Status |
|---|---|---:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| Luka Doncic | LAL | 57.4 | x | x |  | x |  | x |  |
| Tyrese Maxey | PHI | 51.4 |  | x |  | x | x |  |  |
| Domantas Sabonis | SAC | 49.8 | x |  | x |  | x |  |  |
| Trae Young | WSH | 42.6 |  | x |  | x |  |  |  |
| Chet Holmgren | OKC | 40.3 |  | o |  |  | x |  | out, ESPN est. 31 Oct |
| Ja Morant | POR | 37.8 | x |  | x |  | x |  |  |
| Jabari Smith Jr. | HOU | 37.6 |  | x |  | x | x |  |  |
| Moussa Diabate | CHA | 37.5 |  | x |  | x | x |  |  |
| Jarrett Allen | CLE | 36.5 |  | x | x |  | x |  |  |
| Michael Porter Jr. | BKN | 36.0 | x |  |  | x |  | x |  |
| James Harden | CLE | 35.2 |  | x | x |  | x |  |  |
| Alex Sarr | WSH | 31.1 |  | x |  | x |  |  |  |
| Darius Acuff Jr. | SAC | 26.3 | x |  | x |  | x |  |  |

## Streaming Payton Pritchard's slot

Keeping Payton Pritchard (BOS) is worth **54.3** this week: Tue 27 0, Fri 30 27, Sun 01 27.

### One add, now

| Free agent | NBA | Games | Now: GP, min, FP/g | Started | 2026 FP/g | Owned | vs keeping |
|---|---|---|---|---|---:|---:|---:|
| **Ja'Kobe Walter** | TOR | Wed, Fri, Sun | 3, 26.0, 34.7 | 1 of 3 | 17.7 | 10% | **+8.7** |
| **Reed Sheppard** | HOU | Wed, Fri, Sat | 3, 23.3, 29.3 | 1 of 3 | 30.1 | 64% | **+8.6** |
| **CJ McCollum** | ATL | Wed, Thu, Sat | 4, 26.8, 28.2 | 4 of 4 | 32.7 | 76% | **+8.6** |
| **Onyeka Okongwu** | ATL | Wed, Thu, Sat | 4, 26.5, 25.2 | 4 of 4 | 37.6 | 79% | **+6.8** |
| **Obi Toppin** (day-to-day, ESPN est. 28 Oct) | IND | Wed, Fri, Sun | 4, 23.2, 31.5 | 0 of 4 | 22.4 | 15% | **+6.2** |
| **Peyton Watson** | CLE | Wed, Thu, Sat | 3, 32.7, 28.0 | 3 of 3 | 29.8 | 45% | **+5.5** |
| **Aaron Wiggins** (day-to-day, ESPN est. 28 Oct) | ATL | Wed, Thu, Sat | 4, 27.5, 31.5 | 0 of 4 | 19.4 | 24% | **+3.5** |
| **Jaylen Wells** | MEM | Thu, Sat | 4, 29.0, 31.8 | 4 of 4 | 21.7 | 21% | **+3.1** |

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
| CJ McCollum (ATL) | Thu 29 Oct | Ja'Kobe Walter (TOR) | Fri 30 Oct | **+38.2** |
| Reed Sheppard (HOU) | Sat 31 Oct | Ja'Kobe Walter (TOR) | Sun 01 Nov | **+38.2** |
| CJ McCollum (ATL) | Thu 29 Oct | Reed Sheppard (HOU) | Fri 30 Oct | **+38.2** |
| Reed Sheppard (HOU) | Sat 31 Oct | Obi Toppin (IND) | Sun 01 Nov | **+37.4** |
| CJ McCollum (ATL) | Sat 31 Oct | Obi Toppin (IND) | Sun 01 Nov | **+37.4** |

### Lineup with Ja'Kobe Walter in the slot

| Day | Lineup | Playing | Sits |
|---|---:|---:|---|
| Tue 27 Oct | 140 | 4 | — |
| Wed 28 Oct | 375 | 11 | Desmond Bane |
| Thu 29 Oct | 77 | 2 | — |
| Fri 30 Oct | 360 | 10 | — |
| Sat 31 Oct | 109 | 3 | — |
| Sun 01 Nov | 170 | 5 | — |

## Rotating Payton Pritchard's and Fred VanVleet's slots

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, usable on any day: the limit is a matchup total, not a daily cap.
- Streamers considered: the 21 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1082** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+29.6** | Sun 01: VanVleet → Ja'Kobe Walter (TOR) |
| 2 | **+38.2** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Ja'Kobe Walter (TOR) |
| 3 | **+67.8** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 4 | **+96.6** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 5 | **+99.9** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Norman Powell (CHI); Sat 31: Powell → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 6 | **+114.8** | Wed 28: Pritchard → CJ McCollum (ATL); Thu 29: VanVleet → Onyeka Okongwu (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Fri 30: Okongwu → Grayson Allen (CHA); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: Allen → Obi Toppin (IND) |

Every drop of a player below is permanent: after his last game this week, dropping him still gains this week but costs his games next week (Payton Pritchard 4, Fred VanVleet 3).

### Keep one, rotate the other

Keeping a player here means through his last game this week; his slot can still turn over after it.

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 6 | +114.8 |
| Keep Payton Pritchard through Sun 01 Nov, rotate the rest | 4 | +56.7 |
| Keep Fred VanVleet through Sat 31 Oct, rotate the rest | 6 | +101.4 |
| Keep Fred VanVleet all week (never drop), rotate the rest | 5 | +72.6 |

### Break-even

The rate a player needs for keeping him through his last game this week to beat dropping him sooner, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.2): keep him while his rate is above **59.8**.
- **Fred VanVleet** (rate 32.4): keep him while his rate is above **39.4**. His Wed 28 game moves it: under **72 FP** (he averages 32.0) takes it below.

### Best plan: 6 adds, +114.8

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | CJ McCollum (ATL) plays | Fred VanVleet (HOU) plays | 375 | +3.8 | Desmond Bane |
| Thu 29 Oct | Fri 30 | CJ McCollum (ATL) plays | Onyeka Okongwu (ATL) plays | 135 | +58.5 | — |
| Fri 30 Oct | Sat 31 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 354 | −3.0 | — |
| Sat 31 Oct | Sun 01 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 133 | +24.2 | — |
| Sun 01 Nov | Mon 02 | Ja'Kobe Walter (TOR) plays | Obi Toppin (IND) plays | 199 | +31.2 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 07:00PM ET / Thu 29 10:00AM. Losing Payton Pritchard also costs his 4 games next week.
2. **Thu 29 Oct:** drop Fred VanVleet, add **Onyeka Okongwu** (ATL; GP, min, FP/g 4, 26.5, 25.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM. Losing Fred VanVleet also costs his 3 games next week.
3. **Fri 30 Oct:** drop CJ McCollum, add **Reed Sheppard** (HOU; GP, min, FP/g 3, 23.3, 29.3; started 1 of 3). By 08:00PM ET / Sat 31 11:00AM.
4. **Fri 30 Oct:** drop Onyeka Okongwu, add **Grayson Allen** (CHA; GP, min, FP/g 4, 27.8, 25.2; started 0 of 4). By 07:00PM ET / Sat 31 10:00AM.
5. **Sun 01 Nov:** drop Reed Sheppard, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.
6. **Sun 01 Nov:** drop Grayson Allen, add **Obi Toppin** (IND; GP, min, FP/g 4, 23.2, 31.5; started 0 of 4; day-to-day, ESPN est. 28 Oct). By 05:00PM ET / Mon 02 09:00AM.

Left holding at the end of the week: Ja'Kobe Walter (TOR, 3 games next week), Obi Toppin (IND, 3 games next week).

### Notes

- **Add limit:** checked against every executed add this season in ESPN's transaction log (`mTransactions2`, scoring periods 0–9).
  - Five teams made two or more adds in a single scoring period.
  - ESPN counts adds against `matchupAcquisitionLimit` × the matchup's scoring periods: 7 this week, as `docs/league-rules.md` §4 says.
- **Roles come from ESPN's box scores** (the *Started* column).
  - McCollum and Okongwu have started all 4 of Atlanta's games [AJC](https://www.ajc.com/sports/2026/10/hawks-roster/) [ESPN depth chart](https://www.espn.com/nba/team/depth/_/name/atl).
  - Atlanta plays Wed, Thu and Sat.
- **Grayson Allen** is Charlotte's sixth man, at about 28 minutes off the bench [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/grayson-allen-contributes-20-points-off-bench) [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-adds-15-points-off-bench/).
  - His minutes should shrink once Knueppel (ESPN est. 2 Nov) and Coby White (ESPN est. 2 Nov) return. Neither has a timetable reported.
- **Toppin** is probable Wednesday with a left hand sprain [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/obi-toppin-hand-probable-wednesday-vs-phi) [Pacers](https://x.com/Pacers/status/2115189159690223690). No timetable reported; ESPN est. 28 Oct.
- **Sheppard** comes off Houston's bench behind VanVleet [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-reed-sheppard-logs-28-minutes-off-bench). Houston plays Fri and Sat.
- **VanVleet** rested on 24 Oct, the second night of a back-to-back, as knee load management in his return from a torn ACL [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/fred-vanvleet-knee-out-saturday-vs-hawks).
  - Houston plays Fri 30 and Sat 31 back to back.
  - For the second night of a back-to-back, teams must file their injury report by 1 p.m. local time [NBA](https://official.nba.com/nba-injury-report-2025-26/).
- **Walter** has started since Kawhi Leonard went out [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/jakobe-walter-replaces-kawhi-knee-in-starting-5) [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/).
  - Leonard (left knee swelling) is out at least a week per the Raptors and several weeks per Shams; ESPN est. 23 Nov [ESPN](https://www.espn.com/nba/story/_/id/50298441/raptors-kawhi-leonard-weeks-due-knee-sources-say).
- **Lendeborg** is questionable Wednesday at Minnesota with left foot soreness, which he called "nothing crazy" [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/yaxel-lendeborg-foot-questionable-wednesday) [SI](https://www.si.com/nba/warriors/onsi/yaxel-lendeborg-s-foot-injury-has-status-in-doubt-for-warriors-timberwolves-game-01m5zmwrar9h).
  - Golden State may hold his status until after shootaround. No timetable reported; ESPN est. 28 Oct.

## What-if: Okongwu first

A run at 2026-10-28 01:28 UTC with `--sit` `CJ McCollum@2026-10-28`. Treating McCollum as unavailable Wednesday forces Okongwu into the Wednesday add, with everything else unchanged. Its 6-add row is the plan above.

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, usable on any day: the limit is a matchup total, not a daily cap.
- Streamers considered: the 22 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1082** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+29.6** | Sun 01: VanVleet → Ja'Kobe Walter (TOR) |
| 2 | **+38.2** | Wed 28: Pritchard → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 3 | **+67.0** | Wed 28: Pritchard → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 4 | **+95.4** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 5 | **+98.7** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Norman Powell (CHI); Sat 31: Powell → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 6 | **+114.2** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Thu 29: VanVleet → CJ McCollum (ATL); Fri 30: Okongwu → Reed Sheppard (HOU); Fri 30: McCollum → Grayson Allen (CHA); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: Allen → Obi Toppin (IND) |

Every drop of a player below is permanent: after his last game this week, dropping him still gains this week but costs his games next week (Payton Pritchard 4, Fred VanVleet 3).

### Keep one, rotate the other

Keeping a player here means through his last game this week; his slot can still turn over after it.

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 6 | +114.2 |
| Keep Payton Pritchard through Sun 01 Nov, rotate the rest | 4 | +56.7 |
| Keep Fred VanVleet through Sat 31 Oct, rotate the rest | 6 | +101.4 |
| Keep Fred VanVleet all week (never drop), rotate the rest | 5 | +72.6 |

### Break-even

The rate a player needs for keeping him through his last game this week to beat dropping him sooner, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.2): keep him while his rate is above **59.8**.
- **Fred VanVleet** (rate 32.4): keep him while his rate is above **39.0**. His Wed 28 game moves it: under **70 FP** (he averages 32.0) takes it below.

### Best plan: 6 adds, +114.2

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | Onyeka Okongwu (ATL) plays | Fred VanVleet (HOU) plays | 374 | +3.2 | Desmond Bane |
| Thu 29 Oct | Fri 30 | Onyeka Okongwu (ATL) plays | CJ McCollum (ATL) plays | 135 | +58.5 | — |
| Fri 30 Oct | Sat 31 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 354 | −3.0 | — |
| Sat 31 Oct | Sun 01 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 133 | +24.2 | — |
| Sun 01 Nov | Mon 02 | Ja'Kobe Walter (TOR) plays | Obi Toppin (IND) plays | 199 | +31.2 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **Onyeka Okongwu** (ATL; GP, min, FP/g 4, 26.5, 25.2; started 4 of 4). By 07:00PM ET / Thu 29 10:00AM. Losing Payton Pritchard also costs his 4 games next week.
2. **Thu 29 Oct:** drop Fred VanVleet, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM. Losing Fred VanVleet also costs his 3 games next week.
3. **Fri 30 Oct:** drop Onyeka Okongwu, add **Reed Sheppard** (HOU; GP, min, FP/g 3, 23.3, 29.3; started 1 of 3). By 08:00PM ET / Sat 31 11:00AM.
4. **Fri 30 Oct:** drop CJ McCollum, add **Grayson Allen** (CHA; GP, min, FP/g 4, 27.8, 25.2; started 0 of 4). By 07:00PM ET / Sat 31 10:00AM.
5. **Sun 01 Nov:** drop Reed Sheppard, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.
6. **Sun 01 Nov:** drop Grayson Allen, add **Obi Toppin** (IND; GP, min, FP/g 4, 23.2, 31.5; started 0 of 4; day-to-day, ESPN est. 28 Oct). By 05:00PM ET / Mon 02 09:00AM.

Left holding at the end of the week: Ja'Kobe Walter (TOR, 3 games next week), Obi Toppin (IND, 3 games next week).

## What-if: Lendeborg sits Wednesday

A run at 2026-10-28 01:28 UTC with `--sit` `Yaxel Lendeborg@2026-10-28`. Everything else is unchanged.

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, usable on any day: the limit is a matchup total, not a daily cap.
- Streamers considered: the 21 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1043** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+32.6** | Wed 28: Pritchard → Onyeka Okongwu (ATL) |
| 2 | **+62.8** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Ja'Kobe Walter (TOR) |
| 3 | **+92.3** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 4 | **+121.1** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 5 | **+124.4** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Fri 30: Okongwu → Norman Powell (CHI); Sat 31: Powell → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR); Sun 01: VanVleet → Obi Toppin (IND) |
| 6 | **+139.9** | Wed 28: Pritchard → Onyeka Okongwu (ATL); Thu 29: VanVleet → CJ McCollum (ATL); Fri 30: Okongwu → Reed Sheppard (HOU); Fri 30: McCollum → Grayson Allen (CHA); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: Allen → Obi Toppin (IND) |

Every drop of a player below is permanent: after his last game this week, dropping him still gains this week but costs his games next week (Payton Pritchard 4, Fred VanVleet 3).

### Keep one, rotate the other

Keeping a player here means through his last game this week; his slot can still turn over after it.

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 6 | +139.9 |
| Keep Payton Pritchard through Sun 01 Nov, rotate the rest | 4 | +56.7 |
| Keep Fred VanVleet through Sat 31 Oct, rotate the rest | 6 | +127.1 |
| Keep Fred VanVleet all week (never drop), rotate the rest | 5 | +98.3 |

### Break-even

The rate a player needs for keeping him through his last game this week to beat dropping him sooner, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.2): keep him while his rate is above **68.9**.
- **Fred VanVleet** (rate 32.4): keep him while his rate is above **39.0**. His Wed 28 game moves it: under **70 FP** (he averages 32.0) takes it below.

### Best plan: 6 adds, +139.9

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | Onyeka Okongwu (ATL) plays | Fred VanVleet (HOU) plays | 361 | +29.0 | — |
| Thu 29 Oct | Fri 30 | Onyeka Okongwu (ATL) plays | CJ McCollum (ATL) plays | 135 | +58.5 | — |
| Fri 30 Oct | Sat 31 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 354 | −3.0 | — |
| Sat 31 Oct | Sun 01 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 133 | +24.2 | — |
| Sun 01 Nov | Mon 02 | Ja'Kobe Walter (TOR) plays | Obi Toppin (IND) plays | 199 | +31.2 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **Onyeka Okongwu** (ATL; GP, min, FP/g 4, 26.5, 25.2; started 4 of 4). By 07:00PM ET / Thu 29 10:00AM. Losing Payton Pritchard also costs his 4 games next week.
2. **Thu 29 Oct:** drop Fred VanVleet, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM. Losing Fred VanVleet also costs his 3 games next week.
3. **Fri 30 Oct:** drop Onyeka Okongwu, add **Reed Sheppard** (HOU; GP, min, FP/g 3, 23.3, 29.3; started 1 of 3). By 08:00PM ET / Sat 31 11:00AM.
4. **Fri 30 Oct:** drop CJ McCollum, add **Grayson Allen** (CHA; GP, min, FP/g 4, 27.8, 25.2; started 0 of 4). By 07:00PM ET / Sat 31 10:00AM.
5. **Sun 01 Nov:** drop Reed Sheppard, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.
6. **Sun 01 Nov:** drop Grayson Allen, add **Obi Toppin** (IND; GP, min, FP/g 4, 23.2, 31.5; started 0 of 4; day-to-day, ESPN est. 28 Oct). By 05:00PM ET / Mon 02 09:00AM.

Left holding at the end of the week: Ja'Kobe Walter (TOR, 3 games next week), Obi Toppin (IND, 3 games next week).

## What-if: VanVleet rests Saturday

A run at 2026-10-28 01:28 UTC with `--sit` `Fred VanVleet@2026-10-31`. Saturday is the second night of Houston's Fri–Sat back-to-back. Everything else is unchanged.

- Free from: Payton Pritchard Wed 28 Oct, Fred VanVleet Thu 29 Oct. A slot can change from that US day, before its occupant's game that day.
- Each change is one add. 6 left this matchup, usable on any day: the limit is a matchup total, not a daily cap.
- Streamers considered: the 21 free agents worth most to an empty slot over these days (with 18+ minutes), plus the top three for each day.
- Keeping both scores **1050** in our lineup over Wed 28 Oct to Sun 01 Nov.

| Adds | vs keeping | Moves |
|---:|---:|---|
| 1 | **+31.0** | Sat 31: VanVleet → Jaxson Hayes (UTAH) |
| 2 | **+60.6** | Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |
| 3 | **+85.9** | Thu 29: VanVleet → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sun 01: Sheppard → Ja'Kobe Walter (TOR) |
| 4 | **+98.8** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Hayes → Ja'Kobe Walter (TOR) |
| 5 | **+127.6** | Wed 28: Pritchard → CJ McCollum (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Sat 31: VanVleet → Jaxson Hayes (UTAH); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: Hayes → Obi Toppin (IND) |
| 6 | **+147.2** | Wed 28: Pritchard → CJ McCollum (ATL); Thu 29: VanVleet → Onyeka Okongwu (ATL); Fri 30: McCollum → Reed Sheppard (HOU); Fri 30: Okongwu → Grayson Allen (CHA); Sun 01: Sheppard → Ja'Kobe Walter (TOR); Sun 01: Allen → Obi Toppin (IND) |

Every drop of a player below is permanent: after his last game this week, dropping him still gains this week but costs his games next week (Payton Pritchard 4, Fred VanVleet 3).

### Keep one, rotate the other

Keeping a player here means through his last game this week; his slot can still turn over after it.

| Scenario | Adds | vs keeping both |
|---|---:|---:|
| Rotate both | 6 | +147.2 |
| Keep Payton Pritchard through Sun 01 Nov, rotate the rest | 4 | +89.2 |
| Keep Fred VanVleet through Fri 30 Oct, rotate the rest | 6 | +130.8 |
| Keep Fred VanVleet all week (never drop), rotate the rest | 5 | +72.6 |

### Break-even

The rate a player needs for keeping him through his last game this week to beat dropping him sooner, with the other slots rotating as above.

- **Payton Pritchard** (rate 27.2): keep him while his rate is above **59.8**.
- **Fred VanVleet** (rate 32.4): keep him while his rate is above **48.9**. His Wed 28 game moves it: under **126 FP** (he averages 32.0) takes it below.

### Best plan: 6 adds, +147.2

| Day (US) | Melbourne | Slot 1 | Slot 2 | Our lineup | vs keeping | Sits |
|---|---|---|---|---:|---:|---|
| Wed 28 Oct | Thu 29 | CJ McCollum (ATL) plays | Fred VanVleet (HOU) plays | 375 | +3.8 | Desmond Bane |
| Thu 29 Oct | Fri 30 | CJ McCollum (ATL) plays | Onyeka Okongwu (ATL) plays | 135 | +58.5 | — |
| Fri 30 Oct | Sat 31 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 354 | −3.0 | — |
| Sat 31 Oct | Sun 01 | Reed Sheppard (HOU) plays | Grayson Allen (CHA) plays | 133 | +56.6 | — |
| Sun 01 Nov | Mon 02 | Ja'Kobe Walter (TOR) plays | Obi Toppin (IND) plays | 199 | +31.2 | — |

Moves, each made before the earlier tip-off of the two players that day:

1. **Wed 28 Oct:** drop Payton Pritchard, add **CJ McCollum** (ATL; GP, min, FP/g 4, 26.8, 28.2; started 4 of 4). By 07:00PM ET / Thu 29 10:00AM. Losing Payton Pritchard also costs his 4 games next week.
2. **Thu 29 Oct:** drop Fred VanVleet, add **Onyeka Okongwu** (ATL; GP, min, FP/g 4, 26.5, 25.2; started 4 of 4). By 08:00PM ET / Fri 30 11:00AM. Losing Fred VanVleet also costs his 3 games next week.
3. **Fri 30 Oct:** drop CJ McCollum, add **Reed Sheppard** (HOU; GP, min, FP/g 3, 23.3, 29.3; started 1 of 3). By 08:00PM ET / Sat 31 11:00AM.
4. **Fri 30 Oct:** drop Onyeka Okongwu, add **Grayson Allen** (CHA; GP, min, FP/g 4, 27.8, 25.2; started 0 of 4). By 07:00PM ET / Sat 31 10:00AM.
5. **Sun 01 Nov:** drop Reed Sheppard, add **Ja'Kobe Walter** (TOR; GP, min, FP/g 3, 26.0, 34.7; started 1 of 3). By 09:00PM ET / Mon 02 01:00PM.
6. **Sun 01 Nov:** drop Grayson Allen, add **Obi Toppin** (IND; GP, min, FP/g 4, 23.2, 31.5; started 0 of 4; day-to-day, ESPN est. 28 Oct). By 05:00PM ET / Mon 02 09:00AM.

Left holding at the end of the week: Ja'Kobe Walter (TOR, 3 games next week), Obi Toppin (IND, 3 games next week).

## Tip-off times

For the teams named above. Times are ET / Melbourne.

- **ATL:** Wed 28 07:00PM / Thu 29 10:00AM; Thu 29 08:00PM / Fri 30 11:00AM; Sat 31 07:00PM / Sun 01 10:00AM
- **BOS:** Tue 27 07:30PM / Wed 28 10:30AM; Fri 30 07:30PM / Sat 31 10:30AM; Sun 01 03:30PM / Mon 02 07:30AM
- **CHA:** Wed 28 07:00PM / Thu 29 10:00AM; Fri 30 07:00PM / Sat 31 10:00AM; Sat 31 06:00PM / Sun 01 09:00AM
- **CLE:** Wed 28 07:00PM / Thu 29 10:00AM; Thu 29 08:00PM / Fri 30 11:00AM; Sat 31 08:00PM / Sun 01 11:00AM
- **HOU:** Wed 28 08:00PM / Thu 29 11:00AM; Fri 30 08:00PM / Sat 31 11:00AM; Sat 31 08:30PM / Sun 01 11:30AM
- **IND:** Wed 28 07:00PM / Thu 29 10:00AM; Fri 30 08:00PM / Sat 31 11:00AM; Sun 01 05:00PM / Mon 02 09:00AM
- **MEM:** Thu 29 10:00PM / Fri 30 01:00PM; Sat 31 08:00PM / Sun 01 11:00AM
- **TOR:** Wed 28 07:30PM / Thu 29 10:30AM; Fri 30 07:30PM / Sat 31 10:30AM; Sun 01 09:00PM / Mon 02 01:00PM

## Sources

- ESPN fantasy API, league 423671879 (`mRoster`, `mTeam`, `mMatchupScore`, `mSettings`, `mStatus`, `kona_player_info`, `proTeamSchedules_wl`) and ESPN's NBA injury feed, read 2026-10-28 01:28 UTC.
- Research, 28 Oct 2026: [AJC](https://www.ajc.com/sports/2026/10/hawks-roster/); [ESPN depth chart](https://www.espn.com/nba/team/depth/_/name/atl); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/grayson-allen-contributes-20-points-off-bench); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/hornets-grayson-allen-adds-15-points-off-bench/); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/obi-toppin-hand-probable-wednesday-vs-phi); [Pacers](https://x.com/Pacers/status/2115189159690223690); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/rockets-reed-sheppard-logs-28-minutes-off-bench); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-24/fred-vanvleet-knee-out-saturday-vs-hawks); [NBA](https://official.nba.com/nba-injury-report-2025-26/); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-25/jakobe-walter-replaces-kawhi-knee-in-starting-5); [CBS Sports](https://www.cbssports.com/fantasy/basketball/news/raptors-jakobe-walter-thrives-in-starting-role/); [ESPN](https://www.espn.com/nba/story/_/id/50298441/raptors-kawhi-leonard-weeks-due-knee-sources-say); [NBC Sports](https://www.nbcsports.com/fantasy/basketball/player-news/2026-10-27/yaxel-lendeborg-foot-questionable-wednesday); [SI](https://www.si.com/nba/warriors/onsi/yaxel-lendeborg-s-foot-injury-has-status-in-doubt-for-warriors-timberwolves-game-01m5zmwrar9h); Duren [ESPN](https://www.espn.com/nba/story/_/id/50277066/pistons-jalen-duren-hamstring-strain-least-2-weeks).
- ESPN fantasy API `mTransactions2`, scoring periods 0–9, read 28 Oct 2026 01:15 UTC.
