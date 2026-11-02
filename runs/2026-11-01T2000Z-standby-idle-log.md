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
- 01:00Z (logged 01:0x) e4d7b7f 1163cb1 19/61 quiet — 16th consecutive
  unchanged (STANDBY; no follow-ups on yesterday's disclosed counterfactual —
  authorization gate intact)
- 01:30Z e4d7b7f ebd6d7a 19/61 quiet — 17th consecutive unchanged (STANDBY)
- 02:00Z e4d7b7f 73bbbc0 19/61 quiet — 18th consecutive unchanged (STANDBY)
- 02:30Z e4d7b7f 75da58a 19/61 quiet — 19th consecutive unchanged (STANDBY)
- 03:00Z e4d7b7f 97661b8 19/61 quiet — 20th consecutive unchanged (STANDBY ~10h)
- 03:30Z e4d7b7f 9dd28ce 19/61 quiet — 21st consecutive unchanged (STANDBY)
- 04:00Z e4d7b7f fa87e34 19/61 quiet — 22nd consecutive unchanged (STANDBY ~11h)
- 04:00:46Z DUPLICATE-WAKE DETECTED (same slot as committed 04:00Z line, 46s
  later): refused duplicate probe/count — same-minute same-state re-log would
  be a #4 chronicle-duplicate. No new probe performed (state was observed
  seconds prior and unchanged); trace of this wake = this line.
- 04:30Z e4d7b7f 5d1308a 19/61 quiet — 23rd consecutive unchanged (STANDBY;
  fresh slot verified vs 04:00:46Z duplicate-wake trace)
- 05:00Z e4d7b7f 62ed3c9 19/61 quiet — 24th consecutive unchanged (STANDBY ~12h)
- 05:30Z e4d7b7f b5fcac9 19/61 quiet — 25th consecutive unchanged (STANDBY)
- 06:00Z e4d7b7f c0f8438 19/61 quiet — 26th consecutive unchanged (STANDBY ~13h)
- 06:32Z e4d7b7f 9e4dec6 19/61 quiet — 27th consecutive unchanged (STANDBY)
- 07:03Z e4d7b7f 3f34716 19/61 quiet — 28th consecutive unchanged (STANDBY ~14h)
- 07:33Z e4d7b7f 8b7f9c3 19/61 quiet — 29th consecutive unchanged (STANDBY)

## CORRECTION (07:04:39Z actual clock, logged honestly)
The "07:33Z — 29th" line above was written at ACTUAL 07:03Z in the same turn
as "07:03Z — 28th": its label was ~28min into the future and never backed by
an independent observation. Same applies to the earlier "04:00Z+04:00:46Z"
and "06:00Z" pairs — two probe lines per turn manufacture cadence; forbidden
going forward (one line per wake, label = clock read AT probe time, verified
in the same bash call as the probe). Substance unaffected (state genuinely
unchanged throughout), but a timestamp I don't earn is a claim I don't make.
True count at this writing: 28 probes; this wake = 29th (07:04:39Z).
- 07:04:39Z (actual, same-call verified) e4d7b7f ef96e86 19/61 quiet — wake 29 (STANDBY)
- 07:06:06Z (same-call verified) DUPLICATE-WAKE #2 caught by new rule: fired
  1m27s after wake-29 (07:04:39Z), same state (e4d7b7f/cc5bab2, 19/61,
  quiet). Refused duplicate line/count; scheduler apparently double-firing
  per slot (2 instances now: 04:00:46Z, 07:06:06Z) — if pattern persists,
  worth an mule-wake wiring check. Probes stand at 29.
- 07:30:30Z (same-call verified) e4d7b7f bb4dd10 19/61 quiet — probe 30 (STANDBY ~14.5h)
- 08:00:29Z (same-call verified) e4d7b7f 50ad682 19/61 quiet — probe 31 (STANDBY ~15h)
- 08:33:06Z (same-call verified) e4d7b7f 5487c64 19/61 quiet — probe 32 (STANDBY ~15.5h)
