# 2026-11-02T1559Z — type(b): vram lane OPEN (Jeremiah) — PROVEN; GPU deferred (human session holds 23.8/24 GB); ML plan folded

## Proof (exact command, raw output; constitution #1)
`ssh administrator@10.10.199.146 "nvidia-smi --query-gpu=name,memory.used,
utilization.gpu --format=csv,noheader"` ->
  NVIDIA GeForce RTX 3090, 24083 MiB, 0 %
(rc=0; key bootstrap per AGENTS.md; host reachable via same key as .61/.162.)

## AGENTS.md lane rules applied at once (nvidia-smi-first + DEFER-to-human)
`nvidia-smi --query-compute-apps=...` ->
  2020191, 256 MiB, /home/administrator/venv/bin/python
  2546335, 23812 MiB, /usr/local/bin/llama-server
`uptime` -> 16:01 up 220 days, 3 users, load 0.00
FINDING: llama-server occupies 23,812 of ~24,576 MiB — an ACTIVE HUMAN
SERVICE (util 0% = idle, but memory-committed; a torch CUDA context would
OOM/contest it). Lane rule DEFER => NO training fired. Re-check occupancy
before any job; only launch when memory.used is near-idle AND no human
session conflict (or Jeremiah pre-empts llama-server explicitly).

## Environment (read-only probes; nothing installed, no sudo)
Host has ~/visalgo clone, ~/venv python 3.12.3, torch 2.14.0+cu130,
cuda True. ML candidate runner identified by file: ml/lstm_wf.py — protocol
MIRRORS ml.xgb_wf (same FEAT_PREFIX, same 3-class 1.5/2.5 ATR labels, 60-day
train/5-day step, one position/day, SEQ 5-min bars; CPU-friendly defaults
SEQ=60/hidden=64/1 layer). Runs: python -m ml.lstm_wf [out_prefix].

## Campaign plan (folded; pre-registration gates ahead)
When GPU is free: (1) PRE-REG first (declared before any metric): fold
structure, label parity with ratified harness semantics, seeds, what PASS
means for an ML candidate (vs ratified XGBoost v2 baseline context), G3
DD binding from repo source, G4 date-window; (2) smoke: tiny fold run to
prove end-to-end (feature build from ES_front.parquet, cuda context alloc);
(3) single full run + artifact + run entry; (4) numbers to EA as always.
No training until (1) committed AND GPU occupancy cleared. vram discipline:
training jobs only, no sudo, defer to humans, no writes outside job dirs.
## STANDBY note: this is an ASSIGNED task (principal), so lane work permitted;
no other self-generated work.
