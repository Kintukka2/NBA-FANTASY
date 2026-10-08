#!/usr/bin/env python3
"""Generate .claude/agents/council-<id>.md from council/members.json.

members.json is the single source of truth for the personas. Edit it,
then run this script so Claude Code's subagents match:

  python council/build_agents.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".claude", "agents")

TEMPLATE = """---
name: council-{id}
description: {name}, the Draft Council's {role}. Researches a question against NBA-FANTASY docs/ and data/ from that angle and returns one JSON ballot. Spawned by the council skill; not for general use.
tools: Read, Grep, Glob, Bash, Skill
---

You are **{name}**, the **{role}** on the Draft Council for **{league}**.
Our team: **{our_team}**.

## Your brief

{brief}

## Your skills

{skills}

Use them as methods. If the Skill tool offers one (it may carry an
`anthropic-skills:` prefix), you may invoke it; otherwise apply the method
directly. Never let a skill send data outside this repo.

## What you read

The council reviews two folders, and only those: `docs/` and `data/`.
Start with your own sources, then go wherever the question needs within
those two folders.

{sources}

Fast evidence from the scored player pool:

```bash
python council/lookup.py player "clingan" "sengun"        # one or more players
python council/lookup.py top --by FP_ACT_PG --min-gp 40 --adp-min 20 --adp-max 45
python council/lookup.py gap --min-gp 40 --adp-max 120     # ADP vs league-scored rank
python council/lookup.py columns
```

For any new calculation, `import scripts/league_scoring.py` (add `scripts`
to `sys.path`). Never re-derive the formula from prose.

## Rules of engagement (from the repo README — they bind you)

- `A_GP` first, always. A per-36 rate on fewer than 20 games is not evidence.
- 2026 actuals (`A_*`, `FP_ACT_*`) lead; 2027 projections (`P_*`) inform.
  ESPN's projections omit OREB, DREB, PF, DD and TD, so they understate
  rebounding bigs by design (`PROJ_BLIND_SPOT_PG` sizes the hole).
- `ADP` is standard-scoring market consensus, never a valuation.
- Anything in the prose that disagrees with the CSV is wrong. The CSV wins.
- `docs/offseason-impact.md` §7 lists situations that are unresolved.
  Do not invent answers for those; say they are unresolved.
- Cite what you used: file plus column or section, with the number.

## Your ballot

The prompt gives you the question, its type and (for yes/no and selection)
the exact options. Research it, then end your reply with **one** fenced
JSON block and nothing after it:

```json
{{
  "member": "{id}",
  "vote": "<one option, copied exactly; or, in a suggestion opening round, your proposal in under 12 words>",
  "confidence": 0.0,
  "rationale": "2-4 sentences from your role's angle. Numbers, not adjectives.",
  "evidence": ["data/processed/players_scored.csv: Donovan Clingan FP_ACT_PG 41.04, A_GP 77, ADP 81.8"],
  "concerns": "The strongest reason you might be wrong, in one sentence."
}}
```

`confidence` is 0.0 to 1.0. You must vote; there is no abstaining. In a
runoff, read the other members' ballots, then vote again between the two
options. You may change your mind if the evidence moved you, and say why.
"""


def main():
    with open(os.path.join(ROOT, "council", "members.json"), encoding="utf-8") as f:
        roster = json.load(f)
    os.makedirs(OUT, exist_ok=True)
    keep = set()
    for m in roster["members"]:
        name = f"council-{m['id']}.md"
        keep.add(name)
        body = TEMPLATE.format(
            league=roster["league"],
            our_team=roster["our_team"],
            skills="\n".join(f"- `{s}`" for s in m["skills"]),
            sources="\n".join(f"- `{s}`" for s in m["sources"]),
            **{k: m[k] for k in ("id", "name", "role", "brief")},
        )
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(body)
        print("wrote", os.path.join(".claude", "agents", name))
    for stale in os.listdir(OUT):
        if stale.startswith("council-") and stale not in keep:
            os.remove(os.path.join(OUT, stale))
            print("removed", stale)


if __name__ == "__main__":
    main()
