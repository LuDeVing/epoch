# Belief bias: deep document

Subfield: accepting believable conclusions over valid ones. Built from `evidence_a-d.jsonl` (a01-a37, b01-b27, c01-c27, d01-d30), `claims.jsonl` (A01.04-K01-A01.04-K31) and `critique.md`. Written for the single-agent thinking schema (`research_notes/single_agent/SCHEMA.md`, v0.2).

Marks: **[E]** established, **[S]** single source, **[C]** contested. Source marks: **[V]** opened (full text or page text read), **[M]** snippet or abstract only. Where a "[V]" source was read only through a secondary page, the source list says so.

---

## 1. What it is

Belief bias is the tendency to judge an argument by whether its conclusion sounds true, not by whether the conclusion follows from the premises. People accept believable conclusions of invalid arguments and reject unbelievable conclusions of valid ones. The classic task is the categorical syllogism with four cells: valid or invalid, crossed with believable or unbelievable conclusion. The robust human finding is that believable-invalid arguments are accepted almost as often as believable-valid ones (66 to 92 percent across the three original experiments). Three questions drive the field. Does belief change reasoning quality or only the willingness to say "valid"? Is the effect a fast default that slow logic must override? Is it concentrated where the logic is inconclusive? Large language models show the same pattern, with a shape that depends on the model generation, the answer format and the amount of reasoning allowed. [A01.04-K01, A01.04-K13, A01.04-K26]

---

## 2. History and theories in depth

### 2.1 Timeline

| Year | Who | What |
|---|---|---|
| 1943 | Janis and Frick | First named the effect. Critics said atmosphere (the mood of the premises primes a conclusion type) could explain it. [a35, secondary] |
| 1944 | Morgan and Morton | Pitted atmosphere against belief. Belief won more often. [a35] |
| 1962 | Henle | Many "errors" come from reading the premises differently, not from bad logic. [a35] |
| 1980 | Revlin et al. | Argued apparent bias is atmosphere or premise conversion ("All A are B" read as "All B are A"). A rational-rule model predicted 80 percent of decisions in Exp 1. [b20] Criticised by Evans et al. 1983 for a four-option response format and no atmosphere control. [a05] |
| 1983 | Evans, Barston, Pollard (EBP) | The founding 2x2 experiments, with controls for atmosphere and conversion. Proposed both selective scrutiny and misinterpreted necessity. [d21-d24] |
| 1989-92 | Markovits and Nantel; Oakhill, Johnson-Laird, Garnham; Newstead et al. | Misinterpreted necessity and mental models developed and tested. [a07-a09] |
| 1995 | Polk and Newell | Computer model (verbal reasoning theory) that produces belief bias through a fallback rule. [a10] |
| 2000 | Klauer, Musch, Naumer | Multinomial processing tree model. [a11] |
| 2000-07 | Evans | Selective processing and default-interventionist account. [a03, a04] |
| 2003, 2006, 2008 | Thompson et al.; Ball et al.; Stupple and Ball | Inspection-time and eye-tracking tests of the theories. [a10, a31, a01-a03] |
| 2005 | Evans and Curtis-Holmes | Response deadline raises belief bias. [a24, a37] |
| 2010-14 | Dube, Rotello, Heit; Klauer and Kellen; Singmann and Kellen; Heit and Rotello | Signal detection reanalysis and the dispute over it. [a13-a16, a20] |
| 2013-18 | Trippas and colleagues | Moderators (complexity, time, ability), parallel-processing model, 22-study Bayesian meta-analysis. [a17-a23, b01-b09, b14] |
| 2022-26 | Dasgupta/Lampinen, Eisape, Bertolazzi, Ozeki, Valentino, Poddar, SemEval-2026 Task 11 teams | Belief bias in language models and remedies. [c01-c27, d01-d29] |

### 2.2 The original experiments (primary, read in full)

EBP 1983 (Memory and Cognition 11(3), 295-306). [d21-d23, A01.04-K26, V]

| Exp | N | VB | VU | IB | IU | Correct when logic agrees with belief / conflicts |
|---|---|---|---|---|---|---|
| 1 | 24 | 92 | 46 | 92 | 8 | 92 / 27 |
| 2 | 64 | 86 | 62 | 66 | 13 | 87 / 48 |
| 3 | 32 | 91 | 53 | 67 | 6 | 97 / 43 |

Cells are percent who accepted the conclusion as following. VB valid-believable, VU valid-unbelievable, IB invalid-believable, IU invalid-unbelievable. The interaction (belief matters more for invalid items) was p<.01 in Exp 2 and p=.067 (one-tailed) in Exp 3. Exp 1 instructions already said the conclusion must "necessarily follow", and 92 percent still accepted IB. A different set, 89/56/71/10, circulates on Wikipedia and matches no cell. Do not use it. [a33 corrected by critique]

### 2.3 The theory families (Stupple and Ball's taxonomy, credited to Evans) [a03]

| Family | Theory | Core claim | Prediction that separates it |
|---|---|---|---|
| Belief-first | Selective scrutiny (EBP 1983) | Judge the conclusion's believability first. Accept if believable. Reason only if unbelievable. | Longer inspection of unbelievable conclusions at any complexity. |
| Belief-first | Selective processing / default-interventionist (Evans 2000, 2007) | Default: accept believable, reject unbelievable. The analytic stage builds one model, then searches for a confirming model (believable conclusion) or a falsifying model (unbelievable). | More bias under speeding. No extra time on unbelievable. |
| Reasoning-first (escape hatch) | Misinterpreted necessity (EBP 1983; Markovits and Nantel 1989; Newstead et al. 1992) | Reasoning runs first. If the conclusion is possible but not forced, the person is unsure and falls back on belief. | Bias concentrated in indeterminate invalid items. Gone for determinate ones. |
| Reasoning-first | Mental models (Oakhill, Johnson-Laird, Garnham 1989) | Build a model of the premises, form a conclusion, then try to build counter-models. A believable conclusion that fits the first model is accepted without validation. An unbelievable one triggers a counter-model search. | Bias on one-model and indeterminate items. Mixed on multiple-model items. |
| Reasoning-first | Metacognitive uncertainty (Quayle and Ball) | Uncertainty after failed reasoning leads to belief use. | Bias rises with problem complexity. |
| Parallel | Sloman-style two systems running together; Trippas et al. 2017 | Belief and logic are computed side by side. Which interferes more depends on the logic's complexity. | Longer times on conflict problems. Interference in both directions. |
| Formal | Klauer et al. 2000 MPT | Reasoning succeeds with some probability. On failure a guess stage uses belief, atmosphere and the expected base rate of valid items. | Base-rate manipulations interact with belief only in the guess stage. |
| Formal | Signal detection (Dube et al. 2010) | One graded argument-strength axis. Belief shifts the response criterion, not discriminability. | Curved ROCs. No accuracy gap after correcting for criterion. |

The original authors offered the first two ideas themselves and could not separate them from the data. In Exp 2, people who accepted valid-unbelievable conclusions cited premises more (X2=24.61, p<.001) and irrelevant facts less (X2=15.11, p<.001). Verbal protocols may be rationalisations. [d24, A01.04-K28]

### 2.4 How the theories differ in practice

- Selective scrutiny and selective processing say belief decides how hard the model checks. They predict that extra checking helps mostly on unwelcome conclusions.
- Misinterpreted necessity says the checking is the same but the output is "cannot tell", and belief fills the gap. It predicts that a decisive counterexample test helps most on indeterminate invalid items.
- Mental models say the failure is the counter-model search not being run, or being too heavy when there are many models.
- Parallel models say there is no sequence. Conflict is detected early and often not resolved.
- SDT says there is nothing to fix in reasoning, only the threshold. The 2018 meta-analysis supports this on average, but the field still disputes the method (section 5.2).

Evidence tilts against strict selective scrutiny: inspection and eye-tracking data fit parallel or selective-processing patterns, and Thompson et al. 2003 found more time on believable conclusions, the opposite of the prediction. [A01.04-K10 contested; a02, a10, a31] Newstead et al. 1992 found the interaction vanished when only determinate syllogisms were used, supporting misinterpreted necessity, but Exps 3-5 supported mental models. [a09, a36, d08; abstract level]

---

## 3. Core findings with exact numbers

| # | Finding | Numbers | Source (ids) | Status |
|---|---|---|---|---|
| 1 | Believable conclusions are accepted far more than unbelievable ones | EBP Exp 1 N=24: 92/46/92/8 (VB/VU/IB/IU). Exp 2 N=64: 86/62/66/13. Exp 3 N=32: 91/53/67/6. Stupple and Ball N=48: AB-BC figure valid 76/72, invalid 71/36 (believable/unbelievable); BA-CB figure valid 88/60, invalid 61/25 | d21-d23, a01 | [E] (A01.04-K01, A01.04-K26) |
| 2 | Belief effect larger on invalid than valid (the interaction) | Logic x belief F(1,47)=9.15, p=.004 (S&B). EBP Exp 2 p<.01, Exp 3 p=.067. In the harder BA-CB figure the interaction vanished | a01, d22, d23 | [C] as to meaning (A01.04-K02); the raw-rate pattern is replicated |
| 3 | Correct answers fall when logic and belief conflict | EBP: 92 vs 27, 87 vs 48, 97 vs 43. Trippas 2017 Exp 2 (N=82): conflict .68 vs no-conflict .83, OR 1.58. Complex syllogisms under logic instructions, conflict items: .50 (chance) | d21-d23, a23, b14 | [E] (A01.04-K07) |
| 4 | Conflict items take longer | Premise inspection logic x belief F(1,47)=9.74, p=.003; Exp 1 of Trippas 2017: 4786 vs 4503 ms (d=0.17) | a02, b14 | [E] (A01.04-K07) |
| 5 | Believability does not change discriminability on average (ROC meta-analysis) | 22 studies, N=993. BF 7.34 for no difference in da. Equal-variance fit BF 17.28 (believable), 11.84 (unbelievable). Mean "valid" endorsement .92 believable vs .27 unbelievable. Choice-focus effect -.03 [-.08, .02], BF 69.72 | b01-b03 | [C] (A01.04-K03) |
| 6 | Believability does cost accuracy on complex items and in able reasoners | Trippas 2013: accuracy effect on complex, not simple syllogisms. Gone under time pressure and for low capacity. Trippas 2014 N=76: higher-ability fluent group t(15)=3.37, BF 11.34; lower-ability t(21)=0.28, BF 0.23 | a17, b07, b09, d27 | [S] (A01.04-K05) |
| 7 | Time limit raises belief bias (10 s deadline) | Effect on conflict items mostly. No numbers read (abstract level). Deadline is 10 s, not the 2 s on Wikipedia | a24, a37, b16 | [C] (A01.04-K06, A01.04-K30) |
| 8 | Time pressure effect is task-specific | Speeded conditional inference: belief bias size unchanged. Under time pressure the accuracy cost of belief vanished in ROC analysis | d26, d27 | [C] (A01.04-K30) |
| 9 | Complexity decides which of belief or logic interferes more | Modus ponens: validity interfered with belief judgments more. Hardest syllogisms: belief interfered with validity more. Exp 1 N=45, Exp 2 N=84 | a22, b14, d17 | [S] (A01.04-K06) |
| 10 | Wording of the validity question | One item per condition, N=130 (Exp 1), N=162 (Exp 2). Plain wording IB correct: 4% untrained, 10% trained. "Necessarily follow": 66%, 77%. "Criteria of logic": 41%, 67% | a27, a28, d07 | [S] (A01.04-K08, A01.04-K22) |
| 11 | Instruction effects in older multi-item studies | Newstead 1992 Exp 5 long instructions: IB correct 83%. Evans 1994 same instructions: 56%. "Must be true" alone did not remove the bias | d06, a26 | [C] (A01.04-K22) |
| 12 | Misinterpreted necessity: bias sits in indeterminate invalid items | Newstead 1992 Exps 1-2: interaction disappears with determinate items only | a09, a36, d08 | [C] (A01.04-K09), abstract level |
| 13 | Individual differences | Ability: ability on logic index F(1,72)=21.01; on belief response bias F(1,72)=9.59, p=.003. Skeptics vs believers on conflict accuracy t(85)=2.73, p=.008, N=91. Statistical-strategy reasoners more swayed (d=1.66 vs 1.04 for counterexample reasoners; N=170 in Study 1). Older adults and children worse on conflict items | b09, b17, b18, a34 | [E] (A01.04-K11) |
| 14 | Belief strength is a dose | N=102: prototypical 2.65, nonprototypical 2.25, nonword 1.43 of 5 invalid items accepted | b19 | [S] (A01.04-K18) |
| 15 | Disfluent text did not help | N=76: da .92 fluent vs .51 disfluent, F(1,74)=6.22, p=.015, BF 3.30. Belief response bias unaffected | a19, b08 | [S] (A01.04-K12) |
| 16 | Forced choice removes most bias | Presenting a valid and an invalid argument together: no belief bias on accuracy initially (abstract level). One at a time: unbelievable judged more accurately | b24, b23 | [S] |
| 17 | LLMs show the human pattern | Item-level human-model correlation t(345)=4.98. Interaction significant in PaLM 2-L, Flan-PaLM 2, GPT-3.5 (p<.001). None in Chinchilla and PaLM 2-M (answered mostly by content) | c01-c04 | [E] (A01.04-K13) |
| 18 | Older open models are poor at "invalid" and "nothing follows" | LLaMA-3 8B ZS-CoT 30.31% on believable set, 0.83% on invalid. Atmosphere heuristic predicts 82.97% of invalid-schema errors. Zero-shot CoT accuracy on 37 "nothing follows" syllogisms close to 0% (PaLM 2) | c05, c07, c08 | [E] (A01.04-K14) |
| 19 | GPT-3.5 and GPT-4 (2023) lose accuracy on belief-conflicting items | NeuBAROCO GPT-3.5: consistent 56.89, inconsistent 31.37. GPT-4 NLI English 82.92 vs 67.23 congruent vs incongruent. GPT-4 multiple choice (no "none follows" option): 90.00 vs 80.00 English, 97.5 vs 100 Japanese | c10, b26, d25 | [E] for older models; format dependent (A01.04-K29) |
| 20 | GPT-4 in SDT terms (my calculation from BaRDa cells) | Believable: hit .921, FA .579, d' 1.21, c -0.81. Unbelievable: hit .752, FA .100, d' 1.96, c +0.30. GPT-3.5: d' 0.81 vs 1.22, c -0.90 vs +0.41 | d05 | [S] (A01.04-K20) |
| 21 | Recent strong models show a small gap on easy syllogisms | 14 models, 160 items. Gemini 2.5 Pro +1.4 pp, Flash +0.9, GPT-OSS-20B +0.8, GLM-4.6 +1.9, Kimi-K2 +7.5, DeepSeek V3.1 +7.9, Llama 3.2 3B +46.9. Mean +10.81 pp, d=0.66, 12 of 14 positive | d01 | [S] (A01.04-K19) |
| 22 | Reasoning effort is the lever on valid-unbelievable items for one model | GPT-5-nano 69.2% (minimum effort) to 98.8% (medium). GPT-4o 79.5%. Claude-3-sonnet 20.3%, Claude-3-opus 7.2% (deprecated, valid-only items) | d03 | [S] (A01.04-K21) |
| 23 | Same model knows plausibility poorly even when logic is perfect | Syntax accuracy 81.7% vs believability accuracy 56.2% across models; Gemini 2.5 Flash 99.6 vs 51.7 | d02 | [S] |

---

## 4. Mechanisms and formal or computational models

Written so an engineer can implement each one as a measurement or a control step.

### 4.1 The four-cell design and the classic indices [a18]

Let `p(VB)` be the rate of "valid" responses in each cell.

```
logic index       = VB + VU - IB - IU
belief index      = VB + IB - VU - IU
interaction index = VU + IB - VB - IU      # sign as printed in Trippas et al. 2014
```

EBP Exp 1 gives interaction (.92-.92)-(.46-.08) = -.38 in the 2018 convention. [b01] Simulations show these difference scores can lead to wrong conclusions because they assume linear ROCs and they inflate Type I error. [a16, b08]

### 4.2 Signal detection indices [a18, d05]

For each believability cell, take hit rate H = P(say valid | valid) and false-alarm rate F = P(say valid | invalid).

```
d'  = z(H) - z(F)               # sensitivity (equal-variance)
c   = -0.5 * (z(H) + z(F))      # criterion; negative = lean to "valid"
```

Check with the GPT-4 BaRDa cells: believable H=.921, F=.579 gives d'=1.21, c=-0.81. Unbelievable H=.752, F=.100 gives d'=1.96, c=+0.30. [d05] With 0 or 1 rates apply a log-linear correction (add 0.5 to each count, 1 to each total).

With 3-point confidence ratings fit the ROC: `da = sqrt(2/(1+s^2)) * [z(H) - s*z(F)]` where `s` is the z-ROC slope. SDT belief index is `ca(unbelievable) - ca(believable)`. SDT interaction index is `da(unbelievable) - da(believable)`. [a18] Equal-variance is justified by the 2018 meta-analysis (BF 17.28 and 11.84) except near ceiling (Study 2 had a slope above 1). [b02]

Cautions that bind the implementation:
- A 2x2 SDT design with separate criteria per believability is not identifiable without extra assumptions. Fixing the IB mean to 0 forces a criterion-shift reading. [a20]
- Check ROC shape before trusting d' on a new task type. Causal conditionals violated the expected pattern. [b10]
- At 99 percent accuracy, d' and CE are dominated by noise. An unbiased 98 percent model has an expected measured CE around 2.3 in SemEval units. Test any gap against a null with the same accuracy. [c18]

### 4.3 Klauer, Musch, Naumer MPT [a11]

Four trees, one per cell.

```
with prob r(cell):   reasoning reaches a result  -> respond correctly
with prob 1-r:       uncertain -> guess stage
   guess valid with prob g = f(expected validity rate, conclusion plausibility, atmosphere)
```

The told base rate of valid items (many, some, few) shifts `g` and interacts with belief only in the guess stage. Logic-trained people reasoned to a result more often and guessed less, but when guessing were no more or less belief-driven than novices. To implement: run the same item set under three stated base rates and fit `r` and `g` by cell frequency. This yields a "guess rate" and a "belief on guess" rate as separate quantities. Garnham and Oakhill (2005) dispute that the mental-models account maps onto this model. [a12] Formal models are hard to separate with accuracy data alone.

### 4.4 Selective processing (Evans) [a03, a04]

```
default:   accept if believable, reject if unbelievable
analytic:  build one model of the premises
           if conclusion believable:   search for a model that confirms
           if conclusion unbelievable: search for a model that falsifies
```

Because the confirming search can stop early, it leaves invalid-believable conclusions accepted. This is the one model that describes search direction as belief-dependent. For the agent, S4 should always include a refutation attempt, not only a confirming run.

### 4.5 Polk and Newell verbal reasoning theory [a10]

Solve by manipulating linguistic terms. Annotate statements as plausible or implausible. If the generated conclusion is implausible, re-encode the premises. If that fails, choose at random between "not valid" and a belief-based conclusion. The simulation reproduced belief bias. Thompson et al. (2003) revised it: search for an integrating model until a deadline, with a longer deadline for believable content. The failure rule "if the check fails, guess toward the plausible answer" is a risk in an LLM too.

### 4.6 Mental models [a08]

Three stages: comprehension (build the premise model), description (form or compare a conclusion), validation (try to build counter-models). Deduction happens only at validation. One-model problems and indeterminate ones show belief effects. Multiple-model valid items gave inconclusive results (too many models to hold). Implementation hint: externalise the counter-model search by enumeration for multi-premise items.

### 4.7 Heuristic and form-level models

Atmosphere: the quantifier mood of the premises primes the conclusion. It explained 82.97 percent of invalid-schema errors and 92.31 percent of correct valid conclusions for LLaMA-3 8B ZS-CoT. [c07] Under a limit below 20 s, atmosphere was the main cue in people and belief was secondary. Atmosphere vanished with more time while belief bias remained. [a25] Conversion ("All A are B" read as "All B are A") is the other classic form error. [a35]

### 4.8 Representational model of LLMs [c14, c12]

Validity and plausibility are each linearly encoded. Cosine similarity of the two direction vectors is 0.48 to 0.64 (controls 0.10 to 0.13 and -0.12 to -0.17). Across 10 instruction-tuned models (Qwen-2.5, Qwen-3, Gemma-3, 4B to 32B), more aligned directions go with a bigger content effect (beta=0.557, p=0.017). Steering that pulls them apart cuts the effect. This needs open-weight access, so it is not available to a prompt-only scaffold. It does tell us why introspection fails: the two signals are tangled inside. Separation has to happen outside the model. [A01.04-K13-A01.04-K15]

### 4.9 Dual-process timing models

Default-interventionist: belief answer first, logic intervenes later. It predicts belief errors worsen under speeding. Parallel: both are computed together. Evidence for parallel: Trippas et al. 2017, Stupple and Ball 2008, and a 2015 thesis (abstract only). [a22, a02, d20] The agent analogue: do not assume that a short budget raises belief errors. Measure it.

---

## 5. What holds up

### 5.1 Replicated and robust

1. The raw-rate pattern: believable conclusions accepted more, and IB acceptance at 66 to 92 percent. Replicated across EBP's three experiments and Stupple and Ball (71 and 61 percent). [d21-d23, a01]
2. Conflict items are harder and slower. Three independent lines: EBP, Stupple and Ball, Trippas 2017. [A01.04-K07]
3. Ability and analytic disposition help. Religious skeptics, higher Raven scores, counterexample strategy users, younger adults all made fewer conflict errors. [A01.04-K11]
4. LLMs of 2022-2024 show the pattern, in several model families, in several labs. [A01.04-K13]
5. Prompts alone do not fix it in older models: no change with few-shot or instruction tuning (Dasgupta), ICL did not remove it (Bertolazzi), few-shot was the worst strategy in a 14-model study (79.1% vs 82.7% zero-shot, paired t41=2.50, p=.0165, Holm p=.0495, d=-0.39). [c04, c06, d02, A01.04-K14]

### 5.2 Contested

- **Meaning of the interaction.** Dube et al. (2010, 2011) and Heit and Rotello (2014): the interaction is an artefact of difference scores. Belief is a response bias. Klauer and Kellen (2011): ROCs for binary responses are linear. Dube's own data fit misinterpreted necessity. Singmann and Kellen (2014): the 2x2 SDT design is unidentifiable. The 2018 meta-analysis favours Dube on the average, but the authors overlap with that camp. [A01.04-K02-A01.04-K04, a13-a16, a20, b01-b04]
- **Moderators hide inside the null.** Pooled null (BF 7.34) means no average gap, not no gap in anyone. Participant, item and study heterogeneity all had credible intervals above 0. [b05]
- **Time pressure.** Evans and Curtis-Holmes (10 s) support the fast-belief story. Evans, Handley, Bacon 2009 (conditional inference) and Trippas 2013 (SDT) show boundary conditions. Trippas 2017 favours parallel processing. No direct failed replication of the deadline was found, and it was not searched exhaustively. [A01.04-K06, A01.04-K30]
- **Selective scrutiny versus misinterpreted necessity.** Never separated. [A01.04-K09, A01.04-K10, A01.04-K28]
- **Complexity by belief.** Evans and Pollard (1990) found complexity changed discrimination but not the belief effect. Klauer et al. (2000) reread the same data and argued belief mattered more in complex groups. [a04, second-hand]

### 5.3 Failed or partly failed

- "Must be true" instructions did not remove belief bias (Evans et al. 1994; Barston 1986; Evans, Handley, Harper 2001; Handley et al. 2011 per Macchi). [a26, d07]
- Newstead 1992 Exp 5 long instructions gave 83 percent IB correct. Evans 1994 with the same instructions got 56 percent. [d06]
- Disfluency was expected to help and lowered accuracy (Alter et al. 2007 report help, Thompson et al. 2013 a null). [b08]
- EBP Exp 3, with stronger necessity wording, still gave 67 percent IB acceptance. [d23]
- Macchi's "necessarily" result is one syllogism per condition, with a control from a previous experiment. [a28]
- Few-shot belief-trap examples did not reduce bias in LLMs and slightly hurt. [d02]
- Predicate-argument abstraction scored worse than raw text (77.48 vs 92.10). [d14]

### 5.4 Interventions that worked (human or LLM)

| Intervention | Effect | Evidence | Caution |
|---|---|---|---|
| "Does it necessarily follow?" plus "Why?" | IB correct 4% to 66% (untrained), 10% to 77% (trained) | a28, d07 | One item. Control not randomised. No LLM test. |
| Long logic instructions (explain "some", use only given info) | IB correct 83% (Newstead 1992 Exp 5) | d06 | 56% in Evans 1994. |
| Forced choice between a valid and an invalid argument | No initial belief bias on accuracy; Chinchilla showed the same | b23, b24 | Abstract level and one-model appendix. |
| Counterexample strategy | Belief score 1.47 vs 2.47 (statistical strategy) | b18 | Strategy classed from a pretest. |
| Step-by-step prompt on a prior failure set (GPT-4o) | 87 of 100 earlier failures now correct. A belief-conflict warning: 76. Plain prompt: 3 | d04 | Selected failures, valid-only items, no equal-token control. |
| Reasoning effort (GPT-5-nano) | 69.2% to 98.8% | d03 | Valid-only items. Criterion shift not separable. |
| CoT on newer instruction-tuned open models | Qwen2.5-32B CE 0.348 to 0.096. Qwen3-14B 0.213 to 0.014 | c15 | Small open models. Different CE metric. |
| Translate to FOL and run a prover (Qwen3 4B) | 95.83 / CE 2.28 vs end-to-end 84.17 / CE 14.67 | d13 | A strong model's plain prompt is already 98.43 / 2.13. |
| Predicate-logic translation inside the prompt (GPT-4) | 77.78 to 96.67 on 90 items | d25 | No token count. |
| Verify only on 3-2 ensemble splits | 93.4 to 94.3 accuracy, CE 3.39 to 2.85. 19 right and 11 wrong flips | d11 | 8 net items. SD overlaps. Trigger is disagreement, not belief conflict. |
| Activation steering | Llama 3.2 1B 58.17% to 73.56% | c12 | Needs weights. |
| Supervised fine-tuning | LLaMA-3 8B 30.31% to 96.25%. B\|U 22.10% to 4.28% | c06 | Training. Excluded. Generalisation dropped at more premises. |

### 5.5 Interventions that did not work or backfired

Few-shot examples (including a belief-trap example), instruction tuning alone in older models, "must be true" wording alone, disfluent text, solver-only pipelines on weak extraction (Z3 alone 74.7% accuracy, CE 26.28; 98 percent right on invalid items but about 52 percent on valid), widening the solver's authority (Z3 veto: 74.1%), and Z3 on 4-1 splits too (91.7%). [d02, d11, d12, b08, a26, c04]

---

## 6. Language models

### 6.1 What they do, by generation

| Generation | Models | Pattern | Evidence |
|---|---|---|---|
| 2022-23 base | Chinchilla, PaLM 2 M/L, Flan-PaLM 2, GPT-3.5 | Human-like. "Valid" for believable conclusions, high sensitivity, low specificity. Chinchilla and GPT-3.5 said "valid" to nearly all nonsense propositions. Item-level t(345)=4.98 | c01, c02, A01.04-K13 |
| 2023 chat | GPT-3.5, GPT-4 | NeuBAROCO GPT-3.5 inconsistent 31.37 vs consistent 56.89. GPT-4 NLI 82.92 vs 67.23. BaRDa GPT-4 d' 1.96 to 1.21 and c +0.30 to -0.81 (both sensitivity and criterion move) | c10, b26, d25, d05 |
| 2024 open | LLaMA-3, Pythia 160M to 70B | Mostly fail on invalid items. LLaMA-3 8B 0.83% on invalid. Instruction tuning raises invalid accuracy and lowers valid | c05 |
| 2025 small instruction-tuned | Qwen2.5/3, Gemma-3 4B-32B | CoT cuts content effect strongly (see 5.4). Models in the 14-model study differ widely: Gemma 3 27B -13.7 and Qwen3-Next Instruct -7.9 show the reverse sign | c15, d01 |
| 2025-26 frontier / reasoning | Gemini 2.5, GPT-OSS, GLM-4.6, GPT-5 family, Kimi-K2, DeepSeek V3.1 | Near ceiling on easy syllogisms (99 percent). Gap 0.8 to 7.9 pp. Reasoning effort matters inside a model | d01, d03 |
| Claude | Claude-3 only, deprecated | On valid-only items 20.3% and 7.2%. This cannot separate skill from over-rejection. No current Claude model was found tested anywhere | d03, d30, A01.04-K31 |

### 6.2 What changed it, and by how much

- **Model generation and reasoning effort** matter most. GPT-5-nano 69.2 to 98.8 by effort alone. [d03]
- **CoT**: contradictory. Weak for older open models, strong for newer small models (Qwen3-14B CE 0.213 to 0.014), not uniform for FregeLogic's open models (Maverick few-shot CoT CE 3.83 to 10.11, simple CoT lowest mean CE 5.24). [c05, c15, d10] No equal-token test exists. [A01.04-K15]
- **Instruction**: a CoT prompt rescued 87 percent of GPT-4o failures. A belief-conflict warning rescued 76 percent. [d04] These are selected failures, so partly regression to the mean.
- **Few-shot**: no help on syllogisms. Large help on easy NLI for Chinchilla ("highly content-biased" to "near ceiling"). [c04, d02]
- **Answer format**: multiple choice without a "none follows" option hides the bias for GPT-4 (90.00 vs 80.00), NLI shows it (82.92 vs 67.23). [d25] LLMs almost never answer "nothing follows" on abstract syllogisms (37 of 64 items need it; accuracy near 0). [c08]
- **Formalising**: for weak or mid models, a prover wins. For strong models, small gain at 4x to 15x cost (CLOVER $0.30 vs CoT $0.02; FregeLogic about 4,300 tokens and 6 calls per item). [d13, d14, d16, d11]
- **Plausibility knowledge**: models that ace validity score near chance (56.2 percent) on judging whether the conclusion is believable. [d02] Whatever bias exists is not accompanied by a reliable internal belief judgment.

### 6.3 Why the bias persists in LLMs

Plausibility and validity are linearly entangled (c14). A small circuit handles syllogisms, with contamination from commonsense heads (c19). CoT explanations can inherit the content shortcut. Content effects persist in step-by-step text. [c13, d19] This is the basis for G10 (reasoning text is not evidence).

### 6.4 Measurement hazards in LLM studies

- Accuracy-gap metrics at 99 percent ceiling hide the bias. [d01]
- Valid-only benchmarks (BIS) cannot separate skill from a criterion shift. [d03]
- The SemEval CE metric is noisy at high accuracy. Team rankings are weak evidence. [c18, d29]
- Likelihood scoring (Dasgupta) is not free generation. [c01]
- "Believable" is sometimes "true facts" (BaRDa), sometimes "any premise or conclusion conflicts with belief" (NeuBAROCO). [d05, c10]
- Poddar, FregeLogic, SemEval and HABIB_TAZ are preprints, tuned on small sets. [critique]

---

## 7. What our agent should take

Schema labels: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md. Status marks follow the evidence, and the "evidence ids" column cites this folder.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Never let the model judge validity from content alone. A validity check must be run on structure: the premises restated in neutral terms, a refutation attempt, or code. The model's feeling that an answer is right is not a check. | G10 (reasoning text is not evidence), S4 TEST | [E] | A01.04-K01, A01.04-K13, A01.04-K14; c01, c02, c13, c14, d19 |
| A2 | S4 treats every candidate the same way, including answers that look believable. Do not make scrutiny depend on whether the answer feels right. This is consistent with the evidence against strict selective scrutiny and with the parallel-process results. | S4, G3 | [E] as a design rule (the mechanism is [C]) | A01.04-K10; a03, a04, a06, a31, b04 |
| A3 | Input hygiene: S1 restates the problem and fixes the reading of quantifiers ("some" means at least one and possibly all, use only the given information) before reasoning. Misreading premises looks like belief bias. | S1 | [E] for misreading as a confound; the specific prompt text is [S] | a26, a35, b20, A01.04-K09 |
| A4 | Report belief effects with per-cell numbers: hit rate, false-alarm rate, d' and c by believability cell, plus raw cell accuracy. Include invalid items and a "does not follow" option. Never score the agent with the difference-score interaction index alone. | measurement (section 6 logging) | [E] as a method rule (the theory behind it is [C]) | A01.04-K02-A01.04-K04, a13, a16, a18, a20, d03, d25, c18 |
| A5 | Log conflict items separately: label items where the answer the agent prefers disagrees with its derived verdict. Conflict items are slower and harder. | section 6 logging | [E] | A01.04-K07; a02, a22, a23, b14 |
| A6 | Do not add "be careful", "think logically" or belief-trap few-shot examples as fixes. They are already in 4b and the belief-bias evidence repeats it. | 4b | [E] | A01.04-K14; c04, c06, d02, a26 |
| A7 | Keep the S7 counterexample search. A counterexample strategy is the protective one in humans (belief score 1.47 vs 2.47, d=1.04 vs 1.66). | S7, O | [E] (already marked E in the schema) | A01.04-K11; b18, a08 |
| A8 | Offer a "does not follow / nothing follows" option, and keep the check for it in code. LLMs rarely choose it. | S4, S7 | [E] | c05, c08, d25, A01.04-K14 |
| A9 | Do not rely on a prompt to fix content effects in a mid-size model. Where a cheap exact check exists (categorical syllogism forms: 24 valid forms), run it in code after the model labels mood and figure. | G5 (code selects), S4 | [S] for the lookup; [E] that prompts alone are weak | c24 (snippet), c17, c06 |

### 7.2 Test first (single-source, contested or unsupported)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Conflict flag: if the agent's prior belief about the conclusion disagrees with its derived verdict, route extra verification. No LLM test exists. | G1 (doubt on a signal), S6 | [S] humans detect conflict cheaply; LLM test none | a02, a29, A01.04-K07, A01.04-K23, A01.04-K27 |
| T2 | Verify only on conflict vs verify all vs random subset at equal tokens. | S4, S8 | unsupported | A01.04-K10, A01.04-K23, A01.04-K27; d11 |
| T3 | "Necessarily follow" wording. | S1 or S4 wording | [S] (one item, humans) | a28, d07, A01.04-K08, A01.04-K22 |
| T4 | Counterexample step split by determinate and indeterminate invalid items. | S7, O4 | [C] | a09, d08, A01.04-K09, A01.04-K27 |
| T5 | Neutral-symbol reasoning compared with the real-content run, adopt the symbolic verdict on disagreement. | S1, S2, O6 | [S] | c20, d14, A01.04-K17 |
| T6 | Prover or canonical-form parser: LLM translates, code decides. Re-extract when the prover says "invalid" on an item the model believed valid. | O, G5 | [C] | A01.04-K16, A01.04-K24, A01.04-K25; c17, d12-d14 |
| T7 | Pairwise forced choice between a valid and an invalid candidate rather than a single argument. | S7 | [S] | b23, b24 |
| T8 | Budget effect: short vs long reasoning, scored as d' and c separately. | G11, G12 | [C] | A01.04-K06, A01.04-K30, A01.04-K21; d03, d26, d27 |
| T9 | Disagreement routing (verify only when attempts split). | G1, G4 | [S] | d11, A01.04-K23 |
| T10 | Graded belief strength as a predictor of error. | S0 gate | [S] humans only | b19, A01.04-K18 |
| T11 | Restating premises with neutral labels before reading the conclusion (hide conclusion until premises are stated). | S1, S2 | [S] eye-tracking suggests conclusion anchors the re-reading | a31, a32 |
| T12 | Memory lesson "this class has belief traps" shown after the first attempt. | memory | [D] | schema section 5 |

### 7.3 Interpretation rules for the schema's own claims

- G1 (doubt only on signal) and belief bias are in tension. The risk: a believable wrong answer sends no doubt signal. T1 and T2 test whether a belief-conflict signal exists, and A2 keeps S4 neutral. The conflict signal is a candidate, not a replacement for the check.
- G6 (never abstain) plus the Polk and Newell failure rule: flag any final answer that came from a failed check and was chosen by plausibility. [a10]
- G7 (pay for itself) kills any element here that loses at equal tokens. Nothing in this folder has an equal-token test.

---

## 8. Concrete tests on our bench

Common design. Build one item bank with four cells (valid, invalid) x (believable, unbelievable), plus nonsense-content controls. Keep determinate and indeterminate invalid items separate. Every item has a content-swapped twin with identical logic. Add a "does not follow" option. Grade each item by code. Run all arms at equal total tokens (count setup). Log the mode, path, tokens per state and flips. Metric is reported per cell, plus d' and c with the log-linear correction, plus the raw gap against a same-accuracy null. Sizing: at 40 items per cell the standard error on a rate near .5 is about 8 pp, so only effects above roughly 15 pp are visible. For a 10 pp paired effect plan for about 100 items per cell. For 99 percent ceiling items there is nothing to see, so use hard items (multi-model, three-term, complex). [d01, c18, a23]

The bench today is ARC and BRAINTEASER. This is a new item type: it needs an item generator and a code grader. For categorical syllogisms the grader is the 24-form lookup. [c24]

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B0 baseline | 4-cell bank, easy and hard, believable / unbelievable / nonsense | plain model, direct answer | Per-cell accuracy, d', c, raw gap vs null | Easy: gap near 1-8 pp for a strong model (d01). Hard: larger. Unknown for our model (A01.04-K31). Needed before any other test. |
| B1 CoT vs plain at equal tokens (T8) | Hard 4-cell bank | A: one long CoT. B: 3-4 short independent attempts plus code vote (G11) | CE as accuracy gaps, d', c | Medium-sized models may drop a lot with CoT (Qwen3-14B CE 0.213 to 0.014); for a frontier model likely near zero on easy items. The question is whether the bank is hard enough to show anything. |
| B2 Conflict flag routing (T1, T2) | 4-cell bank | A: verify all. B: verify only when stated prior belief about conclusion disagrees with derived verdict. C: verify a random subset of equal size. D: no verification | Accuracy on IB and VU, tokens, how many flips right to wrong | B at least equal to C at lower tokens if the flag carries signal. Prediction is risky: IB errors are made without conflict being felt by the model. Expect B to beat C only if the flag is informative. Unknown. |
| B3 Counterexample search by determinacy (T4) | Indeterminate invalid, determinate invalid, and valid believable items | A: plain. B: add a "find a counterexample, then answer" step | Rate of correct rejection on IB, split by determinacy; false rejection on VB | If misinterpreted necessity holds, gain on indeterminate IB items and no gain on determinate. If selective processing holds, gain on both. |
| B4 Wording (T3) | Many invalid-believable items (40+) | A: "Does it follow?" B: "Does it necessarily follow?" C: "Could the conclusion be false while the premises are true?" | Correct rejection of IB, false rejection of VB, d', c | The wording may shift c only. Human evidence suggests a big effect on one item, none on many. Expect small. |
| B5 Neutral symbols (T5) | 4-cell bank | A: real content. B: restate with variables and reason. C: both, adopt B's verdict on disagreement | Accuracy, agreement rate, tokens | B and C help most on IB. Predicate-argument abstraction was worse (d14), so use canonical syllogism notation, not a loose abstraction. |
| B6 Prover or form lookup (T6) | Categorical syllogisms | A: CoT. B: model labels mood and figure, code looks up the 24 valid forms. C: B plus re-extraction when the lookup says "invalid" on an item the model had judged valid | Accuracy, d', c, tokens | For a strong model small or no gain on accuracy, but exact control of the criterion. Watch the invalid lean (A01.04-K24). |
| B7 Forced choice (T7) | Pairs (one valid, one invalid) with believability crossed | A: single-argument validity. B: pairwise choice | Accuracy by cell | Human forced choice removed most belief bias; expect a gain in IB accuracy. |
| B8 Graded belief (T10) | Conclusions rated 1 to 5 for plausibility by a separate model call or fixed ratings | one arm: plain | Error rate against plausibility rating | Positive dose-response if the human pattern transfers. |
| B9 Disagreement routing (T9) | 4-cell bank | A: vote of 3 attempts. B: vote plus extra check only on a split. C: extra check on all | Accuracy, tokens | FregeLogic saw 8 net items on 960. Expect a small gain at best. |
| B10 Premise-first (T11) | 4-cell bank | A: full item. B: premises restated first, conclusion shown second | Accuracy by cell | Small, humans only; test cheap. |

Each test reports G7 verdicts: keep, restrict, or remove.

---

## 9. What does not transfer, and why

- **Time pressure.** The 10 s deadline takes away the analytic search from a human. A token cap on an LLM does not stop a parallel process of the same kind, and the human findings themselves are mixed (A01.04-K30). Do not carry "rushed means more belief bias" into the agent.
- **Individual differences.** Raven scores, religious belief, age and thinking disposition do not apply to one model. The analogue is model size and generation, and the LLM data on size are mixed (bigger is not always less biased). [c09]
- **Disfluency, fonts, mouse-contingent displays.** No LLM analogue. [A01.04-K12]
- **Eye-tracking and inspection times.** The agent has tokens, not gaze. Used here only as theory evidence.
- **Verbal protocols.** Reports of what people did are rationalisations, as the schema's G10 says for the model.
- **Activation steering, fine-tuning, probes.** Valid but need weights or training. Our scaffold is prompt and code. They only tell us belief and validity are separable directions. [c12, c14, c06]
- **"Think logically" instructions.** Human gains are small and inconsistent. Do not expect more from a model.
- **Dual-process framing.** The agent has no System 1 and System 2 as such. Fast belief answers do not "intervene" on slow logic in a model. The parallel account is a better metaphor, but still a metaphor.
- **Belief as prior knowledge.** For humans belief comes from life experience. For an LLM it is learned world knowledge that can be wrong, and a model may judge plausibility poorly (56.2 percent). [d02] A measure of "what the model believes" needs its own check.
- **Human accuracy numbers.** EBP used undergraduates, one problem per cell (Exp 1), prose passages. The percentages are not a benchmark for an LLM. [d21]
- **Easy-item results.** At 99 percent accuracy, SemEval-type gaps are noise. [c18]

---

## 10. Open questions

From critique.md and claims A01.04-K27, A01.04-K31. These need our own experiments, not more reading.

1. Content effect for a current frontier model with plain prompting, scored by d' and c on hard items (indeterminate invalid, believable and unbelievable). No current Claude, GPT-5 or o-series d' analysis found. [A01.04-K31, d30]
2. CoT at equal tokens for frontier models. [A01.04-K15]
3. Whether the "necessarily follows" wording effect holds across many items, and whether it transfers to LLMs. [A01.04-K22]
4. Counterexample search on indeterminate vs determinate invalid items in LLMs. [A01.04-K09, A01.04-K27]
5. Verify only conflicts vs verify all vs random at equal tokens. [A01.04-K10, A01.04-K23]
6. A belief-versus-verdict conflict flag as an error predictor in LLMs. Only ensemble disagreement was tested. [A01.04-K23]
7. Prover vs prompt abstraction at equal tokens. [A01.04-K16, A01.04-K25]
8. Failed replications of the logic-by-belief interaction in raw rates, and of the 10 s deadline. Not searched exhaustively. [critique]
9. Graded belief strength in LLMs. All LLM studies use binary plausibility. [b19, d18]
10. Whether the SDT reading (belief shifts the criterion) holds for models. The BaRDa numbers say both d' and c move for GPT-4, but those are 2023 data and my own calculation. [d05]
11. Size of the interaction in the 1990s-2000s replications of EBP. Not re-extracted. [critique]
12. Whether a "stop-and-choose-by-plausibility" fallback exists in LLMs (the Polk and Newell failure rule), and whether flagging it helps.
13. Primary sources still unread: Evans and Curtis-Holmes 2005, Newstead 1992, Evans, Handley, Harper 2001, Klauer et al. 2000, Dube 2010 full text. No open PDF. [d30]

---

## 11. Sources

**[V]** opened. **[M]** snippet or abstract only. Where the critique notes a secondary-only read, it is marked (secondary).

### Human literature

1. [V] Evans, Barston, Pollard (1983) On the conflict between logic and belief in syllogistic reasoning. https://link.springer.com/content/pdf/10.3758/BF03196976.pdf (d21-d24)
2. [V] Stupple and Ball (2008) Belief-logic conflict resolution in syllogistic reasoning: inspection-time evidence for a parallel-process model. https://clok.uclan.ac.uk/6125/2/6125_Ball.pdf (a01-a04; author draft)
3. [V] Trippas, Kellen, Singmann, Pennycook, Koehler, Fugelsang, Dube (2018) Characterizing belief bias in syllogistic reasoning: hierarchical Bayesian meta-analysis of ROC data. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6267550/ (b01-b06)
4. [V] Trippas, Handley, Verde (2014) Fluency and belief bias in deductive reasoning. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00631/pdf (a18, a19, b08, b09)
5. [V] Trippas, Thompson, Handley (2017) When fast logic meets slow belief. https://pmc.ncbi.nlm.nih.gov/articles/PMC5432582/ and https://link.springer.com/content/pdf/10.3758/s13421-016-0680-1.pdf (a22, a23, b14, b15, d17)
6. [V] Macchi et al. (2019) How to get rid of the belief bias: boosting analytical thinking via pragmatics. https://ejop.psychopen.eu/index.php/ejop/article/download/1794/1794.pdf/ (a27-a29, d06, d07)
7. [V] Pennycook, Cheyne, Koehler, Fugelsang (2013) Belief bias during reasoning among religious believers and skeptics. https://link.springer.com/content/pdf/10.3758/s13423-013-0394-3.pdf (b17)
8. [V] Markovits, Brisson, de Chantal, Thompson (2017) Interactions between inferential strategies and belief bias. https://link.springer.com/content/pdf/10.3758/s13421-017-0723-2.pdf (b18)
9. [V] Strength and activation level of belief in belief-biased reasoning (2024, Psychonomic Bulletin and Review). https://link.springer.com/content/pdf/10.3758/s13423-024-02461-z.pdf (b19)
10. [V] Revlin, Leirer, Yopp, Yopp (1980) The belief-bias effect in formal reasoning. https://link.springer.com/content/pdf/10.3758/BF03213778.pdf (b20)
11. [V] Singmann and Kellen (2014) Concerns with the SDT approach to causal conditional reasoning. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4030140/ (a20)
12. [V] Trippas, Verde, Handley, Roser, McNair, Evans (2014) Modeling causal conditional reasoning data using SDT. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00217/pdf and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3950845/ (a21, b10; partial read)
13. [V, abstract page] Dube, Rotello, Heit (2010) Assessing the belief bias effect with ROCs. https://pubmed.ncbi.nlm.nih.gov/20658855 (a13); [M] https://doi.org/10.1037/a0019634 (b11)
14. [V, abstract page] Dube, Rotello, Heit (2011) The belief bias effect is aptly named. https://pubmed.ncbi.nlm.nih.gov/21244191 (a14)
15. [V, abstract page] Klauer and Kellen (2011) Reply to Dube, Rotello, Heit. https://pubmed.ncbi.nlm.nih.gov/21244192 (a15); [M] https://doi.org/10.1037/a0020698 (b12)
16. [V, abstract page] Heit and Rotello (2014) Traditional difference-score analyses of reasoning are flawed. https://pubmed.ncbi.nlm.nih.gov/24462712 (a16)
17. [V, abstract page] Trippas, Handley, Verde (2013) The SDT model of belief bias. https://pubmed.ncbi.nlm.nih.gov/23565791 and https://researchers.mq.edu.au/en/publications/the-sdt-model-of-belief-bias-complexity-time-and-cognitive-abilit/ (a17, d27; b07 [M])
18. [V, abstract page] Ball, Phillips, Wade, Quayle (2006) Eye-movement evidence for selective processing models. https://pubmed.ncbi.nlm.nih.gov/16610275 (a31)
19. [V, abstract page] Garnham and Oakhill (2005) Comment on Klauer, Musch, Naumer. https://pubmed.ncbi.nlm.nih.gov/15783296 (a12)
20. [V, abstract page] Evans, Handley, Bacon (2009) Reasoning under time pressure. https://researchers.mq.edu.au/en/publications/reasoning-under-time-pressure-a-study-of-causal-conditional-infer/ (d26)
21. [V (secondary: Hilscher 2014 PhD thesis, used for the 1943-2009 history and for Evans and Pollard, Newstead, Oakhill, Polk and Newell, Thompson, Reverberi, Evans et al. 1994, De Neys, Gilinsky and Judd, Stupple and Ball 2007)] https://utoronto.scholaris.ca/bitstreams/8dbe32a6-240f-4ef9-b729-b0a04afed60e/download (a05-a11, a24-a26, a30, a32, a34, a35)
22. [M] Evans and Curtis-Holmes (2005) Rapid responding increases belief bias. https://doi.org/10.1080/13546780542000005 (a37, b16)
23. [M] Newstead, Pollard, Evans, Allen (1992) The source of belief bias effects in syllogistic reasoning. https://www.doi.org/10.1016/0010-0277(92)90019-E and https://research.leedstrinity.ac.uk/en/publications/the-source-of-belief-bias-effects-in-syllogistic-reasoning/ (a36, d08)
24. [M] Evans, Handley, Harper (2001) Necessity, possibility and belief. https://researchers.mq.edu.au/en/publications/necessity-possibility-and-belief-a-study-of-syllogistic-reasoning/ (d09)
25. [M] Klauer, Musch, Naumer (2000) On belief bias in syllogistic reasoning. https://doi.org/10.1037//0033-295x.107.4.852 (b13; also a11 secondary)
26. [M] Trippas, Verde, Handley (2014) Using forced choice to test belief bias. http://hdl.handle.net/10026.1/9936 (b24)
27. [M] Trippas, Pennycook, Verde, Handley (2015) Better but still biased. https://doi.org/10.1080/13546783.2015.1016450 (b25)
28. [M] Howarth (2015) Believe it or not (Plymouth thesis). https://pearl.plymouth.ac.uk/psy-theses/80 (d20)
29. [V, secondary web page, unreliable cell values] Wikipedia, Belief bias. https://en.wikipedia.org/wiki/Belief_bias (a33; cell values corrected by the critique)

### Language-model literature

30. [V] Lampinen, Dasgupta, Chan et al. (2024) Language models show human-like content effects on reasoning tasks (PNAS Nexus). https://arxiv.org/pdf/2207.07051 (b21-b23, c01-c04, c25)
31. [V] Bertolazzi, Gatt, Bernardi (2024) A systematic analysis of large language models as soft reasoners. https://arxiv.org/abs/2406.11341 (c05-c07; table columns garbled in places)
32. [V] Eisape et al. (2024) A systematic comparison of syllogistic reasoning in humans and language models. https://arxiv.org/pdf/2311.00445 (b27, c08, c09)
33. [V] Ando et al. (2023) Evaluating LLMs with NeuBAROCO. https://arxiv.org/html/2306.12567v1 (c10)
34. [V] Ozeki et al. (2024) Exploring reasoning biases in LLMs through syllogism: NeuBAROCO. https://arxiv.org/pdf/2408.04403 (b26, c11, c26, d25)
35. [V] Valentino et al. (2025) Mitigating content effects through fine-grained activation steering. https://arxiv.org/html/2505.12189v3 (c12, c13, c27)
36. [V] Bertolazzi et al. (2025) How language models conflate logical validity with plausibility. https://arxiv.org/html/2510.06700v2 and https://arxiv.org/pdf/2510.06700 (c14, c15, d18)
37. [V, abstract page] SemEval-2026 Task 11 overview. https://aclanthology.org/2026.semeval-1.450/ (c16, c24 [M])
38. [V] Kartac et al. (2026) UFAL-CUNI at SemEval-2026 Task 11. https://arxiv.org/pdf/2605.04941 (c17, c18, d13)
39. [V, abstract page] Kim, Valentino, Freitas (2025) Reasoning circuits in language models. https://arxiv.org/abs/2408.08590 and https://arxiv.org/pdf/2408.08590 (c19, d28)
40. [V, abstract page] Ranaldi, Valentino, Freitas (2025) Quasi-symbolic abstractions (QuaSAR). https://arxiv.org/abs/2502.12616 (c20)
41. [V, abstract page] Seals and Shalin (2024) Evaluating the deductive competence of LLMs. https://arxiv.org/abs/2309.05452 (c21)
42. [V, abstract page] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 and https://arxiv.org/pdf/2310.15164 (c22, d15)
43. [M] FregeLogic at SemEval-2026 Task 11 (Amazon Science PDF, search snippet). https://cdn.amazon.science/03/34/b09b548943b0b8133b7ddf680e9e/scipub-approval152129-46100782-fregelogic-at-semeval-2026-task-11-a-hybrid-neurosymbolic-architecture-for-contentrobust-syllogistic-validity-prediction.pdf (c23)
44. [V] Akinfaderin and Diallo (2026) FregeLogic. https://arxiv.org/pdf/2604.18328 (d10-d12)
45. [V] Poddar, Sahoo, Ghosh (2025) Understanding syllogistic reasoning in LLMs from formal and natural language perspectives. https://arxiv.org/pdf/2512.12620 (d01, d02)
46. [V] Noe et al. (2025/2026) BIS Reasoning 1.0. https://arxiv.org/pdf/2506.06955 (d03, d04)
47. [V] Clark, Dalvi Mishra, Tafjord (2024) BaRDa. https://arxiv.org/pdf/2312.07527 (d05)
48. [V] Muhamad et al. (2026) ITLC at SemEval-2026 Task 11. https://arxiv.org/pdf/2603.02676 (d14)
49. [V] Ryu et al. (2025) CLOVER. https://arxiv.org/pdf/2410.08047 (d16)
50. [V, abstract and introduction] Maraia et al. (2026) Abstract activation spaces for content-invariant reasoning. https://arxiv.org/pdf/2602.02462 (d19)
51. [V] HABIB_TAZ at SemEval-2026 Task 11. https://arxiv.org/pdf/2607.14349 (d29)
52. [M] Search log for gaps 1, 2, 4, 5, 6, 10 (arXiv API, OpenAlex, WebSearch). https://export.arxiv.org/api/query (d30)
