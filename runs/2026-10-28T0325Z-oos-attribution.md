# 2026-10-28T0325Z — EA-steer reprioritization: OOS pull-forward = **per-session attribution** (17 days × 4 seeds) + one baseline bug caught; H-SIZE pre-registered for next cycle (type: wake, ≤20min)

Per Jeremiah's steer: algorithm-profitability items lead cycles now;
coverage fills leftover minutes. Starting with the promotion-strengthening
OOS work.

## Scope honesty (why not a data refresh today)
The banked tail ends **2026-10-27 16:00 ET** and Wednesday's session
hasn't closed → a re-pull right now adds zero new days. Data refresh
fires tomorrow post-close (18→19 eval days); today's pull-forward value
is **depth**: nobody had looked at WHICH OOS sessions carry the +$36.

## Caught during reconciliation (log-truth fired a third time this week)
My attribution script gave E3 −315/PKG −407 (d −$92) — **contradicting**
the 2000Z result (+$36/+15/+57/−19). Root cause: I'd written E3's trail
as 1.5/1.5; registry E3 is **start 2.0 / step 1.5** (agent_sltp
`2.0 5.0 1.5`) — the exact sltp triple I'd verified live twice. Fixed,
re-ran, result now consistent: **pooled 4-seed d = +$17** (2000Z mean
+$22; difference = per-day grouping arithmetic, same sign/magnitude —
both "≈neutral, slightly positive"). Claim now rests on re-run output,
not memory.

## Session attribution (the new packet content)
Across 17 OOS chop sessions (4-seed mean $): **PKG>E3 on 2 days
(10-06 +38, 10-13 +17), PKG<E3 on 4 (max −22 on 10-16), tie on 11.**
Every |d| ≤ ~$40 — v2's vetoes touch ~1 trade/week in this regime; the
+$17 is a thin positive drift, not a single lucky day. Both variants
negative overall (−424 / −407) — honest regime reminder: the chop tail
is tax-season for everyone; v2's edge remains the high-vol regime.
Promotion packet impact: strengthens the *robustness* claim (no tail
risk concentrated on a day; deltas granular) without inflating the
verdict (still neutral-to-consistent). File: ~/work/oos_attrib.py
(reproducible; uses cached OOS sigs, zero new fitting).

## New pre-registration (EA-steer item 2 — queue discipline now permanent)
**H-SIZE** (next cycle, bars pre-registered before run): ATR-regime
conditioned sizing — hypothesis from the gap-day finding: entries in
HIGH-ATR-regime days carry the edge. Backtest-only policy variant:
size 2× when day-ATR-percentile ≥ 0.7, 0.5× when ≤ 0.3 (qty cap 1 live
⇒ this is a candidate for the DLL's per-chart size param or a future
multi-qty path; claim = backtest economics only).
Bars: S1 mean dPnL vs v2 ≥ +$150 (seeds 0-3) · S2 ≥3/4 positive ·
S3 DD-abs no worse than v2 · S4 recency ≥ 0. Fresh seeds 4-7 confirm if
all pass. If it fails, that's falsification #13, logged.

Sierra: none. Datasets read-only. vram gate #24 unchanged (Thu ping).
