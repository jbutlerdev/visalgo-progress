# 2026-10-28T1320Z — OOS refresh pipeline consolidated (ml/oos_tail_pipeline.py) — validation exposed a SECOND tail anomaly (monster bars from 09:35Z 10-07); pipeline checkpointed, tonight's refresh runs the proven manual path (type: wake, ≤25min)

vram gate #41: unchanged (Thu ping next cycle).

## Shipped (branch algo-dev/oos-pipeline)
Ad-hoc steps used live 3× (1515Z pull-audit, 2000Z OOS, 0325Z re-runs)
consolidated: `python3 -m ml.oos_tail_pipeline --scid <path> --since
<date> [--repo] / --validate --banked <parquet>` →
read_scid → resample_5m → **flip repair (scale_guard wet loop) →
align_scale vs frozen ref** → RTH filter → merge (dedupe keep-last) →
writes oos_repo parquet. Reuses canonical pieces (export.scid,
update_dataset.align_scale, scale_guard scan/classify/rescale) — no
re-implementation.

## Validation-mode finding (this is the valuable part)
Running --validate against the banked tail: scan_flips reports the
documented 02:49Z x100 flip + repairs it, but leaves **1,112 "monster"
bars (close >20,000) starting 2026-10-07 09:35 ET** whose prev-close
ratio is ~0.0100 — classify() rejects them as non-power-of-10 outliers
(99.51x ≠ 100.0 within SCALE_TOL), and align_scale then FATAL-refuses.
**Two readings, TBD next cycle** (each resample costs ~3–4 min, budget
hit): (a) the 09:35 flip is a GENUINELY bad tick cluster in the scid
the banked tail also quietly kept?? — banked audit showed NO monsters,
so more likely (b) the scid file grew between the two copies
(this file was re-pulled 20:31Z; the live writer appends; 09:35 bars
may post-date the banked pull and carry a second x100-ish bug whose
prev-close ratio is off-tolerance because the bar right BEFORE it is
itself mid-bug). Note the banked tail (OOS foundation, MANIFEST-clean
by provenance from 15:06Z copy) ends 16:00 ET with clean scale —
tonight's refresh must re-pull FRESH anyway.

## Tonight's 21:30Z refresh runs the PROVEN manual path (unchanged)
pull → (flip repair by hand as in 1515Z audit) → merge → signals →
replay. The pipeline becomes the primary path once validation passes
on a fresh pull — validation gate is exactly why I built it: it caught
a case the manual flow handled by eyeball, and tonight it either passes
(clean upgrade) or the manual path takes over (status quo). Zero risk
either way.

Files: ml/oos_tail_pipeline.py (branch algo-dev/oos-pipeline; unmerged
until validation passes). Sierra: none. Datasets read-only.

## Footnote (record correction, same cycle)
The log said "branch algo-dev/oos-pipeline" while the commit had
actually landed on local master (push correctly rejected by the
remote's non-ff rule). Fixed within the cycle: commit moved to
algo-dev/oos-pipeline (dffcc920), master reset clean to fb1a019.
The branch-until-validated policy was the intent all along; the log
now matches git reality.
