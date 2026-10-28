# 2026-10-28T2015Z — **Safety bug caught in my own fw24 port before it ever touched orders**: time-stop fired CancelOrder/BuyExit even in the "dry-run" build → fixed + both build modes verified; dev now runs the fixed DLL (type: wake, ~20min)

## The bug (found while preparing the B3 replay trigger)
fw24's tstop block (written 1735Z) called
`sc.CancelOrder` ×(stop+target) + `sc.BuyExit/SellExit`
**unconditionally** — unlike every other order path, which mirrors the
`if (AGENT_DRYRUN) <log only> else <orders>` pattern. Consequence:
my "dry-run" dev build **would have fired real market order calls at
the trade service** on any tstop trigger. Exactly the failure mode
fw25 hardened against — and it lived in code I wrote after that
hardening. Verification-before-exercise caught it; the contract run
was minutes away from being the place it surfaced (on dev, luckily,
but against a real trade service).

## The fix (commit on v4-activation)
* whole cancel-loop + market-exit wrapped in `if (!AGENT_DRYRUN)` —
  dry-run sends NOTHING, state updates (one-shot/day guard, trail
  reset) + logging still run in both modes;
* TSTOP log line now prefixed **`DRYRUN` vs `LIVE`** (and
  `TSTOP(dry)` in orderBuf) — a dry-run trigger can never be
  mistaken for a live close in the log;
* EXIT-REJECTED alarm line only meaningful in live mode;
* **independent evidence the guard bites**: dry build shrank 1.5 KB
  (dead-code elimination of the whole order path when
  AGENT_DRYRUN=1); live build byte-size unchanged (guard always-true
  there, as intended).
Fixed dry-run DLL **deployed to .162 + unit restarted**
(sha c94fa2fe… both ends, 2,426,005 B).

## B3 structural finding (why replay can't exercise tstop)
`AgentFrame.cpp:119` comment + code: **REPLAY mode skips order
calls**, so `pos` never becomes non-zero ⇒ the tstop block
(`pos != 0` gate) can never fire in replay; and the dry-run build
has no order path at all. The honest exercise path is the
**live-order build against dev's SIM account** (fw25
`-DVISALGO_LIVE_ORDERS=1`, deploy on .162 ONLY, after a read-only
SimMode-ON screenshot proof per the brief) — or the AGENT_BACKTEST
engine's simulated position if extended. That's the next cycle's
B3 proper: SimMode verify → build/deploy order-path DLL to dev →
backtest_signals entry w/ long-lived exit → DRYRUN→now LIVE TSTOP
line + bracket-cancel proof.
.61 untouched throughout; restart/Auto-Trading = Jeremiah.
Sierra touched this cycle: .162 (DLL swap w/ sha verify, restart).
