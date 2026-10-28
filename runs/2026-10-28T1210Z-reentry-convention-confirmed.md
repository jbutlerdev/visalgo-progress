# 2026-10-28T1210Z — H-REENTRY declined at scan (kill #3): the never-measured "one entry per day" convention is **protective** — foregone second-crosses net −$13/trade (−$3,342 total, median −$41) (type: wake, ≤25min)

vram gate #39: unchanged (Thu ping next cycle).

## The untested convention
Every PnL ever logged rests on the replay `break`-ing after the first
entry (one trade/day). Nobody measured the foregone edge. Scan (count-
ing/means, seeds 0–1, pkg-standard): after the first trade's (approx-
imated) exit, a second qualifying cross appears on **24% (seed0) to
47% (seed1) of trade-days** — so the convention IS binding often.

**What the second trades would have earned: mean −$13.1, median −$40.6,
total −$3,342.** The late-intraday chase after an already-booked trade
is a LOSING cohort. Declined to formalize (no candidate to adopt; a
−$1,700/seed cohort can't pass any +$150 bar; formal run would be
ceremony).

## Why this matters (recorded as convention confirmation, like label-shape)
* The "obvious" upgrade (allow re-entries → more trades → more PnL) is
  **quantified as harmful** — the harness convention joins the label
  shape (1.5/2.5) as a load-bearing choice whose absence would quietly
  cost ~$3.3k/2-seeds (and DD, unmeasured, would likely worsen too).
* Mechanistically coherent: a second cross after a booked trade means
  the model is *still* extreme after the move already paid — late-
  chasing the same signal past its exhaustion. Same family as the
  zone-5-short and mid-conf-short findings (position stacking on
  extended moves loses; the proba system's persistence pricing noted
  at 1110Z covers this too).
* Caveat recorded: exit-bar for the second-cross window is an
  approximation (trail logic re-implemented in the probe); PnL stats
  themselves use the real sim_trail_p (solid); detection % approximate.

## Scoreboard discipline note
Not a falsification (no pre-registered candidate existed) — a
convention-confirmation diagnostic, like the ATR-decile table. 3C/18F/
1N unchanged. Scan-stage kills now 3 (ATRMIN, STREAK, REENTRY) vs 1
MIXED produced — hypothesis-generation lane ~4 min/kill, validated.

Sierra: none. Datasets read-only. No code change. Repro:
~/work/h_reentry_obs.py. OOS refresh armed 21:30Z tonight.
