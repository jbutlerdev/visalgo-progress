# 2026-10-28T1925Z — fw24 dry-run DLL **RUNNING on sierra-dev** (unit started via sudo, PERF restarted, model calls live ~11ms/bar); agent gate file removed (backup kept); sltp 4th field `1.75 5.0 1.75 54` in place — contract-trigger needs REPLAY_START next (type: wake, ~25min)

## What happened on .162 (dev twin, full authority)
* `systemctl start sierra-app`: plain start = Access denied;
  **`sudo systemctl start`** (dev has passwordless sudo) ⇒ unit
  ACTIVE, wine `SierraChart_64.exe Haus_-_ES_NQ_2.Cht` running;
* **DLL proof-of-life**: agent_debug.log shows the fresh run's PERF
  sequence (calls=1 … 699, http≈11ms/bar ⇒ AGENT_FEATURES model calls
  working) — the staged AgentFrame_64.dll is loaded and executing;
* gate file `agent_off.txt` **moved aside** (⇒ agent ON;
  `.bak-20261028` kept) — note: dev's Auto-Trading-equivalent is moot
  because fw25 makes DRYRUN the compiled default: **no order path
  exists in this build at all** (dry-run DLL, 7 KB leaner);
* `agent_sltp.txt` = "1.75 5.0 1.75 54" (maxbars 54 armed).

## State at checkpoint
* no `DRYRUN`/`gate k=` lines yet because no entry decision has
  fired: replay path needs `commands.json` REPLAY_START (the
  backtest_* files + replay machinery are on dev already — last
  infer stamp 20261021.16000 shows it ran before);
* transient: a pgrep'd PID 2335769 self-exited pre-start (same
  self-exiting stray as 1800Z; harmless).

## Next cycle (B3 finish)
1. `commands.json` REPLAY_START for a day with a known signal-cache
   entry (e.g. via the archived sig caches) — expect `DRYRUN …`
   order lines + `LIVE TSTOP day=… max=54` after bar 54;
2. verify the 7 contract semantics against those lines (oracle);
3. parity: revert sltp to 3-field ⇒ no TSTOP ever;
4. B5: sc_client --dry-run vs dev twin; then C staging-prep page.
.61 untouched (read-only ceiling); restart/Auto-Trading = Jeremiah.
Sierra touched: **.162 only** (unit start via sudo, gate-file rename,
sltp write). Datasets read-only.
