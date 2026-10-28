# 2026-10-28T1235Z — review-stack equity curves on the cockpit (menu-5): E3 → v2 → v3 → v4 rendered side-by-side, recomputed from sig caches (never hand-entered) — README's "curve is the point" now true for the decision stack (type: wake, ≤20min)

vram gate #40: unchanged (Thu ping next cycle).

## Gap fixed
README mandates algos[] with equity curves for performance runs — my
experiment cycles (rightly) logged verdicts not curves, but that left
the ONE thing Jeremiah actually reviews (the v2/v3/v4 stack) without
curves on the cockpit. Computed all four comparators from the sig
caches (single source, repro ~/work/dash_curves.py; metrics recomputed,
never remembered):

| algo | PnL/stream (mean s0-3) | trades | ΔPnL vs E3 |
|---|---|---|---|
| E3 (live registry) | **+$4,487** | 2,272 | — |
| v2 (prob vetoes + trail) | **+$5,314** | 2,160 | +$827 ← matches 0840Z audit exactly ✓ |
| v3 (+ TS54) | **+$5,712** | 2,160 | +$1,225 |
| v4 (+ Z-veto + TS54) | **+$5,803** | 2,059 | +$1,316 |

**The cockpit story is monotonic improvement with FEWER trades**:
2,272→2,059 trades while PnL climbs +29% and DD-of-mean-path improves
−1,820→−1,060 (label note in params: mean-path DD is smoothed;
per-stream DD slightly worse, logged honestly). v2's +827 exactly
reproduces the deployable-definition audit — independent re-validation
through a third code path (dash_curves exec'd from h_zoneveto_pkg's
run_pkg lineage; cross-checks against v2_deployable_audit.py).

## How it renders
This entry carries algos[] ⇒ four cards with sparkline curves +
metric chips at the top of the dashboard feed (the renderRuns loop
already draws them). Review flow: open cockpit → four curves + numbers
→ decide. No tab-switching to logs for the headline comparison.

## Honesty notes
- "mean of seeds 0-3" convention stated in params (each stream is a
  full independent 4y run; mean path ≠ pooled trades).
- v4's Z component remains MIXED/parked (curve shows the full-stack
  effect; the Z-only marginal straddles its bar - logged 0655Z, not
  re-litigated here).
- CPU-convention pending GPU parity (unchanged caveat).

Sierra: none. Datasets read-only (MANIFEST-verified). No code change.
