# Metacognition and learning science: what it offers one thinking agent

Evidence ids are in brackets. "a-", "b-", "c-" ids are written metacog-a-04 and so on; "d" ids are 11-d-NN. Where evidence_d CHECK lines disagree with the earlier claims file, the CHECK lines are used. Most LLM sources are preprints. All learning-science effect sizes except one are unverified.

## 1. What the field studies

Metacognition is thinking about one's own thinking. Nelson and Narens framed it as an object level (doing the task) and a meta level (watching and steering), linked by monitoring going up and control going down [metacog-a-12, memory only]. Learning science asks which study habits work: testing yourself, explaining to yourself, struggling before being taught, worked examples [metacog-a-18, memory only]. For an agent the question is narrower. When should it monitor itself, what signal can it trust, and what should it do when the signal says "doubt"?

Our own data set the frame. Forced doubt helped on open tasks and hurt on single-answer tasks (see 00_PLAN.md). So the useful output of this field is a rule for when not to doubt.

## 2. Established findings

Status "established" means several independent sources agree. Three findings qualify.

**E1. Prompted self-correction without outside feedback does not help reasoning and often hurts.**
- Huang et al. 2024 found that intrinsic self-correction struggles on reasoning and can lower performance [metacog-a-04, metacog-b-04, metacog-c-01].
- Kamoi et al. 2024 surveyed the literature. They found no prior work showing success from prompted-LLM feedback alone, except on unusually suitable tasks. It works with reliable external feedback or after large-scale fine-tuning. Many positive studies had unfair setups [metacog-b-05, metacog-c-02].
- Kumar et al. 2024 trained self-correction with multi-turn reinforcement learning, which offline supervised traces could not do. Gains were 15.6% on MATH (Gemini 1.0 Pro) and 9.1% on HumanEval (Gemini 1.5 Flash). They describe prompted self-correction as largely ineffective [metacog-b-07].
- Caveat: Kamoi partly reviews Huang's body of work, so independence is partial (claims.jsonl note). One low-credibility preprint argues self-correction works at temperature zero with unbiased prompts. Treat that as contested [metacog-b-06].

**E2. Models overthink easy problems; more thinking is not monotonically better.** Eight groups report this.
- Reasoning models spend large compute on simple problems for little gain [metacog-b-13, metacog-c-09].
- They are poorly calibrated in token use on very easy items [metacog-b-11, metacog-c-10].
- They write long on easy problems and do not extend enough on hard ones, which suggests they misjudge difficulty [metacog-b-12].
- Chain-of-thought lowered accuracy on three of six tasks chosen because deliberation hurts people. The largest drop was 36.3 points for o1-preview against GPT-4o [metacog-c-05].
- Longer reasoning lowered accuracy on built tasks. Claude models were distracted by irrelevant information [metacog-c-07].
- At equal compute, plain models beat reasoning models on simple puzzles, reasoning models won on medium ones, and both collapsed on hard ones [metacog-c-08].
- Parallel independent paths with a majority vote gave up to 20% higher accuracy than extended thinking at the same budget [metacog-c-06].
- In 4,018 software-agent trajectories, more overthinking went with lower success. Choosing the candidate with the lower overthinking score raised performance [metacog-c-11].
- Caveat: nearly all are preprints, on reasoning-model families. This matches our result that scaffolds hurt on ARC and word puzzles (00_PLAN.md).

**E3. Written reasoning is an unreliable witness of why a model answered.**
- Biasing features changed answers, and accuracy fell by up to 36% on 13 BIG-Bench Hard tasks, while the explanation did not mention the bias [metacog-c-12].
- Reasoning-model chains of thought revealed a used hint often below 20% of the time. Outcome reinforcement learning raised faithfulness only partway [metacog-c-13].
- Consequence: a model's own account of its confidence is weak monitoring evidence.

## 3. Single-source and contested findings

### 3a. Single-source (one study carries it)

**LLM self-assessment**
- Larger models are well calibrated on multiple-choice and true/false items. P(True) improves when the model sees many of its own samples. A trained P(IK) generalises only partly to new tasks. Models were up to 52B, so these are old models [metacog-a-01, metacog-a-02, metacog-b-09].
- Verbalized confidence from black-box models is overconfident. Sample consistency helps. White-box methods beat black-box ones only slightly. All struggle on professional-knowledge tasks [metacog-a-03, metacog-b-10, metacog-c-14]. This looks opposed to Kadavath, but the two measure different signals (token probability against stated confidence) on different generations. No source settles which to use for current Claude models (critique.md).
- Semantic entropy predicts errors better than P(True) or naive entropy: mean AUROC 0.790 against 0.698 and 0.691 over 30 task-model combinations. It detects confabulation, not consistent errors [metacog-a-06]. Peer reviewed and strong, but our samples are correlated, so consistent errors would slip past it.
- Models are not reliably better at discriminating among their own answers than at generating them [metacog-c-03].
- Judges recognise their own text and prefer it. Self-recognition tracks self-preference, linearly after fine-tuning. GPT-4 and Llama 2 only [metacog-a-05, metacog-b-08, metacog-c-15]. These are three lines for one study.
- Fixing works once the error is located. Failed self-correction is mainly a failure to find the mistake. Given the error location, correction improved results on five reasoning tasks [metacog-c-04].

**Harness and agent results**
- A Nelson-Narens harness (feeling of knowing before, judgment after, a control policy to trust, retry or aggregate) raised Sonnet-4.6 pooled accuracy from 48.3 to 56.9 across HLE-Verified, LiveCodeBench v6 and R-Bench-V, 1859 questions [metacog-a-07, metacog-b-01, 11-d-01]. Updated by the CHECK lines (the earlier critique said no cost data):
  - Cost per question was $0.78 for the harness against $0.29 for pass@1 and $1.42 for a 4-attempt aggregator. The harness scored 56.9 against 53.7 for the aggregator, at about half its cost [11-d-02, 11-d-06].
  - The matched-attempts ablation is weak. Full harness 47.0 [37,57] at average K 2.58, random retry at the same K 45.7 [43,48], pass@1 44.0, on n=100. Intervals overlap, so "directed beats undirected retry" is unproven [11-d-03, 11-d-06].
  - Gains concentrate on hard items. LiveCodeBench Easy moved from 95.4 to 94.7, Medium +1.1, Hard +19.6, HLE +12.0 [11-d-04].
  - Limits stated by the authors: only Sonnet-4.6 passed all diagnosis checks among nine models, the controller is an SVM fitted on a 100-example anchor set, and the tasks are benchmark reasoning, not long-horizon agents [11-d-05]. No independent replication was found [11-d-06].
  - Net: a hypothesis, not a design input.
- Reflexion (verbal lessons stored after environment feedback) reached 91% pass@1 on HumanEval against 80% reported for GPT-4 [metacog-a-09]. It relies on external feedback such as tests. Self-generated feedback quality is reported as the bottleneck of reflection [11-d-11, abstract only].
- Monitoring and regulation dissociate across 20 models (r = .17, wide interval). Accuracy rank and metacognitive sensitivity rank are largely inverted. Models fall into blanket-confidence, blanket-withdrawal and selective profiles [metacog-a-08, metacog-b-02, metacog-b-03, metacog-c-16]. One author, small n, preprint.
- MetaCrit reports that indiscriminate critique degrades performance, so critique strength should vary by input. Abstract only [metacog-b-14].
- Models fine-tuned to predict their own behaviour beat a second model trained on them, but failed on complex and out-of-distribution tasks [metacog-b-15]. A review notes human and LLM metacognition differ in many ways [metacog-b-16].

**Human learning science (all numbers below rest on memory, none opened)**
- Retrieval practice beats restudy, average g about 0.50, larger with feedback [metacog-a-13, metacog-b-18]. The record is confirmed (Psychological Bulletin 140(6)) but the effect size could not be verified [11-d-09, 11-d-10]. Keep as memory.
- Self-explanation prompts, g about 0.55 [metacog-a-14, metacog-b-19].
- Worked examples in maths, g about 0.48 over 181 effects [metacog-a-17]. The benefit shrinks or reverses for experienced learners (expertise reversal) [metacog-a-16].
- Practice testing and distributed practice rated high utility, highlighting and rereading low [metacog-a-18].
- Experts sort problems by deep structure, novices by surface [metacog-a-20].
- A low feeling of rightness on a fluent first answer predicts more rethinking in people [metacog-a-19].
- Hedne et al. found warmth ratings did not separate insight from non-insight solutions (n=51, 971 trials, p=.429), against Metcalfe and Wiebe 1987. Insight solutions were more often correct (about 57% against 37%), yet confidence did not discriminate correct from incorrect, and wrong insight answers were stickier [metacog-a-10, metacog-a-11, metacog-c-18].

### 3b. Contested

- **Productive failure** (try the problem before being taught). A meta-analysis of 53 studies and 166 comparisons found problem-first beat instruction-first for conceptual knowledge and transfer, g = 0.36, larger when the design followed productive-failure principles [11-d-07, metacog-b-17]. The headline is confirmed from the Crossref record. Moderators and the 0.87 bias-corrected figure are not verified [11-d-08]. Grades 2 to 5 and domain-general skills favoured instruction first [11-d-07]. The effect is examined mostly in mathematics [metacog-c-19]. One critic says the control design lacks ecological validity, but that is an opinion post without reanalysis, credibility 35 [metacog-c-20].
- **Intrinsic self-correction at temperature zero** [metacog-b-06]. See E1.

## 4. Mechanisms an agent can run

Each mechanism is tested at equal tokens against the plain model. "Plain" means the same model, same total token budget, spent on one natural answer or on best-of-N with a vote, whichever is stronger.

**M1. Trust the first answer; doubt only on an external signal.**
- Trigger: single-answer task, and no test, tool output or example check has failed.
- Action: return the first natural answer. Do not run a critique round. If a check exists, run it; revise only from the check's output, and say where it failed.
- Check: plain first answer against first answer plus an unconditional self-critique round, at equal tokens, on ARC-style and word-puzzle items.
- Evidence: E1 [metacog-a-04, metacog-b-05, metacog-c-02]; E2 [metacog-c-08, metacog-b-13]; error location is the missing piece [metacog-c-04].
- Risk: low on single-answer tasks, where our own data say doubt hurts. On open-ended tasks it would remove the divergence that made NoveltyBench go from 3.18 to 9.63 distinct answers, so M1 must be gated by task type (see M6).

**M2. Locate the error before fixing it.**
- Trigger: an external check failed and a revision is allowed.
- Action: make the revision step name the failing step or example, using the real check output, then fix only that part.
- Check: revise-with-localised-error against revise-blind, equal tokens.
- Evidence: [metacog-c-04], supported by Kamoi's finding that reliable external feedback is what works [metacog-b-05].
- Risk: the localisation study is single-source and used given error locations, not self-found ones. If the agent self-locates, it falls back into E1.

**M3. Scale effort to difficulty; stop early on easy items.**
- Trigger: after the first answer, the agent estimates difficulty from agreement among a few cheap attempts or from a failing check.
- Action: easy and agreeing, stop. Disagreeing or failing, spend more, and prefer parallel independent attempts with a vote over a longer single chain.
- Check: adaptive allocation against fixed K and against one long chain, at equal mean tokens.
- Evidence: [metacog-c-06, metacog-c-08, metacog-c-11, metacog-b-12]; gains concentrate on hard items [11-d-04].
- Risk: our samples are correlated, so agreement can be agreement on a wrong answer. Vote gains from the literature may be smaller for one model. Ghosal's gain may also be partly an output-variance artifact [metacog-c-06].

**M4. Pre-solve feeling-of-knowing gate (hypothesis).**
- Trigger: any task, before solving.
- Action: ask for a rating of how likely the model is to solve it, then use it to choose between trust, retry and aggregate.
- Check: gate against random retry at matched attempts, with n well above 100 and the cost counted.
- Evidence: [11-d-01, 11-d-02]. The directed-versus-random advantage is unproven [11-d-03, 11-d-06]. Humans show feeling of rightness predicts rethinking [metacog-a-19, memory].
- Risk: high. Verbalized confidence is overconfident [metacog-a-03]. The accuracy and sensitivity ranks across models are largely inverted [metacog-b-02]. The gate adds calls and gave no gain on easy items [11-d-04]. Do not make it load-bearing before our own test.

**M5. Sample-based uncertainty instead of stated confidence.**
- Trigger: a factual or short-answer item where the agent must decide whether to answer or abstain.
- Action: draw several samples, cluster them by meaning, treat a spread as a warning.
- Check: semantic-entropy abstention against stated-confidence abstention, at equal tokens, scored by accuracy on answered items.
- Evidence: [metacog-a-06, metacog-a-03].
- Risk: correlated samples hide consistent errors, which the paper itself says it cannot detect [metacog-a-06]. Our ARC runs, where a wrong program fit every example, are the same failure.

**M6. Route by task type before choosing how much doubt to apply.**
- Trigger: start of every task.
- Action: classify as open-ended (diverge, then prune with an objective check) or single-answer (trust, verify, stop).
- Check: router plus per-type policy against each fixed policy, at equal tokens, over a mixed set.
- Evidence: no direct study of pre-solve open-versus-single prediction was found [11-d-13]. Nearest items are the P(IK) predictor, which generalises only partly [metacog-a-02], critique strength varying by input [metacog-b-14], and experts sorting by deep structure [metacog-a-20, memory].
- Risk: a wrong route is costly in both directions. Our measurements say the split decides everything, and this is the one design step with almost no outside support. It must be validated in our harness.

**M7. Store lessons only when an outside signal confirms them.**
- Trigger: a check passed or failed with a clear cause.
- Action: write a short lesson to memory, tagged with the check that supports it. Do not store lessons from self-judgment alone.
- Check: lesson memory against none, on repeated similar tasks, including a stale-lesson probe.
- Evidence: [metacog-a-09] for gains with test feedback; self-feedback quality is the bottleneck [11-d-11, abstract only].
- Risk: staleness and misleading lessons are unsettled [11-d-14]. An unconfirmed lesson may poison later tasks.

**M8. Do not use the model's written reasons as evidence of its confidence.**
- Trigger: whenever a design step would read the chain of thought to judge correctness.
- Action: judge by outputs and checks, not by the model's explanation of itself.
- Check: judge-by-explanation against judge-by-check on a labelled set.
- Evidence: E3 [metacog-c-12, metacog-c-13].
- Risk: very low. It removes steps rather than adding them.

## 5. Evidence on LLMs and AI agents

- Self-correction fails without outside signal [metacog-a-04, metacog-b-05], and works with tests or tools [metacog-a-09, metacog-b-05].
- Overthinking is common, and Claude models showed distraction by irrelevant information under longer reasoning [metacog-c-07].
- Agentic software tasks show the same pattern: more overthinking, lower success [metacog-c-11].
- Self-evaluation is biased toward the model's own text [metacog-a-05, metacog-c-15], and discriminating among own answers is not reliably easier than generating [metacog-c-03].
- The only Claude-based metacognitive harness result is Cao's. It is a preprint, one model version, no replication [11-d-01, 11-d-05, 11-d-06].
- The newest Claude models have no calibration study in this set. The calibration sources are from 2022 and 2023-24 [metacog-a-01, metacog-a-03].

## 6. What does not transfer to a model

These are judgments. They rest on the cited human findings plus the way an LLM call works.

- Retrieval practice and spacing exist because people forget. An LLM does not forget between calls within a run, and the human effect sizes [metacog-a-13, metacog-a-18, memory] say nothing about it.
- Self-explanation [metacog-a-14, memory] looks like chain of thought already, so the effect may already be spent. Chain of thought itself can hurt [metacog-c-05].
- Feeling of rightness and warmth are felt signals. The warmth signal did not even separate insight from non-insight in people [metacog-a-10, metacog-c-18]. Do not build a gate on a self-rated closeness.
- Worked examples and expertise reversal [metacog-a-16, metacog-a-17] describe learners with limited working memory. Only indirect LLM evidence exists, and it shows models simulating learners, not examples hurting a strong model [11-d-12, abstract only].
- Productive failure is about what a learner retains after instruction [11-d-07]. A model has no retention step in one run.
- Introspection beyond the model's own training distribution failed [metacog-b-15], and human and LLM metacognition differ in many ways [metacog-b-16].

## 7. Open questions

1. Can anything predict before solving whether a task is open-ended or single-answer? None found [11-d-13].
2. Does a directed metacognitive gate beat random retry at matched attempts with adequate n? The only test is n=100 with overlapping intervals [11-d-03].
3. Do stored lessons help without outside feedback, and do they go stale? Not settled [11-d-14, 11-d-11].
4. Does expertise reversal show up when a strong model gets a worked example for a task it already solves? Only indirect evidence [11-d-12]. A gap in two searches, not proof of absence [metacog-a-21, metacog-b-20].
5. How calibrated are current Claude models, by token probability and by stated confidence? Old evidence disagrees [metacog-a-01, metacog-a-03].
6. When should sampling stop? No adaptive stopping rule was found in this field's set.
7. Can locating the error be done reliably by the model itself, or only with an external signal? [metacog-c-04, metacog-b-05]
8. Does the Cao result hold on other models, given only Sonnet-4.6 passed all diagnosis checks? [11-d-05]

## 8. References

How checked: fetched = page opened, abstract = abstract or metadata only, snippet = search snippet, memory = recalled, not opened.

1. Kadavath et al. 2022. Language Models (Mostly) Know What They Know. arXiv 2207.05221. https://arxiv.org/abs/2207.05221. fetched.
2. Xiong, Hu, Lu, Li, Fu, He 2024. Can LLMs Express Their Uncertainty? ICLR 2024 (arXiv 2306.13063). https://arxiv.org/abs/2306.13063. fetched.
3. Huang, Chen, Mishra, Zheng et al. 2024. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024 (arXiv 2310.01798). https://arxiv.org/abs/2310.01798. fetched.
4. Panickssery, Bowman, Feng 2024. LLM Evaluators Recognize and Favor Their Own Generations. NeurIPS 2024 (arXiv 2404.13076). https://arxiv.org/abs/2404.13076. fetched.
5. Farquhar, Kossen, Kuhn, Gal 2024. Detecting hallucinations in large language models using semantic entropy. Nature (PMC11186750). https://pmc.ncbi.nlm.nih.gov/articles/PMC11186750. fetched.
6. Cao, Wang, Qin, Zhang, Xie 2026. LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling. arXiv preprint 2605.14186. https://arxiv.org/abs/2605.14186. fetched.
7. Cacioli 2026. The Metacognitive Monitoring Battery: A Cross-Domain Benchmark. arXiv preprint 2604.15702. https://arxiv.org/abs/2604.15702. fetched.
8. Shinn et al. 2023. Reflexion: Language Agents with Verbal Reinforcement Learning. arXiv 2303.11366. https://arxiv.org/abs/2303.11366. fetched.
9. Hedne, Norman, Metcalfe 2016. Intuitive feelings of warmth and confidence in insight and noninsight problem solving of magic tricks. Frontiers in Psychology (PMC5005374). https://pmc.ncbi.nlm.nih.gov/articles/PMC5005374/. fetched.
10. Kamoi, Zhang, Zhang, Han, Zhang 2024. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey. arXiv 2406.01297. https://arxiv.org/abs/2406.01297. fetched.
11. Liu, Nassereldine, Yang et al. 2024. Large Language Models have Intrinsic Self-Correction Ability. arXiv preprint 2406.15673. https://arxiv.org/abs/2406.15673. fetched.
12. Kumar, Zhuang, Agarwal et al. 2024. Training Language Models to Self-Correct via Reinforcement Learning. arXiv 2409.12917. https://arxiv.org/abs/2409.12917. fetched.
13. Pu, Saxon, Hua, Wang 2025. ThoughtTerminator: Benchmarking, Calibrating, and Mitigating Overthinking in Reasoning Models. arXiv preprint 2504.13367. https://arxiv.org/abs/2504.13367. fetched.
14. Su, Healey, Nakov, Cardie 2025. Between Underthinking and Overthinking: An Empirical Study of Reasoning Length. arXiv preprint 2505.00127. https://arxiv.org/abs/2505.00127. fetched.
15. Chen, Xu, Liang, He, Pang et al. 2024/2025. Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. arXiv preprint 2412.21187. https://arxiv.org/abs/2412.21187. fetched.
16. Hou, Chang, Lu, Qu, Wang et al. 2025. Knowing When to Critique: Task-Adaptive Metacognitive Regulation (MetaCrit). arXiv preprint 2507.15015. https://arxiv.org/abs/2507.15015. abstract.
17. Binder, Chua, Korbak, Sleight et al. 2024. Looking Inward: Language Models Can Learn About Themselves by Introspection. arXiv 2410.13787. https://arxiv.org/abs/2410.13787. fetched.
18. Steyvers, Peters 2025. Metacognition and Uncertainty Communication in Humans and Large Language Models. Current Directions in Psychological Science (arXiv 2504.14045). https://arxiv.org/abs/2504.14045. fetched.
19. Jiang, Zhang, Weller, Wei 2024. SELF-[IN]CORRECT: LLMs Struggle with Discriminating Self-Generated Responses. arXiv preprint 2404.04298. https://arxiv.org/abs/2404.04298. fetched.
20. Tyen, Mansoor, Carbune et al. 2024. LLMs cannot find reasoning errors, but can correct them given the error location. arXiv 2311.08516. https://arxiv.org/abs/2311.08516. fetched.
21. Liu, Geng, Wu, Sucholutsky et al. 2025. Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. arXiv preprint 2410.21333. https://arxiv.org/abs/2410.21333. fetched.
22. Ghosal, Chakraborty, Reddy et al. 2025. Does Thinking More always Help? Mirage of Test-Time Scaling in Reasoning Models. arXiv preprint 2506.04210. https://arxiv.org/abs/2506.04210. fetched.
23. Gema, Hagele, Chen, Arditi et al. 2025. Inverse Scaling in Test-Time Compute. arXiv preprint 2507.14417. https://arxiv.org/abs/2507.14417. fetched.
24. Shojaee, Mirzadeh, Alizadeh et al. 2025. The Illusion of Thinking. Apple preprint, arXiv 2506.06941. https://arxiv.org/abs/2506.06941. fetched.
25. Cuadron, Li, Ma, Wang et al. 2025. The Danger of Overthinking: Examining the Reasoning-Action Dilemma in Agentic Tasks. arXiv preprint 2502.08235. https://arxiv.org/abs/2502.08235. fetched.
26. Turpin, Michael, Perez, Bowman 2023. Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. arXiv 2305.04388. https://arxiv.org/abs/2305.04388. fetched.
27. Chen, Benton, Radhakrishnan et al. 2025. Reasoning Models Don't Always Say What They Think. arXiv preprint 2505.05410. https://arxiv.org/abs/2505.05410. fetched.
28. Sinha, Kapur 2021. When Problem Solving Followed by Instruction Works: Evidence for Productive Failure. Review of Educational Research. https://doi.org/10.3102/00346543211019105. abstract (Crossref record; publisher page gave 403). A second page, https://link.springer.com/10.1007/s11251-020-09525-2, was a snippet.
29. Ashman 2021. Is productive struggle ethical? Blog post (opinion). https://fillingthepail.substack.com/p/is-productive-struggle-ethical. fetched.
30. Rowland 2014. The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. Psychological Bulletin 140(6), 1432-1463. https://doi.org/10.1037/a0037559. memory for the effect size; record confirmed via Europe PMC and Crossref.
31. Bisra, Liu, Nesbit, Salim 2018. Inducing Self-Explanation: a Meta-Analysis. Educational Psychology Review. https://link.springer.com/article/10.1007/s10648-018-9434-x. memory.
32. Barbieri et al. 2023. Meta-analysis of the worked examples effect on mathematics performance. Educational Psychology Review. No URL recorded. memory.
33. Kalyuga, Ayres, Chandler, Sweller 2003. The expertise reversal effect. Educational Psychologist. https://ro.uow.edu.au/edupapers/136. memory.
34. Dunlosky, Rawson, Marsh, Nathan, Willingham 2013. Improving students' learning with effective learning techniques. Psychological Science in the Public Interest. https://journals.sagepub.com/doi/10.1177/1529100612453266. memory.
35. Thompson, Prowse Turner, Pennycook 2011. Intuition, reason, and metacognition. Cognitive Psychology. https://hrcak.srce.hr/en/219803. memory.
36. Chi, Feltovich, Glaser 1981. Categorization and representation of physics problems by experts and novices. Cognitive Science. No URL recorded. memory.
37. Nelson, Narens 1990. Metamemory: a theoretical framework and new findings. Psychology of Learning and Motivation. No URL recorded. memory.
38. Zhang, Shen, Wu, Peng, Wang et al. 2024. Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives. arXiv preprint 2401.02009. https://arxiv.org/abs/2401.02009. abstract.
39. He-Yueya, Goodman, Brunskill 2024. Evaluating and Optimizing Educational Content with Large Language Model Judgments. arXiv preprint 2403.02795. https://arxiv.org/abs/2403.02795. abstract.
