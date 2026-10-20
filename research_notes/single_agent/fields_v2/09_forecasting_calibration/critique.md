# Critique: forecasting and calibration (round 2)

## What is solid
- Human overconfidence and the planning fallacy are old, replicated findings. They support one step: take the outside view before the inside view. They are human data, so transfer to an LLM is by analogy.
- LLM forecasting systems with retrieval and ensembling get close to the human crowd, and experts still lead (about 0.017 Brier). Five sources agree, but most are preprints and one is an organisation page.

## What is shaky
- The core Tetlock story (training, teaming, superforecaster habits) is now contested. The 2025 reanalysis uses the same GJP data, so it is one dissent, not a replication. Treat "base rates, decomposition, small updates" as plausible heuristics, not tested causes.
- Reasoning-model calibration is contested. Yoon (better in 33 of 36 settings) conflicts with Mei (overconfident, worse with depth). All three papers are preprints. The split may be by task type (reasoning vs factual) and by model, which nobody here tested.
- Extremizing, semantic entropy, P(True), the verbalised-confidence ranking and the consistency check each rest on one paper. Several lines are the same paper fetched three times, so line counts overstate support.
- Memory or snippet only: Tetlock 2005 numbers (memory), Mellers 2015 and Satopaa 2021 (snippets), Mellers 2014 training details (snippet), the Wikipedia superforecaster percentages (weak), and the abstract-only items Lu 2025, Turtel 2025, Wildman 2025.
- The Schoenegger result uses 31 questions. Do not lean on its finding that averaging beats feeding in the crowd number.

## Gaps that would change agent design
1. No test of a forecasting procedure (reference class, decompose, update) run by an LLM at equal tokens against plain answering. This is the key gap. Our own data (scaffolds hurt single-answer tasks) says a gate is needed.
2. Correlated samples: extremizing and agreement-as-evidence both assume diverse voters. No source measures how much confidence signal survives when all voters are one model, or one model with varied prompts or retrieved facts.
3. Does verbal or sampled confidence predict correctness on open-ended work (design, research), not only QA and binary events? Almost everything here is QA or binary.
4. Selective prediction: when to abstain or escalate, and how a router built on confidence performs. Not covered.
5. Most calibration papers use 2022 to 2024 models. Current Claude-class models may differ.
6. Learning loop: does an agent that logs its own resolved predictions and recalibrates on its own history improve? Not covered.

## Risks of error
- Leakage in LLM forecasting benchmarks other than ForecastBench; pastcasting depends on how well the web is frozen.
- The parity-by-November-2026 figure is a projection with a wide interval, from an organisation with a stake.
- The earlier brief had a wrong author order and a withdrawn arXiv ID. Both are fixed in the evidence. Other earlier-brief citations (Farquhar 2024, the 2019 Journal of Politics teams study, 2505.14489, 2506.18183) were not re-fetched here.
