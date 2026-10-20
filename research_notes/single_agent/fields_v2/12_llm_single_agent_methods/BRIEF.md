# Single-agent LLM reasoning methods: what it offers one thinking agent

Notes on marks. Ids like [12-a-05] point to lines in evidence_a/b/c/d.jsonl. "[ours]" means our own measurement in 00_PLAN.md. Where evidence_d CHECK lines disagree with the earlier claims file, the CHECK lines are used here. Almost all lines were checked at abstract level, not in full text, so effect sizes are each paper's headline case [critique.md].

## 1. What the field studies

This field asks how one model, with prompts and extra calls but no team, can reason better. The main families are: written step-by-step reasoning (chain of thought), sampling many answers and voting, search over partial thoughts, self-critique and repair, allocating more thinking to harder items, and prompt-level strategies such as step-back or plan-first [12-a-01, 12-a-03, 12-a-08, 12-a-09, 12-a-17, 12-a-23]. The field grew up on math and code, where there is a right answer and often a checker. Very little of it tests open-ended quality [critique.md, gap 1]. That matters for us because our schemas won on open tasks and lost on single-answer tasks [ours].

## 2. Established findings

**2.1 Chain of thought helps on math and symbolic tasks, and little elsewhere.** A meta-analysis of over 100 papers plus tests on 20 datasets and 14 models finds the gains concentrate on math and logic. On MMLU, CoT equals direct answering unless the question or answer contains an equals sign [12-a-05, 12-b-01, 12-c-09]. For planning, CoT gains appear only with problem-specific prompts and fade as problems grow [12-c-16]. About three independent sources. Effect size: not one number; "little or none" off math.

**2.2 Early gains from "think step by step" belonged to early models.** Few-shot CoT set the best GSM8K result on a 540B model [12-a-01]. Zero-shot "Let's think step by step" lifted one older model from 17.7% to 78.7% on MultiArith and from 10.4% to 40.7% on GSM8K [12-a-02]. Modern models reason by default, so these gains no longer apply (see 3b) [12-a-07].

**2.3 Intrinsic self-correction does not work on reasoning.** Without outside feedback, models struggle to fix their own reasoning and sometimes get worse [12-a-09, 12-b-04, 12-c-01, 12-d-14]. A critical survey finds no prior work showing success with feedback from prompted models, except on tasks unusually suited to it [12-a-10, 12-b-05, 12-c-03, 12-d-13]. GPT-4 self-critique caused a significant collapse on Game of 24, graph coloring and planning [12-a-12]. GPT-4 was no better at verifying than generating, and critique content barely mattered [12-c-06]. This is the strongest finding in the set (about five independent sources). It fits our ARC and word-puzzle losses, where the doubt step had no checker [ours].

**2.4 Self-correction works with reliable external feedback.** The survey says it works with reliable external feedback [12-a-10, 12-d-13]. A sound external verifier improved results and simple re-prompting with it kept most of the benefit [12-a-12]. In code, repair gains are modest and uneven once repair cost is counted, and limited by the quality of the feedback [12-c-04, 12-c-05]. Reflexion reached 91% pass@1 on HumanEval against 80% for GPT-4, but its feedback is external or simulated [12-a-13, 12-b-14, 12-c-23].

**2.5 The bottleneck of self-correction is finding the error, not fixing it.** Given the correct error location, models fix reasoning errors well across five tasks, but they are poor at locating errors [12-a-11, 12-b-06]. Feedback quality limits repair in code [12-c-05].

**2.6 Adaptive allocation of compute beats uniform spending, where a verifier exists.** Per-prompt compute allocation was over 4x more efficient than best-of-N, and a smaller model beat a 14x larger one only where it already had non-trivial success [12-a-17, 12-b-08, 12-c-24]. A 7B model with tree search beat a 34B model on MATH [12-b-09]. Both studies are math with trained verifiers, so transfer to open tasks is unknown [12-c-24].

**2.7 Debate and multi-agent systems give weak gains.** Debate protocols do not reliably beat self-consistency [12-b-12, 12-c-07]. Multi-agent systems often give minimal gains on popular benchmarks [12-c-08]. We use one agent, so this mostly confirms that a team is not the first thing to build.

**2.8 Stated reasoning is often not the real cause of the answer.** Biasing features shift answers while explanations omit them, with accuracy down as much as 36% on 13 tasks [12-a-20, 12-c-17]. Reliance on the written chain varies by task and larger models give less faithful chains on most tasks tested [12-a-21, 12-b-19]. Reasoning models reveal used hints in under 20% of cases [12-b-20, 12-c-18]. Do not use a written chain as an audit trail.

## 3. Single-source and contested findings

### 3a. Single-source (one group, not replicated in this set)

- **Self-consistency gains shrink off arithmetic.** +17.9 GSM8K, +11.0 SVAMP, +12.2 AQuA, but +6.4 StrategyQA and +3.9 ARC-challenge, on older models [12-a-03, 12-b-11, 12-c-21].
- **Adaptive stopping of sampling.** Up to 7.9x fewer samples with under 0.1 point loss, over 17 datasets and 3 LLMs [12-a-04, 12-b-10]. Open-task accuracy was not tested.
- **Repeated sampling raises coverage but selection plateaus without a verifier.** SWE-bench Lite coverage went from 15.9% to 56% at 250 samples; without an automatic verifier, majority vote and reward models plateau [12-a-16, 12-b-07, 12-c-20]. Coverage is not pick accuracy.
- **Errors are correlated across models.** When two models both err, they give the same wrong answer about 60% of the time on one leaderboard of 350+ models [12-a-22]. This matches our own concern that samples from one model agree too easily [ours].
- **CoT can lower accuracy where deliberation also hurts people.** Large drops on 3 of 6 tasks, up to 36.3 points (o1-preview vs GPT-4o) [12-a-06, 12-b-02, 12-c-10]. A related preprint finds CoT degrades instruction following [12-c-11].
- **Irrelevant clauses.** One added relevant-looking clause cut accuracy by up to 65% [12-c-15]. A strip-distractors step is suggested but untested.
- **Tree of Thoughts.** Game of 24 rose from 4% to 74%, a task with cheap partial scoring and no equal-compute control in the abstract [12-a-08, 12-b-13, 12-c-22].
- **Process supervision beats outcome supervision** for math step verification, but needs a trained model with 800,000 step labels [12-a-15, 12-b-16]. Not usable by a prompt-only agent.
- **Self-bias in judging.** LLM judges favor their own outputs (preprint, abstract only) [12-c-19].
- **Small models and long CoT.** At 3B or below, models benefit less from long chains; this is a fine-tuning study, low relevance to our model class [12-a-27, 12-b-21, 12-c-25].
- **Budget forcing.** Appending "Wait" on a fine-tuned 32B model raised AIME24 from 50% to 57%; the gain depends on fine-tuning [12-a-19, 12-b-22].
- **Verbalized Sampling.** Asking for several responses with probabilities raised creative-writing diversity 1.6 to 2.1x with no training [12-d-01]. The authors say more capable models benefit more and accuracy is not hurt, but this is a claim without figures on the abstract page [12-d-02]. No independent replication was found [12-d-03].
- **Model-based selection among samples.** Self-certainty picks the best of N without a reward model and works on open-ended tasks, but needs token probabilities [12-d-06]. Universal Self-Consistency has the model pick the most consistent free-form answer and matches standard self-consistency on math (preprint) [12-d-07].
- **Shorter parallel chains over longer ones for o1-like models.** Longer chains did not reliably help, correct answers tended to be shorter, and parallel sampling beat sequential revision (preprint) [12-d-08].
- **AdaptThink.** A trained think/no-think choice cut length 53% and raised accuracy 2.4% for a 1.5B model on math (preprint, needs RL) [12-d-09].

### 3b. Contested

- **The "Illusion of Thinking" collapse.** Reasoning models lose to standard models on easy items and collapse at high complexity under equal compute [12-b-17, 12-c-14, 12-d-10]. A rebuttal says failures can come from output token limits, that some instances are unsolvable, and that asking for a generating function restores accuracy [12-d-11]. The CHECK result: the rebuttal attacks the high-complexity collapse, not the easy-item result, so the collapse is contested and the easy-item overthinking is not rebutted in what was opened [12-d-12].
- **Overthinking of easy items.** o1-like models spend heavy compute on simple problems for little gain [12-b-18, 12-c-13]. This is a preprint, but it points the same way as the easy-item part above.
- **Inverse scaling in test-time compute.** Longer reasoning lowered accuracy on counting with distractors, spurious features and constraint tracking, and Claude models grew more distracted [12-a-18, 12-b-03, 12-c-12]. The tasks are synthetic, which limits transfer. With 12-d-08 this supports a thinking-length cap, but the evidence is not strong.
- **Self-Refine.** About 20% average absolute gain across 7 tasks with GPT-3.5, ChatGPT and GPT-4 [12-a-14, 12-b-15, 12-d-15]. A later account says earlier gains came from oracle labels or weak first prompts, but that account was read only as a search summary [12-c-02]. The CHECK result: a task-type split is plausible (preference or metric tasks versus correctness-labelled reasoning), the leakage claim is single-source, and no equal-token comparison was found [12-d-16].
- **Prompt-level strategy steps beat plain zero-shot CoT.** Step-back: MMLU Physics +7%, Chemistry +11%, TimeQA +27% [12-a-23]. Self-Discover: up to 32% over CoT, with 10 to 40x less compute than CoT-self-consistency [12-a-24]. Analogical prompting beat zero-shot CoT, with no percentages given [12-a-25]. Plan-and-Solve beat zero-shot CoT on all 10 datasets with GPT-3 [12-a-26, 12-b-23]. Baselines are plain or older CoT, compute is not matched, and the 2025 Wharton report finds CoT variants matter little on modern models [12-a-07]. Unproven for current models.
- **CoT value on reasoning models.** Marginal or no gain at much higher token cost, and it can break answers the model had right [12-a-07]. A preprint, abstract only.

## 4. Mechanisms an agent can run

**M1. Checker-gated revision.**
- Trigger: a check exists (examples, tests, a program run, a retrieved fact) and it fails.
- Action: feed the real check output back and ask for a repair; if possible give the failing location, since repair is good when the error is located [12-a-11, 12-b-06].
- Check: same token budget as plain best-of-N with the same checker.
- Evidence: 12-a-10, 12-a-12, 12-c-04, 12-c-05, 12-d-13.
- Risk: low when the checker is sound. Our ARC scaffold was fooled by a program that fit every example [ours], so the checker must include held-out cases.

**M2. No checker, no doubt step.**
- Trigger: single-answer task with no external check.
- Action: keep the first natural answer; do not run self-critique or forced doubt.
- Check: compare against a doubt arm at equal tokens; the plain arm should not lose.
- Evidence: 12-a-09, 12-b-04, 12-a-12, 12-c-06, 12-d-13.
- Risk: this rule protects us. Our BrainTeaser result (about 92% plain vs about 75% with forced doubt) and ARC (4 of 10 vs 2 of 8) match it [ours]. The cost is missing the cases where doubt would have caught a real error, which this evidence says the model cannot reliably find [12-a-11].

**M3. CoT only for multi-step math, symbolic or planning items.**
- Trigger: the item needs several computed steps.
- Action: ask for reasoning; for knowledge or commonsense items, answer directly.
- Check: CoT versus direct at equal tokens, per item class.
- Evidence: 12-a-05, 12-b-01, 12-c-09, 12-a-06, 12-a-07.
- Risk: on current reasoning models extra CoT adds cost with little gain [12-a-07], and on implicit or exception-heavy tasks it can hurt [12-a-06].

**M4. Probe, then stop early when attempts agree.**
- Trigger: any closed-answer task.
- Action: draw a few attempts, stop when they agree, spend more only when they split.
- Check: accuracy and tokens versus fixed-N voting.
- Evidence: 12-a-04, 12-b-10, 12-a-17, 12-b-08, 12-a-03.
- Risk: agreement between samples of one model is weak evidence because errors are correlated [12-a-22, 12-a-16]. Early stop on a shared wrong answer is silent. Gains were measured on math with older models [12-c-21].

**M5. Cap thinking length and prefer shorter samples.**
- Trigger: any thinking call, especially on easy items or items with distractors.
- Action: set a token cap; given several samples, prefer parallel short ones over one long chain; skip deliberation on easy items.
- Check: accuracy versus cap at equal total tokens.
- Evidence: 12-a-18, 12-b-03, 12-d-08, 12-b-18, 12-d-10, 12-d-09.
- Risk: the easy-item rule is supported, but a hard-item cutoff rule is not, since the collapse is contested [12-d-12]. A cap set too low could cut real work on hard items.

**M6. Strip distractors before solving.**
- Trigger: word problems with extra clauses.
- Action: restate only the clauses that bear on the question, keeping the original words.
- Check: with and without the strip at equal tokens.
- Evidence: 12-c-15, 12-a-18.
- Risk: untested as a fix. Rewriting names into codes made our small model worse [ours], so keep the problem's own words.

**M7. Diversity-by-set for open tasks.**
- Trigger: no single right answer (creative, design, search).
- Action: in one call ask for several distinct candidates with stated likelihoods, or show the model its earlier answers and ask for something different [12-d-05]; then an evaluator prunes.
- Check: distinct-answer count and utility at equal tokens on the NoveltyBench arm; our bar is at least 9 distinct of 10 [ours].
- Evidence: 12-d-01, 12-d-02, 12-d-04, 12-d-05.
- Risk: unreplicated [12-d-03]. This is the same kind of step that cost us accuracy on puzzles [ours], so it must be gated by the router.

**M8. Verifier-free selection among candidates.**
- Trigger: several candidates and no checker.
- Action: one selection call over N drafts (universal self-consistency), or self-certainty if the API gives token probabilities.
- Check: selector pick versus best available candidate versus random pick.
- Evidence: 12-d-06, 12-d-07, 12-a-16, 12-c-20.
- Risk: same-model judges favor their own outputs [12-c-19] and samples are correlated [12-a-22]. Selection without a verifier plateaus [12-b-07]. Treat as a tie-breaker, not as proof.

**M9. Strategy-first prompt on a stuck item.**
- Trigger: the probe splits and no attempt passes.
- Action: step back to the principle, or plan first, then solve.
- Check: strategy versus plain resample at equal tokens.
- Evidence: 12-a-23, 12-a-26, 12-b-23, 12-a-24.
- Risk: contested on modern models [12-a-07]. Use at an impasse only.

**M10. Verify by outcome, not by the written chain.**
- Trigger: always, when auditing the agent.
- Action: judge a step by running it or checking it against evidence, never by whether the explanation reads well.
- Check: on a few test cases, log whether the stated reason matches the factor that changed the answer.
- Evidence: 12-a-20, 12-a-21, 12-b-20.
- Risk: none for accuracy; it costs only logging effort.

## 5. Evidence on LLMs and AI agents

Everything above is about LLMs. Most gains come from GPT-3.5, GPT-4 and PaLM-era models [critique.md, gap 3]. Current reasoning models appear in the Wharton report [12-a-07], the inverse-scaling work [12-a-18] and the puzzle study [12-b-17].

For agents, the picture is: reflection with real task feedback helps [12-a-13]; reflection without it does not [12-a-09, 12-d-13]; multi-agent setups add little [12-c-08, 12-b-12]; and tree search pays where partial states are cheap to score [12-a-08, 12-c-22]. Open-ended tasks are covered only by the diversity work, where top models produce far less diverse output than humans and larger models in a family are less diverse than smaller ones [12-d-04]. In-context regeneration helps somewhat but is not enough [12-d-05]. That leaves room for a divergence step to win on open tasks, which matches our NoveltyBench move from 3.18 to 9.63 distinct answers [ours].

An equal-token comparison of CoT, self-consistency and Tree of Thoughts on modern models was not found, and the search budget ran out before this query [12-d-17]. Our own equal-cost runs are the only such evidence.

## 6. What does not transfer to a model

- Process reward models and any method that trains on step labels (800,000 labels) [12-a-15, 12-b-16]. A prompt-only agent has none.
- Budget forcing and AdaptThink as published: both need fine-tuning or RL [12-a-19, 12-b-22, 12-d-09]. Only the idea of a cheap difficulty check carries over.
- The small-model long-CoT finding concerns fine-tuning at 3B or below [12-a-27, 12-b-21]. It says little about prompting a larger model.
- Early CoT headline numbers from 2022 models [12-a-01, 12-a-02].
- Self-certainty needs token probabilities, which the API may not expose [12-d-06].
- "Deliberation hurts" results are tied to specific tasks; do not read them as a general rule against thinking [12-a-06].
- Debate and multi-agent results are about teams, not one agent [12-b-12, 12-c-08].

## 7. Open questions

1. Why does forced divergence win on open tasks and lose on single-answer ones? Nothing here explains it, and Verbalized Sampling does not address the second half [12-d-03].
2. Which of CoT, voting, tree search and our schema wins at equal tokens on current models [12-d-17]?
3. How should the agent decide when to switch a scaffold on? Router and difficulty work is touched only through allocation studies that need a trained verifier [12-a-17, 12-b-08].
4. How to pick among correlated samples without a verifier [12-a-22, 12-a-16, 12-d-07]?
5. Does Self-Refine help on open tasks at equal cost while failing on labelled reasoning [12-d-16]?
6. Is the easy-item overthinking result robust to the output-limit critique [12-d-12]?
7. Do prompt-level strategies (step-back, plan-first) still help on current models [12-a-07]?

## 8. References

The check level is in brackets. Preprints are marked.

1. Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. NeurIPS 2022. https://arxiv.org/abs/2201.11903 [abstract]
2. Kojima, Gu, Reid, Matsuo, Iwasawa (2022). Large Language Models are Zero-Shot Reasoners. NeurIPS 2022. https://arxiv.org/abs/2205.11916 [abstract]
3. Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou (2022). Self-Consistency Improves Chain of Thought Reasoning in Language Models. ICLR 2023. https://arxiv.org/abs/2203.11171 [fetched]
4. Aggarwal, Madaan, Yang, Mausam (2023). Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs. EMNLP 2023. https://arxiv.org/abs/2305.11860 [fetched]
5. Sprague, Yin, Rodriguez, Jiang (2024). To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. ICLR 2025. https://arxiv.org/abs/2409.12183 [fetched]
6. Liu, Geng, Wu, Sucholutsky, Lo (2024). Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. ICML 2025. https://arxiv.org/abs/2410.21333 [fetched]
7. Meincke, Mollick, Mollick, Shapiro (2025). Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting. arXiv preprint (Wharton). https://arxiv.org/abs/2506.07142 [abstract]
8. Yao, Yu, Zhao, Shafran, Griffiths, Cao, Narasimhan (2023). Tree of Thoughts: Deliberate Problem Solving with Large Language Models. NeurIPS 2023. https://arxiv.org/abs/2305.10601 [fetched]
9. Huang, Chen, Mishra, Zheng, Yu, Song, Zhou (2023). Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024. https://arxiv.org/abs/2310.01798 [fetched; the oracle-label claim is snippet only]
10. Kamoi, Zhang, Zhang, Han, Zhang (2024). When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL 2024. https://arxiv.org/abs/2406.01297 [fetched]
11. Tyen, Mansoor, Carbune, Chen, Mak (2023). LLMs cannot find reasoning errors, but can correct them given the error location. ACL 2024 Findings. https://arxiv.org/abs/2311.08516 [fetched]
12. Stechly, Valmeekam, Kambhampati (2024). On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks. arXiv preprint. https://arxiv.org/abs/2402.08115 [abstract]
13. Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao (2023). Reflexion: Language Agents with Verbal Reinforcement Learning. NeurIPS 2023. https://arxiv.org/abs/2303.11366 [fetched]
14. Madaan, Tandon, Gupta, Hallinan, et al. (2023). Self-Refine: Iterative Refinement with Self-Feedback. NeurIPS 2023. https://arxiv.org/abs/2303.17651 [fetched]
15. Lightman, Kosaraju, Burda, Edwards, et al. (2023). Let's Verify Step by Step. ICLR 2024. https://arxiv.org/abs/2305.20050 [fetched]
16. Brown, Juravsky, Ehrlich, Clark, et al. (2024). Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. arXiv preprint. https://arxiv.org/abs/2407.21787 [fetched]
17. Snell, Lee, Xu, Kumar (2024). Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. ICLR 2025. https://arxiv.org/abs/2408.03314 [fetched]
18. Gema, Hagele, Chen, Arditi, et al. (2025). Inverse Scaling in Test-Time Compute. TMLR. https://arxiv.org/abs/2507.14417 [fetched]
19. Muennighoff, Yang, Shi, Li, et al. (2025). s1: Simple test-time scaling. arXiv preprint. https://arxiv.org/abs/2501.19393 [fetched]
20. Turpin, Michael, Perez, Bowman (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023. https://arxiv.org/abs/2305.04388 [abstract]
21. Lanham, Chen, Radhakrishnan, et al. (2023). Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv preprint (Anthropic). https://arxiv.org/abs/2307.13702 [fetched]
22. Kim, Garg, Peng, Garg (2025). Correlated Errors in Large Language Models. ICML 2025. https://arxiv.org/abs/2506.07962 [abstract]
23. Zheng, Mishra, Chen, Cheng, et al. (2023). Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models. ICLR 2024. https://arxiv.org/abs/2310.06117 [abstract]
24. Zhou, Pujara, Ren, Chen, Cheng, et al. (2024). Self-Discover: Large Language Models Self-Compose Reasoning Structures. arXiv preprint. https://arxiv.org/abs/2402.03620 [abstract]
25. Yasunaga, Chen, Li, Pasupat, Leskovec, Liang, Chi, Zhou (2023). Large Language Models as Analogical Reasoners. ICLR 2024. https://arxiv.org/abs/2310.01714 [abstract]
26. Wang, Xu, Lan, Hu, Lan, Lee, Lim (2023). Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models. ACL 2023. https://arxiv.org/abs/2305.04091 [fetched]
27. Li, Yue, Xu, Jiang, Niu, Lin, et al. (2025). Small Models Struggle to Learn from Strong Reasoners. Findings of ACL 2025. https://arxiv.org/abs/2502.12143 [fetched]
28. Wu, Sun, Li, Welleck, Yang (2024). Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models. arXiv preprint. https://arxiv.org/abs/2408.00724 [fetched]
29. Smit, Duckworth, Grinsztajn, et al. (2023). Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs. ICML 2024. https://arxiv.org/abs/2311.17371 [fetched]
30. Chen, Xu, Liang, He, Pang, Yu, et al. (2024). Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. arXiv preprint. https://arxiv.org/abs/2412.21187 [fetched]
31. Chen, Benton, Radhakrishnan, et al. (2025). Reasoning Models Don't Always Say What They Think. arXiv preprint. https://arxiv.org/abs/2505.05410 [fetched]
32. Shojaee, Mirzadeh, Alizadeh, Horton, Bengio, Farajtabar (2025). The Illusion of Thinking. NeurIPS 2025 per page (arXiv preprint). https://arxiv.org/abs/2506.06941 [fetched]
33. Olausson, Inala, Wang, Gao, Solar-Lezama (2023). Is Self-Repair a Silver Bullet for Code Generation? ICLR 2024. https://arxiv.org/abs/2306.09896 [abstract]
34. Stechly, Marquez, Kambhampati (2023). GPT-4 Doesn't Know It's Wrong: An Analysis of Iterative Prompting for Reasoning Problems. arXiv preprint. https://arxiv.org/abs/2310.12397 [abstract]
35. Cemri et al. (2025). Why Do Multi-Agent LLM Systems Fail? arXiv preprint. https://arxiv.org/abs/2503.13657 [abstract]
36. Li, Yu, Zhang, et al. (2025). When Thinking Fails: The Pitfalls of Reasoning for Instruction-Following in LLMs. arXiv preprint. https://arxiv.org/abs/2505.11423 [abstract]
37. Mirzadeh, Alizadeh, Shahrokhi, et al. (2024). GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models. arXiv preprint. https://arxiv.org/abs/2410.05229 [abstract]
38. Stechly, Valmeekam, Kambhampati (2024). Chain of Thoughtlessness? An Analysis of CoT in Planning. NeurIPS 2024. https://arxiv.org/abs/2405.04776 [abstract]
39. Panickssery, Bowman, Feng (2024). LLM Evaluators Recognize and Favor Their Own Generations. arXiv preprint. https://arxiv.org/abs/2404.13076 [abstract]
40. Zhang, Yu, Chong, Sicilia, Tomz, Manning, Shi (2025). Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity. arXiv 2510.01171 (ICML 2026 per search result). https://arxiv.org/abs/2510.01171 [fetched; replication check by snippet]
41. Zhang, Diddee, Holm, Liu, Liu, Samuel, Wang, Ippolito (2025). NoveltyBench: Evaluating Language Models for Humanlike Diversity. arXiv 2504.05228. https://arxiv.org/abs/2504.05228 [abstract]
42. Kang, Zhao, Song (2025). Scalable Best-of-N Selection for Large Language Models via Self-Certainty. arXiv 2502.18581 (NeurIPS 2025 per page). https://arxiv.org/abs/2502.18581 [abstract]
43. Chen, Aksitov, Alon, Ren, Xiao, Yin, Prakash, Sutton, Wang, Zhou (2023). Universal Self-Consistency for Large Language Model Generation. arXiv preprint. https://arxiv.org/abs/2311.17311 [abstract]
44. Zeng, Cheng, Yin, Zhou, Qiu (2025). Revisiting the Test-Time Scaling of o1-like Models. arXiv preprint. https://arxiv.org/abs/2502.12215 [abstract]
45. Zhang, Lin, Hou, Feng, Li (2025). AdaptThink: Reasoning Models Can Learn When to Think. arXiv preprint. https://arxiv.org/abs/2505.13417 [abstract]
46. Lawsen (2025). Comment on The Illusion of Thinking. arXiv preprint. https://arxiv.org/abs/2506.09250 [abstract; full text not read]
