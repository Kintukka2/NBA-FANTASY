"""Run report: one HTML page per skill run, what changed since the last run, and an archive.

    python council/run_report.py                 # the run for today's reports (UTC date)
    python council/run_report.py --date 20261116 # rebuild one past date
    python council/run_report.py --backfill      # every date in docs/analysis, oldest first

Each run page holds:
- the scoreboard: score, projected final, adds left and the next suggested move;
- what changed since the previous run: our roster, the news overrides, the
  suggested moves, the score and projection, news flags, slump flags, the
  injury shortlist and trades;
- the suggested moves now beside the previous run's;
- the matchup plan and the news watch's "What changed for us";
- every report of the run, in full, as an expandable section.

Writes, under docs/runs/:
- <key>.html and <key>.json: the run page and its snapshot (key = YYYYMMDD-HHMM UTC
  of the run's latest report);
- index.html: every run, newest first;
- viewer.html: the same archive as one page for the Artifact tool, loading
  runs/<key>.html on demand.

The figures come from the reports and from council/roster.csv and
council/news_overrides.csv as they stood at the run (git history for past
dates). Nothing is recomputed here.
"""
import argparse
import csv
import datetime as dt
import html
import io
import json
import os
import posixpath
import re
import subprocess
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYSIS = os.path.join(ROOT, "docs", "analysis")
RUNS = os.path.join(ROOT, "docs", "runs")
REPO_BLOB = "https://github.com/Kintukka2/NBA-FANTASY/blob/main/"
MEL = ZoneInfo("Australia/Melbourne")
UTC = dt.timezone.utc

KINDS = [  # (base kind, label)
    ("matchup", "Matchup"),
    ("news-watch", "News watch"),
    ("injury-watch", "Injury watch"),
    ("slump-watch", "Slump watch"),
    ("trade-watch", "Trade watch"),
    ("rookies", "Rookies"),
]
LABEL = dict(KINDS)
FNAME = re.compile(r"^(\d{8})([a-z]?)-(.+)\.md$")
GENERATED = re.compile(r"Generated (\d{4}-\d{2}-\d{2}) (\d{2}):(\d{2}) UTC")


# ---------------------------------------------------------------- reports

def base_kind(kind):
    return "matchup" if kind.startswith("matchup") else kind


def generated_at(md):
    m = GENERATED.search(md)
    if not m:
        return None
    return dt.datetime.strptime(f"{m.group(1)} {m.group(2)}:{m.group(3)}", "%Y-%m-%d %H:%M").replace(tzinfo=UTC)


def report_files(date):
    """{base kind: [report dicts, latest first]} for one UTC date."""
    out = {}
    for f in sorted(os.listdir(ANALYSIS)):
        m = FNAME.match(f)
        if not m or m.group(1) != date:
            continue
        path = os.path.join(ANALYSIS, f)
        md = open(path, encoding="utf-8").read()
        title = re.search(r"^# (.+)$", md, re.M)
        out.setdefault(base_kind(m.group(3)), []).append({
            "file": f, "kind": m.group(3), "suffix": m.group(2), "md": md,
            "title": title.group(1).strip() if title else f,
            "generated": generated_at(md),
        })
    for k, v in out.items():
        v.sort(key=lambda r: (r["generated"] or dt.datetime.min.replace(tzinfo=UTC), r["suffix"]), reverse=True)
    return out


def all_dates():
    return sorted({m.group(1) for f in os.listdir(ANALYSIS) if (m := FNAME.match(f))})


def sections(md, level=2):
    """[(title, body)] for headings of exactly this level."""
    mark = "#" * level + " "
    out, title, buf = [], None, []
    for line in md.split("\n"):
        if line.startswith(mark) and not line.startswith(mark + "#"):
            if title is not None:
                out.append((title, "\n".join(buf)))
            title, buf = line[len(mark):].strip(), []
        elif title is not None:
            if re.match(r"^#{1,%d} " % (level - 1), line):
                out.append((title, "\n".join(buf)))
                title, buf = None, []
            else:
                buf.append(line)
    if title is not None:
        out.append((title, "\n".join(buf)))
    return out


def table_rows(body):
    """Data rows of the first markdown table in body, as lists of cell text."""
    rows, started = [], False
    for line in body.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                started = True
                continue
            if started:
                rows.append(cells)
        elif started:
            break
    return rows


def plain(s):
    return re.sub(r"\*\*|\*|`", "", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)).strip()


def num(s):
    return int(s.replace(",", ""))


def parse_matchup(md):
    d = {"title": None, "score": None, "adds": None, "projection": None, "moves": [],
         "best": None, "holding": None, "plan_title": None, "plan_md": None}
    m = re.search(r"^# (Matchup \d+: .+)$", md, re.M)
    d["title"] = m.group(1).strip() if m else None
    m = re.search(r"\*\*Score:\*\* ([\d,]+) to ([\d,]+)", md)
    if m:
        d["score"] = [num(m.group(1)), num(m.group(2))]
    m = re.search(r"\*\*Adds:\*\* (\d+) used this matchup of (\d+), so \*\*(\d+) left", md)
    if m:
        d["adds"] = {"used": int(m.group(1)), "limit": int(m.group(2)), "left": int(m.group(3))}
    m = re.search(r"for a final of \*\*([\d,]+) to ([\d,]+)\*\*", md)
    if m:
        d["projection"] = [num(m.group(1)), num(m.group(2))]
    m = re.search(r"^### Best plan: (\d+) adds?, ([+\-−][\d.]+)", md, re.M)
    if m:
        d["best"] = {"adds": int(m.group(1)), "gain": m.group(2).replace("−", "-")}
    i = md.find("Moves, each made before")
    if i >= 0:
        for line in md[i:].split("\n")[1:]:
            if not line.strip():
                if d["moves"]:
                    break
                continue
            mv = re.match(r"^\d+\. \*\*([^*]+?):\*\* drop (.+?), add \*\*([^*]+)\*\* \(([A-Z]+)", line)
            if not mv:
                break
            by = re.search(r"By ([^/]+?) / ([^.]+)\.", line)
            d["moves"].append({"day": mv.group(1).strip(), "drop": mv.group(2).strip(), "add": mv.group(3).strip(),
                               "team": mv.group(4), "by_et": by.group(1).strip() if by else "",
                               "by_mel": by.group(2).strip() if by else ""})
    m = re.search(r"^Left holding at the end of the week: (.+)$", md, re.M)
    d["holding"] = m.group(1).strip() if m else None
    plans = [(t, b) for t, b in sections(md) if re.match(r"(Plan|Update|Check-in)\b", t)]
    if plans:
        d["plan_title"], d["plan_md"] = plans[-1]
    return d


def parse_news(md):
    flags, changed = [], None
    for t, b in sections(md):
        if t == "Summary":
            for r in table_rows(b):
                if len(r) >= 7:
                    flags.append({"player": plain(r[0]), "team": r[1], "league": r[2], "flags": r[3],
                                  "rate": plain(r[4]), "status": plain(r[6])})
        elif t.startswith("What changed for us"):
            changed = b
    return {"flags": flags, "changed_md": changed}


def parse_slump(md):
    flagged = []
    for t, b in sections(md):
        if t != "By team":
            continue
        for team, tb in sections(b, 3):
            m = re.match(r"(.+): (\d+)$", team)
            if not m or m.group(2) == "0":
                continue
            for r in table_rows(tb):
                gap = next((plain(c) for c in r if re.fullmatch(r"\*\*[−-][\d.]+\*\*", c)), "")
                flagged.append({"player": plain(r[0]), "fantasy": m.group(1), "gap": gap.replace("−", "-")})
    m = re.search(r"\*\*(\d+) rostered players? (?:is|are) 10\+", md)
    return {"flagged": flagged, "headline": m.group(0).replace("**", "") if m else None}


def parse_injury(md):
    names = []
    for t, b in sections(md):
        if t == "Shortlist":
            for line in b.split("\n"):
                m = re.match(r"^\s*(?:- |\| )\*\*([^*]+)\*\*", line)
                if m and m.group(1).strip() not in names:
                    names.append(m.group(1).strip())
    m = re.search(r"\*\*Injuries:\*\* (\d+) players", md)
    return {"shortlist": names, "injuries": int(m.group(1)) if m else None}


def parse_trade(md):
    trades = []
    for t, b in sections(md):
        if t == "Summary":
            for r in table_rows(b):
                if len(r) >= 3:
                    trades.append({"date": r[0], "player": plain(r[1]), "move": plain(r[2])})
    return {"trades": trades}


PARSERS = {"matchup": parse_matchup, "news-watch": parse_news, "slump-watch": parse_slump,
           "injury-watch": parse_injury, "trade-watch": parse_trade}


# ------------------------------------------------------------- csv state

def git_rev_at(date):
    """Last commit on or before the end of a UTC date."""
    iso = f"{date[:4]}-{date[4:6]}-{date[6:]}T23:59:59Z"
    r = subprocess.run(["git", "-C", ROOT, "rev-list", "-1", f"--before={iso}", "HEAD"],
                       capture_output=True, text=True)
    return r.stdout.strip() or None


def read_csv_at(rel, rev):
    if rev is None:
        path = os.path.join(ROOT, rel)
        text = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    else:
        r = subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{rel}"], capture_output=True, text=True)
        text = r.stdout if r.returncode == 0 else ""
    return list(csv.DictReader(io.StringIO(text))) if text.strip() else []


# ---------------------------------------------------------------- snapshot

def build_snapshot(date, use_git):
    reps = report_files(date)
    if not reps:
        return None, None
    chosen = {k: v[0] for k, v in reps.items()}
    times = [r["generated"] for r in chosen.values() if r["generated"]]
    when = max(times) if times else dt.datetime.strptime(date + "2359", "%Y%m%d%H%M").replace(tzinfo=UTC)
    key = when.strftime("%Y%m%d-%H%M")
    rev = git_rev_at(date) if use_git else None
    roster = [{"player": r["player"], "team": r.get("team", ""), "slot": r.get("slot", "")}
              for r in read_csv_at("council/roster.csv", rev)]
    overrides = [{k: r.get(k, "") for k in ("player", "kind", "value", "until", "source", "note")}
                 for r in read_csv_at("council/news_overrides.csv", rev)]
    snap = {"key": key, "date": date, "when_utc": when.isoformat(), "roster": roster, "overrides": overrides,
            "reports": [{"kind": k, "file": r["file"], "title": r["title"],
                         "generated": r["generated"].isoformat() if r["generated"] else None,
                         "versions": [x["file"] for x in reps[k][1:]]}
                        for k, r in sorted(chosen.items(), key=lambda kv: kind_rank(kv[0]))]}
    for k, fn in PARSERS.items():
        if k in chosen:
            snap[k] = fn(chosen[k]["md"])
    return snap, chosen


def kind_rank(k):
    order = [x for x, _ in KINDS]
    return (order.index(k) if k in order else len(order), k)


# -------------------------------------------------------------------- diff

def diff(prev, cur):
    """[(group, [(change, text)])] — change is added / removed / changed."""
    out = []
    if prev is None:
        return out

    def by(rows, key):
        return {key(r): r for r in rows}

    g = []
    pr, cr = by(prev.get("roster", []), lambda r: r["player"]), by(cur.get("roster", []), lambda r: r["player"])
    for p in cr:
        if p not in pr:
            g.append(("added", f"{p} ({cr[p]['team']})"))
    for p in pr:
        if p not in cr:
            g.append(("removed", f"{p} ({pr[p]['team']})"))
    for p in cr:
        if p in pr and cr[p]["slot"] != pr[p]["slot"]:
            g.append(("changed", f"{p}: {pr[p]['slot']} → {cr[p]['slot']}"))
    out.append(("Our roster", g))

    g = []
    pm, cm = prev.get("matchup") or {}, cur.get("matchup") or {}
    if cm.get("title") and cm.get("title") != pm.get("title"):
        g.append(("changed", f"New matchup: {cm['title']}"))
    if cm.get("score") and pm.get("score") and cm.get("title") == pm.get("title") and cm["score"] != pm["score"]:
        g.append(("changed", f"Score {fmt_pair(pm['score'])} → {fmt_pair(cm['score'])}"))
    if cm.get("projection") and pm.get("projection") and cm.get("title") == pm.get("title"):
        a, b = margin(pm["projection"]), margin(cm["projection"])
        if cm["projection"] != pm["projection"]:
            g.append(("changed", f"Projected final {fmt_pair(pm['projection'])} → {fmt_pair(cm['projection'])} "
                                 f"(margin {a:+,} → {b:+,})"))
    if cm.get("adds") and pm.get("adds") and cm.get("title") == pm.get("title") and cm["adds"]["left"] != pm["adds"]["left"]:
        g.append(("changed", f"Adds left {pm['adds']['left']} → {cm['adds']['left']}"))
    out.append(("Matchup", g))

    g = []
    pa = {m["add"] for m in pm.get("moves", [])}
    ca = {m["add"] for m in cm.get("moves", [])}
    for n in sorted(ca - pa):
        g.append(("added", f"Now suggested: {n}"))
    for n in sorted(pa - ca):
        if n in cr and n not in pr:
            g.append(("changed", f"Picked up: {n}"))
        else:
            g.append(("removed", f"No longer suggested: {n}"))
    out.append(("Suggested pickups", g))

    g = []
    po = by(prev.get("overrides", []), lambda r: (r["player"], r["kind"]))
    co = by(cur.get("overrides", []), lambda r: (r["player"], r["kind"]))
    for k, r in co.items():
        if k not in po:
            g.append(("added", f"{r['player']}: {r['kind']} {r['value']}" + (f" until {r['until']}" if r["until"] else "")))
        elif (r["value"], r["until"]) != (po[k]["value"], po[k]["until"]):
            g.append(("changed", f"{r['player']}: {r['kind']} {po[k]['value']} → {r['value']}"))
    for k, r in po.items():
        if k not in co:
            g.append(("removed", f"{r['player']}: {r['kind']} {r['value']}"))
    out.append(("News overrides", g))

    g = []
    if "news-watch" in cur and "news-watch" in prev:
        pf = by(prev["news-watch"]["flags"], lambda r: r["player"])
        cf = by(cur["news-watch"]["flags"], lambda r: r["player"])
        rank = lambda r: 0 if r["league"] == "us" else 2 if r["league"] in ("free agent", "waivers") else 1
        rows = []
        for p, r in cf.items():
            if p not in pf:
                rows.append((rank(r), "added", f"{p} ({r['team']}, {r['league']}): {r['flags']}"))
            elif r["status"] != pf[p]["status"]:
                rows.append((rank(r), "changed", f"{p}: {pf[p]['status']} → {r['status']}"))
        for p, r in pf.items():
            if p not in cf:
                rows.append((rank(r) + 3, "removed", f"{p} ({r['team']}): no longer flagged"))
        g = [(c, t) for _, c, t in sorted(rows, key=lambda x: x[0])]
    out.append(("News flags", g))

    g = []
    if "slump-watch" in cur and "slump-watch" in prev:
        ps = {r["player"] for r in prev["slump-watch"]["flagged"]}
        for r in cur["slump-watch"]["flagged"]:
            if r["player"] not in ps:
                g.append(("added", f"{r['player']} ({r['fantasy']}) {r['gap']}"))
        cs = {r["player"] for r in cur["slump-watch"]["flagged"]}
        for r in prev["slump-watch"]["flagged"]:
            if r["player"] not in cs:
                g.append(("removed", f"{r['player']} ({r['fantasy']}) is back within 10"))
    out.append(("Slump flags", g))

    g = []
    if "injury-watch" in cur and "injury-watch" in prev:
        ps, cs = prev["injury-watch"]["shortlist"], cur["injury-watch"]["shortlist"]
        g += [("added", n) for n in cs if n not in ps] + [("removed", n) for n in ps if n not in cs]
    out.append(("Injury shortlist", g))

    g = []
    if "trade-watch" in cur:
        pt = {t["player"] for t in (prev.get("trade-watch") or {}).get("trades", [])}
        g += [("added", f"{t['player']}: {t['move']} ({t['date']})") for t in cur["trade-watch"]["trades"]
              if t["player"] not in pt]
    out.append(("Trades", g))
    return out


def margin(pair):
    return pair[0] - pair[1]


def fmt_pair(pair):
    return f"{pair[0]:,} to {pair[1]:,}"


# ---------------------------------------------------------------- markdown

def safe_href(url):
    if url.startswith(("http://", "https://")):
        return url
    path = url.split("#")[0]
    if path.endswith(".md"):
        return REPO_BLOB + posixpath.normpath(posixpath.join("docs/analysis", path))
    return None


def emph(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?![\s*])(.+?)(?<![\s*])\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w])_(?![\s_])(.+?)(?<![\s_])_(?![\w])", r"<em>\1</em>", t)
    return t


def inline(text):
    keep = []

    def hold(s):
        keep.append(s)
        return f"\x00{len(keep) - 1}\x00"

    t = html.escape(text, quote=False)
    t = re.sub(r"`([^`]+)`", lambda m: hold(f"<code>{m.group(1)}</code>"), t)

    def link(m):
        href = safe_href(html.unescape(m.group(2)))
        label = emph(m.group(1))
        if not href:
            return hold(label)
        return hold(f'<a href="{html.escape(href, quote=True)}" target="_blank" rel="noopener noreferrer">{label}</a>')

    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    t = emph(t)
    while "\x00" in t:
        t = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], t)
    return t


LIST_ITEM = re.compile(r"^(\s*)([-*+]|\d+\.)\s+(.*)$")


def md_to_html(md, shift=1, skip_h1=True):
    lines = md.split("\n")
    out, i, n, para = [], 0, len(lines), []

    def flush():
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para.clear()

    while i < n:
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            flush()
            j, buf = i + 1, []
            while j < n and not lines[j].strip().startswith("```"):
                buf.append(lines[j])
                j += 1
            out.append(f'<div class="scroll"><pre><code>{html.escape(chr(10).join(buf))}</code></pre></div>')
            i = j + 1
            continue
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            flush()
            lvl = len(h.group(1))
            if not (skip_h1 and lvl == 1):
                tag = f"h{min(6, lvl + shift)}"
                out.append(f"<{tag}>{inline(h.group(2).strip())}</{tag}>")
            i += 1
            continue
        if re.fullmatch(r"(-{3,}|\*{3,})", s):
            flush()
            out.append("<hr>")
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            flush()
            head = [c.strip() for c in s.strip("|").split("|")]
            seps = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
            align = ["num" if c.endswith(":") and not c.startswith(":") else "" for c in seps]
            rows, j = [], i + 2
            while j < n and lines[j].strip().startswith("|"):
                rows.append([c.strip() for c in lines[j].strip().strip("|").split("|")])
                j += 1

            def cell(tag, c, k):
                cls = f' class="{align[k]}"' if k < len(align) and align[k] else ""
                return f"<{tag}{cls}>{inline(c)}</{tag}>"

            th = "".join(cell("th", c, k) for k, c in enumerate(head))
            tb = "".join("<tr>" + "".join(cell("td", c, k) for k, c in enumerate(r)) + "</tr>" for r in rows)
            out.append(f'<div class="scroll"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>')
            i = j
            continue
        if LIST_ITEM.match(line):
            flush()
            items, j = [], i
            while j < n:
                m = LIST_ITEM.match(lines[j])
                if m:
                    items.append([len(m.group(1).expandtabs(4)), m.group(2)[0].isdigit(), m.group(3),
                                  m.group(2)[:-1] if m.group(2)[0].isdigit() else None])
                    j += 1
                elif lines[j].strip() and lines[j].startswith((" ", "\t")) and items:
                    items[-1][2] += " " + lines[j].strip()
                    j += 1
                elif not lines[j].strip() and j + 1 < n and (LIST_ITEM.match(lines[j + 1]) or
                                                             lines[j + 1].startswith(("  ", "\t"))):
                    j += 1
                else:
                    break
            out.append(build_list(items))
            i = j
            continue
        if s.startswith(">"):
            flush()
            buf, j = [], i
            while j < n and lines[j].strip().startswith(">"):
                buf.append(lines[j].strip()[1:].strip())
                j += 1
            out.append(f"<blockquote>{md_to_html(chr(10).join(buf), shift, skip_h1)}</blockquote>")
            i = j
            continue
        if not s:
            flush()
        else:
            para.append(s)
        i += 1
    flush()
    return "\n".join(out)


def build_list(items):
    html_out, idx = [], 0
    while idx < len(items):
        part, idx = _list(items, idx, items[idx][0])
        html_out.append(part)
    return "".join(html_out)


def _list(items, idx, indent):
    ordered, start = items[idx][1], items[idx][3]
    tag = "ol" if ordered else "ul"
    attr = f' start="{start}"' if ordered and start and start != "1" else ""
    parts = [f"<{tag}{attr}>"]
    while idx < len(items) and items[idx][0] == indent:
        text = inline(items[idx][2])
        idx += 1
        child = ""
        while idx < len(items) and items[idx][0] > indent:
            sub, idx = _list(items, idx, items[idx][0])
            child += sub
        parts.append(f"<li>{text}{child}</li>")
    parts.append(f"</{tag}>")
    return "".join(parts), idx


# ------------------------------------------------------------------- html

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700'
         '&family=Fira+Code:wght@500&family=Fira+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">')

CSS = """
/* Layout: a sticky run bar, a scoreboard strip, the change ledger and moves, then each report as an expandable panel. */
:root {
  --bg: #F4F6F8; --surface: #FFFFFF; --sunken: #ECEFF3; --ink: #16202A; --muted: #556170; --line: #D8DDE4;
  --accent: #B04E19; --accent-ink: #FFFFFF; --accent-soft: #FAEADF;
  --good: #1C6E46; --good-soft: #E2F2E9; --bad: #AD2A20; --bad-soft: #FAE6E3; --info: #24539F; --info-soft: #E5EDF9;
  --font-display: "Barlow Condensed", "Arial Narrow", "Roboto Condensed", system-ui, sans-serif;
  --font-body: "Fira Sans", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono: "Fira Code", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #0E1318; --surface: #151C23; --sunken: #1B232C; --ink: #E4E9EF; --muted: #9BA7B3; --line: #2A3440;
  --accent: #F08A4C; --accent-ink: #1B0F07; --accent-soft: #3A2416;
  --good: #5CC995; --good-soft: #13301F; --bad: #F2867B; --bad-soft: #3B1A17; --info: #8EB2F2; --info-soft: #18263D;
  color-scheme: dark; } }
:root[data-theme="dark"] {
  --bg: #0E1318; --surface: #151C23; --sunken: #1B232C; --ink: #E4E9EF; --muted: #9BA7B3; --line: #2A3440;
  --accent: #F08A4C; --accent-ink: #1B0F07; --accent-soft: #3A2416;
  --good: #5CC995; --good-soft: #13301F; --bad: #F2867B; --bad-soft: #3B1A17; --info: #8EB2F2; --info-soft: #18263D;
  color-scheme: dark; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font: 400 15px/1.55 var(--font-body); }
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10; background: var(--surface); }
a { color: var(--info); text-underline-offset: 2px; }
a:hover { color: var(--accent); }
a:focus-visible, summary:focus-visible, button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 3px; }
.wrap { max-width: 1180px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.runbar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--surface); border-bottom: 1px solid var(--line); }
.runbar .wrap { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px; padding-block: 10px; }
.brand { font: 700 18px/1 var(--font-display); letter-spacing: .04em; text-transform: uppercase; color: var(--accent); }
.runbar .when { color: var(--muted); font-size: 13px; }
.runbar nav { margin-left: auto; display: flex; flex-wrap: wrap; gap: 6px; }
.btn { display: inline-flex; align-items: center; min-height: 36px; padding: 0 12px; border: 1px solid var(--line); border-radius: 18px; color: var(--ink); text-decoration: none; font-size: 13px; font-weight: 500; background: var(--surface); transition: border-color .15s, color .15s; }
.btn:hover { border-color: var(--accent); color: var(--accent); }
.btn[aria-disabled="true"] { color: var(--muted); opacity: .55; pointer-events: none; }
main { padding-block: 20px 56px; display: grid; gap: 28px; }
main > * { min-width: 0; }
h1, h2 { font-family: var(--font-display); font-weight: 700; letter-spacing: .01em; text-wrap: balance; margin: 0; }
h1 { font-size: clamp(28px, 4.4vw, 40px); line-height: 1.05; }
h2 { font-size: 24px; line-height: 1.15; }
.eyebrow { font: 500 11px/1.3 var(--font-mono); letter-spacing: .1em; text-transform: uppercase; color: var(--muted); margin: 0 0 6px; }
.sub { color: var(--muted); margin: 6px 0 0; }
.board { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
.tile { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 14px 16px; display: grid; gap: 4px; align-content: start; min-width: 0; }
.tile .label { font: 500 11px/1.2 var(--font-mono); letter-spacing: .09em; text-transform: uppercase; color: var(--muted); }
.tile .value { font: 700 36px/1 var(--font-display); font-variant-numeric: tabular-nums; }
.tile .value small { font-size: 18px; color: var(--muted); font-weight: 600; }
.tile .note { font-size: 13px; color: var(--muted); }
.tile.next .value { font-size: 22px; line-height: 1.15; }
.lead-up { color: var(--good); } .lead-down { color: var(--bad); }
.pips { display: flex; gap: 5px; margin-top: 4px; }
.pip { width: 14px; height: 14px; border-radius: 50%; border: 2px solid var(--accent); }
.pip.on { background: var(--accent); }
.panel { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 18px 20px; min-width: 0; }
.panel > h2 { margin-bottom: 12px; }
.ledger { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px 24px; }
.ledger h3 { font: 600 13px/1.3 var(--font-body); margin: 0 0 6px; color: var(--muted); text-transform: uppercase; letter-spacing: .06em; }
.ledger ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 6px; }
.ledger li { display: flex; gap: 8px; align-items: baseline; }
.ledger details.more { margin-top: 8px; }
.ledger details.more > summary { cursor: pointer; color: var(--info); font-size: 13px; font-weight: 500; min-height: 32px; display: flex; align-items: center; }
.ledger details.more ul { margin-top: 6px; }
.chip { flex: none; font: 500 10.5px/1 var(--font-mono); letter-spacing: .06em; text-transform: uppercase; padding: 4px 7px; border-radius: 4px; }
.chip.added { background: var(--good-soft); color: var(--good); }
.chip.removed { background: var(--bad-soft); color: var(--bad); }
.chip.changed { background: var(--info-soft); color: var(--info); }
.chip.new { background: var(--accent-soft); color: var(--accent); }
.quiet { color: var(--muted); font-size: 14px; margin: 0; }
.compare { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }
.compare h3 { font: 600 15px/1.3 var(--font-body); margin: 0 0 8px; }
.compare ol { margin: 0; padding-left: 22px; display: grid; gap: 8px; }
.compare .when2 { color: var(--muted); font-size: 13px; }
.move b { font-weight: 600; }
.move .by { display: block; color: var(--muted); font-size: 13px; }
.toc { display: flex; flex-wrap: wrap; gap: 6px; }
details.report { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; min-width: 0; }
details.report + details.report { margin-top: 10px; }
details.report > summary { list-style: none; cursor: pointer; padding: 14px 18px; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 12px; }
details.report > summary::-webkit-details-marker { display: none; }
details.report > summary::before { content: "+"; font: 700 18px/1 var(--font-mono); color: var(--accent); width: 14px; }
details.report[open] > summary::before { content: "\\2212"; }
details.report > summary .t { font: 700 20px/1.15 var(--font-display); }
details.report > summary .d { color: var(--muted); font-size: 13px; }
.md { padding: 0 20px 20px; border-top: 1px solid var(--line); min-width: 0; }
.md h2, .md h3 { font-family: var(--font-display); font-weight: 700; font-size: 20px; margin: 22px 0 8px; }
.md h4 { font-size: 16px; margin: 18px 0 6px; }
.md h5, .md h6 { font-size: 14px; margin: 14px 0 4px; }
.md p, .md li { max-width: 78ch; }
.md ul, .md ol { padding-left: 22px; }
.md li + li { margin-top: 3px; }
.md code { font: 500 12.5px/1.4 var(--font-mono); background: var(--sunken); padding: 1px 5px; border-radius: 4px; }
.md pre { margin: 0; padding: 12px; background: var(--sunken); border-radius: 8px; }
.md pre code { background: none; padding: 0; }
.md blockquote { margin: 10px 0; padding: 4px 14px; border-left: 3px solid var(--line); color: var(--muted); }
.md hr { border: 0; border-top: 1px solid var(--line); margin: 18px 0; }
.scroll { overflow-x: auto; margin: 10px 0; max-width: 100%; }
table { border-collapse: collapse; font-size: 13px; font-variant-numeric: tabular-nums; min-width: 100%; }
th, td { text-align: left; vertical-align: top; padding: 6px 10px; border-bottom: 1px solid var(--line); }
th { font-weight: 600; color: var(--muted); background: var(--sunken); white-space: nowrap; }
td.num, th.num { text-align: right; }
tbody tr:hover td { background: var(--sunken); }
.call .md { border-top: 0; padding: 0; }
.runs { list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }
.run { display: grid; grid-template-columns: minmax(150px, 1.1fr) minmax(170px, 1.6fr) minmax(120px, 1fr) minmax(130px, 1fr); gap: 6px 16px; align-items: center; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 12px 16px; text-decoration: none; color: var(--ink); transition: border-color .15s; }
.run:hover { border-color: var(--accent); color: var(--ink); }
.run .d1 { font: 700 18px/1.1 var(--font-display); }
.run .d2, .run .meta { color: var(--muted); font-size: 13px; }
.run .mt { font-weight: 500; }
.run .nums { font-variant-numeric: tabular-nums; font-size: 14px; }
.bar { position: relative; height: 10px; background: var(--sunken); border-radius: 5px; margin-top: 6px; }
.bar::after { content: ""; position: absolute; left: 50%; top: -2px; bottom: -2px; width: 1px; background: var(--muted); }
.bar span { position: absolute; top: 0; bottom: 0; border-radius: 5px; }
.bar .pos { left: 50%; background: var(--good); }
.bar .neg { right: 50%; background: var(--bad); }
.latest { display: grid; gap: 4px; }
footer { color: var(--muted); font-size: 13px; padding-block: 0 40px; }
@media (max-width: 720px) {
  .run { grid-template-columns: 1fr 1fr; }
  .tile .value { font-size: 30px; }
  .md { padding: 0 14px 16px; }
  details.report > summary { padding: 12px 14px; }
  .panel { padding: 16px 14px; }
}
@media (prefers-reduced-motion: reduce) { * { transition: none !important; scroll-behavior: auto !important; } }
"""


def esc(s):
    return html.escape(str(s), quote=True)


def mel(when_iso):
    w = dt.datetime.fromisoformat(when_iso)
    return w.astimezone(MEL)


def run_label(snap):
    m = mel(snap["when_utc"])
    return f"{m:%a} {m.day} {m:%b %Y}, {m:%-I:%M %p} Melbourne"


def short_label(snap):
    m = mel(snap["when_utc"])
    return f"{m:%a} {m.day} {m:%b}"


def page(title, body, standalone=True):
    head = (f"<title>{esc(title)}</title>"
            '<meta name="claude:viewport-fit-sides" content="cover">'
            f"{FONTS}<style>{CSS}</style>")
    if not standalone:
        return head + body
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f"{head}</head><body>{body}</body></html>")


def tiles(snap):
    m = snap.get("matchup") or {}
    out = []
    if m.get("score"):
        us, them = m["score"]
        lead = us - them
        cls = "lead-up" if lead > 0 else "lead-down" if lead < 0 else ""
        word = "up" if lead > 0 else "down" if lead < 0 else "level"
        out.append(f'<div class="tile"><span class="label">Score</span><span class="value">{us:,}<small> to </small>{them:,}</span>'
                   f'<span class="note {cls}">{word} {abs(lead):,}</span></div>')
    if m.get("projection"):
        us, them = m["projection"]
        lead = us - them
        cls = "lead-up" if lead > 0 else "lead-down"
        best = m.get("best")
        out.append(f'<div class="tile"><span class="label">Projected final, no more moves</span><span class="value">{us:,}<small> to </small>{them:,}</span>'
                   f'<span class="note {cls}">margin {lead:+,}</span>'
                   + (f'<span class="note">best plan adds {best["gain"]} ({best["adds"]} adds)</span>' if best else "")
                   + "</div>")
    if m.get("adds"):
        a = m["adds"]
        pips = "".join(f'<span class="pip{" on" if k < a["left"] else ""}"></span>' for k in range(a["limit"]))
        out.append(f'<div class="tile"><span class="label">Adds left</span><span class="value">{a["left"]}<small> of {a["limit"]}</small></span>'
                   f'<span class="pips" role="img" aria-label="{a["left"]} of {a["limit"]} adds left">{pips}</span></div>')
    if m.get("moves"):
        mv = m["moves"][0]
        out.append(f'<div class="tile next"><span class="label">Next suggested move · {esc(mv["day"])}</span>'
                   f'<span class="value">{esc(mv["drop"])} → {esc(mv["add"])}</span>'
                   f'<span class="note">{esc(mv["add"])} ({esc(mv["team"])}) · before {esc(mv["by_mel"])} Melbourne</span></div>')
    return f'<section class="board" aria-label="Scoreboard">{"".join(out)}</section>' if out else ""


def ledger(changes, prev):
    if prev is None:
        return ('<section class="panel"><h2>What changed</h2><p class="quiet">This is the first run in the archive, '
                "so there is nothing to compare with.</p></section>")
    groups = []
    li = lambda c, t: f'<li><span class="chip {c}">{c}</span><span>{esc(t)}</span></li>'
    for name, items in changes:
        if items:
            shown, rest = items[:8], items[8:]
            more = (f'<details class="more"><summary>Show {len(rest)} more</summary><ul>{"".join(li(c, t) for c, t in rest)}</ul></details>'
                    if rest else "")
            groups.append(f"<div><h3>{esc(name)}</h3><ul>{''.join(li(c, t) for c, t in shown)}</ul>{more}</div>")
    body = "".join(groups) or '<p class="quiet">Nothing in the tracked lists changed.</p>'
    return (f'<section class="panel"><h2>What changed since {esc(short_label(prev))}</h2>'
            f'<p class="sub" style="margin:-6px 0 14px">Against the previous run, {esc(run_label(prev))}.</p>'
            f'<div class="ledger">{body}</div></section>')


def moves_list(moves, other_adds):
    if not moves:
        return '<p class="quiet">No move list in this run\'s matchup report.</p>'
    lis = []
    for mv in moves:
        new = (' <span class="chip new">new</span>' if other_adds is not None and mv["add"] not in other_adds else "")
        lis.append(f'<li class="move"><b>{esc(mv["day"])}:</b> drop {esc(mv["drop"])}, add <b>{esc(mv["add"])}</b> ({esc(mv["team"])}){new}'
                   f'<span class="by">before {esc(mv["by_mel"])} Melbourne ({esc(mv["by_et"])} ET)</span></li>')
    return f"<ol>{''.join(lis)}</ol>"


def compare(snap, prev):
    cm = snap.get("matchup") or {}
    pm = (prev or {}).get("matchup") or {}
    if not cm and not pm:
        return ""
    prev_adds = {m["add"] for m in pm.get("moves", [])} if prev else None
    left = (f'<div><h3>Suggested now</h3><p class="when2">{esc(cm.get("title") or "")}'
            + (f' · best plan {cm["best"]["gain"]} with {cm["best"]["adds"]} adds' if cm.get("best") else "")
            + f"</p>{moves_list(cm.get('moves'), prev_adds)}"
            + (f'<p class="when2">Left holding: {esc(cm["holding"])}</p>' if cm.get("holding") else "") + "</div>")
    if prev:
        right = (f'<div><h3>Suggested at the last run · {esc(short_label(prev))}</h3><p class="when2">{esc(pm.get("title") or "")}'
                 + (f' · best plan {pm["best"]["gain"]} with {pm["best"]["adds"]} adds' if pm.get("best") else "")
                 + f"</p>{moves_list(pm.get('moves'), None)}</div>")
    else:
        right = ""
    return f'<section class="panel"><h2>Moves: now and last run</h2><div class="compare">{left}{right}</div></section>'


def digest(kind, snap, rep):
    if kind == "matchup":
        m = snap.get("matchup") or {}
        bits = []
        if m.get("score"):
            bits.append(f"score {fmt_pair(m['score'])}")
        if m.get("projection"):
            bits.append(f"projected {fmt_pair(m['projection'])}")
        return " · ".join(bits)
    if kind == "news-watch":
        return f"{len(snap['news-watch']['flags'])} players flagged"
    if kind == "slump-watch":
        return snap["slump-watch"]["headline"] or f"{len(snap['slump-watch']['flagged'])} flagged"
    if kind == "injury-watch":
        i = snap["injury-watch"]
        return (f"{i['injuries']} injuries" if i["injuries"] else "") + (f" · shortlist {', '.join(i['shortlist'])}" if i["shortlist"] else "")
    if kind == "trade-watch":
        return f"{len(snap['trade-watch']['trades'])} traded players"
    m = re.search(r"lottery rookies are running at \*\*([\d.]+)×", rep["md"])
    return f"lottery rookies at {m.group(1)}× projection" if m else ""


def nav_html(prev, nxt):
    nav = (f'<a class="btn" href="{esc(prev["key"])}.html" data-run="{esc(prev["key"])}">← {esc(short_label(prev))}</a>' if prev
           else '<a class="btn" aria-disabled="true">← Older</a>')
    nav += '<a class="btn" href="index.html" data-run="">All runs</a>'
    nav += (f'<a class="btn" href="{esc(nxt["key"])}.html" data-run="{esc(nxt["key"])}">{esc(short_label(nxt))} →</a>' if nxt
            else '<a class="btn" aria-disabled="true">Newer →</a>')
    return f'<nav aria-label="Runs">{nav}</nav>'


def run_page(snap, chosen, prev, nxt, standalone=True):
    m = snap.get("matchup") or {}
    title = m.get("title") or "Skill run"
    bar = (f'<header class="runbar"><div class="wrap"><span class="brand">Draft Council</span>'
           f'<span class="when">Run of {esc(run_label(snap))}</span>{nav_html(prev, nxt)}</div></header>')
    head = (f'<div><p class="eyebrow">Skill run · {esc(snap["key"])} UTC</p><h1>{esc(title)}</h1>'
            f'<p class="sub">Run of {esc(run_label(snap))}. Reports: '
            + ", ".join(esc(LABEL.get(r["kind"], r["kind"])) for r in snap["reports"]) + ".</p></div>")
    call = ""
    if m.get("plan_md"):
        call += (f'<section class="panel call"><p class="eyebrow">Matchup plan</p><h2>{esc(plain(m["plan_title"]))}</h2>'
                 f'<div class="md">{md_to_html(m["plan_md"], shift=1)}</div></section>')
    news = snap.get("news-watch") or {}
    if news.get("changed_md"):
        call += (f'<section class="panel call"><p class="eyebrow">News watch</p><h2>What changed for us</h2>'
                 f'<div class="md">{md_to_html(news["changed_md"], shift=1)}</div></section>')
    toc = "".join(f'<a class="btn" href="#rep-{esc(r["kind"])}">{esc(LABEL.get(r["kind"], r["kind"]))}</a>' for r in snap["reports"])
    reps = []
    for r in snap["reports"]:
        rep = chosen[r["kind"]]
        gen = mel(r["generated"]).strftime("%-I:%M %p %a %-d %b") + " Melbourne" if r["generated"] else ""
        vers = ""
        if r["versions"]:
            vers = (" · earlier today: " + ", ".join(f'<a href="{esc(REPO_BLOB + "docs/analysis/" + v)}" target="_blank" rel="noopener noreferrer">{esc(v)}</a>'
                                                     for v in r["versions"]))
        src = f'<a href="{esc(REPO_BLOB + "docs/analysis/" + r["file"])}" target="_blank" rel="noopener noreferrer">{esc(r["file"])}</a>'
        reps.append(f'<details class="report" id="rep-{esc(r["kind"])}"{" open" if r["kind"] == "matchup" else ""}>'
                    f'<summary><span class="t">{esc(r["title"])}</span><span class="d">{esc(digest(r["kind"], snap, rep))}</span></summary>'
                    f'<div class="md"><p class="quiet">Generated {esc(gen)} · source {src}{vers}</p>{md_to_html(rep["md"])}</div></details>')
    roster = ", ".join(esc(f"{p['player']} ({p['team']}{', ' + p['slot'] if p['slot'] not in ('', 'roster') else ''})") for p in snap["roster"])
    body = (f'{bar}<main id="run" class="wrap">{head}{tiles(snap)}{ledger(diff(prev, snap), prev)}{compare(snap, prev)}{call}'
            f'<section><h2 style="margin-bottom:10px">Reports</h2><nav class="toc" aria-label="Reports">{toc}</nav>'
            f'<div style="margin-top:12px">{"".join(reps)}</div></section>'
            f'<section class="panel"><h2>Our roster at this run</h2><p style="margin:0">{roster or "Not recorded."}</p></section>'
            f'</main><footer class="wrap">Built by <code>council/run_report.py</code> from the run\'s reports, '
            f'<code>council/roster.csv</code> and <code>council/news_overrides.csv</code>. Figures are the scripts\'; nothing here is recomputed.</footer>')
    return page(f"Run {short_label(snap)}", body, standalone)


def index_body(snaps, link):
    """The archive list; link(key) gives each run's href."""
    rows = []
    margins = [abs(margin(s["matchup"]["projection"])) for s in snaps if (s.get("matchup") or {}).get("projection")]
    top = max(margins) if margins else 1
    for k, s in enumerate(snaps):
        m = s.get("matchup") or {}
        score = f"score {fmt_pair(m['score'])}" if m.get("score") else "no score yet"
        proj, bar = "", ""
        if m.get("projection"):
            mg = margin(m["projection"])
            proj = f"projected {fmt_pair(m['projection'])} ({mg:+,})"
            w = 50 * abs(mg) / top
            bar = f'<div class="bar" aria-hidden="true"><span class="{"pos" if mg >= 0 else "neg"}" style="width:{w:.1f}%"></span></div>'
        prev = snaps[k + 1] if k + 1 < len(snaps) else None
        n = sum(len(v) for _, v in diff(prev, s)) if prev else 0
        kinds = ", ".join(LABEL.get(r["kind"], r["kind"]) for r in s["reports"])
        rows.append(f'<li><a class="run" href="{esc(link(s["key"]))}" data-run="{esc(s["key"])}">'
                    f'<span><span class="d1">{esc(short_label(s))}</span><br><span class="d2">{esc(mel(s["when_utc"]).strftime("%-I:%M %p"))} Melbourne</span></span>'
                    f'<span><span class="mt">{esc(m.get("title") or "No matchup report")}</span><br><span class="meta">{esc(kinds)}</span></span>'
                    f'<span class="nums">{esc(score)}<br><span class="meta">{esc(proj)}</span>{bar}</span>'
                    f'<span class="meta">{n} change{"s" if n != 1 else ""} since the run before</span></a></li>')
    latest = snaps[0] if snaps else None
    hero = ""
    if latest:
        hero = (f'<div class="latest"><p class="eyebrow">Latest run</p><h1>{esc((latest.get("matchup") or {}).get("title") or "Skill runs")}</h1>'
                f'<p class="sub">{esc(run_label(latest))}. <a href="{esc(link(latest["key"]))}" data-run="{esc(latest["key"])}">Open the latest run</a>.</p></div>')
    return (f'<div id="indexview"><header class="runbar"><div class="wrap"><span class="brand">Draft Council</span>'
            f'<span class="when">{len(snaps)} runs, newest first</span></div></header>'
            f'<main class="wrap">{hero}{tiles(latest) if latest else ""}'
            f'<section><h2 style="margin-bottom:12px">Every run</h2><ul class="runs">{"".join(rows)}</ul></section></main>'
            f'<footer class="wrap">Each run page shows what changed since the run before it, the moves suggested then and now, '
            f'and every report in full. The bar is the projected final margin with no more moves, to one scale across runs.</footer></div>')


VIEWER_JS = """
<div id="reader" hidden></div>
<script>
(function () {
  var index = document.getElementById('indexview'), reader = document.getElementById('reader');
  function wire(root) {
    root.querySelectorAll('a[data-run]').forEach(function (a) {
      var k = a.getAttribute('data-run');
      a.setAttribute('href', k ? '#r-' + k : '#all');
      a.removeAttribute('target');
    });
  }
  function show(key) {
    if (!key) {
      reader.hidden = true; index.hidden = false;
      window.scrollTo(0, 0); return;
    }
    reader.innerHTML = '<main class="wrap"><p class="quiet">Loading the run…</p></main>';
    reader.hidden = false; index.hidden = true;
    fetch('runs/' + key + '.html').then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    }).then(function (t) {
      var doc = new DOMParser().parseFromString(t, 'text/html');
      var bar = doc.querySelector('.runbar'), main = doc.querySelector('main'), foot = doc.querySelector('footer');
      reader.innerHTML = (bar ? bar.outerHTML : '') + '<main class="wrap">' + (main ? main.innerHTML : '') + '</main>' +
        (foot ? foot.outerHTML : '');
      wire(reader);
      window.scrollTo(0, 0);
    }).catch(function () {
      reader.innerHTML = '<main class="wrap"><p>This run could not be loaded. <a href="#all">Go back to every run</a>.</p></main>';
    });
  }
  function route() {
    var h = location.hash.replace(/^#/, '');
    show(/^r-\\d{8}-\\d{4}$/.test(h) ? h.slice(2) : '');
  }
  reader.addEventListener('click', function (e) {
    var a = e.target.closest('a[href^="#rep-"]');
    if (!a) return;
    e.preventDefault();
    var el = document.getElementById(a.getAttribute('href').slice(1));
    if (el) { el.open = true; el.scrollIntoView({ block: 'start' }); }
  });
  wire(index);
  window.addEventListener('hashchange', route);
  route();
})();
</script>
"""


# -------------------------------------------------------------------- main

def load_snaps():
    snaps = []
    if os.path.isdir(RUNS):
        for f in sorted(os.listdir(RUNS)):
            if re.fullmatch(r"\d{8}-\d{4}\.json", f):
                snaps.append(json.load(open(os.path.join(RUNS, f), encoding="utf-8")))
    return sorted(snaps, key=lambda s: s["key"])


def build(dates, today):
    os.makedirs(RUNS, exist_ok=True)
    built = {}
    for date in dates:
        snap, chosen = build_snapshot(date, use_git=(date != today))
        if not snap:
            continue
        for f in os.listdir(RUNS):  # a same-day run whose reports moved on: keep only the latest key per date
            if f.startswith(date + "-") and f[:13] != snap["key"] and f.endswith(".json"):
                old = json.load(open(os.path.join(RUNS, f), encoding="utf-8"))
                if old.get("files") == [r["file"] for r in snap["reports"]]:
                    os.remove(os.path.join(RUNS, f))
                    if os.path.exists(os.path.join(RUNS, f[:-5] + ".html")):
                        os.remove(os.path.join(RUNS, f[:-5] + ".html"))
        snap["files"] = [r["file"] for r in snap["reports"]]
        json.dump(snap, open(os.path.join(RUNS, snap["key"] + ".json"), "w", encoding="utf-8"), indent=1)
        built[snap["key"]] = chosen
    snaps = load_snaps()
    keys = [s["key"] for s in snaps]
    for k, s in enumerate(snaps):
        prev = snaps[k - 1] if k > 0 else None
        nxt = snaps[k + 1] if k + 1 < len(snaps) else None
        path = os.path.join(RUNS, s["key"] + ".html")
        if s["key"] in built:
            open(path, "w", encoding="utf-8").write(run_page(s, built[s["key"]], prev, nxt))
        elif os.path.exists(path):  # an earlier run keeps its content; only its prev/next links move
            old = open(path, encoding="utf-8").read()
            new = re.sub(r'<nav aria-label="Runs">.*?</nav>', lambda _: nav_html(prev, nxt), old, count=1, flags=re.S)
            if new != old:
                open(path, "w", encoding="utf-8").write(new)
    newest = list(reversed(snaps))
    open(os.path.join(RUNS, "index.html"), "w", encoding="utf-8").write(
        page("Draft Council Runs", index_body(newest, lambda k: f"{k}.html")))
    open(os.path.join(RUNS, "viewer.html"), "w", encoding="utf-8").write(
        page("Draft Council Runs", index_body(newest, lambda k: f"#r-{k}") + VIEWER_JS, standalone=False))
    return keys, list(built)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--date", help="UTC date of the run, YYYYMMDD (default: today)")
    ap.add_argument("--backfill", action="store_true", help="rebuild every date in docs/analysis")
    a = ap.parse_args()
    today = dt.datetime.now(UTC).strftime("%Y%m%d")
    dates = all_dates() if a.backfill else [a.date or today]
    keys, built = build(dates, today)
    if not built:
        raise SystemExit(f"No reports in docs/analysis for {', '.join(dates)}.")
    for k in built:
        print(f"Wrote docs/runs/{k}.html")
    print(f"Wrote docs/runs/index.html and docs/runs/viewer.html: {len(keys)} runs.")


if __name__ == "__main__":
    main()
