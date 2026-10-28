# 2026-10-28T1655Z — DLL reconnaissance done + the B3 contract oracle written BEFORE the port: 7 tests pin maxbars semantics (60 ml tests green); B2 patch design finalized for the next dedicated cycle (type: wake, ~20min)

## Contract-first (the right order for a live-money port)
`ml/test_timeslot_contract.py` — the Python oracle the C++ fw24 patch
will be tested against:
1. maxbars=None ⇒ runs to last bar (eod);
2. maxbars=1 ⇒ exit at bar-0 close;
3. **time-stop cuts the bar stream** at the index (a bar-5 spike is
   never seen; exits at bar-4 close — pins "close at bar maxbars−1");
4. TP preempts the stop; 5. SL preempts the stop;
6. trail armed but time-stop still closes at its bar;
7. **the OFF-semantics bridge**: C++ 0=OFF vs Python None=OFF — the
   conversion helper is pinned (raw 0 in Python is a bug: empty
   slice), guarding the exact seam where a port would go wrong.

## B2 reconnaissance (reading the deployed code, no edits yet)
* sltp parse: AgentFrame.cpp:2115 (agent_sltp.txt "slm tpm [trailm]",
  3-field fscanf) — 4th field maxbars extends it cleanly;
* trail machinery :2198-2250 (per-bar block already has barKeyT,
  g_AgTrDay, GetOrderForSymbolAndAccountByIndex + ModifyOrder);
* **key structural finding:** exits are SERVER-SIDE attached brackets
  (Target1Offset/Stop1Offset on the entry order) — so the time-stop is
  NOT just a close: the fw24 block must (a) find BOTH attached orders
  (existing loop finds the STOP only), (b) `sc.CancelOrder` them, then
  (c) market exit via `sc.BuyExit/SellExit` (both confirmed present:
  headers :2770 + NqAmtAgent SimExit pattern). Bar-counting:
  (nowMin−entryMin)/5 within g_AgTrDay — entries are intraday-first-
  cross so the stop always lands same-day; matches harness slices.
* Effort update: ~90-120 lines (bracket-cancel is the extra vs the
  30-60 estimate). **Deferred to a dedicated cycle** per plan
  ("checkpoint long work") rather than half-patched in 10 minutes.

## Suite
ml discover **60 OK** (was 53; +7 contract), sc_client 8 OK.
Branch: algo-dev/v4-activation (contract tests committed on top).

Sierra touched: none. Datasets read-only.
Next: B2 dedicated cycle (patch w/ bracket-cancel + mingw cross-
compile + default-build parity) — then B3 runs the same 7 semantics
against the DLL on .162. 21:30Z OOS refresh + GPU study remain armed.
