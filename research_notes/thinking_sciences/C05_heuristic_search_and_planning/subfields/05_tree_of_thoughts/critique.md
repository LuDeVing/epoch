# Critique: Tree of Thoughts (C05.05)

Cross-check done by re-opening the PDFs (pdftotext) of Yao 2305.10601, Token Economies 2406.06461, XoT 2311.04254, AoT 2308.10379, GoT 2308.09687, Stechly 2402.08115, Huang 2310.01798, Katz 2404.11833. Files deleted afterwards.

## Confirmed (re-opened)
- Yao Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, IO+Refine 27, ToT b=1 45, b=5 74. Confirmed.
- Yao crosswords: ToT 78/60/20, oracle 82.4/67.5/35, no prune 65.4/41.5/5, no backtrack 54.6/20/5; IO 38.7/14/0, CoT 40.6/15.6/1. Confirmed.
- Yao Creative Writing 6.19/6.93/7.56; humans 41 ToT, 21 CoT, 38 similar; refine 7.67/7.91. Confirmed.
- Yao cost table: IO best-of-100 1.8k tokens, $0.13, 33%; CoT best-of-100 6.7k, $0.47, 49%; ToT 5.5k, $0.74, 74%. Ordering confirmed (PDF layout is garbled but consistent).
- Huang: CSQA 75.8 -> 38.1 -> 41.8, GSM8K kept answer 74.7%. Confirmed.
- Stechly: Game of 24 verifier 87.0% (3567/4100), FP 10.4% (320/3071), FN 20.7% (213/1029). Confirmed.
- AoT: ToT 69%, 109.1 queries, 13,900 prompt tokens; AoT 71%, 1 query, 5,450; crossword ToT 46.5% (>200 queries), AoT 52%, CoT-SC 15.6%. Confirmed.
- GoT: 62% better than ToT and over 31% cheaper; 70% over CoT; at P=64 median error 65% and 83% (below CoT and IO). Confirmed.
- XoT: ToT b=1 34.31, b=3 60.58 (GPT-4); XoT 85.40 with 3 revisions. Confirmed.
- Katz: 1362 of 1362 correct (1361 solvable + 1 flagged unsolvable), 1.92-6.83 s, 1.2 interactions for successor function. Confirmed.

## Corrections made
1. b14 (Token Economies evaluator ablation) mixed metrics. Table 3 shows top-1 and best-of-all. GPT-4/GPT-4 b=5 is 74% top-1 (76% best-of-all); GPT-4 proposer + GPT-3.5 evaluator is 68% top-1 (72% best-of-all). The 76% vs 72% in b14 are best-of-all values. Claim K08 uses both labelled.
2. b13/a13 said "SC beats ToT with GPT-3.5". The text says so, but the table gives ToT top-1 25% vs CoT-100 top-1 4%, and best-of-all 35% vs 46%. The winner depends on the metric. Claim K07 flags this.
3. Token Economies ToT b=1 is 65% (GPT-4) but Yao says 45% and XoT says 34.3%. Three values for the same nominal setting (K02).
4. Evidence c09 says GoT cuts error 70% vs CoT; a17 says 65% below CoT at 64 numbers. Both are in the paper (70% overall intro claim, 65% at P=64). Not a conflict.
5. Katz crossword "20/20" assumed candidate answers for each clue; do not read it as a like-for-like crossword solve.

## Contradictions between sources
- Original ToT 74% vs re-runs 69 / 60.6 / 77 (b=3). Larger spread at b=1 (34 to 65). Prompt details and test sets differ.
- FoT table copies ToT's 74% (GPT-4) next to its own Llama3-8B numbers, where base ToT is 10.58%. The table mixes models.
- Token Economies says ToT wins with GPT-4 under matched budget; Katz and AoT say the same score is reached far cheaper by other means.

## Weak spots
- Almost all ToT evidence is Game of 24, plus 20 crossword games, plus invented creative writing. No standard benchmark (MATH, code, open QA) shows ToT itself winning at equal tokens; the later papers use PRM-based search instead.
- Baselines in the original are not compute-matched (best-of-100 oracle is the only matched-ish row).
- No peer-reviewed replication on a different task for plain prompt-only ToT; LATS, RAP, FoT are by authors of the new method.
- The weak-model result (GPT-3.5) is the more relevant case for small agents and is the weakest.

## Seen only in snippets or partly read
- c26 (CS224N project) and c27 (Meta-CoT) were not opened; use as leads only.
- a16/c10 (Tree of Uncertain Thoughts): table cells not read; only text gains.
- a20/c25 (Besta survey): intro only.
- b24/c24 (DeepSeek-R1): negative result in prose, no numbers.
- Snell, Wu, Koh numbers were not re-opened this pass.

## GAPS
1. Does a tree at S6 beat self-consistency at equal tokens for a current (2025-26) frontier model on non-toy tasks (math, code, open reasoning)? No evidence found with prompt-only ToT.
2. Do reasoning models (o1/R1 class) gain anything from an external ToT on top of their internal chain? Any measured study?
3. How good is a prompt-only value/evaluate step as a function of task type (checkable vs uncheckable)? Need false-positive rate of the scorer on idea-generation tasks, not just Game of 24.
4. What is the best tree width/depth rule by difficulty and budget without a trained reward model (Snell's finding needs a PRM)?
5. Does letting the model write code for successor/goal test (Thought of Search) beat per-node LLM calls on non-formal tasks, and what share of our tasks are formalisable?
6. Are there independent replications of ToT on Creative Writing-like open tasks with an independent judge (not GPT-4 self-judging)?
7. Is the Forest-of-Thought / multi-tree gain real at equal tokens with a fixed base model, outside the method authors?
8. How much of the ToT gain is due to the state rewrite per step (RAP world-model) versus branching? An ablation on the same task is missing.
9. How do ToT-style gains change with scorer diversity (different model or prompt as evaluator) versus the same model scoring itself?

## Gap search results (evidence_d.jsonl, d01-d20; claims K24-K30 added)

Search budget was used up early (1 WebSearch worked), arXiv API rate-limited, so work was done by opening papers directly. No ToT-on-reasoning-model study and no third-party FoT or creative-writing ToT replication was found; those are "not found", not "proved absent".

1. Tree vs self-consistency at equal tokens, current model, non-toy: PARTLY CLOSED. Sys2Bench (d01) on GPT-4o: ToT wins only Game of 24 (62 vs SC 18); loses on GSM8K, ProntoQA, HotPotQA, Blocksworld. Mind Evolution and PlanSearch (d04, d05) beat equal-candidate sampling but need a checker. SC@5 in Sys2Bench is not token-matched. No prompt-only, LLM-scored tree win on open reasoning found.
2. Reasoning models plus external ToT: STILL OPEN, with hints. Plain o1 beats ToT on GPT-4o (d02). Outer search on o3-mini helps on a 100-question HLE sample (d03); o1-mini gains 0.5 from PlanSearch (d05); QwQ gains 0.6 from FoT on MATH500 (d20); short-chain voting is a strong baseline (d10, d11). No clean test.
3. Scorer reliability by task type: MOSTLY CLOSED in direction. Checkable: works (Game of 24, 87% verifier accuracy, K10). Uncheckable: LLM judge 53.3% vs chance 50 on research ideas (d15), no correlation with experts on creative writing (d16), vote/RM plateau (d06). A false-positive rate for idea scoring was not measured by anyone found.
4. Width/depth rule without a reward model: PARTLY OPEN. Agreement-based early stop (d09, 3.2x savings) and Snell's difficulty rule (d08) exist; Snell and Wu (d07) need a trained scorer. No prompt-only difficulty-routed tree rule tested.
5. Code for successor/goal test: CLOSED in scope. Wins only for formal domains with meaningful names and tests (d17, d18). Share of our tasks that qualify: small; not measured.
6. Independent creative-writing ToT replication: OPEN. Only indirect evidence that LLM judges are weak there (d16).
7. Multi-tree gain independent: OPEN. FoT is authors-only; gains mixed with self-correction (d20).
8. State rewrite vs branching: OPEN. RAP(1) beats CoT, hinting at structure effect, but no ablation (d19).
9. Scorer diversity: PARTLY CLOSED. Self-preference bias (d13), juries beat one judge (d14), method diversity helps reasoning models (d03, d12). Not tested inside a tree.
