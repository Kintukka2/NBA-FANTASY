---
name: trade-watch
description: Run the Trade Watch. It finds NBA trades (and releases of rotation players) that suddenly change a player's opportunity. On the team he left, it covers the role he vacated and who is taking his minutes. On the team he joined, it covers the gap he can fill: long injuries at his positions, the depth chart, and whose minutes he takes. Research agents check each trade on the web, the confirmed roles can go into council/news_overrides.csv, and the report is saved to docs/analysis/. Use when the user asks for the trade watch, about NBA trades, who benefits from a trade, a traded player's new role, or types "/trade-watch".
---

# Trade Watch

A trade changes opportunity on two teams at once:
- The team he left loses his minutes and shots, and someone there takes them.
- The team he joined has a gap he may fill: an injured starter, a thin position, a missing scorer.

The rate (`council/gamelog.py`) only learns this game by game. The trade watch spots it the day the trade happens.

- `council/trade_watch.py` reads ESPN's NBA transactions feed and the box scores.
- Research agents check each trade on the web.
- Confirmed roles can go into `council/news_overrides.csv`, which `council/matchup.py` applies.

Never compute or edit a figure the script wrote.

## 1. Run the script

```bash
python council/espn_sync.py
python council/trade_watch.py --out docs/analysis/<YYYYMMDD>-trade-watch.md \
  --json <scratchpad>/trade-flags.json
```

Use today's UTC date in the filename. The JSON is the brief for the research agents. Keep it in the scratchpad: don't commit it.

Options:

| Option | Default | Meaning |
|---|---|---|
| `--days` | 30 | trades this many days old or newer |
| `--games` | 10 | recent team games read for depth and the with/without splits |
| `--min-days` | 7 | an injury on the new team counts as a gap when ESPN expects it to last longer than this |
| `--min-minutes` | 15 | a waived player is listed when he played this many minutes a game for the team that waived him |

What the script reports for each traded player in the league pool (rostered, free agent or waivers):

| Part | What it holds |
|---|---|
| **Summary** | Date, from → to, his role before (games, minutes, FP/g, starts with the old team), his role since, rate, league status. |
| **The team he left** | The role he vacated. Once the old team has played without him, a with/without split of his teammates (minutes, FP/g, starts), like the injury watch. Before that, the teammates at his positions: the likeliest heirs. |
| **The team he joined** | Long absences at his positions (injury, ESPN est., their minutes) and the minutes they free up; the depth at his positions over the last `--games` games; once he has played, whose minutes he takes. |
| **Waived rotation players** | Releases of players who played `--min-minutes`+ for the team that waived them. Those minutes are open too. |

If something goes wrong:
- **"Games in progress":** tell the user which games are live and when to run it again. Pass `--allow-live` only if they ask for a mid-game read.
- **A scoring mismatch:** the script exits without a report. Report it, and never patch the numbers.

## 2. Research: required

Spawn research agents with the Agent tool (`general-purpose`), in parallel, one per trade (at most 4). Brief each with the trade's JSON entry, pasted or as a scratchpad file path, and these instructions:

> Search the web, using `extended` mode for the last few days. Answer, each bullet with a link and the source's date:
>
> 1. **The trade:** who went where, and why (salary, a role, an injury on the new team).
> 2. **His new role:** starter or bench, expected minutes, coach or beat-writer comments, his debut date, and which injured or departed player he replaces.
> 3. **The team he left:** who takes his minutes and shots. Name players and minutes where a source gives them.
> 4. **The team he joined:** whose minutes he takes, especially any rostered fantasy player.
> 5. **Verdict:** opportunity up, down or unchanged for him and for each player named, and how long it lasts (until an injured player returns, say).
>
> Never invent a source.

Also send one agent to search for **trades reported in the last few days that ESPN's feed has not listed yet** (agreed but not official, or pending physicals). List each with its source and the players' roles.

Do the checks yourself, not the agents: verify any surprising claim against a second source, and every proposed override row against its source.

## 3. Record what is confirmed

When a source reports a traded player's new role as ongoing, add a `role` row to `council/news_overrides.csv`. That covers a confirmed starter, or a stated minutes range. Format: `player,kind,value,until,source,note`, with value = expected minutes and until = at most 14 days ahead. The news watch skill sets the rules: a linked source, one row per player and kind, and expired rows removed. `council/matchup.py` then values him at his role rate (FP per minute this season × those minutes), marked ‡.

A small sample of minutes with his old team makes the role rate unreliable. Say so, and prefer no row to a guess.

## 4. Write the report

In the report file:
1. Replace each `- _pending_` under **Research** with the sourced bullets and the verdict.
2. Add a **What it means for us** section after the header:
   - pickups (free agents and waiver players whose opportunity jumps);
   - threats to our players' minutes;
   - any override added.
3. Keep the CLAUDE.md rules:
   - **Injury timelines:** every injured player named shows the reported timeline (linked) and *ESPN est.*
   - **Recent form:** L7, L15 and L30 with games for every player judged. Run `python council/form.py "<name>"` for anyone the script did not print.
   - **Small samples:** say "small sample" beside them.
4. Add every link to `## Sources`.

## 5. Deliver

- Commit the report and any `council/news_overrides.csv` change, push, and follow the session's PR rules.
- In the reply:
  - lead with what changes for us: pickups, threats, and overrides added;
  - give each traded player's new role in one line;
  - keep the CLAUDE.md rules on injury timelines, L7/L15/L30 and small samples.

When the user asks to run all skills, run the trade watch with the news watch, before the matchup, so its overrides feed the plan.
