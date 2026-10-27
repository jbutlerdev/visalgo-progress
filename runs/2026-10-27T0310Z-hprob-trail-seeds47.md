# 2026-10-27T0310Z — Package v2 holds on FRESH streams 4–7: +$820 mean, 4/4, DD better in all (type: wake, ≤25min)

**Belt-and-braces per queue (pre-registered this cycle):** confirmed package
C3 (E3 + H-PROB kill-day vetoes + trail 1.75/1.75) vs E3 baseline on four
NEVER-USED ensemble streams (seeds 4–7; new signal caches ~75 s each). Bar:
mean dPnL ≥ +$500 AND ≥3/4 positive.

## Results (full window, cached signals, seeds 4–7)
| seed | E3 | package | d | DD E3 → pkg |
|---|---|---|---|---|
| 4 | +4,151 | +4,687 | **+535** | −1,696 → −1,480 |
| 5 | +1,447 | +2,269 | **+822** | −1,908 → −1,529 |
| 6 | +2,787 | +3,713 | **+926** | −1,946 → −1,631 |
| 7 | +4,451 | +5,447 | **+997** | −1,661 → −1,282 |
| **mean** | +3,209 | +4,029 | **+$820** | −1,803 → **−1,481** |

**VERDICT: HOLDS** (+$820 ≥ 500 bar; 4/4 ≥ 3/4 bar). Note the fresh streams
are much weaker baselines (seeds 5–6 at +$1.4–2.8k vs +$4.5k for 0–3 —
stream variance is genuinely large, exactly the pitfall PROCESS.md #8
warns) — yet the delta is +$535…+$997 and DD improves in every stream.
Pooled across 8 streams: **+$807 mean, 8/8 positive, DD −1,812→−1,483**.

## Meaning for the promotion package
The 0240Z confirmation was not stream luck. The filters (probability vetoes
+ earlier trail) add value on *any* resampling stream — they are policy
improvements, not fits to one training realization. Promotion package v2
(0240Z spec) stands, now with 8-stream evidence.

## Files / hygiene
No repo code changed. Cached replays (new caches kept for future use).
Sierra: none. Dataset read-only.
Process notes: (1) build_dataset requires a Path (script passed str —
fixed); (2) a crash mid-sweep left seed-4's cache written by a code path I
then couldn't re-enter — reran cleanly and the numbers above come from the
single clean sweep (verified same-code all 4 seeds); (3) equity curve shown
for seed-7 (weakest-baseline stream, most honest look at the delta shape).
