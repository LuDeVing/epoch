# ARC methods: what public work says about our improvement ideas

Date: 2026-10-16. Status key: V = checked on the page this session. M = from memory or a search snippet, not checked on the page.

## Table: idea -> evidence -> gain -> source

| # | Idea | Evidence | Gain | Source | Status |
|---|------|----------|------|--------|--------|
| 1a | Augmentation-scored selection (Franzen et al., ARChitects-style) | Same LLM scores each candidate under 16 augmentations (rotate, transpose, recolour, reorder). Product of the probabilities picks the top 2. | Top-2 by sampling prob only: 62.5%. Product over augmentations: 67.6%. Full method 71.6% on public eval. Product beats averaging by about 5 points (66.6 -> 71.6). Needs token likelihoods, so a local model. | https://arxiv.org/html/2505.07859v2 | V |
| 1b | Augmentation as stability criterion | 2024 winners chose answers that stay stable under augmentation. 53.5% private eval. | No separate ablation on the page. | https://arxiv.org/html/2412.04604v2 | V |
| 1c | Prompt-time augmentation with a closed API model (our case) | No clean published number found. Greenblatt varied prompt format and representation (V0, V1, V1.1, V2 with input-output diff) but gave no per-variant gain. | Unknown. | https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt | V (for what he did) |
| 2a | Sample plus one revision round (Greenblatt, GPT-4o) | About 5000 initial plus 3000 revision samples per task. One revision round only. Revision fixed about 20% of remaining wrong programs. Test 37% -> 50%. | +13 points on test (+6 on train). About +3 points per doubling of samples. | same blog link | V |
| 2b | Same method, ARC Prize 2024 report | GPT-4o, thousands of programs per task, debugs the best ones. 42% public eval (43% semi-private). | Report estimates 100M programs/task for 85%. | https://arxiv.org/html/2412.04604v2 | V |
| 2c | Berman evolutionary (Claude Sonnet 3.5, Python) | Up to 500 functions, 31 dynamic prompts per task, several generations. 53.6%. Later Grok-4 with English instructions: 79.6% on ARC-1, about $8.42/task, up to 40 candidates and 36 prompts. | Gain per generation not found. | https://jeremyberman.substack.com/p/how-i-got-a-record-536-on-arc-agi ; https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again | Search snippets only (M) |
| 2d | Poetiq / refinement loop (ARC Prize 2025 report) | Refinement = explore, verify, feed back until training pairs fit. Gemini 3 Pro on ARC-AGI-2: 31% ($0.81) -> 54% (~$31/task). | +23 points at about 38x cost. | https://arcprize.org/blog/arc-prize-2025-results-analysis | V |
| 2e | SOAR (self-improving evolutionary synthesis) | Sample + refine with execution feedback, fine-tuned. 52% public test. | Breakdown not read. | https://arxiv.org/abs/2507.14172 | Abstract V, rest M |
| 3 | Induction + transduction (Li et al.) | Induction first. If any program fits all examples, use it. Else fall back to transduction. No agreement check. 20k programs sampled. | Induction 38.0%, transduction (TTT+rerank) 43.0%, ensemble 56.75% (2 tries, 400 public val). About 9% of passing programs are false positives. | https://arxiv.org/html/2411.02272 (first 100k of 142k chars read) | V |
| 4 | Hypothesis first, then code (Wang et al.) | Random 100 tasks. Several NL hypotheses, each coded and verified on examples. Hypotheses filtered by LLM summary. | Direct 17% -> 30% automated -> 33% with human pick. | https://arxiv.org/abs/2309.05660 | V |
| 5 | Selection among passing programs | Greenblatt: majority vote over passing programs, top 3 outputs. Fallback if fewer than 3 distinct outputs pass: weight by closeness to expected. Drops outputs equal to the test input. Franzen: likelihood product. Li: induction first. | Franzen reports no voting baseline. | links above | V |
| 5b | Attempts allowed | Two attempts per test input. Exact match, no partial credit. | n/a | https://arxiv.org/html/2412.04604v2 | V for the rule; M for ARC-1 pass@2 detail (third party) |
| 6 | Leave-one-out validation of programs | No ARC paper found that does leave-one-out on programs. Closest: Berman's repo scores NL instructions by cross-validation (an LLM executes them on training grids). Li et al. report the false-positive rate (about 9%) but do not use LOO. | No published number. | https://www.sourcepulse.org/projects/18562094 | Snippet only (M) |
| 7 | Haiku / small models on ARC-1 with sampling | No official figure found. A third-party aggregator lists Haiku 4.5 on ARC-1 at "0.477" (scale unclear, unverified). ARC-AGI-2: Haiku 4.5 about 4.0% (32K) and 2.8% (16K), third party. The strong sampled results above are all big models. | Unknown. | https://benchmarklist.com/benchmarks/arc_agi_1/ ; https://llmrun.dev/benchmark/arc-agi-2?show=all | Unverified |

## What this means for our setup

- Our failures are selection failures, not generation failures. At least one right: 34. Picked: 33. Plain: 31.
- Our pick rule already looks like Greenblatt's. His fallback and test-input rejection are the pieces we may lack.
- Franzen's gain needs token likelihoods. With Haiku through an API we cannot do that.
- Ambiguous-example failures match Li et al.'s 9% false positives. There is no published fix beyond ensembling with a different method.
- Official scoring allows two attempts per test input. If we score one answer, we are scoring harder than the official rule.

## Ranked list for our setup (low token cost first)

1. Submit the top 2 output groups (pass@2). Zero extra tokens. Matches the official rule. It rescues "correct minority outvoted" cases. Check how our 33 is scored first.
2. Reject programs whose test output equals the test input. Add Greenblatt's fallback when fewer than 2 distinct outputs pass. Zero model tokens.
3. Execution-only tie-break: run passing programs on augmented training inputs (rotate/flip/recolour) and prefer programs that behave consistently where the task suggests it. A proxy for Franzen's stability scoring. No LLM call. Our own guess, not tested in the literature.
4. Leave-one-out check on passing programs. Re-execution costs no tokens, but programs written from all examples rarely overfit in a way LOO catches. No evidence in the literature.
5. Prompt-time augmentation (permuted example order, transposed or recoloured grids) in some of the 6 attempts. No extra cost per attempt. It may let a minority reading appear, or add more wrong ones. No published gain for API models.
6. A second revision round for near misses only. Greenblatt used one and said more might help.
7. Hypothesis-first step (Wang et al.): +13 points over direct prompting, but we already reason step by step before code, so the gain is likely small.
8. Direct-output prediction by Haiku as a tie-breaker between program groups. One extra call per puzzle. Li et al. did not use agreement, so this is our own idea with no published number.
9. Likelihood scoring and evolutionary search (Franzen, Berman, Poetiq): large gains but need a local model or 10x-100x tokens. Not low cost.

## Gaps

- No Haiku ARC-1 number from a primary source.
- Berman revision counts and the SOAR breakdown were not read.
- Official ARC-1 pass@2 wording was not retrieved from arcprize.org.
