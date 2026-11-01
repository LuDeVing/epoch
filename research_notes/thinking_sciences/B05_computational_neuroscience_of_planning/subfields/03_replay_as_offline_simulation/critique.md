# Critique: B05.03 Replay as offline simulation (Dyna family)

## Sources re-opened this pass (checked against full text)
- Sleep-time Compute (arXiv 2504.13171): 5x, +13%, +18%, 2.5x all confirmed.
- Dyna-Think (arXiv 2506.00320): Table 3 and Table 4 read; r >= 0.32 and +16.8 points confirmed.
- WebDreamer (arXiv 2411.06559): 17.6 / 23.6 / 26.2 (VWA), +34.1%, +42.3%, +23.8% confirmed.
- DreamGym (arXiv 2511.03773): ablation numbers 63.9/13.3, 59.2/9.7, 55.8/7.3, 57.3/7.3 confirmed. Table 1 only partly readable.
- Agent Workflow Memory (arXiv 2409.07429): 35.5 vs 23.5, +12.0, +51.1%, +24.6% confirmed.
- CogEval (arXiv 2309.15129): GPT-4 row values and detour coefficient -2.35 confirmed.
- Momennejad et al. 2017 (PMC6941356): exp2 means and SEMs, exp1 t(57)=2.89 and 10.14 confirmed.
- Schaul 2016: "41 out of 49 games" confirmed on the abstract page.

## Corrections
1. b22 is wrong on the vanilla Dyna row. Dyna-Think Table 3: vanilla Dyna avg 23.2 (BoN 38.5 all tasks), not 24.1. The 24.1 (BoN 35.6 all tasks; 29.3 is a different column) belongs to the DDT next-state row. The c06 figure (23.2) is right. Consequence: vanilla Dyna gave no gain over RFT (23.2) on OSWorld, not a small gain. The "BoN down from 40.7" story in b22 compares against DIT(R1) and a non-"all tasks" column; do not use it.
2. R1 BoN: 44.8 is all-task BoN; 48.8 is the in-domain column. b22 mixed these (48.8). Use 44.8 for all tasks.
3. b25 (DreamGym) column mapping is unreliable. PDF text shows 63.9 and 13.3 sit in the L3.2-3B columns, 68.3 in L3.1-8B, and one ALFWorld cell is missing in the extraction. The statement "Q2.5-7B: DreamGym 0 real 68.3 / 71.0" is likely a wrong column. The GRPO numbers (66.1, 79.8, 6.1 for Q2.5-7B) look right. Keep only the headline (zero-real roughly matches 80K-real GRPO) and the ablations until the table is read as an image.
4. "SR-Dyna fit human revaluation best" (task framing) is not what the 2017 human paper tested. It fitted pure MB, pure SR and hybrid SR-MB. The SR-Dyna claim is the 2020 review's reading plus Russek simulations (a09, a10, b06). Mark as contested.
5. b16: the review says the replay-revaluation link is stronger under high reward variance; the primary data show interaction p=.34 (b09). Treat as not supported.
6. a02/a26/b06/b29 are all Sutton and Barto-derived; counted as one source, so the shortcut claim (K02) is single-source.

## Contradictions between sources
- Replay is for planning (Foster/Wilson-style, Pfeiffer and Foster, Xu 2019) vs memory maintenance (Gillespie 2021: replay favoured previous goal and long-unvisited arms, did not predict next choice). Not resolved; may differ by task and species.
- Dyna helps in tabular RL (Sutton, Moore and Atkeson) but gave little over extra real-data updates in Atari (Holland 2018) and hurt in LLM agents with a separate world model (WindowsAgentArena 20.9 vs 28.4).
- Sleep-time: o1 and high test-time budgets show limited gain; SWE agent case: precision dropped at high budgets (c04).

## Weak spots
- Almost all human and rodent numbers are n=3 to 88 and from one lab each (Momennejad 2017/2018 share an author group). No independent replication of the human revaluation asymmetry was found.
- The Russek 2017 results are simulations in small grid worlds, read only to about 100k of 182k characters.
- Sleep-time compute gain is on synthetic "Stateful" tasks built by the authors, where questions are made predictable from context.
- Dyna-Mind and Dyna-Think use trained models; their lessons for a no-training scaffold are indirect. The only no-training evidence is prompted rollouts (+3 to +14 points on ALFWorld/Sokoban, b19), WebDreamer, sleep-time, AWM, Reflexion, ExpeL.
- c10 text-world GPT-4 numbers came from a two-column parse; check original.
- No cost-matched comparison of "replay pass" vs "same tokens on a fresh attempt" exists in any source read, except sleep-time's pass@k comparison.

## Seen only in snippets or not opened
a17 (Gershman 2014), a18 (Foster and Wilson 2006), a19/c29/b29 (Sutton 1991), b14, b15, c28, c30 (Moore and Atkeson read via a03 only through secondary text). Also: a21, a22, a20, c23 to c26 are abstract-level; no per-task numbers. Moore and Atkeson Table 2 numbers (a03) were not re-opened this pass.

## GAPS (most decision-relevant first)
1. At equal total tokens, does an offline replay pass over stored solved traces (re-derive, relabel, abstract) beat spending the same tokens on a fresh attempt, for repeated item families? Any LLM study with a matched-compute control?
2. What replay priority works for an LLM library: surprise (failed prediction), expected reuse (need), or recency? Has anyone tested EVB-style prioritisation (Mattar and Daw) on LLM memory?
3. How does a stale subgoal get detected and re-tested (the Dyna-Q+ shortcut problem) in LLM agent memories; is there a measured result on library staleness after a task change?
4. When does LLM self-simulation of outcomes stop being better than acting: what hit rate of predicted vs real outcomes is needed before lookahead beats reactive? (Dyna-Think r=.32 to .45; WebDreamer gains.) Any threshold study?
5. Do the 2024-2026 LLM replay results (Sleep-time, AWM, Dyna-Think, DreamGym) replicate on other benchmarks or by other groups, and with what failures?
6. Has any group run human-style revaluation (reward vs transition change) on an LLM agent with an added offline replay step, beyond CogEval's no-replay baseline?
7. Hallucinated-value risk: does updating memory from simulated (not real) outcomes degrade accuracy in LLM libraries, as Aminmansour 2024 predicts for RL? Measured numbers?
8. Independent human replications of the reward > transition revaluation asymmetry and of the replay-replanning correlation (n=24 fMRI is small).
9. Read Sutton 1990/1991 and Moore and Atkeson 1993 primary texts to verify the maze numbers (currently via book and secondary text).
10. Correct DreamGym Table 1 by reading the table as an image: which model, which column.

## Gap search results (gap searcher, evidence_d.jsonl d01 to d20; claims K22 to K27 added)

Web search quota ran out early, and the arXiv, Semantic Scholar and OpenAlex search endpoints returned rate-limit errors. So discovery was limited to one web search pass, Europe PMC, and papers already known by ID. Absence of a study below means "not found with this limited search", not "does not exist".

### Closed
- Gap 10 (DreamGym Table 1): closed (d09). Order is WebShop, ALFWorld, WebArena; inside each, Llama-3.2-3B, Llama-3.1-8B, Qwen-2.5-7B. GRPO 80K real vs DreamGym 0 real: ALFWorld Qwen 79.8 vs 71.0, WebArena 6.1 vs 12.7. K16 rewritten.
- Gap 9, Moore and Atkeson half (d13): closed. Table 2 read as an image and confirmed (stochastic 2627-state 94,000 / 155,000 / 240,000). The 300-backup case is 21,000 obs vs 143,000. Small-maze exceptions recorded.

### Partly closed
- Gap 7 (simulated or wrong updates degrade a library): measured numbers exist for noisy writes, not for simulated outcomes as such. Add-all of self-generated experience cost 3.7 to 12.1 points vs a fixed memory (d01). Harmful update every step: 66.7 vs base 70.7; every 5 steps +5.4 (d07). Tolerance is high for rare errors. Claims K22, K24.
- Gap 2 (replay priority): no one tested expected-value-of-backup on LLM memory. Found: recency ties a learned scorer on a clean library (d04), learned utility beats similarity by under 1 point (d12), utility-based deletion helps only with a good evaluator (d02). Normative extension to uncertain goals exists (d16, abstract only). Surprise-prioritised replay exists only for fine-tuning (d19, not read). K23.
- Gap 3 (stale subgoals): only indirect. Offline vs online workflow memory under a train-test gap (d11); ReMe prunes by utility (d05). Explicit stale-detection and re-test: nothing found. Normative theory only (d17, abstract). K25.
- Gap 4 (hit rate for lookahead): Dyna-Mind across-model table (d08) shows success rising with simulation score, with big gains already at 0.35 on ALFWorld. Still no controlled threshold study. K26.
- Gap 8 (human replication): partial. Zhang et al. 2026 (d14, n=119+119, adapted task) found revaluation replanning but no significant rest benefit (p=.13). Kahn and Daw 2025 (d15, n=100) confirm an SR plus model-based mix. No independent replication of the fMRI replay-replanning correlation, nor of the n=58 and n=88 asymmetry, was found.
- Gap 5 (replication of 2024 to 2026 LLM results): Sleep-time: no replication found (d10). AWM: only the authors' own Mind2Web results (d11). Dyna-Think: the same group reran on new benchmarks (Dyna-Mind, d08); different group's Memento (d12) and ACE (d06) show similar memory-building gains on other benchmarks but test different methods. DreamGym: a Meta-affiliated single group. Failures found: context collapse in full rewriting (d06), add-all hurts (d01), retrieving more than about 5 entries hurts (d05).

### Still open
- Gap 1: no equal-total-token comparison of a replay pass versus a fresh attempt. Sleep-time uses equal test-time tokens only (d10); ACE multi-epoch adds tokens (d06). K27.
- Gap 6: no LLM agent run with reward-versus-transition revaluation plus an added replay step found.
- Gap 9, Sutton 1990/1991: PDF obtained but image-only, no OCR (d20). K01 episode counts remain from secondary text.

### Caveats on this pass
- d16, d17, d19, d20 are abstract-level or unread (opened false). d18 read in part.
- TraceRetain (d04) table layout was garbled in extraction; numbers used are from the prose.
- Xiong et al. were read through a fetched text rendering, final 2,435 characters not read.
