# 2026-10-26T2100Z — H-LONG: long-side entries tested and (partly) rejected (type: wake, experiment)

**Hypothesis (pre-registered from baseline decomposition):** long entries are
noise — 278 longs made +$677 (avg +$2.43/trade) vs 287 shorts +$3,578
(avg +$12.5/trade). Prediction: short-only holds PnL within ±$300 (stream
band) while trade count halves and maxDD shrinks. Falsifier: short-only
loses > $600 vs baseline → longs carry real edge.

**Design:** signals (walk-forward argmax/proba matrices) collected ONCE,
then replayed — A (baseline, first entry ≥ thr any side), B (drop long
trades; entry timing = baseline), C (short-only with re-entry: first
SHORT-class bar ≥ thr). Same window (2022-10-18..2026-10-02, 902 test
days), same thr 0.45 / trail 2.0-5.0-1.5 / noFri. Stream robustness: seeds
0–3 (4 full walk-forwards; stream sd is the documented
CPU-CUDA-equivalent resampling variance).

## Results (per stream; net USD, ES $5/pt, costs 1.25/trade)
| seed | A n | A pnl | A maxDD | A Sharpe | B n | B pnl | B maxDD | B Sharpe |
|---|---|---|---|---|---|---|---|---|
| 0 | 565 | +4,255 | −1,607 | 1.13 | 287 | +3,578 | −904 | 1.69 |
| 1 | 570 | +4,796 | −1,906 | 1.25 | 285 | +3,361 | −1,042 | 1.59 |
| 2 | 570 | +4,874 | −1,960 | 1.29 | 284 | +3,702 | −1,023 | 1.76 |
| 3 | 567 | +4,021 | −1,809 | 1.07 | 283 | +2,770 | −1,009 | 1.33 |
| **mean** | 568 | **+4,487** | −1,821 | 1.19 | 285 | **+3,353** | **−995** | **1.59** |

seed-0 also: B PF 1.36 vs A 1.21 · B worst-quarter −195 vs A −378 ·
B return/DD 3.96 vs A 2.65. C (short-reentry) seed-0: +3,108 / maxDD −957 —
re-entry adds 47 trades for −470 vs B: **rejected** (later-in-day short
signals are worse than the first cross).

## Verdict — honest split
- **H-LONG ("longs are noise") is FALSIFIED as stated.** B loses ~$1,134
  on average (range −680 to −1,250), beyond the ±300 hold band and past the
  −600 falsifier. Longs contribute real (thin) absolute edge: ~+$4/trade
  mean, positive in all 4 streams.
- **But B dominates on risk-adjusted terms in every stream:** Sharpe
  1.19→1.59 (+34%), maxDD −1,821→−995 (−45%), worst-quarter −378→−195,
  PF 1.21→1.36 (seed 0). Per unit of risk, longs are noise; per dollar
  they are (thinly) paid.
- Decision: **do NOT switch the live algo** (absolute PnL is Jeremiah's
  registry currency and E3 is live). Record `E3-short-only` as a
  risk-adjusted variant candidate; natural follow-up H-LONG2 (queued):
  long-side-only threshold bump (thr_long 0.50–0.55) instead of a drop —
  keeps the fat-probability longs (the (0.5,0.55] bucket was strong on both
  sides in the baseline decomposition) and cuts the thin tail that costs DD.

## Files
- Per-trade tables: `runs/data/2026-10-26T2100Z-hlong_A_baseline.csv`,
  `..._B_shortonly.csv` (day, bar, side, prob, entry, atr, exit tag, pnl).
- Signal caches (seeds 0–3) kept in sandbox ~/work for H-LONG2 reuse.
- No algo code changed this run (measurement only); no repo code commits.

## Sierra touched
none.

## Next
1. H-LONG2: asymmetric thresholds thr_short=0.45 / thr_long∈{0.50,0.55}
   (replay on cached signals — cheap, same rigor).
2. Then H-PROB two-sided gate (0.55–0.60 bucket negative on both sides).
