# Computational reconstruction of discoveries: deep document

*Subfield D07.06. Sources: evidence_a-d.jsonl (a01-a28, b01-b30, c01-c30, d01-d18), claims.jsonl (K01-K33), critique.md in this folder. Evidence ids are quoted as a01, K05 and so on. Status tags: [E] established, [S] single-source, [C] contested.*

Short warning before the detail. Most of the evidence is on equation discovery, on weak or mid-size backbones, and on the authors' own benchmarks. Almost none of it tests a scaffold against a strong reasoning model at equal tokens. Read every number below with that in mind.

## 1. What it is

Computational reconstruction of discoveries means writing a program that finds a law, a model or a hypothesis that a scientist once found. The program gets data or facts and must produce the result. The goal is to test a theory of how discovery works. If cheap, explicit steps rebuild the result, then those steps are a sufficient account of the process.

Three eras share this idea.

1. **The 1977-1990 symbolic era.** BACON, ABACUS, STAHL and their relatives. Production rules rebuilt gas laws, Kepler's law, Ohm's law and 18th-century chemistry. Founders: Langley, Simon, Bradshaw, Zytkow. Human companion work: Klahr and Dunbar (1988), Qin and Simon (1990), Klahr and Simon (1999).
2. **The 2009-2023 symbolic-regression era.** Eureqa, AI Feynman, PySR, SRBench. Same loop, bigger search space, loosened data conditions, noise.
3. **The 2023-2026 language-model era.** LLM-SR, LaSR, LLM-SRBench, SR-Scientist, NewtonBench, DiscoveryWorld, FIRE-Bench, SciLaws-Bench. The language model is the proposer or the agent. The old loop remains: propose, fit, score, revise.

Why it matters for our agent. Our schema is a scaffold that tries to make one model think better. A discovery task is a clean test of a schema step. The task has a hidden rule, code can check answers, and the answer can be scored on points the model did not see. So this field gives us (a) a family of tests where checks are cheap, (b) a list of which loop parts pay, and (c) a long list of ways such tests mislead. The field is also a warning. Famous laws are recalled by language models, so a rediscovery of a famous law proves little (K03).

## 2. History and theories in depth

### 2.1 The founding claim

Langley, Simon, Bradshaw and Zytkow (1987, a25, book, not opened) argued that discovery is heuristic search in problem spaces and needs no special faculty. Each program was run on a historical episode. The book was borrow-only and we did not read it. Counts below come from the original papers and from a rival group's account (a06).

### 2.2 BACON

- **BACON.1 (Langley 1977, a01, opened).** A production system in an artificial 2-D world. Data are attribute-object-time-value 4-tuples. Regularity detectors fire on working memory. A constant leads to a generalisation. A steady rise or fall leads to a new attribute built from the change. One value up while another goes down leads to a product term. The paper has four pages and no counts. Its own limits: no conditional laws, built-in knowledge of which dimensions to generalise over, no noise handling. Quote: "once an hypothesis is formed, it is never rejected".
- **BACON.3 (Langley 1979, a02-a04, opened).** Five laws from generated data with one heuristic set: ideal gas law, Kepler's third law, Coulomb's law, Ohm's law, Galileo's laws. Key idea: levels of description. A regularity at one level becomes a datum at the next. Defined terms are treated like observed ones. The system had 86 OPS2 productions in 7 sets: 17 gather data, 16 note regularities (constancy and trend), 3 for term values, 22 to decompose and check new terms against old, 3 to collapse equal descriptions, 8 for irrelevant terms. Ideal gas path: pV constant per (n,T), then pV/T linear in T with slope 8.32, then pV/nT = 8.32.
- **BACON.3 cost table (a03).**

| Law | Productions fired | Defined terms | Redundant terms | Levels | Descriptions |
|---|---|---|---|---|---|
| Ideal gas | 1203 | 8 | 2 | 4 | 27 |
| Kepler | 1119 | 17 | 1 | 3 | 18 |
| Coulomb | 1297 | 18 | 12 | 4 | 27 |
| Galileo | 1150 | 9 | 7 | 3 | 23 |
| Ohm | 4593 | 31 | 84 | 5 | 54 |

  One run per law, so no variance. Ohm's law took about four times the work because many terms were related and 84 redundant terms had to be rejected.
- **Order effects (a04).** The final law did not depend on data order, but cost did. Varying irrelevant variables first found them irrelevant at once. Varying them last reached the same laws with more computation. The author admits the irrelevant-variable result is misleading because irrelevant variables could be added to each task by hand.
- **Later versions (a06, rival account).** BACON.4 added intrinsic properties and common divisors. BACON.5 added symmetry. BACON.6 needs a given law form but handles trig and algebraic laws. A parallel line (Kokar's COPER, El-Shafei's HOTEP) uses dimensional analysis, which needs relevant variables known first.
- **Review view (c01, c02, Kramer et al. 2023).** BACON looked at pairs of variables with all else fixed and built ratios and products until one stayed near constant. It re-derives Kepler as D^3/P^2 = k. One tolerance parameter decides when a term counts as constant. It needs ceteris paribus data, which the review calls a strong assumption. Descendants (Lagramge, ProGED, SINDy, AI Feynman 2.0) keep the generate-and-test loop and widen the search space.

### 2.3 ABACUS and STAHL

- **ABACUS (Falkenhainer and Michalski 1986, a05, opened).** Learns separate equations for data subsets plus logic-style conditions saying when each equation holds (it joins with AQ11). It adds units analysis, proportionality-graph search and suspension search. CPU seconds on a Sun workstation: ideal gas 15 events 3 s; momentum 22 events 68 s; Coulomb 36 events 74 s; Stokes 72 events 49 s; kinetic energy 12 events, 987 nodes, 855 s; chemistry 30 events 31 s. Noise: correct at 0.2 percent, worse at 2 percent. The authors say real data would rule out even 0.2 percent. Quote: "much of this power is achieved by requiring the user to provide a form of the answer". Sums and differences are much harder than products and ratios.
- **STAHL (Zytkow and Simon 1986, a07, a08, opened).** Rebuilds 18th-century componential chemistry from reactions fed in published order. It infers components (charcoal burning means charcoal = phlogiston + ash) and repairs conflicts. It reproduces the century-long phlogiston theory and also Black's mild alkali model and Lavoisier's oxygen theory with the same rules. Its limits, stated by the authors: cannot generalise (oxygen + metal gives oxide + caloric), cannot use properties of substances, does not design experiments, cannot choose between phlogiston and oxygen. Quote: "it does not demonstrate that this path was taken historically".
- **The validity rule from the same paper (a08).** One rediscovery shows one possible path only. A stronger test feeds data piecemeal in historical order and must also reproduce long-held errors. Errors typical of the epoch are diagnostic. This is a design rule for any claim that our step "reproduces discovery X".

### 2.4 The critique of the founding work

- Data were cleaned, variables were chosen by the programmer, and tasks were chosen by the authors (a25, b28, K02).
- Heeffer (2021, b30, search summary only) argues BACON did not use the data the original discoverers had, and induction from observation does not match how the historical laws were found (sine law, Kepler).
- Counted data are almost absent: one run per law, no variance (a03).
- The program showed sufficiency of a method on tidy inputs. It did not show that scientists worked that way.

### 2.5 The human side

- **Klahr and Dunbar (1988, d01-d03, opened in full).** The BigTrak study. Adults learned a programmable toy vehicle and had to find what its REPEAT key did. Search ran in two linked spaces: hypotheses and experiments. Details in section 3.
- **Qin and Simon (1990, b29, search summary only).** Laboratory replication of Kepler discovery: reportedly 4 of 14 subjects found the law (about 29 percent). Not verified (d18).
- **Klahr and Simon (1999, a27, not opened).** Review that joins computational and human work. Claims both lines agree. We have no numbers from it.

### 2.6 The symbolic-regression bridge

- **Eureqa (Schmidt and Lipson 2009, a28, not opened).** Genetic programming that favours equations that predict derivatives of the data. A check that does not depend on a fixed form.
- **AI Feynman (Udrescu and Tegmark 2020, a09-a11, b08-b09, opened).** Dimensional analysis, polynomial fit, symmetry, separability and a neural net for structure. Recursive splitting by structure found with checks. v2 (a11) keeps a Pareto frontier of accuracy against description length.
- **AI Descartes (Cornelio et al. 2023, b23).** Symbolic regression plus a logic prover that checks candidates against background theory. Re-found Kepler's third law from few points. Did not recover time dilation from data but picked the best-generalising formula. Axioms were elicited by hand per problem.
- **Cranmer et al. (2020, a23).** Train a graph network with sparse messages, then fit symbolic regression to its parts. Found a new dark-matter halo formula; the symbolic form generalised out of distribution better than the network.
- **PySR (Cranmer 2023, a24).** Open evolutionary regression; the base for LaSR; a cheap baseline that LLM papers must be set against.
- **AI-Newton (Fang, Jian, Li 2025, b22, c30).** Concept-driven symbolic system. Rediscovered Newton's second law, energy conservation and universal gravitation from 46 simulated noisy mechanics experiments. About 90 concepts and 50 general laws per test case, up to 1200 trials, about 48 hours a run. Builds simple concepts (mass) before complex ones (force) and reuses them. Not shown to use an LLM at its core.

### 2.7 The language-model line

The line runs LLM-SR (2025), LaSR (2024), LLM-SRBench (2025), SR-Scientist (2026), NewtonBench (2026), and 2026 preprints (SciLaws-Bench, library reachability, LLM-PySR, IGSR, KeplerAgent). Details in sections 3 and 6. The old question "which step of the loop is essential" is now asked again, with a language model as proposer.

## 3. Core findings with exact numbers

Status uses the claim file. "Single-source" means one independent group. Many rows lean on one paper family (LLM-SRBench and its authors' LLM-SR, plus SR-Scientist on the same benchmark), so independent counts are lower than line counts suggest (critique).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Cheap heuristics (find constant, find trend, define ratio or product, treat defined terms as data) rediscover classic product and ratio laws on clean data | 5 laws; 86 productions; 1119 to 4593 productions per law; Ohm 31 defined terms, 84 redundant | a01-a03, b28, c01 (K01) | [E] for sufficiency only; the data were clean and hand-chosen |
| Rediscovery of one episode shows one path only; a fair test needs historical order and must reproduce wrong turns | no counts | a07, a08, b30 (K02) | [S] |
| Final law independent of data order; cost depends on order | cost differs by order; no counts beyond tables | a04 (K20) | [E] on cost, small base |
| Staged build-up (simple concepts first, reuse) | AI-Newton 46 experiments, about 90 concepts, 50 laws, up to 1200 trials | b22, c30, a04 (K20) | [E] (3 sources) |
| No code-side redundancy check, term search explodes | Ohm: 31 defined, 84 rejected, versus 1 to 12 for other laws | a03 (K21) | [S] |
| Laws need scope conditions | ABACUS learns conditions; BACON.1 never rejects | a05, a01 (K22) | [E] for the need; no LLM test |
| Humans, Study 1 (Klahr and Dunbar) | N=20; 19 solved; 19.8 min (SD 9.6); 18.2 programs (SD 11.5); 364 programs (304 experiments, 51 control, 7 calibration); 17 of 20 began with the "N means number of repeats" frame; about 28% of experiments had no stated hypothesis; none began with the right rule | d01 (K27) | [S] |
| Humans split by how they escaped the wrong frame | 7 Theorists (memory) versus 13 Experimenters (experiment). Time 11.40 vs 24.46 min (t(18)=3.97, p<.0009); experiments 9.29 vs 18.33 (p<.006); experiments with no stated hypothesis 0.76 vs 6.08 (p<.002); different hypotheses 3.06 vs 4.92 (p<.08). Programming experience: 7 of 7 Theorists, 1 of 13 Experimenters | d02 (K28) | [S] |
| Humans keep refuted ideas and drop supported ones | 220 outcomes: confirmed hypothesis dropped in 21 of 84 (25%); disconfirmed hypothesis kept in 76 of 136 (56%) | d02 (K28) | [S] |
| Listing hypotheses first helps | Study 2, N=10; 4.2 hypotheses listed; 5 of 10 named the right rule; all 10 solved; 6.2 min, 5.7 experiments, 2.4 hypotheses. Theorists (N=4) 3.3 min, 3.0 experiments; Experimenters (N=6) 8.2 min, 7.5 experiments. In Study 1 under 10% of experiments used the right frame; in Study 2 half the subjects proposed it | d03 (K28) | [S] |
| Humans on Kepler data | 4 of 14 subjects (about 29%) | b29 (K26) | [S], unverified, search summary only |
| AI Feynman beats earlier tools (author report) | 100 vs Eureqa 68 on the Feynman set; 90 vs 15 on 20 bonus equations; 66.7 vs 48.9 on arbitrary functions. Abstract says earlier best was 71; Key findings says 68 | a09, a10, b08 (K11) | [S] author-reported; contradicts itself on baseline |
| AI Feynman under independent testing | SRBench: 53% exact noise-free, nearly twice the next (GP-GOMEA 27%); above noise 0.01, DSR, gplearn, AFP_FE, AFP recover more; black-box tasks below FFX and DSR (p <= 6.1e-5). 130 ground-truth, 122 black-box problems, 14+ methods | b10, b11 (K11) | [S]; SRBench figures not re-opened by the cross-checker |
| AI Feynman 2.0 noise robustness | 73 of 100 solved at noise 1e-1 (r=-1); 1 to 3 orders of magnitude more robust than v1; 80% of 10 distributions solved | a11, b09 (K10) | [E] relative to v1 |
| LLMs recite famous laws | LLM-SR: low error in under 20 iterations on Feynman problems; Mixtral perplexity lower on Feynman than on new problems. LLM-SRBench: Llama-3.1-8B on 100 Feynman problems shows sharp early error drops; gap holds at 0 to 15 expression nodes. SR-Scientist footnote: nearly 50% of LSR-Transform near-solved after the first iteration | b07, c05, b02, c08, b20 (K03) | [E] (4 sources) |
| Sharlin and Josephson leakage | Hubble, Kepler, Bode datasets too leaky for the main text; planetary period data recognised without context | c11 (K03) | [E] with K03; stated by authors, not measured |
| LLM-SRBench ceiling | 239 problems (111 LSR-Transform + 128 LSR-Synth). Best symbolic accuracy 31.53% (LLM-SR GPT-4o-mini) on Transform. Best per synthetic domain: chemistry 11.11, biology 25.30, physics 9.91, material science 28.12 (mean about 18.6). The paper's "28.1%" headline is one cell | a14, b01, c07 (K07) | [S]; judge is GPT-4o with 94.6% agreement with humans |
| Data-blind prompting is near useless | Direct prompting symbolic accuracy on LSR-Transform: Llama-3.1-8B 3.61, GPT-3.5 2.10, GPT-4o-mini 7.21; about 0% on most synthetic domains. Same backbones in LLM-SR: Llama-8B 30.63, GPT-3.5 10.81, GPT-4o-mini 31.53 | a15, b04, b06 (K05) | [E] (4 sources) |
| Classic baseline on the same set | PySR on LSR-Transform: symbolic 8.11, Acc0.1 56.76 (LLM-SR best 31.53 / 39.64). PySR symbolic 0% on chemistry and biology, 4.54% on physics | b03 (K04) | [E] |
| Good fit is not the law | LLM-SR GPT-4o-mini, material science: Acc0.1 88.28% but symbolic 20.24%. Symbolic accuracy correlates positively with out-of-domain Acc0.1 and negatively with OOD NMSE | a16, c08, c09, b04 (K04) | [E] |
| Fit and validity disagree | SciLaws-Bench: within a task, fit and validity agree on which of two models is better in 53.6% of 9,279 unequal-fit pairs; 66.4% only at fit margin >= 0.4; across models r=0.83; within GPT-6 across tasks r=0.06 | d07 (K30) | [S] 2026 preprint |
| Ablation, LLM-SR (one problem, GPT-3.5) | Oscillation 2 NMSE: no refinement 1.01e-1 in-domain / 1.81e-1 OOD; no skeleton plus optimiser 3.78e-1 / 3.75e-1. Removing the problem description hurt a lot; removing program form hurt less | a13, b06, c04 (K06) | [E] direction; one problem |
| LLM-SR vs classic regression (author) | about 2.5K iterations vs 2M+ for baselines; E. coli OOD NMSE about 0.0037 vs above 1 | a12, b05, c03 | [S] authors' benchmark, 4 tasks |
| SR-Scientist ablations (Acc0.01 / Acc0.001) | GPT-OSS-120B full 63.57 / 49.35; no analyser 35.66 / 16.28; no experience buffer 57.36 / 41.86; no top-k 58.14 / 41.86. Qwen3-Coder-480B full 49.09 / 24.55; no analyser 41.08 / 14.73; no buffer 35.66 / 16.28; no top-k 26.36 / 13.70. GLM-4.5-Air full 48.32 / 25.06; no analyser 46.51 / 22.48; no buffer 37.21 / 18.61; no top-k 41.96 / 21.71. About 1000 LLM calls per problem, 3 repeats averaged | a18, a19, b19, c17 (K08) | [E] direction; the winning part depends on backbone. "No top-k" means random sampling from the buffer |
| SR-Scientist margin | 6 to 35 points absolute over baselines in 4 fields; classic non-LLM rows 0.00 to about 3% Acc0.01 | a18, c16, c18 | [S] authors' system; LSR-Synth only |
| LaSR on Feynman | Exact solves of 100: GPlearn 20, AFP 24, AFP-FE 26, DSR 23, uDSR 40, AI Feynman 38, PySR 59, LaSR 72 (GPT-3.5, p=1%). Llama3-8B at p=1/5/10%: 67/69/71. Intro says 66; Table 1 says 72. PySR with 10 hours per equation reaches about 62 | a17, b12, c15 (K13) | [C] |
| LaSR on a recall-controlled set | 5.41 to 12.61% symbolic on LSR-Transform (Acc0.1 45.94 to 50.45); far below LLM-SR and SR-Scientist | c08, a15 (K13) | [C] against its Feynman score |
| NewtonBench model ranking | 324 tasks, 12 physics domains, 11 LLMs. Symbolic accuracy overall: GPT-5 75.9, Gemini-2.5-pro 65.4, GPT-5-mini 53.1, o4-mini 47.8, DeepSeek-R1 43.4; GPT-4.1, GPT-4.1-mini, DeepSeek-V3 5.1 to 8.9. GPT-5 uses about 19.15k tokens per task, weak models 2 to 3k. 4 runs per cell | b16, c19 (K14) | [S] |
| NewtonBench hardest setting | complex system with hard shift: GPT-5 40.3, Gemini-2.5-pro 16.7, others under 6 | b17, c19 (K10) | [S] |
| Noise sensitivity | Noise 0.0001 cut GPT-5-mini by 12 to 16 percent versus noise-free (absolute or relative not stated); falls steadily to 0.1. Run on GPT-5-mini only | b17, c20 (K10) | [E] with other sources (AI Feynman, SRBench) |
| Code interpreter helps weak, hurts strong | GPT-4.1 5.8 to 18.9; GPT-4.1-mini 5.1 to 14.7; DeepSeek-V3 8.9 to 13.3; GPT-5-mini 53.1 to 48.1; Gemini-2.5-flash 50.6 to 40.9; o4-mini 47.8 to 45.1; Gemini-2.5-pro 65.4 to 63.7; GPT-5 75.9 to 73.3. Harm appears when code budget goes from 0 to 1 | b18, c20, d14 (K09) | [S]; cause inferred from phrase counts in two traces |
| Whole-loop discovery by agents | DiscoveryWorld (24 main tasks of 120, 5 seeds): ReAct completion 0.38 / 0.18 / 0.18 (easy / normal / challenge), knowledge 0.25 / 0.14 / 0.10; Plan+Execute 0.18 / 0.18 / 0.15; Hypothesizer completion 0.28 / 0.23 / 0.08, knowledge 0.34 / 0.19 / 0.08. 10 human scientists, 1 hour: completion 0.66, knowledge 0.55; 11 of 16 tasks above 60% | b14, b15, c23 (K15) | [E] (3 sources) |
| DiscoveryBench | 264 real tasks, 6 domains, 903 synthetic; best agent 25%. Biology 0, engineering 7, economics 25, sociology 23. Domain hints raised the score (archaeology 9.9 vs 17.5 with hints) | b25, c24 (K15) | [E] |
| FIRE-Bench (ML finding rediscovery) | 30 core + 10 cross-domain tasks. F1: Claude Code (Sonnet-4) 46.7 (sd 23.4, across tasks), Codex (gpt-5 medium) 41.9, OpenHands gpt-5 37.9, o4-mini 31.9. Cross-domain: all under 25. Median CV 0.37 (Claude Code), over 0.6 (OpenHands). Judge precision 0.95, recall 0.86, F1 0.89 | c25, d16 (K15, K17) | [E] |
| FIRE-Bench failure sites | Planning and conclusions, not code. Contradictory plus unrelated claims 76.4 to 95.0% of false positives; alternatives 4.5 to 10.9%. o4-mini to gpt-5 backbone swap: 31.9 to 37.9 (+6.1). Weakest: controls. Stage shares seen only in a chart | c26, d16 (K16) | [S] |
| Cutoff test | Pre vs post cutoff F1, gpt-5: easy 62.3 vs 61.6 (n=6 vs 1); medium 44.5 vs 23.1 (7 vs 6); hard 22.6 vs 31.0 (5 vs 5); o4-mini hard 15.4 to 24.8. Cells hold 1 to 8 tasks | c27, d16 (K24) | [C] too coarse to rank recall controls |
| Renaming as a recall control | Library-reachability study: names and domain (L1) vs anonymous (L2): Acc0.01 49.81 vs 41.09; strict ID+OOD 13.76 vs 6.59; symbolic 8.14 vs 2.71. Anecdote: GPT-5 did not produce the d^3/(m1+m2) form once variables were renamed | d09, c29 (K12, K24) | [S] / [C] |
| Names and context carry signal | PhysGym: top models 66% to 31% as priors fall; o4-mini 62.89 to 41.24 when context removed. LaSR: removing variable names slowed search most. LLM-SR: removing the prior hurt a lot. Effect is not monotone per problem | b13, b21, a13, c14 (K12) | [E] (4 sources) |
| A no-LLM bank beats LLM systems | 129 LSR-Synth tasks, 4 seeds, same fitter and budget: BANK-LaSR Acc0.01 77.71, Acc0.001 62.60, strict ID+OOD 39.53, symbolic 19.77. LLM alone 49.81 / 30.81 / 13.76 / 8.14. Union 77.33 to 77.71 (no gain). Poly-only bank 27.52; union with poly bank 58.14. Earlier reports: SR-Scientist 63.57, LLM-SR 41.08, PySR 29.46, LaSR 16.02. Of 257 L1 LLM successes, 254 also solved by the bank | d08, d09 (K29) | [S] 2026 preprint |
| Division of labour | LLM-PySR, GPT-5.1, 74 AI-Feynman equations: controller 0.958 ACC0.1 at 91k tokens; decider 0.952 at 103k; plain PySR 0.922; equation author 0.892 at 450k; LLM-SR 0.892 at 2.21M; DrSR 0.665 at 2.84M. Controller +3.6 points over PySR with SD 0.165 | d10, d11 (K31) | [S] |
| Selection is the weak step | Best candidate beats submitted law by 0.14 (GPT-5.4-mini) vs 0.03 to 0.04 (GPT-6, Opus 5.5). Best-of-N, N=5 to 20: oracle gains 4.5 (SN) and 5.3 (SV) points; self-selection under 2. 60% of selected winners Pareto-dominated in a pool of five | d06 (K30) | [S] |
| Current-model law discovery | SciLaws-Bench: 118 problems from 381 papers, 14 models, ReAct, 30 turns. Fit SN (50 = published baseline): GPT-6 51.33, GPT-5.5 50.11, Opus 5.5 48.87, GPT-4o-mini 20.59. Validity SV: GPT-6 82.91, GPT-4o-mini 56.02. Parallel structure SS: GPT-6 72.46, Opus 5.5 58.69, GPT-5.5 58.26, GPT-4o-mini 33.47 | d04 | [S] |
| Recall predicts the old form, not the new | Universal recall on 9.3% of tasks; 39.0% recalled by no model. Published-form recovery 92% (Canon, 11 tasks) to 61% (Moat, 46 tasks). Full-law recovery flat at 12 to 13%. GPT-6 full-law 42% overall, 39% on Moat; GPT-4o-mini 0%. Beer-Lambert: all 14 got the published form, none the hidden law | d05 (K32) | [S] |
| Structure probes before generation | KeplerAgent (GPT-4o-mini), 10 ODE systems, 20 equations, symbolic accuracy clean/noisy: 75/45 vs LLM-SR 40/15 vs PySR 30/10; tokens 23k to 30k vs 182k to 184k. Algebraic: 42.34% with 3 attempts | d12, c21, c22 (K19) | [E] direction, weak backbone |
| Probe fails off physics structure | LSR-Transform: PySR 37.84, LLM-SR 31.53, KeplerAgent one run 35.14, best of 3 42.34 (best-of-3 chosen on test NMSE). AI Feynman on non-physical functions 66.7 vs 48.9 | d13, a10 (K19) | [E] on limit |
| Per-term held-out credit | IGSR, 128 problems, 300k tokens, 5 seeds, GPT-4o-mini. Average rank ID NMSE: IGSR 1.35, IGSR-Agent 2.41, LLM-SR 3.71, ICL 3.91, ICSR 4.21, LaSR 5.53. Symbolic ranks close (1.17 vs 1.29 to 1.35) | d15 | [S] |
| Constraints in prompt | More meaningful equations from GPT-4o; did not beat PySR or BMS on complex targets | c12 (K18) | [S] |
| Tie-breaking by derivation or description length | AI Descartes reasoning-error ranking; AI Feynman 2.0 Pareto frontier | b23, a11, c29 (K18) | [E] (3 sources) |
| Retrieve then compose then rank (chemistry) | 51 papers after Jan 2024; inspiration hit ratio at top 4%: GPT-4o 83.7, Llama-70B 83.0, Llama-405B 78.7, Llama-8B 43.5; top 20%: 96.7, 95.1, 95.7, 71.6. Matched score: Top MS 4.020 vs MOOSE 2.882, SciMON 2.549; without multi-step 3.765; without multi-step and ranking 2.863. Self-ranking rank ratio 0.411 to 0.521 | a22, b26, c28 (K23) | [S] |
| LLM-Feynman | Noise 1e-3: 100% vs AI Feynman 85%; noise 1e-2: 86% vs 67%; 20 complex formulas at 1e-2: 90% vs 55% | c13, c14 | [S]; likely partly recall |
| Agents repeat failures | KeplerAgent appendix: stuck at 15.6% MAPE on noisy data | c22 (K25) | [S] anecdote |
| BoxingGym | Ten environments for experiment design and model revision; no tested LLM does well; 32B beat 7B | b27 | [S] abstract only |

## 4. Mechanisms and models

Each mechanism below is written so it can be built. Where a number matters, it is the one from the evidence.

### 4.1 The BACON loop (constancy and term construction)

Inputs: a table of rows (variables, one dependent), a tolerance `tol` for "constant".

1. For the dependent variable `y` and each independent variable `x`, hold the others fixed and read the series.
2. If `y` is constant within `tol`, record the law "y = c" at this level. Stop for this level.
3. If `y` rises steadily with `x`, define `y/x`. If `y` falls as `x` rises, define `y*x`. If the trend is linear, define the slope as a new datum.
4. Add the new term as a column. Treat it as an observed variable. Repeat from step 1.
5. Before step 3 adds a term, check by code that it is not equal (within `tol`) to an existing term. BACON.3 needed this: Ohm's law produced 84 redundant terms.
6. For a second independent variable, run the loop in each context of the first. Then treat the fitted slopes and intercepts as new data at the next level (levels of description, a02).

Properties. Works on products and ratios. Cannot form sums or differences easily. Needs clean data. The final law did not depend on data order, but cost did.

### 4.2 The LLM-SR generate-fit-score-feedback loop

1. Prompt the model with the problem text, variable names, and 2 best past programs from a buffer (k=2 in-context examples, temperature 0.8).
2. The model writes 4 equation skeletons per prompt as Python functions with free parameters.
3. Code fits the parameters (BFGS in numpy, or Adam in torch). Numpy plus BFGS was slightly better.
4. Code scores in-domain and out-of-domain error (NMSE) and stores the program and score in an island buffer.
5. Repeat for about 2.5K iterations.

What each part gave (GPT-3.5, one problem): no refinement raised OOD NMSE to 1.81e-1; letting the model write constants raised it to 3.75e-1. The model proposes structure. Code fits numbers.

### 4.3 The SR-Scientist agent loop

The model is an agent with two tools: a data analyser (run code on the dataset) and an equation evaluator (fit and score a candidate). It runs up to 25 turns per iteration, about 1000 calls in all, and keeps an experience buffer of top equations. The next prompt samples from the top-k of the buffer. Ablations by backbone are in section 3. Implementation note: store the equation, the fitted constants and the score. Sample from the best entries. Random sampling from the buffer ("no top-k") hurt Qwen most (26.36 vs 49.09 Acc0.01).

### 4.4 Structure probes before fitting (AI Feynman, KeplerAgent)

Run cheap tests in code that reveal structure, then split the problem.

- Dimensional analysis: reduce variables to dimensionless groups.
- Polynomial fit: try low-degree exact fits first.
- Symmetry: test whether `f(x,y) = f(x+a, y+a)` or `f(ax, ay) = f(x,y)` holds on the data. A hit lets you drop a variable.
- Separability: test additive `f = g(x) + h(y)` or multiplicative `f = g(x) h(y)` by checking cross-differences or ratios. A hit splits one search into two smaller ones.
- Apply recursively to the sub-problems.

Keep a Pareto frontier of (error, description length) so noise does not hide a simpler form (AI Feynman 2.0, a11). In KeplerAgent the probe output (symmetry found, plot read) sets up the PySR or PySINDy configuration. On clean ODE systems this took symbolic accuracy from 30 (PySR) to 75. On transformed algebraic targets it gave little.

### 4.5 Library bank with a fitter (no-LLM control)

Build a fixed list of generic terms (powers, exp, log, trig, simple products). Run a sparse fit on the bank. This semantics-blind arm solved 77.71% of 129 LSR-Synth tasks at Acc0.01 with a fixed 800-point fitter. An LLM can propose extra terms (14 per call, code forms the products). Use this as the control arm in any equation test.

### 4.6 Role split with numeric gates (LLM-PySR)

The model sets the search (variables, operators, depth). PySR enumerates. Numeric gates decide which candidates survive. Five role splits were compared with GPT-5.1. The controller split gave 0.958 ACC0.1 at 91k tokens. Letting the model write equations or judge candidates cost 4 to 25 times more tokens and did no better. Model-written equations collapsed on atypical formulas (bactgrow, stressstrain). Model-judged retention failed on a near-tie.

### 4.7 Held-out credit assignment (IGSR)

Score each term of a candidate by how much it lowers held-out error when added. Prune weak terms in a tree search. Feed per-term numbers back. At 300k tokens this beat LLM-SR and LaSR on ID NMSE rank (1.35 vs 3.71 and 5.53). Symbolic ranks were nearly equal.

### 4.8 Retrieve, compose, rank (MOOSE-Chem)

1. Screen a corpus (300 papers) for inspirations relevant to the background. Keep top 4%.
2. Compose a hypothesis from background plus one inspiration, in several rounds.
3. Rank hypotheses. The model's own ranking tracks match weakly (rank ratio 0.411 to 0.521). Use a code-run test where one exists.

### 4.9 Dual-space search (Klahr and Dunbar)

State: a hypothesis space and an experiment space, linked. A move in one produces material for the other.

- Hypothesis space: generate frames from memory (here, "N means the number of repeats").
- Experiment space: run a test. If the outcome falls outside the current frame, build a new frame from the result.
- 13 of 20 people could not generate the right frame by memory search. They found it by running experiments in a region that showed the last N steps repeating.
- Behaviour to model: people kept a disconfirmed hypothesis 56% of the time and dropped a confirmed one 25% of the time.

To use this on an LLM trace: label each step as hypothesis-space or experiment-space. Mark which step produced the escape from a wrong frame. Count experiments with no stated hypothesis (humans: 28% overall; 6.08 per Experimenter against 0.76 per Theorist).

### 4.10 Concept-driven law finding (AI-Newton)

Maintain a store of concepts (mass, then force) and general laws. Propose concepts simple first. Test laws across many experiments. Reuse a concept in new experiments. Needs a plausible-reasoning framework supplied by the designers. Cost: up to 1200 trials, about 48 hours.

## 5. What holds up

### 5.1 Replications and independent tests

- **Memorisation of famous laws** [E]. Four lines agree. LLM-SR (under 20 iterations, perplexity), LLM-SRBench (early sharp drop, gap holds at equal size), SR-Scientist (nearly 50% near-solved after one try), Sharlin and Josephson (Kepler, Hubble, Bode leaked). SciLaws-Bench adds that only 9.3% of tasks were recalled by every model and 39.0% by none.
- **The loop beats one-shot prompting** [E]. 2.1 to 7.2% symbolic for direct prompting vs 11 to 32% for the same backbones in LLM-SR.
- **Fit is not the law** [E]. Acc0.1 88.28% with symbolic 20.24%. Fit and validity agree on only 53.6% of pairs. OOD accuracy tracks symbolic accuracy.
- **Noise breaks symbolic recovery** [E]. AI Feynman v1 in SRBench, NewtonBench (0.0001 noise), AI Feynman v2 (relative gain).
- **Backbone-dependent ablations** [E]. SR-Scientist: the analyser mattered most for GPT-OSS-120B, top-k for Qwen, the buffer for GLM.
- **Names and context carry signal** [E]. Four sources. But context can also mislead (PhysGym non-monotone).
- **Agents are far below humans on whole loops** [E]. DiscoveryWorld, DiscoveryBench, FIRE-Bench.

### 5.2 Failures to replicate or shrinking headlines

- **AI Feynman.** 100 of 100 (authors) became 53% exact noise-free in SRBench, and it fell behind other methods above noise 0.01. The paper also gives two baselines (71 vs 68). Authors' headlines shrink under third-party tests.
- **LaSR.** 72 of 100 Feynman in its paper, with an inconsistent intro (66). With PySR given 10 hours per equation the fair gain is about +10, not +13. On a recall-controlled benchmark LaSR scored 5.41 to 12.61% symbolic on LSR-Transform, and the reachability study lists it at 16.02 on LSR-Synth. Either part of its gain is recall, or the benchmark runs used weaker settings. Unresolved [C].
- **LLM-system headlines against a no-LLM bank.** A semantics-blind bank scored 77.71 where the best LLM report was 63.57. Union with the LLM added nothing at full library. So "LLM beats search" needs a bank arm.
- **LLM-PySR vs PySR.** The gain is +3.6 points ACC0.1 with SD 0.165, small against its spread. The big gains are against LLM-SR and DrSR on tokens.
- **KeplerAgent on LSR-Transform.** One run (35.14) lost to PySR (37.84). Only best-of-3 (42.34) won, and that was chosen on test NMSE.
- **Contamination signals disagree** [C]. Renaming stopped GPT-5 recalling Kepler's law (anecdote, two prompts). FIRE-Bench found no clear cutoff effect (cells of 1 to 8 tasks). SciLaws-Bench found recall predicts published-form recovery (92 vs 61%) but not new-structure recovery (12 to 13% in every tier). The controls measure different things.
- **The founding work.** Data were cleaned, one run per law, tasks author-chosen. The 4 of 14 human figure for Kepler is unverified.

### 5.3 Moderators

- **Backbone strength.** Reasoning models dominate (NewtonBench 75.9 vs 5.1 to 8.9). GPT-6 over GPT-5.5 gained 14 points of structure score. A backbone change can swamp a scaffold effect.
- **Code access.** Helps models under about 40% accuracy, hurts those at 40% or more by 1.7 to 9.7 points.
- **Structure available.** Probes win when the target has symmetry or separability (physics, ODEs). They help less on arbitrary or transformed targets.
- **Noise.** All methods degrade. Smaller noise than 0.001 already matters.
- **System complexity.** Hardest NewtonBench setting left only two models above 6%.
- **Domain.** DiscoveryBench biology 0%, engineering 7%, economics 25%.
- **Prior knowledge.** Domain hints lift scores (DiscoveryBench archaeology 9.9 vs 17.5).

### 5.4 Interventions that worked

- Real fit-and-score feedback in a loop (K05).
- Code fits the numbers; the model writes structure (K06).
- Data inspection by code before proposing; a buffer of top attempts (K08).
- Structure probes before generation, for physics-like targets (K19).
- Derivation or complexity tie-breaks computed in code (K18).
- Role splits that keep retention in code (K31, single source).
- Listing hypotheses before experimenting, for humans: N=10, all solved in 6.2 min (K28).
- Per-term held-out feedback for a weak backbone (d15, single source).

### 5.5 Interventions that did not work, or did not help

- Data-blind one-shot prompting (2.1 to 7.2%).
- Letting the model write constants (OOD NMSE 3.75e-1).
- Code access for strong models (-1.7 to -9.7 points).
- Model self-ranking of hypotheses (rank ratio 0.411 to 0.521).
- Model self-selection among finished candidates (under 2 of 4.5 to 5.3 oracle points).
- Model-judged retention on near-ties (LLM-PySR decider on oscillator2).
- Constraints written in the prompt on complex targets (did not beat PySR or BMS).
- Adding LLM terms to a full library (77.3 to 77.7).
- DrSR's reflection layer inside the LLM-PySR comparison (0.665 ACC0.1 at 2.84M tokens). Its own paper claims gains over LLM-SR; the independent test did not show them.
- Hypothesizer scaffold on hard DiscoveryWorld tasks (completion 0.08).

## 6. Language models

### 6.1 How models behave

1. **They recall.** On famous laws the fit comes in under 20 iterations. On a transformed problem the gap persists at equal expression size. Treat an early exact fit as an alarm.
2. **They fit well and name the form poorly.** Material science: Acc0.1 88.28, symbolic 20.24.
3. **They stop early with tools.** Strong models settled sooner when code was available (inferred from phrase counts in two traces).
4. **They choose poorly among their own candidates.** The best candidate beat the submitted law by 0.14 for a weak model and 0.03 to 0.04 for the best.
5. **They fail at controls and conclusions.** FIRE-Bench: 76.4 to 95.0% of false claims were contradictory or unrelated. Controls were the weakest part.
6. **They need names.** Hiding names costs 8 to 9 Acc0.01 points (49.81 to 41.09) in one study and was the biggest slowdown in LaSR.
7. **They generate fewer ideas than a bank can.** The no-LLM bank covered more tasks than the LLM did (254 of 257 LLM successes were also bank successes).

### 6.2 Benchmarks, in time order

| Benchmark | What it tests | Best result | Note |
|---|---|---|---|
| LLM-SRBench (2025) | Equation discovery with recall reduced | 31.53% symbolic (Transform); 9.91 to 28.12% per synthetic domain | Weak backbones (GPT-3.5, Llama-8B, GPT-4o-mini); LLM judge |
| DiscoveryWorld (2024) | Whole-loop discovery in invented worlds | completion 0.38 easy, 0.08 to 0.23 harder; humans 0.66 | 2024 models |
| DiscoveryBench (2024) | Data-driven hypotheses from real papers | 25% | LLM-scored facets |
| NewtonBench (2025/26) | Shifted laws in interactive systems | GPT-5 75.9%; hardest 40.3% | LLM judge, 98.3% agreement with humans |
| SR-Scientist (2026) | Agent loop on LSR-Synth | Acc0.01 63.57 | Authors' system |
| FIRE-Bench (2026) | Rediscovery of ML findings | F1 46.7 | Cells of 1 to 8 tasks |
| SciLaws-Bench (2026) | Real and invented-variant laws, 14 models | Fit SN up to 51.33; structure SS up to 72.46 | Preprint, LLM judges |

### 6.3 What changed the numbers, and by how much

- **Adding a data-fed loop to the same backbone:** from 2.1 to 7.2% up to about 11 to 32% symbolic (K05).
- **Removing the data-analysis tool:** -27.9 Acc0.01 points for GPT-OSS-120B; -8.0 for Qwen; -1.8 for GLM (63.57 to 35.66; 49.09 to 41.08; 48.32 to 46.51).
- **Removing the buffer:** -6.2 (GPT-OSS), -13.4 (Qwen), -11.1 (GLM).
- **Random buffer sampling instead of top-k:** -5.4 (GPT-OSS), -22.7 (Qwen), -6.4 (GLM).
- **Code interpreter:** +13.1 (GPT-4.1), +9.6 (GPT-4.1-mini), +4.4 (DeepSeek-V3); -5.0 (GPT-5-mini), -9.7 (Gemini-2.5-flash), -2.7 (o4-mini), -1.7 (Gemini-2.5-pro), -2.6 (GPT-5).
- **Reasoning model vs non-reasoning model:** 75.9 vs 5.1 to 8.9 (NewtonBench).
- **Backbone swap in FIRE-Bench:** o4-mini to gpt-5 in OpenHands, +6.1 F1.
- **Structure probe on ODEs:** 30 to 75 clean, 10 to 45 noisy (weak backbone).
- **Role split:** ACC0.1 0.958 at 91k tokens vs 0.892 at 2.21M.
- **Names hidden:** Acc0.01 -8.7, strict -7.2, symbolic -5.4 (L1 to L2).
- **Priors removed (PhysGym):** top models 66% to 31%.
- **Domain hints (DiscoveryBench):** 9.9% to 17.5% in one archaeology case.
- **Newest-model gains (SciLaws-Bench):** GPT-6 over GPT-5.5, +14.2 structure score; full-law recovery 42% overall for GPT-6, 0% for GPT-4o-mini.

### 6.4 What the language-model literature does not give us

- No study has a scaffold arm against a strong reasoning model with code at equal tokens on changed-law or invented-law tasks (gap 1 of the critique). SciLaws-Bench has 14 models in one harness and no scaffold arm. LLM-PySR's plain arm is LLM-SR, not a reasoning model with code.
- No study tested a held-out check or a minimum-hypotheses rule against code access (gap 3).
- No LLM study was found that codes traces as hypothesis-space or experiment-space search, feeds a case series in historical order, or compares scope-split revision with overwrite (K33). The search was cut short by rate limits.

## 7. What our agent should take

Schema part: G guardrail, S state, O operator, memory. Evidence ids are in brackets. Status as in the claim file.

### Add now (established)

1. **Never use named classic laws as a test of the schema.** Use changed-law, invented-law or renamed versions, and treat an exact fit in the first few iterations as a recall alarm. Part: G3, G7, G8 (test hygiene). [E] K03. Evidence: b07, c05, b02, c08, a15, b20, c16, c11.
2. **A fit is not a pass; require a point outside the fitted range.** Accept a rule only if it passes extrapolation points the fit never saw. Part: G3, S8. [E] K04. Evidence: a16, c08, c09, b03, b04. (Already matches G3; this adds the extrapolation form and the evidence that symbolic accuracy tracks OOD accuracy.)
3. **Generate, test with real code output, revise.** Real scores fed back beat one-shot prompting at the same backbone. Part: G2, S3-S5. [E] K05. Evidence: a15, b04, b06, c06, c16, b24. (Already in the schema; this is more support.)
4. **The model writes structure; code fits numbers.** Never let the model write fitted constants. Part: G5, S4. [E] K06. Evidence: a13, b06, c04, b24, a20, b05.
5. **Let the agent inspect the data with code before proposing, and keep a buffer of top past attempts sampled by rank.** The weight of each differs by backbone, so ablate per backbone. Part: S1, S2, memory. [E] K08. Evidence: a18, a19, b19, c17, a21, c10, c21.
6. **Add a small-noise rerun of the final answer; reject an answer that flips.** Part: G3, S8. [E] K10. Evidence: b17, c20, c19, a11, b09, b10, c18, c13.
7. **Break ties among equally fitting candidates with a code-computed derivation, constraint or description-length score, not a model opinion.** Part: G3, G5, S7, S8. [E] K18. Evidence: b23, c29, a11, b09, c12, a23, d06, d07.
8. **Use a structure probe in code (units, symmetry, separability) before generating, on tasks with physics-like structure.** Part: S2, O3, O6. [E] K19. Evidence: a09, a10, a06, c21, c22, b08, d12, d13. Do not expect it on arbitrary or transformed targets.
9. **Run at least 3 to 5 seeds per arm and report intervals.** Part: G7. [E] K17. Evidence: c25, a18, b16.
10. **Include the strongest reasoning-model baseline at equal tokens before any claim of scaffold gain, and a no-LLM or plain-search arm where one exists.** Part: G7, G11. [S] K14 and K29 but low-cost; adopted as test hygiene. Evidence: b16, c19, d08, d09.
11. **Keep meaningful names and domain context in the task text, and run a names-stripped version as a recall control.** Part: S1, S2, memory (background priors). [E] K12. Evidence: a13, b13, c15, b21, c14, c24.
12. **Score the whole loop on invented worlds (DiscoveryWorld style), since they remove memory.** Part: S6 control, G12. [E] K15. Evidence: b14, b15, c23, b25, c24, c25.

### Test first (single-source, contested, or untested)

1. **Held-out candidate check before submit.** Code scores every candidate on held-out points and submits the best; compare with self-selection. Part: G3, S7, S8. [S] K30. Evidence: d06, d07, d15.
2. **Minimum-hypotheses rule before first code fit.** List at least k distinct rival laws before using tools; test whether it removes the harm of code access for strong models. Part: G1, G12, S3. [S] K09. Evidence: b18, c20, d14. The cause is inferred from two traces.
3. **Code claim-versus-output check.** Each stated conclusion must appear in executed output. Part: G2, G10, S8. [S] K16. Evidence: c26, b25, d16.
4. **Model proposes structure, code enumerates and keeps (controller split).** Part: G5, S3, S4. [S] K31. Evidence: d10, d11, d15.
5. **Code-gated lesson store.** Keep a few lessons or concepts from past successes and failed attempts (with the failing output) and show them after the first attempt. Part: memory. [C] K13, [S] K25. Evidence: a17, b12, c15, a15, c22, a21.
6. **Scope-tagged revision.** When a rule fails on a subset, split by condition instead of overwriting. Part: S5, S9, O4. [E] for the need in the symbolic literature (K22), untested in LLMs (K33). Evidence: a05, a01.
7. **Dual-space trace coding and forced switch after a disconfirming result.** Part: S6, G1, operators. [S] K28. Evidence: d01-d03.
8. **List hypotheses first, then run discriminating tests.** Part: S2, S7. [S] K28. Evidence: d03.
9. **Retrieve-then-combine for open hypothesis generation, with code-run evaluation.** Part: O7, S3, G8. [S] K23. Evidence: a22, b26, c28.
10. **Staged order of sub-problems; shuffled vs staged check.** Part: S3, memory. [E] on cost in symbolic systems (K20); untested in LLMs. Evidence: a04, a03, b22, c30.
11. **Duplicate and equivalence filter on candidates.** Part: G5, S4. [S] K21. Evidence: a03.
12. **Historical-order case series with wrong turns marked.** Part: test design (G7). [S] K02, K33. Evidence: a07, a08.

## 8. Concrete tests on our bench

Rule for all: both arms at equal total tokens, at least 5 seeds, report intervals, strongest reasoning backbone we run, plain model as the baseline arm.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Synthetic law-finding tasks we generate: invented formulas (products, ratios, sums, a power with a new exponent), variables renamed, 20 to 60 data rows, hidden extrapolation points | Plain reasoning model with code vs generate-fit-score-revise with a buffer | Held-out and extrapolation pass rate; symbolic match by code equivalence (not an LLM judge) | Loop gains on weak backbone (K05); on a strong backbone, gain near zero or small. This is the missing arm (gap 1) |
| T2 | Same items as T1 | Submit by self-selection vs code scores all candidates on held-out points and submits the best | Held-out accuracy of the submitted law; gap between best evaluated and submitted | Closes part of the 0.03 to 0.14 gap; weaker models gain more (K30) |
| T3 | Same items; strong backbone with code | Code access with no rule vs code access plus "list k rival laws first" (k=3) | Pass rate; number of distinct laws proposed before the first fit; exploration rate | Rule removes the 1.7 to 9.7 point harm (K09). If it does nothing, the cause is not early settling |
| T4 | Items with exact formula plus small noise (0.0001, 0.001, 0.01) | Answer accepted as is vs answer rerun on noisy copy and rejected if it flips | False-accept rate; pass rate on the noise-free hidden set | Fewer wrong acceptances at small cost in tokens (K10) |
| T5 | Items with product/ratio structure vs arbitrary compositions | Probe step (units, symmetry, separability tests in code) vs none | Pass rate by item class; tokens per solve | Gain on structured items, none on arbitrary ones (K19) |
| T6 | Items with names kept, names stripped, and law altered | Same scaffold on all three versions | Pass rate across versions; published-form recovery vs new-structure recovery scored separately | A graded drop with renaming; new-structure rate flat across recall tiers (K24, K32). Tells us which control to use |
| T7 | Items with a conditional law (rule A in region 1, rule B in region 2) | Overwrite revision vs scope-split revision | Pass rate on both regions; share of correct scope boundaries | Scope-split keeps old region correct; overwrite loses it (K22). New test, no LLM evidence |
| T8 | A hidden-rule device task à la Klahr and Dunbar (a toy program with an unexplained command, rule not "N repeats" at first) | Plain agent vs forced switch (after a disconfirming result, state a new frame) vs list-hypotheses-first | Solve rate; experiments to solution; share of experiments with no stated hypothesis (human 28%); disconfirmed-hypothesis retention (human 56%) | Retention drops under forced switch; list-first shortens search (K28) |
| T9 | Multi-step tasks with sub-problems of increasing difficulty | Shuffled vs staged order | Same-answer rate; tokens | Same final answer; staged cheaper (K20) |
| T10 | Open hypothesis tasks with a code-run evaluator (e.g. a program whose output we can compare to a hidden rule) | Free generation vs retrieve-then-combine | Hit rate of the right ingredient; evaluator pass rate | Retrieve step lifts hit rate (K23) |
| T11 | Any equation item set | Add a no-LLM term bank at the same fit budget as a control arm | Paired gain of scaffold over bank | Bank is a hard bar (K29). If scaffold does not beat it, report that |
| T12 | Brainteaser-style items with a checkable answer | Claim-versus-output check vs none | Share of contradicted claims in final answers | Drop in contradicted claims (K16) |

Cheapness. T1 to T4 and T11 reuse one generated item set. T5 to T7 need new generators. T8 needs a small simulator. T10 needs an evaluator.

## 9. What does not transfer, and why

- **Equation discovery is not general reasoning.** The tasks have a numeric check, a smooth loss, and a fixed grammar. Many of our items have none of those. Findings about fitting (BFGS beats Adam, bank beats LLM terms) say little about word problems.
- **Historical reconstruction proves sufficiency, not path.** BACON on clean data shows a method is enough. It does not show a model reasoning this way is correct, nor that scientists did (a08, b30).
- **Famous-law results are recall.** Feynman, Kepler, Hubble, Bode, Langmuir are in training text. Anything on them is contaminated (K03).
- **Author-reported headlines.** AI Feynman 100 became 53; LaSR 72 is contested; SR-Scientist and LLM-SR numbers are on the authors' benchmarks.
- **Weak-backbone results.** LLM-SR, LaSR, KeplerAgent, IGSR used GPT-3.5, Llama-8B, GPT-4o-mini or Mixtral. A step that lifted such a model may do nothing for a 2026 reasoning model. NewtonBench shows tools already hurt at 40% accuracy and above.
- **Compute scale.** AI-Newton ran up to 1200 trials and 48 hours. SR-Scientist ran about 1000 calls per problem. LLM-SR ran 10,000 API calls on one NewtonBench domain. Our token budget (G11, G12) does not allow that.
- **Structure probes on physics.** Symmetry and separability need physics-like structure. Our puzzles may not have it (66.7 vs 48.9 on non-physical functions; KeplerAgent on LSR-Transform).
- **Human data is thin.** One toy device, student sample (N=20, N=10), groups formed after the fact, strategy confounded with programming experience (7 of 7 vs 1 of 13). Do not read dual-space as a law about LLMs.
- **ML-paper rediscovery (FIRE-Bench) is not natural law discovery.** Its findings are empirical ML claims, and its cutoff cells are tiny.
- **Judge-scored metrics.** LLM judges score symbolic accuracy in LLM-SRBench, NewtonBench, SciLaws-Bench, DiscoveryBench, MOOSE-Chem. Our G5 wants code equivalence.
- **Multi-agent discovery systems.** Not in this evidence; G9 stays.
- **What the schema bans.** Section 4b bans unstructured self-reflection and verbal-confidence stopping. Nothing here contradicts it. The "oracle reflect" variant in DiscoveryBench used the true match score, which is a ceiling, not something we can deploy (c24).

## 10. Open questions

1. Does a generate-fit-score-revise scaffold beat a plain strong reasoning model with code at equal tokens on changed-law and invented-law tasks? Every positive result so far used weak backbones or the authors' benchmark.
2. Which loop part pays for which current backbone? SR-Scientist ablations are on GPT-OSS, Qwen and GLM.
3. Why do strong models do worse with code? Is it early settling, and does a minimum-hypotheses rule or held-out check fix it?
4. What does an independent replication of AI Feynman, LaSR and LLM-SR show on one shared, recall-controlled set, with repeated seeds and code-based symbolic equivalence?
5. Can a units or separability probe lift an LLM agent the way symmetry lifted KeplerAgent on ODEs, and where does it fail?
6. What are the human bars? Qin and Simon (1990) and Klahr and Simon (1999) were not read. The 4 of 14 figure is unverified.
7. Does historical-order feeding with wrong turns work as a test for an LLM scaffold? No LLM study found.
8. Does scope-tagged revision beat overwrite on conditional laws, and do LLMs learn conditional laws at all?
9. Is the gap between agents and humans mostly control design and conclusion drawing, and does a claim-versus-output check close it?
10. Which recall control best predicts out-of-distribution performance: renaming, altered law, recall-tier audit, or cutoff split? No study compared them on one task set.
11. Are the 2026 preprints (SciLaws-Bench, library reachability, LLM-PySR, IGSR) confirmed after peer review?
12. How much of the gap between LLM systems and the no-LLM bank holds on non-physics tasks where the bank has no reachable terms?
13. Does the BACON.3 redundancy check help LLM agents, or does the model already prune?

## 11. Sources

[V] opened and read this session; [M] snippet, abstract or search summary only. Evidence ids in brackets.

**Founding and symbolic work**
- [V] Langley (1977) BACON: a production system that discovers empirical laws. https://ijcai.org/proceedings/1977/0077.pdf [a01]
- [V] Langley (1979) Rediscovering physics with BACON.3. https://ijcai.org/proceedings/1979/0113.pdf [a02, a03, a04]
- [M] Langley (1979) abstract page. https://mlanthology.org/ijcai/1979/langley1979ijcai-rediscovering [b28]
- [V] Falkenhainer and Michalski (1986) ABACUS. https://link.springer.com/content/pdf/10.1007/BF00114868.pdf [a05, a06]
- [V] Zytkow and Simon (1986) A theory of historical discovery: componential models (STAHL). https://link.springer.com/content/pdf/10.1007/BF00116252.pdf [a07, a08]
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery. https://archive.org/details/scientificdiscov00insc [a25]
- [M] Schmidt and Lipson (2009) Distilling free-form natural laws from experimental data. https://doi.org/10.1126/science.1165893 [a28]
- [V] Kramer et al. (2023) Automated Scientific Discovery: from equation discovery to autonomous discovery systems. https://arxiv.org/abs/2305.02251 [c01, c02]
- [M] Heeffer (2021) Promises and disappointments of AI for scientific discovery. https://www.aup-online.com/content/journals/10.5117/ANTW2021.1.003.HEEF [b30]

**Human studies**
- [V] Klahr and Dunbar (1988) Dual space search during scientific reasoning. https://users.cs.northwestern.edu/~paritosh/papers/sketch-to-models/klahr-dunbar-dual-space-search-cogsci-1988.pdf [d01, d02, d03]. Published version: https://doi.org/10.1207/s15516709cog1201_1 [a26, M]
- [M] Qin and Simon (1990) Laboratory replication of scientific discovery processes. https://search.worldcat.org/oclc/832091458 [b29, d18]
- [M] Klahr and Simon (1999) Studies of scientific discovery. https://doi.org/10.1037/0033-2909.125.5.524 [a27, d18]

**Symbolic regression**
- [V] Udrescu and Tegmark (2020) AI Feynman. https://arxiv.org/abs/1905.11481 [a09, a10, b08]
- [V] Udrescu et al. (2020) AI Feynman 2.0. https://arxiv.org/abs/2006.10782 [a11, b09]
- [V] La Cava et al. (2021) SRBench. https://arxiv.org/abs/2107.14351 [b10, b11]. Only the abstract was read through the arXiv API; the cross-check could not download the PDF.
- [V] Cranmer et al. (2020) Discovering symbolic models from deep learning. https://arxiv.org/pdf/2006.11287 [a23]
- [V] Cranmer (2023) PySR. https://arxiv.org/pdf/2305.01582 [a24]
- [V] Cornelio et al. (2023) AI Descartes. https://arxiv.org/abs/2109.01634 [b23]
- [V] Fang, Jian, Li (2025) AI-Newton. https://arxiv.org/abs/2504.01538 [b22, c30]

**Language-model studies**
- [V] Shojaee et al. (2025) LLM-SR. https://arxiv.org/abs/2404.18400 [a12, a13, b05-b07, c03-c06]. The cross-checker could not download the PDF; three agents agree on the same ablation values.
- [V] Shojaee et al. (2025) LLM-SRBench. https://arxiv.org/abs/2504.10415 [a14-a16, b01-b04, c07-c09]
- [V] Grayeli et al. (2024) LaSR. https://arxiv.org/pdf/2409.09359 [a17, b12, b13, c15]
- [V] Xia, Sun, Liu (2026) SR-Scientist. https://arxiv.org/abs/2510.11661 [a18, a19, b19, b20, c16-c18]
- [V] Ma et al. (2024) LLM and simulation as bilevel optimizers (SGA). https://arxiv.org/pdf/2405.09783 [a20, b24]
- [V] Wang et al. (2025) DrSR. https://arxiv.org/pdf/2506.04282 [a21]
- [V] Sharlin and Josephson (2024/2026) In-context learning and reasoning for symbolic regression. https://arxiv.org/abs/2410.17448 [c10-c12]
- [V] Song et al. (2025) LLM-Feynman. https://arxiv.org/abs/2503.06512 [c13, c14]
- [V] Chen et al. (2025) PhysGym. https://arxiv.org/abs/2507.15550 [b21]
- [V] Zheng et al. (2026) NewtonBench. https://arxiv.org/abs/2510.07172 [b16-b18, c19, c20, d14]
- [V] Yang et al. (2026) KeplerAgent. https://arxiv.org/abs/2602.12259 [c21, c22, d12, d13]
- [V] Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769 [b14, b15, c23]
- [V] Majumder et al. (2024) DiscoveryBench. https://arxiv.org/abs/2407.01725 [b25, c24]
- [V] Wang et al. (2026) FIRE-Bench. https://arxiv.org/abs/2602.02905 [c25-c27, d16]
- [V] Yang et al. (2025) MOOSE-Chem. https://arxiv.org/abs/2410.07076 [a22, b26, c28]
- [V] Cornelio et al. (2025) The need for verification in AI-driven scientific discovery. https://arxiv.org/abs/2509.01398 [c29]
- [M] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 [b27]. Abstract only.
- [V] Huang et al. (2026) SciLaws-Bench. https://arxiv.org/abs/2609.01552 [d04-d07]
- [V] Yao et al. (2026) Library reachability in LSR-Synth. https://arxiv.org/abs/2607.28684 [d08, d09]
- [V] Xie et al. (2026) LLM-PySR. https://arxiv.org/abs/2607.04156 [d10, d11]
- [V] Saveliev et al. (2026) Influence-guided symbolic regression (IGSR). https://arxiv.org/abs/2605.29184 [d15]

**Search logs (not sources)**
- [M] d17: search log; no LLM study found for dual-space trace coding, historical-order feeding, or scope-tagged revision. Weak negative, rate-limited.
- [M] d18: failed access attempt for Qin and Simon (1990) and Klahr and Simon (1999).
