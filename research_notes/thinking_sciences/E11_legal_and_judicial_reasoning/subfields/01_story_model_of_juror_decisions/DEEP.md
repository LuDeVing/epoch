# Story model of juror decisions: deep document

*Subfield E11.01. Written from evidence_a-d.jsonl, claims.jsonl (K01-K27) and critique.md in this folder. Evidence ids (a01, b15, d06 ...) point to lines in the evidence files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Read this first: the founding papers (Pennington and Hastie 1986, 1988, 1992) were never opened by any agent. Every founding number is second-hand, taken from the authors' own 1993 review chapter (d01-d05) or from secondary summaries. Where that matters, the text says so.*

## 1. What it is

The story model is a theory of how people turn a pile of trial evidence into a verdict. It was proposed by Nancy Pennington and Reid Hastie (1986, 1988, 1992, 1993). It says jurors do not add up evidence items. They build a causal story and judge the story.

Three stages (a01, b01, c01, a12):

1. **Build a story.** The juror takes the evidence (scrambled, gappy, piecemeal) plus two kinds of knowledge: what a complete story looks like, and what happens in similar events. From these the juror infers a causal account of what happened.
2. **Learn the verdict categories.** The judge's instructions define each verdict (first-degree murder, manslaughter, self-defence, not guilty). A verdict is a category with criterial features: identity, mental state, circumstances, actions, joined by "and" and "or" (a04). Jurors learn this from one hearing of abstract text.
3. **Match the story to a category.** The verdict is the category whose features the story fits. If no category fits beyond reasonable doubt, the default is not guilty (a04).

The decision rests on the story summary, not on the raw evidence (K01 [E]).

**The story has a fixed shape (a02).** It is an episode schema: initiating events, goals, actions, consequences, accompanying states, in a causal configuration. Episodes nest, so a story is a hierarchy. Knowing the shape lets the juror see what is missing and fill it by inference.

**Confidence rests on certainty principles (a03, b02):**

| Principle | Meaning |
|---|---|
| Coverage | how much of the credible evidence the story explains |
| Completeness | the story has all the expected parts |
| Consistency | no internal contradictions |
| Plausibility | fits world knowledge |
| Uniqueness | no rival coherent story exists |

Coverage plus coherence (completeness, consistency, plausibility) govern acceptance. Uniqueness governs confidence: two coherent stories lower confidence in either. The authors give no weights and no functional form for combining the five (b02). This is why critics call the model hard to falsify (a20).

**Why it matters for our agent.** The model is a theory of selection under incomplete, interdependent evidence. It maps to two parts of the schema. S2 REPRESENT (what form the evidence takes before the answer is chosen). S7 SELECT (how rival candidates are scored: coverage, then coherence, then uniqueness). It also gives a warning: a fluent story is easy to build for any answer (K15), so a story is not evidence for itself (G10).

**Extension to non-legal tasks.** Hastie and Pennington (1996, a09) generalise the model to "explanation-based decision making" for any task that needs comprehension of a complex situation (military tactics, diagnosis). This is argued, not tested (a09 limits).

## 2. History and theories in depth

### 2.1 Roots

- **Story grammars and episode schemas** from text-comprehension research supply the idea of a fixed story shape (a02). The shape was assumed, not derived from juror data (a02 limits).
- **Rival juror theories in the 1970s-80s** were the context. Hastie and Pennington list five (a08, b06): individual differences (authoritarianism and similar traits), the heuristics toolbox, algebraic weight-and-add models, economic utility theory, critical-legal accounts. They argue algebraic models fit overall judgments but give no picture of comprehension and credibility processes. That comparison is the authors' own, not an independent test.
- **Bayesian and "meter" models** (running strength of belief updated by weighting and adding) are argued against by the authors using mock-juror studies that "for the most part" do not support Bayes (a10). This is a post-hoc reading (a10 limits).

### 2.2 The founding studies

| Year | Paper | What it did | Status of our reading |
|---|---|---|---|
| 1986 | Pennington and Hastie, Evidence evaluation in complex decision making, JPSP 51:242 | Murder case (Johnson and Caldwell), four verdict options. Jurors gave verbal protocols. Stories coded as causal event chains. Verdict groups differed in the stories they built. | Not opened (a30). Secondary only. |
| 1988 | Pennington and Hastie, Explanation-based decision making: effects of memory structure on judgment, JEP:LMC 14:521 | Memory study (119-sentence case, recognition test) and the order-of-evidence experiment (2x2). | Not opened (a31). Cells and design read from the 1993 chapter (d01, d02, d05). |
| 1992 | Pennington and Hastie, Explaining the evidence: tests of the Story Model for juror decision making, JPSP 62:189 | Three experiments. Exp 1: story order vs issue order. Exp 2-3: global vs item-by-item judgments, compared with Bayesian and anchor-and-adjust models. | Abstract only (a16, b09). Details from the 1993 chapter (d03, d04). |
| 1993 | Pennington and Hastie, The story model for juror decision making, in Hastie (ed.) Inside the Juror, ch. 8, pp. 192-222 | Fullest statement. Reviews all of the above. | Opened (d01-d05). Crossref lists 175 citations (b08). |
| 1993 | Hastie and Pennington, Implications of the Story Model for the Trial Judge's Behavior | 14-page chapter for judges. Theory plus a 4-judge pilot. | Opened (a01-a08, b01-b06, c01-c03). |
| 1996 | Hastie and Pennington, The O.J. Simpson stories | Applies the model to one trial. | Opened (a09-a11). |

### 2.3 The order-of-evidence experiment, in detail

This is the best-known result. It comes from Pennington and Hastie 1988, reproduced in the 1993 chapter (d01, d02).

- Design: 2x2. Prosecution evidence in story order or witness order. Defense evidence in story order or witness order.
- Materials: a murder trial case reduced to 100 statements (50 prosecution, 50 defense), tape recorded. Prosecution always came before defense. The same statements appeared in every condition; only the order changed (a13, d02). A blog account says 119 statements (a14); that count matches the memory-study materials (d05), so the two accounts probably describe different experiments.
- Sample: N=130 college students, about 32 per cell (cell sizes are not printed; d01).
- Outcome: percent guilty of murder.

| | Defense in story order | Defense in witness order | Row mean |
|---|---|---|---|
| Prosecution in story order | 59 | 78 | 69 |
| Prosecution in witness order | 31 | 63 | 47 |
| Column mean | 45 | 70 | |

The both-witness cell is **63**. One secondary source said 62 (a13); the authors' own table gives 63 and the row and column means reconcile with it (critique.md, d01).

Other results from the same experiment (d02): story-order evidence was rated stronger than witness-order evidence. The perceived strength of one side depended on the order of both sides. Confidence was higher when both sides were in story order, whichever verdict was chosen (not predicted). Memory for the evidence did not differ (K02). The authors state the study was not built to estimate order effects in real trials; openings, closings, redundancy and visual aids that help real jurors were absent (d02 limits).

No test statistics (F, p, effect sizes) are available. The journal article was not opened.

### 2.4 The 1992 replication and the global-judgment studies

- **Exp 1 replication (d03).** New materials (Devine and Ostrom 1985 cases; two cases, one leaning guilty, one leaning innocent), written. Evidence in story order versus legal-issue order. N=414 college students. Free recall clustered by the order given (story clustering high under story order; issue clustering high under issue order; ARC measure). Total recalled did not differ. Verdicts moved in the expected direction and confidence was higher under story order. No effect sizes available.
- **Exp 2-3 (d04, b09).** Two experiments compared the story model with a Bayesian model and an anchor-and-adjust sequential updating model. Item-by-item ratings fit anchor-and-adjust. Global verdict ratings fit neither and fit a story-weight configuration best. Global assessments were about **1.5 times stronger** than the final item-by-item rating. A story-supplement by response-mode interaction on final guilt was found. Fit comparisons are descriptive and authors' own.
- **Boundary found by the authors:** the task changes the strategy. Asking for a judgment after each block pushes jurors toward linear, item-by-item updating (a16 limits). The story process is the default for a single end-of-case judgment.

### 2.5 The memory studies (d05)

- Jurors falsely recognised inferences that belonged to the story of their own verdict. Own-verdict story items were accepted at a higher rate than rejected-verdict story items, for both old items and never-presented lures. Exact rates are not printed in the chapter.
- Jurors rated evidence importance by its causal role in the story.
- Memory for verdict-element definitions was not related to verdict choice. Verdict choice was not explained by differences in how well jurors remembered the legal categories (K21).

So story building adds inferences that later feel like evidence. This is the main source of "false memory" in the model.

### 2.6 Stage two and judges

- **Poor category learning (a04, a05, b04, c03).** Jurors reinterpret abstract terms through the story. Example: told to judge whether the defendant had "exhausted all means to avoid combat", jurors often decided he should never have been at the scene, and so lost self-defence. That reading is wrong in law. Atypical crimes that do not fit a prototype are harder to classify. All qualitative; no counts (K05 [S]).
- **Judges (a07, b05, c02).** Four trial judges, two stimulus trials. Judges also built narratives but reasoned backward from known verdict elements earlier, spent more time on credibility and inference strength, and often matched the case to a remembered precedent. N=4, no statistics.

### 2.7 Authors' stated boundary conditions (a06, b06, c01)

- Mostly criminal trials with realistic, typical cases.
- Extremely violent, racially or politically charged, and emotion-provoking cases were not studied.
- Not claimed universal: almost every mock juror used the strategy, but a few did not do all sub-tasks.
- Mock jurors were mostly students; some work used citizens called for jury duty (sizes not given).

### 2.8 Computational and formal rivals and cousins

- **ECHO / explanatory coherence (Thagard).** Seven principles: symmetry, explanation, analogy, data priority, contradiction, competition, acceptability (a22). Activations in [-1, 1].
  - Byrne 1995 (a19, a20) built ECHO networks from the verbal stories of two real mock jurors from the 1993 data. Juror 109 (not guilty, self-defence): 26 propositions, 18 explanations, 7 links to verdict categories, 19 to testimony. Juror 128 (first-degree murder): 19 propositions, 14 explanations, 8 verdict links, 18 testimony links. ECHO picked each juror's own verdict. Only two jurors, both at the extremes; Byrne is a proponent of the merger.
  - Byrne's critique: coherence, completeness and uniqueness are not formally defined, so readings are possible after the verdict is known (a20).
  - Thagard 2003 (a21, a23, c25): ECHO on the O.J. Simpson network accepts that Simpson was the killer (and that the police tried to frame him). JavaBayes gave P(OJ killed)=.72, P(drug killings)=.29, P(LAPD framed)=.99, from 60 conditional probabilities that were "guesses at best". So pure coherence maximising did not reproduce the acquittal. Thagard adds emotional coherence and group factors. Poll figures (20%, 50%, 3% of 200, 75%) come from books by trial participants (a23). One case, hand-built network. K09 [C].
- **Coherence shift / constraint satisfaction (Holyoak and Simon 1999; Simon, Pham, Le and Holyoak 2001; a32, b33).** The leading option re-weights how later evidence is judged. Not opened by us; citation counts 269 and 203 (a32), 86 (b33). Newer evidence: negative moral emotion toward a defendant shifted agreement with unrelated evidence in three civil studies, N=713, 677, 651; judicial rehabilitation did not remove it (b21). K07 [E].
- **Bayesian causal models (Shengelia and Lagnado 2020; b20).** People update in the right direction as evidence arrives item by item, not by exact Bayes; errors are partly explained by the causal models held. MTurk, Exp 1: 155 recruited, 127 kept; Exp 2: 93. This is the format where the story model itself predicts anchor-and-adjust, so it is not a clean test.
- **Hybrid argument-and-story theory (Bex and Verheij 2010; b34).** Stories must be anchored in evidence by arguments. Metadata only (77 citations).
- **Relative plausibility (b26).** Legal theory: the fact-finder compares complete competing stories. A 2022 paper argues a probabilistic approach can answer the objections. Theory only.
- **Fuzzy-trace theory (b24).** Story is the top-level gist, but gist is also extracted from single items. Position paper.
- **Analyst narratives (b27).** Two intelligence teams built micro-narratives to test hypotheses by mental simulation, then merged them. Qualitative.

### 2.9 Deliberation and group critique

The original model is an individual-juror model. Critiques (b07, a12): thin on group deliberation (a jury can go from 11-1 to 12-0); assumes a logical process with few outside influences; unclear whether the story form itself is causal or only a convenient description. Broad review: Devine et al. 2001, 45 years of deliberation research (b35, not opened, 323 citations).

## 3. Core findings with exact numbers

Status uses the claim ids from claims.jsonl. "Second-hand" means the number comes from a review chapter or summary, not the original paper.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Three-stage structure; verdict rests on the story summary | no numbers | a01, b01, c01, a12 (K01) | [E] as a theory; supported by order and memory studies |
| Story order vs witness order changes verdicts (Pennington and Hastie 1988 as printed in 1993 chapter) | % guilty: pros story/def story 59; pros story/def witness 78; pros witness/def story 31; both witness 63. Row means 69 vs 47; column means 45 vs 70. N=130, about 32 per cell. 100 statements. | d01, d02 (K02) | [E] direction; second-hand cells; no test statistics |
| Recall equal across orders; confidence higher with both sides in story order | no difference in total recall; confidence higher both-story whatever the verdict | d02, d03 | [E] direction, no statistics |
| Replication with new materials, story vs issue order | N=414 students; verdict and confidence in expected direction; recall clustering follows order; total recall equal | d03, a17, c04 | [E] direction; effect sizes unavailable |
| Global judgments are stronger than item-by-item | about 1.5 times; item-by-item fits anchor-and-adjust; global fits story weights | d04 (K20) | [S] review-level numbers |
| Story inferences become false memories | own-verdict story items accepted more (old and lures); rates not printed | d05 (K21) | [S] |
| Verdict-category memory unrelated to verdict choice | no rates | d05 | [S] |
| Jurors reinterpret legal terms through the story; judges reason backward from elements | judges N=4, 2 trials; no counts | a04, a05, a07, b04, b05, c02 (K05) | [S] |
| Direct quantitative test of the certainty principles (Juror Decision Scale) | N=324 in 27 panels of 12; odds ratio for guilty verdict: complainant believability 1.62 pre, 1.45 post; defendant believability 0.68 pre, 0.78 post. Belief in two stories correlated r=-0.30 pre, -0.36 post. Confidence vs complainant belief r=0.10 (ns) pre. Panel verdicts: 22 not guilty, 5 guilty. Fit CFI .94 pre, .96 post; RMSEA .07. | b11-b14 (K04) | [S]; single rape-trial video; page returned 403 later, so numbers are single-read |
| Narrative topic model fits evidence accumulation brain maps better than utility | N=29 usable of 33; BIC narrative 40,285 (p=.014 vs null); utility 41,550 (p=.24); social-affective 41,947 (p=.72); narrative recall BIC 41,436 (p=.019); reading BIC 40,975 (p=.020); word count p=.802; reading complexity p=.571 | b15 (K08) | [S]; BICs from models of different size, only the null comparison is meaningful (critique 4) |
| Additive weights also fit case-strength ratings | crime-type weights for strength vs punishment r=0.904; case strength 36.18, 58.36, 69.39 as items added | b16 | [S] |
| Coherence maximising alone does not reproduce the O.J. verdict | ECHO accepts guilt; JavaBayes P(killed)=.72 | a21, c25 (K09) | [C] |
| Negative emotion shifts agreement with unrelated evidence | three studies, N=713, 677, 651 | b21 (K07) | [E] with a32, b33 |
| Item-by-item special verdict with reasons changes verdicts | Exp 1 N=267, 66.2% for plaintiff overall. Exp 2 N=292: juries (not jurors) found not liable 92.6% under special verdict with reasons vs 40.9% general verdict after deliberation. Juror-level general verdict 43.30% pre vs 40.91% post. | b18, a17, c04 (K10) | [S]; unit is the jury; text is internally inconsistent about direction of the 45.9% figure (critique 1) |
| Timing of expert testimony (before vs after eyewitness) | N=222, 2x3 between; no effect on credibility, guilt rating or verdict | b19 (K11) | [S]; null may be low power |
| Recency, not primacy, in law students | N=407, murder vignette | b22 | [S] |
| Pre-trial bias predicts verdict; evidence anchors do not | N=128 mock jurors, two homicide vignettes, within subject; third "not proven" verdict lowered both guilty and not-guilty verdicts | b17, c05, a18 | [S]; post hoc story-model reading |
| Rape-myth acceptance predicts not-guilty verdicts; legal attitudes do not | N=435 online | b23, c06 | [S]; story model used to explain both outcomes |
| LLM (GPT-4o) recency in legal guilt ratings | order effect F(1,711)=424.76, p<.001; means G-I double 4.24, G-I single 3.54, I-G double 6.04, I-G single 4.77; 720 trials per model | a24, c08 (K12) | [E] (opened twice, with human data from a separate study) |
| GPT-5.2 order effect much weaker | F(1,711)=71.24; means 4.75/4.79/5.35/5.02 | a25 | [E] |
| Humans also show recency | order F(1,686)=54.40; means 4.00, 4.54, 5.77, 5.38; 120 participants, 715 final ratings | a25 | [E] |
| Intermediate rating inflates GPT-4o final guilt | 3.54 vs 4.24 (G-I), 4.77 vs 6.04 (I-G); GPT-5.2 only when incriminating evidence last (5.02 vs 5.35) | a26 | [E] |
| Prompt fixes barely help | PE2 "be meticulous" cut GPT-4o order effect by 0.32 (SE .11, p=.003); PE1 expert -0.19 (p=.075); PE3 justify -0.16 (p=.12); order x prompt F(3,2859)=3.11, p=.026 | c09 (K13) | [S] |
| LLM mock jurors differ from humans in level | guilt probability 63.56 vs 58.82; guilty verdicts 21% vs 49%; 2,304 responses; same direction of effects | c07, d18 (K14) | [E] (abstract/search summary only) |
| LLM explanation scoring: consistency alone cannot tell right from wrong | up to 77% accuracy with all features (chance 50%), +17.5 points over a GPT-3.5 judge; wrong explanations have about 6% deeper proofs, about 10% more concept drift; COPA coherence .66 alone, uncertainty .70 alone, all .77 | a27, a28, c12, c13 (K15) | [E] |
| Raw prompting drops evidence | coverage 0.9014 with audit loop vs 0.8436 without fusion audit; factual consistency 0.7217 vs 0.6000 (+20.3%); temporal coherence 0.2900 vs 0.2150 (+34.9%); cheap tier coverage 0.936 but temporal coherence 0.118 | b31, c14, c15 (K16) | [S]; synthetic scenes, authors' metrics |
| Finding the best explanation is the bottleneck | MuSR murder mysteries GPT-4 80.4% (CoT+), human 94.1%, random 50.0; GPT-4 by prompt: regular 64.8, CoT 65.6, CoT+ 80.4, 1-shot CoT+ 86.0; decomposed 77.6 (1-shot 86.0). True Detective: vanilla GPT-4 27%, CoT 38%, golden chain 83%, random 24%, humans 47% | c16-c18 (K17) | [E] |
| Same facts, different order, different LLM accuracy | Test of Time shuffle vs best order: GPT-4 60.71 vs 65.36 (table: 62.60 under Target-and-StartTime); Gemini 1.5 Pro 63.04 vs 75.00; Claude-3-Sonnet 45.71 vs 73.57 | d06 (K22) | [E] with d07 |
| Premise order | forward (proof) order best; drop up to over 30% on logic; Gemini 1.0 Pro and GPT-3.5 fall from over 65% to below 25% at 12 rules | d07 | [E] |
| Source position bias differs by model | Llama trusts earlier sources; GPT-4o often trusts the last; Gemma and o3-mini mostly invariant | d08 (K23) | [S] |
| Twelve LLM jurors hang | 17 of 18 runs hung; GPT-4o mean 1.0 vote change per run; Llama-4-Scout 2.0 baseline to 6.0 open-minded | b29, c10, c11 (K18) | [E] direction (N=3 per cell) |
| Rival options and calibration | adding 3 distractors cut mean ECE by 0.260 over 27 pairs (SimpleQA 0.433, FaVIQ 0.292, TriviaQA 0.057); worse ECE on TriviaQA for GPT-4-turbo and GPT-4o | d10 (K24) | [S]; mostly a multiple-choice format effect |
| Coverage as a training reward | coverage 33.1% to 52.9% (composite) vs 39.1% correctness-only (R1-Distill-7B, 10 held-out sets); accuracy 54.1 vs 51.1 (R1-Distill-7B), 52.1 vs 50.3 (Qwen3-4B) | d11 (K25) | [S]; RL training, not prompting |
| LLMs under-weight own prior but are pulled to their own wrong answer | prior weight 0.20-0.65 on arithmetic across 9 models; attractor effect positive in 9 of 9; 12 models, over 10 million trials | d12 (K26) | [S] |
| Hypothesis sets lose uniqueness as spaces grow | no numbers read | d15 | [S], abstract only |

## 4. Mechanisms and models

Each mechanism is written so it can be coded. None has a validated parameter set. Where a number is needed we say it is a choice we would make.

### 4.1 The pipeline (stage 1 to 3) as data flow

```
evidence items E = {e1..en}  (each with source, credibility tag, position in presentation)
        |
  [BUILD]  infer causal links among items, fill gaps from world knowledge
        |
  story S = nested episodes: (initiating event -> goal -> action -> consequence -> state)
        |                                   ^ inferred links are marked 'inferred'
  [CATEGORIES]  verdict V_k = conjunction/disjunction of features (identity, mental state, circumstances, actions)
        |
  [MATCH]  for each V_k: fraction of features that S satisfies; choose best; apply default if none met
```

An engineer can implement this as three typed slots (G: model fills a slot, code decides what happens next):

- **Slot 1: story.** The model writes, for each candidate answer, an episode list. Each link carries `supports = [evidence ids]` or `inferred = true`.
- **Slot 2: categories.** The answer criteria (the task's "verdict elements") are parsed once into a feature list per candidate answer.
- **Slot 3: match.** Code computes feature satisfaction by lookup against the story links. The model is not asked to grade its own story.

### 4.2 Certainty scores in code

The authors give no functional form (b02). A usable version, flagged as our choice:

| Score | How code computes it | Note |
|---|---|---|
| Coverage | share of evidence items (from a code-extracted list) cited by at least one story link | VeriScene counts cited evidence files exactly this way (b31). It is a count, not a correctness check (b31 limits). |
| Coverage, stricter | LLM judge lists atomic details of the observations and marks which ones the story explains (CEDAR, d11) | judge has no authorship; adds tokens |
| Consistency | no two links in the story contradict, checked by code over typed claims (IBE-Eval used a Prolog proof, a27) | alone it is weak: LLMs write consistent stories for wrong answers (a28) |
| Parsimony | proof depth and concept drift (a27, c13) | wrong explanations are about 6% deeper and about 10% more drifted on average |
| Plausibility | entailment score per step (a27 coherence) | IBE-Eval coherence alone .66 on COPA |
| Hedging | count of uncertainty words | linguistic uncertainty alone .70 on COPA and the strongest single predictor in the regression (a28) |
| Uniqueness | gap between the best and second-best story on the combined score | the model's own uniqueness idea; no LLM test exists |

IBE-Eval is the only measured evidence on which story-quality features separate right from wrong LLM-written stories: combined features beat any single one, and consistency alone fails (K15 [E]). The best single feature there is not consistency.

### 4.3 Order effects

The mechanism the authors give (a16, d03): story order makes the story easy to build, so the side presented in story order is believed more, and the other side's weak story is lost. Recall clustering follows the order given, total recall is unchanged. The order effect is on how evidence is organised, not on how much is remembered.

Implementable form: the order in which facts are shown to an LLM changes what it builds. The LLM evidence is about order of facts in general (d06, d07) and about recency in guilt ratings (a24-a26). The exact juror manipulation (causal-chronological vs source-by-source) is untested in LLMs (critique gap 2).

### 4.4 Global versus item-by-item mode

Humans switch process by response format (a16, d04). With one end-of-case judgment, they use a story-weight process, and the judgment is about 1.5 times more extreme than the last item-by-item rating. With a rating after each item, they use anchor-and-adjust. For LLMs, asking for an intermediate rating raised final guilt in GPT-4o (a26). So "ask for a rating after each block" is not a neutral instrument.

### 4.5 Coherence shift

State variable: current leading answer L. Rule observed in humans: later evidence is judged more favourable when it supports L (a32, b21). In LLMs the nearest measured effect is a pull toward the model's own earlier wrong candidate (d12) and a larger effect of an intermediate rating (a26). A code-level guard: do not show the model its own earlier answer before it has processed all evidence (consistent with G1).

### 4.6 What the model leaves unspecified (so code must choose)

- How the five principles combine. No weights.
- How a story is built from raw evidence (the inference step itself is a black box).
- What counts as "the same story" when two jurors build slightly different ones.
- How rival stories are generated (jurors often build only one; uniqueness is then not computable).

## 5. What holds up

### 5.1 Replications

- **Story order effect.** Original (1988, N=130) plus a replication with new materials (1992, N=414) plus a cited Smith 1988 (K27). Direction holds in both. No effect sizes or test statistics have been read. No dated failure to replicate was found in several searches (d17). A dissertation suggests the pattern reverses between students and community members (d16, not opened, about 2009, not peer-reviewed). Treat the order effect as lab-robust, field size unknown.
- **Global versus item-by-item.** Two experiments inside the 1992 paper (d04). No independent replication found.
- **Quantitative test of the certainty principles.** One study (Willmott 2018, b11-b14). The authors say the principles had never been directly tested as verdict drivers before this (b14). One case, mostly not-guilty verdicts (22 of 27 panels).
- **Post-2000 studies that cite the model** (Curley 2022, Lilley 2026, Burd 2025, Lin and Paterson 2026) do not manipulate story variables (b17, b18, b19, b23). They use the model to explain results afterwards. That is weak support (a18 limits).

### 5.2 Failures and tensions

| Item | What happened | Source |
|---|---|---|
| Expert testimony timing | Story model predicted help from testimony before the eyewitness; recency predicted help after. Neither won. N=222. | b19 |
| Primacy vs recency | Law students (N=407) showed recency, not primacy, which does not fit a clean story-order account. | b22 |
| LLM recency | Strong recency in GPT-4o, weaker in GPT-5.2 and in humans (also recency). A story model predicts organisation effects, not simple last-item weight. | a24, a25 |
| O.J. Simpson | Coherence maximising alone accepts guilt; model description needs emotion and group factors. | a21, c25 |
| Evidence anchors | An early piece of evidence did not predict verdict; pre-trial bias did. | b17 |
| Post-hoc fit | The model is used to explain both outcomes in the same study (myths fill gaps for acquittal; coherence for conviction). | b23, c06 |
| Undefined constructs | Coherence, completeness and uniqueness have no formal definition. | a20 |
| Neural fit | Narrative model fits better than utility, but additive weights fit case-strength ratings too. | b15, b16 |

### 5.3 Moderators and boundary conditions

- **Response format**: global versus item-by-item changes the process (a16, d04).
- **Participant type**: students versus community (d16, unconfirmed).
- **Case type**: typical criminal cases only. Violent, racially charged, emotional cases were not studied (a06). Emotion shifts evidence weighing (b21).
- **Prior beliefs and myths**: fill story gaps (b23, c06).
- **Group**: deliberation can reverse individual leaning (b07). The LLM version of this fails by anchoring (17 of 18 hung; b29).
- **Verdict form**: special verdicts with reasons shift verdicts strongly (b18), but the unit is the jury and the direction may be a stricter standard rather than better accuracy.

### 5.4 Interventions that worked and did not (all human or LLM, as stated)

| Intervention | Result | Species |
|---|---|---|
| Present evidence in story order | moved verdicts by up to 47 points between extreme cells (78 vs 31) | humans (d01) |
| Special verdict with reasons | fewer findings for plaintiff; 92.6% vs 40.9% not liable at jury level | humans (b18) |
| Judicial rehabilitation instructions | did not reduce emotion-driven coherence shift | humans (b21) |
| Prompt "be meticulous" | cut GPT-4o order effect by 0.32 points; never removed it | LLM (c09) |
| Prompt "act as an expert" / "be ready to justify" | no reliable effect | LLM (c09) |
| "Open-minded" instruction in jury debate | worked on Llama-4-Scout (2.0 to 6.0 vote changes), ignored by GPT-4o (1.0) | LLM (b29) |
| Code-checked audit loop on evidence fusion | coverage 0.9014 vs 0.8436 without it | LLM (c14) |
| Reasoning budget | GPT-5 and Claude 3.7 extended thinking reached exact-match 1.00 on timeline ordering at every list size | LLM (d09) |
| Stratified decoding | reduced loss of hypothesis uniqueness | LLM (d15, abstract) |

## 6. Language models

### 6.1 The headline

No LLM study found manipulates the story-model constructs (coverage, uniqueness, story order) as the independent variable (K19 [S], b32, d20). That is an absence claim from limited search; Semantic Scholar and OpenAlex were rate-limited and arXiv search returned 429. Everything below is the nearest relevant work.

### 6.2 Order and recency

- **GPT-4o on six Polish criminal cases (a24-a26, c08, c09).** Evidence order moves guilt strongly. Final guilt (1-10) with incriminating evidence last was 6.04 (with an intermediate rating) or 4.77 (without). With exonerating evidence last: 4.24 and 3.54. F(1,711)=424.76. 720 trials per model.
- **GPT-5.2.** The effect drops: F(1,711)=71.24. The newer model is less biased but not unbiased. Intermediate-rating inflation appears only with incriminating evidence last (5.02 vs 5.35).
- **Humans in the same design (Wojciechowski et al. 2025, not rerun):** order F(1,686)=54.40, 120 participants. Humans are not a clean baseline.
- **What changed it:** model upgrade (F 424.76 to 71.24); "be meticulous" prompt (-0.32 points, p=.003 for GPT-4o). Expert framing and justification did not reliably help.
- **Caveats:** simplified cases, one rating scale, human data from a separate study (a24 limits). "I-G" in the paper's labels means incriminating last (a24 limits).

### 6.3 Order of facts in general

- **Test of Time (d06).** Shuffled facts score lowest. Gain from shuffle to the best order: Claude-3-Sonnet +27.9 points (45.71 to 73.57), Gemini 1.5 Pro +12.0 (63.04 to 75.00), GPT-4 +4.6 (60.71 to 65.36). Same tokens. The best order was sorting by entity and time, not a causal story.
- **Premise order (d07).** Putting premises in proof order is best for every model tested. Drops of 20 to over 40 points at 12 rules for weaker models.
- **Chronology (d09).** Models keep local order but lose a single global timeline as lists grow: GPT-4.1 exact match on historical events 1.00 at n=2, 0.45 at n=5, 0.10 at n=10, 0.00 at n=20. Reasoning budget fixed it (1.00 at every size for GPT-5 and Claude 3.7 with extended thinking). Building a timeline of events, the first step of a story, is itself unreliable without reasoning budget.
- **Source position (d08).** Llama trusts earlier sources; GPT-4o often trusts the last; Gemma and o3-mini mostly do not. Order fixes must be tested per model (K23).

### 6.4 Stories and explanation quality

- **IBE-Eval (a27, a28, c12, c13).** GPT-3.5 and Llama 2 7B/13B. Models over-rationalise: consistency scores are similar for right and wrong options. Wrong options carry about 6% more proof depth and about 10% more concept drift. Combined features reach up to 77% (chance 50%), +17.5 over a GPT-3.5 judge. Two humans picked the right explanation 96% (COPA) and 91% (E-CARE) on 100 pairs.
- **Douven 2026 (a29).** 16 models from 7 developers reproduce human patterns of inference to the best explanation in three experiments (sensitivity to explanation quality, suppression by an alternative, quality gap and confidence). Temperature 0. Effect sizes not read.
- **MuSR murder mysteries (c16, c17).** GPT-4: 64.8 (regular), 65.6 (CoT), 80.4 (CoT+ strategy described), 86.0 (1-shot CoT+). Human 94.1. Hard-coded decomposition (motive, means, opportunity per suspect) scored 77.6 zero-shot, no better than CoT+.
- **True Detective (c18).** Vanilla GPT-4 27%, CoT 38%, golden reasoning chain 83%, random 24%, average human 47%. Reaching the explanation, not checking it, is the bottleneck.
- **HypoSpace (d15).** Validity stays high while uniqueness and recovery fall as hypothesis space grows. Abstract only.

### 6.5 Coverage

- **VeriScene (b31, c14, c15).** Evidence-to-narrative with a three-round code audit and per-claim citations. Coverage 0.9014 with the audit, 0.8436 without the fusion audit, baseline 0.000 (no citations). Factual consistency +20.3%, temporal coherence +34.9% over an end-to-end multimodal model. A cheap orchestrator kept coverage (0.936) because code checks do the work, but temporal coherence fell to 0.118. Synthetic scenes, 25 scenarios. PDF corrupt on re-check.
- **CEDAR-GRPO (d11).** An LLM judge lists observation details and checks which the hypothesis explains. As an RL reward it lifted coverage from 33.1% to 52.9% and accuracy by 2 to 3 points over correctness-only ablations. It transfers to held-out sets. Training, not prompting; token cost of a prompt-time audit is unmeasured.

### 6.6 Rival hypotheses and calibration

- **Distractor prompting (d10).** Mean ECE down 0.260 across 27 pairs, but worse on the easy dataset for GPT-4-turbo and GPT-4o. Mostly a format effect.
- **Early commitment (d12, d19).** Open models weight their own prior answer at 0.20-0.65 (arithmetic) yet are pulled toward their own most common wrong answer (positive in 9 of 9). Anchoring studies report that prompt-level fixes largely fail (search summaries only).
- **Motivated updating in legal text (d13).** Overview page only: strong early evidence for one side lowers weight on later contradicting evidence; default LLM alpha=1.05, beta=0.38, tau=0.71. Not primary.

### 6.7 Mock jurors and courts

- **Level versus humans (c07, d18).** GPT-4o, Claude 3.5 Sonnet and o1 gave guilt probability 63.56 vs humans 58.82, but guilty verdicts 21% vs 49% (2,304 responses). Direction of effects matched humans, but verdict thresholds differ greatly. No story-based prompt arm exists.
- **JuryBench (b28).** 20 LLMs, 500 US criminal cases, about 432K decisions. Echoes human findings (emotional appeals can backfire, favour defendants like themselves). Does not test coverage or story coherence.
- **Patel et al. (b30).** 26 LLMs, 25 reasonableness questions, 500 humans. LLM answers were more homogeneous and sometimes treated a variable standard as a fixed rule.
- **Deliberation (b29, c10, c11).** 12 LLM jurors almost never changed minds: 17 of 18 runs hung. First-vote anchoring.
- **Court-simulation systems (c19-c24).** SimCourt, AgentsCourt (F1 +8.6% first instance, +9.1% second instance), civil court simulation, trait-conditioned persuasion, AUTOLAW, AgenticSimLaw. None tests a story manipulation. AgenticSimLaw found only negligible gains over the best zero-shot baseline. They reward fluent argument or charge match, not story correctness.
- **IRAC-R1 (d14).** Training a 7B model on issue-rule-application-conclusion traces: 47.9% to 58.1% on Bar-exam QA. Fine-tuning, no generic-CoT baseline on the page, no story-first arm.

### 6.8 Net reading

LLMs build fluent stories for any answer and do not reliably drop or flag wrong ones (K15). Evidence order matters (K12, K22). Early commitment pulls (K26). Raw prompting drops evidence unless code audits coverage (K16). Prompt-only fixes help little (K13). Whether a story-first scaffold beats answering from raw evidence at equal tokens has not been measured by anyone.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status per SCHEMA.md marks.

### Add now (established)

Established items below are ones where the finding itself is [E]. Several cost no tokens. Per G7, each is kept only if the run log shows it does not lose to the plain model, so "add now" means "add as default, log it, drop if it fails".

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Present facts in a sorted, non-shuffled order** (by entity and time, or in the order a solution would use them), never as a raw dump. Free in tokens. | S2 REPRESENT / S1 input hygiene | [E] | K22: d06, d07, d09 |
| A2 | **Do not trust a fluent, consistent story as a signal of correctness.** Consistency alone does not separate right from wrong LLM-written explanations; scoring must use several features or run a check. This is G10 applied to stories. | G10 reinforcement; S7 | [E] | K15: a27, a28, c12, c13 |
| A3 | **No intermediate scoring or tentative answer between evidence blocks** unless the loop needs it. An intermediate guilt rating inflated GPT-4o final guilt by 0.70 to 1.27 points. Consistent with G1. | G1 | [E] | K12: a26; K07: a32, b21 |
| A4 | **Do not use prompt-only wording fixes for order bias** ("be meticulous" gives -0.32 points, never removes it). Matches 4b. | 4b (not to add) | [E] on the phenomenon, [S] on the size | K13: c09 |
| A5 | **Do not rely on multi-agent debate to pick between stories.** First-vote anchoring: 17 of 18 hung. Matches G9. | G9 | [E] | K18: b29, c10 |
| A6 | **Verdict thresholds differ from human levels** (21% vs 49% guilty with similar probabilities), so any cutoff on a model's score must be calibrated on our own bench, not copied. | G5 / S0 class record | [E] | K14: c07, d18 |

### Test first (single-source, contested, or untested for LLMs)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Causal-chronological story order of the facts** vs source-by-source order, same facts, equal tokens. The juror manipulation, never run on an LLM. | S2 REPRESENT | [E] for humans, untested for LLMs (K02, K22) | d01, d03, d06, d07 |
| T2 | **Two-order check:** run the item in two evidence orders in separate contexts, flag disagreement, and use the agreement or an order-averaged answer. | G (order robustness) / S8 | [S] (K12, K23) | a24, a25, d08 |
| T3 | **Rival stories with coverage and uniqueness scores in code** (build 2+ stories, score each, report the gap). Gate it by first-pass confidence (K24). Beware: 4b says a full ACH matrix showed no gain; this test must beat that baseline, not assume it. | S7 SELECT / O-generate | [S] (K03 is [E] for humans only) | a03, b02, d10, d15 |
| T4 | **Coverage audit:** code lists the evidence items, the model cites which ones its story uses, code counts the uncited. Optional LLM judge for atomic details. | S8 VERIFY | [S] (K16, K25) | b31, c14, d11 |
| T5 | **Tag each story link as given or inferred**, then check how often an inferred link is later cited as source evidence. | S2 REPRESENT | [S] (K21) | d05 |
| T6 | **Credibility audit** of each source before the story is built: plant a coherent story from an unreliable source and see whether an explicit audit step lowers acceptance. | G / S8 | [E] for humans (K06), untested for LLMs | b03, c03, a15, b21 |
| T7 | **Read the answer criteria before building the story** (judge-style backward) vs after (juror-style). N=4 judges is the only support. | S1 / S2 | [S] (K05) | a07, b05, c02 |
| T8 | **Element-by-element checklist vs one global answer**, same items. Humans: item-by-item is weaker and shaped by anchor-and-adjust; unit and direction of the special-verdict effect are unclear. | G (stepwise checks) | [S] (K10, K20) | b18, d04 |
| T9 | **Early tentative answer vs none** (coherence shift in an LLM). | G1 | [S] (K26) | d12, a26 |
| T10 | **Computed coherence score per rival story** (ECHO-style or simpler) vs the model's own pick. | S7 | [C] (K09) | a19, a21 |
| T11 | **Score each rival story separately on 0 to 1** instead of forced choice (humans hold weak belief in both; r=-0.30). | S7 | [S] (K04) | b11-b13 |

## 8. Concrete tests on our bench

All tests compare arms at equal total tokens (setup counted, per G7). Items are drawn from the bench's multi-fact reasoning sets with a checkable answer, plus MuSR-style murder mysteries and True Detective-style puzzles where available. Report accuracy, plus calibration where confidence is asked. Run each arm with at least 3 seeds per item and report the paired difference with an interval; a result inside the plain model's seed-to-seed spread counts as no effect. Expected effects are guesses based on the studies cited; none is established for our setup.

| # | Item type | Arm A | Arm B | Metric | Expected effect |
|---|---|---|---|---|---|
| E1 | multi-fact items where facts can be ordered causally (MuSR murder mystery, True Detective-style, temporal items) | source-by-source order of facts | causal-chronological order of the same facts (and a shuffled third arm) | accuracy | B over A by a few points; shuffled lowest. Test of Time shows 4.6 to 27.9 points shuffle-to-best, depending on model (d06). Smaller for stronger models. |
| E2 | same items | single pass, one order | two passes in swapped orders, agreement or order-averaged answer, matched total tokens (A uses two independent samples to match) | accuracy; disagreement rate | disagreement rate flags wrong answers; accuracy gain only if order bias is large. Humans' bias is not the target; GPT-4o-like models show F=424 on guilt ratings (a24). |
| E3 | items with competing explanations, including ones where the plain model is wrong with high confidence | answer directly | build 2+ rival stories, code-computed coverage and uniqueness, choose the best-covering | accuracy and ECE (confidence calibration) | better calibration on hard items, possibly worse on easy ones (d10). Gate by first-pass confidence and compare. |
| E4 | long-evidence items (20 or more facts) | free-form story then answer | story where each link must cite evidence ids; code counts uncited ids; one repair pass for uncovered items | evidence coverage; accuracy; extra tokens | coverage up (VeriScene 0.8436 to 0.9014 range); accuracy gain only if dropped evidence is decisive. |
| E5 | items with a planted unreliable but coherent source | story first | credibility audit of each source, then story | acceptance of the planted story; accuracy | lower acceptance of the planted story; humans under-weight credibility (b03). |
| E6 | items with explicit answer criteria (rule application) | read criteria after building the story | read criteria first, then build the story to them | accuracy | small or none; support is N=4 judges. |
| E7 | multi-block evidence items | no mid-way answer | ask for a tentative answer after block 1, then continue | change in final answer vs no-tentative control; accuracy | final answer drifts toward the tentative one (a26, d12). Expect accuracy loss if the tentative answer is wrong. |
| E8 | items with 3+ plausible answers | one global answer | element-by-element checks per answer, then pick | accuracy; strength of confidence | item-by-item answers weaker and more calibrated; accuracy unknown (d04). |
| E9 | story-link tagging | no tags | each link tagged given or inferred; code reports cited inferred links as evidence | rate of inferred links cited as given; accuracy | rate falls with tags; accuracy effect uncertain. |
| E10 | threshold calibration | direct verdict | story-based prompt, then verdict | positive-verdict rate vs gold rate | tests whether the 21% vs 49% gap (c07) moves with a story prompt. |

## 9. What does not transfer, and why

- **Jury group dynamics.** 12 LLM jurors hang by anchoring (b29). We use one agent. Deliberation findings do not apply, and G9 already bars debate.
- **The default to not guilty.** It is a legal rule layered on the match, not a feature of stories (a04). Our tasks have no asymmetric burden of proof.
- **Emotion, group identity and race.** Part of the Simpson verdict and of coherence shifts (a23, b21). Not a variable for our agent, though the rule "an early lean re-weights later evidence" does transfer (T9).
- **Legal terms reinterpreted through the story.** Stage-two failures (a04, a05) come from one-trial learning of abstract definitions by humans. An LLM reads the criteria directly; whether it reinterprets them is a separate, untested question (T7).
- **Human working-memory limits as the reason for story building.** Humans need a story to compress a long trial. An LLM can hold the evidence in context. Whether compression into a story still helps is open (E1, E3).
- **Mock-juror samples.** Mostly students or online panels, short vignettes, written materials (b17, b19, b22, d01). Effects at real-trial scale are unknown, as the authors admit (d02).
- **Verdict form effects (special verdicts).** The 92.6% vs 40.9% figure is at jury level after deliberation and may reflect a stricter standard (b18). Do not use as evidence that stepwise checking raises accuracy.
- **Brain-imaging results.** Reverse inference from topic maps, N=29, prosecution evidence only (b15). No agent action follows.
- **Court-simulation systems.** They measure charge or sentence match or persuasion, not story correctness (c19-c24).
- **Murder-mystery benchmarks.** Synthetic, two suspects, closer to element matching than story construction (c16).
- **Recency in guilt ratings.** A rating-scale effect on a single number. Its link to story building is not shown (a24 limits).

## 10. Open questions

1. What are the test statistics and effect sizes of the order experiment? Only the four cell percentages are known; the original 1988 and 1992 papers were never opened (critique gap 1).
2. Does causal-chronological order of facts help an LLM beyond sorted-by-time order? (E1.)
3. Does building two or more rival stories and reporting coverage and uniqueness improve calibration over single-story answering? (E3; critique gap 3.)
4. Which story-quality measure best separates right from wrong LLM stories: coverage count, consistency, entailment, hedging? Only IBE-Eval compares several and there consistency fails (critique gap 4).
5. Are there replications or failures of the order effect from 2000 to 2026? None found; the sample-dependent reversal hint (d16) is unconfirmed (critique gap 5).
6. Does a coverage audit transfer to non-forensic tasks at prompt time, and what does it cost in tokens? Transfer shown only as RL reward (d11); VeriScene is forensic (critique gap 6).
7. How big is the story-first versus verdict-first difference, and does it depend on task type? Only N=4 judges (critique gap 7).
8. Does an early tentative answer cause coherence shift in LLMs, and by how much? (critique gap 8.)
9. Does stepwise element checking raise accuracy or only shift thresholds? (critique gap 9.)
10. Does a story-based prompt change the verdict-threshold gap between LLMs and humans (critique gap 10)?
11. Do the five certainty principles combine additively, and with what weights? No one has fitted this; Willmott 2018 gives scale scores but one case (b11).
12. Is the story form itself causal, or only a convenient description of coherence-based reasoning? (b07 critique; rival accounts fit similar data.)
13. Do stronger or reasoning models (GPT-5.2, extended thinking) make order fixes unnecessary? GPT-5.2's order F dropped from 424.76 to 71.24; chronology exact-match reached 1.00 with reasoning budget (d09).
14. Do the stage-two failures (reinterpreting criteria through the story) occur in LLMs?

## 11. Sources

[V] = opened and read as text this session or in the earlier research pass. [M] = metadata, abstract, snippet or secondary summary only. Where critique.md says a source could not be re-opened, the original flag is kept but noted.

**Founding and theory**

- [M] Pennington and Hastie 1986, Evidence evaluation in complex decision making. https://doi.org/10.1037/0022-3514.51.2.242 (a30; not opened)
- [M] Pennington and Hastie 1988, Explanation-based decision making. https://doi.org/10.1037/0278-7393.14.3.521 (a31; not opened)
- [M] Pennington and Hastie 1992, Explaining the evidence (abstract only). https://synapsesocial.com/papers/W1984737313 ; https://doi.org/10.1037/0022-3514.62.2.189 (a16, b09, b10)
- [V] Pennington and Hastie 1993, The story model for juror decision making, ch. 8 in Inside the Juror. https://www.marcellodibello.com/legal-probabilism/readings/Hastie-story-model.pdf (d01-d05)
- [M] Same chapter, publisher page (bibliographic only). https://www.cambridge.org/core/books/inside-the-juror/story-model-for-juror-deci (b08)
- [V] Hastie and Pennington 1993, Implications of the Story Model for the Trial Judge's Behavior. https://ciaj-icaj.ca/wp-content/uploads/documents/import/1993/HASTIE.ED.pdf (a01-a08, b01-b06, c01-c03)
- [V] Hastie and Pennington 1996, The O.J. Simpson stories. https://lawreview.colorado.edu/wp-content/uploads/2026/02/Hastie-Pennington.pdf (a09-a11)
- [V] OpenLearn, Jury decision making: what's the story? https://www.open.edu/openlearn/society-politics-law/law/jury-decision-making-wha (a12, b07; fetch summary)
- [V] Czaban (ELTE) summary of the order experiment. https://ojs.elte.hu/jesz/article/download/6933/5403/13965 (a13, a15; now 403; secondary)
- [M] Onfiction.ca blog, juries and stories. https://www.onfiction.ca/2011/09/juries-and-stories.html (a14)
- [M] Devine et al. 2001, 45 years of jury deliberation research. https://doi.org/10.1037/1076-8971.7.3.622 (b35)

**Rival and computational accounts**

- [V] Byrne 1995, convergence of explanatory coherence and the story model. http://chil.rice.edu/byrne/Pubs/cogsci95.pdf (a19, a20)
- [V] Thagard 2003, Why wasn't O.J. convicted? https://arts.uwaterloo.ca/~pthagard/Articles/OJ.pdf ; https://doi.org/10.1080/02699930302297 (a21-a23, c25)
- [M] Holyoak and Simon 1999. https://doi.org/10.1037/0096-3445.128.1.3 (a32)
- [M] Simon, Pham, Le and Holyoak 2001. https://doi.org/10.1037/0278-7393.27.5.1250 (b33)
- [M] Bex and Verheij 2010. https://doi.org/10.1007/s10506-010-9092-x (b34)
- [V] Shengelia and Lagnado 2020, Bayesian causal reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC7892609/ (b20)
- [V] Evidence, probability and relative plausibility 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9465537/ (b26; abstract and opening)
- [V] Fuzzy-trace and witness testimony 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8508426/ (b24)
- [V] Narrative in intelligence analysis 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC6944337/ (b27)

**Human studies after 2000**

- [V] Willmott et al. 2018, Juror Decision Scale. https://repository.lboro.ac.uk/articles/journal_contribution/Introduction_and_va (b11-b14, c26; later 403, numbers single-read)
- [V] Castrellon et al. 2022, neural support for utility and narrative. https://pmc.ncbi.nlm.nih.gov/articles/PMC9546442/ (b15, b16; re-opened in critique)
- [V] Curley et al. 2022, Verdict spotting. https://pmc.ncbi.nlm.nih.gov/articles/PMC9310652/ (a18, b17, c05)
- [V] Burd et al. 2025, Diverging decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC12729272/ (a17, b18, c04; re-opened, corrections in critique)
- [V] Lin and Paterson 2026, contemporaneous notes. https://pmc.ncbi.nlm.nih.gov/articles/PMC13618115/ (b19)
- [V] Emotion, evidence evaluation and verdict 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12292101/ (b21)
- [V] Law and order effects 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9186347/ (b22)
- [V] Intimate partner rape and rape myths 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13124532/ (b23, c06)
- [V] Gittings, Giffin and Salerno 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12730021/ (b25)
- [M] Reardon dissertation (FIU). https://digitalcommons.fiu.edu/dissertations/AAI3343274 (d16)
- [M] Law review snippet on opening statements. https://repository.law.umich.edu/cgi/viewcontent.cgi?article=3386&context=articl (d17)

**LLM and AI studies**

- [V] Bessis et al. 2026, Legal decision biases in GPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC13024114/ (a24-a26, c08, c09; re-opened in critique)
- [V] Dalal et al. 2024/2025, IBE-Eval. https://aclanthology.org/2024.acl-long.14.pdf ; https://arxiv.org/abs/2402.10767 (a27, a28, c12, c13; re-opened)
- [M] Douven 2026, Abduction in silico. https://link.springer.com/article/10.1007/s11023-026-09803-x (a29; abstract and notes)
- [M] Sun et al. 2025, LLMs as jurors. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1037/lhb000 ; https://www.utupub.fi/bitstreams/41dd9017-bbc2-4c89-9bd2-de03c4803325/download (c07, d18; abstract or search summary)
- [V] Wu 2026, JuryBench. https://arxiv.org/pdf/2609.09887 (b28; single-read)
- [V] Ersoz 2026, 12 Angry AI Agents. https://arxiv.org/abs/2605.01986 ; https://arxiv.org/pdf/2605.01986 (b29, c10, c11; single-read)
- [V] Patel, Wenger and Buccafusco 2026. https://arxiv.org/pdf/2609.06769 (b30)
- [M] Fu et al. 2026, VeriScene. https://arxiv.org/abs/2609.08342 ; https://arxiv.org/pdf/2609.08342 (b31, c14, c15; PDF corrupt on re-check, so single-read)
- [V] Sprague et al. 2024, MuSR. https://arxiv.org/abs/2310.16049 (c16, c17)
- [V] Del and Fishel 2023, True Detective. https://arxiv.org/abs/2212.10114 (c18)
- [V] Zhang et al. 2025, SimCourt. https://arxiv.org/abs/2508.17322 (c19; abstract, intro, setup)
- [V] He et al. 2024, AgentsCourt. https://arxiv.org/abs/2403.02959 (c20)
- [M] Chen et al. 2026, Civil Court Simulation. https://arxiv.org/abs/2606.09632 (c21; abstract)
- [V] Siedler 2026, trait-conditioned persuasion. https://arxiv.org/abs/2604.07028 (c22)
- [V] Nguyen, Pham and Sun 2025, AUTOLAW. https://arxiv.org/abs/2505.14015 (c23)
- [V] Chun, Elkins and Lee 2026, AgenticSimLaw. https://arxiv.org/abs/2601.21936 (c24)
- [V] Fatemi et al. 2024, Test of Time. https://arxiv.org/pdf/2406.09170 (d06)
- [V] Chen et al. 2024, Premise order matters. https://arxiv.org/abs/2402.08939 (d07)
- [V] SMeL Test 2025. https://arxiv.org/pdf/2508.02074 (d08; discussion paragraph only)
- [V] Do LLMs understand chronology? 2025. https://arxiv.org/html/2511.14214v1 (d09; first 100,000 characters)
- [V] Chhikara 2025, Mind the confidence gap. https://arxiv.org/html/2502.11028v3 (d10)
- [V] CEDAR-GRPO 2026. https://arxiv.org/pdf/2608.14791 (d11)
- [V] Evidence Integration in LLMs 2026. https://www.alphaxiv.org/abs/2609.04290.md (d12; first 100,000 characters)
- [M] The Challenge of Simulating Human Strategy 2026 (overview page). https://www.alphaxiv.org/overview/2606.17657 (d13)
- [M] IRAC-R1 2026. https://icml.cc/virtual/2026/80627 (d14; abstract page)
- [M] HypoSpace 2025. https://arxiv.org/abs/2510.15614 (d15; abstract)
- [M] Anchors in the Machine / Anchored Confabulation. https://arxiv.org/pdf/2511.05766 (d19; search summaries)
- [M] Negative-search note, related hypothesis work. https://arxiv.org/abs/2412.13422 (d20); DataCite search (b32)

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 11 established claims: 5 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E11.01-K01** (now single-source: the sources are not independent). The three Hastie-Pennington chapter lines are one document and the 1992 experiments are the same authors' own tests, so the story-model description rests on a single lab; the independent OpenLearn summary (blocked) is a secondary account that itself lists critiques.
- **E11.01-K03** (reworded: the sources support less). The five properties and the uniqueness rule are Hastie and Pennington's theoretical certainty principles (one chapter listed three times, plus their own 1996 article); the only independent check, Willmott et al. 2018, is a scale validation giving 'early evidence' of the certainty-principle process, not a demonstration that acceptance and confidence track each property. Corrected claim: Hastie and Pennington's Story Model holds that acceptance and confidence depend on a story's coverage, completeness, consistency, plausibility and uniqueness, and that two coherent stories lower confidence; independent support is limited to a scale validation (Willmott et al. 2018, n=324) that reports early evidence for this certainty-principle process.
- **E11.01-K06** (reworded: the sources support less). In the Hastie-Pennington chapter this is a theoretical implication of the model ('This means that... jurors will be swayed...'), not a measured result, and it is the authors' own advice to judges; the emotion mock-jury study (PMC12292101) tests affect-driven evidence evaluation, not under-weighting of credibility or inference-chain strength relative to an ideal evaluator, and the Czaban item is a Hungarian secondary relay. Corrected claim: Hastie and Pennington's Story Model predicts that, compared with an ideal evidence evaluator, jurors will be swayed by the consistency and plausibility of a story and under-weight source credibility and inference-chain strength, and they advise judges to stress procedural instructions on credibility and inferential strength; this is a model-derived prediction, with no quantified effect in the sources opened.
- **E11.01-K07** (reworded: the sources support less). Phalen et al. 2025 (N=713, 677, 651) confirmed but the authors call it correlational/mediational, and the second source (Thagard, scanned PDF) was unreadable and is about OJ polls, not re-weighting by a leading verdict. Corrected claim: In three mock-jury studies (N=713, 677, 651), greater negative emotion toward the defendant was associated, via mediation, with more agreement with unrelated plaintiff evidence and less with unrelated defence evidence, and with more liable verdicts; judicial rehabilitation did not reduce this (correlational, single lab).
- **E11.01-K14** (reworded: the sources support less). Numbers (2,304; 63.56 vs 58.82; 21% vs 49%) verified in Sun et al., but only some effects replicated: reporting delay did not (LLMs sensitive, humans not); Wu 2026 does not test level divergence. Corrected claim: LLM mock jurors diverge from humans in level (guilt probability 63.56 vs 58.82 but guilty verdicts 21% vs 49%; 2,304 responses); the defendant-race bias and the rise with more allegations replicated, but sensitivity to reporting delay appeared only in the LLMs.
- **E11.01-K22** (reworded: the sources support less). Test of Time Table 7 numbers match, but for GPT-4 shuffle (60.71) is not the lowest (StartTimeAndRelation 60.54); the paper's 'consistently lowest' is slightly off, 'at equal tokens' is not stated; premise-order drops are up to 20-30 points for GPT-4-turbo/PaLM 2-L (about 16-21 at 12 rules) and over 40 only for weaker models, not a uniform 20 to 40+. Corrected claim: Reordering the same facts changes LLM accuracy: on Test of Time shuffled facts score at or near the lowest (GPT-4 60.71 vs 65.36 best; Gemini 1.5 Pro 63.04 vs 75.00; Claude-3-Sonnet 45.71 vs 73.57), and in deduction (Chen et al. 2024) forward (proof-order) premises beat other orders for every model, by up to 20-30 points for GPT-4-turbo and PaLM 2-L and by over 40 points for weaker models such as Gemini 1.0 Pro and GPT-3.5-turbo.
