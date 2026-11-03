# Theories of mental representation: deep document

*Subfield D06.01. Scope: what it is for a state to carry content (Fodor, Dretske, Millikan, Block, SEP "Mental Representation"), and every LLM or interpretability study that tests or uses these ideas. Schema link: S2 REPRESENT, the question of what a good representation preserves. Evidence ids (a01..d18) and claim ids (D06.01-K01..K28) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Corrections from critique.md are applied. Philosophy is known only through SEP summaries and secondary papers; the primary books were not opened.*

## 1. What it is

Philosophy of mental representation asks one question: what makes an inner state be about something? A neuron pattern, a vector, a line in a scratchpad can all correlate with the world. Only some of them have content: they say the world is a certain way, and they can be wrong.

The representational theory of mind (RTM) says that beliefs and desires are relations to inner representations, and that reasoning is a sequence of such states (a01). Content theories try to say, without circularity, what fixes the content of a representation. There are four families (K01):

1. **Informational (causal).** Content is what reliably causes the token. Dretske 1981, 1988; Fodor 1987, 1990.
2. **Teleological (consumer).** Content is what the state is for: the condition that must hold for the consumer subsystem to do its job. Millikan 1984, 2004; Neander; Papineau; Shea 2018.
3. **Conceptual role.** Content is fixed by inferential or computational relations to other representations. Block 1986, 1998; Piantadosi and Hill for LLMs.
4. **Resemblance and structural.** Content is fixed by a structural match between the representation and what it stands for. Mental imagery debate; Shea's varitel semantics counts structure too (a26).

No theory is accepted. Each has a named problem: the disjunction problem (informational), Swampman and functional indeterminacy (teleological), holism (conceptual role), and indeterminacy of interpretation (Dennett, Churchland; a23).

Why this matters for our agent. S2 asks the model to restate the problem in a form that helps later steps. The philosophy gives three tests for whether a restatement is a real representation and not just words:

- (a) **Information:** it carries information about the task (it matches the source).
- (b) **Consumer use:** later steps actually use it, so editing it changes the output.
- (c) **Misrepresentation:** it can be wrong, and the system can detect that.

Milliere and Buckner state exactly these three criteria for activation patterns (c09; K17). Most LLM work tests (a), some tests (b), almost none tests (c). The mapping from philosophy to the agent is our own synthesis (a24) and is untested as a whole.

## 2. History and theories in depth

**Language of Thought (Fodor 1975).** The neural symbol system is structured like a language. Productivity and systematicity follow from recursive combination of a finite stock of primitives (a02). Fodor and Pylyshyn (1988) argued that connectionist nets need this structure to explain why a mind that can think "John loves Mary" can think "Mary loves John" (a07, not opened; cited via Milliere and Buckner, a21). Transformers re-opened this debate (a21).

**Informational semantics (Dretske 1981, Fodor 1987).** Dretske built content on information theory: a state carries the information that F if it reliably co-varies with F. Function then picks which cause counts (a04). Core objection: information is everywhere. Tree trunks carry their age, smoke carries fire, a thermostat carries temperature, and none of these represent (a03, b02, K02). So information is necessary, not sufficient.

**Disjunction problem (Fodor 1984).** If "X" is caused by dogs and sometimes by foxes, why does it mean dog and not dog-or-fox? Misrepresentation needs a way to say "this token is an error" (a04, d16). Fodor's fix is asymmetric dependence: fox-caused tokens depend on dog-caused ones, not the reverse (a03). This is the philosophical form of a probe problem: a probe decodes "something", but which thing is it about? (a25).

**Teleosemantics (Millikan 1984, 2004; Neander; Dretske 1988).** A representation is a message from a producer subsystem to a consumer subsystem. Its content is the world condition that must hold for the consumer to perform its function in the normal way (a05). Selection history (evolution, and on many accounts learning) fixes the function (d17). Frog case: contents proposed include "frog food" (Millikan), "small dark moving thing" (Neander), "small dark moving frog food" (Agar), "there's a fly" (Martinez). That the field cannot agree is the functional indeterminacy problem (a05, d17).

**Swampman (Davidson 1987).** An accidental physical duplicate with no history has, on history-based teleosemantics, no content (a06). Millikan accepts this for strict history; others allow learning to count. For LLMs the question is whether pre-training, instruction tuning and RLHF count as selection. Mollo and Milliere (2023/2025) say yes, if the tuning gives states a function beyond mimicry (c05, c06, d18). They give no experiment. Note: in the text searched they do not use the words "Swampman" or "disjunction"; those links are SEP-level concepts (critique).

**Conceptual role semantics (Block 1986, 1998).** Content is fixed at least partly by relations among representations: holist (all), molecular (some), atomist (none) variants (a22). Holism threatens shared content across people or models. Piantadosi and Hill (2022) use this to argue LLMs plausibly have meaning without reference, since reference does not fix concepts (postage stamp, Frege, Wittgenstein examples; a20, b19).

**Resemblance and imagery.** 1970s response-time studies found that mental manipulation time varies with the size and orientation of the imagined figure. Kosslyn read this as pictorial; Pylyshyn as descriptive (b03; qualitative, no N in SEP).

**The LLM debate.**
- Bender and Koller (2020): a system trained only on form cannot learn meaning, defined as the relation of form to communicative intent. Octopus test. No experiments (a19).
- Piantadosi and Hill (2022): conceptual role (a20).
- Mollo and Milliere: grounding needs causal-informational relations plus a selection history (c05).
- Mandelkern and Linzen (2024): externalist reference. Words refer through the natural history of their use, not through the speaker's experience (c07).
- Mitchell and Krakauer (2023) report a survey of 480 NLP researchers: 51% agreed a text-only model could understand language in some non-trivial sense, 49% disagreed (b20).

These papers cite each other, so independence is low (critique). The data below do not settle the dispute.

**Interpretability turns the criteria into measurements.** Probes test (a). Interventions test (b). Behavioural coherence tests (Myhill-Nerode compression and distinction) test whether the state is a state at all. Misrepresentation (c) is rarely tested (a24, K17).

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. Numbers marked "figure" were not extracted.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A GPT trained only on Othello move text predicts legal moves | Top-1 illegal-move rate 0.01% (20M synthetic games), 5.17% (championship data), 93.29% (untrained net). Held-out opening test 0.02% | Li et al. 2023 (a08, b04, c01) | E |
| Its board is readable with a nonlinear (2-layer MLP) probe, not a linear BLACK/WHITE probe | Linear error never below about 20% (20.4-23.1% by layer); always-guess baseline 52.95% (main text) or about 47% (appendix; source disagrees with itself); nonlinear error 1.7%; random net nonlinear 25.5-26.4% | Li et al. (a09, b24) | E |
| Editing the activation changes predicted moves (causal use) | 0.12 errors (natural positions) and 0.06 (unnatural) vs 2.68 and 2.59 for null edit; 1000 cases each | Li et al. (a10) | E |
| The board is linear once coded mover-relative (MINE/YOURS/EMPTY) | Linear BLACK/WHITE about 75%; nonlinear BLACK/WHITE peak 98.7%; linear MINE/YOURS peak 99.6% (layer 7), 99.5% at layer 8, 90.8-90.9% at layer 1. Linear intervention 0.10 vs nonlinear 0.12 vs null 2.72 errors | Nanda et al. (a11, b05, c02); Hazineh et al. (b06) | E |
| Chess GPT on human games has board and latent skill | Legal moves 99.8% (16-layer), 99.6% (8-layer); linear board probe 99.6% (random net 74.7%); win rate vs Stockfish level 0 of 64% (16-layer), 46% (8-layer); skill probe 90.5% vs 69.3% random; edited-board legal moves 92.0% with intervention vs 40.5% without | Karvonen 2024 (a12, b07, c19) | E |
| LLMs linearly encode space and time | Llama-2-70b linear out-of-sample R2: world 0.911, USA 0.864, NYC 0.359, historical figures 0.835, entertainment 0.885, headlines 0.746. 7B/13B/70B world 0.881/0.896/0.911; NYC 0.219/0.237/0.359. MLP probe adds little | Gurnee and Tegmark 2024 (a13, b09, c10) | E |
| Truth has a roughly linear direction that sharpens with scale | Mass-mean probes beat logistic regression and CCS in 7 of 8 intervention conditions; LLaMA-2-70B many NIEs near 1, 13B far lower; probes trained on larger_than + smaller_than exceed 95% on Spanish-English translation (13B, 70B) | Marks and Tegmark 2024 (a14, b10, c16) | C |
| Probe accuracy can hide probe capacity | POS tagging, MLP probe: task 97.3%, control 92.8%, selectivity 4.5. Linear probe: 97.2%, 71.2%, selectivity 26.0 | Hewitt and Liang 2019 (b15, c18) | E (method) |
| Decodable is not used | High probe accuracy shows information present, not used; controls and interventions needed | Belinkov 2022 (b14); Milliere and Buckner (b21, c09) | E |
| Unsupervised truth probes find the salient feature, not knowledge | With distractor insertion (Banana/Shed), ground-truth accuracy falls to 50% (chance) for CCS, PCA, K-means; CCS bimodal across seeds. CCS originally about 4% above zero-shot (10 QA sets, 6 models) | Farquhar et al. 2023 (b12); Burns et al. 2022 (b11) | E |
| Supervised and CCS truth probes fail on negation | LLaMA-30B: five of six supervised probes worse than chance on negated sets; CCS reconstruction 50-57% | Levinstein and Herrmann 2023 (c14) | E |
| Negation failure shrinks with scale and diverse training | Training on cities + neg_cities fixes negated translation; larger models generalise better | Marks and Tegmark (b23, c16) | C |
| Truth correlates with text likelihood | cities r = .85, sp_en_trans r = .95; not for negated sets | Marks and Tegmark (c16) | S |
| Accuracy and probes can coexist with an incoherent world model (taxi) | Next-token validity 1.00, state probe 0.91-0.99, compression precision 0.10 (shortest paths), 0.05 (noisy), 0.50 (random walk); distinction recall 0.35-0.99. Shortest-path model valid traversals under detours 0.99, 0.69, 0.08, 0.00, 0.00; random-walk model 0.99, 0.99, 1.00, 0.97, 0.74 | Vafa et al. 2024 (a16, b08, c03) | E |
| Othello model trained on real games fails the same coherence test | The model Li et al. read as a world model passes probes but fails compression and distinction | Vafa et al. (c04) | C (vs Li) |
| Prompted LLMs have weak coherence on a seating puzzle | GPT-4: compression 0.21 (SE .04), distinction 0.56 (.03); GPT-3.5: compression 0.33, distinction 0.18; GPT-4 fully accurate on specified examples | Vafa et al. (c04) | E |
| LLMs as text-game simulators | GPT-4 simulates 77.1% of action-driven transitions, at most 49.7% of environment-driven; game progress 92.1% with rules, 61.5% without; 2954 tuples | Wang et al. 2024 (c21) | S |
| Models define concepts, fail to use them (potemkins) | Definitions correct 94.2%; potemkin rate 0.55 / 0.40 / 0.40 (classify / generate / edit); GPT-4o 0.53/0.38/0.35; Claude-3.5 0.49/0.23/0.29; DeepSeek-R1 0.47/0.39/0.52; Qwen2-VL 0.66/0.62/0.52; MMLU-derived lower bound 0.62 | Mancoridis et al. 2025 (c22, c23) | S |
| Explicit world model plus search helps small models | Blocksworld 2/4/6 step: CoT LLaMA-33B 0.17/0.02/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42; CoT GPT-4 0.50/0.63/0.40 (GPT-4 beats RAP(10) at 6 steps) | Hao et al. 2023 (c20) | S |
| Belief-state geometry in sequence models | RRXOR: belief-state geometry R2 0.95 vs next-token geometry 0.31 | Shai et al. 2024 (a15) | S |
| Representations converge with scale, weakly | Mutual nearest-neighbour alignment across 78 vision models rises with LM score; effect sizes about 0.1-0.3. Colour: text baselines already high (fastText 0.23, PMI 0.11-0.17). The RSA range 0.16-0.33 in a18 is from a garbled table; do not cite | Huh et al. (a17, b17, c13); Abdou et al. (b16, c12) | C |
| Self-conditioning in long runs | Qwen3-32B falls below 50% within 15 turns despite near-perfect first step; error injection 0-100% lowers accuracy at turn 100 in proportion; thinking mode removes it; single-turn horizon GPT-5 2176 steps, Claude-4 Sonnet 432, Grok 4 384, Gemini 2.5 Pro 120 | Sinha et al. 2025 (d01, d02) | C |
| Puzzle collapse beyond a complexity threshold | Even with the algorithm given, collapse at about the same N; Claude 3.7 thinking near-perfect at Hanoi N=5 but fails River Crossing N=3 | Shojaee et al. 2025 (d03) | C |
| Intrinsic self-correction hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GPT-4 GSM8K 95.5 to 91.5, 89.0; GPT-4 HotpotQA 49.0 to 49.0, 43.0; oracle label: GPT-3.5 GSM8K 75.9 to 95.5, GPT-4 95.5 to 97.5 | Huang et al. 2024 (d04) | E |
| Finding the mistake is the bottleneck | BIG-Bench Mistake, 2186 traces: GPT-4 39.80 (trace-level), 52.87 (direct step-level), 43.40 (CoT step-level); GPT-4-Turbo 30.13 and 48.33; GPT-3.5-Turbo 10.44, 14.78, 14.31. Given location, backtracking helps on all 5 tasks | Tyen et al. 2024 (d05) | E |
| Stated reasoning can omit the real cause | Biasing features cut accuracy by up to 36% on 13 BBH tasks (GPT-3.5, Claude 1.0); CoT justifies the biased answer | Turpin et al. 2023 (d07) | S |
| Distractors cut accuracy; voting recovers most | GSM-IC code-davinci-002 COT micro 72.4%, macro 6.0%; LTM 77.5/18.0; ignore-irrelevant instruction 77.8 (COT), 80.6 (LTM); SC (20 samples) COT 88.1, LTM 93.4 micro, LTM+SC macro 45%; 0-COT SC gain 35.5 points; correct answer within 20 samples for 99.7% | Shi et al. 2023 (d08) | E |
| Compact symbolic state helps where text is ambiguous | Brick World GPT-3.5 31.8% to 92.6% (+60.8) with up to 65.8% fewer input tokens; SPARTUN GPT-3.5 47.1 to 49.4 (+2.3), GPT-4 69.8 to 72.6 (+2.8); intermediate tokens 198 to 167 | Hu et al. 2024 (d10) | C |
| In-context entity tracking needs code-trained models | Only GPT-3.5 (code-trained) beat copying the initial state; copy baseline right 62.7% on Alchemy | Kim and Schuster 2023 (d11) | S |
| LLMs do not keep weighted hypotheses | Flight preference task, 624 simulated users, 5 rounds: Bayesian assistant 81%; off-the-shelf models about 36-58%, plateau after round 1; CoT, 30 rounds, base models no help; Bayesian-tuned models agree with Bayes about 80% | Qiu et al. 2025 (d09) | S |
| Belief tracking is causally traced up to 405B | Mechanisms in Qwen2.5-14B, Llama-3-70B, Llama-3.1-405B; probes above 75% on head subsets (Mistral-7B); belief-direction intervention about 0.97 vs about 0.68 random (table garbled) | Prakash et al. 2025 (d12); Zhu et al. 2024 (d13) | S |
| Othello alignment across seven LMs | Up to 99% unsupervised grounding between final-layer representations | Yuan and Sogaard 2025 (d14) | S |
| Belief depth depends on method | Prompting and synthetic-document fine-tuning generalise; under adversarial system prompt, critique and four-turn debate, prompting fails and SDF persists except for egregiously false facts (open-ended belief 80% to 50% in one case) | Slocum et al. 2025 (d15) | S |

## 4. Mechanisms and models

**M1. Probe with controls (to read a representation).**
1. Collect activations at a layer for inputs with known labels (board squares, coordinates, truth).
2. Train a linear probe (ridge or logistic) and, as a check, a small MLP.
3. Train a control task (random labels per word type, Hewitt and Liang) and report selectivity = task accuracy minus control accuracy.
4. Train the same probe on a randomly initialised network. Compare (chess: 99.6% vs 74.7%).
5. Report out-of-sample, with block hold-out where entities cluster (Gurnee and Tegmark).
Caveat: this tests only criterion (a).

**M2. Intervention (to test use).**
1. Find the probe direction. 2. Add or subtract it at the layer so the decoded value flips. 3. Measure whether the output changes as the edited state predicts (Othello: 0.12 errors vs 2.68 null). 4. Use a mass-mean (difference-in-means) direction, which is more causal than logistic regression at equal accuracy (Marks and Tegmark). Report normalised indirect effect.

**M3. Actor-relative coding.** Code each board cell as MINE/YOURS/EMPTY relative to the player to move. This turned a "nonlinear" board into a linear one (about 75% to 99.6%). Lesson for S2: store state in the frame the consumer step needs.

**M4. Myhill-Nerode coherence metrics (Vafa et al.).**
- Compression: two sequences that reach the same true state must allow the same continuations. Precision is measured over sequence pairs the model treats as equal.
- Distinction: two sequences that reach different true states must allow different continuations. Recall is measured over truly different pairs.
- Test sets are built from boundary sequences (shortest differing suffixes). Detour tests: add random detours (the same state reached by a longer route) at rising rates and count valid traversals.
Implementation for the agent: take an item, produce two different histories that end in the same state, and check that the agent's S2 and its next action match.

**M5. Belief-state geometry (Shai et al.).** For a hidden Markov process the optimal predictor keeps a belief over hidden states; the set of reachable beliefs forms a fractal-like simplex geometry. Fit a linear map from activations to belief coordinates (RRXOR R2 0.95). Engineer reading: a state should hold weights over hidden causes, not one best guess.

**M6. Weighted-hypothesis state (from Qiu et al., engineering form).**
```
H = {h_i: w_i}            # hypotheses about the hidden variable, w sums to 1 (code normalises)
on observation o: w_i <- w_i * P(o | h_i); renormalise     # likelihood by rule, in code
act on argmax_i w_i; keep H for the next step
```
The model proposes hypotheses and likelihood tags; code does the arithmetic. Prompt-only versions were not tested; fine-tuning on Bayesian outputs reached about 80% agreement (d09).

**M7. Compact symbolic state (Chain-of-Symbol).** Replace prose intermediate steps with symbols for objects and relations. Fewer tokens (up to 65.8% fewer input tokens) and, on a synthetic spatial task, +60.8 points; on natural spatial QA only +2.3 to +2.8.

**M8. Use-check (our proposal from potemkin results).** After S2 states a concept or rule, give a fresh instance (built by code or an independent instance) and ask the model to apply it. Compare with the stated rule. A mismatch flags a potemkin. Not tested; K14.

**M9. Counterfactual edit of the scratch state (consumer test).** Copy the S2 text, change one slot, re-run the next step. If the output does not move, S2 was not used (criterion b). If it moves as predicted, it was used. This is the prompt-level analogue of M2.

**M10. Re-derive vs copy-forward.** In a multi-step run, either (A) copy the previous state forward and update it, or (B) re-derive the state from the source problem each step. Self-conditioning (d01) predicts A propagates errors. Not tested.

## 5. What holds up

**Replicated or confirmed.**
- Othello board state: Li et al. found it; Nanda et al. and Hazineh et al. (independently, even in a 1-layer model) found it linear with MINE/YOURS coding; Yuan and Sogaard found similar representations in seven LMs. The linear-vs-nonlinear dispute was a coding artefact (K06).
- Chess: extension to real human games (Karvonen), with a latent skill variable.
- Linear space and time: robust to prompt variants and to entity type; the main loss comes from block hold-out (c11). Larger models are better; fine grain (NYC) stays weak at 70B (R2 0.359).
- Decodable is not used: Hewitt and Liang, Belinkov, Milliere and Buckner agree. Probe accuracy needs controls and interventions (K03).
- Unsupervised truth discovery is refuted for CCS by Farquhar et al. and Levinstein and Herrmann (50% under distractors; 50-57% on LLaMA-30B).
- Same-model self-review is weak: Huang et al. and Tyen et al. agree (K22).

**Contested or failed.**
- Truth direction: Marks and Tegmark say it is linear and generalises; Levinstein and Herrmann say it fails on negation; Marks and Tegmark answer that negation failure shrinks with scale and with training on negations.
- Li et al. versus Vafa et al.: same Othello model. It passes probe and intervention criteria but fails behavioural compression and distinction when trained on real games. The criteria differ; both can be true.
- Platonic convergence versus weak colour numbers: alignment rises with scale but absolute values are small and baselines are already high.
- Self-conditioning (Sinha) versus the "illusion of thinking" (Shojaee): both see long-run failure; they disagree on cause (execution vs reasoning limits). Critics also cite output-token limits and unsolvable instances for Shojaee.
- Othello baseline: always-guess error is 52.95% in the main text and about 47% in the appendix.

**Moderators.**
- Probe expressiveness (MLP vs linear) changes the story (selectivity 4.5 vs 26.0).
- Coding frame (absolute vs mover-relative).
- Scale (truth direction; spatial fine grain; negation).
- Data diversity (negations in training).
- Training data: synthetic games give 0.01% illegal moves, championship games 5.17%.
- Distractor features (unsupervised methods fall to chance).
- Code training (entity tracking in-context).
- Fine-tuning versus prompting (belief depth; Bayesian teaching).
- Domain: symbolic gain 60.8 points on a synthetic task, 2.3-2.8 on natural spatial QA.

**Interventions that worked.**
- Mover-relative frame; activation edits; mass-mean directions.
- Giving the error location (oracle) so correction works (d04, d05).
- Sliding context window and thinking mode against self-conditioning (d01, d02).
- Self-consistency (20 samples) and an ignore-irrelevant instruction (+5 to +8 points) against distractors (d08).
- Compact symbolic state on synthetic spatial tasks (d10).
- Fine-tuning on Bayesian outputs (d09).

**Interventions that did not work.**
- Self-verify prompts for self-conditioning (partial; overthinking; d02).
- Intrinsic self-correction (d04).
- CoT, 30 rounds or base models for belief updating (d09).
- Giving the algorithm in the prompt for puzzle collapse (d03).
- Prompted facts under adversarial pressure (d15).

**Gaps in the whole literature (critique).** Open-weight models only for interpretability; no frontier prompted-model result on S2-style restatements except Vafa (seating) and potemkin; no scaffold-level study measuring whether better stated representations raise accuracy at equal tokens; the philosophical papers give no numbers.

## 6. Language models

**What interpretability shows (open models).**
- Small GPTs trained on game text build board states (Othello, chess) that are causally used. Illegal-move rate depends on data: 0.01% synthetic vs 5.17% championship.
- Llama-2 encodes places and dates linearly; R2 rises with size (NYC 0.219, 0.237, 0.359 for 7B, 13B, 70B).
- Truth is partly linear at scale; negation and distractors break weaker probes and unsupervised methods.
- Belief tracking about other agents is linear-readable and causally traced up to Llama-3.1-405B (d12, d13). No result on closed frontier models.

**What behaviour shows (prompted models).**
- Coherence is weak on a seating puzzle: GPT-4 compression 0.21, distinction 0.56; GPT-3.5 0.33 and 0.18 (c04).
- Text-game simulation: GPT-4 77.1% of action-driven transitions, at most 49.7% of environment-driven. Environment-driven changes are lost unless stated (c21).
- Potemkins: 94.2% correct definitions against use-failure rates of 0.55 / 0.40 / 0.40 across models; Claude-3.5 lowest on generation (0.23) and editing (0.29); DeepSeek-R1 worst on editing (0.52); Qwen2-VL worst overall (c22).
- Long runs: first step near perfect, then error compounds as the model reads its own past mistakes. Qwen3-32B below 50% within 15 turns on a synthetic task. Larger non-thinking models self-condition at least as much. Thinking mode removes the effect (Qwen3). Single-turn horizon: GPT-5 2176, Claude-4 Sonnet 432, Grok 4 384, Gemini 2.5 Pro 120 (d01). The task is Markovian and synthetic.
- Hidden-variable tracking: prompted models plateau near a single best guess (36-58% vs Bayes 81%); CoT does not help; fine-tuning does (d09).
- Self-review: GPT-4 finds the first mistake in 39.8-52.9% of cases (others' traces); intrinsic correction lowers accuracy; locating hints fix it (d04, d05). All 2023-era.
- Reasoning text: biased features cut accuracy by up to 36% with unmentioned influence (d07).
- Distractors: macro accuracy 6.0% base, 45% with LTM+SC (d08).

**What changed it, by how much.**
- Mover-relative coding: about 75% to 99.6% linear probe accuracy.
- Training data realism: 0.01% vs 5.17% illegal moves.
- Scale: spatial R2 and truth generalisation rise with size.
- Symbolic state: +60.8 points (synthetic), +2.3/+2.8 (natural).
- RAP world model: Blocksworld 6-step 0.00 to 0.26/0.42 for LLaMA-33B; GPT-4 CoT already 0.40.
- Self-consistency: macro 18% to 45% on GSM-IC with LTM.
- Fine-tuning for Bayes: about 80% agreement with Bayes; prompting no gain.
- Thinking mode: removes self-conditioning in Qwen3.

**Caveat.** Most numbers come from 2022-2024 models or small open models. Nothing here measures a frontier prompted model with an S2 scaffold at equal tokens.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **S2 must be judged by use, not by wording** [E]. Information is not enough; a restatement must change what later steps do. Rule: no step may rely on S2 content that no later step reads. Part: S2 / G. Evidence: K02, a03, b02, c25, a26. A design rule, not a new element.
2. **Do not trust a self-report of having represented something** [E]. Decodable is not used; reasoning text can omit the cause. Matches G10. Part: G. Evidence: K03, b14, b15, c18, c09 (d07 single-source).
3. **Located feedback beats self-review** [E]. Models find their own mistakes poorly (39.8-52.9%) but fix them well once shown. Confirms G2. Part: G. Evidence: K22, d04, d05.
4. **Do not use internal agreement as truth** [E]. Unsupervised consistency probes find the salient feature (50% under distractors); behavioural self-consistency helps but is not proof. Confirms G4. Part: G. Evidence: K10, b11, b12, c14, K24, d08.
5. **Keep distractors out of S2** [E]. Irrelevant sentences cut macro accuracy to 6.0%; an ignore-irrelevant instruction gave +5 to +8 points; voting recovers more. Supports S1 input hygiene. Part: S1/S2. Evidence: K24, d08.
6. **Accuracy does not show a coherent state** [E]. Models can have next-token validity 1.00 and compression precision 0.05-0.50. So perturbation (detour) items belong in our checks. Part: S2 / O (checks). Evidence: K12, K13, a16, b08, c03, c04.

### Test first

| # | Item | Part | Status | Evidence ids | Why not add yet |
|---|---|---|---|---|---|
| T1 | Use-check: apply the stated concept to a fresh instance | S2 / G | [S] | K14, c22, c23 | Potemkin gap measured, no fix tested |
| T2 | Re-derive S2 from source each step vs copy forward | S2 / memory | [C] | K21, d01, d02, d03 | Cause disputed; synthetic tasks |
| T3 | Actor-relative vs absolute restatement (mover-relative frame) | S2 | [S] | K06, a11, b05, b06, c02 | Probe result only; no text-task study |
| T4 | Typed slots vs free restatement vs none | S2 | [C] | K25, d10, d11 | Frontier models untested; natural gain small |
| T5 | Weighted hypothesis set for hidden variables | S2 | [S] | K19, K26, d09, a15 | Fine-tuning evidence only |
| T6 | Explicit environment-change slot | S2 / S5 | [S] | K13, c21 | One model family (49.7% figure) |
| T7 | Counterfactual edit of S2 (consumer test) as a check | G / S4 | [S] | K03, a10, K23 | Prompt-level analogue not run |
| T8 | Seeded misstatement detection: slot vs source line | G / S5 | [S] | K22, d05, K17 | Models are 2023-era |
| T9 | Pressure test of stated S2 content before reliance | G | [S] | K20, d15 | Facts, not task representations |
| T10 | Explicit next-state prediction before acting | S2 / O | [S] | K18, c20 | Gain model-dependent; GPT-4 CoT beats RAP(10) at 6 steps |

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, G7). Report accuracy with confidence intervals, tokens, and failure type. Use at least two models.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 use-check | Concept-application items (define, then classify, generate, edit) in 3 domains | A: S2 only. B: S2 + apply to a fresh code-built instance, checked by an independent instance. C: plain model | Potemkin rate (error given correct definition); final accuracy | Lower potemkin rate (baseline 0.40-0.55 on older models); net gain only if check tokens < gain |
| T2 re-derive vs copy | 20-60 step state-tracking tasks (running state, inventory, board), early error injected in half the runs | A: copy previous S2 forward. B: re-derive S2 from the source each step. C: no S2 | Accuracy at step k; carry-over rate of the injected error | B lower carry-over than A; gain grows with length |
| T3 frame | Turn-taking games and tasks with two actors | A: absolute labels. B: actor-relative (MINE/YOURS) | Accuracy; slot error rate | Small positive for B on role-flipping tasks; near zero elsewhere |
| T4 typed slots | State tracking, spatial relational QA, Blocksworld-style planning, natural SPARTUN-like items | A: typed slots (entities, relations, hidden variables). B: free restatement. C: none | Accuracy at equal tokens | Large on synthetic or ambiguous tasks, small on natural (older models +2.3 to +2.8); frontier may show near zero |
| T5 hypotheses | Hidden-preference or hidden-rule tasks over 5 rounds | A: single best guess. B: weighted list updated by code rule. C: free CoT | Accuracy by round; agreement with Bayes | B closer to Bayes than A or C (baseline 36-58% vs 81%) |
| T6 env change | Text-game or inventory items with environment-driven events | A: free S2. B: S2 with a required "what changes without my action" slot | Transition accuracy on environment-driven events | Gain (baseline at most 49.7%) |
| T7 consumer edit | Any multi-step item | Edit one slot in S2 and rerun the next step | Output change rate for relevant vs irrelevant edits | Used S2: high change on relevant edits, low on irrelevant. Low change means S2 is decoration (prune it) |
| T8 misstatement | Items with a seeded S2 error (wrong quantity, wrong relation) | A: "is this restatement wrong?" B: "does slot k match source line j?" C: independent re-derivation compared by code | Detection rate; false alarm rate | B and C much higher detection than A (baseline 39.8-52.9%) |
| T9 pressure | Items with S2 content, then a contradicting hint | A: rely on S2. B: ask for the source line, then contradict, then rely | Accuracy; flip rate | B reduces flips to wrong content, small token cost |
| T10 predict state | Blocksworld-style planning, 2/4/6 steps | A: CoT. B: explicit next-state prediction per step | Success by plan length | Larger gain on longer plans for smaller models; none for frontier |
| Distractor | GSM-IC style items | A: free S2. B: S2 with relevant quantities only. C: plain | Macro accuracy | B > A on distractor items |
| Detour | Same final state reached by different routes | S2 on vs off | Rate of different next actions on the same state | S2 lowers inconsistency; failures remain on long runs |

## 9. What does not transfer, and why

- **Probe results do not transfer to prompts.** Probes read weights of open models; our agent is prompted and may be closed. Linear-direction findings cannot be used to build a verifier (K09 is contested).
- **Small-GPT game models are not LLMs.** Othello and chess GPTs are trained on one domain; their legal-move rates (0.01% illegal, 99.8% legal) say nothing about prompted accuracy.
- **Philosophical content theories are not testable here.** Selection history, Swampman, disjunction: no experiment tests them for LLMs (K16, K27). Only the use-by-consumer and robustness-under-pushback parts are testable.
- **Platonic convergence and colour alignment** (K15) do not change the scaffold.
- **Spatial R2 values** (K08) are for open-weight Llama-2 and say little about prompted coordinate answers.
- **RAP gains** came from LLaMA-33B; GPT-4 CoT was already at 0.40 on 6-step Blocksworld.
- **Chain-of-Symbol gains** depend on a synthetic task with ambiguous text; natural tasks gain about 2-3 points, and symbol formats are task-specific.
- **Self-conditioning numbers** come from a synthetic Markovian running-sum task; real tasks have long-range dependencies where dropping history hurts.
- **2022-2023 self-review and distractor numbers** come from older models; later RL-trained models may behave differently.
- **Fine-tuning results (Bayesian teaching, SDF)** are training, not scaffolding. We do not train.
- **The imagery debate** is qualitative; it gives no operational rule for S2.

## 10. Open questions

1. Does an explicit typed S2 raise accuracy at equal tokens for frontier prompted models over free restatement? (Gap 1: no direct study.)
2. Does an apply-to-fresh-instance check close the potemkin gap, and at what token cost? (Gap 2.)
3. Do compression and distinction failures occur in prompted frontier models on long tasks, and does re-stating state each step fix them? (Gap 3: failures measured, fix not.)
4. Does actor-relative vs absolute restatement help on text tasks? (Gap 4.)
5. Can an LLM detect misrepresentation in its own earlier restatement without an outside signal? Evidence says poorly (2022-2023 models); no frontier figure. (Gap 5.)
6. Do the Othello and chess world models replicate in closed frontier models? (Gap 6: extended in open models, never contradicted, never tested in closed ones.)
7. Does self-consistency fail under distractor features behaviourally the way probes do? Partly (macro 45% with LTM+SC). (Gap 7.)
8. How much does a weighted-hypothesis S2 add over a single guess in prompt-only form? (Gap 8.)
9. Does selection history ground LLM states? Primary texts by Fodor, Dretske, Millikan and Block remain unopened; no fine-tune-vs-prompt test of grounding exists. (Gap 9.)
10. Which of the three criteria (information, use, misrepresentation) best predicts that a restatement improves the answer? No one has measured it.
11. Does the Li vs Vafa split (probe pass, coherence fail) appear in scaffolded agents: a good-looking S2 with incoherent continuations?

## 11. Sources

[V] = opened (read page or PDF text). [M] = snippet, abstract, or secondary citation only.

**Philosophy and reviews**
- [V] Pitt (2020) SEP Mental Representation. https://plato.stanford.edu/entries/mental-representation/ (a01, a02, a03, a22, a23, b01, b02, b03, c25)
- [V] SEP Causal Theories of Mental Content. https://plato.stanford.edu/entries/content-causal/ (a04, d16)
- [V] Neander, SEP Teleological Theories of Mental Content. https://plato.stanford.edu/entries/content-teleological/ (a05, a06, a26, d17)
- [M] Fodor and Pylyshyn (1988) Connectionism and cognitive architecture; seen through Milliere and Buckner. https://arxiv.org/abs/2401.03910 (a07)
- [M] Fodor 1975, 1984, 1987, 1990; Dretske 1981, 1988, 1995; Millikan 1984, 2004; Block 1986, 1998; Davidson 1987; Shea 2018: known only via SEP and secondary papers.
- [V] Bender and Koller (2020). https://aclanthology.org/2020.acl-main.463/ (a19, b18, c08)
- [V] Piantadosi and Hill (2022). https://arxiv.org/abs/2208.02957 (a20, b19)
- [V] Milliere and Buckner (2024) A Philosophical Introduction to Language Models, parts I and II. https://arxiv.org/abs/2401.03910 and https://arxiv.org/abs/2405.03207 (a21, b21, c09)
- [V] Mitchell and Krakauer (2023). https://arxiv.org/abs/2210.13966 (b20)
- [V] Mollo and Milliere (2023/2025) The Vector Grounding Problem. https://arxiv.org/abs/2304.01481 (c05, c06, d18)
- [V] Mandelkern and Linzen (2024). https://arxiv.org/abs/2308.05576 (c07)

**World models and probes**
- [V] Li et al. (2023) Emergent World Representations. https://arxiv.org/abs/2210.13382
- [V] Nanda, Lee, Wattenberg (2023). https://arxiv.org/abs/2309.00941
- [V] Hazineh, Zhang, Chiu (2023). https://arxiv.org/abs/2310.07582
- [V] Karvonen (2024) chess. https://arxiv.org/abs/2403.15498
- [V] Yuan and Sogaard (2025) Othello World Model Hypothesis. https://arxiv.org/abs/2503.04421
- [V] Gurnee and Tegmark (2024). https://arxiv.org/abs/2310.02207
- [V] Marks and Tegmark (2024). https://arxiv.org/abs/2310.06824
- [V] Burns et al. (2022). https://arxiv.org/abs/2212.03827
- [V] Farquhar et al. (2023). https://arxiv.org/abs/2312.10029 (exact 50% figure confirmed only in text near the setup)
- [V] Levinstein and Herrmann (2023). https://arxiv.org/abs/2307.00175 (earlier snippet b13 was [M]; c14 opened)
- [V] Shai et al. (2024). https://arxiv.org/abs/2405.15943
- [V] Vafa et al. (2024). https://arxiv.org/abs/2406.03689
- [V] Huh et al. (2024). https://arxiv.org/abs/2405.07987
- [V] Abdou et al. (2021). https://arxiv.org/abs/2109.06129
- [V] Belinkov (2022). https://arxiv.org/abs/2102.12452
- [V] Hewitt and Liang (2019). https://arxiv.org/abs/1909.03368
- [M] Park, Choe, Veitch (2023) Linear Representation Hypothesis. https://arxiv.org/abs/2311.03658 (no numbers)
- [M] Yildirim and Paul (2023). https://arxiv.org/abs/2306.12672

**LLM behaviour**
- [V] Hao et al. (2023) RAP. https://arxiv.org/abs/2305.14992
- [V] Wang et al. (2024) text-based world simulators. https://arxiv.org/abs/2406.06485
- [V] Mancoridis et al. (2025) Potemkin Understanding. https://arxiv.org/abs/2506.21521
- [M] Slocum et al. (2025) Believe It or Not (abstract level for c24; d15 opened but results mostly in figures). https://arxiv.org/abs/2510.17941
- [V] Sinha et al. (2025) Illusion of Diminishing Returns. https://arxiv.org/abs/2509.09677
- [V] Shojaee et al. (2025) Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors. https://arxiv.org/abs/2311.08516
- [M] Kadavath et al. (2022) Language Models (Mostly) Know What They Know (abstract level). https://arxiv.org/abs/2207.05221
- [V] Turpin et al. (2023). https://arxiv.org/abs/2305.04388
- [V] Shi et al. (2023) GSM-IC. https://arxiv.org/abs/2302.00093
- [V] Qiu et al. (2025) Bayesian teaching. https://arxiv.org/abs/2503.17523
- [V] Hu et al. (2024) Chain-of-Symbol. https://arxiv.org/abs/2305.10276
- [V] Kim and Schuster (2023) Entity tracking. https://arxiv.org/abs/2305.02363
- [V] Prakash et al. (2025) belief tracking. https://arxiv.org/abs/2505.14685
- [V] Zhu, Zhang, Wang (2024) beliefs of self and others. https://arxiv.org/abs/2402.18496

Links only (researched in parallel elsewhere): Theory comparison; Distributed cognition; Chain-of-thought prompting; Bayesian models of cognition; Cognitive maps; MDPs and POMDPs; Active inference; Working memory and chunking; Conceptual metaphor and blending; Confidence and metacognition.
