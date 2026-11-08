# STANDBY idle log — ROLL 7 (opened 2026-11-08T18:30:46Z, real clock read at file-open)

Continues roll #6 (2026-11-07T2230Z, frozen at 394 lines incl. probe 300
+ NQ-tail experiment entry). Rolls #1-#6 FROZEN documents (traces/
retractions intact — never edited). This roll carries the live cadence.

**Standing state at roll-open** (verbatim from probe 300, logged in roll
#6 at 18:00:59Z, commit 2011c2a): visalgo ticks-builder=e4d7b7f,
progress main=2011c2a, zero-byte=0/61 (data repair VERIFIED 2026-11-08:
19 months restored md5-verified by Jeremiah; my independent checks:
0/61 counter, 8.2G, mtime-isolates-the-19, decode OK), raw-data
AVAILABLE, gpu ssh CONFIRMED (llama-server 23,812 MiB -> human session
-> DEFER holds, read-only occupancy monitor each wake), Campaign-1 tail:
19/19 restored months built OK, 101,087 bars, determinism PASS (sha256
9a14fa6d canary), 20 parquets + 20 manifests sandbox ~/work/nq-tail
(staging path awaits Jeremiah — sandbox non-durable lesson), LSTM pre-reg
41b9044 SINGLE-blocked on GPU freeing (queue answered 'proceed'), dash
rows via tools/dash.py only, idle lines md-only. Ledger 3C/17F+;
300 probes; 26 STRIP-#2 gap rows + recovery arcs x3 closed.

Integrity tally: TEN fabrication-class incidents (all self-caught, zero
trading content touched). Rules: R-F / R-F-2 / R-F-2b (embed-duplicate-
or-invalid) / R-F-3 (probe cites own same-turn output; first tool call;
header ts VERBATIM) / R-F-4 / R-F-4b. Runbook: docs/RUNBOOK-sandbox-
recovery.md. Recovery economics: 3 arcs, each cheaper.

First probe in this roll = 301.
- 2026-11-08T19:05:11Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening:
  "fetch-rc=0 origin/main=2e27285 zero-byte=0/61 artifacts=20
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-08
  time=19:05:11Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 2e27285
  quiet — probe 301 (first line, roll #7). ~64min after probe-300
  (measured from 18:00:59Z; intervening slot was maintenance
  rollover). State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61 post-repair) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  -> DEFER holds; pre-reg 41b9044 gate monitor). Artifacts 20/20
  alive (staging awaits Jeremiah). One entry this turn.
- 2026-11-08T19:32:46Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening:
  "fetch-rc=0 origin/main=b4be8dd zero-byte=0/61 artifacts=20
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-08
  time=19:32:46Z"; R-F-2b: no embedded duplicate -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f b4be8dd
  quiet — probe 302. ~27min after probe-301 (measured from
  19:05:11Z) -> fresh slot. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61 post-repair) | gpu ssh CONFIRMED (llama-server
  23,812 MiB -> DEFER holds; pre-reg 41b9044 gate monitor).
  Artifacts 20/20 alive. One entry this turn.
