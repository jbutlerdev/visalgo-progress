# visalgo-progress

Run log + progress dashboard for the **visalgo algo-developer agent** (forge/herd).
The algo source lives in the private `jbutlerdev/visalgo` repo; this repo holds
only per-run logs and the GitHub Pages dashboard.

Dashboard: https://jbutlerdev.github.io/visalgo-progress/

## Run-log convention (agents MUST follow)

- One file per run: `runs/YYYY-MM-DDTHHMMZ-<slug>.md` (UTC, minute precision).
- Append the same run to `dashboard/data/runs.json` (newest first) so the
  dashboard renders it — keep both in the SAME commit as any code-work
  summary push.
- Content granularity: progress-level (what was attempted, experiments,
  test/backtest status, files touched, sierra instance touched + mode,
  risks/next steps). NO strategy internals, NO dataset contents, NO
  credentials. PnL only as rounded aggregates.

### runs.json entry shape
```json
{"id":"2026-10-26T1400Z-smoke","ts":"2026-10-26T14:00:00Z","type":"wake|manual|deploy","title":"...","summary":"...","status":"ok|partial|blocked|failed","experiments":0,"tests":"pass|fail|n/a","sierra":"none|dev|live-readonly","file":"runs/2026-10-26T1400Z-smoke.md"}
```
