# Critique: E10.07 Analyst sensemaking (cross-check)

## Numbers re-checked against source text (extracted PDFs/HTML in D:/research_scratch/E10.07)
1. Sensecape concepts 68.3 (SD 49.1): confirmed (a21, b13, c13).
2. Selenite 840.3 s vs 1319.3 s, F(1,20)=102.5, precision 98.8 vs 78.4, recall 73.0 vs 30.4: confirmed.
3. GraphRAG graph sizes 8,564/20,691 and 15,754/19,520: confirmed.
4. SCOUT main table: 78.7 at 29.7k tokens, Gemini-3-Pro 68.5 at 273.9k (0.25 acc/k), Claude Code 63.4 at 25.3k: confirmed. Ablations 70.5 (-7.7), 17.7 (-60.5), 74.2 (-4.0), 75.5 (-2.7): confirmed. CORRECTION: the ablation table implies a full-model score of 78.2 (70.5+7.7), not 78.7; the paper's two tables differ by 0.5 and a05/c05 should be read as "about 78". Also the main-table 63.4 for Claude Code appears to be a different column block from the 68.4/17.7 row at line 1338, so do not mix them.
5. Mandel et al. 2018: ACH MAE 0.26 vs control 0.21, t(45.9)=1.49, d=0.43, p=.14: confirmed; direction favors control.
6. Marco: 249.6 vs 297.3 s (16% faster, p=.004), accuracy 88.1 vs 91.9%, chi2=3.35, p=.067: confirmed. Add the speed p-value to b20.
7. InForage mean EM 41.0 vs Search-o1 35.6 and plain RAG 26.5: confirmed in main table (3B).
8. Lebiere 2013 Table 6 (T1 81.7/80.7, T3 S2 34.7 vs 73.8, N=103 novel sample, original N=45): confirmed from PMC text.
9. Li et al. fact coverage (crowd 17 all comprehensive; holistic 6, none comprehensive; step-by-step 9, 5 comprehensive): confirmed. NOTE: this is a 2024 CHI workshop paper (dated 2026 in the evidence by arXiv id); one case, one model (GPT-4), so no statistics.
10. DeepNews: abstract says HFR above 85% above 30,000 characters; 25% vs 0% acceptance: confirmed. a30 says "about 85% above 30,000"; c17 splits "30k 85%, 40k 90%". Consistent.
11. Failing to Falsify: 6% to 78% and 42% to 56% discovery confirmed in the abstract. Qwen3-8B 0.21 to 0.40 (I:C 0.15 to 0.35) confirmed in table. NOT RESOLVED: b18 says Qwen3-32B thinking 0.33 to 0.63, b19 says 0.41 to 0.61; the table text is ambiguous (different intervention rows or model variants). Treat the Qwen3-32B figures as unverified.

## Contradictions and weak spots
- No Pirolli and Card claim has experimental support. The model is notional; the only quantitative fit (Lebiere 2013) tests a different model (data-frame tasks in ACT-R) and misses resource allocation badly.
- ACH evidence is mixed in design, not in direction: the only analyst RCT (N=50) is null, law-student study (N=191) null on question preference, earlier positive studies lacked controls. Heuer says he would ignore non-faithful tests. So status is "contested", not refuted.
- Human tool studies (Sensecape, Selenite, Marco) all use N=7 to 16, measure human output, and often self-built baselines. They do not test an agent's accuracy.
- LLM-agent studies are on different tasks and backbones (3B, 72B, API models), so none can be compared. Several are 2025-2026 preprints; I did not see replications. Model names in a few (e.g. GPT-5.6-terra in SHELDON) were taken from the source and not verified further.
- Marco and Sensecape show a speed/breadth vs accuracy/preference tension; ignored in marketing abstracts.

## Seen only in snippets or not opened
a09, a10, a11, a19, a20 (Russell 1993, Pirolli and Card 1999, Klein et al., Patterson et al. 2001, Kang and Stasko), c24, c25, c26 were not read. The Pirolli and Card 2005 PDF was read, but c24 was a duplicate not opened. Figure-only results (InForage ablation, SCOUT 64K-1M sweep, Tang et al. fidelity table, InterDeepResearch benchmark) have no extracted values.

## GAPS (most decision-relevant first)
1. Does a separate forage-vs-sense split in an LLM agent beat a single mixed loop at equal tokens? No paper isolates it (SCOUT ablates the epistemic state only).
2. Does an explicit written evidence-state (shoebox/evidence file) improve accuracy beyond the same notes kept in context, on tasks that fit in context?
3. Is the incompatible-test (falsification) gain in Failing to Falsify replicated on tasks other than rule discovery, and does it hold at equal tokens?
4. Does structured ACH (matrix) help LLM agents even though it did not help human analysts? No LLM-ACH test with N and a control was found.
5. What are the correct Qwen3-32B figures in Failing to Falsify (0.33 to 0.63 vs 0.41 to 0.61)? Needs the table re-read.
6. Do information-scent / gain-per-fetch stopping rules help without RL training (prompt-only)? InForage trains with PPO.
7. Pirolli and Card's claim that expert analysts gain information faster over time (Figure 6): any measured data? Lebiere 2013 and Andrews 2011 do not test it.
8. Are the Li et al. holistic vs step-by-step findings reproducible with current models and more than one case?
9. How much of the DeepNews context-size effect (30k chars) is redundancy vs simple volume?
10. Can the Andrews large-display effect (structures 15.75 vs 9) be translated into agent workspace size or structure, and does it survive a larger N?

## Gap search results (gap searcher, 2026-11-03; evidence in evidence_d.jsonl, d01-d16)
Search tools were limited: the WebSearch budget was exhausted, arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors. Work used arXiv's own search page and direct PDF reads. Papers could not be searched for broadly, so "none found" means none seen, not none exist.

1. Forage-vs-sense split vs one mixed loop at equal tokens: STILL OPEN. Nearest proxy is SCOUT's w/o-epistemic-state ablation (70.5 vs 78.2 at 28.3k vs 29.7k tokens, d13), which splits action log from evidence state, not forage from sense. PatchScout (d10-d12) tests switching policy, not loop separation.
2. Written evidence state beyond notes in context: PARTLY CLOSED for long documents (SCOUT, -7.7 at equal cost) and for diagnosis (SIA 79.2 vs 72.8 for thinking plus interaction, d07, CIs overlap, more questions asked). STILL OPEN for tasks that fit in context with matched tokens.
3. Falsification gain beyond rule discovery and at equal tokens: PARTLY. Second task (Blicket) is by the same authors and mixed (non-thinking 32B 0.64 to 0.56; thinking 32B 0.57 to 0.86). Tokens per turn rise (d03), totals per episode not reported. No independent replication seen. OPEN.
4. ACH-style matrix for LLM agents: PARTLY CLOSED. AgentCDM (d05, d06) gives a controlled zero-shot test: small gain (about +2) on MCQs; SIA (d07, d08) shows counterfactual critique worth about 5 points in diagnosis. Neither is token-matched or tests analyst tasks. Human null result unchanged.
5. Qwen3-32B figures: CLOSED. Thinking baseline 0.413, TiO 0.613, Dual-Goal 0.600; non-thinking baseline 0.325, Dual-Goal 0.100, TiO 0.362 (d01). Also corrects K11: Qwen3-8B TiO is 0.36, Dual-Goal 0.40.
6. Prompt-only scent or gain-per-fetch stopping: PARTLY CLOSED by PatchScout (d10-d12), a training-free scent/yield patch-switching system. Gain is mostly from switching at all; scent adds a small, inconsistent increment over a fixed-count switch. Task is corpus collection, not QA. Stopping for answering was not tested.
7. Expert analysts gain information faster (Figure 6): CLOSED negatively. Figure 6 is notional, text asserts only (d15).
8. Li et al. reproducibility: STILL OPEN. One case, GPT-4 only (d16); no reproduction seen.
9. DeepNews redundancy vs volume: STILL OPEN, and shown to be undecomposed (d14): one factor, 20 reports per cell, no variance.
10. Andrews large-display effect for agent workspace: STILL OPEN; no new evidence found.

Other corrections: SCOUT full score is about 78 (78.7 main table, 78.2 ablation). New claims K22 to K27 added; K03, K04, K07, K11 updated.
