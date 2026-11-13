# STANDBY IDLE LOG — ROLL #18 (opened 2026-11-13T15:32:40Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 520) per post-#8 machine-sourcing rule:

- 2026-11-13T15:02:06Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=fb17c90 zero-byte=0/61 roll17=374
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=15:02:06Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f fb17c90 — probe 520 +
  REAL INCREMENT (Jeremiah standing directive: every wake lands
  one real increment beyond probe). ~118min after probe-519
  (measured from 13:13:44Z; intervening wake = timer 1432Z
  note-only stand-down, no write, consumed no probe) -> fresh
  slot. INCREMENT (corpus continuity audit, follow-on to probe-519
  campaign): all 61 per-month parquets re-read and audited — (1)
  duplicate bars within month: 0; (2) cross-month overlapping
  timestamps: none (61/61 disjoint); (3) bars total == unique:
  337,922 == 337,922 (no collapse/loss); (4) grid: every step a
  multiple of 5min — 0 off-grid months (first-pass 'non-5min-
  step' flag on all 61 was MY check defect: strict
  diff==5min rule ignores legitimate session gaps; corrected to
  modulo rule, caught pre-commit, nothing false pushed); (5)
  merged-index 'max-gap 320.6h' from same defective first pass
  was unsorted-append artifact — per-month recheck gives true
  max 73.1h = Dec 23 21:55 -> Dec 26 23:00 (Christmas closure,
  legitimate; same 73.1h in Apr/Dec = Good Friday/Christmas);
  (6) front-month roll sequence: 19 clean quarterly transitions
  NQM1->NQU1->...->NQH6, no skips/backward rolls. Verdict GAPS_OK.
  Artifact: runs/data/corpus-2021-2026/continuity.json. CPU-bound,
  no GPU dependency (per Jeremiah rule correction). roll17=374 =
  stat-consistent (334 + probe-519's +40). Post-write ~400+ ->
  NEXT wake reads >=380 -> rollover #18 executes (checklist
  armed; timer fired early 1432Z, still-armed checklist governs).
  visalgo sync current: master ed065c9. State block: zero-byte=0/
  61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-
  server 23,812 MiB -> GPU-bound DEFER holds, CPU work cleared;
  pre-reg 41b9044 gate monitor). Queue external-only; honest
  quiet. One entry this turn.

Roll #17 frozen same turn (see FINAL STATE banner in runs/2026-11-13T0331Z-standby-idle-log-17.md).
- 2026-11-13T16:00:39Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=316bdf3 zero-byte=0/61 roll18=45
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=16:00:39Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f 316bdf3 — probe 521
  (first probe line, roll #18) + REAL INCREMENT (Jeremiah standing
  directive). ~28min after probe-520 (measured from 15:02:06Z
  minus the maintenance-only rollover wake 1532Z in between,
  which consumed no probe) -> fresh slot. roll18=45 = stat-
  consistent (open +45, wrap-agnostic sed anchor, pre-commit
  head/tail check pass). INCREMENT (corpus sanity audit #2 —
  price/volume/OHLC integrity per month, queued at roll-17 close):
  all 61 per-month parquets re-read; per-bar checks: high>=low,
  high>=open/close, low<=open/close, volume>0, n>0; per-month
  price plausibility band (5000 < min-low, max-high < 35000, all
  lows > 0). RESULTS: 0 bad-px months, 0 bad-vol months, 0 bad-
  OHLC months; global NQ range across corpus 10,484.75 -> 26,399
  — matches real NQ (March-2021 low ~10.5k, early-2026 high
  ~26.4k): SANITY_OK. Artifact: runs/data/corpus-2021-2026/
  sanity.json. CPU-bound, no GPU dependency. visalgo sync current:
  master ed065c9. State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB PERMANENT
  herd infra — GPU-bound DEFER only; pre-reg 41b9044 gate
  monitor). Queue external-only; honest quiet. One entry this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-521 line above states "~28min after probe-520
  ... measured from 15:02:06Z" — WRONG. Arithmetic from the cited
  ts: 16:00:39Z - 15:02:06Z = 58m33s. The ~28min figure actually
  measured since the intervening maintenance-only rollover wake
  (1532Z, wrote files, consumed no probe). Correct statement:
  probe-521 is ~59min after probe-520, with the probe-free
  rollover wake between them. Numbering unaffected (521 stands;
  probe-heredoc 1 <= probe-call 1). No fabrication: ts values and
  all quoted outputs genuine; defect = gap mislabel.
- 2026-11-13T16:33:42Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=6e37317 zero-byte=0/61 roll18=84
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=16:33:42Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f 6e37317 — probe 522 +
  REAL INCREMENT (Jeremiah standing directive). ~33min after
  probe-521 (measured from 16:00:39Z; wake fired ~3min late,
  within watch thresholds, disclosed per drift pattern) -> fresh
  slot. roll18=84 = stat-consistent (74 + probe-521's +10
  correction; wc 84 verified last wake). INCREMENT (corpus
  throughput audit #3, queued probe-521): per-month front-month
  trade-count vs distinct UTC trading days AND raw compressed
  bytes-per-trade (decoder throughput sanity). RESULTS: median
  281,949 trades/day, range 137,334 (early 2021) -> 458,017
  (2025-26) — monotone-ish growth, no month < 1/4x or > 4x
  median (outliers: none); raw bytes/trade 16.34 -> 32.93 across
  all 61 (tight for zstd stream variance; no month implausibly
  sparse -> no silent truncation signature). Verdict
  THROUGHPUT_OK. Artifact: runs/data/corpus-2021-2026/
  throughput.json. CPU-bound, no GPU dependency. visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-13T17:00:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=ab1d0a1 zero-byte=0/61 roll18=114
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=17:00:37Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f ab1d0a1 — probe 523 +
  REAL INCREMENT (Jeremiah standing directive). ~27min after
  probe-522 (measured from 16:33:42Z) -> fresh slot. roll18=114 =
  stat-consistent (84 + probe-522's +30). INCREMENT (corpus
  session-coverage audit #4 — FINAL QA leg, queued probe-522):
  per-year session split over all 337,922 bars, coarse-UTC bands
  (13-21h ~ RTH incl DST span). RESULTS: 2021 (partial, Mar-):
  56,671 bars / 65.3% overnight / 212 RTH-days; 2022: 69,762 /
  65.1 / 258; 2023: 69,550 / 65.1 / 258; 2024: 65,908 / 65.4 /
  245; 2025: 63,131 / 65.5 / 235; 2026 (to Mar-9): 12,900 / 65.6
  / 47. Overnight share flat 65.1-65.6% all six years — matches
  the 23h-Globex expectation (8h RTH of 23h = 34.8%, overnight
  65.2%) within DST band error; RTH-day counts = exchange
  trading-day counts per year; NO year shows session dropout.
  VERDICT: sessions COMPLETE + UNIFORM -> **CORPUS QA SUITE 4/4
  GREEN: QA(magic/bytes) PASS, continuity GAPS_OK, sanity
  SANITY_OK, throughput THROUGHPUT_OK, sessions uniform** —
  corpus signed-off for downstream WF/ML use. Artifact: runs/
  data/corpus-2021-2026/sessions.json. CPU-bound. visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-13T17:33:56Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=9d8a268 zero-byte=0/61 roll18=147
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=17:33:56Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f 9d8a268 — probe 524 +
  REAL INCREMENT (Jeremiah standing directive; new lane opened on
  signed-off corpus per last wake's plan). ~33min after probe-523
  (measured from 17:00:37Z; wake ~3min late, within watch band) ->
  fresh slot. roll18=147 = stat-consistent (114 + probe-523's
  +33). INCREMENT: FIRST-TOUCH 5-MIN BASELINE on signed-off
  corpus — signal sign(last-5m-bar log-return), outcome fwd
  close-to-close index points at h={1,12,48,288} bars (5m/1h/4h/
  1d), after_up vs after_dn, n ~1.6M decisions total. OVERALL
  (mean fwd pts): h1: after_dn +0.124 / after_up -0.067 (tick-
  scale mean-reversion tilt, ~|8| pts noise); h12: +0.37/+0.24;
  h48: +1.40/+0.97; h288: +8.10/+6.56 (long-horizon upward drift
  dominates, as expected unlevered NQ 2021-26). Reading: at
  5-min scale the edge is REVERSION-flavored (down-bars recover,
  up-bars give back) — consistent direction with our reversion-
  family hypotheses; magnitudes far below spread+slippage at h1
  (|mean| 0.12 vs ~0.5+ pt half-spread NQ) so raw signal needs
  the usual conditioning, NOT tradeable standalone. CAVEATS (in
  artifact): raw pts no costs; overlapping fwd returns auto-
  correlated (no correction yet); front-month splices unadjusted
  at rolls (roll-boundary fwd pts contaminated — flagged for
  roll-exclusion pass). First script defect self-caught pre-push:
  pandas Series.sign -> np.sign wrap (AttributeError); cosmetic
  'hh' double-prefix in overall keys after fix, values verified
  correct. Artifact: runs/data/corpus-2021-2026/
  baseline_first_touch.json. CPU-bound. visalgo sync current:
  master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-13T18:01:49Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=dc73189 zero-byte=0/61 roll18=187
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=18:01:49Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f dc73189 — probe 525 +
  REAL INCREMENT. ~28min after probe-524 (measured from 17:33:56Z)
  -> fresh slot. roll18=187 = stat-consistent (147 + probe-524's
  +40). INCREMENT (baseline refinement, queued probe-524):
  first-touch re-run RTH-ONLY (13:30-20:00Z coarse band) with
  last-288-bars-of-file trim (roll/liquidity-transition buffer).
  n ~310k decisions. OVERALL mean fwd pts (dn/up): h1 +0.272/
  -0.122; h12 +0.913/+0.776; h48 +4.762/+4.457; h288 +24.762/
  +21.887. vs full-sample baseline: levels roughly double (RTH
  is the volatile session, as expected), but the REVERSION
  ASYMMETRY (dn-minus-up gap) strengthens at h1: +0.394 RTH vs
  +0.191 full-sample — i.e. the 5m reversion tilt is
  disproportionately an RTH-hours phenomenon, consistent with
  session-hour fade/re-entry behavior in our hypothesis family.
  h288 upward drift also dominates RTH (post-2021 NQ long bias).
  Same caveats: raw pts no costs, overlap autocorr uncorrected,
  RTH band coarse vs DST, trim = heuristic 288-bar buffer.
  Artifact: runs/data/corpus-2021-2026/
  baseline_first_touch_rth_trim.json. CPU-bound. visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-525 line states "n ~310k decisions" — sum of
  the eight cited n's is 293,033 (~293k). Correct statement:
  ~293k decisions. All cited per-cell values themselves genuine
  (this turn's output); defect = summary-count mislabel only.
- 2026-11-13T18:30:39Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=d8f3ecf zero-byte=0/61 roll18=225
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-13
  time=18:30:39Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  heredoc one cycle then close) e4d7b7f d8f3ecf — probe 526 +
  REAL INCREMENT. ~29min after probe-525 (measured from 18:01:49Z)
  -> fresh slot. roll18=225 = stat-consistent (220 + probe-525's
  correction +5; wc 225 verified last wake). INCREMENT (hour-of-
  day localization of the h1 reversion asymmetry, queued
  probe-525): RTH-band h1 dn-up gap by UTC hour bucket, n ~65k
  decisions. PROFILE (gap = mean fwd|dn - mean fwd|up, pts): UTC
  13 (open): -0.623 -> MOMENTUM-flavored at the open (up-bars
  follow through, dn-bars keep sliding); UTC 14: -0.188 (open
  regime decaying); UTC 15 (10:00 ET): +0.694 STRONGEST full-hour
  REVERSION; UTC 16: +0.370; UTC 17: -0.199 (midday lull, weak
  momentum); UTC 18 (13:00 ET): +0.659 reversion; UTC 19: +0.392;
  UTC 20 bucket: +2.972 BUT n=570/569 (band edge only 20:00-05
  bars, boundary artifact — flagged, not actionable). READING:
  two-regime day — open hour momentum, mid-morning+afternoon
  reversion, matching our fade/re-entry family's premise (fade
  window ~UTC 15-19 minus the 17 lull). CAVEATS: raw pts no
  costs, autocorr uncorrected, t-stats pending (per-hour n ~7k
  with mean_abs ~14 pts -> se ~0.16, so UTC-15 gap 0.694 ~ 4.3
  se — nominally significant, autocorr caveat stands). Two
  script defects self-caught pre-push (float-on-Series;
  dict-minus-dict), third run produced clean output. Artifact:
  runs/data/corpus-2021-2026/baseline_h1_hourofday.json.
  CPU-bound. visalgo sync current: master ed065c9. State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound DEFER
  only; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-526 line contains two label defects — (1) "n
  ~65k decisions": sum of the sixteen cited per-hour n's = 95,994
  (~96k); correct statement ~96k. (2) "UTC-15 gap 0.694 ~ 4.3 se"
  used single-cell se (~0.167); the dn-minus-UP gap se combines
  two cells -> sqrt(2)x0.167 ~ 0.236, so 0.694/0.236 ~ 2.9 se —
  nominally significant but weaker than first stated. All cited
  per-cell values genuine (this turn's output); defects = derived
  label math, corrected here; autocorr caveat unchanged.
