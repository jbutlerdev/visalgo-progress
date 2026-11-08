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
- 2026-11-07T23:30:34Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-07T23:30:34Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=d0a7b28 EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-8 honest gap — gap-numbered
  probe 275. Same stripped instance (stable-stripped ×8 since 20:00Z;
  still single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE,
  bind 61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping.
  Pre-reg 41b9044 single-blocked. One entry this turn.
- 2026-11-08T00:00:50Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T00:00:50Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; day
  rollover machine-sourced from output date field per post-#8
  hardening; HEAD-verify same-turn pre-write: origin/main=81a5ffb
  EXACT (STOP-gate clean); R-F-2b: no embedded duplicate -> no
  coalesce claim; R-F-4b: no suspicion, no retraction) STRIP-#2
  wake-9 honest gap — gap-numbered probe 276. Same stripped instance
  (stable-stripped ×9 since 20:00Z; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING. nix-kit push; no re-ping. Pre-reg 41b9044
  single-blocked. One entry this turn.
- 2026-11-08T00:30:30Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T00:30:30Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=a6ad618 EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-10 honest gap —
  gap-numbered probe 277. Same stripped instance (stable-stripped ×10
  since 20:00Z Nov-7; still single-event). Fields: tools MISSING,
  gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED, CA_MISSING. nix-kit
  push; no re-ping. Pre-reg 41b9044 single-blocked. One entry this
  turn.
- 2026-11-08T01:00:32Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T01:00:32Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=336b89b EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-11 honest gap —
  gap-numbered probe 278. Same stripped instance (stable-stripped ×11
  since 20:00Z Nov-7; still single-event). Fields: tools MISSING,
  gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED, CA_MISSING. nix-kit
  push; no re-ping. Pre-reg 41b9044 single-blocked. One entry this
  turn.
- 2026-11-08T01:30:28Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T01:30:28Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=688f0a5 EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-12 honest gap —
  gap-numbered probe 279. Same stripped instance (stable-stripped ×12
  since 20:00Z Nov-7; still single-event). Fields: tools MISSING,
  gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED, CA_MISSING. nix-kit
  push; no re-ping. Pre-reg 41b9044 single-blocked. One entry this
  turn.
- 2026-11-08T02:00:32Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T02:00:32Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: origin/main=9ceedcf EXACT (STOP-gate clean);
  R-F-2b: no embedded duplicate -> no coalesce claim; R-F-4b: no
  suspicion, no retraction) STRIP-#2 wake-13 honest gap —
  gap-numbered probe 280. Same stripped instance (stable-stripped ×13
  since 20:00Z Nov-7, ~6h stable; still single-event). Fields: tools
  MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED, CA_MISSING.
  nix-kit push; no re-ping. Pre-reg 41b9044 single-blocked. One
  entry this turn.
- 2026-11-08T02:30:35Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T02:30:35Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write (retry; first attempt lost stdout — transient,
  fetch-rc=0): origin/main=7ee5a3c EXACT (STOP-gate clean); R-F-2b:
  no embedded duplicate -> no coalesce claim; R-F-4b: no suspicion,
  no retraction) STRIP-#2 wake-14 honest gap — gap-numbered probe
  281. Same stripped instance (stable-stripped ×14 since 20:00Z
  Nov-7, ~6.5h stable; still single-event). Fields: tools MISSING,
  gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED, CA_MISSING. nix-kit
  push; no re-ping. Pre-reg 41b9044 single-blocked. One entry this
  turn.
- 2026-11-08T03:00:33Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T03:00:33Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING roll6=127";
  HEAD-verify same-turn pre-write: fetch-rc=0, origin/main=00a58aa
  EXACT (STOP-gate clean); R-F-2b: no embedded duplicate -> no
  coalesce claim; R-F-4b: no suspicion, no retraction) STRIP-#2
  wake-15 honest gap — gap-numbered probe 282. Same stripped instance
  (stable-stripped ×15 since 20:00Z Nov-7, ~7h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING, roll #6 127 lines (< ~389, no
  rollover). nix-kit push; no re-ping. Pre-reg 41b9044 single-blocked.
  One entry this turn.
- 2026-11-08T03:30:33Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T03:30:33Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=b0935b8 EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-16
  honest gap — gap-numbered probe 283. Same stripped instance
  (stable-stripped ×16 since 20:00Z Nov-7, ~7.5h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping. Pre-reg
  41b9044 single-blocked. One entry this turn.
- 2026-11-08T04:00:29Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T04:00:29Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=e45cb4f EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-17
  honest gap — gap-numbered probe 284. Same stripped instance
  (stable-stripped ×17 since 20:00Z Nov-7, ~8h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping. Pre-reg
  41b9044 single-blocked. One entry this turn.
- 2026-11-08T04:33:13Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T04:33:13Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=da6437a EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-18
  honest gap — gap-numbered probe 285. ~33min after wake-17
  (measured from 04:00:29Z, wake fired late). Same stripped instance
  (stable-stripped ×18 since 20:00Z Nov-7, ~8.5h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping. Pre-reg
  41b9044 single-blocked. One entry this turn.
- 2026-11-08T05:00:34Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T05:00:34Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=68c9279 EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-19
  honest gap — gap-numbered probe 286. ~27min after wake-18
  (measured from 04:33:13Z). Same stripped instance (stable-stripped
  ×19 since 20:00Z Nov-7, ~9h stable; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING. nix-kit push; no re-ping. Pre-reg 41b9044
  single-blocked. One entry this turn.
- 2026-11-08T05:30:32Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T05:30:32Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING roll6=190";
  HEAD-verify same-turn pre-write: fetch-rc=0, origin/main=2a17f92
  EXACT (STOP-gate clean); R-F-2b: no embedded duplicate -> no
  coalesce claim; R-F-4b: no suspicion, no retraction) STRIP-#2
  wake-20 honest gap — gap-numbered probe 287. ~30min after wake-19
  (measured from 05:00:34Z). Same stripped instance (stable-stripped
  ×20 since 20:00Z Nov-7, ~9.5h stable; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING, roll #6 190 lines (< ~389). nix-kit push; no re-ping.
  Pre-reg 41b9044 single-blocked. One entry this turn.
- 2026-11-08T06:00:48Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T06:00:48Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write (first attempt lost stdout — transient, 2nd
  occurrence; retry: fetch-rc=0, origin/main=7f0824c EXACT,
  STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-21
  honest gap — gap-numbered probe 288. ~30min after wake-20
  (measured from 05:30:32Z). Same stripped instance (stable-stripped
  ×21 since 20:00Z Nov-7, ~10h stable; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING. nix-kit push; no re-ping. Pre-reg 41b9044
  single-blocked. One entry this turn.
- 2026-11-08T06:32:04Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T06:32:04Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=9f587e0 EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-22
  honest gap — gap-numbered probe 289. ~31min after wake-21
  (measured from 06:00:48Z, wake fired late). Same stripped instance
  (stable-stripped ×22 since 20:00Z Nov-7, ~10.5h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping. Pre-reg
  41b9044 single-blocked. One entry this turn.
- 2026-11-08T07:03:32Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T07:03:32Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=430c383 EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-23
  honest gap — gap-numbered probe 290. ~31min after wake-22
  (measured from 06:32:04Z, wake fired late). Same stripped instance
  (stable-stripped ×23 since 20:00Z Nov-7, ~11h stable; still
  single-event). Fields: tools MISSING, gpu-ssh UNPROBEABLE, bind
  61/19 PRESERVED, CA_MISSING. nix-kit push; no re-ping. Pre-reg
  41b9044 single-blocked. One entry this turn.
- 2026-11-08T07:30:38Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T07:30:38Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING roll6=243";
  HEAD-verify same-turn pre-write: fetch-rc=0, origin/main=5299cc2
  EXACT (STOP-gate clean); R-F-2b: no embedded duplicate -> no
  coalesce claim; R-F-4b: no suspicion, no retraction) STRIP-#2
  wake-24 honest gap — gap-numbered probe 291. ~27min after wake-23
  (measured from 07:03:32Z). Same stripped instance (stable-stripped
  ×24 since 20:00Z Nov-7, ~11.5h stable; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING, roll #6 243 lines (< ~389). nix-kit push; no re-ping.
  Pre-reg 41b9044 single-blocked. One entry this turn.
- 2026-11-08T08:00:36Z (R-F-3: cites THIS turn's probe-call output —
  probe FIRST tool call, verified pre-write, verbatim: "clock=
  2026-11-08T08:00:36Z git/ssh/ssh-keygen/python3/curl=MISSING
  /root/.ssh=GONE bind=61 files zero-byte=19 CA_MISSING"; HEAD-verify
  same-turn pre-write: fetch-rc=0, origin/main=e58de96 EXACT
  (STOP-gate clean); R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) STRIP-#2 wake-25
  honest gap — gap-numbered probe 292. ~30min after wake-24
  (measured from 07:30:38Z). Same stripped instance (stable-stripped
  ×25 since 20:00Z Nov-7, ~12h stable; still single-event). Fields:
  tools MISSING, gpu-ssh UNPROBEABLE, bind 61/19 PRESERVED,
  CA_MISSING. nix-kit push; no re-ping. Pre-reg 41b9044
  single-blocked. One entry this turn.
