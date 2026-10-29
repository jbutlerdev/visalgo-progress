# 2026-10-29T0100Z — Branch consolidation: 4 verified lanes merged to master (fee-basis, live-zgauge, client-tests, ts54-doc); master is now the source of truth again (37+8 tests green) (type: wake, ~12min)

## What landed on master (fb1a019 → 4 merge commits)
* **fee-basis**: MEASURED_RT_FEE_USD=2.26 + AGENTS.md decision-run rule
  + 4 pinning tests (1.25 default stays frozen for reproduction);
* **live-zgauge**: `ml/live_z_gauge.py` (dual-estimator live-vs-expected
  tracker) + 3 tests;
* **client-testcov**: `sc_client/test_client.py` (8);
* **ts54-timeslot**: candidate doc only (TS54 *code* is DLL-side,
  lives on v4-activation until B3/B4 complete).
All four verified-green on v4-activation before merge; post-merge on
master: **37 ml + 8 sc_client OK** (was 30+0).

## What intentionally stays on branches (with reasons)
* **v4-activation** (hprob/zonenveto filter_policy + fw24/25/26 DLL
  changes): deployment-affecting — merges to master only after B3
  passes + Jeremiah-gated deploy (branch = the audit trail);
* hprob-bandgate/zonenveto-policy individually: same reason (their
  code is already inside v4-activation);
* oos-pipeline: monster-bar diagnosis still pending (the 2155Z
  pre-scale-slice finding is the workaround; formal fix later).

## Why this mattered
9 branches deep, master 3 days stale = growing drift risk for anyone
else touching the repo (and for future-me post-compaction). Verified
additive work now flows to master on cadence; gated work stays
clearly labeled on its branch.
Sierra touched: none. Datasets read-only.
Next: B3 awaits Jeremiah (SimMode flip vs backtest alt-path — both
specified); full LSTM study (~35min GPU, caches warm) own slot.
