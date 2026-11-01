# Retrieval as a bandit: deep document

*Subfield C08.09 of case-based reasoning. Question: when an agent keeps a bank of past cases, should it pick the next case by similarity alone, or by a value learned from how well each case worked? Source files in this folder: evidence_a-d.jsonl (ids a01-a28, b01-b27, c01-c27, d01-d20), claims.jsonl (K01-K27), critique.md. Numbers were cross-checked against the PDFs (14 confirmed, 3 corrected; see section 5).*

## 1. What it is

A case bank holds past problems with their solutions and outcomes. At each new problem the agent must choose which case (or few cases) to show the model. The classic choice is nearest neighbour by similarity. The "bandit" view says this is a decision under uncertainty:

- Each stored case is an arm.
- Pulling the arm means putting that case in the prompt.
- The reward is whether the model then solves the problem (usually 0 or 1).
- The agent learns, over time, which cases pay off, and may try uncertain cases on purpose (exploration).

Three levels of "value" exist in the literature, from weakest to strongest:

1. Similarity only (ExpeL, ReasoningBank, AWM, Memp). No value is learned. [a25, a26, b17-b19, c18, c24]
2. A fixed hand-set score (Generative Agents: recency plus relevance plus importance). Not learned. [c20]
3. A value learned from outcomes. Sub-types: supervised from LM probability of the right answer (EPR, LLM-R, CEIL), reinforcement-style Q-values per case (Memento, MemRL, REMEMBERER, Sarukkai), and a true contextual bandit with an exploration bonus (CASCADE). [a01, a09, a12, a21, a22, b09, c11, d01]

The key finding of this subfield, in one line: **learned case value beats similarity in every direct head-to-head found, but the margin on a frozen strong model is small (about 0.6 to 3 points), most of the benefit of case memory comes from having any relevant case at all, and the exploration bonus is the weakest part.** [K01, K02, K03]

Scope note. Evidence here is machine-learning and LLM-agent work plus classic bandit theory. No human-subject study of outcome-weighted memory use is in this subfield's files. Links to other subfields are pointers only (sections 9 and 10).

## 2. History and theories in depth

**Case-based reasoning cycle (1994).** Aamodt and Plaza describe Retrieve, Reuse, Revise, Retain. Retention is part of the cycle: the case base is updated whether the solve worked or failed. Failures may be stored as separate failure cases to give a "reminding" of past failures. Retrieval indexes are tuned by outcome. Their paper is a conceptual review of 1990s systems (CASEY, PROTOS, PATDEX, CHEF) with no experiments and no growth-rate numbers. [d19, a28] CASCADE and Memento map this cycle onto a bandit loop.

**Bandit theory.**
- Thompson (1933) is the origin of sampling an arm in proportion to its chance of being best. Not opened. [a27]
- Auer, Cesa-Bianchi, Fischer (2002): UCB1 has logarithmic regret uniformly in time. In their own simulations on seven reward sets, a tuned epsilon-greedy rule "almost always" did best; UCB1-Tuned was comparable but unproven; UCB2 slightly worse; untuned epsilon-greedy degraded fast. [d11]
- Li, Chu, Langford, Schapire (2010): LinUCB. Linear score per arm plus a confidence-width bonus. Yahoo news data, over 33 million events; hybrid LinUCB gave up to 12.5% click lift over context-free epsilon-greedy, larger when data was scarce. Also gives an unbiased offline replay evaluation from random logs. [a16]
- Chapelle and Li (2011): Thompson sampling beat UCB and epsilon-greedy in simulation and in ad and news data; a damped version (posterior reshaped, alpha below 1) did slightly better. Display-ad regret %: Thompson 4.45 / 3.72 / 3.81 (alpha 0.25 / 0.5 / 1), LinUCB 4.99 / 4.22 / 4.14, epsilon-greedy 5.05 / 4.98 / 5.22, exploit-only 5.00, random 31.95. [d12]
- Kuleshov and Precup (2014): 12 instances (K = 2, 5, 10, 50 arms), 1000 steps, tuned per instance. Softmax and epsilon-greedy beat UCB1 in most settings. At K=50 regret: UCB1 296, UCB1-Tuned about 119, softmax about 32, epsilon-greedy about 29 to 40. UCB1 converged slowest. [d10]
- Garivier and Moulines (2008): under abrupt changes of the best arm no policy beats about sqrt(T) regret; discounted and sliding-window UCB get within a log factor. [d13]
- Neural bandits: NeuralUCB (Zhou 2020) and Neural Thompson (Zhang 2021) give sqrt(T) regret bounds but need very wide networks. Riquelme 2018 found no uncertainty method wins everywhere; Bayesian linear regression on the last layer was the robust choice. Russo 2018: a misspecified prior raises regret. [a17-a20]

**Learned example selection before agents (2021-2024).**
- KATE (Liu 2021): nearest neighbours in embedding space beat random for GPT-3; NQ exact match random 28.6 vs about 41-42 for best variants (columns partly garbled). [b10]
- Zhang, Feng, Tan (2022): first Q-learning view of picking demonstrations as a sequential decision. [a23, b01-b04]
- EPR (Rubin 2022): label each candidate by the LM's probability of the right output, train a dense retriever. [a21, b05, b06, c14]
- LLM-R (Wang 2023): reward model from LLM log-probabilities, distilled to a retriever, iterated. [a22, b07, b08, c15]
- CEIL (Ye 2023): whole-set selection with a determinantal point process. [b09, c23]
- Min 2022: random labels in demonstrations barely hurt, so demonstrations mostly carry format. [b11]
- Levy 2023: choose a set that covers needed structures. [d17]

**Agent memory with outcome value (2023-2026).**
- REMEMBERER (2023): (goal, observation, action, Q) records, n-step updates. [c11, c12]
- Memento (2025): soft Q-learning over a case bank, frozen LLM. [a09-a11, b12-b16, c01-c04]
- MemRL (2026): two-phase retrieval, blend of similarity and Q. [a12-a15, c05-c10, d05, d06]
- Sarukkai et al. (2025): self-generated examples with a plain empirical success rate per trajectory, 5 seeds. [d01-d04]
- CASCADE (May 2026): explicit contextual bandit with UCB over cases, with a regret theorem. [a01-a08]
- Memory-management and benchmark studies: Xiong 2025, Evo-Memory 2026. [d07-d09, d15, d16]
- Distilled memory with no learned retriever: ReasoningBank, Dynamic Cheatsheet, Memp, ExpeL, AWM, Memory-R1. [a26, b17-b24, c16-c19, c24]
- Prompt-pool bandits (not cases): TRIPLE, INSTINCT. [c21, c22]

**Competing theories of why case choice matters.**
1. Relevance theory: the best case is the most similar one; value learning only fixes retrieval noise. Support: Evo-Memory finds plain top-k similarity (ExpRAG) competitive with complex systems. [d15]
2. Utility theory: similar is not the same as useful. EPR beat a BM25 oracle that uses the gold answer on two of three datasets, so surface similarity to the answer is not what makes a case useful. [b06]
3. Format theory: demonstrations teach format, not content, so a learned value is mostly learning "what format fits". Random labels cost only 1.7 to 2.6 points. [b11]
4. Coverage theory: a set of cases should cover what is needed; one-by-one scoring misses it. [b09, d17]

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single = one source; contested = sources disagree or the result is inflated by a flaw.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Learned case choice beats non-learned case retrieval, 12 tasks, Qwen3-32B, 5 seeds | CASCADE 66.68 vs NP-CBR 63.76 (+2.92); zero-shot 48.33; ICRL 52.48; ICRLPlus 54.33; REINFORCE+LoRA 58.93 | a03 (CASCADE) | single (preprint) |
| Same, smaller backbones | 8B 60.84 vs 58.44 (+2.40); 14B 65.10 vs 62.81 (+2.29) | a05 | single |
| Most of the gain is having cases at all | +15.4 of +18.35 over zero-shot is non-learned retrieval; bandit adds +2.92 | a03 | established (K02) |
| Exploration bonus is the weakest part | alpha=0: 66.37 vs 66.68 (-0.31); beats full method on SEntFiN 48.37 vs 47.72, TLP 57.09 vs 56.79, BIRD (NeuralLogUCB 56.21 vs 55.18); LinLogUCB 63.95; NeuralLogUCB 65.39; NeuralLinUCB 65.49 | a04 | single (K03) |
| Learned reranker gain shrinks with a stronger agent loop | ALFWorld Act: 62.01 to 67.43; ReAct: 80.76 to 81.74 (+0.98). ScienceWorld Act 59.36 to 66.84; ReAct 71.52 to 74.67 (+3.15) | a06 | single |
| Tool-use QA and EHR | 2Wiki local RAG 45.94 to 50.06; web 53.29 to 66.51; MIMIC-III EHR 20.75 zero-shot, 44.02 NP-CBR, 55.76 CASCADE | a06 | single |
| Bandit score used to pick items for human labels | Relative gain over standard CASCADE: exploit metric +8.83%, UCB +8.73%, random +5.61% (10% budget) | a07 | single |
| Learned Q beats similarity in Memento, tiny margin | DeepResearcher iter 1 to 5: none 78.65 to 84.47; similarity 79.84 to 84.85; learned 80.46 to 85.44; learned minus similarity +0.62, +0.97, +1.01, +0.82, +0.59 | a10, c02 | single (K01 margin) |
| Any case memory in Memento | CBR adds +6.7 F1 / +8.2 PM (DeepResearcher), +4.5 / +7.0 (HLE), +3.7 / +5.3 (SimpleQA); but learning curve shows only +1.81 (iter 1), +0.97 (iter 5) vs none | a11, c02 | contested (protocols differ; do not add them) |
| Number of cases: 1 to 4 best | Memento F1/PM: K=0 59.9/72.2; 1 63.6/77.9; 2 63.7/78.1; 4 64.5/78.5; 8 64.1/78.2; 16 63.9/78.1; 32 63.9/78.1. ReasoningBank Shopping: 0 -> 39.0; 1 -> 49.7; 2 -> about 46; 3 -> 45.5; 4 -> 44.4 | a11, a26, b20 | established (K04) |
| MemRL beats RAG and other memories over 10 epochs | Avg last/cumulative: none 0.631; RAG 0.679/0.699; Mem0 0.681/0.712; MemP 0.736/0.760; MemRL 0.772/0.798 | a13, c06 | single; runtime flatters |
| MemRL transfer is smaller | Frozen bank, held-out: MemRL 0.794 vs MemP 0.766 vs none 0.709; vs RAG gap 2.8 vs runtime gap 8.15 (my cross-table computation, different splits) | a13, d05 | single (K20) |
| Value learning needs recurring, similar tasks | MemRL vs single-task reflection: avg 0.798 vs 0.761; OS +9.0, ALFWorld +5.1; HLE tie 0.606 vs 0.610 (task similarity 0.186). Evo-Memory gain vs task similarity Pearson 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet) | a15, c09, d06, d15 | established (K05) |
| Blend similarity with Q | MemRL lambda=0.5 best (inverted U over 0, .25, .5, .75, 1); numbers only in a figure | a12, c07 | single (K06) |
| Q tracks success (in-sample) | Pearson r=0.861; success 21.5% (lowest Q bin) to 88.1% (highest); about 12% of top-Q memories are failures | a14, c08 | single (K07) |
| Supervised learned retrieval (EPR), dev | BREAK 26.0 (BM25) -> 31.9; MTOP 52.9 BM25, 57.0 prior CBR -> 64.2; SMCalFlow 46.1 BM25, 51.4 CBR -> 54.3; BM25-oracle 32.3 / 58.9 / 47.3; random 1.7 / 7.3 / 8.9. Test BREAK BM25 17.6 -> EPR 23.9 | a21, b05, b06 | established (K08); a21 mislabels dev as test |
| LLM-R, 30 tasks, LLaMA-7B, 8 examples | random 57.9; k-means 57.0; BM25 61.3; E5 61.4; SBERT 62.1; EPR 63.5; LLM-R iter 1 65.7, iter 2 66.5, iter 3 66.4. Held-out 4 tasks: LLM-R 81.7 vs E5 76.3 | a22, b07, c15 | established; "+7.8%" is 7.8 points |
| Learned retrieval can fail | LLM-R below random on SQuAD (near duplicates, low diversity); small gains on reading comprehension, sentiment, knowledge-heavy tasks | b08 | established with b11, d17 (K09) |
| Random labels barely hurt | 12 models, 16 demos: -1.7 avg (multi-choice), -2.6 (classification); range 0 to 5 | b11 | established |
| Set-level selection beats one-by-one | CEIL avg 64.86 (EPR) vs 68.86 (CEIL n=100); ablation TopK-EPR 57.64, DPP-EPR 59.95, TopK-CEIL 60.73; GeoQuery +2 (template) / +5 (standard) over EPR. Levy: Cover-LS vs Top-K 91.4 vs 88.9 iid, 81.6 vs 74.7 template, 76.3 vs 69.4 TMCD, 70.0 vs 65.8 length | b09, c23, d17 | established (K10); CEIL table garbled |
| Choice of examples matters a lot on small old models | GPT-2: over 30 points spread over 30 random 4-sets; AGNews best 79.5 vs worst 26.1; best of 24 orderings only +8.1% | b01, a23 | single, older models (K11) |
| Learned policy about equals best-of-10 random draws | Same task: random 59.6; max-entropy 59.3; reorder 63.5; best-of-10 72.5; greedy oracle 78.0; learned 71.4 / 71.6 / 69.0. New task: 63.8 (100 cands), 65.4 (1000) vs reorder 63.5 | b02, b03 | single, older models |
| Greedy empirical case value, 5 seeds | gpt-4o-mini, ALFWorld / SQL / Wordcraft: fixed DB 0.73 / 0.75 / 0.55; naive accumulation 0.89 / 0.79 / 0.64; plus exemplar Q curation 0.90 / 0.81 / 0.72 (extra +1, +2, +8) | d01 | single (K21) |
| Curated bank equals repeated sampling | Fixed DB pass@1-5: ALFWorld 0.73/0.87/0.92/0.94/0.96; SQL 0.75/0.78/0.80/0.81/0.82; Wordcraft 0.55/0.62/0.64/0.66/0.72. Naive accumulation sits between pass@2 and pass@3; DB+exemplar curation between pass@3 and pass@5. ALFWorld +20 from accumulation vs +15 from gpt-4o-mini to gpt-4o | d03 | single |
| Label quality decides whether bank growth helps | Fixed memory 67.53 / 16.75 / 40.11 / 71.50 (RegAgent SR / EHRAgent ACC / AgentDriver SR / CIC-IoT ACC); add-all 55.48 / 13.05 / 32.32 / 59.90; coarse judge C1 63.18 / 26.19 / 36.92 / 74.00; C3 (tuned on 300) 67.35 / 34.66 / 47.37 / 79.50; strict human-grade 70.95 / 38.50 / 51.00 / 85.40 | d07 | established (K22) |
| Utility-based deletion | Strict evaluator: EHRAgent 42.06 vs 38.67; CIC-IoT 89.60 vs 85.40; RegAgent 69.80 vs 70.95; AgentDriver 51.81 vs 51.00. Coarse C1: AgentDriver 34.00 vs 36.92 (down). Periodic deletion cuts memory to a quarter to a third | d08 | single (K23) |
| Distilled lessons tolerate label noise | ReasoningBank judge 72.7% accurate; simulated accuracy sweep about 52 (100%), 49.7 (70-80%), 47.6 (50-60%) vs none 39.0 | a26, d14 | established with d07 |
| Failures: raw hurts, lessons help | ReasoningBank success-only 46.5 -> with failures 49.7; Synapse 40.6 -> 41.7; AWM 44.4 -> 42.2 (falls) | d14, d16, d19 | established (K26) |
| Naive verbatim retrieval can hurt | Dynamic Cheatsheet GPT-4o: Game of 24 10 -> 6 (retrieval only) vs 93 (curation) / 99 (both); MMLU-Pro Eng 53.2 -> 48.8; Memp random 74.59 beat Key=Query 73.38 for GPT-4o | b21, b22, c18 | established (K14) |
| Reward design | Memory-R1 PPO judge reward F1 33.69 vs exact-match 41.05 | b24 | single |
| Prompt-pool bandits (not cases) | TRIPLE +9.7 / +13.5 / +17.4% over uniform at 10 evals per prompt, about 8% at 20; INSTINCT best on 11 of 20 tasks, avg rank 1.8, 3 seeds | c21, c22 | single each (K16) |
| Best-of-N competes for tokens | SWE-bench Lite coverage 15.9% (1 sample) to 56% (250); MATH Llama-3-8B coverage 82.9% to 98.44% but majority vote 40.50% to 41.41% | d18 | established (K27) |
| REMEMBERER, early value-tagged memory | WebShop 0.68 / 0.39 vs ReAct 0.66 / 0.36; WikiHow 2.63 / 0.93 vs 2.50 / 0.89 | c11 | single (K13) |

## 4. Mechanisms and models

### 4.1 The generic loop (what every system shares)

1. Recall: take the new query q. Use a fixed embedder to get K candidates (CASCADE K=32; MemRL k1 with a similarity threshold; Memento top-K).
2. Score: give each candidate a score that mixes similarity and learned value.
3. Pick: choose the top 1 to 4 (best evidence: 1 to 4; K04).
4. Act: put the case(s) in the prompt, run the frozen model.
5. Reward: get a success bit r (best if verifiable by code).
6. Update: change the value of the case(s) shown; optionally add the new run to the bank.

### 4.2 CASCADE (contextual bandit) [a01, a02]

- Case = (query, answer, reward). Only cases with r=1 are retained.
- Stage 1: recall K=32 by a fixed embedder. Stage 2: a trained reranker (encoder plus linear head) scores (query, case).
- Pick rule (Eq 7): score = linear-head output + alpha * uncertainty of the encoder feature. Authors suggest alpha=0.1.
- Update: the linear head gets one gradient step per step; the encoder is retrained every H steps by batch logistic loss.
- Theory: regret = coverage gap (no good case in bank; closes as the bank grows) + retrieval regret (good case exists, wrong one picked). Coverage gap O~(T^((d0-1)/d0)) for intrinsic dimension d0 above 1; retrieval regret O~(B*sqrt(T)/kappa); total sublinear. Assumes i.i.d. queries, Lipschitz best case, positive frozen-LLM success chance.
- Implementation note: the bonus is nearly free to drop (alpha=0 costs 0.31). The reranker carries the gain.

### 4.3 Memento (soft Q-learning) [a09, b12, c01]

- Policy pi(c|s,M) = exp(Q(s,c)/tau) / sum exp(Q/tau).
- TD update: Q <- Q + eta [ r + gamma * alpha * logsumexp Q' - Q ]. For single-step tasks it reduces to a supervised target: Q = P(case is a good reference), trained with cross-entropy on the binary success reward.
- Parametric Q is a 2-layer MLP on SimCSE embeddings; the non-parametric variant is cosine similarity only.
- Stores successes and failures. Only the final step of a trajectory is written.
- Engineer's reading: a softmax over Q is a built-in exploration rule (Boltzmann), the form Kuleshov and Precup found strong. [d10]

### 4.4 MemRL (blend) [a12, c05]

- Memory triplet (Intent, Experience, Utility Q).
- Phase A: recall by cosine similarity, threshold plus top-k1.
- Phase B: score = (1 - lambda) * z(similarity) + lambda * z(Q); inject top k2. Best lambda 0.5; best sizes k1=5, k2=3 on HLE.
- Q update: Monte Carlo rule from task reward. Authors admit high variance in long traces and unclear credit when several memories are shown together.
- Z-scoring both terms is what makes the blend weight meaningful. Copy this.

### 4.5 Sarukkai greedy value (simplest multi-seed version) [d02, d04]

- Q(trajectory) = success rate of the tasks where it was retrieved, weighted by retrieval frequency.
- Only trajectories retrieved for at least 3 distinct tasks get a value.
- Per task, keep only the highest-Q successful trajectory. Top-1-Q databases beat bottom-1-Q databases (ALFWorld, Wordcraft; values only in a figure).
- No bonus term, plain empirical mean. Retrieval: top-k similarity, k=6 (ALFWorld, SQL), 10 (Wordcraft). Naive accumulation varies between runs (early lucky examples snowball), which motivates curation.

### 4.6 Supervised value: EPR and LLM-R [b05, b07]

- For each training example, score candidates by the LM's log-probability of the correct output given that candidate as the prompt. Top-5 are positives, bottom are negatives (EPR: candidates are first pruned by BM25, so the retriever only re-ranks).
- Train a dense retriever contrastively. LLM-R adds a cross-encoder reward model, distills it, and mines hard negatives per iteration.
- Cost: one LM scoring pass per candidate, offline, with gold outputs. Gains stop after about 2 rounds.

### 4.7 Exploration rules (if exploring)

- Greedy with small epsilon: robust; tuned epsilon-greedy won most of Auer 2002. [d11]
- Boltzmann/softmax: strongest in Kuleshov and Precup 2014. [d10]
- Thompson on per-case Beta posteriors: simple, best stochastic rule in Chapelle and Li; good under delayed feedback. [d12]
- UCB: worst of the group at many arms (UCB1 regret 296 vs about 32 for softmax at K=50). Case banks can have hundreds to thousands of arms. [d10]
- Drift: use discounted or sliding-window estimates. [d13]
- Caveat: all classic comparisons are stationary and context-free, with millions of pulls (ads) or thousands (simulations). A case bank gives each case a handful of pulls. [d12]

### 4.8 Set-level selection [b09, d17]

- CEIL: conditional DPP over the whole exemplar set (relevance plus diversity), trained contrastively on LM feedback.
- Cover-LS (Levy): pick demonstrations so that needed structures are covered; needs a structure predictor. One failure: SMCalFlow 0-C split near 0 accuracy because the predictor scored 0.
- Engineer's reading: a cheap form is greedy selection with a redundancy penalty (marginal relevance) at the same K.

### 4.9 Budgeted evaluation of candidates [c21]

- TRIPLE treats choice from a pool as fixed-budget best-arm identification: successive halving or continuous rejects, with embedding clustering to share information. Gains fade as budget grows.
- For cases: per query type, evaluate a small shortlist of cases on a few probe problems, halve, keep the best.

### 4.10 Bank hygiene

- Utility-based deletion: drop records with low average downstream success after at least n retrievals. Works only with a strict evaluator. [d08]
- Periodic pruning cuts memory to a quarter to a third with small loss. [d08]
- Under an abrupt task shift, addition plus utility deletion kept performance close to the no-shift run; a cap of 100 to 180 records with utility eviction still beat fixed memory. [d09]

## 5. What holds up

**Replications and cross-checks.** No independent replication of CASCADE exists (single preprint, v1, 5 May 2026, self-reported 5-seed results). [a01, K17] Memento, MemRL, Memory-R1 and ReasoningBank report single runs without error bars. No paired significance tests anywhere in the set. [critique]

**Number checks done by the cross-checker (14 confirmed, 3 corrections).**
- Confirmed: CASCADE averages and ablations; baselines; 8B and 14B; ALFWorld and ScienceWorld; discovery budget; Memento Table 4 and K table; MemRL Table 1 and frozen transfer 0.794 vs 0.766, r=0.861; Active Example Selection numbers; LLM-R and EPR numbers.
- Correction 1: EPR 26.0 -> 31.9, 57.0 -> 64.2, 51.4 -> 54.3 are DEV, not test. Test: BREAK BM25 17.6 vs EPR 23.9. The 57.0 and 51.4 baselines are the prior learned retriever (CBR), not BM25 (52.9 and 46.1), so gains over BM25 are larger.
- Correction 2: LLM-R "+7.8% over random" is 7.8 points (65.7 vs 57.9) for iteration 1; iteration 2 is +8.6 points.
- Correction 3: ReasoningBank k=2 is "about 46" (the printed 46.5 equals the Synapse number elsewhere in the paper).

**Consistent patterns.**
- Direction: learned beats similarity in all direct comparisons (Memento +0.6 to +1.0; MemRL +3.6 over MemP; CASCADE +2.9; EPR +2.9 to +7.2 on dev; LLM-R +5.4 on held-out; Sarukkai +1 to +8). [K01]
- The stronger the base, the smaller the gain: Active Example Selection fades from GPT-2 to larger GPT-3; CASCADE gain under ReAct is +0.98 and +3.15; Memento +0.6 to +1.0; Evo-Memory says smaller models gain most. [a23, a06, c02, d15, K19]
- Saturation: Memento bank saturates at about 3k items; LLM-R stops after iteration 2; marginal gains of added learned layers shrink. [a10, a22, K19]
- Recurring and similar tasks are required. [K05]

**Tensions and weak results.**
- Memento: case memory adds +1.8 (iter 1) and +1.0 (iter 5) in the learning curve but +6.7 F1 / +8.2 PM in the ablation. Different protocols; not additive. [critique]
- CASCADE's "bandit" label is carried by the learned reranker, not the bonus: alpha=0 is within 0.31 points, inside per-task noise (SD 0.1 to 1.0). A linear bandit on frozen features gains only +0.19 over no bandit. [a04]
- MemRL's HLE gain is memorisation of repeated items (its own Appendix B). Runtime gain 8.15 points vs 2.8 on frozen held-out for four shared benchmarks. Cumulative success counts any-epoch success, which flatters exploration. [c10, d05, d06]
- Memento GAIA 87.88% Pass@3 is built on the same split; authors warn of contamination on DeepResearcher benchmarks. [b15, b16]
- A learned policy for example choice transfers poorly to a new task: 65.4 vs 63.5 for plain reordering, with CI up to +/-13 on single tasks. [b03]
- LLM-R fell below random on SQuAD. [b08]
- Dynamic Cheatsheet: retrieval only dropped GPT-4o on Game of 24 (10 to 6) and MMLU-Pro Eng (53.2 to 48.8). Small test sets (AIME: one problem is 3.3 points). [b22, b21]
- REMEMBERER: tiny margins (+3 success points on WebShop, +0.05 reward on WikiHow), no test. [c11]
- Memory-R1 trains weights; EPR and LLM-R train a retriever on gold outputs; neither is a pure scaffold result. [b23, a21]

**Moderators found.**
- Task recurrence and within-dataset similarity (Pearson 0.717 and 0.563). [d15]
- Base competence: with near-zero zero-shot success all methods fail (Qwen3-4B on MIMIC-IV-MR). [a05, K12]
- Model size: small old models gain most. [a23, b01]
- Evaluator quality: an untuned judge leaves a raw bank below fixed memory. [d07]
- Number of cases: 1 to 4. [K04]
- Bank content: raw verbatim cases can hurt; distilled lessons are safer. [K14, K26]
- Duplicate-heavy banks: learned retrieval picks near duplicates. [b08]
- Drift: running means lag; use discount or window. [d13, K25]

**Interventions that worked.**
- Having at least one relevant case (largest effect). [K02]
- Learned reranker or Q blended 50/50 with similarity. [K06]
- Greedy empirical success rate per case with min 3 retrievals (multi-seed). [d01, d02]
- A strict or tuned evaluator before writing to the bank (AgentDriver 47.37 with a 300-run tuned judge vs 36.92 untuned). [d07]
- Utility-based deletion with a strict evaluator. [d08]
- Distilling lessons rather than storing raw trajectories. [d14, b21]
- Set-level selection with coverage or diversity. [d17, b09]
- Using the bandit's own score to choose which items to send for human labels (+8.7% relative vs +5.6% random). [a07]

**Interventions that did not work or are unproven.**
- UCB bonus over greedy. [a04, d10-d12]
- More than 4 retrieved cases. [a11, a26]
- Storing raw failures under baselines that do not distil. [d16, d14]
- Judge-based reward (verbose answers). [b24]
- Learned policy transfer to a new task or larger model. [b03, a23]
- A third LLM-R iteration. [a22]
- Utility deletion with a coarse judge (AgentDriver 34.00 vs 36.92). [d08]

**Not obtained.** Thompson 1933, 1990s case-based reinforcement learning, Smyth and Keane retention work. Reflexion (first page only), ExpeL results tables (read via other papers), AWM (abstract and intro), KATE and CEIL tables (garbled). [critique]

## 6. Language models

**Which models.** CASCADE: Qwen3-4B/8B/14B/32B and Qwen3-30B-A3B, frozen. Memento: GPT-4.1 planner, o3/o4-mini executors. MemRL: GPT-4o, GPT-4o-mini, GPT-5-mini and a Gemini-class backbone (different per benchmark). ReasoningBank: Gemini-2.5-flash plus two others. Evo-Memory: Gemini 2.5 Flash and Claude 3.7 Sonnet. Sarukkai: gpt-4o-mini and gpt-4o. EPR/LLM-R: GPT-Neo, LLaMA-7B. Dynamic Cheatsheet: GPT-4o, Claude 3.5 Sonnet. [a01, a09, a13, a26, d15, d01, b21]

**How they behave.**
- A single relevant case gives most of the benefit; added cases add under 1 point each (Memento +3.7 F1 from the first, then under 1). [c03]
- Frontier models do not need the learned layer much. Evo-Memory finds the plain similarity baseline (ExpRAG) competitive, e.g. ALFWorld 0.76 / 0.90 (Claude 3.7 Sonnet) vs ReMem 0.92 / 0.96, where ReMem rewrites memory with the LLM and is not a value learner. [d15, d16]
- Frozen-bank transfer is the honest number: MemRL +2.8 over RAG, +8.5 over no memory (0.794 vs 0.709). [d05]
- Recording the agent's own successes is itself strong: on ALFWorld +20 points from accumulation vs +15 from upgrading gpt-4o-mini to gpt-4o. [d03]
- A curated bank at a single attempt equals 2 to 5 attempts from a fixed bank; test cost is unchanged, training cost is N times (N parallel databases). Costs are call counts, not tokens, and pass@k assumes an oracle verifier. [d03]
- Format matters more than content on older models: random labels cost 1.7 to 2.6 points. [b11] Later work suggests larger models use labels more; not shown here.
- Example-choice spread: on GPT-2, random sets spread over 30 points; the learned policy lands near best-of-10 random draws. On large models the spread is expected to be much smaller (not measured here). [b01, b02]
- Best-of-N: with a verifier, coverage 15.9% to 56%; without, majority vote barely moves (40.50% to 41.41%). [d18]
- Smaller models benefit most; Qwen3-4B on one task has no signal to learn from. [a05, d15]

**What changed it, by how much.**

| Lever | Change |
|---|---|
| Add any relevant cases (CASCADE) | +15.4 points avg |
| Learned reranker over similarity (CASCADE) | +2.9 (32B), +2.4 (8B) |
| Remove exploration bonus | -0.31 |
| Learned Q vs similarity (Memento) | +0.6 to +1.0 |
| Utility blend (MemRL) | runtime +3.6 over MemP; frozen +2.8 |
| Own-trajectory accumulation (Sarukkai) | +16 / +4 / +9 on ALFWorld / SQL / Wordcraft |
| Learned value on top of accumulation | +1 / +2 / +8 |
| Tuned judge vs untuned for bank writes (AgentDriver) | 47.37 vs 36.92 |
| One case vs four (ReasoningBank) | 49.7 vs 44.4 |

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the class record and lesson store (read at S0, written at S9).
Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Keep 1 to 4 cases, default 1 to 2.** Part: memory read at S0/S3. [E] Evidence: a11, a26, b20, c03, c17 (K04).
2. **Have a relevant case before adding any learned layer.** Build the bank of successes first, then measure. Part: memory, S9 write; G7 (every element must win at equal tokens). [E] Evidence: a03, c03, a11 (K02).
3. **Write to the bank only on a trusted outcome.** Prefer a code-verified result (S4/S8) as the success label; if a model judge is used, check its accuracy on a sample of own runs first. Part: S9 with G2, G3, G10. [E] Evidence: d07, d14, b24, a26 (K15, K22).
4. **Store failures as short avoid-lessons attached to a class, not as retrievable raw examples.** Part: S9 lesson line. [E] Evidence: d14, d16, d19 (K26).
5. **Prefer a distilled strategy or lesson over a verbatim trajectory in the prompt.** Part: memory. [E] Evidence: b21, b22, c18 (K14).
6. **Do not make a UCB bonus the default.** If exploring at all, use plain greedy with small epsilon or Thompson on per-case Beta counts. Part: memory. [E] Evidence: d10, d11, d12, a04 (K24).
7. **Handle drift: use a window or discount on per-case value, and cap the bank by periodic pruning (retrieval count).** Part: memory hygiene. [E] Evidence: d13, d09, d08 (K25).
8. **Use learned value only inside a recurring class; gate by class.** Gain needs recurring similar tasks. Part: S0 gate (class record). [E] Evidence: a15, c09, c10, d15 (K05).
9. **If more than one case is shown, avoid near duplicates (simple diversity or coverage term).** Part: memory read. [E] Evidence: b08, b09, d17 (K09, K10).
10. **Claim a learned case value only after it wins at equal tokens, paired, multi-seed.** Part: G7. [E] Evidence: critique gap 1 (no study reports CIs on frontier models).

### Test first (single-source, contested, or older models only)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Per-case empirical success rate (min 3 retrievals) added to similarity, top-1 | memory | [S] | d01, d02 (K21) |
| 50/50 z-scored blend of similarity and utility | memory | [S] | a12, c07 (K06) |
| Learned reranker from LM feedback on our logs (EPR style) | memory | [E] on old models; [S] for us | a21, a22, b07 (K08) |
| Exploration bonus (UCB, Thompson) over greedy | memory | [C] | a04, d10-d12 (K03) |
| Utility-based deletion with a verified outcome | memory | [S] | d08 (K23) |
| Successive halving over a case shortlist per class | O/memory | [S] | c21 (K16) |
| Set-level (diversity) selection with a learned value | memory | [S] | b09, d17 |
| Bandit score to decide when to ask for an external label | G12/S6 | [S] | a07 |
| Learned case value vs best-of-N at equal tokens | G7/G12 | [S] | d03, d18 (K27) |
| Success-only vs both outcomes under a learned selector | memory | open | d20 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost, any scoring pass, judge calls and retrieval overhead counted). At least 5 seeds, paired difference with 95% CI, non-repeating test items, frozen bank for the test phase.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Recurring-class stream (20+ items per class, e.g. ARC-style rule families) | A: top-1 similarity from verified-success bank. B: top-1 by 0.5 z(sim) + 0.5 z(Q) | Pass rate on held-out items, paired | +0 to +3 points; below 1 means drop it |
| T2 | Scattered tasks (distinct classes) | Same arms | Pass rate | Tie (MemRL HLE pattern) |
| T3 | Bank ablation | none vs similarity vs learned | Pass rate | Most of the gain from the first step (K02) |
| T4 | K sweep K in {0,1,2,4,8} | Fixed prompt budget | Pass rate | Peak at 1 to 4 |
| T5 | Exploration over a long stream | Greedy Q, epsilon-greedy (0.1), Thompson (Beta), UCB | Cumulative regret vs oracle best case; final pass rate | Greedy or Thompson match or beat UCB |
| T6 | Drift: switch task family mid-stream | Running mean vs discounted/window value | Regret over the 100 items after the switch | Window recovers faster |
| T7 | Label noise: success from code vs untuned model judge vs tuned judge | Same bank logic | Pass rate; judge accuracy on 100 sampled runs | Untuned judge falls below fixed memory |
| T8 | Failures: success-only vs raw failures vs failure lessons | Learned selector on | Pass rate | Lessons >= success-only > raw failures |
| T9 | Token trade: N samples + verifier vs 1 sample + learned-value case | Total tokens matched | Pass rate | Verifier arm wins on checkable items; learned value wins where no verifier exists |
| T10 | Duplicate-heavy bank: top-K vs top-K with redundancy penalty | Same K | Pass rate | +1 to +3 |
| T11 | Spread check: 20 random case sets per class | none (diagnostic) | Max minus min pass rate | Spread under 3 points means skip value learning |
| T12 | Memorisation control: repeated vs unseen items, frozen bank | Same arms | Gain on repeated minus gain on unseen | Repeated larger (MemRL 8.15 vs 2.8) |
| T13 | Pruning: none vs periodic prune by retrieval count vs utility eviction | Bank at 25% size | Pass rate | Within 1 point of full bank |

## 9. What does not transfer, and why

- **Weight-trained pieces.** CASCADE's reranker, EPR/LLM-R retrievers and Memory-R1 train parameters on labelled data. Our agent is a scaffold with no training. Only value-table and counting versions (Sarukkai, REMEMBERER, MemRL's Q table) are scaffold-pure. [a01, a21, b23]
- **Large stationary pull counts.** Classic bandit wins (Thompson, UCB regret) come from millions of ad impressions or 1000-step simulations; case arms get a handful of pulls. [d12, d10]
- **Single-step click reward.** LinUCB reward is a click; ours is a delayed, noisy solve. [a16]
- **Old-model effects.** The 30-point spread and the policy-transfer numbers come from GPT-2/GPT-3-era models and classification. [b01, a23]
- **Runtime gains on repeated items.** MemRL runtime and Memento Pass@3 gains include memorisation of seen items; our bench items should not repeat. [c10, b16]
- **Semantic-parsing tasks.** EPR/CEIL/Levy gains are on BREAK, MTOP, SMCalFlow, GeoQuery with Codex or GPT-Neo, where demonstration structure is decisive. [b05, d17]
- **i.i.d. regret theory.** CASCADE bounds need i.i.d. queries and Lipschitz case value; real streams drift and case value depends on the query. [a02, d13]
- **Memory-QA benchmarks.** Memory-R1 and LoCoMo are dialogue recall, not problem solving. [c16]
- **LLM-distilled memory.** ReasoningBank and Dynamic Cheatsheet change what is written, not which stored item is picked; their label-noise robustness does not carry to selection. [d14]
- **Human-label discovery budget.** CASCADE's labelling simulation uses ground-truth labels at 10% budget; not a thinking-time lever. [a07]
- **Cross-links, no content here.** Retrieval and similarity, exploration and exploitation, bandit-style exploration, case-base maintenance, retention policy, relevance-based fate of memories, analogical retrieval (MAC/FAC) and test-time compute scaling are covered by other subfields in this run.

## 10. Open questions

1. Does learned value add anything over top-1 similarity on a frontier model at equal tokens, with paired multi-seed CIs? Best frontier-class numbers are +0.6 to +3 without seeds. [critique gap 1]
2. UCB vs Thompson vs greedy vs epsilon-greedy over a case bank, with regret reported. No study exists. [gap 2, d20]
3. Break-even task similarity for learned value; behaviour under non-i.i.d. streams. [gap 3, d15]
4. Fraction of MemRL and Memento runtime gain that is memorisation, measured on a clean split. Current estimate (two thirds) is a cross-table calculation. [gap 4, d05]
5. Break-even judge accuracy at which a learned selector beats similarity. [gap 5]
6. Credit assignment when several cases are shown together. Only crude schemes exist (Sarukkai retrieval-frequency weighting). [gap 6]
7. Failures under a learned selector (success-only vs both). [gap 7]
8. Equal-token payback of value learning vs best-of-N or extra sampling. Existing numbers are call counts, not tokens. [gap 8, d03]
9. Retention-policy and case-base growth results from the 1990s case-based reinforcement learning line (Smyth and Keane) were not obtained. [gap 9]
10. Does set-level selection interact with learned value, and does it fix near-duplicate failures? No study combines them. [gap 10]
11. Whether the "format, not content" finding (random labels) holds for current frontier models. It bounds what any outcome-based value can learn. [b11]
12. Independent replication of CASCADE. [K17]

## 11. Sources

[V] = opened and read this session (full text or substantial sections); [M] = snippet or very partial.

- [V] Guo, Du, Chen, Chang, Wang (2026) CASCADE: Case-Based Continual Adaptation for LLMs During Deployment. https://arxiv.org/abs/2605.06702 (a01-a08)
- [V] Zhou et al. (2025) Memento: Fine-tuning LLM Agents without Fine-tuning LLMs. https://arxiv.org/abs/2508.16153 (a09-a11, b12-b16, c01-c04)
- [V] Zhang et al. (2026) MemRL: Self-Evolving Agents via Runtime Reinforcement Learning on Episodic Memory. https://arxiv.org/abs/2601.03192 (a12-a15, c05-c10, d05, d06)
- [V] Li, Chu, Langford, Schapire (2010) A contextual-bandit approach to personalized news article recommendation. https://arxiv.org/abs/1003.0146 (a16)
- [M] Zhou, Li, Gu (2020) Neural contextual bandits with UCB-based exploration. https://arxiv.org/abs/1911.04462 (a17; abstract and theorems)
- [M] Zhang, Zhou, Li, Gu (2021) Neural Thompson Sampling. https://arxiv.org/abs/2010.00827 (a18; abstract and opening)
- [V] Riquelme, Tucker, Snoek (2018) Deep Bayesian bandits showdown. https://arxiv.org/abs/1802.09127 (a19)
- [M] Russo et al. (2018) A tutorial on Thompson sampling. https://arxiv.org/abs/1707.02038 (a20; skimmed)
- [V] Rubin, Herzig, Berant (2022) Learning to retrieve prompts for in-context learning (EPR). https://arxiv.org/abs/2112.08633 (a21, b05, b06, c14)
- [V] Wang, Yang, Wei (2023/2024) Learning to retrieve in-context examples for LLMs (LLM-R). https://arxiv.org/abs/2307.07164 (a22, b07, b08, c15)
- [V] Zhang, Feng, Tan (2022) Active example selection for in-context learning. https://arxiv.org/abs/2211.04486 (a23, b01-b04, c13)
- [M] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (a24; first page only)
- [M] Zhao et al. (2024) ExpeL: LLM agents are experiential learners. https://arxiv.org/abs/2308.10144 (a25 methods only; results b17, b18, c19)
- [V] Ouyang et al. (2026) ReasoningBank: Scaling agent self-evolving with reasoning memory. https://arxiv.org/abs/2509.25140 (a26, b19, b20, c17, d14)
- [M] Thompson (1933); Auer, Cesa-Bianchi, Fischer (2002) DOI. https://doi.org/10.1023/A:1013689704352 (a27, b25; the 2002 paper itself was opened via the PDF below)
- [V] Aamodt and Plaza (1994) Case-based reasoning: foundational issues. https://www.iiia.csic.es/~enric/papers/AICom.pdf (d19; DOI https://doi.org/10.3233/AIC-1994-7104, a28)
- [V] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf (d11)
- [M] Liu et al. (2021) What makes good in-context examples for GPT-3 (KATE). https://arxiv.org/abs/2101.06804 (b10; table columns garbled)
- [V] Min et al. (2022) Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837 (b11)
- [M] Ye et al. (2023) Compositional exemplars for in-context learning (CEIL). https://arxiv.org/abs/2302.05698 (b09, c23; table garbled)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (b21, b22)
- [V] Yan et al. (2026) Memory-R1. https://arxiv.org/abs/2508.19828 (b23, b24, c16)
- [V] Zhang et al. (2023) Large language models are semi-parametric reinforcement learning agents (REMEMBERER). https://arxiv.org/abs/2306.07929 (c11, c12)
- [V] Fang et al. (2025) Memp: Exploring agent procedural memory. https://arxiv.org/abs/2508.06433 (c18)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c20)
- [V] Shi et al. (2024) Efficient prompt optimization through the lens of best arm identification (TRIPLE). https://arxiv.org/abs/2402.09723 (c21)
- [V] Lin et al. (2024) Use your INSTINCT. https://arxiv.org/abs/2310.02905 (c22)
- [M] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c24; abstract and intro)
- [V] Sarukkai, Xie, Fatahalian (2025) Self-generated in-context examples improve LLM agents. https://arxiv.org/abs/2505.00234 (d01-d04)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (d07-d09; some cells garbled)
- [V] Kuleshov and Precup (2014) Algorithms for the multi-armed bandit problem. https://arxiv.org/abs/1402.6028 (d10)
- [V] Chapelle and Li (2011) An empirical evaluation of Thompson sampling. https://papers.nips.cc/paper_files/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf (d12)
- [V] Garivier and Moulines (2008) On upper-confidence bound policies for non-stationary bandit problems. https://arxiv.org/abs/0805.3415 (d13)
- [V] Wei et al. (2026) Evo-Memory. https://arxiv.org/abs/2511.20857 (d15, d16; tables garbled)
- [V] Levy, Bogin, Berant (2023) Diverse demonstrations improve in-context compositional generalization. https://arxiv.org/abs/2212.06800 (d17)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d18)
- Gap notes with no data: b26, b27, c26, c27, d20.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 15 established claims: 11 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C08.09-K01** (reworded: the sources support less). Margins quoted as about 0.6 to 3 points omit MemRL +3.6 over MemP (listed in the same evidence) and Sarukkai +8 on Wordcraft; CASCADE uses Qwen3-32B and Sarukkai gpt-4o-mini, so none is a frozen frontier-class test, and "every direct head-to-head" is a claim about the researcher's own search. Corrected claim: In the head-to-head comparisons found, choosing cases by learned value beat similarity-based retrieval, with small margins online (Memento parametric vs non-parametric retriever +0.6 to +1.0 F1/accuracy points; CASCADE +2.92 over non-learned retrieval with Qwen3-32B; MemRL +3.6 over MemP); Sarukkai (5 seeds, gpt-4o-mini) finds learned exemplar curation adds about +1 (ALFWorld), +2 (SQL) and +7 to +8 (Wordcraft) over naive accumulation; no paired test with a frozen frontier-class model was found.
- **C08.09-K09** (reworded: the sources support less). Wang et al. say the LLM-R gains are substantially smaller on knowledge-intensive tasks (commonsense, reasoning, memorised facts; NQ excepted) and say it helps on Sentiment140; the claim re-labels this as small gains on reading comprehension and sentiment, which the paper does not state (sentiment is +41 over random in its table). SQuAD below random, Min et al. 1.7/2.6, and Levy 2.5 to 6.9 check out. Corrected claim: Learned retrieval has failure cases: LLM-R falls below random on SQuAD (many questions share a passage, so it retrieves near duplicates with low diversity) and its gains on knowledge-intensive tasks (commonsense, reasoning, memorised facts; NQ excepted) are much smaller than the 30-task average; random labels in demonstrations cost only 1.7 points on average for multi-choice and 2.6 for classification (Min et al.), so demonstrations mostly convey format, input distribution and label space. Gap pass: set-level coverage selection (Levy 2023) beats top-k similarity by 2.5 to 6.9 points on GeoQuery with Codex (smallest on the i.i.d. split).
- **C08.09-K14** (reworded: the sources support less). Numbers are right (Game of 24 10 to 6, MMLU-Pro Eng 53.2 to 48.8 under DR; Memp 74.59 vs 73.38), but curated memory did not gain on MMLU-Pro Eng for GPT-4o (DC-Cu 44.0, DC-RS 51.2, both below baseline 53.2); it gained only on Game of 24 (93 and 99). Corrected claim: Naive verbatim retrieval can hurt: Dynamic Cheatsheet retrieval-only (DR) dropped GPT-4o on Game of 24 (10 to 6) and MMLU-Pro Eng (53.2 to 48.8); curated memory gained on Game of 24 (93 to 99) but not on MMLU-Pro Eng, where GPT-4o fell under every variant. Memp: random sampling beat query-keyed retrieval for GPT-4o on TravelPlanner (74.59 vs 73.38).
- **C08.09-K24** (reworded: the sources support less). Chapelle and Li is not context-free: it includes contextual bandit experiments (display-ad CTR with features, LinUCB, news recommendation), so "All are stationary and context-free" is wrong; also the 10% to 100% figure is Boltzmann versus its closest competitor, not versus UCB1, and Chapelle and Li call Thompson sampling highly competitive rather than strongest. Corrected claim: Classic bandit sources do not support a UCB bonus as the default: tuned epsilon-greedy almost always did best in Auer 2002; softmax and epsilon-greedy beat UCB1 in most of 12 instances in Kuleshov and Precup 2014 (softmax beat its closest competitor by 10% to 100% in regret); Chapelle and Li 2011 found Thompson sampling beat UCB and epsilon-greedy in simulation and in contextual ad and news experiments. Auer 2002 and Kuleshov and Precup use stationary context-free bandits.
