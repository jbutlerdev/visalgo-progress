# 2026-10-27T2035Z — OOS re-pull: 10-27 now a COMPLETE session (to 16:00 close); per-seed dPnL unchanged (+91/+15/+57/−19) — verdict stable (type: wake, ≤15min)

vram gate #10 unchanged (notify hold → tomorrow if silent; question ~6h).

## Menu-4 continuation: complete-day OOS refresh
The 1540Z OOS window ended mid-session today (15:06Z pull). Session now
closed (16:00 ET), so re-pulled the .scid (scp 9 s), rebuilt the
normalized tail (1,374 bars; +58 incl. the last hour), rebuilt the merged
series, and re-ran both arms × 4 seeds from scratch (deleted old merged
parquet + OOS caches — no stale-input risk).

**Result: per-seed dPnL EXACTLY unchanged (+91/+15/+57/−19, mean +$36).**
The completed session added exactly one trade per stream (11–12 vs 10–11;
all exit='eod' — the new bars are the last hour's flatten, identical in
both arms since none sit in veto cells). E3's absolute PnL moved by the
mark-to-close (−357→−361 etc.), package's by less; relative ordering and
all caveats from 1540Z stand verbatim.

**Value of this cycle:** the OOS record is now on a CLEAN 17-session base
(no half-day), verified stable across the completion — i.e., the thin-
sample verdict wasn't an artifact of cutting the last day mid-tape. Next
OOS refresh when tail grows ~+3 sessions (weekend pull); v3 TS54 recency
on this window can re-run then too (cheap re-derivation).

Sierra: **live-readonly** (one scp pull; no writes). Datasets read-only
(/opt untouched; merged series in workspace scratch). No repo code change.
