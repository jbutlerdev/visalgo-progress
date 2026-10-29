# 2026-10-29T0230Z — v4 `.61` deploy runbook drafted (step C) + gate puzzle ROOT-CAUSED: the deployed fw13 DLL ignores `agent_on.txt` (file-override is fw20+; box build reads the study INPUT only) (type: wake, ~15min)

## Root cause (answers 0200Z's "agent_on.txt exists yet OFF")
`git log -S "FileExists(off)"`: the on/off FILE override was added in
**fw13-era code but the toggle block with `agent_on.txt` honors-file
logic landed in fw20** (`85e7754`, which ALSO removed it from... see
line history: current master has both off/on honors; the deployed
`.162`/`.61` fw13 build only had... verified: fw13-era source lacks
the FileExists(on) branch entirely — the 0-byte `agent_on.txt` (Sep
30) has been IGNORED the whole time; the gate was the study INPUT all
along. Runbook instructs arming BOTH mechanisms (input YES + file).

## The runbook (docs/DEPLOY_RUNBOOK_61.md, master @ 8331baa)
* **Gate stack** (all 5 must hold): input/file arm (fw20+ caveat),
  Global AT, per-chart AT (Jeremiah-only, resets on restart), Trade
  Service + account/contract, and the **fw25 compile gate** — the
  build MUST carry -DVISALGO_LIVE_ORDERS=1 (dry-run is the compiler
  default; verify via build log + size delta vs dry 2,426,005B);
* **Pre-flight**: B3 7/7 contract, live build w/ account+symbol
  compile-pins (fw25/26), dry-build evidence from B4, B5 client
  dry-run, sha-pinned Jeremiah sign-off;
* **Deploy**: backup→scp→sha→arm files (sltp 4th field=54) →
  Jeremiah restart + gate re-arm + mode screenshot → touch agent_on +
  input YES → watch for BUY_ENTRY@/LIVE TSTOP/ORDER REJECTED/ERROR;
* **Kill rule**: exit-side ORDER ERROR = flatten broken (fw11 lore) →
  rm agent_on + manual flatten check, kill-first-ask-second;
* **Day-0**: first BUY_ENTRY@ fill = live-forward test day 0; Trade-
  Tracker pull = first REAL PnL read ever (replaces retracted log-PnL);
* **Rollback <60s** (rm on-file kills trading fw20+; DLL restore backup).

## Next (unchanged, gated)
Jeremiah: attribution answer + B3 pick (+ now: deploy approval chain
per runbook). Then B3→B4→B5→C-execute. LSTM study slot-ready.
Sierra touched: none (read-only ssh listing only; local git archaeology).
