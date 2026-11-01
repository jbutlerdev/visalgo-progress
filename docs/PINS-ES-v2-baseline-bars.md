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
- 580ad9e = sha256 695a40b2e2ef33a98a712f019553ce14099c4c6087388e79fbf142aa99bd60f6 (CURRENT; EA-verified)
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
