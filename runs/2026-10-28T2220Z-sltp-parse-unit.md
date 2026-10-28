# 2026-10-28T2220Z — sltp 4th-field **parse unit: 15 cases ALL PASS** — the silent-failure seam of the time-stop now has a hardware-free gate (type: wake, ~15min)

## Why this item while B3 waits
The activation queue is: B3 (blocked on Jeremiah's SimMode flip or
alt-path pick) → B5 → C-staging. Rather than idle-pick a new
experiment, continued the **hardware-free verification stack** for
the fw24 feature. Trigger logic got its gate at 2120Z; today the
**parse** got one — the parse is the silent-failure seam: a bad read
makes maxbars OFF / wrong WITHOUT any log line complaining.

## `acsil/sltp_test.cpp` (commit a3f4fd4; `g++ -O2 && ./sltp_test`)
Mirrors the deployed parse verbatim (fscanf `"%lf %lf %lf %d"`,
`>= 2` accept, `a > 0.1 && b > a` gate, `t > 0` trail rule,
`mb >= 2 ? mb : 0`, defaults 1.0/4.0/0.0/0) — 15 cases, ALL PASS:
v4 line `1.75 5.0 1.75 54`; 2-/3-field era compat (maxbars stays 0);
mb=1 floored OFF (>=2 rule); t≤0 w/ maxbars ok; whitespace/newline/
extra-token robustness; garbage/empty/missing-file → defaults;
bad-gate (a≤0.1, b≤a) → defaults.
**The behavior worth knowing (documented by test):**
`"1.75 5.0 x 54"` — fscanf stops at the non-numeric 3rd token, so
`mb` is never read ⇒ **maxbars silently OFF**. A typo'd trail field
disables the time-stop with no error anywhere. The unit doesn't
change that (it MUST mirror the DLL), but it pins it so nobody is
surprised, and B3's on-box check (file content + LIVE TSTOP observed)
is the mitigation.

## Hardware-free gate stack for fw24 (grows while gated items wait)
1. python oracle: 7 semantics ✅ (1655Z)
2. C++ trigger logic: 8 cases ✅ (2120Z)
3. C++ sltp parse: 15 cases ✅ (today)
4. trade-service behavior on .162: pending SimMode (Jeremiah: flip
   on dev or direct backtest-engine alt-path; B3 DLL Sim1-pinned ready)

Sierra touched: none (local builds only). Datasets read-only.
Queue otherwise unchanged: B3 → B5 → C; GPU LSTM study (granted) and
B2-adjacent items behind it.
