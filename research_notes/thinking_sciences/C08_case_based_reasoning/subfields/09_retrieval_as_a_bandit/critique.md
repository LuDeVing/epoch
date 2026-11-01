# C08.09 Retrieval as a bandit: cross-check critique

Cross-checker pass. I re-downloaded the PDFs of CASCADE (2605.06702), Memento (2508.16153), MemRL (2601.03192), Active Example Selection (2211.04486), LLM-R (2307.07164), EPR (2112.08633) and ReasoningBank (2509.25140) to D:/research_scratch/C08.09/ and grepped the numbers in the extracted text. PDFs deleted afterwards.

## Numbers re-checked (14 confirmed, 3 corrections)

Confirmed against the source text:
1. CASCADE Qwen3-32B averages: full 66.68, zero-shot 48.33, NP-CBR 63.76, alpha=0 66.37, LinLogUCB 63.95, NeuralLogUCB 65.39, NeuralLinUCB 65.49 (ablation table). Per-task: SEntFiN 47.72 full vs 48.37 w/o exploration; TLP 56.79 vs 57.09; BIRD NeuralLogUCB 56.21 vs full 55.18. OK.
2. CASCADE baselines: ICRL 52.48, ICRLPlus 54.33, REINFORCE+LoRA 58.93. OK.
3. CASCADE 8B: 60.84 vs NP-CBR 58.44; 14B: 65.10 vs 62.81. OK.
4. CASCADE ALFWorld 62.01 to 67.43, ScienceWorld 59.36 to 66.84; ReAct 80.76 to 81.74 and 71.52 to 74.67. OK. 2Wiki local RAG 45.94 to 50.06 not re-checked beyond 50.06; web 53.29 to 66.51 OK.
5. CASCADE discovery budget: Exploit +8.83%, UCB +8.73%, Random +5.61%. OK.
6. Memento Table 4 (no CBR, non-parametric, parametric iter 1 to 5): all values match. GAIA 87.88 Pass@3 and 79.40 test OK. K table (59.9/72.2 ... 64.5/78.5 ...) OK.
7. MemRL Table 1: no memory 0.631, MemP 0.736/0.760, MemRL 0.772/0.798; per-task row OK; frozen transfer 0.794 vs 0.766 OK; r=0.861 and 21.5% to 88.1% OK.
8. Active Example Selection: random 59.6, reordering 63.5, best-of-10 72.5, greedy oracle 78.0, learned 71.4 / 71.6 / 69.0; new task 63.8 and 65.4. OK. Text "11.8/12.1/7.9" OK.
9. LLM-R: random 57.9, SBERT 62.1, EPR 63.5, iterations 65.7 / 66.5 / 66.4; held-out 81.7 vs E5 76.3. OK.
10. EPR: BREAK 31.9, MTOP 64.2, SMCalFlow 54.3, BM25-oracle 32.3, test BREAK 23.9. OK.

Corrections:
- a21 labels EPR 26.0 to 31.9 (BREAK), 57.0 to 64.2 (MTOP), 51.4 to 54.3 (SMCalFlow) as "test results". These are DEV results (b05 has it right). EPR test numbers are lower (BREAK 17.6 BM25 vs 23.9 EPR). Also the 57.0 / 51.4 baseline is the prior learned retriever CBR, not BM25 (BM25 is 52.9 / 46.1), so "vs BM25" gains are bigger than "vs best baseline".
- a22 / b07 / c15 say "+7.8% over random" (relative or percent). It equals 65.7 minus 57.9 = 7.8 absolute points for iteration 1 only. Iteration 2 is +8.6 points. Treat as points, not percent.
- a26 gives ReasoningBank k=2 as 46.5. The source text is garbled ("46 ... with 2") and 46.5 equals the Synapse figure elsewhere in the same paper. Use "about 46" (b20). Values 39.0, 49.7, 45.5, 44.4 confirmed.

## Contradictions and tensions between sources
- Memento Table 4 (learning curve) shows case memory beating no memory by only +1.8 (iter 1) and +1.0 (iter 5) points, while the ablation table claims +6.7 F1 / +8.2 PM on DeepResearcher. Different protocols and metrics (accuracy over iterations vs F1/PM with fixed K). a10/b13 note this partly; the two should not be added.
- CASCADE claims exploration matters (adds a section on UCB for discovery), but its own ablation puts alpha=0 within 0.31 points, inside the per-task noise. The "bandit" label is carried by the learned reranker, not the bonus.
- MemRL gain is largest where the same items repeat (HLE gain is memorisation by its own admission) so "learned value helps" and "learned value memorises the test set" cannot be separated from its runtime table. Memento GAIA Pass@3 has the same problem.
- Learned value helps small/old models a lot (Active Example Selection, LLM-R on LLaMA-7B) and frontier agents little (Memento +0.6 to +1.0; ReAct CASCADE +0.98). Direction is consistent: the stronger the base, the smaller the gain.
- Min et al. (b11): random labels barely hurt, which suggests demonstrations carry format, not content. This undercuts any claim that an outcome-based value is learning "which answer is right"; it may be learning "which format fits".

## Weak spots
- CASCADE is a single unreviewed preprint (v1, May 2026); every CASCADE number is self-reported. No independent replication found.
- Memento, MemRL, Memory-R1, ReasoningBank report single runs without error bars in the tables read. Memento authors flag possible contamination.
- No paired significance tests anywhere in the set. Most learned-vs-similarity gaps (0.6 to 1.0) are inside plausible seed noise.
- Memory-R1 and EPR/LLM-R train model weights or retriever on labelled data; they are not pure scaffold results.
- Cumulative success in MemRL counts any-epoch success, which flatters exploration.
- The classic literature the subfield names (1990s case-based RL, Auer 2002, Thompson 1933, Aamodt and Plaza 1994, Li 2010 hybrid numbers beyond the abstract) was not opened or only partly read: a27, a28, b25, b26 are unopened; a17, a18, a20 were abstract/skim only; a24 first page only; a25 methods only.
- b27 and c26/c27 are gap notes with no data; evidence_b was written while search quota was out.
- Claim K03 and K16 rest on one source (CASCADE).

## Only seen in snippets or partly
- a24 Reflexion (first page), a25 ExpeL (methods only; results from c19/b17/b18 though), a17/a18/a20 (abstract level), b10 KATE (table columns garbled), b09 CEIL (table garbled), c24 AWM (abstract and intro), a27/a28/b25/b26 (not opened).

## GAPS (most decision-relevant first)
1. At equal tokens and on a strong frontier model, does a learned utility add anything over top-1 similarity once the case is already relevant? Memento and CASCADE suggest 0.6 to 3 points, with no seeds or CIs. Needs a paired, multi-seed test on non-contaminated tasks.
2. Is the exploration bonus (UCB or Thompson) worth anything for case choice? CASCADE alpha=0 loses 0.31. No study compares UCB vs Thompson vs greedy Q vs epsilon-greedy over a case bank with regret reported.
3. Does learned case value survive task drift (non-i.i.d. streams, changing tasks)? CASCADE theory assumes i.i.d. MemRL shows it ties where tasks are scattered. What is the break-even task similarity?
4. How much of MemRL/Memento runtime gain is memorisation of repeated test items versus transfer? Need a held-out stream with no repeated items and frozen bank, same backbone.
5. Is outcome-based value learning robust to noisy reward (LLM-judge labels about 72.7% accurate in ReasoningBank)? What accuracy of success label is needed before learned value beats similarity?
6. Can value be assigned to cases when several are shown together (credit assignment)? MemRL admits this is unsolved; CEIL set-level selection suggests it matters. Is there a cheap fix at K of 1 to 4?
7. Do failure cases deserve learned value too (Memento stores both, CASCADE discards them, MemRL keeps 12% near-misses)? No ablation of success-only vs both under a learned selector.
8. Does cost of building value labels (EPR scoring pass per candidate, MemRL runtime updates) pay back at equal total tokens versus spending the same tokens on extra sampling or best-of-N?
9. Classic literature gap: do 1990s case-based RL and CBR utility-learning results (CASCADE original line, Aamodt and Plaza 4R, Auer UCB1 and Thompson) show anything about retention policy and case-base growth that LLM papers have not retested?
10. Does set-level selection (diversity, DPP) interact with a learned value, and does it fix the SQuAD-style near-duplicate failure of LLM-R?

## Gap search results
Search quota was out, so this pass pulled papers directly (evidence_d.jsonl, d01 to d20; 19 opened). New claims K20 to K27; K01, K03, K05, K09, K10, K15, K17 extended.

- Gap 1 (learned value vs top-1 similarity, strong model): PARTLY CLOSED, no frontier test. Sarukkai 2025 (5 seeds, gpt-4o-mini, fresh test tasks): learned exemplar value adds +1, +2, +8 points over naive accumulation (d01). Evo-Memory shows plain similarity retrieval is already competitive on Gemini 2.5 and Claude 3.7 (d15). Still open: frontier model, paired seeds.
- Gap 2 (exploration bonus): PARTLY CLOSED from classics. Tuned epsilon-greedy or softmax matches or beats UCB1 (Auer 2002; Kuleshov and Precup 2014); Thompson best by 1.3 regret points in ads (d10 to d12). No LLM case-bank regret study exists. Open for cases.
- Gap 3 (drift): PARTLY CLOSED. Theory says sqrt(T) regret floor and discount or window fix (d13); Xiong shows one shift survived with utility deletion (d09); gain tracks task similarity (d15). Break-even similarity still unknown.
- Gap 4 (memorisation vs transfer): CLOSED enough to act. MemRL runtime gain over RAG 8.15 points vs frozen-bank held-out 2.8 on shared benchmarks (d05); Sarukkai uses distinct test tasks (d04). Caveat: different splits, no seeds.
- Gap 5 (label noise): MOSTLY CLOSED. Untuned LLM judge can drop a raw bank below fixed memory; tuned judge on 300 runs recovers (d07); distilled lessons barely care (d14). Exact break-even accuracy for a learned selector not measured.
- Gap 6 (credit for several shown cases): STAYS OPEN. Only value-free set coverage (d17) found. Sarukkai Q weights by retrieval frequency, a crude share.
- Gap 7 (failures under a learned selector): STAYS OPEN. Indirect evidence only: raw failures hurt baselines, lessons from failures help (d14, d16); Aamodt and Plaza back keeping failures (d19).
- Gap 8 (cost payback vs best-of-N): PARTLY CLOSED. Curated bank equals pass@2 to pass@5 at no extra test cost, N times training cost (d03); best-of-N needs a verifier (d18). No equal-token study.
- Gap 9 (classics): PARTLY CLOSED. Auer 2002, Chapelle and Li 2011, Aamodt and Plaza 1994 opened (d11, d12, d19). Not obtained: Thompson 1933, 1990s case-based reinforcement learning, Smyth and Keane retention work.
- Gap 10 (learned value x diversity, LLM-R duplicates): STAYS OPEN. No study combines them (d17, d20).

New weak spots: Xiong, Evo-Memory and MemRL tables have no error bars; several Evo-Memory and Xiong table cells were read from garbled text; MemRL 8.15 vs 2.8 is my cross-table computation.
