# Correlated errors: when does agreement among samples from one model signal correctness?

*2026-10-20. Gap brief. Marks: [V] source opened this session; [M] from memory or search snippet only, re-check before use. "Abstract-level" means [V] on the abstract page only, not the full paper. Several 2026 papers below are preprints, single-author or workshop papers. Treat each as one data point.*

## 1. What the field studies

Self-consistency, semantic entropy and "stop when attempts agree" all assume that independent samples make independent mistakes. Then agreement is evidence. Samples from one model are not independent. They share training data, framing habits and blind spots. The question is how much of the agreement is real evidence and how much is the model repeating itself. The field is ensemble theory (error correlation sets the value of a vote), plus LLM calibration and uncertainty work. Our design uses probe agreement as a machine version of feeling of rightness. It drives the router, the early stop, the extremized vote, the calibration table and the trust gate. This brief tests that signal.

## 2. Core findings

**F1. Agreement is positive but weak evidence, and it is conditional. Strength: moderate, several 2026 audits agree, all preprints.**
- A 53-runner audit with about 265,000 samples on GPQA Diamond and AIME found rho between agreement and correctness of 0.20 to 0.59. On GPQA, agreement of 0.8 or more held on 77% of entries, and 48% of those majority answers were wrong. It is useful for unsaturated mid-tier models and for deciding where to spend compute. For the most consistent frontier model it was overconfident and no more accurate. A cross-check on three Claude tiers showed the same. Abstract-level, single author (arXiv 2607.08065) [V].
- Another paper splits agreement into a part explained by a per-question answer preference and a residual. Its own conclusion: agreement is "graded evidence, not certification." GPT-4.1 on GPQA and AIME, plus five open models (arXiv 2608.18795) [V, abstract-level].
- Farquhar et al. 2024 (Nature, semantic entropy): the Oxford authors' own page says it will not catch cases where the model "has been trained into an incorrect style of reasoning or set of facts." That is the "consistent errors" limit. The page does not use that phrase, so quote it as written, not as "misses consistent errors." [V, blog page, not the Nature text; the Nature page was paywalled]. The 0.79 vs 0.69 AUROC figure was in a search snippet only [M].

**F2. By task type, the sign of the problem differs.**
- Puzzle with a checker: agreement matters only through the checker. Our ARC run was fooled twice by a program that fit all examples [ours]. In code, Reflexion's own table shows the same trap. Tests written by the same model passed wrong code: false-positive rate 16.3% on MBPP Python vs 1.4% on HumanEval Python, and Reflexion went from 80% to 77% on MBPP Python while it went from 80% to 91% on HumanEval (GPT-4) [V, full text read]. AlphaCode-style clustering by outputs also has a known trap: trivial programs ("return 0", "return None") form one large wrong cluster, which CodeT reported when it replicated the clustering [V, search snippet of CodeT page, treat as M].
- Multiple choice: agreement is bought cheaply because the answer space is tiny. Wrong options attract the same samples. The 48% wrong-at-high-agreement figure on GPQA above is the best number we have [V, abstract-level]. On two small non-reasoning models (Qwen2.5-7B, Llama-3-8B) on GPQA Diamond with 64 samples, majority vote lowered accuracy on 56.6% and 65.7% of individual problems, while the aggregate barely moved (0.342 to 0.369; 0.273 to 0.313). Dissenting samples were as confident as agreeing ones (median margin about 20.5 nats). Gates based on agreement or token entropy did not capture the 14 to 17 point oracle headroom. Single author, workshop paper, no reasoning models tested (arXiv 2608.11403) [V, via summary page].
- Open tasks: no ground truth, so agreement cannot be scored. A 25x-cost polling study on five truthfulness benchmarks found no consistent gain over one sample and "amplified shared misconceptions." It also found models predict other models' answers better than they identify truth, and that confidence weighting does not help (arXiv 2603.06612) [V, abstract-level, models not named].

**F3. Prompt-level diversity inside one model mostly does not pay. Strength: weak to moderate, one strong negative result.**
- On AIMO 3 (50 olympiad problems, 3 models, 23+ experiments), assigning different reasoning strategies to voters failed in every setup. The author says high-temperature sampling already decorrelates errors, and weaker strategies lose more accuracy than they remove correlation. Best majority vote 42/50 vs pass@20 about 45.5 (arXiv 2603.27844) [V, abstract-level]. This matches our four-strategy loss (92% to 75%) [ours].
- A study of six open models in coding consensus found neither temperature nor persona pairing gave robust accuracy gains, and single agents matched or beat consensus in most conditions (arXiv 2507.11198) [V, search snippet, treat as M].
- Cross-model voting does decorrelate on math. An "LLM jury" paper reports it beats self-consistency on seven benchmarks and closes the gap to an oracle on competition math, with a shared-error floor near zero on math and "non-trivial on science" (arXiv 2607.10139) [V, abstract-level, single author, models and token cost not on the page]. Against that, a truthfulness study finds cross-model errors strongly correlated too (2603.06612 above). Reconcile: cross-model helps where the task has crisp answers and models differ in training; it fails where all models share a misconception.
- Forecasting: a 2026 workshop paper finds the strongest frontier models give tightly correlated predictions and that a second draw from one model adds only a fraction of the information of a draw from a diverse model. The best 5-unit allocation used four different models. 113 questions, 3 samples per model, no confidence intervals (arXiv 2606.29661) [V, abstract-level].

**F4. Fixation on a first wrong frame is real, but the evidence on small and reasoning models is thin.**
- Only Connect Wall (NeurIPS 2023): GPT-4 got 239 correct groups (0-shot) vs 1,405 for humans on the original set. With red herrings diluted GPT-4 rose to 595 (peak 655 at 5-shot). With red herrings removed (WordNet variant) it reached 1,926 groups at 0-shot. So the red herring is a large cause, not the only one. More in-context examples did not reliably help grouping (arXiv 2306.11167) [V, from full text]. Models: GPT-3.5 and GPT-4 only. No reasoning models, no Claude.
- MedEinst (5,383 paired cases, 49 diseases, 17 models): control accuracy 6.5% to 54.3%; Bias Trap Rate (right on the control, same wrong label on the trap) 33.8% to 66.1% for baselines. Gemini-2.5-Pro 60.9%, GPT-5 51.9%, Claude-Sonnet-4.5 43.0%, Qwen3-14B 54.2% vs Qwen3-235B 43.3%. The paper says no meaningful link between size and robustness. It does not compare reasoning vs non-reasoning, and it tests no sampling or voting. Baselines are zero-shot CoT (arXiv 2601.06636) [V, from HTML Table 1]. Implication: a trap is a case where all samples agree on the shortcut. Agreement cannot detect it by construction. Only the control/trap pairing exposes it.
- Gema et al. 2025 (TMLR): longer reasoning lowers accuracy on tasks with distractors, spurious features and constraint tracking. Claude Opus 4 fell from near 100% to about 85 to 90% on misleading-math as reasoning budget grew. o3 was stable there. DeepSeek R1 under natural overthinking fell from about 70% to 30% with five distractors. Claude models get more distracted, o-series overfit to the framing. Most exact numbers are in figures, not text (arXiv 2507.14417) [V, partly read]. It reports no majority-vote result. So "inverse scaling" shows that more thinking within one sample can lock a wrong frame in. It does not show that voting fails on those tasks.
- Sequential vs parallel at equal tokens conflicts: parallel thinking with majority vote beat extended thinking by up to 20% at a 16K budget on o1/R1-class models (arXiv 2506.04210, NeurIPS 2025) [V, abstract]. A different paper reports sequential chains that build on earlier attempts beat parallel self-consistency in 95.6% of configurations on five open models (arXiv 2511.02309) [M, search snippet]. Different setups; unsettled. Neither tests a Claude extended-thinking API.
- Self-consistency gets weaker as models improve: 0.4% gain on HotpotQA and 1.6% on MATH-500 over 20 samples with Gemini 2.5 models, and declines at high sample counts. Mostly HotpotQA and MATH, not our tasks (arXiv 2511.00751) [V, abstract-level].

**F5. Early stopping on agreement is validated only where errors are scattered.** Adaptive-Consistency cut samples up to 7.9x with under 0.1% average drop over 17 datasets and three LLMs (EMNLP 2023) [V, search snippet]. ESC (arXiv 2401.10480) stops only when a whole window agrees [V, snippet]. Neither study asks about unanimous but wrong answers. The base models are older. So the savings are real on tasks the model usually gets right, and silent on the case we care about.

## 3. Mechanisms an agent can run

**M1. Agreement is a prior, never a verdict.**
- Trigger: end of the 4-5 attempt probe.
- Action: write agreement as one number, but route on it only inside a task class where a calibration table exists. If no table exists for the class, treat agreement as "unknown" and do not early-stop on it alone.
- Check: for each class, plot P(correct | k of 5 agree) from our logs. Early stop is allowed only where the lower bound of P(correct | unanimous) beats single-attempt accuracy by a set margin. Equal tokens vs plain best-of-N with the same checker.
- Evidence: F1 (moderate).
- Risk: classes with few items give noisy tables. On our easy ARC-1 items both arms already stop early, so the table may show no gain there.

**M2. Stop only on a check, not on agreement.**
- Trigger: any task with a checker (examples, tests, a run).
- Action: "two attempts agree" ends the run only if both pass the check AND the check includes something the program was not fitted to: held-out example, a symmetry test, or a model-independent test. Agreement without a pass routes to REVISE or ESCALATE.
- Check: count wrong stops (stopped, then wrong) per 100 items, plus tokens saved. Compare to "stop on first pass."
- Evidence: Reflexion false positives, our ARC double fooling, CodeT/AlphaCode cluster trap (F2).
- Risk: costs held-out checks; on tasks with only a few examples there is nothing to hold out.

**M3. Group by behaviour on fresh inputs, then discount trivial clusters.**
- Trigger: candidate programs exist (ARC, code).
- Action: run all candidates on generated new inputs, cluster by output, down-weight any cluster that gives constant, empty or identity outputs, and prefer clusters whose outputs also pass symmetry/invariance checks.
- Check: selector accuracy on offline replay of stored candidates at zero extra model tokens (we already did this: symmetry-first 34/36 vs vote 33/36 [ours]).
- Evidence: execution-based grouping decorrelates because it compares behaviour, not text (F2). No Haiku-class test beyond ours.
- Risk: the model generating the test inputs shares the blind spot, so use rule-based input mutations, not model-written ones.

**M4. Change the question, not the voter, when cheap diversity is wanted.**
- Trigger: multiple choice or no-checker single-answer task, when the probe is unanimous but the item is flagged as trap-prone (many near options, a famous shortcut).
- Action: one extra call with shuffled option order and the option labels renamed, plus one "state the evidence that would separate your answer from the nearest rival" call. Do not assign personas.
- Check: flip rate under shuffling vs accuracy: an answer that survives the shuffle should be more often right than one that does not. Measure the gap on BrainTeaser.
- Evidence: weak. The option-shuffling literature was not found this session [M, unsearched]. Persona and strategy diversity failed (F3).
- Risk: costs tokens, and BrainTeaser shows forced doubt hurts. Run it only on unanimous-but-flagged items, never by default.

**M5. Use a different model for the one tie-break call.**
- Trigger: probe disagrees or a checker-less answer carries high cost.
- Action: one call to a different model family, accepted only if it matches one of the probe answers. Never let it add a new answer.
- Check: wins vs a second sample from the same model at the same token cost.
- Evidence: cross-model decorrelation on math (2607.10139) vs correlated truthfulness errors (2603.06612). Mixed.
- Risk: breaks the "one LLM" rule of this phase. List as an optional arm, not part of the one-agent claim.

**M6. Do not extremize a same-model vote.**
- Trigger: any plan to push a vote share toward 0 or 1.
- Action: keep raw vote fractions. If a probability is needed, map it through the measured calibration table (M1), not through a fixed extremizing exponent.
- Check: Brier score or log loss on our logs: raw vs table vs extremized, by class.
- Evidence: extremizing helps when voters are diverse and under-confident (AIA Forecaster report, 2026, via snippet) [M]. For same-model samples, the effective count falls fast with correlation (a paper gives 8 attempts as about 2.6 independent votes at mean pairwise correlation 0.3, arXiv 2603.27844 [M, from search summary, not found on the abstract page]). Extremizing then amplifies a shared bias.
- Risk: calibration tables from small samples overfit.

**M7. Run an ablation of the probe against the model's own thinking budget.**
- Trigger: before shipping the router.
- Action: three arms at equal total tokens: (a) 1 attempt with extended thinking at the full budget; (b) probe of 4-5 plain attempts with the router; (c) 4-5 attempts each with a small thinking budget. Same checker, same items.
- Check: accuracy at equal tokens per suite, plus the wrong-stop rate. The router earns its place only if (b) or (c) beats (a) on at least one gated suite and does not lose on BrainTeaser by more than 1 point.
- Evidence: none direct. This is the gap (section 4).
- Risk: the answer may be that thinking alone matches the router, which removes its reason to exist on single-answer tasks. Keep it only for the diverge route and for revision from real check output.

## 4. Evidence on LLMs and AI agents

What is solid: (1) Same-model agreement carries some signal, weak and regime-dependent (2607.08065, 2608.18795). (2) It can hide systematic error: Reflexion's false-positive tests [V, full text]; MedEinst trap rates [V]; Only Connect red herrings [V]. (3) Prompt-level diversity within a model rarely beats plain high-temperature sampling (2603.27844, one competition). (4) Behaviour-based checks beat text agreement when a checker exists [ours + CodeT].

What is abstract-level only: every 2026 audit above (single-author or workshop papers; models often unnamed), the jury result, the forecasting diversity result, the sequential-vs-parallel conflict.

What is missing, and this is the gap:
- No study found tests agreement as a stop rule or router on Claude Haiku-class models at equal tokens.
- Almost none uses built-in extended thinking. The Gema paper uses it on Claude but not with voting. The Cao et al. metacognitive harness uses Claude Sonnet 4.6 (see section 6) but does not report token cost on its abstract page.
- None combines small models with checker-less single-answer tasks and a reasoning mode.
- I found no source testing whether native thinking already does the job of a probe. Engineering inference only: a thinking model samples several lines of attack inside one trace, so a probe of K traces may repeat the same internal frame more than K plain samples would. Not tested.

**Verdict for our 4-5 attempt probe.**
1. As a difficulty prior, keep it. Cost is small and the signal is positive on average.
2. As a stop rule, do not stop on agreement alone. Stop on agreement plus a check the program was not fitted to (M2). On tasks without a checker, agreement may stop early only after a per-class table shows it pays (M1).
3. As an extremizer input, drop it for one model (M6).
4. As a trust gate, unanimity does not mean trust. On GPQA-like items 48% of strongly agreeing majority answers were wrong in one audit.
5. The router's value over native thinking is unproven. Run M7 before building more on it.

## 5. What does not transfer, and where it could hurt

- Human feeling of rightness is a meta-memory signal tied to retrieval fluency. A sample count is not fluency. Treat the analogy as a design metaphor.
- Wisdom-of-crowds results assume independent people. One model is one person asked five times.
- Human extremizing results come from teams with different information. Same-model samples share all information.
- Hurts: (a) early stop on unanimous wrong answers (easy-looking traps); (b) persona or strategy voters lose per-attempt accuracy (our 92% to 75%); (c) forced-doubt calls on unanimous answers cost accuracy when the first answer was right; (d) extra thinking can make distractor tasks worse (Gema).

## 6. Checks of earlier claims

**07 F9 and F5 (Reflexion, Self-Consistency).** Reflexion: verified. Base model is GPT-4. HumanEval Python pass@1 80.1 to 91.0 [V, full text]. AlfWorld: ReAct + Reflexion solved 130 of 134 tasks over 12 trials; the AlfWorld agent was prompted with the few-shot ReAct examples "with GPT-3," so the base is a GPT-3-family model [V, full text]; ReAct baseline 108/134 comes from a secondary source [M]. Important caveat for the "revise from real outputs" rule: Reflexion's coding feedback is self-generated unit tests, not real hidden tests. On MBPP Python it was worse than the GPT-4 baseline (80% to 77%) because of 16.3% false-positive passes [V]. So this paper supports "revise from real feedback" only when the feedback is trustworthy, and it is a warning for the self-written-test case. Verdict: keep, but cite the MBPP result next to it. Self-Consistency: abstract gains over CoT are GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-challenge +3.9 [V]. Models are not named on the abstract page; I recall PaLM-540B, GPT-3 and others [M]. "Several to 17 points" is accurate to the abstract. Both used 2022-2023 models without reasoning budgets. Later work shows the gain shrinks on modern models (2511.00751 [V, abstract]).

**06 section 4 (monitor-control harness, arXiv 2605.14186).** Verified identity: "LLMs Know When They Know, but Do Not Act on It: A Metacognitive Harness for Test-time Scaling" (Cao et al.). Fixed Claude Sonnet-4.6, no fine-tuning, pooled accuracy 48.3 to 56.9 across text, code and multimodal benchmarks, authors' own claim. The abstract page gives no token cost and no per-benchmark equal-compute comparison [V, abstract]. Verdict: do not count as support for the router. It shows a harness can be built; it does not show a gain at equal tokens against plain best-of-N.

**03 finding 1, M4/M7 and M5.** The training/teaming gain: the 2014 randomized trial found a one-hour training module (base rates, reference classes, bias awareness) helped [V, via summary]. I did not find a 2025 reanalysis that weakens it. What I found is a 2024 reanalysis (Hauenstein et al., Psychological Science) claiming tournament gaming (choosing easy questions, forecasting late) inflated apparent skill, and a Mellers adversarial-collaboration response [V, snippet]. Verdict: the "2025 reanalysis" label is unverified, rename it "2024 reanalysis, disputed." M4/M7 remain correlational [M]. M5 (extremize a vote) conflicts with same-model dependence: see M6 above. Verdict: drop M5 for one model.

**01 F2 and F3 (Elstein 1978).** Book confirmed (Harvard University Press) [V, catalog]. I could not confirm "3 to 5 hypotheses." A secondary review says about 5 to 7, and that later hypotheses cost more to generate so clinicians settle on early ones [V, snippet, Spanish-language source, weak]. Elstein's group also reports hypothesis-generation instructions had no effect on outcome in a 1973 dissertation [V, snippet]. Verdict: downgrade "strong" to [M]; the number is unclear. F3's "fast is not worse holds even more for models" is not supported: MedEinst shows models fall into shortcut diagnoses [V], and agreement cannot flag them. Keep M1 (add outside candidates) only with a strict trigger.

**02 F6 (devil's advocacy).** Schweiger, Sandberg and Ragan 1986 (AMJ 29(1)) and Schwenk's 1990 meta-analysis (OBHDP 47(1)) exist [V, citation lists]. I could not retrieve effect sizes. A 1989 study found devil's advocacy and dialectical inquiry groups beat consensus groups, with no difference between them [V, snippet]. These are group studies, not single agents. Verdict: keep "moderate for groups, unknown for one agent." The internal contradiction stands. Use only with a strict trigger, because forced doubt lost accuracy in our BrainTeaser data [ours].

**06 F4/F5/F7, M8 (productive failure, self-explanation).** Productive failure: Sinha and Kapur 2021 (Rev. Educ. Res.) is a meta-analysis of 53 studies and 166 comparisons; the "twice / up to three times a good teacher" phrasing is the authors' own words in a press article; I did not get the pooled g [V, snippet]. Self-explanation: Bisra et al. 2018 overall g = .55 over 69 effect sizes from 64 reports [V, abstract]. The sub-effects g 0.87 and 0.19 were not checked. Verdict: self-explanation has an overall effect on humans, productive failure is a human learning effect; neither is tested on LLMs, so M5/M8 stay unproven proposals.

**07 F11/F12 (Self-Discover, step-back).** Self-Discover: up to 32% over CoT, beats CoT-SC by over 20%, with 10 to 40x less inference compute; models GPT-4 and PaLM 2 [V, abstract]. Step-back: gains on MMLU Physics and Chemistry of 7% and 11%, MuSiQue 7%; TimeQA 27% on arXiv/ICLR vs 34% on a DeepMind page, so quote 27% [V, snippet]. I found no replication on small models or saturated-benchmark audit. Verdict: one lab, older large models, no equal-token test against a thinking model. Does not outweigh our 92% to 75% loss. Keep M5 (strategy choice) as a per-class experiment only.

**05 F5 and 04 F6 (pre-mortem, Einstellung).** The "30%" comes from Klein's summary of Mitchell, Russo and Pennington 1989 (J. Behav. Decis. Making 2(1):25-38); the original abstract covers design, not the result, and the metric is plausible reasons generated, not correctness [V, snippet]. Verdict: confirm that the 30% is a reasons-generated metric. Einstellung effect sizes in humans were not checked this session [M]. For LLMs, red herrings and MedEinst show a fixation effect in a single-pass setup [V]. Neither tests a forced-rival step. Verdict: the problem is real; the fix is unproven and, per our data, hurts without a strict trigger.

## 7. Open questions

1. How correlated are 5 plain Haiku attempts on our own suites? Measure directly: mean pairwise error correlation per class, and the effective vote count.
2. Does native extended thinking lower or raise that correlation versus plain sampling at high temperature?
3. Does a per-class calibration table of P(correct | agreement) transfer across tasks, or must it be rebuilt per suite?
4. Does a trap detector based on paired controls (as MedEinst does) have a cheap analogue, such as asking the same item with one fact altered?
5. Does a different model for one tie-break call pay at equal tokens on single-answer tasks?
6. How often does a program that fits every example still fail held-out inputs, and which checks catch it (symmetry, mutations)?

## 8. References

1. Farquhar, Kossen, Kuhn, Gal. Detecting hallucinations in large language models using semantic entropy. Nature 2024. DOI 10.1038/s41586-024-07421-0. Limits quote: https://oatml.cs.ox.ac.uk/blog/2024/06/19/detecting_hallucinations_2024.html [V blog]
2. Ding. When LLMs Agree, Are They Right? arXiv 2607.08065. https://arxiv.org/abs/2607.08065 [V abstract]
3. Zhang et al. Decomposing Wrong-Consensus Agreement in LLM Self-Consistency. arXiv 2608.18795. https://arxiv.org/abs/2608.18795 [V abstract]
4. Bahuguna. When Self-Consistency Backfires. arXiv 2608.11403. https://www.alphaxiv.org/abs/2608.11403 [V summary page]
5. Denisov-Blanch et al. Consensus is Not Verification. arXiv 2603.06612. https://arxiv.org/abs/2603.06612 [V abstract]
6. Nitarach. Model Capability Dominates (AIMO 3). arXiv 2603.27844. https://arxiv.org/abs/2603.27844 [V abstract]
7. Liu. LLMs as a Jury. arXiv 2607.10139. https://arxiv.org/abs/2607.10139 [V abstract]
8. Aitchison et al. Diversity is the Strength of the AI Crowd. arXiv 2606.29661. https://www.alphaxiv.org/abs/2606.29661 [V abstract]
9. Naeini et al. LLMs are Fixated by Red Herrings (Only Connect Wall). arXiv 2306.11167. https://arxiv.org/abs/2306.11167 [V]
10. Chen et al. MedEinst. arXiv 2601.06636, ACL 2026. https://arxiv.org/abs/2601.06636 [V]
11. Gema et al. Inverse Scaling in Test-Time Compute. arXiv 2507.14417, TMLR. https://arxiv.org/abs/2507.14417 [V, partly]
12. Does Thinking More Always Help? arXiv 2506.04210. https://arxiv.org/abs/2506.04210 [V abstract]
13. Sharma and Chopra. The Sequential Edge. arXiv 2511.02309. https://arxiv.org/abs/2511.02309 [M snippet]
14. Self-Consistency Is Losing Its Edge. arXiv 2511.00751. https://arxiv.org/abs/2511.00751 [V abstract]
15. Aggarwal et al. Adaptive-Consistency, EMNLP 2023 [M snippet]. Early-Stopping Self-Consistency, arXiv 2401.10480 [M snippet]
16. Chen et al. CodeT. arXiv 2207.10397 [M snippet]. Li et al. AlphaCode, Science 2022 [M]
17. Shinn et al. Reflexion. arXiv 2303.11366. https://arxiv.org/abs/2303.11366 [V full text]
18. Wang et al. Self-Consistency. arXiv 2203.11171. https://arxiv.org/abs/2203.11171 [V abstract]
19. Cao et al. A Metacognitive Harness for Test-time Scaling. arXiv 2605.14186. https://arxiv.org/abs/2605.14186 [V abstract]
20. Zhou et al. Self-Discover. arXiv 2402.03620. https://arxiv.org/abs/2402.03620 [V abstract]. Zheng et al. Step-Back Prompting. arXiv 2310.06117 [M snippet]
21. Bisra et al. Inducing Self-Explanation: a Meta-Analysis. Educ. Psychol. Rev. 30(3), 2018 [V abstract via snippet]. Sinha and Kapur. Rev. Educ. Res. 2021, DOI 10.3102/00346543211019105 [V snippet]
22. Mitchell, Russo, Pennington. Back to the future. J. Behav. Decis. Making 2(1), 1989 [V citation]. Elstein, Shulman, Sprafka. Medical Problem Solving. Harvard UP 1978 [V catalog]
23. Schweiger, Sandberg, Ragan. AMJ 29(1) 1986. Schwenk. OBHDP 47(1) 1990 [V citations only]
24. Hauenstein et al. 2024 reanalysis of Good Judgment Project and Mellers response (Mack Institute page) https://mackinstitute.wharton.upenn.edu/?p=34033 [V snippet]. AIA Forecaster Technical Report, arXiv 2511.07678 [M snippet]
