# 2026-10-28T0745Z — H-TSSIDE formal: TS54's confirmed effect is **entirely long-side carried** (L-only +$378 ≈ global +$398; short-only +$20 ≈ inert) — short-only simplification REJECTED (E1/E2/E4/E5 fail); global TS stays the spec (type: wake, ≤20min)

vram gate #30: unchanged (Thursday ping next cycle).

## Pre-registered test (bars locked before run; seeds 0–3, pkg-standard,
cached signals)
Hypothesis (mine, stated upfront): TS54 is short-side-carried (shorts
bleed past bar 54) → short-only time-leg would match global and
simplify the DLL. **Result: hypothesis inverted.**

| leg | dPnL vs v2 | DD |
|---|---|---|
| TS global (confirmed spec) | +$398 (4/4) | −1,189 |
| **TS on LONGS only** | **+$378 (4/4)** | −1,250 |
| TS on SHORTS only | +$20 (2/4) | −1,395 |

Bars for the short-only candidate: E1 +20<150 ✗ · E2 2/4 ✗ · E3 DD passes (−1,395 vs −1,486) ✓·
E4 recency −42 ✗ · E5 |S-only−global| = $378 > $50 ✗ → **KEEP GLOBAL
TS** (pre-registered outcome).

## Why this is worth the cycle even without a new candidate
1. **Mechanism corrected (was never tested — 5th instance of
   "confirmed-but-unexamined dimension"):** the time-stop works because
   LONGS that go nowhere by bar 54 get closed (dead-money release +
   avoids their fade), while shorts resolve via trail/TP/SL on their
   own. My "shorts bleed" story was wrong; the data says longs do.
2. **DLL-effort note for Jeremiah's v3/v4 review:** if he ever wants
   the MINIMAL port, the decomposition now on record says **long-only
   TS ≈ global within $20** (short leg contributes ≈0 PnL but global
   still holds the best DD −1,189) — so global remains the
   recommendation; long-only is a documented fallback, short-only is
   off the table.
3. Consistency: TS-global +$398 here exactly reproduces the 1935Z
   discovery figure (seeds 0–3) on the pinned pkg-std harness — the
   retraction-cycle harness fix now cross-validates old results.

Sierra: none. Datasets read-only. No code change. Repro:
~/work/h_ts_side.py. OOS refresh armed 21:30Z tonight.
