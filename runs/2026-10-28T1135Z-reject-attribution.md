# 2026-10-28T1135Z — live attribution check (the scenario I pre-flagged at 0010Z): the 63 ORDER REJECTED lines are still exactly the PRE-RESTART cluster — 0 new since the 22:36Z restart (type: wake, ≤10min)

vram gate #38: unchanged (Thu ping next cycle if silent).

## Check (read-only .61)
Tail shows SELL_ENTRY rc=-1/-8999 lines → looked alarming; attribution
settles it: **ORDER REJECTED count = 63 = byte-count of the historical
cluster triaged yesterday 1410Z (all pre-22:36Z-restart, gate-reset
era)**. Current session (post-restart) has produced **0 rejections** —
consistent with overnight quiet (PERF advancing 154,579 calls, lastIdx
2093 = Wednesday pre-market, 0 ERROR).

## Why worth logging
This is precisely the misattribution risk I flagged in the 0010Z
post-restart note ("any tonight/tomorrow rejections get attributed to
the restart, not a bug"). Confirmed benign: no new entries attempted
since restart (pre-market; entries resume RTH ~08:30 CT). If rejections
reappear DURING RTH post-restart, that means the Auto-Trading gate was
never re-enabled — that's Jeremiah's morning-shift checklist item
(0010Z note stands; never self-fixed).

## Queue
21:30Z tonight: OOS tail refresh (Wednesday session + zone-5 re-probe).
Thu: vram 3rd ping. Review stack v2/v3/v4 unchanged (v3 now
input-complete incl. effort estimate).
Sierra: live-readonly. No code change.
