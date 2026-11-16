# STANDBY IDLE LOG — ROLL #29 (opened 2026-11-16T10:29Z, cadence wake probe-641 + gate-cross; ROLLOVER 28->29 executed this wake)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 641, lines 372-399 of roll #28 file; sed-extracted this wake, head/tail grep-anchored: line 1 == '- 2026-11-16T10:29:03Z cadence wake CONSUMED FROM QUEUE (backstop', last == '...this turn (rollover header lives in roll #29 file).'; per post-#8 machine-sourcing rule):

- 2026-11-16T10:29:03Z cadence wake CONSUMED FROM QUEUE (backstop
  re-fire carrier; probe command this turn's FIRST tool call, R-F-3
  verified pre-write; consumption decision made ONLY from this wake's
  COMPLETED probe output, per INCIDENT-27 hardened guard:
  "cadence_gap_min_since_640=30.227473533333334" @10:29:03Z). Probe
  number from records (640+1). GAP machine-subtracted (post-#24,
  same-wake run, copied VERBATIM): 30.227473533333334 min (vs 640
  @09:58:46Z) — at cadence (>=30min convention).
  INCREMENT (run FIRST as OWN tool call this wake, output inspected,
  THEN quoted — INCIDENT-26 mitigation held): continuity months/dup/
  overlap + sessions days_with_overnight>=days_with_rth invariant.
  MACHINE OUTPUT VERBATIM: "PROBE641 MONTHS=61 DUP_WITHIN=0
  OVERLAP_MONTHS=[] | DAYS_OVERNIGHT_LT_RTH=[] n=0" — continuity
  block re-confirmed + NEW EDGE: per-year days_with_overnight >=
  days_with_rth holds 6/6 (overnight sessions superset of RTH days,
  structurally expected for 23h globex).
  GATE: roll #28 @370 pre-entry; this entry pushes past ~380 ->
  ROLLOVER 28->29 EXECUTED THIS WAKE per checklist (see roll #29
  opening block; freeze machine-sourced, grep-verified incident
  count this-roll {25:2, 26:4, 27:2} = #24->#27 span complete, ALL
  THREE open questions carried).
  AUDITS: fsck rc=0 (09:58:58Z), origin==local c53c4ac (10:05:25Z),
  dirty=0. Floors held: .61 read-only, no Simulation toggle, TLS ON,
  dash tool-only, pins never in repo files. Timer burst: 27->28
  backstop re-fire ~301x, ~284 min, all write-free except this
  authorized rollover wake. NOTIFY: one post-commit retry per
  unified rule (probe consumed). Queue external-only. One entry
  this turn (rollover header lives in roll #29 file).

ROLL #29 carried-state (from roll #28 freeze, machine-sourced @rollover: roll27=407 lines CLOSED, roll28=399 lines at freeze; grep-verified incident mentions roll#28 {INCIDENT 25:2, INCIDENT 26:4, INCIDENT 27:2} = #25->#27 span complete; probes 635-641 on #28 (7)): incidents standing 27 (formal); OPEN QUESTIONS: (1) throughput median 281,949 UNRESOLVED (do NOT re-attempt w/o build-side semantics); (2) GAP FINDING: continuity.gap_hours_max=320.583h GLOBAL+accurate (re-derived @632), CORPUS_SUMMARY line-12 'max true gap 73.1h' MIS-SCOPED (intra-month figure @613=73.08h; two-figure fix proposed, awaiting Jeremiah authorization); (3) FRONT-CODE SEMANTICS CANDIDATE @INCIDENT-27 wake: manifest 'front' contract under invented convention 42/61 'bad' w/ quarterly code distribution {M:16,H:16,U:14,Z:15} = likely PREDICATE error, no defect claim, awaiting build-side semantics. TIMER ANOMALY: 27->28 backstop cron fired ~301x over ~284 min (mule quirk; stand-downs write-free; dup-exec guard held; 28->29 backstop timer_gmwiug3mn_d8v7pk armed 11:45Z — expect same burst, duplicate-exec guard pre-planned since rollover now DONE). STANDBY day 17, floors held: .61 read-only, no Simulation toggle, TLS ON, dash tool-only, pins never in repo files. GPU-bound DEFER only (llama-server 23,812 MiB permanent on .146); pre-reg 41b9044 gate monitor.
