# 2026-10-28T0550Z — **H-ZONEVETO discovery PASS 4/4**: veto zone-5 (above-R4) shorts → +$469 mean, DD better, recency 4/4 — fresh-stream confirm (seeds 4–7) queued next cycle (type: wake, ≤20min)

vram gate #27 (Wed): unchanged — Thursday ping armed.

## How we got here (honest sourcing)
All classical axes closed by 0520Z → per the steer, hypothesis-
GENERATION pass on the one column cached-but-never-used by the harness:
`zone` (AMT zone at the bar, DLL-aligned zone_c; live agent uses zones,
backtest never has). Observational scan (seeds 0–1 ONLY — deliberately
thin so 2–3 stay quasi-fresh): dense cells unremarkable, but **zone-5
(price above AMT R4) entry shorts bleed −$21/trade (n=63)** —
mechanism: late-chasing shorts at extreme highs mean-revert against.

## Formal test (bars locked BEFORE running; seeds 0–3)
v2 + veto shorts whose entry-bar zone==5 (prob-based kill-day vetoes
untouched — different instrument; ~32 trades/seed removed by design).

| bar | result |
|---|---|
| D1 dPnL ≥ +$150 | **+$469 ✓** (all 4 seeds: +656/+682/+392/+144) |
| D2 ≥3/4 positive | 4/4 ✓ |
| D3 DD-no-worse | −1,254 → **−1,168** ✓ |
| D4 recency ≥ 0 | +$137, 4/4 ✓ |

**Discovery PASS.** First discovery-stage pass since the confirmed
candidates — and it came from the feature-addition lane the steer
pointed at (new information, not threshold surgery), immediately after
three straight threshold/label rejections.

## What happens next (pre-registration discipline, unchanged)
Fresh-stream confirm on seeds 4–7 (never seen by scan OR discovery),
same bars, next cycle. If 4/4 (or ≥3/4 + mean ≥ +150): candidate H-
ZONEVETO CONFIRMED → packages become v2+Z / v3+Z (a third review item
for Jeremiah; DLL note: zone data IS available in the live agent — the
ACSIL DLL computes zone_c, so unlike v3's time-stop this may port
WITHOUT new computation, only new gating — to verify before claiming).
If confirm fails: #16→#17 falsification, discovery was luck, logged.
Watch-outs recorded: (a) seeds 0–1 informed the scan's cell choice —
confirm seeds are the true test; (b) zone-5 short n≈32/seed — effect
size must survive on unseen streams; (c) multiple-cells-in-scan
concern — only ONE cell was pre-registered post-scan (no cherry of the
other cells; the −10/−11 long cells at zones 1/4 deliberately NOT
touched).

Sierra: none. Datasets read-only. No code change. Repros:
~/work/h_zone_obs.py + h_zoneveto.py.
