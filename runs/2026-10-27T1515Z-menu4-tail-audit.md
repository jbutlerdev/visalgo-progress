# 2026-10-27T1515Z — menu-4 DONE: fresh .scid tail pulled from .61 (key auth), audited vs frozen front — PASS; 18 fresh days banked as fuel (type: wake, ≤25min)

Key-auth SSH (provisioned 14:43Z) makes the self-serve tail pull real.
Executed menu-4 this cycle under the 24/7 law.

## What ran
1. **Read-only pull:** live front-contract `ESZ26_FUT_CME.scid` (952 MB)
   from .61 via scp to my workspace (never wrote to .61; never touched
   /opt/agent-data). Copy raced the live writer (file grew mid-copy) —
   reader tolerated it; last tick 15:06:38Z captured intact.
2. **Freshness:** covers 2026-08-28 → **2026-10-27 15:06Z (today)** —
   the dataset-frozen blocker is now moot for tail verification: the
   .scid IS the growth path.
3. **Scale finding (independent confirmation):** within-file flip at
   **2026-10-07 02:49Z** — pre-flip rows in points (7,799.5), post-flip
   in x100 tick units (775,100). Exactly the documented ESZ26 tail-bug
   date that `ml/scale_guard` was built for: the canonical dataset's
   guard policy matches the raw source's true behavior. Normalized the
   x100 region by /100 for the audit (raw file untouched).
4. **Overlap audit (front vs scid re-derive, 1,917 common 5-min RTH bars
   in the 8/28–10/2 window):** close diff front−scid **p50 = 0.00 pts,
   mean 0.35, p95 2.25, max 6.75**; per-day offsets tight (std of day-
   means 0.65; day-mean p10/p90 = 0.00/1.05) — consistent with Sierra
   chart-space per-day offsets at the small end for this period (the
   PROCESS-lore ~400-pt offset is a monthly-contract artifact, not
   present here). **Verdict: PASS — the frozen front agrees with the
   independent live source at the tick level for the overlap window.**
5. **Fuel banked:** normalized tail beyond front-end saved —
   **1,316 bars / 18 trading days (10-05..10-27)** in my workspace as
   `ES_tail_20261003_27.parquet` (raw ESZ26 = front month for this
   window, no roll inside; caveat noted: not back-adjusted composite).

## Unblocked / next
- **Menu-1-extension queued (next cycle):** replay package v2 vs E3 on
  the fresh 18-day tail (signals from the existing caches end 10-01 —
  so this first pass is an EXIT-PATH/OHLC sanity replay on new bars
  using cached-model signals where they cover, plus a fresh-feature
  smoke check; full retrain-on-tail evaluation waits for ~60+ days or
  an incremental build_dataset run over the merged series).
- Menu-6 (vram LSTM): box confirmed RTX 3090, auth green; first job
  staged (nvidia-smi gate → own dirs → GPU parity → LSTM wf).
- Menu-3 done; menu-5 (dashboard analytics) remaining for later cycles.

Sierra touched: **live-readonly** (one scp pull; no writes, no toggles).
Datasets: /opt canonical read-only (untouched); frozen front untouched.
Repos: no code change this cycle.
