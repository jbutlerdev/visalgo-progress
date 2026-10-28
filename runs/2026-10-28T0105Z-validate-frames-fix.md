# 2026-10-28T0105Z — menu-3 coverage: validate_frames tests (7) — **found+fixed a real crash**: orphan JSON (missing PNG) crashes the harvest validator (type: wake, ≤20min)

vram gate #19: unchanged (AM ping sent 0010Z; next ping Thu if silent).

## The bug (class: the exact case the tool exists to catch kills the tool)
`loop.validate_frames.parse_frames` collects orphan JSONs for *reporting*
but then iterated **all** JSONs and `os.path.getsize()`'d each `.png`.
A replay harvest with a half-written frame — JSON landed, PNG missing,
precisely the corruption the orphan detection was written for — crashed
the validator with `FileNotFoundError` mid-harvest, so a damaged harvest
couldn't even be diagnosed on the CT. Fix: iterate the json∩png paired
set; orphans still reported. One-line semantic fix, committed with the
tests that found it on `algo-dev/validate-frames-testcov` (`6bd10238`).

## Tests (7, stdlib tmpdir synthetic harvests; main() verdict via stdout)
* pairing + orphans both directions + non-frame files ignored; field
  extraction (bar_index/ohlc/png size);
* clean harvest → `problems: 0` + `mono=True`;
* OHLC invariant (high<open) → detected; bar_end_chart_time lying about
  the filename ts → `TS MISMATCH`; png under threshold → `PNG SMALL`
  (sparse stub files = instant size control); bar_index regression in
  day → `mono=False`.

**Why this file:** validate_frames is the gate every sierra-dev replay
harvest passes through before backfill consumes it (REPLAY_BACKFILL flow);
a crash there costs a whole replay session. Loop suite now 23 tests
(frame_bars 10 + watchdog 6 + validate 7); total offline 52
(+17 scale_guard +15 filter_policy +7 maxbars-spec +7 validate... 
= 52). Six review-ready branches now staged.

State: master fb1a019. Sierra: none. Datasets read-only.
