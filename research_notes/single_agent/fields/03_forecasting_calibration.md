# Superforecasting and calibration: what it offers one thinking agent

Marks: [V] = checked this session through search results or abstracts (not always the full text); [M] = from memory, re-check numbers. Where I only saw a summary, I say so.

## 1. What the field studies

Forecasting research asks how to put honest numbers on uncertain events and how to score them. The key tool is the Brier score: the squared gap between a stated probability and what happened (0 or 1). Lower is better. A score splits into calibration (when you say 70%, it happens 70% of the time) and resolution (you separate events that happen from events that do not). Tetlock's Good Judgment Project (GJP) ran a four-year tournament for IARPA in which ordinary people, and a top 2% called superforecasters, beat intelligence analysts' baselines [M]. The field also covers aggregation of many forecasters, and how stated confidence relates to being right. For an agent, the useful part is the discipline: start from a base rate, split a question into parts, update in small steps, score yourself, and know how sure you are.

## 2. Core findings

1. **Training, teaming and tracking raised accuracy in GJP.** Mellers et al. 2014 report that probability training (reference classes, bias correction, averaging estimates), team discussion and putting top performers into elite teams all improved calibration and resolution [V, abstract level]. Strength: large field experiment, but see finding 2.
2. **That result is now contested.** A 2025 Psychological Science reanalysis (Dougherty, Hauenstein, Illingworth, Thomas per a library entry [V]) used item response models and found that extra variables reduced, removed, or even reversed the training and teaming effects on latent ability. Its reading: those manipulations change behaviour that may be tournament gaming rather than raw skill. A 2019 Journal of Politics study found teams beat individuals [V, summary]. Strength of the training claim: moderate, disputed. Do not build on "CHAMPS KNOW" as proven.
3. **Extremizing aggregates helps.** Averaging forecasts and then pushing the mean away from 0.5 improved accuracy in GJP [V]. Satopaa, Pemantle and Ungar explain it as information diversity: each forecaster holds different private facts, so the average is too timid [V]. It helps less for superforecaster teams, whose forecasts already share information, and less when self-rated expertise is high [V]. Strength: strong in GJP data, theory matched. Condition: it works only when the voters are diverse. Copies of one voter should not be extremized.
4. **Base rates and the outside view, Fermi decomposition, small updates.** These are the habits described in Tetlock's Superforecasting book and attributed to top forecasters [M]. The evidence is correlational (what top scorers report doing), plus the training result in finding 1. Strength: weak to moderate. Treat as plausible heuristics, not tested causes.
5. **Verbalised confidence in LLMs is usually overconfident, but can be improved.** Tian et al. 2023 report that for RLHF-tuned models, asking for a numeric confidence or a ranked list of guesses with probabilities beat raw token probabilities [V, via citations]. Xiong et al. 2024 (ICLR) compared prompting, sampling and aggregation methods and found no single method consistently best, and all struggle on hard, expert tasks [V]. Strength: several replications, mixed.
6. **Agreement across samples is a better signal than a stated number.** Semantic entropy (Kuhn et al. 2023, Farquhar et al. 2024): sample several answers, group those with the same meaning, take the entropy of the groups [V, via citations]. A 2025 study reports verbalised confidence is overconfident while semantic entropy stays comparatively calibrated, and verbalised confidence approaches it when given more reasoning budget; one model, 270 items, so weak [V, summary].
7. **Models can partly judge their own answers.** Kadavath et al. 2022: large models are well calibrated on multiple choice in the right format. P(True) (propose an answer, then rate its truth) works, and improves when the model sees several of its own samples first. P(IK) ("do I know this") is predictable but calibrates poorly on new tasks [V, abstract].
8. **Reasoning models are a mixed case.** "Thinking Out Loud" (EMNLP 2025) finds reasoning training helps calibration on reasoning tasks but SFT-trained reasoners are more overconfident on factual tasks and say "I don't know" much less. Shorter reasoning went with higher confidence [V, summary]. Another paper (2505.14489) finds calibration improves as the chain unfolds, and drops if slow-thinking behaviours are removed. A third (2506.18183) finds deeper reasoning can raise overconfidence [V, summaries]. These conflict, so strength: low.

## 3. Mechanisms an agent can run

**M1. Probe agreement as a confidence score (route and stop).**
- Trigger: step 0 of the plan, after the 4-5 plain attempts.
- Action: group the attempts' final answers by meaning (exact match for ARC grids and word puzzles; a cheap judge call for text). Write `agree = size of largest group / n` and the group sizes. Do not ask the model to state a confidence number as the main signal.
- Check: on our suites, compute AUROC of `agree` against correctness, and compare with the model's own verbalised 0-100. Then run the router with thresholds at equal tokens: stop when agree >= t, escalate when below. Metric: accuracy per token against plain best-of-N.
- Evidence: semantic entropy [V]; Kadavath on samples [V]; Adaptive-Consistency in the plan.
- Risk: agreement measures consistency, not truth. Small models can agree on a wrong easy-looking answer (our ARC program that fit all examples fooled the agent twice). Always rank real check output above agreement.

**M2. Base-rate anchor before the first attempt (cheap, single call).**
- Trigger: any problem with a numeric, yes/no or "how likely" answer, and the plan's route "no check, single answer".
- Action: write (a) the reference class, (b) the class's typical answer or rate, (c) one adjustment with a reason. Then answer. The anchor is a prior, not a command.
- Check: at equal tokens on BrainTeaser and an estimation set, compare to plain. Log how often the final answer differs from the anchor, and whether those changes were right.
- Evidence: outside-view practice [M]; Halawi et al. use retrieval and base-rate style prompting in their pipeline [V, summary]. No test on puzzle tasks.
- Risk: on word puzzles the "base rate" is meaningless and the step adds tokens and an anchor to be wrong about. Run it only for quantity and probability questions. Our data says extra steps on single-answer tasks cost accuracy.

**M3. Fermi split with a spread (estimation tasks only).**
- Trigger: the answer is a number that no check can verify, and the number is large or unfamiliar.
- Action: split into 3-5 sub-quantities, give each a low-high range, multiply or combine, then compare with the direct guess. If the two differ by more than 3x, flag low confidence and escalate to re-read.
- Check: error in log10 against ground truth versus a direct guess, at equal tokens.
- Evidence: [M] from forecasting practice; no controlled LLM study found by me this session.
- Risk: compounding errors on small models; independence assumed when parts are correlated.

**M4. Small, logged updates with a running probability.**
- Trigger: the revise route, after each real check output.
- Action: write "prior p, new evidence, new p" in one line. Cap a single step at a modest change unless the check is decisive (a test passes or fails).
- Check: Brier score of the logged p over the run, and whether revisions help versus a plain re-ask at equal tokens.
- Evidence: incremental updating is a superforecaster habit [M]; LLM evidence is thin.
- Risk: models fake updates (a number moves to look coherent). Only count it if it ties to a real output. This is the same failure as self-critique without signal (Huang 2023 in the plan).

**M5. Extremize a diverse vote (selection among independent attempts).**
- Trigger: the selector has k attempts that were generated with different prompts or isolated calls, and a probability is needed (for abstain decisions or for ranking answers with no check).
- Action: take each attempt's answer-level support, average in log-odds, multiply by a factor a > 1 (start a = 1.5, tune on held-out), and read the result as the final confidence. Do not extremize if the attempts are near copies.
- Check: log loss and Brier on held-out problems, with and without the factor; abstain-rule accuracy at equal tokens.
- Evidence: GJP extremizing [V]; the condition (diversity) is from Satopaa et al. [V]. AIA Forecaster reportedly uses extremization and supervisor aggregation [V, secondary summary, not checked at source].
- Risk: samples from one model are highly correlated, so the information-diversity argument may not hold. Extremizing correlated votes makes overconfidence worse. Test first; treat the factor as possibly 1.

**M6. Calibration table as the stop/escalate rule (learned from our own logs).**
- Trigger: after enough solved problems exist (a few hundred), at look-back.
- Action: bin `agree` and any verbalised confidence by class; store the observed accuracy per bin. At run time, look up the bin: if observed accuracy >= target, stop; if low, escalate one ladder step; if still low after the ladder, abstain or submit best guess.
- Check: the cost-accuracy curve (accuracy vs mean tokens) against fixed thresholds and against plain. Abstain only if the suite scores abstention as a loss smaller than a wrong answer.
- Evidence: calibration curves are the standard method [M]; reasoning models abstain too little [V, summary].
- Risk: our BrainTeaser full scaffold abstained everywhere and scored 0%. A calibration rule must have a floor: never abstain on the first pass; always submit the plurality answer.

**M7. Self-scoring look-back (Brier ledger).**
- Trigger: step 3, when a ground-truth or check result arrives.
- Action: record stated confidence, outcome, and the miss type (overconfident, underconfident, right-for-wrong-reason). Feed only the class-level calibration offset ("on class X you are 15 points over") to the next prompt, one line.
- Check: held-out calibration error (ECE) and accuracy with versus without the line.
- Evidence: feedback on scores is the core of forecaster improvement [M]; for LLMs, no direct test found.
- Risk: a verbal offset may not change a model's behaviour, and the line costs tokens. Prefer to use it in code (M6) rather than in the prompt.

## 4. Evidence on LLMs and AI agents

- **Halawi et al. 2024 (NeurIPS):** a retrieval, reasoning and ensembling system, evaluated on questions after model cutoffs; roughly matches the crowd aggregate, sometimes beats it; averaging with the crowd is better than either [V, abstract]. One blog reports Brier 0.240 vs crowd 0.247; that number is secondary, re-check. Calibration reached the crowd's level only after fine-tuning and ensembling [V, summary].
- **Schoenegger et al. 2024 (Science Advances):** a crowd of 12 LLMs was statistically indistinguishable from 925 humans on 31 binary questions. Models leaned "yes" (acquiescence bias). Showing models the human median improved GPT-4 and Claude 2 by 17-28%, but plain averaging with humans was better [V]. Small sample, old models.
- **ForecastBench (ICLR 2025) and updates:** best LLMs trail superforecasters by about 0.017 Brier in the latest update, projected parity late 2026 (CI wide) [V, FRI posts]. Difficulty-adjusted scores. Do not trust the extrapolation.
- **Verbalised confidence studies:** Xiong 2024, Tian 2023, Kadavath 2022, semantic entropy, and the reasoning-model papers above [V, abstract/summary level].
- **Agent-level uncertainty:** a 2026 taxonomy paper on uncertainty quantification for LLM agents appeared in my search (arXiv id as returned: 2609.07395) [V, title only]. I did not read it; check it before use.
- **Gap:** I found no study that applies superforecaster training (base-rate, decomposition, update logging) as a procedure to LLMs and measures it at equal tokens on non-forecasting tasks. Our test would be new.

## 5. What does not transfer, and where it could hurt

- **Does not transfer:** tournament motivation and reputation stakes; team social dynamics; the personality traits (actively open-minded, numerate) as such; years of feedback on real events. A model has no stake in its Brier score.
- **Verbalised numbers** often reflect style, not knowledge, especially after RLHF [V, citations]. A model saying 85% is weak evidence.
- **Could hurt, given our data:**
  - Any "doubt your first answer" step (devil's advocate, pre-mortem) matches the forced doubt that cost BrainTeaser accuracy. Forecasting's "update on evidence" is fine; "challenge on a schedule" is not.
  - Fermi and base-rate steps add tokens on puzzles where the first natural answer is right (ARC, word puzzles). Gate by problem type.
  - Calibration-based abstention can collapse to abstaining always (the 0% scaffold). Keep a floor.
  - Extremizing correlated samples inflates confidence.
  - Forecasting questions have no answer in hand; puzzles often have a checker. A check beats any confidence, so confidence is for the no-check route only.

## 6. Open questions

1. Does agreement among 4-5 probe attempts predict correctness well enough on our model to route? Needs AUROC per suite.
2. Is the GJP training effect real? The 2025 reanalysis says it may not be; if so, the human-training story gives no support to M2-M4, and each must stand on our own tests.
3. Are repeated samples from one model diverse enough to justify extremizing at all? Test a = 1 versus 1.5 versus 2.
4. Does a one-line calibration offset in the prompt change behaviour, or only code-side thresholds do?
5. Do reasoning-mode calls become better or worse calibrated mid-chain? The three 2025 papers disagree.
6. Can a calibrated "stop" rule beat a fixed early-stop at equal tokens, or is it the same rule with extra steps?

## 7. References

1. Mellers, B. et al. (2014). Psychological Strategies for Winning a Geopolitical Forecasting Tournament. Psychological Science 25(5), 1106-1115. https://www.psychologicalscience.org/journals/psychological-science/0956797614524255/ [V, abstract]
2. Dougherty, Hauenstein, Illingworth, Thomas (2025). Rethinking the Role of Teams and Training in Geopolitical Forecasting. Psychological Science. https://www.psychologicalscience.org/journals/psychological-science/09567976241266481/ [V, abstract; authors from a library entry]
3. Satopaa, Pemantle, Ungar. Combining Probability Forecasts and Understanding Probability Extremizing through Information Diversity. https://arxiv.org/abs/1501.06943 [V, abstract]
4. Satopaa et al. (2014), logistic-regression extremized log-odds aggregator; Ungar, Mellers, Satopaa, Tetlock, Baron (2012), GJP aggregation. Seen only as cited in search summaries [V, secondary].
5. Powell, Satopaa, MacKay, Tetlock. Skew-Adjusted Extremized-Mean (2022 preprint). https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/Skew-Adjusted.pdf [V, summary]
6. Tetlock and Gardner (2015). Superforecasting. Crown. [M]
7. Halawi, Zhang, Yueh-Han, Steinhardt (2024). Approaching Human-Level Forecasting with Language Models. NeurIPS 2024. https://arxiv.org/abs/2402.18563 [V, abstract]
8. Schoenegger, Tuminauskaite, Park, Tetlock (2024). Wisdom of the Silicon Crowd. Science Advances, doi 10.1126/sciadv.adp1528. https://arxiv.org/abs/2402.19379 [V, summary]
9. Karger et al. (2025). ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities. ICLR 2025. https://arxiv.org/abs/2409.19839 [V, title and FRI posts; author list from memory]. Updates: https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human
10. Xiong et al. (2024). Can LLMs Express Their Uncertainty? ICLR 2024. https://arxiv.org/abs/2306.13063 [V, abstract]
11. Tian et al. (2023). Just Ask for Calibration. EMNLP 2023. [V, via citations; ECE numbers unverified]
12. Kadavath et al. (2022). Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221 [V, abstract]
13. Kuhn, Gal, Farquhar (2023) Semantic Uncertainty; Farquhar et al. (2024) Nature, semantic entropy. [V, via citations]
14. Thinking Out Loud: Do Reasoning Models Know When They're Right? EMNLP 2025. https://arxiv.org/abs/2504.06564 [V, summary]
15. arXiv 2505.14489 (calibration improves along the chain) and arXiv 2506.18183 (introspection, deeper reasoning more overconfident). Titles not captured; read before citing. [V, summary only]
16. Uncertainty Quantification for LLM Agents: A Taxonomy, an Evaluation Protocol, and an Empirical Study. arXiv 2609.07395 (id as returned by search). [V, title only]
