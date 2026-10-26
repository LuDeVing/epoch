# Diagnosticity of evidence: deep document

*Subfield E02.02, part of E02 Intelligence analysis. Built from evidence_a-d.jsonl (a01-a28, b01-b27, c01-c29, d01-d19), claims.jsonl (K01-K31) and critique.md in this folder. Ids like a17 or K12 point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Many 2026 items are single preprints; read every number with that in mind.*

---

## 1. What it is

**Diagnosticity** is how much one item of evidence helps choose between rival hypotheses. It is not how well the item fits the favourite.

- Heuer's example: a high temperature proves the patient is sick, but says little about which illness (b01, a03).
- Evidence that every hypothesis predicts equally has no diagnostic value. Heuer says so in plain words (a01).
- The formal version is the likelihood ratio, P(E|H1) / P(E|H2). On a log scale, independent items add up (Good 1950; Fischhoff and Beyth-Marom 1983; both not opened, a28).
- To judge an item you need both likelihoods. Knowing only P(E|H1) tells you nothing. This is the 2x2 table lesson in Heuer's nurse example (a04).

There are two linked skills, and the research shows they come apart:

1. **Selection.** Picking which test or which piece of evidence to ask for next, so that rivals give different answers. In our schema this is S7 (discriminating test).
2. **Weighing.** Once evidence is in hand, giving each item the right weight and combining items without double counting.

Humans are weak at both. Language models are weak at both, but the failure shows up most clearly in selection (K11, K22).

**Why it matters for our agent.** S7 says: when two rules still fit, run the one input where they differ. This document asks whether that step can be made better, cheaper, and safer, and which published recipes survive scrutiny.

**Scope notes.**
- Belief revision, value of information, alternative-explanation controls and bias/debiasing are separate subfields run in parallel. Links only, no coverage here.
- Earlier deep documents in the series cover the general confirmation-bias and ACH material at the field level. This document adds exact numbers, the ACH test record, the pseudodiagnosticity dispute, and the 2024-2026 LLM studies.

---

## 2. History and theories in depth

### 2.1 Formal roots

- **Good (1950), Probability and the Weighing of Evidence.** Evidence adds in log-odds. The weight of evidence is the log likelihood ratio. [M] (a28)
- **Fischhoff and Beyth-Marom (1983).** Use the Bayesian yardstick to catalogue how people depart from it. [M] (a28)
- **Wason (1960).** The 2-4-6 task. People announce a rule after testing only triples their guess predicts. [M] (a26). Heuer's second-hand count: 6 of 29 right on first announcement; 0 of 51 in a repeat by another researcher (a03).
- **Klayman and Ha (1987).** Positive testing is not the same thing as confirmation bias. It is often a good strategy when the guess is true of a minority of cases. It fails when the true rule is broader than the guess. So "seek disconfirming evidence" is the wrong rule. The right rule is "seek the probe where rivals differ". [M] (a26)
- **Oaksford and Chater (1994) and Nelson (2005).** Good tests are chosen by expected information gain over hypotheses. Nelson compared several usefulness measures: Bayesian diagnosticity, probability gain, impact, information gain. [M] (a27, b16). Which score you pick matters: a likelihood-ratio score can rank highly a test that rarely changes the answer (b16 note).

### 2.2 Pseudodiagnosticity

- **Doherty, Mynatt, Tweney and Schiavo (1979).** Given P(datum | favoured hypothesis), people ask next for another datum about the same hypothesis, not the same datum under the rival. [M] (a13, b15). The original percentages were never obtained.
- **Task form** (Crupi and Girotto 2014, a11): two equiprobable hypotheses h and not-h; evidence e with P(e|h) = 65%; choose one more figure from P(e|not-h), P(f|h), P(f|not-h). The classical answer is P(e|not-h). Choosing P(f|h) was called irrational.
- **Kern and Doherty (1982).** 65 senior medical students; 83% chose information that Bayes would not require (same-hypothesis). Abstract only (d15).
- **Feeney, Evans and Venn (2000, 2008).** With a rare first feature, 43% chose the correct cell B and 44% chose the pseudodiagnostic cell C (second-hand, b14).
- **D'Addario and Macchi (2012).** Large conceptual replication, N = 240, six versions. Only 30-31% chose the correct cell. No rarity effect (rare 30% vs common 31.3%, chi2 = .039). What mattered was perceived informativeness (features differing in rarity: 40% vs 25.6%, p < .05) and whether the given percentage was low (40.8% vs 20%, p < .001). (b13)
- **Wolf, Gruppen and Billi (1988).** A short teaching step (competing-hypotheses heuristic plus Bayes' theorem) improved data choice in medical students: intervention n = 119 vs control n = 89, p < .001. Abstract only, nonequivalent groups, effect size unknown. (d16)
- **Normative dispute.** Crupi, Tentori and Lombardi (2009) argued that asking for P(f|h) can be Bayes-rational under some assumptions, so the "bias" may be a misapplied norm [M] (a12). Tweney et al. (2010) disputed this. Crupi and Girotto (2014) say the classical reading is now judged inadequate by all parties (d18).
- **Search habit, not only number misreading.** Anderson and Doherty (2024) found same-hypothesis preferences persist when no percentages are shown. Abstract only. (d17)
- **Accounts of cause.** Working memory holds one hypothesis at a time (Mynatt, Doherty and Dragan 1993); failure of explicit, dual-process reasoning (Evans, Venn and Feeney 2002). Both second-hand (b15).

Net: the existence of a same-hypothesis search tilt is solid. Its size depends on task wording, rarity, perceived informativeness and the numbers shown. The label "irrational" is contested.

### 2.3 Heuer and ACH

- **Heuer (1999), ch. 8, Analysis of Competing Hypotheses.** Eight steps. Step 3 is called the most important: work across the matrix one evidence item at a time, and mark it consistent (C), inconsistent (I) or not applicable with each hypothesis. Step 4 deletes items consistent with all. Step 5 ranks hypotheses by fewest inconsistent items, not most consistent. Step 6 re-checks the few linchpin items and runs a deception check. (a01, a02, b01, b02)
- Heuer calls ACH "a surprisingly effective, proven process" but cites no experiment (b01). He said that if tests failed he would "stick with common sense" (a10).
- The matrix uses ordinal marks. The numeric version (ask "if this hypothesis is true, what is the probability I would see this evidence?") is only an optional refinement (a01).
- Motive: people cannot hold 3 to 7 hypotheses in working memory; more than seven should be grouped (a02, b01).
- Heuer's ch. 4 and 5 also supply the Wason account and a nurse correlation study (Smedslund-style): 18 of 19 given a zero-correlation deck saw at least a weak relation; more than half used only the A-and-F cell (a04; re-checked by the cross-checker). The "86 subjects, none showed intuitive understanding" figure was not re-checked.

### 2.4 The ACH test record

Mandel and Tetlock (2018) argue that ACH leaves too much to the analyst. "Consistency" can mean P(E|H), P(H|E), necessity or plausibility, and the common reading is representativeness: "The meaning of consistency is left up to the analyst to interpret" (a10).

The randomised tests are covered in section 5. In short, none shows an accuracy or coherence gain from the whole matrix, and one shows a mild loss.

### 2.5 The 2024-2026 LLM turn

Three research threads arrived together:

1. **Rule-discovery games** (Wason-style): WILT 2024, FalsifyBench 2026, Jhaveri et al. 2026. Do LLMs test outside their guess?
2. **Information-gain question choice**: Uncertainty of Thoughts 2024, Active Task Disambiguation 2025, BED-LLM 2026, Collaborative Battleship 2026, BoxingGym 2025, QuestBench 2025. Can code-side expected information gain beat the model's own choice of question?
3. **Belief updating and evidence acquisition in context**: Bayesian Teaching (Qiu et al.), BayesBench, From Prompts to Posteriors, AdaptFuse, Ling's hindsight-to-foresight study, WORTH, Martingale score. Can the model weigh evidence, and does it ask for the right evidence?

Section 6 gives the numbers.

---

## 3. Core findings with exact numbers

Status column: **E** established (two or more independent sources), **S** single source, **C** contested, plus scope notes. "Human" or "LLM" says what was studied.

### 3.1 Human findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Evidence consistent with all hypotheses has no diagnostic value | Principle, no test | Heuer ch. 8 (a01, b01); Good (a28, not opened) | S (K01); the principle is the likelihood ratio equal to 1 |
| Wason 2-4-6: people test with what their guess predicts | 6 of 29 right on first announcement; 0 of 51 in a repeat | Heuer citing Wason (a03) | E for the pattern in people and LLMs (K03) |
| Pseudodiagnosticity, medical students | 83% of 65 chose same-hypothesis information | Kern and Doherty 1982, abstract (d15) | C (K02) |
| Pseudodiagnosticity, replication | 30-31% chose correct cell B; N = 240; rarity effect absent | D'Addario and Macchi 2012 (b13) | C |
| Pseudodiagnosticity with rare feature | 43% cell B, 44% cell C | Feeney et al., second-hand (b14) | C |
| Bias persists without percentages | Existence only; no N read | Anderson and Doherty 2024, abstract (d17) | S |
| Short training reduces pseudodiagnostic choice | n = 119 vs 89; p < .001; effect size unknown | Wolf et al. 1988, abstract (d16) | S (K31) |
| ACH, 50 UK analysts: no accuracy gain | MAE 0.26 ACH vs 0.21 control; d = .43; p = .14; 25 per arm | Mandel, Karvetski, Dhami 2018 (b03) | E that the matrix is unproven (K04) |
| ACH raised cue-usefulness ratings | Within-person r = .68 vs .17; d = 1.59; p < .001 | Same (b03) | S (K05) |
| ...but ratings did not carry to accuracy | r(24) = -.10 (ACH), -.42 (control) | Same (b04) | S |
| ACH, 227 panellists: no coherence gain | Reliability MAD .22 vs .18, F = 3.86, p = .05, d = 0.20 for control; coherence agreement .65, d = 0.06 | Karvetski and Mandel 2020 (a05, b07) | E (K04) |
| Non-diagnostic evidence still moved ACH scores | Intercept .233, slope .502, R2 = .055; about 32% (30% on alternate coding) of full-diagnostic impact | Same (a06, b07) | S (K06). The cross-checker note: "non-diagnostic" here means linked to non-diagnostic reliability/credibility ratings, on the matrix consistency score, ACH arm only |
| ACH users double count a perfectly correlated cue | 25% (low salience, n = 20) vs 57% (high salience, n = 21); p = .037; N = 147 | Karvetski, Mandel, Irwin 2020 (b09) | S (K07) |
| Layout changes weighing strategy | Chose consistency-favoured hypothesis: hypotheses in columns 61.8%, in rows 39.2%, text 67.3%; chi2(2) = 9.43; p = .009; N = 161 | Dhami et al. 2024 (a08) | S (K08) |
| Analysts mostly balance consistent and inconsistent evidence | 66.1% balanced, 19.4% consistency, 14.5% inconsistency; N = 62 Dutch military | Same (a08) | S |
| ACH instruction does not change credibility ratings | F(1,153) = .21; p = .649; N = 159 | Otzipka and Volbert 2026 (a09) | E with others (K04) |
| ACH did not reduce serial-position or confirmation bias | N about 39 | Whitesmith 2018 via review (b12) | S, second-hand |
| ACH review: 7 articles, 6 experiments, little to no benefit, maybe harm | Lehner 2008 N = 24; Mandel 2018 N = 50; Karvetski 2020 N = 147; Whitesmith 2018 N = 39; Maegherman 2021 N = 191 (38% of ACH group used the matrix) | Wilcox and Mandel 2023 (b10) | E, no pooled effect |
| Lehner 2008: ACH cut confirmation bias for novices, not experts | N = 24 | Via review (b10) | S, contrary to later tests |
| Most control analysts built a matrix unprompted | 16 of 25 | Dhami, Belton, Mandel 2019 via review (b11) | S, second-hand |
| Probabilities over exclusive hypotheses are incoherent | Four tribe probabilities summed to 1.54 (control, d = 0.96) and 1.77 (ACH, d = 1.69); 91.9% of Dutch analysts nonadditive | Mandel 2018 (b05); Dhami 2024 (a08); Karvetski 2020 (a07) | E (K09) |
| Forcing coherence in code cuts error | MAE .23 to .15 (35%, d = 0.96); plain normalising gave .13; .09 after averaging 50 analysts (61% cut) | Mandel 2018 (b06) | E (K10) |
| ...but most of the aggregation gain is variance reduction | Random responses gained about as much | Cross-check of b06, b09 | E (K10) |
| Search attention is partly bottom-up salience | N = 80, 80, 90; salience effect found; indirect coherence effect not (pooled t(249) = 1.51, p = .13) | Broder et al. 2021 (a15) | S |

### 3.2 LLM findings: choosing the next test

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Instruction-tuned LLMs mostly make positive tests; reasoning models fewer | Positive-test share 66-82% (instruction-tuned) vs 24-39% (reasoning); success 33-41% vs 68-75% | FalsifyBench (b17, c10) | E for the pattern (K03) |
| Success tracks falsification | Spearman rho = -0.779, p = .003 (bias vs success); n = 1,200 games, bias coefficient -4.15 (OR 0.016); oracle error -0.12 (no effect) | b17 | S as a single paper, v1 only |
| Conclusive falsification rate per turn | GPT-OSS-20B 59.2%, GPT-OSS-120B 53.4%, GPT-5.2-Chat 49.5%, GPT-5-Nano 26.6%, Llama-4-Maverick 18.0%; rho = -0.937 with bias | b18 | S |
| Wason 2-4-6 style, 11 LLMs | Success 6-78% (45-turn cap, 80 episodes per cell); thinking models do better; success rises with incompatible-to-compatible test ratio | Jhaveri et al. (d01, b19) | S |
| Hidden-rule game, 2024 models | Best 14/50 (Claude 3.5 Sonnet); o1-mini 13; o1-preview 12; GPT-4o 9; Llama 405B 8; GPT-4o-mini 6 (27.22 guesses, 9.78 repeats); Flash 8b 0 | WILT (b21, c12) | S; older models |
| Test choice and inference are separate skills | o1-mini 13/50 alone, 19/50 on chatgpt-4o-latest's tests | WILT (c13) | S |
| Prompted LLMs ask low-information questions | 20 Questions Prompt-Only 8-45% (Animals); Battleship zero-information questions: Llama-4-Scout 18.5%, GPT-4o 14.6%; QuestBench logic and planning 40-50% | b24, a17, a19 | E (K11) |
| Finding the right question is not solving the problem | QuestBench: GSM-Q above 80% for best models, Logic-Q and Planning-Q 40-50% | a19 | S; tables garbled |
| Code-side expected information gain (EIG) beats model-chosen questions, 2024-25 models | BED-LLM +37.4 points mean, never decreased: Animals GPT-4o 45 to 93, GPT-4o-mini 44 to 88, Llama-3.1-8B 8 to 63; Celebrities Mistral-Large 19 to 91; Things GPT-4o 34 to 64, Llama-3.1-8B 10 to 26 | a17, b22 | C (K12) |
| Uncertainty of Thoughts | "+38.1%" mean over 5 datasets and 5 LLMs (unit unclear, relative or points); DX 97.0%; troubleshooting 43.7 to 67.3 (23.6 points); beats CoT-SC by 33.8, Reflexion by 29.9 | a16, c15 | C; unit ambiguous |
| EIG in Battleship | Small models beat humans; Llama-4-Scout win rate 8% to 82% vs humans; GPT-5 itself gained little | b24 | C |
| A crude balanced-split rule gets much of the gain | Animals GPT-4o-mini: 44 / 78 / 88 (Prompt-Only / Split / BED-LLM); Llama-3.1-8B: 8 / 49 / 63; Things GPT-4o: 34 / 40 / 64 | a17, c17 | S (K13) |
| EIG ablations | Full 93 vs in-context beliefs 25 (Animals GPT-4o); marginal entropy 88; data estimation 70; implicit max 70 | a17, b23 | S |
| One-prompt in-context EIG recipe matches BED-LLM on current reasoning models | Figure only; 40 animals, 20 questions, 3 open reasoning models | From Prompts to Posteriors (d05) | C; the counter-result that moved K12 to contested |
| EIG over model-written programs is not a free win | Multiples of 3 or 7: 8 queries (EIG) vs DNF (positive test) vs 13 (random); odd multiples of 3: 14 / 35 / 21; multiples of 4: 7 / 4 / 2 (EIG worse) | Wild Guesses (d04) | C (K26); workshop paper, one run per cell |
| Free chain of thought adds little to question choice | Animals: GPT-4o-mini 44 to 55, Mistral-Large 33 to 35, GPT-4o 45 to 62, Llama-3.1-8B 8 to 19 | a17, c17 | C (K14) |
| Gains shrink with stronger models | Kobalczyk: gap smaller for more capable models; GPT-5 gained little in Battleship | b25, b24 | S |

### 3.3 LLM findings: asking for evidence and weighing it

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Models diagnose well with all evidence, badly when they must ask | Fullsight 91.0%, Foresight 74.2% (pair-weighted); primary cohort N = 181, k = 3: Foresight 33.1% vs hindsight 73.5% (gap 40.3, CI 32.6-48.6) | Ling 2026 (a20) | S (K11, K22) |
| Part of that gap is fewer facts, most is which facts | Count-matched hindsight 63.0% (gap 29.8, CI 22.1-37.6; 28.7 at k = 6) | d07 | S |
| Set swap vs reorder vs reverse | Set replacement +26.7; reorder same set +9.3 (34.3 to 43.7); reverse hindsight order -26.0 | d07 | S |
| Critical evidence is rarely requested | Recall 16.0% at k = 3, 35.7% at k = 12; top fact never reached in 6 requests in 64.6% of cases | d07 | S |
| Request slots wasted | 58.7% new, 25.3% repeat, 16.0% no match; 3 requests give 2.09 unique facts | d08 | S (K27) |
| Recovery depends on failure type | After a duplicate: switch category 49.7% vs stay 17.1%. After a no-match: stay 65.4% vs switch 27.6% | d08 | S |
| A fixed menu does not beat free-form | 31.7% for both at k = 3 | d08 | S |
| One decisive item rescues a wrong diagnosis | Rank 1 fact +38.8 points over a control fact; Rank 2 +24.8; Rank 3 +10.3 | d09 | S (K30) |
| Distribution shift is not truth-directed gain | JSD 0.633 hindsight vs 0.531 foresight, but reference-diagnosis gain 0.298 vs 0.084 at k = 3 | d09 | S |
| Exculpatory items skipped | Mystery pilot: 31 of 37 runs chose the same wrong trio; suspicion sentences chosen 25 times, exoneration 0 | WORTH (a23, d14) | S (K30); two-story pilot |
| Clue hits do not predict correct answers | GPT-5.6 Sol most clues (3.4 of 12), fewest correct people (0.8 of 3) | d14 | S |
| LLMs update beliefs poorly from sequential evidence | Flight task: 36-58% vs Bayesian assistant 81%; most stop improving after round 1 | Qiu et al. (c01) | E (K15) |
| Prompt fixes failed | CoT, numeric option encoding, 30 rounds, base models: no meaningful gain | c02 | S |
| Incoherence across chats, not within one dialogue | Dutch-book violations above 50% of 30 scenarios across chats; about 10% (Gemini) and 1 of 30 (Gemma) within a dialogue | d06, c04 | E with others (K15, K28) |
| No-reasoning update drifts from oracle | Example 0.643/0.357 vs oracle 0.967/0.033; reasoning gave 0.967/0.033; Python tool brought hard-world KL near 0 | d06, c05 | E (K16) |
| Updating cut success by at least 30% without reasoning | 20 Questions (40 animals), ProteinWorld (40 runs) | c04 | S |
| Base models under-update | Update slope 0.295-0.482; direction agreement 63.7-75.8%; BCC rises with size (r = 0.906 vs log params); 6,460 instances per model | d11 | S; self-consistency only |
| Small models under-update, large models over-update | Seven models, 3B to 70B | BayesBench (c06, d12) | S |
| Externalised Bayes closes the gap with no training | AdaptFuse 76.2 vs Bayesian teaching 73.4 vs self-consistency 44.7 (Gemma, flight task); no-EMA ablation 74.0 | c24 | S, needs hand-specified likelihoods |
| Logit and verbalised confidence are not diagnostic probabilities | AUROC 49.9 (CI 47.8-51.9) and 50.9 (48.7-53.1) | c26 | S (K17) |
| Belief entrenchment | Martingale score 0.103 (ChangeMyView), 0.037 (forecasting), 0.086 (OpenReview); about 0.04 coincided with worse-than-chance forecasts | d13 | S |
| Pro-user bias under active engagement | Unwarranted-behaviour rated 72% (defending frame) vs 60% neutral vs 56% conceding | c07, d12 | S |
| Chatbot feedback suppresses discovery | N = 557; discovery 29.5% random vs 5.9% default GPT; default GPT equivalent to rule-confirming (8.4%); confidence +5.4 for GPT | Batista and Griffiths (c08) | S |
| Absent findings are mishandled | Interaction strength 86.6-89.6% faithful support or conflict; negated or absent misuse 1.2-3.0%; blind review of 130 items, five reviewers agreed on 77% | c19 | S (K21) |
| Hypothesis table gains a little | Top-1 83.2 (none), 85.4 (ReAct), 87.6 (table) | AgentRCA (c20) | C (K14) |
| Counterfactual challenge and structured investigation worth most | Full 79.2; minus structured investigation 72.8; minus counterfactual critique 74.0; minus weight updates 78.5 | Investigator (c22, c23) | C |
| Selection, not generation, is the weak spot | Pool potential 89.2, selected 79.2 | c22, c23 | S (K23) |
| ACH prompt without training adds little | About +2.3 for the fixed decision agent; trained +7.0 to +7.8 | AgentCDM (a24, c28) | S (K25) |
| Content effect on Wason | Realistic beats abstract: z > 2.2 for Chinchilla, PaLM 2-L, GPT-3.5, humans | Lampinen (a22, b27) | S (K24) |

### 3.4 Prompt instructions for negative tests

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Think-in-Opposites (TiO) raised success in all 11 model-mode pairs | 42% to 56% average; Qwen3-8B thinking 21 to 36; Qwen3-32B thinking 41 to 61; Gemini-2.5-Pro 73 to 78; GPT-4o 11 to 16 | d02, b19 | S (K19) |
| Dual-Goal helped 8 of 11 and hurt weak non-thinking models | Qwen3-14B 23 to 13; Qwen3-32B 33 to 10 | d02 | S |
| No equal-token control | Thinking tokens per turn Qwen3-8B 1088 baseline vs 1716 TiO vs 2143 Dual-Goal | d02 | S |
| Transfer to Blicket is mixed | Thinking Qwen3-32B 57 to 86; non-thinking Qwen3-32B 64 to 56; Qwen3-14B 25 to 20 | d03 | S |
| Fine-tuned distillation of the behaviour works | Qwen3-32B 0.41 to 0.64 | b20 | S; needs training |

---

## 4. Mechanisms and models

Written so an engineer can implement them. The model fills slots; the program computes (SCHEMA section 1).

### 4.1 Likelihood ratio and log-odds

For two hypotheses H1, H2 and an item E:

- LR(E) = P(E|H1) / P(E|H2). LR = 1 means the item does not discriminate.
- Log LR is the weight. For independent items, total weight = sum of log LRs (Good; a28).
- For k hypotheses, posterior is prior times likelihood, then normalise. Normalising is done in code, never by the model (G5).
- Independence is an assumption. Correlated items must be grouped and counted once (b09, K07).

**What the model supplies:** one number or a bucket per (item, hypothesis) cell, elicited in one dialogue, with the reference class stated. **What code does:** the product, the sum check, the normalisation, the ranking.

Risk: the model's likelihoods may be poor for real analytic evidence. Nobody has measured that against ground truth (critique gap 5, K28). Internal likelihoods are directionally right 64-76% of the time (d11).

### 4.2 Expected information gain (EIG) over candidate tests

Given a hypothesis set with probabilities p(h), and a candidate test q with possible outcomes o:

- Prior entropy: H(p).
- For each outcome o: P(o) = sum over h of p(h) P(o|h); posterior p(h|o) is proportional to p(h) P(o|h).
- EIG(q) = H(p) minus the expected posterior entropy, averaged over o. (a16, a18)
- Pick the q with highest EIG. A test with EIG near zero cannot change belief, whatever the outcome. In Battleship, 14.6-18.5% of model-asked questions had zero EIG (b24).

Notes:
- EIG is not the same as the entropy of the answer. A test with an uncertain answer may not separate hypotheses. BED-LLM's marginal-entropy ablation fell below full EIG in most cells (b23: Animals Llama-3.3-70B 68 vs 79; Celebrities Qwen2.5-72B 59 vs 84).
- Choice of score matters (Nelson; b16).

### 4.3 The cheap version: Split

Choose the test that divides the live hypotheses most evenly into two groups. On yes/no tests with deterministic outcomes this equals EIG. With noisy outcomes it loses a little. Measured: Split reached 78 vs BED-LLM 88 vs Prompt-Only 44 on Animals with GPT-4o-mini (a17). Caveat: in BED-LLM the "Split" baseline reuses BED-LLM's own filtering (a17 limits), so it is a strong baseline.

### 4.4 BED-LLM pipeline (a17, b22)

1. Keep a history of (question, answer) pairs.
2. Sample candidate hypotheses from the LLM, conditioned on the full history.
3. Filter out hypotheses that contradict the history. Ablation: unfiltered generation drops sharply (in-context beliefs 25 vs 93, Animals GPT-4o).
4. For each candidate question, have the LLM give P(answer | hypothesis, question).
5. Compute EIG in code over the hypothesis set.
6. Ask the top question; update; repeat.

Cost: many calls per turn. Needs a hypothesis set that can be sampled and filtered.

### 4.5 Uncertainty of Thoughts (a16)

Simulate answers to each candidate question, score the entropy drop, propagate reward up a short tree (depth three for cost), pick the best path. Closed-set (candidates given) gains are larger than open-set. Depth limited for cost. The reported gains are relative to direct prompting.

### 4.6 Externalised posterior (AdaptFuse; c24)

A symbolic module holds the Bayesian posterior. The frozen LLM only supplies preference signals (likelihood readings). Needs a hand-specified likelihood and hypothesis set. Much of the margin disappears without the exponential-moving-average step (74.0 without vs 76.2 with).

### 4.7 Split the Labor pattern (d10)

The model reads each source alone and emits a fixed tuple: (hypothesis, reliability bucket, rationale, provenance). Code pools calibrated log-likelihood ratios. Reliability buckets come from observable properties (source length, grounded rationale), not elicited confidence. It shows analytically that summing unnormalised vote weights drifts with source count. This is a design pattern, not evidence that model-supplied LRs are good.

### 4.8 Falsification-aware test selection (b17, b18, d01)

Per test turn, code labels the test relative to the current guess:
- Compatible: the guess predicts "yes".
- Incompatible: the guess predicts "no".
- Conclusive falsification possible: a "yes" outcome would reject the guess.

Log the incompatible-to-compatible ratio (I:C). Human reference I:C 1.79 vs 0.24 (d01); thinking-model baselines 0.14-0.66. When the ratio is low, force one incompatible test. Condition (Klayman and Ha): negative tests help when the working rule may be too narrow; positive tests can falsify when it is too broad (b17 limits).

### 4.9 Request ledger (d08, b21)

Code keeps a record of every test or evidence request and the partition each produced. Exact repeats are rejected. After a duplicate, switch evidence category (49.7% recovery vs 17.1% stay). After a no-match, stay on the category and rephrase (65.4% vs 27.6%). Note: these are associations, not an intervention test.

### 4.10 Coherentise and average (b06, b09)

1. Elicit probabilities over mutually exclusive, exhaustive hypotheses.
2. Normalise to sum 1.
3. Average over N independent judgments.
Error cuts: .23 to .15 after normalising; .09 after averaging 50 analysts. Most aggregation gain is variance reduction: random responses gained about as much. For one model, samples are not independent (G4), so averaging gains will be smaller than for 50 people.

### 4.11 Why a hypothesis-conditioned data source adds no information (c09)

If data are sampled conditional on the user's hypothesis, beliefs do not move toward truth but confidence in the hypothesis grows. No person-side bias is needed. The same logic applies to a test chosen by the leading hypothesis itself: it cannot be wrong, so its outcome carries no news.

---

## 5. What holds up

### 5.1 Replications and failures

| Claim | Verdict | Detail |
|---|---|---|
| Wason-type positive-test tendency | **Holds** in people and in LLMs | Heuer 6/29 and 0/51; LLMs 66-82% positive tests when instruction-tuned (b17); success rises with I:C in 11 models (d01) |
| Pseudodiagnosticity | **Exists, size varies** | Medical students 83% (d15); replication only 30-31% correct and no rarity effect (b13); persists without percentages (d17); norm disputed (a11, d18) |
| ACH improves accuracy | **Not supported** | Four randomised tests plus a review (K04). Mandel 2018: MAE .26 vs .21, p = .14, a trend against ACH (b03) |
| ACH reduces confirmation bias | **Contested, mostly null** | Lehner 2008 (N = 24) positive for novices only; Whitesmith 2018 (about 39) and Otzipka 2026 (N = 159) null (b10, b12, a09) |
| ACH cue-rating step helps | **Single source** | r = .68 vs .17 (b03), but no link to accuracy (b04) |
| Coherence in code helps | **Holds** | .23 to .15 (b06); sums 1.54 and 1.77 (b05); 91.9% nonadditive (a08) |
| Averaging helps | **Holds, but mostly noise reduction** | .09 after averaging; random responses gained about as much (b06, b09) |
| Pure ACH prompt for LLMs helps | **Weak** | About +2.3 without training; +7 to +7.8 with training (a24); multi-agent answer selection, not evidence weighing |
| LLMs weigh sequential evidence poorly | **Holds** across tasks | 36-58% vs 81% (c01); Dutch-book above 50% across chats (c04); drift (d06); under-updating at slope 0.30-0.48 (d11) |
| Code or tool closes the weighing gap | **Holds on synthetic worlds** | Python tool KL near 0 (c05); AdaptFuse 76.2 (c24). Needs stated likelihoods |
| Code-side EIG beats model-chosen questions | **Contested** | Strong on 2024-25 models and closed sets (a16, a17, b24); naive in-context recipe matched it on current reasoning models (d05); loses on simple rules (d04); gain shrinks with model strength (b25, b24) |

### 5.2 Moderators and boundary conditions

- **Model strength and mode.** Reasoning models make fewer positive tests (24-39% vs 66-82%) and succeed more (b17). But 2024 reasoning models did not dominate WILT (o1-preview 12/50 vs Claude 3.5 Sonnet 14/50; b21). Different tasks (semantic vs numeric) and generations. Small reasoning models did worse than instruction-tuned ones (GPT-5-Nano 12%, Qwen3.5-9B 21%; b17).
- **Thinking gain is not only less confirmation.** In Jhaveri et al. thinking raised success without consistently raising I:C (d01). So K18 ("reasoning models succeed because they test more outside their hypothesis") is only partly right.
- **Hypothesis set.** The big EIG gains need a closed or sampleable hypothesis set and an LLM answerer (critique weak spots). Open-set gains are smaller (a16).
- **Hypothesis too narrow or too broad.** Negative tests only pay off when the working rule may be too narrow (b17 limits; Klayman and Ha).
- **Support mismatch.** Very diagnostic queries push the posterior to regions where the model cannot propose valid hypotheses (d04). This is why EIG lost on simple rules.
- **Presentation.** Layout moved choice from 61.8% to 39.2% in people (a08). Perceived informativeness and the given percentage moved pseudodiagnosticity (b13). Position in context changes LLM evidence weight (d19, second-hand).
- **Dialogue vs separate chats.** Coherence is poor across chats and good within one dialogue (d06). Ask likelihoods for all hypotheses in the same dialogue.
- **Content.** Realistic content improves Wason performance in LLMs and people (a22). Abstract hypothesis sets, like ARC, are the hard case.
- **Stance in context.** A stated user hypothesis anchors the model (d12, d13) and makes evidence sampling uninformative (c08). Neither tested removal at the evidence-request step.
- **Correlated evidence.** ACH users double counted a perfectly correlated cue (25% to 57% by salience; b09). Factorised Bayes also failed.
- **Absence.** Negated or absent findings are where shortcut-like LLM errors cluster (c19).

### 5.3 Interventions that worked

- Code-side normalising of probabilities (b06). [E]
- Moving the posterior into code or a tool (c05, c24, d06). [E]
- Code-side EIG or Split for question choice on 2024-25 models and closed hypothesis sets (a17, b24). [C]
- A negative-test prompt line on thinking models (TiO, all 11 cells improved; d02). [S]
- Supplying one top-ranked fact: +38.8 points (d09), a diagnostic of the problem, not a method. [S]
- A short teaching step for medical students: p < .001 (d16). [S]
- Required ranked hypothesis table: 83.2 to 87.6 top-1 (c20). [C]
- Counterfactual challenge of the leading hypothesis: worth about 5 to 6 points in the ablation (c23). [S]
- Row layout for hypotheses: 61.8% to 39.2% consistency-favoured choice in people (a08). [S]

### 5.4 Interventions that did not work

- The whole ACH matrix (K04). No accuracy, coherence or bias gain in four randomised tests.
- ACH rejection-only scoring. Ignoring support and base rates made ACH users use base rates less (b11); Mandel et al. call it a misapplication of Popper (b02).
- Chain of thought alone for belief updating (c02) and a small lift for question choice (c17).
- 30 rounds instead of 5 (c02).
- Dual-Goal on weak non-thinking models (d02): Qwen3-14B 23 to 13, Qwen3-32B 33 to 10.
- A fixed menu of evidence targets (d08): 31.7% both ways.
- A big move in the belief distribution as a sign of good use (d09): JSD did not track truth-directed gain.
- Hypothesis-prompt wording that tells the model to be "analytic" (SCHEMA 4b, from F07). Not re-tested here.

---

## 6. Language models

### 6.1 How they behave

1. **They test what their guess predicts.** Instruction-tuned models use positive tests 66-82% of the time; success tracks fewer positive tests (rho = -0.779; b17). In Jhaveri et al. all 11 models showed the bias, success from 6% to 78% (d01).
2. **They repeat tests and ask empty questions.** WILT: GPT-4o-mini made 27.22 guesses and 9.78 repeats on average (b21). Ling: 25.3% repeated facts, 16.0% matched nothing (d08). Battleship: 14.6-18.5% of questions had zero EIG (b24).
3. **They pick the wrong facts.** Count-matched, the gap to hindsight is still about 30 points (63.0% vs 33.1%; d07). Critical-evidence recall at k = 3 is 16.0%. Selection, not generation, was the bottleneck in the investigation agent (pool 89.2 vs selected 79.2; c22).
4. **They skip exculpatory evidence.** 25 suspicion sentences, 0 exoneration sentences (d14). Clue hits did not predict correct answers.
5. **They update badly and unevenly.** Under-update by slope 0.30-0.48 (d11); small models under-update, large ones over-update (c06); accuracy plateaus after one round (c01); incoherent across chats (c04).
6. **They conform to the stated hypothesis.** Entrenchment (d13), pro-user bias under active engagement (c07, d12); chatbot feedback cut human discovery from 29.5% to 5.9% (c08).
7. **They handle absence worst.** Misuse concentrates in negated findings (c19).
8. **Content matters.** Realistic rules beat abstract ones (a22).
9. **Stated confidence is no likelihood.** AUROC about 50 (c26).

### 6.2 What changed behaviour, and by how much

| Intervention | Effect | Conditions | Source |
|---|---|---|---|
| Code-side EIG (BED-LLM) | +37.4 points mean over prompt-only; never decreased | 2024-25 models; 20 Questions; closed sets | a17, b22 |
| Split rule | Animals GPT-4o-mini 44 to 78; Llama-3.1-8B 8 to 49 | Same | a17 |
| Sampled EIG in Battleship | Spotter accuracy up to +14.7 points; targeting F1 Llama-4-Scout 0.367 to 0.764; Guess Who +28.3 to +42.4 | Sampleable board space; GPT-5 gained little | b24 |
| Uncertainty of Thoughts | "+38.1%" mean; troubleshooting 43.7 to 67.3 | Unit unclear | a16, c15 |
| One-prompt in-context EIG | Matched BED-LLM on three reasoning models | Figure only | d05 |
| Python tool or reasoning mode on updating | KL near 0 | Synthetic worlds with stated likelihoods | c05, d06 |
| AdaptFuse (symbolic posterior) | 76.2 vs 44.7 self-consistency | Needs hand-specified likelihoods | c24 |
| Think-in-Opposites | 42% to 56% mean; all 11 cells up | Not equal-token (+20 to 100% thinking tokens per turn) | d02 |
| Dual-Goal | 8 of 11 up; weak non-thinking models down by 10 to 23 points | Same | d02 |
| Hypothesis table | +4.4 points top-1 | Industrial fault diagnosis | c20 |
| Counterfactual critique | About 5 points in ablation | One backbone; 100 cases | c23 |
| ACH matrix prompt | About +2.3 points | Multiple choice; no training | a24 |
| ACH matrix with training | +7.0 to +7.8 | Training | a24 |
| Distilling TiO traces | Qwen3-32B 0.41 to 0.64 | Training | b20 |

### 6.3 Reading the table honestly

- Most gains come from games with a sampleable hypothesis set and an LLM answerer. Analytic cases with open hypotheses have no test.
- The harness advantage shrinks with model strength (b25, b24, d05). It may be gone for current reasoning models. The Prompts to Posteriors authors call the harness a moving target.
- Many numbers are single preprints under review: Ling, FalsifyBench v1, Investigator, AgentRCA, AdaptFuse.
- Only open-weight or 2024-25 models were used for belief updating. The newest frontier models are untested there.
- No study compares an ACH-style matrix alone with a plain model at equal tokens on evidence-weighing tasks (K25, critique gap 1).

---

## 7. What our agent should take

Each item names the schema part (G, S, O or memory), a status mark, and evidence ids.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep the running posterior over the live hypotheses in code, not in the model's context. The model supplies single likelihood readings; code multiplies and normalises. Reasoning mode plus a calculator also works, so verify with a check rather than trust. | G5, S7 | [E] (K15, K16, K28) | c01, c02, c04, c05, c24, d06, d11 |
| A2 | Never accept raw probabilities over exclusive hypotheses. Normalise in code and flag a sum far from 1. This confirms G5. | G5 | [E] (K09, K10) | a07, a08, b05, b06 |
| A3 | Do not add the full ACH matrix. It stays in section 4b. Add the new evidence: four randomised tests plus a review, no accuracy or coherence gain; "consistency" is ambiguous. | 4b | [E] (K04) | b03, a05, b07, a09, b12, b10, a10 |
| A4 | Log, for every S7 test, whether the leading hypothesis predicted its outcome (compatible or incompatible), the incompatible-to-compatible ratio, and whether any live hypothesis could have been rejected by it. This is measurement only; it changes no behaviour. | Section 6 logs | [E] for the pattern (K03) | b17, b18, c10, c11, d01 |
| A5 | Do not read the model's logit or verbalised confidence as P(E|H). This extends the existing 4b entry. | 4b | [S] (K17) as a single study; consistent with F09 in SCHEMA | c26 |
| A6 | Write the S7 text as "rank candidate tests by how differently the live hypotheses predict them", not "find disconfirming evidence". Wording only. | S7 | [E] for the principle (K03, K12 contested for the method) | a26, b17, a03 |

Note on A5: the schema 4b row already marks confidence-for-stopping [E] from F09 and F07. The new line is about using it as a likelihood. Treat that as [S] until the claim is replicated.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | At S7, have the model rate each live hypothesis's prediction for each candidate test (one dialogue, reference class stated), then code drops tests with equal ratings across hypotheses and ranks the rest by separation. | S7 | [S] (K01, K06, K30) | a01, a06, b07, d09, d14 |
| T2 | Split rule (balanced partition) vs full EIG vs plain choice, on self-generated hypothesis lists, at equal tokens. | S7 | [C] (K12, K13, K26) | a17, c17, d04, d05 |
| T3 | One negative-test line (Think-in-Opposites wording) per mode. Do not use Dual-Goal on non-thinking modes. | S7 | [S] (K19) | d02, d03, b19 |
| T4 | Force the rival's likelihood: "name the rival hypothesis and its likelihood for this same datum". | S7 | [S] (K31, K02 contested) | a04, d16, b13, d15 |
| T5 | Strip the user's or the agent's favoured hypothesis from the evidence-request prompt; show a neutral list of all hypotheses. Extends S1 input hygiene. | S1, S7 | [E] harm (K29), [S] remedy | c08, d12, d13, c07 |
| T6 | Request ledger: reject exact repeats; after a repeat, force a different category; after a no-match, stay and rephrase. | S7, S4 | [S] (K27) | d08, b21 |
| T7 | Cluster dependent evidence (same source, same attempt) before weighing; count a cluster once. | S7, G4 | [S] (K07) | b09 |
| T8 | Add absence probes: record, for every hypothesis, what a missing result would mean. | S7 | [S] (K21) | c19 |
| T9 | Shuffle evidence order and average over orders in the rating step. | S7 | [S], second-hand (no claim id; critique gap 9) | d19, c27 |
| T10 | Rate diagnosticity before the leader is known; or let code compute diagnosticity from separately elicited likelihoods. | S7, G1 | [S] | b12, a10 |
| T11 | Split S7 into a test-proposer slot and an evidence-reader slot with code between them. | S7, section 1 | [S] | c13 |
| T12 | A short domain note on what each kind of evidence can and cannot discriminate. | S1, memory | [S] | c21 |
| T13 | Measure oracle-in-pool vs selected accuracy; if the gap is large, invest in the discriminating test rather than more generation. | S3/S7 | [S] (K23) | c22, c23 |
| T14 | Counterfactual challenge: "what single finding would reject the leader?" before final selection. | S7, S8 | [C] (K14) | c20, c23 |
| T15 | Memory: store the evidence-category and test type that separated rivals for a problem class. | memory | [D] | d08 |

Do not adopt (also record in 4b once confirmed on our bench):
- ACH rejection-only scoring. Keep support and base rates (b02, b11).
- Dual-Goal wording for non-thinking backbones (d02).
- AgentCDM-style ACH matrix aggregation across agents, which conflicts with G9 (a24).

---

## 8. Concrete tests on our bench

Rule for all tests: both arms get the same token budget, set by the more expensive arm. Setup cost counts (G7). Use items with known ground truth. Report mean over at least 3 seeds and a paired difference with a confidence interval. Each test below says the item type, arms, metric and expected effect from the literature (a guess of direction, not a promise).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | **Planted decisive item.** A case with N evidence items (N = 10 to 20) and 2 to 4 hypotheses; one item discriminates, the rest fit all. Include a variant where the decisive item is exculpatory. | (a) plain pick-the-best hypothesis; (b) per-item rating against every hypothesis, code drops equal-rated items, then pick; (c) (b) plus the leader-challenge line | Accuracy of final pick; share of runs that use the decisive item; share of runs that use the exculpatory item | Unknown. Ling shows +38.8 from supplying the decisive fact (d09); WORTH shows 0 exoneration picks (d14). Expect a gain on the exculpatory variant; the large gain claimed for supplying the fact is not a bound on a method. |
| B2 | **Rule-discovery game** (Wason 2-4-6 style, FalsifyBench style, plus ARC-like two-program ties). Hidden rule narrower than the first guess. | (a) plain; (b) TiO line; (c) code forces one incompatible test when I:C is below a threshold | Success at fixed turns; positive-test share; I:C; conclusive falsification rate per turn | Success up 5 to 15 points on thinking modes (d02). Run in direct, short-reason and long-reason modes. Watch non-thinking modes for loss. |
| B3 | **Hidden-hypothesis game with a known set** (20 Questions with a closed list of 40 to 100). | (a) plain; (b) Split; (c) full EIG with model-supplied likelihoods; (d) one-prompt in-context EIG | Success at 20 turns; calls and tokens | Split recovers most of the gain over plain on a non-reasoning backbone (a17). On a reasoning backbone (d) may match (c) (d05). |
| B4 | **Self-generated hypotheses on non-guessing tasks** (diagnosis vignettes, ARC rule selection among model-written programs). | (a) plain choice; (b) Split on the model's own candidate list; (c) EIG; (d) switch policy: cheap tests first, EIG when stalled for 2 rounds | Final accuracy; test count; share of tests the model could not score after a decisive result | EIG may lose on simple items (d04). The switch rule is untested. |
| B5 | **Pseudodiagnosticity 2x2 items** (Doherty style; vary rarity; with and without percentages). | (a) plain; (b) line forcing the rival's likelihood for the same datum | Share choosing the rival cell B | Plain share below 50% on strong models is plausible; (b) should move it toward 100%. Items without percentages separate search habit from number misreading (d17). |
| B6 | **Stated hypothesis in context** on the evidence-request step. | (a) request with the stated hypothesis; (b) request with a neutral list of all hypotheses | Share of requests that address only the stated hypothesis; final accuracy when the stated hypothesis is wrong | Fewer same-hypothesis requests in (b). Size unknown. |
| B7 | **Duplicate and null requests** in an evidence-request task. | (a) free requests; (b) ledger rejects repeats; (c) ledger plus forced category switch after a repeat | Unique-fact rate; accuracy at fixed request budget | Ling baseline 58.7% unique. Switch after repeat recovered 49.7% vs 17.1% staying. |
| B8 | **Probability coherence.** Ask for probabilities over exclusive hypotheses. | (a) raw; (b) code-normalised; (c) normalised and averaged over N samples; (d) random-response control | Sum of probabilities; Brier score; MAE | Normalising helps (b06). Include (d) so variance reduction is not mistaken for skill (K10). |
| B9 | **Correlated cues.** Items where cue 2 is derived from cue 1. | (a) plain weighing; (b) code clusters dependent cues by source | Double-counting rate; accuracy | Humans double count 25-57% (b09). |
| B10 | **Absence items.** The decisive finding is a missing one. | (a) plain; (b) per-hypothesis "what would absence mean" probe | Share of runs that use the absence | Mishandling concentrated in negated findings (c19). |
| B11 | **Likelihood elicitation quality.** Items with known answers. | (a) direct posterior; (b) model-rated P(E|H) pooled in code; (c) same in a reasoning mode; (d) pooled over shuffled orders | Accuracy; Brier score; calibration | Unknown. This answers critique gap 5. |
| B12 | **Layout.** Same evidence as per-hypothesis rows, per-evidence rows, prose. | Three arms | Choice change; consistency-favoured share | People moved 61.8% to 39.2% (a08). Unknown for LLMs. |
| B13 | **Oracle-in-pool gap.** Any generate-then-select task. | Measure only | Oracle accuracy minus selected accuracy | Investigator gap was 10 points (c22). |

Start with B2, B1, B3 (see UNKNOWNS.md for order).

---

## 9. What does not transfer, and why

- **Heuer's matrix as a notation for people.** It exists because people hold 3 to 7 hypotheses in working memory (b01). Code holds the matrix for free. The human benefit, if any, is not our problem.
- **Human ACH null results as proof about LLMs.** The null tests are on people filling in a matrix. A model-and-code design that computes diagnosticity from separately elicited likelihoods is a different thing. No test of that design exists.
- **Large EIG gains from games.** 20 Questions, Battleship and Guess Who have exact, sampleable hypothesis spaces and clean answers. Real analytic hypotheses are open, overlapping and probabilistic. Heuer himself says one item rarely eliminates a hypothesis (a03).
- **LLM-as-oracle noise.** In BED-LLM the answerer is another LLM; in FalsifyBench each model was also the oracle (85-95% accuracy; b17). Our benches have code checks or fixed answers.
- **Fine-tuning results.** Bayesian teaching (c03), TiO distillation (b20), AgentCDM training (a24). Our agent has no training. They show the skill is learnable, nothing more.
- **Pseudodiagnosticity percentages.** Wording-sensitive and norm-disputed. Use the presence of the habit, not the numbers (d17, d18).
- **Wason deterministic feedback.** Analysts see probabilistic evidence (a03).
- **Dutch-book and coherence results on 7B to 70B open models.** The newest frontier models are untested here (critique weak spots).
- **Thinking-mode token costs.** TiO raised thinking tokens per turn by 20 to 100% (d02). Gains under a fixed token cap are unknown.
- **Search attention in stock boards** (a15). Not hypothesis testing.
- **Hypothetical tasks with stated numbers.** Almost all human ACH evidence uses them (critique weak spots).

---

## 10. Open questions

1. Does an ACH-style matrix alone beat a plain model at equal tokens on analyst-style multi-cue items? No direct LLM test exists (K25, critique gap 1).
2. Can the model supply sound P(E|H) for real analytic evidence? Internal likelihoods are directionally right 64-76% (d11), but quality against ground truth is unmeasured (K28).
3. Does a code-side EIG pick beat plain choice on self-generated hypothesis lists in non-guessing tasks, with all calls counted? Partly closed: not reliably (d04, d05).
4. Is the Ling hindsight-foresight gap mainly about which facts? Single preprint, with reference facts chosen by an LLM with hindsight (d07).
5. Real skill vs variance reduction in coherentise-and-average, for a single model (random-response control).
6. How much of the ~30-point gap closes with a code-ranked request list? The 16.0% recall is the number to beat.
7. Does evidence layout (rows, columns, prose) change an LLM's choice, as it does for people? No study found.
8. Does removing a stated hypothesis fix evidence search? Neither c08 nor d12 tested the fix.
9. Does a hard block on repeated requests help? Only associations (d08).
10. Original Doherty 1979 percentages and the Wolf 1988 effect size remain unobtained.
11. Is the Think-in-Opposites gain real at equal tokens? And does it hold outside numeric triples and on non-thinking modes?
12. How does the harness advantage behave on the newest frontier reasoning models? The trend in d05 says it shrinks.
13. Does ordering of evidence change the posterior, and does shuffle-and-average help? Only second-hand statements (d19).
14. Is rejection-only scoring (fewest inconsistencies) worse than likelihood-based pooling in a code pipeline? Not tested for LLMs.
15. What is the right usefulness score (information gain, probability gain, impact, diagnosticity) for our tests? Nelson 2005 not opened.

---

## 11. Sources

[V] opened and read this session (full text or a page; abstract-only and second-hand cases are noted). [M] snippet, metadata or background only.

**Books and classic human studies**
- [V] Heuer (1999) Psychology of Intelligence Analysis, chs. 4, 5, 8. https://www.crest-approved.org/wp-content/uploads/2022/04/Psychology-of-Intelligence-Analysis.pdf and https://www.cia.gov/resources/csi/static/Pyschology-of-Intelligence-Analysis.pdf (a01-a04, b01, b02)
- [M] Heuer ch. 8 CIA page (recalled only) https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/ (c29)
- [M] Good (1950) Probability and the Weighing of Evidence; Fischhoff and Beyth-Marom (1983) https://doi.org/10.1037/0033-295X.90.3.239 (a28)
- [M] Wason (1960); Klayman and Ha (1987) https://doi.org/10.1037/0033-295X.94.2.211 (a26)
- [M] Oaksford and Chater (1994) https://doi.org/10.1037/0033-295X.101.4.608; Nelson (2005) https://doi.org/10.1037/0033-295x.112.4.979 (a27, b16)
- [M] Doherty, Mynatt, Tweney, Schiavo (1979) https://doi.org/10.1016/0001-6918(79)90017-9 (a13, b15)
- [M] Crupi, Tentori, Lombardi (2009) https://doi.org/10.1037/a0017050 (a12)
- [V] (abstract only) Kern and Doherty (1982) https://doi.org/10.1097/00001888-198202000-00004 (d15)
- [V] (abstract only) Wolf, Gruppen, Billi (1988) https://doi.org/10.1097/00001888-198807000-00006 (d16; a14 was snippet only)
- [V] (abstract only) Anderson and Doherty (2024) https://doi.org/10.3758/s13421-023-01502-7 (d17)
- [V] (second-hand) Feeney, Evans, Venn (2000, 2008) via D'Addario and Macchi (b14)
- [V] D'Addario and Macchi (2012) https://doi.org/10.4236/psych.2012.36069 (b13; the cross-checker could not re-parse the page)
- [V] Crupi and Girotto (2014) https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00219/full and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3952137/ (a11, d18)
- [V] Broder et al. (2021) https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8563519/fullTextXML (a15)

**ACH tests and reviews**
- [V] Mandel, Karvetski, Dhami (2018) https://doi.org/10.1017/S1930297500006628 (b03-b06)
- [V] Karvetski and Mandel (2020) https://dlab.sauder.ubc.ca/sjdm/journal/20/200430/jdm200430.html and https://doi.org/10.1017/S1930297500008159 (a05-a07, b07, b08)
- [V] Karvetski, Mandel, Irwin (2020) https://osf.io/download/fb9ej/ (b09; preprint)
- [V] Wilcox and Mandel (2023) https://osf.io/download/an32t/ (b10-b12; Dhami 2019, Whitesmith 2018, Lehner 2008 are second-hand via this review)
- [V] Dhami et al. (2024) https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11169332/fullTextXML (a08; first 100,000 characters)
- [V] Otzipka and Volbert (2026) https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13094959/fullTextXML (a09)
- [V] Mandel and Tetlock (2018) https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6309046/fullTextXML (a10)
- [V] Mellers et al. (2024) https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11373164/fullTextXML (a25)

**LLM: information-gain question choice**
- [V] Hu et al. (2024) Uncertainty of Thoughts https://arxiv.org/abs/2402.03271 (a16, c15; unit of "38.1%" ambiguous)
- [V] Choudhury et al. (2026) BED-LLM https://arxiv.org/abs/2508.21184 (a17, b22, b23, c16, c17; re-checked against Table 1)
- [V] Grand et al. (2026) Collaborative Battleship https://arxiv.org/abs/2510.20886 (b24)
- [V] Kobalczyk et al. (2025) Active Task Disambiguation https://arxiv.org/abs/2502.04485 (b25, c14)
- [V] Gandhi et al. (2025) BoxingGym https://arxiv.org/abs/2501.01540 (a18)
- [V] Li, Kim, Wang (2025) QuestBench https://arxiv.org/abs/2503.22674 (a19; tables garbled)
- [V] Li, Tamkin, Goodman, Andreas (2023) GATE https://arxiv.org/abs/2310.11589 (c18)
- [V] Chari and Pattanaik (2026) Wild Guesses https://arxiv.org/abs/2602.06818 (d04)

**LLM: negative tests and rule discovery**
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench https://arxiv.org/abs/2606.04751 (b17, b18, c10, c11; v1)
- [V] Jhaveri et al. (2026) Failing to Falsify https://arxiv.org/abs/2604.02485 (b19, b20, d01-d03; some tables garbled)
- [V] Banatt et al. (2024) WILT https://arxiv.org/abs/2410.10998 (b21, c12, c13)
- [V] Lampinen et al. (2024) content effects https://arxiv.org/abs/2207.07051 (a22, b27)
- [V] Batista and Griffiths (2026) https://arxiv.org/abs/2602.14270 (c08, c09)

**LLM: asking for and weighing evidence**
- [V] Ling (2026) From Hindsight to Foresight https://arxiv.org/abs/2610.18605 (a20, d07-d09; preprint under review)
- [V] Zou and Xu (2026) WORTH https://arxiv.org/abs/2610.27597 (a23, d14; pilot)
- [V] Qiu et al. (2026) Bayesian Teaching https://arxiv.org/abs/2503.17523 (a21, b26, c01-c03)
- [V] Filbry, Melo, Gal (2026) From Prompts to Posteriors https://arxiv.org/abs/2610.29331 (c04, c05, d05, d06, d19; related-work claims second-hand)
- [V] Samanta et al. (2026) BayesBench https://arxiv.org/abs/2606.30850 (c06, c07, d12; numbers mostly in figures)
- [V] Lin et al. (2026) AdaptFuse https://arxiv.org/abs/2604.03925 (c24)
- [V] Bayesian Coherence Coefficient study (2025) https://arxiv.org/abs/2507.17951 (d11; from an HTML summary page)
- [V] He et al. (2025) Martingale Score https://arxiv.org/abs/2512.02914 (d13)
- [V] Wu (2026) Split the Labor https://arxiv.org/abs/2608.14509 (d10)
- [V] Position paper (2024) next-word probability https://arxiv.org/abs/2411.04962 (c26)
- [V] Lei and Cooper (2026) Elicitation Matters https://arxiv.org/abs/2605.04764 (c27; numbers not extracted)
- [V] Agarwal et al. (2026) Evidence-Informed LLM Beliefs https://arxiv.org/abs/2606.29182 (c25; abstract and method only)
- [V] Liao, Deng, Ren (2026) Auditing Evidence Use https://arxiv.org/abs/2607.20848 (c19)
- [V] Wei and Fink (2026) AgentRCA https://arxiv.org/abs/2607.22385 (c20, c21)
- [V] Marozzo, Lio et al. (2026) LLM-as-an-Investigator https://arxiv.org/abs/2606.13220 (c22, c23)
- [V] Zhao et al. (2025) AgentCDM https://arxiv.org/abs/2508.11995 (a24, c28; tables garbled)

Corrections carried over from the cross-check (critique.md): c16 and c17 name the wrong first author for BED-LLM (the correct list starts with Choudhury); a16's "38.1%" has no unit in the paper; a06 is about the ACH consistency score and reliability-linked non-diagnostic items; b06's 61% mostly reflects variance reduction; a20 omits the count-matched 63.0% figure (added here).
