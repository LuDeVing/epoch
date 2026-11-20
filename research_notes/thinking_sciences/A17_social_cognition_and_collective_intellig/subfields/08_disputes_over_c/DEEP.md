# Disputes over c: deep document

*Scope: the dispute over the collective intelligence factor c in human groups, and the first tests of a c-like factor in LLM agent groups. Evidence ids (a01 to d19) refer to evidence_a-d.jsonl; claim ids (K01 to K25) refer to claims.jsonl, both in this folder. The sibling document on the factor itself is `../07_collective_intelligence_factor_c/DEEP.md`; do not repeat it. Links: consensus and premature agreement (`../05_*`); team science and coordination subfields run in parallel.*

## 1. What it is

c is a statistical factor. Woolley et al. (2010) gave groups several different tasks. Scores on the tasks correlated positively. One factor carried about 43% of the variance. They called it c, "collective intelligence", by analogy with g in individuals.

The dispute is about four questions.
1. Does one general factor exist across human groups, or is it an artefact of task choice, effort and nesting?
2. How much variance does it explain? The headline figure fell from 44% to 19.6% in one correction.
3. What causes it? Member IQ (Bates and Gupta), social sensitivity and turn-taking (Woolley, Engel), or collaboration process (Riedl)?
4. Is it a useful target? Does it predict new tasks, and can anyone raise it on purpose?

For our agent this is a warning. We build one language-model agent that thinks through a scaffold. A c-like score for agent groups is a correlation among task scores. It is not a mechanism and not a design target. Almost all human numbers come from one lab network. The LLM evidence is one team and one protocol.

Bottom line: a positive manifold among group task scores is common (95% of 171 correlations positive). The factor is weak to moderate (about 20 to 43% depending on the metric). It predicts held-out tasks at r about .26 to .40. Its causes are contested. No randomised study raised c and showed transfer.

## 2. History and theories in depth

**2010, the founding claim (a01 to a06).** Woolley, Chabris, Pentland, Hashmi, Malone, Science. Two studies, 699 people, groups of 2 to 5.
- Study 1: 40 groups of 3, up to 5 hours of work, tasks from the McGrath circumplex plus a criterion task. Mean inter-task r = .28. First eigenvalue over 43%, second 18%. One-factor CFA chi2 = 1.66, df = 5, P = .89.
- Study 2: 152 groups of 2 to 5, new tasks. First factor 44%, second 20%. CFA chi2 = 5.85, df = 5, CFI .98, RMSEA .03. Parallel analysis kept one factor. Same lab, so not an independent replication.
- c predicted a criterion task (Study 1 b = .51; Study 2 b = .36). Mean member IQ added little (b = .08 and .05).
- Individual IQ predicted c only weakly: mean r = .15, max r = .19. This made c look like a new group property.
- Claimed correlates: social sensitivity (Reading the Mind in the Eyes, RME), even turn-taking, share of women (r = .23, mostly mediated by RME). Cohesion, motivation and satisfaction did not predict c.
- Weak spot (a06): the comparison with individual g (30 to 50% first-factor share) is loose. Factor share depends on the number and similarity of tasks. 5 to 10 tasks cannot be compared with a 100-item test.

**2014, same-lab extension (a16, a17).** Engel et al., 68 groups, face-to-face or online text. First factor 49% and 41%. RME predicted c at r = .53 (face-to-face) and .55 (online). More total communication went with higher c; uneven contribution with lower c.

**2016, first challenges.**
- Barlow and Dennis (a18, b12): 86 groups of 3 to 5, text chat, four tasks. Mean inter-task r = -0.05. The authors read it as no factor. Rowe's computation from the same data gives a first factor of 42% with 50% of correlations positive. These are different outputs of the same data: a plain eigenvalue share is high even with near-zero correlations in small samples. Read "no factor" as the authors' view and "42%" as Rowe's.
- Bates and Gupta (a13 to a15): an independent replication in Edinburgh and Chennai. Three studies, 312 people. A group factor appeared (Study 1: 39.8% of variance, 72 people in 26 groups of 2 to 4; Study 2: about 50%). But individual IQ explained it. Study 1 R2 = 57%, IQ beta = .76 [.4, 1.12]; RME beta = -.11 (ns); proportion female beta = .12 (ns). In the joint model of Studies 2 and 3 RME had no effect on the latent factor. Group-IQ and average individual IQ were called indistinguishable. Authors: group tests would be redundant. Woolley's side answered that an unmeasured moderator must exist.

**2017, Credé and Howardson (a19, b08, d10).** Reanalysis of six samples. Conclusion: the data do not support one general factor across wide task sets. They argued low effort and nesting (tasks within groups) inflate positive correlations. Rowe's coding finds support for a factor in 5 of 6. Only press accounts were read here; no per-sample first-factor values were obtained (K25). The 2018 reply by Woolley, Kim and Malone was seen as metadata only (a21, c07, d11).

**2019, Graf, Gimpel, Barlow (d12).** 13 studies in 6 papers, 745 teams, only 5 of 8 McGrath task types. Pooled task correlations ran from -0.17 to +0.17, mean r = .001. One-factor CFA: chi2 = 40.79, df = 5, CFI .73, TLI .45, RMSEA .10. First eigenvalue 1.05 (cut 1.38), 17% of variance, second 15%. Parallel analysis points to three factors. Stricter than Rowe, but it pools face-to-face and online matrices and is a work-in-progress report.

**2021, Riedl et al., PNAS (a07 to a12, c01).** 22 studies on one platform (POGS), 5,279 individuals, 1,356 groups, group sizes 2 to 7, 8 task types, 3 in every study (Brainstorm Object, Typing Text, Unscramble Words). Mean inter-task r = .27 (.12 to .50). Loadings .27 to .52. Leave-one-task-out prediction r = .40 [.26, .53]. One SD more CI went with about 18% (plus or minus 12%) better task performance. Random forests: collaboration process (skill congruence, strategy, effort) ranked above individual skill, above group size and composition. For Sudoku individual skill was over 51%; for Unscramble 55% was process. The paper names critics and blames task choice and rules that limit who can enter an answer. This was not independently tested (a12).

**2022 correction (a09, b07, c02).** PNAS 119(19):e2204380119. A software error made average variance extracted (AVE) wrong. 44% became 19.6%. Loadings stayed at .27 to .52. SI fit changed. Model 1 (3 tasks) is saturated (0 df, fit uninformative). Model 2 (5 tasks): chi2(5) = 19.51, CFI .93, RMSEA .046 [.026, .069]. Model 4 (8 tasks): chi2(20, N = 1,356) = 93.28, CFI .833, RMSEA .052 [.042, .063]. The authors say all models still support one factor. The brief's "V via Wikipedia" note was not found in the main text (c23).

**2021, Rowe, Hattie, Hester meta-analysis (b01 to b05, b12, b13, c03, c04).** The best neutral summary. See section 3.

**2024 to 2025, structure and sub-structure.** Rowe 2024 (N = 85, two-factor fit, fluid and crystallised; d14). Kommol, Riedl, Woolley 2025 preprint on the same 22 studies: a hierarchical three-factor model (memory, attention, reasoning) fits best, mostly in established groups (b17, d13). Fit indices were not read. A 2025 dyad study (105 dyads) found social sensitivity beta fell from .39 to .22 once intelligence and confidence entered (b15, b16).

**2024 to 2026, LLM groups.** Zhou et al. (ACL Findings 2026) test an Artificial Collective Intelligence (ACI) factor. Ilic and Gignac (2024) find a general factor across individual LLMs (model-level, not group). Riedl (2025/26) tests coordination with information theory. See section 6.

**Competing explanations of the same positive manifold.**
- Member IQ (Bates and Gupta).
- Shared task format and effort: low effort or fatigue lifts all scores together (Credé).
- Nesting: scores from one group on several tasks share group-level noise.
- Process and skill congruence (Riedl).
- A multi-factor structure with a weak general factor on top (Graf, Rowe 2024, Kommol).
- For LLM groups: base-model strength shared across tasks (Zhou's own limitation, b22).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| One factor in Woolley Study 1 | 40 groups of 3; mean r .28; first factor over 43%, second 18%; CFA chi2 1.66, df 5, P .89 | Woolley 2010 (a02) | Observed; small N |
| One factor in Woolley Study 2 | 152 groups; first 44%, second 20%; CFI .98, RMSEA .03 | Woolley 2010 (a03) | Same lab, not independent |
| Positive manifold across studies | 163 of 171 inter-task correlations positive (95%); 59% between 0 and .30; mean first factor 43.03% over 19 samples | Rowe 2021 (b05, b13) | Established (K01) |
| Variance explained depends on metric | Eigenvalue share about 43%; AVE mean 30.23% over 49 loadings; Riedl corrected AVE 19.6% | Rowe 2021; Riedl correction (b03, c02) | Established (K02) |
| Riedl AVE correction | 44% to 19.6%; loadings .27 to .52 unchanged; 0.52 squared = .27, so 44% was impossible | Correction 2022 (a09) | Established (K03) |
| Fit of the Riedl models | 3-task saturated; 5-task CFI .93, RMSEA .046; 8-task CFI .833, RMSEA .052 | Correction SI (c02) | Established |
| External validity, meta | c to criterion task r = .26 (CI .10 to .40); 8 samples, 857 groups; Q(8) = 59.36; I2 = 86.5%; tau2 = .05 | Rowe 2021 (b01) | Established (K04) |
| External validity, leave-one-task-out | r = .40 [.26, .53]; 1 SD more CI = about 18% (plus or minus 12%) better performance | Riedl 2021 (a10) | Established |
| Power | About 80% of studies underpowered; 84 to 782 groups needed for r = .30 to .10 | Rowe 2021 (b02) | Single-source (K10) |
| Member IQ and c | Woolley: mean r .15, max .19. Rowe pooled .19 (5 samples); independent labs .32, Woolley-affiliated .10. Bates and Gupta: beta .76, R2 57% | a04, b04, a14 | Contested (K05) |
| Lab dependence | Only 7 of 19 Rowe samples independent of Woolley; 12 Woolley-affiliated | Rowe 2021 (b04) | Single-source (K09) |
| Social sensitivity | Engel r .53 and .55 (68 groups); Bates and Gupta: no effect on latent factor; dyads beta .39 to .22 | a17, a15, b15 | Contested (K06) |
| Turn-taking | Not supported in Bates and Gupta (3 studies) or dyad study (beta .08 ns) | a17, b10, b15 | Contested (K07) |
| No factor, small battery | Barlow and Dennis: 86 groups, 4 tasks, mean r -.05 (authors); first factor 42% by Rowe | a18, b12 | Contested (K08) |
| Pooled structure | Graf 2019: 745 teams, mean r .001, CFI .73, first factor 17%, 3 factors by parallel analysis | d12 | Contested (K08, K11) |
| Hierarchical structure | Kommol 2025: 22 studies, three-factor best; Rowe 2024 N = 85 two-factor | b17, d13, d14 | Contested; abstracts only (K11) |
| What predicts c | Process (skill congruence, strategy, effort) top overall; Sudoku over 51% individual skill; Unscramble 55% process | Riedl 2021 (a11) | Single-source (K12) |
| LLM group factor | 108 groups, 8 LLMs, 5 tasks; mean r .55 (human .28); first 66.3%, second 18.7%; CFI .967 | Zhou 2026 (a22, b19) | Single-source (K13) |
| LLM factor predictors | Skill congruence over 50%; mean member ability 37%; size, max ability, effort each under 5% | Zhou 2026 (a24) | Single-source (K14) |
| Cost and ACI | The cheaper centralized group had ACI 9.7% higher than the group costing 75% more with stronger LLMs | Zhou 2026 (b20) | Single-source |
| ACI plug-in gains | 1.1% to 12.3%, mean 4.6% on unseen tasks; one run per cell, no CIs | Zhou 2026 (a25, d09) | Single-source (K15) |
| Model-level g | 591 LLMs, 12 tests; general factor 65.6%; mean loading .81; chi2(44) = 250.42; CFI .984; RMSEA .089 | Ilic and Gignac 2024 (b18, c14) | Established (K16) |
| Social prompts no help | GPT-4.1, N = 10, 200 runs per condition, no significant difference; per extra agent OR .92; +1 temperature OR 1.50; 7,150 runs | Riedl 2025/26 (a26, c12) | Single-source (K17) |
| Debate vs single agent | Smit 2024 MedQA: single .60, Society of Mind .64, Multi-Persona .58; GPQA single .33 vs SoM .27. Zhang 2025: CoT mean 72.5 vs heterogeneous SoM 76.7 | c15 to c18 | Contested (K18) |
| Debate at equal budget | See section 6 | d01 to d05 | Contested (K18) |
| Hidden-profile failure | GPT-4.1 .233 post-discussion vs .733 full information (30 sessions, p < .001); humans .385 vs .604 (8 sessions); 65 tasks | HiddenBench (c19) | Single-source (K19) |
| Disclosure fix | Reveal-All .967 vs .233; secretary .100; one adversarial agent .492; share-everything prompt .467; group of 7 gains +.006 vs +.348 at 3 | HiddenBench v3 (d06, d07) | Single-source (K22) |
| Debate failure modes | Conformity up to 85.5%; 70.0% of correct answers destabilised; oracle gap up to 32.3 pp; 2.1 to 3.4 times tokens | Bertalanic 2026 (d04) | Established (K23) |
| No raised-c intervention | Woolley 2022: 146 teams, synchrony effect on CI B = .09, p = .249; McDonald 2026 feedback did not help; Gupta 2024 nudges mixed | d15 to d17 | Single-source (K20) |

## 4. Mechanisms and models

This section says how each model works, so an engineer can rebuild the analysis on agent data.

**4.1 The factor model.** Collect scores of G groups (or agent configurations) on T tasks. Build the T by T correlation matrix. Fit a one-factor confirmatory model: score_t = loading_t * c + error_t. Report four things, never one.
- Mean inter-task correlation and the share of positive correlations.
- First-eigenvalue share of the correlation matrix (plain eigen-decomposition). This is the "43%" type number.
- Average variance extracted: the mean of squared standardized loadings. This is the "19.6%" type number. With loadings of .27 to .52, squared loadings run from about .07 to .27, so the mean must be below .27. A 44% AVE is impossible with those loadings. Use this as a sanity check: AVE can never exceed the largest squared loading.
- Fit: CFI and RMSEA, plus parallel analysis for the number of factors (Woolley used a cut of 1.38 for 5 to 10 tasks). A model with 3 indicators is saturated (0 df) and says nothing about fit.

**4.2 Leave-one-task-out validity.** For each task k, compute c from the other T-1 tasks (factor score or mean of z-scores), then correlate it with task k across groups. Riedl: mean r = .40. Rowe: criterion r = .26. This is the practical test of whether c is usable.

**4.3 Why a first factor can be spurious (the Credé line).**
- Nesting: each group yields several scores. Group-level noise (fatigue, a bad day, one strong member who works hard) raises all scores together.
- Few and similar tasks: with 4 to 5 tasks the first eigenvalue is large by chance. Barlow and Dennis show a first factor of 42% with mean r near zero.
- Shared base ability: if groups differ in member ability, every task score rises with it. This is the Bates and Gupta view for humans and Zhou's own caveat for LLM groups.
To separate these, compute the factor on individual members' scores on the same tasks and compare it with the group factor. For LLMs, run single agents and groups on the same battery. Zhou does not do this (K21).

**4.4 Predictor analysis.** Random forest or regression of the group factor on group features. Riedl and Zhou both found "skill congruence" on top. Caution: the indicator may be built from the same task skills, so the result may hold by construction (a24 limits).

**4.5 ACI plug-in (Zhou).** Fit ACI on 108 groups. Train a random forest from group features (size, rounds, topology, member ability, skill congruence) to ACI (R2 above 0.8 reported). Use predicted ACI as an extra objective when an optimiser (GPTSwarm, G-Designer) searches for a multi-agent design. Gains 1.1 to 12.3%, mean 4.6%. One run per cell; noise unknown.

**4.6 Hidden-profile protocol (HiddenBench).** Each agent holds some private facts plus shared facts. The group must pool facts to find the right answer. Metric: accuracy after discussion versus accuracy when one agent gets all facts. The Reveal-All ablation forces each agent to state all its private facts in round 1. It is an oracle upper bound and its cost is not reported.

**4.7 Information-theoretic coordination test (Riedl 2025/26).** Treat each agent's per-round output as a time series. Measure temporal synergy (the group predicts its own future better than its parts do) and coordinated alignment. Persona prompts gave identity-linked differentiation. Persona plus a "think about what others might do" prompt gave goal-directed complementarity. Success in the guessing game did not change significantly (200 runs per condition).

## 5. What holds up

**Holds up (established).**
- Positive correlations among group task scores are the norm: 163 of 171 positive. A first factor of about 30 to 43% by eigenvalue is common (K01).
- The factor is weak in strict terms: AVE 19.6 to 30%, loadings at most .52, 8-task fit CFI .833 (K02, K03).
- External validity is modest and heterogeneous: r = .26 (CI .10 to .40, I2 86.5%) and r = .40 leave-one-task-out (K04).
- Reports of the factor's variance must name the metric. Papers that mix eigenvalue share and AVE overstate (K02).
- A general factor exists across individual LLMs (65.6%), but pooled comparisons confound parameter count (K16).
- Debate failure modes at small scale (conformity, collapse, 2.1 to 3.4 times the tokens) are documented (K23).

**Contested.**
- Whether member IQ drives c: r = .15 to .19 (Woolley, Rowe pooled) versus beta = .76 (Bates and Gupta). Independent labs .32, Woolley labs .10. Older team meta-analyses pooled r = .28 for IQ and team performance, while Rowe finds .06 for the IQ-controlled subset against criterion tasks. No clean resolution (K05).
- Social sensitivity and turn-taking: strong in the originating lab, absent in the independent replication, weak in the 2025 dyad study (K06, K07).
- One factor, two or three: Graf 2019, Rowe 2024, Kommol 2025 (K11).
- Whether a factor exists at all on wide task sets: Credé versus Rowe's coding (K08).
- Multi-agent debate versus single agent at equal compute (K18).

**Failed or null results.**
- Barlow and Dennis 2016: no factor from four tasks in chat groups.
- Bates and Gupta: RME and turn-taking did not predict the latent factor.
- Persona and theory-of-mind prompts: no significant change in success (K17).
- McDonald 2026: live feedback did not raise performance; effort-only feedback hurt because teams neglected coordination (press summary only, d16).
- Gupta 2024 nudges (168 groups, search summary only): one skill-discussion nudge raised CI; other nudges lowered it (d17).
- Woolley 2022 randomised hierarchy: synchrony effect on CI not significant (B = .09, p = .249); effect conditional on gender mix (d15).
- No randomised intervention raised c and transferred to a held-out task (K20).

**Moderators.** Task type (Sudoku individual, Unscramble process). Group established or new (three-factor fit mostly in established groups). Online versus face-to-face (pooled in Graf). Battery size and similarity. Lab. Gender mix in the 2022 hierarchy study.

**Interventions that worked.** Only narrow ones: a nudge to discuss who has which skill and how to use it (Gupta 2024, unopened); skill congruence in group assembly (correlational). The practical lesson is to match skills to tasks, not to raise c.

## 6. Language models

**LLM group factor, Zhou et al. 2026 (a22 to a25, b19 to b22, d08, d09).**
- Design: 108 groups. Sizes 3, 5, 8; rounds 2 or 3; topologies decentralized, centralized, random; homogeneous or mixed LLMs. Eight LLMs: gpt-3.5-turbo, gpt-4o-mini, Qwen2.5 7B/32B/72B, GLM-4-9B, InternLM2.5-20B, Gemma-2-27B. Five tasks: commonsense, math, games, coding, writing. Single-model scores ranged 0.40 to 0.81.
- Result: mean inter-task r = .55 (human .28). First factor 66.3%, second 18.7%. CFA CFI .967. Leave-one-task-out: r above .8 on three tasks, about .5 on the rest.
- Predictors: skill congruence over 50%, mean individual ability 37%; group size, max ability, effort each under 5%. A fully connected network was no better than a centralized one with a strong agent at the hub.
- Cost: the dearer group (75% higher cost, stronger LLMs) had the lower ACI; the cheaper group was 9.7% higher.
- Plug-in: 1.1 to 12.3% gain, mean 4.6%, on unseen tasks.
- Limits: one team, one framework (Du et al. style debate), groups under 10, one run per cell, no CIs, only 5 tasks. The group factor cannot be separated from shared single-model ability, because the paper has no factor analysis of single-agent scores on the same tasks (K21). Some G-Designer table rows were mislabelled in the extracted text (d09); only the stated percentages were used. No independent replication found (d19).
- Reading: a stronger first factor than in humans (66% vs 43%) is what you would expect if base-model quality dominates. Do not read it as "LLM groups are more collectively intelligent".

**Model-level g, Ilic and Gignac 2024 (b18, c14).** 591 LLMs, 12 tests: general factor 65.6%, mean loading .81, chi2(44) = 250.42, CFI .984, RMSEA .089. Parameter count correlates with it with diminishing returns. It is pooled across models, so scale is confounded. For scaffold work, compare within one model.

**Coordination, Riedl 2025/26 (a26, c12, c13).** GPT-4.1, Llama-3.1 8B and 70B, Gemini 2.0 Flash and Qwen3 in a guessing game with no communication. Persona and persona plus ToM prompts changed coordination measures but not success (N = 10, 200 runs per condition). Each extra agent cut odds of success by about 8% (OR .92). One more temperature unit raised them by about 50% (OR 1.50; 7,150 runs). Sampling diversity helps; more agents do not.

**Debate versus single agent (K18).**

| Study | Setting | Result |
|---|---|---|
| Smit 2024 (c15, c16) | GPT-3.5, MedQA | Single .60, Society of Mind .64, Multi-Persona .58 |
| Smit 2024 | GPQA | Single .33 vs Society of Mind .27 |
| Zhang 2025 (c17, c18) | GPT-4o-mini, 9 datasets | Society of Mind below CoT on all nine; heterogeneous Society of Mind 76.7 vs CoT 72.5 |
| Wang 2024 (d01) | equal budget | Self-consistency beats debate; debate falls with more budget; answer entropy shrinks |
| Tran and Kiela 2026 (d02) | multi-hop, equal thinking tokens | Single agent matches or beats 5 multi-agent designs; avg .427 vs debate .420 at 100 tokens |
| Hu 2026 (d03) | protocol routing | Each protocol wins somewhere; oracle router +14 pp; vote entropy captures 11 to 19%; 66% of debate-helpful cases are unanimous but wrong |
| Bertalanic 2026 (d04) | small models | Debate uses 2.1 to 3.4 times the tokens for equal or lower accuracy; conformity up to 85.5%; 70.0% of correct answers destabilised; oracle gap up to 32.3 pp |
| Wunderlich 2026 (d05) | equal FLOPs, MMLU-Pro and BBH | Debate +1.3, mixture-of-agents +2.7 points over self-consistency (counter-evidence) |

Reading: debate rarely beats self-consistency at equal tokens. The one setting that helped was heterogeneous models. The equal-FLOPs counter-result shows the answer depends on how cost is counted. Our schema's G9 ("no debate") stays supported, but the claim is contested, not closed.

**Hidden profiles, HiddenBench (c19, c20, d06, d07).** 65 tasks. GPT-4.1 pre-discussion .008, post-discussion .233, full information .733. Humans .385 vs .604. Best model Gemini-2.5-Pro .671. Across 15 LLMs the v3 headline is 30.1% vs 80.7%. Only an extreme conflict prompt helped modestly. Ablations (GPT-4.1, 3 tasks): Reveal-All .967; passive secretary .100; one adversarial agent .492; "share everything" .467. A group of 7 gained +.006 vs +.348 at 3. Reading: the failure is disclosure, not reasoning. The oracle arm is an upper bound.

**Position paper.** Fan et al. 2026 (b24, abstract only) says LLM multi-agent work lacks a metric that separates collaboration gain from extra compute. This matches our G7.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not use any c-like composite as a design target or a score. Judge each scaffold element by held-out task accuracy at equal tokens. | G7 (already), G | [E] | K04, K20; a09, b01, a10 |
| When reporting any general factor from agent batteries, report eigenvalue share, AVE, CFI and RMSEA, and never quote one as the other. | memory (bench reporting rule) | [E] | K02, K03; a09, b03, c02 |
| Do not build on a factor from fewer than 5 tasks or from a saturated model; state which tasks are in the battery. | memory (bench reporting rule) | [E] | K03, K08; c02, a18, d12 |
| Report CIs and seeds on every agent comparison. Heterogeneity is high (I2 86.5%) and most human studies were underpowered. | G7, memory | [E] | K04, K10; b01, b02 |
| Keep G9 (no debate) as the default. If a debate-like operator is ever tested, log answer entropy per round and stop on collapse. | G9, O | [E] for failure modes | K23; d04, d01 |
| Compare any multi-agent variant against self-consistency at equal tokens, not against one sample. | G7, G9 | [E] | K18; d01 to d05 |
| Treat model-level g as scale-confounded; compare scaffolds within one model. | memory | [E] | K16; b18, c14 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Disclosure step: before any parallel-agent merge, each sub-agent lists its private facts in a structured form, and code merges them. Hidden-profile accuracy rose from .233 to .967 for Reveal-All (an oracle). | S3, S4, O | [S] | K19, K22; d06, d07 |
| Heterogeneous sampling (different models or temperatures) instead of more identical agents. OR 1.50 per temperature unit; heterogeneous Society of Mind beat CoT 76.7 vs 72.5. | S3 | [S] | K17, K18; c12, c18 |
| Task-dependent routing: apply a coordination or process step only where the task needs coordination (Unscramble 55% process vs Sudoku 51% individual skill). | G, S0 | [S] | K12; a11 |
| Skill-matched assignment of sub-roles (skill congruence over 50% of ACI importance); a strong agent at a hub beat full connectivity. | O, S0 | [S] | K14; a24 |
| Do not gate debate on self-agreement alone (66% of debate-helpful cases are unanimous but wrong). | G9, S6 | [S] | K24; d03 |
| Equal-speaking-turn rules in any dialogue operator: do not hard-code. | O | [C] | K07; a17, b10 |
| Social-framing or ToM prompts: do not assume help. | G | [S] | K17; a26, c12 |

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup cost counted, per G7). Report mean and 95% CI over at least 3 seeds.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Single-agent factor control | Battery of 6 or more task types (ARC-like, math with checker, code with tests, BrainTeaser, writing with rubric, forecasting) | Single agent 1 sample; single agent best-of-k; k-agent group; same battery, same models | First-eigenvalue share, AVE, CFI, parallel analysis for single vs group scores | If single-agent share is about the same as group share, the ACI factor is base-model ability (K21). Expect equal within about 10 points. |
| T2 Non-debate protocol factor | Same battery | Debate; majority vote; plan-and-merge; central hub with strong agent | Factor share per protocol; leave-one-task-out r | Tests whether the factor depends on the debate framework (gap 1). Expect lower r under vote. |
| T3 Disclosure step | Hidden-profile tasks (HiddenBench subset plus our own constructed ones with private facts) | Free discussion; Reveal-All forced listing; passive summariser; single agent with all facts | Accuracy after discussion | Reveal-All close to .9; summariser near baseline. Check tokens: Reveal-All may cost more. |
| T4 Debate vs self-consistency | MMLU-Pro subset, BBH subset, our bench items with checks | SC with k samples; debate 3 agents 2 rounds at the same total tokens; heterogeneous debate | Accuracy; answer entropy per round | Expect SC >= debate (K18). Heterogeneous debate may tie. |
| T5 Routing | Mixed items | Always SC; always debate; vote-entropy gate; oracle | Accuracy per token | Oracle +14 pp is an upper bound; gate recovers under 20% (K24). |
| T6 Task-dependent process step | Tasks where facts or skills are split across roles vs tasks with one solver | Process step on; off | Accuracy difference by task type | Gain only on split tasks (K12). |
| T7 Social-framing prompts | Guessing-game style and reasoning items | Plain; persona; persona plus ToM | Success rate, 200 runs per arm | No significant difference (K17). |
| T8 ACI-style gain vs noise | Unseen tasks | Design chosen by ACI objective; design chosen by held-out accuracy | Accuracy over seeds | Gain above seed noise is unknown; the 4.6% mean needs 3 or more seeds to judge. |

## 9. What does not transfer, and why

- Social sensitivity (RME), proportion female, turn-taking: these are properties of human members. An LLM has no stable theory-of-mind trait and no gender mix. The evidence is contested even in humans (K06, K07).
- Cohesion, motivation, satisfaction: not predictive in humans; no agent analogue.
- c as a trait of a group: for LLMs the "members" are copies or near copies of a few base models. Independence, which makes groups interesting, is mostly absent (G4).
- Human effort and fatigue artefacts (Credé): a different mechanism in LLM groups, but the same statistical problem (shared base ability) appears.
- Random-forest importances from human groups: the predictors are built from the same task skills and may hold by construction (a24 limits).
- Zhou's group sizes (3, 5, 8) and one debate protocol: our agent is a single scaffolded agent. Sub-agents in S3 are context-isolated samples, not a debating group.
- Short lab tasks with student samples: stakes and duration differ from our items.
- Model-version results (GPT-3.5, 4o-mini, 4.1) age fast.

## 10. Open questions

1. Does a c-like factor survive non-debate protocols with a cost-matched baseline? (gap 1)
2. How much of the LLM group factor is shared single-model ability? Needs single-agent versus group factor analysis. (gap 2, K21)
3. What do Credé and Howardson 2017 and the 2018 reply report per sample? (gap 3, K25)
4. Debate versus self-consistency at equal tokens on information-pooling tasks: does anything beat SC? (K18)
5. Is there any randomised intervention that raised c and transferred to held-out tasks? (gap 5, K20)
6. Is a two-factor structure better for LLM batteries, as for humans? (gap 6)
7. Do the Kommol 2025 fit indices change the 19.6% AVE story? (gap 7)
8. Does a disclosure step hold up at fixed tokens, and without the oracle? (gap 8)
9. Why do independent labs find c-to-IQ r = .32 and Woolley labs r = .10? (gap 9)
10. Is the ACI plug-in gain (mean 4.6%) bigger than seed noise? (gap 10)

## 11. Sources

[V] opened (read), [M] snippet or metadata only.

- [V] Woolley et al. 2010, Evidence for a collective intelligence factor: https://www.Gwern.net/doc/iq/2010-woolley.pdf (a01 to a06); [M] DOI page https://www.science.org/doi/10.1126/science.1193147 (c24)
- [V] Riedl et al. 2021, Quantifying collective intelligence in human groups, PNAS: https://pmc.ncbi.nlm.nih.gov/articles/PMC8166150/ (a07, a08, a10 to a12, b06, b27, c01, c21 to c23)
- [V] Correction for Riedl et al. 2022, PNAS 119(19):e2204380119: https://pmc.ncbi.nlm.nih.gov/articles/PMC9171794/ (a09, b07, c02; one source)
- [V] Rowe, Hattie, Hester 2021, g versus c: https://pmc.ncbi.nlm.nih.gov/articles/PMC8019454/ (b01 to b05, b12, b13, b25, c03, c04)
- [V] Bates and Gupta 2017, Smart groups of smart people: https://gwern.net/doc/iq/2016-bates.pdf (a13 to a15, b09, b10); [V] publisher page https://www.sciencedirect.com/science/article/pii/S0160289616302361 (c08)
- [V] Engel et al. 2014, Reading the Mind in the Eyes or reading between the lines: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115212 (a16, a17, b11); [M] https://doi.org/10.1371/journal.pone.0115212 (c25)
- [V] Barlow and Dennis 2016 via LSE blog: https://blogs.lse.ac.uk/businessreview/?p=11409 (a18); via Rowe's table (b12)
- [V] Credé and Howardson 2017 press accounts: https://www.eurekalert.org/news-releases/667971 (a19, a20); https://www.sciencedaily.com/releases/2017/10/171017124354.htm (b08, b26, d10); https://www.futurity.org/?p=1577982 (c06); [M] https://academicnewsletter.sufe.edu.cn/info/370165 (c05). Original paper not read.
- [M] Woolley, Kim, Malone 2018 reply: https://muriteams.cs.ucsb.edu/node/1168 (a21); https://papers.ssrn.com/abstract=3187373 (c07, d11)
- [V] Zhou et al. 2026, Identifying Collective Intelligence Factor in LLM Agent Groups, ACL Findings: https://aclanthology.org/2026.findings-acl.624.pdf (a22 to a25, b19 to b22, c09 to c11, d08, d09); [M] https://aclanthology.org/2026.findings-acl.624/ (d19)
- [V] Riedl 2025/26, Emergent coordination in multi-agent language models, arXiv 2510.05174, ICLR 2026: https://arxiv.org/abs/2510.05174 and https://arxiv.org/pdf/2510.05174 (a26, b23, c12, c13)
- [V] Ilic and Gignac 2024, arXiv 2310.11616: https://arxiv.org/pdf/2310.11616 (c14); [M] https://arxiv.org/abs/2310.11616 (b18)
- [V] Dyadic collective intelligence study (2025), Cognitive Research: Principles and Implications: https://pmc.ncbi.nlm.nih.gov/articles/PMC12460217/ (b14 to b16; describes Rowe 2024 and Graf 2019)
- [V] Kommol, Riedl, Woolley 2025 (abstract page): https://www.networkscienceinstitute.org/publications/the-structure-of-collective-intelligence-evidence-for-collective-memory-attention-and-reasoning (b17, d13)
- [V] Graf, Gimpel, Barlow 2019: https://www.fim-rc.de/Paperbibliothek/Veroeffentlicht/1043/wi-1043.pdf (d12)
- [V] Rowe, Hattie, Munro 2024 (abstract): https://econpapers.repec.org/RePEc:plo:pone00:0307945 (d14)
- [V] Fan et al. 2026, Towards a science of collective AI (abstract): https://arxiv.org/abs/2602.05289 (b24)
- [M] Burton et al. 2024, How LLMs can reshape collective intelligence: https://www.cmu.edu/tepper/news/stories/2024/september/collective-intelligence-and-llms.html (c26)
- [V] Smit et al. 2024, Should we be going MAD?: https://arxiv.org/html/2311.17371v3 (c15, c16)
- [V] Zhang et al. 2025, Stop overvaluing multi-agent debate: https://arxiv.org/pdf/2502.08788v3 (c17, c18)
- [V] Li, Naito, Shirado 2025/26, HiddenBench: https://arxiv.org/pdf/2505.11556 and https://arxiv.org/pdf/2505.11556v3 (c19, c20, d06, d07)
- [V] Wang et al. 2024, Reasoning in Token Economies: https://arxiv.org/pdf/2406.06461 (d01)
- [V] Tran and Kiela 2026, Single-agent LLMs outperform multi-agent systems on multi-hop reasoning: https://arxiv.org/pdf/2604.02460 (d02)
- [V] Hu, Shen, Lakshmipathi 2026, Statistical scouting: https://arxiv.org/pdf/2605.09618 (d03)
- [V] Bertalanic and Fortuna 2026, The Cost of Consensus: https://arxiv.org/pdf/2605.00914 (d04)
- [V] Wunderlich et al. 2026, Multi-agent reasoning improves compute efficiency: https://aclanthology.org/2026.acl-srw.1.pdf (d05)
- [V] Woolley et al. 2022, Collective attention and collective intelligence: https://doi.org/10.1287/orsc.2022.1602 (d15)
- [V] McDonald et al. 2026, press summary: https://www.cmu.edu/tepper/news/stories/study-real-time-feedback-metrics-collaborative-processes-failed-boost-performance-collective (d16)
- [M] Gupta et al. 2024 nudges (search summary): https://www.eurekalert.org/news-releases/1126556 (d17)
- [M] AEA RCT registry 2896: https://www.socialscienceregistry.org/trials/2896 (d18)

Source-label notes: a09, b07 and c02 are one source. The Riedl "emergent coordination" paper is dated 2025 in some lines and 2026 (ICLR) in others; it is one paper. Where a source was read only through Rowe's tables (Woolley 2010 figures, Barlow and Dennis, Engel), numbers are second-hand.
