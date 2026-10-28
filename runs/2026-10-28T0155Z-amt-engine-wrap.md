# 2026-10-28T0155Z — menu-3/backlog: amt_engine ground-truth check wrapped in unittest (4 cases, incl. a NEW invariant) + silent script-mode crash fixed (type: wake, ≤20min)

vram gate #20: unchanged (next ping Thu if silent).

## Done (branch `algo-dev/amt-engine-testcov`, `18039d4a`)
Yesterday's self-correction backloged "wrap test_amt_engine in unittest"
— it was a main()-only script, so `discover` reported a **vacuous OK**
and the AMT-exactness gate (engine vs the DLL ground-truth dump) was
invisible to the suite. Now 4 real unittest cases:
1. **levels_match_dll** — all 7 level cols subTest'd, |err| ≤ 0.25 tick
   vs `data/amt_exact/`, with an `n > 3` guard so an empty merge can't
   vacuously pass (same failure mode I just caught in discover — now
   fenced inside the test itself);
2. **prev_range** vs dump's `prevR`;
3. **zone_boundaries** — 10 subTest'd probes around S4/S1/BAL/R1/R4;
4. **levels_from_bars smoke** — length + BAL-first-valid **plus a new
   invariant the original script never checked: BAL must be constant
   within a calendar day** (reference-bar driven). Passes.

`setUpClass` skips when the dump is absent, so CT runs (no dataset) stay
green under discover. **Script form also fixed:** plain
`python3 ml/test_amt_engine.py` previously died `ModuleNotFoundError`
(needs `-m` or repo-root cwd); module-level sys.path shim now makes both
invocations work — verified: script prints ALL OK rc=0, unittest 4/4,
ml discover now **34 tests** (was 30; total offline suite **62**).

## Notes
- First harness attempt used assertGreater(len(e),100) from assuming
  dump size; actual dump = 8-day snapshot (n=8) — guard corrected to
  n>3 (still catches empty-merge vacuity) rather than dropped.
- Verdict data unchanged: engine == DLL within tick tolerance on the
  snapshot (max_err 0.250 on S1/R1 = the documented half-tick rounding,
  same as before the wrap).

State: master fb1a019; 7 review-ready branches. Sierra: none. Datasets
read-only.
