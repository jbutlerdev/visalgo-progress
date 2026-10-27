# 2026-10-27T0635Z — no-change on strategy; review-packet enrichment: trade-level economics of package v2 (type: wake, ≤15min)

No new Jeremiah response, dataset still frozen at 10-02, no foreign commits
— standby continues; no experiment run (queue discipline holds).

**Enrichment for the promotion review (descriptive, zero-risk):** ran
per-side/win-loss decomposition on the saved stream-5 pair (the stream
never used in any selection step — honest held-out view; already the
dashboard pair):

|              | E3          | PKG v2        |
|---|---|---|
| trades/PnL   | 569 / +$1,447 | 540 / +$2,269 |
| shorts       | 288 / +$1,474 | 270 / +$1,822 |
| longs        | 281 / −$27   | 270 / +$447  |
| PF           | 1.07        | 1.12         |
| win avg      | +$89.5      | +$83.8       |
| loss avg     | −$66.6      | −$65.5       |
| median trade | −$38.2      | −$29.2       |

**Reading (supports the mechanism claim):** the vetoes cut into the
*median* (loss-heavy) trades (−38→−29) while barely touching the winning
tail (win avg −6%) — and flip the long book from break-even to +$447.
Mean per trade +$2.5 → +$4.2. This is the "cut mediocre cells, keep the
tail" story the H-BE rejection (0510Z) proved in reverse. Appended to
`ml/CANDIDATE_hprob_bandgate.md` (branch commit, review packet only; no
code change, no master change).

Open items unchanged: (1) Jeremiah merge/activation of branch 856e21c4;
(2) dataset growth past 10-01 for the fresh-days re-check.
Sierra touched: none. Datasets read-only.
