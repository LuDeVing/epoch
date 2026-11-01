# Critique: E16.09 Computer chess and game AI

## Numbers re-opened this session (arXiv full text, pdftotext)
All confirmed, none changed:
1. AlphaZero vs Stockfish, 100 games, 1 min/move, 0 losses (1712.01815). The 28W/72D split sits in a table image and was not in the text layer; the 0 losses, 80k vs 70M positions/s and the Figure 2 claim are in the text.
2. Tree of Thoughts Game of 24: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74 (2305.10601).
3. Ruoss et al.: 270M = tournament Elo 2299, blitz 2895 vs humans, puzzles 95.4; 136M 2259/94.5; 9M 2025/88.9; oracle 2713 (2402.04494).
4. KataGo adversary: under 14% compute, >99% no search, >97% superhuman search (2211.00241). Detail added: the 72% at 10^7 visits is over only 50 games, so its interval is wide.
5. RAP Blocksworld RAP(20) 1.00/0.88/0.42 (2305.14992).
6. Schultz et al.: external Elo 2923 / 2875; MAV+MCTS 500 sims 3170, 1000 sims 3191; 100 sims = +68 internal Elo; model is 2.7B (2412.12119).
7. Snell: "up to 4x less test-time compute" and "14x larger model" confirmed (2408.03314).
8. Jones: "additional 10x train-time compute, about 15x test-time" confirmed (2104.03113).
9. LATS HumanEval GPT-4 92.7, GPT-3.5 83.8 confirmed (2310.04406).
10. Table in 1712.01815 reports "losing eight games to Elmo", consistent with b01.
Note: a-file row a16 says "33% relative gain over GPT-4 CoT"; not re-checked. A path error was caught: arXiv 2402.12875 is a different paper (CoT serial problems), not Snell; correct id is 2408.03314. Row ids were not affected.

## Contradictions
- Search value at equal compute. Gains reported for ToT, RAP, LATS, rStar-Math versus Snell (lookahead/MCTS under-performed best-of-N; beam search worsened on easy questions) and Feng (advantage over CoT-SC with ORM vote shrank on GSM8K). Differences: ToT/RAP compare to weak CoT, not best-of-N at equal tokens (ToT does report CoT best-of-100 49% vs 74%, the fairest line).
- LATS GPT-4: 92.7 vs Reflexion 91.0 is a 1.7 point gap; the GPT-3.5 gap (83.8 vs 68.1) is much larger, so the gain shrinks as the base model gets stronger.
- Elo anchors differ across Ruoss (2895 Lichess vs humans), Schultz (2923 CCRL-anchored) and the 2299 vs bots figure; "grandmaster level" is not one number.
- AlphaZero 2017 (28-0 loss, Stockfish handicapped: 1 GB hash, 1 min/move) versus the 2018 Science match (155W 6L 839D, fairer). Win margin shrank; direction held.

## Weak spots
- Most chess/Go results need training; only ToT, RAP-style, LATS and internal-search results can be run on a frozen LLM.
- Single-source status for many LLM rows (one paper each, no independent replication).
- Hex scaling law (Jones) is one game, one algorithm.
- Many Elo values are model-estimated, not match-measured against fixed opponents.

## Seen only in snippets or not opened
b22 ReST-MCTS* and b28 RAP abstract (opened:false); c19-c25 (Deep Blue paper, AlphaGo 2016, UCT paper, Knuth-Moore, Carlini 2023, Kaggle Game Arena, Stockfish NNUE/Lc0) not opened, so K02 and K19 rely partly on memory. c10, c11 exact tables not extracted.

## GAPS
1. At equal tokens, does ToT-style or MCTS-style search beat plain best-of-N with a verifier on a frozen frontier LLM (2025-2026 models), and on which task types does it lose?
2. How does the benefit of search shrink as the base model gets stronger (LATS 1.7 vs 15.7 points; Jones' 15x trade)? Is there a model strength above which search at S6 is not worth the tokens?
3. How well does the LLM's own value estimate predict real outcomes in search (calibration, AlphaGo game-4 style collapse)? Need measured value-vs-outcome curves.
4. Does reasoning-model training (o1/R1-style long chains) already contain implicit search, making an explicit external tree redundant? Direct comparisons 2025-2026.
5. Which branching factor and evaluation cheapness make MCTS beat alpha-beta-style exhaustive pruning for LLM tasks (the Go vs chess lesson)?
6. Do adversarial blind spots (KataGo cyclic attacks) have analogues in LLM tree search, and do verifier checks catch them?
7. Replications of LLM chess and game results (Carlini 1750 Elo, Kaggle Game Arena, GTBench): actual illegal-move rates and Elo in 2025-2026.
8. What is the cost-optimal allocation between generating more branches and a stronger evaluator (generator vs evaluator split in b17), at fixed budget?
9. Does searchless distillation (cached answers) generalise to distribution shift (Fischer random drop) in LLM agents' memory?

## Gap search results (round 2)

Method: arXiv search APIs and the web search tool were rate-limited or out of budget, so sources were reached by known arXiv ids and direct page fetches. 24 evidence lines in evidence_d.jsonl (d01-d24, all opened: full-text PDFs read with pdftotext, plus blog and abstract pages). Claims K24-K33 added; K08, K13, K17, K20, K22, K23 got extra evidence ids. No earlier claim was refuted.

Closed or mostly closed:
- Gap 2 (benefit shrinks with model strength): partly closed for math with process reward models. Liu et al. (d06): for 72B policies best-of-N is best at every difficulty level; structured search helps small policies and hard items. Snell (d07): beam search hurts on easy items. Koh (d10) does not show shrinkage for agents: absolute gains were similar (about +9 and +7.5 points), relative gain larger for the weaker model. No threshold model strength was measured on 2025-26 frontier models.
- Gap 5 (branching and evaluation cost): closed as a rule of thumb (K29), not as a controlled MCTS vs alpha-beta experiment on an LLM task.
- Gap 7 (replication of LLM chess): mostly closed. LLM Chess (d16, d17): best model o3 (low) about 758 Elo, 71.1% of 76 models had abnormal finishes, 62.1% of failed moves were format/tool errors and 37.9% illegal moves. Dynomight (d18): one model strong, chat models weak. Carlini (d19): no Elo on the page; the "about 1750 Elo" figure in earlier notes could not be found there. Kaggle Game Arena (d20): announcement only, no Elo or illegal-move numbers retrieved.

Partly closed:
- Gap 1 (search vs best-of-N at equal tokens): Koh (d09) shows search beats re-ranking at equal compute in resettable web tasks. Wu (d08) shows classic MCTS loses to rollout-free trees. Liu (d06) shows best-of-N wins for large policies. No equal-token test on a 2025-26 frontier model for single-shot tasks was found. Open.
- Gap 3 (value calibration): Kadavath (d14) gives calibration for P(True) in distribution; Snell (d07) and Gao (d13) give evaluator-exploitation shapes. No measured value-vs-outcome curve over LLM search states found. Open.
- Gap 4 (implicit search in reasoning models): Yue (d03) and R1 (d02) say RL sharpens sampling and wide sampling still helps; Illusion of Thinking (d04) is contested by Lawsen (d05); Valmeekam (d15) shows long-horizon gaps. No head-to-head of an external tree against a reasoning model on one task from 2025-26 was found. Open but leaning: explicit breadth is not redundant, explicit deep trees untested.
- Gap 8 (generator vs evaluator split): Gao (d13) and Liu (d06) show evaluator quality and policy size interact; PlanSearch (d12) shows generator diversity matters. No fixed-budget optimum found. Open.

Still open:
- Gap 6 (analogues of KataGo cyclic attacks in LLM tree search): no direct study found. Tseng (d23) confirms defences fail in Go. Value exploitation (Snell, Gao) is the nearest analogue. Whether verifier checks catch it is untested.
- Gap 9 (searchless distillation under shift in agent memory): only Ruoss (d22), 515 Elo drop. No LLM-agent memory test found.

Caveats: the Illusion of Thinking collapse is disputed; the Liu 72B result is for open models of early 2025; LLM Chess Elo uses a different anchor scale than Ruoss or Schultz; Lawsen and Kaggle pages were read as abstract or announcement only.
