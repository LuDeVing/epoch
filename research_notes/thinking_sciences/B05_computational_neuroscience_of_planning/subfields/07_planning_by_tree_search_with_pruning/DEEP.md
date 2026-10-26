# Planning by tree search with pruning: deep document

*Subfield B05.07. Built from evidence_a-d.jsonl (a01-a29, b01-b26, c01-c27, d01-d20), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids in brackets. Claim ids as K##. Corrections from the cross-check (critique.md) are applied here: ToT crossword columns, Snider p-values, SSDP node counts, the LATS table spread.*

---

## 1. What it is

Planning by tree search means: from the current state, list the moves, imagine where each leads, and repeat. The imagined states form a tree. Value is passed back from the leaves to the root. The best first move is chosen.

A full tree grows as b^d (b = branches per step, d = depth). Minds and machines cannot afford it. So every real planner cuts the tree. There are three kinds of cut:

- **Depth limit.** Stop looking after d steps. The leaf needs a substitute value.
- **Width limit (beam).** Keep only the best b states per step.
- **Pruning.** Drop a branch because something about it says "do not continue here". The rule can be good (a rule check says it is a dead end) or bad (it hurt to imagine).

This subfield asks: how do people choose depth and pruning, what goes wrong, and what does it mean for a language-model scaffold that grows a small tree at S6 (impasse)?

Why it matters for our agent. Schema section 4 says: at most 3 children per expansion, depth at most 2, at most 2 expansions per problem, children ranked by test result. These numbers are marked [D] (design choice, no evidence). This document gives the evidence to replace them with rules: depth and width set by budget, pruning by a checked signal, a way to undo a wrong prune.

Three research lines meet here:

1. **Human pruning.** The Huys 2012 maze. People cut branches after a large loss, as a reflex, even when it costs points.
2. **Human depth and resource use.** Keramati, Snider, Huys 2015, Callaway, van Opheusden. Depth falls under time pressure. Cut leaves get cached values. Long plans are split into fragments.
3. **LLM tree search 2023-2026.** Tree of Thoughts, RAP, LATS, Koh, REBASE, Snell, and the 2025-26 budget and pruning papers. The question is what survives at equal tokens.

Overlaps in the series (links only, not covered here): Expected value of control; Value of information; Generation versus evaluation; Plans and schemas; Functional decomposition; Heuristics and biases; Bias and debiasing; Exploration and spontaneous experiments.

---

## 2. History and theories in depth

### 2.1 Early search theory (not opened)

Newell and Simon (1972) and de Groot's chess work are cited for the claim that experts do not search many more moves than novices; they pick better ones [a19]. Not opened this session. Treat as unverified. Later, van Opheusden et al. found that fitted depth does rise with skill in four-in-a-row [d01]. So the old claim and the new one are in tension. Both are model-inferred.

### 2.2 Goal-directed versus habit, and the arbitration idea (2011)

Keramati, Dezfouli and Piray (2011) proposed that the brain does tree search only when the value of perfect information about the cached (habit) value is larger than the cost of deliberating. Cost is reward rate times time. Otherwise it uses the cache. Simulations only: 40 vs 240 training trials, 3000 runs per condition; deliberation time falls to about zero after about 100 trials in one task [a11]. This is the first rule for "when to search at all".

### 2.3 The founding pruning study (Huys et al. 2012)

Healthy volunteers (N=46, groups of 15/16/15) planned in a 6-state maze with 2 buttons and 2-8 move episodes. The groups differed only in the size of the large loss: -70, -100 or -140 pence [a01]. Findings:

- When a path passed the large loss, people stopped searching there. This was "reflexively evoked by large losses and persisted even when overwhelmingly counterproductive" [a01].
- Model comparison: a full look-ahead model predicted about 77% of choices (predictive probability 0.71). Adding discounting, then pruning, then a learned Pavlovian value raised this to about 91% [a02, b01]. The goal-directed model beat a habit (SARSA) model by BIC 314 [a02, b02].
- The pruning was specific to the large loss, not a general discount. Specific beat general pruning in 14/15, 12/16 and 14/15 subjects across the three groups [a03].
- Pruning did not shrink when it became costly. No group difference in specific pruning, even though it was counterproductive in the -70 and -100 groups [a03]. In the -140 group the cost was zero, because an equal path avoided the loss.
- Punishments were treated as about 1.4 times as aversive as equal rewards [a03]. The authors note loss aversion could explain part of the effect without pruning [a03].
- Original claim that pruning correlates with BDI (depressive symptoms): later not reproduced (see 5.3).

The model [a04]: at every tree depth a biased coin stops the search; a separate stop probability applies after large-loss transitions. Binary pruning, not graded. Four model families: Look-ahead, Discount, Pruning, Pruning and Learned.

### 2.4 Fragmenting plans and reusing parts (Huys et al. 2015)

A second study used longer plans (3-5 moves, so 8, 16 or 32 sequences) with N=37 analysed of 41 [a06]. Findings:

- Pruning appeared in 37/37 subjects, also under a time limit [a06, b08].
- People cut the tree into short fragments, solve each greedily and reuse earlier fragments. Fragmentation correlated with depth at Spearman 0.44, significant in 35/37; fragment endpoints matched predictions for 90% of end states [b07].
- Cost arithmetic: a full depth-3 tree costs d x 2^d = 24 operations; a 2-then-1 split costs 10 [a07]. Inferred splits matched the cheapest split that still gives the optimal first move.
- Memoization (reusing fragments with a Chinese-restaurant-process rule) raised log-likelihood by 43 +- 22 per subject and explained 14% more variance; the full model explained 78% of variance [a08, b07].
- Unrestricted fragmentation overfit (iBIC +682 vs baseline). One shared fragmentation for everyone was worse than baseline by iBIC 116, so strategies differ between people [a06, b09].
- Timing evidence is weak: depth-1 fragments were preceded by pauses only 9.7 ms longer (t(36)=2.17, p=0.037) [a07].

### 2.5 Depth under resource limits

- **Snider et al. (2015).** N=6 including two authors. In a fast risky path task, people traded planning depth against how often they replanned. Behaviour fit a brute-force exploration under a fixed work budget (W_BF = 12 +- 2 fast, 48 +- 8 slow) better than efficient-algorithm contours [a14]. Correction from the cross-check: the p-values 1.9e-10 and 1e-7 are for depth and replan rate as predictors of score advantage, not for depth differences between conditions. First choice in a trial was 771 ms slower; plan once, then replan sparingly [a15].
- **Keramati et al. (2016).** N=30 (15 per group). Time limit 2000 ms vs 700 ms per stage in a three-stage task. Planning stronger with more time (rewarded p=0.011, unrewarded p=0.027). Plan-until-habit (plan to a shallow depth, then use cached habit values) stronger under time pressure after rewarded trials (p=0.034) [a09, b04]. Added detail: after unrewarded trials the group difference was not significant (P=0.9) [critique item 11]. Stage-2 habit weights 0.37 +- 0.18 (high resource) vs 0.59 +- 0.23 (low) [a10]. Pure habit was not in the best model. A cut with no leaf value would predict indifference, which does not match the data [a10, b06].

### 2.6 Rational accounts: where to expand, when to stop

- **Sezener, Dezfouli, Keramati (2019).** Value of uncertainty resolution (VUR): expand the leaf whose expansion most raises the best strategy value; stop when the best VUR is below the cost of one expansion. Pruning of the large-loss branch emerges without a Pavlovian parameter: a very bad branch has little overlap with the best one, so expanding it has low value. Simulation only (7x7 grid, budgets 5-25 expansions, Huys task 300 runs per condition). Mean-only and variance-only pruning both fail. Deterministic transitions, Gaussian leaf values, myopic one-step expansion [a12, a13].
- **Mattar and Daw (2018).** Planning as choosing which memory backups to run. Priority = gain x need. Gives forward and reverse replay, and focuses compute near the agent and near rewards [a18]. Same logic as VUR.
- **Callaway et al. (2022; preprint read).** Planning as a metalevel decision. The optimal policy is near best-first search with a stopping rule that depends mostly on the gap between the best and the next-best path, and only partly on the best path's absolute value. Cost per expansion is the main parameter [d03]. Strategy flips with where the variance sits: breadth-first when big rewards come early, best-first when variance is constant, depth-first when it comes late. People switched accordingly [d04].
- **Rival account (Zorowitz, Momennejad, Daw 2020).** Simulation shows an agent that is pessimistic about its own later choices undervalues the branch after a loss and so mimics pruning, with no pruning mechanism [d18]. Never tested against pruning on human data.

### 2.7 Neural and individual-difference work

Lally et al. (2017, fMRI, same recruited sample as Huys 2015: 41 recruited, mean age 23.3) found the optimal path was found 78% of the time when it avoided a large loss but 37% when it had to pass through one (gap 41 points, t(36)=12.51, d=2.06). About 52% of the errors on those trials were aversive pruning (chance about 11%). Per-person pruning ranged from 4% to 93%, split-half r=0.69. Subgenual cingulate tracked the pruning index (t(36)=3.87, pSVC=0.004); insula tracked large-loss receipt and correlated with the pruning gap (r=0.47, p=0.003). State anxiety predicted pruning (p=0.042), depression did not [a16, a17, b12, b14]. Pruning trials were faster than error trials (p=0.004), so pruning looks fast and affect-linked [b14].

### 2.8 Expert depth

van Opheusden et al. (preprint of the 2023 Nature paper): four-in-a-row (4x9 board, about 1.2e16 states). A best-first search model with value pruning, feature dropout and noise fits human moves. Fitted depth rises with skill and practice (see 3). The preprint text was read; the Nature version was not [d01, d02].

---

## 3. Core findings with exact numbers

Status: **E** established (two or more independent sources, claims.jsonl), **S** single-source, **C** contested, **R** refuted. "Human" rows are all from one maze family unless stated. LLM rows are mostly 2023-2026 GPT-4, GPT-3.5 and 1.5B-32B open models, mostly math or puzzles.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People cut branches after a large loss, even when it costs points | N=46 (15/16/15), losses -70/-100/-140; look-ahead predicts 77% of choices, best pruning model about 91%; specific > general pruning in 14/15, 12/16, 14/15 | Huys 2012 [a01-a03, b01] | E (K01), same task and lab family |
| Pruning replicated in a new sample | 37/37 subjects prune; optimal path found 78% vs 37%, d=2.06; about 52% of errors are pruning vs about 11% chance | Huys 2015, Lally 2017 [a06, a16, b12] | E but shared sample |
| Pruning replicated at another site | 40 patients vs 49 controls; pruning 0.33 vs 0.15, F(1,100)=16.46, d=0.81; horizon unchanged p=0.199 | Lavalley 2025 [b15, d17] | E (same paradigm; Huys co-author) |
| Pruning is not linked to depression | 30 depressed vs 31 healthy: 0.617 vs 0.630, t(59)=0.32, p=0.75, BF10=0.27; BDI r=0.068 | Faulkner 2022 [b10, b11] | R (K02) |
| Pruning is stable and person-specific | range 4-93%, split-half r=0.69 | Lally 2017 [b12] | S (K03) |
| Cost of the reflex grows with depth | loss deficit 34%, 40%, 49% at depths 3, 4, 5; F(2,72)=5.58, p=0.009; pruning rate itself did not change with depth | Lally 2017 [b13] | S (K03) |
| Pruning and depth are separable | meth users: pruning up, horizon unchanged (p=0.199); CRT linked to less pruning, b=-0.036 | Lavalley 2025 [b15] | S (K20) |
| Time pressure gives shallower plans and cached leaf values | N=30 (15 per group), 2000 vs 700 ms; planning p=0.011 / 0.027; plan-until-habit p=0.034 (only after reward); habit weight 0.37 vs 0.59 | Keramati 2016 [a09, a10, b04] | E (K04), small N |
| Depth trades off against replanning rate | N=6 (2 authors); work W 12 +- 2 vs 48 +- 8; depth about 3.3 slow, 2.8 fast | Snider 2015 [a14] | E (K04), very small N |
| A cut branch needs a substitute value | cut with no fallback predicts indifference; not seen in data | Keramati 2016 [a10, b06] | S (K05), theory-driven |
| Long plans are fragmented and reused | full depth-3 tree 24 operations vs 10 split; log-lik +43 +- 22 with memoization; Spearman 0.44; 35/37 | Huys 2015 [a07, a08, b07] | S (K06) |
| Shared fragmentation fits worse | delta iBIC +116 vs baseline | Huys 2015 [b09] | S (K06) |
| Skill raises fitted depth | lab N=30, 5 sessions: depth slope 0.255 +- 0.061 per session, Elo slope 21 +- 4.6; 1000 mobile users slope 0.0108 +- 0.0010; depth 4-6 plies; model predicts held-out moves 40.8 +- 1.4% | van Opheusden preprint [d01] | E-ish (K21); preprint; depth model-inferred |
| More time gives deeper plans but not better play | N=30, 5/10/20 s: depth slope 0.042 +- 0.018 (p=0.019); strength -2.0 +- 1.6 Elo (p=0.21); feature drop rate up 0.0027 +- 0.0010 | van Opheusden preprint [d02] | S |
| People follow a resource-rational best-first rule with a gap-based stop | Exp1 N=95: lose 0.92 points vs best policy; expand a max-value path 81.5% (optimal model 74.6-100%, random 51.7%); stop-rule betas best value 0.82, best-vs-next 1.68 (optimal 0.99 and 4.64) | Callaway preprint [d03] | S (K25 for the rule), K21 for human fit |
| Best classical strategy flips with where variance sits | Exp2 N=298, Exp3 N=93, Exp4 N=291; optimal model fits best in all conditions except two | Callaway preprint [d04] | S |
| Value-of-information expansion gives pruning for free | simulation: budgets 5-25 expansions; punishments -140/-100/-70 | Sezener 2019 [a12, a13] | S (K07), simulation only |
| Pessimism about later choices mimics pruning | simulation, Fig 3b | Zorowitz 2020 [d18] | S (K27) rival account |

### 3.2 LLM findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Beam with state check beats best-of-100 samples | Game of 24, GPT-4: IO 7.3, CoT 4.0, CoT-SC (k=100) 9.0, ToT b=1 45, b=5 74, best-of-100 CoT 49, best-of-100 IO 33 | Yao 2023 [a22, c01, b16] | E (K08) |
| Cost of that | ToT 5.5k completion + 1.4k prompt tokens, $0.74, 74%; CoT best-of-100 6.7k/2.2k, $0.47, 49%; IO best-of-100 1.8k/1.0k, $0.13, 33% | Yao 2023 [a24, c03] (rechecked) | E |
| Most chain failures are born at the first step | about 60% of CoT samples already failed after the first three words | Yao 2023 [c02] | S |
| Model-judged pruning cuts true paths; backtracking matters more | crosswords, N=20 games. Letter / word / game success: ToT 78 / 60 / 20; no prune 65.4 / 41.5 / 5; no backtrack 54.6 / 20 / 5; CoT 38.7 / 14 / 0. No-prune search found a correct solution in 4/20 games, 3 of which pruned ToT missed, but output only 1 | Yao 2023 [a23, b17, c04] (columns corrected by the cross-check) | E (K09) |
| Generator matters more than judge | GPT-4 gen + GPT-3.5 eval 64%; GPT-3.5 gen + GPT-4 eval 31%; GPT-3.5 alone 19%; GPT-4 ToT 74% | Yao 2023 [a24, c05] | S (K14) |
| Tree adds little on easy tasks | ToT zero-shot GSM8K 90 vs CoT 86; StrategyQA 83 vs 82; SCULPT GPT-5.2 GSM8K 97.8 vs 96.3 at 24,142 vs 1,120 tokens; BAVT instruct baseline flat 0.289 to 0.293 | Yao [c05]; Fang [c21]; Li [c20] | E (K17) |
| Web agents: best-first search with depth d, breadth b, node budget c | VisualWebArena 18.9 -> 26.4 (+39.7%); WebArena 15.0 -> 19.2 (+28.0%); 200-task subset c=0 24.5, c=5 32.0, c=20 37.0 (+51%) | Koh 2024 [c10] | E (K08) |
| Value function sets the ceiling | none 24.5, LLaVA 30.0, GPT-4o no SC 28.5, SC n=5 32.5, SC n=20 37.0, ground truth 43.5 | Koh [c11] | E (K09) |
| Search beats re-ranking more runs; gain peaks at medium difficulty | re-ranking plateaus near 7 runs at 30% vs search 37.0; easy 34.2 -> 42.3 (+24%), medium 12.7 -> 22.2 (+75%), hard 10.2 -> 14.9 (+47%) | Koh [c12] | E (K13) |
| MCTS rollouts lose per FLOP; reward-balanced tree wins | MATH500: Mistral-7B sampling 256 samples 8.70e14 FLOPs 42.8% vs REBASE 32 samples 1.36e14 FLOPs 45.0%; Llemma-7B 45.5% (10.0e14) vs 46.8% (1.48e14); Llemma-34B 46.7% vs 49.2% | Wu 2024 [c17, d07] | E (K23) |
| Beam beats best-of-N at small budgets, reverses at large budgets and on easy items | MATH, PaLM 2-S* + PRM; budgets 4/16/64/256; bins 1-2 beam worsens with budget; bin 5 nothing helps; per-bin choice about equals best-of-N with up to 4x less compute | Snell 2024 [d08] | E (K13, K23) |
| Learned value beats prompted value; search beats best-of-k at equal tokens only on deeper tasks | Game24 64.8% (learned) vs 21.0% (GPT-3.5 prompt) vs 9.2% (ToT value); equal tokens: Game24 CoT-SC-ORM 50.6% at 684 tokens vs MCTS-ORM 69.3% at 649; PrOntoQA 83.2% at 273 vs 99.6% at 182; little gain on GSM8K | Feng 2023 [d09] | E (K23); table text garbled, recheck before outside use |
| Prompted self-verification is weak | GPT-4 on Game of 24: false negatives 20.7% (213/1029), false positives 10.4%; Blocksworld FNR 15.5%; disguised Blocksworld FNR 97.1% (100/103); standard prompting 5% vs LLM+LLM critique 3% vs LLM + sound verifier 36-38% | Stechly 2024 [d10] | E (K24) |
| Step judges fail on hard sets | ProcessBench F1 GSM8K / MATH / OlympiadBench: Skywork-PRM-7B 70.8 / 53.6 / 22.9; GPT-4o 79.2 / 63.6 / 51.4; o1-mini 93.2 / 88.9 / 87.2 | Zheng 2024 [d11] | E (K24) |
| Overconfident absolute self-scores, relative progress works better | progress verifiers about 5x more compute-efficient and 8-10% more accurate in beam search | Li 2026 [b24]; Setlur 2024 [d14] | S (K28) |
| Budget-aware width: shrink breadth as budget drains | BAVT, OSS-20B, 4 multi-hop QA sets: 5 tool calls EM 0.338 vs baseline 0.334 at 20 calls (baseline at 5 calls 0.194) | Li 2026 [b23, c20] | E (K12), preprint |
| Width set by sibling dispersion | Llama3.1-8B GSM8K tokens 8.22k -> 5.43k, time 114.75 -> 74.58 s (accuracy 90.14 -> 90.45); Qwen3-32B StrategyQA beam 64.33% -> 72.00% with 2.02k -> 1.64k tokens; up to 90% fewer tokens on MATH-500; most sibling similarity above 0.95 | Huang 2026 [b21, c19, critique 7] | E (K12) as budget control; single preprint |
| Merge near-duplicate siblings | Qwen2.5-1.5B MATH500: generated nodes 214.4 -> 31.1 (about 85% fewer), explored 53.3 -> 11.5 (about 78% fewer); GSM8K explored 19.5 -> 4.8; time speedup 2.26x vs DPTS; accuracy within about 5 points | Kim 2025 [b19, b20, d13] | S (K11), small open models, math only |
| Code-side checks prune cheaply and soundly | Thought of Search: Game of 24 1362/1362 in 1.92-6.83 s total; crosswords 20/20; Blocksworld 502/502; SCULPT prunes 34.2% of branches (+1 to +2 points); TabTracer tokens down 59-84% | Katz 2024, Fang 2026, Luo 2026, Long 2023 [c15, c21, c22, c23] | E (K10, K16) |
| Estimated LLM calls on Game of 24 (1362 tasks) | CoT/ReAct 1362, RAP 4086, ToT 245K, GoT 102K, LATS 68K | Katz [c16] | authors' formulas, not bills |
| Depth is the weak point | RAP 2/4/6-step: 1.00 / 0.86-0.88 / 0.26-0.42; PlanBench GPT-4 Blocksworld 34.3%, renamed 4.3%; o1-preview 97.8% small Blocksworld, 23.6% on 20-40 step (110 instances), $42.12 per 100 vs $0.02 for GPT-4o-mini | Hao [a25]; Valmeekam [c13, c14] | E (K15); the RAP "64% average" is unverified |
| Reported collapse of reasoning models with size | Hanoi collapse near N=8; River Crossing fails at N=3 | Shojaee 2025 [d15] | C (K26) |
| ... largely a format and instance artefact | 64k cap allows Hanoi N=12-13 as move list; N=15 as a function in under 5,000 tokens; River Crossing N>=6 unsolvable | Lawsen 2025 [d16] | C; short comment, no systematic numbers |
| LLM reasoning models search shallowly | 27 models, 1404 games, four-in-a-row: mean max depth 1.78 +- 0.71 plies (humans 4-6, inferred); win rate on breadth beta=0.075 (p=0.0025), on depth beta=-0.015 (p=0.82) | Chen 2026 [d05] | S (K19, K22), preprint |
| Their written deep lookahead barely changes the move | myopic model correct on 1236 turns vs 512 for full minimax; removing final-decision paragraphs 2.1% move change; removing whole chosen branch 32.0%; removing largest unchosen branch 1.2%; adding depth-1 paragraphs back 4.1%, deeper too 3.7% | Chen 2026 [d06] | S (K22) |
| Selective pruning and repair inside one controller | cap 16 calls: full 92.8 MATH at 5,280 tokens; no pruning 88.2 at 6,430; N=500 MATH: no repair 73.4% (4,650 tokens), no repair + matched extra expansion 74.6% (5,290), full repair 77.1% (5,280) | Ma 2026 [d12] | S (K23), unverified preprint, row alignment uncertain |
| Sampling with a checker gives most of the gain | SWE-bench Lite DeepSeek-Coder-V2: 15.9% (1 sample) -> 56% (250 samples); math 98.44% coverage at 10,000 samples | Brown 2024 [d19] | S (K29) |
| Training on search traces helps trained models | Searchformer Sokoban 93.7% optimal, up to 26.8% fewer steps than A*; Stream of Search Countdown 51.27% vs 25.73% | Lehnert [a28]; Gandhi [c24] | E (K18) but not transferable |
| LATS vs ToT, RAP: real feedback matters | HotpotQA (GPT-3.5): LATS 0.63; no LM heuristic 0.37; DFS 0.42; no reflection 0.58; HumanEval GPT-4 92.7 vs Reflexion 91.0; WebShop 75.9 vs 53.8 | Zhou 2024 [a26, a27, c08, c09] | E (K08). Table spread: ToT is 0.55, 0.39, 0.49 or 0.34 depending on table and k; do not quote one gap without naming the table |

---

## 4. Mechanisms and models

Each model below is written so it can be coded. Symbols: b = branches kept, d = depth, c = node or call budget, V = value.

### 4.1 Depth-limited planning with a stop probability (Huys 2012) [a04]

```
search(state, depth):
    if depth == 0 or random() < p_stop:        # per-depth coin
        return leaf_value(state)
    for each action a:
        s2, reward = step(state, a)
        if reward <= LARGE_LOSS and random() < p_prune_loss:   # extra stop after a big loss
            q[a] = reward                        # stop; nothing after it is counted
        else:
            q[a] = reward + gamma * search(s2, depth-1)
    return max(q)
```

Key point: the second coin is tied to a salient bad outcome, not to expected value. That is why it is a bias. In humans p_prune_loss was large and did not change with its cost.

### 4.2 Plan-until-habit (Keramati 2016) [a09, a10]

Plan to depth k. At depth k, return a cached value (habit value) instead of zero. Choose k from the time limit: k is smaller under pressure. Mix full planning and plan-until-habit with weights fitted per person. A pure cut with leaf value 0 predicts indifference at the first choice, which is not what people do.

For an LLM scaffold: at the cut, write a one-line rough estimate of the remaining value (or use a stored estimate for the problem class) and carry it up.

### 4.3 Fragmentation and memoization (Huys 2015) [a06-a08, b07]

```
plan(goal_depth D):
    choose subgoal state s* (a state about halfway; best split is the cheapest that still gives the optimal first move)
    plan first leg to s*  (cost of a small tree)
    plan second leg from s*  (small tree)
    cache each solved leg keyed by (start, end)
    on later problems: reuse cached legs before searching
```

Cost model: full tree d x 2^d (24 at d=3); the paper counts 10 operations for a 2-then-1 split. Pick the split per problem, not once for everyone (a shared split was worse than baseline by 116 iBIC).

### 4.4 Work budget (Snider 2015) [a14, a15]

Work W = (d+1)/r x 2^d, with d = depth and r = replan rate. For a fixed W, a deeper plan means fewer replans. Plan once at the start (front-load the thinking), then replan only when needed.

### 4.5 Value-of-information expansion (Sezener 2019; Keramati 2011) [a11, a12]

```
loop:
    for each leaf l: VUR(l) = expected rise in best-strategy value if l were expanded
                    (closed form for Gaussian leaf values N(mu, sigma^2))
    best = argmax VUR
    if VUR(best) < cost_per_expansion: stop
    expand best
```

Cost = eps x average reward. A branch that is very bad has little overlap with the best one, so its VUR is small. Pruning falls out. Myopic (one-step) because joint choice is NP-complete.

LLM proxy for sigma (untested): the spread among sibling continuations (Huang 2026 [c19]) or a relative-progress critic (Li 2026, Setlur 2024 [b23, d14]).

### 4.6 Gain x need (Mattar and Daw 2018) [a18]

Priority of a backup = gain (how much it changes the choice) x need (how likely we are to reach that state). Same shape as VUR. Use both: expand where the answer could change and where the search is likely to go.

### 4.7 Resource-rational best-first with a gap stop (Callaway 2022) [d03, d04]

```
frontier = paths seen so far with estimated values
repeat:
    expand the path with the highest value (best-first)
    gap = value(best) - value(runner_up)
    stop when gap > threshold(cost_per_expansion)
```

Threshold depends on expansion cost. Which classical order wins depends on variance placement: early variance -> breadth-first; constant -> best-first; late -> depth-first. Fixed-beam variants (Fixed iterations, Fixed depth, Fixed branching) were fitted as rivals in van Opheusden [d02]; the likelihood gap is in supplement tables that were not readable.

### 4.8 Tree of Thoughts, breadth-limited BFS (Yao 2023) [a22, c01]

```
states = [root]
for step in 1..T:
    candidates = [propose(s) for s in states]            # generator
    scored = [(evaluate(c), c) for c in candidates]      # sure / maybe / impossible, sampled several times
    states = top_b(scored)                               # prune to breadth b
return best(states)
```

Game of 24: T<=3, b<=5. DFS version for crosswords: prune when state evaluated "impossible", backtrack on dead end. Backtracking mattered more than the pruning rule (word 60% vs 20% without backtrack).

### 4.9 Budget-aware value tree (BAVT) [b23, c20]

Node value is raised to an exponent set by remaining budget ratio. Search moves from wide exploration to greedy as spend rises. A residual critic scores progress (change in value), not state quality. Absolute self-scores are overconfident.

### 4.10 Uncertainty-aware width (UAA) and duplicate merging (SSDP) [c19, d13]

```
siblings = sample m continuations from a state
dispersion = 1 - mean pairwise similarity(siblings)       # embedding, or score variance for closed models
width = clamp(f(dispersion), 1, b_max)                    # agree -> shrink, differ -> widen
merge siblings with similarity > theta, keep one representative
```

SSDP uses one hand-set threshold; the authors say it is dataset and model dependent.

### 4.11 Code-side pruning (Thought of Search; SCULPT; TabTracer; Long 2023) [c15, c21-c23]

Ask the model once to write `successors(state)` and `is_goal(state)` (about 1.2 interactions), then run plain BFS/DFS in code. Or keep an LLM-proposed tree but prune with symbolic checks (units, types, magnitude), state hashing, deduplication, and rollback to snapshots. Zero or near-zero model calls per node.

### 4.12 Reward-balanced width (REBASE) [c17, d07]

Allocate children to a node in proportion to softmax of its step reward; drop low-reward ones. No rollouts. Needs a step value from a trained reward model.

### 4.13 Controller with expand / prune / repair / stop (CoT2-Meta) [d12]

A training-free controller decides per node. Reported as a matched-token ablation: selective repair beats matched extra expansion by 2.5 points at the same tokens. Unverified by others.

---

## 5. What holds up

### 5.1 Replicated

- **Aversive pruning in humans.** Reproduced across samples: Huys 2012 (N=46), Huys 2015 (N=37), Lally 2017 (same recruited sample), Faulkner 2022 (31 healthy controls plus 30 depressed), Lavalley 2025 (49 controls, 40 patients, other site). Pruning present in every subject in Huys 2015 (37/37) [a06, a16, b10, d17]. Limit: all use the same 6-state maze, one lab family. No different-task replication and no independent-lab replication (K27). Pruning was never directly observed. It is the best-fitting model term.
- **Depth shrinks and leaf values appear under time pressure.** Keramati (N=30) and Snider (N=6) agree in direction. Both are tiny [K04].
- **Beam with state checks beats equal-cost sampling.** Game of 24 (Yao), HotpotQA (LATS, RAP), web agents (Koh), MATH with a trained step value (Wu, Snell), Game24 and PrOntoQA with a learned value (Feng). Five or more sources [K08, K23].
- **Gain peaks at medium difficulty and small budgets, and reverses on easy items.** Koh, Snell, Wu, plus the ToT GSM8K and SCULPT results [K13, K17].
- **Model-judged pruning loses true paths.** ToT crosswords, Stechly, ProcessBench, Koh's value-function ceiling [K09, K24].
- **Code checks prune soundly and cheaply.** Thought of Search, SCULPT, TabTracer, Long [K10, K16].

### 5.2 Failed or contested

- **Pruning and depression: refuted.** Huys 2015, Lally 2017 and Faulkner 2022 do not reproduce the 2012 BDI link; Faulkner's Bayes factors favour no group difference (0.27 for pruning, 0.26 for BDI) [K02]. Lally finds state anxiety instead (p=0.042). Do not build agent rules on a mood story.
- **Depth collapse of reasoning models: contested.** Shojaee's collapse is partly token limits, unsolvable instances and answer format (Lawsen) [K26]. Lawsen's comment is short and has no systematic numbers.
- **"Experts search deeper" versus "experts search the same amount and pick better."** Old claim (not opened) versus the new fitted-depth result. Depth is model-inferred in the new work, and van Opheusden notes it conflicts with lower depths in Snider's study [d01].
- **Pruning as separate Pavlovian process versus by-product of value of information (Sezener) versus pessimism about later choices (Zorowitz).** The accounts have never been tested against each other on human data [K07, K27].
- **Time pressure does not always help depth pay.** In van Opheusden, more time gave deeper plans but no better play, because feature drop rate also rose [d02].

### 5.3 Moderators

| Moderator | What changes | Source |
|---|---|---|
| Task difficulty | tree gain peaks at medium; reverses on easy | [c12, d08, d07] |
| Budget | beam beats best-of-N at 4-16 generations then falls behind; BAVT best at low tiers | [d08, b23] |
| Value quality | Koh 24.5 -> 43.5 as value improves; learned beats prompted by 44 points on Game24 | [c11, d09] |
| Judge strength | step-judge F1 falls from 70.8 to 22.9 (Skywork) as problems get hard | [d11] |
| Domain disguise | GPT-4 verifier FNR 20.7% (Game of 24) to 97.1% (disguised Blocksworld) | [d10] |
| Verify prompt | CoT verification lifts Game of 24 verifier accuracy to 98.8% | [d10] |
| Depth | human loss deficit rises 34 -> 40 -> 49% at depths 3-5; LLM RAP 0.88 -> 0.26-0.42 at 6 steps | [b13, a25] |
| Answer format | Hanoi as move list collapses near N=8; as a function works at N=15 | [d15, d16] |
| Reward structure | best strategy flips breadth/best/depth-first; human fragments may break under other rewards (untested) | [d04, a06] |
| Individual | pruning 4-93% across people; fragmentation differs by person | [b12, b09] |
| Reflection | CRT linked to less pruning (b=-0.036) | [b15] |
| Model size | cheaper judge works if the generator is strong; sibling merge tested only up to 8B open models | [a24, d13] |

### 5.4 Interventions that worked

- Check partial states in code (Thought of Search 1362/1362; Long 10/10 3x3 Sudoku) [c15, c23].
- Backtracking (crossword word success 60% vs 20% without) [c04].
- Relative-progress scoring over absolute self-score [b24, d14].
- Shrink breadth as budget drains (BAVT) [c20].
- Scale width by sibling dispersion (UAA) and merge duplicates (SSDP) [c19, d13].
- Per-difficulty choice of method: about the same as best-of-N with up to 4x less compute [d08].
- Value check with more samples: Koh value function SC n=20 gives 37.0 vs 28.5 without [c11].
- Sound external verifier: Game of 24 5% -> 36-38% [d10].

### 5.5 Interventions that did not work, or have no evidence

- Prompted self-critique loop: Game of 24 3% vs 5% for standard prompting [d10].
- MCTS with rollouts at matched FLOPs: loses to weighted sampling (Wu); lookahead rollouts underperform (Snell) [d07, d08].
- Search that over-optimises a weak judge: beam gets worse with budget on easy items [d08].
- Giving the model the algorithm in the prompt did not move the Hanoi collapse point (Shojaee), although the dispute stands [d15].
- Pruning on absolute self-scores (overconfident) [b24].
- Training on search traces: works, but needs training; not available to us [a28, c24].
- ToT on easy tasks: little gain for a lot of cost [c05].

### 5.6 Other weak spots

- Human depth and time studies are tiny (Keramati N=30; Snider N=6 with two authors).
- Callaway and van Opheusden were read as preprints; journal versions not opened.
- LLM comparisons are often matched by nodes or calls, not tokens (ToT's appendix is token-matched but the main tables are by samples).
- Several 2026 items (BAVT, UAA, SCULPT, TabTracer, CoT2-Meta, Chen) are single preprints.
- Tables for Feng, Stechly, ProcessBench and CoT2-Meta were garbled in extraction; values matched by row order. Recheck before quoting outside this folder.

---

## 6. Language models

### 6.1 Baselines: plain models cannot look ahead

- Game of 24, GPT-4: input-output 7.3%, chain of thought 4.0%, CoT self-consistency (k=100) 9.0% [a22]. About 60% of chain samples are already wrong after the first step [c02].
- PlanBench Blocksworld (2023): GPT-4 34.3% (206/600), Instruct-GPT3 6.8%. Renamed objects (Mystery): GPT-4 4.3% (26/600). Pattern recall, not search, is the likely cause [c13].
- o1-preview: 97.8% (587/600) on small Blocksworld, 52.8% Mystery, 37.3% Randomized Mystery, 23.6% on 20-40 step problems (110 instances), 40-111 s per instance, $42.12 per 100 instances vs $0.02 for GPT-4o-mini. Fast Downward solves 100% in 0.265 s [c14].
- Reasoning models in four-in-a-row search shallowly: 1.78 +- 0.71 plies on average; win rate follows breadth (beta 0.075, p=0.0025), not depth (beta -0.015, p=0.82). A myopic model predicts moves better than full minimax (1236 vs 512 turns). Deleting deep paragraphs changes the move 3.7% vs 4.1% with depth-1 paragraphs kept; deleting the whole chosen branch changes it 32.0% [d05, d06]. One game, preprint.

### 6.2 What changed performance, and by how much

| Change | Effect | Source |
|---|---|---|
| State-checked beam instead of samples | 49% -> 74% (Game of 24, GPT-4) | [c01] |
| Beam width 1 (greedy with a state check) | 45%, already most of the gain | [c01] |
| Backtracking in crosswords | word success 60% vs 20% | [c04] |
| Best-first tree on web tasks | +39.7% relative (VWA), +28.0% (WebArena), +51% at c=20 on the subset | [c10] |
| Better value function | 24.5% -> 43.5% (ground truth) | [c11] |
| REBASE vs sampling at lower FLOPs | 45.0 vs 42.8% (Mistral-7B) at 1.36e14 vs 8.70e14 FLOPs | [d07] |
| Learned value vs prompted value | Game24 64.8% vs 21.0% | [d09] |
| Per-difficulty method choice | about equal to best-of-N with up to 4x less compute | [d08] |
| Budget-aware width | 0.338 EM at 5 calls vs 0.334 baseline at 20 calls | [b23] |
| Sibling dispersion width | tokens 8.22k -> 5.43k at same accuracy; StrategyQA +7.7 points with fewer tokens | [b21] |
| Duplicate merge | about 78% fewer explored nodes | [d13] |
| Code-side tree | Game of 24 1362/1362 vs ToT 74-75% (on 100) | [c15] |
| Sound verifier replaces self-critique | 5% -> 36-38% | [d10] |
| Selective repair over matched extra expansion | 77.1 vs 74.6% at about the same tokens | [d12] |

### 6.3 What breaks

- **Judge errors cut the true path.** GPT-4 false-negative rates 20.7% (Game of 24), 15.5% (Blocksworld), 97.1% (disguised Blocksworld) [d10]. Step-judge F1 down to 22.9 on hard sets [d11]. The loss per path is not measured by task and judge size (gap).
- **Depth.** RAP 6-step 0.26 (10 iterations) to 0.42 (20) [a25]. Contested collapse on puzzles [d15, d16].
- **Easy items.** Beam gets worse with budget on MATH bins 1-2 [d08]; ToT gains 4 points on GSM8K at much higher cost [c05]; SCULPT gains 1.5 points at 21x tokens [c21].
- **Cost.** ToT creative writing about 5x the tokens of CoT [a24]. GPT-4 ToT $0.74 vs $0.47 for best-of-100 CoT [c03]. Estimated 245K LLM calls for ToT on 1362 Game-of-24 tasks [c16].
- **Duplicates.** Sibling continuations from one state are mostly copies (similarity above 0.95) [c19]. This links to G4 (one model's samples are not independent).
- **Needs real feedback.** LATS drops sharply without the LM heuristic (0.63 -> 0.37) and with DFS (0.42) [c09]. Tree search needs reversible state; web search has side-effect risk [c10, c22].

### 6.4 Not found

- No study runs the Huys loss-driven pruning task on an LLM [d20, c27]. "Does an LLM drop a branch behind an early vivid failure?" is open.
- No test of a one-line guess or cached value for a cut branch against a zero value, at equal tokens [d20].
- No clean beam-1 vs beam-3 with the same checker at equal tokens [K29].
- No test of sub-plan caching in LLMs [d16].
- No test of value-of-information expansion with an LLM proxy on non-math tasks [K28].

---

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status marks: [E] established, [S] single-source, [C] contested. Evidence ids from this folder.

### Add now (established)

| # | Take | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Prune by a code check on the partial state wherever the rules can be stated (units, types, constraints, dead-end flags, state hash). Use the model only to write the checker or the move generator. | G3, G5, S6 | [E] | K10, K16, K24; c15, c16, c21-c23, d10, d11 |
| A2 | Never prune on a model judgment alone. Judges miss true paths (15-20% of true states, 97% in a disguised domain, F1 22.9 on hard sets). If a judge must be used, keep a pruned-branch list and revisit it when no candidate passes (G6: submit best so far). | S6, G6 | [E] | K09, K24; a23, b17, c04, d10, d11 |
| A3 | Allow backtracking inside S6. It mattered more than the pruning rule (crossword word success 60% vs 20%). Keep state snapshots so undoing is cheap. | S6 | [E] | K09; c04, c22, c08 |
| A4 | Open the tree only where there is a foothold and the item is not easy. Gains peak at medium difficulty and low budgets, and reverse on easy items. Leave easy items to the plain path. | G12, S0, S6 | [E] | K13, K17; c12, d08, d07, c05, c21 |
| A5 | Set width and the search stop by remaining budget: wide early, greedy as the budget drains. Count the cost in model calls and tokens, not nodes. | S6, G7, G12 | [E] | K12; b23, c20, c10, a25, c16 |
| A6 | Check the very first expansion. About 60% of failing chains are already wrong after the first step. Put the state check at depth 1, then at later depths. | S6 | [E] | K08; c02, c01 |
| A7 | A tree beats equal-cost sampling only when partial states can be checked. If nothing can be checked, do not grow a tree; use independent short attempts and a vote (G11). | G11, G12, S6 | [E] | K08, K23, K29; c01, c03, d07, d09, d19 |
| A8 | Prune on a value or progress signal and do not use rollouts. Deep rollouts lose per FLOP. | S6 | [E] | K23; d07, d08 |
| A9 | Do not build rules on the pruning-depression story. Not replicated. | none | [E] (refuted) | K02; b10, b11, b12 |
| A10 | Do not plan to train on search traces. Searchformer and Stream of Search are trained models. | memory | [E] | K18; a28, c24 |
| A11 | Log, per run: depth reached, branches pruned, who pruned them (code or judge), and whether the final answer came from a revisited branch. Needed to judge each element at equal tokens (G7). | G7, logging | [E] design | K09 |

### Test first

| # | Candidate | Part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | **Affective-pruning guard.** Before cutting a branch that holds a vivid failure, evaluate its best continuation once (or say what you would do after that step). | G3, S6 | human [E] / LLM unknown | K01, K27; a01-a03, d18, d20 | Human result is large; no LLM test exists |
| T2 | **Leaf value for a cut branch.** A one-line rough estimate or cached class estimate instead of 0. | S6, memory | [S] | K05, K28; a10, b06, d09, d14 | Human theory only; no LLM test |
| T3 | **Expand where the answer could change.** Use sibling disagreement or a progress score as the proxy for value of information. Stop when the siblings agree. | S6 | [S] | K07, K11, K12; a12, c19, d13 | Simulation and math-only evidence |
| T4 | **Merge near-duplicate siblings** by code before scoring. | S6, G4 | [S] | K11; b19, d13 | Small open models; over-pruning unquantified |
| T5 | **Relative-gap stop rule** (expand best-first, stop when the lead over the runner-up exceeds a threshold). | S6 | [S] | K25; d03, d04 | Human data only; fixed beam is the rival |
| T6 | **Relative-progress scoring** over absolute self-scores for ranking children. | S6 | [S] | K28; b24, d14 | Trained or preprint evidence; LLM-only proxy untested |
| T7 | **Decompose and cache.** Split a deep problem into 2 legs, cache solved legs by (start, end), reuse. | S6, O3, memory | [S] | K06; a07, a08, b07 | Human data only |
| T8 | **Force a backed-up value from depth 2-3** for the top candidates into the choice. | S6 | [S] | K22; d05, d06 | Single preprint; written deep lookahead may be decoration |
| T9 | **Breadth before depth** under a small budget (more candidates at depth 1, not deeper chains). | S6 | [S] | K22; d05 | One game |
| T10 | **Write the deep plan as a procedure** instead of a full step list when the plan is long. | S6 depth cap | [C] | K26; d15, d16 | Format confound |
| T11 | **Cheap judge, strong generator.** Spend the strong model on proposals; a smaller model scores. | S6, G12 | [S] | K14; a24, c05 | One benchmark |
| T12 | **Re-read the whole state at each expansion** so extra depth does not come with lapses. | S6 | [S] | d02 | Human preprint |
| T13 | **Depth cap from a measured sweep** (not the [D] value of 2). Find the plan length where accuracy falls and cap below it. | S6 | [E] that depth is weak; cap value [D] | K15; a25, c13, c14 | Schema's depth 2 and 3 children are placeholders |

---

## 8. Concrete tests on our bench

All tests: two or more arms, same total tokens (setup counted, G7), same items, same model. Report accuracy, tokens, calls, and for pruning tests the number of true-path branches lost. Use the HTSA bench harness. Item types that exist for us: ARC items with an impasse, BRAINTEASER, plus puzzle sets we can make with a code checker (24-style, small constraint puzzles).

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| 1 | Matched-token breadth vs checking (K29) | 24-style puzzles; multi-hop QA; ARC items with a code check | best-of-k + checker; beam-1 + checker; beam-3 + checker | accuracy per 1k tokens, by difficulty bin | beam-1 + checker captures most of the gain; beam-3 adds on medium and hard bins only |
| 2 | Judge prune vs code prune | any task with a stated rule (Sudoku, 24, constraints) | LLM-judged prune; code-checked prune | accuracy, tokens, true-path loss rate | code prune equal or better, fewer tokens; judge loses true path in 10-20% of cases |
| 3 | Revisit list | crosswords-like or constraint puzzles with imperfect judge | judge prune only; judge prune + pruned list revisited on failure | accuracy; share of final answers from revisited branches | revisit list recovers some of the lost solutions (ToT: 3 of 4 missed solutions) |
| 4 | Affective-pruning guard (T1) | seeded early-failure items: an early branch shows a vivid failure, the best answer lies behind it. Text version of the Huys maze at depths 3, 4, 5 | no guard; "evaluate best continuation once before cutting"; "say what you would do after that step" | miss rate on the seeded items | if LLMs prune like humans, guard cuts the miss rate; if they do not prune, no change (still a useful null) |
| 5 | Depth sweep for the cap (T13, K15) | plan-length ladder, 2 to 10 steps | tree off; tree on; tree + procedure format | accuracy vs length; length where accuracy falls | find the depth where accuracy drops; set cap below it |
| 6 | Leaf value (T2) | multi-step puzzles where a cut is forced by budget | cut scored 0; cut gets one-line estimate; cut gets cached class estimate | accuracy at the same tokens | estimate beats zero when the cut falls on the true path |
| 7 | Difficulty gate (A4) | items stratified into easy / medium / hard by plain pass rate | plain; tree always; tree only on medium and low-foothold | accuracy per bin; total tokens | tree off on easy loses nothing and saves tokens; tree helps on medium |
| 8 | Budget-aware width (A5) | 24-style, multi-hop QA | constant width; width shrinking with remaining-token ratio | accuracy at 3 token budgets | shrinking width wins at the low budget; no loss at high |
| 9 | Dispersion width + duplicate merge (T3, T4) | math, QA, one non-math (ARC rule induction) | fixed width 3; dispersion width; dispersion + merge | tokens, accuracy, true-path loss | tokens down, accuracy flat on math; non-math is the open case |
| 10 | Relative-gap stop vs fixed beam (T5) | small suites, 4 paths x 5 steps | fixed width 3; best-first with gap stop | accuracy per token | gap stop spends fewer tokens when the lead is clear |
| 11 | Progress score vs absolute score (T6) | multi-step reasoning | rank children by absolute self-score; by "how much progress did this step make" | accuracy; rank agreement with ground truth | progress score ranks better |
| 12 | Decompose and cache (T7) | deep problems (6+ steps) with repeated sub-problems | one full search; two legs; two legs + cached legs across problems | accuracy, tokens | cached legs save tokens on later problems; one split per problem |
| 13 | Backed-up value ablation (T8) | candidate choice with 3-5 options | choose by depth-1 look; force depth-2 value into the choice; ablate | share of picks changed; accuracy | picks change little unless the value is forced in |
| 14 | Generator/judge swap (T11) | 24-style | strong gen + strong judge; strong gen + small judge; small gen + strong judge | accuracy | small judge costs little; small generator costs a lot |

---

## 9. What does not transfer, and why

- **The pruning reflex itself.** In humans it is fast, affect-linked (subgenual cingulate, insula) and person-specific (4-93%) [a17, b12, b14]. An LLM has no insula. Whether text models show anything like it is unknown. Transfer only the guard, and test it (T1).
- **Time pressure in milliseconds.** Keramati's 700 ms vs 2000 ms limit has no counterpart. The nearest analogue is a token budget, which is a different kind of cost.
- **Mood, anxiety and depression findings.** Not replicated for depression; anxiety link is one p=0.042 result in healthy adults [b12]. Nothing to use.
- **Trained search (Searchformer, Stream of Search, TS-LLM value networks, PRMs).** These need training. We scaffold only. Where a result depends on a trained value (Wu, Snell, Feng, Setlur), we get only the shape of the lesson, not the size of the gain [a28, c24, d07-d09, d14].
- **Memory-based habit values.** Keramati's cached values come from long training in one task. Our nearest thing is the class record and lessons (memory); a cached value is not available on a new class.
- **Human fragmentation measured with 9.7 ms pauses.** The timing evidence is thin and the fragments are inferred from choices. We take only the cost arithmetic (24 vs 10), not the claim that people do this [a07].
- **Four-in-a-row depth numbers.** Depth 4-6 plies is model-inferred and from one game. The LLM figure of 1.78 plies is from one game with judge-extracted trees. Do not set a depth number from either [d01, d05].
- **Web-agent trees.** Koh needs reversible state and risks side effects on real sites [c10]. Our bench is closed, so this is easier. The gain sizes may not carry.
- **Math-only efficiency results.** SSDP, UAA, SCULPT, REBASE: four small open models and math sets. Whether near-duplicate pruning holds for closed models or tasks where branches differ in wording but not meaning is open [d13].
- **Collapse results as a depth cap.** Contested [d15, d16]. Do not set the S6 depth cap from Shojaee.
- **Human simulation inside the head is not the same as written LLM reasoning.** Chen's deletion test suggests written deep lookahead can be decoration [d06]. A scaffold should not count text length as search depth.
- **Where gains come from.** ToT's 45% at b=1 shows much of the benefit is state checking, not the tree. Be careful not to credit width for what the check provides.

---

## 10. Open questions

1. Do LLMs show loss-driven pruning on a text Huys maze, and does "evaluate the best continuation first" remove it? No study found [d20].
2. At equal tokens, how much of tree-search gain survives against best-of-k with the same checker? Beam-1 vs beam-3 with a checker is missing [K29].
3. How often does a model-judged prune remove the true path, by task and judge size? Per-state rates exist (15.5%, 20.7%, 97.1%); per-path rates do not [d10-d12].
4. Does value-of-information expansion with an LLM proxy (sibling dispersion, progress critic) beat fixed width at equal tokens on non-math tasks? [K28]
5. What leaf value should a cut branch get in text planning: cached class estimate, one-line guess, or prior from memory? Does it beat zero? [K05, K28]
6. Does a relative-gap stop beat a fixed beam in an LLM? [K25]
7. Do near-duplicate merges hold for large closed models and non-math tasks? [K11]
8. Where does LLM search really collapse, once format and token limits are controlled? Does a procedure form push the limit? Does sub-plan caching? [K26]
9. Is there any independent-lab, different-task replication of aversive pruning? Does pessimism about later choices (Zorowitz) or pruning explain it? Human data could split them with modified trees. [K27]
10. Do the Nature versions of Callaway 2022 and van Opheusden 2023 change the numbers? Is the fixed-beam variant much worse than best-first in the supplement? [d02]
11. Does depth at the cap come with lapses? In van Opheusden extra time did not help because features were dropped. Does an LLM drop facts from a long search context in the same way? [d02]
12. Does Koh's medium-difficulty peak (easy +24%, medium +75%, hard +47%) hold for text planning and code? Snell and Wu show it for maths. [K13]
13. Does the 4-6 ply human depth vs 1.78 ply LLM depth gap matter for scores, or is breadth enough? [K22]
14. LATS comparison numbers vary with table settings (ToT 0.55 / 0.39 / 0.49 / 0.34). Which setting best matches ours? [critique]
15. RAP's "average 64%" is not reproduced by its listed numbers. Source of the 64%? [critique]
16. CoT2-Meta's matched-token ablation is unverified. Does selective repair beat extra expansion elsewhere? [d12]

---

## 11. Sources

[V] = opened and read this session (full text or PDF/HTML text). [M] = snippet, citation or recall only. Items marked "first pass only" were opened by the first-pass agents and not re-opened by the cross-checker.

### Human and cognitive

- [V] Huys et al. (2012) Bonsai trees in your head. PLoS Comput Biol. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002410 (PMC3297555: https://pmc.ncbi.nlm.nih.gov/articles/PMC3297555/)
- [V] Huys et al. (2015) Interplay of approximate planning strategies. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC4364207/
- [V] Keramati, Smittenaar, Dolan, Dayan (2016) Adaptive integration of habits into depth-limited planning. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC5111694/
- [V] Keramati, Dezfouli, Piray (2011) Speed/accuracy trade-off between habitual and goal-directed processes. https://pmc.ncbi.nlm.nih.gov/articles/PMC3102758/ (first pass only)
- [V] Sezener, Dezfouli, Keramati (2019) Optimizing the depth and direction of prospective planning using information values. https://pmc.ncbi.nlm.nih.gov/articles/PMC6440644/ (first pass only)
- [V] Snider et al. (2015) Prospective optimization with limited resources. https://pmc.ncbi.nlm.nih.gov/articles/PMC4569291/
- [V] Lally et al. (2017) Neural basis of aversive Pavlovian guidance during planning. J Neurosci. https://pmc.ncbi.nlm.nih.gov/articles/PMC5647774/
- [V] Mattar and Daw (2018) Prioritized memory access explains planning and hippocampal replay. https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620/ (first pass only)
- [V] Faulkner et al. (2022) A comparison of pruning during multi-step planning in depressed and healthy individuals. https://pmc.ncbi.nlm.nih.gov/articles/PMC9811346/
- [V] Lavalley et al. (2025) Computational mechanisms underlying multi-step planning deficits in methamphetamine use disorder. Transl Psychiatry. https://pmc.ncbi.nlm.nih.gov/articles/PMC12103525/
- [V] Zorowitz, Momennejad, Daw (2020) Anxiety, avoidance, and sequential evaluation. Comput Psychiatry. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8143038/fullTextXML
- [V] van Opheusden et al. (2021 preprint of Nature 2023) Revealing the impact of expertise on human planning with a two-player board game. https://osf.io/preprints/psyarxiv/rhq5j_v1/
- [M] van Opheusden et al. (2023) Expertise increases planning depth in human gameplay. Nature. https://www.nature.com/articles/s41586-023-06124-2 (page behind login, not read)
- [V] Callaway et al. (2021 preprint of 2022) Rational use of cognitive resources in human planning. https://osf.io/preprints/psyarxiv/byaqd_v1/
- [M] Callaway et al. (2022) Nat Hum Behav version. https://www.nature.com/articles/s41562-022-01332-8 (not read)
- [M] Newell and Simon (1972); de Groot (chess). Cited only; no URL.

### LLM and AI

- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Hao et al. (2023) Reasoning with Language Model is Planning with World Model (RAP). https://arxiv.org/abs/2305.14992 (first pass only)
- [V] Zhou et al. (2024) Language Agent Tree Search (LATS). https://arxiv.org/abs/2310.04406 (first pass only)
- [V] Koh et al. (2024/2026) Tree Search for Language Model Agents. https://arxiv.org/abs/2407.01476
- [V] Lehnert et al. (2024) Beyond A*: Searchformer. https://arxiv.org/abs/2402.14083 (first pass only)
- [V] Gandhi et al. (2024) Stream of Search. https://arxiv.org/abs/2404.03683 (first pass only)
- [V] Valmeekam et al. (2023) PlanBench. https://arxiv.org/abs/2206.10498 (first pass only)
- [V] Valmeekam, Stechly, Kambhampati (2024) LLMs Still Can't Plan; Can LRMs? https://arxiv.org/abs/2409.13373 (first pass only)
- [V] Katz et al. (2024) Thought of Search. https://arxiv.org/abs/2404.11833 (first pass only)
- [V] Long (2023) Large Language Model Guided Tree-of-Thought. https://arxiv.org/abs/2305.08291 (first pass only)
- [V] Wu et al. (2024/2025) Inference Scaling Laws. https://arxiv.org/abs/2408.00724
- [V] Snell et al. (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314
- [V] Feng et al. (2023/2024) AlphaZero-like Tree-Search can Guide LLM Decoding and Training (TS-LLM). https://arxiv.org/abs/2309.17179
- [V] Stechly, Valmeekam, Kambhampati (2024) On the Self-Verification Limitations of LLMs. https://arxiv.org/abs/2402.08115
- [V] Zheng et al. (2024) ProcessBench. https://arxiv.org/abs/2412.06559
- [V] Setlur et al. (2024) Rewarding Progress. https://arxiv.org/abs/2410.08146
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Shojaee et al. (2025) The Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen (2025) The Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250
- [V] Kim et al. (2025) Chopping Trees (SSDP). https://arxiv.org/abs/2511.08595
- [V] Huang et al. (2026) Uncertainty-Aware Budget Allocation for Efficient LLM Tree Search (UAA). https://arxiv.org/abs/2610.22858
- [V] Li et al. (2026) Spend Less, Reason Better: Budget-Aware Value Tree Search (BAVT). https://arxiv.org/abs/2603.12634
- [V] Fang et al. (2026) SCULPT. https://arxiv.org/abs/2601.12842 (first pass only)
- [V] Luo et al. (2026) TabTracer. https://arxiv.org/abs/2602.14089 (first pass only)
- [V] Ma et al. (2026) CoT2-Meta. https://arxiv.org/abs/2603.28135
- [V] Chen et al. (2026) Extracting Search Trees from LLM Reasoning Traces Reveals Myopic Planning. https://arxiv.org/abs/2605.06840

### Search log

- [M] d20: about 20 arXiv and Europe PMC queries for an LLM run of the Huys pruning task and for cut-branch leaf values returned no study. WebSearch was out of budget; OpenAlex and Semantic Scholar were rate-limited. An absence claim from a limited tool set.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 14 established claims: 12 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B05.07-K15** (reworded: the sources support less). PlanBench, o1 (97.8%, 23.63% on 20-40 steps, 40.43-111.11 s, $42.12) and RAP numbers match, but Lawsen's unsolvable-instance point applies to River Crossing N>=6, not to Shojaee's N=3 collapse, and Shojaee report models stay well under the 64k cap; Lawsen's Lua-function test is a preliminary test with no per-model numbers. Corrected claim: Depth is the weak point of LLM search and internal reasoning: RAP success falls from 0.88 (4-step) to 0.26-0.42 (6-step); PlanBench GPT-4 Blocksworld 34.3%, 4.3% when renamed; o1-preview 97.8% on small Blocksworld but 23.6% on 20-40 step problems at about 40-111 s per instance and $42 per 100 instances. Contested: Apple's collapse results (Hanoi N=8, River Crossing N=3) are disputed by Lawsen, who attributes the Hanoi collapse mainly to output-length and format limits and notes River Crossing instances with N>=6 and boat capacity 3 are unsolvable (which does not explain the N=3 collapse); Shojaee et al. say models stay well below the 64k token cap. A preliminary Lua-function test suggests the collapse depth depends on answer format.
- **B05.07-K17** (reworded: the sources support less). ToT GSM8K 90 vs 86 and SCULPT GPT-5.2 numbers match, but the BAVT 0.289-0.293 flat result is a parallel-sampling baseline on an instruct model that the paper attributes to low sample variance, not to task ease; SCULPT also gains +8 on MATH in the same table and is a workflow optimiser, not a reasoning tree. Corrected claim: On easy or saturated benchmarks tree search adds little or costs much: zero-shot ToT on GSM8K 90 vs CoT 86 (GPT-4, 100 questions); SCULPT with GPT-5.2 reaches GSM8K 97.8 vs 96.3 for plain IO at 24,142 vs 1,120 tokens per problem (though MATH 89.9 vs 81.8). Separately, BAVT's baseline on an instruct model stays flat across budgets (0.289 to 0.293 EM) because its samples vary little, which is not evidence about task ease.
