# Limits of deliberate practice: deep document

*Subfield A10.05. Built from evidence_a.jsonl (a01-a26), evidence_b.jsonl (b01-b27), evidence_c.jsonl (c01-c27), evidence_d.jsonl (d01-d18), claims.jsonl (K01-K25) and critique.md in this folder. Ids like b06 point to evidence lines; K-ids point to claims. Publication version matters: the 2014 meta-analysis has an original set of numbers and a 2018 corrigendum set. Both are given and never mixed in one row.*

## 1. What it is

Deliberate practice (DP) is a theory of how people reach expert performance. It says experts get there through long, effortful practice that is designed to improve one weak part, has a clear goal, gives immediate feedback, and is not fun in itself (a01, a19). "Limits of deliberate practice" is the body of work that asks one question: how much of the difference in skill between people do practice hours actually explain?

The short answer from the main meta-analyses:

- Across 88 studies, practice hours explain about 12% of skill variance as first published, 14% after the 2018 corrigendum (b01, a10).
- The share depends on domain. Games, music and sports are well above education and professions (b02).
- The share depends on how regular the domain is, and on how hours and skill are measured (b03, b04).
- Among elite athletes the share is about 1% (b06).
- Chess masters needed anywhere from about 3,000 to about 24,000 hours (d12).
- The founding violin study did not replicate on its core claim (b15).
- The theory's author says the meta-analyses used the wrong definition. A reanalysis with his definition gives 29%, or 61% after correction (b22). This dispute is not settled.

Why it matters for our agent. We build one language-model agent that thinks well through a scaffold, not through training. The practice literature gives three useful warnings:

1. More repetition does not fix everything. Returns diminish, and at the top they nearly stop.
2. What counts is targeted practice with a reliable error signal, not just more hours. In LLM terms: a retry with an outside check, not a retry with the model's own opinion.
3. Practice on one task family does not reliably carry to another.

No study found tests Ericsson-style limits directly on an LLM (K18). Everything in section 6 is analogy, and is labelled so.

## 2. History and theories in depth

### 2.1 The founding paper (1993)

Ericsson, Krampe and Tesch-Romer (1993) proposed that expert performance is the end product of long efforts to improve (a01). They said the framework gives a "sufficient account of the major facts about the nature and scarcity of exceptional performance". They rejected a large role for innate talent except body size. The paper had over 9,000 citations by 2018.

Study 1, West Berlin music academy violinists (a02). N=30: three groups of 10 (best, good, music-teacher track).
- Practice alone accumulated by age 18: best 7,410 h, good 5,301 h, F(1,27)=4.59, p<.05.
- Best and good together vs teachers (3,420 h): F(1,27)=11.86, p<.01.
- Diary week: 24.3 h for best and good vs 9.3 h for teachers, F(1,27)=44.05.
- Sessions in diaries were 1 to 1.5 h.
- The authors claimed "complete correspondence" between skill and accumulated practice alone.

Study 2, pianists (a03). Experts 7,606 h by age 18 vs amateurs 1,606 h, F(1,22)=26.29, p<.001. The paper also frames improvement as a power law of practice when feedback is adequate. Without adequate feedback, improvement is minimal even for motivated people.

Daily limits (a04). The theory says effortful practice is bounded by recovery. Cited motor-learning work shows almost no benefit beyond 4 h a day and reduced benefit beyond 2 h.

Weaknesses of the original design: retrospective interviews, small groups, extreme-group contrast (best vs teacher track), interviewers probably not blind, two ANOVAs that each dropped one group but kept full degrees of freedom, no variances reported (a02). Wording also moved between "necessary" and "sufficient" (a01).

### 2.2 Popular claims and the shift to "necessary but not sufficient"

The 1993 work was popularised as a "10,000 hour rule". The scientific critics did not argue that practice is useless. They argued it is not sufficient. Campitelli and Gobet (2011, "necessary but not sufficient") are the main source. Their chess data come from Argentine players (d12, 2008 conference note on the same data): N=104, DP explained 34% of rating variance; mean hours to master 11,053; fastest 3,016, slowest 23,608 (about 8 times); some players with over 25,000 h never reached master; starting age predicted rating after controlling for hours; group practice predicted skill better than solitary practice. The 2011 journal text could not be opened (403). The press-release wording "about 3,000 vs about 30,000 h" (b24) is a rounded form; use 3,016 and 23,608 h from d12.

### 2.3 The reanalysis wave (2014)

Hambrick et al. (2014) reanalysed 6 chess studies and 8 music studies with correction for measurement error (a05, a08, b09, b10). Practice explained about a third of reliable variance: chess 34.0%, music 29.9%. They also showed overlap between skill groups (b11) and competing factors: working memory (b12), intelligence, starting age, and the Polgar sisters (a23).

The same year Macnamara, Hambrick and Oswald published the 88-study meta-analysis (b01-b05). Platz et al. (2014) answered with a music-only meta-analysis giving a larger corrected r (a16, b14). Hambrick et al. replied (a17, b13). Ericsson (2014) rejected 87 of the 88 studies as not meeting his definition (b21). A lot of the later literature is this definitional fight.

### 2.4 Domain-specific meta-analyses and the replication (2016-2019)

- Sports: Macnamara, Moreau and Hambrick (2016): 18% overall, 1% at elite level (a12, b06). Ericsson (2016) replied that summing any type of sport activity is the wrong measure (a13).
- Chess and cognition: Burgoyne et al. (2016) found chess skill relates to cognitive ability, r=.24 (b23).
- Violin replication: Macnamara and Maitra (2019), preregistered, double-blind, results-blind (b15).
- Ericsson and Harwell (2019): reanalysis keeping 14 of the 88 studies (a18, b22).
- Hambrick, Macnamara and Oswald (2020): "Is the deliberate practice view defensible?" (a10, b21). They document shifting definitions of DP over 25 years.
- Ericsson (2021) response: five criteria define DP; Macnamara et al. broadened it to lectures, solo study and coach-led group activity (a19).

### 2.5 Genetics and other competing factors (2014-2024)

Twin studies test a direct prediction: if practice builds ability, genetic effects should shrink with more practice. Mosing et al. (2014) found practice-ability links run mostly through shared genes (b18). Mosing et al. (2024) tested the prediction directly and found it failed (a20, b19). Early start of training links to adult skill mostly through lifetime practice and family factors, little through a sensitive period (b20).

### 2.6 Where the field stands now

- Nobody serious denies practice matters. The dispute is its size and what counts as practice.
- Independent outside work is thin. Debatin et al. (2023), independent of both camps, find the payoff of structured practice depends on individualization (d14). No neutral re-run of the 88-study set was found (d16).
- A 2026 study of AI-assisted practice in conservatory students (a24) is observational and self-report only.

## 3. Core findings with exact numbers

Version rule: "2014 orig" is the first published text; "2018 corr" is the corrigendum quoted in Hambrick et al. 2020 (a10). Do not compare across versions.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Overall DP share of variance, 88 studies | 2014 orig: r=.35, CI .30-.39, 12% (CI 9-15%), 88% unexplained; 88 articles, 111 samples, 157 effects, N=11,135; I2=84.9; 10 of 157 effects negative. 2018 corr: 14% | b01, a10 | Established (K01) |
| Domain split | 2014 orig: games 26% (r=.51), music 21% (.46), sports 18% (.42), education 4% (.21), professions <1% (.05, p=.62); Q(4)=49.09. 2018 corr: 24 / 23 / 20 / 5 / 1. Effects: music 28, sports 60, education 51, professions 7, games 11 | b02, a10 | Established |
| Predictability of the domain | 2014 orig: high 24% (r=.49), moderate 12% (.35), low 4% (.21); Q(1)=20.49. Coder-rated, confounded with domain | b03 | Single-source (K02) |
| Practice measurement method | Interview 20% (r=.45), questionnaire 12% (.34), log 5% (.22); Q(2)=16.19 | b04 | Established (K04) |
| Performance measurement method | Group membership 26% (.51), lab task 14% (.37), expert ratings 9% (.30), standardized objective score 8% (.28) | b04 | Established (K04) |
| Solitary-only DP and publication bias | Solitary-only 11% overall (games 23, music 23, sports 22, education 3); no missing effects by trim-and-fill | b05 | Established |
| Sports overall | r=.43, CI .35-.50, 18% (CI 12-25%); 52 samples, 63 effects, N=2,765. 2018 corr sports 20% | b06, a10 | Established |
| Sports by skill level | Subelite r=.44; mixed r=.54 (29%); elite r=.11, p=.50, 1% (6 effects, N=228). Adding one excluded effect: r=.28 (8%), still n.s. | b06 | Established (K03); range restriction doubt |
| Sports moderators | Team 17% vs individual 19%; open 17% vs closed 19%; externally paced 17% vs internally paced 41% (r=.64); expert ratings 2% (r=.14); solitary-only r=.47, 22% | b07 | Single-source |
| Sports: earlier start | Higher-skill athletes started 0.11 y later (CI -.41 to .62, p=.68; 24 effects, N=1,477). Unpublished studies r=.33 (11%) vs published larger; Q(1)=4.23, p=.04 | b08 | Single-source |
| Chess, DP share | 6 studies, pooled N=533, uncorrected r=.33 (CI .25-.40), corrected .39; average 34.0% explained (avg corrected r=.57, weighted .49). At reliability .60, 54.7% unexplained; at .90, 30.2% explained | a05, b09 | Established (K09) |
| Chess spread | Masters 832 to 24,284 h; 5 of 16 masters (31.3%) below expert-group mean; 8 of 31 intermediates (25.8%) above expert mean. Argentine sample N=104: 3,016 to 23,608 h, mean 11,053 h, 34% | b11, a06, d12 | Established |
| Music, DP share | Hambrick: 8 studies, 29.9% (range 26.3% at reliability .90 to 39.6% at .60). Platz: 13 studies, N=788, corrected r=.61, CI .54-.67 (37%) | b10, a16, b14 | Contested (K08) |
| Working memory beyond practice | Sight-reading N=57: practice 45.1%, working memory adds 7.4%; r(practice, WM)=.003; no interaction | a07, b12 | Established (K10) |
| Chess and cognitive ability | 19 studies, 26 samples, r=.24 (CI .18-.30). Gf youth .32 vs adult .11 (p=.071); unranked .32 vs ranked .14. Provisional (corrigendum unread) | b23, a22 | Established, provisional |
| Elite child chess | Elite n=23: IQ vs rating r=-.51 (p=.014); practice vs rating r=.46 (p=.028); practice model 60% of rating variance | a21 | Single-source |
| Violin replication, core claim | Best 8,224 h (CI 6,400-10,048), good 9,844 h, less accomplished 4,558 h by age 18; best vs good t24=-0.93, p=.364, d=-0.38; good vs less accomplished t16.57=3.26, p=.005, d=1.33; group eta2=.26 (CI .03-.44) vs original 48% | b15, a14 | Established (K05) |
| Violin: teacher-designed practice | Best 6,251 h, good 6,821 h, less 2,799 h; eta2=.23, p=.005; best vs good d=-0.15; correlates r=.72 with practice alone | a15, b16 | Established |
| Violin: weekly hours | Best 22.69 h, good 30.65 h, less 9.58 h (best vs good p=.024, d=-1.03). Weekly estimates exceeded diaries (F1,35=19.62, p<.001) with no group difference | b16, b17 | Single-source (K06) |
| Definition dispute | Ericsson and Harwell: 14 of 88 studies; r=.54 (CI .44-.63), 29%; objective .49, relative .65; corrected r=.78 (61%). Critics: 7 of 8 DP effects came from studies Ericsson rejected earlier | a18, b22, b21 | Contested (K07) |
| Reliability sensitivity of the corrected share | From r=.56: .60/.60 gives corrected r=.93 (87.1%); .80/.80 gives .70 (49.0%); .90/.90 gives .62 (38.7%) | a11 | Established (arithmetic) |
| Twins, 2014 | 10,500 Swedish twins; practice-ability rs .18 to .36; practice heritable 40-70%; identical twins differing in practice did not differ in ability | b18 | Established (abstract read) |
| Twins, 2024 | 6,471 twins (1,302 complete pairs), mean age 40.7; about 50% genetic, 25% shared, 25% residual; practice-ability r=.36; players vs non-players d=.77 / .78; genetic variance flat, relative heritability rose with practice | a20, b19 | Established (K11) |
| Early start | After adjusting for practice, onset age predicts pitch discrimination only (beta -0.07 musicians, -0.30 twins); not rhythm | b20 | Single-source |
| Far transfer | Music instruction: 0.25 SD passive controls (k=64) vs 0.03 SD active (k=54). WM training: 0.18 vs 0.05 SD. Chess: one active study 0.10 SD | b25 | Single-source (K12) |
| Junior vs senior elite sport | 71 reports, 262 samples, 685 effects, N=9,241. World-class adults: more multi-sport practice, later start, less main-sport practice (abs d .23-.50); juniors the opposite (abs d .23-.61) | b26 | Single-source (K13), abstract read |
| Carlsen top-ten check | 2881 vs mean 2780.6 of next ten, t(9)=-19.38; 18 years practice vs 24.6, t(9)=2.83, p<.05; years not hours | d13 | Single-source, opinion |
| Individualization | N=178 chess: structured practice adds R2=.024 (rs=.19); interaction with didactic capital R2=.43; effect over 3 times higher at +1 SD | d14 | Single-source (K24) |
| Ability remains with equal exposure | Rubik's cube N=79: Gf predicted skill; WM and personality did not | d15 | Single-source (K25) |
| Polgar sisters | Peak 2735 after about 59,904 h vs 2577 after about 79,248 h; case data | b11, a23 | Anecdote |

## 4. Mechanisms and models

This section turns the literature into things an engineer can build or measure.

### 4.1 Variance-share model and disattenuation

The 2014 analyses compute r between accumulated hours and a skill score, then square it. Correction for unreliability (a08):

    true_r = observed_r / sqrt(rel_x * rel_y)

Practice reliability was assumed .80; chess rating reliability .91 (a08). Retrospective versus diary agreement ranged r=.60 to .98 across studies (a08). Because reliability is assumed, the corrected share swings: from r=.56, reliabilities .60/.60 give 87%, .80/.80 give 49%, .90/.90 give 39% (a11). Engineer's rule: any "X explains Y% of variance" claim needs a stated reliability. In our evals, log tokens and calls (reliability near 1) rather than self-reported effort (K06).

### 4.2 Moderators as a regression

The meta-analysis is a random-effects model with moderators: domain, predictability, practice-measure and performance-measure (b02-b04). The big heterogeneity (I2=84.9) means one pooled number is a poor summary. Implementation lesson: report a gain per item class, never one pooled gain.

### 4.3 Threshold, then plateau

Violin replication (b15): practice separates the less accomplished from the good (d=1.33) but not the good from the best (d=-0.38). Sports: elite r=.11 vs subelite .44 (b06). Chess: some masters had less practice than the experts' mean (b11). A simple model that fits: skill = f(practice) with steep early slope, saturating, then other factors (ability, starting age, task choice, teaching quality) dominate. Range restriction can make a plateau look flatter than it is (critique.md), so treat the plateau as likely but not proven.

### 4.4 Quality of practice: individualization and targeting

Debatin et al. (d14): skill gain = a * hours + b * hours * teaching_quality. The interaction lifted R2 from .024 to .43. Macnamara and Maitra (a15) found teacher-designed practice explained no more variance than practice alone, so the data on this are mixed. Both are single samples.

LLM analogue of targeting: STAT (a25) uses a stronger teacher to find the student's missing skills, then builds training data for them (gains up to 7.5% on MATH). APT (a26) trains on the model's own error cases. Both need a feedback source.

### 4.5 Feedback signal as the key variable

In the theory, power-law improvement requires feedback; without it improvement is minimal (a03). In LLMs the same split appears (d01): with oracle labels GSM8K rises 75.9 to 95.5 (GPT-3.5); without oracle it drifts 75.9 to 74.7 over 5 calls. The implementable form: a retry operator is gated on a signal produced by code or an external checker, never by the same model's opinion.

### 4.6 Dose-response curves for LLM loops

Three measured shapes (all analogies to "hours"):
- Sequential self-repair: flat or negative without an oracle (d01, d02, d05).
- Sequential extra thinking: rises then flattens near six times more "Wait" (d09).
- Parallel resampling with a verifier: coverage rises log-linearly, 15.9% to 56% from 1 to 250 samples (d07).

A scaffold should size loop length from a measured curve per task class, with a hard cap.

### 4.7 Difficulty routing

Snell et al. (d08): five difficulty bins from the base model's own pass rate; allocate compute per bin. Compute-optimal allocation matched best-of-N with about 4x less compute. On the hardest bin no method progressed. Implementable: estimate difficulty from a few cheap samples; easy gets one pass, medium gets resampling with a verifier, hardest gets stop or escalate. This is the LLM version of the elite-plateau finding and of domain predictability, but difficulty here is model-estimated, not human-rated (K22).

### 4.8 Practice-induced narrowing

RLVR-trained models win at small k but base models match or beat them at large k (d10, c16). Self-training is bounded by the data distribution (c11). Recursive synthetic data loses distribution tails (c17). Adversarial policies beat superhuman Go AIs over 97% of the time (c21). Practice (training volume) lifts the average and can leave holes. Implementable: track pass@k as well as pass@1 for any scaffold.

## 5. What holds up

### 5.1 Replications and meta-analyses

Holds:
- Practice hours predict skill in games, music and sports at moderate to large size, and weakly in education and professions. The order is stable across the original and corrigendum values (K01).
- Measurement method changes the number: the log method gives 5% and the interview 20% (b04). Extreme-group contrasts inflate (b04, a03).
- At the elite level, hours separate performers weakly: elite sports 1% (b06); violin best vs good not replicated (b15); chess masters' hours overlap those of lower groups (b11).
- Practice does not remove genetic influence on musical ability; heritability rose with practice (a20).
- Ability variables add beyond practice: working memory 7.4% (a07), chess intelligence r=.24 (b23), fluid intelligence in cube solving (d15).

Fails or weakened:
- The 1993 claim of "complete correspondence" between practice and skill: replication explained 26% against 48% in the original, and best vs good d=-0.38 (b15, b17). The replication effect matches the meta-analytic music average (23%), so the original looks like the outlier.
- The prediction that practice shrinks heritability (a20).
- The claim that earlier start separates higher-skill athletes: 0.11 y later, n.s. (b08). Early start in music works through lifetime practice and family factors (b20).
- Intense equal training giving equal results: Polgar sisters peaked at 2735 vs 2577 (a23).

Contested:
- How large the effect is under the original definition: 29% (61% corrected) vs 14% (b22 vs b21). The dispute comes from which of 88 studies count and from assumed reliability (K07).
- Music: corrected r=.61 (37%) vs 29.9% (K08). Different study sets and correction rules. Four studies carry 50% of the Platz weight (b14).
- Whether to report r or r-squared (b13, b14).

### 5.2 Moderators that matter

Domain regularity (24% / 12% / 4%) (b03); how practice is measured (b04); how skill is scored (b04, b07); skill level in the sample (b06); age and level for cognitive ability (youth r=.32, adult .11 for Gf) (b23); published vs unpublished (11% for unpublished sports) (b08).

### 5.3 Interventions that worked and did not

Worked (human):
- Practice with feedback and teacher design separates the lowest tier from the others (b15, a15).
- Individualized teaching raises the payoff of structured practice (d14, single sample).

Did not work (human):
- Far transfer against active controls: 0.03 SD for music, 0.05 SD for working-memory training (b25).
- Summing more hours at the top (b06).

Worked (LLM analogues, see section 6): external-signal retry; verified resampling; difficulty routing; targeted training on weak skills.
Did not work (LLM): intrinsic self-correction; extra self-repair rounds at equal budget; extended thinking beyond a knee.

### 5.4 Weak spots in the evidence

Hours are mostly retrospective self-reports with assumed reliability. The authors on both sides are interested parties. Few independent re-analyses exist (d16). Range restriction may depress elite correlations. Twin studies use auditory discrimination, not performance (a20). Several key items were seen only at abstract level: b18, b26, b27, a13, a26 and the corrigendum per-moderator values (d17, d18).

## 6. Language models

No study found tests the limits of deliberate practice directly on an LLM (K18). What exists is a set of measured results on practice-like loops (retry, repair, resample, train on errors). They map onto the human findings as follows. Everything here is an analogy.

### 6.1 Practice without an outside signal does not help

- Huang et al. 2023, full text (d01): intrinsic self-correction. GPT-3.5 on GSM8K 75.9 to 75.1 (3 calls) to 74.7 (5 calls). CommonSenseQA 75.8 to 38.1 to 41.8. GPT-4 CommonSenseQA 82.0 to 79.5 to 80.0; HotpotQA 49 to 49 to 43. With oracle labels: GSM8K 75.9 to 95.5 (GPT-3.5), 84.3 to 97.5 (GPT-4); HotpotQA 26.0 to 49.0 and 29.0 to 59.0. Multi-agent debate is no better than self-consistency at equal responses.
- Kamoi et al. 2024 survey (d06): no prior work shows successful self-correction with prompted LLM feedback on general tasks except tasks exceptionally suited; works where reliable external feedback exists; fine-tuning enables it.
- Stechly et al. 2023 (c05): GPT-4 is poor at verifying its own graph-colouring answers; gains come from an external verifier choosing among completions (abstract level).
- Reflexion full text (d04): HumanEval pass@1 91% vs 80% for GPT-4. On the 50 hardest HumanEval-Rust problems: full 60%, without test generation 52%, without the written reflection no gain over base. On MBPP Python it falls below base (80%) because of false-positive tests. Not budget-matched.

### 6.2 Repair versus resampling at equal budget

- Olausson et al. 2023, full text (d02): CodeLlama-13b, GPT-3.5, GPT-4 on HumanEval and APPS. At equal sample budget repair is often no better than fresh sampling, especially at small budgets. More initial programs help consistently; more repairs give marginal or negative gains. Human feedback to GPT-4 beats self-feedback (c04).
- Self-Refine full text (d03): per-iteration gains shrink. Code optimization 22.0 to 28.8 after 3 iterations; Sentiment Reversal 33.9 to 36.8; Constrained Generation 29.0 to 49.7. With no or generic feedback one task fell 56.4 to 48.0. Compared to single-pass output, not to a sampling baseline at equal tokens.
- SCoRe (d05): base model on MATH attempt 1 52.6%, attempt 2 41.4% (-11.2). STaR 55.4 to 41.2. Pair-SFT 52.4 to 54.2. Correct-to-incorrect flips 15.8% (base), 19.6% (STaR). RL with a shaped reward: +15.6% MATH, +9.1% HumanEval over base self-correction. This needs weight training.

### 6.3 Dose-response and the elite tail

- Repeated sampling (d07): coverage rises log-linearly; SWE-bench Lite 15.9% (1 sample) to 56% (250 samples). Needs a verifier; without one majority vote and reward models plateau early.
- Budget forcing (d09): AIME24 50% to 57%, flattening near six times more "Wait". AIME24 has 30 problems, so +7 points is about 2 problems.
- Difficulty routing (d08): about 4x less compute than best-of-N at equal accuracy on MATH (PaLM 2-S*). Hardest bin: no method made meaningful progress. A small model with test-time compute beats a 14x larger model on easy and intermediate questions, not on hard ones.
- RLVR (d10): base matches or beats the trained model at large k (up to 256); coverage falls as RLVR proceeds.

### 6.4 Targeted practice and transfer

- STAT (a25): up to 7.5% on MATH; 4.6% average on AIME24/25 and AMC23; stacks on GRPO. Abstract-level.
- Huan et al. 2025 (d11): over 20 reasoning-tuned models, most math gains do not carry elsewhere. Controlled Qwen3-14B math-only: RL transfers, SFT does not (SFT drifts and forgets). This is weight training, not a scaffold, with no human-style active control.
- Voyager (c08): skills library transfers to a new world; single game (abstract level).

### 6.5 Games

Ruoss et al. (c19): 10M games, 15B data points, up to 270M parameters, Elo 2895 without search. Data volume lifts models far in a rule-bound domain, matching the high-predictability band. Adversarial policies beat KataGo over 97% (c21). Humans learned from AlphaZero concepts: 4 grandmasters improved (c20, tiny sample).

### 6.6 AI-assisted human practice

Song et al. (2026) (a24): 512 of 600 conservatory students completed three waves. AI engagement was associated with later self-regulation, which was associated with later instructor-rated performance. Associations only, no logs.

### 6.7 Reading the pattern

Across 6.1-6.3, the split is the same as in humans: practice-like loops help where a clear external signal exists (games, code with tests, verifiable math) and are flat or harmful where the signal is the model's own opinion. The knee of the curve is the LLM version of the elite plateau. Size of the knee for a given scaffold is unmeasured.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Revisions only from an external signal [E].** G2 and G1 already say this. This subfield adds more evidence: intrinsic loops flat or negative (GSM8K 75.9 to 74.7; SCoRe base 52.6 to 41.4); oracle loops large (95.5). Part: G2, S5. Evidence: d01, d05, d06, c05, K15. Action: keep S5 revisions tied to code-located failing output; cite K15 as extra support.
2. **Budget-matched reporting for every loop [E].** Every retry or repair result is reported against best-of-N with the same number of calls. Part: G7. Evidence: d02, d01, K21. Action: add the matched resampling arm to the standing bench protocol.
3. **Cap the sequential loop; prefer parallel samples [E].** S5 at most 2 rounds is already in the schema; the dose-response evidence supports it. Part: S5, G11. Evidence: d02, d09, d07, K20 (K20 itself is [C] on the exact knee). Action: no change to the 2-round cap; do not extend it.
4. **No promise of far transfer, so lessons are scoped by class [E for human, S for LLM].** Part: M (lessons trusted only after helping on two different problems, already in schema). Evidence: b25, d11, K12, K23. Action: keep the two-problem trust rule; do not let class-A lessons auto-apply to class B.
5. **Our own evals use continuous scores and logged effort [E].** Avoid extreme-group contrasts and self-reported effort. Part: eval protocol, no schema change. Evidence: b04, a02, K04.
6. **Report gains per item class, never one pooled number [E].** Heterogeneity is huge in the human data (I2=84.9). Part: G7 and the class record in M. Evidence: b01-b03.
7. **Quote the right version of published numbers [E].** Use the 2018 corrigendum values (14 / 24 / 23 / 20 / 5 / 1) in schema notes and say that the original was 12 / 26 / 21 / 18 / 4 / <1. Evidence: K01, a10.

### Test first (not yet established; see UNKNOWNS.md)

1. **Difficulty routing in S0 [S].** Estimate difficulty from a few cheap samples and route (easy: one pass; medium: resample with check; hardest: stop or escalate). Part: S0, G12. Evidence: d08, b03, K02, K22. G12 already says spend by difficulty; the new part is the stop/escalate rule for the hardest bin and the predictability tag.
2. **Targeted retry beats generic retry [S].** A retry that names the failing part and uses an outside check, against a generic "try again". Part: O, S5. Evidence: d14, a15, a25, c04, K14, K24. Contested in humans (a15 vs d14).
3. **Plateau stopping rule [C].** Stop adding same-type samples when the gain per extra sample falls below a threshold, per class. Part: S6, G11, class record. Evidence: b06, d07, d09, d10, K03, K20.
4. **Early gains mispredict final level [S].** Pick strategies on final-budget quality, not early-iteration gains. Part: G7. Evidence: b26, d03, d01, K13. Only indirect.
5. **Ability gate: gain grows with base model strength [S].** Part: S0 (capacity limits stay). Evidence: d15, a07, b23, K10, K25.
6. **Pass@k check against the base [C].** Part: G7, G4. Evidence: d10, c16, K16.
7. **Lesson transfer across task families with active control [S].** Part: M. Evidence: d11, b25, K23.

## 8. Concrete tests on our bench

All arms use equal tokens. Use items with an executable check where possible. Log tokens and calls, not self-reports. Report per item class with intervals.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Dose-response and knee | One task family with a code check (ARC-style or code puzzles), 100+ items | k = 1, 2, 3, 5, 8 retries: (a) repair with check output; (b) fresh sampling with the same total calls | Pass rate at each k; knee where marginal gain per extra call drops below 1 point | Repair no better than fresh sampling after k=2 (K21); knee near 2-3 |
| T2 Intrinsic vs external signal | Same items | (a) retry on model's own critique; (b) retry on executable failing output; (c) fresh sample | Net pass rate; right-to-wrong flips | (a) flat or negative; (b) positive over (c) at small k |
| T3 Difficulty routing | Items binned by 8 cheap samples into 5 bins | (a) fixed loop; (b) routed loop (light / resample / stop) | Pass rate at equal total tokens; tokens saved at equal pass rate | Same pass rate with about 2-4x fewer tokens (d08); no gain on the hardest bin |
| T4 Predictability tag | Items split into rule-bound (code, arithmetic, grid) and open (essay, ideation, ambiguous) | Loop vs plain at equal tokens, per tag | Gain per tag | Larger loop gain in rule-bound items (K02) |
| T5 Hard-tail best-of-N | Hardest bin from T3 | best-of-N at N=1, 4, 16, 64 vs scaffold | pass@N and pass@1 | Curve flat at the top; scaffold adds nothing on the hardest items |
| T6 Targeted vs generic | Items with a localised failing test | (a) retry naming failing test and line; (b) generic "improve this" retry | Pass rate | (a) beats (b) (K24); small effect |
| T7 Transfer | Two task families A, B | Lessons from A (memory on) vs no lessons vs lessons from an unrelated family C (active control), run on B | Pass rate on B | Lesson from A beats none only if A and B share class; A not better than C otherwise (K12, K23) |
| T8 Ability gate | Same scaffold on a weak and a strong base model | Scaffold vs plain per model | Gain size by model | Gain smaller or flat on the strongest model; test K25 |
| T9 Early vs final | Full budget runs of scaffold variants | Rank variants at 25% budget and at 100% budget | Rank correlation | Correlation below 1; pick on full budget (K13) |
| T10 Coverage | Verifiable items | Scaffold vs base: pass@1 and pass@k, k=16 | Both metrics | Scaffold lifts pass@1; pass@k not lower than base |

## 9. What does not transfer, and why

- **Hours as the unit.** Human practice is hours of effort inside a body that recovers. An LLM has no fatigue and no between-session consolidation inside one run. The daily 4 h limit (a04) has no analogue. The unit that matters for the agent is tokens and calls, which we log exactly.
- **Learning inside the person.** DP changes the person. A prompt scaffold changes nothing in the weights. Self-improvement by weights (SCoRe, STaR, RLVR) is training, which this project does not do. The human result applies only as an analogy to loops inside one run.
- **Genetics and starting age.** Twin results (a20, b19) and early start (b20) have no agent counterpart. The nearest analogue is the base model's capability, tested in T8.
- **Retrospective recall bias.** It is a human measurement problem. Our runs are logged. The lesson survives only as a methods rule.
- **Motivation, mindset, fun.** The theory says DP is not enjoyable; classroom and mindset effects are covered by other subfields (Motivation, mindset, classroom factors). No analogue in an agent.
- **Elite range restriction.** In humans, few elite performers are sampled. Our bench can sample the hard tail directly, so the concern becomes a design choice.
- **Teacher.** A human teacher designs individual tasks. For the agent, "teacher" can be code (tests) or a stronger model; the second is cost-heavy and outside the one-agent design.
- **Far transfer against active controls.** The human null (0.03 SD) concerns children's cognitive outcomes. The LLM evidence is about weights (d11), not scaffolds. Do not read either as a ruling on lesson memory.
- **Link to parallel subfields.** Deliberate practice and Expert-novice differences cover what practice builds; Testing effect and Retrieval as consolidation cover practice mechanisms; Motivation, mindset covers affect. They are not repeated here.

## 10. Open questions

1. Is there a dose-response curve for scaffold loops at equal tokens, and where is its knee? No direct study (gap 1).
2. Does routing on task regularity (human-rated predictability) beat routing on model-estimated difficulty? Only model-estimated was found (gap 2, K22).
3. Does the 1% elite figure survive range-restriction correction? Not found (gap 3).
4. What does the full 2018 corrigendum report per moderator (practice method, performance method, predictability)? The SAGE page was blocked (403) (d17, gap 4).
5. Did the 2018 corrigendum to Burgoyne et al. change the chess intelligence figures? Elsevier page blocked (d18, gap 7).
6. Is the Campitelli and Gobet (2011) journal text consistent with the 2008 figures? The 2011 text was not retrieved (gap 8).
7. Are there neutral re-analyses of the 88-study set or the 14-study subset? None found (d16, gap 9).
8. Do early-iteration gains in agent runs mispredict final quality, as in junior versus senior sport (gap 10)? No source.
9. Does a lesson memory transfer across families against an active control (gap 6)?
10. Can an LLM scaffold detect its own plateau cheaply, without an external signal?
11. Is the difference between targeted and generic feedback real? Humans: a15 vs d14. LLM: c04, d02 point toward targeted, but only for stronger-model or human feedback.
12. The Rubik's cube coefficients (d15) were not extracted.

## 11. Sources

[V] opened (full text or page read), [M] snippet or abstract only. Where an evidence line says opened:false, the mark is [M]. Many LLM papers were first read at abstract level (c lines) and later at full-text level (d lines); those are marked [V].

Human literature
- [V] Ericsson, Krampe, Tesch-Romer (1993). https://doi.org/10.1037/0033-295X.100.3.363 (a01-a04)
- [V] Macnamara, Hambrick, Oswald (2014) meta-analysis. https://www.psychologie.uzh.ch/dam/jcr:658d39fe-2f4b-467f-9ae2-ffeb25caf2b6/McNamara.PsychSci.25.2014.pdf (b01-b05). [M] original journal record https://doi.org/10.1177/0956797614535810 (a09)
- [M] Corrigendum to Macnamara et al. 2014 (2018). https://doi.org/10.1177/0956797618769891 (d17, 403)
- [V] Macnamara, Moreau, Hambrick (2016) sports. https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf (b06-b08); https://doi.org/10.1177/1745691616635591 (a12)
- [M] Ericsson (2016) reply on sports. https://doi.org/10.1177/1745691616635600 (a13, abstract)
- [V] Macnamara and Maitra (2019) violin replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745 (b15-b17, a14, a15)
- [V] Hambrick et al. (2014) Is that all it takes? https://www.gwern.net/doc/psychology/chess/2014-hambrick.pdf (b09-b12, a05-a08, a23)
- [V] Hambrick et al. (2014) Facing facts. https://pmc.ncbi.nlm.nih.gov/articles/PMC4101876 (b13, a17)
- [M] Hambrick et al. (2014) reply to Ericsson. https://researchonline.lse.ac.uk/id/eprint/102315 (b27)
- [V] Platz et al. (2014) music meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC4073287 (b14, a16)
- [V] Hambrick, Macnamara, Oswald (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852 (b21, a10, a11, d16)
- [V] Ericsson and Harwell (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6824411 (b22, a18)
- [V] Ericsson (2021) response. https://doi.org/10.1007/s00426-020-01368-3 (a19)
- [V] Burgoyne et al. (2016) chess cognition. https://www.psychologie.uzh.ch/dam/jcr:4b13cd49-3e58-409f-988e-1e73693e1e0b/Burgoyne.Intelligence.2016.pdf (b23, a22)
- [M] Corrigendum to Burgoyne et al. https://doi.org/10.1016/j.intell.2018.08.004 (d18, 403)
- [V] Bilalic, McLeod, Gobet (2007). https://doi.org/10.1016/j.intell.2006.11.002 (a21)
- [M] Campitelli and Gobet (2011) press release. https://www.psychologicalscience.org/news/releases/deliberate-practice-necessary-but-not-sufficient.html (b24)
- [V] Campitelli and Gobet (2008) CogSci note. http://bura.brunel.ac.uk/bitstream/2438/2120/1/CogSci-2008-deliberate-practice.pdf (d12)
- [V] Gobet and Ereku (2014) Carlsen. https://doi.org/10.3389/fpsyg.2014.00878 (d13)
- [M] Mosing et al. (2014) twins. https://pubmed.ncbi.nlm.nih.gov/25079217/ (b18, abstract)
- [V] Mosing et al. (2024) twins. https://pmc.ncbi.nlm.nih.gov/articles/PMC11433073 (b19, a20)
- [V] Mosing et al. (2021) early start. https://pmc.ncbi.nlm.nih.gov/articles/PMC7809336 (b20)
- [V] Sala and Gobet (2017) far transfer. https://pmc.ncbi.nlm.nih.gov/articles/PMC5724589 (b25)
- [M] Barth et al. (2022) junior vs senior. https://pmc.ncbi.nlm.nih.gov/articles/PMC9124658 (b26, abstract)
- [V] Debatin et al. (2023) individualization. https://doi.org/10.1007/s12144-021-02326-x (d14)
- [V] Meinz et al. (2023) Rubik's cube. https://doi.org/10.3390/jintelligence11010018 (d15)
- [V] Song et al. (2026) AI-assisted practice. https://doi.org/10.3389/fpsyg.2026.1929520 (a24)

LLM and AI literature
- [V] Huang et al. (2023) https://arxiv.org/abs/2310.01798 (c01, d01)
- [V] Kamoi et al. (2024) https://arxiv.org/abs/2406.01297 (c02, d06)
- [V] Kumar et al. (2024) SCoRe https://arxiv.org/abs/2409.12917 (c03, d05)
- [V] Olausson et al. (2023) https://arxiv.org/abs/2306.09896 (c04, d02)
- [M] Stechly et al. (2023) https://arxiv.org/abs/2310.12397 (c05)
- [V] Madaan et al. (2023) Self-Refine https://arxiv.org/abs/2303.17651 (c06, d03)
- [V] Shinn et al. (2023) Reflexion https://arxiv.org/abs/2303.11366 (c07, d04)
- [M] Wang et al. (2023) Voyager https://arxiv.org/abs/2305.16291 (c08)
- [M] Zelikman et al. (2022) STaR https://arxiv.org/abs/2203.14465 (c09)
- [M] An et al. (2023) LEMA https://arxiv.org/abs/2310.20689 (c10)
- [M] Chen et al. (2024) SPIN https://arxiv.org/abs/2401.01335 (c11)
- [M] Yuan et al. (2024) Self-Rewarding https://arxiv.org/abs/2401.10020 (c12)
- [M] Bai et al. (2022) Constitutional AI https://arxiv.org/abs/2212.08073 (c13)
- [M] Zhao et al. (2025) Absolute Zero https://arxiv.org/abs/2505.03335 (c14, c27)
- [M] DeepSeek-AI (2025) R1 https://arxiv.org/abs/2501.12948 (c15)
- [V] Yue et al. (2025) https://arxiv.org/abs/2504.13837 (c16, c26, d10; key sections)
- [M] Shumailov et al. (2023) https://arxiv.org/abs/2305.17493 (c17)
- [M] Villalobos et al. (2022) https://arxiv.org/abs/2211.04325 (c18)
- [M] Ruoss et al. (2024) https://arxiv.org/abs/2402.04494 (c19)
- [M] Schut et al. (2023) https://arxiv.org/abs/2310.16410 (c20)
- [M] Wang et al. (2022) https://arxiv.org/abs/2211.00241 (c21)
- [M] He et al. (2025) STAT https://arxiv.org/abs/2510.10023 (a25)
- [M] Rao et al. (2025) APT https://arxiv.org/abs/2506.03483 (a26)
- [V] Brown et al. (2024) Large Language Monkeys https://arxiv.org/abs/2407.21787 (d07)
- [V] Snell et al. (2024) https://arxiv.org/abs/2408.03314 (d08)
- [V] Muennighoff et al. (2025) s1 https://arxiv.org/abs/2501.19393 (d09, key sections)
- [V] Huan et al. (2025) https://arxiv.org/abs/2507.00432 (d11, key sections; benchmark numbers from a figure)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 8 established claims: 6 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A10.05-K03** (number corrected). Macnamara 2016 abstract (18% overall, 1% elite) and Hambrick 2020 (elite 1%) verified, but '20% after corrigendum' belongs to the sports domain of the 2014 meta-analysis (corrigendum to Macnamara, Hambrick, Oswald 2014), not to the 2016 sports meta-analysis whose overall figure is 18%; r=.11, 6 effects, N=228 could not be checked (full text not reachable). Corrected claim: At the elite level hours barely separate performers: the 2016 sports meta-analysis gives 1% of variance for elite (national level and above) athletes versus 18% overall (elite r about .11, 6 effect sizes, N=228, not significant, as reported by the researcher but not re-verified); separately, the sports domain of the 2014 multi-domain meta-analysis went from 18% as published to 20% after the 2018 corrigendum.
- **A10.05-K21** (reworded: the sources support less). Only Olausson et al. 2023 supports this; Huang 2023 does not test equal-budget repair vs resampling, and Olausson finds gains on HumanEval for Code Llama and GPT-3.5 and on APPS for GPT-4, with mixed results overall. Corrected claim: In one study (Olausson et al. 2023, Code Llama, GPT-3.5, GPT-4 on HumanEval and APPS), self-repair at matched sample budget gave modest, uneven gains: on APPS Code Llama and GPT-3.5 mostly matched or lagged their no-repair baselines while GPT-4 benefited; gains at small budgets were very marginal or absent; more initial samples helped consistently, while more repairs per sample gave marginal gains at higher budgets and sometimes lower performance at lower budgets.
- **A10.05-K11** (now single-source: only one opened source, code check).
