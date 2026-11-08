#!/usr/bin/env python3
"""dash.py — the ONLY sanctioned way to touch the dashboard data.

The dashboard (docs/index.html) renders docs/data/runs.json +
docs/data/candidates.json. Hand-written appends drifted badly
(300+ standby rows, string "algos", missing titles -> "undefined"
cards and empty charts). This tool enforces the schema at write
time; `sanitize` repairs anything that predates it or slipped
through from an old checkout.

Usage (run from the visalgo-progress repo root, then git push):

  python3 tools/dash.py append \
      --title "campaign 2: NQ 2022 walk-forward" \
      --type experiment \
      --summary "..."            # or --summary-file runs/notes.md
      --file runs/2026-11-07T...-campaign2.md   # full log path in-repo
      --status ok|partial|blocked|failed \
      --algo "name=ema-cross-9/21" [--equity curve.csv] [--metrics m.json] [--params p.json]
      --tests "34 passed" --sierra dev

  python3 tools/dash.py sanitize [--apply]

Equity CSV: one column (cumulative P&L series) or "idx,cum".
metrics.json / params.json: flat JSON objects of scalars.

Constitution (AGENTS.md): the dashboard carries (a) experiments with
artifacts, (b) blocked <=5 lines, (c) corrections. Standby/idle wakes
log NOTHING here — decision_loop keeps the idle log in /runs only if
a human asks. wake/analysis types are rejected.
"""
import argparse, csv, json, os, re, sys, time

RUNS = "docs/data/runs.json"
ALLOWED_TYPES = {"experiment", "deploy", "correction", "manual", "maintenance",
                 "integrity-audit", "blocked"}
STANDBY_RE = re.compile(r"\b(standby|idle wake|idle log|check-in \(no|no-op wake)\b", re.I)
MAX_ROWS = 800


def load():
    try:
        with open(RUNS) as f:
            v = json.load(f)
        return v if isinstance(v, list) else []
    except Exception:
        return []


def save(rows):
    rows = rows[-MAX_ROWS:]
    tmp = RUNS + ".tmp"
    os.makedirs(os.path.dirname(RUNS), exist_ok=True)
    with open(tmp, "w") as f:
        json.dump(rows, f, separators=(",", ":"))
    os.replace(tmp, RUNS)


def clean_text(s, limit=None):
    if not isinstance(s, str):
        return ""
    s = re.sub(r"\s+", " ", s).strip()
    if limit and len(s) > limit:
        s = s[: limit - 1].rstrip() + "…"
    return s


def norm_equity(eq):
    """Accept [[i,v]...], [v,...], [{t/idx,x,v|y|cum}...] -> [[i,v],...] of finite floats."""
    out = []
    if not isinstance(eq, list):
        return out
    for i, p in enumerate(eq):
        try:
            if isinstance(p, (int, float)):
                out.append([i, float(p)])
            elif isinstance(p, list) and len(p) >= 2 and isinstance(p[1], (int, float)):
                out.append([float(p[0]), float(p[1])])
            elif isinstance(p, dict):
                v = p.get("cum", p.get("v", p.get("y", p.get("equity"))))
                k = p.get("i", p.get("idx", p.get("t", p.get("x", i))))
                if isinstance(v, (int, float)):
                    out.append([float(k), float(v)])
        except Exception:
            continue
    return out


def norm_algo(a):
    """-> dict {name, metrics{num}, params{scalar}, equity[[k,v]]} or None."""
    if isinstance(a, str):
        a = {"name": a}
    if not isinstance(a, dict):
        return None
    name = clean_text(a.get("name"), 80) or "algo"
    metrics = {clean_text(k, 40): v for k, v in (a.get("metrics") or {}).items()
               if isinstance(v, (int, float)) and not isinstance(v, bool)}
    params = {}
    for k, v in (a.get("params") or {}).items():
        if isinstance(v, (int, float, str, bool)):
            params[clean_text(k, 40)] = v
        elif isinstance(v, (list, dict)) and json.dumps(v, default=str).__len__() < 400:
            params[clean_text(k, 40)] = v
    eq = norm_equity(a.get("equity", a.get("equity_curve")))
    out = {"name": name}
    if metrics:
        out["metrics"] = metrics
    if params:
        out["params"] = params
    if len(eq) >= 2:
        out["equity"] = eq
    return out if (len(eq) >= 2 or metrics) else None


def norm_row(r, i=-1):
    if not isinstance(r, dict):
        return None
    t = (r.get("type") or "").lower()
    if t not in ALLOWED_TYPES:
        return None  # wake/analysis/anything invented: drop
    ts = r.get("ts") or ""
    if not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?(Z|[+-]\d{2}:\d{2})?$", ts):
        # never hand a renderer a free-text "timestamp" — Invalid
        # Date once did (2026-11-08).
        ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    summary = clean_text(r.get("summary"), 600)
    title = clean_text(r.get("title"), 120)
    if not title:  # never render "undefined": derive from summary
        title = (summary[:72] + "…") if summary else f"run {ts or i}"
    if STANDBY_RE.search(title) and not r.get("algos"):
        return None
    row = {"ts": ts, "type": t, "title": title}
    if summary:
        row["summary"] = summary
    for k in ("status", "tests", "sierra", "file", "id"):
        v = r.get(k)
        if isinstance(v, str) and v.strip():
            row[k] = clean_text(v, 200 if k == "file" else 60)
    algos = [n for n in (norm_algo(a) for a in (r.get("algos") or [])) if n]
    if algos:
        row["algos"] = algos
    return row


def sanitize(rows):
    out, seen = [], set()
    for i, r in enumerate(rows):
        n = norm_row(r, i)
        if not n:
            continue
        key = (n["ts"], n["title"])
        if key in seen:
            continue
        seen.add(key)
        out.append(n)
    return out


def read_equity(path):
    vals = []
    with open(path, newline="") as f:
        rd = csv.reader(f)
        rows = [r for r in rd if r and any(c.strip() for c in r)]
    if rows and not all(is_num(rows[0][-1]) for _ in [0]):
        pass
    start = 0
    if rows and not is_num(rows[0][-1]):
        start = 1  # header
    for k, r in enumerate(rows[start:]):
        try:
            if len(r) >= 2 and is_num(r[0]) and is_num(r[1]):
                vals.append([float(r[0]), float(r[1])])
            elif is_num(r[-1]):
                vals.append([float(k), float(r[-1])])
        except Exception:
            continue
    return vals


def is_num(s):
    try:
        float(s)
        return True
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("append")
    a.add_argument("--title", required=True)
    a.add_argument("--type", required=True)
    a.add_argument("--summary", default="")
    a.add_argument("--summary-file", default="")
    a.add_argument("--file", default="", help="in-repo full-log path shown as 'full log' link")
    a.add_argument("--status", default="", choices=["", "ok", "partial", "blocked", "failed"])
    a.add_argument("--tests", default="")
    a.add_argument("--sierra", default="")
    a.add_argument("--algo", action="append", default=[],
                   help='name=... or plain name; repeat. Attach --equity/--metrics/--params to the LAST --algo')
    a.add_argument("--equity", default="", help="CSV path (equity series for the last --algo)")
    a.add_argument("--metrics", default="", help="JSON path (metrics for the last --algo)")
    a.add_argument("--params", default="", help="JSON path (params for the last --algo)")

    s = sub.add_parser("sanitize")
    s.add_argument("--apply", action="store_true")
    ns = ap.parse_args()

    if ns.cmd == "append":
        t = ns.type.lower()
        if t not in ALLOWED_TYPES:
            print(f"REFUSED: type '{ns.type}' is not loggable. The dashboard carries experiments, "
                  f"deploys, corrections, manuals, maintenance, audits, blocked — standby/wake logs "
                  f"NOTHING. (provenance constitution)", file=sys.stderr)
            return 0
        summary = ns.summary or ""
        if ns.summary_file:
            with open(ns.summary_file) as f:
                summary = summary or f.read()
        algos = []
        for spec in ns.algo or []:
            name = spec.split("=", 1)[1] if spec.startswith("name=") else spec
            algos.append({"name": name, "equity": [], "metrics": {}, "params": {}})
        if algos:
            last = algos[-1]
            if ns.equity:
                last["equity"] = read_equity(ns.equity)
            if ns.metrics:
                with open(ns.metrics) as f:
                    last["metrics"] = json.load(f)
            if ns.params:
                with open(ns.params) as f:
                    last["params"] = json.load(f)
        row = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "type": t,
            "title": clean_text(ns.title, 120),
            "summary": clean_text(summary, 600),
            "algos": algos,
        }
        for k in ("status", "tests", "sierra", "file"):
            v = getattr(ns, k)
            if v:
                row[k] = v
        n = norm_row(row)
        if not n:
            print("REFUSED: row failed schema (title required, non-standby)", file=sys.stderr)
            return 1
        rows = sanitize(load() + [n])
        save(rows)
        print(f"appended: {n['title'][:70]}  (rows={len(rows)}); now: git add -A && git commit && git push")
        return 0

    if ns.cmd == "sanitize":
        rows = load()
        fixed = sanitize(rows)
        print(f"rows {len(rows)} -> {len(fixed)}")
        if ns.apply:
            save(fixed)
            print("applied")
        return 0


if __name__ == "__main__":
    sys.exit(main())
