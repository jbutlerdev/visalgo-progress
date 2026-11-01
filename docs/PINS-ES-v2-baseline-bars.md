# EA-RATIFIED LOCKED BARS — H-GAPDAY / OOS (ES instrument ONLY)

Author: executive assistant (EA lane, agent 67d61b63). Ratified from visalgo's
pre-registration as delivered in-channel at Oct-31 01:0xZ; this file is the
durable EA-authored bar document (provenance: EA memory + visalgo chat texts;
delegate does NOT echo bars into repo files to keep pin provenance clean).

## Instrument scope
ES-only. Pins are ES-derived (package-standard replay on ES front-month
streams, data/parquet/ES_front.parquet). Running these bars on NQ data yields
MEANINGLESS results. No cross-instrument porting in either direction.

## Canonical replay script
scripts/hgapday_replay_staged.py @ visalgo
- e318f24 = sha256 27be2ff74a1f7afe487e298851d9697b69edad72ca3a9374408d508dfa71401d (CURRENT; EA-verified; staged signals() rewired to repo wf_adaptive bindings-confirmed call-seq; runnable-in-repo)
- 580ad9e = sha256 695a40b2e2ef33a98a712f019553ce14099c4c6087388e79fbf142aa99bd60f6 (prior; EA-verified)
- e46fa29 = sha256 4bc4fafd783aee6367c1855518c7909c27bdbe685300891921825d1047883ac0 (pre-patch provenance; EA-verified)
Logic change pending: arms must call W.replay (package-standard) before ANY
numbers are quoted. Calibrate gate retained as harness VERIFICATION.

## Calibrate gate
3-way side-mapping discovery vs pins [6331, 8083, 6742, 6296] (seeds 0-3),
tolerance ±1%, else STOP (no numbers from a harness that fails calibration).
Side mapping confirmed from entry_for(): side=+1 iff arg==2 (calibrate becomes
verification once arms are W.replay-standard).

## Bars (family H-SIZE/H-ATRTHR; DD binding per H-FRI lesson)
- G1: mean dPnL(v2+GAPDAY − v2) ≥ +$150 over seeds 0-3
- G2: ≥ 3/4 seeds positive
- G3: BINDING — pooled max-DD abs no worse (repo-source DD curves required;
      verdict may print only "PROVISIONAL G1G2 (G3 pending — BINDING)" until
      G3 code runs; PASS string unreachable without it)
- G4: recency (12-month DATE WINDOW, matching H-PROB population; empty slice
      raises; <100 days warns; never vacuous 4/4) ≥ 0, ≥ 3/4
PASS(all 4) → confirm seeds 4-7 on identical bars → candidate doc + review.
FAIL → falsification #17, ledger 3C/17F; gap-day preference stays DESCRIPTIVE.

## Pre-written prediction (recorded pre-run, Oct-31)
Expect FAIL on G1 — non-gap trades are net-positive (~+$7.1/trade), so removing
them likely costs more than it saves. A pass of ALL bars earns EXTRA suspicion:
OOS-tail + fresh-seed validation required before any claim.

## Veto semantics (H-GAPDAY definition)
gap_atr = |open_d − close_{d−1}| / ATR14(day mean over valid bars);
VETO entries on gap_atr < 0.5 (single pre-chosen knob; mirrors/thresholds are
exploratory-only and may run only after primary passes). noFri + trail
1.75/1.75 + kill-day vetoes inherited from package-standard replay verbatim.

## AMENDMENT 2026-11-01T18:4xZ — pins UNREPRODUCIBLE; re-baseline route ratified (EA adjudication)
Finding (visalgo calibrate attempt #1, progress@494cca8): original pins
[6331,8083,6742,6296] are not reproducible from ANY file-side harness
(wf_adaptive: wrong trail/sl/fees; W.replay call-seq: 4 OOMs off AND misses
repo's own same-spec report 61.05). Root cause: the harness the pins encode was
the perished campaign script (pre-outage, stash-era); EA holds spec-level memory
(thresholds/bars/prediction) but NOT the harness source text — route (a)
(exact-source restoration) is EXHAUSTED. Calibrate-against-unreproducible-pins
is vacuous; delegate's refusal to run it silently is endorsed.

Ratified route (b) RE-BASELINE, conditions:
1. Named file-side harness: exact file + commit + call sequence committed and
   documented BEFORE any new pins derived. First candidate: W.replay call-seq
   per visalgo's bindings-confirmed header @ 580ad9e.
2. New pins derived on the pre-registered spec window (run_adaptive_oos header
   2022-10-18..2024-10-18, 2.0_5.0_0.45_trail_noFri, seeds 0-3), calibrating
   trivially (it IS the harness) — gate becomes harness-identity check +
   trade-count sanity (n per seed recorded, not assumed ~660).
3. Policy bars G1-G4 UNCHANGED as policy: dPnL remains RELATIVE (v2+GAPDAY vs
   v2, same harness) so the pre-registered FAIL-G1 prediction stays
   adjudicable. NOTE: W.replay trade universe (~n250/seed) is smaller than the
   perished harness (~n660) ⇒ the +$150 absolute bar is now HARDER, i.e.
   fail-safe direction; kept as-is deliberately.
4. Old pins archived: HISTORICAL, unreproducible, EA-memory provenance. They
   remain the evidence base for the already-confirmed H-PROB/v2/v3 candidate
   numbers — Jeremiah's pending promotion decisions reference that perished-
   harness evidence; re-derivation on the new harness is REQUIRED before any
   activation (flagged to owner separately).
5. Bars authority: this doc (EA-authored) + EA memory; delegate never echoes
   pins into repo files.

## AMENDMENT 3 2026-11-01T18:5xZ — RATIFIED WINDOW = days_all[-504:], NEW PRECONDITION G0 (EA adjudication)
Delegate honest-scale flag (re-baseline derivation @ visalgo 3e70829, spec
scripts/spec_v2_rebaseline.json): v2 baseline on the spec window
(2022-10-18..2024-10-18) is NEGATIVE (−218.89/−663.38/−191.44/−166.07,
n 253/258/247/253, deterministic cent-for-cent). dPnL off a losing baseline
risks a MECHANICAL G1 pass (vetoing loss-carrying trades from a strategy that
loses $310/seed) — which the FAIL-G1 pre-prediction, written for a profitable
baseline, does not anticipate. Ratified:

1. ADJUDICATION WINDOW = days_all[-504:] (repo default tail). PARAMS UNCHANGED
   from spec_v2_rebaseline.json (2.0_5.0_0.45_trail_noFri, trail, noFri,
   SEED/ENSEMBLE per bindings). WINDOW-ONLY change. NO variant selection:
   repo-report +277 top-variant figure is context only — do not chase it.
   If params-fixed/full-stream baseline is also negative → STOP (see G0),
   no further window/variant shopping.
2. NEW PRECONDITION G0 (harness-context gate, declared pre-GAPDAY-numbers):
   v2 baseline mean over seeds 0-3 on the ratified window must be > $0.
   G0 fail ⇒ outcome = NOT-ADJUDICABLE-CONTEXT: recorded as neither PASS nor
   FAIL (the pre-prediction's mechanism assumed a working strategy); hypothesis
   shelved pending fresh re-registration. Not a failure, not a pass.
3. G1-G4 UNCHANGED. FAIL-G1 pre-prediction stands; context now matches its
   written premise (profitable baseline) when G0 passes.
4. SPEC-WINDOW PINS archived as harness-identity evidence + context finding:
   on the file-side harness v2 is SIGN-NEGATIVE on 2022-24 — perished-harness
   +$6.6k-class numbers are not merely unreproducible but sign-divergent;
   strengthens re-derivation-before-activation gate on H-PROB v2/v3.
5. Ratified-window pins deterministic (2-run identical) → send to EA doc;
   repo keeps ZERO pin values (condition 5 unchanged).

## AMENDMENT 4 2026-11-01T19:1xZ — RATIFIED-WINDOW PINS (v2 baselines, CONFIRMED-PENDING-2ND-RUN)
Window days_all[-504:] (spec_v2_ratified.json @ visalgo 4ea5f48, committed
pre-run; params frozen), harness = staged script e318f24 (EA-verified):
| seed | v2 mean | n |
|---|---|---|
| 0 | $2,761.08 | 315 |
| 1 | $3,161.20 | 311 |
| 2 | $2,920.40 | 314 |
| 3 | $3,345.36 | 315 |
Mean +$3,047.01 — G0 PASS (all four positive; profitable-baseline context).
Status: CONFIRMED-PENDING-2ND-RUN — pins become canonical on the second
identical run (determinism identity check; attempts #1/#2 were cent-for-cent).
Context note for archive: sign agrees with perished harness on THIS window
(+$6.6k-class vs new ~half-scale, smaller n); the earlier sign-divergence was
spec-window (2022-24) specific. Activation-gate on H-PROB v2/v3 stands
(non-reproducible scale, unreproducible harness).
Pre-prediction status: FAIL-G1 premise-class (profitable baseline) now holds;
its MAGNITUDE basis (perished-harness economics, e.g. +$7.1/trade) does not
transfer — treat as directional, not numeric, anchor.
G3 accepted-as-repo-source: summarize_days on day_pnl (repo function); PASS
string unreachable unless G3 computes (BINDING per original doc).
