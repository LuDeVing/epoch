# Relational reasoning gap: deep document

*Subfield A18.11 of comparative cognition. Written 2026-11-03 from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b07, d04 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The relational reasoning gap is the claim that humans reason about relations between relations, and non-human animals mostly do not, or only with heavy training. The founding statement is Penn, Holyoak and Povinelli (2008, Behavioral and Brain Sciences): only humans approximate a physical symbol system, with higher-order, systematic, relational reasoning (a01, a02, d12).

The standard test is relational match-to-sample (RMTS). The animal sees a sample pair, for example two identical icons (relation "same"). It must pick, from two test pairs, the pair that shows the same relation. One test pair is "same" and one is "different". No icon is shared between sample and choices, so the match must be on the relation, not on the objects. The older, simpler test is same/different (S/D) with arrays of icons.

Why this matters for our agent:
- Our agent is a language model. Plain LLMs show relational ability on familiar analogy items, but it breaks when the surface form changes (section 6).
- The gap literature says what a system needs: separate the roles from the fillers, keep working memory free for the relation, and use external symbols as labels. These map to operator O7 (map an analogue), to S2 (represent) and to guardrail G3 (pass on something the answer was not fitted to).
- Status for the schema: this is background for O7 (SUBFIELDS.md row, priority Med). Most animal results do not transfer. The LLM results do.

Scope notes. Parallel subfields cover analogical problem solving, incremental mapping, connectionist mapping models, fluid reasoning, and chain-of-thought. This document only links to them. It covers the animal gap, the human load result, the relational-bottleneck models, and every LLM or AI test of the same construct that was found.

## 2. History and theories in depth

### 2.1 The animal tradition (1980s to 2010s)

- Premack (1983): the language-trained chimpanzee Sarah solved RMTS. Premack concluded that symbol training is needed for second-order relations (a22, second-hand through a06).
- Oden, Thompson and Premack (1988, 1990): apes without language training mostly failed. Flemming et al. (2007) also failed (a06).
- Thompson, Oden and Boysen (1997): language-naive chimpanzees succeeded after training with arbitrary tokens for same and different (a23, a06, second-hand). Thompson and Oden (2000) proposed that only apes, not monkeys, judge relations between relations (a21, second-hand).
- Fagot, Wasserman and Young (2001): baboons learned S/D over icon arrays and showed entropy effects like humans (a24, second-hand). Cook and Wasserman (2007): pigeons matched 16-icon arrays by higher-order relation and transferred to new icon sets (a07).
- Monkeys with pair-RMTS: passed only after extensive training (Fagot and Parron 2010; Fagot and Thompson 2011; Truppa et al. 2011) (a06, a08, a10).
- Vonk (2003) reported gorillas and orangutans with limited training (a06, second-hand).

Result by 2008: relational matching looked like a language-linked human skill, with scattered exceptions that needed tokens, arrays or thousands of trials.

### 2.2 Penn, Holyoak and Povinelli 2008 (full text read in the gap pass, d12)

The article is organised by domain, not by numbered claims. Domains: similarity (perceptual vs relational), rules, higher-order spatial relations, transitive inference, hierarchy, causal relations, theory of mind, and then the "relational reinterpretation hypothesis". Key quantitative cases cited in it (d12):
- Fagot et al. 2001: baboons fell to chance on "different" trials when the sample array shrank from 16 icons to 2. Humans were unaffected. This is the entropy account: arrays can be solved from perceptual variability, not from an abstract relation.
- Bovet and Vauclair 2001: baboons needed on average 14,576 extra trials on a conceptual same/different task.
- Kuhlmeier and Boysen 2002: only 2 of 7 chimpanzees were above chance with identical hiding sites.
- True analogy in apes rested on one chimpanzee, Sarah (Gillan 1981). Oden et al. (2001) later showed Sarah's behaviour could be explained by counting featural differences.

The proposed mechanism is a symbolic-connectionist account (role-filler binding). The paper takes a discontinuity position: a difference in kind, not only degree. Its reading list is large (about 1,176 citations, a01).

### 2.3 Continuity replies

- Fagot and Maugard (2013): baboons solve a re-encoding RMTS where the relevant dimension is only revealed after the sample vanishes, so a stored relation must be re-read. They say this rules out the Penn et al. variability explanation. Penn's camp disputes this (a25, a03-a05).
- Smirnova et al. (2015): hooded crows matched relations after only identity-matching training (b14, abstract only). Dymond and Stewart (2016) criticise the method: not automated, correction trials, possible mealworm sound and smell cues, no inter-observer agreement, two crows (d13). That is a methods challenge, not a failed replication.
- Martin-Ordas (2023): wild bumblebees preferred object matching over relations, but only when the objects were far apart (a14).
- Hodgetts, Close and Hahn (2023): apes use structured similarity in one task and featural similarity in another. The gap depends on stimulus familiarity (a12, a13).

### 2.4 The explicit-reconstrual account (Smith and Church lab)

Rival to a pure representational-capacity story. In humans, finding the relational solution after perceptual cues are faded needs explicit working-memory processing. A concurrent load stops humans from crossing the "perceptual-conceptual barrier" (a09, b16, a26). Reviews read species differences as an explicit-declarative vs implicit-procedural split (b11). This account predicts that making the relation explicit helps, which is exactly what a text scaffold does.

### 2.5 Computational accounts

- Webb, Sinha and Cohen (2021): ESBN, a recurrent net with external memory that binds keys to values (a17, a18, c20).
- Altabaa, Webb, Cohen, Lafferty (2024): Abstractor, relational cross-attention (a20, c21).
- Webb, Frankland, Altabaa et al. (2024): the "relational bottleneck" review. It links Penn et al. to a design principle: force the network to see relations among inputs, not input attributes. Children learn relational tasks from fewer than about 20 examples, versus very large sets for standard nets (a16).
- Geiger et al. (2022): networks can learn identity and ABA patterns with the right input representation (c19). Tartaglini et al. (2023): fine-tuned CLIP ViTs learn S/D out of distribution (c18).

### 2.6 The LLM turn (2022 to 2026)

Webb, Holyoak and Lu (2023) claimed emergent analogy in GPT-3. Hodel and West (2023), Lewis and Mitchell (2024), Stevenson et al. (2024/25) and Musker et al. (2025) tested it with counterfactual twins and found fragility. Webb et al. (2024) replied that code execution closes the gap. In 2025-2026 reasoning models closed the accuracy gap on ConceptARC text but not the competence gap (d01), and a 2026 RMTS study shows frontier VLMs pass animal-style RMTS (d04). The debate has moved from "can they" to "how robust, and by what rule".

## 3. Core findings with exact numbers

Status uses the claims.jsonl labels. Second-hand lines are marked.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Baboons solve re-encoding RMTS after training | 4 baboons; mean 77% correct (range 74.9-80.8%); training 5-6 weeks, 80% needed per block | Fagot and Maugard 2013 (a03) | [E] |
| Perceptual interference is large in baboons | Consistent vs inconsistent trials: shape 96.3 vs 62.2, colour 94.3 vs 55.4. Inconsistent still above chance (68.5 colour, 70.2 shape) | a04 | [E] |
| Cross-dimension probes are fragile | Baseline 76.6% (range 74.7-81.6) vs probes 63.4% (54.4-76.2). 3 of 4 baboons above chance, p<.01 | a05 | [S] |
| Pigeons transfer relational matching imperfectly | 4 pigeons; baseline 79.1, symmetry test 45.3, novel sets 60.8 and 59.2, retest transfer 70.1 vs 75.7; only 2 of 3 transferred in Phase 4 | Cook and Wasserman 2007 (a07) | [S] |
| Capuchins rarely learn RMTS | 1 of 5 passed. First set mean 11,639 trials to criterion. Roberta: 7,392 trials to flip a same-bias, then 21,888 trials to about 70%. Transfer 65.6-67.7% | Truppa 2011 (a08) | [E] |
| Monkeys mostly fail | Rhesus none above chance over 10,000 trials (up to 260,000 with cue fading in reviews). Capuchins above chance only in sessions 14-15, run without opaque screens | Thompson 2016 (b12); b11 | [E] |
| Few baboons acquire pair-RMTS | 6 of 29 reached 80% after 15,000-30,000 trials (review figure) | Fagot and Thompson 2011 via a10 | [E] (second-hand) |
| Humans reach RMTS easily | About 99% correct in the unloaded fading task; 43 of 53 (80%) crossed fast, 20% stalled at similarity in the 60s | Smith et al. 2019 (a09, a10) | [S] |
| Working-memory load blocks the crossing | Control N=53 matching .913; load N=51 .865; number task .938 vs .833 | a09, b16 | [S] |
| Apes use structure less in unfamiliar tasks | Humans 98% (Task 1) and 90% (Task 2) variance by structural model; apes 58% in Task 1, featural 98% in Task 2; species x task F(1,15)=14.99, p=.002 | Hodgetts 2023 (a12, a13) | [S] |
| Bumblebees choose objects, not relations, when far apart | Distant: object over spatial W=3, P=0.002; Near: no preference W=31, P=0.891; 33% relational, 40% object strategy | Martin-Ordas 2023 (a14) | [C] |
| Pigeon "analogy" advantage came from a cue | Mean error distance 1.15 (ordered) vs 1.73 (random); no speed difference after reversal; 6 birds | b17 | [S] |
| Infants represent "same" up to 4 items | 6 experiments, N=192; 4 items yes, 5 or 6 no | Hochmann 2022 (b20) | [S] |
| Noun labels unlock relational choice in preschoolers | n=192; helps 4- and 5-year-olds, not 3; adjectives no help | Zhu 2025 (b21) | [S] |
| Toddlers infer "same" not "different" | Same 28/41 (68%, BF10=4.07); different 25/50 (50%, BF10=0.33) | b22 | [S] |
| Relational complexity lowers human accuracy | Criterion in 20.2 +/- 0.86 trials; transfer accuracy 0.82 +/- 0.02 | b18 | [S] |
| Plain GPT-3 matches humans on in-distribution analogy | Digit Matrices (humans N=40): generative OR 1.88 (p=0.005), multiple choice OR 6.27 (p=2.3e-8); letter strings (N=57) OR 1.76; semantic-distance OR 3.24 (p=0.0165); story analogy OR 0.37 (p=0.0003) | Webb 2023 (c01, c03, c04, b01) | [C] |
| Counterfactual letter strings break LLMs | Humans 0.753 (136 people, 1,876 samples); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (6,840 each) | Lewis and Mitchell 2024 (b03, c07) | [E] |
| Synthetic alphabet breaks GPT-3 | Generative accuracy below 0.1 on extend, successor, predecessor, fix; humans (N=121) unchanged | Hodel and West 2023 (b05, c06) | [E] |
| Code closes the gap (reply) | GPT-4 plain vs humans P=8.9e-13; GPT-4+code vs humans P=0.496; 46% of GPT-4 errors used a valid alternative rule | Webb 2024 (b06, c08) | [C] |
| Error types differ | Alternate valid rule: GPT-3 5.81, GPT-4 22.00, humans 38.59%. Incorrect rule 30.97 / 32.67 / 14.67% | b04 | [S] |
| Transfer across alphabets fails for models, not people | Latin/Greek/Symbol: adults .88/.91/.89; children .62/.66/.67; GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Llama-405B .79/.74/.27; Gemma-2 27B .60/.39/.14 | Stevenson 2024/25 (d07, c09) | [E] |
| Order of examples changes LLMs, not humans | Permuted pairs: Claude 3 -1.78 (z=-4.22), GPT-4 -1.68 (z=-3.98), Llama-405B -2.34 (z=-5.50), all p<0.001. Default condition no gap (p=0.097, 0.194, 0.097) | Musker 2025 (b07, c11, d14) | [S] |
| Text format hurts | ACRE GPT-4 text 0.272 vs symbolic 0.512; GPT-3.5 0.184 vs 0.445; davinci-003 0.098 vs 0.427 | Gendron 2023 (c15) | [E] |
| GPT-4 failed ConceptARC in 2023 | Humans over 90% on 11 of 16 concepts, over 80% on the rest; GPT-4 under 30% on 15 of 16; best ARC program under 80%, below 60% on 11 of 16 | Moskvichev 2023 (b08) | [E] |
| o3 closes the accuracy gap on ConceptARC text | o3 medium 77.1, low 68.3, medium+tools 75.6; humans 73.0; Gemini 2.5 Pro 66.0; Claude Sonnet 4 60.2 | Beger 2025 (d01) | [S] |
| But the rules are often wrong | Unintended or incorrect rules among correct outputs: o3 and Gemini about 27%, Claude about 19%, humans about 7% | d01 | [S] |
| Vision: right rule, wrong grid | Correct-intended rules vs correct grids: o3 40.0 vs 29.2, Claude 14.4 vs 6.9, Gemini 23.5 vs 5.8 (McNemar p<1e-5) | d02 | [S] |
| Rule choice is unstable across runs | Same rule class in all 3 passes for only 54.2-56.4% of tasks; pairwise consistency 66.0-70.9% | d17 | [S] |
| More tokens do not fix range shift | I-RAVEN to I-RAVEN-X: o3-mini 86.6 to 17.0 at 3.4x tokens; R1 80.6 to 23.2; neuro-symbolic ARLC 98.6 to 88.0 | Camposampiero 2025 (d06) | [S] |
| Frontier VLMs pass animal-style RMTS | Relational rate, no CoT: GPT-5.4 100, Opus 4.6 100, Gemini 3.1 Pro 100; GPT-5.4-mini 32.2, Haiku 4.5 42.5. With CoT: 83.4 and 99.9 | Minegishi 2026 (d04) | [S] |
| Scale decides the relational circuit | Qwen3.5 0.8B 50.0 (no circuit), 4B 77.3, 9B 89.3; Gemma-4 E2B 26.3 to 31B 100 | d04, d05 | [S] |
| Reasoning models beat plain LLMs on nonword syllogisms; analogy weakest | Analogy: Llama 3.3 70B 47.31, Llama 3.1 405B 55.19, GPT OSS 20B 83.27, GPT OSS 120B 83.85. Shuffled premises: 48.27, 55.39, 77.50, 79.81 | Raemaekers 2025 (d10) | [S] |
| Relation-encoding architectures generalise OOD | Same/different at m=95: ESBN+TCN 100.0, Transformer 73.7, LSTM 61.8, Relation Net 50.5; m=98: 100.0 vs 56.1 / 56.5 / 52.3. Distribution-of-3 m=95: 99.7 vs 28.0 | Webb 2021 (a17, a18, c20) | [E] |
| Self-generated analogies give small gains | GSM8K GPT-3.5: 0-shot 75.0, CoT 75.8, 5-shot CoT 76.7, analogical 77.8; davinci-003: 14.8 / 50.3 / 54.0 / 61.0 | Yasunaga 2024 (c13) | [E] |
| Counterfactual twins reduce many tasks | Arithmetic from near-perfect to near-zero in some bases; MiniSCAN from above 80% to almost zero | Wu 2024 (c14); Qiu 2024 (b09) | [E] |
| Abstraction-then-map helps far analogies in small models | MCQ Llama YARN 0.45 vs 0.28; Qwen 0.46 vs 0.41; near ARN: Qwen CoT 0.79 vs YARN 0.69 | Khojasteh 2026 (d09) | [S] |
| Patching hidden states recovers part of failures | Up to 38.4% behaviour change (Gemma-7B); 32.3% Llama-2-13B; 35.6% Qwen2.5-14B | Lee 2025 (d08) | [S] |
| Penn et al. quantitative anchors | Baboons at chance on 2-icon different trials; 14,576 extra trials; Sarah the only analogy case | d12 | [E] (full text) |

## 4. Mechanisms and models

Each mechanism is stated so an engineer can build it.

### 4.1 Entropy and variability shortcut (why array tasks fool you)

Mechanism: in a 16-icon array, "all same" has low variability and "all different" has high variability. A system can pick the matching array by comparing a variability score. No relation is needed. With 2 icons the shortcut disappears (d12, a24, a25, b11).
Implementation: when you build a relational test for the agent, compute a surface statistic (token overlap, string length, count of distinct tokens) for each option. If a classifier on that statistic alone gets above chance, the item leaks. Drop it or add a probe that breaks it (cross-mapping, reversal; a05, b17).

### 4.2 Re-encoding probe (Fagot and Maugard)

Mechanism: show the source, then reveal the question dimension only after the source is gone. The solver must hold a relation, not a percept. Cross-mapping probes use colour in the source and shape in the target (a03-a05).
Implementation: build item twins. Twin A shares surface features with the answer. Twin B uses a different surface (rename entities, swap alphabet, swap modality). Score twin B minus twin A. Consistent vs inconsistent cue trials (96.3 vs 62.2 in baboons) give a "cue interference" score you can report for the agent.

### 4.3 The perceptual-conceptual barrier (Smith and Church)

Mechanism: start with items where a cheap perceptual match works. Fade the cue in steps (similarity ladder). A solver that only uses the cue collapses when it fades. A solver that builds the relation crosses. Load blocks crossing (a09).
Implementation: a similarity ladder of 8 to 16 levels. Report the level at which accuracy collapses. For an LLM, "load" is long context or distractors, so test with matched irrelevant text (loose analogue in d10).

### 4.4 Relational bottleneck, ESBN, Abstractor (what the scaffold must emulate)

Mechanism (ESBN, a17): the controller never sees the content. It sees only similarity between a new item and stored keys. Content values sit in an external memory slot bound to a key. Rules are learned over keys, so they apply to unseen content. Temporal context normalisation (TCN) was needed: without it ESBN stays near 50% on same/different (a17, c20).
Mechanism (Abstractor, a20): relational cross-attention. Queries and keys are object features, but the values are pairwise relation vectors, so the output carries only relations.
Text analogue for an agent (O7 pre-step; untested): (1) an extraction call lists entities as symbols E1..En with a typed relation table R(Ei, Ej) = label; (2) the solving call sees only the table, not the surface words; (3) code maps symbols back to words. YARN (d09) is a small-model version: decompose, abstract roles, then map.

### 4.5 Two circuits in VLMs (Minegishi 2026)

Mechanism: an early circuit groups by surface object features. A late circuit groups by abstract relation. Direct answers can follow the early circuit. Chain of thought lets the late circuit win. Head ablation on ARC-AGI-1 drops accuracy more than random-head ablation for Gemma-4-26B and 31B. With CoT the relational answer survives ablation (d05).
Implication: for small models, an explicit "write the relation first" step moves the answer from the object route to the relation route (GPT-5.4-mini 32.2 to 83.4; Haiku 4.5 42.5 to 99.9; d04).

### 4.6 Relation encoded, application fails (Lee 2025)

Mechanism: probes find the relation in mid-upper layers when the model succeeds. Failures come from missing relation info or from failing to apply it to the new entity. Patching the first pair's hidden state recovers up to 38% (d08).
Implementation: an external executor applies the rule. The model proposes the rule, code applies it (b09, b10, b06).

### 4.7 Hypothesis refinement with an interpreter (Qiu 2024)

Mechanism: the LM proposes a rule as a program, an interpreter runs it on the examples, the failing cases are shown back, the LM refines. It was strongest on 3 of 4 datasets, yet collapsed on counterfactual variants (b09, b10). It matches the schema S2 to S5 loop plus G2 and G3.

### 4.8 Analogical prompting (Yasunaga 2024)

Mechanism: the prompt asks the model to write related problems with solutions, then solve the target. Gains are small on strong models, large on weak ones (c13). Of 50 failures, 10 had irrelevant exemplars, 12 had wrong ones, and 28 had correct exemplars but still failed (c13).

## 5. What holds up

### 5.1 Animal side

Holds up ([E]):
- RMTS is hard for non-human primates. Rhesus: none passed over 10,000 trials in the 2016 replication, and 260,000 trials in cue-fading reports (b12, b11). Baboons: 6 of 29 (a10). Capuchins: 1 of 5, at about 70% (a08).
- Perceptual cues interfere strongly. Baboon consistent vs inconsistent: 96.3 vs 62.2 (a04).
- Results shrink when cueing is controlled. Thompson 2016: capuchins above chance only in sessions run without opaque screens (b12).

Contested ([C]):
- Whether array successes are relational. Penn et al. say variability explains them. Fagot and Maugard say their design rules this out (a25).
- Crow analogy (b14). Dymond and Stewart (d13) list method flaws. No formal failed replication was found.
- Bumblebees prefer objects over relations when objects are far apart (a14).

Not verified: Premack 1983, Thompson-Oden 1997 and 2000, Fagot 2001 are second-hand (a21-a24). The "6 of 29" figure comes from reviews.

Moderators found: training length, token or symbol training, stimulus familiarity (a12, a13), array size and entropy, meaningful vs abstract stimuli (a11), spatial separation (b11), distance between objects (a14), and small animal groups (typically 1 to 6 animals).

Interventions that worked in animals: arbitrary tokens in chimpanzees (a06, b13); gradual cue fading in some baboons (a10); differential outcomes giving rhesus transitory two-item RMTS (b13). Did not work: token training in rhesus (Flemming 2008, b13); cue fading in rhesus (a10, b11); differential reward alone (a10).

### 5.2 Human side

- Humans cross the perceptual-conceptual barrier at high rates (80% fast, 20% stall) and load disrupts it (a09). Infant capacity is bounded (4 items; b20). Naming helps 4- and 5-year-olds (b21). So humans are not "all relational": they depend on explicit processing.
- Warning from Hodel and West: matching a human score does not show the same mechanism (b25).

### 5.3 Machine side

Holds up:
- Counterfactual drops are robust across studies: Hodel and West (b05), Lewis and Mitchell (b03), Stevenson (d07), Wu (c14), Qiu (b09). Four or more groups.
- Text format penalty (c15).
- Relational bottleneck architectures generalise OOD (a17, a18, c20, c21).

Contested:
- Whether counterfactual failure is comprehension (Lewis and Mitchell: comprehension checks mostly near 1.0, so mostly not), counting (Webb 2024: code fixes it), or missing prerequisites (Stevenson: ordering rules fail, repetition rules transfer; d07). All three have evidence. They may add up.
- Whether Webb's original result survives. Lewis and Mitchell found GPT accuracy below the human average even on the original alphabet (b03).

Interventions that worked on LLMs:
- Code execution (Webb 2024: P=0.496 vs humans; b06, c08). Written by the original authors, not independent.
- Chain of thought on small VLMs (d04).
- Prepending earlier solved items (Stevenson, c10).
- Ordinal-number attribute naming over random naming (over 20 points in larger models, c12) and decomposition by attribute (+2.8 for GPT-3 175B; OPT 125M 22.2 to 45.6; c12).
- Symbolic rather than text encoding (c15).
- Abstraction-then-map in small open models, far analogies only (d09).

Interventions that did not work or were small:
- Chain of thought on abstract tasks was often no better (c16).
- Self-generated analogies on strong models: +1.0 to +2.0 points on GSM8K (c13).
- More reasoning tokens under range shift: 86.6 to 17.0 at 3.4x tokens (d06).
- Tools on ConceptARC text: no gain for o3 (75.6 vs 77.1 at medium), losses for Claude (55.0 vs 60.2) and Gemini (60.4 vs 66.0) (d01). In vision, tools help (d02).

Gaps (critique.md): no 2025-2026 reasoning-model result on counterfactual alphabets was found; no scaffold-vs-plain test at equal tokens on relational tasks (d16); no distractor-similarity study mirroring Smith 2019.

## 6. Language models

### 6.1 Timeline of how LLMs behave

| Period | What was found | Numbers | Ids |
|---|---|---|---|
| 2021 | Plain nets (LSTM, Transformer, Relation Net) fail OOD on same/different and RMTS, like untrained animals. ESBN with binding memory does not. | m=95: Transformer 73.7, ESBN+TCN 100.0; RMTS m=95: Transformer 49.9, ESBN+TCN 95.0 | a17, c20 |
| 2022-23 | GPT-3 matches or beats UCLA students on text analogy | Digit Matrices OR 1.88 (generative), 6.27 (multiple choice); letter strings OR 1.76 | b01, c01 |
| 2023 | GPT-4 weak on grid concepts | ConceptARC GPT-4 under 30% on 15 of 16 concepts; humans over 90% on 11 | b08 |
| 2023 | Abstract-reasoning benchmarks: low scores, CoT no rescue, text worse than symbolic | ACRE GPT-4 0.272 text, 0.512 symbolic | c15, c16 |
| 2023-24 | Counterfactual twins break GPT-3/3.5/4; humans unaffected | GPT-3 <0.1 on synthetic alphabet; mean 0.488 / 0.350 / 0.452 vs humans 0.753 | b05, b03, c07 |
| 2024 | Reply: GPT-4 with code matches humans | P=0.496 | b06, c08 |
| 2024-25 | Cross-alphabet transfer fails; ordering rule missing | GPT-4o .85 to .48; Llama-405B .79 to .27 vs adults .88 to .89 | d07 |
| 2025 | Best LLMs match humans on default semantic mapping; order permutation breaks them | Coefs -1.68 to -2.34, p<0.001 | c11, b07 |
| 2025 | Reasoning models close accuracy on ConceptARC text but use wrong rules | o3 77.1 vs humans 73.0; about 27% unintended rules vs 7% | d01 |
| 2025 | Reasoning models collapse under range and noise shift | o3-mini 86.6 to 17.0 | d06 |
| 2025 | Open models: relation encoded, application fails | Patching recovers up to 38% | d08 |
| 2026 | Frontier VLMs pass animal-style RMTS; small ones are object-biased until CoT | 100 vs 32.2 / 42.5; CoT 83.4 / 99.9 | d04 |

### 6.2 What the pattern says

1. Capacity is there on familiar items. Plain frontier models pass in-distribution analogies and simple RMTS (d04, c01).
2. Robustness is not there. Rename the alphabet, reorder the examples, widen the value range, change the modality, and accuracy drops. Humans do not drop on most of these (d07, c11, d06).
3. The accuracy gap and the competence gap are different. o3 gets 77.1% on ConceptARC text, above humans, but about 27% of its correct answers rest on an unintended rule versus about 7% for humans. In vision the right rule is found more often than the right grid is produced (d01, d02). Rule choice changes across identical runs in nearly half of tasks (d17).
4. Models describe grids with cell words, humans with object words (d03). The input format differs (humans saw images), so treat this as a hint.
5. Failure causes stack. Misreading (small), counting or indexing (fixed by code, b06), missing prerequisites such as ordering (d07), and failure to apply an encoded relation (d08).
6. Scale and reasoning matter a lot for the easy relations. Below 4B parameters a relational circuit may never form (Qwen3.5-0.8B at 50.0, d05). GPT OSS 120B gets 83.85 on analogy syllogisms vs 55.19 for Llama 3.1 405B (d10). Reasoning models do not fix hard shifts (d06).

### 6.3 What changed it, by how much

| Change | Effect | Ids |
|---|---|---|
| Code execution for counting letters | GPT-4 from significantly below humans to P=0.496 (no difference) | b06, c08 |
| Chain of thought, small VLM | GPT-5.4-mini 32.2 to 83.4; Haiku 4.5 42.5 to 99.9 | d04 |
| Reasoning effort, o3 on ConceptARC text | low 68.3 to medium 77.1 (+8.8) | d01, d16 |
| Reasoning effort in vision | no gain; tools help (o3 5.6-6.7 to 29.2) | d02 |
| Python tools, text | o3 77.1 to 75.6; Claude 60.2 to 55.0; Gemini 66.0 to 60.4 | d01 |
| Symbolic encoding vs text | GPT-4 ACRE 0.272 to 0.512 | c15 |
| Ordinal vs random attribute names in text Raven | over 20 points in large models | c12 |
| Decompose Raven problem by attribute | GPT-3 175B +2.8; OPT 125M 22.2 to 45.6 | c12 |
| Prepend solved examples | LLMs generally better (size in appendix, not read) | c10 |
| Self-generated analogical exemplars | GSM8K GPT-3.5 75.8 to 77.8; davinci-003 50.3 to 61.0 | c13 |
| Abstract-then-map pipeline | far MCQ Llama 0.28 to 0.45; near analogies no gain | d09 |
| Fine-tuned CLIP for S/D | above 95% median on OOD sets | c18 |
| Extra reasoning tokens under shift | 86.6 to 17.0 even at 3.4x tokens | d06 |

### 6.4 Conflicts in the LLM record

- Webb 2023 vs Lewis and Mitchell / Hodel and West: same task family, opposite verdict. The difference is the item (familiar or counterfactual) and code use (critique.md).
- Monk et al. 2024 (abstract only, d11) says language models fail animal-style RMTS. The 2026 VLM study says frontier models pass (d04). The first is unverified, so the second stands.
- Musker 2025: no gap by default, large gap when the order is permuted. Both are true.
- Human baselines differ across studies (0.753 Prolific vs undergraduates), so the size of the gap shifts with the human sample.

## 7. What our agent should take

Tags: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = S9 lessons and class pass rates.

### Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Every new operator or relational step is tested on a surface-changed twin (renamed entities, permuted alphabet, recoded symbols), not only on the familiar item. A pass on the familiar item alone is not a pass. | G3, G7 | [E] | b03, b05, d07, c14, b09 (K07, K16) |
| A2 | The model proposes the rule; code applies it and checks it on held-out inputs. Counting, indexing and ordering are done in code, not by the model. | G2, G5, O7 | [E] for the split (rule found, application fails); [C] for how much code explains | b09, b10, d08, d02, b06 (K08) |
| A3 | Re-encode text-form relational problems into a symbolic or typed form before solving (ordinal attribute names, symbols). | S2, O6 | [E] | c15, c12 (K11) |
| A4 | Keep O7 as a late operator fired at an impasse, not a default. Unaided analogy gives small gains on strong models (+1 to +2 points) and large ones only on weak models. | G1, G11, O7 | [E] | c13 (K12) |
| A5 | Do not read an accuracy pass as competence. For ARC-like items, log the stated rule beside the answer (feeds S9) and score both. | G10, S9 | [S] for the 27% figure, [E] for the principle | d01, d17 (K17) |
| A6 | Count a model's counterfactual or twin drop as the measured robustness of a class. Store it in the class record. | S0, memory | [E] | b03, d07 |

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Role-filler table step before mapping: list entities as E1..En, relations as a table, solve on the table, code maps back. | O7, S2 | [S], small open models only, no equal-token test | d09, a16, a17 (K21, K13) |
| T2 | "Write the relation first" step for small or weak backbones. Large gain in small VLMs; frontier models are already at ceiling. | S2, O7 | [S] | d04, d05 (K19) |
| T3 | State the rule, then test it on an object-level paraphrase and a recoded variant. Compare intended-rule rate and accuracy to plain at equal tokens. | S4, S8, G3 | [S] | d01, d03, d17 (K17) |
| T4 | Average over shuffled example orders (2 to 3 orders) when the item gives example pairs. Cost is extra samples, so compare at equal tokens against single-order best-of-N. | S3, G4 | [S] | b07, c11, d14 (K09) |
| T5 | Rule-induce-then-execute with an external executor under range and noise shift. | O7, G5 | [S] | d06, d16 (K18) |
| T6 | Second-mapping check: ask for an alternative valid rule and score both (humans find alternates in 38.59% of errors, GPT-3 5.81%). | S7 | [S] | b04, c08 |
| T7 | Short noun-label step: name the relation in one word before using it. | S1, S2 | [S] human-only (preschoolers) | b21, a06 |
| T8 | Similarity-ladder fading: start with a cue-rich analogue, then strip surface cues step by step. | O7, S5 | [S] human-only | a09, a26 (K15) |
| T9 | Reasoning-token cap vs relation-first scaffold on far-analogy items (does extra thinking help or hurt?). | G11, G12 | [C] | d06, d01, d16 |
| T10 | Entropy-leak check on our own relational test items before use. | test hygiene | [E] for the leak principle, test is cheap | d12, a25 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (G7), setup cost counted, at least 3 seeds, items drawn so that the twin is matched to the original. The baseline arm is plain model at the same budget with the best of N short attempts, voted in code.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 twin robustness (A1, A6) | Letter-string analogies in Latin, permuted (2, 5, 10 letters) and symbol alphabets; 60 items per alphabet | plain vs scaffold with code for ordering and counting | Accuracy per alphabet; drop = Latin minus symbol | Plain drop of 20 to 40 points on strong non-reasoning models (d07: GPT-4o .85 to .48). Scaffold drop under 10 points. |
| B2 propose-apply split (A2) | ConceptARC-style grids, 16 concepts x 3 items (use text grids) | model solves directly vs model writes program rule, code applies and checks on held-out pair | Accuracy and intended-rule rate (human-coded on a subset) | Gain of 5 to 15 points on non-reasoning backbones; near zero for o3-class (d01 shows tools did not help text). |
| B3 role-filler table (T1) | Far analogies (word and story) 100 items; near 100 items | CoT vs extract-table-then-map | Accuracy, split near vs far | Gain on far, none or loss on near (d09). Success if far gain at least 5 points at equal tokens. |
| B4 write-the-relation (T2) | RMTS-style text items with nonce labels, object-bias rate | direct vs relation-first, on a small backbone and the main one | Relational-choice rate | Small backbone +30 to +50 points (d04); main backbone no change at ceiling. |
| B5 rule statement audit (T3) | ConceptARC subset, 80 items | plain reasoning vs state-rule-then-test-on-paraphrase | Accuracy; share of correct answers with an unintended rule | Unintended-rule share falls from about 27% toward 10% with no accuracy loss. |
| B6 order averaging (T4) | Musker-style mapping items with permuted pair order, 3 orders | single order, best-of-3 same order, 3 shuffled orders voted in code | Accuracy under permutation | Shuffled-order voting recovers part of the drop; best-of-3 same order does not. Success if shuffled beats same-order at equal tokens. |
| B7 range shift (T5) | I-RAVEN-X-style generated matrices with value ranges 10x training range, noisy attributes | plain reasoning vs induce-rule-then-execute | Accuracy at standard and shifted range | Plain falls more than 30 points (d06); executor arm falls under 10. |
| B8 second mapping (T6) | Letter-string items with a valid alternative rule | single rule vs two-rule scoring | Fraction of correct-alternative answers accepted | Raises measured accuracy; checks whether the model finds alternates (GPT-4 22% in b04, 46% in b06). |
| B9 ladder (T8) | Analogy items with surface similarity at 5 levels | plain vs fading ladder prompt | Accuracy at lowest-similarity level | Gain at the low-similarity levels, none at the high end. Human-only evidence, so treat as exploratory. |
| B10 thinking cap (T9) | Far analogy 100 items | reasoning budget 1x, 3x vs relation-first scaffold at 1x | Accuracy per token | Extra tokens give little under shift (d06); scaffold wins per token. |
| B11 leak check (T10) | Our own relational item pools | surface-feature classifier | Accuracy of the classifier on item features | Must be within 5 points of chance; otherwise rewrite items. |

## 9. What does not transfer, and why

- Heavy-training results (thousands of trials in baboons, capuchins, rhesus). The agent gets zero task training and works in context. The animal learning curve is not our problem (a08).
- Species cut-off arguments (apes yes, monkeys no; Thompson and Oden). Graded species differences give no operator for a model.
- Array entropy shortcuts and Clever Hans cueing. Relevant only as test-design hygiene (B11), not as agent behaviour.
- Bumblebee spatial-search paradigm (a14). Different task, small wild-caught samples.
- Infant capacity limit of 4 items (b20). A model has a context window, not a 4-item limit. It transfers only as "chunk before comparing", which is untested for LLMs.
- Cultural effects in toddlers (b22). No analogue in a text scaffold.
- ESBN, Abstractor, relational bottleneck architectures. They require training. The scaffold can only imitate the idea in text (T1), and the imitation is not evidence that the idea works in a prompt.
- Neural patching and head ablation (d05, d08). Needs internal access; we use an API.
- Human working-memory load (a09). Literal load manipulations do not map to a model; only a loose analogue (long distractor context) exists.
- Fine-tuned CLIP same/different (c18). Training result.
- Language-trained ape symbols (Premack). The nearest equivalent is explicit relation labels in text, which is already part of S2.

## 10. Open questions

1. Do 2025-2026 reasoning models close the counterfactual-alphabet and ConceptARC twin gaps, and at what token cost? (partly closed: accuracy yes on ConceptARC text, d01; counterfactual alphabets not tested.)
2. Does a role-filler table step beat plain CoT at equal tokens on frontier models? Only small open models were tested (d09).
3. How much of the LLM twin drop is misreading, counting, missing prerequisites, or failure to abstract? Three accounts, all with partial evidence (b23, b06, d07, d08).
4. Is order sensitivity fixed by averaging over shuffled orders? No study (d14).
5. Do self-generated analogies still help on 2025+ models? No test found (d15).
6. Does the gap on animal RMTS survive controlled replication? Crow and pigeon transfer have only methods critiques (d13); monkey results are consistent but small-N.
7. Effect size of the species gap was never computed across species (critique gap 7).
8. Does accuracy fall with distractor similarity or context length in LLMs as it does in humans under load (Smith 2019)? Not tested (critique gap 9).
9. What exactly did Monk, Meyer and Ngo (2024) test? Abstract only (d11).
10. Are the human baselines comparable across studies? 0.753 Prolific vs undergraduate samples (critique.md).
11. Is the rule instability across runs (54 to 56% identical) a cost that voting over rules, not answers, can fix? Untested (d17).

## 11. Sources

[V] = opened and read this session or in the gap pass. [M] = abstract, snippet or second-hand only.

Animal and human studies
- [V] Penn, Holyoak, Povinelli (2008) Darwin's mistake. https://doi.org/10.1017/s0140525x08003543 ; full text https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Penn-Holyoak-Povinelli.2008.pdf ; PubMed https://pubmed.ncbi.nlm.nih.gov/18479531/ (the PubMed record is abstract-only) (a01, a02, b15, d12)
- [V] Fagot and Maugard (2013) Analogical reasoning in baboons. https://link.springer.com/content/pdf/10.3758%2Fs13420-012-0101-7.pdf (a03-a06, a25)
- [V] Cook and Wasserman (2007) Relational matching-to-sample by pigeons. https://link.springer.com/content/pdf/10.3758/BF03193099.pdf (a07)
- [V] Truppa et al. (2011) Capuchin same/different. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0023809&type=printable (a08)
- [V] Smith, Jackson, Church (2019) Breaking the perceptual-conceptual barrier. https://link.springer.com/content/pdf/10.3758/s13421-018-0890-9.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6451666/ (a09, a10, a26, b16)
- [V] Flemming et al. (2008) What meaning means for same and different (abstract). https://pubmed.ncbi.nlm.nih.gov/18489233/ (a11)
- [V] Hodgetts, Close, Hahn (2023) Similarity and structured representation. https://eprints.bbk.ac.uk/id/eprint/50753/1/50753.pdf (a12, a13)
- [V] Martin-Ordas (2023) Wild bumblebees revisited. https://www.nature.com/articles/s41598-023-49840-5.pdf (a14)
- [V] Dissociative framework for same-different conceptualization (2021 review). https://pmc.ncbi.nlm.nih.gov/articles/PMC8192071/ (b11)
- [V] Thompson, Flemming, Hagmann (2016) Old-world and new-world monkeys and spatial relations. https://pmc.ncbi.nlm.nih.gov/articles/PMC4729642/ (b12, b13)
- [M] Smirnova et al. (2015) Crows spontaneously exhibit analogical reasoning. https://pubmed.ncbi.nlm.nih.gov/25532894/ (b14)
- [V] Dymond and Stewart (2016) Relational and analogical reasoning in comparative cognition. https://journalpub.escholarship.org/uclapsych_ijcp/article/5419/galley/3267/download (d13)
- [V] Endpoint distinctiveness in pigeons (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4405791/ (b17)
- [V] Relational complexity influences analogical reasoning ability (2023, iScience). https://pmc.ncbi.nlm.nih.gov/articles/PMC10074587/ (b18, b19)
- [V] Hochmann (2022) Abstract relations in infancy. https://pmc.ncbi.nlm.nih.gov/articles/PMC9987345/ (b20)
- [V] Zhu (2025) Preschoolers and kind membership. https://pmc.ncbi.nlm.nih.gov/articles/PMC11729786/ (b21)
- [V] Relational reasoning across cultures: South Korea, US, China (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13509761/ (b22)
- [M] Thompson and Oden (2000) The paleological monkey and the analogical ape. https://doi.org/10.1207/s15516709cog2403_2 (a21)
- [M] Premack (1983) The codes of man and beasts. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences (a22)
- [M] Thompson, Oden, Boysen (1997) Language-naive chimpanzees. Only a search link was recorded (a23)
- [M] Fagot, Wasserman, Young (2001) Entropy in baboons and humans. Only a search link was recorded (a24)

Models and architectures
- [V] Webb, Sinha, Cohen (2021) Emergent symbols through binding in external memory. https://arxiv.org/abs/2012.14601 (a17-a19, c20)
- [V] Altabaa, Webb, Cohen, Lafferty (2024) Abstractors. https://arxiv.org/abs/2304.00195 (a20, c21)
- [V] Webb, Frankland, Altabaa et al. (2024) The relational bottleneck. https://arxiv.org/abs/2309.06629 (a16)
- [V] Geiger, Carstensen, Frank, Potts (2022) Relational reasoning and generalization in neural networks. https://arxiv.org/abs/2006.07968 (c19)
- [V] Tartaglini et al. (2023) Deep networks can learn same-different. https://arxiv.org/abs/2310.09612 (c18)

LLM and AI studies
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a15, b01, b02, b24, c01-c05)
- [V] Hodel and West (2023) Response. https://arxiv.org/abs/2308.16118 (b05, b25, c06)
- [V] Lewis and Mitchell (2024) Counterfactual tasks and analogical reasoning. https://arxiv.org/abs/2402.08955 (b03, b04, b23, c07)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks. https://arxiv.org/abs/2404.13070 (b06, c08)
- [V] Stevenson et al. (2024/2025) Can LLMs generalize analogy solving like people. https://arxiv.org/abs/2411.02348 (c09, c10, d07)
- [V] Musker et al. (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (b07, c11, d14)
- [V] Moskvichev, Odouard, Mitchell (2023) ConceptARC. https://arxiv.org/abs/2305.07141 (b08)
- [V] Qiu et al. (2024) Phenomenal yet puzzling. https://arxiv.org/abs/2310.08559 (b09, b10)
- [V] Hu et al. (2023) In-context analogical reasoning with language models (Raven). https://arxiv.org/abs/2305.17626 (c12)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (c13); [M] for the 2025-26 follow-up search (d15)
- [V] Wu et al. (2024) Reasoning or reciting. https://arxiv.org/abs/2307.02477 (c14)
- [V] Gendron et al. (2023) LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 (c15, c16)
- [V] Yiu et al. (2025) KiVA. https://arxiv.org/abs/2407.17773 (c17)
- [V] Beger et al. (2025) Distinguishing rule from answer on ConceptARC. https://arxiv.org/abs/2510.02125 (d01-d03, d16, d17)
- [V] Minegishi et al. (2026) Matching Object or Relation. https://arxiv.org/abs/2610.07646 (d04, d05; URL as recorded in the evidence file)
- [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty (I-RAVEN-X). https://arxiv.org/abs/2503.11207 (d06)
- [V] Lee et al. (2025) The Curious Case of Analogies. https://arxiv.org/abs/2511.20344 (d08)
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/abs/2603.29997 (d09)
- [V] Raemaekers, Finn, De Houwer (2025) Relational abilities of LLMs and reasoning models. https://pmc.ncbi.nlm.nih.gov/articles/PMC12837307/ (d10)
- [M] Monk, Meyer, Ngo (2024) Language models and uniquely human cognition (RMTS). https://www.preprints.org/manuscript/202401.1681 (c22, d11; abstract only, HTTP 403)
