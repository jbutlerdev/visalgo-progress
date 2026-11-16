# STANDBY IDLE LOG — ROLL #27 (opened 2026-11-16T00:04:30Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 623, lines 367-397 of roll #26 file; sed-extracted this wake, head/tail grep-anchored: line 367 == '- 2026-11-15T23:30:40Z (...', line 397 == '...One entry this turn.'; /tmp extract lost to sandbox wipe and REBUILT same wake — disclosed, post-#8 machine-sourcing rule):

- 2026-11-15T23:30:40Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=414bddf zero-byte=0/61 roll26=366
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-15
  time=23:30:40Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gaps by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT — 29m52s after
  probe-622 (23:30:40 - 23:00:48 = 0:29:52 per python datetime
  tool call, copied verbatim per incident-24 mitigation; single
  anchor — no probe-less wake since) -> fresh slot. Probe number
  from records (622+1). roll26=366 = stat-consistent (329 +
  probe-622's +37). INCREMENT (post-campaign menu): SESSIONS
  FULL RECOMPUTE — sessions.json years dict re-derived from
  scratch off the published bars (per-bar UTC-hour band split
  13<=h<21 per the artifact's own documented coarse-UTC
  semantics, day-sets via date()): **all 6 fields x 6 years
  (bars/rth_bars/overnight_bars/days_with_rth/days_with_overnight
  /overnight_share_pct) match EXACTLY, 0 mismatched**. Strongest
  sessions leg of the campaign: 594 verified the share formula
  internally, 600 the cross-artifact consistency — this is full
  independent recompute from the physical bars. CPU-bound
  (~3min, all 61 files read). visalgo sync current: master
  ed065c9. State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB PERMANENT
  herd infra — GPU-bound DEFER only; pre-reg 41b9044 gate
  monitor). ROLLOVER WATCH: roll26=366, gate ~380 -> next wake
  likely executes roll 26->27 (full checklist armed). Queue
  external-only; honest quiet. One entry this turn.

ROLL #27 carried-state (from roll #26 freeze, machine-sourced): probes 613-623 on #26 (probe-623 token omission disclosed there); incidents standing 24 (in-file #23,#24); OPEN QUESTIONS: (1) throughput median 281,949 UNRESOLVED (do NOT re-attempt w/o build-side semantics); (2) GAP FINDING global max 320.58h cross-boundary w/ CORPUS_SUMMARY line-12 'max true gap 73.1h' MIS-SCOPED (intra-month figure; fix proposed, awaiting Jeremiah authorization). STANDBY day 17, floors held: .61 read-only, no Simulation toggle, TLS ON, dash tool-only, pins never in repo files. GPU-bound DEFER only (llama-server permanent on .146); pre-reg 41b9044 gate monitor.

TIMER STATE: rollover-27 backstop timer_emwi5cd62_c3l9jm (armed
2026-11-15T21:3xZ for 00:11Z) now OBSOLETE — exec happened 00:01-
00:06Z this wake (pre-timer). Its 00:11Z fire -> NOTE-ONLY STAND-
DOWN (one-timer rule; roll #27 already open; no writes/probes on
that wake). Next backstop armed this wake for roll 27->28.
- 2026-11-16T00:31:05Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=fb72374 zero-byte=0/61 roll27=43
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-16
  time=00:31:05Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gaps by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT, DUAL-ANCHORED
  per #23 lesson — 1h00m25s after probe-623 (23:30:40Z Nov-15 ->
  00:31:05Z Nov-16 = 1:00:25 per python datetime, copied verbatim;
  two probe-less wakes intervened: rollover-exec 00:01-00:07Z +
  stand-down 00:11Z) AND 26m35s after the roll-#27-open exec wake
  (00:04:30 -> 00:31:05, subtracted) -> fresh slot. Probe number
  from records (623+1). roll27=43 = stat-consistent (37 + timer-
  note +6, both committed on open wake). FIRST PROBE ON ROLL #27.
  INCREMENT (post-campaign menu): GLOBAL TIMESTAMP UNIQUENESS —
  all 337,922 ts_recv values across all 61 files counted:
  **distinct == total, 0 duplicated timestamps** — no 5m bar ts
  appears in >1 row corpus-wide; cross-file boundary overlap
  ruled out at VALUE level (complements probe-574's overlapping_
  months=0 doc-level claim + probe-607's ordering proof; dup
  within-file already covered @574 dup_within_month, this adds
  the cross-file value-level leg). CPU-bound (~3min). visalgo
  sync current: master ed065c9. State block: zero-byte=0/61 |
  raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server
  23,812 MiB PERMANENT herd infra — GPU-bound DEFER only;
  pre-reg 41b9044 gate monitor). Queue external-only; honest
  quiet. One entry this turn.
- 2026-11-16T01:01:10Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3012c8d zero-byte=0/61 roll27=73
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-16
  time=01:01:10Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gap by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT — 30m05s after
  probe-624 (01:01:10 - 00:31:05 = 0:30:05 per python datetime,
  copied verbatim; single anchor — no probe-less wake since;
  prior-wake disclosure honored: secondary anchors machine-sourced
  henceforth) -> fresh slot. Probe number from records (624+1).
  roll27=73 = stat-consistent (43 + probe-624's +30). INCREMENT
  (post-campaign menu): BAR-CLOCK-ALIGNMENT (value-level) — all
  337,922 ts_recv: minute divisible by 5, second==0, microsecond
  ==0, single signature after full re-count -> **PASS**. Draft-1
  predicate bug disclosed pre-claim: I wrote minute==0 (hour-top
  only) -> OFF-GRID false-negative on first run; inspect showed
  12 evenly-spread buckets (all sec/usec 0) -> corrected to
  minute%5==0; per policy predicate bugs self-handled pre-claim
  are not incidents. NEW EDGE: probe-575 checked grid-alignment
  per-file on indices; this is the value-level corpus-wide re-
  count incl second/microsecond. CPU-bound (~3min). visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 |
  raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server
  23,812 MiB PERMANENT herd infra — GPU-bound DEFER only;
  pre-reg 41b9044 gate monitor). Queue external-only; honest
  quiet. One entry this turn.
- 2026-11-16T01:31:02Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=2463e49 zero-byte=0/61 roll27=103
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-16
  time=01:31:02Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gap by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT — 29m52s after
  probe-625 (01:31:02 - 01:01:10 = 0:29:52 per python datetime,
  copied verbatim; single anchor — no probe-less wake since) ->
  fresh slot. Probe number from records (625+1). roll27=103 =
  stat-consistent (73 + probe-625's +30). INCREMENT (post-campaign
  menu): BARS-DATES <-> SESSIONS DAY-SETS — per-year distinct
  UTC-date sets recomputed from bars split by the documented RTH
  band, compared to sessions.json day counts: **all 6 years match
  exactly (0 mismatched)**; overnight-only day totals also
  recomputed (weekend/holiday overnight-only days exist as
  expected for a ~23h product). Adds SET-level date identity +
  overnight-only accounting to probe-623's numeric recompute.
  CPU-bound (~3min). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
  [PROVENANCE NOTE probe-626, same wake post-write: the recorded
  "strictly superset" phrasing went beyond the gated assertion
  (gate covered counts only). Verified directly after the write:
  rth_only_days=0 measured -> overnight day-sets ⊇ rth day-sets
  per year; claim stands, but flagged as claim-precedes-measure
  (process deviation #24-family, no false content — corrected
  within-wake per #16/#18 honesty policy; next time gate the
  output on EVERY asserted clause).]
- 2026-11-16T02:00:45Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=fa15a0f zero-byte=0/61 roll27=137
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-16
  time=02:00:45Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gap by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT — 29m43s after
  probe-626 (02:00:45 - 01:31:02 = 0:29:43 per python datetime,
  copied verbatim; single anchor — no probe-less wake since) ->
  fresh slot. Probe number from records (626+1). roll27=137 =
  stat-consistent (103 + probe-626's +26 +8 note = 137).
  INCREMENT (post-campaign menu): EXHAUSTIVE WITHIN-MONTH GAP
  CLASSIFICATION — all 337,861 consecutive-pair diffs (=337,922
  -61, arithmetic tie-in ✓): **every diff a whole multiple of
  5min (0 off-grid)**; 333,915 exactly 300s, 3,946 session gaps
  (classes: 2,694 sub-1h overnight edges, 981 ~1h, 226 2-day,
  33 5h — holiday/weekend spans, all plausible; every clause
  gated on printed output per probe-626 mitigation). Completes
  the gap story: 574 doc-level, 607 ordering, 612/613 max-gap
  anchors, 613 intra-month values, now every-pair classification.
  CPU-bound (~3min). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
  [PROVENANCE NOTE probe-627, same wake post-write: the gap-class
  list in the entry is the TOP-4 of a longer Counter (2694+981+
  226+33 = 3,934 of 3,946 non-300s pairs); 12 pairs sit in smaller
  unlisted classes — all still 5min-multiples per the gated
  off_multiple=0 check. Claim as gated (0 off-grid) unaffected;
  listing was illustrative, now explicitly marked top-4.]
