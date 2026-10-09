---
name: council
description: Put a question to the Draft Council. A non-voting researcher first searches the web and writes a sourced briefing to docs/research/; then nine persona agents each research NBA-FANTASY docs/ and data/ from their own angle, cast a weighted vote (yes/no, a selection, or a suggestion), a runoff settles any split, and the highest-voted answer is reported. Use for any draft or fantasy question the user wants "the council" to decide, e.g. "/council Clingan or Sengun at 24?".
---

# Convene the Draft Council

The question is in the arguments (or the user's message). The roster, vote
weights and personas live in `council/members.json` (the researcher under
`researcher`); the rules are in
`council/PROTOCOL.md`. Counting is done by `council/tally.py`, never by you.

## 1. Frame the motion

Decide the type and write the options. Do not research the answer yourself.

| Type | When | Options |
|---|---|---|
| `yes_no` | "Should we…", "Is X worth…" | exactly `["Yes", "No"]` |
| `selection` | the question names the choices ("A or B", "which of A, B, C") | the named choices, spelled as the question spells them |
| `suggestion` | open: "who should we take at 24?", "what do we do at 11?" | none yet — members propose in the opening round |

Read `council/taken.txt` if it exists: players already off the board, one
per line. Include it in every member prompt. If the user names picks that
have happened, append them to that file first.

Read `council/roster.csv`: our current roster (player, team, pos, slot,
how and when acquired). Include it in the researcher's prompt and every
member prompt. If the user reports a move that is not in the file yet,
update the file first (see "During the season" in `council/PROTOCOL.md`).

Create `council/sessions/<YYYYMMDD-HHMMSS>-<slug>.json`:

```json
{ "question": "...", "type": "selection", "options": ["A", "B"],
  "asked_at": "<ISO time>", "taken": [], "research": null, "rounds": [] }
```

## 2. Research briefing — the researcher goes first, alone

Every meeting starts with fresh web research. Spawn **one** subagent with
`subagent_type: "council-researcher"`. If that type is not available in
this session, use `general-purpose` and start the prompt with: *"Read
`.claude/agents/council-researcher.md` and act as that agent for the rest
of this task."*

Its prompt contains: the question, every player and team the question or
its options name (for a suggestion, the likely candidates: our roster's
weak spots and the top names `council/lookup.py` returns for the slot),
the taken list, and today's date. Wait for it to finish — the members
need its file.

Check the file it names exists under `docs/research/` and follows the
format (findings with source URLs, "Conflicts with the repo", "Could not
confirm"). Do not edit its findings. Record the path in the session JSON
as `"research": "docs/research/<file>.md"`.

If the web is unreachable or the researcher fails, write no briefing, set
`"research": null`, carry on, and say in the report that the council
decided without fresh news.

## 3. Opening round — all nine members, in parallel

Spawn one subagent per member in `council/members.json`, **all in a single
message** so they run concurrently. Use `subagent_type: "council-<id>"`. If
that type is not available in this session, use `general-purpose` and start
the prompt with: *"Read `.claude/agents/council-<id>.md` and act as that
member for the rest of this task."*

Each prompt contains: the question, the type, the exact options (or, for a
suggestion, "propose one answer"), the taken list, **the research briefing
path** with the instruction to read it first, and the instruction to
research `docs/` and `data/` and end with the JSON ballot. Keep each agent's
id or name so you can message it again in a runoff.

Collect the nine JSON ballots into `rounds[0]`:

```json
{ "name": "opening", "options": [...], "ballots": [ { "member": "coach", "vote": "...", ... } ] }
```

## 4. Suggestion questions — pool the proposals

For `suggestion` only: merge the opening proposals into distinct options.
Proposals that name the same player or the same plan are one option; keep
the clearest wording. Do not drop a proposal because you dislike it. Then
run a **vote round**: send every member (SendMessage to the same agent if
you can, so it keeps its research; otherwise a fresh subagent with all
opening ballots attached) the pooled options and every member's opening
rationale, and ask for a new ballot choosing one option exactly. Store it
as `rounds[1]` with `"name": "vote"` and the pooled `options`.

For `yes_no` and `selection`, the opening round is the vote round.

## 5. Count

```bash
python council/tally.py council/sessions/<file>.json
```

If it prints `NO MAJORITY -> runoff`, run one **runoff** round: send every
member the two runoff options and all ballots from the previous round, ask
for a final ballot between those two, append it as a round with
`"name": "runoff"` and `"options": [the two]`, and run `tally.py` again.
The runoff result is final — the highest-weighted option wins, ties break
as the script says.

## 6. Inform the user

Lead with the verdict in one line, then:

- **Verdict:** the winning answer, its share of the vote weight, majority
  or plurality, and the round it was settled in.
- **Tally:** each option with its weight and who voted for it.
- **Why:** the two or three strongest pieces of evidence behind the
  winner, with file and number, drawn from the winning ballots.
- **Dissent:** the strongest case on the losing side, in one or two lines.
- **Flags:** anything a member called unresolved (§7), thin sample, or
  injury-dependent — the user must verify those in the draft room.
- **News:** the one or two briefing findings that moved the vote, with
  their source, and anything in "Could not confirm" that matters.

Keep it short enough to read inside a 90-second pick clock. Then tell the
user the session file path and the briefing path. Do not overrule the vote with your own opinion.
