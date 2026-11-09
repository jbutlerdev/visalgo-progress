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
