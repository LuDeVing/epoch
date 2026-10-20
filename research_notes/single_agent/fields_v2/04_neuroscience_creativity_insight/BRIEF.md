# Cognitive neuroscience of creativity and insight: what it offers one thinking agent

Notes on reading this brief. Ids like a-01 stand for neuro-a-01; b-xx for neurocreat-b-xx (or neuro-b-xx); c-xx and d-xx for neuro-c-xx and neuro-d-xx. Where an evidence_d CHECK line disagrees with the earlier claims file, the CHECK line is used. Our own measurements come from 00_PLAN.md (marked [ours]). Brain findings here are analogies for an agent, not tests of an agent (b-22).

## 1. What the field studies

The field uses brain imaging, EEG and brain stimulation to ask what happens when people produce new ideas (divergent thinking, poetry, music, art, metaphor) and when they suddenly see a solution (insight). It also covers incubation: whether a break helps, and why (a-01, a-15, a-16). Two lab families dominate: Beaty, Silvia and Benedek on idea generation, and Kounios and Beeman on insight (critique, a-13, a-14). The evidence is mostly correlational (c-12), often small-sample (c-15), and the imaging literature on creativity contradicts itself on which region matters (c-18).

## 2. Established findings

These have status "established" in the claims file, with the CHECK corrections applied. The "independence" notes matter: several rest on one lab family.

**E1. Creative work uses the default network and the executive control network together, although they usually oppose each other.** A review across divergent thinking, poetry, music and visual art says they cooperate (a-01). A connectome model fit on 163 people found the high-creativity network had hubs in default, salience and executive regions (b-01, b-02). The review reads the default network as a stream of candidate ideas from memory and the control network as a constraint to the goal (a-02). This is correlational (c-12), and the memory account is partly speculative (c-14).

**E2. Early idea generation couples default with salience regions; later stages couple default with executive regions.** Seen in divergent thinking (a-05, b-03) and in novel metaphor production (a-25). Independence is weak, since the same lab ran all of it. Read it as "a switch, then control".

**E3. Divergent thinking quality needs both loose association and executive ability.** In two studies, both semantic distance of answers and executive ability (broad retrieval, fluid intelligence) uniquely predicted answer quality (a-10). In a latent-variable study of 230 people, working-memory updating and inhibition predicted creativity but shifting did not (a-12). Beaty and Kenett separate free from goal-directed association (b-04). Cognitive control helps most when conceptual knowledge is limited (b-05, snippet only, credibility 60).

**E4. Later ideas in a session are more original (serial-order effect), and high fluid intelligence flattens the rise.** Reported as replicated in many studies, though the count was not given (a-11). Semantic-distance models reproduce the effect in human data (b-15). This is a human result. The claim that LLMs show it is unverified (see section 5).

**E5. Divergent thinking and insight use non-overlapping brain regions.** A meta-analysis of 57 fMRI studies (27 divergent, 30 insight) found no overlapping clusters (a-24). A separate meta-analysis of 20 divergent-thinking studies, 596 people, found four clusters (a-23). A review of 72 studies says the literature is self-contradicting, so no single-region claim is safe (c-18). Treat them as two different processes.

**E6. The control network is not one thing.** One control subnetwork correlates positively with the default network at rest and another negatively, and only one tracks individual creative ability (c-16, c-17, 171 people). The review adds that control involvement depends on how goal-directed the task is (a-06). This warns against a single "critic" step.

**E7. Insight differs from analytic solving in the right temporal lobe and in brain state before the problem.** Right anterior superior temporal gyrus activity was higher for insight solutions, with an EEG gamma burst about 0.3 s before the answer (a-13; fMRI n=13, EEG n=19). Activity before the problem appeared predicted later insight versus analytic solving (a-14, b-06), and an alpha-dominant state was held longer in insight trials (b-08). Same lab family, small samples, and several lines are snippets (b-07, b-08, a-15). Treat as moderate. One alpha finding has no found replication (c-19, snippet).

**E8. Unconscious thought theory ("decide after distraction") fails to replicate.** A replication of N=399 found no advantage, with a Bayes factor of 7.83 for the null (c-01). A meta-analysis of 61 effect sizes shrank from g=0.15 to g=0.018 after bias correction (c-02). A second replication in deception detection also favored the null (c-03). This is the strongest negative result in the set.

**E9. Intrinsic LLM self-correction without outside feedback can lower reasoning accuracy.** Huang et al. found this on reasoning tasks (c-22). Lu et al. found no gain from self-correction or tree search for creativity in code generation (b-19). This matches our always-doubt losses on single-answer tasks [ours].

## 3. Single-source and contested findings

### 3a. Contested

**C1. Incubation size.** The earlier files disagreed (0.41 versus 0.29). The CHECK line resolves it from the primary paper: 117 effect sizes from 29 publications and 3,606 people, weighted random-effects mean d = 0.29, 95% CI 0.21 to 0.39 (d-01, d-03). The 0.41 is the unweighted mean (d-02), so a-16 and its CI of 0.28 to 0.54 should not be quoted as the headline. Use 0.29. It is a small effect. Subgroup means were 0.22 for linguistic insight (65 studies), 0.26 for visual (35) and 0.29 for creative tasks (only 14 studies) (d-04).

**C2. Incubation helps creative tasks more than insight tasks, and helps more after long preparation.** Supported by the regression in the primary paper (a-17, d-05, d-04), but the raw subgroup gap is small (d-04). A divergent mean of .65 quoted in a secondary source is not in the primary paper (d-05). Single meta-analysis.

**C3. An undemanding break task beats rest.** Per the primary paper, this holds only for linguistic insight problems (difference 0.45, p<.05); the high-versus-low demand difference pointed the same way but was not significant (d-06). So it is a moderator for one problem class, not a general rule. Gilhooly reports another study with no effect of break demand or length (c-05).

**C4. Mind wandering during a break raises originality (Baird 2012).** In 145 people, only an undemanding task raised Unusual Uses originality, and only on problems seen before the break (a-19). The effect was in originality, not fluency (a-20). The authors note the Remote Associates Task gives inconsistent incubation effects (a-21). Later work leans against replication: n=85 found no mind-wandering effect (d-07), and a preregistered study found no difference between break tasks, with a link between mind wandering and gains only when the prompt was reused (d-08). Verdict: contested, leaning not replicated (d-09, b-11 snippet).

**C5. Mechanism of incubation.** Evidence argues against secret unconscious work on the problem (c-06). Thoughts about the target during the break did not predict later performance (c-08). The default-plus-executive mixing idea is speculation (a-22). Mechanism is open (c-07: unconscious-work accounts are untested for knowledge-lean problems).

**C6. Does the aha feeling signal a correct answer?** Mixed (d-15). It raised belief in unrelated true and false statements in a preregistered study of 300 (b-12, snippet). It can be induced falsely, and warnings reduce but do not prevent that (d-14, snippet). But it predicted accuracy on problems needing implicit processing (d-12, b-13) and was highest for solutions with a correct first move (d-13). Not a clean contradiction, and not a reliable correctness signal.

### 3b. Single-source

- **S1. Generation and evaluation are different modes.** Evaluation recruits control more than generation (a-03, poets; a-04, art students). Two small studies reported through one review. The split is not clean in time (c-13).
- **S2. Connectome models predict creative ability only weakly, and shrink outside the discovery sample.** r about 0.30 inside, 0.35 and 0.28 in two small outside samples (a-08), but r 0.13 and 0.11 in 405 people (a-09). Useful as caution.
- **S3. Most "insight" problems are solved analytically; impasse is about 8%.** One study of 115 (c-09, c-10: divergent thinking explained about 2% of variance). Direction is supported by an independent lab (d-10, d-11); the 8% figure stays unverified. Dual-task costs are not unique to insight (c-11).
- **S4. 40 Hz tACS over the right temporal lobe raised verbal insight accuracy by about 19-20%** (b-09, n=31 crossover). No transfer to agents.
- **S5. Deliberate, not spontaneous, mind wandering predicts creativity.** Trait questionnaire, n=77, snippet (c-20).
- **S6. People favor feasible, typical ideas when selecting, and originality correlates negatively with feasibility.** Snippet of a secondary summary (c-21).

## 4. Mechanisms an agent can run

Every mechanism needs an equal-token test against the plain model. Our data say forced divergence helped open tasks (NoveltyBench distinct answers 3.18 to 9.63; architecture search 7% lower perplexity) and hurt single-answer tasks (ARC plain 4/10 versus scaffold 2/8; word puzzles about 92% versus about 75%) [ours]. Samples from one model are correlated, so agreement is weak evidence [ours].

**M1. Loose generator, then separate controller.**
- Trigger: open-ended task with no single right answer, or an objective check that can prune.
- Action: Call 1 writes many candidates with no judging, the obvious one first. Call 2, with a different prompt and the task goal, filters and edits them.
- Check: against the plain model at equal tokens, measure distinct answers and judged quality on a held-out open set. Also run a variant where one call does both.
- Evidence: a-01, a-02, a-10, a-12, b-04; human generate-then-evaluate split a-03, a-04 (single-source, S1); LLM two-phase prompt preprints b-18 and d-16 (abstract only; about 1.6 times as many distinct high-utility tasks in d-16).
- Risk: on single-answer tasks the first natural answer is usually right [ours], so the loose phase wastes tokens. Neuroscience says control depends on how goal-directed the task is (a-06) but gives no rule for choosing the mode. The router must come from our own measurements. Also c-13: the split is blurry, so do not expect a clean win.

**M2. Switch step before control.**
- Trigger: M1 is active and the first candidates cluster around one idea.
- Action: a short step that forces a move away from the current cluster (a different frame or source domain) before the controller reads anything.
- Check: compare distinct-cluster count with and without the step, at equal tokens.
- Evidence: a-05, b-03, a-25 (same lab, weak independence).
- Risk: this is a loose analogy. It is the same as forced divergence, which already hurts single-answer tasks [ours]. Fires only in M1 mode.

**M3. Pair association with a control step, and keep the control part split.**
- Trigger: designing the critic role.
- Action: use several narrow critics (does it meet the goal? is it feasible? is it new?) rather than one "judge".
- Check: one broad critic versus the split critics, same tokens, scored on a pruning task with an objective answer such as the architecture run.
- Evidence: a-12 (inhibition and updating matter, shifting does not), c-16, c-17 (control is several networks).
- Risk: more calls. Evaluator design matters and a smaller in-loop scorer scored higher in one preprint (d-17, abstract). LLM raters favored AI-made answers until elaboration was controlled (d-18, preprint), so same-model judges may be biased toward their own style.

**M4. Longer divergent runs, later items count.**
- Trigger: open task where the first ten ideas are all common.
- Action: keep sampling in one running list, and keep the later items for the controller.
- Check: compare originality of items 1-10 versus 11-30 within one context, and versus the same count from independent calls.
- Evidence: human serial-order effect a-11, b-15 (established for humans). For LLMs unverified (d-21; b-21 is an unopened preprint, credibility 35).
- Risk: samples from one model are correlated [ours], and a repeating list may collapse into one theme. The independent-calls arm of the test settles this.

**M5. No built-in "felt aha" trust.**
- Trigger: any step where the model reports a sudden "I see it" or high confidence after a reframe.
- Action: treat a sudden reframe as a hypothesis, and run the real check (examples, tests) before accepting it.
- Check: compare accuracy when such reframes are accepted outright versus when checked, at equal tokens.
- Evidence: b-12, d-14 (aha can mislead); d-12, d-13 (it also tracks correctness in some cases, so mixed, d-15); e9 for self-correction without feedback (c-22).
- Risk: checking costs tokens when the first answer was right. This is consistent with our "trust the first answer until a check fails" principle, so low risk.

**M6. Do not add incubation or "sleep on it" steps until tested.**
- Trigger: temptation to add a delay, a distractor call, or a second look after an unrelated task.
- Action: none. Record as a negative design rule.
- Check: if tested later, a break call that does an unrelated task versus a repeat of the same call, equal tokens, open-ended tasks only.
- Evidence: effect is small, d = 0.29 (d-01), mechanism unclear (c-06, a-22), main supporting experiment not replicated (d-07, d-08, d-09), and unconscious thought theory fails (c-01, c-02, c-03).
- Risk: model calls have no covert processing between them, so the human mechanism is absent (section 6). The most likely gain is just resampling.

**M7. Gate on task type; keep the plain path for single-answer tasks.**
- Trigger: every task.
- Action: probe, then route. Open tasks go to M1 to M4. Single-answer tasks with a check go to a convergent path.
- Check: the gate must not lose to plain by more than 1 point on BrainTeaser and must keep at least 9 distinct of 10 on NoveltyBench (00_PLAN.md gates).
- Evidence: the field supports a split between divergent and insight processes (a-24, a-23) and says insight problems are mostly solved analytically (c-09, c-10, d-10; single-source). The routing rule itself comes from our data, not this field.
- Risk: misrouting. No study here tests a router.

## 5. Evidence on LLMs and AI agents

- Intrinsic self-correction without outside feedback can lower accuracy (c-22), and self-correction and search gave no creativity gain in code (b-19). Both agree with our results [ours].
- Two-phase prompts that separate free exploration from constraint satisfaction raised diversity and novelty (b-18, abstract only, no numbers on the page; d-16, abstract, about 1.6 times as many distinct high-utility tasks). Both are preprints from the same group.
- Iterative generate-and-select with an LLM scorer reached human-benchmark creativity on recipes, but more iterations alone did not help, and a smaller scorer gave higher scores (d-17, preprint, abstract).
- Evolutionary persona diversification raised Alternative Uses response diversity by 78.8% and originality by 26.1% (d-22, snippet, credibility 45).
- LLM raters scored AI-made answers higher across 4,813 responses, and the bias vanished once elaboration was controlled (d-18, preprint, fetched). The evidence does not show LLM judges match humans on novelty (d-23).
- A 14-model evaluation found no clear creative gains over 18 to 24 months and only 0.28% of responses in the top 10% of human benchmarks (d-19, snippet).
- LLM help raised creativity during use but may hurt later unassisted creativity in 1,100 people (b-20). This concerns users, not agent design.
- fMRI of 170 people against LLMs of 270M to 72B parameters: alignment with the default network rises with model size and with idea originality (b-16); a reasoning-trained variant showed the opposite pattern (b-17). Preprint, speculative; d-20 notes it does not report a serial-order gain.
- No study was found that tests incubation, mind wandering or an aha moment as a deliberate step in an LLM agent loop (b-22). The serial-order effect in LLMs is unverified (d-21).

## 6. What does not transfer to a model

- Brain imaging results (network coupling, gamma bursts, alpha states, tACS) have no agent step. They are correlational even in humans (c-12, c-15, c-18, a-13, b-09).
- Incubation depends on a mind that keeps running between attempts. Model calls hold no hidden process between them, and the human mechanism is itself unsettled (c-06, c-08, a-22).
- The default network "retrieves from long-term memory" (a-02). A model's weights are not episodic memory, and even in people the memory account is speculative (c-14).
- Insight as a rare impasse-and-restructure event may be uncommon (c-09, single-source), so a step built around it has a narrow target.
- Individual-difference findings (fluid intelligence flattening the serial-order rise, a-11) describe people, not a single model.
- Results come from small specialised samples such as poets, pianists and art students (c-15).

## 7. Open questions

1. Does a later-is-more-original effect appear in LLM sampling, in one context and across independent calls? Needs a direct test in our harness (d-21).
2. Which task features should route to divergent mode? The field says control depends on goal-directedness (a-06) but gives no rule.
3. How do good thinkers evaluate ideas? Almost nothing here (a-07 lists it as open; c-21 is a snippet).
4. Do same-model judges prefer their own style, and does elaboration length explain it (d-18, d-23)?
5. Is the incubation mechanism resampling, a change of context, or something else? A break-call test could separate them (c-06, a-22).
6. Do experts and novices differ in when to diverge? Not covered by this evidence.
7. Is the 8% impasse figure real (c-09, d-11)? If it is, then doubt on schedule is wrong for most problems, which agrees with our results.

## 8. References

1. Beaty, Benedek, Silvia, Schacter (2016). Creative cognition and brain network dynamics. Trends in Cognitive Sciences 20(2):87-95. https://pubmed.ncbi.nlm.nih.gov/26553223/ (also PMC4724474). Checked: fetched. Ids: a-01 to a-07, c-12 to c-15.
2. Beaty, Kenett, Christensen, Rosenberg, et al. (2018). Robust prediction of individual creative ability from brain functional connectivity. PNAS 115(5):1087-1092. https://pmc.ncbi.nlm.nih.gov/articles/PMC5798342. Checked: fetched. Ids: a-08, a-09, b-01, b-02.
3. Beaty, Silvia, Nusbaum, Jauk, Benedek (2014). The roles of associative and executive processes in creative cognition. Memory & Cognition. https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/c/122043/files/2020/08/2014_Beaty_MemCogn.pdf. Checked: fetched. Ids: a-10, a-11.
4. Benedek, Jauk, Sommer, Arendasy, Neubauer (2014). Intelligence, creativity, and cognitive control. Intelligence 46:73-83. https://pmc.ncbi.nlm.nih.gov/articles/PMC4175011/. Checked: fetched. Id: a-12.
5. Jung-Beeman, Bowden, Kounios, et al. (2004). Neural activity when people solve verbal problems with insight. PLoS Biology 2(4):e111. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC387276/. Checked: fetched. Id: a-13.
6. Kounios, Frymiare, Bowden, Fleck, Subramaniam, Parrish, Jung-Beeman (2006). The prepared mind. Psychological Science 17(10):882-890. https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01798.x/ and preprint https://conference.nber.org/confer/2006/ICCs06/kounios.pdf. Checked: abstract (a-14), snippet (b-06).
7. Kounios, Beeman (2014). The cognitive neuroscience of insight. Annual Review of Psychology 65:71-93. https://pubmed.ncbi.nlm.nih.gov/24405359/. Checked: snippet. Id: a-15.
8. Sio, Ormerod (2009). Does incubation enhance problem solving? A meta-analytic review. Psychological Bulletin 135(1):94-120. https://www.gwern.net/doc/psychology/writing/2009-sio.pdf. Checked: fetched. Ids: a-16 to a-18, d-01 to d-06 (b-10 is a snippet of the same work at https://pmc.ncbi.nlm.nih.gov/articles/pmc3990058).
9. Baird, Smallwood, Mrazek, Kam, Franklin, Schooler (2012). Inspired by distraction. Psychological Science 23(10):1117-1122. https://www.cmhp.ucsb.edu/sites/default/files/2018-12/Baird%20et%20al.%20%282012%29%20Inspired%20by%20distraction.pdf. Checked: fetched. Ids: a-19 to a-22, c-08.
10. Cogdell-Brooke, Sowden, Violante, Thompson (2020). A meta-analysis of functional magnetic resonance imaging studies of divergent thinking. Human Brain Mapping. https://pmc.ncbi.nlm.nih.gov/articles/PMC7643395. Checked: fetched. Id: a-23.
11. Kuang et al. (2022). Human Brain Mapping 43(16):4864-4885. Meta-analysis of divergent thinking and insight fMRI. https://pmc.ncbi.nlm.nih.gov/articles/PMC9582370. Checked: fetched. Id: a-24.
12. Beaty, Silvia, Benedek (2017). Brain networks underlying novel metaphor production. Brain and Cognition 111:163-170. https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/c/122043/files/2020/08/2017_Beaty_BrainCogn.pdf. Checked: fetched. Id: a-25.
13. Beaty, Benedek, Kaufman, Silvia (2015). Default and executive network coupling supports creative idea production. Scientific Reports 5:10964. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4472024/. Checked: snippet. Id: b-03.
14. Beaty, Kenett (2023). Associative thinking at the core of creativity. Trends in Cognitive Sciences 27(7). https://cris.biu.ac.il/en/publications/associative-thinking-at-the-core-of-creativity/. Checked: abstract. Id: b-04.
15. Beaty, Kenett, Hass, Schacter (2022). Thinking & Reasoning. https://cognitive-complexity.net.technion.ac.il/files/2022/10/Beaty-Kenett-Hass-Schacter-2022.pdf. Checked: snippet. Id: b-05.
16. Beeman, Kounios and colleagues (2008). Aha! The cognitive neuroscience of insight (Northwestern PDF). https://bpb-us-e1.wpmucdn.com/sites.northwestern.edu/dist/a/699/files/2015/11/Aha-The-cognitive-neuroscience-of-insight-2895xqe.pdf. Checked: snippet. Id: b-07.
17. Yu, Oh, Kounios, Beeman (2022). NeuroImage. https://doaj.org/article/5bf717ee61784f57a3bdfe77c760e8bb. Checked: snippet. Id: b-08.
18. Santarnecchi, Sprugnoli, Bricolo, Costantini, et al. (2019). Scientific Reports 9:5778. https://pmc.ncbi.nlm.nih.gov/articles/PMC6453961. Checked: fetched. Id: b-09.
19. Review in PMC on mind wandering and incubation (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9053813/. Checked: snippet. Id: b-11.
20. Laukkonen, Kaveladze, Tangen, Schooler (2020). Cognition. https://www.Gwern.net/doc/psychology/cognitive-bias/illusion-of-depth/2020-laukkonen.pdf. Checked: snippet. Id: b-12.
21. Laukkonen, Ingledew, Grimmer, Schooler, Tangen (2021). Getting a grip on insight. Cognition and Emotion 35(5):918-935. https://doi.org/10.1080/02699931.2021.1908230 (also https://research.vu.nl/en/publications/getting-a-grip-on-insight-real-time-and-embodied-aha-experiences-/). Checked: abstract (d-12), snippet (b-13).
22. Laukkonen, Schooler, Tangen (2018). The eureka heuristic (preprint). https://labs.psych.ucsb.edu/schooler/jonathan/sites/labs.psych.ucsb.edu.schooler.jonathan/files/pubs/eurekaheuristic_preprint_laukkonenschoolertangen_2018-2.pdf. Checked: snippet. Id: b-14.
23. Beaty, Johnson (2021). Automating creativity assessment with SemDis. Behavior Research Methods. https://link.springer.com/10.3758/s13428-020-01453-w. Checked: abstract. Id: b-15.
24. Ismayilzada, Luchini, Gokce, AlKhamissi, et al. (2026). arXiv 2604.03480 (preprint, under review). https://arxiv.org/abs/2604.03480v1. Checked: fetched (b-16, b-17), abstract (d-20).
25. Nguyen, Singla (2025) and Nguyen, Tschiatschek, Singla (CreativeDC). arXiv 2512.23601 (preprint). https://arxiv.org/abs/2512.23601. Checked: abstract. Ids: b-18, d-16.
26. Lu, Wang, Li, Jiang, Khudanpur, Jiang, et al. (2025). arXiv 2407.09007 (NAACL 2025 per a search result). https://arxiv.org/abs/2407.09007. Checked: fetched. Id: b-19.
27. Kumar, Vincentius, Jordan, Anderson (2025). CHI 2025, arXiv 2410.03703. https://arxiv.org/abs/2410.03703. Checked: fetched. Id: b-20.
28. Unknown authors (2026). Preprints.org 202609.2250 (serial order in LLMs). https://www.preprints.org/manuscript/202609.2250. Checked: snippet only, not opened. Id: b-21.
29. Nobrega (2026). TACIT. arXiv 2602.07061 (preprint). https://arxiv.org/pdf/2602.07061. Checked: snippet. Id: b-22.
30. Nieuwenstein, Wierenga, Morey, Wicherts, et al. (2015). On making the right choice: a meta-analysis and large-scale replication attempt of the unconscious thought advantage. Judgment and Decision Making 10(1). https://dlab.sauder.ubc.ca/sjdm/journal/14/14321/jdm14321.html. Checked: fetched. Ids: c-01, c-02.
31. Wu, Mei, Yan (2019). Frontiers in Psychology. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.00893/full. Checked: fetched. Id: c-03.
32. Gilhooly (2016). Frontiers in Psychology 7:1076. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01076/full (also PMC4956660). Checked: fetched. Ids: c-04 to c-08.
33. Salmon-Mordekovich, Leikin (2023). Psychological Research 87(6):1995-2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC10366031 and https://doi.org/10.1007/s00426-022-01786-5. Checked: fetched (c-09 to c-11), abstract (d-10, d-11).
34. Beaty, Cortes, Zeitlen, Weinberger, Green, et al. (2021). Cerebral Cortex 31(10). https://pure.psu.edu/en/publications/functional-realignment-of-frontoparietal-subnetworks-during-diver/. Checked: fetched. Ids: c-16, c-17.
35. Dietrich, Kanso (2010). Psychological Bulletin, as quoted in a Frontiers article. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00215/full. Checked: fetched (secondary quote). Id: c-18.
36. Kounios, Jung-Beeman, as reported by NSF (2009). https://www.nsf.gov/news/what-happens-when-aha-strikes. Checked: snippet. Id: c-19.
37. Agnoli et al. (2018). Journal not confirmed. https://flore.unifi.it/bitstream/2158/1100326/2/Agnoli%20et%20al%202018.pdf. Checked: snippet. Id: c-20.
38. Nijstad et al. (as summarized in a secondary source). arXiv 1409.2207. https://arxiv.org/pdf/1409.2207. Checked: snippet. Id: c-21.
39. Huang, Chen, Mishra, Zheng, Yu, Song, Zhou (2023). Large language models cannot self-correct reasoning yet. arXiv 2310.01798 (ICLR 2024). https://arxiv.org/abs/2310.01798. Checked: fetched. Id: c-22.
40. Du, Gordon, Tolmie (2025). Brain Sciences 15(6):595. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12190454/. Checked: fetched. Id: d-07.
41. McDaniel, Habibi, Kaplan (2025). Scientific Reports 15:24629. https://doi.org/10.1038/s41598-025-09736-y. Checked: abstract. Id: d-08, d-09.
42. Wiley, Miller (2026). Journal of Intelligence 14(9):198. https://doi.org/10.3390/jintelligence14090198. Checked: abstract. Id: d-13.
43. Grimmer, Tangen, Freydenzon, et al. (2023). Cognition and Emotion 37(2):329-338. https://doi.org/10.1080/02699931.2023.2187352. Checked: snippet. Id: d-14.
44. Anderson, Verhoef, Zohrehvand, et al. (2026). arXiv 2608.07243 (preprint). https://arxiv.org/abs/2608.07243. Checked: abstract. Id: d-17.
45. Domanti, Mock, Agnoli, De Angelis, et al. (2026). arXiv 2604.20569 (preprint). https://arxiv.org/abs/2604.20569. Checked: fetched. Ids: d-18, d-23.
46. Haase, Hanel, Pokutta (2025). arXiv 2504.12320 (preprint). https://arxiv.org/abs/2504.12320. Checked: snippet. Id: d-19.
47. Moon, Cho, Borrajo, Ganesh, et al. (2026). arXiv 2609.30492 (preprint). https://arxiv.org/abs/2609.30492. Checked: snippet. Id: d-22.
48. arXiv API search for LLM serial-order effects (2026). Zero relevant entries. http://export.arxiv.org/api/query?search_query=all:%22serial+order%22+AND+all:%22language+models%22+AND+all:creativity. Checked: fetched. Id: d-21.
