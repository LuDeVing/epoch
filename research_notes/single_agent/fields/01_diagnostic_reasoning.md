# Medical diagnostic reasoning: what it offers one thinking agent

Marks: [V] source checked this session by search (abstract level, not full text unless said); [M] from memory, re-check numbers. No reference below is invented; where I could not confirm a number I say so.

## 1. What the field studies

Diagnosis is a single-answer task under uncertainty with a long tail of costly misses. Researchers study how clinicians go from a few cues to a ranked list of possible diseases (the differential), how they pick tests, and why they err. The main models are hypothetico-deductive reasoning (Elstein: early hypotheses from the first cues, then tests chosen to separate them), pattern recognition and illness scripts (Schmidt and Boshuizen: experts hold compact disease schemas and match to them), and dual-process theory (fast intuitive System 1, slow analytic System 2; Croskerry). The applied branch counts errors (premature closure, anchoring) and tests fixes (checklists, forced reflection, time-outs). This field is the closest human analogue to our "single-answer task where the first natural answer is usually right, but a miss is expensive". Its hardest lesson is the one our data already show: slowing down and doubting by schedule often does not help.

## 2. Core findings

**F1. Premature closure is the top cognitive cause of diagnostic error.** In 100 internal-medicine error cases, cognitive factors were involved in about 74% and system factors in about 65%; premature closure (stopping to consider alternatives once a diagnosis is reached) was the most common cognitive cause. Graber, Franklin, Gordon 2005 [V, abstract]. Strength: moderate. It is a case review with no control group, so it shows where errors cluster, not what fixes them.

**F2. Hypothesis generation is early and small.** Clinicians form 3 to 5 hypotheses within the first minutes, and the right one usually has to be on the list at that point; later reasoning mostly tests the list. Elstein, Shulman, Sprafka 1978 [M]. Strength: strong, replicated across decades, but the numbers are from memory. Implication: failure to generate the right candidate is the root miss, and no later check repairs it.

**F3. Slow, careful reasoning does not beat fast reasoning on average.** Residents told to be careful took about 30% longer per case and were not more accurate than residents told to be fast. Norman et al. 2014, Academic Medicine, randomized, n of 96 and 108 [V, abstract]. A related result: across cases, longer response time correlated with lower accuracy (r = -0.54), Sherbino 2012 [V, via the same search]. Strength: moderate to strong (several controlled experiments). Errors track case difficulty and missing knowledge more than "too fast".

**F4. Generic reflection prompts are mixed.** A systematic review of dual-process interventions found many studies with some effect, with guided reflection the most consistent (Lambe et al. 2016, BMJ Qual Saf [V, via a thesis summary]). A later randomized study of 186 students found reflection gave no more accurate final diagnoses than first impressions (Lambe et al. 2018, Frontiers in Psychology [V]). Strength: weak to mixed. Gains show up when reflection is structured (compare findings against each hypothesis), not when it is "think again".

**F5. A list of alternatives helps only if the right answer is on it.** In a randomized experiment, students given a differential-diagnosis checklist that contained the correct diagnosis scored 0.75 against 0.49 for controls. A checklist without the correct diagnosis scored 0.43 (not significantly different, slightly worse). Time per case rose in both checklist arms. Kämmer et al. 2021, Medical Education [V, abstract]. Strength: one controlled study, clear mechanism. This is the most useful single result for us: prompting alone to "consider alternatives" gives little; a source of good alternatives gives a lot.

**F6. Debiasing checklists and cognitive forcing give small or null effects in controlled work.** Sibbald, Norman et al. compared a debiasing checklist with a knowledge-retrieval checklist on ECG reading (Adv Health Sci Educ 2019) [V for citation only; I did not confirm the result]. From memory, the knowledge-retrieval style checklist helped more than the debiasing style [M]. The AHRQ issue brief on diagnostic checklists is a good summary of the weak-to-moderate evidence [V link found, not read in full]. Strength: weak. Treat "debias by instruction" as unproven.

**F7. Experts organize knowledge as illness scripts; novices reason causally and slowly.** Schmidt and Boshuizen: with experience, long causal chains compress into "encapsulated" scripts of enabling conditions, fault, and consequences [M]. Experts' errors are more about wrong script selection than missing facts. Strength: moderate, mostly qualitative and recall studies. Transfer: an LLM already has the scripts in weights; the open question is whether writing them out helps retrieval.

**F8. Bayesian test selection: choose tests that best split the leading hypotheses, and watch cost.** Normative theory (expected information gain, thresholds for testing vs treating, Pauker and Kassirer [M]). Human clinicians are poor at probabilities (Gigerenzer-style base-rate neglect [M]), but the normative frame is clear. Strength for the theory: strong. Strength that teaching it improves practice: weak. It matches our principle 5 (name a rival, test where they differ).

**F9. Diagnostic time-out and "what else could this be" pauses are plausible but thinly tested.** Practitioner essays recommend them (Croskerry, Graber [M]); I found no controlled trial with a clear gain this session. Strength: weak. Do not rely on it.

## 3. Mechanisms an agent can run

Equal-token comparison is always against the plain model with the same call budget.

**M1. Candidate set before commitment, with an outside source of candidates.**
- Trigger: the problem has a single answer, the probe attempts disagree or no check passes (router branch "escalate"). Not on easy agreement.
- Action: take the probe's distinct answers as the candidate list. Add up to 2 candidates from a separate "list the usual suspects for this problem class" call that does not see the probe answers (fresh sample, so it is independent). Merge, drop duplicates.
- Check: on a set with known answers, measure "gold answer in candidate set" rate (recall) with and without the extra call. Then final accuracy at equal tokens. Pass if recall rises more than the cost of the call.
- Evidence: F2, F5 (alternatives help only when the right one is present). Strength moderate.
- Risk: more candidates give more distractors. Our BrainTeaser data show forced alternatives hurt (92% to 75%). Run only at an impasse, never on agreement.

**M2. Discriminating-evidence step (Bayesian split).**
- Trigger: two or more candidates remain after the probe.
- Action: for the top 2 or 3, write, per candidate, "what would be true if this were right that is false for the others"; pick the single observation or check that best separates them; run it (execute code, test an example, re-read the text for that fact). Update a written ranking.
- Check: accuracy on the "disagree" subset versus best-of-N with the same tokens; also count how often the chosen check actually moved the ranking.
- Evidence: F8 and Elstein hypothetico-deductive loop [M]; fits plan principle 5.
- Risk: if the agent invents the "evidence" from its own head, it is self-critique without a signal (Huang et al. 2023 [M]) and can worsen answers. Require the check to read real input or run code.

**M3. Anti-anchoring: blind second opinion.**
- Trigger: any decision where a single wrong early answer would be costly and no external check exists (BrainTeaser-like, multiple choice).
- Action: one extra independent call that sees the problem but not the first answer; compare; if equal, stop; if different, go to M2.
- Check: error rate on items where call 1 was wrong; compare with a second plain sample at the same cost (this is just self-consistency, so the bar is: beat plain majority vote at equal tokens).
- Evidence: F1 (premature closure), and LLM anchoring results (section 4). Humans: independent second opinions help in some studies [M].
- Risk: nearly identical to best-of-2; may add nothing. Honest expectation: a tie with voting.

**M4. Premature-closure gate, run only when evidence is open.**
- Trigger: the agent is about to output while one critical fact is unverified, or confidence is below a threshold taken from the probe agreement.
- Action: a fixed 3-line close-out: (a) "What finding does my answer not explain?" (b) "What would I regret not having ruled out?" (c) if either has a real item, run a check on it; else stop.
- Check: rate of reversals that were correct vs reversals that broke a right answer. Gate passes only if correct reversals exceed broken ones by a margin on a held-out set.
- Evidence: F1; the "unexplained finding" question is the standard cognitive-forcing item [M]. F3/F4 warn it may do nothing.
- Risk: highest of the five. F3 and our own data say schedule-based doubt costs accuracy. Keep the trigger conditional on low agreement.

**M5. Illness-script cards (retrieval of compact class schemas).**
- Trigger: step 0 classifies the problem into a known class (a puzzle family, a bug type, a research-task type).
- Action: inject at most 2 short cards per class: "enabling conditions, key discriminating features, common look-alikes". Write cards from past lessons (links to the plan's look-back ledger).
- Check: held-out problems of the same class; accuracy with cards vs none at equal tokens; also test a wrong-class card to measure harm.
- Evidence: F7; indirectly F5 (knowledge-retrieval checklists beat debiasing checklists, recalled [M]).
- Risk: a wrong card anchors the model, which is exactly what BiasMedQA-style studies show (section 4).

**M6. Cost-aware information gathering (when the agent can ask for more).**
- Trigger: tasks with tools or lookups of unequal cost.
- Action: before each lookup, state which candidate pair it separates and its cost; skip lookups that separate nothing.
- Check: score = accuracy minus cost, versus plain agent on the same budget.
- Evidence: Microsoft's MAI-DxO scores accuracy and cost together (section 4); F8.
- Risk: planning overhead can eat the budget (our 0% scaffold).

## 4. Evidence on LLMs and AI agents (2023 to 2026)

- **GPT-4 on hard case records.** Kanjee, Crowe, Rodman, JAMA 2023, NEJM clinicopathologic cases [V for existence and method]. From memory the correct diagnosis was in the model's differential in about 64% of cases (45 of 70) [M, re-check].
- **Randomized trial, physicians with an LLM.** Goh et al., JAMA Netw Open 2024 [V]: giving physicians access to an LLM did not significantly improve their diagnostic reasoning score over conventional resources, while the LLM alone scored higher than both physician groups. Lesson: the model's output was not used well by humans. For us: the value is in the program's structure, not in advice that gets ignored. One trial; effects were small.
- **Cognitive bias in medical LLMs.** Schmidgall et al., npj Digital Medicine 2024 [V]. BiasMedQA, 1,273 USMLE-style questions rewritten to carry clinical biases. Six models tested; GPT-4 was most resistant, Llama 2 70B and PMC Llama 13B dropped a lot. Three mitigation strategies helped but did not restore accuracy. Takeaway: small models are more anchorable, and our model is small. I did not read which mitigations worked best.
- **Orchestrated panel for sequential diagnosis.** Microsoft AI, "Sequential Diagnosis with Language Models" and MAI-DxO, 2025 [V via search summaries]. 304 NEJM cases turned into step-by-step encounters where the agent must ask for findings and pays a virtual cost per test. The orchestrator simulates a panel that proposes differentials and picks tests by value versus cost. With o3 it reported about 80 to 85% accuracy (sources differ; 81.9% at about $4,735 average in one summary) against 20% for the generalist physicians they tested. Caveats: authors' own benchmark, virtual costs, no independent replication found, and the physicians worked without references. This is the strongest public example of a diagnostic schema (differential + test choice + cost) wrapped around one model. Whether the gain comes from the panel structure or just more compute per case is not isolated in what I read.
- **Other work I know of but did not verify this session** [M]: Med-PaLM 2 and AMIE (Google, conversational diagnostic dialogue and a differential-diagnosis study); chain-of-thought prompting studies in medical QA (MedPrompt, Nori et al. 2023: dynamic few-shot, self-generated CoT, choice-shuffle ensembling gave large gains on MedQA). The choice-shuffle ensemble is a direct anti-anchoring device and maps to M3. Re-check all numbers before citing.

Strength overall: strong on "LLMs can do differential generation at expert level", weak on "which schema step causes the gain".

## 5. What does not transfer, and where it could hurt

- **Does not transfer:** fatigue, emotion, overconfidence from experience, time pressure, patient interaction, and the "gut feeling" as a bodily state. The remedies for these (take a break, check mood) are void for a model. Human System 1 is learned from thousands of cases; the model's "fast answer" is its prior, so Norman's finding (fast is not worse) likely holds even more for it.
- **Does not transfer well:** checklists work for people partly by prompting memory of facts; the model has the facts, so the useful part is only the retrieval cue (M5), not the nag.
- **Hurts:** (a) Any rule of the form "always list alternatives / always doubt" repeats our BrainTeaser loss. F3 and F4 are the human version of that loss. (b) A candidate list without the right answer can make results worse (F5, 0.43 vs 0.49). (c) Anchoring can come from the schema itself: a wrong illness card or a leading differential steers a small model (BiasMedQA). (d) Setup cost: M1 to M6 together are a heavy scaffold; our heavy scaffold scored 0%. Run at most one or two per problem and only after the router sees disagreement.
- Medicine has a clear-asymmetry cost (missing a deadly disease). Most of our tasks do not. Do not copy "rule out the worst case first" unless a task has that asymmetry.

## 6. Open questions

1. Does an independent "usual suspects" call raise gold-in-candidates enough to pay for itself on ARC-like tasks? (F5 says yes only if recall rises.)
2. Is M3 anything more than majority vote? Test against plain best-of-2 and best-of-3.
3. Does a card from a similar class help or anchor a small model? Needs a wrong-card control.
4. Which part of MAI-DxO's gain is structure and which is compute? An equal-token ablation does not exist in what I found.
5. Does the diagnostic "gate before closing" help once the router already stops on agreement, or is the router the whole benefit?
6. I did not verify: Kämmer's reflection-prompt trial, the exact Sibbald results, and any controlled test of the diagnostic time-out.

## 7. References

1. Graber ML, Franklin N, Gordon R. Diagnostic error in internal medicine. Arch Intern Med 2005;165(13):1493-1499. https://pubmed.ncbi.nlm.nih.gov/16009864/ [V]
2. Norman GR, Sherbino J, Dore K, et al. The etiology of diagnostic errors: a controlled trial of system 1 versus system 2 reasoning. Acad Med 2014;89(2):277-284. https://pmc.ncbi.nlm.nih.gov/articles/PMC4539330 (listed in search; abstract-level) [V]
3. Sherbino J, et al. 2012, response time and accuracy correlation (r = -0.54). Reported in item 2's search context; I did not fetch the paper [M].
4. Lambe KA, et al. Dual-process cognitive interventions to enhance diagnostic reasoning: a systematic review. BMJ Qual Saf 2016;25:808-820. [V for citation, via a thesis summary]
5. Lambe KA, et al. Frontiers in Psychology 2018 (guided reflection randomized study, 186 students). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2018.02297/pdf [V]
6. Kämmer JE, et al. Differential diagnosis checklists reduce diagnostic error differentially: a randomised experiment. Med Educ 2021. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9290564/ [V]
7. Sibbald M, et al. Debiasing versus knowledge retrieval checklists to reduce diagnostic error in ECG interpretation. Adv Health Sci Educ 2019;24(3):427-440. [V for citation only]
8. AHRQ PSNet, diagnostic checklists issue brief. https://www.ahrq.gov/diagnostic-safety/resources/issue-briefs/dxchecklists-7.html [V link only]
9. Kanjee Z, Crowe B, Rodman A. Accuracy of a generative AI model in a complex diagnostic challenge. JAMA 2023;330(1):78-80. https://pmc.ncbi.nlm.nih.gov/articles/PMC10273128 [V for existence; the 64% figure is M]
10. Goh E, et al. Large language model influence on diagnostic reasoning: a randomized clinical trial. JAMA Netw Open 2024;7(10):e2440969. NCT06157944. [V]
11. Schmidgall S, et al. Evaluation and mitigation of cognitive biases in medical language models. npj Digit Med 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11494053/ ; arXiv 2402.08113 [V]
12. Nori H, et al. Microsoft AI / Research. Sequential Diagnosis with Language Models (MAI-DxO), 2025. https://www.microsoft.com/en-us/research/publication/sequential-diagnosis-with-language-models/ ; blog https://microsoft.ai/news/the-path-to-medical-superintelligence/ [V via search summaries; author list not checked]
13. Elstein AS, Shulman LS, Sprafka SA. Medical Problem Solving: An Analysis of Clinical Reasoning. Harvard Univ Press, 1978 [M].
14. Schmidt HG, Boshuizen HPA. On acquiring expertise in medicine. Educ Psychol Rev 1993 [M].
15. Croskerry P. A universal model of diagnostic reasoning. Acad Med 2009 [M].
16. Nori H, et al. Can generalist foundation models outcompete special-purpose tuning? (MedPrompt) arXiv 2311.16452, 2023 [M].
17. Huang J, et al. Large language models cannot self-correct reasoning yet. 2023 [M], cited in 00_PLAN.md.
