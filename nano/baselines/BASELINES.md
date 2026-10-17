# Baseline history

Each promotion: the candidate that became the new baseline and the verdict it won on.

## v2 (2026-10-15T00:28:14) from v1

- run: arch-2__nano__gpt2_50m__scaffold__r0, candidate strongest_scaled, source hash 8e5673d520b3
- hypothesis: the dense skeleton of the strongest 2026 open models (DeepSeek-V4 / Kimi K3) scaled to 21M: latent attention, QK-norm, four-stream residual mixing
- change: Attention, Block.combine, Config.d_ff 1077
- verdict: {"status": null, "n": null, "mean": null, "delta": null, "p": null, "gain": null}
- note: owner's decision: the strongest scaled-down architecture (one seed, 4.0939) becomes the baseline to improve

