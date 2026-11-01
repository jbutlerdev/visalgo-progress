# 2026-11-01T1800Z — PRE-REGISTRATION (committed BEFORE numbers): H-GAPDAY arms on the ratified file-side harness

## Harness (ratified, unchanged): scripts/gapday_arms.py follows
calibrate_v2.py call-seq EXACTLY (build_dataset -> W.SEED -> days_all[-504:]
-> build_day_index -> collect_signals -> sub-wrap -> W.replay(dat, days,
0.45, 2.0, 5.0, "trail", "noFri")). Arms:
  v2         = replay over all days;
  v2+GAPDAY  = replay over days2 = [d : gap_atr(d) >= 0.5].
Day-veto == day-removal is EXACT (replay = at most one entry/day; gate noFri
does not consume cross-day state -> filtering cannot contaminate the arms;
brk-style gates WOULD, but are not in the ratified spec).
gap_atr(d) = |open_d - close_{d-1}| / mean_valid(atr_d); prev day from
days_all ordering (window is a TAIL of days_all => prev always exists, no
1e9 edge-case); open/close = first/last bar of day; atr = ATR14 column daily
mean over finite values (nulls counted + reported). Matches PINS doc veto
semantics verbatim.
## Harness-resolution disclosure (doc's "trail 1.75/1.75 + kill-day inherited
verbatim from package-standard replay"): under the ratified FILE harness the
params are locked to spec_v2_ratified.json -> trail = ml/wf_adaptive.
sim_pnl_trail file source (2.0/1.0*atr0); NO kill-day veto exists in
gate_ok("noFri") — "verbatim" resolves to FILE SOURCE, no hand-rolling
(any hand-rolled kill-day would violate the W.replay mandate = the very
vacuous-harness class this campaign exists to prevent).
## Gates (declared now, before sight of any arm number)
G0 (already PASSed @1745Z run; re-checked): mean baseline > $0.
G1: mean dPnL(2-1) >= +$150 | G2: >=3/4 seeds dPnL>0.
G3 BINDING: pooled daily pnl = SUM over seeds per calendar date, per arm;
maxdd via W.summarize_days (REPO SOURCE) on pooled series; PASS iff
|dd_arm2| <= |dd_arm1|. PASS string unreachable unless G3 computed (FIX2).
Per-seed DD printed as context.
G4: 12-month DATE WINDOW (max_date - 365d, H-PROB convention): per-seed
rec dPnL from both arms' daily pnl maps; >=0 in >=3/4 AND pooled rec dPnL
>=0; empty slice RAISES; <100 days WARNS; never vacuous.
## Determinism: single run; baseline totals per seed printed — expected
CENT-IDENTICAL to ratified pins (2,761.08/3,161.20/2,920.40/3,345.36) =
second-run identity proof across processes (condition 5 ask); n expected
315/311/314/315. Deviation from either expectation = STOP + report, no
re-runs until diagnosed.
## Verdict strings (exact, from doc): PASS(all four)->"confirm seeds 4-7";
G3-not-computed->"PROVISIONAL G1G2 (G3 pending — BINDING)"; else FAIL ->
falsification #17 (ledger 3C/17F), gap-day preference stays DESCRIPTIVE.
FAIL-G1 expected (EA pre-prediction; my expectation aligned).
