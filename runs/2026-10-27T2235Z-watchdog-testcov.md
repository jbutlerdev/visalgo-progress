# 2026-10-27T2235Z — menu-3: frame_watchdog offline coverage (6 tests, branch watchdog-testcov); loop suite now 16 tests (type: wake, ≤15min)

vram gate #14: unchanged (second ping due tomorrow AM per hold).

## Delivered
`loop/test_frame_watchdog.py` (branch `algo-dev/watchdog-testcov`, test-
only): locks the live-capture safety net's contract —
* dark strip (~15 chart bg) → clean; message-log pane (~230) → dirty
* threshold at edges: mean 99 clean / 100 dirty (spec: <100)
* PARTIAL log pane (top half of strip, mean ~122) → dirty — the realistic
  post-restart corruption case
* tooling failure (broken/missing PNG) **fails open** — a broken decoder
  must never mass-quarantine the corpus; this test documents the existing
  `except: return True` as *intended policy*, so a future refactor can't
  silently flip it to fail-closed (which would have deleted-corpus-
  adjacent blast radius).
6/6 green; `loop` suite now 16 tests (frame_bars 10 + watchdog 6).
Fixture bug (np.asarray read-only view) caught & fixed pre-commit. No
production code touched.

## Cycle ledger (today, since activation 14:05Z)
Menus executed: 1 (9/9 re-verify), 2 (H-CAP reject), 3 (loop+watchdog
coverage), 4 (tail audit + complete-day OOS refresh), 5 (per-year +
per-month + recency-triangle analyses); strategy: H-TS→v3 CONFIRMED
(8/8) + Friday-gate audit (informational); OOS: 17-session base stable,
TS leg neutral-by-inactivity. Deferrals: vram gate ×14. Decision stack
(v2 / vram a-b-c / v3 DLL) fully documented for Jeremiah; branches:
hprob-bandgate, ts54-timeslot, loop-testcov, watchdog-testcov.

Sierra: none. Datasets read-only. master fb1a019 clean.
