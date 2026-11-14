# NQ 5-min Corpus — operator index
_compiled 2026-11-14T00:21:14Z | roll #19 | all artifacts below are IN THIS FOLDER_

## Corpus
- NQ front-month 5-min bars, 2021-03 -> 2026-03 | 337,922 bars | 428,266,327 trades | 61 per-month parquets (manifest.json keys total_bars/total_trades/months)
- Decoder: ml/nq_ticks_load.month_bars VERBATIM @ origin/algo-dev/ticks-builder e4d7b7f (semantics VERBATIM from ticks-builder e4d7b7f)
- Build + QA: roll #18 probe-519 campaign, QA pass flag: 61

## QA & audits (all green)
- manifest.json — build QA (bytes/zstd/dbn-magic/tick-sanity)
- QA_TABLE.md — human-readable QA
- continuity.json — GAPS_OK (0 dups, 0 overlaps, max true gap 73.1h holiday-legit, 19 clean quarterly rolls)
- sanity.json — SANITY_OK (0 bad months; NQ 10,484.75 -> 26,399 real-plausible)
- throughput.json — THROUGHPUT_OK (median 281,949 trades/day)
- sessions.json — sessions uniform (overnight share 65.1-65.6% all years)
- raw_window_check_jan25_aug24.json — Jan25/Aug24 raw windows complete (NO re-pull)

## Baseline family (honest null-leaning verdict)
- BASELINE.md — formal write-up, WF-null reference role
- baseline_first_touch.json — full-hours, 4 horizons (n=1,306,200 decisions)
- baseline_first_touch_rth_trim.json — RTH+trim variant (n=293,033)
- baseline_h1_hourofday.json / baseline_h1_hourofday_tstats.json — hour profile, i.i.d. t max 2.3
- baseline_h1_boot.json — day-block bootstrap: UTC15/18 CI-excl-zero (borderline)
- baseline_h1_boot_noroll.json — + roll-exclusion: UTC15 FALLS OUT, UTC18 sole survivor
- baseline_h1_weekday.json — no significant weekday (max t=1.7)
- baseline_h1_stability.json — year-half stability: 6/11 positive, sign flips (corroborates closure)
- bars/ — the 61 per-month parquet corpus

## Pre-registration (family-closing)
- PREREG_utc18_fade.md — v1 + RESULTS section 7: **FAIL** (CI [-1.882,+4.424] incl zero; stale-edge year trend) -> hour-of-day family CLOSED, no v2
- prereg_utc18_fade_result.json — machine result


## Expiry-truncation months (probe-557 finding — load-bearing for WF/ML)
Five month files end at their front contract's 3rd-Friday expiry
(decoder semantics: single volume-argmax front per file, trading
stops at expiry): **202406 (ends Jun-21), 202409 (Sep-20),
202503 (Mar-21), 202506 (Jun-20), 202512 (Dec-19)**. Raw files
for these months are FULL (verified 202406: 7,999,761 ticks to
Jun-30; NQM4 last tick Jun-21 13:29:45Z). TREAT THESE 5 MONTHS
AS PARTIAL (~first 3 weeks of front) in WF/ML; month boundaries
remain roll-discontinuous (BASELINE.md roll-exclusion guidance).

## Standing rules for downstream use
- Any candidate strategy must beat BASELINE.md net of costs, not gross
- Reused-hour testing FORBIDDEN (budget spent; new hypothesis needs new justification)
- GPU-bound work DEFERRED (llama-server permanent herd infra); CPU-bound unblocked
