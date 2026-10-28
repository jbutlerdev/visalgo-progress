# 2026-10-28T2250Z — tstop cancel-**selection** unit: 10/10 PASS — the safety-critical "which brackets die" predicate pinned hardware-free; gate stack now 7+8+15+10 (type: wake, ~15min)

## Item (queue status)
B3 still awaits the SimMode flip / alt-path pick → continued the
hardware-free gate stack (each cycle adds the next port-critical pure
piece). Trigger (2120Z) and parse (2220Z) done; today the
**cancel-selection predicate** — the safety-critical one: a wrong
pick leaves a stray TP/SL working AFTER the market close (a dead
position's bracket could re-open it), or cancels the wrong side.

## `acsil/cancel_test.cpp` (commit 69a2b24; plain g++)
Mirrors the DLL predicate verbatim (`ours && against && attached &&
working`, `oq>=0 ? oq==AGENT_QTY : -oq==AGENT_QTY`, against = pos>0 ?
SELL : BUY). 10 cases ALL PASS:
* long ⇒ BOTH SELL brackets (stop+target) cancelled; short ⇒ both BUY;
* entry-side orders untouched (long never cancels BUY);
* **Sierra sign convention pinned**: `qty = -1` IS ours (the
  negative-quantity branch — easy port miss);
* qty 0/2 not ours; unattached skipped; not-working (filled/dead)
  skipped;
* 5-order mix ⇒ exactly the 2 valid picked;
* **documented by-design behavior**: a stale exit-side qty-1 attached
  order from a PRIOR entry IS cancelled (orphan-clearing on the exit
  side). Scope note: selection has no parent-order check — cancels
  ALL matching exit-side attached orders on symbol+account. Safe
  today (the agent is the sole trader on MESZ26/23064968 and the
  qty-1 + attached + against filters are tight); if a human ever
  hand-trades that account, revisit (would add `ParentOrderID ==
  our entry id` to the predicate). Logged as known-scope, not a bug.

## Gate stack (hardware-free, all green)
1. python contract oracle — 7 ✅
2. C++ trigger logic — 8 ✅
3. C++ sltp parse — 15 ✅
4. C++ cancel-selection — 10 ✅ (today)
5. trade-service behavior on .162 — **the only remaining unknown**,
   pending SimMode (B3 DLL Sim1-pinned, ready to run).
Everything testable without the trade service is now tested. B3's
on-box run will cover the live API interactions (CancelOrder rc's,
BuyExit fill, bracket-fill races) that units can't reach.

Sierra touched: none. Datasets read-only.
