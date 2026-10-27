# 2026-10-27T1910Z — H-TS (time-stop leg): CANDIDATE FOUND — TS=54 passes all 4 bars (+$398, DD −1,189), TS=48 also passes; fresh-stream confirm queued (type: wake, ≤25min)

vram gate #7: unchanged (hold notify).

## Menu-2 exit-family: time-stop stacked on package v2 (pre-registered)
Close any open trade at entry+maxbars bars (maxbars ∈ {36,42,48,54,60}).
Mechanism story (NEW leg — registry's time-stop family, never tested
stacked): stalled trades decay into SL hits; cutting them early frees
capital. Tail story (H-BE/H-TP3) predicted HARM — this is the adversarial
time-angle test. Bars: T1 ≥ +$150, T2 ≥3/4, T3 DD-abs no worse,
T4 recency ≥ 0. (36/42 rejected first pass; 48-60 re-swept per protocol
before any conclusion.)

| TS (bars) | dPnL | pos | DD | rec | verdict |
|---|---|---|---|---|---|
| 36 | +$23 | 2/4 | −1,196 | −275 | reject |
| 42 | +$62 | 2/4 | −1,136 | −156 | reject |
| **48** | +$210 | **4/4** | −1,153 | +9 | **PASS** |
| **54** | **+$398** | **4/4** | −1,189 | +115 | **PASS** |
| 60 | +$89 | 4/4 | −1,274 | +18 | T1-fail (converging to PKG) |

**Reading (disciplined, not sold yet):** shape is internally coherent —
constrained-set is nested (60 ⊂ 54 ⊂ 48 ⊂ ...), and marginal bands
behave: trades open 54+ bars are net-toxic (cutting them +$398), the
48–54 band is mildly protective (+210 vs +398 ⇒ the 48–54 band costs
~−$188), beyond 60 the leg is nearly inert. DD improves consistently
(−1,486 → −1,153/−1,189, ~20% better) — and unlike prior candidates this
ONE keeps PnL AND DD (prior DD-gains came with PnL loss). The tail story
survives its time-angle test in the right way: cutting *stalled* trades
(isn't progressing = the toxic tail subset) helps; cutting price-tail
access (BE/early-TP) hurts.

**Status: CANDIDATE, not confirmed.** Two cells passing (48+54) =
plateau-like, and the neighborhood (42/60) behaving as nested-set logic
demands. But per H-TRAIL protocol, promotion requires: (1) fresh-stream
confirm seeds 4–7 (queued next cycle — the 0310Z step), (2) honest check
that TS=54's +$398 isn't one-month concentration (monthly slice). If
both pass → package v3 proposal (E3 + vetoes + trail 1.75/1.75 + TS≈54)
as a separate review item, stacked on top of v2 — NOT folded into the
pending v2 decision (which stays clean).

State: master fb1a019; caches intact (TS replay adds no new caches).
Sierra: none. Datasets read-only. No repo code change.
