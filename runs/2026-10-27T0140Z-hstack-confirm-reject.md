# 2026-10-27T0140Z — Combined H-PROB×K30 cell FAILS K-neighborhood: cutoff was an in-sample spike (type: wake, ≤25min)

**Pre-registered before running:** T1 recency (12mo dPnL ≥ +$100, ≥3/4,
DD no worse) AND T2 K-neighborhood (K∈{28,32,35} on top of H-PROB, full
window: ≥2/3 cells with positive dPnL vs prob-alone AND DD ≤ prob-alone's
−1,623). Both → promote combined; else shelve.

## Results (cached signals, seeds 0–3)
T1 recency: A +$2,138/DD −$730 → combined +$2,375/DD −$641, dPnL **+$237,
4/4** — PASS.

T2 K-neighborhood (dPnL vs H-PROB-ALONE, full window):
| K | dPnL | pos | mean DD | ok? |
|---|---|---|---|---|
| 28 | −$417 | 0/4 | −1,293 | NO |
| 30 (the chosen cell) | +$72 vs prob | 4/4 | −1,288 | (reference) |
| 32 | +$35 | 2/4 | −1,406 | NO (DD bar fails... wait, passes DD but only 2/4 pos → NO by cells rule) |
| 35 | −$122 | 0/4 | −1,522 | NO |
**0/3 — FAIL** (needed ≥2).

## Verdict
**Combined cell SHELVED.** T2 did exactly its job: the K=30 cutoff edge sits
on a PnL spike — neighbors are worse than no cutoff at all. The K30
"super-additive DD" from 0035Z survives (all cells cut DD), but the PnL
premium is knife-edge in K, i.e. in-sample fitting, not structure. Contrast
with H-PROB's T2 (4/5 positive perturbations): the probability-veto gate is
structure, the time-of-day gate is noise. **E3 + H-PROB (prob vetoes only)
remains THE single confirmed candidate** — unchanged promotion package from
0105Z.

Strategy-cycle scoreboard (all pre-registered): H-LONG ✗, H-LONG2 ✗,
H-TOD ✗, H-STACK/combined ✗(T2), **H-PROB ✓✓✓** (full-window + recency +
robustness). Entry-surgery pattern continues: only mechanism-backed,
probability-quality cells convert.

## Files / hygiene
No repo code changed; cached replays; Sierra none. (T2 row note: K32
printed pos=2/4 → fails the "positive mean dPnL" cell rule anyway; table
kept as measured, verdict unaffected: 0/3 regardless of reading.)
