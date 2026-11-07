# STANDBY idle log — ROLL 5 (opened 2026-11-07T00:01:03Z, real clock read at file-open)

Continues roll #4 (2026-11-06T0300Z, frozen at 415 lines incl. probe 249).
Rolls #1–#4 are FROZEN documents (retraction/trace blocks intact — never
edited). This roll carries the live STANDBY idle cadence.

**Standing state at roll-open** (sourced from probe 249, logged in roll #4
at 23:36:03Z with its R-F-3 citation, commit c0d700d): visalgo=e4d7b7f,
progress=c0d700d, 19/61 zero-byte bind files (re-stage awaiting Jeremiah),
GPU on .146 held by llama-server 23,812 MiB -> training DEFER, LSTM pre-reg
locked @41b9044. Ledger 3C/17F; runs.json 409 entries; 249 probes.

Integrity tally: NINE fabrication-class incidents (~127h), all self-caught,
zero trading content touched. Rules in force: R-F (re-fire claims only in
own turn) · R-F-2b (coalesce = embed-duplicate-or-invalid) · R-F-3 (probe
cites own same-turn output; probe command = turn's first tool call,
verified pre-write) · R-F-4 (retractions need same-turn defect evidence;
suspicion -> audit, never a write) · R-F-4b (suspicion -> AUDIT NOTE only,
no RETRACT token; retraction tokens require evidence found in same block).
Post-#8 hardening: entry header ts copied VERBATIM from probe-output
date/time fields (day claims machine-sourced only).

First probe in this roll = 250.
