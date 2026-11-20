# Language of thought: deep document

*Subfield D06.02, philosophy of mind. Built from evidence_a-d.jsonl (about 78 lines, about 40 distinct sources), claims.jsonl (K01-K22) and critique.md in this folder. Importance for our agent: background. The practical yield is small and mostly about evaluation hygiene, decomposition, code offload and memory writes. Many evidence lines duplicate one source, so counts below are by independent source, not by line.*

## 1. What it is

The language of thought hypothesis (LOTH, Fodor 1975) says that thinking happens in an inner symbolic medium, "Mentalese". Complex thoughts are built from primitive symbols by combination rules. Mental processes act on the form of those symbols (a01).

Core theses listed by the SEP entry (a01): the representational theory of thought (RTT), compositionality, logical structure, classical computation, and formal syntactic computation. All arguments for LOTH are abductive, that is, inference to the best explanation (a01).

Three phenomena are meant to be explained:
- **Productivity.** A finite thinker can entertain unboundedly many thoughts. Finite primitives plus recursive rules explain this (a02). It is a competence claim. Real thinkers run out of memory and time.
- **Systematicity.** Whoever can think "John loves Mary" can think "Mary loves John". Systematicity of inference: whoever infers p from "p and q" can infer m from "m and n" (a03).
- **Compositionality and inferential coherence.** The meaning of a complex thought comes from its parts and their mode of combination.

Why this matters for machine learning: these are testable as generalisation tests. Train on some combinations, test on new ones. Productivity becomes "longer or deeper than seen". Systematicity becomes "known parts in new roles or pairs". That is what SCAN, CFQ, COGS and PCFG SET do (a07-a12). So the debate between classical symbol systems and connectionist nets became an empirical benchmark literature, and later a literature on LLMs.

Honest scope. The hypothesis is a claim about human cognition. It gives our agent vocabulary and test shapes. It adds no operator of its own. The scaffold already treats thought as structured steps run by code (SCHEMA section 1).

## 2. History and theories in depth

**Founding (1975-1990).**
- Fodor (1975): learning and decision theories presuppose an internal representational medium with language-like syntax and semantics (a20, not opened).
- Fodor and Pylyshyn (1988): systematicity, productivity, compositionality and inferential coherence must be explained by any theory of cognitive architecture. Classical architectures (symbols with constituent structure, structure-sensitive processes) predict them. Plain connectionist nets have no built-in guarantee. At best they implement a classical system (a04, a21; read via the SEP reconstruction, the 1988 paper was not opened).
- Smolensky (1988, 1990): tensor-product binding of role and filler vectors gives distributed representations with recoverable structure (a23, not opened). Chalmers and van Gelder gave similar replies (a05).
- Fodor and McLaughlin (1990): vector constituents are not causally operative, so they do not explain systematicity (a05, a22). The dispute is about whether implicit vector structure counts as constituency. The SEP text says data never settled it. Do not cite the DOI for a22 until checked: a22 and b21 disagree on the last digit.
- Marcus (1998, 2001): connectionist nets fail to generalise rules outside the training space, while infants show rule-like generalisation (a24, not opened). Lake and Baroni 2018 is the modern form of this test.

**Non-human evidence.** Gallistel and King (2009) defend classical computation using navigation and memory in animals (a06, via SEP). SEP warns that evidence from perception or navigation does not establish RTT for high-level human thought.

**Modern versions.**
- Probabilistic language of thought: concept learning as Bayesian inference over short programs (Piantadosi, Tenenbaum, Goodman, 2012 and 2016; a25, not opened).
- "The best game in town" (Quilty-Dunn, Porot, Mandelbaum, BBS 2023): LOT is the best explanation of a cluster of effects across vision, memory, animal and infant work (a26, only SEP citation seen).
- Program-induction builds: DreamCoder (a19, c22), LLM plus probabilistic programs (c20), LLM hypothesis proposers with Bayesian scoring (c21).

**The empirical turn (2018 onward).** Lake and Baroni 2018 turned the "dax" thought experiment into a benchmark. Keysers 2020 gave a principled way to build splits (maximum compound divergence). Csordas 2021 and Ontanon 2022 showed the early failure was partly setup. Lake and Baroni 2023 answered with meta-learning. LLM-era work (2022-2026) asks the same question of pretrained models, usually under names like compositionality gap, reversal curse, counterfactual tasks and process errors.

**Mechanistic turn (2024-2025).** Feng and Steinhardt (b17) and Yang et al. (d08) found variable-binding-like circuits inside LLMs. This is a partial vindication of a weak symbol story, as an emergent mechanism.

**Where the field stands.** The strong claim (a symbolic code is built into the architecture) is not needed to get systematic behaviour from nets. The claim that systematic behaviour does not come free is correct: it needs the right training signal, setup or explicit decomposition. Whether that settles anything about human minds is contested (K15).

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. "Model" means trained from scratch unless a pretrained LLM is named.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Seq2seq nets pass a random split, fail a new primitive in composed commands (SCAN add-jump) | Random split best 99.8%. Add-jump best 1.2%, overall-best 0.08%. Turn-left up to 90.3%. 5 runs, 100k presentations | Lake and Baroni 2018 (a07, a09) | E (with CFQ, COGS) |
| Generalisation rises with coverage of composed examples | 1% of commands about 5%; 2% about 54%; 4% about 93%. Jump from 8, 16, 32 composed commands: 38.3, 77.8, 88.4% | a07, a09 (c02) | S |
| Length extrapolation fails (productivity) | Length split best 20.8%, overall-best 13.8%; 60.2% with oracle length. 24-action commands 95.76% to 48-action 22.8% | a08 | E (with Hupkes, Csordas) |
| Attention SRN on random split is weak and unstable | 59.7% mean, range 18.4-94.0% | a07 | S |
| CFQ: compound divergence predicts accuracy | Random vs MCD: LSTM+attn 97.4 vs 14.9; Transformer 98.5 vs 17.9; Universal Transformer 98.0 vs 18.9. SCAN MCD 6.1, 1.1, 1.2. R2 of compound divergence 0.81-0.88; length ratio 0.11-0.22 | Keysers 2020 (a10, b03) | E |
| COGS: near-perfect in distribution, poor out | In-distribution 96-99%; generalisation 16-35%, seed sd about 6-8 points. Transformer 0.35, uni-LSTM 0.32, bi-LSTM 0.16. Recursion and PP depth near 0% | Kim and Linzen 2020 (a11, b04) | E |
| PCFG SET five tests | Task accuracy LSTM 0.79, ConvS2S 0.85, Transformer 0.92. Systematicity 0.53/0.56/0.72. Productivity 0.30/0.31/0.50 (drops 62/64/46%). Overgeneralisation 0.68/0.79/0.88 | Hupkes 2020 (a12, b02) | E |
| Rare exceptions are not memorised | At 0.1% exception rate Transformer applies the rule to 88% of exceptions at some point (LSTM 68%, ConvS2S 79%); at 0.5% almost no overgeneralisation | c09 | S |
| Setup, not architecture, explains much of the Transformer gap | PCFG productivity 50 to 85%; systematicity 72 to 96%; COGS 35 to 81%; SCAN length 100% with relative positions. Invisible on IID validation | Csordas 2021 (a13, b05); Ontanon 2022 (b06, numbers not extracted) | E |
| Meta-learning gives human-like few-shot systematicity | Humans (n=25) 80.7% exact, 72.5% on longer outputs; MLC 82.4% and 77.8%. One-to-one errors 56.3% MLC vs 24.4% human. SCAN lexical error 0.22% vs 99.27% plain. COGS lexical error 0.87%. SCAN length and COGS structural: 100% error | Lake and Baroni 2023 (a15, c10, c11) | S |
| Least-to-most closes SCAN length gap in a prompted LLM | code-davinci-002 16.7 / 16.2 / 99.7 (standard / CoT / LtM), 14 exemplars. text-davinci-002 6.0 / 0.0 / 76.0. code-davinci-001 0.4 / 0.0 / 60.7. 13 residual failures (6 mis-scoped repeat after "around") | Zhou 2022 (a14, b07, c12, c13) | S |
| Compositionality gap in 2-hop questions | About 40% across GPT-3 sizes; ChatGPT 42.9%; GPT-4 23.0%. Self-ask 79.6 vs CoT 45.7 (Davinci-002, Compositional Celebrities, 8.6k questions); Davinci 54.2 vs 1.1 | Press 2023 (b08, c14) | S |
| Multi-step failure grows with depth; hidden wrong steps | 3x3 multiplication ChatGPT 55%, GPT-4 59%. 82.3% of correct 4x2-digit answers had a wrong step | Dziri 2023 (a16, b09, c17) | S for the number; E for depth decay (with d04) |
| Hidden wrong-step rate rises with difficulty | Share of correct-answer solutions with a wrong step: GSM8K 3.5%, MATH 18.8%, OlympiadBench 32.2%, Omni-MATH 51.8%. Critic F1: o1-mini 87.9, QwQ-32B 71.5, GPT-4o 61.9 | ProcessBench (d09) | S |
| Accuracy follows output probability | GPT-4 shift cipher 51% high-probability output vs 13% low. Pig Latin 42 vs 23% | McCoy 2024 (b13) | E |
| Counterfactual variants lower accuracy | GPT-4 two-digit addition base-10 100.0 vs base-9 23.4 (1,000 instances). GPT-3.5 parseable programs 99% to 62-75% | Wu 2024 (a18, d02) | E |
| Reasoning model shrinks but keeps the effect | o1-preview shift cipher 47% (low-prob) to 92% (high). Acronyms 100% vs 99.9% rare, but far more thinking tokens on rare | McCoy o1 (d01) | E with b13 |
| Irrelevant clause hurts | GSM-NoOp: Phi-3-mini down by more than 65%; o1-preview still declines (figure not extracted) | GSM-Symbolic (d03) | S |
| Reasoning models collapse beyond a depth | Hanoi 10 disks needs 1,023 moves; models fail near move 100. River Crossing first error by move 4. Giving the algorithm did not help. Non-thinking wins at low complexity at equal compute | Shojaee 2025 (d04) | S (commentary on token limits not read) |
| Reversal curse | GPT-4 parent 79% vs child 33%. Fine-tuned GPT-3: 96.7% forward, about 0 reversed (50.0% in the matched-order description experiment). Llama-1 above 80% / below 7% (the question-answer experiment). Absent for in-context facts | Berglund 2023 (a17, b11, c25) | S (one paper; small-model echo in d06) |
| Reversal in small models is a binding failure | 0.0% reversal for standard next-token training regardless of depth or tied embeddings; JEPA design and memory layers fix it | Wang and Sun 2026 (d06) | S |
| Code as thought removes arithmetic failure | GSM-HARD: CoT 65.6 to 20.1%; PAL stays 61.5% (down 14.3). Direct 19.7 to 5.0. Object counting 96.7% (+23.7). In 16 of 25 inspected cases CoT wrote near-identical reasoning for small and large numbers | PAL (c18, c19) | S; supported by d05 |
| CoT helps mostly on symbolic tasks | Mean gains: symbolic +14.2, math +12.3, logic +6.9 points; other categories 56.8 vs 56.1. About 95% of MMLU gain on questions with an equals sign. Plan plus tool solver beat plan plus CoT solver in most settings | Sprague 2025 (d05) | E |
| LLM binding circuits | Additivity check: above 99% control, below 3% under mean interventions (Pythia, LLaMA). Symbol abstraction, symbolic induction and retrieval heads; Llama-3.1 70B 95% on 2-shot rule induction | Feng and Steinhardt (b17); Yang 2025 (d08) | E for binding-like codes, interpretation C |
| GPT-3 does relational reasoning | Digit matrices vs humans (N=40): generative OR 1.88, p=0.005; multiple choice OR 6.27. Zero-generalisation OR 1.76, CI [1.27, 2.46]. Story analogies: humans better, OR 0.37 | Webb 2023 (b15, c24) | C |
| Abstract reasoning is weak out of distribution | Up to about 0.6 accuracy at 16 examples (GPT-4, Davinci-3); fine-tuned LLaMA2 near-perfect in distribution, big drop on OOD syntax | Gendron 2023 (b16) | C |
| Grokking composition | Train accuracy above 99% at about 14K steps; ID test 9.2% then near perfect after about 50x more steps; OOD composition zero after 2M steps | Wang 2024 (b18) | S |
| Latent thought vs words | ProsQA CoT 77.5 vs Coconut 97.0; ProntoQA 98.8 vs 99.8; GSM8k CoT 42.9 vs Coconut 34.1 vs no-CoT 16.5 | Hao 2024 (c26, d10) | S |
| Program induction | DreamCoder SyGuS 3.7% before, 79.6% after learning (CVC4 82.4%; big budget 84.3%); 93% of physics laws learned after 8 cycles | Ellis 2020 (a19, c22) | S |
| LLM hypothesis proposal plus Bayes | 100 proposals explain 81% of human judgment variance (R2 .81), within 3% of human accuracy | Ellis 2023 (c21) | S |
| Infant rule learning is small | 20 reports, 63 experiments, 1,318 infants; Hedges g 0.25, 95% CI 0.09-0.40; publication bias likely; no tone learning without speech priming (Marcus 2007) | Rabagliati 2019 (d11, d13) | C |
| Rats transfer an XYX rule | Abstract only; counts not read | Murphy 2008 (d14) | S |

## 4. Mechanisms and models

Each is described so an engineer could build the test or the component.

**4.1 Compound-divergence splits (Keysers).** Take a dataset of items built from atoms (words, operators, entities) and compounds (combinations). Define atom divergence and compound divergence as distances between train and test frequency distributions of atoms and compounds. Search for a train/test split that keeps atom divergence near 0.02 and maximises compound divergence. Accuracy drops as compound divergence rises. For our bench: build items from our own operators (O1-O8) and problem classes, hold out specific operator-pair or role combinations, and report accuracy against compound novelty, not against length (b03).

**4.2 Primitive-in-composition test (SCAN add-jump).** Show a new primitive only in isolation or in few composed contexts. Test it in composed contexts it never appeared in. Score is a function of how many distinct composed examples were seen (8, 16, 32 composed commands gave 38.3, 77.8, 88.4%). Distinct composed examples matter more than repeats (c02).

**4.3 Length and depth split.** Train or exemplify up to length L. Test beyond it. Check separately whether failures are the stop decision (end-of-sequence) rather than the content (a08; Csordas follow-up). Oracle length lifted SCAN length from 20.8 to 60.2%, so a large part of the loss was the stopping decision; the rest was content.

**4.4 Compositionality gap (Press).** For each 2-hop question, ask both single-hop questions and the composed one. Gap = P(both singles right) minus P(composed right). Self-ask mechanism: the prompt shows the model writing "Are follow-up questions needed? Follow up: ... Intermediate answer: ..." lines, ending in "So the final answer is". Optionally route each follow-up to a search tool (b08, c15).

**4.5 Least-to-most prompting (Zhou).** Two prompts. Stage 1, decomposition: from a few exemplars, the model lists the sub-problems from simplest to hardest. Stage 2, solving: solve each sub-problem in order, with earlier sub-problems and answers in context. On SCAN this used 14 exemplars and a grammar-aware decomposition prompt. Code decides the order and what goes into context (a14, c12). Cost: more calls, so any claim of benefit must be at equal tokens.

**4.6 Code as thought (PAL).** The model writes a program whose variable names carry the problem entities. An interpreter runs it and the result is the answer. This moves exact execution (arithmetic, counting, loops) out of the model. The model keeps parsing and planning (c18, c19, d05).

**4.7 Variable binding in LLMs (Feng and Steinhardt; Yang).** Entities and their attributes receive matching "binding ID" vectors in the residual stream. Swapping the vector swaps the belief. Three head types in open models: symbol abstraction heads (token to abstract variable), symbolic induction heads (run induction over variables), retrieval heads (read out the value). Detection method: causal mediation, then ablation. A prompt cannot change this. It matters because capacity is limited: binding distance reflects how discernible entities are (b17, d08).

**4.8 Meta-learning for compositionality (MLC).** Train one Transformer on a stream of episodes. Each episode has a fresh random assignment of words to meanings plus a few study examples and a query. The model must infer the mapping in context. This trains systematicity as a skill. It needs training, so it is out of reach for a prompt-only scaffold. A prompt analogue, many fresh few-shot episodes in context, is untested (a15, c10).

**4.9 Bayesian program and hypothesis search.** DreamCoder: wake phase solves tasks with programs written from a library; sleep phases add abstractions to the library and train a neural guide. LLM variant (Ellis 2023): the LLM proposes about 100 natural-language hypotheses per batch, a prior and a likelihood reweigh them, the posterior is used for prediction. Implementable as propose-many, score-in-code, answer-from-top (a19, c21).

**4.10 Latent thought (Coconut).** Feed the last hidden state back as the next input embedding instead of decoding a word. Needs training with a curriculum that replaces CoT steps by latent steps one at a time. Latent thoughts hold several candidate next steps, like breadth-first search. Not available to a prompt-only scaffold (c26, d10).

**4.11 Step-error audit (ProcessBench).** Humans annotate the first erroneous step in solutions. A critic prompted to find the first error is scored by F1 on error and correct solutions. The strongest model as critic beat small process reward models (d09).

## 5. What holds up

**Holds up well (two or more independent sources).**
- Random-split success hides recombination failure, in RNNs and Transformers, on SCAN, CFQ, COGS and PCFG SET (K01).
- IID validation hides the gap. Selecting settings on in-distribution data is the main way people fooled themselves (K02). Csordas: early stopping on an IID set was misleading. Keysers tuned on a random split only to avoid leaking the test distribution (c06).
- Productivity (longer than seen) is harder than lexical systematicity. It is the weakest facet for all three PCFG models, and for SCAN (K03).
- LLM accuracy depends on output probability, task frequency and surface features even in deterministic symbolic tasks. Reasoning training reduces the effect on accuracy but not to zero (K08, K17).
- CoT helps mostly on math, symbolic and logic tasks; elsewhere about nothing (d05).

**Replications and failed replications.**
- The early claim "Transformers cannot do systematicity" (from a10, a11) was largely a setup artifact. Csordas and Ontanon lifted PCFG productivity 50 to 85%, COGS 35 to 81%, SCAN length to 100%. Structural COGS cases remain weak, and MLC still scores 100% error on SCAN length and COGS structural (c11).
- Reversal curse: echoed in small from-scratch models (0.0% reversal, d06). No frontier or reasoning-model reversal test and no agent-with-memory test was found.
- Press gap: shrank with GPT-4 (23.0%) but not with GPT-3 size. The scale effect is unclear.
- Infant rule learning: the original effect (Marcus 1999) is real but small (g 0.25). Marcus 2007 found a high-powered null for tones. Later work (Ferguson and Lew-Williams 2016, cited in the meta-analysis) found non-speech learning in a communicative setting. Publication bias is flagged (d11, d12, d13).
- GPT-3 analogical reasoning (Webb): later work challenged contamination (c24). Dziri says LLMs match subgraphs; Webb says GPT-3 does abstract relational reasoning above humans. The two were not reconciled; they use different tasks.
- No independent replication found for MLC on structural splits, Coconut, least-to-most on current models, or grokking.

**Moderators.**
- Coverage: distinct composed examples (c02).
- Probability and frequency of task, output, input (b13).
- Depth of the computation graph (a16, d04).
- Difficulty (d09).
- Exposure to speech versus tones in infants (d13).
- A hand-written decomposition prompt and a code-pretrained model for least-to-most (c12).

**Interventions that worked.**
- Explicit decomposition, one paper (K04): 99.7% vs 16.2% on SCAN length.
- Code execution for arithmetic (K10): 61.5% vs 20.1% on GSM-HARD.
- Plan plus tool solver over plan plus CoT solver (d05).
- Meta-learning episodes, lexical splits only (K05).
- Self-ask, one paper on a retired model (K06).
- Stronger-model critic for step errors (d09).
- Architecture or memory fixes for the reversal curse in small models (d06).

**Interventions that did not work.**
- Scaling alone did not close the Press gap (about 40% across GPT-3 sizes).
- Giving the algorithm in the prompt did not stop collapse on puzzles (d04).
- Data augmentation did not remove the reversal curse (c25).
- Training past overfitting gave no OOD gain on multiplication (b09).
- Plain CoT did not help SCAN length (16.2% vs 16.7% standard; 0.0% for text-davinci-002).
- Attention in RNNs gave unstable results (59.7%, range 18.4-94.0%).

**Weak spots in the evidence.**
- Founding human-side claims have no numbers in our files (Fodor 1975, Fodor and Pylyshyn 1988, Smolensky, Marcus book, Quilty-Dunn were not opened).
- Nothing from 2025-2026 on frontier reasoning models for CFQ, COGS, Compositional Celebrities or SCAN length.
- Several records say "numbers not extracted" (b06, b12, b14, c15).
- Records c01-c13 are labelled llm-study but test RNNs and Transformers trained from scratch.

## 6. Language models

**Pretrained LLMs, 2022-2023 era.**
- 2-hop composition: gap about 40% across GPT-3 sizes; ChatGPT 42.9%, GPT-4 23.0% (b08, c14). Self-ask lifted Davinci-002 from 45.7 to 79.6% (b08). Unopened lead: nine frontier LLMs fail two-hop without CoT in over half of question categories (d07, snippet only; do not cite numbers).
- SCAN length: standard prompting 16.7%, CoT 16.2%, least-to-most 99.7% (code-davinci-002). Text-davinci-002 6.0, 0.0, 76.0 (a14, c12). The gain needs decomposition, and the strongest result used a code-pretrained model.
- Multiplication: ChatGPT 55%, GPT-4 59% on 3x3. 82.3% of correct 4x2 answers had a wrong step (a16).
- Reversal curse: GPT-4 79% vs 33% (a17). It does not occur when the fact is in context (b11).
- Counterfactual tasks: GPT-4 addition 100.0% base-10 vs 23.4% base-9 (d02). GPT-3.5 programs 99% to 62%.
- Embers of autoregression: GPT-4 shift cipher 51% vs 13% by output probability (b13).
- Abstract reasoning: GPT-3 beats undergraduates on digit matrices (OR 1.88 and 6.27) and loses on story analogies (OR 0.37) (b15, c24). Gendron finds weak OOD abstract reasoning (b16). Lampinen finds human-like content effects (b14). Mahowald separates formal language competence from functional reasoning (c23).

**Reasoning-trained models, 2024-2025.**
- o1-preview: shift cipher 47% to 92% by output probability, down from big common/rare gaps in earlier models. Rare acronym accuracy 99.9% but with many more thinking tokens (d01). Thinking tokens act as a difficulty signal.
- GSM-NoOp: one irrelevant clause still cuts o1-preview accuracy. Phi-3-mini down by more than 65% (d03).
- Puzzle depth: o3-mini, DeepSeek-R1 and Claude 3.7 thinking collapse beyond a model-specific depth, spend fewer thinking tokens near collapse, and do not benefit from the algorithm being written in the prompt. Non-thinking models win at low complexity at equal compute (d04). Commentary on token limits and puzzle solvability was not read.
- Hidden wrong steps: 3.5% to 51.8% of correct-answer solutions contain a wrong step as difficulty rises (d09). The 82.3% multiplication figure was not re-measured on reasoning models.
- CoT: the meta-analysis shows the benefit is concentrated in symbolic tasks and in execution rather than planning (d05).

**Mechanistic.** Open LLMs (Pythia, LLaMA, Llama-3.1, Qwen2.5, Gemma-2) contain binding-ID vectors and symbol abstraction, symbolic induction and retrieval heads. Ablating them sends the correct-answer probability to zero (b17, d08).

**What changed performance, and by how much.**
- Decomposition: +83.0 points on SCAN length (16.7 to 99.7), one model.
- Code offload: +41.4 points over CoT on GSM-HARD (20.1 to 61.5).
- Self-ask: +33.9 points on Compositional Celebrities (45.7 to 79.6), one model.
- Model upgrade GPT-3.5 to GPT-4 on the Press gap: 42.9% to 23.0%.
- Reasoning training on rare-variant gaps: mostly removed on accuracy for o1 on the tested tasks, not removed for output-probability sensitivity.
- Scaling alone: no change in the Press gap across GPT-3 sizes.

**Caveat.** Almost every LLM number here is from GPT-3, GPT-3.5, GPT-4, Llama-1 or o1-era models. We have no CFQ, COGS or SCAN-length numbers for current Claude, Gemini 2.5+ or GPT-5-era models. Treat all effects as hypotheses for current models.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Keep a held-out recombination split for every scaffold evaluation, and never tune on in-distribution items.** G (evaluation hygiene, extends G3 and G7). [E] K01, K02. Evidence a07, a10, a11, a13, b03, b05, c06. Reason: IID scores were near perfect (96-99%, 97-98%) while systematic scores were 16-35% and 15-19%. Settings picked on IID data look fine and fail.
2. **Pair each bench item with a rare or counterfactual twin and an irrelevant-clause twin; report the gap.** G (check against surface familiarity). [E] K08, K17. Evidence b13, a18, d01, d02, d03. A gap means pattern reuse, not procedure. Use thinking-token spend on the rare variant as a difficulty signal.
3. **Verify intermediate steps, not only final answers, on hard items.** G (extends G2 and G10). [E] that wrong steps grow with difficulty (a16, d09, c17 and d04 agree on depth decay); the 82.3% figure is single-task. Reason: 3.5% to 51.8% of correct-answer solutions hide a wrong step. Use the strongest available model or code as checker, not a small verifier.
4. **Control step count and nesting depth with code, not with the model.** G/S (program owns counters). [E] K03. Evidence a08, a12, d04. Productivity fails first and hardest.

### Test first (single-source or contested)

5. **Decompose operator (O3) as least-to-most: list sub-problems, solve in order with earlier answers in context.** O3. [S] K04. Evidence a14, b07, c12, c13. One paper, a retired model. Test on compositional splits at equal tokens against plain CoT.
6. **Ask-sub-question step for multi-hop items (self-ask).** O3. [S] K06. Evidence b08, c14, c15. Measure the gap with and without it.
7. **Offload exact execution to code (PAL).** O (new offload operator; closest existing is O6 change representation). [S] K10, K18. Evidence c18, c19, d05, d04. Cheap to test. Also tests whether the collapse depth moves.
8. **Write each fact in both directions into memory.** memory. [S] K09, K21. Evidence a17, b11, c25, d06, d16. Reversal does not occur for in-context facts, so a memory store that writes both directions at write time should sidestep it. Untested on current models.
9. **Propose many, score in code, answer from the top (Bayesian-style hypothesis proposer).** O/S3. [C] K13. Evidence a19, c21, c20. Strong results are in narrow domains with tuned priors.
10. **Abstract-symbol twin of each item (strip content, keep structure).** G. [C] K14. Evidence b14, b15, b16. Content effects exist in humans too, so a gap is not proof of failure.
11. **Fresh-episode few-shot prompting (MLC analogue).** memory. [S] K05. Evidence a15, c10, c11. Needs training in the original. Low priority.

Not to take: latent-thought medium (K16), mechanistic binding circuits (K11, K22), grokking (K12), the philosophical dispute (K15), infant data (K19). Background only.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup included, per G7). Report the paired difference with a bootstrap CI over items, 3 or more runs per item.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items built from our own operator pairs; exemplar side uses some pairs, test uses held-out pairs (compound split) vs random split | Same scaffold on both splits | Accuracy gap random minus compound split | Gap should exist for the plain model; if near zero for current models, drop the recombination split as a priority |
| T2 | Rare or counterfactual twin per item (base-9 arithmetic, shifted cipher, altered rule) | Plain vs scaffold | Accuracy on twin minus original; thinking tokens on twin | Gap smaller than the 2023 numbers (GPT-4 100.0 vs 23.4); scaffold should not widen it |
| T3 | Irrelevant-clause twin (GSM-NoOp style) | Plain vs scaffold with S1 input hygiene | Accuracy drop | S1 hygiene recovers part of the drop |
| T4 | Multi-hop items (2 to 4 hops) with known sub-facts | Plain CoT vs self-ask vs least-to-most | Composition gap = P(singles right) minus P(composed right) | Gap smaller for decomposition arms; expect less than the 2022 effect on strong models |
| T5 | Arithmetic and counting with large numbers (GSM-HARD style) | CoT vs code-as-thought | Accuracy on the large-number variant | Code arm holds up (61.5 vs 20.1 in 2022); smaller gap on reasoning models |
| T6 | Procedures with 8 to 12 steps, depth varied | In-prompt execution vs code execution | Accuracy by depth; depth at 50% accuracy | Code execution moves the collapse depth up |
| T7 | Sample of correct-answer traces from hard items | Strongest-model step critic vs none | Share of correct-answer traces with a flagged step; accuracy after fixing flagged steps | Share rises with difficulty (3.5% to 51.8%); fixing helps if flags are precise |
| T8 | Facts stored then queried in the reverse direction | One-direction store vs both-direction store | Reverse recall accuracy | Both-direction store near forward accuracy |
| T9 | Items 2x and 4x longer than any exemplar | Plain vs program-controlled counters | Accuracy at 1x, 2x, 4x length; error type (content vs stop) | Program control flattens the decay |
| T10 | Abstract-symbol twin vs content version | Plain vs scaffold | Accuracy gap content minus abstract | Gap exists; scaffold should not widen it |

## 9. What does not transfer, and why

- **The philosophy itself.** LOTH is a claim about human minds. Showing a scaffold is "symbolic" proves nothing about performance. Only the generalisation tests transfer.
- **Training-only fixes.** MLC (a15), Coconut (d10), Csordas setup fixes (a13), JEPA and memory layers (d06) and mechanistic head edits (d08) all need training or weight access. Our agent is a scaffold.
- **Toy-grammar results.** SCAN, COGS, CFQ and PCFG SET are synthetic. The baselines were RNNs and small Transformers trained from scratch. Do not read their accuracy numbers as LLM numbers (critique correction).
- **Hand-written decomposition prompts.** Least-to-most used a grammar-aware prompt built for SCAN (c12). A general task needs the model to find the decomposition, which is a judged step and adds noise (SCHEMA section 1).
- **Infant and animal rule learning.** Small and conditional (g 0.25). It says little about an LLM agent (K19).
- **Bayesian LoT models.** Strong results rest on hand-given primitives and priors tuned on human data (c21, c22). Our open tasks have no such primitives.
- **Mechanistic binding results.** They explain why abstract reasoning works at all. They give the scaffold no lever.
- **Hidden-error rates from math.** ProcessBench is math with annotated steps. Our open-mode tasks have no step gold labels.
- **Old-model numbers.** All LLM effects are from the GPT-3 to o1 era. Current models may differ in either direction.

## 10. Open questions

1. Do current reasoning models (o3, Claude, Gemini 2.5+) still show a compositionality gap on CFQ, COGS, Compositional Celebrities and SCAN length?
2. Does least-to-most or self-ask beat plain CoT at equal tokens on 2025-2026 models, outside SCAN?
3. Does the reversal curse persist in frontier models, and does writing inverse facts in a memory store remove it?
4. How much of the hidden-wrong-step rate remains in tool-using reasoning models, and does a step check reduce it?
5. Where does code-as-thought lose to CoT on current models?
6. What are the exact sample sizes and effects in Marcus 1999 and the animal replications? Have the Fodor-Pylyshyn replies produced any data?
7. Is there a prompt-only version of MLC that reaches comparable systematicity, and has anyone replicated MLC on structural splits?
8. Does Coconut replicate independently? Is there a prompt-level analogue?
9. Is there an LLM benchmark of role-filler independence (variable binding) with scores on compositional tasks?
10. Why did the Press gap fall for GPT-4 but not with GPT-3 scale? Training data, size or post-training?
11. How do the Dziri subgraph-matching reading and the Webb abstract-reasoning reading fit together?

## 11. Sources

[V] opened (full text or page text read), [M] snippet or abstract only, as recorded in the evidence files. Evidence ids in brackets.

- [V] Rescorla, Stanford Encyclopedia, The Language of Thought Hypothesis (2024). https://plato.stanford.edu/entries/language-thought/ [a01-a06]
- [V] Lake and Baroni (2018) Generalization without Systematicity (SCAN). https://arxiv.org/abs/1711.00350 [a07-a09, b01, c01-c03]
- [V] Keysers et al. (2020) Measuring compositional generalization (CFQ). https://arxiv.org/abs/1912.09713 [a10, b03, c05, c06]
- [V] Kim and Linzen (2020) COGS. https://arxiv.org/abs/2010.05465 [a11, b04, c04]
- [V] Hupkes et al. (2020) Compositionality decomposed. https://arxiv.org/abs/1908.08351 [a12, b02, c07-c09]
- [V] Csordas, Irie, Schmidhuber (2021) The devil is in the detail. https://arxiv.org/abs/2108.12284 [a13, b05]
- [V, intro only] Ontanon et al. (2022) Making Transformers solve compositional tasks. https://arxiv.org/abs/2108.04378 [b06]
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 [a14, b07, c12, c13]
- [V] Lake and Baroni (2023) Human-like systematic generalization through meta-learning, Nature. https://www.nature.com/articles/s41586-023-06668-3 and https://pmc.ncbi.nlm.nih.gov/articles/PMC10620072/ [a15, b10, c10, c11]; [M] abstract-only re-read https://doi.org/10.1038/s41586-023-06668-3 [d15]
- [V] Press et al. (2023) Measuring and narrowing the compositionality gap. https://arxiv.org/abs/2210.03350 [b08, c14, c15]
- [V] Dziri et al. (2023) Faith and Fate. https://arxiv.org/abs/2305.18654 [a16, b09, c16, c17]
- [V] Berglund et al. (2023/2024) The Reversal Curse. https://arxiv.org/abs/2309.12288 [a17, b11, c25]; [M] search digest [d16]
- [V] Wu et al. (2023/2024) Reasoning or Reciting. https://arxiv.org/abs/2307.02477 [a18, b12, d02]
- [V] McCoy et al. (2024) Embers of Autoregression. https://arxiv.org/abs/2309.13638 [b13]
- [V] McCoy et al. (2024) o1 and embers of autoregression. https://arxiv.org/abs/2410.01792 [d01]
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 [d03]
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941 [d04]
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [d05]
- [V] Wang and Sun (2026) Is the Reversal Curse a Binding Problem? https://arxiv.org/abs/2504.01928 [d06]
- [M] arXiv 2411.16353, nine frontier LLMs on two-hop reasoning without CoT (search snippet). https://arxiv.org/abs/2411.16353 [d07]
- [V] Yang et al. (2025) Emergent symbolic mechanisms in LLMs. https://arxiv.org/abs/2502.20332 [d08]
- [V] Zheng et al. (2025) ProcessBench. https://arxiv.org/abs/2412.06559 [d09]
- [V] Hao et al. (2024) Coconut. https://arxiv.org/abs/2412.06769 [c26, d10]
- [V] Gao et al. (2023) PAL. https://arxiv.org/abs/2211.10435 [c18, c19]
- [V] Feng and Steinhardt (2024) How do language models bind entities in context? https://arxiv.org/abs/2310.17191 [b17]
- [V] Wang et al. (2024) Grokked transformers are implicit reasoners. https://arxiv.org/abs/2405.15071 [b18]
- [V] Ellis et al. (2020/2021) DreamCoder. https://arxiv.org/abs/2006.08381 [a19, c22]
- [V] Ellis (2023) Human-like few-shot learning via Bayesian reasoning over natural language. https://arxiv.org/abs/2306.02797 [c21]
- [V] Wong et al. (2023) From word models to world models. https://arxiv.org/abs/2306.12672 [c20]
- [V] Lampinen et al. (2024) Language models show human-like content effects on reasoning. https://arxiv.org/abs/2207.07051 [b14]
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196 [b15, c24]
- [V] Gendron et al. (2023) LLMs are not strong abstract reasoners. https://arxiv.org/abs/2305.19555 [b16]
- [V] Mahowald et al. (2024) Dissociating language and thought in LLMs. https://arxiv.org/abs/2301.06627 [c23]
- [V] Rabagliati, Ferguson, Lew-Williams (2019) Abstract rule learning in infancy, meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC6294696/ [d11]
- [V, abstract only] Marcus et al. (1999) Rule learning by seven-month-old infants. https://doi.org/10.1126/science.283.5398.77 [d12]
- [V, abstract only] Marcus, Fernandes, Johnson (2007) Infant rule learning facilitated by speech. https://doi.org/10.1111/j.1467-9280.2007.01910.x [d13]
- [V, abstract only] Murphy, Mondragon, Murphy (2008) Rule learning by rats. https://doi.org/10.1126/science.1151564 [d14]
- [M] Fodor (1975) The Language of Thought. https://mitpress.mit.edu/9780674510302/the-language-of-thought/ [a20]
- [M] Fodor and Pylyshyn (1988) Connectionism and cognitive architecture. https://doi.org/10.1016/0010-0277(88)90031-5 [a21, b19]
- [M] Fodor and McLaughlin (1990) Connectionism and the problem of systematicity. https://doi.org/10.1016/0010-0277(90)90032-8 [a22, b21] (DOI last digit disputed between records; check before citing)
- [M] Smolensky (1990) Tensor product variable binding. https://doi.org/10.1017/S0140525X00052432 [a23]
- [M] Marcus (1998, 2001) Rethinking eliminative connectionism; The Algebraic Mind. https://doi.org/10.1006/cogp.1998.0694 [a24]
- [M] Piantadosi, Tenenbaum, Goodman (2012, 2016) Bayesian LoT models. https://doi.org/10.1016/j.cognition.2011.11.001 [a25]
- [M] Quilty-Dunn, Porot, Mandelbaum (2023) The best game in town, BBS. https://doi.org/10.1017/S0140525X22002849 [a26]
