# Cognitive-historical analysis: deep document

*Subfield D07.03. Sources: evidence_a-d.jsonl (a01-a25, b01-b30, c01-c27, d01-d22), claims.jsonl (K01-K29), critique.md. Where critique.md corrected an earlier evidence line, the corrected value is used here and flagged.*

## 1. What it is

Cognitive-historical analysis is a method. It studies how scientists reason by reading the historical record (notebooks, papers, letters) next to lab studies of ordinary human cognition. The goal is not to write history. The goal is to learn which thinking processes produce new concepts (a01, a10).

The base claim is naturalist. Scientists' methods grow out of everyday abilities: mental modeling, analogy, abstraction, visualisation, simulative imagining. Reflective method building then sharpened them ("bootstrapping"). From a01: "the problem-solving practices of scientists arise out of and are constrained by basic cognitive capacities."

Key people and works:
- Nersessian (1987 named the method; 2008 *Creating Scientific Concepts*; 2007 handbook chapter; 2009 and 2025 reviews). Main case: Maxwell, "On Physical Lines of Force" (1861-62).
- Gentner et al. (1997): Kepler, read with structure-mapping theory.
- Nersessian and Chandrasekharan (2009): hybrid analogies in a neural-engineering lab (history plus ethnography).
- Clement (2022): 24 heuristic processes drawn from historians' cases and expert think-aloud studies.

Why it matters for our agent: it is the main source for O6 (change representation, model building) and O7 (map an analogue). It says how a mapping is built: pick a source, narrow it with target constraints, simulate, abstract. It does not say when to use it. That timing question (S6 placement) is what the SUBFIELDS row asked for, and this field has no counts to answer it.

Honesty point. The method itself has no effect sizes. Support is a handful of case studies (Maxwell, Kepler, Newton, Faraday, two bioengineering labs). Nersessian says generality comes from bootstrapping, explicitly not from inductive generalisation (b02). No independent replication or historian's critique of the Maxwell reading was found (K27, d21). So the method is a source of hypotheses for the agent, not a source of proof.

## 2. History and theories in depth

### 2.1 Origins and stance
- Early 1970s: historians and philosophers treated analogies and diagrams as aids, not as reasoning. Nersessian's archival work reversed this (d21, her own account).
- Her contrast class: lab experiments and AI discovery programs (Klahr and Simon 1999, BACON) have low ecological validity. They omit material, social and cultural resources and the work of formulating the problem (b03).
- Type of claim: "model-based reasoning" is how scientists generate concepts. Three forms: analogical, visual (imagistic), simulative (thought experiments) (a11, a12).

### 2.2 The Maxwell case (a02, a03, a21, b06)
Sequence as Nersessian reads it:
1. Target constraints from electromagnetism: rotation (magnetic force rotates polarised light) and geometry (lines of force).
2. Source selection: continuum mechanics, narrowed to elastic fluids (vortices) because the target constraints fit.
3. First hybrid model: the vortex model.
4. Simulating the model in imagination exposed a problem: neighbouring vortices would rub and move the wrong way. New constraint: friction.
5. Second hybrid: add idle wheels (from machine mechanics, a second source domain).
6. Generic abstraction: drop the specific mechanism; keep what it shares with any system where one part passes motion on continuously. That gave continuous-action transmission, the field concept (a03).

Counts: 2 hybrid models, 2 source domains, 3 named abstraction types. Clement (b06) reads the same case as: imagine the field as a fluid with vortices, apply a continuum-mechanics schema to get first maths, evaluate, modify. This is a convergence claim between one historical case and Clement's protocols, with no statistics.

### 2.3 The Kepler case (a05-a08)
Gentner et al. coded Kepler's beliefs about light (5 beliefs) and about the motive power (vis motrix), and ran the Structure-Mapping Engine. They argue four analogical processes change a concept:
- highlighting: alignment shows which shared structure matters;
- projection: candidate inferences are carried from source to target;
- re-representation: rewrite either side to improve the match (Kepler: "light is instantaneous" versus "force acts in time");
- use of alignable differences: connected differences become salient. Kepler argued light and motive power differ because an eclipse blocks light but does not stop planetary motion.

Evidence that the analogies drove his thinking (a08): he published dead ends, left his 1596 book intact in 1621 with notes (25 years), and read Gilbert's *De Magnete* and wrote his own optics. Light falls as inverse square; his force law was a simple inverse (1/r) by a plane argument (a07). He replaced Copernicus's "at least 34 circles" with 6 ellipses and repeated one calculation "at least seventy times" (both verified by critique.md).

Unverified: critique.md could not find "4 candidate inferences" or "8 minutes of arc" in the text. Do not use those two figures.
Weakness: the authors chose the coding of Kepler's beliefs. Precedent for failure: Hanson's abductive reconstruction of Kepler was judged "not a historically adequate account" (Lugg 1985; d18).

### 2.4 Hybrid models in live labs (a09, a10, a21, b04)
- Study: 5 years, 2 labs, 148 interviews, 40 research meetings fully transcribed, 800+ hours of observation (a10).
- Finding: researchers did not map one ready-made source onto a target. They built an intermediate model (a dish of living neurons, then a computational model) carrying constraints from both source and target. Constraints are "straps"; hybrid models are "strap crossings" (a09).
- Standard analogy theories (one source, one target) do not cover this. Three study types (historical, protocol, ethnographic) are cited as showing hybrid construction (a21).
- Success conditions (b04): structural analogies work when relational structure maps (Maxwell). Functional analogies work when the model reproduces target behaviour (an in vitro artery model). Abstraction is broad: idealisation, approximation, simplification, omission, limiting case, generic modelling.

### 2.5 Competing and neighbouring accounts
- Hesse (neutral analogies suggest hypotheses) versus Bartha (analogy as confirmation: no) (a12).
- Clement's four-level hierarchy of 24 heuristic processes with a Generation-Evaluation-Modification cycle (b05).
- Dunbar's in-vivo lab studies: analogy is central to practice (a25, second-hand).
- Search-based discovery: BACON, KEKADA (Langley et al. 1987; a24, second-hand). AI Feynman and AI-Newton rediscover laws with no analogy (c18, c19). This is the rival view: much discovery can be done by search over equations.
- Structure-mapping theory (Gentner) supplies the formal mapping the history cases use.
- A 2026 case analysis of Bohr's complementarity-relativity analogy lists matched elements, then dissimilarities, and finds the analogy weakened by the dissimilarities (b07). One case, qualitative.

### 2.6 Everyday cognition behind the method (a04, b12-b14)
Simulation is real in the lab. Mental rotation latency grows with rotation angle (Shepard, Cooper, Kosslyn). People simulate moving around a wall, not through it. In gear and pulley problems response time follows rotation angle, and people trained in rules switch to rules and answer faster. Relational reasoning can be trained: high-cuing of correspondences raised extension to new contexts (Richland and McDonough 2010); generating far analogies primed adults to attend to relations (Vendetti 2014, Walker 2018); self-generated relations beat passive listening in 3-4 year olds (Simms and Richland 2019); among 272 pupils latent class analysis found 4 relational-attention clusters. Expert geoscientists spontaneously generate analogies grounded in causal principles (Goldwater, Gentner et al. 2021; no figures read).

## 3. Core findings with exact numbers

Status uses claims.jsonl labels, with critique corrections.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Maxwell built hybrid models in stages | 2 hybrid models, 2 source domains, 3 abstraction types | a02, a03, a21, b06 (K01) | established, case-study only |
| Kepler analogies: highlight, project, re-represent, use alignable differences | 4 processes; 5 light beliefs coded; 34 circles to 6 ellipses | a05-a08 (K03) | single-source |
| Scientists' analogies are mostly structural, not surface | Economics group: 69 of 88 (78%) no surface overlap; 97 analogies, about 7 h, coder agreement 96%, kappa 0.85 | b08 (K02) | established |
| Analogy distance depends on setting | Microbiology labs 98% within domain (Dunbar); psychology labs over 75% within (Saner and Schunn); engineering 55% within / 45% outside; political writing 77% outside; economists 53% within / 47% outside (44 vs 39 of 83) | b09, b10, d17 (K02) | established; Dunbar figures second-hand |
| "Near sources for fixes, far for new concepts" | No counts. Review says goals had no effect on distance in political writing | a11, d17, d18 (K19) | contested |
| Purposes of expert analogies (n=77) | example 35%, visualisation 25%, exaggeration 14%, inclusion 12%, differentiation 10%, abstraction 3%, critique 1% | b09 | single-source |
| No surface-similarity constraint on distance among economists | Structural analogies 31 outside / 31 within; superficial 7 / 6 | b11 | partial non-replication of Christensen and Schunn |
| GPT-3 beats students on standard text analogies | Digit matrices (N=40) generative OR 1.88, CI 1.21-2.91, p=0.005; multiple choice OR 6.27, p=2.3e-8; letter strings (N=57) OR 1.76, p=6.3e-5 | a13, b15, c07 (K05) | single-source (one lab) |
| GPT-3 weaker on story analogies, esp. far | N=54: OR 0.37, p=0.0003; near p=0.0039; far p=0.065 (not above chance) | b16, c07 | single-source |
| Counterfactual letter strings break GPT, not humans | Humans 0.753 (1,876 samples); GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (6,840 per model) | b17, c08 (K06) | established |
| Same on symbol alphabets in another lab | Adults 0.88/0.91/0.89 (Latin/Greek/Symbol, n=62); GPT-4o 0.85/0.63/0.48; Claude-3.5 0.68/0.62/0.46; Llama-3.1 405B 0.79/0.74/0.27; Gemma-2 27B 0.60/0.39/0.14; children 0.62/0.66/0.67 (n=41-42) | c09 (K06) | established |
| Independent critique | N=121 students; GPT-3 generative accuracy under 0.1 on synthetic alphabet for extend, successor, predecessor, fix-sequence | b19 | established with c08, c09 |
| Error types differ | Alternate valid rule: GPT-3 5.81%, GPT-4 22.00%, humans 38.59%. Incorrect rule: GPT-3 30.97%, GPT-4 32.67%, humans 14.67%. No GPT-3.5 row exists (earlier b18 was wrong) | a14, critique | established |
| Failure may be counting, fixed by code | GPT-4+code vs humans P=0.92; GPT-4 vs humans P<2e-16; GPT-4+CoT vs humans P=3e-8; code disabled 21.7% vs 22.5%, P=0.73; 38% of GPT-4 errors used a valid alternative rule; humans N=99/97. Preprint P=0.496 and 46% is superseded | d06 (K07) | contested |
| GPT-4 on digit matrices collapses when the blank moves | Original 0.813, alternate blank 0.480, symbols 0.790 | d07 | single-source |
| Far story analogies (18 problems) | GPT-4 total 0.75 (correct-first 0.89, second 0.61); humans 0.86 (1.0, 0.72) | d07 | single-source |
| ARN: far analogy vs near distractor is the hard cell | GPT-4 29.1, GPT-3.5 21.7, SBERT 1.0; humans 91.4; random 50. GPT-4 across four cells 94.0 / 92.5 / 57.1 / 29.1 (avg 68.1). Headline 39.6% = mean of two far cells (45.3, 33.9) over 9 systems; GPT-4 alone 43.1; human far avg 94.1 | a15, d01, d02 (K08) | established |
| Extracting each story's message first helps far analogies | CoT demos with message extraction: up to +30 points (read from figure); plain demos about +10 and hurt near | d03 (K21) | single-source |
| Story analogy falls with length | AnaloBench 1/10/30 sentences: GPT-4 89.1/66.5/60.7; GPT-3.5 65.3/46.4/30.8; Claude 68.2/30.2/25.9; humans 96.0/72.5/73.3; retrieval from 200 stories near random | d10, d11 (K28) | single-source |
| StoryAnalogy | ChatGPT about 30% multiple choice vs humans over 85% (24K pairs) | d22 | single-source |
| Reasoning models on abstract relations | Nonword analogies: gpt-oss-120B 83.85, 20B 83.27; Llama 3.1 405B 55.19, 3.3 70B 47.31 (1,364 problems); shuffled order: 79.81, 77.50, 55.39, 48.27 | d20 (K29) | single-source |
| o3 matches humans with different rules | ConceptARC text, 480 tasks: humans 73.0; o3 77.1 (medium); Claude Sonnet 4 60.2; Gemini 2.5 Pro 66.0. About 27% of correct o3 and Gemini answers use wrong or unintended rules; Claude 19%; humans 7%. Annotator agreement 84.8%, kappa 0.70 | d08, d09 (K22) | single-source |
| Python tools do not help on text abstraction | o3 77.1 to 75.6; Claude 60.2 to 55.0; Gemini 66.0 to 60.4. Visual o3 5.6 to 29.2 with tools | d08 | single-source |
| Analogical prompting | GSM8K GPT-3.5 77.8 vs 75.8 (0-shot CoT) and 76.7 (5-shot CoT); MATH 37.3 vs 33.9 / 34.9; davinci-003 GSM8K 61.0 vs 50.3 / 54.0; K=1..5: 76.1, 77.0, 77.5, 77.3, 77.8; diverse 77.8/37.3 vs non-diverse 75.9/35.2; plus self-consistency 85.3/46.0; Codeforces GPT-4 19 vs 16-17 | a16, b24, b25, c10, c11 (K09) | single-source |
| Small models need real exemplars | curie-001 and davinci-001 prefer labelled few-shot; K=1 hurts | b25 | single-source |
| Thought Propagation | Shortest path optimal rate, GPT-4: IO 0.78, CoT 0.76, ToT 0.46, TP 0.88; GPT-3.5: 0.33 / 0.26 / 0.22 / 0.65; one layer costs about ToT tokens | d14 (K26) | single-source, 2023 models |
| Step-Back (state the principle first) | MMLU Physics/Chemistry: GPT-4 CoT 82.9/85.3, Step-Back 84.5/85.6 (+1.6/+0.3); PaLM-2L CoT 65.0/75.3, Step-Back 73.2/81.8; fixes 20.5% of errors, introduces 11.9% | d15 | single-source |
| Physics-engine simulation | Mind's Eye: +27.9 points zero-shot, +46.0 few-shot on 39 tasks; GPT-3 1.3B with it 29.8% vs vanilla 175B 29%; one subtask 46.7 to 84.2 | a17 (K10) | single-source |
| Simulation does not help with a rule shortcut | Ring of 12, n=200: CoT 52.5 vs VoT 49.5 | a18, d19 | single-source |
| System complexity is the killer in law discovery | GPT-5 vanilla 90.3/90.3/87.5 (easy/medium/hard); complex system 72.9/63.2/40.3; Gemini-2.5-pro vanilla hard 69.4 vs complex hard 16.7; non-thinking models under 10% | c01, c02 (K13) | single-source |
| Code tool helps weak models, slightly hurts strong | GPT-4.1 5.8 to 18.9 (+13.1); GPT-4.1-mini 5.1 to 14.7; DeepSeek-V3 8.9 to 13.3; GPT-5 75.9 to 73.3 (-2.6); GPT-5-mini 53.1 to 48.1; o4-mini 47.8 to 45.1; DeepSeek-R1 43.4 to 37.4; Gemini-2.5-flash 50.6 to 40.9 (-9.7); Gemini-2.5-pro gains on hardest cell 16.7 to 22.2 | c03, d04 (K14) | established as a pattern |
| "Less exploration" is the cause | Trace-word exploration rate on two models; correlational; guardrail untested | d05 (K23) | contested |
| Small noise damages law discovery | GPT-5-mini at noise 0.0001 lost 12-16% relative | c04 | single-source |
| Equation benchmarks measure memory | LLM-SRBench: 239 problems; best symbolic accuracy 31.53% (Transform), 28.1% (Synth) | c16 (K15) | established |
| Non-LLM systems rediscover laws | AI Feynman 100/100 vs Eureqa 71% (68% in its conclusion); 20 bonus 90% vs 15%; AI-Newton: 46 experiments, about 90 concepts, 50 laws, 48 h | c18, c19, c20 (K16) | established |
| LLM-SR | E. coli OOD NMSE 0.0037 vs PySR 1.0141; 2.5K iterations vs 2M+; loses on Oscillation 2 OOD (0.0291 vs uDSR 0.0015) | a19, c17 | single-source |
| Pre-1900 model gives only glimpses | 3.3B params, about 22B tokens; CORE 0.1400 (pre-1900) vs 0.2602 (FineWeb-Edu) | c05, c06 (K17) | single-source |
| LLM ideas rated more novel, less feasible | Novelty human 4.84 (n=119), AI 5.64 (n=109), AI+rerank 5.81; idea-level AI 5.62, p=0.03; feasibility 6.61 vs 6.34 (ns); excitement 4.55 vs 5.19 (p=0.04); 49 ideas per condition, 79 reviewers, 298 reviews; about 200 of 4,000 non-duplicate; best LLM judge 71.4% pairwise | b26, b27, c12 (K11) | single-source |
| Novelty does not survive execution | AI novelty 5.778 to 4.729 (-1.049); human 4.912 to 4.903; execution-stage gap p=0.586; excitement -1.760; overall -1.976; 43 experts, 19 human and 24 AI ideas | d12 (K24) | single-source |
| Far inspiration helps little | MOOSE novelty (GPT-4 judge): random 2.957, BM25 3.364, ground-truth inspirations 3.000; MOOSE pipeline novelty 2.483 to 3.390; experts 2.276 to 3.197; SciMON: ground truth better in 85% of pairs, 55.6% of ideas gained novelty in loop 1, 57.8% in loop 2 | a20, b28, b29, c13, c14 (K12) | established (weak effect) |
| Planned retrieval raises diversity | Nova: 3.4x unique ideas; 37.5% of top-4 in a 10-expert panel (17.53% of worst-4) | d13 | single-source |
| Chain-of-Ideas | Human ELO: real paper 1100, CoI 1085, RAG 1029, AI-Scientist 812; gains stop at chain length 5 | c24 | single-source |
| Facet recombination | Scideator: 22 researchers, p<.01 creativity support; retrieval top-10 hit 89.66% vs 5-14% ablations | b30 | single-source |
| Inspiration retrieval in chemistry | MOOSE-Chem hit ratio (top 4% of 300): GPT-4o 83.7%, Llama-70B 83.0%, Llama-8B 43.5% | c15 | single-source |
| Human analogy rescues a small model | Qwen-2.5-7B, pre-1936 corpus: unguided 2/20; with grain-silo analogy 20/20 (p<0.001); Stokes' Law used 0/20 vs 18/20 | d16 (K25) | single-source |
| Agents on real science tasks | ScienceAgentBench 102 tasks: Claude-3.5 self-debug 32.4%. DiscoveryWorld 120 tasks: humans (N=11) 66% vs best agent 38% easy, 18% challenge | c21, c22 | single-source |

## 4. Mechanisms and models

### 4.1 Staged hybrid-model construction (Nersessian), as a procedure
Implementable as a chain of model calls gated by code. Input: a target problem with known constraints and an impasse.
1. State target constraints. List 2-5 hard facts the answer must satisfy. Code stores the list.
2. Retrieve sources. Ask for 2-3 source domains whose structure could carry those constraints. Code dedups. (Retrieval is the weak point: d11, d16.)
3. Narrow. For each source, write which features survive the target constraints and which are dropped. Output a typed mapping: object to object, relation to relation.
4. Build the hybrid. Write the intermediate model as an explicit object (state variables, rules) carrying source mechanics and target constraints.
5. Simulate. Run it. If the state is hard to track, call code (grid, small program, physics engine). Mind's Eye gave +27.9 points, but ring navigation shows no gain where a rule shortcut exists (a17, d19).
6. Find the failure the simulation exposes (Maxwell's friction), add a constraint, borrow a fix from a second source if needed (idle wheels). Max 2 rounds.
7. Generic abstraction. State what the working model shares with a class of systems; carry the class statement, drop the mechanism. Step-Back tests this step alone: small on strong models (+1.6, +0.3 for GPT-4), larger on weaker (PaLM-2L +8.2, +6.5 over base on physics, chemistry) (d15).
8. Check by code on held-out or mutated inputs (G3). The mapping is a hypothesis, not proof.

### 4.2 Structure mapping (Gentner), as an algorithm
- Represent each side as predicates with arguments (relations between objects, higher-order relations).
- Align: find a one-to-one mapping that maximises matched relations, preferring connected systems of relations (systematicity).
- Project: unmatched source relations connected to the match become candidate inferences about the target.
- Re-represent: if the match is poor, rewrite predicates so they align (Kepler: "instantaneous" to "acts in time").
- Alignable differences: after alignment, list differences tied to the match. These are the informative ones (the eclipse test).
- Implementation: the model emits predicate lists; code does the alignment count. Whether LLM-written predicates are reliable enough is untested.

### 4.3 Message extraction first (ARN)
Per story, write a one-line abstract message (proverb level). Compare messages, not surface text. CoT demonstrations that extract the message first gave up to 30 points on far analogies (d03). Cheap variant for retrieval: index the relational skeleton, not the text (AnaloBench retrieval on raw stories is near random, d11).

### 4.4 Analogical prompting and Thought Propagation
- Analogical prompting: "recall 3 relevant, diverse problems, solve them, then solve this one." Needs a capable model; K=1 hurts; 3-5 is enough (b25, c11).
- Thought Propagation: propose analogous problems, solve each, aggregate their solutions to refine the target answer. One layer costs about ToT tokens (d14).

### 4.5 Why counterfactual tests matter
A counterfactual task keeps the structure and changes surface and convention (permuted alphabet, symbols, moved blank). If accuracy drops, the model leaned on memorised surface patterns. If it holds, it used structure. Use as a probe for the agent (c08, c09, d07).

## 5. What holds up

Replications and agreement:
- Counterfactual letter-string failure was found by three groups (Lewis and Mitchell, Hodel and West, Stevenson et al.) across models from GPT-3 to GPT-4o, Claude-3.5, Llama-3.1, Gemma-2. Adults hold at 0.88-0.91 on all alphabets (K06). Caveat: they form one debate around one task family.
- The far-analogy-vs-similar-distractor failure appears in ARN (GPT-4 29.1), AnaloBench (length, retrieval), StoryAnalogy (ChatGPT about 30%), Webb story analogies (far not above chance) and Lewis and Mitchell far stories (GPT-4 0.75 vs 0.86 humans). Different groups, same direction.
- Expert analogies are structural, not surface (b08, plus base rates in b10).
- LLM idea novelty is fragile: 5% unique (b27), best LLM judge 71.4% pairwise, and the novelty gap vanished after execution (d12).
- Equation-discovery benchmarks on known equations overstate ability (c16).

Failures, non-replications, contested:
- Webb's headline (GPT-3 reasons by analogy) does not generalise to counterfactual forms. Webb's reply says code execution closes the gap (P=0.92 published) and the cause is counting. The code-disabled control (21.7% vs 22.5%) supports it. It is GPT-4 only; no reasoning model tested (K07).
- Lewis and Mitchell, and Hodel and West, argue lack of generalisation. Both fit the data; neither isolates tuning. GPT-3.5 under GPT-3 (0.350 vs 0.488) is confounded by prompt format (K20).
- "Near for fixes, far for new concepts" (Dunbar) is contested. Microbiology labs: 98% within domain, so far analogy is rare in real discovery. Political writing: no goal effect (K19).
- Christensen and Schunn's surface-similarity constraint did not hold in economists (b11).
- Preprint P=0.496 / 46% became P=0.92 / 38% in the published reply (d06). Use the published figures.
- Maxwell and Kepler readings: no independent replication; Hanson's Kepler reading was rejected by historians (d18). Kepler coding was chosen by the authors (a05).

Moderators:
- Model strength. Analogical prompting needs a capable model (b25). Code helps weak models and slightly hurts strong ones (d04). Step-Back helps weak models more (d15).
- Story length: accuracy falls, scale stops helping (d10).
- Surface-similar distractors cause the below-chance results (d01, d02).
- System complexity, not equation difficulty (c02).
- Observation noise (c04).
- Setting and audience set analogy distance for experts (d17).

Interventions that worked:
- Message-extraction CoT demonstrations on far analogies (up to +30, figure-read) (d03).
- Code execution for position and counting in permuted alphabets (d06).
- Physics engine for physical outcomes (+27.9 zero-shot) (a17).
- Self-generated diverse exemplars, small gains (+2 GSM8K, +3 to +4 MATH); self-consistency adds more (85.3) (c10, c11).
- Human-supplied analogy to a 7B model (2/20 to 20/20): shows source choice is the bottleneck (d16).
- Planned retrieval (Nova 3.4x unique ideas) (d13); facet-based retrieval (Scideator) (b30).

Interventions that did not work or hurt:
- Plain demonstrations on near analogies (hurt) (d03).
- Chain of thought on counterfactual letter strings (P=3e-8 vs humans) (d06).
- Code tools on text abstraction (o3 -1.5, Claude -5.2, Gemini -5.6) and on strong law-discovery agents (d04, d08).
- VoT where a rule shortcut exists (d19).
- Random vs BM25 inspiration: tiny novelty difference (2.957 vs 3.364 under a GPT-4 judge) (b28).
- Retrieval from a 200-story bank: near random (d11).
- Steering a small model (layer 18, strength 4.5): 0/20 and incoherent text (d16).
- LLM self-judging of ideas (b27). MOOSE, SciMON and SciAgents are scored by LLMs; SciAgents' five self-scored runs got 6-8 with no validation (c23).

## 6. Language models

Most models tested are 2022-2024. Evidence on 2025-2026 reasoning models is adjacent only.

Standard analogy tasks (GPT-3, Webb 2023): beats students on digit matrices and letter strings, loses on story analogies (a13, c07). One lab made the human baselines.

Counterfactual forms: every LLM drops; humans do not. GPT-4o on Latin/Greek/Symbol 0.85/0.63/0.48; Llama-3.1 405B 0.79/0.74/0.27; adults 0.88/0.91/0.89 (c09). GPT-4 digit matrices: 0.813 original, 0.480 when the blank moves (d07). What changed it: GPT-4 plus code matched humans (P=0.92); CoT did not (d06). Error profile: more incorrect-rule errors (GPT-4 32.67% vs humans 14.67%), fewer valid alternative-rule errors (22% vs 38.59%) (a14).

Narrative analogy: the failure is far analogy against a near distractor (GPT-4 29.1, humans 91.4). Near analogies are fine (GPT-4 94.0). Plain similarity (SBERT) reaches 77.9% in the near setting and 1.0 on far-vs-near-distractor. Message-extraction CoT demonstrations moved far analogies by up to 30 points. Length hurts: GPT-4 89.1, 66.5, 60.7 at 1, 10, 30 sentences; retrieval from 200 stories is near random.

Reasoning models: gpt-oss gets about 83-84% on abstract nonword analogies vs Llama 47-55% (d20). On ConceptARC text o3 reaches 77.1 vs humans 73.0, but a quarter of correct answers rest on wrong rules (27% o3 and Gemini vs 7% humans) (d08, d09). Rule-label consistency over repeat runs was only 66.0-70.9%, so rule scoring is noisy. No reasoning model has been run on counterfactual letter strings or ARN far cells in anything opened (K29).

Prompting: analogical prompting gives +2 points on GSM8K and +3 to +4 on MATH for GPT-3.5, +7 to +11 on GSM8K for davinci-003, and +2 to +3 on Codeforces for GPT-4. Small models do worse. Step-Back: PaLM-2L physics 65.0 to 73.2; GPT-4 82.9 to 84.5. Thought Propagation: shortest path GPT-4 0.88 vs CoT 0.76 vs ToT 0.46.

Simulation: Mind's Eye gives +27.9 zero-shot and lets a 1.3B model match a 175B (29.8 vs 29). VoT helps navigation and tiling, not the ring task.

Scientific discovery agents: NewtonBench shows a reasoning-model gap (GPT-5 75.9 vs non-thinking under 10%) and a complexity cliff (87.5 hard vanilla vs 40.3 hard complex). Code interpreter: +13.1 for GPT-4.1, -2.6 for GPT-5. DiscoveryWorld: best agent 38% easy, 18% challenge, humans 66%. ScienceAgentBench 32.4%. LLM-SRBench best 31.53%.

Idea generation: blind human novelty 5.64 for LLM vs 4.84 for experts, then no novelty edge after execution (4.729 vs 4.903). Duplication is severe. Far inspiration retrieval changes novelty a little and is mostly judged by LLMs.

Historical rediscovery: a 3.3B pre-1900 model gives glimpses only (energy quanta; sometimes sees equipartition fail at high frequency). A 7B model with the right material in context solved the cracking counterfactual 2/20 alone and 20/20 with a human-given analogy. A person supplied the analogy, so this shows retrieval is the bottleneck, not self-directed analogy.

Direct test of the cognitive-historical method on a model (staged hybrid-model operator vs unstructured analogy): none found (K26).

## 7. What our agent should take

Marks as in SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Counterfactual and mutated probes for any analogy or transfer claim.** Part: G3, S8, bench. [E] K06, K15. Evidence: b17, c08, c09, b19, c16. Report the drop from canonical form. Standard forms hide reciting.
2. **A recalled "far analogy" is a hypothesis; map by explicit correspondence and verify in code.** Part: O7 (supports the existing [E] that unaided analogy rarely transfers). [E] K02, K08. Evidence: d01, d02, b08. A surface-similar distractor is the hazard.
3. **Set source distance by setting, not by a "go far" default.** Part: O7. [E] K02. Evidence: b08, b10, d17. Real lab experts are mostly within domain. Default medium; go far only after medium fails.
4. **Do not add a code tool without checking the agent still explores.** Part: G12, O6. [E] as a pattern, K14. Evidence: c03, d04, d08. Offer code for counting, position and arithmetic; not as default for hypothesis search on strong models.
5. **Score the stated rule, not only the answer.** Part: G10, S8. [E]-adjacent: the 27% figure is single-source (K22) but fits G10. Evidence: d08, d09, a14. Log the rule; have code compare it with held-out behaviour.
6. **Judge analogy-sourced ideas by running them; dedup before ranking.** Part: G8. [E] K11, K24 with F01/F05. Evidence: b26, b27, d12, b28.
7. **Treat case-study evidence as design rationale only.** Part: doc discipline. [E] K04. The Maxwell staging stays [S].

### Test first (not yet in the schema)

1. **Staged analogy operator for O6/O7** (state target constraints, pick source, narrow, build hybrid, simulate, abstract, check). Part: O6/O7 at S6. [S] K01, K26 (open). Evidence: a02, a03, a21, b06, d14, d15. No direct test exists.
2. **Message or skeleton extraction before comparing cases.** Part: O7, memory. [S] K21, K28. Evidence: d03, d10, d11.
3. **Explicit align, project, re-represent, check-differences steps.** Part: O7. [S] K03. Evidence: a05-a08.
4. **Self-generated diverse analogous problems vs self-consistency at equal tokens.** Part: O7. [S] K09, K26. Evidence: a16, c10, c11, d14. Self-consistency added more than the analogy step.
5. **Simulate step only where no rule shortcut exists.** Part: O6. [S] K10. Evidence: a17, a18, d19.
6. **Forced-exploration quota alongside a code tool.** Part: G12, O6. [C] K23. Evidence: d05, c03.
7. **Isolate sub-models in complex systems (Maxwell's partial models).** Part: O3, O6. [S] K13. Evidence: c02.
8. **Write explicit correspondences before transfer.** Part: O7. [S] K18. Evidence: b12-b14 (human education studies).
9. **Source distance by goal (repair vs invent), medium vs far.** Part: O7. [C] K19. Evidence: a11, d17, d18.
10. **Code tool for counting on a reasoning model for analogy items.** Part: G, O7. [C] K07. Evidence: d06, b20.
11. **Lessons stored as relational skeletons.** Part: memory. [S] K28. Evidence: d10, d11.

## 8. Concrete tests on our bench

All arms at equal total tokens, same model, same items, at least 5 seeds, bootstrap CIs.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Counterfactual transfer: ARC-style tasks with permuted colour or symbol mapping, plus originals; reworded BRAINTEASER items | plain thinking vs staged operator | accuracy drop (mutated minus original) | Smaller drop with the operator if it uses structure; none expected on originals |
| T2 | Far-analogy vs near-distractor pairs (ARN-style, about 100 built from our bank) | direct comparison vs message-extraction first vs staged operator | accuracy on the far-vs-near-distractor cell | +10 to +30 for message extraction (d03); no loss on near cell |
| T3 | Impasse items with plain pass rate 10-60% | plain vs analogical prompting (3 diverse) vs staged operator | pass rate; tokens to first pass | Operator +3 to +8 over plain on a strong model; analogical prompting +0 to +3 |
| T4 | Items where a shortcut rule fits the examples but not held-out inputs | answer only vs answer plus stated rule checked by code | share of correct answers resting on the wrong rule | Fewer wrong-rule successes (from about 25% toward 10%) |
| T5 | State-tracking items (grids, counts) with and without a rule shortcut | text only vs code tool vs simulate step | accuracy by item class and tokens | Gains only on no-shortcut items; null on shortcut items (as d19) |
| T6 | Hidden-rule systems with 1 vs 3 interacting parts | tool only vs tool plus exploration quota (minimum N probes before fitting) | accuracy on 3-part systems | Quota recovers part of the loss on strong models; none on weak |
| T7 | Lesson retrieval | raw-text vs relation-skeleton index | hit rate of correct analogue in top 3; downstream pass rate | Skeleton beats raw (raw retrieval near random in d11) |
| T8 | Open design items | idea with analogy source vs without, judged by running a spec check | executed success rate; uniqueness after dedup | Rating gain vanishes after execution (d12); look for any execution-level gain |
| T9 | Permuted-alphabet letter strings | plain vs code tool vs CoT | accuracy | Code closes the gap if counting is the cause (d06); shows if a reasoning model already does |
| T10 | Cases of 1, 10, 30 sentences | direct vs summarise-to-skeleton first | accuracy by length | Smaller decay with length |

## 9. What does not transfer, and why

- **The Maxwell timeline as a recipe.** It is one author's reading of one genius over years. Our agent has a token budget and small problems. Only the staged structure is borrowed, as a hypothesis (K01, K27).
- **Ethnography.** Distributed lab cognition (whiteboards, wikis, physical models, people) has no counterpart in a single-agent loop (a09, a10). Closest: the code-run model and lesson memory.
- **Mental imagery and gesture.** Human imagistic simulation (a04, b05) maps only loosely to text grids or physics engines, and only where state is hard to track.
- **Years of incubation.** Kepler took 25 years and repeated one calculation at least 70 times (a08). Token-capped runs cannot copy that; incubation effects failed to replicate (SCHEMA 4b).
- **Dunbar's "far for new concepts".** Real labs are 98% within domain (d17). A fixed far default would not match expert practice, and ARN shows far analogy against a similar distractor is the failure.
- **Child and education findings** (b12-b14). Hints toward explicit correspondences only; effect sizes not given; human learners.
- **Benchmarks on known laws.** Rediscovery measures memory (c16), and non-LLM systems solve all 100 Feynman equations (c18). LLM success says nothing about model-based reasoning.
- **Pre-1900 training test.** Needs model training (c05); not possible for a scaffold.
- **LLM-judged novelty results** (MOOSE, SciMON, SciAgents). The judge is a model; G8 forbids relying on it.

## 10. Open questions

1. Does a staged hybrid-model operator beat plain analogical prompting at equal tokens on a 2025-2026 reasoning model? No test exists (K26).
2. Do current reasoning models still fail counterfactual letter strings and symbol analogies, and does code close the gap?
3. Do current models still fail far-vs-near-distractor narrative analogies, and does skeleton-first retrieval fix it?
4. What are Dunbar's primary in-vivo numbers? Only second-hand.
5. Has anyone replicated the Maxwell or Kepler readings, or have historians objected? None found; search was rate limited.
6. Is simulation worth its tokens? Break-even never measured.
7. Does a forced-exploration guardrail remove the code-tool loss? Never tested.
8. Does far inspiration raise human-judged novelty without lowering feasibility once ideas are run? Not shown.
9. Which operator comes before real breakthroughs, and at start or at impasse? The SUBFIELDS questions (a) and (b) rest on three to five hand-picked cases and no counts.
10. Unresolved numeric conflicts: human sample in Lewis and Mitchell (about 46 vs 136; likely trial counts vs recruits); Eureqa 71% vs 68%; ARN rows partly read from prose.
11. Is the permuted-alphabet gap caused by chat tuning (GPT-3.5 worst) or by counting? Neither study isolates it (K20).

## 11. Sources

[V] = opened this session. [M] = snippet or second-hand only.

- [V] Nersessian (2007) Mental modeling in conceptual change. https://www.cc.gatech.edu/aimosaic/faculty/nersessian/papers/Nersessian-ModelingConceptualChange.pdf (a01-a04)
- [V] Gentner, Brem, Ferguson, Wolff, Markman, Forbus (1997) Analogy and creativity in the works of Johannes Kepler. https://groups.psych.northwestern.edu/gentner/papers/ (a05-a08; "4 candidate inferences" and "8 minutes of arc" not found on re-check)
- [V] Nersessian and Chandrasekharan (2009) Hybrid analogies in conceptual innovation in science. https://www.cc.gatech.edu/aimosaic/faculty/nersessian/papers/ (a09, a21)
- [V] Nersessian (2009) How do engineering scientists think? Topics in Cognitive Science. https://www.cc.gatech.edu/aimosaic/faculty/nersessian/papers/ (a10)
- [V] Nersessian (2025) How do scientists think? Topics in Cognitive Science. https://europepmc.org/article/PMC/PMC11792771 (b01-b04, d21)
- [V] Clement (2022) Multiple levels of heuristic reasoning processes in scientific model construction. https://europepmc.org/article/PMC/PMC9127582 (b05, b06)
- [V] Jaeger (2026) Complementarity as Relativity: Bohr's relativistic analogy. https://europepmc.org/article/PMC/PMC13703519 (b07)
- [V] Kretz and Krawczyk (2014) Expert analogy use in a naturalistic setting. https://europepmc.org/article/PMC/PMC4244599 (b08-b11, d17)
- [V] Richland and Zhao (2026) Relational reasoning and educational applications. https://europepmc.org/article/PMC/PMC12938770 (b12-b14)
- [V] Stanford Encyclopedia of Philosophy: Scientific Discovery. https://plato.stanford.edu/entries/scientific-discovery/ (a11, a24, a25, d18)
- [V] Stanford Encyclopedia of Philosophy: Models in science. https://plato.stanford.edu/entries/models-science/ (a12)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196 (a13, b15, b16, c07)
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning in LLMs. https://arxiv.org/abs/2402.08955 (a14, b17, c08; b18 corrected)
- [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215 (d07)
- [V] Hodel and West (2023/2024) Response: Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2308.16118 (b19)
- [V] Webb, Holyoak, Lu (2024/2025) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070 ; published: https://europepmc.org/article/PMC/PMC12107539 (b20, d06)
- [V] Stevenson et al. (2024) Can LLMs generalize analogy solving like children can? https://arxiv.org/abs/2411.02348 (c09)
- [V] Wu et al. (2024) Reasoning or reciting? Counterfactual tasks. https://arxiv.org/abs/2307.02477 (b21; per-task figures not read)
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626 (b22, b23)
- [V] Sourati et al. (2024) ARN: Analogical Reasoning on Narratives. https://arxiv.org/abs/2310.00996 (a15, d01-d03)
- [V] Ye et al. (2024) AnaloBench. https://arxiv.org/abs/2402.12370 (d10, d11)
- [V] StoryAnalogy (2023). https://arxiv.org/abs/2310.12874 (d22)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (a16, b24, b25, c10, c11)
- [V] Yu et al. (2024) Thought Propagation. https://arxiv.org/abs/2310.03965 (d14)
- [V] Zheng et al. (2024) Take a Step Back. https://arxiv.org/abs/2310.06117 (d15)
- [V] Liu et al. (2022) Mind's Eye. https://arxiv.org/abs/2210.05359 (a17)
- [V] Wu et al. (2024) Visualization-of-Thought. https://arxiv.org/abs/2404.03622 (a18, d19)
- [V] Beger et al. (2025) Distinguishing performance from competence (ConceptARC). https://arxiv.org/abs/2510.02125 (d08, d09)
- [V] Raemaekers (2026) Relational abilities of LLMs and large reasoning models. https://europepmc.org/article/PMC/PMC12837307 (d20)
- [V] Nature Communications (2026) Human analogical guidance amplifies LLM problem solving. https://europepmc.org/article/PMC/PMC13223311 (d16)
- [V] NewtonBench (2025). https://arxiv.org/html/2510.07172v2 (c01-c04, d04, d05)
- [V] LLM-SR (2024/2025). https://arxiv.org/abs/2404.18400 (a19, c17)
- [V] LLM-SRBench (2025). https://arxiv.org/html/2504.10415 (c16)
- [V] AI Feynman (2020). https://arxiv.org/html/1905.11481 (c18)
- [V] AI-Newton (2025). https://arxiv.org/html/2504.01538 (c19)
- [V] Li, Ji, Zhang (2022) From Kepler to Newton. https://arxiv.org/abs/2111.12210 (c20; abstract page only)
- [V] Hla (2025) Machina Mirabilis. https://michaelhla.com/blog/machina-mirabilis.html (c05, c06)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109 (b26, b27, c12)
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap. https://arxiv.org/abs/2506.20803 (d12)
- [V] SciMON. https://arxiv.org/abs/2305.14259 (a20, b29, c13)
- [V] MOOSE. https://arxiv.org/abs/2309.02726 (b28, c14)
- [V] MOOSE-Chem. https://arxiv.org/html/2410.07076 (c15)
- [V] Scideator (2026). https://arxiv.org/abs/2409.14634 (b30)
- [V] Nova (2024). https://arxiv.org/abs/2410.14255 (d13)
- [V] ScienceAgentBench (2024). https://arxiv.org/html/2410.05080 (c21)
- [V] DiscoveryWorld (2024). https://arxiv.org/html/2406.06769 (c22)
- [V] SciAgents (2024). https://arxiv.org/html/2409.05556 (c23)
- [V] Chain-of-Ideas agent (2024). https://arxiv.org/html/2410.13185 (c24)
- [M] Nersessian (2008) Creating Scientific Concepts. https://mitpress.mit.edu/9780262515078/creating-scientific-concepts/ (a22); blurb https://www.nhbs.com/creating-scientific-concepts-book (c27)
- [M] Maxwell (1861-62) On Physical Lines of Force. https://doi.org/10.1080/14786446108643067 (a23, not read)
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery (a24, via SEP)
- [M] Dunbar (1995, 1997, 2001) in vivo studies (a25, via SEP and Kretz and Krawczyk)
- [M] Officechai coverage of Machina Mirabilis. https://officechai.com/ai/someone-built-an-llm-to-test-out-d (c25)
- [M] LLM-Feynman (2025). https://arxiv.org/pdf/2503.06512 (c26; snippet: over 90% of Feynman formulas)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 4 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D07.03-K04** (reworded: the sources support less). Sources are mostly Nersessian's own work; SEP presents model-based reasoning as one perspective with critics and one of several approaches, not as established how scientists generate new concepts. Corrected claim: Model-based reasoning (analogical, visual, simulative) is argued, chiefly by Nersessian, to be a key way scientists generate new concepts; this rests on historical case studies and ethnography of labs, argued by a bootstrapping method rather than statistics.
- **D07.03-K08** (number corrected). Table 2 of Sourati et al. averages 12 rows (SBERT plus 11 LLM variants), not 9 systems; recomputing the far-vs-near column over those 12 gives 33.9. Corrected claim: Models fail ARN when a far analogy competes with a surface-similar distractor: 29.1% for GPT-4 and 33.9% on average over the 12 systems in Table 2 (random 50%, humans 91.4%). The 39.6% headline is the mean of the two far-analogy cells (45.3 and 33.9) across all 12 systems, not a single-model far-analogy score. GPT-4 on far-vs-far is 57.1.
- **D07.03-K12** (reworded: the sources support less). MOOSE does not describe BM25 inspirations as far, and its BM25 novelty (3.364) is close to ground-truth hypotheses (3.380) and above ground-truth inspirations (3.000), so 'only modestly' and 'fall short of real papers' are not supported by MOOSE; the 85% figure is SciMON only. Corrected claim: Retrieving inspirations raises GPT-4-judged novelty in MOOSE (2.957 with random inspirations to 3.364 with BM25 inspirations, close to the 3.380 of ground-truth hypotheses), while in SciMON expert comparison the original paper's idea was judged higher in technical level and novelty in 85% of comparisons, so generated ideas still fall short of real papers in that study.
- **D07.03-K15** (reworded: the sources support less). LLM-SRBench's 31.5 and 28.1 percent are for the best system evaluated there (GPT-4o-mini-era models), while NewtonBench on shifted laws reports 75.9 percent (GPT-5) and 65.4 percent (Gemini-2.5-pro), so 'best only 28-32 percent' is not general. Corrected claim: Benchmarks built on known equations may largely measure memory: on LLM-SRBench's transformed and synthetic problems the best system evaluated (LLM-SR with GPT-4o-mini) reached only 31.5 percent (LSR-Transform) and 28.1 percent (LSR-Synth) symbolic accuracy, although on NewtonBench's shifted laws frontier reasoning models reach 75.9 percent (GPT-5) and 65.4 percent (Gemini-2.5-pro), while non-reasoning models stay under 10 percent.
- **D07.03-K02** (now single-source: only one opened source, code check).
