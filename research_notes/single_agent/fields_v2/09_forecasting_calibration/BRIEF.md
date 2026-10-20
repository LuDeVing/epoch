# Forecasting and calibration: what it offers one thinking agent

Evidence ids are written short: a-01 means forecasting-a-01, and so on. Where the round-2 CHECK lines (d-xx) disagree with claims.jsonl, the CHECK lines are used.

## 1. What the field studies

Forecasting research asks how well people and machines put numbers on uncertain events, and how to improve those numbers. The main tools are the Brier score (squared error of a probability) and calibration (do 70% claims come true 70% of the time). The field has three parts. The first is human studies: the Good Judgment Project tournaments, overconfidence and the planning fallacy (a-01, a-11, a-12). The second is aggregation: how to combine many forecasts (a-05, a-09). The third is newer: how well language models state confidence and forecast real events (a-14, a-19, a-21).

For our agent the field offers two things. One is a way to attach honest confidence to an answer, which a router could use. The other is a set of habits (outside view, decomposition, small updates) that might improve a single answer. The evidence is stronger for the first than for the second.

## 2. Established findings

**E1. People are overconfident, and inside-view estimates run optimistic.**
- People who claimed 100% certainty on general-knowledge items were wrong about 20% of the time. Nominal 90% intervals captured the answer about 50% of the time (a-12, review, Lichtenstein et al. 1982).
- Planning fallacy: 37 students predicted 33.9 days for a thesis and took 55.5 days. About 30% finished inside their own estimate (a-11, n=37).
- Overestimation is strongest on hard tasks (a-13, Wikipedia summary, weaker).
- These are human data. They support "take the outside view" only by analogy for a model.

**E2. Agreement among several samples, and better aggregation, reduce verbalised overconfidence in LLMs.**
- Xiong et al. tested prompting, sampling and aggregation on 5 datasets and 5 LLMs. Consistency across sampled responses reduced overconfidence (a-14, b-14, ICLR 2024).
- Kuhn et al. found that grouping sampled answers by meaning predicts QA accuracy better than comparable baselines (a-17, b-16). Farquhar et al. (Nature 2024) extended the idea: average AUROC 0.790 over 30 task-model combinations, against 0.691 for naive entropy and 0.698 for P(True) (d-06, d-09).
- Caveats. The semantic-entropy papers come from one lab (d-09). Gains are over a weak baseline (c-09 makes the same point for verbalised confidence). Test models were open-weight, not Claude (d-07).

**E3. LLM forecasting systems with retrieval and ensembling come close to the human crowd, and experts still lead.**
- Halawi et al.: a retrieval-augmented system nears the crowd aggregate on post-cutoff questions and sometimes beats it (a-19, b-03). On 914 test questions it scored Brier 0.179, against the crowd at 0.149 and the best plain baseline at 0.208 (d-03).
- On ForecastBench, experts beat the top LLM with p < 0.001 in the original paper (a-21, b-06, c-13). A later update puts superforecasters ahead by 0.017 Brier (a-22, an organisation page).
- Lu 2025 (abstract only) says LLMs beat the crowd but trail experts (b-08). The AIA Forecaster report claims parity with superforecasters (b-07, preprint, weaker).
- Status: established in direction. Nearly all sources are preprints, and the parity date (November 2026) is a projection from an interested party (a-22).

## 3. Single-source and contested findings

### 3a. Contested

**C1. Human forecasting training and teaming.** Mellers et al. 2014 reported that training, teaming and tracking drove accuracy. Probability training was randomly assigned and taught reference classes, bias correction and averaging (a-01, a-02). The abstract gives no effect size (a-01), and the full paper could not be opened (d-20). A 2025 reanalysis with item response theory found these effects were eliminated, reduced or reversed once extraneous variables were controlled (a-03, b-01, c-01, Psychological Science). It also found that strategic-responding traits separate superforecasters, so the cause of their edge is hard to identify (a-04, b-02, c-02). The reanalysis uses the same GJP data, so it is one dissent, not a replication. "Base rates, decomposition and small updates cause skill" is a plausible heuristic and nothing more.

**C2. Do reasoning models know their limits?** Three preprints, three emphases.
- Yoon et al.: reasoning models were better calibrated than non-reasoning ones in 33 of 36 settings (6 models, 6 datasets, 1,000 examples each), and calibration improved along the chain (b-17, c-06, d-10). Removing exploring and backtracking hurt calibration most (TriviaQA ECE 0.042 to 0.161) (b-18, d-11). Models were open-weight, not Claude (d-10).
- Mei et al.: reasoning models often state over 85% confidence when wrong, and deeper reasoning raises confidence in wrong answers (b-19, c-04, d-12). This appears where accuracy stays flat with depth, as on SimpleQA. Where accuracy rose with depth (GPQA), deeper reasoning helped (d-12).
- Zeng et al.: reasoning training improves verbal calibration on reasoning tasks, but models say "I don't know" far less on factual tasks (a-18, b-20, c-07).
- CHECK d-14 says these mostly do not conflict. Yoon compares model pairs. Mei varies depth inside one model and tests introspection. A factual-versus-math split does not explain the difference. Neither tests a current Claude model. In Mei, Claude 3.7 Sonnet was the best calibrated, and its error rose only about 2 points from low to high reasoning, against about 7 for o3-mini (d-13).

### 3b. Single-source

- **S1. Extremizing.** The best amount depends on how much forecasters' information overlaps, and it helps only when they hold diverse private information (a-05, b-22, c-16; cite arXiv 1406.2148, since 1501.06943 was withdrawn, a-06). Satopaa 2021 (snippet) says removing noise mattered more than correcting bias (a-09).
- **S2. Verbalised beats token probabilities.** For RLHF models, verbalised confidence roughly halved calibration error against token probabilities on TriviaQA, SciQ and TruthfulQA (a-15, b-12, c-09). One study, three QA sets, weak baseline.
- **S3. Self-evaluation.** Large models are reasonably calibrated on multiple choice and true/false in the right format. P(True) improves when the model sees several of its own samples. P(IK) generalises poorly to new tasks (a-16, b-15, c-10). One preprint, older models.
- **S4. Semantic entropy limits.** It detects only confabulation from missing knowledge. It misses confident errors from training misconceptions and systematic reasoning failures (d-07). It costs about 5 to 10 times more compute in extra samples (d-08).
- **S5. LLM crowds.** Twelve LLMs matched 925 humans on only 31 binary questions, with a strong yes-bias (a-20, b-04, c-11, d-16). Showing GPT-4 and Claude 2 the human median improved them 17 to 28%, but plain averaging beat it (b-05, c-12). Suggestive only.
- **S6. Logical consistency.** LLM forecasts contradict each other across related questions, and the inconsistency score correlates with later Brier score (b-10, c-15). Usable as a label-free check. One preprint.
- **S7. Pastcasting.** Resolved-question benchmarks give results comparable to live forecasting (b-11, abstract only). Leaked-answer retrodiction scores should be treated as inflated (c-13).
- **S8. Outcome-based RL.** A 14B model trained on forecasting outcomes matched o1 accuracy and improved calibration (b-09, abstract only).
- **S9. Agents.** Step-level calibration does not imply trajectory-level calibration. Step errors are coupled, and averaging hides late overconfidence (b-21, 2026 preprint, 4 models).
- **S10. Traits.** Cognitive ability, knowledge and open-mindedness predicted accuracy (a-10, snippet). Experts' long-run predictions were often no better than others, and foxes beat hedgehogs (a-23, memory only).
- **S11. Promotional numbers.** The claims that GJP was 35 to 72% more accurate and that superforecasters beat analysts by 30% come from press and organisation pages (a-07, a-08). Use as a warning, not as effect sizes.

## 4. Mechanisms an agent can run

The key negative finding comes first. Two papers bear directly on whether forecasting procedures help an LLM, and neither shows a gain. On PaLM 2 with 692 questions, no structured strategy beat the plain prompt on unweighted Brier: Basic 0.1062, Base Rates 0.1233, Breakdown 0.1815 (d-01). That edge is partly a label artifact, since about 63% of questions resolved No, and on a class-balanced score the human baseline beat every LLM method (d-02). Halawi never isolated the base-rate prompt, and the paper calls its prompt gain minor (d-03). Verdict: not supported (d-04, d-05). Our own data agrees that forced extra steps hurt single-answer tasks (c-17). So every mechanism below sits behind a gate.

**M1. Outside-view check (reference class first).**
- Trigger: a quantitative estimate on a task with a known class (duration, cost, success rate) and no external check. Not for puzzles or lookups.
- Action: name a reference class, state its typical result, then adjust.
- Check: run plain answer and M1 at equal tokens on resolved estimates. Score Brier plain and class-balanced.
- Evidence: a-11, a-12, a-02. Against: d-01, d-04.
- Risk: it was worse than plain in the only LLM test (d-01). Human support is by analogy (E1) and contested (C1).

**M2. Spend calls on facts, not on templates.**
- Trigger: the answer depends on facts outside the model's training.
- Action: retrieve, then reason once. Do not add reasoning scaffolds.
- Check: ablate retrieval against prompt structure at equal calls.
- Evidence: d-03, d-21 (removing retrieval moved Brier 0.186 to 0.206; the reasoning prompt gave a minor gain).
- Risk: single preprint (d-21). Retrieval adds noise and cost on tasks that need none.

**M3. Sampled-agreement probe as a confidence signal.**
- Trigger: step 0 of the plan, a single-answer question with no checker.
- Action: draw several samples, group by meaning, use the spread as uncertainty. Escalate only if the group splits.
- Check: AUROC of the spread against correctness, at the token cost of the same samples used for a best-of-N baseline.
- Evidence: a-14, b-14, a-17, d-06, d-08.
- Risk: same-model samples share beliefs, so agreement can be shared error (d-07, d-15). It cannot catch systematic reasoning failures (d-07). Cost is 5 to 10 times (d-08).

**M4. Direct verbalised confidence, nothing added.**
- Trigger: any final answer that a router or user will act on.
- Action: ask once for a probability with the answer. Do not add a "reflect on your uncertainty" pass.
- Check: calibration error against M3 on resolved items.
- Evidence: a-15, b-12, c-09, d-13 (reflection made Claude 3.7 worse, c-05).
- Risk: LLMs are overconfident when verbalising (a-14, b-13). Evidence is on 2022 to 2024 models (d-14).

**M5. Cross-question consistency check.**
- Trigger: the agent holds several related claims or estimates (a plan, a forecast set).
- Action: write the logical relations (A implies B; P(A) + P(not A) = 1) and test them. Re-ask on violation.
- Check: does the violation score predict error better than chance, per extra call spent?
- Evidence: b-10, c-15.
- Risk: single preprint, binary forecasts. Consistent answers can still be wrong.

**M6. Do not extremize one-model samples.**
- Trigger: aggregating several samples from the same model.
- Action: average, and do not push the result away from 50%.
- Check: compare extremized and plain averages on resolved items.
- Evidence: a-05, c-16, d-15. The rule is our inference and untested (d-17).
- Risk: if real diversity exists (different prompts, retrieved facts), averaging may leave signal unused.

**M7. Trajectory-level confidence for long runs.**
- Trigger: an agent run with many steps and a final answer.
- Action: record confidence at each step and at the end. Flag a late jump that no new check backs.
- Check: does the trajectory signal predict final failure better than mean step confidence?
- Evidence: b-21.
- Risk: one 2026 preprint. Extra bookkeeping tokens.

**M8. Prediction ledger (design proposal).** Log each stated confidence and its resolved outcome, and recalibrate from the agent's own history. No source tests this. It is our extension of the training idea (a-02, contested) and the RL result (b-09, abstract only).

## 5. Evidence on LLMs and AI agents

- Verbalised confidence is overconfident (a-14, b-13). Larger models calibrate better (a-14). No elicitation method wins consistently, and all struggle on professional-knowledge tasks (b-13, c-08).
- Multiple choice and true/false in the right format are well calibrated (a-16). Verbalised confidence beats token probabilities for RLHF models (a-15).
- Semantic entropy works on QA for open-weight models (d-06). It needs many samples (d-08).
- Different models still share errors. Across 350+ LLMs, two wrong models gave the same wrong answer about 60% of the time on one dataset. Correlation rises with shared provider and with model size and accuracy (d-15). Within one model it is probably higher, but this was not measured (d-17).
- On forecasting, retrieval pipelines approach the crowd, and experts lead by about 0.017 Brier (d-03, a-22). A crowd of 12 different LLMs matched humans on 31 questions (a-20).
- For agents, step calibration does not carry to the trajectory (b-21).
- Abstention has a survey (d-18, abstract). No evidence was found on confidence-based routing for open-ended tasks (d-19).

## 6. What does not transfer to a model

- Human training effects (C1). Contested in humans and untested in models (a-03, d-04).
- Superforecaster traits and team effects (a-04, a-10). Teams made of one model are correlated (d-15).
- Extremizing, which assumes diverse private information (a-05). One model's samples are not independent voters (d-15, d-17).
- The planning-fallacy mechanism (a-11) rests on human motivation. Only the outside-view habit might carry over, and the one LLM test failed (d-01).
- Promotional margins (a-07, a-08).
- Semantic entropy as a truth test. Low entropy does not guarantee factuality (d-07).

## 7. Open questions

1. Does a reference-class or decomposition procedure beat plain answering at equal tokens for a current Claude-class model? The only direct test used PaLM 2 (d-01, d-04), and 2025 work was not searched (d-05).
2. How much confidence signal survives when all voters are one model, or one model with varied prompts or retrieved facts? No direct measurement (d-17).
3. Does sampled or verbal confidence predict correctness on open-ended work (design, research), not only QA and binary events? Not found (d-19).
4. When should an agent abstain or escalate, and how does a confidence router perform? Only a survey was opened (d-18, d-19).
5. Do 2022 to 2024 calibration results hold for current models? Neither Yoon nor Mei tested a Claude 4-class model (d-14).
6. Does an agent that recalibrates on its own resolved predictions improve (M8)? Not covered.
7. The Mellers 2014 effect size and the 2019 Journal of Politics teams study could not be verified (d-20).

## 8. References

1. Mellers, Ungar, Baron, Ramos, Gurcay, Fincher, et al. (2014). Psychological Strategies for Winning a Geopolitical Forecasting Tournament. Psychological Science 25(5). https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/ . Checked: fetched (abstract level; full paper blocked, d-20). Ids: a-01, a-02.
2. Hauenstein, Thomas, Illingworth, Dougherty (2025). Rethinking the Role of Teams and Training in Geopolitical Forecasting. Psychological Science 36(1). https://www.psychologicalscience.org/journals/psychological-science/09567976241266481/ . Checked: fetched. Ids: a-03, a-04, b-01, b-02, c-01 to c-03.
3. Satopaa, Pemantle, Ungar (2014). Combining Probability Forecasts and Understanding Information Diversity. arXiv 1406.2148 (1501.06943 withdrawn). https://arxiv.org/abs/1406.2148 . Checked: fetched. Ids: a-05, a-06, b-22, c-16.
4. Satopaa et al. (2021). Bias, Information, Noise (BIN) model of forecasting. Management Science. Via https://en.wikipedia.org/wiki/Superforecaster . Checked: snippet. Id: a-09.
5. Mellers et al. (2015). The psychology of intelligence analysis: drivers of prediction accuracy in world politics. Via https://en.wikipedia.org/wiki/Superforecaster . Checked: snippet. Id: a-10.
6. Wikipedia pages on the Good Judgment Project and Superforecaster. https://en.wikipedia.org/wiki/Good_Judgment_Project ; https://en.wikipedia.org/wiki/Superforecaster . Checked: fetched (weak sources). Ids: a-07, a-08.
7. Buehler, Griffin, Ross (1994), planning fallacy, via https://en.wikipedia.org/wiki/Planning_fallacy . Checked: fetched (secondary). Id: a-11.
8. Lichtenstein, Fischhoff, Phillips (1982), overconfidence, via https://en.wikipedia.org/wiki/Overconfidence_effect . Checked: fetched (secondary). Ids: a-12, a-13.
9. Tetlock (2005). Expert Political Judgment. Book. https://en.wikipedia.org/wiki/Expert_Political_Judgment . Checked: memory. Id: a-23.
10. Xiong, Hu, Lu, Li, Fu, He, Hooi (2024). Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs. ICLR 2024. https://arxiv.org/abs/2306.13063 . Checked: fetched. Ids: a-14, b-13, b-14, c-08.
11. Tian, Mitchell, Zhou, Sharma, et al. (2023). Just Ask for Calibration. https://arxiv.org/abs/2305.14975 . Checked: fetched. Ids: a-15, b-12, c-09.
12. Kadavath et al. (2022). Language Models (Mostly) Know What They Know. Preprint. https://arxiv.org/abs/2207.05221 . Checked: fetched. Ids: a-16, b-15, c-10.
13. Kuhn, Gal, Farquhar (2023). Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation. https://arxiv.org/abs/2302.09664 . Checked: fetched. Ids: a-17, b-16.
14. Farquhar, Kossen, Kuhn, Gal (2024). Detecting hallucinations in large language models using semantic entropy. Nature 630:625-630. https://www.nature.com/articles/s41586-024-07421-0 . Checked: fetched. Ids: d-06, d-07, d-09.
15. Kossen, Han, Razzak, Schut, et al. (2024). Semantic Entropy Probes. Preprint. https://arxiv.org/abs/2406.15927 . Checked: fetched. Id: d-08.
16. Yoon, Kim, Yang, Kim, Kim (2025). Reasoning Models Better Express Their Confidence. Preprint. https://arxiv.org/abs/2505.14489 . Checked: fetched. Ids: b-17, b-18, c-06, d-10, d-11.
17. Mei, Zhang, Yin, Lidard, et al. (2025). Reasoning about Uncertainty: Do Reasoning Models Know When They Don't Know? Preprint. https://arxiv.org/abs/2506.18183 . Checked: fetched. Ids: b-19, c-04, c-05, d-12, d-13.
18. Zeng, Xuan, Cui, Voigt (2025). Thinking Out Loud: Do Reasoning Models Know When They're Right? Preprint. https://arxiv.org/abs/2504.06564 . Checked: fetched. Ids: a-18, b-20, c-07.
19. Halawi, Zhang, Yueh-Han, et al. (2024). Approaching Human-Level Forecasting with Language Models. Preprint. https://arxiv.org/abs/2402.18563 . Checked: fetched. Ids: a-19, b-03, c-14, d-03, d-21.
20. Schoenegger, Tuminauskaite, Park, Tetlock (2024). Wisdom of the Silicon Crowd: LLM Ensemble Prediction Capabilities Rival Human Crowd Accuracy. Science Advances. https://arxiv.org/abs/2402.19379 . Checked: fetched. Ids: a-20, b-04, b-05, c-11, c-12, d-16.
21. Karger, Bastani, Yueh-Han, et al. (2025). ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities. https://arxiv.org/abs/2409.19839 . Checked: fetched. Ids: a-21, b-06, c-13.
22. Forecasting Research Institute (2026). LLMs are closing the gap on human forecasters (Substack post). Checked: fetched (organisation page). Id: a-22.
23. Alur, Stadie, Kang, et al. (2025). AIA Forecaster: Technical Report. Preprint. https://arxiv.org/abs/2511.07678 . Checked: fetched. Id: b-07.
24. Lu (2025). Evaluating LLMs on Real-World Forecasting Against Human Superforecasters. Preprint. https://arxiv.org/abs/2507.04562 . Checked: abstract. Id: b-08.
25. Turtel, Franklin, Skotheim, et al. (2025). Outcome-based Reinforcement Learning to Predict the Future. Preprint. https://arxiv.org/abs/2505.17989 . Checked: abstract. Id: b-09.
26. Paleka, Sudhir, Alvarez, et al. (2025). Consistency Checks for Language Model Forecasters. Preprint. https://arxiv.org/abs/2412.18544 . Checked: abstract (b-10) and fetched (c-15). Ids: b-10, c-15.
27. Wildman, Bosse, Hnyk, Muhlbacher, et al. (2025). Bench to the Future: A Pastcasting Benchmark for Forecasting Agents. Preprint. https://arxiv.org/abs/2506.21558 . Checked: abstract. Id: b-11.
28. Lin, Lan, Guan, Jing, Fan (2026). Uncertainty Quantification for LLM Agents. Preprint. https://arxiv.org/abs/2609.07395 . Checked: fetched. Id: b-21.
29. Pratt, Blumberg, Carolino, et al. (2024). Can Language Models Use Forecasting Strategies? Preprint. https://arxiv.org/abs/2406.04446 . Checked: fetched. Ids: d-01, d-02, d-04, d-05, d-17.
30. Kim, Garg, Peng, Garg (2025). Correlated Errors in Large Language Models. https://arxiv.org/abs/2506.07962 . Checked: fetched. Id: d-15.
31. Wen, Yao, Feng, Xu, Tsvetkov (2024). Know Your Limits: A Survey of Abstention in Large Language Models. TACL. https://arxiv.org/abs/2407.18418 . Checked: abstract. Ids: d-18, d-19.
32. Project measurements, C:\Users\User\Desktop\AGI\research_notes\single_agent\00_PLAN.md (2026). Checked: read locally. Id: c-17.
