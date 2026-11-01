# Conceptual combination (noun-noun): deep document

*Subfield A09.04 of creative cognition. Built from evidence_a-d.jsonl (ids a01-d16), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids in brackets. Status marks: [E] established, [S] single-source, [C] contested. Almost no human study here is newer than 2000; almost all LLM work is 2021-2026 and tests older or mid-size models.*

## 1. What it is

Conceptual combination is how two concepts merge into one. "Pet fish", "garden furniture", "chocolate crocodile", "zebra clam". The question is how a person (or model) gets the meaning of the whole from the two parts, when the whole is more than a list of the parts' features.

Three kinds of phrase matter:
- **Conjunctions** ("sports which are games", "pets which are birds"). Hampton's work. The question is category membership and attribute inheritance.
- **Noun-noun compounds** ("elephant frog", "banana table"). Wisniewski, Gentner, Gagne, Shoben, Costello, Keane. The question is which reading people build.
- **Adjective-noun phrases** ("brown apple", "fake gun"). Smith et al. Related, used only as side evidence.

Why it matters for our agent. Our open mode (S3 in open mode, O7 map an analogue, O8 reframe) will take seed pairs from distant domains and merge them to get ideas. That is conceptual combination done by a model. The human literature says what a merge normally contains (mostly inherited features, little true novelty), what makes it richer (conflict between parents, scenario building), and what readings exist. The LLM literature says where models fail (finding the shared abstraction, emergent properties) and that different models produce the same blends.

Scope notes. Conceptual blending (Fauconnier and Turner) and analogy have their own subfield documents in this series; here they appear only where a number links them. Creativity-as-search, fixation and ideation, and combinational creativity are covered in parallel documents.

## 2. History and theories in depth

**Feature-set and prototype era (1980s).** Smith, Osherson, Rips and Keane (1988) proposed the Selective Modification Model for adjective-noun phrases. A modifier moves all "votes" in one slot (colour) to one value and raises that slot's weight. It predicts that a brown apple is a better "brown apple" than an "apple". Hampton calls it over-specified: moving the votes alone gives the same prediction [a11]. It works for intersective adjectives, not for noun-noun relations.

**Hampton's composite prototype (1987, 1988).** Take the union of the parents' attributes, weight them by their importance in each parent (a weighted average), apply a necessity constraint (an attribute necessary for either parent stays) and a coherence repair (conflicting attributes are dropped or changed). Category membership then comes from similarity to this composite above a criterion. The same mechanism handles typicality and class membership (the "unitary" hypothesis) [a04, b21, a06]. Predictions that held:
- Overextension: items accepted in "A and B" but rejected from A alone [a01, a02].
- Compensation: strong fit to one parent offsets weak fit to the other [a02, b03].
- Dominance and non-commutativity: one parent counts more; "A which are B" differs from "B which are A" [a04, a10].
- Inheritance with exceptions: necessary attributes pass on; conflicting generic ones can fail ("warm and cuddly" does not carry to pet fish) [a06].

**Emergence debate.** Murphy (1988) showed emergent properties in combinations (casual shirts are pulled over the head). Hampton and Rips argued these come from peeking at known instances (the "No Peeking Principle"), not from computing from the parts [a12]. Hampton's resolution: emergence has two routes. Extensional feedback (pet birds talk, known from real instances). Scenario construction (pet birds live in cages, worked out from the conflict between "wild" and "pet") [a05].

**Relation-based theories (1990s).** Gagne and Shoben's CARIN: a modifier carries a distribution over 16 thematic relations (LOCATED, DURING, FOR...). The reader picks one. Availability depends on how often the modifier has gone with that relation [a16]. Priming a relation speeds the next compound that uses it [a18]. Maguire et al. (2007) reanalysed the competition claim and found it unsupported [a17].

**Wisniewski and Gentner: dual-process / structural alignment.** Relation linking is only one route. Property mapping ("elephant frog" = a large frog) and hybrids ("zebra horse") also occur. Wisniewski (1997) adds two processes: comparison (align the two nouns) and construction (build a new structure when alignment is not enough). Hybrids rise as the nouns get more similar, which is the evidence for alignment [b09, d09, d15]. The meaning must make a new category that differs from the head in a way tied to the modifier [d15].

**Costello and Keane C3 (2000).** Constraint-guided combination with three pragmatic constraints: diagnosticity (the modifier's features should be those that identify it), plausibility, informativeness (the phrase must say something new). Creativity arises because the constraints can be met in many ways. We could not open the paper, so human-match numbers are not in our evidence [a22, b23, c28].

**Quantum-probability models (2010s-2026).** Aerts, Sozzo and colleagues: Hampton's membership data cannot sit in one classical (Kolmogorov) probability space. Example: Mint is 0.87 food, 0.81 plant, 0.90 food-and-plant [a19, a21, b12]. A Fock/Hilbert model with interference fits. Hampton replies that a sequential-projection quantum model cannot give double overextension, and that his 1988 data had about 10 participants per item, too few for complex fits [a20, b11]. Aerts et al. (2026) report that ChatGPT and Gemini violate a Bell inequality on a combined concept; values above the Tsirelson bound mean the method is suspect [a28].

**Language-model era (2021-2026).** Work splits into (a) interpretation of compounds (paraphrase, relation choice), (b) property and emergence generation, (c) combinational creativity benchmarks (KOMBINE), (d) pipelines (PopBlends), (e) vision-language models, (f) representation probing.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Overextension: items accepted in "A and B" but rejected from A | Exp 1: 8 compounds, 127 items; 93 items more likely in the conjunction, 22 the reverse; 66% rejected "all garden furniture is furniture" | Hampton 1988 [a01] | [E] K01 |
| Chess is a game but not a sport, yet counted in "sports which are games" | 61% would not call chess a sport; 51% rated it in the conjunction. Of games that were not sports 25% got positive conjunction ratings; of sports that were not games 54%. About 8-9 per cell, 35 total | Hampton 1988 Exp 2 [a02] | [E] K01, K02 |
| Not noise: a contrast-plus-random-variability model fails | Mean recall parameter u=.512; fitted model predicted overextension far below observed | Hampton 1988 [a03] | [E] |
| Overextension with pictures | Letters 163 over vs 46 under; faces 239 vs 51; 34 participants over-extended more, 8 the reverse (z=3.86, p<.001) | Hampton 1996 [a08, b01] | [E] K01 |
| Survives change of base rate and yes/no format | Exp 2: 32 per condition; positive conjunctive categorisation letters 27% vs 26%, faces 33% vs 39%; augmenting items in both categories raised face double overextension 6% to 16% | Hampton 1996 [b02] | [E] |
| Vaguer dimension is overextended more | Age 50% vs emotion 20% at similar boundary sharpness; augmented condition: age 30% to 41% | Hampton 1996 Exp 3-4 [a09] | [E] |
| Compensation | Independence predicts 25% positive conjunction at 50%/50%; observed 26-39% | Hampton 1996 [b03] | [E] K02 |
| Geometric-average rule for membership; negated conjunctions also overextended | Two experiments, "Tools which are also Weapons" | Hampton 1997 [a10] | [E] K02 |
| Guppy effect is real but rarer than simple overextension | Cited, not re-measured | Storms et al. via Hampton 2013 [b11] | [E] K21 |
| Emergent attributes are rare in ordinary conjunctions | 3 of 174 attributes emergent (strict), 11 (lenient). Of 37 attributes unimportant to both parents, about 8% important for the conjunction. More emergence for low-overlap pairs (pets/birds) than high-overlap (sports/games) | Hampton 1987 via 1996 chapter [a05, b04] | [E] K03 |
| Negated conjunctions cut the logical route to new attributes | 6 pairs, 51 attributes with median 0% for head; 24 stayed 0%, 11 slightly broke it, only 6 reached 10%+. Those 6 are mostly category stretching (tent as dwelling) | Hampton 1989 data [a07, b05] | [E] K03 |
| Evaluative (antagonistic) pairs produce emergence | 4 pairs, 210 attributes. Of 65 true of own side, 11 (17%) inherited. Of 80 true of the other side, 55 (69%) inherited. Of 63 false for both, 22 (35%) true of the conjunction | Hampton, Dillane, Oren via 1996 chapter [a07, b07] | [S] K04 |
| Impossible combinations force repair and emergence | 9 pairs, 20 subjects; about 220 attributes mainly from one parent vs about 170 emergent (informal count) | Hampton 1996 chapter [b08] | [S] K04 |
| Traits: congruent pairs inherit fully | 31 of 32 inherited; incongruent: 16 of 25 inherited, 9 not; no emergence | Hampson 1990 via chapter [b06] | [S] |
| Noun pairs are not only relations | 400 phrases, 20 subjects; only 40% described as a relation; about 30% property form; 87% rater agreement (these two figures unverified, OCR) | Wisniewski and Gentner 1991 [b09] | [E] K05 |
| Mass-noun modifiers | 59 of 100 described an object made of the mass; mass-animal: animal lost reference in 26 of 27; mass-artifact: kept it in 21 of 32 when function preserved | W and G 1991 [b10] | [S] |
| Construal | 3,003 meanings of 224 novel combinations from 189 subjects; 70% construed a referent atypically | Wisniewski 1996a via 1997 [d09] | [S] |
| Similarity drives property mapping | 72% (high similarity) vs 48% (low) | Wisniewski 1996 via Bock and Clifton [a14] | [C] K06 |
| Salience drives property mapping | 79% (salient modifier feature relevant to head) vs 23% and 16% | Estes and Glucksberg 2000 via B and C [a14] | [C] K06 |
| Similarity does not predict property mapping once pairs are randomised | 160 pairs, 8 groups of 20; similarity mean 2.64/7; r=-.06 (nat. kinds -.08, artifacts -.22) | Bock and Clifton 2000 [a15] | [C] K06 |
| CARIN competition not supported | r .44 to .34 without free parameter; RT vs competitor distance r=-.09 (N=28), .08 (N=26); 1,030 vs 1,073 ms | Maguire et al. 2007 [a17] | [C] K07 |
| Relation priming is real | 224 ms (dominant relation prime), 143 ms (subdominant) faster | Gagne and Shoben 2002 [a18] | [S] K07 |
| Ontological type predicts meaning type (event/perceptual/environmental %) | Art-art 93/7/0 (N=195); nat-art 88/12/0 (157); art-nat 66/34/0 (157); nat-nat 15/34/51 (148) | Levin et al. 2019 via Li et al. [a25] | [S] K08 |
| Quantum fit to overextension data | Mint 0.87/0.81/0.90; refrigerator 0.9/0.7/0.575 (or); TV 0.7/0.9/0.925 | Aerts et al. 2014, 2016 [a19, b12] | [C] K20 |
| LLM Bell test | Human CHSH 2.4197; ChatGPT 2.25 and 3.09 (mean 2.67); Gemini 2.12 and 4 (mean 3.06); bound 2.83 | Aerts et al. 2026 [a28] | [C] K20 |
| GPT-3 matches human relation mix for novel compounds, not nonsense words | 38 compounds x 3 prompts x 4 temps = 456 generations; kappa .844; r up to .93; nonsense words r=.105; 30% of exclusions were head/modifier inversions | Li, Carlson, Potts 2022 [a24, c05, c06] | [S] K09 |
| GPT-3 paraphrases compounds | Familiar 95.64%; novel (105 items) 83.81% vs human 73.33%; 97% vs 80% copied n-grams; BERTScore 91.94, ROUGE-L 47.31, METEOR 56.27 | Coil and Shwartz 2023 [b17, b18, c01-c04] | [S] K10 |
| Open 7B models are weak | Lexicalised 38-45% by surprisal (Llama-2 inst 44.8, Mistral 42.2, Falcon 38.0; GPT2-xl 33.8; BERT-large 26.2); concreteness coefficient 0.703; Mistral novel-compound same-head .578 (1-shot) vs same-modifier .469 | Rambelli et al. 2024 [c07-c09] | [S] K11 |
| Spelling out the linking event helps | GPT-4o novel same-head 51.4 to 55.7, 52.0 to 57.8, 52.8 to 58.3; lexicalised 69.6 to 74.4; Mistral same-modifier 30.5 to 51.3; about 55% of compounds have more than one reading; GPT-4o 10-15 points lower on novel | Ye, Tu, Pustejovsky 2025 [d10, d16] | [S] K28 |
| Emergent properties are hard for LLMs | 12,315 triples; GPT-4o judges property presence 82.6% (95.6% yes, 69.6% no); property type 56.4% vs human 81%; human majority label accuracy 87% emergent, 79% component, 76% canceled | Song et al. 2025 CCPT [a26, b13, b14] | [S] K12 |
| Spread-activation prompt gives little | Emergent 45.1 to 45.8, canceled 60.5 to 63.3; filter ablation +1.2 emergent, +7.7 canceled; SEM up to 1.7 | Song et al. 2025 [a27, b14] | [S] K12 |
| Blending is the hardest combinational task | 35 LLMs: association 59.0%, analogy 53.4%, blend 43.4%. Given a valid generic space, coherent blend 97.1% | Schapiro et al. 2025 KOMBINE [c11, c12] | [S] K13 |
| Humans score lower than LLMs on validity | Humans (N=75): 22.1 / 32.9 / 12.8% vs LLM 59.0 / 53.4 / 43.4% | KOMBINE [c14] | [S] K15 |
| Models invent the same properties | 19.9% (412/2,070) reuse 2+ properties; blends 37.3% vs analogies 2.6%; same provider 2.3x more likely | KOMBINE [c13] | [E] K14 (general sameness corroborated by d05, d06; blend rates single-study) |
| Pipeline beats free brainstorming | 2.03 vs 0.87 ideas per pair (paired Wilcoxon p<0.001); mental demand 2.85 vs 5.80 (p=0.004); N=10; connecting-concept accuracy 55.3-58.7% | PopBlends [c15, c16] | [S] K16 |
| LMs beat ConceptNet at proposing the shared property | P@1000 66.38 vs about 5.9; P@100 24.84 vs 2.70 | Ge and Parikh 2021 [c17] | [S] K17 |
| Vision-language models weak on compounds | Human 96.25; CLIP 78.25; OpenCLIP 83.90; MetaCLIP 81.35; with LLM captions 86.50 (+8.25 points) and 86.25 (+2.35); nouns reversed 41.00 | Kumar et al. 2024 [a29, b19, c23] | [S] K18 |
| Embeddings compose roughly additively | Cosine to true compound: addition .852, weighted .854, ridge .922; Mistral .854 / .914; multiplication -0.038 | Nagar et al. 2025 [c21] | [S] K19 |
| Old LMs fail adjective-noun inference | Human 94.3%; GPT-2 71.75%; non-local adjective humans 89.8% vs RoBERTa 19.3% | Rodriguez et al. 2024 [c10] | [S] K22 |
| Large LMs give human-like membership for novel adjective-noun pairs | 798 bigrams; 75.3% human-like by log-prob, 61.4% by generated context; Llama-3-70B JS divergence 0.17 vs uniform baseline 0.34, majority 0.40, Llama-2-7B 0.38 | Ross et al. 2024 [b15, b16] | [S] |
| Structure-first analogy step | 2 calls vs 2 (cross-domain) vs 1 (no-domain). Novel-solution rate Claude 1.6 / 21.6 / 50.4%; Gemini 8.9 / 37.8 / 68.9%; diversity +90-173%; human check AR more novel 78% (kappa .445, 50 pairs) | Shen et al. 2026 [d01] | [S] K25 |
| Far analogies gave downstream gains | Domain distance 6.99 / 6.83 / 7.53 vs no-domain 2.29 / 3.08 / 3.37; 4 implemented cases; about 13-fold on one metric; Spearman .729 | Shen et al. 2026 [d02] | [S] K26 |
| Diversity needs varied inputs plus structure | Persona+CoT 248 unique category combos vs human 197, default 88; evolved personas +78.8% vs random +8.7%; temp 1.5 marginal; min-p T=2.0 left 81% of pairs above .7 similarity; pooling 40 GPT-4 sessions cosine .428 vs CoT .255 and students .243; creative prompts 0.459 to 0.576 vs humans 0.738; cross-model similarity 71-82% | Deng et al., Meincke et al., Wenger and Kenett, Jiang et al., Moon et al. [d03-d07] | [E] K27 |
| Repeated sampling collapses | 4,000 seed ideas per topic, about 5% left after de-duplication at cosine .8 | Si et al. 2024 [d08] | [S] |
| Humans name image pairs more diversely | Greater semantic distance and entropy than multimodal LLMs | Ali et al. 2026 [c25] | [S] K23 |

## 4. Mechanisms and models

Each is written so it can be coded.

### 4.1 Composite prototype (Hampton)
Input: attribute sets A_attrs and B_attrs, each attribute with an importance weight in its parent.
1. Union all attributes.
2. Importance in the blend = weighted average of importance in A and in B (a dominance weight w for the head, 1-w for the modifier; w differs by order, which gives non-commutativity). Hampton 1997 found the membership rule is a geometric average of constituent membership values [a10].
3. Necessity: any attribute with importance above a high cutoff in either parent stays in the blend.
4. Impossibility: any attribute impossible for either parent is impossible for the blend.
5. Conflict repair: if two kept attributes conflict (wild vs pet), drop the weaker or change one concept.
6. Membership of an item = similarity of the item to the composite above a criterion.
Prediction for code: an item with high membership in A and middling membership in B ranks as a member of A-and-B more often than a strict intersection predicts. Use as a probe, not a component.

### 4.2 Route chooser (Wisniewski and Gentner, Wisniewski 1997)
For a pair (M, H):
1. Relation linking: pick a relation r so that "H that r M". Slot-filling, minor change to H.
2. Property mapping: pick a salient property p of M that fits a dimension of H; result is "H with p" (zebra clam).
3. Hybrid: align the two nouns; build an object that is both (zebra horse). Possible only when functions do not conflict; likelier when nouns are similar.
4. Construal: treat one noun as a part, material or related thing (tiger chair = covered in tiger skin).
Implementation: ask for all three or four readings separately, then keep distinct ones. Choosing by similarity is contested [a14, a15].

### 4.3 Relation inventory and priming (CARIN)
Table P(relation | modifier) from a corpus or from model samples. The reader samples one relation; a recent same-relation example speeds the choice. The competition-based speed claim failed [a17], but the priming effect stands [a18]. For an agent: a prior example with relation r will bias the next blend toward r. This is a hazard (fixation), not a feature.

### 4.4 C3 constraint filter (Costello and Keane)
Generate candidate readings. Score each on:
- Diagnosticity: do the modifier's identifying features show up in the reading.
- Plausibility: could it exist, consistent with what we know.
- Informativeness: does the reading say something not already implied by the head.
Keep readings passing all three. Not tested with an LLM judge (K24, K29). Note G5: a judge model must be blind and length-normalised, or the filter must be done in code (for example an embedding check for informativeness, distance from the head alone).

### 4.5 Emergence routes (Hampton)
- Extensional feedback: recall real instances of the blend, read off properties. Prompt: "list three real or imagined instances of an A-B; what is true of them that is not true of A or B in general?"
- Scenario construction: describe a situation in which both parents hold, notice the conflict, resolve it, record what the resolution implies. Prompt: "Where do A and B clash? What would have to be true for both to hold?"
Both give testable steps. Emergence is more common when parents conflict [b07, b08] and for low-overlap pairs [a05].

### 4.6 KOMBINE decomposition (generic space)
Blending = (1) find the generic space (shared abstraction), (2) build the blend that keeps it. Models fail at step 1 (43.4% valid) and are good at step 2 (97.1% given step 1) [c12]. Implementation: two calls. Call 1: "What abstract structure do X and Y share? Give 3." Code scores each against both inputs (embedding closeness to both, not to only one). Call 2: blend under the best abstraction.

### 4.7 PopBlends fixed pipeline
Stage 1: expand each concept with associations (model plus knowledge base). Stage 2: find connecting concepts (code ranks by overlap). Stage 3: search scenes that merge them. The model fills slots, code ranks. Connecting-concept accuracy about 55-59% regardless of how much GPT was used [c15].

### 4.8 Structure-first analogy (Shen et al.)
Call 1: extract the problem's relational structure and propose far domains. Call 2: solve within each domain. The step gave 21.6% to 50.4% novel solutions on Claude at 2 calls vs 2 [d01].

### 4.9 Quantum model (do not build)
Hilbert-space state, context-dependent projection, interference term. Fits double overextension by a free angle per item. Fit, not prediction [a19, b12, a20]. Skipped.

## 5. What holds up

**Replicated or corroborated.**
- Overextension: Hampton 1988 (words), 1996 (pictures, 4 experiments, base-rate and format controls), 1997 (natural concepts, negation). Same author across all. Three strands (words, pictures, negated forms) but one lab [a01-a10, b01-b03]. Rated [E].
- Dominance and non-commutativity: 1988, 1997 [a04, a10]. [E]
- Emergence rare, mostly inherited: 1987, 1989, 1990 (Hampson), 1996 chapter [a05, b04-b06]. [E]
- Property mapping and hybrids exist beside relation linking: Wisniewski and Gentner 1991, Wisniewski 1996/1997, Davidson and Stevenson 1995, Estes and Glucksberg 2000, Bock and Clifton 2000 [b09, a13-a15, d09]. [E]
- Homogeneity of LLM ideas: KOMBINE, Wenger and Kenett (22 LLMs), Jiang et al. (25 models, 26K queries), Si et al., Meincke et al. [c13, d04-d06, d08]. [E]

**Failed, contested, or weak.**
- CARIN competition. Fit advantage came from a free parameter; no RT relation to competitor distance [a17].
- Similarity as the cause of property mapping. Wisniewski 1996 (72% vs 48%) against Bock and Clifton (r=-.06 once pairs randomised). Likely salience confounded with similarity; Wisniewski's similarity manipulation was extreme (sister terms vs distinct categories) [a14, a15].
- Quantum models. Fit, not forecast. Hampton disputes projection versions; Aerts's Bell values above 2.83 signal method trouble [a20, b11, a28].
- Selective Modification: over-specified [a11].
- Evidence base is thin. Most human data is 1987-2000 with about 10-35 per cell and one lab. Hampton himself says precision was not warranted at n about 10 per item [a19, a20]. No large-sample (N over 200) replication found; the search tools were limited, so this is absence of found evidence, not proof [d13].
- Emergence counts depend on rating thresholds; b08 is an informal count with no inter-rater check. Emergence in negated conjunctions is mostly category stretching [b05].

**Moderators.**
- Parent conflict or incompatibility raises emergence [b07, b08].
- Overlap of parents: low-overlap pairs give more emergence [a05].
- Ontological type of parents: art-art 93% event readings; nat-nat 51% environmental [a25].
- Concreteness and relation class for LLMs: accuracy up with concreteness (coefficient 0.703); per-class 80-94% for FROM, CAUSE2, MAKE2 vs about 15% for a reversed class [c08].
- Word frequency for LLMs: accuracy falls as compound frequency falls [c03]; GPT-4o 10-15 points lower on novel [d10].
- Vagueness of the dimension: vaguer dimension overextended more [a09].
- Prompt shots: more shots can hurt (Mistral same-modifier 0.469 to 0.30) [c09].

**Interventions that worked (LLM).**
- Spelling out the linking event: +4 to +6 points GPT-4o, +9 to +21 open models [d10].
- Fixed-step pipeline: 2.03 vs 0.87 ideas per pair, N=10, no quality rating [c16].
- Structure-first analogy step: novel-solution rate 21.6% to 50.4% (Claude) at equal call count [d01]. Not a blend task.
- Persona plus CoT: 248 vs 88 unique category combos [d03]. Evolved, spread-out personas +78.8% diversity [d07]. Not a blend task.
- LLM-written example captions for CLIP: +8.25 / +2.35 points [c23].

**Interventions that did not work (LLM).**
- Temperature: 1.5 marginal, 2.0 garbled [d03]. Min-p at T=2.0: 81% of pairs still above .7 similarity [d06].
- Pooling many sessions or models: 40 pooled GPT-4 sessions among least diverse (.428) [d04]; cross-model similarity 71-82% [d06].
- Creative system prompts: variability 0.459 to 0.576 vs humans 0.738 [d05].
- Random personas: +8.7% only [d07].
- Spread-activation prompting for emergent properties: 45.1 to 45.8, within error [b14].
- Instruction tuning on open models: not reliable (Falcon instruct worse than base) [c07].

## 6. Language models

**Interpretation of compounds is mostly solved for big models.** GPT-3: 95.64% on familiar compounds; 83.81% on 105 novel ones vs crowd humans 73.33% [b17, c02]. The human baseline is one paraphrase with little incentive, so it is a low bar. GPT-3 copies web n-grams (97% of copied n-grams in correct familiar paraphrases, 80% for novel), so some of the score is recall [b18, c03]. Typical error: head and modifier swap (banana table defined as a banana) [c04].

**But composition may be recall.** With real nouns GPT-3 matches the human relation mix (r up to .93); with nonsense words and definitions in context r=.105; 30% of excluded outputs were inversions [a24, c06]. GPT-4o on relation choice is 10-15 points lower for novel than for lexicalised compounds [d10]. A 2025 Cognitive Science abstract reports that on novel compounds older distributional models beat BERT-base and Llama-2-13b (abstract only) [d11]. No frontier-model test of the nonsense-word idea exists (K29).

**Smaller and older models.** Open 7B models: 38-45% on lexicalised compounds, with poor transfer when the head or modifier is swapped for a hypernym (same-head .578, same-modifier .469 for Mistral 1-shot) [c07, c09]. Eight older neural LMs trailed humans (94.3%) on adjective-noun inference; GPT-2 71.75% [c10]. Larger LMs (Llama-3-70B) reach human-like membership spread for 75.3% of novel adjective-noun bigrams and do as well on zero-frequency as on frequent bigrams [b15, b16].

**Emergence is the weak point.** GPT-4o names property type correctly 56.4% vs human 81%; every model scores 27 or lower on emergent-completion; LLMs do better than humans on canceled properties and worse on emergent [a26, b13, b14]. Spread activation gave +0.7 on emergent (45.1 to 45.8) [b14].

**Blending is the hard creative task.** Across 35 LLMs, blend validity 43.4%, below analogy 53.4% and association 59.0%. The failure is the generic space: found 43.4% of the time; once found, 97.1% coherent [c11, c12]. Humans (Prolific, N=75) were lower on all three, with a hard-task caveat [c14]. The critique notes KOMBINE lists model names that look speculative; use per-model rankings with care.

**Homogeneity.** Models invent the same properties for the same pair: 19.9% reuse of 2+ properties, 37.3% on blends vs 2.6% on analogies, same-provider 2.3x more likely [c13]. This matches general results: 22 LLMs far more alike than humans [d05]; 25 models 71-82% similar [d06]; repeated sampling leaves about 5% unique at cosine .8 [d08].

**What changed outcomes.**
- Explicit relation or linking event: +4 to +6 (GPT-4o), +9 to +21 (open) [d10].
- Fixed pipeline with code ranking: doubled idea count, N=10 [c16].
- Structure-first, far-domain: novel-solution share 1.6% / 21.6% / 50.4% [d01].
- Persona+CoT for diversity: 88 to 248 category combinations [d03].
- Decoding changes, pooling, creative-prompt wording: small to none [d03-d06].

**Other model types.** CLIP and kin: 78.25% vs human 96.25%; reversing order drops to 41.00% (order sensitivity echoes human non-commutativity) [c23]. Text-to-image models treat egg noodle as separate eggs and noodles [c24]. Embeddings compose almost additively (cosine .85 addition, .92 ridge) [c21]. Small autoregressive models keep relation information at the compound's last token [b20]. A German BERT probe recovers compositionality ratings only moderately (about .33-.43) [c22]. Concept structure from the same LLM varies more across tasks than in humans [c20] (not a combination study).

**Bell tests.** ChatGPT/Gemini violate CHSH with values up to 3.09 and 4, above 2.83. That is a method signal, not stronger-than-quantum behaviour [a28]. Ignore for design.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Evidence ids in brackets.

### Add now (established)

1. **G8/O7: do not expect novelty from a merge for free.** Blends inherit most attributes; emergence is rare (3 of 174 strict) [a05, b04, b06]. Treat a blend as a seed for a later test, not as an idea. Part: G8/O7, S3 open mode. [E] K03. No new step; a design principle.
2. **S3 open mode (G4): get diversity from inputs and structure, not decoding.** Do not rely on temperature, creative wording or pooling samples or models to widen blends. Varied inputs plus a structured step work [d03-d07]. [E] K27, K14.
3. **S3 open mode: code draws the seed pairs, spread in embedding space, and logs property overlap across runs.** Cross-model and cross-sample sameness is large (19.9% overall, 37.3% on blends) [c13, d05, d06]. This fits the existing S3 text (code keeps history of directions tried). [E] K14, K27.
4. **G10 note: a fluent blend is not proof of composition.** [a24, c06]. [S] K09 on its own, but consistent with G10 [E]. Keep as a note, no new step.

### Test first

1. **Generic-space step before blending (O7).** KOMBINE bottleneck is step 1 [c12]; structure-first helped on research problems [d01]. [S] K13, K25. Test T1.
2. **Scenario-construction / extensional-feedback step for emergent properties (O7).** Mechanism from Hampton [a05]; LLM weakness on emergence [a26]; spread activation gave no clear gain [b14]. [S] K12, K03. Test T2.
3. **Several construals per pair (O7).** Relation, property, hybrid readings all occur in humans [b09, d09, a13] and about 55% of compounds have more than one reading [d16]; that the readings exist is [E] (K05), that asking for them helps an agent is untested. Test T5.
4. **Run both orders of a pair (O7).** Combination is non-commutative in humans [a04, a10] and CLIP drops 37 points with nouns reversed [c23]. [E] K02 for humans; agent benefit untested. Test T6.
5. **Seed distance band (S3 open mode).** One far-domain win with no near arm [d02]. SCHEMA O7 already says far analogues raise variance and lower the mean. [S] K26. Test T4.
6. **Conflict-driven seed pairs.** Incompatible or antagonistic pairs raise emergence in humans [b07, b08]. [S] K04. Test T2.
7. **Linking-event statement.** +4 to +6 on GPT-4o relation choice [d10]; free generation untested. [S] K28. Test T7.
8. **Fixed expand-connect-select pipeline.** PopBlends at N=10 [c16]. [S] K16.
9. **C3 plausibility / diagnosticity / informativeness filter in code or a blind judge (S4).** Paper unopened [a22]. [S] K24. Test T8.
10. **Persona plus CoT seeds for blends.** Established for ideation [d03, d07]; blends untested. [S] K27 transfer.
11. **LM, not KB, proposes shared properties.** [c17]. [S] K17. Low priority, since our harness has no KB.
12. **Overextension and non-commutativity in frontier LLMs; nonsense-word compounds.** Probes, not operators. K29. Tests T9, T10.

## 8. Concrete tests on our bench

All arms get equal total tokens; setup cost counts (G7). Items are scored in code where possible; model judges are blind to arm and length-normalised (G5, G8).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 generic-space step | 60 distant seed pairs (KOMBINE-style) | A free blend; B two-call "name 3 shared abstractions, code picks the one closest to both inputs, then blend"; same total tokens | Valid-blend rate (valid generic space and coherent blend, blind judge; spot check with 20 human labels); baseline 43.4% | +10 points or more on valid rate [c12, d01] |
| T2 scenario step | 40 pairs, half low-conflict, half incompatible | A plain blend; B blend plus "where do these clash, what must be true for both" plus "three real instances" | Emergent-attribute count per blend (property true of blend, of neither parent; two blind raters, kappa reported); CCPT-style subset (200 items) | +20% emergent properties; larger for incompatible pairs |
| T3 diversity of seeds and structure | 30 problems from our open-mode suite, 4 blends per problem | A same seed pair, plain; B code-randomised pairs spread in embedding space; C B plus persona + draft-then-revise | Property reuse across 3 runs and 2 models (embedding threshold as in KOMBINE); distinct-direction count | Reuse falls from about 37% toward 20% or lower; C lowest |
| T4 seed distance | 30 tasks with a code-checked outcome (our design and puzzle sets) | Near, medium, far seed bands | Downstream pass rate and spread; look for an inverted U | Mean falls with distance, spread rises; far band wins only where the class has a foothold (G12) |
| T5 construals | 50 novel compounds | A one reading; B three construals (relation, property, hybrid), keep distinct | Distinct valid ideas per pair; idea-set diversity | More distinct ideas, no loss in validity |
| T6 order | 40 pairs, both orders | A fixed order; B both orders pooled; C random order | Distinct valid ideas; overlap between orders | Orders differ; pooling adds ideas at 2x cost; loses at equal tokens unless overlap is below 50% |
| T7 linking event | 100 compound relation items (Rambelli-style) and 30 free-blend items | A plain; B state the linking event first | Accuracy on relation choice; valid rate on free blends | +3 to +5 on frontier relation choice; free-blend effect unknown |
| T8 C3 filter | 100 generated blends per arm | A no filter; B code filter on informativeness (distance from head alone) plus plausibility (blind judge); C both | Quality of the top 3 retained vs a random 3, by downstream test | Top-3 quality up when the filter removes head-only blends |
| T9 overextension probe | 40 borderline items in A, B, A-and-B, both orders | Frontier model, 3 temperatures | Share of items with higher membership in A-and-B than in the weaker parent; order effect | Human-like overextension (about 60-70% of borderline items) and asymmetry |
| T10 nonsense words | 20 nonsense compounds with definitions vs 20 real | Single model | Correlation of relation mix with the human type pattern (Levin) | Frontier models keep r above .5; if r collapses toward .1, treat fluent blends as recall |

## 9. What does not transfer, and why

- **Composite prototype membership and overextension.** They explain how people judge membership. The agent's job is generating ideas and answers, not categorising borderline items. Overextension helps as a probe only.
- **Quantum probability models.** Fit, no prediction; free parameters; Bell values over the bound [a28, a19]. Do not build.
- **CARIN competition.** Failed reanalysis [a17].
- **Human effect sizes at n about 10 per cell.** Treat as direction, not size [a19, a20].
- **Human validity as a target.** Humans are below LLMs on valid rate and explore different semantic regions [c14]. Measure novelty and validity apart (K15).
- **Compound interpretation as a separate step.** Frontier models already paraphrase well (83.81% vs 73.33%) [c02]; only small models gain much [d10]. Spend no tokens on a separate interpretation step.
- **Vision-language findings (Compun, egg noodle).** Our agent is text. Order sensitivity is the only link [c23].
- **Embedding additivity.** Interesting, not a scaffold lever [c21].
- **Mass-noun and animal-artifact reference rules.** Human reading rules for short phrases; our blends are not read this way [b10].
- **Evaluative stereotype pairs (socialist stockbroker).** Opinions of imaginers; no tests reported [b07]. Use only for the idea that antagonism raises emergence.
- **Blend quality is not task success.** No study links one to the other (critique). Do not assume it.

## 10. Open questions

1. Does a generic-space step lift valid-blend rate at equal tokens for a frontier model? (KOMBINE shows the bottleneck, never tests a fix.)
2. Do distant seeds help downstream results compared with near seeds, and which distance is best? One study, no near arm [d02].
3. Can blend homogeneity be cut by random seed selection, personas or cross-model pooling at equal tokens? Evidence is from general ideation only.
4. Does a scenario or extensional-feedback step raise emergent properties in LLMs?
5. Do current frontier LLMs show human overextension and non-commutativity, and does it matter for reasoning?
6. Do Costello and Keane constraints, applied by code or a blind judge, raise the quality of retained blends? (Paper unopened.)
7. Is there a large-sample (N over 200) replication of Hampton's overextension and of rare emergence? None found with limited search tools [d13].
8. Do PopBlends-style pipelines beat free blending at larger N without a human in the loop?
9. Does the nonsense-word collapse (r .93 to .105) hold for frontier models?
10. Does blend quality predict task success for an agent?
11. Which of Wisniewski and Gentner's counts (87% rater agreement, 40% relation) survive checking? OCR was garbled.
12. Is the KOMBINE per-model ranking reliable? The model names look speculative.

## 11. Sources

Marks: [V] opened this session; [M] snippet or abstract only.

**Human founding work and theory**
- [V] Hampton (1988) Overextension of conjunctive concepts. https://www.staff.city.ac.uk/hampton/PDF%20files/hamptonjep88.pdf (a01-a04)
- [V] Hampton (1996) Conjunctions of visually based categories. https://www.staff.city.ac.uk/hampton/PDF%20files/HamptonJEP%2096.pdf (a06, a08, a09, b01-b03)
- [V] Hampton (1996) Emergent attributes in combined concepts (chapter; includes 1987, 1989, Hampson 1990, Hampton-Dillane-Oren). https://www.staff.city.ac.uk/hampton/PDF%20files/Creative%20concepts%201996.pdf (a05, a07, b04-b08)
- [V] Hampton (1997) Conceptual combination: conjunction and negation. https://www.staff.city.ac.uk/hampton/PDF%20files/Hampton%20ConjNeg%20M&C%201997.pdf (a10; cell counts not extracted)
- [V] Hampton (1996) Conceptual combination chapter (Lamberts). https://www.staff.city.ac.uk/hampton/PDF%20files/Hampton%20ConceptComb%20Lamberts96.pdf (a11-a13)
- [V] Hampton (2013/2014) Extension and intension commentary. https://www.staff.city.ac.uk/hampton/PDF%20files/TOPICS%202013.pdf (a20)
- [V] Hampton (2013) Commentary on Pothos and Busemeyer. https://www.staff.city.ac.uk/hampton/PDF%20files/Hampton%20BBS%202013%20Pothos.pdf (b11, b21)
- [V] Wisniewski and Gentner (1991). https://groups.psych.northwestern.edu/gentner/papers/wisniewski%26Gentner_1991.pdf (b09, b10; OCR poor)
- [V] Wisniewski (1997) When concepts combine. https://link.springer.com/content/pdf/10.3758/BF03209392.pdf (d09, d15)
- [V] Bock and Clifton (2000) Role of salience. https://link.springer.com/content/pdf/10.3758/BF03211838.pdf (a14, a15)
- [V] Maguire, Devereux, Costello and Cater (2007) CARIN reanalysis. https://mural.maynoothuniversity.ie/id/eprint/8843/1/PM-Reanalysis-2007.pdf (a16, a17)
- [V] Gagne and Shoben (2002) Priming relations. https://link.springer.com/content/pdf/10.3758/BF03194965.pdf (a18)
- [V] Aerts and Sozzo (2014). https://arxiv.org/abs/1401.3626 (a19)
- [V] Aerts et al. (2016) Context and interference. https://arxiv.org/abs/1612.06038 and https://arxiv.org/pdf/1612.06038 (a21, b12)
- [V] Aerts et al. (2026) Quantum structure in AI language. https://arxiv.org/abs/2511.21731 (a28)
- [M] Costello and Keane (2000) C3. https://www.doi.org/10.1016/s0364-0213(00)00020-3 (a22, b23, c28)
- [M] Second-hand only, via the sources above: Gagne and Shoben (1997); Estes and Glucksberg (2000); Levin et al. (2019); Storms et al. (2005); Smith et al. (1988); Murphy (1988); Hampton (1987, Memory and Cognition 15); Wisniewski (1996a) (a06, a12, a14, b11, b24, c29)

**LLM and AI studies**
- [V] Li, Carlson and Potts (2022) GPT-3 systematicity. https://arxiv.org/abs/2210.09492 (a24, a25, c05, c06)
- [V] Coil and Shwartz (2023). https://arxiv.org/abs/2305.10568 (b17, b18, c01-c04)
- [V] Song et al. (2025) CCPT. https://arxiv.org/abs/2502.06086 (a26, a27, b13, b14)
- [V] Rambelli et al. (2024). https://aclanthology.org/2024.acl-long.637/ (c07-c09)
- [V] Ye, Tu and Pustejovsky (2025). https://aclanthology.org/2025.emnlp-main.1315.pdf (d10, d16)
- [V] Ross, Davidson and Kim (2024). https://arxiv.org/pdf/2410.17482 (b15, b16)
- [V] Rodriguez, Wang and Pylkkanen (2024). https://aclanthology.org/2024.lrec-main.472/ (c10)
- [V] Schapiro et al. (2025) KOMBINE. https://arxiv.org/abs/2509.21043 (c11-c14)
- [V] Wang et al. (2023) PopBlends. https://arxiv.org/abs/2111.04920 (c15, c16)
- [V] Ge and Parikh (2021). https://arxiv.org/abs/2106.14127 (c17, c18)
- [V] Kumar et al. (2024) Compun. https://arxiv.org/abs/2404.00419 (a29, b19, c23)
- [V] Kendrick et al. (2025). https://aclanthology.org/2025.cmcl-1.30.pdf (b20)
- [V] Vemuri, Shah and Varma (2024). https://arxiv.org/abs/2405.16128 (c19; single concepts only)
- [V] Suresh et al. (2023). https://arxiv.org/abs/2304.02754 (c20; abstract and introduction only)
- [V] Nagar et al. (2025). https://arxiv.org/abs/2506.00914 (c21)
- [V] Miletic et al. (2025). https://arxiv.org/abs/2505.14130 (c22)
- [V] Pan et al. (2025) food image generation. https://arxiv.org/abs/2512.09095 (c24)
- [V] Ali et al. (2026). https://arxiv.org/abs/2610.27894 (c25)
- [V] Shen, Druckmann and Zou (2026). https://arxiv.org/abs/2605.11258 (d01, d02)
- [V] Deng, Brucks and Toubia (2026). https://arxiv.org/abs/2602.20408 (d03)
- [V] Meincke, Mollick and Terwiesch (2024). https://arxiv.org/abs/2402.01727 (d04)
- [V] Wenger and Kenett (2025). https://arxiv.org/abs/2501.19361 (d05)
- [V] Jiang et al. (2026) Artificial Hivemind. https://arxiv.org/abs/2510.22954 (d06)
- [V] Moon et al. (2026). https://arxiv.org/abs/2609.30492 (d07)
- [V] Si, Yang and Hashimoto (2024). https://arxiv.org/abs/2409.04109 (d08; duplication result only)
- [M] Ciapparelli, Zarbo and Marelli (2025) Cognitive Science. https://doi.org/10.1111/cogs.70048 (d11)
- [M] Chen, Poeppel and Zuanazzi (2023). https://doi.org/10.31234/osf.io/gf2r9 (d12)
- [M] Absence checks via Crossref title search. https://api.crossref.org/works (d13, d14)
- [M] Wisniewski (1997) typeset mirror, unopened at first, later read in full from the Springer PDF as d09. https://typeset.io/pdf/when-concepts-combine-2uztzy42jq.pdf (a23, b22)
