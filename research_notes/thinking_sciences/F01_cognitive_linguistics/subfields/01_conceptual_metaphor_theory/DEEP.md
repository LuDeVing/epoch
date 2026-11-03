# Conceptual metaphor theory: deep document

*Subfield F01.01. Built from evidence_a-d.jsonl (a01-a32, b01-b26, c01-c27, d01-d17), claims.jsonl (K01-K32) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Lakoff and Johnson 1980 and Lakoff 1999 were not opened; theory comes from Lakoff 1993 [V].*

## 1. What it is

Conceptual metaphor theory (CMT) says metaphor is not only decoration in language. It is a way of thinking. A person understands one domain (the target, often abstract) through another domain (the source, often concrete). The link is a set of fixed correspondences, called a mapping. The shorthand is TARGET IS SOURCE, for example LOVE IS A JOURNEY, TIME IS SPACE, GOOD IS UP.

Key claims:

- Mappings are in thought, not in single words. Many surface phrases come from one mapping. [a01, a03]
- A mapping carries source knowledge into the target. "We're stuck" evokes the travel scenario (a blocked vehicle), which licenses inferences about the relationship: get it moving, give up the goals, abandon the vehicle, stay with least effort. [a02]
- The Invariance Principle: the mapping keeps the structure of the source that fits the target and drops the rest. This is a hypothesis with no data in the chapter. [a04]
- Evidence listed by Lakoff: polysemy, inference patterns, novel metaphorical language, semantic change, psycholinguistic experiments. He calls the first three "the most robust". That is the analyst's own linguistic generalisation, not behaviour. [a01]

Why it matters for our agent: operator O6 (change representation) asks the model to restate a problem in other terms. CMT is the nearest theory of what restating in a source domain does: it carries structure over and licenses inferences. It also predicts the risk: the mapping can carry inferences that are false of the target.

What this subfield finds, in one paragraph. The human behavioural evidence is thin and contested. The famous framing effect (crime as beast vs virus) is real in the original lab, 10-18 points, but weaker with better designs and failed in one independent replication. Embodied-metaphor priming mostly fails to replicate. The space-to-time mapping is the best supported. LLMs read familiar metaphors almost as well as people, but they are brittle on novel mapping tasks, over-label metaphor, invent source domains, and can be steered into worse answers by metaphorical wording. No study tests whether restating a reasoning problem in a different source domain helps a frontier model. The same-domain cousins (rephrase, step-back, self-generated analogs) do help.

Links to other subfields in this run (not covered here): Conceptual blending, Analogical problem solving, Chain-of-thought prompting, Valence framing, Incremental mapping, Connectionist and hybrid mapping models.

## 2. History and theories in depth

**Founding (1980-1999).** Lakoff and Johnson (1980, "Metaphors We Live By") argued that ordinary language is full of systematic metaphor (ARGUMENT IS WAR). Lakoff (1993, "The Contemporary Theory of Metaphor") is the clean statement and the one opened here. Lakoff (1999, with Johnson, "Philosophy in the Flesh") adds embodiment: primary metaphors come from bodily experience (GOOD IS UP, AFFECTION IS WARMTH). Neither book was opened. [a01]

**The mapping model [a02-a05].**
- LOVE IS A JOURNEY: four core correspondences. Lovers map to travellers. The relationship maps to the vehicle. Common goals map to destinations. Difficulties map to impediments.
- Mappings are between conceptual domains, not words. Names such as "LOVE IS A JOURNEY" only label the mapping.
- TIME mappings: times are things, passing is motion, the future is in front of an observer. Two variants: the observer moves through still times (ego-moving), or times move past a still observer (time-moving). [a05]
- Limits: the analyst chooses the correspondence set. Nobody tested whether people draw the mapped inferences. English-based.

**Behavioural era (2000-2013).**
- Boroditsky (2000, read only via a review chapter [a07-a12]): primes in space shift time judgements; time primes space less. This is the "weak" metaphoric structuring view: spatial schemas help think about time but are not required. Prime-strength confound noted: spatial primes were pictures, time primes were calendar sentences. [a08, a09]
- Nunez, Motz and Teuscher (2006) argued the ego-moving vs time-moving split is the wrong cut and proposed Ego-RP and Time-RP framings. The theory's own two-way split was revised. [a10]
- Cross-language variation: Aymara puts the past in front. German, Swedish and US English speakers prefer different frames of reference. [a11]
- Line-length and duration tasks show asymmetry without any metaphorical language, among the stronger pieces. [a12]
- Teuscher et al. (2008): brain-response congruity effect smaller for metaphorical time sentences than literal space sentences (N=24 behaviour, N=12 ERP). Fits "career of metaphor" accounts. [a13]
- Thibodeau and Boroditsky (2011, 2013): the crime-as-beast/virus studies. Section 5.

**Critiques and alternatives.**
- Polarity correspondence (Lakens 2012): positive-UP effects come from shared polarity, not a GOOD IS UP mapping. [b13, b14]
- Statistical learning, magnitude matching, valence matching and semantic mediation as explanations, not only embodiment (Liu and Lupyan 2026 review, 72 cross-sensory and 84 cross-conceptual studies). Space-time is symmetric in infants and asymmetric in adults with language. [d16]
- The replication crisis hit the embodied branch (warmth, cleanliness, head-heart). [b11, b12, a22]
- Meta-analysis shows tiny average framing effects. [b08, b09]

**Computational era (2021-2026).** Metaphor generation conditioned on mappings (CM-BART), probing of metaphor in pretrained models, benchmarks (Fig-QA, MUNCH), psychologically informed chain of thought (Prystawski), GPT-4 evaluations (Ichien), and 2025-26 audits showing surface-cue use and harmful steering. Section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Beast vs virus framing shifts free-text crime solutions toward enforcement | Exp 1: 74% vs 56% enforcement, chi2=13.94; second study 71% vs 54%; 65% overall enforcement; metaphor shift 18-22 points vs party gap 8-9 and gender gap 8 | Thibodeau and Boroditsky 2011 [a14, b01, b04] | [C] |
| Forced-choice follow-up, smaller effect | 42% vs 31% first-choice enforcement, N=939, chi2=12.55, p<.001; per-experiment enforcement 19%, 76%, 39% | T and B 2013 [a18, b05] | [C] |
| Needs a full frame, not a keyword | Lexical prime: 64% (beast) vs 65% (virus), chi2=.001, p=.99, N=235 (a15 misstates this; b02 correct) | T and B 2011 Exp 3 [b02] | [S] |
| Frame must come first | First: 40% vs 22%; last: 69% vs 64%, p=.59 | T and B 2011 Exp 4-5 [b03] | [S] |
| People do not notice the metaphor | 3-15% name it as influential; recalling it changed nothing (54% vs 56% congruent, p=.84, N=353) | [a17, a18] | [S] |
| Independent replication found no effect | Four experiments, N=253, 259, 252, 1,026; all p>=.34 | Steen et al. 2014 [a19, a20, b06] | [C] |
| Same-lab recode restores a small effect | Recoded "neighborhood watch": Exp 4 chi2(4)=8.61, p=.072, w=.16; pooled N=876 chi2(4)=16.35, p=.003, w=.14; Exp 1 N=526 w=.16; Exp 2 N=521 w=.09 | T and B 2015 [d01] | [C] |
| Extended metaphor changes memory, not preference | Reading time vs enforcement r=.16, .23 | Steen 2014 [b07] | [S] |
| Meta-analysis of metaphor framing | 91 studies, N=34,783, d=0.11; concept-level d=0.22 (k=36), word-level d=0.04 (k=55); science/education d=0.11 vs other d=0.23 | Brugman et al. 2019 [b08, b09] | [S] (not re-opened) |
| Well-powered related studies | Antagonist disaster metaphors d=.47 (N=363) then .15 (N=636), .20 (N=937); vaccine metaphors vs literal F=0.059, p=.81, N=301 | Hauser and Fleming 2021; Flusberg 2024 [d02, d03, d04] | [C] |
| COVID war metaphor | 3.37 vs 3.04 war-congruent choices, p=.25, N=202 | Panzeri 2021 [b10] | [S] null |
| Warmth and prosocial choice fails | Original OR=3.52, N=50; replication pooled OR=0.77 [0.58,1.02], N=861; Chabris N=128 and 177 | Lynott 2014; Chabris 2019 [b11, b12] | [E] fail |
| Head-heart moral judgement fails | N=203 and N=304, Bayesian support for no effect | [a22] | [E] fail (abstract only) |
| GOOD IS UP is polarity | Effect gone with 75% negative words, N=68 | Lakens 2012 [b13] | [S] |
| Space primes time | 71.3% answered by the primed frame; time does not prime space | Boroditsky 2000 via review [a07-a09, a12] | [E] (secondary report) |
| Metaphor processing has a cost | d' 1.7 (space) vs 1.4 (time), N=24; smaller ERP effect N=12 | Teuscher 2008 [a13] | [S] |
| Metaphoric colour bias | Colour IAT d=1.44 vs race IAT d=1.12, N=200, r=.30 | Durgin 2026 [a21] | [S] |
| LLM reads familiar metaphor | GPT-4 91.27%, humans 94.42% (95.39% after exclusions), GPT-3 Davinci 68.41%, RoBERTa 90.32%, 1,146 items, 3.35% non-answers | Ichien 2023; Liu 2022 [a23, c01, c09] | [E] |
| LLM reversed metaphors | 56% vs humans 50%; r=0.79 over 55 items | Ichien 2023 [a24, c02] | [S] |
| MUNCH paraphrase judgement | Mostly at or below chance .25; generation MRR LLaMA-13B .33, LLaMA-30B .47, GPT-3.5 .54 | Tong 2024 [a27, c07] | [S] |
| Source domain naming | GPT-3: 81.33% curated, 53.74% English LCC, 34.65% Spanish LCC | Wachowiak and Gromann 2023 [b20, c13] | [S] |
| Metaphor gaps in modern models | Concept-irrelevant readings in 15-25% of outputs for GPT-4, GPT-4o, o3-mini, R1; R1 28.68 to 46.41 with POS shuffling | Ye et al. 2026 [d06] | [S] |
| Lexical overlap inflates scores | Qwen2.5-72B CoT: Figurative-NLI 95.43 metaphor vs 88.58 literal | Sanchez-Bayona 2025 [d05] | [S] |
| Over-detection | TroFi 3,736 sentences, literal recall GPT-3.5 5.59%, GPT-4-turbo 60.53%, GPT-4o 54.24% | Hicke 2024 [d07] | [S] |
| Metaphor wording misleads code models | Inefficient algorithm choice 9.6% to 23.3% (Qwen), 4.4% to 34.5% (DeepSeek), 2.9% to 23.6% (Gemma); danger metaphors doubled misaligned answers 20% to 40% in Qwen3-32B | Hu et al. 2026 [a32, d08] | [S] |
| Equivalent framings flip LLM choices | P(B) 4.3% to 68.8% (64.5 points), 82 models, 11 families | Wang and Zhang 2026 [d09] | [S] |
| Opposite-frame restatement debiases | Framing disparity cut by avg 92%, bias score 93% (BBQ, 8 models, 3B-14B, four calls) | DeFrame 2026 [d10] | [S] |
| Premise order | Accuracy down 20-40% on reorder (GPT-4-turbo 94.1 to 85.0 on R-GSM) | Chen 2024 [d11] | [S] |
| Same-domain restatement | RaR: GPT-4 average 64.95 to 89.77 over ten tasks | Deng 2023 [d12] | [S] |
| Step-back / analogs / thought propagation | PaLM-2L MMLU Physics 66.4 to 73.2 (GPT-4 69.4 to 84.5, CoT alone 82.9); GSM8K 75.0 to 77.8; +12 to +15 points | [c21, c22, c23] | [E] |
| Spatial restatement | VoT GPT-4 route success 9.48 to 14.72; next step 54 to 59; ring navigation 49.5 vs CoT 52.5 | Wu 2024 [d13] | [S] |
| Metaphor-theory CoT | Curie 2.49 to 2.76 (QUD vs none beta=.41 [-.02,.84], ns); DaVinci 3.71 to 3.74 | Prystawski 2022 [a26, c04, c05] | [S] |
| Analogy brittle | Counterfactual alphabets 0.35-0.49 vs humans 0.753; SCAN MRR .022 (GPT-2), .048 (BERT) | [c19, c20] | [E] |
| Mapping-conditioned generation | CM-BART 2.87 vs 2.12 (MERMAID), exact match 29.3% vs 13.3%; agreement .37-.50 | Stowe 2021 [a29, c15] | [S] |

## 4. Mechanisms and models

Each is written so an engineer could build it.

**4.1 The mapping as a data structure.** A mapping is a typed table: source element to target element, plus a list of source inferences to carry. Example for LOVE IS A JOURNEY: {lovers: travellers, relationship: vehicle, goals: destinations, difficulties: impediments}; inference: "vehicle blocked, so options are free it, stay, abandon, stay with least effort". Implement as JSON. Code checks completeness: every source element used in the restatement has a stated target element. [a02]

**4.2 Invariance check.** After restating in the source domain and reasoning there, each inference taken back must be tested against known target facts. Code step: list the inferences; for each, ask a narrow yes/no question about the target with the facts shown; drop those that fail. This is the engineering form of the Invariance Principle. It is needed because modern models give irrelevant or imported content in 15-25% of outputs and metaphor wording raised bad choices by up to 30 points in code models. [a04, d06, a32]

**4.3 Frame-invariance probe.** Two restatements in opposed frames (beast/virus style), answer both, reconcile in code. DeFrame cut disparity by about 92% in small models. Cheap guard: if the final answer flips between frames, mark it unreliable and fall back to the neutral arm. [d09, d10]

**4.4 Why the effect needs a full frame.** A single keyword prime did nothing (64% vs 65%); the metaphor in an integrated sentence did (74% vs 56%). Implementation: pass a correspondence table, not a cue word. Untested in LLMs. [b02]

**4.5 Position.** The frame worked only when first. For an LLM, put the restated frame before the facts and compare with after. Premise order alone moves accuracy 20-40%, so position will matter. Untested for metaphor. [b03, d11]

**4.6 Polarity control.** Positive and negative labels create spurious congruency. Balance polarity of source and target labels, and strip evaluative words from the source domain. [b13, d08]

**4.7 Mapping-conditioned generation.** CM-BART: given source and target domains, generate. Explicit domains steer output. For an agent: supply both domains and the table rather than "think of it as X". [a29]

**4.8 Spatial restatement.** Visualization-of-Thought: write the layout as text after each step. Works for tasks with ordering or layout; helped 70B but not 8B. [d13]

**4.9 Processing cost.** Cross-domain mapping costs tokens. Count them and compare at equal budget. [a13]

## 5. What holds up

**Holds up reasonably.**
- Space-to-time mapping: primed frames shift temporal judgements, with asymmetry (concrete to abstract). Secondary report only. [a07-a12]
- LLMs interpret familiar metaphors near human level. [a23, c01, c09]
- Same-domain restatement and analogy prompts help LLMs. [c21-c23, d12]
- Models are very sensitive to equivalent wording and order. [d09, d11]

**Failures and nulls.**
- Embodied priming: warmth (N=861), head-heart (N=507), cleanliness and Macbeth effect (b15, b16 only snippets, do not quote). [b11, b12, a22]
- Steen et al. 2014 four-experiment null (N up to 1,026). The same-lab recode brings back a small effect (w=.14) but is post hoc and not independent. Do not treat Steen as a clean refutation. Still contested. [a19, d01]
- Panzeri 2021 COVID war metaphor null. Vaccine metaphor null (p=.81). [b10, d03]
- Brugman 2019: d=0.11 over 91 studies, small-study effects present.

**Moderators.**
- Frame level: concept-level d=0.22 vs word-level d=0.04. [b08]
- Topic: science/education weaker. [b09]
- Position: first only. [b03]
- Politics: Republicans less swayed (49% vs 63% match, chi2=5.46; post hoc, 28 Republicans in Exp 4). [b04]
- Scoring of answer options: one option recoded moves the Steen result from null to p=.072. [d01]
- Language and culture: Aymara, Mandarin, German, Swedish differences. [a11]
- Model size: scaffold helps Curie, not DaVinci. VoT helps 70B, not 8B. [a26, d13]

**Effect size shrinks with power.** d=.47 fell to .15 and .20 as N grew (antagonist metaphors). The original lab numbers are an upper bound. [d02]

**What worked as intervention.** Opposite-frame restatement (DeFrame); same-domain rephrase and step-back; mapping-conditioned generation. **What did not.** Keyword primes; psychologically informed CoT for strong models; Kramer's CMT prompting paradigm (no numbers, 100 self-built problems, four small models). [a30, d14]

**Self-report is not a check.** People name the metaphor in 3-15% of cases while being moved by it. For models too, reasoning text is not evidence (G10). [a17]

## 6. Language models

**Reading metaphors.** Strong models do well on familiar items. Fig-QA: GPT-4 91.27% vs humans 94.42%; GPT-3 Davinci 68.41%; RoBERTa 90.32%. GPT-3 often restated the metaphor literally and contradicted itself across 4 samples in 37.7% of cases (all 4 correct only 19.3%). [a23, c09, c10] Novel literary metaphors: GPT-4 at or above student level (source effect p=.045); one lab, leak risk. [a24]

**Understanding as mapping.** MUNCH: LLaMA-13B/30B and GPT-3.5 mostly at or under chance on apt-vs-inapt paraphrase; generation MRR .33/.47/.54 (the critique fixed an earlier label shift). [a27, c07, c08] Newer models: 15-25% concept-irrelevant readings for GPT-4, GPT-4o, o3-mini, R1; no reasoning advantage. [d06] Open 7B-72B models score higher on metaphor than on literal paraphrase, which tracks lexical overlap. [d05] Ye et al. multiple-choice near chance (46-52%) for seven models is a format effect (very fine options), not a conflict with Ichien. [a31]

**Naming source domains.** GPT-3: 81.33% curated, 53.74% English, 34.65% Spanish; errors mostly invented domains. The 62.12% error figure is given two meanings by two agents; unresolved. [b20, c13, c14] GPT-4 chain of thought labelled four speeches: r=.987 on category counts, but F1 .963 for health and 0 for plants; the reference is a tool, not humans. [b24] Detection: models over-label; literal recall as low as 5.59%. [d07]

**Probing.** Metaphoricity sits in middle layers of BERT, RoBERTa, ELECTRA and transfers across four languages; probe gaps over baseline can be small (TroFi about 68 vs 67). Detection is not use. [a28, c12]

**Using metaphor to reason.**
- Prystawski: theory-derived CoT helped Curie, not DaVinci. [a26]
- Kramer: no usable numbers. [a30, d14]
- Harm: metaphor wording degraded code-model choices (up to +30 points inefficient algorithms) and danger metaphors doubled misaligned answers in Qwen3-32B; concrete metaphors halved them (40% to 20%). [a32, d08]
- Framing: 82 models flipped choices by up to 64.5 points on equivalent framings; DeepSeek was least sensitive. Reasoning traces lowered B rates in an exploratory check (.811 to .254). [d09]
- Fix: DeFrame, about 92% disparity reduction in small models. [d10]
- Neighbours: RaR took GPT-4 from 64.95 to 89.77; step-back is mixed (GPT-4 CoT 82.9 vs step-back 84.5); self-generated analogs +2.8 on GSM8K; VoT small gains on spatial tasks. [d12, c21, c22, d13]

**Analogy limits.** Counterfactual letter strings: 0.35-0.49 vs humans 0.753. Familiar forms: GPT-3 matched students (OR=1.88 digit matrices, 1.76 letter strings). The difference is familiarity. [c17-c19]

**Culture.** Western default in metaphor generation (abstract only). Multilingual encoders are weaker in non-English figurative inference (XLM-R 63.99%). [d15, c25]

**Bottom line.** Understanding the metaphor is not the bottleneck for strong models. Applying a mapping correctly and not importing false inferences is. No one has measured O6 on a frontier model at equal tokens.

## 7. What our agent should take

### Add now (established)

Few items here are established, and none is an established benefit of O6. These are guards and baselines.

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not borrow human embodied-priming effect sizes or design on the premise that bodily grounding matters | none (4b entry) | [E] | K07: b11, b12, a22 |
| Understanding a familiar metaphor is not the bottleneck; spend tokens on applying the mapping | O6 | [E] | K11: a23, b19, c01, c09 |
| If O6 uses a source domain, make it concrete and familiar; unfamiliar sources collapse performance | O6 | [E] | K21: c19, c20 |
| Same-domain abstraction and analogy (step-back, self-generated analog, rephrase) is the tested neighbour; use it as the baseline for O6 | O6, O7 | [E] | K20: c21-c23 |
| Direction of restatement: concrete source to abstract target (space for time) | O6 | [E] (human, secondary report) | K09: a07-a12 |

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Always run a no-reframe arm; expect d about .15-.20, not .5 | G7, O6 | [C] | K01, K02, K24 |
| Invariance check: drop source inferences false of the target | O6 | [S] | K17, K30, K13 |
| Frame-invariance check: answer under two opposed frames, flag flips | G, O6 | [S] | K26, K27 |
| Correspondence table beats cue word or free text | O6 | [S] | K04, K16 |
| Place the reframe before the facts | S1/S2, O6 | [S] | K03 |
| Strip evaluative words from the source domain | G (framing risk) | [S] | K32, K23 |
| Spatial restatement only for ordering and layout tasks | O6 | [S] | K29, K09 |
| Mapping overhead must pay for itself at equal tokens | G7 | [S] | K10 |
| Pre-register scoring of answer types before any reframe test | test method | [S] | K25 |
| Scaffold gain shrinks with model strength; test on the model we ship | G7 | [S] | K19 |
| Rationale mention rate: log whether text names the frame when the answer shifts | G10 | [S] | K05 |
| Keep O6 at impasse only (G1), never routine | G1, S6 | [D] | K06: d=0.11 average |

O6 stays [S] in SCHEMA.md. Nothing in this document raises it.

## 8. Concrete tests on our bench

All arms at equal tokens (cap the longest arm, trim or pad others to the same budget; count mapping overhead). Report accuracy, paired flips, tokens.

1. **O6 vs RaR vs step-back vs plain CoT.** Items: BrainTeaser-style lateral puzzles, word puzzles, ARC-like items. Arms: plain CoT; rephrase-and-respond; step-back; self-generated analog; O6 free-text source-domain restatement; O6 with correspondence table. Metric: accuracy and paired flips (right-to-wrong, wrong-to-right). Expected: O6 at or below RaR on non-spatial items; table arm above free text by a few points; gains under 3 points are noise.
2. **Spatial vs text restatement.** Items: ordering, scheduling, interval and route problems. Arms: plain; spatial layout restatement (VoT-style); text. Metric: accuracy. Expected: gain on layout tasks (about +5 points as in VoT), none or loss on abstract tasks.
3. **Frame-invariance.** Items: 60 problems each in two logically equivalent frames. Arms: single frame; two-frame answer with code reconciliation (DeFrame style) at the same total calls. Metric: flip rate and accuracy. Expected: flips fall sharply, accuracy flat or up.
4. **Invariance check.** Items: problems where the natural source domain has a misleading entailment (a war or journey frame that suggests a wrong action). Arms: restate and solve; restate, solve, filter inferences against target facts. Metric: rate of answers using a false imported inference. Expected: large drop, small token cost.
5. **Position.** Same items, reframe before the facts vs after vs absent. Metric: accuracy and flip rate. Expected: first position shifts answers more (human hint); unknown for models.
6. **Loaded vs neutral source.** Restatement with evaluative words (war, danger) vs neutral wording. Metric: shift in judgement items and accuracy. Expected: loaded source shifts answers toward the frame.
7. **Model-strength interaction.** Run test 1 on a small and a large model. Expected: scaffold helps small, not large.
8. **Rationale mention rate.** In test 3, record whether the model's text mentions the frame when its answer shifts. Expected: low mention rate, supporting G10.

## 9. What does not transfer, and why

- **Embodiment.** Bodily grounding matters for people, not for a text model; priming effects also fail to replicate. [b11, b12, a22]
- **Human effect sizes.** Original 17-18 points shrank to 10 points and to d=.15-.20 under power. Do not plan around them. [a14, a18, d02]
- **Unnoticed influence.** People do not notice the frame; a model can be asked and its rationale logged, but the rationale is unreliable. [a17]
- **Polarity and IAT results.** GOOD IS UP and IAT bias are stimulus or measurement issues in humans. [b13, a21]
- **ERP and reaction-time costs.** Brain-level processing costs map only loosely to token cost. [a13]
- **Cultural mapping variation.** Matters for human populations; a monolingual agent mostly needs one stable source domain, though models show a Western default. [a11, d15]
- **Interpretation benchmarks.** Fig-QA and MUNCH measure reading metaphors, not using them to solve problems. [K11, K13]
- **Lakoff's own evidence.** Polysemy and inference patterns are linguistic generalisations, not behaviour. [a01]

## 10. Open questions

1. Does restating in a different source domain beat plain CoT, RaR, step-back and self-generated analogs at equal tokens on a 2025-2026 model? Nobody has tested it.
2. Does the first-position effect hold for LLMs?
3. Correspondence table vs free text vs one cue word in an LLM?
4. How often do strong and reasoning models import source inferences that contradict the target?
5. Why did Steen et al. fail? Is the recode explanation right? No independent preregistered replication of beast/virus was found.
6. Does a value-loaded source (war, danger) bias judgement in current models? Only Qwen3-32B and code-model data exist.
7. Do reasoning models differ on apt vs inapt metaphor judgement? Partly closed: no advantage in d06.
8. Which source domains give measurable benefit beyond space for time?
9. Cross-language variation in mapping choice.
10. Full-text numbers for Boroditsky 2000, Brugman 2019, Lynott 2014 (403 and 404 errors; do not quote).
11. The 62.12% figure in Wachowiak and Gromann has two readings.

## 11. Sources

[V] opened (page or full text read by an earlier agent in this series), [M] snippet or abstract only. Where the critique says "not re-verified", the line says so.

- [V] Lakoff (1993) The Contemporary Theory of Metaphor. https://terpconnect.umd.edu/~israel/lakoff-ConTheorMetaphor.pdf
- [V] Wikipedia, Conceptual metaphor. https://en.wikipedia.org/wiki/Conceptual_metaphor
- [V] Samuel, Athanasopoulos and Bylund (2017) review chapter on Boroditsky 2000 and related. https://openaccess.city.ac.uk/id/eprint/28248/
- [V] Teuscher et al. (2008) Congruity effects in time and space. https://pages.ucsd.edu/~scoulson/Papers/tmcc08.pdf
- [V] Thibodeau and Boroditsky (2011) Metaphors we think with. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0016782
- [V] Thibodeau and Boroditsky (2013) Natural language metaphors covertly influence reasoning. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052961
- [V] Steen, Reijnierse and Burgers (2014) When do natural language metaphors influence reasoning? https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0113536
- [V] Thibodeau and Boroditsky (2015) Measuring effects of metaphor in a dynamic opinion landscape. https://pmc.ncbi.nlm.nih.gov/articles/PMC4517745/
- [V] Durgin et al. (2026) A downside of conceptual metaphor. https://pmc.ncbi.nlm.nih.gov/articles/PMC13547199/
- [M] Head-heart replication (2024). https://doi.org/10.1080/00221309.2024.2360405
- [V] Ichien, Stamenkovic and Holyoak (2023) LLM displays emergent ability to interpret novel literary metaphors. https://arxiv.org/abs/2308.01497
- [V] Prystawski, Thibodeau, Potts and Goodman (2022) Psychologically-informed chain-of-thought prompts for metaphor understanding. https://arxiv.org/abs/2209.08141
- [V] Tong et al. (2024) Metaphor Understanding Challenge Dataset (MUNCH). https://arxiv.org/abs/2403.11810
- [V] Aghazadeh et al. (2022) Metaphors in pre-trained language models. https://arxiv.org/abs/2203.14139
- [V] Stowe et al. (2021) Metaphor generation with conceptual mappings. https://arxiv.org/abs/2106.01228
- [V] Kramer (2025) Conceptual Metaphor Theory as a prompting paradigm. https://arxiv.org/abs/2502.01901
- [V] Ye et al. (2025/2026) Probing semantic alignment, lexical anchors (Unveiling LLMs' metaphorical understanding). https://arxiv.org/abs/2510.04120
- [V] Hu et al. (2026) Metaphors are a source of cross-domain misalignment. https://arxiv.org/html/2601.03388
- [V] Hu et al. (2026) Metaphor-induced algorithmic steering (arXiv id as recorded; not re-verified). https://arxiv.org/abs/2607.28683
- [V] Brugman, Burgers and Vis (2019) Metaphorical framing in political discourse (not re-verified). https://www.cambridge.org/core/product/identifier/S186698081900005X/type/journal_article
- [V] Panzeri, Di Paola and Domaneschi (2021) COVID-19 war metaphor. https://journals.plos.org/plosone/
- [V] Lynott et al. (2014) replication of Williams and Bargh (not re-verified). https://osf.io/preprints/psyarxiv/eg2pu
- [V] Chabris et al. (2019) Two failures to replicate (not re-verified). https://osf.io/preprints/psyarxiv/mvn9b
- [V] Lakens (2012) Polarity correspondence. https://osf.io/preprints/psyarxiv/m54yb
- [M] Johnson, Cheung and Donnellan (2014). https://doi.org/10.1027/1864-9335/a000186
- [M] Earp et al. (2014). https://doi.org/10.1080/01973533.2013.856792
- [V] Wachowiak and Gromann (2023) Does GPT-3 grasp metaphors? https://aclanthology.org/2023.acl-long.58/
- [V] Frontiers in Psychology (2025) LLM prompt engineering for embodied cognition. https://www.frontiersin.org/articles/10.3389/fpsyg.2025.1591408/full
- [M] Thibodeau, Hendricks and Boroditsky (2017). https://doi.org/10.1016/j.tics.2017.07.001
- [M] Hauser and Schwarz (2015). https://doi.org/10.1177/0146167214557006
- [V] Liu, Cui, Zheng and Neubig (2022) Fig-QA. https://arxiv.org/abs/2204.12632
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning. https://arxiv.org/abs/2212.09196
- [V] Lewis and Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955
- [V] Czinczoll et al. (2022) Scientific and creative analogies. https://arxiv.org/abs/2211.15268
- [V] Zheng et al. (2023) Step-Back. https://arxiv.org/abs/2310.06117
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Yu, He and Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965
- [V] Chakrabarty et al. (2023) I Spy a Metaphor. https://arxiv.org/abs/2305.14724
- [V] Kabra et al. (2023) Multilingual and multicultural figurative language. https://arxiv.org/abs/2305.16171
- [M] Dodge et al. (2015) MetaNet, Mohler et al. (2014), Shaikh et al. (2014), cited via Stowe. https://arxiv.org/abs/2106.01228
- [M] Mitchell (2020) as cited in Czinczoll. https://arxiv.org/abs/2211.15268
- [V] Hauser and Fleming (2021) Mother Nature's Fury. https://pmc.ncbi.nlm.nih.gov/articles/PMC8414834/
- [V] Flusberg et al. (2024) Seatbelts and raincoats. https://pmc.ncbi.nlm.nih.gov/articles/PMC10763949/
- [M] Ervas et al. (2022), Liu and Chen (2023), Zhang and Yang (2023), Europe PMC snippets. https://www.ebi.ac.uk/europepmc/webservices/rest/search
- [V] Sanchez-Bayona and Agerri (2025) Metaphor and Large Language Models. https://arxiv.org/html/2507.15357v1
- [V] Hicke and Kristensen-McLachlan (2024) Science is Exploration. https://arxiv.org/html/2410.08991
- [V] Wang and Zhang (2026) Framing effects in independent-agent LLMs. https://arxiv.org/html/2603.19282
- [V] Lim, Kim and Whang (2026) DeFrame. https://arxiv.org/html/2602.04306
- [V] Chen et al. (2024) Premise order matters. https://arxiv.org/html/2402.08939
- [V] Deng et al. (2023/2024) Rephrase and Respond. https://arxiv.org/html/2311.04205v2
- [V] Wu et al. (2024) Visualization-of-Thought. https://arxiv.org/html/2404.03622
- [M] Chang, Qu and Li (2026) Metaphors We Compute By (abstract only). https://arxiv.org/abs/2604.04732
- [V] Liu and Lupyan (2026) The unity of sense and mind (first 100k characters). https://pmc.ncbi.nlm.nih.gov/articles/PMC12769545/
- [M] Brugman 2019 / Lynott 2014 / Boroditsky 2000 full-text attempts (403 and 404). https://onlinelibrary.wiley.com/doi/full/10.1111/lang.12313
