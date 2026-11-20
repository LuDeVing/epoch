# Heuristics and biases: deep document

*Subfield E04.09. Written 2026-11-20 from evidence_a-d.jsonl (a01-a28, b01-b26, c01-c29, d01-d20), claims.jsonl (K01-K28) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Evidence ids in brackets point to the jsonl files. Where a number was corrected in the critique, the corrected number is used.*

## 1. What it is

Heuristics and biases (H&B) is the research program started by Daniel Kahneman and Amos Tversky in the early 1970s. Its claim: people judge probability, frequency and value with a small set of mental shortcuts. The shortcuts are usually useful. They also produce errors that are systematic, meaning the errors lean in a predictable direction. They are not random noise. [a01]

Three shortcuts came first (Tversky and Kahneman 1974):

- **Representativeness.** Judge how likely A belongs to class B by how much A resembles B. Ignores base rates, sample size and regression to the mean.
- **Availability.** Judge frequency by how easily examples come to mind. Distorted by ease of recall or ease of imagining.
- **Anchoring and adjustment.** Start from a number, adjust, stop too soon. The final answer stays near the start.

Later work added prospect theory and framing (1979, 1981), the conjunction fallacy (1983), and attribute substitution (Kahneman and Frederick 2002): when a target question is hard, answer an easier related one unless a slower check catches it. [a14]

Why this subfield matters to our agent:

1. **Contrast.** The sister subfield, naturalistic decision making (NDM, Klein), says expert intuition is often good. H&B says intuition is often biased. Kahneman and Klein (2009) agreed on a boundary: intuition is trustworthy only in regular environments with long feedback. [b25, snippet only]
2. **Section 4b of SCHEMA.md** already lists "bias checklists and debiasing instructions" and "tell the model to slow down" as things not to add. This document checks that list against the newest evidence, and finds the picture is more mixed than "never".
3. **Language models are now a test bed.** At least 40 papers run classic H&B tasks on LLMs. Their results tell us which human biases a model inherits, which it does not, and which fixes work.

Main take-away up front: human H&B findings are half-robust (framing and explicit anchoring hold up; many others shrank or failed). LLM bias is real but task-specific, unstable across wording, and mostly a property of cues in the prompt rather than a general "bias level". Most debiasing prompts do little. A few specific operators work.

## 2. History and theories in depth

### 2.1 The founding papers

**Tversky and Kahneman 1974, "Judgment under uncertainty", Science.** [a01-a09, all opened] A review of experiments with student subjects. Key items:

- *Base-rate neglect.* Given a bland personality sketch ("Dick"), subjects judged P(engineer) = .5 whether the group was 70% or 30% engineers. With no sketch they used the prior correctly. Worthless evidence erased the base rate. [a02]
- *Sample size.* Hospital problem: larger hospital (about 45 births a day) or smaller (about 15). Which records more days with over 60% boys? Answers: larger 21, smaller 21, about the same 53. Correct: the smaller. [a03]
- *Chance and regression.* H-T-H-T-T-H judged likelier than H-H-H-T-T-T. Predictions of teaching success 5 years out were identical to percentile ratings of one practice lesson, i.e. no regression. [a04]
- *Availability by imaginability.* Committees of 2 versus 8 from 10 people. Median estimates 70 versus 20. Correct is 45 for both. [a05]
- *Anchoring.* A number was set in the subjects' presence, then they judged the percentage of African countries in the UN. Median 25 for anchor 10, median 45 for anchor 65. [a06]
- *Insufficient adjustment.* 8x7x...x1 versus 1x2x...x8 in 5 seconds. Median 2,250 versus 512. Correct 40,320. [a07]
- *Overconfidence.* 98% intervals missed the truth about 30% of the time (should be 2%). Events given .34 average probability happened 26% of the time. [a08]
- *Conjunctive events.* Most subjects preferred a 7-reds-in-a-row bet (p = .48) over a simple 50% bet. [a09]

**Tversky and Kahneman 1981, "The framing of decisions", Science.** [a10-a12, opened]

- Asian disease problem. Problem 1 (N = 152, lives saved): 72% sure 200 saved, 28% the 1/3 chance of saving 600. Problem 2 (N = 155, lives lost): 22% sure 400 die, 78% the 2/3 chance that 600 die. Same outcomes, preference reversal. [a10]
- Dominance violation. Two decisions shown separately: 84% took the sure $240 gain, 87% took the 75% chance to lose $1,000. 73% ended with the A+D pair, which is dominated by B+C (3% chose B+C). When the combined problem was shown (N = 86), 100% chose the dominant option. [a11]
- Mental accounting. Drive for $5 off a $15 calculator: 68% yes. Off a $125 calculator: 29% (N = 93, 88). [a12]

**Tversky and Kahneman 1983, Linda.** Most people rank "bank teller and feminist" above "bank teller". The 85% figure is quoted second-hand in Suri et al. [a13, snippet only]

### 2.2 Theory development

- **Prospect theory** (1979, 1992). Value is defined on gains and losses from a reference point, loss-averse, with probability weighting. The loss aversion coefficient across 600+ estimates is lambda = 1.955. [b07]
- **Attribute substitution** (Kahneman and Frederick 2002). One mechanism for all three heuristics. A fast System 1 answers an easier question; System 2 may or may not monitor. [a14, snippet only]
- **Dual-process framing** is covered in another subfield (Dual-process accounts of judgment, run in parallel). Link only. One note from this folder: a 2026 study of 249 people on 250 inference tasks finds that high and low CRT scorers fit the same parallel-constraint-satisfaction model, with high scorers using it more consistently. No two-system split is needed. [b12, K22]

### 2.3 The rival program: ecological rationality

Gigerenzer (1996) and Gigerenzer and Gaissmaier (2011) argue that the heuristics are vague labels, the norms used to call answers wrong are narrow, and errors shrink when problems are given in natural frequencies. Kahneman and Tversky (1996) replied that errors remain across many tasks. [a15, b24, snippets only] A meta-analysis of 35 articles (226 estimates) finds the natural-frequency benefit is real but conditional: short-menu formats and visual aids help both formats, and method choices change results. [d17, abstract only]

### 2.4 The joint position

Kahneman and Klein (2009): trust intuition only when the environment is regular enough to learn and the person had long, quick feedback. [b25, snippet only] This is the bridge to NDM. For an LLM it raises an open question (section 10): is there an analogue of a "regular, well-fed-back" domain where the first answer can be trusted?

## 3. Core findings with exact numbers

Status key: Robust = replicated at scale; Shrunk = replicates smaller; Failed = did not replicate; Unreplicated = no large replication found; Human = original human study only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Base-rate neglect with worthless evidence | P(engineer) = .5 in both 70% and 30% groups | T&K 1974 [a02] | Human; no large replication found |
| Insensitivity to sample size (hospital) | 21 larger / 53 same / 21 smaller; correct = smaller | T&K 1974 [a03] | Human; training does not transfer (see 5.3) |
| Imaginability availability (committees) | medians 70 vs 20; truth 45 | T&K 1974 [a05] | Human; no large replication found |
| Anchoring, explicit number | UN items: median 25 vs 45; Many Labs 1 reported it replicates | T&K 1974 [a06]; Klein 2014 [a16 snippet] | Robust (second-hand numbers) |
| Anchoring, incidental (phone P97 vs P17) | original N = 207, d = 0.30; replication N = 6,826, d = 0.04 (CI -0.01 to 0.09) | Many Labs 2 [b03] | Failed |
| Insufficient adjustment (factorial) | 512 vs 2,250; truth 40,320 | T&K 1974 [a07] | Human; no large replication found |
| Overconfidence in intervals | 98% intervals miss about 30% of the time | T&K 1974 [a08] | Human; widely replicated elsewhere (not in our evidence) |
| Asian disease framing | N = 152: 72/28; N = 155: 22/78 | T&K 1981 [a10] | Robust |
| Risky-choice framing, pooled | Kuhberger 1998: d = 0.31 (100+ studies, about 30,000 people); bias-corrected d = 0.52 (range 0.16 to 0.91 by task); Many Labs 1 d = 0.60; Im and Chen 2022 h = 0.612, 100,000+ people, 49 countries | Kuhberger 2023 [b06] | Robust; about a quarter of people show no effect |
| Attribute and message framing | about d = 0.10 for message framing; food meta d = 0.47 overall, attitudes 0.82, intentions 0.05 | Kuhberger 2023 [b07] | Small or inconsistent |
| Calculator / mental accounting | original N = 181: 68% vs 29% (OR 4.96); replication N = 7,228: 49% vs 32%, d = 0.40 (CI .35-.45), OR 2.06 | Many Labs 2 [b02] | Shrunk |
| Affect-driven choice (certain vs unlikely) | N = 7,218: 47% vs 51%, d = -0.08 | Many Labs 2 [b04] | Reversed |
| Many Labs 2 overall | 28 findings, 125 samples, 15,305 people, 36 countries; 15/28 (54%) significant at p<.05, 14/28 at p<.0001; median d 0.60 original to 0.15; 9/28 reversed; heterogeneity in 11/28 | Klein 2018 [b01] | Meta-evidence |
| Linda conjunction | 85% pick conjunction (second-hand) | T&K 1983 [a13] | Human; no large replication in our evidence |
| Conjunction fallacy and pay | pooled d = 0.19, OR 1.40, n = 3,276 | Incentivization meta-analysis [d18] | Small effect of incentives |
| Natural frequencies help Bayes | 35 articles, 226 estimates; effect conditional on format | McDowell and Jacobs 2017 [d17] | Real, conditional |
| Bias composites are unreliable | 15-task composite alpha = 0.484; 13-task split-half about 0.38 (N = 1,279); no general bias factor | Berthet 2021 [b08]; Aczel 2015 [b09] | Robust |
| CRT in humans | 38% correct (original 41%, n = 3,428); 55% intuitive | Hagendorff 2023 [a18, b13] | Robust |
| Debiasing training | analogical training (N = 154): gain only on statistical-principle biases at 4 weeks; awareness training no gain | Aczel 2015 [b10] | Narrow transfer |
| Small-numbers training | N = 100 scientists; 20% scored zero; training did not transfer to a quiz | RSOS 2022 [b11] | Failed transfer |

Reading the table: the effects that survive are the ones with large, stable effect sizes and clean task logic (explicit anchors, risky-choice framing). Textbook items with vivid vignettes shrank or reversed when tested on thousands of people. We should size LLM tests with the shrunken effect, not the original.

## 4. Mechanisms and models

Each mechanism below is stated so that it can be coded as a probe or an operator.

### 4.1 Anchoring and adjustment

Model: answer = anchor + adjustment, where adjustment stops when the value feels plausible. Effect size scales with anchor plausibility and with the uncertainty of the quantity.

Implementation of a probe: for each item with a numeric answer, make two prompts that differ only in an anchor number (low, high). Bias score = mean(high) - mean(low), normalised by the control spread. Include a control with no anchor to check accuracy. [c07, d03, d05]

LLM-specific findings:
- The effect acts in shallow layers (Huang et al. 2026). [c24]
- It enters through any channel, not only the user prompt: external text, retrieved documents, tool outputs. Irrelevant anchors barely move four recent API models (influence 0.00-0.02 on an index scale) while plausible anchors move them 0.07-0.16. [d03]
- Plausible anchors are the dangerous ones, because they look like evidence. A tool result that contains a number is an anchor.

### 4.2 Framing (prospect theory)

Model: choice depends on gain/loss coding relative to a reference point. Probe: the same decision in gain and loss wording; measure flip rate. For code-level framing, hold the artifact fixed and change only the goal text. [a10, c27]

Caveat from Kuhberger 2023: prospect theory predicts both halves of the pattern (risk-averse for gains, risk-seeking for losses), but studies often show only one half. Example in the review: 10 of 30 took the sure gain (not above 50%, p = .068), but only 3 of 30 took the sure loss. [b23] Rival accounts exist.

### 4.3 Representativeness and base-rate neglect

Model: probability judged by similarity to a prototype; base rate dropped. Bayes rule needs prior x likelihood. Probe: give prior, likelihood and a vivid description; compare answer with the computed posterior. Use novel numbers and changed colours or names, because the known items are memorised. [c03] In a 45-model test, representativeness was the weakest area even for the best models: o4-mini resistance 0.527, gpt-4.1 about 0.547. [d01]

### 4.4 Availability and ease of retrieval

In an LLM the analogue is the "most salient or most recent context item wins". Jones and Steinhardt (2022) used it to predict code-model failures: flipping the operation order dropped Codex accuracy from 50% to 17%. [a25] Order and primacy effects in prompts are the same family. [b17, c22]

### 4.5 Cue susceptibility in agents

The agent-level version of all of the above: a cue unrelated to the task logic (author name, earlier analysis, stated goal, result order, a user hypothesis) changes the outcome. In code review with fixed code, mean relative recall gap: framing 33.2%, anchoring 23.5%, halo 18.4%. [c27] In search agents, a dead-end history cut the switch-after-failure rate for one model from 100% (no history) to 87% (neutral) to 23.5% (dead-end history). [d15] This is the mechanism to guard against, not "System 1".

### 4.6 What a bias score is

Most LLM papers use bias score = rate of target answer under treatment minus under control. This measures sensitivity to a cue. It does not measure accuracy. Low bias can come from refusing, answering at random, or one fixed position preference (Llama 1B in Malberg looked least biased but failed to decide in 33% of tests). [c21] Always report both gap and accuracy.

### 4.7 Debiasing operators that have been tested

| Operator | How to implement | Evidence |
|---|---|---|
| Counter-anchor | Supply both a high and a low anchor, or generate an opposing anchor | GPT-4 answers near bias-free value [c20] |
| Ignore-instruction | "Ignore extraneous numbers" in system text | Helped Disc 0.26 to 0.16 (Qwen-7B), 0.30 to 0.10 (Llama-8B) [d04] |
| Two-phase "set the standard first" (Anti-DP) | Step 1: write what a correct answer needs. Step 2: answer | Llama-3.1-8B total anchoring 34.7% to 24.7% [d06] |
| Axiom elicitation | Elicit best-practice axioms for the task, inject, then answer | Median sensitivity 12.9% to 6.3% (p<.001), about 51% reduction [d08] |
| Self-rewrite (SACD) | Loop: detect bias, analyse it, rewrite the prompt, answer the rewrite | Lowest scores in finance, health, law; e.g. FOMC Llama-8B avg 0.1570 vs vanilla 0.3805 [d11] |
| Abstain plus bias inspection | Tell the model to inspect for traps; allow "none" | GPT-4 33.2 to 79.0 (no abstain), 93.5 with abstain [c19] |
| Natural-frequency restatement | Restate probabilities as counts of 1,000 | Human evidence only [d17] |
| Dead-end history | Show the failed attempts before the next try | Qwen switching 87% to 23.5% [d15] (this changes the behaviour; effect on accuracy is not shown) |

Do not implement: debate, Reflexion-style reflection as debiaser, generic "be rational" warnings (see 5.4).

## 5. What holds up

### 5.1 Human replications

- **Many Labs 2.** Half of 28 classic findings replicated at p<.05, median effect fell from d = 0.60 to d = 0.15, and 9 reversed. Variation came more from the effect than from the sample or country. [b01]
- **Framing.** The best-supported H&B result. Pooled d about 0.5-0.6 for risky choice. About a quarter of people show none. Outside risky choice it falls to about 0.10 for message framing. [b06, b07]
- **Anchoring.** Explicit anchors hold (Many Labs 1, second-hand). Incidental anchors failed at scale (d = 0.04 vs 0.30). [b03]
- **Mental accounting (calculator).** Replicated but shrank: 68% vs 29% became 49% vs 32%. [b02]
- **Gaps.** No large preregistered replication was found for Linda rates, base-rate neglect rates, availability or insufficient adjustment. We do not know if these hold. [d17, d18 are abstract only]

### 5.2 Measurement problems

Composite bias scores have alpha 0.484 for 15 tasks. Versions of one task are not interchangeable. There is no general bias factor; at least two latent factors; bias scores correlate only moderately with ability. [b08, b09] Consequence for agent work: never track "the agent's bias level". Track named, item-specific gaps.

### 5.3 Debiasing in humans

- Analogical-encoding training (N = 154) helped 4 weeks later only on statistical-principle biases (sample size, base rate, regression, covariation). Awareness training and no training did not. [b10]
- Interactive small-sample training (N = 100) helped on the training task and did not transfer to a quiz. [b11]
- Incentives reduce the conjunction fallacy slightly (d = 0.19). [d18]
- A paper titled "Debiasing decisions ... a single training intervention" (Morewedge 2015) claims feedback-based training works. Not opened. [b26]

Summary: transfer to new task types is weak, awareness alone fails, feedback and worked analogies work narrowly. [K06, established]

### 5.4 Prompt-level debiasing in LLMs (mixed)

Worked, with caveats:
- Counter-anchor (both anchors) on GPT-4 [c20]. Single paper.
- Ignore-instruction on small models [d04].
- Axiom elicitation, 51% mean reduction, up to 73% on some biases, median sensitivity 12.9% to 6.3% [d08].
- SACD self-rewrite beats awareness and few-shot, but is not matched on tokens and does not measure accuracy [d11, K16 contested].
- Self-help rewrite left 0% (Llama-2 13B) and 1.4% (Llama-2 7B) biased framing prompts; GPT-4 2.7% [a24].
- Abstain plus bias inspection [c19].

Did not work or backfired:
- Generic bias warning: 10.3% vs 12.9% control, not significant per bias after FDR [d08].
- Self-check for bias raised anchoring (Disc 0.26 to 0.45, Qwen-7B External) [d04].
- Knowledge enhancement worsened anchoring 34.7% to 50.5%; self-improving 38.4% (and Qwen2.5-7B 40.0% to 48.0%) [d06].
- Chain of thought, thoughts-of-principles, ignore-anchor and reflection did not reliably fix anchoring in GPT-4/4o [c20]. CoT helped one model (Qwen 0.26 to 0.14) and not another (Llama 0.30 to 0.31) [d04].
- Few-shot debiasing could break instruction following: admit/reject ratios under 1% [c16].
- Generic prompt debiasing on judgment biases (base rate, anchoring, sunk cost, status quo): accuracy -4.4% (backfires). It works for response-position bias (+40.5%), social bias +5.9%, not for information-order bias [d12].
- Rationality appeals ("be objective") raised resistance +6.5 to +14.9 points for some biases but made overattribution worse by up to 8.8 points [d02].
- Social-perspective prompting did little and worsened bandwagon; naming the bias (AwaRe) reduced bandwagon [b18]. Awareness helped primacy but not others [b17].
- Debate and Reflexion amplified bias (section 6.5).

Pattern: debiasing is bias-specific. A fix that works for one family often does nothing or backfires for another. [K24 established]

### 5.5 Moderators

- **Model strength.** Reasoning models lower but do not remove anchoring (22-25% of novel items still anchored). [d05, c24]
- **How the cue arrives.** Plausible and external anchors beat irrelevant ones. [d03]
- **Number of reasoning steps.** More steps raised sensitivity to confirmation (+33.66 pp), framing (+23.10), bandwagon (+8.84), availability (+9.81), anchoring (+3.77); hindsight fell (-17.25). [d07] This is directly against the assumption that more thinking always helps.
- **Chat format.** Adding any user turn shifts measured bias; zero-shot benchmark numbers do not carry to chat. A neutral user turn added +0.086 for Llama-3.1-8B. Biased user content raised bias in 6 of 8 models. [d14]

## 6. Language models

### 6.1 Timeline of model behaviour

| Period | Models | Pattern |
|---|---|---|
| 2022 | GPT-3 davinci | Human-like errors on CRT and some vignettes. All three CRT items answered with the intuitive wrong answer. [c01, a17] |
| 2022-23 | text-davinci-003, ChatGPT-3.5, GPT-4 | CRT correct: 5%, 59%, 96% (humans 38%). Intuitive: 80%, 15%, 0% (humans 55%). The newer models became "hyperrational". [c04] |
| 2023-24 | Llama-2, Claude 2, Bard, GPT-4 on 12 tasks | Many wrong answers are not the human bias but plain illogic. [c13] |
| 2024-25 | 20 to 45 models, 30 biases | Biases show up in at least some models. Capability does not predict low bias. [c21, d01] |
| 2025-26 | GPT-5.4-mini, Claude Haiku 4.5, Gemini 2.5, o4-mini | Irrelevant anchors resisted; plausible anchors and representativeness still bite. [d01, d03] |

### 6.2 Classic tasks on LLMs

- **Binz and Schulz 2022 (GPT-3).** 12 of 12 standard vignettes answered correctly or human-like. Framing, certainty effect and probability overweighting appeared; 3 of 6 prospect-theory effects found. It avoided the cab-problem base-rate error but failed perturbed versions: cab colour changed to black gave 20%; the CRT premise changed still gave 10 cents. This looks like recall of known items, not rule use. [a17, c01-c03] [K08 single-source]
- **Hagendorff et al. 2023 (CRT).** 150 CRT-style tasks. Numbers above. Chain of thought on davinci-003: correct 5% to 28%, intuitive 80% to 29%. Blocking reasoning in ChatGPT-3.5 left correct answers unchanged (CoT share 97% to 0%, change 4%, p = .49); GPT-4 correct 95% to 88%, intuitive 0% to 10%. Worked examples of the same type: type 1 from 2% to 92% after two examples, another type 12% to 92% after seven. [a18-a20, c04-c06] Transfer to other task types was not tested. [K09, K10 single-source]
- **Suri et al. 2023 (GPT-3.5 vs 60 mTurk humans, 30 per cell).** Anchoring: low anchor mean 20.83 (humans 22.50), high anchor 105.97 (humans 80.50), t(58) = 8.78, p<.0001. GPT-4 in 5 trials: 22.0 vs 94.33. Conjunction: ChatGPT chose the conjunction 18 of 20 times, humans 10 of 20. Framing: efficacy 5.2 (positive) vs 4.6 (negative). Endowment: kept the old coin 37 of 40 (92.5%) vs humans 34 of 40 (85%). Cells are small. [a21, a22, c07, c08]
- **Shaki et al. 2023 (davinci-003, token probability).** Priming, distance, SNARC, size congruity found; anchoring absent. [a27, c26] This conflicts with Suri. Likely difference: method, model, sample size. [K14 contested]
- **Macmillan-Scott and Musolesi 2024 (7 LLMs, 12 tasks).** Correct with sound reasoning: GPT-4 0.692, Claude 2 0.550, Bard 0.358, GPT-3.5 0.292, Llama-2 70b 0.150, 13b 0.050, 7b 0.025. Incorrect and not human-like: Llama-2 13b 0.700, 7b 0.608, GPT-3.5 0.408, GPT-4 0.142. Incorrect and human-like: GPT-3.5 0.217, Llama-2 7b 0.167, GPT-4 0.042. **Critique correction:** the earlier extraction (a26) of "GPT-4 human-like 73.3%" and "GPT-3.5 50.8%" is wrong or unexplained; use the c13 values above. The same prompt gives different answers across runs (e.g. Llama-2 7b on Monty Hall said switching does not matter). [c13, c14] [K13 single-source]
- **Instruction tuning.** Itzhak et al. (bias score = treatment minus control choice rate): certainty effect davinci-002 0.24, davinci-003 0.67; belief bias (invalid) 0.55 and 0.65; GPT-4 decoy-expensive 0.38 vs DaVinci 0.00 in 1-shot. Instruction-tuned models showed more decoy, certainty and belief bias than base models. Critique note: the Mistral and T5 columns were garbled in extraction; the Mistral figure (0.05 vs 0.26) and GPT-4 certainty (0.15) are unconfirmed. [a23, c09, c10] Caveat from CogBias: much measured bias is first-option preference (first option chosen 77-79% vs 36.8% chance) and dialogue format alone shifts bias. [d12, d14] [K11 contested]

### 6.3 Large batteries

- **Malberg et al. 2024.** 20 LLMs, 30 biases, 30,000 test cases (200 scenarios x 5 variants x 30 biases). All 30 biases appeared in at least some models. Status quo and disposition effect ran opposite on average. Gemini 1.5 Pro least biased; larger OpenAI models somewhat more biased; a random baseline showed no bias. [b15, c21] [K12 established]
- **Knipper et al. 2025.** 45 models, 8 biases, 2,887,500 responses. Mean bias resistance (1 = never biased): claude-3-7-sonnet 0.822, o4-mini 0.821, QwQ-32B 0.800, gpt-4.1 0.778, Llama-3.3-70B 0.740, phi-4 0.736, Qwen2.5-0.5B 0.427. Susceptibility 17.8% to 57.3%. o4-mini by bias: anchoring 0.786, framing 0.810, representativeness 0.527. Size reduces bias by up to 39.5%; prompt specificity up to 14.9%. [d01, d02]
- **Huang et al. 2026 SynAnchors.** Novel synthetic anchoring items (to avoid memorised classics). Share of questions anchored: Qwen2.5-0.5B 60.5%, Llama-3.2-1B 57.1%, Mistral-7B 51.1%, Qwen2.5-7B 40.0%, GPT-4o-mini 37.0%, GPT-4o 27.3%, DeepSeek-R1 25.0%, Qwen3-235B thinking 22.0%. Numeric relative error: DeepSeek-R1 0.114 vs GPT-4o 0.270. [d05, c24]
- **AnchorBench 2026 (14 models, greedy).** Control accuracy 96-100% for API models. External suite influence, irrelevant vs plausible anchor: GPT-5.4-mini 0.00 vs 0.14, Haiku 4.5 0.00 vs 0.12, Gemini 2.5 Flash 0.02 vs 0.07, Grok-3-mini -0.00 vs 0.16. [d03]
- **Takenami 2025 (negotiation agents).** Seller agents with an anchor got better prices from buyer LLMs, like humans. o1 mitigated the effect in 35 of 50 matched cases vs GPT-4o. [c23]
- **Instability warnings.** BiAxisBias (stereotype tasks, not H&B items): instability with 3 wordings 10.5% vs 6.3% for 3 identical calls; 9 of 28 model pairs reverse across 4 task paradigms; selection and rationale disagree in 34.2% of 7,959 dual-valid cases. [d19] Talboy and Fuller: five classic prompts on ChatGPT-3.5, GPT-4 and Bard in March and August 2023, identical wording. Some answers flipped between sessions (ChatGPT-3.5 used Bayes in March, wrong non-Bayes in August; Bard the reverse). [d20] [K28 established]

### 6.4 LLMs as judges

Koo et al. (CoBBLeR): 16 LLM judges, 630K samples. Order bias in 11 of 15 models; bandwagon over 70% follow a fake "85% preferred" statistic; salience (length) proportion 0.56 GPT-4, 0.63 ChatGPT, 0.62 Llama-2; largest models prefer their own answers above 50% with names hidden; about 40% of comparisons showed some bias. [a28, c22] [K19 established] This matches SCHEMA G5.

### 6.5 Agent and code settings

- **Code generation (Jones and Steinhardt 2022).** Framing line copied by Codex 62.2-92.7% (81% in one test, baseline 4.5%); CodeGen 70.7% vs 0.0%. Irrelevant function plus framing line dropped Codex accuracy from 32.9% to 2.4-10.6%; CodeGen 25.6% to 1.5-11.0%. Name-description conflict: 100% to 4.4-4.6%. Anchor functions with a bug leaked into solutions. [a25, c11, c12]
- **Code review (Shahriar 2026, 8 LLMs).** Recall gaps framing 33.2%, anchoring 23.5%, halo 18.4%. 43 of 48 gaps significant in C/C++, 44 of 48 Java, 46 of 48 Python. Anchoring raised recall 11.16 points on reasoning-dependent bugs vs 4.24 on pattern ones. Combined cues: Mistral near 75% attack success (best single under 51%), Gemini 45% (25%). Prompt-only defences weak (four models above 80% under the weak defence; all open models above 39% under the strong); counterproductive on Claude. [c27, c28] [K20 established]
- **Software-engineering dilemmas (Sovrano 2025, 2026).** 8 biases, 6 models. Anchoring and availability sensitivity 5-12%; hindsight and hyperbolic discounting up to 70%. Steps-effect as in 5.5. [d07]
- **Search agents (Xiao and Yu 2026, 10 models, 1,000 worlds).** Dead-end history: Qwen switch rate 100% to 87% to 23.5%. Wrong hypothesis from the user: accuracy loss up to 43.5 pp for one model, 3.6 to 17.4 pp for most. A seek-disconfirming instruction gave +23.0 pp accuracy on one model, with +22.5 pp of another quantity (the record is truncated at this point); effects differ by model. [d15] [K25 established]
- **Debate and Reflexion.** In SACD tables (FOMC, Llama-3.1-8B): vanilla 0.3805, CoT 0.3425, Reflexion 0.3830, debate 0.5020, self-help 0.2100, SACD 0.1570. Debate on gpt-3.5 FOMC 0.5155; Reflexion on PubMedQA with Llama-70B 0.5585. [d11, c18] Oh et al.: debate amplifies the majority initial view, right or wrong; every action with initial consistency above 0.5 became more likely. [d09] Ma et al.: judge debate cut DeepSeek-V3 position consistency from 0.82 to 0.71 after round 1; no further significant rise. [d10] [K17 established; Reflexion-specific evidence is one paper.] This agrees with SCHEMA G9.

### 6.6 Confidence

Four 2025 models, 24,000 trials. Accuracy / mean stated confidence / ECE: Gemini 2.5 Pro 80.9% / 99.5 / 0.185; Haiku 4.5 75.4% / 86.0 / 0.122; Gemini 2.5 Flash 70.9% / 97.9 / 0.272; Kimi K2 23.3% / 95.7 / 0.726. Confidence-correctness correlation up to r = 0.175 (Gemini 2.5 Pro r = 0.011). One preprint. [d16] [K26 single-source] This matches the existing 4b row on verbal confidence.

### 6.7 Mechanism-level evidence

Bias directions are linearly readable: probes reach 99.8% (judgment), 98.2% (information processing), 99.2% (response). Steering lowers bias with little capability loss in Llama, up to -19.0 pp for judgment biases in Qwen. Not available to a prompt-only scaffold. [d13]

### 6.8 Limits of the LLM evidence

- Most studies use 2022-2023 models. Frontier 2026 models are almost untested with contamination control.
- CRT and Linda are public; competence and memorisation cannot be separated. [c03]
- Many "many studies" count the same few papers (critique weak spot).
- Several 2026 sources are preprints (d03, d12, d14, d15, d16).
- Bias scores measure sensitivity, not accuracy.

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Treat cues outside the task as anchors and move them out of the attempt prompt.** Numbers, stated guesses, author names and earlier analyses go to a marked block (existing S1 input hygiene). Applies to tool outputs and retrieved text too. Schema: S1 and G. Status [E] for the harm, with evidence K14, K23, K25, K20: c27, d03, d05, d07, d15, a25, c07. The remedy itself stays [S] (see Test first). Note SCHEMA S1 already has this; the new evidence extends it from the user prompt to tool and retrieval output (d03).
2. **Randomise candidate order and strip popularity statistics in any judging step.** Schema: G5 (extend). [E] K19: a28, c22, b18.
3. **Do not use debate or Reflexion-style reflection as a debiaser.** Schema: G9 (confirmed, add a bias-amplification reason). [E] K17: c18, d09, d10, d11.
4. **Do not rely on generic "be careful / be rational / be aware of bias" prompts.** Schema: 4b (confirmed; the new row text could read "generic debiasing prompts backfire on judgment biases, -4.4%"). [E] K24: d02, d04, d06, d08, d12; also K06 for humans: b10, b11.
5. **Measure per bias, with several items, paraphrases and repeats; pin the model version.** Schema: log and bench design (section 6). [E] K05, K28: b08, b09, d19, d20.
6. **Treat stated confidence as a weak signal, not a stop rule.** Schema: G (matches 4b). [E] K26 plus existing F09 and F07: d16.
7. **Size any human-derived test using the shrunken effect and prefer effects that replicate at scale (explicit anchors, risky-choice framing).** Schema: bench design. [E] K01-K04: b01, b02, b03, b06.
8. **Extra reasoning steps are not safe by default on cue-laden tasks.** Confirmation +33.66 pp and framing +23.10 pp with more inference steps. Schema: G11 (supports; add "cue-laden" to the list of conditions where more thinking hurts). [E for the direction in this paper, but one paper family: Sovrano, d07; label [S] when citing alone. Counted here because G11 already has eight independent sources.]
9. **A model's wrong answers are often plain illogic and vary by run, so single-sample bias tests are not enough.** Schema: bench. [S] K13: c13, c14. Keep out of schema; use as test design only.

### Test first (not yet established)

- **Counter-anchor operator at S6 or S3 (O):** supply an opposing anchor or ask for the answer under both a high and a low anchor, code takes the midpoint or checks agreement. Evidence c20 (GPT-4, one paper). [S]
- **Ignore-instruction plus two-phase "state the standard first" (Anti-DP) at S1:** d04, d06. Gains 6 to 10 points; backfires in some models. [C]
- **Axiom elicitation step (O):** elicit best practice rules for the task class, inject before answering. 51% mean bias reduction (d08). Single 2026 paper, bias sensitivity only, no accuracy. [S]
- **Self-rewrite (SACD) as O8 variant "reframe the prompt":** d11, a24. Strongest bias-gap result but not token-matched and with no accuracy measure. [C]
- **Abstain plus bias-trap inspection:** c19 (GPT-4 33.2 to 79.0 on a trap benchmark). Conflicts with G6 (never abstain on the first pass), so test only as "flag" not "refuse". [S]
- **Dead-end history in memory (S5/S6):** show failed attempts so the agent switches strategy less blindly. d15. One paper; effect on accuracy not shown. [S]
- **Seek-disconfirming instruction (O):** d15, one model +23.0 pp accuracy; effect varies by model. [S]
- **Counts-out-of-1000 restatement for base-rate problems (O6):** human evidence only (d17). No LLM test found. [S]
- **Gate on sample agreement rather than stated confidence to skip deliberation:** not tested. [S]
- **Novel-variant probes for CRT, cab and Linda items:** to separate recall from rule use (c03). [S]

## 8. Concrete tests on our bench

All tests use two or more arms at equal token budget (counting setup tokens, as G7 demands). Use at least 3 paraphrases and 5 repeats per item, with the model version pinned. Report accuracy and bias gap together.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Numeric estimation with a plausible anchor in prompt text, in a tool output, and in a retrieved doc (novel items, 40 per channel) | A plain model; B plain + CoT; C input hygiene (anchor moved to marked block); D ignore-instruction; E counter-anchor | Bias gap (high minus low anchor mean / control spread); control MAE | Gap falls by 30%+ for C and E vs A; irrelevant-anchor gap already near 0 on frontier models (d03) |
| T2 | Gain/loss framing pairs for decisions (30 pairs, new vignettes, plus 10 code-review pairs with goal text changed) | A plain; B restate-in-opposite-frame step; C SACD-style rewrite | Flip rate between frames; accuracy against ground-truth where defined | Classic risky-choice framing already low on strong models (d01 framing 0.81); expect code-review gap 33% (c27) to fall with B |
| T3 | Wrong-hint tasks: planning or code-review task with a plausible wrong hint or earlier analysis | A plain; B hint moved to marked block, answer then re-checked; C seek-disconfirming instruction; D dead-end history shown | Accuracy; switch rate; pp loss vs no-hint control | Wrong-hint loss of 3.6-17.4 pp (d15) falls under B or C; D lowers switching but accuracy effect unknown |
| T4 | Base-rate problems with novel numbers and changed colours (30 items) | A plain; B counts-out-of-1000 restatement; C CoT; D worked example of a different type | Accuracy vs computed posterior | Representativeness resistance about 0.53 on frontier models (d01) leaves room; B should help if the human effect transfers |
| T5 | CRT-style trap items with changed premises (30 items) | A direct; B CoT; C our schema loop; D few-shot of same type; E few-shot of a different type | Accuracy; intuitive-trap rate | Direct accuracy on strong models near 88% even without CoT (a20); expect little gain; D vs E tests transfer (K10) |
| T6 | Judge steps: 100 pairwise comparisons, order swapped, fake popularity statistic | A naive judge; B order randomised, stats stripped; C length-normalised | Flip rate on swap; agreement with ground truth | Order bias in 11 of 15 models (c22); B should remove most flips |
| T7 | Debate vs single-agent rewrite on biased prompts | A single rewrite; B debate of equal total tokens; C plain voting | Bias gap; accuracy | B worse than A and C (d11, d09, d10) |
| T8 | Stated confidence gate: run 200 mixed items, gate deliberation on (i) stated confidence, (ii) sample agreement of 5 short runs, (iii) none | Equal-token budgets across gates | Accuracy per token; cases where a confident first answer was wrong | (ii) beats (i); (i) near random (r up to 0.175 in d16) |
| T9 | Reliability check for every probe above | Same arm, 3 paraphrases x 5 repeats | Between-wording vs between-repeat variance | Wording variance larger than repeat variance (d19: 10.5% vs 6.3%); drop probes with high instability |
| T10 | Reasoning-length effect on cue-laden tasks | Short (cap) vs long reasoning at equal item sets | Bias gap and accuracy | Confirmation and framing gaps grow with steps (d07); expect short cap to do no worse |

## 9. What does not transfer, and why

- **Human System 1 / System 2 framing.** LLM errors are often plain illogic (c13) or recall of memorised items (c03), not a fast-versus-slow split. Hagendorff found that blocking chain of thought barely hurt the newest model (a20), so the written reasoning is not the mechanism.
- **Human training effects.** Humans need weeks and feedback; transfer fails even there (b10, b11). In-context worked examples gave 2% to 92% on one task type in an older model (c06) but we have no transfer evidence.
- **Vivid vignettes.** Linda, hospital, cab and CRT are public. Strong-model scores are partly memory. Only novel or perturbed items count. [c03, critique]
- **Individual-difference findings.** "Who is biased" research (Berthet, Aczel) has no direct analogue; an LLM has no stable trait. Composites are not meaningful. [b08]
- **Loss aversion, endowment and status quo as value-based effects.** Status quo and disposition ran opposite in LLMs. [c21] An LLM has no stakes. Treat these as response-pattern tests, not as value theory.
- **Incentive manipulations.** Pay has d = 0.19 for humans (d18). No stakes for a model. Tokens are the only cost analogue.
- **Natural frequency advantage.** Human working-memory story. May still help as a representation change (O6), but needs a test.
- **Activation steering.** Works in Llama (d13) and is outside a prompt-only scaffold.
- **Social-stereotype bias results (BiAxisBias).** Used here only for the instability point; those tasks are not H&B items. [d19]

## 10. Open questions

1. Do 2026 frontier and reasoning models show anchoring, framing and conjunction errors on novel, contamination-controlled items, and how large are the rates? Partly closed for anchoring and representativeness (d01, d03, d05); open for conjunction and framing.
2. At equal tokens, does a counter-anchor or rewrite step beat plain CoT and self-consistency on both bias gap and accuracy? No paper matches tokens.
3. Which biases cost accuracy on agent tasks scored against ground truth (planning, forecasting, code review), as opposed to merely flipping answers? Flips are measured (d07, d15, c27); outcome accuracy is mostly not.
4. Do debate and Reflexion amplify bias under all conditions? Debate: three papers. Reflexion: one (SACD).
5. Large preregistered human replications for availability, representativeness, base rates and conjunction. None found. This limits how much to trust the originals as test targets.
6. Is there an LLM analogue of the Kahneman-Klein condition (regular environment plus feedback), and can sample agreement or a regularity check identify when a first answer is safe? No test found. Stated confidence is not enough (d16).
7. Is the instruction-tuning amplification real or a position and chat-format artefact (d12, d14)? No reproduction on current open models.
8. Does in-context debiasing transfer to held-out task types? Only same-type results exist (c06). Prompt debiasing varies by bias family (d12), which predicts poor transfer.
9. What is the test-retest reliability of bias probes on LLMs? No formal coefficient on classic heuristic tasks (d19, d20 give partial signals).
10. Why does extra reasoning raise confirmation and framing sensitivity while lowering hindsight? (d07). Is it driven by the model reading the cue more times?
11. The truncated record d15 (seek-disconfirming instruction) needs re-checking before any number from it is quoted outside this document.

## 11. Sources

[V] = opened and read this session or an earlier run of this batch; [M] = snippet or abstract only, or not opened.

Primary human studies and reviews
- [V] Tversky and Kahneman (1974), Judgment under uncertainty. https://www.science.org/doi/10.1126/science.185.4157.1124 (a01-a09)
- [V] Tversky and Kahneman (1981), The framing of decisions. https://www.science.org/doi/10.1126/science.7455683 (a10-a12)
- [M] Tversky and Kahneman (1983), Extensional vs intuitive reasoning. https://psycnet.apa.org/doi/10.1037/0033-295X.90.4.293 (a13)
- [M] Kahneman and Frederick (2002), Representativeness revisited. https://doi.org/10.1017/CBO9780511808098.004 (a14)
- [M] Gigerenzer (1996) and Kahneman and Tversky (1996). https://doi.org/10.1037/0033-295X.103.3.592 (a15)
- [M] Klein et al. (2014), Many Labs 1. https://doi.org/10.1027/1864-9335/a000178 and https://econtent.hogrefe.com/doi/10.1027/1864-9335/a000178 (a16, b05; HTTP 403)
- [V] Klein et al. (2018), Many Labs 2. https://scholarlypublications.universiteitleiden.nl/handle/1887/74652 (b01-b04)
- [V] Kuhberger (2023), Systematic review of risky-choice framing. https://pmc.ncbi.nlm.nih.gov/articles/PMC10620856/ (b06, b07, b23)
- [V] Berthet (2021), Measurement of individual differences in cognitive biases. https://pmc.ncbi.nlm.nih.gov/articles/PMC7930832/ (b08)
- [V] Aczel et al. (2015), Measuring individual differences in decision biases. https://pmc.ncbi.nlm.nih.gov/articles/PMC4652008/ (b09)
- [V] Aczel et al. (2015), Real-life debiasing, analogical encoding. https://pmc.ncbi.nlm.nih.gov/articles/PMC4523707/ (b10)
- [V] Royal Society Open Science (2022), Law of small numbers training. https://pmc.ncbi.nlm.nih.gov/articles/PMC8889191/ (b11)
- [V] Cognitive reflection and rational choice (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13295265/ (b12)
- [M] Gigerenzer and Gaissmaier (2011), Heuristic decision making. https://www.annualreviews.org/doi/10.1146/annurev-psych-120709-145346 (b24)
- [M] Kahneman and Klein (2009), Conditions for intuitive expertise. https://psycnet.apa.org/doi/10.1037/a0016755 (b25)
- [M] Morewedge et al. (2015), Debiasing decisions. https://doi.org/10.1177/2372732215600886 (b26)
- [M] McDowell and Jacobs (2017), Natural frequencies meta-analysis. https://doi.org/10.1037/bul0000126 (d17)
- [M] Incentivization and the conjunction fallacy, meta-analysis (2023). https://doi.org/10.1007/s00426-023-01837-5 (d18)

LLM studies
- [V] Binz and Schulz (2023), Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (a17, b20, c01-c03)
- [V] Hagendorff, Fabi and Kosinski (2023), Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (a18-a20, b13, b14, c04-c06)
- [V] Suri, Slater, Ziaee and Nguyen (2023). https://arxiv.org/abs/2305.04400 (a21, a22, b21, c07, c08)
- [V] Itzhak, Stanovsky, Rosenfeld and Belinkov (2023/24), Instructed to bias. https://arxiv.org/abs/2308.00225 (a23, b19, c09, c10)
- [V] Echterhoff et al. (2024), BiasBuster. https://arxiv.org/abs/2403.00811 (a24, b16, b17, c15, c16)
- [V] Jones and Steinhardt (2022), Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299 (a25, c11, c12)
- [V] Macmillan-Scott and Musolesi (2024). https://arxiv.org/abs/2402.09193 (a26, c13, c14)
- [V] Shaki, Kraus and Wooldridge (2023). https://arxiv.org/abs/2308.14337 (a27, c26)
- [V] Koo et al. (2024), CoBBLEr. https://arxiv.org/abs/2309.17012 (a28, c22)
- [V] Malberg et al. (2024/25). https://arxiv.org/abs/2410.15413 (b15, c21)
- [V] Sumita, Takeuchi and Kashima (2024). https://arxiv.org/abs/2412.00323 (b18)
- [V] Zhong et al. (2024/25), Balancing rigor and utility. https://arxiv.org/abs/2406.10999 (b22, c19)
- [V] Lyu et al. (2025), SACD. https://arxiv.org/abs/2504.04141 (c17, c18, d11)
- [V] Lou and Sun (2024), Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (c20)
- [V] Takenami et al. (2025). https://arxiv.org/abs/2508.21137 (c23)
- [V] Huang et al. (2026), SynAnchors. https://arxiv.org/abs/2505.15392 (c24, d05, d06)
- [V] Valencia-Clavijo (2026), Anchors in the machine. https://arxiv.org/abs/2511.05766 (c25)
- [V] Shahriar et al. (2026), Words speak louder than code. https://arxiv.org/abs/2606.30587 (c27, c28)
- [M] Hagendorff et al. (2024), Machine psychology (abstract only). https://arxiv.org/abs/2303.13988 (c29)
- [V] Knipper et al. (2025), The bias is in the details. https://arxiv.org/abs/2509.22856 (d01, d02)
- [V] Borjigin et al. (2026), AnchorBench. https://arxiv.org/abs/2608.14320 (d03, d04)
- [V] Sovrano et al. (2025), Is general-purpose AI reasoning sensitive to data-induced cognitive biases. https://arxiv.org/abs/2508.11278 (d07)
- [V] Sovrano et al. (2026), Mitigating prompt-induced cognitive biases. https://arxiv.org/abs/2604.16756 (d08)
- [V] Oh et al. (2025/26), From belief entrenchment to robust reasoning in LLM agents. https://arxiv.org/abs/2503.16814 (d09)
- [V] Ma et al. (2025), Judging with many minds. https://arxiv.org/abs/2505.19477 (d10)
- [V] Huang et al. (2026), CogBias. https://arxiv.org/abs/2604.01366 (d12, d13)
- [V] Weerasekara et al. (2026), Conditional cognitive biases in LLMs. https://arxiv.org/abs/2608.05166 (d14)
- [V] Xiao and Yu (2026), Cognitive bias signatures in search-equipped agents. https://arxiv.org/abs/2611.05720 (d15)
- [V] Ghosh and Panday (2026), Dunning-Kruger effect in LLMs. https://arxiv.org/abs/2603.09985 (d16)
- [V] Gan et al. (2026), BiAxisBias. https://arxiv.org/abs/2605.09041 (d19)
- [V] Talboy and Fuller (2023). https://arxiv.org/abs/2304.01358 (d20)

Links to other subfields (not covered here): Debiasing; Dual-process accounts of judgment; Prospect theory and risky choice; Naturalistic decision making; Verbal confidence; Evidence and probability reasoning; Judicial bias and noise; Structured analytic techniques.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 15 established claims: 11 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E04.09-K06** (reworded: the sources support less). Two small single studies (Aczel 2015 N=154; Bishop et al. 2022 N=100 on sample-size neglect) are generalised to 'human debiasing training' as a whole; Aczel supports gains only for statistical-principle tasks and no benefit of awareness training, Bishop shows no transfer of one interactive training to a quiz. Corrected claim: In one analogical-encoding training study (Aczel et al. 2015, N=154) gains 4 weeks later appeared only on statistical-principle bias tasks, and an awareness-only training group showed no improvement; in a separate study (Bishop et al. 2022, N=100) interactive sample-size training improved the training task but did not transfer to a judgment quiz.
- **E04.09-K15** (reworded: the sources support less). Lou and Sun report Both-Anchor brings GPT-4 close to the bias-free value only when the high and low hints bracket that value (8 of 15 questions listed); for the other questions answers still deviate significantly. Corrected claim: Simple prompt fixes for anchoring (CoT, ignore-anchor, reflection) do not reliably remove it; supplying both a high and a low anchor brings GPT-4 answers close to the bias-free value only when the two anchors bracket that value, and other questions still deviate; reasoning models reduce but do not remove anchoring.
- **E04.09-K23** (reworded: the sources support less). Numbers support the pattern, but the models tested are mostly small or mid-tier API models (GPT-5.4-mini, Claude Haiku 4.5, Gemini 2.5 Flash, Grok-3-mini, o4-mini, GPT-4.1, Claude 3.7 Sonnet), not 'frontier'; framing resistance is 0.80-0.81 (about 19% biased), so 'largely resisted' is loose. Corrected claim: Recent API and reasoning models (2025-26, mostly mini/flash/Haiku-tier plus o4-mini, GPT-4.1 and Claude 3.7 Sonnet) still show anchoring and representativeness effects, and plausible anchors still move answers on novel or synthetic items, while irrelevant anchors barely move them (influence 0.00-0.02) and classic framing is mostly resisted (resistance about 0.80); no source tested current top-tier models with contamination control.
- **E04.09-K25** (reworded: the sources support less). Xiao and Yu show first-placed evidence order shifts final answers toward the first-placed document (more during active search), and dead-end history reduces strategy switching; they do not show that first evidence order lowers the chance of changing course. Sovrano 2025 and 2026 are one lab (counted once); 'cost' really means bias sensitivity, which rises with reasoning steps for five biases (largest for confirmation +33.66 pp and framing +23.10 pp) and falls for hindsight and hyperbolic discounting. Corrected claim: On agent-like tasks (software engineering dilemmas, search), bias cues change decisions with the task logic or document set fixed; bias sensitivity rises with the number of reasoning steps for anchoring, availability, bandwagon, confirmation (+33.66 pp) and framing (+23.10 pp) but falls for hindsight and hyperbolic discounting (Sovrano et al.); in search agents, first-placed evidence shifts final answers toward it and dead-end work histories reduce strategy switching relative to matched neutral histories (Xiao and Yu).
