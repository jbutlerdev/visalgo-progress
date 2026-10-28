# 2026-10-28T0805Z — H-ATRMIN: hypothesis NOT SUPPORTED by scan → no formal run (declined), but the ATR-decile table lands a 4th independent triangulation of high-vol concentration (type: wake, ≤15min)

vram gate #31: unchanged (Thursday ping next cycle if silent).
Live .61: not checked (overnight quiet hours; last read 0010Z healthy).

## Pre-registered flow worked as designed
Hypothesis (stated before scan): micro-ATR entries are cost-dominated
(TP≈5×ATR barely over $2.50 round trip) → bottom deciles negative →
ATR-floor candidate. **Scan (seeds 0–1, counting/means only) says NO:**
bottom deciles are POSITIVE (d0 mean +$8.3, d1 +$7.2). The negatives
are mid-distribution (d3 −$7.0/neg-tot −751, d4, d6) — no floor, and
vetoing scattered mid-deciles would be multiple-comparison cherry-
picking dressed as a mechanism. **No formal pre-registration filed;
candidate declined at scan stage** (cheapest possible kill: 20 min,
no bar erosion, scoreboard stays 3C/16F honestly).

## What the table is worth (recorded as diagnostic, not candidate)
PnL by entry-ATR decile (2 seeds, ~1,080 trades): **top decile alone
carries ≈+$4,790 of ≈+$10.7k pooled — ~45% of ALL PnL from 10% of
trades**; d7–d8 also strong (+$2.0k/+2.4k). This is the **4th
independent angle** on the same mechanism (per-year 2025/26
concentration, gap-day preference, H-SIZE DD-mechanics, now ATR-decile
dose-response). Monotone-with-noise: mean PnL rises with ATR except
where chop grinds mid-vol. Useful for: (a) kill-day/veto refinement
prioritization, (b) explaining package behavior to Jeremiah, (c) if a
crash-like OOS window ever arrives, this predicts where the wins
cluster. NOT useful as a live knob (H-SIZE already falsified
ATR-conditioned exposure; the absolute-DD constraint is the reason).

## Discipline notes
- Both HYPOTHESIS-GENERATION cycles so far (zone→MIXED, this→declined)
  cost <25 min and produced either a review item or an honest no-run;
  queue policy validated.
- No bar-shopping: could have pre-registered "veto d3+d4+d6" after
  seeing the table (would likely "pass" discovery on informed seeds) —
  explicitly declined; if anyone wants that tested, it needs fresh
  streams + pre-registration from a stated mechanism, which none has.

Sierra: none. Datasets read-only. No code change. Repro:
~/work/h_atrmin_obs.py. OOS refresh armed 21:30Z.
