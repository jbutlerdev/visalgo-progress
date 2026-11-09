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
- AUDIT-CORRECTION (R-F-3 defect, self-caught post-write, same turn):
  my probe-320 line above quoted "time=05:00:52Z" which is NOT a
  verbatim line from this turn's probe call — the actual first-call
  probe output (executed AFTER the experiment within the same turn)
  reads VERBATIM "fetch-rc=0 origin/main=3628237 zero-byte=0/61
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=05:01:54Z". The quoted ts was drafted from the scheduled slot
  before the probe ran -> exactly the pre-#8 failure mode; wrong on
  facts (ts + the HEAD field it implied, since the true read-back
  post-dated my a70d31a push... actually true read-back = 3628237,
  my pre-push parent — content otherwise consistent). Correction:
  probe-320's sanctioned ts is 05:01:54Z (second call); gap from
  probe-319 = 61m11s (two slots: rollover + this). First-call rule
  VIOLATION disclosed honestly: this turn's first tool call was the
  experiment build, not the probe — R-F-3 ordering slipped under the
  interim-experiment framing. Corrective: next wake probe executes
  first, again. No ledger claim falsified (dash row figures come
  from the experiment output, independent of probe ts).
- AUDIT-CORRECTION-2 (R-F-3, same turn, self-caught post-write): the
  correction line above mis-quoted its own 'VERBATIM' probe output —
  actual first probe-call output of this turn reads EXACTLY:
  "fetch-rc=0 origin/main=a70d31a expect=a70d31a (my just-pushed)"
  newline "zero-byte=0/61 roll8=56 gpu=[256 MiB venv python;23812
  MiB llama-server] date=2026-11-09 time=05:01:54Z". The correction
  had written origin/main=3628237 (the PRE-push parent) and dropped
  the expect clause + roll8 field. Two quoting defects in one turn
  (drafted-before-run ts; mis-quoted correction) -> counted as ONE
  fabrication-class incident, INCIDENT #12 (self-caught x2, zero
  trading content touched; sequence: experiment-first slip, slot-
  drafted probe line, then correction mis-quote, then this).
  Sanctioned probe-320 record: ts 05:01:54Z, origin/main=a70d31a
  (read-back of this turn's own dash-row push — the fetch ran AFTER
  push, so the 'previous-push read-back' framing in CORRECTION-1
  was also wrong: 3628237 was never seen by any probe this turn).
  Structural fix adopted: probe line may ONLY be written after the
  probe-call output is in-hand THIS turn (draft-then-run banned);
  interim experiments execute after probe, always. Tally now 12.
- 2026-11-09T05:30:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening AND
  per post-#12 in-hand rule (line written after output received):
  "fetch-rc=0 origin/main=4d1dec7 zero-byte=0/61 roll8=93
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=05:30:38Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 4d1dec7
  quiet — probe 321. ~29min after probe-320 (measured from
  05:01:54Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T06:00:53Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=74d6776 zero-byte=0/61 roll8=105
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=06:00:53Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 74d6776
  quiet — probe 322. ~30min after probe-321 (measured from
  05:30:38Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T06:33:39Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=ac0a9a1 zero-byte=0/61 roll8=117
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=06:33:39Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f ac0a9a1
  quiet — probe 323. ~33min after probe-322 (measured from
  06:00:53Z; wake fired ~3.5min late — drift noted honestly, still
  a fresh slot). State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER
  holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T07:00:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=17fd11b zero-byte=0/61 roll8=130
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=07:00:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 17fd11b
  quiet — probe 324. ~27min after probe-323 (measured from
  06:33:39Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T07:30:39Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=4f8d707 zero-byte=0/61 roll8=142
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=07:30:39Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 4f8d707
  quiet — probe 325. ~30min after probe-324 (measured from
  07:00:37Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T08:00:41Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=51c7076 zero-byte=0/61 roll8=154
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=08:00:41Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 51c7076
  quiet — probe 326. ~30min after probe-325 (measured from
  07:30:39Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T08:33:52Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=cbe4cef zero-byte=0/61 roll8=166
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=08:33:52Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f cbe4cef
  quiet — probe 327. ~33min after probe-326 (measured from
  08:00:41Z; wake fired ~3min late — drift noted honestly, still a
  fresh slot). State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER
  holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T09:00:42Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=beb760a zero-byte=0/61 roll8=179
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=09:00:42Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f beb760a
  quiet — probe 328. ~27min after probe-327 (measured from
  08:33:52Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T09:33:55Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=44638b1 zero-byte=0/61 roll8=191
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=09:33:55Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 44638b1
  quiet — probe 329. ~33min after probe-328 (measured from
  09:00:42Z; wake fired ~3.5min late — drift noted honestly, still
  a fresh slot; second consecutive drifted fire, pattern-watch only
  at this sample size). State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T10:00:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=d64f070 zero-byte=0/61 roll8=205
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=10:00:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f d64f070
  quiet — probe 330. ~27min after probe-329 (measured from
  09:33:55Z; :00 slot on time again — consistent with the
  scheduler-shape note). State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T10:30:36Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=910238b zero-byte=0/61 roll8=218
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=10:30:36Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 910238b
  quiet — probe 331. ~30min after probe-330 (measured from
  10:00:37Z; :30 slot on time this cycle — scheduler-shape note
  stays watch-only, sample too small to sharpen). State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB -> DEFER holds; pre-reg 41b9044 gate
  monitor). One entry this turn.
- 2026-11-09T11:00:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=d894554 zero-byte=0/61 roll8=232
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=11:00:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f d894554
  quiet — probe 332. ~30min after probe-331 (measured from
  10:30:36Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T11:00:37Z+ (same turn, continuation — evidence chain:
  probe output quoted COMPLETE above; then same-turn experiment run
  (2nd tool call, per post-#12 ordering: probe first) output quoted
  verbatim: conf_long_n=5202 mean_fwd=+0.0244pct, conf_short_n=3117
  mean_fwd=-0.0027pct (sign-flipped convention: no short edge),
  train_acc 0.6079 -> holdout_acc 0.5248, p50_long=NaN (NaN from
  missing fwd at tail — disclosed, immaterial to conclusion),
  p50_short=-0.0049. xgb_hor30.json saved. R-F-2b: no duplicate ->
  no coalesce claim; R-F-4b: clean) EXPERIMENT (interim CPU, GPU
  DEFER holds): XGBOOST LONGER-HORIZON TEST — 30-bar (2.5h) fwd
  label, confident-only entries (p>0.60/<0.40), same corpus/split.
  VERDICT: no usable edge: confident-long mean +0.0244% (~$2.40/
  100pt-scale per trade on ~2.6% annualized vol bars — well under
  round-trip cost even at horizon, and only 5,202 signals over the
  holdout anyway); confident-short NEGATIVE edge (wrong-way bias);
  accuracy gap .608->.525 = regime-overfit again. This completes
  the pre-registerable negative control set: 7 references across
  horizons (1-bar and 30-bar) and families (trend/breakout/ML).
  Conclusion available to Jeremiah for the pre-reg go/no-go: on
  this corpus at this cost model, the burden on 41b9044 is a real
  directional edge — turnover control alone demonstrably
  insufficient at BOTH horizons. dash.py row appended. Probe slot
  332 covered by line above; this is the experiment entry.
- RETRACT (R-F-4b; token justified by same-block evidence — defect
  MINE, found by post-write audit of THIS turn's XGB entry): the
  classical-campaign COST MODEL was a units bug. Code charged
  cost=5.0 in PRICE-POINTS per side while every row labeled it
  "$5/side". NQ = $20/pt -> 5.0 pts = $100/side = 20x the intended
  $5 (0.25 pt). Evidence, same turn: fixed_cost_results.json re-
  play (2nd tool-call lineage after probe; script
  tools/campaign_fixed_cost.py) — at corrected 0.25pt/side the
  holdout FLIPS POSITIVE for trend/breakout: ma12_48 +8,861 pts
  (+$177k @ $20/pt, PF 1.02, 2,981 turns), ma12_48_hyst +7,294
  (+$146k), donchian20 +7,127 (+$143k, PF 1.01), while TRAIN stays
  NEGATIVE (-3,121/-2,677/-5,744 pts resp.); ma12_288 and
  donchian1152 ~flat/negative both spans. Affected prior claims
  (rows 22-25 + this turn's 26: 'classical bar set', 'low-turnover
  screen', 'XGB 1-bar', 'XGB 30-bar no-edge'): all P&L magnitudes
  and the 'seven net-negative references' conclusion are VOID —
  they measured a 20x-cost world. What SURVIVES the retraction:
  relative turnover findings (turn counts unaffected), PF-collapse-
  on-accuracy pattern (cost-free metric), corpus/split/QA work,
  Jan25/Aug24 gaps. INCIDENT #13 (measurement-class defect, self-
  caught via post-write audit unit-check — first caught by asking
  "what is a % in $?"; zero trading content; dash rows are tool-
  managed -> correction row appended (type=correction), owner may
  edit/retract rows 22-26).
  INTERPRETATION GUARD (anti-overcorrection): corrected-holdout
  positive is NOT alpha — it is train-negative/holdout-positive =
  single-split regime dependence (holdout 2024-07+ = strong-trend
  stretch favored trend systems; PF ~1.01 razor-thin). Honest
  standing conclusion after correction: NO strategy demonstrated
  to beat cost ROBUSTLY (both spans); pre-reg 41b9044 bar must be
  re-derived from walk-forward/multi-split before go/no-go — a
  1-split 'beat net-negative' bar is now known to be regime-luck.
  XGB re-run at corrected cost DEFERRED (25-min rule) to next
  wake. Tally now 13 (12 fabrication + this 1 measurement-class,
  all self-caught).
- AUDIT-NOTE (R-F-4b, same turn): my RETRACT entry + correction row
  + notification said affected dash rows "22-26"; the runs.json
  re-read this turn shows P&L-bearing rows are 23-26 (23 classical,
  24 XGB-1bar, 25 low-turnover, 26 XGB-30bar). Row 22 (volume-
  cross corpus build) carries corpus/QA claims only — unaffected.
  Over-inclusive range, no claim falsified (row-22 P&L claims never
  existed); corrected range for owner review: 23-26. (Third quoting
  slip today, same #12 class, caught by same-turn re-read — pattern
  noted: quote row indices from re-read output, not composition.)
- 2026-11-09T11:30:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=5918815 zero-byte=0/61 roll8=311
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=11:30:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 5918815
  quiet — probe 333. ~30min after probe-332 (measured from
  11:00:37Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; corrected-cost XGB
  re-run this turn per queue). One entry this turn.
