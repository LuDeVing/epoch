# Einstellung (set) effect: deep document

*Subfield A10.01. Sources: evidence_a.jsonl to evidence_d.jsonl, claims.jsonl (K01 to K27), critique.md in this folder. Ids (a01, b05, c11, d14) are evidence lines. Limits: the Luchins (1942) monograph was never opened. Every Luchins number comes from Binz and Schulz (2022), who re-coded percentages from the thesis tables. The first critique pass could not re-open sources (disk full, rate limits). The gap pass (evidence_d) then re-opened the Binz and Schulz text and the two Bilalic 2008 papers and confirmed their numbers; it also added the 2025-2026 LLM work on failed attempts in context. Most 2025-2026 LLM evidence is single-lab preprints.*

## 1. What it is

Einstellung means "set" or "attitude" in German. A solver uses a working method on several problems. A new problem can be solved by that method, but a shorter or better method exists. The solver keeps the old method and does not find the better one. The old method works. It is just not the best.

Three parts must be present:

1. A method that has worked before (the set).
2. A new problem where the method still works but is wasteful (the critical problem).
3. A better route that the solver finds when the set is absent (the control group does).

This differs from functional fixedness (an object is seen in only one use) and from plain error (the old method is wrong). In Einstellung the old method gives a correct answer. The loss is in efficiency, or in never finding a solution that needs a change of approach.

Why it matters for our agent: the schema fires doubt only on a signal (G1). Einstellung is the case with no failure signal, because the familiar route succeeds. So G1 has a blind spot here, and the S6 operators only fire after an impasse that may never come.

Two kinds of set matter for a language model, and the literature mixes them:

- **In-context set.** Built inside the prompt or the run by earlier same-method examples, drafts or failed attempts. This is the Luchins design. Our harness controls it.
- **Pretraining default.** A habit learned in training (a familiar pattern with a trap). Red-herring puzzles, medical trap items and counterfactual tasks test this. Our harness does not control it, only the prompt around it.

## 2. History and theories in depth

**Luchins (1942).** Water-jar studies, a doctoral thesis published as Psychological Monographs 54(6). Subjects get three jars (A, B, C) of given sizes and must measure a target amount. Training ("E") problems all solve with the long formula B - A - 2C. Critical problems (C1, C2) solve by the same formula or by a shorter one (A - C or A + C). An extinction problem can only be solved by the short method. Controls skip the training and see the critical problems straight away. Scale: over 1000 subjects across conditions (a25, second-hand). Experiment 1 as rebuilt: 310 subjects (NYU students and New York school pupils), 155 trained and 155 control (a01).

**Luchins and Luchins (1959).** Book-length follow-up. Source of the figure that 64% of trained subjects failed the extinction problem against 5% of controls (a08, second-hand; the time limit was 2.5 minutes, so part of the failure is time-out). Also reported the age finding (a06, second-hand; the age numbers were re-checked in d15).

**Ross (1952) and Luchins and Luchins (1959).** Rigidity grew with age, IQ controlled. Luchins himself reported no strong IQ or education effect (a06). So "IQ unrelated" is contested (K11).

**Saariluoma (1990).** First chess version. Four smothered-mate training problems, then a problem with a shorter solution. 10 of 12 players missed the shorter ones. In a matched-groups version only 11% of choices were optimal, against 69% when the familiar solution was disabled by moving one piece (a09, second-hand; groups of 6; original not opened).

**Wiley (1998), Frensch and Sternberg (1989).** Domain knowledge can hurt. Baseball experts did worse on remote-associates items where baseball suggested a wrong answer. Bilalic et al. argue this is inflexibility in a related domain only, not true within-domain expert inflexibility (a24).

**Lovett and Anderson (1995).** ACT-R model of strategy choice in a Luchins-like Building Sticks Task (a21).

**Bilalic, McLeod and Gobet (2008a, Cognitive Psychology).** The key modern work. Chess experts shown a position with a familiar five-move smothered mate and a shorter three-move mate stop at the familiar one. Effect about three skill standard deviations (a10, a11, b07, b08).

**Bilalic, McLeod and Gobet (2008b, Cognition).** Eye movements: players said they were looking for something better, but gaze stayed on the familiar-solution squares (a13).

**Bilalic, McLeod and Gobet (2010).** Review framing the effect as a general bias source: a recognised pattern activates a schema, the schema steers attention, and consistent information is picked up while the rest is dropped. They link it to confirmation bias and anchoring (a15, b13). This is the authors' view; the link is not tested.

**Sheridan and Reingold (2013).** Boundary conditions in chess: the familiar move must be acceptable (a16, b14, b15).

**Ellis and Reingold (2014).** Anagrams: a familiar word as the central string slows solving (a17, b16).

**Crooks and McNeil (2009).** Tested Luchins' own claim that more than one set problem adds nothing. Found it wrong (a20).

**Ninomiya, Iwata, Terai and Miwa (2024).** Extended jar task (five jars, 62 trials). A more complex trained procedure led to earlier discovery of the shortcut, against a simple "load raises rigidity" idea (a19).

**Binz and Schulz (2022).** Computational reconstruction with a resource-rational model (a01 to a07, b01 to b06).

Three theory families compete:

- **Schema and attention (Bilalic).** A familiar pattern triggers a schema that guides attention (a15).
- **Cost of leaving the prior (Binz and Schulz).** The solver has a prior over methods from earlier problems. Moving away costs effort, modelled as a KL penalty (a07).
- **Strategy selection (Lovett and Anderson).** The solver picks the strategy with the best past success ratio. No special rigidity process is needed (a21).

They work at different levels: what is activated, what it costs to move, and why the prior was set. They are not exclusive.

## 3. Core findings with exact numbers

Plain-group N differs between rows (155, 153, 121) because each condition is compared with its own matched plain group. Do not pool across rows.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Main effect: trained subjects use the long method, controls never | C1/C2: 128/155 (83%) trained vs 0/155 control, chi2=218.02. C3/C4: 100/155 (65%) vs 0/155, chi2=147.62. C1/C2 vs C3/C4 within trained: chi2=13.0, p<.001. N=310 | Binz and Schulz 2022 from Luchins thesis (a01, b01) | Established (K01); monograph not opened |
| Extinction problem failure | 64% of trained vs 5% of controls. 2.5 minute limit | Luchins and Luchins 1959 via Bilalic (a08) | Second-hand |
| Dose: more training, stronger set | 10 problems: 112/112 (100%) on C1/C2, 111/112 (99%) on C3/C4. 2 problems: 79/108 (73%) and 59/108 (55%). chi2=34.64 and 61.93 | Luchins tables 12-13 (a03, b03) | Established (K02) |
| Dose, independent replication | N=81 (107 recruited, 16 excluded). Single-step use on both critical problems: 76% at dose 0, 22% at 1, 27% at 5, 0% at 10, 12% at 20 (overall 24/81 = 29%). Logistic beta=-0.15, z=-3.87, p<.001 (odds fall 1.16x per set problem). Extinction solved by 83% (67/81). No U-shape from 0 to 40 | Crooks and McNeil 2009 (a20) | Established. One set problem already cuts flexibility, against Luchins' text |
| Warning "Don't be blind" | Long method 87/153 (57%) vs 83% plain on C1/C2, chi2=24.16. 57/153 (37%) vs 65% on C3/C4. Short method 43% and 63%. "Over half switched" holds only on C3/C4 | Binz and Schulz (a02, b02) | Single-source (K03) |
| Interleaved training (E and short-best problems) | 20/124 (16%) long method vs 97/121 (80%) blocked, chi2=100.65. Seven training problems, college students | Luchins tables 14-15 (a04, b04) | Single-source (K04) |
| Time pressure | C1/C2: 95/98 (97%) vs 126/153 (82%), chi2=12.08. C3/C4: 94/98 (96%) vs 100/153 (65%), chi2=31.8. (b05 printed 99% and 55%; these are wrong.) | Luchins tables 28-30 (a05) | Single-source (K05) |
| Age | 504 subjects, four ranks (primary, junior high, senior high, college freshmen). Long-method share on C1/C2 rises with age, r(503)=0.19, p<.001; direct-method share falls, r=-0.18, p<.001 | Binz and Schulz re-analysis of Luchins data (d15) | Established in Luchins' data (K11); small r; age is mixed with years of practice with one method |
| IQ | Luchins found no strong IQ or education effect; Ross (1952) and Luchins and Luchins (1959) found the age rise with IQ controlled | Second-hand (a06, d15) | Contested; sources not opened |
| Chess skill gradient, Exp 1 | 2-solution problem found by Grand Masters 100% (n=6), International Masters 50% (n=6), Masters 18% (n=11), Candidate Masters 0% (n=11). 1-solution control: all experts 100%; Class A 63% (n=8), B 13% (n=8), C 0% (n=8). Logistic B=.013, SE=.005, Z=8.4, p=.004. 100 Elo points lower cuts the odds by 3.67. Fitted P(find): GM .64, IM .32, Master .12, CM .01 (fit is below the observed GM rate) | Bilalic et al. 2008a, re-opened (a10, b07, b08, d11) | Established (K06) |
| Chess skill gradient, Exp 2 | B=.006, SE=.0016, Z=3.72, p=.0002 (different problems from Exp 1; the 3.67 and 1.82 are not interchangeable; d11). Four problem pairs. GM/IM 92% (n=12), Masters 69% (n=12), CMs 35% (n=12). Weaker players on 1-solution: A 91%, B 66%, C 47%. Odds factor 1.82 per 100 Elo; found 87% at Elo 2500, 67% at 2300, 37% at 2100. Finders averaged Elo 2357 vs 2242, t(34)=2.09, p=.044. One easy problem showed no effect | Bilalic et al. 2008a (a11, b08) | Established |
| Chess, prior rejection (Exp 3) | 12 players (5 GM, 4 Masters, 3 CMs). Plan correctly rejected in problem 2, correct again in problem 3; 10 min per problem. All failed except one of five GMs. Solvers median Elo 2547 vs 2258, U=2, p=.017 | Bilalic et al. 2008a (a12, b10) | Single-source, tiny N |
| Experts misjudge peers | 12 experts (mean Elo 2231) predicted 86%, 74%, 59% for IM, Master, CM; actual 50%, 18%, 0%. Exp 2: predicted 97/89/73%, actual 92/69/35% | Bilalic et al. (b09, a11) | Established as a pattern (K07) |
| Gaze stays on the familiar squares | Candidate Masters, about 5 per group. Settled on smothered mate after 37 s (SD 20); all said they sought better. 2-solution group: no gaze shift over six periods, F(5,20)=0.6, ns. 1-solution group found optimum in 79 s (SD 25); gaze moved, F(5,20)=11.9, p<.001, partial eta2=.75 | Bilalic et al. 2008b (a13, b11) | Established with Sheridan and Reingold (K07); small N |
| Set lingers after the lure is gone | Exp 1: 148 s (SD 90) vs 79 s (SD 25), t(8)=1.67, p=.13, d=1.2 (not significant, about 5 vs 5 players). Later experiment: fresh players needed about half the time, t(44)=2.16, p=.036, d=.65; skill by group F(2,40)=0.9, ns. Compared with a historical group, not randomised. Re-read in d13 | Bilalic et al. 2008b (a14, b12, d13) | Suggestive; counts as established only together with the magic lure and LLM data (K09) |
| Search time before success or giving up | Median search before success: GM 7 s, IM 9 s, Master 10 s. Players who failed searched 9 s (IM), 8 s (Master), 8 s (Candidate Master) before settling on the familiar mate | Bilalic et al. 2008a, verbal protocols (d12) | Established (K07) |
| Impossible lure still blocks | Magic trick, N=120 (40 per version). 82.5% proposed the false solution in control. Real secret found by 60% (false-solution-extinction version) vs 87.5% (no false solution), chi2=7.81, p<.01 | Thomas, Didierjean and Kuhn, manuscript (a18) | Manuscript, not peer reviewed |
| Boundary: familiar move is a blunder | 17 experts, 17 novices; 4 test and 8 filler problems. Problem 1 (familiar move good but suboptimal): 8/17 experts and 8/17 novices chose it. Problems 2 to 4 (blunder): all experts and most novices avoided it. Experts reached the target region sooner (407 vs 719 ms, p<.01). Gaze disengagement for experts F(1,66)=13.12, p<.01; novices F(1,66)=2.25, ns | Sheridan and Reingold 2013 (a16, b14, b15) | Single-source (K08) |
| Anagrams | N=60, 72 trials, 45 s limit. RT 15.3 s (word) vs 13.4 s (non-word), t(59)=3.25, p<.01. Accuracy 51.7 vs 53.8%, t(59)=1.52, ns. Dwells 8.11 vs 6.76, t(59)=4.69. First fixation on the string shorter for words (encoding help) | Ellis and Reingold 2014 (a17, b16) | Replication in a new domain; a 1.9 s slowdown, not an accuracy loss |
| Cognitive load can help | 74 students, 62-trial five-jar task. Survival curves differ, chi2(1)=4.97, p=.028. Found the alternative at all: 25 (low) vs 27 (high), Fisher p=.161 | Ninomiya et al. 2024 (a19) | Single-source; contradicts "load raises rigidity" |
| Programming | 39 developers; 44% showed a set; those with a set had fewer months of Python (t=2.806, p=.006). Colour change and "forget earlier solutions" did not break it | Sergeyuk et al. 2023 (c24, b28) | Single-source, small N |
| Maths equivalence | Complex-first order reduces shortcut use, flexibility and understanding. N=41 undergraduates, N=87 fifth and sixth graders (summary page only) | DeCaro 2016 (b18) | Snippet only [M] |
| Matchsticks | Non-insight sets: no effect on insight problems. Insight sets: help or hurt by problem type | Ollinger et al. 2008 (b17) | Snippet only [M] |
| Think-aloud | Does not change effect size in the water-jug task; protocols show repeated variants of the old method | Blech, Gaschler and Bilalic 2020 (b19) | Snippet only [M] |

## 4. Mechanisms and models

### 4.1 Resource-rational prior with a cost to leave it (Binz and Schulz)

An engineer can implement it like this.

- Keep a probability distribution over solution methods (the prior p).
- On each problem choose a policy q that maximises expected utility minus (1/beta) times KL(q || p). Beta is an inverse temperature: high beta means cheap to move away from the prior, low beta means sticking to it.
- After each problem, update the prior by one gradient step (learning rate 0.5 in their runs) toward the method used and found to work.
- Their settings: plain beta=25, DBB beta=30, speedy beta=15. Of 100 simulated agents, E-method use on C1/C2 and C3/C4: plain 90 and 84; DBB 68 and 46; speedy 97 and 98. Alternating training 23 vs 90 for E-only training (a07).
- A perfect searcher would check 9261 options. An agent with beta=0.6 checks about 10 (b06).
- It reproduces the main effect, warning, dose, interleaving and time pressure. Ablations say every part is needed.
- Weak point: beta is hand-set per condition and there is no likelihood fit. It fits aggregate percentages, so it is a plausibility check, not a strong test (K12).

Design rule it suggests: examples shape the prior. Anything that lowers the cost of leaving it (explicit alternatives, a forced list) should work better than a reminder.

### 4.2 Strategy selection by success ratio (Lovett and Anderson, ACT-R)

- Each strategy is a production rule with counts of successes and failures.
- Estimated success chance is a Bayesian estimate from those counts plus a prior.
- The strategy with the highest expected gain (success chance times value minus cost) fires.
- 68 CMU students (one removed for recalling the jars, 67 analysed), 90 problems, success ratios 80/20 and 60/40. Fit R2=.99 on binned data, R2=.66 per subject on the last 45 problems. 6 of 48 subjects in three conditions picked the better strategy on at least 43 of the last 45 problems (a21).
- Implication: a strategy that always works keeps being chosen even if another is cheaper. Rigidity is the expected result of a success-based chooser that does not track cost.

### 4.3 Schema-guided attention (Bilalic)

- A pattern is recognised and the matching schema (chunk or template) activates.
- Attention goes to the features the schema predicts. Gaze data: experts stay on the familiar squares while believing they search (a13).
- Consistent evidence is picked up; other evidence is not sampled.
- Easier problems show the effect in weaker players, harder ones in stronger players (a15). Finer templates in strong players reject a plan that does not fit (a12).

Engineer's reading: the first recognised approach sets what the model attends to, and later sampling is conditioned on it. For an LLM the nearest analogue is the context itself.

### 4.4 A detector (our inference, untested)

Human signs: stated intention ("looking for something shorter") does not match behaviour (no new squares visited); long time to settle (37 s); after failure the next attempts are variants of the old method (b19). Agent-trace parallels: claims of exploring with no new method in the attempts; near-copies of the first method; no change of approach after a reject. All can be checked by code comparing attempt structure. This is a design idea, not an established result (see UNKNOWNS U6).

Two LLM results shape the design. First, a model's own words are a weak signal: reasoning models state the hint they used in often under 20% of cases (average faithfulness 25% for Claude 3.7 Sonnet, 39% for R1; d18), and human experts also said they were searching while their gaze did not move (d12, a13). So the detector must read behaviour, not claims. Second, candidate behaviour features exist: where in the trace the first answer appears and how much follows it (d17), the number of distinct new routes after the first answer, and tokens spent re-checking the first route (K26). None has been built or validated for Einstellung.

### 4.5 Context drag: a rejected route keeps its pull

This is the LLM version of the set, and it needs no theory beyond how a model reads its context.

- The model conditions every new token on all earlier tokens. A wrong draft, a failed call or a long run of same-method examples makes similar tokens more likely.
- Measured in reasoning models: with one wrong draft in context, answers stay structurally closer to the draft (tree edit distance) than clean-slate answers do (d01).
- Measured in small models (135M to 1.7B): the surface form of the failed call explains 83% of the damage; replacing the verbatim call with a runtime description removed 76% of it (d05).
- Design consequence for an engineer: a failure record should be a short neutral description of what was tried and why it failed, never the verbatim failed text, and the retry frame should differ from the first frame.

## 5. What holds up

### Replications and extensions

- Numbers: the gap pass re-read the Binz and Schulz text and every Luchins count held (d14). It found that the 0.99 vs 0.55 typo for time pressure is printed in the paper itself; the counts (94/98, 100/153) give 0.96 vs 0.65. Chess odds factors 3.67 and 1.82 were re-read in the Bilalic paper (d11). The 1942 monograph is still unopened, so the Luchins numbers stay second-hand.
- Age: in Luchins' own 504 subjects the long-method share rises with age (r=0.19, p<.001; d15). It reads as more history with one method, not as more capability.
- Dose effect: two routes agree. Luchins' tables: 2 problems 73%/55%, 10 problems 100%/99% (a03). Crooks and McNeil (N=81): flexibility falls with dose, biggest drop from 0 to 1 set problem (76% to 22%) (a20). Strong.
- Chess: graded by skill, large, found in two experiments by the original group (a10, a11, d11). Expert forecasts of peers were far too high (86/74/59% predicted vs 50/18/0% actual; d12). Sheridan and Reingold found it again with eye tracking, but experts and novices fell equally for a good-but-suboptimal move (8/17 each) (b14). The mechanism (attention on the familiar move) agrees; the skill moderation differs.
- Other domains: anagrams (a17), maths equivalence (b18, snippet), matchsticks (b17, snippet), programming (c24), magic (a18, manuscript). The effect travels, though in anagrams it is a 1.9 s slowdown.

### Failures and weak spots

- Luchins' claim that practice beyond a few problems does not matter is refuted by Crooks and McNeil and by his own thesis tables.
- Two cheap programming interventions (editor colour, "forget earlier solutions") did not break the set (c24).
- Think-aloud did not change the effect (b19, snippet).
- The "148 vs 79 s" lingering result is not significant (p=.13).
- Higher training complexity led to earlier discovery of the alternative (a19), the reverse of a simple load story.
- The rejection test is thin in humans: the 148 vs 79 s result is p=.13 and the later one compares with a historical group (d13). Support for "a rejected route keeps its pull" comes mostly from LLM work (K22).
- No meta-analysis of the Einstellung effect was found.
- No adequately sized, Luchins-style test in an LLM exists (section 6).

### Moderators

- Dose: strong. Time pressure: raises the set (97% vs 82%; 96% vs 65%) (a05).
- Skill: reduces but does not remove the effect (a10, b10).
- Quality of the familiar option: a blunder is avoided, a merely good option is taken (b14).
- Age: grows with age per later work (a06, contested).
- Problem difficulty: an easy fifth chess problem showed no effect (a11).
- Training composition: interleaving removes most of the effect (a04).

### Interventions

| Intervention | Result | Status |
|---|---|---|
| One-off warning ("Don't be blind") | Long method 57% vs 83% (C1/C2), 37% vs 65% (C3/C4). Helps, does not remove | Single-source |
| Interleaving short-best problems into training | 16% vs 80% | Single-source, largest effect |
| Disabling the familiar solution | Experts find the short line (b07); 69% vs 11% (a09) | Works, but removes the trigger, not the habit |
| Less time pressure | Set weaker (65% vs 96%) | Single-source |
| Colour change / "forget earlier solutions" | No effect | Single-source, small N |
| Think-aloud | No change | Snippet |
| Advice: remind yourself, write down contrary facts at once | No measured effect (b20) | No evidence |
| More complex trained procedure | Earlier discovery of the alternative (a19) | Single-source |

Pattern: a plain reminder gives a partial effect. Changing what was learned (interleaving) gives the largest. This is what the cost-of-leaving model (4.1) predicts.

### Competing explanations

- Rational learning from a skewed history (4.2) vs attention capture by a schema (4.3). Both predict persistence. The warning data (partial switching) suggest the short route can be found when the solver is told to look.
- Part of the extinction failure is the 2.5 minute limit (a08).
- Familiarity also helps encoding (a17), so the net effect mixes interference and help.

## 6. Language models

Many LLM papers use the word "Einstellung" or "fixation", but almost none uses the Luchins design (build a set with earlier problems, then measure). Most use trap items. Trap items measure a default learned in pretraining, not a set built in context.

### Direct Luchins-style order test

Haq et al. (2025; c01, c02, b21). Items from DeCaro (2016): six complex and six shortcut maths equivalence problems. Llama-3.1-8B, Llama-3.1-70B, GPT-4o. Six items per cell, so one item is 0.17.

- Few-shot exact match, GPT-4o: shortcut-only 0.33, shortcut after complex 0.66, complex-only 0.66, complex after shortcut 0.83.
- Llama-8B: 0.16, 0, 0, 0. Llama-70B: 0, 0.16, 0, 0.66.
- With zero-shot chain of thought, shortcut-only: Llama-8B 0.5, Llama-70B 0.5, GPT-4o 0.66; complex-first lifted these to 0.66 each. Steps to solution stayed at 3 in every model and condition (humans need 1 on shortcut items).
- Reading: prior complex problems did not hurt; most cells rose. No statistics, no repeats, no no-set control. It fails to show a set. It does not refute one (K13, contested). The fixed 3 steps looks like a CoT routine, not an order effect.

### Trap and red-herring benchmarks

- **Only Connect walls (a22, b22, c03 to c05).** 494 test walls (1976 groups). Humans solved 285 walls and 1405 groups. GPT-4 0-shot solved 6 walls (239 groups); best 5-shot 7 walls (269 groups). GPT-3.5 0-shot solved 0 walls (114 groups). With red herrings removed (OCW-WordNet): GPT-4 471 of 494 walls (1926 groups), GPT-3.5 337 walls. Randomised variant: GPT-4 59 walls (595 groups). More shots did not help: GPT-4 correct groups 239, 262, 272, 269, 249 at 0, 1, 3, 5, 10 shots. Limits: no training sequence, the lure is built into the item, WordNet walls are also easier, failures include knowledge gaps, 2023 models.
- **M-ARC (Kim et al. 2025; b23, c06, c07).** 100 hand-written medical items where the familiar pattern gives a wrong answer. Most LLMs below 50%, several below 20%. Best: Gemini-1.5-Pro 50%, o1 48%. Five physicians averaged 66% (SE 5.3%). Models were overconfident across 15 samples per question; larger models better calibrated but still overconfident. Agreement across samples can be the same trap repeated.
- **M-ARC retest (Shidara et al. 2026; b24, c08, c09).** Reasoning models at their highest effort setting, 15 runs each. The paper did not vary effort (d06), so "effort is the lever" is a hypothesis, and reasoning vs non-reasoning is confounded with training. Claude 4.1 Opus mean 0.751 (95% CI 0.738 to 0.763) vs physicians 0.66 (CI 0.55 to 0.75): no significant difference; also Gemini 2.5 Pro, GPT-5.1, Grok-4-Fast-Reasoning. On the 20 items physicians most missed, humans scored 36% (CI 26 to 46%) vs 73% on the rest; best model decisively right on 55.0%, decisively wrong on 25.0%. Limits: same 100 items, now public (contamination), highest effort only.
- **MedEinst (Chen et al. 2026; a23, b25, b26, c10 to c12).** 5,383 paired cases, 49 diseases, 17 LLMs, built from DDXPlus. Trap rate = share of control-correct pairs where the trap case still gets the control answer. Gemini-2.5-Pro 60.90%, GPT-5 51.87%, Claude-Sonnet-4.5 42.98%, Qwen3-32B 43.46%. Base accuracy: GPT-5 54.30%, Gemini 53.58%, Claude 42.09%, Qwen3-32B 40.25%. No size gain ("Stronger Priors, Stronger Blindness"). Across 15 plain LLMs baseline accuracy and trap rate correlate weakly (r=0.49 by our computation, n=15, not significant; d07). Robust accuracy is nearly flat at 11 to 12% for most models; DeepSeek-R1 (42.20 / 11.32 / 46.12) and QwQ-32B (41.05 / 11.14 / 44.88) are not clearly better than Qwen3-32B (40.25 / 11.86 / 43.46) (accuracy / robust / trap). Multi-agent frameworks lowered accuracy: MDAgent 29.70, DyLAN 32.11 vs base 40.25. But their trap rates (40.34, 41.69) were slightly below the base 43.46 (d08), so the claim that debate "reinforced the majority prior" is not shown by the trap rate. Trap rate is conditional on a correct control answer, which biases comparisons across weak and strong models. GPT-5 errors: blindness to key evidence in over 35%; of the rest 43% underthinking and 22% overthinking. The authors' own agent on Qwen3-32B: base accuracy 40.25 to 55.49 (plus causal audit) to 69.49 (plus memory); robust accuracy 11.86 to 19.94 to 24.21; trap rate 43.46 to 38.32 to 33.75. Preprint, own system on own benchmark, LLM-built cases, no independent run.
- **Tension.** MedEinst: stronger models are not less fooled. Shidara: reasoning models reach physician level. The benchmarks differ (100 hand-written items vs 5,383 generated). Reasoning effort may be the variable; nobody has tested it on MedEinst.

### Failed attempts and drafts in context (the closest LLM analogue of a built set)

None of these use the Luchins design, but each shows that material already in the context pulls the next attempt toward the same kind of answer. They are single-lab preprints from 2025-2026.

- **Contextual drag (Cheng et al. 2026; d01 to d03).** 11 models, 8 tasks, 16 samples per question. One wrong draft in context versus a clean slate (pass@1): GPT-OSS-20B HMMT25 58.63 to 20.54; GPT-OSS-120B HMMT25 61.01 to 48.51; Qwen3-32B HMMT25 49.70 to 36.90; GPT-OSS-20B AIME24 51.88 to 17.50; GPT-OSS-120B GPQA-Diamond subset 58.24 to 35.70; GPT-OSS-120B Game of 24 77.34 to 56.94. Frontier models lose less: GPT-5 AIME25 87.50 to 81.73; Gemini-3 Pro 94.23 to 90.38. Tree edit distance shows the answers stay closer to the wrong draft. More wrong drafts (1 to 4) do more harm.
  - An explicit "this draft is wrong, do not copy" line did not restore clean-slate accuracy. Even after the model itself verified the draft as wrong, changes versus clean slate ranged from -23.8 to +16.1 points depending on model and benchmark. Iterative refinement could collapse (GPT-OSS-20B), while majority voting over the same samples rose.
  - Mitigations: rewriting the draft (REVISE) gave GPT-OSS-20B HMMT25 62.20 vs clean 58.63, but Qwen3-32B CRUXEval-I only 65.36 vs clean 75.83 (leaving the draft in: 54.89). Filtering the draft gave 45.83 and 62.90 on those cells. A fine-tuned reset lifted GPT-OSS-20B AIME24 17.5 to 40.6 and HMMT25 33.9 to 45.3, not to clean level. Denoising costs at least 2x inference.
- **Reflection repeats the fault (Weatherhead et al. 2025; d04).** Eight frontier models wrote items under rules, critiqued themselves, and revised. The second attempt repeated the original failure category in 85.36% of 567 attempts (484/567). Reasoning-marketed models had no edge. Not a Luchins design.
- **Feedback backfires in small agents (Gumaan 2026; d05).** Six checkpoints, 135M to 1.7B parameters. Leaving a failed tool call in the transcript raised the chance of repeating it over four candidates from 0.06 to 0.54; greedy decoding repeated it exactly on 19% of items after failure vs 0% before. "Do not repeat" changed nothing. Retrying from the same clean prompt was the worst harness for repetition. Replacing the verbatim call with a description removed 76% of the effect. Frontier models untested.
- **Dose.** The harm grows with the number of wrong drafts (d01). A Luchins-style dose of same-method examples was not found in any LLM study. Many-shot work (Agarwal et al. 2024; d19, abstract only) shows dose changes behaviour in general. Example order moves results (Lu et al. 2022; d20, abstract only).

### Aggregation and shared priors

- **Voting beats debate on average (Choi et al. 2025; d09).** Qwen2.5-7B over seven benchmarks: single 0.7205; decentralised debate T=2 0.7377, T=3 0.7112, T=5 0.7050; centralised debate 0.6551; majority voting 0.7691.
- **Errors are shared (Kim et al. 2025; d10).** Over 350 LLMs, pairs agree about 60% of the time when both are wrong (about 33% by chance). More accurate models are more correlated.
- Together: voting only helps if the right answer is the likely one. On a shared-prior trap the majority is wrong. Differently framed prompts are the untested remedy (K24).

### Trace shape and token effort

- **Illusion of Thinking (Shojaee et al. 2025; d17).** On easy puzzles reasoning models find the answer early and keep exploring wrong paths. On hard puzzles they fixate on early wrong answers and token effort drops near collapse. Published critiques (token limits, infeasible instances) were not opened.
- **Faithfulness (Chen et al. 2025; d18).** Reveal rates are often under 20%; the trace is a weak witness of what drove the answer.
- **No effort sweep.** No study varied reasoning effort or token cap on a fixed trap set (K25). Token-budget work (Han et al. 2024; d21, abstract only) measures cost, not rigidity.

### Related fixation work

- **Counterfactual tasks (Wu et al. 2024, c18).** Eleven tasks. Performance drops consistently when default rules change (base-10 arithmetic, standard indexing) but stays above chance. A pretraining default, not an in-context set.
- **MacGyver (Tian et al. 2024, c19, c20).** 1,683 problems on unconventional tool use. GPT-4 efficient solution 18.9%, infeasible 37.5%. On 180 sampled solvable problems, divergent-then-convergent raised efficient solutions by 6.5 points (self-reflection 2.2); self-reflection cut infeasible solutions by 9.7 points (divergent-convergent 4.3). Claude 2 and Llama-2-13b did not gain from self-reflection. Single runs.
- **BRAINTEASER (Jiang et al. 2023, c21).** ChatGPT 53% and 63% on two subtasks vs humans 92% and random 25%. 2023 models.
- **Multi-solution tasks (Guan et al. 2025; c13, c14, b29).** Short CoT stops after an initial answer set. Short-CoT calibration error above 78.22% for all series; long CoT cuts it by at least 18.28%. New-solution discovery 0.01 to 0.20% for short CoT vs up to 2.50% for long CoT. A nudge "Wait, there may be other solutions" raised precision and recall (figure only). Self-consistency n=32 on Qwen3-8B Long-CoT: TimeTabling recall 9.99 to 49.55 (table partly garbled).
- **Underthinking (Wang et al. 2025, c16).** The opposite failure. Wrong answers use 225% more tokens and 418% more thought switches than correct ones (QwQ-32B-Preview and R1 models on MATH500, GPQA Diamond, AIME2024). A decoding penalty on thought-switch tokens raised accuracy with no training. Forcing persistence is not always good.
- **Self-correction without outside feedback (Huang et al. 2024, c17).** GPT-3.5 CommonsenseQA 75.8, then 38.1 (round 1), then 41.8 (round 2). GPT-4 GSM8K 95.5, 91.5, 89.0. With oracle labels GPT-3.5 GSM8K 75.9 to 95.5. 2023-era models.
- **Agent frameworks (PPoGA, c15).** Names functional fixedness as the failure of agents that cannot drop a flawed plan; adds whole-plan correction. GrailQA 78.9 vs 76.5; CWQ 64.5 vs 63.2; WebQSP Hits@1 83.1 vs 82.0. Gains of 1 to 2 points; fixedness not measured directly.
- **Human side of the loop (Liu et al. 2025, c25).** 450 participants; prior system experience shapes prompt style. Betas about 0.1. About users, not models.
- **Network analogues.** Gu and Shi (2025; b27, c23): two-phase CIFAR-100 with a spurious patch; continual learners reached accuracy sooner than scratch (negative adaptation delay); performance deficit 0.107 +/- 0.039 for the one positive case; the authors say the pattern is not Einstellung. Loewe et al. (2024; c22): 99 humans and 99 networks; 49 of 99 humans (49.5%) found a hidden shortcut; networks mimic the abrupt switch only with regularised gating and noise (K19).

### What changed LLM fixation, and by how much

| Change | Effect | Source |
|---|---|---|
| Removing red herrings | GPT-4 walls solved 6 to 471 of 494 | c04 |
| More few-shot examples | none (239 to 249 groups at 0 vs 10 shots) | c05 |
| Reasoning models at highest effort (M-ARC) | below 50% to 0.751, level with physicians | c08 |
| Model size / baseline strength (MedEinst) | none; weak positive link between accuracy and trap rate (r=0.49, n=15, ns) | c11, d07 |
| Multi-agent debate (MedEinst) | accuracy 40.25 to 29.70 / 32.11; trap rate 43.46 to 40.34 / 41.69 (slightly lower) | d08 |
| Wrong draft left in context (contextual drag) | up to -38 points (GPT-OSS-20B HMMT25 58.63 to 20.54); frontier -4 to -6 | d01 |
| Explicit "draft is wrong" line | did not restore clean-slate accuracy | d02 |
| Rewriting the draft (REVISE) | restored or beat clean slate in some cells (62.20 vs 58.63), not others (65.36 vs 75.83) | d03 |
| Failed call as verbatim text vs description (small models) | repeat probability 0.06 to 0.54 with verbatim; description removed 76% of the harm | d05 |
| Self-reflection on own failure | repeated the failure category in 85.36% of attempts | d04 |
| Majority voting vs debate (general benchmarks) | 0.7691 vs 0.65 to 0.74 | d09 |
| Evidence audit plus validated-path memory (authors' system) | trap rate 43.46 to 33.75, accuracy 40.25 to 69.49 | b26 |
| Long vs short CoT (multi-solution) | new-solution discovery 0.01 to 0.20% to up to 2.50% | c13 |
| "There may be other solutions" cue | recall and precision up (figure only) | c14 |
| Divergent then convergent prompt (MacGyver) | +6.5 points efficient solutions | c20 |
| Self-reflection without feedback | worse (GSM8K 95.5 to 89.0) | c17 |
| Complex-first order in context (Haq) | no harm, often better; 6 items per cell | c01 |

No study found measures Einstellung in an LLM agent with a Luchins-style design at adequate N. This is the main gap.

## 7. What our agent should take

Marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **A passing route is not proof it is the best one. G1 note, S4. [E] K01, K06; a01, a10, b07, b08.** G1 fires doubt only on a signal, and Einstellung has none. Add a note that the cost of a passing route (steps, tokens) is logged, so code can compare it. Keep it signal-driven: forced doubt on a schedule cost 17 points on word puzzles (G1 data), so this must not become a schedule.
2. **Fixation survives rejection: keep rejected routes out of fresh attempts. S3, S5. [E] K09, K22; b10, b12, a14, a18, b19, d01, d02, d05, d13.** S3 already gives each attempt a fresh context. Add that after a route is rejected, code records it as a short neutral description (not the verbatim text) and later attempts do not see the text as a starting point. Human data: a lure known to be impossible still cut finding the real solution (60% vs 87.5%). LLM data: failed drafts cut accuracy by up to 38 points, labels and warnings did not undo it, and a description instead of the verbatim call removed 76% of the harm in small models. Caution: rewriting is not always safe (K23), so the exact record format is a Test-first item.
3. **Stated search is not evidence of search. G10. [E] K07, K26; a13, b11, b09, a16, d12, d18.** Experts said they were searching while gaze stayed put (median 8 to 9 s of "search" before settling). Reasoning models mention the hint they used in often under 20% of cases. Check traces by code, not by the model's claim.
4. **No plain reflect or be-careful prompt as the fix. 4b. [E] K17, K03; c17, a02, d02, d04.** Already listed. New support: self-correction without feedback lowered GSM8K 95.5 to 89.0, reflection repeated the first failure category in 85.36% of attempts, and an explicit "draft is wrong" line did not restore clean-slate accuracy.
5. **Do not count on debate, voting over one prompt, or model size to remove a shared trap. G9, G4. [E for the shared-error fact, C for size] K24, K16, K15; d09, d10, d08, c07, c11.** Models share errors (about 60% agreement when both are wrong). Debate lowered MedEinst accuracy but its trap rate was not higher, so do not claim debate makes fixation worse. Size gave no gain in MedEinst. Keep voting for ordinary items, where it beats debate (0.7691 vs 0.65 to 0.74).
6. **Structured alternatives beat plain reflection. S3 open mode, O. [E] K17; c20.** Divergent-then-convergent raised efficient solutions 6.5 points vs 2.2 for self-reflection.

### Test first

| Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|
| In-context set: N same-method examples, then a critical item with a shorter route | G1, S3 | [C] | K13, K01, K02; c01, a01 | Only LLM test has 6 items per cell and shows no set. If our agent has none, drop in-context order work. |
| Interleaved vs blocked examples | S3, memory (lessons) | [S] | K04; a04 | Largest human effect (16% vs 80%). Bears on how lessons and few-shot examples are built. |
| Dose curve 0, 1, 5, 10, 20 same-method examples | memory (lessons), S3 | [E] human only | K02; a20 | One set problem cut human flexibility 76% to 22%. Sets a safe count of same-class lessons. |
| Hint line vs forced list of alternatives vs plain reflection | S3, O, 4b | [S] | K03, K17; a02, c20, c14 | Human warning gave 20 to 28 points; LLM cue data is figure-only. |
| Rejected route cleared vs left in context vs described neutrally | S3, S5 | [E] human and LLM drift, format untested | K09, K22, K23; d01, d03, d05 | Direct test of the lure effect, and which record format is safe. |
| Reasoning effort and token cap sweep on one model, fixed private trap set | S0, G11 | open | K25; d06, d07 | No sweep exists; M-ARC and MedEinst disagree. |
| Voting over reframed prompts vs same-prompt voting | S7, G4 | supported-indirect | K24; d09, d10 | Shared errors mean same-prompt voting may not break a trap. |
| Trace detector for "claims to explore, only varies old route" | S6 trigger | [S] | K07; a13 | Would give G1 a code-checked signal in the no-failure case. |
| Tight vs loose token budget on trap items | G11, G12 | [S] | K05; a05 | Human set rose under time pressure (96% vs 65%); G11 favours short thinking. |
| Low vs high reasoning effort on a fixed trap set | S0, G11 | [C] | K15, K16, K18 | M-ARC and MedEinst disagree on what helps. |

These go to UNKNOWNS.md and enter SCHEMA.md only after the test passes.

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup counted, G7). Report fixation with confidence intervals. Minimum 50 items per cell (Haq had 6).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Generated Luchins-style tasks (jar-like or arithmetic): 5 training items solved by a long method, then critical items with a shorter route, plus an extinction item only the short route solves. 50+ critical items per cell | (a) control: critical items only; (b) blocked: 5 same-method examples in context; (c) interleaved: examples of both types | Share of critical answers using the long method; extinction-item pass rate | If model matches people: (b) far above (a), which is near 0%; (c) near (a). If (b) equals (a), no in-context set at this scale |
| T2 | T1 items, dose series | 0, 1, 2, 5, 10, 20 same-method examples | Long-method share vs dose | Monotone rise; a big step at 1 if humans transfer |
| T3 | T1 items, prompt arms | (a) none; (b) one line "a shorter method may exist"; (c) forced list of 2 alternative methods before solving; (d) plain "reflect on your answer" | Long-method share; accuracy | (c) beats (b) beats (d); (d) near (a) or worse |
| T4 | Paired trap items (MedEinst style or our own): control case and trap case with one flipped fact | Single attempt; 3 same-prompt samples with code vote; 3 reframed samples with code vote; debate (negative control); audit step | Trap rate (control right, trap wrong); robust accuracy | Same-prompt voting and debate do not cut trap rate; reframing and the audit step cut it by a few points |
| T5 | Puzzles with a known longer familiar route and a shorter route | Plain; harvest of dropped candidates (S4); assigned untried direction in a fresh context | Share of runs reaching the shorter route | Harvest and assigned direction beat plain |
| T6 | Route A shown impossible in context, then related items | A left in; A removed; one line "A failed" | Share of next attempts that are variants of A (code-judged) | Removed beats left in |
| T7 | T1 critical items | Tight vs loose token budget | Long-method share | Tight raises fixation if humans transfer |
| T8 | Fixed private trap set | Low vs high thinking budget | Trap rate; tokens per item; thought-switch count | High effort cuts trap rate; watch the opposite failure (c16) |
| T9 | T1 and trap items | Ask "are you exploring alternatives?"; code counts distinct methods | Gap between claim and count | A large gap justifies building the detector |

| T10 | T6 items, record format | Failed attempt: kept verbatim; removed; short neutral description; rewritten by a second call (counted in tokens) | Pass rate on the next attempt; similarity to the failed route | Removed or description beats verbatim by several points; rewrite helps on some tasks only (K23) |
| T11 | Trap items (private) | Same-prompt voting k=3; reframed voting k=3; single attempt | Trap rate; robust accuracy | Same-prompt voting leaves trap rate near single; reframing lowers it |

Controls: shuffle item order, fix seeds, keep held-out items for the final report (G3), record setup cost of every added line.

## 9. What does not transfer, and why

- **Water-jar rates.** The 83% and 65% are for people with years of habit and paper-and-pencil group testing. They give no rate for an LLM.
- **Skill as protection.** Chess skill helps because experts have finer templates (a12). A bigger LLM has no such property; MedEinst finds no size effect (c11).
- **Time pressure.** People hurry because of a clock. Our agent has a token budget and no stress. The parallel is loose (K05).
- **Age and IQ.** No analogue (K11).
- **Eye tracking.** No gaze in an LLM. The nearest analogue is trace structure, which we have not measured.
- **Prior habit vs in-context set.** The human set builds over minutes of learning. In an LLM the only set is the context, unless the item matches a pretraining default. M-ARC, MedEinst, Only Connect and counterfactual tasks test the latter. The two may need different fixes.
- **The "Don't be blind" warning.** It worked on people because they could change behaviour at once. For an LLM, the line sits in the same context that creates the set. Needs test T3.
- **Network analogues (Gu and Shi, Loewe).** Small image or perceptual networks, not language agents (K19).
- **Popular advice** (remind yourself, record contrary facts) has no measured effect (b20).
- **Eye-tracking N.** Groups of 5, one position, Candidate Masters only. Do not scale it up.

## 10. Open questions

1. Does a Luchins-style order manipulation produce a set in current LLMs and reasoning models, at adequate N and equal tokens?
2. Does reasoning effort reduce Einstellung more than size, and where is the break point (M-ARC vs MedEinst)?
3. Which intervention cuts LLM fixation at equal tokens: warning line, forced alternatives, interleaving, context clearing, or a second independent attempt?
4. Does the human finding that one set problem already hurts hold for in-context examples?
5. Do LLMs repeat variants of a rejected route (Bilalic Exp 3, magic lure)?
6. The 3.67 and 1.82 per 100 Elo figures and the Luchins counts were re-confirmed (d11, d14). Still open: the 1942 monograph itself, Luchins and Luchins (1959) and Ross (1952).
7. The age effect is real in Luchins' data (d15). It maps to history with one method, not to capability. Does in-context history length act the same way?
8. Does debate or self-consistency voting reinforce the shared prior on non-medical Einstellung tasks? Is independent sampling with different framings better?
9. Can a trace-based detector of "claims to search, does not" be built?
10. Does token or time pressure raise fixation in LLMs, as in people (97% vs 82%)?
11. Does the Crooks and McNeil dose result replicate in other tasks?
12. Is the interleaving result (16% vs 80%) real? It is a single 1942 source with no modern replication.
13. Has the M-ARC retest been affected by leakage? The items are public; a fresh private trap set is needed.
14. Do the contextual-drag and failed-call results (small and open models, math and code) hold for frontier agents on tool tasks?
15. What record format for a rejected route is safe: description, removal, or rewrite? Rewrite beat clean slate in some cells and lost in others.
16. Do shared errors across models (about 60% agreement when both are wrong) make cross-model voting useless on shared-prior traps, and do reframed prompts fix it?

## 11. Sources

[V] means the page or PDF text was opened and read this session. [M] means snippet or abstract only. Evidence ids in brackets.

- [V] Binz and Schulz (2022) Reconstructing the Einstellung effect. https://osf.io/download/yhcf4/ (a01 to a07, b01 to b06)
- [M] Binz and Schulz (2022), search abstract. https://scholarhub.vn/publication/Reconstructing-the-Einstellung-Effect/29151f8d (c26)
- [M] Luchins (1942) Mechanization in problem solving: the effect of Einstellung. Psychological Monographs 54(6). Not opened; cited via https://escholarship.org/uc/item/1976z9q8 (a25)
- [V] Bilalic, McLeod and Gobet (2008) Inflexibility of experts, reality or myth? Cognitive Psychology 56. http://bura.brunel.ac.uk/bitstream/2438/641/1/ (a08 to a12, a24, b07 to b10; the full file name is truncated in the evidence file)
- [V] Bilalic, McLeod and Gobet (2008) Why good thoughts block better ones. Cognition. http://bura.brunel.ac.uk/bitstream/2438/2276/1/Einstellung-Cognition.pdf ; https://doi.org/10.1016/j.cognition.2008.05.005 (a13, a14, b11, b12)
- [V] Bilalic, McLeod and Gobet (2010) The mechanism of the Einstellung (set) effect. http://bura.brunel.ac.uk/bitstream/2438/5777/1/Fulltext.pdf (a15, b13)
- [V] Bilalic and McLeod (2014) Why your first idea can blind you to a better one. Scientific American. https://www.scientificamerican.com/article/why-your-first-idea-can-blind-you-to- (b20; URL truncated in the evidence file)
- [V] Sheridan and Reingold (2013) Mechanisms and boundary conditions of the Einstellung effect in chess. https://doi.org/10.1371/journal.pone.0075796 (a16, b14, b15)
- [V] Ellis and Reingold (2014) The Einstellung effect in anagram problem solving. https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00679/pdf (a17, b16)
- [V] Thomas, Didierjean and Kuhn (manuscript) It is magic! https://eprints-gro.gold.ac.uk/21982/3/Kuhn_manuscript.pdf (a18)
- [V] Ninomiya, Iwata, Terai and Miwa (2024) Cognitive load and working memory capacity. https://link.springer.com/content/pdf/10.3758/s13421-023-01448-w.pdf (a19)
- [V] Crooks and McNeil (2009) Increased practice with set problems hinders performance on the water jar task. https://escholarship.org/uc/item/1976z9q8 (a20)
- [V] Lovett and Anderson (1995) Making heads or tails out of how people select problem-solving strategies. https://www.andrew.cmu.edu/user/lovett/cogsci95.html (a21)
- [M] Ollinger, Jones and Knoblich (2008) Mental set and insight problem solving. https://irep.ntu.ac.uk/id/eprint/23048/ (b17)
- [M] DeCaro (2016) Inducing mental set constrains procedural flexibility. https://doi.org/10.3758/s13421-016-0614-y (b18)
- [M] Blech, Gaschler and Bilalic (2020) Why do people fail to see simple solutions? https://doi.org/10.1080/13546783.2019.1685001 (b19)
- [V] Sergeyuk, Titov, Golubev and Bryksin (2023) Overcoming the mental set effect in programming problem solving. https://arxiv.org/abs/2307.06673 (c24; b28 was abstract only)
- [V] Alavi Naeini et al. (2023) Large language models are fixated by red herrings. https://arxiv.org/pdf/2306.11167 (a22, b22, c03 to c05)
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833 (b21, c01, c02)
- [V] Kim et al. (2025) Limitations of LLMs in clinical problem-solving arising from inflexible reasoning. https://arxiv.org/abs/2502.04381 (b23, c06, c07)
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility in clinical problem-solving. https://arxiv.org/abs/2601.11866 (b24, c08, c09)
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636 and https://arxiv.org/html/2601.06636 (a23, b25, b26, c10 to c12; a23 was read through a summarising fetch)
- [M] Guan et al. (2025) Beware of reasoning overconfidence. https://arxiv.org/abs/2512.01725 (b29 abstract only; c13 and c14 are marked opened in the evidence file, with a partly garbled table)
- [V] Jeon, Cho and Shu (2025) PPoGA. https://arxiv.org/abs/2602.00007 (c15)
- [V] Wang et al. (2025) Thoughts are all over the place: underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 (c16)
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c17)
- [V] Wu et al. (2024) Reasoning or reciting? Counterfactual tasks. https://arxiv.org/abs/2307.02477 (c18)
- [V] Tian et al. (2024) MacGyver. https://arxiv.org/abs/2311.09682 (c19, c20)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057 (c21)
- [V] Loewe et al. (2024) Abrupt and spontaneous strategy switches. https://arxiv.org/abs/2302.11351 (c22)
- [V] Gu and Shi (2025) Einstellung Rigidity Index. https://arxiv.org/abs/2510.00475 (b27, c23)
- [V] Liu, Karimnazarov and White (2025) Trapped by expectations. https://arxiv.org/abs/2504.02074 (c25)
- [V] Cheng, Zhu, Zhao and Arora (2026) Contextual drag. https://arxiv.org/abs/2602.04288 (d01 to d03; some table columns garbled)
- [V] Weatherhead, Salim and Belbasis (2025) Illusions of reflection. https://arxiv.org/abs/2510.18254 (d04)
- [V] Gumaan (2026) Feedback that backfires. https://arxiv.org/abs/2608.23651 (d05)
- [V] Choi et al. (2025) Debate or vote. https://arxiv.org/abs/2508.17536 (d09)
- [V] Kim, Garg, Peng and Garg (2025) Correlated errors in large language models. https://arxiv.org/abs/2506.07962 (d10; appendices not checked)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (d17; critiques not opened)
- [V] Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (d18)
- [M] Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/abs/2404.11018 (d19, abstract only)
- [M] Lu et al. (2022) Fantastically ordered prompts. https://arxiv.org/abs/2104.08786 (d20, abstract only)
- [M] Han et al. (2024) Token-budget-aware LLM reasoning. https://arxiv.org/abs/2412.18547 (d21, abstract only)
- Re-opened in the gap pass: Binz and Schulz (d14, d15), Bilalic et al. 2008a (d11, d12), 2008b (d13), Shidara et al. (d06), MedEinst (d07, d08), Haq et al. (d16); URLs as above.
- [M] Saariluoma (1990), Wiley (1998), Frensch and Sternberg (1989), Luchins and Luchins (1959), Ross (1952): cited only through Bilalic et al. and Binz and Schulz; not opened.
