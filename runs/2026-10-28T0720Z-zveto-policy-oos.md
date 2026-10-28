# 2026-10-28T0720Z — Z-candidate: OOS validation ruled out (0/4 zone-5 shorts exist in chop) + policy gate landed as **default-OFF spec** (6 tests, branch zonenveto-policy) (type: wake, ≤20min)

vram gate #29: unchanged (Thursday ping next cycle if silent).

## OOS probe — the honest verdict on re-preregistration
Feasibility probe (counting only, no PnL peek): zone-5 SHORT entries
under package-standard replay in the OOS tail = **[0,0,0,0] across 4
seeds**. The chop tail contains NO zone-5 shorts → the OOS sign test
*structurally cannot* validate the Z gate (it would be
neutral-by-inactivity for the 4th time). Consequence: re-preregistering
Z against the tail is theater — rejected on design grounds, not effort.
Z's remaining honest evidence is what it already has: DD-improves 9/9
streams + recency +$193 4/4 + confirm +$210 4/4, with discovery PnL
straddling (−147 on one seed). **Disposition: MIXED, parked; un-parking
needs either a high-vol OOS window (a crash-like regime with real
above-R4 shorting — none exists in our tail yet) or Jeremiah's judgment
on the DD/recency case.** Not re-litigating the PnL bar.

## Pipeline prep that IS useful regardless: policy gate as spec
`ml/filter_policy.decide()` on the v2-lineage branch gains the zone gate
**exactly mirroring the backtest**, default `ZONE_VETO_SHORT_OFF = None`
→ live behavior byte-identical until GO + explicit wiring (same
OFF-by-default discipline as the prob vetoes). Kill-day veto keeps
precedence in the reason field (tested). Zone source documented:
current-bar zone per ml/amt_engine.zone_index; DLL mirror verified to
exist (NqAmtAgent.cpp:261) — so if Jeremiah ever approves, the port is:
pass zone to decide() in service + gate zone_of() at the DLL entry —
**both sides already have code paths staged or exist**.
6 new tests (21 on branch): default-off identical, zone-5 vetoes,
other zones enter, longs inert (first fixture attempt collided with the
kill-day long band — self-caught, fixture corrected to p below the
band so only the zone gate could fire), kill-day precedence, zone=None
inert.

## State
Branch `algo-dev/zonenveto-policy` (`a7c129bf`, off hprob-bandgate —
stacks UNDER v2, reviewable as v2+Z when Z is decided). Sierra: none.
Datasets read-only. No prod change. OOS tail refresh still armed for
post-Wednesday-close (new day → new sessions, re-check zone-5 presence
then).
