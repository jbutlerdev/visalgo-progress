# RUNBOOK — algo-dev sandbox recovery (minted by the 2026-11-07 incident)

**Why this file exists:** /root/work proved non-durable TWICE (stripped-wipe
00:30Z; recycle 19:33Z). Durable things: the two GitHub repos, the injected
GH_TOKEN, the platform-baked SSH key (~/.ssh since re-provision), agent memory.
Gap logs and recovery recipes live HERE, not in workdirs.

## On every wake, FIRST tool call = availability probe
`git/ssh/python3/curl` on PATH, CA bundle, bind mount (ls /opt/agent-data/visalgo/raw
| wc -l, zero-byte count), refs (fetch + rev-parse), GPU (read-only nvidia-smi via
ssh administrator@10.10.199.146). The probe's output is the ONLY sanctioned source
for cadence-line values (R-F-3) — never from memory, never from a prior turn.

## If the sandbox is stripped (no git/python/CA)
1. DO NOT fabricate a probe line. Honest gap = one notification to Jeremiah +
   one line to EA (first occurrence), then quiet gaps until fixed.
2. Request sandbox packages via the proper channel (request_sandbox_packages);
   they persist across sandboxes once approved.
3. NIX-KIT FALLBACK (pre-re-provision; worked 08:35Z 2026-11-07):
   - git: /nix/store/*git-2.55.0/bin/git (PATH-prepend per call)
   - CA:  /nix/store/*libressl*/etc/ssl/cert.pem  (144 certs) via GIT_SSL_CAINFO
   - python3/ssh: full nix paths
   - CAVEAT: env exports DO NOT persist across tool calls — re-export EVERY call
     (silent push failure = this, 99% of the time)
   - NEVER http.sslVerify false. Verification ON always; if it fails, escalate.
4. Gap-log: append to docs/RUNBOOK gap ledger below (this repo!), one line per
   wake with the observed clock + MISSING/GONE fields. Machine-sourced ts only.

## On recovery (tools return) — STOP-gate sequence
1. Clone both repos (env-injected token URL ONE-SHOT; scrub configs; grep
   x-access-token must be 0 in .git/config).
2. HEAD-verify vs last-known-good: visalgo algo-dev/ticks-builder + progress main
   (last values live in the newest runs/*.md line). ANY drift on my refs =
   STOP + ping EA before pushing anything. (Default-branch drift is triaged:
   authorship + dates + topology; reported, not escalated, if benign.)
3. Verify bind mount as its OWN field (tools-OK-but-bind-gone is a distinct
   platform failure). Bind healthy = count>0 AND spot-decode via
   databento DBNStore.from_file (iter yields records; databento>=0.90 API path
   is databento.historical.store / DBNStore.from_file, NOT databento.store).
4. GPU lane: read-only nvidia-smi only. llama-server resident = human session =
   DEFER (occupancy judgment is Jeremiah's call, never self-judged). No sudo.
5. Cadence resumes md-only (runs/*.md). runs.json ONLY via tools/dash.py append.

## Known state invariants (update on change, with evidence)
- refs @ 2026-11-07T19:40Z: ticks-builder e4d7b7f / progress daf6214
- bind @ 2026-11-07: 61 files, 19 zero-byte (Sep24-Mar26 re-stage queue)
- GPU key: platform-baked ~/.ssh (agent key; fingerprint n/a — .pub absent)
- stack @ rebuild base: pyarrow 15.0.2 numpy 1.26.4 xgboost 3.2.0 pandas 1.5.3
  databento 0.90.0; venv torch 2.14.0+cu130 on .146
- LSTM pre-reg 41b9044: single-blocked on GPU free (queue answered 'proceed')

## Gap ledger (append-only; strip after full recovery verified)
(none open — last closed 2026-11-07T19:33Z, RECOVERY-#2)
