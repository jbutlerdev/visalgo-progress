# STANDBY IDLE LOG — ROLL #23 (opened 2026-11-14T20:01:49Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 573) per post-#8 machine-sourcing rule:

- 2026-11-14T19:32:32Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=425dcff zero-byte=0/61 roll22=369
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-14
  time=19:32:32Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 425dcff — probe
  573 + **RE-DERIVATION CAMPAIGN COMPLETE 61/61**. ~32min after
  probe-572 (measured from 19:00:43Z; recomputed; wake ~2min late,
  within watch band) -> fresh slot. roll22=369 = stat-consistent
  (344 + probe-572's +25). FINAL TWO (sanctioned outstanding
  list): 202409 rebuilt (3998,6) == published, front=NQU4 —
  expiry-truncation month re-derived EXACT through its Sep-20
  cutoff (decides-at-that-tick front stays U4; the documented
  PARTIAL semantics reproduce bit-identically), EQUALS=True
  (10.4s); 202411 rebuilt (5679,6) == published, front=NQZ4
  (whole-span argmax), EQUALS=True (8.9s). === CAMPAIGN RECORD
  (probe-544..573, 30 waking cycles): **EVERY ONE of the 61
  corpus months (2021-03..2026-03) rebuilt from raw GLBX.MDP3
  .dbn.zst through the pinned e4d7b7f decoder (VERBATIM
  nq_ticks_load.py) is EXHAUSTIVELY EQUAL to its published
  5-min parquet** — shape + full index + OHLCV at 6dp, zero
  mismatches, zero exceptions; includes all 5 expiry-truncation
  months (202406/09, 202503/06/12) reproduced exactly under
  documented PARTIAL semantics; all 61 raw files re-decoded from
  source, no cached intermediates. Full-year completions: 2021
  10/10, 2022 12/12, 2023 12/12, 2025 12/12 (each month-by-
  month verified at claim time). NEXT: CORPUS_SUMMARY.md
  re-derivation section -> COMPLETED status (next wake or with
  rollover). Rollover watch: roll22=369 ~threshold -> exec
  candidate next wake (timer 9mwgpxgks_kluz03 21:07Z). CPU-bound
  (~19s). visalgo sync current: master ed065c9. State block:
  zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound DEFER
  only; pre-reg 41b9044 gate monitor). Queue external-only;
  honest quiet. One entry this turn.
- 2026-11-14T20:30:45Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=6b69b18 zero-byte=0/61 roll23=43
  gpu=[23812 MiB llama-server;256 MiB venv python] date=2026-11-14
  time=20:30:45Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 6b69b18 — probe
  574 + REAL INCREMENT. ~58min after probe-573 (20:30:45Z -
  19:32:32Z = 58m13s; the intervening rollover-22 exec wake at
  ~20:01 consumed NO probe per maintenance rule, so probe-573
  remains the last probe -> gap measured against it; 28m56s since
  that exec measurement) -> fresh slot. CORRECTION (measurement-
  class INCIDENT #19, self-caught in post-write audit): first
  draft wrote "~29min after probe-573" and "28m13s" — both wrong:
  58m13s vs probe-573 (failed to account for the probe-less exec
  wake), and 20:30:45-20:01:49 = 28m56s not 28m13s. Recorded per
  incident protocol; substantive claims (sweep 61/61) unaffected. roll23=43 = stat-
  consistent (rollover open committed at 43 lines probe-573
  header, +0 since). INCREMENT (post-campaign menu, first entry):
  **PUBLISHED-BARS HASH SWEEP COMPLETED 61/61** — every file in
  runs/data/corpus-2021-2026/bars/ sha256-identical to its
  persistent original in ~/visalgo-corpus/bars/ ("BARS-HASH-SWEEP:
  61/61 identical, 0 mismatched" @ 20:31:29Z); upgrades the prior
  3/3 spot-check (roll-20 era) to full-corpus coverage; combined
  w/ 13/13 JSONs + re-derivation 61/61, the published corpus dir
  is now hash-complete (bars+JSON) AND bit-exactly reproducible
  from raw. CPU-bound (fast). visalgo sync current: master
  ed065c9. State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB PERMANENT
  herd infra — GPU-bound DEFER only; pre-reg 41b9044 gate
  monitor). Queue external-only; honest quiet. One entry this
  turn.
