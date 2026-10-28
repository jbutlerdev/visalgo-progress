# 2026-10-28T0250Z — menu-3: sc_client.dtc offline tests (11) vs fake DTC server — the money-path client had ZERO coverage (type: wake, ≤25min)

vram gate #22: unchanged (next ping Thu if silent).

## Why this file
`sc_client/dtc.py` (387 lines) is the component that will one day place
**real orders** against Sierra's DTC server — and it had no tests at
all. Every prior sc_client validation was live-ish (dry-run against
sierra-dev). Offline unit coverage of its error paths is cheap insurance
for the day a code path that "can't happen" does, mid-session.

## Delivered (branch `algo-dev/dtc-client-testcov`, `e2d282fb`)
Stdlib-only `FakeDTC` server speaking the **real wire contract**: 16-byte
binary `<HHii4s` encoding handshake, then NUL-delimited JSON frames.
11 tests, 1.1 s:
* **handshake:** wrong type/encoding → `DTCError` (not a hang); server
  close mid-handshake → "closed" error;
* **logon:** `Result!=1` → "logon failed"; `TradingIsSupported=false` →
  error **names the Sierra setting to fix** (the ops slogan that saves
  a blind debugging session);
* **orders:** qty>1 refused **client-side** (forward-test cap; asserted
  nothing reaches the server); first ORDER_UPDATE matched by
  ClientOrderID returned with `_status`/`_reason` enum mapping;
* **framing:** order update split across two TCP chunks still parses
  (partial-frame reassembly); **wrong-ClientOrderID update does NOT
  satisfy the wait** — unmatched parked, later true match wins: the
  misattribution guard for a multi-order future;
* `wait_for` timeout raises with saw-what diagnostics.

**Caught while building (mine, recorded):** fake first replied with a
12-byte handshake; real DTC answers 16 — client then blocks its full
10-s connect timeout (the suite's first run took 90 s and surfaced
exactly that). Both sides of the contract now pinned to bytes.

Suite: offline 62 → **73 tests** (loop 23, ml 34, sc_client 11, +...
= 68? No — verified: loop 23 + ml 30 master/34 branches + maxbars 7 +
amt 4 + dtc 11; per-file ok-counts re-verified this cycle, log-truth
rule). 8 review-ready branches. Sierra: none. master fb1a019.
