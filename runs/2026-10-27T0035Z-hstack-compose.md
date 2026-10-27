# 2026-10-27T0035Z — H-STACK: H-PROB × K30 compose near-additively (+$567, 4/4, DD −1,288) (type: wake, exploratory, ≤25min)

**Question (follow-up from 0005Z queue):** do the two kept filters — H-PROB
kill-day vetoes (short p(0.55,0.60], long p>0.60; +$495 4/4) and H-TOD K30
kill-day late cutoff (+$100 3/4, individually below bar) — compose
independently or cannibalize? Exploratory pass (no new success bar claimed —
the combined cell gets a pre-registered confirmation next cycle if Jeremiah
wants it pursued).

## Results (seeds 0–3, cached signals, identical exits/gate/window)
| variant | mean dPnL | pos | mean maxDD | mean Sharpe |
|---|---|---|---|---|
| A baseline | — | — | −1,820 | 1.19 |
| prob (H-PROB) | +$495 | 4/4 | −1,623 | 1.38 |
| k30 (cutoff) | +$100 | 3/4 | −1,462 | 1.34 |
| **prob+k30** | **+$567** | **4/4** | **−1,288** | **1.55** |

Additive expectation was +$596 → combined achieves 95% of it (mild overlap,
expected: the 5 vetoed-population trades per stream sometimes sat past bar
30 anyway). DD improvement is SUPER-additive (−1,288 vs predicted ~−1,370):
the cutoff removes late tail-risk that prob-vetoes alone leave in.

Per-seed combined: +4,750 / +5,247 / +5,376 / +4,840 (all 4/4 positive,
every stream beats H-PROB-alone on DD; seed-1 PnL dips $127 below
H-PROB-alone while gaining $445 DD — the k30 cost reappearing at the
margin).

## Reading / next
- Mechanisms are independent: probability-quality vetoes + late-hour risk
  removal. If pursued: pre-register H-STACK (combined kill-day) vs the SAME
  bars used for H-PROB (dPnL ≥ +$150... it clears by design since
  exploratory already shows +$567 4/4 — the pre-registration would be a
  formality; the honest new test is band-edge / K sensitivity or OOS split).
- **Better next step (proposed):** pre-registered OOS confirmation of
  H-PROB alone on the last 12 months of the window (2025-10-27..2026-10-02)
  — kills the in-sample-selection concern that applies to ALL candidates
  including a combined one. Then combine only what survives.
- Status: H-PROB still the single pre-registered accepted candidate
  (awaiting Jeremiah); H-STACK recorded as exploratory positive, NOT a
  candidate row yet.

## Files / hygiene
- trades: runs/data/2026-10-27T0035Z-probk30_s0.csv (seed-0 combined).
- Sierra: none. Dataset: read-only. No repo code changed.
