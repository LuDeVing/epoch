# Systematicity: deep document

*Subfield C10.02 of analogy engines. Principle: prefer mappings whose matched relations belong to a connected system governed by higher-order relations. Why it matters for our agent: it is a rule for scoring a mapping (schema O7, "Map an analogue"). Built from evidence_a-d.jsonl (a01-a31, b01-b28, c01-c30, d01-d15), claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids are in brackets. Sibling subfield: 01_structure_mapping_sme (SME itself, not repeated here).*

## 1. What it is

Systematicity is the third rule of Gentner's structure-mapping theory (1983). The three rules are:

1. Drop object attributes (a01).
2. Keep relations between objects.
3. Among relations, keep those that belong to a connected system governed by higher-order relations.

A higher-order relation takes other relations as arguments. Order of a relation is 1 + the maximum order of its arguments. First-order relations take objects. A CAUSE over two relations is second-order (a01).

The rule is purely syntactic. It uses no domain content. A fact is more likely to be carried from base to target if it is tied into a causal or mathematical system that also maps. An isolated fact is less likely to be carried.

Gentner's examples (a02):
- Solar system to atom: MORE MASSIVE THAN(sun, planet) maps, because it sits inside the central-force system. HOTTER THAN(sun, planet) does not, because no mappable system surrounds it.
- Heat to water: "puncture causes water to flow out" is preferred over "the vessel has a lid", because the first is embedded in a CAUSE.

Two things must be kept apart:
- The principle is a preference, not a law. It says which candidate matches get weight when several are possible.
- The score is something to compute (SME does it, section 4). Whether people use it is an empirical question (sections 3 and 5).

For our agent the question is narrow. When the agent has two or more candidate mappings from an analogue to the current problem, does scoring them by connected relational structure pick better than a plain model judgment, at equal tokens? No study answers this (K21, K27). Everything below is the nearest evidence.

## 2. History and theories in depth

**1983, Gentner.** The theory paper states the rules. It has no direct test of systematicity. It cites a study where people wrote interpretations of comparisons like "a cigarette is like a time bomb". Judges coded them as attribute or relation. Analogy interpretations were mostly relational. Descriptions of the same objects were not. Aptness correlated with relational content. No N or coefficients are given in the paper (a03, b15).

**1986, Gentner and Toupin.** First direct developmental test. Children re-enacted a target story using a base story just heard. The base was systematic (a moral gave a higher-order causal structure) or not. Difficulty varied with how characters were cross-mapped (a08, a09, b04).

**1989, SME and its tuning.** Falkenhainer, Forbus and Gentner built the Structure-Mapping Engine. It implements systematicity as local "trickle-down" of belief (a12, b09). Forbus and Gentner (1989) then asked how best to implement the preference. They cut 8 evaluation parameters to 3, swept them, and compared trickle-down against order scaling and Dempster-Shafer (a15-a17, b08). Holyoak and Thagard's ACME is the rival constraint-satisfaction model. Forbus and Gentner say it overlaps heavily with SME. It was not opened here (a24).

**1991, Clement and Gentner.** The key behavioural test: do people treat the shared-system fact as the one that matters? Three experiments (a04-a07, b01-b03). Details in section 3.

**1993, Gentner, Rattermann and Forbus.** The retrieval versus soundness split. Surface matches are recalled most. Structural matches are rated most sound. This became the main reason given for why unaided analogy rarely transfers (b05-b07).

**1997, Gentner and Markman; Bowdle and Gentner.** Review of the evidence, including the claim that asymmetry arises when one item is more systematic and serves as base (a10, a11, b14). Bowdle and Gentner tested this directly (d08).

**2007-2017, the causal-model challenge.** Lee and Holyoak showed that removing a shared preventive cause lowers similarity but raises inferential strength. They read this as people running a causal model of the target (a19, a20, b12). Colhoun and Gentner (2009) replicated the data but argued the right measure is all candidate inferences, and that SME plus a causal step reproduces it (a21, a22, b10, b11). Myers and Gentner (2017) found a carried-over higher-order strength relation (a23, b13). The mechanism is contested (K08).

**2022-2026, the LLM era.**
- Webb, Holyoak and Lu (2023) gave GPT-3 Gentner's own story materials (b17, c03).
- Sourati et al. built ARN on the surface-mapping versus system-mapping distinction (a25, a26, b24, c15).
- Lewis and Mitchell re-ran the story test and counterfactual letter strings (a27, b19, b20, c06).
- Sultan and Shahaf (2022) built a text-to-SME-style mapping pipeline (a28, a29, c19).
- YARN (Khojasteh et al. 2026) is the closest test of a mapping scorer against a plain LLM (d01, d02, d15).
- Gentner and Forbus (2025) give the latest summary from the theory's authors (b16).

**Competing explanations.**
- Goal-driven (pragmatic) accounts: mapping is steered by purpose, not structure (Holyoak; argued against in b09, not tested here).
- Causal-model accounts: people simulate the target's causes (Lee and Holyoak).
- Association accounts for LLMs: success is reachable from word similarity (K18).

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree (claims.jsonl). Single-source = one lab or paper. Contested = sources disagree.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People rate the fact inside a shared causal system as more central to the analogy than an equally plausible isolated fact. Target-only controls show no bias. | N=48, 4 passages. Rating shared 6.28 vs different 4.89; target-only 5.22 vs 5.31. Condition x fact type F(1,44)=13.99, p<.001. Choice score (of 4) 3.17 vs 2.0, F(1,44)=18.43. | Clement and Gentner 1991 Exp 1 (a04, b01) | Single-source (one lab) |
| People predict the shared-system fact about the target far more (base visible). | N about 32, 16 per group. Predictions .53 shared vs .12 other; target-only .12 and .12. Per critique: 1.63 vs 0, F(1,28)=20.05. Choice 2.9 vs 1.8, F(1,28)=16.43. Only 2 of 4 passages reliable (87% and 69% vs 44% and 25%). | Clement and Gentner 1991 Exp 2 (a06, b02) | Single-source |
| From memory (base hidden) the effect is weaker and one passage fails. | N=24 per group. Prediction difference .92 vs .13, F(1,44)=5.15, p<.05. Choice 1.875 vs 1.0 of 3, F(1,44)=13.15. Passage 2: 54% vs 58%, no effect. | Clement and Gentner 1991 Exp 3 (a07, b03; critique correction 1) | Single-source |
| Soundness follows shared relational structure, not shared objects. | N=30, 18 sets. Analogy 4.40 vs surface 2.80 vs first-order-only 2.74, F(2,58)=70.51, p<.0001. | Gentner, Rattermann, Forbus 1993 Exp 1 (b05) | Established (K03; Webb 2023 N=54 humans pick the causal-structure story) |
| Crossed design: relational overlap drives soundness. Objects add a little. | N=20 raters. Literal 4.50, analogy 4.09, surface 3.40, first-order-only 2.88. Relational F(1,19)=85.78. Object F(1,19)=7.01, p<.02. | GRF 1993 Exp 2 (b06) | Single-source |
| Retrieval follows surface overlap. | Recall after one week: surface .78, analogy .44, first-order-only .25, F(2,58)=75.45. Crossed design: literal .56, surface .53, analogy .12, first-order .09. | GRF 1993 (b05, b06) | Single-source |
| The retrieval gap is at access, not storage. | N=27. Surface probes pick the base 82% (16.46 of 20). Relational probes 55% (11 of 20), chance. | GRF 1993 Exp 3 (b07) | Single-source |
| Systematicity helped children only when mapping was hard. | N=72 (36 aged 4-6, 36 aged 8-10). Systematicity F(1,68)=6.28, p<.05. Age F(1,68)=14.93. Systematicity x mapping F(2,136)=3.89. Older t(34)=2.48; younger t(34)=1.08 n.s. | Gentner and Toupin 1986 (a08, a09, b04) | Single-source. Authors' footnote: no significant age x systematicity interaction. |
| Under short deadlines (about 700-1000 ms) local matches win. | Reported through a review only. | Gentner and Markman 1997 (b14) | Single-source, secondary |
| Similarity and inferential strength dissociate. | Exp 1 N=42. Similarity 7.58 / 4.77 / 5.09. Strength 33.60 / 58.57 / 35.32. F(2,36)=16.79 and 8.44. Exp 2 N=60. | Lee and Holyoak 2007 (a19, a20, b12) | Established, 2 labs (K07) |
| The dissociation replicates in the Gentner lab. | N=70. Similarity GGP 7.53 > GG 6.35 > GP 5.01, F(2,286)=44.4. Effect inference GG 89.4 > GGP 74.4 > GP 46.1, F(2,270)=164.6. Over all candidate inferences, strength follows the similarity order. | Colhoun and Gentner 2009 (a21, b10) | Data established; mechanism contested (K08) |
| A carried-over higher-order strength relation shifts inference. | 32 analysed. 62.28 vs 47.28, t(31)=3.44, p<.005. Similarity 6.25 vs 5.78, p=.13. | Myers and Gentner 2017 (a23, b13) | Single-source, small N |
| Asymmetry: the more systematic passage is the preferred base. | N=48 each. Forward comparisons .76 (t(47)=10.52). Forward inferences .80. Projected inferences .81 vs .24 reverse (deletion), .71 vs .28 (replacement). | Bowdle and Gentner 1997 (d08) | Single-source |
| SME scores a mapping by local trickle-down of 80% belief. | Solar-atom SES 6.03 vs 4.04 vs 1.87. Karla stories 22.4 (analogy) vs 16.8 (surface). Under appearance rules 7.7 vs 6.4. | Falkenhainer et al. 1989 (a12-a14, b09) | Single-source (same group) |
| Trickle-down is robust. Order scaling and Dempster-Shafer are not (bottom-heavy sets). | 343 parameter points, 6,174 evaluations over 3 triads. Works: trickle-down 4-16, same-predicate .001-.01. Fails: trickle-down at or below 1. | Forbus and Gentner 1989 (a15-a17, b08) | Single-source; fit binary on 3 triads |
| LLMs match people on near analogies, fail far ones with surface lures. | ARN, 1,096 triples. Far: humans 94.1% vs models 39.6%. Near: 97.9% vs 75.0%. GPT-4: near-far 94.0, near-near 92.5, far-far 57.1, far-near 29.1; avg 68.1. Humans avg 96.0. | Sourati et al. 2023/2024 (a26, b24, c15, c16) | Established (K11) |
| GPT-3 not above chance on far story analogies. | Near p=.0039; far p=.065. Humans N=54, t(53)=16.7 far. Odds ratio 0.37, p=.0003. | Webb et al. 2023 (b17, c03) | Established with ARN and others (K11) |
| GPT-4 on 18 far story analogies is high but order-biased. | 0.86 (31/36); 1.0 correct first, 0.72 second. Paraphrased correct story 0.72 (26/36). Humans N=245: 0.78 both orders, 0.70 paraphrased. Webb's GPT-4: 0.75. | Lewis and Mitchell 2024 (a27, b19) | Single-source |
| Extract-the-message CoT demonstrations raise far accuracy and hurt near. | Up to +30 absolute points far (GPT-based). 2, 4, 6 demonstrations. | Sourati et al. (c17) | Single-source |
| Self-generated analogies give small gains on strong models only. | GSM8K 75.0 to 77.8; MATH 33.0 to 37.3 (GPT-3.5-turbo). Small models: no gain. With self-consistency 85.3 and 46.0. | Yasunaga et al. 2024 (b27, c20-c22) | Established (K16); not a structure test |
| Text-to-mapping pipelines recover mappings. | Top-3 precision 0.87 (ProPara), 0.94 (psychology stories). Question-form 0.82 vs verb-only 0.48 (top-1). | Sultan and Shahaf 2022 (a29, c19) | Established with StoryAnalogy and YARN (K17) |
| Long surface-heavy stories hurt LLMs more than people. | GPT-4 89.1 / 66.5 / 60.7 for 1 / 10 / 30 sentences. Humans 96.0 / 72.5 / 73.3. Retrieval recall@3 42.9% / 6.5% / 3.9% (random 1.6%). | AnaloBench (d03) | Single-source |
| Mapping scorer vs plain LLM at 8B. | Raw phrases MCQ 0.17 (chance 0.25). With abstraction 0.46 (Qwen), 0.45 (Llama). ARN far: Llama mapping 0.46 vs zero-shot 0.42; Qwen 0.47 vs 0.52. Far-near stays below 0.50. | YARN (d01, d02) | Single-source |
| Relational-summary retrieval beats surface retrieval. | Precision at top 1%: purpose 0.739, TF-IDF 0.63. Good-idea rate 0.71 vs 0.28 (N=38). Off-the-shelf embedding retriever 38.5 vs random 37.6. | Hope et al. 2017; RA-RFT 2026 (d04, d05) | Single-source (K24) |
| An LLM judge accepts wrong analogies on surface grounds. | GPT-4 precision about 0.50 with hint, 0.00 without. Humans precision 0.67-1.00, recall 0.06-0.39. Humans n=199, GPT-4 n=60. | d06 | Single-source |
| Frontier 2025-26 models still trail students on far analogy (grid transforms). | Best model 48-51% over 12 attempts vs 59-69% single-attempt humans. | ARCANA (d07) | Single-source |

## 4. Mechanisms and models

### 4.1 SME scoring of systematicity (implementable)

Input: two symbolic descriptions, base and target. Each is a set of predicates. A predicate has a functor, ordered arguments, and an order (1 + max order of its arguments). Entities are order 0.

Steps (a12, b09, b16):
1. **Local match hypotheses (MH).** Create an MH for each pair of base and target statements that satisfy the match rules (same predicate, or same function). Evidence 0.5 for same functor in the free-for-all rule set; initial score 0.2 in b09's setup.
2. **Support structure.** If an MH pairs two relations, MHs pairing their arguments are required. Link them.
3. **Trickle-down.** Each MH passes 80% of its belief to the MH of its argument pair. Rule: `(implies (MH b1 t1) (MH b2 t2) (0.8 . 0.0))`. A deep matched system lifts the scores of the object matches under it.
4. **Build global mappings (gmaps).** Merge MHs into structurally consistent clusters: one-to-one, and parallel connectivity (matched relations have matched arguments).
5. **Score a gmap.** Plain sum of MH belief. Dempster's rule was dropped for roundoff and because normalised evidence blocks comparison across bases (a12).
6. **Pick the highest gmap, then project candidate inferences.** Unmatched base statements connected to the mapped system are carried to the target.

Notes for an engineer:
- The sum is not normalised for the size of base and target (authors say so; a12). Compare gmaps only over the same pair, or add your own normaliser.
- Mapping is NP-complete in general. SME avoids that by local construction (b16).
- Worked numbers: standard solar-atom mapping 6.03, temperature-to-mass reading 4.04, reversed mass reading 1.87. The 4.04 case is low for two reasons: different functions get less evidence, and no systematic structure surrounds temperature (a13).
- Runtime: a flat baseball analogy could not be mapped in hours. A PHINEAS problem took 53 minutes and fell to 34 seconds after systematic structure was added (b09). Systematic structure prunes search, a second use for a program-side scorer.

### 4.2 The simplified parameter set that was tested

Forbus and Gentner reduced evaluation to three parameters (a15, b08): Same-Predicate, Same-Function, Trickle-Down. Working region with additive-max normalisation:
- Trickle-Down 4 to 16.
- Same-Predicate 0.001 to 0.01.
- Same-Function 0.0001 to 0.01.

Every point in that region put the analogy above the appearance match in three story triads. Failing: Trickle-Down at or below 1, Same-Predicate at or above 0.3. Fit is binary, not a correlation (b08).

### 4.3 Why trickle-down and not order scaling

Order scaling: `O3(MH) = Min(1.0, C x [1 + Order(MH) x Order-Bias])`, order bias in {0, 0.5, 1, 2, 4, 8, 16}. It only signals that high-order relations exist. It fails on bottom-heavy sets because local normalisation caps each match (a17). Trickle-down signals connectivity, which is what the principle says. Dempster-Shafer fit only top-heavy (mostly abstract) descriptions (b08).

Specificity Conjecture (a16): human memory descriptions are mostly bottom-heavy (much appearance, little higher-order structure). The paper says this is argued, not measured. The bottom-heavy test set had twice as many match hypotheses for the appearance match as for the analogy match. A predicted "order cutoff" (past some depth, extra systematicity cannot be told apart) has no human data (a17).

### 4.4 Two-stage retrieval (MAC/FAC style)

The retrieval simulation in GRF 1993 used a cheap content-vector filter, then structure mapping on survivors. Share of probes whose base passed both stages: literal 1.0, surface .89, analogy .67. It matched the ordering of human data only (b07). For our agent: cheap filter by surface or embedding first, then the expensive mapping score on a short list.

### 4.5 Text to relations (the missing front end)

SME needs predicates. Free text has none. Two recipes:
- **Sultan and Shahaf 2022** (a28, a29, c19). Extract entities and relations with QA-SRL question forms. Beam-search a one-to-one mapping that maximises the sum, over base entity pairs, of sim(R(bi,bj), R(M(bi),M(bj))). Mapping into "empty" scores 0. There is no higher-order term, so this is a pairwise proxy for a connected system.
- **YARN** (d01, d02, d15). Split each story into atomic events with a temporal index. Give each event an open-vocabulary frame "[modifier]-[root]". Add abstraction levels (conceptual two hierarchy levels, evaluative, stage, narrative arc). Map by cosine similarity with a FAME-style one-to-one assignment. Raw phrases score below chance (0.17). The abstraction level must match surface overlap: low level for near pairs, high level without modifiers for far-near pairs.

Extraction error was not measured in either recipe (d15, critique gap 3).

### 4.6 The causal-model alternative

Lee and Holyoak: build a causal model of the target, compute the effect probability from shared and unshared causes. Colhoun and Gentner: map first (SME), then run a simple causal calculation on the candidate inference. Both reproduce the dissociation. The Gentner-side simulation took the highest-SES mapping and used candidate-inference support scores (a22, b11). No fit statistic is given. An engineer can implement both as variants and compare (K08 test).

## 5. What holds up

**Holds up reasonably.**
- Soundness follows relational structure, not shared objects (K03).
- Similarity and inferential strength dissociate under shared preventive causes (K07). Two labs, N=42, 60, 70.
- LLMs fail far analogies when surface lures are present (K11). ARN, Webb, AnaloBench, StoryAnalogy and ARCANA all point one way.
- Embedding similarity or association solves much of what looks like analogy (K18): SBERT 77.9% on near ARN analogies; GPT-4 over 70% of children's verbal analogies from the C term only (b26, c16).

**Single lab, not independently replicated.**
- Clement and Gentner 1991 itself. No independent replication was found (d13, K27). Bowdle and Gentner 1997 is a within-lab extension. Sample sizes are 24 to 72 per study. Effect sizes beyond F and p are not reported in the originals.

**Failures and boundary conditions inside the original studies.**
- Exp 2 of Clement and Gentner: only 2 of 4 passages differed reliably.
- Exp 3: Passage 2 failed in both tasks (54% vs 58%). The authors blame misrepresentation of the base chain. That is an explanation, not a test.
- From memory the effect shrank (.92 vs .13, against the larger base-visible gap).
- Children: no benefit at 4-6. The effect appeared only in the hardest cross-mapped condition for older children. The footnote reports no significant age x systematicity interaction (a09, b04). The systematic stories were also longer (about 200 vs 170 words), so a length confound remains (a08).
- Easy mappings: everyone near ceiling.
- Short deadlines: local matches win (secondary report only).
- Asymmetry needs alignable structure. With shuffled non-alignable pairs it shrinks (d08).
- Trickle-down fails under wrong settings; order scaling fails earlier on bottom-heavy sets (a17).

**Mechanism disputes.**
- Lee and Holyoak versus Colhoun and Gentner: same data, two accounts (K08). "Mean over all inferences" is the Gentner side's choice of measure. Myers and Gentner: inference effect significant (p<.005), similarity effect not (p=.13).

**Interventions in LLM work.**
- Worked: abstraction before mapping (MCQ 0.17 to 0.46); question-form relations over verb-only (0.82 vs 0.48); extract-the-message CoT demonstrations (up to +30 far, a cost on near); retrieval by relational summary (d04); code execution on counting-heavy letter strings (b22).
- Did not work or small: raw-phrase mapping; self-generated analogies on small models; self-generated analogies on strong models (+2.8 GSM8K, +4.3 MATH); the 8B mapping scorer on near items (Qwen 0.69 vs CoT 0.79).
- Not tested: thinking budget. ARCANA did not vary it. ARN has no reasoning-model rerun (d11).

**Numbers not to inflate.**
- "Models 57%" on ARN is an average over the full model set, not GPT-4. GPT-4 averages 68.1 (critique correction 4).
- Human letter-string accuracy is 0.753 [0.734, 0.773], not 0.754 (correction 3).

## 6. Language models

**Near versus far.** On ARN, GPT-4 is close to human on near analogies. It collapses when the distractor shares surface with the query and the correct answer shares only the relational system: far-near 29.1% (below the 50% random line), far-far 57.1% (b24, c15). Average over models: near analogy vs far disanalogy 76.9%, near vs near 73.2%, far vs far 45.3%, far analogy vs near disanalogy 33.9% (b24).

**The apparent contradiction.** GPT-4 got 0.86 on 18 far story analogies (Lewis and Mitchell), yet 29.1% on ARN far-near. In the story items the wrong story shares surface events without the causal structure, and the correct story is two-way. ARN's far-near distractors share surface with the query. This is a task difference, not an error (critique). Reading: "LLMs fail far analogies" holds when surface lures are present.

**Order and paraphrase.** GPT-4: 1.0 when the correct story is first, 0.72 second. Humans 0.78 both orders. Paraphrasing the correct story dropped GPT-4 from 0.86 to 0.72 and humans from 0.78 to 0.70. With 18 problems the authors say the difference is hard to call (b19).

**Counterfactual letter strings.** Accuracy over all alphabets: humans 0.753; GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (model-to-number mapping read from a scrambled table). Webb et al. reply: GPT-4 with code matched humans (P=0.496); without code it did not (P=8.9e-13). 46% of GPT-4 errors were valid alternative rules vs 39% of human errors (b22, c11). Hodel and West: memorisation not ruled out (b21, c10). Lewis and Mitchell found their GPT runs below the human average even on the original problems, unlike Webb (c07). Contested (K13); one lab ran the code test.

**Re-representation.** Musker et al. 2025: the best models (GPT-4, Claude 3, Llama 405B) reach human level on many conditions. They fail the permuted-pairs control (coefficients -1.68, -1.78, -2.34; humans unaffected) and depend on example order. Study 2: Claude 3 about 0.70 reference match, same as humans (coef 0.21, p=0.64); GPT-4 and Llama-405B about 0.35 (GPT-4 coef -1.37, p=0.002). Prompt variants moved scores from near 0 to 40% in one condition and from 20% to 100% in another (b23, c12, c13).

**Long and surface-rich input.** AnaloBench: GPT-4 falls from 89.1% to 60.7% as stories grow from 1 to 30 sentences. Humans go 96.0 to 73.3. The gap grows from 6.9 to 28.8 points. GPT-3.5: 65.3, 46.4, 30.8. Retrieval from 200 stories: recall@3 42.9% at 1 sentence, 6.5% at 10, 3.9% at 30 (random 1.6%) (d03).

**Story analogy identification.** StoryAnalogy 4-way: random 25%, humans 85.7%, ChatGPT 32.4%, GPT-3.5 37.1%, LLaMa-65B 28.6%, FlanT5-xxl 45.4%, retrieval baseline 44.9% (b25). Model scores come from a garbled table.

**Judge precision.** In a Gick-and-Holyoak-style matching task GPT-4 found all relevant sources when hinted but also accepted wrong ones (precision about 0.50). Without a hint it never claimed the correct story (d06).

**Frontier 2025-26.** ARCANA (grid transforms from real-world sources), total solved over 12 attempts with/without typo credit: GPT 5.2 51.20% / 48.33%, Gemini 3 Pro 43.06% / 29.19%, Grok 4.1 Fast 24.88% / 18.66%, Claude Opus 4.5 8.61% / 7.18%. Humans pass@1 68.96% / 58.35% (d07). Between-model differences are huge. A ranking study found frontier closed models do well on narrative analogies (MAP 0.8158 Claude Opus, 0.8181 GPT-5.2) while small open models are far lower (Llama-8B 0.2987) (d09). Different formats, so not comparable to ARN.

**Inside the model.** Patching hidden states fixed up to 38.4% of wrong proportional-analogy cases in open models. Probes reached 82.9% in mid layers. Relational information is present but not applied to new entities (d10). Not usable by a prompt-only agent.

**What changed performance, and by how much.**
- Solved CoT demonstrations that first extract the message: up to +30 on far (c17).
- Abstraction before mapping: MCQ 0.17 to 0.46 (d01).
- Question-form relations: top-1 mapping precision 0.48 to 0.82 (c19).
- Code tool: closes the human gap on counting-heavy letter strings (b22).
- Self-generated analogies: +2.8 / +4.3 points, strong models only (c20, c21).
- Scale: GPT-3 to GPT-4 lifted ARN near-far to 94%, but far-near stayed 29.1%.
- Structure scoring: no net win shown. The 8B mapping scorer beat zero-shot by 0.04 on Llama far and lost by 0.05 on Qwen far (d01).

**Caveats.** Nobody tested a systematicity score used as an agent step (critique). Most models tested are 2023-2024. Analogical prompting (Yasunaga, Thought Propagation) is not structure mapping and must not be counted as support. Thought Propagation's gains come with several solver calls and, in creative writing, analogs that are paraphrases of the input (c23).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Do not trust one model judgment that an analogue "matches" when the candidate shares surface with the query. Strong models sit at or below chance on far analogies with surface lures. An O7 analogue must pass a code-run or held-out check before it steers the answer (extends G3, G5). | G (O7 precondition) | [E] | K11; a26, b24, c15, c16, b17, c03, d07, d12, d01 |
| Add an anti-shortcut ablation to the bench. Hide the A:B pair, or run embedding-only. If accuracy survives, the item does not test mapping. | G (bench hygiene) | [E] | K18; c16, b26, c30 |
| Judge soundness on relations, not on shared objects or words. Any rating prompt or code score must count shared relations and cause chains, not shared entities. | O7 check | [E] | K03; b05, b06, a30, b17, c03 |
| Do not use "looks similar" as proof that an inference follows. Keep a similarity score and an inference-support check separate. | O7 | [E] | K07; a19-a21, b10, b12 |
| If self-generated analogies are used as an O7 variant, they must beat the same tokens spent on extra samples, and only on strong models. Gains are small (+2.8 to +4.3). | O7 | [E] | K16; b27, c20-c23 |
| If relations are extracted, ask in question form or with abstraction, never as raw verb phrases (raw 0.17 vs 0.25 chance; question form 0.82 vs 0.48). | O7 front end | [E] | K17; a29, c19, d01, d15 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Score candidate mappings by trickle-down over a typed relation graph, in code. | G / O7 | [S] | K09, K10; a12-a17, b08, b09 |
| Extract-relations-then-map beats direct LLM mapping at equal tokens. | O7 | [S] | K21; d01, d02 |
| A "state the high-level message" step, on far cases only. Costs near accuracy. | S1 / O7 | [S] | K15; c17 |
| Retrieve stored cases by a one-line purpose and mechanism summary, not raw text. | memory | [S] | K24, K04; d04, d05, b07 |
| Compress cases to relations before comparing or retrieving (bottom-heavy swamping). | memory / O6 | [S] | K10, K23; a16, a17, d03 |
| Swap option order and paraphrase; treat disagreement as a failure flag. | G | [S] | K12; a27, b19 |
| Choose the richer, more causally connected case as base. | O7 | [S] | K20; d08, a11 |
| Apply systematicity scoring only when objects are cross-mapped or ambiguous. | O7 gate | [S] | K05; a08, a09, b04 |
| Precision-oriented verify of the causal chain before accepting a retrieved analogue. | S8 / O7 | [S] | K22; d06 |
| Two abstraction levels, keep the one where the top two mappings differ most. | O6 / O7 | [S] | K25; d02, d15 |
| Code tool for counting-like steps in structure tasks. | O | [C] | K13; b20-b22, c06, c11 |
| Two post-mapping variants: pure structural score vs score then causal-model check. | O7 | [C] | K08; a22, b11, b13 |
| Smaller thinking budget favors local matching; larger favors connected mapping. | S/O budget | [S] | K06; b14 (secondary only) |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, counting setup and extraction. Same model unless the test varies it. Include a plain arm and a best-of-N arm at the same budget (G7, G9).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARN-style far-near and far-far triples, 100+ items | (A) plain; (B) extract events, abstract, map one-to-one, score; (C) extra samples at same tokens | Accuracy per partition | B above A on far-near, at or below A on near. If B does not beat A and C at equal tokens, drop it (K21). |
| T2 | Same items, agent's own model | thinking off vs on, same token cap | Far-near accuracy | Shows whether failure is a budget issue (K26). Expect little change (G11). |
| T3 | Clement-and-Gentner-style items: connected vs isolated fact (30+ new passages) | plain; connected-structure prompt; code trickle-down on extracted graph | Rate of picking the connected fact (human .53 vs .12) | Structure arm above plain. |
| T4 | T3 items with base hidden after a lossy summary | prose summary vs relation-list summary | Connected-pick rate | Relation summary preserves the effect better (K02, K23). |
| T5 | Retrieval of stored cases for new problems | raw-text key; purpose+mechanism line; relation list | Top-3 hit of structure-matched case; downstream pass rate | Relational key beats raw on far items (K04, K24). |
| T6 | Same analogy at 1, 10, 30 sentences | raw; compressed to relations; trickle-down scorer on extracted graph | Accuracy by length | Compression flattens the length drop (K23, K10). |
| T7 | Lee and Holyoak items (shared vs missing preventive cause, blank features) | similarity; inference strength; both in separate fresh contexts | Rank order of conditions on each measure | Check for similarity-up, strength-down (K07; gap 5). Cheap: 9 arguments. |
| T8 | Any analogy item set | single run; both orders; both orders + paraphrase | Accuracy on agreement vs disagreement | Disagreement predicts error (K12). |
| T9 | Any analogy item set | hide A:B; embedding-only | Accuracy drop | Remove items whose accuracy survives (K18). |
| T10 | Two sources, one correct, one surface-similar | judge alone; judge + chain-alignment check | Precision and recall of accepted analogues | Precision rises from about 0.50 (K22). |
| T11 | Near, far-far, far-near items | low abstraction; high abstraction; margin pick | Accuracy per partition | Margin pick matches best fixed level (K25). |
| T12 | Mixed easy and cross-mapped items | always score; score only when cross-mapped; never | Accuracy and tokens | Same accuracy on hard items, fewer tokens on easy (K05). |

## 9. What does not transfer, and why

- **Child development results (Gentner and Toupin).** Our agent is not developing. The result only supplies a boundary: systematicity matters when the mapping is hard.
- **Retrieval by surface overlap.** In people, surface drives recall (.78 vs .44). An LLM with a text memory behaves the same way through embeddings (38.5 vs random 37.6). A warning, not a design to copy.
- **Reaction-time results (700-1000 ms).** An agent has token budgets, not milliseconds. The finding came through a review only (b14).
- **Hand-coded predicates.** SME's published numbers use hand-written symbolic input. Getting predicates from text is the open step (c14, d15). The 6.03 / 4.04 / 1.87 scores are not what extracted graphs will give.
- **Ordinal fit of SME to human ratings.** Three triads or five story sets, no statistics (a14, b08). Not evidence that the scorer beats an LLM judge.
- **Undergraduate samples with short written stories, one lab.** Not expert agents with long contexts.
- **Analogical prompting (Yasunaga, Thought Propagation).** Analogy as a prompt device, not a structure score (c23).
- **Hidden-state patching and probes.** Not available to a prompt-only agent (d10).
- **Training-based retrieval gains (RA-RFT).** They train both retriever and model. They show relevance is not similarity, not that a prompt will fix it (d05).
- **Proverb as proxy for system mapping.** ARN's far analogies share a proverb, a coarse stand-in for a connected relational system (a25). A far-near win on ARN need not carry to real causal systems.

## 10. Open questions

1. Does scoring a mapping by connected higher-order structure beat a plain LLM judge at equal tokens on far analogies with surface lures? No study (K21, K27). Closest: YARN at 8B, no token counts.
2. Has Clement and Gentner 1991 been replicated by an independent lab, with effect sizes and expert samples? None found (d13). The search was limited by rate limits.
3. How accurate is LLM relation extraction, and how much does extraction error cost the final score? Not measured in Sultan and Shahaf or YARN.
4. Does the trickle-down scorer still prefer the right mapping on bottom-heavy cases, and does re-representation fix it? Nobody tested the scorer on AnaloBench-style length changes.
5. Does the Lee and Holyoak dissociation appear in LLMs? None found (d14).
6. What predicts a wrong connected system (misleading causal chains)? Untested.
7. Do reasoning models still fail ARN far-near, and do thinking budget or tools change it? No retest (d11, K26).
8. What is the token cost of a mapping-score step against best-of-N, and where is the break-even? No study (d14).
9. Does choosing the richer case as base improve LLM inference accuracy? Shown only in people (d08).
10. Do the trickle-down value 0.8 and the working region 4-16 hold when the graph is LLM-extracted and noisy? Tuned on three hand-coded triads.
11. Does a higher-order score help when the "systems" are code or math, not stories? Not found.
12. Which account of the dissociation (causal model vs map-then-infer) predicts LLM behaviour better? Open (K08).

## 11. Sources

[V] = opened and read as page or PDF text this session. [M] = snippet, abstract only, or secondary report.

- [V] Gentner (1983) Structure-mapping: a theoretical framework for analogy. https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf
- [V] Clement and Gentner (1991) Systematicity as a selection constraint in analogical mapping. https://groups.psych.northwestern.edu/gentner/papers/ClementGentner91.pdf
- [V] Gentner and Toupin (1986) Systematicity and surface similarity in the development of analogy. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1003_2 and https://groups.psych.northwestern.edu/gentner/papers/GentnerToupin86.pdf
- [V] Gentner, Rattermann and Forbus (1993) The roles of similarity in transfer. https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf
- [V] Gentner and Markman (1997) Structure mapping in analogy and similarity. https://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman97.pdf
- [V] Falkenhainer, Forbus and Gentner (1989) The Structure-Mapping Engine. http://www.qrg.northwestern.edu/papers/Files/smeff2%28searchable%29.pdf and https://groups.psych.northwestern.edu/gentner/papers/FalkenhainerForbusGentner89.pdf
- [V] Forbus and Gentner (1989) Structural evaluation of analogies: what counts? http://www.qrg.northwestern.edu/papers/Files/esenfin%28searchable%29.pdf
- [V] Bowdle and Gentner (1997) Informativity and asymmetry in comparisons. https://groups.psych.northwestern.edu/gentner/papers/BowdleGentner97.pdf
- [V] Gentner and Forbus (2025) The Structure-Mapping Engine: a multidecade interaction. https://groups.psych.northwestern.edu/gentner/papers/GentnerForbus-2025-SME.pdf
- [V] Lee and Holyoak (2007) Causal models guide analogical inference. https://escholarship.org/uc/item/7714650n
- [V] Colhoun and Gentner (2009) Inference processes in causal analogies. https://groups.psych.northwestern.edu/gentner/papers/Colhoun_Gentner_SOFIA_042709.pdf
- [V] Myers and Gentner (2017) Analogical inferences in causal systems. https://escholarship.org/uc/item/9cq5c1r7
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Webb, Holyoak and Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in large language models. https://arxiv.org/abs/2411.14215
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning. https://arxiv.org/abs/2402.08955
- [V] Hodel and West (2023) Response: emergent analogical reasoning. https://arxiv.org/abs/2308.16118
- [V] Musker, Duchnowski, Milliere and Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803
- [V] Sourati, Ilievski, Sommerauer and Jiang (2024) ARN: Analogical reasoning on narratives. https://arxiv.org/abs/2310.00996
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874
- [V] Sultan and Shahaf (2022) Life is a circus and we are the clowns. https://arxiv.org/abs/2210.12197
- [V] Stevenson et al. (2023) Do large language models solve verbal analogies like children do? https://arxiv.org/abs/2310.20384
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Yu, He and Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965
- [V] Bhavya, Xiong and Zhai (2022) Analogy generation by prompting large language models. https://arxiv.org/abs/2210.04186
- [V] Yuan et al. (2024) AnalogyKB. https://arxiv.org/abs/2305.05994 (abstract, intro, part of tables)
- [V] Wijesiriwardene et al. (2023) ANALOGICAL. https://arxiv.org/abs/2305.05050
- [V] Mitchell, Palmarini and Moskvichev (2023) Comparing humans, GPT-4 and GPT-4V on abstraction (ConceptARC). https://arxiv.org/abs/2311.09247
- [V] Ushio et al. (2022) BERT is to NLP what AlexNet is to CV. https://arxiv.org/abs/2105.04949
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/abs/2603.29997
- [V] Ye, Wang, Choi et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370
- [V] Hope, Chan, Kittur and Shahaf (2017) Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585
- [V] RA-RFT authors (2026) Learning to reason by analogy via retrieval-augmented reinforcement fine-tuning. https://arxiv.org/abs/2606.13680 (first authors not recorded)
- [V] Authors not recorded (2025) Can LLMs help improve analogical reasoning for strategic decisions. https://arxiv.org/abs/2505.00603
- [V] ARCANA authors (2026) ARCANA benchmark. https://arxiv.org/abs/2610.29271
- [V] Authors not recorded (2026) When models know more than they say. https://arxiv.org/abs/2604.03877
- [V] Authors not recorded (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344
- [V] Wikipedia, Structure-mapping theory (secondary summary only). https://en.wikipedia.org/wiki/Structure-mapping_theory
- [M] Lassaline (1996), causal structure in category-based induction, as described by Colhoun and Gentner. https://groups.psych.northwestern.edu/gentner/papers/Colhoun_Gentner_SOFIA_042709.pdf
- [M] Holyoak and Thagard (1989) ACME, as discussed by Forbus and Gentner and by Lee and Holyoak. http://www.qrg.northwestern.edu/papers/Files/esenfin%28searchable%29.pdf
- [M] Hofstadter and Mitchell (1995) Copycat, second-hand via Musker et al. No URL opened.
- [M] Goldstone and Medin (1994); Ratcliff and McKoon (1989), deadline result via Gentner and Markman 1997. Not opened.
- [M] Search records for independent replication, LLM dissociation test and token-cost comparison (Crossref, Europe PMC, arXiv listings; absence is not proof). https://api.crossref.org/works and https://arxiv.org/search/
