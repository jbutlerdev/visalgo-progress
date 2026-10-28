# 2026-10-28T0310Z — menu-3: sc_client.client tests (7) — trade-direction mapping pinned; suite now 82 (type: wake, ≤15min)

vram gate #23: unchanged (next ping Thu if silent).

## Delivered (branch `algo-dev/client-testcov`, `e5565ce0`)
`sc_client/client.py` is the typed wrapper the model loop talks to —
its `ENTER_LONG→buy / ENTER_SHORT→sell / EXIT→exit` dict is precisely
where a typo silently flips trade direction with no other symptom.
Fake-bridge tests (which double as the SierraBridge Protocol doc for
whoever wires the real SCBridge post-Phase-0):
* HOLD short-circuits ("held", nothing reaches the bridge);
* side mapping asserted as an ordered list (the direction contract);
* symbol/qty/position passthrough;
* Action enum **values pinned** — loop/ and any persisted decisions key
  on those exact strings, renaming one is now a test failure;
* **documented-not-luck finding:** `Action` is a *str*-Enum, so raw
  string decisions (from JSON) are accepted, unknown action → KeyError.
  (My first test asserted strings must be rejected — wrong premise,
  str-mixin hashes equal; corrected to document the real contract
  rather than my expectation of it.)

7 green in 0.0 s. Suite: 75 → **82** (added 7; per-file method from
0258Z used — dot-form ok-counts, verified this cycle). 10 review-ready
branches.

## Standing backlog after this
Most menu-3 surface is now covered (scale_guard, repair_scale,
filter_policy, frame_bars, watchdog, validate_frames, maxbars-spec,
amt_engine, dtc, client). Remaining candidates: loop/forward_test.py
(needs fake ct_env — heavier), sim/ entry points, ml/feature-engineering
golden-value tests. Next cycle: forward_test dry-run paths if the
session-gate check passes cheaply, else sim/.

Sierra: none. Datasets read-only. master fb1a019.
