# Expert decision making: what it offers one thinking agent

Ids in brackets point to lines in evidence_a.jsonl (expdec-a), evidence_b.jsonl (expdec-b), evidence_c.jsonl (expert-c) and evidence_d.jsonl (expdec-d). Where a CHECK line in evidence_d disagrees with claims.jsonl, the CHECK line is used. Our own measurements come from 00_PLAN.md and are marked [ours].

## 1. What the field studies

This field asks when expert judgment can be trusted, when it fails, and what experts do at the moment a first answer comes to mind. It mixes three groups. The first is the heuristics-and-biases camp (Kahneman). The second is the naturalistic camp (Klein), which studies experts at work. The third is the study of expert memory and search, mostly in chess. Both camps agree on one test: an intuition is only as good as the regularity of the environment and the feedback that trained it [expdec-a-01]. For an agent this turns into a design question. When should it keep its first answer, when should it doubt it, and what should it use to decide?

## 2. Established findings

Status "established" means two or more independent sources. Counts are thinner than the number of lines suggests, because many lines are the same paper.

**2.1 A familiar good answer blocks a better one, but only when it is good (Einstellung).** In chess, the first idea triggered by familiar features blocks a better solution. Expert players who said they were looking for something better kept fixating on features of the first solution, shown by eye tracking [expdec-a-05]. A second experiment set the boundary. When the familiar move was good but not best, players kept looking at it. When it was a blunder, most players disengaged, and experts who found the best move gradually disengaged [expdec-a-06, expert-c-12]. Independent sources: two (Bilalic 2008, Sheridan and Reingold 2013). Domain: chess only. Effect sizes were not in the abstracts. The agent lesson is a gate. Doubt pays when the first answer is plausible but possibly not best. It buys little when the first answer is obviously wrong or obviously right.

**2.2 LLMs cannot reliably fix their own reasoning without an outside signal.** Huang et al. found that models struggle to self-correct reasoning and sometimes get worse [expdec-a-13, expdec-b-04, expert-c-01]. The Kamoi survey found no prior work showing success with feedback from prompted models, except on unusually well-suited tasks. What works is reliable external feedback or large-scale fine-tuning [expdec-b-05, expert-c-02]. Stechly et al. found that GPT-4 is poor at both solving graph coloring and checking its own solutions, and that iterative gains appear because the right answer is already among the top completions that an outside verifier can spot [expdec-b-06]. A follow-up found self-critique collapsing accuracy on Game of 24, graph coloring and planning, while a sound external verifier gave large gains [expert-c-03]. Independent sources: three. This matches our own result that always-doubt hurt on single-answer tasks [ours].

**2.3 Multi-agent debate does not reliably beat sampling at matched cost.** Du et al. reported gains on math, strategy and factuality [expdec-a-14, expdec-b-08, expert-c-06]. Smit et al. found debate systems do not reliably beat self-consistency or ensembling at matched cost and are sensitive to settings such as agreement level, though some variants improve with tuning [expdec-b-07, expert-c-04]. Wang et al. found a single model with a strong prompt reaches nearly the performance of the best discussion method, and discussion wins only when the prompt has no demonstrations [expert-c-05]. Cemri et al. report minimal gains from multi-agent systems on popular benchmarks, with 1,600+ traces sorted into 14 failure modes, including task verification failures [expert-c-07]. Independent sources: three critiques. Du's gains are real on its tasks. The dispute is about the cause, and the critiques point to extra sampling. Several critiques use older models.

**2.4 Chess expertise is a large library of stored patterns, and the memory edge survives random material.** A meta-analysis found a moderate, significant correlation between expertise and recall of random material, in nearly every study [expdec-a-07]. The numeric r was lost in the abstract. Skilled memory also uses long-term retrieval structures beyond simple chunks [expdec-a-08]. Independent sources: two. This corrects the older claim that the edge vanishes on random positions. It is domain-specific.

**2.5 Models reason more logically than people but keep systematic biases.** Larger PaLM 2 models reasoned more logically than smaller ones and than humans, yet kept systematic errors, some matching human biases and some confident and wrong [expdec-b-19]. On cases where strict logic conflicts with common sense, seven LLMs including GPT-4o reached only mediocre accuracy and applied rules too rigidly [expdec-b-20]. Independent sources: two, both abstract level. No result here shows that a counterexample-search step improves accuracy [expdec-d-11].

## 3. Single-source and contested findings

### 3.1 Single-source

- **Intuition needs a regular environment with feedback; confidence is not a sign of accuracy.** One review by two authors from opposed camps [expdec-a-01, expdec-a-02]. It is a consensus statement, not an experiment.
- **Formulas beat clinical judgment on average.** Mechanical prediction beat clinical judgment by about 10% accuracy. Clinicians were substantially better in only 6 to 16% of studies, and mechanical prediction was substantially better in 33 to 47% [expdec-a-03, expdec-a-04]. One meta-analysis. The two ranges describe different tails of the same distribution. Transfer: prefer a checker or rule over judgment when one exists.
- **Stated LLM confidence is a weak guide.** Verbalized confidence is overconfident. Consistency over several samples reduces overconfidence, no method wins everywhere, and all struggle on professional-knowledge tasks [expdec-b-11]. Failure prediction from confidence was weak, with AUROC from 0.522 to 0.605 [expdec-b-12].
- **Agreement across samples (partly settled by the CHECK line).** In the self-consistency paper, the share of decodes matching the final answer correlated strongly with accuracy on GSM8K for PaLM-540B [expdec-d-06]. Models can estimate P(True) for their own answers, and self-evaluation improves when the model first sees many of its own samples [expdec-d-08]. Against this, errors across models are highly shared. Across 350+ models, when two are both wrong they give the same wrong answer about 60% of the time, and larger models stay highly correlated [expdec-b-10]. The CHECK verdict is that these do not contradict. Agreement ranks items well on average yet can be confidently wrong when errors are shared. Use it as a soft router input, never as proof [expdec-d-12]. No AUROC table was opened.
- **Self-consistency helps.** Over greedy chain of thought: GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-challenge +3.9 points [expdec-b-16]. Original paper only.
- **Execution feedback helps code.** Letting a model see execution results raised accuracy by 2 to 3% on Spider without unit tests and by up to 12% on TransCoder and MBPP with unit tests, and matched baselines using over 10 times more samples [expdec-d-07]. Abstract only. The CHECK verdict is that this agrees with Stechly and Huang, but no paper compared execution and self-critique head to head, so the gap is unmeasured [expdec-d-13].
- **Models prefer their own outputs.** Evaluators favor their own generations, and self-preference tracks self-recognition after fine-tuning, with controlled experiments suggesting a causal link [expdec-a-15, expdec-b-09, expert-c-11]. Three lines, one paper. Transfer: hide authorship from critics.
- **Chain of thought helps mainly on math and symbolic tasks.** A meta-analysis of 100+ papers and 20 datasets on 14 models found little gain elsewhere. On MMLU direct answering is nearly as good unless an equals sign is present [expdec-b-15, expert-c-09]. Same paper twice.
- **Chain of thought can lower accuracy where deliberation also hurts people.** One task dropped by up to 36.3 points for o1-preview against GPT-4o [expert-c-08]. Preprint. It matches our word-puzzle drop [ours].
- **Written reasoning can be unfaithful.** Biasing features cut accuracy by up to 36% across 13 BIG-Bench Hard tasks, and explanations rarely mentioned the bias [expdec-b-18, expert-c-10]. This is a different effect from the 36.3 points above. Implication: a written rationale is not proof of the real reason.
- **Fast and slow are entangled in newer models (full text read, CHECK lines win).** On cognitive reflection tasks, correct answers were 5% for davinci-003, 59% for ChatGPT-3.5 and 96% for ChatGPT-4. Trap answers were 80%, 15% and 0%. Humans were 38% correct and 55% trap [expdec-d-01, expdec-d-05]. The earlier figures in b-13 (70 to 90% traps) and c-14 are superseded by these. Forbidding chain of thought left ChatGPT-3.5 unchanged and cut ChatGPT-4 from 95% to 88% [expdec-d-03]. On semantic illusions correct answers were 18%, 74% and 88%, and davinci fell for the illusion 72% of the time [expdec-d-04]. Prompting davinci-003 to use algebra cut trap answers from 80% to 29% and raised correct from 5% to 28%, but atypical wrong answers rose from 15% to 43% [expdec-d-02]. This is a revised preprint, not yet checked against the journal version [expdec-d-05]. Earlier versions of the claim also appear at [expdec-a-16, expdec-b-14, expert-c-14].
- **LLM Einstellung.** On 5,383 paired medical cases with flipped evidence across 49 diseases and 17 models, frontier models had high accuracy but severe bias-trap rates [expdec-b-01, expert-c-13]. Preprint, credibility 55. The 60.9% figure from the older brief is not in the abstract and is dropped [expdec-b-02].
- **Compositional tasks degrade fast.** Accuracy decays quickly as task complexity grows because transformers match linearized subgraphs [expert-c-15].
- **Reasoning evaluates better than it produces.** The argumentative theory says reasoning exists to build and judge arguments for persuasion, which would explain confirmation bias and weak solitary reasoning [expdec-a-12, expert-c-16]. A theory paper with large commentary.
- **Feeling of rightness.** Initial intuitive answers carry a metacognitive signal. Low feeling led to longer rethinking and more answer changes across four experiments, and the feeling was predicted by how fluently the answer came to mind [expdec-a-10, expdec-a-11]. A machine analogue is untested here.
- **Human forecasts as an anchor.** An ensemble of 12 LLMs matched 925 human forecasters on 31 binary questions, and showing models the median human forecast raised accuracy 17 to 28% [expdec-a-17].
- **Deliberate practice varies by field.** It explained 26% of variance in games, 21% in music, 18% in sports, 4% in education and under 1% in professions [expdec-a-09]. Weakly relevant to agent design.
- **Pattern knowledge can replace search.** A 270M transformer trained on engine values reached a Lichess blitz rating of 2895, about grandmaster level, with no explicit search [expdec-b-17]. Preprint, not a prompting method.
- **Pre-execution critique.** PreFlect critiques and refines plans before acting, using errors distilled from past trajectories. The abstract reports gains over reflection baselines but no numbers [expdec-b-03]. Preprint, credibility 45.
- **Tetlock: foxes beat hedgehogs.** Only a commentary snippet was seen; the book was not opened [expdec-a-20]. Treat as memory-level.

### 3.2 Contested or unresolved

- **Pre-mortem.** Pre-mortem raises the number of reasons generated, but no controlled study shows better final decisions. The "30% more reasons" figure counts reasons, not their quality [expert-c-17]. A study of 178 students, known only from a secondary summary, found that imagining failure lowered confidence in the plan, and measured confidence rather than outcomes [expert-c-18]. The newer papers found are conceptual or qualitative [expdec-a-18]. The CHECK line could not open the 2010 paper and keeps pre-mortem as an untested hypothesis [expdec-d-09]. Thin evidence, not refutation.
- **Recognition-primed decision making.** No primary source was opened and the critics are not covered [expdec-d-10]. A 2026 survey of 225 military personnel found that endorsement of Klein's framework is not one-dimensional [expdec-a-19]. That is attitudes, not decision quality.

## 4. Mechanisms an agent can run

Each mechanism lists Trigger, Action, Check, Evidence and Risk. The Check is always an equal-token test against the plain model, on the suites in 00_PLAN.md. Mechanisms rest on human findings unless stated, and most are hypotheses to measure.

**M1. Verifier first.**
- Trigger: a runnable check exists (examples, unit tests, a program run).
- Action: generate candidates, run them, revise from real outputs, and select only among those that pass.
- Check: against best-of-N with the same checker and the same submissions.
- Evidence: [expdec-b-05, expert-c-03, expdec-b-06, expdec-d-07, expdec-a-03].
- Risk: low. Self-Debug gains were larger with tests [expdec-d-07]. Our ARC run was fooled twice by a program that fit every example [ours], so keep a held-out check. The gap between execution and critique is unmeasured [expdec-d-13].

**M2. Gated doubt.**
- Trigger: the first answer is plausible and the task is open-ended, or a check fails. Not on a schedule.
- Action: only then write a rival answer and the input that separates the two.
- Check: scaffold with the gate against plain, at equal tokens, on BrainTeaser and on NoveltyBench.
- Evidence: [expdec-a-05, expdec-a-06, expert-c-08, expdec-b-02].
- Risk: high if ungated. Always-doubt lost on single-answer tasks [ours]. Self-critique with no signal can reduce accuracy [expdec-a-13]. Einstellung was bounded to good-but-not-best first moves [expdec-a-06]. Chess only.

**M3. Trap-rate calibration per model.**
- Trigger: a new model or a new task family.
- Action: measure how often the first natural answer is the trap on a few known cases, then set the doubt gate from that number.
- Check: compare gated and ungated doubt per model at equal tokens.
- Evidence: [expdec-d-01, expdec-d-02, expdec-d-03].
- Risk: the numbers come from GPT-3 era to GPT-4 models. Weak models had 80% traps and gained from forced reasoning but made new atypical errors. Strong models had 0 to 15% traps [expdec-d-01, expdec-d-02]. Our small models may sit in between.

**M4. Agreement as a soft router.**
- Trigger: step 0 of the plan, a probe of several natural attempts.
- Action: if attempts agree and a check passes, stop. If they split, escalate. Never treat agreement alone as proof.
- Check: log agreement against correctness per task and test whether early stopping loses accuracy at equal tokens.
- Evidence: [expdec-d-06, expdec-d-08, expdec-d-12, expdec-b-10, expdec-b-11].
- Risk: shared errors. About 60% of joint errors are identical across models [expdec-b-10], and stated confidence predicts failure poorly [expdec-b-12]. Samples from one model are more correlated still [ours].

**M5. Blind critic.**
- Trigger: any step where a model judges candidates.
- Action: strip authorship and order cues before the judge sees them, and have it derive the expected answer from the examples before it sees candidate outputs.
- Check: judge accuracy with and without hidden authorship on the same candidates.
- Evidence: [expdec-a-15, expdec-b-09, expert-c-11].
- Risk: low cost. The effect is one paper, and self-preference was shown for judging between texts, not for puzzle selection. Unknown for our models.

**M6. Run, do not narrate.**
- Trigger: the agent writes a reason for its answer.
- Action: treat the rationale as a hypothesis. Require a run, a check against the examples, or a counterfactual test before it counts.
- Check: does requiring a run beat accepting the rationale, at equal tokens?
- Evidence: [expdec-b-18, expert-c-10, expert-c-15].
- Risk: costs extra calls on tasks with no runnable check. There the step does nothing.

**M7. Outside-view anchor for open forecasts.**
- Trigger: a forecasting or estimation task with a known base rate or reference class.
- Action: show the base rate or the human median first, then reason about deviations.
- Check: forecast accuracy with and without the anchor.
- Evidence: [expdec-a-17].
- Risk: 31 questions only [expdec-a-17]. It may anchor wrongly when the case is truly unusual.

**M8. Pre-mortem and pre-execution critique (hypothesis).**
- Trigger: a plan is about to be executed and the run is expensive or irreversible.
- Action: assume the plan failed, list causes, and fix the top ones, drawing on a ledger of past failure causes.
- Check: plan success rate against reflection after failure, at equal tokens.
- Evidence: [expdec-b-03, expert-c-17, expert-c-18, expdec-d-09].
- Risk: the evidence for people shows more reasons, not better decisions. It may waste tokens on single-answer tasks.

**M9. Chunk ledger (hypothesis).**
- Trigger: look-back step after a problem.
- Action: store solved patterns by class, and retrieve a few for the next problem of that class.
- Check: held-out problems of the same class, with and without retrieval.
- Evidence: [expdec-a-07, expdec-a-08, expdec-b-17].
- Risk: the human evidence is chess memory. Retrieval of wrong-class lessons could anchor the agent, which is the Einstellung risk [expdec-a-05].

**M10. One call, not a debate.**
- Trigger: a design choice between a multi-agent debate and several independent samples from one agent.
- Action: prefer independent samples plus a selector over debate rounds. Use several calls only where the plan's diverge mode applies.
- Check: debate against self-consistency at matched tokens.
- Evidence: [expdec-b-07, expert-c-05, expert-c-07, expdec-b-16].
- Risk: low. Debate critiques used older models, so new reasoning models may differ.

## 5. Evidence on LLMs and AI agents

What the field shows for models, in order of strength:

1. External feedback beats self-opinion. Three independent sources agree [expdec-a-13, expdec-b-05, expert-c-03].
2. Debate is mostly extra sampling. Three independent sources agree [expdec-b-07, expert-c-05, expert-c-07].
3. Models are poorly self-calibrated in words [expdec-b-11, expdec-b-12], and their errors are shared with other models [expdec-b-10]. Agreement across samples still ranks items on average [expdec-d-06, expdec-d-12].
4. Chain of thought helps on math and symbolic tasks and not much elsewhere [expdec-b-15]. It can hurt where deliberation hurts people [expert-c-08], and its text may not state the real reason [expdec-b-18].
5. Model strength changes the picture. Weak models fall for traps (80% on CRT) and strong ones almost never do (0%) [expdec-d-01]. Strong chat models solve most reflection items without visible reasoning [expdec-d-03]. A strong model's first answer is therefore more often right, which fits our finding that plain wins on single-answer tasks [ours].
6. Models still anchor. Medical cases with flipped evidence give high bias-trap rates [expdec-b-01]. Models also apply logic too rigidly [expdec-b-20] and keep human-like biases [expdec-b-19].
7. Judging is biased toward self [expdec-b-09].

Not found in this round: any test that recognize-then-simulate, progressive deepening, or a counterexample search helps an LLM [expdec-d-11]. Most of the model studies use GPT-4 class or older models, and our agent runs smaller ones.

## 6. What does not transfer to a model

- **Years of experience feeding a pattern library.** The human chess results rest on thousands of hours of trained pattern memory [expdec-a-07, expdec-a-08]. A model has no such personal history, and the Einstellung experiments need trained patterns to trigger. Whether a model's version matches is unknown.
- **Eye-tracking and fixation findings.** The mechanism of Einstellung was shown through gaze [expdec-a-05]. A model has no gaze. We can test only its behavior, as the medical benchmark does [expdec-b-01].
- **Felt confidence.** Humans have a fluency-based feeling of rightness [expdec-a-11]. A model's verbalized confidence is weak [expdec-b-12]. Only sampling-based agreement is a possible substitute, and it is partly settled and risky [expdec-d-12].
- **Deliberate practice.** Explained variance in people [expdec-a-09] says nothing about inference-time steps.
- **Human fast versus slow.** Models show the pattern less cleanly. Strong models stay accurate when chain of thought is blocked [expdec-d-03], so fast and slow are entangled and a two-system split may be the wrong picture.
- **Group dynamics and persuasion.** The argumentative theory assumes people who want to win [expdec-a-12]. Copies of one model do not have independent views [expdec-b-10].
- **Fox versus hedgehog traits.** The evidence is a snippet [expdec-a-20], and a model has no stable style to select.

## 7. Open questions

1. Does agreement across samples predict correctness well enough to route on? The strongest item is partly settled with one model on mostly in-distribution tasks, and no AUROC table was opened [expdec-d-12]. Our own router data is the test.
2. Does a doubt step help a small model that falls for traps more often? The CRT evidence suggests yes for weak models and no for strong ones [expdec-d-01, expdec-d-02]. Measure per model.
3. Does execution beat self-critique head to head, and by how much? [expdec-d-13]
4. Do recognize-then-simulate, progressive deepening or counterexample search improve an LLM at equal tokens? No evidence found [expdec-d-11, expdec-d-10].
5. Does a pre-mortem change outcomes, for people or agents? [expdec-d-09, expdec-a-18]
6. Do debate critiques hold for newer reasoning models? [expert-c-04, expert-c-07]
7. Is the hurt-by-deliberation result for o1-preview model-specific? [expert-c-08]
8. How well does naturalistic decision research outside chess (firefighters, nurses) hold up, and what do Klein's critics say? [expdec-d-10]
9. Are the Hagendorff figures unchanged in the journal version? [expdec-d-05]

## 8. References

How checked: fetched = full page opened; abstract = abstract opened; snippet = search snippet only; memory = no page opened.

1. Kahneman D, Klein G. 2009. Conditions for intuitive expertise: a failure to disagree. American Psychologist 64(6):515-526. https://pubmed.ncbi.nlm.nih.gov/19739881/ (abstract) [expdec-a-01, a-02]
2. Grove WM, Zald DH, Lebow BS, Snitz BE, Nelson C. 2000. Clinical versus mechanical prediction: a meta-analysis. Psychological Assessment 12(1):19-30. https://pubmed.ncbi.nlm.nih.gov/10752360/ (abstract) [expdec-a-03, a-04]
3. Bilalic M, McLeod P, Gobet F. 2008. Why good thoughts block better ones: the mechanism of the pernicious Einstellung (set) effect. Cognition 108(3):652-661. https://pubmed.ncbi.nlm.nih.gov/18565505/ (abstract) [expdec-a-05]
4. Sheridan H, Reingold EM. 2013. The mechanisms and boundary conditions of the Einstellung effect in chess. PLoS ONE 8(10):e75796. https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/ (fetched; also https://pubmed.ncbi.nlm.nih.gov/24124515/, abstract) [expdec-a-06, expert-c-12]
5. Sala G, Gobet F. 2017. Experts' memory superiority for domain-specific random material generalizes across fields of expertise: a meta-analysis. Memory & Cognition 45(2):183-193. https://pubmed.ncbi.nlm.nih.gov/27770253/ (abstract) [expdec-a-07]
6. Gobet F, Simon HA. 1996. Templates in chess memory. Cognitive Psychology 31(1):1-40. https://pubmed.ncbi.nlm.nih.gov/8812020/ (snippet) [expdec-a-08]
7. Macnamara BN, Hambrick DZ, Oswald FL. 2014. Deliberate practice and performance in music, games, sports, education, and professions: a meta-analysis. Psychological Science 25(8):1608-1618. https://pubmed.ncbi.nlm.nih.gov/24986855/ (abstract) [expdec-a-09]
8. Thompson VA, Prowse Turner JA, Pennycook G. 2011. Intuition, reason, and metacognition. Cognitive Psychology 63(3):107-140. https://pubmed.ncbi.nlm.nih.gov/21798215/ (abstract) [expdec-a-10, a-11]
9. Mercier H, Sperber D. 2011. Why do humans reason? Arguments for an argumentative theory. Behavioral and Brain Sciences 34(2):57-74. https://pubmed.ncbi.nlm.nih.gov/21447233/ (abstract) [expdec-a-12, expert-c-16]
10. Huang J, Chen X, Mishra S, Zheng HS, Yu AW, Song X, Zhou D. 2024. Large language models cannot self-correct reasoning yet. ICLR 2024. https://arxiv.org/abs/2310.01798 (abstract; fetched in the c round) [expdec-a-13, b-04, expert-c-01]
11. Kamoi R, Zhang Y, Zhang N, Han J, Zhang R. 2024. When can LLMs actually correct their own mistakes? A critical survey of self-correction of LLMs. TACL. https://arxiv.org/abs/2406.01297 (abstract; fetched in the c round) [expdec-b-05, expert-c-02]
12. Stechly K, Marquez M, Kambhampati S. 2023. GPT-4 doesn't know it's wrong: an analysis of iterative prompting for reasoning problems. arXiv preprint 2310.12397. https://arxiv.org/abs/2310.12397 (abstract) [expdec-b-06]
13. Stechly K, Valmeekam K, Kambhampati S. 2024. On the self-verification limitations of large language models on reasoning and planning tasks. arXiv preprint 2402.08115. https://arxiv.org/abs/2402.08115 (fetched) [expert-c-03]
14. Du Y, Li S, Torralba A, Tenenbaum JB, Mordatch I. 2024. Improving factuality and reasoning in language models through multiagent debate. ICML 2024. https://arxiv.org/abs/2305.14325 (abstract; fetched in the c round) [expdec-a-14, b-08, expert-c-06]
15. Smit A, Duckworth P, Grinsztajn N, Barrett TD, Pretorius A. 2023. Should we be going MAD? A look at multi-agent debate strategies for LLMs. ICML 2024. https://arxiv.org/abs/2311.17371 (abstract; fetched in the c round) [expdec-b-07, expert-c-04]
16. Wang Q, Wang Z, Su Y, Tong H, Song Y. 2024. Rethinking the bounds of LLM reasoning: are multi-agent discussions the key? arXiv preprint 2402.18272. https://arxiv.org/abs/2402.18272 (fetched) [expert-c-05]
17. Cemri M et al. 2025. Why do multi-agent LLM systems fail? arXiv preprint 2503.13657. https://arxiv.org/abs/2503.13657 (fetched) [expert-c-07]
18. Panickssery A, Bowman SR, Feng S. 2024. LLM evaluators recognize and favor their own generations. NeurIPS 2024. https://arxiv.org/abs/2404.13076 (abstract; fetched in the c round) [expdec-a-15, b-09, expert-c-11]
19. Kim E, Garg A, Peng K, Garg N. 2025. Correlated errors in large language models. ICML 2025. https://arxiv.org/abs/2506.07962 (abstract) [expdec-b-10]
20. Xiong M, Hu Z, Lu X, Li Y, Fu J, He J, Hooi B. 2024. Can LLMs express their uncertainty? An empirical evaluation of confidence elicitation in LLMs. ICLR 2024. https://arxiv.org/abs/2306.13063 (abstract) [expdec-b-11, b-12]
21. Hagendorff T, Fabi S, Kosinski M. 2023. Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in ChatGPT. Nature Computational Science 3(10):833-838. https://pmc.ncbi.nlm.nih.gov/articles/PMC10766525 (fetched), and arXiv:2212.05206 v2 https://arxiv.org/pdf/2212.05206 (fetched, full text; preprint) [expdec-a-16, b-13, b-14, expert-c-14, expdec-d-01 to d-05]
22. Sprague Z, Yin F, Rodriguez JD, Jiang D, Wadhwa M, Singhal P, Zhao X, Ye X, Mahowald K, Durrett G. 2025. To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. ICLR 2025. https://arxiv.org/abs/2409.12183 (abstract; fetched in the c round) [expdec-b-15, expert-c-09]
23. Wang X, Wei J, Schuurmans D, Le Q, Chi E, Narang S, Chowdhery A, Zhou D. 2023. Self-consistency improves chain of thought reasoning in language models. ICLR 2023. https://arxiv.org/abs/2203.11171 (abstract; ar5iv version fetched) [expdec-b-16, d-06]
24. Liu R, Geng J, Wu AJ, Sucholutsky I, Lombrozo T, Griffiths TL. 2024. Mind your step (by step): chain-of-thought can reduce performance on tasks where thinking makes humans worse. arXiv preprint 2410.21333. https://arxiv.org/abs/2410.21333 (fetched) [expert-c-08]
25. Turpin M, Michael J, Perez E, Bowman SR. 2023. Language models don't always say what they think: unfaithful explanations in chain-of-thought prompting. NeurIPS 2023. https://arxiv.org/abs/2305.04388 (abstract; fetched in the c round) [expdec-b-18, expert-c-10]
26. Chen W, Zhu Z, Huang G, Wang W. 2026. MedEinst: benchmarking the Einstellung effect in medical LLMs through counterfactual differential diagnosis. arXiv preprint 2601.06636. https://arxiv.org/abs/2601.06636 (abstract; fetched in the c round) [expdec-b-01, b-02, expert-c-13]
27. Wang H, Cao Y, Lin L, Chen J. 2026. PreFlect: from retrospective to prospective reflection in large language model agents. arXiv preprint 2602.07187. https://arxiv.org/abs/2602.07187 (abstract) [expdec-b-03]
28. Ruoss A et al. 2024. Amortized planning with large-scale transformers: a case study on chess. arXiv preprint 2402.04494. https://arxiv.org/abs/2402.04494 (abstract) [expdec-b-17]
29. Eisape T, Tessler MH, Dasgupta I, Sha F, van Steenkiste S, Linzen T. 2023. A systematic comparison of syllogistic reasoning in humans and language models. arXiv preprint 2311.00445. https://arxiv.org/abs/2311.00445 (abstract) [expdec-b-19]
30. Chan J, Gaizauskas R, Zhao Z. 2025. RULEBREAKERS: challenging LLMs at the crossroads between formal logic and human-like reasoning. ICML 2025. https://arxiv.org/abs/2410.16502 (abstract) [expdec-b-20]
31. Dziri N et al. 2023. Faith and fate: limits of transformers on compositionality. NeurIPS 2023. https://arxiv.org/abs/2305.18654 (fetched) [expert-c-15]
32. Schoenegger P, Tuminauskaite I, Park PS, Bastos RVS, Tetlock PE. 2024. Wisdom of the silicon crowd. Science Advances 10(45):eadp1528. https://pubmed.ncbi.nlm.nih.gov/39514669/ (abstract) [expdec-a-17]
33. Chen X, Lin M, Schaerli N, Zhou D. 2023. Teaching large language models to self-debug. arXiv preprint 2304.05128. https://arxiv.org/abs/2304.05128 (abstract) [expdec-d-07]
34. Kadavath S et al. 2022. Language models (mostly) know what they know. arXiv preprint 2207.05221. https://arxiv.org/abs/2207.05221 (abstract) [expdec-d-08]
35. Wippold GM, Garcia KA, Domlyn A, Wong D, Fernandez ME. 2025. Proactive planning for contextual fit: the role of the implementation premortem. Implementation Science Communications. https://pubmed.ncbi.nlm.nih.gov/40775380/ (abstract) [expdec-a-18]
36. Mitchell DJ, Russo JE, Pennington N. 1989. Back to the future: temporal perspective in the explanation of events. J Behavioral Decision Making 2. Known only through a blog summary, https://corporate.jasoncollins.blog/premortem (snippet) [expert-c-17]
37. Veinott B, Klein G, Wiggins S. 2010. Premortem experiment. Title and venue not confirmed. Known only through the same blog summary (snippet); the paper could not be opened [expert-c-18, expdec-d-09]
38. Mattingsdal J. 2026. Assessing military professionals' endorsement of decision-making assumptions. Behavioral Sciences 16. https://pubmed.ncbi.nlm.nih.gov/42073967/ (abstract) [expdec-a-19]
39. Keil FC. 2010. When and why do hedgehogs and foxes differ? Critical Review 22(4):415-426. Search listing https://europepmc.org/search?query=Keil%20hedgehogs%20foxes%202010 (snippet; Tetlock's book not opened) [expdec-a-20]
40. Klein G, Calderwood R, Clinton-Cirocco A (1986) and Lipshitz et al. (2001), recognition-primed decision model. No primary source opened (memory) [expdec-d-10]
