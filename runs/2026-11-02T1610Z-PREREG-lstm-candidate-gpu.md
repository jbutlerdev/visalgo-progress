# 2026-11-02T1610Z — PRE-REGISTRATION (committed BEFORE any metric): ML candidate #1 — walk-forward LSTM on ratified ES surface (vram lane)

## Status: GATED. No training until (a) GPU occupancy cleared (llama-server
23,812/24,576 MiB at 16:01Z; Jeremiah asked: queue-poll vs hold-for-free),
AND (b) this doc stands as the locked spec. No metric sighted before launch.

## What runs (file-confirmed, not memory)
Runner: ml/lstm_wf.py (visalgo@e4d7b7f, unmodified — if modification needed,
it becomes a NEW named script + this doc amended pre-run). Host:
administrator@10.10.199.146 (RTX 3090; ~/visalgo clone; ~/venv py3.12.3,
torch 2.14.0+cu130 cuda True). Entry: ~/venv/bin/python -m ml.lstm_wf <out>.
Protocol (read from file): same FEAT_PREFIX (ml.xgb_wf), same 3-class labels
(ml.features.make_labels defaults 1.5/2.5 ATR, WIN-horizon), prev-60-day
train / 5-day step, one position/day, entry argmax w/ hold-class filter,
SEQ=36 (<=42 constraint), HIDDEN 64 x1 layer, EPOCHS 30, BATCH 256, LR 1e-2,
TICK 5.0 / COST 1.25 — parity-checked vs pipeline TICK_USD/ENTRY_COST_USD
(both 5.0/1.25 defaults, grep-quoted in wake).

## Locked experiment spec (declared now)
- Data: data/parquet/ES_front.parquet via ml.features.build_features (same
  stream as ratified harness). Window: days_all[-504:] (RATIFIED window —
  same context as canonical v2 pins; no new windows).
- Seeds: torch.manual_seed + np.seed = 0..3 (mirrors xgb 4-seed convention).
- Arms: LSTM vs the RATIFIED XGBoost v2 baseline context (harness identity:
  W.replay call-seq; LSTM replays its own signals with the SAME sim_pnl
  intra-bar exits as its file — exit-parity deviation vs W.replay trail
  declared UP FRONT: lstm_wf uses sim_pnl (fixed SL/TP), so its comparison
  target is the ratified harness's FIXED-exit e3 shape from the OOS table
  (descriptive context), NOT v2 trail. Hypothesis = model class, exits held
  at file defaults; no exit knob shopping).
- Primary metric (declared): per-seed total pnl_usd + n (recorded not
  assumed); G1-style bar: mean pnl within [-50%, +inf) OF e3 pooled total
  (12,043.70 per OOS table @ 845bb33) — i.e. LSTM must not collapse the
  strategy; +$150 bars do NOT transfer (EA policy: bars are per-hypothesis);
  a beat of e3 is reported as DESCRIPTIVE unless separately pre-registered.
- G3 (BINDING): maxdd via repo summarize_days on pooled daily pnl (same
  convention as H-GAPDAY G3); verdict never prints without it.
- G4: 12-month date-window recency (same rule; empty raise, <100 warn).
- Determinism: fixed seeds; versions recorded (torch/py/cuda); single run
  per seed; re-run only as identity check (diagnostics-not-evidence).
## Discipline: DEFER to human sessions (re-query compute-apps before alloc);
no sudo; training jobs only; writes confined to out_prefix dir; no key/config
touching; artifacts + raw stdout committed per constitution; numbers to EA
before any candidate claim (promotion = Jeremiah).
