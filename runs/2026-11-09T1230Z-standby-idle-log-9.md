# STANDBY idle log — ROLL 9 (opened 2026-11-09T12:30:54Z, real clock read at file-open)

Continues roll #8 (2026-11-09T0430Z, frozen at 406 lines incl. probe 334,
the low-turnover screen, incidents #12-#14 + audit corrections, the COST
UNITS BUG retraction #13, corrected-cost replays, and the clean-text
re-issue). Rolls #1-#8 FROZEN documents (traces/retractions intact —
never edited). This roll carries the live cadence.

**Standing state at roll-open** (verbatim from probe 334, logged in roll
#8 at 12:01:18Z, commit bebaebc): visalgo ticks-builder=e4d7b7f,
progress main=bebaebc, zero-byte=0/61, raw-data AVAILABLE 61/61, gpu ssh
CONFIRMED (llama-server 23,812 MiB -> human session -> DEFER holds,
read-only monitor each wake). Corpus DONE: volume-cross front 61/61
months, 351,842 bars, 2021-03-10..2026-03-09 (Jan25 28-31 + Aug24 28-30
source gaps disclosed, re-pull awaited). RESEARCH STATE post-correction
(#13 units bug voided the first campaign family; rows 23-28 owner-
review, row 29 clean re-issue): corrected-cost classical trend systems
= regime-dependent near-breakeven (holdout-positive/train-negative, PF
~1.01 — NOT alpha); naive XGB 1-bar = genuinely negative on favorable
holdout (-3,340.5 pts, PF 0.94 @ 5USD-side-equiv, cross-validated
across 2 runs); walk-forward bar re-derivation = prereg 41b9044
prerequisite (queued as next substantive build). Dash contract: tool-
only appends, SINGLE-QUOTED args, spell USD (shell-expansion rule).
Ledger rows=29; 334 probes; 26 STRIP-#2 gap rows + recovery arcs x3.

Integrity tally: FOURTEEN incidents (13 fabrication-class + 1
measurement-class #13; all self-caught, zero trading content) + 2
alarm-hygiene near-misses. New rules in force: in-hand probe lines
(#12), units-gate before first run (#13), complete-figure-or-reread
quoting (#14), single-quote dash args (shell rule). Runbook:
docs/RUNBOOK-sandbox-recovery.md. Verify-before-assert covers ALERTS.

First probe in this roll = 335.
- 2026-11-09T13:02:05Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=c369352 zero-byte=0/61 roll9=33
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=13:02:05Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f c369352
  quiet — probe 335 (first line, roll #9). ~61min after probe-334
  (measured from 12:01:18Z; intervening slot = maintenance
  rollover). State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER
  holds; pre-reg 41b9044 gate monitor). One entry this turn.
- 2026-11-09T13:02:05Z+ (same turn, continuation — evidence chain:
  probe output quoted COMPLETE above; then wf_classical.py run
  (units banner + worked example PASS first per #13 rule; one
  pandas kwarg crash fixed same-turn, disclosed) then FULL-JSON
  re-read before writing any figure (#14 rule) — sanctioned values
  verbatim: ma12_48 c025 mean 207.6 pts median 279.6 pct_pos 60.0;
  ma12_48 c050 mean -16.6 median 45.7 pct_pos 50.0;
  ma12_48_hyst c025 mean -16.4 median 857.8 pct_pos 60.0;
  ma12_48_hyst c050 mean -188.1 median 676.4 pct_pos 60.0;
  donchian20 c025 mean -87.7 median -578.6 pct_pos 40.0;
  donchian20 c050 mean -362.8 median -817.4 pct_pos 20.0;
  donchian1152 c025 mean -218.6 median -222.5 pct_pos 40.0;
  donchian1152 c050 mean -223.6 median -227.5 pct_pos 40.0.
  (c025 = 0.25 pts/side = 5 USD-side-equiv; c050 = double; USD =
  pts*20; windows = 10 six-month rolling-origin blocks, parameter-
  free families so every window is pure OOS. R-F-2b: no duplicate
  -> no coalesce claim; R-F-4b: clean) EXPERIMENT (queued prereq
  build, timeboxed): WALK-FORWARD BAR RE-DERIVATION, classical
  family. FINDING: the single-split flip-positive was regime-luck,
  confirmed — best cell ma12_48@c025 wins only 60 pct of windows
  (mean +207.6 pts = ~4.1k USD per 6mo window at 5USD-side-equiv,
  ~1 contract) and MEAN GOES NEGATIVE at 2x cost; donchian20
  collapses to 20 pct windows-pos at c050; 5-day donchian flat-
  negative both. ROBUST CLASSICAL BAR for 41b9044 go/no-go
  (proposed to Jeremiah): beat ma12_48@c025 on mean-window net AND
  pct_windows_pos>=60 on the SAME 10-window protocol — anything
  less is indistinguishable from trend-regime luck. dash.py row
  appended (single-quoted args). One entry this turn.
- 2026-11-09T13:30:36Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=df524fe zero-byte=0/61 roll9=74
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=13:30:36Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f df524fe
  quiet — probe 336. ~28min after probe-335 (measured from
  13:02:05Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; WF bar proposed,
  awaiting ratification + GPU). One entry this turn.
- 2026-11-09T14:00:39Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=9219887 zero-byte=0/61 roll9=87
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=14:00:39Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 9219887
  quiet — probe 337. ~30min after probe-336 (measured from
  13:30:36Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; WF bar proposed,
  awaiting ratification + GPU). One entry this turn.
- 2026-11-09T14:30:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=c35e73d zero-byte=0/61 gpu=[256 MiB venv
  python;23812 MiB llama-server] date=2026-11-09 time=14:30:38Z";
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) e4d7b7f c35e73d quiet — probe 338.
  ~30min after probe-337 (measured from 14:00:39Z) -> fresh slot.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor; WF bar proposed, awaiting ratification +
  GPU). One entry this turn.
- 2026-11-09T15:00:40Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening and
  post-#12 in-hand rule:
  "fetch-rc=0 origin/main=00bae71 zero-byte=0/61 roll9=113
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=15:00:40Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: DISCLOSED same-turn drafting slip — this turn's
  OPENING prose (out-of-ledger) pre-drafted "probe 340 / expect=
  f412860"; the probe output corrected it before any write: true
  predecessor = probe 338 @ 14:30:38Z tip 00bae71 (chain intact,
  no drift), this line is probe 339. No ledger row was ever
  written from the draft -> annotation, not retraction; third
  instance of draft-before-output class, counter incremented in
  spirit, formal count unchanged) e4d7b7f 00bae71 quiet — probe
  339. ~30min after probe-338 (measured from 14:30:38Z) -> fresh
  slot. State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) |
  gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-
  reg 41b9044 gate monitor; WF bar awaiting ratification + GPU).
  One entry this turn.
- 2026-11-09T15:30:34Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, and post-339 zero-pre-prose rule (first
  asserted content of the turn is below this line, after the probe
  returned):
  "fetch-rc=0 origin/main=199c80f zero-byte=0/61 roll9=133
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=15:30:34Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 199c80f
  quiet — probe 340. ~30min after probe-339 (measured from
  15:00:40Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; WF bar awaiting
  ratification + GPU). One entry this turn.
- 2026-11-09T15:30:34Z+ (same turn, continuation — evidence chain:
  probe output quoted COMPLETE above; then same-turn XGB walk-
  forward run under the proposed bar protocol (units banner PASS
  first per #13; all figures below appeared COMPLETE in tool
  output per #14): net_pts_per_window [-891.2, -880.8, -842.5,
  -1065.5, -389.8], mean -814.0, median -880.8, pct_windows_pos
  0.0. PROTOCOL DISCLOSED: expanding-origin (fit on everything
  strictly before each window), 6mo windows starting 2024-H1
  (first ~3y corpus consumed as initial train -> only 5 windows),
  xgb capped 120 trees for the 25-min timebox (disclosed; deeper
  models are pre-reg territory), single cost 0.25 pts/side, bands
  .55/.45 next-bar exec. VERDICT: naive XGB FAILS the proposed
  bar on both tests (mean -814.0 vs required >207.6; 0.0 pct wins
  vs required >=60) — decisively, not marginally. This is the
  FIRST test of an ML candidate against a robustness bar rather
  than a single split; the bar is doing exactly its job. Note:
  pre-reg 41b9044's spec (3 arms, v2 gate) is the properly-
  powered version of this test and remains gated on GPU + bar
  ratification. dash.py row appended (single-quoted). One entry
  this turn.
- 2026-11-09T16:00:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=af76e4f zero-byte=0/61 roll9=168
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=16:00:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f af76e4f
  quiet — probe 341. ~30min after probe-340 (measured from
  15:30:34Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; XGB-WF dry-run failed
  bar, awaiting Jeremiah ratification + GPU). One entry this turn.
- 2026-11-09T16:00:37Z+ (same turn, continuation — evidence chain:
  probe output quoted COMPLETE above; then loose-variant trend
  screen under WF protocol (units banner PASS per #13; run tail
  TRUNCATED two blocks -> NOTHING written until full json re-read
  per #14; sanctioned figures verbatim from that re-read):
  ma12_48_holdmin48 mean 522.7 median 387.2 pct_pos 63.6 turns
  9,247 nets [686.8 -986.0 -2102.0 -2429.0 1134.5 171.8 387.2
  3097.8 3170.0 -1057.0 3675.5]; vwap48_288_hyst1 mean 175.1
  median 196.5 pct_pos 63.6 turns 1,810; vwap288_1152_hyst2 mean
  36.4 median -308.0 pct_pos 36.4 turns 358. FINDING:
  ma12_48_holdmin48 MEANS BEATING the proposed bar cell (522.7 vs
  207.6) at same window-win rate (63.6 pct) — hold-minimum filter
  cuts whipsaw losses in the weak windows. CAVEATS BEFORE ANY
  CLAIM: (a) post-hoc variant family — screen is exploration,
  NOT confirmation; bar cell itself is parameter-free textbook,
  this one has a tuned knob (48); (b) bar ratification pending —
  if Jeremiah ratifies 'beat ma12_48@c025', honest follow-up =
  confirm holdmin on the PRE-REG spec's protocol not this one;
  (c) PF-equivalent not re-derived here. NO dash row for
  exploration-tier result (schema: rows are for runs with stated
  verdicts; this is a screen feeding the pre-reg decision, md-
  only is the honest tier). One entry this turn (probe slot 341
  above).
- 2026-11-09T16:30:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=ac91bcf zero-byte=0/61 roll9=204
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=16:30:37Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f ac91bcf
  quiet — probe 342. ~30min after probe-341 (measured from
  16:00:37Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor; holdmin48 screen
  candidate awaits pre-reg-protocol confirmation + Jeremiah
  ratification). One entry this turn.
- 2026-11-09T17:00:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=6d64820 zero-byte=0/61 roll9=218
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=17:00:38Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 6d64820
  quiet — probe 343. ~30min after probe-342 (measured from
  16:30:37Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). Queue external-only
  (ratification + GPU); no interim build this wake (pre-registered
  exploration budget spent; honest quiet). One entry this turn.
- 2026-11-09T17:30:36Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=59a629d zero-byte=0/61 roll9=232
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=17:30:36Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 59a629d
  quiet — probe 344. ~30min after probe-343 (measured from
  17:00:38Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). Queue external-only
  (WF-bar ratification + GPU freeing); honest quiet, no interim
  build. One entry this turn.
- 2026-11-09T18:00:55Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=0693c3a zero-byte=0/61 roll9=246
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=18:00:55Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 0693c3a
  quiet — probe 345. ~30min after probe-344 (measured from
  17:30:36Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB ->
  DEFER holds; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- 2026-11-09T18:30:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=4732533 zero-byte=0/61 roll9=259
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=18:30:38Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 4732533
  quiet — probe 346. ~30min after probe-345 (measured from
  18:00:55Z) -> fresh slot. Roll #9 at actual 259 lines < ~389 ->
  no rollover this wake (heads-up forecast 259 independently
  confirmed by this actual wc -l — forecast-vs-actual delta zero,
  rollover stays gated on actual count at wake time). State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB -> DEFER holds; pre-reg 41b9044 gate
  monitor). Queue external-only; honest quiet. One entry this turn.
- 2026-11-09T19:00:31Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=f69b8a5 zero-byte=0/61 roll9=275
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=19:00:31Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f f69b8a5
  quiet — probe 347. ~30min after probe-346 (measured from
  18:30:38Z) -> fresh slot. Roll #9 275 < ~389 -> no rollover.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor). Queue external-only; honest quiet. One
  entry this turn.
- 2026-11-09T19:33:04Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3529b5c zero-byte=0/61 roll9=289
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=19:33:04Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 3529b5c
  quiet — probe 348. ~32min after probe-347 (measured from
  19:00:31Z; wake fired ~2.5min late, drift disclosed per pattern
  — within watch thresholds, no flag). Roll #9 289 < ~389 -> no
  rollover. State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER
  holds; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- 2026-11-09T20:03:43Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=9819bda zero-byte=0/61 roll9=304
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=20:03:43Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 9819bda
  quiet — probe 349. ~31min after probe-348 (measured from
  19:33:04Z) -> fresh slot. Roll #9 304 < ~389 -> no rollover.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor). Queue external-only; honest quiet. One
  entry this turn.
- 2026-11-09T20:33:22Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=e47b088 zero-byte=0/61 roll9=318
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=20:33:22Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f e47b088
  quiet — probe 350. ~30min after probe-349 (measured from
  20:03:43Z) -> fresh slot. Roll #9 318 < ~389 -> no rollover.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor). Queue external-only; honest quiet. One
  entry this turn.
- 2026-11-09T21:00:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=b22abe1 zero-byte=0/61 roll9=332
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=21:00:38Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f b22abe1
  quiet — probe 351. ~27min after probe-350 (measured from
  20:33:22Z) -> fresh slot. Roll #9 332 < ~389 -> no rollover
  (rollover now ~4 wakes out at current line-rate). State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB -> DEFER holds; pre-reg 41b9044 gate
  monitor). Queue external-only; honest quiet. One entry this turn.
- 2026-11-09T21:30:35Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=5935a75 zero-byte=0/61 roll9=346
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=21:30:35Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 5935a75
  quiet — probe 352. ~30min after probe-351 (measured from
  21:00:38Z) -> fresh slot. Roll #9 346 < ~389 -> no rollover
  (rollover watch: ~33 lines/2 wakes recent rate -> threshold
  reached in ~2-3 wakes; gating stays on actual wc -l at wake
  time). State block: zero-byte=0/61 | raw-data AVAILABLE (61/61)
  | gpu ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds;
  pre-reg 41b9044 gate monitor). Queue external-only; honest
  quiet. One entry this turn.
- AUDIT-NOTE (same turn, post-write): probe-352 line's rollover
  forecast said "~33 lines/2 wakes"; actual from this + prior probe
  outputs (318->332->346) = 28 lines/2 wakes (14/wake) -> threshold
  ETA ~3 wakes, inside the stated ~2-3 hedge. Derived-stat misquote
  self-caught; forecast was hedged and gating is actual wc -l so no
  claim affected; corrected here for the record.
- 2026-11-09T22:00:36Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=f9a608c zero-byte=0/61 roll9=368
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-09
  time=22:00:36Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f f9a608c
  quiet — probe 353. ~30min after probe-352 (measured from
  21:30:35Z) -> fresh slot. Roll #9 368 < ~389 -> no rollover this
  wake; next wake likely maintenance rollover (~21 lines to
  threshold at recent rate; actual wc -l at wake time governs).
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor). Queue external-only; honest quiet. One
  entry this turn.
