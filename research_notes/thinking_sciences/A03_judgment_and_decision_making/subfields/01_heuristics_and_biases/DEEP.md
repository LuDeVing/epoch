# Heuristics and biases: deep document

*Subfield A03.01. Built from evidence_a-d.jsonl, claims.jsonl (K01 to K37) and critique.md in this folder. Evidence ids (a01 ... d21) and claim ids (K01 ...) are cited throughout. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

*Reading note. Most LLM studies below used one prompt per cell, small item sets, and models from 2022 to 2024. Numbers for named models date quickly. Scoring differs between papers, so effect sizes are not comparable across LLM studies.*

---

## 1. What it is

The heuristics-and-biases program asks one question. When people judge probability, frequency or a number, do they follow logic and probability theory? The answer from the program is no, and the deviations are systematic, not random. The authors explained them with a small set of mental shortcuts.

The three founding heuristics (Tversky and Kahneman 1974, a01):

- **Representativeness.** Probability is judged by how much the case resembles a stereotype. Base rates, sample size and regression are ignored.
- **Availability.** Frequency is judged by how easily examples come to mind or can be built.
- **Anchoring and adjustment.** An estimate starts from a number and moves too little from it.

The later unifying idea is **attribute substitution** (Kahneman and Frederick 2002, a20, K11): a hard target question is answered by a related, easier one that is more accessible. "How likely?" becomes "how typical?". This chapter was not opened by any worker, so the claim rests on summaries.

Standard findings named in the focus line:

- **Linda problem / conjunction fallacy.** A "feminist bank teller" is ranked more probable than "bank teller".
- **Base-rate neglect.** A stereotype description overrides a stated prior.
- **Sample-size insensitivity.** A small hospital and a large one are judged equally likely to deviate from 50 percent.

Why it matters for our agent. The agent is one language model run through a scaffold. The schema's S1 step (input hygiene) moves suggestive material, such as a stated guess, an authority claim or an irrelevant number, into a marked block. This subfield is the human evidence base for that step, and the LLM evidence says how large the effect is for models and what removes it. Two kinds of cue matter most: a vivid description that replaces a prior, and a number that pulls a numeric answer. Both are things code can find in the input.

Scope limits. This document covers the founding studies, their replications and rivals, and every LLM or AI study that tests or uses them. Related but separate subfields in this run (Bias and debiasing, Outside view and base rates, Ecological rationality, Diagnosticity of evidence) are only linked, not covered.

---

## 2. History and theories in depth

### 2.1 Origins (1969 to 1974)

Tversky and Kahneman began the work in 1969 and wrote the 1974 Science paper in 1973 (a12). Their stated method has three parts: compare intuition with a normative rule, search for the heuristic behind the gap, and explore the gap between judgment and rational belief theory. The paper was cited over 420 times by April 1983 and about 1,100 times by 2015 in Web of Science (a12, a17).

Key weakness, noted by the authors' own critics: the 1974 paper is a list of biases, not a process model. The heuristics are named after the fact, and many numbers in it come from earlier cited studies, not from the paper itself (a01).

The 1973 paper (Kahneman and Tversky, "On the psychology of prediction") gave the first direct Bayes tests: the engineer-lawyer problem, the Tom W. study, the cab problem and the regression study (a06, a07, a08). The 1983 Psychological Review paper added the conjunction fallacy (a09 to a11).

### 2.2 The three heuristics as first stated

| Heuristic | Core claim | Founding evidence |
|---|---|---|
| Representativeness | Likelihood judgment follows similarity to a stereotype | Tom W. mean likelihood vs similarity r = .97, vs base rate r = -.65 (a06) |
| Availability | Frequency follows ease of recall or construction | Committees of 2 vs 8 from 10 people: median 70 vs 20, true 45 for both (a05) |
| Anchoring and adjustment | Start at a number, adjust too little | Wheel of fortune: median 25 (anchor 10) vs 45 (anchor 65) African UN members (a04) |

### 2.3 Rival and refining theories

1. **Pragmatic / Gricean reading (Hertwig and Gigerenzer 1999, b02, b25, d02).** People treat the description as relevant and read "probable" as "plausible" or "possible". In a paraphrase study only 7 of 39 (18 percent) responses read "probability" in a mathematical way. Frequency wording cut violations to 0 to 13 percent. Kahneman and Tversky (1996) disputed this (a21; opened only as a snippet).
2. **Frequency-format / ecological account (Gigerenzer and Hoffrage 1995, a13).** Errors fall when numbers are given as natural frequencies, because the Bayes calculation becomes a ratio of counts. Boundary: the gain is carried by numerate people (Chapman and Liu 2009, a14) and was absent for base-rate neglect in older adults (a15).
3. **Intensional / similarity account (Jonsson and Hampton 2006, a16).** People accept "all sofas have X" but doubt "all uncomfortable handmade sofas have X". More specific is more believable and less probable, which predicts an inverse conjunction effect. This is a competing account of Linda.
4. **Selective accessibility and mixed anchoring accounts.** Anchoring may come from adjustment that stops at the first plausible value (Epley and Gilovich 2006, a22, snippet only) or from selective retrieval of anchor-consistent knowledge. Simmons, LeBoeuf and Nelson (2010, a18) add a boundary: accuracy motivation reduces anchoring only when people know which direction to adjust.
5. **Resource-rational anchoring (Lieder et al. 2018, b08, b09).** A sampling-based adjustment with a cost-benefit stopping rule fits ten anchoring phenomena, including load and incentive effects.
6. **Dual-process individual differences (Toplak, West, Stanovich 2011, b06, b26).** The three-item CRT predicts performance on heuristics-and-biases tasks beyond intelligence and thinking dispositions. "Miserly" processing is a trait separate from ability.
7. **Bayesian sampler (Zhu and Griffiths 2024, a23).** Probability judgments are noisy samples pulled toward the middle by a prior. This explains incoherent judgments in people and LLMs with one model.
8. **Metacognitive myopia (Scholten et al. 2024, c22).** Conceptual claim that LLMs track the frequency of cues in context, not their validity or sample size. No new data.

### 2.4 The Kahneman-Gigerenzer dispute in one paragraph

Gigerenzer's side: many "errors" come from narrow norms and vague heuristics, and wording or format can remove, restore or invert them. Kahneman and Tversky's side: frequency judgments are also biased, and the effect survives within-subject and between-subject designs. The data say both are partly right. Frequency wording cuts Linda violations from a median 87 to 17 percent across the literature (d02), but only about 30 of those 70 points come from response mode alone, and one study found almost no effect (85 vs 81 percent, Jones et al. 1995, b03). The error is never zero in the probability format and not always zero in the frequency format.

---

## 3. Core findings with exact numbers

Status here is the claim status in claims.jsonl, adjusted where the critique requires. "H" = human study, "L" = LLM study.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| H. Base rates ignored when any description is present (engineer/lawyer) | Bayes odds ratio should be 5.44; subjects gave "essentially the same" answers. Worthless description: .5 in both groups. No description: .7 and .3 used correctly. 1973 data: mean 50 percent (low-engineer group, N = 85) vs 55 percent (high-engineer group, N = 86), t = 3.23, df = 169 | a02, a07 (K01) | [E] |
| H. Tom W.: likelihood tracks similarity, not base rates | likelihood vs similarity r = .97; vs base rate r = -.65; over 95 percent said computer science more likely than humanities or education; only 24 percent considered the description might be inaccurate | a06 (K01) | [E] |
| H. Cab problem: base rate suppressed | 85 percent blue cabs, witness right 4 in 5. Base-rate-only group median 80 percent (N = 36); with witness median 20 percent (N = 35); Bayes about 41 percent | a07 | [E] (original data; causal-base-rate boundary below) |
| H. Base-rate neglect depends on design | Weaker in within-subject designs; "disappears" in Varey, Mellers, Birnbaum 1990 (secondhand); weaker with natural frequencies | b04, a13 (K02) | [C] |
| H. Linda, standard wording | 85 percent (Linda) and 87 percent (Bill), N = 88 undergraduates; 12 of 12 direct tests violated, overall 88 percent; probability and representativeness ranks correlate .96 and .98 | a09 (K03) | [E] |
| H. Linda re-run | 83 percent (15 of 18) in Study 1; 88 percent (21 of 24) and 82 percent (18 of 22) in Study 2 standard conditions | b02, d02 (K03, K34) | [E] |
| H. Statistics training only partly helps | Graduate students with statistics credit (N = 64): 36 percent still erred. Betting wording: 56 percent violations (n = 60). "Whether or not" wording: 57 percent (n = 75). Resemblance argument chosen: 65 percent (n = 58) | a10 (K03) | [E] |
| H. Conjunction error across domains | Medical (5 problems) mean 91 percent, range 73 to 100; Borg tennis 72 percent (N = 93); sub-4-minute mile 76 percent (N = 96); earthquake/flood geometric means 3.1 vs 2.2 percent (N = 245) | a11 | [E] (1980s student samples; problems built to elicit error) |
| H. Linda wording and format effects | Health-survey item: 65 percent (percent wording, N = 147), 25 percent ("how many of 100", N = 117), 11 percent (estimate base group first, N = 360). Literature median: 87 percent probability ranking vs 17 percent frequency estimation; response mode alone about 30 of the 70 points. Frequency vs probability: 58 vs 25 (T and K); 73 vs 23 (Fiedler); 59 vs 35 (Reeves and Lockhart); 85 vs 81 (Jones et al., no effect). Clarifying phrase 89 to 57 and 77 to 56; Politzer and Noveck 77 to 29; betting 89 to 56 | a10, b02, b03, d02 (K04) | [C] |
| H. Pragmatic reading of "probable" | 7 of 39 paraphrases (18 percent) mathematical; 18 different meanings across 39 paraphrases | b25, d02 (K05) | [E] |
| H. Inverse conjunction effect | Exp 1: unmodified sentences got 21 percent more yes responses; Exp 2: inverse conjunction on 56 percent of pairs; quantifier changes barely moved it | a16 | [S] |
| H. Natural frequencies and Bayes | Study 1, 60 students, 15 problems: Bayesian algorithms 16 percent (probability, standard menu) vs 46 percent (frequency); short menu 28 vs 50 percent. Format effect about 3 times the menu effect | a13 (K06) | [C] |
| H. Frequency gain is carried by numerate people | N = 346; high numeracy n = 190, low n = 156; format by numeracy interaction; Down's item 47.62 percent, drunk-driving item 9.91 percent correct | a14 (K06) | [C] |
| H. Sample-size insensitivity | Hospital item (1974): larger hospital 21, smaller 21, "about the same" 53. Student sample N = 346: hospital item 28.6 percent correct, squash item 15.6 percent | a03, b06 (K07) | [E] |
| H. No regression toward the mean | Predictions from a measure said to be unreliable were as extreme as from a reliable one (N = 32, 37 per group; no significant difference). Student sample: 40.2 percent solved the regression item | a08, b06 (K08) | [E] |
| H. Numeric anchoring, founding | Wheel of fortune: median 25 vs 45. Factorial in 5 seconds: ascending 512, descending 2,250, true 40,320. Payoffs did not remove the effect | a04 | [E] |
| H. Numeric anchoring, Many Labs 1 | 36 samples, 6,344 participants in the whole project. Replication d medians: babies born 2.43, Everest 2.00, Chicago 1.88, NYC distance 1.18. 36 of 36 samples in expected direction for all four items. Original aggregate d = 0.93 (different design). Group means low vs high anchor: babies 3.2k vs 26.7k; Chicago 1.03m vs 3.00m | d01, b01, a19 (K09, K34) | [E] |
| H. Anchoring heterogeneity | Q up to 312.75 (Chicago), 152.34 (Everest); no setting variable above partial eta squared .022 | b24, d01 (K31) | [S] |
| H. Accuracy motivation and direction | Miami temperature item: only 41 percent believed they adjusted too little with a plausible anchor; more than half with an implausible one. Incentives help when direction is known | a18, b09 (K10) | [E] |
| H. Resource-rational anchoring model | Simulated adjustments fell 18.61 percent under load (83.45 vs 102.06 relative adjustment); about 14 vs 60 adjustments | b08 (K10) | [E] (as model) |
| H. Availability | Committees: medians 70 (size 2) and 20 (size 8), true 45 | a05 | [E] (1974; not re-run in this folder) |
| H. Overconfident intervals | 98 percent intervals missed the truth for about 30 percent of problems | a05 (K30) | [S] for human; see LLM rows |
| H. CRT predicts bias-task performance | N = 346; CRT mean 0.7 of 3; 55.8 percent solved none; CRT r = .49 with rational-thinking composite, cognitive ability r = .41; extra variance delta R squared about .025, .080, .064 | b06, b26 (K28) | [E] |
| H. Percent correct on classic tasks (students) | Causal base rate 53.8; hospital 28.6; squash 15.6; regression 40.2; gambler's fallacy 69.4 and 92.2; conjunction 19.1; covariation 36.1; Bayes 22.3; framing 62.7; sunk cost 64.2; outcome bias 72.0 | b06 | [E] |
| H. One-session training | Game and video; N = 238 lab (156 game, 82 video), 192 follow-up. Overall bias d: game 1.74 post, 1.16 follow-up; video 1.75 and 1.07. Anchoring d: game .70 / .63; video .80 / .66. Representativeness d: game 1.51 / 1.05; video 1.80 / 1.09. Projection game 1.11 / .54 | b07 (K12) | [S] |
| L. GPT-3.5 anchoring | Book-count item: means 20.83 (low) vs 105.97 (high), t(58) = 8.78; humans 22.5 vs 80.50, t(58) = 5.55. GPT-4: 22.0 vs 94.33 (5 trials each) | a24, b12, c08 (K14) | [E] |
| L. GPT-3 anchoring (Jacowitz and Kahneman items) | 14 questions; landed exactly on the anchor 67 percent of the time; 41 percent of outputs gibberish | c04, a27 (K14) | [E] |
| L. Expert-labelled hints anchor GPT-4 class models | 12 of 12 expert-hint questions showed significant anchoring in all models; 62 questions, 11 exceptions in the grid, 9 of them GPT-3.5; GPT-4 anchoring index 0.45 vs 0.61 human; stronger models more consistently anchored | a28, b14, c11 (K14) | [E] |
| L. Anchoring share across 11 models (SynAnchors) | Anchored share of 100 questions: Qwen2.5-0.5B 60.5, Llama-3.2-1B 57.1, Mistral-7B 51.1, GPT-4o-mini 37.0, Llama-3.1-8B 34.7, GPT-4o 27.3, DeepSeek-R1 25.0, Qwen3-235B thinking 22.0 percent | c12, d09 (K14, K15) | [E] |
| L. Anchoring across 20 models (Malberg) | Anchoring score mostly 0.29 to 0.67; availability 0.02 to 0.26; no clear size or capability link | c14 (K14) | [E] |
| L. Anchor pathways (AnchorBench, 14 models, 360 items per suite) | Mean anchor influence, irrelevant / plausible: prompt 0.05 / 0.22; own earlier answer (History) 0.05 / 0.34; tool result 0.07 / 0.18; retrieval 0.03 / 0.13; demonstrations 0.02 / 0.03. Frontier models: irrelevant about 0.00 to 0.03, plausible 0.07 to 0.16 in the prompt. Plausible anchors raised mean error by +3.6 points | d06 (K29, K33) | [E] for pathway ordering (with a29, d08); [S] for frontier detail |
| L. Prior score in context moves judges | 8 models, 185,271 valid calls: shift in 7 of 8; GPT-4.1 d -0.67, Claude-4.5-Sonnet d -0.44, Llama-3.2-3B d -0.71 | d08 (K29) | [S] |
| L. Earlier user turn raises bias | Presence effect positive in 7 of 8 models (Llama-3.1-8B +0.086 ... Claude-3.5-Haiku -0.101) | d16 (K29) | [S] |
| L. Sequence effects in decisions | Llama models changed 40 to 52 percent of decisions between sequential and all-at-once setups; GPT-4 admitted 40.5 percent more students under "reject" framing | a29, b16, c16 (K29) | [E] |
| L. Anchoring needs no prior of the model's own | gpt-oss-120B anchoring index 0.000 on grounded facts and 0.90 to 1.01 on invented quantities (human about 0.49) | d12 (K36) | [S] |
| L. Anchoring falls with confidence | Susceptibility falls as confidence rises, right or wrong (abstract only) | d18 (K36) | [S] |
| L. Anchor lives in shallow layers | Causal tracing: anchor tokens matter in early layers; circuits transfer within a model, not reliably across base and tuned variants | c12, a33, b21, d09 (K27) | [E] |
| L. Agents anchored by first offer | Seller utility baseline / anchored / buyer informed: GPT-4o 0.61 / 0.98 / 0.92; GPT-4 0.37 / 0.91 / 0.78; Llama 3 0.15 / 0.78 / 0.59; Qwen2.5 0.55 / 0.96 / 0.76. 322 simulations | c13, d10 (K24) | [S] |
| L. Code models anchored by wrong earlier function | Codex baseline 32.9 percent; 2.4 to 10.6 percent framed; framing line copied in 81 vs 4.5 percent of outputs; accuracy drop 22.3 to 30.5 points | a27, b13, c03 (K25) | [S] |
| L. Linda, GPT-3 | Chose the conjunction (single prompt) | c01, a25 (K18) | [C] |
| L. Linda on 1,024 new vignettes | Accuracy Linda items: GPT-3 family 0.46, humans 0.56, ChatGPT 0.70, GPT-4 0.98. Bill items: GPT-3 0.53, humans 0.83, GPT-4 0.99. davinci-003 step-by-step prompt: +0.39 (Linda). Option order mattered in models, not in humans | d11 (K18) | [S] |
| L. Cab, hospital, CRT, GPT-3 | Cab approximately correct; hospital "about equal"; CRT 3 of 3 intuitive wrong | c01, a25 (K18) | [C] |
| L. Vignette edits break GPT-3 | Black cab (colour not in the data) got 20 percent; Wason order reversed flipped the answer; CRT with false premise still 10 cents; 4 of 4 perturbations failed | c02, b10 (K18) | [C] |
| L. CRT by model | 150 CRT tasks: humans 38 correct / 55 intuitive; davinci-003 5 / 80; ChatGPT-3.5 59 / 15; ChatGPT-4 96 / 0. Semantic illusions: davinci-003 72 percent fell, 18 correct; ChatGPT-3.5 74 correct; ChatGPT-4 88 correct. CoT on davinci: correct 5 to 28, intuitive 80 to 29. Blocking CoT for ChatGPT-4: 95 to 88 correct | a26, c05, c06 (K17) | [E] |
| L. Representativeness hardest for LLMs | Knipper (45 models, 2.8 million responses): bias-consistent 17.8 to 57.3 percent; representativeness resistance 0.36 to 0.60, lowest of the family; anchoring resistance 0.49 to 0.79; size over 32B reduces bias in 39.5 percent of cases. REHEAT: GPT-3.5 34.7, GPT-4 31.2, LLaMA-2-70B 27.2, PaLM 2 14.8 percent vs 153 humans 27.2 percent | b18, c15, c09 (K13) | [E] |
| L. Hints on REHEAT | General hint GPT-4 36.6 (+5.4); specific hint 46.5 (+15.3); PaLM 2 +11.8; one-shot GPT-4 +5.2 (to 36.4), LLaMA +14.5; zero-shot CoT GPT-3.5 -4.0, GPT-4 +3.9 | c09, c10 (K23) | [S] |
| L. Classic tasks: errors mostly not human-like | 7 models, 12 tasks, 10 runs each: GPT-4 correct with correct reasoning 69.2 percent; Claude 2 55.0; Llama-2-7b wrong in 77.5; human-like bias with wrong answer: GPT-3.5 21.7 percent (50.8 including human-like correct); GPT-4 human-like 73.3; Llama-2-13b 8.3 | a30, b17, c07 (K19) | [C] |
| L. Probability judgments incoherent in the human direction | 4 models (GPT-3.5, GPT-4, LLaMA-2 7b and 70b); identities (negation, conjunction, disjunction) broken; inverted-U mean-variance relation | a23 (K19) | [S] |
| L. Tuning and bias | Belief-invalid bias: base davinci 0.00, text-davinci-002 0.55, text-davinci-003 0.65; belief-valid 0.00, 0.19, 0.21. CRT trap removed by tuning | b15, a26 (K20) | [C] |
| L. Reasoning models and anchoring | 30 vignettes, 12,350 calls: reasoning vs sibling delta = +0.031, t(29) = 1.45, p = .157; anchoring d = 1.89; bias does not fall with thinking tokens (0, 1,024, 4,096, 8,192) | a34 (K15) | [C] |
| L. Generic debias prompt | Judgment accuracy -4.4 percent (backfire) vs response-position +40.5 percent; baseline judgment shifts -4.3 (GPT-4o-mini), -7.7 (Llama-3.3-70B), -2.7 (Qwen2.5-72B) points; steering cut bias 26 to 32 percent at up to -19.0 points capability (Qwen) | a35, b19, c18 (K21) | [C] |
| L. Interval overprecision | GPT-4o-mini coverage 0.63 / 0.59 / 0.64 at nominal 0.90 / 0.95 / 0.99 (500 test Fermi questions). Eleven LLMs at 95 percent: 9 to 44 percent coverage; reasoning effort no help. Hit rate flat from 60 to 95 percent requested; |r| of length with level up to .014. Conformal recalibration restores coverage (Winkler score -25.2, -27.8, -59.4 percent) | d03, d04, d05 (K32) | [E] |
| L. Natural frequencies | No model used natural frequencies unprompted (3 reasoning models, 1 problem); prompted 3 of 3 correct but reasoning flawed in several | b23, c21, d14 (K26) | [S] |
| L. Code beats wording on probability | GPT-4: basic 18 percent, CoT 32, PAL 54, Monte Carlo 86, ProbLog 97 | d21 (K35) | [S] |

---

## 4. Mechanisms and models

This section is written so an engineer could build each piece. Where a mechanism is only a proposed reading, it says so.

### 4.1 Representativeness as a similarity read-out

Human model. Given a description D and categories C1..Cn, the person scores sim(D, Ci) and ranks by it. The prior P(Ci) is available but unused. Evidence: likelihood vs similarity r = .97, vs base rate r = -.65 (a06). The prior is used when no description is given and ignored when a worthless description is given (a02).

Implementable form for the agent:
1. Detect "description plus category question" items in S1: a person or object description, a list of categories, a request for probability.
2. In code, build a table: category, stated prior (from the task or absent), model's likelihood of the description given category.
3. Combine by Bayes in code (odds = prior odds x likelihood ratio). The model supplies only the likelihood ratio. Do not ask the model to multiply.
4. Report both the model's raw ranking and the combined one. A gap between them is the bias signal (a G1-style trigger).

LLM note. Representativeness is the weakest family for LLMs (resistance 0.36 to 0.60, K13), and story-wrapped versions are harder than bare statistics (c10). Meaning: the model can do the arithmetic and knows the rule, but the story pulls it off.

### 4.2 Conjunction rule as a code check

Rule: P(A and B) <= P(A). Any pair of candidate statements where one adds a condition to the other can be checked without a model.

Implementation. Parse or have the model tag each candidate claim with the list of conditions it asserts. Count conditions. A candidate with more conditions must not get a higher probability than its subset claim. If it does, flag and re-ask with the counts format (4.4). The same check applies to the model's own multi-step claims: a causal story that adds detail can raise perceived probability (earthquake and flood, a11), so code should count conditions, not read plausibility.

Competing reading to keep in mind. In humans part of the error is a pragmatic reading of "probable" (b25), and an intensional account predicts the reverse pattern for universal statements (a16). A check on the model's output should therefore also fix the question wording to set inclusion ("is the set of A-and-B cases larger than the set of A cases?").

### 4.3 Anchoring and adjustment

Human model (Epley and Gilovich; Lieder et al. b08):
- Start at anchor a. Draw a sequence of adjustments toward the truth. Stop when the value looks plausible or when the cost of another step exceeds its expected gain.
- Under load or time pressure the model predicts fewer adjustments: about 14 vs 60 in the fit, a relative-adjustment drop of 18.61 percent.
- Accuracy motivation raises the number of adjustments only if the person knows which way to go (Simmons et al., a18). If direction is unknown they believe they have adjusted enough.

LLM picture, built from several papers:
- The anchor is read in shallow layers (c12, a33, d09). Circuits for low and high anchors transfer within a model but not reliably across base and instruction-tuned variants (a33, b21). So a fix tuned on one model version may not carry to the next.
- Influence is graded and depends on plausibility and on the model's own prior. Irrelevant numbers move frontier models almost not at all (0.00 to 0.03), plausible-but-wrong ones move them 0.07 to 0.16 in the prompt and 0.34 when the number is the model's own earlier answer (d06). With no prior at all (invented quantities) anchoring approaches 1.0 (d12). Susceptibility falls as confidence rises (d18).
- Part of the shift can be rational: a plausible number is evidence when it is the only signal (d06, d12).

Implementable rules from this:
1. **Classify each number in the input** as evidence, task-given constant, or non-evidence (a stated guess, a counterparty offer, an earlier attempt's answer, an authority's claim). Code does the classification as far as it can (position, source tag); the model labels only the ambiguous ones.
2. **Move non-evidence numbers out** of the estimation context into a marked block shown only after an independent first estimate, or not at all.
3. **Never let an attempt see another attempt's number.** Echo of own earlier answer is the strongest pathway (0.34; d06).
4. **Evaluate items in separate contexts.** Earlier scores and earlier user turns shift later judgments (d08, d16); a running context also keeps own confidence drifting (d15).
5. **Two-sided bracketing is an untested-on-current-models option.** Showing a low and a high hint that straddle the truth brought GPT-4 close to the no-anchor value on 8 of 15 questions (c11, b14). It needs the truth to lie between the hints, so it is a code-side construction, not a model instruction.

### 4.4 Frequency format and counts rewrite

Human model. Natural frequencies keep the base rate in the counts, so P(H|E) = (hits) / (hits + false alarms) is a single ratio. Gains: 16 to 46 percent Bayesian algorithms (a13); health-survey conjunction item 65 to 25 to 11 percent (a10).

Implementation: code rewrites "P(disease) = 1 percent, P(positive | disease) = 80 percent, P(positive | no disease) = 10 percent" into "out of 1,000 people, 10 have the disease; 8 of those test positive; of the 990 without it, 99 test positive" and then does the division. The rewrite must be done by code. Reasoning models do not choose counts on their own and use them inconsistently when told to (b23, c21, d14).

Boundary. The human gain depends on numeracy (a14), and the large LLM gains on probability tasks came from code or simulation (GPT-4 18 to 86 to 97 percent; d21), not from wording. So the likely best rule is: count rewrite plus code arithmetic. Whether the rewrite alone adds anything for a current model is not known (K35).

### 4.5 Sample size and regression

Both are statistical facts the model can state when asked (the model usually knows the rule; c10). The failure is that the story hides which rule is relevant.

Implementation as a pre-answer check in S0 or S1: code (or a tiny routed model call) tags the item for "has a sample or n", "predicts from a noisy cue", "has a stated class proportion". If tagged, the answer step must first write the n, the base rate or the reliability, and a shrink step: pred = mean + r x (cue - mean), with r supplied by the task or by code. Evidence that the naming step helps: REHEAT specific hints +15.3 points for GPT-4 (c10), but hints were hand-written per bias type and leak the task type, so the effect on spontaneous items is unknown.

### 4.6 Calibration

Observed: LLM intervals are too narrow, and the stated level barely matters (d03, d04, d05). Mechanism: nothing in the model links the word "90 percent" to interval width.

Implementation: collect (stated interval, truth) pairs on checkable items from the agent's own domain. Fit a single widening factor by split-conformal calibration. Apply it to every interval the agent reports. This restored near-nominal coverage in d03 and d04.

### 4.7 Why the model is not a human

Different causes for different effects (c23): CRT-style trap errors first rise with scale and then vanish with instruction tuning and chain of thought. Cue-contamination effects (anchoring, representativeness) do not follow this reversal. So a stronger model does not need less S1 hygiene.

---

## 5. What holds up

### 5.1 Replications and robustness (human)

| Effect | Verdict | Evidence |
|---|---|---|
| Numeric anchoring | Replicates very strongly. 36 of 36 samples, d 1.18 to 2.43, larger than the original (the original number is from a different design). Flag priming (0.02) and currency priming (0.00) did not replicate, anchoring did | d01, b01, b24 |
| Gain/loss framing | Replicates at about half the original size (0.58 to 0.60 vs 1.13) | d01, b01 |
| Linda | The error replicates in the standard probability ranking at 82 to 88 percent. No failed replication of the standard design was recorded. The rival result is about interpretation, not about the raw rate | a09, b02, d02 |
| Base-rate neglect | Reduced or absent when the same subjects see both base-rate conditions; moderated by causal relevance (Bar-Hillel, Koehler; named, not opened); format-dependent | b04, a13 |
| Sample-size insensitivity, regression neglect | Hold in student samples at low solution rates (15.6 to 40.2 percent correct). Not stress-tested against failed replications in this folder | b06 |
| Availability | 1974 results not re-run here. Experienced-ease versus content separation (Schwarz et al. 1991) not opened | a05 |
| Calibration overconfidence | 98 percent intervals missed about 30 percent in 1974; human re-runs not collected here | a05 |

Critique caveats (critique.md): Many Labs 1, Hertwig and Gigerenzer and the 1983 paper were re-opened at source for the key numbers only in part (d01, d02). The 1983 numbers were consistent across lines but not fully re-verified. The human literature after 2015 on Linda outside Hertwig and Gigerenzer is thin in this folder.

### 5.2 Moderators that matter

- **Format.** Counts and frequency wording cut Linda errors by 20 to 60 points in most studies (b03), never fully in the probability format. They did not help in Jones et al. (85 vs 81 percent; b03) or for base-rate neglect in older adults (a15).
- **Design.** Within-subject presentation weakens base-rate and conjunction effects (b04, K02).
- **Numeracy.** Frequency gains concentrate in high-numeracy people (a14). The CRT predicts bias-task performance beyond intelligence (b06).
- **Direction knowledge.** Accuracy motivation helps against anchoring only when direction is known (a18).
- **Uncertainty and expertise.** More uncertainty about the quantity gives more anchoring. Experts are reduced but not immune (b09).
- **Anchor distance.** Effect grows with distance, then flattens for absurd anchors (b09).
- **Training.** One session with feedback reduced bias at 8 to 12 weeks (b07), but by one team and with self-built measures of low reliability (.52 to .62 for the anchoring subscale).

### 5.3 What worked and what did not as an intervention

Human:
- Worked: a counts / "how many of 100" reformulation (a10); a clarifying phrase (89 to 57 percent) and rephrasing (77 to 29 percent) (b03); a one-session game or video with feedback (b07).
- Did not work, or only partly: telling people the rule; statistics training (36 percent still erred); a betting format (56 percent still erred); paying for accuracy against a provided anchor with unknown direction (a04, a18).

LLM:
- Worked: removing the cue; showing both a low and a high hint that bracket the truth (c11, b14); computing with code or simulation (d21); a short "use only task evidence, ignore extraneous numbers" line on two 7 to 8B models (mean -0.12 in anchor discrimination in 4 of 4 cells; d07); iterative detect-and-rewrite when the bias is an injected cue (SACD: FOMC Llama-3.1-8B bias 0.157 vs vanilla 0.3805; c17, d13); conformal recalibration for intervals (d03, d04); hand-written specific hints on REHEAT (c10); same-template worked examples with correct, non-intuitive answers for davinci (c06, b28); "set your own criteria first" on one model (34.7 to 24.7 percent; d09).
- Did not work, or backfired: chain of thought, thoughts of principles, "ignore the hint" and reflection on GPT-4 class models with expert hints (a28, b14, c11); "think carefully" (Llama 34.7 to 36.8) and a reflection turn (38.4) on SynAnchors (d09); a self-check turn (Qwen-7B 0.26 to 0.45, d07); CoT for a judge (-0.429 to -0.633, d08); a generic bias reminder for judgment biases (-4.4 percent, c18); more thinking tokens, 0 to 8,192 (a34); more reasoning effort for intervals (d04); few-shot debiasing and counterfactual prompts, which pushed Llama-2 to near 0 or 1 admit rates (c16); few-shot with intuitive examples (b28); multi-agent debate (SACD paper bias 0.5020 vs vanilla 0.3805; c17).
- Mixed: awareness reminders (helped five biases on GPT-3.5, two on GPT-4, not the anchoring tasks; c19); telling a buyer model that the seller anchors (GPT-4o 0.38 to 0.32, o1 0.40 to 0.20, QwQ 0.26 to 0.00; d10); a restate-the-anchor line (lowered anchoring on all five items, p = .057; a34).

### 5.4 Contradictions that are not resolved

1. **Do reasoning models anchor less?** SynAnchors: yes (DeepSeek-R1 25 percent, Qwen3 thinking 22 percent vs 60.5 for Qwen2.5-0.5B). Kraishan: no (delta +0.031 ns; d = 1.89). Lou and Sun: stronger models more consistently anchored by expert hints. Different metrics, items and models (K15, [C]).
2. **Does "ignore it" work?** Failed on GPT-4 class models with expert hints (b14, c11); worked a little on two 7 to 8B models with irrelevant numbers (d07). The hint type differs (expert claim vs irrelevant number) and the models differ (K16, [C]).
3. **Does tuning raise or lower bias?** Raises belief and decoy bias (b15); removes the CRT trap (a26). Direction depends on the bias (K20, [C]).
4. **Are LLM errors human-like?** Mostly not across tasks (a30); yes in direction for anchoring, conjunction and probability incoherence (a23, a24). Different measures (K19, [C]).
5. **Debiasing prompts.** Generic reminder backfires on judgment biases (c18); awareness helps some (c19); iterative rewrite helps strongly on injected cues (c17). Different models, metrics and bias definitions (K21, K22).

---

## 6. Language models

### 6.1 Which classic effects appear

| Task | LLM result | Notes |
|---|---|---|
| Numeric anchoring | Present in every study that tested it. GPT-3.5: 20.83 vs 105.97 (human 22.5 vs 80.5). GPT-3: exactly on the anchor 67 percent. SynAnchors: 22 to 61 percent of questions anchored. Malberg: scores 0.29 to 0.67 | a24, c04, c12, c14 |
| Linda (conjunction) | GPT-3 falls; ChatGPT 0.70 on new vignettes; GPT-4 0.98 on 1,024 new vignettes | d11 (2023 models only) |
| Base rate (cab) | GPT-3 near-correct; adversarial edit gave 20 percent | c01, c02 |
| Base rate and other representativeness (REHEAT) | 14.8 to 34.7 percent, near human 27.2 percent | c09 |
| Sample size (hospital) | GPT-3 "about equal" | c01 |
| CRT | Rises then vanishes: davinci 80 percent intuitive, ChatGPT-3.5 15, ChatGPT-4 0 | a26 |
| Availability | Weak (0.02 to 0.26) | c14 |
| Framing | Asian-disease: risky choice 45 percent (save) vs 74 percent (die) in GPT-3, humans 28 and 78; Codex format framing 81 vs 4.5 percent copy | c04, b13 |
| Overconfident intervals | Coverage 9 to 63 percent at stated 90 to 99 percent | d03, d04, d05 |
| Probability incoherence | Present in the human direction in 4 models | a23 |

### 6.2 What changed the effect, and by how much

- **Model scale and training.** CRT traps: strong scale effect then reversal (a26). Anchoring: no clean scale effect (c14, a28); size over 32B reduces bias in 39.5 percent of cases (b18). Resistance averages 0.45 (Llama-3.2-1B) to 0.82 (o4-mini and a Claude model) (c15).
- **Reasoning budget.** Does not lower bias across 0 to 8,192 thinking tokens (a34). Forced chain of thought: davinci intuitive 80 to 29 percent (c06) but GPT-4 only 95 to 88 correct when blocked (a26, so little to gain at the top). REHEAT: CoT +3.9 for GPT-4, -4.0 for GPT-3.5 (c09).
- **Prompt detail.** More detailed, context-rich prompts reduced most biases by up to 14.9 percent and raised overattribution by up to 8.8 percent (b18).
- **Cue location.** Own earlier answer 0.34 > prompt 0.22 > tool result 0.18 > retrieval 0.13 > demonstrations 0.03 (d06). The first scenario in a repeated task persisted: 77.5 percent same-direction adjustment, then 80.0 percent after the switch (d17, weak).
- **Cue plausibility.** Irrelevant numbers barely move frontier models; plausible wrong ones do (d06). Expert-labelled hints are followed almost always (12 of 12 questions; b14).
- **Cue novelty.** With no prior, anchoring is near 1.0 (d12).
- **Option order.** Mattered strongly in models and not in humans on Linda vignettes (d11).
- **Fix type.** See 5.3. Removing the cue worked; talking about the cue mostly did not.
- **Model version.** The vendor patched the public Linda example within a day (b12). Fixes to famous items are patches, not general repair. Circuits differ between base and tuned versions (a33).

### 6.3 Contamination

Famous vignettes are likely in training data. Small edits broke GPT-3 (c02). But on 1,024 newly written Linda/Bill vignettes GPT-4 scored 0.98, so strong-model success on conjunction items is not only memory (d11). In PsyAgentBench, textbook wording vs matched counterfactual content changed Asch conformity of Llama 3.3 70B from 46.2 to 3.8 percent, and of gpt-oss-120B only from 96.7 to 85.8 percent, so some "human-like" effects depend on recognising the named paradigm (d12). No 2025 to 2026 model was tested on perturbed Linda, cab or hospital items (K18).

### 6.4 Agent-setting evidence

- Negotiation: a high first offer lifted seller utility (GPT-4o 0.61 to 0.98). Informing the buyer helped little (0.92). Reasoning-model buyers recovered more. Persona gave no protection (c13, d10).
- Code: a wrong earlier function lowers Codex from 32.9 to 2.4 to 10.6 percent when framed (a27, c03).
- Judges: prior scores in context shift 7 of 8 models (d08).
- Planning: a 1B model clung to its first proposal in a 6G simulation; a randomised first proposal gave up to 25 percent energy saving (d20, low weight).
- Operations: GPT-4 deviated up to 70 percent more than human benchmarks in a newsvendor task, and kept the early-round direction (d17, weak).

### 6.5 Caveats for the whole section

Single prompts per cell, temperature 0 or one sample, small item sets (critique weak spots). Anchoring scores are logit difference, anchoring index, anchored ratio or utility, so numbers do not compare. Debiasing results are bias scores, not accuracy at equal tokens, and token cost is rarely reported. No LLM study of the exact 1974 98-percent almanac design exists.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### 7.1 Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Treat every number in the input that is not evidence (a stated guess, a counterparty offer, an authority's figure, an earlier attempt's answer) as an anchor. S1 code moves it out of the estimation context. Human anchoring is large and stable, and LLM anchoring is present in every study. The removal step itself has no direct equal-token test, but it is the only fix with a clear mechanism. | S1 | [E] for the harm; the remedy stays [S] as in SCHEMA.md | a24, b14, c12, d01, d06; K09, K14 |
| 2 | Each attempt and each item is evaluated in a fresh context. Own earlier answers are the strongest anchor pathway (0.34 vs 0.22 prompt). Earlier scores and earlier user turns shift later judgments. | S3, S1 | [E] | d06, d08, d16, a29, c16; K29 |
| 3 | Do not use thinking budget, "think carefully", "ignore the hint", reflection, or a generic bias reminder as the anchor fix. Evidence points away from them for expert hints and judgment biases. (Already in SCHEMA.md section 4b; this adds the anchoring-specific data.) | G11, 4b | [E] for budget and generic reminder not being enough; [C] for the exact "ignore" line | a34, c18, b14, c11, d09; K15, K16, K21 |
| 4 | Never use a stated confidence level as a number. Model intervals cover 9 to 64 percent when 90 to 99 percent was asked, and more reasoning did not widen them. If the agent reports ranges, apply a widening factor fitted on checkable items. | G, memory | [E] | d03, d04, d05; K32 |
| 5 | Test items for the agent must be fresh or mutated, with randomised option order. Famous vignettes are likely memorised; option order moves models, not people. | G3 | [E] for the principle (G3); the quantitative contamination size is [C] | c02, d11, d12; K18 |
| 6 | Judge an answer by checks, not by the reasoning story. Graded chains showed correct answers from wrong reasoning and the reverse. | G10 | [E] | c25, a30, c07 |
| 7 | Keep all non-evidence cues out of the voting context too: same-model samples share the anchor, so agreement across attempts is not proof the anchor was resisted. | G4 | [E] | a28 (stronger models more consistent), a30; G4 |
| 8 | Do arithmetic for probability items in code, not in the model's head (Bayes combination, normalising, identity checks). | G5 | [S] on LLM effect size (GPT-4 18 to 86-97 percent, one paper); [E] that the model does not do it itself | d21, b23, c21, a14 |

Item 8 is listed here because it fits G5 (code selects and normalises) and costs almost nothing, but the effect size is single-source; the schema should log it as [S] until the test in UNKNOWNS passes.

### 7.2 Test first (not established)

| # | Candidate | Schema part | Status | Evidence | Why it is not yet [E] |
|---|---|---|---|---|---|
| T1 | Strip or label non-evidence numbers vs thinking budget at equal tokens, on anchored numeric items | S1 | [S] (a34 p = .057, five items) | a34, d07 | No equal-token comparison exists (critique GAP 1) |
| T2 | Short "use only task evidence; ignore extraneous numbers" line | S1 | [C] | d07 vs b14, c11 | Worked on two 7 to 8B models, failed on GPT-4 class models with expert hints |
| T3 | Tag each number as evidence or non-evidence, then compare error on plausible-but-wrong values | S1 | [S] | d06 | One benchmark; some anchor shift is rational |
| T4 | "State whether the number is too high or low, then answer" (direction first) | O | [S] | a18, d10 | Human-only mechanism; no LLM test of direction knowledge vs accuracy instruction |
| T5 | Counts-format rewrite for conjunction and Bayes items, by arithmetic difficulty | S1/O6 | [C] | a13, a14, b03, d14 | Human gains vary; no 2025 to 2026 LLM test |
| T6 | Name the base rate and sample size first, then answer | S1/O | [S] | c10 | Hints were hand-written per bias type; old models |
| T7 | Code-checked conjunction and probability-identity check with re-ask in counts form | G | [S] for LLM effect | a09, a23, d11 | Unknown how often current models violate; Linda is solved by GPT-4 on new vignettes |
| T8 | Detect-and-rewrite loop (SACD-like) vs one-pass restate | S1/O | [S] | c17, d13 | Round 1 can hurt; 3 to 9 extra calls; bias defined as cue-following |
| T9 | Two-sided bracketing hints when the agent must use a hint | S1 | [S] | b14, c11 | One paper, two high-school authors |
| T10 | Randomised first guess or first proposal in search seeding | S3 | [S] | d20 | 1B model, simulation |
| T11 | Few-shot examples of own past anchored errors with corrections | memory | [S] | b07 | Human training result, one team; LLM few-shot debiasing often broke models |
| T12 | Conformal widening factor for stated ranges | G | [E] for the need, [S] for transfer to our domain | d03, d04 | Need own checkable items |
| T13 | Place a hint after the first independent attempt rather than before | S1 | [S] | b14 (suggested), SUBFIELDS question (c) | Suggested, not measured |
| T14 | Mark the origin of each number ("this came from the counterparty / an earlier guess, so it probably pulls up") | S1 | [S] | d10 | The direction was obvious in the negotiation study |

---

## 8. Concrete tests on our bench

General rules for all tests: both arms get the same token budget, including any setup tokens; items are fresh or mutated, with option order randomised; at least 40 items per arm and 3 samples per item, each in a fresh context; report accuracy or shift with a bootstrap interval; log tokens per item.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1. Anchor strip vs budget | 40 numeric estimation items with a checkable truth (population, dates, counts), each with an irrelevant number and a plausible-wrong number, and a no-anchor control | (a) plain; (b) plain with extra thinking tokens equal to the strip cost; (c) code strips or labels the number; (d) restate-the-anchor line | Anchor shift = (estimate under high anchor - estimate under low anchor) / true value; also absolute error | (c) cuts shift most (more than half); (b) no gain (a34, d04); (d) small gain |
| B2. Evidence label | Same items, with both plausible-wrong and plausible-right anchors | (a) plain; (b) each number tagged "evidence / not evidence" by code | Error on wrong anchors vs error on right anchors | Error on wrong falls; error on right does not rise (otherwise the tag only removes information) |
| B3. Own-answer anchor | 40 items scored twice | (a) second estimate in the same context as the first; (b) fresh context | Mean absolute difference from first estimate; error vs truth | (a) pulled to own first answer (about a third, d06); (b) independent |
| B4. Ignore line | Anchored items with expert-labelled hints and with irrelevant numbers | (a) plain; (b) "use only task evidence, ignore extraneous numbers"; (c) strip | Anchor shift | (b) small gain on irrelevant numbers, none on expert hints; (c) beats both |
| B5. Direction first | Anchored items where the anchor is clearly too high or clearly too low and items where it is plausible | (a) "be accurate"; (b) "the number shown is probably too high"; (c) "state whether too high or low, then answer" | Shift and error | (c) helps when direction is clear; no gain when plausible (a18) |
| B6. Counts rewrite | 40 Bayes items (20 easy-arithmetic, 20 hard-arithmetic) and 40 conjunction items, new vignettes | (a) probability wording; (b) code rewrites to counts, model divides; (c) "state the base rate first"; (d) code computes the answer from model-supplied terms | Accuracy; interaction with difficulty | (d) highest (d21 pattern); (b) gain on hard-arithmetic items smaller than on easy ones (a14 analogue) |
| B7. Conjunction check | 40 new Linda-type items in the form of pairs with a nested set; mix of plausible and implausible stories | (a) plain; (b) plain with code check P(A and B) <= P(A) and a re-ask in counts form on violation | Violation rate; accuracy | Violation rate low in both on a strong model (d11); the check matters only for weaker or smaller models |
| B8. Sample size and regression | 30 new hospital-type and 30 predict-from-noisy-cue items | (a) plain; (b) name the n or reliability first; (c) forced shrink step with r supplied by code | Accuracy | (c) > (b) > (a) on regression; smaller gain on sample size |
| B9. Perturbation | The same Linda, cab, hospital and CRT items in canonical form and mutated (colour not in the data, false premise, reordered options) | Canonical vs mutated in a plain arm | Accuracy drop | Large drop signals memory (c02); also tells us which items to retire |
| B10. Calibration | 50 checkable estimates, 90 percent ranges | (a) plain; (b) fixed widening factor; (c) "name two ways the range could be wrong" step | Coverage at the stated 90 percent | (a) 40 to 65 percent coverage; (b) near 90; (c) small gain |
| B11. Judge independence | 30 items to score on a rubric, each with a prior score available | (a) one running context; (b) fresh context per item with no prior scores | Score shift vs no-prior score | (a) shifts toward the prior (d08: d -0.4 to -0.7); (b) none |
| B12. Detect and rewrite | Anchored decision prompts with an injected cue | (a) single restate; (b) SACD-like loop, stopped at the same token total | Cue-following rate and accuracy | (b) wins on bias score but loses on accuracy once tokens are matched, unless one round is enough |

---

## 9. What does not transfer, and why

1. **The raw human error list is not the model's error list.** Across 7 models and 12 tasks, wrong answers were mostly not human-like (a30). GPT-3 failed Linda but not the cab problem (c01). So a human bias checklist is a poor guide to what to check in the model (K19, [C]). Measure per class on the model in use.
2. **Classic puzzle errors fade, cue errors do not.** CRT traps fall to 0 percent intuitive in ChatGPT-4, while anchoring stays at 22 to 25 percent in the best reasoning models (a26, c12, c23). Do not read a pass on textbook items as evidence of hygiene.
3. **Human debiasing by training does not carry.** One-session training with feedback (b07) assumes a learner who remembers. The agent has no persistent learner; the analogue (few-shot error examples) is untested and few-shot debiasing broke small models (c16).
4. **Frequency-format gains may be a human arithmetic effect.** Humans gain when counts make the division easy (a14). Models do not choose counts on their own (b23, d14), and where they solve probability tasks well the gain is from code (d21). The format effect for a current model is open.
5. **Motivation and incentives.** Paying for accuracy is a human lever (a18). An accuracy instruction in a prompt is not an incentive. The only LLM analogue (telling the buyer about the tactic) names the bias, not the direction (d10).
6. **The Linda finding at the 85 percent level.** On new vignettes GPT-4 reaches 0.98 (d11). For a strong model, Linda is not a live risk; the live risk is representativeness in story form with base rates (REHEAT 31.2 percent for GPT-4; c09).
7. **Within-subject protection.** Humans who see both base-rate conditions use base rates more (b04). Our agent sees a single item per context, which is the between-subject condition where the bias is larger. This argues for placing priors next to the case in the same slot.
8. **Activation steering.** Cut judgment bias 26 to 32 percent in CogBias (c18) but needs open weights and cost up to 19.0 points of capability on Qwen. Outside the scaffold-only constraint. Same for training methods (a36).
9. **Mechanism facts about layers.** Anchor circuits in shallow layers (a33, d09) explain why late prompt text does not undo them, but give no tool to the scaffold except that the cue should not enter the context.
10. **Negotiation results.** The anchoring there was instructed ("the seller should anchor") in a simulated setting (c13). The number it supplies for the agent is the existence of the effect, not its size.

---

## 10. Open questions

1. Does a strip or restate step at equal tokens beat extra thinking budget on anchored numeric items for current models? (Only direct evidence is a34, p = .057, five items.)
2. Does "name the base rate and sample size first" help current LLMs, and at what token cost?
3. Do Linda, cab and hospital results hold on perturbed versions for 2025 to 2026 models?
4. Does a counts-format rewrite help on conjunction and Bayes items by arithmetic difficulty, as in people?
5. Which debiasing form wins on judgment biases at equal tokens: iterative detect-and-rewrite, generic reminder or concrete rule hint?
6. How large is context-order anchoring in long agent contexts, and does a fresh context for each item remove it? (AnchorBench has no fresh-context arm.)
7. Do LLM 98 percent intervals in the exact 1974 almanac design replicate the human 30 percent miss?
8. Is the shallow-layer anchor reachable by any late instruction, or only by removing the number? (No paper tests this.)
9. Does the direction-knowledge result (Simmons et al.) have an LLM analogue?
10. How much of the plausible-anchor shift is rational use of evidence vs bias? (d06, d12 say part is rational.)
11. Does the anchor pull stay when the same value is passed as labelled evidence? (K33 test.)
12. Is the dependence of anchoring on model confidence (d18) usable as a trigger (a low-confidence flag), given that verbal confidence is unreliable (G, 4b)?
13. Not verified at source: Kahneman and Frederick 2002 (a20), Gigerenzer 1991 and the 1996 replies (a21), Epley and Gilovich 2006 (a22), and the numbers on Bar-Hillel / Koehler base-rate causality. Anything citing them stays at snippet level.
14. Reasoning-model results mostly come from preprints dated 2026 read through a fetch summary (d08, d09, d12, d16, d21), and d18 is an abstract only. Re-open before relying on them.

---

## 11. Sources

[V] = opened and read this session or by the checker. [M] = snippet / abstract / relayed only.

**Founding and human literature**

- [V] Tversky and Kahneman (1974), Judgment under uncertainty. https://www.socsci.uci.edu/~bskyrms/bio/readings/tversky_k_heuristics_biases.pdf (a01 to a05)
- [V] Kahneman and Tversky (1972/1973), On the psychology of prediction. https://scholarsbank.uoregon.edu/items/098a706d-e32d-4d73-ba06-6dd92ae502a9 (a06 to a08)
- [V] Tversky and Kahneman (1983), Extensional versus intuitive reasoning. https://pages.ucsd.edu/~mckenzie/TverskyKahneman1983PsychRev.pdf (a09 to a11)
- [V] Tversky and Kahneman (1983), Citation Classic note. https://garfield.library.upenn.edu/classics1983/A1983QG78800001.pdf (a12)
- [V] Gigerenzer and Hoffrage (1995), How to improve Bayesian reasoning without instruction. https://pages.ucsd.edu/~scoulson/203/GG_How_1995.pdf (a13)
- [V] Chapman and Liu (2009), Numeracy, frequency, and Bayesian reasoning. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7197DAAA5CC39185A3E4E02FD36A6FD0/S1930297500000681a.pdf/numeracy-frequency-and-bayesian-reasoning.pdf (a14)
- [V] Stock, Fisk and Montgomery, Measures of Bayesian reasoning performance (abstract and repository copy, year approximate). https://researchonline.ljmu.ac.uk/id/eprint/5485/3/Measures%20of%20Bayesian%20Reasoning%20Performance%20on%20Norma%20and%20Natural%20Frequency%20Tasks.pdf (a15; sample sizes not extracted)
- [V] Jonsson and Hampton (2006), The inverse conjunction fallacy. https://www.staff.city.ac.uk/hampton/PDF%20files/ICF%20JML06.pdf (a16)
- [V] Lewinski (2015), Commentary on Tversky and Kahneman 1983. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01832/pdf (a17, b05)
- [V] Simmons, LeBoeuf and Nelson (2010), Accuracy motivation and anchoring. https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Simmons-et-al.-2010.pdf (a18)
- [V] Klein et al. (2014), Many Labs 1. https://stanford.edu/~knutson/jdm/klein14.pdf (b01, b24, d01); secondary table: https://www.lesswrong.com/posts/eXwpbnSeRHTahvJAx/is-anchoring-a-reliable-cognitive-bias (a19)
- [V] Hertwig and Gigerenzer (1999), The conjunction fallacy revisited. https://pages.ucsd.edu/~scoulson/203/gigerenzer1.pdf (b02 to b04, b25, d02)
- [V] Toplak, West and Stanovich (2011), CRT as predictor. https://link.springer.com/content/pdf/10.3758/s13421-011-0104-1.pdf (b06, b26)
- [V] Morewedge et al. (2015), Debiasing decisions. https://openaccess.city.ac.uk/id/eprint/12324/1/Debiasing_Decisions_PIBBS.pdf (b07)
- [V] Lieder, Griffiths, Huys and Goodman (2018), Anchoring reflects rational use of cognitive resources. https://escholarship.org/content/qt4fk2487n/qt4fk2487n.pdf (b08, b09)
- [M] Kahneman and Frederick (2002), Representativeness revisited. https://www.cambridge.org/core/books/heuristics-and-biases/representativeness-revisited-attribute-substitution-in-intuitive-judgment/AAB5D933A3F944CFB5CB02265D376C8F (a20, catalogue page and summary only)
- [M] Gigerenzer (1991) and Kahneman and Tversky (1996) / Gigerenzer (1996) replies. https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Gigerenzer-on-Kahneman+Tversky-1996.pdf (a21, blocked; the 85 vs 20 percent figure came from a Wikipedia summary and is not used)
- [M] Epley and Gilovich (2006), Why the adjustments are insufficient. https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01704.x/ (a22, abstract page only)

**LLM and AI studies**

- [V] Binz and Schulz (2022/2023), Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a25, b10, c01, c02)
- [V] Hagendorff, Fabi and Kosinski (2022/2023), Thinking fast and slow in large language models. https://arxiv.org/abs/2212.05206 (a26, c05, c06); published version https://arxiv.org/abs/2306.07622 (b11, b28; numbers differ from arXiv v2, use v2)
- [V] Jones and Steinhardt (2022), Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (a27, b13, b27, c03, c04)
- [V] Suri, Slater, Ziaee and Nguyen (2023), Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (a24, b12, c08)
- [V] Zhu and Griffiths (2024), Incoherent probability judgments in LLMs. https://arxiv.org/abs/2401.16646 (a23)
- [V] Lou and Sun (2024), Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (a28, b14, c11)
- [V] Echterhoff et al. (2024), Cognitive bias in decision-making with LLMs (BiasBuster). https://arxiv.org/abs/2403.00811 (a29, b16, c16, c24)
- [V] Macmillan-Scott and Musolesi (2024), (Ir)rationality and cognitive biases in LLMs. https://arxiv.org/abs/2402.09193 (a30, b17, c07)
- [V] Sumita, Takeuchi and Kashima (2024), Cognitive biases in LLMs: a survey and mitigation experiments. https://arxiv.org/abs/2412.00323 (a31, b20, c19)
- [V] Itzhak et al. (2024), Instructed to bias. https://arxiv.org/abs/2308.00225 (a32, b15; a32 alone was a snippet, b15 opened)
- [V] Owusu, Wiegreffe and Feldman (2026), Localizing anchoring pathways in language models. https://arxiv.org/abs/2606.12818 (a33, b21)
- [V] Kraishan (2026), The long road to the same answer. https://arxiv.org/abs/2610.10049 (a34)
- [V] Huang et al. (2026), CogBias. https://arxiv.org/abs/2604.01366 (a35, b19, c18)
- [V] Knipper et al. (2025), The bias is in the details. https://arxiv.org/abs/2509.22856 (b18, c15)
- [V] Saeedi, Goodarzi and Canbaz (2025), Heuristics and biases in AI decision-making. https://arxiv.org/abs/2410.02820 (b22, c20; abstract and intro only, per-bias numbers not verified)
- [V] Araya (2025), Chains-of-thought in Bayesian reasoning. https://arxiv.org/abs/2503.15268 (a37, b23, c21, d14)
- [V] Wang, Xiao, Chen and Oswald (2024), REHEAT. https://arxiv.org/abs/2404.01461 (c09, c10, c25)
- [V] Huang et al. (2025/2026), SynAnchors. https://arxiv.org/abs/2505.15392 (c12, c27, d09; d09 via fetch summary)
- [V] Takenami, Huang, Murawaki and Chu (2025), Anchoring in LLM price negotiation. https://arxiv.org/abs/2508.21137 (c13, d10)
- [V] Malberg, Poletukhin, Schuster and Groh (2025), A comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413 (c14; not re-opened by the checker)
- [V] Lyu et al. (2025), Self-Adaptive Cognitive Debiasing. https://arxiv.org/abs/2504.04141 (c17, d13)
- [V] Scholten et al. (2024), Metacognitive myopia in LLMs. https://arxiv.org/abs/2408.05568 (c22; conceptual)
- [V] Epstein et al. (2025), FermiEval. https://arxiv.org/abs/2510.26995 (d03)
- [V] Hobor, Brcic, Kovac and Poje (2026), Bayesian elicitation with LLMs. https://arxiv.org/abs/2604.01896 (d04)
- [V] Bahaj et al. (2025), Gauging overprecision in LLMs. https://arxiv.org/abs/2504.12098 (d05)
- [V] Borjigin et al. (2026), AnchorBench. https://arxiv.org/abs/2608.14320 (d06, d07)
- [V] Anchoring bias in LLM-as-a-judge systems (2026). https://arxiv.org/abs/2608.25869 (d08; fetch summary)
- [V] Yax, Anllo and Palminteri (2023/2024), Studying and improving reasoning in humans and machines. https://arxiv.org/abs/2309.12485 (d11)
- [V] PsyAgentBench (2026). https://arxiv.org/abs/2609.22090 (d12; fetch summary)
- [V] Harshavardhan (2026), Self-anchoring calibration drift. https://arxiv.org/abs/2603.01239 (d15; abstract and design)
- [V] Weerasekara, Kamarthi and Isaacs (2026), Conditional cognitive biases in LLMs. https://arxiv.org/abs/2608.05166 (d16; fetch summary)
- [V] Liu, Chen and Zhong (2025), Large Language Newsvendor. https://arxiv.org/abs/2512.12552 (d17)
- [V] Owusu and Feldman (2026), Anchoring depends on confidence and post-training. https://aclanthology.org/2026.acl-short.16/ (d18; abstract only, so effectively [M] for numbers)
- [V] Wu, Guo and Yiu (2026), Bias by necessity. https://arxiv.org/abs/2605.08716 (d19; low weight, not used for claim status)
- [V] Chergui et al. (2026), Mitigating anchoring bias in LLM agents for 6G networks. https://arxiv.org/abs/2606.18272 (d20; low weight)
- [V] Probabilistic reasoning in generative LLMs. https://arxiv.org/abs/2402.09614 (d21; fetch summary)
- [M] Wang et al. (2026), Making bias non-predictive (EIT). https://arxiv.org/abs/2602.01528 (a36; training method, outside scope)
- [M] Itzhak et al. as relayed by Sumita et al. (c26, same source as a32)

Note on duplicates. The 113 evidence lines cite about 55 distinct papers. Many findings appear in two or three lines of the same paper, so counts of lines overstate independent evidence (critique section 2, item 5).
