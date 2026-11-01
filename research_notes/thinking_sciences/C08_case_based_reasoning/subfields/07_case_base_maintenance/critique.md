# C08.07 Case-base maintenance: cross-check critique

## Sources re-opened this session (full text, pdftotext)
Xiong et al. 2025 (arXiv 2505.16067), ExpeL (2308.10144), Dynamic Cheatsheet (2504.07952), ReasoningBank (2509.25140), Agent Workflow Memory (2409.07429), Mem0 (2504.19413).
Not re-opened: Smyth and Keane 1995, Wilson and Martinez 2000 (no free PDF found; arXiv guess returned an unrelated paper), Zhu and Yang 1999, Memento, Voyager, ACE, Sarukkai, Evo-Memory.

## Corrections
1. Xiong table (strict evaluator): the numbers in a11/b13/c01/c02 are confirmed (fixed 67.53/16.75/40.11/71.50; add-all 55.48/13.05/32.32/59.90; strict 70.95/38.50/51.00/85.40, sizes 4100/2411/2125/1050 and 2938/1012/1178/904).
2. b16 swaps two rows. Periodic vs history labels for RegAgent and CIC-IoT are reversed in b16. The memory sizes settle it: periodic prunes hard (Reg 67.65 at 949; EHR 38.59 at 302; Driver 50.94 at 467; IoT 80.80 at 310), history prunes lightly (Reg 69.80 at 2286; EHR 42.06 at 784; Driver 51.81 at 846; IoT 89.60 at 788). a14 and c04/c05 are right; b16 is wrong for Reg and IoT. The pdftotext layout is ambiguous, so this is inferred from sizes and the paper text, not read from labelled cells.
3. ExpeL table 3: hand-crafted insights is 32.0, insights with reflections 29.0, gpt-3.5 insights 32.0 (a17, c16 right). b20 says hand-crafted about 29 and reflections 28: wrong. ALFWorld confirmed: ReAct 40.0, reason-similarity 48.5, random 42.5, ExpeL 59.0 (b19 ALFWorld "54% vs 59%" compares with Reflexion, not part of this table). Again the extracted layout is shifted; reading in sequence order gives the a17 values.
4. Dynamic Cheatsheet: Claude 3.5 Sonnet AIME 2024 baseline is 23.3, not 23 (c10, loose). DC-Cu 50.0, DC-RS 46.7, retrieval-only 43.3, full-history 26.7 (text). GPT-4o: baseline 20.0, DC-Cu 36.7, DC-RS 40.0, full-history 6.7 (text). GPT-4o GPQA-Diamond: table gives 57.1 for DC-RS and 58.1 for DC-Cu, but the text says 57.1 to 58.1 "with DC-RS": internal inconsistency in the paper.
5. ReasoningBank: 49.7 is WebArena-Shopping (Gemini-2.5-flash) ReasoningBank; AWM 44.4 and 46.5 for success-only ReasoningBank (line 707) confirmed; judge accuracy 72.7% confirmed.
6. AWM: 24.6% and 51.1% relative, +12.0 absolute and the 0.1 rule-vs-LM gap confirmed.
7. Mem0: abstract says 91% lower p95; body says 1.44 s is a 92% reduction (search vs total). Treat "about 91-92%".

## Contradictions
- Judge sensitivity: Xiong finds a coarse judge costs 4 to 12 points and can fall below the fixed baseline; ReasoningBank finds near-flat success from 100% to 50% simulated judge accuracy. Different tasks, different memory content (raw trajectories vs distilled strategies). Unresolved.
- Deletion value: history-based deletion helps EHRAgent and CIC-IoT but not RegAgent; periodic pruning hurts IoT with a strict judge. No policy dominates.
- Memento sees no swamping up to about 3k items; Xiong sees damage from add-all at 2k to 4k records. The difference is the quality gate, not the size.
- Smyth and Keane: 100% competence is on a 50-case base with a toy domain; modern results are on benchmark agents. They are not comparable.

## Weak spots
- Almost all LLM maintenance evidence for deletion comes from one paper (Xiong), one backbone (GPT-4o-mini), four agents. Independent replication is absent, so most claims are single-source.
- AIME 2024 has 30 questions; Dynamic Cheatsheet gains are in steps of 3.3 points with no confidence intervals.
- Classic CBR numbers (Smyth and Keane, Wilson and Martinez, Zhu and Yang) are from the executor's reading but not re-checked here; the Smyth and Keane base is only 50 cases.
- No study at equal tokens: added memory means added prompt tokens, which most papers do not control.
- MemoryBank forgetting is untested; Voyager skill-library pruning is not studied.

## Seen only in snippets or memory
a26 to a30, b05 to b12 (Minton, Leake and Wilson, Brighton and Mellish, Delany and Cunningham spam-filter editing, Smyth and McKenna 2001, Zhu and Yang original), plus the Smyth and Keane figures held in a04/a05/c23 that were read by earlier agents but not by me. The b35 note says search quotas were exhausted.

## GAPS
1. At equal prompt tokens, does a verified-retain memory with deletion beat a plain fixed-size window for an LLM agent on a non-agentic reasoning benchmark (not Xiong's four agent tasks)?
2. How accurate must the retain judge be (ground truth vs same-model self-judgment) before add-if-verified beats fixed memory? Reconcile Xiong with ReasoningBank.
3. Do competence-style rules (delete auxiliary and support cases, keep pivotal) transfer to LLM case banks, and how do you define coverage and reachability with embedding similarity?
4. Does swamping (retrieval cost and mismatch) appear at 10x to 100x bank size (tens of thousands of cases), and how does retrieval-precision decay with size?
5. Does Delany and Cunningham case editing (noise and conflict removal) or Brighton and Mellish instance selection show up as gains for LLM few-shot banks with wrong labels?
6. Does Leake and Schack exploration-versus-exploitation maintenance, or usage-based forgetting, beat recency or Ebbinghaus decay (MemoryBank) in an ablation?
7. Does deduplication and merging of near-identical cases (Mem0 style) change accuracy, or only cost?
8. Are the Xiong results reproducible with a stronger backbone and a different agent family?
9. Is failure retention (ReasoningBank) better than success-only under a fixed size cap, and what share of failures to keep?
10. Minton and Francis-Ram utility-problem numbers: what did they actually measure, and is the match to LLM context cost real?


## Gap search results

Evidence file: evidence_d.jsonl (d01 to d20, all opened this session). Web search quota ran out early; arXiv PDFs were fetched directly by id, and Semantic Scholar, OpenAlex and the arXiv API were rate limited, so some searches by topic could not be run. Papers were found from memory of the literature, then opened.

1. Equal tokens, non-agentic benchmark: PARTLY. Evo-Memory (d04) uses AIME, GPQA and MMLU-Pro with a shared top-4 retriever and one prompt limit; plain retrieval (ExpRAG) is about as good as the best evolving method, gains are moderate. ACE on FiNER (d14) shows a 10K-token pruned context equals a 100K one (78.6 vs 78.3). No study compares verified-retain with deletion against a fixed window on a reasoning set. Open.
2. Judge accuracy: NARROWED, not closed. Pan et al. (d18): judges 74-93% accurate already give big gains on web tasks. Memory-R1 (d10): a worse manager costs 6-8 F1. Huang et al. (d19): same-model self-judging of reasoning is unreliable. Best reading: the judge must be grounded in an outcome or verifier; the accuracy needed is task dependent. No sweep at fixed task.
3. Competence rules: OPEN. Embedding coverage definitions exist (d11, d12) but only for query-time selection or pool building, never for deleting cases. Needs a new test.
4. Swamping at 10x-100x: PARTLY. Speed does not degrade with a vector index (A-Mem, d13: 0.31 us to 3.70 us, 1k to 1M notes) and the capacity limit is far away (Weller, d05: 500k+ at 512 dims best case). Accuracy vs bank size beyond about 3k cases is still unmeasured. Open on accuracy.
5. Case editing and instance selection with wrong labels: PARTLY CLOSED. Gao et al. (d06): wrong labels hurt generation heavily and a local neighbour filter recovers +13.8 to +18.8 EM; Min et al. (d07): classification barely cares (0-5%). Delany-Cunningham and Brighton-Mellish themselves were not tested on LLM banks, but the mechanism is supported for generation tasks.
6. Usage-based forgetting vs recency or decay: OPEN. MemoryBank (d17), SAGE (d15) and MemoryOS (d16) were all checked; none ablates the forgetting rule. Leake and Schack not tested anywhere.
7. Dedup and merging: PARTLY. ACE (d14) shows threshold changes of 50-90% move FiNER accuracy within about 5 points with no trend; A-Mem (d13) shows updating neighbours helps accuracy. No on/off dedup arm with repeats. Current best reading: mostly cost, effect on accuracy not distinguishable from noise.
8. Stronger backbone or other agent family: PARTLY. Evo-Memory (Gemini 2.5, Claude 3.7) and Memp (GPT-4o, Claude 3.5 Sonnet, Qwen2.5-72B) show memory gains on other families, and that raw append is not best. Nobody re-ran Xiong's add-all vs strict vs fixed design. Open as a replication.
9. Failures vs success-only under a cap: OPEN. Evo-Memory (d04) says unfiltered failures hurt plain baselines; Memp (d09) discards failures in one arm and revises in place in the best arm. No sweep of failure share under a size cap.
10. Minton and Francis-Ram: HALF CLOSED. Minton read via Zito-Wolf review and his own reply (d01, d02): about 20% of rules retained, 2-3x speed-up, utility = savings minus use cost, effect depends on a time cap. Francis and Ram 1993 not found online (d03, reference only). The mapping to LLM context cost is plausible (cost of use = tokens and distraction) but not measured.

New contradictions: Min (random labels harmless) vs Gao (noisy labels harmful on generation): resolved by task type. Dedup dip at 70% in ACE shows noise at the same size as the claimed effects.
Still weak: all added LLM results are single runs without intervals; several table layouts were scrambled by pdftotext, so only headline figures were taken.
