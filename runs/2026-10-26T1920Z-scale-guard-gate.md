# 2026-10-26T1920Z — nightly append gate hardened: shared scale_guard, 4 defects fixed (type: wake)

Cycle goal: follow-up from the repair_scale run — the backlog item said
"apply the outlier policy to `update_dataset`". It needed more than a
policy share: the nightly append gate (`align_scale`) had independently
grown the SAME three defects I fixed yesterday in repair_scale, **plus a
fourth** (a correction-ordering flaw that false-FATALs the real 10-07
failure mode). This gate is the guard that let the x100 tail INTO the
parquets, so its behavior is now locked down by tests.

## Findings (measured pre-fix, synthetic + real canonical ESZ26 bars)
1. **31x bad-tick blip "repaired" with a nonsense /10 factor** — would
   bake x31 corruption into every later bar of a nightly append.
2. **Negative close -> `ValueError` math domain error** — crash, no clear
   operator message.
3. **Whole-file x1000 scale -> FATAL** — median snap was hardcoded /100
   (`med > 5*ref_close`); any other power of 10 refused a fixable fetch.
4. **Correction-ordering flaw (new this run)**: the whole-file median snap
   ran BEFORE in-file flip repair, so an x100 tail skewed the file median
   -> whole file snapped /100 -> flip repair fired again -> double
   correction -> false FATAL on exactly the 2026-10-07 failure mode.
   (Caught by a realistic wet check: real ESZ26 bars with x100 tail from
   bar 10.)

## Fix (master `93198df`)
- New **`ml/scale_guard.py`**: single shared source of truth for scale-flip
  detection + policy (power-of-10 tolerance 1e-3 in log10, non-positive
  closes skipped, dry-scan == wet-plan, division for exact quarter-tick
  round-trips, flips/outliers split).
- `ml/repair_scale.fix_frame` now delegates to the guard — its 15 tests
  pass UNCHANGED (behavior contract; detector deduped with zero drift).
- `align_scale` rewritten: **flips-then-snap ordering** (relative
  correction first, then absolute), REFUSES outlier jumps + non-positive
  closes (bad .scid tick -> operator message + exit 2, no corruption),
  whole-file snap to ANY power of 10.

## Verification
- **30/30 unit tests pass** (15 new `ml/test_scale_guard.py` + the 15
  existing repair_scale contract; post-merge on master too). New tests:
  x100/x1000/x100-whole-file repair, 31x/94x refuse-not-corrupt, negative
  refuse, clean pass-through, volume never scaled, ordering regression
  (tail+x100 double-correction), mixed whole-file+tail.
- **Real-data wet checks (A-E)** on canonical ESZ26 Oct bars through the
  gate: A clean append bit-exact; B x100-tail fetch restored bit-exact;
  C 31x bad tick refused; D x100 whole file restored bit-exact; E 94x
  refused. (Scratch in ~/work; read-only mount respected.)
- No dataset files written anywhere; repo data/parquet untouched this run.

## Sierra touched
none.

## Pending / next
- pyarrow now preinstalled (package request f2fc8ab5 approved, thank you) —
  pip bootstrap dropped.
- Next candidates: `export/roll.py` roll-gap audit (back-adjustment
  continuity across roll days — same class of silent-corruption bug), or
  `loop/forward_test` observability; E3/B12C candidate experiment when
  fresh RTH data is the bottleneck.
