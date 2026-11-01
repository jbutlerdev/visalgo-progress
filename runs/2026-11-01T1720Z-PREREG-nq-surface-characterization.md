# 2026-11-01T1720Z — PRE-REGISTRATION (before numbers): NQ surface baseline characterization (campaign-2-style, EA-ratified 17:1Z)

## Scope + separation (EA standing policy quoted)
42 clean NQ months (runs/data/NQ_ticks_5m_202103..202408, campaign 1,
QA-clean @18a8843). DESCRIPTIVE facts about the NQ surface only. NO strategy
claims, NO comparison to ES numbers, NO borrowing of ES bars/pins/results
(locked bars 49aaa52c/215ff0ee stay untouched ES-instrument artifacts).
Any future NQ hypothesis pre-registers its own gates against THESE facts.

## Pre-registered metrics (declared BEFORE computing; commands fixed)
script: scripts/nq_surface_characterize.py (new, committed pre-run), reads
only runs/data/*.parquet. For each month, then pooled:
 M1 bar count, mean/std of 5-min log returns (close-to-close);
 M2 realized vol = std(r)*sqrt(78*252) (5m bars/day ~78 nominal 24h-adjacent;
    constant declared now, no tuning after sight);
 M3 max |1-bar return| and its date;
 M4 mean volume/bar, share of zero-range bars (high==low);
 M5 discontinuity-gap ratio: over bar pairs with index diff > 5min,
    g = |open_t - close_prev| / same-day median(high-low); report median,
    p90, p99 pooled (session-structure fact for any future NQ gapday test);
 M6 weekday table: mean |daily return| per weekday (facts for any NOFRI-style
    decision on this surface);
 M7 roll audit: front symbol (manifest) changes only in 4 calendar windows
    (mid-month Mar/Jun/Sep/Dec + Jan/Apr/Jul/Oct) — count roll dates, expect
    14 rolls across 42 months (front H/M/U/Z quarterly).
## Acceptance (descriptive run, no pass/fail gates): every metric printed with
its command; any metric that cannot be computed = stated, not skipped.
## Output: runs/data/nq_surface_characterization.csv + this entry completed.
