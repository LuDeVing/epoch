# Conceptualization (grounded cognition): deep document

*Subfield A16.01. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b25, c01-c21, d01-d16), claims.jsonl (K01-K22), critique.md in this folder. Relevance to our agent: background only. No source tests a scaffold step derived from this theory at equal tokens.*

## 1. What it is

Grounded cognition is the view that concepts are built from the body's perceptual, motor and introspective states, and that thinking re-runs (simulates) those states. The rival view is that concepts are amodal symbols: abstract records that are not tied to any sense or movement.

Three claims are often mixed together. They need to be kept apart.

1. **Concepts are simulations.** Understanding "eagle in the sky" means re-activating a visual pattern with wings spread (Barsalou 1999, 2008; a01-a03).
2. **Body shape constrains which concepts a creature can acquire.** What you can reach, grasp and see sets the basic concepts (UP, CONTAINER, GRASPABLE). This is the Lakoff and Johnson line (a04, a17).
3. **Abstract concepts are understood through metaphor** from bodily experience: happy is up, love is a journey (Lakoff and Johnson 1980, 1999; a04).

The empirical status differs sharply by claim.

- Claim 1 has small, task-dependent effects in sentence-picture verification (K02) and a failed flagship motor effect (K01).
- Claim 3 as a priming effect has weak, mostly failed evidence (K04).
- A newer question is whether LLMs trained only on text can recover grounded structure. Here there is real, measured data (K07-K15, K19-K22).

Barsalou himself warns that "embodied cognition" wrongly suggests everyone claims the body is necessary (a01). The actual claim is milder: modal simulation is one of the systems used.

For our agent the field is background. The agent is text-only, so the bodily part has no direct meaning. The transferable idea is narrow: a concept may be better treated as a re-runnable situation model (state trace) than as a fixed definition. That idea has some LLM support (K14, K19) but no equal-token scaffold test (K18).

## 2. History and theories in depth

**Before 1999.** Classic cognitive science treated concepts as amodal symbols: feature lists, semantic networks, propositions. Lakoff and Johnson (1980) argued that everyday abstract talk is metaphorical and rooted in body experience. Evidence was linguistic: patterns across languages, with no effect sizes (a04).

**Perceptual Symbol Systems (Barsalou 1999, BBS 22:577-660; a02, a03).** The core mechanism:

- Association areas capture sensory-motor patterns during experience.
- Selective attention extracts schematic parts of the pattern.
- Memories of one component, organised around a frame, form a **simulator**. A simulator is roughly a concept or type.
- A simulator can produce unlimited simulations, one per situation. This gives type-token binding, inference, productivity, recursion and propositions without amodal symbols.
- Abstract concepts are grounded in complex simulations of physical and introspective events.

PSS is a verbal theory. Barsalou 2008 says a computational implementation is still an open goal (a02). It is hard to falsify as a whole. Only the abstract of the 1999 paper was read (a03).

**Barsalou 2008 (Annual Review; a01, a05-a07).** Widens the claim to "grounded cognition": modal simulation, bodily states and situated action. Evidence he reviews:

- Property verification. Solomon and Barsalou (2004): perceptual variables such as property size best predicted verification time. Larger properties were harder to verify (a05).
- Modality switching. Pecher, Zeelenberg and Barsalou (2003): verifying BLENDER-loud after CRANBERRIES-tart was slower than after LEAVES-rustling (a13).
- Lesions. Damage to visual areas raises loss of animal categories. Motor-area damage raises loss of tools (a06).
- Imaging. Hauk, Johnsrude and Pulvermuller (2004): reading lick, pick, kick activated motor strip areas near the tongue, finger and foot representations (a18).
- Causality. TMS over motor areas affects language processing. Barsalou says much more research is needed (a07).

**Behavioural landmarks.**

- Glenberg and Kaschak (2002): the action-sentence compatibility effect (ACE; a08).
- Stanfield and Zwaan (2001), Zwaan (2002), Connell (2005, 2007): implied orientation, shape and colour in sentence-picture verification (a10-a12).
- Schnall (2008): cleanliness priming and moral judgment (b04).
- Strack, Martin and Stepper (1988): pen-in-mouth facial feedback (a26).

**Critics.**

- Mahon and Caramazza (2008): sensory-motor activation during concept use can be spread from amodal concept nodes, so it does not prove embodiment. Strong embodiment conflicts with neuropsychology. Proposal: grounding by interaction (a16, b21).
- Rey and the SEP entry: motor activity may reflect *conceptions* (what we think about an object), not the concept itself (a17).
- Louwerse (2011): symbol interdependency. Language statistics carry much perceptual information, so effects read as simulation can come from distributional data (a15). Louwerse and Connell (2011) said modality-switch costs can arise from linguistic co-occurrence (a13 limits).
- Meteyard et al. (2012): the neural evidence supports weak, graded embodiment, not strong necessity (b22).

**Competing accounts of the data.** Not "simulation vs nothing". Three families remain: (a) strong simulation, (b) amodal concepts plus spreading activation, (c) distributional language statistics (symbol interdependency). Solomon and Barsalou (2004) show a task can use both: with unassociated false properties, word association predicted verification better; with highly associated false properties, which block that shortcut, perceptual variables did (a14). So the method decides which mechanism a result shows.

**Theory moves to AI (2020-2026).**

- Bisk et al. (2020), "Experience grounds language": five world scopes (corpus, internet, perception, embodiment, social). Text-only learning cannot reach the deeper ones (a20, c10). A position paper, no experiments.
- Merrill et al. (2021): formal result. Text assertions let a model emulate meaning only for semantically transparent languages. Where an expression's value varies by context, emulation can become uncomputable (c11).
- Mahowald et al. (2024): formal vs functional competence. LLMs are strong at the first, patchy at the second (c12).
- Binder et al. (2016): about 65 experiential attributes (sensory, motor, spatial, temporal, affective, social, cognitive) as a componential semantic model (a19). This is the bridge from theory to the rating norms used to test LLMs.
- Pavlick (2023) and Patel and Pavlick (2022) argue text-only LMs may map to grounded spaces. Not opened; treat as unverified (c20, c21).

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent confirmations or a verified large replication), **S** single source, **C** contested. Source ids refer to the evidence files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ACE original, Exp 1 | 44 recruited, 9 dropped, N=35; interaction F(1,34)=7.75; 155 ms on 1,766 ms (about 9%) | Glenberg and Kaschak 2002 (a08, c18) | Original; not replicated |
| ACE original, Exp 2A, 2B | 2A N=70, ACE F(1,68)=3.72 (marginal); 2B N=72; Exp 2a latency 170 ms on 1,871 ms | a08, c18 | Original |
| ACE 18-lab replication | 1,492 recruited, 214 excluded, N=1,278; effect on log lift-off CI95 [-0.006, 0.004]; preregistered negligible range under 100 ms | Morey et al. 2022 (a09, c18) | **E** null for this paradigm |
| ACE third-person variants | Exp 1 about 117 analysed, Exp 2 about 115; effects one direction or one axis only; depend on animacy and priming | Cai, Qi, Fan 2025 (d13) | C (conditional) |
| ACE further series | No robust compatibility effects; effects explainable without action simulation (abstract only; author attribution inferred) | JEP:LMC 2025 (d14) | S, weak |
| Implied orientation, replications | Exp 1a 33 ms, N=164, d=.10, BF01 1.06; Exp 1b 38 ms, N=172, d=.09, BF01 0.46; original 44 ms, d=.13 (N=40); pooled BF01 0.04 | Zwaan and Pecher 2012 (a10, b01) | C (small; BF ambiguous per study) |
| Implied shape, replications | Exp 2a 57 ms, N=176, d=.15; Exp 2b 70 ms, N=176, d=.18; original 64 ms, d=.31 (N=42); pooled BF01 0.01; accuracy .98 vs .96 | a11, b02 | Replicated; effect about half the original d (K03, S) |
| Implied colour, replications | Exp 3a N=152, 157 ms match advantage, d=.24; Exp 3b N=152, 85 ms, d=.17, BF01 1.22; originals -138 and -154 ms (mismatch advantage), d=-.25, -.27 | a12, b03 | C: sign flipped |
| Colour result depends on RT treatment | Pooled BF01 5.26 on trimmed RTs (favours no effect), under 0.01 on medians | critique correction 1 | C |
| Cleanliness and moral judgment | Original N=40, d=-0.60, p=.06; direct replication N=208, d=-0.01, p=.95; post hoc effort moderator: low effort d=-0.29, p=.04; high effort d=+0.19, p=.16 | Huang 2014 (b04, b05) | C, leaning null |
| Pen-in-mouth facial feedback, RRR | 17 labs, N=1,894, difference 0.03 [-0.11, 0.16] vs 0.82 original on 10-point scale; 15 of 17 lab intervals excluded 0.82; 17 of 17 BFs favour null | Wagenmakers et al. 2016 (d10) | **E** null for the pen task |
| Facial feedback, Many Smiles | N=3,878, 19 countries; mimicry and voluntary action raised felt happiness; pen-in-mouth inconclusive (abstract only) | Many Smiles 2022 (d12) | C; pooled sizes not verified |
| Facial feedback meta-analysis | 286 effects, 138 studies; small, heterogeneous; bias for affective judgments only; bias-corrected d not found (a recalled 0.29 is unverified) | Coles et al. 2019 (d11, b20) | C |
| Bodily feedback on motivation | z-curve review: poor evidentiary value | Azaad 2026 (c19) | S |
| Embodied effects in verb processing | g=0.259, p<.005; 33 samples, 265 effects, N=12,357; leave-one-out g 0.22-0.33; fail-safe N 4,903 | Three-level meta-analysis 2026 (c17) | S; pools paradigms, mostly Chinese L2 |
| Blind vs sighted animal appearance | Size ordering agreement with sighted raters: sighted 80.7%, blind 49.7%; height 62.3% vs 30%; shape odd-one-out 74.4% vs 55.1%; card-sort rho shape .81, texture .77, colour .35; blind-to-sighted colour rho .12 vs sighted-sighted .53. n=20 per group | Kim, Elli, Bedny 2019 (b06) | **E** with d15, d16 |
| Colour from text, blind and sighted | Embedding effect .60 [.51,.67] sighted vs .21 [.11,.29] blind; 120M-token fiction corpus beat 750M and 600B-token corpora (algorithms differ); beat GPT-4 elicited ratings | Liu, van Paridon, Lupyan 2025 (c14, d15) | S |
| Blind reliance on language statistics | N=42 (21 early blind, 21 sighted); group F(1,39)=9.40, p=.004 | Anceresi et al. 2025 (d16) | S |
| Text LMs recover colour geometry | 18 terms; Kendall tau up to .33 (ELECTRA), .16 (RoBERTa); BERT mini to base RSA max .077 to .162; linear-map selectivity about .73-.78; shuffled controls p>.05; fastText static .23; warm colours align better | Abdou et al. 2021 (a22, b07, c06) | **E** (with Marjieh) |
| Surprisal link | rho 0.12-0.17, p<.05 | b08 | S, weak |
| GPT predicts human sensory similarity | Pearson r: pitch .92, loudness .89, colours .89, consonants .57, taste .54, timbre .42; human split-half pitch .90 [.87,.92], consonants .46 [.36,.56]; colour naming ARI English GPT-4 0.59 [.56,.63], GPT-3.5 0.50, GPT-3 0.39 | Marjieh et al. 2023 (a21, b09, c04; corrected) | S |
| GPT-4 gain not vision-specific | Gain over other models about r=.15 colours, .16 pitch, .16 taste, .14 consonants | b10 | C (see K10) |
| LLM ratings vs human norms | GPT-4 sensorimotor (n=7) vs non-sensorimotor (n=11) dims: U=65, P=0.018, r_rb=0.69; GPT-3.5 U=67, P=0.010, r_rb=0.74; PaLM U=76, P<0.001, r_rb=0.97. Humans N=829 (Glasgow) and 3,500 (Lancaster), about 4,442 words | Xu et al. 2025 (c01) | S |
| Vision link in that study | Gain GPT-4 over GPT-3.5 vs visual association: imageability Rs=.69, concreteness Rs=.62; gustatory Rs=.01, torso Rs=.02; preprint: imageability .26 to .91, visual dim .27 to .76, rs=.77 over 18 dims | c02, b12 (preprint) | C |
| LLMs vs humans on abstract concept properties | 21 models; none above r=.37 with human property frequencies; human ceiling above .9; but rating alignment r about .6-.8 (Claude Sonnet 4.6 mean r=.760); SAE steering shifted categories +5.3% sensorimotor, +4.7% motor, +9.4% internal | Chlapanis et al. 2026 (a23, b13, b14) | S |
| VLM vs text backbone | QA accuracy small pair 68.0 to 77.5%, large pair 78.8 to 85.5%; gains uneven: ARC-C 65.70 to 78.41, WinoGrande 52.41 to 63.30, CSQA 61.51 to 71.58, PIQA 35.30 to 71.90 | Roy et al. 2026 (b15, b25) | C (training mix confound) |
| VLM affordance deficit | 18 VLMs vs over 2,000 humans on 15 tasks; affordance beta=0.171 [0.04,0.30], p=.022; sensory beta=0.163, p=.028; about 18 points; resists prompting and newer releases. Captions: affective terms 52% (CC12M), 56% (RedCaps) vs 36% affordance | Rosenberg et al. 2026 (b16, b17) | S |
| Grounding at fixed scale | OPT-175B zero-shot 85% on material, near chance on mass; CLIP-ViT-L/14 still 18.5% below humans on embodied sets; VLM distillation gain equals scaling LM 134x; multimodal beats BERT on ViComTe, size does not help | Li et al. 2023 VEC; Zhang et al. 2022 (d06, d07) | **E** modest, uneven |
| PIQA gap, 2019 | Human 94.9; RoBERTa 355M 77.1; BERT 340M 66.8; GPT 124M 69.2; chance 50 | Bisk et al. 2020 (d05) | Dated |
| Visual vs text word learning | Visual helps mainly in low-data regimes; text-only catches up or wins with more data; visual worse on SimVerb-3500; GIT-style joint nearly identical to text-only | Zhuang et al. 2024 (c07, c08) | C |
| Multimodal image encoders as semantic models | Image encoders comparable to LLMs even on non-visual attributes; multimodal slightly better (scores not extracted) | Oneata et al. 2025 (a25) | S |
| World state in LM hidden states | Alchemy splice: T5 consistent with new state 75-87% vs 24-38% single context; BART 58-87%; probe 58.5%, 64.8% at state declaration | Li, Nye, Andreas 2021 (c09) | S |
| Othello-GPT intervention | Errors 2.68 to 0.12 (natural, 1,000 cases), 2.59 to 0.06 (unnatural, 1,000); illegal moves 0.01% vs untrained 93.29%; linear probe error never below 20% | Li et al. 2023 (d08) | S, synthetic |
| Llama-2 represents space and time | Probes on 6 datasets; space and time neurons; authors say probing alone does not show use | Gurnee and Tegmark 2024 (d09) | S |
| Visualization-of-Thought, GPT-4 | CoT / VoT: route success 9.48 / 14.72; completion 37.02 / 40.77; next-step 48.61 / 55.28; tiling 54.15 / 63.94; NL navigation 54.00 / 59.00 (p<0.16). GPT-4 without viz: 46.98 on tiling | Wu et al. 2024 (d01) | S |
| MVoT (fine-tuned multimodal) | Maze 92.95%, MiniBehavior 95.14%, FrozenLake 85.60%; CoT on FrozenLake 0.9401 (3x3) to 0.3911 (6x6); 90.80% of CoT errors were wrong hole coordinates | Li et al. 2025 (d02) | S |
| Mind's Eye (simulator) | UTOPIA 39 tasks: +27.9 zero-shot, +46.0 few-shot points; 1.3B + simulator 29.8% vs 175B vanilla 29.0% | Liu et al. 2022 (d03) | S |
| SimToM perspective taking | GPT-3.5 BigToM +29.5 over 0-shot, +14.2 over CoT; ToMI +16, +19, +47 for Llama2-7b, 13b, GPT-3.5; slight drop for GPT-4 | Wilf et al. 2023 (d04) | S |
| Conceptual metaphor prompting | 100 tasks, 4 small models, LLM judge (Llama3.3 70B); CMT beats or matches; no p-values | Kramer 2025 (c13) | S, weak |

## 4. Mechanisms and models

The mechanisms below are written so that an engineer can build or test them. Items marked (human) describe human cognition; the rest have LLM data.

**4.1 Simulator and simulation (PSS; human).**
- Data structure: a *simulator* is a frame plus a store of component memories (perceptual, motor, introspective). A *simulation* is one instance drawn from the simulator and adapted to the current situation.
- Runtime: on reading "the eagle in the sky", the system retrieves the simulator EAGLE, binds the slot "location=sky", and re-activates a visual state with spread wings. A later picture is checked against that state. A match gives faster verification.
- Engineer's version for text: concept = (frame slots, default values per slot, typical state transitions). On each use, fill the slots from the situation and write out the resulting state. This is what Visualization-of-Thought does for spatial grids (4.4).
- Limit: PSS gives no commitment on which slots are perceptual. Barsalou 2008 says implementation is open (a02).

**4.2 Dual mechanism in property verification (human).**
- Two routes run in parallel: (1) a word-association route (fast, shallow), (2) a simulation route (slower, perceptual, size-sensitive).
- Which route decides the answer depends on the false probes. If false probes are weakly associated, route 1 suffices and the simulation signature disappears. If false probes are highly associated, route 1 fails and route 2 shows (Solomon and Barsalou 2004; a14).
- Engineer's check: any "simulation helps" claim for an LLM must beat a control where the shallow route is blocked.

**4.3 Distributional recovery of perceptual structure (LLM).**
- Colour terms occur in contexts (adjectives, collocations). Embedding distances over these contexts approximate CIELAB distances. Abdou et al. measure this by representational similarity analysis (RSA: correlate the pairwise distance matrices; Kendall tau) and by a linear map from embeddings to the colour space scored against shuffled controls (a22, b07).
- The signal travels through second-order co-occurrence: words that share neighbours, not words that appear together (Liu et al., c15). Fiction corpora carry more colour-adjective signal per token than subtitles or web crawl (c14).
- Implement: no scaffold needed. The model already holds this. The check is to elicit it (pairwise similarity prompt, as in Marjieh) and compare with norms.

**4.4 State trace as an imagery substitute (LLM).**
- Visualization-of-Thought: after each reasoning step the model writes the grid state in text. The next step reads the previous state. This replaces holding a mental image (d01).
- Needed pieces: a fixed state format (grid of characters), a per-step update rule, a final answer read from the last state.
- Measured: GPT-4 tiling 63.94 vs 54.15 for CoT. Route success 14.72 vs 9.48. NL navigation only 59.00 vs 54.00 and p<0.16. Without the viz instruction, GPT-4 got 46.98 on tiling, so asking for the trace, not extra tokens alone, is the reported cause. But token counts were not matched (d01).
- Failure mode: the model's state lines are often wrong, and errors compound. MVoT shows that on FrozenLake 90.80% of CoT errors were wrong hole coordinates (d02): text coordinates break on larger grids (0.9401 at 3x3 to 0.3911 at 6x6).

**4.5 World-state probes and edits (LLM).**
- Linear and nonlinear probes decode state from hidden layers (Li et al. 2021, c09; Othello-GPT, d08; Gurnee and Tegmark, d09).
- Causal test: edit the hidden state, then check whether the output follows. Othello-GPT: legal-move errors fall from 2.68 to 0.12. This shows a learned *world state* is causally used. It does not show perceptual symbols.
- An engineer cannot do this on an API model. It matters as an existence proof: state tracking is real inside LMs trained on text.

**4.6 External simulator (LLM).**
- Mind's Eye pipeline: a text-to-code translator turns the physics question into a simulator script, the simulator runs, its result is written back into the prompt as a hint, and the LM answers. Gain +27.9 zero-shot (d03).
- This is the one case where "simulation" helps a lot. The gain comes from the engine, not from the LM imagining.

**4.7 Perspective filtering (SimToM).**
- Stage 1: rewrite the story keeping only what character X knows. Stage 2: answer from that filtered story. Gain +14.2 over CoT for GPT-3.5, none for GPT-4 (d04).
- The single-prompt version did not reproduce the gain, so the separation of the two stages matters.

**4.8 Conceptual metaphor prompt (LLM).**
- The prompt asks for explicit source-domain to target-domain mappings. Only one weak study (c13). No mechanism evidence.

## 5. What holds up

**Replications and failures (human).**

- ACE failed in 18 labs (N=1,278, effect near 0). This is the best-powered test of the best-known motor-language effect. Two 2025 papers still find only conditional effects or none (K01, E).
- Implied shape replicated (57 and 70 ms), but at about half the original d (.15 and .18 vs .31). Orientation is tiny (d about .10, BF01 0.5 to 1.1). Colour flipped sign. So: some real small effects, original effects inflated, and the direction of some effects is not stable (K02, K03).
- Cleanliness priming: d=-0.60 became d=-0.01. The effort moderator was proposed after the failure and is not independent (K04).
- Pen-in-mouth: null in 17 labs. Many Smiles found that mimicry and voluntary facial actions work while the pen task did not. So "the bodily manipulation matters" is a boundary condition, not a rescue of the original (K05).
- A 2026 z-curve review rates motivation-bodily-feedback studies as poor in evidentiary value (c19).
- The 2026 three-level meta-analysis finds g=0.259 in verb processing, but pools paradigms that failed elsewhere (K06).

**Moderators and boundary conditions.**

- Task choice: associative shortcuts can mimic simulation (a14). Louwerse and Connell: modality-switch costs may come from language co-occurrence (a13).
- Concrete vs abstract: effects in verb studies depend on verb concreteness and verb layer (c17).
- Response effort (Huang; post hoc).
- Perspective and animacy for third-person ACE (d13).
- RT treatment for colour (critique correction 1).
- Participant pool: MTurk samples were slower and older than lab students (b01).

**Where the data say language does much of the work.**

- Blind people know a lot about appearance, but less: size ordering 49.7% vs 80.7%, shape 55.1% vs 74.4%, colour card-sort rho .35 against .81 for shape. Blind adults infer from taxonomy and habitat, not only from language (b06).
- Text embeddings predict blind colour-adjective associations with effect .21 vs .60 sighted (c14).
- Early blind adults lean more on neighbourhood density (F(1,39)=9.40; d16).
- Net: language carries a large but partial share. Both "text suffices" and "grounding is required" are too strong (K15, E).

**Interventions that worked (LLM).**

- Writing a state trace per step: GPT-4 tiling +9.8 points, route success +5.2, next-step +6.7 (d01). Token cost not matched.
- An external simulator: +27.9 and +46.0 points (d03).
- Perspective filtering: for GPT-3.5 and Llama2 only (d04).
- Distilling from VLMs to LMs on embodied concepts: gain comparable to scaling LM parameters 134x (d07).
- Training on images: helps concrete QA (68.0 to 77.5) but confounded (b15).

**Interventions that did not work or were not shown.**

- Prompt engineering did not remove the VLM affordance deficit (b16).
- Scaling text LMs did not fix embodied concepts (d07) or ViComTe (d06).
- SimToM did nothing for GPT-4 (d04).
- Imagery prompts as such at equal tokens: no study found (K20).
- Metaphor prompt benefit has no human or significance-tested check (K17).

**Inflation prior.** Across motor-language, priming and facial feedback, replications give about zero to half the original effects. Any claim about a human embodied effect should be discounted by at least half (K03, a prior from a single source).

## 6. Language models

**Perception from text alone.**

- Colour structure in static and contextual embeddings (tau up to .33, 18 terms) (K07, E).
- GPT-4 similarity ratings match humans in pitch (r=.92, vs human split-half .90), colours (.89), consonants (.57 vs split-half .46), taste (.54), timbre (.42). Human reliability caps the score in noisy domains (K08).
- Marjieh et al. argue the GPT-4 gain over other models comes from richer text, not images. Xu et al. tie the GPT-4 gain to visual association. Neither isolates vision, since models differ in size, data and tuning (K10, C).

**Where text falls short.**

- Motor and sensory norms: GPT-4 U=65, P=0.018 against non-sensorimotor; PaLM r_rb=0.97 (c01). Medians quoted in the preprint line (0.64 and 0.77 non-sensorimotor) did not match the published text; do not use them (critique correction 5).
- Abstract concept properties: none above r=.37 with human property frequencies in free generation; r about .6-.8 in rating. The task format decides how grounded a model looks (K11).
- Affordances in VLMs: beta=0.171, about 18 points, not fixed by prompting or newer releases (K12).
- Physical commonsense, 2019: 17.8 points under humans (RoBERTa 77.1 vs 94.9). Dated; frontier numbers were not measured here (K21).

**What grounding (training on images) did.**

- Mass-type concepts: CLIP/BLIP beat OPT-175B (OPT near chance on mass, 85% on material) (d07).
- ViComTe: multimodal encoders beat BERT, scale did not help (d06).
- Matched Llama pairs: QA gains of 9.5 and 6.7 points on average, but uneven (PIQA 35.30 to 71.90 for one pair, CSQA 76.17 to 77.15 for another) (b15, b25).
- Word learning: visual helps in low-data regimes. With more data text-only catches up or wins, and visual is worse on verbs (c07).
- Image-only encoders reach LLM level on non-visual attributes (a25).
- Net (K13, C): modest, uneven, confounded by training mix. Not evidence that images are required for most concept tasks.

**What changes behaviour in a text-only LLM.**

- A written state trace per step (VoT): +5 to +10 points on GPT-4 spatial tasks, tokens not matched (K19).
- An external simulator: large gains (K20).
- Perspective filtering: weak models only (K20).
- Sparse-autoencoder steering of grounding features moved categories +4.7 to +9.4% (b14). A model-internals result.
- Conceptual metaphor prompting: positive in small models, with an LLM judge and no statistics (K17).

**Internal world state.** LM hidden states hold entity states (75-87% vs 24-38% after splicing), board states (editing cuts errors from 2.68 to 0.12) and space and time coordinates (K14). No causal test exists for perceptual concepts such as colour.

**Honesty note.** Almost all LLM evidence here uses prompted ratings or similarity tasks, not use of the concept in action or reasoning. None of it tests a scaffold step at equal tokens.

## 7. What our agent should take

Relevance is background. Nothing here is established as a scaffold element, so "Add now" is short and mostly says what to leave out.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not add embodied-effect priming, metaphor priming or bodily-state steps to the schema. The human effects that motivated them failed or shrank in large replications. This supports G7 (every element must win at equal tokens). | G7 (reason for exclusion; add to section 4b only if the author agrees) | [E] | K01 (a09, c18, d13, d14), K04 (b04, b05), K05 (d10) |
| Treat any claimed simulation gain as roughly half its first estimate until replicated at equal tokens. | G7 | [E] for human effects; [S] for transfer to LLMs | K03 (b01, b02) |
| Text carries much but not all perceptual knowledge. For a motor, affordance or non-visual sensory fact, do not trust the model's own ratings without a check; route to code, lookup or a tool when one exists. | G3, G10 (check outside the model) | [E] that text carries part, not all; the routing rule itself is untested | K07, K15, K12 (c01, b16, b06, c14) |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Per-step written state table (VoT style) for spatial and state-tracking items, beside plain CoT at equal tokens | S2 REPRESENT / O6 change representation | [S] | K19 (d01, d02), K14 (c09, d08) |
| External simulator or code step in place of an imagery prompt for physics items | O6 / tool in S4 TEST | [S] | K20 (d03) |
| Two-stage perspective filter for belief and knowledge questions | S1 UNDERSTAND | [S], weak models only | K20 (d04) |
| Ask the agent to write concrete situations for abstract concepts before answering definition questions | O7 map an analogue / S2 | [S] | K11 (a23, b13) |
| Metaphor-framed prompt vs plain on judgment items, human or fixed rubric | O8 reframe the goal | [S] weak; LLM reframing is already null in one large test per SCHEMA | K17 (c13) |
| Implied-state listing before shape-dependent questions | S1 / S2 | [C] | K02 (a10-a12, b01-b03) |
| Memory: store lessons as typed situation frames (slots and default states) vs plain text lessons | memory (S9) | [C]; theory only | K18 (a01, a02) |

## 8. Concrete tests on our bench

Both arms always get the same total token budget (output plus any added context). Report accuracy, tokens, and the paired difference with a bootstrap 95% interval. Run at least 3 seeds. Include one control arm that adds the same number of neutral tokens (for example, a restatement of the task).

| Item type | Arm A | Arm B | Metric | Expected effect |
|---|---|---|---|---|
| Grid or spatial reasoning (tiling, route, next-step; 100+ items) | Plain CoT | Per-step state table | Accuracy; state-line accuracy by human check | +3 to +8 points on GPT-4-class models, likely smaller once tokens are matched; none on easy items |
| State tracking in toy worlds (Alchemy-style, object moves, 100 items) | Plain CoT | Explicit state table updated each step | Final-state accuracy | Positive; larger on long chains |
| Physics word problems with a checkable answer | Imagery prompt ("picture it, state what you see") | Code or simulator step, same tokens | Accuracy | Code beats imagery; imagery roughly equals plain |
| Belief questions (false-belief, who-knows-what) | One-prompt CoT | Two-stage perspective filter | Accuracy | None on frontier models, gain on small ones |
| Perceptual commonsense (colour, size, texture, sound; held-out norms) | Plain | "State sensory properties first" | Rank correlation with human norms (Lancaster-style) | Small or none; text already holds the structure |
| Motor and affordance facts (what can be done with an object) | Plain | State-first, plus a tool check where one exists | Accuracy vs human norm set | Weak on motor norms; test whether the tool check lifts it |
| Abstract concept definition matching (100 concepts) | Plain | Generate 3 concrete situations, then define | Match to human property lists (fixed rubric, not an LLM judge) | Small positive on emotion and internal-state properties |
| Judgment items with a fixed rubric | Plain prompt | Metaphor-framed prompt | Rubric score, human-checked sample | Likely null, based on the failed priming literature |
| Shape-dependent verification (implied shape and orientation) | Plain | List implied visual states first | Accuracy | Small; expect none |

Rules from SCHEMA that apply: G3 (score on held-out items), G7 (kept only if it wins at equal tokens), G10 (decide from outputs, not from the reasoning text).

## 9. What does not transfer, and why

- **Motor effects (ACE, somatotopy).** Our agent has no body or motor cortex. The best test of the effect failed anyway (K01).
- **Facial feedback and bodily-state priming.** No face. The human effect was null or weak in the largest studies (K05).
- **Cleanliness and metaphor priming.** Priming depends on a human's state before judging. An LLM re-reads the whole prompt each call, so nothing carries over. The human effect was also close to zero (K04).
- **Modality-switching cost in property verification.** It is a reaction-time effect from shared neural resources. A stateless model has no reaction time.
- **Neuroimaging and lesion evidence.** Brain-area activations map to no lever on an API model.
- **Blind-sighted comparisons.** They show how language compensates in humans. They give no knob for the agent.
- **Vision training as an intervention.** Our agent is fixed. We cannot add images at training time, and the effect is confounded with scale in any case (K10).
- **Probing and activation edits.** Valid for open-weight research, not available through an API.
- **Position papers (Bisk 2020, Merrill 2021).** Arguments about what text-only training can learn in principle. They give no scaffold rule.
- **Simulation as imagery.** What helps LLMs is a written state trace or an external engine. It is not a human's sensory re-enactment, and evidence for the second is not an argument for the first.

## 10. Open questions

1. Does an imagery or "state the sensory details" prompt improve reasoning at equal tokens? No study found (gap 1).
2. Does a per-step state trace win once its extra tokens are matched? VoT did not match tokens (d01).
3. What are the pooled Many Smiles effects and moderators? Paywalled; only the abstract was read (gap 2).
4. What is the bias-corrected Coles 2019 effect? Not found. A recalled 0.29 and a thesis snippet of about 0.20 are both unverified (gap 4; the R dataset psymetadata could recompute it).
5. Do frontier LLMs (2025-2026) close the PIQA, VEC and affordance gaps? Only 2019-2023 models and 2026 VLM data are measured here.
6. Is the vision gain of GPT-4 over GPT-3.5 caused by images or by scale and tuning? Cannot be isolated on one model (K10).
7. Do LLM concept representations causally mediate behaviour on perceptual concepts? Interventions exist only for Othello and toy worlds (gap 7).
8. Petilli et al. 2024 blind vs sighted data were not located (gap 8). Abstract concepts in blind groups are untested.
9. Does the Solomon and Barsalou associative-vs-simulation boundary appear in LLM property verification? No study (gap 9).
10. Do metaphor-framed prompts help in a human-judged, significance-tested study? None found (gap 6).
11. Do free generation and rating formats measure the same grounding? r<=.37 vs r about .6-.8 suggests not (K11).
12. Does the Chlapanis result hold with human coders instead of an LLM judge?
13. Which of the 2025 conditional ACE effects, if any, replicate with preregistration?

## 11. Sources

[V] = opened and read (this or the earlier session, per the evidence files). [M] = snippet or abstract only.

**Theory and reviews**
- [V] Barsalou 2008, Grounded cognition. https://vsegaux.github.io/vault_M2_CNA_UGA/Sciences-du-langage/Articles/Barsalou_AnnuRevPsycho2008.pdf (a01, a02, a04-a07)
- [M] Barsalou 1999, Perceptual symbol systems. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0140525X99002149 (a03)
- [V] Stanford Encyclopedia of Philosophy, Embodied Cognition. https://plato.stanford.edu/entries/embodied-cognition/ (a17; read via a summariser)
- [M] Louwerse 2011. https://doi.org/10.1111/j.1756-8765.2010.01106.x (a15)
- [M] Mahon and Caramazza 2008. https://doi.org/10.1016/j.jphysparis.2008.03.004 ; https://pubmed.ncbi.nlm.nih.gov/19084756/ (a16, b21)
- [M] Meteyard et al. 2012. https://pubmed.ncbi.nlm.nih.gov/21163473/ (b22)
- [M] Binder et al. 2016. https://doi.org/10.1080/02643294.2016.1147426 (a19)
- [V] Bisk et al. 2020, Experience grounds language. https://arxiv.org/abs/2004.10151 (a20, c10)
- [V] Merrill et al. 2021. https://arxiv.org/abs/2104.10809 (c11)
- [V] Mahowald et al. 2024. https://arxiv.org/abs/2301.06627 (c12)
- [M] Pavlick 2023, Symbols and grounding in large language models (c20; no URL)
- [M] Patel and Pavlick 2022. https://openreview.net/forum?id=gJcEM8sxHK (c21)
- [V] Conceptual blending in humans and language models 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13461484/ (c16)

**Human studies and replications**
- [V] Glenberg and Kaschak 2002. https://link.springer.com/content/pdf/10.3758/BF03196313.pdf (a08)
- [V] Morey et al. 2022. https://link.springer.com/content/pdf/10.3758/s13423-021-01927-8.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9038876/ (a09, c18)
- [V] Cai, Qi, Fan 2025, Frontiers in Psychology. https://doi.org/10.3389/fpsyg.2025.1562351 (a27, d13; N inferred from df)
- [V, abstract only] JEP:LMC 2025 ACE series, author attribution unconfirmed. https://doi.org/10.1037/xlm0001327 (d14)
- [V] Zwaan and Pecher 2012. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0051382&type=printable ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3530580/ (a10-a12, b01-b03)
- [M] Pecher, Zeelenberg, Barsalou 2003. https://doi.org/10.1111/1467-9280.t01-1-01429 (a13)
- [M] Solomon and Barsalou 2004. https://doi.org/10.3758/bf03196856 (a14)
- [M] Hauk et al. 2004. https://doi.org/10.1016/s0896-6273(03)00838-9 (a18)
- [V] Huang 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4222330/ (b04, b05)
- [V] Wagenmakers et al. 2016 RRR. https://pure.uva.nl/ws/files/14872420/Registered_Replication_Report.pdf (d10; a26 and b18 were abstract or memory)
- [V, abstract only] Many Smiles 2022. https://www.nature.com/articles/s41562-022-01458-9 (d12; b19 is a snippet with a different URL)
- [V, abstract only] Coles, Larsen, Lench 2019. https://doi.org/10.1037/bul0000194 (d11; b20 snippet)
- [V] Azaad 2026 z-curve. https://pmc.ncbi.nlm.nih.gov/articles/PMC13597610/ (c19; statistics not extracted)
- [V] Three-level meta-analysis 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13295721/ (c17)
- [V] Kim, Elli, Bedny 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6561279/ (b06; not re-opened in critique)
- [M] Petilli et al. 2024. https://boa.unimib.it/retrieve/d54cc852-66b1-4bab-acaf-994bbba84fa5/Petilli-2024-J%20Cogn-VoR.pdf (b23; not read)
- [V] Liu, van Paridon, Lupyan 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11997174/ ; https://doi.org/10.1038/s44271-025-00230-9 (c14, c15, d15)
- [V] Anceresi et al. 2025. https://doi.org/10.3758/s13423-024-02557-6 (d16)

**LLM and AI studies**
- [V] Marjieh et al. 2023. https://arxiv.org/abs/2302.01308 (a21, b09, b10, c04, c05)
- [V] Abdou et al. 2021. https://arxiv.org/abs/2109.06129 (a22, b07, b08, c06)
- [V] Xu et al. 2025, Nature Human Behaviour. https://pmc.ncbi.nlm.nih.gov/articles/PMC12454144/ ; https://doi.org/10.1038/s41562-025-02203-8 ; preprint https://arxiv.org/abs/2305.19103 (a24, b11, b12, b24, c01-c03; use c01, not the b11 medians)
- [V] Chlapanis et al. 2026. https://arxiv.org/abs/2605.08837 (a23, b13, b14; not re-opened in critique)
- [V] Oneata, Elliott, Frank 2025. https://arxiv.org/abs/2506.03994 (a25)
- [V] Roy, Wang, MacLellan 2026. https://arxiv.org/abs/2601.18065 (b15, b25)
- [V] Rosenberg et al. 2026. https://arxiv.org/abs/2603.26589 (b16, b17)
- [V] Zhuang, Fedorenko, Andreas 2024. https://arxiv.org/abs/2310.13257 (c07, c08)
- [V] Li, Nye, Andreas 2021. https://arxiv.org/abs/2106.00737 (c09)
- [V] Li et al. 2023, Othello-GPT. https://arxiv.org/abs/2210.13382 (d08)
- [V] Gurnee and Tegmark 2024. https://arxiv.org/abs/2310.02207 (d09)
- [V] Kramer 2025, Conceptual metaphor theory as a prompting paradigm. https://arxiv.org/abs/2502.01901 (c13)
- [V] Wu et al. 2024, Visualization-of-Thought. https://arxiv.org/abs/2404.03622 (d01)
- [V] Li et al. 2025, MVoT. https://arxiv.org/abs/2501.07542 (d02)
- [V] Liu et al. 2022, Mind's Eye. https://arxiv.org/abs/2210.05359 (d03)
- [V] Wilf et al. 2023, SimToM. https://arxiv.org/abs/2311.10227 (d04)
- [V] Bisk et al. 2020, PIQA. https://arxiv.org/abs/1911.11641 (d05)
- [V] Zhang et al. 2022, ViComTe. https://arxiv.org/abs/2205.01850 (d06)
- [V] Li et al. 2023, VEC benchmark. https://arxiv.org/abs/2305.14057 (d07)
