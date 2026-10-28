# 2026-10-28T1800Z — Dry-run hardening (fw25): order-sending is now OPT-IN at compile time (safe default) + sierra-dev environment surveyed for B4 (type: wake, ~18min)

## Why
`AGENT_DRYRUN` was a source-edited const — the deployed .61 DLL is a
LIVE build (fw22, "edit to 0, ship"). For a live-money-adjacent
activation whose next steps involve installing DLLs on dev and testing
tstop paths, "remember to keep it 1 on dev" is a habit, not a control.
This cycle converted it into a compile-time control.

## The change (fw25, commit on v4-activation)
* `#ifndef VISALGO_LIVE_ORDERS / #define VISALGO_LIVE_ORDERS 0` →
  `AGENT_DRYRUN = !VISALGO_LIVE_ORDERS`: **default = DRY-RUN, no
  orders**, forever, unless a build explicitly passes
  `-DVISALGO_LIVE_ORDERS=1`;
* the .61 live build (only, after Jeremiah's go) must carry the flag
  explicitly — the go-instructions page (C) will pin the exact
  command line;
* (macro-collision caught in-flight: first attempt `#define
  AGENT_DRYRUN` renamed the variable itself — distinct name used);
* both modes cross-compile: default **2,427,517** B vs live
  **2,434,696** B — the ~7 KB delta is the order path compiling
  in/out, independent evidence the flag bites.
Dev DLL for B3: `/tmp/AgentFrame_dev_fw24.dll`
sha256 `400a91ee…` (dry-run default + AGENT_FEATURES=1).

## sierra-dev (.162) environment survey (for B4)
* `~/SierraChart/ACSIL/` has **no DLLs, no RELOAD** — fw24 would be
  the FIRST DLL there; B4 must also create the dir layout + study
  attach (AgentFrame study on a chart) — bigger than a drop-in swap;
* agent dir exists (backtest_* files, agent_debug.log) — the frame
  pipeline has run there before;
* `sierra-app` unit **inactive** but a sierra process exists (pid
  2323631, started outside systemd) — unit-vs-process discrepancy
  logged for B4 reconciliation (don't fight an unmanaged instance).

## Next (B3/B4, dedicated cycle)
Deploy dev DLL → start/attach on .162 (chart w/ agent), sltp file
`1.75 5.0 1.75 54`, dry-run (now the DEFAULT), run the 7 contract
semantics vs LIVE TSTOP log lines; then B4 proper w/ RELOAD+md5+LOAD
proof. .61 untouched; restart/Auto-Trading = Jeremiah.
Sierra touched: .162 READ-ONLY (ls/pgrep). Datasets read-only.
