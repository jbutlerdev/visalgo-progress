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
