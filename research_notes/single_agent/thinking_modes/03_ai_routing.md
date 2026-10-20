# 03 - AI routing between convergent and divergent reasoning modes

Tags: [V] = checked on the web this session (search results; abstract-level only, I did not read full papers). [M] = from memory, not checked. Numbers are quoted only where a search result showed them.

## 1. Adaptive test-time compute and strategy routing

- Snell, Lee, Xu, Kumar, 2024, "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters", arXiv 2408.03314 [V]. Per-prompt "compute-optimal" allocation beats uniform best-of-N by more than 4x in efficiency. The best method (verifier search vs. sequential revision) depends on prompt difficulty. A smaller model plus test-time compute beat a 14x larger one, but only on problems where the small model already had a non-trivial success rate. Difficulty is estimated from the base model's pass rate ([M] for the binning detail).
- Zhou et al., 2024, "Self-Discover: Large Language Models Self-Compose Reasoning Structures", arXiv 2402.03620 (NeurIPS 2024) [V]. The model picks and composes reasoning modules per task, then follows the structure. Reported to beat CoT with self-consistency by over 20% on some tasks with 10-40x less inference compute. Evidence that a one-time, per-task strategy choice is cheap. It routes by task, not by sample.
- Pan et al., 2025, "Route to Reason: Adaptive Routing for LLM and Reasoning Strategy Selection", arXiv 2505.19435 [V]. Jointly routes model and reasoning strategy by difficulty under a budget; reports higher accuracy than the best single model with over 60% fewer tokens (authors' claim). Related: DOTS, arXiv 2410.03864 [V, snippet: LLM chooses reasoning actions per question]; arXiv 2510.08731 [V, one-line summary: semantic router applying reasoning only when beneficial].
- Brown et al., 2024, "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling", arXiv 2407.21787 [V]. Coverage (solved by any sample) rises log-linearly over four orders of magnitude of samples. With automatic verifiers (code, proofs) coverage becomes accuracy (SWE-bench Lite 15.9% to 56% at 250 samples). Without verifiers, majority vote and reward models plateau after a few hundred samples. This is the key "verifier availability" fact.
- Wang et al., 2022, "Self-Consistency Improves Chain of Thought Reasoning", arXiv 2203.11171 [M]. Majority-voting baseline.
- Evidence on routing specifically by problem type (convergent vs. open-ended design): none found. The routing literature is almost all difficulty-based on single-answer tasks. The type-routing rule below is therefore an inference, not a replicated result.

## 2. Combining convergent and divergent generation

- Wang et al., 2024, "Planning In Natural Language Improves LLM Search For Code Generation" (PlanSearch), arXiv 2409.03733 [V]. Argues inference scaling stalls from low output diversity; searches over natural-language observations and plans before code. Claude 3.5 Sonnet on LiveCodeBench: pass@200 77.0% vs 60.6% for repeated sampling and 41.4% best no-search pass@1. Gains are reported to be predictable from measured idea diversity. It is a coverage (pass@k) result with test-based selection; it does not show per-sample accuracy rising.
- Diversity vs. temperature: Zhang et al., 2020, "Trading Off Diversity and Quality in Natural Language Generation", arXiv 2004.10450 [V, title seen]. Temperature trades quality for diversity. SimpleStrat, arXiv 2410.09038 [V, snippet only]: temperature does not fix answer-space diversity (example: a model putting 87% of mass on "California"); proposes stratification, i.e. structure rather than a sampling knob. A selective-sampling paper reported that high-temperature sampling hurts precise reasoning such as math [V snippet, paper not identified]. No direct prompt-diversity vs. temperature head-to-head found; treat as open.
- Mouret and Clune, 2015, "Illuminating search spaces by mapping elites" (MAP-Elites), arXiv 1504.04909 [V]. Keep the best solution per cell of a user-chosen behavior grid; yields many high-performing, qualitatively different solutions. Authors call their empirical evidence preliminary.
- Bradley et al., 2023, "Quality-Diversity through AI Feedback" (QDAIF), ICLR 2024 [V, poster page]. LM generates variations and judges quality and diversity; covers more of the search space with high-quality samples than non-QD controls in all but one creative-writing domain.
- Romera-Paredes et al., 2023, "Mathematical discoveries from program search with large language models" (FunSearch), Nature 625:468-475 [V]. LLM proposes programs, automated evaluator filters; evolutionary loop; new cap-set constructions and bin-packing heuristics. (Island model details [M].)
- Novikov et al., 2025, "AlphaEvolve: A coding agent for scientific and algorithmic discovery", arXiv 2506.13131 [V]. Extends FunSearch to whole codebases, many languages, multi-objective, automated evaluators.
- Lu et al., 2024, "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery", arXiv 2408.06292 [V]. Ideation, experiments, writing, automated review; under $15 per paper (authors' claim, judged by their own automated reviewer).

Pattern: divergence is rewarded where an automatic evaluator exists to filter wrong ideas (cap sets, bin packing, code tests). It is generation breadth plus a hard filter, not diverse voting.

## 3. Cheap signals for problem type and difficulty

- Agreement among a few samples: Aggarwal et al., 2023, "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs", arXiv 2305.11860 (EMNLP 2023) [V]. Stops sampling when the running majority is stable; up to 7.9x fewer samples, under 0.1% average accuracy drop (17 datasets, 3 LLMs). Critique in arXiv 2401.10480 (early-stopping self-consistency) [V]: needs threshold tuning and is threshold-sensitive.
- Semantic agreement as uncertainty: Farquhar et al., 2024, "Detecting hallucinations in large language models using semantic entropy", Nature 630:625-630 [V]. Entropy over clusters of meaning, not wording; needs no task-specific data.
- Self-assessed confidence: Kadavath et al., 2022, "Language Models (Mostly) Know What They Know", arXiv 2207.05221 [M]. P(True)/P(IK) reasonably calibrated in-distribution; weaker off-distribution.
- Verifier availability and answer-space size: Large Language Monkeys [V] shows verifier presence decides whether sampling breadth converts to accuracy. Answer-space size has no dedicated routing paper found; it is an inference (a small answer space makes exact-match voting meaningful; free-form outputs never collide).

## 4. Simplicity and selection in program search

- AlphaCode: Li et al., 2022, "Competition-Level Code Generation with AlphaCode", arXiv 2203.07814 (Science) [V]. Massive sampling, filter by tests on given examples, cluster by behavior, submit a small set; authors name sampling plus filtering and clustering as essential. Top 54.3% on Codeforces (>5,000 participants). Clustering is behavior-based voting robust to varied surface code.
- Shortest-program prior: Solomonoff/Levin/Kolmogorov; Chollet 2019, "On the Measure of Intelligence", arXiv 1911.01547 [M]. The claim that simpler ARC programs generalize better to held-out grids is common ARC practice [M], not checked.
- FunSearch/AlphaEvolve balance novelty and correctness: correctness enforced by the evaluator, novelty by population structure (islands, archive-like databases) [M for those details]. AI Scientist uses an LLM reviewer and literature novelty check [M for the novelty-check detail].

## 5. Proposed routing design

Principle: the modes need different things. Convergent needs per-sample accuracy plus a selector. Divergent needs coverage plus an evaluator. So route on "is there a hard cheap verifier, and do cheap samples converge", not on topic labels.

Step 0, free signals (no LLM calls):
1. Verifier available? Examples with ground-truth outputs (ARC train pairs), test suite, executable scorer. Evidence: Large Language Monkeys [V]. Output V in {exact, scored, none}.
2. Output format: fixed grid/number/choice (small checkable answer space) vs. free-form design text.

Step 1, probe (about 4-5 cheap, natural, direct samples at modest temperature; no divergent framings):
3. Agreement: fraction in the largest semantic/behavioral cluster (execution-output clusters for code, exact grid match for ARC, meaning-clusters for text). Evidence: Adaptive-Consistency, semantic entropy [V]. Optionally one P(True) read [M].
4. If V=exact, the fraction of probe samples that pass the verifier.

Step 2, rule:
- V=exact and a probe sample passes: convergent, finish early (Adaptive-Consistency logic [V]). No divergent mode.
- V=exact, none pass, agreement high (confidently wrong, default framing stuck): convergent revision/sampling first (Snell: method depends on difficulty [V]), plus a divergent slice of roughly 20-30% (tunable guess) using plan-level diversity, which is the PlanSearch setting and showed coverage gains with test selection [V].
- V=exact, none pass, agreement low: very hard or underspecified; shift toward divergent plan-level diversity with the verifier as filter.
- V=none or scored only, free-form output, agreement low or undefined: divergent mode, but only if a scorer or judge exists to prune (QDAIF, FunSearch pattern [V]). With no evaluator at all, fall back to a few ideas plus self-consistency-style selection and flag low confidence; selection is the bottleneck without verifiers [V].
- Keep a convergent baseline as a floor on divergent tasks, since divergent winners are rare.

Why not blend by default: our measurement (divergent framings 2-4x less accurate per attempt on single-answer puzzles) is consistent with the quality-diversity trade-off in sampling literature [V, weak evidence]. With a hard verifier, diversity pays only through coverage, so it must be bought with enough samples to overcome the per-sample loss. Break-even check: divergent is worth it on a verifiable task only if its extra distinct-solution coverage outweighs the per-sample accuracy ratio at equal budget. Estimate this from our own logs, not from assumption.

Step 3, shifting budget during the run (Snell's compute-optimal allocation [V]; bandit-style reallocation [M]):
- Initial split about 70/30 convergent/divergent on verifiable tasks and 30/70 on open-ended ones (guess; tune on logs).
- After each round track marginal yield per token per mode: new verifier passes (verifiable) or new top-k scorer entries (open-ended). Move budget toward the higher recent yield; floor each mode near 10% so the estimate stays live.
- Convergent saturation: majority cluster stable across rounds, stop (Adaptive-Consistency [V]). If stable but verifier-failing, release budget to divergent.
- Divergent saturation: new ideas land in occupied cells of a small MAP-Elites-style archive (descriptors such as architecture family or change type [V]); stop sampling new framings and refine the top elites.
- Selecting divergent output: pass every candidate through the same verifier or evaluator, cluster by behavior (AlphaCode [V]), prefer the simpler candidate on ties (shortest-program prior [M]).

Validation plan: log per problem the probe agreement, verifier status, and which mode ultimately won. Check that probe agreement predicts convergent success (expected from the self-consistency literature) and that ARC items with failed high-agreement probes are rescued by divergent slices at a rate that beats the 2-4x per-attempt penalty. Since no type-routing paper exists, this validation is the real evidence.

## Gaps and caveats
- No paper found that routes between convergent and divergent prompting modes by problem type.
- No verified direct prompt-diversity vs. temperature comparison.
- Searches returned abstracts and summaries; figures are as reported by authors or search summaries, not re-derived.
