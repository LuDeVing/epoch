# Connectionist and hybrid mapping models: deep document

*Subfield A11.05. Evidence ids (a01-a27, b01-b26, c01-c30, d01-d18) and claim ids (A11.05-K01 to K28) refer to the jsonl files in this folder. Written 2026-11-03 from those files and critique.md. Schema parts: G guardrail, S state, O operator.*

## 1. What it is

This subfield covers three families of models of analogy.

- **ACME** (Holyoak and Thagard 1989). A localist constraint-satisfaction network. Each unit says "element X in the source maps to element Y in the target". Links between units encode three soft constraints: structure (one-to-one, consistent arguments), meaning similarity, and pragmatic importance (what the goal needs). The network relaxes until it settles.
- **LISA** (Hummel and Holyoak 1997, 2003). A hybrid symbolic-connectionist model. Predicates and objects are distributed meaning patterns. Role-filler bindings are held by synchrony of firing. One architecture does access (retrieval), mapping, inference and schema induction. Working memory is small: about 4 to 6 role bindings at once.
- **Copycat** (Hofstadter and Mitchell). Analogy as perception. Representation building and mapping run together in one loop. A "temperature" measures how coherent the current answer is and sets how random the search is.

Why it matters for our agent: these are the oldest worked designs for a mapping step. They say what a mapping step must do: score candidate correspondences on several constraints, enforce one-to-one, respect a capacity limit, keep retrieval apart from mapping, gate inferences on coverage, and re-describe while mapping. Since 2023 a second literature tests whether LLMs do this. That literature gives the numbers we can use.

Honest summary: the model papers are mostly small hand-built simulations that reproduce the signs of human effects, not their sizes. The LLM literature is large, partly contested, and mostly on letter strings. Almost nothing here has been tested as a prompt scaffold at equal tokens. That is why most of section 7 is "Test first".

## 2. History and theories in depth

### 2.1 Background
- Structure-mapping (Gentner) says analogy aligns relational structure and prefers systematic, higher-order relations. SME implements this with given representations and a hard structural filter.
- Multiconstraint theory (Holyoak and Thagard 1995/1997; a17) says analogy is shaped by three pressures at once: similarity, structure, purpose. They are found by parallel constraint satisfaction. ARCS handles access, ACME handles mapping, and ACME was extended to inference (Holyoak, Novick, Melz 1994).

### 2.2 ACME (1989)
- Setup: predicate-calculus propositions for each analog. A unit is made for every plausible pair of elements. Excitatory links join units that support each other (a predicate pair and its argument pairs). Inhibitory links join units that compete (the same element mapped to two things). Similarity and pragmatic inputs add activation.
- Fixed parameters in all reported runs: decay .1, excitation .1, inhibition -.2 (a01). Settling usually under 100 cycles, never over 220.
- Robustness (a02): decay .001 to .2 worked equally; excitation .01 to .12 worked, above .12 unstable; inhibition up to -.9 worked but high inhibition can lock in an early wrong mapping; pragmatic weight best near .3. ACME never lost a correct mapping to a later-rising wrong one.
- Ablation (a03): deleting every third source or every second target proposition mostly kept the right mappings. One failure: deleting the predicate "filament" left the tumor with no positive mapping.
- Design claim: ACME can find an isomorphism with no meaning overlap (a09: attribute mapping settled by cycle 71, goodness .61).
- Inputs were small. The laser/fragile-glass network had 192 units and 1,773 links and settled at cycle 31 (b01). Units grow with the product of the two analog sizes (a01).

### 2.3 LISA (1997, 2003)
- Distributed meaning codes plus synchrony binding. Propositions fire one after another; active roles and fillers fire out of phase, so binding is "same phase". Mapping connections are learned only while both analogs are in working memory (a10).
- Capacity: a phase set of about 4 to 6 out-of-phase groups (a10, b04). This is the main design difference from ACME, which holds all local matches at once.
- Hummel and Holyoak list four doubts about earlier models (b09): no working-memory limit; no joint account of access and mapping; mapping that is both too powerful and too restricted; no schema learning. Their Table 1 lists 14 phenomena to explain.
- Retrieval (b08): a Weber fraction of summed activation so short and long analogs compete fairly, then Luce choice competition. Wharton et al. (1991) found human retrieval fits Luce.
- Inference and schemas (b07, 2003): an inference is made only if at least 70% of the importance-weighted structure is mapped. At most three propositions fit in working memory.

### 2.4 Copycat
- Four parts: a hand-built concept network (Slipnet), a workspace, many small perceptual agents (codelets), and a temperature (a18, c27). Temperature is high early (random, parallel, bottom-up) and falls as a coherent answer forms (more deterministic, serial, top-down).
- Conceptual slippage is the abstraction mechanism: letter to group, successor to predecessor.
- Central disagreement with SME and ACME (a19): Copycat builds the representation inside the mapping loop. SME-style systems get representations first. Holyoak and Thagard note that Copycat and SME constraints exclude pragmatics, while ACME includes them (a08).
- Limits per Mitchell 2021 (b21, c26): hand-built concept network, source and target are given (no retrieval), ad hoc parameter tuning, no learning of permanent new concepts, synthetic domains only (a26).

### 2.5 Learned relatives
- ESBN (Webb, Sinha, Cohen 2021; a27, c23): a network with external key-value memory. Keys are abstract variables, values are content. It generalised at 95% or better to new entities, even with as few as 2 entities in training. A learned cousin of LISA binding.
- Abstractors / relational bottleneck (Altabaa et al. 2024; Webb et al. 2024; c24, c25): force a module to carry only relations, not object features. Better sample efficiency on relational tasks. Exact numbers only in figures.

## 3. Core findings with exact numbers

Status: E = two or more independent sources; S = single source; C = contested; D = dated (older models). Garbled-table warnings are in section 5.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ACME settles the convergence-problem mappings in all four lightbulb/radiation versions; cycles barely depend on surface similarity | d=.1, e=.1, i=-.2; under 100 cycles typical, max 220 | a01, a04, b01 | S |
| ACME fails on cross-mapped, non-systematic stories with default inhibition | Table 15: systematic 3 / 4 / 38 cycles (same-object / dissimilar / cross-mapped); non-systematic 3 / 4 / no success; retune inhibition to -.1 or min -.3 to succeed | a05, b02, d18 | S |
| ACME is too powerful: solves the unnatural boys-dogs mapping that people solve only slowly | 6 of 8 students correct in 3 min (b03/b05); a06 reports 5 all-six + 2 four-of-six + 1 unable. Counting differs | a06, a16, b03, b05 | E (direction); counts unresolved |
| LISA phase set about 4 to 6 role bindings; boys-dogs fails unless about 10 role bindings are in the set | Fails with 1 proposition and with 5 propositions of one analog; succeeds only with 10 | a10, a14, b04 | S |
| Access and mapping dissociate (Ross 1989) | Access human/LISA: .22/.58, .04/.17, .01/.09, -.22/-1.3. Mapping human/LISA: .19/1.98, .14/1.82, .11/.94, .16/.94. Signs match, sizes up to 10x too big | b06, a11 | S |
| LISA retrieval ordering matches humans | Luce index .43 close analog, .34 schema, .23 far analog; mapping 7/7 close and schema, 6/7 far | a12 | S |
| Pragmatic goal changes mapping | Humans: economic goal 43% vs 35%; military goal 29% vs 65%. LISA activation difference .58 (Econ-hi) vs .04 neutral | a13, a17 | E (2 sources) |
| Inference gate: 70% importance-weighted coverage | Lassaline sim, 50 runs per condition: medium constraint both inferences 15, weak-only 11, partial 13, none 11 | b07 | S |
| GPT-3 matches or beats students on text digit matrices | N=40. Generative OR 1.88, p=.005, CI [1.21, 2.91]; multiple choice OR 6.27, p=2.3e-8, CI [3.28, 11.99] | a20, b10, c01 | E |
| GPT-3 on letter strings | N=57. Overall OR 1.76, p=6.3e-5, CI [1.34, 2.31]. Zero-generalisation subset separately OR 1.76, p=.0007 | a20, c01 | E |
| GPT-3 below humans on story analogies | N=54. OR 0.37, p=.0003. Near: GPT-3 p=.0039. Far: GPT-3 p=.065 (n.s.); humans t(53)=16.7. GPT-4 spot test far better | a21, c03 | E |
| GPT-3 difficulty profile resembles humans but is steeper | Per-item r(30)=0.39, p=.027. Spatial permutation: humans OR 0.52; GPT-3 OR 0.06 | c02 | S |
| Counterfactual alphabets break GPT-3 | Generative accuracy under 0.1 on extend, successor/predecessor, fix-alphabet; only remove-redundant and sort (2 of 6 types) held | a22, b12, c05, c30 | E |
| Larger counterfactual test | Pooled accuracy humans .753 [.734,.773] (1,876 samples, 136 people); GPT-3 .488, GPT-3.5 .350, GPT-4 .452 (6,840 each). Row labels ambiguous in PDF text | a23, b13, c07 | E (order inferred) |
| Error types differ | Incorrect rule: GPT-3 30.97%, GPT-4 32.67%, humans 14.67%. Alternative-rule errors: GPT-4 22%, GPT-3 5.81%, humans 38.59% (row label lost in one extraction) | c08, d03, b13 | S |
| Code tool rescues permuted alphabets | Humans vs GPT-4 no code P=8.9e-13; vs GPT-4 + code P=.496. Humans N=99 and 97 | b16, c10, c11 | C |
| Far-transfer letter strings: humans stable, LLMs fall | Adults .88/.91/.89 (N=62), children .62/.66/.67 (N=41); GPT-4o .85/.63/.48; Claude-3.5 .68/.62/.46; Llama-405B .79/.74/.27; Gemma-27B .60/.39/.14 (Latin/Greek/Symbol) | a24, b17, c12 | S |
| GPT-4 story analogy relies partly on shortcuts | 86% to 72% when correct target's sentence overlap removed (humans 78% to 70%). Answer order: 89% (16/18) when Story A correct vs 61% (11/18) when Story B correct | b15, d03 | E |
| Re-representation tasks: LLMs match humans by default, brittle otherwise | Humans N=194. Claude 3 permuted-pairs coef -1.78; numeric condition GPT-4 and Llama-405B about 0.35 vs humans and Claude 3 about 0.7 | a25, c14-c16 | S |
| ConceptARC, GPT-4 (2023) | Humans 91% (83-97% per group); GPT-4 25% zero-shot, 33% one-shot; Kaggle first place 52% | b18, b19, c28 | E, D |
| ConceptARC, reasoning models (2025) | Human pass@1 73%; o3 77.1% (medium, no tools), 75.6% with tools; o4-mini 77.7%; Gemini 2.5 Pro 66.0%; Claude Sonnet 4 60.2% (72.5% re-scored); GPT-4o 14.6%. About 27% of o3 and Gemini correct outputs use unintended rules vs about 7% for humans | d01, d02 | S |
| Effort helps text, tools do not | o3 text: low 68.3%, medium 77.1%, low+tools 67.9%, medium+tools 75.6%. Visual: low 6.5%, medium 5.6%, low+tools 18.2%, medium+tools 29.2% | d02 | S |
| Far analogy (ARCANA, 200 tasks) | Human pass@1 68.96% (58.35% strict). GPT 5.2 pass@3 51.20%; Gemini 3 Pro 43.06%; Grok 4.1 Fast 24.88%; Claude Opus 4.5 8.61%. Best model 10.13 points below humans strict; Opus 4.5 51.63 below | d05 | S |
| Copycat-style LLM loop | 9 of 17 hard ARCANA tasks, 2.22 loops on average, no control arm | d06 | S |
| Retrieval vs application in GPT-4 | With hint: recall 1.00, precision 0.52 and 0.50. Humans: precision .67/.75, recall .26/.39. No hint: AI 0 | d08 | S |
| Self-generated analogs | About +4% average (Yasunaga). Qin: GSM8K+MATH relevant 52.4 vs none 55.8 vs random same-domain 55.7; BBH relevant 63.2 vs none 61.9. Example accuracy on MATH: relevant 62%, none 72%, random-same 86% | b23, c19, d09, d10 | C |
| Fixed verified examples beat per-query self-generated | ICLmath 75.7 GSM8K / 36.8 MATH (avg 56.3); ICLbio 77.9 / 34.9 (avg 56.4) | d10 | S |
| Thought Propagation | Shortest path: TP .65 optimal, ToT .22, IO .33 (backend unconfirmed). Creative writing coherence GPT-4: IO 6.193, CoT 6.927, ToT 7.684, TP 7.989 | c21, c22 | S |
| Long CoT does not fix binding load | o3-mini 86.6% to 17.0% on I-RAVEN-X; R1 80.6% to 23.2%; high effort lifts o3-mini only to 31.0% at 53,596 reasoning tokens. Llama-3.1 70B letter strings 0.35 / 0.10 / 0.05 / 0.00 / 0.00 for 0 / 2 / 5 / 10 / 20 permuted letters | d14, d15 | E |
| Small transformers need copy tasks | 93.9% on new alphabets with seen transformations; 12.3 to 13.1% on new transformations; matching heads in 100% of runs with copy tasks vs about 25% without | d04 | S |
| Where it fails inside open LLMs | Patching fixed up to 38.4% of failed proportional cases; relation info sits in mid-upper layers; abstract "next" concept vector similarity 0.16 vs 0.75 for verbal concepts | d13, d14 | S |
| Embeddings alone reach 78% on 18 Gentner stories | Humans .847, GPT-3 .75, Llama-70B .8538, GPT-4o .8233; item-level r with humans only .526 for GPT-4o-mini; embedding margin r=-.032 | b26, d12 | S |
| Story-analogy identification among many stories | ChatGPT about 30% vs humans over 85% | d16 | S |

## 4. Mechanisms and models

### 4.1 ACME as an algorithm
Inputs: two sets of propositions, each `pred(arg1, arg2, ...)`. Optional meaning-similarity table and a list of goal-relevant elements.

1. For every pair of same-arity predicates (one from each analog) make a unit. For each argument slot make units for the object pairs. Only type-compatible pairs get units.
2. Excitatory links (weight e): predicate-pair unit <-> its argument-pair units. This makes the structure mutually supporting.
3. Inhibitory links (weight i, negative): between any two units that map the same source element to different targets, or the same target from different sources. This is soft one-to-one.
4. Meaning input: a special unit with fixed activation links to each unit, weight proportional to similarity of the pair.
5. Pragmatic input: another special unit links to units that involve goal-relevant elements (weight about .3 was best, a02).
6. Update each cycle with decay d: `a <- a(1-d) + net*(max-a)` if net > 0, else `a(1-d) + net*(a-min)`. Repeat until activation change is under a threshold. For each source element read the unit with the highest final activation. Report "goodness".
7. Cost: units grow with the product of the two sizes. Inputs must first be written as clean propositions.

Failure modes to design against: cross-mapped objects (similar objects in different roles) needed retuned inhibition (b02); high inhibition can block recovery from an early wrong mapping (a02); one missing predicate can erase a mapping (a03).

### 4.2 LISA as an algorithm
1. Driver and recipient analogs, each a set of propositions. Each proposition has role units (predicate-object pairs) with distributed meaning codes.
2. Select one proposition (or a few) in the driver to fire. Active role and filler units fire out of phase, so binding is "same phase".
3. Activation spreads through shared meaning units into the recipient (or into long-term memory for retrieval). Recipient role units with matching meaning respond in the matching phase.
4. Mapping connections grow between co-active driver and recipient units (Hebbian) and are limited by global inhibition, so each driver unit ends with one preferred match.
5. Retrieval = Weber fraction of summed activation then Luce competition (b08).
6. Inference: if at least 70% of importance-weighted driver structure is mapped (b07), unmapped driver propositions are copied into the recipient with mapped substitutions.
7. Key knob: the size of the phase set (4 to 6 bindings). The goal enters by firing goal-relevant propositions first and more often (a13).

### 4.3 Copycat loop
- Workspace holds the strings and the structures built so far (groups, bonds, correspondences).
- Codelets propose structures. Their chance of success depends on Slipnet activation and on temperature.
- Temperature = how coherent the current structure set is. High: try anything. Low: commit to what is built.
- Slippage: when two things do not match, allow a neighbouring concept in the Slipnet (successor to predecessor).
- ConceptSIR (d06) is the only LLM version found: propose concepts, slip concepts, introspect on a prediction error, execute as code, reflect, loop up to 5 times.

### 4.4 Learned analogues
- ESBN: write (key, value) pairs to memory; read by key similarity; the controller sees the similarity pattern, not the value content. This forces rules that apply to any entity.
- Abstractor: cross-attention where queries and keys come from object features but values are learned symbols, so the output carries relations only.
- Small transformers (d04): matching heads between example input and output positions are the learned core. They appear only with copy tasks in training.

### 4.5 Shared design core (usable in a scaffold)
1. Candidate correspondences are explicit objects with scores.
2. Scores combine structure, meaning and goal.
3. One-to-one is a soft constraint applied by competition.
4. Mapping happens in small serial chunks (LISA) or all at once (ACME); the human evidence favours chunks.
5. Retrieval and mapping are different steps with different cues.
6. Inference needs coverage of the mapped structure first.
7. Re-description can happen during mapping (Copycat; human re-representation on boys-dogs).

## 5. What holds up

### 5.1 Model papers
- Only the authors' own simulations back ACME and LISA. All inputs are hand-built, tens of units; no variance across runs in the parts read. The 1997 runs were on a 486 PC. No open-domain text test exists (critique).
- LISA reproduces signs, not sizes. Ross mapping: LISA 1.98 vs human .19. Last access contrast: -1.3 vs -.22. "LISA explains" is qualitative.
- Copycat evidence is entirely qualitative, with no human comparison data (b21, a26).
- The boys-dogs result is not clean. a06 reports 5 of 8 all-six-correct, 2 four-of-six, 1 failed. Secondhand sources say 6 of 8 within 3 minutes (b03/b05). Direction is stable: people can solve it, slowly, by re-representing.
- Holyoak and Thagard 1989 Tables 4 and 5 were garbled in extraction. Do not quote the 69/33/13 human convergence percentages or per-condition cycles for the lightbulb versions without checking print. Table 15 was re-read cleanly (d18): 3 / 4 / 38 and 3 / 4 / none.

### 5.2 LLM replications and failures
- **Original claim** (Webb et al. 2023): GPT-3 matches students. Digit matrices OR 1.88 and 6.27; letter strings OR 1.76.
- **Failure to generalise** (Hodel and West; Lewis and Mitchell 2024): counterfactual alphabets drop GPT-3 below 0.1 on lookup-dependent types. Pooled: humans .753 vs GPT-3 .488, GPT-3.5 .350, GPT-4 .452. GPT models were also below humans on the original problems. Prompt wording was not the cause (c09).
- **Reply** (Webb et al. 2024/2025): the failure is index counting; GPT-4 with code matched humans (P=.496). The same pattern held on two alphabets and two engines, so they argue it is not memorisation. Still contested: it shows one missing skill, not that abstraction is present. Single group.
- **Cross-development test** (Stevenson et al.): humans flat across alphabets, every LLM falls, worst in the symbol alphabet. Models passed a next/previous diagnostic, so they knew the letters.
- **Shortcuts:** GPT-4 story analogy loses 14 points on paraphrase (humans 8). Strong answer-order bias (89% vs 61%). Sentence embeddings alone get 78% (humans .847). Part of the "emergent" story result is surface overlap.
- **Item-level mismatch:** difficulty profiles correlate weakly with humans (r = .526 at best, d12). Webb's GPT-3 had r(30)=.39.
- **Reasoning models (2025-26):** match humans on text ConceptARC, but with unintended rules in about 27% of correct outputs (humans 7%). Tools do not raise text accuracy; effort does. Far analogy (ARCANA) is still 10 to 52 points below humans. Raven-like tasks collapse under load. No counterfactual letter-string test of o-series or Claude 4+ was found (open).
- **Prompt methods:** analogical prompting is contested. Qin et al. found relevance does not help on math; accuracy of the examples does. Verified fixed examples were cheaper and as good. Thought Propagation is one paper. MetaLadder needs fine-tuning.

### 5.3 Moderators and boundary conditions
- Format familiarity and token lookup. Lookup-free items hold; lookup-dependent items fail.
- Surface overlap and answer position in forced-choice analogy.
- Number of simultaneous bindings (I-RAVEN-X, permuted letters).
- Distance of transfer (Latin, Greek, symbol; near vs far stories; ARCANA).
- Model size: small models make poor self-generated exemplars (c20). Larger models about 15 points better on stories (b26).
- Tool access: helps index counting (contested), not text ConceptARC.
- Interventions that worked: code execution on index tasks (C); reasoning effort on text ConceptARC; verified fixed exemplars on math; explain-first prompts up to 0.915 on 18 stories (d12; column assignment uncertain); copy tasks in small-model training.
- Interventions that did not: tools on text ConceptARC; relevance-based self-generated analogs on math; longer chain of thought under rising load; a one-shot prompt on GPT-4 ConceptARC (33% vs humans 91%).

## 6. Language models

**How they behave.** Early GPT-3 looked human on easy, familiar-format analogies. When the surface changes but the relation does not, accuracy drops, and humans do not drop. This is stable across Hodel and West, Lewis and Mitchell, Stevenson et al. and Musker et al. Mechanistic work in open 7B to 70B models agrees: relation information is present when answers are right; failures split between missing the relation and failing to apply it (d13); abstract concepts like "next letter" have no invariant vector (d14).

**What changed it, by how much.**
- Model generation: pooled counterfactual accuracy GPT-3 .488, GPT-3.5 .350, GPT-4 .452. No clear gain. GPT-4o .85 / .63 / .48 across alphabets.
- Code execution: from far below humans (P=8.9e-13) to indistinguishable (P=.496) on permuted-alphabet letter strings. One group's result.
- Reasoning effort: o3 text ConceptARC 68.3% (low) to 77.1% (medium). GPT-4 was 25% in 2023, so the 2023 to 2025 jump is about 50 points.
- Scoring the rule, not only the answer: about 27% of correct outputs use the wrong rule.
- Binding load removes the gain: o3-mini 86.6% to 17.0%; 3.4x more tokens does not fix it.
- Far analogy: the strongest 2025-26 model is still 10.13 points below humans (strict); the weakest tested is 51.63 below.
- Prompting: analogical prompting about +4% on average (Codeforces GPT-4 Acc@1 16% to 17-19%, so 1 to 3 points), not stable across models and tasks.

**Do LLMs implement ACME/LISA?** Webb et al. argue attention supplies pairwise similarity and key/value indirection supplies binding (b11, c04). No ablation tests this (contested). Musker et al. say success raises the burden of proof for models with built-in structure, but variation across task versions points to different mechanisms (c18).

**Hybrids using these ideas.** ConceptSIR is the one Copycat-inspired LLM loop (9 of 17, no control). Abstractors and ESBN are trained, not prompted. Puranam et al. show retrieval and application split in GPT-4 (d08).

## 7. What our agent should take

The mapping step sits at O7 (map an analogue) and O6 (change representation). Retrieval sits in memory and S3 grounding. Checks sit in G3, G5, G10.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Never accept a base-form analogy pass as proof of abstraction. Require a variant check (permuted symbols, swapped names, paraphrase) before accepting a mapping. | G3 | [E] | K11, K13, K14; a22, a23, c07, b15 |
| A2 | Randomise answer order and require the answer to survive an order swap on forced-choice analogy items. | S1 input hygiene | [E] | K14; b15, d03, d12 |
| A3 | Do index counting, letter positions and heavy rule application in code. Cap the number of bindings handled per model step. | G11, tools | [E] for load collapse; [C] for the code rescue | K26, K12; d14, d15, b16 |
| A4 | When a pass is claimed, log the stated rule next to the answer where a check exists. | G10, S8 | [S], cheap hygiene | K22; d01 |
| A5 | State the goal before mapping; let it decide which correspondences matter. | S0, O7 | [E] (2 sources) | K07; a13, a17 |
| A6 | Do not let the model judge "is this a good analogy" from surface fit. Check structure in code where possible. | G5 | [E] | K14, K25; d08, d12 |
| A7 | Treat an unnatural isomorphism as a re-representation task, not an exhaustive match. Budget serial steps for it. | O6 | [E] direction | K03; a06, a16, b03, b05 |

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Explicit scored mapping step: list candidate correspondences, score on structure / meaning / goal, enforce one-to-one, then answer. | O7 | [S] | K01, K02; a01, b02 |
| T2 | Chunked serial mapping with a cap of about 4 to 6 bindings per step. | G budget, O7 | [S] | K04, K26; a14, d15 |
| T3 | Keep retrieval of an analog apart from mapping; add a structure check before transfer. | memory, O7 | [S] | K05, K06, K25; a11, b06, d08 |
| T4 | Coverage gate on analogical inference: accept an inferred claim only if at least 70% of importance-weighted source structure is mapped. | O7, S8 | [S] | K08; b07 |
| T5 | Re-describe while mapping (Copycat) vs map from a fixed description. | O6, O7 | [S] | K09, K24; a18, a19, d06 |
| T6 | Anonymise object names (relational bottleneck) before mapping. | S1, O6 | [S], indirect | K19, K28; c24, d14 |
| T7 | Self-generated analogs vs verified fixed exemplars. | O7, O2 | [C] | K17, K18; d09, d10 |
| T8 | Code tool for index and counting steps on counterfactual items. | tools | [C] | K12; b16, c10 |
| T9 | State the input-output correspondence of the examples (what maps to what) before applying the rule. | S2 | [S] | K27; d04 |
| T10 | Split "state the relation in words" from "apply it to the target". | S2, S3 | [S] | K28; d13 |

## 8. Concrete tests on our bench

All arms at equal total tokens, with setup counted (G7). Report item-level results, not only means (K21).

1. **Variant invariance (A1).** Items: letter strings, text ConceptARC-style grids, digit matrices. Arms: plain model scored on 4 variants (base, permuted alphabet at 5 letters, symbol alphabet, paraphrase). Metric: accuracy drop from base to far variant, and answer agreement across variants. Expected: a base-to-far drop of 10 to 40 points for current models; this drop is what the scaffold tries to shrink.
2. **Order and paraphrase invariance (A2).** Items: the 18 Gentner stories and a larger story set. Arms: plain vs order-swapped agreement. Metric: accuracy by correct-position and invariance rate. Expected: removes an 89%-vs-61% type position gap.
3. **Scored mapping step (T1).** Items: cross-mapped relational items (similar objects in different roles), digit matrices, far stories. Arms: free CoT vs explicit candidate table with structure/meaning/goal scores and one-to-one check. Metric: accuracy on cross-mapped items and rate of surface-object errors. Expected: gain on cross-mapped items, none on easy ones; token cost visible.
4. **Chunked mapping (T2).** Items: generated mappings with 3, 6, 10, 15 correspondences. Arms: single pass vs chunks of 4 vs chunks of 6. Metric: accuracy by number of correspondences. Expected: single pass falls with load; chunks flatten the curve above 6.
5. **Retrieval vs mapping split (T3).** Items: memory with near and far analogs plus surface distractors. Arms: retrieve-and-use vs retrieve, structure-check, then use. Metric: precision and recall of the used source; final accuracy. Expected: precision up from about 0.5.
6. **Coverage gate (T4).** Items: analogy-based inference questions where the target lacks a supporting relation. Arms: no gate vs gate at 70% vs gate at 50%. Metric: unsupported-inference rate and true-inference recall. Expected: fewer unsupported inferences at a small recall cost.
7. **Re-describe on error (T5).** Items: ConceptARC and ARCANA-like tasks with a failing first description. Arms: fixed description with N resamples vs re-describe after a failing check. Metric: solve rate and share solved only after re-description. Expected: gain where the first description is wrong; none elsewhere.
8. **Anonymisation (T6).** Items: relational tasks with misleading object meanings. Arms: original vs neutral tokens in the mapping step. Metric: accuracy on cross-mapped items. Expected: gain only when surface meaning misleads.
9. **Analog source (T7).** Items: GSM8K-style and BBH subsets. Arms: plain CoT vs self-generated analogs vs verified fixed examples vs self-consistency. Metric: accuracy per token. Expected: verified fixed set at least as good and cheaper; self-generated no better than self-consistency.
10. **Code for index steps (T8).** Items: counterfactual letter strings at intervals 1 and 2. Arms: no tool vs tool for index lookup. Metric: accuracy vs human reference. Expected: large gain on lookup-dependent items, none on lookup-free.
11. **Rule scoring (A4).** Items: ConceptARC subset. Arms: answer only vs answer plus stated rule. Metric: share of correct answers with an unintended rule. Expected: 15 to 30% on strong models, from d01.

## 9. What does not transfer, and why

- **Synchrony binding, activation settling, Hebbian mapping weights.** These are network mechanics. A language model has no phase set, and its capacity is not 4 to 6 slots. We keep the binding cap only as a test, not as a fact.
- **ACME's exact parameters and cycle counts.** They belong to hand-built networks. Cycles are not tokens.
- **LISA's human effect sizes.** The model is off by up to 10x, so they are not targets.
- **Copycat's Slipnet and temperature.** The concept net is hand-built and domain-specific. Only the principle (re-describe while mapping) can be tried.
- **ESBN, Abstractors, small-transformer copy-task training.** They need training; our agent is a scaffold (K19, K27).
- **MetaLadder and fine-tuned analog training** (d11). Training, not scaffold.
- **Mechanistic claims** (attention equals ACME; patching results). Open models of 7B to 70B only; no scaffold lever.
- **Analogical prompting as "analogy".** It only borrows the word; it is not a mapping model.
- **Classic human-only data** (Ross, Wharton, Lassaline, Spellman and Holyoak). College-student word problems; they inform design, not LLM behaviour.

## 10. Open questions

1. Do 2025-26 reasoning models pass counterfactual letter strings and far-transfer variants, and does the pass come from abstraction or from tool use? No study found.
2. Does an explicit ACME-style scored mapping step beat free CoT at equal tokens? Only a confounded ARCANA correlation exists.
3. Does serial chunked mapping help LLMs on many-correspondence problems? Only indirect support.
4. Does separating retrieval from mapping cut surface-driven negative transfer in a memory agent? One GPT-4 study.
5. Is interleaved re-description better than a fixed description? ConceptSIR has no control arm.
6. Can an importance-weighted coverage gate cut unsupported analogical inferences? Nothing found.
7. Does prompt-level anonymisation of entities help? Indirect only.
8. What do Holyoak and Thagard 1989 Tables 4 and 5 report? Needs the print.
9. Which boys-dogs count is right (5 + 2 + 1, or 6 of 8)?
10. Is the Lewis and Mitchell Table 2 row order right (GPT-4 below GPT-3 pooled)? Check the figure.
11. How big is the surface-overlap shortcut on other analogy benchmarks? Cheap tests exist (swap, paraphrase, permute).
12. Are letter-string failures missing abstraction or missing index skill? Webb et al. vs Hodel and West / Lewis and Mitchell is unresolved.

## 11. Sources

[V] = opened and read this session. [M] = snippet or abstract only.

- [V] Holyoak and Thagard (1989) Analogical mapping by constraint satisfaction. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Holyoak_Thagard.1989.pdf (a01-a09, b01-b03, d18; Tables 4/5 garbled)
- [V] Hummel and Holyoak (1997) Distributed representations of structure (LISA). https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Hummel-Holyoak.1997.pdf (a10-a16, b04-b06, b08, b09; Ross numbers not re-opened)
- [V] Hummel and Holyoak (2003) A symbolic-connectionist theory of relational inference and generalization. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Hummel-Holyoak.2003.pdf (b07)
- [V] Holyoak and Thagard (1997) The analogical mind. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/HolyoakThagard.1997pdf.pdf (a17)
- [V] Mitchell (2021) Abstraction and analogy-making in artificial intelligence. https://arxiv.org/abs/2102.10717 (a18, a19, b21, b22, c26, c27)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a20, a21, b10, b11, c01-c04; re-opened in critique)
- [V] Hodel and West (2023/2024) Response: Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2308.16118 (a22, b12, c05, c06, c30)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955 (a23, b13, c07-c09; re-opened)
- [V] Webb, Holyoak, Lu (2025) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070 (b16, c10, c11)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2025) Can LLMs generalize analogy solving like children can? https://arxiv.org/abs/2411.02348 (a24, b17, c12, c13; re-opened, children not re-read)
- [V] Lewis and Mitchell (2025) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215 (b14, b15, d03)
- [V] Musker, Duchnowski, Millière, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (a25, a26, c14-c18)
- [V] Moskvichev, Odouard, Mitchell (2023) The ConceptARC benchmark. https://arxiv.org/abs/2305.07141 (b19, c28)
- [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4 and GPT-4V on abstraction and reasoning tasks. https://arxiv.org/abs/2311.09247 (b18)
- [V] Beger et al. (2026) Distinguishing performance gains from learning when solving analogy problems (ConceptARC, rules). https://arxiv.org/abs/2510.02125 (d01, d02)
- [V] Hellwig, Zuidema, Stevenson, Lewis (2026) Transformer See, Transformer Do. https://arxiv.org/abs/2604.06501 (d04)
- [V] Chen, Wang, Wang (2026) ARCANA. https://arxiv.org/abs/2610.29271 (d05-d07)
- [V] Puranam, Sen, Workiewicz (2025) Can LLMs help improve analogical reasoning for strategic decisions? https://arxiv.org/abs/2505.00603 (d08)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (b23, c19, c20; re-opened)
- [V] Qin, Xia, Wang et al. (2025) Relevant or Random. https://arxiv.org/abs/2404.12728 (d09, d10)
- [V] Lin, Pan, Li et al. (2025) MetaLadder. https://arxiv.org/abs/2503.14891 (d11)
- [V] Yu, He, Ying (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (c21, c22; table backend not confirmed)
- [V] Inani, Kabra, Marupudi, Varma (2025) Modeling understanding of story-based analogies. https://arxiv.org/abs/2507.10957 (b26, d12; table columns scrambled)
- [V] Lee, Song, Yoon, Park, Kang (2025) The Curious Case of Analogies. https://arxiv.org/abs/2511.20344 (d13)
- [V] Opielka, Rosenbusch, Stevenson (2025) Analogical reasoning inside LLMs. https://arxiv.org/abs/2503.03666 (d14)
- [V] Camposampiero et al. (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty? https://arxiv.org/abs/2503.11207 (d15)
- [V] Cheng Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (d16; abstract-level numbers)
- [V] Xiang, Ma, Cao, Zhu, Zhu (2026) Grounding Before Generalizing. https://arxiv.org/abs/2604.24062 (d17; indirect)
- [V] Webb, Sinha, Cohen (2021) Emergent symbols through binding in external memory. https://arxiv.org/abs/2012.14601 (a27, c23; line b25 was abstract only)
- [V] Altabaa, Webb, Cohen, Lafferty (2024) Abstractors and relational cross-attention. https://arxiv.org/abs/2304.00195 (c24; figures only, no exact accuracies)
- [M] Webb, Frankland et al. (2024) The relational bottleneck as an inductive bias. https://arxiv.org/abs/2309.06629 (b24, c25; abstract and introduction only)
- [M] Gendron, Bao, Witbrock, Dobbie (2023) LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 (b20; abstract only)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 3 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A11.05-K03** (reworded: the sources support less). Hummel & Holyoak 1997 call current models 'arguably' overpowerful and say the evidence is 'only suggestive' that people tend to re-represent; 'only via re-representation' is too strong; the sources are one lab (Holyoak) and the 6/8 and Keane figures are cited second-hand in Hummel & Holyoak 1997 (the 6/8 is not found in the Holyoak & Thagard 1989 text). Corrected claim: Hummel and Holyoak (1997) argue that ACME and SME can map analogies of any size with equal ease and so are arguably overpowerful; on the unnatural boys-dogs mapping people tend to re-represent the analogs (6 of 8 students solved it in 3 min per Holyoak and Thagard; about 3 to 6 min with error feedback in Keane et al. 1994), though the evidence is only suggestive.
- **A11.05-K07** (now single-source: the sources are not independent). Numbers (43% vs 35%, 29% vs 65%) match Hummel & Holyoak 1997, quoting Spellman & Holyoak 1996, but both listed sources are the Holyoak lab and the human data come from a single experiment; Holyoak & Thagard 1997 is a same-lab review with no new numbers.
- **A11.05-K14** (now single-source: the sources are not independent). Numbers match Lewis & Mitchell 2024 (GPT-4 .86 to .72 on 36 trials from 6 problems; humans .78 to .70; answer-order effect), but the only other source (Inani et al.) merely cites that work, so there is one source, and the paraphrase sample is small.
- **A11.05-K19** (reworded: the sources support less). The 95%-or-better with as few as 2 entities result is ESBN's alone (Webb, Sinha, Cohen 2021); Abstractors are reported as sample-efficiency gains, not that figure; all listed sources share authors (Webb, Cohen), so one research group. Corrected claim: Key/value binding in external memory (ESBN, Webb, Sinha and Cohen 2021) let networks generalise learned rules to novel entities at 95% or better on all four tasks, with as few as 2 entities on same/different; relational-bottleneck models such as Abstractors (same group) show better sample efficiency on relational tasks; this resembles LISA-style role binding by analogy (the note's gloss).
- **A11.05-K26** (reworded: the sources support less). All numbers match, but I-RAVEN-X raises rule length, value range and perceptual noise (not 'binding load'), the 3.4x token figure is o3-mini only (5445 to 18482), and the Llama-3.1 70B letter-string result is a non-reasoning model that says nothing about long chain of thought. Corrected claim: Reasoning models do not stay robust on analogy as task size and perceptual uncertainty grow: o3-mini falls 86.6% to 17.0% and R1 80.6% to 23.2% on I-RAVEN-X, o3-mini despite about 3.4x more reasoning tokens (and only 31.0% at high effort); separately, non-reasoning Llama-3.1 70B letter-string accuracy falls 0.35 to 0.00 as the alphabet is permuted.
- **A11.05-K10** (now single-source: only one opened source, code check).
