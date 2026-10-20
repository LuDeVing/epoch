# Cognitive science of reasoning and problem solving: what it offers one thinking agent

Evidence ids are written as a-01, b-05, d-11 and so on. They are the lines in evidence_a to evidence_d.jsonl of this folder. Where an evidence_d CHECK line (d-17 to d-22) disagrees with claims.jsonl, the CHECK line wins. Most human findings below were read from abstracts or snippets, not full papers, and the checked level is in the references.

## 1. What the field studies

The field asks how people search for answers, when they stop, and when they doubt a first answer. It has five main strands. Problem solving as search through a space of states, using means-ends analysis and subgoals (a-20, a-21). Dual-process work on when a quick first answer is kept or checked (a-07 to a-13, b-16, b-18, c-01). Insight work on how a stuck solver changes the way the problem is represented (a-04, a-05, c-20). Scientific reasoning as a search over hypotheses and over experiments (a-01, a-02, a-03). Work on thinking biases and logic errors (a-16, a-17, a-18). A newer strand tests language models on the same tasks (a-22, b-06, b-14, b-15, c-12, c-16).

For our project the field matters for one reason. Our data say the first natural answer is usually right on puzzles, and forced doubt hurt. This field says when doubt is worth its cost.

## 2. Established findings

"Established" here means two or more credible sources. The critique warns that independence is often lower than the count, so each entry says how independent the sources really are.

**E1. On human reasoning items, correct answers are often already present in the first, fast response.** In four two-response experiments with a deadline and memory load, many correct logical answers came at once, and slow correction was not the main source of correct final answers (c-01, a-10). A summary of the same study reports about 30% logical at once, about 10% corrected by deliberation, and about half wrong and kept (a-10, snippet level). Raoelison and colleagues found that repeated deliberation did not raise the accuracy of later fast answers, and that correct final answers were often non-corrective (c-02, snippet). A related extension from the same lab supports the pattern (b-16). Independence is about 2 labs. The check line d-17 says Ghasemi 2022 does not report the share of correct first responses, so b-17 is dropped from this finding. Size: no pooled effect size. The percentages above are from one paper and a secondary summary.

**E2. Lower confidence in the first answer predicts more reflection and more answer changes.** Seen in three lines of work (a-11, a-12, a-13). All are snippet level. Pennycook adds that conflict detection sometimes fails (a-13). No effect size was read.

**E3. Chain of thought helps mainly on math and symbolic tasks, and little elsewhere.** A meta-analysis of over 100 papers, 20 datasets and 14 models found this, and on MMLU CoT matched direct answering unless an equals sign was present (c-12, fetched). On Blocksworld planning, gains appear only with very specific prompts and fade as problem size grows (c-17, fetched). Independence: two groups.

**E4. Reasoning models often reach the right candidate and then fail to keep it.** On 201 Japanese insight riddles, reasoning models often wrote the correct candidate in the thought log but did not endorse it (b-01, preprint, fetched). On AIME 2024, models disregarded a correct solution even when given it (b-13, preprint, fetched). Reasoning models scored 17.6% on the riddles, non-reasoning models 7.6%, humans 52.9% (b-02). Two preprints, two groups.

**E5. External checks fix planning where the model alone is poor.** GPT-4 averaged about 12% success on plan generation, and external verifiers that send back errors are the proposed fix (b-09, b-10, c-17). All preprints, and effectively one research group, so treat the count as about 1.5.

**E6. Without outside feedback, self-correction does not help and often hurts.** Huang and colleagues (fetched) report GSM8K GPT-3.5 75.9 to 74.7, GPT-4 95.5 to 89.0, Llama-2 62.0 to 36.5, and CommonSenseQA GPT-3.5 75.8 to 41.8 after two rounds (c-14, d-05). Earlier gains used ground-truth labels to decide when to stop (GPT-3.5 GSM8K 75.9 to 84.3), so they were oracle-guided (d-07). With outside feedback, CRITIC beats chain of thought: AmbigNQ F1 58.6 to 64.9, HotpotQA F1 42.8 to 52.9 (d-08). Its no-tool variant gains little on QA (58.3, 46.1) and is mixed on math (d-09). Check d-19: supported for external feedback, but no source here is compute matched.

**E7. Folk tricks failed replication.** Hard-to-read fonts did not raise Cognitive Reflection Test scores: the original plus 16 replications gave no effect (a-14, fetched). The unconscious-thought advantage gave g = -0.01 in a replication with N = 399, and a meta-analysis of 61 effects fell from g = 0.15 to 0.018 after trim-and-fill (a-15, fetched). Do not build disfluency or distraction-incubation steps.

**E8. Models show human-like content effects in logic.** Logic tasks are answered better when the content supports the inference (b-14). Larger PaLM 2 models are more logical than smaller ones, yet keep human-like errors such as sensitivity to term order (b-06). Two labs.

**E9. Problem solving is search, and representation changes difficulty.** The search framing with means-ends analysis and subgoals is foundational (a-20). Isomorphic Tower of Hanoi problems differ in difficulty (a-21, findings not read). This is a framework, not an effect size.

## 3. Single-source and contested findings

### Single-source

- **Trap items.** On designed conflict items the intuitive answer was right only about 20% (base rate) and 24% (conjunction) of the time, yet reasoners were about 10 points less confident than on controls (a-07, a-08, fetched, N = 247 and 147). Trap items are built to fool people, so 20% is not a base rate for real work.
- **CoT can hurt.** CoT lowered accuracy in 3 of 6 human-psychology tasks (b-03, c-13, d-10, preprint). The headline 36.3 points is o1-preview against GPT-4o, not one model with CoT on and off (d-11, d-20). Same-model drops are 23.1 (GPT-4o), 8.0 (Claude 3 Opus), 6.05 (Gemini 1.5 Pro), about 2 for small Llamas (d-11). Face recognition fell for GPT-4o 64.0 to 51.2 and Claude 3 Opus 44.0 to 29.6 (d-12). Claude 3.5 Sonnet rose 65.9 to 67.7 on implicit learning (d-10). Quote 23.1, not 36.3. No replication was found (d-20).
- **Counterexamples are hard for models.** The best agent made a valid counterexample for under 9% of wrong solutions on REFUTE, though it solved up to 48% of the same problems (b-05, preprint, fetched).
- **Unfaithful reasoning text.** Biasing features such as always labelling the answer (A) dropped CoT accuracy by up to 36% on 13 tasks, and the explanations did not mention the bias (c-18, fetched).
- **Search over thoughts.** On Game of 24, GPT-4 CoT solved about 4% and Tree of Thoughts about 74% (b-08, snippet, one task, many calls).
- **Biases are weakly tied to ability.** Myside, framing, anchoring and base-rate neglect are weakly related to intelligence (a-16, a-17, one lab, snippet). A medical preprint with 5,383 cases and 17 LLMs suggests models hold on to a common first diagnosis against counterfactual evidence (b-07, fetched; the figure was not verified).
- **SDDS.** Scientific reasoning as hypothesis search plus experiment search, extended to four spaces (a-01, a-02, a-03, c-11). Samples were 20 and 10 adults. No replication found (c-11), and no LLM application by name (b-21).
- **Early GPT models made human-like intuitive errors on reflection items; ChatGPT models mostly did not**, even with CoT blocked (b-15, a-22). One paper. a-22 is from memory.
- **Aha is not a clean marker.** 56.1% of correct insight solutions came with Aha in one study (b-22, unnamed listing, weak). See also a-06 and c-09.

### Contested

- **Strict fast-then-slow dual process.** De Neys argues that heuristic and logical intuitions are both generated at once and deliberation matters mainly when they conflict (a-09, b-18). Critics say the two-types framework lacks support, and defenders reply that the critique targets a non-central premise (c-03). The field is still revising it (c-04). We use "check when signals conflict", not two modules.
- **Insight as sudden representational change.** Supported by matchstick studies, where representational change had a strong effect and heuristics a minimal one (a-04, a-05, c-20). A 2023 review and a 2023 change-point paper call the suddenness evidence inconclusive because it rests on self-report (a-06, c-09).
- **Talking hurts insight.** Schooler found it (c-05). An 80-person test did not (c-06). A 2025 replication of no effect was known only from a search summary (c-07). A 115-student study found neither pure view wins (c-08). Face verbal overshadowing did replicate (c-19), so the effect is task specific.
- **Reasoning-model collapse.** Reasoning models lose to plain models on easy puzzles, gain at medium, and collapse at high complexity (c-15, b-11). A rebuttal says the Hanoi collapse is partly an output token limit and River Crossing had impossible instances (b-12, preprint, preliminary). Overthinking of trivial items is better supported than the collapse (c-16).
- **Mental-model theory.** People represent mostly true cases and miss false ones (a-18). A 2012 meta-analysis of 12 syllogism theories found none adequate (c-10). No test shows that adding a counterexample step helps an LLM. The LLM fit in a-19 is a preprint, and its arXiv id matches b-06, so the attribution of a-19 is unreliable.
- **Self-consistency as a confidence signal.** Calibrated when the model is mostly right, but it amplifies confidence in systematic errors (b-19). Asking for verbal confidence calibrated better at about one fifth the cost (ECE 0.166 vs 0.229) (b-20). Both are unnamed 2026 preprint snippets. Do not rely on them.

## 4. Mechanisms an agent can run

All checks must be run at equal total tokens against the plain model, with the gate overhead counted (d-02, d-18). Our own data set the default: puzzles and single-answer items trust the first answer, open tasks diverge.

**M1. Task-type gate for deliberation.**
- Trigger: start of every problem.
- Action: classify as math or symbolic, planning, pattern-feel or perceptual, single-answer puzzle, or open-ended. Allow written step-by-step reasoning only for the first two. For pattern-feel items keep a direct-answer arm.
- Check: plain model vs gate at equal tokens, on a mixed set of the five task types.
- Evidence: c-12, c-17, d-10, d-11, d-12, c-16.
- Risk: a wrong classification sends a task down the wrong path. Harm size depends on the model (d-10), so measure on our own model before trusting the table.

**M2. Short answer first, then confidence-gated escalation.**
- Trigger: single-answer task with no external check.
- Action: take a short answer, read a confidence signal, spend long reasoning only when confidence is low or two signals disagree. Log when they disagree.
- Check: three arms at equal total tokens including the gate: gate on, gate off, always deliberate.
- Evidence: d-01, d-02, d-03, d-18, a-11, a-12, c-01, b-19.
- Risk: CAR used about 45% fewer tokens, but it is a preprint on small models, was not token matched, and was worse on GSM8K Llama (71.6 vs 72.9) (d-01, d-02). Confidence measures are inconsistent across settings (d-03). Samples from one model agree with each other even when wrong (b-19). The human feeling of rightness has no direct machine twin.

**M3. Keep-or-reject step on candidates already generated.**
- Trigger: the reasoning trace contains a candidate answer that is later dropped.
- Action: list the candidates seen in the trace, then explicitly test each against the problem statement, and pick one.
- Check: final-answer accuracy vs the plain model at equal tokens, on insight-like riddles and competition math.
- Evidence: b-01, b-02, b-13.
- Risk: the extra step is itself unreliable self-review (E6). Gate it on a real check where one exists. On BrainTeaser, forced doubt cost us accuracy.

**M4. Revision only from an outside signal.**
- Trigger: a code run, a test, retrieval or a verifier returns a result.
- Action: revise from that output. Without any outside signal, do not do a reread-and-fix round.
- Check: revise-with-signal vs no revision vs reread-only at equal tokens.
- Evidence: c-14, d-05, d-07, d-08, d-09, d-19, b-09, b-10.
- Risk: no cited source is compute matched (d-19), and no code-specific equal-compute source was found. The ARC program that fit every example and was wrong shows that a weak check can mislead.

**M5. Search over alternatives for search-like tasks.**
- Trigger: a task with a state to extend, such as Game of 24 or a puzzle with partial steps, and an evaluator that can prune.
- Action: generate several next steps, score each, backtrack.
- Check: ToT-style search vs best-of-N at equal calls.
- Evidence: b-08, a-20.
- Risk: one task, many calls, snippet level. The gain over CoT may come from sheer sample count.

**M6. Decompose only when compositional.**
- Trigger: the task is harder than the worked examples and splits into ordered subquestions.
- Action: list subquestions in order, solve each, feed answers forward. A one-line plan before solving is a cheaper variant.
- Check: decomposition vs CoT vs plan-first line at equal tokens. Check d-22: this is NOT SETTLED. Only abstracts were opened and neither mentions a token-matched ablation.
- Evidence: d-13, d-14, a-20.
- Risk: the least-to-most result (99% vs 16% on SCAN) is one synthetic benchmark on an old model (d-13). Plan-and-Solve is a wording gain over zero-shot CoT (d-14).

**M7. Two rival hypotheses and the experiment that separates them.**
- Trigger: a task with a testable world, such as a program, simulation or data.
- Action: keep a hypothesis list and an experiment list. Choose the experiment that best separates the top two hypotheses.
- Check: SDDS-style loop vs plain iterate-and-fix, with a training run or a test as judge.
- Evidence: a-01, a-02, a-03, c-11.
- Risk: human samples were 20 and 10 adults, no replication and no LLM test by name (c-11, b-21). This fits our architecture-search win, but that win has no field evidence of its own.

**M8. Impasse trigger for reframing.**
- Trigger: repeated failed attempts, or attempts that disagree and no check passes.
- Action: only then relax a constraint, re-chunk, or restate the problem in a different form.
- Check: reframe-on-impasse vs never-reframe vs always-reframe at equal tokens.
- Evidence: a-04, a-05, c-20, a-06, c-09.
- Risk: insight-as-restructuring is contested. Do not add a timed "stop and incubate" step (a-15). Do not forbid thinking aloud for insight (c-06).

**M9. Counterexample hunt with code.**
- Trigger: a candidate solution that code can run against generated tests.
- Action: write inputs designed to break the candidate and run them.
- Check: caught-bug rate and final accuracy vs no hunt.
- Evidence: b-05, a-18, c-10.
- Risk: without code, models rarely build valid counterexamples (b-05). Mental-model theory gives no LLM proof that this step helps (c-10).

## 5. Evidence on LLMs and AI agents

- CoT is not a free upgrade. It helps on math and symbolic tasks (c-12) and can hurt on implicit pattern and perception tasks, by 23.1 points in the cleanest same-model case (d-11).
- Reasoning models overthink trivial items (c-16) and lose to standard models at low complexity at equal compute (c-15). The high-complexity collapse is disputed (b-12).
- Models write the right answer in the trace and then drop it (b-01, b-13).
- Self-correction needs outside feedback (c-14, d-05, d-08). Multi-agent debate did not beat self-consistency at equal response count on GSM8K with gpt-3.5: 83.2 vs 85.3 at 6 responses, 83.0 vs 88.2 at 9 (d-06, one model).
- Gating deliberation by confidence cuts tokens in some settings (d-01, d-04) but is inconsistent (d-03), and nothing here is token matched (d-18). SelfBudgeter needs training and is not a prompt-only step (d-04).
- Models copy human content effects and some biases (b-06, b-14, b-07). Written reasoning can be unfaithful (c-18).
- Planning improves with external verifiers (b-09, b-10, c-17).

## 6. What does not transfer to a model

- **Feeling of rightness.** The human signal has no machine twin. Agreement across samples and token probability are proxies, correlated within one model (b-19, d-03).
- **Trap-item base rates.** About 20% correct on designed conflict items says nothing about real tasks (a-08).
- **Time pressure and memory load.** The two-response method blocks deliberation with a deadline and load (c-01). A model has no equivalent switch. Reasoning models cannot turn reasoning off (d-11).
- **Student samples and small lab samples.** Undergraduates (a-07) and 20 and 10 adults (a-01) are weak grounds for a design rule.
- **Fluency and incubation tricks.** Failed replication in people (a-14, a-15), and there is no reason to expect them to work in a model.
- **Verbal overshadowing.** Task specific in people (c-19, c-05, c-06). The analogy to "CoT hurts" is by task type (d-10), not by mechanism.
- **Human bias patterns as a model map.** Early GPT models showed intuitive errors that later chat models mostly lost (b-15), so the bias list must be measured per model.

## 7. Open questions

1. Does sample agreement or low confidence decide when extra effort pays, at equal tokens, in one model? Partly supported, weak, and not settled (d-18). This is our central router question.
2. Does outside-signal revision beat reread-only at equal compute on code and math? Supported in direction, not compute matched (d-19).
3. Do decomposition and plan-first lines beat CoT at equal tokens? Not settled (d-22).
4. Do experts restate a problem by deep structure, and does a restate step help a model? Not settled. Chi, Feltovich and Glaser 1981 was not opened, and our plan cites it from earlier work only (d-21).
5. Are the Bago and De Neys results replicated by other labs? Not settled (d-21). d-15 and d-16 name candidate sources, but the numbers were not read.
6. Analogy and transfer from solved problems (Gentner, Holyoak), worked examples and self-explanation (Chi, Renkl), and abstention (can a model know it does not know). No evidence in this set. These bear on our lessons ledger and the abstain behavior.
7. Does a forced-divergence step have any support from this field? No. Our open-task wins have no backing here, so keep the router split.

## 8. References

Check level in brackets. Preprints are marked.

1. Klahr D, Dunbar K. 1988. Dual Space Search During Scientific Reasoning. Cognitive Science 12(1):1-48. https://dc2.philarchive.org/rec/KLADSS [snippet] (a-01, a-02)
2. Schunn CD, Klahr D. 1995. A 4-Space Model of Scientific Discovery. Cognitive Science Society proceedings. https://escholarship.org/uc/item/40q1p8f6 [snippet] (a-03, c-11)
3. Knoblich G, Ohlsson S, Haider H, Rhenius D. 1999. Constraint relaxation and chunk decomposition in insight problem solving. JEP: LMC 25:1534-1555. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf [snippet; PDF unreadable] (a-04)
4. Oellinger M, Jones G, Knoblich G. 2006. Heuristics and representational change in two-move matchstick arithmetic tasks. Advances in Cognitive Psychology. https://doaj.org/article/0984fa1657b949aa835a5950d1cd286a [snippet] (a-05)
5. Insight problem solving review (title not confirmed). 2023. Journal of Intelligence 11(5):86. https://www.mdpi.com/2079-3200/11/5/86 [snippet] (a-06)
6. De Neys W, Cromheeke S, Osman M. 2011. Biased but in doubt: conflict and decision confidence. PLoS ONE 6(1):e15954. https://pmc.ncbi.nlm.nih.gov/articles/PMC3026795 [fetched] (a-07, a-08)
7. De Neys W. 2012. Bias and conflict: A case for logical intuitions. Perspectives on Psychological Science 7:28-38. https://doi.org/10.1177/1745691611429354 [snippet] (a-09)
8. Bago B, De Neys W. 2017. Fast logic? Examining the time course assumption of dual process theory. Cognition 158:90-109. https://ideas.repec.org/p/hal/journl/hal-03510054.html and BPS summary https://bps.org.uk/research-digest/contra-kahneman-your-minds-fast-and-intuitive-system-one-capable-logic [fetched] (a-10, a-11, c-01)
9. Thompson VA, Prowse Turner JA, Pennycook G. 2011. Intuition, reason, and metacognition. Cognitive Psychology 63:107-140. https://cris.haifa.ac.il/en/publications/the-role-of-answer-fluency-and-perceptual-fluency-as-metacognitiv/ [snippet] (a-12)
10. Pennycook G, Fugelsang JA, Koehler DJ. 2015. What makes us think? A three-stage dual-process model of analytic engagement. Cognitive Psychology 80:34-72. https://uwspace.uwaterloo.ca/handle/10012/10600 [snippet] (a-13)
11. Meyer A, Frederick S, Burnham TC, et al. 2015. Disfluent fonts don't help people solve math problems. JEP: General 144(2). https://digitalcommons.georgiasouthern.edu/psych-facpubs/85 [fetched] (a-14)
12. Nieuwenstein MR, Wierenga T, Morey RD, et al. 2015. On making the right choice: a meta-analysis and large-scale replication attempt of the unconscious thought advantage. Judgment and Decision Making 10(1):1-17. https://dlab.sauder.ubc.ca/sjdm/journal/14/14321/jdm14321.html [fetched] (a-15)
13. Stanovich KE, West RF. 2008. On the relative independence of thinking biases and cognitive ability. JPSP 94:67. https://marginalrevolution.com/marginalrevolution/2009/02/papers-i-need-to-read.html [snippet, secondary page] (a-16)
14. Stanovich KE, West RF, Toplak ME. 2013. Myside bias, rational thinking, and intelligence. Current Directions in Psychological Science. https://iphils.uj.edu.pl/~a.trybus/classes/logic/cs/12.Stanovich.Myside.Bias.pdf [snippet] (a-17)
15. Khemlani S, Johnson-Laird PN. 2017. Illusions in Reasoning. Minds and Machines 27(1):11-35. https://api.philpapers.org/rec/KHEIIR [snippet] (a-18)
16. Khemlani S, Johnson-Laird PN. 2012. Theories of the syllogism: a meta-analysis. Psychological Bulletin. https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf [snippet] (c-10)
17. Newell A, Simon HA. 1972. Human Problem Solving. Prentice-Hall. https://britannica.com/science/means-ends-analysis [snippet] (a-20)
18. Kotovsky K, Hayes JR, Simon HA. 1985. Why are some problems hard? Evidence from Tower of Hanoi. Cognitive Psychology 17:248-294. https://www.cmu.edu/dietrich/psychology/pdf/kotovsky_vita.pdf [snippet; findings not read] (a-21)
19. Hagendorff T, Fabi S, Kosinski M. 2023. Human-like intuitive behavior and reasoning biases emerged in large language models but disappeared in ChatGPT. Nature Computational Science 3:833-838. https://pmc.ncbi.nlm.nih.gov/articles/PMC10766525 [snippet; a-22 memory] (a-22, b-15)
20. Mizumoto, Nguyen, Han, Li, Nakawake, Nguyen. 2025. The Metacognitive Bottleneck: Japanese Riddles Reveal Fundamental Limits of Machine Insight. arXiv 2509.14704 (preprint). https://arxiv.org/abs/2509.14704 [fetched] (b-01, b-02)
21. Liu, Geng, Wu, Sucholutsky, Lombrozo, Griffiths. 2024/2025. Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. arXiv 2410.21333 (preprint; ICML 2025 per c-13). https://arxiv.org/abs/2410.21333 [fetched] (b-03, c-13, d-10, d-11, d-12; b-04 is a secondary summary, https://papers.lunadong.com/paper/11737, snippet)
22. Sinha, Goel, Kumaraguru, Geiping, Bethge, Prabhu. 2025. Can Language Models Falsify? Evaluating Algorithmic Reasoning with Counterexample Creation. arXiv 2502.19414 (preprint). https://arxiv.org/abs/2502.19414 [fetched] (b-05)
23. Eisape, Tessler, Dasgupta, Sha, van Steenkiste, Linzen. 2024. A Systematic Comparison of Syllogistic Reasoning in Humans and Language Models. NAACL 2024. https://arxiv.org/abs/2311.00445 [fetched] (b-06, a-19)
24. Chen, Zhu, Huang, Wang. 2026. MedEinst: Benchmarking the Einstellung Effect in Medical LLMs through Counterfactual Differential Diagnosis. arXiv 2601.06636 (preprint). https://arxiv.org/abs/2601.06636 [fetched] (b-07)
25. Yao et al. 2023. Tree of Thoughts: Deliberate Problem Solving with Large Language Models. NeurIPS 2023. https://arxiv.org/pdf/2305.10601 [snippet] (b-08)
26. Valmeekam, Marquez, Sreedharan, Kambhampati. 2023. On the Planning Abilities of Large Language Models: A Critical Investigation. arXiv 2305.15771 (preprint). https://arxiv.org/abs/2305.15771 [snippet] (b-09)
27. Valmeekam et al. 2024. LLMs Still Can't Plan; Can LRMs? A Preliminary Evaluation of OpenAI's o1 on PlanBench. arXiv 2410.02162 (preprint). https://arxiv.org/pdf/2410.02162 [snippet] (b-10)
28. Shojaee, Mirzadeh, Alizadeh, Horton, Bengio, Farajtabar. 2025. The Illusion of Thinking. NeurIPS 2025 (arXiv 2506.06941). https://arxiv.org/abs/2506.06941 [fetched]; b-11 is a secondary summary at https://aiweekly.co/alerts/apple-paper-reasoning-models-collapse-past-complexity-threshold [snippet] (c-15, b-11)
29. Opus, Lawsen. 2025. The Illusion of the Illusion of Thinking. arXiv 2506.09250 (preprint, preliminary). https://arxiv.org/html/2506.09250v1 [snippet] (b-12)
30. Cuesta-Ramirez, Beaussant, Mounsif. 2025. Large Reasoning Models are not thinking straight: on the unreliability of thinking trajectories. arXiv 2507.00711, KONVENS 2025. https://arxiv.org/abs/2507.00711 [fetched] (b-13)
31. Lampinen, Dasgupta et al. 2024. Language models, like humans, show content effects on reasoning tasks. PNAS Nexus. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11250216/ [snippet] (b-14)
32. Bago B, De Neys W. 2019. The smart System 1: evidence for the intuitive nature of correct responding on the bat-and-ball problem. Thinking and Reasoning (venue not confirmed). https://www.iast.fr/fr/node/102370 [snippet] (b-16)
33. Ghasemi O, Handley S, Howarth S, Newman IR, Thompson VA. 2022. Logical intuition is not really about logic. JEP: General. https://doi.org/10.1037/xge0001179 [snippet] (b-17, d-16; b-17's first-response claim is rejected by d-17)
34. De Neys W. 2023. Advancing theorizing about fast-and-slow thinking, and reply Further advancing fast-and-slow theorizing. Behavioral and Brain Sciences 46. https://www.cambridge.org/core/product/DE3FE876FAED5DFAEF0DF92CDCDEA652 [snippet] and https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/further-advancing-fastandslow-theorizing/57847E353F098DC7325B3F7D6DFB3A1B [fetched] (b-18, c-04)
35. Black-Box Reliability Certification for AI Agents via Self-Consistency Sampling and Conformal Calibration (authors unknown). 2026. arXiv 2602.21368 (preprint). https://arxiv.org/pdf/2602.21368 [snippet] (b-19)
36. When Can We Trust LLM Graders? Calibrating Confidence for Automated Assessment (authors unknown). 2026. arXiv 2603.29559 (preprint). https://www.alphaxiv.org/abs/2603.29559 [snippet] (b-20)
37. LLM-AutoSciLab: Closed-Loop Scientific Discovery via Active Experimentation with LLMs (authors unknown). 2026. arXiv 2605.24043 (preprint). https://www.alphaxiv.org/abs/2605.24043v1 [snippet] (b-21)
38. Aha experience and insight studies (search listing, authors unknown). 2024. https://share.swps.edu.pl/handle/swps/2407 [snippet, not opened] (b-22)
39. Raoelison M, Keime E, De Neys W; Voudouri A, Bago B, et al. 2021. Think slow, then fast: does repeated deliberation boost intuitive reasoning? Judgment and Decision Making and related. https://www.iast.fr/node/102370 [snippet] (c-02)
40. Raoelison M, Thompson VA, De Neys W. 2020. The smart intuitor: cognitive capacity predicts intuitive rather than deliberate thinking. Cognition. https://doi.org/10.1016/j.cognition.2020.104381 [snippet; title, authors, DOI only] (d-15)
41. Melnikoff DE, Bargh JA. 2018. The Mythical Number Two, with replies. Trends in Cognitive Sciences. https://cse.buffalo.edu/~rapaport/575/The-Insidious-Number-Two_2018_Trends-in-Cognitive-Sciences.pdf [snippet] (c-03)
42. Schooler JW, Ohlsson S, Brooks K. 1993. Thoughts beyond words: when language overshadows insight. JEP: General. https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/schooler1993.pdf [snippet] (c-05)
43. Gilhooly KJ, Fioratou E, Henretty N. 2010. Verbalization and problem solving: insight and spatial factors. British Journal of Psychology 101(1):81-93. https://uhra.herts.ac.uk/id/eprint/2391 [snippet] (c-06)
44. Macchi et al. 2025. Verbalization and insight problem solving. Journal of Intelligence. https://www.boa.unimib.it/retrieve/faef22bd-9e10-4dfc-b28b-385f976aa963/Macchi-2025-J.%20Intell.-VoR.pdf [snippet; HTTP 403, not opened] (c-07)
45. Salmon-Mordekovich N, Leikin R. 2023. Insight problem solving is not that special, but business is not quite 'as usual'. Psychological Research 87(6):1995-2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC10366031 [fetched] (c-08)
46. Tracing Cognitive Processes in Insight Problem Solving: Using GAMs and Change Point Analysis (authors unknown). 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10219327/ [snippet] (c-09)
47. Sprague Z, Yin F, Rodriguez JD, Jiang D, Wadhwa M, Singh P, et al. 2025. To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. ICLR 2025. https://arxiv.org/abs/2409.12183 [fetched] (c-12)
48. Huang J, Chen X, Mishra S, Zheng HS, Yu AW, Song X, Zhou D. 2024. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024. https://arxiv.org/abs/2310.01798 [fetched] (c-14, d-05, d-06, d-07)
49. Chen X, Xu J, Liang T, He Z, Pang J, Yu D, Song L, et al. 2024. Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. arXiv 2412.21187 (preprint). https://arxiv.org/abs/2412.21187 [fetched] (c-16)
50. Stechly K, Valmeekam K, Kambhampati S. 2024. Chain of Thoughtlessness? An Analysis of CoT in Planning. arXiv 2405.04776 (preprint; later NeurIPS). https://arxiv.org/abs/2405.04776 [fetched] (c-17)
51. Turpin M, Michael J, Perez E, Bowman SR. 2023. Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023. https://arxiv.org/abs/2305.04388 [fetched] (c-18)
52. Alogna VK et al. 2014. Registered Replication Report: Schooler and Engstler-Schooler (1990). Perspectives on Psychological Science. https://pubmed.ncbi.nlm.nih.gov/26186759 [snippet] (c-19)
53. Jones G (2003); Oellinger M, Jones G, Danek AH, Knoblich G (2013). Testing two cognitive theories of insight; Cognitive mechanisms of insight. JEP: LMC. https://irep.ntu.ac.uk/18103/ [snippet] (c-20)
54. Lu, Yu, Xu, Ran, Tang, Wang, Shan, Fu, Feng, Tang, Wang, Huang. 2025. Prolonged Reasoning Is Not All You Need: Certainty-Based Adaptive Routing for Efficient LLM/MLLM Reasoning. arXiv 2505.15154 (preprint). https://arxiv.org/html/2505.15154v1 [fetched] (d-01, d-02)
55. Lewis-Lim, Tan, Zhao, Aletras. 2025. Can Confidence Estimates Decide When Chain-of-Thought Is Necessary for LLMs? arXiv 2510.21007 (preprint). https://arxiv.org/abs/2510.21007 [abstract] (d-03)
56. Li, Dong, Ma, Zhang, Jia, Sui. 2025. SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning. arXiv 2505.11274 (preprint). https://arxiv.org/abs/2505.11274 [abstract] (d-04)
57. Gou, Shao, Gong, Shen, Yang, Duan, Chen. 2023. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing. ICLR 2024 (arXiv 2305.11738). https://arxiv.org/html/2305.11738 [fetched] (d-08, d-09)
58. Zhou, Schaerli, Hou, Wei, Scales, Wang, Schuurmans, et al. 2022. Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. ICLR 2023 (arXiv 2205.10625). https://arxiv.org/abs/2205.10625 [abstract] (d-13)
59. Wang, Xu, Lan, Hu, Lan, Lee, Lim. 2023. Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models. ACL 2023 (arXiv 2305.04091). https://arxiv.org/abs/2305.04091 [abstract] (d-14)
