# 2026-10-28T2355Z — 5th hardware-free gate: tstop **full exit-chain order** (stream-cut → sl → tp → trail → eod) — C++ agrees with the Python oracle on all 7 cases, (tag, pnl) exact (type: wake, ~18min)

## Discovery this cycle (matters for the B3 decision)
While hunting the next unit-testable piece I found the backtest
engine already carries a **simulated position** (`g_BtSide` +1/−1 with
g_BtSL/g_BtTP/g_BtTrDay, exit check order: new-day→sl→tp→1555-eod,
close-based trail replica of sim_pnl_trail, one-entry-per-day).
⇒ the earlier assumption ("pos never nonzero → tstop only
exercisable via trade service") was WRONG for the backtest engine:
Jeremiah's alt-path (2) is cleanly feasible inside it (AGENT_BACKTEST
build + backtest_signals + g_Bt-side tstop block, zero trade service).
Flagged ready-to-build on a word.

## New gate: `acsil/tstop_replay_test.cpp` — 7/7 PASS (commit 75453a5)
Replicates the DLL exit sequence (maxbars stream-cut FIRST, then
sl, tp, trail update on settled close, eod) and asserts **identical
(tag, pnl) to ml/test_timeslot_contract.py** on all 7 cases (incl.
the SHORT mirror + trail-armed-still-time-stopped). Three authoring
hiccups fixed transparently (leftover junk line, const-ref resize,
sed'd include) — test-only, committed clean.

## Gate stack (5 layers, all green)
1. python contract oracle 7 ✅ · 2. trigger 8 ✅ · 3. parse 15 ✅
4. cancel-selection 10 ✅ · 5. **exit-chain order C++ vs Python 7/7 ✅**
Honest scope line: gate 5 is a MIRROR of the deployed chain (validates
check-ORDER + cross-language semantics agreement), not the DLL
itself — the on-box run still owns the live-API half (CancelOrder
rcs, BuyExit fill, bracket-fill races). That half needs either the
SimMode flip or my backtest-engine extension (both paths now
fully-specified; waiting on Jeremiah's pick or a word to build the
alt-path).

Sierra touched: none. Datasets read-only. GPU LSTM study scheduled
~00:04Z still ahead.
