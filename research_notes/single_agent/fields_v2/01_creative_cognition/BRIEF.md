# Creative cognition: what it offers one thinking agent

Ids like a-03 mean creative-a-03 in the evidence files. "Our data" means the measurements in 00_PLAN.md (NoveltyBench distinct answers 3.18 to 9.63; architecture search 7% lower perplexity; ARC plain 4/10 vs scaffold 2/8; word puzzles about 92% vs about 75%). Where evidence_d CHECK lines (d-22 to d-28) differ from claims.jsonl, the CHECK lines are used.

## 1. What the field studies

Creative cognition asks how people produce ideas that are both new and useful, and what gets in the way. The founding frame is Geneplore: a generate phase builds rough candidate structures, and an explore phase tests and develops them, in cycles (a-01, a-02). It is a descriptive model with no replication found and no LLM application found (c-21, b-22). Most human work uses short lab tasks with student samples: inventing alien animals, designing with examples, brainstorming in groups, taking breaks from a problem (a-03, a-05, a-09, a-13). Newer work asks the same questions of language models: how varied their ideas are, whether they fixate, and whether they can judge ideas (b-01, b-05, d-06).

## 2. Established findings

Status "established" means at least two independent sources agree. Size and source quality are given, because several are weaker than the label suggests.

**E1. Examples cause fixation.** People who see an example copy its features. They do so after a distractor task and when told to avoid it (a-05, a-06, a-07). Three lines of work agree: Jansson and Smith 1991, Smith et al. 1993, and the 2022 review (a-05, a-06, a-07, c-12). Limits: the examples meta-analysis of Sio, Kotovsky and Cagan 2015 says conditions decide whether examples fixate or inspire (a-08). I only confirmed it exists, not its numbers (d-17). Examples that break basic assumptions can raise creativity (c-13, essay level). Quantity, abstraction and closeness of the example change the risk (d-18, abstract only). So fixation is the default, not a law.

**E2. Group brainstorming loses to pooled solo work.** In 22 experiments, 18 found the pooled solo ("nominal") groups better and 4 found no difference. None found real groups better (a-09). Production blocking, meaning waiting your turn so ideas are lost, explained most of the loss (a-10, c-10). Fear of evaluation hurt individuals but did not explain the group gap (a-11). A meta-analysis found nominal groups better, with larger loss in bigger groups, but I only saw a snippet, no effect size (a-12). The transferable part for an agent is narrow: generate in isolation, then pool.

**E3. LLM output on open prompts is homogeneous.** One model repeats itself and different models converge (b-01, c-05). Frontier models are less varied than human writers, and larger models are often less varied than smaller ones (b-02). Independent LLM samples are less varied than independent human samples because the model blends knowledge into one distribution (b-06). Prompting for creativity or reasoning left cross-trial diversity flat, and frontier models had the narrowest vocabulary (c-07). Four sources, two peer-reviewed or benchmarked (b-01, b-02), two preprints (b-06, c-07). This agrees with our NoveltyBench result (3.18 of 10 distinct, plain model).

**E4. LLM judges are poor on contested taste and on novelty.** Models, reward models and LM judges track human ratings worse where annotators disagree (c-06, b-01). LLM self-evaluation of research ideas is weak (b-08, d-08). A judge told which idea reviewers found novel changed its verdict on over half of identical pairs (d-06, preprint). Judged novelty did not survive execution (b-09, d-07). No work found proves that a tournament or judge panel fixes this. Execution-based or external checks are the only option with some support (d-23).

**E5. Creativity training works a little.** Raw effects look large: d = 0.64 (a-18, snippet), g = 0.53 across 332 effect sizes (a-15). The largest and most careful meta-analysis (169 studies, 844 effects) found 0.53 raw but only 0.29 to 0.32 after correcting for publication bias, with many flawed studies (a-17). Use 0.3 SD. Haase 2023 found methods aimed at convergent thinking beat those aimed at divergent thinking, but on k = 11 with huge spread (a-16). That is not enough to act on.

**E6. Thinking models and general ability do not reliably predict creativity.** On CREATE, thinking models were not always better even with large token budgets (b-14). LiveIdeaBench found idea quality poorly predicted by general-intelligence scores (b-17). Zhang 2025 and Verdoorn 2026 agree in direction (b-02, c-07). Caveat: these are mostly preprints with LLM judges (b-14, b-17). Read it as "more thinking tokens is not a creativity strategy", not as a measured effect size.

## 3. Single-source and contested findings

### 3a. Single-source (one study or one group; hold loosely)

- **Typical-first (path of least resistance).** People imagining novel category members recall an Earth exemplar and modify it (a-03, c-19). Frith et al. 2022 cite it but add no replication (a-04), and no replication or meta-analysis was found (d-24). Treat Ward as one old study read from snippets (a-03).
- **Incubation.** Setting a problem aside gives a weighted effect of 0.29, 95% CI 0.21 to 0.39, over 117 effect sizes (a-13, d-14). Larger for divergent than insight tasks, larger with longer preparation, smaller when the break is filled with demanding work (a-14). All four lines trace to one meta-analysis. No newer meta-analysis or replication was found, and no LLM analogue exists (d-26).
- **More ideas does not give better chosen ideas.** Idea quantity was unrelated to the quality of the idea finally selected, and people prefer feasible over original ideas when picking (c-11). One review abstract. Needs a second source.
- **LLMs fixate too.** Early outputs narrow later ones. Chain-of-thought reduced fixation in LLMs but not in humans (b-05). A design-engineering agent also fixated on existing paradigms (d-09), and a hackathon LLM showed design fixation (d-11, snippet).
- **AI ideas help individuals but narrow the set.** In a randomized study of 293 writers, AI story ideas raised novelty (+5.4% with one idea, +8.1% with five) and usefulness, but stories grew more alike (b-07, c-02). Low-creativity writers gained most (c-03). One study.
- **Ideation-execution gap.** Blind experts rated LLM ideas more novel than human ideas (b-08). After 43 experts executed them, LLM ideas lost more score on every metric and rankings often flipped (b-09, d-07). One research group, two stages. Strong designs.
- **Spread and quality are separate dials.** Reasoning prompts raised the score but not diversity, and wider sampling raised diversity without a matching score gain (c-07, c-08). One preprint, five models.
- **Multi-agent structure.** Interaction structure mattered more than agent count. Authority-led groups gave less diversity, more agents gave diminishing returns, dense communication converged early (b-12). Preprint.
- **Ensembles of different models.** Pooling several LLMs beat any single model on counts of unique valid scientific ideas (d-13, abstract only).
- **Same-prompt spread is large.** Only 0.28% of responses reached the top 10% of human creativity benchmarks, and the authors advise repeated sampling (d-12, abstract).
- **Analogy pipelines for LLMs.** Cross-domain analogy then search raised solution diversity 90 to 173% on four biomedical problems (d-05). Idea-Catalyst raised average novelty 21% (d-19). Both abstract only, judges unknown or not stated (d-05, d-19).
- **Separate generation from selection.** A split between free divergent generation and a convergent step against constraints improved interactive agents (d-10, abstract only). A metacognitive supervising agent beat self-regulation, and both beat a plain loop, at similar compute (d-09, one design problem).
- **Verbal overshadowing.** Describing a solution while working can impair insight (c-20). From memory, not verified, with replication concerns in the wider literature.
- **LLM help may hurt later solo work.** Two pre-registered experiments, 1,100 participants (b-13). Weak relevance to a standalone agent.
- **Remote Associates Test is a poor LLM measure.** Contamination is claimed from a search summary only (b-16). Validity doubts come from low-credibility snippets (c-18).
- **Flat associative hierarchy.** Mednick's idea was later questioned (a-19). Snippet level, weak hypothesis.

### 3b. Contested

- **Verbalized sampling (VS) raises diversity 1.6 to 2.1 times in creative writing, more for capable models** (b-03, c-09, d-01). Authors blame typicality bias in preference data (b-04). Quality is judged by one LLM judge and reported as "comparable", basic VS and sequence prompting cost some quality, and no best-of-n or top-k test was found (d-02, d-03). Does diversity boosting improve the best output? Unsettled (d-22). A separate preprint states that diversity methods often cost quality (d-04). One preprint, no independent replication.
- **Far analogies.** Far combinations raise novelty, but evidence that they raise quality is mixed. Two lab studies found lower quality, and on an innovation platform greater distance lowered the chance of success (c-14, c-15). Distant analogies help only up to a point (d-16). After far analogies a professional team's ideas were more similar to the previous ones, though output rate rose (d-15). A 2019 study of 84 students found near analogies better for designers without analogy training (c-16, b-20, same study, snippet). Rule from the CHECK: medium distance, then iterate (d-25).
- **Personas restore diversity.** Ten persona generators gave a pool close to human-only diversity (c-04, preprint). A white paper reports +4.1 points of LLM-judged diversity and flags judge bias (b-21, low credibility). Deng et al. found ordinary personas partitioned knowledge better than creative-expert personas, so content matters (b-05).
- **Temperature as a creativity dial.** Weak link to novelty, moderate to incoherence, one model and one task (b-11). Wider sampling pools did raise cross-trial diversity in five models (c-08). Both can hold: novelty and cross-trial diversity are different. A re-examination of min-p sampling found no gain over baseline samplers (d-20, snippet).

## 4. Mechanisms an agent can run

Equal-token test for every Check: run the plain model with the same total tokens (for example, best-of-k plain samples), and score both with the same external measure. A mechanism passes only if it wins at equal tokens, and on single-answer tasks it must not lose.

**M1. Task-type gate (build ourselves).**
- Trigger: start of every task.
- Action: classify the task as open-ended (many valid answers, no single key) or single-answer. Turn on M2 to M8 only for open-ended. Single-answer tasks get the plain first answer plus a real check.
- Check: on a mixed set (NoveltyBench-style prompts plus ARC and word puzzles), gate on vs gate off vs plain, equal tokens. Success is the open-task gain kept and the single-answer loss gone.
- Evidence: d-27 (no source gives a gate); our data (diverge helped on open tasks, hurt on ARC and word puzzles).
- Risk: a wrong classification applies divergence to a single-answer task, which cost accuracy every time in our data. A task can be part open, part single-answer.

**M2. Isolated generation, fresh context per idea, then pool.**
- Trigger: gate says open-ended.
- Action: make k independent calls, each from the bare task, none seeing the others' ideas. Pool afterward.
- Check: k isolated calls vs one call that lists k ideas vs k sequential calls with "avoid the previous", equal tokens, compared by distinct-answer count and best-of-k score.
- Evidence: a-09, a-10 (human blocking, a loose analogy); b-05 (LLM fixation, preprint); b-06; b-12; d-12.
- Risk: only one preprint shows isolation beats sequential for LLMs (b-05). The human blocking result is about turn-taking, which an LLM does not have (a-10). Isolated samples share one model's distribution, so they stay correlated (b-06, c-07).

**M3. Write the typical answer first, then move away from it.**
- Trigger: open-ended task, at the start of each isolated call.
- Action: state the most obvious answer, label it "typical", and require the final idea to differ in a named feature.
- Check: with vs without the typical-first step, equal tokens, distinct count and judged usefulness. Our NoveltyBench schema already wrote the obvious answer first, so test this part alone.
- Evidence: a-03, c-19 (one old study); b-05; b-02.
- Risk: weakest human base (d-24). It is a plausible rule, not a tested one. Forced difference can give odd but worse ideas (b-09).

**M4. Verbalized sampling.**
- Trigger: open-ended task, when one call must give several answers.
- Action: ask for a set of answers with stated probabilities, sampled from the tails.
- Check: best-of-k quality under VS, persona and plain sampling, on a task with an external score (this is exactly the gap named in d-22).
- Evidence: b-03, c-09, d-01, d-02, d-03, d-22.
- Risk: single preprint, one judge, basic VS cost some quality (d-02). Raises spread, and spread is not creativity (c-08).

**M5. Feasibility and execution check before choosing.**
- Trigger: after generating, before selecting, whenever an idea can be run, simulated or tested.
- Action: run the candidate if a check exists (a training run, code, a test). Otherwise write the cheapest test and apply it. Rank by the measured result, not the judged novelty.
- Check: pick by check vs pick by LLM judge, same candidates, same tokens, compared on the external score.
- Evidence: b-09, d-07; b-08; c-11; d-23 (only execution-based selection has support); d-09 (measured design score). Our architecture search used a training run as judge and won 7%.
- Risk: costs tokens. Where no check exists the step falls back to a weak judge (d-06).

**M6. Judge by someone other than the generator.**
- Trigger: selection with no external check.
- Action: use several prompts and judges, with different models if possible, and keep disagreement visible. Do not let the generating call rank its own ideas as the only filter.
- Check: panel vs single self-judge on a task with human or executed ground truth, equal tokens.
- Evidence: c-06; b-08; d-06; d-23. No work shows a panel fixes it (d-23).
- Risk: a panel of one model is correlated. It is a weak filter, not a repair. Judge wording can flip verdicts (d-06).

**M7. Medium-distance analogy, then iterate.**
- Trigger: open-ended task stuck near the obvious answer, or the escalation ladder reaches "borrow by analogy".
- Action: choose a source domain at medium distance, write the mapping, make several refinement rounds, then run the M5 check.
- Check: analogy step vs plain extra samples, equal tokens, scored by an external test.
- Evidence: d-25; d-16; d-15; c-14, c-15; d-05 (preprint, abstract only).
- Risk: contested (3b). Too-far sources lower quality (c-15, d-16). Analogy generation clusters in narrow domains (d-04).

**M8. Two phases, generate then explore, with a separate supervisor.**
- Trigger: open-ended task with a constraint set.
- Action: phase one is free generation with no judging. Phase two selects against constraints and develops survivors. A separate call checks whether the loop is stuck on one paradigm.
- Check: two-phase vs one-pass at equal tokens. Include the supervisor call in the token count.
- Evidence: a-01, a-02 (framework, not tested); d-10; d-09.
- Risk: Geneplore is a metaphor, not tested evidence (c-21). The agent results are abstract-level preprints (d-09, d-10). Setup cost sank our full scaffold on BrainTeaser (own data).

**M9. Revisit after a context reset (untested).**
- Trigger: stalled open-ended task.
- Action: drop the context, keep only the task and a one-line state, and try again later.
- Check: reset vs continue, equal tokens.
- Evidence: a-13, a-14 give 0.29 for humans; d-26 found no LLM analogue.
- Risk: the human effect is small, and the break mechanism may not exist in a model. Try only because it is cheap.

**M10. Mixed models or personas in the pool.**
- Trigger: open-ended task, when an agent can call more than one model or voice.
- Action: pool candidates from different models or ordinary-person personas, not creative-expert personas.
- Check: mixed pool vs single-model pool, equal tokens, best-of-k.
- Evidence: d-13; b-01; c-04; b-05.
- Risk: contested (3b). Personas may add noise rather than quality (d-04).

## 5. Evidence on LLMs and AI agents

- Diversity is the main problem. Models repeat themselves and each other (b-01, b-02, c-05), and one study traces it to blending knowledge into one distribution (b-06). Preference data may favor typical text (b-04, hypothesis).
- Flat prompts do not fix it. Creativity and reasoning prompts raised scores without raising cross-trial diversity (c-07). More thinking tokens did not reliably help (b-14).
- LLMs beat the average human on a word-distance task but not highly creative humans (b-10).
- Novelty without execution is misleading. LLM ideas looked better to reviewers and lost after execution (b-08, b-09).
- Judging is weak. See E4 (c-06, d-06, d-23).
- Single-model sampling gives a wide spread, so repeated sampling is advised (d-12). Ensembles of models did better than single models on unique valid ideas (d-13).
- Agent systems: a design agent fixated, and separate metacognitive supervision helped (d-09). Structure beats agent count in multi-agent idea generation (b-12). Splitting divergent from convergent steps helped (d-10).
- Note on measurement: much LLM diversity is scored by an LLM judge, which the evidence itself calls unreliable here (c-06, d-06). Only one source checked execution (b-09).
- Not found: a controlled test of conceptual blending, constraint relaxation, TRIZ or SCAMPER procedures on LLM agents (d-28), and a test of independent resampling vs sequential "avoid previous ideas" prompting beyond one preprint (b-05).

## 6. What does not transfer to a model

- **Production blocking.** Humans lose ideas while waiting their turn (a-10). A model has no turn-taking. Only "isolate samples, then pool" carries over.
- **Incubation as a rest period.** There is no clear analogue of a break (d-26). A demanding filler task shrank the human effect (a-14), and a context reset is not the same thing.
- **Evaluation apprehension.** It hurt humans (a-11). A model has no fear of judgment.
- **Group size effects.** Human group loss grows with size (a-12). Multi-agent LLM results show diminishing returns for different reasons (b-12).
- **Training and drug effects.** Creativity training (a-17) and drugs (a-15) change people, not a fixed model.
- **Student lab tasks.** One-shot ideas by students (a-03, a-05) may not carry over to a model that can run 50 calls.
- **Remote Associates and similar tests.** Likely contaminated in training and a poor measure of LLM creativity (b-16).
- **Exposure over time.** A model has no memory between calls unless we give it one. Fixation by earlier examples (a-05) applies only to what sits in the current context (b-05).

## 7. Open questions

1. How to tell open-ended from single-answer tasks. No source supplies a gate (d-27).
2. Does diversity-raising help the best answer, or only the spread? No top-k or best-of-n test was found (d-22, d-03).
3. What selection method works after generation? Only execution-based or external checks have any support (d-23).
4. Does independent resampling beat sequential "avoid previous ideas"? One preprint (b-05).
5. Do concrete procedures (reformulation, constraint relaxation, blending) help LLM agents? No controlled evidence found (d-28, b-18, b-19).
6. Does Ward's typical-first effect replicate, and does an LLM show the same pull? (d-24, b-05)
7. Is there any LLM analogue of incubation? (d-26)
8. Do reasoning models gain in creativity? Two benchmarks say no, both preprints with LLM judges (b-14, b-17).
9. Does the 0.3 SD training effect give any prior for prompt training of agents? Likely none (a-17).

## 8. References

How checked: fetched = page opened; abstract = abstract page only; snippet = search result only; memory = not opened.

1. Finke, Ward, Smith 1992. Creative Cognition: Theory, Research, and Applications. MIT Press. https://www.cede.ch/en/books/?id=1709959 (snippet; a-01, a-02, c-21; also https://api.philpapers.org/rec/FINICA, snippet)
2. Ward 1994. Structured imagination: The role of category structure in exemplar generation. Cognitive Psychology 27(1). https://eprints.gla.ac.uk/226695 (snippet; a-03; c-19 via https://www.rug.nl/hrm-ob/bloggen/blog-01-09-2015-innovatie-en-het-pad-van-de-minste-weerstand, snippet)
3. Frith, Gerver, Benedek, Christensen 2022. Neural Representations of Conceptual Fixation during Creative Imagination. Creativity Research Journal. https://beatylab.la.psu.edu/files/2022/09/2022-Frith-CRJ.pdf (fetched; a-04, a-07, a-20)
4. Jansson and Smith 1991, Design fixation, Design Studies 12(1); Smith, Ward, Schumacher 1993, Memory & Cognition. As summarized at https://pmc.ncbi.nlm.nih.gov/articles/PMC5365093 (fetched, secondary; a-05, a-06). Jansson and Smith also via https://www.psychologytoday.com/us/blog/creativity-you/201703/can-conformity-be-creative (snippet; c-12). Okada and Ishibashi 2017 via the same blog (fetched; c-13).
5. Sio, Kotovsky, Cagan 2015. Fixation or inspiration? A meta-analytic review of the role of examples on design processes. Design Studies 39. https://doi.org/10.1016/j.destud.2015.04.004 (snippet; a-08, d-17)
6. Examples in Design Education: Inspiration or Fixation? 2018. SHS Web of Conferences. https://doi.org/10.1051/shsconf/20184801061 (abstract; authors not retrieved; d-18)
7. Diehl and Stroebe 1987. Productivity loss in brainstorming groups: Toward the solution of a riddle. J. Personality and Social Psychology. https://homepages.se.edu/cvonbergen/files/2013/01/Productivity-Loss-In-Brainstorming_Toward-the-Solution-of-a-Riddle.pdf (fetched; a-09, a-10, a-11)
8. Mullen, Johnson, Salas 1991. Productivity loss in brainstorming groups: A meta-analytic integration. Basic and Applied Social Psychology. https://scrapbox.io/nishio-en/Productivity_Loss_in_Brainstorming_Groups:_A_Meta-Analytic_Integration (snippet; a-12)
9. Stroebe, Nijstad, Rietzschel 2010. Beyond productivity loss in brainstorming groups. Advances in Experimental Social Psychology. https://research.rug.nl/en/publications/beyond-productivity-loss-in-brainstorming-groups-the-evolution-of/ (abstract; c-10, c-11)
10. Sio and Ormerod 2009. Does incubation enhance problem solving? A meta-analytic review. Psychological Bulletin 135(1). https://eprints.lancs.ac.uk/id/eprint/56211 (fetched; a-13, a-14); https://doi.org/10.1037/a0014212 (abstract; d-14); c-17 (abstract)
11. Haase, Hanel, Gronau 2023. Creativity Enhancement Methods for Adults: A Meta-Analysis. Psychology of Aesthetics, Creativity, and the Arts. https://edoc.hu-berlin.de/bitstreams/957e5d97-99fb-4c1d-91ac-48b7ccf9032a/download (fetched; a-15, a-16)
12. Sio and Lortie-Forgues 2024. The impact of creativity training on creative performance: a meta-analytic review. Psychological Bulletin 150(5). https://eprints.whiterose.ac.uk/id/eprint/209749/ (fetched; a-17)
13. Scott, Leritz, Mumford 2004. The effectiveness of creativity training: A quantitative review. Creativity Research Journal 16. Reported via https://repository.essex.ac.uk/34344/1/CreativityEnhancementMethods_accepted.pdf (snippet; a-18)
14. Mednick 1962; Benedek and Neubauer 2014. The roles of associative and executive processes in creative cognition. Memory & Cognition 42(7). https://pure.psu.edu/en/publications/the-roles-of-associative-and-executive-processes-in-creative-cogn/ (snippet; a-19)
15. Jiang, Chai, Li, Liu, Fok, Dziri, Tsvetkov et al. 2025. Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond). NeurIPS 2025. https://arxiv.org/abs/2510.22954 (fetched; b-01, c-05, c-06)
16. Zhang, Diddee, Holm, Liu, Liu, Samuel, Wang et al. 2025. NoveltyBench. arXiv 2504.05228 (preprint). https://arxiv.org/abs/2504.05228 (fetched; b-02)
17. Zhang, Yu, Chong, Sicilia, Tomz, Manning 2025. Verbalized Sampling. arXiv 2510.01171 (preprint). https://arxiv.org/abs/2510.01171 (fetched; b-03, b-04 snippet, c-09 abstract, d-01 to d-03 fetched)
18. Deng, Brucks, Toubia 2026. Examining and Addressing Barriers to Diversity in LLM-Generated Ideas. arXiv 2602.20408 (preprint). https://arxiv.org/abs/2602.20408 (abstract; b-05, b-06)
19. Doshi and Hauser 2024. Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances 10(28). https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532 (fetched; b-07, c-01, c-02, c-03)
20. Si, Yang, Hashimoto 2024. Can LLMs Generate Novel Research Ideas? ICLR 2025. https://arxiv.org/abs/2409.04109 (fetched; b-08; abstract d-08)
21. Si, Hashimoto, Yang 2025. The Ideation-Execution Gap. ICLR 2026. https://arxiv.org/abs/2506.20803 (fetched; b-09, d-07)
22. Bellemare-Pepin, Lespinasse, Thoelke, Ha 2025. Divergent Creativity in Humans and Large Language Models. arXiv 2405.13012 (preprint). https://arxiv.org/abs/2405.13012 (fetched; b-10)
23. Peeperkorn, Kouwenhoven, Brown, Jordanou 2024. Is Temperature the Creativity Parameter of Large Language Models? ICCC 2024. https://arxiv.org/abs/2405.00492 (snippet; b-11)
24. Chen, Tong, Yang, He, Zhang, Zou, Wang et al. 2026. Diversity Collapse in Multi-Agent LLM Systems. arXiv 2604.18005 (preprint). https://arxiv.org/abs/2604.18005 (fetched; b-12)
25. Kumar, Vincentius, Jordan, Anderson 2024. Human Creativity in the Age of LLMs. arXiv 2410.03703 (preprint). https://arxiv.org/abs/2410.03703 (fetched; b-13)
26. Wadhwa, Roy, Lederman, Li, Durrett 2026. CREATE: Testing LLMs for Associative Creativity. arXiv 2603.09970 (preprint). https://arxiv.org/abs/2603.09970 (fetched; b-14, b-15; b-16 snippet)
27. Ruan, Wang, Hong, Wang, Liu, Sun 2024. LiveIdeaBench. arXiv 2412.17596 (preprint). https://arxiv.org/abs/2412.17596 (fetched; b-17)
28. Search summary of a 35-LLM blending benchmark, title and authors unconfirmed. https://arxiv.org/abs/2509.21043 (snippet; b-18, low credibility)
29. Gu et al. 2024. LLMs can Realize Combinatorial Creativity. arXiv 2412.14141 (preprint). https://arxiv.org/abs/2412.14141 (snippet; b-19, b-22)
30. Design-by-analogy experiment, 84 students, 2019 (authors not captured; Becattini and Cascini given in a search result). https://www.designsociety.org/publication/30665/on_the_effective_use_of_design-by-analogy_the_influences_of_analogical_distance_and_commonness_of_analogous_designs_on_ideation_performance (snippet; b-20, c-16)
31. The Spark Effect. 2025. arXiv 2510.15568 (preprint). https://arxiv.org/html/2510.15568v1 (snippet; b-21)
32. Wan and Kalman 2025. Follow-up to Doshi and Hauser with persona-diverse ideas. arXiv 2504.13868 (preprint). https://arxiv.org/pdf/2504.13868 (snippet; c-04)
33. Verdoorn and Paperno 2026. High Scores, Narrow Vocabularies. NeurIPS 2026 workshop poster. https://neurips.cc/virtual/2026/164741 (abstract; c-07, c-08)
34. Chan and Schunn 2015. The importance of iteration in creative conceptual combination. Cognition. https://www.lrdc.pitt.edu/Schunn/papers/Chan-Schunn2015-Cognition.pdf (snippet; c-14, c-15)
35. Chan and Schunn 2015. The impact of analogies on creative concept generation: lessons from an in vivo study. Cognitive Science 39(1). https://europepmc.org/search?query=%22analogies%20on%20creative%20concept%20generation%22 (abstract; d-15)
36. Fu, Chan, Cagan, Kotovsky, Schunn, Wood 2013. The Meaning of Near and Far. Journal of Mechanical Design. https://doi.org/10.1115/1.4023158 (abstract; d-16)
37. Remote Associates Test validation studies, 2017, as summarized at https://en.wikipedia.org/wiki/Remote_Associates_Test (snippet; c-18)
38. Schooler, Ohlsson, Brooks 1993. Thoughts beyond words. J. Experimental Psychology: General. No URL (memory; c-20)
39. Shen, de Sousa, Barcelos, Guo, Zhu 2026. On the Diversity of Analogy Making in LLMs. arXiv 2608.03233 (preprint). https://arxiv.org/abs/2608.03233 (abstract; d-04)
40. Shen, Druckmann, Zou 2026. Unlocking LLM Creativity in Science through Analogical Reasoning. arXiv 2605.11258 (preprint). https://arxiv.org/abs/2605.11258 (abstract; d-05)
41. Sternlicht, Shahid, Jansen, Weld, Siangliulue et al. 2026. Old Ideas, Novel Problems. arXiv 2610.02022 (preprint). https://arxiv.org/abs/2610.02022 (fetched; d-06)
42. Xu, Martelaro, McComb 2026. Supervising Ralph Wiggum. arXiv 2603.24768 (preprint). https://arxiv.org/abs/2603.24768 (abstract; d-09)
43. Park et al. 2026. Beyond One Path. arXiv 2605.28465 (preprint). https://arxiv.org/abs/2605.28465 (abstract; d-10)
44. Ege, Ovrebo, Stubberud, Berg, Elverum et al. 2024. ChatGPT as an inventor. arXiv 2404.18479 (preprint). https://arxiv.org/abs/2404.18479 (snippet; d-11)
45. Haase et al. 2025. Has the Creativity of Large-Language Models peaked? arXiv 2504.12320 (preprint). https://arxiv.org/abs/2504.12320 (abstract; d-12)
46. Mathur et al. 2026. LLM Jaggedness Unlocks Scientific Creativity. arXiv 2605.10574 (preprint). https://arxiv.org/abs/2605.10574 (abstract; d-13)
47. Kargupta, Mehri, Hakkani-Tur, Han 2026. Sparking Scientific Creativity via LLM-Driven Interdisciplinary Inspiration (Idea-Catalyst). arXiv 2603.12226 (preprint). https://arxiv.org/abs/2603.12226 (abstract; d-19)
48. Schaeffer, Kazdan, Denisov-Blanch 2025. Min-p, Max Exaggeration. arXiv 2506.13681 (preprint). https://arxiv.org/abs/2506.13681 (snippet; d-20)
49. Liu et al. 2026. MindFlow. arXiv 2610.11966 (preprint). https://arxiv.org/abs/2610.11966 (abstract; d-21; tournament ranking of thinking flows, no numbers)
50. CHECK lines d-22 to d-28: the research round's own re-checks (fetched or abstract level, see each line). No separate source.
