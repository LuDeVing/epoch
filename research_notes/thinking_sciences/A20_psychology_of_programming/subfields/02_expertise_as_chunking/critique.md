# Critique: A20.02 Expertise as chunking (cross-check)

## Numbers re-opened this session (PDF text read)
Confirmed with no change:
- Vessey 1985 (a03): 73.7% vs 36.1% of variance in debug time; 15 min 40 s vs 28 min 3 s; 20 min 24 s vs 23 min 19 s; agreement 10 of 16; all five incorrect-change makers were novices by chunk class. R2 = 0.737 also confirmed.
- Le et al. 2026 (a22, c08): DS-R1-Qwen-7B L0 63.8, L1 64.2, L1b 51.8, L2 57.0, L3 56.2; SmolLM3-3B 45.0 to 33.0; Phi-4 Mini rho 0.47; OR 12.5 (CI 6.4-24.2); humans 40.46 to 31.09 overall; expert row 40.48, 44.00, 55.56, 40.00, 37.50.
- Kou et al. 2024 (a24, b06, c04): 211 incorrect snippets, 27%, 22 participants, mean 5.62 years, property keywords 45.2%.
- cAST (b09, c15): RepoEval StarCoder2 Pass@1 GIST 57.9 vs 51.2; CodeSage 73.2 vs 67.6; SWE-bench Claude Pass@1 BGE 16.3 vs 13.7, CodeSage 16.7 vs 14.0, GIST 15.0 vs 14.7; RepoEval Recall BGE 69.8 vs 67.4, GIST 75.0 vs 70.7, CodeSage 83.9 vs 82.1.
- Glasz et al. 2025 (a26, c02): ICC 0.960 and 0.908; 2,002 comments; 1.28M requests; "up to 20% more factual, up to 10% more useful".
- Ikutani 2021 (b02): r=0.593 p=0.0059 n=20; r=0.722 p=0.000007 n=30; accuracy 76.0 (SD 13.5); rating mean 954.3 (SD 864.6).
- Crichton 2021 (b01): 6.5 (SD 3.7) letters, 7.2 (SD 3.4) nouns, p=0.45.
- Sketch-of-Thought (c14): 82.30 vs 82.24, 74.36% fewer tokens.

## Corrections and fill-ins
1. c03 had no coefficient for the MUMPS context-length effect. Glasz prints rho = 0.199, p = 8.80e-10 (a26 was right). Note that p is very small with a weak rho, which means a large sample of comments (not a strong effect).
2. a24 calls the 22 raters "programmers"; Kou says they were 22 CS-department students (18 male, 4 female). Treat as students.
3. The human expert result in Le (expert accuracy 55.56% at L1b) is a single cell. The paper gives no per-cell n in the text I read, and 55.56 = 5/9 or 10/18 style fractions suggest very few expert answers. a21/a22 say humans "peaked at L1b" for experts; true for the expert row only. The beginner and intermediate rows fall at L1b (26.32, 37.50). Weight this claim as weak.
4. a22 says "Instruct models showed a sensitivity peak at L1b under System-2 prompting". Confirmed in text, but the same paper says S2 prompting slightly reduces accuracy at L1b for some models, so the direction is mixed.
5. a06/a07 are consistent: the 15 of 16 match is between two author-defined measures on the same 16 people.
6. K07 and K08 (recall and plan evidence) rest only on second-hand reviews (a10-a15, b11-b16). Their "opened:true" flags in a13-a15 refer to the Detienne review text, not the primaries. Treat all numbers there as absent.

## Contradictions between sources
- Vessey's abstract reads as "experts breadth-first, novices depth-first". The text has two novice types (breadth-first without a system model, and depth-first). a07 is right; b17 and c01 use the simplified wording.
- Plan/function chunking (Adelson, Rist, Soloway) vs control-flow chunking (Pennington, Shneiderman and Mayer): not resolved; Detienne 1990 says neither side was tested with strong controls (a16, a14).
- Gaze-prior fine-tuning: EyeMulator reports gains in all 36 cells, HumanLLM reports a loss on completion (-0.65 CodeBLEU) and gains only on summarisation (c05 vs c07). Different models, different data, so no clean comparison.
- Plan-first prompting: Self-planning and Structured CoT report gains; CodeChain says modular CoT alone lowered performance without revision (c17 vs c18/c19).
- The Le paper says reasoning-tuned small models align with human difficulty, but the best aligned (Phi-4 Mini rho 0.47) is a weak match; the same paper finds longer CoT goes with lower accuracy, and no significant gap for wrong answers after controls.

## Weak spots
- The founding study is N=16, one COBOL program, one firm, classification partly circular. No replication of Vessey's propositions was found in this series. This is a hypothesis, as the repo note says.
- Nearly every "chunking" LLM paper (cAST, Glasz, EyeMulator, Sketch-of-Thought) uses the word for retrieval units, tokenisation, or compact prompts. They do not test Vessey's idea. They support only a weaker design statement: structure-aware units beat fixed units.
- Several top-down results (Self-planning, Structured CoT, Parsel, EyeLayer, Agentless) are abstract-level or "up to" numbers on older models; none controls for tokens.
- Glasz uses GPT-4o as grader, which our schema says to distrust.
- Le et al. covers only models up to 8B; the question for a frontier agent is open.
- Cross-sectional neuroscience (b02-b04, a19) has small N and no chunk-size measure.

## Only seen in snippets or titles (do not cite numbers)
c21, c22, c23 (3.5 vs 2.4 chunk size is a secondary snippet), c24, c25, c26, b11-b16, b18-b25, a10-a12.

## GAPS (most decision-relevant first)
1. Does an agent trace metric built from Vessey's three counts (mode switches, returns to the top state, location changes) predict solve rate at equal tokens, and does a revisit or switch cap help?
2. Does forcing a "list at least two candidate faults plus build a program model before the first edit" step lower wrong-patch rate versus a plain agent at equal tokens on a held-out bug set?
3. Do frontier LLMs show the expert pattern under misleading names (accuracy rises or holds at L1b) that Le found in humans but not in 0.5B-8B models? With what expert sample size?
4. Do LLMs show the Shneiderman recall effect (coherent vs scrambled code) and the Soloway-Ehrlich cost (convention-breaking code mis-read as the conventional version)? No LLM study was found.
5. Which chunk unit (function, AST node, control-flow block, data-flow slice) gives the best context for an agent on bug localisation at equal tokens? cAST and Glasz test only fixed vs structure-aware.
6. Is there any independent replication of Vessey (1985) with a larger sample, a second language, or hard novel bugs? Searches here were limited by rate limits.
7. Is hierarchical coarse-to-fine localisation (Agentless style) better than flat search because of fewer revisits, or only because of smaller context?
8. Can the GPT-4o-graded advantage of LLM partitions (Glasz) be confirmed with human or execution-based grading?
9. What are the primary numbers of the 1976-1986 recall and beacon studies (Shneiderman, McKeithen, Wiedenbeck, Adelson), so the effect size can be stated?
10. Does the Chase-Simon template account (chunks plus links) change what an agent should store as a "chunk" in memory?

## Gap search results (2026-11-03, evidence_d.jsonl d01-d16)
Search limits: WebSearch budget was spent by other agents, the arXiv API returned empty bodies, OpenAlex was rate-limited. Used Semantic Scholar citations, Crossref, the HuggingFace papers index and direct PDF reads (11 PDFs opened).

Partly closed:
- Gap 1 (trace metric): partly. AgentLens (d09) shows process signals (out-of-space inspection, cycles, blind retries) separate pass from fail at AUROC 0.766, but no single signal is significant, references are built from passing runs, and nothing is token-matched. No test of Vessey's three counts and no revisit-cap intervention. Mehta and Datta (d10) warn that early stability is not error. Still open as an experiment.
- Gap 2 (model-before-edit step): partly. ACQUIRE (d01) gives 66.4 to 70.8 Pass@1 (+4.4 pp) with a question-first stage, +33% cost, one backbone; a single-hypothesis proposal arm fell to 66.0, below baseline. Human data (d02) say a correct early hypothesis matters (OR 6.24) and fault locations alone do not (OR 1.4). No token-matched test on a held-out bug set.
- Gap 3 (frontier models under misleading names): partly. 2025 large chat models (d11) never gained under misleading names (changes of -0.3 to -8.9 points on execution Pass@1). No reasoning-tuned 2026 model and no larger human expert sample was found.
- Gap 5 and 7 (chunk unit, hierarchy): partly. SWE-Explore (d06) shows coverage plus compactness drive repair, with a threshold at 50-75% of core regions; d07 shows cheap explorers keep 78-94% of Hit@3. No comparison of function vs AST vs flow-block vs slice, and no flat-vs-hierarchical ablation.

Stayed open:
- Gap 4 (LLM recall effect, Soloway-Ehrlich cost): no study found (d16). Only a partial analogue: perplexity spikes track human confusion on convention-breaking code, rho 0.47 vs 0.05 (d12).
- Gap 6 (replication of Vessey): none found in 300 citing titles (d15); the behaviour-study table lists Vessey at N=16 (d03); Li and Coblenz 2026 (d04) agree conceptually only. Gugerty and Olson (N=44) and Katz and Anderson (N=77) texts were not opened.
- Gap 8 (human or execution grading of Glasz): not found.
- Gap 9 (primary numbers of the 1976-1986 recall and beacon studies): only Crossref metadata (d14, opened:false). Do not cite numbers.
- Gap 10 (template account for memory chunks): not found.

New caution from this pass: d13 (AUROC 0.63 vs 0.86) says human-style complexity is a weak predictor of LLM difficulty, so human chunk theory should not be copied into the agent without a model-specific check.
Claims changed: K04 to contested, K15, K21 and K23 extended; K24-K29 added (claims.jsonl now 29 lines).
