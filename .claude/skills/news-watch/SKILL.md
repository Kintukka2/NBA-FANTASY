---
name: news-watch
description: Run the News Watch. It reads the news ESPN's fantasy app shows for our roster, the best free agents and waiver players, our opponents this week and next, and injuries across the league's rosters, and flags what the rate misses or ESPN gets wrong. That covers an injury date the news contradicts, a move into or out of the starting lineup, a minutes trend or limit, a back-to-back rest signal, and an out listing with no date or no news. Research agents then check each flag on the web, the confirmed findings go into council/news_overrides.csv (the matchup plans apply them), and the report is saved to docs/analysis/. Use when the user asks for the news watch, what the news says, whether ESPN's injury dates or labels are right, role or minutes changes, rest days, or types "/news-watch".
---

# News Watch

The rate (`council/gamelog.py`) only knows games already played. ESPN's
injury labels and return dates are often placeholders. The news watch closes
that gap:

- `council/news_watch.py` reads ESPN's player news and the box scores, and
  flags the players where they disagree or something has changed.
- Research agents check each flag on the web.
- What they confirm goes into `council/news_overrides.csv`, which
  `council/matchup.py` applies in place of ESPN's estimate and the rate.

Never compute or edit a figure the script wrote.

## 1. Run the script

```bash
python council/espn_sync.py
python council/news_watch.py --out docs/analysis/<YYYYMMDD>-news-watch.md \
  --json <scratchpad>/news-flags.json
```

Use today's UTC date in the filename. The JSON holds every flagged player
with his full news notes, last 5 games and ESPN status. It is the brief for
the research agents. Keep it in the scratchpad: don't commit it.

Options. Pass any the user gives:

| Option | Default | Meaning |
|---|---|---|
| `--ours` | off | our roster only |
| `--fa` | 40 | free agents and waiver players checked, by rate |
| `--value` | 25 | injured free agents and waiver players are also checked when last season (or the projection) is worth this many FP/g |
| `--days` | 4 | news this many days old or newer is read for role, minutes and rest |
| `--soon` | 7 | an ESPN return within this many days is checked against talk of a longer absence |
| `--stale` | 5 | days without news that make an "out" listing a gap |
| `--min-change` | 5 | minutes change over the last 3 games that is flagged |
| `--ahead` | 7 | days ahead to look for back-to-backs |

What the script flags:

| Flag | Means |
|---|---|
| **injury** | ESPN expects him back within `--soon` days but the news talks of weeks, no timetable, surgery or a re-evaluation; or ESPN's date has passed; or he played after being listed out; or newer news points to a return; or a fresh note names an injury ESPN's feed does not list. |
| **role** | The box scores show him moving into the starting lineup (started 1+ of his last 2 games after 25% or fewer before) or out of it, or a headline announces it. |
| **minutes** | His last 3 games' minutes are `--min-change`+ off his season's (outlier games left out), or the news mentions a minutes limit or a bigger or smaller role. |
| **rest** | His team has a back-to-back in the next `--ahead` days and the news mentions rest or load management, or he sat one night of an earlier back-to-back while playing the games either side. |
| **gap** | Listed out with no ESPN return date, or (when due back within 14 days) with no news in `--stale` days. |

Scope:
- our roster
- the top `--fa` free agents and waiver players by rate, plus injured ones worth `--value`+
- this week's and next week's opponents, with every flag
- every other team's roster, with injury and gap flags only

**Role rate** = FP per minute this season (outlier games left out) × his
minutes in the new role. The report shows it beside the rate. The plans use it
only after step 3 records the role.

If something goes wrong:
- **"Games in progress":** tell the user which games are live and when to run it again. Pass `--allow-live` only if they ask for a mid-game read.
- **A scoring mismatch:** the script exits without a report. Report it, and never patch the numbers.

## 2. Research: required

Every flag is a question, not a finding. Spawn research agents with the
Agent tool (`general-purpose`), in parallel, in one message:

- **Batches:** up to 5 flagged players per agent, at most 4 agents.
  If more players are flagged, run a second round.
- **Priority:**
  1. our roster
  2. free agents and waiver players with an injury flag, or in the top 15 by rate
  3. our opponents
  4. the rest

Brief each agent with its players' entries from the JSON. Paste them in full,
or write each batch to its own scratchpad file and give the agent the path.
Add these instructions:

> Search the web for the latest news on each player, using `extended` mode for anything from the last few days. Answer every flag:
>
> - **injury:** What is the latest reported timeline from the team, a beat writer or the NBA's official injury report, and its date? Is ESPN's estimate right, too early or too late? Give the first game he is expected to play, if a source supports one.
> - **role:** Is the lineup change ongoing, or a one-off (a teammate resting, a matchup)? Whose return ends it? What minutes is he expected to play?
> - **minutes:** What explains the change (a lifted restriction, a rotation change, blowouts, foul trouble)? Will it last?
> - **rest:** Has the team said he will sit a night of the back-to-back? Does he have a pattern of resting on back-to-backs?
> - **gap:** What is his status now?
>
> For each player, return:
> - one or two sourced bullets per flag, each with a link and the source's date;
> - a verdict: *ESPN confirmed*, *ESPN corrected* or *nothing new found*;
> - proposed override rows, in the CSV format below, only where a linked source supports them.
>
> Override rows: `player,kind,value,until,source,note`
>
> - **`return`**: value = the first date he can play.
>   - When a source gives a re-evaluation date, use the day after it.
>   - When it says "week-to-week" with no date, use 7 days after the note and say it is a floor.
>   - When that floor has passed and he is still listed out with no timetable, use 7 days after the latest out report.
> - **`sit`**: value = a date he will not play. Only when the team or a beat writer says so.
> - **`role`**: value = expected minutes; `until` = when the role is expected to end, at most 14 days ahead. Only when the source reports the role as ongoing.
>
> Use the player's name exactly as given. Never invent a source.

Do the checks yourself, not the agents: injury dates against the official
NBA injury report when the agents disagree, and every proposed row against
its source.

## 3. Record the overrides

Edit `council/news_overrides.csv`:

- Add each confirmed row with its source URL and a short note.
- Remove the rows the report's **Overrides** table marks *expired*.
- Replace a row when newer news changes it, and keep one row per player and kind.
- Never add a row without a linked source.
- Never record a roster move here: `python council/espn_sync.py` syncs `council/roster.csv` from ESPN.

`council/matchup.py` applies the file:
- a player is out before his `return` date and plays from it, whatever ESPN says;
- he misses each `sit` date;
- his role rate replaces his rate while the `role` row is in force, marked ‡.

## 4. Write the report

In the report file:

1. Replace each `- **Research:** _pending_` with the sourced bullets and the
   verdict. Where a row was added, add `Override: <kind> <value>`.
2. Add a **What changed for us** section after the header:
   - our players' corrected timelines and roles;
   - targets whose value moved;
   - the overrides added or removed.
3. Keep the CLAUDE.md rules:
   - **Injury timelines:** every injured player named shows the reported timeline (linked) and *ESPN est.*, or "no timetable reported".
   - **Recent form:** L7, L15 and L30 with games beside the season average. The script prints them; a 5+ L7 gap gets a reason.
   - **Small samples:** say "small sample" where a rate rests on 2 games or fewer (the script marks †).
4. Add every link to the `## Sources` list.

## 5. Deliver

- Commit the report and `council/news_overrides.csv`, push, and follow the session's PR rules.
- In the reply, lead with what changed for us:
  - our players' real timelines;
  - role or minutes changes worth acting on;
  - injured targets whose return ESPN misdates;
  - the overrides added, and which matchup projections they move.
- Say whether to re-run `/matchup`: always when an override touches this week's rosters.
- Keep the CLAUDE.md rules in the reply too: injury timelines, L7/L15/L30, small samples.

When the user asks to run all skills, run the news watch first, so the
matchup plan uses its overrides.
