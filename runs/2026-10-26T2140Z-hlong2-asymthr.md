# 2026-10-26T2140Z — H-LONG2 (asymmetric thr_long): REJECTED; path-dependence found (type: wake, experiment)

**Hypothesis (pre-registered at 2100Z close):** the long-side loss in B
(short-only) is concentrated in the thin prob band (0.45,0.50]; raising
thr_long alone (keep "fat" longs ≥0.50) should recover most of B's DD/Sharpe
gain at ≤ half of B's PnL cost. Success bar (family-wise): mean PnL loss vs
A < $300 AND mean maxDD improvement ≥ 25%; partial: pooled Sharpe > B's 1.59
with loss < $1,134. Replay on cached signals (identical exits, 902 test
days, noFri, thr_short 0.45, trail 2.0/5.0/1.5).

## Stage 1 (seed 0 scan) — no cell qualifies
| variant | n | PnL | maxDD | Sharpe | loss vs A | loss ÷ B-loss(677) |
|---|---|---|---|---|---|---|
| A baseline | 565 | +4,255 | −1,607 | 1.13 | — | — |
| B short-only | 287 | +3,578 | −904 | 1.69 | 677 | 1.00 |
| thr_long 0.50 | 500 | +3,308 | −1,371 | 0.99 | 947 | **1.40** |
| thr_long 0.55 | 441 | +3,123 | −1,331 | 1.04 | 1,133 | 1.67 |
| thr_long 0.60 | 392 | +2,608 | −1,207 | 0.97 | 1,648 | 2.43 |

Selection rule (largest T with loss ≤ ½·B) → **no T qualifies**; per
protocol T=0.55 still goes to stage 2 (it was pre-registered from the
decomposition).

## Stage 2 (T=0.55, seeds 0–3)
| seed | A pnl | A maxDD | A Sharpe | T pnl | T maxDD | T Sharpe |
|---|---|---|---|---|---|---|
| 0 | +4,255 | −1,607 | 1.13 | +3,123 | −1,331 | 1.04 |
| 1 | +4,796 | −1,906 | 1.25 | +3,977 | −1,276 | 1.33 |
| 2 | +4,874 | −1,960 | 1.29 | +3,917 | −1,247 | 1.32 |
| 3 | +4,021 | −1,809 | 1.07 | +2,846 | −1,250 | 0.97 |
| **mean** | **+4,487** | **−1,820** | **1.19** | **+3,466** | **−1,276** | **1.17** |

- Success: loss $1,021 (needs <300) → **FAIL** (DD improvement 29.9% passes
  the 25% bar alone).
- Partial: pooled Sharpe 1.17 < B's 1.59 → **FAIL**.
- **Verdict: H-LONG2 REJECTED.** Asymmetric thresholds are strictly dominated
  by B (short-only) on every axis that matters: T loses ~as much PnL as B
  (1,021 vs 1,134) for half the DD benefit and none of the Sharpe benefit.

## Mechanism finding (the real payload)
Side×bucket decomposition (seed 0, per-trade avg USD):
```
short  (0.45,0.50]  202 tr  +1,495   +7.4/tr    (thin shorts are GOOD)
short  (0.50,0.55]   52 tr  +2,114  +40.7/tr
short  (0.55,0.60]   19 tr    -223  -11.7/tr    (negative)
long   (0.45,0.50]  182 tr    +220   +1.2/tr    (thin, near-breakeven)
long   (0.50,0.55]   62 tr    +856  +13.8/tr
long   (0.60,1.0]    11 tr    -239  -21.7/tr    (negative)
```
Cutting the thin long band (worth only +$220 total on seed 0) costs ~$947 —
~4× the band's own PnL. Reason: the first-cross entry rule is **path-
dependent**; when a thin long is vetoed, the day's entry moves to a later
bar whose (different-ATR-context) trade is on average worse. The thin longs
were gate-keeping days whose later alternatives are bad. Corollary:
probability calibration ≠ entry timing; the model's early weak signals are
screening out worse late-day trades.

## Decision / next
- E3 baseline unchanged (live); B remains the only risk-adjusted variant.
- **H-PROB (next cycle), refined by today's table**: SIDE-CONDITIONED band
  gates — drop short entries with p∈(0.55,0.60) and long entries with
  p>0.60 (the two negative cells), keep everything else. Naive (side-blind)
  band gating would have been mis-specified: (0.45,0.5] is good on the short
  side and marginal-but-load-bearing on the long side.

## Files
- trades: runs/data/2026-10-26T2140Z-hlong2_T055_s0.csv
- No algo code changed (measurement only). Sierra: none.
