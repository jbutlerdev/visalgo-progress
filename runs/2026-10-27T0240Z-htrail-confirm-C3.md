# 2026-10-27T0240Z — H-TRAIL CONFIRMED: E3 + H-PROB + trail(1.75/1.75) passes all 4 pre-registered bars — promotion package upgrade (type: wake, ≤25min)

**Pre-registered battery (rules written this cycle before running):** cells
C1(1.75,1.5) / C2(2.0,1.75) / C3(1.75,1.75), each ON TOP OF H-PROB vetoes;
priority diagonal-first (C3→C1→C2). Bars: S1 streams (mean dPnL vs HP
≥+$100, ≥3/4), S2 recency-12mo (dPnL vs E3-12mo ≥+$75, ≥3/4), S3 DD no
worse than HP (−1,623), S4 anti-knife-edge perturbation of chosen cell >0.

## Results (cached signals, seeds 0–3, full window; HP = E3+H-PROB mean +$4,982 / DD −1,623)
| cell | dPnL vs HP | pos | d12mo vs E3 | pos12 | mean DD | S1 | S2 | S3* |
|---|---|---|---|---|---|---|---|---|
| C1 (1.75,1.5) | +147 | 4/4 | +233 | 4/4 | −1,410 | ✓ | ✓ | ✓(−1,410 better) |
| C2 (2.0,1.75) | +256 | 4/4 | +554 | 4/4 | −1,683 | ✓ | ✓ | ✗(−1,683 worse) |
| **C3 (1.75,1.75)** | **+331** | **3/4** | **+520** | **4/4** | **−1,486** | ✓ | ✓ | ✓(−1,486 better) |

S4 for C3: perpendicular pert (1.625,1.75) vs HP = **+$203 (3/4 positive)**
→ plateau, not spike. (Diagnostics: C1-pert +147; C2-pert −34 — consistent
with C3 being the slope-target.)

**VERDICT: C3 CONFIRMED.** Full-package expectation vs E3 baseline:
**+$794 mean (+18%), maxDD −1,820→−1,486 (−18%), recency-12mo dPnL vs E3
+$520 4/4.** Exit-layer structure is real (trail timing, mirror of
H-PROB's probability-quality structure).

## Honest hiccup (caught and disclosed, same cycle)
My S3 implementation inverted the comparison: with DD stored negative,
`m_dd <= hp_dd` PASSES worse DD and FAILS better DD — it would have
selected C2 (DD −1,683, actually worse) and rejected C3/C1 (both DD-better).
Caught on readout before selecting. The pre-registered prose bar said "no
worse than HP" — intent applied; corrected scoring is what this log reports.
(Effect on battery: none beyond correcting the flags; all S1/S2/S4 numbers
unaffected.)

## Promotion package (v2, for Jeremiah) — supersedes 0105Z single-filter spec
**E3 + H-PROB + trail(1.75/1.75)**:
1. Entry (first-cross): SHORT 0.55<p≤0.60 → HOLD day; LONG p>0.60 → HOLD
   day (kill-day, NOT continue-scan).
2. Exits: SL 2.0 ATR / TP 5.0 ATR; trail trigger **1.75** ATR, step **1.75**
   ATR (fw30: agent_sltp.txt "1.75 5.0 1.75"; DLL already parameterized —
   no recompile needed, file-driven).
Evidence: full-window +$794 4/4-stream-consistent (3/4 strict on the stacked
cell), DD −18%, Sharpe chain 1.19→1.38 (H-PROB) → stacked cell measured per-
seed; recency-12mo +$520 vs E3, 4/4. Caveats unchanged: filters located
in-sample (forward test = true OOS); S4 covers one perpendicular direction.

## Next (queued)
- Append confirmations to ml/CANDIDATE_hprob_bandgate.md (rename scope
  CANDIDATE_e3_filters) + fw30 implementation note on request/approval.
- Optional: seeds 4–7 robustness on the final cell only (cheap, cached) as
  belt-and-braces before Jeremiah review.
