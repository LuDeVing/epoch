# Critique and cross-check: C08.08 Retention policy

## Sources re-opened (PDF text, this session) and checked
- CASCADE 2605.06702: 66.68 / 48.33 / 63.76 / 66.37 / 63.95 / 65.39 / 65.49 confirmed (table at line ~1895). Abstract text "improves macro-averaged success rate by 20.9% over zero-shot" confirmed.
- Xiong et al. 2505.16067 Table 1: all fixed / add-all / C1-C3 / strict numbers for 4 agents confirmed.
- Memento 2508.16153: GAIA 87.88 Pass@3 val, 79.40 test, K sweep (59.9/72.2 ... 64.5/78.5 ... 63.9/78.1), learning curves 78.65-84.47 and 80.46-85.44 confirmed.
- Smyth and Keane 1995: 50 cases, 160 targets, limit 75 (reached after 25 trials), 80% utility and 86% random, FD/FUD 100% confirmed.
- Dynamic Cheatsheet 2504.07952: AIME 2024 23.3 baseline, 26.7 full history, 50.0 DC confirmed.
- ReasoningBank 2509.25140: 40.6 to 41.7, 44.4 to 42.2, 46.5 to 49.7, judge accuracy 70-90% flat confirmed verbatim.
- Sarukkai 2505.00234: ALFWorld 73 to 89 to 93, AUROC 0.77 confirmed.

## Corrections
1. b16 names the Memento authors as Wang et al.; the first authors are Zhou and Chen (a20 and c21 are right).
2. CASCADE "20.9%" is not defined in the text I read as relative or absolute. On the 12-task Qwen3-32B table the absolute gain is 18.35 points (66.68 vs 48.33) and relative 38%. The 20.9 is over 16 tasks; do not quote it as either until checked.
3. Xiong EHRAgent coarse C1 is 26.19 in Table 1 but 25.91 in the Table 2 block; strict is 38.50 vs 38.67. Small run-to-run or rounding gaps; use Table 1 for addition, Table 2 for deletion.
4. a02/a03 are right on assignment (utility 80, random 86); b-file and a-file agree.
5. c11: ReasoningBank 46.5 is its success-only score and 49.7 with failures (confirmed). Do not confuse with the Synapse 46.5 in the Gemini-pro table.
6. Memento's reported deltas (a22) are one ablation step not identified; treat "-18.0 F1" as unlocated.

## Contradictions
- Judge noise: Xiong says coarse judges lose to strict ones and sometimes to fixed memory; ReasoningBank says 70-90% judge accuracy barely matters. Likely explanation: ReasoningBank stores distilled strategies, Xiong stores raw executions. Untested.
- Failures: CASCADE discards them (and says so as a limit); Memento, ExpeL, ReasoningBank, Evo-Memory keep them. Only ReasoningBank ablates directly; no study compares success-only vs both in one retrieval setup.
- Consolidation: Zhang 2026 says rewriting hurts; Dynamic Cheatsheet, ReMe and ReasoningBank rely on rewriting/distillation and gain. Format and model strength differ.
- Deletion: Smyth and Keane footprint deletion (100%) vs Pan 2005 (pivotal rule keeps noisy outliers). Different noise levels; no LLM test.

## Weak spots
- No study ablates the retention rule alone, with retrieval and model fixed. CASCADE has no "retain all" or "retain novel" arm in the main run (its always-retain test uses ground truth).
- Most deletion/addition evidence is on small agents (RegAgent, EHRAgent), short streams (about 1000-4000 records), single task families.
- Zhang et al. 2026 (b14, b15): marked opened by the earlier agent; my arXiv title search did not find it and I did not re-open it. Its ARC-AGI 54% figure is unconfirmed here.
- The Smyth-Keane results are one run per policy, on a toy valuation domain with nearest-neighbour retrieval.
- Aha 1991, Minton 1990, Racine and Yang, Leake and Wilson: not opened (a05, a27, b23-b25, c25, c26 are memory only).
- Evo-Memory, ExpHarness, dual-memory, Self-Consolidation, ReMe row mapping: seen at figure/summary level; per-variant numbers not read.
- Mixed-source ceilings: AWM, Voyager use environment or code checks as the gate; we may not have that on open reasoning.

## GAPS
1. At equal tokens and fixed retrieval, which write gate wins for a frozen LLM on reasoning tasks: add-all, success-only, novelty-only (uncovered by nearest case), or success plus failure lessons?
2. What judge accuracy is needed before a self-judged write gate beats a fixed seed memory, for raw-trace vs distilled-strategy storage? (Resolves Xiong vs ReasoningBank.)
3. Does a novelty gate (store only when no stored case solves it) replicate Yang and Zhu's coverage efficiency with LLM agents, and at what bank size does it saturate?
4. How fast does a success-only bank decay on a long stream (over 1000 tasks) with distribution shift, and does capped deletion by later-use utility prevent it? (CASCADE and Memento leave this untested.)
5. Do failed attempts stored as one-line lessons add anything over success-only retention, controlling for token cost? (Only ReasoningBank tests this.)
6. Is consolidation (rewriting cases into lessons) harmful beyond ARC-AGI-type tasks? Re-open and verify Zhang et al. 2026 and look for replications.
7. When should the agent refuse to retain even a verified success (e.g. correct for the wrong reason; CASCADE always-retain hurt 4 of 12 tasks)? What cheap signal detects this?
8. Does competence-style deletion (keep pivotal cases) work with embedding retrieval, which has no clean coverage sets, or does utility-by-later-retrieval do equally well?
9. What does "20.9%" mean in the CASCADE abstract, and what is the per-task spread across the 16 tasks (rather than the 12-task table)?
10. How much of the retention gain is just more diverse few-shot examples? A control with random same-task examples at the same count is missing in most papers (ExpeL Table 3 is the exception).

## Gap search results
Sources re-opened this session (PDF text): Zhang 2026 (2605.12978), CASCADE (2605.06702, table S4 and supplement), ExpeL, ReasoningBank, Xiong, Evo-Memory, ACE, SEDM, ReMe, MemRL, Sarukkai, LifelongAgentBench. The web search quota ran out and the arXiv, OpenAlex and Semantic Scholar APIs were rate-limited, so forward-citation search was not possible; papers were fetched by arXiv id. Evidence is in evidence_d.jsonl (d01-d20); claims K18-K24 were added and K07, K09, K11, K17 updated.

- Gap 1 (four write gates at equal tokens): OPEN. Only pairwise pieces: selective beats add-all by 3.50 Avg@4 (ReMe); paired-test admission cuts prompt tokens 40 percent at equal or better accuracy (SEDM). See d13, d12, d20.
- Gap 2 (judge accuracy needed): PARTLY CLOSED. Raw traces: 6 of 12 coarse-judge cells beat the fixed seed bank in Xiong Table 1 (d10); no percent accuracy given. Distilled strategies: ReasoningBank real judge 72.7 percent, simulated 50 to 100 percent all above no memory (d09). The store-format explanation is plausible but untested.
- Gap 3 (novelty gate replicates Yang and Zhu, saturation size): OPEN. Nearest: CASCADE discovery trigger gives +8.83 percent vs 5.61 percent for random placement (d07).
- Gap 4 (decay over 1000+ tasks with shift): OPEN with partial data. 400-step decay under agent-managed consolidation (d04); Xiong shift and capped memory at 100 or 180 records (d11). No success-only stream over 1000 tasks found.
- Gap 5 (failure lessons at equal tokens): OPEN on tokens. Gains are small (+0.7 to +3.2) and raw failures can hurt (d13, d09, d16).
- Gap 6 (consolidation harm beyond ARC): CLOSED on verification. Zhang 2026 is real and the harm shows on ALFWorld, ScienceWorld, WebShop and AppWorld (d01-d05); ACE corroborates a rewrite collapse (d18). No independent replication of Zhang found; delta-append and add plus delete avoid most of the harm.
- Gap 7 (refuse a verified success): PARTLY CLOSED. Cheap signals: paired replay (SEDM, d12) and per-case retrieval-outcome Q (Sarukkai d15, MemRL d14). CASCADE's 4 hurt tasks were retriever-capacity failures, not wrong cases (d07).
- Gap 8 (competence deletion with embeddings): PARTLY CLOSED. Later-use utility works with embeddings (d13, d14, d15). Footprint or competence deletion with embeddings is untested.
- Gap 9 (20.9 percent): PARTLY CLOSED. Undefined in the text; the 12-task gain is +18.35 points, range +2.1 to +51.2, median +15.7 (d06). The 16-task figure was not reconstructed.
- Gap 10 (diverse few-shot control): PARTLY CLOSED. ExpeL: random successful examples +2.5, task-similar retrieval +19 (d08); strong models gain little from replay (d17).

Corrections: Zhang 2026 is now confirmed (opened). Evo-Memory, ReMe, ExpeL and Sarukkai table cells were mapped by row order from garbled text; treat them as approximate.
