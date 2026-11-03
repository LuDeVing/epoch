# MCTS limits: deep document

*Subfield C05.04. Source files in this folder: evidence_a-d.jsonl (ids a01-d16), claims.jsonl (K01-K31), critique.md. Marks: [V] = page or PDF text opened this session; [M] = snippet or abstract only. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Schema parts: G = guardrail, S = state, O = operator (see research_notes/single_agent/SCHEMA.md).*

## 1. What it is

Monte Carlo tree search (MCTS) builds a search tree by repeating four steps: select a path with a bandit rule (usually UCT), expand a node, play out to the end (rollout), and back up the result as an average. It does not need a hand-made evaluation function. That is its strength. It is also the source of its limits.

The "MCTS limits" subfield asks where this method fails. The Wikipedia page gives the main cause: the tree grows in a selective, lopsided way, and values are averages of sampled outcomes. A single refuting move can be washed out by many good outcomes. The page also says the search has many parameters and no safe defaults (a01 [V]).

Four families of limit appear in the evidence:

1. **Trap blindness.** Averaging cannot see a narrow, forced loss a few moves deep. Evidence is mostly chess, 2010 era (a02, a03, b01-b04).
2. **Slow worst-case convergence.** Theory says UCT can be over-optimistic and need a tower of exponentials of trials in the worst case (a05, b10).
3. **Evaluator blind spots.** The search is only as good as its value signal. Superhuman Go programs keep exploitable blind spots (a08, a09). Learned step scorers and LLM judges for reasoning can be fooled (d05, d06).
4. **Cost and parameter sensitivity.** In LLM use, rollouts cost many tokens, depth degrades results, and settings such as the exploration constant matter (a13, b17, d09, d10).

Why this matters for our agent. The schema has an idea tree at S6 (operators O1-O8, at most 3 children, depth 2, 2 expansions). This document is the caution side of that design: when does a tree, scored by averages or by a model judge, lose to plain sampling plus a code check, and what guardrails follow.

Scope note. Basic UCT theory, AlphaZero, Tree of Thoughts and LATS appear here only where they test a limit. Related subfields run in parallel (Monte Carlo tree search; Pruning of decision trees; Chain-of-thought prompting; Learned refinement and self-verification). Links only, no coverage here.

## 2. History and theories in depth

**2002 to 2007: the bandit foundations.** Auer, Cesa-Bianchi and Fischer (2002) gave finite-time bounds for the UCB1 rule (a22 [M]). Kocsis and Szepesvari (2006) applied it to tree search and called it UCT, with convergence in the limit (a21 [M]). Browne et al. (2012) surveyed the field (a23 [M]). These three were not opened. Their claims reach us through later papers.

**2007: the first warning.** Coquelin and Munos (2007) showed that UCT with the usual confidence term can have a regret lower bound that is a composition of D-1 exponentials in depth D. With a square-root confidence term the bound is double exponential. For D = 20 the transition phase is about 10^156837 trials (a05, b10 [V]). Critique note: this is a worst-case constructed tree, not a typical one. It says convergence in the limit tells us nothing at small budgets. They proposed BAST and a modified UCT that do better under a smoothness assumption (a06). The smoothness constants are unknown for language.

**2010: the trap argument.** Ramanujan, Sabharwal and Selman (2010) defined a "trap" at level k: a move that looks fine to a sampler but loses by force against best play within k plies. They measured how often traps occur in chess and how UCT values them (a02-a04, b01-b03 [V]). A UAI 2010 follow-up used synthetic trees with planted critical nodes (b04, b05, c02). Ramanujan and Selman (2011) studied trade-offs, including the exploration constant, in Mancala, where UCT beat minimax (b06, b07, c03). The critique stresses this: UCT is not intrinsically weak. Trap blindness is game dependent.

**2012 to 2018: repairs.** Baier and Winands (2018) built MCTS-minimax hybrids that run a shallow minimax inside the tree or in rollouts. They are the cleanest evidence that trap blindness can be repaired by exhaustive shallow search (b08, b09, c05 [V]). Orseau, Lelis, Lattimore and Weber (2018) showed that in sparse-reward deterministic puzzles, sampled search degrades toward uniform search, and a bounded best-first enumeration (LevinTS) beats it (b11, b25).

**2016 to 2017: learned values.** AlphaGo and AlphaZero replace random rollouts with a learned policy and value network (a24 [M], a07 [V]). AlphaZero beat Stockfish while searching about 80 thousand positions per second against 70 million for Stockfish (a07). The standard reading is that the weakness was the value model, not the search loop (K06).

**2023 to 2025: blind spots persist.** Wang et al. (2023) trained "cyclic" adversaries that beat KataGo, a superhuman Go program, at high rates, including at high search budgets (a08, a10). Tseng et al. (2025) tried three defences; fresh adversaries beat each one (a09, b14, c08).

**2023 to 2026: MCTS for language models.** Tree of Thoughts (c09), RAP (a15), LATS (a17), AlphaZero-like decoding (a18), rStar (a19), web-agent tree search (a20), ReST-MCTS* (c29) and rStar-Math (d08) apply tree search to LLM reasoning. Results are mixed: Snell et al. (a12) found beam and lookahead search over-optimize against a process scorer; Wu et al. (a13) found MCTS costs dozens of times more tokens than voting; DeepSeek-R1's appendix reported that MCTS with a fine-grained value did not scale (a11, c13); Inoue et al. found standard MCTS loses to repeated sampling on ARC-AGI (b15).

**2022 to 2026: why search against a learned judge breaks.** Reward over-optimization (d04), master-key attacks on judges (d06), optimized suffixes on process reward models (d05) and the extreme-value effect in step selection (d14) give the mechanism. It is the same pattern as Go: the search finds the evaluator's blind spots.

Competing explanations for why tree search underperforms sampling in LLM work:
- The value signal is bad (most papers; supported by d01, d02, d05, d06).
- Rollouts waste tokens (a13, a26).
- Parameters were not tuned (d09, d10).
- The model is the wrong kind (d11: depth helps post-trained models, hurts base models).
- The task has no external signal (a17 vs b15).

These are not exclusive. No paper isolates them.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Shallow chess traps are common | Semi-random games: 7-10% of boards at 15-31 ply hold a trap at levels 1-7, up to 15% at 47 ply. 200 grandmaster games: about 12% at 47 ply. 200 games per condition. | a02, b01 (Ramanujan 2010) [V] | [S] |
| UCT undervalues traps | Value scale -1..1, ideal trap value -1. Level-3 board: trap move -0.250, UCT best -0.083, minimax-7 best -0.092. Level-5: -0.012 vs +0.020. Level-7: about -0.056 vs -0.066 on the extracted row. Four boards only. | a03, b02 | [S] |
| More samples do not fix it | At 10x minimax node count UCT trap value stays above -0.15 for level-5 and level-7 traps; only level 3 drops. About 70% of iterations go deeper than needed. | a04, b03 | [S] |
| Soft traps in expert play | 52% of 50 grandmaster games had at least one soft trap. MM-6-R beat MM-2-R 66%. | b04 [V] | [S] |
| Worst-case regret | Composition of D-1 exponentials (log bound); double exponential (sqrt bound); D=20 gives about 10^156837 trials. | a05, b10 [V] | [E] (K05) |
| Exploration constant has no safe default | Mancala best c = 2.5; c = 20 gives a minimax-like tree; small c gives an unfocused tree. Several hundred games per point. | b06 [V] | [E] (K20) |
| Minimax hybrids repair traps | Informed rollouts vs MCTS-Solver with random rollouts, 2000 games each: Catch the Lion 96.8%, Othello 79.9%, Breakthrough 75.4%. | b09 [V] | [E] (K03) |
| Alpha-beta still wins often | Hybrid vs enhanced alpha-beta, 1000 games each: Breakthrough 66.9%, Catch the Lion 17.4%, Othello 26.9%. | b08 | [S] (K04) |
| Learned value removes the chess gap | AlphaZero 80k positions/s vs Stockfish 70M; no losses to Stockfish in the reported match. | a07 [V] | [E] (K06) |
| Go evaluator blind spot | Cyclic adversary: 1048/1048 vs defended Latest with no search; 95.7% (1007/1052) at 4096 visits; 97.3% (1000 games) vs undefended Latest at 4096; 82% at 10^6 visits (50 games); 72% at 10^7 visits (50 games, small sample). Pass adversary 99.9% vs no-search KataGo. | a08, a10, b12, c07; critique corrections [V] | [S] (K07) |
| Patches do not close the class | 90% win with 26% of defence compute; 81% with 5%; 42% vs iterated-defence victim even at 65,536 visits; gift-adversary 91% vs dec23-victim at 512 visits. | a09, b14, c08 [V] | [S] (K08) |
| DeepSeek-R1 MCTS attempt | No benchmark numbers. Problems: step definition, step correctness, reward hacking. MCTS helps only with a pre-trained value model. | a11, c13 [V] | [S] (K09) |
| MCTS vs sampling on ARC-AGI | Budget 128 generations, Pass@2: sampling 15.0 (GPT-4o) and 18.6 (DeepSeek-V3); standard MCTS 9.0 and 14.0; AB-MCTS-M 12.3 and 16.0. Sampling plateaus near 512 generations while MCTS keeps improving. | b15, b16 [V] | [E] (K10) |
| MCTS vs sampling on code | Average rank over 6 settings: sampling 3.5, standard MCTS 4.2. But LiveCodeBench DeepSeek-V3 MCTS 43.2 vs sampling 40.7; CodeContest DeepSeek-V3 43.8 vs 43.2. MLE-Bench rank (3 tasks, GPT-4o, n=1): AB-MCTS-M 1.3, refinement 2.3, sampling 3.0, MCTS 3.3. | b15, c17 | [E] mixed (K10, K11) |
| Cost of rollouts | MATH500 Mistral-7B: sampling 256 samples 42.8% at 8.70e14 FLOPs; REBASE 32 samples 45.0% at 1.36e14. MCTS needs "dozens of times" more tokens. | a13, a26, c14 [V] | [S] (K12) |
| Beam search over-optimizes on easy items | MATH levels 1-2: beam degrades as budget rises; levels 3-4: helps; level 5: nothing helps. Lookahead cost counted as N x (k+1) samples. Budgets 4-256. Compute-optimal allocation beats best-of-N with about 4x less compute. | a12, a27, c15 [V] | [S] (K13) |
| Verifier false positives cap resampling | HumanEval+ (200 samples/task), MBPP+ (50/task). Best attempt count often under 10. Single-sample accuracy correlates with false-positive rate. | b19, c20 [V] | [E] (K14) |
| Verifier-backed sampling scales | SWE-bench Lite: 15.9% (1 sample) to 56% (250 samples) vs single-sample SOTA 43%. Without a verifier, voting and reward models plateau. | d07 [V] | [E] with K14 |
| Noisy step labels | Monte Carlo step labels worse than LLM-judge or human labels. Only 24% of RAP LLaMA2-7B GSM8K trajectories were judged correct. | b20, c22, a19, c31 [V] | [E] (K15) |
| Scorers miss earliest errors | ProcessBench, 3,400 cases: most open PRMs lose to prompted general models on hard problems; o1-preview misses 20-30% of wrong responses. Average F1: o1-mini 87.9, GPT-4o 61.9. | d01, d02 [V] | [S] (K25) |
| Planning degrades with length | Tight budget MCTS success L=2..12: 1.00, 0.92, 0.50, 0.11, 0.05, 0.00 (avg 0.43). Bi-Search avg 0.45. Loose budget L=12: MCTS 0.05, Bi-Search 1.00. | b17, b18, c18 [V] | [E] (K16) |
| RAP Blocksworld | LLaMA-33B, 2/4/6 steps: CoT 0.17/0.02/0.00; RAP(10) 1.00/0.86/0.26; RAP(20) 1.00/0.88/0.42. GPT-4 CoT 0.50/0.63/0.40. | a15, a16, c10 [V] | [E] with K16 |
| Budget failure modes | Tight budget: ToT-BFS 98% search exhaustion, DFS 92%, MCTS 52% exhaustion and 48% budget violation, bidirectional 92% budget violation. | c18, b17 | [S] (K17) |
| Search helps with a real signal | LATS HumanEval 92.7% Pass@1 (GPT-4); ToT Game of 24 GPT-4: IO 7.3, CoT 4.0, CoT-SC 9.0, ToT b=1 45, b=5 74; web agents VWA 18.9 to 26.4 (+39.7% rel), WA +28.0% rel. | a17, c09, a20, c19 [V] | [E] (K18) |
| Self-critique hurts; sound check helps | GPT-4, 100 items per domain. Game of 24: standard 5%, LLM+LLM critique 3%, sound verifier 36-38%, k=25 sampling 42%. | d03 [V] | [E] (K26) |
| Evaluator exploitable | Optimized 100-token suffix lifts PRM reward above 0.9 on flawed reasoning (training reward 0.11 to 0.95); master-key answers give judge false positives up to 35% (punctuation, GPT-4o) and 60-90% ("Thought process:"). 43% of RL reward gain is style. | d05, d06, d04 [V] | [E] (K27) |
| Large budgets can reverse scaling | GSM8K large budget: AlphaZero-style 53.6%, ReSCALE 58.4%, Best-of-N 53.4%. Game24: 82.9 vs 85.3. Default UCT C=1 failed on Blocksworld; tuned C gave +5.27 (of +25.00 total). | d09, d10 [V] | [E] (K28) |
| Good PRM can flip the result | rStar-Math 7B: MATH 58.8 to 90.0; ablation MCTS with PPM 89.4 vs ORM best-of-N 82.6 (not budget matched). Code-PRM study: MCTS > beam > best-of-N > vote as budget rises. | d08, b21, c29 | [C] (K24) |
| Depth depends on model type | DeepMath level 9, equal tokens, Pass@16: Qwen3-4B base 0.9004 baseline vs 0.6377 with entropy branching (-29.2%); instruct +0.65%; range +0.5% to +39% for instruct/RLVR, -10% to -29% for base. | d11 [V] | [S] (K29) |
| First step matters | Forced wrong first step: R1-Distill-7B 94.8 to 28.5; 1.5B 95.4 to 64.4; 32B 100 to 85.8; Qwen3-235B 100 to 78.7. | d12 [V] | [S] (K30) |
| Sudoku vs CountDown | Backtracking DFS solver gets 97% of Sudoku boards, 57% of CountDown questions; backtracking wins Sudoku, loses CountDown at fixed tokens. | c16 [V] | [S] (K22) |
| Sparse puzzles | Sokoban 1000 levels: uniform 88; LubyTS(512,32) 884 +/- 4 (11.5M expansions); LevinTS 1000 (6.6M); LAMA 1000 (3.15M). | b11, b25 [V] | [S] (K19) |
| Pruning errors are systematic | ToolTree calibrated gap threshold +4.38 utility points; CI excludes zero only at budgets B100 and B200. | b23, c25 (2026 preprint) | [S] (K21) |
| Diversity-keeping selection | Robust selector beat outcome- and step-level baselines in 14 of 16 settings (theory plus experiments). | d14 (abstract and intro only) [M] | [S] (K31) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build or test it.

**4.1 UCT selection and why averages hide traps.** At each node pick the child that maximises mean_value + c * sqrt(ln(N_parent) / N_child). The mean is over all rollouts through that child. A trap child has one refuting reply among many replies. If most rollouts from that child win, the mean stays high. The refutation is found only if the search samples that one reply deeply enough. Ramanujan found that wasted depth grows about exponentially with trap depth (b03), because the search goes deep into lines that looked good first. A minimax search of depth k finds a level-k trap exactly because it takes the minimum over replies, not the mean.

**4.2 The minimum-versus-mean rule.** Implementation: the backup value for a node where the opponent (or an adversarial check) chooses is the minimum over children, not the mean. Hybrids put minimax of depth 1-2 in the selection or rollout step (b08, b09). For an LLM agent the analogue is: a candidate answer or plan step gets a score equal to its worst test result, not its mean test result. A mean over tests hides one failing test.

**4.3 Rollout cost accounting.** In LLM search a rollout is a full generation. Count every generated token in the budget, including rollouts, value calls and critique calls. Wu et al. note standard MCTS rarely reaches final answers inside a rollout, so it spends many tokens per node (a13, a26). REBASE avoids rollouts by sampling children in proportion to a reward-balanced weight and used about 6x fewer FLOPs at higher accuracy (a13). Lookahead cost in Snell is N x (k+1) samples (a12).

**4.4 Evaluator over-optimization (the extreme-value effect).** Take n candidates scored by a noisy scorer. The top-scored one is partly a lucky error. As n and depth grow, the chance that the top prefix is spuriously high grows (d14, d04). Gold reward follows R(d) = d(alpha - beta*d), d = sqrt(KL), for best-of-n (d04): it rises, then falls. Fixes: keep two or more branches per step instead of pruning to the top (d14, 14 of 16 settings), cap the number of candidates ranked by a noisy scorer, and use an independent check at the end.

**4.5 Exploit search against the evaluator.** Go adversaries train a policy that wins by reaching positions the value net misjudges; cyclic groups are one such class (a08). For LLMs, suffix strings and master-key tokens raise scores without improving content (d05, d06). Audit procedure: search for inputs that maximise the judge score while failing a ground-truth check; report the fooled rate; re-run on a held-out attack family after any patch (a09, d06).

**4.6 Hybrid with an exhaustive shallow check.** Run the sampled search, then apply a code check that tries to refute the top candidate at depth 1-2 (counterexample, held-out test, mutated input). If refuted, drop it and take the next. This is the LLM version of MCTS-Solver plus minimax (b08, d03). A sound check also lets plain resampling scale near log-linearly (d07).

**4.7 Exploration and width.** UCT constant: best c = 2.5 in Mancala, c = 20 gives minimax-like (b06); default C = 1 failed on Blocksworld and tuned C added 5.27 points (d10). Adaptive branching (AB-MCTS) decides at each node whether to go wider (sample a new child) or deeper using a Bayesian posterior over child quality. It beat plain MCTS and repeated sampling on CodeContest from budget 32 and on three MLE-Bench tasks (b16, c17). Root selection also matters: Gumbel top-k plus sequential halving at the root restored monotonic scaling where an AlphaZero-style root rule declined (d09).

**4.8 Depth and cost budgets.** Under a tight cost cap, success falls from 0.92 to 0.11 between plan lengths 4 and 8 (b17). The failure is not only wrong answers: 48% of MCTS runs violated the budget (c18). Cost caps need a hard stop in code, not in the prompt.

**4.9 Bounded best-first enumeration (LevinTS).** Expand nodes in order of depth divided by policy probability (Levin cost), with a guaranteed bound on expansions. Used where reward is sparse and deterministic and sampled search drifts to uniform (b11). Needs a policy distribution over actions. For an LLM that means token or step probabilities, which our deployed models may not expose.

## 5. What holds up

**Multi-source (established):**
- Resampling against an imperfect verifier is capped by its false-positive rate; the best attempt count is often under 10 (b19, c20, d02, d03, d06, d07; 4 sources) [E].
- Step-level evaluators are noisy and exploitable (d01, d05, d06, b20, c22, a19, c31; 3+ sources) [E].
- Planning success falls steeply with length (b17, a15; 2 sources) [E].
- Search pays where a real environment or test signal exists (a17, a20, c09; 3 sources) [E].
- Sound external verification beats LLM self-critique (d03, d02) [E].
- Parameters (c, root selection, width) are task specific (b06, d09, d10) [E].
- A learned value largely removes the chess weakness (a07, c06) [E].

**Single source, no independent replication:**
- All trap-frequency numbers (chess, 2010, one group). The trap utility table rests on four boards (critique).
- Adversarial Go: one lab and one network lineage. The 72% at 10^7 visits is only 50 games.
- Cost-awareness (Zhang et al.): one group.
- PAC-CF pruning calibration: a 2026 preprint with a CI excluding zero at only two budgets.
- REBASE FLOPs table: one group.

**Failures and contradictions:**
- MCTS vs sampling: ARC and GPT-4o code favour sampling (b15). DeepSeek-V3 code favours MCTS (43.2 vs 40.7 on LiveCodeBench). A good code PRM favours MCTS (b21). Mixed.
- Hybrids help most where traps are dense (Catch the Lion), yet alpha-beta still beats the hybrid there (17.4% hybrid win). Repairing traps does not make MCTS beat exhaustive search (b08).
- UCT beats minimax in Mancala (b06). Trap blindness is not universal.
- Backtracking wins Sudoku and loses CountDown (c16). No single search style.
- rStar-Math works with MCTS where R1's token-level MCTS did not (d08 vs a11). The reconciliation (a trained step value from code-verified outcomes) is plausible but untested.
- Illusion of Thinking (d15) reports collapse beyond a complexity level; critics blame token limits and unsolvable instances. Disputed. Not an MCTS paper.

**Interventions that worked:** shallow minimax hybrid (b09); sound external verifier (d03, d07); rollout-free reward-balanced tree (a13); adaptive width (b16); tuned UCT constant (+5.27, d10); Gumbel root plus halving (d09); diversity-keeping selection (d14); compute-optimal allocation by difficulty (a12, about 4x less compute).

**Interventions that did not:** more rollouts for deep traps (a04); patching one Go exploit (a09); LLM-critique self-verification (d03); fine-grained token-level MCTS without a pre-trained value (a11); default UCT constants (d10); beam search on easy items (a12); Master-RM patching beyond its own attack family (d06).

**Moderators:** verifier quality (largest); presence of an external signal; task structure; model type (base vs post-trained, d11); item difficulty (a12); budget size (d09, d10).

## 6. Language models

**What LLM tree search looks like.** A state is a partial reasoning chain or a plan prefix. Actions are generated continuations. Values come from one of: a prompted LLM self-evaluation, a trained PRM, an outcome check that runs code or tests, or a learned value head. The limit story depends almost entirely on which value is used.

**With a real signal, search helps.**
- LATS with HumanEval tests: 92.7% Pass@1 (GPT-4). HotPotQA: LATS (n=5, k=50) 0.63 vs ReAct 0.42, CoT-SC 0.40 (a17).
- Web agents: VWA 18.9 to 26.4 (+39.7% relative), WA +28.0% relative, Llama-3-70B +119.7% relative; search can use up to 20x more LM calls (a20, c19).
- ToT Game of 24 with GPT-4: 74% vs CoT 4% (c09). But plain k=25 sampling with a sound check reached 42% in a separate GPT-4 test (d03). ToT includes a check of the arithmetic. This weakens the claim that the tree structure itself adds value.

**Without a real signal, search often loses to sampling.**
- ARC-AGI, no feedback: standard MCTS 9.0 / 14.0 vs sampling 15.0 / 18.6 Pass@2 (b15).
- Self-critique loops lowered accuracy (d03).
- DeepSeek-R1 abandoned MCTS for token-level reasoning (a11).
- RAP LLaMA2-7B: only 24% of trajectories correct on GSM8K (c31).

**Scorer problems.** ProcessBench: most open PRMs lose to prompted general models on hard Olympiad items (d01). Frontier models verify poorly out of the box, but self-verification improves with more samples (d02). Optimized suffixes drive PRM reward above 0.9 on flawed reasoning (d05). Judge false positives reach 35-90% under master keys (d06).

**Budget.** Rollouts are expensive. REBASE reached 45.0% at 1.36e14 FLOPs vs sampling 42.8% at 8.70e14 (a13). Under a tight cap MCTS had 48% budget violations (c18). Token accounting differs between papers (generations, FLOPs, node expansions), so none of these comparisons share a unit (critique).

**Depth.**
- Plan length: MCTS 0.92 at L=4, 0.11 at L=8 (b17). RAP LLaMA-33B 0.88 at 4 steps, 0.42 at 6 with 20 iterations (a15).
- First-step sensitivity: a forced wrong first step cuts R1-Distill-7B from 94.8 to 28.5 and Qwen3-235B from 100 to 78.7 (d12). This is a trap analogue, though injected, not natural.
- Later alternative solutions in a chain can mislead a correct first solution: Llama-distilled-70b row 21.2 / 77.9 / 0.9 (misleads / neutral / helps; column labels inferred) (d13, intro and Table 1 only).
- Model type: depth lifts instruct and RLVR models (+0.5% to +39%) and hurts base models (-10% to -29%) at equal tokens (d11).
- Reasoning models collapse beyond a complexity level (d15, disputed).

**What changed the result, by how much.** Sound verifier: Game of 24 from 3% (LLM critique) to 36-38% (d03). Tuned UCT constant: +5.27 (d10). Trained step value: rStar-Math 89.4 vs ORM best-of-N 82.6, not budget matched (d08). Root rule: 58.4 vs 53.6 (d09). Compute-optimal allocation: about 4x compute saved (a12). Hybrid minimax: up to 96.8% win rate (b09; games, not LLMs).

**Not yet measured.** Nobody has built chess-style one-fatal-step items for LLM reasoning (critique gap 1). Nobody has measured natural trap density in reasoning or debugging trees (gap 8). There is no clean MCTS vs sampling comparison on frontier long-chain reasoning models (gap 9). There is no numeric crossover of verifier false-positive rate where tree search wins (d16).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Ids refer to claims.jsonl (K) and the evidence files.

### Add now (established)

1. **A selected answer must pass a code check that tries to refute it, and the score is the worst test, not a mean or a judge score.** Part: G3, S4, S8. Status [E] for "sound external checks beat model judges" (K26, K14, K27; d03, d07, d06). The "worst test" detail is [S] (K03; b09) and goes to Test first. Evidence ids: K26, K14, K27.
2. **Cap attempts by the checker's false-positive rate.** Part: G2/G3, S3. Status [E] (K14; b19, c20, d02, d03). Keep attempts under 10 per item until we measure our checker. Agrees with G11.
3. **Never use the generating model's own judgement as the value function in a tree.** Part: G5, G8, S7. Status [E] (K15, K27, K26; d01, d05, d06, b20, c31). Already in G5. New part: evaluators are actively exploitable, so more search raises the risk.
4. **Count rollout, value and critique tokens, including discarded branches, inside the budget when comparing arms.** Part: G7, section 6 logging. Status [E] as a rule of method (a13, a26, c18); the 'dozens of times' figure itself is [S] (K12).
5. **Gate tree search on an external signal and on estimated difficulty.** Part: G12, S0. Status [E] (K18, K10, K13; a17, a20, b15, a12). G12 says "foothold" (base rate above zero). Add: also require a test or environment signal.
6. **Do not scale tree budget blindly.** Part: G11/G12. Status [E] (K28; d09, d10). Plot accuracy against budget on a held-out set; stop when the curve bends.
7. **Keep the S6 limits (3 children, depth 2, 2 expansions).** Planning success falls steeply by length 6-8 (K16 [E]; a15, b17). Depth 2 sits in the safe zone.
8. **Hard stop on budget in code, not in the prompt.** Part: G7, S6. Numbers are [S] (K17; c18, b17); rule is design.

### Test first

| Item | Part | Status | Evidence | Why test |
|---|---|---|---|---|
| Worst-test (minimum) scoring vs mean at S7 | S7 | [S] | K03, K01; b08, b09 | trap result is from games only |
| Shallow exhaustive refutation pass on the top candidate before submit | S8 | [S] for open tasks | K03, K26, K30; b09, d03, d12 | strong in games and Game of 24; untested on open tasks |
| Code check on the first committed step | S3/S4 | [S] | K30; d12 | wrong step was injected, not natural |
| Keep 2+ branches per expansion instead of pruning to the top score | S6 | [S] | K31, K21; d14, c25 | d14 read only to abstract and intro |
| Adaptive width (wider vs deeper) in the S6 tree | S6 | [S] | K11; b16, c17 | one group; mixed on ARC |
| Held-out adversarial audit of our own judge or checker | G3/G5 | [S] for our evaluator; [E] others are exploitable | K27, K08; d05, d06, a09 | no data on our model |
| Depth vs breadth by model type | G11/G12 | [S] | K29; d11 | Pass@16, tuned on one model |
| No pruning without a calibrated margin | S6 | [S] | K21; c25 | preprint; CI barely excludes zero |
| Backtracking vs parallel by task structure | S0/S6 | [S] | K22; c16 | one paper |
| "MCTS beats sampling with a good PRM" | none | [C] | K24; b21, d08 | do not adopt; we have no PRM |

Do not add now: UCT or any bandit selection over LLM-scored nodes (K09, K13, K28), rollout-based MCTS (K12), pruning by judge score (K21, K27), LevinTS (needs policy probabilities, K19).

## 8. Concrete tests on our bench

All arms get the same total tokens, including rollouts, judge calls and setup. Report paired item-level comparisons. Item sets: ARC subset (held-out example check), BRAINTEASER (no check), code or planning items with tests.

1. **Fatal-refutation items (K01, K25, K30).** Item type: 20 problems where a natural first step looks right and has one exact refutation (a test or counterexample). Arms: (A) plain sampling and vote; (B) sampling plus LLM-judge scoring of steps; (C) sampling plus code refutation of the top candidate. Metric: share of final answers that carry the fatal flaw. Expected: B accepts the flaw more often than C; C near zero. If B is no worse than C, trap blindness does not appear in our setting.
2. **Tree vs sampling (K10, K11, K18).** Item type: ARC subset with held-out check plus 20 code items with tests. Arms: (A) k independent attempts with code selection; (B) S6 idea tree with code tests as value; (C) same tree with an LLM judge as value. Metric: pass rate on the unfitted part. Expected: B >= A on code with tests; C < A on ARC; A >= B on ARC.
3. **Verifier false-positive sweep (K14, d16).** Item type: items with a weak checker (public tests) and a strong checker (public plus hidden). Arms: attempts 1, 2, 4, 8, 16, 32 selected by the weak checker. Metric: strong-checker pass rate vs attempts. Expected: curve peaks under 10 attempts and bends down when false positives are high. Output: our checker's false-positive rate and the attempt cap.
4. **Min vs mean selection (K03, K01).** Item type: items with several unfitted tests per candidate. Arms: (A) select by mean test pass; (B) remove any candidate that fails a critical test; (C) vote. Metric: final accuracy. Expected: B >= A where one critical test exists; equal elsewhere.
5. **Parameter sensitivity (K20, K28).** Item type: 30 planning items. Arms: tree width 2, 3, 5 and depth 1, 2, 3, plus sampling. Metric: accuracy at equal tokens and the spread of the best setting across tasks. Expected: best settings differ by task; the default fails on at least one.
6. **Depth cap (K16, K31).** Item type: planning items with plan length 2 to 10. Arms: depth 1 to 4 with a code check at each depth vs a check only at the end. Metric: success by length. Expected: success collapses past some length; per-depth checks flatten the slope.
7. **Adversarial judge audit (K27, K08).** Item type: 50 wrong answers with master keys or style strings appended, on our judge. Arms: raw judge vs blind, length-normalised judge (G5). Metric: false-positive rate. Expected: raw judge 20-60% (range from d06); G5 version lower. Re-test on a held-out attack family after any patch.
8. **Diversity-keeping prune (K31).** Item type: 40 items with a noisy scorer. Arms: keep top 1; top 2; top 2 by diversity. Metric: accuracy at equal tokens. Expected: diverse top 2 >= top 1 as depth grows.
9. **Difficulty gate (K13).** Item type: items bucketed by plain pass rate. Arms: search always on; search only in middle bins; no search. Metric: accuracy at equal tokens. Expected: always-on loses on easy bins; nothing helps on the hardest bin.
10. **Model-type probe (K29).** Item type: one hard set; measure answer diversity over 16 iid samples; run depth vs breadth at equal tokens. Metric: Pass@16 and single-answer accuracy. Expected: depth helps only if base diversity is low.

## 9. What does not transfer, and why

- **Trap frequency numbers.** 7-15% of chess positions is a chess fact. Reasoning chains have no adversary and no minimax structure. No one has measured trap density in language or code trees (critique gap 8).
- **Go adversarial win rates.** One lab, one network family, a fixed-rule game. The lesson (search finds evaluator blind spots) transfers as a design caution, not as numbers.
- **Worst-case regret 10^156837.** A constructed tree. It proves that convergence in the limit says nothing at small budgets. It is not a cost estimate.
- **AlphaZero beating Stockfish.** Needs huge self-play training for a value net. We have no trained value function and cannot train one.
- **rStar-Math, ReST-MCTS*, PRM-guided MCTS.** Four rounds of policy and value training are a large fixed cost (d08). Our scaffold does not train.
- **DeepSeek-R1 result.** Concerns token-level MCTS in a training context.
- **LevinTS and policy-based enumeration.** Needs policy probabilities and deterministic dynamics.
- **MCTS-minimax hybrid win rates (96.8%).** Game win rates against another program. They show repair is possible, not how much it gives LLM reasoning.
- **Pass@16 and coverage numbers (d07, d11).** Coverage is not accuracy unless a verifier selects the answer.
- **Illusion of Thinking collapse (d15).** Controlled puzzles; disputed; not MCTS.
- **Most LLM comparisons use GPT-4o, DeepSeek-V3, Llama-2 or Mistral-7B** (critique gap 9). Frontier long-chain reasoning models may behave differently.

## 10. Open questions

1. Does trap blindness occur in LLM reasoning search? Needs one-fatal-step items and a measured accept rate (critique gap 1, K25).
2. At what verifier false-positive rate and difficulty does tree search beat plain sampling at equal total tokens? Only brackets exist (d16).
3. Does a shallow exhaustive check on a sampled chain recover most of the loss on open tasks, as hybrids do in games?
4. Where should depth be capped, and does the cap depend on scorer noise (K31) or on branching complexity (d15)?
5. How task specific are exploration constant, width and rollout count for LLM tasks?
6. Is the evaluator blind spot a fixed class that survives patching, as in Go? Master-RM fixed its own family only (d06). Not tested on our judge.
7. Which of the R1, rStar and ReST-MCTS results survive with a code-checked value? rStar-Math suggests yes (d08) but has no equal-token comparison with sampling.
8. What is the natural trap density in reasoning or debugging trees?
9. Do MCTS vs sampling results on 2025-26 long-chain reasoning models still favour sampling?
10. Is the first-step effect (d12) general fragility or an artifact of injecting a wrong answer (changed by 1 or 10)?

## 11. Sources

[V] = opened this session (per evidence files). [M] = snippet or abstract only. Evidence ids in brackets.

1. [V] Wikipedia, Monte Carlo tree search (a01, a25). https://en.wikipedia.org/wiki/Monte_Carlo_tree_search
2. [V] Ramanujan, Sabharwal, Selman (2010) On Adversarial Search Spaces and Sampling-Based Planning, ICAPS (a02-a04, b01-b03, c01). https://cdn.aaai.org/ojs/13437/13437-40-16955-1-2-20201228.pdf ; https://www.cs.cornell.edu/~raghu/Raghuram_Ramanujan_files/icaps10.pdf
3. [V] Ramanujan, Sabharwal, Selman (2010) Understanding Sampling Style Adversarial Search Methods, UAI (b04, b05, c02). https://arxiv.org/abs/1203.4011
4. [V] Ramanujan and Selman (2011) Trade-Offs in Sampling-Based Adversarial Planning, ICAPS (b06, b07, c03). https://www.cs.cornell.edu/~raghu/Raghuram_Ramanujan_files/icaps11.pdf
5. [V] Coquelin and Munos (2007) Bandit Algorithms for Tree Search, UAI (a05, a06, b10, c04). https://arxiv.org/abs/cs/0703062
6. [V] Baier and Winands (2018) MCTS-Minimax Hybrids with State Evaluations, JAIR 62 (b08, b09, b24, c05). https://jair.org/index.php/jair/article/view/11208
7. [V] Silver et al. (2017) Mastering Chess and Shogi by Self-Play (a07, c06). https://arxiv.org/abs/1712.01815
8. [V] Wang et al. (2023) Adversarial Policies Beat Superhuman Go AIs, ICML (a08, a10, b12, b13, c07). https://arxiv.org/abs/2211.00241
9. [V] Tseng et al. (2025) Can Go AIs Be Adversarially Robust? (a09, b14, c08). https://arxiv.org/abs/2406.12843
10. [V] Orseau, Lelis, Lattimore, Weber (2018) Single-Agent Policy Tree Search With Guarantees (b11, b25, c27). https://arxiv.org/abs/1811.10928
11. [V] DeepSeek-AI (2025) DeepSeek-R1, appendix (a11, c13). https://arxiv.org/abs/2501.12948
12. [V] Snell et al. (2024) Scaling LLM Test-Time Compute Optimally (a12, a27, c15). https://arxiv.org/abs/2408.03314
13. [V] Wu et al. (2025) Inference Scaling Laws, ICLR (a13, a14, a26, c14). https://arxiv.org/abs/2408.00724
14. [V] Hao et al. (2023) Reasoning with Language Model is Planning with World Model, RAP (a15, a16, c10). https://arxiv.org/abs/2305.14992
15. [V] Zhou et al. (2024) Language Agent Tree Search (a17, c11). https://arxiv.org/abs/2310.04406
16. [V] Feng et al. (2023) AlphaZero-Like Tree-Search can Guide LLM Decoding and Training (a18, c12). https://arxiv.org/abs/2309.17179
17. [V] Qi et al. (2024) rStar: Mutual Reasoning Makes Smaller LLMs Stronger (a19, c31). https://arxiv.org/abs/2408.06195
18. [V] Koh et al. (2024) Tree Search for Language Model Agents (a20, c19). https://arxiv.org/abs/2407.01476
19. [M] Kocsis and Szepesvari (2006) Bandit based Monte-Carlo planning (a21). https://link.springer.com/chapter/10.1007/11871842_29
20. [M] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem (a22). https://link.springer.com/article/10.1023/A:1013689704352
21. [M] Browne et al. (2012) A Survey of Monte Carlo Tree Search Methods (a23). https://ieeexplore.ieee.org/document/6145622
22. [M] Silver et al. (2016) Mastering the game of Go (a24). https://www.nature.com/articles/nature16961
23. [V] Inoue et al. (2025) Wider or Deeper? Adaptive Branching Tree Search (b15, b16, c17). https://arxiv.org/abs/2503.04412
24. [V] Zhang et al. (2025/2026) Cost-Awareness in Tree-Search LLM Planning (b17, b18, c18). https://arxiv.org/abs/2505.14656
25. [V] Stroebl, Kapoor, Narayanan (2024, rev. 2026) The Limits of Inference Scaling Through Resampling (b19, c20). https://arxiv.org/abs/2411.17501
26. [V] Zhang et al. (Qwen team, 2025) Lessons of Developing Process Reward Models (b20, c22). https://arxiv.org/abs/2501.07301
27. [M] Chen et al. (2025) From Mathematical Reasoning to Code: Generalization of Process Reward Models (b21, c24). https://arxiv.org/abs/2506.00027
28. [V] Wang et al. (2025) Rethinking Inference-Time Scaling (b22, c21). https://arxiv.org/abs/2504.14047
29. [V] Qian et al. (2026) PAC-CF (b23, c25). https://arxiv.org/abs/2604.14345
30. [V] Yao et al. (2023) Tree of Thoughts (c09). https://arxiv.org/abs/2305.10601
31. [V] Qin et al. (2025) To Backtrack or Not to Backtrack (c16). https://arxiv.org/abs/2504.07052
32. [V] Setlur et al. (2025) Scaling Test-Time Compute Without Verification or RL is Suboptimal (c23). https://arxiv.org/abs/2502.12118
33. [V] Kambhampati et al. (2024) LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks (c26, position paper). https://arxiv.org/abs/2402.01817
34. [V] Kaufmann and Koolen (2017) MCTS by Best Arm Identification (c28, theory). https://arxiv.org/abs/1706.02986
35. [V] Zhang et al. (2024) ReST-MCTS* (c29). https://arxiv.org/abs/2406.03816
36. [M] Xie et al. (2024) MCTS Boosts Reasoning via Iterative Preference Learning (c30). https://arxiv.org/abs/2405.00451
37. [V] Zheng et al. (2025) ProcessBench (d01). https://arxiv.org/abs/2412.06559
38. [V] Zhao et al. (2025) Sample, Scrutinize and Scale (d02). https://arxiv.org/abs/2502.01839
39. [V] Stechly, Valmeekam, Kambhampati (2024) On the Self-Verification Limitations of LLMs (d03). https://arxiv.org/abs/2402.08115
40. [V] Gao, Schulman, Hilton (2022) Scaling Laws for Reward Model Overoptimization (d04). https://arxiv.org/abs/2210.10760
41. [V] Tiwari et al. (2026) Reward Under Attack (d05). https://arxiv.org/abs/2603.06621
42. [V] Zhao et al. (2025) One Token to Fool LLM-as-a-Judge (d06). https://arxiv.org/abs/2507.08794
43. [V] Brown et al. (2024) Large Language Monkeys (d07). https://arxiv.org/abs/2407.21787
44. [V] Guan et al. (2025) rStar-Math (d08). https://arxiv.org/abs/2501.04519
45. [V] Ugadiarov et al. (2026) Revisiting Tree Search for LLMs: Gumbel and Sequential Halving (d09). https://arxiv.org/abs/2603.21162
46. [V] Gao et al. (2024) Interpretable Contrastive MCTS Reasoning (d10). https://arxiv.org/abs/2410.01707
47. [V] Choraria et al. (2026) Know Thy Reasoner (d11). https://arxiv.org/abs/2604.10827
48. [V] Liao et al. (2025) Lost at the Beginning of Reasoning (d12). https://arxiv.org/abs/2506.22058
49. [M] Jiang et al. (2026) FoE: Forest of Errors (d13; intro and Table 1 only). https://arxiv.org/abs/2604.02967
50. [M] Joo and Klabjan (2026) Mitigating Over-Optimization in PRM-Guided Search (d14; abstract and intro only). https://arxiv.org/abs/2608.30051
51. [V] Shojaee et al. (2025) The Illusion of Thinking (d15). https://arxiv.org/abs/2506.06941
