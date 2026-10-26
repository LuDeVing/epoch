# Schema induction: deep document

*Subfield A11.04. Written from evidence_a-d.jsonl (a01-a31, b01-b29, c01-c26, d01-d19), claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids are cited in brackets. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Where critique.md corrected an evidence line, the corrected value is used here.*

---

## 1. What it is

Schema induction is learning an abstract rule or structure by comparing concrete cases. The learner sees two or more solved examples. It finds what they share and what is irrelevant. It keeps the shared structure as a schema. It then uses the schema on a new problem that looks different on the surface.

Three layers matter.

1. **Induction.** Build the schema from cases. Human work asks: does comparing two cases give a better schema than studying one?
2. **Access.** Notice, later, that a new problem fits the schema. This is the retrieval problem. A neighbouring subfield (analogical access) covers it. We only note where it limits induction.
3. **Application.** Use the schema to solve the new problem. This is where most errors are, even after the schema is correct.

For our agent there are two families of method.

- **Human-style induction** (Gick and Holyoak, Gentner): two worked cases, a forced comparison, a stated rule, a transfer test.
- **LLM abstraction methods**: state the principle before solving (step-back), plan at an abstract level before concrete steps (abstraction-of-thought), self-generate cases (analogical prompting), build a reasoning structure once per task class (Self-Discover), keep a store of reusable templates or routines (Buffer of Thoughts, Agent Workflow Memory, ReasoningBank).

The key fact up front: **no published study tests the human recipe on a language model at equal tokens** (critique gaps 1 and 2). Everything about models below is indirect.

Links to other subfields in this run (not covered here): analogical access (retrieval of the right stored case), library learning (turning solved subgoals into tools), chunking and template theory, fixation (a single case can anchor), evaluation of creativity.

---

## 2. History and theories in depth

### 2.1 Gick and Holyoak 1983: the founding experiments

**Problem and base rate.** Duncker's radiation problem. About 10% solve it with no story (a02, b06). About 30% solve it before a hint after reading one relevant story and being asked to recall or summarise it.

**Theory.** A schema is defined by the correspondences between two analogs [a01]. A single story keeps the schema implicit, tied to its surface details. A second story, mapped to the first, lets the shared structure become explicit and detachable.

**Six experiments, read from the PDF [a02-a08, b01-b06]:**

| Exp | Manipulation | Result (pre-hint / total solved) |
|---|---|---|
| 1 (cord problem) | story analog vs control; recall vs summary instruction | analog 71% vs control 20% pre-hint; 98% vs 30% total. Recall 68% vs summary 75%. About 25 per cell, 69 subjects |
| 2 (N=88) | one analog + principle; one analog; principle alone | 32/80 (N=31), 29/79 (N=28), 28/66 (N=29). G2(2)=2.05, p=.36. No gain from the principle |
| 3 (N=66) | one analog + diagram; one analog; diagram alone | 23/81 (N=26), 40/76 (N=25), 7/67 (N=15). No gain from the diagram |
| 4 (N=98) | two analogs (similar or dissimilar) vs one analog + control | two: 45% vs one: 21% pre-hint (G2=6.35, p<.01); total 80% vs 53% (G2=8.36, p<.003). Similar 39/79 (N=28), dissimilar 52/83 (N=23), one+control 21/53 (N=47) |
| 5 (N=143) | two analogs with vs without a stated principle | 62% vs 40% pre-hint (G2=6.75, p<.01); total 82% vs 67% (p<.05). Good schemas 44% vs 10% |
| 6 (N=189) | two analogs with vs without diagrams; similar vs dissimilar | diagram 57% vs 37% pre-hint (p<.01); total 92% vs 79%. Similar vs dissimilar: no effect |

**The schema-quality result.** Exp 4 had each subject write a description of the similarity. Good schemas: 91% solved pre-hint (10/11). Intermediate: 40%. Poor: 30%. The mix was 21% good, 20% intermediate, 59% poor. G2(4)=15.8, p<.005 [a06]. Critique re-opened these numbers and confirmed them; the 10/11 cell was not rechecked. Exp 5 added: good schemas reached the solution 94% vs 53% for poor, in the with-principle group (G2(4)=13.0, p<.02). Without a principle the link was not significant (p=.14).

**Reading.** Two cases and a forced similarity description about double unaided transfer. A principle or a diagram helps only when attached to a pair, not to one case. Most people still write poor schemas.

### 2.2 Catrambone and Holyoak 1989: the limits of context

A replication and extension [a09-a12, b07-b09].

- Exp 1 replicated. Comparing two analogs: 47% pre-hint (n=19) vs 16% without comparison. Total 71% vs 41% for one analog.
- Exp 2: after a 30-minute filled delay, or a context shift, no condition beat the 10% base rate pre-hint. Total with hint: 65% (30-min) vs 42% (1-week). One-week pre-hint was 0% (n=15). Quote: "Little or no analogical transfer is obtained after a delay of even 30 min."
- Rescue (Exp 4 and 5): three changes together raised transfer. They were directive comparison questions, a third example, and target wording that matched the schema. Exp 4 (N=90): directive 36% vs 10% pre-hint; appropriate schemas 86% vs 26% (G2=28.91). Exp 5 (one week, n=23): 74% unaided, vs 7% and 23% in the earlier one-week conditions.
- Schema quality predicted transfer weakly here: Exp 1 appropriate 58% vs poor 29% pre-hint (p=.20), totals 67% vs 71% (no difference).

The three changes were confounded. This paper was not re-opened in the cross-check; numbers rest on the first read.

### 2.3 The Gentner-Loewenstein-Thompson line: analogical encoding

Gentner's structure-mapping theory says analogy is a mapping between relational structures. Comparison makes shared relations salient and incidental surface features fade. "Analogical encoding" is learning by comparing two cases side by side at study time.

- **Thompson, Gentner, Loewenstein 2000** [a13-a15, b10-b11]. Masters of management students. Comparison group 14/22 dyads (64%) used contingent contracts in a live negotiation vs advice group 5/22 (23%), chi2(1,N=44)=7.50, p<.01. Not one person in the Advice group drew a parallel between the cases. If both dyad members stated a sophisticated principle: 88% used contracts; one member: 45%. Quality of case-by-case advice did not predict behaviour (25% vs 18%). Earlier work cited there (not opened): compare 54% vs advice 13%; naming the principle added nothing.
- **Gentner, Loewenstein, Thompson 2003** [a16-a18]. Exp 1: guided analogy 47% (15/32) vs baseline 6%, chi2=7.92. Exp 2 (N=128): comparison 48% vs separate 19%, chi2=11.85; linked the cases 98% vs 16%. Exp 3 (N=158, live negotiation): guided 90%, compare 70%, separate 55%, baseline 37%. "Ideal contract" answers in Exp 3: 73% and 68% (guided, compare) vs 48% and 47% (separate, baseline); full schema articulation 35% vs 8%.
- **Loewenstein, Thompson, Gentner 2003** [a19-a20, b12-b13]. Teams. Comparison 24/60 (40%) vs separate 8/37 (22%) vs baseline 50/213 (23%); chi2(2,N=310)=7.08, p<.05; comparison vs separate alone p=.06. Teams 32% vs solo 34%. Schema induced 55% vs 32%. Participants linked the cases: 100% (comparison) vs 18% (separate).
- **Kurtz, Miao, Gentner 2001** [b16]. Heat-flow scenarios, N=80. Joint interpretation with listed correspondences gave most insight. 48% of that group used all three key schema terms.
- **Gentner, Loewenstein, Thompson, Forbus 2009** [b14-b15]. Comparison at recall time can retrieve an earlier case: 27% vs 6% (Exp 4, N=73). Surface-similar retrieval 30% vs 78%. A simulation (SME-style) was reported to capture both retrieval and transfer.
- **Kurtz and Loewenstein 2007** [d12]. Re-opened. Comparing two unsolved problems at test time, under an instruction to find one shared solution: 51% (Exp 1, N=293) and 40% (Exp 2, N=224) found the convergence solution. One story plus one problem: 13%. Two solved stories compared: 38% and 35%. Two problems solved separately: 16%, near baseline. See K26.

### 2.4 Meta-analysis (Alfieri, Nokes-Malach, Schunn)

Journal paper 2013 [a21-a22]: d=.50, 95% CI [.44,.56], 336 tests from 57 experiments. The 2011 conference report gave d=.60 (CI [.47,.72], I2=59%) [a23, b18]. Use .50. Four of fifteen moderators were reliable in the journal paper: comparison objective (finding similarities best), principle presentation (principles after comparison beat principles before), content (perceptual content larger), lag (immediate tests larger). Age, setting, experience and comparison task type did not moderate. Only the abstract was read. Full text is paywalled; no per-moderator effect sizes exist in our notes.

### 2.5 Formal models

- **SME** (structure-mapping engine) finds the best relational alignment between two cases.
- **SAGE** (sequential analogical generalisation engine) builds on SME. Each new case is matched against stored items. If similarity is above an assimilation threshold, it merges into a generalisation. Otherwise it is stored as its own case.
- **ALIGN** (McLure, Friedman, Forbus 2015) adds near-miss cases: similar cases with a different label. The differences between a case and its near-miss show what the schema must exclude [a24-a25, c24].

### 2.6 What the theories disagree on

| Question | One side | Other side |
|---|---|---|
| Is the explicit principle useful? | Helps with a pair (GH83 Exp 5); Alfieri: after comparison is better | Adds nothing with one analog (GH83 Exp 2); Gentner group: naming it added nothing |
| Does separate study help? | 55% vs 37% baseline (Gentner 2003 Exp 3) | 22% vs 23% baseline (Loewenstein 2003) |
| Should the pair be varied? | theory: dissimilar pairs force abstraction | data: 39% vs 52%, not significant |
| Is the induced schema the mediator? | Gick and Holyoak: quality predicts transfer; Thompson: principle quality predicts | Catrambone: weak link in small samples; correlational everywhere |

---

## 3. Core findings with exact numbers

Status uses claim ids from claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Two analogs beat one for unaided transfer | 45% vs 21% pre-hint; 80% vs 53% total; N=98 | Gick and Holyoak 1983 Exp 4 [a05, b01] | [E] K01 |
| Replication: comparison instruction raises transfer | 47% vs 16% pre-hint, n=19 each; total 71% vs 41% | Catrambone and Holyoak 1989 Exp 1 [a09] | [E] K01 |
| Compare vs separate study | 48% vs 19%, N=128, chi2=11.85 | Gentner et al. 2003 Exp 2 [a17] | [E] K01 |
| Meta-analytic effect of case comparison | d=.50, CI [.44,.56], 57 experiments, 336 tests | Alfieri et al. 2013 [a21] | [S] K09 (abstract only) |
| Most learners still fail unaided | 40 to 48% in comparison conditions; 70 to 90% only with heavy scaffolding | GH83, Gentner 2003, Catrambone | [E] K02 |
| Studying cases separately | 22% vs 23% baseline (teams) but 55% vs 37% (pairs) | Loewenstein 2003; Gentner 2003 Exp 3 | [C] K03 |
| More guidance, more transfer | guided 90%, compare 70%, separate 55%, baseline 37%; directive questions lift good schemas 26% to 86% | Gentner 2003 Exp 3; Catrambone Exp 4 [a18, b09] | [E] K08 |
| Principle with one analog | 32% vs 29% pre-hint | GH83 Exp 2 [a03] | [S] K04 |
| Principle with two analogs | 62% vs 40% pre-hint; 82% vs 67% total; N=143 | GH83 Exp 5 [a07] | [S] K04 |
| Schema quality predicts transfer | good 91% vs poor 30% pre-hint; negotiation 88% vs 45% | GH83; Thompson 2000 [a06, a14] | [E] K05 (correlational) |
| Similar vs dissimilar pair | 39% vs 52% pre-hint, not significant | GH83 Exp 4 [a05] | [S] K06 |
| Delay or context change kills unaided transfer | no condition above 10% base rate after 30 min | Catrambone and Holyoak 1989 Exp 2 [a10] | [S] K07 |
| Rescue of delayed transfer | 74% unaided at 1 week vs 7% and 23% earlier (three confounded changes) | Catrambone and Holyoak 1989 Exp 5 [a11] | [S] K07 |
| Comparing two unsolved problems | 51% and 40% vs 13% (story + problem); 38%/35% (two solved stories) | Kurtz and Loewenstein 2007 [d12] | [S] K26 |
| Joint comparison needed to link cases | 88 to 100% of comparers vs 16 to 18% of separate learners linked them | Gentner 2003; Loewenstein 2003; Gentner 2009 [a17, b13, b14] | [E] K22 |
| Teams no better than solo | 32% vs 34% | Loewenstein 2003 [a19] | [S] (part of K22) |
| Boundary: comparison helps only some learners | informal/formal comparison helped conceptual items only for learners who disliked maths: 2.83 vs 1.49, N=111 | Hattikudur et al. 2016 [b17] | [S] (part of K22) |
| Step-back, weak model | PaLM-2L: Physics 66.4 to 73.2, Chemistry 70.9 to 81.8, TimeQA 41.5 to 66.0 | Zheng et al. 2023 [a26, c01, c02] | [S] K10 |
| Step-back, strong model | GPT-4 over CoT: Physics 84.5 vs 82.9, Chemistry 85.6 vs 85.3 (within SD); StrategyQA 82.8 to 82.7 | same | [S] K10 |
| Step-back fixes and breaks | physics: fixes 20.5%, new errors 11.9%; TimeQA fixes 39.9%, new 5.6% | same [b24, c03] | [S] K12 |
| Abstraction is rarely the failing step | over 90% of step-back errors in the Reasoning step; Self-Discover 87.5% structures correct, 74.7% of failures computation | Zheng; Zhou 2024 [a28, c03, c10] | [E] K11 |
| Buffer of Thoughts (GPT-4) | Game of 24 82.4 (ToT 74.0, CoT 11.0); Checkmate-in-One 86.4 (meta-prompting 57.2); Geometric Shapes 93.6 (78.2); MGSM 89.2 (CoT 85.5); cost about 12% of multi-query methods | Yang et al. 2024 [a29, b25, c04] | [E] K13 (family) |
| Agent memory of reusable routines | AWM +12.0 WebArena; ReasoningBank +4.6 to +8.3 over no memory | Wang 2024; Ouyang 2026 [c21, c23] | [E] K13 |
| Memory ladder | WebArena flash: none 40.5, raw 42.1, workflows 44.1, distilled 48.8; Dynamic Cheatsheet Game of 24: baseline 10, raw retrieval 6, curated 93 to 99 | ReasoningBank; DC [d07, d08] | [E] K31 |
| Self-generated analogs | GSM8K 75.0 to 77.8, MATH 33.0 to 37.3 (GPT-3.5); K=1 worst (76.1/34.8), K=3 to 5 stable | Yasunaga et al. 2024 [c06, c07, d17] | [S] K15, [E] K28 for the count |
| Abstraction-of-Thought | 3-shot BBH prompting +15.1 (Llama-3-8B 60.0 to 75.1); about 80% more tokens; finetune headline needs training | Hong et al. 2024 [c08, c09] | [S] K16 |
| Self-Discover | BBH +7 / +6 over CoT (PaLM 2-L / GPT-4); MATH +8.5 / +2; T4D 85 vs 52 (GPT-4); 10 to 40x fewer calls than self-consistency | Zhou et al. 2024 [c10, d05] | [S] K23 |
| Hypothesis search on ARC | GPT-4: direct 17, programs only 23, LLM hypotheses 30, human-selected 33, human-written 45 | Wang et al. 2024 [c17, d10] | [S] K19 |
| False passes in list functions | 45.4% of programs that passed shown examples failed ground truth; summarising lost 26% of correct hypotheses | Parab et al. 2025 [c19, c20] | [C] K20 |
| Analogy brittle off-distribution | GPT-4 digit matrices 0.813 original, 0.790 symbols, 0.480 blank moved; humans flat | Lewis and Mitchell 2024 [c14, d13] | [C] K17 |
| Source choice by GPT-4 | correct source named unprompted 0 of 15; with hint claims both (precision 0.50 to 0.52, recall 1.00) | Puranam et al. 2025 [c16, d11] | [S] K18 |
| Reasoning models gain little from extra prompting | step-by-step: o3-mini +2.9, o4-mini +3.1, Gemini Flash 2.5 -3.3 points; time +20 to 80% | Meincke et al. 2025 [d01] | [S] K24 |
| Terse reasoning control | GSM8K GPT-4o: standard 53.3, CoT 95.4, Chain of Draft 91.1 at about 40 vs 200 tokens | Xu et al. 2025 [d03] | [S] K25 |
| Contrast with own errors | LEAP GPT-4 +7.5 DROP, +3.3 HotpotQA, under 1 on GSM8K/MATH; contrastive CoT GSM8K 69.2 to 79.0 (GPT-3.5) | Zhang 2024; Chia 2023 [d15, d16] | [C] K27 |
| Near-miss cases | ALIGN 62% vs prototypes 55% vs examples 55% (sketches, p<.01); geospatial peak 77% vs 62% vs 53% | McLure et al. 2015 [c24] | [S] K21 |

---

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

### 4.1 Analogical encoding (human recipe)

1. Present two solved cases of the same structural class, with different surface content.
2. Instruct a directive comparison: "list the correspondences, then what they share, then what is irrelevant".
3. Have the learner write the schema in its own words.
4. Optionally add the principle label after the comparison (Alfieri; GH83 Exp 5).
5. Test on a new instance with a new surface form.

Why it works (structure mapping): alignment makes shared relations salient and drops surface features. The learner writes a representation that is not tied to either case. Separate study gives no alignment, so only 16 to 18% of separate learners even link the cases [b13].

Active ingredients ranked by evidence: (a) joint comparison, (b) a directive form that lists correspondences, (c) a second case, (d) a third case plus matched wording for delayed use, (e) a principle label after the comparison, (f) a diagram.

### 4.2 SME-style mapping (implementable)

```
map(base, target):
  score every candidate pairing of entities and relations
  keep pairings that are structurally consistent (one-to-one, parallel connectivity)
  prefer systems of mutually connected relations over isolated matches
  return the best global mapping and a score
```

For an LLM agent, the model proposes the correspondences as a list. Code checks one-to-one use and that every mapped relation has mapped arguments. This is a slot the model fills; the program checks structure (SCHEMA.md section 1).

### 4.3 SAGE generalisation (implementable)

```
library = []
for case in stream:
    best = argmax over library items of sim(case, item)   # SME score
    if sim(case, best) >= theta (0.8 in ALIGN):
        best = merge(best, case)    # keep shared facts; mark differing facts with probabilities
    else:
        library.append(case)
```

Settings from McLure et al.: threshold 0.8. Too low: incidental differences get merged. Too high: generalisations stay small and numerous [a25]. Generalisation alone did not beat raw examples (55% vs 55%).

### 4.4 ALIGN near-miss contrast (implementable)

For a new case, also retrieve the most similar stored case with a different label. Compare them. The differing facts become discriminating features that the schema must keep. Gain: +7 points (62%) in sketches; geospatial 77% peak vs 62% prototypes. Domains were tiny symbolic sets, not language reasoning.

### 4.5 Step-back (prompting)

```
q_back = LLM("What is the underlying principle or concept behind: {question}?")   # 1 call
principle = LLM(q_back)
answer = LLM("Using {principle}, answer: {question}")
```

Zheng et al. used few-shot exemplars of step-back questions; one exemplar was enough and more gave no gain [b23]. TimeQA gain comes largely from a better retrieval query [a27].

### 4.6 Buffer of Thoughts

```
key_info = distill(problem)                  # restate constraints, variables
template = retrieve(meta_buffer, key_info)    # by embedding similarity
if none close: build new template
solution = instantiate(template, key_info)
meta_buffer = manager.update(meta_buffer, solution)  # add new template if novel
```

Ablations: removing the distiller hurts hard tasks most (Game of 24, Checkmate-in-One). Without the manager, accuracy does not rise across rounds [b26, c05]. Templates carry a worked procedure, not only a principle; that is why gains are large where step-back's are small.

### 4.7 Abstraction-of-Thought

Format the reasoning in two layers: an abstract plan first, then concrete steps (often with code). Prompting alone: +15.1 on BBH 3-shot for Llama-3-8B. Cost: about 80% more tokens. The finetuning table (348k samples) is out of scope for a scaffold.

### 4.8 Analogical prompting

The model writes K related but different example problems with solutions (and, for code, key knowledge), then solves the target. K=1 is worst because the model over-relies on one case. K=3 to 5 is stable [c07, d17]. Helps large models, fails on small ones.

### 4.9 Self-Discover

Once per task class, compose a reasoning structure from atomic modules from a few unlabeled examples (select, adapt, implement). Then one call per instance. 10 to 40x fewer calls than CoT with self-consistency. Structures discovered by a strong model help weaker models (Llama2 52% vs CoT 42% on disambiguation QA) [c11].

### 4.10 Hypothesis search

Ask for several natural-language rule hypotheses. Implement each as a program. Run on the shown examples. Summarising the hypotheses first loses some correct ones (12.1 points absolute in list functions; 30 vs 33 tasks in ARC). In ARC, a program that passed the shown examples almost always passed the test. In list functions, 45.4% of such programs failed ground truth.

### 4.11 Memory of routines (AWM, ReasoningBank, Dynamic Cheatsheet, PlugMem)

Store abstracted routines with example-specific values replaced by placeholders. Retrieve by similarity. AWM rule-built workflows (de-duplicated action sequences) matched model-written on WebArena (35.6 vs 35.5) and trailed on Mind2Web (task success 2.0 vs 4.8). Distilled strategies from both successes and failures beat raw trajectories.

---

## 5. What holds up

### 5.1 Replicated and robust

- **Two analogs beat one** (GH83 Exp 4, Catrambone Exp 1, Gentner Exp 2; meta-analysis d=.50) [E K01]. Independent labs partly: Gick/Holyoak and Catrambone are UCLA; Gentner group is Northwestern; Alfieri is separate.
- **Forced, directive comparison beats loose or separate processing** [E K08, K22]. 98% vs 16% linking the cases is the cleanest mechanism check.
- **Transfer is partial even with comparison** (40 to 48%) [E K02]. Do not assume a derived schema gets used.
- **Abstraction is rarely the failing step; application is** [E K11].
- **Memory of validated, abstracted routines beats raw reuse** [E K31, K13], with caveats below.
- **Self-generated analogs: K=1 is worst, K=3 to 5 is stable** [E K28], effects of 1 to 3 points.

### 5.2 Failures, contested results and boundaries

- **Separate study:** 22% vs 23% (no gain) in one study; 55% vs 37% in another [C K03]. Different tasks and baselines.
- **Delay and context change:** unaided transfer vanishes [S K07]. Rescue involves three confounded changes.
- **Hattikudur 2016:** comparison helped only learners who disliked maths [b17].
- **Teams do not beat solo** (32% vs 34%) [a19].
- **A stated principle with one analog:** zero effect (32% vs 29%) [S K04].
- **Similar vs dissimilar pair:** no reliable difference [S K06]. The idea that varied examples help is a trend only.
- **Schema quality as mediator:** correlational; Catrambone totals show no link (67% vs 71%) [E K05 with caveat].
- **Step-back on strong models:** GPT-4 gain over CoT is +1.6 and +0.3, within SD; none on StrategyQA or GSM8K [S K10].
- **Step-back regressions:** fixes 20.5% but breaks 11.9% [S K12].
- **LLM analogy robustness:** Webb 2023 found GPT-3 above human mean (digit matrices OR 1.88, p=.005, N=40). Hodel and West, Lewis and Mitchell, Stevenson found collapse on altered alphabets or moved blanks. Contested [C K17]; Webb's authors dispute the contamination reading. No test on current reasoning models.
- **Hypothesis search false passes:** 45.4% in list functions vs near zero in ARC [C K20]. Domain and example count decide how much "passes the shown examples" means.
- **Wrong-vs-right contrast:** LEAP gives +7.5 on DROP but under 1 on math, and Llama-2-70B did not follow the lessons. Contrastive CoT +9.8 GSM8K on GPT-3.5 with doubled demonstration length [C K27].
- **Reasoning-trained models:** extra step-by-step prompting +3 points or less; few-shot examples are reported to degrade DeepSeek-R1 (no numbers) [S K24].

### 5.3 Interventions that worked

Joint comparison; directive questions with listed correspondences; a third case with matched target wording (for delay); principle label after a pair; diagrams with a pair; near-miss contrast cases (small symbolic data); a once-per-class reasoning structure; stored validated routines with a manager that updates the store.

### 5.4 Interventions that did not

A principle or diagram added to a single case; separate per-case advice; mentioning the principle during training (cited); team discussion; unaided analogy after a delay; summarising rule candidates before testing (loses 9 to 26% of correct ones); few-shot demonstrations for reasoning-trained models (reported).

### 5.5 Weak spots in the evidence base (from critique.md)

- Human cells are small (15 to 50), samples are undergraduates, and the radiation problem carries most of the induction literature.
- The Gentner, Loewenstein, Thompson, Kurtz, Forbus papers are one research network.
- Alfieri read from the abstract only. Replication evidence is thin: Boyce et al. 2023 student replication is marked successful in the FORRT atlas with no N or effect size; a "2017 replication of Kurtz and Loewenstein" could not be found and must not be cited.
- Catrambone 1989 and Thompson 2000 numbers rest on the first read, not on the cross-check.
- BoT, Self-Discover, AWM, ReasoningBank, PlugMem use the authors' own benchmarks. Leakage between template and test items is not excluded.
- Literature search was thin for 2025 to 2026 because search tools hit quotas (critique, gap search note). Absence of a paper means "not found", not "does not exist".

---

## 6. Language models

### 6.1 Do they do analogy and induction?

- On familiar forms, strongly. GPT-3 matched or beat college students on text matrices, letter strings and story analogies [c12].
- Off the familiar form, no. GPT-4 digit matrices: 0.813 original, 0.790 with symbols, 0.480 with the blank moved. Humans stayed about flat (0.715, 0.771, 0.704) [c14, d13]. Letter strings with synthetic alphabets: GPT-3 falls on 5 of 6 problem types (N=50 per type; humans N=121 stay level) [c13]. Latin/Greek/symbol alphabets: GPT-4o 0.85/0.63/0.48; Claude-3.5 0.68/0.62/0.46; adults 0.88/0.91/0.89 [c15]. Story analogies: GPT-4 89% (16/18) when the right answer was first vs 61% when second [d13]. o1-preview lost 17.5 points from one irrelevant clause in GSM-NoOp [d14].
- Source choice. Puranam et al. (humans N=199, 46 per target; GPT-4 15 trials per cell). GPT-4 never named the correct source unprompted (0/15). With a hint it claimed both sources nearly every time (precision 0.50 to 0.52, recall 1.00) [d11]. Human factory problem 6.3% to 8.7% with hint; HR problem 20.3% to 37%.
- Critique: no test on current reasoning models for altered alphabets, and no test of a rewording rescue.

### 6.2 Prompting methods and measured gains

| Method | Model | Gain | Token cost | Notes |
|---|---|---|---|---|
| Step-back | PaLM-2L | Physics +6.8 over base (66.4 to 73.2), Chem +10.9, TimeQA +24.5 | one extra call | gain vs CoT also positive on PaLM-2L |
| Step-back | GPT-4 | +1.6 / +0.3 over CoT | one extra call | within SD (0.5 to 1.4) |
| Step-back | Llama2-70B | Physics 51.9 to 64.8 | one extra call | CoT 59.3 / 64.1 |
| Analogical prompting | GPT-3.5 | GSM8K +2.8, MATH +4.3; about +4 average | self-written cases | K=1 worst |
| Contrastive CoT | GPT-3.5-Turbo | GSM8K +9.8, AQuA +4.0 | demonstration length doubled | with self-consistency +12.6 to +17.6 |
| LEAP | GPT-4 | DROP +7.5, HotpotQA +3.3, math under 1 | extra lesson-writing step | Llama-2-70B no gain |
| Abstraction-of-Thought | Llama-3-8B | BBH 3-shot +15.1 | about 80% more tokens | mixes in code |
| Self-Discover | GPT-4 | BBH +6, T4D +33, MATH +2 over CoT | 3 extra calls per class, then 1 per instance | PaLM 2-L: BBH +7, T4D +29, MATH +8.5 |
| Buffer of Thoughts | GPT-4 | Game of 24 82.4 vs 74.0 ToT; Checkmate 86.4 vs 57.2 | about 12% of multi-query cost | BoT+Llama3-70B: Game of 24 78.4 vs 2.4 alone |
| Hypothesis search | GPT-4 | ARC 23 to 30 | many programs | list functions 71.3 vs 73.1 plain two-shot |
| Chain of Draft (control) | GPT-4o | GSM8K 91.1 vs CoT 95.4 | about 40 vs about 200 tokens | the right fair control |

### 6.3 What changed behaviour, and by how much

- **Model strength.** The same method gives large gains on a weak or mid model and near-zero on a strong one (step-back PaLM-2L vs GPT-4; Self-Discover MATH +8.5 vs +2; analogical prompting fails on small models; StyleBench: structure helps only large models on hard search tasks).
- **Template content.** Buffer of Thoughts gives huge gains because it supplies a worked procedure. Step-back supplies only a principle. Dynamic Cheatsheet shows the same: a stored runnable routine took Game of 24 from 10 to 93-99 for GPT-4o, while Claude 3.5 Sonnet never adopted the routine (12 to 14).
- **Task type.** Largest where the task needs recall of principles or knowledge (TimeQA, physics, T4D). Self-Discover's gains are largest on world-knowledge tasks and moderate on algorithmic ones (corrected in critique). Zero on StrategyQA and GSM8K for step-back.
- **Number of cases.** Self-generated: K=1 worst, K=3 to 5 stable; K=1 to K=3 adds 1.4 (GSM8K) and 2.5 (MATH). Retrieved agent memory: 1 experience best, 4 worse (44.4).
- **Reasoning-trained models.** Step-by-step prompting adds +2.9 / +3.1 (o3-mini, o4-mini) and -3.3 (Gemini Flash 2.5) on GPQA Diamond for 20 to 80% more time [d01]. DeepSeek reports few-shot examples degrade R1 [d02].
- **Memory form.** WebArena (Gemini-2.5-flash): none 40.5, raw 42.1, workflows 44.1, distilled 48.8, plus test-time scaling 51.8. AWM hurt on the multi-site subset (3.4 vs 10.3 no memory). PlugMem: structuring raw episodes beats chunking (LongMemEval 75.1 vs 62.8).
- **Error regression.** Step-back breaks 11.9% of previously right physics answers.

### 6.4 What no one has measured

- The human recipe on a model (two cases, forced alignment, derived rule, new instance) at equal tokens.
- Any abstraction method against a terse-reasoning control on a current model.
- Whether a model's written rule quality predicts its held-out success.
- Pair choice (similar, dissimilar, near-miss) for models.
- A rewording step as rescue for retrieval of a stored rule.
- Three-arm memory ablation (raw cases vs code-built routines vs model-written templates) on a held-out class.

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | In S2, when two or more solved cases of the same class are available, require a joint comparison step that outputs a correspondence list and the shared structure. Never summarise cases one by one. | S2 | [E] | K01, K08, K22; a05, a09, a17, b13 |
| A2 | Use two cases, not one, for any induction. For model-generated or retrieved cases, use 3 and cap at 3 to 5 (1 is worst for self-generated; more than 1 to 2 hurt in retrieved memory). | S2 / S3 | [E] | K01, K28; d17, d07 |
| A3 | Check an induced rule by running it on held-out instances (G3). Do not trust its wording. Do not spend tokens validating the abstract step; spend them on checked execution of what follows it. | G3 / S4 | [E] on the first half of A3 (K11); the 'running beats judging wording' part is [C] (K29) | K11, K29; a28, c03, c10, c19, d10 |
| A4 | Store reusable abstractions as validated, runnable routines with placeholders, kept by a code-run manager that adds only when the routine passes a check. Offer them by similarity and after the first attempt. | memory | [E] | K13, K31; c05, c21, c23, d07, d08 |
| A5 | Do not expect a schema to fire by itself. Retrieval must be explicit, and each retrieved case must be checked against the target (G3). | S3 / memory | [E] on the retrieval gap (K02, K07 partly); the check step itself is [S] | K02, K18, K30; a10, d11 |
| A6 | Report transfer per condition in logs; never assume a derived schema was used. | G7 / logging | [E] | K02 |
| A7 | Test every induced rule on a transformed variant (renamed symbols, reordered clauses) before storing it. | G3 / S8 | [E] that surface changes hurt models (K30); the use as a pre-storage test is [S] | K30; d13, d14 |

These match existing SCHEMA.md elements: S2 "study every example", O7 "map an analogue", the memory section, and G3. Nothing in "Add now" needs a new state.

### Test first (single-source, contested, or untested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Pair-comparison induction step (two cases, forced alignment, derived rule) vs plain, at equal tokens. The decisive gap. | S2 | [S] human only | K01, K22, K27; no LLM test |
| T2 | Gate induction on the plain pass rate and principle-recall need. | S0 | [S] design inference | K33, K24, K10, K23 |
| T3 | Step-back before solving, only where plain fails or disagrees. | S1 / O2 | [S] older models only | K10, K12 |
| T4 | Keep the plain answer as a candidate next to the abstracted answer; select by check. | G1 / S7 | [S] | K12 |
| T5 | Sibling problem operator: write a problem with the same structure, solve both under one shared-strategy instruction. | new O | [S] human | K26 |
| T6 | Principle line added after (not before) a two-case comparison. | S2 | [S] | K04, K09 |
| T7 | Per-class reasoning structure built once and reused (Self-Discover style), setup tokens counted. | S0 | [S] older models | K23 |
| T8 | Near-miss contrast case stored with each case. | memory / S2 | [S] tiny symbolic data | K21 |
| T9 | Dissimilar vs similar pair choice. | S2 | [S] trend only | K06 |
| T10 | Rewording step on retrieval of a stored rule. | memory | [S] human | K07, K18 |
| T11 | Code-built vs model-written routines. | memory | [C] | K14, K31 |
| T12 | Hypothesis list kept raw (no summarising) before testing. | S2 / S4 | [C] | K20 |
| T13 | Abstract-plan-then-concrete format (AoT prompting form) vs plain at equal tokens. | S3 | [S] | K16 |
| T14 | Wrong-vs-right contrast lessons (LEAP) after a failed attempt. | S5 / S9 | [C] | K27 |

---

## 8. Concrete tests on our bench

Common rules. Every arm gets the same token budget, setup tokens included (G7). Always include a terse-reasoning arm (about 40 tokens per step, Chain of Draft style) and a zero-shot arm, since few-shot may hurt reasoning-trained models. Test items use new surface forms. Report accuracy, tokens, and flips right-to-wrong and wrong-to-right per arm.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Induction by comparison | ARC-style or rule-discovery items in classes of at least 6 items; 2 solved cases of the class shown, then a new instance with changed surface form | (a) plain zero-shot; (b) 1 solved case; (c) 2 solved cases, no instruction; (d) 2 cases + forced correspondence list and rule; (e) 2 cases solved separately with per-case summary; (f) self-generated K=3 cases | pass rate on held-out new-surface instance; rule correct on held-out inputs | humans: (d) about 2x (c) or (b); models: expected +0 to 3 points, possibly negative on reasoning models. Add (d) only if it beats (a) and (f) |
| T2 Gate | mixed items: easy, hard recall, hard reasoning | always-on induction vs gated (only when plain fails or disagrees) vs never | accuracy per token | gated equal accuracy at fewer tokens |
| T3 Step-back | knowledge-heavy and physics-style items | plain short reasoning vs step-back vs step-back + plain as a second candidate with code or check select | pass rate; regressions | gains only where plain pass rate is low; expect 0 on high-pass classes |
| T5 Sibling problem | BRAINTEASER-style items with a structural twin | solve target alone vs write sibling and solve both under one strategy vs two-sample vote | pass rate | modest, human Kurtz effect 51% vs 13% will shrink |
| T6 Principle after | two-case comparison items | principle line before vs after vs none | pass rate on new instance | small; positive only if after beats none |
| T7 Per-class structure | one class of at least 20 items | structure built once vs per-item reasoning; count setup cost | accuracy per total token | positive only after about 10 items per class |
| T8 Near-miss | classification-like rule items | stored cases only vs merged summary vs cases + near-miss | held-out accuracy | +0 to 7 points |
| T9 Pair choice | same item class | similar pair vs dissimilar pair vs near-miss pair | new-surface accuracy | likely tied |
| T10 Rewording | stored rule applied to differently worded instance | direct retrieval vs retrieval after restate-in-own-words | retrieval hit rate | positive if wording drives misses |
| T11 Memory form | task stream from one class + a held-out class | raw solved cases vs code-built routines vs model-written templates | accuracy on held-out class; leakage check | routines at least raw; leakage visible on held-out |
| T12 Raw vs summarised hypotheses | ARC items | test every raw hypothesis vs summarise first | solved count | raw at least summarised |
| T13 AoT form | multi-step items | abstract plan then concrete vs plain; match tokens by trimming | pass rate | small |
| Rule-quality check | any induction arm | judge-rated rule quality vs held-out run success | correlation added beyond run result | if none, drop judging rule wording |

---

## 9. What does not transfer, and why

- **Delay and memory failure.** Human unaided transfer fails after 30 minutes because the cue is not used. A model has no delay and no forgetting inside a context. The equivalent is retrieval from an external store. Inside one context the delay literature does not apply.
- **Learner motivation and effort.** Hattikudur's finding depends on disliking maths. A model has no such trait.
- **Team effects.** Teams did no better than solo, and debate is already out (G9).
- **Naming the principle.** For humans this changes how the schema is stored. For a model, a stated principle is just context and may anchor (fixation). Treat it as a test (T6).
- **Single-case anchoring in humans vs models.** K=1 hurts models because they copy it (analogical prompting). In humans one case leaves the schema implicit. Both say "use more than one" but for different reasons.
- **Teaching with a live negotiation outcome.** Contingent-contract transfer is a behaviour task with a 23 to 37% baseline. Our items are scored answers with a check.
- **Finetuned abstraction formats.** AoT's headline (finetune on 348k samples) does not apply to a no-training scaffold.
- **Benchmark-specific templates.** BoT's Game of 24 and Checkmate gains depend on a template that carries the whole procedure. On open problems no such template exists, and the leakage between template and test items is unexcluded.
- **Human insight instruction ("find similarities").** Written for people who need to attend. A model attends to what is in context; the equivalent is a structured output form, which is test T1(d).
- **Long-run human learning ladders.** Gains require explicit effort and scaffolds that models may not follow (Llama-2-70B did not follow LEAP lessons).
- **Self-judged schema quality.** In people, rated schema quality predicts transfer. In models, judging wording is the pattern G5 and G10 warn against.

---

## 10. Open questions

1. Does the human recipe help a model at equal tokens against one case, plain reasoning and self-generated cases? (No paper tests it.)
2. Do step-back, abstract-plan-first and Self-Discover beat a terse plain answer on a current strong or reasoning-trained model?
3. Does the choice of pair (similar, dissimilar, near-miss) matter for models?
4. Does a model's written rule score predict its held-out success? ARC and list functions disagree on how reliable "passes the shown examples" is.
5. Is a stored abstraction safe across surface forms on current reasoning models? Is a rewording step an effective rescue?
6. How much of the memory gain is abstraction, and how much is reuse of validated routines? Clean three-arm ablation missing.
7. Alfieri per-moderator effect sizes (principle after vs before, similarities vs differences, lag).
8. Details of the Boyce et al. 2023 replication (N, effect size). The Kurtz and Loewenstein replication claim needs to be located or dropped.
9. When should the agent skip induction? Rule untested.
10. Can a forced causal-structure check fix GPT-4-style source choice (0 of 15 unprompted, precision 0.50 with hint)?
11. Is the human gain from "comparison at test time on two unsolved problems" (Kurtz and Loewenstein) available to a model by writing a sibling problem?
12. Do reasoning-trained models gain or lose from supplied cases (DeepSeek says lose; no numbers)?

---

## 11. Sources

[V] = opened and read this session (PDF or HTML text). [M] = snippet or secondhand only.

**Human studies**
- [V] Gick and Holyoak (1983) Schema induction and analogical transfer. https://www.gwern.net/doc/psychology/1983-gick.pdf
- [V] Catrambone and Holyoak (1989) Overcoming contextual limitations on problem-solving transfer. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Catrambone_Holyoak1989.pdf (not re-opened in the cross-check)
- [V] Thompson, Gentner and Loewenstein (2000) Avoiding missed opportunities in managerial life. https://mail.loewenstein.web.illinois.edu/papers/Thompsonetal%20OBHDP00.pdf and https://doi.org/10.1006/obhd.2000.2887 (PDF not fetched in the cross-check pass)
- [M] Loewenstein, Thompson and Gentner (1999) Analogical encoding facilitates knowledge transfer in negotiation. Cited secondhand in Thompson 2000 (compare 54% vs advice 13%; naming the principle no effect).
- [V] Gentner, Loewenstein and Thompson (2003) Learning and transfer: a general role for analogical encoding. https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf
- [V] Loewenstein, Thompson and Gentner (2003) Analogical learning in negotiation teams. https://business.illinois.edu/loewenstein/papers/Loewensteinetal%20AMLE03.pdf
- [V] Gentner, Loewenstein, Thompson and Forbus (2009) Reviving inert knowledge. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2009/Gentner,Loewenstein,Thompson&Forbus_2009-1.pdf
- [V] Kurtz, Miao and Gentner (2001) Learning by analogical bootstrapping. https://groups.psych.northwestern.edu/gentner/papers/KurtzMiaoGentner01.pdf
- [V] Kurtz and Loewenstein (2007) Converging on a new role for analogy in problem solving and retrieval. https://escholarship.org/uc/item/2f49g0br
- [V] Hattikudur, Sidney and Alibali (2016) Does comparing informal and formal procedures promote mathematics learning? https://alibali.psych.wisc.edu/wp-content/uploads/sites/371/2018/02/HattikudurSidneyAlibali2016.pdf
- [V] Alfieri, Nokes-Malach and Schunn (2013) Learning through case comparisons: a meta-analytic review (abstract via OpenAlex only). https://doi.org/10.1080/00461520.2013.775712
- [V] Alfieri, Nokes and Schunn (2011) Aligning structural components across learning tasks of case comparisons (conference abstract). https://files.eric.ed.gov/fulltext/ED528947.pdf
- [V] Boyce, Mathur and Frank (2023) student replication of Gick and Holyoak, as listed in the FORRT replication atlas (atlas page only; no N). https://forrt.org/flora-replication-atlas/doi/10.1016/0010-0285(83)90002-6
- [M] "Replication of Kurtz and Loewenstein (2007), Memory and Cognition 2017", search summary, could not be verified. https://link.springer.com/article/10.3758/BF03193454
- [V] Puranam, Sen and Workiewicz (2025) Can LLMs help improve analogical reasoning for strategic decisions? https://arxiv.org/abs/2505.00603

**Models and LLM studies**
- [V] McLure, Friedman and Forbus (2015) Extending analogical generalization with near-misses (ALIGN/SAGE). https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2015/McLure-Friedman-Forbus-AAAI15.pdf
- [V] Zheng et al. (2023/2024) Take a step back. https://arxiv.org/abs/2310.06117
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Hong et al. (2024) Abstraction-of-Thought makes language models better reasoners. https://arxiv.org/abs/2406.12442
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620
- [V] Wang et al. (2024) Hypothesis search: inductive reasoning with language models. https://arxiv.org/abs/2309.05660
- [V] Parab, Lu, Wu and Gulwani (2025) Analysis of error sources in LLM-based hypothesis search. https://arxiv.org/abs/2509.01016
- [V] Wang, Mao, Fried and Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Yang et al. (2026) PlugMem. https://arxiv.org/abs/2603.03296
- [V] Webb, Holyoak and Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Hodel and West (2024) Response: emergent analogical reasoning. https://arxiv.org/abs/2308.16118
- [V] Lewis and Mitchell (2024) Using counterfactual tasks / Evaluating the robustness of analogical reasoning. https://arxiv.org/abs/2402.08955 and https://arxiv.org/abs/2411.14215
- [V] Stevenson et al. (2024/2025) Can large language models generalize analogy solving like children can? https://arxiv.org/abs/2411.02348
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229
- [V] Zhang, Madaan, Gao et al. (2024) In-context principle learning from mistakes (LEAP). https://arxiv.org/abs/2402.05403
- [V] Chia et al. (2023) Contrastive chain-of-thought prompting. https://arxiv.org/abs/2311.09277
- [V] Meincke, Mollick, Mollick and Shapiro (2025) Prompting Science Report 2: the decreasing value of chain of thought. https://arxiv.org/abs/2506.07142
- [V] DeepSeek-AI (2025) DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [V] Xu, Xie, Zhao and He (2025) Chain of Draft. https://arxiv.org/abs/2502.18600
- [V] Guo et al. (2026) StyleBench. https://arxiv.org/abs/2509.20868
- [M] Lewin (2026) Missing skill or failed conceptual control? (abstract only). https://zenodo.org/records/23510027
