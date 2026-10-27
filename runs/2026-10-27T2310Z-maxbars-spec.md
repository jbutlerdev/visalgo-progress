# 2026-10-27T2310Z — menu-3/spec: maxbars contract tests (7, branch maxbars-spec) — doubles as the DLL acceptance spec for the v3 time-stop (type: wake, ≤15min)

vram gate #15: unchanged (notify hold → tomorrow AM).

## Delivered
`ml/test_maxbars_spec.py` (branch `algo-dev/maxbars-spec`, `3d95ac61`):
locks the exact semantics `sim_trail_p(maxbars=…)` implements — which,
if Jeremiah approves the acsil time-stop leg, are the **acceptance
criteria the DLL must replicate** (so backtest and live can't drift, the
policy-divergence class we keep hitting):
* beyond-window bars **invisible** — a TP at bar 60 must NOT fire under
  maxbars=54; control assertion proves the same data DOES fire without
  the leg (guards against a no-op time-stop that "passes" everything);
* time-stop exit = **close of bar maxbars-1**, tag "eod" (not next-bar
  open — a real off-by-one/price-source trap for the C++ port);
* SL-before-TP precedence preserved inside the window (same-bar touch →
  SL wins);
* trail active inside the window (rising lows-held run-up arms the trail
  at first trigger bar, exits on first post-runup break — hand-computed
  trail level 102.25 asserted to 10 dp);
* short symmetry; `maxbars=None` == current live behavior (inert-when-
  nothing-fires regression anchor).

7/7 green. Two fixture bugs self-caught (rising closes necessarily
trigger the trail; run-up lows must stay above the rising trail) — spec
validated against implementation, implementation unchanged.

**Why this cycle was worth it:** the v3 DLL work, if approved, now has a
portable correctness contract — the mingw build passes when these 7
semantics hold on a C++ reimplementation harness (and the two fixture
traps above are exactly where a hand-ported time-stop would go wrong).
Ready-to-use the moment the go comes; no more backtest/live drift risk
on the time leg.

## Ledger
Menus 1–5 exercised today; strategy: v3 CONFIRMED (8/8) + Friday audit;
coverage: loop 16 + maxbars-spec 7. Five review-ready branches staged:
hprob-bandgate (v2) · ts54-timeslot (v3) · loop-testcov ·
watchdog-testcov · maxbars-spec. Decision stack (v2 / vram a-b-c / v3
DLL) fully documented.
Sierra: none. Datasets read-only. master fb1a019 clean.
