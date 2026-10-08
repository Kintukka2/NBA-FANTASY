#!/usr/bin/env python3
"""Export every tab of the source workbook to CSV, verbatim.

No cleaning, no computation, no reordering. Cell values are written
exactly as openpyxl reads them so that data/raw/ stays a faithful
transcription of the workbook.

Provenance: the workbook itself was built from ESPN's private league
endpoint (kona_player_info, splits 002026 and 102027) which requires
authenticated browser cookies. That JSON is NOT recoverable from a
shell, so the workbook is the upstream-most artifact available here and
is committed alongside the CSVs. Refresh recipe: docs/data-dictionary.md.

Usage:  python scripts/export_raw.py
"""
import csv
import os
import sys

import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WORKBOOK = os.path.join(ROOT, "data", "raw", "ESPN_Fantasy_Player_Database_2026-27.xlsx")
RAW_DIR = os.path.join(ROOT, "data", "raw")

# Worksheet title -> output filename. Explicit so a renamed tab fails
# loudly instead of silently writing to a new path.
TABS = {
    "MASTER": "master.csv",
    "2026 Actual": "actuals_2026.csv",
    "2027 Projections": "projections_2027.csv",
    "League Settings": "league_settings.csv",
}


def main():
    if not os.path.exists(WORKBOOK):
        sys.exit("missing workbook: %s" % WORKBOOK)
    wb = openpyxl.load_workbook(WORKBOOK, read_only=True, data_only=True)
    found = {ws.title for ws in wb.worksheets}
    missing = set(TABS) - found
    if missing:
        sys.exit("workbook tabs missing: %s (found %s)" % (sorted(missing), sorted(found)))

    for title, fname in TABS.items():
        ws = wb[title]
        out = os.path.join(RAW_DIR, fname)
        n = 0
        with open(out, "w", newline="", encoding="utf-8") as fh:
            wr = csv.writer(fh, lineterminator="\n")
            for row in ws.iter_rows(values_only=True):
                # Trailing all-empty rows are an artefact of the xlsx
                # bounding box, not data.
                if all(c is None for c in row):
                    continue
                wr.writerow(["" if c is None else c for c in row])
                n += 1
        print("%-24s -> %-24s %5d rows" % (title, fname, n))
    wb.close()


if __name__ == "__main__":
    main()
