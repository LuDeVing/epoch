# Foraging and patch leaving: deep document

*Subfield B02.08. Question for our agent: when should it leave a depleting source (an operator, a line of attack, a retrieval stream)? Candidate S6 rule: leave when current yield falls below the average yield of the whole run. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K26), critique.md in this folder. Ids like a04 or d11 are evidence lines. Honest summary: the biology is strong and the LLM side is almost empty. No study found tests a "yield below running average" stop on a language model.*

## 1. What it is

Patch foraging is the problem of an animal in a world of clumps of food. Each clump (patch) gives less the longer you stay, because you deplete it. Moving to a new patch costs travel time. The question is when to leave.

The founding answer is the marginal value theorem (MVT, Charnov 1976, with Charnov and Orians 1973 before it). Leave when the instantaneous intake rate in the patch falls to the long-run average rate of the whole habitat, travel time included. Written out: leave at the time t* where g'(t*) = g(t*) / (t* + travel). Two direct consequences. Longer travel means a longer stay. A richer environment means a shorter stay. (a17, b25, c21. The founding papers were not opened here; the rule was confirmed in Wispinski 2023, c21.)

The theorem assumes a known, smooth, deterministic depletion curve, no uncertainty, and a rate-maximising forager. Most later work asks what happens when these assumptions fail.

The idea has been carried into thinking in three ways.
- Foraging in memory: semantic fluency (naming animals) works like patch foraging. People stay in a cluster (pets, farm animals) and switch when the within-cluster retrieval rate falls below the global average (Hills, Jones, Todd 2012; a22, not opened here).
- Foraging in visual search and decisions: berry picking (Wolfe 2013, b06) and the Kolling fMRI task, where people choose between engaging with a current option and searching for a better one (a01).
- Foraging for information: "information foraging" design ideas for retrieval agents (c10, c11, c12).

Mapping for our agent: patch = an operator (O1-O8) or a line of attack. Yield = new verified information per step. Travel cost = cost of switching (lost context, setup tokens). Average rate = running mean yield across the run. S6 is the control state that decides when to abandon an operator.

## 2. History and theories in depth

**1973-1986, theory.** Charnov and Orians (1973) set out optimal patch use. Charnov (1976) formalised the marginal value theorem. Stephens and Krebs (1986, a18) is the textbook with the extensions: uncertainty, variance, risk sensitivity. None was opened in this study.

**2008-2013, humans in cognitive foraging.** Hutchinson, Wilke and Todd (2008, a20, not opened) found human visual foragers adapt leaving rules to item dispersal, with simple rules such as giving-up time. Wolfe (2013, b06) ran six berry-picking experiments with about 10 observers each. With uniform patches, leaving matched MVT. With mixed patch quality and slow travel, observers left too early (Exp4 slow travel 0.66 berries/s vs MVT 0.45; fast travel 0.76 vs 0.75). With no colour cue (Exp6) leaving did not follow a rate rule. Hills et al. (2012) carried the rule to memory search.

**2011, neurons.** Hayden, Pearson and Platt (2011, a04, a05) recorded monkey dorsal anterior cingulate (dACC) neurons. Firing ramped up with time in patch and reached a fixed level at the moment of leaving. Longer travel lowered the ramp gain and raised the threshold. This gave an accumulator-to-threshold picture of leaving.

**2012, Kolling.** Kolling, Behrens, Mars and Rushworth (2012, a01, b01) built a two-stage fMRI task. A person either engages with an encountered option or searches among 6 boxed alternatives, at 3 search-cost levels, using 12 pre-learned values. dACC activity rose with the value of searching and fell with the encountered value. vmPFC tracked the chosen option. Behaviour showed a bias against searching: people needed more objective gain to search than to engage (a02). This is the key work named for this subfield.

**2014-2016, the neural dispute.** Shenhav, Straccia, Cohen and Botvinick (2014, a08, b02) replicated the task (Exp1, N=15) and built Exp2 (N=14) that decoupled foraging value from choice difficulty. dACC followed difficulty, not foraging value. Kolling et al. (2016, b03) replied that their design shared under 2.5 percent variance between search value and difficulty, and that search value survived controls. The camps still disagree (K06). The behavioural MVT results are not touched by this dispute.

**2015, learning the threshold.** Constantino and Daw (2015, a06, a07, b05) showed humans adapt thresholds to travel and depletion, and that a rule which learns the average reward rate beat temporal-difference models. People still overharvested (left late), 9 to 10 percent below optimal earnings.

**2015-2023, overharvesting becomes the main puzzle.** Monkeys are more patient in a foraging frame than a choice frame (Blanchard and Hayden 2015, a11). Rats overharvest too (Kane 2019, b08). Harhen and Bornstein (2023, a12, b07) argued overharvesting is rational: it comes from learning a multi-modal environment and adaptive discounting under uncertainty. Wispinski et al. (2023, c07) showed deep RL agents overstay plain MVT but match discounted MVT.

**2013-2026, Bayesian and stochastic accounts.** Marshall et al. (2013, c23, snippet only) found Bayesian updating won in a baboon experiment and a patch-MVT model won in the wild. Kilpatrick, Davidson and El Hady (2020, 2021; c15, b12) derived leave rules as inference about patch quality. Webb et al. (2025, a16, a25) found a hierarchical Bayesian rule fit mice best. A 2026 reanalysis (a14) said variability in leave time is stochastic choice, not learning noise. Kilpatrick and El Hady (2026, b13, c16) said the best rule depends on patch variability. Zylberberg (2024, d13) generalised MVT to discounting.

**2024-2026, language models.** Two strands meet the theory. (1) Semantic fluency in LLMs shows foraging-like structure (b18, b19, c05, c06). (2) The overthinking and underthinking literature is a stopping problem in all but name (d01-d10). No paper tests a depleting-patch task or a yield-below-average rule on an LLM (K15; c24, d18).

## 3. Core findings with exact numbers

Status follows claims.jsonl: E established (several independent sources), S single source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Foragers stay longer when travel is longer (monkeys, humans, rats, mice) | Monkeys: beta=1.247, P<0.0001, 2834 leaves, travel 0.5-10.5 s. Humans: Exp1 travel t(10)=5.7, depletion t(9)=5.1 (both p<.001); Exp2 depletion F(1,25)=82, travel F(1,25)=42.1. Rats: longer travel beta=1.893 trials (t=6.04) | Hayden 2011 (a04); Constantino and Daw 2015 (a07); Kane 2019 (b08) | E (K01) |
| Stay length tracks patch richness | Humans stayed longer in rich vs neutral patches (t=19.77) and neutral vs poor (t=12.57); thresholds fell in poorer environments (Constantino and Daw) | Harhen and Bornstein 2023 (b07) | E (K01) |
| Monkeys follow MVT but overstay | Overstay about 2.2 s (P<0.01); 97.2% of best-fit rate-maximising reward; 2 monkeys, 102 dACC neurons | Hayden 2011 (a04, a05) | E (K02) |
| Humans overharvest | Earnings about 9-10% below optimal; 47 analysed of 52; overharvest in 3 of 4 Exp2 conditions (t<3.6, p<.002) | Constantino and Daw 2015 (a06) | E (K02) |
| Rats overharvest | n=8, beta=3.396 trials (SE .176, t(6.96)=19.27, p<.001) | Kane 2019 (b08) | E (K02) |
| Overharvest is learned and conditional | 116 of 176 analysed; overall t(115)=3.88, P=.00018; poor t=6.92, neutral t=9.00, rich t=1.38 P=.17 (none); first two vs last two blocks t(115)=3.27, P=.0014; after rare switch t(115)=4.67 | Harhen and Bornstein 2023 (a12, b07) | E (K03) |
| Learned average-rate rule beats TD in humans | Exceedance probability 0.999; expected frequency 0.83 (Exp1), 0.85 (Exp2); vs R-learning 0.87 and 0.93 | Constantino and Daw 2015 (a06) | E (K01-K03) |
| Overharvest explained by adaptive discounting | Cross-validation error: adaptive discounting 16.55 (best for 64% of people), TD 22.47 (14%), MVT learning 32.31 (22%; predicted underharvesting, t=-7.26) | Harhen and Bornstein 2023 (a12) | E, one model family |
| Discounted MVT fits learning agents; plain MVT does not | 12 agents (3 per discount rate): +15.8 steps SE 2.7 (p<0.05) vs plain MVT; +0.9 steps SE 2.8, p=0.74 vs discounted MVT | Wispinski 2023 (c07) | E (K13) |
| World-model agent lands near MVT; model-free does not | DreamerV2 within +-1 quartile of MVT in at least 3 of 4 patch spacings; PPO outside the IQR in all 4; 3 training runs each | Fonseca 2025 (c09, b17) | S, preprint |
| Bias against searching | Indifference at foraging value 1.65 (SE 0.26, t(14)=6.5, p=1.4e-5), N=15; and 5.0 (SE 1.3, t(13)=3.9), N=14; zero would be neutral | Shenhav 2014 (a09, b02) | E (K07) |
| dACC tracks foraging value | Slope difference t(17)=-2.54, p=0.021. N not stated (do not cite 18) | Kolling 2012 (a01) | C (K06) |
| dACC tracks difficulty instead | difficulty t(13)=2.8, p=0.014; foraging value t(13)=0.47, p=0.64; contrast p=0.046; rho 0.80 (Exp1 design) vs 0.07 (Exp2) | Shenhav 2014 (a08) | C (K06) |
| Kolling reply | Shared variance of search value and difficulty under 2.5% | Kolling 2016 (b03) | C (K06) |
| Rat ACC: fast and slow reward-rate integrators | 22 rats, 148 ACC units; trials per patch rose with starting reward beta=2.294; inactivation: more trials beta=2.397; rats still followed MVT | Kane 2022 (a10) | S |
| Monkeys more patient in the foraging frame | 4 monkeys; all left earlier on the choice task than foraging predicts (P<0.0001); daily discount vs leave time correlations n.s. | Blanchard and Hayden 2015 (a11) | S |
| Social patch foraging follows MVT, small effect | 3 macaques, Kendall tau 0.069-0.079 (P<0.0001); Akaike weights 0.83-0.98 | Sci Rep 2017 (a15) | S |
| Overstay costs earnings | 42 of 52 humans, 18 gerbils; residence vs earnings r=-0.717 (lab), -0.653 (fMRI); none in gerbils; mean rate 0.165 reward/s; giving-up time about 10.4 s vs 4.1 s | Guldener 2024 (a13) | S |
| Mice leave at their own average rate | 16 mice; leave rate vs average rate correlated p<0.001; difference n.s. | Lottem 2018 (b14) | S |
| Simple heuristics rival MVT at low noise | RMSE low stochasticity: constant time 4.88, MVT-OPT 4.90, time since reward 5.86, reward count 6.57; best Bayesian 3.54. High stochasticity: 4.92, 4.67, 7.03, 4.85 | Webb 2025 (a16, a25) | S (K05) |
| Winning rule depends on setting | Baboons: Bayesian in experiment, MVT in the wild; mice: Bayesian best at high stochasticity | Marshall 2013 (snippet); Webb 2025 | C (K04) |
| Leave variability is stochastic choice | Reanalysis of 3 datasets (humans 39 and 29, rats 8); early vs late variability Bayes factors 3.71, 3.64, 2.55 for no change; SD of leave time 20-50% of mean | 2026 (a14) | C (K09) |
| Stress and traits shift the threshold | N=65, perceived stress beta=-0.49 t(61)=-2.91 p<.01, cortisol beta=-0.37 p<.05, group effect null; N=145 adversity study; N=756 apathy sample (cost-insensitivity effect failed in confirmation) | Lenow 2017 (b09); b15; b11 | S (K08) |
| Count vs timing rule switches at about 25% variability | About 25 percent patch variability | Kilpatrick and El Hady 2026 (b13, c16) | S (K19), theory |
| Optimal stay under discounting | Longer than plain MVT when yield only falls; shorter when later payoffs can rise | Zylberberg 2024 (d13) | S (K23), theory |
| LLMs switch less than humans in fluency | Switch ratio 0.55 human vs 0.40 LLM (p<0.0001); transition matrix Spearman 0.701; 681 human and 2285 LLM sequences kept; Llama-3 1B/3B/8B/70B | Lacosse 2026 (b18, c01) | S (K10) |
| Switch probe on natural data near chance | AUROC 0.57 from activations vs 0.751 from output probabilities (contrastive sets 0.96-0.98) | Lacosse 2026 (c02) | S (K12) |
| Depletion inside LLMs predicts switching | r at least 0.31, p<0.0001 in middle layers, five models 2B-9B; steering Gemma-2-9B layer 26: 0.29 baseline to 0.70 (positive) or 0.07 (negative) | Leckie 2026 (c03, c04) | S (K11) |
| LLMs do not explore in bandits from raw history | T=500, N=20; over 60% of GPT-4 basic-prompt replicates had suffix failure; only GPT-4 + chain of thought + summarised statistics explored | Krishnamurthy 2024 (c17, b21) | E (K14) |
| A given statistic helps big models only partly | Gemini-1.5 Pro win rate 45.5 raw, 60.0 summary, 59.6 algorithm-guided, UCB 90.6; Flash 27.7/34.8/32.2; Gemma-2B 7.6/10.5/4.9; Gemma-9B 10.5/5.3/4.1 | Nie 2024 (d11) | E (K14) |
| Overthinking: first round already right | o1-like models used 1,953% more tokens than conventional models for 2+3; first round correct in over 92% of correct cases, in under 60% of tokens | Chen 2024 (d01) | E (K17) |
| Confidence exit saves tokens | DEER: 11 models, 10 benchmarks, chains 19.1-80.1% shorter, accuracy +0.3 to +5.0%; probe exit threshold 0.85: 88.2% accuracy, about 24% fewer tokens | Yang 2025 (d02); Zhang 2025 (d04) | E (K17) |
| Adaptive exit beats fixed-step exit at equal tokens | 87.4% (Thr 0.8) vs about 82.5% static exit; R1-Distill-Llama-8B on MATH | Zhang 2025 (d04) | S (K20) |
| Models settle early | Final answer reached after about 60% of steps; Answer Consistency cut tokens over 40% on NaturalQuestions with accuracy up | Liu and Wang 2025 (d03) | E (K17) |
| More forced thinking has a peak | 82.2% to 87.3% (385 to 1,100 tokens), then 70.3% at 15,980; entropy 12x up | Ghosal 2025 (d08) | E (K21) |
| Budget forcing flattens | AIME24 50% to 57%; flat near 6 forced continuations; too many forcings give loops | Muennighoff 2025 (d09) | E (K21) |
| Repeated sampling has diminishing returns | SWE-bench Lite 15.9% (1 sample) to 56% (250), log-linear | Brown 2024 (d10) | E (K21) |
| Underthinking on hard items | Wrong answers: 225% more tokens, 418% more thought switches; switch tokens 13.8 to 5.7 with a decoding penalty (DeepSeek-R1, AIME2024); gap between switches 580.1 to 941.6 tokens | Wang 2025 (d05, d06) | S (K22) |
| Length does not track difficulty | Accuracy peaks at a short or medium length rank, not the longest | Su 2025 (d07) | S |
| Social framing drives LLM escalation | Alone: mostly divest. Peer deliberation: 99.2% escalate (249 of 251) vs 46.2% hierarchical (115 of 249); about 6,500 trials | Barkett 2025 (d15) | S (K25) |
| Step-efficiency penalty helps retrieval agents | R = gamma^max(0,T-2) * (R_outcome + alpha*R_gain); InForage 42.1/59.7 vs Search-R1-GRPO 40.9/55.2 (column labels scrambled, do not name the benchmark) | Qian and Liu 2025 (c10) | C (K16) |
| Sufficiency stop saves tokens | SCOUT 78.7 at 29.7k tokens vs Gemini-3-Pro 68.5 at 273.9k (LOOGLE-V2 first column; task not confirmed) | Zhang 2026 (c11) | C (K16) |
| LLM swarm robots with a hand-set 60 s starvation timer | 36 configurations, 360 trials, 53,189 calls; mean relative gain +70% | Li 2026 (c19) | S |

## 4. Mechanisms and models

Each model is described so it can be coded.

**4.1 Marginal value theorem.** Inputs: gain curve g(t), travel time T. Average rate R = g(t) / (t + T). Leave when instantaneous rate g'(t) <= R. In code keep `reward_total`, `time_total`, `time_in_patch`. Each step compute `local_rate` (last yield or a smoothed last k yields) and `global_rate = reward_total / time_total`. Leave if `local_rate < global_rate`. Switch cost counts as time in the denominator. Predictions: longer travel, longer stay; richer environment, shorter stay.

**4.2 Learned threshold (Constantino and Daw 2015).** The agent does not know g. It learns the average reward rate with a recency-weighted delta rule, `R <- R + alpha * (rate - R)`, and leaves when the current rate drops under R. This beat TD and R-learning (exceedance 0.999). It still overharvested; adding risk sensitivity closed the gap. Learning rate alpha is a parameter to set.

**4.3 Two-integrator model (Kane 2022, Hayden 2011).** A fast local integrator tracks recent yield; a slow global integrator tracks the long-run rate. A leaky competing accumulator pushes toward "leave" when local falls under global. The decision variable ramps to a threshold; higher travel cost raises the threshold and lowers ramp gain. Deep RL agents show the same ramping in LSTM units (c08). Variability in leave time came from ramp slope (the threshold-distance account was not significant).

**4.4 Discounted MVT (Wispinski 2023; Zylberberg 2024).** Replace the plain average by a discounted one. When yield only falls, the best stay is longer than plain MVT; when later payoffs can rise, shorter. Implementation: same rule with a patience factor on the threshold. Test 0.8, 1.0, 1.2 times the running average (K23). The right margin for an LLM is unknown.

**4.5 Bayesian patch inference (Kilpatrick 2020, 2021; Webb 2025).** The forager does not see the depletion rate. It keeps a posterior over each patch's decay rate (and over environment richness in the hierarchical version) and updates it with each reward. It leaves when estimated yield, or certainty, falls under a threshold. Uncertainty makes it overharvest initially poor patches and underharvest initially rich ones. A hierarchical Bayesian model fit mice best (RMSE 3.54 vs 4.90 for MVT-OPT at low stochasticity). Sketch: conjugate update of a decay-rate estimate per operator, with a prior taken from earlier runs (the memory idea, K03).

**4.6 Counting vs timing rules (Kilpatrick and El Hady 2026).** With low patch variability, count rewards found. Once variability exceeds about 25 percent, time the gaps between rewards. In a scaffold: for stable operators use "N fruitless steps in a row"; for high-variance operators use time since last yield.

**4.7 Simple heuristics (Webb 2025, Wolfe, Hutchinson).** Constant time per patch, giving-up time, reward count. In mice at low noise constant time (4.88) matched optimal MVT (4.90). Reward count was worst (6.57). The fixed-budget baseline is strong; a yield rule must beat it.

**4.8 Accumulator view (Davidson and El Hady 2019, b26, not read).** Patch leaving as evidence accumulating to a bound, a bridge from MVT to drift-diffusion.

**4.9 Stochastic leave rule (a14).** Add noise to the threshold. Leave-time SD is 20 to 50 percent of the mean in animals and humans. For a scaffold, run-to-run variation of the switch step is normal; vote across runs rather than trusting one.

**4.10 LLM analogues.** Confidence exit (DEER, d02): at transition words ask for a trial answer, compute the mean max token probability, stop if it passes a threshold calibrated with median absolute deviation. Probe exit (d04): a linear probe on hidden states predicts whether an intermediate answer is right. Answer consistency (d03): stop when probe answers agree over a window of k steps. Sufficiency (SCOUT, c11): stop when a gap-diagnosis step says the evidence answers the query. These are level rules (is the answer good enough), not rate rules (is the gain falling below average). A rate rule would use the change in a chosen yield measure per step.

**4.11 Cheap yield measures in a reasoning scaffold.** Change in the probed answer between steps (d03). Trial-answer confidence (d02). Probe score (d04, open weights only). Marginal coverage per extra sample (d10). Count of new verified facts or constraints. Fresh versus repeated items in the last outputs (black-box proxy for K11). Which is best is untested (gap 2).

## 5. What holds up

**Replications and agreement.**
- Qualitative MVT sensitivity to travel and richness: monkeys (a04, a15), humans (a06, a07, a12, b06), rats (b08), mice (b14, a16), gerbils (a13), deep RL agents (c07, d14). Eight or more independent sources. The most solid result (K01).
- Overharvesting in monkeys, humans, rats, RL agents (K02). Six sources.
- Overharvesting is explained by learning and uncertainty (K03): absent in rich environments (t=1.38), shrinks with experience, explained by discounting (a12, c07).
- Bias against searching (K07): original (a02) and two Shenhav samples (a09). All in one task design.

**Failures, refutations and boundaries.**
- Neural: Kolling 2012 (dACC = foraging value) was challenged by Shenhav 2014 (dACC = difficulty) and answered by Kolling 2016. Contested, small samples (N=14-15). Not needed by the agent (K06).
- "All foragers overharvest" is a tendency, not a law. Gerbils did not; only some humans did (a13); rich environments show none (a12); Wolfe's observers left too early with mixed patches and slow travel (b06). Risk-sensitive modelling removes the bias in Constantino and Daw (p=.2, .10).
- Winning model flips with setting: baboons (c23), mice (a16). Contested (K04).
- Simple heuristics can match MVT at low noise (K05, single source, mice).
- Leave time varies within identical contexts. Stochastic choice vs learning noise is argued, not settled (K09).
- Wolfe Exp6 (no colour cue) showed leaving does not follow a rate rule when the rate is hard to see. In Wispinski a colour cue gave the instantaneous rate, which made estimation easy (limits of c07). MVT works when the yield signal is visible. For an LLM, yield is hard to see.
- Apathy study: cost-insensitivity effect held in discovery (449) but missed in confirmation (756) (b11).
- The Hayden likelihood ratio (about 1.3e52) is odd and was not re-checked. Do not quote it (critique).

**Moderators that worked.** Travel time, depletion rate, starting reward (rats beta=2.294 trials), environment richness, experience (early vs late blocks), rare environment switches (t(115)=4.67), task framing (monkeys more patient when framed as foraging), stress (higher perceived stress, longer stay), dopamine (cabergoline changed the background-rate effect in poor environments, b10), adverse childhood experiences (explored less), serotonin activation in mice (more persistence).

**Interventions in LLM stopping work.**
- Worked: confidence early exit (DEER: chains 19.1-80.1% shorter, accuracy +0.3 to +5.0%); probe exit (about 24% fewer tokens at equal accuracy; 87.4% vs about 82.5% against a fixed-step exit); answer consistency (over 40% fewer tokens on NQ); self-training on first-correct solutions (d01); preference tuning for shorter answers (d07, accuracy "acceptable"); a penalty on thought switches for hard items (d06); step-efficiency penalty in RL retrieval (c10); sufficiency stop (c11); handing the model summary statistics (d11, c17) and tool use (d12, c18).
- Did not work or only partly: forced thinking beyond about 1,100 tokens (accuracy falls to 70.3%); too many budget-forced continuations (loops); summary statistics for small models (Gemma gained nothing); algorithm-guided support still far under UCB (60.0 vs 90.6); the efficiency penalty hurt on the authors' long-chain dataset (c10); steering works unevenly across models and layers (c04).

**Source quality.** Founding sources not opened. Hayden 2011, Constantino and Daw, Harhen t(115)=3.88 and Kane rat studies were read once and not re-verified by the critique. Ten numbers re-opened by the critique were all confirmed. Several 2026 arXiv items are unreviewed preprints, partly read.

## 6. Language models

**No direct test exists.** No paper runs an LLM through a Kolling or Constantino-Daw patch task with a depleting reward, and none uses "yield below running average" as a stop trigger (K15; c24, d18). The claim rests on arXiv listing pages and one web search, so it is weak evidence of absence.

**Semantic fluency (closest to MVT).**
- Llama-3 1B/3B/8B/70B on animal naming switch categories less than humans: switch ratio 0.40 vs 0.55 (p<0.0001), transition structure matches (Spearman 0.701); 699 human sequences, 681 human and 2285 LLM kept (b18, c01). They stay longer in a patch.
- A Llama 2 Chat 7B generator needed a global cue to switch (c05).
- Inside open models, switch probability rises as in-category items among the strongest concepts run out (r>=0.31, five models 2B-9B, c03). Steering moves Gemma-2-9B switch rate 0.29 to 0.70 or 0.07 (c04).
- A switch probe on natural human data is near chance (AUROC 0.57; output probabilities 0.751; c02).
- Limits: Llama-3 and animals only; workshop and preprint papers; frontier chat models untested (d17, K26).

**Overthinking is overstaying.** Reasoning models keep producing rounds after the first correct one (d01: over 92% of correct cases right in round one, under 60% of tokens; 1,953% more tokens than conventional models on 2+3). Answers settle after about 60% of steps (d03). Forced thinking has a peak (82.2 to 87.3 to 70.3 percent, d08). Repeated sampling gives log-linear coverage, so each sample adds less (d10). These are the yield curve of a depleting patch. The fixes found are level rules (confidence, consistency, sufficiency), not rate rules. Size: 19.1-80.1% fewer tokens (DEER), about 24% fewer at equal accuracy (probe), over 40% fewer on NQ.

**Underthinking is leaving too early.** On hard items wrong answers had 418% more thought switches and 225% more tokens (d05). Penalising switch tokens cut them on AIME2024 for DeepSeek-R1 from 13.8 to 5.7 and raised accuracy (d06). Length does not follow difficulty (d07). A leave rule tuned on easy items can hurt hard items; a dwell floor is needed (K22).

**Bandits (exploration).** Raw-history prompts fail to explore (over 60 percent of GPT-4 replicates had suffix failure; T=500, N=20). Summary statistics, chain of thought and tool use help (c17, c18, d11, d12). Even so Gemini-1.5 Pro reaches 60.0 against UCB at 90.6, and small Gemma models gained nothing from the given numbers (d11). Reasoning models exploit best but are slow (d12). Lesson: compute the statistic in code and hand it over, but do not assume the model uses it well (K14).

**Escalation and sunk cost.** Alone, LLMs mostly divest from a failing option; under peer deliberation 99.2% escalate vs 46.2% under hierarchy (d15; model names not captured). GPT-4o and Gemma 2 mostly recognised sunk-cost irrationality in vignettes (d16). A human-style bias against switching has not been measured in agents (K25).

**Retrieval agents with information foraging as metaphor.** InForage (RL, Qwen2.5 3B/7B, step penalty gamma^max(0,T-2)) beat Search-R1 variants (c10). SCOUT stops on evidence sufficiency at about a tenth of the tokens (c11). DeepNews reports a "knowledge cliff" under 15,000 retrieved characters (c12; one author, weak). The LLM-Foraging swarm paper used a hand-set 60 s starvation timer and gained +70% (c19). None tests an MVT rule.

**RL agents (not LLMs).** Recurrent deep RL agents learn near-MVT leaving and match discounted MVT (+0.9 steps, p=0.74); plain MVT overstay was +15.8 steps. DreamerV2 landed near the optimum; PPO did not (c07, c09).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Put a code-run leave check in S6; do not rely on the model's sense of being stuck.** Humans show a bias against switching (indifference 1.65 and 5.0, not 0) and LLMs switch less than humans in fluency and need a global cue. Part: S6, G1 (the check is a signal-driven trigger, not a schedule). [E] for the human bias; the LLM side is [S]. Evidence: a02, a09, b02, b18, c05.
2. **Compute the yield statistic in code and give it to the model.** Raw history fails (over 60% suffix failure); summaries and tools help (K14). Expect imperfect use (Pro 60.0 vs UCB 90.6). Part: S6, O, G5. [E]. Evidence: c17, c18, d11, d12, b21.
3. **Make the stop signal depend on yield over time, not on attempt count alone.** Counting rewards was the worst heuristic in mice (6.57 vs 4.88 for constant time). Part: S6. [S] (mice only). Evidence: a25, a16.
4. **Have a stop at all.** First rounds already hold most correct cases; confidence or consistency exits kept accuracy with 19-80% shorter chains; forced extra thinking eventually lowers accuracy (K17, K21). Fits G11 and G12. Part: S6, G11. [E]. Evidence: d01, d02, d03, d04, d08, d09, d10.
5. **Set the leave point on a pilot set from the marginal gain curve.** The yield curve has a finite peak; restarting beats staying late (K21). Part: S6, G7, G12. [E]. Evidence: d08, d09, d10.
6. **Give leave rules a dwell floor.** The mirror error exists: too-frequent switching goes with wrong answers on hard items (K22). A rule tuned on easy items must not cut off hard ones. Part: S6, G12. [S] (d05, d06, d07). Kept here as a safety guard; test it (U4). Evidence: d05, d06, d07.
7. **Include a fixed-budget-per-operator arm in every comparison.** Constant time matches MVT at low noise (K05) and G7 requires winning at equal tokens. Part: G7. [S]. Evidence: a25.
8. **Treat switch cost as an input.** Longer travel gives longer stays in animals, humans and RL agents (K01, K24). In a scaffold, cost of dropping an operator (context lost, setup tokens) should enter the rule. Part: S6. [E] in biology; scaffold effect untested. Evidence: a04, a07, b08, d14.

### Test first

- **Yield-below-running-average trigger** vs fixed-step and sufficiency stops at equal tokens (K15, K20). The S6 core; no test exists. [S]. Evidence: a06, a10, d04.
- **Patience margin** 0.8, 1.0, 1.2 times the average (K23). [S, theory]. Evidence: d13, c07, a12.
- **Which yield measure** (answer change, new verified constraints, confidence delta, fresh-item count). Evidence: d02, d03, d10, c03.
- **Bayesian per-operator yield estimate** vs running average (K04, [C]). Evidence: a16, b12, c23.
- **Yield memory across runs as a prior** (K03; [E] in humans, untested in agents). Evidence: a12, b07.
- **Noise regime switch** between count and time rules at about 25% variability (K19, [S], theory). Evidence: b13, c16.
- **Stochastic trigger or vote across runs** (K09, [C]). Evidence: a14, a13.
- **Social framing and multi-agent set-ups** worsen overstay (K25, [S]). Evidence: d15.
- **Black-box depletion proxy**: fresh vs repeated items in recent outputs (K11 without white-box access). Evidence: c03.

## 8. Concrete tests on our bench

All arms get the same total token budget per item, setup cost counted (G7). Report accuracy and accuracy per token, split by item difficulty and by operator.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed bench (ARC-style, brain teasers, reasoning items) where S6 picks among O1-O8 | (a) fixed step budget per operator; (b) sufficiency stop; (c) leave when recent yield < running average; (d) plain model | Accuracy per token; steps wasted after last useful yield | (c) over (a) and (b) by 2 to 5 points on mixed items; may tie on easy. Success: at least +2 points at equal tokens |
| T2 | Same, difficulty stratified | (c) with dwell floor of 0, 2, 4 steps | Accuracy on hard items; accuracy on easy items | Floor of 2 recovers hard-item loss, costs under 1 point on easy |
| T3 | Same | Threshold at 0.8, 1.0, 1.2 times running average | Accuracy per token; overstay vs rule | Best at 0.8 (more patient) per overharvest evidence; flatter curve with noisy yield |
| T4 | Same | Yield from (i) model estimate off raw transcript, (ii) code-computed statistic shown to model, (iii) code computes and code alone fires the leave | Accuracy per token; agreement of leave step with an oracle | (iii) >= (ii) > (i); (ii) well under (iii) for weaker models (d11) |
| T5 | Items with explicit switch cost: restart drops context vs keeps context | 3 cost levels (as in Kolling) | Dwell length | Dwell rises with cost (K01, K24) |
| T6 | Synthetic depleting-reward task (answer pool shrinks, e.g. list all items of a class), run as a Constantino-Daw style task | Cold start vs table of earlier yields | Overstay vs optimal rule; reward earned | Overstay shrinks with a yield table (K03) |
| T7 | Same item run 5 times | Fixed trigger vs stochastic trigger vs majority across runs | Variance of leave step; accuracy | Variance 20-50% of mean as in animals; vote helps if bias is run-level (K09) |
| T8 | Single agent vs multi-agent peer set-up on a failing line | Code leave check on or off | Escalation rate; tokens | Code check blocks peer escalation (d15) |
| T9 | Shenhav indifference-point task adapted: continue operator vs switch with stated gains | Frames: alone, peer | Gain needed before the agent switches vs zero | Shows if LLM agents have a switching bias; if indifference is above zero, add a margin |
| T10 | Semantic fluency on the current model (animals plus two other categories) | Plain vs prompt stating current yield | Switch ratio vs human 0.55 | Re-test of K26 on a frontier model |

## 9. What does not transfer, and why

- **Neural claims (dACC, vmPFC, serotonin, dopamine, cortisol).** Contested (K06) and irrelevant to a scaffold. Stress and apathy effects (K08) only show the threshold is tunable.
- **A known depletion curve.** MVT assumes g(t) is known and smooth. A reasoning step has no clean reward; yield is noisy and delayed, and an insight can follow a long flat stretch. Boundary cases: Wolfe Exp6 (no rate cue, no rate rule) and Zylberberg (when payoffs can rise, a shorter stay is optimal).
- **Physical travel time.** Switch cost in a scaffold is lost context and setup tokens. Whether context loss behaves like travel time is untested (gap 6).
- **Independent patches.** Foragers move to a fresh patch; an agent's next operator often inherits the failed trace and the same model's blind spots (G4). The next patch is correlated with the last.
- **Activation probes and steering vectors.** Need open weights and precomputed lenses; the natural-data probe is near chance (AUROC 0.57). Unusable on a closed frontier model.
- **Overstay as a pure bias.** Human overharvest is partly rational under uncertainty (Harhen). Forcing early leaving would be wrong where the environment is unstable or rich (no overharvest in rich patches, t=1.38).
- **Semantic fluency results.** Llama-3 and animal names; do not generalise to frontier chat models (K26).
- **Training-based fixes.** InForage, self-training for shorter chains, learned probes need training or white-box access. Our schema trains nothing.
- **Mouse heuristic parity (K05).** Comes from track tasks where travel and decay were set by track length.
- **Robotics (LLM-Foraging).** The 60 s starvation trigger is a hand-set timer, not a leave rule.

## 10. Open questions

1. Does a yield-below-average stop beat fixed-step and sufficiency stops on a language model at equal tokens? (K15, gap 1.)
2. What is the right yield for a reasoning step, and is it cheap enough inside the token budget? (Gap 2.)
3. Is the best threshold more patient than the plain average, and by how much? (Gap 3, K23.)
4. Which noise regime do hard items fall in; does the 25 percent variability switch have an LLM counterpart? (Gap 4.)
5. Does giving the model the computed number fix overstay, or does it ignore it on stopping tasks? Bandit results say partly. (Gap 5.)
6. What is the cost of switching in a scaffold, and does a higher cost lengthen stays? (Gap 6.)
7. Does a memory of earlier per-operator yields cut overstay as experience does in humans? (Gap 7.)
8. Do the fluency results hold for frontier models and other categories? (Gap 8.)
9. Do LLM agents show the human bias against searching? (Gap 9.)
10. Is the neural dispute (difficulty vs foraging value) of any use to the design? Probably not.
11. Why do rich environments show no overharvest, and does a rich enough item set in our bench behave the same?
12. Is the stochastic leave time (a14) an artefact of the model or a feature worth using as diversity?
13. Charnov 1976, Stephens and Krebs, Hills 2012 and Hutchinson 2008 were not opened; read them before citing exact rules.

## 11. Sources

[V] = opened and read this study (as marked in the evidence files). [M] = snippet, abstract listing or memory only.

Founding and theory
- [M] Charnov (1976) Optimal foraging, the marginal value theorem. https://doi.org/10.1016/0040-5809(76)90040-X
- [M] Charnov and Orians (1973) Optimal foraging: some theoretical explorations. https://www.jstor.org/stable/2459881
- [M] Stephens and Krebs (1986) Foraging Theory. https://press.princeton.edu/books/paperback/9780691084428/foraging-theory
- [V] Kilpatrick, Davidson, El Hady (2020) Normative theory of patch foraging decisions (abstract page only). https://arxiv.org/abs/2004.10671
- [V] Kilpatrick, Davidson, El Hady (2021) Uncertainty drives deviations in normative foraging decision strategies (abstract). https://pmc.ncbi.nlm.nih.gov/articles/PMC8277480/
- [V] Kilpatrick and El Hady (2026) Resource depletion accelerates rate learning but not richness learning (abstract and first page). https://arxiv.org/abs/2607.29476
- [M] Davidson and El Hady (2019) Foraging as an evidence accumulation process (downloaded, not read). https://pmc.ncbi.nlm.nih.gov/articles/PMC6682163/
- [V] Zylberberg (2024) Generalized marginal value theorem. https://www.biorxiv.org/content/10.1101/2024.10.28.620618

Human and animal behaviour
- [V] Kolling, Behrens, Mars, Rushworth (2012) Neural mechanisms of foraging. https://pmc.ncbi.nlm.nih.gov/articles/PMC3440844/ (Science DOI [M]: https://doi.org/10.1126/science.1216516)
- [V] Shenhav, Straccia, Cohen, Botvinick (2014) ACC engagement in a foraging context reflects choice difficulty. https://pmc.ncbi.nlm.nih.gov/articles/PMC4156480/
- [V] Kolling et al. (2016) Value, search, persistence and model updating in ACC. https://pmc.ncbi.nlm.nih.gov/articles/PMC7116891/
- [V] Hayden, Pearson, Platt (2011) Neuronal basis of sequential foraging decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC3553855/
- [V] Constantino and Daw (2015) Learning the opportunity cost of time. https://pmc.ncbi.nlm.nih.gov/articles/PMC4624618/
- [V] Blanchard and Hayden (2015) Monkeys are more patient in a foraging task. https://pmc.ncbi.nlm.nih.gov/articles/PMC4324901/
- [V] Harhen and Bornstein (2023) Overharvesting reflects rational structure learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC10068834/
- [V] Kane et al. (2019) Rats exhibit similar biases in foraging and intertemporal choice. https://pmc.ncbi.nlm.nih.gov/articles/PMC6794087/
- [V] Kane et al. (2022) Rat ACC continuously signals decision variables. https://pmc.ncbi.nlm.nih.gov/articles/PMC9302469/
- [V] Guldener et al. (2024) Patch leaving in humans and gerbils. https://pmc.ncbi.nlm.nih.gov/articles/PMC11327252/
- [V] Stochastic choice drives variability in patch foraging (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13447090/ ; bioRxiv version [M] https://www.biorxiv.org/content/10.1101/2025.10.28.685063.full.pdf
- [V] Social information foraging in macaques follows the MVT (Sci Rep 2017). https://pmc.ncbi.nlm.nih.gov/articles/PMC5596022/
- [V] Webb et al. (2025) Dynamic Bayesian updating to model meta-uncertainty in mice. https://pmc.ncbi.nlm.nih.gov/articles/PMC12068741/
- [V] Wolfe (2013) When is it time to move to the next raspberry bush? https://pmc.ncbi.nlm.nih.gov/articles/PMC4521330/ (journal DOI [M] https://doi.org/10.1167/13.3.10)
- [V] Lenow et al. (2017) Chronic and acute stress promote overexploitation. https://pmc.ncbi.nlm.nih.gov/articles/PMC5469305/
- [V] Dopamine modulates dynamic decision-making during foraging (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7329313/
- [V] Apathy and compulsivity on planning and stopping (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8970514/
- [V] Lottem et al. (2018) Serotonin neurons promote active persistence. https://pmc.ncbi.nlm.nih.gov/articles/PMC5843608/
- [V] Adverse childhood experiences and exploration (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8794829/
- [V] Neural evidence of switch processes in semantic and phonetic foraging (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10589708/
- [M] Hutchinson, Wilke, Todd (2008) Patch leaving in humans. https://doi.org/10.1016/j.anbehav.2008.06.008
- [M] Hills, Jones, Todd (2012) Optimal foraging in semantic memory. https://doi.org/10.1037/a0026299
- [M] Marshall et al. (2013) How do foragers decide when to leave a patch? Baboons. https://openresearch-repository.anu.edu.au/items/e71277a0-d39a-49dd-b830-d4b54716e5f3
- [M] Spontaneous thought transitions follow a foraging-like policy (bioRxiv 2026). https://doi.org/10.64898/2026.09.07.749780

RL and LLM studies
- [V] Wispinski et al. (2023) Adaptive patch foraging in deep RL agents. https://arxiv.org/abs/2210.08085
- [V] Fonseca et al. (2025) World models unlock optimal foraging. https://arxiv.org/abs/2512.12548
- [V] Lacosse, Duarte, Todd, McNamee (2026) Semantic fluency in LLMs. https://arxiv.org/abs/2603.01822
- [V] Leckie, Todd, Foster (2026) Signatures of semantic search in LLM activations. https://arxiv.org/abs/2609.35599
- [V] Heineman, Koenen, Varma (2024) Path dependent category fluency. https://arxiv.org/abs/2405.06714
- [V] Moore (2025) Optimal foraging in memory retrieval. https://arxiv.org/abs/2511.12759
- [V] Binz and Schulz (2023) Cognitive psychology of GPT-3. https://pmc.ncbi.nlm.nih.gov/articles/PMC9963545/
- [V] Krishnamurthy et al. (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371
- [V] Harris and Slivkins (2026) Should you use your LLM to explore or exploit? https://arxiv.org/abs/2502.00225
- [V] Nie et al. (2024) EVOLvE. https://arxiv.org/abs/2410.06238
- [V] Chen et al. (2024) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187
- [V] Yang et al. (2025) Dynamic Early Exit in Reasoning Models. https://arxiv.org/abs/2504.15895
- [V] Liu and Wang (2025) Answer convergence as a signal for early stopping. https://arxiv.org/abs/2506.02536
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419
- [V] Wang et al. (2025) Thoughts are all over the place (underthinking). https://arxiv.org/abs/2501.18585
- [V] Su et al. (2025) Between underthinking and overthinking. https://arxiv.org/abs/2505.00127
- [V] Ghosal et al. (2025) Does thinking more always help? https://arxiv.org/abs/2506.04210
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393
- [V] Brown et al. (2024) Large language monkeys. https://arxiv.org/abs/2407.21787
- [V] Qian and Liu (2025) Scent of Knowledge (InForage). https://arxiv.org/abs/2505.09316
- [V] Zhang et al. (2026) SCOUT. https://arxiv.org/abs/2605.04496
- [V] Jiang (2025) DeepNews. https://arxiv.org/abs/2512.10121
- [V] Ragavan and Alipour (2024) Revisiting human information foraging. https://arxiv.org/abs/2406.04452
- [V] Azzopardi and Roegiest (2026) Information farming. https://arxiv.org/abs/2601.12544
- [V] Li et al. (2026) LLM-Foraging swarm robots. https://arxiv.org/abs/2605.01461
- [V] Barkett, Long, Kroger (2025) Big-Muddy escalation. https://arxiv.org/abs/2508.01545
- [V] Cognitive biases in LLMs incl. sunk cost (2024). https://arxiv.org/abs/2410.02820
- [V] arXiv listing search for "patch foraging" and "marginal value theorem", 1 Nov 2026 (gap note). https://arxiv.org/search/?query=patch+foraging&searchtype=abstract

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.08-K01** (reworded: the sources support less). Under MVT a richer environment lowers stay time (higher leaving threshold); sources show thresholds fall in poorer environments (longer travel, steeper depletion), so 'stay longer when the environment is richer' is reversed; richness only raises stays at the patch level. Corrected claim: Humans, monkeys, rats and mice all follow the marginal value theorem qualitatively: they stay longer (leave at a lower reward threshold) when travel is longer or the environment is poorer, and leave at a higher threshold in richer environments; they also stay longer in richer patches.
- **B02.08-K03** (reworded: the sources support less). Harhen and Bornstein explain overharvesting with their own model in one human task; Constantino and Daw still find a significant residual overharvesting bias in the MVT learning model, and Kane's rats overharvested in every condition. Corrected claim: A learning-and-uncertainty account (rich-poor mix, uncertainty-adaptive discounting) explains much of human overharvesting in one task (Harhen and Bornstein 2023): it shrank with experience and was absent in rich environments; but a residual overharvesting bias remains in other human work (Constantino and Daw 2015) and rats overharvested in every condition (Kane 2019).
