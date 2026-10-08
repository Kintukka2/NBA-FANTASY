#!/usr/bin/env python3
"""Recompute league-scored fantasy points from raw box-score columns.

Reads   data/raw/master.csv          (verbatim transcription of the workbook)
Writes  data/processed/players_scored.csv
        data/processed/verification.csv

Deterministic: same input always produces byte-identical output. Floats
are rounded to 4 decimal places, row order is a stable sort, line
endings are LF. Regenerate and `git diff` to audit the committed copy.

The point of this script is that nobody has to trust the FPTS columns
ESPN hands over. Every one of them is rebuilt here from PTS/FGM/FGA/...
using scripts/league_scoring.py, then compared against ESPN's own
figure. The comparison is written to verification.csv.

Computed columns are deliberately mechanical. Nothing here ranks,
tiers, weights or projects -- that is the council's job. Where the
source data has a structural hole (ESPN does not project OREB, DREB,
PF, DD or TD, so P_FPTS_AVG understates rebounding bigs) this script
measures the size of the hole from the player's own observed actuals
and reports it as a column, rather than patching the projection.

Usage:  python scripts/recompute.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from league_scoring import per_game, season_total  # noqa: E402

RAW = os.path.join(ROOT, "data", "raw", "master.csv")
OUT_DIR = os.path.join(ROOT, "data", "processed")
OUT = os.path.join(OUT_DIR, "players_scored.csv")
VERIFY = os.path.join(OUT_DIR, "verification.csv")

ROUND = 4
THIN_SAMPLE_GP = 20   # documented threshold for the SAMPLE_FLAG column
# Tolerance for the ESPN cross-check, in points per game.
#
# The source workbook stores per-game averages rounded to 2 decimal
# places, so every one of the ~12 stat inputs carries up to +/-0.005 of
# rounding error. Weighted by the scoring values those errors sum to a
# worst case of about 0.105 pts/game:
#   (1+2+1+1+1+1+1+1+2+4+4+2) * 0.005 = 0.105
# Anything inside 0.15 is therefore arithmetic noise from the source
# precision, not a formula disagreement. Observed max is 0.0645.
TOLERANCE = 0.15

COMPUTED = [
    "FP_ACT_PG_CORE", "FP_ACT_BONUS_PG",
    "FP_ACT_PG", "FP_ACT_PG_ESPN", "FP_ACT_PG_DELTA",
    "FP_ACT_TOT", "FP_ACT_PER36",
    "FP_PROJ_PG_CORE", "FP_PROJ_PG_ESPN", "FP_PROJ_PG_DELTA",
    "FP_PROJ_TOT_CORE", "FP_PROJ_PER36",
    "OREB_SHARE_ACT", "DD_PER_GP_ACT", "TD_PER_GP_ACT",
    "PROJ_BLIND_SPOT_PG", "SAMPLE_FLAG",
]


def num(v):
    """Blank, None and unparseable all mean 'no data' -> 0.0."""
    if v is None or v == "":
        return 0.0
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def r(v):
    if v is None:
        return ""
    v = round(float(v), ROUND)
    # Normalise -0.0 so it never shows up in a diff.
    return 0.0 if v == 0 else v


def main():
    if not os.path.exists(RAW):
        sys.exit("missing %s -- run scripts/export_raw.py first" % RAW)
    os.makedirs(OUT_DIR, exist_ok=True)

    with open(RAW, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh))
    header, body = rows[0], rows[1:]
    ix = {name: i for i, name in enumerate(header)}

    required = ["Player", "A_GP", "A_PTS", "A_FGM", "A_FGA", "P_GP", "P_PTS"]
    for col in required:
        if col not in ix:
            sys.exit("raw master.csv is missing expected column %r" % col)

    def g(row, col):
        return num(row[ix[col]]) if col in ix else 0.0

    out_rows, verify_rows = [], []

    for row in body:
        if not row or not row[ix["Player"]]:
            continue

        # ---- actuals: full formula, OREB double-counted, bonuses in the total
        a_gp = g(row, "A_GP")
        a_min = g(row, "A_MIN")
        a_oreb = g(row, "A_OREB")
        a_dd, a_td = g(row, "A_DD"), g(row, "A_TD")
        act_pg = per_game(
            g(row, "A_PTS"), g(row, "A_FGM"), g(row, "A_FGA"),
            g(row, "A_FTM"), g(row, "A_FTA"), g(row, "A_3PM"),
            g(row, "A_REB"), a_oreb, g(row, "A_AST"),
            g(row, "A_STL"), g(row, "A_BLK"), g(row, "A_TO"),
        )
        # ESPN's A_FPTS_AVG is A_FPTS / A_GP, and A_FPTS includes the
        # double/triple-double bonuses. So the bonuses are amortised into
        # the per-game average rather than sitting only in the season
        # total. Confirmed exactly: Jokic 55 DD + 34 TD over 65 GP gives
        # (3*55 + 6*34)/65 = 5.6769, which is precisely the gap between
        # the bare per-game formula and ESPN's 74.94.
        act_bonus_pg = (3 * a_dd + 6 * a_td) / a_gp if a_gp else 0.0
        act_pg_full = act_pg + act_bonus_pg
        act_tot = season_total(act_pg, a_gp, a_dd, a_td)
        act_espn = g(row, "A_FPTS_AVG")

        # ---- projections: ESPN publishes no OREB/DREB/PF/DD/TD, so the
        # OREB term is 0 and there are no bonuses. Hence _CORE.
        p_gp = g(row, "P_GP")
        p_min = g(row, "P_MIN")
        proj_pg = per_game(
            g(row, "P_PTS"), g(row, "P_FGM"), g(row, "P_FGA"),
            g(row, "P_FTM"), g(row, "P_FTA"), g(row, "P_3PM"),
            g(row, "P_REB"), 0.0, g(row, "P_AST"),
            g(row, "P_STL"), g(row, "P_BLK"), g(row, "P_TO"),
        )
        proj_tot = season_total(proj_pg, p_gp)
        proj_espn = g(row, "P_FPTS_AVG")

        # ---- how much the projection structurally cannot see, measured
        # from this player's own 2026 line. Arithmetic on observed data,
        # not a forecast.
        blind = a_oreb + act_bonus_pg

        a_reb = g(row, "A_REB")
        flag = "NO_SAMPLE" if a_gp == 0 else ("THIN" if a_gp <= THIN_SAMPLE_GP else "")

        out_rows.append(row + [
            r(act_pg), r(act_bonus_pg),
            r(act_pg_full), r(act_espn), r(act_pg_full - act_espn),
            r(act_tot), r(act_pg_full / a_min * 36) if a_min else "",
            r(proj_pg), r(proj_espn), r(proj_pg - proj_espn),
            r(proj_tot), r(proj_pg / p_min * 36) if p_min else "",
            r(a_oreb / a_reb) if a_reb else "",
            r(a_dd / a_gp) if a_gp else "",
            r(a_td / a_gp) if a_gp else "",
            r(blind), flag,
        ])

        if a_gp > 0:
            d = act_pg_full - act_espn
            verify_rows.append([
                row[ix["Player"]], a_gp, r(act_pg_full), r(act_espn), r(d),
                "OUTLIER" if abs(d) > TOLERANCE else "ok",
            ])

    # Stable sort: actual FP/g descending, then name. Ties resolve the
    # same way on every machine.
    pg_at = len(header) + COMPUTED.index("FP_ACT_PG")
    name_at = ix["Player"]
    out_rows.sort(key=lambda x: (-float(x[pg_at] or 0), str(x[name_at])))
    verify_rows.sort(key=lambda x: (-abs(float(x[4] or 0)), str(x[0])))

    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh, lineterminator="\n")
        wr.writerow(header + COMPUTED)
        wr.writerows(out_rows)

    with open(VERIFY, "w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh, lineterminator="\n")
        wr.writerow(["Player", "A_GP", "recomputed_pg", "espn_pg", "delta", "status"])
        wr.writerows(verify_rows)

    deltas = [float(v[4]) for v in verify_rows]
    outliers = [v for v in verify_rows if v[5] == "OUTLIER"]
    print("players written        : %d" % len(out_rows))
    print("players with a sample  : %d" % len(verify_rows))
    if deltas:
        print("mean delta vs ESPN     : %+.4f pts/game" % (sum(deltas) / len(deltas)))
        print("max |delta|            : %.4f pts/game" % max(abs(d) for d in deltas))
    print("outliers (>%.2f pts/g) : %d" % (TOLERANCE, len(outliers)))
    for o in outliers[:10]:
        print("   %-28s GP=%-3s recomputed=%-8s espn=%-8s delta=%s" % tuple(o[:5]))
    if outliers:
        sys.exit("verification failed: scoring formula does not reproduce ESPN's figures")
    print("\nverification passed - formula reproduces ESPN's league scoring")


if __name__ == "__main__":
    main()
