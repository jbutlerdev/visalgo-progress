# PRE-REGISTRATION — UTC18 fade-window hypothesis (NQ 5m)

Status: DRAFT v1 (this file is the pre-registration; any post-results
edit must be a NEW section, never an edit of sections 1-6)
Data: signed-off corpus (roll #18), bars as-is; roll-exclusion pass
as in baseline_h1_boot_noroll.json (quarter-start 288-bar trims).

## 1. Hypothesis (single, falsifiable)
After a DOWN 5m bar during UTC 18:00-18:55 (13:00-13:55 ET band),
buying the next bar open and exiting at fixed holding time H has
positive mean net PnL per trade; after UP bars, no entry (symmetric
fade NOT claimed).

## 2. Primary metric
mean_net_pts = mean(fwd-H-point PnL − COSTS) per trade, COSTS =
0.50 pts (NQ half-spread+slip estimate, fixed ex ante).

## 3. Decision rule
PASS iff day-block bootstrap (B=1000, seed 424242, block=trading
day, quarter-start trims per section Data) CI95 lower bound > 0 on
mean_net_pts over the FULL 2021-03→2026-03 corpus. One H chosen
ex ante: H = 12 bars (1h), motivated by probe-530/531 h1-only
finding being the tested cell, no H sweep permitted.

## 4. Splits (descriptive only, cannot flip PASS)
year-by-year table; first-half vs second-half sign check (a sign
flip on the 2nd half is logged as CONCERN and requires Jeremiah
sign-off before any live-track use, even if aggregate PASSes).

## 5. Multiple-testing budget
This document spends the ENTIRE hour-of-day family budget (hours
15/16/17/19 were tested and failed; re-testing them here is
forbidden). One hypothesis, one metric, one H, one seed.

## 6. Deviation protocol
Any deviation (data change, metric change, H change) = new pre-reg
number (v2), old version kept immutable, and v1 results remain
reported as run.

---
## 7. RESULTS (appended 2026-11-13T22:30Z per deviation protocol — sections 1-6 untouched)
Executed exactly as pre-committed (script mirrors spec; result JSON:
prereg_utc18_fade_result.json). n_trades=6,510 over 1,141 days.
mean_net_pts = +1.347, day-block boot CI95 [-1.882, +4.424] ->
**CI INCLUDES ZERO -> **FAIL** (PASS rule = CI lower bound > 0).
Descriptive (cannot flip verdict): half1 +2.27 / half2 +0.445,
sign_flip FALSE (direction persists but decays); by-year means
2021 +4.105, 2022 +2.042, 2023 +0.145, 2024 -0.478, 2025 -1.559,
2026(partial) +15.491. Reading: point estimate positive but CI
far too wide (n too small at this hour band); year trend shows
2021-22 edge decayed to ~flat/negative by 2024-25 — consistent
with a stale historical edge, not a live one. VERDICT STANDING:
hypothesis NOT supported; hour-of-day family CLOSED (budget
spent per section 5). NO v2: any UTC18 re-test requires a NEW
hypothesis with NEW justification, not a re-run.
