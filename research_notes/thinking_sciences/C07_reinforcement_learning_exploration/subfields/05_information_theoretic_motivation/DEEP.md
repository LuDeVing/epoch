# Information-theoretic motivation: deep document

*Subfield C07.05 of reinforcement-learning exploration. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Evidence ids (a01, b07, d03 ...) point to the jsonl lines. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Information-theoretic motivation means choosing what to do next by an information measure, not by an outside reward. Four families matter.

- **Empowerment.** The channel capacity from the agent's actions to its later sensor states. In a deterministic discrete world it equals the log of the number of states the agent can reach (a01, K01). It scores how many different futures the agent can reliably cause.
- **Information gain (curiosity).** The expected drop in uncertainty about a hidden thing (world dynamics or a hypothesis) after seeing the result of an action. Lindley's formula: EIG(x) = H[p(theta)] - E[H[p(theta|y;x)]] (a24).
- **Predictive information.** Mutual information between the past and the future of a process (a22). Basis for curiosity-as-prediction theories (a23, not opened).
- **Active inference.** Pick policies by expected free energy, which splits into extrinsic value (reward) and epistemic value (information gain) (a19, a18).

Why it matters to our agent: S7 (SELECT) has a "discriminating test" step. When two rules still fit, run the one input where they differ. That is a probe choice problem. The literature gives a precise rule for it: pick the probe with the highest expected information gain over the live hypotheses. It also gives evidence on how badly a language model does this by feel.

The main practical result of this folder: **expected information gain computed by code over sampled hypotheses beats asking the model which probe is best** (K10, K12). Empowerment is a weaker, more contested tool.

## 2. History and theories in depth

**2.1 Empowerment (2005 to 2015).** Klyubin, Polani and Nehaniv (2005) defined empowerment as the channel capacity between actions and later sensor states (b28, not opened; read through Salge et al.). Salge, Glackin and Polani (2014) is the review that was opened (a01-a07).

- First demo: a 10x10 maze, 5 actions (4 moves and stay), 5-step lookahead. 5-step empowerment ran from 3.46 to 5.52 bits. Cells with the most reachable positions score highest, so the agent finds open areas and junctions with no goal (a02). Cost: 5^5 = 3125 action sequences per cell.
- Anthony et al. (2008): local n-step empowerment correlates with global closeness centrality in box-pushing grids and scale-free graphs. No coefficient given. It breaks down when the horizon does not reach the box (a03).
- Sensor evolution: a genetic algorithm evolved sensor layouts to maximise 4-step empowerment; a small cost per sensor stopped degenerate layouts (a04).
- Jung et al. (2011): Monte Carlo empowerment on a continuous pendulum. A greedy controller sampled 5 actuations and picked the one whose next state had the highest empowerment. The pendulum swung up and balanced with no reward. Other time steps and power limits gave cycling or resting at the bottom (a07).
- Known limits (a05, a06): with a long horizon or rich sensors, empowerment is flat (100-step horizon gives log 100 everywhere). It does not pursue an external goal; a low-empowerment goal state is not sought.

**2.2 Scalable estimators (2015 to 2026).**
- Mohamed and Rezende (2015): a variational lower bound on mutual information, learned by a net from pixels. Exact Blahut-Arimoto costs O(N K S^2). In rooms of 400 states or fewer, variational and exact landscapes matched (correlation 1.00, R2 0.90; K=5). Qualitative demos: movable box high, fixed box low; keys, lava walls, predator flight (a08, a09).
- Gregor, Rezende, Wierstra (2016) VIC: learn options by maximising mutual information between option and end state. Reward is log q(option|start,end) minus log p(option). On MNIST digit pairs, 4.6 nats = about 99.5 states of a maximum 100 (a10, a11). Hard to train; needed alternating fixed reward and fixed policy. Extrinsic transfer used a weight of 30 on a 15x15 four-room world (a12).
- Eysenbach et al. (2018) DIAYN: fixed uniform skill prior, reward log q(z|s) - log p(z), plus a policy entropy term (SAC, weight 0.1). VIC learns its prior and collapsed to a handful of skills (the "Matthew effect"); DIAYN kept many (a13, a14). One environment, authors' own comparison.
- Levy et al. (2024) latent-predictive empowerment (b21); Garg et al. (2026) offline empowerment (b22); Schneider et al. (2025) empowerment pretraining (b23); Kobayashi (2026) empowerment in best-of-N (b24). All small or task-dependent gains (see section 5).

**2.3 Information-gain curiosity.**
- VIME (Houthooft et al. 2016): bonus = KL between posterior over dynamics before and after a transition. Dynamics net: one hidden layer of 32 units, batch 5000. Naive exploration and L2 prediction error almost never reached the sparse goal (MountainCar, CartPoleSwingup, HalfCheetah, others). Curves only, no table (a15).
- Prediction error is not information gain. Burda et al. (2018) tested 54 environments (48 Atari). Inverse-dynamics features beat random features in 55% of Atari games. The "noisy TV" problem: an agent that controls a noise source rewards itself without progress (b25, a16).

**2.4 Active inference.**
- Sajid et al. (2021): reward is one more observation with a preference over it; with zero reward preference agents still explore through epistemic value (a19). Proponents' review, small tasks.
- Tschantz et al. (2020): deep active inference with ensemble and information gain. MountainCar solved optimally in one trial (25 episodes of at most 200 steps). Cup Catch: no benefit. Workshop paper, figures only (a20).
- Hafner et al. (2022): one KL-minimisation objective recovers max-entropy RL, empowerment, information gain, skill discovery and active inference by choice of target. Theory only (a17).
- Critique: Millidge, Tschantz, Buckley (2020) show expected free energy is not simply free energy in the future; the natural extension has an epistemic term of the opposite sign, which would discourage exploration (a18, b26). The epistemic term comes from a prior belief that the agent reaches preferred outcomes. Contested inside its own community (K08).

**2.5 Bayesian experimental design in LLMs (2023 to 2026).** The same Lindley formula, with a language model as hypothesis sampler and answer model: GATE (a26), UoT (a25), Active Task Disambiguation (b16), OPEN (c18), BED-LLM (a27), Shoot First (b13), CuriosiTree (c15), ASIG (b11). This is where the usable evidence is.

**2.6 Human data.** Brandle et al. (2023, c25, not opened) found empowerment contributes to exploration in Little Alchemy 2. Yiu et al. (2025) and Lidayan et al. (2025) add child and adult studies (section 3).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Empowerment equals log of reachable states in a deterministic world | 5-step maze: 3.46 to 5.52 bits; 5^5 = 3125 sequences | a01, a02 | [E] |
| Variational estimate matches exact in small worlds | Correlation 1.00, R2 0.90, rooms of 400 states or fewer | a08 | [E] |
| Empowerment flat at long horizon | 100-step horizon gives log(100) everywhere | a05 | [S] |
| VIC prior collapse vs DIAYN fixed prior | VIC: handful of skills; DIAYN: many (figure) | a14 | [S] |
| Information-gain curiosity solves sparse tasks; L2 prediction error does not | VIME curves on MountainCar, CartPoleSwingup, HalfCheetah | a15 | [E] |
| Prediction-error curiosity breaks on noise | 54 environments; inverse dynamics beat random features in 55% of Atari games | b25 | [E] |
| Deep RL empowerment bonus: weak | 4 sparse gridworlds, 10 runs; no significant time-to-success gap with all runs; significance (t=2.29, p=0.024, curiosity vs baseline) only after dropping a 1e7-frame outlier; empowerment vs baseline p about 0.46 and 0.27 | b19, c08 | [E] |
| Offline empowerment bonus helps some tasks | OGBench, 5 seeds: beat CRL on 5 tasks, par elsewhere; four older estimators failed; usable bonus range about one order of magnitude | b22 | [S] |
| Empowerment in best-of-N: task-dependent | IQM return Cheetah 264.47 random vs 280.97 E-BoN; Walker 300.59 vs 301.38 (H-BoN 313.68); Quadruped 438.57 vs 416.37 (random best) | b24 | [S] |
| Active inference one-trial MountainCar | Optimal in a single trial; Cup Catch no benefit | a20 | [S] |
| EIG question choice by code roughly doubles 20 Questions | +37.4 percentage points over prompting; 6 LLMs, 3 target sets, 100 targets each; never decreased. Mean over 18 cells: BED-LLM 70.7, Entropy 57.6, Split 55.4, Data-Estimation 42.2, CoT 39.5, Implicit Max 38.6, Prompt-Only 30.3, ICL Beliefs 26.8 | b07, d03 | [E] |
| Single-cell examples | Animals GPT-4o-mini: Prompt-Only 44, Split 78, BED-LLM 88. Celebrities Mistral-Large: 19, 63, 91. Llama-3.1-8B Animals: 8 to 63 | b07 | [E] |
| Ablation grid (Animals GPT-4o) | BED 93, Entropy 88, Data-est 70, ICL Beliefs 25, Implicit Max 70, CoT 62, Prompt-Only 45 | b08 | [E] |
| Entropy proxy loses to full EIG when answers are noisy | BED-LLM beat Entropy in 18 of 18 cells, gap 8 to 23 points (Celebrities Mistral-Large 91 vs 68); full EIG costs no extra calls | d03, d05 | [E] |
| Raw in-context beliefs break first | EIG on unfiltered in-context beliefs 26.8 vs Prompt-Only 30.3 (18-cell mean) | d06 | [E] |
| Soft targets shrink the gain | Film preference, 200 profiles, 10 films rated 1-5: Entropy no gain over Prompt-Only; BED-LLM boost clearest across model classes; size not extracted | b09, d05 | [E] |
| UoT: +38.1% average success (relative) | 5 datasets, 5 LLMs; Llama3-70B +46.6% = mean of per-cell relative gains (absolute about 10.1 points); GPT-4 troubleshooting 43.7 to 67.3 | a25, b05, d01 | [S] |
| UoT beats self-consistency over questions at equal tokens | About 4.6k tokens, GPT-4 closed set (20Q / diagnosis / troubleshooting): CoT-SC k=33 32.6/37.6/42.5; Adapted-ToT 33.8/85.1/60.3; pruned UoT 48.1/88.4/63.2 | d02 | [S] |
| Generic reasoning wrappers hurt question asking | CoT and PP below plain GPT-4 in 20Q closed set | b06 | [S] |
| Unaided GPT-4 on 20 Questions | About one third of entities found | b15 | [E] |
| Frontier models ask too many questions | 7 frontier models vs dynamic-programming oracle on 25-300 item tasks (numbers in figures) | b12 | [S] |
| Battleship: EIG lifts weak LMs | Llama-4-Scout F1 0.367 to 0.764; GPT-4o 0.450 to 0.782; GPT-5 alone 0.716; win rate 0.82-0.83 vs humans (N=42), 0.67 vs GPT-5 at 1% of cost | b13 | [S] |
| Battleship: question step alone is small | F1 +0.021 to +0.026 (Scout, GPT-4o); zero-EIG questions 18.5% to 0.2% (Scout), 14.6% to 1.2% (GPT-4o); GPT-5 no significant gain | d09 | [S] |
| Candidate count M | Best-of-M raises best EIG up to M about 10, reaching 94.2% of the 0.227-bit ceiling (eps 0.1, max EIG 0.531) | d09 | [S] |
| Hypothesis count N | At 10 hypotheses the rank of 5 candidates matched 85 (one game); defaults N>=15, M=15 (BED-LLM) or N=20, M=5 (Kobalczyk) | d04, d07 | [S] |
| Hypothesis diversity | Mutual-information score, diverse prompt vs vanilla: N=10 0.57 vs 0.46; N=20 0.58 vs 0.54; N=30 0.60 vs 0.58 | d07 | [S] |
| EIG-uniform beats EIG weighted by log-probs | 15 animals, 5 seeds; GPT-3.5, GPT-4o-mini; gap smaller for GPT-4o-mini | b16, d07 | [E] |
| Code clarification with execution oracle | HumanEval after 4 questions (base vs EIG, binary): GPT-3.5 70.8 to 85.6; Llama3-70B 78.8 to 87.5; Llama3-8B 53.0 to 65.8; GPT-4o-mini 79.6 to 81.5. APPS GPT-4o-mini 62.9 to 75.3. 48 tasks, 3 run seeds | d08 | [S] |
| Cost per turn | Implicit O(1); implicit-ToT O(M); EIG O(N+M+N*M); code O(N+M) | d07 | [E] |
| BED-LLM wall time (Qwen2.5-72B, Animals) | Prompt-Only 26-45 min; BED-LLM 2h30m; Data-Estimation 1d17h | d06 | [S] |
| DPO on EIG pairs | Llama-2-chat 7B S@1 (zero-shot / FT / DPO): INLG 56.7/46.6/68.9; Things 51.1/42.2/61.1; Celebrities 71.1/46.7/72.2. FT raised EIG yet lowered S@1 | b10 | [S] |
| RL with EIG reward (ASIG) | 7B success more than doubles; 14B only +4.2 (animals), +1.8 (plants); 25x to 36x cheaper than BED-LLM; MediQ 7B accuracy 46.7 to 47.6 | b11 | [S] |
| Preference questions: GATE | 388 participants, 3 domains; higher area under curve than supervised, pool-based active learning or user prompts; significant only in content recommendation and email validation | a26 | [S] |
| CuriosiTree | Llama-3.1-70B, 50 trials, lupus; deliberation-only and retrieval-only never correct; of 95 reasoning steps 84% kept top diagnosis and 62% of those lowered entropy; costs 1/1/2/3, lambda 0.1 | c15, d15 | [S] |
| LLMs explore badly in bandits | Only 1 of 48 (GPT-3.5, Llama2) / 72 (GPT-4) configs explored well; basic GPT-4 suffix failure in over 60% of replicates | c16 | [E] |
| GPT-3 horizon task | No directed exploration signature | c17 | [S] |
| Little Alchemy 2 | 720 elements, 500 trials: Llama-8B 9, Llama-70B 25, GPT-4o 35, human 42 (29,493 players), R1 85, o1 177 (t=9.71) | c01 | [S] |
| LLMs weight uncertainty, not empowerment | Temperature raised uncertainty weight (beta 2.911, z 7.44) not empowerment (beta 0.196, z 1.067, p 0.286). Empowerment signal peaks at layer 72; choice at layer 1 | c02, c03 | [S] |
| Prompting did not fix it | Engineered GPT-4o prompt: 43 vs 35 elements, t -1.17, p 0.304; steering no gain | c04, d10 | [S] |
| EELMA tracks agent performance | No CoT: Gridworld 0.19 to 0.01 bits (99%); Hanoi 0.29 to 0.09 (65%). 1600 and 800 trajectories | b02 | [S] |
| EELMA in WebArena | Spearman 0.83-0.94 in 3 domains, flat in Shopping; pooled 0.39 (N=16); tau-bench 0.71 (N=6); visitation entropy 0.16 / -0.71 | b03, b04, d11 | [S] |
| EELMA failure modes | 43/106 Qwen trajectories left the sandbox; tau-bench retail (3-7% pass) inverts; airline 0.59/0.71/0.74 for 1.5B/7B/32B | b03, d12 | [S] |
| Human empowerment preference | Study 1: 80 children, 120 adults; extra-small star 46.25% children, 80.83% adults vs chance 33% | b18 | [S] |
| Free play (Crafter) | 51 children recruited, 24 adults; exploration progress correlates with entropy and empowerment; information gain not consistent | c05, c06 | [C] |
| Goal statements and exploration | rho 0.8, p 0.005 unadjusted, N=10 children; goals 21% of child utterances vs 10% adult; labelled by gpt-3.5-turbo | c07, d13 | [C] |
| Goal-conditioning in ELLM | No significant gain; ELLM about 6 achievements vs 9 oracle; 64.9% of goals feasible | d14 | [S] |
| Empowering a human user | Pass@1 more than doubles (Llama-3.1-8B, 554 LiveCodeBench); 192% average gain over SFT; 18-person study 78% preferred (p 0.015); acceptance 8.08% vs 6.18% (p 0.0002) | c10, c11 | [S] |
| Multi-turn drop | 15 LLMs, 200,000+ conversations; -39% (abstract; caption -35%): aptitude -15%, unreliability +112%; SNOWBALL recovers 15-20% | d16 | [S] |
| Intrinsic reward in reasoning RL | GRPO on AIME 2024 up to 22.23% relative; training time 12.13h to 14.55h (Countdown-34) | c19 | [S] |
| Greedy EIG guarantees | (1-1/e) of best adaptive policy for fixed budget; ln Q + 1 for coverage; noiseless adaptive submodular only | d17 | [E] (theory) |

## 4. Mechanisms and models

**4.1 Empowerment, exact.** For each candidate action sequence of length n, find the distribution of final sensor states. Empowerment = max over action distributions of I(A^n; S_n). Compute by Blahut-Arimoto. In a deterministic world, count distinct reachable end states and take log2. Cost grows as |A|^n. A text agent can do the deterministic case by listing the distinct outcomes a probe could return.

**4.2 Empowerment, learned.** Train a policy q(a|s) and a decoder that predicts the action sequence from (start, end) state. The bound is I >= E[log q(a|s,s') - log p(a|s)]. VIC and DIAYN use this with an option or skill z. DIAYN: fix p(z) uniform, reward log q(z|s) - log p(z) plus entropy bonus. Do not learn the prior (VIC collapse, a14). Needs a training loop; not usable in a scaffold.

**4.3 Expected information gain for a probe (the part to implement).** Following BED-LLM (a27, d03-d06) and Active Task Disambiguation (b16, d07):

1. Sample N hypotheses (N about 10 to 20) from the model, each in a fresh call. Use a diversity prompt (d07).
2. Filter: keep only hypotheses that agree with every observation so far. Resample for up to about 3 cycles if too few remain (d04, d06).
3. Propose M candidate probes (M about 5 to 15).
4. For each probe and each hypothesis, get the predicted answer. For a code task, run the candidate programs on the probe input (cheap, near-noiseless; d08). For a language answerer, ask the model (N*M calls).
5. Weight hypotheses uniformly (EIG-uniform beat log-prob weighting; b16).
6. Score the probe: EIG = H[answers marginal] - E_h[H[answer | h]]. With deterministic answers, group hypotheses by predicted answer and take the entropy of the group sizes.
7. Choose argmax. Ask or run it. Update by filtering; repeat.

With a noisy answerer modelled as a binary symmetric channel of rate eps, EIG = Hb(eps + (1 - 2 eps) p) - Hb(eps), where p is the predicted probability of "yes" (d09). If eps is the same for all probes, ranking by marginal entropy equals ranking by EIG (derivation, d09). They differ only when noise differs by probe: crashing code, unreliable tools. Then use full EIG (K13).

**4.4 Uncertainty of Thoughts (UoT).** The planner simulates answers to candidate questions for up to three steps and scores each branch by information gain over the possibility set, and propagates reward up the tree (a25). Pruned UoT runs at about 4.7k tokens, close to CoT-SC k=33 at 4.6k (d02). Works on closed sets.

**4.5 Stopping rule (weak).** Only CuriosiTree gives one: utility = information gain minus lambda times cost (lambda 0.1), stop when the top class probability passes a threshold or the cost budget runs out (d15). Theory covers noiseless cases only (d17). Proposed rule for us (not tested): stop when best EIG per token falls below the expected value of one more reasoning step, or when the leading hypothesis passes a set probability.

**4.6 Empowerment as a monitor (EELMA).** Train an encoder over text states, estimate the mutual information between action text and future state text, over many trajectories (estimates stabilise near 50% of the data; b01). Needs a trained estimator, so not cheap (d11).

**4.7 Active inference loop.** Policy score G = - (expected extrinsic value) - (expected epistemic value). Reduces to EIG per token cost in the one working LLM usage (b12). Use the information-gain term only (K08).

## 5. What holds up

**Holds up (several sources):**
- Explicit EIG by code beats LLM judgement of the best probe. BED-LLM 70.7 vs Implicit Max 38.6 on the same candidates; UoT, Active Task Disambiguation, Shoot First agree on direction (K10, K12).
- Filtering hypotheses against all observations is required. Unfiltered in-context beliefs scored 26.8, below Prompt-Only 30.3 (K27).
- Full EIG beats entropy proxy when noise differs. 18 of 18 cells (K13).
- Uniform hypothesis weights beat model log-probs (K14).
- Prediction-error curiosity fails on noise; information-gain based bonuses do not (K06).
- Empowerment is an exploration prior, not a goal objective (K03).
- Off-the-shelf LLMs explore badly unless summaries are computed outside the model (K22). Only 1 of the bandit configurations worked.
- Multi-turn context hurts probing: models answer early and lean on earlier wrong attempts (K27, d16).

**Failures and weak results:**
- Empowerment in deep RL: Massari et al. found no significant difference with all runs kept (b19). Significance came after removing one outlier, with one-sided t-tests. Empowerment-inspired reward only matched a VAE curiosity reward. Later work is small or mixed: PPO no clear gain (b23); E-BoN best on 1 of 3 tasks (b24); offline bonus helps 5 of many tasks and is fragile (b22).
- Four earlier offline empowerment estimators failed to recover a usable map (DADS saturates at log K; DV-empowerment unbounded; b22).
- Plain fine-tuning on optimal questions raised EIG but lowered success in all three sets (b10).
- High EIG did not always give better play for weak models (d09).
- Active-inference expected free energy: derivation contested (K08).
- Goal-statement finding: r 0.8 on N=10, unadjusted p, LLM-labelled; ELLM found no goal-conditioning gain (K21).
- Position papers on LLMs and active inference give no data (K25).

**Moderators:**
- Model strength. Gains shrink for strong models: GPT-4o-mini vs GPT-3.5 in 20Q (b16); GPT-4o-mini HumanEval +1.9 points binary (d08); GPT-5 in Battleship no significant gain (d09); 14B ASIG +1.8 to +4.2 (b11).
- Target type. Concrete entities gain most; soft profiles gain less (b09).
- Answer noise. Zero with code execution (d08); matters for language answerers.
- Task coverage. Almost all LLM EIG results are closed-set 20-Questions style with 100 targets or fewer per cell.
- Same model as questioner and answerer may inflate the gain (BED-LLM boost clearest across model classes; d05 hints at agreement).

**Interventions that worked:**
- Code computes EIG; the model only samples and answers (b07).
- Execution oracle for code tasks (d08).
- Externally summarised history for bandits (c16).
- Moving the EIG computation to a cheap selector, so a small model plus selector beats a larger plain model at 1% of the cost (b13).
- Larger candidate set M up to about 10 (d09).

**Interventions that did not work:**
- Asking the model to name the most informative question (b08).
- CoT-style wrappers for question asking (b06).
- Verbal prompt advice to explore (Little Alchemy 2, p 0.304; c04, d10).
- Feature steering on LLaMA3.1-70B (c04).
- Temperature (raised uncertainty weight, not empowerment; c02).
- Weighting by log-probs (b16).

## 6. Language models

**20 Questions and diagnosis (closed sets).**
- Unaided GPT-4 finds about one third of entities (b15).
- Prompt-Only mean 30.3% over 18 BED-LLM cells; BED-LLM 70.7%; +37.4 points (d03, b07).
- UoT +38.1% relative; do not compare with +37.4 points (d01).
- Matched tokens (about 4.6k, GPT-4): pruned UoT 48.1/88.4/63.2 vs CoT-SC k=33 32.6/37.6/42.5 (d02). The SC voted on the next question, not on the final answer.
- DPO on EIG pairs lifts a 7B model (b10); RL with EIG reward does too, with weak transfer (b11).

**Games.** Battleship (b13, d09): Scout F1 0.367 to 0.764 with the full module set; the question step alone adds +0.021 to +0.026. Guess Who +28.3 to +42.4 points. Spotter accuracy +14.7 points (Claude 4 Opus 86.8 to 94.4; GPT-4.1 75.2 to 90.9), but this used code generation, not EIG alone. LMs ask low-value questions: Scout 62.2% SpotterQA accuracy vs humans 92.5%; complex questions 72.8% to 60.4% (b14).

**Code and clarifying questions.** EIG over sampled programs raises HumanEval and APPS accuracy after four questions (d08, c14). No token-matched baseline exists.

**Diagnosis.** CuriosiTree: greedy EIG-per-cost action choice beats random and self-evaluation in a simulated lupus case (c15). One diagnosis, 50 trials.

**Exploration.** Bandits: only one configuration explored well (c16). Little Alchemy 2: only o1 (177) and R1 (85) beat humans (42) (c01). Most models weight uncertainty and under-use empowerment; verbal prompting and steering did not help (c04, d10). The empowerment weights come from a net fitted to human data (Brandle et al.), not a true mutual-information estimate (c02).

**Empowerment of an LM agent as a measure.** EELMA (b01-b04, d11, d12). Aggregate correlation only; fails at floor performance and when agents leave the task.

**Training with an intrinsic reward.** IMAGINE: up to 22.23% relative on AIME 2024 GRPO (c19). Training only.

**Multi-turn.** Performance falls with underspecified multi-turn chat: aptitude -15%, unreliability +112%, SNOWBALL recovers 15-20% (d16). Probe-selection code should restate the live hypothesis set at each step.

**What changed behaviour, by how much (ranked).** Code-side EIG: +37.4 points. Hypothesis filtering: 26.8 to 70.7 (largest single component). Full EIG over entropy: +13 points. Model-judged best probe: +8 points over prompting. CoT: +9 points. Verbal exploration advice: no significant change.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| In the S7 discriminating test, score candidate probes by expected information gain computed in code over sampled hypotheses. Do not let the model rate which probe is most informative. | S7, G5 | [E] | K10, K12; b07, b08, d03, c13 |
| Filter every sampled hypothesis against all observations so far before scoring. Restate the live set each step. | S7, G2 | [E] | K27; d06, d16 |
| Weight hypotheses uniformly, not by model log-probabilities. | S7 | [E] | K14; b16, d07 |
| Where probes have unequal noise (tool output, code that may fail), use full EIG, not predictive entropy. | S7 | [E] | K13; d03, d05, d09 |
| Prefer information gain to surprise or novelty as a probe criterion. | S7 | [E] | K06; b25, a15, a16 |
| Treat any empowerment-style option count as an exploration prior only; once a goal is set, switch to goal value. | S7, S6 | [E] | K03; a06, c09 |
| Give probe selection externally computed summaries (counts, per-option averages), not raw history. | S7, memory | [E] | K22; c16, d16 |
| Do not use debate or generic reasoning wrappers for probe choice (agrees with G9, G10). | G | [E] | b06, b08 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| EIG probe selection beats self-consistency on the FINAL answer at equal tokens, on open reasoning items. | S7 | [S] | K11, d02; gap 1 |
| About 10 to 15 diverse hypotheses and 5 to 10 candidate probes are enough. | S7 | [S] | K26; d04, d07, d09 |
| Code-execution probes: run sampled candidate programs on a sampled input, score by output split. | S4, S7 | [S] | K28; d08 |
| Consistency filter ablation. | S7, G2 | [E] mechanism, [S] on our items | K27 |
| Stopping rule on EIG per token. | S7, G7, G12 | [C] | K29; d15, d17 |
| Computed option-count hint at open-mode probe choice. | S6, S7 | [S] | K18; c02, d10 |
| EELMA-style or cheap trace statistic as a failure monitor. | G | [S] | K19, K30; b02, d11, d12 |
| Goal-stating step before exploratory probes. | S6 | [C] | K21; c07, d13, d14 |
| Small model plus EIG selector against larger plain model at equal cost. | S0, S7 | [S] | K16; b13 |

## 8. Concrete tests on our bench

All arms get the same total token budget, counting hypothesis sampling, candidate generation and scoring calls. Setup cost counts (G7).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with two rules both fitting the examples (ARC-style, code spec ambiguity) | (a) model picks the discriminating test; (b) EIG over N=12 sampled rules, M=6 probes; (c) the same tokens spent on extra independent attempts + vote | Final correct rate; probes to resolution | (b) above (a) by 5 to 15 points. (b) vs (c) unknown; the open gap. |
| T2 | 20-Questions-style hidden-rule items (own, 100 or fewer) | Prompt-only, Implicit Max, Entropy, full EIG; all with filter | Success at 20 questions | Reproduce about 70 vs 30; check weaker gain for strong models. |
| T3 | Code items with an executor | EIG split on sampled program outputs vs sampling the same number of extra programs and voting | Pass rate on held-out tests | Gain 2 to 12 points, smaller for strong models (d08). |
| T4 | Same T1 items | Filter on vs filter off | EIG probe quality, final accuracy | Filter off drops below prompt-only (K27). |
| T5 | Items where tool output is noisy | Entropy vs full EIG with per-probe noise estimate | Final correct rate | Full EIG ahead when noise differs by probe. |
| T6 | T1 items | N in {5, 10, 20, 40} and M in {3, 6, 10} | Argmax stability against N=40; accuracy per token | Plateau near N=10 to 15, M=10 (K26). Gives the missing token-cost curve. |
| T7 | Soft-target items (open design, preference-like) | EIG vs prompt-only | Judge score by running checks, not model opinion (G8) | Little or no gain (b09). Also tests a runtime softness detector. |
| T8 | Open-mode exploration items | Uncertainty-only vs uncertainty + computed option count per candidate | Distinct valid outcomes found | Small gain; contested. |
| T9 | Our own traces | Cheap trace statistics vs empowerment estimate for per-run failure prediction | AUC | Cheap statistics probably match. |
| T10 | T1 items | Stop rule: EIG per token threshold vs fixed 4 probes | Accuracy per token | Fewer probes, same accuracy. |

## 9. What does not transfer, and why

- **Variational empowerment estimators, VIC, DIAYN.** They need a training loop over many episodes. A scaffold cannot train.
- **Empowerment bonuses as RL rewards.** Gains over curiosity are weak and fragile in deep RL (K05). We do not train.
- **Active inference expected free energy.** Contested derivation; practice reduces to EIG per cost (K08). Use the plain term.
- **Training LLMs on EIG labels (DPO, RL, IMAGINE).** Out of scope. A scaffold supplies the EIG calculation instead (K17, K24).
- **Empowering a human user (Ellis et al.).** The agent is solo. Design analogy only (K20).
- **Human child studies.** Behavioural, small, and not about LLM scaffolds (K21).
- **20 Questions numbers.** Closed sets, an LLM answerer, 100 targets per cell. Open reasoning probes may differ. Treat 70 vs 30 as the upper bound.
- **Hand-set costs.** CuriosiTree costs (1, 1, 2, 3) are arbitrary.
- **UoT 38.1%.** Relative gain, averaged over cells. Not comparable with percentage points (d01).

## 10. Open questions

1. At equal total tokens, does EIG probe selection beat self-consistency on the final answer, on open reasoning tasks? (Gap 1.)
2. What is the token-cost curve for the number of hypotheses and candidates? (Gap 2.)
3. Where does the entropy proxy fail with mixed-reliability tools? Untested. (Gap 3.)
4. Does a computed option-count hint help? Only verbal advice was tested (GPT-4o, p 0.304). (Gap 4.)
5. Can empowerment from our own traces predict per-run failure? Only aggregate correlations exist (N=16, N=6). (Gap 6.)
6. Do the goal-statement results replicate in larger samples, and does a goal-stating step help an LLM? (Gap 7.)
7. Which long-context failure comes first: poor hypothesis sampling, miscalibrated answer model, or ignoring history? The hypothesis set breaks first on current evidence; contexts were 20 turns or less. (Gap 8.)
8. How do we detect at runtime that a task is soft? (Gap 9.)
9. What is the right stopping rule? (Gap 10.)
10. Is part of the 20Q gain due to questioner and answerer agreeing? (d05)
11. The UoT gaps 33.8, 29.9, 28.3 were not recomputed; they are very probably relative too.
12. Brandle et al. (2023) and Klyubin et al. (2005) were not opened. The human Little Alchemy 2 basis for empowerment weights is second-hand.

## 11. Sources

[V] = opened this session (full text). [M] = snippet or citation only.

| Id | Source | Mark | URL |
|---|---|---|---|
| a01-a07 | Salge, Glackin, Polani (2014) Empowerment: an introduction | [V] | https://arxiv.org/pdf/1310.1863 |
| a08, a09 | Mohamed and Rezende (2015) Variational information maximisation | [V] | https://arxiv.org/pdf/1509.08731 |
| a10-a12 | Gregor, Rezende, Wierstra (2016) Variational intrinsic control | [V] | https://arxiv.org/pdf/1611.07507 |
| a13, a14 | Eysenbach et al. (2018) DIAYN | [V] | https://arxiv.org/pdf/1802.06070 |
| a15 | Houthooft et al. (2016) VIME | [V] | https://arxiv.org/pdf/1605.09674 |
| a16 | Burda et al. (2018) Random network distillation | [V] | https://arxiv.org/pdf/1810.12894 |
| a17 | Hafner et al. (2022) Action and perception as divergence minimization | [V] | https://arxiv.org/pdf/2009.01791 |
| a18, b26 | Millidge, Tschantz, Buckley (2020) Whence the expected free energy? | [V] | https://arxiv.org/pdf/2004.08128 |
| a19 | Sajid, Ball, Parr, Friston (2021) Active inference: demystified and compared | [V] | https://arxiv.org/pdf/1909.10863 |
| a20 | Tschantz et al. (2020) Reinforcement learning through active inference | [V] | https://arxiv.org/pdf/2002.12636 |
| a21 | Tschantz et al. (2020) Scaling active inference | [M] | https://arxiv.org/pdf/1911.10601 |
| a22 | Bialek, Nemenman, Tishby (2001) Predictability, complexity and learning | [V] | https://arxiv.org/pdf/physics/0007070 |
| a23 | Still and Precup (2012) Information-theoretic curiosity-driven RL | [M] | https://link.springer.com/article/10.1007/s12064-011-0142-z |
| a24 | Lindley (1956) expected information gain (formula read in BED-LLM; original not opened) | [M] | https://arxiv.org/pdf/2508.21184 |
| a25, b05, b06, d01, d02 | Hu/Wang et al. (2024) Uncertainty of Thoughts | [V] | https://arxiv.org/abs/2402.03271 |
| a26 | Li et al. (2023) GATE | [V] | https://arxiv.org/pdf/2310.11589 |
| a27, a28, b07-b09, c12, c13, d03-d06 | Choudhury, Bickford Smith et al. (2026) BED-LLM | [V] | https://arxiv.org/abs/2508.21184 |
| b01-b04, d11, d12 | Song, Gore, Kleiman-Weiner (2025/26) EELMA | [V] | https://arxiv.org/abs/2509.22504 |
| b10 | Mazzaccara, Testoni, Bernardi (2024) DPO and EIG | [V] | https://arxiv.org/abs/2406.17453 |
| b11 | Hartmann et al. (2026) ASIG | [V] | https://arxiv.org/abs/2607.03426 |
| b12 | Dutta, Ramachandran, Sra (2026) Active inference as context acquisition | [V] | https://arxiv.org/abs/2608.19202 |
| b13, b14, d09 | Grand et al. (2026) Shoot First, Ask Questions Later? | [V] | https://arxiv.org/abs/2510.20886 |
| b15 | Zhang, Lu, Jaitly (2024) Multi-turn planning via 20 Questions | [V] | https://arxiv.org/abs/2310.01468 |
| b16, c14, d07, d08 | Kobalczyk et al. (2025) Active Task Disambiguation | [V] | https://arxiv.org/abs/2502.04485 |
| b17 | Piriyakulkij, Kuleshov, Ellis (2024) Active preference inference | [V] first page only | https://arxiv.org/abs/2312.12009 |
| b18 | Yiu et al. (2025) Empowerment gain and causal model construction | [V] | https://arxiv.org/abs/2512.08230 |
| b19, c08, c09 | Massari et al. (2021) Empowerment may drive exploration | [V] | https://arxiv.org/abs/2107.07031 |
| b20 | Kumar (2018) Empowerment-driven exploration | [V] | https://arxiv.org/abs/1810.05533 |
| b21 | Levy, Allievi, Konidaris (2024) Latent-predictive empowerment | [V] abstract-level | https://arxiv.org/abs/2410.11155 |
| b22 | Garg et al. (2026) Offline empowerment | [V] | https://arxiv.org/abs/2610.24461 |
| b23 | Schneider et al. (2025) Empowerment policy pre-training | [V] | https://arxiv.org/abs/2510.05996 |
| b24 | Kobayashi (2026) Flexible empowerment, extended best-of-N | [V] | https://arxiv.org/abs/2604.15614 |
| b25 | Burda et al. (2018) Large-scale study of curiosity | [V] | https://arxiv.org/abs/1808.04355 |
| b27, c23 | Kulveit et al. (2023) Predictive minds | [V] | https://arxiv.org/abs/2311.10215 |
| b28 | Klyubin, Polani, Nehaniv (2005) Empowerment | [M] | none recorded |
| b29 | Friston et al. (2015, 2017) Active inference and epistemic value | [M] | none recorded |
| b30 | Ruggeri and Lombrozo (2015) Children's efficient search | [M] | none recorded |
| c01-c04, d10 | Pan, Xie, Wilson (2025) LLMs think too fast to explore | [V] | https://arxiv.org/abs/2501.18009 |
| c05-c07, d13 | Lidayan et al. (2025) Intrinsically motivated humans and agents | [V] | https://arxiv.org/abs/2503.23631 |
| c10, c11 | Ellis et al. (2025) Training LLM agents to empower humans | [V] | https://arxiv.org/abs/2510.13709 |
| c15, d15 | Cooper et al. (2025) The Curious Language Model | [V] | https://arxiv.org/abs/2506.09173 |
| c16 | Krishnamurthy et al. (2024) Can LLMs explore in-context? | [V] | https://arxiv.org/abs/2403.15371 |
| c17 | Binz and Schulz (2023) Cognitive psychology of GPT-3 | [V] | https://arxiv.org/abs/2206.14576 |
| c18 | Handa et al. (2024) OPEN | [V] | https://arxiv.org/abs/2403.05534 |
| c19 | Gao et al. (2026) IMAGINE | [V] | https://arxiv.org/abs/2505.17621 |
| c20 | LLM-driven intrinsic motivation for sparse reward RL (2025) | [V] | https://arxiv.org/abs/2508.18420 |
| c21 | Wen (2025) The missing reward | [V] | https://arxiv.org/abs/2508.05619 |
| c22 | Prakki (2024) Active inference for self-organizing multi-LLM systems | [V] | https://arxiv.org/abs/2412.10425 |
| c24 | Demircan et al. (2024) SAEs reveal TD learning in LLMs | [M] | https://arxiv.org/abs/2410.01280 |
| c25 | Brandle et al. (2023) Empowerment in Little Alchemy 2 | [M] | https://doi.org/10.1038/s41562-023-01661-2 |
| d14 | Du et al. (2023) ELLM | [V] | https://arxiv.org/abs/2302.06692 |
| d16 | Laban et al. (2025) LLMs get lost in multi-turn conversation | [V] | https://arxiv.org/abs/2505.06120 |
| d17 | Golovin and Krause (2011/2017) Adaptive submodularity | [V] statements, not proofs | https://arxiv.org/abs/1003.3967 |

Caveats on the record: several 2026 items are preprints without peer review (b11, b13, b22, b24, c12, c19). WebSearch was exhausted during gap search, so papers not reached by citation chains may be missing.
