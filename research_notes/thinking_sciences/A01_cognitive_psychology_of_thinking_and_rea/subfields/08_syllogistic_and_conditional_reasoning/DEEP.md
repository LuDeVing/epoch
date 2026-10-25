# Syllogistic and conditional reasoning: deep document

Series: A01 cognitive psychology of thinking and reasoning, subfield 08. Written 2026-10-21 from evidence_a-d.jsonl (ids a01-a29, b01-b29, c01-c27, d01-d24), claims.jsonl (A01.08-K01-A01.08-K36) and critique.md. Earlier documents in this series (mental models, Wason, content effects, belief bias, dual process) are not repeated. Where they overlap, this file only points to them.

Reading marks. [E] established, [S] single source, [C] contested. [V] source opened, [M] snippet or secondary table only. Evidence ids in brackets, e.g. (a03).

---

## 1. What it is

Two tasks, one family: draw or judge a conclusion from premises that contain quantifiers or "if".

**Categorical (quantified) syllogisms.** Two premises, each of one of four moods, linking three terms A, B, C.
- Moods: A "All X are Y", I "Some X are Y", E "No X are Y", O "Some X are not Y".
- Figure is the order of the terms. Figure 1: A-B, B-C. Figure 2: B-A, C-B. Figure 3: A-B, C-B. Figure 4: B-A, B-C.
- 4 x 4 moods x 4 figures = 64 premise pairs. Under the usual scoring 27 have a valid conclusion linking A and C. 37 have none, so the right answer is "nothing follows" (NVC). (a23, a01)
- The 27 and 37 depend on existential import (section 2.7). 24 valid forms with it, 15 without. The "27" count includes conclusions that need Gricean implicature.

**Conditional inference.** One rule "if p then q" plus a fact.
- Modus ponens (MP): p, so q. Valid.
- Modus tollens (MT): not-q, so not-p. Valid.
- Affirming the consequent (AC): q, so p. Invalid under the material reading.
- Denying the antecedent (DA): not-p, so not-q. Invalid under the material reading.
- Related tasks: suppression (extra premises), probability of "if" judgments, negation manipulations ("if not-p then q"), and the "new paradigm" that treats "if" as probabilistic, not truth-functional.

**Why it matters for our agent.** These are the cleanest tasks where a code check can decide validity. Humans have a well-measured error map for them (stable across labs). Language models show both human-like errors and their own. The subfield gives us test items for S4, a list of traps for S1 and S0, and a case study in when a formal solver helps and when it hurts.

SUBFIELDS.md row: "Quantifiers, 'if', atmosphere and matching effects; test items for S4." This document extends that to a full set of measured effects and agent tests.

---

## 2. History and theories in depth

Dates before 1999 below are background knowledge of the field. The meta-analysis (a01-a05, d08-d11) is the main opened source for the human syllogism history. Older primary papers were not opened.

### 2.1 Heuristic theories (early to mid 20th century)

- **Atmosphere** (Woodworth and Sells 1935; Begg and Denny 1969 rule). The "mood" of the premises sets the mood of the conclusion.
  - Any negative premise gives a negative conclusion.
  - Any "some" premise gives a "some" conclusion.
  - Otherwise a universal affirmative.
  - Weakness: a conclusion always fits the atmosphere, so it can never predict a correct "nothing follows". Most valid conclusions also fit it, so it looks better than it is. Only invalid items separate theories. "there is always a conclusion that fits the atmosphere of the premises" (a05).
- **Matching** (Wetherick and Gilhooly 1995). Take the mood of the most conservative premise, ranked E, O, I, A (a05).
- **Illicit conversion** (Chapman and Chapman 1959). Read "All A are B" as "All B are A", and "Some A are not B" as "Some B are not A". It has a probabilistic base in ordinary speech (a23).

### 2.2 Formal-rule theories

- **PSYCOP** (Rips). Natural-deduction rules plus Gricean implicatures. Errors come from missing rules or lost steps. With implicatures it reaches the 27 valid problems (a23, a24).
- **Verbal reasoning model** (Polk and Newell). Errors come from encoding and re-encoding of the premises, with no counterexample search. Best overall fit in the meta-analysis (84% correct predictions) but unstable across data sets (a03, a24).

### 2.3 Model theory (Johnson-Laird and colleagues)

- People build a small number of mental models of the premises. They read off a candidate conclusion from the first model. Careful reasoners then search for a counterexample (an alternative model). If one is found, the conclusion is dropped. If none is found, it stands. If no conclusion holds in all models, "nothing follows".
- Hard problems need more models. That predicts difficulty and varied wrong answers (a02, b04).
- mReasoner (2020 update): a stochastic program that builds an initial model and optionally searches for counterexamples. Fit to the meta-analysis data r = 0.82 (a21). Designed by the proponent group.
- See the mental-models document in this series for the general theory.

### 2.4 Probability heuristics model (PHM; Chater and Oaksford 1999)

- Quantifiers are treated as probability statements, ordered by informativeness: all > most > few > some > none > some-not (a06).
- Four heuristics, usable without testing validity:
  - **min**: the conclusion has the quantifier type of the least informative premise.
  - **p-entailment**: if min's conclusion type is not available, fall back to a weaker type that it implies.
  - **attachment**: the subject of the conclusion comes from the end term of the min premise.
  - **max**: confidence rises with the informativeness of the most informative premise.
- Fit: five data sets, 320 data points, 6 fitted parameters, r(318) = .90, RMS .30, over 80% of variance. The min heuristic explains 95.17% of the non-NVC conclusions on invalid problems. People were logically correct on only 51.8% of trials in the pooled sets (64.9% valid, 46.8% invalid) (a07).
- Min matches the p-valid conclusion type on 22 of 31 p-valid classical syllogisms, 32 of 38 once "most" and "few" are added (a06).
- Follow-up: "few" did not behave as more informative than "some" in the original experiments. Oaksford, Roberts and Chater (2002) fixed this by splitting positive from negative quantifiers (three experiments, N = 81, 40, 50; Kendall W .84 in Exp 2). This is a rescue after the fact (a09).
- Critique (Khemlani and Johnson-Laird): assumes people cannot test validity, so it cannot explain why some people are much more accurate (a06).

### 2.5 The 2012 meta-analysis (Khemlani and Johnson-Laird)

The central summary of the human syllogism field. Read in the author copy (d08-d11).
- Twelve theories reviewed in three families (heuristic, formal-rule, model/diagram). Seven had predictions usable for scoring. Euler circles, Venn diagrams, verbal substitution, monotonicity and source-founding were left out (b01, d08).
- Six data sets, all 64 premise pairs, participants drawing their own conclusions: Johnson-Laird and Steedman 1978 (two tests, N = 20 each), Johnson-Laird and Bara 1984 (N = 20, Milan), Bara et al. 1995 (two groups of 20, Florence), Roberts et al. 2001 (N = 56). Total N = 156 (d08).
- Verdict: "None of the 12 theories provides an adequate account" (a01).
- Reliability is high. Kendall W = .86 for the 27 valid problems, .64 for the 37 NVC problems, .45 for response entropy. Entropy against accuracy r = -0.52 (a02, d08).
- A response counted as reliable if given on at least 16% of trials (chance 1/9; 9 responses = 4 moods x 2 term orders + NVC) (a02).
- Each theory trades hits (predicts what people say) against correct rejections (does not predict what they do not say). See table in section 3 (a03, d09).

### 2.6 Conditional inference: from truth tables to probability

Background (not opened): Wason-era work showed the asymmetry MP > MT, and AC and DA drawn though invalid. Evans (1977) and later negations-paradigm work found negative-conclusion bias, strongest for DA and MT (a28, secondary).

- **Suppression** (Byrne 1989). An extra premise changes which inferences people accept. Argued to be a challenge for formal-rule theories, because a valid MP is withheld (a13, a14). Accounts:
  - Non-monotonic logic programs with abnormality conditions (Stenning and van Lambalgen 2008; weak completion semantics) (a14).
  - Answer-set programming. Handles AC/DA suppression but not additional-antecedent MP suppression by completion alone (a15).
  - Reinterpretation of what the premises mean (b10). More people considered an outside explanation, so fewer concluded with certainty (33% Byrne, 44% Dieussaert, against 92% and 69% in the plain group).
  - Counterexample retrieval from memory (De Neys et al. 2003): acceptance falls with each retrieved disabler (MP, MT) or alternative (AC, DA) (b11).
- **Probabilistic account** (Oaksford, Chater and Larkin 2000). See section 4.2.
- **New paradigm** (Evans and Over; Oaksford and Chater; Over; Singmann, Klauer and Over). Replace the truth-functional "if" with the conditional-probability view: P(if p then q) = P(q|p) ("the Equation"). Reasoning from uncertain premises is then judged by probability logic, not truth tables (b13, b14).
- **Mental-model rival** (Girotto and Johnson-Laird 2004). People represent "if" with few explicit models, so P(if) and P(q|p) should diverge (a18).
- **Relevance** (Skovgaard-Olsen, Singmann, Klauer 2016; van Rooij and Schulz 2019). The Equation weakens when p is irrelevant to q. A dependence between p and q is needed (b18, a20).

### 2.7 Existential import

"All A are B" may or may not imply that some A exist.
- Traditional (Aristotelian) reading: yes. 24 syllogisms valid.
- Modern (Boolean) reading: no. 15 valid. The 9 extra forms are the "import-dependent" moods.
- Datasets rarely state which they use (c09). Provers such as Prover9 do not assume import and need a patch (d15).
- The human data of the 2012 meta-analysis neutralised it by telling participants "that individuals of all relevant sorts exist" (d11).

### 2.8 Individual differences

- Accuracy ranges from 15% to 85% correct on valid problems across people (a22).
- Group means: 55% valid conclusions at a selective US university, 37% at a non-selective Italian university (a22, b05).
- Some never look for alternative models and rarely say NVC. Others search but cannot state a conclusion common to all models and say NVC too often (a22).
- Working-memory correlation about .7 is unpublished and second hand (a22).
- For conditionals, people split into conditional-probability responders (n = 69) and conjunctive responders (n = 46) (b15).

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested. "Src" gives evidence ids. Numbers marked (sec) come from a secondary table.

### 3.1 Categorical syllogisms, humans

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Difficulty is a property of the problem. Ranks agree across six data sets | Kendall W .86 (27 valid), .64 (37 NVC), .45 (entropy); entropy vs accuracy r = -0.52; N = 156 in six data sets | Khemlani and Johnson-Laird 2012; a02, b02, d08 | [E] (one meta-analysis, but six independent data sets; re-checked in author copy) |
| Average human accuracy | 44.63% on 27 valid items; 40.97% (quoted) or 41.05% (recomputed) on 37 NVC items | KJL 2012; d11, c04 | [E] |
| Easiest and hardest items | Easiest valid (All B are A; Some C are B) 90% correct. Hardest valid (All B are A; None of the C is B) 1% correct. Easiest NVC (None A are B; None C are B) 76% say NVC. Hardest NVC (Some B are A; All C are B) 12% say NVC | a02, b04, d11 | [E] |
| Hard items give more varied wrong answers | Response entropy about 1 bit for easy items, over 2 bits for hard ones | b04 | [E] |
| Figural effect on direction of conclusion | Valid conclusion that fits the bias drawn by about 80%, one that violates it by about 20%. Example: 15 of 17 wrote "Some A are C" for Some A are B; All B are C. 16 of 17 wrote "Some C are A" for the reversed order | KJL 2012; a04, b05, d10 | [E] (3 sources) |
| Figural effect on correct NVC | Fig 1 50%, Fig 2 57%, Fig 3 70%, Fig 4 86% (Jonckheere z = 3.32, p < .001; Johnson-Laird and Bara 1984, 10 s limit) | a04, d10 | [S] one study quoted in the meta-analysis |
| Theory scores: mental models | Hits 95%, correct rejections 74%, correct predictions 78% | a03, d09 | [S] |
| Theory scores: verbal models | Hits 63%, rejections 90%, overall 84%; I2 = 52%, Q = 10.69, p = .06 | a03, d09 | [S] |
| Theory scores: conversion | Hits 44%, rejections 93%, overall 83% | a03, d09 | [S] |
| Theory scores: atmosphere | Hits 51%, rejections 85%, overall 78% | a03, b06, d09 | [S] (table text was scrambled; rows matched by text) |
| Theory scores: PSYCOP, PHM, matching | PSYCOP 44 / 85 / 77; PHM 52 / 79 / 73; matching 59 / 74 / 71 (hits / rejections / overall) | a03, d09 | [S] |
| Family aggregates | Model-based 76% vs heuristic-based 66% correct predictions. Mental-model hits show publication-bias signal (z = 2.03, p < .05) | a01, b03, d09 | [S] |
| "Only" premises defeat atmosphere | Both premises "only": 16% of conclusions contained it. One premise "only": 2% | a05 | [S] |
| PHM pooled fit | r(318) = .90, RMS .30, over 80% variance, 6 parameters, 320 points. Min heuristic explains 95.17% of non-NVC conclusions on invalid items. Logically correct 51.8% overall (64.9% valid, 46.8% invalid) | Chater and Oaksford 1999; a07 | [C] (fit is not mechanism; rivals fit too) |
| PHM attachment | All 32 syllogisms in figures 1 and 4 agree. Figures 2 and 3: 22 of 24 conform, 1 violates, 1 tie | a08 | [S] |
| Sample differences | 55% valid conclusions (selective US university) vs 37% (non-selective Italian); individuals 15% to 85% | a22, b05 | [E] |
| Existential import changes the count of valid forms | 24 valid (traditional) vs 15 (modern); 27 valid among 64 used in the human meta-analysis with import neutralised | a23, c09, d14 | [E] |

### 3.2 Conditional inference, humans

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Standard abstract rates, "if p then q" | MP 100, DA 55, AC 74, MT 61 (percent endorsing; N = 120) | Evans et al. 2007; b16 | [E] pattern; single table |
| Negation changes rates | "If not-p then q": MP 96, DA 55, AC 81, MT 35. "If not-p then not-q": MP 95, DA 40, AC 74, MT 39. "If p then not-q": MP 99, DA 37, AC 68, MT 64 | b16 | [E] direction (older negation literature, a28, a12); numbers [S] |
| Suppression, Byrne 1989 (secondary tables) | MP: 96% simple, 96% alternative, 38% additional. AC: 71% simple, 13% with alternative (a snippet said 16%). DA: 46 / 4 / 63. MT: 92 / 96 / 33 (plain / alternative / additional). Percentages are share drawing the conclusion | a13, a14, b08 | [E] direction; sizes (sec) |
| Suppression replication, Dieussaert et al. 2000 | MP 88 / 93 / 60; DA 49 / 22 / 49; MT in additional group 44 | b09 | [E] direction replicates; size about half (MP drop 58 points vs 28) |
| Certainty drops with a plausible exception | Share concluding with certainty in additional group: 33% (Byrne), 44% (Dieussaert); plain group 92% and 69% | b10 | [S] |
| Suppression across 15 scenarios (Neth and Beller 1999, N = 50) | Only p/q: MP 92.7, MT 75.3, AC 58.0, DA 62.0. Plus alternative: 92.7, 78.0, 16.0, 14.0. Plus additive: 64.0, 46.7, 50.0, 47.3 (percent, out of 150) | a16 | [E] |
| Necessary condition raises AC and DA | 92.5% vs 40.0% (chi2 = 68.91, p < .01). Sufficient condition raises MP/MT 91.7% vs 81.7% (chi2 = 4.01, p < .05). Insufficient condition did not reduce MP/MT (77.5% vs 81.7%, n.s.) | a16 | [S]; only the "raise" predictions held |
| Wording choice follows formal direction | 68.2% of choices matched the formally appropriate wording (79.2% only p/q, 64.0% alternative, 61.3% additive) | a17 | [S] |
| Suppression is graded in the number of counterexamples (De Neys et al. 2003) | Exp 1: 178 students, 4 discarded; AC with alternatives linear trend F(1,87) = 20.84; MP with disablers F(1,85) = 20.46; MT with disablers F(1,85) = 16.02 (all p < .001). DA with alternatives: no clear effect (Rao R(3,85) = 1.86, p < .15). Disabler presentation raised AC, Rao R(4,82) = 4.67, p < .002 | b11, b12; corrected in critique | [E] for MP, MT and AC; DA not supported |
| High-probability conclusion effect (Oaksford, Chater and Larkin 2000) | Exp 1 (N = 30): overall F(1,87) = 22.90, p < .0001; MT F = 5.78, p < .025; MP F = 3.53, p = .064. Converse order DA' > AC' > MT' > MP'. Exp 2 (N = 25): F(1,72) = 28.91. Exp 3 (N = 20): AC F(1,57) = 4.62, MT F(1,57) = 4.54, DA n.s. (p = .26) | a10-a12, a29 | [C] (effects replicate within the lab; the DA and MT handling is disputed) |
| P(if p then q) tracks P(q|p) | r = .84 vs r = .61 for the conjunction (N = 30). Mixed model: P(q|p) b = .78, F(1,88.14) = 86.81, p < .001; conjunction b = .00; material b = -.01 | Singmann et al. 2014; b13 | [C] |
| Rival: people do not equate them | Girotto and Johnson-Laird (2004), Exp 1 N = 48: conditional probability correct 68% vs complete probability of the conditional 17% (z = 11.8, p < .00005). Exp 2 N = 20: 87% vs 32%. Oberauer and Wilhelm (secondary): 52% equal in Exp 1B, 23% consistently in Exp 1A. Evans et al. 2003 (secondary): 54% rating with 2 diamonds, 37% with 12 | a18, a19 | [C] |
| Two reader types | N = 120, 115 classified: conjunctive n = 46, conditional n = 69. Ability (AH4) 91.65 vs 98.07, t = 2.45, p = .013. Higher ability gives fewer DA (t = 2.63) and AC (t = 2.81) fallacies, not more MT | b15, b17 | [S] |
| Relevance weakens the Equation | Slope of P(if) on P(C|A): positive .78 (CI .71-.85), negative .61 (CI .52-.71), irrelevant .43 (CI .35-.52). t(41.53) = 3.26; t(53.13) = 6.22. 577 completed, 348 kept | Skovgaard-Olsen et al. 2016; b18 | [S] |
| Concessive "even if" follows the Equation better than "if" | Direction only; slope numbers not extracted | b19 | [S] |

### 3.3 LLM findings (summary; detail in section 6)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Strong 2024 LMs beat average humans on syllogisms, not by much | Best PaLM 2 about 75% vs human about 50%; largest model slightly below second largest | Eisape et al. 2024; c01, b24 | [E] |
| LLMs avoid "nothing follows" (non-reasoning models) | Eisape: near 0% on the 37 NVC items (zero-shot CoT). Bertolazzi: best 32.50% (LLaMA-3 70B instruct). Ando and Mineshima: "neutral" 63.2% (Claude 3.5 Sonnet), 25.3% (GPT-4o-mini) | c03, b25, c04, d21 | [C]: reasoning models look different (binary tasks) |
| Atmosphere predicts LLaMA-3 8B output | 92.31% of correct valid conclusions, 82.97% of invalid-schema errors, 62.79% of valid-schema errors | Bertolazzi et al. 2024; a26, c06 | [S] (one model) |
| Instruction tuning trades valid for invalid accuracy | LLaMA-3 70B base: 58.89% valid, 30.63% overall. 70B instruct: 54.44% valid, 32.50% invalid, 41.25% overall. 8B instruct: 78.15 valid, 30.28 invalid, 50.00 overall | c04, critique check 1 | [E] |
| Modus tollens is hardest | Soft accuracy MP .59, disjunctive .54, MT .31 | Wang and Shi 2025; c15 | [E] (several sets) |
| LLMs rarely retract on added requirement | Belief-R: Belief Update accuracy about 10 to 22% (named API and Llama-3 models), maintain 35 to 92% | Wilie et al. 2024; d01-d03 | [S] |
| Reasoning-tuned models near ceiling on binary validity | o3 and GPT-5 recall on invalid 99.6 to 100%; countermodel construction o3 99%, Qwen3-32B 89% | Zang 2026, Rabern 2026; d12, d18 | [S] each; binary tasks |

---

## 4. Mechanisms and models

Written so an engineer can implement them as code checks, predictors or test generators.

### 4.1 Syllogism representation and validity check

Encode each premise as (mood, subject term, predicate term). Moods A, I, E, O.
- A: all S are P. I: some S are P. E: no S are P. O: some S are not P.
- A conclusion is (mood, end term 1, end term 2). Eight candidate conclusions (4 moods x 2 directions) plus NVC give 9 responses, as in the human data (a02).
- Validity by model enumeration (exact, no theorem prover needed): with three terms there are 8 regions of a Venn diagram. Assign each region empty or non-empty (2^8 assignments). A candidate conclusion is valid if it holds in every assignment that satisfies both premises. Under the traditional reading, add the constraint that each term set is non-empty (import). Counting valid forms gives 15 (modern) or 24 (traditional). The count of 27 in the meta-analysis comes from PSYCOP-style implicatures (a23); do not rely on it as a clean logical count. Use the benchmark's own key.
- Lookup alternative: parse mood and figure, look up the pair in a table of valid forms (24 or 15). Zong and Lin (2024) describe this as a cheap structural check (c08). Mood detection by a model reached 87.9% on 116 textbook items, figure only 48.3%, full configuration 44.8% (c08), so the parse is the weak link, not the table.
- Contradiction check (a27): an answer set may not contain A with O, or E with I, or NVC with another conclusion. Code can reject these without a model.

### 4.2 Heuristic predictors (use as bias detectors, not as policies)

- **Atmosphere predictor.** Rule from section 2.1. Code computes the atmosphere conclusion. If the model's answer equals it and the validity check disagrees, flag a shallow-pattern answer (a05, c06).
- **Matching predictor.** Take the most conservative premise by rank E, O, I, A.
- **PHM min / attachment predictor** (a06, a08).
  1. Rank quantifiers by informativeness: A > I > E > O (for the four classical ones). In a combined "all > most > few > some > none > some-not" scale for generalised quantifiers.
  2. Conclusion mood = mood of the least informative premise (min). If invalid, use the p-entailment fallback (a weaker form).
  3. Attachment: the conclusion's subject is the end term of the min premise. If both premises have the same type, no prediction (these are the 8 same-type syllogisms in figures 2 and 3 where people say NVC) (a08).
  4. Confidence grows with the informativeness of the max premise. PHM fitted order parameters for conclusion direction: pA 55.30, pI 24.08, pE 15.97, pO 15.00 (a07).
  A model answer that follows min but is logically invalid is the typical human-like error (a06).
- **Conversion predictor.** Swap subject and predicate in A and O premises, recompute validity. If the model's answer is valid only under conversion, tag a conversion error (c06, c13: conversion predicts 58.33% of LLaMA-3 mistakes, 50.70% of Pythia mistakes).
- **Figure normalisation.** Re-state the same problem in the term-swapped order. Disagreement between the two is a free inconsistency signal (c02).

### 4.3 Mental-model counterexample search (the method behind the best human results)

1. Build the initial model(s) of the premises.
2. Read a candidate conclusion from the model.
3. Try to build a second model that satisfies the premises and falsifies the candidate.
4. If found: discard the candidate and read the next. If not: accept. If no candidate survives: NVC.

The agent version is the same loop. Code enumerates the 2^8 region assignments (section 4.1) and returns a concrete counterexample or none. The model then only has to write the candidate and read the counterexample back. Humans who never search rarely say NVC; humans who search but cannot hold a common conclusion say it too often (a22). The counterexample step is what separates the two. mReasoner has a parameter for this (System 2) and larger LMs fit with higher values of it (b26).

### 4.4 Probabilistic conditional model (Oaksford, Chater and Larkin 2000)

Treat "if p then q" as a 2 x 2 table over p and q.
- Parameters: a = P(p), b = P(q), e = P(not-q given p) (exceptions).
- MP endorsement = P(q|p) = 1 - e.
- DA = P(not-q | not-p). AC = P(p | q). MT = P(not-p | not-q). All follow from a, b, e by Bayes' rule (a10).
- Predictions: a high-probability conclusion effect for DA, AC and MT (a negated category is large, so negative conclusions look better); a low-probability premise effect for AC and DA; opposite effects for the converse inferences. With no exceptions MT is drawn regardless of probabilities (a29).
- Held: first and third predictions. Second was weak or an artifact in Exp 2 and 3 (a29).
- Implementation: given stated frequencies, compute the four conditional probabilities in code and compare with the model's acceptance. Use it as a calibration reference, not as ground truth for validity.
- Caveat: the handling of negated propositions for DA and MT is challenged by Verschueren and Schaeken, seen only as an abstract record [M] (critique). Treat the model as contested for the denial inferences (A01.08-K17).

### 4.5 Probability of the conditional

Candidate readings of "P(if p then q)":
1. Conditional probability P(q|p) (the Equation).
2. Conjunction P(p and q).
3. Material conditional P(not-p or q).
4. Complete-model readings (Girotto and Johnson-Laird): the proportion of all relevant possibilities where the conditional is true.

Test design: a pack of cards (e.g. 30 cards, 6 yellow circles, a number of yellow diamonds). Ask: "How likely is it that if a card is yellow it is a circle?" and "Given a yellow card, how likely is it a circle?" The set of explicit counts lets code compute all four readings and score which one the answer is nearest to (a18, a19). In Singmann et al. (everyday believable conditionals) only P(q|p) mattered (b13). In Girotto and Johnson-Laird's card problems it did not (a18). The two designs differ in materials and instruction, so the disagreement is partly a design difference.

Relevance extension: add the relevance manipulation (positive, negative, irrelevant) so the antecedent does or does not change the probability of the consequent. Slope on P(C|A) is the measure (b18).

### 4.6 Defeasible rules (suppression logic, code-side)

Encode a rule as: q if p and not abnormal(r). Each extra premise adds or removes abnormality conditions.
- Additional requirement: "if r then q"-type premise where r is also needed. It adds an abnormality condition (r must hold). MP is now withheld unless r is known. Retract and answer "may or may not q".
- Alternative: "if r then q" gives q another route. It does not touch the original rule's MP. It lowers AC and DA because q no longer implies p.
- This is the Belief-R design (d01): Step t gives MP or MT conclusion; step t+1 adds a premise; classify it as requirement (update) or alternative (maintain).
- A checker that treats "if" as strict material implication will disagree with people and with good models on exception-laden items (a15).
- Opposite risk (RULEBREAKERS, d04): a rigid rule is applied against world knowledge. Example: "Anne is in Stockholm or Sweden; she is not in Sweden" so she is in Stockholm is formally valid, but the rule is not what the world supports. The check "does the formal conclusion contradict background knowledge?" is a second code step.

### 4.7 Counterexample count as confidence (De Neys et al. 2003)

Acceptance of MP and MT falls with each retrieved disabler. Acceptance of AC (and with weaker support DA) falls with each retrieved alternative. A count of retrieved counterexamples maps to a graded confidence. Side effect: listing disablers raised AC (b12). A prompt that lists exceptions can push the model toward the converse. So enumerate counterexamples in one slot, apply them to the target inference in another, and have code count (b11, b12).

### 4.8 Dual-source model (Singmann, Klauer and Over 2014)

Two sources for a conditional inference: background knowledge about the content, and a form-based belief from the logic of the argument. Fit estimated the form component from a second, abstract-content task with strong deduction instructions. The combined model fit as well as a model fed only the probabilised task. Probability-logic standards fit MP but not MT (b14). Agent version: run the form check on an abstracted copy and the content check on the original, score them separately, combine in code.

### 4.9 Solver pipelines

Pattern (Logic-LM, LINC, SemEval systems; c18, c19, d14-d17): LLM translates, a program decides.
- Translation unit: one proposition at a time into a fixed form (FOL as LaTeX then rewritten to Prover9 syntax; or A/B/C letter-abstracted standard form).
- Decision: Prover9, Z3, or a lookup in the 24 valid forms.
- Patches: existential import (add a non-empty fact for each term), structured output for extraction (Z3 parse failure fell from 22% to near zero, c20), fallback when parsing fails.
- Report parse error rate and reasoning error rate separately (A01.08-K33).
- Variant: dual-view. Parse twice, once from the native text and once with content terms replaced by symbols; a deterministic verifier decides (d17).
- Variant: vote then solve. Five LLM classifiers vote; the solver is called only on 3-2 splits (c20, d24).

---

## 5. What holds up

### 5.1 Replications and meta-analyses

- **Syllogism difficulty ranks.** Reliable. Six independent data sets from three countries, W = .86 and .64. Entropy W = .45 is weaker but significant (d08). [E]
- **Figural effect.** Replicated across studies and a robust LLM effect too (b24, c02, d21: GPT-4o-mini accuracy by figure F1 89.1, F2 66.7, F3 69.5, F4 58.7). The cause is disputed: the authors favour a semantic account over working-memory first-in-first-out (a04). [E] for the effect, [C] for the mechanism.
- **Byrne suppression.** Direction replicates (Dieussaert 2000, Neth and Beller 1999, De Neys 2003). Size does not: Byrne MP drop 58 points (96 to 38), Dieussaert 28 points (88 to 60) (b09). Byrne restricted permitted answers to a fixed set, which may inflate the effect (b09). Original paper not opened. [E] direction, [C] size.
- **Graded suppression.** De Neys 2003 (every counterexample counts): MP, MT with disablers and AC with alternatives. DA not supported (critique correction). [E] for the three, [S] for DA being null.
- **Probability of conditionals.** Not a settled replication. Three camps (conditional probability, conjunction, mental-model complete) each have data (b13, a18, a19, b15). The best reading is a distribution of reader types, not a universal (b15). [C]
- **Relevance effect.** One large online experiment (577 completed, 348 kept; 40% exclusion). Slopes .78, .61, .43. A second, independent replication was not found. [S]
- **High-probability conclusion effect.** Replicated across three experiments inside one lab, at N = 30, 25, 20. Small samples. The low-probability premise effect failed to hold (a29). No independent-lab replication was found. [S] to [C]
- **Meta-analytic limits.** The 2012 meta-analysis has N = 156 over six data sets. Two labs dominate, and the first author's group proposed one compared theory. Mental-model hits show a publication-bias signal (z = 2.03) (a01, a03). Absolute accuracy depends on instructions ("absolute certainty" vs "follows necessarily") (b04).

### 5.2 Failed or weakened predictions

- No theory fits (a01).
- PHM: "few" vs "some" anomaly, fixed by a later split of positive and negative quantifiers (a09).
- Oaksford et al.: low-probability premise effect unreliable or artifact (a12, a29). Schroyens and Schaeken (2003): the deductive and probabilistic accounts are not isomorphic (a12, secondary).
- Neth and Beller: only the "raise" predictions held; "lower" ones (insufficient, unnecessary) did not (a16).
- De Neys 2003: DA not affected by more alternatives; AC raised by listing disablers (b11, b12).
- Mental-model theory predicted figure difficulty order 4 > 1 > 2 > 3, which the meta-analysis does not confirm (a08).
- Answer-set programming cannot reproduce additional-antecedent MP suppression by completion alone (a15).

### 5.3 Moderators

- **Ability.** Higher ability: fewer DA and AC fallacies (t = 2.63, 2.81), not more MT (MT trended lower) (b17). Conditional-probability responders have higher AH4 (b15).
- **Working memory.** About .7 with syllogism accuracy (unpublished, second hand) (a22).
- **Strategy.** Varies between and within people (b07, a22).
- **Sample.** 55% vs 37% valid conclusions across universities (a22).
- **Content.** Necessity and sufficiency of the condition (a16); relevance (b18); believability (a25; see belief-bias document).
- **Instruction wording.** "Absolute certainty" vs "follows necessarily"; existential-import wording; definite article cues existence (a23, d11).
- **Task format.** Free production vs multiple choice vs binary yes/no gives very different NVC rates (c03, section 6).
- **Negation.** MT 61% with "if p then q" vs 35% with "if not-p then q" (b16). Implicit negation (binary materials) removed the extra MT difficulty but not DA (a12).

### 5.4 Interventions

Worked (in humans or models):
- Telling participants individuals of all relevant sorts exist (neutralises import) (d11).
- For models, a prior-check prompt on empty terms: modern-logic accuracy up by about 3 to 11 points for most Qwen3 models, e.g. Qwen3-14B-Thinking 87.08 to 97.67. Qwen3-4B went down, 62.67 to 59.71 (d13). [S]
- Rules written into the prompt (GPT-5): accuracy 78.1% to 89.9%, content effect 19.14 to 4.95. Adding a script checker over letter-abstracted terms: 96.6%, CE 2.63 (d16). [S]
- Translate-then-explain: GPT-4 77.78 to 83.33 (translation correct 96.67%), a loss for GPT-3.5 (58.89 to 52.22) (d22). [S]
- Parse-then-prove with a structured intermediate format: 95.83 vs 85.97 for direct syntax, 79.22 for LLM-as-prover (d15). [S]
- Explicit CoT or strict-logic frame on previously failed items: 87% and 76% of GPT-4o failures recovered, against 3 to 5% for basic prompts (d19). Selection effect: only failed items re-prompted.
- Vote then solver tiebreak: accuracy 94.3 +/- 0.9, CE 2.85 +/- 1.23 (c20). [C] (see below).
- Fine-tuning on form (Bertolazzi; not available to us) (c05).

Did not work (or not reliably):
- Few-shot examples for NVC, even same-schema ones (c05, b20). In SylloBio few-shot did help F1 (+14% Gemma-7B, +43% Llama-3-8B) but is sensitive to lexical change (c22). In Poddar, few-shot mean 79.1 vs zero-shot 82.7 (t41 = 2.50, p = .0165) (d20). Mixed, so [C].
- Plain CoT as a debiaser: GPT-OSS-20B CE went from 13.67 (zero-shot) to 31.14 (simple CoT); Llama 4 Maverick few-shot CoT CE 3.83 to 10.11 (d24). In the same paper CoT lowered CE for Qwen (zero-shot CE 8.86, CoT 5.07), so it varies by model. [C]
- CoT and plan-and-solve for Belief-R: BREU gain about 1 point (d02).
- Diagrams and logic notation for multimodal models: no reliable help (d21).
- Fine-tuning on countermodels alone did not transfer to validity (d18).
- Telling the model to ignore plausibility helped "somewhat" but CE stayed high (d16).
- Activation steering (Valentino et al.): up to 15% absolute gain, needs open weights (c21). Out of scope.

### 5.5 Contested solver claim (A01.08-K10)

FregeLogic: vote with solver tiebreak 94.3% / CE 2.85 vs Z3 as main judge 74.7% / CE 26.28 vs Z3 veto 74.1% / 26.70 (c20). UFAL-CUNI: a 4B model with a Prover9 pipeline got 95.8% (d15). Ten SemEval systems hit 100% (d14). The difference is parse quality and the templated data. No paper compares vote-with-tiebreak and parse-then-prove at equal tokens. FregeLogic costs about 4,300 tokens and six calls per item (d24). Status: [C].

---

## 6. Language models

### 6.1 Overview by task

| Task | Typical result | Source |
|---|---|---|
| 64-mood production, 9 options | Larger models above average humans on valid items, about 50% human vs 75% best PaLM 2. Near 0% on NVC under zero-shot CoT. Largest model not best | c01, c03, b24, b25 |
| Same, open models | LLaMA-3 8B instruct 50.00% overall (78.15 valid, 30.28 invalid). 70B instruct 41.25% (54.44 valid, 32.50 invalid). 70B base 30.63%. Pythia-1.4B 14.22% | c04 |
| Real-vs-nonce words | Content effects stay in zero-shot and in-context. Fine-tuning removes them only with pseudo-words | b23, c05 |
| Chain length | 3 and 4 premise chains lower zero-shot accuracy; 280 items each | b23, A01.08-K21 |
| Validity of a supplied conclusion, 2025-26 reasoning models | Near ceiling. GPT-5 variants 98.6 to 99.7% on belief-inconsistent valid items; Gemini 2.5 Flash 99.6% syntax accuracy | d19, d20, c11 |
| Belief revision (suppression design) | Very low update accuracy, about 10 to 22% | d01-d03 |
| Rule rigidity against world knowledge | GPT-4o 0.0022 paired accuracy on one MT subset | d04 |
| Conditional probability judgments | Respond to P(B|A) with slopes 0.21 to 0.65 (small models); relevance effects weaker and differently shaped | d05, d06 |
| MT vs MP | MT .31 vs MP .59 soft accuracy | c15 |
| Abduction with syllogistic forms | GPT-4 zero-shot abduction about 42% vs deduction 72.22% (n = 216) | c24 |

### 6.2 Syllogism behaviour in detail

**Accuracy and scale.**
- Eisape et al.: all four PaLM 2 sizes, zero-shot CoT (75 decoded tokens at temperature 0.5). Larger = more accurate on average, but the largest was below the second largest, and on some items (e.g. EA1) accuracy fell with size. Llama 2 replication: near human level, small rise with size. Accuracy is scored on the 27 valid items (c01, b24). A step-by-step prompt gave moderately higher accuracy (b24).
- Human-like errors persist: figural ordering effect (all four sizes, a bit stronger than humans), same top-three human fallacies, confident errors (accuracy inversely related to response entropy). Larger models were somewhat more susceptible to the fallacies (c02). Response distributions correlate fairly highly with human distributions, highest for the smallest PaLM 2 (c02).
- mReasoner fit: 1296 parameter settings, 923 finished; first principal component 77% of variance, correlated with accuracy. In a control with the correct answer's probability set to 0, PC1 had zero correlation with accuracy and 0.6 with the System-2 parameter. Authors read this as larger LMs being more deliberative (b26). [S] interpretation.

**Instruction tuning.** Raises invalid-item accuracy, lowers valid-item accuracy (c04). Always score both.

**Atmosphere.** LLaMA-3 8B ZS-CoT output predicted by atmosphere (section 3.3). Humans: atmosphere predicts 62.50% of correct valid conclusions and 0% on invalid. Models look more atmosphere-driven than people (a26, b21). One model only.

**NVC aversion.**
- Eisape: near 0% under the generative zero-shot prompt. A binary yes/no format (Appendix B.3) gets markedly higher accuracy on NVC items. So part of the aversion is an elicitation effect (c03, critique 4).
- Bertolazzi: in-context examples (including same-schema ones) do not fix it. SFT does, at the price of pattern-matching on the 64 schemas. In-context learning made answers more contradictory (LLaMA-3 8B contradictory answers: zero-shot CoT 1.09%, ICL-out 1.72%, ICL-in 3.12%, SFT 0.31%; Pythia-1.4B 18.91, 28.12, 28.28, 73.91 of which 70.47% were "nothing follows" plus another conclusion) (b22). LLaMA completeness (answer includes all valid conclusions): 43.14% zero-shot vs 96.93% SFT, 72.93 and 76.24 ICL (a27).
- Ando and Mineshima: "neutral" 63.2% (Claude 3.5 Sonnet) vs 25.3% (GPT-4o-mini), labels only, no CoT. NeuBAROCO GPT-4: neutral about 30 points below other labels, often answered "contradiction" (d21, c14).
- Reasoning-tuned models: o3 and GPT-5 reject invalid and import-dependent conclusions at 99.6 to 100% recall in a binary task (d12). Countermodel construction 99% (o3), 89% (Qwen3-32B), against 0 to 42% for conventional models (d18). But the model is told the argument is invalid in d18, and d12 supplies the conclusion. **Nobody has tested free production of NVC on the 37 items with a reasoning model.** [C] (A01.08-K04).

**Figural and conversion effects.** NeuBAROCO: lower accuracy on conversion and atmosphere items. GPT-3.5 atmosphere items 39.42%; fine-tuned NLI models 0% and 0.96% (b27). GPT-4o-mini conversion 52.6% in natural language, 36.8% with Euler diagrams, Claude 3.5 Sonnet 84.2% (d21).

**Precision and recall.** One model: precision 99.2%, recall 42.8% on validity (rejects valid). Gemma 3 27B IT: recall 93.1%, precision 61.0% (accepts too much). Same accuracy, opposite error (c12, A01.08-K23). Vanilla GPT-5 over-rejected: about 60% on valid items, 96% on invalid (d16).

**Existential import drift.** SemEval-2026 Task 11 uses the traditional reading (confirmed by organisers). Under it o3 and GPT-5 score Acct about 62.5% because they accept exactly the 15 modern-valid forms (EN+ 62.50 / 62.53; modern 100.00). Gemini-2.5-Pro 65.17 / 97.33; Gemini-3-Pro-Preview 63.48 / 99.00; Claude-3.7-Sonnet 70.33 / 92.00; Claude-4.5-Sonnet 70.01 / 92.52; GPT-4.1 80.04 / 82.38; GPT-4o 93.33 / 68.75 (traditional / modern). With an empty minor term, Gemini-3-Pro-Preview flips to 98.41 / 64.02 (d12). Thinking variants drift to the modern reading faster than instruct ones; Qwen3-Next-80B Thinking per-mood consistency ranges 8.33 to 62.50 across settings (d13). A benchmark score here may reflect the logic reading, not skill.

**Belief and content.**
- 2022-24 era: Lampinen et al. show the human direction of content effect in PaLM 2-L, Flan-PaLM 2 and GPT-3.5 (belief-by-validity interaction z > 5.9); not significant for Chinchilla and PaLM 2-M. A few-shot or simple instruction cut bias partly (c07). Overlaps the content-effects and belief-bias documents.
- 2025-26 models: belief bias (congruent minus incongruent accuracy) +0.9 (Gemini 2.5 Flash), +1.4 (Gemini 2.5 Pro), +1.9 (GLM-4.6), +7.5 (Kimi-K2), +7.9 (DeepSeek V3.1), +12.5 (Gemini Flash Lite), +28.0 (Qwen3-Next 80B Thinking), +31.6 (Llama 3.3 70B), +46.9 (Llama 3.2 3B). 12 of 14 models positive; mean +10.81 (p = .028, d = 0.66); bias-ability correlation -0.565; 160 items, 14 models, 26,880 evaluations (c11, d20). Small item set (only 38 believable conclusions).
- BIS Reasoning 1.0 (5000 valid belief-inconsistent items, Japanese): GPT-5-mini 99.72, GPT-5-nano (medium) 98.84, gpt-oss-20b 98.56, Qwen3-32B 99.58 (no thinking) and 99.12 (thinking), GPT-4o 79.54, GPT-5-nano (minimum effort) 69.22, GPT-4-turbo 59.48, Claude-3-Opus 7.18, Claude-3-Sonnet 20.34 (d19). Effort setting matters.
- Valid items only: says nothing about rejecting invalid-plausible ones. Keep content tests on invalid-plausible items too (d16, d19).

### 6.3 Conditional behaviour in detail

- **Holliday, Mandelkern and Zhang (2024).** 29 LLMs, 20 instances per pattern, chance 50%. All commit basic fallacies. Zero-shot basic-pattern accuracy about 45% to 89% across models; CoT lifts the best to near 90%, errors remain. Accuracy tracks Arena Elo, MMLU and GSM8K. Many models over-generalise MP, MT and disjunctive syllogism to modal cases where they fail. Some reject MT with "might not" but accept the equivalent "not must". Top models accept contested conditional modus ponens (CMP) zero-shot. The authors reject the material reading, so some "errors" rest on a theoretical stance (c16, c17).
- **Wang and Shi (2025).** Soft accuracy MP .59, disjunctive .54, MT .31 (pairwise p < .001). Modality: may .61, propositional .55, must .27. Mixed-effects marginal R2 .342, conditional R2 .543. Lower perplexity goes with higher accuracy in every model. Few-shot demos help partly by copying (c15).
- **LogicBench.** GPT-4 propositional MT: 59.05 "yes", 55.28 "no" (vs hypothetical syllogism 84.75 "yes"). ChatGPT 66.11 / 55.63; Gemini 81.47 / 75.99; Mistral 44.96 / 47.96. First-order MT: "yes" 88 to 93, "no" 62 to 77 for four of five models. So both negation-in-context and a yes-bias appear (d23).
- **SylloBio-NLI.** 7 schemes, biomedical facts. Zero-shot from 70% (generalised MP) to 23% (disjunctive syllogism, below the 50% chance). Best open model 64% and 55% on two tasks (c22). Per-schema breakdown needed.
- **Lexical negation.** GPT-4 stays high on most conditions; many other models (GPT-3.5, LLaMA-65B, Vicuna, OPT, BLOOM) fall toward 50% or a constant answer when a predicate is replaced by its lexical negation (c23).
- **Belief-R.** Third-premise design on 30 LMs. 1912 basic items; 1074 Belief Update (537 MP, 537 MT), 670 Belief Maintain. Update / maintain / BREU (direct, CoT, plan-and-solve): Llama-3 70B 10.99/92.09/51.54, 12.57/89.40/50.99, 12.66/88.21/50.44. GPT-4 Turbo 19.65/82.69/51.17, 21.51/81.19/51.35, 16.76/83.73/50.25. Mixtral 8x22B 35.38/36.57/35.98, 27.28/34.93/31.11, 44.04/53.13/48.59. Claude 3 Sonnet direct 9.40/88.66/49.03. Best models about 50% BREU; most non-API models near 0% update. MT bases harder (higher update, much lower maintain). Mental-state items kept more often. Maintain accuracy drops with a distractor premise (378 matched items) (d02, d03). The models lean to "keep". Note that this is a different failure from Byrne's humans, who over-retract.
- **RULEBREAKERS.** Seven LLMs. Only Llama-3-8B-Instruct above 0.6 paired accuracy (chance 0.25). GPT-4o and Gemma-2-27b-it perfect on ordinary items and worst on rulebreakers. Confidence in "yes" is higher on ordinary items (p < .0001), so a latent signal exists (d04). So LLMs fail in both directions: not retracting under a stated requirement, and not rejecting a formal conclusion that world knowledge refutes.
- **Orth, Mondorf and Plank (2026).** Llama 8B/70B and Qwen 7B/72B; 144 conditionals (3 relation types x 4 prior levels x 12 contexts), five samples at T = 1.0. Vanilla slopes on P(B|A): 0.35, 0.65, 0.38, 0.21 (Llama 8B, 70B, Qwen 7B, 72B), p < .0001 each. Relation-type effect NEG / POS vs IRR: Llama 8B 0.10 / 0.30, Llama 70B 0.07 / 0.01 (p = .060 for the type effect), Qwen 7B 0.06 / 0.26, Qwen 72B 0.20 / 0.30. Human means (centred) IRR -0.25, NEG -0.26, POS 0.19; models' positive means 0.01 to 0.16 so the gap is in the positive condition. Larger, few-shot and CoT variants show steeper slopes for negative than positive relations, the reverse of people (.78 positive vs .61 negative). ICC over five samples .769 to .978 (vanilla). Ratings cluster at certain values. P(B|A) in stimuli came from human norming, and conjunction/material readings were not tested (d05-d07). Table rows partly scrambled in the PDF text.
- **Abductive and deontic variants.** GPT-4 abduction about 42% vs deduction 72.22%; few-shot deduction 95.83%; Llama-3-70B few-shot abduction 75.46%, deduction 84.72%; belief-inconsistent items about 10 points worse (c24). Deontic Wason rules are easier by 5.0 to 41.2 points for every model and prompt type; selection patterns fit matching bias better than confirmation bias (c25).

### 6.4 Formal solvers

| System | Result | Source |
|---|---|---|
| Logic-LM, GPT-4 (Standard / CoT / Logic-LM) | PrOntoQA 77.40 / 98.79 / 83.20; ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04. GPT-3.5 average gain 39.2% over standard and 18.4% over CoT (not GPT-4). FOLIO executable rate about 79.9% before refinement | b28, c18; critique 6 |
| LINC (ten parses, majority vote) | ProofWriter GPT-4 98.3%, GPT-3.5 96.4%. StarCoder+ FOLIO 56.0% vs 41.8% CoT. GPT-4 LINC vs CoT on FOLIO: McNemar p = .58. StarCoder+ parse syntax errors 38% | c19 |
| FregeLogic (vote, Z3 on 3-2 splits), N = 960 | Tiebreaker 94.3 +/- 0.9, CE 2.85; Z3 weighting 93.4, 3.39; Z3 only 74.7, 26.28; Z3 veto 74.1, 26.70. About 4,300 tokens, 6 calls, 12.1 s sequential (2.8 s parallel) | c20, d24 |
| UFAL-CUNI (Qwen3 4B Thinking) | Full pipeline 95.83 acc, CE 2.28; direct Prover9 syntax 85.97, CE 12.23 (18% syntax errors); LLM as prover 79.22, CE 20.21; end-to-end zero-shot 84.17, CE 14.67; single-step parse 95.81, CE 2.14. Test 95.29 acc, rank 19 of 35. Of 21 validation errors, 10 were gold-label errors, 2 parse errors | d15 |
| lakshadvani (GPT-5) | Vanilla 78.1%, CE 19.14; + rules prompt 89.9%, 4.95; + checker 96.6%, 2.63; competition 100%, CE 0 | d16 |
| 0704mis, subtask 3 (12 languages) | Dual-view 95.83%, CE 5.21; single native 92.08%, 4.89; masked single 97.50%, CE 1.71 | d17 |
| SemEval overview | About 250 participants, over 3000 submissions, 35 system papers; ten systems at 100% / CE 0, at least seven pseudo-formal. Zero-shot: Qwen3 14B 97.38 (CE 4.23), Qwen3 8B 95.81 (CE 4.23), Llama 3.1 8B 64.17 (CE 32.15), Qwen2.5 14B 67.50 (CE 44.54). Score = Acc / (1 + ln(1 + CE)) | d14 |

Reading: a solver wins when parsing is easy and the logic is regular (templated syllogisms, ProofWriter). It loses when translation is lossy (PrOntoQA, FOLIO text). Parse errors are correlated model errors: a ten-way vote of parses cannot detect a shared misreading of "some" or "all" (c19). That ties to G4.

### 6.5 What changes behaviour, by how much (ranked by effect)

1. Switching to a reasoning-tuned model: binary validity from about 60-80% to 98-100% (d12, d19, d20). Large.
2. Formal checker on a templated parse: 78.1% to 96.6% (GPT-5) (d16). Large.
3. Rules in the prompt: +11.8 points, CE -14.2 (d16). Moderate to large.
4. Effort setting: GPT-5-nano minimum 69.22 vs medium 98.84 (d19). Large.
5. Strict-logic or explicit CoT frame on non-reasoning GPT-4o failures: 76 to 87% recovered (d19).
6. Translate-then-explain: +5.6 points for GPT-4, negative for GPT-3.5 (d22).
7. Prior-check about empty terms: +3 to +11 points toward modern reading (d13).
8. CoT in Belief-R: about +1 BREU (d02). Negligible.
9. Few-shot for NVC: negligible (c05).
10. SFT: large but out of scope (c05).

---

## 7. What our agent should take

Schema parts: G guardrails (G1-G12), S states (S0-S9), O operators (O1-O8), M memory. Statuses use the claim file with critique corrections. Section 4b items (bias checklists, "be careful" prompts, unstructured self-reflection, debate) are not re-proposed here. Where this document's findings agree with them (e.g. plain CoT does not reliably debias), it is noted.

### 7.1 Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | **Score valid and invalid items separately, and report false accept and false reject separately.** Never one pooled accuracy. Instruction tuning moved invalid up and valid down; two models with equal accuracy erred in opposite directions. | G7 (harness), M (class record) | [E] | c04, c01, c12, A01.08-K08, A01.08-K23; b24 |
| 2 | **Code-side contradiction check.** Reject any answer set holding A with O, E with I, or NVC with another conclusion. No model needed. | G5 (code selects), S4 | [E] direction (one paper's numbers) | a27, b22 |
| 3 | **Normalise premise order (figure) and check agreement across both orders.** Disagreement between a problem and its term-swapped twin is a free inconsistency signal and an impasse trigger. | S1 (normalise), G1 (signal), G3 (mutated input) | [E] | a04, b05, c02, d10, d21, A01.08-K03 |
| 4 | **State the existential-import reading and the grading logic in the S0 / S1 restatement.** Which reading holds (24 or 15 valid forms) decides which syllogisms are valid. Benchmarks do not agree with frontier models by default. | S0 / S1 | [E] | a23, c09, d12-d15, A01.08-K20, A01.08-K32 |
| 5 | **Weight MT separately; log it as its own item type.** MT is the weak valid form for people and models, with negation making it worse (35% with "if not-p then q"). | S4 test set, M | [E] | c15, b16, b17, d23, A01.08-K18, A01.08-K19 |
| 6 | **Expect surface-pattern answers on invalid items; flag them in code.** Compute atmosphere / min-heuristic predictions in code. If the model's answer equals the heuristic prediction and the validity check disagrees, tag it. | G1 trigger, S4 | [E] direction for LLMs generally, [S] numbers | a05, a06, c06, a26 |
| 7 | **Do not rely on few-shot examples to teach "nothing follows."** Use a structural step instead. | G-series, 4b adjacent | [S] strictly, but see #8 | b20, c05 |
| 8 | **Any solver step needs a fallback and separate error counts.** Report parse errors and reasoning errors apart; fall back to the plain answer when the parse fails; patch existential import. | O (formal check), G6 | [E] | b28, c18, c19, d14, d15, A01.08-K09, A01.08-K33 |
| 9 | **Check a formally valid conclusion against background knowledge before accepting it, and check an added premise for a defeater before keeping an MP conclusion.** Both failure directions are measured in LLMs. | G (premise-completeness), S4 | [E] for humans (suppression), [S] each for LLMs | a13, b09, b11, d01, d04, A01.08-K11, A01.08-K12 |
| 10 | **Do not conflate "probability of if" with P(C|A) in prompts; define which quantity is asked.** | S1 | [C]/[E] for the need to define | a18, a19, b13, b15 |
| 11 | **Per-problem difficulty from the human table for effort allocation.** Spend more checking where human answers are spread (high entropy) and in figures 1 and 2 for NVC. | S0 / S3 budget (G12) | [E] for the human map | a02, b04, d08, d10, A01.08-K01 |

### 7.2 Test first

Each item has a hypothesis; none is established for LLMs. Order is by value per cost.

| # | Test | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | **Counter-model search step for NVC.** Code enumerates region assignments and returns a counterexample to each candidate; the model reads it back. Compare against plain CoT on the 37 invalid items at equal tokens. | O (counterexample search), S4, S7 | [S] (human best-practice; LLM unproven) | a21, b03, b26, d18, A01.08-K04, A01.08-K30 | Gap 2 and gap 1. Might be unneeded on a reasoning base. |
| T2 | **Per-candidate binary questions instead of "what follows?"** Loop over the 8 candidate conclusions with one yes/no each, plus NVC if none. | S3 / S4 | [S] | c03 | Eisape's binary format raised NVC accuracy. |
| T3 | **Rules-in-prompt before any solver.** Aristotelian forms written into the prompt. | S1 / S4 | [S] | d16, A01.08-K34 | +11.8 points at one model. |
| T4 | **Parse-to-letters then reason in prose (abstraction).** | O6 (change representation), S1 | [C] | c07, d16, d17, d22, A01.08-K22 | No clean test exists. |
| T5 | **Requirement-vs-alternative classification state for any added premise.** | S4 / O (revise) | [S] | d01-d03, A01.08-K27 | CoT and plan-and-solve added about 1 point. |
| T6 | **Contrapositive rewrite on MT items.** | O5 (work backwards), O6 | [S] | c15, d03, d23, A01.08-K18 | Cause of MT difficulty not isolated. |
| T7 | **Knowledge-conflict probe before accepting a valid-form inference.** | G, S4 | [S] | d04, A01.08-K28 | Counterbalances a solver front end. |
| T8 | **Vote with solver tiebreak vs parse-then-prove vs plain vote at equal tokens.** | G4, G5, O (verify) | [C] | c20, d14-d16, d24, A01.08-K10 | No equal-token comparison exists. |
| T9 | **S0 existence line (traditional vs modern) on the nine import-dependent moods.** | S0 | [E] need, [S] size | d13, A01.08-K32 | Prior-check helped 3 to 11 points; pin-traditional untested. |
| T10 | **Style vote on conditional-probability items.** Sample five times, classify each as P(C|A), conjunction or material, test if the majority beats a single run. | G4, G5 | [S] | b15, d07, A01.08-K16, A01.08-K35 | Style classification does not exist for LLMs. |
| T11 | **Relevance check before accepting an "if" claim as a premise.** | S1 | [S] | b18, d05, d06, A01.08-K15, A01.08-K29 | LLM slopes differ in shape from humans. |
| T12 | **Counterexample enumeration depth for graded confidence.** Prompt for 0 to 4 disablers or alternatives; map the count to confidence in code. Watch the AC side effect. | S4 | [E] human, [S] LLM | b11, b12, A01.08-K12 | Listing disablers raised AC in people. |
| T13 | **Translate-to-logic then reason, gated on translation accuracy (>= about 90%).** | O (formal check) | [S] | d22, A01.08-K36 | Gain for GPT-4, loss for GPT-3.5. |
| T14 | **Chain decomposition into pairwise steps.** | O3 (decompose) | [S] | b23, A01.08-K21 | Zero-shot accuracy falls with chain length. |

### 7.3 Do-not-add (consistent with SCHEMA 4b)

- Do not hard-code one human-error theory into the agent (a01, A01.08-K02). Use the theories only as detectors.
- Do not assume more CoT removes content effects: model-dependent (d24).
- Do not add a "be careful with syllogisms" instruction: SCHEMA 4b already covers this class.
- Do not treat a solver as the sole judge unless the parse is shown reliable (c20, b28).
- Do not add few-shot examples as the NVC fix (c05).

---

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (G7). Pre-register the metric. Report per item type, never pooled. Use the `bench` harness arms (plain, best-of-N, scaffold). Seeds and counts below are suggestions, not fixed.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | **64-mood production task.** All 64 premise pairs, real and nonce words, nine options including NVC. Run with a reasoning and a non-reasoning model. | plain CoT vs scaffold with code-side counter-model enumeration (T1) | Accuracy on the 27 valid items and the 37 NVC items separately; atmosphere-fit share of errors on NVC items; per-figure NVC recall (human reference 50 / 57 / 70 / 86%); contradiction rate | Non-reasoning base: NVC from about 0 to 30% toward the human 41%, valid accuracy kept within a couple of points. Reasoning base: possibly no gain (tokens wasted). |
| B2 | **Binary-per-candidate format** (T2) on the same 64 items | generative vs yes/no loop, equal tokens | NVC recall; valid accuracy; false accept rate | Higher NVC recall for non-reasoning model (Eisape appendix B.3). |
| B3 | **Figure-swapped twins.** Each of the 27 valid problems in its figure and a term-swapped variant. | plain vs "restate premises in both orders, then conclude" (no more than equal tokens) | Accuracy gap by figure; agreement rate between twins | Gap of the order seen in humans (about 80% vs 20% for fit vs violating bias) for a plain model; smaller gap with normalisation. |
| B4 | **Existential-import items.** The nine import-dependent moods under both keys. | plain vs S0 existence line (traditional or modern pinned) | Accuracy under the stated key; share answered on each reading | Plain reasoning model sits on modern (Acct about 62.5%); pinning traditional should move it (untested; the sign is not established). |
| B5 | **Content 2 x 2** (valid/invalid x plausible/implausible), 12 to 30 items per cell | plain vs rules-in-prompt vs abstraction step (T3, T4) | Belief bias (congruent minus incongruent); accuracy on invalid-plausible items | If bias on the base model is under about 2 points, skip the debias step (d20). Otherwise expect rules in prompt to cut CE (GPT-5: 19.14 to 4.95). |
| B6 | **Suppression set** (Byrne design): MP, MT, AC, DA with plain / alternative / additional premise. Adapt Belief-R subsets (update and maintain). | plain CoT vs requirement-vs-alternative classification step (T5) vs defeater-listing step | Update accuracy and maintain accuracy separately; MP/AC/DA/MT acceptance by condition | Plain: update low (about 10 to 22% for non-reasoning models), maintain high. A classification step should raise update without dropping maintain. Direction of any change is not established. |
| B7 | **Rulebreaker items** (RULEBREAKERS style) | plain vs knowledge-conflict probe (T7) | Paired accuracy on rulebreakers and on matched ordinary items | Plain model accepts the formal conclusion; the probe should reduce this without lowering ordinary-item accuracy. |
| B8 | **MT items**, affirmative, explicit negation, implicit negation | plain vs contrapositive rewrite (T6) | MT accuracy per form; answer flips across the three forms | MT lower than MP; negated antecedent worst (human 35 to 39%). Rewrite may close the gap; cause is not isolated. |
| B9 | **P(if A then C) vs P(C|A) probe** on matched relevant, negative, irrelevant items (card style and everyday). Five samples each. | direct ask vs "suppose A" first | Slope on P(C|A) by relevance (human .78 / .61 / .43); gap P(if) minus P(C|A); share of conjunction answers per sample | LLM slopes weaker than human; style varies across samples; a majority vote across styles tested (T10). |
| B10 | **Counterexample depth.** Rules with 0 to 4 disablers or alternatives given. | plain vs enumerate-then-apply | Acceptance by count; AC side effect | Graded decline as in De Neys 2003; watch AC rise with disablers. |
| B11 | **Solver step.** 960-item templated set plus 100 free-text syllogisms | plain 5-vote vs 5-vote + solver tiebreak vs single parse-then-prove | Accuracy, content effect, parse error rate separately, tokens per item (FregeLogic about 4,300) | Templated: parse-then-prove near 96%+. Free text: parse failures rise; tiebreak safer. |
| B12 | **Chain length.** 2, 3, 4 premises | whole vs pairwise reduction | Accuracy by length | Whole-chain accuracy falls with length; stepwise holds. |

Calibration set: use the per-item human percentages of Table 6 of the meta-analysis as a difficulty ladder and compute Kendall tau between the agent's failure rank and human rank (A01.08-K01). Interpret a low tau as the agent failing for different reasons than humans, which is informative, not bad.

---

## 9. What does not transfer, and why

- **Working-memory accounts.** First-in-first-out working memory as an explanation of the figural effect, and the .7 working-memory correlation. A language model has no limited-capacity buffer in that sense. The figural effect still shows up in LLMs (b24), so a different cause is at work. Do not copy working-memory fixes (chunking for load).
- **Individual differences in strategy.** Human strategy classes (model builders vs not) need think-aloud data. We only see outputs. Response style classes in LLMs are untested (A01.08-K35).
- **The Equation as a normative default.** Whether P(if) = P(q|p) is "the right answer" is contested (b13 vs a18). For an agent the right move is to define the quantity in the prompt, not to impose a view.
- **Human suppression as the target.** Byrne's humans over-retract MP under an added requirement; LLMs under-retract (Belief-R) and also over-apply rules (RULEBREAKERS). The human pattern is not the goal and not the LLM failure. The agent's target is the correct defeasible answer, not the human one.
- **Human NVC reluctance.** Humans are reluctant to say NVC (about 41% correct), models far more (near 0% in generative format), so copying human norms is not enough (c03).
- **Atmosphere and matching as full explanations.** They explain surface agreement and some LLM errors, but fail on "only" premises (a05) and cannot produce NVC. Use as detectors only.
- **PHM's assumption that reasoners cannot test validity.** True of many people, not true of a scaffolded agent with a code check (a06).
- **mReasoner fits.** r = 0.82 to human data and a fit to LMs are diagnostics of a simulator with hand-set parameters. Not decision-relevant (A01.08-K25).
- **Small-model results.** Atmosphere fit is for one 8B model; many LLM numbers are from LLaMA-3 8B, Pythia, PaLM 2 and 7-8B open models. They may not describe current reasoning models (critique weak spots).
- **Activation steering and fine-tuning.** Strong effects (up to 15% absolute; SFT near ceiling) but outside a scaffold-only agent (c21, c05).
- **Templated benchmark results.** SemEval 100% systems exploit regular templates. Free text breaks parsing (FOLIO, c19; PrOntoQA, b28).
- **Diagram aids.** Euler and linear diagrams did not reliably help multimodal LLMs (d21).
- **Formal-rule "strict if".** Treating "if" as material implication disagrees with both humans and good models on exception-laden items (a15).

---

## 10. Open questions

From critique gaps and the gap pass; with what would close each.

1. **Do reasoning-tuned models say "nothing follows" in free production?** Binary results say they reject invalid conclusions (d12), but the 37-item production test and the atmosphere-fit score are missing. Test B1.
2. **Does an explicit counter-model step help at equal tokens?** LogicSkills told the model the argument was invalid, so noticing invalidity is untested (d18). B1, B2.
3. **Suppression and defeater listing in reasoning-tuned models.** Belief-R tested no reasoning-tuned models (d01). MP/AC/DA/MT rates are not reported. B6.
4. **Is the LLM P(if A then C) closer to P(C|A), the conjunction or the material conditional?** Orth et al. did not compare these (d05). B9.
5. **Why is MT hard?** Negation, backward direction and yes-bias all appear (d03, d04, d23). A contrapositive rewrite has not been tested. B8.
6. **Equal-token comparison of vote with tiebreak vs parse-then-prove.** Not available (d24). B11.
7. **Which existential import reading does a given benchmark assume, and does pinning it help?** Prior-check moves toward modern (d13); a prompt pinning traditional was not tested. B4.
8. **Can a prompt-only abstraction step remove content effects in modern models?** No study lets the same model reason in prose after letter replacement. B5.
9. **Response-style variation across samples.** Only numeric ICC reported (d07). B9.
10. **The effect sizes of the "some" quantifier cases and generalised quantifiers (most, few).** The meta-analysis gives per-item percentages only (d10). LLM data on generalised quantifiers not found.
11. **Does the high-probability conclusion effect hold for LLMs?** Not tested. Vary P(p), P(q), exceptions in descriptions and check acceptance against P(not-p | not-q). Also check the Verschueren and Schaeken challenge.
12. **Independent replication of the relevance effect and of the 17% vs 68% result** by non-aligned labs. None found.
13. **Do human error maps predict model errors for current models?** Eisape found fairly high correlation for PaLM 2 (c02); no such analysis for reasoning models.
14. **Is the Byrne size of suppression partly a response-format artifact?** Byrne used a fixed answer set (b09); Dieussaert found about half the effect. Original not opened here.
15. **Does listing disablers cause AC errors in LLMs?** Seen in people (b12), untested in models.
16. **Source checks still due.** Byrne 1989 original and Verschueren and Schaeken full text were not opened (critique).

---

## 11. Sources

[V] = opened and read (full text or PDF, or author copy) this study. [M] = snippet or secondary table only.

**Human syllogisms**
- [V] Khemlani and Johnson-Laird (2012) Theories of the syllogism: a meta-analysis. Psychological Bulletin. https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf ; author copy https://mentalmodels.princeton.edu/papers/2012syllogisms-meta-analysis.pdf (a01-a05, a22-a25, b01-b06, d08-d11). The critique could not reopen it; the gap pass opened the author copy and verified reliability, Table 8 and figure numbers. Table text was scrambled in places.
- [V] Chater and Oaksford (1999) The probability heuristics model of syllogistic reasoning. https://www.dectech.co.uk/publications/LinksNick/ReasoningAndDecisionMaking/The%20Probability%20Heuristics%20Model%20of%20Syllogistic%20Reasoning.pdf (a06-a08)
- [V] Oaksford, Roberts and Chater (2002) Relative informativeness of quantifiers used in syllogistic reasoning. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/BF03195273.pdf (a09)
- [V] Khemlani (2020) Psychological theories of syllogistic reasoning (chapter). https://modeltheory.org/papers/2020syllogisms-chapter.pdf (a21, b07; partly read)

**Conditional inference, probability, suppression**
- [V] Oaksford, Chater and Larkin (2000) Probabilities and polarity biases in conditional inference. https://www.dectech.co.uk/publications/LinksNick/ReasoningAndDecisionMaking/probability%20and%20polarity%20biases%20in%20conditional%20inference.pdf (a10-a12, a28, a29). Negations literature inside it (Evans 1977; Pollard and Evans 1980; Wildman and Fletcher 1977; Evans et al. 1995; Evans and Handley 1999) is [M].
- [M] Byrne (1989) Suppressing valid inferences with conditionals. Numbers via secondary sources: https://arxiv.org/pdf/2311.04412 (a13, a15), https://arxiv.org/pdf/2002.10149 (b08-b10), https://iccl.inf.tu-dresden.de/w/images/7/77/BST.pdf (a14, Dietz and Holldobler 2016 slides). The original was not opened.
- [M] Dieussaert et al. (2000), suppression replication, via https://arxiv.org/pdf/2002.10149 (b09). Original not opened.
- [V] Neth and Beller (1999) How knowledge interferes with reasoning. https://www.psych.uni-goettingen.de/de/cognition/publikationen-dateien-neth-3/1999_nethbeller_how-knowledge-interferes-with-reasoning_suppression-effects-by-content-and-context.pdf (a16, a17)
- [V] De Neys, Schaeken and D'Ydewalle (2003) Inference suppression and semantic memory retrieval: every counterexample counts. https://link.springer.com/content/pdf/10.3758/BF03196099.pdf (b11, b12; re-checked in critique)
- [V] Singmann, Klauer and Over (2014) New normative standards of conditional reasoning and the dual-source model. https://pmc.ncbi.nlm.nih.gov/articles/PMC4029011/ (b13, b14)
- [V] Evans, Handley, Neilens and Over (2007) Thinking about conditionals: a study of individual differences. https://link.springer.com/content/pdf/10.3758/BF03193509.pdf (b15-b17)
- [V] Girotto and Johnson-Laird (2004) The probability of conditionals. https://www.jstage.jst.go.jp/article/psysoc/47/4/47_4_207/_pdf (a18, a19)
- [M] Evans, Handley and Over (2003), Oberauer and Wilhelm (2003): figures via Girotto and Johnson-Laird (a19).
- [V] Skovgaard-Olsen, Singmann and Klauer (2016) The relevance effect and conditionals. https://discovery.ucl.ac.uk/id/eprint/10107867/1/The%20Relevance%20Effect%20and%20Conditionals-CORRECTED.pdf (b18, b19)
- [V] van Rooij and Schulz (2019) Conditionals, causality and conditional probability. https://link.springer.com/content/pdf/10.1007/s10849-018-9275-5.pdf (a20; theory paper)
- [M] Verschueren and Schaeken, "Denial inferences: Oaksford, Chater and Larkin (2000) on shaky ground" (abstract record via OpenAlex; critique item 7).
- [M] Cariani (2017) and Espino (2020) suppression snippets, mentioned in c27 (35% contravening-MP endorsement vs 99% basic MP; unverified).

**LLMs on syllogisms**
- [V] Eisape et al. (2024) A systematic comparison of syllogistic reasoning in humans and language models. https://arxiv.org/abs/2311.00445 (b24-b26, c01-c03)
- [V] Bertolazzi, Gatt and Bernardi (2024) A systematic analysis of large language models as soft reasoners: the case of syllogistic inferences. https://arxiv.org/abs/2406.11341 , https://arxiv.org/pdf/2406.11341 (a26, a27, b20-b23, c04-c06)
- [V] Lampinen et al. (2024) Language models show human-like content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (b29, c07; syllogism section only)
- [V] Ando et al. (2023) NeuBAROCO. https://arxiv.org/abs/2306.12567 (b27, c13; abstract and intro in one version)
- [V] Ozeki et al. (2024) Exploring reasoning biases in LLMs through syllogism: NeuBAROCO. https://arxiv.org/abs/2408.04403 (c14, d22)
- [V] Zong and Lin (2024) Categorical syllogisms revisited. https://arxiv.org/abs/2406.18762 (c08, c09)
- [V] Zang et al. (2026) A syllogistic probe: tracing the evolution of logic reasoning in LLMs. https://arxiv.org/abs/2601.17426 (c10, d12, d13). Table captions assigned by position.
- [V] Poddar, Sahoo and Ghosh (2025/2026) Understanding syllogistic reasoning in LLMs from formal and natural language perspectives. https://arxiv.org/abs/2512.12620 (c11, c12, d20)
- [V] Nguyen et al. (2026) BIS Reasoning 1.0. https://arxiv.org/abs/2506.06955 (d19)
- [V] Ando and Mineshima (2026) Do diagrams help large language models reason? https://arxiv.org/abs/2607.23513 (d21)
- [V] Rabern, Mondorf and Plank (2026) LogicSkills. https://arxiv.org/abs/2602.06533 (d18)
- [V] Valentino et al. (2026) Mitigating content effects on reasoning in language models through fine-grained activation steering. https://arxiv.org/abs/2505.12189 (c21; abstract, intro, summary text)
- [V] Wysocka et al. (2025) SylloBio-NLI. https://arxiv.org/abs/2410.14399 (c22)
- [V] Ye et al. (2023) Assessing step-by-step reasoning against lexical negation. https://arxiv.org/abs/2310.14868 (c23)
- [V] Abe et al. (2026) Abductive reasoning with syllogistic forms in LLMs. https://arxiv.org/abs/2603.06428 (c24)
- [V] Abi Akl et al. (2026) Are you talking logic to me? https://arxiv.org/abs/2608.12374 (c26; abstract, setup, dataset tables)

**LLMs on conditionals and revision**
- [V] Holliday, Mandelkern and Zhang (2024) Conditional and modal reasoning in large language models. https://arxiv.org/abs/2401.17169 (c16, c17)
- [V] Wang and Shi (2025) Logical forms complement probability in understanding language model (and human) performance. https://arxiv.org/abs/2502.09589 (c15)
- [V] Parmar et al. (2024) LogicBench. https://arxiv.org/abs/2404.15522 (d23). PDF tables partly garbled.
- [V] Wilie et al. (2024) Belief revision: the adaptability of large language models reasoning (Belief-R). https://arxiv.org/abs/2406.19764 (d01-d03). Table A1 partly unlabeled.
- [V] Chan, Gaizauskas and Zhao (2025) RULEBREAKERS. https://arxiv.org/abs/2410.16502 (d04)
- [V] Orth, Mondorf and Plank (2026) If probable, then acceptable? https://arxiv.org/abs/2510.08388 (d05-d07). Table 2 partly scrambled.
- [V] Abe et al. (2026) Evaluation of deontic conditional reasoning in LLMs: Wason's selection task. https://arxiv.org/abs/2603.06416 (c25)

**Solvers and SemEval-2026 Task 11**
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (b28, c18)
- [V] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 (c19)
- [V] Akinfaderin and Diallo (2026) FregeLogic. https://arxiv.org/abs/2604.18328 (c20, d24)
- [V] Valentino et al. (2026) SemEval-2026 Task 11 overview. https://aclanthology.org/2026.semeval-1.450/ (d14)
- [V] Kartac et al. (2026) UFAL-CUNI at SemEval-2026 Task 11. https://arxiv.org/abs/2605.04941 (d15)
- [V] Advani (2026) lakshadvani at SemEval-2026 Task 11. https://aclanthology.org/2026.semeval-1.80/ (d16)
- [V] Gupta, Goyal and Bedi (2026) Team 0704mis at SemEval-2026 Task 11. https://aclanthology.org/2026.semeval-1.224/ (d17)

**Not a source**
- c27 (search gap, opened:false) was a claim of absence of LLM suppression studies. It is refuted by Belief-R (d01). Kept only as a record of the search failure.

Several 2026 items are arXiv or workshop preprints and may be un-peer-reviewed. Dates are as recorded in the evidence files.
