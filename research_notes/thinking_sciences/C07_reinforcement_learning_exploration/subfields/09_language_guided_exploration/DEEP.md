# Language-guided exploration: deep document

*Subfield C07.09. Written from evidence_a-d.jsonl (a01-d18), claims.jsonl (K01-K34) and critique.md in this folder. Evidence ids are quoted as a01, d06 and so on. Claim ids as K02. Status marks: [E] established (two or more independent papers), [S] single source, [C] contested. "Independent" is counted by paper and lab, not by evidence line: several lines cover the same paper.*

*Links to parallel subfields (not covered here): Epistemic value and curiosity; Search over thoughts; Tree of Thoughts; Language Agent Tree Search; Analogical prompting for LLMs; Compression at inference time; Calibration and overconfidence; Novelty measurement. Earlier siblings in C07: 01 bandits, 03 count-based, 05 information-theoretic, 07 novelty search, 08 Go-Explore and archives.*

## 1. What it is

Classic exploration in reinforcement learning (RL) is blind. The agent is pushed toward states that are new, surprising or rarely visited. Count bonuses, RND, NGU and APT are of this kind. They have no idea which new things are worth the effort. A random pixel pattern is new. Chopping the 400th tree is new in a sense too.

Language-guided exploration adds a language model as a source of prior knowledge about what is sensible to try. The model reads a text description of the situation and says what is plausible, useful or interesting. That output is then used in one of five ways.

1. **Goal suggestion.** The model proposes goals; the agent is rewarded for reaching them (ELLM, a01).
2. **Preference reward.** The model ranks pairs of events; a reward model is distilled from the ranks (Motif, ONI, a14, a17).
3. **Interestingness filter.** The model judges which learnable tasks are also worth learning (OMNI, a07).
4. **Curriculum or next-task proposal.** The model proposes the next task given what the agent can and cannot do (Voyager, OMNI-EPIC, a11, a10).
5. **Search control.** The model picks which stored state to return to and which action to try there (Intelligent Go-Explore, c18).

A sixth family writes reward code (Eureka, Text2Reward). It needs a simulator and does not apply to us (K18).

A seventh strand tests the model as the explorer itself, with no RL training. These are the bandit and game studies (Krishnamurthy, EVOLvE, Schmied, Pan, BALROG). They find that unscaffolded models explore badly. That strand motivates scaffolds.

**Why it matters for our agent.** Our schema has a generation state, S3, where the agent produces attempts. In open mode, code keeps a history of directions tried and assigns untried ones. The question here: should the model itself be asked "what is worth trying here", and what must surround that question so it does not hurt? The research answers in a hedged way. The prior helps over pure novelty in game worlds the model knows. It produces roughly a third unusable suggestions. It needs an external check, a novelty tie-break, and a record of what was tried. Nobody has tested it on an open-answer reasoning task at equal tokens. That is the main gap.

**Scope warning.** Almost every positive result is in game worlds (Crafter, Minecraft, NetHack, BabyAI, Atari) that the model knows well, and most needed RL training or an environment reward. Only Voyager and Intelligent Go-Explore are prompt scaffolds, and Voyager used 3 runs. No paper reports tokens per success.

## 2. History and theories in depth

### 2.1 Roots
- **Intrinsic motivation in RL.** Count-based bonuses, prediction-error curiosity (RND), episodic novelty (NGU) and entropy bonuses (APT) reward newness. They fail on the "noisy TV" problem: a source of random change looks endlessly new. They also chase what is new, not what is useful. Siblings 01, 03, 05 cover these.
- **Go-Explore and novelty search.** Archives of interesting states and open-ended search (siblings 07, 08). Language-guided variants replace hand-made "interesting" heuristics with a language model.
- **Language models as world knowledge.** SayCan (Ahn et al. 2022, a13) had a model propose steps and a learned value function filter them for feasibility. The idea that the model proposes and something else disposes recurs in every later paper.

### 2.2 The founding works (2022-2023)
- **SayCan (2022).** 101 instructions, PaLM 540B. Mock kitchen: plan success 84%, execution 74%. Real kitchen: planning drops 3 points, execution drops 14 (a13, b20). Proposals are cheap; feasibility is where the loss is. Needs trained affordance value functions per skill.
- **ELLM, Du et al. (2023) [V].** The founding study for "LLM suggests plausible useful behaviours". In Crafter, a model sees a captioned state and suggests goals; the agent gets reward when its behaviour matches a suggestion by sentence-embedding similarity. Pretraining reaches about 6 achievements per episode. Oracle with true rewards: about 9. RND, APT, Novelty: under 3 (a01, c02).
- **GLAM, Carta et al. (2023).** A different route: the LLM is the policy, fine-tuned with PPO. Learns BabyAI-Text fast (0.8 success after 250k steps) but generalises poorly to new objects and tasks (a23, b22).
- **OMNI, Zhang et al. (2023).** Learning progress (LP) is drawn to tasks that are learnable but boring. A model of interestingness (MoI) built from an LLM filters them. In Crafter, 82 tasks learned versus 55 for LP and 4 for uniform (a07, b05).
- **Voyager, Wang et al. (2023).** GPT-4 proposes the next task from state and history in Minecraft, writes code skills, and verifies. 63 unique items in 160 iterations, 3.3x the baselines (a11).
- **Motif, Klissarov et al. (2023).** Llama 2 70B ranks pairs of NetHack messages; a reward model is distilled. Intrinsic reward alone beats the score-trained agent on the score task (a14, b11).
- **SPRING (2023).** GPT-4 reads the Crafter paper and plays by answering questions: 27.3% vs DreamerV3 14.5%, but one wrong fact about the crafting table costs 24% (b21).
- **Eureka and Text2Reward (2023).** Reward code from LLMs: 83% of 29 tasks beat expert human reward (Eureka), 13 of 17 manipulation tasks (Text2Reward) (a27, b18, b19).

### 2.3 Consolidation (2024-2026)
- **Bougie and Watanabe, iLLM (PMLR v260, 2025) [V].** Adds two LLM jobs to curiosity: action generation and history compression. A Hopfield module maps state-actions into the LLM's token embeddings, so no text description is needed. Uses a 280M Transfo-XL, not a modern LLM (d08, a19). Date note: some lines say 2024; use 2025.
- **OMNI-EPIC (2024/25).** The LLM writes the task and the environment code, filtered by interestingness, with an archive (a10, c20).
- **Intelligent Go-Explore, Lu, Hu, Clune (2025).** The LLM picks the state to return to, the action to try, and whether the result is interesting (c18, d05).
- **ONI, Zheng et al. (2025).** An online variant of Motif with no 1-billion-step offline data phase (a17).
- **Bandit-style audits of the model as explorer.** Krishnamurthy et al. (2024), EVOLvE/BanditBench (Nie et al. 2024), Schmied et al. (2025), Harris and Slivkins (2026) (a24, c12, b17, d01).
- **Side literature.** NoveltyBench (2025), Verbalized Sampling (2026), Si et al. (2024) on research ideas, Huang et al. (2024) on self-correction, Sclar et al. (2024) on prompt-format sensitivity, Valmeekam et al. (2024) on planning (d11-d16). These do not study exploration directly. They show what the "ask the model what to try" step does on text.

### 2.4 Competing views
- **Prior versus novelty.** One view: the LLM prior replaces novelty bonuses. The authors' own view: it does not. ELLM suggests mixing with RND (a03). iLLM keeps a curiosity term and says the boost is largest early (b15).
- **Prior versus training.** GLAM fine-tunes the LLM as policy. ELLM, Motif and iLLM keep the LLM out of control and use it as a signal. We do not train, so only the signal and proposal ideas apply.
- **Proposal versus judgment.** An LLM that proposes differs from one that judges. Proposal works in games (K02, K07). Judgment of ideas is near chance on research ideas (45-54% ranking accuracy vs 56.1% for humans, d14) and self-checking fails without external feedback (d16). Our guardrails G5 and G8 already say this.

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ELLM goals beat novelty-only in Crafter pretraining | about 6 achievements per episode vs under 3 for RND, APT, Novelty; oracle about 9 | Du 2023 (a01, c02) | [E] with iLLM, K02 |
| iLLM beats best baseline in Crafter | about 7 vs 6 achievements per episode (10 seeds); margin of 1 | Bougie 2025 (a19, c16) | [E] with ELLM, K02 |
| Quality audit of LLM-suggested goals | 64.9% good, 13.6% context-blind, 16.4% against common sense, 5.0% impossible | Du 2023 Table 2 (a02) | [S] K01 |
| Rewarded goals after similarity matching | 66.5% good, 1.1% context-insensitive, 32.4% common-sense violations, 0% impossible (line b02 mislabels 32.4% as impossible; critique corrected) | Du 2023 (a02, critique) | [S] |
| Matching free text to goal is weak | false negatives 11% on average, 100% for chop-grass; false positives when goals share words (wood, stone) | Du 2023 (a06) | [E] K04 with iLLM MiniHack |
| LLM never suggested a needed step | wood pickaxe never suggested in Crafter; authors suggest mixing with RND | Du 2023 (a03) | [S] anecdote |
| Downstream fine-tuning of ELLM policy unreliable | all methods unlearned early skills; frozen-policy exploration worked better | Du 2023 (c24) | [S] |
| Smaller GPT-3 models degraded ELLM | Codex and Davinci used; smaller ones worse (no number) | Du 2023 (a01) | [S] |
| Interestingness filter on LP (Crafter, 10 seeds, 100M steps) | tasks learned: uniform 4, LP 55, OMNI 82; interesting tasks learned 3, 9, 14; success on interesting tasks 0.103, 0.52, 0.78; all-task success 0.030, 0.42, 0.56; p<1e-3 | Zhang 2023 (a07, b05, c07) | [S] K05 |
| Model filter equals author-written oracle | OMNI vs LP+oracle, all but one comparison p>0.05; larger boring set (195 boring): OMNI 96 tasks, 0.59; oracle 101, 0.62; LP 67, 0.40 | Zhang 2023 (b06, c08) | [S] K06 |
| OMNI generating tasks zero-shot (AI2-THOR, GPT-4) | OMNI 13 tasks (CI 11-17), LP 2 (0-3), uniform 0 (0-2) | Zhang 2023 (a09, b07) | [S] |
| OMNI on BabyAI: relative gain, tiny absolute | tasks 8 vs 4 vs 1; success 0.0075 vs 0.006 vs 0.0047 | Zhang 2023 (a07, b07) | [S] |
| Voyager unique items | 63 in 160 iterations, 3.3x baselines; wood/stone/iron in 6/11/21 iterations (3/3 runs); diamond 1 of 3 runs (102 iterations); AutoGPT 92/94/135, diamond 0/3; ReAct, Reflexion 0/3 | Wang 2023 (a11) | [S] K07 (3 runs) |
| Voyager ablations | random curriculum -93% items; no self-verification -73%; GPT-3.5 for code: 5.7x fewer items; unseen tasks 3/3 in 19 +/- 3 iterations vs 0/3 | Wang 2023 (a12, b09, c15) | [S] |
| Voyager hallucinated tasks | asked for a copper sword and chestplate (do not exist); no rate | Wang 2023 (b10) | [E] K08 with ELLM 5% impossible and OMNI-EPIC unsolvable environments |
| OMNI-EPIC success detector vs humans | 72.7% agreement (50 participants); one run: 16 done, 6 failed, 1 uninteresting | Faldor 2024 (a10) | [S] |
| Motif on NetHack | intrinsic only beats score-trained agent on score task; staircase levels 3-4: extrinsic and RND 0% success, Motif above 0; Oracle task about 30% with intrinsic plus extrinsic | Klissarov 2023 (a14, b11, c04) | [E] K10 with ONI |
| ONI online variant | 5 seeds, 95% CI; ONI-classification matches Motif on all tasks except Oracle; beats Motif on 3 of 4 reward-free progress metrics; no 1e9-sample offline phase | Zheng 2025 (a17) | [E] K10 |
| Reward hack by composition | default prompt: agent stayed on level 1, ate hallucinogen corpse; reworded prompt: intended descent | Klissarov 2023 (a15, b12, c06) | [S] K09 |
| Scale and one hint sentence | Llama 2 7B < 13B < 70B on staircase 3; one added sentence of game knowledge significantly better; prompt modifiers +106% gold (CI 64-157), +17% descents, +150% kills | Klissarov 2023 (a16, b13, c05) | [S] K11 |
| iLLM BabyAI PickUpLoc | RND and NGU under 0.25 after 100M steps; iLLM(hop) 0.85 after 68M | Bougie 2025 (b14, c16) | [S] |
| iLLM Atari (100M steps, 10 seeds) | Montezuma 2,632 vs best baseline ChibiT 1,231; PrivateEye 4,422 vs 3,633; Gravitar 4,044 vs 2,983; Pitfall 125 vs -6 (NGU); Seaquest 18,851 vs APT 19,989 (not a win) | Bougie 2025 (d08) | [S] K33 |
| iLLM noisy-TV (GoToObj) | original: RND 0.51, ELLM 0.66, iLLM(obs) 0.94; noise patch: RND 0.24, ELLM 0.45, iLLM 0.65; noise action 0.10: ChibiT 0.66, iLLM(obs) 0.87; paired t-tests p<0.002 | Bougie 2025 (d10) | [S] |
| iLLM MiniHack | LavaCross-Full 0.98-1.0 vs best baseline 0.50; MultiRoom-N4-Monster 0.75 vs 0.70; River-Monster 0.38 vs 0.22 (baseline label unconfirmed); RND, NGU 0.0 on all five | Bougie 2025 (d09) | [S] River-Monster cell doubtful |
| iLLM backbone | avg return over 9 BabyAI tasks: Transfo-XL 0.83-0.85, Flan-T5 0.75-0.79, Llama-2 7B 0.87-0.88 | Bougie 2025 (c17, d10) | [S] |
| LLM priors help where the LLM already knows the domain | iLLM authors: gains smaller where it knows less; large on Montezuma, absent on Seaquest (uncontrolled) | Bougie 2025 (b15, c17, d08) | [E] K03 (ELLM small-model drop as second point) |
| Unscaffolded LLM bandit exploration | 1 of 48/48/72 configs worked (GPT-4, hint, external per-arm summary, CoT, temp 0); basic GPT-4: suffix failure in over 60% of replicates; two failure modes: suffix failure, uniform-like | Krishnamurthy 2024 (a24, b16, b24, c09) | [S] K12 |
| Knowing-doing gap | Gemma2 27B: 87% correct rationales, greedy action in 58% of those; 2B covers about 40% of arms, 9B/27B about 65%; 2B copies the most frequent action | Schmied 2025 (b17, b25) | [S] K13 |
| Summary vs raw history | few-shot UCB demos: summary 50.2% win-rate vs raw 27.5% (Gemini Flash); fine-tuning: raw 65.6% vs summary 28.3%; few-shot easy demos 50.2 vs hard 43.0; fine-tune hard 65.6 vs easy 54.5 | Nie 2024 (c12, c13) | [E] K14 with Krishnamurthy |
| GPT-3 horizon task | regret 2.72 vs humans 3.24; reward-difference beta=0.18; rudimentary random exploration, no directed exploration | Binz and Schulz 2023 (c11) | [S] K15 (outdated model) |
| Zero-shot game agents explore poorly | BALROG best average 32.64% (Claude 3.5 Sonnet); NetHack best 1.5% (o1-preview); no model solved MiniHack quest or boxoban; agents revisit rooms | Paglieri 2024 (c21, c22) | [E] K16 |
| Reflexion no better than ReAct in long horizons | no improvement in any tested game; authors' guess: long history | Lu 2025 (c18, c25) | [E] K16 |
| Intelligent Go-Explore, Game of 24 (GPT-4, 100 problems) | naive 70, ReAct 82, Reflexion 83, IGE 100; IGE 100% in 150 operations, 70.8% faster than best baseline (DFS); Llama-3 400B 44/68/54/98; Claude Sonnet 3.5 24/58/80/86 | Lu 2025 (d05, d07) | [S] K17 |
| IGE ablations, Game of 24 at 150 steps (100 seeds) | full 100; random action choice 68 +/- 9; random state 96 +/- 3.5; no filter 93 +/- 5; no per-state action history 33 +/- 9; classic Go-Explore 38 +/- 22; BabyAI: full 84, random state 24, no filter 48 (25 seeds) | Lu 2025 (d06) | [S] K29 |
| IGE with generic prompts | Game of 24 96 (vs 100); BabyAI 84 to 68; TextWorld Cooking 92 to 72; ReAct BabyAI 48 to 24 | Lu 2025 (d07) | [S] K31 |
| IGE cost | GPT-4: Game of 24 1.04 USD, BabyAI 2.01, TextWorld 1.28 per task; no tokens per success | Lu 2025 (d05) | [S] K30 |
| Propose K candidates, then a bandit, beats random and retrieval (text) | MovieLens (943 users): Qwen 671.88 (K=10), Mistral 735.38 vs random 570.39, genre 617.27; Q/A 0.5-0.6 vs under 0.1; arXiv titles GPT-4o about 0.63-0.83 vs MMR retrieval 0.39-0.52 | Harris and Slivkins 2026 (d01) | [S] K24 |
| Contextual bandit puzzles: LLMs below linear regression | text non-linear puzzle: linear baseline 70% correct; every LLM config significantly lower; one GPT-4 code run about 70 USD | Harris and Slivkins 2026 (d02) | [S] |
| Reasoning models explore better than chat models (Little Alchemy 2) | elements in 500 trials: o1 177, R1 85, GPT-4o 35, LLaMA 70B 25, 8B 9, humans 42 (29,493 players); o1 vs humans t=9.71 | Pan 2025 (d03, d18) | [S] K27 |
| Strategy hints did not help GPT-4o | 43 vs 35 elements, t=-1.17, p=0.304; steering also no help | Pan 2025 (d04) | [S] K29 |
| Reasoning models switch thoughts too early | 225% more tokens and 418% more switches on wrong answers; switch penalty gave a few points on AIME | Wang 2025 (d17) | [S] K28 |
| Plain repeated sampling is a weak baseline | frontier models under 3 distinct answers in 10 samples; showing earlier answers restores human-level diversity; system-prompt nudges and paraphrase barely help | Zhang 2025 NoveltyBench (d12) | [E] K25 |
| Verbalized sampling | diversity 1.6-2.1x direct (creative writing); ratings poem 1.90 / 2.07 / 2.39 (direct/sequence/VS); synthetic maths data accuracy: baseline 32.8, direct 30.6, sequence 33.7, VS-Standard 36.1, VS-CoT 37.5 | Zhang 2026 (d13) | [E] K25 |
| LLM research ideas: more novel, slightly less feasible, repetitive | 79 experts, 49 ideas per arm: novelty 4.84 human vs 5.64 AI (5.81 reranked); feasibility 6.61 vs 6.34 (n.s.); about 5% of 4,000 seed ideas non-duplicate at cosine 0.8; LLM judge ranking accuracy 45-54% vs 56.1% human | Si 2024 (d14) | [E] K25, K26 |
| Same-model checking does not recover errors | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; oracle labels: GPT-4 97.5 | Huang 2024 (d16) | [E] K26 |
| Prompt format sensitivity | up to 76 points (LLaMA-2-13B); GPT-3.5 up to 56 points, median 6.4, 320 formats | Sclar 2024 (d11) | [E] K31 |
| Familiarity: renamed Blocksworld | best LLM 62.6% (LLaMA 3.1 405B zero-shot) to under 5% obfuscated; o1-preview 97.8% to 52.8%; o1-mini 56.6% to 19.1% | Valmeekam 2024 (d15) | [S] K32 |
| Wrong fact in a prior | SPRING: one wrong crafting-table fact cuts performance 24% | Wu 2023 (b21) | [S] K21 |
| LLM plus curiosity fragile in a tiny study | MiniGrid DoorKey, 3 runs: VAE-only above 0.6; LLM+VAE 1 below 0.2; LLM+VAE 2 and 3 did well | Quadros 2025 (a26) | [C] K22 |
| SayCan plan vs execution | 84% plan, 74% execution mock kitchen; real kitchen execution -14 points | Ahn 2022 (a13) | [S] K19 |

## 4. Mechanisms and models

Each mechanism is stated so an engineer can build it.

### 4.1 Goal suggestion with similarity reward (ELLM)
1. A captioner turns the state into text (in Crafter, trained on 847 human plus 900 synthetic labels, a06).
2. Prompt the LLM with the state text: "what should the agent do next?" It returns a short list of goals in words.
3. At each step, embed the agent's last action caption and each goal. If cosine similarity passes a threshold, give reward 1 and drop that goal.
4. Train an RL policy on that reward during pretraining. Use it frozen for exploration downstream.

Failure points: 35% of suggested goals were not good (13.6 + 16.4 + 5.0) (a02). The matcher gives 11% false negatives and many false positives (a06). The model may never suggest a needed step (a03). The authors' fix is a novelty term.

For a text agent, take the structure: propose a list, check, credit only after a separate check. The credit step is the weak link.

### 4.2 Preference-distilled reward (Motif, ONI)
1. Collect pairs of event captions from play.
2. Ask a model which of two is better progress. Parse the answer (about 90% parse rate, c04).
3. Train a reward model on the ranks (Motif offline; ONI online with an asynchronous server and distilled hash, classification or ranking models).
4. Use the reward model as intrinsic reward, alone or with the task reward.

Risk: combining a good intrinsic reward with the task reward produced a hack (a15). A reworded prompt removed it, so wording changes behaviour. For us the useful part is pairwise ranking: ask the model to compare two candidate states on progress and let code pick the branch. Untested outside games.

### 4.3 Interestingness filter on learning progress (OMNI)
1. Maintain a pool of tasks. Estimate learning progress per task (change in success rate).
2. Without a filter, LP chases learnable but boring tasks (repeated, compound, synonym tasks).
3. Ask the model, with few-shot examples: is this task interesting given the tasks already solved?
4. Sample tasks by LP times interest. Optionally let the model also generate new tasks from the lists of tasks done and failed.

The "interesting" oracle was non-repetitive tasks, defined by the authors (a08). The authors note Goodhart risk if the filter becomes an optimisation target (c08).

### 4.4 Curriculum proposal with verification and skill memory (Voyager)
Loop: GPT-4 sees state and history, proposes the next task; writes code; environment feedback plus a self-verification step decide success; successful code goes into a library. Ablations: random curriculum -93%, no self-verification -73% (a12). Needs environment feedback throughout. Proposals can be impossible (b10).

### 4.5 Archive with LLM-chosen frontier (Intelligent Go-Explore)
1. Store every visited state with its path and outcome.
2. Ask the LLM which archived state is most promising. Return to it (simulator restore).
3. Ask the LLM for an action there, with the history of actions already tried in that state in the prompt.
4. Ask whether the result is interesting; add it only if so. The filter keeps the archive small.

The per-state action history is the most valuable piece on Game of 24: dropping it cost 67 points (d06). State selection and filtering matter on long-horizon text games (BabyAI 84 vs 24 and 48, d06). The no-reset variant (replay the path in the prompt) is only mentioned, not tested (d05, K30).

### 4.6 History compression with a curiosity term (iLLM)
Ask the LLM to (a) generate plausible actions and (b) summarise the state-action trajectory. Use these as extra intrinsic signals beside a curiosity bonus. A Hopfield memory maps raw state-actions into the LLM's token embedding space. With a 280M Transfo-XL it resists noisy-TV (GoToObj noise patch 0.65 vs RND 0.24, d10).

### 4.7 The explorer-as-LLM view and the summary-state fix
Krishnamurthy et al.: give the LLM a hint to explore, an externally computed per-arm count and mean, and zero-shot chain of thought at temperature 0. Only that configuration explored well (a24). EVOLvE agrees for few-shot (50.2% vs 27.5% for raw history, c12). Schmied shows the same model can write the right rationale and still choose greedily (b17). Mechanism: bias toward frequent and recent actions (b25) and toward exploiting.

Implementation for a text agent: code keeps a table of option, tries, outcome. The prompt shows the table, not the raw log. Code, not the model, chooses the least-tried option when an explore rule fires (as S3 open mode already does).

### 4.8 Propose K, then run a bandit (Harris and Slivkins)
One LLM call proposes K candidate arms in a huge semantic space. A standard bandit (UCB1) then runs over those K arms. This moves the exploration discipline to code and uses the LLM only for the prior. It beat random and retrieval baselines (d01). It did not test plain repeated sampling.

### 4.9 Proposal diversity (NoveltyBench, Verbalized Sampling)
Independent samples from an aligned model collapse to a few answers. Two prompt-only fixes: regenerate with earlier answers shown, or ask for several answers with stated probabilities in one call (d12, d13). If our agent asks "what is worth trying" many times, proposals must be generated with memory of earlier proposals or they will be duplicates. The schema's rule that attempts are isolated has a cost here: isolated samples collapse. The schema sidesteps this in open mode, where code assigns directions.

## 5. What holds up

### 5.1 Replications and independence
- **No independent replication of ELLM or OMNI was found** (K34). The only outside use: iLLM re-ran ELLM as a baseline and found it weaker (GoToObj 0.66 vs 0.94). That is not a test of ELLM's claims. IGE comes from the OMNI lab. The Motif-ONI pair is the best case: ONI matches Motif on most NetHack tasks without its data phase (a17).
- The literature search was limited. The WebSearch budget ran out and API rate limits blocked citation-graph search. Absence of replication is weak evidence, not proof.
- Several "established" claims rest on two papers from related groups (OMNI, OMNI-EPIC and IGE from the Clune lab; Motif and ONI from Meta and Mila). Read "[E]" as "two papers agree", not "many labs agree".

### 5.2 What survives
- **Prior beats pure novelty in knowledge-rich games** (K02): ELLM 6 vs under 3; iLLM 7 vs 6; iLLM Atari wins on four of five.
- **Preference-style reward works in NetHack and an online variant matches it** (K10).
- **The prior must be verified** (K04, K08): 35% bad suggestions; false negatives and positives in matching; hallucinated items in Voyager; unsolvable code environments in OMNI-EPIC; one wrong fact -24% in SPRING.
- **Prior plus novelty, not prior alone** (K23): ELLM and iLLM authors both say so.
- **Same-model checking does not rescue it** (K26): Huang et al.; LLM judges near chance on ranking ideas.
- **Plain sampling is a weak baseline** (K25).
- **Summaries of tried options help in-context exploration** (K14).
- **Zero-shot agents explore badly in long horizons**, and Reflexion adds nothing over ReAct there (K16).

### 5.3 Failures, boundary conditions, moderators
- **Domain familiarity.** Gains are largest where the model already knows the domain (K03). Indirect: renaming Blocksworld takes the best LLM from 62.6% to under 5% (d15). No exploration paper varies familiarity under control.
- **Model scale.** Smaller GPT-3 models degraded ELLM. Llama 2 7B < 13B < 70B on a NetHack task (K11). In iLLM the backbone changes the score only slightly (0.83 to 0.88).
- **Prompt wording.** Motif's default prompt gave a hack; a reworded one did not (K09). IGE generic prompts cost 12-20 points on two text games, 4 on Game of 24 (K31). Format changes move older models by up to 76 points (d11). Nobody measured the spread for probe-asking prompts.
- **Fine-tuning after ELLM pretraining** was unreliable for all methods (c24).
- **Interaction with other signals.** Motif's good reward plus task reward gave a hack. Quadros's tiny study found LLM+VAE below VAE-only in one of three configurations (K22, [C]).
- **Baseline weakness.** Voyager's ReAct and Reflexion baselines were re-implemented by the authors and scored 0/3. That may reflect weak implementations. Only 3 runs.
- **Absolute levels.** OMNI on BabyAI: 0.0075 vs 0.006 success; the gain is only relative. iLLM Crafter margin is one achievement. Seaquest is not a win.
- **Authors' own oracles.** OMNI's "interesting" is the authors' definition. "LLM equals oracle" means the model reproduces that definition, not an independent notion.

### 5.4 Interventions that worked
- External per-option summary (Krishnamurthy, EVOLvE).
- Archive with per-state action history and filtering (IGE; the history alone is worth 67 points on Game of 24).
- Showing earlier answers when regenerating (NoveltyBench).
- Oracle or external feedback for correction (GPT-4 97.5 with oracle labels).
- One added line of domain knowledge (Motif).
- A decoding penalty on thought switching (a few points on AIME, d17).
- Proposing K candidates, then a standard bandit (d01).

### 5.5 Interventions that did not work
- Strategy hints ("be diverse and forward-looking"), chain of thought, self-reflection for GPT-4o in Little Alchemy (43 vs 35, p=0.304, d04).
- Reflexion in long horizons (c25).
- Same-model self-correction (d16).
- System-prompt nudges and paraphrase for diversity (d12).
- LLM as ranker of ideas (45-54%, d14).
- Giving GPT-4 the translation of obfuscated names (10%, d15).

## 6. Language models

**As proposer (what is worth trying).** The LLM suggests mostly sensible things in knowledge-rich worlds: about 65% good in Crafter (a02). For research ideas, LLM ideas were judged more novel than expert ideas (5.64 vs 4.84) with feasibility only slightly lower (6.34 vs 6.61, n.s.) (d14). But they repeat: about 5% of 4,000 samples remained after de-duplication. In a text bandit with many semantic arms, one call proposing K candidates beat random and retrieval baselines by large margins on MovieLens, Q/A and arXiv titles (d01).

**As explorer with no scaffold.** Poor. GPT-3.5, GPT-4 and Llama 2 failed in nearly every bandit configuration (only 1 worked across 48/48/72; a24). The basic GPT-4 prompt had suffix failure in over 60% of replicates (K12). Gemma2 27B writes the right rationale 87% of the time and acts greedily in 58% of those (K13). BALROG: best average 32.64%, NetHack 1.5% (c21). Harris and Slivkins (2026) with GPT-5.2 and others: LLMs exploit well on small contextual puzzles but stay below linear regression, and summaries help on simple tasks only (d02). GPT-5.2 was used only on exploit tasks.

**What changed it, by how much.**
- *External summary of tried options*: near-greedy failure to near Thompson sampling in one config (a24); few-shot win-rate 27.5% to 50.2% (c12).
- *Reasoning training*: Little Alchemy 2 elements 35 (GPT-4o) to 85 (R1) and 177 (o1), above humans at 42 (d03). Chat models rely on uncertainty and ignore empowerment; o1 uses both. R1 writes long traces that revisit past trials (d18). One game.
- *Prompt hints on a chat model*: no gain (d04).
- *Scale*: monotone in Llama 2 7B/13B/70B on one NetHack task (a16); 2B to 27B lifts coverage from 40% to 65% (b17).
- *Familiarity*: planning accuracy 62.6% falls under 5% with renaming; o1-preview holds 52.8% (d15).
- *Self-check*: no help without external feedback (d16). 2023-era models.
- *Regeneration with memory*: diversity back to the level of 8 human authors (d12).
- *Verbalized probabilities*: 1.6 to 2.1x diversity; larger models gain 1.5 to 2x more (d13).
- *Reasoning models still err*: on wrong answers they use 225% more tokens and 418% more thought switches (d17).

**Caveats.** The iLLM LLM is 280M parameters. ELLM used Codex and Davinci. Most bandit studies use 2023-2024 models. IGE used GPT-4 and 2024 models; the Sonnet 3.5 gain over Reflexion was not significant (86 vs 80, d07). There is no 2025-2026 frontier-model repeat of ELLM, OMNI or IGE (K34). Whether S3 prior-asking adds anything for a reasoning-trained model is not tested (K27, K28 argue weakly against redundancy).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = S9 and code-held records.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | In open mode, treat the answer to "what is worth trying" as a proposal list that is checked, never as truth. Expect about one third unusable. | S3 (open mode), G8 | [E] | K01 (a02), K08, K26; b10, a10, d14 |
| A2 | Check proposals with something external: a rule, a run result, a held-out example. Do not let the same model re-check its own proposals. | G2, G5, S4 | [E] | K26 (d16, d14); K04 (a06, b14) |
| A3 | Credit a probe only after a separate check that it produced its stated effect. Free-text similarity matching is unreliable (11% false negatives; shared words give false positives). | G (no unchecked credit), S4 | [E] | K04 (a06, b04, b14) |
| A4 | Pair the prior with a novelty or untried tie-break. Never use the prior alone. | S3 | [E] | K23 (a03, c24, b15); K02 |
| A5 | Keep a code-held tally of what was tried and the outcome; show a summary table, not the raw log. Code picks the least-tried option when an explore rule fires. | S3 open mode, memory | [E] for the summary (two papers); effect size on frontier models unknown | K14 (c12, a24, b16) |
| A6 | When a baseline is needed for "ask the model for ideas", use a regeneration loop that shows earlier answers (or a verbalized-probability prompt), not independent samples. | S3, G7 | [E] | K25 (d12, d13, d14) |
| A7 | For any model-based filter or prior, report the spread over about 10 paraphrases of the prompt. Count a gain smaller than the spread as unproven. | G7 | [E] | K31 (d11, d07); K09 |
| A8 | Do not expect the prior to help as much on obscure or renamed domains. Report results split by familiarity. | S0 gate | [E] (weak) | K03 (b15, c17, a01) |
| A9 | Proposals can name things that do not exist or cannot be done. Feasibility is a named check in the proposal step. | G, S4 | [E] | K08 |

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | "What is worth trying here" step at S3 versus a regeneration loop and versus a novelty tie-break, at equal tokens, on open-answer text items. | S3 | [S] nothing on reasoning tasks | K24, K25; gap 1 |
| T2 | A per-state tried-list in the prompt on a puzzle set. Dropping it cost 67 points on Game of 24 with GPT-4 Turbo. Frontier-model effect unknown. | memory, S3 | [S] | K29 (d06, d04) |
| T3 | Propose K candidates in one call, then run a plain bandit rule over them in code. | S3 + code | [S] | K24 (d01) |
| T4 | Interestingness filter before spending tokens: drop repetitive or boring sub-goals. | S3, S6 | [S] | K05, K06 (a07, c08) |
| T5 | Reasoning model versus chat model: does the S3 prior add less for the reasoning model? | S0 gate | [S] | K27 (d03, d18) |
| T6 | A "finish this branch before switching" rule plus a visible tried-list on a reasoning model. | G11, O, memory | [S] | K28 (d17) |
| T7 | Frontier list of unresolved sub-goals; and a no-reset version that replays the stored path. | memory | [S] | K17, K30 (d05, d06) |
| T8 | Pairwise "which state is closer to the goal" ranks used to pick a branch in code. | S3, S7 | [S] | K10 (a14, a17) |
| T9 | One line of task knowledge in the "what to try" prompt. | S1, S3 | [S] | K11 (b13) |
| T10 | Rename-entity control: S3 gain on original versus nonsense-renamed items. | S0 | [S] | K32 (d15) |
| T11 | Probe-prompt paraphrase spread (10 paraphrases) as a standing check. | G7 | [S] | K09, K31 (a15, d11) |
| T12 | Injected false fact in the prior, to see whether verification catches it. | G | [S] | K21 (b21) |

Not taken: Eureka and Text2Reward reward code (K18, needs a simulator); GLAM and Schmied-style RL fine-tuning (K20, K13, training); SayCan value functions (K19, trained per skill); the GPT-3 horizon-task result (K15, outdated model).

**Schema fit.** G4 says samples from one model are not independent; the regeneration finding (A6) agrees. G8 says the generating model is never the final selector of ideas; that agrees with LLM judges ranking ideas near chance (d14). G1 says doubt only on a signal; nothing here supports exploring on a schedule. The prior belongs at S3 in open mode and at S6 impasse, which matches the schema's current use. We propose no new state or operator.

## 8. Concrete tests on our bench

All arms at equal tokens, setup cost counted (G7). Report solved items per 1,000 tokens and the paraphrase spread (A7). Use the bench harness. Items: our open-answer word and brain-teaser items and ARC-style items with a checker; for open-answer items, a hand rubric for novelty and a run-based check for validity.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | 40 open-answer items with at least 3 valid answers, plus 20 single-answer items with a check | (a) independent samples; (b) regeneration loop showing earlier answers; (c) "what is worth trying" proposals then external check; (d) b plus code novelty tie-break | valid distinct answers per 1,000 tokens; solved rate on single-answer items | b well above a (NoveltyBench); c adds only if its prior beats b; small or none on single-answer items |
| B2 (T2) | 30 multi-step puzzles with dead ends | with and without a per-state tried-list summary | solved at equal tokens | positive on 2024 models (100 vs 33); smaller on frontier models; add if gain >= 8 points |
| B3 (T3) | 20 items with a large option space and a cheap grader | K random draws; K proposals; K proposals plus UCB in code; retrieval baseline | reward at fixed token budget | proposals plus UCB above random (d01); open question is whether it beats b of B1 |
| B4 (T4) | task lists with injected boring or repetitive sub-goals | model filter; hand rule; no filter | solved per token | filter at least equal to the hand rule |
| B5 (T5) | same 40 items | chat vs reasoning-trained model, S3 prior on or off | difference in solved rate | smaller gain for the reasoning model (K27) |
| B6 (T6) | long-chain items where reasoning models fail by switching | "finish branch" rule; visible tried-list; both; neither | switches per solved item; solved rate | fewer switches, equal or better accuracy |
| B7 (T7) | puzzles with a restore point, and the same without | flat tried-list; frontier list with path replay | tokens per success | archive pays only if tokens per success beats the flat list |
| B8 (T8) | branch-choice items (two partial solutions) | model pairwise rank; code score; random | pick accuracy against the checker | model above random, below code score when a check exists |
| B9 (T10) | B1 items original vs entities renamed to nonsense | S3 prior on vs off | gain on original minus gain on renamed | positive difference supports K32 |
| B10 (T11) | the S3 prompt, 10 paraphrases | all arms | min-max spread | any claimed gain must exceed the spread |
| B11 (T12) | items with one planted false premise in the prior | verify step vs none | drop in accuracy | verify step cuts the drop (SPRING: 24%) |
| B12 (A3) | probes with a stated effect | similarity matcher vs separate check vs ground truth | disagreement with ground truth | matcher worse (ELLM 11% false negatives) |

## 9. What does not transfer, and why

- **Intrinsic-reward training (ELLM, Motif, ONI, OMNI, iLLM).** Tens of millions to a billion RL steps. Our agent does not train. Only the structure (proposal, filter, check) carries over, not the sample-efficiency numbers.
- **Reward code (Eureka, Text2Reward).** Needs a simulator with a fast fitness function. We have none for open text items.
- **Game worlds the model knows.** Crafter, Minecraft, NetHack and BabyAI have heavy text coverage. Gains may shrink on a new task (K03, K32).
- **Resets and rich state text.** Go-Explore needs return to an archived state (d05). ELLM needs a state captioner. Text puzzles often have neither.
- **Costs.** Voyager's GPT-4 was about 15x the cost of GPT-3.5 (b10). IGE reports cost per task (1.04 USD on Game of 24) and spends extra calls on state choice and filtering. At equal tokens every call must pay back.
- **Small and old models.** iLLM used 280M. Schmied used Gemma2 2B-27B. Krishnamurthy used GPT-3.5, GPT-4, Llama 2. Frontier and reasoning models are unmeasured, and reasoning models already explore better in Little Alchemy 2.
- **Authors' oracles and re-implemented baselines.** OMNI's oracle and Voyager's baselines come from the authors.
- **Bandit results.** Small, noise-limited, with a summary that may be impossible to build in a complex task (authors' warning, a24).
- **Self-check results.** From 2023 models on answer correction, not probe feasibility.

## 10. Open questions

1. Does "what is worth trying" at S3 beat a regeneration loop or a novelty tie-break on a text reasoning task at equal tokens? Nothing outside games tests this (gap 1).
2. How often are model-proposed probes infeasible or context-blind on puzzles, maths and code, and does a cheap external check recover the loss? Only Crafter's 35% is known (gap 2).
3. Does a tried/untried tally fix greedy collapse in 2025-2026 frontier models? Last tested on GPT-4 Turbo and Gemma (gap 3).
4. How large is the paraphrase spread when the prompt asks for probes (gap 4)?
5. Does an archive help without environment resets, and what is tokens per success (gap 5)?
6. Does an interestingness filter transfer beyond repetitive versus non-repetitive, with an author-independent oracle (gap 6)?
7. Does the prior shrink in unfamiliar domains under a controlled test (gap 8)?
8. Are there replications of ELLM, OMNI or IGE outside the original labs, with open or 2025-2026 frontier models (gap 9)? Citing papers could not be searched.
9. Is the S3 prior redundant for reasoning-trained models (gap 10)? Pan (d03) and Wang (d17) point in different directions.
10. Does LLM plus curiosity combine reliably? The one small study (Quadros, 3 runs) says no for one configuration.
11. The iLLM River-Monster baseline value (0.22) could not be tied to a named method; the cell stays doubtful.

## 11. Sources

[V] opened and read as full text this session by the research agents. [M] snippet only. The cross-check re-opened ELLM, OMNI, Voyager, Krishnamurthy, Schmied, EVOLvE, Motif and iLLM. GLAM, SayCan, Eureka, Text2Reward, SPRING, OMNI-EPIC, Intelligent Go-Explore, BALROG, ONI, Quadros and Binz and Schulz were read by first-pass agents and not re-opened by the cross-checker; their numbers are not re-verified.

| Mark | Source | URL |
|---|---|---|
| [V] | Du et al. (2023) Guiding Pretraining in RL with LLMs (ELLM) | https://arxiv.org/abs/2302.06692 |
| [V] | Zhang et al. (2023) OMNI | https://arxiv.org/abs/2306.01711 |
| [V] | Faldor et al. (2024/25) OMNI-EPIC | https://arxiv.org/abs/2405.15568 |
| [V] | Wang et al. (2023) Voyager | https://arxiv.org/abs/2305.16291 |
| [V] | Ahn et al. (2022) SayCan | https://arxiv.org/abs/2204.01691 |
| [V] | Klissarov et al. (2023) Motif | https://arxiv.org/abs/2310.00166 |
| [V] | Zheng et al. (2025) ONI: online intrinsic rewards from LLM feedback | https://arxiv.org/abs/2410.23022 |
| [V] | Bougie and Watanabe (2025) iLLM | https://proceedings.mlr.press/v260/bougie25a.html |
| [V] | Carta et al. (2023) GLAM | https://arxiv.org/abs/2302.02662 |
| [V] | Krishnamurthy et al. (2024) Can LLMs Explore In-Context? | https://arxiv.org/abs/2403.15371 |
| [V] | Quadros et al. (2025) LLM-driven intrinsic motivation for sparse reward RL | https://arxiv.org/abs/2508.18420 |
| [V] | Ma et al. (2023) Eureka | https://arxiv.org/abs/2310.12931 |
| [V] | Xie et al. (2023) Text2Reward | https://arxiv.org/abs/2309.11489 |
| [V] | Wu et al. (2023) SPRING | https://arxiv.org/abs/2305.15486 |
| [V] | Schmied et al. (2025) LLMs are Greedy Agents | https://arxiv.org/abs/2504.16078 |
| [V] | Binz and Schulz (2023) Using cognitive psychology to understand GPT-3 | https://arxiv.org/abs/2206.14576 |
| [V] | Nie et al. (2024) EVOLvE / BanditBench | https://arxiv.org/abs/2410.06238 |
| [V] | Lu, Hu and Clune (2025) Intelligent Go-Explore | https://arxiv.org/abs/2405.15143 |
| [V] | Paglieri et al. (2024) BALROG | https://arxiv.org/abs/2411.13543 |
| [V] | Harris and Slivkins (2026) Should you use your LLM to explore or exploit? | https://arxiv.org/abs/2502.00225 |
| [V] | Pan, Xie and Wilson (2025) LLMs think too fast to explore effectively | https://arxiv.org/abs/2501.18009 |
| [V] | Sclar et al. (2024) Quantifying LMs' sensitivity to spurious features in prompt design | https://arxiv.org/abs/2310.11324 |
| [V] | Zhang et al. (2025) NoveltyBench | https://arxiv.org/abs/2504.05228 |
| [V] | Zhang et al. (2026) Verbalized Sampling | https://arxiv.org/abs/2510.01171 |
| [V] | Si, Yang and Hashimoto (2024) Can LLMs generate novel research ideas? | https://arxiv.org/abs/2409.04109 |
| [V] | Valmeekam, Stechly and Kambhampati (2024) LLMs still can't plan; can LRMs? | https://arxiv.org/abs/2409.13373 |
| [V] | Huang et al. (2024) LLMs cannot self-correct reasoning yet | https://arxiv.org/abs/2310.01798 |
| [V] | Wang et al. (2025) Thoughts are all over the place: underthinking of o1-like LLMs | https://arxiv.org/abs/2501.18585 |
