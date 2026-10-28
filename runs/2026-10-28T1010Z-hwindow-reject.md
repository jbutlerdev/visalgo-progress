# 2026-10-28T1010Z — H-WINDOW formal: REJECTED both cells catastrophically (60d −$8,390 / 120d −$6,017 vs registry 90d) — falsification #17; registry confirmed joint optimum on ALL harness knobs; my "shorter adapts faster" prior inverted (type: wake, ≤25min)

vram gate #35: unchanged (Thu ping next cycle).

## Pre-registered test (bars locked before run; H-CAP methodology)
Last untouched harness axis: TRAIN_DAYS=90. Cells 60/120, fresh
training seeds 0–1 per cell (W.SEED per seed — H-LABEL lesson applied;
FEAT_PREFIX reset — h_label lesson applied), pkg-standard replay
(noFri both arms), cached signals baseline. C1 ≥ +$150 / C2 both seeds
positive / C3 DD-no-worse.

| cell | dPnL | DD |
|---|---|---|
| TRAIN_DAYS=60 | **−$8,390** (−7,619/−9,161) | −1,402 → −5,508 |
| TRAIN_DAYS=120 | **−$6,017** (−5,118/−6,916) | −1,402 → −2,762 |
| registry 90d | — (baseline) | −1,402 |

**REJECT both = falsification #17.** No expansion beyond 2 seeds/cell
(rule: expand only on signal — there was negative signal at 40–60×
the bar; spending seeds 2–3 would be waste, not rigor).

## What this settles
* **Registry is now the confirmed joint optimum on every harness
  dimension tested:** model capacity (H-CAP: depth/lr/n_est), label
  shape (H-LABEL), window length (this), plus all entry/exit/exposure/
  sizing/side cells. The harness configuration is not tunable further
  without new information — only feature additions or model family
  (LSTM, vram-blocked) remain.
* My stated mechanism prior (shorter window → faster regime adaptation,
  given the high-vol concentration findings) was **wrong in both
  directions**: 60d is the WORST (too little data per fold — ~30
  bars/day × 60 days ≈ 1.8k bars vs 90d's ~2.7k, below what the 3-class
  problem needs), 120d staler AND DD-deepening. 90d is genuinely the
  interior optimum, not an accident. (Positive control: DD degrades
  monotonically with distance from 90 — same shape as the PnL story.)
* Both fresh-train lesson-scripts (SEED, FEAT_PREFIX) worked; cached
  win60/win120 sigs kept for reuse.

Sierra: none. Datasets read-only (MANIFEST-verified yesterday). No code
change. Repro: ~/work/h_window.py. Scoreboard 3C/**17F**/1N.
