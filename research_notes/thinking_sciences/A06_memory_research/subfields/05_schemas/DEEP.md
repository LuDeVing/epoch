# Schemas: deep document

*Subfield A06.05. Written from evidence_a-d.jsonl (a01-a35, b01-b33, c01-c25, d01-d17), claims.jsonl (K01-K29) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. A source is [V] only if its page or PDF text was read; many founding papers were not (section 11). Where a number was not read, this document gives none.*

## 1. What it is

A schema is a structured bundle of prior knowledge about a kind of situation. It has a fixed frame and slots that take values. Empty slots are filled with defaults. In human memory it does five jobs (Brewer and Nakamura 1984, a14): it directs attention, gives a framework that holds episodic detail, combines generic and episodic information into one instantiated memory, aids retrieval, and edits output.

Four things matter for our agent.

1. **Reconstructive recall.** Remembering rebuilds the past from a few kept traces plus the schema. It does not play back a stored record. Output can contain things never seen.
2. **Gap filling.** When the input is silent, the schema supplies the typical value. The person (or model) cannot tell supplied from observed.
3. **Persistence.** A schema that has worked is hard to revise. Minsky: old assumptions, once acquired, are persistent (a09).
4. **Fixation.** The pull that makes recall efficient also makes the agent repeat the typical answer and miss the atypical fact.

For a language-model agent a schema lives in three places: the weights (default world knowledge), the prompt (task templates, lessons), and the memory store (summaries, rules, workflows). Section 6 shows all three produce schema effects. The memory store is where we have control.

The word is loose. Ghosh and Gilboa (2014, b30, abstract only) require four features for a "memory schema": an associative network, a basis in multiple episodes, lack of unit detail, adaptability. Much neuroscience uses the word without them. Alba and Hasher (1983, not opened) argued that "is memory schematic?" bundles five claims of unequal strength. So we test each schema process separately and never build "one schema module" (K19, [C]).

## 2. History and theories in depth

### 2.1 Head to Bartlett (1920-1932)
Bartlett took "schema" from the neurologist Head (1920), who used it for a postural model. Bartlett said he disliked the word. He objected to the cortex as storehouse, to traces "rising into consciousness", and to the term being "too definite and too sketchy". He defined it as "an active organisation of past reactions, or of past experiences" and suggested "organised setting" as better [a01, V, archive.org copy of the 1995 reprint]. The word later hardened into a fixed-structure idea he did not intend.

Method of repeated reproduction: read a story, reproduce it after about 15 minutes, again at longer intervals. Instructions were informal and no statistics were reported. Bartlett warned that frequent reproduction makes a form stereotyped fast [a02].

The War of the Ghosts: a Native American folk tale of about 330 words, adapted from a translation (Boas). Events had no obvious link and the ending was supernatural. The series in the chapter used 20 subjects (7 women, 13 men) [a03]. Changes seen: omission, rationalisation of odd parts, loss of proper names and numbers, transformation of the title, and a prepotent theme that organises the rest. Title omitted by 7 of 20; 10 of the others transformed it [a04]. The "no arrows" excuse was omitted by half; of the 10 who kept it, 6 were women, which Bartlett read as a possible affective effect (confounded with sex and war exposure) [a06]. One subject turned "ghosts" into a clan name, was satisfied, and the error and his confidence grew with each recall [a05, N=1].

Theory: the organism "can turn round upon its own schemata" and infer what must have occurred. Remembering is a constructive justification of an attitude toward a mass of past reactions [a07]. Literal recall is rare. Remembering is rebuilt each time, like a skilled stroke in a game [a08].

Brewer and Nakamura (1984) note that Bartlett wrote two theories: an official pure-reconstructive one and an unofficial one that keeps some specific traces. The pure version cannot explain recall of unique episodic details (that the typewriter was an Underwood) [a14, V]. This is the key correction: **schemas plus traces, not schemas instead of traces.**

### 2.2 Piaget (1952)
Piaget gave the first developmental theory of schemas: assimilation (fit input to the schema) and accommodation (change the schema). Only the lineage was read (Wikipedia, a18). Piaget matters here by name, not by evidence in this folder.

### 2.3 Frames, scripts, schemata (1974-1980)
Minsky (1974, a09, V): a frame is a data structure for a stereotyped situation. Top levels are fixed. Terminals (slots) take values and come with default assignments attached loosely so new items can displace them. A failed match calls a replacement frame from a retrieval network. Frames share terminals across viewpoints. Minsky warns frames can impose stereotypes and jump to conclusions. The earliest frames become the centres of later ones, because each success adds a pointer to them [a10]. Design proposal, no experiments.

Rumelhart and Norman (1978) and Rumelhart (1980) [a19, M, not opened]: schemata are data structures with variables, embedded in each other, that act like procedures to interpret input. Three learning modes: accretion (add facts), tuning (adjust a schema), restructuring (create a new one). This maps cleanly onto an agent note store (section 4).

Schank and Abelson scripts follow Minsky (lineage only, a18).

### 2.4 Schema theory in reading research (1977-1984)
Anderson and Pichert (1977) tested whether a schema acts at encoding or at retrieval. Pichert and Anderson (1977) showed the importance of story elements depends on the reader's perspective. Brewer and Nakamura reviewed the 1970s-80s work, split schema function into five processes, and re-analysed several studies by subtractive logic, concluding some support mechanisms other than the ones claimed [a14, a16].

### 2.5 Critique and competing accounts
- **Alba and Hasher (1983)** [a20, b28, M]: five claimed processes (selection, abstraction, interpretation, integration, deterministic reconstruction); evidence for several is weak; people keep much specific detail. Not opened; thesis from citation memory.
- **Hintzman (1986)** [a26, M]: MINERVA 2 stores only episodic traces, no schema, yet shows prototype and schema-abstraction effects at retrieval. Schema behaviour without schema storage. Not opened.
- **DRM false memory** theories (activation-monitoring, fuzzy-trace, global matching): none explains all list-type results [a25, V review]. DRM uses associative word lists, not schemas.
- **Instruction accounts of Bartlett:** Gauld and Stephenson (1967) are cited as showing accuracy instructions reduce distortion [a22, b24, M, citation memory only].
- **Non-replication on other material:** Wynn and Logie (1998) found stable recall of real events over months [a23, b23, M, secondary report only]. Different material, so not a direct replication.

### 2.6 Modern formal models
- **Category Adjustment Model** (Huttenlocher 2000) and its Bayesian versions (Hemmer and Steyvers 2009, b33, M): recall is a weighted blend of a fine-grained trace and a category prior, weights set by relative uncertainty. Xu, Hemmer and Zhang (2023, b11, V) propose a generalised CAM that fits both older and newer data (typical items pulled more).
- **SLIMM** predicts a U-shape between expectancy and memory. A 2026 partial failed replication reproduced the U-shape but not the predicted brain interactions [b31, M abstract]. Nguyen, McRae and Zacks (2026, b15) contrast SLIMM with "schema copy plus tag".
- **Compressive RAG model of consolidation** (2026, b06, V): store a gist plus a few surprising details, rebuild with an LLM. Reproduces Bartlett-like intrusions.
- **Schema learning in transformers** (Swaminathan 2023, c14, V) and **schema-based hierarchical active inference** (Van de Maele 2026, c15, V): formal models, not testable by prompting alone (K20).
- **Neuroscience anchor:** Tse et al. (2007, a35, M): rats with a flavour-place schema learned new pairs in one trial and consolidated them in about 48 h. Not opened.

## 3. Core findings with exact numbers

Status: **ok** = two or more independent sources; **single** = one source; **contested** = sources disagree; **unread** = widely cited, numbers not read.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Schema is an "active organisation", not a store | Definition; Bartlett disliked the word | Bartlett 1932 [a01] | ok (historical) |
| War of the Ghosts: omission, rationalisation, transformation | 20 subjects (7 F, 13 M); title omitted by 7, transformed by 10 of the rest; arrows excuse omitted by half, 6 of 10 keepers women | Bartlett 1932 [a03, a04, a06] | contested: small N, no statistics |
| Bartlett replicated with controls | Delays 15 min, 1 week, 6 months; distorted share rises with delay; N and rates not read | Bergman and Roediger 1999 [d02, b22] | single, abstract only |
| Bartlett not replicated with real-event material | Stable recall over months; no numbers read | Wynn and Logie 1998 [b23] | contested, secondary only |
| Accuracy instructions cut distortion | Not verified | Gauld and Stephenson 1967 [b24] | unread |
| Office schema causes false recall (books) | Direction confirmed by secondary pages; N conflicts (86 vs 30); no rates | Brewer and Treyens 1981 [a15-a17, b25, d01] | unread; no numbers may be cited |
| Perspective shift recalls previously unrecalled info | Exp 1 N=39: shifters +7.1% new-view info vs -2.9% no-shift, F(1,35)=9.57, p<.01; old-view loss -7.2% vs none, F(1,35)=2.22, n.s. Exp 2 N=16: +10% new (t(15)=3.02), -21% old (t(15)=5.36), no control | Anderson and Pichert 1977 [a11] | direction ok, small N |
| Importance is perspective-bound | 63 raters, split-half .91-.98, tau across perspectives about .11; Exp 2 N=113: importance F(2,202)=103.4, omega^2=.23 immediate; delayed (N=45, 47) F(2,160)=9.18, omega^2=.03; homebuyer subcase failed | Pichert and Anderson 1977 [a13] | single lab; medium effect immediate, small at delay |
| Congruent items learned faster, not remembered better item-wise | N=48. Learning 34.65/36 (SD 1.44) vs 28.21 (SD 6.86), Z=-5.74. d' congruent 1.31 vs incongruent 1.67; global 1.88 vs 2.31; detailed 0.74 vs 1.03 (Z=-4.58, -3.92) | Sweegers 2015 [b08] | contested vs a31, a33, b14 |
| Congruent associative memory better; item benefit needs consolidation | N=76 women, delays 0/20/48 h. Item d': delay x congruency F(2,66)=5.04. Associative: congruency F(1,66)=17.59, p<.001, no delay interaction | van Kesteren 2013 [a31] | single, one lab |
| Incongruent components remembered worse than congruent | One analysis 30 of 31 analysed; recognition and cued recall lower for incongruent despite more fixations | Frank 2018 [a33] | single |
| Incongruent sequences benefit only for content violations | 4 experiments, 193 students (Exp 4 N=42); powered for d=0.28 congruent, d=0.12 incongruent | Curtis 2026 [b14] | single, preprint |
| Meta-analysis: slight advantage for inconsistent info; direction set by measure | 60 studies, 165 tests; corrected recall/recognition favour inconsistent; uncorrected recognition favours consistent; pooled effect not read | Rojahn and Pettigrew 1992 [d03] | ok but old, person-memory only, abstract only |
| Gist rises with surprise; schema-consistent end gets no boost | 1a N=67, 1b N=46 at 24 h, 2 N=62; no slower forgetting for consistent at 24 h | Nguyen 2026 [b15] | single, preprint |
| Congruent location recall better at once, gone at delayed recognition | Exp 1 N=195; later N=183 (Czech) | Gustarova and Chromy 2026 [b16] | single, preprint |
| Schema clustering memory effect is fragile | Exp 1 N=63: t(124)=1.99, p=.049, d=0.35, BF01=0.87; Exp 2 N=75 (24 h): d=0.11, BF01=4.63. Generalisation to new words robust: d=0.76 and 0.54 | Cockcroft 2022 [b09, b10] | contested for memory; ok for generalisation |
| Typical items pulled to category centre; semantic beats visual cue | Seen in 3 of 4 experiments; vanishes with non-category layout; conceptual beats perceptual when competing | Tompary and Thompson-Schill 2021; 2025 preprint; g-CAM [b11-b13] | ok (3 sources) |
| Predicting an event creates a false memory of it | Exp 1a N=71: 0.153 (d=1.08) no feedback; 0.035 (d=0.52) after rebuttal; Exp 1b N=67: 0.221 vs 0.060; survives 24 h (N=66, 67); Exp 3 schema-consistent predictions larger, d=0.61 | Mubarak and Fukuda 2026; Mubarak 2026 [b17, b18] | single lab, preprints |
| Everyday event recall: false memory rate | N=229; 27.4% of recalled events false (22.4% conflicts, 7.7% confabulations); 48.6% recalled; centrality OR 1.12; corpus similarity OR 1.16 (conflicts); surprisal OR 1.16 (confabulations) | Verbal recalls preprint 2026 [b20, b21] | single, LLM-labelled (kappa .87 accurate vs not; .27 error type) |
| Single event recalled better than last of a repeated event | Registered report; independent of prior knowledge | 2025 registered report [b19] | single |
| LLM misleading questions raise human false memory | N=200; immediate false memories over 3x control, 1.7x survey; 36.4% of chatbot responses misled | Chan 2024 [d07] | single; harms people, not LLM memory |
| LLMs show human content effects in reasoning | Wason: z>2.2, p<.03 for Chinchilla, PaLM 2-L, GPT-3.5; people called believable invalid syllogism valid 90% (prior work) | Lampinen/Dasgupta [a27, c06] | one paper family, counted twice in evidence; independent 2 |
| Counterfactual versions of familiar tasks lower LLM accuracy | 11 tasks; GPT-3.5 parseable programs 99% default vs 62/71/75% flipped/rot90/rot180; CoT and 16 shots narrow, do not close | Wu 2023/24 [c01, c02, d08] | ok |
| Larger models can do worse when prior beats instruction | Memo Trap, Resisting Correction | McKenzie 2023 [c03] | ok, task-dependent |
| LLMs cling to memory under substitution evidence, accept coherent counter-evidence | GPT-4 memorisation ratio 80% on popular entities with mixed evidence; of 50 stubborn cases, 34 from ambiguous items | Xie 2024 [c04, c05] | ok |
| Stereotype gap filling in pronoun resolution | 4 LLMs, 60 sentences x 3 repeats; 6.8x (female), 3.4x (male); noted ambiguity 5%; same answer 90% | Kotek 2023 [c07, c08] | single |
| LLM chains keep stereotype-consistent, negative, social, threat content | 5 preregistered experiments; betas 0.058, 0.117, 0.183 (ambiguity resolved negatively), 0.321, 0.523 | Acerbi and Stubbersfield 2023 [b04, d04] | single model (ChatGPT-3), short chains |
| LLM chains drift to attractors | 6 models x 3 tasks x 100 chains x 50 steps; Continue > Take inspiration > Rephrase; toxicity strongest | Perez 2025 [b01-b03, d05] | ok |
| GPT-4 multimodal chains | N=348 humans, 10 steps; velocity t(198)=4.05 (humans), -7.01 as reported (GPT-4); GPT-4 above humans (6.97, 10.87) | Kumar 2024 [a28, c16, c25, d06] | one paper, counted once |
| Gist plus lookup matches full text at lower length | QuALITY 230 docs, 2086 Qs: gist compression 85.53%; ReadAgent-P 86.91%, -S 87.17%, full text 85.83%, MemWalker 66.73%; 3.5x-20x context | Lee 2024 [c09] | ok |
| Lossy summary worse than none | MultiWOZ: wrong-time emission 27% to 59% (8B), 0% to 49% (Opus); exact recovery 0.00; n=90 per cell | Kwon 2026 [c11, c12] | single, one author |
| Abstraction memory hurts | Anti-persistence best in 9 of 9 settings; abstraction below trajectory in 7 of 9; Reflexion 52.9% | Wang 2026 [a29] | single; settings not independent |
| Abstraction memory helps | AWM +24.6% Mind2Web, +51.1% WebArena; ExpeL ALFWorld 40.0 to 59.0, HotpotQA 28.0 to 39.0; Reflexion 130/134; BoT +11% Game of 24, +51% Checkmate-in-One; SA-ICL up to 36.19% (best case) | [c18-c21, a30] | contested vs a29; author-run |
| Stale memory | STALE best 55.2%, GPT-4o-mini 8.7%, LightMem 17.8%; 70.3% of prompts expose a superseded value without update resolution | Chao 2026; Deng 2026 [c13, d14] | ok (2 sources) |
| Provenance available is not provenance used | 16 models; inspected the path in about 20% of episodes; followed stale memory 74.7-77.3%; forced slot +61.3 to +81 points; PlanFence: freshness-only executor stale 30/30, PlanFence correct 30/30 | Nakayashiki 2026; Chen 2026 [d11, d15] | single each, preprints |
| Whole-context rewrite can collapse memory | 18,282 tokens, acc 66.7 to 122 tokens, 57.1; no-context 63.7 | ACE [d09] | one observed case |
| Wrong playbook entries harm only when constant | FiNER base 70.7; harmful every step 66.7; every 5 steps 76.1; none 78.3 | ACE A.4 [d10] | single |
| Wrong stored records are replayed and injected | Retained vs deleted correctness e.g. CIC-IoT 78.9 vs 56.7; MINJA injection 98.2%, attack 76.8% | Xiong 2025; Dong 2026 [d12, d13] | ok; MINJA adversarial |
| Generative agents embellish | 25 agents; candidacy knowledge 4% to 32%, party 4% to 52%; embellishments anecdotal | Park 2023 [c22] | single |

## 4. Mechanisms and models

Each is written so it can be coded. "Slot" means a field in a note.

### 4.1 Frame with slots and defaults (Minsky, Rumelhart) [a09, a19]
- Data: `frame = {name, fixed_conditions[], slots{name: {value, default, source: observed|default|inferred}}}`.
- Match: score input against the frame; below a threshold, retrieve a replacement frame.
- Fill: for each empty slot write the default and tag `source=default`.
- Lesson: **keep the source tag.** Human gap filling goes wrong because supplied and observed values look alike at recall. A program can keep the tag; a person cannot.
- Rumelhart's learning modes map to note edits: accretion = append a fact; tuning = edit a slot default; restructuring = replace the frame (rare, gated).

### 4.2 Reconstruction as blend of trace and prior (CAM, g-CAM) [b11, b33, b12]
- recalled = w * trace + (1 - w) * category_prior, with w = trace_precision / (trace_precision + prior_precision).
- Noisier traces (long delay, compressed summary) move recall toward the category centre. Typical items move more than atypical (b11, b12). The effect vanishes if items are not organised by category.
- Engineering reading: after summarising, an atypical number or name drifts toward a typical one. Check by diffing note values against source.

### 4.3 Schema as retrieval plan (Anderson and Pichert) [a11, a12]
- A perspective does not change what is stored. It changes what is searched. Recall of previously unrecalled facts rose after the shift.
- Implementation: keep the full source; at retrieval pass a perspective string and rank chunks by relevance to it. A perspective-free summary will lose perspective-relevant detail.

### 4.4 Serial reproduction as a Markov chain [b05, b01]
- Each rewrite samples from p(output | input, prior). Iterated, the chain converges toward the prior's stationary distribution (Meylan 2021, b05). Rate depends on how loose the instruction is: Continue > Take inspiration > Rephrase [b01]. Higher temperature raised attractor strength only in constrained tasks. Bigger or newer models pull less [b02].
- Implementation: any note rewritten by the model repeatedly is such a chain. Count rewrites per note and cap them.

### 4.5 Gist plus surprising detail (compressive RAG) [b06]
- Store gist + k surprising details; rebuild with an LLM from the parts plus background knowledge.
- Gist + 1 to 3 details balances tokens against cosine similarity to the original (500 ROC Stories). Intrusions match the topic the model was tuned on; more at higher temperature; some at greedy decoding. Consolidating the rebuilt story is worse than the encoded one.
- ReadAgent is the engineering sibling [c09]: paginate, write a gist per page, keep raw pages, look up pages when a question needs detail. Gist navigates; raw text answers.

### 4.6 Prediction-error memory (SLIMM and rivals) [b15, b14, b31]
- SLIMM: gist memory U-shaped in expectancy. Rival: copy schema-consistent content and tag the differences.
- Data: gist rose with surprise, no boost at the consistent end [b15]; incongruent benefit only for content violations, not order [b14]; brain predictions failed [b31].
- Reading: tagging violations at write time is cheap; the benefit shows for gist, not detail.

### 4.7 Abstraction-memory loop and error reproduction [a29, d10, d12]
- Loop: trajectory -> model writes rule -> rule injected into next trajectory -> that trajectory writes the next rule. A wrong rule shapes the trajectory that renews it.
- Wang et al. fix: anti-persistence (keep trajectories, rebuild guidance on demand, discard after use).
- ACE: incremental delta edits with non-LLM merging stop whole-context collapse [d09].
- Evaluator-gated addition plus history-based deletion beat unfiltered addition [d12].

### 4.8 Derivation links and forced checks [c12, d11, d15]
- Store each conclusion with links to its inputs and input versions. Before acting, verify the inputs are unchanged (PlanFence).
- Availability is not use: with 2 checks out of 6 records, models rarely opened the path. Code must put one check on the critical path.
- Source-first note: keep recomputable source, not only the derived value. Works while the source fits the budget; when truncated the model asserts a partial total, turning a detectable failure into an undetectable one [c12].

### 4.9 Rule-capture probe [c01, d08]
- Build pairs of the same problem under the default and a flipped convention, plus a comprehension check. An accuracy gap that survives comprehension is capture, not misreading.

## 5. What holds up

### 5.1 Replicated or multiply supported
- **Typical items pulled to category centre** (b11-b13): three sources.
- **LLM prior capture:** counterfactual tasks (c01-c03, d08), content effects (a27, c06), knowledge conflicts (c04, c05). Several independent papers.
- **LLM chains drift toward attractors** (b01-b03, a28, d05).
- **Stale memory** (c13, d14).
- **Perspective effect** (a11-a13): two reports from one group with small N (39, 16). Output editing and guessing were not fully excluded. Treat the direction as likely and the size as unknown.

### 5.2 Contested
- **Congruent vs incongruent advantage.** The 1992 meta-analysis finds a slight advantage for inconsistent items, direction set by test type (d03). Lab studies split: congruent better for associations (a31); incongruent better for item d' when the schema already solves the task (b08); congruent better than incongruent, yet incongruent sometimes better than baseline (a33); both better than unrelated, incongruent only for content violations (b14). Time matters: congruent advantage at once but gone at delayed recognition (b16); item benefit needs consolidation (a31). Do not assume congruent items are always kept or dropped.
- **Schema clustering memory effect** (b09): one of two experiments, small, inconclusive Bayes factor; none at 24 h.
- **Bartlett's replication.** Bergman and Roediger (d02) say yes; Wynn and Logie (b23) found stable recall of real events; Gauld and Stephenson (b24) are cited for instruction effects. None was read in full. Honest position: distortion exists, its size depends on instructions and material, and Bartlett's rates cannot be cited.
- **Abstraction memory in agents.** Helps in AWM, ExpeL, BoT (c18-c20); hurts relative to raw trajectories in Wang et al. (a29). Likely difference: seeded wrong rules and error handling. Never tested head to head (K10).

### 5.3 Failed or partial failures
- Raykov 2026: SLIMM U-shape reproduced, predicted brain interactions not [b31].
- Cockcroft: memory benefit not stable [b09].
- Xie: much of the "stubborn LLM" result came from incoherent counter-evidence [c05].
- Source-first notes decay when the source no longer fits or decoys crowd it [c12].
- Frontier models showed 0.00 wrong emission in some soft/hard conditions in Kwon's own text (critique item 5), so the lossy-memory effect depends on prompt design.

### 5.4 Moderators
- Delay: importations rise with retention interval (a12); distortion share rises with delay (d02); congruent advantage gone at delay (b16); item benefit needs consolidation (a31).
- Test type: recall, recognition, guessing correction (d03).
- Whether the schema already solves the task: congruent items stored worse (b08).
- Instruction looseness: Continue > Inspire > Rephrase (b01); accuracy instruction for people (b24, unread).
- Temperature: more intrusions at higher temperature; distortion persists at greedy decoding (b06). Attractor strength rises with temperature only in constrained tasks (b02).
- Model size/era: bigger or newer models pulled less in chains (b02); larger models more stubborn on substitution evidence (c05); inverse scaling on some prior-vs-instruction tasks (c03).
- Frequency of wrong entries: harm only when every step (d10).

### 5.5 Interventions
| Intervention | Result | Source |
|---|---|---|
| Direct rebuttal of a wrong prediction (humans) | false memory 0.153 to 0.035; not zero; survives 24 h | b17 |
| Gist plus lookup | equal or better than full text, 3.5x-20x context | c09 |
| Source-first notes | recovery 1.00 where source fits; 0.00 past a size cliff | c12 |
| Forced check on the critical record | +61 to +81 points | d11 |
| One-sentence target-blind rule | +89.3 points in the 3-constraint store | d11 |
| Derivation links with version check | stale plans: 30/30 failures to 30/30 correct | d15 |
| Serve only the active value of a correctly keyed slot | removes stale exposure; key assignment is hard | d14 |
| Incremental delta edits | avoid collapse | d09 |
| Anti-persistence | best in 9 of 9 settings | a29 |
| Evaluator-gated memory addition | better than unfiltered | d12 |
| Schema template from one good example (SA-ICL) | +4.9, +6.4 vs +0.6, +0.3 for plain one-shot in two settings; up to 36.19% best case | a30 |
| CoT / 16 shots on counterfactual tasks | narrows, does not close | d08 |
| Accuracy instruction (people) | reported to reduce distortion | b24 (unread) |
| "List the assumed defaults" step | never tested | K28 |

## 6. Language models

### 6.1 Prior capture in the weights
- Counterfactual tasks (Wu et al., c01, c02, d08): GPT-4, GPT-3.5, Claude, PaLM-2 do worse on a flipped convention (base 9 vs 10, 1-based indexing, altered chess), above chance but consistently lower. GPT-3.5 parseable programs fell from 99% to 62/71/75%. A comprehension check shows the rule was mostly understood. Zero-shot CoT and up to 16 examples narrow the gap; CoT can hurt on simple memorised cases. The gap tracks how common the default is.
- Inverse scaling (c03): on Memo Trap-style tasks larger models can do worse (trend across published series, sometimes U-shaped).
- Content effects (a27, c06): human-like belief bias on syllogisms (all z>=2.25 or chi2>=6.39, p<=0.01); Wason advantage for realistic rules; NLI at ceiling (all p>0.2). Item-level human-model correlation t(345)=4.98. Few-shot examples gave mild gains. 2022-era models.
- Knowledge conflict (c04, c05): coherent counter-evidence accepted when alone; confirmation bias when memory-consistent evidence is also present (GPT-4 80% memorisation on popular entities). Order effects exceed 5% for most models, 30% for PaLM2 and Llama2-7B.
- Stereotype gap filling (c07, c08): 6.8x and 3.4x; the ambiguity was noted 5% of the time; explanations were wrong and hid the cause. 2023 commercial models.

### 6.2 Reconstruction and drift in memory-like loops
- Telephone-game chains (b01-b03, d05): drift grows with instruction looseness. Toxicity collapses toward zero fastest. Length rises for GPT-4o-mini and Mixtral, falls for GPT-3.5 and Llama3-8B. Llama3-70B and GPT-4o-mini have weaker attractors. Property-level measures only; facts were not tracked.
- Content biases in chains (b04, d04): ChatGPT keeps stereotype-consistent, negative, social and threat content more; ambiguity resolved negatively. Surprise not tested.
- GPT-4 grid chains (a28, c16, c25): GPT-4 changes boards less than humans when language is the bottleneck, but moves faster overall.
- Compressive RAG model (b06): Mistral-7B tuned on a Wikipedia topic then the War of the Ghosts produced intrusions matching the topic (football for Sport). Cosine-scored simulation, not a human replication.
- LLM as annotator (b20): centrality and corpus similarity predict which human recalls are distorted.
- Agents (c22): embellish with world knowledge (anecdotes), rarely fabricate whole events.

### 6.3 Agent memory built from abstractions
- Pro: AWM, ExpeL, BoT, Reflexion, SA-ICL (section 3). Author-run, mostly without equal-token controls, on tasks with repeated structure.
- Con: Wang et al. (a29): abstraction below trajectory in seven of nine settings, anti-persistence cheapest in calls. Preprint; the paper warns its nine settings are not independent.
- Damage conditions: harmful bullets cost 4.0 points only when injected every step; every 5 steps the playbook still beat base by 5.4 (d10). Raw wrong records are replayed too (d12); injected records are used (98.2% injection, 76.8% attack).
- Lossy summary (Kwon): wrong-time emission 59% vs 27% (8B), 49% vs 0% (Opus); exact recovery 0.00.
- Staleness: STALE best 55.2%; models inspect the derivation in about 20% of episodes; forced slot +61 to +81.

### 6.4 What changed behaviour, by how much
| Change | Effect |
|---|---|
| Tighter instruction (Rephrase vs Continue) | weaker attractor (b01) |
| Bigger/newer model | weaker attractor (b02) |
| Higher temperature | stronger attractor in constrained tasks only (b02) |
| Zero-shot CoT | gap narrows; can hurt memorised cases (c02) |
| 16-shot examples | gap narrows, not closed (d08) |
| Coherent counter-evidence | accepted at high rates (c05) |
| Gist plus lookup | +1.1 to +1.3 points over full text (c09) |
| Source-first | 1.00 where source fits (c12) |
| Forced critical-path check | +61 to +81 points (d11) |
| Version-linked derivation | 0/30 to 30/30 conflicts detected (d15) |
| Incremental vs whole rewrite | avoids 18,282-to-122 token collapse (d09) |

No LLM study tests Bartlett's design (single-step story recall with rationalisation scoring) or the Brewer and Treyens room (K29). We do not know the size of Bartlett-like distortion in one rewrite by a current frontier model.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established)
1. **memory** [E]: notes keep the original or a re-openable pointer next to any summary. Summaries navigate; answers use source on demand. Evidence: c09, b06, a14 (pure reconstruction cannot hold episodic detail), c12.
2. **memory** [E]: lessons are appended as small dated edits. No whole-memory LLM rewrite. Evidence: d09, b01-b03, d05, a28, d02 (K06, K26).
3. **memory/G** [E]: each lesson carries a timestamp, the input it was derived from and a validity flag. Stale values are not served. Evidence: c13, d14, d15 (K21). Note the derivation-use part is single-source and goes to Test first.
4. **G** [E]: a default or prior must not override a stated rule or contrary evidence. This reinforces G10, because the written reason hides the cause (c08). Evidence: c01-c05, d08, c08 (K12, K13).
5. **memory** [E]: keep "lessons shown after the first attempt, not before" (SCHEMA.md section 5). The first attempt is where default capture shows. Evidence: c01, c03, c04, a09, a10.
6. **memory** [E]: score note recall with a guessing correction, and never assume congruent items are kept better. Evidence: d03, b08, a31.
7. **docs** [E]: cite no Bartlett or Brewer-Treyens rate. Numbers unread (a17, b25, d01).

### Test first
| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Source-first notes (derivation kept, not only conclusion) | memory/G | [S] | c11, c12, d11, d14, d15 | One author per source; fails past a size cliff |
| Forced "open the derivation" check on any stored limit before acting after a correction | G/S | [S] | d11, d15 | Single-author preprints; huge effect needs replication |
| List-the-assumed-defaults operator in S1/S2 | S/O | [S] | d08, c07 | Nobody tested it; CoT already narrows the gap |
| Stored abstractions vs raw cases, with seeded wrong rule | memory | [C] | a29, c18-c20, d10, d12 | Sources conflict |
| Provenance tag (observed/default/inferred) per slot | memory | [S] | a09 by design, d14 | Design extension, no LLM test |
| Perspective-conditioned retrieval or summary | memory/O1 | [S] | a11, a13 | Human-only |
| Violation flag at write time | memory | [C] | b14, b15, b04 | Human results mixed; LLM chain bias runs toward congruent |
| Cap on rewrites per note, plus numeric drift check | memory | [S] | b01, d02, b11 | Delay effect read from abstract only |
| LLM centrality as distortion flag | memory | [S] | b20 | One preprint |
| Template (schema) from one good example at impasse | O7 | [S] | a30, c19 | Best-case numbers |

## 8. Concrete tests on our bench

All arms get equal total tokens, including notes and setup. At least 3 seeds. Log right-to-wrong and wrong-to-right flips per arm (SCHEMA.md section 6).

1. **Counterfactual capture probe.** Items: 30 problem pairs, default vs flipped convention, plus a comprehension check each. Arms: plain; plain + CoT; S1 restatement with a "assumed defaults and where this task differs" line. Metric: accuracy on flipped items and default-minus-flipped gap. Expected: the gap narrows beyond CoT alone. If not, drop.
2. **Seeded wrong rule vs wrong raw fact.** Items: 40 tasks from 4 repeating families. Arms: clean memory; one wrong rule seeded; one matching wrong raw case seeded. Metric: accuracy on later same-family tasks; count of later notes copying the error. Expected: the wrong rule spreads wider (Wang) but is correctable if code gates additions.
3. **Source-first vs summary-only.** Items: 30 multi-step tasks over 3 families (arithmetic with units, scheduling, code state) with a planted mid-run error and a later correction. Arms: summary-only; source-first; source-first + forced derivation check. Metric: exact recovery after correction; wrong-confident emission. Expected: recovery gain where the source fits the budget, none past it.
4. **Bartlett probe.** Items: 20 unfamiliar folk-style stories (300-400 words) plus 20 familiar-script stories with 5 planted atypical details. Task: recall after a filler, then after 5 and 20 summarise-and-rewrite cycles. Arms: plain; "state what the text did not say"; source reopened. Metric: rationalised or intruded details (string match against source, spot-checked), omitted atypical details. Expected: drift grows with cycles; source arm stays low.
5. **Rewrite budget.** Items: 20 notes of about 150 words with numbers and names. Arms: 1, 5, 20 self-rewrites, with and without provenance tags. Metric: numeric and entity retention; drift toward typical values. Expected: drift grows with rewrites; tags slow it.
6. **Perspective-conditioned retrieval.** Items: 30 long documents, each with two perspectives. Arms: perspective-free summary; perspective-conditioned summary; full context. Metric: recall of perspective-relevant vs irrelevant facts. Expected: conditioned summary raises relevant recall; loses the other perspective unless source is reopened.
7. **Violation flag at write.** Items: 40 event logs, 25% with a rule-violating event. Arms: summary only; summary + "unexpected" tags; violating events kept verbatim. Metric: recall of violations; false recognition of 10 plausible absent items. Expected: tags raise violation recall; if not, drop.
8. **Forced critical-path check.** Items: 50 six-record scenarios with one superseded constraint. Arms: free budget of 2 checks; one slot forced onto the anchoring record. Metric: stale-following rate. Expected: large drop (+60 points in d11); this is a replication on our own models.
9. **Brewer-Treyens for agents.** Items: 20 described rooms, each with 10 expected, 4 unexpected and 6 absent-but-expected test objects. Arms: summary memory; summary + source pointer; no memory. Metric: false recognition of absent-but-expected objects; miss rate of unexpected ones. Also supplies the missing LLM number for K29.

## 9. What does not transfer, and why

- **Unconscious schema acquisition and slow consolidation** (Tse, van Kesteren): weights do not change at test time. Consolidation only exists if we write notes.
- **Human exposure and delay** (35 seconds in a room, weeks of retention): the agent's delay is the number of rewrites or tokens, not clock time.
- **Neural claims** (SLIMM brain predictions, clone-structured graphs): not testable by prompting (K20). SLIMM's brain predictions already partly failed [b31].
- **DRM word lists**: associative activation, not schemas [a25].
- **Rationalisation as motive and affective determination** (a06): a model has no motive; the affective result is confounded and tiny.
- **Misleading chatbots creating false memory in people** (d07): about people, matters for user-facing design only.
- **Human congruency effects at long delay**: they depend on consolidation, which prompting does not reproduce.
- **Schema as one module**: five processes with unequal evidence (K19).
- **Reflexion-style gains** need a clear failure signal [c21], absent in open memory.
- **Telephone-game property trends** (toxicity to zero) concern style, not which facts are dropped [b03, d05].

## 10. Open questions

1. Exact N and intrusion/recognition rates in Brewer and Treyens (1981), and an LLM replication (gap 1, K17, K29).
2. Gauld and Stephenson (1967) and Wynn and Logie (1998) numbers; the size of the instruction effect (gap 5).
3. Does a seeded wrong rule persist longer than a seeded wrong raw fact at equal tokens? (K09, K27, gap 2).
4. Does source-first beat summary-only across several task families? (K08, gap 3).
5. Do current frontier models reproduce Bartlett-style distortion in single-step recall, and how does it scale with delay or context length? (gap 4).
6. Does an assumptions-listing operator close the counterfactual gap beyond CoT? (K28, gap 6).
7. Which schema-violating items does LLM summarisation drop or keep: surprise or congruence? (gap 7).
8. Is there a newer congruency meta-analysis (Stangor and McMillan 1992 not found; gap 8)?
9. Does repeated self-summarisation drift matter at our context lengths, and does provenance tagging slow it? (gap 9).
10. Can LLM-estimated centrality flag notes at risk of distortion? (b20, gap 10).
11. How much of "abstraction hurts" in Wang et al. comes from seeded errors rather than abstraction?
12. Do the 2026 preprints (b14-b18, b20, d11, d15, a29) survive peer review?

## 11. Sources

[V] = page or full text read. [M] = metadata, snippet, abstract only, or citation memory.

**Bartlett and theory**
- [V] Bartlett (1932) Remembering, 1995 reprint (a01-a08). https://archive.org/details/frederic-c.-bartlett-remembering-a-study-in-experimental-and-social-psychology-c (could not be re-opened in the critique pass; counts stand as first recorded)
- [V] Minsky (1974) A Framework for Representing Knowledge (a09, a10). https://courses.media.mit.edu/2004spring/mas966/Minsky%201974%20Framework%20for%20knowledge.pdf
- [M] Rumelhart (1980) Schemata (a19). https://doi.org/10.4324/9781315107493-4
- [M] Alba and Hasher (1983) Is memory schematic? (a20, b28). https://doi.org/10.1037/0033-2909.93.2.203
- [M] Hintzman (1986) (a26). https://doi.org/10.1037/0033-295X.93.4.411
- [V] Brewer and Nakamura (1984) (a14-a16). https://files.eric.ed.gov/fulltext/ED248491.pdf
- [V] Wikipedia, Schema (psychology), lineage only (a18). https://en.wikipedia.org/wiki/Schema_(psychology)
- [M] Ghosh and Gilboa (2014) (a34, b30). https://doi.org/10.1016/j.neuropsychologia.2013.11.010
- [M] Tse et al. (2007) (a35). https://doi.org/10.1126/science.1135935

**Reading research**
- [V] Anderson and Pichert (1977) (a11, a12). https://files.eric.ed.gov/fulltext/ED142974.pdf
- [V] Pichert and Anderson (1977) (a13). https://files.eric.ed.gov/fulltext/ED134936.pdf

**Founding studies and replications**
- [M] Brewer and Treyens (1981) (a17, b25, d01). https://doi.org/10.1016/0010-0285(81)90008-6 ; secondary https://www.themantic-education.com/ibpsych/2021/10/15/key-study-the-office-schema-study-brewer-and-treyens-1981/
- [M] Lampinen, Copeland and Neuschatz (2001) (b26). https://doi.org/10.1037/0278-7393.27.5.1211
- [M] Bergman and Roediger (1999), abstract page read (a21, b22, d02). https://link.springer.com/article/10.3758/BF03201224
- [M] Gauld and Stephenson (1967) (a22, b24). https://doi.org/10.1111/j.2044-8295.1967.tb01054.x
- [M] Wynn and Logie (1998) (a23, b23, d17). https://doi.org/10.1002/(SICI)1099-0720(199802)12:1<1::AID-ACP493>3.0.CO;2-M
- [M] Roediger and McDermott (1995) (a24). https://doi.org/10.1037/0278-7393.21.4.803
- [V] Huff, Bodner and Fawcett (2021) DRM review (a25). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8200635/
- [M] Rojahn and Pettigrew (1992), abstract read via Europe PMC (b27, d03). https://europepmc.org/article/MED/1535823
- [M] Tuckey and Brewer (2003) (b29). https://doi.org/10.1002/acp.906
- [M] Kleider et al. (2008) (b32). https://doi.org/10.1002/acp.1361

**Modern human work**
- [V] van Kesteren et al. (2013) (a31). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3567062/
- [V] Sweegers et al. (2015) (a32, b08). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4659923/
- [V] Frank et al. (2018) (a33). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6049394/
- [V] Cockcroft et al. (2022) (b09, b10). https://osf.io/preprints/psyarxiv/nzurq
- [V] Xu, Hemmer and Zhang (2023) (b11). https://osf.io/preprints/psyarxiv/9a7ft
- [V] Tompary and Thompson-Schill (2021) (b12). https://osf.io/preprints/psyarxiv/u754s
- [V] Conceptual vs perceptual features (2025) (b13). https://osf.io/preprints/psyarxiv/swy32
- [V] Curtis et al. (2026) (b14). https://osf.io/preprints/psyarxiv/56kqr
- [V] Nguyen, McRae and Zacks (2026) (b15). https://osf.io/preprints/psyarxiv/dc9tw
- [V] Gustarova and Chromy (2026) (b16). https://osf.io/preprints/psyarxiv/5dsvq
- [V] Mubarak and Fukuda (2026) (b17). https://osf.io/preprints/psyarxiv/acshn
- [V] Mubarak et al. (2026) (b18). https://osf.io/preprints/psyarxiv/g8peq
- [V] Prior knowledge registered report (2025) (b19). https://osf.io/preprints/psyarxiv/7tg4p
- [V] Predicting memory distortions in verbal recalls (2026) (b20, b21). https://osf.io/preprints/psyarxiv/sfqea
- [M] Hemmer and Steyvers (2009) (b33). https://doi.org/10.1111/j.1756-8765.2008.01010.x
- [M] Raykov et al. (2026) (b31). https://doi.org/10.1098/rstb.2025.0250

**LLM and AI**
- [V] Dasgupta, Lampinen et al. (2022) (a27, c06). https://arxiv.org/abs/2207.07051
- [V] Kumar et al. (2024) (a28, c16, c25, d06). https://arxiv.org/abs/2402.03618
- [V] Wang, Panaganti and Zhou (2026) (a29). https://arxiv.org/abs/2610.27406
- [V] Chen et al. (2025) SA-ICL (a30). https://arxiv.org/abs/2510.13905
- [V] Perez et al. (2025) (b01-b03, d05). https://arxiv.org/abs/2407.04503
- [V] Acerbi and Stubbersfield (2023) (b04, d04; c17 is the PNAS DOI, [M]). https://pmc.ncbi.nlm.nih.gov/articles/PMC10622889/
- [V] Meylan, Nair and Griffiths (2021) (b05). https://arxiv.org/abs/2101.09788
- [V] Hippocampo-neocortical compressive RAG (2026) (b06, b07). https://pmc.ncbi.nlm.nih.gov/articles/PMC13447824/
- [V] Wu et al. (2023/24) (c01, c02, d08). https://arxiv.org/abs/2307.02477
- [V] McKenzie et al. (2023) (c03). https://arxiv.org/abs/2306.09479
- [V] Xie et al. (2024) (c04, c05). https://arxiv.org/abs/2305.13300
- [V] Kotek et al. (2023) (c07, c08). https://arxiv.org/abs/2308.14921
- [V] Lee et al. (2024) ReadAgent (c09, c10). https://arxiv.org/abs/2402.09727
- [V] Kwon (2026) (c11, c12). https://arxiv.org/abs/2606.25449
- [V] Chao et al. (2026) STALE (c13). https://arxiv.org/abs/2605.06527
- [V] Swaminathan et al. (2023) (c14). https://arxiv.org/abs/2307.01201
- [V] Van de Maele et al. (2026) (c15). https://arxiv.org/abs/2601.18946
- [V] Wang et al. (2024) Agent Workflow Memory (c18). https://arxiv.org/abs/2409.07429
- [V] Yang et al. (2024) Buffer of Thoughts (c19). https://arxiv.org/abs/2406.04271
- [V] Zhao et al. (2024) ExpeL (c20). https://arxiv.org/abs/2308.10144
- [V] Shinn et al. (2023) Reflexion (c21). https://arxiv.org/abs/2303.11366
- [V] Park et al. (2023) Generative Agents (c22). https://arxiv.org/abs/2304.03442
- [V] Binz and Schulz (2023) (c23). https://arxiv.org/abs/2206.14576
- [V] Sumers et al. (2024) CoALA (c24). https://arxiv.org/abs/2309.02427
- [V] Chan et al. (2024) (d07). https://arxiv.org/abs/2408.04681
- [V] Zhang et al. (2026) ACE (d09, d10). https://arxiv.org/abs/2510.04618
- [V] Nakayashiki (2026) (d11). https://arxiv.org/abs/2608.25553
- [V] Xiong et al. (2025) (d12). https://arxiv.org/abs/2505.16067
- [V] Dong et al. (2026) MINJA (d13). https://arxiv.org/abs/2503.03704
- [V] Deng and Sinchaisri (2026), abstract and introduction (d14). https://arxiv.org/abs/2610.10265
- [V] Chen, Wang and Brinton (2026) PlanFence, abstract and introduction (d15). https://arxiv.org/abs/2609.03340
- [M] Who Remembers What? (2025), abstract only (d16). https://underline.io/lecture/138001-who-remembers-whatquestion-tracing-information-fidelity-in-human-ai-chains

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 3 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A06.05-K01** (now single-source: the sources are not independent). Numbers match Anderson and Pichert (+7.1% vs -2.9%, F(1,35)=9.57; -21% in Exp 2, t(15)=5.36), but a11 and a12 are one report and a13 is the same authors' companion report, so it is one lab's work; also the Exp 1 old-perspective loss (-7.2%) was not significant.
- **A06.05-K06** (reworded: the sources support less). Attractor ordering, toxicity and model differences are confirmed in Perez et al., but the GPT-4-faster-than-humans velocity result is from Kumar et al. on binary grid boards, not text chains, and the claim does not scope it. Corrected claim: Serial-reproduction chains converge on attractors in LLMs: attractor strength Continue > Take inspiration > Rephrase; toxicity the strongest attractor property among the four tested; strength varies by model (Llama3-70B and GPT-4o-mini weaker). Separately, in a binary-grid-board serial-reproduction task GPT-4 chains had higher chain velocity than human chains.
- **A06.05-K11** (reworded: the sources support less). The 86.91-87.17% QuALITY scores correspond to ~2.4-2.8x extension (ReadAgent-P 1-6 pages, ReadAgent-S), the ~3.5x setting scores 86.16%, and the 20x comes from NarrativeQA; the 1-page look-up was below full text (84.13%); the Spens-Burgess paper shows gist stores produce schema intrusions, not accuracy support. Corrected claim: ReadAgent gist memory with look-up extends effective context 3.5x to 20x across three tasks; on QuALITY it scored 86.16% (3.5x setting) to 87.17% (ReadAgent-S) vs 85.83% for the full text, though a 1-page look-up scored 84.13%; gist plus detail retrieval is a plausible schema-like store, with gist reconstruction producing schema-like intrusions in a related model.
- **A06.05-K13** (now single-source: the sources are not independent). Both evidence lines for the counterfactual-accuracy result are the same Wu et al. paper; McKenzie et al. concerns inverse scaling and does not test counterfactual task variants; Wu says above random on most (not all) tasks, abstract says nontrivial.
- **A06.05-K24** (reworded: the sources support less). Acerbi and Stubbersfield coefficients match, but it is one study on one model (ChatGPT-3, Jan 2023); the Perez et al. line does not support it (toxicity collapses toward zero over chains), so the general 'LLMs' wording is wider than the evidence. Corrected claim: In five transmission-chain experiments with ChatGPT-3 (Acerbi and Stubbersfield 2023), the model retained stereotype-consistent, negative, social and threat content over neutral content and resolved ambiguity negatively (coefficients 0.058 to 0.523, all P<0.01); other multi-turn work (Perez et al. 2025) finds toxicity decays in LLM chains, so the bias is not general.
- **A06.05-K14** (now single-source: only one opened source, code check).
