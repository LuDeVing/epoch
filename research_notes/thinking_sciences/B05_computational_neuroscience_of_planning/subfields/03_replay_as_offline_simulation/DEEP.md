# Replay as offline simulation (Dyna family): deep document

*Subfield B05.03. Built from evidence_a-d.jsonl (ids a01-a27, b01-b29, c01-c30, d01-d20), claims.jsonl (K01-K27) and critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. Where the critique corrected an evidence line, the corrected figure is used here.*

## 1. What it is

Dyna is a way to learn from experience twice. The agent acts in the world and updates its values from what happened. Between real steps it also "replays": it draws a remembered or modelled transition, pretends it just happened, and runs the same update. Real and simulated experience go through one learning rule (Sutton and Barto, a01).

Why it matters in three fields:
- **Reinforcement learning (RL).** Offline planning steps make a new fact spread through the value table fast, without more real trials. Prioritised sweeping and prioritised replay decide which replays to run first.
- **Neuroscience.** Hippocampal "replay" (sequences of place-cell firing during rest) looks like Dyna's planning step. Human rest-period brain data link replay to later replanning. The strongest theory, Mattar and Daw 2018 (a13), says the brain replays in order of expected value.
- **Language-model agents.** The same pattern appears as: reflect on past runs (Reflexion), induce reusable workflows from solved tasks (Agent Workflow Memory), reason about a context before the question arrives (sleep-time compute), or simulate next states before acting (WebDreamer, Dyna-Think).

Our link: the schema's S9 LOOK BACK writes one lesson line per solved item. A Dyna-style offline pass between tasks would re-process stored traces to update the subgoal library: re-derive, relabel, abstract, prune, re-test. This document asks what the evidence says about doing that well, and whether it beats spending the same tokens on a fresh attempt. The honest answer is that the second question has not been tested in any study we read (K27).

Out of scope here, covered elsewhere: Mattar and Daw's full model and rodent replay (subfield 04, prioritised memory access), replay and wake-sleep learning in AI, hierarchical options, test-time compute scaling, retention policy. Links are noted where they overlap.

## 2. History and theories in depth

**1990-1991. Sutton's Dyna.** Sutton proposed an architecture that integrates learning, planning and reacting. The agent learns a model of the world from real steps. Between steps it runs n planning updates on model-generated transitions. Learning and planning use exactly the same algorithm. Sutton's original papers (a19, d20) were only reachable as image PDFs or snippets here, so the early numbers come from the 2018 textbook (a01) and Moore and Atkeson.

**1993. Prioritised sweeping.** Moore and Atkeson (a03, d13) and Peng and Williams (1993) noted that uniform replay wastes backups. Keep a priority queue of states. When a state's value changes a lot, push its predecessors on the queue ordered by the size of the change. A fixed backup budget then goes where it matters. This is the first prioritised replay.

**Dyna-Q+.** Sutton and Barto (a02) added an exploration bonus. In the Blocking Maze (environment changes at step 1000) and Shortcut Maze (changes at step 3000), plain Dyna-Q cannot find a new shortcut. Its model says no shortcut exists, and it never retries. Dyna-Q+ gives each state-action a bonus that grows with time since last tried, so planning drifts toward stale parts of the model. This is the origin of the "stale model" problem we care about for subgoal libraries.

**2013-2017. Variants.** Small backups (van Seijen and Sutton, c25) make each update cost independent of successor count. Prioritised experience replay in deep RL (Schaul 2016, a23/c21) ranks stored transitions by temporal-difference (TD) error. Hindsight replay (c22) relabels failed episodes with the goal actually reached, so a failure becomes a success for another goal. Replay-buffer studies (Zhang and Sutton c23, Fedus c24) show bigger buffers are not always better.

**2006-2019. Replay enters the lab.** Foster and Wilson 2006 (a18, snippet only) found reverse replay in rats. Karlsson and Frank 2009 (a14) found awake replay of remote places. Gershman, Markman and Otto 2014 (a17, snippet only) showed people revalue retrospectively. Momennejad et al. 2017 (a07, a08) ran the revaluation tasks that separate model-based from successor-representation (SR) learners. Momennejad et al. 2018 (a11) linked rest-period replay to replanning in fMRI. Liu et al. 2019 (a15) found MEG replay that follows learned structure, not seen order. Vikbladh et al. 2019 (a16) showed hippocampal damage impairs model-based planning.

**2017. SR-Dyna.** Russek, Momennejad, Botvinick, Gershman and Daw (a04-a06, b01-b03) proposed that the brain learns a successor representation M (expected discounted future state visits) and uses Dyna-style replay to update it. Three algorithms are compared by simulation: SR-TD (no replay), SR-MB (recompute M from a model), SR-Dyna (replay updates M). Their key prediction: with too little replay, Dyna-Q becomes model-free and fails everything, while SR-Dyna degrades to SR-TD and still passes reward revaluation.

**2018. Prioritised memory access.** Mattar and Daw (a13): each replay backup has Expected Value of Backup, EVB = Gain x Need. Greedy EVB ordering reproduces reverse replay after a surprise, forward replay before a choice, and many rodent findings. See subfield 04.

**2020. Momennejad's review** (a10, b06, a27) ties SR, replay and generalisation together, and is the source of the label "SR-Dyna fits human revaluation best". Critique item 4: the 2017 human paper never fitted SR-Dyna. It fitted pure model-based, pure SR and a hybrid. The label is the review's reading plus simulations. Status [C].

**2021-2025. Rethinking what replay is for.** Gillespie et al. (b11) found rat replay favoured previous goals and long-unvisited arms and did not predict the next choice. This supports memory maintenance, not only planning. Sagiv et al. 2025 (d16, abstract only) extend EVB to uncertain goals. Antonov and Dayan 2025 (d17, abstract only) treat replay as exploration.

**2023-2026. Dyna in language-model agents.** Four lines:
1. Offline thinking before the query (sleep-time compute, c01).
2. Learn workflows and playbooks from past traces (AWM c13, ACE d06, ReMe d05, Memento d12).
3. Simulate outcomes before acting (WebDreamer c08, Dyna-Mind b17-b20, Dyna-Think a24).
4. Synthetic experience for training (DreamGym c11, d09).
Most of the "Dyna" label is borrowed. Only Dyna-Think and Dyna-Mind use the name, and both train weights.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| More planning steps per real step speed learning in a tiny maze | 47-state Dyna maze: n=0 needs about 25 episodes to near-optimal; n=5 about 5; n=50 about 3. First episode about 1700 steps for all n | Sutton and Barto, a01 | [E] (K01) |
| Prioritised sweeping needs fewer observations than Dyna variants | Stochastic 2627-state maze, observations to 98% optimal: Dyna-PI+ 240,000; optimistic Dyna 155,000; prioritised sweeping 94,000. 4528 states: 525,000 / 310,000 / 200,000 | Moore and Atkeson, a03, d13 | [E] (K03) |
| Large-state gain with a backup budget | 14,400-state rod-in-maze, 100 backups per observation: Q and Dyna-PI+ never converged; optimistic Dyna 55,000; prioritised sweeping 14,000. At 300 backups on the 4528-state maze: 143,000 obs (3 h) vs 21,000 | a03, d13 | [E] |
| Exceptions on small mazes | 15-state stochastic: 600 vs 400 observations; one small problem Dyna-PI+ 252 vs prioritised sweeping 472 | d13 | [E] boundary |
| Prioritised replay beats uniform in deep RL | Better on 41 of 49 Atari games | Schaul 2016, a23, c21 | [E] |
| Plain Dyna-Q misses new shortcuts | Blocking Maze change at step 1000; Shortcut Maze at step 3000; Dyna-Q+ recovers, Dyna-Q does not | a02, a26 | [S] (K02, all trace to one book) |
| Humans revalue more after reward change than transition change | Exp1 n=58: reward .520 (SEM .020), transition .450 (.023), control .031 (.031). Reward>transition t(57)=2.89 p<.01; reward>control t(57)=10.14; transition>control t(57)=9.05 | Momennejad 2017, a07 | [S] (K04) |
| Same pattern in an active task | Exp2 n=88, switch rates: reward .659, transition .466, policy .500, control .080. Reward vs transition Z=-2.85 p=.0034; transition vs policy Z=.56 p=.58 | a08, b05 | [S] (K04) |
| Too little replay: Dyna-Q fails all, SR-Dyna passes reward revaluation | Simulation, k=10 vs k=10000 replay samples. Both pass all tasks at k=10000 | Russek 2017, a04, a05 | [S] simulation only (K06) |
| Rest replay predicts replanning (fMRI) | n=24. Replanning in revaluation t(23)=4.89 p<.0001; control t(23)=-0.10. Replay-replanning Spearman rho=.54 (p=.0068) vs -.13 (p=.55); difference p=.023 | Momennejad 2018, a11 | [C] (K07) |
| "Stronger under reward noise" claim | Interaction p=.34; not supported | b09, critique item 5 | Not supported |
| Independent lab: no rest benefit | n=119+119, ages 7-23, adapted task. Reward revaluation drives replanning with and without 60 s rest. Rest effect -0.02 [-0.06, 0.01], p=.13 | Zhang et al. 2026, d14 | [C] |
| Human replay follows structure, not order | MEG n=21 and n=22. Rule quiz 94.4% (study 1), 73.1% (study 2) vs 50% chance. Structure code leads object code t(20)=6.47 | Liu 2019, a15 | [S] (K08) |
| Remote replay in rats | 3 rats. Remote events 5/22, 149/346, 102/212. Awake 44.1% vs quiescent 35.7% of 1046 candidates, Z=3.36 | Karlsson and Frank, a14 | [E] with b11 (K09) |
| Replay did not predict next choice | 4 rats; replay favoured previous goal and unvisited arms | Gillespie 2021, b11 | [E] with a14 (K09) |
| Hippocampal lesions impair model-based planning | 19 patients vs 19 controls; 54-63% of hippocampus resected | Vikbladh 2019, a16 | [S] (K10) |
| Humans mix SR and model-based | n=100: beta_MB .88, beta_SR .866, beta_TD .369. SR weight .604 after congruent vs .336 after incongruent changes, p<.006; 93 of 100 in predicted direction | Kahn and Daw 2025, d15 | [C] for the SR-Dyna label (K05) |
| Policy reuse via successor features + GPI | N=132, 96, 113, 303; SF&GPI preferred in 3 of 4; Exp1 no difference. About 40% excluded | Tomov 2021, b13 | [S] (K21) |
| One-step Dyna gives little over extra real updates in Atari | Six games, DQN vs Dyna-DQN at matched updates. Per-game scores not extracted | Holland 2018, a21 | [E] with a20, a22 (K11) |
| Short branched rollouts are safer than long ones | Matches asymptote of best model-free methods with fewer samples | Janner 2019, a22 | [E] (K11) |
| Offline reasoning before the question | About 5x less test-time compute at equal accuracy; up to +13% (Stateful GSM) and +18% (Stateful AIME); cost per query 2.5x lower in multi-query | Lin 2025, c01, c02 | [S] (K12) |
| Sleep-time reversal at high budgets | Claude 3.7 Sonnet, SWE feature task: sleep-time wins on file-set F1 at low test budgets (about 3,000-10,000 tokens); plain test-time wins at high budget (sleep-time agent had lower precision) | c04 | [S] |
| Simulating next states helps a web agent | GPT-4o VisualWebArena 17.6 reactive to 23.6 WebDreamer (+34.1% rel); tree search 26.2; wall clock 180-234 s vs 749-972 s tree search | Gu 2024, c08, c09 | [E] (K13) |
| Prompted rollouts help untrained models | Qwen2.5-7B Sokoban 25.8 to 30.0, ALFWorld 35.4 to 39.1. GPT-4o ALFWorld 51.3 to 64.8. GPT-4.1 ALFWorld 54.4 to 67.9 | Dyna-Mind, b19 | [E] with c08 (K13) |
| Simulation quality tracks success | ALFWorld sim score 0.18/0.35/0.36/1.00 with success 35.4/55.2/62.5/87.7. Sokoban 0.21/0.54/0.93 with 25.8/57.0/96.6. Dyna-Think r >= 0.32 | d08, c07, b20 | [E] (K14, K26) |
| GPT-4 as text-world simulator | At most 59.9% accurate on non-trivial state changes | Wang 2024, c10 | [E] (K14) |
| Separate Dyna world model does not reliably help | OSWorld vanilla Dyna 23.2 vs RFT 23.2 (no gain; the 24.1 figure in b22 is the DDT row). WindowsAgentArena 20.9 vs 28.4. In-thread DDT 26.6 and 34.9 | Dyna-Think, c06 (corrected) | [S] (K15) |
| Dyna-GRPO beats GRPO | Sokoban 77.1 vs 73.1; ALFWorld 90.8 vs 87.0; AndroidWorld 31.8 vs 27.8 | Dyna-Mind, b17 | [S]; trained model |
| Synthetic experience partly replaces real | Table 1 (WebShop/ALFWorld/WebArena; Llama-3.2-3B/Llama-3.1-8B/Qwen-2.5-7B): GRPO 80K real vs DreamGym 0 real: ALFWorld 65.3/70.9/79.8 vs 62.1/66.3/71.0; WebArena 7.3/6.1/6.1 vs 13.3/9.1/12.7 | DreamGym, d09 | [S] (K16) |
| Offline workflow induction | WebArena 35.5 vs 23.5 (+12.0 points, +51.1% rel) | AWM, c13 | [S] (K17) |
| Offline vs online workflows under train-test gap | Mind2Web Step SR: in-task 45.1 vs 43.6; cross-website 33.7 vs 33.9; cross-domain 32.6 vs 35.5. Whole-task SR 0.7-4.8% | AWM, d11 | [S] (K25) |
| Offline replay of traces into playbook | AppWorld, DeepSeek-V3.1: ReAct 42.4; ACE without multi-epoch 56.8; full 59.4 (+17.0). Five epochs add about +2.6 | ACE, d06 | [S] |
| Full rewrite collapses memory | 18,282 tokens at accuracy 66.7 fell to 122 tokens and 57.1 (baseline 63.7) | ACE, d06 | [S] |
| Add-all hurts, gated add helps | GPT-4o-mini, 4 agents. Fixed / add-all / strict: RegAgent 67.5/55.5/71.0; EHRAgent 16.8/13.1/38.5; AgentDriver 40.1/32.3/51.0; CIC-IoT 71.5/59.9/85.4 | Xiong 2025, d01 | [E] with d05, d06 (K22) |
| Retrieval depth limit | More than about 5 retrieved entries stops helping, then hurts | ReMe, d05 | [S] |
| Recency equals scored retention on clean library | ALFWorld FIFO-K50 190/200 vs 190/200; with 75% distractors Precision@5 3.8% FIFO vs 16.6% scored | TraceRetain, d04 | [S] (K23) |
| Corrupted updates, dose-response | FiNER: base 70.7; harmful update every step 66.7; every 5 steps 76.1; none 78.3 | ACE, d07 | [S] (K24) |
| Frontier LLM cognitive maps | GPT-4 CogEval: 1-step .99, 3-step .55, transition revaluation .60, detour .55, shortcut .56; detour coefficient -2.35 | Momennejad 2023, c15 | [S] (K19) |

## 4. Mechanisms and models

### 4.1 Tabular Dyna-Q
```
loop:
  s = current state; a = epsilon-greedy(Q, s)
  take a, observe r, s'
  Q[s,a] += alpha * (r + gamma * max_a' Q[s',a'] - Q[s,a])      # direct learning
  Model[s,a] = (r, s')                                             # deterministic model
  repeat n times:                                                  # planning
      pick a previously seen (s_p, a_p) at random
      (r_p, s_p') = Model[s_p, a_p]
      Q[s_p,a_p] += alpha * (r_p + gamma * max Q[s_p',:] - Q[s_p,a_p])
```
Maze settings in a01: gamma 0.95, alpha 0.1, epsilon 0.1. The n knob trades compute for sample efficiency. Gain is largest in the first few episodes after a new fact.

### 4.2 Dyna-Q+
During planning, use reward r + kappa * sqrt(tau), where tau is the time since (s,a) was last tried in real experience. Also allow planning over never-tried actions, modelled as returning to the same state. Effect: the planner "wants" to re-test old parts of the model, so it can find a shortcut. Cost: some wasted real steps after every change.

### 4.3 Prioritised sweeping
```
after each real step (s,a,r,s'):
    update Model; P = |r + gamma*max Q[s',:] - Q[s,a]|
    if P > theta: queue.push((s,a), P)
repeat n times while queue not empty:
    (s,a) = queue.pop_max()
    do the backup for (s,a)
    for each predecessor (s_bar,a_bar) known to lead to s:
        P = |r_bar + gamma*max Q[s,:] - Q[s_bar,a_bar]|
        if P > theta: queue.push((s_bar,a_bar), P)
```
The queue sends a surprise backwards along known paths. This matches reverse replay after a surprise. Moore and Atkeson's gain was biggest when states were many and backups few (a03, d13). On tiny mazes it can lose (d13).

### 4.4 Expected value of backup (Mattar and Daw, a13)
EVB(s,a) = Gain(s,a) x Need(s). Gain is how much the policy would improve at s if this backup ran. Need is the discounted expected number of future visits to s from the current state. Backups with zero gain or zero need have zero value. Greedy EVB gives reverse replay after a reward and forward replay before a choice. Exact for deterministic MDPs; grid-world simulation only. Full treatment in subfield 04.

### 4.5 Successor representation and SR-Dyna
SR matrix M[s,s'] = expected discounted future occupancy of s' starting from s. Value V(s) = sum over s' of M[s,s'] * R(s'). Three learners (a04, b01):
- **SR-TD.** Update row M[s,:] by TD after each step. No planning. After a reward change only R changes, so V updates at once. Passes reward revaluation and latent learning. Fails transition and policy revaluation (M is stale).
- **SR-MB.** Recompute M from a learned one-step model T by M = (I - gamma T)^-1. Solves transition revaluation but costs a matrix inverse.
- **SR-Dyna.** After each step, draw 10 one-step samples with recency-weighted probability and do a TD update on M with each. After a change, replay k samples (k=10 insufficient; k=10000 sufficient).
Failure modes (b02, b07): TD-learned SR drifts when rewards are non-uniform or visits uneven; a short-horizon SR (gamma 0.1) misses distant relations. SR-Dyna cannot handle hidden state (b03).

### 4.6 Why the SR matters for an engineer
Cached summaries (SR rows) survive a low replay budget for reward changes. Full re-derivation (Dyna-Q) does not. The analogy for a text library: a short cached "what leads to what" summary per subgoal tolerates few offline passes. A library of full traces needs many. This is analogy only (K06).

### 4.7 LLM-side mechanisms
- **Sleep-time compute (c01).** Phase 1, no question: the model reads the context and writes inferred facts, likely sub-questions and lemmas into a richer context c'. Phase 2: answer using c' with a small budget. Works when questions are predictable from the context (c03). Cost is shared across several questions (c02).
- **WebDreamer (c08).** For each candidate action, the model writes the predicted next page state in words; a scorer rates them; the best action is taken. 4-5x faster than real tree search.
- **Dyna-Think / Dyna-Mind (a24, b17).** Train the model to produce next-state predictions or critiques inside its reasoning. Needs weights. The prompted version (SimRollout, b19) needs no training.
- **Workflow and playbook induction (c13, d06).** An LLM turns solved trajectories into reusable routines (AWM) or delta-updates a structured playbook (ACE). Delta updates avoid collapse. Retrieve at most about 5 entries (d05).
- **Write gate (d01).** Admit a new entry only if an evaluator confirms the outcome. A strict evaluator beat add-all on all four agents.

## 5. What holds up

**Replications and internal consistency.**
- Offline planning speeds learning: textbook result, confirmed by prioritised sweeping tables and by deep-RL prioritised replay (41/49 Atari). Strong [E].
- Prioritised beats uniform: three sources (K03). Boundary: small state spaces and ample backups (exceptions in d13). The best ordering rule differs by task.
- Replay is not only for planning: two rat studies (K09).
- Write gating: three LLM memory studies agree (K22).
- Simulating before acting: WebDreamer and Dyna-Mind prompted rollouts agree in direction (K13). Different tasks, different models.

**Failures and nulls.**
- One-step Dyna in Atari adds little over extra real-data updates (a21). A learned model can mislead values (hallucinated value, a20).
- LLM agent with a separate world model: no gain on OSWorld (23.2 vs 23.2) and a loss on WindowsAgentArena (20.9 vs 28.4) (c06).
- Independent rest-benefit test (Zhang 2026, d14): p=.13, wrong direction.
- Noise moderator of the fMRI replay-replanning link: p=.34 (b09).
- Sleep-time: with few queries per context it is not worth it (c02). At high test-time budgets plain compute wins on SWE feature localisation (c04). o1 showed limited gains (c01).
- ACE: full-context rewrite collapses memory (d06).
- Retrieving more than about 5 entries hurts (d05).
- Large replay buffers can hurt (c23).

**Moderators that were measured.**
- Predictability of the question from the context (sleep-time, c03).
- Number of queries sharing the offline pass (c02).
- Train-test gap: offline workflows trail online by 0.2-2.9 Step SR points as the gap grows (d11).
- Evaluator quality for writes and deletes (d01, d02).
- Corruption rate: below 1 in 5 tolerated; every step harmful (d07).
- State-space size vs backup budget for prioritisation (a03).
- Simulator accuracy: success rises with it across models (d08), but no fixed-model sweep exists (K26).

**What did not hold or is unverified.**
- "SR-Dyna fits human revaluation best" [C] (K05).
- Replay gain under high reward variance: not supported.
- No independent replication of the n=58 / n=88 asymmetry, or of the fMRI correlation (n=24).
- Sleep-time and AWM have no replication by another group (d10, d11).
- Most human and rodent numbers come from n=3 to 88 and a single lab each. Momennejad 2017 and 2018 share an author group.
- Russek 2017 results are simulations in small grid worlds.

**Interventions that worked (LLM).**
- Strict outcome check on writes: +3 to +22 points vs a fixed memory (d01).
- Delta updates of a playbook: ACE +17.0 on AppWorld (d06).
- Keypoint memory over raw trajectories: +4.17 vs +2.67 over no memory on BFCL-V3 (d05).
- Prompted lookahead: +3 to +14 points on ALFWorld/Sokoban (b19), +6.0 points on VWA for GPT-4o (c08).

**Interventions that did not.**
- Add-all of self-generated experience: 3.7 to 12.1 points worse than fixed memory (d01).
- Learned case selection over similarity: under 1 point (Memento 85.44 vs 84.85, d12).
- Recency vs learned scoring on a clean library: tie (d04).
- Extra epochs over the same traces: about +2.6, but tokens are not matched (d06).

## 6. Language models

**Cognitive-map and revaluation tasks.** CogEval (c15, c16): GPT-4 scores .99 on 1-step planning but .55 on 3-step, .60 on transition revaluation, .55 on detour, .56 on shortcut. Chain-of-thought and BFS/DFS prompts helped little. No replay step was added. No study ran human-style reward-vs-transition revaluation with an added offline replay pass on an LLM (K27).

**World-model quality.** GPT-4 as a text-world simulator is at most 59.9% accurate on non-trivial state changes (c10). Across models in Dyna-Mind, ALFWorld success climbs from 35.4 at sim score 0.18 to 87.7 at exact simulation; Sokoban from 25.8 at 0.21 to 96.6 at 0.93 (d08). Dyna-Think reports r >= 0.32 between world-model accuracy and task success (c07). RL training lowered the correlation (r up to .96 for R1 on Sokoban before RL, b20). Cause and effect are not separated: stronger models both simulate better and act better.

**Simulate before acting.**
- WebDreamer, GPT-4o on VWA: 17.6 reactive, 23.6 with simulation (+34.1% relative), 26.2 with real tree search; 4-5x faster than tree search (c08, c09). A fine-tuned 7B simulator reached 21.9 vs 17.2 for the untuned 7B base (c09).
- Prompted SimRollout (b19): +3 to +14 points.
- Trained: Dyna-GRPO beats GRPO by 4 points (b17). ReSim matches R1 on Sokoban (96.4 vs 96.6) at about 1/14.5 of the tokens (b18).
- Separate world-model Dyna in OSWorld and WindowsAgentArena: no gain or a loss (c06). In-thread simulation helped. So how the simulator is wired in matters.

**Offline thinking and memory.**
- Sleep-time: about 5x test-time saving, +13%/+18% (c01). The control is equal test-time tokens (d10). Synthetic "Stateful" tasks built so the question is predictable.
- AWM: WebArena 35.5 vs 23.5 (c13). Whole-task success on Mind2Web stays under 5% (d11).
- ACE: AppWorld 42.4 to 59.4 with offline replay of training traces (d06).
- ReMe: Qwen3-14B + ReMe 44.66 vs Qwen3-32B no memory 40.89 Avg@4 (d05). A smaller model with good memory can beat a larger one without.
- Reflexion: HumanEval pass@1 91% vs 80% (c17, abstract only). Voyager: 3.3x more unique items (c20, abstract only).

**Synthetic experience (training).** DreamGym trains on LLM-simulated environments. Zero real data roughly matches 80K-real-interaction GRPO, with ALFWorld Qwen losing 8.8 points (71.0 vs 79.8) and WebArena gaining (12.7 vs 6.1) (d09). Single group.

**What changed performance, by how much.**

| Change | Size | Source |
|---|---|---|
| Strict write gate vs add-all | +15 to +25 points on 3 of 4 agents (EHRAgent 13.1 to 38.5) | d01 |
| Delta-updated playbook vs no memory | +17.0 | d06 |
| Offline workflows | +12.0 | c13 |
| Next-state simulation before acting | +6 to +14 | c08, b19 |
| Offline pre-reasoning | up to +13/+18, or 5x less test compute | c01 |
| Learned retrieval over similarity | under +1 | d12 |
| Extra replay epochs | about +2.6 | d06 |
| Harmful update every step | -4.0 (70.7 to 66.7) | d07 |

**Caveats.** Many gains come from trained models or the authors' own benchmarks. The only no-training evidence is prompted rollouts, WebDreamer, sleep-time, AWM, ACE, ReMe, Reflexion, ExpeL (critique). No source compared a replay pass with a fresh attempt at equal total tokens.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the subgoal/lesson library written at S9.

### Add now (established)

1. **Gate every library write on a checked outcome.** Part: memory, S9, G2/G3. [E]. Evidence: d01, d02, d05, d06 (K22). A strict check beat add-all on all four agents, +3 to +22 vs fixed memory; add-all cost 3.7 to 12.1. Close to G2/G3 already; make it explicit for S9: no lesson is stored unless a code-checked result confirms it.
2. **Treat the model's own predicted outcome as a hint, never as evidence.** Part: G2, G10. [E]. Evidence: c10 (59.9% ceiling), d08, a20 (K14, K11). Any value written from a simulated outcome is tagged "simulated" and checked on the next real run.
3. **Use short lookahead branched from real stored cases, not long imagined chains.** Part: S2/S3, O3/O5. [E]. Evidence: a22, a21, a20 (K11).
4. **Include old, unvisited items in any replay pass, not only recent successes.** Part: memory. [E]. Evidence: a14, b11 (K09).
5. **Cap library size.** Part: memory. [E]. Evidence: c23, c24 (K20). Large buffers can hurt; include the newest entry always.
6. **Pay for replay only when reuse is likely.** Part: G7, G12. [S]. Evidence: c02, c03. Few queries per context: not worth it. Gate any offline pass on expected reuse count.
7. **Update the library by delta, never by full rewrite.** Part: memory. [S, but the failure is large]. Evidence: d06 (66.7 to 57.1 after collapse). Cheap, no known downside.
8. **Store short keypoints, retrieve at most about 5.** Part: memory. [S]. Evidence: d05 (+4.17 vs +2.67; K above 5 hurts). Same-group ablation.
9. **Log retrieval count and outcome per entry.** Part: memory. [S]. Evidence: d02, d05. Needed to test any deletion or priority rule. Costs nothing.

Items 1 to 5 rest on two or more independent sources; items 6 to 9 are single-source but cheap and low risk, so they are safe defaults while their tests run.

### Test first

1. **Replay pass vs fresh attempt at equal total tokens.** Part: memory, S9. [open]. Evidence: d10, d06, K27. The highest-value unknown. See T1.
2. **Dyna-Q+ style stale re-test.** Part: memory, S0. [S, analogy]. Evidence: a02, d11 (K02, K25). After a task-fact change, does scheduled re-test of old entries beat a library that never re-tests?
3. **Replay priority.** Part: memory. [S]. Evidence: a03, a13, d04, d12 (K03, K23). Surprise (failed prediction) times reuse likelihood against recency and random. On a clean library recency ties scored (d04), so gain probably appears only under pollution.
4. **Sleep-time pre-computation per item family.** Part: memory, S1/S2. [S]. Evidence: c01-c04.
5. **Prompted next-state prediction gated on measured hit rate.** Part: S2, G10. [E for direction, threshold unknown]. Evidence: c08, b19, d08 (K13, K26).
6. **Abstract-rule restructuring of stored traces.** Part: memory, O6/O7. [S]. Evidence: a15 (K08). Reorganise by rule, not order seen; test transfer to new surface content.
7. **Reuse of stored sub-solutions for a new goal vs replanning.** Part: memory, O3. [S]. Evidence: b13 (K21).
8. **Hindsight relabelling of failed attempts.** Part: memory, S9. [S, abstract only]. Evidence: c22. A failed trace may solve a different item; store it under that goal.
9. **Corruption tolerance of the library.** Part: G2. [S]. Evidence: d07, d18 (K24). Measure the accuracy loss at 5-20% bad entries before trusting simulated updates.

## 8. Concrete tests on our bench

All arms at equal total tokens, counting offline replay tokens and setup. Report accuracy per total token. Use the repeated item families on the bench, with held-out items from the same family for scoring.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Repeated families (5 or more solved items each), then held-out items | A: replay pass over stored solved traces (re-derive, relabel, abstract) then solve. B: same tokens spent on fresh attempts with no replay. C: S9 one-line lesson only | Accuracy on held-out items at equal total tokens | Small win for A over C when reuse is high; parity with B on one-off items |
| T2 | Same, three replay budgets | 0, few (5 traces), many (all traces) | Accuracy vs replay tokens | Big gain from the first few passes, then flat (a01 shape: 25 to 5 to 3 episodes) |
| T3 | Families where one rule changes after the library is built | A: no re-test. B: scheduled re-test of oldest entries (Dyna-Q+ analogue). C: replay of successes only | Accuracy on changed items; token cost on unchanged items | B beats A and C on changed items; costs a few percent on unchanged |
| T4 | Same families, polluted writes | Add-all, strict gate, strict gate + recency | Accuracy; library size | Strict gate beats add-all by 3 or more points (d01) |
| T5 | Library with 0, 5, 10, 20% injected wrong entries | Plain library vs outcome-tagged and simulated-tagged entries | Accuracy loss vs corruption rate | Small loss below 20%; sharp above (d07) |
| T6 | Replay order | Random, recency, surprise-weighted (failed prediction x reuse count) | Accuracy at fixed replay tokens | Clean library: tie. Polluted: surprise-weighted better (d04 pattern) |
| T7 | Items with predictable follow-up questions on shared context | Sleep-time pre-reasoning (1, 3, 5 questions per context) vs none | Accuracy per total token by number of queries | Win only above 2-3 queries per context (c02) |
| T8 | Lookahead | Reactive vs prompted next-state prediction; and a noisy-oracle simulator at 40/60/80/100% accuracy, fixed model | Accuracy; break-even hit rate | Lookahead helps above a break-even hit rate; find it (K26) |
| T9 | Text version of reward-vs-transition revaluation, with and without a replay step | Replay on/off x reward/transition change | Revaluation score as in a07 | Transition change harder; replay helps transition more than reward (a05 prediction) |
| T10 | Retrieval depth | Retrieve 1, 3, 5, 8 entries | Accuracy | Peak near 5 (d05) |

Rule for every test: report item counts per family. A gain counts only if it clears the plain-model arm at equal tokens (G7).

## 9. What does not transfer, and why

- **Value tables and TD updates.** The schema has no numeric value over states. Dyna's n planning steps update Q. We would update text entries. The sample-efficiency curve (a01) may not carry over.
- **Reliable models.** Dyna assumes a model learned from real data. An LLM "model" hallucinates (59.9% ceiling on non-trivial changes, c10). Value from simulated states can mislead (a20).
- **Free idle compute.** In RL, planning runs in idle time. On our bench tokens are the budget and G7 counts them. Sleep-time gains were against test-time tokens only (d10).
- **Hippocampal mechanics.** Reverse and forward replay timing, ripples, place cells have no counterpart. The principle (priority by gain and need) may transfer, the mechanism does not.
- **The SR itself.** A matrix of expected state occupancy has no direct equivalent in free-text problems with open state spaces. SR-Dyna also cannot handle hidden state (b03).
- **The human revaluation asymmetry.** One lab, n=58 and 88, a gap of about 0.07 in score (a07). Do not design around it.
- **Training-based results.** Dyna-Think, Dyna-Mind, DreamGym, Dyna-GRPO train weights (a24, b17, d09). We do not. Only prompted variants (b19) apply.
- **Atari, robotics, maze benchmarks.** Mostly tabular or image tasks with dense state.
- **Mind2Web-style gains.** Whole-task success under 5% (d11); step gains may not reflect solved problems.
- **Single-step prediction agents.** The write-gate study used regression, EHR code, driving and traffic tasks, not multi-step reasoning (d01 limits).

## 10. Open questions

1. At equal total tokens, does a replay pass over stored solved traces beat a fresh attempt for repeated item families? (K27, critique gap 1)
2. Which priority wins on an LLM library: surprise, expected reuse (need) or recency? No expected-value-of-backup test on LLM memory was found. (K23)
3. How is a stale subgoal detected and re-tested? Is library staleness after a task change measured anywhere? (K25)
4. What simulator hit rate makes lookahead beat reactive acting? (K26)
5. Do sleep-time, AWM, Dyna-Think and DreamGym replicate on other benchmarks or by other groups?
6. Does a replay step change LLM behaviour on reward-vs-transition revaluation? (K27)
7. Does updating memory from simulated (not real) outcomes degrade accuracy, and by how much? Noisy writes are measured (d07); simulated outcomes as such are not.
8. Independent replication of the human reward > transition asymmetry and of the replay-replanning link at larger n. d14 is a partial, null-leaning answer.
9. The primary text of Sutton 1990/1991 was not readable (image-only PDF, d20). Early maze episode counts remain via the textbook.
10. Is replay for planning or for memory maintenance? Gillespie 2021 (b11) conflicts with planning-focused results. The answer may differ by task or species.
11. What is the break-even reuse count for amortising an offline pass on a text library? Sleep-time says several queries per context; no direct number for libraries.
12. When does one non-transferable case become an over-general rule (OEP, d18)? Needs measurement on our bench.

## 11. Sources

[V] = opened (full text or page read). [M] = snippet or abstract-level only. Evidence ids in brackets.

**Dyna and prioritised replay (RL)**
- [V] Sutton and Barto, Reinforcement Learning: An Introduction, ch. 8 [a01, a02, a26]: http://incompleteideas.net/book/RLbook2020.pdf
- [M] Sutton and Barto as used for Dyna-Q+ shortcut experiments [b29]: same URL
- [V] Moore and Atkeson 1993, Prioritized sweeping [a03, d13]: https://link.springer.com/content/pdf/10.1007/BF00993104.pdf
- [M] Moore and Atkeson via DOI [c30]: https://doi.org/10.1007/BF00993104
- [M] Sutton 1991, Dyna [a19, c29]: http://incompleteideas.net/papers/sutton-91.pdf ; https://doi.org/10.1145/122344.122377
- [M] Sutton 1990, Integrated architectures [d20, image-only PDF]: http://incompleteideas.net/papers/sutton-90.pdf
- [V] Schaul et al. 2016, Prioritized experience replay [a23, c21]: https://arxiv.org/abs/1511.05952
- [M] Andrychowicz et al. 2017, Hindsight experience replay [c22]: https://arxiv.org/abs/1707.01495
- [M] Zhang and Sutton 2017 [c23]: https://arxiv.org/abs/1712.01275
- [M] Fedus et al. 2020 [c24]: https://arxiv.org/abs/2007.06700
- [M] van Seijen and Sutton 2013 [c25]: https://arxiv.org/abs/1301.2343
- [M] Hafner et al. 2023, DreamerV3 [c26]: https://arxiv.org/abs/2301.04104
- [V] Aminmansour et al., value hallucination [a20]: https://arxiv.org/abs/2006.04363
- [V] Holland, Talvitie, Bowling 2018 [a21]: https://arxiv.org/abs/1806.01825
- [V] Janner et al. 2019, MBPO [a22]: https://arxiv.org/abs/1906.08253

**Human and animal replay, SR, theory**
- [V] Russek et al. 2017, PLoS Comput Biol [a04-a06, b01-b03, c27]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005768
- [V] Momennejad et al. 2017 [a07-a09, b04, b05]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6941356/ ; https://www.biorxiv.org/content/10.1101/083824v2.full
- [V] Momennejad 2020 review [a10, a27, b06, b07, b16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9004662/
- [M] Momennejad 2020 via DOI [c28]: https://doi.org/10.1016/j.cobeha.2020.02.017
- [V] Momennejad et al. 2018, eLife [a11, a12, b08, b09]: https://elifesciences.org/articles/32548
- [V] Mattar and Daw 2018 [a13, a25]: https://www.biorxiv.org/content/10.1101/225664v4.full.pdf
- [V] Karlsson and Frank 2009 [a14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC2750914/
- [V] Liu et al. 2019 [a15, b10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6657653/
- [V] Vikbladh et al. 2019 [a16]: https://pmc.ncbi.nlm.nih.gov/articles/PMC6508991/
- [M] Gershman, Markman and Otto 2014 [a17]: https://pubmed.ncbi.nlm.nih.gov/23230992/
- [M] Foster and Wilson 2006 [a18]: https://doi.org/10.1038/nature04587
- [V] Gillespie et al. 2021 [b11, b12]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8497431/ ; https://www.biorxiv.org/content/10.1101/2021.03.09.434621v1.full
- [V] Tomov, Schulz and Gershman [b13]: https://www.biorxiv.org/content/10.1101/815332v1.full
- [M] Stachenfeld, Garvert, Schapiro; Sarel, Boccara, Butler, as cited in Momennejad 2020 [b14, b15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9004662
- [V] Zhang, Kahn, Daw, Nussenbaum, Hartley 2026 [d14]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12797880/
- [V] Kahn and Daw 2025 [d15]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11700031/
- [M] Sagiv, Akam, Witten, Daw 2025 [d16]: https://doi.org/10.1016/j.neuron.2025.09.021
- [M] Antonov and Dayan 2025 [d17]: https://doi.org/10.1038/s41467-025-56731-y

**Language-model studies**
- [V] Lin et al. 2025, Sleep-time Compute [c01-c04, d10]: https://arxiv.org/abs/2504.13171
- [V] Yu et al. 2025, Dyna-Think [a24, b22-b24, c05-c07]: https://arxiv.org/abs/2506.00320 ; https://arxiv.org/html/2506.00320v3
- [V] Dyna-Mind 2025 [b17-b21, d08]: https://arxiv.org/abs/2510.09577 ; https://arxiv.org/html/2510.09577v1
- [V] Gu et al. 2024, WebDreamer [c08, c09]: https://arxiv.org/pdf/2411.06559
- [V] Wang et al. 2024, text-based world simulators [c10]: https://arxiv.org/pdf/2406.06485
- [V] Chen et al. 2025, DreamGym [b25, b26, c11, c12, d09]: https://arxiv.org/abs/2511.03773
- [V] Wang et al. 2024, Agent Workflow Memory [c13, d11]: https://arxiv.org/abs/2409.07429
- [M] Hao et al. 2023, RAP [c14]: https://arxiv.org/abs/2305.14992
- [V] Momennejad et al. 2023, CogEval [c15, c16]: https://arxiv.org/pdf/2309.15129
- [M] Shinn et al. 2023, Reflexion [c17]: https://arxiv.org/abs/2303.11366
- [M] Zhao et al. 2024, ExpeL [c18]: https://arxiv.org/abs/2308.10144
- [M] Park et al. 2023, Generative Agents [c19]: https://arxiv.org/abs/2304.03442
- [M] Wang et al. 2023, Voyager [c20]: https://arxiv.org/abs/2305.16291
- [M] Agent Learning via Early Experience 2025 [b27]: https://arxiv.org/abs/2510.08558
- [M] Holt et al., Fact-augmented lookahead planning [b28]: https://arxiv.org/abs/2506.09171
- [V] Xiong et al. 2025, memory management [d01-d03]: https://arxiv.org/abs/2505.16067
- [V] Reddy 2026, TraceRetain [d04; table garbled, prose used]: https://arxiv.org/abs/2606.29178
- [V] Cao et al. 2025, ReMe [d05]: https://arxiv.org/abs/2512.10696
- [V] Zhang et al. 2026, ACE [d06, d07]: https://arxiv.org/abs/2510.04618
- [V] Zhou et al. 2025, Memento [d12]: https://arxiv.org/abs/2508.16153
- [V, partial] Wang et al. 2026, OEP [d18]: https://arxiv.org/abs/2605.18930
- [M] Hazard et al. 2025, SuRe [d19]: https://arxiv.org/abs/2511.22367

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 9 established claims: 8 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B05.03-K09** (now single-source: the sources are not independent). Numbers match, but Karlsson and Frank 2009 (3 rats) and Gillespie et al. 2021 (4 rats) are both from the Loren Frank lab, so the two rat-replay sources are one lab's work.
