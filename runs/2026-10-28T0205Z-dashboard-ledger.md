# 2026-10-28T0205Z — menu-5: dashboard candidate-ledger panel — decision stack + falsification scoreboard now rendered on the cockpit page (type: wake, ≤20min)

vram gate #21: unchanged (next ping Thu if silent).

## Why
Everything Jeremiah needs to decide (v2 GO / v3 DLL / vram a-b-c) was
scatterable across 60+ run logs. The dashboard rendered only
stats+runs. Review friction on the decision stack = slower unblocks =
worse herd throughput. Made it one glance:

**New `#candidates` panel** (top of page), data-driven from
`docs/data/candidates.json` (new file; edit JSON, page follows — no HTML
changes needed to track future candidates):
* scoreboard line: **3 confirmed · 12 falsified · 1 neutral**;
* review-stack cards with status badges (AWAITING GO / AWAITING DLL
  DECISION / BLOCKED ON COEXISTENCE), branch name, one-paragraph
  evidence summary, and an explicit **"needs:" line** naming the single
  ask per item;
* collapsible falsification table (all 12 hypotheses + verdicts) —
  the scoreboard-discipline artifact that keeps the program honest,
  visible without cluttering the feed.
Badge variants .ok/.warn added (page had none). Markup + JSON validated
(this sandbox has no browser; visual polish deferred to next live view).

Content mirrors the canonical sources (CANDIDATE_hprob_bandgate.md,
CANDIDATE_ts54_timestop.md, deferrals ledger) — dashboard is a VIEW,
not a second source of truth; updated-stamp included so staleness is
visible.

State: master fb1a019; 7 review-ready branches; offline suite 62.
Sierra: none. Datasets read-only.
