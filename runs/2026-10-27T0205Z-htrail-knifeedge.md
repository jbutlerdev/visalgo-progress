# 2026-10-27T0205Z — H-TRAIL: E3 exit cell is NOT a local optimum — 2 neighbors at +$195/4/4 → queued for confirmation (type: wake, ≤25min)

**Pre-registered question:** registry exit (trail trigger 2.0 / step 1.5 ATR)
was picked from a 24-cell scan (wf_exit_scan, 10-03) but never
neighborhood-tested. Cells: (trig,step) ∈ {(1.75,1.5),(2.25,1.5),(2.0,1.25),
(2.0,1.75)} vs E3 baseline, full window (2022-10-18..2026-10-02), cached
signals, seeds 0–3, entry layer = plain baseline. Self-check: base cell
reproduced 2220Z A to the cent.

## Results (mean dPnL vs baseline; baseline mean +$4,487 / DD −1,820)
| neighbor | dPnL | pos | mean maxDD |
|---|---|---|---|
| trig 1.75 (step 1.5) | **+$194** | **4/4** | −1,607 |
| trig 2.25 | −$1,346 | 0/4 | −1,848 |
| step 1.25 | −$311 | 0/4 | −1,843 |
| step 1.75 (trig 2.0) | **+$205** | **4/4** | −1,881 |

**VERDICT (pre-registered rule): KNIFE-EDGE** — two neighbors exceed +$150 at
4/4 → the registry cell is UNDER-FIT in both trail dimensions. Per protocol
the neighbors are QUEUED, not adopted (selection-on-4-streams is exactly the
freedom pre-registration exists to police).

## Reading
- Trigger asymmetry is steep and real: 2.0→2.25 costs −$1,346 (trail starts
  too late, gives back profits) while 1.75 gains +$194 4/4 — earlier trail
  activation (1.75 ATR favorable) locks in more of the path. Combined with
  step-up (1.75) also positive, the surface slopes toward (1.75,1.75).
- DD: trig-neighbor improves DD (−1,607); step-neighbor trades DD slightly
  worse (−1,881) for PnL — different characters, need the confirm battery
  (streams already cover resampling noise; a diagonal cell (1.75,1.75)
  should be included next cycle since both edges point there).
- This is the exit-layer mirror of H-PROB: mechanism exists (trail timing
  matters, strongly, monotonically-ish on trigger), unlike K30's flat noise.
  Registry exit-layer choice from 10-03 was a coarse-grid pick, not an edge.

## Next (queued, will pre-register before running)
Full confirmation battery for cells {(1.75,1.5),(2.0,1.75),(1.75,1.75)}:
recency-12mo + stream means + DD bars vs E3 AND vs H-PROB-alone (promotion
interaction: does the trail gain survive on top of the prob vetoes?). If
yes: E3+H-PROB+trail-up becomes the promotion package candidate; fw30 spec
updates agent_sltp.txt semantics accordingly (DLL already parameterized via
agent_sltp.txt "2.0 5.0 1.5" → "1.75 5.0 1.75").

## Files / hygiene
No repo code changed; replay only; Sierra none. Self-check assert on base
cell PASS (matches 2220Z +$4,255.49 seed-0 exactly).
