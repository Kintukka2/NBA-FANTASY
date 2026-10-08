# Draft Council — protocol

Nine persona agents review `docs/` and `data/`, vote, and agree on the
highest-voted answer. Ask from Claude Code in this repo:

```
/council Should we take Jokic if he falls to 8?          # yes / no
/council Clingan or Sengun with pick 24?                 # selection
/council Who should we pair at 40 and 41?                # suggestion
```

## The members

| Member | Role | Weight | Starts from |
|---|---|---:|---|
| Coach | Draft strategist (chair) | 3 | `docs/league-rules.md`, `docs/scoring.md` |
| Archivist | Data steward | 1 | `docs/data-dictionary.md`, `docs/methodology.md`, `data/raw/`, `verification.csv` |
| Cipher | Projections | 3 | `players_scored.csv`, `actuals_2026.csv`, `projections_2027.csv`, `scripts/league_scoring.py` |
| Ledger | Value & ADP | 2 | `players_scored.csv`, `docs/offseason-impact.md` §4 + App. A |
| Medic | Availability | 2 | `docs/offseason-impact.md` §1, `Injury` / `A_GP` / `P_GP` |
| Scout | Role & opportunity | 2 | `docs/offseason-impact.md` §2-§7 |
| Tempo | Roster & schedule | 1 | `docs/league-rules.md` §3-§5, `Pos` |
| Vex | Sceptic | 2 | every doc's traps, §7, Appendix A |
| Quill | Scribe | 1 | `council/sessions/`, all of `docs/` |

17 weight in total. Every member may read anything in `docs/` and `data/`;
the sources are where each one starts. Personas, skills, sources and
weights live in `members.json` — edit there, then run
`python council/build_agents.py` to regenerate `.claude/agents/council-*.md`.

## How a question is decided

1. **Frame.** The question is typed `yes_no` (options Yes/No),
   `selection` (the choices it names) or `suggestion` (open).
2. **Opening round.** All nine research in parallel and each returns a
   JSON ballot: `vote`, `confidence`, `rationale`, `evidence`, `concerns`.
3. **Pool** (suggestions only). Proposals are merged into distinct
   options, and every member votes again among them, seeing everyone's
   opening rationale.
4. **Count.** `council/tally.py` weights each ballot. More than half the
   weight is a majority.
5. **Runoff.** Three or more options and no majority: the top two go to
   one runoff round, with every ballot on the table. Its result is final.
6. **Ties** break on weight × confidence, then the chair's vote.
7. **Verdict.** The highest-voted option, its share, the tally, the
   strongest evidence and the strongest dissent.

Every session is saved to `council/sessions/` as JSON — the record Quill
reads, and the file the Draft Council UI replays on its ring.

## During the draft

List players as they go in `council/taken.txt`, one per line (or just tell
Claude "X and Y are gone" and it appends them). Every member excludes them.
