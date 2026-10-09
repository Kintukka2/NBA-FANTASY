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

`council/roster.csv` is our live roster. Whenever the user reports a move
(add, drop, IR, trade), update it in the same turn and commit: remove the
dropped player, add the new one with `acquired` and `acquired_on`, set
`slot` to `IR` for an IR stash. Only record moves the user says were made,
never planned ones.
