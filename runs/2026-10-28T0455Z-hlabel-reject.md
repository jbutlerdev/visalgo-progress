# 2026-10-28T0455Z — H-LABEL formal: REJECTED catastrophically (label/exit alignment at live sltp 2.0/5.0 collapses trades 666→108, PnL +143 vs +6,863) — falsification #15; harness seed-wiring bug self-caught (type: wake, ≤25min)

vram gate #26 (Thursday ping next cycle if silent).

## The pre-registered test (bars locked before run)
The train-label shape (slf=1.5, tpf=2.5) ≠ live exit system (SL 2.0 /
TP 5.0 + trail). Hypothesis: align labels to live sltp (2.0, 5.0),
retrain (fresh fits, ~96 s/seed CPU), replay v2 rules UNCHANGED (thr
0.45 uniform — per-cell retune pre-declared as multiple comparisons;
trade-count side-effects pre-declared as diagnostic-only).

| bar | result |
|---|---|
| L1 dPnL ≥ +$150 | **−$6,700 mean ✗ (fails by ~40×)** |
| L2 ≥3/4 | 0/4 ✗ |
| L3 DD | passes (−685 vs −1,279) — trivially: almost no trades |
| L4 recency | moot (collapsed) |

**Verdict: REJECT — the most decisive of the program.**

## The finding (label shape is load-bearing)
(2.0, 5.0) labels are too hard to resolve within the label horizon: the
asymmetric payoff rarely touches TP before the horizon → most labels
flatten to hold/0 → argmax almost never clears 0.45 → **108 trades vs
661–666**. The harness's (1.5, 2.5) isn't an arbitrary knob — it's a
signal-density sweet spot. Positive control: DD "improves" to −685
purely by not trading (the neutral-by-inactivity pattern again).

**Self-caught harness bug (recorded):** my script set `W.SEED=0` once,
so the four "seeds" are byte-identical (all +143/108/DD−685) — the
per-seed d spread came only from the cached v2 baselines. NOT re-run:
rescue would need a +$6,700 swing against a 40×-threshold failure;
pre-registration covers reporting as-is. (Cached-stream generators set
SEED per seed — pattern noted for any future fresh-train experiment.)
Also fixed mid-run: `build()` mutated `P.FEAT_PREFIX`, breaking the
second seed's `build_dataset` dropna — prefix reset added.

**Layer map:** label-shape axis CLOSED (previously flagged as the
likely next lane at 0420Z; now falsified from the alignment direction).
Remaining: feature ADDITIONS (heavy), LSTM (vram-blocked). Both
open decisions unchanged (v2 GO / v3 DLL), queue healthy.

Sierra: none. Datasets read-only. No code change. Repro: ~/work/h_label.py
