# Language as a tool for relations: deep document

Scope: Gentner's claim that relational words and labels help people compare cases and see shared structure, and Lupyan's claim that words feed back into processing. Applied to our agent at schema state S2 (REPRESENT: name the relation). Evidence ids (a01-d16) point to evidence_a-d.jsonl in this folder. Claim ids (A15.08-K01 to K29) point to claims.jsonl. Where a figure is second-hand it says so.

Bottom line: the human evidence that naming a relation raises relational retrieval and transfer is real but thin (one lab, a few studies, modest odds ratios). No study found tests the effect directly on an LLM. The nearest LLM results (naming attributes, stating the relation in the prompt) are positive on average but model-dependent. So naming relations is a "test first" item, not an "add now" item. What is established is the problem it targets: unaided retrieval and analogy favour surface similarity, in people and in LLMs.

## 1. What it is

The idea is that relational words are cognitive tools. A relation (inoculation, brace, same, above) is hard to see because relations are encoded in different ways in different situations, while objects are encoded the same way every time. A relation name invites one uniform reading of a case, so two cases that share the name become easier to align and later to retrieve.

Three linked claims:
1. Retrieval claim (Jamrozik & Gentner 2020). A relational label at encoding or at retrieval raises cross-domain relational reminding (a01-a05).
2. Learning claim (Gentner and colleagues). Giving two cases a shared relational or contrastive label, especially with comparison, raises transfer in children (a16, a17, b03-b05).
3. Processing claim (Lupyan). An active word feeds back and changes ongoing processing (label-feedback hypothesis, a08-a12). The effect is online and transient.

What this subfield is not: whether language shapes colour or space perception in general (Whorf), or whether LLMs have language-based thought (Mahowald 2024, b25, not opened). It is the narrow tool claim: does putting a name on a relation help the next comparison?

Our agent's link: S2 is where the agent restates the problem in its own terms. The question is whether adding an explicit relation name (and a one-line definition) there improves later case retrieval (O7 map an analogue, memory lessons) and transfer.

## 2. History and theories in depth

Structure-mapping line (Gentner).
- Structure-mapping theory: analogy aligns relational structure and ignores surface. Novices are pulled by surface matches. This is the base for SCHEMA O7.
- Early developmental work (all second-hand): Rattermann & Gentner 1998: labelling objects "daddy, mommy, baby" raised 3-year-olds' relational matches from 32% to 79% (a15). Gentner & Namy 1999: a shared novel label on two standards made 4-year-olds favour the taxonomic match (b03). Loewenstein & Gentner 2001: comparing two near-identical rooms, with no new word, raised twin-object correct choices above 70% vs 42% control (a18, b05). Loewenstein & Gentner 2005: spatial words (top, middle, bottom) improved preschoolers' mapping in a three-tier box and the benefit lasted 2 days (b04, b06). Dessalegn & Landau 2008: 57% correct without relational language vs 79% with "red is on the left" (b03). Christie & Gentner 2014: even nonsense names for relations helped children (c22).
- Mutability: relational terms (verbs) change meaning with context more than entity terms (nouns) do (Gentner & France 1988, a07). Content also bends relations: addition problems were 82% accurate for symmetric pairs (tulips-daffodils) and 61% for asymmetric pairs (tulips-vases) (Bassok et al. 1998, a06). This is the reason a relation name can help: it fixes one construal.
- Gentner 2016 "Language as cognitive tool kit": the moderate Whorfian summary by the main proponent (b09, abstract only).
- Adult retrieval (Jamrozik & Gentner 2020): the main adult test. Details in section 3.
- Zheng, Goldwater & Gentner 2025: the cleanest recent design, 2 (alignment) x 2 (label) with children.

Lupyan line.
- Label-feedback hypothesis (Lupyan 2012, a08): words are not a separate channel. An active word feeds back to perceptual and conceptual layers. Evidence: redundant nonsense labels sped category learning (Lupyan, Rakison & McClelland 2007, a09); the word "five" sped search for 5s but only if heard within 1600 ms (Lupyan & Spivey 2010, a10); telling people shapes were rotated 2s and 5s sped search (2008, a11); a valid label before a flash-suppressed picture boosted detection (Lupyan & Ward 2013, b14).
- Nameability: easy-to-name features speed rule-based category learning (Zettersten et al. 2024, a20).
- Representational alignment: redundant labels made people's later sorts more alike (Mind Melds 2024, b11, b12, d09).
- 2026 positions: Lupyan, Gentry & Zettersten (abstract only, d11): language supplies compact, culturally accumulated abstractions to any learner. Liu & Lupyan (partly read, d10): four mechanisms for cross-domain mapping (statistical learning, magnitude matching, valence matching, semantic mediation); whether language drives or reflects mappings is unresolved.

Competing accounts of why labels help (a05): (a) uniform relational construal (Gentner); (b) local salience of the named relation; (c) plain lexical cue, a word match between encoding and test; (d) self-generated labels. The domain-label null (a04) weakens (b) and (c) only partly. Comparison alone, with no label, also helps (b05), so labels are one route among several.

Infant counterpoint: Anderson, Chang, Hespos & Gentner 2022 found no benefit of "same/different" labels for 12-month-olds (a13, a14), while Gerson & Woodward 2014 reported label help for action goals (a21, not opened). Contested.

## 3. Core findings with exact numbers

Status: single = one lab or one study; contested = studies disagree; second-hand = figure taken from a later paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Without labels, adults retrieve same-domain cases far more than relational ones | Exp 1 N=251 (36 per condition, 7 conditions). Domain 4.58 vs relational 1.56 of 10 | Jamrozik & Gentner 2020 (a02) | single study, 2 experiments |
| Relational label at encoding and/or test raises relational retrieval | Relational matches of 10: baseline 1.56; encoding label before 3.19, after 3.40; test label before 2.51, after 1.97 (n.s., p=.188); both before 5.67, both after 6.78 | same (a03) | single |
| Domain labels do not help | Exp 2 N=114 (17 per condition). Relational baseline 2.44; relational label 4.21-4.53 (about 1.8x). Domain-label Bayes factors 0.389 (domain matches) and 0.301 (relational matches), intercept-only preferred | same (a04) | single |
| Domain matches fall with relational labels | 4.58 down to 2.53 and 2.80 (encoding labels), about 2.25 and 1.89 (test labels) | same (a03) | single |
| Shared contrastive label raises transfer in 5-7 year olds | Exp 1 N=64 (16 per cell). Transfer language b=2.278, p=.001, OR 3.15 [1.63, 6.88]; alignment b=1.938, p=.005, OR 2.66. Repair: alignment OR 2.31 (p=.003); language p=.58 | Zheng et al. 2025 (a16, b01) | single (one concept: brace) |
| Label effect persists and reaches far transfer | Exp 2 N=116 (29 per cell). Label ORs: Day-1 repair 1.55 (p=.032), Day-2 repair 1.76 (p=.012), near transfer 2.57 (p=.001), far construction 1.60 (p=.027), far recognition 1.75 (p=.007). Alignment far construction OR 1.36, p=.15 | same (a17, b02) | single |
| Alignment and label add up | no alignment x language interaction in Exp 1; Exp 2 interactions inconsistent | same | single |
| Comparison alone helps without a new word | Twin-object trials over 70% vs 42% control (3.5-year-olds) | Loewenstein & Gentner 2001, via Zheng (a18, b05) | second-hand |
| Relational words raise preschool mapping | Dessalegn & Landau 57% vs 79%; Rattermann & Gentner 32% vs 79% | via Zheng 2025 and Anderson 2022 (a15, b03) | second-hand |
| 12-month-olds do not benefit from "same/different" | N=64; relational-label trials F(1,60)<1, p=.354; 34 of 64 looked longer at novel. Versus Ferry 2015 no-label infants: 18.31 vs 13.21 s, F(1,121)=5.05, p=.026. (16.60 vs 16.05 s is the pair-habituation phase; relational-label test trials were 20.32 vs 17.02 s, n.s.) | Anderson et al. 2022 (a13) | failed extension |
| Object labels did not help infants either | N=48; F(1,43)<1, p=.75; pair habituation F(1,43)=3.89, p=.055; interaction F=7.59, p=.009 | same (a14) | failed extension |
| Easy-to-name features speed rule learning | Adults 95.8% vs 87.3%, d=1.06, p<.001 (N=90). Children 71.0% vs 65.9%, p=.118 (N=97, ages 4-6); condition x block p=.010; last block of round 1 74.2% vs 63.3%, d=0.57. No effect at generalisation (adults p=.91, children p=.33) | Zettersten et al. 2024 (a20) | single; not re-checked later (page error) |
| Redundant labels speed novel category learning | Lupyan, Rakison & McClelland 2007 (no N in review); an online adult replication failed | a09, b10 | contested; replication abstract only |
| Redundant labels increase between-person alignment | Exp 1 N=129 (45/43/41 after 39 exclusions): alignment .20 vs .11 and .12 (p<.001); categoricality .65 vs .38 (p=.024) and .40 (p=.038). Exp 2 N=122 (41/37/44, 65 excluded): alignment .35 vs .21 and .27; categoricality .66 vs .49 (p=.04), vs no labels .60 (n.s.) | Mind Melds 2024 (b11, b12, d09) | single; categoricality only partly replicated |
| Label effect is time-limited | gone when the word came over 1600 ms before display | Lupyan & Spivey 2010 (a10) | single, described in a review |
| Labels boost unseen objects into awareness | valid label improved d' and RT (2013); a preregistered EEG study N=20 found no boost and no change in Visual Awareness Negativity (2026) | b14, b15 | contested; low-power null |
| GPT-3 matches students with no labels | Digit matrices (N=40): generation OR 1.88, p=.005; multiple choice OR 6.27. Letter strings (N=57): OR 1.76, p=6.3e-5. Story analogies (N=54): near p=.0039, far p=.065; humans better, GPT-3 OR 0.37, p=.0003 | Webb et al. 2023 (a22, a23, b17) | not robust (next row) |
| That competence is brittle | Digit matrices, blank moved: humans 0.715 to 0.771; GPT-3.5 0.813 to 0.480; GPT-4 0.810 to 0.477. Symbol swap: no drop (GPT about 0.79). Permuted letter alphabets: GPT-3, 3.5, 4 fall at each step, humans flat | Lewis & Mitchell 2024 (a24, b18, c07, c08) | two tasks, one lab |
| Naming entity attributes lets a text LM solve visual matrices | GPT-3 175B Center 77.2% (ordinal names) vs 51.8% (random words) vs 28.2% (ASCII quasi-image). Decomposition: OPT 125M 22.2 to 45.6%; OPT 1.3B 47.2 to 72.0%; 3x3Grid 86.4 to 93.2% | Hu et al. 2023 (c01-c04) | single; authors' own naming |
| Distractor attribute barely hurts named prompts | Center 76.0% and 80.0% (RAVEN orientation values), 72.6% and 77.8% (random values) | same (c03) | single |
| Stating the shared relation in the prompt | EMA accuracy zero-shot to targeted-knowledge prompt: GPT-3.5-Turbo 45.70 to 55.25; FlanT5 36.47 to 44.26; Falcon 24.17 to 25.40; Mistral 26.59 to 27.37; Zephyr 29.46 to 15.83; 6 of 9 models up. Extra relevant text without the relation: GPT-3.5 about 38.3-38.8 | KnowledgePrompts 2024 (d02) | single; name bundled with reasoning text |
| Telling the model to weigh relations over shared entities | Story-analogy identification: FlanT5-xxl 41.2 to 48.0; GPT-3.5 33.7 to 44.0; little change for LLaMa, ChatGPT | StoryAnalogy 2023 (d06) | single |
| Object structure helps ARC, edges hurt | GPT-4 13/50 to 23/50 (object JSON); 81 to 97 of 400; object JSON + edge 19 (few-shot) / 16 (CoT) vs 21 / 23 without edges; reasoning correct in 20 of 23 object solves vs 3 of 13 grid solves | Xu et al. 2023 (d04, d16) | single |
| Far analogies with surface distractors | ARN accuracy (near/far, near/near, far/far, far/near): GPT-4 94.0/92.5/57.1/29.1, GPT-3.5 88.1/81.3/50.4/21.7, human 98.6/97.2/96.8/91.4. Random is 50% | Sourati et al. 2024 (c18) | agrees with AnaloBench, Stevenson |
| Long-story analogy gap | AnaloBench T1 at 1/10/30 sentences: GPT-4 89.1/66.5/60.7; GPT-3.5 65.3/46.4/30.8; Claude 68.2/30.2/25.9; human 96.0/72.5/73.3. Retrieval from about 200 stories near random | Ye et al. 2024 (d05) | single benchmark |
| Models solve children's verbal analogies by association | 622 items, 14,006 children aged 7-12. Controlling for association drops each model 1-2 age years | Stevenson et al. 2023 (c13) | single |
| ConceptARC relational concepts | Human vs GPT-4: Above/Below .90 vs .23; Same/Different .93 vs .20; Inside/Outside .83 vs .27; Count .86 vs .03; Order .95 vs .23 | Moskvichev et al. 2023 (b21) | single |
| 2025 reasoning models close the accuracy gap, not the rule gap | o3 text 77.1%, Gemini 2.5 Pro 66.0, Claude Sonnet 4 60.2 (72.5 after re-assessment), humans 73%. About 27% of o3 and Gemini correct outputs rest on unintended or incorrect rules; Claude about 19% | Beger et al. 2025 (d08) | single |
| Mechanism: relation info in mid-upper layers | Patching fixes up to 38.4% of failures (Gemma-7B; Qwen2.5-14B 35.6%; Llama-2-13B 32.3%). Probe about 82.9% | Lee et al. 2025 (b19, d01) | single |
| Function-vector injection lifts far analogies | GPT-J far 42.5 to 61.0; LLaMa-3.1 far 57.5 to 74.0; LLaMa-3.1 near 87.5 to 85.0 | arXiv 2601.08169 (d03) | single; activation level |
| Self-generated analogues before solving | GSM8K GPT-3.5: 5-shot CoT 75.0% vs 75.8-77.8%; MATH 33.0 vs 33.9-37.3; text-davinci-003 14.8 vs 50.3-61.0; BIG-Bench 0-shot word sorting 66.8 to 75.2, logical deduction 30.0 to 41.6 | Yasunaga et al. 2024 (c10, a25, b20) | single; not relation naming |

## 4. Mechanisms and models

Each mechanism is written so it can be turned into code or a prompt.

M1. Uniform construal at encoding (Gentner).
- Problem: a case is stored as objects, domain, and loosely encoded relations. A later query shares the domain or objects, not the relation, so retrieval returns same-domain cases (4.58 vs 1.56 of 10).
- Mechanism: attach a relation name (one noun phrase, such as "inoculation", "single point of failure", "diagonal brace") to the stored case and to the query. Matching on the name pulls relational matches.
- Implementation: each memory record has fields {domain_tag, relation_name, relation_definition (1 line), case_text}. At query time the agent writes a relation_name for the current problem; retrieval ranks by name match first, text similarity second. Code does the ranking (G5).
- Cost: one short model call per case at write time and per query at read time. Both-phase labelling gave the largest effect (5.67-6.78 vs 1.56), but part may be a plain word match (a03 limits). For an agent a word match is acceptable; it is the point.

M2. Compare, then name (Zheng 2025).
- Alignable pair of cases, then a shared contrastive label. Alignment and label add independently in Exp 1 (OR 2.66 and 3.15). The label helped transfer, not the immediate task.
- Implementation: with two solved cases in context, have the agent list the aligned parts, give both the same name, then state the rule under that name. Compare with compare-only and name-only.

M3. Placement and timing (Jamrozik; Lupyan & Spivey).
- A test label placed after the passage did not help (1.97, p=.188); before it did (2.51). Feedback effects fade after about 1600 ms.
- Implementation: put the relation name before the case text, and repeat it next to the question. Do not append it at the end of a long context.

M4. Specificity of label type.
- Domain labels give no gain (BF 0.30-0.39). The gain is for a relational label. Control arms must use a domain tag of equal length.

M5. Label as attribute abstraction (Hu 2023).
- Convert raw input into named attributes with an ordered vocabulary. Ordinal names beat random words by over 20 points at larger sizes. Names that carry order or structure do the work.
- Implementation: for grid or table tasks, extract objects with code, give each attribute a consistent short name, decompose per attribute. Code-extracted objects raised GPT-4 on ARC (13/50 to 23/50) but edge lists lowered it, so add only the few relations that matter.

M6. Relation stated in the prompt (KnowledgePrompts; StoryAnalogy).
- Prompt carries "the shared relation is X; X means Y". Gains in 6 of 9 models, a large loss in one (Zephyr -13.63). The sign depends on the model, so it needs a per-model gate.

M7. Label feedback as a model of why.
- A word, once active, biases features toward the category. A transformer has no online feedback loop from word to perception. The reading that carries over is that a name in context shifts attention and next-token distributions toward the named relation. This is an analogy, not evidence. Relation function vectors (d03) are the activation-level version: far analogies +16.5 to +18.5 points, near ones -2.5 to -3.

M8. Shared vocabulary for agreement (Mind Melds).
- A shared label set raises agreement between people's sorts (.20 vs .11). For an agent, a fixed relation vocabulary could raise agreement between samples. Under G4 agreement is a hint, not proof, and it may reduce diversity (untested).

M9. Why naming may fail.
- The model must already hold the relation. Lee 2025: failures are missing information or non-application; naming fixes only the first. 12-month-olds without a usable concept got nothing (a13). Self-generated names can be wrong (about 27% of correct o3 outputs rest on wrong rules, d08).

## 5. What holds up

Holds up:
- Unaided retrieval and analogy favour surface. Human: 4.58 vs 1.56 of 10. LLM: ARN far/near 29.1% (GPT-4), AnaloBench retrieval near random, Stevenson association results. Four sources.
- Comparison of alignable cases helps without any word (b05, a16, a18). Labels add to it (a16).
- Zero-shot LLM analogy skill is brittle under surface change (Lewis & Mitchell, two tasks).
- Naming and structuring objects helps LLMs on matrix tasks (Hu, Xu), when the names carry structure.

Does not hold, or contested:
- Lupyan 2007 redundant-label advantage: online adult replication failed (b10, abstract only, N unknown).
- Lupyan & Ward 2013 unseen-object boost: 2026 EEG null, N=20 (low power).
- Infants: no label benefit for same/different (N=64) or object labels (N=48). Gerson & Woodward 2014 disagree for action goals (not opened).
- Children and nameability: adults strong (d=1.06), children n.s. overall (p=.118).
- Mind Melds Exp 2: categoricality weaker, n.s. vs no labels; heavy exclusions.
- Webb 2023 human-level analogy: broke on counterfactual variants.
- No further replication of Jamrozik 2020 found (search was constrained).

Moderators.
- Label type: relational, not domain (a04).
- Position: before the item (a03).
- Timing: transient (a10).
- Learner knowledge: the label needs a usable relation concept (a13). A review says a relational mindset must be induced before encoding (b22, Goldwater & Jamrozik 2019).
- Measure: the label helped later transfer, not immediate repair (a16).
- Model: the sign of a prompt-level relation statement varies by model (Zephyr -13.63).

Worked (human): relational label at both phases; shared contrastive label after aligned comparison; relational spatial words for preschoolers.
Worked (LLM, indirect): named ordinal attributes; object JSON; relation stated in the prompt for 6 of 9 models; relation-over-entity instruction for 2 of 4; self-generated analogues (small gain on GSM8K, large on weak models); relation vector injection (activation level).
Did not work: domain labels; edge lists on ARC (19/16 vs 21/23); extra relevant text without the relation (GPT-3.5 38.3-38.8 vs 45.70 baseline); label-prompt steering alone (18% vs 75%, d03); random or semantic structured-knowledge prompts (GPT-3.5 38.29 for random, below zero-shot 45.70).

Confounds: label vs comparison vs salience in most developmental studies; all Jamrozik items are one stimulus set (10 relational patterns).

## 6. Language models

Direct tests: none found of Gentner's relational-label effect or Lupyan's label feedback on LLMs (c24, d13). The search was rate limited, so this is unproven absence.

Nearest evidence, in order of closeness:
1. Hu et al. 2023 (c01-c04). Naming attributes in text. GPT-3 175B 77.2% with ordinal names, 51.8% random-word names, 28.2% ASCII image. Decomposition doubled OPT-125M (22.2 to 45.6). Zero-shot, authors' own mapping, RAVEN only.
2. KnowledgePrompts (d02). 15K analogies, 236 relation types. Stating the relation: GPT-3.5 +9.55, FlanT5 +7.79, Falcon +1.23, Mistral +0.78, CodeT5 +1.00, Zephyr -13.63, GPT2 -1.01, Orca -0.34. Not isolated from the reasoning text.
3. StoryAnalogy template (d06). FlanT5-xxl +6.8, GPT-3.5 +10.3; little for LLaMa and ChatGPT. Older models.
4. Xu 2023 (d04). Object structure: GPT-4 13 to 23 of 50; edges hurt.
5. Yasunaga 2024 (c10). Self-recall of analogues. GPT-3.5 on GSM8K 75.0 to 75.8-77.8; text-davinci-003 14.8 to 50.3-61.0. The code variant asks the model to name core concepts first, with no ablation of that step (c11).
6. Thought Propagation (c12). +12% shortest path, +15% agent planning; abstract only.
7. Guo 2024 (d12). A written description of entities and implicit relation helped smaller models modestly (FLAVA 26.4 to 33.3 Hits@1); a fine-tuned predictor reached 56.20 vs 43.39 for base LLaVA.

Behaviour on the target problems.
- Near analogies fine, far poor: ARN GPT-4 94.0 vs 29.1 on the hardest cell.
- Lean on association (Stevenson 2023).
- Order bias: GPT-4 89% (16/18) when Story A correct, 61% (11/18) when B (c09).
- ConceptARC in 2023: Count .03, Same/Different .20 for GPT-4. By 2025 o3 hits 77.1% on text, but about 27% of its correct answers use wrong rules (d08). Grade the stated relation, not just the answer.
- Models state permuted-alphabet rules at near 1.0 (GPT-4 1.0/1.0/1.0) yet fail the analogy, so the failure is application, not knowledge (d07). A pure naming scaffold may not fix this.
- Mechanism: relation in mid-upper layers; patching recovers 30-38% of failures in 7-14B open models (d01). A prompt route is untested.
- Newer GPT-4 snapshots did not beat 0613 on digit matrices. No relation-name arm on any reasoning model.
- Content effects: models, like people, reason better when meaning supports logic (c20).

Size of what changed results: object structure +10/50 on an ARC subset; ordinal vs random names +20 points; relation statement from +9.55 to -13.63; relation-over-surface instruction +6.8 / +10.3; function vector on far analogies +16.5 / +18.5; decomposition up to +20 points on multi-component tasks for small models.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. Do not rely on unaided similarity retrieval for analogues. Treat same-domain or surface matches as the default failure; at O7 require a typed mapping checked by code. Part O7/G, [E]. Evidence: a02, c18, d05, c13 (K19). This confirms the existing O7 note and adds nothing new to the schema.
2. Keep far analogues for impasses and open mode, not routine problems. Already in SCHEMA O7. [E]. Evidence: K19.
3. Do not treat a correct answer as proof of a correct relation; check the stated rule where the class has a checker. Part G3/S8, [E]. Evidence: d08, d16, c07. Overlaps G3 and G10.
4. When testing any analogy scaffold, perturb the surface form, since zero-shot competence collapses under perturbation. Part G3/bench, [E]. Evidence: b18, c08 (K15).

Nothing about relation labels for LLMs is established. All label items are under Test first.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Relation name field on memory records and queries, name before case | S2, memory, O7 | [S] human only | a02, a03, a04 (K01) |
| T2 | Relation name vs same-length domain tag vs none | S2 | [S] | a04, a05 (K02) |
| T3 | Name placed before the case vs after | S2 | [E] for people (a03, a10), untested on LLMs | K03 |
| T4 | Compare-then-name at O7 (aligned pair, shared name, rule under the name) | O7, O3 | [S] children | a16, a17 (K04, K05) |
| T5 | One-line relation statement in the analogy step, gated per model | S2 | [S], sign varies | d02, d06 (K23, K24) |
| T6 | Short consistent feature names vs opaque names; object extraction by code on grid tasks, with few or no relation edges | S2, O6 | [S] | a20, c01, d04 (K08, K16, K25) |
| T7 | One-line definition per relation name, checked on content-conflict items | S2, G | [S] second-hand | a06 (K13) |
| T8 | Recall-then-solve vs fixed examples | O3, memory | [S] | c10 (K17) |
| T9 | Fixed relation vocabulary across samples to raise agreement | S2, G4 | [S] | b11, d09 (K10) |
| T10 | Self-generated name vs supplied name vs wrong name | S2 | untested | a05 |

Rule: nothing in Test first goes into SCHEMA.md until it wins at equal tokens (G7).

## 8. Concrete tests on our bench

All arms get the same total token budget; name-writing calls count. Use at least three model sizes, since the sign varies by model. Report paired bootstrap intervals.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 retrieval by name (T1, T2) | Library of 100+ solved problems over at least 10 relational patterns, each with a same-domain decoy and a cross-domain relational match (Jamrozik design in text) | (a) plain text retrieval; (b) relation name at store and query; (c) same-length domain tag at both; (d) name at store only; (e) name at query only | Share of top-1 that is the relational match; same-domain share | (b) at least 2x (a) in relational share if the human effect carries (human 1.56 to 5.67); (c) equals (a) |
| B2 placement (T3) | Same items as B1, solving with a retrieved case | name before case; name after case; before and repeated next to the question | Solve accuracy | before beats after by a few points; repeat adds little |
| B3 compare-then-name (T4) | Rule learned from two examples, then near and far transfer items (CS or engineering rules, ConceptARC groups) | aligned vs unaligned pair x shared name vs no name (2x2) | Near and far transfer accuracy; immediate-task accuracy | alignment and name each add; name helps transfer more than the immediate task |
| B4 relation statement (T5) | 300+ proportional or story analogies, at least 3 relation types, near and far | zero-shot; relation name + 1-line definition; equal-length neutral relevant text; relation-over-surface instruction | Accuracy by model | positive for most models, negative for some; neutral text no gain |
| B5 naming quality (T6) | RAVEN-text and ConceptARC text | ordinal names; random-word names; opaque symbols | Accuracy | ordinal beats random by 10+ points |
| B6 edges (T6) | ARC subset, 50+ tasks | object JSON; JSON + selected relation edges; JSON + all edges | Solves | all edges below objects only |
| B7 perturbation (K15) | Letter-string and digit-matrix with permuted alphabet or moved blank | plain; rule statement given; relation name given | Accuracy on perturbed vs original | statement narrows the gap only if failure is missing information |
| B8 recall-then-solve (T8) | GSM8K or MATH slices of mid difficulty | fixed exemplars; self-recall; self-recall with core-concept naming step | Accuracy; tokens | self-recall +1 to 3 points on mid models; the naming-step ablation is new |
| B9 agreement (T9) | Open-answer class | free relation names vs fixed vocabulary, 8 samples each | Pairwise agreement; number of distinct answers | agreement up; diversity must not fall |
| B10 who names (T10) | Same as B1 | model writes own name; gold name supplied; wrong name supplied | Retrieval share; accuracy | gold > self > none; wrong name at or below none |

## 9. What does not transfer, and why

- Infant label results (a13, a14, a21): the learner has no relation vocabulary. Our model has a large one.
- Perception effects (Lupyan & Ward, Lupyan & Spivey): millisecond timing, visual awareness. A text agent has neither. Contested anyway (b15).
- Nameability of colours (a20): rests on human vocabulary and familiarity. The analogue (short, consistent feature names) is weak.
- Label feedback as a literal loop: a transformer has no online feedback from a word to perception. Only the context-bias reading carries over, as an analogy.
- "Redundant" labels (Lupyan 2007, Mind Melds): the point there is that the label adds no information. A name in a prompt can add information, so effects are not comparable.
- Human memory with a 15-minute filler: agent memory is a lookup, not decay. Whether an embedding retriever shows the same surface bias is inference (AnaloBench retrieval near random hints that it does).
- Activation-level methods (patching, function vectors; d01, d03): need model internals. A prompting-only agent cannot use them; they only suggest what a good name should encode.
- Self-generated analogues (Yasunaga): case recall, not naming.
- Children's single-concept studies (brace): one domain, US children, modest odds ratios.
- Most models in the literature are 2023-era; reasoning models appear only in ConceptARC (d08).

## 10. Open questions

1. Does adding a relation name (vs domain tag vs none) to a retrieved or in-context case raise relational transfer for an LLM at equal tokens? No direct study.
2. Does position matter for LLMs, and does the effect vanish when the model must generate the name itself?
3. Does compare-then-name beat compare-only or name-only?
4. Which analogy failures are missing relation information (fixable by naming) vs failure to apply it? Lee 2025 gives no split. Is the 30-38% patching gain reachable by prompt?
5. Does naming quality (ordinal vs random) generalise from RAVEN to text relations and ConceptARC?
6. Do names narrow the far-analogy gap (ARN 29.1%) for 2025-2026 models?
7. Do label gains survive permuted alphabets and moved blanks? Explicit rule statements are the candidate (d07: models state the rule at near 1.0 yet fail).
8. Does a shared label vocabulary raise sample agreement, and does it cost diversity?
9. Is Jamrozik 2020 replicated outside its lab? Was the failed Lupyan 2007 replication adequately powered (sample size unread)?
10. Does the Zheng 2025 label effect hold beyond one engineering concept?
11. Does an embedding retriever show the human surface bias, and does a name field fix it?
12. Does a wrong name hurt more than no name?

## 11. Sources

[V] opened and read this session (full text or substantive part). [M] snippet, abstract or listing only.

- [V] Jamrozik & Gentner (2020) Relational labeling unlocks inert knowledge. Cognition 196:104146. https://groups.psych.northwestern.edu/gentner/papers/JamrozikGentner_2020-RELM.pdf (a01-a05)
- [M] Jamrozik & Gentner 2020, abstract. https://doi.org/10.1016/j.cognition.2019.104146 (b07)
- [V] Lupyan (2012) Label-feedback hypothesis. Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2012.00054/pdf (a08-a12)
- [V] Anderson, Chang, Hespos & Gentner (2022) No evidence for language benefits in infant relational learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC8943688/ (a13, a14)
- [V] Zheng, Goldwater & Gentner (2025) Structural alignment and linguistic contrast help children learn. https://pmc.ncbi.nlm.nih.gov/articles/PMC12741211/ (a16-a19, b01-b05)
- [V] Zettersten et al. (2024) Nameability supports rule-based category learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC10922161/ (a20; a later re-fetch returned an error stub)
- [V] Mind Melds: verbal labels induce greater representational alignment (Open Mind 2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11338297/ (b11, b12, d09, b26)
- [V] Categorization in infancy: labeling induces a persisting focus on commonalities. https://pmc.ncbi.nlm.nih.gov/articles/PMC4995729/ (b13, abstract and introduction)
- [V] Relational reasoning and educational applications (2026 review). https://pmc.ncbi.nlm.nih.gov/articles/PMC12938770/ (b22)
- [V] Liu & Lupyan (2026) The unity of sense and mind. https://pmc.ncbi.nlm.nih.gov/articles/PMC12769545/ (d10, part of the text)
- [V] Webb, Holyoak & Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196 (a22, a23, b17, c05, c06, c25)
- [V] Lewis & Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955 (a24, b18, c07)
- [V] Lewis & Mitchell (2024) Digit matrices and story analogies. https://arxiv.org/abs/2411.14215 (c08, c09, d07)
- [V] Hu, Storks, Lewis & Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626 (c01-c04)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (a25, b20, c10, c11)
- [V] Yu, He & Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (c12, abstract numbers only)
- [V] Stevenson et al. (2023) Do LLMs solve verbal analogies like children do? https://arxiv.org/abs/2310.20384 (c13)
- [V] Ushio et al. (2021) BERT is to NLP what AlexNet is to CV. https://arxiv.org/abs/2105.04949 (c14)
- [V] Musker et al. (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (c15)
- [V] Lee et al. (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344 and https://arxiv.org/html/2511.20344 (b19, c16, d01)
- [V] Sourati et al. (2024) ARN: Analogical Reasoning on Narratives. https://arxiv.org/abs/2310.00996 (c18, c19)
- [V] Moskvichev, Odouard & Mitchell (2023) ConceptARC. https://arxiv.org/abs/2305.07141 (b21; a26 title page only)
- [V] Beger et al. (2025) Distinguishing performance from understanding on ConceptARC. https://arxiv.org/html/2510.02125 (d08)
- [V] Lampinen et al. (2024) Content effects on reasoning. https://arxiv.org/abs/2207.07051 (c20, abstract and text claims)
- [V] Gendron et al. (2024) LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 (c21, limited)
- [V] KnowledgePrompts, arXiv 2412.00869. https://arxiv.org/html/2412.00869v2 (d02, d13)
- [V] Relational knowledge distillation with fine-tuned function vectors, arXiv 2601.08169. https://arxiv.org/html/2601.08169v1 (d03)
- [V] Xu et al. (2023) LLMs and the ARC. https://arxiv.org/html/2305.18354 (d04, d16)
- [V] Ye et al. (2024) AnaloBench. https://arxiv.org/html/2402.12370 (d05)
- [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/html/2310.12874 (d06)
- [V] Guo et al. (2024) Can multimodal LLMs think analogically? https://arxiv.org/html/2411.01307v1 (d12)
- [V] Liu, Marjieh, Zhu, Goldberg & Griffiths (2026) Parallelogram theory of analogy. https://arxiv.org/abs/2603.19066 (c17, d15; abstract and introduction only)
- [M] Gerson & Woodward (2014) Labels facilitate infants' comparison of action goals. https://pmc.ncbi.nlm.nih.gov/articles/PMC4072221/ (a21)
- [M] Zettersten & Lupyan (2020); Lupyan & Zettersten (2020). https://europepmc.org/search?query=Zettersten%20Lupyan (a27)
- [M] Lupyan, Gentry & Zettersten (2026) How important is language for human-like intelligence? https://doi.org/10.1177/17456916251398539 (a28, d11)
- [M] Loewenstein & Gentner (2005) Relational language and relational mapping. https://doi.org/10.1016/j.cogpsych.2004.09.004 (b06)
- [M] Structure mapping and relational language support children's learning of relational categories. https://doi.org/10.1111/j.1467-8624.2011.01599.x (b08)
- [M] Gentner (2016) Language as cognitive tool kit. https://doi.org/10.1037/amp0000082 (b09)
- [M] Redundant-label replication of Lupyan, Rakison & McClelland 2007. https://doi.org/10.31234/osf.io/5e8mz_v2 (b10)
- [M] Lupyan & Ward (2013). https://doi.org/10.1073/pnas.1303312110 (b14)
- [M] Linguistic cues do not influence subliminal visual processing (Cortex 2026). https://doi.org/10.1016/j.cortex.2026.03.010 (b15)
- [M] The role of language in forming the concepts same and different (Cognition 2026). https://doi.org/10.1016/j.cognition.2026.106568 (b16)
- [M] Semantic anchors facilitate task encoding in continual learning (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12483573/ (b23)
- [M] Verbal recoding underlies visual ambiguity resolution (2026). https://doi.org/10.1037/xge0001979 (b24)
- [M] Mahowald et al. (2024) Dissociating language and thought in LLMs. https://pmc.ncbi.nlm.nih.gov/articles/PMC11416727/ (b25)
- [M] INLG 2025 (2025.inlg-main.28) analogical reasoning fragile. https://preview.aclanthology.org/ingest-luhme/2025.inlg-main.28.pdf (d14)
- [M] Second-hand via other papers, originals not opened: Rattermann & Gentner 1998; Christie & Gentner 2014; Hoyos et al. 2016; Bassok, Chase & Martin 1998; Gentner & France 1988; Gentner & Namy 1999; Namy & Gentner 2002; Dessalegn & Landau 2008; Loewenstein & Gentner 2001; Lupyan, Rakison & McClelland 2007; Lupyan & Spivey 2008, 2010; Gentner et al. 2013 (a06, a07, a09-a11, a15, a18, c22, c23).

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 2 established claims: 1 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A15.08-K03** (reworded: the sources support less). In Jamrozik and Gentner, label position mattered only for labels at test (after the passage n.s., p=.188); at encoding before vs after did not differ (3.19 vs 3.40 relational matches), and the 1600 ms decay comes from a perceptual 'five' search task (Lupyan and Spivey), not relational labelling. Corrected claim: In Jamrozik and Gentner (2020), test labels helped only when placed before the test passage (labels after the passage did not, p=.188), while at encoding the position (before or after) made no clear difference. In a separate perceptual search task (Lupyan and Spivey 2010), a spoken label's benefit disappeared when it preceded the display by more than about 1600 ms.
- **A15.08-K05** (now single-source: only one opened source, code check).
- **A15.08-K14** (now single-source: only one opened source, code check).
- **A15.08-K15** (now single-source: only one opened source, code check).
