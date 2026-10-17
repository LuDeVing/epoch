# NoveltyBench setup notes (2026-10-16)

Tags: [V] = read on the page via fetch (a small summarizer model read the page, so re-check exact numbers before citing). [M] = from memory or inference.

Sources:
- Paper: https://arxiv.org/abs/2504.05228 (v4, 9 Aug 2025), HTML https://arxiv.org/html/2504.05228v4
- Code: https://github.com/novelty-bench/novelty-bench (README raw: https://raw.githubusercontent.com/novelty-bench/novelty-bench/main/README.md)
- Site: https://novelty-bench.github.io
- Data: https://huggingface.co/datasets/yimingzhang/novelty-bench

## 1. Dataset
- [V] HF id: yimingzhang/novelty-bench. Splits: `curated` (100 rows), `wildchat` (1000 rows). Columns: id, prompt.
- [V] NB-Curated: 100 author-written prompts, 4 categories (randomness, factual knowledge, creative writing, subjectivity). 8 human answers each.
- [V] NB-WildChat: 1000 prompts picked from WildChat-1M with GPT-4o.
- [V] Repo `data/` also has human annotations and classifier training data.

## 2. Protocol
- [V] k = 10 generations per prompt. Temperature 1.0. No RAG, no tools.
- [V] Paper: "Each generation is independent and the model has no knowledge of previous generations." Default = 10 independent samples. The paper does not literally say "separate API calls"; independence implies it.
- [V] Repo flag `--sampling` (README examples use `regenerate`; other mode names not confirmed). Read src/inference.py.
- [V] Max tokens: paper does not state it. README: new submissions use `--max-tokens 2048 --reasoning-effort low`. v1.0 used 512 and truncated 20-55% of WildChat answers.
- [V] On Claude, max_tokens also bounds thinking, so the code doubles it. A response that burns its budget on thinking is recorded `[empty]`. Refusals are `[refused]`.
- [V] In-context regeneration (paper 4.3): after each answer, ask the model for a different one, keeping all earlier answers in the conversation. One multi-turn chat. Exact wording not seen.

## 3. Scoring
There are TWO versions. They are not comparable.
- v1.0 (the paper): [V] fine-tuned DeBERTa-v3-large, binary "functionally equivalent" classifier, sees only the first 128 tokens. About 1000 annotated pairs train, 100 test. Accuracy is reported inconsistently (79% in Sec 3, 71% in App A.4; F1 0.811). Quality = Skywork-Reward-Gemma-2-27B-v0.2, raw reward mapped to 1-10 (calibrated on 2400 MT-Bench generations vs GPT-4 scores).
- v1.1 (current README default): [V] one `gpt-5.6-luna` call per prompt reads all 10 responses in full and partitions them. `claude-opus-5` scores the first response of each group, 1-10. Needs OPENAI_API_KEY and ANTHROPIC_API_KEY. Judge agreement ARI 0.90-0.97 vs 0.29-0.80 for the classifier. Judge prompts: JUDGE_SYSTEM in src/partition.py, SCORE_SYSTEM in src/score.py.
- Formulas [V]:
  - distinct_k = number of equivalence classes among the k samples.
  - utility_k = (1-p)/(1-p^k) * sum_{i=1..k} p^(i-1) * 1[c_i differs from all earlier c_j] * u_i
  - Patience p = 0.8 (CLI `--patience 0.8`). Only the first sample of each new class earns credit. Duplicates add zero.
- Headline metrics: mean distinct (out of 10) and mean utility (1-10), per split. Paper headline: frontier models give fewer than 4 distinct answers in 10; larger models within a family are less diverse.

## 4. Compute for scoring
- v1.0 reward model: Skywork-Reward-Gemma-2-27B-v0.2. [M] 27B params = about 54 GB in bf16, about 14-16 GB at 4-bit. It does NOT fit 6 GB. 4-bit plus CPU offload would run, but slowly, and needs lots of system RAM.
- DeBERTa-v3-large [M]: about 435M params, about 1 GB fp16. Fits easily, runs on CPU too.
- v1.1 judges are API calls, no GPU needed. [V] README lists no GPU requirement.
- Smaller reward model [M, not verified on a page]: Skywork-Reward-V2 has small variants (about 0.6B to 8B). Using one changes the scale, so scores will not match published v1.0 numbers. We would have to rerun baselines ourselves.
- [V] Batch APIs: `src/batch.py` (judging) and `src/batch_generate.py` (generation) use provider batch APIs at half price. Flow: submit, status, collect.
- Generation of our method runs on the Claude API, so no local GPU is needed there.

## 5. Reported numbers
Paper Table 1 [V via summarizer; v1.0 scoring; I did not confirm which split(s) it averages]. distinct /10, utility /10:
- Claude-3.5 Haiku 1.94 / 2.50
- Claude-3.5 Sonnet 1.76 / 2.36
- Claude-3 Opus 2.04 / 2.67
- gpt-4o-mini 2.65 / 3.11
- gpt-4o 2.88 / 3.27
- gemini-1.5-pro 1.85 / 2.73
- gemini-2.0-flash-lite 2.83 / 3.20
- gemini-2.0-flash 2.81 / 3.17
- gemini-2.0-pro 2.25 / 2.64
- command-r7b 3.58 / 3.35; command-r 2.68 / 2.98; command-r-plus 2.79 / 3.08
- gemma-2-2b-it 5.66 / 4.63; 9b 3.25 / 3.93; 27b 3.03 / 3.77
- Llama-3.2-1B 6.74 / 2.81; 3.2-3B 5.10 / 3.24; 3.1-8B 5.24 / 3.76; 3.3-70B 2.49 / 2.87; 3.1-405B 3.20 / 3.39

Saved paper PDF (for checking tables and Figure 5): C:\Users\User\.claude\projects\C--Users-User-Desktop-AGI\d4f97148-54eb-4a3d-9538-2165b22b0c9f\tool-results\webfetch-1792147721716-x2sumt.pdf

- No Claude 4.x numbers found in the paper. The live leaderboard (novelty-bench.github.io) may have newer rows under v1.1, but the table did not load in my fetch. Open it in a browser.
- Prompting baselines (paper Sec 4.3, Figure 5) [V]. Numbers are in the figure only, not in text:
  - Resampling at T=1 (the default).
  - Paraphrasing each prompt: marginal gain.
  - System prompt "You are a producer of unique answers, and you strive to tell each user a novel answer to their question.": marginal gain.
  - In-context regeneration: best. Three models roughly match human diversity. GPT-4o and Gemini 2.0 Pro exceed human cumulative utility.
  - Human baseline: 8 authors on NB-Curated (dashed lines in Fig 5).
- The jury baseline that matters is in-context regeneration. We can rerun it ourselves with `--sampling regenerate`.
- Token-budget caution: regeneration re-reads earlier answers, so it costs more tokens than independent sampling. Count input plus output tokens in the equal-budget comparison.

## 6. Commands (from README) [V]
Install:

    pip install -e .      # or: uv sync
    export OPENAI_API_KEY=...
    export ANTHROPIC_API_KEY=...

Pipeline (README example, OpenAI mode):

    python -m src.inference --mode openai --model gpt-5.6-luna --data curated --eval-dir results/curated/luna --num-generations 10 --max-tokens 2048 --reasoning-effort low
    python -m src.partition --eval-dir results/curated/luna --concurrency 32
    python -m src.score --eval-dir results/curated/luna --concurrency 16 --patience 0.8
    python -m src.summarize --eval-dir results/curated/luna

- Steps 2-4 take `--version` (default 1.1; `--version 1.0` = DeBERTa + Skywork).
- Inference modes: `openai`, `vllm`, `transformers`. No documented `anthropic` mode in what I read [unverified]. Read src/inference.py. Fallback: write our own `generations.jsonl` in the repo format (fields: model, generations (10 strings), generation_key, generation_config [V, from HF page]) and run only steps 2-4. This also lets us plug in our divergent method.

## Open items
1. Read src/inference.py for the Claude path and `--sampling` modes (GitHub tree fetch failed once).
2. Confirm which split(s) Table 1 covers, and v1.0 vs v1.1 for leaderboard rows.
3. The judge model names (gpt-5.6-luna, claude-opus-5) came via a summarizer. Confirm in src/partition.py and src/score.py, and check judge cost and availability on our keys.
