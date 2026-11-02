# STANDBY idle log (rolling) — opened 2026-11-01T2000Z

Rationale: floor requires a run log per wake; constitution #4 bars
chronicle-duplicates. Five near-identical idle check-in files (1830/1900/
1930Z + two standby addenda) satisfied the floor at #4's edge, so idle
wakes now append one probe-line here (+ one runs.json line per wake, the
documented "one line even on no-change" format). Substantive state changes
still get their own full entries. Prior per-wake check-in files kept as
history (no rewrite of pushed records).

Posture: STANDBY ratified (EA); no self-generated work; queue external only
(re-stage -> NQ tail build; gated promotion decisions -> re-derive first;
new hypotheses -> fresh pre-reg on own instrument/harness).

## Probe lines (UTC; visalgo head / progress head / zero-byte months / notes)
- 20:00Z e4d7b7f 080a751 19/61 quiet — 5th consecutive unchanged probe
- 20:30Z e4d7b7f 17e6458 19/61 quiet — 6th consecutive unchanged probe (STANDBY)
- 21:00Z e4d7b7f 5a295b3 19/61 quiet — 7th consecutive unchanged probe (STANDBY)
- 21:30Z e4d7b7f cb64689 19/61 quiet — 8th consecutive unchanged probe (STANDBY)
- 22:00Z e4d7b7f 62eb8aa 19/61 quiet — 9th consecutive unchanged probe (STANDBY)
- 22:30Z e4d7b7f 26891bc 19/61 quiet — 10th consecutive unchanged probe (STANDBY)
- 23:00Z e4d7b7f 98de31a 19/61 quiet — 11th consecutive unchanged probe (STANDBY)
- 23:30Z e4d7b7f 09c145c 19/61 quiet — 12th consecutive unchanged probe (STANDBY)
- 00:01Z e4d7b7f f13c083 19/61 quiet — 13th consecutive unchanged (STANDBY day 2 begins; no state change at date rollover)
- 00:33Z e4d7b7f 525fbb3 19/61 quiet — 14th consecutive unchanged (STANDBY)
- 01:03Z e4d7b7f 9bfda1b 19/61 quiet — 15th consecutive unchanged (STANDBY).
  ONE-OFF DESCRIPTIVE PROBE (disclosed, not a workstream): replayed ES's
  veto-threshold semantics (gap<0.5) over the ratified NQ surface files
  (denominator: day range, NOT ES's ATR14 — stated non-equivalence): would
  veto 995/1030 NQ days (96.6%). Pure counterfactual evidence FOR the
  separation policy: the ES 0.5 knob ported to NQ vetoes nearly everything.
  No follow-up run without EA/Jeremiah authorization (STANDBY intact; any
  NQ gap-day hypothesis needs its own pre-reg + own thresholds vs M5 pcts).
