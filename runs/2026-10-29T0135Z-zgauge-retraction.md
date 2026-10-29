# 2026-10-29T0135Z — **RETRACTION: the live forward-test PnL was false precision.** The activity log cannot produce trustworthy PnL; gauge rewritten to report only what's trustworthy (fills/RT counts, fee decomposition, raw NLV). −$304/−$18/1σ reads retracted (type: wake, ~22min)

## How it came out (started as a bugfix)
Chasing the z-gauge's known flow-detection gap (est2 gave −140 vs
manual −304), the raw dump exposed the real problem: **NLV swings of
±$300 between sessions while Change fields stay fee-multiples**
(10-20: NLV −324.52 w/ change −14.52; 10-21: −258.79 w/ −9.04;
10-16/17: +161/+310). Trading at $5/pt on MES cannot produce those
swings from 2-3 round-trips; the Balance: field is cash-side (moves
with deposits AND margin), so the flow heuristic fabricated phantom
flows. Neither sum(Change) nor NLV-continuity is a PnL estimator
here. (Also corrected inline: an interim "FLOW-SUSPECT >150" heuristic
was itself dropped — a +161 NLV jump can be legitimate PnL.)

## Retracted (with their runs noted)
* 1455Z: "live forward −$304/14 sessions" + "≈1σ adverse vs −$78
  expected" (manual calc, same defect: NLV endpoint diff w/ partial
  flow correction);
* 1925Z/2155Z: −$304 restatements & "cumulative ≈ −$18" tail reads;
* 1545Z: z-gauge est1/est2 z-scores as PnL verdicts.
**What SURVIVES (unaffected):** measured fee $2.26/RT (k×2.26
decomposition — fee fields ARE reliable); RT/fill counts (20 RTs in
the agent era — real trading IS happening on the account); the whole
backtest/confirmation edifice; v4 approval; the OOS tail results
(from parquet data, not these logs).

## What the gauge says now (and a test pins it)
`VERDICT: fills occur on live account (count-based). Trading PnL:
UNKNOWN-FROM-THIS-SOURCE -> use Sierra Trade Tracker / official
reports (queued).` Test asserts no PnL z can ever be printed again.

## Replacement path (queued, next cycles)
Proper realized-PnL source, in order of preference: (1) Sierra Trade
Tracker window on .61 via sierra-capture + parse; (2) DTC
trade-history request type (new msg in sc_client — dev-box work);
(3) broker/official statements if Jeremiah can pull them. Until then:
NO live-PnL claims, forward test judged on fills-existing + the
backtest's expectations only.

Suites: 37 ml + 8 sc_client OK (new honesty test included).
Sierra touched: none (local analysis of previously-pulled copies).
