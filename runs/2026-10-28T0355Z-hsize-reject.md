# 2026-10-28T0355Z — H-SIZE formal: REJECTED on S3 (DD binding: −1,254→−2,340) despite S1 = 29× threshold (+$4,380) — falsification #13, mechanism validated, deployment-policy note (type: wake, ≤20min)

vram gate #24: unchanged (Thu ping).

## The pre-registered test (bars locked 0325Z, run as-is)
v2 + ATR-regime sizing: 2× entry when entry-ATR ≥ stream p70, 0.5×
when ≤ p30. Seeds 0–3, cached signals, no new fitting.

| bar | result |
|---|---|
| S1 dPnL ≥ +$150 | **+$4,380 ✓ (29× threshold — largest effect of the program)** |
| S2 ≥3/4 positive | 4/4 (+3,833/+5,616/+4,117/+3,954) ✓ |
| S3 DD-abs no worse (**binding**) | −1,254 → **−2,340** ✗ → **REJECT** |
| S4 recency ≥ 0 | +$1,765 (4/4) ✓ |

**Pre-registered verdict: REJECT.** S3 was made binding after the
H-FRI lesson (test the risk dimension formally, not just PnL) — and it
did its job: the DD failure is *mechanical, not noise*: 2× on high-ATR
days doubles exactly the exposure those days create, and those days
carry the wins (edge is high-vol concentrated — same finding as the
per-year corrections and gap-day result, now triangulating from a third
direction).

## Diagnostic (recorded, not re-litigated — no bar-shopping)
Ratio view: PnL +93% for DD +87% — return/DD is roughly flat, i.e.
sizing is *risk-neutral scaling*, not risk-free alpha; the absolute-DD
constraint is protecting the live account, and the mechanism it
protects against (fat right tail of vol-clustered losses) is exactly
what got amplified. **Deployment-policy note for Jeremiah:** live qty
is capped at 1 by dtc.py anyway, so H-SIZE as specified is
undeployable today regardless; if he ever wants vol-tilted size,
these numbers (+4,380/−2,340 vs +4,717-baseline/−1,254... recompute
before quoting, see file) are on record — that's a capital-policy
decision, not an alpha claim.

**Series disposition:** H-SIZE REJECT = falsification #13. The
mechanism (edge concentrates in high-ATR regimes) is now CONFIRMED as a
*description* from three independent angles (per-year, gap-day, sizing)
— future work uses it for explanation/prioritization (e.g. kill-day
veto refinement targets), not as a live sizing knob.

Repro: ~/work/h_size.py (fixed seed-0 cache path mid-run: sig_cache.pkl
has no _s0 suffix). Sierra: none. Datasets read-only. No code change.
