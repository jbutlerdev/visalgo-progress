# 2026-10-29T0030Z — Approved GPU study, part 1: **paired XGB-vs-LSTM pilot done** — LSTM ahead on the slice (+$74 vs −$131, WR 50 vs 38%) but n≈27 trades = far too thin for any claim; llama restored-verified (type: wake, ~28min)

## GPU session #2 (Jeremiah-approved; restore gate honored)
A1 baseline locked (active/health:200/laguna-xs-2.1/24,083 MiB) → A2
stop (266 MiB) → A3 sync canonical `ml/`+`export/` (vram repo was
b0fb47f, pre-`ml/`) + paired-pilot run → A4 **RESTORE verified**:
active, health:200, correct model, 24,083 MiB. Outage ~50 min (longer
than planned: my pilot harness had 4 hardcoded-path bugs — all in my
scratch script, none in the repo; fixed one per round-trip).

## The pilot (paired, identical everything)
Same folds (8 folds × 5 test-days from day 90 ≈ 40 trading days),
same 27 features, same entry semantics (first-cross 0.45 ≤ bar 41,
WIN-36 guard, noFri, one/day), same pessimistic E3-trail exit
(2.0/1.5, sl-first), seed 0. XGB = registry cfg ens3; LSTM =
ml/lstm_wf Net (LSTM 64→16→3, SEQ 36) trained per fold on GPU.

| arm | trades | PnL | maxDD | win% | mean p |
|---|---|---|---|---|---|
| XGB (registry) | 29 | **−131** | −239 | 37.9 | 0.487 |
| LSTM | 26 | **+74** | −139 | 50.0 | 0.805 |

## Honest read (no claim made)
* direction interesting — LSTM better on this slice AND its
  mean-confidence 0.805 (vs XGB 0.487) says it's *confidently* better
  or miscalibrated, can't tell at n=26;
* **n≈27 trades ≈ ±$300 1σ — statistically nothing**; and these folds
  are REGISTRY-ERA days (the window the whole candidate story was
  tuned on) — informative for signal-quality comparison, NOT OOS;
* pre-registered next step (if the study proceeds): full 212-fold
  walk-forward (~35 min GPU, caches exist now) × seeds 0–2 + the OOS
  tail window, calibration (reliability) check on LSTM probabilities.
  No deployment implication whatever until then; E3/registry stands.
Fold caches + result.json on vram (`~/pilotwork/`) and copied here.

## vram hygiene note (Jeremiah FYI)
`~/visalgo` there had **pre-existing staged work** (drift_check.py,
build DLLs, PROCESS.md — 14 files) which I left untouched; my cleanup
removed only my own synced copies, but the sync had overwritten their
working-tree copies of `ml/drift_check.py` + `ml/PROCESS.md` with the
canonical versions (staged blobs still hold the originals:
`git diff` on those two if you care). My artifacts left behind:
`~/lstm_pilot.py`, `~/pilotwork/` — deletable.

Sierra touched: none (vram is not a Sierra box). Datasets read-only,
canonical parquet hash-verified on vram. Llama restored + verified.
