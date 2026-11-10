# Language Agent Tree Search: deep document

*Subfield C05.06. Scope: Monte Carlo tree search (MCTS) run by a language model, with an LM value function, written reflection and real environment feedback. Key work: LATS (Zhou et al., arXiv 2310.04406). Evidence files: evidence_a-d.jsonl (ids a01 to d19), claims.jsonl (K01 to K28), critique.md. Sibling subfields (Tree of Thoughts, Search over thoughts, Language-guided exploration, Neural and LLM proof search) are covered elsewhere; only links are noted here.*

Reading guide: "n" is children sampled per node, "k" is trajectories (rollouts) per question, "SR" is success rate, "EM" is exact match, "SC" is self-consistency. All LATS numbers are the authors' own unless marked.

## 1. What it is

LATS turns Monte Carlo tree search into a loop for one language model. The model does three jobs: it proposes actions (the policy), it scores states (the value function) and it writes lessons after a failure (the reflector). There is no trained world model and no trained value net. The environment supplies real observations and, sometimes, a real success signal.

One LATS iteration has six steps (a01):
1. **Selection.** Walk from the root to a leaf by the UCT rule (exploration weight w = 1 by default).
2. **Expansion.** Sample n actions (default n = 5) at the leaf. Each becomes a child node.
3. **Evaluation.** Score each child. The score mixes an LM rating with a self-consistency count: V(s) = lambda * LM(s) + (1 - lambda) * SC(s). SC counts how often the same action was sampled again at the same state. lambda = 0.5 for HotPotQA and Game of 24, 0.8 for code and WebShop (a02).
4. **Simulation.** Run the best child forward to a terminal state, acting in the real environment. In code, each action is a whole program, so simulation is skipped (a06).
5. **Backpropagation.** Push the terminal reward up the path and update visit counts and values.
6. **Reflection.** On failure, the LM writes a short lesson from the trajectory. Lessons are kept in context for later iterations.

Why it matters for our agent. S6 (impasse) in our schema is a small tree of operator children tested by code. LATS is the main published design for such a tree with real feedback. The question for us is not "is LATS good" but which of its parts survive when (a) there is no training, (b) a code check can stand in for the LM value, (c) cost is counted in tokens and (d) the model may already think natively for a long time.

Short verdict from the evidence set: tree search over agent actions helps when the signal is external (tests, execution, environment), the judge is accurate or sampled several times, and states can be reverted. The headline LATS numbers are weakly supported (small samples, oracle feedback, one failed independent re-run). Simple retry or resampling with the same real check often matches it at a small fraction of the cost.

## 2. History and theories in depth

**Lineage.**
- *MCTS and AlphaZero.* Selection by UCT, expansion, rollout and backup come from classical MCTS. AlphaZero added learned policy and value nets. LATS keeps the shape and replaces the nets with prompts.
- *Tree of Thoughts (ToT), Yao et al. 2023 (a25).* BFS or DFS over LM-proposed thoughts, scored by a prompted value. Game of 24 with GPT-4: CoT 4%, ToT (b = 5) 74%. ToT used about 5.5k completion tokens per case, close to 100 CoT trials (6.7k). Best of 100 CoT reached 49%. So ToT's gain was already partly a sampling-budget effect. See the Tree of Thoughts subfield.
- *RAP, Hao et al. 2023 (a20, b06, b22, c15).* MCTS where the LM is policy and simulated world model. No environment. Blocksworld, LLaMA-33B: success at 2/4/6 steps 1.00/0.86/0.26 for RAP(10) and 1.00/0.88/0.42 for RAP(20), against CoT 0.17/0.02/0.00. GPT-4 CoT scored 0.50/0.63/0.40, so at 6 steps GPT-4 CoT beat RAP(10). LATS's design claim is that real environment steps beat a simulated world model.
- *Reflexion, Shinn et al. 2023 (a16, a17, c14).* After a failed trial, write a lesson, keep it, retry. ALFWorld (134 tasks): ReAct+Reflexion solved 130 of 134 in 12 trials, ReAct alone stalled between trials 6 and 7. HumanEval GPT-4 pass@1 91% vs 80% baseline. MBPP Python got worse (77.1 vs 80.1) because model-written tests had a 16.3% false-positive rate (1.4% on HumanEval Python). LATS reuses this reflection step.
- *Self-correction critique, Huang et al. 2024 (a18, a19).* Gains reported for Reflexion-style loops used oracle correctness labels. Without the oracle, self-correction lowers accuracy. This is the main challenge to LATS's reflection part and to its HotPotQA setup.

**LATS (Zhou et al., 2023, ICLR 2024).** Claims a unified method: reasoning (CoT), acting (ReAct), planning (tree search) in one loop. Test beds: HotPotQA, HumanEval, MBPP, WebShop, Game of 24. Main claim: best at the same trajectory budget. The authors state the limits themselves: it costs more than ReAct or Reflexion, and it needs the environment to revert to earlier states (a11, d07).

**Descendants and rivals (2024 to 2026).**
- *Koh et al. (TMLR 2025).* Best-first tree search in live web environments (VisualWebArena, WebArena) with a multimodal GPT-4o value that averages several reasoning samples (a12 to a15, d04 to d06).
- *SWE-Search (Antoniades et al., ICLR 2025).* MCTS for SWE-bench Lite with a hybrid value (number plus written critique) and a debate discriminator (a27, b14, b15).
- *Agent Q (Putta et al. 2024).* MCTS with a self-critique value, plus DPO training on the trees (a26, b16, b26). Training puts it out of scope for us, but the test-time part is a data point.
- *MCTSr (Zhang et al. 2024), ReST-MCTS\*, AlphaZero-like TS-LLM (Feng et al.), R-MCTS (Yu et al.), DARS.* Math, trained-value and web variants (c16, c17, a21, d19, d16).
- *Compute-matched critics.* Wu et al. (a23), Snell et al. (b10), Chen et al. (c10), Olausson et al. (b12), Stechly et al. (a24), Kapoor et al. (d01) all ask the same question: does the search beat spending the same budget on plain sampling plus a good selector?

**Competing explanations of why LATS works.**
1. *Real search over a branching space with backing out of mistakes* (the authors' account; Koh's case studies of compounding error, c24).
2. *More samples plus a selector.* A tree is a way to spend extra calls. Best-of-N with the same selector may do as well (Wu, Snell, Kapoor, Brown c20).
3. *The oracle.* On HotPotQA the environment tells the agent if its submitted answer was right (a05). Part of the gain may come from that signal, not the tree (Huang, Karthikeyan d08).
4. *Static guidance.* The value of written reflections may be the fixed hint, not its content (d15).

The evidence does not separate these four cleanly. See section 5.

## 3. Core findings with exact numbers

Status key: **established** = two or more independent sources agree; **single-source**; **contested** = sources disagree. Claim ids are K01 to K28 from claims.jsonl.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| LATS beats ReAct, Reflexion, ToT, RAP on authors' tests (GPT-3.5, HotPotQA, acting) | EM: ReAct 0.32, ReAct best-of-k 0.38, Reflexion 0.51, ToT 0.39, RAP 0.54, LATS 0.63, LATS n=3 0.58, n=10 0.65, CoT+ReAct start 0.71. 100 questions, k=50 | Zhou 2023 (a04, b01, c01) | contested (K01) |
| HotPotQA reasoning only | CoT 0.34, CoT-SC 0.38, ToT 0.55, RAP 0.60, LATS(CoT) 0.62 | a03 | single-source |
| HotPotQA uses an oracle: the environment says if the submitted answer was right; no ablation removes it | Tables 2, 3, 8 | a05, d07 | established that the oracle is used (K02) |
| HumanEval pass@1, GPT-3.5 | CoT 46.9, ReAct 56.9, Reflexion 68.1, ToT 54.4, RAP 63.1, LATS 83.8 | a06, c02 | contested (K01) |
| HumanEval pass@1, GPT-4 | base 80.1, Reflexion 91.0, LATS 92.7. Gain over Reflexion +1.7 (vs +15.7 at GPT-3.5) | a06, c02 | single-source (K03) |
| WebShop, 50 tasks, GPT-3.5 | Score/SR: ReAct 53.8/28.0, best-of-k 59.1/32.0, Reflexion 64.2/35.0, LATS 75.9/38.0; fine-tuned 67.5/45.0; human 82.1/59.6. Score gain large, SR gain +3 over Reflexion | a07, c03 | single-source |
| Game of 24, GPT-3.5, n=5, k=30 | CoT 0.08, Reflexion 0.12, ToT 0.20, RAP 0.40, LATS 0.44; lambda=1 (no SC) 0.40. The ToT paper with GPT-4 reports 74%, so the LATS ToT baseline is weak | a08, b18, a25 | single-source |
| Ablation, HotPotQA | Full 0.63; no LM heuristic 0.37; DFS instead of MCTS 0.42; no reflection 0.58. Reflexion alone gains 0.19 over ReAct; reflection adds only 0.05 inside LATS | a09, b02, c04 | contested for reflection (K11), established for value (K05) |
| Equal trajectories | ReAct best-of-250 0.42; CoT-SC k=250 0.40; LATS n=1 k=50 0.48; ToT 0.49; RAP 0.54; LATS n=5 0.63 | a10, b03 | contested (K04): matched in trajectories, not tokens |
| Cost per success (HotPotQA) | Tokens on success: RAP 210,215; LATS 176,500 and 173,290 (two rows). Nodes at k=10/30/50: ToT 33.97/47.54/84.05, RAP 31.53/37.71/70.60, LATS 28.42/34.12/66.65. Token counts cover successes only | a10, b03, c05, critique | single-source |
| Independent LATS re-run, HumanEval, 164 problems, 5 runs | LATS GPT-4 88.0 (82.3 to 91.5) at $134.50 vs published 92.7; LATS GPT-3.5 80.4 (78.7 to 83.5) at $9.49 vs published 83.8. The original dropped 3 problems with no example tests plus a 4th (execution error), and used a subset of tests | Kapoor 2024 (d01, d02) | failed replication (K01) |
| Retry baselines on the same set | Warming GPT-4 93.2 ($2.45); retry 92.0 ($2.51); Reflexion 87.8 ($3.90); LATS 88.0 ($134.50). LATS costs about 55x warming | d01, d03 | single-source (K19) |
| Web search gain (Koh) | VWA GPT-4o+SoM 18.9 to 26.4 (+39.7% rel.); WebArena GPT-4o 15.0 to 19.2 (+28.0%); Llama-3-70B VWA 7.6 to 16.7, WA 7.6 to 10.1. Absolute results under 27% | a12, b04, c06 | single-source (K06) |
| Budget helps, with diminishing returns (VWA 200-task subset) | no search 24.5; c=5 32.0; c=20 37.0. Depth/branch: d1b3 26.0, d1b5 32.0, d2b3 31.5, d2b5 35.0, d3b5 35.5, d5b5 37.0 (critique-corrected) | a13, c07 | single-source (K07) |
| Search vs re-ranking whole trajectories at about equal compute | re-ranking plateaus near 30% at n=7; search c=5 beats it; c=20 gives 37.0 | a13, d04, c09 | single-source |
| Value function is the bottleneck | Koh: none 24.5; LLaVA-34B value 30.0; GPT-4o no SC 28.5; SC n=5 32.5; SC n=20 37.0; ground-truth reward 43.5. LATS: removing LM heuristic 0.63 to 0.37 | a09, a14, b05, c08, d05 | established (K05) |
| Gain is largest on medium difficulty (VWA, by action difficulty) | easy 34.2 to 42.3 (+24%); medium 12.7 to 22.2 (+75%); hard 10.2 to 14.9 (+47%) | a15, c09 | single-source |
| Search needs a judge near 90% accurate | Chen: no significant gain over re-ranking below about 90% judge accuracy; Spider greedy 62.3 vs best naive re-ranking 61.5; GSM8K GPT-3.5 re-rank 47.6, iterative 48.4, tree 51.0 (McNemar p>0.05); with an oracle judge tree 73.0 vs 64.1 | Chen 2024 (c10, c11, c12) | established (K12) |
| Environment observations raise judge accuracy | CodeLlama-13B: Spider 58.2 to 83.6, Bird 49.4 to 79.6, GSM8K 62.2 to 70.6. GPT-3.5 Spider 67.0 to 90.0, Bird 64.3 to 89.2 | c12 | single-source |
| Self-judge top pick is no better than random without ground truth | GSM8K accuracy (Llama3-70B / Mistral-7B / Haiku3 / Sonnet3): no search .813/.426/.866/.757; ground truth .958/.820/.964/.923; random node .751/.450/.864/.680; majority vote .883/.608/.905/.786; self-reward pick .776/.469/.854/.685 | Karthikeyan 2025 (d08) | single-source (K20) |
| Self-feedback MCTS can hurt (ToolTalk F1) | Sonnet3 .706 to .559; Haiku3 .638 to .605 | d09 | single-source (K21) |
| Self-correction without an oracle hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GSM8K 75.9 to 75.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49.0 to 43.0 (round 2). With oracle: GPT-4 HotpotQA 49 to 59 | Huang 2024 (a18, a19, c13) | established (K08) |
| LLM critic vs sound verifier | Game of 24: standard 5%, LLM critic 3%, sound verifier 36% to 38%, resampling k=25 42%. Verifier accuracy 87.0%, FPR 10.4%, FNR 20.7%. Blocksworld self-critique 40 to 55 is an exception | Stechly 2024 (a24, b13, b29) | established (K09) |
| Self-repair vs fresh samples | Repair/i.i.d. ratio mostly 0.83 to 1.09; human feedback 52.6% vs GPT-4's own feedback 33.3% | Olausson 2024 (b12, b25) | single-source (K10) |
| MCTS costs far more than sampling on math | Wu: MCTS underperforms sampling at every budget, often dozens of times more tokens; Llemma-7B with REBASE beats Llemma-34B. SWE-Search GPT-4o cost $40.86 to $576.00 (about 14x) for +5.3 points | a23, b09, c18, b14 | established (K13) |
| Beam search over a PRM helps medium, hurts easy | Snell: compute-optimal allocation needs up to 4x less compute (16 vs 64 generations); very little benefit on the hardest | b10, b21, c19, d10 | established (K14) |
| SWE-Search gains | Resolve rate GPT-4o 25.7 to 31.0; mini 13.0 to 17.0; Qwen-72B 18.0 to 24.7; DeepSeek-V2.5 16.3 to 21.0; Llama-70B 13.6 to 17.7; mean +23% relative. Value function picks the correct patch 73% of the time, discriminator 84% | a27, b14, b15, c21 | single-source (K17) |
| Many samples with exact verifier | SWE-bench Lite DeepSeek-Coder-V2: 15.9% at 1 sample to 56% at 250 | Brown 2024 (c20) | single-source (K18) |
| Trained value >> prompted value | Game24 LLaMA-SFT policy: prompted LLaMA value 9.2, GPT-3.5 value 21.0, trained 64.8. Agent Q OpenTable 81.7 to 95.4 with search; WebShop base 28.6, RFT 31.3, DPO 37.5, base+MCTS 48.4, Agent Q+MCTS 50.5, human 50.0 | a21, b07, a26 | established (K15), not usable without training |
| Branch gate (prompted) | BN-DP cuts tokens, calls and time 75% to 85% on math in 14 settings with little accuracy change; BN-SC unstable in 1 to 4 settings | Chain-in-Tree (d11) | single-source (K23) |
| Reasoning-era model (Qwen3-30B-A3B-2507) | MATH500 79.25 to 80.60 to 82.09; AIME25 48.67 to 50.00 to 53.33; GPQA-D 47.55 to 64.65 (MCTS-RAG) to 65.08; ReST-MCTS AIME25 20.00 (collapse). Table cells inferred by position | PRISM-MCTS (d17) | single-source (K24) |
| Best-of-N over agents saturates | 60% to 94% of the 100-agent gain is reached by 20 agents with an exact verifier | d14 | single-source (K25) |
| Written feedback may be static guidance | Qwen2.5-Coder-7B, 252 failures: feedback 85.3%, fixed template 86.1%, resample 68.3% (+17.1 pp, CI +9.9 to +24.2) | d15 | single-source (K26) |
| Program-owned tree with small model | ReAcTree 8B about ReAct 70B; +25 pp goal success rate at 70B; at 7B a complex hierarchical prompt hurt | d18 | single-source (K27) |
| RAP degrades with horizon | LLaMA-33B 1.00/0.86/0.26 at 2/4/6 steps; GPT-4 CoT beats RAP(10) at 6 steps (0.40 vs 0.26) | a20, b22 | single-source (K16) |

Corrections recorded by the cross-check (critique.md): the 210,215 token figure belongs to RAP, not ToT; Koh's d=2,b=5 cell is 35.0, not 32.0; Agent Q WebShop baselines are base 28.6, RFT 31.3, DPO 37.5; LATS k=50 accuracy appears as 0.61 in Tables 9/10 and 0.63 in Table 3 (different runs, not a conflict).

## 4. Mechanisms and models

This section is written so an engineer can build each piece. The program owns control; the model fills slots (SCHEMA section 1).

### 4.1 The LATS loop as code

```
root = Node(state0)
for it in range(budget):
    leaf = select(root)               # UCT down the tree
    if leaf.terminal: backprop(leaf, reward); continue
    kids = [leaf.child(sample_action(leaf.state)) for _ in range(n)]
    for c in kids:
        c.value = lam*lm_score(c) + (1-lam)*sc_score(c)   # SC: share of sibling samples equal to this action
    best = argmax(kids, key=value)
    r = rollout_or_check(best)        # real env steps, or run tests
    backprop(best, r)
    if r is failure: leaf.reflection = lm_write_lesson(trajectory(best))
final = pick(candidates)              # highest reward; see 4.5
```
UCT: score(child) = value(child) + w * sqrt(ln(N_parent) / N_child), w = 1 (a01). The critique could not verify the paper's exploration-weight ablation (one extraction says w=0.5 gave 0.55 and w=2.0 gave 0.63; the table was garbled). Treat w as untuned.

### 4.2 Value function
- LM score: ask the model to rate the state or action (for example 1 to 10, or good/bad with a reason).
- SC score: sample the same decision several times; the share agreeing is the SC score. In Game of 24, lambda=1 (no SC) gave 0.40 vs 0.44 at lambda=0.5 (b18).
- Koh's version: average several multimodal reasoning samples (n=5 or n=20). Ladder 28.5 (single) to 32.5 (n=5) to 37.0 (n=20), ground truth 43.5 (d05). No cost-matched control against extra branches exists (K28).
- Code: value = pass share of model-written tests, mixed with the LM score (lambda 0.8). The final answer is scored on the real hidden tests (b19). Reflexion's false-positive warning applies: 16.3% on MBPP (a17).
- SWE-Search: number plus written critique; picks the right patch 73% of the time (b15).
- Break-even: about 90% judge accuracy (Chen). Giving the judge environment output (execution result) is what raised judge accuracy from about 58-67% to 80-90% (c12).

### 4.3 Reflection
The failed trajectory goes to the LM with a prompt to write a short lesson. The lesson is appended to the context for later expansions. Evidence that it works inside a tree is weak: 0.05 on HotPotQA (a09), and on WebShop the reflections were "often generic" (a07). With real tests Reflexion helps on Rust HumanEval (0.60 to 0.68 with tests, b02/a17) but hurts on MBPP Python through false positives. Newer work suggests the hint may act as fixed guidance (d15).

### 4.4 Real feedback versus simulated world model
LATS takes environment steps and observations. RAP asks the LM to imagine next states. Real feedback avoids drift; RAP success falls with horizon (a20). The cost is reversion: the environment must allow going back. Koh implemented back-tracking by reset-and-replay of the action list, because the Back button loses page state (d06). Destructive actions (placing an order) must be excluded or gated by a classifier (d06). LATS names HumanEval, WebShop, ALFWorld and ToolBench as reversible (d07).

### 4.5 Readout: which node to return
Options: top self-score, highest real reward, majority vote across nodes, discriminator debate (SWE-Search, 84% correct pick vs 73% for value). Without ground truth, top self-score was at or below random on 3 of 4 models; majority vote was the reliable readout (d08).

### 4.6 Budget controls
- Matched trajectories (LATS) are not matched tokens. Token cost of a tree grows with k, n and rollout length. SWE-Search is about 14x cost (b14, d16); R-MCTS 6x to 10x ReAct tokens (d19, column alignment uncertain).
- Gate branching: a prompted yes/no "is branching needed here" check cut cost 75% to 85% on math (d11). A trained predictor does the same with 1.5x to 2x CoT cost vs about 10x for ToT (d12).
- Gate by difficulty: Snell's per-question difficulty estimate cost 2048 samples per question and was not charged (d10).

### 4.7 Our small tree compared with what was tested
SCHEMA section 4 tree rules: 3 children, depth 2, 2 expansions. Koh's grid (VWA subset, no search 24.5, best 37.0): d1b3 26.0, d2b3 31.5, d2b5 35.0, d5b5 37.0 (c07). Our shape sits near d2b3. By simple arithmetic on those cells, d2b3 captures about 56% of the full gain (7.0 of 12.5 points). This is a derived estimate on one subset, not a finding of the paper.

## 5. What holds up

**Holds up (two or more sources).**
- The value or judge signal is what limits search (K05, K12). Ground truth beats the best LM value by 6.5 points (43.5 vs 37.0), and removing the LM value costs 0.26 on HotPotQA.
- Without an external signal, self-correction and self-judged search do not help and can hurt (K08, K09; K20 supports): Huang, Stechly, Karthikeyan, Chen agree.
- Cost accounting matters (K13): MCTS needs dozens of times more tokens than sampling on math; SWE-Search about 14x for +5.3 points.
- Gate search by difficulty (K14): beam search helps medium, hurts easy at high budget, little on hardest.
- LATS numbers are weakly supported (K02): small sets, one run, no intervals, oracle on HotPotQA, altered HumanEval set.

**Failed or partial replication.** Kapoor et al. re-ran the public LATS code on HumanEval (5 runs). GPT-4 got 88.0 (min-max 82.3 to 91.5) vs 92.7 published; GPT-3.5 got 80.4 vs 83.8. A warming retry baseline got 93.2 at $2.45 vs $134.50 for LATS. The original dropped problems and used partial tests (d01, d02). No independent HotPotQA or WebShop re-run was found in four targeted searches (gap 9). Descendants (Koh, SWE-Search, Agent Q) show the idea works in other settings, but none re-tests LATS itself.

**Moderators found.**
- Model strength: gain over Reflexion +15.7 (GPT-3.5) vs +1.7 (GPT-4) on HumanEval (K03, single source).
- Task difficulty: medium items gain most (Koh +75% relative); easy items can lose (Snell).
- Signal type: real tests and execution observations raise judge accuracy (c12); prompt-only self-judging does not (d08).
- Horizon: RAP's simulated world model decays at 6 steps (a20); depth in real environments helps on web (c07).
- Task type: ToolTalk with open-ended steps lost with self-feedback (d09).
- Model era: on a 2025 reasoning model, MCTS gives small math gains and a mismatched tree collapsed (d17); the DeepSeek-R1 report says MCTS self-improvement failed and native long reasoning allocates compute by difficulty (d13).

**What worked.**
- Search with a real or accurate signal on web tasks (+28% to +40% relative, small absolute) and code agents (+17% to +27% relative on SWE-bench Lite).
- Self-consistency on the value call (28.5 to 37.0).
- Tree search over whole-trajectory re-ranking at about equal compute on web (37.0 vs about 30), where steps cannot be re-tried cheaply.
- A program-owned tree letting an 8B model approach a flat 70B agent (ReAcTree, d18).
- A cheap branch gate (d11).

**What did not work.**
- Self-critique as a verifier (Game of 24 3%, GPT-3.5 CSQA 75.8 to 38.1).
- Self-reward top pick on GSM8K (at or below random).
- MCTS at equal tokens on math (Wu), lookahead search (Snell).
- Reflection inside a tree: small (+0.05), may be a static hint.
- Simple retries beat LATS on HumanEval at 1/55 the cost (Kapoor).
- Complex hierarchical prompts at 7B (d18).

**Competing explanations still open.** Whether the tree-over-retry gain is real when the check is real and cost is matched in tokens (gap 1). Only Koh gives a matched-call web result and only Kapoor gives a matched-dollar code result, and they point opposite ways.

## 6. Language models

How models behave in this setting, by role.
- *As action sampler.* GPT-3.5 and GPT-4 sample diverse enough actions that a tree beats one path on tasks where an early wrong step ruins the run. Greedy web agents fail by compounding early error (Koh, c24).
- *As value function.* Weak when prompted. Koh: single GPT-4o call 28.5, 20-sample average 37.0, LLaVA-34B 30.0. TS-LLM: prompted LLaMA value 9.2 vs trained 64.8 on Game24 (b07). Karthikeyan: self-reward top pick .776/.469/.854/.685 vs random .751/.450/.864/.680 across Llama3-70B, Mistral-7B, Haiku3, Sonnet3. Judge accuracy: GPT-4-Turbo 76.5 (Spider), 76.2 (Bird), 93.8 (GSM8K); GPT-3.5 67.0 on Spider (c10). Judgment is good on checkable arithmetic (GSM8K) and poor on code and open steps.
- *As reflector.* Writes plausible lessons that are often generic. The gain is real with a real signal, near zero or negative without it (Huang; Reflexion MBPP).
- *Stronger models.* The tree's edge over a strong baseline shrinks (+1.7 at GPT-4). Frontier-model best-of-N curves can be flat, leaving little variance to harvest (d14).
- *Reasoning-era models.* Only indirect data. PRISM-MCTS on Qwen3-30B-A3B-2507 adds 1 to 5 points on math and about 17 on retrieval-heavy GPQA, and one baseline MCTS loses about 28 points on AIME25 (48.67 to 20.00) (d17). The R1 report says its own MCTS attempt was dropped (d13). No clean tree-vs-no-tree run on o-series, Claude or Gemini thinking exists (gap 4).
- *Small models.* A program-owned tree helps 7B to 8B models (ReAcTree 8B near flat 70B), but prompt complexity hurts at 7B (d18). SWE-Search gains hold across five models from 4o-mini to Llama-70B, mean +23%.
- *Cost.* GPT-4o SWE-Search $40.86 to $576.00; mini 9.90 to 42.50; Qwen 8.50 to 18.37 (critique). LATS GPT-4 HumanEval $134.50 vs warming $2.45.

## 7. What our agent should take

Format per item: schema part, status, evidence ids.

### Add now (established)

1. **Children in the S6 tree are tested by a code check, not scored by the model.** Schema part S6 and S4, operators (O) ranked in code. Status [E]. K05, K09, K12; c10, c12, c08, a24, d08. Our S6 already ranks children by test result in code. This confirms it. Where no check exists, do not rely on a prompted value to pick.
2. **Turn S6 tree search off when there is no accurate judge.** Schema part S6 gate (links G12). [E]. K12, K09; c10, c11, d08, d09. Search is not worth it below roughly 90% judge accuracy, and with a self-judge it can lower results (ToolTalk). In no-check mode keep the plain path.
3. **Revise only from real output.** G2, S5. [E]. K08, K09; a18, a19, a24. Already G2. The evidence strengthens it: oracle gains vanish without the oracle.
4. **Report accuracy at equal total tokens, failures included.** G7, section 6 logging. [E]. K13, K02; a23, b14, d01. Trajectory-matched comparisons hid cost gaps of 14x to 55x.
5. **Spend search by difficulty.** G12, S0 gate. [E]. K14; b10, a15, c19. Medium items gain; easy items can lose at high budget; the hardest gain little. Do not tree easy items.
6. **Keep a no-search arm and a best-of-N arm with the same verifier in every evaluation of S6.** G7. [E] as method (K02, K13). Evidence: d01, c20, a23.

### Test first

1. **Tree over reflect-retry at equal tokens (S6).** [C] K01, K04, K19. Tree 37.0 vs re-rank about 30 on web (d04); retries 93.2 vs LATS 88.0 on code (d01).
2. **Value self-consistency versus extra branches at equal calls (S6 value).** [S] K28; d05. Ladder 28.5 / 32.5 / 37.0, no matched control.
3. **Agreement across branches as the readout when no check exists (S7).** [S] K20; d08. Majority vote .883 vs self-pick .776 on Llama3-70B.
4. **Written reflection inside the tree, with a fixed-hint arm and a plain-resample arm (memory, S5).** [C] K11, K26; a09, d15.
5. **Reversibility tag on each operator (S6).** [S] K22; d06, d07. Never expand an irreversible child.
6. **Cheap prompted gate on whether to branch at a node (S6 gate).** [S] K23; d11.
7. **Thinking-model baseline: one native extended-thinking attempt vs the tree at equal tokens (S0, S6).** [S] K24; d17, d13. SCHEMA section 7 already lists this as the first test.
8. **Small program-owned tree with flat short node prompts on a small and a large model (S6 design).** [S] K27; d18.
9. **Difficulty gating with a prompted estimate (S0).** [S] K23; d10, d12.
10. **Depth and breadth: is our 3 children x depth 2 x 2 expansions tree near the knee?** [S] K07; c07.

Excluded: trained value models, DPO on trees, process reward models (K15). They need training, which the project rules out; keep as an upper bound only.

## 8. Concrete tests on our bench

Bench item types available: ARC-style grid items (checkable on held-out example pairs, G3) and BrainTeaser-style items (no code check, multiple choice or short answer). Arms are matched on total tokens including failed branches and setup. Use at least 300 items per arm when possible, 3 seeds, and report confidence intervals.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| T1 | Tree vs retry vs best-of-N | ARC items with held-out check, mixed difficulty | (a) one plain pass; (b) best-of-N with check; (c) reflect-retry loop; (d) our S6 tree (3 children, depth 2) | Accuracy at fixed token cap; accuracy per 1k tokens; gain by difficulty tercile | Tree no better than (b) on easy; +3 to +8 points on medium if Koh transfers; if Kapoor transfers, (b) or (c) ties (d) |
| T2 | Value source in the tree | ARC items | tree with code-check value; tree with LM value (1 call); tree with LM value (n=5 samples); same tokens | Accuracy; judge accuracy vs truth | Code check > LM n=5 > LM 1 call, spread about 6 to 15 points (Koh 24.5 to 43.5) |
| T3 | Value samples vs branches | ARC items, no check at node level | A: n=5 value samples, 3 branches; B: 1 value sample, 8 branches; C: 3 branches, n=1 | Accuracy at same LM calls | Unknown. If A beats B by 2+ points, keep value SC |
| T4 | Readout without a check | BrainTeaser items | top self-score; majority across nodes; plain single pass | Accuracy | Majority vote > self-pick; self-pick near random (d08) |
| T5 | Tree on/off switch | BrainTeaser plus ARC | always-tree vs gated (tree only if calibration judge accuracy >= 0.9 or a check exists) vs plain | Accuracy; tokens | Gated >= plain; always-tree may lose on no-check items (ToolTalk pattern, K21) |
| T6 | Reflection ablation | ARC items that fail on first pass | tree + reflection; tree, no reflection; tree + fixed generic hint; tree + plain resample | Fix rate on first-pass failures | If fixed hint is about equal to reflection (d15), drop per-failure reflections; expected differences 0 to 5 points |
| T7 | Branch gate | ARC and BrainTeaser | prompted yes/no gate at each node vs always branch | Tokens saved; accuracy change | 50% to 80% fewer tokens, under 1 point change (d11 on math) |
| T8 | Thinking-mode baseline | both | one native extended-thinking pass; tree with short passes; best-of-N short | Accuracy at token cap | Per G11, N short may match or beat; tree adds only on medium items |
| T9 | Model-size check | ARC items | T1 arms on a small and a large model | Tree gain at each size | Gain larger on the small model (K03, d18) |
| T10 | Tree shape | ARC items | d1b3, d2b3, d2b5, d3b3 | Accuracy vs tokens | Knee near d2b3 (derived estimate 56% of full gain) |

Log for each run: mode, tokens per node, which node was returned vs the best node available, judge verdict vs truth, and whether a reflection flipped wrong to right or right to wrong (SCHEMA section 6).

## 9. What does not transfer, and why

- **Trained value models, DPO on trees, process reward models.** TS-LLM (64.8 vs 9.2), Agent Q (95.4% OpenTable), Snell's PRM. We do not train. Treat as upper bounds.
- **HotPotQA oracle numbers.** The 0.63 is oracle-assisted. We have no oracle at answer time in no-check mode; do not expect it.
- **Live web environments.** WebArena gains (19.2%) rest on reset-and-replay in a browser and a multimodal value. Our items are text or grids, where revert is free.
- **RAP-style simulated world models.** Decays with horizon (0.26 at 6 steps); our S6 uses code to run candidates.
- **Large rollout counts (k=50, k=250).** Our token budget forces tiny trees. Results from k=50 or c=20 may not hold at depth 2.
- **Math results with trained reward models (Wu, Snell).** They say MCTS is expensive; they do not test a prompted value, so they transfer as a cost warning only.
- **LATS "CoT then ReAct" best arm (0.71).** One run, 100 questions, oracle.
- **Game of 24 numbers with GPT-3.5.** The ToT baseline in LATS (0.20) is far below the ToT paper's GPT-4 74%. It says little about frontier models.
- **Debate discriminator (SWE-Search 84%).** Our G9 bans debate. The discriminator used multi-agent debate; the 11-point gain over value (73% to 84%) is not available to us. Use a code check or agreement instead.

## 10. Open questions

1. Does tree search beat best-of-N with the same real verifier at equal total tokens (failures included), N >= 300 items, 3 seeds? (Gap 1: only partial.)
2. How much of LATS's HotPotQA gain remains without ground-truth feedback? No ablation exists (K02).
3. Is the 90% judge threshold stable across models and tasks? Chen is one study; Karthikeyan's four-model sign flips do not settle it.
4. Does the gain survive on 2025 to 2026 reasoning models with native long thought? No clean test; indirect data say gains shrink.
5. Does self-consistency on the value beat extra branches at the same cost? No matched control (K28).
6. When do written reflections inside a tree help or hurt, by feedback type? No tree-internal ablation by feedback type.
7. What happens on tasks with irreversible actions? Only design guidance, no measured test.
8. Can difficulty gating work with a prompted per-item estimate? Only a per-step math gate and a trained predictor were measured.
9. Do independent re-implementations reproduce HotPotQA 0.63 or WebShop 75.9? None found.
10. Does a program-owned tree keep its gain when the model only fills slots? ReAcTree supports it, but it is a task hierarchy, not an operator tree.
11. Is MCTS (UCT) better than plain best-first or beam at our tiny budget? Koh used best-first; LATS compared MCTS with DFS (0.63 vs 0.42), which is not a best-first control.

## 11. Sources

[V] = opened and read (PDF or HTML text) in this research; [M] = snippet only. The critique notes that some table cells came from garbled PDF text; those are flagged in section 3.

- [V] Zhou, Yan, Shlapentokh-Rothman, Wang, Wang (2023/2024). Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models. https://arxiv.org/abs/2310.04406 (a01 to a11, b01 to b03, b17 to b19, b28, c01 to c05, d07)
- [V] Koh, McAleer, Fried, Salakhutdinov (2024; TMLR 2025). Tree Search for Language Model Agents. https://arxiv.org/abs/2407.01476 (a12 to a15, b04, b05, b20, c06 to c09, c24, d04 to d06)
- [V] Kapoor, Stroebl, Siegel, Nadgir, Narayanan (2024). AI Agents That Matter. https://arxiv.org/abs/2407.01502 (d01 to d03)
- [V] Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao (2023). Reflexion. https://arxiv.org/abs/2303.11366 (a16, a17, c14)
- [V] Huang, Chen, Mishra, Zheng, Yu, Song, Zhou (2024). Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (a18, a19, b11, b24, c13, c25)
- [V] Hao, Gu, Ma, Hong, Wang, Wang, Hu (2023). Reasoning with Language Model is Planning with World Model (RAP). https://arxiv.org/abs/2305.14992 (a20, b06, b22, c15)
- [V] Feng, Wan, Wen, McAleer, Wen, Zhang, Wang (2023/2024). AlphaZero-Like Tree-Search can Guide Large Language Model Decoding and Training. https://arxiv.org/abs/2309.17179 (a21, a22, b07, b08, b23)
- [V] Wu, Sun, Li, Welleck, Yang (2024/2025). Inference Scaling Laws. https://arxiv.org/abs/2408.00724 (a23, b09, b27, c18)
- [V] Snell, Lee, Xu, Kumar (2024). Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. https://arxiv.org/abs/2408.03314 (b10, b21, c19, d10)
- [V] Stechly, Valmeekam, Kambhampati (2024). On the Self-Verification Limitations of Large Language Models. https://arxiv.org/abs/2402.08115 (a24, b13, b29)
- [V] Yao, Yu, Zhao, Shafran, Griffiths, Cao, Narasimhan (2023). Tree of Thoughts. https://arxiv.org/abs/2305.10601 (a25)
- [V] Putta, Mills, Garg, Motwani, Finn, Garg, Rafailov (2024). Agent Q. https://arxiv.org/abs/2408.07199 (a26, b16, b26, c22)
- [V] Antoniades et al. (2024; ICLR 2025). SWE-Search. https://arxiv.org/abs/2410.20285 (a27, b14, b15, b30, c21)
- [V] Olausson et al. (2023/2024). Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896 (b12, b25)
- [V] Chen et al. (2024). When is Tree Search Useful for LLM Planning? It Depends on the Discriminator. https://arxiv.org/abs/2402.10890 (c10 to c12)
- [V] Zhang et al. (2024). MCTSr, Accessing GPT-4 level Mathematical Olympiad Solutions. https://arxiv.org/abs/2406.07394 (c16)
- [V] Zhang et al. (2024). ReST-MCTS\*. https://arxiv.org/abs/2406.03816 (c17)
- [V] Brown et al. (2024). Large Language Monkeys. https://arxiv.org/abs/2407.21787 (c20)
- [V] Karthikeyan, Yuan, Mansimov et al. (2025). A Study on Leveraging Search and Self-Feedback for Agent Reasoning. https://arxiv.org/abs/2502.12094 (d08, d09)
- [V] Li (2025/2026). Chain-in-Tree. https://arxiv.org/abs/2509.25835 (d11)
- [V] Gao et al. (2026). Domain-Specialized Tree of Thought through Plug-and-Play Predictors. https://arxiv.org/abs/2603.20267 (d12)
- [V] DeepSeek-AI (2025/2026). DeepSeek-R1. https://arxiv.org/abs/2501.12948 (d13)
- [V] Wang, Chen, Li, Chalamala, Liu (2026). Test-Time Compute Scales Better with Parallel Teams. https://arxiv.org/abs/2611.09798 (d14)
- [V] Aphale and Singh (2026). Rethinking Self-Repair in Code-as-Policy Agents. https://arxiv.org/abs/2611.06863 (d15)
- [V] Aggarwal et al. (2025). DARS: Dynamic Action Re-Sampling. https://arxiv.org/abs/2503.14269 (d16)
- [V] Xie et al. (2026). PRISM-MCTS. https://arxiv.org/abs/2604.05424 (d17)
- [V] Choi, Kim, Ong et al. (2026). ReAcTree. https://arxiv.org/abs/2511.02424 (d18)
- [V] Yu, Peng, Vajipey et al. (2025). R-MCTS: Teaching AI Agents to Explore with Reflective MCTS. https://arxiv.org/abs/2410.02052 (d19)
- [M] SEAG, ReTreVal, SGA-MCTS beyond abstract: seen only in snippets in the gap search and not used for any number here.
