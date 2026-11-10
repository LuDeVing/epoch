# C05.06 Language Agent Tree Search: cross-check critique

## Re-opened sources (10 numbers checked, text from PDFs this session)
1. LATS Table 10 tokens: CONFIRMED RAP 210,215; LATS 176,500 and 173,290 (two LATS rows). **Correction:** evidence c05 assigns 210,215 to ToT and 176,500 to RAP. That is wrong. ToT has no token entry. a10/b03 are right.
2. LATS Table 9 node counts: ToT 33.97/47.54/84.05, RAP 31.53/37.71(?)/70.60, LATS 28.42/34.12/66.65 at k=10/30/50. The PDF text is column-shifted. c05 and b03 read it correctly. a10 ("3.55 fewer nodes than RAP, 12.12 fewer than ToT") is the paper's average claim, not the k=50 row (70.60-66.65 = 3.95).
3. LATS accuracy at k=50: Table 9/10 shows LATS 0.61, Table 3 shows 0.63. Both exist in the paper; c05's 0.61 is a different table, not a conflict.
4. LATS HotPotQA uses ground-truth feedback (paper text near Table 10: "benefiting from ground-truth feedback"). Treat the 0.63 as an oracle-assisted number (a04 flagged this; b01/c01 did not).
5. Koh et al. depth/branch grid: the PDF table is garbled. The c07 reading (d1b3 26.0, d1b5 32.0, d2b3 31.5, d2b5 35.0, d3b5 35.5, d5b5 37.0) fits the printed relative gains (+6, +29, +43, +45, +51). **Correction:** b04 says d=2,b=5 is 32.0%; that is wrong (32.0 is d=1,b=5).
6. Agent Q WebShop: confirmed base 28.6, RFT 31.3, DPO 37.5, MCTS 48.4, Agent Q+MCTS 50.5, human 50.0. **Corrections:** b16 ("DPO 28.6", "Agent Q trained 29.5") and c22 ("DPO 31.3, RFT 40.6") are wrong; a26 is right. Also confirmed 95.4% on OpenTable with online search. b16's RFT 67.2 not re-checked.
7. SWE-Search cost: confirmed GPT-4o $40.86 to $576.00 (about 14x); mini 9.90 to 42.50; Qwen 8.50 to 18.37. Some table cells are shifted in text; the GPT-4o row is clear.
8. SWE-Search 73% value-function and 84% discriminator accuracy, and the +1.4% Moatless-Adapted gain: confirmed.
9. Chen et al.: confirmed "least 90% accuracy" requirement, Spider greedy 62.3 vs best re-ranking 61.5, GSM8K GPT-3.5 47.6/48.4/51.0 with McNemar p>0.05, oracle 64.1/66.0/73.0. Bird numbers not re-opened.
10. Table 9/10 sample-size notes (100 HotPotQA questions) taken from a05, not re-opened.

Not re-opened this pass (taken from the evidence files): Huang (a18/a19), Olausson (b12), Wu (a23/b09), Snell (b10), Stechly (a24/b13), RAP, TS-LLM, Reflexion, Large Language Monkeys, MCTSr, ReST-MCTS*.

## Contradictions between sources
- Token and node attributions (above). Depth/branch cell (above). Agent Q WebShop baselines (above).
- b02 says exploration weight w=0.5 gave 0.55 and w=2.0 gave 0.63; a01 says default w=1. The paper's Table 11 was garbled in extraction, so the w ablation is unverified.
- Game of 24: LATS paper reports ToT 0.20 with GPT-3.5; the ToT paper reports 74% with GPT-4. Different models, so not a conflict, but LATS's weak ToT baseline is a handicap.
- Reflection: Reflexion alone +0.19 over ReAct, but only 0.05 inside LATS; so search absorbs most of the benefit (K11 contested because Rust ablation shows 0.60 to 0.68 with tests).
- Self-correction: Huang says it hurts; LATS/Reflexion say it helps. Resolved by the external-signal condition, but LATS's own value is an LM signal plus oracle feedback on HotPotQA.

## Weak spots
- Almost every LATS number is the authors' own GPT-3.5 run on a small set with no variance. No independent replication of LATS itself was found; only descendants (Koh, SWE-Search, Agent Q) use the idea, each in a different setting.
- Budgets are matched in trajectories, not tokens, and token counts cover successes only.
- Absolute gains on real environments are small (WebArena 19.2%, WebShop success +3 over Reflexion, SWE-Search +5.3).
- Math results (Wu, Snell) use trained process reward models, so they say little about a prompted-value agent.
- Costs of 14x (SWE-Search) have no equal-cost best-of-N control.
- No evidence at all on 2025-2026 frontier reasoning models: does native long-thought make tree scaffolds redundant?

## Seen only in snippets
Nothing is marked snippet-only in the evidence files (all opened:true), but several table cells came from garbled PDF text (LATS Tables 9 and 11, Koh depth grid, Olausson ratio grid, Stechly per-domain gains, TS-LLM equal-token table).

## GAPS
1. Does LATS beat a best-of-N with the same verifier at equal total tokens (failures included) when the signal is real tests or a hard checker, with N>=300 items and 3 seeds? (decides whether S6 should be a tree at all)
2. How much of LATS's HotPotQA gain remains without ground-truth feedback?
3. What is the break-even judge accuracy for tree search with prompted (not trained) value, measured on code, math and agent tasks? Chen finds about 90%; is that stable across models?
4. Does the LATS/SWE-Search/WebArena gain survive on 2025-2026 reasoning models (o-series, Claude, Gemini thinking), or does native long-thought absorb it?
5. Does self-consistency on the value (n=5 to 20) beat spending the same tokens on more branches? Koh shows gains but no cost-matched test.
6. How often do written reflections inside a tree help vs hurt (Rust +0.08 with tests, only +0.05 in LATS, MBPP Python worse)? Under which feedback type?
7. Which tasks allow state reversion? What happens on tasks with irreversible actions where LATS cannot backtrack (live web destructive actions)?
8. Is difficulty-gating (search only on medium items, per Snell) workable with a prompted difficulty estimate, and what is its cost?
9. Do independent re-implementations of LATS (e.g. LangGraph, LlamaIndex, later benchmarks) reproduce 0.63 HotPotQA / 83.8 HumanEval? Search for failed replications.
10. Does a program-owned tree with a small model as slot-filler (our scaffold design) keep the gain, versus the model driving the loop itself?

## Gap search results (evidence_d.jsonl, d01-d19; claims K19-K28 added, K01/K02/K04/K09/K11/K12 updated)

Status key: closed = answered with measured data; partly = some data, main condition untested; open = no usable data.

1. LATS vs best-of-N at equal total tokens, real tests, N>=300, 3 seeds: PARTLY. Koh (d04) shows search beats re-ranking at about equal LM calls on a 200-task web subset (37.0 vs about 30). Kapoor (d01, d03) shows on HumanEval that retry baselines match LATS accuracy at 1/55 of the dollars. No study has N>=300, 3 seeds and token-matched cost with failures included. DARS (d16) gives only a cost-scaling table.
2. HotPotQA gain without ground truth: OPEN for LATS itself (d07: no such ablation). Proxy from Karthikeyan (d08, d09): on GSM8K the oracle-free self-reward choice is at or below random for Haiku3 and Sonnet3 and gains come from majority vote; on ToolTalk it lowers F1. Treat 0.63 as an oracle number.
3. Break-even judge accuracy across models: PARTLY. No new threshold. New data: judge quality ladder in Koh (LLaVA 30.0, GPT-4o 37.0, truth 43.5) and Karthikeyan's four-model sign flips. The 90% figure of Chen is neither confirmed nor refuted across models.
4. Survival on 2025-2026 reasoning models: OPEN to PARTLY. No clean tree-vs-no-tree run on o-series, Claude or Gemini thinking. Indirect: PRISM-MCTS on Qwen3-30B-A3B-2507 shows small math gains and a large loss for one MCTS baseline (d17); DeepSeek-R1 report says MCTS self-improvement failed and native compute follows difficulty (d13); parallel teams shows a frontier model's best-of-N curve flat (d14). Needs our own run.
5. Value self-consistency vs more branches at equal cost: OPEN. Koh (d05) gives the value-SC ladder (28.5, 32.5, 37.0) but no branch-matched control.
6. Reflections inside a tree, by feedback type: PARTLY. d15 and d03 suggest reflection effects may be static-hint or retry effects and can hurt when the hint mismatches; no tree-internal ablation by feedback type was found.
7. Reversion and irreversible actions: CLOSED as design guidance (d06, d07): reset-and-replay, gate destructive actions, no empirical test on destructive tasks.
8. Difficulty gating with a prompted estimate: PARTLY. Prompted per-step branch gate is cheap and works on math (d11); per-item difficulty by sampling is costly (d10); trained predictor works but needs training (d12). No prompted per-item gate was measured on code or web agents.
9. Independent re-implementations of LATS: PARTLY. One failed replication on HumanEval (d01, d02: 88.0 vs 92.7 for GPT-4; 80.4 vs 83.8 for GPT-3.5; evaluation changes in original). No independent HotPotQA or WebShop re-run found in 4 targeted searches; LangGraph or tutorial ports were not found as measured studies.
10. Program-owned tree with a small model as slot-filler: PARTLY. ReAcTree (d18) supports it (8B about 70B flat ReAct) but is a task-hierarchy tree, and a complex format hurt at 7B. SWE-Search small-model results (earlier evidence) are the other data point.

Corrections made to earlier claims: K01 moved to contested; K02 to established (three sources); K04 to contested; K09 and K12 to established.

Sources opened as full PDF text this pass: Kapoor 2407.01502, Koh 2407.01476, LATS 2310.04406 (re-read), Snell 2408.03314, Karthikeyan 2502.12094, DARS 2503.14269, Chain-in-Tree 2509.25835, DST 2603.20267, DeepSeek-R1 2501.12948, parallel teams 2611.09798, self-repair 2611.06863, PRISM-MCTS 2604.05424, ReAcTree 2511.02424, R-MCTS 2410.02052. Table cells from PRISM, DARS, R-MCTS and ToolTalk were column-shifted in text; mappings inferred and flagged in limits. Not verified: SEAG (snippet only), ReTreVal, SGA-MCTS beyond abstract.
