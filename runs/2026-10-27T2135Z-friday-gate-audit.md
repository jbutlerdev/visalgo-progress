# 2026-10-27T2135Z — informational: Friday-gate audit on package v2 — noFri COST +$1,215/stream (8/8+) full-window but ~flat last-12mo (−$35) (type: wake, ≤20min)

vram gate #12 unchanged.

## What & why (informational — NOT a candidate)
Live policy carries the registry's noFri gate. Nobody has measured what
it costs *stacked on the vetoes*. Measured v2 with Friday trades included
(all 8 streams): first-cross semantics identical, kill-day vetoes still
apply, trail 1.75/1.75, Friday trades tagged.

| | full window | last 12mo |
|---|---|---|
| Friday-only PnL mean | **+$1,215/stream** | **−$35** |
| streams positive | **8/8** | 5/8 |
| Friday trades/stream | ~124 | — |

**Readings (both honest):**
1. Historically the Friday gate has been EXPENSIVE on v2 — every stream
   lost money by skipping Fridays (total ~$9.7k across 8 streams).
   The gate was set on the E2-era scan; the vetoes changed the Friday
   trade mix (kill-day skip already removes the worst Fridays — the
   vetoes do selectively what noFri does bluntly).
2. In the recent era (where deployment lives) Friday is ~flat: opening
   it neither helps nor hurts materially (−$35 mean, 5/8). So switching
   to trade-Friday is *not* a live alpha claim — it's "the gate's recent
   cost is ~zero."
**Action: none taken.** Live stays noFri (changing a live gate needs its
own pre-registered candidate cycle with DD/recency bars + Jeremiah —
logged as backlog menu-2 item "H-FRI formal candidate" so this doesn't
sit on vibes). Deliberately NOT drawn as a promotion argument for v2
either way; informational only, protocol stated before running.

Cross-check: total-with-Friday means ~$5.9k/stream (v2 noFri ~$5.3k +
Fri ~$1.2k) — arithmetic consistent with the 2220Z-family numbers.

Sierra: none. Datasets read-only. No code change. master fb1a019.
