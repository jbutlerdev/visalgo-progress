#!/usr/bin/env python3
"""backfill_algos.py — derive real equity curves + metrics from trade CSVs.

Scans runs/data/*.csv for per-trade logs (columns include pnl_usd), builds
the algo card data the dashboard needs, and attaches it to the runs.json
row that references the CSV (direct mention, same-timestamp run log, or
date prefix). Orphan CSVs get a generated `experiment` row per date so
real, artifact-backed charts are NEVER invisible.

Idempotent: re-running refreshes equity/metrics from the CSVs; never
downgrades an algo that already has equity. Metrics are computed, never
invented: net_pnl = sum(pnl_usd), trades, win_rate, max_dd from the
curve — everything traceable to the artifact (provenance #1).

Usage: python3 tools/backfill_algos.py [--apply]
"""
import csv, glob, json, os, re, sys
from collections import defaultdict

RUNS = "docs/data/runs.json"
DOWN = 400


def curve_from_csv(path):
    rows = []
    with open(path, newline="") as f:
        rd = csv.DictReader(f)
        if not rd.fieldnames or "pnl_usd" not in [c.strip() for c in rd.fieldnames]:
            return None
        for r in rd:
            try:
                rows.append((r.get("day", ""), int(r.get("bar") or 0), float(r["pnl_usd"])))
            except Exception:
                continue
    if len(rows) < 3:
        return None
    rows.sort(key=lambda x: (x[0], x[1]))
    cum, acc, peak, dd, wins = [], 0.0, 0.0, 0.0, 0
    for day, bar, pnl in rows:
        acc += pnl
        cum.append([float(len(cum)), round(acc, 2)])
        peak = max(peak, acc)
        dd = max(dd, peak - acc)
        if pnl > 0:
            wins += 1
    step = max(1, len(cum) // DOWN)
    eq = cum[::step]
    if eq and eq[-1][0] != cum[-1][0]:
        eq.append(cum[-1])
    return {
        "equity": eq,
        "metrics": {
            "net_pnl": round(acc, 2),
            "trades": len(rows),
            "win_rate": round(wins / len(rows), 3),
            "max_dd": round(dd, 2),
        },
        "window": f"{rows[0][0]}..{rows[-1][0]}",
        "trades_n": len(rows),
    }


def main():
    apply = "--apply" in sys.argv
    try:
        rows = json.load(open(RUNS))
    except Exception:
        rows = []
    rows = [r for r in rows if isinstance(r, dict)]

    used = set()
    attached = 0

    # 1) attach by explicit reference in the row's summary or its run .md
    md_cache = {}
    def md_text(r):
        f = r.get("file") or ""
        if f and f not in md_cache:
            try:
                md_cache[f] = open(f).read()
            except Exception:
                md_cache[f] = ""
        return md_cache.get(f, "")

    for csv_path in sorted(glob.glob("runs/data/*.csv")):
        base = os.path.basename(csv_path)
        cands = []
        for r in rows:
            if base in (r.get("summary") or "") or base in md_text(r):
                cands.append(r)
        if not cands:
            # same-timestamp run log: 2026-10-27T1540Z-<x>.csv <-> file/ts
            m = re.match(r"(\d{4}-\d{2}-\d{2})T(\d{2})(\d{2})Z", base)
            if m:
                day, hhmm = m.group(1), m.group(2) + m.group(3)
                for r in rows:
                    ts = (r.get("ts") or "")[:13] + ":" + (r.get("ts") or "")[14:16]
                    f = r.get("file") or ""
                    if f.startswith(f"runs/{m.group(1)}T{hhmm}") or (r.get("ts") or "").startswith(f"{m.group(1)}T{hhmm[:2]}:{hhmm[2:]}"):
                        cands.append(r)
        if not cands:
            # date-prefix bucket: CSVs from the same session-day battery
            day = base[:10]
            same_day = [r for r in rows if (r.get("ts") or "").startswith(day) and r.get("type") == "experiment"]
            if same_day:
                cands = [min(same_day, key=lambda r: abs(int(r.get("ts", "")[11:13] or 0) - int(base[11:13] or 0)))]
        if not cands:
            continue  # orphan -> generated row below
        art = curve_from_csv(csv_path)
        if not art:
            continue
        used.add(base)
        r = cands[0]
        algos = r.setdefault("algos", [])
        name = re.sub(r"^\d{4}-\d{2}-\d{2}T\d{4}Z-", "", base).rsplit(".", 1)[0]
        for a in algos:
            if a.get("name") == name and a.get("equity"):
                break
        else:
            algos.append({
                "name": name,
                "equity": art["equity"],
                "metrics": art["metrics"],
                "params": {"source_csv": f"runs/data/{base}", "window": art["window"], "unit": "USD"},
            })
            attached += 1

    # 2) orphans (real artifacts no row references) -> one row per date
    orphans = defaultdict(list)
    for csv_path in sorted(glob.glob("runs/data/*.csv")):
        base = os.path.basename(csv_path)
        if base in used or not re.match(r"\d{4}-\d{2}-\d{2}T", base):
            continue
        if curve_from_csv(csv_path):
            orphans[base[:10]].append(base)
    added_rows = 0
    for day, files in sorted(orphans.items()):
        ts = f"{day}T12:00:00Z"
        row = next((r for r in rows if (r.get("ts") or "").startswith(day) and r.get("type") == "experiment"
                    and "artifact battery" in (r.get("title") or "")), None)
        if not row:
            row = {"ts": ts, "type": "experiment", "status": "ok",
                   "title": f"artifact battery {day}",
                   "summary": f"Generated row: {len(files)} trade-log artifact(s) from {day} not referenced by any run log; equity + metrics computed from the CSVs.",
                   "algos": []}
            rows.append(row)
            added_rows += 1
        for base in files:
            art = curve_from_csv(f"runs/data/{base}")
            name = re.sub(r"^\d{4}-\d{2}-\d{2}T\d{4}Z-", "", base).rsplit(".", 1)[0]
            if any(a.get("name") == name and a.get("equity") for a in row["algos"]):
                continue
            row["algos"].append({
                "name": name, "equity": art["equity"], "metrics": art["metrics"],
                "params": {"source_csv": f"runs/data/{base}", "window": art["window"], "unit": "USD"},
            })
            used.add(base)
            attached += 1

    rows.sort(key=lambda r: r.get("ts") or "", reverse=True)
    print(f"algos attached: {attached}, generated rows: {added_rows}, rows total: {len(rows)}")
    if apply:
        tmp = RUNS + ".tmp"
        with open(tmp, "w") as f:
            json.dump(rows, f, separators=(",", ":"))
        os.replace(tmp, RUNS)
        print("applied")


if __name__ == "__main__":
    main()
