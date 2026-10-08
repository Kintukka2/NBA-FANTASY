#!/usr/bin/env python3
"""Count a council round. Deterministic, stdlib only.

The model never adds up votes: this script does. It reads a session file
(see council/PROTOCOL.md), weights each ballot in the chosen round by the
member's vote weight from council/members.json, and writes the result back
into that round.

Rules
  - Weighted plurality. Each ballot counts its member's `weight`.
  - Majority means strictly more than half the weight cast.
  - With three or more options and no majority, the round reports
    `needs_runoff` and the top two options go to a runoff round.
  - Ties on weight break on sum(weight x confidence), then on the chair's
    vote, then on the option listed first.

Usage
  python council/tally.py council/sessions/<file>.json [--round N]
    N defaults to the last round. Prints a summary and updates the file.
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMBERS = os.path.join(ROOT, "council", "members.json")


def tally(session, round_index, roster):
    rnd = session["rounds"][round_index]
    weights = {m["id"]: m["weight"] for m in roster["members"]}
    chair = roster.get("chair")
    options = list(rnd.get("options") or session.get("options") or [])

    score, conf, voters = {}, {}, {}
    chair_vote = None
    for b in rnd["ballots"]:
        mid, vote = b["member"], b["vote"].strip()
        if mid not in weights:
            sys.exit(f"unknown member {mid!r}")
        if options and vote not in options:
            sys.exit(f"{mid} voted {vote!r}, which is not one of {options}")
        if vote not in options:
            options.append(vote)
        w = weights[mid]
        c = float(b.get("confidence", 0.5))
        score[vote] = score.get(vote, 0) + w
        conf[vote] = conf.get(vote, 0) + w * c
        voters.setdefault(vote, []).append(mid)
        if mid == chair:
            chair_vote = vote

    cast = sum(score.values())
    order = sorted(
        options,
        key=lambda o: (-score.get(o, 0), -conf.get(o, 0), 0 if o == chair_vote else 1, options.index(o)),
    )
    winner = order[0]
    tied = [o for o in order if score.get(o, 0) == score.get(winner, 0)]
    majority = score.get(winner, 0) * 2 > cast
    needs_runoff = (not majority) and len([o for o in options if score.get(o, 0) > 0]) >= 3

    if len(tied) > 1:
        if conf.get(tied[0], 0) != conf.get(tied[1], 0):
            tiebreak = "confidence"
        elif chair_vote in tied:
            tiebreak = "chair"
        else:
            tiebreak = "order"
    else:
        tiebreak = None

    result = {
        "winner": winner,
        "weight_cast": cast,
        "majority": majority,
        "share": round(score.get(winner, 0) / cast, 3) if cast else 0,
        "tiebreak": tiebreak,
        "needs_runoff": needs_runoff,
        "runoff_options": order[:2] if needs_runoff else None,
        "standings": [
            {
                "option": o,
                "weight": score.get(o, 0),
                "confidence_weight": round(conf.get(o, 0), 3),
                "voters": voters.get(o, []),
            }
            for o in order
        ],
    }
    rnd["result"] = result
    return result


def main():
    p = argparse.ArgumentParser()
    p.add_argument("session")
    p.add_argument("--round", type=int, default=-1)
    a = p.parse_args()

    with open(MEMBERS, encoding="utf-8") as f:
        roster = json.load(f)
    with open(a.session, encoding="utf-8") as f:
        session = json.load(f)

    r = tally(session, a.round, roster)
    rnd = session["rounds"][a.round]
    if not r["needs_runoff"]:
        session["verdict"] = {
            "answer": r["winner"],
            "round": rnd.get("name"),
            "share": r["share"],
            "majority": r["majority"],
            "tiebreak": r["tiebreak"],
        }

    with open(a.session, "w", encoding="utf-8") as f:
        json.dump(session, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"Round: {rnd.get('name', a.round)}  |  weight cast: {r['weight_cast']}")
    for s in r["standings"]:
        bar = "#" * int(s["weight"])
        print(f"  {s['weight']:>3}  {bar:<18} {s['option']}  ({', '.join(s['voters']) or '-'})")
    if r["needs_runoff"]:
        print(f"NO MAJORITY -> runoff between: {r['runoff_options'][0]!r} and {r['runoff_options'][1]!r}")
    else:
        how = "majority" if r["majority"] else "plurality"
        tb = f", tie broken on {r['tiebreak']}" if r["tiebreak"] else ""
        print(f"VERDICT: {r['winner']}  ({how}, {r['share']:.0%} of weight{tb})")


if __name__ == "__main__":
    main()
