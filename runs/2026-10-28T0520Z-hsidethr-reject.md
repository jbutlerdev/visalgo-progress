# 2026-10-28T0520Z — H-SIDETHR formal: REJECTED 0/4 bars (dPnL −$2,656; DD WORSE too) — mid-confidence shorts are profitable AND hedge long-side drawdown; calibration lane closed for now (#16) (type: wake, ≤15min)

vram gate #26 (Wed): unchanged — Thursday ping due next cycle if silent.
OOS refresh armed for tonight post-20:00Z close (18th day).

## Pre-registered test (bars locked before run; one cell only per
multiple-comparisons rule)
Side-conditional threshold: SHORTS' thr 0.45→0.50 (longs unchanged) —
the calibration-lane cell with the strongest prior (chop shorts bleed).
Seeds 0–3, cached signals, v2 otherwise unchanged.

| bar | result |
|---|---|
| C1 dPnL ≥ +$150 | **−$2,656 ✗** (all 4 seeds negative) |
| C2 ≥3/4 positive | 0/4 ✗ |
| C3 DD-no-worse | **−1,254 → −1,798 ✗ (worse!)** |
| C4 recency ≥ 0 | −$512 (0/4) ✗ |

**Verdict: REJECT — falsification #16, clean sweep.**

## The informative part
Expected: removing chop-bleed shorts → DD improves, PnL ~flat.
Actual: removing them **both** loses money **and deepens DD** by $544.
The mid-confidence (0.45≤p<0.50) shorts are *dual-purpose*: individually
 profitable AND structurally hedging the long book's drawdown — which
 is presumably WHY the uniform-thr sweep (0940Z) found 0.45 the overall
 interior optimum: the side x thr cross isn't exploitable by trimming
 either side. The kill-day vetoes (a *different* side-conditional rule,
 confined to p∈(0.55,0.60] shorts on kill-days) remain the correct
 surgical instrument; blunt side-trimming is not.

**Calibration-lane disposition:** the mirror cell (longs' thr 0.50) was
pre-declared exploratory-only if primary passed — primary failed
decisively, mirror NOT run (no bar-shopping; expected-value of the
mirror given this result ≈ the same mechanism in reverse, and the
uniform sweep already covers the aggregate). Lane stays open only for
methods that ADD information (new features, richer models), not
threshold surgery on existing probs.

Layer/axis map now: entry (sides/times/gaps/fades/thr/bands/side-thr
cross), exit (trail/TP/SL/TS), capacity, exposure/gates, sizing,
label-shape — all closed. Remaining lanes: feature ADDITIONS (heavy,
fold-honest engineering), LSTM (vram-blocked). v2-GO / v3-DLL unchanged.

Sierra: none. Datasets read-only. No code change. Repro: ~/work/h_sidethr.py
