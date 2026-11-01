# Prioritised memory access: deep document

*Subfield B05.04. Written from evidence_a-d.jsonl, claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids (a01 ... d33) point to lines in the evidence files. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

Prioritised memory access is the idea that a learner does not replay or revisit stored experience at random or in order of recency. It picks the next memory update by expected benefit. Mattar and Daw (2018) made this exact. Every possible memory update (one Bellman backup, i.e. one value update at one stored state) gets a score called the expected value of backup (EVB):

**utility = gain x need**

- **Gain**: how much the update would improve future reward, because it would change the choice made at that state. If the update would not change the choice, gain is zero.
- **Need**: how many times, discounted, the agent expects to be in that state soon. Computed from the successor representation (SR), a table of expected future state occupancy.

The agent runs the highest-utility update first, then recomputes, then runs the next. One rule yields many observed rodent replay patterns: forward replay before a run (need is high ahead of the agent), reverse replay after a surprise (gain is high behind the agent), replay of remote places, fewer replays with experience, and reverse replay that rises with bigger reward and falls when reward is removed (a01-a09).

The machine-learning cousin is prioritised experience replay (PER; Schaul 2016): sample stored transitions by the size of their TD (prediction) error. This has gain-like content only. It has no need term and no policy-change term (a12).

Why it matters for our agent. The agent holds stored subgoals, notes and partial derivations. Context and tokens are limited, so it must decide which to revisit. Mattar and Daw give a principled rule: revisit what (a) would change the plan if updated and (b) is likely to be needed soon. The open problems are whether this beats recency and random ordering at equal tokens in a language-model scaffold, and which cheap proxy for gain works. As of this search nobody has tested that directly (K17, K23).

Scope of this document: the rodent and human replay evidence, the model and its theory extensions, the RL engineering literature, and LLM work that orders, filters, decays or re-ranks stored material. Replay as offline simulation (Dyna family), retrieval and similarity, and case-base maintenance are covered by other subfields; only links are noted here.

## 2. History and theories in depth

**Roots in AI (1990s).** Sutton's Dyna (1991) learns from simulated experience between real steps. Moore and Atkeson (1993) prioritised sweeping orders those updates by the size of the predicted value change and pushes surprise back to predecessor states. Peng and Williams (1993) did similar work. Mattar and Daw treat both as special cases of their rule. We did not open the originals; all is second-hand from Mattar and Daw and Schaul (a13, b20, c18).

**Rodent replay discovery (2006-2013).**
- Foster and Wilson (2006): awake rats replay a just-run path in reverse at the end of the run (abstract only, a14).
- Diba and Buzsaki (2007): forward sequences before a run, reverse after. Opened in the author manuscript: 36% of events significantly forward-correlated and 19% reverse-correlated; 841 of 887 forward events at the start end before running; 395 of 464 reverse events at the far end after the run (d26). The forward:reverse ratio was about 2 (95% CI 1.74 to 2.11).
- Davidson, Kloosterman and Wilson (2009): long 10.3 m track, 4 rats, 263 significant events: 40% forward (106), 26% reverse (68), 33% mixed (89). For events over 250 ms: 48% forward (66/138) vs 25% reverse (34/138). 40% of replay trajectories start within 50 cm of the rat vs 17% by chance. So forward outnumbered reverse in this design (a16).
- Karlsson and Frank (2009): awake rats replay places they are not in, including a remote track. 182 of 442 (41.2%) of events in track 2 replayed track 1 (a18).
- Gupta et al. (2010): replay is not a simple function of experience; novel never-travelled paths and rarely run paths are replayed (abstract only, a20).
- Pfeiffer and Foster (2013): in an open 2 m x 2 m arena with 36 possible goals, sequences before movement run from the current position to the goal and predict the immediate path, even for novel start-goal pairs. 2,028 trajectory events, none above P 0.02 under two shuffle tests (d27).
- Olafsdottir et al. (2015): preplay of a seen but never visited rewarded arm. 4 rats, 212 cells (b08).

**Causal tests.** Jadhav et al. (2012): interrupting awake sharp-wave ripples impaired spatial learning (abstract, a21). Widloski and Foster (2022): replays route around moved barriers (abstract, a22).

**The model, 2018.** Mattar and Daw (Nat Neurosci 21:1609). Simulated rat tasks with fixed parameters and no fitting. Match to data is qualitative (a01-a11, c01, c02). Key reported matches: Ambrose 2016 reward asymmetry, Diba/Davidson direction patterns, initiation at or just behind the agent, goal over-representation, fall of replay count with experience, Olafsdottir preplay.

**Reward-modulation data the model leans on.** Ambrose, Pfeiffer and Foster (2016): 5 rats. Reward raised 4x at one track end: reverse replay rose (z=3.57, p=3.6e-4), forward did not (z=0.305, p=0.76). Reward removed: reverse fell (z=-2.05, p=0.041), forward fell less clearly (z=-1.83, p=0.068). 581 of 738 (79%) and 314 of 409 (77%) replays were classified by direction (a17, b03). Caveats: dwell time moved with reward (20.3 vs 8.1 s at 4x; 3.3 vs 8.5 s at 0x), and under stricter criteria there were zero reverse replays at the removed reward.

**Human tests (2018-2026).**
- Momennejad et al. (2018, eLife, fMRI, N=24 analysed): rest-time reinstatement of old states predicted re-planning after a reward change only when revaluation was needed (rho=0.54, p=0.0068 vs control rho=-0.13, p=0.55; difference p=0.023). Reinstatement fell across rests (t(23)=2.9, p=0.007), consistent with falling gain (a24, a25, b06).
- Liu, Dolan, Kurth-Nelson and Behrens (2019): human rest replay follows learned structure, reverses after reward (b07).
- Eldar et al. (2020, MEG, N=40): online replay after surprising, policy-relevant news; re-evaluation raised reward by 11.1% (p=0.001). No formal gain/need test (a26).
- Liu, Mattar, Behrens, Daw and Dolan (2021, Science, MEG, N=29): the first direct human test of gain x need. See section 3 (a27, a28, b05, b25, c03, c04).
- Wimmer et al. (2023): replay before choice when planning pays; after reward, replay of the distal environment grows with time since last experience (abstract only, d05).
- Neuron 2026 iEEG (N=34, abstract only): ripples carried which indirect experience was most valuable to update; longer ripples carried stronger priority signals (d29).
- Anxiety study (Nat Commun 2025, abstract only): backward replay of a reward-linked sequence fell with trait anxiety (d31).

**Challenges.**
- Gillespie et al. (2021): 8-arm task, 4 rats, 23 to 33 sessions each. Replay covered the previous goal (about two-fold enriched), not the upcoming choice. Future-arm enrichment was small and not in all animals. Classifiers predicting correct vs error trials from replay counts were near 50% (a23, b04). The authors say replay "seems unlikely to implement the value updates that could drive behavior".
- Carey, Tanaka and van der Meer (2019): 4 rats, 19 of 24 sessions analysed. Replay content was biased away from the arm preferred that day (content vs choice r(19)=-.75, p<.001), even before the task started (d01).
- Tirole, Duvelle and Bendor (2026 preprint, 3 decoded rats): behavioural state, not reward size, predicted awake replay rate; sleep replay favoured the most recent episode regardless of reward (d28).
- Preplay of never-visited paths (Olafsdottir; Gupta) breaks the model assumption that replay only recombines experienced transitions (b08).

**Theory extensions (2022-2025).**
- Gagne and Dayan (2022, PLoS Comput Biol): add uncertainty and forgetting. When the internal model is uncertain, the best replay can favour wrongly chosen suboptimal actions, so "pessimal" replay is rational. Human re-analysis of Eldar data: n=25, Spearman M=0.04, p=0.04. Forgetting parameter vs decision flexibility beta=-0.37, p=0.016 (d02).
- Jensen, Hennequin and Mattar (2024): a recurrent agent meta-learns when to run rollouts. Rollout probability vs human thinking time r=0.186; after conditioning on distance to goal r=0.070. 94 participants (d03).
- Diekmann and Cheng (2023): a cheap rule using experience strength, similarity and inhibition of return comes close to Mattar and Daw in RL (abstract only, d04).
- Sagiv et al. (2025): utility extended to routes toward future as well as current goals, weighted by the estimated chance of later relevance (d30).
- No paper found replaces the one-step (myopic) gain with a multi-step value of a replay chain (d19; 92 citing records scanned by title).

**RL engineering line.** Schaul 2016 PER; Rainbow ablation (Hessel 2018); Zhang and Sutton 2017 (large buffers slow learning); Fedus 2020 (prioritisation adds little at larger capacity without n-step); Sujit 2023 ReLo (PER worse than uniform in places); Lahire 2022 LaBER; Panahi 2024 (no prioritised variant consistently beats uniform with neural nets); Jiang 2021 Prioritized Level Replay; Wang 2025 Prioritized Generative Replay; MBPO (Janner 2019) for compounding model error (section 5).

**LLM line (2023-2026).** Generative Agents (2023) score memory by recency + self-rated importance + relevance. Then, in 2024-2026: replay in RL fine-tuning (CodeIt, P2Value, FreshPER, advantage-prioritised replay, DyJR, Fatemi's prioritised replay), outcome-weighted memory retrieval (MemRL, ReMe, ExpHarness, APEX-EM), retention policies, and scaffold-level event-driven memory (Weighted Memory Tree). Section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Utility = gain x need reproduces forward replay before runs and reverse replay after surprise | Simulated gridworld and tracks; softmax beta=5, gamma=0.9, alpha=1, 20 planning steps at episode start and end, 50 episodes; significant replay = run of 5 or more backups by permutation test. No parameter fitting; counts shown only as figures | Mattar and Daw 2018 (a01-a09, c01, c02) | [S] model, qualitative match (K01) |
| Prioritised replay learns faster than none or random (Dyna) replay in the model | Curves only, no tabulated step counts | a04 | [S] |
| Reverse replay tracks reward change; forward replay does not | Rats N=5. 4x reward: reverse z=3.57 p=3.6e-4, forward z=0.305 p=0.76; forward vs reverse z=4.30. 0x reward: reverse z=-2.05 p=0.041, forward z=-1.83 p=0.068. 581/738 (79%) classified | Ambrose 2016 (a17, b03) | [E] with Liu 2021 (K03); dwell-time confound |
| Human backward replay (160 ms lag) is stronger for high-utility non-local paths | N=29. Non-local content t(28)=2.92 p=0.007; high vs low utility t(28)=3.30 p=0.003. Decoding peak 47% vs 6% chance | Liu 2021 (a27, c03) | [E] with Ambrose; one human study |
| Forward replay (30 ms lag) shows no utility effect | t(28)=-0.34, p=0.74. 30 ms replay ripple power t(28)=3.98 p=4.3e-4; 160 ms replay ripple t(28)=0.64 p=0.53; difference p=0.0052 | Liu 2021 (b25, c03) | [E] (K03) |
| Gain, not need, carries the behavioural effect | Non-local learning rate: high-gain 0.79 vs low 0.37 (p=0.020). High-need 0.61 vs low 0.54 (p=0.16). Need levels 17/33/50%. Gain and need uncorrelated r=-0.004. Local vs non-local rates 0.64 vs 0.60 | Liu 2021 (a28, b05, c04) | [E] in biology (K02); need only 3 levels |
| Backward replay goes with faster non-local learning | Learning rate 0.70 with significant 160 ms replay vs 0.61 without (difference 0.09, p=0.023); forward 30 ms difference 0.01. Replay strength vs reward per trial r=0.41, p=0.03 | Liu 2021 preprint text (b05, c04) | [S] (K24) |
| Rest reinstatement predicts re-planning only when revaluation is needed | N=24. rho=0.54 p=0.0068 vs control rho=-0.13 p=0.55; difference p=0.023. Replanning t(23)=4.89 vs -0.10. Noisy vs noiseless split p=0.066 | Momennejad 2018 (a24, b06) | [S] (K04) |
| Replay falls across rests as prediction errors shrink | Rest 1 to 3 t(23)=2.9 p=0.007; revaluation vs control in rest 1 t(23)=2.17 p=0.039 | Momennejad 2018 (a25) | [S] |
| Online MEG replay after surprising policy-relevant news | N=40. Forward lag 130 ms; flexibility beta=0.17, surprise 0.06, interaction 0.19; moves with high sequenceness less likely re-chosen rho=-0.04 p=0.04 (n=25); re-evaluation raised reward 11.1% p=0.001 | Eldar 2020 (a26) | [S] |
| Forward events outnumber reverse in a pausing design | 263 events: 40% forward, 26% reverse, 33% mixed; events over 250 ms 48% vs 25%; forward more frequent p<0.005 (all 263), p<0.002 (over 250 ms). Forward replay did not predict the next path (15 vs 12); reverse did not reliably match the path just taken (9 vs 7) | Davidson 2009 (a16) | [E] direction is design-dependent (K08) |
| Before-run forward, after-run reverse (founding counts) | 841/887 forward before run; 395/464 reverse after. 36% forward vs 19% reverse of events | Diba and Buzsaki 2007 (d26, b21) | [E] (K08) |
| Replay covers remote, rare and never-travelled paths | Remote replay 182/442 (41.2%) Z=12.67; awake rest 256/580 (44.1%) vs quiescent 373/1046 (35.7%) p<0.001; preplay of unvisited arm, 4 rats, 212 cells | Karlsson and Frank 2009; Olafsdottir 2015; Gupta 2010 (a18, b08, a20) | [E] (K07) |
| Replay favours the previous goal, not the upcoming choice | 4 rats; previous-goal replay about 2x enriched; R2 for current-goal replay vs reward 0.033/0.015/0.012/0.025; previous-goal replay vs later visits p=0.49/0.32/0.18/0.08; classifiers near 50% | Gillespie 2021 (a23, b04) | [C] (K06) |
| Replay content biased away from the preferred arm | 4 rats, 19 sessions; r(19)=-.75 p<.001; SWR content z=-.41 vs +.40, p=.004; pre-task bias z=-.55 vs .39 p=.003 | Carey 2019 preprint (d01) | [C] (K06) |
| Forgetting makes pessimal replay optimal | Human MEG n=25, M=0.04 p=0.04; beta=-0.37 p=0.016; gain threshold vs benefit beta=0.24 p=0.083 (n.s.) | Gagne and Dayan 2022 (d02) | [S] (K21) |
| Rank-based PER beats uniform replay in DQN | Median human-normalised score 48% to 106% on 49 Atari games; mean 122% to 355%; better on 41 of 49. Double DQN, 57 games: median 111% to 128%, mean 418% to 551%. alpha=0.7, beta0=0.5 | Schaul 2016 (a12, b10, c05) | [E] (K09), but see next row |
| Raw error priority is brittle | PER worse than uniform in SAC, Seaquest, SpaceInvaders (ReLo; DM Control, MinAtar, 24 Atari games, 5 seeds). Rainbow 1M to 10M buffer: +17.3% median without prioritisation; -2.3% without n-step. Buffers 1e2 to 1e6 slow learning. No prioritised variant consistently beats uniform (Panahi, abstract) | b12, b13, b14, c06, d13 | [E] (K10) |
| Plain PER fails in LLM RL because priorities go stale; exponential age decay fixes it | Qwen2.5 0.5B/3B-VL/7B, 8 tasks: +46% NQ Search, +367% Sokoban Simple, +133% VLM FrozenLake, +18% AIME vs on-policy; little on GSM8K (>93% base). tau=500 fast drift, 1000 slower. Buffer 50K, alpha=0.6, beta=0.4 | FreshPER (a30, b16, d08) | [S] one group (K11) |
| Advantage-ranked rollout replay beats GRPO and beats uniform replay at equal volume | Qwen3-Base 0.6B/1.7B/4B, 3 seeds: +0.61/+0.60/+1.66 pp. Table 4, 1.7B, single seed: uniform rollout 16.19 avg / 28.96 pass; abs-advantage priority 16.58 / 32.35. Naive replay 0.83 and 1.82 pp below no-replay at 4B. Age cap 10 best (pass 32.35; cap 1 29.59; cap 30 27.34); replay ratio 0.5 | Yoo 2026 (a31, d20) | [S] (K12) |
| Difficulty-targeted selection + recent rollout reuse cuts GRPO time | 23% to 62% less time at equal performance, 6 model-dataset pairs | Sun 2026 (b17) | [S] (K13), training only |
| Problem-level priority p(1-p) is useful but starves unseen problems | Qwen2.5-7B, 1000 problems, 250 steps, single run; over 600 problems never seen; 12.5% random exploration did not fix it | Fatemi 2026 (c07, c25) | [S] proof of concept |
| P2Value gains are mostly distillation | GPT-Neo APPS-mixed 5.73 to 42.12 (trained on GPT-4-turbo samples). Self-fine-tuning: GPT-2 7.30 to 8.12; GPT-Neo 5.73 to 5.39 (down); WizardCoder 40.24 to 41.25. No ordering ablation | Chen 2025 (a32, d06) | [S] (K14); not evidence for ordering |
| Admission vs use of replay (confidence admission, JS regulariser, short window) | Qwen3-4B-Base six math sets: GRPO 29.8 to DyJR 34.1 (3 runs); confidence admission +2.5 (PG+IS) and +3.7 (JS); JS +1.5 over PG+IS; window M=8 34.1 vs M=16/32/64 32.9/31.7/30.9. Qwen3-1.7B 17.3 to 19.5. Ablations single-run | Li 2026 (b18, d07) | [S] (K15) |
| Learned outcome utility re-ranks agent memory | Avg CSR: no memory 0.631; RAG 0.699; Self-RAG 0.726; Mem0 0.712; MemP 0.760; MemRL 0.798 (+3.8% over MemP). Q weight best at 0.5 (inverted U). Q vs success r=0.861; 21.5% success in lowest Q bin to 88.1% in highest. Transfer +2.8% over MemP | MemRL (c13, d09) | [S] (K18); no recency/random control |
| LLM-rated importance is no better than recency in a retention test | LoCoMo F1 at budget 32: Recency 0.017, GA-heuristic 0.019, GA-LLM 0.016, Mixed 0.057, BC-learner 0.090, OSL-MR 0.123. Budget 128: OSL-MR F1 0.263, Mixed 0.087, Recency and GA below 0.03 | Kang 2026 (d10) | [S] (K19); retention, not order |
| Recency is close to random; a learned value is far better; a peeking cue is not usable | LongMemEval-S, 479 cases, keep top 30%: learned 0.770, uniform weights 0.657, self-relevance 0.518, recency 0.368, random 0.300, goal-only 0.286. Oracle: goal-only 0.979 (blind 0.286) | Chen and Cheng 2026 (d21) | [S] (K28, K19) |
| Model's own first-error pick beats random reset | OLMo-3-7B and Qwen2.5-14B, 10 benchmarks, 3 seeds, compute matched: SRPO best on 7/10 (14B), 6/10 (7B); RRPO about GRPO. Clean-prefix resets 28.7% vs 16.3% Pass@4. About half of self-localisations overshoot | Samanta 2026 (d22) | [S] (K25), training time |
| Stale beliefs fail mostly through dependants | 400 scenarios, 1,200 queries, up to 150K tokens. Best plain model 55.2%; memory frameworks 5.1% to 17.8%; CUPMEM 68.0%. Premise resistance 78.0% (Type I), 75.0% (Type II). Type II lower in nearly all systems | STALE (d23) | [S] (K26) |
| Event-driven, branch-scored prompt memory beats linear history | GAIA-Text, 127 questions, 3 small models: linear 20.47/24.41/9.45; full WMT 33.86/33.07/17.32. Mean +9.97 pp with 32.8% fewer prompt tokens. Unweighted tree 15.75/25.20/9.45 | Weighted Memory Tree (d24) | [S] (K27); package bundled |
| Decay differs by content type | Half-lives 148 to 189 decode steps (system text) vs 14 to 16 (scratchpad); Qwen2.5-1.5B/3B | MemDecay (d25) | [S] (K29), KV cache not notes |
| Short, branched model rollouts bound compounding error | Hopper: k raised 1 to 15 linearly was best; k=1 also worked. Bound has a term falling in k and one rising linearly | MBPO (d12) | [S] (K22) |

## 4. Mechanisms and models

**4.1 The Mattar-Daw algorithm (implementable).**

State: a table of action values `q(s,a)` learned so far, a transition model `T`, and the current state.

1. For every candidate backup (s_k, a_k, r, s'_k), compute:
   - `gain = sum_a (pi_new(a|s) - pi_old(a|s)) * q_new(s,a)`. This is the expected improvement of the policy at s if the backup is applied. For a greedy agent it is positive only if the best action would flip.
   - `need = row of (I - gamma*T)^-1 for the current state, at column s`. This is the expected discounted number of future visits to s. For an absent agent (rest), use the stationary distribution of T.
2. `EVB = gain * need`. Apply the highest-EVB backup. Update q. Recompute the priorities of the predecessors of the updated state (surprise propagates backward).
3. Stop after a fixed number of steps (20 in the paper), or when EVB falls below a minimum (1e-10 in the paper, so that all 20 steps are used).
4. A "replay event" is a chain of 5 or more consecutive backups. Chains build depth-first: a reverse chain goes back from the state with a prediction error; a forward chain goes ahead from the agent.

Why direction emerges: after a surprise, gain is large at the predecessors of the surprising state, and need is positive for states the agent just left or is about to revisit, so reverse chains win. Before a run, need is highest ahead of the agent, so forward chains win. Zero need or zero gain gives zero utility, so either factor can veto (a05, a08).

Why reward change is asymmetric: learning that a good action got much worse gives high gain; learning it got a bit worse but is still best gives about zero gain. That is why reverse replay moved with reward size and forward did not (a08). Experience lowers gain (errors shrink) and raises need (routes become predictable), so replay count falls (a09).

Settings in the paper: 4 moves; softmax beta=5; gamma=0.9; alpha=1; reward noise SD 0.1; transition learning rate 0.9; open field 6x9; two 1x10 track segments; full transition model known at start (a03).

**Stated limits (a11, b19).** Gain needs the policy effect known before the backup, which the authors call "admittedly unrealistic". Myopic (single one-step backup; no setup value for later backups). No uncertainty. Stationary, deterministic, tiny tasks. No process model for how the brain computes priority. Suggested approximation: myopic value of perfect information.

**4.2 Cheap approximations of the two terms.**
- Need proxies: successor-representation row (exact in tabular); recency or frequency of use; dependency distance to the current goal; a learned probability that the item will be called. Warning (K28): a need cue that saw the future question scored 0.979 but 0.286 blind. Compute need only from what exists at decision time.
- Gain proxies: size of prediction error (PER); learnability (loss drop; ReLo); absolute advantage (Yoo 2026); p(1-p) problem difficulty (Fatemi); a learned Q-value from outcomes (MemRL); the model's own first-wrong-step judgement (SRPO); the number of dependants of a changed fact (STALE). None has been validated as a gain predictor in a scaffold (K16, K19).
- Diekmann and Cheng's rule: strength + similarity + inhibition of return (abstract only). Inhibition of return stops the same item being picked again and again.

**4.3 Engineering PER (Schaul 2016).** Priority `p_i = |delta_i| + eps` (proportional) or `1/rank(i)` (rank-based). Sample with `P(i) = p_i^alpha / sum p^alpha`. Correct the bias with importance weights `w_i = (N * P(i))^-beta`, annealed. New items get maximal priority. Settings chosen: alpha=0.7, beta0=0.5 (rank); alpha=0.6, beta0=0.4 (proportional). Failure modes: greedy ordering over-fits a few high-error items, is sensitive to noise, and starves items whose error was low at first visit (a12).

**4.4 Freshness weighting (FreshPER).** `priority_eff = priority * exp(-age/tau)`. Derived from effective sample size, which decays exponentially with policy divergence. Half-life = tau x ln 2. tau=500 where the policy drifts fast, 1000 where it drifts slower (d08). Agent analogue: age counted in how many relevant new facts have arrived, not in tokens.

**4.5 Fresh-anchored replay (Yoo 2026).** Each batch mixes fresh data with replayed items (replay ratio 0.5), replayed items are ranked by absolute advantage, and nothing older than 10 steps is used (a31, d20).

**4.6 Admission vs ordering (DyJR).** Separate two questions: who gets into the buffer (confidence admission) and how the buffer is used (a divergence regulariser vs policy-gradient replay). A short window (last 8) beat longer windows (d07).

**4.7 Event-driven memory score (Weighted Memory Tree).** Each memory item has a retention score. It is updated by events (outcome recorded; branch failed; branch superseded). It decays only by missed selection ("elapsed time alone does not affect retention"). A branch is scored as max plus mean of its items minus failed and obsolete fractions. An invalidation event suppresses the branch directly (d24). This is the nearest published scaffold-level analogue of gain x need, but it bundles ordering, folding and suppression.

**4.8 Write-time dependency tracking (CUPMEM in STALE).** When a fact is stored, search for existing beliefs that depend on it, and flag them. At 68.0% overall vs 55.2% for the best plain model, it is the strongest result on stale dependants (d23).

**4.9 Learned outcome utility (MemRL).** Store (intent, experience, Q) triples. Retrieve in two phases: similarity top-k1 (k1=5), then re-rank to k2=3 by `(1-lambda)*sim + lambda*Q`, lambda=0.5. Update Q from reward by a Monte Carlo rule. Needs repeated tasks with reward feedback (d09).

**4.10 Guarding imagined rollouts (MBPO).** Branch short rollouts from real states; cap depth; mix with real data. Error grows with horizon (d12).

## 5. What holds up

**Holds up (replicated or from two or more independent sources).**
- Gain over need. Reward-change effects on replay were seen in rats (Ambrose) and humans (Liu 2021; Momennejad). Gain-linked effects were significant in 3 of 3 studies that tested them; the need-only effect was null in 1 of 1 (p=0.16). That synthesis is ours, not a meta-analysis (b22). Status [E] for gain-first, but it rests on one rat paper and one human paper that match in direction (K02).
- Reverse replay is the reward-sensitive one (Ambrose z=3.57 vs forward z=0.305; Liu 160 ms backward vs 30 ms forward p=0.74) (K03).
- Replay is not limited to recent or frequent paths (4 sources, K07).
- Direction is design-dependent (Diba before/after vs Davidson forward majority) (K08).
- Prediction-error priority beat uniform replay on Atari (Schaul; the Rainbow ablation said removing PER or n-step hurt most games), but Rainbow is not a clean replication (K09, critique corrections 3 and 6).

**Failures and boundary conditions.**
- Raw priority is brittle: ReLo, Fedus, Panahi, Zhang and Sutton (K10). Fedus: larger-capacity gains depend on n-step returns, not prioritisation. Zhang and Sutton: large buffers slow learning.
- Staleness is the main LLM failure (FreshPER; Yoo 2026 age cap 10 best, 30 worst).
- Replay content does not follow the planned choice in two rat studies (Gillespie 2021; Carey 2019). Gagne and Dayan's forgetting model reproduces the pessimal pattern while still using gain x need, so these results limit need-only and recency rules more than they limit gain x need (K06, [C]).
- Problem-level priority starves unseen items (Fatemi; Schaul's greedy PER starvation).
- Self-rated importance did no better than recency in one retention test (K19).
- Naive uniform or group-level replay is no better than no replay at 4B (Yoo).
- P2Value self-fine-tuning is flat or negative (GPT-Neo 5.73 to 5.39).
- Preplay of unexperienced paths breaks the model's assumption (Olafsdottir).

**Weak points of the whole structure.**
- The model was not fitted; all matches are qualitative (K01).
- The human gain x need test is one study, N=29, one task, three need levels, correlational, gain estimated from a model; the lags (160 ms, 30 ms) were chosen from the same data. No same-task replication found among 128 citing records (d18). The 2026 iEEG study (N=34, abstract only) is an extension, not a replication (d29).
- The 160 ms backward replay is slower than rodent ripple replay and may reflect conscious computation (c03).
- No study of language agents separates ordering from filtering, except Yoo 2026 (training time, single seed for the ordering ablation).
- Search recall for 2024-2026 LLM memory papers is limited (b24, d33).

**Interventions that worked (in LLM RL, training-time unless noted).** Age decay (FreshPER); age cap plus fresh anchoring plus advantage rank (Yoo); confidence admission plus short window (DyJR); moderate-difficulty selection (Sun, 23% to 62% time saved); reset to the first self-judged error (SRPO). At prompt time: learned-Q re-ranking (MemRL), event-driven memory (WMT), write-time dependency search (CUPMEM).

**Interventions that did not work.** Plain PER with |reward| priority in LLM RL; ranking by importance rated by the LLM (no better than recency); uniform group-level replay at 4B; P2Value self-fine-tuning; 12.5% random exploration did not fix starvation; a relevance cue scored blind (0.286, below random 0.300).

## 6. Language models

No study was found that tests gain x need ordering by name in a language-model agent (K17, K23, c24). The LLM evidence is indirect, in four groups.

**A. Replay ordering in RL fine-tuning (training time; it changes weights, so it does not transfer directly).**
- FreshPER (a30, d08): standard PER underperforms on-policy; age decay fixes it. Peak gains +46%, +367%, +133%, +18% over on-policy; little on GSM8K (>93% base) or CliffWalking. One group, preprint, percent gains on low bases.
- Yoo 2026 (a31, d20): +0.61/+0.60/+1.66 pp over GRPO at 0.6B/1.7B/4B (3 seeds). The only ordering ablation at equal replay volume: abs-advantage priority 16.58 avg / 32.35 pass vs uniform 16.19 / 28.96 at 1.7B (single seed). The authors note that equal accuracy might be reached by spending the compute on generation.
- DyJR (d07): 29.8 to 34.1. Admission and regulariser matter; ordering is not tested.
- Sun 2026 (b17): time cut 23% to 62%.
- Fatemi 2026 (c07, c25): p(1-p) problem priority; single run; starvation; plateau.
- Bae 2025 (c08): filtering to success rate near 0.5, up to +12% (abstract).
- CodeIt (c10): hindsight relabelling plus prioritised replay, 59 of 400 ARC eval tasks (about 15%); hindsight gave about 40% improvement; uniform sampling gave a small drop in cumulative performance but a large drop in policy performance (forgetting).
- P2Value (d06): gains are mostly distillation.
- SRPO (d22): self-chosen reset beats random reset; clean-prefix 28.7% vs 16.3% Pass@4.

**B. Outcome-weighted memory retrieval for agents (prompt time, frozen model).**
- MemRL (d09): CSR 0.798 vs RAG 0.699 vs MemP 0.760. Learned Q correlates with success, r=0.861. Needs rewards over repeated tasks; no recency or random control; mixed models in the average; single runs; about 12% of high-Q memories were failures.
- ReMe (c14): Qwen3-8B with ReMe beat Qwen3-14B without memory: +8.83% Avg@4 and +7.29% Pass@4; deletion not isolated.
- ExpHarness (c16): a trained copilot sets how much to favour useful vs similar experience; +12.1% and +4.5% on static tasks, +21.4% and +12.7% on agentic tasks over the strongest baseline; interaction steps cut up to 21.6%; ablations do not isolate utility ranking alone.
- APEX-EM (c22): +7.6 pp BigCodeBench; +1.4 and +1.0 pp on OS and DB. Trajectory memory (c23): up to +14.3 pp on AppWorld, +28.5 pp on complex tasks. Both retrieve by similarity or structure, not utility.
- Memory management study (c15): agents copy retrieved records (error propagation); history-based deletion helped with a reliable evaluator and hurt on AgentDriver with GPT-4o-mini as evaluator.
- Caution: none of these has a recency or random control at equal tokens (critique).

**C. Importance, retention and decay.**
- Generative Agents (c17, d11): recency + importance (LLM 1 to 10) + relevance, equal weights, min-max scaled. Full architecture TrueSkill 29.89 vs 21.21 with no memory, planning or reflection (Cohen's d = 8.16). The ablations remove whole components, so the importance term is untested.
- Retention (d10, d21): see section 3. Learned value 0.770 vs recency 0.368 vs random 0.300; LLM-rated importance no better than recency.
- MemDecay (d25): half-lives differ by region, about 10x.

**D. Stale beliefs and dependencies.**
- STALE (d23): 55.2% best plain model; frameworks 5.1% to 17.8%; dependency search 68.0%.
- WMT (d24): +9.97 pp over linear history with 32.8% fewer tokens (small models, 127 questions).
- TTEL (d17, listing only): pass@64 of 71.0% with 360.4k tokens vs 735.0k for independent sampling, by localising the error. FOCUS: 55.4 vs 48.2 BrowseComp-Plus. Not opened.

**What changed LLM behaviour, by how much (summary).** Age decay turned a harmful priority into a helpful one (+46% to +367% on three tasks, +18% on AIME). An age cap of 10 vs 30 moved pass from 32.35 to 27.34. A short window moved 34.1 to 30.9. Learned utility re-ranking moved CSR 0.699 to 0.798. Event-driven memory moved accuracy about 10 pp at 33% fewer tokens. Dependency search moved stale-belief accuracy 55.2% to 68.0%. LLM-rated importance moved nothing relative to recency.

**What LLMs do not do.** Nothing here shows a language model computing gain well. Self-localisation of the first wrong step overshoots about half the time (d22). The model's own "stuck" signal is unreliable (SCHEMA S6, r=.17).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the agent's stored subgoals and notes.

### Add now (established, [E])

1. **Always run a uniform or random-order control against any priority rule, at equal tokens, and report where priority loses.** Part: G7. [E] K10 (b12, b13, b14, d13, d20). Reason: priority was worse than uniform in several settings.
2. **Do not hard-code revisit direction.** Let the score decide. Part: memory/O. [E] K08 (a16, d26, b21). Forward majority in one design, before/after split in another.
3. **Keep a quota for rarely used or untried subgoals so a need-ordered queue does not starve them.** Part: memory. [E] K07 (a18, a20, b08, a16); starvation also seen in Fatemi and Schaul (c25, a12).
4. **Never use recency or need alone as the only ordering signal without a gain-type control.** Part: memory. [E] K02 (a17, a27, a28, b05): the empirical signal is in gain. Caution: this is rat and human evidence. As a rule for LLMs it is a hypothesis until the tests below pass, so we add only the "no ordering without a control" part now.
5. **Never compute need or relevance with information from the future question or answer.** Part: memory. [S] K28 (d21: 0.979 oracle vs 0.286 blind). Design hygiene, not an effect claim; listed here because it is logically required.

### Test first (not yet established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Order stored subgoals by gain x need proxies vs recency vs random | memory | [S] K01, K17 | a01, a02, d09, d20, d21 |
| T2 | Gain-only vs need-only vs product ordering | memory | [E] in biology, untested in LLMs | a28, b05, c04 |
| T3 | After a failure or changed fact, revisit upstream steps backward from the change point vs forward re-read | O (credit assignment), S5 | [E] in biology (K03); [S] for agent (K24, K25) | a17, b25, c03, d22 |
| T4 | Trigger revisit only when new evidence changes a stored item's value, vs always revisit | memory (consistent with G1) | [S] K04 | a24, a25, b06 |
| T5 | Event-driven reset of priorities of dependants vs time decay | memory | [S] K20, K26, K27 | d08, d23, d24, d25 |
| T6 | Score a subgoal with its dependants (non-myopic gain) vs single-item gain | memory | [S] K21, K26 | d19, d23, d24, d30 |
| T7 | Gain proxies (self-rated chance the plan changes, logprob shift, critic score, dependency count), correlated with measured benefit | memory | [S] K16, K19 | d09, d10, d11, d21 |
| T8 | Keep fresh derivations beside replayed ones, with an age cap | memory | [S] K12 | a31, d20 |
| T9 | Per-type decay (slow for plans and goals, fast for scratch notes) | memory | [S] K29 | d25, d28 |
| T10 | Learned outcome Q re-ranking of retrieved subgoals across repeated tasks | memory | [S] K18 | c13, d09 |
| T11 | Start any imagined continuation from a verified state, cap its depth, check against real feedback | G2, G3 | [S] K22 | d12, d13, d32 |
| T12 | Revisit the option the agent currently disfavours, or the last failed subgoal | memory | [C] K06 | a23, b04, d01, d02 |

Notes: T11 extends G2 (already no revision from opinion alone). T4 is consistent with G1 (doubt only on a signal). The WMT package (d24) can be reproduced whole in our harness first, then ablated piece by piece.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, including setup and scoring cost (G7). Report mean and spread over at least 3 seeds. Always include a random-order arm and a recency-order arm. "Item" means a multi-step reasoning item with a stored list of subgoals or partial results the agent can revisit, and a code-checkable answer.

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Multi-step items with 6 to 12 stored subgoals and budget to revisit only 3 | (a) gain x need from a cheap proxy; (b) recency; (c) random; (d) gain only; (e) need only | Final answer accuracy at equal tokens | Gain-based arms beat recency and random by a few points if the proxy has any validity; gain-only close to the product (from K02) |
| B2 | Planted-error items: a wrong intermediate fact is revealed late | (a) backward revisit from the change point; (b) forward re-read from the start; (c) random step | Accuracy after repair; tokens to repair | Backward wins if credit assignment helps. SRPO suggests targeted revisit beats random (28.7% vs 16.3% Pass@4 for clean prefix) |
| B3 | Changed-fact items: a later message invalidates a stored belief, directly or through a dependency (STALE-style) | (a) dependants-first; (b) recency-first; (c) time decay; (d) event reset | Accuracy on direct and propagated cases | Dependants-first and event reset beat recency on propagated cases. STALE: best plain 55.2% vs 68.0% with dependency search |
| B4 | Items as B1 with a distractor-heavy list | (a) priority with quota for untried items; (b) priority without quota; (c) uniform | Accuracy; share of untried items ever visited | Quota prevents starvation, small cost on easy items |
| B5 | Proxy validation: for each item, measure the real benefit of revisiting it alone (change in answer quality) | Self-rated gain, logprob shift, critic score, dependency count, recency | Spearman correlation with real benefit | Self-rated likely near zero (d10); dependency count likely positive on B3 items |
| B6 | Mid-episode change: new evidence arrives half way | (a) time decay; (b) event-driven reset; (c) no decay | Accuracy after the change | Event reset beats time decay; both beat no decay (FreshPER direction) |
| B7 | Mixed fresh and replayed context | (a) replayed only; (b) fresh + replayed 50/50 with age cap; (c) fresh only | Accuracy at equal context tokens | Mixed beats replayed-only (K12); may tie fresh-only |
| B8 | Open-set items needing diverse subgoals | (a) top-score only; (b) score plus diversity penalty (inhibition of return) | Accuracy and number of distinct directions visited | Diversity penalty avoids collapse (K15 direction) |
| B9 | Repeated item families (cross-task memory) | (a) similarity only; (b) similarity + learned Q (lambda 0.5); (c) recency; (d) random | Accuracy over rounds | Q helps after enough rounds, no effect in round 1 (MemRL needs repeated tasks) |

## 9. What does not transfer, and why

- **Hippocampal sequence structure and ripple timing.** The 30 ms and 160 ms lags, place-cell decoding and ripple power are brain facts. Nothing in an LLM scaffold uses them.
- **The successor representation as a computed table.** Our subgoals are not a small tabular MDP. Exact need and gain require a known transition model and policy effect. The authors call the gain requirement "unrealistic" even for the brain (a02).
- **Training-time replay results.** FreshPER, advantage replay, DyJR, P2Value, Sun, SRPO and CodeIt change model weights. Our agent is a scaffold with a frozen model. These results show what a priority score does to a learner; they do not show the same gain at prompt time.
- **The 5-backup replay event.** A convenience for significance tests, not a design target.
- **Rat spatial tasks.** Tiny, deterministic and stationary; reward is food. Our items are open-ended with noisy partial results.
- **Atari numbers.** The median is over 49 games, and the mean is dominated by one game (Video Pinball). Do not copy +106% as an expected gain.
- **MemRL's learned Q.** It uses reward feedback over 10 epochs of repeated tasks. Inside one reasoning episode there is no such feedback.
- **Preplay and pessimal replay as design goals.** They show the brain breaks the pure model; they do not tell us to add noise.
- **Anxiety and rumination speculation.** Untested, clinical, no agent mapping (b19, d31).
- **KV-cache eviction.** MemDecay is about attention memory in tiny models, not note ordering.

## 10. Open questions

1. Does gain x need ordering of stored subgoals beat recency and random at equal tokens in a prompt-time scaffold? Nobody has run it (K17, K23).
2. Which cheap gain proxy predicts the real benefit of revisiting? Self-rated importance failed one retention test; no logprob-shift proxy has been tested.
3. After a changed fact, does backward revisit from the change point beat forward re-read in LLM multi-step tasks at equal tokens? SRPO and STALE do not compare direction.
4. Has Liu 2021 (N=29) been replicated with a larger sample or another task? None found among 128 citing records; the 2026 iEEG study is an extension (abstract only).
5. How fast should priority decay inside one reasoning episode, and does event reset beat time decay? No ablation exists.
6. Does scoring a subgoal together with its dependants beat single-item gain? WMT and STALE are suggestive; no ablation.
7. Is there an ordering ablation for P2Value or MemRL? Absent. Closed only for advantage replay (Yoo, training time).
8. How do LLM agents with prioritised self-simulation limit compounding error? Search found only listings (Imagine-then-Plan, GILP).
9. How far do the contested rat results (Gillespie; Carey; Tirole) limit a utility account once gain is estimated with forgetting?
10. Founding and recent papers still unopened in full: Foster and Wilson 2006, Gupta 2010, Jadhav 2012, Widloski 2022, journal Carey 2019, the Neuron 2026 iEEG body, Wimmer 2023, Diekmann 2023, Panahi 2024 full text, Moore and Atkeson 1993.
11. Does a replay score that treats good and bad news asymmetrically (the gain asymmetry) help an LLM revise beliefs, or only add noise?
12. Is the right unit for ordering a subgoal, a fact, or a whole branch? WMT scores branches; Mattar and Daw score single backups.

## 11. Sources

[V] = opened this run (full text or full page, per the evidence files). [M] = snippet, abstract or listing only.

**Theory and neuroscience**
- [V] Mattar and Daw (2018) Prioritized memory access explains planning and hippocampal replay. https://www.biorxiv.org/content/biorxiv/early/2018/05/20/225664.full.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620/
- [M] Moore and Atkeson (1993) Prioritized sweeping. https://doi.org/10.1007/BF00993104
- [M] Sutton (1991) Dyna; Peng and Williams (1993), as described in Mattar and Daw.
- [M] Foster and Wilson (2006) Reverse replay of behavioural sequences. https://doi.org/10.1038/nature04587
- [V] Diba and Buzsaki (2007) Forward and reverse hippocampal place-cell sequences during ripples. https://pmc.ncbi.nlm.nih.gov/articles/PMC2039924/
- [V] Davidson, Kloosterman and Wilson (2009) Hippocampal replay of extended experience. https://pmc.ncbi.nlm.nih.gov/articles/PMC4364032/
- [V] Karlsson and Frank (2009) Awake replay of remote experiences. https://pmc.ncbi.nlm.nih.gov/articles/PMC2750914/
- [M] Gupta et al. (2010) Hippocampal replay is not a simple function of experience. https://doi.org/10.1016/j.neuron.2010.01.034
- [M] Jadhav et al. (2012) Awake hippocampal sharp-wave ripples support spatial memory. https://doi.org/10.1126/science.1217230
- [V] Pfeiffer and Foster (2013) Hippocampal place-cell sequences depict future paths to remembered goals. https://pmc.ncbi.nlm.nih.gov/articles/PMC3990408/
- [V] Olafsdottir et al. (2015) Hippocampal place cells construct reward related sequences. https://pmc.ncbi.nlm.nih.gov/articles/PMC4479790/
- [V] Ambrose, Pfeiffer and Foster (2016) Reverse replay is uniquely modulated by changing reward. https://pmc.ncbi.nlm.nih.gov/articles/PMC6013068/
- [V] Momennejad et al. (2018) Offline replay supports planning in human RL. https://elifesciences.org/articles/32548
- [V] Liu, Dolan, Kurth-Nelson and Behrens (2019) Human replay spontaneously reorganizes experience. https://pmc.ncbi.nlm.nih.gov/articles/PMC6657653/
- [V] Carey, Tanaka and van der Meer (2019) preprint. https://www.biorxiv.org/content/10.1101/397950v1.full ; [M] journal version https://pubmed.ncbi.nlm.nih.gov/31427771/
- [V] Eldar, Lievre, Dayan and Dolan (2020) The roles of online and offline replay in planning. https://elifesciences.org/articles/56911
- [V] Liu, Mattar, Behrens, Daw and Dolan (2021) Experience replay is associated with efficient nonlocal learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC7610948/ ; preprint https://www.biorxiv.org/content/10.1101/2020.10.20.343061v1.full.pdf
- [V] Gillespie et al. (2021) Hippocampal replay reflects specific past experiences rather than a plan. https://pmc.ncbi.nlm.nih.gov/articles/PMC8497431/
- [M] Widloski and Foster (2022) Flexible rerouting of replay around barriers. https://doi.org/10.1016/j.neuron.2022.02.002
- [V] Gagne and Dayan (2022) Optimism and pessimism in optimised replay. https://pmc.ncbi.nlm.nih.gov/articles/PMC8809607/
- [M] Diekmann and Cheng (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10076035/
- [M] Wimmer, Liu, McNamee and Dolan (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC9963918/
- [V] Jensen, Hennequin and Mattar (2024) A recurrent network model of planning. https://pmc.ncbi.nlm.nih.gov/articles/PMC11239510/
- [V] Sagiv et al. (2025) Between planning and map-building. https://pmc.ncbi.nlm.nih.gov/articles/PMC12633763/
- [M] Trait anxiety and reward-related replay (Nat Commun 2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12381021/
- [V] Tirole, Duvelle and Bendor (2026 preprint) Time, but not reward, shapes replay-based episodic prioritization. https://www.biorxiv.org/content/10.64898/2026.06.10.731494v1.full
- [M] Human hippocampal ripples prioritize model-based learning (Neuron 2026). https://europepmc.org/article/MED/41962539
- [V] Annual Review of Neuroscience (2026) Planning in the Brain: It's Not What You Think It Is. https://pmc.ncbi.nlm.nih.gov/articles/PMC13224046/
- [M] Human hippocampal replay prioritizes weakly learned information (2018). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6156217/
- [M] Citation scans: https://europepmc.org/article/MED/34016753 ; https://europepmc.org/article/MED/30349103

**RL engineering**
- [V] Schaul et al. (2016) Prioritized Experience Replay. https://arxiv.org/pdf/1511.05952
- [V] Hessel et al. (2018) Rainbow. https://arxiv.org/pdf/1710.02298
- [V] Zhang and Sutton (2017) A deeper look at experience replay. https://arxiv.org/pdf/1712.01275
- [V] Fedus et al. (2020) Revisiting fundamentals of experience replay. https://arxiv.org/pdf/2007.06700
- [V] Sujit et al. (2023) ReLo. https://arxiv.org/pdf/2208.10483
- [V] Lahire et al. (2022) LaBER. https://arxiv.org/pdf/2110.01528
- [V] Jiang et al. (2021) Prioritized Level Replay. https://arxiv.org/abs/2010.03934
- [V] Wang et al. (2025) Prioritized Generative Replay. https://arxiv.org/abs/2410.18082
- [V] Janner et al. (2019) MBPO. https://arxiv.org/pdf/1906.08253
- [M] Panahi et al. (2024) Prioritized replay and generalization. https://arxiv.org/abs/2407.09702
- [M] Aubin et al. (2018) https://arxiv.org/abs/1802.05594 ; Brea (2017) https://arxiv.org/abs/1711.06677 ; Pham and Dam (2026) https://arxiv.org/abs/2609.06186
- [M] Andrychowicz et al. (2017) Hindsight Experience Replay. https://arxiv.org/abs/1707.01495

**Language-model studies**
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/pdf/2304.03442
- [V] Butt et al. (2024) CodeIt. https://arxiv.org/abs/2402.04858
- [V] Chen et al. (2025) P2Value. https://arxiv.org/pdf/2410.12236
- [V] Bae et al. (2025) Online Difficulty Filtering. https://arxiv.org/abs/2504.03380
- [V] Fatemi (2026) Prioritized Replay for RL Post-training. https://arxiv.org/abs/2601.02648
- [V] Sun et al. (2026) Difficulty-targeted selection and rollout replay. https://arxiv.org/pdf/2506.05316
- [V] Ma et al. (2026) FreshPER. https://arxiv.org/pdf/2604.16918
- [V] Yoo et al. (2026) Rollout-level advantage-prioritized replay. https://arxiv.org/pdf/2606.04560
- [V] Li et al. (2026) DyJR. https://arxiv.org/pdf/2603.16157
- [V] Samanta et al. (2026) SRPO and RRPO. https://arxiv.org/pdf/2605.25507
- [V] Zhang et al. (2026) MemRL. https://arxiv.org/pdf/2601.03192
- [V] Cao et al. (2026) ReMe. https://arxiv.org/abs/2512.10696
- [V] How memory management impacts LLM agents (2025). https://arxiv.org/abs/2505.16067
- [V] Feng et al. (2026) ExpHarness. https://arxiv.org/abs/2605.30712
- [V] APEX-EM. https://arxiv.org/abs/2603.29093
- [V] Trajectory-informed memory generation (IBM). https://arxiv.org/abs/2603.10600
- [V] Kang et al. (2026) OSL-MR. https://arxiv.org/pdf/2606.10616
- [V] Chen and Cheng (2026) Learning what to remember. https://arxiv.org/pdf/2606.12945
- [V] Wu et al. (2026) STALE. https://arxiv.org/pdf/2605.06527
- [V] Dao, Kathalkar and Eaton (2026) Weighted Memory Tree. https://arxiv.org/pdf/2608.20631
- [V] Matam and Kim (2026) MemDecay. https://arxiv.org/pdf/2607.10582
- [M] FOCUS, TTEL listings. https://arxiv.org/search/?query=%22credit+assignment%22+%22language+model%22+reasoning+step
- [M] Imagine-then-Plan and GILP listings. https://arxiv.org/abs/2601.08955
