# 2026-11-01T1820Z — PRE-REGISTRATION (design before numbers): OOS candidate table on the ratified file-side harness (ES lane, campaign 2-ES)

## Why fresh pre-reg (separation policy)
Original oos() (staged script) uses hand-rolled arms = NON-STANDARD (banned
from quoting). Ratified harness = W.replay call-seq. Arms below are therefore
re-expressed EXCLUSIVELY in file-source vocabulary (ml/wf_adaptive replay
signature: thr, slm, tpm, mode in fixed|be|trail, gate in
none|brk10_60|brk10_100|brk20_150|trend|volf|zone|early|noFri combos).
Window = ratified days_all[-504:], seeds 0-3 (same ratified context as G0/G1;
NO new windows, NO variant selection beyond the three pre-declared arms).

## Arms (exactly three, pre-declared; nothing added post-sight)
  v2   = (thr .45, slm 2.0, tpm 5.0, "trail", "noFri")   [ratified baseline]
  e3   = (thr .45, slm 2.0, tpm 5.0, "fixed", "noFri")   [fixed-exit control]
  v4   = (thr .45, slm 2.0, tpm 5.0, "trail", "noFri_zone") [zone-gate variant]
       — gate_ok parses substring gates; "noFri_zone" applies BOTH (file
       source: if "noFri" in name / if name=="zone" — CHECK: "zone" branch
       is name=="zone" EXACT, so combined string does NOT apply zone!).
       => v4 corrected pre-run to gate "zone" ALONE? NO — that drops noFri,
       changing two knobs. DECLARED RESOLUTION: v4 = ("zone") alone, labeled
       "zone-only (noFri dropped — file source cannot combine)"; comparison
       to v2 is then 2-knob and DESCRIPTIVE-ONLY for v4; only e3-vs-v2 is a
       1-knob adjudicable contrast. (File beats memory beats elegance.)
## Metrics per arm (pooled + per-seed recorded, not assumed)
n trades; total pnl; summarize_days fields (pnl,h1,h2,worst_q,maxdd,win_days)
via repo source; daily-pnl csv artifact (per-arm per-date, seeds summed) ->
runs/data/oos_table_YYYYMMDDTHHMMZ.csv. Determinism: single run; identity
expected v2 total == canonical pins (cent-for-cent) else STOP+report.
## Gates: NONE beyond determinism identity — this table is DESCRIPTIVE
characterization feeding Jeremiah's candidate-stack review; any future
hypothesis on these arms pre-registers its own bars. No PASS/FAIL strings.
## Procedure: script scripts/oos_table.py (commit before run) -> single run
-> type (a) entry with raw stdout + csv artifact.
