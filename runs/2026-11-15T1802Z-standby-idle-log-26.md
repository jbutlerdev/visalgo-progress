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
- 2026-11-15T19:01:00Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=7036299 zero-byte=0/61 roll26=84
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=19:01:00Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23 watch: gaps by explicit
  subtraction w/ anchor labels) e4d7b7f 7036299 — probe 614 +
  REAL INCREMENT. 23m55s after probe-613 (19:01:00 - 18:37:05 =
  23m55s, subtracted; no probe-less wake since, single anchor) ->
  fresh slot. Probe number from records (613+1). roll26=84 =
  stat-consistent (49 + probe-613's +31 +4 net incident-23
  block). INCREMENT (post-campaign menu): MONTH-SET IDENTITY —
  the 61 ym-keys of continuity.front_sequence, manifest.rows,
  QA_TABLE rows and bars/ filenames compared as SETS: **all four
  identical, 61 each, zero symmetric difference**. This is the
  set-level companion to probe-602's sum-level chain (equal
  totals did not logically preclude, e.g., one month swapped —
  now ruled out at key level; every per-month field tie in
  588-613 sits on this shared key set). CPU-bound (fast).
  visalgo sync current: master ed065c9. State block: zero-byte=
  0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound
  DEFER only; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- 2026-11-15T19:30:44Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=ba597b2 zero-byte=0/61 roll26=111
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=19:30:44Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23 watch: gaps by explicit
  subtraction w/ anchor labels) e4d7b7f ba597b2 — probe 615 +
  REAL INCREMENT. 29m44s after probe-614 (19:30:44 - 19:01:00 =
  29m44s, subtracted; single anchor — no probe-less wake since) ->
  fresh slot. Probe number from records (614+1). roll26=111 =
  stat-consistent (84 + probe-614's +27). INCREMENT (post-campaign
  menu): ZSTD FRAME-FLAGS + CHECKSUM-DECLARATION AUDIT — parsed
  every raw file's frame header: magic b28b52ffd OK 61/61 AND
  **all 61 declare the FContent_Checksum flag** (xxhash content
  checksum present in every frame — the files self-certify
  integrity, deepening probe-577's magic-only look and probe-
  609's decode pass: python-zstandard verifies that checksum on
  stream end, so 609's zero-error result already implied checksum
  validation — this wake establishes the flag was actually set,
  i.e. the verification was real, not vacuously skipped).
  CPU-bound (fast). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
- 2026-11-15T20:00:54Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=461ee05 zero-byte=0/61 roll26=139
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=20:00:54Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23 watch: gaps by explicit
  subtraction w/ anchor labels) e4d7b7f 461ee05 — probe 616 +
  REAL INCREMENT (partial, honestly scoped). 30m10s after probe-
  615 (20:00:54 - 19:30:44 = 30m10s, subtracted; single anchor —
  no probe-less wake since) -> fresh slot. Probe number from
  records (615+1). roll26=139 = stat-consistent (111 + probe-
  615's +28). INCREMENT (post-campaign menu): BUILD-ORDERING
  TEMPORAL PROVENANCE — draft-1 assumed built_utc on all 5 QA
  artifacts -> KeyError-class crash on the two that lack it
  (disclosed; structure re-inspected before any claim). Result
  on the 3 that carry built_utc: manifest 14:51:42Z < throughput
  16:34:45Z < sessions 17:01:03Z (all 2026-11-13) — **PASS for
  the timestamps that exist**: manifest first, derived after,
  ~2h09m campaign span, no inversions. SCOPE LIMIT recorded:
  sanity.json + continuity.json carry NO timestamp field — their
  build-order cannot be timestamp-verified (structural fact of
  the artifacts, not a defect; noted for completeness so future
  readers don't assume 5-way temporal proof). CPU-bound (fast).
  visalgo sync current: master ed065c9. State block: zero-byte=
  0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound
  DEFER only; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- 2026-11-15T20:31:06Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=2faa442 zero-byte=0/61 roll26=170
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=20:31:06Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23 watch: gaps by explicit
  subtraction w/ anchor labels) e4d7b7f 2faa442 — probe 617 +
  REAL INCREMENT (weak-positive, honestly scoped). 30m12s after
  probe-616 (20:31:06 - 20:00:54 = 30m12s, subtracted; single
  anchor — no probe-less wake since) -> fresh slot. Probe number
  from records (616+1). roll26=170 = stat-consistent (139 +
  probe-616's +31). INCREMENT (post-campaign menu): PARQUET
  WRITER-PROVENANCE SWEEP — KeyValueMetadata inspected on all 61
  published parquets: **uniform ABSENCE of created_by (and all
  kv metadata) across 61/61**. Disclosed twice over: (a) draft-1
  crashed on my wrong assumption that metadata is bytes (it's
  dict-like) — no claim made; (b) the PASS is WEAK-POSITIVE:
  uniformity of absence is consistent w/ single-build origin but
  proves little alone (writer sigs just weren't embedded; no
  over-reading, unlike my 'created_by uniform -> single writer'
  draft wording which I caught pre-record as over-interpretation
  of absent data). Recorded for completeness of the physical-
  layer audit trail. CPU-bound (fast). visalgo sync current:
  master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-15T21:00:43Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=e83f10c zero-byte=0/61 roll26=201
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=21:00:43Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23 watch: gaps by explicit
  subtraction w/ anchor labels) e4d7b7f e83f10c — probe 618 +
  REAL INCREMENT. 29m37s after probe-617 (21:00:43 - 20:31:06 =
  29m37s, subtracted; single anchor — no probe-less wake since) ->
  fresh slot. Probe number from records (617+1). roll26=201 =
  stat-consistent (170 + probe-617's +31). INCREMENT (post-
  campaign menu): QA_TABLE zstd/dbn FLAG COLUMNS <-> MANIFEST
  MAGIC BOOLEANS — all 61 table (zstd=Y, dbn=Y) pairs ==
  manifest zstd_magic/dbn_magic **exactly, 0 mismatched** (every
  manifest boolean True, hence every table cell Y). Table<->
  manifest flag edge closes the last untested human-readable
  column pair; the physical truth behind the flags was
  independently established @577 (magic bytes), @592 (manifest
  bytes vs disk) and @615 (frame-flags + checksum declaration).
  CPU-bound (fast). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
