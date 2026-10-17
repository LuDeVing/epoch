# Nano-replica specifications

Date: 2026-10-10. Sources: `DeepSeek_V41_Tech_Report.txt` (sections 2.1-2.5,
4.2.1-4.2.2) and `MiMo_V2_6_technical_report.txt` (sections 2.1, 2.4, 3.1-3.2),
both extracted from the official PDFs in this folder.

Goal: three architectures at the same non-embedding parameter budget (~20M),
same tokenizer, data, token budget, optimizer and seeds, so that differences in
validation loss come from the architecture only. Every deviation from the
published design is listed, because the replicas are approximations.

## Common settings (held constant across all three)

| Setting | Value | Why |
|---|---|---|
| Tokenizer | GPT-2 BPE (tiktoken), vocab padded to 50304 | standard for nano-scale comparisons; swap later if memory requires |
| Context | 1024 | fits 6 GB VRAM; long-context components are out of scope |
| Non-embedding params | ~20M (+/- 10%) | 6 GB VRAM, 20-30 min runs |
| Norm / activation / positions | RMSNorm, SwiGLU, RoPE, no biases | both papers use these |
| Embeddings | tied input/output | saves ~19M params at this scale; both baselines get the same treatment |
| Optimizer | Muon for 2-D weight matrices, AdamW for norms, embeddings, routers, gates | DeepSeek pre-trains with Muon; MiMo switches to Muon mid-training; speedrun uses Muon. Holding it constant isolates architecture |
| LR schedule | warmup 2% then constant, cosine decay over the last 30% | mirrors DeepSeek's shape (constant then decay) compressed to the budget |
| Batch | ~0.5M tokens per step (grad accumulation) | measured after throughput test |
| Token budget | 100M tokens (adjust after throughput test; target 20-30 min per run) | |
| Seeds | 3 per config | noise floor |
| Metric | val loss (nats/token) on held-out 5M tokens; bits per byte reported too | |

## A. nano-GPT2 (reference)

Dense pre-norm Transformer, 12 layers, d=384, 6 heads x 64, SwiGLU FFN hidden
1024, RMSNorm, RoPE, tied embeddings. ~21M non-embedding params. This is the
modded-nanoGPT speedrun shape scaled down (the speedrun uses d=768, 124M).
Purpose: sanity check against a known ladder, and the base for the rediscovery
test in `EXPERIMENT_PLAN.md` stage 2.

## B. nano-MiMo (Xiaomi MiMo-V2.6)

Published design (Pro): 70 layers = 60 sliding-window attention (SWA) blocks and
10 global attention (GA) blocks, pattern "K SWA blocks then 1 GA block"; the
very first block is GA with a dense FFN; window 128; 128 Q heads / 8 KV heads;
head dims 192 (QK) / 128 (V); hidden 6144; MoE FFN in every block with 384
routed experts, 8 active, no shared expert; MTP speculative decoder (5 SWA
layers, predicts 7 tokens) used during pre-training; AdamW in pre-training,
Muon variant ("Muown") in mid-training.

Nano replica:
- 13 layers: block 0 = GA + dense SwiGLU FFN; then 3 groups of (3 SWA + 1 GA) = 12 hybrid blocks. Ratio 3:1 instead of 6:1 so there are at least 3 GA layers.
- SWA window 128 (as published).
- GQA: 6 Q heads, 2 KV heads, head dim 64 for QK and V.
- d=384.
- MoE in all hybrid blocks: 8 routed experts, 2 active, no shared expert, expert hidden 512, auxiliary-loss-free load balancing (per-expert bias, update speed 0.001) plus a small sequence-level balance loss (weight 1e-4), following the DeepSeek recipe since MiMo's report does not give its router details.
- MTP: off in the baseline. Listed as a candidate modification for the loop (MiMo says it improves pre-training performance).

Deviations: layer ratio (3:1 vs 6:1), head dims (64/64 vs 192/128), expert count and granularity (8/2 vs 384/8), router recipe borrowed from DeepSeek, no MTP, no vision/audio.

## C. nano-DeepSeek-V4.1 (DeepSeek-V4.1-Flash)

Published design: 40 layers = 20-layer causal encoder + 20-layer decoder
(Causal Encoder-Decoder, CED). Every layer has a global-attention branch and a
sliding-window branch (window 128), except the first two layers (SWA only).
CED: decoder layers do not compute global KV from their own hidden state; the
global KV of every decoder layer is projected from the final encoder hidden
state with layer-specific projection weights. SWA KV stays layer-local in all
layers. CSA2 sparse attention with cross-layer sharing: encoder uses compression
rate 2 in groups of 6 (first layer Full mode, five Reuse mode); decoder uses
rate 1 in groups of 4 (Full or Reindex, then Reuse); top-k 512; hidden 5120;
64 query heads x 512 dims with MLA-style query compression (1280); MoE in all
blocks: 1 shared + 384 routed experts, 6 active, expert hidden 2304, SwiGLU
clamped at 10; mHC (4 residual streams); Engram conditional memory at layers 1
and 14 (n-gram orders {2,3,4}, 8 hash heads, ~16M entries per head, 2048 dims
per order, context-aware gating, multi-branch integration, no causal conv);
Muon + AdamW + Sinkhorn-balanced embeddings; batch 100.6M tokens; 45T tokens.

Nano replica:
- 12 layers = 6 encoder + 6 decoder, d=384.
- Layers 0-1: SWA only (as published). Layers 2-11: global branch + SWA branch (window 128), outputs summed after separate output projections (the report describes an "additional branch of sliding window attention"; exact merge is not given, so the sum of two projected outputs is an assumption).
- CED: decoder layers 6-11 compute global K,V from the encoder output (hidden state after layer 5) with per-layer projections W_K^l, W_V^l; they compute their own Q and their own SWA K,V.
- Cross-layer KV sharing in the encoder (the Reuse mode of CSA2 without the sparse indexer): layer 2 computes global KV; layers 3-5 reuse it. Implemented as a toggle so it can be ablated.
- CSA2 compression and the sparse indexer: omitted at context 1024 (rate 1, top-k = all, i.e. dense global attention). Listed as a long-context extension.
- GQA: 6 Q heads, 2 KV heads, head dim 64. No MLA compression.
- MoE in all blocks: 1 shared + 8 routed experts, 2 routed active, expert hidden 512, SwiGLU clamp 10, aux-loss-free balancing (bias speed 0.001) + sequence-level balance loss 1e-4.
- Engram-lite at layers 1 and 6: n-gram orders {2,3,4}; 2 hash heads per order; table sizes distinct primes near 2^16; embedding dim 64 per order concatenated (192) and projected to d; context-aware gating (sigmoid gate from the layer's hidden state); hashing over raw GPT-2 token ids (the published tokenizer compression step is skipped). Learning rate scaled 5x as published.
- mHC: omitted in v1 (candidate modification for the loop).
- Sinkhorn-balanced embedding update: omitted; embeddings use AdamW.

Deviations: everything in the three "omitted" lines above, GQA instead of MLA, expert count and granularity, the branch-merge assumption, Engram size and the skipped tokenizer compression.

## Parameter accounting (target ~20M non-embedding each)

Rough per-layer costs at d=384: attention with GQA (6Q/2KV, dim 64) ~ 0.44M;
dense SwiGLU FFN hidden 1024 ~ 1.18M; MoE with 8 experts hidden 512 ~ 4.7M
total but only ~1.18M active per token (2 experts). Because MoE replicas hold
more total parameters at equal active parameters, we match on ACTIVE
non-embedding parameters (~20M) and report total parameters as a secondary
metric. The replicas must not win simply by being bigger; the harness logs both
counts for every run.

## What the loop is allowed to change

Anything: attention layout, window size, expert count, routing, Engram size and
placement, residual structure (mHC), MTP, optimizer settings, schedule, data
order, tokenizer. Each change is one experiment at the fixed budget. Changes
that raise active parameter count beyond the budget are flagged, not forbidden.
