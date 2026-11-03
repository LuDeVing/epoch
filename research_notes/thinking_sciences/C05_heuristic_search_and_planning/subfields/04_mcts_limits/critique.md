# C05.04 MCTS limits: cross-check critique

## Corrections made (sources re-opened this session)
1. Wang et al. 2023 (arXiv 2211.00241): the 72% win rate at 10^7 victim visits is over only 50 games and is against Latest (the undefended net). 82% at 10^6 visits (50 games). The 95.7% figure (1007/1052, 4096 visits) is vs Latest-def; 97.3% (1000 games) vs undefended Latest at 4096 visits; 1048/1048 vs no-search Latest-def. Lines a08, a10, b12 blurred these. Treat 72% as a small-sample number.
2. Ramanujan et al. 2010: 7-10% (semi-random, 31 ply), up to 15% (47 ply), about 12% (grandmaster, 47 ply) confirmed. Table 1 has four boards with traps at levels 1, 3, 5, 7; a03's extra row is a different board. UCT clearly detects only the level-1 trap and partly level 3.
3. Coquelin and Munos: double exponential in D; D=20 gives about 10^156837 confirmed. It is a worst-case constructed tree.
4. Inoue et al. (AB-MCTS) table confirmed exactly (ARC Pass@2 sampling 15.0/18.6 vs MCTS 9.0/14.0; avg rank sampling 3.5, MCTS 4.2). Correction: standard MCTS beats sampling on LiveCodeBench with DeepSeek-V3 (43.2 vs 40.7) and CodeContest with DeepSeek-V3 (43.8 vs 43.2). So "MCTS does not beat sampling" holds for ARC and GPT-4o code, not everywhere. The MLE-Bench rank (MCTS 3.3) uses only three competitions, GPT-4o, n=1.
5. Zhang et al. cost-awareness (arXiv 2505.14656): MCTS tight-budget row 1.00 0.92 0.50 0.11 0.05 0.00 avg 0.43, Bi-Search avg 0.45, failure shares 98/92/52% exhaustion and 48/92% budget violation all confirmed. Year differs between b17 (2025) and c18 (2026): same paper, versions.
6. Orseau et al. Sokoban table confirmed (Uniform 88; LubyTS(512,32) 884 +/- 4, 11.5M expansions; LevinTS 1000, 6.6M; LAMA 1000, 3.15M).
7. Hao et al. RAP: RAP(10) 1.00/0.86/0.26 and RAP(20) 1.00/0.88/0.42 confirmed.
Not re-opened (rely on earlier agents): Baier and Winands win rates, Snell, Wu REBASE FLOPs, DeepSeek-R1 appendix, Stroebl, Tseng exact settings.

## Contradictions between sources
- b21 (Chen et al.): with a PRM, MCTS beats beam, best-of-N and voting. a12/c15/b15/a13 show tree search not beating sampling. Likely reconciled by verifier quality, domain (code with tests) and budget; not proven.
- b08: hybrids help most in Catch the Lion, yet alpha-beta still beats the hybrid there (17.4% hybrid win). Repairing traps helps MCTS; it does not make it beat exhaustive search.
- LATS (a17) is strong on HumanEval with test feedback; AB-MCTS shows ARC (no feedback) favors plain sampling.
- Ramanujan and Selman 2011 (b06): UCT beats minimax in Mancala, so UCT is not intrinsically weak; the trap explanation is game-dependent.
- c16: backtracking wins Sudoku, loses CountDown; no single search style.

## Weak spots
- Trap evidence is chess-only, 2010-era UCT with random playouts; the utility table rests on four boards. No direct measurement of trap blindness in LLM tree search.
- Adversarial Go is one lab and one network lineage.
- Token accounting differs across LLM papers (generations, FLOPs, node expansions), so "equal budget" is not uniform.
- PAC-CF (b23/c25) is a 2026 preprint with a CI excluding zero at only two budgets.
- b and c files overlap; claims count independent sources by paper group, not by line.
- b20 and c22 are the same Qwen paper.

## Only seen in snippets or abstract
- c24 (PRM math to code, 2506.00027) and c30 (Xie et al.) not read beyond abstract. a21-a24 (Kocsis and Szepesvari, Auer et al., Browne et al., Silver 2016) and Althofer 2012 not opened. c03 Mancala win-rate tables not extracted.

## GAPS
1. Does trap blindness occur in LLM reasoning search? Build items with a single fatal refutation step and measure whether sampled-average or LLM-judge scoring accepts it, versus an exhaustive code check.
2. At what task difficulty and verifier false-positive rate does tree search beat plain sampling at equal total tokens (rollouts included)?
3. Does a shallow exhaustive verification pass added to a sampled chain recover most of the loss, as minimax hybrids do in games, for LLM tasks?
4. Where should depth be capped? Success falls from 0.92 to 0.11 between plan length 4 and 8; is there a depth where reframing beats deeper search?
5. How task-specific are search parameters (exploration constant, width, rollout count) for LLM tasks, and how sensitive is accuracy to them?
6. Is the evaluator blind spot (PRM or LLM judge) a fixed class that survives more search and patching, as with cyclic groups in Go? Needs a held-out adversarial evaluation of our own evaluator.
7. Which of the DeepSeek-R1, rStar and ReST-MCTS results survive when the value signal is code-checked rather than learned?
8. Has anyone measured trap-state density in natural-language reasoning or code-debugging trees, so we know when selective expansion is risky?
9. Do MCTS vs sampling comparisons on 2025-26 long-chain reasoning models still favor sampling, since most data use GPT-4o or DeepSeek-V3?

## Gap search results
Sources opened this pass (full PDF text): ProcessBench, Zhao et al. verification scaling, Stechly et al., Gao et al. overoptimization, Reward Under Attack, One Token to Fool, Large Language Monkeys, rStar-Math, ReSCALE, SC-MCTS*, Know Thy Reasoner, Lost at the Beginning, FoE (intro and Table 1), Illusion of Thinking, Joo and Klabjan (abstract and intro). Evidence is in evidence_d.jsonl (d01-d16). Arxiv and Semantic Scholar APIs returned 429, so discovery used 6 web searches plus direct PDF fetches.

1. LLM trap blindness (single fatal step): STAYED OPEN for a direct test. Partial: ProcessBench (d01) and Zhao (d02) show scorers miss earliest errors on hard items, o1-preview misses 20-30% of wrong responses. No paper builds chess-style fatal-refutation items. Keep the agent test.
2. Tree search vs sampling crossover: PARTLY CLOSED. No numeric crossover. Brackets: sound code check favours sampling (d03, d07); weak LLM or PRM judges cap everything (d02, d06). Working rule only.
3. Shallow verification pass recovering the loss: CLOSED for planning/code-style tasks. A sound external check yields large gains (Game of 24 5% to 36-38%), an LLM self-check does not (d03); verification scaling beats voting (d02). No equivalent of a minimax hybrid was measured on open-ended reasoning.
4. Depth cap: PARTLY CLOSED. Collapse depends on branching complexity not length (d15, disputed), and noisy scorers make deep prefixes more often spuriously top-ranked (d14). No measured optimum depth.
5. Parameter sensitivity: PARTLY CLOSED. Default UCT C failed until tuned (+5.27, d10); root selection changes the sign of scaling (d09). Only small models and single tasks.
6. Fixed evaluator blind-spot class: PARTLY CLOSED for PRMs and judges (d05, d06, d04): exploitable, universal suffixes, 43% style share. Not tested on our evaluator; the Go-style "patch and find the next one" result is not replicated for LLM judges (Master-RM fix held for its own attack family only).
7. R1, rStar, ReST-MCTS with code-checked values: PARTLY CLOSED. rStar-Math (d08) works with step values trained from code-verified outcomes (MCTS PPM 89.4 MATH vs best-of-N ORM 82.6, not budget-matched; Q-value PRM 88.2). ReST-MCTS and R1 not re-opened. K09 annotated.
8. Trap density in NL or code trees: STAYED OPEN. Closest is recoverability from a forced wrong first step (d12: 94.8 to 28.5 for R1-Distill-7B; 100 to 78.7 for Qwen3-235B) and FoE (d13). No natural frequency.
9. 2025-26 reasoning models: PARTLY CLOSED. Know Thy Reasoner (d11) compares depth vs iid sampling at equal tokens on Qwen3, OLMo-3, Nemotron-3: depth helps instruct and RLVR (up to +39%), hurts base (to -29%). Still no clean MCTS vs sampling on frontier reasoning models.

Claims changed: K14 to established (4 sources); K15, K08, K13, K20, K24 gained evidence; K09 annotated with the rStar counterpoint. New claims K25-K31.
Caveats: all 2026 items are preprints; d13 and d14 only partly read; d11 uses pass@16 and possible token truncation.
