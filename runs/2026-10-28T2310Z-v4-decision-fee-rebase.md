# 2026-10-28T2310Z — v4-vs-E3 decision numbers re-based at the MEASURED fee (2.26/RT, per the fee-basis rule): **+$1,370 pooled 4/4, recency +$783 4/4** — the GO case stands at honest fees (type: wake, ~12min)

## Why
AGENTS.md fee-basis rule (from the 1455Z live-fee finding): every
number feeding a GO/NO-GO must be stated at the measured live fee
(2.26/RT), not only the frozen 1.25 legacy default. All v4 decision
figures so far (0840Z deployable audit +$827, recency +$837) were at
1.25. Recomputed from the saved per-stream trade frames (conc_trades_*,
recompute-not-remember) by shifting each trade by −$1.01.

## Result (mean-path 4 seeds, pkg-standard replay, at 2.26)
| | E3 | v4 | Δ |
|---|---|---|---|
| pooled 4y | +3,913 avg | +5,283 avg | **+1,370 (4/4 seeds)** |
| recency 12m | — | — | **+$783 (4/4 seeds)** |
Per-seed Δ: [+1,197, +1,827, +1,056, +1,400] · recency [+552, +1,028,
+$744, +810]. Trade counts: v4 ~517 vs E3 ~568 (fewer trades AND
higher PnL at honest fees — the vetoes+TS54 cut cost-bearing noise).
Fee shift moves v4-vs-E3 delta UP (v4 trades less, so the +$1.01/trade
penalty hits E3 harder) — the measured fee *strengthens* the package
case: Δ +827@1.25 → +1,370@2.26.
**Self-check logged:** first print had a sign bug in my own summary
line (rows correct, aggregate flipped); caught by recompute rule,
clean table above.

## What this changes
Deployment-review table is now fee-honest end to end. No new claims
beyond existing approval (v4 package already approved 1340Z; B3-gated
activation unchanged). Ledger: v4 card carries the fee-rebased Δ.
Sierra touched: none. Datasets read-only (frames in my workspace).
Next: GPU LSTM study scheduled ~00:04Z; B3 awaits Jeremiah (SimMode
flip or backtest alt-path).
