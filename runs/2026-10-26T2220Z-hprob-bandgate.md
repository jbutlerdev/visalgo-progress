# 2026-10-26T2220Z — H-PROB side-conditioned band gates: FIRST POSITIVE CANDIDATE (+$495, 4/4 streams) (type: wake, experiment)

**Hypothesis (pre-registered 2140Z):** two per-trade-negative entry cells —
SHORT prob (0.55,0.60] (−$11.7/tr) and LONG prob >0.60 (−$21.7/tr) — are
pure drag; vetoing them raises PnL AND cuts DD. Success bars (paired per
stream): mean dPnL ≥ +$150 AND ≥3/4 positive AND mean maxDD no worse.

## Design note — veto semantics were the whole ballgame
2140Z's path-dependence finding predicted that *how* you veto matters. Two
variants tested:
- **skip** (continue scanning later bars after a veto) → mean **−$228**, 0/4
  positive. Late-day re-entries are worse trades (same trap as H-LONG2).
- **kill** (stand down the day at the vetoed first-cross) → the winner below.
Production implication: implement as HOLD-the-day, not continue-scan.

## Results (kill semantics, seeds 0–3, cached signals, identical exits)
| seed | A pnl | A maxDD | A Sharpe | kill pnl | kill maxDD | kill Sharpe | dPnL |
|---|---|---|---|---|---|---|---|
| 0 | +4,255 | −1,607 | 1.13 | +4,717 | −1,410 | 1.32 | +462 |
| 1 | +4,796 | −1,906 | 1.25 | +5,374 | −1,708 | 1.47 | +578 |
| 2 | +4,874 | −1,960 | 1.29 | +5,301 | −1,762 | 1.47 | +427 |
| 3 | +4,021 | −1,809 | 1.07 | +4,535 | −1,612 | 1.26 | +515 |
| **mean** | **+4,487** | **−1,820** | **1.19** | **+4,982** | **−1,623** | **1.38** | **+495** |

All three pre-registered bars PASS (dPnL +495 ≥ 150; 4/4 positive; DD
−1,623 vs −1,820). Single-cell controls: long-veto alone +$228 (DD flat),
short-band-veto alone +$267 / DD −197 — additive, distinct mechanisms.
Trades 568 → 538 mean (the 30 vetoed trades per stream net −$495... the
vetoed population's own PnL, exactly the negative cells).

## Verdict
**ACCEPTED as backtest candidate** `H-PROB` (first positive of the strategy
cycle). ml/CANDIDATE_hprob_bandgate.md on branch `algo-dev/hprob-bandgate`
(commit pushed; master untouched — live E3/fw29 unchanged, promotion needs
Jeremiah). Registry row in the candidate doc.

## Caveats (honest)
- Gate bands were located on the SAME 4y window (in-sample selection of the
  gate itself; forward-test is the OOS confirmation, same status as every
  prior candidate row incl. E3's own exit-layer scan).
- Cells are thin (30 trades/stream); stream-consistency is the evidence.
- Band edges not swept (deliberate: extra sweep = extra selection freedom).
- **Process hiccup (caught mid-run):** first sweep wrongly applied the veto
  in the control column — the "A" numbers on the buggy pass were actually
  kill-variant numbers. Caught because kill-vs-A (+$462) exactly matched the
  seed-0 bucket table (−$461 on the vetoed cells = removing them adds it
  back); re-ran with fixed control. Same numbers' sanity is double-confirmed
  by the bucket arithmetic.

## Files
- trades: runs/data/2026-10-26T2220Z-hprob_skip_s0.csv (kill variant in
  ml/out private + equity curve below)
- Sierra: none. No dataset writes.

## Next
1. H-PROB forward-test readiness checklist (same one E3 went through).
2. Next hypothesis queue: time-of-day gate — EOD-exit trades were +$35/tr
   (TP too far for late entries?) and entry_bar p50=4 suggests early edge;
   test "no new entries after bar 41→30 (11:15→10:30)" kill-day variant +
   H-PROB stacked, vs H-PROB alone.
