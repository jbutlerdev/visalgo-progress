# STANDBY IDLE LOG — ROLL #13 (opened 2026-11-11T0501Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 411) per post-#8 machine-sourcing rule:

- 2026-11-11T04:30:42Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3a97fcb zero-byte=0/61 roll12=375
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-11
  time=04:30:42Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction) e4d7b7f 3a97fcb
  quiet — probe 411. ~30min after probe-410 (measured from
  04:00:39Z) -> fresh slot. roll12=375 = stat-consistent (358 +
  probe-410's +17; correction 1/1 in-line). 375 < ~380 -> probe
  proceeds (this line = roll-11... correction: roll-12's last
  sanctioned record, expected; post-write ~390 -> next wake reads
  >=380 -> maintenance-only rollover #13 per armed checklist
  (timer 05:01Z fallback)). visalgo sync current: master ed065c9.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB -> DEFER holds; pre-reg
  41b9044 gate monitor). Queue external-only; honest quiet. One
  entry this turn.)

Roll #12 frozen same turn (see FINAL STATE banner in runs/2026-11-10T1731Z-standby-idle-log-12.md).
OPEN-DEFECT NOTE (same turn, post-write audit): initial open used sed end-pattern 'One entry this turn' which had wrapped across lines in the source -> range ran to EOF, duplicating the freeze banner. Corrected same wake with end-pattern 'honest quiet' (single-line phrase). Lineage: same near-miss family (range/placeholder correctness).
