# Mental models theory: deep document

Subfield: reasoning by building models of possibilities (Johnson-Laird, Byrne, Khemlani, Ragni and others).
Parent field: A01, cognitive psychology of thinking and reasoning.
Written for the single-agent thinking schema (`research_notes/single_agent/SCHEMA.md`, v0.2).
Built only from the evidence files in this folder: `evidence_a-d.jsonl` (a01-a27, b01-b29, c01-c32, d01-d28),
`claims.jsonl` (K01-K33) and `critique.md`. Evidence ids are given in brackets, for example [a04]. Claim ids are K-numbers.

Status marks used here: **[E]** established, **[S]** single source, **[C]** contested. A claim marked [E] can still be
established for people only. Where this matters it is said in the text.

Three warnings that apply to the whole document:

1. Almost all human data come from one network of labs (Johnson-Laird, Khemlani, Ragni and their students). Sources
   outside that network: Eisape et al., Bertolazzi et al., Singmann et al., Dames et al., Espino et al., Sable-Meyer and
   Mascarenhas, Ghasemi et al., Oberauer, Newstead, and the Oxford erotetic group. "Independent" counts in this document
   are weak.
2. The LLM evidence is from 2023-2024 chat models, open models up to 70B, and one 38-model set. No study was found on
   current frontier or reasoning models with Johnson-Laird's own illusion items [c31, d28]. That is a negative search
   result, not proof.
3. Dates and models change fast. Anything here that is about LLM behaviour must be re-measured on our model.

---

## 1. What it is

Mental models theory says that people reason by building small, iconic mental pictures of the possibilities that a set
of statements allows, and by reading conclusions off those pictures. A conclusion is *necessary* if it holds in all the
models, *possible* if it holds in at least one, and *probable* if it holds in most [a01]. The theory's key claims are
that models are kept small because working memory is limited, that a model represents only what is true (the principle
of truth), and that people search for counterexamples (models where the premises hold and the conclusion fails) only
sometimes. These claims predict what is easy (one model), what is hard (many models), and a special class of confident,
systematic errors called illusory inferences. The theory has working computer programs, the main one being mReasoner.
For our agent the useful parts are code-checkable: enumerate the possibilities, count the models, search for a counter-model.
The human-psychology parts mostly do not transfer (section 9).

---

## 2. History and theories in depth

### 2.1 Who and when

Background not taken from the evidence files (stated from general knowledge, not opened this session): the idea of a
"small-scale model" in the head goes back to Craik (1943). Johnson-Laird's book *Mental Models* (1983) and Johnson-Laird and
Byrne's *Deduction* (1991) set out the modern theory. Rival families at the time were formal-rule theories (Braine, Rips)
and pragmatic-schema theories. Treat this paragraph as orientation only.

From the evidence files:

- **1978.** Johnson-Laird and Steedman gave 20 Columbia students the syllogism set. Later modelling still fits these data
  [b16, d18]. That sample gave "nothing follows" on 45% of items, against 30% in the meta-analysis (z=6.19, p<.001) [b16, d18].
- **1989.** Byrne showed that valid conditional inferences can be suppressed by added background content. Modus ponens fell
  from 96% to 38% when an extra requirement was added (N=24) [a20]. This became the model-theory account of how premises
  are turned into models: interpretation comes first.
- **1996-1999.** Johnson-Laird and Savary discovered illusory inferences: inferences that feel obvious, are drawn with
  high confidence, and are wrong [a01-a05, b01-b05]. This is the theory's best novel prediction, because rival theories
  did not predict a systematic error.
- **1999.** Bucciarelli and Johnson-Laird studied syllogism strategies with paper, think-aloud and cut-out shapes [a17, a18].
  Johnson-Laird and colleagues published naive probability theory: people count equiprobable models of what is true [a12-a14].
- **2000.** The antidote papers: Yang and Johnson-Laird (quantified illusions and a fix), Goldvarg and Johnson-Laird (modal
  illusions), Santamaria and Johnson-Laird (framing effects) [a06, a07, d03-d06].
- **2005.** Goodwin and Johnson-Laird on relational reasoning (transitive, pseudo-transitive, non-transitive) [a19].
- **2008-2009.** Khemlani and Johnson-Laird showed illusions with pure embedded disjunctions, which answered the objection
  (from Rips) that illusions come from misreading "if" [a08, a09, b06, b07, d07].
- **2010-2012.** PNAS summary of the theory [a10]. The syllogism meta-analysis found no theory adequate [a15, a16, b15].
  Probabilities of unique events [b26, d19].
- **2014.** Set-membership inferences [a24].
- **2016-2022.** mReasoner: a unified program with four parameters [b16, b17, a22, a23, c26].
- **2018.** Meta-analysis of 228 selection-task experiments [b20]. Ragni and Johnson-Laird on possibility reasoning [a21, b27].
  A one-week retest of syllogisms [b18].
- **2019.** Meta-analysis of conditionals (39 experiments, 2378 participants) [b21]. Position paper on why machines do not yet
  reason like people [c24].
- **2021.** An independent-lab retest [b19, d10]. An independent-lab replication of the disjunction illusion [d24].
- **2023-2026.** LLM studies begin: GPT-3 to GPT-4 on erotetic-theory items [c07, c08, d02]; PaLM 2 on all 64 syllogisms [a26, b25, c01, d12];
  open models on syllogisms and content effects [a27, b24, c06, d13]; 38 models on disjunction fallacies [d01]; conditional and modal
  reasoning in 25-29 LLMs [c02, d17].
- **2024.** The most recent human replication of a conditional illusion, Espino et al. (N=80, Spanish) [d08].

### 2.2 The main claims, in order of how much they matter for us

1. **Possibilities, not rules.** Reasoning is manipulating sets of possibilities, not applying formal inference rules [a10, c24].
2. **Parsimony.** Reasoners prefer one model, because working memory is limited. Most frequent conclusions are those that fit a
   single model [a25]. mReasoner finds that models of about 2 to 4.5 tokens fit people, and that dozens of models do no better [a23].
3. **Principle of truth.** A model represents what is true in a possibility, not what is false. Implicit models stand for
   "other possibilities exist". From this follow illusions: a conclusion that is true in the explicit models but wrong when the
   false cases are made explicit [a01, a04].
4. **Difficulty follows the number of models.** One-model problems are easy, multiple-model problems are hard [a17, a19, a24]. There is
   one boundary: for embedded disjunctions, model count alone does not explain difficulty [a09].
5. **Counterexample search is the control point.** Good reasoners deliberately look for a counter-model. Poor reasoners stop at the first
   model [a10, a22, b17, b29]. A believable conclusion tends to stop the search, an unbelievable one starts it [a10].
6. **Content and knowledge shape the models.** Byrne's suppression effects [a20], belief bias [a10, b29], and the fact that background
   knowledge can block a formal inference [c09].

### 2.3 How the rival theories differ

| Theory family | Core claim | Where it differs from mental models | Evidence in our files |
|---|---|---|---|
| Formal rules (Braine, Rips and others) | People apply inference rules in a mental logic | Predicts no systematic fallacy of the illusion type. Rips raised two rivals: "or else" read as "and", and a programming-language reading of "else" | The authors answer with a rubric test and a no-conditional version (disjunctions only, N=40); the illusion stayed [a05, b03, b04, b05, a08]. The rival refutations are made by the theory's authors. |
| Heuristic theories (atmosphere, matching, PHM, conversion) | Fast surface rules give syllogism answers | No model construction at all | Aggregated model-based theories 76% vs heuristic 66% [a15]. Atmosphere predicts LLM errors very well (92.31% / 82.97% / 62.79%) [a27, b24, c06]. Matching heuristics explain related logic effects, below chance when matching and logic disagree (N=409) [d25]. |
| Probabilistic (Oaksford et al.) | Conditional inference is probabilistic | Treats the four conditional inferences as independent choices | Response patterns across 39 experiments are more redundant than independent-choice simulations [b21]. Oberauer (2006) found a probabilistic theory did worse than a modified model theory (abstract only) [b22]. |
| Erotetic theory (Koralus and Mascarenhas) | Premises are questions; reasoning keeps maximally strong answers | A sibling. It also predicts illusions, and says the illusion can arise without exact word matching in the model-theory sense | Authors of the model theory call it "a variant" [b13]. An independent lab found the disjunction illusion is triggered by knowledge links, not only matching, against both theories' exact matching step [d24]. |
| Credulous vs skeptical (Stenning and van Lambalgen) | Interpretation choice drives errors | Not a possibility-model account | Listed as a rival; not tested here [b13]. |
| Suppositional / exclusive suppositional | Conditionals are evaluated by supposition | Wins on one task type in the conditional meta-analysis | In 39 experiments, models won for production, a directional variant for evaluation, exclusive suppositional for choosing among options. No single winner [b21]. |
| Dual-process variants | Fast model, slow check | Add a System 2 | mReasoner builds this in: System 1 builds and scans one model, System 2 searches for counterexamples [a22]. Oberauer found model theory holds up with directionality and dual process added [b22]. |

Take-away: no theory wins everywhere. The syllogism meta-analysis ends with "none of the above" [a15]. The conditional meta-analysis
finds the winner depends on the task format [b21]. This is why section 7 takes procedures, not claims about truth.

---

## 3. Core findings with exact numbers

Status is the claims-file status (K-number). "Human only" means no LLM test exists. N is per experiment.

| # | Finding | Numbers | Source | Status |
|---|---|---|---|---|
| 1 | Probability illusion, cards (Exp 1) | N=24 Princeton. Controls 71% correct, illusions 17%. 20 of 24 better on controls, 2 ties, p<.001. 21 of 24 picked an impossible card at least once | Johnson-Laird and Savary 1996 [a02] | K01 [E], human |
| 2 | Probability illusions across connectives (Exp 2) | N=20. Illusions 13% correct, controls 64% (T=1, n=18, p<<.005). 17 of 20 worse on illusions. Two-model controls 52% vs one-model 83%. Only 56% of illusion responses matched the exact prediction | 1996 [a03] | K01 [E], human |
| 3 | Core illusion, conditionals | N=16. 100% of conclusions on illusions were the predicted invalid one. Controls 88% and 100%. Confidence 4.4 vs 4.3 of 5. All 16 better on controls | Johnson-Laird and Savary 1999 Exp 1 [a04, b01] | K01, K02 [E] |
| 4 | Same, web sample | N=20. 15 of 20 gave the illusory "there is an ace", 5 said indeterminate. 15 right on control | 1999 Exp 2 [b03] | K01 [E] |
| 5 | Illusion without conditionals | N=40. Illusion 1: 85% fallacy. Illusions 3 and 4: 63% and 68%. Control 98% correct. 33 of 40 drew an illusory conclusion and passed control | 1999 Exp 3 [b04] | K01 [E] |
| 6 | Modal illusions | N=20 (Exp 1). Controls 91%, illusions 15%. Exp 2: controls 79%, illusions 22%. Confidence 4.17 vs 4.24 | Goldvarg and Johnson-Laird 2000 [d03, d04] | K01, K02 [E] |
| 7 | Quantified illusions | N=20 each. Controls 90% vs illusions 54% (Exp 1); 93% vs 51% (Exp 2). Illusions of impossibility much weaker (about 54% pooled) | Yang and Johnson-Laird 2000a [a06, b08] | K01 [E], human |
| 8 | Embedded disjunction illusions | Exp 1 N=18: illusions 17% and 22% correct, controls 100% and 78%. Exp 2: controls 95%, illusions 19%. Exp 3 (yes/no format): controls 81%, illusions 63% | Khemlani and Johnson-Laird 2008/2009 [a08, b06, d07] | K01 [E] |
| 9 | Conditional illusion replicated, Spanish lab | N=80. Controls 83% vs illusions 6% correct (z=7.82, r=.87). Illusory answer "ace" 69% (if-then); "only if" shifts to "may or may not" 64%. Confidence 3.9 vs 4.0. Exp 3: 68% vs 30% (r=.64) | Espino et al. 2024 [d08] | K01 [E], partly independent |
| 10 | Disjunction illusion replicated, independent lab (Paris) | Exp 1 analysed N=64: valid control accepted 87%, invalid control 26%; link strength predicts target acceptance (slope .97, R2=.9, 7 items). Exp 2 N=70: 90% and 20%; slope .69, R2=.58 | Sable-Meyer and Mascarenhas 2021 [d24] | K01, K32 [E] |
| 11 | Confidence does not flag illusions | 4.4 vs 4.3 (5-pt); 4.17 vs 4.24; 3.9 vs 4.0; 5.45-6.26 of 7, no reliable differences | [a04, d03, d04, d07, d08] | K02 [E], human only |
| 12 | Illusion size depends on framing and format | Physical vs logical disjunctions 84% vs 19% correct; yes/no format 63% vs 19% in open choice; co-reference: illusions 10% vs controls 78% (N=35) | Santamaria and JL 2000, K&JL 2009, Walsh and JL 2004 [d06, d07, d09] | K20 [S] |
| 13 | Prose warning or rubric does not remove illusions | Tricky-warning slowed people, fallacies stayed (no counts). Rubric "one true, one false": 15/20 still fell | [a05, b02, b03] | K03 [S] |
| 14 | Two-case procedure helps but costs | One-case: illusions 33 to 65%, controls 93 to 79% (z=3.27, 2.31). Two-case: illusions 39 to 71%, controls 87 to 72% (z=3.72, 1.99); gap gone (z=0.44) | Yang and JL 2000b [a07, b09, b10, d05] | K04 [C], K21 [S] |
| 15 | Check instruction in modal task | Exp 3 N=20 in two groups. Second half, illusions: help 71%, no help 30% (U=10, p<.002). Possibility illusions 0% to 57% in the help group | Goldvarg and JL 2000 [d04] | K03 [S] |
| 16 | Embedded-disjunction instruction | Group difference n.s. (z=1.7, p=.09); gap smaller when instructed (z=2.2, p<.05). Gap 34 vs 79 points in block 2 | [b07, d07] | K03 [S] |
| 17 | Model count drives difficulty (syllogisms) | One-model 80% vs multiple-model 21% vs no-valid-conclusion 50% (N=20) | Bucciarelli and JL 1999 [a17] | K05 [E] |
| 18 | Model count (set membership) | 92% vs 51% (z=3.21, Cliff's delta .56); only one-vs-multiple was a significant predictor (b=3.31, SE .42) | Khemlani, Lotstein, JL 2014 [a24] | K05 [E] |
| 19 | Model count (relations) | Transitive 98%, pseudo-transitive 72%, non-transitive 8%. Second-order 84% vs third-order 56% (z=3.00). Shallow vs deep 91% vs 93% | Goodwin and JL 2005 [a19] | K05 [E] |
| 20 | Exception: embedded disjunctions | 3-model illusions 17-22% correct; 4-model controls 78-100% | [a09] | K05 boundary |
| 21 | Refuting conclusions with cut-outs | 19 people. Correct refutation 59%, correct "cannot refute" 71%. One-model 71%, multiple-model 70%, no-valid-conclusion 50% | Bucciarelli and JL 1999 Exp 3 [a18] | K06 [E] |
| 22 | Syllogism theories meta-analysis | 6 datasets, N=156. Hits: mental models 95%, verbal 63%. Correct rejections: conversion 93%, verbal 90%, mental models 74%. Overall: verbal 84%, mental models 78%. Model-based 76% vs heuristic 66%. Verbal I2=52% | Khemlani and JL 2012 [a15, b15] | K08 [C] |
| 23 | Syllogism difficulty is stable | Kendall's W=.86 (27 valid), .64 (37 invalid) over six studies. Easiest valid 90%, hardest valid 1%. Easiest invalid 76%, hardest 12%. Entropy vs accuracy r=-.52 | [a16] | K07 [E] |
| 24 | mReasoner fit | Aggregate r=.80, RMSE=.13 (meta-analysis fit r=.82 in 2016). Individuals: mean best fit r=.70. Groups r=.78, .83, .91. Poor group size 2.0, search .4; best group size 4.5, search .8, reconclude .6. Kendall W=.28, p=.33 for parameter concordance. Set membership: search .58, R2=.75 | [a22, a23, b16, b17, d18, a24] | K09 [S], in-sample |
| 25 | Practice gain, small retest | N=20. 58% to 68%, 19 of 20 improved, 27.5 changes per person, 95.9% kept polarity | Ragni et al. 2018 [b18] | K10 [C] |
| 26 | Practice gain, larger retest | N=100. Overall 50.1% to 52.7%. Valid 55.5% to 60.3%, invalid 46.1% to 47.2%. Slope significant only for valid items in session 1; fewer NVC answers | Dames, Klauer, Ragni 2021 [b19, d10] | K10 [C] |
| 27 | Conditional suppression | N=24 (8 per group). Modus ponens 96% simple vs 38% additional requirement; modus tollens 92% vs 33%; denial of antecedent 46% vs 4% (alternative); affirmation of consequent 71% vs 13% | Byrne 1989 [a20] | K11 [S] |
| 28 | Conditional meta-analysis | 39 experiments, 15 studies, 2378 people. Patterns more redundant than 10,000 independent-choice simulations | Ragni, Dames, JL 2019 [b21] | K17 [C] |
| 29 | Possibility judgments | Exp 1 N=53: 80% of model-theory predictions vs 56% for modal logic K (z=6.1); r2 .99 vs .01. Exp 2 N=51: 83% vs 50%. Exp 3 N=50: where they differ, Yes 89%, No 76% in the theory's favour | Ragni and JL 2018 [a21, b27] (corrected by critique) | K12 [S] |
| 30 | Naive probability | Biased problems 1.1 of 8 unbiased vs controls 5.6 of 9 (N=25). Subadditivity: "at least A" 60% vs 45%+44%. Unique-event conjunctions violate the joint distribution on 56% of trials (N=39); 34% verbal vs 68% numeric (N=18) | [a12, a13, b26, d19] | K13 [E] |
| 31 | Selection task meta-analysis | 228 experiments (99 with all 16 selections). Mean informativeness 2.14 bits of 4. Feedback moves choices toward counterexamples | Ragni and Kola 2018 [b20] | K14 [E] |
| 32 | Counterexample use | Correct rejection 92% (inconsistent) vs 74% (merely consistent). Counterexample use 51% vs 21% | Cited in Johnson-Laird 2010 [a11] | K14 [E], second-hand |
| 33 | Fluency of valid conclusions | Replicated, then vanished once content was randomised across valid and invalid | Singmann et al. 2014 [b23] | K16 [S], failed replication of a spin-off |
| 34 | "Model method" training | Reported 95% vs 63%, 15 s vs 24 s after 2 minutes. 2012 text: 65% to 95%, 25 s to 15 s. Unpublished 1999 thesis, no N | [b28, d11] | K15 [C], do not quote |
| 35 | Spatial models vs plain logic | 4 datasets (N=33, 30, 49, 51). Best model 71.9-79.1%; transitive closure 73.4-75% | Ragni, Brand, Riesterer 2021 [c25] | K29 [S] |

Corrections carried over from the critique: the "89% yes, 76% no" modal figures belong to Exp 3, not Exp 2; Exp 2 N is 51, not 50;
for Khemlani and Johnson-Laird do not quote a single "instructed accuracy" number from the 2008 version, use the 2009 text [d07];
b11's "57%" is one table cell (possibility illusions after the check), the overall figure is 71% [d04].

---

## 4. Mechanisms and formal or computational models

This section is written so an engineer can implement it. It separates what the sources say from our own design.

### 4.1 Representation

- A **mental model** is one possibility: a set of tokens, each token standing for an entity or a true atomic fact.
  Example: "A or B (exclusive)" has models `{A}` and `{B}`. Inclusive "A or B" has `{A}`, `{B}`, `{A,B}` [a25].
- A **possibility set** is the list of models of one premise. Premises are combined by pairing models and dropping contradictions.
- **Principle of truth** [a01, a04]: by default, a model lists only what is true in that possibility. What is false is not written.
  A fully explicit model also lists the false atoms.
- **Implicit models**: the ellipsis `...` stands for "other possibilities exist, not yet spelled out" [a01].
- **Modal readout** [a01]: necessary = holds in all models. Possible = holds in at least one. Probable = holds in most.
- **Naive probability** [a12]: with no other information, treat each model as equiprobable. P(event) = share of models containing it.
  Two principles: P1, a proper subset of models is less probable (sound). P2, more models means more probable (risky, needs equiprobable models) [a01].
  Biased results appear when the models the reasoner builds differ from the fully explicit ones [a13].

### 4.2 Conditional and disjunction handling (from the examples in the sources)

- "If A then B" initially gets models `{A,B}` and `...`. Fully explicit: `{A,B}`, `{not A, B}`, `{not A, not B}`. "Only if" and "if and only if" change the models,
  and so change the illusory answer [d08].
- Content changes which models exist. Byrne's additional requirement adds a possibility where A holds and B does not, so modus ponens is withdrawn;
  an alternative cause adds a possibility where B holds without A, so affirmation of the consequent is withdrawn [a20].

### 4.3 Worked example of an illusion (so the failure is concrete)

Premises: "If king then ace, or else if not king then ace. There is a king." What follows? [a04]

- Principle-of-truth reading: both conditionals give `{king, ace}` and `{not king, ace}`. Whatever happens, there is an ace. Everyone says "ace".
- Fully explicit reading: "or else" means exactly one conditional is true. Take the king as given. The second conditional (if not king then ace) is then vacuously true.
  So the first must be false, so king and not ace. The premises force **no ace**.
- Why people fail: they represent the true cases of each conditional and forget what it means for the other to be false.

Card example from 1996 [a02]: "Only one is true: king or ace or both; queen or ace or both. Which is more likely, king or ace?"
Most say ace. Truth: with an ace in the hand, both statements would be true, which breaks "only one is true". So ace is impossible.

### 4.4 The case-table procedure (the antidote)

From the antidote papers [a07, b09, b10, d05]: for "only one premise is true", work out (1) premise 1 true and premise 2 false, then (2) premise 2 true and premise 1 false.
Combine the resulting possibilities. Engineer's version (our design, not in the sources):

```
def case_table(premises):            # premises: list of boolean formulas, "exactly one true"
    rows = []
    for i, p in enumerate(premises):
        # case i: premise i true, all others false
        rows.append({"true": p, "false": [q for j, q in enumerate(premises) if j != i]})
    return rows                      # code builds rows; model fills what each row implies
def possibilities(rows, atoms):      # code enumerates truth assignments consistent with each row
    return [a for a in all_assignments(atoms) if any(consistent(a, r) for r in rows)]
def verdict(conclusion, poss):       # necessary / possible / impossible, by the modal readout
    vals = [conclusion(a) for a in poss]
    return "necessary" if all(vals) else "possible" if any(vals) else "impossible"
```

Human result for this procedure: 33 to 65% and 39 to 71% on illusions, but controls fell 93 to 79 and 87 to 72, and about 29% error stayed [d05]. The model-theory
reason it is only a partial fix is that people must still hold and combine the cases.

### 4.5 mReasoner (the main implementation) [a22, a23, b16, b17, c26, d18]

Two systems:

- **System 1.** Build one small model from an intensional representation of the premises, then scan it with heuristics for a conclusion.
- **System 2.** With some probability, search for counterexamples by three moves: **add** a token, **split** an individual, **swap** properties.
  If a counterexample is found, revise: possibly weaken the conclusion to a safer one, or say "nothing follows".

Four parameters:

| Parameter | Meaning | Values seen |
|---|---|---|
| LEN / size | how many entities in the model (left-truncated Poisson, mean below 6) | 2.0 (poor group) to 4.5 (best group); other fits above 4.0 |
| BROAD / atypicality | how often atypical (non-default) entities are added | best below .5 |
| SYSTM2 / search | probability that the counterexample search runs | .4 poor, .8 best, .58 set membership |
| WEAKEN / reconclude | probability of weakening a refuted conclusion | .6 in both extreme groups |

Fit: aggregate r=.80, RMSE=.13; individuals mean r=.70; 4 free parameters against 576 data cells [b17]. Grid searches: 1,000 settings x 100 runs for 32 immediate inferences;
1,512 settings for syllogism subsets; Eisape et al. ran 1,296 settings of which 923 finished [a23, c01]. Public code (LISP, Mac binary, v0.9.6188, last updated 2017-06-28; GitHub skhemlani/mReasoner) [c26].
Limits: parameters are chosen on the same data (in-sample), the program has no belief or knowledge handling [c26], and individual parameters show no concordance [d18].

Engineer's mapping to the schema (our design): System 1 = S3 first attempt. System 2 = S4/S7 code-run counterexample search. `search` = a budget or trigger, not a fixed rate.
`weaken` = the S7 step that drops to "nothing follows" or to a weaker claim when a counter-model exists.

### 4.6 Counterexample search by construction

Untrained people build counterexamples with cut-out shapes using the same three moves as the program (add tokens, split individuals, swap properties),
but with many more interpretations and search orders [a17, a18]. A code version for quantified premises over a small domain is exact: enumerate all models
over n individuals and check whether any has premises true and conclusion false. The Sphere Neural-Network does this with Euler diagrams: it found all 24 valid syllogisms among 256,
built a counter-model for every invalid one, and handled 3 to 12 terms (up to about 2 minutes at 12 terms) [c19].

### 4.7 Other computational models

- **Spatial.** PRISM, SpatialReasoner variants and VerbalReasoner predict individual answers to spatial relational problems. They add little over a transitive-closure baseline on easy
  problems (71.9-79.1% vs 73.4-75%) and differ only where problems are indeterminate [c25].
- **Possibility-based simulations for modal reasoning.** A possibility-set program fits modal conclusions from non-modal premises closely (no correlation quoted) [c24].
- **Erotetic prompt (LLM version).** "List the premises, turn each into a question, keep the alternatives, then reason step by step" [c08].

---

## 5. What holds up

### 5.1 Replications and independent confirmation

- **Illusions.** The best-attested effect. Independent confirmation: Espino et al. 2024 (N=80, conditional illusion, 83% vs 6%, r=.87, confidence equal) [d08],
  Sable-Meyer and Mascarenhas 2021 (disjunction illusion, controls 87%/90% accepted vs invalid controls 26%/20%) [d24]. The review says no study failed to give a reliable effect [b12],
  but that is the authors' claim, and the 128-person study it cites is the authors' own. Espino et al. are only partly independent (they worked with the same network); Sable-Meyer and Mascarenhas
  are independent but favour a rival account. Tabossi, Rips, Walsh and Koralus originals were not read in full. No meta-analysis of illusions exists in our set.
- **Syllogism difficulty is stable** across six studies (W=.86 and .64) [a16].
- **Confidence fails to flag illusions** in three labs (K02).
- **Model-count difficulty** in syllogisms, set membership and relations (K05), all from one network.

### 5.2 Failures, moderators and boundary conditions

- **The model-theory program over-predicts.** Hits 95% but correct rejections 74%. No theory is adequate [a15, K08].
- **Not every predicted illusion works.** Illusions of impossibility were near 54% pooled and vary by item [a06]. An inclusive-inclusive embedded disjunction illusion was weak (58% correct) [b06].
  Only 56% of illusion responses matched the exact model prediction in one study [a03]. The theory predicts direction better than each answer.
- **Framing.** Physical disjunctions 84% correct vs logical 19% [d06]. Response format: 63% with yes/no vs 19% in open choice [d07]. Co-reference changes rates (10% vs 78%) [d09].
  Human results are not one number (K20).
- **Practice effects.** Small retest: 58 to 68%. Larger retest: gain only on valid items inside session 1, fewer NVC answers, so possibly a response-bias shift rather than deeper checking [b18, b19, d10]. Contested (K10).
- **Failed replication of a spin-off.** The claim that valid conclusions feel more fluent vanished when conclusion content was randomised [b23].
- **Rival explanation for related effects.** Matching heuristics produce the apparent intuitive-logic effect and go below chance when matching and logic disagree (N=409, four experiments) [d25].
  Knowledge links, not only word overlap, drive the disjunction illusion [d24].
- **The "model method" is unverified.** Source: an unpublished 1999 thesis. Johnson-Laird's own two reports give 65 vs 95% and 25 vs 15 s (2012) and 63 vs 95% and 24 vs 15 s (2024). No N, no design, no replication [b28, d11].
- **Pragmatics and item order** controls are not quantified in anything we read (critique gap 6).

### 5.3 Interventions

| Intervention | Result | Status |
|---|---|---|
| Generic warning ("beware, tricky") | Slowed people down, fallacies stayed (no counts) [a05, b02] | not effective, K03 [S] |
| Explicit rubric "one is true, one is false" | 15 of 20 still fell for the illusion [b03] | not effective |
| Check one premise at a time (modal) | Illusions 30% to 71% second half, overall still far from ideal; possibility illusions 57% [d04] | partial, K03 [S] |
| One-case instruction (quantified) | Illusions 33 to 65%, controls 93 to 79% [a07, b09] | partial, with a cost |
| Two-case instruction (quantified) | Illusions 39 to 71%, controls 87 to 72%; gap gone; 29% error remains [b10, d05] | partial, with a cost, K04 [C], K21 [S] |
| Instruction for embedded disjunctions | Group difference n.s. (p=.09), gap shrank (p<.05) [b07, d07] | weak |
| Reframe to physical objects | Illusion accuracy 19% to 84% [d06] | strong but changes content, K20 [S] |
| Yes/no response format | 19% to 63% correct [d07] | format effect |
| Feedback in selection task | Choices move toward counterexamples [b20] | K14 [E] |
| Concrete integer cases ("out of 10 chances") | 53% vs 8% [a14, d21] | second-hand, do not quote |
| "Model method" | 95% vs 63% [b28, d11] | unverified, do not quote |
| Practice, no feedback | small gains, maybe bias shift [b18, b19, d10] | K10 [C] |

Pattern: instructions that change the procedure help partly and cost accuracy on easy items. Generic warnings do nothing. Reframing the content works best but is not general.

---

## 6. Language models

### 6.1 Syllogisms

- **PaLM 2** (Eisape et al.): human accuracy about 50% (139 people, 27 syllogisms with conclusions, 9 answer options), best LM about 75%, scale not steady (largest slightly below second
  largest). Models show the figural effect and the same top human fallacies. On the 37 syllogisms whose correct answer is "nothing follows", model accuracy is near 0%. Zero-shot chain of thought, 30 samples at
  temperature 0.5. mReasoner mapping: first component 77% of variance, loads on the System 2 parameter; with correct answers zeroed it still correlates .6 with SYSTM2. Llama 2 is about human level overall but fails easy items [a26, b25, c01, d12].
- **Open models** (Bertolazzi et al.): LLaMA-3 70B 58.89% on valid vs human 44.63%; correlation .80 with human difficulty. Invalid items: 70B base 10.28%, 70B instruct 32.50%, 8B instruct 30.28%.
  The atmosphere heuristic predicts 92.31% of correct valid answers and 82.97% (invalid) / 62.79% (valid) of errors. In-context examples did not teach "nothing follows" and made models more self-contradictory;
  supervised fine-tuning fixed it (near ceiling, 0.31% contradictory) [a27, b24, c06, d13]. Fine-tuning is training, so out of scope for us.
  More premises lowers zero-shot CoT accuracy [c06].
- **Existential import.** Larger and "thinking" models drift toward modern logic (abstract-level) [d15]. The answer key must state the convention (K23).
- **Belief bias in 2025 models.** 14 models, 160 items, validity judgement task: mean belief bias +10.81 pp (p=.028, d=0.66), 12 of 14 positive, top models under 2 pp, worst +46.9 pp; correlation of ability and bias -0.565 [d14].
  Ten open models (2025-26): all content effects shrink with chain of thought, all above 89% accuracy [d22]. Open 2024 models lose 8-40% on valid unbelievable items; the largest instruct model does not [d13].
  Human-like content effects appear in Chinchilla, PaLM 2, GPT-3.5 and are stronger on harder tasks [c05].
- **Euler-diagram checker.** GPT-3.5 best 80% at 3 terms falling to 51.67% at 12 terms; GPT-4o 95.83% best and 89.17% at long chains; the checker 100% [c19].

### 6.2 Illusions and disjunction fallacies

- GPT-3, 3.5 and 4 (March 2023, chat interface, one sample per item, 61 mixed problems): human-style fallacious outputs 18%, 33%, 34%; ETR-predicted outputs 59%, 77%, 75%; correct inference 49%, 61%, 72%.
  An example: GPT-4 concluded Jane is looking at the TV [c07, d02].
- 38 models, 383 generated fallacy problems: mean correct 40.6% (min 16.7, median 31.0, max 91.7). Correctness vs Arena Elo r=0.004 (p=.981). Share of wrong answers that are the predicted fallacy rises with Elo (Spearman .36, p=.0265).
  Reversing premise order blocked the fallacy in 46.15% (chatgpt-4o-latest), 68.00% (gpt-4.5-preview), 37.27% (gemini-2.5-flash-preview), 38.78% (deepseek-chat-v3-0324) of cases [d01].
- No test with Johnson-Laird's own materials, matched controls, human rates on the same items, or a confidence/self-consistency measure [c31, d28].

### 6.3 What changed behaviour, and by how much

| Change | Effect | Source | Note |
|---|---|---|---|
| Erotetic prose prompt, GPT-3.5 | fallacies blocked 14/17 vs 4/17 (p=.0045) | [c08] | only items that had already failed were retested, regression to the mean possible |
| Same prompt, GPT-4 | 7/19 vs 8/19 (p=.77) | [c08, d02] | no gain over a plain step-by-step control |
| Same prompt, GPT-3 | 4/8 vs 4/8 | [c08] | |
| Reverse premise order | 37-68% of fallacies blocked | [d01] | four models |
| Chain of thought on modal and conditional patterns | +0.2 to +21.5 points zero-shot CoT; few-shot -8 to +12.5 | [c02] | nearly all models still accept two invalid modal patterns |
| CoT or symbolic translation on rulebreakers | raised ordinary accuracy, lowered rulebreaker accuracy | [c09] | rulebreaker paired accuracy 0.0022 to about 0.3; best of 7 under 0.7 |
| Prompt rewording and premise prefixes on rulebreakers | up to +24.13 (gemma-2-27b); range 31.27 to 69.12 | [c09] | no model passed 69% |
| Flag-and-reason for belief-conflicting premises | gap 14% to 7%, overall +4% (11 models) | [c22] | |
| Premise reordering (reduction measured, not a fix) | accuracy drop over 30% (GPT-4-turbo, GPT-3.5, PaLM 2-L, Gemini 1.0 Pro) | [c13] | 2023-24 models |
| Solver feedback "wrong" only (syllogism satisfiability, 256 tasks) | gpt-3.5 47.27% to 56.64%; gpt-4o 77.39% to 80.01%; 111 and 51 tasks never solved | [c20] | feedback was only a verdict |
| Solver counterexample in planning | GPT-4 alone 19/20 at 3 blocks and 2/20 at 10 blocks; counterexample loop improves | [c23] | iteration table not extracted |
| Visualization of Thought (grid state after each step) | +23.5 over no-visualization; 87.1% vs 57.4% tracking; but CoT 52.5 vs VoT 49.5 on ring navigation (N=200) | [c12] | grid worlds |
| Self-built cognitive map before reasoning (VLM) | 40.48% to 41.43% frozen; fine-tuned 57.8%; given map 32.00% (worse) | [c10] | images, tiny model, gain is mostly training |
| Disagreement-triggered verification | 82.1% at 0.592K tokens vs 80.0% at 1.458K always-on, vs 79.8% at 1.732K self-consistency | [d23] | non-logic tasks; misses uniform errors |
| Scaffolding the successful structure | up to +66.7% on some ill-structured types; losses up to -72.0% for small models | [c21] | about 50 problems per cell |
| Menu of thinking tools ("MeMo") | +6.0 (StrategyQA, GPT-4), +10.2 (Figure of Speech) | [c18] | different meaning of "mental model"; does not support Johnson-Laird |

### 6.4 Other LLM patterns

- Models do not spontaneously enumerate possibilities. Symbolic (truth-table) strategy is rare. Llama-2-70B reasoned soundly in 31.7% of cases [d16]. Models rarely answer "nothing follows" [K06, K22].
- Models read premises well (GPT-4 translation to predicate logic 87/90 English, 86/90 Japanese) but fail at the inference step; neutral items are about 30 points harder [c03].
- Premises that contradict world knowledge cost an average of 14% across 11 models [c22]. Rulebreakers: rigid rule application beats knowledge [c09].
- LLM probability judgements are incoherent in human-like ways (GPT-4, GPT-3.5, LLaMA-2; 24 event pairs) [d20].
- Spatial: most models above 0.85 on retrieval; egocentric perspective change near chance [c11].
- Wason task: models weak, human content effect much weaker (humans about 70% on social rules, models about 30%) [c14]; deontic rules help models by +5.0 to +41.2 points [c16].
- The Euler-diagram model builder and solver loops show that external model construction works where the LLM alone degrades with length [c19, c23].

---

## 7. What our agent should take

Rule from schema section 8: nothing goes in as [E] on one lab's say-so. Moving a mark needs two independent sources. The statuses below are the claims-file statuses,
with the "human only" caveat made explicit. Equal-token testing (G7) applies to everything.

### 7.1 Add now (established)

These are cheap, low-risk, and supported by two or more sources. Most are bench and harness hygiene or small changes to existing schema parts.

| # | Item | Schema part | Status | Evidence | What to do |
|---|---|---|---|---|---|
| A1 | Confidence and self-report are not an error signal on the illusion class. Keep doubt triggers in code (G1), not in felt certainty. | G1, G10 | [E] (human). Not tested on LLMs | K02; a04, d03, d04, d07, d08 | Do not use stated confidence as a trigger for the case-table or counterexample step. Note for the S0 gate: do not rely on "model feels sure". |
| A2 | Add an explicit "no valid conclusion" candidate to S4 harvest, and let code test it. | S4 | [E] that models rarely produce it; the lift from adding it is untested | K06, K22; a17, a18, a26, b24, c01, d12, d13, d16 | Always include "nothing follows" in the candidate list for questions that ask what follows. Count it in the class record (S9). |
| A3 | Counterexample search is where error drops: keep S7's discriminating test, and widen it so it also fires for conclusions that are consistent with but not entailed by the premises. | S7 | [E] (already in schema); human basis K14 | K14; b20, a11 | Note: a11 is second-hand and b29 was a snippet, so the "two sources" are thin. Keep as is, do not strengthen. |
| A4 | When code finds a counter-model, pass the concrete counter-model back, not a bare "wrong". | S5, G2 | [E] | K30; c20, c23 | Bare "wrong" feedback gave +9.37 points (gpt-3.5) and +2.62 (gpt-4o) over 10 rounds with 111 and 51 tasks never solved. Concrete failing cases are the working pattern in planning. |
| A5 | Log the number of models per item as a class feature. | S0, S9, G12 | [E] for humans; LLM curve untested | K05; a17, a24, a19, a09 | Cheap logging only. Do not assume the human curve (21% for multiple-model syllogisms) for our model. |
| A6 | Probability combination, probability normalising and counting are done in code. | G5 | [E] | K13; a12, a13, b26, d19, d20 | Already in G5. Evidence strengthens it: human violation rates 56% (N=39), LLM identity violations in four models. |
| A7 | Bench hygiene: fix the answer format and report it; randomise referents and content across valid and invalid; state the existential-import convention in the key; use matched controls on the same premises with a different question. | bench design | [E]/[S] | K16, K20, K23, K32; b23, d07, d06, d09, d15 | Format can move correct rate from 19% to 63% on the same premises. Same-premise, different-question is the right ablation design [b05]. |
| A8 | Do not use fluency or a sense of validity as a signal. | G10 | [S] (b23) | K16 | Listed here because it is a never-do. Single source but a clean failed replication. |
| A9 | Do not quote or build on the "model method" 95% vs 63%. | none | [C] | K15; b28, d11 | A no-add note for 4b. |
| A10 | Scaffold strength must be gated by model strength; heavy scaffolds hurt small models. | G7 | [S] | c21 | Matches G7. Measure the plain baseline each time. |

Candidate additions to schema 4b ("not to add"): (a) generic "beware, this may be a trick" warnings on reasoning items [K03, a05, b02, b03] (note that for GPT-4 a plain control prompt blocked as many
fallacies as the erotetic prompt [d02]); (b) the 95% model method as a justification; (c) fluency or felt validity as a signal [K16]. Each is single-source or human-only, so they would enter 4b only as [S].

### 7.2 Test first

These enter as [S] or [D] with the equal-token test in section 8. None is justified yet for LLMs.

| # | Item | Schema part | Status | Evidence | Why test first |
|---|---|---|---|---|---|
| T1 | **Possibility case table** for "exactly one is true" and disjunction items: code builds the rows (premise i true, others false), the model fills each row, code enumerates and applies the modal readout. | O3, S4, S7 | [C] (K04) | a07, b09, b10, d05, c08, d02, K21 | Human gain 33-65% / 39-71% on illusions at a cost of about 15 points on controls. For LLMs: GPT-3.5 14/17 vs 4/17, GPT-4 7/19 vs 8/19, retested failures only. Code-built version untested. Gate it (G1). |
| T2 | **Trigger for the table or counterexample search.** Item-structure triggers from code (multiple-model item, "only one is true" rubric, "nothing follows" candidate present, modal wording) versus sample disagreement versus always-on. | G1, S7, O5 | [S] (K09, K31) | a22, d18, d23 | Disagreement triggers beat always-on on math and commonsense (82.1% at 0.592K vs 80.0% at 1.458K) but cannot catch errors that repeat across samples, which is what illusions and syllogism errors do (K02, K07). |
| T3 | **NVC option plus code counterexample search** on the 64 syllogisms. | S4, S7, O5 | [E] for the gap, [S] for the fix | K06, K22; a26, d12, d13, c06 | No frontier or reasoning-model test. Fix existential import first (K23). |
| T4 | **Counting table for probability**: code expands the full state table, the model fills cells, code counts. | O3, G5 | [S] (K24) | a12, a13, d20, d19 | LLM incoherence is shown; nobody compared a counting table with sum-to-one normalisation (which already cuts error about 35%, G5). |
| T5 | **Code-reordered premises**: sort independent premises into a chain before model building. | S1, O2 | effect [E], remedy [S] (K27) | c13, d01, d26, d27 | Effect: drop over 30% in 2023-24 models. No measurement on frontier or reasoning models. d27 order effect is moral, not deduction. Dependent steps cannot be reordered freely. |
| T6 | **Rulebreaker / knowledge-block check**: "does background knowledge make this rule's conclusion unacceptable?" before applying a formal pattern. | G1, O3 | [S] (K26) | c09 | CoT and symbolic translation helped ordinary items and hurt rulebreakers; a table or form-based step could do the same. Test on both item types. |
| T7 | **Content swap or flag-and-reason** for belief bias. | S1, G2 | [C] (K18) | d14, d22, c22, a27, b24, c05 | Belief bias is small in top models (under 2 pp) and 8-40% in 2024 open models. Counterexample vs flag-and-reason is untested. |
| T8 | **Modal check**: before judging "might" and "must" conclusions, list the possibilities each premise allows, then check. | O3 | [S] (K25) | c02, d17, a21 | Nearly all 2024 LLMs accept two invalid modal patterns. Human norm is parsimonious (K12), so define the norm per benchmark. |
| T9 | **Spatial state table**: write coordinates or the grid after every step, in a table. | O3, memory | [C] (K28) | c12, c10, c11 | VoT gains on some tasks, not on ring navigation; gain in MindCube was small unless trained. |
| T10 | **Practice and history**: does an in-context history of earlier items change accuracy on held-out items, or only the NVC rate. | memory | [C] (K10) | b18, b19, d10 | Human gain may be only a bias shift. Score valid and invalid items separately. |
| T11 | **Harvest-and-test the NVC and weaker conclusion** (mReasoner's "reconclude"): when a counter-model exists, drop to a weaker supported claim. | S7 | [S] | a22, b16 | Parameter value .6 in both extreme groups, so it does not separate good from poor reasoners. |

---

## 8. Concrete tests on our bench

General design for every test below: both arms get the **same token budget**, counting setup and scaffold tokens (G7). Control arms: plain, plain plus a generic warning, plain plus a prose rubric, scaffold.
Report accuracy on **both** target items and matched controls, because the human cost of the case-table procedure was on controls. At least 20 items per type (bigger for subgroup claims). Fix and report the answer format.
Items are built by code so the key is exact. Score "nothing follows" separately.

### Test 1: illusion items with matched controls (decides T1, T2; K33 gaps 1, 2)

- **Item type.** Code-generated pairs on the same premises, one question that exposes the illusion and one that does not.
  Types: embedded disjunction ("A or else (B or else C)"), conditional pairs ("If K then A, or else if not K then A; K"), quantified, modal ("only one is true; is X possible?"),
  plus items where matching and logic disagree and items where a knowledge link triggers it (K32, d24, d25).
- **Arms.** (a) plain; (b) plain + warning; (c) plain + rubric "one true, one false"; (d) prose case-split ("assume premise 1 true and 2 false, then reverse");
  (e) code-built case table with the model filling each row; (f) (e) fired only on a code trigger.
- **Metric.** Accuracy on illusions and on controls; the gap; the number of fallacy answers of the predicted kind; stated confidence and sample agreement for right vs wrong answers (K02 test); tokens per item.
- **Expected effect (hypothesis, not a result).** Arm (c) at or near plain, as in humans and for GPT-4 (8/19 vs 7/19). Arm (e) closes most of the illusion gap, with some control cost.
  Human reference points: illusions 33 to 65% and 39 to 71%, controls down 93 to 79 and 87 to 72. Arm (f) keeps most of the gain and loses less on controls.
  If top models already do well on illusions (the best of 38 models reached 91.7% on disjunction items [d01]), the operator is not needed for those models. Record it and gate it off.

### Test 2: NVC option with counterexample search (T3; gap 4)

- **Item type.** 64 syllogisms with a fixed existential-import key (report both keys). 37 have "nothing follows" as the correct answer.
- **Arms.** plain; plain with an explicit "no valid conclusion" option; option plus code counterexample search (the code enumerates models over a small domain; the model only explains a counter-model if one is found); the same fired on a trigger.
- **Metric.** Accuracy on NVC items and on valid items separately; false-rejection rate (valid items answered "nothing follows"); atmosphere-consistent errors; tokens.
- **Expected effect.** NVC accuracy rises from the near-0% PaLM 2 baseline [a26, d12] without raising false rejections much. Open models: in-context examples do not do this [a27, b24], so expect the code search, not the prompt, to do the work.

### Test 3: search trigger vs always-on (T2; gap 6)

- **Item type.** Mixed set: illusions, syllogisms, set-membership items, controls.
- **Arms at equal tokens.** never; always; on sample disagreement; on a code item signal (multiple-model item, "only one is true" rubric, "nothing follows" candidate present).
- **Metric.** Share of errors each trigger catches; accuracy; tokens.
- **Expected effect.** Disagreement misses uniform errors (illusions, repeated syllogism fallacies [d23, K07]); the item-signal trigger beats always-on at equal tokens. First check whether errors repeat across fresh samples (K07 test).

### Test 4: counting table for probability (T4; gap 9)

- **Item type.** Unique-event paradigm: P(A), P(B), P(A and B), P(A and not B); plus naive-probability problems with biased vs unbiased premise sets (a12, a13).
- **Arms.** plain; plain + normalise to sum 1 over exclusive answers; code-built full-state table, model fills cells, code counts.
- **Metric.** Joint-distribution violation rate (human baseline 56%); deviation from the exact value; tokens.
- **Expected effect.** Table beats plain clearly. Table beats sum-to-1 normalisation only if the errors are about the *models* and not about the arithmetic. Unknown.

### Test 5: premise order (T5; gap 10)

- **Item type.** 50 chain deductions with independent premises, original order vs shuffled; add a version with belief-conflicting content.
- **Arms.** plain; code re-ordered into a chain; flag-and-reason; reorder + flag-and-reason.
- **Metric.** Accuracy by order; drop under shuffle (published drop over 30% for 2023-24 models [c13]); tokens.
- **Expected effect.** Smaller drop for current models. Record whether a drop exists at all for our model.

### Test 6: rulebreakers and modal patterns (T6, T8)

- **Item type.** Paired rulebreaker/ordinary items (modus tollens, disjunctive syllogism with knowledge conflicts) [c09] and the two invalid modal patterns [c02], 20 items each.
- **Arms.** plain; CoT; a possibility table; a "does knowledge block this?" check.
- **Metric.** Paired accuracy (both items right, chance .25), acceptance of invalid modal patterns, and ordinary-item accuracy as a cost check.
- **Expected effect.** CoT may lift ordinary and lower rulebreakers [c09]. The knowledge-block check should lift rulebreakers without hurting ordinary items. The table is a risk on rulebreakers.

### Test 7: belief or content swap (T7)

- **Item type.** Same syllogism forms, believable vs unbelievable vs pseudo-word content.
- **Arms.** plain; flag-and-reason; counterexample search; abstract relabelling.
- **Metric.** Content effect (believable minus unbelievable accuracy on valid items). Published ranges: +10.81 pp mean for 14 models, under 2 pp for top models [d14].
- **Expected effect.** Small for a strong model. If the plain arm has under 2 pp, drop the step.

### Test 8: in-context history and the NVC rate (T10)

- **Item type.** 64 syllogisms in two blocks, with or without prior solved items in context.
- **Metric.** Accuracy and NVC rate separately for valid and invalid items on held-out items.
- **Expected effect.** If history moves only the NVC rate, then it is a bias shift (as Dames et al. 2021 suggest for humans), and lessons in memory must be checked on held-out items (G3).

### Test 9: model-count curve (A5; gap 5)

- **Item type.** Syllogisms and set-membership items grouped by code-computed model count.
- **Metric.** Accuracy by model count at equal tokens, plain vs scaffold.
- **Expected effect.** Humans 80% vs 21%; set membership 92% vs 51%. For a strong LLM the curve may be flat. If it is flat, model count is useless as a budget signal.

### Test 10: spatial state table (T9)

- **Item type.** Navigation and layout items with 3 to 10 steps, including an egocentric perspective change.
- **Arms.** plain; CoT; a state table after each step.
- **Metric.** Accuracy and token cost; skip items that reduce to arithmetic.
- **Expected effect.** Gain on multi-step layout, none on ring-type arithmetic [c12].

First three tests to run, in this order (from the critique): Test 1, Test 2, Test 3. Keep any table gated until Test 1 reports its cost on controls.

---

## 9. What does not transfer, and why

| Human finding | Why it may not carry to an LLM agent |
|---|---|
| Working-memory limits create the preference for one model | LLMs have no such limit in the same form [a25]. The pattern of errors (single-model answers) may still appear, as in PaLM 2, but for other reasons. |
| Student samples, N 16 to 56 per experiment | Effects at that size are rough. Effect sizes for LLMs must be measured on our items. |
| Illusion size from one lab | Wording, format and co-reference move the rate (84% vs 19%; 63% vs 19%; 10% vs 78%) [d06, d07, d09]. No single human number should be a target. |
| mReasoner parameters (size, search, weaken) as individual-difference traits | Fits are in-sample with free parameters, and the program has no belief handling [b17, c26]. The "search probability" is a description, not a trigger rule [d18]. |
| Practice gain without feedback | Likely a response-bias shift in the larger study [b19, d10]. For an agent, in-context history needs a held-out check (G3). |
| "Model method" training | Unverified anecdote [b28, d11]. Telling a person to list possibilities is instruction; for a model the equivalent is a structural step, not a hint. |
| Fluency of valid conclusions | Failed replication [b23]. |
| Warning instructions | Fail for people [a05]; for GPT-4 a plain control prompt blocked as many fallacies as the theory prompt [d02]. |
| Supervised fine-tuning fixes (NVC, content bias) | Training. Out of scope [a27, b24, c06]. Steering vectors need hidden states [d22]. |
| Euler-diagram neural checker | Authors' own architecture, syllogisms only, takes up to about 2 minutes at 12 terms [c19]. The idea (exact external model builder) transfers; the network does not. |
| "Mental models" in MeMo and in everyday-things probes | A different concept: thinking tools and world knowledge. They give no support to Johnson-Laird's method [c18, c27]. |
| Human content effect in the Wason task | Much weaker in LLMs [c14]. |
| Full modal logic as the norm | People are parsimonious in possibility reasoning and violate normal modal logics [a21]. Decide the norm per benchmark. |
| Spatial model-building for easy relational items | Models add little over transitive closure (71.9-79.1% vs 73.4-75%) [c25]. Heavy model-building only for indeterminate cases. |
| Rule-theory logic as a fix | Formal translation can hurt where knowledge blocks a rule (rulebreakers) [c09]. |
| The theory's own claims on rival accounts | The refutations of rivals are by the authors [a05, b12, b13]. Use the procedure, not the claim. |

---

## 10. Open questions

1. Do current frontier and reasoning LLMs fall for Johnson-Laird's own illusions (propositional, quantified, embedded disjunction, modal) at human rates, with matched controls, and is their confidence or sample agreement uninformative about the errors? Only 2023 chat models and a disjunction-type set exist (K19, K33).
2. Does a code-built possibility table beat plain and beat a prose warning at equal tokens, and what does it cost on controls (human cost about 15 points)? Include rulebreaker and modal items (K25, K26), where formal structure can hurt.
3. What should trigger counterexample search for a model? Item-structure signal vs disagreement vs always-on (K09, K31).
4. Do frontier and reasoning LLMs accept "nothing follows" when it is right, and does an explicit option plus code search lift NVC accuracy without raising false rejections (K06, K23)?
5. Is the "model method" real? The original data are unavailable (K15).
6. Is there an independent replication of illusions with proper pragmatic and item-order controls? Tabossi, Rips, Walsh and Koralus originals were not read in full. Espino et al. 2024 is the only conditional replication.
7. Is the human practice gain a bias shift or deeper checking, and does in-context history shift only the NVC rate in an LLM (K10)?
8. Does belief or content bias remain in frontier and reasoning models once forms are fixed, and does counterexample search remove it better than flag-and-reason (K18)?
9. Does a code counting table fix LLM probability incoherence beyond sum-to-one normalisation (K24)?
10. Do premise-order drops and rulebreaker failures persist in current frontier models, and does code reordering or checking fix them (K26, K27)?
11. Is the LLM illusion partly a surface-matching effect (d25) and partly a representation effect? The two predict different fixes.
12. Why is the best of 38 models at 91.7% while the mean is 40.6%? What do the best models do, and is it a procedure we can copy?
13. How should reasoning-model "thinking" be compared to a code-run scaffold on these items (schema slot "thinking-mode baseline")? No study found.

---

## 11. Sources

Marks: **[V]** opened and read this session (full text or substantial part; partial reads are noted). **[M]** snippet, abstract or second-hand only.
Where an earlier agent marked a source opened but the critique could not recheck it, a note says so.

### Core theory, illusions and remedies

1. Johnson-Laird and Savary (1996) Illusory inferences about probabilities. [V, but the critique could not re-open it: web archive returned a bot challenge, so a02/a03 numbers are unchecked] https://web-archive.southampton.ac.uk/cogprints.org/657/1/prob.htm
2. Johnson-Laird and Savary (1999) Illusory inferences: a novel class of erroneous deductions. [V, numbers re-checked by critique] https://modeltheory.org/papers/1999illusory.pdf
3. Yang and Johnson-Laird (2000a) Illusions in quantified reasoning. [V] https://logic.pku.edu.cn/ann_attachments/p1.pdf
4. Yang and Johnson-Laird (2000b) How to eliminate illusions in quantified reasoning. [V, rechecked] https://modeltheory.org/papers/2000eliminate-illusions.pdf and https://logic.pku.edu.cn/ann_attachments/p2.pdf
5. Goldvarg and Johnson-Laird (2000) Illusions in modal reasoning. [V for Exp 1-3 in d03/d04; earlier b11 was second-hand] https://modeltheory.org/papers/2000illusions3.pdf
6. Santamaria and Johnson-Laird (2000) An antidote to illusory inferences. [V] https://modeltheory.org/papers/2000antidote-to-illusions.pdf
7. Khemlani and Johnson-Laird (2008/2009) Illusory inferences about embedded disjunctions / Disjunctive illusory inferences and how to eliminate them. [V; use the 2009 text] https://modeltheory.org/papers/ssk/ssk2008disjillusions.pdf and https://modeltheory.org/papers/2009disjunctive-illusions.pdf
8. Walsh and Johnson-Laird (2004) Co-reference and reasoning. [V, partly: abstract, Exp 3, parts of Exp 1] https://link.springer.com/content/pdf/10.3758/BF03195823.pdf
9. Khemlani and Johnson-Laird (2017) Illusions in reasoning. [V] https://modeltheory.org/papers/2017illusions.pdf
10. Espino, Orenes and Moreno-Rios (2024) Illusory inferences in conditional expressions. [V] https://link.springer.com/content/pdf/10.3758/s13421-024-01571-2.pdf
11. Sable-Meyer and Mascarenhas (2021) Indirect illusory inferences from disjunction. [V] https://hal.science/ijn_03462059v1/document
12. Ghasemi, Handley and Howarth (2023) Illusory intuitive inferences: matching heuristics explain logical intuitions. [V, Exp 3 and 4 skimmed only] https://osf.io/276tw/download
13. Koralus and Mascarenhas (2013) The erotetic theory of reasoning. [M, fetch empty] https://escholarship.org/uc/item/1ft528sw
14. Johnson-Laird (2010) Mental models and human reasoning (PNAS). [V, review] https://www.modeltheory.org/papers/2010mms%26human-reasoning.pdf
15. Johnson-Laird and Goldvarg (1997), cited for the same-premise test. [M, not opened; cited in 2]

### Syllogisms, relations, sets, conditionals, modality, probability

16. Bucciarelli and Johnson-Laird (1999) Strategies in syllogistic reasoning. [V] https://modeltheory.org/papers/1999strategies.pdf
17. Khemlani and Johnson-Laird (2012) Theories of the syllogism: a meta-analysis. [V, rechecked] https://modeltheory.org/papers/ssk/ssk2012syllogisms-meta-analysis.pdf
18. Khemlani and Johnson-Laird (2016) How people differ in syllogistic reasoning. [V] https://modeltheory.org/papers/2016syllogisms-indvl-diffs.pdf
19. Khemlani and Johnson-Laird (2021/2022) Reasoning about properties: a computational theory (mReasoner). [V] https://modeltheory.org/papers/2021mReasoner.pdf ; software page https://www.modeltheory.org/mreasoner/ [V]
20. Khemlani, Lotstein and Johnson-Laird (2014) A mental model theory of set membership. [V] https://modeltheory.org/papers/2014set-membership.pdf
21. Goodwin and Johnson-Laird (2005) Reasoning about relations. [V; not all experiment sizes read] https://modeltheory.org/papers/2005reasoningrelations.pdf
22. Byrne (1989) Suppressing valid inferences with conditionals. [V, table rechecked] https://modeltheory.org/papers/1989suppression.pdf
23. Ragni and Johnson-Laird (2018) Reasoning about possibilities: human reasoning violates all normal modal logics. [V, corrected by critique] https://modeltheory.org/papers/2018humans-vs-modal.pdf
24. Ragni, Riesterer, Khemlani and Johnson-Laird (2018) Individuals become more logical without feedback. [V] https://modeltheory.org/papers/2018logical-wo-feedback.pdf
25. Dames, Klauer and Ragni (2021) The stability of syllogistic reasoning performance over time. [V full text in d10; the publisher page in b19 returned only an abstract] https://modeltheory.org/papers/2021stability-syllogisms.pdf and https://doi.org/10.1080/13546783.2021.1992012
26. Ragni and Kola (2018) On selecting evidence to test hypotheses. [V] https://modeltheory.org/papers/2018selection.pdf
27. Ragni, Dames and Johnson-Laird (2019) A meta-analysis of conditional reasoning. [V] https://modeltheory.org/papers/2019meta-conditionals.pdf
28. Oberauer (2006) Reasoning with conditionals. [M, abstract] https://publishup.uni-potsdam.de/solrsearch/index/search/searchtype/authorsearch/author/Klaus+Oberauer
29. Singmann, Klauer and Kellen (2014) Intuitive logic revisited. [V] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3995688/
30. Newstead, Handley and Buck (1999) and related belief-bias work. [M, search summary only] https://researchportal.plymouth.ac.uk/en/publications/the-source-of-belief-bias-effects-in-syllogistic-reasoning/
31. Johnson-Laird, Legrenzi, Girotto, Sonino Legrenzi and Caverni (1999) Naive probability. [V] https://modeltheory.org/papers/1999naiveprob.pdf
32. Girotto and Gonzalez (2001), cited for 53% vs 8%. [M, not opened] https://modeltheory.org/papers/1999naiveprob.pdf
33. Khemlani, Lotstein and Johnson-Laird (2012) The probabilities of unique events. [V] https://modeltheory.org/papers/2012prob-unique-events.pdf
34. Johnson-Laird (2024) Mistakes in thinking about cognitive science and how to reduce them; Johnson-Laird (2012) Mental models and consistency (Bell's "model method"). [V, but second-hand for Bell's thesis; unpublished] https://modeltheory.org/papers/2024mistakes.pdf and https://modeltheory.org/papers/2012consistency.pdf
35. Khemlani and Johnson-Laird (2019) Why machines don't (yet) reason like people. [V] https://www.modeltheory.org/papers/2019machine-reasoning.pdf
36. Ragni, Brand and Riesterer (2021) The predictive power of spatial relational reasoning models. [V] https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.626292/full
37. Mannhardt, Bucher, Brand and Ragni (2021) Predicting spatial belief reasoning. [M, abstract] https://mathpsych.org/presentation/585

### Language-model studies

38. Eisape et al. (2024) A systematic comparison of syllogistic reasoning in humans and language models (NAACL). [V, rechecked] https://arxiv.org/abs/2311.00445
39. Bertolazzi, Gatt and Bernardi (2024) LLMs as soft reasoners: syllogistic inferences (EMNLP). [V, c06 numbers rechecked] https://arxiv.org/abs/2406.11341
40. Bertolazzi, Pezzelle and Bernardi (2026) How language models conflate logical validity with plausibility. [V] https://arxiv.org/pdf/2510.06700
41. Poddar, Sahoo and Ghosh (2025/2026) Understanding syllogistic reasoning in LLMs from formal and natural language perspectives. [V in d14; c29 was abstract only] https://arxiv.org/pdf/2512.12620
42. Zang et al. (2026) A syllogistic probe: tracing the evolution of logic reasoning in LLMs. [V, abstract and introduction only] https://arxiv.org/pdf/2601.17426
43. Koralus and Wang-Masciantica (2023) Humans in humans out. [V, rechecked] https://arxiv.org/abs/2303.17276
44. Richardson, Kearns, Moss, Wang-Mascianica and Koralus (2026) Theory-grounded evaluation of human-like fallacy patterns in LLM reasoning. [V] https://arxiv.org/pdf/2506.11128
45. Holliday, Mandelkern and Zhang (2024) Conditional and modal reasoning in large language models (EMNLP). [V] https://arxiv.org/abs/2401.17169 (c02 and d17 give 29 vs 25 models; the numbers are not fully reconciled)
46. Chan, Gaizauskas and Zhao (2025) Rulebreakers. [V, rechecked] https://arxiv.org/abs/2410.16502
47. Chen, Chi, Wang and Zhou (2024) Premise order matters in reasoning with LLMs. [V, abstract and method] https://arxiv.org/abs/2402.08939
48. He et al. (2025) Order doesn't matter, but reasoning does. [V, table layout scrambled] https://arxiv.org/pdf/2502.19907
49. Tennant et al. (2026) Normative robustness as a frontier for non-verifiable reasoning. [V, abstract and setup] https://arxiv.org/pdf/2606.12731
50. Joishy et al. (2026) Flying pigs, FaR and beyond (CounterLogic). [V, rechecked] https://arxiv.org/abs/2505.22318
51. Lampinen et al. (2024) Language models show human-like content effects on reasoning tasks. [V] https://arxiv.org/abs/2207.07051
52. Ozeki et al. (2024) NeuBAROCO. [V] https://arxiv.org/abs/2408.04403 ; Ando et al. (2023) earlier version [M] https://arxiv.org/abs/2306.12567
53. Seals and Shalin (2024) Evaluating the deductive competence of LLMs. [V] https://arxiv.org/abs/2309.05452
54. Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs. [V, per-model rates not extracted] https://arxiv.org/abs/2402.09193
55. Abe et al. (2026) Deontic conditional reasoning in LLMs. [V, per-model cells not extracted] https://arxiv.org/abs/2603.06416
56. Tsvilodub et al. (2024) Experimental pragmatics with machines. [V] https://arxiv.org/abs/2405.05776
57. Mondorf and Plank (2024) Comparing inferential strategies of humans and LLMs in deductive reasoning. [V] https://arxiv.org/pdf/2402.14856
58. Zhu and Griffiths (2024/2025) Incoherent probability judgments in LLMs. [V] https://arxiv.org/pdf/2401.16646
59. Dong, Jamnik and Lio (2025) Sphere neural-networks for rational reasoning. [V, rechecked] https://arxiv.org/abs/2403.15297
60. Jha et al. (2023) Counterexample guided inductive synthesis using LLMs and SAT solving. [V, full iteration table not extracted] https://arxiv.org/abs/2309.16436
61. Wan et al. (2025) Derailer-Rerailer. [V] https://arxiv.org/pdf/2408.13940
62. Kargupta et al. (2025) Cognitive foundations for reasoning and their manifestation in LLMs. [V] https://arxiv.org/abs/2511.16660
63. Wu et al. (2024) Visualization-of-Thought. [V, rechecked, table scrambled] https://arxiv.org/abs/2404.03622
64. Wang et al. (2025/2026) MindCube. [V] https://arxiv.org/abs/2506.21458
65. Jiang, Qin and Li (2026) SpatialText. [V] https://arxiv.org/abs/2603.03002
66. Guan et al. (2024) Towards generalist prompting for LLMs by mental models (MeMo). [V; different concept] https://arxiv.org/abs/2402.18252
67. Gu, Dalvi Mishra and Clark (2023) Do language models have coherent mental models of everyday things? [V, abstract and introduction; different concept] https://arxiv.org/abs/2212.10029
68. Nighojkar et al. (2025) Giving AI personalities leads to more human-like reasoning. [M, abstract] https://arxiv.org/abs/2502.14155
69. Li, Yu and Ettinger (2022) Counterfactual reasoning; Lewis and Mitchell (2024). [M, summaries only] https://arxiv.org/abs/2212.03278

### Search records (not sources of findings)

70. Coverage-gap searches for LLM tests of model-theory paradigms (c31) and frontier-model search log (d28). [M] https://export.arxiv.org/api/query and https://api.openalex.org/works?search=illusory+inferences+language+models

Items marked [M] must not be quoted for numbers.
