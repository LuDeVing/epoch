# Debiasing and cognitive forcing: deep document

*Subfield E01.06. Sources: evidence_a-d.jsonl (ids a01-a25, b01-b28, c01-c28, d01-d18), claims.jsonl (K01-K33), critique.md. Numbers were cross-checked where the critique says so. Items marked "not opened" are leads, not facts.*

## 1. What it is

Debiasing is any step meant to stop a known thinking error from reaching the final answer. In medicine the target errors are anchoring, premature closure, availability, search satisficing, confirmation and framing. Cognitive forcing is one family of debiasing. A forcing strategy is a rule that makes the thinker stop at a set point and do a set thing. "Have I considered a second diagnosis?" is a forcing rule. A checklist is a written forcing rule.

Our question is narrow. Can a scaffold step of this kind raise the accuracy of one language-model agent, at equal tokens, against a plain model? Guardrails G1 (doubt only on a signal) and G7 (every element must pay for itself) and section 4b of the schema ("slow down", bias checklists, self-reflection are not to be added) already lean on this subfield. This document checks that lean and finds where it is too strong.

Short answer from the evidence:

- Generic "slow down" and "be aware of bias" steps do not help people. This is established.
- Content-based steps (a list of alternatives built from the case, a key-variable list at verify time, knowledge of how look-alike diseases differ) sometimes help. This is contested or single-source.
- LLMs are hurt by injected bias. Warnings recover only a small part. Self-review without outside feedback lowers accuracy.
- The strongest positive signals are not "debias" but "trigger a check on a signal" and "commit before reading advice". Both are single-source for LLMs.

## 2. History and theories in depth

**Dual-process base.** The theory behind debiasing is that fast intuitive thinking (System 1) produces biased answers and slow analytic thinking (System 2) can catch them. The dual-process subfield (E01.04) covers this. This subfield only tests the remedy.

**Croskerry 2003 (a01).** Croskerry proposed cognitive forcing strategies (CFS) in Annals of Emergency Medicine. Three levels: universal (be aware of how you think), generic (for example a differential list) and specific (one counter-move per named pitfall). It relies on metacognition: the clinician learns to notice a trigger situation and force a different move. It is a proposal with no data. The abstract claims it can inoculate trainees.

**Ely, Graber, Croskerry 2011 (a02, b06).** Proposed three checklists: a general cognitive-approach checklist, a differential-diagnosis checklist, and a pitfall list per disease. The authors say these were built informally and never rigorously tested.

**Croskerry, Singhal, Mamede 2013 (b04, b05).** Two review papers. Part 1 says evidence that bias causes real diagnostic error is scarce and borrowed from other domains. Part 2 lists debiasing tools with evidence tags. It states that CFS showed "minor effects", that consider-the-opposite marginally reduced anchoring, that checklist support comes mostly from surgery and ICU, and that for stopping rules no published example exists. So the founder's own later review is cautious.

**Graber 2012 (a07).** Narrative review of 141 articles. 42 tested an intervention, 100 only suggested one. Three classes: knowledge and experience, reasoning skills, cognitive help (decision support, second opinion). Tests were mostly on trainees in artificial settings.

**The Norman-Sherbino line (a03-a06).** A Hamilton group tested the claim directly. Their view (Norman 2017) is that errors come mostly from knowledge gaps, not from fast thinking, and that case difficulty drives error more than thinking style. This is the competing explanation to Croskerry.

**The Mamede line (a10, b14-b16, b13).** A Rotterdam group developed "deliberate reflection": the clinician lists features for and against the leading diagnosis and for alternatives. They found it helps on hard cases. Their later work (2020) moved from process to knowledge: teach how look-alike diseases differ, and the availability bias is blunted.

**The Sibbald line (a11, a12, b07, b08).** A checklist helps when it is used at the verify step after commitment and carries content (key ECG variables). A generic debiasing checklist does not.

**Human-AI advice (b26, a21-a25).** Bucinca 2021 moved the idea to AI advice: forcing the person to think before seeing the AI cuts overreliance. This is the closest human result to an agent that reads a tool or critic output.

**LLM period (2023-2026).** Three strands. (1) LLMs show human-like bias when it is injected (BiasMedQA, BiasBuster). (2) LLMs cannot self-correct without outside feedback (Huang 2023). (3) 2026 work on premature closure and information-seeking shows the LLM failure is often self-generated, not injected. Competing view: debate and role agents (Ke 2024, Catfish) cut bias, but matched-cost reviews (d01-d03) say the gain is mostly extra sampling.

## 3. Core findings with exact numbers

Status: E = established (2+ independent sources), S = single source, C = contested. "Source" gives evidence ids.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Telling residents to be reflective, not fast, did not raise accuracy | 44.5% fast vs 45.0% reflective; 69 s vs 89 s per case; wrong cases took 17 s longer; n=96 and 108 | Norman 2014 (a05, b02) | E (K01) |
| CFS teaching did not cut errors in novices | n=191 (145 vs 46); searched for second diagnosis 52% vs 48% (p=0.91); uncommon diagnosis 45% vs 45% (p=0.98); false-positive 64% vs 77% (p=0.12) | Sherbino 2014 (a04, b01) | S (K02); novices, 6 cases |
| Generic bias checklist does not beat control | ECG, n=61, 20 ECGs, no checklist beat control; Shimizu n=188, no gain from general debiasing list; clinic workshop preceptor agreement 74% vs 78% (p=0.64) | a11, b08, a09, b10 | E (K03) |
| Content checklist at verify step corrects more errors | 0.27 vs 0.04 corrected per ECG (n=16); 0.29 vs 0.03 (n=15); same lab | Sibbald 2013, 2015 (a12, b07) | S (K05) |
| Knowledge checklist was null in a later test | Sibbald 2019: neither checklist beat control | a11, b08 | C (K04) |
| Mnemonic checklist helped only the first half of the test | first 5 cases 9.15 vs 8.18 of 15 (p=0.008); last 5 9.58 vs 9.81; total p=0.159; n=88 | Chew 2017 (a13) | C |
| Differential checklist raised hard-case scores, lowered easy-case scores | 8.25 vs 8.77 (p=0.01) and 7.21 vs 7.96 (p=0.001) as re-checked; n=188 | Shimizu 2013 (a09) | E (K12) |
| Meta-analysis of workplace reasoning tools: small gain | 29 studies, 2732 people; g=0.20 (0.10-0.29), I2=38% after removing 3 studies that trained people first; g=0.28 (0.14-0.43), I2=70% with them; real or simulated patients 0.41; only 2 patient-based studies; 1 preregistered | Staal 2022 (b17) | E (K06) |
| Systematic review: guided reflection most consistent, but heterogeneous | 28 studies, no pooled effect | Lambe 2016 (a08) | E |
| Reflection helps residents on complex cases, not simple | student replication n=186 no gain on strict scoring (0.47 control vs 0.42, 0.41); dermatology n=61 gain 49.7 vs 38.4 (p=0.002) | a10, b11, b12, b16 | C (K07) |
| Reflection hurts at once, helps a week later | immediate 0.48 vs 0.62; delayed 0.66 vs 0.48; n=46 | Mamede 2012 (b14) | S (K08) |
| Knowledge of look-alike differences blocks induced availability bias | 0.40 vs 0.24, diff 0.16 (0.05-0.27), p=0.004; unbiased cases 0.36 vs 0.41, p=0.45; n=91 | Mamede 2020 (b13) | S (K09) |
| Little proof that debiasing cuts real error | reviews: evidence scarce, borrowed; workshop null | b04, b19, b20, a07 | E (K10) |
| Web debiasing course in mental health | n=137, 4 vignettes, p<.001 | Jenkins 2016 (b09) | S (K11) |
| Injected bias lowers every LLM tested | BiasMedQA 1,273 USMLE items, 6 models; GPT-4 72.7% clean, 14.0% relative worst-case drop (false consensus); GPT-3.5 49.7%, 37.4% mean relative drop; GPT-4 admits 40.5% more under reject framing | c01, c02, c04, a15, a16 | E (K13) |
| Bias warnings give small, model-dependent gains | +3.5 to +6.5 points across BiasMedQA models; GPT-4 frequency bias 0.627 to 0.720; none for PMC-Llama | c03, c05, b21 | E (K14) |
| Example prompts confuse the measure | GPT-4 clean accuracy rose 0.727 to 0.757-0.763 with examples; in BiasBuster contrastive and few-shot made models answer always yes or always no | c17, c05 | E (K15) |
| Self-help (model rewrites the biased prompt) best in BiasBuster | GPT-4 framing gap -0.405 baseline to -0.010; GPT-3.5 group attribution cut only 8.9% | a16, c04 | S |
| Clinical reasoning-style prompts do not beat CoT | GPT-4 MedQA: CoT 76%, differential 78% (p=0.24), analytic 78%, Bayesian 72% (p=0.07); GPT-3.5 differential 38% vs 46% (p<0.001) | Savage 2024 (a18, c15) | S (K16) |
| Self-review without feedback does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1 after one round; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle stop GPT-3.5 GSM8K 75.9 to 84.3, GPT-4 95.5 to 97.5 | Huang 2023 (c14, c28) | E (K17) |
| Reasoning model less biased, not bias-free | o1: no measurable bias in 7 of 10 vignette pairs; hindsight 52% vs 85% (GPT-4); post hoc 17% vs 56%; Occam's razor 100% vs 0% | Degany 2025 (a17, b24) | S (K18) |
| LLMs fail to see missing information | MetaMedQA 1,373 items: unknown recall 0% in 9 of 12 models; false action ~70% with correct option removed (~48% with safety prompt); >55% of answers committed in first two turns; utilisation 57% to 26% in last round | a19, c09, c10, c12, c13 | E (K19); mostly 2026 preprints |
| A hard completeness gate alone hurt | 38.0% to 32.7%; gate plus 5 samples plus entropy check 49.3% (N=150, one 70B model) | Srivastava 2026 (c11) | C (K20) |
| Deferring the question raised first-commit accuracy | up to 62.6%; wrong-to-right revisions up to 10.6x right-to-wrong | Fang 2026 (c10, c21) | S (K21) |
| Role agents fix biased misdiagnoses | 0/80 to 61/80 (76%) top-2; 16 cases x 5 runs; cases chosen because first answer was wrong | Ke 2024 (a20, b22, c07) | C (K22) |
| Debate rarely beats self-consistency at matched cost | MedQA: Medprompt 0.65, debate 0.64, SC 0.60, single 0.60; debate beat CoT in about 15% of 36 configurations; mixing model families helped | d01-d03 | E (K27) |
| Signal-triggered reflection beats always-on | MATH-500 Qwen3-8B: plain reflect toxic 4.2% vs effective 5.2%; triggered net +3.7 vs +1.0; 65.2 vs 60.8 budget-matched SC | Hao 2026 (d06) | S (K28) |
| Process helps hard items, hurts easy ones in LLMs | sequential revision lowered accuracy on PubMedQA; o1-like models used up to 1,953% more tokens on "2+3" | d05, d11 | C (K29) |
| Bias is partly self-generated | GPT-4 on real oncology notes: 23.1% error (validation set), 85.4% of errors reasoning failures, confirmation and anchoring most common | Kenaston 2025 (d07) | S (K30) |
| Commit-before-advice cuts overreliance in people | n=199, 6 conditions; forcing beat simple explanation; liked less; overreliance not removed | Bucinca 2021 (b26) | S (K23) |
| Pre-answer rebuttal flips LLMs more | 61.75% vs 56.52% (p<0.001); regressive flips 14.66% | SycEval (d09) | C (K31) |
| Physician plus GPT-4 did not beat physician alone | 76% vs 74%, diff 2 (-4 to 8), p=.60, n=50; GPT-4 alone 16 points higher | Goh 2024 (a21) | S (K24) |
| Time per case marks difficulty, not care | wrong cases 17 s longer | a05, b02 | S (K25) |
| Memorable errors blamed on anchoring, premature closure | 60.0%, 58.5%, availability 46.2%; n=130 | Japan survey (a14) | S (K26) |

## 4. Mechanisms and models

Each mechanism is written as something code could do.

**M1. Why generic debiasing fails (human account).** Bias is mostly unconscious, so a person cannot reliably notice it when told to. Extra time goes to the same reasoning that produced the first answer. In Norman's data the extra 20 s of reflective instruction did nothing, and wrong cases already took longer. Mechanism: the second pass reuses the same knowledge. If knowledge is missing, a second pass cannot add it (Norman 2017; m1 and Oh 2025 say the same for LLMs, d11, d12).

**M2. Why content-based steps can work.** A step that supplies new information (an alternatives list, a key-variable list, the contrast between look-alikes) changes what the second pass can see. Sibbald's checklist made residents fixate more of the ECG (fixations 88 vs 52). Mamede 2020 raised knowledge of discriminating features. Implementable form: code builds from the case a list of confusable candidates and the features that separate each pair; the model fills one line per pair.

**M3. Commit then verify.** The checklist helped at the verify step, after a commitment, not before. Implement: S3/S4 produce and commit an answer; S8 runs a separate pass with a code-built list; log corrected and introduced errors separately. This matches G2 (revise from real output) if the list points at checkable facts.

**M4. Signal-triggered check.** Plain reflection fixes about as many answers as it breaks (5.2% vs 4.2%). Trigger it only when sampled answers disagree or entropy is high (REGAR: 3.7% net, 65.2 vs 60.8 at matched tokens). Implement: draw k short samples, compute disagreement in code, run the check only if disagreement exceeds a threshold. This is G1 made operational.

**M5. Difficulty routing.** Process steps help hard items and hurt easy ones (Shimizu, Mamede, PubMedQA revision). Implement: S0 estimates difficulty (class pass rate, sample disagreement, trace length); alternatives and reflection steps run only above the threshold.

**M6. Input hygiene.** BiasMedQA and BiasBuster biases are injected sentences (stated guess, false consensus, framing, anchor). Code can strip or move them (S1 hygiene), which removes the bias instead of asking the model to resist it. The strip itself is untested in these sources; the damage figures are the reason to try it.

**M7. Commit-before-advice.** Record the agent's own answer before it reads any critic or tool output. Bucinca 2021 and Yan 2026 (summary only) support this for people. SycEval shows LLMs flip more with a pre-answer rebuttal. Implement: freeze the answer; only then show critic text; count right-to-wrong flips.

**M8. Premature closure in LLMs.** Models commit early, treat more relevant facts as a sign of decidability, and almost never say "none of the above" (c09-c13, a19). Implement: a code completeness check on required evidence fields before S7; defer the answer slot until fields are filled (K21). Caution: the gate alone lowered accuracy (c11); it paid only with samples and disagreement.

**M9. Deferred answer slot.** Withhold the diagnostic question until evidence is collected (Fang 2026: up to +62.6% first-commit accuracy). For multi-step items only.

**M10. Heterogeneous voters.** Matched-cost reviews find that mixing model families is the one debate lever that works (d03). Fits G4: same-model samples are correlated.

## 5. What holds up

**Held up (established).**

- Generic slow-down or reflect instructions: null on accuracy, positive on time cost. Norman 2014 plus reviews (K01).
- Generic debiasing checklists: null in ECG (n=61), in Shimizu (n=188), in a clinic workshop (K03).
- Small pooled gain from any reasoning tool, g=0.20 (K06). Too small to expect to see on a single bench.
- Evidence for real-practice error reduction: none that is clean (K10).
- LLMs lose accuracy under injected bias, in every model tested (K13).
- Bias warnings recover only part of it, unevenly by model (K14).
- LLM self-review without outside feedback does not help (K17).
- Debate and roles do not reliably beat sampling at matched cost (K27).

**Failed or weak.**

- CFS teaching: the 2011 pilot was not opened; the 2014 trial was null. One lab, novices, 6 cases. It does not prove CFS cannot work for experts.
- Mnemonic checklist (Chew): first half only, post hoc split.
- Reflection replication with students: null on strict scoring.
- Hard completeness gate alone (c11): -5.3 points.
- Reasoning styles as prompts (differential, Bayesian): no gain over CoT; worse for GPT-3.5.
- Few-shot and contrastive debias examples in BiasBuster: models answered always yes or always no.

**Moderators.**

- Case difficulty: process helps hard, hurts easy (K12, K29).
- Expertise: residents benefit from reflection, novices unclear.
- Content versus process: content checklists beat bias lists, unevenly (K04).
- Scoring rule: strict scoring erased the reflection gain.
- Timing: checks work at the verify step, not before; reflection hurts now and helps later (b14).
- Individual: forcing helps people high in Need for Cognition most (b26).
- Model: warnings help GPT-4, not small or medical models; example prompts change clean accuracy.

**Interventions that worked.** Knowledge of look-alike differences (Mamede 2020); verify-time key-variable checklist (Sibbald); guided reflection on complex cases; commit-before-AI (Bucinca); self-help prompt rewriting in BiasBuster; signal-triggered reflection (math); deferred question (staged evidence); mixed-model debate.

**Interventions that did not.** Be-aware warnings for humans; generic checklists; CFS teaching in novices; always-on self-review; role debate at matched cost; hard gate alone; AI-literacy training (73.3% vs 84.9% control, n=44, not opened); giving physicians GPT-4 (K24).

**Weak spots in the evidence base.** Almost all human data are vignette or exam tasks with students and residents. The Staal review found 2 patient-based studies. LLM bias studies inject a sentence; they do not test Croskerry's mechanism. Ke 2024 starts every case at 0% by selection and has an effective n of 16. Most 2026 papers are single-source preprints that the cross-checker did not re-open.

## 6. Language models

**Baseline damage.** BiasMedQA: GPT-4 drops 14.0% relative in the worst case (false consensus) and 0.2% under confirmation bias; GPT-3.5 loses 37.4% on average; cross-model bias means 24.9, 18.2, 12.9, 8.1 (the per-model figures in a15 were corrected in the critique). BiasBuster: GPT-4 admits 40.5% more students under the reject framing. Anchoring: GPT-4 and 4o are anchored by fake expert hints on 62 forecasting questions, and CoT, ignore-the-hint and reflection all failed (c06).

**What changed it.**

| Intervention | Effect | Note |
|---|---|---|
| Bias education or awareness prompt | +3.5 to +6.5 points (BiasMedQA); small in BiasBuster | none for PMC-Llama; GPT-4 best |
| Few-shot or contrastive examples | confounded; models over-answer yes or no | clean accuracy shifts by about 3 points |
| Self-help (rewrite prompt) | GPT-4 framing gap -0.405 to -0.010 | input rewrite, not answer review |
| CoT, ignore the hint, reflection (anchoring) | no removal of effect | non-medical |
| Reasoning-style prompts | no gain over CoT | GPT-3.5 worse |
| Unprompted self-review | worse (CSQA 75.8 to 38.1) | external or oracle signal needed |
| Role agents (Ke) | 0/80 to 61/80 top-2 | selected-failure design, no matched control |
| Dissent agent (Catfish) | +12.7 points on medical QA; silent agreement 61-89% to 11-17% | beats frameworks, not a plain prompt |
| Matched-cost debate | roughly equal to SC | model mixing helps (d03) |
| Safety or stop prompt | false action ~70% to ~48% | still high |
| Hard gate alone | -5.3 points | with 5 samples plus entropy +11.3 (c11) |
| Deferred question | up to +62.6% first-commit accuracy | staged-evidence tasks |
| Entropy-triggered reflection | 65.2 vs 60.8 SC at matched tokens | math only |
| Reasoning model (o1, R1) | less bias; not zero | Occam's razor 100% biased; R1 93% on 100 MedQA with anchoring errors |

**Self-generated failure.** On real oncology notes GPT-4 erred on 23.1% (validation), 85.4% of those reasoning failures, with confirmation and anchoring most common (d07). Frontier models rarely say "none of the above" and commit in the first two turns in over 55% of cases. This is the LLM version of Croskerry's pitfalls, and no debiasing step has been tested on it.

**Reasoning traces.** In 32 models, 91% of traces scored above threshold, yet trace quality was decorrelated from accuracy (c13). Thinking models rationalised expert-labelled wrong hints (d10). This supports G10.

**Token economics.** Parallel samples beat a larger token budget for short-reasoning 7B medical models (d11). Test-time scaling peaks near 4K tokens, and "Wait" forcing adds little without knowledge (d12). Nothing found compares forced extra thinking against a bias warning at equal tokens.

## 7. What our agent should take

### Add now (established)

Mostly these confirm and sharpen the existing schema. None adds a new state.

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Keep "slow down, be careful, reflect" out of the schema | 4b, G1 | [E] | a05, b02, b20, a10 (K01) |
| Keep generic bias-checklist or "list common biases" steps out | 4b, G7 | [E] | a11, b08, a09, b10, b18 (K03) |
| Do not credit any debiasing step with real-world gain; require a measured gain on our own items | G7 | [E] | b04, b17, b19 (K06, K10) |
| Unprompted self-review stays excluded; revise only from located failing output | G1, G2 | [E] | c14, c28, d04, d06 (K17) |
| Debate and role agents stay excluded unless they win against sampling at matched tokens | G9, G4 | [E] | d01-d03 (K27) |
| Run bias-injected versions of our items on the plain agent as a baseline damage figure (a measurement, not a feature) | G10, logging | [E] that damage exists | c01, c02, a16 (K13) |
| Always report clean accuracy of each mitigation arm | G7 | [E] | c17, c05 (K15) |
| Extra process on easy items is waste or harm; route by S0 difficulty | G12 | [E] human, [C] LLM | a09, a10, d05, d11 (K12, K29) |
| A code completeness check may be used as an S4 signal only paired with sample disagreement, never alone | S4, G1 | [C] | c11 (K20) |

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Code-built "alternatives and discriminating features" list at S8 verify | O1/S8, memory | [C]/[S] | a12, b07, b13, a11, a13 (K04, K05, K09) |
| Signal-triggered check (fire on sample disagreement) vs scheduled | S8, G1, G12 | [S] | d06, d04, d15 (K28) |
| Commit before reading critic or tool output | S1/S7, G2 | [S] | b26, a23, d09, d10 (K23, K31) |
| Input hygiene: strip stated guesses, authority claims, framing in S1 | S1 | [D] untested | c01, a16, c06 (K13, K14) |
| One-line bias warning vs plain at equal tokens | G1/G7 | [E] small gain, model-dependent | c03, c05, b21 (K14) |
| Defer the answer slot until evidence fields are complete | S0/S3 | [S] | c10, c21 (K21) |
| Gate plus samples plus entropy | S4/G5 | [S] | c11 (K20) |
| Trace length as difficulty signal | G12 | [S] | a05, d08, d11 (K25, K32) |
| Different-model second voter | G4 | [S] | d03 (K27) |
| Discriminating-feature memory vs extra thinking | memory/O7 | [S] | b13, d12 (K09, K32) |
| Structured category sheet built by code | O1/S4 | [S] | d14 (K33) |
| Lessons from solved items (reflect, store contrast) | memory | [S] | b14 (K08) |

## 8. Concrete tests on our bench

All arms use equal total tokens (the plain arm gets extra independent samples with code voting to fill the budget). Report clean accuracy, biased accuracy, tokens, and counts of wrong-to-right and right-to-wrong flips.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with an injected stated guess, authority claim or framing sentence (our task set, BiasMedQA style) | plain; plain plus k samples with vote; S1 hygiene strip; one-line warning | accuracy on biased items, drop vs clean | strip beats warning; warning +3 to +6 points; plain plus samples may match both |
| T2 | Mixed easy and hard items with known plain pass rate | alternatives step on all; alternatives step only on hard (S0 gate); plain plus samples | accuracy by difficulty bin; harm on easy items | harm on easy under "all"; routing wins |
| T3 | Items with a check | scheduled self-check on every item; check only when k samples disagree; plain plus samples | net fixes (fixed minus broken); accuracy | triggered net positive, scheduled about zero (REGAR: +3.7 vs +1.0) |
| T4 | Items with a planted wrong critic or tool note | advice first; commit first then advice | flip rate of correct answers; acceptance of wrong advice | commit-first lowers flips; size unknown |
| T5 | Multi-step evidence items with required fields | immediate answer; deferred answer slot; code completeness gate alone; gate plus samples | accuracy, first-commit rate | deferral helps; gate alone may hurt |
| T6 | Confusable-pair items | code-built discriminating-feature list at verify; bias warning; plain plus samples | accuracy on look-alike items; clean accuracy | list beats warning on biased items, no change on clean |
| T7 | Items where the right option is removed | plain; none-of-the-above prompt; completeness check | false action rate | prompt lowers ~70% to ~48%; check lowers further |
| T8 | Any items | trace-length logging | AUC of length for predicting error | above 0.55 means a usable difficulty signal |
| T9 | Hard items | same-model samples; second model family as voter | accuracy | heterogeneous voter wins (G4) |

## 9. What does not transfer, and why

- **Teaching.** Most human interventions are training (CFS course, workshop). A model is not trained by our scaffold; only what sits in the prompt or code at run time counts. Sherbino's null for teaching says little about run-time steps.
- **Unconscious bias.** Human debiasing is hard because bias is unconscious. An LLM's context is fully inspectable by code, so some biases (an injected guess) can be removed by code, which people cannot do.
- **Time cost.** Slow-down costs minutes for people and a few tokens for a model. The measured null still holds, but the cost argument does not.
- **Real-practice outcomes.** Human error rates in clinic have no analogue on our bench.
- **Need for Cognition, liking, trust** (Bucinca): not relevant to an agent.
- **Physician plus LLM trials** (Goh, Qazi): test human-AI teaming, not agent internals.
- **Mental-health vignette course** (K11): different field, vignette only.
- **BiasMedQA and BiasBuster**: injected-sentence tests; they do not test self-generated premature closure.
- **7B medical model findings** (d11, d12): our agent uses stronger models.
- **Self-report survey** (a14): hindsight labels; it may pick targets, not remedies.

## 10. Open questions

1. At equal tokens, does a bias warning, alternatives list or devil's advocate pass beat extra samples with code voting on bias-injected items? No source controls tokens.
2. Does a signal-triggered check beat a scheduled one on clinical or non-math items? One source, math.
3. Do forced alternatives help on hard LLM items and hurt on easy ones? No clinical study splits by difficulty.
4. What is the size of a code-built key-variable checklist for an LLM? Human data are n=15 and 16, one lab.
5. How much agent error is self-generated premature closure versus injected? No share-of-error estimate and no mitigation tested (Kenaston, d07).
6. Does commit-before-advice reduce acceptance of wrong critic output? Indirect support only (d09, d10).
7. Is the Ke 2024 gain from the roles or from five samples? Matched control not run.
8. Does knowledge-based immunisation work in LLM memory and beat a bias warning? Nothing found.
9. Do reasoning models make debiasing prompts unnecessary? A BiasMedQA reasoning preprint (d13) says they are not protected, but its numbers were not read.
10. Which of Croskerry's specific rules have any outcome test? Only Sherbino 2014's two bias types.
11. Do the 2026 premature-closure results (c09-c13) replicate? All are preprints not independently re-opened.

## 11. Sources

[V] opened (full text or relevant sections by the first agents or the cross-checker), [M] snippet or abstract only.

- [M] Croskerry 2003 CFS, https://europepmc.org/article/MED/12514691 (a01)
- [M] Ely, Graber, Croskerry 2011 checklists, https://europepmc.org/article/MED/21248608 (a02, b06)
- [M] Sherbino 2011 pilot, https://europepmc.org/article/MED/21240788 (a03; not opened by anyone)
- [M] Sherbino 2014 ineffectiveness of CFS, https://europepmc.org/article/MED/24423999 (a04, b01; abstract re-read by cross-checker)
- [M] Norman 2014 System 1 vs System 2, https://europepmc.org/article/MED/24362377 (a05, b02; abstract re-read)
- [M] Norman 2017 causes of errors, https://europepmc.org/article/MED/27782919 (a06, b03)
- [M] Graber 2012 interventions review, https://europepmc.org/article/MED/22543420 (a07)
- [M] Lambe 2016 dual-process review, https://europepmc.org/article/MED/26873253 (a08)
- [M] Shimizu 2013 checklist and debiasing, https://europepmc.org/article/MED/23228085 (a09; abstract re-read)
- [M] Mamede 2008 reflective practice, https://europepmc.org/article/MED/18412886 (a10)
- [M] Sibbald 2019 debiasing vs knowledge checklists, https://europepmc.org/article/MED/30694452 (a11, b08)
- [V] Sibbald 2015 verifying with a checklist, https://europepmc.org/article/PMC/PMC4564443 (a12)
- [M] Sibbald 2013 checklists improve experts, https://europepmc.org/article/MED/23398016 (b07)
- [V] Chew 2017 TWED checklist, https://europepmc.org/article/PMC/PMC5707798 (a13)
- [V] Japan physicians survey 2022, https://europepmc.org/article/PMC/PMC9032995 (a14)
- [V] Schmidgall 2024 BiasMedQA, https://pmc.ncbi.nlm.nih.gov/articles/PMC11494053/ and https://arxiv.org/abs/2402.08113 (a15, b21, c01-c03, c17)
- [V] Echterhoff 2024 BiasBuster, https://arxiv.org/abs/2403.00811 (a16, b25, c04, c05, c23)
- [V] Degany 2025 o1 vignettes, https://pmc.ncbi.nlm.nih.gov/articles/PMC12372181/ (a17, b24)
- [V] Savage 2024 diagnostic reasoning prompts, https://arxiv.org/abs/2308.06834 (a18, c15, c25)
- [V] Griot 2025 MetaMedQA, https://europepmc.org/article/PMC/PMC11733150 (a19)
- [V] Ke 2024 multi-agent bias, https://pmc.ncbi.nlm.nih.gov/articles/PMC11615553/ and https://arxiv.org/abs/2401.14589 (a20, b22, c07, c18)
- [V] Goh 2024 JAMA Netw Open RCT, https://europepmc.org/article/PMC/PMC11519755 (a21)
- [M] Qazi 2026 automation bias, https://europepmc.org/article/MED/42932681 (a22)
- [M] Yan 2026 independent judgment, https://europepmc.org/article/PMC/PMC13655004 and https://europepmc.org/article/MED/42865604 (a23, b27)
- [M] Tran 2026 AI Timeouts, https://europepmc.org/article/PMC/PMC13730618 and https://europepmc.org/article/MED/42979606 (a24, b28)
- [M] Pham 2026 hypothesis cues, https://europepmc.org/article/PMC/PMC13680241 (a25)
- [V] Croskerry, Singhal, Mamede 2013 parts 1 and 2, https://pmc.ncbi.nlm.nih.gov/articles/PMC3786658/ and https://pmc.ncbi.nlm.nih.gov/articles/PMC3786644/ (b04, b05)
- [M] Jenkins 2016 debiasing RCT, https://europepmc.org/article/MED/26727411 (b09)
- [M] Smith and Slack 2015, https://europepmc.org/article/MED/29540027 (b10)
- [V] Costa Filho 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6684533/ (b11)
- [V] Guided reflection in students 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC6265413/ (b12)
- [V] Mamede 2020 immunising, https://pmc.ncbi.nlm.nih.gov/articles/PMC7362774/ (b13)
- [M] Mamede 2012 reflection and learning, https://europepmc.org/article/MED/22515754 (b14)
- [M] Mamede 2012 salient distractors, https://europepmc.org/article/MED/22389021 (b15)
- [V] Mamede 2023 deliberate reflection, https://pmc.ncbi.nlm.nih.gov/articles/PMC10083910/ (b16)
- [V] Staal 2022 meta-analysis, https://pmc.ncbi.nlm.nih.gov/articles/PMC9685706/ (b17)
- [V] Checklist systematic review 2022, https://pmc.ncbi.nlm.nih.gov/articles/PMC9058772/ (b18)
- [V] Audit and communication review 2019, https://pmc.ncbi.nlm.nih.gov/articles/PMC6716834/ (b19)
- [V] Cognitive error in emergency medicine 2020, https://pmc.ncbi.nlm.nih.gov/articles/PMC7673867/ (b20)
- [M] Wang and Redelmeier 2024 NEJM AI, https://europepmc.org/article/MED/42932773 (b23)
- [V] Bucinca 2021 forcing functions, https://arxiv.org/abs/2102.09692 (b26)
- [V] Lou and Sun 2024 anchoring, https://arxiv.org/abs/2412.06593 (c06, c24)
- [V] Wang 2025 Catfish agent, https://arxiv.org/abs/2505.21503 (c08, c20)
- [V] Handler 2026 premature closure, https://arxiv.org/abs/2605.15000 (c09, c19, d16)
- [V] Fang 2026 MINT, https://arxiv.org/abs/2604.04325 (c10, c21)
- [V] Srivastava 2026 premature handoff, https://arxiv.org/abs/2606.18068 (c11, c22)
- [V] Watanabe 2026 factor coverage, https://arxiv.org/abs/2610.25819 (c12, c27)
- [V] Braitsch 2026 information seeking, https://arxiv.org/abs/2607.10275 (c13, c26)
- [V] Huang 2023 cannot self-correct, https://arxiv.org/abs/2310.01798 (c14, c28)
- [V] Alessa 2025 bias induction, https://arxiv.org/abs/2507.03194 (c16)
- [V] Smit 2024 MAD, https://arxiv.org/abs/2311.17371 (d01)
- [V] Wang 2024 multi-agent discussions, https://arxiv.org/abs/2402.18272 (d02)
- [V] Zhang 2025 stop overvaluing debate, https://arxiv.org/abs/2502.08788 (d03)
- [V] Kamoi 2024 self-correction survey, https://arxiv.org/abs/2406.01297 (d04)
- [V] Chen 2024 overthinking, https://arxiv.org/abs/2412.21187 (d05)
- [V] Hao 2026 REGAR, https://aclanthology.org/2026.findings-emnlp.805.pdf (d06)
- [V] Kenaston 2025 oncology notes, https://arxiv.org/abs/2511.20680 (d07)
- [V] DeepSeek R1 medical audit 2025, https://arxiv.org/abs/2504.00016 (d08)
- [V] Fanous 2025 SycEval, https://arxiv.org/abs/2502.08177 (d09)
- [V] Christophe 2026 overalignment, https://arxiv.org/abs/2601.18334 (d10)
- [V] Oh 2025 test-time scaling medical, https://arxiv.org/abs/2506.13102 (d11)
- [V] m1 2025, https://arxiv.org/abs/2504.00869 (d12)
- [M] BiasMedQA reasoning preprint 2025, https://www.medrxiv.org/content/10.1101/2025.06.22.25330078.full.pdf (d13; full text blocked)
- [M] Sonoda 2025 structured prompt, https://pubmed.ncbi.nlm.nih.gov/39625594/ (d14)
- [M] Reflective Confidence 2025, https://arxiv.org/abs/2512.18605 (d15)
- [M] MUSE 2026, https://arxiv.org/abs/2605.27288 (d17)
- [M] Economics of accuracy 2025, https://www.medrxiv.org/content/10.64898/2025.12.22.25342804.full.pdf (d18)

Links to parallel subfields (not covered here): cognitive bias and premature closure (E01.05), reflective reasoning and second look (E01.07), dual-process theory, pre-mortem, choice architecture and nudging, cognitive task analysis, self-correction and search subfields.
