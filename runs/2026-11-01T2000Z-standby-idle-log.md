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
