# 2026-10-27T2110Z — v3 deployment number completes: recency 12mo uplift vs E3 = **+$491** (v2 +$481), DD further improved — "flat marginal" ≠ "no recent edge" (type: wake, ≤15min)

vram gate #11: unchanged (question ~6.5h; notify-hold to tomorrow).

## Completing 2010Z's honest correction with the RIGHT comparison
2010Z flagged TS54's marginal dPnL (v3−v2) as flat last-12mo (+$10).
True but potentially misleading for the decision: the deploy choice is
**against live E3**, not against v2. Ran the full recency triangle on
fresh streams 4–7 (last 12mo, one replay each — no new tuning):

| | E3 | v2 | v3 (+TS54) |
|---|---|---|---|
| mean 12mo PnL | +$2,548 | +$3,029 | +$3,039 |
| uplift vs E3 | — | **+$481** | **+$491** |
| per-seed v3−E3 | | | +224/+681/+304/+755 (4/4 +) |

(v2's +$481 reproduces 0105Z's +$520 discovery-window figure within seed
noise — independent consistency check.)

**Final v3 review framing (now complete and internally consistent):**
- Full window: +$279–398 over v2 (8/8), DD −20% cumulative vs E3.
- Recent era: **keeps the entire v2 recency uplift (~+$480–490, 4/4
  positive)** AND improves DD further (−1,481→−1,430 fresh).
- So TS54 = "same recent-era PnL as v2, lower DD, extra full-window
  PnL" — a strictly-superior-to-v2 *risk* profile whose PnL edge is
  earned mostly in the 2025 regime. That, plus the DLL-leg requirement,
  is the complete honest packet.

Candidate doc already carries the 2010Z slice; this triangle lands in
the same doc section next cycle if the review hasn't started — log is
sufficient for the dashboard trail.

Sierra: none. Datasets read-only. No code change. master fb1a019.
