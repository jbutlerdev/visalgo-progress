# 2026-11-01T1820Z — type(b): calibrate attempt #1 -> FAIL -> STOP (no massaging). Package-standard harness spec is NOT reconstructible from files; EA holds the bars AND (solemnly) their spec context.

## What ran (constitution #1)
Plumbing smoke (15d window): build_dataset 101,379 rows/1,321 days (1s),
collect_signals+replay OK.
`python3 scripts/calibrate_v2.py spec` (W's own call sequence; spec from the
IN-REPO run_adaptive_oos report header: 2022-10-18..2024-10-18,
2.0_5.0_0.45_trail_noFri, seeds 0-3) ->
  seed 0 pnl -218.89 n 253 | seed 1 -663.38 n 258 | seed 2 -191.44 n 247 |
  seed 3 -166.07 n 253
NON-ADJUDICATIVE numbers (harness not established): vs EA bars [6331,8083,
6742,6296] => FAIL by 4 orders of magnitude. ±1% gate: STOP.

## Diagnosis (evidence, not excuses)
(1) Bars' n-scale ~ matches repo grid (n 253 for that variant) but pnl does
not even match the repo's OWN report for same spec (report: 61.05) -> bars
were NOT produced by ml.wf_adaptive.main path at all.
(2) Bars are campaign-era v2 (TRAIL_START/STEP=1.75/1.75 — vs wf_adaptive
sim_pnl_trail hardcoded 2.0/1.0; sl=None trail-only; fee handling unknown)
-> produced by the campaign replay script whose canonical bytes perished in
stash 49aaa52c. My recreation = flagged NON-STANDARD. There is NO
file-reconstructible package-standard harness. STOP is correct.
## Asks of EA (bars-holder must also hold spec context):
a) exact window dates of the bars (start/end);
b) entry-point/command that produced [6331,8083,6742,6296] (script name +
   args as recorded in the 49aaa52c-era adjudication);
c) fee/tick treatment (TICK_USD/ENTRY_COST_USD applied? which values);
d) if no such context exists in your record -> the bars are unverifiable and
   re-baselining (new file-derived pins) is a Jeremiah/EA adjudication call,
   not my silent re-pin. I do not touch bars.
progress@f8d431a prior; script scripts/calibrate_v2.py @ visalgo e49f504.
