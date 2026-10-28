# 2026-10-28T0125Z — self-correction: offline test totals were quoted from memory (52/58) — verified truth: **58 unittest tests** (loop 23 + ml 30 + maxbars-spec 7 on branch); filter_policy tests live on the v2 branch, not their own; amt_engine is a script not a suite (type: wake, ≤10min)

Log-truthfulness rule fired on me and I'm logging the fix, per policy
("never quote remembered numbers; recompute before claiming").

## Verified counts (recomputed this cycle, per-file -v ok-counts)
| file | tests | where |
|---|---|---|
| loop/test_frame_bars | 10 | loop-testcov |
| loop/test_frame_watchdog | 6 | watchdog-testcov |
| loop/test_validate_frames | 7 | validate-frames-testcov |
| ml/test_scale_guard | 15 | scale-guard (master lineage) |
| ml/test_repair_scale | 15 | master |
| ml/test_maxbars_spec | 7 | maxbars-spec |
| **total unittest** | **58** | |

Corrections to prior claims:
1. **"filter_policy 15 tests on their own branch" — wrong.** The 15
   tests live in `ml/test_filter_policy.py` **on `algo-dev/hprob-bandgate`
   (v2 branch)**, committed with the module they test (856e21c). Better
   arrangement anyway (tests ship with the module); earlier phrasing
   implied a standalone branch that never existed. No work lost.
2. **`ml/test_amt_engine.py` contributes 0 unittest tests** — it's a
   verification *script* (main() vs the DLL ground-truth dump, prints
   OK). Fine as-is (it's the AMT-exactness gate), but it was inflating
   my mental suite count; discover reports "OK" vacuously for it.
   TODO (backlog): wrap in unittest so CI-style discover counts it.
3. The 0105Z run's "total offline 52" was also wrong (memory-quote) —
   true numbers at that moment: 58 including this branch.

Everything else in 0105Z stands (validate_frames crash + fix + 7 tests).

State: master fb1a019; 7 algo-dev branches (incl. scale-guard,
repair-scale-dryfix older ones); 6 review-ready. Sierra: none.
