# 2026-10-27T1445Z — menu-3: loop.frame_bars offline coverage (10 tests, found 1 real bug); .61 auth DEGRADED (watch item) (type: wake, ≤25min)

Vram retry at cycle start: still refused (no binding landed) — menu-6
remains blocked; not hammering (retry once per cycle).

## Menu-3 delivered (branch algo-dev/loop-testcov, commit pushed)
10 offline tests for `loop/frame_bars.py` (SFT-label-critical pure
functions): NAME_RE accept/reject, **atr14 convention locked** (Wilder TR
incl. prev-close gaps, min_periods=14, first-bar TR=H−L — hand-computed
windows catch drift to EWM/min_periods=1, which would make labels see
'ATR as volume noise'), build_day_bars sort/contract, forward_outcomes
shift semantics (fwd1_range = NEXT bar H−L; tail NaNs; range only h=1),
load_frames ingest + bad-name skip. **Suite found one real bug:**
empty-dir load_frames returned a no-column frame that crashes downstream
`.empty`-path users — typed-empty guard added. Two fixture-arithmetic
slips were mine, caught by hand-computation before commit. 10/10 green;
ml suite still 30 OK. (Picks up the brief's loop/ coverage item under the
corrected 24/7 law — no session excuse.)

## Watch item: .61 ssh auth degraded (menu-4 blocked mid-cycle)
Timeline today: standard askpass pattern worked at 08:03, 10:00, 12:01,
14:00–14:06 (14:06 listed ESZ26_FUT_CME.scid fine) → **14:31 onward:
`Permission denied` + "Too many authentication failures"** from the same
working command (fresh askpass inline, NumberOfPasswordPrompts=1, plain
pattern — all refused). Backed off after ~4 attempts (no brute-force
pattern from my side; likely server-side rate-limit/faillock after
today's many short sessions, or a password rotation ~14:10Z). NOT using
the vram blocker notification to ask for anything beyond: if Jeremiah
sees it — a `faillock --reset` on .61 (or telling me the password
rotated) unblocks the menu-4 fresh-.scid-tail audit; I keep backing off
and retrying at ≤1 attempt/cycle. Live agent itself unaffected (last
healthy read 14:06Z; this is sshd-side only).

## Scoreboard / state
Menu-1 done (9/9, seed 8 +$659). Menu-3 done (this). Menu-4 partial
(audit script understood; pull blocked). Menu-6 blocked (vram auth).
master 47a0992; new branch pushed. Sierra: none this cycle (backed off).
