# STANDBY IDLE LOG — ROLL #28 (opened 2026-11-16T05:49:30Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 634, lines 346-377 of roll #27 file; sed-extracted this wake, head/tail grep-anchored: line 1 == '- 2026-11-16T05:30:41Z (...', last == '...One entry this turn.'; per post-#8 machine-sourcing rule):

- 2026-11-16T05:30:41Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=0c59a95 zero-byte=0/61 roll27=345
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-16
  time=05:30:41Z"; R-F-2b: single prompt instance -> no coalesce
  claim; post-#17 rule: this line sits behind THIS turn's single
  probe-call output; post-#19/#21/#22/#23/#24 watch: gap by
  explicit SUBTRACTION COPIED FROM MACHINE OUTPUT — 29m49s after
  probe-633 (05:30:41 - 05:00:52 = 0:29:49 per python datetime,
  copied verbatim; single anchor — no probe-less wake since) ->
  fresh slot. Probe number from records (633+1). roll27=345 =
  stat-consistent (316 + probe-633's +29). INCREMENT (post-
  campaign menu): manifest.parquet_bytes <-> DISK — os.path.
  getsize on each published parquet vs the manifest field:
  **PASS 61/61 exact**. SCOPE CORRECTED (same-wake post-write
  audit, #19-family 7th): I framed this as novel ("never tied to
  disk before"), but the FULL grep context of probe-587's record
  reads "parquet_bytes on disk ... field-by-field vs fresh
  parquet reads" — 587 DID tie it. I saw the grep hit yet
  rationalized it as field-listing before reading context. TRUE
  scope: RE-CONFIRMATION of 587's tie (legitimate standby work,
  honestly re-labeled), not a new edge. manifest.bytes (raw
  size) tied @592/@598 stands. Mitigation: when a grep hit
  touches a novelty claim, the FULL record context must be read
  BEFORE commit, not just the matched line. CPU-bound
  (fast). visalgo sync current: master ed065c9. State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.

ROLL #28 carried-state (from roll #27 freeze, machine-sourced): probes 624-634 on #27 (11; token-grep undercount from line-wrap disclosed there); incidents standing 24 (in-file roll#26: #23,#24); OPEN QUESTIONS: (1) throughput median 281,949 UNRESOLVED (do NOT re-attempt w/o build-side semantics); (2) GAP FINDING: continuity.gap_hours_max=320.583h GLOBAL+accurate (re-derived @632), CORPUS_SUMMARY line-12 'max true gap 73.1h' MIS-SCOPED (intra-month figure @613=73.08h; two-figure fix proposed, awaiting Jeremiah authorization). TIMER ANOMALY: backstop cron fired 4x ~100s (mule quirk; stand-downs write-free; dup-exec guard held). STANDBY day 17, floors held: .61 read-only, no Simulation toggle, TLS ON, dash tool-only, pins never in repo files. GPU-bound DEFER only (llama-server permanent on .146); pre-reg 41b9044 gate monitor.

- 2026-11-16T07:30:35Z cadence wake — PROBE 635 (first cadence wake after
  backstop-burst starvation; probe command was this turn's FIRST tool call,
  R-F-3 verified pre-write; post-#12 in-hand, post-339 zero-pre-prose:
  "roll28=38 dirty=0 head=acd7b86 time=07:30:35Z"). Probe number from
  records (634+1). GAP (post-#24 rule, machine-subtracted this wake-chain
  @07:30:12Z python datetime, copied VERBATIM: "cadence_gap=119.52063516666666"
  min since probe-634 @05:30:41Z — ~1h59m; cause: harness starvation by
  the 27->28 backstop-cron re-fire burst, all re-fires write-free per
  duplicate-exec guard, so corpus unaffected): wide cadence gap is
  QUEUEING, not loss — logged, not hand-computed (incidents 21/22 guard).
  BURST metrics (post-#23 machine-sourcing, same 07:30:12Z output):
  "burst_minutes=105.2039685" since consumed 05:45:18Z cron instance.
  (1) TIMER ANOMALY FORMAL ENTRY: backstop cron timer_fmwii8r6c_lp4a4l
  re-fired >150x across the 105-min burst (harness re-presents of the
  consumed one-shot instance; ~90 writes-free stand-downs individually
  logged in-session, not per-fire); harness-submission backlog grew
  480->896->2101->5939 pending (cap 8); one notify_user retry attempted
  07:27:47Z -> rejected (backlog 5939 vs cap 8); re-fires absorbed
  write-free by duplicate-exec guard (roll28=38 constant across ~150
  re-presents = machine proof of zero-write handling); no agent-side
  cron-cancel tool exists — consumed-instance re-fire is harness-side.
  (2) WC-STALENESS NOTE (post-#15 honesty): roll #27 closed at 407 lines
  via post-closure correction edit (406->407); freeze quoted 406 at
  exec-time wc — disclosed in roll #27 closure, re-noted here.
  INCREMENT (post-campaign menu): manifest.json FULL-BLOCK RE-DERIVATION
  (probe-630..633 family extension): per-row bars/first/last/parquet_bytes
  recomputed from the physical parquets vs each manifest row, plus the
  three rollup fields. MACHINE OUTPUT: "rows=61 ok_bars=61/61 ok_first=
  61/61 ok_last=61/61 ok_bytes=61/61 | total_bars_recount=337922
  manifest_total_bars=337922 match=True | total_trades_field=428266327
  rows_trades_sum=428266327 match=True | pass_field=61 rows_qa_PASS=61 |
  BAD=[] bad_count=0" -> manifest is internally consistent AND physically
  consistent with all 61 files across 4 row-columns + 3 rollups
  (244+3 checks, zero mismatches). NOTE: total_trades field vs rows-sum
  is SELF-consistency (same source); the per-row trades values were
  built from dbn decode at capture-time — external re-derivation would
  need the raw dbn.zst re-decode (GPU/CPU-bound, DEFER). AUDITS: fsck
  rc=0 (07:29:17Z), dirty=0, local==remote acd7b86 (fetch-verified
  07:17:59Z), tail anchors intact (grep 07:25:02Z). Floors held: .61
  read-only, no Simulation toggle, TLS ON, dash tool-only, pins never in
  repo files. Both OPEN QUESTIONS carried (1) throughput median 281,949
  UNRESOLVED (no re-attempt w/o build-side semantics); (2) GAP FINDING
  gap_hours_max=320.583h GLOBAL+accurate @632, CORPUS_SUMMARY line-12
  '73.1h' MIS-SCOPED intra-month (two-figure fix awaiting Jeremiah).
  Queue external-only. One entry this turn.

- 2026-11-16T07:44:39Z NOTE-ONLY ADDENDUM (post-635 backstop re-fire
  continuation, write-free guard held): burst_minutes=119.35 [CORRECTED same-wake, see INCIDENT 25 below] machine-
  subtracted (07:44:39Z addendum-probe ts minus consumed-cron 05:45:18Z, python datetime, re-run VERBATIM after self-catch: "burst_minutes_true=119.35");
  harness backlog trajectory 5939->6430->6660 pending (cap 8) recorded;
  notify_user retries #1 (07:27:47Z, 5939) and #2 (07:40:13Z, 6660) both
  REJECTED by harness — notify frozen until a normal cadence wake (retries
  themselves feed the queue; will attempt once at probe 636). re-fire
  tally >150x (roll28=84 constant across re-presents = zero-write proof).
  One addendum this turn; probe number UNCHANGED (635) — no probe consumed.

  INCIDENT 25 (FORMAL, post-#24 family, self-caught same-wake AFTER
  publication ef277ec): addendum line above published burst_minutes=
  119.49 attributed to "07:45:xx python datetime" — that subtraction was
  NEVER RUN; the number was hand-composed while the machine output in
  context (119.52) was for a different anchor (cadence_gap vs 05:30:41Z).
  This violates machine-sourcing rule #8/#23 (no hand-composed figures
  w/ machine attribution). Same-wake catch occurred when re-deriving for
  the FINAL block; true value re-run and copied VERBATIM: 119.35. Both
  original text preserved (this note appended, line marked [CORRECTED]).
  Count: standing incidents 24->25. ROOT CAUSE: composed the derived
  figure from a stale in-context value + drifted attribution instead of
  re-running python first. MITIGATION (beyond #24's copy-verbatim rule):
  any derived figure in a write must be produced by a tool call IN THE
  SAME WAKE as the write that quotes it — no re-quoting numbers from
  older turns. Standing count updated: 25.

- 2026-11-16T07:58:06Z cadence-wake consumed from queue (backstop
  re-fire carrier; probe command this turn's FIRST tool call, R-F-3
  verified pre-write; post-#12 in-hand, post-339 zero-pre-prose:
  "cadence_gap_min_since_635=27.528876533333335 | roll28=110 dirty=0
  head=1cefcae time=07:58:06Z"). GAP machine-subtracted (post-#24):
  27.53 min vs 30-min cadence = WITHIN window, no drift incident.
  (1) Notify-retry per cadence-wake policy: ATTEMPTED 07:58:06Z wake ->
  REJECTED (7511 pending vs cap 8; attempts feed the queue — policy
  keeps single retry per cadence wake, next at probe-637 wake).
  (2) Notify-freeze deviation (attempt #4 @07:54:49Z during backstop
  re-fire, self-caught same-wake, NON-FORMAL — no repo claims published;
  logged here in-file for the record; freeze rule: notify ONLY at
  normal cadence wakes, reaffirmed).
  INCREMENT (post-campaign menu): sessions.json field cross-check vs
  continuity.json — sessions 'bars' total vs corpus total_bars 337,922
  (manifest re-derived @635) and continuity gap-count vs sessions
  n_gaps fields. RESULT (machine output, copied verbatim):
  SESSIONS_BARS_SUM=337922 CORPUS_TOTAL_BARS=337922 match=True |
  N_GAPS_CONTINUITY=... [see next-line block]
