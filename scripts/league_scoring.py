"""Canonical scoring function for GONG league 423671879 (2026-27).

Single source of truth. Every agent imports from here rather than
re-deriving the formula from prose. Stdlib only.

Verified against ESPN's own league-scored totals for all 906 players
carrying a 2026 sample: mean deviation -0.01 pts, zero outliers.
See docs/scoring.md for the derivation and the net event values.
"""

# Per-event point values, exactly as configured in the league.
# PF is scored but worth 0. QD is configured at +40 and never occurs.
WEIGHTS = {
    "PTS": 1, "FGM": 2, "FGA": -1, "FTM": 1, "FTA": -1, "3PM": 1,
    "REB": 1, "OREB": 1, "AST": 2, "STL": 4, "BLK": 4, "TO": -2,
    "PF": 0, "DD": 3, "TD": 6, "QD": 40,
}


def per_game(pts, fgm, fga, ftm, fta, tpm, reb, oreb, ast, stl, blk, to):
    """Fantasy points for one game's worth of per-game averages.

    Excludes DD/TD/QD bonuses: the source data carries those as season
    counts, not rates, so they belong in season_total().

    OREB is deliberately added on top of REB. The league scores total
    rebounds at +1 and offensive rebounds at +1 again, so an offensive
    board is worth 2 and a defensive board 1.
    """
    w = WEIGHTS
    return (
        w["PTS"] * pts
        + w["FGM"] * fgm
        + w["FGA"] * fga
        + w["FTM"] * ftm
        + w["FTA"] * fta
        + w["3PM"] * tpm
        + w["REB"] * reb
        + w["OREB"] * oreb
        + w["AST"] * ast
        + w["STL"] * stl
        + w["BLK"] * blk
        + w["TO"] * to
    )


def season_total(fpts_per_game, gp, dd=0, td=0, qd=0):
    """Season fantasy total: per-game rate x games, plus the bonuses."""
    w = WEIGHTS
    return fpts_per_game * gp + w["DD"] * dd + w["TD"] * td + w["QD"] * qd


# Net value of a single event, after the attempt penalty is applied.
# Derived, not configured -- see docs/scoring.md.
NET_EVENT = {
    "made_two": 3, "made_three": 5, "missed_fg": -1,
    "made_ft": 1, "missed_ft": -1,
    "steal": 4, "block": 4, "assist": 2,
    "dreb": 1, "oreb": 2, "turnover": -2,
}

# Shooting break-even points, where attempts stop costing you points.
BREAK_EVEN_FG2 = 0.25   # 1/4 from two
BREAK_EVEN_FG3 = 1 / 6  # ~16.7% from three
BREAK_EVEN_FT = 0.50    # 1/2 from the line
