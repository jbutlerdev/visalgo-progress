# 2026-10-27T0340Z — Filters package WIRED into the decision path (env-gated, branch-only, default OFF) (type: wake, ≤25min)

Queue item (b) from 0310Z: consolidate the confirmed filters package into
code + implementation note so promotion is one review-click.

## What changed (branch algo-dev/hprob-bandgate, commit 856e21c4 — NOT deployed)
1. **`ml/filter_policy.py` (new)** — single source of truth for the entry
   decision: argmax → thr-demotion → **kill-day vetoes** (SHORT
   p∈(0.55,0.60], LONG p>0.60). Pure stdlib; `decide()` returns
   (action, argmax, thr_applied, veto_reason). 10 unit tests incl. band
   edges (0.55/0.6001 enter; 0.5501/0.60 veto) and precedence.
2. **`ml/service.py`** — decide_payload now calls the shared policy, gated
   `VISALGO_FILTERS=1`. **Default OFF reproduces today's live decisions
   byte-identically** (verified by replaying the old code path on boundary
   probability vectors; the 40/40 offline suite passes). Bonus fix: old
   code's `elif` meant the volf log-field was skipped when thr had
   demoted the entry (action unaffected — both HOLD — but the field lied).
3. **`ml/drift_check.py`** — parity checker now uses the SAME policy.
   **Fixes an existing drift bug**: the checker compared raw argmax while
   the service applied ENTRY_THR demotion — any below-thr entry bar would
   have shown false DRIFT. (Found while wiring; same class of
   policy-divergence bug this module now structurally prevents.)

## Deployment plan (pending Jeremiah, one review-click)
- Code: merge branch → vram `git pull` → `systemctl restart visalgo-svc`
  with `VISALGO_FILTERS=1` (drop-in env; one-line unit change).
- Exits: `agent_sltp.txt "1.75 5.0 1.75"` on the chart workdir (file-driven
  in fw29 DLL — no recompile; the trail half needs no code at all).
- Rollback: unset env (+ restore sltp file) — behavior returns to registry
  E3 exactly (OFF_VETO proven byte-identical).
- Evidence chain: 2220Z (bars) → 0105Z (recency+robustness) → 0240Z
  (exit-cell confirm) → 0310Z (streams 4–7: 8/8 pooled +$807, DD −18%).

## Files / hygiene
- Branch-only; master untouched; live vram NOT touched (no ssh, no restart).
  Sierra: none. Dataset read-only.
- Dashboard algos[]: package vs E3 on stream 5 (never used in any selection
  step) — honest fresh-stream pair.
- Process notes: two test fixtures wrong pre-run (0.60-in-band; argmax was
  HOLD) — caught by the tests themselves, fixed; OFF_VETO placement moved
  from service into the policy module (single source of truth).
