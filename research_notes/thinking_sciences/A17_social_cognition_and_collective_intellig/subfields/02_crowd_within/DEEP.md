# Crowd within: deep document

*Subfield A17.02. Written 2026-10-27 from evidence_a-d.jsonl (a01-a29, b01-b26, c01-c29, d01-d26), claims.jsonl (K01-K32) and critique.md in this folder. Evidence ids in brackets, for example [a02]. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

---

## 1. What it is

The "crowd within" is the idea that one mind can act like a small crowd. Ask one person the same question twice. Average the two answers. The average is usually closer to the truth than either answer alone.

Why it works, in the founding account: a guess is not a fixed best estimate. It is a draw from an internal probability distribution. Two draws carry partly independent noise. Averaging cancels some of that noise [a04].

What it cannot do:
- It removes variance. It does not remove bias. Shared bias stays [a03, a11].
- The second guess from the same mind is worth far less than a guess from a second person. Best estimates: about 1.1 to 1.5 independent people [K02].
- It only works if there is spread to average. An expert who gives the same answer every time has nothing to average [b06].

For our agent the mapping is direct. A language model at temperature above zero is literally a sampler from a distribution. So "resample and combine" is a crowd within. Self-consistency voting is the machine form [a25]. The human literature gives us the shape of the curve (small gain, fast saturation, ceiling near 1.5 to 2 independent sources). The LLM literature tells us where the machine case differs (discrete answers, big gains on weak baselines, shared errors, often zero spread on strong models).

Boundary of this document: single-model resampling and its combination rules. Debate, self-correction and cross-model crowds appear only as comparison points. Links to parallel subfields (not covered here): Bias and debiasing; Reflective reasoning and second look; Diagnosticity of evidence; Generation versus evaluation; Expected value of control; Outside view and base rates.

---

## 2. History and theories in depth

### 2.1 Before 2008: averaging within a judge

- **Ariely et al. 2000.** Tested averaging within one judge for subjective probabilities. 64 volunteers judged 200 true/false statements about US city populations over 400 trials in 4 blocks. Repeated items came back about 100 trials later. Mean probability score (lower is better): individual .252, within-person average .250, between-person average .234. Within-person correlation of repeats .66, between-person .57. The authors wrote that averaging pairs within subjects "has virtually no effect" [d01]. First-hand read in the gap search; earlier snippets (a05) only described it second hand.
- **Why Ariely found nothing, per Vul and Pashler:** probability judgments are biased toward 0 and 1. Averaging cuts variance but not bias. Ariely's own paper gives two reasons it cannot separate: correlated pairs need many more than two draws to help, or the dependence has a form the correlation misses [d01, a05].
- **Earlier treatment of the second guess** was as a debiasing aid (Hirt and Markman 1995; Mussweiler et al. 2000), not as a sample [a04].

### 2.2 Vul and Pashler 2008: the founding study

- 428 online participants, 8 CIA World Factbook percentage questions. They were unexpectedly asked for a second, different guess, either at once (n=255) or 3 weeks later (n=173) [a01, b01].
- The average beat both single guesses. Second guesses were worse than first guesses (t(254)=3.6 immediate, t(172)=2.8 delayed). That is the key point: the gain is not new information. It rules out "people looked something up" [a04].
- Size of the gain: error cut vs guess 1, 95% CI [2.5%, 10.4%] immediate and [11.6%, 20.4%] delayed [a02].
- Formal model (section 4): lambda 0.11 immediate, 0.32 delayed. Their summary: you gain about one tenth as much from asking yourself twice as from a second opinion [a02].
- Authors later said they under-reported the t values. Corrected: immediate 4.41 and 9.90, delayed 6.22 and 9.85. The delay-vs-immediate test moved from t(426)=2.12 to t=2.68, p=.008 [a08, b01].
- Explanation offered for the delay benefit: less anchoring on the first guess [b01].

### 2.3 Herzog and Hertwig 2009: dialectical bootstrapping

- Participants estimated years of historical events. The strategy group was told to assume the first estimate was wrong, think of reasons why, and estimate again. The claim: this gives a larger gain than just asking again [a13, b12].
- The original paper is paywalled. Not opened by us. What we know is second hand, plus the reanalysis below.
- Herzog and Hertwig's own control group (no strategy) gained 0.3 points of median error (SD 2.3, CI [0.0, 0.8], d=0.12) [a08, b03]. So the plain second-guess effect in that data set was close to zero.
- The method used 20 percent trimmed averages across participants [a16].

### 2.4 First replications and the dispute (2010-2014)

- **Hourihan and Benjamin 2010.** N=170. MSE: average 484, guess 1 502 (t(169)=2.15, p=.03), guess 2 565. Moderator: low working-memory people gained more (r=-.16; 1.07 vs 1.04 equivalent persons). Account: a smaller memory sample per guess overlaps less across guesses [a09, b04].
- **Rauhut and Lorenz 2011.** Five estimates per person. Averaging five was no better than averaging the first two. Unopened, known through later papers [a18, b23].
- **Herzog and Hertwig 2009 (control), Banker and McCoy (unpublished).** Gain with CI touching zero (d=0.12); gain non-significant but in the expected direction (MSE 463 to 452, n=201, dz=0.16) [a08].
- **Steegen et al. 2014**, pre-registered, high powered (section 5.1). The effect replicated.
- **White and Antonakis 2013.** Reanalysed Herzog and Hertwig's data: 40 date items, 101 people (50 dialectical, 51 control). The headline gain came from a score tied to how often the second guess equals the first (0.7% identical in dialectical vs 20.2% in control). With an untied score, both groups gained equally: median absolute error 130.9 to 125.8 (dialectical) and 130.5 to 125.4 (control); interaction F(1,99)=0.00, p=.98; d=0.38 vs 0.39. Quote: "Dialectical instructions are not needed to achieve the wisdom of many in one mind" [d02]. Herzog and Hertwig replied that measure and trimming explain the gap (unopened) [b13].
- **Fraundorf and Benjamin 2014.** People cannot tell when to average (section 5.4) [a17].

### 2.5 Field data and the expertise boundary (2018-2021)

- **van Dolder and van den Assem 2018.** 1.2 million observations from three incentivised guessing contests. Within-person aggregation helps, more with delay, but "the average of a large number of judgements from the same person is barely better than the average of two judgements from different people." Abstract only [b11, a19].
- **Fiechter and Kornell 2021.** Numerosity task. Without training, inner-crowd variance term a=0.05 (BF10 1417). After 12 practice trials with feedback, a=0.005 (BF10 0.02, evidence for no effect), while the outer-crowd effect stayed (a=0.024) [a10, b06]. Expertise kills the inner crowd.

### 2.6 Different-perspective and ensemble methods (2023-2026)

- **Fujisaki, Yang, Ueda 2023.** Give your own estimate, then estimate what people in general would say, and average. Beat dialectical and plain repeats on MSE reduction in Exp 1 and 2; five estimates were no better than two [a22, b09].
- **Gomilsek et al. 2024.** Fermi-style decomposition vs dialectical vs control, N=285. All gained 1 to 4 percent; strategy effect not significant; ranking flipped with trimming [a14, b08].
- **Fujisaki et al. 2025.** Five thinking styles kept improving with more estimates (d=0.59 vs five plain repeats); still only about 1.5 persons [a23, b10].
- **Van de Calseyde and Efendic 2025.** N=2,884. Disagreeing perspectives help on hard items, hurt on easy ones [a21, b07].
- **2026 reanalyses (OSF preprints, abstract only).** Repeated-estimate baseline near-zero net gain; dialectical bootstrapping worsened crowd accuracy; mixed-instruction crowds did not beat the best single instruction at any group size [d03]. A measurement paper warns that squared-error scores mix a shift in position with a change in spread [d04].
- **2026 perceptual replication.** Unfamiliar face matching, 80 trials. Aggregating one person's 2 or 3 decisions raised AUC by 5.9 and 7.9 percent. A week's delay did not add to it. Cross-person aggregation gained more [a24].

### 2.7 The machine line

- **Self-consistency (Wang et al. 2022/2023).** Sample many reasoning chains, vote on the final answer. This is the crowd within for LLMs. It was invented independently of the human literature [a25, b16].
- **Agent Forest (Li et al. 2024).** Same-model sampling and voting scales with ensemble size; larger relative gain on hard tasks [a26, b17].
- **Self-correction critique (Huang et al. 2024).** The machine version of dialectical bootstrapping (reconsider with no outside feedback) fails [a27, b18].
- **Correlation measurements (2025-2026).** Kim et al. (between models), Yu et al., Nguyen et al., Kohli (measured effective votes) [a29, d05, d08, d17].
- **Efficiency and boundary studies (2025-2026).** Self-consistency losing its edge on near-ceiling models; fresh vs same-context resampling; two-call bound on vote gain [d16, d21, d11].

### 2.8 Competing explanations for the human effect

1. **Sampling from an internal distribution** (Vul and Pashler). Gains come from cancelling independent noise [a04].
2. **Memory overlap** (Hourihan and Benjamin). Independence of draws depends on how much of the same memory sample is reused [a09].
3. **Anchoring** (delay account). The first guess biases the second. Delay or a different perspective lowers anchoring [b01].
4. **Strategy change / use of a second view.** Dialectical and other-perspective prompts. Largely not supported once the metric is fixed [d02].
5. **Pure arithmetic of the squared error.** The diversity prediction theorem: crowd gain equals variance of the estimates. Describes, does not explain [a11].
6. **Bracketing.** The truth falls between the two guesses more often, which guarantees the average beats at least one. Bracketing rates: 22 percent self-perspective vs 35 percent disagreeing in Exp 2 [a21]; helpful bracketing 70.6 percent of cases in Gomilsek [b08].

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested (from claims.jsonl).

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Averaging two guesses beats either one | Original N=428, 8 items: avg beat guess 1 t(254)=2.25 (later corrected 4.41) immediate, t(172)=3.94 delayed. Error cut CI [2.5,10.4]% immediate, [11.6,20.4]% delayed | Vul and Pashler 2008 [a01, a02] | [E] (K01) |
| Replication, pre-registered | Immediate N=471: MSE 589 / 615 / 541 (guess 1 / guess 2 / average), dz 0.40 vs g1, 0.47 vs g2. Delayed N=140: 517 / 589 / 467, dz 0.34 vs g1, 0.72 vs g2 | Steegen et al. 2014 [a06, b02] | [E] (K01) |
| Second guess is worse than first, average still wins | dz -0.10 immediate, -0.25 delayed (Steegen); t(254)=3.6 and t(172)=2.8 (original); MSE 502 vs 565 (Hourihan) | [a01, a06, a09] | [E] |
| A second guess from yourself is worth little | lambda 0.11 immediate, 0.32 delayed; 1.11 and 1.32 equivalent people; 1.04 to 1.07 in Hourihan; about 1.5 for a five-style ensemble | [a02, a09, a23] | [E] (K02) |
| Many own guesses approach only about two people | "Barely better than the average of two judgements from different people", 1.2 million observations | van Dolder and van den Assem 2018 (abstract) [b11] | [E] with K02 |
| More plain own estimates stop helping | MSE flat from 1 to 5 plain estimates; five estimates no better than two (t57=0.032, p=.97) | Rauhut and Lorenz 2011 via others; Fujisaki 2023, 2025 [b09, b10, b23] | [S] (K03) |
| Delay between guesses helps | Original: delayed gain larger. Steegen: vs guess 1 no extra benefit (gain 50 vs 48, t(609)=0.18, p=.858, BF 12.9 for no difference); vs guess 2 yes (121 vs 73, t(609)=3.14, p=.002, d=0.30, post hoc). 2026 perceptual: no delay gain | [a07, b02, a24] | [C] (K04) |
| Expertise removes the inner-crowd gain | Untrained a=0.05 (BF10 1417); trained a=0.005 (BF10 0.02). Outer crowd stays (0.10 vs 0.024) | Fiechter and Kornell 2021 [a10, b06] | [S] (K05) |
| Gain is larger on hard items | Disagreeing perspective beat self on 87 percent of hard items vs 33 percent of easy (Exp 2); interaction -13.49, CrI [-19.77,-7.34]; N=2,884 | Van de Calseyde and Efendic 2025 [a21, b07] | [E] with LLM data (K07) |
| Low-span people gain more | r=-.16, p<.05; 1.07 vs 1.04 persons; N=170 | Hourihan and Benjamin 2010 [a09, b04] | [S] (K22) |
| Dialectical bootstrapping beats a plain second guess | Original claim. Reanalysis: 130.9 to 125.8 vs 130.5 to 125.4, interaction p=.98, d=0.38 vs 0.39. Gomilsek: strategy effect F(2,279)=1.07 p=.345; d=0.007 untrimmed vs d=0.40 trimmed | White and Antonakis 2013; Gomilsek 2024 [d02, b08] | [C] (K08) |
| Control (plain) second guess in H&H data | 0.3 points median error gain, CI [0.0,0.8], d=0.12 | [a08] | [E] small |
| Other-perspective ("what would people say") beats dialectical and repeats | Exp 1 N=452: MSE-reduction CI other [29.40,75.63], dialectical [19.69,68.92], repeated [-1.46,33.70]. Exp 3: five estimates no gain over two | Fujisaki 2023 [a22, b09] | [C] (K10) |
| Five thinking styles keep improving | N=76 (38 per arm); d=0.59, t=2.51, p=.012; 1.51 persons at T=5; ceiling under 2 | Fujisaki 2025 [a23, b10] | [C] (K10). Note: a23 said N=64; the paper says 76 |
| Fermi decomposition as second sample | Untrimmed error cut 2.6 percent (d=0.34) aided, 3.9 percent (d=0.31) unaided; N=285 | Gomilsek 2024 [a14] | [S] |
| Asking another person beats asking yourself again | Better in all 6 conditions; mean +8.3 points (SE 0.8) | Gomilsek 2024 [a15] | [E] (K16) |
| People cannot choose between their own guesses | Pooled MSE first 537, second 606, average 500. Choosing accuracy 47 to 57 percent; break-even 67 percent; only 17 of 52 reached it | Fraundorf and Benjamin 2014 [a17, b05] | [E] (K09) |
| Averaging two own confidence ratings | d=0.67 to 1.44 over taking the higher one, three data sets; own confidence correlation r=.50 to .85 | Litvinova et al. (abstract) [b15] | [S] (K23) |
| Within-person averaging of probabilities | PS .252 to .250 (within) vs .234 (between), N=64 | Ariely et al. 2000 [d01] | [S] (K30) |
| Inner crowd in perceptual decisions | AUC +5.9 percent after 2, +7.9 after 3; accuracy +2.3 and +4.8 percent | 2026 face matching [a24] | [S] (K21) |

### 3.2 LLM studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Self-consistency over greedy CoT | PaLM-540B GSM8K 56.5 to 74.4 (+17.9); AQuA +12.5; SVAMP +7.6; AddSub 91.9 to 93.7 (+1.8); LaMDA-137B GSM8K 17.1 to 27.7; UL2-20B 4.1 to 7.3. 40 paths | Wang et al. [a25, b16, c06] | [E] (K11) |
| Equal-response comparison on GPT-3.5 GSM8K | 1 response 76.7; self-consistency 82.5 / 85.3 / 88.2 at 3 / 6 / 9 | Huang et al. 2024 [a27, c23] | [E] |
| Small model matches bigger | Llama2-13B ensemble 0.59 vs Llama2-70B single 0.54 on GSM8K (size 40; parity at 15) | Li et al. 2024 [a26, b17] | [E] |
| Relative gain larger when baseline weak | GSM8K relative gain 69 percent (13B), 37 (70B), 16 (GPT-3.5); MATH 200, 120, 34. Absolute: MATH Llama2-13B only 0.03 to 0.09 | [b17, c19] | [E] (K07) |
| Gain shrinks near ceiling | Gemini-2.5-Pro MATH-500: 98 percent single pass, 99.2 at 3 samples, 99.6 at 15 (+1.6 at about 15x cost); Flash-Lite HotpotQA +0.4 from 1 to 20 samples | Loo 2025 [d16] | [E] with K07 |
| Strong models give zero spread | 78 of 108 GPT-4/4o runs had near-zero SD over 30 runs at T=0.8; 79 percent of open-ended cases had mean similarity above 0.8 (T=1.0, 50 responses) | Lou and Sun 2024; Jiang et al. 2025 [c12, c15] | [E] (K06) |
| Share of near-unanimous items | 32.7 percent (Qwen3-1.7B, T=1.5, MMLU-Pro); two calls of Qwen2.5-7B at T=0.2 disagree on about 0.6 percent | [d20, d11] | [E] with K06 |
| Same-model vote is worth about 1.3 to 2.9 independent votes | Correctness correlation 0.45 to 0.60 (GSM8K), ceiling 1.7 to 2.2, reached by K=8 to 16 [d05]; error correlation 0.35 to 0.77, cap 1/rho [d08]; nine frontier models 2.18 effective votes, CI [2.07,2.31] [d17] | Yu 2026; Nguyen 2026; Kohli 2026 | [E] (K24). Small open models only |
| Self-review without feedback fails | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0 (3 and 5 calls); oracle labels lift it (97.5), so the gain is the label, not the review | Huang et al. 2024 [a27, b18, c22] | [E] (K12) |
| Same-context self-refine gains little | Best-round gain 0.0 to 6.7 points; loss up to 44.3 at tightest window | Nguyen 2026 [d25] | [E] with K12 |
| Debate ties or loses to equal-budget voting | Self-consistency at least as good as debate in 93 percent of 980 settings; significantly better in 57; debate better in 0.5. 23-model study: debate no edge over 9-sample vote, 1.6x wall-clock, 3.4x tokens | Nguyen 2026; Ferreira 2026 [d09, d22] | [E] (K18) |
| Voting plateaus, coverage keeps rising | MATH Llama-3-8B: coverage 82.9 percent at 100 samples to 98.44 at 10,000; vote 40.50 to 41.41 | Brown et al. 2024 [c21] | [E] (K13) |
| Majority vs oracle gap for a small model | 40.7 vs 44.7 percent (128 samples); best combiner wins back about 38 percent of gap (+2.24 points non-trivial) | Sakai 2026 [d20] | [S] (K32) |
| Forecast resampling | Baseline Brier 0.1676; mean 0.1656; median 0.1651; geometric mean 0.1655; trimmed 0.1649 (gain 0.0027, 1.6 percent); USC 0.1691; human crowd 0.1600 | Halawi et al. [b21, d24] | [C] (K14, K29) |
| Resampling 500 draws, numeric inflation forecasts | 7 to 35 percent error cut, most within 10 draws; removable variation about 16 percent of single-response error | Jaworski and Alam 2026 (abstract) [c11] | [C] (K14) |
| Cross-model crowd matches human crowd | 12 models, 31 questions: Brier 0.20 vs 0.19, p=.85. Best single (GPT-4) 0.15, better than the crowd | Schoenegger et al. [c01, b20] | [S]. Not a same-model test |
| Mixing in a human median beats self-update | GPT-4 0.17 to 0.14, Claude 2 0.22 to 0.15; plain machine+human average 0.13 and 0.14, better than the update | [c03] | [E] with a15 (K16) |
| Errors shared across models | Both wrong: agree about 60 percent (chance 1/3); 349 models, 12,032 questions | Kim et al. 2025 [a29, b19] | [E] (K15) |
| Confident wrong majorities | Nine models: all wrong on 5.1 percent of items (<1 in 1,000 under independence); unanimous answers right 90.9 percent. gpt-4.1 GPQA: high-agreement answer wrong 48 percent, CI [.40,.56]; 28 percent of cases wrong for every runner | Kohli 2026; Ding 2026 [d17, d18] | [E] (K31) |
| Voting fails when the right answer is a minority | 20.4 to 6.0 percent from N=1 to 16 on a selected subset | Wang, Hong, Bagci 2026 [d19] | [S]. Subset chosen by outcome |
| Prompt variation lowers correlation, moves accuracy little | Correlation fell in 55 of 57 cells (mean -38 percent; QA -67, math -9 to -29); accuracy within +-4 points, mixed sign | Yu et al. 2026 [d06] | [S] (K26) |
| Method diversity beats resampling in planning | GPT-4 graph coloring: SC-10 23 vs IDIV-SE 74 vs DIV-SE 97; Blocksworld 3 GPT-4: SC-10 73 vs DIV-SE 94; AQuA +9.8 to +16.5 | Naik et al. [b22, c28] | [C] (K17) |
| Mixed prompts or models worse than resampling | PaLM GSM8K: SC x40 74.4, 40 prompt sets 58.9, mixed models 16.0 to 36.9; Self-MoA +6.6 percent over mixed MoA | Wang; Li (Self-MoA) [c07, c20] | [C] (K17) |
| Persona prompts cost accuracy | Mean over tasks: solo 80.4, debate 84.4, SC-9 84.8, persona 81.9 (scrambled row) | Ferreira 2026 [d22] | [C] (K17) |
| Fresh context beats showing the failed attempt | Near-identical retry 33 to 68 percent shown own code vs 2 to 14 percent fresh; 1.5B .749 vs .688 (p=.006); tie at 7B | Verma 2026 [d21] | [S] (K28) |
| Sequential beats parallel at equal tokens | 43 of 45 settings; text/table mismatch on the headline cell (76.7 vs 83.3); 30-problem sets | Sharma and Chopra 2025 [d13] | [C] (K27) |
| Parallel voting beats elaborate loops | Majority voting best of verifier-free methods; sequential revisions add drift | Wang et al. 2025; Zeng et al. 2025 [d14, d15] | [C] (K27) |
| Temperature up to 1.0 does not hurt single-sample accuracy | Kruskal-Wallis H(10)=10.439, p=0.403 (GPT-3.5 CoT, 1,000 questions); incoherent at 1.6 | Renze and Guven 2024 [c25] | [S] (K19) |
| Temperature raises vote gain | QQP: 5-vote gain -0.06 to +2.57 over T=0.2 to 2.0 | Liu 2026 [d12] | [S] |
| Verbalized sampling restores diversity | 1.6 to 2.1 times diversity in creative writing; not accuracy | Zhang et al. 2025 [c17] | [S] (K20) |
| Cheap pilot sets the sample budget | K=4 pilot; rule keeps 96 to 103 percent of K=32 accuracy at 25 to 44 percent of cost | Yu et al. 2026 [d07] | [E] with d11 (K25). Small models |
| Two-call disagreement caps vote gain | 3-vote gain at most half the disagreement rate; 0.6 percent disagreement gives cap +0.46 | Liu 2026 [d11] | [E] with d07 (K25) |

---

## 4. Mechanisms and models

### 4.1 Hyperbola across independent people

Mean squared error of the average of N different people: `MSE(N) = a/N + b`. Fits Vul and Pashler across-person data with R2=1 [a03].
- `b` is the shared bias of the population. No averaging removes it.
- `a` is the variance term. It is what averaging removes.
- The same fit, `a/t + b`, is used for inner crowds by Fiechter and Kornell [a10].

### 4.2 Lambda: what is the next same-source sample worth?

Within one person, N guesses reduce error by `1 / [1 + lambda (N - 1)]`. Lambda is the worth of an extra own guess against one from another person. 0 means nothing, 1 means a full independent sample [a03].
- Human values: 0.11 immediate, 0.32 delayed.
- Lambda comes from interpolating on the fitted curve, so it is model dependent [a02].
- At infinity the limit is `1/lambda` independent people at most. With lambda 0.5 that is 2.

### 4.3 Design effect and effective votes (the engineering form)

Same idea, written for voters. For K samples with pairwise correlation `c` (or `rho`):

`n_eff = K / (1 + (K - 1) * c)`, and `n_eff <= 1/c` as K grows [d05, d08].

Measured values for LLMs:
- Correctness correlation (GSM8K, T=0.7): Qwen2.5-7B 0.60 (n_eff 1.42 / 1.55 / 1.65 / 1.67 at K=4/8/16/32, ceiling 1.71), Llama-3.1-8B 0.53 (1.55 to 1.94), Mistral-7B 0.45 (1.71 to 2.13, ceiling 2.21). HotpotQA 0.61, BoolQ 0.79 [d05].
- Error correlation: 0.35 to 0.77 over five models and four tasks; hardest, most structured tasks (MATH500) 0.5 to 0.77 [d08].
- Nine different frontier models: n_eff 2.18 (phi .391) [d17].
- The assumption of independence predicted 100 percent accuracy where truth was 81.9 (error 18 to 24 points). A beta-binomial fit from a K=4 pilot predicted K=32 accuracy within 3.3 to 4.8 points [d05].
- Caution: correctness correlation across questions mixes shared item difficulty with true dependence. What we really need for planning is the spread of per-item success rates, which a pilot can estimate [critique].

### 4.4 Diversity prediction theorem

Collective squared error = average individual squared error minus the variance of the estimates (Page 2007) [a11, a20, b25].
- Gain from averaging equals the variance of the samples.
- Zero variance means zero gain, whatever the quality.
- Variance is not always useful: a wild guess adds variance and can raise the average individual error (Van de Calseyde: a third of forced contrary samples overshoot and hurt) [b07, b08].
- Fujisaki 2025: the ensemble had worse individual error but higher diversity and won [a20].

Practical use: measure spread over samples before paying for more.

### 4.5 Disagreement bound

For binary tasks, the 3-vote gain is at most half the rate at which two calls disagree [d11]. Run two samples on a validation slice. If they agree almost always, stop.
- Qwen2.5-7B at T=0.2: disagreement about 0.6 percent, so 3-vote gain cap +0.46 points, 5-vote cap +0.47; observed 5-vote gain at most 0.17 (QNLI) and 0.04 (QQP).
- Raising temperature from 0.2 to 2.0 raised the 5-vote gain from -0.06 to +2.57 points. It also lowered single-call accuracy [d12].

### 4.6 Adaptive sample count from a pilot

Rule from Yu et al.: estimate `c` from a K=4 pilot. Stop adding samples when the marginal gain of one more falls below 2.5 percent. Chosen K: 6 (c=0.60), 8 (c=0.53), 10 (c=0.45). Result: 96 to 103 percent of K=32 accuracy at 25 to 44 percent of the cost. Threshold 0.01 to 0.1 kept 97 to 101 percent. Global `c`, not per item; small instruct models [d07].

```
pilot(task_class):
    for item in sample(20..100 items):
        answers = [model(item, fresh_context) for _ in range(4)]
    c = mean pairwise correctness correlation
    K = smallest k with  n_eff(k+1) / n_eff(k) - 1 < 0.025
    store (task_class, c, K)
```

### 4.7 Coverage versus selection

Many samples produce a pool. The pool has two numbers: coverage (any sample correct) and vote accuracy.
- MATH, Llama-3-8B: coverage 82.9 percent at 100 samples, 98.44 at 10,000. Vote 40.50 to 41.41 [c21].
- MMLU-Pro (1.7B, 128 samples): vote 40.7, oracle 44.7 [d20].
- Voting plateaus near 100 samples. Beyond that, gains need a real check (G3), not more votes.
- Where the right answer is a minority, voting falls as samples are added [d19].

### 4.8 Combiners

For numbers (forecasts, estimates):
- Mean, median, geometric mean and trimmed mean: within 0.0007 Brier of each other at n=6 [d24].
- LLM-as-aggregator (USC): worse than no ensemble (.1691 vs .1676) [b21, d24].
- Median is the safe code-side choice when the samples may share a lean [c02].
- Report with and without trimming. The dialectical dispute is a trimming dispute [a16, b08].

For discrete answers: plurality vote, in code. Agreement rate tracks accuracy but is only a hint [c08, d18].

### 4.9 Bracketing and the unit of analysis

Bracketing: the truth lies between the two guesses. Helpful bracketing (average beats the better guess) occurred in 70.6 percent of Gomilsek cases [b08]. Bracketing rate rose from 22 to 35 percent with a disagreeing perspective [a21]. Guess correlation fell from r=.74 (self) to r=.33 (disagree) [b07].

### 4.10 Measuring correctly

- Report bias (shift of the mean toward the truth) and spread (variance) separately. A folded score hides which one moved [d04].
- Do not use a score tied to the second answer equalling the first. This produced the dialectical result [d02].
- Compare against a single sampled answer at working settings, not greedy. Greedy is a weak baseline and inflates the gain (PaLM +17.9) [b26].

---

## 5. What holds up

### 5.1 Replications

| Check | Result |
|---|---|
| Vul and Pashler immediate effect, Steegen (N=471, pre-registered) | Replicated. dz 0.40 vs guess 1, 0.47 vs guess 2 [a06] |
| Delayed effect, Steegen (N=140) | Replicated vs both guesses (dz 0.34, 0.72). But the delay moderator only half-replicated [a07] |
| Hourihan and Benjamin (N=170) | Replicated (average 484 vs 502, p=.03) [a09] |
| Rauhut and Lorenz 2011 | Found a gain; no extra gain past two estimates [a18] |
| Herzog and Hertwig 2009 (control) | Gain d=0.12, CI includes zero [a08] |
| Banker and McCoy (unpublished) | Non-significant, expected direction (dz=0.16) [a08] |
| Muller-Trede 2011, numerical general knowledge | Mixed record ("but see") [a12] |
| van Dolder (field, 1.2 million observations) | Positive, tiny against two people [b11] |
| Face matching 2026 | Positive (AUC +5.9, +7.9 percent); delay no help [a24] |

Overall: the basic effect is real and robust in percentage and quantity questions. It is small. Effect size against the first guess: dz 0.12 to 0.40. Error cut about 8 percent (541 vs 589) [K01].

### 5.2 Failures and disputed results

- **Ariely 2000:** no within-person gain for probability scores [d01].
- **Dialectical bootstrapping:** the extra gain was an artefact of the score. White and Antonakis: d=0.38 vs 0.39, p=.98. Gomilsek: no strategy difference untrimmed, d=0.40 only with 20 percent trimming. 2026 reanalysis (abstract): worse crowd accuracy [d02, b08, d03].
- **Delay:** Steegen BF 12.9 for no difference vs guess 1. 2026 perceptual: no delay gain [a07, a24].
- **Multi-estimate gains:** five plain estimates no better than two [b09, b23].
- **Perspective methods:** the 2025 five-style gain (d=0.59) comes from one lab; the same research tradition's 2026 reanalysis found mixed-instruction crowds no better than the best single instruction [a23, d03].

### 5.3 Moderators

| Factor | Direction | Evidence |
|---|---|---|
| Independence of the second sample (delay, method, perspective) | More independence, more gain; but net still about 1.5 persons | [b01, a21, a23] |
| Item difficulty / first-guess error | Harder: larger gain (disagreeing perspective helps 87 percent of hard items; hurts 67 percent of easy) | [b07] |
| Expertise / peaked answer distribution | Removes the gain | [a10, b06] |
| Working memory span | Low span gains slightly more (1.07 vs 1.04) | [a09] |
| Baseline strength in LLMs | Gain larger when weak; +17.9 at 56.5, +1.8 at 91.9; +1.6 at 98 | [a25, d16] |
| Temperature | Higher T lowers correlation and raises vote gain, costs single-call accuracy | [d12, c25] |
| Task type | Open-ended: very similar samples; discrete reasoning: large vote gains; chess: +1 to 4 | [c15, a26, b17] |
| Model size | Bigger models vary less between calls and gain less | [c11, c12] |

### 5.4 Interventions

Worked:
- Taking the average (or a vote) in code, always. People who choose do worse than the always-average rule [a17, b14].
- Independent resampling and voting on discrete-answer reasoning tasks [a25, a26].
- Different thinking styles per estimate: gain keeps growing past two samples (human, one lab) [a23].
- Mixing in a different source: another person [a15], a human forecast [c03].
- Fresh context for retries in small code models [d21].
- Two-call or K=4 pilot to size the sample budget [d07, d11].

Did not work:
- "Assume you were wrong" second-look prompts as a gain over plain resampling [d02, a27].
- Asking the model to review itself with no feedback [a27, c22, d25].
- Asking the model to combine its own samples (USC) [b21, d24].
- Debate beyond equal-budget voting [d09, d22].
- Persona voters [d22].
- Debiasing prompts for anchoring (CoT, ignore-anchor, reflection) [c13].
- Letting people pick the better of their own guesses [a17].
- Consistency patches for forecasts: raised consistency, not accuracy [c27].

---

## 6. Language models

### 6.1 How an LLM crowd within behaves

1. **Large gains on discrete reasoning with weak baselines.** Self-consistency +17.9 on GSM8K (PaLM-540B, vs greedy). GPT-3.5 76.7 to 88.2 at 9 samples [a25, a27]. This is far larger than the human 8 percent. The cause is task type (a discrete answer, many reasoning paths, a weak greedy baseline), not a stronger inner crowd [critique].
2. **Gains shrink near ceiling.** +1.8 on AddSub (91.9); +1.6 for Gemini-2.5-Pro at 98 percent single pass; +0.4 for Flash-Lite on HotpotQA at about 20x tokens [c06, d16].
3. **Strong models often show no spread.** 78 of 108 GPT-4/4o runs had near-zero SD [c12]. 32.7 percent of items near-unanimous for a 1.7B model at T=1.5 [d20].
4. **Open-ended outputs are alike.** 79 percent of cases have mean similarity above 0.8 at T=1.0. Across models, 71 to 82 percent [c15, c16].
5. **Effective sample size is about 2.** 1.3 to 2.9 votes for small models [d05, d08]; 2.18 for nine frontier models [d17]. Same-model is at best equal to that.
6. **Votes saturate fast.** K=8 to 16 reaches 96 to 98 percent of the ceiling [d05]. Coverage keeps rising to 10,000 samples; vote does not [c21].
7. **Agreement is a hint, not proof.** gpt-4.1 on GPQA: 48 percent of high-agreement answers wrong; 28 percent confidently wrong for every runner. Exploratory Claude tiers showed the same pattern [d18]. Unanimous panel answers right 90.9 percent [d17].
8. **Self-review fails.** CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0. GPT-3.5 kept its GSM8K answer 74.7 percent of the time and flipped right to wrong more often than wrong to right [a27, b18]. Small models churn: Llama changed 40 to 52 percent of anchoring decisions when allowed to revise [c14].
9. **Anchoring.** GPT-4 anchoring index about 0.45 (human 0.61). Debiasing prompts did not fix it. Several hints from different angles helped [c13]. Shown its own failed code, a model made a near-identical retry 33 to 68 percent of the time [d21].

### 6.2 What changed the gain, and by how much

| Lever | Effect | Source |
|---|---|---|
| Samples K=1 to 9 (GPT-3.5, GSM8K) | 76.7, 82.5, 85.3, 88.2 | [a27] |
| Samples 1 to 40 (Llama2-13B, GSM8K) | 0.35 to 0.59; MATH 0.03 to 0.09 | [b17] |
| Temperature 0.2 to 2.0 (small binary tasks) | 5-vote gain -0.06 to +2.57 | [d12] |
| Temperature 0.5 to 1.2 (gpt-oss-120b, N=8, 50 AIMO problems) | 38, 40, 39.3, 37 of 50; no real difference | [d10] |
| Prompt-template variation | correlation -38 percent; accuracy +-4, mixed | [d06] |
| Method diversity (planning, graph coloring) | GPT-4 23 to 97 | [b22] |
| Mixed prompt sets | 74.4 to 58.9 (PaLM GSM8K) | [c07] |
| Persona prompts | about -2.9 vs SC-9 mean | [d22] |
| Model size at equal N=8 | gpt-oss-120b 39.3 vs 20b 31.0 (bigger than any prompt trick) | [d10] |
| Fresh vs continued context | 2 to 14 vs 33 to 68 percent near-identical | [d21] |
| Combiner for forecasts | within 0.0007 Brier; LLM aggregator -0.0015 | [d24] |
| Mixing in a human crowd forecast | GPT-4 Brier 0.17 to 0.13 (plain average) | [c03] |
| Chain length for reasoning models | longer is not better; shorter correct solutions; revision plateaus after about 10 steps | [d15] |
| Sequential refinement at equal tokens | contested: wins 43 of 45 [d13] vs loses to voting [d14, d15, d09] | |

### 6.3 Forecasting and numbers

- Six same-system forecasts averaged: Brier 0.1676 to 0.1649 (1.6 percent). Probably inside noise [b21, d24].
- 500 draws on inflation forecasts: 7 to 35 percent error cut, most within 10 draws (abstract only; could not be opened). Removable variation about 16 percent of single-response error, up to 76 [c11].
- Cross-model crowd (12 models): Brier 0.20 vs 0.19 for humans. Best single model (GPT-4, 0.15) beat the crowd. Acquiescence bias in the mean (57.35 percent) survived averaging [c01, b20, a28].
- Human crowd plus model: best in every setting [b21].

### 6.4 Why the human and LLM numbers differ

Human: 8 percent MSE, 1.1 to 1.5 persons, knowledge recall, noisy memory. LLM: +10 to +18 points on reasoning vote, 1.3 to 2.9 votes, discrete answers, varied reasoning paths. The vote converts path diversity into answer accuracy. The human average converts estimate noise into estimate accuracy. Do not transfer human numbers.

### 6.5 Dated warning

Most gains come from 2022 to 2024 models with weak greedy baselines (PaLM, LaMDA, GPT-3.5, Llama2). The effective-votes studies use 0.5B to 32B open models. Nothing in this folder measures n_eff for a current frontier reasoning model. The only frontier data are Kohli (nine models, NLI), Ding (GPQA), Loo (Gemini-2.5) and Harshavardhan (3 models, stated confidence only; df=14, weak) [d26].

---

## 7. What our agent should take

Schema parts: G (guardrail), S (state), O (operator), memory. Status: [E] established, [S] single source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| N1 | Plan for about 2 effective votes from one model, not k. State in G4 that extra same-model samples past K of about 8 to 16 add little. Cap plain resampling at a small K per item. | G4, G12 | [E] | K24, K02, K15; a02, a29, d05, d08, d17 |
| N2 | Combine in code with a fixed rule. For discrete answers plurality; for numbers the median. Never let the model choose between, or merge, its own samples. | G5 | [E] | K09, K12; a17, b05, b14, b21, d24, c22 |
| N3 | Gate extra sampling on spread. Two samples per item; if they agree and the item has a passing check, stop. Zero spread means no gain. | G12, S0 | [E] (human + LLM) | K06, K07, K25; a10, b06, c12, d11, d16, d20 |
| N4 | Calibrate the budget once per problem class with a K=4 pilot, not a fixed k. Store `c` and chosen K in the class record. Small-model evidence; verify on our model (see U1). | memory (class record), G12 | [E] (2 sources, small models) | K25; d07, d11 |
| N5 | Agreement is a hint, never a pass. Do not skip a check because samples agree. | G3, G4 | [E] | K31, K15; d17, d18, c08 |
| N6 | Do not use "assume your answer is wrong" or free self-review as an accuracy booster. Keep out of 4b list: unstructured second look. (Confirms existing 4b entry.) | 4b | [E] | K12; a27, c22, d25 |
| N7 | Log coverage (any attempt right), vote accuracy, and check-picked accuracy at 8, 16, 32 samples. The gap is the selection bottleneck. | Logging (section 6), S7 | [E] | K13; c21, d20 |
| N8 | Log per-item sample spread and the share of items with zero spread, per class. Feeds N3. | Logging | [E] | K06; c12, d20 |
| N9 | Mixing in an outside signal (a code-run check, retrieved evidence, a human prior) by a fixed rule beats the model's own update. | G3, S8 | [E] | K16; a15, c03 |
| N10 | Independent resampling beats debate at equal tokens (already G9). Keep an equal-token voting arm as the control for every multi-sample feature. | G9, G7 | [E] | K18; d09, d22, c23 |

### Test first

| # | Candidate | Part | Status | Evidence | Why not yet |
|---|---|---|---|---|---|
| T1 | Fresh-context vs continued-context second sample (the agent analogue of delay) | S3, G2 | [S] | K28, K04; d21, d25 | Small code models only; no lambda on numeric tasks; human delay effect contested |
| T2 | Prompt-diverse samples (different operators or framings) vs temperature-only samples | S3, O1-O8 | [C] | K17, K26, K10; b22, c07, d06, d10, d22 | Correlation falls but accuracy mixed; persona tax; conflict between DIV-SE and PaLM result |
| T3 | Other-perspective second sample ("what would others answer") combined in code | S3 | [C] | K10; a22, a23, d03 | One lab; 2026 reanalysis contradicts; no LLM test |
| T4 | Forced contrary ("assume wrong") sample combined by code, not self-review | S5 | [C] | K08; d02, d03 | Human gain was an artefact; no LLM test combined in code |
| T5 | Sequential refinement vs k parallel samples, equal tokens, reasoning model | G9, G11 | [C] | K27; d13, d14, d15, d23 | Two lines of evidence disagree; none on current reasoning models |
| T6 | Temperature raised to 0.8 to 1.0 for sampled attempts | S3 | [S] | K19; c25, d12 | Single-sample accuracy shown flat; vote gain shown small |
| T7 | Verbalized list ("give 5 answers with probabilities") in one call vs 5 independent calls | S3 open mode | [S] | K20; c17 | Diversity, not accuracy |
| T8 | Median of k numeric samples vs single sample for forecasts or estimates | G5 | [C] | K14, K29; b21, c11, d24 | 1.6 percent vs 7 to 35 percent unresolved |
| T9 | Averaging verbalized confidences (two fresh-context confidences) | G5 | [S] | K23, K30; b15, d01 | Human: Ariely says no gain; Litvinova says gain |
| T10 | Route extra samples by first-pass disagreement (difficulty signal) vs uniform | G12 | [E] direction, untested on our items | K07, K25 | Per-item routing not tested |
| T11 | Skip resampling for experts (peaked samples) | G12 | [S] | K05 | Same as N3; the human expertise study is single |

---

## 8. Concrete tests on our bench

All arms at equal total tokens (count prompt + completion tokens of every call, including pilots and any combiner). Plain model arm: one sampled attempt at working settings, not greedy. Report with item-level paired bootstrap CIs, and report bias and spread separately for numeric items.

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | ARC-style grid puzzles with a check; word puzzles (BRAINTEASER) | (a) 1 sample, (b) K=4 fresh-context samples + plurality, (c) K=8 plurality, (d) K=16 plurality; k set by budget split | Accuracy; effective votes `n_eff = K/(1+(K-1)c)`; coverage vs vote vs check-picked | Gain from K=1 to 4 positive, K=8 to 16 flat. n_eff 1.5 to 2.5. Coverage rises well above vote [K24, K13] |
| B2 | Same items | 2-sample gate vs always-K vs never resample | Accuracy at equal tokens; share of items gated out | Gate keeps 95+ percent of always-K accuracy at 30 to 60 percent fewer tokens; most savings on high-pass-rate classes [K25, K07] |
| B3 | Numeric estimate tasks (Fermi, percentage facts, quantities) | single vs mean of 2 vs median of 5, all samples fresh context | MSE, median absolute error, bias and variance separately, with and without 20 percent trimming | About 5 to 10 percent MSE cut from 2 samples, flat after about 2 to 3. Gain mostly variance, bias unchanged [K01, K03] |
| B4 | Forecast-style binary questions with known outcomes | single vs median of 5 vs mean of 5 vs model-merged | Brier score | Median or mean 1 to 3 percent better; model-merged worse [K14, K29] |
| B5 | Mixed items; control for fresh vs continued | k fresh-context samples vs k samples that see the previous one | Pairwise answer similarity; accuracy | Fresh lower similarity (2 to 14 vs 33 to 68 percent) and equal or better accuracy [K28] |
| B6 | Items with a check | temperature-only (T=0.7 to 1.0) vs 5 operator-diverse prompts vs 5 persona prompts | Accuracy; correlation c; n_eff | c falls about 38 percent with prompts; accuracy within +-4 points; persona worse [K26, K17] |
| B7 | Items with a check | k parallel samples vs one chain k times longer vs sequential refinement of k steps (reasoning model) | Accuracy | Parallel at least equal; sequential wins only if d13 is right [K27] |
| B8 | Hard vs easy halves (split by pilot pass rate) | uniform resample vs routed by 2-sample disagreement | Accuracy per token | Routing wins 5 to 20 percent tokens at same accuracy; contrary samples hurt easy items [K07, b07] |
| B9 | Items with a check | forced "assume wrong" second sample, combined by code, vs plain second sample | Accuracy; share of right-to-wrong flips | No gain over plain second sample [K08, d02] |
| B10 | Hard multiple-choice items | plurality vote vs check-picked from distinct answers | Rate of confident wrong majorities; accuracy | Wrong modal answer on 5 to 25 percent of hard items; the check picks better [K31, K32] |
| B11 | Any verbalised confidence | single confidence vs mean of 2 fresh-context confidences | Calibration error / Brier | Little or no gain [K30] |

---

## 9. What does not transfer, and why

- **Human gain sizes.** Human inner crowd is 8 percent MSE on percentage facts. LLM voting gains are 10 to 18 points on reasoning. Different tasks and baselines [critique].
- **The delay.** Humans forget; the first guess fades. A model has no fade; a fresh context removes the first answer completely. The closest analogue is fresh context, not time [K04, K28].
- **Working-memory overlap.** The memory-sample account has no direct model analogue. The nearest thing is retrieving different evidence per sample [a09].
- **Dialectical instructions.** They changed the answer but not the accuracy in people, and the model version (self-review) hurts. Instructions given inside the same context also anchor [d02, a27].
- **Expertise.** Humans become peaked with training. Models are peaked by default on easy items, and so the "expert" boundary is item-specific, not model-wide [c12].
- **Averaging.** Humans average numbers. Most agent tasks have discrete or structured answers. Plurality vote, not mean, is the operation. Averaging only suits numeric outputs [a25].
- **Perceptual and confidence findings.** Face matching and confidence averaging are boundary notes [K21, K23].
- **Between-model crowd results.** The 12-model forecasting crowd is not a test of the inner crowd. It supports "mix sources" [c01].
- **AIMO negative-correlation claim.** An algebraic artefact (-1/(N-1)); do not cite [d10].
- **Ariely's probability result** is about true/false probability scores with repeats separated by about 100 trials. It does not say an LLM's repeated samples never help [d01].
- **Small-model correlation numbers.** Effective-vote measurements come from 0.5B to 32B open models; do not assume the same for a frontier reasoning model [d05, d08].

---

## 10. Open questions

1. What is the within-model n_eff of a current frontier or reasoning model, at several temperatures, on numeric and discrete tasks? (No study. Decides how many samples are worth paying for.)
2. At equal tokens, does k-sample voting beat one longer reasoning pass for a current reasoning model? Three studies say yes for small models, one says no [K27].
3. What share of items on our benchmarks have zero spread? Does a two-sample test predict who gains per item (not just per dataset)?
4. Does fresh context lower correlation versus continued context, and by how much, on numeric tasks?
5. For same-model forecasts and numbers: is 1.6 percent vs 7 to 35 percent a task effect or a sample-count effect? (Jaworski and Alam not opened.)
6. Does a contrary or other-perspective sample, combined by code, help modern LLMs? No LLM test found.
7. How often is the wrong answer the modal answer on our tasks? (Ding found 48 percent for high-agreement answers on GPQA; our rate is unknown.)
8. Does prompt-diverse sampling beat temperature sampling when each variant's own quality is matched? (DIV-SE vs Wang vs Yu not reconciled.)
9. Do the human findings hold in modern, pre-registered, large studies outside percentage questions? Herzog and Hertwig 2009 and 2014, Rauhut and Lorenz 2011, Litvinova, van Dolder and Jaworski and Alam remain unopened.
10. Sample-count formula: is the 2.5 percent marginal-gain stop rule right for our model, or is a cost-aware rule better?
11. Does sample correlation depend on item difficulty, so that per-item n_eff is much lower on hard items?
12. Sharma and Chopra table/text mismatch: is "sequential wins 43 of 45" real?

---

## 11. Sources

[V] opened and read this session (full text or substantial text). [M] snippet, abstract or second-hand description only.

### Human studies

- [V] Vul and Pashler (2008) Measuring the crowd within. https://Www.Gwern.net/doc/statistics/prediction/2008-vul.pdf
- [V] Steegen, Dewitte, Tuerlinckx, Vanpaemel (2014) Measuring the crowd within again. https://pmc.ncbi.nlm.nih.gov/articles/PMC4112915/
- [V] Hourihan and Benjamin (2010) Smaller is better. https://pmc.ncbi.nlm.nih.gov/articles/PMC2891554/
- [V] Fraundorf and Benjamin (2014) Knowing the crowd within. https://pmc.ncbi.nlm.nih.gov/articles/PMC3915883/
- [V] Fiechter and Kornell (2021) How the wisdom of crowds, and of the crowd within, are affected by expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC7865038/
- [V] Gomilsek et al. (2024) Fermian guesstimation can boost the wisdom-of-the-inner-crowd. https://pmc.ncbi.nlm.nih.gov/articles/PMC10904748/
- [V] Fujisaki, Yang, Ueda (2023) On an effective and efficient method for exploiting the wisdom of the inner crowd. https://pmc.ncbi.nlm.nih.gov/articles/PMC9984468/
- [V] Fujisaki et al. (2025) An ensemble method utilising multiple thinking styles. https://pmc.ncbi.nlm.nih.gov/articles/PMC12371095/
- [V] Van de Calseyde and Efendic (2025) Disagreeing perspectives enhance inner-crowd wisdom for difficult questions. https://pmc.ncbi.nlm.nih.gov/articles/PMC13428925/
- [V] Authors not recorded (2026) Two out of three ain't bad (face matching). https://pmc.ncbi.nlm.nih.gov/articles/PMC13675558/
- [V] Ariely et al. (2000) Effects of averaging subjective probability estimates between and within judges. https://doi.org/10.1037/1076-898X.6.2.130
- [V] White and Antonakis (2013) Does dialectical bootstrapping work? (postprint + supplement). https://doi.org/10.1177/0956797612449174
- [V] OSF preprint (2026) From inner diversity to outer crowds (abstract). https://osf.io/preprints/psyarxiv/rxgzc_v1
- [V] OSF preprint (2026) When one measure hides multiple mechanisms (abstract). https://osf.io/preprints/psyarxiv/e9qn6_v7
- [M] Herzog and Hertwig (2009) The wisdom of many in one mind. https://doi.org/10.1111/j.1467-9280.2009.02271.x
- [M] Herzog and Hertwig (2014) Think twice and then. https://doi.org/10.1037/a0034054
- [M] Rauhut and Lorenz (2011) The wisdom of crowds in one mind. https://doi.org/10.1016/j.jmp.2010.12.003
- [M] van Dolder and van den Assem (2018) The wisdom of the inner crowd in three large natural experiments. https://doi.org/10.1038/s41562-017-0247-6
- [M] Litvinova, Herzog, Kall, Hertwig (2019/2020) Confidence judgments. https://doi.org/10.31234/osf.io/ngweh
- [M] Page (2007) diversity prediction theorem (as used in a11, a20, b25).

### LLM studies

- [V] Wang et al. (2023) Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171
- [V] Li et al. (2024) More agents is all you need. https://arxiv.org/abs/2402.05120
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Schoenegger, Tuminauskaite, Park, Tetlock (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Kim, Garg, Peng, Garg (2025) Correlated errors in large language models. https://arxiv.org/abs/2506.07962
- [V] Halawi, Zhang, Wang, Steinhardt (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563
- [V] Naik et al. (2023/2024) Diversity of thought improves reasoning abilities of LLMs (DIV-SE). https://arxiv.org/abs/2310.07088
- [V] Lou and Sun (2024) Anchoring bias in large language models. https://arxiv.org/abs/2412.06593
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs. https://arxiv.org/abs/2403.00811
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Zhang et al. (2025) Verbalized Sampling. https://arxiv.org/abs/2510.01171
- [V] Li et al. (2025) Rethinking Mixture-of-Agents (Self-MoA). https://arxiv.org/abs/2502.00674
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Du et al. (2023) Multiagent debate. https://arxiv.org/abs/2305.14325
- [V] Renze and Guven (2024) Effect of sampling temperature on problem solving. https://arxiv.org/abs/2402.05201
- [V] Arora et al. (2022) Ask Me Anything. https://arxiv.org/abs/2210.02441
- [V] Paleka et al. (2024) Consistency checks for language model forecasters. https://arxiv.org/abs/2412.18544
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692
- [V] Yu et al. (2026) Diversity combining for multi-path LLM reasoning. https://arxiv.org/abs/2609.38829
- [V] Nguyen, Gupta, Le (2026) Think more or read more? https://arxiv.org/abs/2610.23246
- [V] Nitarach (2026) Model capability dominates (AIMO 3). https://arxiv.org/abs/2603.27844
- [V] Liu (2026) Two calls, two moments. https://arxiv.org/abs/2605.03379
- [V] Sharma and Chopra (2025) The sequential edge. https://arxiv.org/abs/2511.02309
- [V] Wang et al. (2025/2026) Rethinking inference-time scaling. https://arxiv.org/abs/2504.14047
- [V] Zeng et al. (2025) Revisiting the test-time scaling of o1-like models. https://arxiv.org/abs/2502.12215
- [V] Loo (2025/2026) Self-consistency is losing its edge. https://arxiv.org/abs/2511.00751
- [V] Kohli (2026) Nine judges, two effective votes. https://arxiv.org/abs/2605.29800
- [V] Ding (2026) When LLMs agree, are they right? https://arxiv.org/abs/2607.08065
- [V] Wang, Hong, Bagci (2026) A decodability criterion. https://arxiv.org/abs/2608.17124
- [V] Sakai, Song, Larson (2026) When does delegation beat majority? https://arxiv.org/abs/2606.08098
- [V] Verma (2026) Try again, don't look back. https://arxiv.org/abs/2607.26117
- [V] Ferreira, Liu, Zheng (2026) Beyond symmetric agents. https://arxiv.org/abs/2609.35875
- [V] Bilal et al. (2026) Refining over resampling. https://arxiv.org/abs/2608.05643
- [V] Harshavardhan (2026) Self-anchoring calibration drift. https://arxiv.org/abs/2603.01239
- [M] Jaworski and Alam (2026) Synthetic Consensus (Crossref abstract; SSRN 403). https://doi.org/10.2139/ssrn.7382959

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 13 established claims: 10 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A17.02-K02** (reworded: the sources support less). Numbers match, but 1.1-1.5 is the equivalent number of people for the whole averaged set (lambda 0.11/0.32 is the second guess's worth), and the 'field data say barely better than two different people' clause is not in any opened source (Gomilsek only shows asking someone else wins in all 6 conditions, +8.3 points). Corrected claim: Averaging two guesses from the same person is worth only about 1.1 to 1.3 independent people (Vul and Pashler: lambda 0.11 immediate, 0.32 delayed, i.e. a second guess is worth 11-32% of a second person's guess; 1.04-1.07 in a replication by Hourihan and Benjamin); even an ensemble of five different thinking styles reaches only about 1.5 people (Fujisaki et al. 2025); asking another person beat re-asking oneself in all six conditions of Gomilsek et al. 2024.
- **A17.02-K18** (reworded: the sources support less). Numbers (93% of 980 settings; 23 models, 1.6x wall-clock, 3.4x tokens) match the abstracts, but the final sentence 'Only the original debate paper lacked this control' is a sweeping universal no source supports (Du et al. did include a 3-agent majority baseline, just not budget-matched); '9-sample' not on the abstract page. Corrected claim: Debate between copies of one model beats a single agent but not equal-budget voting: self-consistency matched or beat debate in 93 percent of 980 matched settings (5 open models, 4 tasks), and a 23-model study found debate tied or lost to matched-budget sampling/voting at 1.6x wall-clock and 3.4x tokens. The original debate paper (Du et al.) compared only against a 3-agent majority baseline that was not budget-matched; Huang et al. found debate underperforms self-consistency at equal response counts.
- **A17.02-K24** (reworded: the sources support less). Yu (corr 0.45-0.59/0.60, ceiling 1.71-2.21) and Kohli (n_eff 2.18) check out, but 'so a same-model crowd cannot be better' is an inference from a different-model panel on NLI, not shown by any source; Nguyen rho range 0.35-0.77 and 1/rho cap not seen in abstract (full text pending). Corrected claim: Same-model votes are worth about 1.3 to 2.9 independent votes, whatever the sample count. Two independent measurements on small open models agree: correctness correlation 0.45 to 0.60 on GSM8K gives a ceiling of 1.7 to 2.2 effective votes, reached by K=8 to 16 (Yu et al. 2026); error correlation 0.35 to 0.77 across five models and four tasks gives a cap of 1/rho (Nguyen et al. 2026). Nine different frontier models gave only about 2.2 effective votes on NLI (Kohli 2026), which suggests, but does not show, that a same-model crowd is no better.
- **A17.02-K09** (now single-source: only one opened source, code check).
