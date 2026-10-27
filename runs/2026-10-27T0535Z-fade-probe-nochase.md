# 2026-10-27T0535Z — fade probe: vetoed cells are chop, not mis-calibration (no-chase); data standby confirmed (type: wake, ≤25min)

**Context:** promotion package (branch 856e21c4) awaits Jeremiah; queue is
intentionally unpadded. Data-availability check first: signal caches end
**2026-10-01** (900 days) and `ES_front.parquet` is externally built (no
self-serve extension path in-repo) — the planned fresh-days re-check stays
blocked on dataset growth, as logged. No repair attempts on read-only data
(floor rule; noted ESF6-style files at /opt are raw contracts, not the
front-series builder output).

**Observation (measurement-first, promotion-decision rule pre-registered
before running):** are H-PROB's vetoed cells (SHORT p(0.55,0.60],
LONG p>0.60) systematically WRONG (fade-able) or just choppy? Traded the
OPPOSITE side at each vetoed first-cross (package exits 1.75/1.75,
seeds 0–3). Rule: pursue H-FADE only if mean opposite PnL ≥ +$400/stream.

**Result: +$266/stream mean (279/255/295/235 — suspiciously uniform), split
vetoed-SHORT cells +$217, vetoed-LONG cells +$49. Below the bar → NO CHASE.**
Interpretation: the cells are *mediocre*, not *inverted* — consistent with
the veto's true mechanism being **day-skip** (bad re-rating days carry
worse pre-veto trades too, which is why skip-and-continue measured −$228
while kill-day earned +$495). Fading would monetize noise while destroying
the skip benefit; the pre-registered bar worked exactly as an anti-churn
device.

**Series closure:** this was the last untested implication of the entry-
probability layer. Entry-surgery series: CLOSED (5 falsified + 2 confirmed).
Honest open items: (1) Jeremiah — package merge/activation decision;
(2) dataset — fresh-days re-check when ES_front grows past 10-01;
(3) nothing else queued that isn't exposure-removal churn.

Hygiene: observation-only probe (no promotion claim); scripts in ~/work,
caches read-only, repo code unchanged, Sierra none.
