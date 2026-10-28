# 2026-10-28T0258Z — suite-count correction #2: distinct offline unittest total is **75**, not 73 (per-file dot-form ok-counts re-verified; my loop used the slash path form which fails to import → false zeros) (type: wake, footnote)

Verified ledger (each file at its home branch, `python3 -m unittest
<dot.path> -v | grep -c 'ok$'`):
scale_guard 15 + repair_scale 15 + frame_bars 10 + watchdog 6 +
validate_frames 7 + maxbars_spec 7 + amt_engine 4 + dtc 11 = **75**.

(Tool gotcha for the record: `python3 -m unittest ml/test_x` runs "1
test" and FAILS at import — only `ml.test_x` works; earlier flaky "Ran
1"/zero counts were this. 0250Z's "73" was additive arithmetic from
memory again; this entry's table is the authoritative count.)

Substance of 0250Z unaffected (11 dtc tests green, branch e2d282fb).
