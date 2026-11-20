# Automated discovery: deep document

*Subfield E15.10. Machine scientists and LLM hypothesis search. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b26, c01-c26, d01-d16), claims.jsonl (K01-K23), critique.md in this folder. Written 2026-11-20. Schema parts refer to `research_notes/single_agent/SCHEMA.md` v0.2 (G1-G12, S0-S9, O1-O8, section 4b). Nothing here is added to the schema until it passes a test (see UNKNOWNS.md).*

*Honesty note. The founding-era work (BACON, Eureqa, Robot Scientist Adam) was NOT opened in this folder, so it has no verified numbers. Everything with a number below was read in arXiv full text or a PMC page unless marked [M]. Many "established" marks rest on papers from related groups, so independence is partial.*

## 1. What it is

Automated discovery is the use of programs to find new knowledge: equations, hypotheses, algorithms, mathematical constructions, drug candidates, or whole papers. It has three families.

1. **Symbolic machine scientists (before LLMs).** Search over formulas or rules, scored by fit to data. Examples: BACON (1980s), Eureqa (genetic programming, 2009), AI Feynman (2020), PySR (2023).
2. **Robot scientists.** A closed loop of hypothesis, automated experiment, update. Examples: Adam (yeast genes, 2009), Eve (drug screening, 2015), Genesis (systems biology, in progress).
3. **LLM-based discovery systems (2023-2026).** The LLM proposes; code or a judge scores. Four sub-types:
   - Program search with an exact scorer: FunSearch, AlphaEvolve, LLM-SR.
   - Idea and hypothesis generators with a judge: Si et al. ideation agent, Nova, AI co-scientist.
   - End-to-end paper pipelines: AI Scientist v1 and v2, Agent Laboratory, Jr. AI Scientist, Kosmos.
   - Benchmarks of data-driven discovery: DiscoveryBench, ScienceAgentBench, MLE-bench, PaperBench, LLM-SRBench.

**Why it matters for our agent.** Every discovery system is a generate-test-select loop: S3 generate, S4 test, S7 select. The literature is a large natural experiment on what makes that loop work. The central pattern across the sources below: **a loop works when there is a cheap, exact, held-out scorer in code, and fails when the selector is a model's opinion.** That is the line our guardrails G3, G5 and G8 already draw. The literature also shows where the schema is untested: no source compares a scaffold against plain sampling at equal tokens (gap 1, claim K22).

## 2. History and theories in depth

### 2.1 Heuristic search for laws (1970s to 1990s)

BACON and its successors (Langley, Simon, Bradshaw, Zytkow 1987; a19, c21 [M], not opened) rediscovered Kepler's third law and Ohm's law by heuristic search through combinations of terms in clean data. Critics said the designers supplied the variables and the representation. This is the oldest form of the claim that discovery is problem solving (Simon). Kepler's own case is quoted in the AI Feynman intro: about four years and 40 failed ovoid fits before the ellipse (a01). No success rates from this era are verified here.

### 2.2 Evolutionary symbolic regression (2009 to now)

Eureqa (Schmidt and Lipson 2009; a20 [M]) used genetic programming scored by fit and invariants. PySR (Cranmer 2023; a03) is the standard open version: multi-population evolution with islands, simulated annealing, constant optimisation, simplification, and a Pareto front of accuracy against complexity. It needs very many evaluations; the LLM-SR baselines ran 2M+ iterations (a04). SRBench (La Cava 2021; b13, d10) put 14 symbolic regression methods and 7 ML methods on 252 problems with 10 repeated trials. Operon (genetic programming with parameter fitting) had the best test R2 on real data. AI Feynman recovered 53% of ground-truth equations at zero noise, nearly twice the next (GP-GOMEA, 27%), but four other methods beat it above noise 0.01.

### 2.3 Physics-inspired decomposition (AI Feynman, 2020)

AI Feynman (a01, a02, c19) fits a neural network, then tests the learned function for symmetry, separability and compositionality, and splits the problem into smaller ones. It found all 100 Feynman Lectures equations where Eureqa found 71. On 20 harder bonus equations it went from 15% (Eureqa) to 90%. Version 2 added generalised symmetries from network gradients, normalising flows, and a Pareto frontier with pruning after each merge (a02). The key idea: discovery becomes tractable when structure lets you cut the search space. This maps onto our O3 (decompose) and O6 (change representation).

### 2.4 Robot scientists

Adam (King 2009; a21, c22, d16 [M]) closed a loop on yeast gene function. A secondary report says 12 of 20 hypotheses confirmed (not verified; do not cite without King 2009). Eve's active-learning screen (Williams 2015; d15, opened): about 14,400 compounds plus about 1,600 approved drugs, throughput over 10,000 compounds per day, three loops picking 96 compounds each after training on 4,800. TNP-470 inhibited P. vivax DHFR with IC50 0.16 uM against over 165 uM for the human enzyme (about 1000-fold selective). The 2024 Genesis review (d14) lists aims (1,000 bioreactors, 1,000 cycles per day) but reports 12 of 48 bioreactor units built, so these are aims, not results. Hit rates against random screening were not in the pages read. These systems are developer-reported and narrow, with human-built logic bases.

### 2.5 LLM program search (2023 to 2025)

- **FunSearch** (Romera-Paredes 2023; d01, d02, opened via PMC): an LLM (Codey, PaLM 2 family, no fine-tuning) writes functions; an automatic evaluator scores them; an island database keeps the best. Compute: about 10^6 samples, 15 samplers, 150 CPU evaluators.
- **LLM-SR** (Shojaee 2024; a04, c10): the LLM writes equation skeletons as Python programs; an optimiser fits the constants; an evolutionary buffer feeds the best programs back.
- **AlphaEvolve** (Novikov 2025; a16, b16, c12): evolves whole programs with a Gemini ensemble and automated evaluators.

### 2.6 LLM idea and hypothesis generation

- **Si, Yang, Hashimoto 2024** (a06, b01-b03, c04, c05): the first large blind human study of LLM research ideas.
- **Si, Hashimoto, Yang 2025** (a08, b04, c06, d07, d08): the execution follow-up.
- **Nova** (d11) and a 2026 five-architecture study (d12): iterative planning and retrieval for novelty.
- **AI co-scientist** (Gottweis 2025; a13, a14, b17, b23, c07, d13): generate, debate, rank by Elo, evolve.
- **Gupta and Pruthi 2025** (b09, b10, b24): idea-level plagiarism in LLM proposals.

### 2.7 End-to-end paper pipelines and agent benchmarks

AI Scientist v1 (Lu 2024; a09, a10, b07, c01), v2 (Yamada 2025; a12, b08, c03), its independent evaluation (Beel 2025; a11, b05, b06, c02), Agent Laboratory and AgentRxiv (Schmidgall 2025; c14, d05, d06), Jr. AI Scientist (c18), Kosmos (Mitchener 2025; b18, b19, c17), a position paper on implementation limits (Yang 2025; c15), and benchmarks DiscoveryBench (a18, c08), ScienceAgentBench (a17, c09), MLE-bench (b14, b21, c16), PaperBench (b15, b22, d09), LLM-SRBench (a05, b11, b12, c11).

### 2.8 Competing theories of why LLM discovery works or fails

- **Search-with-verifier view.** The LLM is a proposal distribution; the evaluator does the knowing. Wins appear where a cheap exact evaluator exists (AlphaEvolve, FunSearch, LLM-SR). Supported by the pattern of successes and failures (a23, c23).
- **Recitation view.** Strong results on famous equations are memorisation. Supported indirectly by LLM-SRBench (a25, b12): low error in under 20 iterations on Feynman forms, but 31.5% and 28.1% on transformed and synthetic forms. No clean contamination test exists.
- **Judging-is-easier-than-doing view.** Reviewers can be fooled before execution but not after it (a24). Supported by Si 2024 vs Si 2025.
- **Compute view.** Scaling test-time compute and attempts gives gains (c09, b14, a13), but with a plateau on long-horizon tasks (d09). Contested.

## 3. Core findings with exact numbers

Status key: E = established (two or more independent sources); S = single source; C = contested or mixed; W = weak. Ids point to the evidence files.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM ideas rated more novel than expert ideas before execution | Novelty 4.84 human, 5.64 AI, 5.81 AI+human rerank (1-10); 49 ideas per condition, 79 reviewers, 298 reviews, 7 NLP topics; AI vs human p<0.05 after correction; overall 4.69 human, 4.83 AI, 5.32 rerank (p=0.06); feasibility 6.53 vs 6.30 | Si 2024 (a06, b01, c04) | S (K01) |
| The novelty advantage vanishes after execution | 43 experts, about 103 h each; change after execution, human vs AI: novelty -0.010 vs -1.049; excitement +0.078 vs -1.760; effectiveness -0.052 vs -1.879; overall -0.628 vs -1.976; FDR p=0.025, 0.001, 0.003, 0.004; 19 human and 24 AI projects. Final novelty 4.90 vs 4.73; overall 3.97 vs 3.41 (not significant) | Si 2025 (a08, b04, c06) | S (K02) |
| Idea-stage score does not predict executed score for AI ideas | Pearson AI: novelty -0.019, excitement -0.321, effectiveness 0.172, overall -0.092; human overall 0.158; N=43 in total. After execution overall tracks effectiveness r=0.654 | Si 2025 app. D (d07, d08) | S (K19) |
| LLM judges and human reviewers both near chance on fine ranking | Human reviewer agreement 56.1% (balanced split-half); best LLM pairwise ranker 53.3%; Claude-3.5 zero-shot accept/reject of papers 71.4%, GPT-4o 61.1%, Claude-3-Opus 63.5%; few-shot and CoT no significant gain; only 17 of 49 reranked ideas overlapped the AI-ranked top | Si 2024 (a07, b03, c05) | S (K03) |
| Over-generation saturates | 4000 seed ideas per topic; about 200 (5%) non-duplicates at cosine 0.8 (MiniLM); threshold set by manual inspection | Si 2024 (a07, b02, c05) | S (K04) |
| Planning plus retrieval raises unique ideas at equal idea count | 100 ideas per method; over 80% unique; 3.4x more unique novel ideas than baseline; without planning unique ideas flat (42.4 at step 2, 44.1 at step 3). Token cost not matched | Nova (d11) | S, confounded |
| Five ideation architectures differ in novelty | Mean novelty 3.57, feasibility 2.80, impact 3.47 (0-5); 30 ratings (6 experts x 5 proposals); best 4.17 (decomposition, long-context); reflection-only 2.33; novelty-feasibility r=0.23 | 2026 study (d12) | S, weak |
| A quarter of LLM proposals have verified source overlap | 13 experts, 50 proposals; 14.0% score 5 plus 10.0% score 4 = 24.0%; Turnitin 0%, OpenScholar 0%; GPT-4o finds the source 89.0% with oracle access, 32.7% from parametric memory, 68.5% with SSAG; Claude 3.5 Sonnet 88.8%, 1.3%, 51.3%. (An earlier note said 36% including score 3; the table gives 32.0%, so 36% is wrong.) | Gupta and Pruthi 2025 (b09, b10) | S (K14) |
| LLM + numeric evaluator beats classical symbolic regression at far lower evaluation count | LLM-SR 2.5K iterations vs 2M+ for PySR, uDSR, DSR, NeSymReS, E2E; E. coli out-of-domain NMSE about 0.0037 vs above 1 for others; 4 new tasks; GPT-3.5 and Mixtral backbones; some Mixtral E. coli OOD results worse (5.46) | Shojaee 2024 (a04, c10) with a03 | E (K05) |
| LLM equation discovery inflated by memorisation | 239 problems (111 LSR-Transform, 128 LSR-Synth); best symbolic accuracy 31.5% (LLM-SR, GPT-4o-mini) and 28.1%; direct prompting GPT-4o-mini 7.21%; LaSR best numeric Acc0.1 50.45% on Transform; at equal node-count complexity Transform below Feynman; symbolic match judged by GPT-4o (94.6% agreement with humans) | LLM-SRBench (a05, b11, b12, c11) | E (K06), indirect evidence |
| Non-LLM structure search solves the textbook set but is brittle | AI Feynman 100/100 vs Eureqa 71; bonus 90% vs 15%; SRBench exact recovery 53% at zero noise vs 27% (GP-GOMEA); beaten by DSR, gplearn, AFP_FE, AFP above noise 0.01; not different from others on Strogatz ODEs | a01, c19, b13, b20, d10 | E (K07) |
| Program search with an exact scorer finds verified new results | AlphaEvolve: matched best known on 75% and improved 20% of 50+ open problems; 4x4 complex matmul in 48 multiplications; kissing number d=11 to 593; 0.7% fleet compute recovered; 23% kernel speedup; 1% Gemini training time | a16, b16, c12 | S (K08), developer-reported |
| FunSearch hit rate and cost | n=8 cap set of 512 found in 4 of 140 runs (about 3%); capacity bound 2.2180 to 2.2202; full I(12,7) set in 60% of runs; bin packing excess bins over L2 bound (first fit / best fit / FunSearch): OR1 6.42/5.81/5.30%; OR3 5.74/5.37/3.11%; Weibull 100k 4.00/3.79/0.03%; about 10^6 samples, 150 CPU evaluators. Prior record 496 and the no-LLM ablation not verified | Romera-Paredes 2023 (d01, d02) | S (K08, K18) |
| Agentic data-driven discovery benchmarks stay low | DiscoveryBench best 25% (biology and engineering 0%); ScienceAgentBench 32.4% alone, 34.3% with expert knowledge, o1-preview 42.2% at over 10x cost; MLE-bench bronze+ 16.9% pass@1, 34.1% pass@8; PaperBench best agent 21.0% | a17, a18, b14, b15 | E (K09) |
| More compute helps, but not uniformly | ScienceAgentBench 32.4 to 42.2%; MLE-bench pass@8 doubles pass@1; GPT-4o 8.7% at 24 h vs 11.8% at 100 h; co-scientist Elo rose over time on 203 goals with no saturation; PaperBench o1 plateaus after about 1 h and humans overtake after about 24 h (41.4% vs 26.6%, 3-paper subset) | a17, b14, a13, d09 | C (K10, K21) |
| Fully automated paper pipelines fail often in independent tests | 5 of 12 experiments (42%) crashed; code edits +8% characters on first iteration, then 118, 83, 66, 21; median 5 citations, 5 of 34 from 2020 or later; all 12 ideas labelled novel incl. micro-batching for SGD; 4 of 7 manuscripts had missing figures or hallucinated numbers; DeepReviewer rated all 28 papers from 5 systems as reject (ratings 2.33-4.63) | Beel 2025 (a11, b05); Yang 2025 (c15) | E (K11) |
| AI-written papers can pass a low bar | One of 3 AI Scientist v2 manuscripts scored 6, 6, 7 (mean 6.33, about top 45%) at an ICLR workshop, withdrawn after acceptance; the other two rejected; Jr. AI Scientist rejected at Agents4Science | a12, b08, c18 | E (K12), low bar |
| AI Scientist v1 reviewer | Balanced accuracy 0.65 vs 0.66 for humans; F1 0.57 vs 0.49; AUC 0.65 both; false negative rate 0.39 vs 0.52; correlation 0.18 with human mean vs 0.14 between two humans; $0.25-0.50 per review; independent test rejected 9 of 10 papers incl. 4 humans accepted | Lu 2024 (a10); Beel 2025 (b06) | C (K13) |
| LLM reviewer ensembles near human accuracy | 1,963 ICLR 2025 papers: meta-reviewer over all personas 81.8%, average of personas 75.1%, default single reviewer 70.6%, human average 83.9% (n=540), top 1% human 92.4%; 5-way accuracy 52.5% meta vs 37.6% human average; BERT 63.7%; reviewers turn more positive after rebuttal | ReviewerToo (d03, d04) | S (K20) |
| Autonomous long-run scientist: accurate reports, weak synthesis | 102 audited statements: 79.4% accurate; data analysis 85.5% (n=55); literature 82.1% (n=28); synthesis 57.9%; 200 rollouts, 42,000 lines of code, 1,500 papers per run; 4.1 expert-months (n=6) or 6.14 (n=7) per 20-cycle run | Kosmos (b18, b19, c17) | S (K15), company-reported |
| Co-scientist wet-lab results | 3 of 5 AML repurposing drugs reduced viability (binimetinib IC50 as low as 2 nM; KIRA6 10 nM vs 180 nM in TK6); cf-PICI mechanism matched unpublished lab work (n=1, no denominator); 11 goals: preference rank 2.36, novelty 3.64/5, impact 3.09/5; o3-mini-high and R1 competitive at much lower compute | a13, a14, b23, d13 | C (K16), developer-reported |
| Shared prior reports help modestly, with a selection problem | Single lab reading its own papers: 70.2 to 78.2% MATH-500 (+11.4% relative, N=40 generations); three labs 13.7% relative; transfer +3.3% on average (MedQA 79.6 to 85.6); best method chosen on the same MATH-500 test set; parallel labs duplicated effort; hallucinated experiment results | AgentRxiv (c14, d05, d06) | S (K17) |
| Robot scientists have few comparable numbers | Eve: 14,400 compounds, over 10,000 per day, three loops of 96, TNP-470 IC50 0.16 uM vs over 165 uM; Adam 12 of 20 only as secondary report; Genesis 12 of 48 units, aims only | d14, d15, d16 | W (K23) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it.

### 4.1 Propose-evaluate-feedback loop with an evolutionary buffer (LLM-SR, FunSearch, AlphaEvolve)

1. Define a scorer in code: input is a candidate (equation skeleton as a Python function, or a program), output is a number. It must run fast and be exact. Score on data the generator has not seen where possible (LLM-SR reports in-domain and out-of-domain error).
2. Keep a buffer (FunSearch: islands) of the best candidates with their scores. Several independent islands keep diversity; periodically reseed the worst islands from the best.
3. Build a prompt that shows a few top candidates (sorted by score, with the score and a short problem description) and asks for a new or improved one. Sample many in parallel.
4. Run each candidate, drop those that crash or time out, add the rest to the buffer.
5. Repeat. Report the hit rate across repeated runs, not only the best run (FunSearch: 4 of 140 runs found the record; K18).

For continuous constants (LLM-SR), the LLM writes only the form; a numeric optimiser fits parameters inside the evaluator. This split (LLM does structure, code does numbers) is a main reason it needs 2.5K iterations, not 2M+.

### 4.2 Structure-exploiting decomposition (AI Feynman)

1. Fit a neural network to the data.
2. Test the fitted function for dimensional analysis, symmetry (translation, scaling), separability (f(x,y)=g(x)h(y) or g(x)+h(y)), and compositionality.
3. If a test passes, split the problem into sub-problems with fewer variables and recurse.
4. Solve small problems by brute-force search over a grammar; keep a Pareto frontier of error against complexity (v2).

This is what lets it reach 100/100. The tests only help when the data match the assumptions (SRBench: poor on noisy real data).

### 4.3 Generate-debate-rank tournament (co-scientist)

Agents: generation, reflection, ranking, evolution, proximity (de-duplication), meta-review. Hypotheses play pairwise debates; an Elo rating accumulates; top ones are evolved; the loop runs longer to scale compute. Note the circularity: the Elo is produced by the same system family that proposes the hypotheses, and the authors state that Elo is auto-evaluated. Wet-lab outcomes (3 of 5 drugs) are the only independent evidence. Our G9 says no debate; this system uses debate, but no source isolates debate from extra sampling (K16 is contested).

### 4.4 Idea agent with retrieval, over-generation, de-duplication and ranking (Si 2024)

Retrieve up to 120 papers; generate 4000 seed ideas per topic; de-duplicate at cosine 0.8 (about 200 remain); pairwise-rank with N=5 rounds; expand into proposals. Failure points the authors found: duplicates dominate, and the LLM ranker is near chance (53.3%).

### 4.5 Plan-retrieve-generate loop (Nova)

Plan the next retrieval from the current ideas; retrieve; generate; repeat. Without the planning step unique ideas stay flat. Cost is not reported, so equal-token benefit is unknown.

### 4.6 Tree search over experiments (AI Scientist v2)

A manager agent runs best-first tree search over experiment code; a vision-language model reads figures and gives feedback; no human templates. Result: one of three workshop papers passed.

### 4.7 Persistent world model plus parallel agents (Kosmos)

A shared structured memory links a data-analysis agent and a literature agent over up to 20 cycles. Every claim must cite code or a paper (traceability). Reported value grows close to linearly to 20 cycles. The weak part is synthesis (57.9%), where claims are interpretations not directly computed.

### 4.8 Reviewer ensemble (ReviewerToo)

Run several persona reviewers (default, permissive, critical, and so on), then a meta-reviewer combines them. Ensemble 81.8% vs single 70.6%. Caution: permissive and critical personas have near-zero or negative agreement (kappa), and reviewers shift positive after seeing a rebuttal, so hide rebuttals and authorship.

### 4.9 Shared report repository (AgentRxiv)

Agents write reports to a store; later agents retrieve them. The gain is real in the single-lab case but the selection-on-test-set problem inflates it. Needs an out-of-sample check before trust.

## 5. What holds up

### 5.1 Holds up (two or more sources)

- **An exact evaluator makes LLM search effective.** LLM-SR (2.5K vs 2M+ iterations), FunSearch and AlphaEvolve all use code scorers. Independent confirmation is partial: LLM-SR is followed up by LLM-SRBench (same group), and AlphaEvolve and FunSearch are one lab (K05 established; K08 single-source).
- **Memorisation inflates textbook benchmarks.** LLM-SR notes under-20-iteration Feynman success; LLM-SRBench measures the gap (K06). The test is indirect, but the direction is consistent.
- **Agent benchmarks of real discovery tasks stay low** (25%, 32.4%, 16.9%, 21.0%), across four benchmark groups (K09).
- **Independent audits of AI Scientist found many failures** (42% crash, thin citations, hallucinated numbers, all 28 papers reject-level; K11). The original authors listed hallucinated plots and ablations as failures too.
- **Non-LLM structure search is strong on clean textbook data and brittle on noise** (K07).

### 5.2 Single-source or contested

- Pre-execution novelty advantage and its post-execution collapse (K01, K02). One group, one field (NLP prompting ideas), one 2024 model generation, N=43 executed ideas. The ranking flip is not significant at this N. Treat the direction as strong, the size as uncertain.
- Reviewer reliability (K13): Lu reports 65% vs 66% balanced accuracy; Beel found 9 of 10 rejected (n=10); ReviewerToo found ensemble 81.8% vs single 70.6% on 1,963 papers. The conflict is explained by single prompt vs ensemble and by sample size, but Lu's reviewer was not retested at scale.
- Compute (K10): more compute helps on ScienceAgentBench and MLE-bench but not past about an hour on PaperBench for o1. The plateau may be a scaffold artefact (the agent stops early). The boundary condition is unknown.
- Co-scientist (K16): wet-lab support is real but 3 of 5 and developer-run; no independent audit.
- AgentRxiv (K17): selection on the test set.

### 5.3 Failures and failed replications

- AI Scientist v1 replication (Beel): 42% crash, novelty check wrongly labelled known ideas novel. Small sample (12 experiments, one student, older model version).
- Idea novelty did not survive execution (Si 2025).
- Idea-stage judge scores have near-zero or negative correlation with executed scores for AI ideas (K19).
- Plagiarism checkers: 0% detection (K14). Retrieval of the source, not detection, is the bottleneck.
- LLM-SR gains were not uniform: Mixtral E. coli OOD NMSE 5.46 (a04).
- AI Feynman is not significantly better on Strogatz ODEs or real-world black-box problems (b20).
- Kosmos synthesis statements 57.9% accurate (K15).

### 5.4 Moderators

| Moderator | Effect |
|---|---|
| Cheap exact scorer present | Loop wins (records, 2.5K iterations); absent: 25-32% benchmarks |
| Familiar vs transformed problem | Large drop for transformed forms (31.5%, 28.1%) |
| Noise | AI Feynman exact recovery falls above 0.01 noise |
| Judging before vs after execution | Novelty gap of +0.80 turns to a drop of about 1 point |
| Domain | DiscoveryBench: economics 25%, sociology 23%, biology and engineering 0% |
| Reviewer: single prompt vs ensemble | 70.6% vs 81.8% |
| Model strength | AlphaEvolve and Lu 2024 improve with stronger LLMs (Llama 405B 2.30 vs Sonnet 3.82 mean reviewer score) |

### 5.5 Interventions that worked and did not

Worked: code evaluators with held-out data; evolutionary buffers; extra attempts (pass@8); structure-based problem splitting (non-LLM); retrieval planning for diversity (Nova, equal idea count only); reviewer ensembles; requiring citations of code or papers (Kosmos).

Did not work: over-generation of ideas (plateau at about 5% unique); LLM pairwise ranking of ideas (53.3%); few-shot and CoT for the ranker (no significant gain); keyword novelty search; commercial plagiarism tools (0%); letting reviewers read a rebuttal (they drift positive).

## 6. Language models

How LLMs behave on these tasks, and what changed it.

| Task | Result | What changed it |
|---|---|---|
| Rate novelty of ideas (as writer) | AI ideas +0.80 novelty vs experts pre-execution | Pipelines differ: reflection-only 2.33 vs decomposition 4.17 of 5 (d12) |
| Execute those ideas | AI ideas lose 1.05 to 1.88 points; humans about 0 | Executors changed some ideas during implementation (b26) |
| Rank ideas | 53.3% pairwise vs 56.1% human agreement | Few-shot and CoT: no significant gain |
| Review papers | Single prompt 70.6%; ensemble 81.8% vs 83.9% human; AI Scientist reviewer 65% | Ensemble of personas +11 points; weaker models (4o-mini, Llama 405B) much worse |
| Equation discovery, famous forms | Low error in under 20 iterations | Memorisation |
| Equation discovery, transformed | 31.5% symbolic accuracy (best) vs 7.21% direct prompting with GPT-4o-mini | Programming-with-LLM scaffold plus evaluator |
| Open math problems | 20% beaten, 75% matched | Stronger LLM improves results; removing evolution or context hurts |
| Data-driven discovery | 25%, 32.4%, 42.2% (o1-preview, more than 10x cost) | Expert knowledge +1.9 points on ScienceAgentBench |
| ML engineering | 16.9% pass@1, 34.1% pass@8 | More attempts doubles; 100 h vs 24 h gives only +3.1 points for GPT-4o |
| Paper replication | 21.0%; o1 plateau after about 1 h | Humans overtake after about 24 h |
| Long autonomous runs | 79.4% statements accurate; synthesis 57.9% | Traceable citations to code and papers |
| Source detection for plagiarism | 1.3% (Claude 3.5 from memory) to 88.8% (with oracle source) | Retrieval is the whole difference |

**Reading across the rows.** LLMs are good proposers and poor judges. Where code judges, results are real. Where an LLM judges, results are inflated or unstable: the co-scientist Elo, LLM reviewers, the GPT-4o symbolic-match check (94.6% agreement with humans), DeepReviewer scoring. How much these judges move the headline numbers is not measured.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Evidence ids as above.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep G8 as is. Never let the generating model pick among its own ideas; select by running candidates in code. The discovery sources add that ideation scores did not predict execution (Pearson -0.09 overall for AI ideas) and ranker accuracy is 53.3% vs 56.1% | G8, G5 | [E] (already in schema); the new post-execution data are [S] | a07, b03, c05, d07; K03, K19 |
| A2 | For items with a numeric or program check, run propose-evaluate-feedback: show the model its best candidate(s) with score, fit constants in code, keep the buffer. This is the S3/S4/S5 loop already in the schema; the literature confirms the evaluator is the active ingredient | S3, S4, S5, G2 | [E] | a04, c10, a03; K05 |
| A3 | Evaluate on mutated or unseen forms; report the gap from the original. A pass on the textbook form is not proof | G3 | [E] | a05, b12, c11; K06 |
| A4 | On noisy data, do not trust a structure-exploiting decomposition until its gain is checked on held-out noisy data | O3, O6, G3 | [E] | b13, b20, d10; K07 |
| A5 | Do not use keyword search as a novelty check. If a novelty step is used it must retrieve and compare to sources | G8 | [E] | b05, b09, b10; K11, K14 |
| A6 | Keep G9. The strongest discovery system that uses debate gives no isolated debate-vs-sampling test, so nothing here overturns the schema | G9 | [E] (schema stays) | a13, b23; K16 |
| A7 | Final claims that are not computed or cited are the weakest part of long autonomous runs; tag claims by type and verify the interpreted ones | G10, S8 | [S] (one audit); general idea matches G10 [E] | b18, c17; K15 |
| A8 | Log hit rate across repeated runs and samples per success, not best-of-run | G7 | [S], design hygiene | d01; K18 |

### Test first (single-source, contested or open)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Equal-token control: generate-test-select (code scoring) vs best-of-N plain sampling on discovery-type items. No source runs this | G7 | open | K22, d11, d12 |
| T2 | Run-then-select vs judge-then-select: rank by executed outcome and compare to model-judge rank | G8 | [S] | a08, d07; K02, K19 |
| T3 | Novelty-by-retrieval step in S4 (find a source, then compare) | G8, S4 | [S] | b09, b10; K14 |
| T4 | Code de-duplication and unique-count monitor in S3; do operator prompts (O1-O8) raise unique count at equal tokens? | S3, O1-O8, G4 | [S] | a07, d11; K04 |
| T5 | Opposed-persona ensemble as a screen, rebuttals and authorship hidden | G5, S4 | [S] | d03, d04; K20 |
| T6 | Retained-notes memory across tasks vs none, with out-of-sample check | memory | [S] | d05, c14; K17 |
| T7 | Compute allocated by difficulty vs uniform; score vs token budget to find the plateau; one long run vs several short fresh runs | G12, G11 | [C] | a17, b14, d09; K10, K21 |
| T8 | Claim-type auditing in S8: does it cut wrong final claims? | S8, G10 | [S] | b18; K15 |

## 8. Concrete tests on our bench

All arms get equal total tokens, with setup cost counted (G7). Use existing bench items (ARC-style, word puzzles, BrainTeaser) plus a small equation-recovery set with transformed forms for items with a numeric check.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 control | Items with a code check (ARC programs; equation recovery with transformed forms) | (a) plain model, N samples, first pass or majority; (b) scaffold: generate, test on the check, revise from failing output, select by code | Held-out pass rate per 1M tokens; hit rate across 5+ repeats | Scaffold above plain only where a held-out check exists. Decides G7 for discovery; size unknown |
| T2 | Open design or idea items where a runnable outcome exists | (a) model judge picks; (b) run every candidate, pick by outcome | Rank correlation of pick with later outcome; mean final outcome | Run-based wins; judge-outcome correlation near 0 to 0.2 |
| T3 | Idea items with known prior art | (a) no novelty step; (b) keyword search; (c) retrieve then compare | Share of true prior-art ideas flagged; ideas kept | (c) above (b) above (a); keyword near zero |
| T4 | Open-mode generation (S3) | (a) plain resampling; (b) fresh context plus one operator per attempt | Unique candidates per 100k tokens after dedup (cosine 0.8) | Plain plateaus near 5% unique; operators raise it, size unknown |
| T5 | Single-answer and review-like items | (a) single judge; (b) 3-persona ensemble with code aggregate; (c) majority of plain samples | Accuracy against ground truth | Ensemble above single judge by about 10 points (ReviewerToo); vs plain samples probably null (G4, G9) |
| T6 | Sequences of related items | (a) no memory; (b) lessons shown after first attempt; (c) lessons shown before | Pass rate on later items; contamination check on held-out set | (b) small gain; (c) fixation risk; AgentRxiv transfer was only +3.3% |
| T7 | Mixed-difficulty set | (a) uniform budget; (b) difficulty-based budget; (c) one long run vs several short fresh runs | Pass rate vs tokens, plateau point | Short fresh runs above one long run past the plateau; size unknown |
| T8 | Answers with explanations | (a) none; (b) tag claims, verify interpreted ones | Wrong final claims per 100 | Fewer interpreted-claim errors; size unknown |

## 9. What does not transfer, and why

- **The discovery wins depend on a fast exact scorer** (AlphaEvolve, FunSearch). Many of our items have a weak or no check (no-check mode). These results transfer to checked mode only.
- **Scale of search.** FunSearch used about 10^6 samples and 150 CPU evaluators; the headline cap set came in 4 of 140 runs. Our token budgets are far smaller. Expect hit rates well below the headline.
- **Evolutionary islands** need a large population; with 2 to 4 short attempts there is nothing to evolve. Borrow the evaluator and feedback, not the island structure.
- **Multi-agent tournaments and shared repositories** (co-scientist, AgentRxiv) conflict with the single-agent design and G9; their gains are confounded by extra sampling and, for AgentRxiv, test-set selection.
- **Idea novelty studies are NLP-only**, human-judged, on 2024 models. Our bench has no human-novelty items.
- **Paper-level results** (workshop acceptance, reviewer scores) do not map to our item types (K12: calibration only).
- **Robot-science wet-lab loops** need hardware; nothing to implement.
- **Time-saved claims** (Kosmos 4.1 and 6.14 expert-months) are subjective estimates, not accuracy.
- **Founding-era systems** (BACON, Adam): no verified numbers, so nothing to compare.

## 10. Open questions

1. Does any generate-test-select loop for discovery beat best-of-N sampling at equal tokens? (K22; no source; decides G7.)
2. How well does code-run outcome predict later human-judged value outside NLP prompting ideas? (d07 is N=43.)
3. How often is a "novel" hypothesis a retrieved one in biology and chemistry? No overlap-rate study found beyond the NLP 24.0%.
4. Where does extra compute stop helping, and is the PaperBench plateau a scaffold artefact? No compute-versus-horizon curve across tasks.
5. Which Kosmos and co-scientist claims fail in independent labs? No independent audit found; d13 is n=1 and journalistic.
6. Are LLM-based symbolic regression methods noise-fragile like AI Feynman? SRBench has no LLM method.
7. Does shared memory survive without selecting on the test set? AgentRxiv's best method was chosen on MATH-500 itself.
8. How much of the LLM-SRBench gap is memorisation and how much real difficulty? No clean contamination test.
9. What are FunSearch's exact prior record (496?) and the no-LLM ablation? Supplement not opened.
10. What hit rates do classical systems (BACON, Adam) have, for comparison? Not retrieved.
11. How much do LLM judges (GPT-4o symbolic match, DeepReviewer, Elo) change the headline numbers? Not measured.

## 11. Sources

[V] = opened and read this session (arXiv full text, PMC page, or PDF text). [M] = snippet or recall only.

| Source | Mark | URL |
|---|---|---|
| Udrescu and Tegmark (2020) AI Feynman | [V] | https://arxiv.org/abs/1905.11481 |
| Udrescu et al. (2020) AI Feynman 2.0 | [V] | https://arxiv.org/abs/2006.10782 |
| Cranmer (2023) PySR | [V] per a03; c20 says downloaded, not read | https://arxiv.org/abs/2305.01582 |
| La Cava et al. (2021) SRBench | [V] | https://arxiv.org/abs/2107.14351 |
| Shojaee et al. (2024) LLM-SR | [V] | https://arxiv.org/abs/2404.18400 |
| Shojaee et al. (2025) LLM-SRBench | [V] | https://arxiv.org/abs/2504.10415 |
| Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas | [V] | https://arxiv.org/abs/2409.04109 |
| Si, Hashimoto, Yang (2025) The ideation-execution gap | [V] | https://arxiv.org/abs/2506.20803 |
| Lu et al. (2024) The AI Scientist | [V] | https://arxiv.org/abs/2408.06292 |
| Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist | [V] | https://arxiv.org/abs/2502.14297 |
| Yamada et al. (2025) AI Scientist-v2 | [V] | https://arxiv.org/abs/2504.08066 |
| Gottweis et al. (2025) Towards an AI co-scientist | [V] | https://arxiv.org/abs/2502.18864 |
| IEEE Spectrum report on co-scientist at Imperial College | [V] (journalistic) | https://spectrum.ieee.org/ai-co-scientist |
| Romera-Paredes et al. (2023) FunSearch (Nature) | [V] via PMC page read through a summariser; Nature page [M] | https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/ ; https://www.nature.com/articles/s41586-023-06924-6 |
| Novikov et al. (2025) AlphaEvolve | [V] | https://arxiv.org/abs/2506.13131 |
| Chen et al. (2025) ScienceAgentBench | [V] | https://arxiv.org/abs/2410.05080 |
| Majumder et al. (2024) DiscoveryBench | [V] | https://arxiv.org/abs/2407.01725 |
| Chan et al. (2025) MLE-bench | [V] | https://arxiv.org/abs/2410.07095 |
| Starace et al. (2025) PaperBench | [V] | https://arxiv.org/abs/2504.01848 |
| Mitchener et al. (2025) Kosmos | [V] | https://arxiv.org/abs/2511.02824 |
| Schmidgall and Moor (2025) AgentRxiv | [V] | https://arxiv.org/abs/2503.18102 |
| Yang et al. (2025) AI Scientists fail without strong implementation capability | [V] | https://arxiv.org/abs/2506.01372 |
| Toyooka et al. (2026) Jr. AI Scientist | [V], exact scores not extracted | https://arxiv.org/abs/2511.04583 |
| Gupta and Pruthi (2025) All that glitters is not novel | [V] | https://arxiv.org/abs/2502.16487 |
| Sahu et al. (2025) ReviewerToo | [V] | https://arxiv.org/pdf/2510.08867 |
| Nova (2024) iterative planning and search for novel ideas | [V] | https://arxiv.org/pdf/2410.14255 |
| Multi-workflow novelty study (2026) | [V] | https://arxiv.org/html/2601.09714 |
| King et al. (2024) Genesis | [V] | https://arxiv.org/pdf/2408.10689 |
| Williams et al. (2015) Eve, repositioning drugs | [V] via summariser | https://pmc.ncbi.nlm.nih.gov/articles/PMC4345494 |
| Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery (BACON) | [M] | https://mitpress.mit.edu/9780262620529/ |
| Schmidt and Lipson (2009) Eureqa, Science | [M] | https://doi.org/10.1126/science.1165893 |
| King et al. (2009) The automation of science (Adam), Science | [M] | https://doi.org/10.1126/science.1165620 |
| Scientific American on Robot Scientist Adam (12 of 20) | [M] | https://www.scientificamerican.com/article/robot-scientist-discovers-potential-malaria-drug/ |
| Burger et al. (2020) A mobile robotic chemist | [M] | https://doi.org/10.1038/s41586-020-2442-2 |

*Links to parallel subfields (not covered here): Retrieval and ensembles for LLM forecasts, RL on verifiable rewards, Probabilistic programming, Autoformalisation, Search theory, Social epistemology of discovery, Kuhn and paradigm crisis, Research methods, Team science, Strong Programme and SSK, Minimum message length.*

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 6 established claims: 4 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E15.10-K05** (now single-source: the sources are not independent). All supporting evidence is one paper (Shojaee et al., LLM-SR, listed twice); Cranmer's PySR paper is a software description that does not support the claim; the numbers (2.5K vs over 2M iterations, E. coli OOD NMSE 0.0037 vs lowest baseline 1.01) match, but the paper itself is inconsistent (main text says 22M).
- **E15.10-K06** (now single-source: the sources are not independent). All sources are the same lab's papers (LLM-SRBench listed five times plus LLM-SR by the same authors); numbers 31.5% and 28.1% match, but memorisation is only 'suggested' by the authors, not shown independently.
