# 2026-11-01T1730Z — PRE-REGISTRATION (before numbers): harness-reproduction attempt (route (a), file-side)

## Trigger + evidence found in files (not memory)
runs/2026-10-28T0400Z-hsize-ratio-fix.md records the pins VERBATIM: "v2
stream means ... +$6,331/+$8,083/+$6,742/+$6,296 (seeds 0-3, cached sigs,
CPU convention)" — pre-outage entry, independent of EA memory; 0355Z entry
names repro h_size_base.py/h_size.py (perished ~/work). Route (a) executable
file-side: my regenerated staged script (580ad9e, 3 EA review rounds folded)
claims to BE the campaign harness (trail 1.75/1.75, noFri, kill-day veto,
first-bar p>=0.45, sl-first, +0.25t, CPU convention).

## Procedure (fixed BEFORE running)
1. Patch staged script signals(): use repo W.collect_signals (bindings
   1705Z) + cache per seed under work dir; ohlcv dict from np columns
   (o,h,l,c = [:,0..3]); window = days_all[-504:] (repo main default —
   declared choice; miss-analysis will check window if needed).
2. calibrate(): 3-way side-mapping search (entry_for() says arg==2->+1;
   search retained as harness verification), reproduce pins +-1%, else STOP.
3. One run, no spec-shopping. Window/feature variants are NOT tried
   iteratively until match (that would be bar-shopping the gate); single
   declared configuration.

## Interpretation (declared now)
MATCH +-1% on all 4 seeds -> campaign harness recovered in-file; calibrate
gate passes on its own lineage; W.replay-mandate vs campaign-harness becomes
EA adjudication item (bars encode THIS harness, not wf_adaptive.replay).
MISS -> STOP, report; route (b) re-baseline is then the only sound path and
remains EA/ Jeremiah adjudication. No third path, no silent retries.
