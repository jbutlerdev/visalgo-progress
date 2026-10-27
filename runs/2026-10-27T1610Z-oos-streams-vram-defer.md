# 2026-10-27T1610Z — OOS stream-variance (4 seeds on the 17-day tail): package +$36 mean, 3/4 — vram DEFERRED (GPU fully held by llama-server) (type: wake, ≤25min)

## Menu-6 guest-ethics check: DEFER (correct per policy)
vram `nvidia-smi`: GPU util 0% **but 24.1/24.6 GiB held** — a 10-day-old
`llama-server` (administrator, serving `qwen3.8-27b-visalgo` to the herd)
holds 23.8 GB; ~460 MB free. Utilization is idle but memory is not, so an
LSTM job cannot allocate and an OOM-kill contest would most likely pick
the new big job — exactly the contention guest ethics forbids. No job
submitted, nothing touched on vram beyond read-only queries. Retry next
cycle; if the holder persists days, @notify Jeremiah (he owns the box).

## Menu-1 extension: OOS on 4 training streams (pre-registered extension of 1540Z)
Same 17 post-freeze days, harness fold protocol, SEED=0..3:
| seed | E3 | PKG v2 | ΔPnL |
|---|---|---|---|
| 0 | −$357 | −$266 | +$91 |
| 1 | −$433 | −$417 | +$15 |
| 2 | −$431 | −$374 | +$57 |
| 3 | −$432 | −$450 | −$19 |
| **mean** | **−$413** | **−$377** | **+$36 (3/4 +)** |

**Reading (honest):** the chop regime is stream-robust (E3 ≈ −$413 across
all four seeds — the window is hard, not unlucky), and the package keeps
its relative ordering (mean +$36, DD better in 3/4) but the margin
collapses to noise-level at n≈10 trades/stream. No confirmation claim;
consistent-with-4y-plateau is all 17 chop days can support. Accumulation
continues; meaningful OOS at ~60+ days. One honest flag: seed-3 Δ negative
— reported as-is, no seed selection.

State: master fb1a019; fuel tail in workspace; caches clean. Sierra: none.
Datasets read-only. No repo code change.
