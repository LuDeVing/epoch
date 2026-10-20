# Intelligence analysis and structured analytic techniques: what it offers one thinking agent

Marks: [V] checked this session (page or abstract fetched, or search result read); [M] from memory, re-check numbers. Where I only saw a search summary and not the full paper, I say so.

## 1. What the field studies

Intelligence analysis is judgment under uncertainty with thin, conflicting, sometimes deceptive evidence and no clean ground truth. Richards Heuer's *Psychology of Intelligence Analysis* (CIA, 1999) [M] argued that analysts fail less from lack of data than from habits of mind: they lock onto one story early, treat evidence that fits the story as proof, and never write down the rivals. The field's answer is a set of structured analytic techniques (SATs): Analysis of Competing Hypotheses (ACH), key assumptions check, devil's advocacy, red team, premortem. These force the analyst to externalize the reasoning so it can be inspected. Since about 2016 a small group (Mandel, Dhami, Karvetski, Chang, Tetlock) has tested whether the techniques work. The result is the most useful part for us: the logic is sound, but the controlled evidence for the full procedure is weak or negative.

## 2. Core findings

**F1. ACH procedure and its one clever idea.** [M] List all plausible hypotheses. List evidence. Build a matrix: each cell says whether an item is consistent, inconsistent, or neutral to a hypothesis. Work across rows, not down columns. Drop evidence that fits every hypothesis (it has no diagnostic value). Prefer the hypothesis with the least evidence against it, not the most for it. This rests on a sound point from philosophy of science (Popper; also Platt 1964, already in our plan): confirming evidence is cheap, disconfirming evidence is informative. Strength of the logic: strong. Strength of evidence that humans following the procedure judge better: see F2.

**F2. ACH did not improve judgment in controlled tests.**
- Mandel, Karvetski, Dhami 2018, *Judgment and Decision Making* 13(6) [V, abstract and results fetched]. 50 UK intelligence analysts, randomized to ACH or no method, on a task with four hypotheses and 12 cues and known ground truth. ACH did not improve accuracy: mean absolute error 0.26 for ACH vs 0.21 for control (p = .14, favoring control). No gain in rank order or coherence (probabilities summed to 1.77 for ACH, 1.54 for control; ideal is 1.0). Small, young sample, simple task. Strength: moderate (one randomized trial, small N).
- Same paper [V]: what did work was statistical repair. Forcing probabilities to sum to 1 cut error from 0.23 to 0.15 (35%). Averaging 50 analysts after that cut it to 0.09 (61%). Most of the aggregation gain came from about three analysts.
- Same paper [V]: ACH-trained analysts rated cue usefulness much closer to its true probability gain (r = .68 vs .17 for control) but this did not carry into better final probabilities. So the "diagnosticity" step trained a skill that the later steps did not use.
- Dhami, Belton, Mandel 2019, *Applied Cognitive Psychology*, "The analysis of competing hypotheses in intelligence analysis" [V, abstract via search result]. 50 analysts, randomized. ACH users did not complete all steps. Mixed evidence on confirmation bias. ACH may raise inconsistency and error.
- Karvetski and Mandel 2020, *JDM* 15(6) [V, fetched]. 227 participants, six cases, uncertain evidence with varied source reliability. No coherence advantage for ACH. ACH slightly less reliable on matched case pairs (mean deviation .22 vs .18, p = .051, d = 0.20). Both groups were too conservative (stayed near 50/50). ACH users let non-diagnostic evidence move their scores by roughly 30% of the effect of fully diagnostic evidence ("pseudo-diagnostic weighting"). Authors: findings do not support ACH improving probabilistic judgment. Strength: moderate, consistent with the 2018 and 2019 trials.
- Whitesmith 2019: ACH did not reduce confirmation bias or serial position effects [V, only as cited inside Karvetski and Mandel 2020; original not read].

**F3. Layout may matter more than procedure.** Dhami et al. 2024, *Cognitive Research: Principles and Implications* [V, search result only; full text blocked by redirects, so details unconfirmed]. People shown hypotheses in rows and evidence in columns were less likely to show confirmation bias; the standard ACH layout did not give this effect. Read as: how evidence is laid out against hypotheses can change behavior. Strength: weak to moderate, one paper, not fully read.

**F4. SATs may fix one bias by causing its opposite, and decomposition is untested.** Chang, Berdini, Mandel, Tetlock, "Restructuring structured analytic techniques in intelligence," *Intelligence and National Security* 2017/2018 [V, abstract via search result; exact year and author list vary across sources]. Their claims: SATs treat bipolar biases (can err in either direction) as unipolar, and the assumption that breaking a problem into a matrix cuts noise had never been tested. Strength: argument plus review, not a trial.

**F5. Field-level evidence is thin.** RAND (Artner, Girven, Bruce 2016, RR1408) [V, search result]: the US intelligence community strongly pushes SATs but has made little effort to measure whether they improve analysis. A pilot found products that used SATs addressed a wider range of outcomes. That is breadth, not accuracy. A separate systematic review reported moderate to strong support for ACH, brainstorming and devil's advocacy [V, seen only as a search snippet, source not identified; treat as unverified].

**F6. Devil's advocacy and dialectical inquiry.** Management research on groups: Schweiger, Sandberg and colleagues found groups using devil's advocacy or dialectical inquiry made better-quality decisions than consensus groups, with no difference between the two (1986 AMJ and 1989 follow-up) [V, via search summaries]. Schwenk 1990 meta-analysis (*OBHDP* 47(1), 161-176) exists [V, bibliographic record only; effect sizes not read]. Strength: moderate for group decision quality on business cases. Caveat [M]: critics note effects are on decision quality in lab cases and that devil's advocacy can reduce confidence and satisfaction. No intelligence-specific trial that I found.

**F7. Wisdom of a few, plus repair, beats method.** The strongest positive result in this field is F2's second bullet: coherence repair and averaging a small number of independent judgments. Independent judgments plus aggregation is a mechanism an agent can run cheaply, and it matches our probe-and-vote step.

## 3. Mechanisms an agent can run

Ranked by how well evidence plus our own data support them. None is "run ACH always."

**M1. Evidence-by-hypothesis matrix, built only at a split (the "ACH-lite").**
- Trigger: the probe attempts disagree (route ESCALATE) or the problem is explanatory with several live causes and a fixed pool of evidence (diagnosis, debugging, "which rule fits these examples"). Not when attempts agree.
- Action: the program asks for 2 to 5 mutually exclusive hypotheses taken from the disagreeing probe answers. Then for each evidence item (the examples, test outputs, facts in the prompt), one short call scores consistent / inconsistent / neutral per hypothesis, evidence-major order (rows = evidence). Count inconsistencies per hypothesis in code. Pick fewest inconsistencies; ties go to the simplest.
- Check: at equal tokens, accuracy on the subset of problems where the probe split, vs plain majority vote of the same number of calls. Also log whether the matrix winner differs from the vote winner and who is right when they differ.
- Evidence: logic of F1; no human trial shows gain (F2). So this is a hypothesis to measure, but in code the counting is done by the program, which removes the human failure of not finishing steps (Dhami 2019). Strength: weak.
- Risk: the matrix scoring is itself LLM judgment, so one score error flips the pick. Pseudo-diagnostic weighting (F2) means neutral items leak into scores; the program must discard items marked consistent with all hypotheses.

**M2. Diagnosticity filter: the best next test.**
- Trigger: two or more hypotheses survive and a cheap test exists (run code on a new input, query a fact, probe an example).
- Action: from the matrix, find the evidence item or test input where the hypotheses disagree most. Compute expected outputs per hypothesis before running. Run it. Drop items all hypotheses predict equally.
- Check: tests used per solved problem, and accuracy at equal calls vs choosing a random test. In the plan this is the "input where rivals disagree" tie-break; here it is made a loop.
- Evidence: Mandel 2018 found usefulness ratings can track true probability gain (r = .68) when trained [V]; Platt 1964 and Klayman and Ha 1987 are in the plan. Strength: moderate in principle, our ARC selector already benefits from similar anchoring.
- Risk: costs calls; wasted if the problem is a plain-answer one.

**M3. Key assumptions check, at an impasse only.**
- Trigger: ladder step 3 (re-read) after two failed revisions.
- Action: one call lists the assumptions the current best candidates share ("grid is the output size", "name means the same as in the prompt") and marks each as stated in the task, inferred from examples, or assumed. The program then spawns one attempt per assumption of the third kind with that assumption negated.
- Check: rescue rate on impasse problems vs an equal number of fresh resamples.
- Evidence: SAT practice [M]; no trial. It targets shared assumptions, which a resample of the same model will repeat. Strength: weak.
- Risk: our BrainTeaser result shows forced doubt hurts when the first answer was right. Fires only after failed checks, never on a schedule.

**M4. Coherence repair and small-panel aggregation of probabilities.**
- Trigger: any step where the agent outputs a probability over a set of mutually exclusive answers (a forecast, a rubric score, a choice among options).
- Action: normalize to sum to 1 in code. Draw 3 independent calls and average the normalized vectors.
- Check: Brier or log score vs a single call, at equal tokens against best-of-3 by vote.
- Evidence: the strongest positive result here (35% error cut by repair, 61% with aggregation, about three judges capturing most of it) [V, human analysts, one task]. Strength: moderate; transfer to LLMs untested by this paper but cheap.
- Risk: averaging only helps if the calls are not copies of each other. Same-model samples are correlated; use varied prompts.

**M5. Devil's advocate as a scored second pass on the leader, not as a default.**
- Trigger: no external check exists, stakes of a wrong answer are high, and the probe agreed (so we are confident, which is when an unchecked error is most costly). Open question whether to use at all; see section 5.
- Action: an isolated call gets the task and the leader answer and must write the strongest case against it plus one observable test that would break it. The program runs the test if one exists; if no test exists, the critique is discarded unless it names a concrete fact in the prompt that contradicts the answer.
- Check: net flips (right to wrong vs wrong to right) at equal tokens. Gate: must not lose on BrainTeaser by more than 1 point.
- Evidence: group-decision studies (F6), not LLM tasks. Our own data says unconditional doubt hurts. Strength: weak.
- Risk: highest of the five. Make it opt-in and keep the discard rule.

**M6. Hypotheses-first, evidence-major layout for the prompt itself.**
- Trigger: whenever the agent must weigh many facts against several options.
- Action: present options as rows or columns in a fixed table and put the facts in the other axis, so each fact is judged against all options in one pass.
- Check: A/B the same prompt content in prose vs table, at equal tokens.
- Evidence: Dhami 2024 layout effect [V, snippet only]. Strength: weak.
- Risk: our rewriting of names into codes made the small model worse; keep the problem's own words in cell labels.

## 4. Evidence on LLMs and AI agents

Reported separately. This is thin. I found no 2023-2026 paper that tests a full ACH matrix on LLMs against a plain baseline.

- Jhaveri, GX-Chen, Sucholutsky, Choi, "Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models," arXiv 2604.02485, April 2026 (ICLR 2026 listing seen) [V, abstract fetched]. Eleven LLMs, a Wason 2-4-6 style rule-discovery task. Models often propose tests that confirm their hypothesis rather than test it, which slows rule discovery. Prompting with human interventions such as "consider counterexamples" cut the bias, and rule-discovery rate rose from 42% to 56% on average. They distilled the behavior into the model and it carried to a second task (Blicket test). This is the closest support for M2 and M3. It is an exploration task with a hidden rule and feedback, i.e. a setting where doubt is pointed at a check. Strength: moderate (11 models, one paradigm).
- A search result described a framework for murder-mystery puzzles (MuSR) in which "hypothesis structuring" gave most of the gain across 10 models [seen only in a search summary from ksp.etri.re.kr; I could not confirm the paper title, authors, or the claimed 89% figure; do not cite until found].
- Structure-aware search paper, arXiv 2609.00738 [V as a search result, not read in full]: standard tree search can stay in one "reasoning basin" and keep elaborating the same suspect on a MuSR case; keeping a distinct alternative hypothesis alive fixed the example. One example is an anecdote, not a result.
- Cognitive-bias benchmarks for LLMs (arXiv 2410.15413, CogBias 2604.01366, CoBRA 2509.13588) [V as search results] measure confirmation bias and similar effects. None I saw scores diagnosticity or ACH matrices.
- LLM-as-analyst proposals exist (an Afeka research-center page proposes multi-agent LLMs for ACH) [V, search result; a project description, not a result].

Read together: LLMs do show a confirm-first habit in hypothesis testing, and a counterexample prompt helps when a feedback signal exists. Whether a full matrix beats it is unmeasured. That gap is itself a cheap experiment for us.

## 5. What does not transfer, and where it could hurt

Does not transfer:
- The human worry about career, group consensus, and organizational pressure. An agent has none of that.
- Analyst training and compliance. Humans skipped ACH steps (Dhami 2019); a program does not skip. This removes one reason ACH failed, so human null results do not prove an agent null.
- Inter-analyst independence in red teaming. Several calls of one model share its blind spots.
- Intelligence tasks have no ground-truth check at decision time. Many of our tasks do. When a check exists, run it; do not build a matrix.

Where it could hurt, given our data:
- ACH ends in "pick the hypothesis with least evidence against." On single-answer tasks the first natural answer is usually right; building rivals and scoring inconsistencies is forced doubt in a new costume. Our BrainTeaser drop (92% to 75%) is the warning.
- Cost: a matrix is one call per evidence item. With 10 items and 4 hypotheses that is a lot of tokens and our heavy scaffold already hit 0% from setup cost.
- Human trials found ACH users no better and slightly less consistent (F2). A pipeline that adds judged steps adds noise sources.
- Pseudo-diagnostic weighting: the model will count neutral facts as support for a favorite. The program must filter, not trust.
- Devil's advocacy lowers confidence in correct answers; with an LLM judge reading the critique, correct answers get overturned.

Rule that follows: all six mechanisms sit behind the router and fire only on a split among probes, a failed check, or an open explanatory problem with a fixed evidence pool. None runs on the converge path.

## 6. Open questions

- Does code-counted ACH on LLM-scored cells beat majority vote on the subset of problems where probes split? (M1, cheapest test.)
- Is the human null result due to unfinished steps, bad interface, or because the method itself adds noise? Karvetski 2020 suggests noise from non-diagnostic evidence; an agent with a hard filter may differ.
- Does the Dhami 2024 layout effect replicate for LLMs, and does it hold for rows vs columns? I could not read the full paper.
- Do three varied-prompt samples of one model act like three analysts for the aggregation gain (M4)? Correlated errors may shrink it.
- Can the diagnosticity step be made reliable (r near .68 against true information gain) with a small model?
- I found no controlled intelligence trial of red teaming or key assumptions check. They remain practice, not evidence.

## 7. References

1. Heuer, R. J. Jr. (1999). *Psychology of Intelligence Analysis.* CIA Center for the Study of Intelligence. [M] (ACH is in chapter 8.)
2. Mandel, D. R., Karvetski, C. W., Dhami, M. K. (2018). Boosting intelligence analysts' judgment accuracy: What works, what fails? *Judgment and Decision Making* 13(6), 607-621. [V] https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html
3. Dhami, M. K., Belton, I., Mandel, D. R. (2019). The "analysis of competing hypotheses" in intelligence analysis. *Applied Cognitive Psychology.* [V, abstract] https://strathprints.strath.ac.uk/69049/
4. Karvetski, C. W., Mandel, D. R. (2020). Coherence of probability judgments from uncertain evidence: Does ACH help? *Judgment and Decision Making* 15(6), 939-958. [V] https://dlab.sauder.ubc.ca/sjdm/journal/20/200430/jdm200430.html
5. Dhami et al. (2024). Study of ACH matrix layout and confirmation bias. *Cognitive Research: Principles and Implications.* DOI 10.1186/s41235-024-00560-y. [V snippet only; authors and title not confirmed] https://cognitiveresearchjournal.springeropen.com/articles/10.1186/s41235-024-00560-y
6. Chang, W., Berdini, E., Mandel, D. R., Tetlock, P. E. (2017/2018). Restructuring structured analytic techniques in intelligence. *Intelligence and National Security.* [V abstract via search; year and author list uncertain]
7. Artner, S., Girven, R., Bruce, J. (2016). *Assessing the Value of Structured Analytic Techniques in the U.S. Intelligence Community.* RAND RR1408. [V search result] https://www.rand.org/pubs/research_reports/RR1408.html
8. Schwenk, C. R. (1990). Effects of devil's advocacy and dialectical inquiry on decision making: a meta-analysis. *Organizational Behavior and Human Decision Processes* 47(1), 161-176. [V record only] https://ideas.repec.org/a/eee/jobhdp/v47y1990i1p161-176.html
9. Schweiger, D. M., Sandberg, W. R., Ragan, J. W. (1986). Group approaches for improving strategic decision making. *Academy of Management Journal* 29(1), 51-71. [V via citation list]
10. Whitesmith, M. (2019). ACH, confirmation bias and serial position effects. [V only as cited in item 4]
11. Jhaveri, A. R., GX-Chen, A., Sucholutsky, I., Choi, E. (2026). Failing to Falsify: Evaluating and Mitigating Confirmation Bias in Language Models. arXiv 2604.02485. [V] https://arxiv.org/abs/2604.02485
12. Escaping Redundant Reasoning: Structure-Aware Search for Inference-Time LLMs. arXiv 2609.00738. [V search result, not read] https://arxiv.org/pdf/2609.00738
13. A Comprehensive Evaluation of Cognitive Biases in LLMs. arXiv 2410.15413. [V search result] https://arxiv.org/pdf/2410.15413
14. Platt, J. R. (1964). Strong inference. *Science.* Klayman, J., Ha, Y. (1987). Confirmation, disconfirmation, and information in hypothesis testing. *Psychological Review.* [V in the plan; not rechecked here]
