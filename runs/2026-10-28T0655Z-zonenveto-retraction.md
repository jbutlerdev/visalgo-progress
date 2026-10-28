# 2026-10-28T0655Z — **RETRACTION + correction: H-ZONEVETO "CONFIRMED" was measured on a non-package-standard replay (missing Friday skip) — under the correct definition discovery FAILS D1 (+$95, not +$469). Demoted to MIXED/under review; ledger back to 3C/16F. v4 composition numbers re-measured pkg-standard: still strongly positive.** (type: wake, ≤25min)

vram gate #29: unchanged (Thursday ping armed).

## What happened (self-audit, ~50 min after the confirmation)
While verifying the DLL zone-gating claim (confirmed: acsil/NqAmtAgent
.cpp:261 has zone_of() mirroring ml/amt_engine — port IS gating-only),
I audited my own ZVETO harness and found **my run_zv/run4 replay
functions omitted the Friday skip** that every package-standard replay
in this program includes (h_ts_confirm.run has
`weekday()==4: continue`; my new scripts defined their own replays
without it). All historical packet numbers (v2 +807/+481, v3 TS +302/
+491) were and remain correct — they exec the proper run(). Only
TODAY's ZVETO/v4 numbers were off-definition.

## Corrected numbers (package-standard: noFri + trail 1.75 + vetoes; single pinned script h_zoneveto_pkg.py / h_zveto_final.py)
| group | d(Z vs v2) | was (off-def) |
|---|---|---|
| discovery 0–3 | **+$95, 3/4 (seed3 −147) → D1 FAILS the +$150 bar** | +$469 4/4 |
| confirm 4–7 | **+$210, 4/4 (passes)** | +$457 4/4 |
| seed 8 | +$117 | — |
| pooled 9 streams | **9/9 sign-positive, mean ≈ +$149** (borderline) | — |
| DD | improves in ALL groups (e.g. conf −1,481→−1,284) | same direction |
| recency marginal (Z) | **+$193, 4/4 (robust)** | +$137 |

**v4 composition (pkg-std, correct now):** TS54 on v2+Z **+$394, 4/4**
(robust complementarity); **v4 vs E3 recency +$837, 4/4** — best on
record by a wide margin (v3 +491, v2 +481).

## Verdict per pre-registration (no protecting my earlier claim)
Discovery D1 fails under the correct definition → the 0625Z CONFIRM is
**retracted**; ledger 4C→**3C/16F**. Honest characterization: the
zone-5-short veto is a **MIXED candidate** — DD-improving in 9/9
streams and recency-positive 4/4 (its robust face), with an
absolute-PnL effect straddling the pre-set bar (+$149 vs ≥$150) once
Fridays are handled per definition. The +$469/+457 replication I
celebrated was real *within its own harness* — both arms shared the
bug — which is exactly why "same script both arms" is necessary but
NOT sufficient; the script must match the DEPLOYED definition. That
lesson goes in the postmortem.

## What survives and what's next
* v3 (v2+TS54) UNAFFECTED — its numbers were always pkg-std.
* v4's recency story survives (v4-vs-E3 +837 pkg-std measured correctly
  now); its Z-component awaits a clean re-preregistration on a
  definition-pinned harness (no seed-reuse claim inflation this time;
  likely framing = DD/recency candidate, PnL-bar re-set BEFORE run as
  a *new* pre-registration, discovery already informed → treat seeds
  0–8 all as informed, fresh validation only on the OOS tail going
  forward).
* filter_policy port note: zone gating feasible (DLL computes zones;
  Python side reads zone from frame JSON - verify field name at wiring).

Jeremiah notified of the retraction (he received the earlier claim).
Sierra: none. Datasets read-only. No prod change.
