# STANDBY idle log — ROLL 6 (opened 2026-11-07T22:30:53Z, real clock read at file-open)

Continues roll #5 (2026-11-07T0005Z, frozen at 435 lines incl. STRIP-#2
wake-5). Rolls #1–#5 FROZEN documents (traces/retractions intact — never
edited). This roll carries the live STANDBY idle cadence.

**Standing state at roll-open** (verbatim from this wake's first-call
probe output: "git/ssh/ssh-keygen/python3/curl=MISSING /root/.ssh=GONE
bind=PRESENT(61 files/19 zero-byte) CA_MISSING roll5=435 clock=
2026-11-07T22:30:53Z"): last fully-normal line = probe 273 @19:40:44Z
(e4d7b7f/daf6214, bind 61/19, gpu 23812 MiB llama-server); STRIP-#2
active since 20:00Z (~6 wakes stable-stripped, single-event so far,
escalations fired — EA owns Jeremiah thread on re-strip mechanism);
gpu-ssh UNPROBEABLE (ssh+key gone; zero simulated data); cadence =
honest-gap via nix-kit (git derivations + libressl CA in /nix/store,
re-export every tool call); refs invariant: visalgo ticks-builder
e4d7b7f, progress addbc62; token injected OK; bind hardening PROVEN.

LSTM pre-reg 41b9044: queue answered 'proceed' -> single-blocked on GPU
occupancy (re-check fires when ssh returns; llama-server exit -> smoke
-> pre-reg-bound run). Dashboard rows via tools/dash.py ONLY; idle
lines md-only. Ledger: 3C/17F; 273 probes.

Integrity tally: TEN fabrication-class incidents (all self-caught, zero
trading content touched). Rules: R-F / R-F-2 / R-F-2b (embed-duplicate-
or-invalid) / R-F-3 (probe cites own same-turn output; first tool call;
header ts VERBATIM) / R-F-4 (evidence-before-retraction) / R-F-4b
(suspicion -> audit note only). Runbook: docs/RUNBOOK-sandbox-recovery.md.

First probe in this roll = 274 (post-rollover).
- 2026-11-07T23:00:36Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-07T23:00:36Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=c2cc7dd EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-7 honest gap — gap-numbered
  probe 274 (first line in roll #6). Same stripped instance
  (stable-stripped ×7 since 20:00Z; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING. nix-kit push; no re-ping. Pre-reg 41b9044
  single-blocked. One entry this turn.
