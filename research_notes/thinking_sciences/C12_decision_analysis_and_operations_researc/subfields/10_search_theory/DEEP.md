# Search theory: deep document

*Subfield C12.10, decision analysis and operations research. Brief: "Where to look when finding costs." Key works: Koopman; job and price search. Priority: Low, background only. Evidence: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c26, d01-d16), claims.jsonl (K01-K20), critique.md. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Search theory asks one question. Looking costs something. Where should you look next, and when should you stop?

It has four classic branches.

1. **Search for a hidden target** (Koopman, WWII; Stone). Keep a probability map over places. Look where probability times detection chance per unit cost is highest. After an empty look, update the map by Bayes' rule.
2. **Economic search** (Stigler 1961-62, McCall 1965-70). A buyer or job seeker samples offers at a cost. Stigler fixes the sample size in advance. McCall lets the searcher stop after each offer, with a reservation value.
3. **Search for the best of several costly options** (Weitzman 1979, "Pandora's box"). Each option has an opening cost and a random prize. Each gets an index. Open in index order and stop when the best prize beats all remaining indices. It is a special case of the Gittins index.
4. **Stopping problems and foraging** (secretary problem, Charnov's marginal value theorem). Decide when to commit or when to leave a patch.

For our agent the field is background. It does not give a new operator. It gives a clean way to think about three decisions the schema already makes: which check to run next, when to stop sampling or checking, and when to leave a line of reasoning. The strongest new LLM evidence is about stopping (Section 6). Evidence on "which check next" by an index rule is thin and in one case negative.

## 2. History and theories in depth

**Koopman and Morse (1940s).** Bernard Koopman worked in the US Navy anti-submarine group (ASWORG, led by Morse). His report *Search and Screening* (OEG Report 56, 1946) was the first theory of searching for a hidden target. It stayed confidential until 1958 (a01). Our sources do not describe his lateral range curves or the random-search formula. Only the Wikipedia summary was read, so those details are not confirmed here.

**Bayesian search and Stone (1960s-2011).** Bayesian search was used for USS Thresher (1964) and USS Scorpion (lost May 1968, found end October 1968, about 740 km south-west of the Azores, under over 3,000 m of water). Stone's *Theory of Optimal Search* won the 1975 Lanchester Prize. Stone et al. (2011) used it for the Air France 447 recorders (a04, b21). These facts are from secondary summaries. No success rate or count of failed hunts is available.

The update rule (a02): with prior p in a cell and detection chance q, an empty look gives p' = p(1-q)/(1-pq). Every other cell with prior r becomes r/(1-pq). The rule fails if q is overestimated, because the true cell is then wrongly dropped.

The boxes rule (a03): for one hidden object in independent boxes, always look in the box with the highest p_i * a_i / c_i (prior, times detection chance, over cost). Blackwell solved the one-object case, Assaf extended it. It is a special case of the Gittins index. The formula was garbled in extraction, so it is read as p_i a_i / c_i.

**Stigler (1961, 1962).** Stigler framed price and job search as economics (a05, a06). In the 1961 fixed-sample model the buyer picks n quotes ahead and minimises expected price plus n times the cost per quote. A simultaneous sample is not optimal when one can look one at a time. The 1962 labour paper measured dispersion for equal workers: 44 Chicago MBA graduates received 144 offers in 1960-61; mean monthly offer $540.7, SD $43, coefficient of variation 7.9%, 2.25 offers per student. A national survey gave CV 6.4-9.1% for non-engineers and about 4.0-4.3% for engineers. Company offers to engineers correlated 0.660, 0.761 and 0.577 across years (a24). Persistent dispersion means search keeps paying. Limits: starting salaries only, one school, scanned-text OCR.

**McCall (1965, 1970).** McCall made search a sequential optimal stopping problem (a07, a08). With a known offer distribution the best rule is a reservation wage: reject below, accept above. A higher offer variance raises the reservation wage and lengthens search, even for a risk-averse searcher, because bad offers can be refused. Assumptions: known fixed distribution, constant value of money. The reservation wage falls if the worker loses skills or runs out of money. Sequential models assume the buyer cannot learn the distribution while searching.

**Secretary problem (1960s).** With n candidates in random order, no recall, and rank-only information, reject the first n/e and take the next best-so-far. Win probability tends to 0.368. Exact values: n=2 0.500, n=3 0.500, n=4 0.458, n=5 0.433, n=10 0.399; cutoffs r = 1,1,2,2,3,3,3,4,4,4 for n=1..10 (a14). With cardinal values the cutoff is earlier. Original papers not opened.

**Weitzman (1979), Pandora's box.** Each box i has cost c_i and random prize v_i. Give each box a reservation value sigma_i solving E[(v_i - sigma_i)+] = c_i. Open boxes in decreasing sigma. Stop when the best prize found exceeds every unopened sigma. First-best welfare is E[max_i min(sigma_i, v_i)] (a10, a11). Assumptions: independent boxes, known distributions, instant inspection, the cost is paid even if the prize is taken. Weitzman's own paper was not opened; the rule is read from Kleinberg et al. and Kalayci et al. Gittins and Jones (1979) reached the same index idea for discounted bandits (a13). Olszewski and Weber (2015) and Doval (2014) extend it (a25, reference list only).

**Kleinberg, Waggoner, Weyl (2016).** They read the index as a real option: sigma is the strike price, the highest price at which paying to look still pays. A descending-price procedure makes bidders reproduce the optimal search, because the price is guaranteed when information is bought. Their calibrations (start-up acquisition, timber auctions) put coordination losses one to two orders of magnitude above ex-ante asymmetry losses (a11, c22).

**Charnov (1976), marginal value theorem.** Leave a patch when its current capture rate falls to the average rate over the whole environment, travel included (a17). Field support is rough: great tits foraged about 30% better than random (Naef-Daenzer 1999); yellow dung flies predicted 40 min, observed 36 min (Parker 1999); armadillos and guinea pigs stayed longer than predicted (Cassini 1990). Animals tend to stay longer than the theory says.

**Correlated options (2020).** Chawla et al. show Weitzman's independence assumption breaks in real settings. Fully adaptive strategies cannot be approximated within any sub-linear factor from samples. A fixed probe order with adaptive stopping is a constant-factor approximation to the best such strategy (a12, d12).

**Cost-aware optimisation (2024-2026).** Xie et al. use the Pandora's-box Gittins index as an acquisition rule with a stopping rule for Bayesian optimisation; it is a heuristic when values are correlated. Only the abstract was read (d13).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Bayes update after an empty look | p' = p(1-q)/(1-pq); others r/(1-pq) | a02 | [E] |
| Optimal box order for one hidden object | highest p*a/c | a03 | [E] |
| Pandora's rule is optimal for independent boxes | sigma from E[(v-sigma)+]=c; welfare E[max min(sigma,v)] | a10, a11 | [E] |
| Secretary 1/e rule | 0.368 limit; n=10: 0.399, cutoff 4 | a14 | [E] |
| Wage dispersion exists, so search pays | 44 MBAs, 144 offers, CV 7.9%; year-to-year r 0.58-0.76 | a06, a24 | [E] |
| Lab subjects under-search (Japan, 103 students) | searches 3.10/3.13/3.38 vs optimum 4.54; payoffs 8.30/8.44/8.41 vs 9.03 (gaps n.s.) | b01 | [E] direction; effect sizes single-lab |
| Under-search costs little profit | Marcu and Noussair: 177 students, 180 problems each; lower freeze fee increased under-search | b04, b05 | [E] |
| Rival explanations do not beat plain model | regret, sunk cost, misperceived horizon, risk aversion all failed to improve fit | b06 | [E] (one design) |
| Risk preference predicts search length only in the passive design | Holt-Laury; prior studies disagree | b03 | [C] |
| People recall old offers rarely | about 12% (11.2-12.8%); termination about 30% per search | b02 | [S] |
| Repeated secretary game: people learn fast | 6,537 players, 48,336 games; optimal win 62.2% (7 boxes), just under 60% (15); humans within 5-10 points after a few games | b11 | [S] |
| First-game errors go both ways | about 25% stop below critical value; at most 75% above | b12 | [S] |
| Progressive stopping heuristic | over 95% of optimal on three multi-threshold variants; 98.5% for n up to 100,000 (related rule) | b13 | [C] simulation only |
| Humans in fuse-or-extract game stop wrongly | 210 people; optimal switch at step 9 chosen by 32%; at step 0 by 18% | b15 | [S] |
| LLMs stop at the wrong step | GPT-4 and Llama switch at step 5 where optimum is 9 or 0; GPT-3.5 switch-once 71.4%/14.3%/57.1%/28.6% | b16, c01, c02 | [S] |
| Formula alone does not fix LLM stopping; explaining the example helped | CoT prompt reached optimum in some cells only | b17, c03 | [S] |
| LLMs lock into greedy arm in bandits | GPT-4 basic prompt: suffix failure in over 60% of replicates; only one configuration worked | a18, c09, c10 | [E] |
| Hard bandit, T=100 | median reward UCB 0.55, Thompson 0.47, Greedy 0.40; one LLM config 0.68; BNRND 0.33 | c10 | [S] |
| GPT-3 beat humans on regret, with no directed exploration | regret 2.72 vs 3.24, t(38878)=-5.03; short horizon t(5566)=-0.043; long horizon t(5550)=-4.07 | a19, c11, c12 | [S] |
| Early-stopping self-consistency | samples cut 33.8% MATH, 80.1% GSM8K, 76.8% StrategyQA, 78.5% CSQA, 84.2% Coin Flip, 67.4% Last Letters; GPT-4 MATH 60.32 both | a20, c07, c08 | [E] |
| Adaptive-Consistency | up to 7.9x fewer samples, under 0.1% accuracy drop | d08 | [E] |
| Confidence-weighted voting | over 40% fewer paths; Gemma2-9B MATH 73% cost cut | d07 | [E] |
| DeepConf | GPT-OSS-120B AIME25 99.9% vs 97.0% maj@512; tokens cut up to 84.7%; low variant 43-79%, one set -0.9% | d06 | [E] with overconfidence limit |
| DEER early exit | CoT length cut 19.1-80.1%, accuracy +0.3 to +5.0%, 11 models, 10 benchmarks | d09 | [S] |
| Pandora's-box stopper for sampling | 15-35% fewer generations at equal quality; win rate above 54%; 1,600 profiles | b18, c04, c05, d14 | [S] |
| Bayesian precision stopping for evals | 57.2-97.3% fewer trials, mean 81.1%; mean deviation 0.006 | b19 | [S] |
| Coverage rises log-linearly with samples | SWE-bench Lite 15.9% to 56% at 250 (single-sample SOTA 43%); MATH Llama-3-8B coverage 82.9% to 98.44% but vote/RM 40.50% to 41.41% | a21 | [S] |
| Adaptive compute by difficulty | about 4x less compute than best-of-N in some settings; small model beats 14x larger on easy and intermediate questions, not reliably hard | a23, d11 | [E] |
| Hidden-state probe predicts difficulty | up to 50% less compute at equal quality (code); up to 10% quality gain at fixed budget | d10 | [E] (needs hidden states) |
| Tree of Thoughts, Game of 24 | CoT 4% vs ToT 74% (GPT-4) | a22 | [S] |
| Gittins rule on PRM tree search gave no gain | 70.5-71.4% vs 71.6-71.9% (greedy, beam); GBFS 46.0 | d02 | [S] |
| Online Weitzman indices beat FrugalGPT cascade | simulation: 3 APIs, 30,000 periods; known/unknown-reward gap about 0.17% of oracle | d01 | [S] simulation |
| Reasoning models help bandit exploration but not enough | all LLMs lose to linear regression; o1-mini vs GPT-4o took linear regret to PSRL-level in one task | d03, d04 | [C] |
| Length-incentivised RL | in-domain +4.4%, out-of-domain +2.7% | d05 | [S] |
| No Stigler/McCall test with LLM subjects exists | Horton's Homo Silicus has no search task | d15 | [S] |
| Marginal value theorem field fit | tits about 30% better than random; dung flies 36 vs 40 min | a17 | [S] |

## 4. Mechanisms and models

Each is written so an engineer can code it.

**4.1 Probability map with a detection model (a02, a03).**
State: hypotheses H_1..H_n with priors p_i (sum to 1), check cost c_i, detection chance a_i (probability the check shows the truth if H_i is true).
Loop: pick i = argmax p_i * a_i / c_i. Run the check. If it finds the target, stop. If empty, set p_i' = p_i(1-a_i)/(1-p_i a_i); every other p_j' = p_j/(1-p_i a_i). Repeat until the budget ends.
Hazards: a_i must be honest. If the check is weak and you set a_i too high, the true hypothesis is dropped. One hidden target only. In code, the checks must be real tool runs, not model opinion (G2, G10).

**4.2 Pandora's rule (a10, a11).**
For each option i with known value distribution v_i and cost c_i, solve E[(v_i - s)+] = c_i for s_i (a one-dimensional root-find; the left side falls as s rises). Sort by s_i descending. Open the next box. Keep best = max prize found. Stop when best >= the largest remaining s_i. Take best.
Reading: s_i is the price at which the option is just worth looking at. A box with high variance gets a high s_i even if its mean is low.
Limits: independence, known distributions, no discounting beyond cost.

**4.3 Reservation threshold for sequential offers (a07).**
Offers X_t iid, cost k per look. Reservation x* solves E[(X - x*)+] = k. Accept the first X >= x*. Higher variance raises x*. With a finite horizon, x* falls as the horizon shrinks (backward induction: x*_t equals the value of continuing).

**4.4 Secretary rules (a14, b13).**
Rank-only, no recall: skip the first n/e, then take the next best-so-far. Cardinal values: earlier cutoff. Multi-threshold variants: progressive stopping, a rule on the ratio of interviewed to remaining, said to reach over 95% of optimal in simulation (b13).

**4.5 Adaptive stopping of repeated sampling (a20, d08, b18).**
- Window agreement (ESC): draw answers in windows of size w (8 for MATH, 5 for others); stop if a whole window is unanimous; max L (64 MATH, 40 others).
- Bayesian stopping (Adaptive-Consistency): stop when the posterior probability that the current majority stays the majority exceeds a threshold. Needs comparable answers.
- Pandora stopper (Kalayci): each generation is a box; keep an upper-confidence estimate of the acceptance rate; stop when the best reward found beats the threshold. Rewards are normalised across prompts by a Bradley-Terry style transform. The optimism term prevents premature stopping (c06). It needs a reward model.
- Precision stopping for evaluations (Pilditch): stop when the credible interval width reaches a target (0.05, 97% intervals).

**4.6 Confidence-based abandon (d06, d09).**
DeepConf: track token confidence per trace; drop traces whose recent confidence falls below a percentile threshold. DEER: at reasoning transition points ask for a trial answer; stop if its confidence is high. Both are marginal-value stops for a single chain. Both break where the model is confidently wrong.

**4.7 Per-prompt budgets (a23, d10, d11).**
Estimate a difficulty bin. Give easy prompts a small budget, mid prompts more, hard prompts less (extra compute helps hard prompts least). Difficulty sources: oracle bins, PRM scores, hidden-state probe. For API-only use a pilot of a few samples and the agreement rate (no verified result; K20).

**4.8 Marginal value theorem (a17).**
Track the rate of progress on the current line (checks passed or hypotheses eliminated per token). Leave when it falls to the average rate over the whole task, including the switching cost. Not tested on LLM reasoning in our sources.

**4.9 Correlated hypotheses fallback (a12, d12).**
Fix a probe order, stop adaptively. This is the provable constant-factor fallback. Fully adaptive index rules have no efficient approximation under correlation.

## 5. What holds up

**Held up.**
- Index and Bayesian theory: mathematically established. Operational use is documented only through secondary summaries (K14).
- Human under-search: the direction is reported across designs and decades (Cox and Oaxaca 1989, Sonnemans 1998, Kittaka 2021, Marcu and Noussair 2022). Only Kittaka (b01-b03) and Marcu and Noussair (b04-b07) were opened. Older primaries (b08-b10, b23, b24) are secondhand.
- Under-search is cheap. Payoff gaps were not significant in Kittaka (8.30-8.44 vs 9.03).
- Adaptive stopping of sampling: five independent lines (ESC, Adaptive-Consistency, CISC, DeepConf, Kalayci) save tokens with small accuracy change.
- Per-prompt allocation: Snell and Damani agree in direction.

**Failed or weakened.**
- Rival theories of under-search (regret, sunk cost, misperceived horizon, risk aversion) did not beat the plain model in one design (b06). Risk preference mattered only in the passive design (b03). Prior studies disagree about risk versus loss aversion (Schunk 2009 vs Miura 2017, Bhatia 2021).
- Gittins on PRM-guided tree search: no gain, because the value estimate was poor (d02).
- Progressive heuristics: simulation only, no human replication (b13). Contested.
- Snell's predicted difficulty bins lose gains at higher budgets, and the cost of estimating difficulty was not charged (d11).
- DeepConf overconfidence: aggressive filtering can hurt where the model is confidently wrong; one set lost 0.9% (d06).
- Reward-model-free stopping works on single-answer math; no evidence for open-ended tasks (critique).

**Moderators.**
- Design: passive vs active search changes how much people under-search (b01: 3.095 vs 3.380 searches). Recall option and freeze fee change under-search (b05).
- Learning: repeated play with a learnable distribution brings people near optimal in a few games (b11); one-shot play does not. First-game errors go both ways, so "stops early" is not universal.
- Task: stopping savings are larger on easy tasks (ESC 84.2% Coin Flip vs 33.8% MATH).
- Model: reasoning models help exploration but do not remove the failure (d03, d04).

**Interventions that worked.** Explore hint plus external per-arm summaries plus chain of thought (GPT-4, a18). External posterior sampling with LLM sub-calls (d04). Explaining why an example is optimal (c03, partial). Agreement or confidence stopping (d06-d09). Hidden-state difficulty probe (d10). Length-incentivised RL (d05, outside our scope).

**Interventions that did not work.** Giving the MDP formula (c03). Raw history in the prompt (a18). PRM value in Gittins sampling (d02). Stopping without an optimism bonus (c06).

**Data quality notes (from critique).**
- Binz and Schulz: a19 and c11 are one paper; count once. Goldstein: b11 and c17 are one paper. Duplicate lines: b15-b17 = c01-c03; b18 = c04; b19 = c15; a18 = c09.
- The Zhang and Zhao numbers could not be re-verified in the last session.
- Pilditch has an internal inconsistency in the GPQA item count; efficiency numbers are unaffected.
- Snell: the paper says "about 4x less test-time compute" in some settings. Do not write "4x better in general".
- Classical numbers (Koopman, Gittins, Weitzman, secretary rule, MVT) come mostly from Wikipedia and citing papers.

## 6. Language models

**Exploration in context.**
- Krishnamurthy et al. (2024): GPT-3.5, GPT-4, Llama2 in bandits mostly fail to explore. Failure modes: suffix failure (greedy lock-in) and uniform behaviour. GPT-4 basic prompt: suffix failure in over 60% of replicates. 48 configurations each for GPT-3.5 and Llama2, 72 for GPT-4; only one worked: explore hint, external per-arm summaries, chain of thought. Avoiding lock-in sometimes lost reward through dithering (BNRND: 0 suffix failures, median reward 0.33).
- Binz and Schulz (2023): GPT-3 regret 2.72 vs human 3.24 (t(38878) = -5.03) but no directed exploration and no horizon effect. Low regret can hide failure to explore.
- Harris and Slivkins (2026): reasoning models exploit best but are slow and costly; tools and summaries help on medium tasks; every LLM still loses to linear regression. As candidate proposers LLMs scored 0.5-0.6 vs random below 0.1 on a contrarian task (d03).
- Arumugam and Griffiths (2026): moving from GPT-4o to o1-mini changed linear regret to PSRL-level regret in one stochastic task, using an external PSRL algorithm with LLM sub-calls (d04).
- Wang et al. (2026): long traces covering many states are exponentially unlikely under autoregressive sampling ("Shallow Exploration Trap"). Length-incentivised RL: +4.4% in-domain, +2.7% out-of-domain (training; d05).
- EVOLvE (d16) was only skimmed; no numbers used.

**Stopping decisions.**
- Zhang and Zhao (2024): LLMs in a fuse-or-extract game. Where humans stopped too early, LLMs stopped earlier. Where the optimum was to extract at once, LLMs over-explored. No learning across rounds. The formula plus an example did not fix it. Asking for an explanation of why the example is optimal moved models to the optimum in some cells. Small, preliminary, not re-verified.

**Stopping repeated sampling (the best-supported use).**
- ESC (2024): 33.8-84.2% fewer samples, same accuracy; sample-matched SC lost up to about 30 points on weaker models.
- Adaptive-Consistency (2023): up to 7.9x fewer samples, under 0.1% loss.
- CISC (2025): over 40% fewer paths.
- DeepConf (2025): up to 84.7% fewer tokens; low variant 43-79%.
- DEER (2025): chains 19.1-80.1% shorter, accuracy +0.3 to +5.0%.
- Kalayci et al. (2025): 15-35% fewer generations at equal reward; win rate above 54%; needs a reward model. Small open models (Llama-3.1 8B, Mistral 7B, Qwen-2.5 7B).
- Pilditch (2026): 57.2-97.3% fewer evaluation trials.
- Caveat: baselines are usually fixed-N voting or unrestricted reasoning, not a tuned fixed budget at equal tokens. The exception is Kalayci's tuned best N, which the adaptive rule beat "in nearly all cases".

**Index rules on agent choices.**
- Belloni et al. (2026): learned Weitzman indices for which LLM API to call next beat a fixed FrugalGPT cascade in simulation only (d01).
- Cinquin et al. (2025): a Gittins sampling rule in PRM-guided tree search gave 70.5-71.4% vs 71.6-71.9% for greedy or beam (23 problems, Qwen2.5-Math-7B). The authors blame the PRM value estimate.
- Jain and Krishnamurthy (2025): optimal stopping as a threshold curve in belief space for herding and for switching large to small LLMs; small real-LLM tests (c13, c14).

**Compute allocation.** Snell (2024): about 4x less compute than best-of-N in some settings; a small model with extra compute beats a 14x larger one on easy and intermediate questions. Brown (2024): coverage 15.9% to 56% on SWE-bench Lite at 250 samples, but vote or reward-model selection plateaus (40.50% to 41.41% on MATH where coverage reaches 98.44%). Yao (2023): Game of 24 from 4% to 74% with tree search.

**Not found.** No LLM study tests Koopman's allocation. None tests a Stigler or McCall search with LLM subjects (Horton has no search task, d15). None tests a Weitzman index on an agent's own tool calls or hypothesis checks. None tests a marginal-value rule for leaving a reasoning branch at equal tokens. Cross-task memory of thresholds is untested (Kalayci learns within one run).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Stop repeated sampling by agreement (window or Bayesian stop) rather than a fixed N, on single-answer tasks. Keep a minimum sample count. | G11/G12 budget; O sample-and-vote | [E] | a20, c07, c08, d08, d07 |
| Stopping and confidence signals must be backed by an answer that can be compared. Do not use confidence alone where the model is confidently wrong. | G10, G4 | [E] | d06, d07, d08 |
| Raw history is not enough for choosing what to try next. Keep external per-option summaries (counts, outcomes) computed in code, and say "explore" explicitly. | G5 (code selects), O choice | [E] | a18, c10, d04 |
| Allocate budget by difficulty; do not use a uniform budget. Say "about 4x in some settings", not "4x in general"; weak on the hardest items. | G12, S0 | [E] | a23, d10, d11 |
| Bayesian update after a failed check done in code: p' = p(1-q)/(1-pq), with q honest and set low when the check is weak. | O (what to check next), G2 | [E] (math) | a02, a03 |
| Treat independence as a known limit. With correlated hypotheses use fixed order plus adaptive stop. | O | [E] (theory) | a12, d12 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Order checks by p*a/c when check costs differ, versus a fixed order. | O | [S] | a03, d01 |
| Pandora-style stopper on sampling with a verifier or reward model. | G budget | [S] | b18, c04, d14 |
| Confidence- or trial-answer-based early exit inside a single chain. | G11 | [S] | d06, d09 |
| Marginal-yield rule for abandoning a reasoning branch. | G1, S control | [S] | a17, d02 |
| Pilot agreement as the difficulty signal for the budget. | S0, G12 | [S] | d10, d11 |
| Memory of past stopping thresholds across tasks. | memory | [S] | b11, b12 |
| Forced explain-the-optimum step for stop and switch decisions. | G | [S] | c03 |
| Threshold escalation from cheap to expensive model. | G | [S] | c13, d01 |
| Progressive stopping for choosing when to commit to a candidate answer. | G | [C] | b13, b14 |

Do not add: an LLM-judged value estimate as the input to an index rule (d02). No operator is added. This field only tunes G11 and G12 and the choice of next check in O.

## 8. Concrete tests on our bench

All arms at equal total tokens, including pilot, setup and index computation cost (G7).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Single-answer math and reasoning items | Fixed N vote vs window-agreement stop (w 4-8) vs Bayesian stop | Accuracy per 1,000 tokens | Same accuracy at 30-60% fewer tokens (ESC range) |
| T2 | Same items plus a verifier-checked set | Window agreement vs token-confidence stop vs trial-answer stop | Accuracy per token; error on confidently-wrong items | Agreement beats confidence on confidently-wrong items |
| T3 | Synthetic hypothesis tasks: n hypotheses, unequal check costs, imperfect checks | Fixed order vs random vs p*a/c order | Mean cost to find the target; success within budget | Index order lowers cost; gain grows with cost spread |
| T4 | T3 with correlated hypotheses (known correlation) | Independent index vs fixed order plus adaptive stop | Cost to find target | Gap shows the price of independence |
| T5 | Mixed difficulty items | Uniform budget vs pilot-agreement adaptive budget | Accuracy at equal total tokens, pilot cost charged | Gain on mid-difficulty items; none on hard |
| T6 | Bandit and search task with 5-20 options | Raw history vs external per-option summary vs summary plus explicit explore instruction | Cumulative regret; suffix failure rate (best option never picked after step T/2) | Suffix failure falls from high to low |
| T7 | Fuse-or-extract finite-horizon game (Zhang and Zhao design) | Direct vs formula-plus-example vs forced explain-the-optimum | Distance of switch step from optimum | Less early or late bias |
| T8 | Repeated search tasks with a fixed hidden distribution | No memory vs memory of past thresholds | Win rate over games 1-10 | Near-optimal after a few games |
| T9 | Multi-step reasoning with several branches | Fixed depth vs marginal-yield abandon rule | Accuracy per token | Gain only if branch value is calibrated |
| T10 | McCall job-search task with LLM subjects | Direct play vs reservation rule given | Regret versus the optimum | Reveals the LLM bias direction (open) |
| T11 | Cheap and expensive model | Fixed routing vs threshold escalation | Accuracy at equal cost | Small gain; compare with always-cheap |

## 9. What does not transfer, and why

- **Hidden-target maps from naval search.** Physical detection chances are measurable. For an LLM check, the detection chance q is unknown, and an overestimate drops the true hypothesis (a02).
- **Reservation values need known distributions.** An agent rarely knows the value distribution of its options. Kalayci learns it online but with a reward model.
- **Independence.** Hypotheses and reasoning samples are correlated (G4: samples from one model are not independent). The exact index rule is lost (d12).
- **Human under-search lessons.** Humans stop early with small profit loss. LLMs stop at the wrong step in both directions (c02), so "search more" is not a fix.
- **Wage dispersion, marriage markets, descending price.** Economic equilibrium results (a09, a11) have no counterpart in a single agent.
- **Marginal value theorem.** No LLM tests; field fit is rough and animals overstay.
- **Reward-model stopping savings.** Measured on tasks with a checker or reward model. Not shown for open-ended work. Kalayci's rule needs a reward model.
- **Hidden-state probes and RL.** Need model internals or training; outside our scope (d05, d10).
- **Tree of Thoughts, 4% to 74%.** One task, many more calls, no per-call cost accounting (a22).
- **Operational Bayesian search stories.** Secondary summaries; no failure counts (K14).

## 10. Open questions

1. Does a Weitzman or Gittins style index on an agent's own tool calls beat fixed orders at equal tokens? The closest results are simulation-only or negative (d01, d02).
2. Does adaptive stopping hold with no reward model, on open-ended tasks?
3. Do Zhang and Zhao's stopping errors replicate on current frontier and reasoning models?
4. Is exploration failure fixed by reasoning models, or only by external summaries?
5. Which cheap, API-only signal gives per-prompt difficulty?
6. Does a marginal-value abandon rule beat fixed depth at equal tokens?
7. How much does the independence assumption cost on real LLM hypothesis sets?
8. Does cross-task memory of thresholds transfer to an LLM agent?
9. How do LLM-simulated subjects behave on Stigler or McCall search compared with the optimum?
10. Can the primary texts (Koopman, Weitzman, Schotter and Braunstein, Brown et al. 2011) be opened to confirm numbers now taken from Wikipedia or citing papers?

## 11. Sources

[V] opened (full text or page) this session or by earlier agents; [M] snippet or secondhand only. Several evidence lines duplicate others; papers are counted once.

- [V] Bernard Koopman (Wikipedia) https://en.wikipedia.org/wiki/Bernard_Koopman (a01). Koopman (1946) itself [M].
- [V] Bayesian search theory (Wikipedia) https://en.wikipedia.org/wiki/Bayesian_search_theory (a02-a04, b21)
- [V] Search theory (Wikipedia) https://en.wikipedia.org/wiki/Search_theory (a05, a07-a09, b20). Stigler 1961 and McCall 1965, 1970 originals [M].
- [V] Stigler (1962) Information in the labor market http://www.nber.org/chapters/c13574.pdf (a06, a24; OCR text)
- [V] Kleinberg, Waggoner, Weyl (2016) https://arxiv.org/abs/1603.07682 (a10, a11, a25, c22). Weitzman (1979) https://doi.org/10.2307/1910412 [M] (b25, c23).
- [V] Chawla et al. (2020) Pandora's Box with Correlations https://arxiv.org/abs/1911.01632 (a12, d12)
- [V] Gittins index (Wikipedia) https://en.wikipedia.org/wiki/Gittins_index (a13)
- [V] Secretary problem (Wikipedia) https://en.wikipedia.org/wiki/Secretary_problem (a14, a15). Seale and Rapoport; Bearden [M].
- [V] Optimal stopping (Wikipedia) https://en.wikipedia.org/wiki/Optimal_stopping (a16)
- [V] Marginal value theorem (Wikipedia) https://en.wikipedia.org/wiki/Marginal_value_theorem (a17)
- [V] Krishnamurthy et al. (2024) https://arxiv.org/abs/2403.15371 (a18, c09, c10)
- [V] Binz and Schulz (2023) https://arxiv.org/abs/2206.14576 (a19, c11, c12). Wilson et al. (2014) [M] (c24).
- [V] Li et al. (2024) ESC https://arxiv.org/abs/2401.10480 (a20, c07, c08). Wang et al. self-consistency https://arxiv.org/abs/2203.11171 [M] (c25).
- [V] Brown et al. (2024) Large Language Monkeys https://arxiv.org/abs/2407.21787 (a21)
- [V] Yao et al. (2023) Tree of Thoughts https://arxiv.org/abs/2305.10601 (a22)
- [V] Snell et al. (2024) https://arxiv.org/abs/2408.03314 (a23, d11)
- [V] Kittaka, Mikami, Shimada (2021) https://www.iser.osaka-u.ac.jp/library/dp/2021/DP1148.pdf (b01-b03)
- [V] Marcu and Noussair (2022) https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/micropaper22/micro1115.pdf (b04-b07, c21)
- [M] Brown, Flinn, Schotter (2011) https://www.aeaweb.org/articles?id=10.1257/aer.101.2.948 (b08); Schotter and Braunstein (1981) (b09); Cox and Oaxaca (1989) (b10); Rapoport and Tversky (1970) (b23); Kahan, Rapoport, Jones (1967) (b24). No URLs known for the last four.
- [V] Goldstein, McAfee, Suri, Wright (2020) https://www.mcafee.cc/Papers/PDF/SecretaryMS.pdf (b11, b12, c17, c18)
- [V] Spiliopoulos, Rapoport, Seale (2023) https://link.springer.com/content/pdf/10.1007/s11238-022-09881-0.pdf (b13, b14, c19, c20)
- [V] Zhang and Zhao (2024) https://zhaobn.github.io/assets/pdfs/Zhang24stopping.pdf (b15-b17, c01-c03). Not re-located in the last session; numbers unverified.
- [V] Kalayci, Raman, Dughmi (2025) https://arxiv.org/abs/2510.01394 (b18, c04-c06, d14)
- [V] Pilditch (2026) https://arxiv.org/abs/2608.14425 (b19, c15, c16)
- [V] Caplin and Dean (2010) https://www.columbia.edu/~md3405/Other_Paper_5.pdf (b22, methods draft)
- [V] Jain and Krishnamurthy (2025) https://arxiv.org/abs/2411.01271 (c13, c14)
- [M] Koopman (1956) and Stone (1975) as named in the subfield brief (c26)
- [V] Belloni, Chen, Wei (2026) https://arxiv.org/abs/2606.07392 (d01)
- [V] Cinquin, Pleiss, Kristiadi (2025) https://arxiv.org/abs/2510.20272 (d02)
- [V] Harris and Slivkins (2026) https://arxiv.org/abs/2502.00225 (d03)
- [V] Arumugam and Griffiths (2026) https://arxiv.org/abs/2504.20997 (d04)
- [V] Wang, Yan et al. (2026) https://arxiv.org/abs/2602.11748 (d05)
- [V] Fu et al. (2025) DeepConf https://arxiv.org/abs/2508.15260 (d06)
- [V] Taubenfeld et al. (2025) CISC https://arxiv.org/abs/2502.06233 (d07)
- [V] Aggarwal et al. (2023) Adaptive-Consistency https://arxiv.org/abs/2305.11860 (d08)
- [V] Yang et al. (2025) DEER https://arxiv.org/abs/2504.15895 (d09)
- [V] Damani et al. (2024) https://arxiv.org/abs/2410.04707 (d10)
- [V] Xie et al. Pandora's Box Gittins Index for Bayesian optimisation https://arxiv.org/abs/2406.20062 (d13, abstract only)
- [V] Horton (2023) https://arxiv.org/abs/2301.07543 (d15)
- [M] Nie et al. (2025) EVOLvE https://arxiv.org/abs/2410.06238 (d16, skimmed)
