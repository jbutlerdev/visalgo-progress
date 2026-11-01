# 2026-11-01T1750Z — type(b): custody re-anchor (EA verified pre-patch sha) + pins-in-files audit

## Commands + outputs (constitution #1)
`sha256sum scripts/hgapday_replay_staged.py` ->
695a40b2e2ef33a98a712f019553ce14099c4c6087388e79fbf142aa99bd60f6 (HEAD 580ad9e
= bindings-confirmed version). EA independently verified e46fa29 =
4bc4fafd…47883ac0 EXACT (their lane, via API) — true at the time; my 17:05Z
bindings patch advanced the file. NEW canonical: 580ad9e / 695a40b2…; EA to
re-anchor (checkpoint sent). Old sha retained as provenance of pre-patch step-0.

## Pins-in-files audit (files over memory)
`grep -rn "6331" runs/ ml/ ~/progress/runs/` -> pins [6331,8083,6742,6296]
appear ONLY in my own run entries + script header (self-references); no
canonical locked-bars doc in either repo. Consistent with ratified custody:
bars live in EA memory (49aaa52c/215ff0ee), not repo files. Noted: if Jeremiah
wants a durable bars doc, EA-authored entry (not my memory-echo) is the
provenance-sound route.

## Gate-chain re-anchor (unchanged fact, restated once)
ES stream in-repo (101k bars to 2026-10-02) => sig-cache rebuild + calibrate
stand UPSTREAM-independently of re-stage; re-stage gates NQ tail only.
EA's latest chain phrasing placed re-stage first — flagged for correction in
checkpoint, so nobody idles waiting on the wrong dependency.
Next executable (next wake, budget-gated): arms rewrite to W.replay per 1705Z
confirmations; then calibrate attempt vs EA-held bars.
