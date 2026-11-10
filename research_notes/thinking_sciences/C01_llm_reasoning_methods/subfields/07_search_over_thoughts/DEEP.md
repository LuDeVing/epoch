# Search over thoughts: deep document

*Subfield C01.07. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K28), critique.md in this folder. Ids like a02, c12, d07 are evidence lines. Numbers are as the papers report them unless marked. Most evidence lines were read as full PDF text; a few were not (see section 11).*

## 1. What it is

Search over thoughts means the model does not write one chain of reasoning. It writes several candidate next steps, a judge scores the partial states, and a controller keeps some, drops others and may go back. The states form a tree or a graph.

Four design choices define any method in this family (a01):
1. **Thought step:** what one node is (an equation, a word, a plan line, a web action).
2. **Generator:** how children are made (sample independently, or propose several in one prompt).
3. **State evaluator:** how a node gets a value (model prompt "sure / maybe / impossible", a vote, a learned value net, a reward model, or code).
4. **Search rule:** BFS with beam b, DFS with a value threshold, MCTS, beam search, A*-like or reward-balanced expansion.

Chain of thought, self-consistency (CoT-SC), best-of-N and self-refine are special cases: trees of small depth or breadth (a01). So the real question is never "tree or no tree". It is: at equal tokens, does branching with a judge beat sampling whole answers and picking one?

For our agent this is the S6 idea tree: at an impasse the program grows a tree where each child applies one operator (O1-O8), code tests each child, then expands the best or prunes. This document tells us when that is worth the tokens.

Links to other subfields run in parallel (not covered here): Tree of Thoughts (C05), Language Agent Tree Search, Neural and LLM proof search, Automated planning, Compression at inference time, Dual-process theory, Calibration and overconfidence, Creative problem solving, Cognitive conflict and impasse.

## 2. History and theories in depth

**Human problem solving as search.** Newell and Simon (1972, Human Problem Solving) framed thinking as search through a problem space of states and operators, guided by heuristics. ToT cites this directly and also dual-process theory (fast proposal, slow deliberate evaluation) (a24, second-hand only). Classical AI gave A* (Hart et al. 1968) and MCTS; ToT names them but did not test them (a24).

**2022-2023: flat sampling.** CoT and CoT-SC (Wang et al.) sample whole chains and vote. They have no way to drop a bad first step. On Game of 24 about 60% of CoT chains were already dead after step 1 (a03). That is the gap ToT targets.

**May 2023: ToT and kin.** Yao et al. ToT (a01-a07): BFS/DFS with model-written proposals and model-written value judgments. Long (2023) published a similar "ToT solver" with a rule-based checker on Sudoku (a08, b06). RAP (Hao et al. 2023) used the LLM as both policy and world model, with MCTS on Blocksworld and GSM8K (a09, a10). Xie et al. (2023) used self-evaluation guided beam search on Codex (a11, a12). Aug 2023: Graph of Thoughts (Besta) added merge and refine operations so thoughts can combine (a13, a14). Algorithm of Thoughts (Sel) put a search trace inside one prompt (a15). LATS (Zhou) added MCTS plus reflection for agents (b10, b11).

**Late 2023-2024: skeptics and learned values.** TS-LLM (Feng et al.) showed prompted values are weak and learned value nets are strong (a17, a18). Chen et al. found tree search with LLM discriminators 10-20x slower than re-ranking with negligible gain (b13). Stechly et al. showed 150 direct queries plus a sound verifier nearly match ToT (c13). Wang et al. "Token Economies" re-ran ToT with budgets (c12). Katz et al. "Thought of Search" had the LLM write successor and goal-test code and ran plain BFS: 100% on Game of 24 at about $40-scale cost versus an estimated $14,000-16,000 for RAP and LATS (b16, d16). Training on search traces (Stream of Search, Searchformer) showed dead ends help, but only through training (a19, a20).

**2024-2025: inference scaling.** Snell et al. showed search against a process reward model (PRM) is difficulty dependent (a21, b14, c15). Wu et al. found cheap rollout-free REBASE beats MCTS (a22, b15). DeepSeek-R1 reported MCTS failing in token space (b18). Planning in natural language (PlanSearch) moved search from steps to ideas (c19). Tree search for web agents gave real gains (a23).

**2025-2026: reasoning models.** With long built-in chains, studies on R1-distills, QwQ and others found simple voting equals or beats search and revision (d03-d05). Sequential versus parallel is contested and depends on chain caps (d06). AB-MCTS showed the best arm flips with budget (d07, d08). BAVT (2026) is the only found tree that beat equal-budget voting on a reasoning model, and only with a value signal (d01, d02). Novelty-based ToT (Hamm and Ajanovic 2026) tuned ToT on Blocksworld with a thinking-mode model (c22).

**Competing explanations of why ToT worked.**
- *Search itself helps* (Yao): pruning at step 1 and backtracking.
- *Code does the work* (Stechly, Katz): a sound sure/impossible pruner on a tiny step space (4573 states in Game of 24) carries it; LLM-guided search is neither sound nor complete and costs far more calls (c13, b16, b25).
- *Evaluator quality is the lever* (Wang, Chen, Feng): a random evaluator drops Top1 from 0.74 to 0.0 (c12); a learned value lifts Path@1 from 21.0 to 64.8 (a17).
- *Diversity is the lever* (PlanSearch, Si): gain tracks idea diversity; samples collapse to few unique ideas (c19, d12).

## 3. Core findings with exact numbers

Status: **E** = two or more independent sources; **S** = single source; **C** = contested.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| ToT beats flat sampling on Game of 24 (GPT-4, 100 hard games) | IO 7.3, CoT 4.0, CoT-SC(100) 9.0, IO best-of-100 33, CoT best-of-100 49, ToT b=1 45, ToT b=5 74 (%) | Yao 2023 (a02, b01) | S |
| About 60% of CoT chains fail at step 1 | about 60% on Game of 24 | Yao 2023 (a03, b02) | S |
| ToT cost vs best-of-100 CoT | ToT 5.5k completion + 1.4k prompt tokens, $0.74, 74%; CoT best-100 6.7k + 2.2k, $0.47, 49% | Yao (a07, b03) | S |
| Independent reruns of ToT land lower or vary | 69% (AoT, b=5); Wang b=5 0.74-0.76, b=3 0.77, b=1 0.65; GPT-3.5: 19% (Yao), 20% (LATS), 25% (Wang) | a15, c11, c12, b22 | E (value varies 5-8 points) |
| Yao b=1 is 45% but Wang b=1 is 0.65 | 20-point gap, same task | a02, c12 | C |
| Mini crosswords (20 games, GPT-4) | word success IO 14, CoT 15.6, ToT 60; letters 38.7/40.6/78; games solved 0/1/4 of 20; oracle best state 7/20 | Yao (a05, b04) | S |
| Crossword ablations | no prune: letters 65.4, words 41.5, 1 game; pruning missed 3 of 4 solved boards | a05, critique | S |
| Sound code verifier closes most of the gap | 150 direct queries + sound verifier 70% vs ToT 74% | Stechly 2024 (c13) | S |
| Code-written successor + goal test + BFS | Game of 24: 1361 of 1362 solved, 100%; 1.2 rounds successor, 1 goal; full space 4573 states; four domains 1.0-2.8 rounds | Katz 2024 (b16, c17, d13) | E (with GIF-MCTS limits) |
| Evaluator quality decides | random evaluator Top1 0.0; GPT-3.5 evaluator 0.68-0.72; GPT-3.5 generator + GPT-4 evaluator 0.30; GPT-3.5 both 0.25; evaluate-once 0.73 | Wang 2024 (c12), Yao (a06) | E |
| Learned value beats prompted value | Game24 Path@1: LLaMA prompted 9.2, GPT-3.5 prompted 21.0, learned 64.8; CoT greedy 12.7 | Feng 2023 (a17, a18) | E |
| Tree search needs a very accurate judge | discriminator about 90% accuracy needed; tree search 10-20x slower than re-ranking, negligible gain; observation-enhanced discriminators up to +30.2 and +8.4 points | Chen 2024 (b13) | S |
| Step judges are noisy | ProcessBench first-error F1 avg: o1-mini 87.9, GPT-4o 61.9; idea rankers 43-53% vs human 56.1% | Zheng (d09), Si (d12) | E |
| Self-correction without oracle hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1/41.8; GPT-4 GSM8K 95.5 to 91.5/89.0 | Huang 2024 (d10, c24) | E |
| Equal tokens: sample+select usually as good | GSM8K CoT-SC with reward model 52.3 vs BFS-V 52.5; SC beats ToT on GPT-3.5 | a18, c12 | E |
| Reasoning models: voting equals or beats search | R1-distills, QwQ: majority voting beat PlanSearch, mixture of agents, revisions; revision wrong-to-right under 10%; GSM8K "wait" to 16k tokens -11.8%, parallel +10.1% | Wang 2025, Ghosal, Zeng (d03-d05) | E |
| Sequential beats parallel with 4096-token chain cap | 43 of 45 configs, best +46.7 (Qwen3-235B AIME25 76.7 vs 30.0) | Sharma 2025 (d06) | C |
| Value-guided tree beats voting on a reasoning model | GPT-OSS-20B avg EM, 4 multi-hop QA: parallel 0.268, tree random expansion 0.215, tree + step value 0.309, full BAVT 0.388 | Li 2026 (d01, d02) | S |
| PRM beam search is difficulty dependent | beam beats best-of-N at levels 3-4 and small budgets; hurts at levels 1-2 and at 256 generations; compute-optimal about 4x less compute; small model beats 14x larger in FLOPs-matched test | Snell 2024 (a21, b14, c15) | S |
| REBASE beats MCTS and sampling | Llemma-7B + REBASE beats Llemma-34B; about 2x fewer FLOPs; MCTS leaves unfinished solutions | Wu 2024 (a22, b15, c16) | E (with R1 report) |
| Single-call trace matches multi-call ToT | AoT 71% with 1 query (5,450 prompt + 998 completion tokens) vs ToT 69% with 109.1 queries (13,900 + 5,500); crosswords 52 vs 46.5 | Sel 2023 (a15, c11) | S |
| Graph merge helps decomposable tasks | sorting median error 61% lower than ToT at P=64, 69% at P=128, negligible at P=32; cost over 31% lower; GPT-3.5 only, no ablation | Besta 2023 (a14, b07, d15) | S |
| Training on search traces | Countdown 51.27% vs 25.73% optimal-path; 57.1% of 285,501 trajectories reach the goal; Searchformer 93.7% optimal Sokoban, 26.8% fewer steps | Gandhi, Lehnert (a19, a20) | E, training only |
| Plan-space search raises pass@k | LiveCodeBench Claude 3.5 Sonnet: pass@200 77.0 vs 60.6 repeated sampling, pass@1 no search 41.4 | Wang 2024 PlanSearch (c19) | S |
| Web-agent search | VWA 18.9 to 26.4 (+39.7%); WebArena 15.0 to 19.2 (+28.0%); Llama-3-70B VWA 7.6 to 16.7; gains rise with budget | Koh 2024 (a23, b20) | S |
| LATS ablations | HotpotQA EM: no LM heuristic 0.37, DFS 0.42, no reflection 0.58, full 0.63; HumanEval GPT-4 92.7, GPT-3.5 83.8; sampling baselines 0.40-0.42 at 250 | Zhou 2023 (b10, b11, c08, c09) | C (baselines re-run by authors) |
| Cost of LLM-in-loop search | about $40 IO/CoT, $200 ReAct, $14,000 RAP, $16,000 LATS (estimate, same suites) | Katz (d16) | S |
| RAP on Blocksworld | LLaMA-33B 2/4/6-step: RAP(10) 1.00/0.86/0.26, RAP(20) 1.00/0.88/0.42; CoT 0.17/0.02/0.00; GPT-4 CoT 0.50/0.63/0.40 | Hao 2023 (a09, b08) | S |
| Small model + MCTS + cross-check | GSM8K LLaMA2-7B 12.51 to 63.91; baseline few-shot CoT only | Qi 2024 rStar (c20) | S |
| AB-MCTS | budget 128: LiveCodeBench GPT-4o sampling 37.8, AB-MCTS-A 39.1, MCTS 36.7; on ARC sampling wins at 128; AB-MCTS overtakes at 200-500 | Inoue 2025 (d07, d08) | S |
| Open-ended writing (ToT) | GPT-4 coherence IO 6.19, CoT 6.93, ToT 7.56; refine on IO 7.67; human pairs (authors): 41 ToT, 21 CoT, 38 similar | Yao (a04, b05) | S |
| Idea novelty: flat overgenerate-and-rank | blind human novelty 5.64 vs 4.84 (human), 49 ideas per arm, 79 reviewers; 4000 seeds give about 200 unique | Si 2024 (d11, d12) | S, no tree arm |
| Novelty-tuned ToT with thinking mode | Blocksworld Qwen-14B 50 items: naive 3/50, thinking 23/50, base ToT 0, tuned ToT 11/50, tuned + thinking 94% at 229k-330k tokens | Hamm and Ajanovic 2026 (c22) | S |

## 4. Mechanisms and models

### 4.1 Plain ToT loop (implementable)
```
frontier = [root]
for depth in 1..T:
    cand = []
    for s in frontier:
        cand += propose(s, k)          # one prompt returns k next steps, or k samples
    score = [value(c) for c in cand]   # value: 3 samples of sure/maybe/impossible -> number
    frontier = top_b(cand, score)      # code does the sort
return best(frontier)                  # code check if available
```
Yao: b=5, 3 value samples per state, proposal prompt lists next equations (a02). Game of 24 has 3 steps. Cost is 5-100x CoT tokens (a07).

### 4.2 What makes it pay
- **Foothold:** the plain model must already be right sometimes (G12). Weak generator is the bottleneck: GPT-3.5 generation with GPT-4 evaluation scored 0.30 (c12).
- **Cheap strong evaluator:** a cheap evaluator is fine if it is accurate. GPT-3.5 evaluating GPT-4 proposals kept 0.68-0.72 at $33.53 vs $159.87 (critique, c12).
- **Sound pruning:** "impossible" must be right. Crossword pruning dropped 3 of 4 solved boards (a05, critique). Keeping pruned nodes in a reserve list is our proposal, untested.
- **Early failure:** if chains die at step 1 (60% in Game of 24), branching at step 1 is where search helps (a03).
- **Depth cap:** RAP success falls with plan length (0.32 at 10 steps) (a10).

### 4.3 Code instead of LLM (Thought of Search)
Ask the LLM once to write `successors(state)` and `is_goal(state)`. Test on 3 labelled cases. Loop at most 3 rounds (mean 1.0-2.8). Then run BFS/DFS in code: zero further LLM calls, sound and complete. Applies only to deterministic, fully observable tasks (GIF-MCTS authors say so, d14). This is also a formalisability test: if you cannot write it in 3 rounds, fall back to sampling. Caveat: the crossword result assumes 10 candidate answers per clue including the right one (d13).

### 4.4 Algorithm of Thoughts (one-call trace)
Put worked examples in the prompt that show the whole search, dead ends and backtracking, written out. The model continues the pattern in one generation. 1 query and 998 completion tokens vs 109 queries (c11). Risk: the model may skip branches silently; only tested on arithmetic and crosswords.

### 4.5 Graph of Thoughts
Add Aggregate (merge several thoughts into one) and Refine (loop on a thought). Sorting 64 numbers: split into chunks, sort each, merge, score, keep best. Volume of a thought = number of earlier thoughts that can reach it. Gain is tied to decomposition (no ablation without scoring) (a13, d15). A merge can be done in code for sorting and set intersection.

### 4.6 PRM-guided beam search and REBASE
Beam: sample n steps, score with a trained PRM, keep top. REBASE: no rollouts; each node's reward sets how many children it gets, and finished solutions are voted. Cheaper than MCTS because MCTS leaves unfinished solutions (a22). Needs a trained reward model, which we lack for most tasks.

### 4.7 Adaptive width/depth (AB-MCTS)
At each node, choose to widen (new sample) or deepen (refine an existing one) with Thompson sampling on observed scores. Needs a sound score. Sampling wins at small budget; trees win after sampling plateaus (d07, d08).

### 4.8 Value-guided budgeted tree (BAVT)
Single reasoning-model backbone, prompted step value, exploit-late scheduling. The random-expansion ablation matters: without the value signal the tree is worse than voting (d02).

### 4.9 Plan-space search
Generate several natural-language plans first, then code from each plan. Gain tracks diversity of plans (c19). This maps to O1-O8: each operator yields a different plan.

## 5. What holds up

**Holds up (two or more sources):**
- ToT beats flat CoT-SC on closed puzzles with a checkable state (Game of 24, crosswords, Sudoku, Blocksworld) on GPT-4-class models. Absolute values vary 5-8 points across reruns (K02).
- The evaluator is the lever; a random evaluator gives 0.0 (K04).
- Prompted self-evaluation is a weak value; learned values or code checks are far better (K05).
- At equal tokens on short-horizon tasks, sample plus vote or rerank is as good or better (K07, K21).
- Cheap rollout-free expansion beats MCTS in token space (K10).
- Code search beats LLM-in-the-loop search on cost and soundness where the task is formalisable (K03, K26).
- A strong base model without search can beat a weaker model with search (K18).
- Training on search traces helps; prompting for them is not shown (K13).

**Failed or weak:**
- ToT's headline came from GPT-4 on 100 hard games, one run, no confidence intervals (critique).
- LATS gains over ToT/RAP rest on baselines the authors re-ran with fewer samples; LATS uses more nodes (critique).
- R1 reports MCTS failing, no numbers (b18).
- Revision after a wrong answer: wrong-to-right under 10% (d05); self-correction without an oracle lowers accuracy (d10).
- GoT: only GPT-3.5, no ablation, no gain at P=32 (d15).
- Breadth above b=3 shows no gain in independent runs (0.74 at b=5 vs 0.77 at b=3, c12).
- Zero-shot ToT adds little where the model is strong: GSM8K 90 vs 86, StrategyQA 83 vs 82, 100 items (a07).

**Moderators:**
- *Task:* closed, code-checkable problems benefit; open-ended ideation has no tree evidence.
- *Difficulty:* beam search hurts easy items (levels 1-2), helps mid (3-4) (b14). At large budgets PRM over-optimisation hurts.
- *Judge accuracy:* about 90% for tree search to beat reranking (b13).
- *Budget:* sampling wins at small budgets on ARC, search after plateau (d08).
- *Chain cap:* sequential wins under 4096-token chains, parallel with uncapped chains (d04-d06).
- *Model type:* instruct models repeat failures (Qwen3-30B instruct baseline 0.289 to 0.293 across budgets) while reasoning models improve with budget (OSS-20B 0.194 to 0.334) (d17).

**Interventions that worked:** step-1 branching; value-guided expansion over random; code verifiers; reflection in LATS (0.58 to 0.63); decomposition and merge at large sizes; reversible-action trees on the web; plan diversity.

**Interventions that did not:** budget-matched MCTS in token space; prompted self-correction; adding branches past b=3; splitting steps into separate calls in Hamm and Ajanovic (results got worse).

## 6. Language models

- **GPT-4 (2023):** ToT Game of 24 69-77% vs CoT 4% and best-of-100 49%. GPT-3.5: ToT 19-25%, with SC beating ToT per token (c12).
- **Strong model, easy task:** little gain (GSM8K 90 vs 86).
- **Small open models:** large gains from search with learned values or training (TS-LLM; rStar LLaMA2-7B 12.51 to 63.91; Llama-3-70B VWA 7.6 to 16.7). Baselines are often weak (single-sample few-shot CoT), so the gap to equal-token voting is not measured.
- **Code-written search:** GPT-4 wrote correct successor/goal code in 1-2.8 rounds; 100% on Game of 24 (d13). This beats every LLM-in-the-loop tree.
- **Reasoning models (2025-26):** long chains already contain internal search. On R1-distills and QwQ, majority voting equals or beats external search and revision (d03-d05). Only BAVT shows a tree winning (0.388 vs 0.268 EM), and only with a value signal. No o-series, Claude thinking or ToT/graph arm was found. Thinking mode lifts Blocksworld from 3/50 to 23/50 on Qwen-14B (c22).
- **Equal tokens is the key:** ToT's 74% vs 49% at 5.5k vs 6.7k tokens looks like a win, but with a sound verifier 150 flat queries reach 70% (c13).
- **Judges:** ProcessBench F1 87.9 (o1-mini) to 61.9 (GPT-4o); olympiad problems worse; 32.2% of correct-answer solutions on OlympiadBench still contain a process error (d09). Idea judges 43-53% (d12).
- **Diversity:** 4000 seeds give about 200 unique ideas (d12). Instruct models repeat failures with more budget (d17).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)
1. **Default to sample-and-select; branch only on a trigger.** G1/G12/S6. [E] K07, K21. Evidence a18, c12, d03, d04, d05.
2. **Code does the pruning and selection; a model judge is never the only gate.** G5/G2. [E] K04, K05, K23. Evidence c12, a17, d09, d10, b13.
3. **Spend on the generator before the evaluator; a cheap evaluator is fine only if measured accurate.** G7/S6. [E] K04. Evidence c12, a06.
4. **Check the base model first; skip search when base accuracy is already high.** G12. [E] K18. Evidence a12, a07, b05.
5. **Formalisability gate: try writing successor and goal-test code in at most 3 rounds against 3 labelled cases; if it works, run code search; else sample.** S6/G5. [E] K03, K26. Evidence b16, c17, d13, d14.
6. **If you grow a tree, prefer reward-balanced expansion with many finished branches over MCTS rollouts.** S6. [E] K10. Evidence a22, b15, c16, b18.
7. **Log variance over 3 seeds before claiming any tree gain under 8 points.** G7. [E] K02. Evidence a15, c11, c12, b22.
8. **Revise only with real failing output; no no-oracle self-correction.** G2. [E] K05. Evidence d10, c24, d05.
9. **Search pays only where there is a foothold; cap depth.** G12/S6. [E] K08. Evidence a03, a18, a10.

### Test first
1. **Step-1 branching trigger** (low agreement or failed check at step 1). S6. [S] K08. a03.
2. **Judge-accuracy gate (20-50 labelled items, branch only above threshold).** G5/S6. [S] K23. d09, b13.
3. **Value-guided tree with a random-tree control vs voting on a reasoning model.** S6. [S] K20. d02.
4. **Route by difficulty bin; no beam on easy items.** G12. [S] K09. b14, c15.
5. **Trigger deeper search at sampling plateau with a sound score.** S6. [S] K24. d07, d08.
6. **Code-run merge step on decomposable tasks.** S6/O3. [S] K12, K27. a14, d15.
7. **One-call search trace (AoT) on two non-arithmetic tasks.** S6. [S] K11. a15, c11.
8. **Plan-diversity step before code (operators as diverse plans).** S6/O1-O8. [S] K14. c19.
9. **Idea tree vs sample-rank-dedup with blind novelty raters.** S6/G8. [S] K17, K25. d11, d12.
10. **Reserve list for pruned nodes.** S6. [D] no direct evidence; critique gap 8. a05.
11. **Unique-answer stop rule for widening.** G1. [S] K28. d12, d17.
12. **Reversible-step limit on action trees.** G7. [S] K15. a23.
13. **Feeding real failed attempts as context** (nearest prompt analogue to search-trace training). M/G2. [E] for training only (K13); prompting untested. a19, b12.

## 8. Concrete tests on our bench

All arms at equal total tokens (prompt + completion, setup included, G7). 3 seeds. Report mean and range.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 100 Game-of-24-style items plus 100 ARC or Brainteaser items | (a) tree b=3 with prompted value, (b) best-of-N with code check, (c) code-written successor/goal BFS (where it forms) | solved rate | code BFS 95-100% where it forms; tree within 5 points of code-verified sampling; tree not better when a code check exists |
| T2 | Items with a codable check, easy and hard bins | (a) sample+vote, (b) tree with step value, (c) tree with random expansion | solved rate by difficulty bin | tree wins only in mid-hard bin; random tree below vote (K20 replication) |
| T3 | 50 items with labelled partial states | judge accuracy per task; then branch vs sample only above 90% | judge accuracy; solved rate | gate prevents losses on tasks where judge is near chance |
| T4 | Items where plain model gets 10-60% | trigger arms: always tree, never tree, step-1-disagreement trigger | solved rate per token; false-trigger cost on easy items | trigger matches best fixed arm at 30-50% fewer tokens |
| T5 | Decomposable tasks at 2-3 sizes (sort, set intersection) | split + code-merge (no scoring) vs GoT-style scoring vs flat | error rate by size | code merge captures most gain at large size, none at small |
| T6 | 40 open ideation prompts | idea tree with operators vs sample-rank-dedup, blind 3 raters, length-normalised | novelty and usefulness | no gain over flat; if tree wins, +0.5 on a 10-point scale |
| T7 | 2 non-arithmetic tasks | AoT one-call trace vs multi-call tree | solved rate, skipped-branch rate | within 3 points of tree at under 25% of tokens |
| T8 | Constraint tasks | prune with reserve list vs hard prune | recovery rate of right branch | reserve recovers some of the false prunes |
| T9 | Reasoning-model items (thinking mode) | voting vs tree vs sequential refine, uncapped chains | accuracy, per-chain tokens | voting equal or better; tree only with sound score |

## 9. What does not transfer, and why

- **ToT headline numbers.** One task, 100 items, GPT-4 (2023), no confidence intervals. Game of 24 has a tiny state space and a sure/impossible check code could do.
- **GoT sorting gain.** GPT-3.5 only, gain vanishes at small sizes, decomposition not separated.
- **rStar, TS-LLM and Searchformer gains.** Need training, a learned value net or a weak baseline. We train nothing.
- **PRM beam search and REBASE.** Need a trained process reward model. We have only prompted judges.
- **Stream of Search.** Training on search traces; prompting is not tested.
- **Web-agent trees.** Rely on resettable environments; irreversible actions break them.
- **Code BFS.** Works only for deterministic, fully observable tasks.
- **Creative-writing ToT.** GPT-4 coherence score, authors as human raters; this is not novelty.
- **2023 model numbers.** Reasoning models run internal search; external tree gain over voting is unproven (K21).

## 10. Open questions

1. At equal tokens, with only a prompted judge, does any tree beat sample-and-select on o-series, R1 or Claude thinking, on tasks that are not code-checkable? (Partly closed: leaning sample first.)
2. What judge accuracy is needed per task, and can we measure it online before branching? Only Chen's 90% exists.
3. Does an idea tree beat flat overgenerate-and-rank on human novelty? No study found.
4. How much of GoT's gain is decomposition plus merge?
5. Is AoT robust beyond arithmetic and crosswords?
6. Does the formalisation route extend to ill-formed domains, and how do we detect failure?
7. What is the right trigger (step-1 disagreement, verifier failure, difficulty bin) and what is the false-trigger cost?
8. How often does a false "impossible" prune remove the right branch, and does a reserve list help?
9. Split roles (strong generator, cheap evaluator) at equal dollar cost on reasoning models.
10. Why does breadth stop helping at b=3? Duplication and instruct-model repetition are hypotheses (K28), not tested.
11. Why do Yao and Wang disagree by 20 points at b=1?

## 11. Sources

[V] = opened and read as full text this series; [M] = snippet or second-hand only.

- [M] Newell and Simon 1972, Human Problem Solving (cited via Yao). https://arxiv.org/abs/2305.10601 (a24)
- [M] Wang et al. 2023, Self-Consistency. https://arxiv.org/abs/2203.11171 (a25)
- [V] Yao et al. 2023, Tree of Thoughts. https://arxiv.org/abs/2305.10601 (a01-a07, b01-b05, c01-c04)
- [V] Long 2023, LLM Guided Tree-of-Thought. https://arxiv.org/abs/2305.08291 (a08, b06, c05)
- [V] Hao et al. 2023, RAP. https://arxiv.org/abs/2305.14992 (a09, a10, b08, b09, c07)
- [V] Xie et al. 2023, Self-Evaluation Guided Beam Search. https://arxiv.org/abs/2305.00633 (a11, a12, b17, c10)
- [V] Besta et al. 2023, Graph of Thoughts. https://arxiv.org/abs/2308.09687 (a13, a14, b07, c06, d15)
- [V] Besta et al. 2024, Demystifying Chains, Trees, and Graphs of Thoughts. https://arxiv.org/abs/2401.14295 (b21, c25; abstract and intro level)
- [V] Sel et al. 2023, Algorithm of Thoughts. https://arxiv.org/abs/2308.10379 (a15, a16, c11)
- [V] Feng et al. 2023, TS-LLM. https://arxiv.org/abs/2309.17179 (a17, a18)
- [V] Zhou et al. 2023, LATS. https://arxiv.org/abs/2310.04406 (b10, b11, c08, c09)
- [V] Huang et al. 2024, LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c24, d10)
- [V] Gandhi et al. 2024, Stream of Search. https://arxiv.org/abs/2404.03683 (a19, b12, c21)
- [V] Lehnert et al. 2024, Beyond A* (Searchformer). https://arxiv.org/abs/2402.14083 (a20)
- [V] Chen et al. 2024, When is tree search useful for LLM planning. https://arxiv.org/abs/2402.10890 (b13)
- [V] Stechly, Valmeekam, Kambhampati 2024, Self-verification limitations. https://arxiv.org/abs/2402.08115 (c13)
- [M] Chen et al. 2024, Pairwise comparison (C-ToT). https://arxiv.org/abs/2402.06918 (c14; not re-opened)
- [M] Wang and Zhou 2024, CoT reasoning without prompting. https://arxiv.org/abs/2402.10200 (c23; table garbled)
- [V] Wang et al. 2024, Reasoning in Token Economies. https://arxiv.org/abs/2406.06461 (c12)
- [V] Katz et al. 2024, Thought of Search. https://arxiv.org/abs/2404.11833 (b16, b25, c17, d13, d16)
- [V] Dainese et al. 2024, GIF-MCTS code world models. https://arxiv.org/abs/2405.15383 (d14)
- [V] Koh et al. 2024, Tree search for language model agents. https://arxiv.org/abs/2407.01476 (a23, b20, c18)
- [V] Snell et al. 2024, Scaling LLM test-time compute. https://arxiv.org/abs/2408.03314 (a21, b14, c15)
- [V] Wu et al. 2024, Inference scaling laws (REBASE). https://arxiv.org/abs/2408.00724 (a22, b15, c16)
- [M] Qi et al. 2024, rStar. https://arxiv.org/abs/2408.06195 (c20; not re-opened)
- [V] Wang et al. 2024, PlanSearch. https://arxiv.org/abs/2409.03733 (c19)
- [V] Si, Yang, Hashimoto 2024, Can LLMs generate novel research ideas. https://arxiv.org/abs/2409.04109 (d11, d12)
- [V] Zheng et al. 2024, ProcessBench. https://arxiv.org/abs/2412.06559 (d09)
- [V] DeepSeek-AI 2025, DeepSeek-R1. https://arxiv.org/abs/2501.12948 (b18)
- [V] Muennighoff et al. 2025, s1. https://arxiv.org/abs/2501.19393 (b19)
- [V] Inoue et al. 2025, Wider or Deeper (AB-MCTS). https://arxiv.org/abs/2503.04412 (d07, d08)
- [V] Wang, Zhu, Saad-Falcon et al. 2025, Rethinking inference-time scaling. https://arxiv.org/abs/2504.14047 (d03)
- [V] Ghosal et al. 2025, Does thinking more always help. https://arxiv.org/abs/2506.04210 (d04)
- [V] Zeng et al. 2025, Revisiting test-time scaling of o1-like models. https://arxiv.org/abs/2502.12215 (d05)
- [V] Sharma and Chopra 2025, The Sequential Edge. https://arxiv.org/abs/2511.02309 (d06)
- [V] Li et al. 2026, BAVT. https://arxiv.org/abs/2603.12634 (d01, d02, d17)
- [M] Hamm and Ajanovic 2026, Novelty-based ToT search. https://arxiv.org/abs/2605.06040 (c22; detail beyond abstract not re-opened)
