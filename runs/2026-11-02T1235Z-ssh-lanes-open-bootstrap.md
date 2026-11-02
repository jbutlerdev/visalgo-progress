# 2026-11-02T1235Z — type(b): SSH LANES OPEN (Jeremiah) — bootstrap verified on .162; .61 not probed (not sanctioned yet)

## Command + raw output (constitution #1)
`ssh -o StrictHostKeyChecking=accept-new dev@10.10.199.162 hostname` ->
  Warning: Permanently added '10.10.199.162' (ED25519) to the list of known
  hosts.
  sierra-dev
  rc=0
Bootstrap per Jeremiah + AGENTS.md L213-217: key from $AGENT_SSH_KEY (7-line
PEM) -> ~/.ssh/id_ed25519 perms 600; key never echoed/printed (L227 rule).
AGENTS.md re-read at source first (files over memory; L74-76 .162 = experiment
twin, L225 targets, L248 vram note).

## Scopes as stated by principal (12:33Z)
- .162 dev: OPEN, key-auth VERIFIED (this entry = proof).
- .61 LIVE: HARD READ-ONLY (tail logs, read scid/state only; no
  orders/restarts/DLL pushes). NOT probed this wake — hostname not in the
  sanctioned enumeration; probe deferred to when a read-only purpose exists.
- vram: CLOSED pending Jeremiah confirmation.
## STANDBY: lifted-with-conditions? Not stated; treating as lanes-open but
no new self-generated Sierra work — awaiting concrete task (likely: scid/
state reads feeding tail-pull when re-stage lands; DLL-side ts54 leg someday
— both need explicit ask).
