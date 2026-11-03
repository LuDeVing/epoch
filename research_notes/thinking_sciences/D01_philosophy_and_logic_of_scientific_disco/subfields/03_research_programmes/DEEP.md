# Research programmes: deep document

*Subfield D01.03. Hard core, protective belt, progressive versus degenerating. Key work: Lakatos (1970/1978). Built from evidence_a-d.jsonl (a01-a31, b01-b26, c01-c25, d01-d16), claims.jsonl (K01-K30) and critique.md in this folder. Where evidence line b14 and claim K07 disagree on the Huang oracle numbers, K07 is right (see critique.md).*

## 1. What it is

Imre Lakatos (1970, "Falsification and the Methodology of Scientific Research Programmes") proposed that science should appraise a series of theories, not a single theory. Each series is a research programme. A programme has three parts.

- **Hard core.** A few statements that the programme holds fixed by decision. For Newton: three laws of mechanics plus the law of gravitation (4 statements, a01). The core is not proved. It is shielded by a rule.
- **Protective belt.** Auxiliary hypotheses and initial conditions. When a prediction fails, the failure is redirected onto the belt. The belt may be adjusted or replaced (a02).
- **Heuristics.** The negative heuristic says: do not aim modus tollens at the core. The positive heuristic is a partly articulated plan of ever more complex models (a03). The scientist follows the plan and mostly ignores early anomalies.

The appraisal rule (a04, a14):

- A series is **theoretically progressive** if each new theory has excess empirical content over the last (it predicts something new). This can be checked by logic at once.
- It is **empirically progressive** if some of that excess content is later confirmed. This can take an indefinite time.
- If either clause fails, the series is **degenerating**: theories are fabricated only to accommodate known facts.
- Degrees of ad hoc: ad hoc1 = no excess content; ad hoc2 = excess content but none corroborated; ad hoc3 = heuristically unmotivated.

The falsification rule (a05): T is falsified only when a rival T' exists that (1) has excess empirical content, (2) explains all of T's unrefuted earlier success, and (3) has some excess content corroborated. So elimination needs a rival.

Why it matters for our agent. A reasoning agent that fails a check will patch its attempt. Each patch is a belt move. The agent needs a signal for "this patching is not going anywhere": a degenerating signal that fires the impasse detector (S6) and tells the agent to stop patching, restart, change operator or accept the best attempt (G6). Lakatos supplies the concepts (core vs patches, excess content, accommodation vs prediction). He does not supply a threshold. The honest finding of this document: the philosophy gives the idea, the LLM literature gives the numbers, and no study joins the two.

## 2. History and theories in depth

**Roots.**
- Duhem (a25): hypotheses are tested in groups, so a failed prediction does not say where the error is. Quine extended this to holism. Lakatos rejects Duhem's appeal to "good sense" and simplicity as taste (a15) and replaces it with an explicit content test on the series of adjustments.
- Popper (a26): modifications are unscientific only if their sole purpose is to evade falsification. Lakatos calls his own view "sophisticated falsificationism" (a31).
- Kuhn (a24): normal science ignores or explains away anomalies; crisis comes from accumulation. Lakatos sits between Popper (one anomaly can suffice) and Kuhn: anomalies are tolerated while the belt is progressive.

**The case studies in Lakatos's text (opened, a06-a13).**
- Newton's sequence of models: fixed point sun with one planet; both orbit a common centre; several planets with no interplanetary force; mass balls; spinning balls; interplanetary forces; bulging planets (a03). Early changes were driven by the plan, not by anomalies.
- Halley's comet return was predicted and seen 72 years later (a06, a08). Mercury's perihelion anomaly sat for decades and became a refutation only when Einstein explained it (a09).
- Prout (1815): atomic weights are whole numbers. Anomalies were blamed on impure samples, so the programme attacked the observational theories. Stas declared it unfounded in 1860; Crookes proposed fractionation in 1886; isotopes resolved it about a century later (a11). Lakatos calls this a programme progressing in an ocean of anomalies. It is a rational reconstruction: Prout himself denied the anomalies.
- Bohr: progressive from 1913; ad hoc steps for spin and relativistic splitting (1924); replaced by wave mechanics, which predicted a new fact (Davisson-Germer) (a12). Lakatos concedes the timing was a coincidence. Nunan (1982) published an immanent critique of this case (a29, metadata only).
- Marxism as degenerating: four failed bold predictions and post-hoc patches (a07). A contested political judgement.
- Fitzgerald contraction is ad hoc2, not ad hoc1 (a14). Bohr-Kramers-Slater 1924 had excess content, but all its new predictions failed.

**Novelty.** The Balmer formula was known before Bohr. Lakatos still counts it as novel because Bohr's theory implied a different statement about energy-level differences (a13). Later work splits novelty into temporal, use- and theory-relative versions. Zahar: a fact is novel if no rival predicts it and it was either unknown or not what the core was built to explain (b02). Under Zahar, Mercury's perihelion counts as novel for Einstein. SEP: novelty is comparative; neither rivals nor conventional wisdom may have predicted it (a18, b02).

**Tolerance, and no stopping number.** Progress may be intermittent. Each step must increase content, but corroboration only has to appear now and then (a06). There is "no instant rationality" (a09). Budding programmes need lenient treatment. Kepler's ellipses were seen as crucial against Descartes about 100 years later. Copernicus's parallax was found in 1838, nearly 300 years after 1543 (b01). Lakatos also dropped his own early belief that programmes have a saturation point (a17). Result: the criterion has no threshold (K03).

**Appraisal is not advice.** It is rational to stay with a degenerating programme and try to make it progressive. What is irrational is to deny its poor record (a10). He wanted journals to decline papers that only absorb counter-evidence ad hoc, and funders to withhold money. Hacking reads the rule as advice to the historian, not to the working scientist (b11, K04).

**Reversals.** Urbach judged the environmentalist IQ programme degenerating. The Flynn effect (1987), about 13 years later, reversed that (a20, b04).

**Critics (K22).**
- Feyerabend: any development can claim intermittent progress, so the test is empty (the waiting objection, b08). Applied strictly, it condemns programmes that later recover. If only appraisal, it is close to "anything goes" (a19). Lakatos died in 1974 before replying (a27).
- Kuhn, Musgrave: rational reconstruction fits history to the theory (b05). Lakatos never showed that scientists switched when his criterion fired (he admitted this in 1968) (a21).
- Laudan: effectiveness = importance-weighted solved empirical problems minus anomalies and conceptual problems (a22). Problems are hard to individuate. Bird: accumulating false solutions counts as progress.
- Kuipers (b06): a refuted theory can still be progressive if it has more successes and fewer counter-examples. Vickers: novel predictions have been historically unreliable evidence.
- Pseudoscience (a23): Lakatos would label a non-progressive field pseudoscientific even when practitioners try to improve it. Thagard would not.

**Later uses.**
- Meehl (1990): shield the core with auxiliary changes only if the theory has a track record ("money in the bank") and the core has high verisimilitude (b12). Seen only in a secondary snippet. The primary PDF returned HTTP 403 (K23).
- String theory judged degenerative by Lakatos's test: facts known in advance, no new testable predictions, a multiverse added after a failed fit. Yet giving up and persisting can both be defended (b10).
- Branahl (2024, v3 2026): a third category, **stagnant**, for programmes with no empirical progress for benign outside reasons. Four criteria, all required: pure theorizing for too long; no rival progressing; benign epistemic limits; still of high value (b07, c22). Example: accelerators reach about 10^4 GeV vs GUT scale 10^15 GeV. Philosophy paper; no AI test.
- Applied labels in other fields: symbolic AI as degenerating (Dreyfus review, a28), human sociobiology (a30), soil-erosion modelling (b13). All three seen as metadata or abstract only.
- Denario (2025, d01, c23, c24): the only 2025-2026 AI-science paper found that invokes Lakatos. Essay level. It asks whether training data is a new hard core and whether a programme with no human-readable core can be progressive. No measurement.

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single-source; contested. Numbers were re-checked against PDF text in the critique pass unless noted.

### 3a. Philosophy of science

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Unit of appraisal is a series of theories: core + belt + heuristic | Newton core = 4 statements | Lakatos 1970 (a01-a03); SEP (a18) | established (K01) |
| Progress needs excess content AND some of it confirmed; accommodation only = degenerating | ad hoc1/2/3 defined | Lakatos (a04, a14) | established (K02) |
| No stop threshold; tolerance is open-ended | Prout 1815 to about 1911; Halley 72 yr; Copernicus parallax 1838 (about 295 yr after 1543) | a06, a09, a11, b01 | established (K03) |
| Verdicts are retrospective and have reversed | IQ verdict reversed about 13 yr later (Flynn 1987); Mercury tolerated for decades | a20, b03, b04 | established (K04) |
| Novelty is comparative and contested; needs a reference set | Balmer 3 levels (B0, B1, B2); Zahar use-novelty | a13, a18, b02 | established (K05) |
| A third label "stagnant" for no-check situations | 4 criteria | Branahl (b07, c22) | contested (K21) |
| Critics: rule is empty or unusable | none numeric | Feyerabend, Kuhn, Hacking, Laudan (a19, a21, a22, b05, b08) | established as a debate (K22) |
| Meehl: shield the core only with a track record | no numbers read | b12 (secondary) | single-source (K23) |

### 3b. LLM evidence on patching without a signal

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Intrinsic self-correction (no oracle) does not help and often hurts | GPT-3.5 CSQA 75.8 -> 38.1 (3 calls) -> 41.8 (5); GSM8K 75.9 -> 75.1 -> 74.7; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; GPT-4 HotpotQA 49 -> 49 -> 43 | Huang 2024 (b14, c01) | single-source (K06) |
| The oracle label, not the patching, produces the gains | GPT-3.5 GSM8K 75.9 -> 84.3, CSQA 75.8 -> 89.7, HotpotQA 26.0 -> 29.0; GPT-4 GSM8K 95.5 -> 97.5, CSQA 82.0 -> 85.5, HotpotQA 49 -> 59 | Huang Table 2 (K07; the b14 oracle row is wrong, c02 is the GPT-4 row) | single-source |
| Still true for reasoning models | o1-preview accuracy 4.2 points lower, 15.6% of correct overturned; o1-mini 12.1 lower, 34.0% overturned; 4o 20.4 lower, 58.8% overturned; 3.5-turbo 8.7 lower, 26.5% | Zhang 2025 (d02) | established with Huang and Kamoi (K08) |
| No successful intrinsic self-correction under fair settings | SCoRe (training): +15.6 pts MATH (Gemini 1.0 Pro), +9.1 HumanEval (1.5 Flash) | Kamoi 2024 (b18, c05); Kumar 2024 (b21) | established (K08) |
| Debate/extra rounds lose to sampling at equal calls | GSM8K GPT-3.5 self-consistency 82.5 (3), 85.3 (6), 88.2 (9) vs debate 83.2 (6), 83.0 (9) | Huang (b15, c04) | single-source (K10) |
| Self-repair of code is not clearly better than resampling; feedback is the bottleneck | GPT-4 own feedback 33.30% vs human 52.60% repair success (competition 3.67 vs 14.67); 16 participants, 40 programs | Olausson 2024 (b16, c08) | single-source (K09) |
| Self-verification unreliable; blind spot | Game of 24 verifier acc 87.0%, FP 10.4%, FN 20.7%; Blocksworld FN 97.09%; blind spot 64.5% over 14 models, "Wait" cuts 89.3%, 5,306 traces cut 76.0% | Stechly (b19); Tsui (b20) | established (K11) |
| Revisions destroy correct answers | naive revision flips 38% of correct to wrong (Snell, MATH); o1-preview 15.6%, o1-mini 34.0% | d05, d02 | established (K27) |

### 3c. LLM evidence on when patching pays and when to stop

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Reliable test signal -> gain; unreliable -> loss | HumanEval Py FP 0.01: 0.80 -> 0.91. MBPP Py FP 0.16: 0.80 -> 0.77. Rust 0.60 -> 0.68. TP/FN/FP/TN HumanEval 0.99/0.40/0.01/0.60; MBPP 0.84/0.59/0.16/0.41 | Reflexion (b22, c11, c12) | established (K12) |
| Finite best number of retries once false passes cost | cost-benefit ratio 4: optimal K about 5 (HumanEval+, 4 models); high ratio: K = 0 | Stroebl 2024-26 (d04) | established (K24) |
| With a real check, gains arrive in the first 2-3 rounds | Self-Debug: successes mostly within 3 turns (cap 10), TransCoder about +12 pts; CRITIC: 2-3 rounds; S*: QwQ-32B 72.6 -> 74.2 at 2 rounds | d06, d07, d08 | established (K25) |
| Model-written tests add nothing over public tests | no gain in S* ablation | d08 | single-source (K26) |
| Patch size shrinks as a loop degenerates | edits 529 -> 118 -> 83 -> 66 -> 21 chars (template 6,260 chars) | Beel 2025 (c20) | single-source (K13) |
| Quality of agent-science output under patch loops | 5 of 12 experiments (42%) failed; 4 of 7 manuscripts (57%) hallucinated numbers; depth cap 3; 3 AI papers submitted among 43 workshop submissions, 1 accepted (score 6.33) | c19, c20, c21 | single-source (K18) |
| Later reasoning rounds add little | first solution holds most correct answers; 48.6% fewer tokens on MATH500 at equal accuracy | Chen 2024 (b24) | established (K14) |
| Abandoning too early also hurts | wrong answers use 225% more tokens; QwQ AIME24 38.3 -> 44.1 with switch penalty (alpha 3, beta 600); R1 73.8 -> 74.8; prompt "stay on one thought" 72.4 | Wang 2025 (c14, c15) | established (K15) |
| Extended thinking helps then hurts; forced floor helps hard sets only | GSM8K 82.2 -> 87.3 at 1100 tokens, 70.3 at about 16,000; s1 AIME24 50.0 -> 53.3 (2x) -> 56.7 (4x), MATH500 93.0 -> 92.2 | Ghosal (d14); s1 (d13) | established (K29) |
| Stop errors in multi-agent traces | step repetition 15.7%; unaware of termination 12.4%; premature termination 6.20%; no or incomplete verification 8.20%; 1600+ traces; kappa 0.88 (experts, 150 traces), 0.77 LLM annotator | MAST (d09) | established (K29) |
| Failed attempts in context hurt | 39% average drop, 200,000+ conversations; accuracy falls as history error rate rises; re-appending the question cut overturned answers by 5.3-10.9 points; last-attempt-only context helped 1 of 3 models | d10, d11, d03, d08 | contested (K28) |
| More reflection words do not mean more accuracy | R1-Zero reflection not positively correlated with accuracy; base model already says "aha" | Liu 2025 (d12) | established (K30) |
| Hypothesis-bank patching from misfits works with labels | +31.7, +13.9, +3.3, +24.9 over few-shot; update stage +0.7 to +8.1 | HypoGeniC (c16, c17) | established (K16) |
| Two layers (hypothesis then code) beat direct | ARC 100 tasks GPT-4: 17% direct, 19% CoT, 23% program only, 30% LLM-filtered hypotheses, 33% human-selected | Wang 2024 (c18) | single-source (K17) |
| Cheap calibrated correctness signal from internals | ROC-AUC above 0.7, ECE below 0.1, R1-Distill-32B above 0.9 on AIME; 24% fewer tokens | Zhang 2025 (d15) | established, needs hidden states (K30) |
| No LLM study labels traces progressive/degenerating | 0 found in 2 searches | c25, d16 | gap, not proof (K20) |

## 4. Mechanisms and models

### 4.1 The Lakatos structure as a data model

An engineer can log an attempt line as a record:

```
programme = {
  core:      [task restatement, hard constraints, answer format]   # fixed after S1
  heuristic: planned sequence of operators / models (positive heuristic)
  belt:      [patch_1, patch_2, ...]  # each: what failed, what changed, predicted_new_case, result
}
```

- **Core** = what S1 UNDERSTAND fixed: the task as stated, constraints, output format. Patches may not rewrite it. Only a restart (a new programme) may.
- **Belt** = the current candidate method, with each revision logged as a patch.
- **Positive heuristic** = the operator queue (O1-O8). It explains a patch as motivated rather than ad hoc3.

### 4.2 Operational excess-content test (the main implementable idea)

Lakatos's two clauses become two code checks per patch:
1. **Theoretical progress (excess content).** Does the patch make a checkable claim beyond the failing example? Operational form: the patch must output a prediction for at least one input it was not built from (held-out example, mutated input, symmetry).
2. **Empirical progress (corroboration).** Run that prediction through an external verifier (code, tests, known answer). Pass = corroborated.

Labels per patch:
- progressive = predicted a held-out case and the case passed.
- ad hoc2 = predicted a held-out case and it failed.
- ad hoc1 = predicts nothing beyond the failing example (it only fixes the one failure).

This is the operational form of K02 and K05. It must use an external verifier (G3, G8). Evidence that a model-written test can stand in for this is negative (d08, K26). So the claim is a design hypothesis, untested (U1).

### 4.3 Degenerating signals (cheap, loggable)

All are proxies. None is validated against accuracy.
- Consecutive patches that are ad hoc1 or ad hoc2 (count K).
- Patch size shrinking: edit size below a fraction of the first patch (Beel: 529 to 21, about 4% of the first) (K13).
- Repetition: the new attempt is near-identical to a previous one (MAST step repetition 15.7%, d09).
- Check score flat or down across patches (the only one with direct support: Stroebl, Reflexion).
- Check false-positive rate high (Reflexion FP 0.16 hurt; Stroebl: FP rises with K).

### 4.4 Stop-or-continue as a decision rule

Stroebl's cost-benefit form (d04): continue only while the expected gain of one more attempt exceeds the expected cost of a false pass plus tokens. At ratio 4 the optimum was about 5 tries; with a bad enough check the optimum is 0. Snell (d05): difficulty changes whether to patch (easy items) or resample in parallel (hard items). Wang (c14): a stop rule must also not cut a line too early. So the rule has two sides.

- Floor: do not abandon a line before a minimum number of patches or tokens unless the check shows a clear fail (guards underthinking).
- Cap: stop after N consecutive non-progressive patches (guards overthinking and endless patching). The data point is N = 2 to 3 when a real check exists (K25).
- Both thresholds depend on the S0 difficulty class and on check quality.

### 4.5 Accept-patch guard

Keep best-so-far (G6). Accept a patch only if the external check improves. This follows from the 38% and 15.6-58.8% flip rates (K27).

### 4.6 What to do when the cap fires

Options in order (a design choice, not tested): (1) submit best-so-far; (2) restart from the core with a different operator (S6, O1-O8); (3) spend the rest of the budget on independent samples (G4, G12; Huang: voting beats extra rounds, K10); (4) if no check exists at all (the "stagnant" case), accept the best attempt and spend budget elsewhere (K21). Allow one reopening at a budget fraction, because verdicts reverse (K04).

### 4.7 Context handling

Models lean on their own earlier wrong attempts (d10, d11). Two alternatives to test: full history vs core restatement plus last failure note only (K28). Evidence is mixed, so both stay as arms in a test.

## 5. What holds up

**Holds up (two or more sources).**
- Without an external signal, LLM self-patching does not help and often hurts. Huang (2024), Kamoi (survey), Zhang (2025, includes o1 models), Stechly and Tsui agree (K06, K08, K11). Caveat: Huang's HotpotQA test set is 100 questions, and the prompts came from earlier papers.
- With a reliable external check, 2 to 3 rounds capture most gain (Self-Debug, CRITIC, S*; K25).
- Check reliability decides the sign of the effect (Reflexion FP 0.01 vs 0.16; Stroebl; K12, K24).
- Revision can destroy correct answers (Snell 38%, Zhang 15.6-58.8%; K27).
- Both stop errors exist: too long (Chen, Ghosal, MAST) and too short (Wang; K14, K15, K29).
- Lakatos gives no stopping number, and the criterion is retrospective (K03, K04).
- Displayed reflection is not progress (Liu, Wang's prompt null; K30).

**Failed or contradictory results.**
- Self-Refine (Madaan 2023) reported gains; Huang and Kamoi attribute reported gains in this literature to oracle labels or weak baselines (b23, c05). Self-Refine's own numbers were not extracted here.
- Reflexion looks like a counter-example to Huang, but its gains track the environment signal. Its own MBPP result (0.80 -> 0.77, FP 0.16) fits Huang (K12). Kamoi flags Reflexion as using external signals.
- Olausson: stronger-model feedback helps weak models (b17), but that is cross-model repair, not self-repair; it shows diagnosis is the bottleneck (c09: self-repair gains over baseline up to 3% for GPT-3.5, up to 10% for Code Llama).
- Last-attempt-only context: helped one of three models in S*, hurt two (d08). Not a settled intervention.
- Overthinking (later rounds add little) and underthinking (switching too early hurts) look opposed. They hold in different regimes. No source tests a rule that adapts (critique.md).
- Kamoi notes that decomposable-answer tasks (e.g., CoVe) allow some intrinsic correction (c05). Boundary condition.

**Moderators.**
- Check reliability (FP rate): decisive.
- Task difficulty: easy favors sequential refinement, hard favors parallel samples (Snell d05; Ghosal d14).
- Model strength: stronger models flip fewer correct answers (GPT-4 vs GPT-3.5 in Huang c03; o1-preview 15.6% vs 4o 58.8% in d02).
- Model type: thinking models self-reflect inside the chain, so external loops may add less, but S* still found gains from real execution feedback (d08).
- Context: the history of errors and the original question position (d03, d11).

**Interventions that worked.**
- External execution feedback (Self-Debug up to +12 pts on TransCoder and MBPP; Reflexion HumanEval +11 pts at FP 0.01).
- Hypothesis bank with replacement from misfits (HypoGeniC, +3.3 to +31.7).
- "Wait" appended to break the blind spot (Tsui, 89.3% cut; non-reasoning open models).
- Thought-switch penalty at decode (Wang; +5.8 pts QwQ AIME24; needs decoding control).
- Re-appending the original question (d03).
- Hidden-state probe for early exit (24% fewer tokens; open models only).

**Did not work.**
- Prompting "stay on one thought" (R1 72.4, below plain 73.8).
- Model-generated tests as the patch check (S*).
- Debate (Huang, K10).
- Counting reflection words (Liu).
- A strong switch penalty (alpha 20) over a long duration lowered accuracy (c14).

## 6. Language models

No study tests an LLM directly against Lakatos's progressive-versus-degenerating criterion or core protection (c25, d16, K20). The absence is stated with caution: search tools were rate-limited and few searches were available. Everything below is analogy through behaviour that matches the Lakatos pattern.

**Self-patching without a signal is a degenerating programme.** Huang (c01): CSQA 75.8 -> 38.1 -> 41.8. The model more often turns right answers into wrong ones than the reverse and cannot tell progress from degeneration (c03). In 2025 the same holds for o1-preview (-4.2 points), o1-mini (-12.1) and 4o (-20.4) (d02). The drop is smaller for stronger models, not zero. Reasons (d03): wavering between answers (GPT-3.5 changed 81.3% of answers more than 6 times in 10 rounds), prompt bias, and in decision tasks human-like bias (perfectionism bias 49.0% in that paper's failure split, not independently checked).

**Patching with a real signal pays, in the first 2-3 rounds.** Code and math with tests: Self-Debug, CRITIC, S*, Reflexion (K25, K12). Gains are small to moderate (S*: +1.6 on QwQ-32B at 2 rounds; Reflexion +11 on HumanEval; up to +12 on TransCoder).

**The patch step has a price.** Olausson's pass@t charges for sampling, feedback and repair. A ratio at or below 1 against plain resampling means the patching was degenerating. Under equal calls, voting beats debate (Huang: 88.2 at 9 vs 83.0).

**Check reliability is the hinge.** Reflexion: TP 0.99, FP 0.01 -> gain 0.80 to 0.91. TP 0.84, FP 0.16 -> loss 0.80 to 0.77. Stroebl: the optimal retry count is finite; weak models have more false passes; the FP rate rises with K.

**Stop-side errors.** Too long: the first solution holds most correct answers (Chen; 48.6% fewer tokens at equal MATH500 accuracy); accuracy rises then falls with extra thinking (GSM8K 82.2 -> 87.3 -> 70.3, Ghosal); parallel sampling beats extended thinking by up to 20% at equal tokens. Too short: 225% more tokens in wrong answers, more switches, and a switch penalty lifts AIME24 by 5.8 (QwQ) and 1.0 (R1). Multi-agent traces: step repetition 15.7%, unaware of termination 12.4%, premature termination 6.20% (MAST).

**Context and drift.** Models lean on their earlier wrong attempts (39% mean drop in multi-turn, d10) and condition on injected errors (d11; the paper says recent thinking models are not affected, from summary text only). Re-appending the question reduced overturns by 5.3-10.9 points (d03).

**Agentic science systems cap patching.** AI Scientist-v2 caps debug depth at 3 (c19); Denario caps n_fails and idea iterations (c23). Independent test of v1: edit sizes 529, 118, 83, 66, 21; 42% of experiments failed; 57% of manuscripts had hallucinated numbers (c20). Novelty judged by keyword search flagged known ideas as new (c21), which supports G8.

**What changed behaviour, by how much.**
- External check instead of self-judgement: from losses (CSQA -37.7 points with GPT-3.5) to gains (CSQA +13.9 with oracle labels).
- Reliable test (FP 0.01 vs 0.16): +11 vs -3 points on the same base 0.80.
- Fine-tuning for self-correction (SCoRe): +15.6 / +9.1 points. Not available to a scaffold.
- "Wait" trigger: 89.3% of blind spot removed (non-reasoning open models only).
- Switch penalty: +5.8 / +1.0 AIME24 points; needs decoding control.

## 7. What our agent should take

Status codes: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | A patch must cite the real failing output located by code, and be accepted only if an external check improves. Keep best-so-far; never let a patch replace a better prior answer. | G2, G6, S5 | [E] | K27, K08, K12; d05, d02, c02 (K07), b18 |
| A2 | When an external check exists, default patch cap at S6 of 2 to 3 failed patches, then stop patching that line. The exact number is a default, tuned by U2. | S6 | [E] for the 2-3 pattern | K25; d06, d07, d08 |
| A3 | Do not run a patch loop when no real check exists. Accept the best attempt (G6) and spend the budget on independent samples or another operator. | G2, G6, G12, S6 | [E] | K06, K08, K11, K24; c01, b18, d02, d04 |
| A4 | Gate patching on check reliability. In S0, estimate the false-positive rate of the available check. Skip or shorten revision when it is weak. | S0, G3 | [E] for the direction; threshold unknown | K12, K24; c12, d04 |
| A5 | Do not score progress by counting "wait", "recheck" or reflection words. Score by change in the external check. | G10 | [E] | K30; d12, c15 |
| A6 | Do not use model-written critique or model-written tests as the progress judge. Do not accept the model's own novelty claim. | G8, G10 | [E] | K05, K11, K26; c21, b19, d08 |
| A7 | Charge patch loops for their tokens: compare each against the same tokens spent on fresh samples (pass@t). | G7, G9 | [E] | K09, K10; c08, c10, c04 |
| A8 | Two-sided stop rule: cap endless patching, and set a floor so a line is not abandoned early on a hard item. Log repetition as a loop signal. | S6, G11, G12 | [E] that both errors exist; the rule itself is untested | K14, K15, K29; b24, c14, d09, d13, d14 |
| A9 | Keep the core (task restatement, constraints, answer format) separate from patches in the logs. | S1, S5, M | [E] as a concept; effect on accuracy untested | K01; a01-a03 |
| A10 | Never make a "degenerating" flag permanent. Keep best-so-far and allow one reopening at a budget fraction. Verdicts reverse and Lakatos tolerated long dry runs. | S6, G6 | [E] on the philosophy; the fraction is a choice | K03, K04; a06, a20, b04 |
| A11 | Keep a small bank of rival rules, replace the worst on misfit examples, and check on held-out inputs. | S2, S3, G3 | [E] with labels | K16; c16, c17 |

### Test first

| # | Item | Part | Status | Evidence ids | Test |
|---|---|---|---|---|---|
| T1 | Per-patch excess-content tag: each patch must predict one held-out case, checked by an external tool. Fire S6 after K consecutive patches that predict nothing or predict wrongly. | G1, S6 | [S] untested | K02, K05, K26; a04, a14, d08 | U1 |
| T2 | Compare caps of 1, 2, 3 failed patches at equal tokens, split by exact-answer vs open items. | S6 | [S] | K25, K29 | U2 |
| T3 | Shrinking patch size and repetition as degenerating predictors, on our own transcripts first. | S6 | [S] | K13, K29; c20, d09 | U3 |
| T4 | Fixed core: patch from the S1 restatement plus last failure note only, versus full history. | S1, S5 | [C] | K28; d03, d08, d10, d11 | U4 |
| T5 | "Wait"-style trigger inside S5 versus the plain revise prompt. | S5, G10 | [S] (non-reasoning open models only) | K11; b20 | U5 |
| T6 | Adaptive stop rule (floor and cap by S0 difficulty) versus fixed cap and fixed floor. | S6, G12 | [S] | K15, K29 | U6 |
| T7 | Break-even check reliability: where does revision change sign? | S0, G3 | [S] | K12, K24 | U7 |
| T8 | Rule-then-code two-layer scaffold on ARC-like items. | S2, S3 | [S] | K17; c18 | U8 |
| T9 | A "stagnant" state in S0 for items with no check. | S0, S6 | [C] | K21 | U9 |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, including setup and any extra check calls (G7). Report accuracy with a binomial confidence interval and the paired difference. Use items with an external verifier. Where tokens differ, spend the leftover on extra independent samples in the shorter arm.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| U1 excess-content tag | ARC-style rule items and code items with hidden tests | A: patch loop with round cap only. B: same, but each patch must output a held-out prediction checked by code; stop after 2 untagged or failed predictions | Accuracy at equal tokens; patches per solved item; tokens spent after the last useful patch | B saves tokens at same or higher accuracy. Prior: small gain (1 to 3 points). Real risk of zero (K26). |
| U2 cap size | Code (tests) and word/brain-teaser items (exact answer) | Caps of 1, 2, 3 failed patches, plus no cap with a token limit | Accuracy at equal tokens, by item class | Cap 2 to 3 best on tested items (K25). Little gain from 3 over 2. |
| U3 patch-size / repetition signal | Our logged transcripts, then live | Post hoc: predict final failure from patch-size ratio and repeat rate. Live: stop when the ratio falls below x of the first patch | AUC for eventual failure; tokens saved at equal accuracy | AUC above 0.65 is worth a live test. |
| U4 fixed core | Multi-turn patch items | A: full history. B: S1 restatement + last failure note | Accuracy; correct-to-wrong flip rate | B fewer flips; effect size unknown, evidence mixed (d08). |
| U5 "Wait" trigger | Items whose first answer is wrong in the plain arm | Plain revise prompt vs "Wait" + located failing output | Accuracy; flip rate | Benefit on non-reasoning models; expect null on reasoning models. |
| U6 adaptive rule | Mixed-difficulty set with S0 difficulty class | Fixed cap; fixed floor; adaptive (floor on hard, cap on easy) | Accuracy at equal tokens | Adaptive at least as good as the better fixed rule; untested anywhere. |
| U7 break-even reliability | Code items with checks of known FP rate (inject false passes) | Revision loop gated on FP rate vs ungated | Accuracy vs FP rate curve; sign-flip point | Sign flip between FP 0.01 and 0.16 per Reflexion; the point on our checks is unknown. |
| U8 two-layer scaffold | ARC-like items | Direct; program-only; rule-then-code | Accuracy | Ordering as in Wang (17 / 23 / 30 on GPT-4). |
| U9 no-check handling | Open items with no verifier | A: patch loop. B: best attempt + samples + vote | Rubric or blind human score | B equal or better (K06, d04). |

Also run a control: for every patch-loop arm, an arm spending the same tokens on fresh independent samples with code selection (A7).

## 9. What does not transfer, and why

- **Lakatos's timescales.** Decades-long tolerance (Prout, Copernicus) cannot be used for a run of minutes. His tolerance is about community-scale science. An agent has a token budget. Use his concepts, not his patience.
- **Retrospective appraisal.** Verdicts were made in hindsight and reversed (K04). An online stop rule has no hindsight. Hacking's reading (advice to historians) argues against copying the rule directly.
- **Rival-needed falsification.** Lakatos's elimination rule needs a rival programme with excess content (a05). A single agent line has none unless the agent runs a second line (pluralism, a16). That is expensive, and no LLM evidence says it beats sampling (G4, G9).
- **Novelty by model judgement.** Novelty is comparative and needs a reference set. A model's own claim is not valid (K05, c21).
- **Stagnant programmes.** Branahl's cases are physics fields with inaccessible experiments. The category matters only as a way to handle no-check items, and it is contested (K21).
- **Training-based fixes.** SCoRe (+15.6 / +9.1), R1-Zero-style RL, the switch penalty at decoding, hidden-state probes: all need training or model internals. A scaffold on a closed model cannot use them (b21, c14, d15).
- **Evidence from older models.** Huang uses GPT-3.5 and GPT-4. The o1 results (d02) show the effect persists, but 2025-2026 replications at equal tokens are missing. The claim in d11 that thinking models are unaffected by earlier errors comes from summary text only.
- **Cross-domain base rates.** Most numbers are GSM8K, CSQA, HotpotQA, HumanEval, MBPP, MATH, AIME. Open-ended or creative tasks have no equivalent check.
- **Multi-agent failure shares.** MAST percentages are shares of annotated failures, not failure rates, and come from multi-agent frameworks (d09).
- **Philosophical labels as acceptance tests.** Calling an LLM line "progressive" has no grounding unless a verifier decides it. Counting Lakatos terms in text is not a measure.
- **Agentic-science caps.** The depth-3 cap in AI Scientist-v2 is a design choice, not a tested optimum (K18).

## 10. Open questions

1. What patch-count or no-progress threshold at S6 gives the best accuracy at equal tokens, for exact-answer versus open problems? (Partly closed: 2-3 rounds, but no 1/2/3 head-to-head.)
2. Does a held-out prediction test per patch separate good patches from degenerating ones better than a round cap? (Open; needs an external verifier.)
3. Does Huang's no-oracle result hold for 2025-2026 reasoning models (o-series, R1, Claude with thinking) at equal tokens? (Partly: o1 loses accuracy; R1/V3 rows unreadable; no equal-token test.)
4. Where is the break-even check reliability for revision? (Reflexion gives only 0.01 vs 0.16; Stroebl gives the cost form.)
5. Can shrinking patch size or similarity of successive patches predict failure in our own transcripts? (Open.)
6. Is there a published LLM study that labels traces as progressive or degenerating? (None found; not a proof of absence.)
7. How to handle "stagnant" items with no check? The design default is best attempt plus samples. No evidence.
8. Can one adaptive rule beat a fixed cap and a fixed floor? (Both errors measured; no head-to-head.)
9. Does a fixed core reduce drift versus whole-attempt rewrite? (Contested; no direct test.)
10. Meehl (1990) primary text: any numeric guidance on how long to shield a core? (Not read.)
11. Does the thought-switch penalty have a prompt-level or scaffold-level equivalent that works? (The prompt version failed in R1, c15.)
12. Does the 2-3 round pattern hold outside code and math, where the check is weaker?

## 11. Sources

[V] = opened and read this session (page or PDF text). [M] = metadata or snippet only.

**Philosophy of science**
- [V] Lakatos (1970/1978) Falsification and the Methodology of Scientific Research Programmes. https://archive.org/details/TheMethodologyOfScientificResearchProgrammes (a01-a17)
- [V] Stanford Encyclopedia: Imre Lakatos. https://plato.stanford.edu/entries/lakatos/ (a18-a20, b01-b05; first 100,000 of 130,627 characters plus the Feyerabend section)
- [V] Wikipedia: Imre Lakatos. https://en.wikipedia.org/wiki/Imre_Lakatos (a21)
- [V] SEP Scientific Progress. https://plato.stanford.edu/entries/scientific-progress/ (a22, b06)
- [V] SEP Pseudo-Science and the Demarcation Problem. https://plato.stanford.edu/entries/pseudo-science/ (a23)
- [V] SEP Thomas Kuhn. https://plato.stanford.edu/entries/thomas-kuhn/ (a24)
- [V] SEP Pierre Duhem. https://plato.stanford.edu/entries/duhem/ (a25)
- [V] SEP Karl Popper. https://plato.stanford.edu/entries/popper/ (a26)
- [V] SEP Paul Feyerabend. https://plato.stanford.edu/entries/feyerabend/ (a27)
- [V] Sfetcu (2019) overview of MSRP. https://archive.org/details/ImreLakatosTheMethodologyOfScientificResearchProgrammesAnOverview (a31)
- [V] Branahl (2024, v3 2026) Stagnant Lakatosian Research Programmes. https://arxiv.org/abs/2404.18307 (b07-b09, c22)
- [V] Johansson and Matsubara (2011) String Theory and General Methodology. https://arxiv.org/abs/0912.3160 (b10, b11)
- [M] Meehl (1990) Appraising and amending theories (secondary summary). https://ohexel.github.io/2025/11/26/reading-meehl-appraising-and-amending-theories.html (b12); the primary at meehl.umn.edu returned HTTP 403
- [M] Batista (2025) EGU poster. https://meetingorganizer.copernicus.org/EGU25/EGU25-18554.html (b13)
- [M] Dreyfus review, Is AI a degenerating program? https://doi.org/10.1016/0004-3702(95)00087-9 (a28)
- [M] Nunan (1982) Bohr critique. https://doi.org/10.1007/bf01801188 (a29)
- [M] Human sociobiology, BBS 1987. https://doi.org/10.1017/s0140525x00056478 (a30)
- [M] Feyerabend (1975) waiting objection, cited through Branahl (b08).
- [M] Park, Leahey, Funk disruptiveness drop (90%), cited through Branahl (c22), not verified.

**Language models**
- [V] Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (b14, b15, c01-c04)
- [V] Olausson et al. (2024) Is Self-Repair a Silver Bullet. https://arxiv.org/abs/2306.09896 (b16, b17, c08-c10)
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes. https://arxiv.org/abs/2406.01297 (b18, c05-c07)
- [V] Stechly, Valmeekam, Kambhampati (2024) Self-Verification Limitations. https://arxiv.org/abs/2402.08115 (b19)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (b20)
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917 (b21; abstract and intro in the first pass, numbers re-checked in the critique)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b22, c11-c13)
- [M] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651 (b23; no numbers extracted)
- [V] Chen et al. (2024) Overthinking of o1-like LLMs. https://arxiv.org/abs/2412.21187 (b24)
- [M] Huang et al. (2025) POPPER. https://arxiv.org/abs/2502.09858 (b25; abstract and intro only)
- [M] Chen et al. (2023) Self-Debug abstract. https://arxiv.org/abs/2304.05128 (b26); the body was read later as d06
- [V] Wang et al. (2025) Underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 (c14, c15)
- [V] Zhou et al. (2024) HypoGeniC. https://arxiv.org/abs/2404.04326 (c16, c17)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660 (c18)
- [V] Yamada et al. (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 (c19)
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 (c20, c21)
- [V] Denario project (2025). https://arxiv.org/abs/2510.26887 (c23, c24, d01; read via a summarising fetch)
- [V] Zhang et al. (2025) Dark Side of Intrinsic Self-Correction. https://arxiv.org/abs/2412.14959 (d02, d03; table layout partly garbled)
- [V] Stroebl, Kapoor, Narayanan (2026 v3) Limits of Inference Scaling Through Resampling. https://arxiv.org/abs/2411.17501 (d04)
- [V] Snell et al. (2024) Scaling LLM Test-Time Compute. https://arxiv.org/abs/2408.03314 (d05)
- [V] Chen et al. (2023) Teaching LLMs to Self-Debug. https://arxiv.org/abs/2304.05128 (d06)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d07; numbers in figures, not read)
- [V] Li et al. (2025) S*. https://arxiv.org/abs/2502.14382 (d08)
- [V] Cemri et al. (2025) Why Do Multi-Agent LLM Systems Fail (MAST). https://arxiv.org/abs/2503.13657 (d09)
- [V] Laban et al. (2025) LLMs Get Lost in Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (d10)
- [V] Illusion of Diminishing Returns (ICLR 2026). https://arxiv.org/abs/2509.09677 (d11)
- [V] Liu et al. (2025) Understanding R1-Zero-Like Training. https://arxiv.org/abs/2503.20783 (d12)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (d13; AIME24 has 30 problems, one problem = 3.3 points)
- [V] Ghosal et al. (2025) Does Thinking More Always Help. https://arxiv.org/abs/2506.04210 (d14)
- [V] Zhang et al. (2025) Reasoning Models Know When They're Right. https://arxiv.org/abs/2504.05419 (d15)
- [M] Negative search records for direct Lakatos-on-LLM tests (c25, d16); GraphTracer and a preprints.org item seen only as snippets.
