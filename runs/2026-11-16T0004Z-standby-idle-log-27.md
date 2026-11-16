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
