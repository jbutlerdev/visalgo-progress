# 2026-10-28T0625Z — **H-ZONEVETO CONFIRMED** (fresh streams 4–7: 4/4, +$457, DD −1,732→−1,418) + composition: **v4 = v2+Z+TS54 composes (TS marginal +$562 4/4; vs E3 recency +$522 = best on record)** (type: wake, ≤25min)

vram gate #28: unchanged (Thursday ping armed next cycle).

## Confirm (pre-registered at 0550Z; same locked bars; seeds never seen)
| | discovery (0–3) | confirm (4–7) |
|---|---|---|
| dPnL | +$469 (4/4) | **+$457 (4/4)** |
| DD | −1,254→−1,168 | **−1,732→−1,418** |
| recency | +$137 4/4 | +$88 4/4 |
| vetoed | ~32/seed | ~32/seed |

Magnitude, sign, DD direction, AND veto-count replicate on unseen
streams — **strongest replication of the program** (3rd CONFIRMED:
E3 baseline, H-PROB/v2, now H-ZONEVETO; scoreboard 3C/16F/1N).

## Composition (the strategic result)
v4 = v2 + ZVETO + TS54 (v3's time leg):
* TS54 marginal ON TOP of v2+Z: **+$562, 4/4** — bigger than its +$302
  on plain v2 ⇒ the mechanisms are **complementary** (zone-5 shorts that
  would run long get both vetoed AND time-capped independently);
* **v4 vs E3 recency(12mo): +$522, 4/4** — supersedes v2's +$481 and
  v3's +$491: **best recent-era delta on record**;
* OOS chop tail: d = **exactly $0.0 (4/4)** — zone-5 shorts never open
  in chop ⇒ neutral-by-inactivity (third instance; zero-information,
  reported as such, not counted as a win).

## Honest caveats (in the doc too)
Seed 8 (9th stream) not yet run on ZVETO — next cycle extends to 9/9
like we did for v2/v3. CPU-convention pending GPU parity. Scan used
seeds 0–1 (confirm seeds are the true test). n≈32 vetoes/seed but
replicated across 8 streams. DLL expectation: gating-only reuse of
live zone_c (VERIFY before claiming — next cycle reads the acsil source).

## What this changes for Jeremiah's decision stack
Three separable review items now, each independently decidable:
1. **v2** (prob vetoes + trail) — GO/no-GO, staged;
2. **v3** (v2+TS54) — needs DLL work approval (contract = maxbars spec);
3. **v4** (v2+Z+TS54) — best package on record; needs Z-veto DLL check
   (likely gating-only) + same activation interlocks. If approving all
   three, v4 ⊃ v2 ⊃ ... — recommended end-state is v4, but v2 alone
   still fully stands as a decision today.

Branch `algo-dev/zonenveto` (`f27cbfc2`) with CANDIDATE_zoneveto.md.
Sierra: none. Datasets read-only. No prod change. Repros:
h_zone_obs / h_zoneveto / h_zoneveto_confirm / h_zoneveto_extra.
