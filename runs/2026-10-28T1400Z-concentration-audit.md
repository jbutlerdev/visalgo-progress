# 2026-10-28T1400Z — Jeremiah's concentration concern: audited end-to-end (trade validation + reporting rule, no artificial smoothing) (type: manual, ≤25min)

## The observation, quantified
"You keep noticing 1 day makes a significant amount of profit" —
confirmed with numbers (mean-path over seeds 0–3, pkg-standard):

| | total | top day | top1 share | top5 share | ex-top5 | pos-days |
|---|---|---|---|---|---|---|
| E3 (live) | +4,487 | **2025-04-10** | **23.5%** | 59.7% | +1,806 | 45.9% |
| v2 | +5,314 | same day | 19.8% | 56.4% | +2,317 | 48.3% |
| v3 | +5,712 | same day | 18.4% | 52.5% | +2,716 | 48.7% |
| **v4 (approved)** | +5,803 | same day | **18.1%** | 51.6% | **+2,807** | 48.9% |

Same top day in **all 4 independent streams** (per-seed share 16–26%)
— the day is systematic (regime), not seed noise.

## (1) Is 2025-04-10 a VALID trade? — YES (raw-bar validation)
Trade: ENTER_SHORT @5728.0 (bar 1, p=0.532 clears thr, ATR 42.16 —
huge), TP=5517.2, SL=5812.4, day: post −3.3% prev-day close, 78 bars,
range 5501–5743, close 5653.5 (the April-2025 tariff-crash regime):
* **TP reachable:** day low 5501 < TP 5517 ✓ (trail took $1,053 = 211 pts);
* **SL never threatened:** post-entry highs ≤ 5743 < SL 5812 ✓ (no
  lucky-survival story; the short was never wrong);
* **Scale clean:** prices 5.5–5.7k (x100-sanity: max 5731, not ~500k)
  ✓; prev-day continuity −3.3% = crash day, not bad ticks ✓;
* Model behavior coherent: crash continuation was exactly the
  high-ATR-regime edge the program has triangulated 4 ways.
**Verdict: real trade; nothing to fix.**

## (2) Smoothing policy — REFUSED artificial smoothing, adopted NOTE
Per your own caveat ("don't artificially smooth, but note outliers"):
* every dashboard algo card now carries `top1_day / top1_share% /
  top5_share% / ex_top5 / pos_days%` metric chips (merged into the
  1235Z curves entry) + policy line in params ("noted, not smoothed");
* repro `~/work/conc_audit.py` (saves per-stream daily frames for any
  future audit — the check can be re-run on any variant in minutes);
* the honest review headline: **the edge is NOT one day** — ex-top5
  E3 +$1,806 / v4 +$2,807 remain solidly positive, ~48–49% of days
  positive, median day ≈ 0; the day is a regime-bonus, and the
  approved stack *reduces* reliance on it (23.5% → 18.1%) rather than
  adding it.

## Standing rule (adopted this cycle)
Any headline aggregate I report from now on ships with top-1/top-5
share + ex-top5 alongside. vram llama re-confirmed healthy (active,
laguna-xs-2.1, health:200) — GPU session closed cleanly last cycle.
Sierra: none. Datasets read-only.
