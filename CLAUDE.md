# NBA-FANTASY

Source material for the Draft Council (GONG league 423671879, 2026-27). Read
`README.md` for the data layout and its rules of engagement.

When the user asks "the council" anything, or uses `/council`, follow
`.claude/skills/council/SKILL.md`: first the non-voting researcher
(`council-researcher`) searches the web and writes a sourced briefing to
`docs/research/`, then nine persona agents (`council/members.json`,
`.claude/agents/council-*.md`) research `docs/` and `data/`, vote, and the
highest-voted answer is reported. Votes are counted by `council/tally.py`,
never by hand. Sessions are saved to `council/sessions/`.

When the user asks for the slump watch, who is underperforming, or uses
`/slump-watch`, follow `.claude/skills/slump-watch/SKILL.md`. Run
`council/slump_watch.py` and never compute its figures by hand. It refuses
to run while NBA games are live.

When the user asks for the injury watch, injury replacements, who to pick up
because of injuries, or uses `/injury-watch`, follow
`.claude/skills/injury-watch/SKILL.md`. Run `council/injury_watch.py`, then
add sourced research. It refuses to run while NBA games are live.

When the user asks for the news watch, what the news says, whether ESPN's
injury dates are right, role or minutes changes, rest days, or uses
`/news-watch`, follow `.claude/skills/news-watch/SKILL.md`. Run
`council/news_watch.py`, then research agents check every flag on the web.
When running all skills, run the news watch first so the matchup uses its
overrides. It refuses to run while NBA games are live.

When the user asks for the trade watch, about NBA trades, who benefits from
a trade, or a traded player's new role, or uses `/trade-watch`, follow
`.claude/skills/trade-watch/SKILL.md`. Run `council/trade_watch.py`, then
research agents check each trade. When running all skills, run it with the
news watch, before the matchup. It refuses to run while NBA games are live.

When the user asks to prepare for the matchup, who to stream, who to pick up
for particular days, or uses `/matchup`, follow
`.claude/skills/matchup/SKILL.md`. Run `council/matchup.py`, then add
research and a plan. It refuses to run while NBA games are live.

**Injury timelines, always.** Whenever a reply or a report names an injured
player, give the expected return next to the name:

- the reported timeline (team or beat source, linked) when one exists
- ESPN's estimate from `python council/injuries.py`, labelled *ESPN est.*

If nothing has been reported, say "no timetable reported" and still give
ESPN's estimate. Never list injured players by name alone.

**Recent form, always: 7, 15 and 30 days.** Every player analysis (a reply,
a report, a plan, a council ballot) that judges a player gives their FP/g
over the last 7, 15 and 30 days, with games played, beside the season
average and ESPN's projection:

- The report scripts print them as `L7`, `L15` and `L30` columns. For any
  other player, run `python council/form.py "<name>" ...` (or `--ours`) and
  quote it. Never compute the windows by hand.
- When L7 is 5+ FP/g off the season average, say so and give the reason
  (minutes, role, injury, shooting), or say that none was found.
- State the sample: a window of 1 or 2 games is noise and is called that.
  Early in the season L15 and L30 equal the season average, and the scripts
  say so.
- **Outlier games** (`council/gamelog.py`): a bad game (worst FP, 12+ under
  the next worst, 3+ games) and a short game (fewest minutes, more than 10
  under the next fewest, 2+ games) are dropped. The scripts show such a
  window as **A → B**, B being the average without the outlier. Quote both.
  Good games are never dropped.

**Small samples, always flagged.** When a player's rate or an average rests on
2 games or fewer (after any dropped outlier), say "small sample" beside it,
in every reply, report, plan and ballot. The scripts mark these rates with
**†** or "(small sample)". Example: Yves Missi's rate rests on one 68-FP
game after his 9-minute injury exit was dropped.

**The rate every plan uses** (`council/gamelog.py`, used by `matchup.py`):
last season ×1 (ESPN's projection if none), this season ×2, L30 ×3, L15 ×4,
L7 ×5, each outlier-adjusted, skipping parts with no games. `form.py` prints
it as **Rate**. Never compute it by hand.

**Opponent factor: information only.** `matchup.py` shows each game's
**opponent factor** (`council/opponents.py`: what opponents score against
that team over their own averages, by position, shrunk toward even and
capped at ±15%) as `@WSH +6%`. `b2b` marks a back-to-back's second night.

- The factor stays out of projections, gains and plans until its audit
  (`python council/opponents.py --audit`) certifies it.
- The audit replays the season with only earlier games and tests the factor
  against what players actually scored. Every matchup header prints its
  verdict.
- `--opp` applies the factor as a what-if. Label any such figure as a what-if.

**ESPN's labels are not taken at face value.** Return dates, roles and rest
days that the news watch research confirms go into `council/news_overrides.csv`
(`return`, `sit`, `role`), one sourced row each, with a date it ends.
`matchup.py` applies them in place of ESPN's estimate and the rate:

- a **role rate** (FP per minute this season × the confirmed minutes) replaces the rate, marked **‡**;
- quote the role rate beside the rate;
- never add a row without a linked source, and remove expired rows.

**Adds left: only from `matchup.py`.** The weekly limit follows that week's
NBA game days, so a week with an empty day has 6. Quote the limit and the
adds used from the script's **Adds** line (`--next` for next week). Live
games don't change that line, so `--allow-live` is fine for it. Never
assume 7.

**ESPN is the source of truth for rosters.** `python council/espn_sync.py`
writes `council/roster.csv` and `council/taken.txt` to match the ESPN app:
adds, drops, IR moves and trades. Every skill runs it first. Commit what it
changes and name the moves it recorded in the reply. No confirmation from the
user is needed. When the user mentions a move, run the sync rather than
editing the file by hand. A planned move is not on ESPN, so it is not
recorded.
