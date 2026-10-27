# 2026-10-27T0005Z — H-TOD (late-entry cutoff): REJECTED on pre-registered bars (type: wake, ≤25min check-in)

**Hypothesis (from 20:00Z decomposition):** entries whose first-cross bar
k>30 (≥12:00 ET) are dead weight (69 trades, −$32, avg −$0.50/tr). Cutting
late entries should raise PnL or at least cut DD without cost. Sweep
K∈{25,30,35} kill-day (stand down) + K30 skip-continue control. Bars: mean
dPnL ≥ +$150, ≥3/4 positive, mean maxDD no worse; least-intrusive K passing.

## Results (seeds 0–3, cached signals, vs A mean +$4,487 / DD −1,820)
| variant | mean dPnL | pos | mean maxDD | verdict |
|---|---|---|---|---|
| K25 kill (cutoff 11:35) | **−$475** | 0/4 | −1,454 | rejected |
| K30 kill (cutoff 12:00) | **+$100** | 3/4 | −1,462 | **rejected (< +$150 bar)** |
| K35 kill (cutoff 12:25) | −$93 | 1/4 | −1,716 | rejected |
| K30 skip | +$100 | 3/4 | −1,462 | identical to kill (no post-12:00 re-crosses ever materialized after a veto — first-cross beyond 30 rarely has a later sibling ≥ thr) |

## Verdict + reading
H-TOD **REJECTED**: no K passes the +$150 bar; the DD gain (−1,462 vs −1,820)
at K=30 costs the PnL bar by $50. Honest interpretation: the late bucket is
flat on average (−$0.50/tr), not negative — cutting it removes ~flat trades
that occasionally carry big wins (hence DD improves but PnL doesn't hold its
bar). This is the third consecutive finding of the same meta-pattern:
**the entry population is more homogeneous than bucket averages suggest;
path-dependence (first-cross) makes post-hoc bucket surgery unreliable.**
Only per-trade-NEGATIVE cells with a mechanism (H-PROB's two veto bands)
have converted so far.

## Queue state
- ACCEPTED candidate: H-PROB (2220Z) — awaiting Jeremiah promotion review.
- Rejected: H-LONG, H-LONG2, H-TOD.
- Next queued: (a) H-PROB stack sanity — does H-PROB + K30 compose or
  double-cut (cheap, cached)? (b) exit-side hypothesis instead of entry-side
  (entry surgery is 0-for-3 while the trail layer was registry-chosen once;
  try nothing — exit scan is already done — instead queue forward-test
  readiness checklist for H-PROB).
