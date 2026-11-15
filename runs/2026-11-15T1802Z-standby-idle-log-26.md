# STANDBY IDLE LOG — ROLL #26 (opened 2026-11-15T18:02:24Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 612) per post-#8 machine-sourcing rule:

- 2026-11-15T17:30:58Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=2eb6857 zero-byte=0/61 roll25=376
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=17:30:58Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22 watch: gap by explicit
  subtraction) e4d7b7f 2eb6857 — probe 612 + REAL INCREMENT
  (FINDING-CLASS, first of the campaign). 29m58s after probe-611
  (17:30:58 - 17:01:00 = 29m58s, subtracted) -> fresh slot. Probe
  number from records (611+1). roll25=376 = stat-consistent (348
  + probe-611's +28). INCREMENT: GLOBAL-MAX-GAP CHECK (gap sweep
  incl. all 60 file boundaries) -> **320.58h** boundary gap
  (2025-12-19 14:25Z -> 2026-01-01 23:00Z), NOT the 73.1h
  CORPUS_SUMMARY claims. Investigation chain (machine-sourced,
  no premature claim): (a) bars/manifest/QA_TABLE all agree
  202512 last=2025-12-19 14:25:00Z, 4,031 bars, 3,899,641 trades
  (consistent, PASS-marked); (b) 7 weekday sessions absent
  (12-22/23/24/26/29/30/31); (c) DECISIVE raw-side decode of
  glbx-mdp3-20251201-20251231: 7,232,079 records thru
  2025-12-31 21:59:59Z — **1,573,145 records AFTER the cutoff,
  99.8% NQH6** (Mar-26, the post-roll contract), only 49 NQZ5.
  ROOT CAUSE = documented decoder semantic (front = WHOLE-FILE
  volume argmax, nq_ticks_load.py @e4d7b7f): NQZ5 won the
  whole-file argmax, so post-roll NQH6 trades are dropped by
  design -> 202512 published bars end at the roll; re-derivation
  campaign reproduced it (same VERBATIM decoder). VERDICT: NOT
  data loss (raw intact & complete per 609 decode sweep), NOT
  inconsistency (all artifacts agree), BUT **CORPUS_SUMMARY
  "max true gap 73.1h" is a mis-scoped claim** — grid_check_v2
  top_gaps was computed WITHIN months, missing cross-file
  boundaries; legacy v1 gap_hours_max=320.583 was the accurate
  global figure (probe-578's "v2 is the record" note REFINED:
  v2=within-month scope; v1=global incl boundaries). OPEN ITEM
  for freeze: summary line 12 needs "73.1h within-month max;
  320.6h global max = documented Dec-25 roll-cutoff semantic";
  downstream: 5-min bars 2025-12-22..31 absent BY DESIGN — do
  not treat as hole. CPU-bound (fast). visalgo sync current:
  master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-15T18:37:05Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=1ce8fd0 zero-byte=0/61 roll26=49
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=18:37:05Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22 watch: gap by explicit
  subtraction) e4d7b7f 1ce8fd0 — probe 613 + REAL INCREMENT.
  1h06m07s after probe-612 (18:37:05 - 17:30:58 = 1h06m07s) and
  34m41s after the probe-less rollover-25->26 exec wake
  (18:37:05 - 18:02:24 = 34m41s; both anchors quoted per #19
  lesson; INCIDENT #23 measurement-class self-caught in post-write
  audit: first draft labeled 34m41s as 'after probe-612' — that
  value belongs to the exec-wake anchor, exec wake consumed no
  probe so probe-anchor gap is 1h06m07s; anchor mix-up corrected
  by explicit dual subtraction) -> fresh slot. Probe number from records (612+1). roll26=49 =
  stat-consistent (rollover open committed at 49 lines, +0 since).
  INCREMENT (post-campaign menu): INTRA-MONTH GAP VALUES <->
  PHYSICAL INDEX — max consecutive-bar gap recomputed per file
  from published indices: all claimed grid_check_v2 top months
  (202112/202204/202212/202312 @ 73.1h) **reproduced exactly**,
  physical per-file max also 73.1h (raw 73.08h == 73.1 at the
  artifact's own 1-decimal rounding convention; initial 'DIFF'
  was MY tolerance being stricter than the artifact's precision —
  disclosed, no claim made from it). Completes the gap story
  opened by probe-612: claimed intra-month max IS the true max
  over all 61 files (no month exceeds it); the 320.58h global
  figure stands as the cross-boundary roll-cutoff finding.
  CPU-bound (fast). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
