# GONG League — Rules Reference

**League ID:** 423671879 · **Sport:** ESPN Fantasy Basketball (fba) · **Season:** 2026-27
**Format:** Head-to-head, points scoring, 8 teams, single division ("Snakepit Championship 26")
**Source:** pulled directly from the league's own configuration (`view=mSettings&view=mTeam`) on 8 Oct 2026. This is the league's live config, not a guess.

---

## 1. Draft

| Setting | Value |
|---|---|
| Type | **Snake** |
| Date/time | **Thu 8 Oct 2026, 19:45 AEDT** (08:45 UTC) |
| Draft room opens | 18:45 AEDT (one hour early) |
| Time per pick | **90 seconds** |
| Rounds | **13** (one per roster spot) |
| Keepers | 0 |
| Trading during draft | Disabled |
| Players available | All 1,095 — nothing is drafted or rostered yet |

**Pick order (round 1):**

1. Dr White Slong `BWC`
2. Team Nic Kerr `NIc`
3. Lauri Birds `TF`
4. Melbourne poopoo `MEL`
5. Cream Abdul-Yammar `YAM`
6. Matt Wright's Foxies `FOX`
7. Cheeky Blinders `CHKY`
8. **Come-in Cider `CCDR` ← our team**

Snake reverses each round, so slot *n* picks at `n`, `17−n`, `16+n`, `33−n`, and so on.

### Our picks — slot 8 (the turn)

Last pick of odd rounds, first pick of even rounds, so we pick **back-to-back every time**:

| Round | Overall picks |
|---|---|
| 1 → 2 | **8, 9** |
| 3 → 4 | **24, 25** |
| 5 → 6 | **40, 41** |
| 7 → 8 | **56, 57** |
| 9 → 10 | **72, 73** |
| 11 → 12 | **88, 89** |
| 13 | **104** |

**What the turn means for us.** We never get a player at the top of a tier, but we always get two bites at once. The right way to use that is to treat each turn as a *pair* decision rather than two separate picks — take two players who complement each other, and accept that anyone we're deciding between at pick 8 will be gone by pick 24. Practically: at every turn, identify the two best players available under *our* scoring and take both, rather than reaching for positional need. The cost of the turn is that we wait 15 picks between turns; the benefit is we can build positional pairs (e.g. two bigs, or a steals specialist plus an efficient scorer) without a rival splitting them.

**League members (display names):** ESPNFAN7429974536 · Richo4 · P-diddy707 · Christmas Jones · tomfarrar · ESPNFAN6645801983 · kyle.booth2 · BurtonIsMyDaddy

---

## 2. Scoring — this is a custom build, not an ESPN default

| Category | Points | Note |
|---|---:|---|
| Point scored (PTS) | **+1** | |
| Field goal made (FGM) | **+2** | a made FG is worth 2+2 = effectively 4 on a two-pointer |
| Field goal attempted (FGA) | **−1** | misses are punished |
| Free throw made (FTM) | **+1** | |
| Free throw attempted (FTA) | **−1** | |
| Three pointer made (3PM) | **+1** | on top of the 3 PTS and the FGM bonus |
| Rebound (REB) | **+1** | |
| Offensive rebound (OREB) | **+1 extra** | OREB scores twice — once as REB, once again here |
| Assist (AST) | **+2** | |
| Steal (STL) | **+4** | |
| Block (BLK) | **+4** | |
| Turnover (TO) | **−2** | |
| Double-double (DD) | **+3** | |
| Triple-double (TD) | **+6** | |
| Quadruple-double (QD) | **+40** | |
| Personal foul (PF) | 0 | not scored |

**The exact formula** (verified against ESPN's own fantasy totals across all 558 players with 2026 production — mean deviation −0.01 pts, max 3.8, zero outliers):

```
FPTS = PTS + 2·FGM − FGA + FTM − FTA + 3PM + REB + OREB + 2·AST + 4·STL + 4·BLK − 2·TO
       (per game, × GP)  + 3·DD + 6·TD + 40·QD  (season totals)
```

### What this scoring rewards

- **Steals and blocks are the single biggest lever.** At +4 each they are worth four points apiece, the same as two assists or four rebounds. A 1.5 STL / 1.5 BLK guard or wing is enormously more valuable here than in a standard points league.
- **Efficiency matters more than volume.** A missed field goal costs −1 and returns nothing. A made two-pointer is worth 2 (PTS) + 2 (FGM) − 1 (FGA) = **+3 net**; a miss is **−1**. So a two-point jumper breaks even at roughly **25% FG**. A made three is 3 + 2 + 1 − 1 = **+5 net**, breaking even near **17% 3P**. Volume shooting is still profitable, but high-FGA / low-FG% guards bleed value relative to their raw scoring.
- **Free throws are nearly neutral.** Made FT = +1+1−1 = **+1**; missed FT = **−1**. Free-throw volume is a small positive only for good shooters.
- **Offensive rebounds count double.** Big men who live on the offensive glass get paid twice.
- **Turnovers are expensive.** −2 per turnover means a high-usage ball handler with 4 TO/g is giving back 8 points a night.
- **Centers and defensive specialists are structurally underpriced** relative to ESPN's own ADP, because ADP is built for standard scoring.

---

## 3. Roster

| Slot | Count |
|---|---:|
| PG | 1 |
| SG | 1 |
| SF | 1 |
| PF | 1 |
| C | 1 |
| G (PG/SG) | 1 |
| F (SF/PF) | 1 |
| UTIL | 3 |
| **Starters** | **10** |
| Bench (BE) | 3 |
| IR | 1 |
| **Total roster spots** | **13** (+1 IR) |

- **Position limit:** maximum **4** players at the G slot grouping; all other positions unlimited.
- **Lineup changes:** unlimited (no move limit).
- Ten of thirteen players start every week. The bench is only three deep, so **there is very little room to stash upside**. Every pick needs to be someone you would plausibly start.

---

## 4. Waivers & acquisitions

| Setting | Value |
|---|---|
| Waiver type | Traditional waivers (**no FAAB / no budget**) |
| Waiver period | 24 hours |
| Processing | **Sundays, 08:00** |
| Waiver order | Does **not** reset after a claim |
| Season acquisition limit | Unlimited |
| Per-matchup acquisition limit | **Scales with the week — roughly 7 typical, ~4 in light weeks** |
| Lineup changes | **Unlimited, daily** (`moveLimit: -1`) |

> The raw config shows `matchupAcquisitionLimit: 1`, but that is the value for the **current** (preseason) matchup period, not a season-long cap. Per league experience the limit is recalculated each week in proportion to the number of NBA game days in that period — typically around **7**, dropping to about **4** in compressed weeks (All-Star break, etc.). Confirmed by HIMOTHY, 8 Oct 2026.

**This is the single most strategically important setting in the league.** Around seven adds a week, combined with unlimited daily lineup changes, means the waiver wire is a live, continuously usable tool rather than an emergency measure. See §8.

---

## 5. Schedule & playoffs

| Setting | Value |
|---|---|
| Scoring period | **Weekly** |
| Regular season | **20 match