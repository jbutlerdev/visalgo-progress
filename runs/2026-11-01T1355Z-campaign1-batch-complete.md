# 2026-11-01T1355Z — type(a): Campaign 1 dataset build COMPLETE for all usable bind months — 42/42 parquets + manifests; DATASET-INTEGRITY REPORT: 19 of 61 raw months are 0-byte files

## Build (commands: scripts/build_ticks_5m.py per month; one loop, raw rc per file)
42 months built Mar-2021..Aug-2024, ~9 s each: bars 5.3k-6.3k/month typical
(202103=4369 partial start-month, 202406=3995 shortest), front-month roll
follows calendar correctly (NQM1->NQN/H2->...->NQU4 per value_counts). All
manifests written; all committed under runs/data/ (42 parquet + 42 json).

## DATASET-INTEGRITY REPORT (constitution #1: quoted)
`ls -la /opt/agent-data/visalgo/raw/ | awk '$5 == 0'` -> 19 files, exactly:
glbx-mdp3-20240901 .. glbx-mdp3-20260301 (Sep-2024 through Mar-2026 inclusive,
every month), all ZERO bytes. Failures raw: `ValueError: Cannot create data
source from empty file: <name>`. Non-empty count: 43 (incl. first). Bind du:
5.9G total. Consequence: derived dataset covers 2021-03-10..2024-08-31 only.
Per AGENTS.md: reporting, not repairing — for Jeremiah to re-stage those 19
months (or confirm intentional). The H-GAPDAY/OOS era (Sep-2025+) is INSIDE
the hole: when Jeremiah re-stages, tail-pull can come from raw bind (better
than the closed-ssh .scid route).

## Next
(1) QA rollup pass (schema/dupes/gaps across 42) -> rollup artifact + entry.
(2) Report to Jeremiah (notify): 19 zero-byte months + what they cost.
(3) Frozen sequence (H-GAPDAY/OOS) — NOTE blocked by same hole: eval window
needs re-staged recent months; calibrate gate on 2021-2024 data possible but
would change the pinned baselines meaning (different streams) -> calibrate
against REPO sig-cache semantics first (repo ml/ path still exists per EA),
or re-pin after restage. Decision item flagged in EA checkpoint.
