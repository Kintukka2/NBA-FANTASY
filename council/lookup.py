#!/usr/bin/env python3
"""Quick queries over data/processed/players_scored.csv for council members.

Stdlib only. Read-only. Nothing here ranks or values players -- it only
filters and sorts the committed columns so a member can find evidence
fast. The judgement stays with the member.

Usage:
  python council/lookup.py player "clingan" ["jokic" ...]
  python council/lookup.py top --by FP_ACT_PG [--min-gp 40] [--adp-min 30]
                               [--adp-max 60] [--pos C] [--team SA]
                               [--injury ACTIVE] [--limit 20] [--asc]
                               [--cols Player,ADP,FP_ACT_PG]
  python council/lookup.py gap [--min-gp 40] [--adp-max 120] [--limit 25]
      ADP rank vs FP_ACT_PG rank among players with a sample: who the
      market (standard-scoring ADP) is mispricing in this league.
  python council/lookup.py columns
"""
import argparse
import csv
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data", "processed", "players_scored.csv")

DEFAULT_COLS = [
    "Player", "Team", "Pos", "Injury", "ADP", "A_GP", "A_MIN",
    "FP_ACT_PG", "FP_ACT_TOT", "FP_PROJ_PG_CORE", "PROJ_BLIND_SPOT_PG",
    "P_GP", "A_STL", "A_BLK", "A_OREB", "SAMPLE_FLAG",
]


def load():
    with open(DATA, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(v, default=None):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def norm(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def show(rows, cols):
    widths = {c: max(len(c), *(len(str(r.get(c, ""))) for r in rows)) if rows else len(c) for c in cols}
    print("  ".join(c.ljust(widths[c]) for c in cols))
    for r in rows:
        print("  ".join(str(r.get(c, "")).ljust(widths[c]) for c in cols))
    print(f"({len(rows)} rows)")


def filtered(rows, a):
    out = []
    for r in rows:
        gp = num(r.get("A_GP"), 0) or 0
        adp = num(r.get("ADP"))
        if a.min_gp is not None and gp < a.min_gp:
            continue
        if a.adp_min is not None and (adp is None or adp < a.adp_min):
            continue
        if a.adp_max is not None and (adp is None or adp > a.adp_max):
            continue
        if a.pos and a.pos.upper() not in r.get("Pos", "").upper().split("/"):
            continue
        if a.team and r.get("Team", "").upper() != a.team.upper():
            continue
        if a.injury and r.get("Injury", "").upper() != a.injury.upper():
            continue
        out.append(r)
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("player")
    sp.add_argument("names", nargs="+")
    sp.add_argument("--all", action="store_true", help="print every column")

    for name in ("top", "gap"):
        t = sub.add_parser(name)
        t.add_argument("--by", default="FP_ACT_PG")
        t.add_argument("--min-gp", type=float)
        t.add_argument("--adp-min", type=float)
        t.add_argument("--adp-max", type=float)
        t.add_argument("--pos")
        t.add_argument("--team")
        t.add_argument("--injury")
        t.add_argument("--limit", type=int, default=20)
        t.add_argument("--asc", action="store_true")
        t.add_argument("--cols")

    sub.add_parser("columns")
    a = p.parse_args()
    rows = load()

    if a.cmd == "columns":
        print("\n".join(rows[0].keys()))
        return

    if a.cmd == "player":
        hits = [r for r in rows if any(norm(n) in norm(r["Player"]) for n in a.names)]
        if not hits:
            sys.exit("no match")
        if a.all:
            for r in hits:
                print("\n".join(f"{k}: {v}" for k, v in r.items()))
                print("-" * 40)
        else:
            show(hits, DEFAULT_COLS)
        return

    cols = a.cols.split(",") if a.cols else DEFAULT_COLS

    if a.cmd == "top":
        pool = [r for r in filtered(rows, a) if num(r.get(a.by)) is not None]
        pool.sort(key=lambda r: num(r[a.by]), reverse=not a.asc)
        if a.by not in cols:
            cols = cols + [a.by]
        show(pool[: a.limit], cols)
        return

    if a.cmd == "gap":
        if a.min_gp is None:
            a.min_gp = 20
        pool = [r for r in filtered(rows, a) if num(r.get("ADP")) is not None and num(r.get("FP_ACT_PG")) is not None]
        by_adp = sorted(pool, key=lambda r: num(r["ADP"]))
        by_fp = sorted(pool, key=lambda r: -num(r["FP_ACT_PG"]))
        fp_rank = {r["PlayerID"]: i + 1 for i, r in enumerate(by_fp)}
        for i, r in enumerate(by_adp):
            r["ADP_RANK"] = i + 1
            r["FP_RANK"] = fp_rank[r["PlayerID"]]
            r["RANK_GAP"] = r["ADP_RANK"] - r["FP_RANK"]
        pool.sort(key=lambda r: r["RANK_GAP"], reverse=not a.asc)
        gcols = ["Player", "Team", "Pos", "Injury", "ADP", "ADP_RANK", "FP_ACT_PG", "FP_RANK", "RANK_GAP", "A_GP", "SAMPLE_FLAG"]
        print("RANK_GAP > 0: scores better here than the market drafts him. < 0: the market overpays (use --asc).")
        show(pool[: a.limit], gcols)


if __name__ == "__main__":
    main()
