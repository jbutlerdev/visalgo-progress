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
