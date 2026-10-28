# 2026-10-28T0910Z — packet docs synced to the deployable-definition audit: CANDIDATE_hprob gains the primary DEPLOYABLE table; CANDIDATE_ts54 gets its clean-definition note (type: wake, ≤10min)

vram gate #33: unchanged (Thursday ping next cycle if silent).

## Done (review-packet integrity — evidence and docs never drift)
* `CANDIDATE_hprob_bandgate.md` (tip `3f40644d`): new **DEPLOYABLE
  DEFINITION** section placed FIRST before the confirmation chain —
  noFri both arms (= activation config): pooled +$827 4/4, DD −1,486
  vs −1,820, recency +$534 4/4, pre-locked rule PASS; packet tables
  (+807/+481) explicitly retained as the historical discovery record,
  with repro pointer. Reviewer sees the decision-grade numbers first.
* `CANDIDATE_ts54_timestop.md` (tip `5cf2d02f`): definition note
  confirming TS scripts always carried the Friday skip (weekday()-grep
  sweep) — reviewer doesn't have to wonder whether the 0655Z-class bug
  touched these numbers. It didn't, and the doc now says so on its face.

## Process note (recorded per log-truthfulness)
First doc-edit attempt this cycle failed silently on both files: I
guessed anchors ("## Confirmation chain", "## Protocol") from memory
instead of grepping — one assert fired (caught by the guard I put in
the script), the other no-op'd (caught by the follow-up git status
showing nothing to commit). Fixed by grepping actual `^##` headings
first. Same class of lesson as the harness audits: verify structure
before editing; guards saved the record twice in one cycle.

## Queue state
Tonight 21:30Z: OOS tail refresh (new Wednesday session + zone-5
re-probe). Tomorrow (Thu): vram 3rd ping if silent. Standing: v2/v3/v4
review stack unchanged; Z parked MIXED.
Sierra: none. Datasets read-only. master fb1a019.
