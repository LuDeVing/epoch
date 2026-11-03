# Map versus value replay: deep document

*Subfield B05.05. Writer pass, 2026-11-03. Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b09, d03 ...) point to those files. Claim ids are B05.05-Kxx.*

## 1. What it is

Hippocampal replay is the fast re-activation of place-cell sequences during rest and pauses. The question: what does replay build?

Two answers:

- **Value replay (planning view).** Replay updates a value function for the goal the animal has now. It runs backups in order of need x gain (Mattar and Daw 2018, b13, a11). If one goal dominates, replay depicts routes to that goal.
- **Map replay (map-building view).** Replay builds a goal-general map, so that any goal can be reached later. It is prioritised by beliefs about which goals will matter in future (Sagiv, Akam, Witten and Daw 2025, b01, a10).

Sagiv et al. call the map the **Geodesic Representation (GR)**. It is a stack of Q-pages, one per candidate goal. Each page holds shortest-path values to that goal, with that goal terminal and the only reward. One replayed transition updates every page. Value replay is the special case of one goal (a01).

Why it matters for our agent: the agent holds memory (routes, sub-solutions, lessons). The map view says to keep routes for several likely future goals, not only the current one. And it says to rank what to rehearse by (how likely the goal is) x (how much the update helps). This is a memory-design rule. It does not touch the guardrails.

Scope of the evidence. The theory is a tabular simulation paper. The animal data are two small rat datasets re-read by theory. No LLM study tests the theory directly (K10). The nearest AI work is hindsight relabeling (HER, AgentHER, HSL, ECHO), which reuses a trajectory for goals other than the one pursued. All of that is training-time except ECHO.

## 2. History and theories in depth

**Roots (1990s to 2017).**
- Dayan 1993 introduced the successor representation (SR), expected discounted future occupancy, which generalises across reward functions (a23, not opened).
- Kaelbling 1993 "Learning to achieve goals": goal-conditioned shortest-path learning for many goals at once. It is the ancestor of the GR (c05, seen only as a citation).
- Russek et al. 2017 introduced Dyna-SR: the SR updated by replayed transitions. SR plus TD handles reward change but not transition (detour) change. Replay repairs part of this (a17).
- Momennejad et al. 2017: N=58 humans revalued more after a reward change (0.520, SEM 0.020) than after a transition change (0.450, SEM 0.023), t(57)=2.89, p<0.01. Both beat control (0.031) (a18).
- Andrychowicz et al. 2017 (HER): replay each episode with a goal that was actually achieved. Sparse-reward failures become successes for another goal. Sampling future states in the same episode with k=4 or 8 worked best. A simulated pick-and-place policy ran on a real Fetch robot with no fine-tuning (c06).
- Schaul et al. 2016 (Prioritized Experience Replay): replay by TD error. Beat uniform replay on 41 of 49 Atari games (c07).

**Value replay in the brain.**
- Pfeiffer and Foster 2013: before moving, sequences depict paths to a remembered goal, a Home well visited every trial (b14, a22; abstract only).
- Ambrose, Pfeiffer and Foster 2016: reverse replay rate rises with reward size (4x reward) and falls when reward is 0. Forward replay does not change (a16).
- Mattar and Daw 2018: replay priority = gain x need. Forward and reverse sequences and the reward asymmetries come out of one rule. Tabular simulations, gain by brute force (b13, a11).

**The anomalies.**
- Gillespie et al. 2021 (4 rats, 24/32/23/33 sessions): in an 8-arm task where the goal arm moves after 4-15 rewards, remote replay was 34.5-47.2% of sharp-wave ripples (SWRs). Before a choice it was enriched for the previous block's goal arm (about 20% of remote events in search trials, about 2-fold rate in a Poisson GLM). The arm just visited was under-replayed. The upcoming choice was not predicted. Content could not separate correct from error trials (a12, a13, b09, b10). The authors read it as memory maintenance (b11).
- Carey, Tanaka and van der Meer 2019 (4 rats): rats chose the outcome they were deprived of (food-restricted 89% food, water-restricted 80% water). Replay content favoured the other arm. The bias was already present in pre-task rest (a14, a15).

**The synthesis.** Sagiv et al. (bioRxiv 2024, Neuron 2025): priority = expected (need x gain) summed over a belief distribution P(g) over goals (a02). With one dominant goal, this is value replay. With goals that rotate or recur, it is map building. Replay follows a slow estimate of the goal distribution, so it can lag behaviour (a05, a06). With known alternating dynamics it leads (Pfeiffer and Foster pattern, b06, c03).

**Rival accounts.**
- Memory maintenance (Gillespie, b11).
- Representation protection (Chen and van der Meer 2024/2026): replay of non-chosen options protects task representations from interference when experience is unbalanced. r=0.53 (single-cell) and 0.49 (ensemble) between representational separation and paradoxical replay, both p<0.05. In a second dataset the ensemble r=0.32, p=0.18, not significant (b16).
- Experience-strength replay with similarity and inhibition of return (Diekmann and Cheng 2023): cheap, near Mattar-Daw quality (b17).
- Temporal-context-model replay (Zhou et al.): similar predictions, since its associations coincide with the SR (b08).
- Compositional replay (Bakermans et al. 2025): replay builds new fields when landmarks move; no goal-switching statistics (b18).
- Adaptation-based goal trapping (Mallory, Widloski and Foster 2026, 4 rats, 44 sessions): replay at a fixed rewarded goal is about 2x as frequent (Z=5.4), slower and ends at the goal (d14, K23). A pure map must also explain this.
- Barrier-aware rerouting (Widloski and Foster 2022): in 27 of 31 barrier sessions (87%) replay avoided barrier violations beyond the 95th percentile of control, with 3 rats (b15).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Replay priority is summed over a goal belief; one backup updates all goal pages | GR = one Q-page per goal; single-goal GR equals Q-learning; discount 0.95 | Sagiv 2025 (a01, a02, b01) | single-source theory |
| Value agent replays only the nearest-reward route; GR agent replays both arms in distance order | one simulated T-maze, no statistics | Sagiv 2025 (a03, b02) | single-source, qualitative |
| GR replay concentrates on bottleneck states; need = discounted betweenness; corridor interiors under-replayed | n=250 simulated sequences, two mazes | Sagiv 2025 (a04, b03) | model prediction, untested in animals |
| Goal-switching order: p11=0.5 replays g1 then g2; p11=0.05 replays g2 first | simulation only; Q agent replays only g1 | Sagiv 2025 (a07, c03) | untested prediction |
| Replay lags behaviour: previous goal arm over-replayed | 4 rats; remote replay 35.1/41.1/34.5/47.2% of SWRs; previous goal about 20% of pre-choice remote events; about 2-fold rate; 711/848/725/1065 search trials | Gillespie 2021 (b09, b10, a12) | one lab, N=4, contested reading |
| Future-arm replay is small, not absent | significant in 2 of 4 rats (subset) and 3 of 4 (GLM) | Gillespie 2021 (b09, critique) | one lab |
| Replay content cannot separate correct from error trials | cross-validated binomial GLM; 848/1308/614/780 subsampled trials | Gillespie 2021 (a13) | one lab |
| Behaviour follows deprivation, replay favours the other arm | N=4; food-restricted 89% food, water-restricted 80% water; chi2(3)=188.7; SWR food 0.28 vs water 0.72 on food days; pre-task bias chi2(3)=30.1 | Carey 2019 (a14, a15) | single-source, no independent replication |
| Sagiv model fits both datasets | qualitative; slow rate and decay set by hand; 10 blocks per goal; Carey sim 10 virtual subjects x 6 sessions | Sagiv 2025 (a05, a06, b04, b05) | contested, flexibility risk (b06) |
| Reverse replay scales with reward size | 4x reward raises, 0 reward lowers; forward unchanged | Ambrose 2016 (a16) | established |
| Replay barrier-aware rerouting | 27/31 sessions (87%), p<0.001; 3 rats | Widloski & Foster 2022 (b15) | one lab |
| Replay at fixed goal 2x frequency, slower, ends at goal | N=4, 44 sessions, 1960 vs 1939 stops; Z=5.4, p=5.7e-8 | Mallory 2026 (d14) | preprint, rival account |
| Paradoxical replay tracks representation richness | r=0.53 and 0.49 (p<0.05); second set r=0.55 and 0.32 (p=0.18) | Chen & van der Meer (b16) | preprint, correlational |
| Humans reuse paths for unpursued goals | 62.39% partial reuse (CI 53.99-69.53) vs 50% chance, p=0.0049 (n=100); 62.80% in shortcut exp; 67.1% in a third | Carvalho 2025/26 (c10) | single-source; exp 2 CI in v2 looks like a typo |
| Prioritised replay by TD error | 41 of 49 Atari games better than uniform | Schaul 2016 (c07) | established |
| HER "future" sampling | k=4 or 8 best; real Fetch robot, no fine-tuning | Andrychowicz 2017 (c06) | established |
| GPT-4 fails multi-step routes on community graphs | 0 of 30 runs at T=0 (max 10% at higher T); means: 1-step 0.99, 3-step 0.55, detour 0.55, policy revaluation 0.21 | Momennejad 2023 (a25, c11) | single-source (CogEval) |
| Hindsight relabeling in fine-tuning: HSL | ALFWorld unseen SFT 78.36 to SFT+HSL 97.76 (single run); seen 82.14 to 93.57; PlanCraft 70.00 to 75.12; WebShop 63.81 to 66.97; 1B agent | Li 2026 (b22, b23) | self-reported, one lab |
| HSL sample efficiency | 800 demos: 55.2% to 83.6%; DPO+HSL 800 demos 92.5% vs DPO >3200 demos 82.8% | Li 2026 (b23) | self-reported |
| AgentHER | +7.6 to +11.4 pp over SFT-Success (current version; v1 said 7.1-11.7); 2x data efficiency; random relabel -6.1 pp; label noise 5.9% to 2.9% with multi-judge; precision 97.1% WebArena, 96.0% ToolBench; 38.7% of filtered pairs were valid | Ding 2026 (c18, b24, b25) | single author, one lab; use current numbers |
| In-context hindsight relabeling, frozen model (ECHO) | XMiniGrid-Stateful: +80% over ReAct, +42% over next best; 34/40 (85%) imputed workflows reached the goal; PeopleJoinQA 4.6% below best | Hu 2026 (d03, d04, a26) | single-source, only in-context test |
| Sleep-time compute | about 5x less test-time compute at equal accuracy; up to +13% (GSM) and +18% (AIME); 1-2 queries per context unfavourable, 5-10 favourable; 2.5x cost cut per query when shared | Lin 2025 (d01, d02) | single-source |
| Latent learning fails in LMs without retrieval | latent items about 6% and 12% on codebook/reversal baselines; oracle retrieval helps | Lampinen 2025 (c08, c09) | single-source |
| Memory eviction | clean stream: all bounded policies within Wilson 95% CI; 75% distractors: Precision@5 unbounded 20.2 to 12.4%, FIFO 15.8 to 3.8%, value-scored 16.9 to 16.6% | Reddy 2026 (d08, d09) | single-source |
| Stacked memories conflict | fact + reflection: skip rate 77% to 20%, pass@5 58.8% to 52.9% (WikiSQL, 51 examples) | Li & Tao 2026 (d06) | single-source, small |

## 4. Mechanisms and models

### 4.1 Value replay (Mattar and Daw)
For each stored transition (s, a, r, s'):
- Gain(s,a) = expected improvement in return from updating the policy at s with one Bellman backup.
- Need(s) = discounted expected number of future visits to s from the current state (an SR row).
- EVB = Gain x Need. Replay the transition with the largest EVB. Repeat within the replay budget. After a backup, recompute (reverse sequences emerge after a reward; forward sequences emerge from need).

Learning rate 1.0, discount 0.9 in their runs (a11).

### 4.2 Map replay (Sagiv et al.)
Keep G(s,a,g) for each candidate goal g. G is the expected discounted return from taking a in s, then following the shortest-path policy to g. Goal g is terminal with unit reward. For a replayed (s,a,s'):

G(s,a,g) <- G(s,a,g) + alpha * [gamma * max_a' G(s',a',g) - G(s,a,g)], for every g (reaching g gives reward 1).

Priority of a candidate backup = sum over g of P(g) x Need_g(s) x Gain_g(s,a). Need_g uses the SR under the goal-g policy. Gain_g is the policy improvement at s for goal g, valued by the post-update G. They compute gain by brute-force enumeration (tabular) (a02, c04). Discount 0.95. Replay learning rate 0.7 in the Gillespie sim, 0.1 in the Carey sim (a05, a06).

### 4.3 Two goal trackers
Two Rescorla-Wagner estimators:
- Fast R_behav: drives choice. Tracks the current goal.
- Slow R_replay: estimates the across-block goal distribution that weights replay. Small per-step decay on the GR.

The slow tracker gives lag. Replay favours the old goal, current-goal replay rises through the block, and old-goal enrichment fades over several blocks (b04, c02). The Q-value agent does the opposite: current goal first, declining within a block.

### 4.4 When each regime wins
- Prioritisation matters only when experience or replay is limited (b08).
- Value replay wins when one goal dominates for long, the route space is large, and dynamics are known (b06, b08).
- Goal-general replay wins when goals rotate or recur, p11 is low, or the goal set is large relative to the budget.
- Predicted: bottleneck states get replayed more (need = discounted betweenness); with p11 = 0.05 the other goal is replayed first (a04, a07).

### 4.5 Engineering analogues an engineer can implement now
- **Hindsight tagging (HER/ECHO).** After each episode, list the goals the trajectory actually achieved. Store the trajectory (or a compressed workflow) under each goal. Verify each label (c18, d03).
- **Preplay (Multitask Preplay, sleep-time compute).** During idle budget, compute routes to accessible but unpursued goals. Pay only if the later reuse probability is high (c10, d02).
- **Priority queue.** Score each stored route as P(goal) x gain, where gain is the saving if the route is current and correct. Evict the lowest score.
- **Cheap approximations.** Strength x similarity x inhibition of return (Diekmann and Cheng) when exact gain is too costly (b17). Default representation (Piray and Daw) as a goal-reusable occupancy map (a19).
- **Limits stated by the authors.** The GR is off-policy, learns one goal at a time (not goal sequences), is tabular and has goals terminal. Proposed fixes: sets of SRs with generalised policy improvement, or hierarchy (c04).

## 5. What holds up

**Holds (several sources, or well-established):**
- Value-driven replay: reward size raises reverse replay (Ambrose, a16) and prioritised replay by TD error beats uniform (c07). K06, K18.
- Goal relabeling helps LLM agents: HSL, AgentHER (self-reported, fine-tuning) and, in-context, ECHO. Different labs, different methods, same direction. K08.
- Preplay of unpursued tasks pays when reuse is likely: humans (c10), deep RL (c10), sleep-time compute (d01, d02). K13.
- Boundary: gain is smaller when one goal is achievable (HSL WebShop 63.81 to 66.97 vs ALFWorld unseen 78.36 to 97.76), matching Sagiv's boundary (b23, b08). K07.
- Replay-based updating repairs transition changes that a plain SR misses (a17, a18). K17.

**Does not hold, or is contested:**
- Whether replay actually builds a goal map. The Sagiv fit is qualitative, with chosen rates and decay. Gillespie's authors favour memory maintenance, Chen and van der Meer favour representation protection, Mallory favours adaptation. No experiment separates them (critique). K03, K15.
- The model can fit both lagging and predictive replay by choosing the prior (b06). That is a flexibility risk.
- The bottleneck and goal-switching-order predictions are untested. The newest rat data (Mallory 2026) keeps the goal fixed in a session (d14, d18). K16.
- Future-arm replay in Gillespie was small but significant in 2-3 of 4 rats. So the planning signal is weak, not absent.
- Carey: no independent replication. N=4 rats and one lab. K05.
- Animal evidence is N=4 per study, one lab each.

**Negative results in LLMs:**
- Momennejad 2023: GPT-4 0 of 30 on community-graph shortest path. CoT and BFS/DFS prompts helped only marginally and unevenly (c12). K11.
- Cognitive-map chain of thought: fine-tuned 76.5% vs 19.0% optimal planning, but few-shot cognitive-map prompts gave 0-1% on Llama-3 and GPT-4o. Only GPT-o1 with plain prompts rose to 38% at 4 shots (d11). 2026 frontier models: adjacency input 80-86% vs visual grid 16-34%, and they build no cumulative map across questions (d12, abstract only). K12 contested.
- ECHO: PeopleJoinQA accuracy 4.6% below the best baseline (d03).

**Moderators:**
- Goal recurrence and predictability (sleep-time compute gain rises across 5 predictability bins; 1-2 queries per context is a loss, 5-10 a win, d01, d02).
- Test-time budget: at high budgets test-time-only compute wins (d02).
- Label noise: naive random relabeling hurt by 6.1 pp; multi-judge gating raised precision (c18).
- Number of valid goals per task: gain larger with many valid goals and long tasks (b23).
- Stream noise: eviction policy matters only with distractors (d08, d09).
- Memory type: reflection helps only under MCTS, not best-of-N; fact memory is accuracy-neutral but cuts trajectories 19-26% on tasks with reusable structure (d06).

**Interventions that worked:** hindsight relabeling with gating; preplay when reuse is likely; value-scored eviction under noise; explicit adjacency input.
**Did not work:** random relabeling; CoT or BFS prompts alone for graph routes; stacking fact + reflection memories (d06); cognitive-map prompts few-shot on 2024 models.

## 6. Language models

No LLM study tests goal-distribution-weighted replay (K10, weak absence: Semantic Scholar and OpenAlex were rate limited). What exists:

**Base map competence.**
- CogEval (Momennejad 2023), GPT-4 means: 1-step 0.99, 2-step 0.82, 3-step 0.55, n-step 0.47, detour 0.55, shortcut 0.56, policy revaluation 0.21, reward revaluation 0.67, transition revaluation 0.60. Shortest path one cluster away: 0 of 30 at T=0 (c11, a25).
- Webb et al. 2025 (Nature Communications): a prompt-only modular planner (monitor, predict, evaluate, decompose, orchestrate, tree search) solved Valuepath 100%, Steppath perfect at 2-3 steps, and Tower of Hanoi 3 disks at nearly 7x the zero-shot rate (100% best of 5). Reward revaluation only on par (d13).
- Input format matters more than reasoning: adjacency 80-86% vs visual grid 16-34% (d12).

**Hindsight relabeling.**
- Training-time: HSL (1B agent, 70B relabeler) ALFWorld unseen 78.36 to 97.76; AgentHER +7.6 to +11.4 pp over success-only SFT, +3.0 to +6.2 over AWM; SAC-GLAM with HER is more sample efficient (no scores extracted) (b22, c18, b21).
- In-context: ECHO, frozen GPT-4o, +80% over ReAct on XMiniGrid-Stateful, +42% over the next baseline; 85% of imputed workflows reached the goal; cost: PeopleJoinQA 4.6% below best (d03, d04). Recurrence fixed at 16 queries over 4 goals per environment, never varied (d05).

**Goal-agnostic stored routes.** Agent Workflow Memory +51.1% relative on WebArena; ExpeL transfer HotpotQA to FEVER 59.0 to 64.2%; HippoRAG +11 R@2 on 2Wiki; Reflexion +22% absolute on ALFWorld (c17, c20, c16, c19). None weights by future-goal likelihood (K14).

**Preplay.** Sleep-time compute: about 5x less test-time compute at equal accuracy, up to +13%/+18% when scaling sleep-time compute; 2.5x per-query cost cut when shared; 10x price weighting on test-time tokens (d01, d02). Lampinen 2025: LMs fail latent learning (using information seen but not needed) unless episodic retrieval is added (oracle retrieval helps significantly) (c08).

**Memory management.** TraceRetain on ALFWorld, gpt-5-mini: held-out transfer 47-49 of 50 with memory vs 39 of 50 without. Under 75% distractors value-scored kept Precision@5 at 16.9 to 16.6% while FIFO fell to 3.8%. No goal-drift test (d08, d09). Write cost: reflection about 3.5M policy tokens plus 0.2M supervisor vs 2.2M with no memory on WikiSQL (d07).

**What changed behaviour, and by how much.** Input format (2-5x), hindsight relabeling (+8 to +19 points at training time; +80% in-context), gating (noise 5.9% to 2.9%), precompute with predictable queries (about 5x test-time saving). Plain prompting alone did not change community-graph routing (CoT marginal).

All figures are self-reported against the authors' own baselines. HSL: 1B-parameter agent, one run for 97.76 (a second table shows variance, e.g. 96.27 +- 2.11). Numbers drift across preprint versions (AgentHER).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Tag stored routes by every goal they solve, not only the task they came from.** Memory. [E] for the general idea (HER, HSL, AgentHER, ECHO). Evidence: b22, c18, d03, c06, K08. Condition: verify each label by a code check or replay before storing (K09). This is a memory write rule and respects G2/G10 (evidence from output, not claims).
2. **Cheap default: current-goal routes first when one goal dominates; widen only when goals vary.** Memory. [E]. Evidence: b06, b08, b23, K06, K07. Matches G7 (pay for itself).
3. **Do not read lag as failure; judge rehearsal by later-task help.** Memory evaluation rule. [E] as method. Evidence: b11, K04. The bench should score reuse on later problems, not only the current one.
4. **Gate precompute by expected reuse.** Memory/G12. [E] (one study with graded data, plus humans and deep RL). Evidence: d01, d02, c10. Precompute only when several later queries are likely. One or two is a loss.
5. **Present routes in explicit adjacency/list form, not prose grids.** S2 REPRESENT. [E] in direction (d12 abstract, c11); the 2-5x size is single-source.
6. **Check a stored route table against ground truth before use.** G3/S8. [E]. Evidence: c11, a25, K11 (models hallucinate edges on community graphs). Code checks it, not the model.

### Test first

1. **Goal-probability-weighted route store** (priority = P(goal) x gain) vs recency vs current-goal-only. Memory. [S]. Evidence: a02, b01, K01, K10. No LLM test exists.
2. **Slow and fast goal trackers.** Memory/S0. [C]. Evidence: b04, a05, K03. Does a slow recurrence prior beat a fast "last goal" prior when goals switch?
3. **In-context hindsight tagging with a noise sweep.** Memory. [S]. Evidence: d03, d04, K20. Break point of label noise unknown.
4. **Preplay of nearby unpursued goals vs test-time retrieval at equal tokens.** Memory. [S]. Evidence: c10, d02, K13, K19.
5. **Hub/bottleneck route priority.** Memory. [S]. Evidence: a04, b03, K16. Untested even in animals.
6. **Eviction by P(goal) x gain x success under goal drift.** Memory. [S]. Evidence: d08-d10, K22.
7. **Goal-switching order rule** (rehearse the other goal first when p11 is low). Memory. [S]. Evidence: a07, c03.
8. **One route per goal vs route plus reflection notes.** Memory. [S]. Evidence: d06, K21.
9. **LLM-estimated P(goal) from task history.** S0/Memory. No evidence (d17).
10. **Prompt-only map-building before planning (cognitive-map CoT).** O/S2. [C]. Evidence: c13, d11, d12, d13, K12. Do not add: 2024 negative, 2026 open.

## 8. Concrete tests on our bench

Common rules: both arms get the same total token budget, counting setup, write, precompute and retrieval tokens (G7). Code selects (G5). At least 3 seeds and a Wilson 95% interval per arm. Items are multi-goal task streams with controlled goal recurrence.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Goal-weighted store | stream of 40 tasks over 6 goals, goal drawn from a Markov process, p11 in {0.05, 0.5, 0.9} | (a) current-goal-only memory; (b) recency; (c) P(goal) x gain; (d) no memory | solved fraction in last 20 tasks; tokens per solve | (c) beats (a) when p11 <= 0.5; equal or worse at p11 = 0.9 (Sagiv boundary) |
| T2 In-context hindsight tagging | ECHO-style environments, 16 queries over 4 goals | (a) tag with achieved goals, verified; (b) tag unverified; (c) tag only the target goal; (d) no memory | reward per query; reuse accuracy | (a) > (c); (b) close to (a) at low noise |
| T3 Noise sweep | T2 with 0, 10, 25, 50% wrong labels | verified vs unverified | solve rate vs noise | locates break point; verification shifts it up |
| T4 Preplay vs retrieval | tasks with 1, 3, 10 later queries per context | (a) idle-budget precompute of top-k routes; (b) retrieve at test time; (c) none | accuracy at equal total tokens | (a) wins at 5-10 queries, loses at 1-2 |
| T5 Slow vs fast goal tracker | goals switch in blocks of 10 | (a) fast only; (b) fast + slow prior; (c) uniform | tasks solved right after a switch and after switching back | (b) > (a) on switch-back |
| T6 Hub priority | community-graph routing tasks | (a) hub routes first; (b) random routes; (c) goal-specific tails | reuse rate of stored routes | (a) > (b) |
| T7 Eviction under drift | bounded store, goal set changes at step 50; variant with 75% distractor writes | LRU, LFU, FIFO, P(goal) x gain x success | Precision@5, solve rate after drift | score-based wins under drift, ties on clean stream |
| T8 P(goal) estimate | model outputs a goal distribution from its history | model estimate vs frequency counter in code | Brier score; downstream solve rate | counting in code >= model (G5); if the model wins, allow it |
| T9 One route vs stacked notes | same tasks | route only; route + reflection | solve rate, tokens | route only >= stacked |

## 9. What does not transfer, and why

- **Rat hippocampal timing and ripple physiology.** We have no sharp-wave ripples or rest periods. Only the scheduling logic transfers.
- **Tabular GR.** One Q-page per goal needs a small enumerable state space. An LLM agent's states are open text. Authors say the GR is tabular, gain is brute force and goals are terminal (c04, a08). Use route tables over named goals, not a Q-table.
- **Qualitative fit as proof.** The Sagiv fit uses chosen rates and a flexible prior, so it is no quantitative guide (b04, b06).
- **Training-time hindsight gains.** HSL, AgentHER and SAC-GLAM change weights. Fine-tuning gains (+8 to +19 points) do not predict gains from a prompt-only store. Only ECHO is in-context.
- **Self-reported numbers on small models.** The HSL agent is 1B parameters. Gains may shrink on frontier models.
- **Cognitive-map CoT.** The 76.5% result needs fine-tuning. Few-shot prompts gave 0-1% on 2024 models (d11).
- **Deprivation effects (Carey).** No analogue for a language-model agent.
- **Goal trapping (Mallory).** Local adaptation at the current goal is a neural mechanism with no direct scaffold twin. The lesson is only: keep current-goal routes too (K23).
- **Stable single-goal tasks.** One dominant goal means value replay is enough. A map adds cost without gain (b23, WebShop).

## 10. Open questions

1. Does any LLM-agent study weight stored routes by P(future goal) and measure it at equal tokens? None found.
2. How much label noise breaks in-context hindsight tagging? No sweep exists.
3. Which task statistics (goal recurrence, switching rate p11, number of goals) flip the advantage between map memory and current-goal memory for an LLM? Only sleep-time compute gives graded evidence.
4. Can an LLM estimate P(future goal) from its own task history? Does slow vs fast updating matter? No calibration study.
5. Token cost of preplay vs retrieval at equal total tokens. No clean test.
6. Do the bottleneck and goal-switching-order predictions hold in rodent or human data? The newest rat data cannot test them.
7. Which rival account is right (map, maintenance, representation protection, adaptation)? A separating experiment: switch the rewarded arm at a known rate and read replay order (d18).
8. Does cognitive-map CoT survive without fine-tuning on 2026 frontier models? d12 says input format dominates.
9. Are HSL and AgentHER independently replicated, and do they hold at large model scale? No independent result found.
10. How should a bounded memory evict routes when goals drift? No test.

## 11. Sources

[V] = opened and read this session. [M] = snippet or abstract only.

- [V] Sagiv, Akam, Witten, Daw (2025) Between planning and map building, Neuron. https://pmc.ncbi.nlm.nih.gov/articles/PMC12633763/
- [V] Sagiv et al. (2024 preprint, updated 2025) bioRxiv. https://www.biorxiv.org/content/10.1101/2024.02.29.582822
- [V] Mattar and Daw (2018) Prioritized memory access explains planning and hippocampal replay. https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620/
- [V] Gillespie et al. (2021) Hippocampal replay reflects specific past experiences rather than a plan for subsequent choice. https://pmc.ncbi.nlm.nih.gov/articles/PMC8497431/
- [V] Carey, Tanaka, van der Meer (2019) Reward revaluation biases hippocampal replay content away from the preferred outcome (bioRxiv preprint; final version [M]). https://www.biorxiv.org/content/10.1101/397950
- [M] Pfeiffer and Foster (2013) Hippocampal place-cell sequences depict future paths to remembered goals. https://pmc.ncbi.nlm.nih.gov/articles/PMC3990408/
- [V] Ambrose, Pfeiffer, Foster (2016) Reverse replay of hippocampal place cells is uniquely modulated by changing reward. https://pmc.ncbi.nlm.nih.gov/articles/PMC6013068/
- [V] Widloski and Foster (2022) Flexible rerouting of hippocampal replay sequences around changing barriers. https://pmc.ncbi.nlm.nih.gov/articles/PMC9473153/
- [V] Mallory, Widloski, Foster (2026 preprint) Spatial goals trap hippocampal replay (results read in d14). https://doi.org/10.64898/2026.09.02.748857
- [V] Chen and van der Meer (2024, dated 2026) Paradoxical replay can protect contextual task representations. https://www.biorxiv.org/content/10.1101/2024.05.09.593332
- [V] Diekmann and Cheng (2023) A model of hippocampal replay driven by experience and environmental structure. https://pmc.ncbi.nlm.nih.gov/articles/PMC10076035/
- [V] Bakermans et al. (2025) Constructing future behavior in the hippocampal formation. https://pmc.ncbi.nlm.nih.gov/articles/PMC12081289/
- [V] Exploring replay (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11829958/
- [V] Spatial learning drives rapid goal representation in hippocampal ripples (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9097771/
- [V] Russek et al. (2017) Predictive representations can link model-based RL to model-free mechanisms. https://pmc.ncbi.nlm.nih.gov/articles/PMC5628940/
- [V] Momennejad et al. (2017) The successor representation in human reinforcement learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC6941356/
- [V] Piray and Daw (2021) Linear reinforcement learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC8368103/
- [M] Dayan (1993) Successor representation. https://doi.org/10.1162/neco.1993.5.4.613
- [M] Kaelbling (1993) Learning to achieve goals (cited in Sagiv; not read).
- [V] Andrychowicz et al. (2017) Hindsight Experience Replay. https://arxiv.org/pdf/1707.01495
- [V] Schaul et al. (2016) Prioritized Experience Replay. https://arxiv.org/pdf/1511.05952
- [V] Carvalho, Hall-McMaster, Lee, Gershman (2025/26) Multitask Preplay. https://arxiv.org/pdf/2507.05561
- [V] Lampinen et al. (2025) Latent learning: episodic memory complements parametric learning. https://arxiv.org/pdf/2509.16189
- [V] Momennejad et al. (2023) Evaluating cognitive maps and planning in LLMs (CogEval). https://arxiv.org/abs/2309.15129
- [V] Kim, Lee, Park, Seo (2024) How language models extrapolate outside the training data. https://arxiv.org/abs/2406.15275
- [M] Li, Zhu, Das, Dube (2026) Do LLMs build spatial world models? https://www.iclr.cc/virtual/2026/10018071
- [V] Webb et al. (2025) Improving planning with LLMs (MAP). https://arxiv.org/abs/2310.00194
- [V] Li et al. (2026) Spinning Straw into Gold (HSL), ICLR 2026. https://www.alphaxiv.org/abs/2607.04235 and https://iclr.cc/virtual/2026/poster/10009594
- [V] Ding (2026) AgentHER. https://arxiv.org/abs/2603.21357
- [V] Hu, Van Durme, Andreas, Jhamtani (2026) ECHO. https://arxiv.org/abs/2510.10304
- [V] Carta et al. (2024) SAC-GLAM. https://arxiv.org/html/2410.12481v3
- [M] Hindsight Planner (2024). https://arxiv.org/html/2412.19562v1
- [V] Lin, Snell, Packer et al. (2025) Sleep-time Compute. https://arxiv.org/abs/2504.13171
- [V] Li and Tao (2026) When does memory help multi-trajectory inference. https://arxiv.org/abs/2605.28224
- [V] Reddy (2026) TraceRetain. https://arxiv.org/abs/2606.29178
- [V] Bamidele (2026) AMV-L. https://arxiv.org/abs/2603.04443
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/pdf/2409.07429
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/pdf/2308.10144
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/pdf/2303.11366
- [V] Gutierrez et al. (2024) HippoRAG. https://arxiv.org/pdf/2405.14831
- [V] Whittington et al. (2022) Relating transformers to models of hippocampus. https://arxiv.org/pdf/2112.04035
- [V] Dzhivelikian and Panov (2025) Biologically interpretable cognitive architecture. https://arxiv.org/pdf/2510.03286
- [V] Yu et al. (2025) Dyna-Think. https://arxiv.org/pdf/2506.00320
- [V] Yu et al. (2025) Dyna-Mind. https://arxiv.org/pdf/2510.09577
- [V] Holt et al. (2026) Fact-augmented lookahead planning. https://arxiv.org/pdf/2506.09171
- [M] Stower et al. (2025) Multi-modal cognitive maps (c25). https://cris.fau.de/publications/336725841
- [M] Momennejad group MAP note (c26). https://latent.space/wiki/ida-momennejad/

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 8 established claims: 3 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B05.05-K07** (reworded: the sources support less). Sagiv et al. says prioritized replay matters in data/compute-limited regimes and reduces to the value model when one goal predominates, but does not say goal-general replay pays off 'only' then; the HSL numbers (WebShop 63.81->66.97, ALFWorld unseen 78.36->97.76) are right, but the single-goal explanation is that paper's hedged 'likely', and the 'same boundary' analogy is the notes' own inference from one preprint. Corrected claim: Goal-general replay is most useful when experience or replay is limited and goals recur or switch (Sagiv et al.). A hindsight-relabeling LLM paper (HSL) is loosely consistent: its WebShop gain is smaller (63.81 to 66.97), which the authors say is 'likely' because WebShop allows only one achievable goal per trajectory, vs ALFWorld unseen 78.36 to 97.76.
- **B05.05-K08** (reworded: the sources support less). Numbers verified (HSL 78.36->97.76 Llama-3.2-1B; AgentHER current abstract +7.6-11.4, v1 +7.1-11.7; ECHO up to 80% over ReAct in XMiniGrid avg reward, 34/40=85%), but 'All are training-time' contradicts the next sentence: ECHO is prompt-only with no weight updates. Corrected claim: Hindsight relabeling for LLM agents (HSL, AgentHER, ECHO, SAC-GLAM) reuses a trajectory as a demonstration for other achieved goals: HSL ALFWorld unseen 78.36 to 97.76 (SFT vs SFT+HSL, 1B agent), AgentHER +7.6 to +11.4 pp over SFT-Success (current version; v1 said 7.1-11.7), ECHO up to 80% over a ReAct baseline in average reward. HSL, AgentHER and SAC-GLAM are training-time; ECHO is in-context (prompt-only, no weight updates) and 34 of 40 imputed workflows (85%) reached their goal. All are self-reported; no independent replication of HSL or AgentHER was found.
- **B05.05-K13** (reworded: the sources support less). Preplay numbers (62.39%, CI 53.99-69.53, p=0.0049; 62.80%) and Lampinen oracle-retrieval match; but the sleep-time ~5x saving is for a single query per context, and only the extra amortised 2.5x (t=10, cost-weighted) needs several queries sharing the context. Corrected claim: Preplay of unpursued but accessible tasks is reflected in human behaviour (partial path reuse 62.39%, CI 53.99-69.53, vs 50% chance, p=0.0049; 62.80% in the shortcut experiment) and beats baselines in deep RL; latent learning fails in parametric systems without episodic retrieval (oracle retrieval helps). Sleep-time compute: about 5x less test-time compute at equal accuracy for a single query per context, a further average cost cut up to 2.5x when about 10 queries share the context, and the gain is larger when the query is more predictable from the context.
- **B05.05-K14** (number corrected). ExpeL HotpotQA->FEVER transfer is ReAct 63 -> ExpeL Transfer 70 (Act 58); the 59.0 -> 64.2 figures are ExpeL+Reflexion on ALFWorld (R0 vs R3). AWM +51.1% relative and HippoRAG +11 R@2 on 2Wiki (59.2->70.7) are right; the 'none weights by future goal likelihood' part is an unverifiable absence claim. Corrected claim: Goal-agnostic stored routes and workflows help LLM agents (Agent Workflow Memory +51.1% relative on WebArena; ExpeL transfer HotpotQA to FEVER 63 to 70% over ReAct; HippoRAG +11 R@2 on 2Wiki) but none found weights memories by likelihood of future goals.
- **B05.05-K17** (reworded: the sources support less). Russek et al.: SR-Dyna solves the detour task only with enough offline replay (else it degrades to SR-TD); Momennejad et al. bioRxiv Exp 1 N=58 and reward > transition revaluation (t(57)=2.89), but the means 0.52 and 0.45 appear nowhere in the text/legends (possibly only in Fig 4A), so they could not be confirmed; Piray & Daw not opened. Corrected claim: Replay-based updating can repair transition (detour) changes that plain successor representations miss, provided enough offline replay (Russek et al. 2017); humans revalue more after a reward change than after a transition change (Momennejad et al. 2017, N=58, t(57)=2.89, p<0.01).
