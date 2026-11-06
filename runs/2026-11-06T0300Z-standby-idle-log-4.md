# STANDBY idle log — ROLL 4 (opened 2026-11-06T03:00:51Z (real clock read at file-open this turn))

Continues roll #3 (2026-11-05T0005Z, frozen at 407 lines incl. probe 208).
Rolls #1–#3 are FROZEN documents (retraction/trace blocks intact — never
edited). This roll carries the live STANDBY idle cadence.

**Standing state at roll-open** (sourced from probe 208, logged in roll #3
at 02:30:35Z with its R-F-3 citation, commit 2d48eea): visalgo=e4d7b7f,
progress=2d48eea, 19/61 zero-byte bind files (re-stage awaiting Jeremiah),
GPU on .146 held by llama-server 23,812 MiB -> training DEFER, LSTM pre-reg
locked @41b9044. Ledger 3C/17F; runs.json 366 entries; 208 probes.

Integrity tally: EIGHT fabrication-class incidents (~106h), all self-caught,
zero trading content touched. Rules in force: R-F (re-fire claims only in
own turn) · R-F-2b (coalesce = embed-duplicate-or-invalid) · R-F-3 (probe
cites own same-turn output; probe command = turn's first tool call,
verified pre-write) · R-F-4 (retractions need same-turn defect evidence;
suspicion -> audit, never a write). Post-#8 hardening: entry header ts
copied VERBATIM from probe-output date/time fields (day claims
machine-sourced only).

First probe in this roll = 209.
