# Argument evaluation criteria: deep document

*Subfield D04.05. Evidence ids (a01..d17) are in evidence_a-d.jsonl; claim ids (D04.05-K01..K35) are in claims.jsonl; checks are in critique.md. Status marks: [E] established, [S] single-source, [C] contested. Cautions from critique.md are applied (98 papers / 103 datasets / 24 non-aggregated; LOGICOM raw numbers only; Qwen size curve only as "near random below about 7B").*

## 1. What it is

Argument evaluation criteria are the tests we use to decide if an argument is good. The best-known set is ARS: the premises must be **A**cceptable, **R**elevant and **S**ufficient (Johnson and Blair 1977, 1994/2006; Govier). [a01, a04, b21]

- **Acceptable.** The premise is true, or acceptable in some other way (plausible, common knowledge, granted by the audience). [a01, a02]
- **Relevant.** The premise gives some support to the conclusion. [a01]
- **Sufficient.** The premises together give enough support to warrant accepting the conclusion as likely, true or plausible. [a01, a05]

ARS replaced the old test "is it deductively valid?". It fits everyday arguments, which are almost never valid in the formal sense. Fallacies are then read as failures of one of the three: an unacceptable premise, an irrelevant one, or too little support. [a03] That gives a countable defect list without fallacy names.

Why it matters to our agent. Open answers (essays, advice, explanations, moral or policy claims) have no code check. Step S8 (Verify) needs something better than "check your answer". ARS is a short, theory-backed checklist for that step. The key findings of this document:

1. Real arguments fail on sufficiency far more than on relevance. [a09, c09]
2. Sufficiency is also the criterion that humans and models judge least reliably on hard items. [b26]
3. A generic "review your answer" pass often hurts. [d03]
4. No study has tested an ARS checklist as a Verify step on end-task quality. [b27, d17]

So ARS is a promising design, not a proven one. Most of the evidence is about how well people and models can rate arguments, not about whether rating improves answers.

## 2. History and theories in depth

**Founding (1970s to 2010).** Johnson and Blair, *Logical Self-Defense* (1977; later editions to 2006), proposed that a good argument has acceptable, relevant and sufficient premises (RSA). Govier, *A Practical Study of Argument* (1985 to 2010), uses the same three tests under the label ARG (acceptability, relevance, grounds). Both books were seen only through citations and the SEP in this research; they were not opened. [a04, b21, c27]

**Informal logic around ARS (from SEP, a01 to a03, d14 to d16).**
- Acceptability is not the same as truth. Under uncertainty a premise may be only plausible. In a persuasion dialogue it may have to be acceptable to the particular audience. A true premise may be unacceptable in a setting like a legal hearing. [a02]
- Relevance and sufficiency are intuitive and graded. No numeric measure exists. [d16]
- A fallacy counts as one only if the mistake is common enough to matter (Johnson 1987 frequency requirement). [d14]
- Sufficiency for conductive arguments (many non-decisive reasons) is cumulative: you collect enough reasons without proving the conclusion (Johnson and Blair 2011). Possin (2016) is a sceptic. [a03, d16]
- Hansen (2012) argues informal logic should not assess premise acceptability at all. [a01]
- Boudry, Paglieri and Pigliucci (2015), second-hand: normative notions like fallacies rarely fit real arguments and are too refined to operationalise. [a27, snippet only]

**Computational turn (2016 to 2017).** Wachsmuth et al. (2017) built a 15-dimension taxonomy. Cogency = local acceptability + local relevance + local sufficiency. Dialectical (global) versions add one new idea: global sufficiency means the anticipated counter-arguments are rebutted. Dialectical quality builds on rhetorical, which builds on logical quality. [a08, a28] Stab and Gurevych (2017) built the first sufficiency corpus on essays. [a05, a06]

**Perspectives on quality.** Lauscher et al. (2020) found that four experts could not tell the 15 sub-dimensions apart and collapsed them to cogency, effectiveness and reasonableness. [a17] Romberg et al. (2025) review 98 papers that introduce 103 datasets; only 24 keep non-aggregated labels, and quality is perspective-dependent: expert, crowd and novice groups differ. [b14, c20, critique]

**Rival: the Bayesian view.** Hahn and Oaksford (2007): argument strength is graded and depends on content (prior belief in the conclusion, source reliability, alternatives). The same form (argument from ignorance, circular argument, slippery slope) can be strong or weak. People's ratings follow these factors. [a25, a26] This is a challenge to form-only checklists. No LLM study compares the two. [K22]

**LLM turn (2023 to 2026).** Work moved to using LLMs as ARS judges (Mirzakhmedova 2024, ConQRet 2024, Ocampo 2026), as sufficiency checkers (CASA 2024), as critical-question generators (2024/2025), and as subjects whose own justifications are scored on Govier's tests (Henselmans 2026). Wachsmuth et al. (2024) argue that LLMs should be instructed with argumentation theory rather than tuned to leaderboards; this is a position, not a result. [a19]

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| ARS is the standard definition; NLP nests it locally (cogency) and globally (reasonableness) | 15 dimensions; 320 args, 304 kept, 3 experts, over 14,000 assessments | a01, a05, a08, b25 | [E] |
| Humans agree well on sufficiency in essays overall | 433 args; 91.07% agreement; kappa .7672; alpha .7673 | Stab and Gurevych 2017 (a06, b01) | [E] |
| ... but agreement collapses on contested cases | alpha .77 overall, .14 on the 32% of items flagged insufficient by at least one annotator | CASA footnote (b06, c17) | [E] |
| Relevance and acceptability agree worse than sufficiency in essays | kappa .435 (relevance), .259 (acceptability), 2 annotators, 100 args; skew (15% / 14% violating) lowers kappa | a06 | [S] |
| Real debate arguments are mostly insufficient, mostly relevant | of 304: local sufficiency low/med/high 172/119/13; relevance 25/155/124; acceptability 84/169/51; cogency 150/131/23; global sufficiency 231/72/1 | Wachsmuth 2017 (a09) | [E] |
| Expert agreement on ARS in debates is only moderate | alpha at most .22 for 7 annotators; best pair above .4 except global sufficiency; cogency-local sufficiency Pearson .84 | a10 | [E] |
| People notice irrelevance reliably, missing evidence less | "off-topic" with relevance r .95; "no credible evidence" with acceptability .49; Kendall .64 convincing vs quality; 736 pairs | a11 | [S] |
| Crowd needs 10+ ratings | 10 ratings, 102 workers; crowd vs expert alpha: acceptability .49, relevance .42, local sufficiency .18, cogency .27; groups of 5: .38 and .05 | a12, c18 | [E] |
| Weak support has lexical cues; CNN near human | CNN acc .843, macro F1 .827 vs human .911; SVM .785; majority .662; top cues: example, my, I, friend | a07, b02 | [E] |
| Length confounds quality labels | local sufficiency error .39 to .30 with text features; length best for overall | a16 | [E] |
| Premises alone predict sufficiency; a generated conclusion adds nothing | F1 premises-only .875; all .885; conclusion-only .553; generated .532 | Gurcke 2021 (a18, b03) | [S] |
| LLM judges are self-consistent, not valid | humans alpha .37/.40; GPT-3.5 local sufficiency .69 to .79; PaLM 2 .97 to .98 (no reasoning) vs .63 (with reasoning); Llama-70B zero- vs few-shot kappa .831 vs .49 against humans | a20, c08, c01 | [E] |
| Sufficiency is where models agree worst with humans | PaLM 2 max alpha .71 (other dims); GPT-3.5 negative values on sufficiency (approx.) | a21, b26 | [E] |
| Judge setup moves agreement a lot | GPT-4o listwise + self-consistency: cogency .47, acceptability .45, relevance .52, local sufficiency .57, global sufficiency .53; crowd global sufficiency -.17; GPT-3.5 listwise .16 alone, .35 with SC; pointwise GPT-3.5 -.40 to .64; dimension order .203 vs .447 | a22, b10, b11, c03, c04 | [E] |
| Retrieval metrics first lift agreement on long arguments | alpha .184 to .395 (up to .461 per critique), 73 args | c05 | [S] |
| Adding LLM annotations is model-specific | experts .40 to .50 with 5 PaLM 2; GPT-3.5 lowers | b08, c02 | [E] |
| Pairwise LLM judging of logic is moderate; CoT often hurts | Llama-70B few-shot Pearson .474, kappa .493, 53.0% vs majority baseline kappa .442 (48.3%); random .288; 13,952 pairs; run-to-run change at most 7.75% | a24, b15, c06, c07 | [E] |
| Small judges fail | below about 7B near random; Qwen2.5-72B above human-human kappa | b17, c21, c22 | [E] |
| LLM-made context helps a scorer | Spearman cogency .348 to .424 (BERT dual encoder) | b13, c13 | [S] |
| CASA counterfactual objection beats plain prompt (7B models) | macro-F1 73.4 vs 66.8 zero-shot; objections rational 92% vs 90%; revisions better 58% vs 7% worse; ablation 65.8 | b04, b05, c14, c15 | [S] |
| Frontier models fail grounds, not relevance, when defending moral verdicts | 9 models, 200 items, 6,778 cells; relevance fail under 0.5%; 18.2% cells low grounds; judge pair agreed 89.6% (3,389 pairs, 352 disagreements); low-grounds median 738 words vs 767 | Henselmans 2026 (c09 to c11) | [S] |
| Models defend the trace better than the post-hoc justification | 3,182 pairs, 8 models, positive local advantage in all | c12 | [S] |
| LLM debaters are swayed more by fallacious support | GPT-3.5 17% vs 10%; GPT-4 56% vs 37% (analysis A2); A1: 37 vs 29 and 67 vs 37; 1,800 debates | LOGICOM (c23) | [S] |
| Named-fallacy detection is imperfect | GPT-4 accuracy .79 (N=780), macro-F1 .71; "Appeal to Emotion" None in 16 of 41 | c24 | [S] |
| Critical questions written by LLMs are weak | at most about 57% useful; 11 models; annotator agreement .54; LLM labelling of usefulness agreed below 0.1 | c25, d02 | [E] for the 57% cap |
| Laypeople already separate strong from weak | difference 1.30 vs experts 1.61; r .62; N=278; analytic thinking r about .30; overconfidence -.15 | b18, b19 | [S] |
| Generic self-review does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1 (3 calls); GPT-4 GSM8K 95.5 to 89.0 (5 calls) | Huang 2024 (d03) | [E] |
| Concrete yes/no checklist beats free-form self-critique | LiveBench reasoning +7.8 (Command-R+); GPT-4o +0.8 overall; Self-Refine down to -25.2 in a category; judge-human exact agreement 46.4% to 52.2% | TICK/STICK (d10, d11) | [S] |
| Toulmin question gate helps reasoning plans | +4.61% reasoning, +5.4% math; best 18 of 20; GPT-4o judge; tokens not matched | CQoT (d01) | [S] |
| Separate probes with the draft hidden beat joint check | FACTSCORE 55.9 / 60.8 / 63.7 / 71.4 (baseline, joint, factored, factor+revise) | CoVe (d09) | [S] |
| CoT gains concentrate in math and symbolic tasks | symbolic +14.2, math +12.3, logical +6.9; other about +0.7 | Sprague 2025 (d04) | [E] |
| CoT can lower accuracy on judgment-style tasks | artificial grammar GPT-4o 87.5 vs 64.4 | Liu 2025 (d05) | [S] for ARS transfer |
| Judges favour own text and cues | position flips: GPT-4 25%, GPT-3.5 58%, Llama 89%; sentiment robustness .65 to .80; fallacy-oversight .92 to .99 | d06, d07 | [E] |
| One irrelevant sentence hurts math | under 30% of base problems solved across variants; 20-sample SC +11 points; best macro 45% | Shi 2023 (d08) | [S] |
| Unsupported factual claims can be flagged by resampling | AUC-PR 93.42 vs random 72.96, N=20 samples | SelfCheckGPT (d13) | [S] |
| Verbalised confidence is overconfident | mostly 80 to 100%; AUROC black-box 0.522 | d12 | [S] |
| No direct test of an ARS Verify step on end-task quality | none found | b27, d17 | gap |

## 4. Mechanisms and models

**4.1 The ARS checklist as a procedure (implementable).** Run it on the final claim and its support only, not on every sentence. [a27]

1. Extract the claim and the premise list from the draft answer (code or a short model step). Mark each premise with its source: given in the task, common knowledge, tool-checked, or model-asserted.
2. **Acceptability.** For each premise: acceptable for which audience? Is it given, checked, or only plausible? Output weak / moderate / strong, not pass/fail. [K34] Model-asserted factual premises get a resample check (4.4). A premise with no external source is marked "plausible", never "fact". [a02]
3. **Relevance.** For each premise: does it bear on the claim? Cheap, and nearly always fine in model output (fails under 0.5%). [c09] Use mainly to drop padding and irrelevant retrieved text. [d08]
4. **Sufficiency.** The premise set as a whole. Ask: what is missing, what is the strongest objection, is it answered? This is the step that fails. [a09, c09] Use these sub-probes:
   - counterfactual: "describe a case where all premises hold and the conclusion fails" (CASA, 4.2);
   - single-example flag: does the support rest on one example or personal experience? [a07]
   - global: name the strongest counter-argument and say if the draft rebuts it. [a08, a28]
5. Code decides: the defect list is data (which premise, which criterion, what is missing). Any defect goes to S5 (Revise) with the defect cited. This follows G2, as the revision acts on a named defect.

**4.2 CASA counterfactual objection.** Prompt the LLM to write contexts in which the premises hold and the conclusion fails. Then check each with an NLI model: if the context is consistent with the premises, the argument is insufficient. This gave macro-F1 73.4 vs 66.8 zero-shot on BIG-bench fallacies with Llama-2-7B, and the revisions made from the objections beat the originals 58% vs 7% worse. [b04, b05, c14] Only 7B models were tested. Engineer note: the NLI step can be replaced with a second, independent sample asked "is this objection consistent with the premises?".

**4.3 Judge configuration.** From ConQRet: pose a listwise prompt with all dimensions at once; rotate the dimension order and average three orders; use self-consistency; prefer zero-shot to few-shot. [a22, b11, c04] Cost: two extra calls for three orders. Equal-token rule: three orders cost the same as three samples of a single pointwise check, so compare those two.

**4.4 Acceptability without retrieval.** Resample 3 to 20 answers. Check each premise against the resamples. Low agreement means weak support. This detects inconsistency, not consistent error. [d13] With retrieval, ConQRet-style first-score-the-context prompts raised agreement (.184 to .395). [c05]

**4.5 Factored verification.** Run each probe as a separate call with the draft hidden or reduced to the single claim under test. Factored beat joint on factual precision (63.7 vs 60.8; factor-and-revise 71.4). [d09] Applied to ARS: run A, R and S as three separate calls, or run only S.

**4.6 Concrete questions beat abstract advice.** STICK-style yes/no items written about the specific answer beat free-form self-critique. [d10] ARS items should be turned into specific questions: "Does premise 2 (X) have a stated source?" not "Is the argument acceptable?"

**4.7 Fixed questions over invented ones.** LLMs generate useful critical questions at most about 57% of the time, and LLM labelling of usefulness agreed with humans under 0.1. [c25, d02] Use a fixed ARS question list and, if scheme questions are wanted, a fixed Walton list from sibling subfield D04.02.

**4.8 Bayesian alternative (not implemented, a design option).** Ask: how likely is the conclusion given the premises, and what else would explain them? Hahn and Oaksford rate support as posterior belief given alternatives. [a25, a26] LLM verbal confidence is poor (80 to 100% regardless), so this needs a consistency-based estimate (4.4) in place of a stated number. [d12]

## 5. What holds up

**Replicated or multiply supported.**
- Sufficiency is the common defect of real arguments; relevance is rarely the problem. Debates (Wachsmuth 2017) and frontier model answers (Henselmans 2026) show the same pattern, in different media. [a09, c09] Independent sources: 2.
- Human agreement on sufficiency is much lower than the headline suggests: alpha .77 on essays but .14 on the hard 32%; alpha .27 for experts on debates. [a06, b06, a10, a20] Four sources agree sufficiency is weak or unstable. [K04]
- Crowds need 10+ ratings. [a12, c18]
- LLM self-consistency is high and validity is moderate. [a20, a21, b07, c08, b16]
- Chain-of-thought does not reliably help judging: Ocampo (pairwise logic) and Mirzakhmedova (PaLM 2 .97 to .63 with reasoning); Sprague shows CoT gains are confined to math and symbolic tasks. [a24, a20, d04]
- Generic self-review fails without outside feedback. [d03]
- Judge bias (own text, position, sentiment). [d06, d07]
- Weak-support cues are lexical and length is a confound. [a07, a15, a16]

**Failures, caveats, moderators.**
- Model-specific effects: adding LLM raters helps with PaLM 2 and hurts with GPT-3/3.5. [b08]
- Size: below about 7B judges are near random. Ocampo found "bigger is not always better" among mid-size models; they default to one side or avoid ties. [b17, c07, b16]
- Prompt wording and dimension order move agreement a lot (.203 vs .447). [b11]
- Few-shot helps only large models; zero-shot beat few-shot in ConQRet. [c07, c04]
- Domain: Q&A agreement is higher than debate agreement; sarcasm and irony drive disagreement. [a17]
- Perspective: expert, crowd and novice groups differ; mixing groups lowers alpha (cogency .372 expert, .230 crowd, about .1 novice, .083 mixed). [b14]
- Labels reward length. [a16]
- Skew lowers kappa for rare violations (relevance, acceptability). [a06]
- LOGICOM: relative figures ("41% and 69% more likely") do not follow from the raw numbers; quote raw numbers per analysis. [critique 3]

**Interventions that worked (small, mostly 7B or older models).** CASA objections (+6.6 macro-F1); LLM-made context for a scorer (+.076 Spearman); retrieval-metric prompting (+.21 alpha); CQoT (+4.6 and +5.4% judge score); STICK checklists; factored verification; resampling for factual claims. All were measured on proxies (agreement, judge scores, factual precision). None was measured on ARS-checked end-task accuracy at equal tokens.

**Interventions that did not work.** Generating a conclusion to test sufficiency (adds nothing, F1 .532); asking the model for its own critical questions (below 57% useful); chain-of-thought before verdict (lower agreement in Ocampo; PaLM 2 .97 to .63); few-shot for medium models; generic self-correction.

**Unresolved.** The 2017 essay result (sufficiency easy) and the 2017 debate result (sufficiency hard) differ by domain, scale (2 vs 3 levels) and label skew; CASA's .14 shows the easy number is inflated. [critique]

## 6. Language models

**As judges of ARS (agreement with humans).**
- Older models, pointwise: GPT-3.5 and PaLM 2 rated 320 arguments on 15 dimensions. Self-agreement alpha .6 to .98; human agreement moderate; weakest on sufficiency; GPT-3.5 shows systematic disagreement with experts on sufficiency. [a20, a21, b07]
- GPT-4o listwise with self-consistency: alpha with experts .47 cogency, .57 local sufficiency, .53 global sufficiency, average .48. That is better than crowd (cogency .27, global sufficiency -.17). Self-consistency doubled GPT-3.5 average (.16 to .35). [a22]
- Pairwise logic quality, 12 open models, Webis-ArgQuality-20: best (Llama-70B few-shot) kappa .493, Pearson .474, 53.0% agreement, a thin margin over a majority rule (kappa .442, 48.3%). CoT often lowered agreement. [a24, c06, c07]
- Debate speeches: models above about 7B are better, Qwen-2.5-72B exceeds human-human kappa; models rate speeches lower than humans. [b17, c21]
- Position bias: small models prefer a side and rarely say tie; few-shot raised tie use to 62.97% for some. [b16]
- Run-to-run label change at most 7.75% (Ocampo); GPT-4o agreement 83 to 90% at temperature 0.3. [a24, c28]

**As arguers and subjects.**
- Frontier models defending moral verdicts (9 models, 6,778 cells): relevance failure under 0.5%; 18.2% of cells low on grounds; two models produced 67.8% of failures; hedging, not length, marks low grounds. Judges (Claude Sonnet 4.6 and GPT-5.4) agreed 89.6%. The judges overlap the subject models. [c09, c10, c11]
- Reasoning trace is defended better than the final justification in all 8 models. [c12]
- LOGICOM: GPT-3.5 17% vs 10% persuaded by fallacious vs logical arguments; GPT-4 56% vs 37% (A2); the stronger model is more susceptible. [c23]
- Fallacy naming: GPT-4 accuracy .79 (N=780), macro-F1 .71; the .90 figure excludes "None" outputs. [c24]

**As critics.**
- CASA (7B): +6.6 macro-F1 over zero-shot; revisions improved 58% vs 7% worse. [b04, b05]
- CQoT (5 frontier-class models of 2024): +4.61% and +5.4% judge score; smallest model did worse than CoT on reasoning. [d01]
- Critical-question generation: at most about 57% useful across 11 models. [d02]
- TICK/STICK: concrete checklist +7.8 on LiveBench reasoning for Command-R+, but only +0.8 for GPT-4o overall; Self-Refine hurt. [d10]
- Intrinsic self-correction hurts (GPT-3.5 CommonSenseQA 75.8 to 38.1). [d03]

**What changed performance.** Judge configuration (listwise, SC, order averaging), model size (above about 7B), retrieval metrics (alpha .184 to .395), concrete questions, factored probes. What did not: few-shot (mixed), CoT (negative in the ARS-adjacent studies).

**Caveat on model age.** Most ARS-judge data are 2023 to 2024 models. Only Henselmans (2026) and Ocampo (2026) use recent models, and Ocampo uses open weights. We have no 2026 frontier-model result on the hard sufficiency items.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep the Verify judge a different model family from the generator, swap option order, hide authorship and any proposed answer (extends G5). | G5 / S8 | [E] | d06, d07; K31 |
| A2 | Read judge self-agreement as nothing about validity; validate any judge against a gold set before use. | G4 / S8 | [E] | a20, c08, b16; K09 |
| A3 | Aggregate several independent judge samples for any sufficiency or cogency verdict in code (one rating is noisy). | G4, G5 / S8 | [E] | a12, a22, b11; K04, K08, K10 |
| A4 | Length-normalise: do not let longer or more fluent answers look more sufficient. | G5 / S8 | [E] | a16, a15; K07 |
| A5 | Do not use a generic "review your answer" as the Verify move without a baseline: it must beat a no-verify arm and a self-consistency arm. | G2, G7 / S8 | [E] | d03; K25 |
| A6 | Use a strong judge model (well above 7B) for any model-based Verify check. | S8 | [E] | b17, c22; K13 |
| A7 | Do not use written chain-of-thought as the verifier of an ARS verdict; keep verdict first, brief rationale (follows G10 and G11; ARS-specific evidence is from older or open models). | G10, G11 | [E] on direction | a24, a20, d04; K12, K30 |
| A8 | Do not rely on fallacy names; a defect list by A, R, S is enough. | S8 | [S] | c24, a03; K19 |
| A9 | Fixed ARS questions, not model-invented critical questions. | S8 / O | [E] on the 57% cap | c25, d02; K20, K28 |

### Test first (not established; see UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Verify with the ARS checklist (concrete yes/no items, A, R, S separate) vs a generic check, at equal tokens, on open answers. | S8 | [S] | K01, K24, K26; b27; d10 |
| T2 | Sufficiency-only probe (draft hidden, counterfactual objection, strongest-objection rebuttal) vs full triad. | S8 / O | [S] | K05, K15, K29; c09, b04, d09 |
| T3 | Global sufficiency item: name the strongest objection and say if the draft answers it. | S8 | [S] | a28, a09 |
| T4 | Resample agreement for acceptability of factual premises. | S8 | [S] | K33; d13 |
| T5 | Mark irrelevant retrieved passages before use, with 3 to 5 samples. | S1 / S8 | [S] | K32; d08, b12 |
| T6 | Single-example or anecdote flag as a cheap weak-support signal. | S8 | [S] | a07; K07 |
| T7 | Check the final justification against the reasoning trace (trace is defended better). | S8 | [S] | c12; K17 |
| T8 | Adversarial: feed fallacious support to Verify and measure acceptance. | G / S8 | [S] | c23; K18 |
| T9 | Verdict-first vs rationale-first for the ARS judge. | S8 | [S/C] | d04, d05, a24; K30 |
| T10 | Graded (weak/moderate/strong) and audience-named acceptability vs pass/fail. | S8 | [C] | d14, d16, a25; K34, K22 |
| T11 | Counterfactual-objection generation before judging sufficiency. | O | [S] | b13, b04; K14 |
| T12 | Hedge sensitivity of the judge (paired rewrites). | S8 | [S] | c11; K16 |

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup, probes and revisions). Blind judge: different family from the answerer, option order swapped, authorship hidden, length-normalised. Add a human-checked gold subset of at least 60 items for any judge validity claim.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 | Open questions with a reference or rubric (policy, ethics, "should we", causal explanations); 100 items | (a) no verify; (b) generic "check your answer" + revise; (c) 3-sample self-consistency (equal calls); (d) ARS checklist + revise | blind pairwise win rate and rubric score; accuracy where a key exists | (d) beats (b) by at least 5 win-rate points; (b) at or below (a) (d03) |
| E2 | Same items | ARS triad (3 calls) vs sufficiency-only probe (draft hidden) at equal tokens | win rate; defects found per 1,000 tokens | sufficiency-only equal or better, since relevance fails under 0.5% |
| E3 | Items with a known missing premise (premise-removal gold set built from answers; 60 items) | CASA-style objection vs plain "is this enough?" vs strongest-objection rebuttal | detection F1 on insufficiency, hard items only | objection beats plain by 5+ F1 |
| E4 | Answers with factual premises, closed-book | resample agreement (5 samples) vs single-pass "is this premise true?" | AUC for premise error | resampling above single pass; limited to inconsistent errors |
| E5 | Retrieved passages with 0, 1, 3 irrelevant or fallacious paragraphs (GSM-IC and LOGICOM style) | no filter vs relevance mark + drop vs ARS check | answer accuracy; acceptance rate of fallacious support | filter reduces accuracy drop; ARS check cuts fallacy acceptance |
| E6 | Judge validity | single pointwise vs listwise x3 orders vs verdict-first/rationale-first | agreement (alpha) with human gold, hard items only | listwise x3 above single; verdict-first not worse than CoT |
| E7 | Paired rewrites: same answer hedged vs plain; short vs long; fluent vs plain | judge scores | score gap | quantify hedge and length bias; drop the cue if the gap exceeds 0.3 SD |
| E8 | Same-family vs cross-family judge | win-rate difference | self-preference size | cross-family judge shows lower self-bias |

## 9. What does not transfer, and why

- **Agreement metrics are not outcome metrics.** Almost all numbers here score how well a rater matches humans on a corpus. They do not show that using the rating improves an answer. [b27]
- **Corpora are human arguments**: learner essays, debate comments, Q&A posts. Model answers differ: relevance failure is near zero, and hedging is the cue. [c09, c11]
- **Persuasion is not soundness.** UKPConvArg and IBM ArgQ rank convincingness or "would use in a speech", not ARS. [a13, a15]
- **Small and old models.** CASA used 7B models; most judge studies used GPT-3.5 and PaLM 2. Frontier behaviour is unmeasured on the hard items.
- **Crowd methods** (10 raters at $0.10) do not apply to one agent. The analogue is several samples, but samples from one model are correlated (G4).
- **Fallacy-naming results** (LOGICOM, Lim and Perrault) concern debate and labelled datasets. Naming is not evaluation. [c24]
- **Self-correction and CoT results** come from math or psychology-style tasks (d03, d04, d05). They show the direction of risk, not an ARS result.
- **Perspective dependence.** Quality ratings vary by rater group. With a single agent we must fix an audience in the prompt rather than pool. [b14]
- **Conductive and defeasible arguments.** Sufficiency has no formal test; a checklist cannot decide it, only surface what is missing. [d16, a03]
- **Henselmans (2026)**: moral questions only, and the judges are LLMs that overlap the subjects; self-preference is possible.

## 10. Open questions

1. Does an ARS-checklist Verify step improve end-task answer quality at equal tokens against a generic check? (No study.)
2. Which ARS move does the work: relevance, acceptability or sufficiency? Is a sufficiency probe alone as good as the triad?
3. Does CASA-style objection still help on frontier models and on whole answers rather than short fallacy items?
4. Frontier-model sufficiency judge agreement with humans on hard items (the .14 regime); do 3 to 5 samples fix it?
5. Can acceptability of premises be judged closed-book, and how much does retrieval add?
6. Does CoT before the verdict hurt ARS judging on 2026 frontier models?
7. Are ARS judges biased toward own-family, fluent or hedged answers? Is hedging a real defect or a judge cue?
8. What do Johnson and Blair and Govier say about limits (conductive arguments, audience-relative acceptability) that a prompt should encode? The books are unread.
9. Checklist vs probability strength (Hahn and Oaksford) for calibrated confidence: no LLM study.
10. Are models persuaded by fallacious supporting text inside the agent's own retrieved context, and does an ARS check cut it?
11. Is the claim "annotator information reported for only 8 datasets" true? Unverified (critique 2).

## 11. Sources

[V] = opened (per the evidence files); [M] = snippet or second-hand only.

- [V] Stab and Gurevych (2017) Recognizing insufficiently supported arguments in argumentative essays. https://aclanthology.org/E17-1092.pdf (a05 to a07, b01, b02, c17)
- [V] Wachsmuth et al. (2017) Computational argumentation quality assessment in natural language. https://aclanthology.org/E17-1017.pdf (a08 to a10, a28)
- [V] Wachsmuth et al. (2017) Argumentation quality assessment: theory vs. practice. https://aclanthology.org/P17-2039.pdf (a11, a12, c18)
- [V] Habernal and Gurevych (2016) Which argument is more convincing? https://aclanthology.org/P16-1150.pdf (a13)
- [V] Gretz et al. (2020) IBM-ArgQ-Rank-30kArgs. https://arxiv.org/abs/1911.11408 (a14)
- [V] Toledo et al. (2019) Automatic argument quality assessment. https://aclanthology.org/D19-1564.pdf (a15)
- [V] Wachsmuth and Werner (2020) Intrinsic quality assessment of arguments. https://arxiv.org/abs/2010.12473 (a16)
- [V] Lauscher et al. (2020) Rhetoric, logic and dialectic. https://aclanthology.org/2020.coling-main.402.pdf (a17)
- [V] Gurcke, Alshomary, Wachsmuth (2021) Assessing the sufficiency of arguments through conclusion generation. https://arxiv.org/pdf/2110.13495 (a18, b03, c16)
- [V] Wachsmuth et al. (2024) Argument quality assessment in the age of instruction-following LLMs. https://arxiv.org/abs/2403.16084 (a19, c19)
- [M] Same paper, LREC-COLING page. https://preview.aclanthology.org/setup/2024.lrec-main.135 (b24)
- [V] Mirzakhmedova et al. (2024) Are LLMs reliable argument quality annotators? https://arxiv.org/abs/2404.09696 (a20, a21, b07 to b09, c01, c02)
- [V] Dhole, Shu, Agichtein (2024) ConQRet. https://arxiv.org/abs/2412.05206 (a22, a23, b10 to b12, c03 to c05)
- [V] Ocampo, Nyiranziza, Ceolin (2026) Pairwise Bradley-Terry argument quality. https://arxiv.org/abs/2605.28313 (a24, b15, b16, c06 to c08)
- [V] Liu, Feng, Chang (2024) CASA. https://arxiv.org/abs/2401.05249 (b04 to b06, c14, c15)
- [V] Deshpande et al. (2023/2024) Contextualizing argument quality assessment with LLMs. https://arxiv.org/abs/2305.12280 (b13, c13)
- [V] Romberg et al. (2025) Towards a perspectivist turn in argument quality assessment. https://arxiv.org/abs/2502.14501 (b14, c20)
- [V] Sternlicht et al. (2025) Debatable intelligence. https://arxiv.org/abs/2506.05062 (b17, c21, c22)
- [V] Svedholm-Hakkinen, Hietanen, Baron (2024) Individual differences in argument evaluation. https://link.springer.com/10.1007/s10503-023-09620-x (b18 to b20)
- [V] Henselmans, Prinzhorn, Libert (2026) Measuring AI accountability through argument quality. https://arxiv.org/abs/2609.05088 (c09 to c12)
- [V] Payandeh et al. (2024) How susceptible are LLMs to logical fallacies (LOGICOM). https://arxiv.org/abs/2308.09853 (c23)
- [V] Lim and Perrault (2024) LLM in identifying logical fallacies. https://arxiv.org/abs/2404.05213 (c24)
- [V] Calvo Figueras and Agerri (2025) Benchmarking critical questions generation. https://arxiv.org/abs/2505.11341 and https://arxiv.org/html/2505.11341v3 (c25, d02)
- [M] Calvo Figueras and Agerri (2024) Critical questions generation. https://arxiv.org/abs/2410.14335 (c26, abstract only)
- [V] Al Rebdawi and Alhamzeh (2025) Argument quality annotation and gender bias. https://arxiv.org/abs/2508.08262 (c28)
- [V] Hahn and Oaksford (2007) The rationality of informal argumentation. https://pdf.stafforini.com/hahn-2007-rationality-informal-argumentation.pdf (a25, a26; b23 not retrieved)
- [V] Stanford Encyclopedia of Philosophy: Informal Logic, Fallacies, Argument and Argumentation. https://plato.stanford.edu/entries/logic-informal/ , https://plato.stanford.edu/entries/fallacies/ , https://plato.stanford.edu/entries/argument/ (a01 to a03, d14 to d16)
- [V] Castagna, Sassoon, Parsons (2024) Critical-Questions-of-Thought. https://arxiv.org/abs/2412.15177 (d01)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d03)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (d04)
- [V] Liu et al. (2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 (d05)
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076 (d06)
- [V] Ye et al. (2025) Justice or prejudice? (CALM). https://arxiv.org/abs/2410.02736 (d07)
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (d08)
- [V] Dhuliawala et al. (2024) Chain-of-Verification. https://arxiv.org/abs/2309.11495 (d09)
- [V] Cook et al. (2024) TICKing all the boxes. https://arxiv.org/abs/2410.03608 (d10, d11)
- [V] Xiong et al. (2024) Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d12)
- [V] Manakul, Liusie, Gales (2023) SelfCheckGPT. https://arxiv.org/abs/2303.08896 (d13)
- [M] Johnson and Blair (2006) Logical Self-Defense; Govier (2010) A Practical Study of Argument; https://philarchive.org/archive/GOVPIA (a04, b21, c27; not opened)
- [M] Hoffmann and Catrambone (2023) criteria for objectively bad arguments. https://releve.erudit.org/fr/revues/informallogic/2023-v43-n1-informallogic07982/1099208ar.pdf (b22)
- [M] Boudry, Paglieri, Pigliucci (2015), second-hand via https://aclanthology.org/P17-2039.pdf (a27)
