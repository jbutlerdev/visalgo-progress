# 2026-10-28T0840Z — pre-deployment due-diligence: **v2 holds on the DEPLOYABLE definition** (noFri on BOTH arms = what activation actually runs): +$827 pooled 4/4, DD −1,486 vs E3 −1,820, recency +$534 4/4 — GO-pending verdict rule (locked pre-run) passes (type: wake, ≤20min)

vram gate #32: unchanged (Thursday ping next cycle).

## Why this audit (the ZVETO retraction's systemic lesson, applied)
The 0655Z retraction taught: *both-arms-same-script is necessary but
not sufficient — the script must match the DEPLOYED definition.*
Systematic sweep found the same class in the PACKET lineage: hprob.py,
hstack_confirm.py, hprob_oos.py, htrail_confirm.py, h_seeds47, h_seed8
— all six lack the Friday skip the **live DLL enforces** (noFri is a
DLL-side rule, so activation runs noFri regardless of backtest). Only
the TS scripts had it. Packet deltas were therefore "filters without
the Friday gate" — internally consistent, but not literally what gets
deployed.

## The audit (verdict rule locked BEFORE running; seeds 0–3, cached sigs)
Both arms now package-standard (noFri): E3 = no vetoes + trail 2.0/1.5;
V2 = kill-day vetoes + trail 1.75/1.75 — the exact activation config.

| metric | packet (Fri included) | **deployable (both arms noFri)** |
|---|---|---|
| pooled dE3 | +$807 | **+$827 (4/4: +462/+1,167/+511/+1,168)** |
| DD mean | −1,486 vs −1,820 | **−1,486 vs −1,820 (unchanged to the dollar)** |
| recency 12mo | +$481 | **+$534 (4/4)** |

**Verdict rule: POOL ≥ +$500 AND ≥3/4 AND DD-no-worse → PASS. v2
STAYS GO-pending on the deployable definition.** Removing Fridays
slightly HELPS both deltas (Friday trades were the weaker cohort on
both sides — consistent with the H-FRI formal's flat-recent finding).

## What this changes
* **Promotion packet strengthened at exactly the right moment** — the
  numbers Jeremiah reviews are now the deployed-definition numbers
  (the activation checklist already assumed them; now they're measured
  that way).
* All numbers in the deployable column are this script's fresh output
  (incl. DD); the packet column quotes prior runs — the DD match to the
  dollar is genuine (Friday cohort trades were vetoed/held on most streams)
  but treat the fresh column as authoritative.
* Packet docs (CANDIDATE_hprob_bandgate.md) should cite the deployable
  table as primary (branch doc update queued next cycle).
* The definition-sweep method (grep weekday() across harnesses +
  dual-arm recompute) is now the standing pre-review gate for any
  packet number.

Sierra: none. Datasets read-only. No code change. Repro:
~/work/v2_deployable_audit.py. OOS refresh armed 21:30Z tonight.
