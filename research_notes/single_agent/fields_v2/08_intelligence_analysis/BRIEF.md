# Intelligence analysis and structured analytic techniques: what it offers one thinking agent

Evidence ids point to the evidence_*.jsonl files in this folder. Where evidence_d CHECK lines disagree with claims.jsonl, the CHECK lines are used. One warning first: nearly all the human tests of these techniques come from one author group (Mandel, Karvetski, Dhami), with small samples and simple tasks. "Established" below means several papers, not several labs (intel-d-09, intel-a-14).

## 1. What the field studies

Intelligence analysis studies how analysts weigh uncertain evidence and name the most likely explanation. Its toolkit is called structured analytic techniques (SATs). The best known is Analysis of Competing Hypotheses (ACH). The analyst lists rival hypotheses, lists evidence, marks which evidence fits which hypothesis, ignores evidence that fits all of them, and prefers the hypothesis with the fewest inconsistencies (intel-a-01, intel-a-02). Heuer also warns not to treat an unproven hypothesis as disproved (intel-a-03) and advises a check on linchpin assumptions (intel-a-06). Other techniques are devil's advocacy, key assumptions check, pre-mortem and red team. The field also runs forecasting tournaments, which measure accuracy directly (intel-a-21).

For our agent the interesting point is that this field has tested its own methods, and the results are sober.

## 2. Established findings

**E1. Full ACH gave human analysts no accuracy gain.** In a randomized trial of 50 UK analysts, ACH-trained analysts were not more accurate than controls. Mean absolute error was 0.26 for ACH and 0.21 for control, with random guessing at 0.33 (intel-a-07, intel-a-08, ia-b-01, ia-c-02). A second paper, probably on the same analyst pool, found ACH users did not complete all the steps, bias results were mixed, and ACH may raise inconsistency and error (intel-a-10, ia-b-05, ia-c-09). With 227 online participants, ACH gave no coherence advantage (intel-a-11, ia-c-06). A further experiment found ACH and a factorized Bayes method did not improve accuracy (intel-a-13, intel-d-05). A critical review of 7 articles and 6 experiments concluded ACH as a whole gives little or no benefit (intel-a-14, preprint). Effects are small and mostly p > .05. This is "no gain", not proven harm. Mandel 2018 and Dhami 2019 are not fully independent.

**E2. Repairing probabilities in code beats the technique.** Analysts' probabilities over four exclusive hypotheses summed to 1.77 (ACH) and 1.54 (control) instead of 1.0 (ia-b-02, ia-c-03). Forcing them to sum to 1 cut error about 35% (0.23 to 0.15). Averaging all 50 analysts after that cut it about 61% (to 0.09) (intel-a-09, ia-b-03, ia-c-04, intel-d-04). Plain normalization alone reached 0.13, nearly as good as the fancier repair (ia-b-03). After repair, ACH and control were equal at 0.15 (ia-c-02). Coherence gains from brief training and from aggregation recur in other work (intel-a-20, intel-a-13). All of this is human data on one task. The number of judges needed for most of the gain is unverified (intel-d-10), so the figure "about 3" must not be hard-coded.

**E3. The SAT tradition has not validated itself.** Tradecraft norms are loosely grounded in judgment science and never validity-tested. Warnings against one bias can create the mirror-image bias (intel-a-18, intel-a-22). A RAND review says the community promotes the techniques but has made little effort to measure them (ia-c-10, snippet only). This overlaps in authorship with E1, so it is not fully independent.

**E4. People and LLMs both prefer confirming tests.** Heuer reports the human effect, citing Wason's 2-4-6 task (intel-a-05). Eleven LLMs show the same on a hidden-rule task, and counterexample prompting raised rule discovery from 42% to 56% (intel-a-24, ia-b-09, ia-c-11, preprint). The gain was on a task where tests return feedback.

**E5. Self-critique without an external signal is weak.** Intrinsic self-correction struggles and can lower accuracy (ia-c-12). Models fail mainly at locating errors, and correct well when told where the error is (ia-c-13). They also struggle to spot fallacious steps (ia-c-14). All are preprints or one benchmark.

**E6. Debate does not reliably beat voting.** Debate is not reliably better than self-consistency (ia-c-15). Multi-agent gains on popular benchmarks are often minimal (ia-c-16). Correlated errors reinforce consensus mistakes (ia-b-15). Voting improved reasoning tasks by 13.2% and consensus improved knowledge tasks by 2.8% across seven protocols (ia-b-17). Mostly preprints.

**E7. Models conform and flatter.** All tested LLMs conform to majority answers, more so when uncertain (ia-b-18). Five assistants show sycophancy, so a critic can be pulled toward the stated answer (ia-c-17). Both are preprints.

**E8. Aggregation and calibration work in forecasting.** In a human tournament, training, teaming and tracking improved calibration and resolution, and training taught reference classes and averaging (intel-a-21). LLM assistants raised human forecast accuracy by 24 to 28% in a preregistered study of 991 people (ia-b-13, preprint). An LLM system with search, a reconciling supervisor and statistical calibration matched human superforecasters on ForecastBench (ia-b-14, preprint).

## 3. Single-source and contested findings

### Single-source

- **Diagnosticity training did not carry through.** ACH-trained analysts rated cue usefulness far better (r = .68 vs .17), but final accuracy did not improve (ia-b-04, ia-c-05).
- **Pseudo-diagnostic weighting.** Only ACH users let non-diagnostic evidence move their ratings, at about 30% of the effect of fully diagnostic evidence (ia-b-07, ia-c-07). Both groups were also too conservative (ia-c-08).
- **Layout.** Hypotheses in rows cut confirmation bias; the standard columns layout and plain text did not (N = 161, p = .009, phi = .24) (intel-d-01, intel-d-09). Layout did not change credibility sensitivity (intel-d-03). Among 62 Dutch analysts and cadets, 66% used a balanced strategy unaided (intel-d-02). So the effect is small, on one task, and may be a student effect.
- **ACH did not change adversarial allegiance** in a mock expert witness study of 159 people (intel-a-17, abstract only).
- **Real analysts were underconfident.** In 1,514 real forecasts, discrimination was good and the main error was underconfidence, helped by recalibration (intel-a-19, abstract).
- **Minority answers.** About one in four divergent debate cases had the right answer held by the minority (ia-b-16, preprint).
- **Heuer's logic** (evidence that fits all hypotheses has no diagnostic value) is sound but rests on one book (intel-a-01). Heuer also cites a medical study where extra data collection did not raise accuracy (intel-a-04, second-hand).

### Contested

- **Does ACH harm?** The direction is consistent (p = .051, d = 0.20 on reliability; coherence loss in one study; error gap p = .14) but significance is weak (ia-b-06, intel-a-12, ia-c-06, intel-a-13, ia-c-02).
- **Devil's advocate in LLMs.** For: anticipatory reflection gave +3.5 points on WebArena (ia-b-20) and a 48-person study found higher group satisfaction (ia-b-19, satisfaction, not accuracy). Against: ia-c-12, ia-c-17, and our own BrainTeaser drop to about 75% under forced doubt (00_PLAN.md). A 1990 meta-analysis of devil's advocacy in human groups exists, but nobody could open its effect sizes (intel-a-26, ia-b-21, intel-d-08). Treat as unresolved.
- **Drop voting for minorities?** The one-in-four figure (ia-b-16) argues against pure voting. E6 says voting is still the baseline to beat.

## 4. Mechanisms an agent can run

Equal-token test for every mechanism: run the plain model with the same total tokens (the same number of natural samples plus a vote) on the same items, and keep the mechanism only if it wins. The field gives hypotheses, not results, for LLMs (intel-d-07).

**M1. Coherence repair of any probability vector.**
- Trigger: the agent outputs probabilities or confidences over exclusive options.
- Action: normalize to sum to 1 in code. No extra model call.
- Check: Brier or log score against the plain, unnormalized output on the same items. It costs zero tokens, so only quality is compared.
- Evidence: intel-a-09, ia-b-03, ia-c-03, ia-c-04, intel-a-20.
- Risk: very low. Does nothing for single-answer tasks. Human data only.

**M2. Small varied-panel average.**
- Trigger: the agent must give a probability or ranking, and the probe shows attempts disagree.
- Action: several independent calls with differently worded prompts, each normalized (M1), then averaged in code.
- Check: against the same number of identical-prompt samples with a vote. Also plot error against panel size on our tasks and choose the size from that curve, because the "about 3" figure is unverified (intel-d-10).
- Evidence: ia-c-04, intel-a-21, ia-b-14, ia-b-13.
- Risk: samples from one model are correlated, so the gain will be smaller than the 61% in humans (ia-b-15). On single-answer tasks, averaging adds nothing over the first natural answer.

**M3. Diagnosticity filter.**
- Trigger: the agent weighs a list of facts or clues against two or more rival answers.
- Action: ask for each clue, per rival, "consistent / inconsistent / neutral". Code drops clues that are consistent with all rivals before any scoring.
- Check: agreement with ground truth when clues are scored with and without the filter, at equal tokens.
- Evidence: intel-a-01, ia-b-07, ia-c-07.
- Risk: the labels are model judgments with no external check (ia-c-12). Humans trained to rate cue usefulness still did not improve the end result (ia-b-04), so the filter could be a good sub-skill that changes nothing.

**M4. Counterexample test, only with feedback.**
- Trigger: a hypothesis can be tested by running something (code, an example, a rule probe) and the result comes back.
- Action: ask for the test whose failure would refute the leading hypothesis, not one it already fits. Run it. Revise from the real result.
- Check: rule-discovery or pass rate against plain test choice at equal calls.
- Evidence: intel-a-05, intel-a-24, ia-c-11, ia-c-13.
- Risk: without an oracle this becomes self-critique (ia-c-12). Keep it behind a real check.

**M5. Live-but-unproven tag.**
- Trigger: the agent is about to discard a rival answer.
- Action: discard only on a positive contradiction, not because support is missing. Otherwise keep it tagged live.
- Check: how often the final answer was a rival that the plain run discarded early.
- Evidence: intel-a-03.
- Risk: single-source, from a book. Can keep a task open longer than needed and burn tokens on single-answer items, where our data show the first answer is usually right (00_PLAN.md).

**M6. ACH-lite at a split (test, do not assume).**
- Trigger: the probe splits (attempts disagree) and no executable check exists.
- Action: build a rows layout, hypotheses as rows and evidence in columns. A model labels each cell. Code counts inconsistencies per hypothesis, after the M3 filter. Pick the fewest inconsistencies, with M1 normalization on any scores.
- Check: against a vote of the same total tokens on split items only. Also log run-to-run consistency, since ACH was slightly less reliable in people (ia-c-06). Kill rule: drop it if consistency or accuracy falls.
- Evidence: intel-a-02, intel-d-01, ia-c-06, ia-c-08.
- Risk: the human trials say full ACH gives no gain (E1). The only reason to expect more is that code never skips steps (intel-a-10), which is untested. Do not run it by default.

**M7. Key assumptions check at an impasse.**
- Trigger: attempts disagree and M4 has no oracle.
- Action: list assumptions behind the leading answer, negate each unverified one, and see whether the answer survives.
- Check: against a plain resample at equal tokens.
- Evidence: intel-a-06 (practice from a book). No controlled study was found (intel-d-11).
- Risk: pure practice, no evidence of benefit. Same self-critique problem as ia-c-12.

**M8. Confidence recalibration.**
- Trigger: the agent reports a confidence or a probability to a user or a router.
- Action: map raw confidence through a curve fitted on the agent's own past outcomes.
- Check: calibration error against raw output on held-out items.
- Evidence: intel-a-19, intel-a-21, ia-b-14.
- Risk: the curve is fitted to our tasks. Real analysts were underconfident (intel-a-19), while LLMs may be over- or underconfident, so the direction may differ. Not tested for LLMs here.

## 5. Evidence on LLMs and AI agents

- The LLM evidence is thin and mostly preprints, often checked at abstract level (intel-d-06, ia-b-13, ia-b-14).
- No paper was found that tests a full ACH matrix against a plain baseline at equal tokens. An arXiv search for "analysis of competing hypotheses" AND LLM returned only AgentCDM, and one for "structured analytic techniques" returned zero (intel-d-07, ia-b-22). This is thin evidence of absence from one search tool.
- AgentCDM is ACH-inspired and reports state-of-the-art results, but the abstract has no numbers, and it trains the model, so it is not a prompt-only test (intel-a-25, intel-d-06). Treat as zero.
- SIA, an evidence-first troubleshooting agent with competing hypotheses, was tested on 303 threads, but no usable numbers were read (ia-b-11). A GPT-4 multi-agent diagnosis study went from 0/80 to 57/80 on simulated cases with no human baseline and no equal-token control (ia-b-12). Neither counts.
- Positive but indirect: counterexample prompting (ia-c-11), forecasting aggregation with calibration (ia-b-14), LLM assistance for human forecasters (ia-b-13).
- Negative or cautionary: weak self-correction (ia-c-12, ia-c-13), debate versus voting (ia-c-15, ia-b-15), conformity and sycophancy (ia-b-18, ia-c-17).
- Our own data point the same way as the cautionary side. Forced doubt and divergence helped on open tasks and hurt on single-answer tasks (00_PLAN.md: NoveltyBench 3.18 to 9.63 distinct; architecture search 7% lower perplexity; ARC 4/10 vs 2/8; BrainTeaser about 92% vs about 75%). Intelligence work is mostly open-ended explanation under uncertainty, which is the regime where doubt tends to pay. This is our own reading, not a finding of the field.
- A correction to an earlier brief: arXiv 2609.00738 is BASIN, a history-biased search paper, not an ACH or hypothesis-structuring paper, and the "89% hypothesis structuring" claim could not be found. Drop both (ia-b-10).

## 6. What does not transfer to a model

- **Training analysts.** The ACH trials test a trained human. A model needs no training and has no habits to retrain (intel-a-07).
- **Skipped steps.** Humans skipped ACH steps (intel-a-10). A program does not, so the human null may not predict the program result. This is a hypothesis, not a result.
- **Team structure.** Red teams, devil's advocate roles and group satisfaction (ia-b-19) assume independent minds. Samples from one model are correlated (ia-b-15), and a model critic drifts toward the stated answer (ia-c-17).
- **Mirror-image bias warnings.** The claim that correcting one bias creates its opposite (intel-a-18) is about human judgment. For an agent it is a reason to measure, not a rule.
- **Underconfidence.** The real-analyst finding (intel-a-19) is a human trait.
- **Credibility and deception.** Source credibility ratings and adversarial inputs were not covered, and the layout benefit did not extend to credibility sensitivity (intel-d-03).
- **Popularity as evidence.** Wide use of SATs says nothing about whether they work (ia-c-10).

## 7. Open questions

1. Does an ACH-like matrix, counted by code, beat a vote of equal tokens on LLM tasks with several rival answers? This is the central gap (intel-d-07).
2. How many varied judges give most of the aggregation gain, for LLMs? The human figure is unverified (intel-d-10).
3. Does the probe's agreement signal predict when M3 and M6 help, so a router can switch them on only at a split? Base rates of first-answer-right by task type are not yet measured (00_PLAN.md).
4. Do pre-mortem, key assumptions check and red team help at all? No controlled study was found, and search budget ran out before this could be settled (intel-d-11).
5. What are the effect sizes in Schwenk 1990, and does devil's advocacy help when an external check exists? (intel-d-08, intel-a-26)
6. Does coherence-averaging of LLM probabilities lower Brier score? Not settled (intel-d-11).
7. Does the rows-layout benefit appear in LLMs, and is it only a student effect? (intel-d-01, intel-d-02)
8. Does turning verbal probability words into numbers matter for how the agent reports confidence? It was not searched (intel-d-11).

## 8. References

Check level in brackets.

1. Heuer RJ Jr. 1999. Psychology of Intelligence Analysis. CIA Center for the Study of Intelligence. https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf [fetched; a book, not data]
2. Mandel DR, Karvetski CW, Dhami MK. 2018. Boosting intelligence analysts' judgment accuracy: What works, what fails? Judgment and Decision Making 13(6), 607-621. https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html [fetched by two agents; the Crossref record was abstract only]
3. Dhami MK, Belton IK, Mandel DR. 2019. The "Analysis of Competing Hypotheses" in intelligence analysis. Applied Cognitive Psychology 33(6), 1080. https://strathprints.strath.ac.uk/69049/ [fetched by one agent, abstract in others]
4. Karvetski CW, Mandel DR. 2020. Coherence of probability judgments from uncertain evidence: does ACH help? Judgment and Decision Making 15(6). https://dlab.sauder.ubc.ca/sjdm/journal/20/200430/jdm200430.html [fetched]
5. Karvetski CW, Mandel DR, Irwin D. 2020. Improving probability judgment in intelligence analysis: from structured analysis to statistical aggregation. Risk Analysis 40(5), 1040-1057. https://doi.org/10.1111/risa.13443 [abstract]
6. Dhami MK, Mandel DR et al. 2019. Improving Probability Judgment in Intelligence Analysis: From Structured Analysis to Statistical Aggregation. PsyArXiv preprint. https://doi.org/10.31234/osf.io/fb9ej [abstract; preprint]
7. Wilcox J, Mandel DR. 2023. Critical review of ACH experiments. PsyArXiv preprint. https://doi.org/10.31234/osf.io/an32t [abstract; preprint]
8. Dhami MK, Belton IK, De Werd P. 2024. Effects of task structure and confirmation bias in alternative hypotheses evaluation. Cognitive Research: Principles and Implications. https://pmc.ncbi.nlm.nih.gov/articles/PMC11169332/ [fetched]
9. Otzipka J, Volbert R. 2026. ACH and adversarial allegiance in mock expert witnesses. PLoS One 21(4), e0346891. https://doi.org/10.1371/journal.pone.0346891 [abstract]
10. Mandel DR, Tetlock PE. 2018. Correcting judgment correctives in national security intelligence. Frontiers in Psychology 9, 2640. https://doi.org/10.3389/fpsyg.2018.02640 [abstract]
11. Mandel DR, Irwin D. 2022. Critique of the structured-analytic-technique approach. PsyArXiv preprint. https://doi.org/10.31234/osf.io/7hx2c [abstract; preprint]
12. Artner S, Girven R, Bruce J. 2016. Assessing the value of structured analytic techniques in the U.S. intelligence community. RAND RR1408. https://www.rand.org/pubs/research_reports/RR1408.html [snippet; direct fetch returned 403]
13. Whitesmith M. 2020. Cognitive Bias in Intelligence Analysis: Testing the Analysis of Competing Hypotheses Method. Edinburgh University Press. https://doi.org/10.3366/edinburgh/9781474466349.001.0001 [snippet]
14. Mandel DR, Barnes A. 2014. Accuracy of forecasts in strategic intelligence. PNAS 111(30), 10984-10989. https://doi.org/10.1073/pnas.1406138111 [abstract]
15. Mandel DR. 2015. Instruction in information structuring improves Bayesian judgment in intelligence analysts. Frontiers in Psychology 6, 387. https://doi.org/10.3389/fpsyg.2015.00387 [abstract]
16. Mellers B, Ungar L, Baron J et al. 2014. Psychological strategies for winning a geopolitical forecasting tournament. Psychological Science 25(5), 1106-1115. https://doi.org/10.1177/0956797614524255 [abstract]
17. Schwenk CR. 1990. Effects of devil's advocacy and dialectical inquiry on decision making: a meta-analysis. OBHDP 47(1), 161-176. https://ideas.repec.org/a/eee/jobhdp/v47y1990i1p161-176.html [record only; effect sizes not read; memory]
18. Jhaveri AR, GX-Chen A, Sucholutsky I, Choi Y. 2026. Confirmation bias in LLMs on a Wason 2-4-6 style task. arXiv 2604.02485. https://arxiv.org/abs/2604.02485 [fetched; preprint]
19. Huang J, Chen X, Mishra S, Zheng HS, Yu AW, Song X, Zhou D. 2023. Large language models cannot self-correct reasoning yet. arXiv 2310.01798. https://arxiv.org/abs/2310.01798 [abstract; preprint]
20. Tyen G, Mansoor H, Cărbune V, Chen P, Mak T. 2024. LLMs cannot find reasoning errors, but can correct them given the error location. ACL Findings; arXiv 2311.08516. https://arxiv.org/abs/2311.08516 [abstract]
21. Hong R, Zhang H, Pang X, Yu D, Zhang C. 2023. A closer look at the self-verification abilities of LLMs in logical reasoning. arXiv 2311.07954. https://arxiv.org/abs/2311.07954 [abstract; preprint]
22. Smit A, Duckworth P, Grinsztajn N et al. 2023. Should we be going MAD? arXiv 2311.17371. https://arxiv.org/abs/2311.17371 [abstract; preprint]
23. Cemri M et al. 2025. Why do multi-agent LLM systems fail? arXiv 2503.13657. https://arxiv.org/abs/2503.13657 [abstract; preprint]
24. Liu et al. 2026. AceMAD, peer prediction for debate. arXiv 2603.06801. https://arxiv.org/abs/2603.06801 [abstract; preprint]
25. He et al. 2026. Minority answers in multi-agent debate. arXiv 2606.29270. https://arxiv.org/abs/2606.29270 [abstract; preprint]
26. Kaesberg L, Becker J, Wahle JP et al. 2025. Voting or consensus? Decision protocols in multi-agent debate. arXiv 2502.19130. https://arxiv.org/abs/2502.19130 [abstract; preprint]
27. Zhu et al. 2024. Conformity in large language models. arXiv 2410.12428. https://arxiv.org/abs/2410.12428 [abstract; preprint]
28. Sharma M et al. 2023. Towards understanding sycophancy in language models. arXiv 2310.13548. https://arxiv.org/abs/2310.13548 [abstract; preprint]
29. Lee, Hwang, Kim, Lee. 2025. LLM devil's advocate in group decisions. arXiv 2503.14263. https://arxiv.org/abs/2503.14263 [abstract; preprint]
30. Wang, Li, Deng, Roth, Li. 2024. Anticipatory reflection in web agents. arXiv 2405.16334. https://arxiv.org/abs/2405.16334 [abstract; preprint]
31. Schoenegger P, Park PS, Karger E et al. 2024. LLM assistants and human forecasting accuracy. arXiv 2402.07862. https://arxiv.org/abs/2402.07862 [abstract; preprint]
32. Alur et al. 2025. LLM forecasting system matching superforecasters on ForecastBench. arXiv 2511.07678. https://arxiv.org/abs/2511.07678 [abstract; preprint]
33. Zhao X, Zhao S, Yu H, Zhang L et al. 2025. AgentCDM. arXiv 2508.11995. https://arxiv.org/abs/2508.11995 [abstract; preprint]
34. Marozzo, Lio. 2026. SIA evidence-first troubleshooting agent. arXiv 2606.13220. https://arxiv.org/abs/2606.13220 [abstract; preprint]
35. Ke et al. 2024. Multi-agent conversations for bias-caused misdiagnosis. arXiv 2401.14589. https://arxiv.org/abs/2401.14589 [abstract; preprint]
36. Cheng L. 2026. Escaping reasoning basin collapse with history-biased search (BASIN). arXiv 2609.00738. https://arxiv.org/abs/2609.00738 [abstract; preprint]
37. arXiv API queries, 2026-10-20, for "analysis of competing hypotheses" AND LLM and for "structured analytic techniques". http://export.arxiv.org/api/query?search_query=all:%22analysis+of+competing+hypotheses%22+AND+all:LLM [fetched]
