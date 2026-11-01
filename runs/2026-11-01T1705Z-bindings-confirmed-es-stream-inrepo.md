# 2026-11-01T1705Z — type(b): replay bindings confirmed vs repo files (3 falsified) — ES stream is IN-REPO, frozen sequence NOT blocked by broken bind

## Commands + outputs (constitution #1)
`ls ml/` -> ml/hprob_oos.py MISSING, ml/walk_forward.py MISSING (my staged
script's imports falsified). Real API (grep/sed quoted): ml/wf_adaptive.py
(SEED=0 L50, ENSEMBLE=3, TRAIN_DAYS=90, TEST_STEP=5, MAX_ENTRY_BAR=41,
collect_signals L64, build_day_index L239, replay L194, summarize_days L261) +
ml/pipeline.py build_dataset L90 (reads data/parquet/{FAM}_front.parquet,
VISALGO_FAM=ES default).
`python3 -c read_parquet ES_front.parquet` -> rows 101784, range
2021-02-26..2026-10-02 US/Eastern 5m — **ES stream complete through 2026-10-02
IN-REPO**, independent of the 19 zero-byte bind months.

## Consequences
(1) calibrate gate + OOS + H-GAPDAY frozen sequence run on the IN-REPO ES
stream -> NOT blocked by Jeremiah re-stage. Re-stage only gates NQ tail.
(2) side encoding confirmed from entry_for(): arg==2 -> +1 (0 down,2 up) —
3-way calibrate guessing demoted to harness-verification.
(3) my hand-rolled simulate() = NON-STANDARD (no TICK_USD/ENTRY_COST_USD, no
sub-bar exits, no WIN, no gate_ok): flagged in-file, numbers must come from
W.replay (entry c+0.25*side, sim_pnl_trail/be/fixed, pnl_pts*TICK_USD -
ENTRY_COST_USD). TODO next wake: arms rewrite calling W.replay; then calibrate
vs pins [6331,8083,6742,6296] +-1%.
visalgo@580ad9e (bindings block in script header; py_compile OK).
EA checkpointed (batch-boundary: unblocks frozen sequence).
