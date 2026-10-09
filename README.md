# NBA-FANTASY — GONG league 423671879, 2026-27

Source material for the Draft Council. League: 8 teams, H2H points,
**custom scoring**, snake, 13 rounds, no keepers. Our team is
**Come-in Cider (`CCDR`)**, picking **6 of 8** (corrected 8 Oct 2026; earlier material said 8).

## Read in this order

1. **`docs/scoring.md`** — why this league does not play like a standard
   one. Steals and blocks at +4, offensive rebounds scored twice, every
   attempt −1. Read before forming any opinion about a player.
2. **`docs/data-dictionary.md`** — provenance, every column, and the
   known traps in the source data.
3. **`docs/offseason-impact.md`** — every roster change since 1 June
   2026 for all 30 teams, organised by whether last season's number
   still describes this season's situation. The draft-night injury
   board, 21 format-specific buys, and **24 situations left explicitly
   unresolved in §7 — do not invent answers for those.** Appendix A
   reconciles the whole document against the CSV.
4. **`data/processed/players_scored.csv`** — 1,095 players, 67 columns,
   league-scored. Start here for analysis.

## Layout

```
data/raw/     ESPN_...xlsx          the source workbook, committed
              master.csv            verbatim transcription, 1,095 rows
              actuals_2026.csv      558 rows
              projections_2027.csv  348 rows
              league_settings.csv   league config
data/processed/
              players_scored.csv    raw + 17 computed columns
              verification.csv      per-player cross-check vs ESPN
scripts/      league_scoring.py     canonical scoring function
              export_raw.py         xlsx -> data/raw/*.csv
              recompute.py          raw -> data/processed/*
docs/         scoring.md            the formula and what it implies
              data-dictionary.md    provenance, columns, traps
              offseason-impact.md   situational analysis, all 30 teams
              league-rules.md       full league configuration
              methodology.md        how the pool was extracted and verified
              research/             web briefings, one per council meeting
```

## Ask the council

```
/council Clingan or Sengun with pick 24?
```

First a non-voting researcher (Wire) searches the web for the latest news
on the players involved and writes a sourced briefing to `docs/research/`.
Then nine persona agents research `docs/` (briefing included) and `data/`,
vote (yes/no, a selection, or a suggestion), settle any split in a runoff,
and report the highest-voted answer. See `council/PROTOCOL.md`.

```
council/      members.json          personas, skills, sources, vote weights
              PROTOCOL.md           how a question is decided
              lookup.py             fast queries over players_scored.csv
              tally.py              weighted vote count, runoff, tiebreaks
              build_agents.py       members.json -> .claude/agents/council-*.md
                                    (nine members + council-researcher)
              taken.txt             players already drafted
              roster.csv            our live roster, updated after every move
              sessions/             every council session, as JSON
```

## Reproduce

```bash
pip install -r requirements.txt
python scripts/export_raw.py
python scripts/recompute.py
git diff --stat          # empty means the committed data matches
```

`recompute.py` exits non-zero if the formula stops reproducing ESPN's
own league-scored figures. Both scripts are deterministic, so a diff is
always signal.

Nothing is in Git LFS, deliberately — agents cannot read pointer files.

## Rules of engagement

- **Import `scripts/league_scoring.py`.** Do not re-derive the formula
  from prose, including from `docs/scoring.md`.
- **`A_GP` first, always.** Several apparent bargains rest on fewer than
  20 games.
- **2026 actuals lead; 2027 projections inform.** Standing instruction
  from the owner. ESPN's projections also omit `OREB`, `DREB`, `PF`,
  `DD` and `TD` entirely, so they understate rebounding bigs by design.
- **`ADP` is standard-scoring.** Treat it as market consensus, never as
  a valuation. The gap between ADP and league-scored production is the
  opportunity this whole repo exists to find.
- **Add columns rather than asking for them.** The pipeline is a script,
  not a fixed table. If the question needs a stat that is not there,
  compute it.
- **Nothing in this repo ranks players.** No tiers, no board, no
  valuation — on purpose. Those are the council's output, not its input.

## Known state of the prose

`docs/offseason-impact.md` has been reconciled against the CSV. Twelve
figures that the research pass got wrong were corrected in place rather
than footnoted, so there is no longer a body-versus-appendix split to
trip over. Appendix A lists every correction and what it changed, which
is worth reading on its own as a map of where the research was weakest.

Two of those corrections matter enough to restate here. **Jokić, not
Wembanyama, is the top asset** — 74.97 FP/g against 59.50. And **Clingan
was undersold by a third**: 41.0 FP/g over a full 77 games at ADP 81.8,
because the first pass counted only his rebounding and blocks.

Anything in the prose that disagrees with the CSV is wrong. The CSV is
regenerated and verified on every run of `recompute.py`; the prose is
not.
