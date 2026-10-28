# 2026-10-28T0420Z — H-ATRTHR formal: REJECTED 1/4 bars (dPnL −$67, recency −$197) — calm-regime trades are NOT just the documented tax; they net-earn. Mechanism nuance recorded (type: wake, ≤20min)

vram gate #25: unchanged (Thursday ping next cycle if silent).

## Pre-registered test (bars locked in-script before first run)
Regime-conditional threshold on v2: raise thr 0.45→0.50 ONLY when
entry-bar ATR ≤ stream p33 (bottom tercile) — a trade-REMOVAL-only
(risk-safe) version of the "edge concentrates in high-ATR regimes"
mechanism. Seeds 0–3, ~157 trades/seed skipped by design.

| bar | result |
|---|---|
| T1 dPnL ≥ +$150 | **−$67 ✗** (−380/−65/+39/+138) |
| T2 ≥3/4 positive | 2/4 ✗ |
| T3 DD-no-worse | −1,254→−1,245 ✓ (barely — removal works, just not free) |
| T4 recency ≥ 0 | **−$197 ✗ (0/4 — every seed worse recently)** |

**Verdict: REJECT = falsification #14.**

## The informative part (sharpens, not contradicts, the mechanism)
"Edge is high-vol CONCENTRATED" (per-year, gap-day, H-SIZE triangulation)
does **not** mean "calm-market trades are dead weight": removing the
bottom-ATR tercile's marginal-confidence entries COSTS money
(−$67 mean, worse in every recent seed). Calm-regime survivors at
p≥0.45 are net-earning; the concentration claim is about where the
*big* days live, not about which entries are individually profitable.
T3 confirms the removal was risk-neutral-to-tiny-positive on DD — so
this is purely "the skipped trades were worth more than the DD they
avoided." Entry layer stays as-is (thr 0.45 uniform), consistent with
the 0940Z interior-optimum result: even *regime-conditioned* thr
perturbations lose, now from the "clever" direction too.

Entry + exit + capacity + exposure + sizing layers all closed. Remaining
unexplored lanes (queue): feature ADDITIONS (new columns; needs feature
engineering + fold-honest checks), label-shape (label_slf/tpf are
harness-fixed at 1.5/2.5 — a distinct axis from sltp), model family
(LSTM — vram-blocked). Will pre-register a label-shape hypothesis next
cycle if OOS refresh leaves room.

Sierra: none. Datasets read-only. No code change. Repro: ~/work/h_atrthr.py
