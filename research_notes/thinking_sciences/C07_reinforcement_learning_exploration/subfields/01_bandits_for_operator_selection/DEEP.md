# Bandits and Thompson sampling for operator selection: deep document

*Subfield C07.01. Written 2026-10-26 from `evidence_a-d.jsonl` (a01-a31, b01-b27, c01-c28, d01-d19), `claims.jsonl` (K01-K29) and `critique.md` in this folder. Evidence ids in brackets. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested. Numbers marked "own simulation" are ours (d15-d18), synthetic, and set hypotheses, not facts.*

*Links to other subfields (not covered here): resource-rational strategy selection (when to spend on choosing), quality-diversity and novelty search (what to reward), anytime search and restarts (stall-triggered resets), Go-Explore and archives, library learning (which operators exist at all).*

---

## 1. What it is

A multi-armed bandit is a repeated choice among K options (arms). Each pull gives a noisy reward. The goal is to collect reward while still learning which arm is best. The cost of not knowing is called regret: reward lost against always pulling the best arm.

For us the arms are the operators O1-O8 of the schema (Specialise, Generalise, Decompose, Drop a constraint, Work backwards, Change representation, Map an analogue, Reframe the goal), plus maybe a "do nothing" arm. Other arm sets in the literature: prompt design strategies, candidate prompts, which LLM writes a mutation, which island to expand.

Three jobs get called "bandit" in the papers. They are different.

1. **Operator selection during search.** Pick which operator to apply next, learn from outcomes. Regret matters. (Evolutionary computation calls this adaptive operator selection, AOS.)
2. **Best-arm identification.** Spend a fixed budget on candidates, then name one winner. Regret during the spend does not matter. Only the final pick does. (TRIPLE, successive halving.)
3. **Model or prompt routing.** Pick which LLM or prompt to call per query. (ShinkaEvolve, PAK-UCB, Meta-Reasoner.)

AOS splits into two parts that people often blur: **credit assignment** (turn an outcome into a reward number) and **selection rule** (turn reward history into a choice). The evidence says credit assignment may matter as much as the rule [b10].

The central difficulty for us: nearly all theory and most simulations assume 10^4 to 10^7 pulls. Our agent has 20 to 60 pulls per problem, 8 arms, delayed feedback, and arms that are not independent (all outputs come from one model, G4). Almost nothing published tests that regime [critique, Weak spots].

---

## 2. History and theories in depth

**1933, Thompson.** Sample a belief about each arm from its posterior, play the arm whose sample is highest. Forgotten for decades.

**1985, Lai and Robbins.** Lower bound: any consistent policy must pull each worse arm about ln(n)/KL times, so regret grows at least like ln n [a01, b27; original not opened, only restated in Auer 2002 and Chapelle and Li]. Their index policies reach this but are hard to compute.

**2002, Auer, Cesa-Bianchi, Fischer.** UCB1: play the arm with highest mean + sqrt(2 ln n / n_i). First simple policy with log regret uniformly over time, rewards in [0,1], no prior [a02]. Theorem 1: regret <= 8 sum(ln n / Delta_i) + (1 + pi^2/3) sum(Delta_j). The constant 8 is loose. Same paper:
- UCB1-Tuned (variance-aware index) beat UCB1 in nearly all of 7 settings, no proof [a03].
- A tuned decaying epsilon-greedy "performs almost always best" but only after c was searched per setting; mistuned it degrades fast [a04].
- UCB1-Normal for Gaussian rewards has constants near 256 and rests on two conjectures checked numerically [a05].

**2002, Auer, Cesa-Bianchi, Freund, Schapire.** EXP3 for adversarial rewards. Regret <= about 2.63 sqrt(g K ln K); matching lower bound (1/20) min(sqrt(KT), T) [a18, a19]. With K=8 and T near 64 the bound is almost T. Nothing can be proven to learn at that scale. Any gain at our scale has to come from priors or structure.

**2008-2011, Garivier and Moulines.** For abrupt changes, discounted UCB and sliding-window UCB cost about sqrt(T log T); lower bound of order sqrt(T) per change [a16, a17, b01, b02]. Window tuned as 2B sqrt(T log T / Upsilon), which needs the number of breakpoints.

**2008, Da Costa, Fialho, Schoenauer, Sebag.** Dynamic MAB (D-MAB) for AOS: UCB1 plus restart of all counts when a Page-Hinkley test fires; reward scaling because UCB assumes rewards in [0,1] [a21-a25]. This is the classic non-LLM design.

**2009-2010, Fialho, Maturana and others.** Credit-assignment studies: extreme-value credit (max of last window) vs average [d04, d05, b24 not opened, c26 not opened]; rank-based credit [d06].

**2009, Whitacre, Pham, Sarker.** Credit by lineage survival over several generations beat immediate fitness gain [b10, b11].

**2011-2012, the Thompson revival.** Chapelle and Li: empirical case that TS is competitive or better than UCB, needs no tuning, tolerates delay [a09-a11, b06, b07]. Agrawal and Goyal: first log-regret bound for TS (gap dependence 1/Delta^3, weaker) [a06, b05]. Kaufmann, Korda, Munos: Beta(1,1) TS on Bernoulli is asymptotically optimal, matching Lai and Robbins [a07, a08, b03, b04]. Bubeck and Cesa-Bianchi 2012 is the standard survey [a20]. Russo et al. 2018 tutorial gives the "probability matching" view and the prior and non-stationary variants [a12-a15].

**2014, Kuleshov and Precup.** Large simulation: tuned epsilon-greedy and Boltzmann beat UCB1 and UCB1-Tuned at 1000 steps; Thompson not included [b08, b09].

**2020, Sun and Li.** Dynamic Thompson sampling (cap Beta counts at C=100) for MOEA/D operator selection [a26, a27, b12].

**2021, meta-Thompson and misspecified priors.** Kveton et al., Simchowitz et al., Hong et al.: learn the prior across tasks; bound the loss from a wrong prior [d02, d03, d19].

**2023-2026, bandits inside LLM systems.** ProTeGi (UCB and halving to pick prompts, 2023) [c06]; TRIPLE (best-arm identification for prompts, 2024) [a30, a31, b17, b18, c04, c05]; OPTS (Thompson over prompt strategies, 2025) [a28, a29, b14-b16, c01-c03]; AB-MCTS (Thompson go-wider vs go-deeper, 2025) [c07, c08]; ShinkaEvolve (UCB1 over LLMs) [b20, c09]; Meta-Reasoner (LinUCB over reasoning moves) [b21, c15]; AdaEvolve, TIDE, Deliberate Evolution, CoEvo-AHD, LLaMEA operator thesis [b22, c10-c14, d09, d10]. In parallel, studies of LLMs as bandit agents [c16-c21, c24].

**Competing views on the selection rule (unresolved).**
- Theory favours Thompson or KL-UCB (asymptotically optimal); tuned simple heuristics win on small simulations [b08]; best-arm rules win when the goal is a final pick [c04]. See section 5.
- Hyper-heuristic reviews give no agreed verdict between choice functions and bandits [b26, snippet only].

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Any consistent policy has at least log regret; UCB1 and TS reach that rate; guarantees are asymptotic | UCB1: 8 sum ln n/Delta_i + (1+pi^2/3) sum Delta_j. TS: (1+eps) sum Delta_a (ln T + ln ln T)/KL + C | Lai and Robbins via a01/b27; Auer 2002 [a02]; Kaufmann 2012 [a07] | [E] K01, K02 |
| Constant C hides short-horizon behaviour; adversarial lower bound is nearly T at K=8, T~64 | (1/20) min(sqrt(KT), T) | [a19, a07] | [E] |
| TS beats UCB and handles delay better | Delay table, T=10^6, 10 items, 100 reps: UCB regret 24,145 (delay 1) to 226,220 (delay 1000); TS 9,105 to 59,256; ratio 2.65 to 3.82 | Chapelle and Li [a10], re-checked | [E] K03 |
| All optimal policies beat UCB at small horizons; TS easiest to implement | 10-arm test, T=20,000, N=50,000; 2-arm T=10,000, N=20,000 | Kaufmann [a08, b04] | [E] |
| Narrower posterior (less exploration) can lower regret in short runs | Ad CTR regret %: TS alpha 0.25/0.5/1 = 4.45/3.72/3.81; LinUCB 4.99/4.22/4.14; eps-greedy 5.05/4.98/5.22; exploit-only 5.00; random 31.95 | [b07, a11, b06] | [S] (one setting; raised variance) |
| Tuned eps-greedy and Boltzmann beat UCB1 in 1000-step simulation | Boltzmann beat nearest rival by 10 to 100% total regret; tuned per setting; no TS | Kuleshov and Precup [b08] | [E] K04 (tuning is the hidden cost) |
| UCB1-Tuned beats UCB1; tuned eps-greedy often best | 7 settings, 100,000 plays, 100 runs | Auer [a03, a04] | [E] |
| Plain stationary bandits lag after the best arm changes; windows or restart recover | Window ~ sqrt(T ln T); window 0.2 of nominal explores too much; T=50,000, K=10, 50 runs | [a16, a17, b13, d11] | [E] K05 |
| Short AOS epochs: bandits beat PM and AP; change detector adds nothing at 50 pulls or Boolean rewards | T=200 uniform TCR (k): PM 7.36, AP 9.19, MAB-M 9.46, MAB-A 8.18, D-MAB-M 9.75, D-MAB-A 9.79 (max 10). T=50: 1.80/2.12/2.25/1.98/2.24/2.20 (max 2.5). Boolean T=200: 7.90/8.13/8.19/7.50/7.57/7.71. Outlier: p_best .21 to .29 (random .2) | Da Costa 2008 [a22-a25] | [S] K06 |
| PM/AP setup partly fails to replicate | Best p_min 0 to 0.01, not 0.1; PM = AP in Boolean and Outlier | [a25] | [S] K07 |
| Credit by lineage survival beats immediate gain | Credit effect +15.86 (t=7.28, p=3.2e-10); final +17.92 (p=8.4e-13); 10 functions, 10 runs, 8 designs | Whitacre [b10, b11] | [S] K08 |
| Extreme credit beats average in Fialho tests; makes bandits risk-seeking | Best combo beats uniform 22-0 on 22 SAT instances; f1000 false clauses 10.3 vs uniform 55.8; T=200 sliding MAB 8746 (extreme) vs 8522 (average); at T=50 best bandits close ~30 to 40% of gap to optimal | [d04, d05] | [S] K23 |
| Rank credit robust to reward scale | AUC-B, SR-B beaten only by highly tuned DMAB | [d06] | [S] |
| Dynamic TS reported better than FRRMAB | 16/19 IGD, 18/19 HV; UF8 text contradicts table | Sun and Li [a26, a27, b12] | [C] K09 |
| Strategy selection in prompt optimiser (DE optimiser, Llama-3-8B, 27 BBH, 3 seeds) | Manual 39.52; APET 20.73; EvoPrompt 48.43; OPTS(APET) 52.87; OPTS(US) 53.87; OPTS(TS) 55.67. TS - US = +1.80; US - EvoPrompt = +5.44 | OPTS [b14] (corrected: table, not text "1.7%") | [S] K10 |
| Same, GA optimiser | Plain 48.40; APET 51.34; uniform 52.89; TS 53.48 (TS - US = +0.59) | OPTS Table 10 [critique, d08] | [S] |
| Paired tests over 27 tasks | DE: +1.79, SD diff 3.57, t=2.61, TS wins 18, loses 7, ties 2, sign p=0.043, Wilcoxon p=0.008. GA: +0.60, t=0.96, 12 wins 14 losses, sign p=0.85 | own analysis [d07, d08] | [S] K22 |
| Headline "50%" gain is one task from a near-zero baseline | GPT-4o mini, task 8: 2.67 (SD 1.43) to 52.33 (SD 11.45); task 19: 79.17 to 79.43; task 23: 80.67 to 81.83. Ruin names 27.17 to 67.67; some tasks lose (colored objects 53.00 to 49.50) | [c02, b15] | [E] K21 |
| LLM choosing its own strategy is worse | OPTS(APET) 52.87 vs US 53.87 vs TS 55.67. Meta-Reasoner: direct LLM choice 82 vs 89 (Game of 24), 80.74 vs 84.13 (TheoremQA) | [b15, b21, c15] | [C] K11 |
| Best-arm rules beat uniform and UCB at ~5 evals per prompt | Pool 30, budget 150, 20 runs: SH +15 / CR +12 (GPT-3.5), +15 / +16 (Llama2) over Uniform; +5 / +3 and +6 / +7 over UCB. 10 evals per prompt: CR +9.7, CLST +13.5, GSE +17.4%. 30 evals: all equal | TRIPLE [a30, a31, b17, c04, c05] | [S] K12 |
| Embedding sharing wins when candidates outnumber budget | 150 prompts, budget 100: CLST/GSE beat BO-EI by 21/28% (GPT-3.5), 31/42% (Llama2); beat NeuralUCB by 38/45% (GPT-3.5), 26/16% (Llama2). Ranks: Uniform 4.00, CR 2.92, CLST 1.58, GSE 1.50 | [b18, a15] | [E] K14 |
| UCB vs halving for prompt selection | Uniform 0.77/0.59/0.77/0.61; UCB 0.83/0.66/0.85/0.66; SR 0.81/0.62/0.82/0.66; SH 0.82/0.64/0.80/0.62 (differences 0.01 to 0.04) | ProTeGi [c06] | [C] K13 |
| Bandit gain over uniform in LLM evolutionary search is small | LLaMEA (N=6): Random 0.8304 (SD 0.0148), UCB 0.8453 (0.0296), SW-UCB-S 0.8417, SW-UCB-M 0.8401, SW-UCB-L 0.8235, Top3 0.8350, Geometric-S 0.8470. TIDE ablation "w/o UCB" gap %: 5.87/8.91/12.64 at sizes 50/100/200 | [c10, c12, b20, c09] | [E] K16 |
| Stall-triggered meta-guidance matters more than bandit in AdaEvolve | Circle packing: full 2.6294; no meta-guidance 2.5213; no bandit island selection 2.6180. Signal processing: full 0.7178; no meta 0.5476; no bandit 0.619. 3 runs | [b22, d09] | [C] K17 |
| State-keyed hand policy beats uniform | NMSE: full 4.37e-4; uniform 1.02e-2 (23x); fixed refine 8.69e-3; no stagnation monitor 7.69e-4 (1.8x); no memory 1.34e-3; no tool 2.52e-2. Acc0.01: 15.91 / 6.82 / 9.52 / 13.64 / 9.52 / 4.55%. Run count not stated | Deliberate Evolution [c13, d10] | [S] K15, K29 |
| Wider-or-deeper TS vs repeated sampling | At 128 generations: ARC-AGI Pass@2 repeated 15.0 / 18.6 (GPT-4o / DeepSeek-V3) vs AB-MCTS-M 12.3 / 16.0, AB-MCTS-A 14.0 / 16.6; CodeContest GPT-4o 40.6 (M) vs 37.9; LiveCodeBench 38.9 vs 37.8; mean rank 3.5 / 2.3 / 2.7. Repeated sampling plateaus at 200 to 500 generations | AB-MCTS [c07, c08] | [S] K19 |
| LLMs as bandit agents fail to explore | GPT-4 basic prompt: suffix failure >60% (T=500, K=5 gap 0.2); all but five configs >=15% suffix failure at T/2 | Krishnamurthy [c16] | [E] K20 |
| Own simulation, 8 operators, 20-60 pulls | Hard, T=60 regret: uniform 7.90, UCB1 7.34, TS flat 6.88, UCB c=0.5 6.52, eps0.1 6.04, fixed guess right 30%: 5.73, right 50%: 4.11. Typical, T=60: uniform 15.25, UCB1 12.51, TS 10.21, eps0.1 7.94 | [d15] | [S] K24 (synthetic) |
| Wrong prior cheap at 30 pulls, right prior pays | Hard: flat TS 3.65, uniform 3.92; strength 8 right 2.71 / wrong 3.81; strength 16 right 1.95 / wrong 3.98. Typical: flat 6.00, uniform 7.47; strength 8 right 3.60 / wrong 6.50; strength 16 2.24 / 7.11. 50/50 mix at 16: 2.97 and 4.67 | [d16] | [S] K25 (synthetic) |
| Plain TS needs no cap at 30-60 pulls | Regret T=30, stationary/switch: none 6.92/7.37; C=5 6.92/7.38; C=20 6.96/7.35; C=50 6.94/7.38; uniform (switch) 7.88. T=60: none 12.54/14.05; C=10 12.55/14.01 | [d17] | [S] K26 (synthetic) |
| For final pick at ~5 evals, halving ~ tuned UCB ~ TS | K=10, budget 50, gap 0.15: uniform 0.38, halving 0.47, UCB1 0.48, UCB c.5 0.54, TS 0.50. K=30, budget 150, gap 0.20: uniform 0.26, halving 0.51, UCB1 0.41, UCB c.5 0.54, TS 0.52 | [d18] | [S] K27 (synthetic) |
| LLM-made prior cuts early regret | 14 to 17% (LLM oracle), 19 to 20% (real conjoint) at T=1000; GPT-3.5 13.79 to 19.65%; Claude-3 Haiku 14.51 to 20.39% | Alamdari [d01] | [S] K28 |
| Theory: wrong prior loss | |R(true) - R(wrong)| <= 2 H^2 TV B | Simchowitz [d03] | [S] |
| Contextual TS guarantee vacuous at small T | O~(d^1.5 sqrt(T)) exceeds T when T < d^3 (our arithmetic) | Agrawal and Goyal 2013 [d13] | [S] |

---

## 4. Mechanisms and models

This section is written so an engineer can code it. Reward is always computed by code from a check, never by the model's opinion (G2, G5, G10).

### 4.1 Beta-Bernoulli Thompson sampling over operators

State per arm i: alpha_i, beta_i. Start (1,1) or an informative prior (4.5).
```
choose():   for each allowed arm i: theta_i ~ Beta(alpha_i, beta_i)
            return argmax theta_i          # ties: random
update(i, r in {0,1}): alpha_i += r ; beta_i += 1 - r
```
- Binary reward: 1 if the child subgoal passed the code check or improved the best-so-far; 0 otherwise. OPTS uses exactly this (1 if the new prompt's dev score beats the incumbents) [a28].
- No exploration constant. The only knobs are the prior and the reward definition [a09].
- Delayed feedback: choose all pending operators from the same posterior before seeing results. TS randomises, so batch picks differ; UCB would pick the same arm repeatedly [a10].
- Add an "inaction" arm (apply no operator). OPTS did; it limits loss on tasks where strategies hurt [c01]. Fits G1.

### 4.2 UCB variants (fallback)

UCB1: pick argmax mean_i + sqrt(2 ln n / n_i); rewards must be in [0,1]; pull each arm once first [a02]. With 8 arms and 30 pulls, the initial sweep takes 27% of the budget. UCB1-Tuned replaces the bonus with sqrt(ln n / n_i * min(1/4, V_i)), where V_i = sample variance + sqrt(2 ln n / n_i) [a03]. In our simulation a smaller constant (c=0.5) beat both UCB1 and flat TS at 20-60 pulls [d15].

### 4.3 Non-stationary variants

- **Sliding window**: use only the last tau pulls per arm; tau about sqrt(T ln T) [a16, d11]. At T=30 that is about 10, a third of the run, so it is almost the same as nothing.
- **Discounting**: multiply old counts by gamma < 1 each step [a16, d12].
- **Capped counts (dynamic TS)**: if alpha+beta >= C, rescale so alpha+beta = C [a26]. One line. C=100 was used at thousands of evaluations.
- **Restart on change (D-MAB)**: run a Page-Hinkley test on the reward stream (tolerance delta=0.15, threshold gamma 0.5 to 20 depending on scenario); when it fires, zero all counts [a21].
- **Stall reset**: our version: when the impasse detector (S6) fires, reset the posterior toward the prior. Untested.
- Our simulation: at T=30-60, caps of 5 to 50 change regret by under 0.15 [d17]. Use plain TS unless runs are long.

### 4.4 Credit assignment options

| Credit | Definition | Evidence |
|---|---|---|
| Binary improvement | 1 if child beats incumbent | OPTS [a28]; DYTS [a26] |
| Relative gain | exp(max(r - r_base, 0)) - 1, normalised (ShinkaEvolve); relative offspring-over-parent improvement (Deliberate Evolution, TIDE) | [c09, d10, c12] |
| Extreme value | max of last 10 gains | wins in Fialho tests; risk-seeking; helps at long epochs [d04, d05] |
| Rank / AUC | rank of the operator's reward among recent rewards | scale-free; robust [d06] |
| Lineage | credit for the 2 to 3 step descendants of the output | [b10, b11]; decays after a few steps |

For Beta-Bernoulli TS you need a binary reward. Real-valued gains need Gaussian TS or a threshold (success = gain above median of recent gains).

### 4.5 Priors

- Informative prior: set (alpha_i, beta_i) = (1 + s*p_i, 1 + s*(1-p_i)) with p_i an expected pass rate and s pseudo-counts. Cap s at 4 to 8 [d16].
- Source of p_i: (a) hand design; (b) hierarchical pooling across past tasks: shrink operator means toward the cross-task mean [d02, d19]; (c) an LLM's stated preference as pseudo-counts, outcomes override [d01]. Only (a) and (b) have theory; (c) has one contextual-bandit study at T=1000.
- Wrong-prior cost is bounded by 2 H^2 TV B [d03], which grows with H squared. Short runs are the safe place for a modest prior.

### 4.6 State-keyed (contextual) operator choice

Keep one posterior per (state, operator), with partial pooling: posterior for (s, i) starts from the global posterior for i scaled to s0 pseudo-counts. State key candidates: schema state (S3 vs S5 vs S6), parent quality bucket (LLaMEA: operator value falls as parent fitness rises [c10]), region visited often or not (Deliberate Evolution [c13]). Rich contextual TS has vacuous guarantees below T = d^3 [d13]. With 30 pulls over 4 states and 8 operators there are 3 to 10 pulls per state. Pooling or a hand-set table is needed.

### 4.7 Best-arm identification for the final choice

Sequential halving: split budget B over ceil(log2 K) rounds. Each round give every surviving candidate B/(rounds * survivors) evaluations, keep the top half by mean [c04]. Tuning-free. In our simulation it ties tuned UCB and TS at about 5 evaluations each, and beats plain UCB1 only when candidates are many [d18]. Original halving gains assume converging training curves, not i.i.d. judgments [d14].

### 4.8 Wider-or-deeper (AB-MCTS)

At each node, Thompson sampling decides between "generate a new child" (a node with a probability model for an unseen child) and "refine an existing child". UCT cannot be used because arms are created on the fly [c07]. Relevant to S3 vs S5 choice, but the gain over repeated sampling appears only above ~200 generations on ARC-AGI [c07, c08].

### 4.9 Pairwise bandits for label-free selection

Double Thompson sampling over duels judged by an LLM: best on 13 of 16 BBH tasks, depends on a noisy judge (judge accuracy where answers differ 0.59 to 0.99 by model) [b19]. Conflicts with G5/G8 unless the judge is blind and length-normalised.

---

## 5. What holds up

### 5.1 Solid

- Log regret is the best possible; TS and UCB1 reach it; TS is asymptotically optimal on Bernoulli [a01, a02, a07, b03]. [E]
- TS needs no tuning and tolerates delay better than UCB (ratios 2.65 to 3.82) [a10, b06]. [E]
- Plain greedy locks in on a poor arm [a12]. So never just reuse the first operator that worked. [E]
- Non-stationarity has a built-in cost of order sqrt(T) per change; forgetting is needed once the world changes at unknown times [a16, b02, b13]. [E] But short horizons do not use it (d11, d12, d17).
- Embedding or feature sharing beats independent arms when arms outnumber budget [b18, a15]. [E]
- Reported LLM-bandit gains rest on 3 to 6 seeds, no significance tests, author-tuned baselines [critique; c02, b22, c10]. [E]
- LLM-in-context bandits mostly fail to explore (5 sources) [c16, c17, c19, c20, c24]. [E]

### 5.2 Failures, contradictions, boundary conditions

- **Tuned simple rules beat UCB** [a04, b08]. The result is about tuning, not about eps-greedy being better. TS was not in Kuleshov's study. Untuned defaults are the fair test.
- **UCB vs best-arm rules**: ProTeGi finds UCB >= halving (differences 0.01 to 0.04) [c06]; TRIPLE finds halving and continuous rejection above UCB (+3 to +7%) [c04]. Theory favours best-arm rules for a fixed budget. Our simulation: tie [d18]. [C]
- **OPTS gap depends on optimiser**: DE +1.79 (significant across tasks), GA +0.60 (not) [d07, d08]. Thompson over uniform is small. The big part (+5.4 points) comes from having the strategies and letting code choose among them [b14]. [S]
- **The "up to 50%" headline is one task from a near-zero baseline** [c02].
- **DYTS table vs text**: text says best on UF8; IGD table marks GRA and IRA better on UF8 (and UF9). 16/19 does not match the table [critique]. [C]
- **ShinkaEvolve**: caption "slightly improves", takeaway "significantly outperforms"; no numbers [b20, c09].
- **TIDE**: removing UCB is the best ablation at size 50 and worst at size 200 [c12]. The bandit's value depends on problem size.
- **Small windows hurt**: SW-UCB-L (0.8235) is below random (0.8304) in LLaMEA; small windows drift to uniform [c10, c11]. Theory: window near sqrt(T ln T) [d11].
- **Outlier / rare big reward**: every selector near random (p_best .21 to .29 vs .2) [a24]. A mean-based bandit cannot find a rare-insight operator.
- **Change detector adds nothing at 50-pull epochs or Boolean rewards** [a23, a24].
- **Thierens PM/AP defaults** did not replicate (p_min 0 to 0.01 vs 0.1) [a25].
- **Meta-Reasoner**: text and table disagree on ToT (45% to 74% vs 32% to 65%); the 89 vs 4 contrast is against plain CoT, not a fair control; fair control (LLM picks) costs only 7 and 3.4 points [b21, c15].
- **PAK-UCB**: the Sudoku (70.82 vs 50.42; 86.85 vs 93.6) and HumanEval (92.3 vs 86.5; 48.8 vs 82.3) figures are success rates of two base models. They show the models are complementary, not the router's gain [critique].
- **TRIPLE pool-10 line** (a30: "pool 10, budget 50, avg +35% over uniform") could not be found in the paper text; the checked setup is pool 30, budget 150, and pool 150, budget 100. Treat the +35% as unconfirmed [critique].
- **AdaEvolve vs Deliberate Evolution**: one says stall-triggered guidance outweighs the bandit; the other says the state-keyed policy (23x) outweighs the stagnation monitor (1.8x). Neither isolates a plain forced switch [d09, d10]. [C]

### 5.3 What worked and what did not (interventions)

| Intervention | Worked? | Where |
|---|---|---|
| Code picks the strategy (uniform or TS) instead of the LLM | Yes, +1 to +3 points | OPTS [b15]; Meta-Reasoner [c15] |
| Bandit instead of uniform | Small: +1.8 (DE), +0.6 (GA), +0.015 fitness (LLaMEA, N=6) | [b14, d08, c10] |
| Inaction arm | Limits losses | OPTS [c01] |
| Smart allocation at ~5 evals per candidate | Yes, +12 to +16% over uniform | TRIPLE [c04] |
| Smart allocation at 30 evals per candidate | No | [c05] |
| Change detector at 50-pull epochs | No | [a23] |
| Small sliding window | No, hurts | [c10, c11] |
| Extreme credit | Yes at long epochs; risk-seeking | [d04, d05] |
| Lineage credit | Yes, decays after a few steps | [b10, b11] |
| Giving the LLM UCB values in its prompt | Helps most (Gemini Flash MAB win-rate 27.5 raw history to 50.2 guided) | EVOLvE [c17] |
| Warning plus "explore" instruction on LLM bandits | Raises exploration; a warning alone barely; helped labels raised regret | [c20] |

---

## 6. Language models

### 6.1 LLM as the bandit agent (in-context)

- Of all prompt and model setups tried (GPT-3.5, GPT-4, Llama2; Bernoulli K=5 gap 0.2 and K=4 gap 0.5; T=500), one worked: GPT-4 with chain of thought and counts-and-means supplied. Basic GPT-4 prompt: suffix failure in more than 60% of replicates; all but five configs had at least 15% suffix failure at T/2 [c16].
- GPT-3 (2022) beat humans on regret in a two-armed bandit (mean regret 2.72 vs 3.24) but showed no directed exploration [c18].
- Reasoning (chain of thought, o3-mini, DeepSeek-R1) raised directed exploration and cut regret to human level on a 2-armed task; on a 4-armed non-stationary task directed exploration stayed absent (uncertainty-bonus parameter negative for all LLMs) [c19].
- Arm labels bias choice: positive-sounding labels get exploited even if worse; negative reward values cause far more exploration than positive ones; alphanumeric labels act close to UCB [c20]. Our operator names (Specialise, Generalise) are semantic labels, so an in-context chooser would be biased.
- TextBandit (25 rounds, 500 runs, best arm 65%): best-arm rate Qwen3-4B 89.2%, Qwen3-8B 37.5%, Llama-3.1-8B 31.6%, Phi-2 25.4% vs Thompson 51.1%, UCB 47.6%, eps-greedy 38.1%, random 31.8%. More arms hurt (Llama 31.56% at 2 arms to 7.37% at 5). The Qwen3-4B outlier is unexplained and unreplicated [c24].
- Numeric bandits on text embeddings often match or beat LLM bandits; LLMs win only for complex non-linear rewards [c21].
- BanditBench (EVOLvE): giving UCB-computed values in the prompt helps most; fine-tuning on UCB trajectories lets a small model beat a larger one. Raw history is weakest. Contextual bandit Flash: 3.6 vs 60.7 win-rate (raw vs guided). UCB itself 90.6 / 96.4 [c17]. Table pairing uncertain.

What changed LLM behaviour, and by how much: chain of thought plus summary statistics (from fail to success, GPT-4 only) [c16]; algorithm-guided values (27.5 to 50.2 win-rate) [c17]; reasoning models (human level on 2 arms) [c19]; a warning plus explore instruction [c20]. All point the same way: the model reads statistics well and does not compute them. Keep the bandit in code (G5).

### 6.2 LLM-chosen vs code-chosen operator

OPTS: LLM chooses 52.87, uniform code 53.87, TS 55.67 [b15]. Meta-Reasoner: LLM direct 82 vs bandit 89 (Game of 24); 80.74 vs 84.13 (TheoremQA); also with 87 vs 94 on Gemini-exp-1206 [b21, c15]. Both are authors' own ablations. [C] K11, but consistent with G5.

### 6.3 Bandits inside LLM systems (what the gains look like)

- Prompt strategy selection: +5.4 (uniform) and +7.2 (TS) over EvoPrompt (DE) [b14].
- Model selection (ShinkaEvolve): ordering single < uniform ensemble < bandit ensemble; no numbers [b20].
- Island selection (AdaEvolve): -0.011 (circle) when removed [d09].
- Operator selection (LLaMEA): +0.015 over random, N=6, about one SD [c10].
- Repeated sampling vs adaptive branching on ARC-AGI: repeated sampling better at 128 (15.0 vs 12.3) [c07].

### 6.4 What is not known for current frontier models

All LLM-as-agent studies use 2022-2025 models and horizons of 25 to 500. The OPTS task LLM is Llama-3-8B. No study of Thompson sampling over reasoning operators with a current model at a few dozen pulls exists.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Operator and strategy selection is done by code from counts, never by the model's free-text judgment; the model may receive computed statistics but does not pick. | G5 (already) / S6 | [E] | K20: c16, c17, c19, c20, c21, c24 |
| A2 | Never use pure greedy reuse of the last operator that worked; some randomisation or posterior sampling is needed. | S6 operator pick | [E] | K01/K02: a12; Lai and Robbins a01 |
| A3 | Always compare a bandit with a uniform-random control (and a fixed-order control) before keeping it; expect a gain of 0 to 2 points. Needs at least 10 seeds or 10 paired items and a stated minimum effect. | G7 | [E] | K16, K21: b14, d08, c10, c02 |
| A4 | If outcomes of operators arrive in a batch or after a delay, use randomised selection (TS) not deterministic UCB. | S6 | [E] | K03: a10, b06 |
| A5 | Treat operators as correlated arms: log features (problem class, state, parent quality) so evidence is shared rather than counting each operator independently. | memory | [E] | K14: b18, a15 (design only; see Test first for the state-keyed bandit itself) |
| A6 | Log per operator: state, parent quality, outcome, tokens. Needed to run every test in section 8. | section 6 logging | [E] by design (G7 and section 6 of SCHEMA) | K15 |
| A7 | Do not rely on tuned parameters from the literature (window, p_min, C); use untuned defaults and report sensitivity to one constant. | G7 | [E] | K04, K07: a04, b08, a25 |

Note: A1 to A7 add nothing new to the operator list. They fix how the S6 operator pick is built and measured. No claim here supports a learned selector beating uniform; that is in Test first.

### Test first (single-source, contested, or synthetic)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Beta-Bernoulli Thompson selector over O1-O8 plus an inaction arm, reward 1 if the child improved the best check. | S6 / O1-O8 | [S] | K02, K10, K22: a28, b14, d07, d08 |
| T2 | Informative prior of 2 to 8 pseudo-counts per operator from past tasks (hierarchical pooling), capped. | memory / S0 | [S] | K25: d02, d03, d16, d19 |
| T3 | LLM-stated operator preference as the prior, not the chooser. | memory / S6 | [S] | K28: d01 |
| T4 | A fixed best-guess operator order (by class) as a baseline that may beat all flat-prior learners at 8 arms and under 60 pulls. | S6 | [S] (synthetic) | K24: d15 |
| T5 | State-keyed posterior, pooled toward a global one, vs a global bandit. | S0-S9 / O | [S] | K15, K29: c10, c13, d10, d13 |
| T6 | Stall-triggered forced switch (the existing S6 trigger) vs bandit only, at equal tokens. | G1 / S6 | [C] | K17: b22, c13, d09, d10 |
| T7 | Credit rule head to head under the same Thompson rule: binary, relative gain, max of last 5, rank. | memory | [S] | K23: d04, d05, d06 |
| T8 | Lineage credit (2 to 3 step descendants). | memory | [S] | K08: b10, b11 |
| T9 | Successive halving to pick the final answer among candidates at about 5 checks each (S7/S8). | S7 | [S] | K12, K27: c04, d18 |
| T10 | Plain TS, no window; add a stall reset only if the stall rule exists. | S6 | [S] | K26: d11, d12, d17 |
| T11 | Thompson go-wider vs go-deeper (AB-MCTS) on ARC items at budgets under 128. | S3/S5 | [S] | K19: c07, c08 |
| T12 | Rank-based credit when reward scales differ across tasks. | memory | [S] | d06 |

---

## 8. Concrete tests on our bench

Every test: both arms at equal tokens, same items, at least 10 seeds (or 10 paired items), a pre-registered minimum effect. Replay first (free): re-run selectors on logged operator outcomes, then run live only for tests that pass the replay. Item types: ARC items (with a check on held-out examples) and BRAINTEASER items.

| ID | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | Does any learner beat uniform? | ARC and BRAINTEASER items that reach S6 | uniform random operator; fixed best-guess order; flat TS; TS with prior | pass rate at equal tokens; regret on replayed logs at 20, 40, 60 pulls | TS - uniform of 0 to 2 points; may be 0 [b14, d08] |
| B2 | Prior strength | same | flat Beta(1,1); right prior s=4 and s=8; deliberately wrong prior s=8 | pass rate; regret at T=30 | right prior: gain; wrong prior at s=8 costs 0.2 to 0.5 successes [d16] |
| B3 | Stall switch vs bandit | items that hit an impasse | bandit only; forced switch on stall only; both | pass rate; tokens to first pass | unknown; AdaEvolve hints stall rule larger [d09] |
| B4 | State-keyed vs global | same | global TS; 3-state key (early, mid, late parent quality) pooled to global | pass rate; regret | small gain at best; per-state samples 3 to 10 [d13] |
| B5 | Credit rule | replay logs | binary; relative gain; max of last 5; rank; lineage 2-step | cumulative reward under the same TS | extreme: helps only at long runs [d05]; lineage: gain decays [b11] |
| B6 | LLM-as-prior vs LLM-as-chooser | same | flat TS; LLM chooses; LLM prior s=4 capped | pass rate | prior >= flat; chooser <= uniform [b15, d01] |
| B7 | Final pick | candidate sets with ~5 checks each | uniform; successive halving; TS; UCB c=0.5 | P(pick correct answer) | halving ties TS within 0.04 [d18] |
| B8 | Window | runs with 40+ pulls | plain TS; cap 20; stall reset | regret | no difference [d17] |
| B9 | Wider vs deeper | ARC items, budgets 16 to 128 generations | repeated sampling; TS wide/deep | Pass@2 | repeated sampling ahead below 128 [c07] |
| B10 | Seed noise floor | any | same arm run 10 times | SD of pass rate | sets the minimum detectable effect |

Replay design: log (item, state, operator, outcome, tokens). Simulated bandit is run on the outcomes of operators that were actually executed. For counterfactual operators you need either a full-factorial log (run all 8 operators on every item once; cost 8x) or an offline estimator. Gap: full-factorial logs are the cheapest honest source of real operator reward tables, and they unlock B1, B2, B4, B5, B8 at no more live cost.

---

## 9. What does not transfer, and why

- **Asymptotic regret theory.** Bounds are for T near 10^4 to 10^7; the constants are silent at 30 pulls [a07, a19, b03]. Our horizon is two to three orders smaller.
- **Window and discount results.** Every opened study starts at 200 pulls [d11, d12]. Our simulation says caps are inert at 30 to 60 [d17].
- **Change detection (Page-Hinkley).** No gain at 50-pull epochs [a23].
- **Contextual TS and LinUCB guarantees.** Vacuous below T = d^3 [d13].
- **Meta-Reasoner / LinUCB trained on 30 to 50 queries.** Training query counts are far above what we have per class; reward is an LLM judge [c15].
- **Adversarial (EXP3) bounds.** Too conservative; sqrt(KT) is almost T [a19].
- **Selection among LLMs or islands.** AdaEvolve, ShinkaEvolve, TIDE run hundreds of generations over populations [b22, b20, c12]. We have one problem and few dozen operator calls.
- **Prompt-optimiser gains (OPTS).** 50 iterations x population 10 = up to 500 evaluations, and reward is a dev-set score. Our reward is a single problem's check. The TS-over-uniform gap was measured only with 3 seeds averaged.
- **Rare-big-win operators.** Mean-based bandits fail with outlier rewards [a24]. If the value of O7 or O8 is occasional breakthroughs, a pass-rate bandit will under-use them.
- **Arms that improve with use (TI-UCB).** Needs thousands of pulls; our operators do not train [c23].
- **Label-free duels (Prompt Duel).** Depends on an LLM judge; conflicts with G5 and G8 unless judged by code [b19].
- **Human bandit behaviour as a model.** Humans and LLMs differ; no human-data finding here applies directly [c18, c19].
- **Simulations d15 to d18.** Our own, Bernoulli, assumed arm distributions, no standard errors. They show what is plausible, not what our logs will show.

---

## 10. Open questions

1. At 20 to 60 pulls and 6 to 10 arms with real operator logs, how does TS with a weak prior compare with UCB1, uniform and a fixed best-guess operator? (Only synthetic evidence [d15].)
2. Which credit rule works with Thompson sampling: binary, relative gain, extreme, rank, lineage? No head-to-head exists.
3. Does a stall-triggered forced switch beat or add to a bandit at equal tokens? (Contested.)
4. Does state-keying beat a global bandit at small budgets? How should pooling work?
5. How much prior information helps, and what happens when the prior points at the wrong operator? (Simulated at 30 pulls only.)
6. Does the OPTS TS-over-uniform gap survive 10+ seeds, equal API calls and other optimisers? (DE yes across tasks, GA no.)
7. For choosing among final candidates at about 5 checks each on ARC and BRAINTEASER, is halving better than TS or UCB c=0.5?
8. Is the LLM's stated preference a good prior, and better than the LLM choosing?
9. Do operators interact (applying O3 after O6)? All bandits here treat arms as independent single pulls. Sequences of operators (tree depth 2) are unmodelled.
10. How do heavy-tailed operator gains (rare breakthroughs) get credited without a mean-based bandit missing them?
11. Is the 4B-over-8B pattern in TextBandit real? (Unreplicated.)
12. Do current reasoning models, given counts and means, explore well enough to act as a bandit with no code? (All evidence is on older models.)

---

## 11. Sources

[V] = opened and read as full text (PDF or HTML) this series. [V*] = read through a fetch summary, numbers not re-checked. [M] = snippet or bibliographic record only.

**Theory and classic bandits**
- [M] Lai and Robbins (1985) Asymptotically efficient adaptive allocation rules. Restated in Auer 2002 and Chapelle and Li. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf (a01, b27)
- [V] Auer, Cesa-Bianchi, Fischer (2002) Finite-time analysis of the multiarmed bandit problem. https://homes.di.unimi.it/cesa-bianchi/Pubblicazioni/ml-02.pdf (a02-a05)
- [V] Auer, Cesa-Bianchi, Freund, Schapire (2002) The nonstochastic multiarmed bandit problem. https://homepages.math.uic.edu/~lreyzin/papers/auer02.pdf (a18, a19)
- [V] Agrawal and Goyal (2012) Analysis of Thompson Sampling for the multi-armed bandit problem. https://arxiv.org/abs/1111.1797 (a06, b05)
- [V] Kaufmann, Korda, Munos (2012) Thompson Sampling: an asymptotically optimal finite time analysis. https://arxiv.org/abs/1205.4217 (a07, a08, b03, b04)
- [V] Chapelle and Li (2011) An empirical evaluation of Thompson sampling. https://papers.nips.cc/paper_files/paper/2011/file/e53a0a2978c28872a4505bdb51db06dc-Paper.pdf (a09-a11, b06, b07)
- [V] Russo, Van Roy, Kazerouni, Osband, Wen (2018) A tutorial on Thompson sampling. https://arxiv.org/abs/1707.02038 (a12-a15)
- [V] Bubeck and Cesa-Bianchi (2012) Regret analysis of stochastic and nonstochastic multi-armed bandit problems. https://arxiv.org/abs/1204.5721 (a20)
- [V] Kuleshov and Precup (2014) Algorithms for the multi-armed bandit problem. https://arxiv.org/abs/1402.6028 (b08, b09)
- [V] Agrawal and Goyal (2013) Thompson Sampling for Contextual Bandits with Linear Payoffs. https://arxiv.org/abs/1209.3352 (d13)

**Non-stationary, priors, hierarchies**
- [V] Garivier and Moulines (2011) On upper-confidence bound policies for non-stationary bandit problems. https://arxiv.org/abs/0805.3415 (a16, a17, b01, b02)
- [V] Fiandri, Metelli, Trovo (2025) Sliding-Window Thompson Sampling for Non-Stationary Settings. https://arxiv.org/abs/2409.05181 (b13, d11)
- [V] Raj and Kalyani (2017) Taming Non-stationary Bandits: A Bayesian Approach. https://arxiv.org/abs/1707.09727 (d12)
- [V] Kveton et al. (2021) Meta-Thompson Sampling. https://arxiv.org/abs/2102.06129 (d02)
- [V] Simchowitz et al. (2021) Bayesian decision-making under misspecified priors. https://arxiv.org/abs/2107.01509 (d03)
- [V, abstract and setting only] Hong et al. (2022) Hierarchical Bayesian Bandits. https://arxiv.org/abs/2111.06929 (d19)
- [V] Jamieson and Talwalkar (2016) Non-stochastic Best Arm Identification and Hyperparameter Optimization. https://arxiv.org/abs/1502.07943 (d14)
- [V] TI-UCB authors (2024) Which LLM to Play? Time-Increasing Bandits. https://arxiv.org/abs/2403.07213 (c23)

**Adaptive operator selection and hyper-heuristics**
- [V] Da Costa, Fialho, Schoenauer, Sebag (2008) Adaptive operator selection with dynamic multi-armed bandits. https://www.cs.ubc.ca/~hutter/EARG.shtml/earg/papers08/pap333s1-dacosta.pdf (a21-a25, c25)
- [V] Maturana, Fialho, Saubion, Schoenauer, Sebag (2009) Extreme Compass and Dynamic MAB. https://inria.hal.science/inria-00377450 (d04)
- [V] Fialho, Da Costa, Schoenauer, Sebag (2010) Analyzing bandit-based adaptive operator selection mechanisms. https://inria.hal.science/inria-00519579 (d05)
- [V] Fialho, Schoenauer, Sebag (2010) Toward Comparison-based Adaptive Operator Selection. https://inria.hal.science/inria-00471264 (d06)
- [V] Whitacre, Pham, Sarker (2009) Credit assignment in adaptive evolutionary algorithms. https://arxiv.org/abs/0907.0592 (b10, b11)
- [V] Sun and Li (2020) Adaptive operator selection based on dynamic Thompson sampling for MOEA/D. https://arxiv.org/abs/2004.10874 (a26, a27, b12)
- [M] Fialho et al. (2008-2010) extreme value AOS bibliography. https://www.lri.fr/~marc/selectedBib.html (b24); https://hal-univ-tlse3.archives-ouvertes.fr/INRIA/inria-00377450 (c26)
- [M] Li, Fialho, Kwong, Zhang (2014) FRRMAB. https://scholars.cityu.edu.hk/en/publications/adaptive-operator-selection-with-bandits-for-a-multiobjective-evo/ (b25)
- [M] Hyper-heuristic choice function vs MAB (search summary). https://link.springer.com/10.1007/s10732-018-9369-x (b26)
- [M] BRACIS 2021 DQN selector for HyFlex. https://sol.sbc.org.br/index.php/bracis/article/view/19037 (c28)
- [M] RIDER, windowed TS over nine prompt operators (PDF damaged). https://www.fruct.org/files/publications/volume-39/fruct39/Dra.pdf (c27)

**LLM systems using bandits**
- [V] Ashizawa et al. (2025) OPTS. https://arxiv.org/abs/2503.01163 (a28, a29, b14-b16, c01-c03, d07, d08)
- [V] Shi et al. (2024) TRIPLE. https://arxiv.org/abs/2402.09723 (a30, a31, b17, b18, c04, c05)
- [V] Pryzant et al. (2023) ProTeGi. https://arxiv.org/abs/2305.03495 (c06)
- [V] Inoue et al. (2025) AB-MCTS. https://arxiv.org/abs/2503.04412 (c07, c08)
- [V*] Prompt Duel Optimizer (2025). https://arxiv.org/abs/2510.13907 (b19)
- [V*] Lange et al. (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349 (b20, c09)
- [V*] Sui et al. Meta-Reasoner. https://arxiv.org/abs/2502.19918 (b21, c15)
- [V*] AdaEvolve (2026). https://arxiv.org/abs/2602.20133 (b22, d09)
- [V] Simonides (2026) LLaMEA operator analysis, Leiden MSc thesis. https://theses.liacs.nl/pdf/2025-2026-SimonidesKKoen.pdf (c10, c11)
- [V*] TIDE (2026). https://arxiv.org/abs/2601.21239 (c12)
- [V*] Deliberate Evolution (2026). https://arxiv.org/abs/2606.04360 (c13, d10)
- [V*] CoEvo-AHD (2026). https://arxiv.org/abs/2606.00718 (c14)
- [V*] PAK-UCB (Hu et al.). https://arxiv.org/abs/2410.13287 (c22)
- [V] Alamdari, Cao, Wilson (2024) Jump Starting Bandits with LLM-Generated Prior Knowledge. https://arxiv.org/abs/2406.19317 (d01)

**LLMs as bandit agents**
- [V] Krishnamurthy et al. (2024) Can large language models explore in-context? https://arxiv.org/abs/2403.15371 (c16)
- [V*] Nie et al. (2024) EVOLvE / BanditBench. https://arxiv.org/abs/2410.06238 (c17)
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (c18)
- [V*] Zhang et al. (2025) Exploration-exploitation of LLMs vs humans vs MAB algorithms. https://arxiv.org/abs/2505.09901 (c19)
- [V*] Semantic Bandits (2026). https://arxiv.org/abs/2608.16707 (c20)
- [V*] Berdica et al. (2026) When Do We Need LLMs? https://arxiv.org/abs/2604.05859 (c21)
- [V*] TextBandit (2025). https://arxiv.org/abs/2510.13878 (c24)

**Own work**
- Local simulations d15 to d18 (not papers); task-level re-analyses d07 and d08 of OPTS tables.

Note on the V* group: the critique re-opened OPTS, TRIPLE, DYTS, Kaufmann, AB-MCTS, PAK-UCB (text figures only), Auer, Chapelle and Li, Da Costa and Simonides as PDF text. The V* sources were read through fetch summaries and their numbers were not re-checked.
