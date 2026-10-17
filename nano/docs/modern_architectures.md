# Reference digest: how the strongest open language models of 2026 are built

Source material: DeepSeek-V4.1-Flash technical report (Sep 2026), Xiaomi MiMo-V2.6 technical
report (2026), the modded-nanoGPT speedrun record log (2024-2026). Extracted facts only; sizes
are for the full models, so each component must be scaled down to a 21M-parameter model.
This document is reference material for proposing changes. It is not an instruction to copy any
of it; a component counts only if it lowers validation loss at the fixed budget.

## 1. DeepSeek-V4.1-Flash (552B backbone, 8-16B active per token)

- Causal Encoder-Decoder (CED): 40 layers split into a 20-layer causal encoder and a 20-layer
  decoder. Decoder layers do not compute their own global keys and values; they project them
  from the encoder's final hidden state with per-layer weights. Sliding-window keys and values
  stay layer-local. Motivation: halve prefill compute; measured as loss-neutral at scale.
- Every layer has two attention branches: a global branch and a sliding-window branch (window
  128), outputs combined; the first two layers use the window branch only.
- Compressed Sparse Attention 2: global keys and values are shared across groups of layers
  (one "Full" layer computes them, the following layers reuse them), with a lightweight indexer
  selecting the top-512 entries per query. Only matters at long context (64K-1M).
- Mixture of experts in every block: 1 shared expert plus 384 small routed experts, 6 active
  per token, SwiGLU with clamping at 10; auxiliary-loss-free load balancing (a per-expert bias
  updated after each step) plus a tiny sequence-level balance loss (1e-4).
- Engram conditional memory: a hashed lookup table keyed by 2-, 3- and 4-gram token ids
  (8 hash heads per order, ~16M entries each, FP8), gated by the hidden state, inserted at two
  layers. Decouples memorization from computation; lookups are deterministic and prefetchable.
- Multi-stream residual (mHC): 4 parallel residual streams mixed by token-wise coefficients
  predicted from the stream itself; "single-pass" variant shifts the mixing coefficients by one
  block to allow kernel fusion.
- Optimizer: Muon for all linear-layer matrices (momentum 0.95, update RMS rescaled to 0.18),
  AdamW for norms and other vectors, Sinkhorn-balanced updates for embeddings; learning rate
  warmed up over 2000 steps, held constant for most of training, cosine decay in the last
  quarter; batch of ~100M tokens.
- Vision encoder and FP4 key-value cache: irrelevant at nano scale.

## 2. Xiaomi MiMo-V2.6 (1.02T total, 42B active)

- Hybrid blocks: 60 sliding-window attention blocks and 10 global attention blocks, in a
  repeating pattern of 6 window blocks then 1 global block; the very first block is global
  with a dense feed-forward to stabilize early learning. Window size 128.
- Grouped-query attention: 128 query heads, 8 key-value heads; query-key head dim 192,
  value head dim 128 (different sizes for keys and values).
- Mixture of experts in every block with 384 routed experts, 8 active, no shared expert.
- Multi-token prediction during pre-training: a small draft head predicts several future
  tokens; reported to improve pre-training quality, later reused for speculative decoding.
- Pre-training with AdamW, then a switch to a Muon variant with row-norm control for large
  batches; MXFP4 quantization-aware training in mid-training.

## 3. modded-nanoGPT speedrun innovations (small-model record log, GPT-2 124M scale)

Changes that each cut the time to reach a fixed validation loss, in roughly the order they
were found: the Muon optimizer; untied input and output embeddings; QK-normalization (RMSNorm
on per-head queries and keys); zero-initialized output projections of residual branches;
rotary embeddings; ReLU-squared activation in the feed-forward; logit soft-capping (tanh);
U-net style skip connections between early and late layers; "value embeddings" (an extra
token embedding added to the values of attention in some layers); learnable scalars on
residual and skip paths; sliding-window attention whose window grows during training
(FlexAttention); learning-rate schedule with a long constant phase and a linear cooldown;
batch size warmup; longer sequence length late in training; momentum warmup for Muon;
embedding learning rate decoupled from matrix learning rate; attention scale tweaks.

## 4. Scaling notes for a 21M-parameter, 50M-token run

- Experts: 8 to 16 small experts with 2 active keeps the active parameter count near the
  dense baseline; load balancing bias speed 0.001 is a reasonable starting point.
- Windows: a 128-256 token window at context 1024 already saves compute; a local/global
  pattern of 3:1 keeps at least three global layers in 12.
- Engram: table sizes near 65k entries per head, 2 heads per order, embedding width 64 per
  order; the learning rate for the table should be several times the matrix learning rate.
- Multi-stream residual and CSA2 are the most code and the least likely to pay at this scale.
- Every change must keep the non-embedding parameter count within 10 percent of 21.24M; the
  budget is fixed, so slower steps mean fewer tokens are seen.
