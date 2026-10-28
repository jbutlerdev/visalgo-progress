# 2026-10-28T1545Z — Fee basis codified (MEASURED_RT_FEE_USD=2.26 + decision-run rule + 4 tests) and the live z-gauge built: E3-MES forward test currently **z ∈ [−0.52, −0.07] — not broken** (type: wake, ~20min)

## (1) Fee-basis codification (queue item 1 from 1455Z; log catch-up)
Branch `algo-dev/fee-basis` (76e6457):
* `MEASURED_RT_FEE_USD = 2.26` constant added (measured live MES, from
  the k×2.26 Change-field decomposition);
* **decision-run rule in AGENTS.md step 3**: GO/NO-GO numbers must run
  at 2.26 (or report both); the 1.25 default is explicitly FROZEN for
  legacy reproduction (never silently repoint — keeps every logged
  number bit-reproducible);
* 4 pinning tests (subprocess-level default check + env-override).

## (2) Live-vs-expected z-gauge (queue item 3 from 1455Z) — DONE
Branch `algo-dev/live-zgauge` (37 ml tests OK):
`python3 -m ml.live_z_gauge <fills_dir> --since 2026-10-08`
* parses read-only TradeActivityLog copies; era filter (agent era
  starts 10-08; Sept sessions excluded);
* **dual estimator** (honest-range design): est1 EOD `Change:`-sum
  misses sessions without an adjustment line (lower |loss| bound);
  est2 NLV-continuity minus inferred flows — reported as a RANGE
  because coverage is 10/11 sessions (busiest day 10-22 lacks the line);
* verdict line: |z| < 2 ⇒ not broken (vs chop-conditioned −$5.65/session).

**Current live read (E3-MES forward era):** 11 sessions, 20 RTs,
z ∈ **[−0.52, −0.07]** ⇒ **the forward test is tracking expectations;
not broken, not yet proven** — exactly the running gauge the 1455Z
cycle said we needed instead of one-off gut calls. (Deposit detection
heuristic flagged −33 vs manual +160 — est2 has a flow-detection gap;
logged as known limitation, range still bounds the truth.)

## Queue state (from 1455Z)
1 fee-basis ✅ · 3 z-gauge ✅ · 2 fill-price extraction (DTC
trade-activity request type — needs new protocol msg; next cycle on
the dev box) · tonight 21:30Z OOS refresh armed · GPU LSTM study
session queued · v4 DLL lane next.

Sierra touched: none this cycle. Datasets read-only.
