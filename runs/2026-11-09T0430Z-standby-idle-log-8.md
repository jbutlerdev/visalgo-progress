# STANDBY idle log — ROLL 8 (opened 2026-11-09T04:30:57Z, real clock read at file-open)

Continues roll #7 (2026-11-08T1830Z, frozen at 370 lines incl. probe 319,
the NQ full-corpus QA pass, RETRACT/incident-#11 entry, volume-cross front
build, classical baseline campaign, naive-XGBoost experiment + audit
notes). Rolls #1-#7 FROZEN documents (traces/retractions intact — never
edited). This roll carries the live cadence.

**Standing state at roll-open** (verbatim from probe 319, logged in roll
#7 at 04:00:43Z, commit f25f40b): visalgo ticks-builder=e4d7b7f,
progress main=f25f40b, zero-byte=0/61 (Jeremiah data-repair verified),
raw-data AVAILABLE 61/61, gpu ssh CONFIRMED (llama-server 23,812 MiB ->
human session -> DEFER holds, read-only monitor each wake), Campaign-1
5y corpus DONE: volume-cross front 61/61 months, 351,842 bars, span
2021-03-10..2026-03-09 (FRONT_ROLLUP.json; Jan25 28-31 + Aug24 28-30
source gaps disclosed, re-pull awaited); classical bar set: dualMA
-$38.3k / Donchian20 -$52.8k / naive-XGB -$80.5k (holdout PF 0.32)
all net-negative at $5/side -> pre-reg 41b9044 must beat net-negative
on same holdout; LSTM pre-reg SINGLE-blocked on GPU (queue 'proceed'
answered); dash rows tools/dash.py-only, idle lines md-only. Ledger
rows=24; 319 probes; 26 STRIP-#2 gap rows + recovery arcs x3 closed.

Integrity tally: ELEVEN fabrication-class incidents (all self-caught,
zero trading content touched) + alarm-hygiene near-miss (false fleet
flag retracted same-turn). Rules: R-F / R-F-2 / R-F-2b / R-F-3 (probe
cites own same-turn output; first tool call; header ts VERBATIM) /
R-F-4 / R-F-4b (verify-before-assert covers alerts). Runbook:
docs/RUNBOOK-sandbox-recovery.md.

First probe in this roll = 320.
- 2026-11-09T05:00Z (slot note — probe 320 deferred to the probe-call
  below; R-F-3 governs) EXPERIMENT (interim, CPU-only, while GPU DEFER
  holds): COST-ROBUST LOW-TURNOVER SCREEN, 3 variants on the same
  volume-cross corpus/split/cost (lowturn_results.json):
  ma12_48_hysteresis(2bp band): train -25,615/4,829 turns, holdout
  -3,560/2,285 PF 0.99; ma12_288 (day-trend): train -8,068/1,986,
  holdout -4,993/989 PF 0.99; donchian1152 (5-day): train -5,286/141,
  holdout -2,182/69 PF 1.00. VERDICT: turnover reduction shrinks
  losses ~5-24x (hysteresis halves turns; 5-day Donchian cuts 11,401
  -> 69) and PF converges to ~1.00 — gross signal is essentially
  zero-cost-neutral; NONE beats the bar (all still net-negative on
  holdout). Cumulative pre-reg context: SIX net-negative references;
  LSTM must show real directional edge, not just turnover control.
  dash.py row appended. One entry this turn.
- 2026-11-09T05:00:52Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from its output line "fetch-rc=0
  origin/main=3628237 zero-byte=0/61 gpu=[256 MiB venv python;23812
  MiB llama-server] date=2026-11-09 time=05:00:52Z"; R-F-2b: no
  embedded duplicate -> no coalesce claim; R-F-4b: no suspicion, no
  retraction) e4d7b7f 3628237 quiet — probe 320 (first line, roll
  #8). ~30min after probe-319 (measured from 04:00:43Z; intervening
  slot was maintenance rollover). State block: zero-byte=0/61 |
  raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server
  23,812 MiB -> DEFER holds; pre-reg 41b9044 gate monitor). One
  entry this turn.
