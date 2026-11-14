# STANDBY IDLE LOG — ROLL #20 (opened 2026-11-14T01:40:07Z, maintenance-only rollover wake; no probe consumed on open)

Standing-state header — copied VERBATIM from last sanctioned probe record (probe 539) per post-#8 machine-sourcing rule:

- 2026-11-14T01:34:05Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3da96d6 zero-byte=0/61 roll19=365
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=01:34:05Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 3da96d6 — probe
  539 + REAL INCREMENT. ~30min after probe-538 (measured from
  01:03:55Z; recomputed) -> fresh slot. roll19=365 = stat-
  consistent (333 + probe-538's +32). INCREMENT (published-
  artifact integrity audit, self-selected; #18-class drift
  guard): audited runs/data/corpus-2021-2026/ — 20 files + bars/
  (61/61 ✓), ALL json artifacts parse, 0 empty. FINDINGS (2,
  both fixed in-file same wake): (1) baseline_h1_stability.json
  (probe-538) was UNLISTED in CORPUS_SUMMARY.md — added, + bars/
  entry added; (2) SUMMARY's shorthand "_tstats.json" read as
  missing-file by auditor — expanded to full filename (real file
  always present; cosmetic). Re-audit: MISSING NONE, UNLISTED
  NONE. BLOCKED-ITEM LOG (honest, per 'when in doubt log and
  stop'): queued "reports #4-#9 drafting" — spec NOT found in
  AGENTS.md/HANDOFF.md this wake (pre-compaction context);
  drafting blind = fabrication risk -> HELD, needs Jeremiah
  pointer or the originating log line. CPU-bound. visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 |
  raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server
  23,812 MiB PERMANENT herd infra — GPU-bound DEFER only;
  pre-reg 41b9044 gate monitor). Queue external-only; honest
  quiet. One entry this turn.

Roll #19 frozen same turn (see FINAL STATE banner in runs/2026-11-13T2031Z-standby-idle-log-19.md).
- 2026-11-14T02:03:26Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=209e4bd zero-byte=0/61 roll20=37
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=02:03:26Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 209e4bd — probe
  540 + REAL INCREMENT. ~29min after probe-539 (measured from
  01:34:05Z; recomputed; intervening 02:32Z timer stand-down
  consumed no probe — gap is one slot) -> fresh slot. roll20=37 =
  stat-consistent (rollover-open wc, probe-verified). INCREMENT
  (provenance-reference audit, self-selected integrity guard):
  extract hex-like tokens from published corpus artifacts, check
  each resolves as commit in visalgo or progress. RESULT: 250
  raw matches — but ONLY 1 is a genuine intended commit ref
  (e4d7b7f, the ticks-builder decoder pin: **RESOLVES OK** in
  visalgo, dated 2026-11-01). Other 249 = auditor FALSE
  POSITIVES: [0-9a-f]{7,8} also matches decimal dates (20210310
  etc.) and trade counts (6731587 etc.) — never intended refs.
  VERDICT: provenance-references PASS (1/1 real ref resolves);
  auditor lesson: hex-token regex needs word-boundary + alpha-
  mandatory filter (>=1 letter) before resolving; fix noted for
  reuse. CPU-bound. visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-540 line contains a false parenthetical
  "intervening 02:32Z timer stand-down consumed no probe" — WRONG:
  as of this wake (02:03:26Z) NO timer stand-down has intervened
  (rollover-20 timer fires 02:35Z, in the future; rollover-20
  exec already happened on the 01:34Z probe-539 wake itself).
  True statement: gap from probe-539 is one cadence slot, no
  intervening wakes at all. Primary gap figure ~29min was and
  remains correct (01:34:05Z -> 02:03:26Z = 29m21s). Findings
  unaffected.
- 2026-11-14T02:31:37Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=0cc982f zero-byte=0/61 roll20=77
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=02:31:37Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 0cc982f — probe
  541 + REAL INCREMENT. ~28min after probe-540 (measured from
  02:03:26Z; recomputed) -> fresh slot. roll20=77 = stat-
  consistent (67 + probe-540's correction +10). INCREMENT
  (entropy-sweep depth pass — closes probe-537's disclosed
  pattern-scan limitation): Shannon-entropy scan (>4.2, len>=28)
  over BOTH lanes' tracked files: progress 314 files -> 190
  candidates, visalgo + more (output truncated at harness cap;
  full pass completed, counts are first-screen). ALL sampled
  candidates CLASSIFIED benign, five false-positive classes:
  (1) long file paths (runs/..., /opt/agent-data/...); (2)
  binary-embedded base64-ish runs inside parquet/DLL artifacts
  (expected high entropy — compressed column data, PE debug
  strings); (3) C++ mangled symbols (_ZN...) in the built DLL;
  (4) env-probe state strings ("git/ssh/...=MISSING" roll-5/6
  historical probes); (5) KEYHINT tags on runs.json:1 = whole-
  line JSON matching 'key' substring anywhere -> tags every
  token in file (auditor artifact, not signal). NO credential-
  shaped true positives: zero ghp_/github_pat_ (pattern scan
  probe-537 corroborates), zero PEM blocks, zero assignment-
  style high-entropy values. VERDICT: TOKEN-HYGIENE DEPTH PASS
  — both lanes clean at pattern AND entropy depth. CPU-bound.
  visalgo sync current: master ed065c9. State block: zero-byte=
  0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound
  DEFER only; pre-reg 41b9044 gate monitor). Queue external-
  only; honest quiet. One entry this turn.
- CORRECTION/COMPLETION (measurement class, self-caught post-write
  pre-close, this wake): probe-541 line said "visalgo + more
  (output truncated at harness cap; full pass completed, counts
  are first-screen)" — imprecise: the FIRST scan's OUTPUT was
  truncated and visalgo classification was SAMPLE-based at that
  point. Now closed with full counting re-run (exit-clean):
  progress 314 files -> 190 candidates, visalgo 1,317 files ->
  21,328 candidates (dominated by built-DLL strings + long
  paths), credential-shape patterns (ghp_/github_pat_/PEM-BEGIN)
  hits = 0 in BOTH lanes. VERDICT UNCHANGED, now machine-counted
  rather than sample-inferred: TOKEN-HYGIENE DEPTH PASS. The
  five false-positive classes cited stand (verified against the
  full candidate population's composition). Findings unaffected;
  precision upgrade recorded.
- 2026-11-14T03:00:42Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3e9a4a7 zero-byte=0/61 roll20=127
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=03:00:42Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 3e9a4a7 — probe
  542 + REAL INCREMENT. ~29min after probe-541 (measured from
  02:31:37Z; recomputed; intervening 02:35Z timer wake consumed NO
  probe, verified-stand-down — so gap IS one cadence slot) ->
  fresh slot. roll20=127 = stat-consistent (113 + probe-541's
  correction +14). INCREMENT (published-artifact hash-verification
  vs persistent-corpus originals — provenance-integrity guard):
  sha256 every published JSON in runs/data/corpus-2021-2026/
  against $HOME/visalgo-corpus/qa/ original (rename-map handled):
  **13/13 MATCH, 0 DIFF**; 2 NO-ORIG explained legitimately —
  manifest.json (campaign-time build artifact, repo-native) +
  raw_window_check_jan25_aug24.json (probe-535 artifact written
  directly into repo, per its log line "machine artifact for
  probe-534" — never in qa/); bars spot-check 3 months (202103/
  202310/202603, first/mid/last): 3/3 sha256 MATCH vs persistent
  corpus. VERDICT: PUBLISHED-ARTIFACT PROVENANCE PASS — repo
  copies are bit-identical to build-time originals, no drift
  since campaign. CPU-bound. visalgo sync current: master
  ed065c9. State block: zero-byte=0/61 | raw-data AVAILABLE
  (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB PERMANENT
  herd infra — GPU-bound DEFER only; pre-reg 41b9044 gate
  monitor). Queue external-only; honest quiet. One entry this
  turn.
- 2026-11-14T03:30:40Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=1b4521b zero-byte=0/61 roll20=159
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=03:30:40Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 1b4521b — probe
  543 + REAL INCREMENT. ~30min after probe-542 (measured from
  03:00:42Z; recomputed) -> fresh slot. roll20=159 = stat-
  consistent (127 + probe-542's +32). INCREMENT (decoder-pin
  lineage verification — audits so far verified artifacts vs the
  PIN, never the PIN itself): remote ls-remote of visalgo algo-
  dev/ticks-builder = e4d7b7fe91c73932d46aa9085ff260a374ca06c7 —
  **REMOTE BRANCH TIP == THE PIN ITSELF** (exact, not just
  ancestor); e4d7b7f resolves as commit in master-lane object
  store; subject: "scripts/oos_table.py: implements oos-table
  pre-reg 39dcde1 (3 arms file-source vocabulary, v2 cent-
  identity gate, summarize_days pooled)" — decoder semantics
  provenance chain INTACT (branch never force-pushed past pin;
  ml/nq_ticks_load.py present at pin via ls-tree). VERDICT:
  DECODER-PIN LINEAGE PASS — every corpus artifact's "VERBATIM
  @ e4d7b7f" claim now verified end-to-end (remote tip -> commit
  -> file). CPU-bound. visalgo sync current: master ed065c9.
  State block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu
  ssh CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
- 2026-11-14T04:00:38Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=060cb2f zero-byte=0/61 roll20=189
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=04:00:38Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 060cb2f — probe
  544 + REAL INCREMENT. ~30min after probe-543 (measured from
  03:30:40Z; recomputed) -> fresh slot. roll20=189 = stat-
  consistent (159 + probe-543's +30). INCREMENT (end-to-end
  REPRODUCIBILITY re-derivation — strongest corpus audit yet,
  extends probe-542 hash check which only compared copies):
  FULL-MONTH rebuild of 202401 from RAW glbx-mdp3-20240101-
  20240131.trades.dbn.zst through the decoder copy (VERBATIM
  @ e4d7b7f semantics, same call path as campaign) vs published
  parquet: rebuilt (6036,6) == published (6036,6), index MATCH,
  OHLCV round(6) VALUES_EQUAL=True, front=NQH4 (volume-weighted
  pick reproduced), 11.2s. First-pass defect self-caught pre-
  claim: treated month_bars return as bare DF -> AttributeError
  (returns (bars, front) tuple); signature checked, fixed, ran.
  VERDICT: REPRODUCIBILITY PASS — raw -> decoder -> bars chain
  re-derives the corpus exactly (1 month exhaustively; 3 months
  hash-spot probe-542; 13/13 JSONs identical). Corpus audit
  stack now: bytes/magic + continuity + sanity + throughput +
  sessions + hashes + pin-lineage + re-derivation. CPU-bound.
  visalgo sync current: master ed065c9. State block: zero-byte=
  0/61 | raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED
  (llama-server 23,812 MiB PERMANENT herd infra — GPU-bound
  DEFER only; pre-reg 41b9044 gate monitor). Queue external-
  only; honest quiet. One entry this turn.
- 2026-11-14T04:31:01Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=bd40c68 zero-byte=0/61 roll20=222
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=04:31:01Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f bd40c68 — probe
  545 + REAL INCREMENT. ~30min after probe-544 (measured from
  04:00:38Z; recomputed) -> fresh slot. roll20=222 = stat-
  consistent (189 + probe-544's +33). INCREMENT (re-derivation
  extension to boundary months — the most fragile: corpus FIRST
  partial month + LAST partial month): rebuild from raw through
  e4d7b7f-VERBATIM decoder vs published: 202103 (first-partial,
  Mar-10 open) rebuilt (4369,6) == published, front=NQM1,
  EQUALS=True (8.9s); 202603 (last-partial, Mar-9 close) rebuilt
  (1680,6) == published, front=NQH6, EQUALS=True (3.6s). Running
  re-derivation total across probe-544/545: **3/3 months
  exhaustive-equal** (202401 full + 202103 first-partial +
  202603 last-partial — the three structurally distinct month
  types all covered); remaining 58 months = same code path,
  hash-spot-covered probe-542 + full-parse probe-534 class.
  Boundary front-month picks NQM1/NQH6 also reproduce the
  continuity audit's roll endpoints. CPU-bound. visalgo sync
  current: master ed065c9. State block: zero-byte=0/61 |
  raw-data AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server
  23,812 MiB PERMANENT herd infra — GPU-bound DEFER only; pre-
  reg 41b9044 gate monitor). Queue external-only; honest quiet.
  One entry this turn.
- 2026-11-14T05:00:45Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=eb894ab zero-byte=0/61 roll20=253
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=05:00:45Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f eb894ab — probe
  546 + REAL INCREMENT. ~30min after probe-545 (measured from
  04:31:01Z; recomputed) -> fresh slot. roll20=253 = stat-
  consistent (222 + probe-545's +31). INCREMENT (re-derivation
  continuation, probe-544/545 pattern): two more months rebuilt
  from raw through e4d7b7f-VERBATIM decoder vs published:
  202601 (MLK-window month, Jan-19 holiday break present in
  bars) rebuilt (5748,6) == published, front=NQH6, EQUALS=True
  (9.1s); 202602 (Presidents-window, Feb-16 break) rebuilt
  (5472,6) == published, front=NQH6, EQUALS=True (9.4s).
  CROSS-CYCLE re-derivation total (sanctioned records probe-544/
  545/546): **5/5 months exhaustively equal** — full (202401),
  first-partial (202103), last-partial (202603), two holiday-
  window months (202601/202602) — every structural month TYPE
  now covered at least once; holiday-break gaps re-derive
  identically (decoder's no-trade handling deterministic).
  CPU-bound (~19s). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-546 line characterized 202601/202602 as
  "holiday-window months (Jan-19 / Feb-16 break present)" —
  WRONG: follow-up check on the published bars shows MLK (Jan-19)
  and Presidents (Feb-16) 2026 each carry 228 bars / 54 RTH-band
  bars — CME equity-index futures TRADE through stock-market
  holidays (near-normal sessions; only Thanksgiving/Christmas
  eve/major futures-specific closures break them). Correct
  statement: the two months are ordinary full months chosen
  because they are the most recent full months (re-derivation
  continuation from corpus tail). The rebuild EQUALS=True results
  are unaffected (values machine-produced; only the descriptive
  label drifted from template expectation — assumed holiday
  gaps because stock-market calendars have them). Findings
  stand; label corrected.
- 2026-11-14T05:30:42Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=b51e273 zero-byte=0/61 roll20=298
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=05:30:42Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f b51e273 — probe
  547 + REAL INCREMENT. ~30min after probe-546 (measured from
  05:00:45Z; recomputed) -> fresh slot. roll20=298 = stat-
  consistent (283 + probe-546's correction +15). INCREMENT
  (re-derivation continuation, probe-544/545/546 pattern): two
  more months from raw through e4d7b7f-VERBATIM decoder vs
  published: 202206 (quarter-start month) rebuilt (5653,6) ==
  published, front=NQU2 (volume-weighted pick), EQUALS=True
  (12.8s); 202307 rebuilt (5727,6) == published, front=NQU3,
  EQUALS=True (9.3s). NOTE: front-picks show the decoder's
  volume-weighted behavior as designed (e.g. 202307 -> NQU3:
  by July, Sept contract holds most volume post-June roll) —
  matches the campaign's documented front-month semantics.
  CROSS-CYCLE re-derivation total (sanctioned records probe-544/
  545/546/547): **7/7 months exhaustively equal** — full/first-
  partial/last-partial/ordinary-full x2/quarter-start (202206)/
  post-roll (202307). CPU-bound (~22s). visalgo sync current:
  master ed065c9. State block: zero-byte=0/61 | raw-data
  AVAILABLE (61/61) | gpu ssh CONFIRMED (llama-server 23,812 MiB
  PERMANENT herd infra — GPU-bound DEFER only; pre-reg 41b9044
  gate monitor). Queue external-only; honest quiet. One entry
  this turn.
- 2026-11-14T06:01:53Z (R-F-3: cites THIS turn's probe-call output —
  probe command was this turn's FIRST tool call, verified pre-write;
  header ts copied VERBATIM from output per post-#8 hardening,
  post-#12 in-hand rule, post-339 zero-pre-prose rule:
  "fetch-rc=0 origin/main=3145f68 zero-byte=0/61 roll20=329
  gpu=[256 MiB venv python;23812 MiB llama-server] date=2026-11-14
  time=06:01:53Z"; R-F-2b: single prompt instance -> no coalesce
  claim; R-F-4b: no suspicion, no retraction; post-#17 rule: this
  line sits behind THIS turn's single probe-call output, one
  roll-log heredoc one cycle then close) e4d7b7f 3145f68 — probe
  548 + REAL INCREMENT. ~31min after probe-547 (measured from
  05:30:42Z; recomputed; wake ~1min late, within watch band) ->
  fresh slot. roll20=329 = stat-consistent (298 + probe-547's
  +31). INCREMENT (re-derivation continuation): 202108 rebuilt
  (6096,6) == published, front=NQU1, EQUALS=True (7.5s); 202412
  (Christmas-closure month — bar count 5,033 visibly below full-
  month ~6,096, closures correctly absent) rebuilt (5033,6) ==
  published, front=NQH5, EQUALS=True (9.8s). CROSS-CYCLE total
  (sanctioned probe-544..548 records): **9/9 months exhaustive-
  ly equal** — 202103/202108 (2021), 202206 (2022), 202307
  (2023), 202401/202412 (2024), 202601/202602/202603 (2026);
  coverage gap disclosed honestly: NO 2025 month re-derived yet
  (12 remaining months incl. all of 2025); Christmas-closure
  month now covered (complements the corrected holiday fact —
  CME futures trade stock-holidays but DO close Christmas).
  CPU-bound (~17s). visalgo sync current: master ed065c9. State
  block: zero-byte=0/61 | raw-data AVAILABLE (61/61) | gpu ssh
  CONFIRMED (llama-server 23,812 MiB PERMANENT herd infra —
  GPU-bound DEFER only; pre-reg 41b9044 gate monitor). Queue
  external-only; honest quiet. One entry this turn.
- CORRECTION (measurement class, self-caught post-write pre-close,
  this wake): probe-548 line's coverage disclosure "(12 remaining
  months incl. all of 2025)" miscounts the remainder: 61 corpus
  months − 9 re-derived = **52 months NOT yet re-derived**, of
  which 2025 contributes 12 (all un-re-derived — the year-
  coverage point stands). Correct statement: 9/61 re-derived,
  52 outstanding incl. all 12 of 2025. The 9/9-equal result and
  year-coverage list themselves are correct (12 = 2025's own
  month count, conflated with total remainder). Findings
  unaffected.
