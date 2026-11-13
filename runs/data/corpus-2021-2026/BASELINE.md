# NQ 5-min first-touch baseline — formal write-up
_built 2026-11-13T20:02:30Z | corpus: NQ front-month 5m bars 2021-03→2026-03, 337,922 bars (SIGNED OFF roll #18 probe-523, QA suite green)_

## Design
- Signal: sign(log-return) of last completed 5m bar.
- Outcome: fwd close-to-close index points at h = 1, 12, 48, 288 bars (5m/1h/4h/1d).
- Samples: full-hours (n=1,306,200 decisions) and RTH-only 13:30-20:00Z + 288-bar file-tail trim (n=293,033).
- Costs/slippage: NONE applied (raw points). Overlap autocorr uncorrected — t-stats optimistic.
- Note: full-hours artifact keys carry disclosed 'hh' double-prefix (probe-524 cosmetic defect); normalized here.

## Headline results (mean fwd pts after up-bar / after down-bar)
| horizon | full up | full dn | RTH up | RTH dn | dn−up gap (full / RTH) |
|---|---|---|---|---|---|
| h1 (5m) | -0.067 | 0.124 | -0.122 | 0.272 | 0.191 / 0.394 |
| h12 (1h) | 0.244 | 0.37 | 0.776 | 0.913 | 0.126 / 0.137 |
| h48 (4h) | 0.968 | 1.403 | 4.457 | 4.762 | 0.435 / 0.305 |
| h288 (1d) | 6.558 | 8.101 | 21.887 | 24.762 | 1.543 / 2.875 |

## Hour-of-day (RTH band, h1 gap t-stats, i.i.d. se)
- UTC 13: gap -0.623 t=-1.1 (dn -0.044±0.418 / up 0.579±0.363)
- UTC 14: gap -0.188 t=-0.5 (dn -0.418±0.286 / up -0.23±0.296)
- UTC 15: gap 0.694 t=2.0 (dn 0.393±0.255 / up -0.301±0.234)
- UTC 16: gap 0.37 t=1.3 (dn 0.259±0.22 / up -0.111±0.187)
- UTC 17: gap -0.199 t=-0.7 (dn -0.073±0.207 / up 0.126±0.208)
- UTC 18: gap 0.659 t=2.3 (dn 0.584±0.209 / up -0.075±0.196)
- UTC 19: gap 0.392 t=1.3 (dn 0.247±0.22 / up -0.145±0.219)
- UTC 20: gap 2.972 t=0.4 (dn 4.736±5.497 / up 1.764±6.238)

## Weekday (h1 gap)
- Mon: gap 0.382 t=1.1
- Tue: gap 0.115 t=0.3
- Wed: gap 0.147 t=0.4
- Thu: gap -0.03 t=-0.1
- Fri: gap 0.652 t=1.7

## Verdict (honest)
- 5m reversion tilt real in DIRECTION (dn−up gap positive RTH hours UTC15-19) but WEAK: max gap t ~2.0-2.3, autocorr-optimistic → no cell standalone-significant.
- Open hour (UTC13) MOMENTUM-flavored (gap −0.623 t=−1.1) — two-regime day shape, suggestive not conclusive.
- Sub-cost at h≤48: |means| ≤ ~0.3 pts (full) / ~1 pt (RTH) vs NQ half-spread+slip ≥ ~0.5-0.75 pts → NOT tradeable raw; useful as FEATURE inside a conditioned model.
- h288 gap tracks drift (long bias), not a signal.
- NO weekday gate (max t=1.7 Fri).
- Roll contamination mitigated only by heuristic 288-bar trim; exact roll-exclusion pass open.

## Recommended use
NULL/BASELINE reference for WF-bar ratification: candidates must beat this net of costs, not gross. Hour-of-day regime shape is the one structure worth a properly autocorr-corrected re-test (block bootstrap over days) before any GPU spend.
