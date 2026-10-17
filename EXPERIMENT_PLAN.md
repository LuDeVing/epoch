# HTSA Experiment Plan: nano-replica benchmark

Status: draft v0.1, 2026-10-10
Purpose: a local, affordable, verifiable testbed where the HTSA loop proposes
changes to a modern LLM architecture and the proposals are judged by training
runs, not by opinion.

Related: `ARCHITECTURE.md` (the agent loop), `SYNTHESIS.md` (pending),
`research_notes/architectures/` (tech reports and extracted specs).

---

## 1. The idea in one paragraph

We cannot shrink a 500B-parameter model's weights, but we can re-implement its
architecture at 10 to 30 million parameters and train it from scratch under a
fixed compute budget. That nano replica is the baseline. The HTSA loop then
proposes modifications (architecture, optimizer, schedule, data order, anything).
Each proposal is trained under the identical budget and seeds and compared on
held-out validation loss. A plain agent at matched token spend proposes
modifications too, so we can isolate what the human-reasoning scaffold adds.
A small-scale win is evidence the loop can invent; it is not proof the invention
scales, and results are reported exactly that way.

## 2. Hardware and environment (measured 2026-10-10)

| Item | Value | Implication |
|---|---|---|
| GPU | NVIDIA RTX 4050 Laptop, 6 GB VRAM | models up to ~30M params at context 1024 in bf16; ~60M with checkpointing |
| CPU / RAM | i5-13450HX, 15.7 GB | fine for data loading and tokenization |
| Disk C: | 3.2 GB free | too small; nothing goes here except code |
| Disk D: | 162 GB free | environment, datasets, runs |
| Python | 3.14 system; no torch | pinned 3.12 venv on D: via uv |

Layout:
```
C:\Users\User\Desktop\AGI\          # code, docs, notes (this project)
  nano\                             # training harness and architecture modules
D:\AGI-lab\
  .venv\                            # Python 3.12 + torch (CUDA)
  data\                             # tokenized shards (FineWeb-Edu subset)
  runs\<run-id>\                    # one folder per experiment: config, log, metrics.json
  cache\                            # uv and HF caches
```

## 3. Baselines

Three nano architectures, all at the same parameter budget (~20M non-embedding),
same tokenizer, same data, same token budget, same seeds:

- **nano-GPT2** (reference): the modded-nanoGPT speedrun style baseline, so our
  numbers can be sanity-checked against a known ladder.
- **nano-MiMo** (Xiaomi MiMo-V2.6 family): interleaved local sliding-window and
  global attention; small MoE (8 experts, 2 active).
- **nano-DeepSeek-V4.1**: 20-layer causal encoder feeding 20-layer decoder scaled
  down to e.g. 6+6 layers; the decoder's global KV projected from final encoder
  states; MoE with 1 shared + N routed experts; an Engram-lite token-lookup
  memory (hashed n-gram embedding table). Compressed Sparse Attention 2 is left
  out at context 1024 (it only pays at long context); optional later at 8-16K.

Specs come from the tech reports in `research_notes/architectures/`.

## 4. Fixed budget and metric

- Token budget per run: 100M tokens of FineWeb-Edu (adjust after measuring
  throughput; target 20-30 minutes per run on the 4050).
- Context 1024, vocab GPT-2 (50257) or a 16K BPE if memory requires.
- Metric: validation loss (nats/token) on a held-out 5M-token shard, plus bits
  per byte so tokenizer changes stay comparable.
- Seeds: 3 per configuration for any claimed improvement. A change counts only
  if its mean beats the baseline mean by more than 2x the seed standard deviation.
- Secondary: wall-clock, peak VRAM, parameter count (improvements must not just
  be "a bigger model").

## 5. Staging

1. **Harness and baselines.** Single-file trainer with pluggable modules, fixed
   budget runner, seed control, metrics logging. Run the three baselines x 3 seeds.
   Record the noise floor.
2. **Rediscovery ladder (calibration).** Using nano-GPT2, hide 3-5 known
   speedrun improvements (e.g. a known optimizer change, a known attention or
   embedding trick, a known schedule change). Give the loop only the metric and
   the baseline script. Score: how many it rediscovers, at what token cost,
   versus a plain agent at matched spend. This is the benchmark that tells us
   whether the loop is any good before we spend compute on unknowns.
3. **Novelty on nano-V4.1 / nano-MiMo.** Point the loop at the modern baselines
   with no hints. Any seed-robust improvement is logged as a candidate finding,
   with its diff, metrics and the loop's reasoning trace.
4. **Scale check (optional, rented GPU).** Re-run the top 1-3 findings at
   124M-param speedrun scale on a rented 8xH100 hour to see whether they survive
   one step of scaling.

## 6. What the loop needs from the architecture (feeds back into ARCHITECTURE.md)

- `experiment` skill: edit config or module, launch training, parse
  metrics.json, append to the experiment ledger. Verification = the run itself.
- Experiment ledger in `memory/`: every tried diff with result, seed stats, and
  the hypothesis behind it (this is the "library" of partial results).
- Population search: recombine past diffs that each helped.
- Stopping and budget rules: experiments per day, when to abandon a line.
- Compute-matched comparison arm (plain agent) built into the harness.

## 7. Known limits

- 6 GB VRAM caps model size; MoE and Engram benefits may be small or absent at
  20M params. Report null results as null results.
- Seed noise at this scale is large relative to typical architecture gains.
  Three seeds is the minimum; five is better for close calls.
- The nano replicas are approximations of the published designs, not the
  models themselves. Every deviation is listed in the module docstring.
- No ladder of known records exists for nano-V4.1, so stage 2 uses nano-GPT2.
