# 2026-10-28T1110Z — DLL portability assessment for the v3/v4 decisions: time-stop ≈ 30–60 lines (trail state machine already has entry-bar tracking); zone-veto confirmed gating-only (type: wake, ≤15min)

vram gate #37 (Wed): unchanged. H-STREAK declined at scan (yesterday's
outcome carries no signal - proba system already prices persistence;
2nd clean scan-stage kill).

## Why this cycle (decision-support, not tuning)
Tuning lanes exhausted (registry joint optimum complete, 3C/18F/1N).
The binding constraint on profitability NOW is Jeremiah's review stack
(v2 GO / v3 DLL / v4), and the review lacks one input: **how much work
is the DLL actually?** I read the source and answered it:

**Time-stop (v3's blocker) — MUCH cheaper than feared:**
`AgentFrame.cpp` fw23 trail machinery already maintains exactly the
state a time-stop needs: `g_AgTrDay` (entry day), `g_AgTrBarKey`
(entry bar "YMD.HHMM"), `g_AgTrAtr0`, and a per-bar update block that
fires precisely when a NEW bar closes since entry (line ~2201:
`barKeyT != g_AgTrBarKey`). Port = (a) `int g_AgTrBars` incremented in
that same block, reset at entry; (b) when `g_AgTrBars >= maxbars` and
position open → market close (mirror of the flatten path); (c) 4th
sltp-file field ("2.0 5.0 1.75 54"), default 0 = OFF; (d) validation =
the 7 `ml/test_maxbars_spec.py` semantics as a C++-harness checklist.
**Estimate: 30–60 lines, one file, no new computation.**

**Zone-veto (Z gate) — confirmed gating-only:** `zone_of()` exists
(NqAmtAgent.cpp:261); entry blocks (AgentFrame ~2290/2335) have the
bar; gate = compare at the ENTER_SHORT decision. (Status unchanged:
Z is MIXED/parked - this is cost-of-readiness, not a recommendation.)

**Risk note (unchanged interlocks):** any future DLL change goes
mingw-cross → sierra-dev (*.bak timestamped, RELOAD, md5 + LOAD
verify) → contract tests → only then a Jeremiah-gated .61 deploy;
Auto-Trading gate never self-fixed.

## What this gives the review
v3 decision now has: effect (+$302 9/9 pkg-std, DD better all 9),
mechanism (long-side carried, 0745Z), contract spec (7 tests), and
**implementation cost (≈1 dev-hour + test harness)**. v4 adds the Z
gate (+$394 TS-complement; Z component MIXED). No new numbers needed
from me to start.

Sierra: none. Datasets read-only. No code change. Queue: OOS refresh
21:30Z tonight; Thu vram ping #3.
