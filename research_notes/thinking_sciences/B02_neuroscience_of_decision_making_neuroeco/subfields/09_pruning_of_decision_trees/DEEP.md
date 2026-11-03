# Pruning of decision trees: deep document

*Subfield B02.09. Sources: evidence_a-d.jsonl (ids a01-a25, b01-b27, c01-c26, d01-d15), claims.jsonl (K01-K26), critique.md. Schema parts refer to `research_notes/single_agent/SCHEMA.md` v0.2 (G1-G12, S0-S9, O1-O8, memory). Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

Pavlovian pruning is a human planning bias. When a person searches a tree of future moves in their head, they stop looking down a branch as soon as it hits a large loss. They do this even when the branch hides the best path. The bias is called Pavlovian because a bad outcome triggers it as a reflex. It does not come from weighing costs. (a01, K01)

Two things must be kept apart.

1. **Loss-triggered pruning** (the Huys effect). A branch is cut because of one salient bad outcome. Cheap, reflexive, biased. Human studies from 2012 to 2025 measure this.
2. **Value-based pruning** (the AI sense). A branch is cut because a scorer rates it low. Alpha-beta, ProbCut, Tree of Thoughts, beam search with a process reward model. Almost every LLM paper in this folder tests this second kind. No study found tests the first kind in an LLM (K21, d13).

Why it matters for our agent: the schema builds a tree only at S6 (O1-O8; max 3 children, depth 2, 2 expansions, all [D] placeholders). The open question is how to cut children. A rule such as "drop a line after a bad first step" copies the human reflex. The evidence says: in humans it saves effort but is a known bias; in LLMs the scorers that trigger cuts are noisy. So cuts must be reversible, logged and tied to code checks (K22).

Key terms.
- **Specific pruning (gamma_S)**: the chance of continuing to search after a large loss. Lower means more pruning.
- **General pruning (gamma_G)**: the chance of continuing after any other outcome.
- **ONLL / OLL trials**: trials where the optimal path has no large loss / has a large loss on it. The accuracy gap between them is the behavioural signature.

## 2. History and theories in depth

**Roots in AI.** Alpha-beta pruning cuts branches that cannot change the minimax value. It is exact (Knuth and Moore 1975, c23, not opened). ProbCut cuts a branch when a shallow search says it is probably outside the window, trading a small error rate for depth (Buro 1999, c24, not opened). Lesson: exact pruning is free; heuristic pruning has an error rate you must measure.

**Serotonin theory (2008).** Dayan and Huys modelled trains of thought as a Markov decision process. Serotonin stochastically ends a train when it reaches an aversive state. Continuation probability falls exponentially with negative value at rate alpha_5HT (alpha=20 in the main run; 400 states per sign block, 8 links per state, gamma 0.9, 20,000 learning trains). Strong inhibition makes aversive states visited less, so their badness is under-estimated (optimism) while average reward during learning rises. Lowering inhibition after learning (a model of tryptophan depletion) gives more negative outcomes and large negative prediction errors, since cut branches are now visited. No human data (a09-a11). Cools, Nakamura and Daw (2011) frame serotonin and dopamine as opponents, with many caveats on causality (a21).

**Founding human study (Huys et al. 2012, PLoS Comput Biol).** Six-state maze, two keys, deterministic transitions, fixed gains and losses. Subjects planned 2-8 moves ahead. Three groups differed only in the large loss: -70, -100, -140 points (large reward +140). N=46 (15, 16, 15). Findings (a01-a08, b01-b05, b25):
- A full look-ahead model predicted 77% of choices (predictive probability 0.71). So people did plan.
- A discount model beat a SARSA habit model by iBIC 314. Splitting the discount into general and specific (after-large-loss) pruning helped much more. The best model (pruning plus learned Pavlovian state attraction) predicted 91% of choices.
- Specific pruning exceeded general pruning in 14/15, 12/16 and 14/15 subjects (order -70, -100, -140).
- Pruning did not shrink when it cost money. In the -140 group an equal path avoided the loss (free). In -100 and -70 pruning lost money. Specific pruning did not differ across groups.
- Loss aversion (punishments about 1.4 times rewards) did not remove the need for pruning. Adding loss weights to the best model gave no gain.
- Depth: at depth 4-5 the optimal path through a loss was taken more often if the loss came in the first half than in the second half. No difference at depth 6+ (few trials). The authors say this follows from how the two rates interact, not from a built-in depth rule (a25).
- A second pull: a state that paid out before attracts choice. From state 6 with 2+ moves left, about 90% went to state 1 (small -20 loss, big reward behind). With one move left that was wrong, yet about 40% still went there (a07, b04).
- Depression link: specific pruning correlated with sub-clinical BDI (94% of subjects had low BDI, range 0-15), after controlling age, sex, verbal IQ, working memory and NEO traits. Exact p-values were not recoverable from the HTML read (a08, b05).

**Replication in fMRI (Lally et al. 2017, J Neurosci).** N=37 analysed (41 recruited). Loss was -70 pence. Optimal path chosen 78% (SD 18) with no large loss on it, 37% (SD 18) with one. Gap 41 points, t(36)=12.51, d=2.06. Gap by depth 3/4/5: 34, 40, 49 points (d=1.36, 1.86, 1.70). Pruned errors were faster than other errors and more common on harder trials. Model fit: iBIC lookahead 3052, discount 2549, pruning 2472, pruning plus loss 2466; variance explained 41.7, 52.5, 54.4, 55.3%. Pruning explained about 52% of suboptimal choices. Subgenual cingulate (SGC) tracked a trial-by-trial pruning inclination: peak t(36)=3.87, pSVC=0.004, stronger at higher depth (t(36)=3.47, pSVC=0.009). Insula and DLPFC responses to receiving large losses correlated with overall pruning. Depression link not replicated; state anxiety related to the gap at t(37)=2.12, p=0.042, uncorrected (a12-a15, b08-b11, b27, c02).

**Interplay with other shortcuts (Huys et al. 2015, PNAS).** New sample, N=37 (41 recruited), harder time-pressured version (9 s plans, depth 3-5, plans entered blind). Pruning survived a model that also had plan fragmenting and memoisation: 1-gamma_S < 1-gamma_G in 37/37 subjects, model capturing 78% of variance. Once fragmenting was modelled, general discounting was near zero, so generic early stopping was mostly a side effect of chunking. Fragments ended in the salient state 2 for 90% of target end states (range 0.83-0.99). A depth-3 tree costs 24 additions; fragmenting into depth 2 plus depth 1 costs 10 (a18, a19, b06, b07).

**Clinical tests.**
- Faulkner et al. 2022: unmedicated depressed adults (N=30, mean BDI 25.44) vs healthy (N=31, BDI 3.00). gamma_S 0.630 vs 0.617, t(59)=0.320, p=0.750, BF10=0.272. BDI vs gamma_S within depressed r=0.068, p=0.748. Money won p=0.73, BF10 about 0.27. Large gain weighted about 3 times the large loss (rho +140 7.25, -140 -2.60 in healthy). The Pavlovian state-attraction term did not help here (a16, a17, b12-b15).
- Methamphetamine use disorder 2025: N=40 users vs 49 controls. Aversive pruning 0.33 vs 0.15, F(1,100)=16.46, d=0.81. Points 2034 vs 3145 (d=0.77). Accuracy on no-large-loss trials equal. Correct on optimal-large-loss trials 19% vs 35%. Parameter recovery r>=0.91. A breathing-resistance anxiety induction did not raise pruning (ps>=0.058); Group x Resistance F(1,90)=5.17, p=0.025 (users pruned slightly less) (b16-b18).

**Formal accounts of why such a reflex persists.**
- Rational use of time: stop deepening when expected gain falls below time cost; time pressure (2000 ms vs 700 ms groups) shrinks depth (Sezener 2019, b20; Keramati 2011, a22). Pruning is then partly rational. Callaway 2022 (resource-rational planning) could not be opened (c26, d11).
- Safety versus efficiency (Mahajan 2025, eLife): a fixed Pavlovian avoidance bias blocks discovery of a large reward behind pain. A bias gated by outcome uncertainty keeps safety and loses little efficiency. Simulations in grid worlds (T-maze: +0.1 left, +1 right, at least -0.5 damage on the way right). Small human VR test N=28 (b19, b26).
- Value-gap pruning (prune moves below best minus a threshold, citing Huys 2012) appears in vmPFC lesion work: Four-in-a-Row, 18 patients vs 30 controls; Two-Step 49 vs 20 with no group difference. Groups were not compared on pruning threshold (b21).

**Companion bias.** Guitart-Masip 2012 go/no-go task, N=47: reward cues push action, punishment cues push inaction (action x valence F(1,45)=40.15; t(46)=4.85 and 5.08). It shows a general valence-to-inhibition link, but in motor choice, not mental search (a20).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People get the best path wrong when it runs through a big early loss | 78% vs 37% correct, t(36)=12.51, d=2.06, N=37; gap 34/40/49 pts at depth 3/4/5 | Lally 2017 (a12, b08) | [E] K01 |
| Original effect with a pruning model | Look-ahead predicts 77% of choices; best model 91%; iBIC gain over SARSA habit 314; N=46 | Huys 2012 (a05, b02) | [E] K01 |
| Pruning model beats discount model | iBIC 2549 to 2472 (gain 77.5); pruning+loss 2466; variance 52.5 to 54.4 to 55.3% | Lally 2017 (a13, b09) | [E] K01 |
| Pruning present in all subjects of a second sample | 37/37 subjects, 78% variance explained, harder 9 s task | Huys 2015 (a18, b06) | [E] K01 |
| Pruning persists when costly | specific pruning same across -70/-100/-140 groups (n=15-16 each) | Huys 2012 (a03, b01) | [S] K02 |
| Not just loss aversion | punishments about 1.4x rewards; loss term adds 5.8 iBIC in Lally; large gain about 3x large loss in Faulkner | a06, a13, a17 | [E] K03 |
| Pruning saves effort | pruned errors faster than other errors; more common on hard trials; gap grows with depth | Lally 2017 (a04, b04, b11) | [E] K04 |
| Subgoal fragmenting adds to pruning | fragments end in salient state for 90% of targets; gamma_G near zero after fragment modelling | Huys 2015 (a18, a19, b07) | [S] K05 |
| Depression link | positive in Huys 2012 (healthy, BDI 0-15); null in Lally; null in Faulkner: 0.630 vs 0.617, p=0.75, BF10=0.27 | a08, a15, a16 | [C] K06 |
| Methamphetamine use disorder prunes more | 0.33 vs 0.15, F(1,100)=16.46, d=0.81; points 2034 vs 3145 | 2025 study (b16) | [S] K07 |
| Anxiety link weak | state anxiety p=0.042 uncorrected (Lally); induction null (ps>=0.058) | a15, b17 | [C] K08 |
| Neural correlate | SGC t(36)=3.87, pSVC=0.004 (small-volume corrected, one sample) | Lally 2017 (a14, b10) | [S] K09 |
| Fixed avoidance bias distorts learning; gated bias fixes it | simulation (alpha_5HT=20; T-maze); VR test N=28 | Dayan & Huys 2008; Mahajan 2025 (a09-a11, b19) | [E] K10 (model-based) |
| LLM value-pruning tree search beats CoT | GPT-4 Game of 24: CoT 4%, best-of-100 CoT 49%, ToT b=1 45%, b=5 74% | Yao 2023 (a23, c05) | [E] K12 |
| Fair ToT gap | 74% vs 49% (best-of-100 CoT), not 74 vs 4; ToT uses about 5.5k tokens per case, close to 100 CoT trials | c05 | [E] K12 |
| LLM pruners cut correct branches | crosswords: no-prune solved 4/20 games, 3 missed by pruned run; PAC-CF top-K=4 removes reference action 64.4% on conflict frontiers; full path kept 0/24 | a24, c06, b23, d04 | [E] K13 |
| Generator matters more than judge | GPT-4 gen + GPT-4 judge 74; + GPT-3.5 judge 64; GPT-3.5 gen + GPT-4 judge 31; both 3.5 19 | Yao 2023 (c07) | [S] K14 |
| Self-evaluation is not a reliable trigger | GPT-3.5 kept its answer 74.7% on GSM8K after two rounds; gains with oracle labels, vanish without | Huang 2024 (c11) | [C] K15 |
| Dropping good lines too early | wrong answers use 225% more tokens and 418% more switches; over 70% of wrong responses hold a correct thought | Wang 2025 (c12) | [E] K16 |
| LLMs search shallow | mean max depth 1.78 plies (SD 0.71) vs humans 4-6; breadth beta=0.075 p=0.0025, depth p=0.82 | Chen 2026 (c03, d09) | [S] K26 |
| Confidence-based cuts save tokens | DeepConf online up to 84.7% fewer tokens (99.9% AIME25 is offline mode); ThinkPrune 10,355 to 3,574 tokens, accuracy slightly up | c13, c14 | [E] K17 |
| Hold-before-switch helps (mild only) | TIP alpha=3, beta=600: QwQ-32B AIME24 38.3 to 44.1; R1-Distill-32B 61.4 to 64.1; DeepSeek-R1 73.8 to 74.8; prompt-only 72.4; strong penalty with beta>300 hurt | d02, d03 | [S] K24 |
| Rule-based legality pruning is exact and valuable | no Monitor: invalid moves 31% in Tower of Hanoi, other variants 0% | Mondal 2025 (c15, c16) | [S] K18 |
| Novelty pruning needs tuning | up to 20x token cut when tuned; badly tuned gave near-zero solves and over 100% more cost | arXiv 2605.06040 (c17) | [S] K19 |
| Test result plus critic beats bare critic | CodeTree HumanEval 94.5 full; 91.5 without node-abort; 92.7 execution output only | d07 | [S] K25 |
| Score pruning vs sampling at equal compute | beam+PRM wins mid-hard items at small budgets, loses at large and on easy; REBASE 45.0% at 1.36e14 FLOPs vs 42.8% at 8.70e14 (Mistral-7B, MATH500); MCTS lost | d05, d06, d08 | [C] K23 |
| Trace text causal test | removing chosen branch changes move 32.0%; final decision 2.1%; largest unchosen branch 1.2% | Chen 2026 (c04) | [S] K20 |
| Anxiety text raises bias in LLMs | beta=0.08, p=.02 on preprompt STICSA; 6 of 12 models passed checks; GPT-4 and Claude-1 no effect | Coda-Forno 2024 (c19, d10) | [S] K21 |

## 4. Mechanisms and models

**4.1 Human pruning model (implementable).** The value of a sequence is the sum of discounted outcomes. The discount at step t depends on the previous outcomes.

```
V(seq) = sum_t ( prod_{k<t} c_k ) * r_t
c_k = gamma_S   if outcome k was a large loss     (specific pruning)
c_k = gamma_G   otherwise                          (general pruning)
```

c_k is the continuation weight of the rest of the path. With gamma_S about 0.6 (Faulkner; Lally; slightly above in Huys 2012) a large loss cuts the weight of everything after it. Choice follows a softmax over V. Rewards get sensitivity parameters (Faulkner used four, one per outcome size). Optional extras: a loss weight (adds 5.8 iBIC in Lally, little), a learned Pavlovian state attraction (needed in 2012, not in 2022), and a fragmenting layer (subgoal, greedy solve, reuse of stored sub-plans). Per-trial pruning inclination = KL divergence between the trajectory distributions of the discount model and the pruning model (Lally). Parameter recovery r>=0.91 (b18). The summary score is pi = gamma_G - gamma_S.

Why depth matters: pruning applies at every large loss on the path, so a deeper tree gives more chances to cut. The depth effect follows from the two rates, with no explicit depth rule (a25).

**4.2 Dayan-Huys model.** Each internal state s has value V(s). When the train of thought enters s with V(s)<0, it ends with probability that rises as exp(alpha * V(s)) falls (alpha=20 strong; 0 none). Learning only sees visited states, so aversive states are under-sampled and their values stay too good. Design rule: a prune that hides outcomes also hides the evidence that would correct the prune (a09, a10).

**4.3 Safety-efficiency gate (Mahajan 2025).** Make the avoidance weight depend on outcome uncertainty. High uncertainty lowers the bias so the path is explored; low uncertainty keeps it. Engineer's reading: prune only on a signal whose reliability is known, and allow re-visit when the cut rested on an uncertain signal (b19, K10).

**4.4 Rational depth rule (Sezener 2019).** Expand a node while the expected value of information from deeper search exceeds its time cost. Mean-based and variance-based pruning were compared with this rule in simulation (b20). Maps to G12: set depth by budget and difficulty.

**4.5 LLM value pruning (Tree of Thoughts).** Propose k thoughts per node, have a scorer label each (sure, maybe, impossible), keep the best b or drop "impossible" (c05). Failure: the scorer calls valid options impossible (rare crossword words) and the cut is irreversible. PAC-CF calibrates a threshold for coverage target Q=0.95 with R=4 evaluator repeats and reports path survival 97.46% (Game24) and 99.80% (Blocksworld) at B100, plus +4.38 utility points for ToolTree (b22, b23). On a biased scorer (TSP50) repeats did not help: conflict frontiers lose 57.5% (R=1) vs 64.4% (R=16) of reference actions at K=4 (d04). Resampling reduces noise, not bias.

**4.6 Reversible or safer variants seen in LLM work.**
- Abort returns to siblings (CodeTree; weak revival) (d07).
- Post-pruning after a bad tool result marks the edge non-viable (ToolTree, c18).
- Merge near-duplicate nodes instead of cutting by score: 85-90% fewer nodes, accuracy typically within 5% of the best baseline, up to 2.3x speedup (d01, abstract only).
- Novelty pruning of thought nodes (c17).
- Confidence early stop of a trace (DeepConf, c14); training to shorten (ThinkPrune, c13).

**4.7 Mirror mechanism: switching too early.** Thought-switch tokens ("alternatively") mark abandonment. TIP subtracts alpha from switch-token logits for beta tokens after a thought starts. Best: alpha=3, beta=600 (chosen on AIME 2022-23). A strong penalty with a window above 300 lowered accuracy (d02, d03).

## 5. What holds up

**Replications.**
- The behavioural effect (loss on the path lowers best-path choice; a pruning model wins) replicated in Lally 2017 (N=37), Huys 2015 (N=37, 37/37 subjects), Faulkner 2022 (healthy arm N=31; gamma_S about 0.6 in both groups) and the 2025 methamphetamine study (controls prune at 0.15, users 0.33). Effect sizes are large (d=2.06 for the accuracy gap).
- Caveat: all are the same task from one lab lineage (UCL/Zurich). No independent task paradigm has tested it (critique weak spots).

**Failures and null results.**
- Depression link: positive in Huys 2012 only. Lally 2017 and Huys 2015 did not reproduce it. Faulkner 2022 in clinical depression: null, BF10=0.27. Authors suggest mild severity and low-intensity treatment; untested (b15).
- Learned Pavlovian state attraction: needed in 2012 (90% then 40% effect), not in Faulkner 2022 (b13).
- Anxiety: state anxiety p=0.042 uncorrected; induction null (b17).
- Loss aversion as the cause: not supported (K03), though Huys notes loss aversion may itself be Pavlovian (a06).
- Cost-insensitivity: one study, one group per loss size (N=15-16) (K02). No replication found (d14; a search failure, not proof of absence).

**Moderators.** Depth raises the loss/no-loss gap (34/40/49 points). Time pressure and difficulty raise pruning (Lally; Sezener). Substance use raises it (d=0.81). Female participants pruned more in the 2025 study (F(1,84)=5.98, p=0.017). Reward size changed behaviour across loss groups (more avoidance at -140), explained by the model through reward weight (a03).

**Competing explanations.** Loss aversion (rejected by model comparison, with the caveat above). Rational depth limits (some pruning is optimal, K11). Chunking (explains general discount, not specific pruning). Working-memory limits (controlled in the 2025 study, b18).

**LLM interventions that worked.** ToT value pruning on Game of 24 (74%); RAP 64% on Blocksworld with LLaMA-33B; LATS 92.7 HumanEval; ToolTree about +10% over best prior planner; PAC-CF +4.38 utility; CodeTree 94.5 HumanEval; legality Monitor (31% invalid moves without it, 0% with); DeepConf and ThinkPrune cost savings; TIP +2.7 to +5.8 points on AIME24 (+2.7 R1-Distill-32B, +5.8 QwQ-32B).
**Did not work or conditional.** Self-evaluation without an outside signal (Huang 2024). Score-guided beam at large budgets and on easy items (Snell). MCTS vs sampling at equal FLOPs (Wu). Badly tuned novelty pruning. Strong switch penalty. Prompt-only hold (72.4 vs 73.8). Resampling a biased scorer (d04). Compute fairness: ToT's headline 74 vs 4 mixes compute; the fair gap is 74 vs 49 (K12).

## 6. Language models

**No direct test.** No study was found that shows an LLM the Huys maze and measures loss-triggered pruning (K21, d13). The search was partial: web budget exhausted and the arXiv, OpenAlex and Semantic Scholar APIs returned 429 errors. Absence is not proof.

**Nearest evidence.**
1. *Value pruning helps but is leaky.* ToT Game of 24: CoT 4.0%, best-of-100 CoT 49%, ToT b=1 45%, b=5 74%. About 60% of CoT samples were already wrong after the first step (c05), so a bad first step is informative on checkable arithmetic. But the scorer is fallible. Crosswords letter/word/game success: 78/60/20% with pruning, 65.4/41.5/5% without pruning, 54.6/20/5% without backtracking, 82.4/67.5/35% with an oracle state. Scorer quality is the ceiling (a24, c06).
2. *Cuts remove the right branch under a biased scorer.* PAC-CF TSP50: top-4 removed the reference action 64.4% on conflict frontiers; top-6 39.1% vs 24.0% on control; full path kept in 0/24 (K=4) and 1/24 (K=6) conflict instances, 4/24 and 8/24 on control (b23, d04).
3. *Self-scored cuts are unreliable without an outside signal.* Huang 2024, with oracle labels: GPT-3.5 GSM8K 75.9 to 84.3, GPT-4 GSM8K 95.5 to 97.5, GPT-4 HotpotQA 49.0 to 59.0. Without oracle, gains vanish or reverse (c11). ToT's self-scoring works on Game of 24, a checkable task. Task type may explain the difference; not tested (K15 contested).
4. *Judge versus generator.* A weak judge with a strong generator held up (64 vs 74); a weak generator collapsed (31) (c07).
5. *External signals help most.* LATS gains rely on tests and environment feedback (c10). CodeTree: test result plus critic 94.5; execution output only 92.7; no node-abort 91.5 (d07). The legality Monitor is the biggest single module of the brain-inspired planner (c16).
6. *Shallow search.* In four-in-a-row, mean max depth is 1.78 plies (14 reasoning models in d09; 27 models in c03) vs 4-6 for humans. Win rate rose with breadth, not depth. More reasoning effort gave larger trees. Causal paragraph deletion: chosen branch 32.0%, final decision 2.1%, largest unchosen branch 1.2%; adding back depth-1 paragraphs cut change to 4.1%, depth 2+ to 3.7% (c03, c04, d09). Depth-by-loss tests are missing.
7. *Switching too fast is the LLM twin of over-pruning.* Wrong answers: 225% more tokens, 418% more switches. TIP gains are small on strong models (DeepSeek-R1 +1.0). The prompt-only hold gave 72.4 vs a 73.8 baseline (c12, d02).
8. *Compute fairness, 2024-25.* Beam with PRM beats best-of-N on levels 3-4 at budgets 4-64 and degrades on levels 1-2; lookahead search underperforms (Snell, d05). REBASE +1.9 to +5.3 points MATH500 at matched samples; MCTS worse than sampling (d06). s1: sequential Wait lifts 50% to about 57% on AIME24, flat after about 6x base budget; 12 of 30 questions overflowed context at 512 sequential steps (d08). No 2025-26 frontier ToT-vs-best-of-N test found (K23 contested).
9. *Affect in prompts.* Anxiety text raised bias on a bias benchmark (beta=0.08, p=.02; only 6 of 12 models responded consistently; GPT-4 and Claude-1 no effect) (c19). Positive emotional lines raised accuracy (8.00% on Instruction Induction; 115% on BIG-Bench) (c21). Three older LLMs were loss averse in lotteries, Claude highest (c20). Plain LLMs planned poorly (about 3% success on older models; human baseline 78%) (c22). None of this tests branch cutting.
10. *Cheap cuts.* DeepConf: online mode up to 84.7% fewer tokens; offline AIME25 GPT-OSS-120B pass@1 91.8, majority 97.0, DeepConf@512 99.9. ThinkPrune: R1-Distill-1.5B 10,355 to 3,574 tokens with accuracy slightly up; QwQ-32B 8,763 to 4,494; DeepScaleR 5,914 to 3,370; each about 2% drop (c13, c14). These change decoding or training, not a prompt scaffold.

## 7. What our agent should take

Schema fit: the tree is built only at S6 under O1-O8. Children are ranked by test result in code. This subfield bears on how children are cut and when a line is abandoned.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Cut a branch only on a code-checked signal** (failing test, illegal move, violated constraint), never on the model's own opinion of the branch. Write it into the tree rules in section 4 as the only allowed prune trigger. | G2, G5, O3 tree rules | [E] | K13, K15; a24, c06, c11, d04 |
| A2 | **Log every prune** (branch, trigger, score) so false prunes can be counted later. | section 6 logging, G7 | [E] that pruners leak (K13) | b23, c06, d04 |
| A3 | **A bad first step alone does not prune.** In humans this reflex persists at cost and distorts learning; in LLMs the scorer is leaky. Treat "bad first step" as a hint that raises verification, not as a cut. | G1 | [E] as a warning (K03, K10); the cost-insensitive part is [S] (K02) | a01, a03, a06, a09, a10, b19 |
| A4 | **More depth, more verification, not less.** Humans prune more as depth and difficulty grow (gap 34/40/49 points). Keep G12 allocation by difficulty. | G12 | [E] in humans (K04); no LLM test | a04, a12, b04, b11 |
| A5 | **Do not trust a model score alone at equal tokens.** The fair ToT gap is 74 vs 49, and score pruning loses to sampling on easy items and at large budgets. Turn tree pruning on only for medium-hard items with a foothold (already G12). | G7, G12 | [E] for the fair comparison (K12); size of benefit [C] (K23) | a23, c05, d05, d06 |
| A6 | **Confidence early stop of one attempt** (when token probabilities exist) as a budget tool, not a branch judge. | G11 | [E] three sources, decoding-level, so only if the API gives logprobs | K17; c12-c14 |

### Test first

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code-triggered prune with sibling revival vs self-score prune vs no prune, equal tokens. | O3, G1, S5/S6 | [S] | K22, K25; d07, c11 |
| T2 | Minimum hold time before an attempt may be abandoned (0, 300, 600, 1000 tokens), enforced by code. Prompt-only failed in the one test. | G1, S6 | [S] | K24; d02, d03 |
| T3 | Loss-triggered pruning in an LLM: Huys maze in text. If the gap is large, add a rule that bad early outcomes never prune. | G1, S0 | [S] indirect | K21; a12, c19 |
| T4 | Depth-gated verification: raise check count with depth. | G12 | [S] | K04, K26 |
| T5 | Duplicate-merge instead of score-cut. | O3 | [S] | d01 |
| T6 | Strong model generates, code or cheap judge prunes. | G5 | [S] | K14; c07 |
| T7 | Rule-based legality and constraint pruning where the task has rules (exact, but size of gain unmeasured outside Hanoi). | G5, S4 | [S] | K18; c15, c16 |
| T8 | Novelty prune with dev-set tuning (G7). | G7, open mode | [S] | K19; c17 |
| T9 | Fragment stops at a bad intermediate result (O3 with a stop rule). | O3 | [S] | K05; a18, a19 |
| T10 | Causal trace audit: delete unchosen branches; if the answer does not change, cut that text. | G10 | [S] | K20; c04 |
| T11 | Anxiety or loss framing as a lever: do not add; test only to rule it out. | G1, 4b | [C] | K08, K21 |

Not to take: mood-driven pruning (K06), neural localisation (K09), pruning tied to anxiety or substance state (K07, K08).

## 8. Concrete tests on our bench

All arms at equal total tokens. Report per-item results with bootstrap intervals. Split every result by difficulty (plain-model pass rate).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1) | Code tasks with unit tests; ARC items with a check | A no prune (resample); B prune on failing test, revive best pruned sibling when live branches fail; C prune on model self-score | solve rate; right branches lost (logged) | B beats C by a few points; C no better than A (Huang 2024); B > A on medium-hard, equal on easy |
| E2 (T3) | Text Huys maze: 6 states, 2 actions, fixed gains/losses, depth 3-5; OLL vs ONLL; loss sizes -70/-100/-140 | A plain; B scaffold with "no cut on a single outcome"; C code-computed full-tree sums | accuracy ONLL minus OLL (human gap 41 points; 34/40/49 by depth) | LLM gap smaller than human; larger at depth 5 if the model does not enumerate; C removes it |
| E3 (T2) | Math items (AIME-style) with a thinking model | hold 0, 300, 600, 1000 tokens, code-enforced | pass@1; switches; correct thought abandoned | peak near 300-600; flat or negative at 1000 |
| E4 (A5) | Mixed easy, medium, hard | plain, best-of-N, one long line, prune-and-expand | solve rate vs tokens, by difficulty | tree pruning wins only on medium-hard at low budget |
| E5 (A2) | Same trees as E1 | logged prunes with oracle label | false-prune rate, self-score vs test trigger | self-score high (PAC-CF scale 50-64% on biased scorers); test trigger near 0 |
| E6 (T5) | GSM8K or MATH style trees | score-cut vs duplicate-merge | accuracy and node count | merge within 5 points accuracy with far fewer nodes |
| E7 (T4) | Problems with 3, 4, 5, 6 step solutions | fixed checks vs checks growing with depth | solve rate by depth | gain at depth 5+ |

## 9. What does not transfer, and why

- **Serotonin and Pavlovian neurobiology.** The agent has no serotonin system. The mechanism must be tested behaviourally (K09).
- **Mood and depression links.** Contested in humans (K06). An agent has no mood.
- **Loss as a payoff.** In the human task a loss is a number on a screen. In our tasks a failed check is information, not a loss. The trigger humans use (valence) is the one we should not use.
- **Effort saving.** Humans prune because search is slow. LLM search costs tokens, and code can enumerate a small tree in full (the human maze has at most 2^8 sequences).
- **Deep trees.** Humans plan 4-6 plies; LLMs reach 1.78. The human depth effect cannot be assumed for LLMs (K26).
- **Training-based methods.** ThinkPrune needs RL; TIP changes logits; DeepConf needs token probabilities. A prompt-level scaffold may not have these.
- **Small and old models.** ToT used GPT-4 and GPT-3.5; Wu 2024 used small open models; effects may not hold on 2026 models.
- **Self-score pruning from ToT.** Our schema forbids model judges without checks (G5). Take its tree structure, not its trigger.

## 10. Open questions

1. Does an LLM shown the Huys maze prune after a large early loss, and how big is the OLL-ONLL gap vs 41 points? (open)
2. Does LLM pruning grow with depth and token budget as in humans? (open; Chen 2026 shows breadth over depth)
3. Is a code-triggered prune with sibling revival better than self-score prune at equal tokens? (partly closed by CodeTree; single source)
4. How often does a ToT-style scorer discard the eventually correct branch outside Game of 24 and crosswords, and does it rise with scorer noise? (partly closed by PAC-CF)
5. Is the human cost-insensitivity of pruning replicated with several groups per loss size? (open)
6. Does ToT pruning survive an equal-token test against best-of-N on 2025-26 models? (contested)
7. What hold time avoids both over-pruning and over-switching? (TIP only)
8. Do anxiety or loss framings change the pruning of an LLM? (open)
9. What threshold would a resource-rational planner choose, and does it match gamma_S about 0.6? (open; Callaway 2022 unread)
10. Why does the learned Pavlovian state attraction appear in 2012 and vanish in 2022?
11. The meth study reports F(1,100) with 89 participants (repeated-measures df?); unexplained.
12. Does any independent task paradigm show loss-triggered pruning outside the Huys maze lineage?

## 11. Sources

[V] = opened and read by a searcher or the critique. [M] = snippet or not opened.

- [V] Huys et al. 2012, Bonsai trees in your head. https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002410 and https://pmc.ncbi.nlm.nih.gov/articles/PMC3297555/ (a01-a08, a25, b01-b05, b25, c01). Re-checked by critique.
- [V] Dayan and Huys 2008, Serotonin, inhibition, and negative mood. https://pmc.ncbi.nlm.nih.gov/articles/PMC2222921/ (a09-a11)
- [V] Lally et al. 2017, neural basis of aversive Pavlovian guidance. https://pmc.ncbi.nlm.nih.gov/articles/PMC5647774/ (a12-a15, b08-b11, b27, c02). Re-checked.
- [V] Faulkner et al. 2022, pruning in depressed and healthy. https://pmc.ncbi.nlm.nih.gov/articles/PMC9811346/ (a16, a17, b12-b15). Re-checked.
- [V] Huys et al. 2015, Interplay of approximate planning strategies. https://pmc.ncbi.nlm.nih.gov/articles/PMC4364207/ (a18, a19, b06, b07)
- [M] Huys et al. 2015 PNAS page (403). https://www.pnas.org/doi/10.1073/pnas.1414219112 (c25; content came via PMC)
- [V] Methamphetamine use disorder planning, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12103525/ (b16-b18). Re-checked.
- [V] Guitart-Masip et al. 2012, Go and no-go learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC3387384/ (a20)
- [V] Cools, Nakamura, Daw 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3055512/ (a21)
- [V] Keramati, Dezfouli, Piray 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3102758/ (a22)
- [V] Sezener, Dezfouli, Keramati 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6440644/ (b20; d15 not re-opened)
- [V] vmPFC lesion planning, 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11924998/ (b21)
- [V] Mahajan et al. 2025, Balancing safety and efficiency. https://pmc.ncbi.nlm.nih.gov/articles/PMC12490855/ (b19, b26)
- [M] Callaway et al. 2022, Rational use of cognitive resources in human planning. https://www.nature.com/articles/s41562-022-01407-x (c26, d11; login wall)
- [M] Knuth and Moore 1975. https://doi.org/10.1016/0004-3702(75)90019-3 (c23)
- [M] Buro 1999, ProbCut. https://webdocs.cs.ualberta.ca/~mburo/ps/probcut.pdf (c24)
- [V] Yao et al. 2023, Tree of Thoughts. https://arxiv.org/abs/2305.10601 (a23, a24, b24, c05-c07). Table re-checked.
- [V] Xie et al. 2023, Self-Evaluation Guided Beam Search. https://arxiv.org/abs/2305.00633 (c08; not re-opened by critique)
- [V] Hao et al. 2023, RAP. https://arxiv.org/abs/2305.14992 (c09; not re-opened)
- [V] Zhou et al. 2024, LATS. https://arxiv.org/abs/2310.04406 (c10; not re-opened)
- [V] Huang et al. 2024, LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c11). Re-checked.
- [V] Wang et al. 2025, Underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 and https://arxiv.org/html/2501.18585 (c12, d02, d03). Re-checked.
- [V] Hou et al. 2025, ThinkPrune. https://arxiv.org/abs/2504.01296 (c13; not re-opened)
- [V] Fu et al. 2025, DeepConf. https://arxiv.org/abs/2508.15260 (c14). Re-checked (offline vs online).
- [V] Mondal, Webb, Momennejad 2025, modular agentic planner. https://arxiv.org/abs/2310.00194 (c15, c16; not re-opened)
- [V] Novelty-based Tree-of-Thought Search, 2026. https://arxiv.org/abs/2605.06040 (c17; not re-opened)
- [V] ToolTree 2026. https://arxiv.org/abs/2603.12740 (c18; not re-opened)
- [V] Coda-Forno et al. 2024, Inducing anxiety in LLMs. https://arxiv.org/abs/2304.11111 (c19; d10 abstract only)
- [V] Jia et al. 2024, decision-making framework for LLMs. https://arxiv.org/abs/2406.05972 (c20; not re-opened)
- [V] Li et al. 2023, Emotional stimuli. https://arxiv.org/abs/2307.11760 (c21; not re-opened)
- [V] Valmeekam et al. 2023, Planning abilities of LLMs. https://arxiv.org/abs/2302.06706 (c22; not re-opened)
- [V] Qian et al. 2026, PAC-CF. https://arxiv.org/html/2604.14345v6 (b22, b23, d04). Re-checked.
- [V] Chen et al. 2026, Extracting search trees from LLM reasoning traces. https://arxiv.org/abs/2605.06840 and https://arxiv.org/html/2605.06840 (c03, c04, d09). Re-checked.
- [V] Kim et al. 2025, Chopping Trees (abstract page only). https://arxiv.org/abs/2511.08595 (d01)
- [V] Snell et al. 2024, Scaling test-time compute. https://arxiv.org/html/2408.03314 (d05)
- [V] Wu et al. 2024, Inference scaling laws. https://arxiv.org/html/2408.00724 (d06)
- [V] CodeTree 2024. https://arxiv.org/html/2411.04329 (d07)
- [V] Muennighoff et al. 2025, s1. https://arxiv.org/html/2501.19393 (d08)
- [M] PRM false negative vs false positive snippet. https://arxiv.org/pdf/2602.09305 (d12)
- [M] Negative searches for an LLM run of the Huys task and for replication of cost-insensitivity (d13, d14); search was partial.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.09-K01** (now single-source: the sources are not independent). Huys 2015 (PNAS) and Lally 2017 report the same 41 recruited / 37 analysed volunteers (Huys 2015: 'the same 37 subjects included there' for the fMRI report), so the '2015 sample' is not a fourth sample; independent samples are Huys 2012 (N=46), the Lally/Huys 2015 sample (N=37) and Faulkner 2022 (N=61, depressed and healthy), all one task from related labs.
- **B02.09-K03** (reworded: the sources support less). Numbers are right (iBIC 2472 vs 2466; Faulkner reward weight 7.25 vs loss -2.60), but Lally et al. call loss aversion 'evident' and Pruning+Loss the best model (dIBIC 5.8, which they report as an improvement), and Huys 2012 found subjects about 1.4x more sensitive to punishments than rewards; the robust finding is that pruning beats loss-aversion-only models, not that loss weighting adds nothing. Corrected claim: Pruning is not reducible to loss aversion: models with pruning beat models with loss weighting alone (Huys 2012, Lally 2017), and pruning remains after loss sensitivities are fitted. Loss weighting still adds a little: in Lally 2017 Pruning+Loss was the best model (iBIC 2466 vs 2472 for Pruning), Huys 2012 found punishments weighted about 1.4 times rewards although adding loss aversion to its best model did not improve parsimony, and in Faulkner 2022 the fitted large-gain weight (7.25) was about 2.8 times the large-loss weight (-2.60) in healthy controls.
