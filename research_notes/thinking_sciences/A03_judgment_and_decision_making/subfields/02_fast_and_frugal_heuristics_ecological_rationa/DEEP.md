# Fast and frugal heuristics, ecological rationality: deep document

*Subfield A03.02. Built from evidence_a-d.jsonl (107 lines), claims.jsonl (K01-K24) and critique.md in this folder. Evidence ids (a01, b12, c05, d06 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested. Date: 2026-11-01.*

---

## 1. What it is

The "adaptive toolbox" is a research programme (Gigerenzer, Todd, Goldstein, Hertwig and colleagues, Max Planck Institute for Human Development, Berlin). It makes three claims.

1. People decide with small, simple rules. Each rule has three building blocks: a search rule (which cue next), a stopping rule (when to stop) and a decision rule (what to choose once stopped).
2. A simple rule can match or beat a complex model on new data, not only on fitted data. Using less information can be better. This is "less is more".
3. Whether a rule is good depends on the structure of the environment, not on the rule in the abstract. This is "ecological rationality".

Main rules:

| Rule | What it does |
|---|---|
| Recognition heuristic (RH) | Two objects, only one recognised: pick the recognised one. |
| Take-the-best (TTB) | Recognition first, then cues in order of validity. Stop at the first cue that tells the objects apart. Choose the object it favours. |
| Take-the-last, Minimalist | Cheaper TTB variants: reuse the cue that worked last, or try cues in random order. |
| Tallying (unit weight) | Count cues for each object. Pick the larger count. |
| Fast-and-frugal tree (FFT) | Binary classification tree with m+1 leaves and an exit at every node. Same building blocks as TTB. |
| Satisficing (Simon) | Take the first option that meets an aspiration level. TTB is built on it. |
| Elimination by aspects (Tversky) | Drop options that fail the first aspect, then the next. Background only; no new data in this folder. |

Why it matters for our agent. The schema gate S0 picks a mode (direct, short reason, step-by-step, checked, open). This subfield gives theory and numbers on when a simple rule is enough, boundary conditions on when it is not, and one structural lesson: classify the environment first, then pick the strategy. G11 (think briefly by default) and G12 (spend by difficulty) are the same idea.

Honest limit. The programme studies binary-cue paired comparison and classification from stored knowledge. An LLM agent solving puzzles is a different setting. The structure of the argument transfers (stop early, few cues, match rule to environment). The specific rules mostly do not (section 9).

---

## 2. History and theories in depth

### 2.1 Roots
- Simon (1955, 1956): bounded rationality, satisficing. Search ends when an option is good enough.
- Tversky (1972): elimination by aspects, a sequential non-compensatory rule.
- Dawes and Corrigan (1974): improper (unit-weight) linear models predict almost as well as fitted ones. Czerlinski et al. later fixed an imbalance in that comparison (b12).
- Einhorn and Hogarth (1975): unit weights can beat fitted weights when predictability is low, objects per cue are few and cues are correlated (b13, a32).

### 2.2 Founding paper: Gigerenzer and Goldstein (1996), Psychological Review (a01-a07, b30)
Task: which of two German cities is larger. Cities above 100,000 inhabitants (the paper text says 83; later papers say 81). 9 binary cues plus recognition. Ecological validities run from 1.00 (national capital, which discriminates only 2% of pairs) down to .51 (East Germany, 27%).

Simulation: 6 cue-knowledge levels (0, 10, 20, 50, 75, 100%) x 84 recognition levels x 500 simulated persons x 3,403 city pairs, about 858 million tests. Recognition validity set to about .80 from a Chicago student survey.

Results (Table 2, mean proportion correct): TTB .658, weighted tallying .658, multiple regression .657, tallying .656, weighted linear .623, unit-weight linear .621, Minimalist .647, Take-the-last .645. Cue values looked up: TTB 5.91, Take-the-last 5.29, Minimalist 5.64; integration rules look up all. With 100% of cue values known: TTB .691, weighted tallying .693, regression .694.

What the headline hides:
- The two linear models lost only because they did not honour the recognition principle. Add it and the gap vanishes (a05). So TTB equals tallying and regression here. It does not beat them.
- The test used the same 3,403 pairs as the simulation. It is not cross-validated prediction (a04). A regression fit R-squared = .87 on the same data (a07).

Less-is-more result (a03, b30): accuracy peaked near 77% when only part of the cities were recognised and fell when all were. Recognition alone peaks near 65% (half the pairs use recognition at 80%, the rest are guesses at 50%). It needs recognition validity set high in advance.

### 2.3 Out-of-sample evidence: Czerlinski, Gigerenzer and Goldstein (1999), via Gigerenzer and Brighton (2009)
20 real data sets, paired comparisons, cross-validated (a08, a09, b12). TTB looked up 2.4 cues on average; regression and tallying 7.7. Tallying and TTB predicted better out of sample than multiple regression, although regression fit better in sample. Ten of the 20 sets came from one regression textbook (Weisberg 1985). No source we have opened the 1999 chapter. One secondary report gives 71% TTB vs 68% regression (c18). On the 83-city set alone, 10,000 random splits gave TTB 72.2, regression 71.9, tallying 71.4 (d14, Wikipedia, unverified). Margins are small. The surviving claim is parity at far lower cost, not a large win.

Anecdote (a08): decision theorists asked to guess predicted TTB would be 5 to 10 points worse than regression. None guessed it would win.

### 2.4 Why: bias-variance and environment structure (a10-a12, b13)
- Error = bias squared + variance + noise. A rule that ignores cue dependencies has high bias but low variance. With small samples variance dominates, so the simple rule wins. With more data flexible models catch up.
- Polynomial demo: 30 noisy points. Fit always improves with degree, but prediction error rises past degree 3.
- A greedy TTB variant (cues ordered by conditional validity) fits better and predicts worse than plain TTB on the city task and in Guttman environments.
- Proofs: if each cue weight exceeds the sum of all later weights (noncompensatory), TTB and the linear model give identical inferences (Martignon and Hoffrage 1999, 2002). Independent cues plus an odds condition: TTB is optimal (Katsikopoulos and Martignon 2006). Highly redundant cues: TTB rivals or beats a confirmation rule (Dieckmann and Rieskamp 2007).
- Tallying wins at low predictability (R-squared about .5 or less), few objects per cue (ratio 10 or less) and correlated cues (a32, b13).
- Chater et al. (2003) and Brighton (2006): TTB vs perceptron, nearest neighbour, GCM, C4.5, CART. Chater et al. fitted on the learning sample and tested on the whole, which favours overfitters. With cross-validation TTB won at every training size on the city task and across 20 data sets (a10). The authors' own group did the reanalysis.
- Bias-variance is exact only for squared error. For classification it is a metaphor (a11).

### 2.5 Recognition heuristic and its decade of dispute (a18-a22, b01-b11, b19, b20)
- RH is ecologically rational when recognition validity alpha = C/(C+W), over pairs with exactly one recognised object, is high. Alpha tracks use: r = .64 over 11 studies (a18, a32); r = .57 over 43 studies (b03).
- Domain split (Pohl 2006): Swiss cities, population alpha .86, adherence 89%; distance from centre alpha .51, adherence 54% (a18, b05).
- Boundary conditions: Oppenheimer (2003) recognised small nearby towns vs fictitious cities, recognised chosen 37%; Chernobyl vs a fictitious city about 30% (a19, b09). Leprosy vs an unrecognised disease: 85% judged the unrecognised one more frequent (recognition validity only about 60% for disease frequency; Pachur and Hertwig 2006). Mixed reference class: 75% vs 89% for a clean set (Pohl 2006).
- Contradicting cues: Richter and Spaeth group means 98% (positive cue), 95% (none), 82% (negative cue) (b01). Voter task: 73% with a negative cue, 87-89% without (b02).
- Use is only slightly higher when recognition is right than wrong: 82% vs 76% (Hilbig and Pohl 2008; b05).
- Individual level: 17 of 28 followed recognition with at most one exception in 32 trials; median 97% with and without contradiction; with contradiction 43% unchanged, 39% less, 18% more. Pachur et al. (2008): 23% always chose the recognised object despite contradicting cues (b10).
- Marewski et al. (2010): five compensatory models with free parameters did not predict better than the parameter-free heuristic (b02). One study set.
- Hilbig and Richter (2011) comment (b06, b07), multinomial r-model on the same data. Aggregate adherence reported as M = .91 (not found in the text on re-check; unverified). Estimated true use r = .80 (SE .01). Deterministic model (r = 1) misfit, p < .001. At individual level (N = 28) the pure-heuristic submodel (r = .96) fit significantly worse for 20 of 28 (71%). Model-free index: 17 of 28 (61%) reliably discriminated recognition-right from recognition-wrong; 11 of 28 (39%) within the 95% CI of zero.
- Castela et al. (2014): 16 data sets; RH use is higher when recognition comes with further knowledge, favouring a memory-state account (b19; abstract and intro read).
- Within-person study (2017, N = 99): 87 of 99 changed recognition reliance between a high-validity and a low-validity domain, but not in line with their own item-level validities; cross-domain correlation 0.38 [0.15, 0.58] (b20).
- Memory models: ACT-R forgetting (Schooler and Hertwig 2005) and MINERVA (Dougherty et al. 2008) both produce less-is-more; the fluency heuristic covers the case where both objects are recognised (a21). Greene et al. (2014): response times follow question frame x number recognised, as magnitude-comparison theories predict (b29, abstract only). Chess re-analysis: 123 people who recognised no player still inferred nationality and Elo above chance, probably from name regularities (b28).

### 2.6 Less-is-more for recognition: contested (a03, a20, b04, b08)
- Found: Goldstein and Gigerenzer (2002), Frosch et al. (2007), groups (Reimer and Katsikopoulos 2004). Informal: about 60% of US students vs about 90% of Germans correct on a US city-size question (Goldstein 1997); BBC radio 65% (New York) vs 82% (London), uncontrolled, as the authors say.
- Not found: Pachur and Biele (2007), Pohl (2006). Pachur (2010) reviewed 10 data sets where recognition validity exceeded knowledge validity: mixed. Validities change with the number recognised, which breaks the constant-validity assumption. Katsikopoulos (2010): the effect can arise without alpha > beta under imperfect memory.
- Status: real in analysis and simulation; weak in human data.

### 2.7 Individual-level tests of TTB (a13, b14, b15)
- Newell, Weston and Shanks (2003): TTB-consistent adherence 75%, 80%, 89% (Exp 1), 92%, 89%, 89% (Exp 2), yet only 33% of participants fully consistent. Newell and Shanks (2003): validities .80, .75, .70, .69; 60 trials with feedback; only 3 of 16 searched in validity order. Proponents say 60 trials are too few to learn the last two orders (100 or more needed). Newell (2005) called the evidence "elusive".
- Bergert and Nosofsky (2007): "vast majority" used stochastic TTB over additive weighting. Hilbig and Richter dispute the majority claim. Cue order was given in those tasks.
- Strategy selection is learned: Rieskamp and Otto (2006), TTB-consistent judgments rose from 28% to 71% in a high-variability environment and fell to 12% in a low-variability one. Dieckmann and Rieskamp (2007): TTB predicted best at high redundancy, compensatory at low. Broeder and Newell (2008): higher IQ went with correct strategy selection (b15; reviews, originals not opened).

### 2.8 Fast-and-frugal trees (a14-a16, a24-a26, b16, b17, c18-c20)
- Martignon et al. (2008): 30 classification problems; logistic regression fit better, FFT cross-validated accuracy close or identical (a14).
- Pneumonia macrolide tree (age, fever duration) 72% vs 75% for a logistic score (a14, b16).
- Coronary care triage (Green and Mehr 1997): a three-question tree beat a regression instrument needing about 50 probabilities and roughly halved physicians' false alarms (a15; secondhand).
- Bail (Dhami 2003): tree 92% and 85% correct (cross-validated) in two courts vs 86% and 73% for weighted additive. Magistrates spent 6 to 10 minutes per case yet said they weighed everything (a16; secondhand; predicts behaviour, not correctness).
- Hiatus heuristic vs Pareto/NBD (Wuebben and Wangenheim 2008): apparel retailer 83% vs 75%; airline 77% vs 74%; CD retailer tie 77% (a17; secondhand).
- FFTrees (Phillips, Neth, Woike, Gaissmaier 2017; a24-a26, b17): ten real data sets, 100 simulations each, 50/50 train/test. Mean cues used: fan 1.85, zig-zag 4.85, max 6.5. Mean balanced accuracy of construction rules: fan .81, zig-zag .75, max .64. Out-of-sample balanced accuracy: SVM .86 (crashed on 2 sets, so mean over 8), FFT .83, regularised logistic regression .83, random forest .83. Worst for FFT: occupancy set. Arrhythmia (68 cases, 280 cues): FFT .66, CART .64, LR .52, RLR .70, NB .71. Heart disease: 1.7 to 1.74 cues on average, weighted accuracy about .88; explicit cue costs (thal $102.90, cp $1.00) allow cheap-first trees.
- Software (Chen, Fu, Krishna, Menzies 2018): tiny trees (5 lines or fewer) better in 43 of 56 comparisons (77%) (c19). Bug reports: LDA topics + FFT matched or beat complex text miners on six NASA sets (c20).
- Counter-example: Hug (2023), career-funding referee judgments, training n = 237: logistic regression slightly better than FFTs; referees seem to use many criteria (c18).

### 2.9 Learned TTB and meta-learned heuristics (a28-a30, b21-b23, c21-c24)
- ABC-TTB (Schulz, Speekenbrink, Meder 2016): learns cue order and direction by reinforcement; accepts proposal trees that explain a data subset. On 81 cities x 9 cues, best overall vs TTB and CART across learning sets from 5 objects up (read from a figure). Compute grows faster than exponentially as the acceptance standard tightens. Learning cost is not in the accuracy comparison.
- Probabilistic TTB (Peltola, Jokinen, Kaski 2019): likelihood model, MCMC; four data sets (homeless, profsalary, city, mileage), 1,000 train/test splits; comparable or better than TTB and ABC-TTB; better than logistic regression except on mileage, the largest set.
- ERMI (Jagadish et al. 2026, arXiv 2509.00116): an LLM writes about 7,000 decision tasks per condition; a small network is meta-learned on them and then picks the strategy people pick. Gini of attribute weights .3399 (SEM .0631) when cue ranking is known (one-reason), .0743 (SEM .0138) when direction is known (equal weights), .1794 (SEM .0333) when unknown (weighted). Posterior model frequency against human data: .7299 (2 attributes), .6284 (4 attributes). The LLM makes the environments; it is not the decision maker.
- Same idea on category learning (c24, abstract and intro only).

### 2.10 Frugal is not fast (a27, b18)
Bobadilla-Suarez and Love (2018): participants were told which heuristic to follow; which country has the higher GDP; 2,000 ms deadline. Exp 1 (unordered, colour-coded cues): tallying faster and more compliant than TTB; about a quarter of the TTB group excluded (26%, 25%) vs 1% and 13% for tallying. Exp 2 (cues ordered by validity, colour removed): TTB faster. Fewer cues does not mean less time.

---

## 3. Core findings with exact numbers

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| TTB matches the best integration rules on city size with fewer lookups | .658 TTB vs .657 regression vs .656 tallying; 5.91 lookups vs all cues; simulated, in-sample | G&G 1996 (a04) | [E] as parity, one environment |
| Linear models lost only for lack of the recognition principle | .623 / .621 vs .658; gap vanished when added | G&G 1996 (a05) | [E] |
| Cheaper variants lose little | Minimalist .647, Take-the-last .645; lookups 5.64, 5.29 | G&G 1996 (a06) | [E] |
| Simple rules predict out of sample as well as regression over 20 data sets | TTB 2.4 cues vs 7.7; CIs +-.4 points per study; exact percentages not in any text read | Czerlinski 1999 via G&B 2009 (a08, b12) | [E] parity; percentages unverified |
| City-set margins under 1 point | TTB 72.2, regression 71.9, tallying 71.4 | d14, d13 | [S] |
| TTB beats ML learners on small training samples | Beats perceptron, kNN, C4.5, CART at every size under cross-validation; edge fades with more data | Brighton 2006, Chater 2003 (a10, b13) | [E], authors' own reanalysis |
| Bias-variance explains the edge | 30 points, error rises past degree 3 | G&B 2009 (a11) | [E] theory |
| Noncompensatory cues: TTB = linear model | Each weight > sum of later weights | Martignon & Hoffrage (a12) | [E] proof |
| Tallying wins in some structures | R-squared <= .5, objects/cues <= 10, correlated cues | Einhorn & Hogarth 1975 (a32, b13) | [E] |
| Less-is-more peak in founding simulation | About 77% at partial knowledge; 65% recognition alone | G&G 1996 (a03, b30) | [E] as simulation |
| Less-is-more in human data | Found in some, not in Pachur & Biele 2007 or Pohl 2006; 10 sets mixed | Pachur 2010 (a20, b08) | [C] |
| Recognition use tracks recognition validity | r = .64 over 11 studies; r = .57 over 43 | a18, b03 | [E] |
| Domain split in RH use | 89% vs 54% (alpha .86 vs .51); about 30% Chernobyl vs fictitious city | Pohl 2006; Oppenheimer 2003 (b05, b09) | [E] |
| Contradicting cues lower RH use | 98% to 82%; 87-89% to 73% | b01, b02 | [E] |
| Pure RH vs mixed use | r-model true use .80; 20 of 28 (71%) differ from pure use; 17 of 28 followed at most one exception in 32 trials | Hilbig & Richter 2011; G&G 2011 (b06, b10) | [C] |
| Strategy use is learned | TTB-consistent 28% to 71% (high variability), to 12% (low); 87 of 99 changed reliance across domains | Rieskamp & Otto 2006; b20 | [E] |
| Individual compliance with TTB low in early tests | 3 of 16 in validity order; 33% fully consistent | Newell & Shanks 2003 (a13) | [C] |
| FFTs near ML accuracy with about 2 cues | FFT .83 vs SVM .86, RLR .83, RF .83; 1.85 cues | Phillips 2017 (a24, a25, b17) | [E] |
| FFT beats regression in some applied sets | Bail 92/85 vs 86/73; pneumonia 72 vs 75 (loses); software 43 of 56 | a16, a14, c19 | [E] mixed; some secondhand |
| Regression beat trees in expert judgment | Logistic slightly better, n = 237 | Hug 2023 (c18) | [S] counter-example |
| Frugal is not fast | Exp 1 and 2 reverse; 2,000 ms deadline | a27, b18 | [S] |
| Longer CoT hurts when the right answer is "cannot be determined" | 77.1% direct, then 66.5, 64.7, 64.4, 62.1 with longer CoT; pre-registered drop 17.3 points [7.7, 25.5]; controls about 82% flat | Bogdan 2026 (a31, c01) | [S] |
| That effect varies by model | Qwen2.5 32B -2.92 [-4.05,-1.81]; 7B -2.86; 14B -2.23; GPT-4o -0.89 [-2.15,+0.39]; Claude Sonnet 4.5 -0.80 [-2.08,+0.48] (Pr<0 = .884); Phi-3.5 +0.98 | Bogdan 2026 (c02) | [S] |
| Reasoning models abstain less on unanswerable items | 20 LLMs, 35k+ items; abstention recall -24% for R1-Distill-Llama-70B and s1.1 32B vs instruct; bigger budgets generally lower it | Fan 2025; AbstentionBench (d08, d09) | [E] direction, 2 groups |
| CoT helps mainly on math and symbolic tasks | Gains: math 14.2, symbolic 12.3, logical 6.9 points; about 95% of MMLU gain on "=" questions | Sprague 2025 (c05) | [E] |
| CoT hurts on human-like "verbal overshadowing" tasks | GPT-4o implicit grammar 87.5 to 64.4 (-23.1, p<.0001); o1-preview 57.7 vs GPT-4o zero-shot 94.0; face recognition worse for all 6 models (GPT-4o 64.0 to 51.2); exceptions task 12.5 vs 2.9 rounds (+331%); Claude 3.5 Sonnet unchanged (65.9 to 67.7) | Liu 2025 (c06) | [E] on 3 of 6 tasks tried |
| Inverse scaling in test-time compute | Sonnet 3.7, Opus 4, o3-mini inverse on spurious-feature regression; Sonnet 4, o4-mini, o3 flat or noisy; Qwen3-32B positive; few-shot fixed much of it | Gema 2025 (c07) | [E] model-specific |
| Overthinking is costly and often useless | +1,953% tokens on 2+3; first round right in over 92% of correct cases; QwQ-32B 3.5 solutions and 741.8 tokens on ASDIV vs 1.0 and 166.4 for Llama-3.3-70B-Instruct | Chen 2025 (c13, d06) | [E] |
| A mode gate saves tokens at flat accuracy | AdaptThink length -50.9% (GSM8K), -63.5% (MATH500), -44.7% (AIME24), accuracy +4.1, +1.4, +1.6; mean -53%, +2.4%. Thinkless: long thinking -50 to -90% | c14, d07 | [E]; both need RL |
| Cascades keep quality at lower cost | FrugalGPT up to 98% cost cut at GPT-4 accuracy (or +4% at same cost); RouteLLM 95% of GPT-4 quality (MT Bench 8.8) at 50% strong-model calls | c15, c16 | [E] cost; trained scorers |
| LLM-written simple rules lose to trained learners | RF 90.2%, NB 88.5%, KNN/LR/DT 86.9%, Claude Sonnet 4.6 rules 80.3% (F1 .833), GPT-4o rules 70.5% (F1 .690) | Alaswad 2026 (c25) | [E] with c26 |
| Walking an LLM-built greedy tree loses to zero-shot | 12 of 12 pairs; 33.19% to 6.33% in one deep case | MYOPIA 2026 (c26) | [E] with c25 |
| Irrelevant context cuts accuracy | At most 18% of baseline-solved problems stay solved under all distractor types | Shi 2023 (d10) | [S] |
| LLMs learn numeric cue weights in context | 50 examples; Claude 3 Opus and GPT-4 above RF, GB, KNN on linear sets | Vacareanu 2024 (d11) | [S] |
| LLMs have internal familiarity signals | Steering the unknown-entity latent gives almost 100% refusal (Gemma 2 2B); semantic-entropy probes AUROC 0.7-0.95; metacognitive information varies by 1.98; rank corr. with accuracy -0.80 (TriviaQA) vs +0.00 (Natural Questions) | d01, d03, d04 | [E] existence; use as cue untested |
| Human-like bias in LLMs is scale-dependent | CRT: humans 38% (41%, n = 3,428 original), davinci-003 5%, ChatGPT-3.5 59%, GPT-4 96% | Hagendorff 2023 (c04) | [E] |
| Tuning installs heuristics | Decoy, certainty, belief bias higher in instruction-tuned models; 15 of 15 base/tuned pairs avoid number endpoints | c11, c27 | [E] |

---

## 4. Mechanisms and models

Written so an engineer can implement them.

### 4.1 Take-the-best
```
inputs: objects A, B; cues sorted by validity v_i descending; values in {+, -, ?}
1 recognition: if exactly one of A, B is recognised -> choose it, stop
2 for each cue i in order:
3    look up A and B on cue i
4    if one is + and the other is not -> choose the + one, stop      (discrimination rule)
5 if no cue discriminated -> guess
validity v_i = (#times cue picks the larger object) / (#pairs it discriminates)
discrimination rate d_i = #pairs it discriminates / #pairs
```
Take-the-last reuses the last cue that worked. Minimalist uses random order. Both can be intransitive when values are missing.

### 4.2 Tallying
Score(X) = number of + cues (or sum of +1/-1). Choose the larger. No weights, no order. Wins with correlated cues, low predictability and small samples.

### 4.3 Recognition heuristic and validity
alpha = C / (C + W) over pairs with exactly one recognised object. Use RH only if alpha is high for that reference class. Mixed or unknown classes lowered use in people (a19) and should lower it in a design. The r-model separates true heuristic use from knowledge-based and guess responses, so mean adherence is not mistaken for pure use.

### 4.4 Fast-and-frugal tree
m+1 leaves for m cues. Every cue node has one exit leaf and one continuation, except the last, which has two leaves. Construction (Phillips 2017):
- `max`: order cues by single-cue accuracy. Weak: .64, 6.5 cues.
- `zig-zag`: alternate the exit direction. .75, 4.85 cues.
- `ifan`/`dfan`: build all 2^(m-1) exit structures over the top cues and keep the best by weighted accuracy (weight sets the miss vs false-alarm trade). .81, 1.85 cues. Median build time ifan 2.61 s vs 0.59 s for max.
Frugality: mean cues used (mcu), percent cues ignored (pci). Cue costs can put cheap cues first.

### 4.5 Learned cue order
- ABC-TTB: reinforce cue order and direction; accept proposals that predict a data subset.
- Probabilistic TTB: noisy likelihood over cue order, direction and thresholds; MCMC; explicit uncertainty.
Both need labelled calibration data. An agent can do the plain version: for each gate feature, record how often it predicted the right mode on a calibration set, then sort by that validity.

### 4.6 Choosing the strategy from environment structure
- One dominant cue or very uneven validities (noncompensatory): one-reason / TTB / small tree.
- Many weak correlated cues, low predictability, few examples per cue: tallying.
- Much data, independent cues, high predictability: weighted or flexible model.
ERMI reproduces this: ranking known -> one-reason; direction known -> equal weights; unknown -> weighted (a30).

### 4.7 Satisficing as a stop rule for an agent
Aspiration level = a code-checked pass. Take the first candidate that meets it; do not search on. This equals G6 and G11. Stop on a signal, not a schedule (G1).

### 4.8 Machine analogues of the stopping rule (c13-c16, d06, d07)
- Cascade (FrugalGPT): call the cheapest model first; stop when a reliability score passes.
- Router (RouteLLM): one up-front decision, strong vs weak model.
- Mode gate (AdaptThink, Thinkless): think vs no-think per query.
All three are trained, not prompted.

### 4.9 Bogdan's account of when to truncate (a31, b26)
Theory: an agent unsure of its own cue precision should stop after k high-validity cues; under "Descending Dominance" that equals TTB. Prediction: longer CoT hurts when meta-uncertainty is high. Per-item regime score: cross-prompt variance (5 paraphrases) + cross-seed variance + calibration error; validated by simulate-and-recover (r above 0.96) on the author's own simulated data only. The cheap reusable part is sample disagreement as an uncertainty proxy.

---

## 5. What holds up

### 5.1 Replicated or independently supported
- Parity of simple and complex rules out of sample on small data at far fewer cues: Czerlinski (via 3 reviews), Phillips 2017 (10 sets), Chen 2018 (software), Martignon 2008 (30 sets). [E] for parity. The programme's own authors ran most of it.
- Bias-variance as the reason; the edge shrinks as training sets grow. [E]
- Environment structure decides which strategy wins. [E]
- Recognition validity predicts reliance (r = .64, .57); people adapt reliance by domain. [E]
- Strategy use shifts with feedback (28 to 71 vs 12). [E]
- In LLMs: more reasoning is unsafe on unanswerable items (two independent groups, same sign) [E direction]; CoT gains concentrate in math and symbolic tasks (Sprague, 100+ papers) [E]; overthinking wastes tokens (Chen) [E].

### 5.2 Failures and contested results
- RH: group adherence looks like pure use; an r-model says about 80% true use and most individuals differ from pure use. Both sides are partisan. No neutral adjudication.
- Less-is-more for recognition: analytic and informal confirmations; mixed human tests.
- TTB at individual level: 3 of 16 in validity order; 33% fully consistent.
- FFT vs regression: loses on pneumonia (72 vs 75) and on Hug's referee data; wins are largest with little data; many applied comparisons were fits, not predictions (b16).
- Time pressure: Exp 1 and 2 reverse.
- LLM-built rules and trees lose to trained learners (80.3, 70.5 vs 90.2) and to zero-shot (12 of 12).

### 5.3 Moderators
- Sample size (small favours simple).
- Cue structure (noncompensatory, redundant, correlated).
- Recognition validity, and whether recognition is tied to the criterion.
- Contradicting cues; reference-class coherence.
- Cue order known or learned (Rieskamp and Otto: 100+ trials).
- Model size and family for CoT effects (Qwen mid-size strong, frontier directional, Phi-3.5 reversed).
- Item type: indeterminate, perceptual and spurious-feature items are hurt by long reasoning; math and symbolic items benefit.

### 5.4 Interventions that worked
- Few-shot examples largely fixed spurious-feature reliance (c07).
- Self-consistency and an "ignore irrelevant information" instruction helped against distractors (d10).
- A tailored system prompt helped abstention but did not fix it (d09).
- Self-training toward shorter solutions cut tokens without hurting accuracy (c13); trained gates cut length 50-90% at flat or higher accuracy (c14, d07).
- Self-help debiasing (model rewrites its own prompt) reported to work in admissions-style prompts (c08; per-model numbers not extracted).

### 5.5 Interventions that did not work
- Larger reasoning budgets on unanswerable items (abstention worse).
- LLM-authored rules or trees in place of data-derived ones (c25, c26).
- CoT on pattern, perception and exception-rule tasks (c06).
- Forced doubt in our own word puzzles: 92% plain vs 75% (schema G1, [O]; not from this folder).

### 5.6 Gaps in the evidence base (critique.md)
- Czerlinski percentages never read in an open text.
- Founding simulation: one environment, simulated knowledge.
- Most applied results are secondhand (a09, a15, a16, a17, a22, a23).
- Peer-reviewed venues were not searchable in the gap search (quota). "No LLM study of the adaptive toolbox" is strong for arXiv, unknown for journals.
- Duplicate evidence lines count once (Bogdan, Jagadish, Phillips, Schulz, Peltola, Bobadilla-Suarez and Love, G&G 1996).

---

## 6. Language models

### 6.1 What has been tested
Nothing in our evidence runs the founding paradigms (city-size paired comparison, cue-ordered TTB, FFT construction) on an LLM (K16; about 28 further arXiv queries, zero hits; d15, d16). The LLM work that touches this subfield falls into groups.

**A. LLMs as environment generators.** Jagadish et al. (2026): an LLM writes about 7,000 tasks per condition; a small network meta-learns on them and reproduces human strategy choice (Gini .3399 / .0743 / .1794; model frequency .7299 and .6284). The LLM is not the decision maker. (a30, b23, c23, c24)

**B. Does thinking more hurt? (nearest analogue of "stop early")**
- Bogdan (2026), single-author preprint: 7 models, 5 CoT lengths, 7,875 responses, 45 items (31 high-uncertainty, 14 controls). High-uncertainty accuracy 77.1% direct, then 66.5 / 64.7 / 64.4 / 62.1% with longer CoT. Pre-registered drop 17.3 points [7.7, 25.5]. Controls about 82%, flat. By model: strong in Qwen2.5 (7B, 14B, 32B), directional in GPT-4o and Claude Sonnet 4.5, inconclusive in Mistral 7B, reversed in Phi-3.5. Limits: author-built items; "correct" means picking "cannot be determined"; LLM judge (Claude Sonnet 4.5, 91.5% raw agreement on a 150-cell pilot); amended pre-registration; no reasoning-trained models. Realised step count reverses the sign (endogenous), so only assigned length is causal. The paper itself says the frontier result "suggests rather than establishes". (a31, b24, b25, c01, c02)
- Fan et al. (2025) and AbstentionBench (Kirichenko et al. 2025): independent groups, same direction. Reasoning models write much longer answers on missing-premise questions and abstain less. Abstention recall falls 24% on average for two reasoning models vs instruct counterparts; larger budgets generally worsen it. Judge identity not verified. (d08, d09)
- Liu et al. (2025): human "thinking hurts" tasks transfer to LLMs on 3 of 6 tried (implicit grammar, face recognition, exceptions). Three others showed mixed or positive CoT effects. (c06)
- Gema et al. (2025): inverse scaling in test-time compute on distractors, spurious features and constraint tracking, with different failure patterns per family. (c07)
- Stechly et al. (2025): in Blocksworld, CoT helps only when prompts are specific to the problem class and fades as size passes the examples. Exact accuracies not extracted. (c17)

**C. Where CoT helps.** Sprague et al.: gains 14.2 (math), 12.3 (symbolic), 6.9 (logical) points; about 95% of MMLU gain is on "=" questions. A gate that skips deliberation outside the symbolic class loses little. (c05)

**D. Mode gates and cascades.** Chen (+1,953% tokens on 2+3; over 92% of correct cases right in round one), AdaptThink, Thinkless, FrugalGPT, RouteLLM. Cost wins from trained or learned gates. A prompt-only gate is untested. (c13-c16, d06, d07)

**E. Rules and trees written by LLMs.** Alaswad 2026 (80.3 and 70.5 vs 90.2 for RF on UCI heart disease). MYOPIA (tree traversal below zero-shot in 12 of 12 pairs; 33.19% to 6.33%; 12.6-point gap between recalling and grounding labels for one model). Qiu et al. (2026) claim LLM-built trees help few-shot tabular classification (abstract and intro only). (c25, c26, c28)

**F. Heuristics and biases in LLMs (not the adaptive toolbox).**
- Binz and Schulz (2023): GPT-3 got 12 of 12 standard vignettes right or with a human-like error; fell for conjunction (Linda) and the hospital problem; all 3 CRT items intuitive-wrong; no base-rate neglect on the cab problem; adversarial rewordings broke it. (c03)
- Hagendorff et al. (2023): CRT, 150 tasks. Humans 38%; davinci-003 5% (80% intuitive-wrong); ChatGPT-3.5 59% (15% intuitive); GPT-4 96% (0% intuitive); CoT in 97% and 84-85% of replies. (c04)
- Macmillan-Scott and Musolesi (2024): 7 LLMs, irrationality not human-like, inconsistent across repeats (abstract only). (b27)
- Suri et al. (2023): ChatGPT shows anchoring, representativeness, availability, framing and endowment effects, matched by humans (d12). Echterhoff et al. (2024): 13,465 prompts; awareness, contrastive, counterfactual, few-shot and self-help debiasing (c08). Lampinen et al. (2024): content effects on NLI, syllogisms and Wason, same direction as humans (c09). Jones and Steinhardt (2022): Codex anchoring and frequency bias (c10). Itzhak et al. (2024): instruction tuning raises decoy, certainty and belief bias (c11). Opedal et al. (2024): some child-like math word-problem biases (c12). Ansari (2026): 18 open-weight lines, tuning removes endpoints in number choice in 15 of 15 pairs (c27).

**G. Familiarity signals (recognition analogue).** Gemma-2 entity-recognition direction, causal for refusal (d01). P(IK) and P(True) (d02). Semantic-entropy probes AUROC 0.7 to 0.95; the black-box version costs 5 to 10x more compute (d03). Confidence informativeness is domain-specific: factor 1.98 across models, rank correlation with accuracy -0.80 on TriviaQA vs +0.00 on Natural Questions (d04). None tested as a take-the-best cue. The shape (valid in one domain, not another) mirrors the human 89% vs 54% split.

**H. In-context learning of cue weights.** Vacareanu et al. (2024): 50 examples, 12 LLMs; Claude 3 Opus and GPT-4 above RF, GB and KNN on linear sets. Numeric regression, not binary-cue order. (d11)

### 6.2 What changed behaviour, and by how much

| Lever | Effect | Where |
|---|---|---|
| Longer CoT on indeterminate items | -17.3 points pooled; -15.0 raw (77.1 to 62.1) | Bogdan |
| CoT on implicit grammar (GPT-4o) | -23.1 points | Liu |
| CoT on exceptions task | 12.5 vs 2.9 rounds (+331%) | Liu |
| Reasoning fine-tuning | -24% abstention recall | AbstentionBench |
| Trained thinking-mode gate | length -44.7 to -63.5%; accuracy +1.4 to +4.1 | AdaptThink |
| RL mode gate | 50 to 90% less long thinking | Thinkless |
| Cascade | up to 98% cost cut | FrugalGPT |
| Few-shot examples | largely fixed spurious-feature reliance | Gema |
| Instruction tuning | more decoy, certainty, belief bias | Itzhak |
| Scale + CoT by default | CRT 5% to 59% to 96% | Hagendorff |
| Irrelevant context | at most 18% of solved items stay solved | Shi |

### 6.3 What this means
- Thinking more is not free and sometimes harmful; the harm depends on model and item type.
- Evidence that "few cues" beats "many cues" for an LLM is thin. That test is open (section 8, T1).
- Mapping "stop after one cue" to "stop thinking early" is an analogy. Bogdan makes it by theory only.
- Frontier models show a directional effect at most in Bogdan; Claude 3.5 Sonnet was unchanged in Liu. Do not assume our model shows it.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = stored history.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Classify task class and environment structure before choosing a mode. A strategy is good only relative to a class. | S0 | [E] | K03; a12, a32, b15 |
| N2 | Use simple modes (direct, short reason) where the class allows. Aim for parity at lower cost, not a win. | S0 | [E] | K01, K23; a04, a08, b12 |
| N3 | Skip deliberation outside symbolic and math classes. CoT gains concentrate there. | S0 | [E] | K11; c05 |
| N4 | Keep direct mode for perception-like, exception-rule and spurious-feature items; long reasoning cut accuracy by about 23 points there. Put those item types in the gate's test set. | S0, G11 | [E] | K12; c06, c07 |
| N5 | Route indeterminate or ill-posed items to a short check; do not grant a bigger reasoning budget. | S0, G11 | [E] direction (size single-source, K10) | K18; d08, d09 |
| N6 | Do not trust one cue (familiarity, a retrieved answer) without domain validity. Reliance should move with measured validity. | G | [E] | K05, K19; a18, b05, b09, d04 |
| N7 | Build the cost side of the gate: log tokens and correctness for direct vs full schema per item. | G7, G12 | [E] | K20; d06, d07 |
| N8 | Order checks by cost and validity; stop at the first decisive one (cascade). | S0, O | [E] as cost result | K13; c14-c16 |
| N9 | If a tree gate is built, derive cue order and thresholds from data, never from the LLM's own guess. | S0 | [E] | K14; c25, c26 |
| N10 | Learn cue order from a calibration set rather than assuming it. | O, memory | [E] | K17; a28, a29, b21 |
| N11 | Report per-item mode use, not only averages. | G7 | [C] origin, cheap rule | K06; b06, b01 |
| N12 | Probe our model with a few classic bias items before relying on a heuristic-based design. | G | [E] model-specific | K15; c04, c11, c27 |
| N13 | Count real tokens and latency of few-cue vs many-cue modes. Fewer cues is not automatically faster. | G7 | [S] | K07; a27, b18, d06 |

N1-N8 restate G11, G12 and S0 with new numbers. They add confidence, not new elements. No new operator is added. Section 4b ("not to add") is respected: no persona voters, no debate, no model-chosen mode without a check.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Cue-limited prompt (top k validity-ordered cues) vs all cues at equal tokens. | S0, O | [S] | K21, K16; d10 indirect |
| T2 | Self-consistency agreement or semantic-entropy proxy as the one-reason cue for the gate, only where AUROC is high. | S0, G | [S] | K19; d01, d03, d04 |
| T3 | "Longer thinking hurts on indeterminate items" on our model, our items, a non-LLM judge. | S0, G11 | [S] | K10; a31, c02 |
| T4 | Data-derived 3-question FFT as the S0 gate vs LLM-chosen mode at equal tokens. | S0 | [S] | K09, K14; a24, c25 |
| T5 | Cascade: direct first, escalate only on a failed cheap check, vs always-full. | S0, O | [S] on prompt-only | K13, K20 |
| T6 | Outcome-feedback updating of which mode is chosen vs fixed mode. | S0, memory | [S] | K08; b15 |
| T7 | In-context learning of noncompensatory cue order from 8, 16, 32 labelled pairs. | O, memory | [S] | K22; d11 |
| T8 | Few vs many examples shift where simple modes stop winning. | S0 | [E] theory, untested on LLMs | K02; a11, a25 |
| T9 | Mean-pure vs mixed per item: is mode use one rule or a mixture? | measurement | [C] | K06; b06 |

---

## 8. Concrete tests on our bench

All arms at equal total tokens (setup, retries and judge calls counted, per G7). Held-out items. Per-item results and bootstrap CIs.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 cue limiting | Paired comparison (city size, 9 binary cues) and one new cue-based task | (a) all cues, (b) top-k validity-ordered cues (k = 1, 2, 3), (c) k random cues | Accuracy; tokens per item | (b) at k = 2-3 within 1-2 points of (a) at fewer tokens; (c) below (b). If (a) is clearly best, drop cue limiting. |
| T2 familiarity as cue | Factual items by task class | Gate by agreement over 5 samples vs always-direct vs always-full | AUROC of agreement vs correctness per class; accuracy at equal tokens | AUROC >= .75 on some classes, near .5 on others (as d04 suggests). Gate pays only on the high ones. |
| T3 indeterminate items | 30+ "cannot be determined" items we write, with matched definite-answer controls | direct, short CoT, long CoT | Correct-abstention rate; control accuracy | Drop of about 10 points direct to long; smaller on frontier models; none on controls. Key-scored, no LLM judge. |
| T4 FFT gate | Mixed bench items tagged by class (symbolic, perceptual, indeterminate, open) | (a) 3-question FFT from calibration data, (b) LLM-chosen mode, (c) always-full, (d) always-direct | Accuracy at equal tokens; false-skip rate | (a) >= (b); both beat (c) when tokens are capped. |
| T5 cascade | Same bench | direct then escalate on failed cheap check vs always-full | Accuracy; tokens; break-even false-skip rate | Same accuracy at 30 to 50% fewer tokens if the check is valid. |
| T6 feedback-learned mode | 100+ items with outcome feedback | fixed mode vs mode chosen by running success per class | Cumulative accuracy; late-run mode shares | Late-run share of the better mode rises (analogue of 28% to 71%). |
| T7 cue order in context | Binary-cue pairs from a noncompensatory generator (weights halving per cue) vs a compensatory one | 8, 16, 32 labelled pairs in context | Share of choices matching first-discriminating-cue vs weighted sum | Shows whether the model learns order or defaults to weighting. |
| T8 sample size | Same task | few vs many worked examples, simple vs full mode | Accuracy gap by example count | Gap favours simple mode at few examples and shrinks with many. |
| T9 per-item usage | Any above | Per-item mode use | Pure vs mixed share | Report only; guards against false "pure" averages. |

Controls: a perceptual set and a spurious-feature set (Liu, Gema style) to confirm the gate sends them to direct mode.

---

## 9. What does not transfer, and why

- Binary cues stored in memory. TTB assumes known cue values. An LLM reads text and builds cues on the fly; no fixed validity order exists unless we construct one.
- The recognition heuristic itself. LLM "recognition" is a trained, partly calibrated internal signal. d01-d04 show it exists; no test uses it as a one-reason cue. An idea to test, not a rule.
- Less-is-more for recognition. Contested in humans; rests on constant-validity and memory assumptions that do not map to LLM training. Skip (K04).
- Effort cost. Humans save effort by looking at fewer cues. An LLM's cost is tokens, and fewer cues may not mean fewer tokens or less latency (a27, K07).
- The founding result. Simulated knowledge, one environment, in-sample, with the recognition principle doing part of the work. Parity, not a win.
- The pure-vs-mixed user debate. Our model has no "person". Only the measurement rule N11 carries over.
- Heuristics-and-biases LLM papers. They measure human-like errors, not the adaptive toolbox, and are model- and scale-specific (CRT 5%, 59%, 96%).
- Trained gates and routers. AdaptThink, Thinkless, FrugalGPT and RouteLLM need RL or trained scorers. Our approach avoids training. The finding transfers; the method does not.
- LLM-written trees. Close cousins of FFTs, but when the model picks cues and order itself they lose (c25, c26). Cue order must come from data.
- Harm from long reasoning at the frontier. Directional at most for Claude Sonnet 4.5 and GPT-4o; reasoning-trained models were not in Bogdan. Overthinking is measured as waste, not always lower accuracy (c13).
- Applied FFT results as proof of accuracy. Several are fits; several are secondhand.

---

## 10. Open questions

1. Does a cue-limited prompt match full-information prompting on the city-size task and a new task at equal tokens? No one has run it (K16, K21).
2. Does Bogdan's effect hold on independent items, another group, a non-LLM judge and current frontier models?
3. What are the exact Czerlinski cross-validated accuracies, and does the edge persist on larger modern data sets with proper tuning?
4. Which observable features (task class, equals sign, answer type, model confidence) predict when direct mode equals the full schema? What is the false-skip cost? (K20 measured savings only.)
5. Does self-consistency agreement or an internal known-entity signal act as a valid single cue, and does its validity change by domain as in 54% vs 89%?
6. Can an LLM learn a noncompensatory cue order from a few in-context examples, or does it default to weighting? No LLM run of the Rieskamp-Otto paradigm exists (K22).
7. Do data-derived FFTs beat LLM-chosen mode routing at equal tokens?
8. What are the real token and latency costs of few-cue vs many-cue modes in an agent?
9. Are there peer-reviewed 2024-2026 papers on LLMs and ecological rationality (Judgment and Decision Making, Cognition, Psychological Review, CogSci) that arXiv search missed?
10. Does mode use look pure at the mean but mixed per item in our own measurements?
11. Is the recognition-heuristic dispute resolvable, or only a modelling choice?
12. Does the 77% less-is-more peak survive when validities change with knowledge, as Pachur (2010) says they do?

---

## 11. Sources

[V] = opened and read this session. [M] = snippet, abstract, secondary report or tool summary only.

| Source | Mark | URL |
|---|---|---|
| Gigerenzer and Goldstein (1996) Reasoning the fast and frugal way | [V] | https://library.mpib-berlin.mpg.de/ft/gg/GG_Reasoning_1996.pdf ; https://doi.org/10.1037/0033-295X.103.4.650 |
| Gigerenzer and Brighton (2009) Homo heuristicus | [V] | https://library.mpib-berlin.mpg.de/ft/gg/GG_Homo_2009.pdf ; https://doi.org/10.1111/j.1756-8765.2008.01006.x |
| Czerlinski, Gigerenzer and Goldstein (1999) How good are simple heuristics? | [M] (via G&B 2009, c18, d13, d14) | https://library.mpib-berlin.mpg.de/ft/gg/GG_Homo_2009.pdf |
| Gigerenzer and Gaissmaier (2011) Heuristic decision making | [V] | https://library.mpib-berlin.mpg.de/ft/gg/GG_Heuristic_2011.pdf ; https://doi.org/10.1146/annurev-psych-120709-145346 |
| Pachur, Todd, Gigerenzer, Schooler, Goldstein (2011) The recognition heuristic: a review | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC3132682/ |
| Gigerenzer and Goldstein (2011) The recognition heuristic: a decade of research | [V] | https://doi.org/10.1017/S1930297500002126 |
| Hilbig and Richter (2011) Homo heuristicus outnumbered | [V] | https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/user_upload/Richter/hilbig_richter_inpress.pdf |
| Castela, Kellen, Erdfelder, Hilbig (2014) Subjective recognition experience | [M] (abstract and intro) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4181781/ |
| Within-person adaptivity in frugal judgments from memory (2017) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC6441105/ |
| Heuristics in judgment tasks with unrecognized elements (2019) | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC7909188/ |
| Greene, Frosch, McCloy, Beaman (2014) Time to decide? | [M] (abstract) | https://pmc.ncbi.nlm.nih.gov/articles/PMC4296670/ |
| Phillips, Neth, Woike, Gaissmaier (2017) FFTrees | [V] | https://journal.sjdm.org/17/17217/jdm17217.pdf |
| Bobadilla-Suarez and Love (2018) Fast or frugal, but not both | [V] | https://pmc.ncbi.nlm.nih.gov/articles/PMC5708146/ |
| Schulz, Speekenbrink, Meder (2016) Simple trees in complex forests | [V] | https://arxiv.org/abs/1605.01598 |
| Peltola, Jokinen, Kaski (2019) Probabilistic Take The Best | [V] | https://arxiv.org/abs/1911.00572 |
| Jagadish, Thalmann, Coda-Forno, Binz, Schulz (2026) Meta-learning ecological priors from LLMs | [V] | https://arxiv.org/abs/2509.00116 |
| Jagadish, Coda-Forno, Thalmann, Schulz, Binz (2024) Human-like category learning | [M] (abstract and intro) | https://arxiv.org/abs/2402.01821 |
| Bogdan (2026) Free Energy Heuristics | [V] | https://arxiv.org/abs/2606.15877 ; https://arxiv.org/pdf/2606.15877 |
| Binz and Schulz (2023) Using cognitive psychology to understand GPT-3 | [V] | https://arxiv.org/abs/2206.14576 |
| Hagendorff, Fabi, Kosinski (2023) Human-like intuitive behavior in LLMs | [V] | https://arxiv.org/abs/2212.05206 |
| Sprague et al. (2025) To CoT or not to CoT | [V] | https://arxiv.org/abs/2409.12183 |
| Liu, Geng, Wu, Sucholutsky, Lombrozo, Griffiths (2025) Mind your step (by step) | [V] | https://arxiv.org/abs/2410.21333 |
| Gema et al. (2025) Inverse scaling in test-time compute | [V] | https://arxiv.org/abs/2507.14417 |
| Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs | [V] (per-model numbers not extracted) | https://arxiv.org/abs/2403.00811 |
| Lampinen et al. (2024) LMs show human-like content effects on reasoning | [V] (exact accuracies not extracted) | https://arxiv.org/abs/2207.07051 |
| Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases | [M] | https://arxiv.org/abs/2202.12299 |
| Itzhak, Stanovsky, Rosenfeld, Belinkov (2024) Instructed to bias | [V] (per-model numbers not extracted) | https://arxiv.org/abs/2308.00225 |
| Opedal et al. (2024) Do LMs exhibit the same cognitive biases in problem solving? | [M] | https://arxiv.org/abs/2401.18070 |
| Chen et al. (2025) Do not think that much for 2+3=? | [V] | https://arxiv.org/abs/2412.21187 |
| Zhang, Lin, Hou, Feng, Li (2025) AdaptThink | [V] | https://arxiv.org/abs/2505.13417 |
| Chen, Zaharia, Zou (2023) FrugalGPT | [V] (numbers not rechecked) | https://arxiv.org/abs/2305.05176 |
| Ong et al. (2025) RouteLLM | [V] (numbers not rechecked) | https://arxiv.org/abs/2406.18665 |
| Stechly, Valmeekam, Kambhampati (2025) Chain of thoughtlessness? | [V] | https://arxiv.org/abs/2405.04776 |
| Hug (2023) How do referees integrate evaluation criteria | [V] (not rechecked in full) | https://arxiv.org/abs/2312.04569 |
| Chen, Fu, Krishna, Menzies (2018) Applications of psychological science for actionable analytics | [V] (not rechecked in full) | https://arxiv.org/abs/1803.05067 |
| Agrawal, Tu, Menzies (2018) Can you explain that, better? | [V] (not rechecked in full) | https://arxiv.org/abs/1804.10657 |
| Alaswad et al. (2026) LLM-generated rules for heart disease prediction | [V] | https://arxiv.org/abs/2609.13192 |
| Mesabah et al. (2026) MYOPIA | [V] | https://arxiv.org/abs/2610.21573 |
| Ansari (2026) 3, 7, 14, 17, 42 | [V] | https://arxiv.org/abs/2610.36178 |
| Qiu et al. (2026) From prompts to trees | [M] (abstract and intro) | https://arxiv.org/abs/2610.10227 |
| Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs | [M] (abstract) | https://pmc.ncbi.nlm.nih.gov/articles/PMC11295941/ |
| Suri, Slater, Ziaee, Nguyen (2023) Do LLMs show decision heuristics similar to humans? | [V] | https://arxiv.org/abs/2305.04400 |
| Ferrando, Obeso, Rajamanoharan, Nanda (2025) Do I know this entity? | [V] | https://arxiv.org/abs/2411.14257 |
| Kadavath et al. (2022) Language models (mostly) know what they know | [V] | https://arxiv.org/abs/2207.05221 |
| Kossen et al. (2024) Semantic entropy probes | [V] | https://arxiv.org/abs/2406.15927 |
| Anon. (2026) Do LLMs know what they know? Metacognitive efficiency | [V] | https://arxiv.org/abs/2603.25112 |
| Davis-Stober, Dana, Budescu (2010) Why recognition is rational | [M] (fetch-tool summary) | https://www.cambridge.org/core/product/7A3B56BC46C2EB4D278BB20769231738/core-reader |
| Thinkless (2025) | [V] (table alignment garbled) | https://arxiv.org/abs/2505.13379 |
| Fan et al. (2025) Missing premise exacerbates overthinking | [V] | https://arxiv.org/abs/2504.06514 |
| Kirichenko, Ibrahim, Chaudhuri, Bell (2025) AbstentionBench | [V] | https://arxiv.org/abs/2506.09038 |
| Shi et al. (2023) LLMs can be easily distracted by irrelevant context | [V] | https://arxiv.org/abs/2302.00093 |
| Vacareanu et al. (2024) From words to numbers | [V] | https://arxiv.org/abs/2404.07544 |
| Hutchinson and Gigerenzer (2005) Simple heuristics and rules of thumb | [V] | https://malagr.de/hutch/hutchpub/behpro1.pdf |
| Wikipedia, Take-the-best heuristic (accessed 2026-11-01) | [M] secondary | https://en.wikipedia.org/wiki/Take-the-best_heuristic |
| Search log: arXiv queries for LLM + recognition heuristic / TTB / FFT (about 28) | [M] negative result | https://export.arxiv.org/api/query |

Secondhand only, not opened: coronary triage (Green and Mehr 1997), bail (Dhami 2003), hiatus heuristic (Wuebben and Wangenheim 2008), Wimbledon (Serwe and Frings 2006), recognition-based investing and elections (Ortmann 2008, Boyd 2001, Gaissmaier and Marewski 2010), Rieskamp and Otto (2006), Dieckmann and Rieskamp (2007), Broeder and Newell (2008), Newell and Shanks (2003), Newell, Weston and Shanks (2003), Bergert and Nosofsky (2007), Pachur (2010), Chater et al. (2003), Brighton (2006), Martignon et al. (2008). All known through the reviews above.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 13 established claims: 8 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A03.02-K05** (number corrected). 54% vs 89% (Pohl 2006) and about 30% (Oppenheimer) check out, but the contradicting-cue figure is 95% to 82% mean (Richter & Spaeth; median stayed 97%); 98% belongs to Newell & Fernandez, where it fell to 64%. Corrected claim: People use the recognition heuristic selectively: adherence drops when recognition is not tied to the criterion (54% for distance vs 89% for population in Pohl 2006; about 30% choosing the recognized object for Chernobyl vs a fictitious city) and when a contradicting cue exists (Richter & Spaeth: mean adherence 95% to 82%, median unchanged at 97%; Newell & Fernandez: 98% to 64%).
- **A03.02-K11** (number corrected). Sprague et al. give average CoT gains of 14.2 for symbolic, 12.3 for math, 6.9 for logical; the claim swaps the labels. The 95% MMLU equals-sign figure is confirmed. Corrected claim: CoT helps mainly on math and symbolic tasks (average gains 12.3 points for math and 14.2 for symbolic); elsewhere direct answering is near equal, and as much as 95 percent of the MMLU gain is on questions containing an equals sign. This supports a gate that skips deliberation on non-symbolic items.
- **A03.02-K15** (reworded: the sources support less). Itzhak et al. find decoy effects mixed (and the T5 to Flan-T5 certainty rise not significant) and cannot separate RLHF from instruction tuning; Ansari's 15 of 15 is for distributions becoming less uniform, while endpoint avoidance is reported as medians (base already avoids endpoints at 0.30-0.60 of interior rate, tuned near 0). Corrected claim: Tuning-installed heuristics in LLMs are measurable: instruction-tuned or RLHF models show higher certainty-effect and belief-bias scores than their pretrained counterparts (decoy-effect results are mixed, and RLHF cannot be isolated from instruction tuning), and across 15 base/tuned pairs instruction tuning made number choice less uniform in all 15, with tuned models almost never returning the endpoints (median ratio to interior rate near 0 vs 0.30-0.60 for base). Scale changes human-like heuristic errors non-monotonically (CRT: davinci-003 5 percent, ChatGPT-3.5 59, ChatGPT-4 96).
- **A03.02-K17** (reworded: the sources support less). Schulz et al. (2016) test only the 81-city data (plus simulated data) and compare TTB, ABC-TTB and CART, not logistic regression; the four datasets (homeless, profsalary, city, mileage) and the logistic-regression comparison are Peltola et al. (2019), where regression wins on mileage. Corrected claim: Learned take-the-best variants recover cue order from data: ABC-TTB (Schulz et al. 2016) outperforms classic TTB and CART on the 81-city data set (read from a figure) and recovers simulated TTB structure, and probabilistic TTB (Peltola et al. 2019) performs comparably or better than classic TTB and ABC-TTB and better than logistic regression on three of four small benchmarks (homeless, profsalary, city; logistic regression wins on mileage, the largest). These are model papers on few benchmark data sets, with Peltola's reusing Schulz's data.
- **A03.02-K18** (reworded: the sources support less). AbstentionBench's budget sweep (s1.1 32B, R1 Distill 'same trend') shows abstention not improving on GSM8k-Abstain and worsening on UMWP while accuracy rises, and o1 reasoning effort was mixed, so 'generally worsen' is too strong. Corrected claim: More reasoning is not safe on unanswerable or ill-posed items: reasoning models write much longer answers on missing-premise questions (Fan et al.), reasoning fine-tuning lowers abstention by 24% on average across 20 LLMs (Kirichenko et al.), and bigger reasoning budgets in a sweep on two models did not improve abstention (no gain on GSM8k-Abstain, a decline on UMWP) while accuracy rose. Two independent groups, same direction, different designs.
- **A03.02-K01** (now single-source: only one opened source, code check).
- **A03.02-K03** (now single-source: only one opened source, code check).
