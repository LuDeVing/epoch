# Decomposition (Fermi-ize): deep document

*Subfield E03.05, forecasting and calibration. Built from evidence_a-d.jsonl (ids a01-a25, b01-b17, c01-c28, d01-d19), claims.jsonl (K01-K27) and critique.md in this folder. Schema reference: SCHEMA.md v0.2, operator O3 (Decompose), guardrails G1-G12. Evidence ids are cited in brackets, claim ids as K##.*

**Verdict in one paragraph.** Decomposition is a real tool with a narrow window. In people, it cuts error about 20-fold when the target is huge and unknown, and makes error worse (about 458 percent higher) when the target is familiar. In language models, it helps a lot on long, compositional, symbolic tasks (SCAN 16.2 to 99.7). It does nothing measurable for prompt-only forecasting (Brier change +0.008, adjusted p = .774). It gives a small, uncertain gain when sub-questions are forecast blind with fresh research (Brier 0.141 to 0.132, confounded with extra research). Nobody has run the equal-token test on a modern model. So O3 stays [S]. The one solid rule is the gate: decompose when the answer is unknown and the parts are easier and independent, and not otherwise.

---

## 1. What it is

**Decomposition** means splitting a hard question into parts that are easier to answer, answering each part, and combining the answers with a rule. "Fermi-izing" is the numeric form: a target is written as a product of factors (piano tuners in a city = population x share with a piano x tunings per year / tunings per tuner per year). Raiffa (1968) called it the spirit of decision analysis [a01].

Three kinds are easy to confuse.

| Kind | What is split | How parts combine | Example |
|---|---|---|---|
| Multiplicative (Fermi) | A quantity into factors | Multiply | Packs of film sold in the US = households x share with cameras x packs per year [b01] |
| Event decomposition | A probability into sub-events | Probability laws, e.g. P(A and B) = P(A) x P(B given A) | Paleka consistency laws [c06] |
| Sub-question decomposition for search or reasoning | A question into easier questions | Model reads the sub-answers and writes the final answer | Halawi sub-queries [a16], Bosse blind sub-forecasts [c01], least-to-most [a19] |

Additive splits (disaggregation) are out of scope [a01].

**Why it matters for our agent.** SCHEMA O3 says: at an impasse, write 2 to 4 sub-problems whose answers combine into the answer. The schema marks it [S]. This document asks when it helps, when it hurts, and what must surround it (a gate, an independence check, a recompose step).

**What the field lacks.** The key work named in SUBFIELDS.md is Tetlock and Gardner (2015), *Superforecasting*. It reports no effect size for decomposition, and we could not open it [a10]. The superforecaster training study (Chang et al. 2016) never names decomposition [d10]. So the human numbers here come from the Armstrong/MacGregor line of work, not from Tetlock.

---

## 2. History and theories in depth

### 2.1 Human judgment (1968-1994)

- **Raiffa 1968.** Decision analysis splits a problem into assessable pieces. This is the theoretical root [a01].
- **Armstrong, Denniston and Gordon 1975 (founding study).** 151 subjects, random groups, odd quantities (Polaroid film packs, tobacco, dropouts, contest cards). Decomposed groups were more accurate on 12 of 13 comparisons and significantly better on 9 of 13 (median test, p < .05). Tobacco: 64 percent of direct estimates were off by a factor of 10 or more, against 20 percent of decomposed ones. The gain was largest where subjects knew least; ranking of problems by prior confidence matched ranking of gains (Spearman, p < .05 in two groups). The authors concluded decomposition "usually helps and is unlikely to hurt" [a02, b01, b02]. The last claim was later shown wrong.
- **Exploratory side result.** 11 self-decomposers against 11 given-decomposition subjects on two problems: self-decomposition was worse on both, not significant [b03].
- **MacGregor, Lichtenstein and Slovic 1988.** 16 almanac-style problems, 45 subjects per estimate. Decomposed estimates beat global ones overall [a03].
- **Ravinder, Kleinmuntz and Dyer 1988.** A measurement-error model: the random error of a decomposed estimate depends on component error size and on how correlated the component errors are [a08, abstract only].
- **Henrion, Fischer and Mullin 1993.** Almanac quantities, five fractiles. Decomposition did not significantly change median accuracy or calibration. It moved a bias from underestimating uncertainty (direct) to overestimating it (decomposed). Self-chosen and experimenter decompositions did not differ [a09, not opened].
- **MacGregor and Armstrong 1994 (the pivot paper).** They re-cut the old data by problem type and ran a new randomised experiment. Result: decomposition helps only when the target is extreme and uncertain. They gave three conditions and a decision procedure (section 4) [a01, a04, a05, b08].

### 2.2 Theory: why it should work, and when it should not

1. **Parts are easier.** People know more about components than about the whole, so each component has less relative error [a01].
2. **Errors partly cancel.** Independent over- and under-estimates in the parts offset in the product. This needs part errors not to be strongly positively correlated.
3. **Compounding.** Two parts each 20 percent high give a target 44 percent high (1.2 x 1.2) [a01, b06]. A shared wrong anchor multiplies through. In MA94, subjects misjudged the US population by a factor of 1.4 to 2 (1.97 in one case) and two non-extreme problems inherited that error [a23, a05].
4. **Retrieval structure.** Decomposition forces knowledge retrieval along named channels. This is the MacGregor 1988 framing ("structuring knowledge retrieval") [a03].

### 2.3 Language models (2021-2026)

Four strands that should not be mixed:

1. **Fermi estimation by models.** Kalyan et al. 2021 built the benchmark (about 1,000 real and 10,000 synthetic problems, each with an executable program and facts) [a11]. Liu et al. 2025 re-tested GPT-3.5, GPT-4 and Llama 3 [a14]. Epstein et al. 2025 tested interval calibration on 1,000 Science Olympiad Fermi questions [a15].
2. **Decomposition as a prompting method for reasoning.** Least-to-most (Zhou 2022) [a19], decomposed prompting (Khot 2022) [a21], successive prompting (Dua 2022) [c17], self-ask (Press 2022) [a20], plan-and-solve (Wang 2023) [c20], divide-or-conquer distillation (Wu 2024) [c18], ADaPT (Prasad 2024) [d14].
3. **Decomposition for faithfulness.** Radhakrishnan et al. 2023 [a18]. Lanham 2023 gives the motivation: chain-of-thought text is often not the cause of the answer [c24].
4. **Decomposition for forecasting.** Halawi 2024 (sub-questions steer search) [a16]; Schoenegger 2025 (prompt-only Fermi, event, time decomposition) [b13, d03]; Bosse 2026 (blind sub-forecasts) [c01, d01]; Paleka 2024 (consistency laws that decomposition implies) [c06].

### 2.4 Reading across the two literatures

Human result: gain depends on how extreme and unknown the target is. LLM result: gain depends on task length and compositional structure. The shapes match (big help at the hard end, nothing or harm at the easy end), but tasks, metrics and models differ, so there is no pooled estimate [a22].

---

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single source, **C** contested, **H** human-only, **O** older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Decomposition helps on extreme, unknown quantities (humans) | New experiment, 280 subjects, 10 problems, 1,078 estimates. Six extreme problems (3.5 million to 4.2 billion): better on 5 of 6; median error ratio cut 19.78-fold (p < .001). Area of US 33.88 to 1.70; wheat 45.71 to 6.92; pants 17.38 to 10.00; auto accidents 93.33 to 1.86; athletic shoes cut 4.10; TV Guide worse 7.76 to 10.96 (ns) | MA94 [a05, b05] | E, H (K01) |
| Pooled reanalysis of earlier studies | Nine extreme problems: error cut 68.3-fold. Six others: about zero net effect. 1988 data, 6 extreme: 99.3 to 3.0 (96.3 cut); 5 non-extreme: 1.8 to 2.3 (about 50 percent worse). 1975 data, 3 extreme: 18.0 to 5.7 | MA94 [a03, a04, b04] | E, H; split was post hoc |
| Founding study | N = 151; decomposed better in 12 of 13, significant in 9 of 13; tobacco 64 percent vs 20 percent off by 10x or more | Armstrong 1975 [b01] | H; decompositions supplied |
| Decomposition hurts on familiar quantities (humans) | Four non-extreme problems (4 digits or fewer): median error up 458 percent (p < .05 two-tailed); Argentine immigrants 4.89 to 46.77; bank failures 10.45 to 19.50; presidents 1.23 to 1.35; coin 1.82 to 1.41 | MA94 [a05, d09] | E, H (K02) |
| Gain tracks how little the estimator knows | Rank of prior confidence matched rank of gain, Spearman p < .05 in 2 of 3 groups; digits in true value correlate +0.75 with IQR across subjects | Armstrong 1975, MA94 [b02, a03] | S (K03) |
| Parts easier than whole is not guaranteed | Parts easier for only 3 of 6 problems measured. Spread (log10 IQR) fell on 4 of 6 extreme problems (area of US 2.30 to 0.37; wheat 3.30 to 0.89) and rose on 3 of 4 non-extreme (Argentine immigrants 1.00 to 2.14; TV Guide 1.36 to 1.85) | MA94 [a06, b06] | S, H (K04) |
| Error compounding | +20 percent x +20 percent = +44 percent; US population error 1.97 carried into two problems; Kalyan jelly-bean case 3 orders of magnitude off from one bad fact | MA94, Kalyan [a01, a23, a13] | E (K04) |
| Self-chosen decomposition not better than given | 11 vs 11, two problems, worse, ns. Henrion 1993: no difference (not opened). Kalyan: generated decompositions "seldom meaningful" | Armstrong, Henrion, Kalyan [b03, a09, b09] | S (K05) |
| Overconfidence barely moves | Chance of being within 10 percent: global expected 38.9, got 10.9 (28.0 points over); decomposed expected 32.6, got 9.0 (23.6 over). Three self-rating measures correlated above .99 across 6 problems | MA94 [a07, b07] | S, H (K06) |
| Human deliberation stays overconfident | Where 10 percent of z-scores should fall below a point, 42 percent did; where 90 percent should, 68 percent | Cognitive Science 2025 [d13] | S, H |
| Instructed Fermi decomposition in groups | Study 2 (preregistered, 240 people, 60 groups): decompose vs share-and-combine numbers, z = 2.1, p = .039, d = 0.26, 95 percent CI -0.09 to 0.61. Study 1: consensus error 0.72 vs 1.18 for mean of initial guesses (d = 0.81). Group use beat solo use | Barrera-Lemarchand 2026 [d12] | S, H; CI includes zero (K25) |
| LLMs are far off on real Fermi problems | T5, question-only: program-derived score about 0.01 to 0.04. Facts supplied: direct 0.18, program 0.36, fact F1 0.95. fp_score levels 0 / 2 / 4: GPT-4 0.466 / 0.479 / 0.500; GPT-3.5 0.398 / 0.420 / 0.418; Llama 3 0.439 / 0.469 / 0.460 (556 test questions) | Kalyan 2021, Liu 2025 [a12, a14, d07] | E, O (K08) |
| Executing the program beats guessing the number | 0.36 vs 0.18 (T5, facts supplied) | Kalyan [a12, b09] | S, O (K09) |
| LLM intervals overconfident on Fermi questions | Nominal 99 percent intervals cover about 65 percent. GPT-4o-mini 0.63 / 0.59 / 0.64 at nominal 0.90 / 0.95 / 0.99. Conformal adjustment gives about 99 percent coverage; Winkler score down 54 percent (25.2 / 27.8 / 59.4 percent at 0.90 / 0.95 / 0.99). Log-probability method 0.85 / 0.89 / 0.90 | Epstein 2025 [a15, d08] | E (K07); small cheap models |
| Prompt-only decomposition does not help LLM forecasts | 38 prompts, 4 models, 100 ForecastBench questions, about 3,700 forecasts per model, control Brier 0.208-0.227. Fermi +0.008, Event +0.007, Time -0.008, all adjusted p = .774. Unadjusted t-tests: Fermi +0.004 (p = .643), Event +0.002 (p = .751), Time -0.013 (p = .096). Bayesian prompt +0.030 (worse, p < .001) | Schoenegger 2025 [b13, d03] | S (K10); no retrieval |
| Blind sub-forecasts give a small gain | 500 questions: Brier 0.141 (CI 0.122-0.161) to 0.132 (0.115-0.149), better in 94.4 percent of 10,000 bootstraps. Calibration term 0.026 to 0.008; refinement 0.091 to 0.083 | Bosse 2026 [c01, d01, d02] | S (K11); extra GPT-5 research in that arm |
| The two forecasting results disagree | Schoenegger null vs Bosse small gain | b13 vs c01 | C (K12) |
| Sub-questions inside a retrieval pipeline | Full system Brier .179, crowd .149, random .25, best baseline GPT-4-1106 .208. Ablations: no fine-tuning .186; no fine-tuning and no retrieval .206. Sub-question step never ablated | Halawi 2024 [a17, d04] | S (K13) |
| Models know parts, fail to compose | Compositionality gap near 40 percent at all GPT-3 sizes; 42.9 percent ChatGPT; 23.0 percent GPT-4. Hardest category: 1.2 percent right on 2-hop while answering 80 percent of sub-questions. Bamboogle: direct 17.6, CoT 46.4, self-ask 57.6, self-ask plus search 60.0 | Press 2022 [a20, b12, c11, c12] | S, O (K14) |
| Sub-answer confidence predicts composition | Max perplexity 1.000-1.002: 81.1 percent of 2-hop right; 1.232-6.738: 42.6 percent | Press [c13] | S (K15) |
| Gain is larger on long chains | SCAN length split, code-davinci-002: standard 16.7, CoT 16.2, least-to-most 99.7. GSM8K CoT vs L2M by steps: 2 steps 76.68 vs 74.53 (CoT better); 3 steps 67.29 vs 68.91; 4 steps 59.39 vs 59.73; 5+ steps 39.07 vs 45.23. Overall 60.87 vs 62.39. DROP non-football 74.77 vs 82.45 | Zhou 2022 [a19, c08-c10] | S, O (K16) |
| Two-stage decompose-then-solve beats single stage | GSM8K EM / DROP F1 / Bamboogle: single GPT 20.32 / 46.51 / 49.6; GPT+GPT 65.13 / 55.73 / 54.4; Vicuna-13B decomposer + GPT solver 62.93 / 47.13 / 48.8; GPT decomposer + Vicuna solver 28.51 / 20.90 / 29.6. Distilled decomposer + GPT solver 67.02 / 55.19 / 52.0; distilled solver 48.98 / 13.37 / 31.2 | Wu 2024 [c18, c19] | E (K17); weak GSM8K baseline |
| Factored decomposition: more faithful, not more accurate | Averages: zero-shot 72.8, few-shot 79.7, CoT 86.0, CoT-decomposition 85.6, factored 81.8. CoT leads CoT-decomposition by 0.4 | Radhakrishnan 2023 [a18, d06] | E (K18) |
| Decompose only on failure | GPT-3.5 executor success: ALFWorld ReAct 43.3, plan-and-execute 43.3, ADaPT 71.6; WebShop 32.0 / 17.0 / 44.0; TextCraft 19.0 / 27.0 / 52.0 | ADaPT [d14] | S (K23) |
| Stepwise reasoning pays on symbolic structure | Mean CoT gain: symbolic +14.2, math +12.3, logic +6.9; other categories 56.8 vs 56.1 | Sprague 2025 [d15] | E (K24) |
| Blind sub-answers beat in-context ones (non-numeric) | Llama 65B FACTSCORE: few-shot 55.9; CoVe joint 60.8; factored 63.7; factor+revise 71.4 | CoVe [d16] | S (K22) |
| Decomposition implies checkable laws | Violation of Cond check correlates with Brier 0.92 / 0.87 (first dataset), 0.71 / 0.69 (second). Or check 0.14 / 0.24 weak; Negation on second dataset -0.36 / -0.13. Patching forecaster gave no ground-truth Brier gain | Paleka 2024 [c06, d05] | S (K19, K27) |
| Superforecaster training bundle | Brier gain 10-11 percent (year 1), 12 (year 2), 6 (year 3), 7 (year 4); decomposition not isolated, term absent from paper; 2025 re-analysis shrinks or flips training and team effects | Chang 2016, Hauenstein 2025 [d10, d11] | E that it cannot be cited for O3 (K26) |

---

## 4. Mechanisms and models

Each item is written so it can be coded.

### 4.1 The error model (when decomposition wins)

Let target T = F1 x F2 x ... x Fk. Work in logs: log T = sum of log Fi. Let ei be the log error of part i and E the log error of a direct estimate.

- Decomposed log error = sum of ei. Its variance = sum of Var(ei) + 2 x sum of Cov(ei, ej).
- Decomposition wins if that variance is smaller than Var(E).
- With independent parts it needs sum Var(ei) < Var(E). With positive correlation, the covariance terms add and can wipe out the gain.
- Bias adds too. If every part is 20 percent high, the target is 44 percent high at k = 2 (1.2^2) and 2.07 times at k = 4 (1.2^4).

The three MA94 conditions follow [a01, d09]:
1. The target is hard to estimate (Var(E) large).
2. Each part has smaller relative error than the target (Var(ei) small).
3. Part errors are not strongly positively correlated.

A fourth shows in the data: part count matters. More parts give more chances for a shared bias to multiply. Keep k at 3 to 5 (the Bosse prompt asks for 3 to 5 sub-questions [c02]).

### 4.2 The gate (MA94 procedure, adapted for a program) [b08]

Original human procedure: rate uncertainty; if above the midpoint, pretest with 20 subjects; if the upper-quartile geometric mean has 7 or more digits, compare interquartile ranges of target, components and recomposition; use the narrower.

Agent translation (untested; see section 8):

```
samples = n independent direct answers (n = 3..5), fresh contexts
spread  = IQR of log10(samples)          # same statistic MA94 used
if spread >= threshold (about 1.75 log10, the MA94 high-disagreement cut) -> decompose
else -> answer directly
```

Two further triggers have support elsewhere:
- ADaPT: decompose only when the executor fails [d14]. Forecasting has no immediate failure signal, so use sample disagreement as the proxy.
- Numeric multiplicative structure: stepwise reasoning pays on math and symbolic tasks (+12 to +14 points) and about +0.7 elsewhere [d15].

### 4.3 The decompose-then-solve pipeline

Two stages beat one [c18]. The decomposer can be a cheap model with small loss; the solver must be strong [c18, c19]. Implementation:

1. The decomposer returns 3 to 5 named sub-problems and a combine rule as a formula, not prose.
2. Each sub-problem is answered in its own context, blind to the parent question and to the other parts (CoVe factored [d16]; Bosse blind sub-forecasts [c02]).
3. Code evaluates the combine rule. Executing a program beat guessing the number, 0.36 vs 0.18 [a12].
4. A recompose check compares the combined answer to a direct estimate. A large gap is a signal to resample, not to average blindly. (MacGregor and Lichtenstein 1991: people reconcile by averaging [b08].)

### 4.4 Blindness and factoring

Radhakrishnan's factored decomposition answers each sub-question in a separate context. Faithfulness rises; accuracy drops about 4 points against CoT (81.8 vs 86.0) [a18, d06]. This matches the schema's own rule of fresh contexts with no authorship and no proposed answer (G4, G5). Its value for numeric forecasts is untested [K22].

### 4.5 Consistency monitor (event decomposition)

For events A and B, a model should satisfy P(A and B) = P(A) x P(B given A). Compute the gap per question. Across forecaster configurations the Cond gap tracks Brier (r = 0.92 / 0.87), but a patching forecaster built on the checks gave no ground-truth gain and did not generalise to held-out checks [c06, d05]. Use it as a logged monitor (SCHEMA section 6), not as a repair.

### 4.6 Calibration wrapper

Decomposition does not fix interval width (humans 28.0 to 23.6 points over; LLMs about 65 percent coverage at nominal 99) [a07, a15]. Conformal recalibration did (about 99 percent coverage, Winkler down 54 percent) [a15]. Keep it separate from the decomposition step: calibrate the final interval on a held-out set of the same question type.

### 4.7 Scoring

Kalyan fp_score = max(0, 1 - |log10(A / A*)| / 3). One at the exact answer, zero at three or more orders of magnitude off [a11]. MA94 error ratio = max(est / true, true / est), tested on logs [a05].

---

## 5. What holds up

### 5.1 Replications and agreement

- **Human, extreme targets.** Three data sets (1975, 1988, 1994) agree in direction. The 1994 experiment is a randomised test of a pattern found post hoc in earlier data, which is the right check [a04, a05]. It is the same research group plus one reanalysis, so independence is limited [critique].
- **Human, easy targets.** Harm shows in the 1994 randomised experiment (458 percent) and in the 1988 reanalysis (about 50 percent worse). Two data sets [K02].
- **LLM, long compositional tasks.** Least-to-most, decomposed prompting, successive prompting, self-ask and two-stage distillation all gain where tasks are long or structured (SCAN 99.7 vs 16.2; Bamboogle 57.6 vs 46.4; Wu GSM8K 65.13 vs 20.32) [a19, a20, c17, c18]. Gains are small or negative where tasks are short (GSM8K 2-step 74.53 vs 76.68) [c10].
- **LLM Fermi interval overconfidence.** One 2025 study, three models, consistent [a15].

### 5.2 Failures, nulls and caveats

- **Henrion 1993.** No median accuracy effect, only a shift from under- to over-estimating uncertainty. Seen only through an abstract description and MA94 [a09].
- **Schoenegger 2025.** All three decomposition prompts null. Frequency-Based Reasoning (-.019, adjusted .022), Base Rate First (-.016, adjusted .036) and Step-Back (-.015, adjusted .036) cleared simple t-tests, and the preregistered mixed model erased them (adjusted p = .774 for everything but Bayesian) [b13, b14, d03]. The authors include Tetlock and Mellers.
- **Radhakrishnan 2023.** Decomposition costs accuracy against plain CoT [d06].
- **ADaPT.** Always-decompose (plan-and-execute) hurt on WebShop: 17.0 vs ReAct 32.0 [d14].
- **Press 2022.** The gap did not close with scale in GPT-3 (about 40 percent at every size), though GPT-4 reached 23.0 percent [a20].
- **Kalyan 2021.** Right answers from meaningless decompositions (Europe airborne, 0.98) and wrong answers from sound ones (jelly beans, 0.00) both occur. A score alone does not show which [a13].
- **Consistency patching.** No Brier gain [d05].
- **Superforecaster training.** A bundle of 6-12 percent; no isolated decomposition arm; the 2025 re-analysis weakens even the bundle [d10, d11].

### 5.3 Weak spots in the evidence base (critique.md)

1. Human evidence is 1975-1994, almanac quantities, one group plus a reanalysis. The "extreme" cut (digit count) is post hoc, unit-dependent, and was revised from over 7 to 7 or more digits [a25].
2. No human decomposition study on event probabilities scored by Brier, which is what our agent forecasts.
3. LLM forecast decomposition: Bosse is one model, 500 questions, overlapping CIs, extra research in the decomposed arm, paired-difference CI not reported [d01]. Schoenegger is 100 questions, 2024 models, no retrieval [d03].
4. Bosse's Table 2 text is garbled; trust the abstract (Gemini 3 Pro 0.134, GPT-5 0.149, Gemini 2.5 Flash 0.179) [d02].
5. Radhakrishnan Table 4 text is garbled. The prose gap of 0.4 and column arithmetic settle CoT 86.0 vs CoT-decomposition 85.6. The HotpotQA figures in b11 and c22 mix rows [d06].
6. Seen only as abstract or snippet: Ravinder 1988, Henrion 1993, Hauenstein 2025. The Tetlock book was not opened. Chang 2016 was read as a summary page [a08, a09, a10, d10, d11].

### 5.4 Moderators with support

| Moderator | Direction | Evidence |
|---|---|---|
| Target extremeness and unfamiliarity | More gain | a03, a05 |
| Part errors correlated | Less or negative gain | a01, a23, b06 |
| Parts easier than whole | Needed | a06 |
| Task length / steps | More gain with more steps | c10 |
| Having facts (retrieval) | Needed for numeric Fermi; decomposition cannot supply facts | a12, a13, d03 |
| Solver strength | A weak solver cannot be rescued by a good decomposer | c18, c19 |
| Who decomposes | Given decompositions at least as good as self-made in humans; a cheap decomposer is fine for LLMs | b03, c18 |

### 5.5 Interventions that worked and did not

Worked: gating to hard or unknown targets (humans); two-stage decompose then solve; running the combine rule as code; blind sub-answers (non-numeric); decompose-on-failure; conformal interval recalibration.

Did not work, or no evidence: prompt-only Fermi, event or time decomposition for forecasting; a Bayesian-style prompt (worse); always-decompose; consistency patching; crediting superforecaster training.

---

## 6. Language models

### 6.1 Fermi problems

- **Finding the decomposition is the weak step.** A fine-tuned T5 given only the question scored 0.01 to 0.04 through its own program. Given the facts, the program route scored 0.36 against 0.18 for a direct guess [a12]. About 80 percent of generated programs ran, most were single-operation, and about 20 percent of problems need more [b09].
- **Bigger models are better but still weak.** GPT-4 reached fp_score 0.466 / 0.479 / 0.500 across structured prompt levels; GPT-3.5 0.398-0.420; Llama 3 0.439-0.469. All at or under 0.500. Prompt structure moved scores by 0.02 to 0.03 [a14, d07]. The prompts varied structure in general, not decomposition alone. No 2025-2026 frontier score was found.
- **Intervals are too narrow.** Coverage at nominal 99 percent was about 65 percent and did not rise with the requested level [a15, d08]. The authors theorise that a model's own reasoning trace narrows its answer distribution ("tunnel vision"). This is a hypothesis with no measurement [d08].

### 6.2 Forecasting

| Setting | Result | Source |
|---|---|---|
| Base LLMs, no retrieval, 2024 | Brier 0.208 to 0.227; random 0.25 | b13 |
| Prompt-only decomposition, 4 models | +0.008 / +0.007 / -0.008 vs control, adjusted p = .774 | b13, d03 |
| Retrieval pipeline with sub-question search, GPT-4 era | 0.179 vs crowd 0.149; retrieval plus fine-tuning worth about 0.027 | a17, d04 |
| ReAct agent, ensemble | 0.169 vs single 0.180 (human median 0.172, 201 questions); plain GPT-4o ensemble 0.218 vs single 0.210 (worse) | d18 |
| Blind sub-forecasts, Gemini 3 Pro | 0.141 to 0.132 | c01 |

Reading: decomposition without new evidence does nothing, since the model has nothing new to split into. With fresh research per sub-question, a small gain appears, located in the calibration term of the Brier split (0.026 to 0.008) while refinement fell only 0.008 [d02]. That fits a picture where sub-forecasts pull a YES-biased final forecast (mean forecasts 0.37-0.42 against a base rate of 0.292 [c03]) back toward the base rate. It is a hypothesis, not a result.

### 6.3 Reasoning tasks

- Gains concentrate in symbolic and math tasks (+14.2, +12.3, +6.9) and almost vanish elsewhere (56.8 vs 56.1) [d15].
- Least-to-most: 99.7 vs 16.2 on SCAN, +1.5 on GSM8K, worse on 2-step problems [c08-c10].
- Plan-and-solve: average over six math sets 70.4 (zero-shot CoT) to 72.9 (PS) to 76.7 (PS+). Part of the gain comes from detailed rules, not the plan [c20]. Of zero-shot CoT errors, calculation 7, missing-step 12, semantic misunderstanding 27 (percent of a 100-problem sample); planning targets only the missing-step class [c21].
- Compositionality gap: 40 percent for GPT-3 at all sizes, 42.9 for ChatGPT, 23.0 for GPT-4 [a20].
- Two-stage pipelines: the gain depends on solver strength [c18].

### 6.4 What changed behaviour, and by how much

| Change | Effect |
|---|---|
| Add self-ask (follow-up questions) | Bamboogle 46.4 to 57.6; with search 60.0 [c12] |
| Add decompose-first with a decomposer model | GSM8K 20.32 to 65.13 (weak baseline) [c18] |
| Run the combine rule as code | 0.18 to 0.36 [a12] |
| Condition on sub-answer confidence | 42.6 vs 81.1 percent composition success [c13] |
| Answer follow-ups blind | FACTSCORE 60.8 to 63.7 [d16] |
| Decompose on failure | ALFWorld 43.3 to 71.6 [d14] |
| Conformal wrapper on intervals | Coverage 65 to about 99 percent [a15] |
| Faithfulness-oriented factoring | More faithful, 4.2 points less accurate [d06] |
| Prompt-only forecasting decomposition | No change [b13] |

---

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part: G, S, O, or memory. Evidence ids in brackets.

### Add now (established)

1. **Gate O3 by extremeness and difficulty; never always-on.** Decompose only when the target is large or unknown and a direct answer is a guess; leave familiar quantities alone. Schema part: O3 plus the S0 and S6 trigger, consistent with G1. [E] K01, K02; a05, b05, a03, d09.
2. **Require the three conditions before accepting a split:** the target is hard, parts are easier than the whole, part errors do not share one anchor. Schema part: O3 precondition. [E] K04; a01, a06, a23, b06, d09.
3. **Two-stage structure: a decomposer, then a separate strong solver.** A cheap decomposer is acceptable; a weak solver is not. Schema part: O3 architecture, with cost counted under G7. [E] K17; c18, c19, a21.
4. **Combine with code, not prose.** The decomposer outputs a formula and code evaluates it. Schema part: G5 applied to O3. [E] for the design rule (G5, F08); the 0.36 vs 0.18 magnitude is [S] K09 (a12, b09).
5. **Do not trust stated interval width; recalibrate on held-out data.** Decomposition leaves overconfidence in place (humans 23.6 points over; LLMs 65 percent coverage at nominal 99). Schema part: G (calibration), S9 class record. [E] K07; a07, a15, d08, d13.
6. **Do not cite superforecaster training as evidence for O3.** Schema part: documentation. [E] K26; d10, d11.
7. **Log every decomposition run:** mode, trigger, part count, tokens, whether the final answer moved from the direct-sample median, and the Cond gap for events. Schema part: SCHEMA section 6, so G7 can judge O3. [E] by G7.
8. **Keep O3 at [S] in SCHEMA.md.** The evidence supports a gated version, not an unconditional operator; no element reaches two independent LLM-forecasting sources. [E] by SCHEMA rule 8.1.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Three-arm equal-token forecast test: direct, extra research without structure, blind sub-questions, with retrieval | O3 | [C] K12 | b13, c01, d01 |
| T2 | Sample-spread trigger (decompose when 3 to 5 direct samples disagree) vs always vs never | S0 gate, O3 | [S] K02, K03, K23 | a05, b02, d14 |
| T3 | Blind vs in-context sub-forecasts on numeric items | O3 | [S] K22 | d16, d01 |
| T4 | Agent-written vs templated decompositions | O3 | [S] K05 | b03, b09 |
| T5 | Part-level resampling to cut correlated error | O3, G4 | untested, indirect | d17, d18, d09 |
| T6 | Sub-answer confidence gate on recompose | G | [S] K15 | c13 |
| T7 | Cond-gap per-question monitor as a resample trigger | G, S6 | [S] K19, K27 | c06, d05 |
| T8 | Sub-question line ablation in a retrieval query prompt | S3, retrieval | [S] K13 | a16, d04 |
| T9 | Step-count trigger (decompose at 4+ steps) | O3 | [S] K16, K24 | c10, d15 |
| T10 | Conformal wrapper on agent intervals | G | [E] for the LLM coverage failure; wrapper untested on our agent | a15 |
| T11 | Kalyan fp_score with and without retrieval | O3 | [E] weakness known; our number unknown | a14, d07 |
| T12 | Reconcile several independent decompositions by reasoning vs by averaging | O3, S7 | [S] K25 | d12 |

---

## 8. Concrete tests on our bench

All arms get equal total tokens: setup, decomposer, sub-answers, combine step and any research are all counted. Where the bench has retrieval, every arm gets the same retrieval budget. Use paired items and a paired bootstrap (10,000 resamples) and report the paired CI, which Bosse did not [d01].

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Binary forecasting questions with retrieval, at least 500 items | A direct plus retrieval; B direct plus extra research sampled to the same tokens; C blind sub-questions (3 to 5) plus recompose | Brier, split into calibration and refinement | C minus B between -0.005 and 0 Brier (smaller than Bosse's -0.009 once extra research is controlled); a null is plausible. A gain, if any, sits in the calibration term |
| T2 | Fermi numeric items (Kalyan real set, 556 test items, plus MA94-style almanac items) | A always direct; B always decompose; C decompose if the IQR of 3 to 5 direct samples is at least 1.75 log10 | fp_score; median error ratio; tokens | C at least as good as the better of A and B; B worse than A on familiar items (MA94: +458 percent error); C well above A on extreme items |
| T3 | Numeric forecast or Fermi items | A sub-answers in context; B sub-answers blind to parent and each other | fp_score or Brier | B above A by a small margin (CoVe +2.9 FACTSCORE); null likely on numbers |
| T4 | Fermi items | A agent-written decomposition; B template from a fixed library; C gold (Kalyan program) | fp_score | C above B above A; the A to C gap shows what finding the decomposition costs |
| T5 | Fermi items with one injected biased fact in one part | A one estimate per part; B 3 independent estimates per part, median | log error of target; damage from the bias | B reduces damage; size unknown, likely small if the bias is shared across samples (G4) |
| T6 | Two-hop and multi-part items | A always recompose; B recompose only if sub-answer confidence is high, else resample | accuracy, tokens | B higher at equal tokens (Press: 81.1 vs 42.6 percent by band) |
| T7 | Conditional or conjunction forecast pairs | A none; B resample when the Cond gap passes a threshold | Brier; gap before and after | Strong correlation across configurations (0.92 / 0.87) but expect a weak per-question effect (patching gave none) |
| T8 | Forecast questions in a replica Halawi query stage | A queries with sub-question lines; B without | Brier with retrieval | Under 0.02 Brier (the whole retrieval stack is worth about 0.027) |
| T9 | Reasoning items with labelled step count | A always decompose; B decompose at 4+ steps; C never | accuracy by step band | Gain at 5+ steps (+6 points in Zhou), none at 2 steps |
| T10 | Held-out interval set | A raw 90 percent intervals; B conformal-adjusted | coverage; Winkler score | A about 63 percent; B about 90 percent; Winkler down about 25 percent |
| T11 | Kalyan real set | A plain model; B model plus retrieval; C model plus retrieval plus gated decomposition | fp_score | B or C above 0.50 would beat the GPT-4 era; unknown |
| T12 | Fermi items | A average of 3 independent decompositions; B reconcile the 3 by code-run comparison of factors | log error | B above A is plausible if disagreement points at the weak factor (groups d = 0.26) |

---

## 9. What does not transfer, and why

1. **The human digit-count "extreme" rule.** It is unit-dependent and post hoc [a25]. Use disagreement across samples instead.
2. **Human "given decomposition" results.** In MA94 and Armstrong, experimenters supplied the breakdown, and self-made ones did no better [b03]. An LLM must produce its own, and Kalyan shows generated decompositions are seldom meaningful (T5, 2021) [b09].
3. **Cancellation of independent human errors.** One model's samples share beliefs, so part errors are likely more correlated than independent people's (G4; self-consistency gains are smaller than independence would give [d17]). The MA94 independence condition may be violated by default.
4. **Almanac quantities to event probabilities.** All human data are quantities. Our agent forecasts events scored by Brier. Brier punishes wide errors less than log error does, and the combine rule for events is probability algebra, not multiplication.
5. **Superforecaster training.** Not isolable and weakened by re-analysis [d10, d11].
6. **Least-to-most and SCAN gains.** SCAN is synthetic with a clean grammar; the models are code-davinci-002 era; the gain is length generalisation, which a modern reasoning model largely gets from its own long trace [c08].
7. **Wu 2024 GSM8K gain.** The single-stage baseline was weak (20.32), which inflates it [c18].
8. **Faithfulness gains.** They cost about 4 accuracy points and do not make one answer more correct [d06]. Useful for auditing (G10), not for scoring.
9. **Consistency patching.** Built on checks that do not carry to held-out checks [d05].
10. **Fine-tuned T5 numbers (Kalyan).** 2021 models fine-tuned on the task; frontier models with tools may differ greatly.
11. **Epstein overconfidence.** Cheap models (GPT-4o-mini, Claude-3.5-Haiku, Grok-3-mini); frontier reasoning models are unmeasured here [a15].

---

## 10. Open questions

1. Does decomposition improve Brier for a modern LLM on binary forecast questions at equal tokens, isolated from retrieval? Decisive for O3; b13 and c01 conflict.
2. What trigger tells the agent when to decompose? Only decompose-on-failure (ADaPT) and a structure cue have been tested, neither on forecasts.
3. Does blindness of sub-forecasts to the parent matter for numbers?
4. Do multiple samples per part reduce correlated-part errors in LLMs?
5. Is the sub-question line in Halawi-style pipelines worth its cost?
6. Does decomposition change LLM interval calibration, as it modestly did in humans (28.0 to 23.6 points over)?
7. How well do 2025-2026 frontier models score on Kalyan's real set (best known 0.50)?
8. Does a recomposition-consistency check beat plain decomposition as a gate?
9. Is the Bosse gain a calibration correction (shrinking a YES-biased forecast) rather than better discrimination? The Brier split points that way.
10. What did Tetlock's superforecasters actually do with decomposition, and can it be isolated? No opened source answers this.
11. Does the human extremeness rule have an LLM analogue, the model's own knowledge boundary? K03 is single-source.

---

## 11. Sources

[V] = opened and read this session. [M] = snippet, abstract or second-hand only.

| Source | Mark | URL |
|---|---|---|
| MacGregor and Armstrong (1994) Judgmental decomposition: when does it work? Int. J. Forecasting | [V] | https://marketing.wharton.upenn.edu/wp-content/uploads/2022/02/140-JSA-Judgmental-Decomposition-When-Does-It-Work.pdf ; https://doi.org/10.1016/0169-2070(94)90027-2 |
| Armstrong, Denniston and Gordon (1975) The use of the decomposition principle in making judgments | [V] repository record; 1975 numbers also via MA94 | https://repository.upenn.edu/entities/publication/c1c49f1b-3311-4e36-bd68-35cf357b8459 |
| MacGregor, Lichtenstein and Slovic (1988) Structuring knowledge retrieval | [M] numbers via MA94 | (see MA94 PDF above) |
| Ravinder, Kleinmuntz and Dyer (1988) The reliability of subjective probabilities obtained through decomposition | [M] abstract | https://ideas.repec.org/a/inm/ormnsc/v34y1988i2p186-199.html |
| Henrion, Fischer and Mullin (1993) Divide and conquer? | [M] | https://ideas.repec.org/a/eee/jobhdp/v55y1993i2p207-227.html |
| Tetlock and Gardner (2015) Superforecasting | [M] not opened | https://www.penguinrandomhouse.com/books/227815/superforecasting-by-philip-e-tetlock-and-dan-gardner/ |
| Chang, Chen, Mellers and Tetlock (2016) Developing expert political judgment | [V] summary page | https://jbaron.org/journal/16/16511/jdm16511.html |
| Hauenstein, Thomas, Illingworth and Dougherty (2025) Rethinking the role of teams and training | [M] abstract | https://doi.org/10.1177/09567976241266481 |
| Barrera-Lemarchand et al. (2026) Fermi decomposition in groups, Nature Communications | [V] | https://doi.org/10.1038/s41467-026-76365-y |
| Deliberation in guesstimation (Cognitive Science, 2025) | [V] Europe PMC full text | Europe PMC record (title and journal only) |
| Kalyan et al. (2021) How much coffee was consumed during EMNLP 2019? Fermi problems | [V] | https://arxiv.org/abs/2110.14207 |
| Liu et al. (2025) LLM for complex reasoning task: an exploratory study in Fermi problems | [V] | https://arxiv.org/abs/2504.02671 |
| Epstein, Winnicki, Sornwanee and Dwaraknath (2025) LLMs are overconfident | [V] | https://arxiv.org/abs/2510.26995 |
| Halawi, Zhang, Yueh-Han and Steinhardt (2024) Approaching human-level forecasting | [V] | https://arxiv.org/abs/2402.18563 |
| Schoenegger, Tuminauskaite, Park, Bastos and Tetlock (2025) Prompt engineering LLM forecasting capabilities | [V] | https://arxiv.org/abs/2506.01578 |
| Bosse, Muhlbacher, Wildman, Phillips and Schwarz (2026) Automating forecasting question generation | [V] | https://arxiv.org/abs/2601.22444 |
| Paleka, Goel, Geiping and Tramer (2024) Consistency checks for language model forecasters | [V] | https://arxiv.org/abs/2412.18544 |
| Karger et al. (2025) ForecastBench | [V] keyword scan only | https://arxiv.org/abs/2409.19839 |
| Hsieh, Fu and Chen (2024) Reasoning and tools for human-level forecasting | [V] | https://arxiv.org/abs/2408.12036 |
| Lu (2025) Evaluating LLMs on real-world forecasting against expert forecasters | [M] abstract-level | https://arxiv.org/abs/2507.04562 |
| Radhakrishnan et al. (2023) Question decomposition improves the faithfulness of model-generated reasoning | [V] | https://arxiv.org/abs/2307.11768 |
| Lanham et al. (2023) Measuring faithfulness in chain-of-thought reasoning | [M] abstract | https://arxiv.org/abs/2307.13702 |
| Zhou et al. (2022) Least-to-most prompting | [V] | https://arxiv.org/abs/2205.10625 |
| Press et al. (2022) Measuring and narrowing the compositionality gap | [V] | https://arxiv.org/abs/2210.03350 |
| Khot et al. (2022) Decomposed prompting | [V] text only; figures not read | https://arxiv.org/abs/2210.02406 |
| Dua et al. (2022) Successive prompting | [V] table garbled | https://arxiv.org/abs/2212.04092 |
| Wu et al. (2024) Divide-or-conquer? Which part should you distill | [V] | https://arxiv.org/abs/2402.15000 |
| Wang et al. (2023) Plan-and-solve prompting | [V] | https://arxiv.org/abs/2305.04091 |
| Prasad et al. (2024) ADaPT | [V] | https://arxiv.org/abs/2311.05772 |
| Sprague et al. (2025) To CoT or not to CoT | [V] | https://arxiv.org/abs/2409.12183 |
| Dhuliawala et al. (2023) Chain-of-verification | [V] | https://arxiv.org/abs/2309.11495 |
| Wang et al. (2023) Self-consistency | [V] | https://arxiv.org/abs/2203.11171 |
