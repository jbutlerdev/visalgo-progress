# 2026-10-27T0105Z — H-PROB CONFIRMED on pre-registered recency + band-robustness tests (type: wake, ≤25min)

**Pre-registered before running (this cycle):** T1 recency — dPnL over last
12 months ≥ +$75 mean, ≥3/4 streams positive, DD no worse. T2
band-neighborhood — 5 alternative band-edge cells, ≥4 must have positive
mean dPnL (full window). Both required for confirmation; either → demote.

## T1 — recency (2025-10-27..2026-10-02, seeds 0–3)
A mean +$2,138 / DD −$730 → H-PROB mean **+$2,351 / DD −$639**;
mean dPnL **+$213, 4/4 positive**. PASS.

## T2 — band neighborhood (full window, seeds 0–3, mean dPnL)
| alt cell | dPnL | pos |
|---|---|---|
| short band widened low (0.50,0.60] | **−1,389** | 0/4 |
| short band widened high (0.55,0.65] | +260 | 4/4 |
| short band narrowed (0.55,0.58] | +84 | 4/4 |
| long veto lowered >0.55 | +498 | 4/4 |
| long veto raised >0.65 | +351 | 4/4 |
**4/5 PASS** (threshold ≥4/5).

The single failing cell is *informative, not damaging*: widening the short
veto down to 0.50 also vetoes short (0.50,0.55] — the single BEST bucket in
the whole entry population (+$40.7/tr, +$2,114 seed-0). So the result
confirms the gate's structure is real: there genuinely is a good band
(0.45–0.55] below the veto zone, and the 0.55 lower edge is load-bearing,
not arbitrary. Widen-high/narrow/long-edge perturbations all stay positive
(0.60 upper edge is a plateau, mildly conservative).

## Verdict
**H-PROB CONFIRMED as backtest candidate** — pre-registered full-window
bars (2220Z: +$495, 4/4, DD bar) + recency (this run) + robustness proxy.
Remaining honest caveat, unchanged: bands were located in-sample; T1 tests
recency, T2 robustness — the true selection-OOS is the forward test.

## Promotion package (for Jeremiah) — candidate spec
- Filter (in the agent's first-cross decision): if argmax=SHORT and
  0.55 < p ≤ 0.60 → HOLD day; if argmax=LONG and p > 0.60 → HOLD day.
  **Kill-day semantics (do NOT continue scanning after a vetoed cross —
  skip-continue measured −$228).**
- Expected effect (4y, 4 streams): +$495 mean (+11%), maxDD −1,820→−1,623,
  Sharpe 1.19→1.38; last-12mo: +$213, DD −730→−639.
- Candidate doc: ml/CANDIDATE_hprob_bandgate.md (branch
  algo-dev/hprob-bandgate; will append confirmations on request).
- Optional additive, NOT yet confirmed: K30 late-cutoff (H-STACK 0035Z:
  combined +$567/DD −1,288/Sharpe 1.55, exploratory only).

## Files / hygiene
No repo code changed; cached-signal replay only; Sierra none.
