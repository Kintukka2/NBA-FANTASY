# Skill runs

One HTML page per skill run, built by `council/run_report.py`, and an archive
of every run.

**Open the archive:** https://claude.ai/artifact/16YVNRxMxfCZhhf91E45Uq

It is a private page that only the owner, and anyone the owner shares it with,
can open. It lists every run, newest first. Each run page opens in place, with
links to the run before and after it.

## What a run page holds

1. **The scoreboard:** the score, the projected final with no more moves, the
   adds left, and the next suggested move as two steps:
   - drop the player after his last game ends, naming the opponent and the tip-off;
   - add the new player before his game, with the tip-off in Melbourne time.

   Every move in the move lists uses the same wording.
2. **What changed since the previous run:**
   - our roster;
   - the matchup (score, projection, adds);
   - the suggested pickups;
   - the news overrides;
   - news flags, slump flags, the injury shortlist and trades.
3. **Moves:** the moves suggested now, beside those of the run before.
   - A **new** tag marks each player who was not suggested before.
4. **The matchup plan** and the news watch's *What changed for us*.
5. **Every report of the run, in full.** Each one expands from the list, and
   the matchup report starts open.
6. **Our roster** at that run.

## Files

| File | What it is |
|---|---|
| `<YYYYMMDD-HHMM>.html` | A run page. The key is the UTC time of the run's latest report. |
| `<YYYYMMDD-HHMM>.json` | That run's snapshot: parsed figures, the roster and the overrides. The next run compares against it. |
| `index.html` | The archive, newest first. |
| `viewer.html` | The archive as one page for the Artifact tool. It loads `runs/<key>.html` on demand. |

GitHub shows these files as source code. To read them, use the archive link
above, or open the HTML files in a browser.

## Building and publishing

```bash
python council/run_report.py                  # today's run (UTC date)
python council/run_report.py --date 20261116  # rebuild one past date
python council/run_report.py --backfill       # every date in docs/analysis
```

**Which files a run uses:**
- **Reports:** each date takes its latest report of each kind. The others are
  linked as "earlier today".
- **Roster and overrides, past dates:** read from git, as `council/roster.csv`
  and `council/news_overrides.csv` stood at the end of that day.
- **Roster and overrides, today:** the working copies.

**Earlier runs stay as built.** Only their previous and next links are updated.

**After building, republish the archive** with the Artifact tool:
- Pass `url` = the archive link above. From a new conversation, `read` it first.
- `file_path` = `docs/runs/viewer.html`.
- `files` = `{"runs/<key>.html": "docs/runs/<key>.html"}` for the new run, and
  for any run whose links changed (the one before it).
