# C01.07 Search over thoughts: cross-check critique

## Re-opened sources (full PDF text, this session)
Confirmed exactly: ToT (Yao 2023: 7.3/4.0/9.0/45/74%, best-of-100 CoT 49%, $0.74 vs $0.47, ~60% fail at step 1, GSM8K 90 vs 86, StrategyQA 83 vs 82); AoT (Sel: ToT 69%, 109.1 queries, AoT 71%, 1 query; crosswords 46.5% vs 52%; fine-tune CoT 12% vs AoT 63%); Stechly (150 direct queries + sound verifier = 70% vs 74%); Katz (1361/1362, 100%, ToT 75% on 100 problems, 4573 states); Chen (>=90% discriminator, tree search at least 10-20x slower, +30.2 and +8.4 points); LATS (92.7, 83.8, 0.63, 0.44); RAP (0.86/0.42/0.26, 51.6/48.6, 33% relative); TS-LLM (64.8, 52.5, 21.0, 52.3 CoT-SC with reward model, 41.4 greedy); Koh (18.9 to 26.4, 15.0 to 19.2); PlanSearch (77.0, 60.6, 41.4); Snell ("up to 4x less compute", 14x larger model); Wang et al. Token Economies Table 3.

## Corrections and refinements
1. Wang Table 3 (Game of 24, GPT-4): ToT b=5 Top1 0.74, b=3 0.77, b=1 0.65, evaluate-once 0.73, random evaluator 0.0, GPT-3.5/GPT-3.5 0.25, GPT-4 propose + GPT-3.5 evaluate 0.68, GPT-3.5 propose + GPT-4 evaluate 0.30. Text says 72% at $33.53 (GPT-3.5 evaluator) vs 76% at $159.87 (GPT-4 evaluator). Evidence c12 says "evaluate once 0.73" as if a drop; it is nearly equal on Top1 but total accuracy falls (0.352 vs 0.4). Gain is cost, not accuracy.
2. Wang's ToT b=1 is 0.65, but Yao's b=1 is 45%. Same task, same model family, 20 points apart. Implementation detail matters more than breadth.
3. Yao's ToT b=5 beats Wang's own b=3 by nothing (0.74 vs 0.77): breadth above 3 is not shown to help.
4. a12 compares CoT GPT-4 92.0 to search+PAL Codex 80.2 across model generations; use as direction only.
5. Cost rows in the ToT PDF are column-garbled in text; pairing checked against the success column (49% / 74%), consistent.
6. c22 (Hamm and Ajanovic 2026), c19 detail beyond abstract, c20 (rStar), c23, c14 were not re-opened here. a24 and a25 are second-hand.

## Contradictions
- ToT Game of 24 ranges 69-77% for GPT-4 and 19-20% for GPT-3.5 across authors; Katz reports ToT as 75%.
- Yao says ToT beats 100 CoT samples; Stechly and Wang show that with a sound verifier or equal tokens, flat sampling nearly matches ToT. The comparison depends on whether the sampling arm is allowed a verifier.
- LATS reports big gains over ToT/RAP, but the baselines were re-run by the authors with fewer samples; LATS uses more nodes (n=5, k=30-50).
- Snell finds beam search beats best-of-N at moderate difficulty; Chen and TS-LLM find sampling competitive. Difference: trained PRM vs prompted judge.

## Weak spots
- Nearly all gains are on Game of 24, crosswords, Blocksworld, Sudoku, sorting, Countdown: closed puzzles with code-checkable states. Almost nothing on open-ended ideation.
- Small N: 20 crossword games, 10 Sudoku puzzles per size, 100 Game-of-24 items, one run each; no confidence intervals in ToT, Long, AoT.
- Most 2023 numbers are GPT-3.5/GPT-4 (2023) or Codex. Reasoning models (o1, R1-class) with built-in long chains are barely covered; R1 reports MCTS failing (no numbers).
- Evidence files a, b, c overlap heavily (same ~15 papers); claim independence counts distinct papers, not lines.

## Seen only in snippets or second-hand
Newell and Simon (1972), Wang self-consistency original, Besta survey (abstract and intro only), Hamm and Ajanovic, rStar, C-ToT pairwise, CoT-decoding table (garbled).

## GAPS
1. At equal total tokens, with a prompted LLM judge only, does any tree/graph search beat sample-and-select on the 2025-2026 reasoning models (o-series, R1, Claude thinking) on tasks that are NOT code-checkable?
2. How accurate must the state judge be, per task, for branching to pay at equal tokens (Chen gives about 90% for SQL/math), and can we measure it cheaply online before deciding to branch?
3. Does an idea tree improve human-rated novelty or usefulness on open-ended ideation (blind raters, length-normalised), or only a GPT-4 coherence score?
4. How much of the gain comes from decomposition plus merge (GoT) rather than search, and what is the smallest code-run merge operator that keeps it?
5. Is a single-call search trace (AoT) robust beyond arithmetic puzzles and crosswords, and does it silently skip branches?
6. Does letting the LLM write the successor and goal-test code (Thought of Search) extend to ill-formed domains, and how do we detect when it cannot be formalised?
7. What is the right trigger for branching (step-1 disagreement, verifier failure, difficulty bin), and what is the false-trigger cost on easy items where beam search hurts (Snell levels 1-2)?
8. Is pruning revisable cheaply: how often does a false "impossible" verdict remove the right branch (crossword 3 of 4 solved boards missed), and does keeping pruned nodes in a reserve list recover them?
9. Do trees help more with a stronger generator and a cheaper evaluator in reasoning models (split roles), at equal dollar cost?
10. Why does breadth stop helping above b=3 in independent runs, and does depth cap (Blocksworld decay with length) interact with it?

## Gap search results (evidence_d.jsonl d01-d17, claims K20-K28)
Source limits: WebSearch gave one working query before the shared budget ran out; arXiv API, Semantic Scholar and OpenAlex returned rate-limit errors. Sources came from that one search and from known arXiv ids, then were read as full PDF text.

1. Reasoning models, equal tokens, no code check: PARTLY CLOSED, leaning "sample first". Wang 2025 (R1-distills, GPQA, LiveCodeBench), Ghosal 2025 and Zeng 2025: majority voting beats search and revision. Only BAVT (2026, GPT-OSS-20B, tool QA) shows a tree beating equal-budget voting, and only with a value signal. No o-series, Claude-thinking or ToT/graph arm found. Sharma 2025 disagrees (4096-token cap confound). See K20-K22.
2. Judge accuracy needed and online measurement: STAYS OPEN. ProcessBench and Si give per-task judge accuracy (87.9 vs 61.9 F1; 43-53% on ideas); Chen's 90% remains the only threshold. No paper measures judge accuracy online before branching. A cheap test is proposed in K23 (20-50 labelled items), untested.
3. Idea tree and human novelty: STAYS OPEN. Blind human raters favour flat overgenerate-and-rank (5.64 vs 4.84); no tree arm found. The judge is near chance and 4000 samples give about 200 unique ideas (K25).
4. GoT decomposition vs search: STAYS OPEN. GoT has no ablation and used only GPT-3.5 (K27).
5. Single-call trace (AoT) robustness: STAYS OPEN. No new study found; nothing opened on skipped branches.
6. Formalisability of tasks: PARTLY CLOSED. Katz round counts (1.0-2.8) and GIF-MCTS limits (deterministic, fully observable) give a usable gate (K26). Not tested on ill-formed domains.
7. Trigger and false-trigger cost: PARTLY CLOSED. AB-MCTS: sampling wins at small budget on ARC, search wins after plateau (K24); BAVT: exploit-late scheduling adds 0.079 EM. No paper measures the cost of false triggers on easy items.
8. False "impossible" pruning and reserve list: STAYS OPEN. Nothing found beyond Katz noting that LLM-proposed crossword candidates may omit the right word.
9. Split roles at equal dollar cost: STAYS OPEN. Only Wang (earlier) and BAVT cost tables on a single backbone; no new split-role test.
10. Why breadth stops at b=3: PARTLY CLOSED as a hypothesis. Duplication (200 of 4000 unique) and instruct-model mode collapse (0.289 to 0.293) are candidate causes (K28); the depth-cap interaction is untested.

New corrections: the Besta GoT paper compares only against its own ToT variants and only on GPT-3.5. The Katz crossword result assumes 10 candidate answers per clue including the right one. Oracle-label figures from Huang were column-garbled and are approximate.
