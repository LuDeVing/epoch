# Innovation studies: what it offers one thinking agent

Evidence ids are written in short form: a-01 means innov-a-01, b-01 means innovation-b-01, c-01 means innov-c-01, d-01 means innovation-d-01. Where a d-file CHECK line disagrees with the earlier claims file, the CHECK line is used here. Most LLM evidence is preprints. Many human-side sources were only seen as snippets or recalled from memory, and each section says so.

## 1. What the field studies

Innovation studies asks where new and useful things come from and why most attempts fail. Its tools are large citation and patent datasets, lab experiments on idea generation, and models of search. Most of it is about science and firms, not about single minds (a-01, a-09, a-13). Its newest branch tests LLMs as idea generators and as judges of ideas (b-01, b-03). That branch bears most directly on our agent. The field studies open problems only. It says almost nothing about single-answer tasks, which is where our schemas lost (d-09).

## 2. Established findings

Status "established" means at least two independent sources agree. Most of these are preprints, so treat effect sizes as soft.

**E1. Novel combinations widen the spread of outcomes.** Distant recombination lowers the average result and raises the variance, so both failures and breakthroughs come from unfamiliar search. Fleming found lower average usefulness but higher variance for new component combinations in patents (a-09, c-16). Wang, Veugelers and Stephan found that papers with many first-time journal combinations get 12.04% more citations and 14.90% higher citation dispersion (a-05, b-21). Their odds of landing in the top 10% were 16.80% higher and in the bottom 10% were 16.76% higher (a-06). Foster, Rzhetsky and Evans report that innovative links are published less often but are better cited when they are (a-11, snippet only). The outcome in all three is citations, so this is about science, not answers.

**E2. Samples from one LLM, and across LLMs, are too alike.** Generating 4000 ideas per topic left about 200 unique ones, about 5% (b-02). LLM answers to creativity tests are much more similar to each other than human answers are, across many models (b-08, c-05). One model repeats itself and different models give strikingly similar open-ended outputs (b-09). A feedback-tuned model cut diversity across writers, while the base model did not (c-06). Aligned models have lower token entropy and cluster tightly (c-07). In a randomised trial, GPT-4 story ideas raised novelty by 5.4% (one idea) to 8.1% (five ideas) and usefulness by 3.7% to 9.0%, yet stories became more similar to each other (b-06, c-20; one study, counted once). Users of ChatGPT produced less distinct ideas than users of another tool (b-07). This matches our own fact that samples from one model are correlated.

**E3. LLM judges are weak selectors of ideas.** The best Claude pairwise ranker agreed with human review ranking 53.3% of the time and GPT-4o 45.0%, against 56.1% between two human reviewers (b-03). LLM judges rate model-written research questions as highly novel while experts prefer reference questions (b-11). Real future citations and acceptance correlated negatively with LLM-judged novelty (rho -0.29) (b-12). LLM raters preferred AI answers on the Alternate Uses Task, but the bias vanished once idea elaboration was controlled (b-13). Judges also align less with humans when humans disagree among themselves (b-09). Self-evaluation failed in the original study (c-01).

**E4. LLM novelty claims are inflated.** The AI Scientist system misclassified established concepts as new, and 42% of its experiments failed from coding errors (c-03). A considerable fraction of LLM research documents were smart plagiarism that detectors missed (c-04). With E3 (b-11, b-12) this makes four independent signals that LLM-judged novelty is not trustworthy.

**E5. A single draw rarely reaches the top, but many draws plus selection do.** Across 14 LLMs only 0.28% of responses reached the top 10% of human creativity benchmarks, yet the same model and prompt ranged from below average to original (b-10). Professional authors scored about 66% higher than LLM text on a creativity index (c-08). On functional-fixedness problems GPT-4 scored 62.4% single-try and 92.3% best-of-many (b-20). Best-of-many only pays if a working selector exists, which E3 questions.

**E6. LLMs explore and exploit poorly alone, so the program should keep the books.** All tested LLMs did worse than linear regression on bandits, though they are useful for proposing candidates in large semantic action spaces (b-18). Most LLMs struggle to explore a hidden state space, and do better with more reasoning ability (b-19). Only GPT-4 with chain of thought and an externally summarised history explored well (c-09). Thinking-enabled models mix random and directed exploration like humans but adapt worse when the environment changes (b-17). These are bandit and hidden-state tasks, so the step to idea search is by analogy.

**E7. Self-correction without outside feedback does not help.** Without external feedback LLM self-correction struggles and sometimes lowers performance (c-10). Assistants show sycophancy, so a critic prompted by the user's idea tends to agree (c-11). On a rule-constrained open task, eight frontier models gained little from self-critique and repeated the same violations (d-08, preprint). Self-correction is more useful in open-ended generation than in multiple-choice selection, which is limited by the options given (d-07, preprint).

**E8. Measures of breakthrough are not clean.** The reported decline in the disruption index is partly a database artefact (c-12, preprint). A literature review finds disruption indices inconsistent, time-biased and data-biased (c-13). This matters only for how much weight to give team-level innovation results.

**E9. Analogical retrieval and literature grounding move ideas toward real later work.** Retrieving concepts across abstraction levels and recombining them raised similarity to later real research by about 7-10% (b-14). Scideator users reported more creativity support (b-15). Retrieval-augmented generation scored 2.5 times higher on real impact in a time-split test (b-12). Idea-Catalyst reports novelty up 21% and insightfulness up 16%, though the abstract does not say who judged (d-10). All preprints, all weak proxies. A d-file check found no controlled study with human or execution outcomes (d-12).

**E10. Generate alone, then pool, beats interacting brainstorm groups.** Mullen et al. (c-18) and Girotra et al. (c-19) were recorded from memory and not opened. Treat this as provisional. It is a team result. Its use for one model is only the design point that draws should be independent and selection a separate step.

## 3. Single-source and contested findings

**Single-source.**
- Conventional core plus a small tail of unusual pairs gives the highest impact. The hit rate was 9.11 per 100 against a background of 5 (a-01). Low conventionality with high tail novelty scored 5.33, near background, and low on both scored 2.05 (a-02). About 40% of papers have some unusual tail pairs (a-03). This is one study cited several times (b-22, c-14). The d-file check found no replication in patents, software or LLM ideas that tests the conventional-core part (d-18). Yu and Romero found unusual dataset pairings linked to higher impact in 30,000+ papers, but without a core test (d-17, preprint). Keep as a hypothesis.
- The LLM novelty edge vanishes after execution. Blind reviewers rated LLM ideas more novel than expert ideas (5.64 vs 4.84) and slightly less feasible (6.34 vs 6.61) (b-01). After 43 experts executed ideas, the AI novelty edge disappeared (5.78 vs 4.91 before, 4.73 vs 4.90 after) and AI ideas lost about 1.05 novelty points and 1.98 overall points (b-04, b-05, c-02, d-01). Reviewers found flaws only once results were visible (b-05). It is an ICLR 2026 poster (d-02). The d check found no independent replication, but its search budget ran out, so absence is not proven (d-03). Hypothesis.
- Novel work is recognised late. Novel papers are less likely to be top-cited in a short window and sit in lower-impact journals (a-07), but are more often top 1% in the long run (b-21, c-15). One research group, counted once.
- People reject creative ideas under uncertainty, so rate novelty and usefulness separately (c-17, memory only, human raters).
- Escalation of commitment is a robust costly error, from one meta-analysis (a-19). Human result, no LLM test.
- Organisations under-invest in exploration (a-13, snippet), and a 2018 review asks for individual-level evidence (a-14, snippet).
- Problem finding predicts better creative work, from one art-student study (a-15, a-16, snippets).
- Rewarding Bayesian surprise found 5-29% more LLM-surprising discoveries (b-16). Surprise is measured by LLM beliefs.
- Divergent-then-convergent prompting with a feasibility reflection step raised efficient solutions (b-20).
- Refining a diversity-selected subset of ideas (MMR-k) gave the best proxy tradeoff and fewest duplicates, with random-k a strong cheap baseline (d-04, preprint, proxy only).
- Prize winners make more innovative moves (a-12, snippet from press coverage).
- Teams insert more novel combinations than solo authors, 37.7% more (a-04). Weak for one agent.

**Contested.**
- Small teams disrupt (a-17, a-18, snippets). Lin, Li and Wu defend it with controls and note small-team impact may take a decade (d-14). Petersen et al. find the effect weak and positive at 8 or more authors (d-15). Huang and Xie find disruption rising with team size once reference length is handled (d-13). All preprints. Verdict: contested, not refuted, not a design rule (d-16).

## 4. Mechanisms an agent can run

Each mechanism is a program-run step. The equal-token test means: give the plain model the same total tokens (for example the same number of plain samples, then its own pick) and compare on the same items.

**M1. Task gate.**
- Trigger: first call, before any schema step.
- Action: classify the task as open-ended (many valid answers, an external or later check exists) or single-answer (first natural answer usually right). Only open tasks enter M2 to M7.
- Check: gate-on versus always-on versus plain at equal tokens on a mixed set of open and single-answer items.
- Evidence: d-09, d-07, d-08, c-10.
- Risk: a wrong gate puts a single-answer task into divergence, which cost us ARC (direct attempt 56% right, divergent cards 12-31%) and word puzzles (92% to 75%). The literature only partly reconciles the tension with our open-task wins (d-09), so this is a hypothesis.

**M2. Independent draws with program-side dedup.**
- Trigger: gate says open.
- Action: make N separate calls, none seeing the others, with varied framing. The program, not the model, removes near-duplicates by embedding similarity.
- Check: equal tokens versus N plain samples; count distinct clusters and expert or executed quality, not distinctness alone.
- Evidence: b-02, b-08, b-09, c-05, c-06, c-18, c-19.
- Risk: our NoveltyBench win (3.18 to 9.63 distinct) has no quality measure beside it, and novelty without a conventional base did not pay in citations (a-02). Dedup cannot fix a pool that lacks good ideas.

**M3. Selection that is not the generator's opinion.**
- Trigger: after M2, when there is more than one candidate.
- Action: rank by an external check where one exists (run, test, retrieval, execution). Where none exists, use a separate judge call with elaboration length controlled, and treat its ranking as weak. Keep a diverse top set rather than one pick when possible.
- Check: pick by M3 versus random pick versus pick by the generating model, at equal tokens.
- Evidence: b-03, b-11, b-12, b-13, c-01, c-11, d-04.
- Risk: judges near chance add cost and noise (b-03). A humor pipeline with best-of-N, critique and judging tied a plain baseline (d-05). Selection may add nothing on strong models.

**M4. Cheap execution before ranking.**
- Trigger: a candidate can be run, simulated or tested at small cost.
- Action: run a minimal version of each top candidate and rank on the result. Our architecture-search win used a training run as judge.
- Check: rank-by-opinion versus rank-by-run at equal tokens including the run cost.
- Evidence: b-04, b-05, d-03 (the flip is a hypothesis), c-10, d-04.
- Risk: execution costs tokens or compute, and many answers have no runnable check. Si 2025 used human experts, not cheap runs (b-04).

**M5. Program-run exploration ledger.**
- Trigger: any search over many options across calls.
- Action: the program stores what was tried, the outcome and a summary. Each new call receives the summary and a forced list of untried regions. The model only proposes.
- Check: ledger versus no ledger at equal tokens on the same search task.
- Evidence: b-18, c-09, b-19, b-17.
- Risk: the evidence is bandits and hidden states, not idea search (E6). The ledger adds prompt tokens every call and could narrow the search.

**M6. Conventional core with a small distant tail.**
- Trigger: open task, after the gate.
- Action: build most candidates by ordinary near-neighbour moves and reserve one or two slots for ideas built from a distant-field analogy found by retrieval.
- Check: core-only versus core-plus-tail versus all-distant, at equal tokens, scored by execution or expert quality.
- Evidence: a-01, a-02, a-09, a-05, b-14, b-15, d-10, d-12, d-18.
- Risk: the core-plus-tail rule is single-source and about citations (d-18). Distant-analogy quality has no controlled test (d-12). The tail raises variance (E1), so a bad tail wastes tokens. The ratio is a design choice to tune.

**M7. Score novelty and usefulness separately, with a prior-art check.**
- Trigger: before accepting an idea as new.
- Action: score novelty and usefulness on two scales with length controlled. Retrieve prior work for each finalist and reject rewrites of it.
- Check: finalists with the check versus without, against an expert or later-outcome label.
- Evidence: c-17, c-03, c-04, b-11, b-12, b-13.
- Risk: c-17 is from memory and about human raters. A prior-art step can wrongly kill a real novelty and adds tokens.

**M8. Stop rules set in advance.**
- Trigger: every branch kept alive across more than one round.
- Action: before the round, write the evidence that would kill the branch. The program applies it and does not let the model argue the branch back.
- Check: pre-set kill rule versus model-chosen stopping, at equal tokens.
- Evidence: a-19, a-07 (do not kill on a short-horizon score alone).
- Risk: a-19 is a human result. Early kills clash with the pattern that novel work looks weak early (a-07, b-21). Manage with a reserve slot.

## 5. Evidence on LLMs and AI agents

- Ideas: LLM ideas looked more novel on paper (b-01) and the edge disappeared after execution (b-05, single source, d-03).
- Diversity: single-model sampling collapses (b-02, b-09) and alignment makes it worse (c-06, c-07).
- Judging: LLM judges are near chance and inflate novelty (b-03, b-11, b-12).
- Search: LLMs explore poorly alone (b-18, b-19, c-09).
- Correction: self-correction without feedback fails (c-10), critics are sycophantic (c-11), and reflection did not fix rule violations on a constrained open task (d-08).
- Creative puzzles: models often recall the right fact but fail the non-obvious connection (d-11, benchmark abstract only).
- Scaffolding: a best-of-N, critique and judging pipeline tied a plain frontier baseline on humor (d-05, one task).
- Gap: no source gives a curve for how many ideas to generate before returns fall, with an external selector (d-06). Only Tian's single point (b-20) and our own runs can set N.

## 6. What does not transfer to a model

- Team results: small-team disruption (a-17), team novelty insertion (a-04) and brainstorm group loss (c-18, c-19). One model's personas are correlated samples (b-08), so a team analogy is weak. Only the structure carries over: independent generation, then a separate selection.
- Citation outcomes (a-05, a-06) measure what a community rewarded years later, not whether a thought was good (b-12).
- Organisation-level explore versus exploit budgets (a-13, a-14) are about resources over years. The agent version would be a token budget, which is a design choice and not evidence.
- Escalation of commitment (a-19) is driven by sunk cost and ego. Whether a model shows it is untested here.
- Delayed recognition (a-07) cannot help an agent that is scored at once, except as a reason to keep a reserve slot.

## 7. Open questions

- When not to diverge. The field studies open problems only (d-09). Our gate has to be tested (M1).
- How many ideas to generate and how to prune. No curve exists (d-06).
- Whether always-doubt and always-diverge help only when the task rewards change. The reconciliation is partial (d-09, d-07).
- Whether the conventional-core mix works for LLM ideas. No replication (d-18).
- Whether the execution flip replicates. Single team (d-03).
- Whether distant-analogy retrieval helps when judged by outcomes, not LLM raters (d-12).
- Whether a lessons ledger across runs helps. It is only inferred from Fleming, where combination familiarity raised expected citations about 10-11% (a-10).
- Open-ended agent work beyond ideation, such as design and code architecture, has no counterpart in this field's evidence (d-06).

## 8. References

Checked means how we know the source: fetched (page opened), abstract, snippet (search result only) or memory. Ids are the evidence lines that cite each source.

1. Uzzi, Mukherjee, Stringer, Jones (2013). Atypical combinations and scientific impact. Science 342:468-472. https://www.kellogg.northwestern.edu/faculty/jones-ben/htm/atypical_combinations_and_scientific_impact.pdf. Checked: fetched/memory/snippet. Ids: a-01, a-02, a-03, a-04, b-22, c-14.
2. Wang, Veugelers, Stephan (2016). Bias against novelty in science (working paper; later Research Policy 2017). NBER WP 22180. https://www.nber.org/papers/w22180.pdf. Checked: fetched. Ids: a-05, a-06, a-07, a-08.
3. Fleming (2001). Recombinant uncertainty in technological search. Management Science 47(1):117-132. https://funginstitute.berkeley.edu/wp-content/uploads/2012/10/Recombinant-Uncertainty-in-Technological-Search.pdf. Checked: fetched/memory. Ids: a-09, a-10, c-16.
4. Foster, Rzhetsky, Evans (2015). Tradition and innovation in scientists' research strategies. American Sociological Review 80(5):875-908. https://www.sciencedaily.com/releases/2015/10/151009155546.htm. Checked: snippet. Ids: a-11, a-12.
5. March (1991). Exploration and exploitation in organizational learning. Organization Science 2(1):71-87. https://acawiki.org/Exploration_and_exploitation_in_organizational_learning. Checked: snippet. Ids: a-13.
6. Wilden, Hohberger, Devinney, Lavie (2018). Revisiting James March (1991): whither exploration and exploitation?. Strategic Organization 16(3):352-369. https://researchers.mq.edu.au/en/publications/revisiting-james-march-1991-whither-exploration-and-exploitation/. Checked: snippet. Ids: a-14.
7. Getzels, Csikszentmihalyi (1976). The creative vision: a longitudinal study of problem finding in art. Book, Wiley. https://edcircuit.com/important-overlooked-aspect-of-creativity/. Checked: snippet. Ids: a-15.
8. Getzels, Csikszentmihalyi (as reviewed by Perkins) (1976). The creative vision. Book. https://libcat.library.tamu.edu/Record/in00000601483. Checked: snippet. Ids: a-16.
9. Wu, Wang, Evans (2019). Large teams develop and small teams disrupt science and technology. Nature 566:378-382. https://sonic.northwestern.edu/large-teams-develop-and-small-teams-disrupt-science-and-technology. Checked: snippet. Ids: a-17, a-18.
10. Sleesman, Conlon, McNamara, Miles (2012). Cleaning up the Big Muddy: a meta-analytic review of the determinants of escalation of commitment. Academy of Management Journal 55(3):541-562. https://Www.Gwern.net/doc/psychology/cognitive-bias/sunk-cost/2012-sleesman.pdf. Checked: fetched. Ids: a-19.
11. Si, Yang, Hashimoto (2024). Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers. arXiv 2409.04109 (ICLR 2025 poster). https://arxiv.org/abs/2409.04109. Checked: fetched. Ids: b-01, b-02, b-03, c-01.
12. Si, Hashimoto, Yang (2025). The Ideation-Execution Gap: Execution Outcomes of LLM-Generated versus Human Research Ideas. arXiv 2506.20803 (preprint). https://arxiv.org/abs/2506.20803. Checked: fetched. Ids: b-04, c-02, d-01.
13. Si et al. (2025). The Ideation-Execution Gap. arXiv 2506.20803 (preprint). https://arxiv.org/html/2506.20803. Checked: fetched/snippet. Ids: b-05, d-02.
14. Doshi, Hauser (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances 10(28) eadn5290. https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532/. Checked: fetched/memory. Ids: b-06, c-20.
15. Anderson, Shah, Kreminski (2024). Homogenization Effects of Large Language Models on Human Creative Ideation. arXiv 2402.01536 (C&C 2024). https://arxiv.org/abs/2402.01536. Checked: fetched. Ids: b-07.
16. Wenger, Kenett (2025). We're Different, We're the Same: Creative Homogeneity Across LLMs. arXiv 2501.19361 (preprint). https://arxiv.org/abs/2501.19361. Checked: fetched. Ids: b-08, c-05.
17. Jiang, Chai, Li, Liu, Fok, Dziri, Tsvetkov, Sap, Albalak, Choi (2025). Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond). arXiv 2510.22954 (preprint). https://arxiv.org/abs/2510.22954. Checked: fetched. Ids: b-09.
18. Haase, Hanel, Pokutta (2025). Has the Creativity of Large-Language Models peaked?. arXiv 2504.12320 (preprint). https://arxiv.org/abs/2504.12320. Checked: fetched. Ids: b-10.
19. not captured on page (2026). RQ-Bench: On the Limits of LLM-as-Judge for Scientific Novelty Assessment. arXiv 2606.12071 (preprint, June 2026). https://arxiv.org/abs/2606.12071. Checked: fetched. Ids: b-11.
20. not captured on page (2026). HindSight: Evaluating LLM-Generated Research Ideas via Future Impact. arXiv 2603.15164 (preprint). https://arxiv.org/abs/2603.15164. Checked: fetched. Ids: b-12.
21. Domanti, Mock, Agnoli, De Angeli (2026). The Effect of Idea Elaboration on the Automatic Assessment of Idea Originality. arXiv 2604.20569 (preprint). https://arxiv.org/abs/2604.20569. Checked: fetched. Ids: b-13.
22. Gu, Wang, Zhang, Li (2024). LLMs can realize combinatorial creativity: generating creative ideas via LLMs for scientific research. arXiv 2412.14141 (preprint). https://arxiv.org/abs/2412.14141. Checked: fetched. Ids: b-14.
23. Radensky, Shahid, Fok, Siangliulue, Hope, Weld (2024). Scideator: Human-LLM Scientific Idea Generation Grounded in Research-Paper Facet Recombination. arXiv 2409.14634 (preprint). https://arxiv.org/abs/2409.14634. Checked: fetched. Ids: b-15.
24. Agarwal et al. (author list not captured) (2025). AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise. arXiv 2507.00310, NeurIPS 2025. https://arxiv.org/abs/2507.00310. Checked: fetched. Ids: b-16.
25. author list not captured (2025). LLMs vs humans vs bandit algorithms on the exploration-exploitation tradeoff. arXiv 2505.09901 (preprint). https://arxiv.org/abs/2505.09901. Checked: fetched. Ids: b-17.
26. Harris, Slivkins (2025). Should You Use Your Large Language Model to Explore or Exploit?. arXiv 2502.00225, UAI 2026. https://arxiv.org/abs/2502.00225. Checked: fetched. Ids: b-18.
27. author list not captured (2025). Disentangling Exploration of Large Language Models by Optimal Exploitation. arXiv 2501.08925 (preprint). https://arxiv.org/abs/2501.08925. Checked: fetched. Ids: b-19.
28. Tian et al. (2024). MacGyver: Are Large Language Models Creative Problem Solvers?. NAACL 2024 (arXiv 2311.09682). https://arxiv.org/abs/2311.09682. Checked: fetched. Ids: b-20.
29. Wang, Veugelers, Stephan (2017). Bias against novelty in science: A cautionary tale for users of bibliometric indicators. Research Policy 46(8):1416-1436 (NBER WP 22180). https://www.nber.org/papers/w22180. Checked: fetched/memory. Ids: b-21, c-15.
30. Beel, Kan, Baumgart (2025). Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising Future?. arXiv:2502.14297 (preprint). https://arxiv.org/abs/2502.14297. Checked: fetched. Ids: c-03.
31. Gupta, Pruthi (2025). All That Glitters is Not Novel: Plagiarism in AI Generated Research. ACL 2025 (arXiv:2502.16487). https://arxiv.org/abs/2502.16487. Checked: fetched. Ids: c-04.
32. Padmakumar, He (2023). Does Writing with Language Models Reduce Content Diversity?. ICLR 2024 (arXiv:2309.05196). https://arxiv.org/abs/2309.05196. Checked: fetched. Ids: c-06.
33. Mohammadi (2024). Creativity Has Left the Chat: The Price of Debiasing Language Models. arXiv:2406.05587 (preprint). https://arxiv.org/abs/2406.05587. Checked: fetched. Ids: c-07.
34. Lu, Sclar, Hallinan, et al. (2024). AI as Humanity's Salieri: Quantifying Linguistic Creativity of Language Models via Systematic Attribution of Machine Text against Web Text. arXiv:2410.04265 (preprint). https://arxiv.org/abs/2410.04265. Checked: fetched. Ids: c-08.
35. Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024). Can large language models explore in-context?. NeurIPS 2024 (arXiv:2403.15371). https://arxiv.org/abs/2403.15371. Checked: fetched. Ids: c-09.
36. Huang, Chen, Mishra, Zheng, Yu, Song, Zhou (2023). Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024 (arXiv:2310.01798). https://arxiv.org/abs/2310.01798. Checked: fetched. Ids: c-10.
37. Sharma, Tong, Korbak, et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv:2310.13548 (preprint, ICLR 2024). https://arxiv.org/abs/2310.13548. Checked: fetched. Ids: c-11.
38. Holst, Algaba, Tori, Wenmackers, Ginis (2024). Dataset Artefacts are the Hidden Drivers of the Declining Disruptiveness in Science. arXiv:2402.14583 (preprint). https://arxiv.org/abs/2402.14583. Checked: fetched. Ids: c-12.
39. Leibel, Bornmann (2023). What do we know about the disruption index in scientometrics? An overview of the literature. arXiv:2308.02383 (preprint). https://arxiv.org/abs/2308.02383. Checked: fetched. Ids: c-13.
40. Mueller, Melwani, Goncalo (2012). The Bias Against Creativity: Why People Desire but Reject Creative Ideas. Psychological Science. https://doi.org/10.1177/0956797611421018. Checked: memory. Ids: c-17.
41. Mullen, Johnson, Salas (1991). Productivity loss in brainstorming groups: A meta-analytic integration. Basic and Applied Social Psychology. https://doi.org/10.1207/s15324834basp1201_1. Checked: memory. Ids: c-18.
42. Girotra, Terwiesch, Ulrich (2010). Idea Generation and the Quality of the Best Idea. Management Science. https://doi.org/10.1287/mnsc.1090.1144. Checked: memory. Ids: c-19.
43. Micah Zhang (2026). Budgeted Subset Refinement for Execution-Aware LLM Research Ideation. arXiv 2607.14118 preprint. https://arxiv.org/abs/2607.14118. Checked: fetched. Ids: d-03, d-04.
44. Marek Suppa, Viktoria Ondrejova, Lucia Ganajova, Gregor Karetka, Daniel Skala (2026). RAGthoven at SemEval-2026 Task 1. arXiv 2607.13189 preprint (summary from API feed). https://arxiv.org/abs/2607.13189. Checked: abstract. Ids: d-05.
45.  (2026). gap check, best-of-N creative scaling. arXiv API queries. http://export.arxiv.org/api/query?search_query=all:%22best-of-n%22%20AND%20all:creativity. Checked: fetched. Ids: d-06.
46. Hossein A. Rahmani, Satyapriya Krishna, Xi Wang, Mohammadmehdi Naghiaei, Emine Yilmaz (2025). Self-Correcting Large Language Models: Generation vs. Multiple Choice. arXiv 2511.09381 preprint. https://arxiv.org/abs/2511.09381. Checked: fetched. Ids: d-07.
47. Sion Weatherhead, Flora Salim, Aaron Belbasis (2025). Illusions of reflection: open-ended task reveals systematic failures in Large Language Models' reflective reasoning. arXiv 2510.18254 preprint. https://arxiv.org/abs/2510.18254. Checked: fetched. Ids: d-08.
48. Weatherhead et al.; Rahmani et al. (2025). synthesis of arXiv 2510.18254 and 2511.09381. preprints. https://arxiv.org/abs/2510.18254. Checked: fetched. Ids: d-09.
49. Priyanka Kargupta, Shuhaib Mehri, Dilek Hakkani-Tur, Jiawei Han (2026). Sparking Scientific Creativity via LLM-Driven Interdisciplinary Inspiration. arXiv 2603.12226 preprint. https://arxiv.org/abs/2603.12226. Checked: fetched. Ids: d-10.
50. Mete Ismayilzada, Renqing Cuomao, Daniil Yurshevich, Anna Sotnikova, Lonneke van der Plas, Antoine Bosselut (2026). CresOWLve: Benchmarking Creative Problem-Solving Over Real-World Knowledge. arXiv 2604.03374 preprint (summary from API feed). https://arxiv.org/abs/2604.03374. Checked: abstract. Ids: d-11.
51.  (2026). gap check, analogical retrieval. arXiv API queries. http://export.arxiv.org/api/query?search_query=all:%22large%20language%20models%22%20AND%20all:analogical%20AND%20all:retrieval%20AND%20all:creativity. Checked: fetched. Ids: d-12.
52. Junming Huang, Yu Xie (2026). Large scientific teams are more, not less, disruptive. arXiv 2610.07329 preprint. https://arxiv.org/abs/2610.07329. Checked: fetched. Ids: d-13.
53. Yiling Lin, Linzhuo Li, Lingfei Wu (2025). Team Size and Its Negative Impact on the Disruption Index. arXiv 2502.00219 preprint. https://arxiv.org/abs/2502.00219. Checked: fetched. Ids: d-14.
54. Alexander M. Petersen, Felber Arroyave, Fabio Pammolli (2024). The disruption index suffers from citation inflation and is confounded by shifts in scholarly citation practice. arXiv 2406.15311 preprint. https://arxiv.org/abs/2406.15311. Checked: fetched. Ids: d-15.
55. Huang and Xie; Lin, Li and Wu; Petersen et al. (2026). synthesis. arXiv preprints. https://arxiv.org/abs/2610.07329. Checked: fetched. Ids: d-16.
56. Yulin Yu, Daniel M. Romero (2024). Does the Use of Unusual Combinations of Datasets Contribute to Greater Scientific Impact?. arXiv 2402.05024 preprint. https://arxiv.org/abs/2402.05024. Checked: fetched. Ids: d-17.
57.  (2026). gap check, Uzzi replication. arXiv API and web search. http://export.arxiv.org/api/query?search_query=all:%22atypical%20combinations%22. Checked: fetched. Ids: d-18.
