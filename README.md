# visalgo-progress

Run log + **performance dashboard** for the visalgo algo-developer agent
(forge/herd). The algo source lives in the private `jbutlerdev/visalgo`
repo; this repo holds per-run logs, equity curves, params and metrics.

Dashboard: https://jbutlerdev.github.io/visalgo-progress/

## Run-log convention (agents MUST follow)

- One file per run: `runs/YYYY-MM-DDTHHMMZ-<slug>.md` (UTC, minute
  precision). Write it with a BASH heredoc (the chat write-tool writes to
  a different filesystem than bash — see visalgo/AGENTS.md).
- Same commit: prepend the run to `docs/data/runs.json` (newest first).
- **Any algo tested, backtested, replayed or forward-observed in the run
  MUST appear in `algos[]` with params, metrics and an equity curve.**
  The dashboard is a quant cockpit: the curve is the point of the run.
- Content: full performance detail is welcome (params, fills, drawdowns,
  per-trade tables in the .md, strategy descriptions). The private repo
  keeps the indicator/ACSIL source — nothing here needs censoring.
  The ONLY hard rule: **never commit credentials, tokens, account
  numbers, or vault paths.**
- Verify before pushing: `git show --stat HEAD` lists every intended file.

### runs.json entry shape (v2)
```json
{
  "id": "2026-10-26T1400Z-e3-target-sweep",
  "ts": "2026-10-26T14:00:00Z",
  "type": "wake|experiment|deploy|manual|example",
  "title": "E3 target sweep 25-40 pts",
  "summary": "what happened, verdict, next step",
  "status": "ok|partial|blocked|failed",
  "tests": "pass|fail|n/a",
  "sierra": "none|dev|live-readonly",
  "file": "runs/2026-10-26T1400Z-e3-target-sweep.md",
  "algos": [
    {
      "name": "E3-MES",
      "params": {"entry": "B12C cross 5m", "target_pts": 32.75,
                 "stop_pts": 13.25, "session": "RTH", "dataset": "ES_front 2024-2026"},
      "metrics": {"net_pnl": 1240.5, "trades": 87, "win_rate": 0.54,
                  "max_dd": -310.0, "profit_factor": 1.42, "sharpe": 1.1},
      "equity": [["2026-01-02T14:30Z", 12.5], ["2026-01-03T15:10Z", -30.0]]
    }
  ]
}
```
- `equity`: **cumulative** P&L series `[iso_time, cum_pnl]`, $ per contract
  or $ total — state units in params/metrics. Downsample to ≤500 points
  (dashboard thins further). For backtests, one point per trade or per
  bar-close, whichever is smaller.
- `params`: everything that differs from defaults + dataset/window id.
- `metrics`: minimum `net_pnl, trades, win_rate, max_dd`; add
  `profit_factor`, `sharpe`, etc. as available.
- Baselines/comparisons: add a second `algos[]` entry named e.g.
  `"E3-MES (baseline)"` so the curves sit side by side.

Old v1 entries (no `algos[]`) still render — just without curves.
