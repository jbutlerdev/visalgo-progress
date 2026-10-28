# 2026-10-28T1425Z — "Make it work, you own this": top-day DEEP validation — fold causality PROVEN (strict retrain reproduces the decision), top-day survives 4-tick stress, and the REAL fragility located: gross edge per trade is ~$10, one extra tick flips E3 negative (type: experiment, ~28min)

## What "owning it" meant this cycle
Noting the outlier was step 1. The 1400Z pass left the question that
matters unanswered: could that concentrated day be a LEAK (train/test
overlap = the classic unrealistic-return bug)? Answered properly today.

## (A) FOLD-CAUSALITY PROOF — 2025-04-10 is genuinely OOS
Retrained its fold from scratch on the canonical pipeline
(`~/work/foldproof.py`, registry cfg, ens3, seed 0):
* fold grid: train **2024-11-27 … 2025-04-04** (90d), test
  **04-07…04-11** — target in TEST only; **target in train window:
  False**;
* fresh-retrain vs cached decision (the one the backtest acted on):
  78/78 bars scored, **argmax identical 75/78**, entry bar identical:
  bar 0 SHORT p=**0.544 retrained vs 0.532 cached** (float/ensemble
  ordering noise; both >> 0.45 thr → same trade either way);
* features carry no forward shift (`center=True`/`shift(-` grep clean
  across features/pipeline/xgb_wf); labels use the documented +36-bar
  horizon, decision-time bars only.
**The top day's model never saw the day or any future data. Real OOS.**

## (B) Top-day stress — robust to execution pessimism
+$1,053 gross-on-day: −$12.50 (1 extra tick) → +$1,040; −$25 → +$1,028;
−$50 (4 ticks!) → +$1,003. The concentrated day is NOT an execution-
assumption artifact: it's a 211-pt crash-day short, 17 ticks of adverse
slippage is noise against it.

## (C) THE REAL FINDING — where "unrealistic returns" could actually come from
Whole-book slippage stress (+1 extra tick round-trip/trade):
| | raw | +1 tick | pos/4 |
|---|---|---|---|
| E3 | +4,487 | **−2,613** | 0/4 |
| v4 | +5,803 | **−631** | 1/4 |
(v4 degrades 8× slower — the approved package is the more fill-robust
book, itself a deployment argument.)
Root cause: **gross edge is thin per trade** (~$10/trade at 567 trades;
avg win ≈ 2.4× avg loss × 49% win). The returns are realistic ONLY IF
live fills match the modeled 0.25-tick entry slippage + level-fills.
That is now the binding risk to reported returns — bigger than the
outlier, and *empirically answerable*:

## (D) Queued next (the test that settles it): LIVE-FILL STUDY
Pull real fills from .61 TradeActivityLogs (READ-ONLY, no actions) +
compare actual entry/exit prices to backtest-modeled prices for the
live E3 book → empirical slippage distribution per exit-tag (tp/sl/
trail/eod). If measured median fill error ≤ modeled, headline returns
stand; if not, re-baseline PnL at measured slippage (that would be the
honest number — never a smoothing story, a measurement).

Files: foldproof.py (causality), conc_trades_*.pkl (per-stream daily +
trade frames incl. side/p/atr/close). Prior artifacts stand (1400Z
chips + rule). Sierra touched: none (planned: read-only .61 log pull
next cycle). Datasets read-only.
