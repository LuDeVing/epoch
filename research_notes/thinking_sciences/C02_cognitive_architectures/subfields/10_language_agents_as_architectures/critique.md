# Critique, C02.10 Language agents as architectures

## Corrections made
Re-opened: Reflexion, Huang et al., Voyager, MemGPT, ReAct, ToT, Generative Agents, Zhu and Simmons, Fan and Lan.

1. b12 and c12 are wrong. In Reflexion Table 1 the 77.1 vs 80.1 pair is MBPP Python (matches Table 2: 0.80 to 0.77), not Leetcode Hard. Leetcode Hard Python is 7.5 (GPT-4) vs 15.0 (Reflexion). a14 had it right. The PDF text rows are offset.
2. b13 and c15 misread the oracle table of Huang et al. Table 2: GPT-3.5 standard 75.9/75.8/26.0 (GSM8K/CSQA/HotpotQA); GPT-3.5 oracle 84.3/89.7/29.0; GPT-4 standard 95.5/82.0/49.0; GPT-4 oracle 97.5/85.5/59.0. So "GPT-3.5 oracle 95.5 and 49.0" and "GPT-4 HotpotQA 29.0 to 59.0" are wrong; 95.5/49.0 are GPT-4 baselines. Oracle gain is modest for GPT-3.5 (+8.4 GSM8K, +3 HotpotQA) and +2.0 GSM8K, +10.0 HotpotQA for GPT-4. Intrinsic numbers confirmed (75.9, 75.1, 74.7; CSQA 75.8, 38.1, 41.8; GPT-4 GSM8K 95.5, 91.5, 89.0; HotpotQA 49, 49, 43).
3. Confirmed: MemGPT DMR; Voyager (3.3x, 15.3x/8.5x/6.4x, 2.3x, -93%, -73%, 5.7x); ReAct (71%, 33-90%, mean 62%, HotpotQA 27.4 vs CoT 29.4 vs CoT-SC 33.4, FEVER 64.6); ToT (7.3, 4.0, 9.0, 45, 74); Generative Agents (29.89, 26.88, 25.64, 22.95, 21.21, d=8.16, chi2(4)=150.29); Reflexion Rust 52/60/68; Zhu and Simmons 14/15 vs 15/15, p 0.446 and 0.347, 120 vs under 40 dollars.
4. Zhu and Simmons token column is garbled in the PDF text (rows misaligned; one row seems to show bootstrapped tokens above action-only). Only the cost sentence is reliable.
5. Fan and Lan: ten architectures, no inter-rater claim, no PRISMA or causal claim, corpus frozen 26 Jul 2026 confirmed. "42 systems" and "company authors group" (c05) not re-checked.

## Contradictions and weak spots
- Reflexion reports gains (+22, +20, +11) yet loses on MBPP Python; Huang et al. say intrinsic self-correction fails. Reconciled only by "reliable external signal", but Reflexion's HotpotQA setup used ground-truth correctness, so that gain is partly an oracle gain.
- Kamoi et al. is a survey; it is not independent measurement beyond Huang.
- Kirk/Wray/Laird papers share authors; STARS and Wray results are one group. NL2GenSym is one group on its own benchmark.
- The central source (Fan and Lan) is one preprint, one coder, no experiment. Every gap is a hypothesis.
- No study here compares a Soar/ACT-R-style scaffold with plain CoT or best-of-N at equal tokens. ToT, LATS and Voyager use many more calls.
- Generative Agents and MemGPT measure believability and a self-built retrieval task, not reasoning gain.
- Voyager baselines were re-interpreted by the authors; 3 runs each.

## Only seen in snippets or not opened
c24 (Always-On Agents survey), c25 (Joshi and Ustun), a26 Newell 1990, a27 chunking 1986, a28 ACT-R 2004 (no founding numbers such as activation equation or chunking speed-up). Assanie 2022 unread. Memory-R1, AWM, ADAS, LATS, NL2GenSym, STARS and LLM-ACTR numbers were not re-opened this pass.

## GAPS
1. Does a typed impasse trigger with a scoped sub-call (Soar style) beat plain retry or reflection at equal tokens on reasoning tasks? No measurement exists.
2. Does a commit/reconsider step in a ReAct-like loop improve outcomes at equal tokens (Wray et al. open question)?
3. How reliable must a check be before reflection helps? Find the false-positive-rate threshold (Reflexion MBPP 16.3% vs 1.4%) with current reasoning models.
4. Does intrinsic self-correction still fail on 2025-2026 reasoning models, and with which verifier types does it recover?
5. Does chunking-style caching of verified solutions pay back at equal total tokens when reuse conditions are code-checked? Soar chunking speed-up data (Laird 1986) is unread.
6. What are ACT-R's activation equation and fit numbers (Anderson 2004), and does recency/frequency/context retrieval beat plain similarity retrieval in agent memory at equal tokens?
7. Is there an independent recoding of Fan and Lan's D3/D4 ratings, and do other 2025-2026 agent-architecture surveys agree on the residual gaps?
8. Does ToT/LATS-style search keep its edge over best-of-N at the same call budget on non-puzzle tasks?
9. Does the Soar-group finding that omitted search control costs orders of magnitude more steps carry over to prompt scaffolds (specs with versus without search control)?

## Gap search results

Limits of this pass: web search budget ran out on the first query, and arXiv/Semantic Scholar/OpenAlex APIs returned HTTP 429. Evidence came from direct fetches of 19 arXiv HTML pages (read through a fetch summariser, not full-text reading; long pages were cut at 100000 characters). Evidence lines are d01 to d20 (d04 is not opened). (C: ran out of space mid-pass; files were staged in D:/research_scratch/C02.10 and copied here afterwards.)

1. Typed impasse trigger vs plain retry at equal tokens: OPEN. No study found. Nearest equal-budget evidence: Wang et al. (d10) shows self-consistency beats Reflexion, debate and ToT at 20 queries; Snell et al. (d14) shows difficulty-aware allocation matches best-of-N with up to 4 times less compute.
2. Commit/reconsider step in a ReAct loop: OPEN. Nearest: bounded "Wait" continuation gives AIME24 50.0 to 56.7 and then flattens (d16).
3. How reliable must a check be: PARTLY CLOSED. Rough break-even is 60 to 70% error-finding accuracy (Tyen, d03, from a simulation figure); best 2023 LLM finder 52.87%. Stechly (d01) gives verifier false-positive/negative rates (G24 10.4/20.7; coloring 6.5/95.8) and shows a sound verifier is what lifts results. No measurement with current reasoning models. Reflexion's 16.3% vs 1.4% false-positive contrast is still the only matched pair on code.
4. Intrinsic self-correction on 2025-2026 reasoning models: PARTLY CLOSED, indirectly. Tsui (d05) finds a near-zero blind spot in R1-style models and big gains from "Wait" on V3; Liu et al. (d06) show reflection words do not imply accuracy. SCoRe (d07) independently confirms the old prompt-only failure (-11.2 on MATH). No direct replication of Huang et al. on reasoning models found. Verifier types that recover: code run, sound planner/verifier (d01), tools (d09).
5. Chunking-style caching payback at equal total tokens: OPEN. ExpeL (d19) shows training-free reuse works (ALFWorld 40 to 59) but without total-token accounting. Laird 1986 data not reachable.
6. ACT-R activation equation and recency/frequency retrieval vs similarity: OPEN for the equation (Anderson 2004 not read). For the comparison: no ACT-R-style arm found; BM25 beats an embedding model and long context beats agentic memory (d17); Mem0 trades 6 J-points for about 15 times fewer tokens (d18).
7. Independent recoding of Fan and Lan / other surveys: OPEN. The 48-author survey (d20) was only skimmed, no Soar/ACT-R mapping seen.
8. ToT/LATS vs best-of-N at the same call budget off puzzles: PARTLY CLOSED, answer leans no edge. SC beats ToT/Reflexion/debate at matched budget (d10); MCTS below sampling at equal FLOPs (d13); web search beats reranking but at up to 20 times the calls (d12); LATS has no equal-budget best-of-N arm (d11).
9. Omitted search control in prompt scaffolds: OPEN. No study found.

Claims changed: K03 to established (3 independent sources); K08 to contested; K02 evidence extended; K04, K06, K09, K11, K14, K15 notes added. New claims K17 to K22.
