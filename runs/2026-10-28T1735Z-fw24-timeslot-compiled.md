# 2026-10-28T1735Z — **B2 done: fw24 TIME-STOP written & cross-compiles** (86-line patch, OFF=byte-identical audit PASS, 2.43 MB DLL) — B3 contract run on sierra-dev next (type: wake, ~25min)

## The patch (acsil/AgentFrame.cpp, commit 9825098 on v4-activation)
* **agent_sltp.txt 4th field**: `"1.75 5.0 1.75 54"` → g_AgMaxBars=54;
  `mb` defaults 0, `g_AgMaxBars = (mb >= 2 ? mb : 0)` — 3-field files
  keep maxbars 0 (OFF);
* **entry bar time recorded** (g_AgTrBarHH/MM) in both entry blocks
  (state-only, no control-flow change);
* **time-stop block** before the exit path: when holding our entry
  (g_AgTrDay==entryDay, key differs from current bar, one-shot per day
  via g_AgMaxBarsHitDay) and `(now−entry)/5 ≥ g_AgMaxBars`:
  1. find OUR working attached orders against the position (both stop
     AND target — the pre-existing trail loop only ever looked for the
     stop), `sc.CancelOrder` each (log failures, continue anyway);
  2. market close via `sc.BuyExit/SellExit` (TextTag
     visalgo-agent-tstop);
  3. reset trail state, log `LIVE TSTOP day= since= max= rc= canc=`,
     EXIT-REJECTED alarm line if the close itself is rejected.
* **OFF-parity audit (the safety gate)**: block reachable only under
  `g_AgMaxBars > 0`; default 0; fscanf-fail path → 0; no other lines
  touched (diff +86/−2, both − lines are the modified fscanf). With a
  3-field sltp file the DLL is behaviorally pre-fw24.

## Toolchain finding (for the record)
build.sh's docker flow is unavailable in-sandbox; direct
`x86_64-w64-mingw32-g++ -shared -O2 -I sc_headers -static ...
AgentFrame.cpp -lwinhttp` builds it (**-lwinhttp AFTER the source** —
lib-before-source fails to link; that's also why build.sh's default
target differs). Baseline (pre-patch) compiles too — same flags, so
the diff-vs-baseline audit above is apples-to-apples.

## B3 next (the gate before any deploy)
Run the 7 ml/test_timeslot_contract semantics against the DLL on
sierra-dev .162: dev-side sltp file `1.75 5.0 1.75 54`, dry-run mode,
verify LIVE TSTOP lines + bracket cancellation via TradeActivityLogs
read-back; default-build (no 4th field) parity check on the same
chart. Only then B4 (deploy to .162 ACSIL dir with *.bak + RELOAD +
md5 + LOAD lines) and B5 (sc_client dry-runs). .61 untouched;
staging-prep only later; restart/Auto-Trading = Jeremiah.

DLL artifacts: baseline & fw24 in /tmp (rebuildable from 9825098;
md5s recorded at B4 deploy time). Sierra touched: none this cycle.
