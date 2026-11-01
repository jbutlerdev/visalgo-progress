# 2026-11-01T1825Z — type(a): OOS candidate table on ratified harness (DESCRIPTIVE per pre-reg 39dcde1; identity gate passed)

## Lineage: pre-reg 39dcde1 (design before numbers; zone-combination bug
caught pre-run) -> scripts/oos_table.py (visalgo, committed pre-run,
py_compile OK) -> single run (no re-runs; versions np1.26.4/pd1.5.3/xgb1.7.4).

## Raw stdout
seed 0: v2 2761.08 n315 | e3 3292.04 n315 | v4 3174.98 n214
seed 1: v2 3161.20 n311 | e3 2548.61 n311 | v4 3124.38 n211
seed 2: v2 2920.40 n314 | e3 2984.92 n314 | v4 2683.08 n218
seed 3: v2 3345.36 n315 | e3 3218.12 n315 | v4 2947.62 n217
identity: v2 totals cent-identical to canonical pins OK
v2 [ratified baseline]        pooled n 1255 total 12188.04 | pooled-days {n 327, pnl 12188.02, h1 4611.44, h2 7576.58, worst_q -463.86, maxdd -7564.81, win_days 46.8}
e3 [fixed-exit, 1-knob]       pooled n 1255 total 12043.70 | pooled-days {n 327, pnl 12043.64, h1 4803.03, h2 7240.61, worst_q -1388.86, maxdd -7037.14, win_days 36.7}
v4 [zone-only, 2-knob, DESC-ONLY] pooled n 860 total 11930.05 | pooled-days {n 234, pnl 11930.0, h1 3663.52, h2 8266.48, worst_q -3449.48, maxdd -5672.46, win_days 46.6}

## Descriptive readings (NO gates; no PASS/FAIL per pre-reg — future
hypotheses on these arms pre-register their own bars)
- e3-vs-v2 (1-knob): ~equal totals (-0.4%) BUT different shape: worst quarter
  3x worse (-1,388.86 vs -463.86), win-days 36.7 vs 46.8, maxdd slightly
  better. Fixed exits trade tail-capture for worse worst-quarter on this
  window.
- v4 (2-knob, DESCRIPTIVE-ONLY by pre-reg): -31% trades, ~equal total,
  worst_q far worse (-3,449.48), maxdd notably better (-5,672.46). Zone
  gate alone reshapes risk profile substantially.
- HONEST NOTE: per-seed sums vs pooled summarize_days differ by 2 cents
  (12,188.04 vs 12,188.02) — artifact of per-row 2-dp rounding in the CSV
  path; magnitude immaterial, recorded not smoothed.
- 0 null_atr/identity exceptions; single run; no re-runs.

## Artifact
runs/data/oos_table_20261101T1759Z.csv (3,370 rows: arm/seed/date/pnl_usd).
Feeds Jeremiah's candidate-stack review (with the activation-gate flag:
PRE-re-baseline numbers on unreproducible harness need re-derivation before
activation; THIS table is already file-side and reproducible).
