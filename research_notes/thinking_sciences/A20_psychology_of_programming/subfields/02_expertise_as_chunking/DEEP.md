# Expertise as chunking: deep document

*Subfield A20.02. Status in SUBFIELDS.md: hypothesis, not established. Evidence files: evidence_a-d.jsonl (ids a01-d16). Claims: claims.jsonl (A20.02-K01 to K29). Cross-check: critique.md.*

## 1. What it is

Chunking is grouping many small items into one unit that can be held, recalled and reasoned about as a whole. In programming, the claim is that experts see a program as a few meaningful units (a "sort", a "control break", a "running total"), and novices see it line by line.

Vessey (1985) took this one step further. She did not test whether experts chunk. She defined expertise by chunking. A programmer was an "expert" if the way they debugged one COBOL program showed effective chunking: few jumps between functions, few returns to the top, few changes of location. Then she asked what else the experts did. Her answer, stated as propositions "for further testing", was:

- Experts debug breadth-first and build a model of how the whole program works (a "system view").
- Novices either lock onto one early hypothesis and go depth-first, or search broadly but with no system model. Both fail.

Why this is in our series: our agent is one language model with a thinking schema. The schema has a "do not lock in" flavour (G1: doubt only on a signal; S6 impasse; O1-O8 operators). Vessey gives a human-derived story for why lock-in hurts. The question for us is narrow. Can the three chunking counts be measured on an agent trace, do they predict failure, and would a step that forces a program model and several candidate faults before the first edit help at equal tokens?

Honest status after this research:
- The founding study is N=16, one program, one firm. No independent replication was found (d14, d15; K28).
- Most "chunking" papers on LLMs (2023-2026) use the word for retrieval units, tokenisation or compact prompts. They do not test Vessey (K23).
- The best we can claim is a weaker design statement: structure-aware units beat fixed-size units, and building a model of the code before editing tends to help agents (K18, K04).

## 2. History and theories in depth

**2.1 Chess and the chunk (1973-1996).** Chase and Simon (1973) showed that chess masters recall real positions far better than novices and do not recall random positions better. The explanation: masters hold tens of thousands of familiar patterns (chunks). Gobet and Simon (1996) tested the strong version on random positions. Gobet et al. (2001) review chunking mechanisms. CHREST is the computational model. We did not open these (b18, b19, b25, c25: metadata or snippets only; no numbers cited). The later "template" account (chunks plus slots and links) is a rival to pure chunk counts; its use for agent memory is unsettled (gap 10).

**2.2 Recall studies for code (1976-1981).** Shneiderman (1976) and McKeithen et al. (1981) are the standard citations for the code version: experts recall coherent programs better than novices, and the advantage shrinks or vanishes for scrambled programs. Exact numbers were not recovered in this run (b11, b12, c24 are metadata only). Do not quote effect sizes. Brooks (1977), as cited by Vessey, put a typical programmer's store at about 50,000 chunks (a09; an estimate, not a measurement).

**2.3 Plans, schemas and beacons (1981-1990).**
- Adelson (1981, 1984): experts organise by function (abstract categories), novices by surface syntax. A secondary snippet gives chunk size 3.5 vs 2.4 items (c23, not opened; do not cite).
- Rist (1986), as reviewed by Detienne (1990): asked to group lines that "did the same thing", novices used a mix of syntax and plan chunks; experts used almost only plan chunks; plan use fell for complex programs (a15).
- Soloway and Ehrlich (1984): experts rely on programming-plan and rules-of-discourse knowledge; code that breaks the conventions hurts experts more (second-hand).
- Wiedenbeck (1986): beacons are surface cues (a name, a swap of two variables) that trigger a plan. Not opened (b14).
- Detienne (1990) review (a13-a16): experts evoke plans from cues and distort recall toward schema defaults (recalled counter I instead of J, "while" for "repeat", an inserted "creation" function not in the program). 269 production rules coded and grouped into 47 general rules in one protocol study; N not given. Norcio found indenting by functional chunks raised correct fill-in. Detienne notes the plan vs control-flow question was not resolved with strong controls.
- Pennington: control-flow structure is read first, language-dependent; this is the main rival to the plan account (K08).

**2.4 Vessey (1985).** Founding process study (a01-a09). Details in section 3. Vessey 1985 is cited about 295 times and the 1986 follow-up 82 times (d14). No citing title in a 300-title screen read as a replication.

**2.5 Modern human work (2017-2026).**
- fMRI: Siegmund et al. (2017), 11 participants: bottom-up comprehension (obfuscated names, scrambled layout) activated more of BA 39, 6, 21, 40, 44 than comprehension with semantic cues. The authors read this as semantic chunking (a19). The expected memory-area activation for plans was not found.
- Expertise and cortex: Ikutani et al. (2021) found that how well the function category of a snippet can be decoded from cortex tracks AtCoder rating (b02).
- Learning: one Python semester produced no clear new neural code in 22 novices (b04). EEG of 45 readers: expertise sharpened the response to syntax violations (P600) but not to semantic implausibility (N400) (b03).
- Mapping study: of 95 code-comprehension experiments, 53.7% used only students and 9.5% only professionals. Very few link to chunking, beacons or plans. No pooled effect size (b05).
- Working memory in tracing: about 7 variable-value pairs, no name effect (b01).
- Debugging: Alaboudi and LaToza (2020, 2021) and Li and Coblenz (2026) study professional debugging. None replicates Vessey's counts (d02-d04).

**2.6 LLM era (2023-2026).** Four threads, none a direct test of Vessey:
1. Names as beacons: LLMs lose accuracy when identifiers are removed or misleading (a25, a22, d11).
2. Structure-aware chunks for retrieval and documentation (cAST, Glasz; b09, c15, a26).
3. Human attention or gaze used as a prior for training (EyeMulator, EyeLayer, HumanLLM; c05-c07).
4. Plan-first and coarse-to-fine generation or localisation (Self-planning, Structured CoT, Parsel, CodeChain, Agentless, ACQUIRE; c16-c20, d01).

## 3. Core findings with exact numbers

Status key: E established (2 or more independent sources, consistent), S single-source, C contested, H human-only, O older or small models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Vessey sample and task | 16 programmers, one firm, 8 "experts" and 8 "novices" by chunking class; one COBOL sales-report program with a control-break bug; two bug levels (high, low), 4+4 per cell | Vessey 1985 (a01) | S, H |
| Chunking measured by three counts | switches between debugging functions; returns to the top "Debug program" function; changes of location. 11 of 16 got the same class on all three; 3 on a 2:1 basis; 2 ties; one borderline subject made an expert to keep 8 vs 8 | a02 | S, H |
| Chunking class predicts debug time better than manager rating | 73.7% vs 36.1% of variance; mean 15 min 40 s (experts) vs 28 min 3 s (novices); manager split 20 min 24 s vs 23 min 19 s | a03 | S, H (partly circular) |
| Experts take fewer steps, not faster steps | time to discover error P=0.005 (R2=0.572); phases P=0.001 (R2=0.712); episodes P=0.003 (R2=0.570); modules P=0.045 (R2=0.299); mistakes P=0.005 (R2=0.500); hypotheses P=0.045 (R2=0.230); time per episode not different | a04 | S, H |
| Lock-in on a hypothesis is the novice failure | 9 of 16 stated hypotheses; 19 in total; 4 clearly constrained (NH1, NL2, NL3, NL4), all novices; two used shotgun random edits; all five who made an incorrect change were novices by chunk class | a05, critique | S, H |
| Search breadth alone is not enough | two binary conditions (breadth-first search; system thinking) matched the chunk class for 15 of 16; breadth-first without a model still failed and counted as novice; 6 of 16 strategy paths used | a06 | S, H |
| Start point, read vs mentally execute, data division did not separate groups | data-division items R2=0.104; output-first vs program-first no effect | a08 | S, H (low power) |
| Vessey's own limits | classification never tested for reliability; one program; propositions untested statistically | a07, a09 | S |
| No replication found | 300 citing titles screened, 0 replications; N=16 listed in a behaviour-study table; larger strategy studies (N=44, N=77) are students and not opened | d14, d03 | S |
| Early hypothesis quality matters more than fault location (humans) | 20 developers, 60 sessions; potential hypotheses OR 6.24 (p=0.03); fault locations OR 1.4 (p=0.64); correct hypothesis at stage 2 gives 5x success (p=0.01); first hypotheses 11% correct (3 of 27) | Alaboudi, LaToza 2020 (d02) | S, H |
| A debugging strategy can be taught | 44 undergraduates (41 finished); context-specific steps 80% correct after one session and after 3 weeks (CI 62-98%) vs 20-44% in other groups (p<0.05, Holm); time 13-15 min vs 22-27 min | d05 | S, H |
| Function-level cortical code tracks rating | decoding accuracy 76.0% (SD 13.5) vs AtCoder rating mean 954.3 (SD 864.6): r=0.593 (p=0.0059, n=20); r=0.722 (p=0.000007, n=30) | Ikutani 2021 (b02) | C, H |
| Semantic cues cut activation vs bottom-up reading | 11 participants, 12 trials each, p<0.01 FDR | Siegmund 2017 (a19) | S, H |
| Expertise sharpens syntax, not semantic, brain response | N=45; P600 expertise x syntax b=1.04 p<0.001; N400 interaction b=0.45 p=0.025; semantic x expertise behaviour b=-5.30 p=0.051 | Kuo, Prat 2024 (b03) | S, H |
| Tracing working-memory limit | Exp1 N=15: 6.5 (SD 3.7) pairs with letter names, 7.2 (SD 3.4) with noun names, p=0.45; Exp2 N=14; over half of errors were swapped bindings | Crichton 2021 (b01) | S, H |
| Human code-comprehension evidence is thin | 95 studies; 53.7% all-student | Wyrich 2023 (b05) | E |
| LLMs rely on names as beacons | CodeBERT code search MRR Java 70.36 to about 17.03, Python 68.17 to about 23.7 with all names anonymised; clone detection F1 94.87 to about 85 | Wang 2023 (a25, c10) | E (with a22, d11) |
| Small LLMs under misleading names | DS-R1-Qwen-7B L0 63.8, L1 64.2, L1b 51.8, L2 57.0, L3 56.2; SmolLM3-3B 45.0, 44, 34, 38, 33; 12 models 0.5B-8B | Le 2026 (a22) | S, O |
| Human experts did not lose under misleading names | humans 40.46 to 31.09 overall; expert row 40.48, 44.00, 55.56, 40.00, 37.50 (L0, L1, L1b, L2, L3); the 55.56 cell is a very small n | Le 2026 (a21, critique) | S, H (weak) |
| Larger 2025 chat models do not gain either | execution Pass@1 ClassEval original/misleading: GPT-4o 76.6/71.1, Qwen3-Coder 92.6/83.7, DeepSeek V3 90.0/88.8, Llama 4 81.1/80.8; LiveCodeBench GPT-4o 82.9/82.3, Qwen3-Coder 99.3/93.8, DeepSeek V3 99.3/97.2, Llama 4 80.2/75.5; summarisation GPT-4o 87.3 to 58.7 | Le 2025 (d11) | S, O |
| Reasoning-tuned small models track human task difficulty | Spearman: Phi-4 Mini 0.47, DS-R1-Qwen-7B 0.37, SmolLM3-3B 0.36, Qwen3-0.6B 0.30 (p<=0.003); Llama-3.1-8B 0.08, CodeLlama-7B 0.02, DS-Coder-6.7B 0.10 (n.s.); 50 undergraduates, 20 tasks | a21 | S, O |
| Longer CoT goes with lower accuracy (small models) | rho=-0.520 (p=1.11e-4); wrong answers not significantly longer after controls (p=0.33); low token limit hurts strong models OR=12.5 (CI 6.4-24.2) | a23 | S, O |
| LLM and human attention differ | 211 incorrect snippets, 57 (27%) explained by 5 patterns; 22 CS students (mean 5.62 years); SHAP focus matched human fixation in at most 22% of 68 Java methods | Kou 2024 (b06, c04), Li 2024 (b07) | E (2 sources) |
| Mutations that break data flow hurt code models | average modification effect up to 34%; some mutations fail over 20% of tasks | Hooda 2025 (b08) | S, O |
| Structure-aware chunks beat fixed chunks for code retrieval | RepoEval Pass@1 StarCoder2: GIST 57.9 vs 51.2, CodeSage 73.2 vs 67.6; Recall@5 BGE 69.8 vs 67.4, GIST 75.0 vs 70.7, CodeSage 83.9 vs 82.1; SWE-bench Lite Claude Pass@1 BGE 16.3 vs 13.7, CodeSage 16.7 vs 14.0, GIST 15.0 vs 14.7 | cAST (b09, c15) | E (with Glasz) |
| LLM partitions match experts best | MUMPS, ALC; 2,002 comments; 1.28M GPT-4o grading calls; ICC 0.960 and 0.908; docs "up to 20% more factual, up to 10% more useful"; MUMPS length effect rho=0.199 p=8.8e-10 | Glasz 2025 (a26, c02) | S (GPT-4o grader) |
| Gaze priors for training | EyeMulator gains in all 36 cells (+0.2% to +34.4%); EyeLayer Qwen3-1.7B BLEU-4 13.36 to 15.12; HumanLLM summarisation BLEU 5.36 to 10.32, completion CodeBLEU 5.42 to 4.77 (-0.65) | c05-c07 | C |
| Plan-first generation | Self-planning up to +25.4% relative; Structured CoT up to +13.79%; Parsel HumanEval 67 to 85%; CodeChain APPS GPT-3.5 22.33 to 30.24 (+35% relative) but modular CoT alone lowered results without revision | c17-c20 | C, O |
| Coarse-to-fine localisation | Agentless 32.00% (96 of 300) at $0.70; edit location 47.00 vs 50.67 when skipping a level (approximate) | c16 | S |
| Model-before-edit step helps an agent | ACQUIRE 66.4 to 70.8 Pass@1 (+4.4 pp), cost $0.055 to $0.073; single-hypothesis Proposal arm 66.0 (below baseline); FreeQ 67.0; 22 gained, 22 pass-to-fail regressions; rounds -7.1% | Lin 2026 (d01) | S |
| Exploration quality drives repair | restricted-context resolve rate: Oracle 59.7, CoSIL 59.3, Codex 50.3, Mini-SWE-Agent 50.0, TF-IDF 26.0, BM25 12.7, Random 4.7; context efficiency r=0.950 (about 13 explorers); resolve stays low until 50-75% of core regions present | SWE-Explore (d06) | S |
| Cheap explorers keep most of the signal | 78-94% of Hit@3; tokens down 84-95% | d07 | S |
| Agent trace signals predict outcome only moderately | 1,815 trajectories (47 tasks), AUROC 0.766, accuracy 72.0%; failing runs 58% more out-of-space inspections, 32% more cycles; no single signal significant; 10.7% of passing runs "Lucky" (0.5% Opus 4.5 to 23.2% GPT-4.1) | AgentLens (d09) | S |
| Early commitment is stability, not error | step-4 similarity vs variability r=-0.35; monitor AUROC 0.81; commit prompt cut variability 28% vs filler, no accuracy gain; vanishes on hard questions (QA) | d10 | S |
| Compact "chunked symbolic" reasoning | 74.36% fewer tokens, 82.30 vs 82.24 (Qwen-2.5-32B); CommonsenseQA 40.00 with Chunked Symbolism vs 84.60 with another paradigm | Sketch-of-Thought (c14) | S (not code) |
| Human chunk learner vs LLMs | HVM vs human recall time R=0.86 (training), 0.7 (transfer), N=112; LLMs transfer weakly | c11 | S |
| LLM difficulty is not human difficulty | AUROC 0.63 (human complexity metrics) vs 0.86 (shadow model) | d13 | S |
| LLM perplexity tracks human confusion on convention-breaking code | rho=0.47 confusing vs 0.05 clean; 1,432 usable EEG trials from 24 participants; effect size 0.42-0.45 | d12 | S |

## 4. Mechanisms and models

**4.1 Vessey's measurement, as code.** Everything here can be computed on an agent trace. Define a "debugging function" per trace segment (for an agent: orient/read, hypothesise, localise, edit, test, verify). Then:

1. `switches` = number of changes between debugging functions.
2. `top_returns` = number of returns to the top state (the agent's "start again / re-plan" state; in our schema, S1 or S2 after the first S3).
3. `loc_changes` = number of changes of location (file or function touched, compared with the previous action's location).
4. Add Vessey's secondary counts: `episodes` (maximal runs in one function), `modules_examined`, `re_examinations` of the faulty module, `hypotheses_stated`, `wrong_edits`.
5. Rank all runs on the three counts (adjust location counts for bug difficulty, as Vessey did for bug level). Vessey forced an 8 vs 8 split. Do not force a split. Use the counts as continuous predictors of solve rate.

Important: Vessey's expert label is derived from these counts. The counts cannot "predict" strategy without circularity. For the agent, the counts must be tested against an outside outcome (solve rate, wrong-patch rate) at equal tokens.

**4.2 Vessey's decision table, as code.** Two binary flags per run:
- `open_search` = the agent kept at least two candidate faults alive before its first edit (code check on the logged hypothesis list).
- `has_model` = the agent wrote a program model (what each module does, how control and data flow) before its first edit (code check for a model block).
Expert-like = both true. Vessey found this table matched the chunk class for 15 of 16 humans (a06). It is a test candidate, not a rule.

**4.3 Lock-in detector.** Vessey's "constrained" subject made edits driven by one early hypothesis and kept returning to it. Proxy: share of edits that target the location of the first-stated hypothesis, and count of consecutive edits with no new hypothesis. Shotgun mode: a run of edits with no stated reason. d10 warns that early stability is not error (a prompt that cut variability 28% gave no accuracy gain). A lock-in flag must be judged by solve rate, not by stability.

**4.4 Chunk store (memory), the engineering version.**
- Unit: function, class or AST subtree with a size cap (cAST uses a cap of 2000 non-whitespace characters, splitting on syntax-tree boundaries and merging small siblings).
- Retrieval: embed units; return whole units, never cut inside one.
- Chunk summary: one line per unit written by the model once and stored with the unit id. Glasz-style: partition by logical boundary, summarise per partition, then combine.
- Cost: tokens spent building summaries must be counted (G7).

**4.5 Template account.** Chase-Simon chunks have slots (CHREST "templates"). For the agent, a stored "plan" (for example accumulate-then-print-on-break) with named slots is a candidate memory object. Not tested. No evidence beyond human theory.

**4.6 Coarse-to-fine localisation.** Agentless: file, then class or function, then edit lines; each level pruned before the next. Skipping the middle level lowered edit-location accuracy by about 3.7 points (approximate). Implementation: three prompts, each shown only the candidates from the level above; code picks top-k; no agent loop.

**4.7 Model-first step (ACQUIRE).** Before any edit: generate targeted questions about the repo (about 70% were "mechanism" questions), answer them by reading code, store the answers as a knowledge block (232 audited QA pairs, 99.1% supported), then run the normal resolver with that block. The ablations matter: category-free questions gave 67.0, a single-hypothesis proposal gave 66.0, full gave 70.8.

**4.8 Debug process signals (AgentLens).** Out-of-known-good-space inspections (files outside the set touched by passing runs on that task), cyclic patterns (repeated action n-grams) and blind retries. Composite AUROC 0.766. Limit: the reference is built from passing runs.

**4.9 Beacon check.** Rename identifiers (consistently, behaviour preserving), or make them misleading, and see whether the answer changes. For an agent this is a diagnostic of name reliance, and a mutation test in the spirit of G3 (a pass must be on something the answer was not fitted to).

## 5. What holds up

**Holds up (two or more sources, consistent):**
- Identifier names act as beacons for code models. Removing or corrupting them costs accuracy (a25, a22, d11, b08). The size ranges from a few points (DeepSeek V3 execution 90.0 to 88.8) to large (summarisation GPT-4o 87.3 to 58.7; code search MRR 70.36 to about 17).
- Structure-aware chunking beats fixed-size chunking for code retrieval and documentation (b09, c15, a26). Gains are modest: +2.67 Pass@1 on SWE-bench Lite, +4.3 Recall@5 on RepoEval, up to +5.5 on StarCoder2 RepoEval.
- LLM attention is not human attention (b06, b07): at most 22% of Java methods show significant agreement.
- The human code-comprehension literature is mostly students and has no pooled expertise effect (b05, b10).

**Does not replicate or is missing:**
- No independent replication of Vessey 1985 (d14, d15, d03). The classification was never checked for reliability (a09). Absence in a limited search is not proof of absence.
- The expert gain under misleading names rests on one cell (55.56%, critique). It was not reproduced in 12 small models (a22) or in four 2025 large chat models (d11: changes from -0.3 to -8.9 points across eight cells, none above original).
- The gaze-prior literature is mixed: EyeMulator positive in all 36 cells, HumanLLM negative on completion (-0.65 CodeBLEU) (c05 vs c07). Different models and data.
- Plan-first prompting: gains reported by Self-planning and Structured CoT, but CodeChain found modular CoT alone lowered results without a revision step (c17 vs c18, c19). Most numbers are abstract-level "up to" values on older models and are not token-matched.
- Recall and beacon primaries (Shneiderman, McKeithen, Wiedenbeck, Adelson) were not opened; no numbers (b11-b16).

**Moderators and boundary conditions:**
- Task framing and notation: plan chunking vs control-flow chunking depends on the task and the language (K08; Detienne 1990).
- Expertise is cheap to claim: managers' ratings explained only 36.1% of variance in debug time. Years of programming correlated with task duration at r=0.330 in 216 programmers (b10).
- Hypothesis quality, not location, helped humans (OR 6.24 vs 1.4, d02). Experience in years gave OR 1.14 (p=0.04).
- Context length: a positive effect on comment accuracy in MUMPS (rho=0.199) but not in ALC, where full-file input scored lowest (a26).
- Chunked symbolic reasoning failed outside maths (c14).
- Human difficulty does not carry over: AUROC 0.63 vs 0.86 (d13). Only reasoning-tuned small models track human difficulty (rho 0.30-0.47), and 0.47 is a weak match.

**Interventions that worked:**
- Teaching a task-specific localisation procedure with worked examples: 20-44% to 80% (d05, students, N=44).
- Question-first model building for an agent: +4.4 pp (d01, one backbone, cost +33%).
- Structure-aware retrieval chunks (above).
- Coarse-to-fine localisation (Agentless; a design choice, not ablated against flat search).

**Interventions that did not work or backfired:**
- Single-hypothesis "proposal" before the edit: 66.0 vs baseline 66.4 (d01).
- Generic guidelines ("explore broadly"): 20-44%, no better than no instruction (d05).
- A commit-to-a-plan prompt: variability down 28%, accuracy unchanged (d10).
- A working-memory-tax prompt in small LLMs: negligible (a23).
- Attention maps as a design tool: weak alignment with programmers (b06; K16).
- Modular prompts alone, without revision (CodeChain).

## 6. Language models

**6.1 Do LLMs chunk like human experts?** The tests are indirect.

- Names. All models tested lose accuracy under obfuscation. Small models (0.5B-8B): best DS-R1-Qwen-7B 63.8 to 51.8 at misleading names; SmolLM3-3B 45 to 34 (a22). Larger 2025 chat models: modest execution drops (-0.3 to -8.9 points) and larger summarisation drops (GPT-4o 87.3 to 58.7; DeepSeek V3 87.7 to 76.7) (d11). Ambiguous names hurt more than misleading ones (DeepSeek V3 90.0 to 69.3; Llama 4 80.2 to 56.4).
- Human experts held or gained under misleading names (44.00 to 55.56 at L1b) while models did not. This is one small cell. No frontier reasoning model has been run on this task.
- Mutations. Breaking def-use chains costs code models up to 34% on average (b08).
- Memorisation check. GPT-4o repeated the original output on 13 ClassEval samples, but on only 2 under misleading names, so part of baseline accuracy is memorised (d11).
- Confusion. Qwen2.5-Coder-32B perplexity spikes where human EEG shows confusion on convention-breaking code (rho 0.47 vs 0.05) (d12). This is the nearest LLM analogue of the Soloway-Ehrlich cost. No study ran a direct convention-breaking test with a "report what the code says" metric (gap 4).
- Scrambled vs ordered recall (Shneiderman): no LLM study found (d16).

**6.2 Do LLM agents show Vessey's pattern?** No study tested it (K23; 300 citing titles screened). Related measured results:
- AgentLens (d09): failing runs inspect more files outside the known-good space (+58%) and loop more (+32%). No single signal was significant. 10.7% of passes were lucky.
- ACQUIRE (d01): building a model first raised Pass@1 by 4.4 pp on one backbone. The single-hypothesis arm fell below baseline. The direction fits Vessey (model plus open search), but cost rose 33% and the paper cites Vessey in discussion only.
- Early commitment (d10): measurable, but stability is not error.
- SWE-Explore (d06): the quality of what was explored explains repair (r=0.950 over about 13 explorers; resolve rate low until 50-75% of core regions are present).

**6.3 What changed LLM results, by how much.**

| Change | Effect | Source |
|---|---|---|
| Structure-aware vs fixed chunks | RepoEval StarCoder2 Pass@1 +5.6 to +6.7; SWE-bench Lite Claude Pass@1 +0.3 to +2.7 by retriever | c15 |
| Question-first model building | +4.4 pp at +33% cost | d01 |
| Hierarchical localisation, skipping one level | -3.7 points edit location (approx.) | c16 |
| Misleading names | -0.3 to -8.9 execution points (large chat); 63.8 to 51.8 (7B reasoning) | d11, a22 |
| Plan-first prompting | up to +25.4% relative (Self-planning), +13.79% (Structured CoT); older models | c18, c19 |
| System-2 prompt plus one example | lifted all small models; WM-tax prompt negligible | a23 |
| Gaze-prior fine-tuning | +0.2% to +34.4% relative (EyeMulator); -0.65 CodeBLEU on completion (HumanLLM) | c05, c07 |
| Compact chunked symbolic reasoning | -74% tokens at equal accuracy on maths; fails on commonsense | c14 |

**6.4 Cautions.**
- "Chunking" in LLM papers usually means retrieval units or compact prompts (K23).
- Glasz uses GPT-4o as judge; our schema distrusts model judges (G5, G8).
- Le 2026 covers models up to 8B only.
- Many numbers are abstract-level "up to" values on older models.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Chunk code context by structure, not by fixed lines.** Where the agent retrieves or stores code, cut at function or AST boundaries with a size cap, never inside a unit. Schema: M (retrieval) and S1 input. Status [E]. Evidence: b09, c15, a26 (K18). Gain: a few points; cost near zero. This is a design statement, not Vessey.
2. **Do not trust names as proof.** When a check depends on what code "does", verify behaviour by running it or by a behaviour-preserving rename. Names are beacons that can mislead. Schema: G3 (mutated input) and S4 TEST. Status [E]. Evidence: a25, a22, d11, b08 (K14). This extends G3 and adds no new state.
3. **Keep Vessey as a hypothesis.** Do not encode "breadth-first with system view" as a rule. Status [E] for the negative: K01, K13, K28. Nothing from this subfield enters SCHEMA.md except items 1 and 2, as notes on existing parts.
4. **Log the trace counts.** Cheap and passive: in the run log (SCHEMA section 6) record switches between states, returns to S1/S2 after S3, and location changes, per run. This changes no behaviour and supplies data for the tests below. Evidence: a02 (definition), d09 (signals). It is logging, not a claim.

### Test first (not established; nothing goes in until the test in UNKNOWNS.md passes)

| Item | Schema part | Status | Evidence ids | Test id |
|---|---|---|---|---|
| Force a program model (what the code does, flows) plus at least 2 candidate faults before the first edit | S2 REPRESENT for code tasks | [C] | a05, a06, d01, d02 (K04, K05, K26) | U1 |
| Revisit or switch cap (limit returns to the top state and location changes) | G2 / S6 | [S] | a04, d09, d10 (K03, K24, K25) | U2 |
| Trace metric from Vessey's three counts as an impasse or budget signal | S6 / G12 | [S] | a02, d09 (K24) | U3 |
| Hypotheses (not just locations) as the hint form for the patcher | S5 / S6 | [S] | d02 (K26) | U4 |
| Coarse-to-fine (hierarchical) localisation vs flat | S2 / S3 | [S] | c16, d06, d07 (K21) | U5 |
| Task-chosen code view (control flow vs data flow vs function) | S2 REPRESENT | [C] | a14, a15, b13 (K08) | U6 |
| Quote-the-line check on convention-breaking code | G2 / G3, S4 | [S] | a12, a13, d12 (K09) | U7 |
| Worked localisation example vs generic "explore broadly" | S1 / S2 prompt, M | [S] | d05 (K27) | U8 |
| Plan-first with revision vs direct, at equal tokens | S3 | [C] | c17-c20 (K20) | U9 |
| Model perplexity or retry counts as a hard-region flag | S0 / S6 | [C] | d12, d13 (K29) | U10 |
| Chunk summaries as memory (build once, retrieve whole units) | M | [S] | a26, c02 (K19) | U11 |
| Frontier models under misleading names | none (measurement) | [S] | a22, d11 (K15) | U12 |

## 8. Concrete tests on our bench

All tests run both arms at equal tokens (G7), with setup cost counted. Code is the grader (G5); no model judge. Report solve rate, wrong-patch rate and tokens. Use paired items, at least 60 per arm to see a 10-point effect, with a bootstrap interval.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| U1 model-first | held-out bug-fix items with unit tests | plain agent vs agent that writes a program model and lists at least 2 candidate faults before the first edit | solve rate; wrong-patch rate (patch that fails tests) | wrong-patch rate down; solve rate +2 to +5 pp (ACQUIRE gave +4.4 at +33% cost; here it must beat plain at the same tokens) |
| U1b ablation | same | model only; 2 faults only; both | same | both parts needed (Vessey 15 of 16); the single-hypothesis arm should not beat baseline (d01: 66.0 vs 66.4) |
| U2 revisit cap | same | no cap vs cap on returns to S1/S2 (for example 2) and on location changes | solve rate; tokens to solve | small gain or none; harm if the cap cuts needed exploration |
| U3 trace metric | all agent runs from our logs | none; metric computed after the fact | AUROC of solve vs counts; compare with token count alone | AUROC above 0.75 and above the token-only baseline |
| U4 hint type | bug items with oracle hints | no hint; location hint; hypothesis hint | solve rate | hypothesis hint beats location hint (humans: OR 6.24 vs 1.4) |
| U5 hierarchy | repo-localisation items | flat top-k vs file-then-function-then-lines | Hit@3 at equal tokens; solve rate | hierarchy better only if revisits fall; else context size is the cause |
| U6 view choice | mixed items (control flow, data flow, function purpose) | fixed view vs task-chosen view | accuracy per item type | task-chosen better on mixed types, no gain on single type |
| U7 convention-break | tracing items with a seeded convention-breaking line | plain vs required quote-the-line check | rate of reporting the conventional version | fewer plausible-fill errors with the quote check |
| U8 example form | localisation items | generic "explore broadly" vs problem-specific worked example vs none | localisation accuracy | worked example up (humans 20-44% to 80%); generic no better than none |
| U9 plan-first | held-out coding set | direct vs plan-first vs plan-first plus revision | pass@1 | gain only with revision (CodeChain) |
| U10 hard flag | all items | uniform budget vs budget by perplexity or retry flag | solved per token | gain if the flag predicts failure better than length |
| U11 chunk memory | long-context code tasks | fixed-line retrieval vs AST chunks vs AST chunks plus summaries | Pass@1 and tokens | AST beats fixed (+3 to +6); summaries pay only if build cost is below the saving |
| U12 names | execution-prediction items, original vs misleading names | frontier model, both name conditions; add a small human expert group if possible | accuracy gap | gap near zero for frontier reasoning models; if large, add a structure re-derivation step |

## 9. What does not transfer, and why

- **Vessey's expertise label.** It comes from human process counts on a 1980s COBOL batch program worked from printed listings (output listings, data division). Those categories do not exist in agent work.
- **Breadth-first vs depth-first as a trait.** In Vessey this was a coder's judgement of commitment to an early hypothesis (a05), not a measured search order. An agent's search is set by prompts and tools. Only a behaviour and its effect on solve rate make sense, not a trait.
- **Human working memory.** The 7-pair tracing limit (b01) and chunking as a cure for a short human store do not match a model's large context. A model's failure mode is attention dilution and plausible fill (K09, K29), not capacity. Human complexity metrics predicted LLM failure at AUROC 0.63 vs 0.86 for a shadow model (d13).
- **Expertise as years or rating.** An agent has no years. Its "expertise" is the class record (SCHEMA memory): the pass rate on similar items.
- **Neuroscience.** Small N, cross-sectional, no chunk-size measure (K10, K11). Not usable for design.
- **Gaze and attention.** LLM attention does not match programmers (b06, b07). Gaze priors are a training method, outside a scaffold (K17).
- **Retrieval "chunking".** Same word, different thing. It supports structure-aware units only.
- **Student samples.** Most human code studies use students (53.7%) and cannot speak for professionals.
- **Persona prompts.** "You are an expert programmer" is not a chunking intervention. It is the claimed-role style (manager rating, 36.1% of variance) rather than the process style (73.7%). G4 also bans persona voters on single-answer problems.

## 10. Open questions

1. Does a trace metric from Vessey's three counts predict solve rate at equal tokens, and does a revisit or switch cap help? (Partly: d09 gives AUROC 0.766 for other signals.)
2. Does a required program model plus at least 2 candidate faults before the first edit lower the wrong-patch rate at equal tokens? ACQUIRE is the nearest test (+4.4 pp, +33% cost, one backbone).
3. Do frontier reasoning models show the human-expert pattern under misleading names? How large must the expert human group be?
4. Do LLMs show the Shneiderman recall effect (coherent vs scrambled code) and the Soloway-Ehrlich cost? No study found.
5. Which chunk unit works best for agent context: function, AST node, control-flow block or data-flow slice?
6. Does hierarchical localisation help through fewer revisits or through smaller context?
7. Is there any independent replication of Vessey (larger N, second language, hard novel bugs)?
8. Can the Glasz LLM-chunk advantage be confirmed with a human or execution-based grader?
9. What are the primary effect sizes of the 1976-1986 recall and beacon studies?
10. Does a Chase-Simon template account (chunks with slots) improve what the agent stores as a memory chunk?
11. Is the 55.56% expert cell in Le 2026 real, given its very small n?
12. Why do human experts hold or gain under misleading names, and is this a structure-reading skill that a prompt can elicit?

## 11. Sources

Marker: [V] opened this session (page or PDF text read), [M] snippet, metadata or title only (no numbers cited). The list is generated from the evidence files; ids in brackets point to evidence lines.

- [V] Vessey (1985) Expertise in debugging computer programs: A process analysis. Int J Man-Machine Studies 23:459-494 (a01, a02, a03, a04, a05, a06, a07, a08, a09, a28) https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/vessey85.pdf
- [V] Detienne (1990) as above, reporting Shneiderman (1976) (a10, a11, a12, a13, a14, a15, a16, a27) https://arxiv.org/pdf/cs/0702003
- [V] Wyrich (2023) Source code comprehension: a contemporary definition and conceptual model (history section) (a17, a18) https://arxiv.org/pdf/2310.11301
- [V] Siegmund et al. (2017) Measuring neural efficiency of program comprehension. ESEC/FSE (a19, a20) https://www.se.cs.uni-saarland.de/publications/docs/SPP+17.pdf
- [V] Le, Nguyen, Nguyen (2026) Do machines struggle where humans do? LLM and human comprehension of obfuscated code (a21, a22, a23, c08) https://arxiv.org/abs/2606.31725
- [V] Kou, Chen, Wang, Ma, Zhang (2024) Do large language models pay similar attention like human programmers when generating code? Proc ACM Softw (a24) https://arxiv.org/pdf/2306.01220
- [V] Wang et al. (2023, v5 2024) How does naming affect LLMs on code analysis tasks? (a25) https://arxiv.org/pdf/2307.12488
- [V] Glasz et al. (2025) Can LLMs replace humans during code chunking? MITRE (a26) https://arxiv.org/pdf/2506.19897
- [V] Crichton, Agrawala, Hanrahan (2021) The Role of Working Memory in Program Tracing (b01) https://arxiv.org/abs/2101.06305
- [V] Ikutani et al. (2021) Expert Programmers Have Fine-Tuned Cortical Representations of Source Code (eNeuro) (b02) https://www.eneuro.org/content/eneuro/8/1/ENEURO.0405-20.2020.full.pdf
- [V] Kuo and Prat (2024) Computer programmers show distinct, expertise-dependent brain responses to violations in form and meaning (Sci Rep) (b03) https://pmc.ncbi.nlm.nih.gov/articles/PMC10914777/
- [V] Liu and Bedny (2025) Learning to Program Recycles Preexisting Frontoparietal Population Codes of Logical Algorithms (J Neurosci) (b04) https://pmc.ncbi.nlm.nih.gov/articles/PMC12590113/
- [V] Wyrich, Bogner, Wagner (2023) 40 Years of Designing Code Comprehension Experiments: A Systematic Mapping Study (b05) https://arxiv.org/abs/2206.11102
- [V] Kou et al. (2024) Do Large Language Models Pay Similar Attention Like Human Programmers When Generating Code? (FSE) (b06, c04) https://arxiv.org/abs/2306.01220
- [V] Li et al. (2024) Do Machines and Humans Focus on Similar Code? Explainability of LLMs in Code Summarization (b07) https://arxiv.org/abs/2402.14182
- [V] Hooda et al. (2025) Do Large Code Models Understand Programming Concepts? Counterfactual Analysis for Code Predicates (b08) https://arxiv.org/abs/2402.05980
- [V] Zhang et al. (2025) cAST: Enhancing Code RAG with Structural Chunking via Abstract Syntax Tree (b09, c15) https://arxiv.org/abs/2506.15655
- [V] Issever, Catalbas, Duran (2023) Examining Factors Influencing Cognitive Load of Computer Programmers (Brain Sci) (b10) https://pmc.ncbi.nlm.nih.gov/articles/PMC10452396/
- [M] Shneiderman (1976) Exploratory experiments in programmer behavior (b11) https://doi.org/10.1007/BF00978316
- [M] McKeithen, Reitman, Rueter, Hirtle (1981) Knowledge organization and skill differences in computer programmers (b12) https://doi.org/10.1016/0010-0285(81)90013-5
- [M] Adelson (1981, 1984) Problem solving and the development of abstract categories in programming languages / When novices surpass experts (b13) https://doi.org/10.3758/BF03197118
- [M] Wiedenbeck (1986) Beacons in computer program comprehension (b14) https://doi.org/10.1016/S0020-7373(86)80083-9
- [M] Gilmore and Green (1984) Programming plans and programming expertise (b15) https://doi.org/10.1080/14640748408402107
- [M] Barfield (1986) Expert-novice differences for software: implications for problem-solving and knowledge acquisition (b16) https://doi.org/10.1080/01449298608914515
- [V] Vessey (1985) Expertise in debugging computer programs: a process analysis (IJMMS) (b17, c01) https://doi.org/10.1016/S0020-7373(85)80054-7
- [M] Chase and Simon (1973) Perception in chess (b18) https://doi.org/10.1016/0010-0285(73)90004-2
- [M] Gobet and Simon (1996) Recall of rapidly presented random chess positions is a function of skill (b19) https://doi.org/10.3758/BF03213951
- [M] Busjahn et al. (2015) Eye Movements in Code Reading: Relaxing the Linear Order (ICPC) (b20) https://doi.org/10.1109/icpc.2015.36
- [M] Peitek, Siegmund, Apel (2020) What Drives the Reading Order of Programmers? An Eye Tracking Study (ICPC) (b21) https://doi.org/10.1145/3387904.3389279
- [M] Bauer, Siegmund et al. (2019) Indentation: Simply a Matter of Style or Support for Program Comprehension? (ICPC) (b22) https://doi.org/10.1109/icpc.2019.00033
- [M] Fucci et al. (2019) A Replication Study on Code Comprehension and Expertise using Lightweight Biometric Sensors (ICPC) (b23) https://doi.org/10.1109/icpc.2019.00050
- [M] Castel et al. (2003) Experts sometimes show more false recall than novices: a cost of knowing too much (b24) https://doi.org/10.1016/s1041-6080(03)00018-9
- [M] Gobet et al. (2001) Chunking mechanisms in human learning (Trends Cogn Sci) (b25) https://doi.org/10.1016/S1364-6613(00)01662-4
- [V] Glasz et al. (2025) Can LLMs Replace Humans During Code Chunking? (c02, c03) https://arxiv.org/abs/2506.19897
- [V] Zhang et al. (2025) EyeMulator: Improving Code Language Models by Mimicking Human Visual Attention (c05) https://arxiv.org/abs/2508.16771
- [V] EyeLayer (2026, ICPC) gaze priors for LLM code summarisation (c06) https://arxiv.org/abs/2602.22368
- [V] HumanLLM (2025) Enhancing Code LLM Training with Programmer Attention (c07) https://arxiv.org/abs/2503.14936
- [V] Rong et al. (2026) On Behavioral Alignment of Model-Code and Human-Code Understandability via Behavioral Proxies (c09) https://arxiv.org/abs/2609.26101
- [V] Wang et al. (2024) How Does Naming Affect LLMs on Code Analysis Tasks? (c10) https://arxiv.org/abs/2307.12488
- [V] Wu, Thalmann, Dayan, Akata, Schulz (2025, ICLR) Building, Reusing, and Generalizing Abstract Representations from Concrete Sequences (c11) https://arxiv.org/abs/2410.21332
- [V] Wu, Alaniz, Schulz, Akata (2025) Discovering Chunks in Neural Embeddings for Interpretability (c12) https://arxiv.org/abs/2502.01803
- [V] Yu (2025) Adaptive Token Boundaries: Integrating Human Chunking Mechanisms into Multimodal LLMs (c13) https://arxiv.org/abs/2505.04637
- [V] Aytes, Baek, Hwang (2025) Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching (c14) https://arxiv.org/abs/2503.05179
- [V] Xia et al. (2024) Agentless: Demystifying LLM-based Software Engineering Agents (c16) https://arxiv.org/abs/2407.01489
- [V] Le et al. (2024, ICLR) CodeChain: Modular Code Generation through Chain of Self-revisions with Representative Sub-modules (c17) https://arxiv.org/abs/2310.08992
- [V] Jiang et al. (2023) Self-planning Code Generation with Large Language Models (c18) https://arxiv.org/abs/2303.06689
- [V] Li et al. (2023) Structured Chain-of-Thought Prompting for Code Generation (c19) https://arxiv.org/abs/2305.06599
- [V] Zelikman et al. (2023) Parsel: Algorithmic Reasoning with Language Models by Composing Decompositions (c20) https://arxiv.org/abs/2212.10561
- [M] Concept-Guided Interpretability via Neural Chunking (2025; seen in a title list, not opened) (c21) https://arxiv.org/abs/2505.11576
- [M] Yang et al. (2024) SWE-agent: Agent-Computer Interfaces (recalled, not opened) (c22) https://arxiv.org/abs/2405.15793
- [M] Adelson (1981, 1984) problem solving and abstract categories in programming (search snippet only) (c23) https://doi.org/10.3758/BF03197722
- [M] McKeithen, Reitman, Rueter, Hirtle (1981) Knowledge organization and skill differences in computer programmers (search snippet only) (c24) https://doi.org/10.1016/0010-0285(81)90012-2
- [M] CHREST computational chunk model of expert recall (search snippet only) (c25) https://www.chrest.info/
- [M] Johnson and Soloway (1985) PROUST; Rich and Waters (1990) Programmer's Apprentice (recalled, not opened) (c26) https://doi.org/10.1109/TSE.1985.231854
- [V] Lin et al. (2026) Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution (ACQUIRE) (d01) https://arxiv.org/abs/2607.11111
- [V] Alaboudi and LaToza (2020) Using Hypotheses as a Debugging Aid (VL/HCC) (d02) https://arxiv.org/abs/2005.13652
- [V] Alaboudi and LaToza (2021) An Exploratory Study of Debugging Episodes (d03) https://arxiv.org/abs/2105.02162
- [V] Li and Coblenz (2026) A Grounded Theory of Debugging in Professional Software Engineering Practice (FSE) (d04) https://arxiv.org/abs/2602.11435
- [V] Zhang, Roy and Arnaoudova (2025) Context-Specific Instruction: A Longitudinal Study on Debugging Skill Acquisition and Retention for Novice  (d05) https://arxiv.org/abs/2509.22420
- [V] Zhang et al. (2026) SWE-Explore: Benchmarking How Coding Agents Explore Repositories (d06) https://arxiv.org/abs/2606.07297
- [V] Al Awad and Ivanov (2026) Cost-Effective Repository Exploration for Agentic Issue Localization (d07) https://arxiv.org/abs/2608.29675
- [V] Oderinwale (2026) Agent trajectories as programs: fingerprinting and programming coding-agent behavior (ProcGrep) (d08) https://arxiv.org/abs/2606.16988
- [V] Sahoo et al. (2026) AgentLens: Revealing The Lucky Pass Problem in SWE-Agent Evaluation (d09) https://arxiv.org/abs/2605.12925
- [V] Mehta and Datta (2026) When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents (d10) https://arxiv.org/abs/2606.22936
- [V] Le et al. (2025) When Names Disappear: Revealing What LLMs Actually Understand About Code (d11) https://arxiv.org/abs/2510.03178
- [V] Abdelsalam et al. (2025) How do Humans and LLMs Process Confusing Code? (d12) https://arxiv.org/abs/2508.18547
- [V] Machtle et al. (2026) Beyond Accuracy: Characterizing Code Comprehension Capabilities in (Large) Language Models (d13) https://arxiv.org/abs/2601.12951
- [V] Citation scan of Vessey (1985) and Vessey (1986) via Semantic Scholar and Crossref (d14) https://api.crossref.org/works/10.1109/tsmc.1986.289308
- [M] Crossref metadata for founding recall and beacon studies: Shneiderman (1976); McKeithen et al. (1981); Wiedenbeck (1986); Soloway and Ehrlic (d15) https://api.crossref.org/works?query.bibliographic=Shneiderman+Exploratory+experiments+in+programmer+behavior
- [V] Search log for gaps 3, 4, 8 and 10 (HuggingFace papers index queries, 2026-11-03) (d16) https://huggingface.co/api/papers/search?q=shuffled+code+LLM+comprehension

Cited only through secondary reviews [M]: Brooks (1977), Soloway and Ehrlich (1984), Rist (1986), Pennington (1987), Norcio (1986), Gugerty and Olson (1986), Katz and Anderson (1987); see a09, a13-a16, d03.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.02-K13** (reworded: the sources support less). Wyrich et al. support 53.7% all-student of 95 and that almost no studies link design to comprehension theory in general, but say nothing specific on chunking or on pooled effect sizes for expertise; Issever et al. (EMIP reanalysis) does not address either, so the 'no pooled effect size' absence claim is unsupported (second source not opened for relevance, being off-topic). Corrected claim: Of 95 code-comprehension experiments (1979-2019), 53.7% used all-student samples, and almost none linked their design to a comprehension theory (Wyrich et al. 2023); whether a pooled effect size exists for the expertise effect was not established by these sources.
- **A20.02-K18** (number corrected). cAST numbers confirmed; but Glasz et al. report LLM partitions beat all methods except Single Module (which aligned best with experts, near-perfect recall on MUMPS), and the least factual comments came from Single Module chunking (most limited context), not fixed-length chunking; fixed-length chunks merely had minimal overlap with expert split points. Corrected claim: Structure-aware chunking beats fixed-size chunking in code RAG: cAST (RepoEval Pass@1 StarCoder2 GIST 57.9 vs 51.2; SWE-bench Lite Claude-3.7 BGE 16.3 vs 13.7, GIST 15.0 vs 14.7). In Glasz et al. (legacy MUMPS/ALC), LLM-chosen partitions matched expert partition points better than all other methods except single-module (subroutine) chunking, fixed-length chunks had minimal overlap with expert partitions, and single-module chunking, with the least context, gave the least factual comments.
