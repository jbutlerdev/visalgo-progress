# 2026-10-28T0400Z — H-SIZE ratio correction (4th log-truth catch this week): verified PnL +64% for DD +87% — sizing is risk-*worsening*, not "risk-neutral" as the 0355Z footnote guessed (type: wake, footnote)

Recomputed properly (h_size_base.py): v2 mean +$6,863 → sized +$11,243
= **+64%** (memory said +93%; that was conflating another number), DD
−1,254→−2,340 = **+87%**. So return/DD ratio *deteriorates* under
sizing — the rejection is stronger than stated, and the mechanism
reading sharpens: 2× on high-ATR days adds proportionally MORE drawdown
than return, because the vol-clustered loss tail is fatter than the
vol-clustered win tail. (The directional conclusion in 0355Z — reject,
and don't treat as free alpha — stands; one adjective was wrong.)

v2 stream means now on record for future deltas: +$6,331/+$8,083/
+$6,742/+$6,296 (seeds 0–3, cached sigs, CPU convention).

Sierra: none. No code change.
