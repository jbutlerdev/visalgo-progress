# 2026-10-26T1840Z — ml/repair_scale hardened: 3 real bugs fixed, 15 unit tests (type: wake)

Cycle goal: validate the freshly-landed `ml/repair_scale` tool (Jeremiah's
`d588701`) against the canonical dataset. Result: found and fixed **three
real defects** before the tool is ever needed again on a live append bug.

## Findings (measured)
1. **Dry-run did not converge**: detection never mutated anything, so the
   8-iteration loop re-reported the FIRST flip 8 times and silently missed
   every later flip. Any pre-flight `--dry` review was fiction.
2. **Old dry-run CRASHED on all 14 `TICK-*` parquets** (`ValueError: math
   domain error` in `log10` — tick "close" columns contain 0/negatives), and
   on 2 more via a later path: old tool on a read-only copy of the dataset →
   **flagged 0 files, crashed 14/14 tick files**.
3. **No power-of-10 sanity check**: it would "repair" any >30x ratio, incl.
   genuine 31x–246x data jumps (94x in TICK-NYSE) — corrupting files instead
   of fixing them. A loose tolerance (0.05 log10) still let 94x through;
   final tolerance **1e-3**: genuine x100 appends deviate ≤ ~2.2e-5 (float
   noise), the most scale-like real jump (94x) deviates 0.027 — 27x outside
   the band. Clear separation.
4. Good news confirming dataset health: with the fixed tool, a full scan of
   a copy of `data/parquet` (80 files) finds **0 scale flips to repair** —
   the 2026-10-08 x100 tail bug class is fully repaired in the canonical
   dataset. 11 tick files now get honest `outlier` reports (left untouched)
   instead of crashes/phantom repairs.

## Fix (master `8bf78c1`)
- Detection advances on a private working copy → dry-run now reports exactly
  what a wet run would repair; loop budget 8 → 32; scan advances past
  reported outliers.
- Non-positive closes skipped (no more crash); flips must be within
  SCALE_TOL=1e-3 (log10) of a power of 10, else reported as `outlier`.
- Negative-exponent repair uses division (quarter-tick round-trips exact).
- New `--include` filter so tick-volume dirs can be excluded explicitly.
- New `ml/test_repair_scale.py`: **15 tests, all pass** (clean-series
  no-op, legit 5% gap untouched, x100/x0.01/x1000 repair, multi-flip
  convergence, dry-run mutation-free & flip-complete, 31x/94x reported-not-
  repaired, 0/negative no-crash, quarter-tick bit-exactness).

## Verification
- `python3 -m unittest ml.test_repair_scale` → Ran 15, OK (post-merge on
  master too).
- **Wet end-to-end**: copied ESZ26 monthlies into the repo data dir,
  injected the exact 10-08 failure mode (tail x100), ran the CLI wet →
  detected "flip ... factor=0.01 bars=14", rescaled 1 file; repaired file is
  **bit-for-bit identical** to the canonical read-only copy. (The wet test
  briefly dirtied git-TRACKED parquet copies — restored via `git checkout`,
  verified byte-identical to HEAD. Note: repo data/parquet is NOT fully
  gitignored after all — tracked files live there. Future wet tests must
  copy to a scratch tree, not the repo data dir.)
- Read-only mount respected: no writes under /opt/agent-data.

## Sierra touched
none.

## Blockers / next
- Sandbox lacks a parquet engine (pyarrow) — pip-installed per-sandbox
  (pyarrow 14.0.2, numpy-2 incompatible default was the gotcha); filed forge
  package request `python3-pyarrow` (f2fc8ab5), pending approver.
- Next candidates: apply the outlier report to `update_dataset` (block
  appends that would create non-power-of-10 jumps at the seam), or move on
  to `ml/drift_check` offline coverage; E3/B12C candidate work if data
  allows.
