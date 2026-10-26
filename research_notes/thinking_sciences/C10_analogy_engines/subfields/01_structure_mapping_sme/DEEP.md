# Structure mapping (SME): deep document

*Subfield C10.01. Sources: evidence_a-d.jsonl (a01-a30, b01-b27, c01-c29, d01-d18), claims.jsonl (K01-K37), critique.md, all in this folder. Evidence ids are cited in brackets, claim ids as K##. "Opened" means the page or PDF text was read in the research run. The search tools hit quota limits late in the run, so "no study found" means "not found under a blocked search", not "does not exist".*

## 1. What it is

Structure-mapping theory (Gentner 1983) says an analogy is a mapping of relations from a **base** (the known case) to a **target** (the new case). Object attributes are dropped. Relations between objects are kept. When there are many relations to choose from, people keep the ones that sit inside a connected system tied together by higher-order relations such as CAUSE or IMPLIES. This preference is called **systematicity** [a01].

The Structure-Mapping Engine (SME; Falkenhainer, Forbus, Gentner 1989) is the program form. Input: two descriptions written as predicate-calculus items. Output: a few **global mappings** (gmaps). Each gmap has three parts [a04]:

1. **Correspondences**: which base item maps to which target item.
2. **Candidate inferences**: base facts that have no target match but are tied to the mapped structure, so they are proposed as new facts about the target.
3. **A structural evaluation score (SES)**: a number saying how good the mapping is, using structure only and no domain knowledge.

Why it matters for our agent: this is the spec for operator **O7 (Map an analogue)**. SCHEMA.md O7 now says unaided analogy rarely transfers [E] and the mapping step is [S]. The question for this subfield is whether the mapping step can be done as typed relation lists written by the model, with a small SME-like routine in code computing the mapping, the inferences and the score (SUBFIELDS.md row C10.01). The honest answer from the evidence: the human cognitive science is solid, the algorithm is well documented, LLMs are weak at exactly what SME does well (far analogies against surface distractors), but **no study has tested the central design question**: does a structural score computed from LLM-written relation lists predict that a transferred step helps an agent at equal tokens? [K26, K37, d18].

Links to other subfields run in parallel (not covered here): Plans and schemas, Generation versus evaluation, Worked-example research, Diagnosticity of evidence, Recombinant search, Functional decomposition.

## 2. History and theories in depth

### 2.1 The founding theory (1983)

Gentner (1983) gave three mapping rules [a01]:

1. Discard the attributes of objects.
2. Try to keep relations between objects.
3. Among relations, prefer systems held together by higher-order relations (systematicity).

The worked example is Rutherford's atom. MORE-MASSIVE-THAN(sun, planet) maps because it belongs to the central-force system. HOTTER-THAN(sun, planet) does not, because it is isolated from that system.

The paper also gives a **taxonomy of comparisons** [a02]:

| Type | Attributes mapped | Relations mapped |
|---|---|---|
| Analogy | few | many |
| Literal similarity | many | many |
| Mere appearance | many | few |
| Anomaly | few | few |
| Abstraction | base objects are variables | many |

Heat/water is the standard example. The deep chain is CAUSE{AND[PUNCTURE, CONTAIN], FLOW-FROM}. A shallow chain about a lid containing water exists too. Systematicity picks the deep chain.

The theory is purely syntactic: the rules look at the form of the representation, not at what the domain content means. This is both its strength (domain-general) and its weakness (the answer depends on how the input is written). The 1983 paper also states a hard limit: predicates are matched as identical, and matching similar-but-not-identical predicates would cause an infinite regress [a01].

Early evidence: people interpreting "a cigarette is like a time bomb" gave mostly relational content, and analogies with more relational content were rated more apt (Gentner 1980b, cited only; no N in the 1983 paper) [a03].

### 2.2 Relational selectivity in metaphor (1988)

Gentner and Clement 1988: 16 metaphors. Aptness correlated with relational content r=.65 (judges) and r=.56 (undergraduate raters), and with attributional content r=-.31 (not significant) [a10]. This tests the rival salience-imbalance view (Ortony), which predicts the opposite. Limit: only 16 items, relational content scored after the fact, and the authors accept that some attribute metaphors exist.

### 2.3 The algorithm (1989)

SME works in four steps [a04, b01]:

1. **Local match hypotheses.** Match-constructor rules pair base and target items. By default, items with the same predicate (functor) are paired, and their arguments are paired too.
2. **Gmap construction.** Merge match hypotheses into maximal sets that satisfy two constraints: **one-to-one** (an item maps to at most one item) and **support** (if a match is kept, the matches of its arguments are kept too; also called parallel connectivity).
3. **Candidate inferences.** Base facts that touch the mapped structure but have no target match are proposed as target facts.
4. **Scoring.** Each match gets evidence. A same-functor match gets 0.5. A rule passes 80 percent of a match's belief down to its children (the "trickle-down" of systematicity). The gmap SES is the sum of the match evidence [a05].

Dempster combination was dropped because of round-off errors with many hypotheses and because normalising stops cross-base comparison [a05]. The weights are hand set; the authors say rankings were "not overly sensitive" in preliminary tests, but give no numbers [a05].

Worked examples [a06]:

- Water flow to heat flow: top gmap SES 5.99, then 3.94 and 2.44 (the 3.94 and 2.44 values were not re-checked in the critique pass). Mapping: beaker to coffee, vial to ice cube, water to heat, pipe to bar, pressure to temperature. Candidate inference: temperature difference causes heat flow.
- Solar system to atom: 6.03 for the standard reading (mass difference plus attraction), 4.04 for a reading that maps temperature to mass with little supporting structure, 1.87 for a spurious reading (sun mass to electron mass).
- Run time on a Symbolics 3640: 0.70 s (14 hypotheses), 0.91 s (16), 9.68 s for the large PHINEAS case (69). SME had been applied to over 40 analogies.

Limits: toy descriptions of 11 to 71 expressions written by the authors, and the "right" answer is the one the authors expected [a06].

**Complexity** [a07, b01, b02]: match hypotheses grow about c*N with c under 5 in practice (worst case N^2). Steps up to scoring are about O(N^2). The final merge was worst-case factorial in the original, but the authors saw near best-case behaviour. Runtime depends on **how systematic** the description is, not on its size. Flat, relation-poor descriptions are the slow case. One PHINEAS problem took 53 minutes with flat descriptions and 34 seconds after higher-order structure was added (the authors' own anecdote, no outside replication) [b02].

**Representation sensitivity** [b03]: if base and target are written at different abstraction levels (GREEK-TRAGEDY vs SHAKESPEARE-DRAMA) there are no shared predicates and no analogy is found. Too much detail gives many spurious matches. The authors proposed sliding descriptions up and down an abstraction hierarchy. Lovett and Forbus (2017) later added re-representation after failed matches [b03, a22].

**Match rule sets** (the SME "modes") [a08, a16]:

- Analogy mode: only relations (and functions) match. 
- Mere-appearance mode: only attributes match.
- Literal-similarity mode: both match.

The 1989 paper used the mode switch to simulate a human story study (Karla the hawk). Story set 5: analogy rules scored the true analogy 22.36 against appearance rules 6.41. For the surface-only story, analogy rules gave 16.82 and appearance rules 7.70. Five triads (15 stories) were encoded [a08]. Later work (Forbus 2017) dropped separate rule sets for one similarity rule set in which structure wins by scoring [a02, a18].

### 2.4 Human studies that built the evidence base (1986-1999)

**Gentner and Toupin 1986** [a09, b08]. N=72 children (36 aged 4-6, 36 aged 8-10) acted out a story with toy animals, then again with new characters. Object similarity (transparency) helped everyone. A systematic story (explicit causal chain and moral) helped older children, mostly when the object match was misleading. Stats: Age F(1,68)=14.93, p<.001; Systematicity F(1,68)=6.28, p<.05; Mapping F(2,136)=29.01; Systematicity x Mapping F(2,136)=3.89, p<.05. Older group: t(34)=2.48, p<.01; younger t(34)=1.08, n.s. The systematicity gain was significant only in the hardest (cross-mapped) condition. Limits: no Age x Systematicity interaction in the overall test, so the age difference is not firmly shown; systematic stories were longer; small cells.

**Clement and Gentner 1991** [a11, a12]. Experiment 1: N=48 undergraduates, 4 passage pairs. People rated the key fact inside the shared causal system as more important (M 6.28 vs 4.89 for the isolated fact); a target-only control showed no difference (5.22 vs 5.31). Choice: analogy group chose the shared-system fact 3.17 of 4 times vs 2.0 for target-only, F(1,44)=18.43, p<.001. Per passage, 67-92 percent vs 42-54 percent; Fisher exact significant in 3 of 4 passages. Experiment 2 (N=32, 16 per group), free prediction: shared-system fact .53 of analogy-group responses vs .12 for the other fact; target-only .12 and .12. Choice among supplied predictions: 87 and 69 percent vs 44 and 25 percent on the two passages that differed (2 of 4 passages significant). Interrater agreement .88. Experiment 3 repeated this with other materials (not read cell by cell). Limits: invented creatures, short passages, one passage behaved oddly with poor memory (42 percent) for its base.

**Gentner, Rattermann, Forbus 1993** [a13, a14]. The key dissociation. Experiment 1, N=30 (MIT). Soundness ratings: analogy 4.40, surface match 2.80, first-order-relations match 2.74; F(2,58)=70.51. Retrieval after 6-8 days: surface .78, analogy .44, first-order .25; F(2,58)=75.45. Soundness vs retrieval r(52)=.15, n.s. Across three studies: surface .78/.53/.52 vs analogy .44/.12/.07 (critique re-check). Experiment 2 replicated the retrieval order with a literal-similarity condition: order LS >= SF > AN >= FOR was stable across three variations (numbers second-hand via the MAC/FAC paper: about .53 surface, .12 analogy, .03 first-order). Limits: stories, one lab, one-week delay; the soundness instructions were revised for Exp 2 out of concern that raters judged usefulness.

**Markman and Gentner 1993** [a15, a16]. Rating similarity first pushes people toward relational mappings. Exp 1: relational responses .69 after similarity rating vs .42 one-shot, F(1,33)=7.30, p<.05 (3-mapping control .60). Exp 1b: .69 vs .47 (one-shot) vs .39 (artistry rating first), F(1,69)=6.00 and 11.44. Exp 2: high-systematicity pairs .61 vs .14, t(22)=3.46, p<.01. Low-systematicity pairs gave no clean effect, which the authors called surprising. Item analysis (6 of 8 pairs) was not significant by sign test. SME in literal-similarity mode preferred the relational reading (top gmap 12.94) unless extra shared attributes or a smaller relational structure tipped it to the object match.

**Markman and Gentner 1996** [b10]. Alignable differences (differences attached to matched structure) lower similarity more than unrelated differences. Exp 1: on 88 percent of trials people picked the nonalignable-difference picture as most similar. A boundary on the pure relational account: of 72 consensus alignable differences, 43 (60 percent) came from objects placed in correspondence by attribute similarity.

**Gentner and Markman 1997** [b09, a30]. The review of structural alignment: one-to-one mapping, parallel connectivity, systematicity, alignable vs nonalignable differences, transparency. It lists the benchmark phenomena any model must reproduce: relational similarity, structural consistency, systematicity, candidate inferences, alignable differences, interactive interpretation, multiple interpretations, cross-mapping. It also lists where the pure account fails: retrieval follows surface similarity, and fast responses use local matches. Response-deadline studies: under about 700-1000 ms, people base similarity on local matches (even cross-mapped objects) rather than on relational structure [b09]. The Wolff and Gentner 2011 result (second-hand, not opened): at 500-600 ms there is no difference between a metaphor and its reverse; at 1,200-1,600 ms the forward direction wins. This supports early symmetric alignment and later directional projection of inferences [a20].

### 2.5 Retrieval: MAC/FAC (1995)

Forbus, Gentner, Law 1995 [a17]. Retrieval in two stages. MAC: a cheap dot product over content vectors (counts of predicates) picks a few candidates by surface-heavy overlap. FAC: SME scores the survivors structurally. This reproduces the human order LS >= surface > analogy >= first-order. Simulation on 9 story sets (45 stories). The constraint-satisfaction rival ARCS (Thagard) on the Karla story with 100 fable distractors gave activations LS .67, FOR -.11, SF -.17, AN -.27, which breaks the human order twice. MAC/FAC was about two orders of magnitude faster than ARCS on identical data. ARCS did not settle after 1,000 iterations on some inputs (runs up to 12 hours) [a17, a24]. Limits: matches the ordering, not item-level human data; the ARCS comparison is run by the SME authors on their own encodings; ACME itself was not read.

### 2.6 Rival theories

- **ACME/ARCS (Holyoak and Thagard)** [a24]: a constraint-satisfaction network with structural, semantic and pragmatic constraints, settling to one interpretation. Pragmatic (goal) constraints are explicit.
- **Goal-driven accounts (Holyoak)** [b13]: no separate structural matching stage; mapping is interleaved with problem solving. The SME authors note that systems which carry over relevant structure first lack the focusing a partial match gives, and suspect them to be costlier. The direct experiments (Spellman and Holyoak 1996; Hummel and Holyoak 1997) could not be retrieved.
- **Copycat, LISA, DORA, IAM, SIAM** [a23]: named in the 2025 review; not read.
- **Salience imbalance (Ortony; Glucksberg)** [a10]: attribute-based accounts of metaphor. Some metaphors fit them; Gentner and Clement 1988 favoured relations.
- **Hammond, Seifert, Gray 1991** [b09]: a cited challenge to the retrieval-versus-structure dissociation (not read).

### 2.7 Scaling up and extensions (1990-2017)

**Greedy merge** [a18, a19, c20]. Forbus et al. 2017 changed SME in five ways: greedy merge (1 to 3 best mappings in O(n^2 log n)), incremental mapping, **ubiquitous predicates** (relations like CAUSE that should not drive alignment), structural evaluation of candidate inferences, and match filters for task constraints. Defaults: at most 3 mappings; keep only mappings within 20 percent of the best score (cutoff 0.8). Greedy found the same best mapping as exhaustive merge in 52 of 56 analogies (93 percent; Forbus and Oblinger 1990, second-hand; hand-built set from SME's own library). Grootswagers 2013, reported in the same paper: greedy matched exhaustive on 87.5 percent of generated pairs and 99.89 percent of ACME-dataset play pairs (a different criterion: score optimality). Over 5,843 runs from five task models, runtime tracks n^2 log n at R^2 above 0.9 for geometric analogies, oddity, thermodynamics and AP physics, and above 0.36 for moral decision-making. Actual match hypotheses were 2 to 32 percent of the worst case on average. Greedy fails when many large kernels conflict.

**Inference evaluation** [a21, b04]. Forbus, Gentner, Everett, Wu 1997 added two scores for a candidate inference: **support** (how much of the mapping backs it) and **extrapolation** (how far it goes beyond the mapping). Inferences are held as defeasible beliefs in a truth-maintenance system, tied to belief in the mapping, retracted on contradiction. A simulation reproduced Lassaline (1996): adding a base relation that explains the inferred property raises inductive strength. Heit and Rubenstein (1994) and Osherson et al. (1990) orderings were reproduced qualitatively. In a CyclePad case-based coach prototype, the highest support score always gave the best advice, on a small number of problems. No human data; the extrapolation score experiments were only planned.

**Perception as analogy** [b07]. Lovett, Sagi, Gentner, Forbus 2009: N=20; relational similarity effect on same-different F(1,19)=36.3, p<.01; model local-configuration matches correlate r=.64 and local-object matches r=.54 with performance. Only 10 items.

**Raven's matrices** [a22, b05, b06, c23]. Lovett and Forbus 2017: the SME-based model with CogSketch perception and re-representation solved 56 of 60 Standard Progressive Matrices, 75th percentile of 1993 US adult norms. Human sample (42 Northwestern students, 2 excluded): mean 30.0/36 on 36 items, equal to 54/60 and the 61st percentile. Regressions on model-derived factors explained .63 and .67 of item accuracy variance. The four misses (D11, D12, E11, E12) were among the hardest for people. Mean accuracy and response time correlate r=.89 across the 36 problems. Geometric-analogy model: R^2 above .76 with human reaction times (Lovett and Forbus 2012) [b05]. A 2026 survey quotes 44/48 on sections B to E (converted 55/60) and Evans geometric analogies: all 20 matched the human-preferred answer (N=34 humans; reaction-time r=.59 normal mode, .75 shape-identicality mode) [c23]. Critique correction: the paper's "41st percentile" belongs to a different model with 50/60. The 2025 review says 61st percentile for CogSketch with SME [a23, c21]; this conflicts only by conversion. Limits: hand-built symbolic inputs from sketches; the model does not predict wrong answers people choose; one lab.

### 2.8 Removing the hand-coded input (2008-2023)

**LRME** [a25, c19]. Turney 2008: given two word lists, scores relations between words using corpus statistics and finds the best one-to-one mapping. 91.5 percent on 20 problems (10 science analogies, 10 metaphors) vs 87.6 percent for humans (N=22), not significantly different; best attribute-similarity method 76.8 percent. On 374 SAT analogy questions its relation scorer got 56 percent vs 57 percent for the average human. Limits: word level, no systematicity or inferences, average m=7 so exhaustive m! was workable.

**FAME** [a26, c11, c12]. Jacob, Shani, Shahaf 2023: relations from ConceptNet, Open IE, Quasimodo and GPT-3.5; beam search with a relaxed one-to-one rule. 2x2 problems (80 from Green et al. 2010): near 85 percent, far 77.5 percent (chance 33.3 percent). Extended problems (36, mean domain size 3.3): 77.8 percent perfect (chance 13.1 percent); correct in top-2 83.3 percent, top-3 91.7 percent. Versus LRME on 19 noun-only problems: 84.2 vs 75 percent. Plain GPT-3.5: near 92 (":" prompt) or 88 ("->" prompt), far 80, extended 44 or 58. So GPT-3.5 matches FAME where the 2x2 problems are probably on the web, and falls on larger unseen ones. Ablation: GPT-3 as only knowledge source gave 57.5 / 50 / 66.7; dropping Open IE gave 58.3 on extended. Against humans on one task: 90 vs 70.2 percent. Limits: entity lists only, no inference scoring, small sets, likely leakage on 2x2.

### 2.9 Modern restatements (2025-2026)

- Gentner and Forbus 2025 [a23, c21, c28]: SME in use for four decades; works over representations from language, vision or reasoning; graph matching is NP-complete in general, SME uses an approximate merge; some versions use vector embeddings inside structural scoring (Liang et al. 2016). They call it open whether generative AI can do analogical processing without a symbol system. Self-review, no LLM comparison run.
- Weitekamp and MacLellan 2026, SMTB [d08]: bounded-search structure mapper tested against SME v4 on 5,845 domain pairs (ap-physics 1,137; geometry 873; moral decision 420; oddity 3,411; thermo 4). Total time: SME 70.95 s, greedy SMTB 5.97 s, SMTB width 3 depth 3 30.99 s. Mapping scores 21.6 percent above SME (22.6 percent with 10 paired walks); abstract says about 50 percent better on large nested domains. Authors' own scoring. They also argue that on flat first-order representations SME loses its higher-order bias and acts like greedy merging.
- Donvito and Lieto 2026 [a28, c23]: formal ranking of SME, CogSketch, METCL and LLMs on constraints of structure-mapping theory. Functional/structural ratio: SME and CogSketch 0.606, METCL 0.407, LLMs 0.109. Generality: LLMs 0.500, CogSketch 0.125, SME 0.063. Performance match: SME and CogSketch 0.923, METCL 0.714, LLMs 0.578. This is the authors' scoring grid, not a measurement.
- Lee, MacLellan, Weitekamp 2026 [d13]: structure-mapping guided self-explanation (no LLM): see section 6.

## 3. Core findings with exact numbers

Status key: **replicated** = at least two independent reports in the sources; **single-source**; **contested** = sources disagree; **human-only**; **older models only** = tested on 2023-2024 models.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People pick the fact inside a shared causal system as the key part of an analogy | Choice 3.17 vs 2.0 of 4, F(1,44)=18.43; rating 6.28 vs 4.89; N=48 | Clement & Gentner 1991 [a11] | Human-only; consistent with later reviews [b09]; no modern replication found |
| People predict the target fact that follows from the shared system | Free prediction .53 vs .12 (target-only .12 and .12); N=32 | Clement & Gentner 1991 Exp 2 [a12] | Human-only; 2 of 4 passages significant on choice |
| Soundness follows structure, retrieval follows surface | Soundness 4.40/2.80/2.74; retrieval .78/.44/.25; r(52)=.15; N=30 | Gentner, Rattermann, Forbus 1993 [a13] | Replicated within the paper (3 studies, .78/.53/.52 vs .44/.12/.07) and in simulation [a17]; one lab |
| Surface-heavy retrieval order LS >= SF > AN >= FOR is stable | about .53 / .12 / .03 recall (second-hand) | GRF 1993 Exp 2 via MAC/FAC [a14] | Second-hand |
| Systematic story helps older children in hard conditions | N=72; Systematicity F(1,68)=6.28; older t(34)=2.48; younger t(34)=1.08 | Gentner & Toupin 1986 [a09] | Human-only; no Age x Systematicity interaction |
| Metaphor aptness tracks relational content | r=.65 and .56 vs attributional r=-.31; 16 items | Gentner & Clement 1988 [a10] | Human-only, small item set |
| Rating similarity first increases relational mapping | .69 vs .42 (F(1,33)=7.30); .69 vs .47 vs .39 (Exp 1b); high-systematicity .61 vs .14 | Markman & Gentner 1993 [a15] | Human-only; low-systematicity result unexpected |
| Alignable differences matter more; but 60% of consensus correspondences were attribute driven | 88% picked nonalignable-difference picture; 43/72 | Markman & Gentner 1996 [b10] | Human-only; a boundary condition |
| Fast judgments use local matches | Under about 700-1000 ms local; metaphor direction effect appears by 1,200 ms | Gentner & Markman 1997; Wolff & Gentner 2011 [b09, a20] | Review plus second-hand |
| SME ranks the textbook mapping first by structure only | Heat/water top 5.99; atom 6.03 vs 4.04 vs 1.87 | Falkenhainer et al. 1989 [a06] | Authors' own toy examples; re-confirmed in text [critique] |
| Runtime depends on systematicity, not size | PHINEAS 53 min flat vs 34 s structured | FFG 1989 [b02] | Single anecdote |
| Greedy merge nearly matches exhaustive | 52/56 (93%); 87.5% and 99.89% in Grootswagers | Forbus et al. 2017 [a18, a19] | Replicated (2 datasets), different criteria, hand-built sets |
| Inference support score picks best advice; reproduces induction orderings | Always best on small CyclePad set; qualitative fit to 3 studies | Forbus et al. 1997 [a21, b04] | Single-source, tiny test set |
| Comparing two cases beats separate study | 47% vs 6% baseline (N=48); 48% vs 19% (N=128); negotiation 90% guided, 70% comparison, 55% separate, 37% baseline | Gentner, Loewenstein, Thompson 2003 [b11] | Replicated within paper (3 experiments); business students; 68% said they did not recall the prior cases |
| Inert knowledge: prior case rarely used unprompted | 3 of 16 (19%) used the principle; 50% of those taught transferred vs 19% baseline; Duncker about 10% unaided, 85% after story plus hint (second-hand) | Loewenstein, Thompson, Gentner 1999 [b12] | Replicated (classic; Gick & Holyoak figures second-hand) |
| SME-based model solves Raven's at adult level | 56/60 (75th pct, 1993 norms); humans 54/60 (61st); R^2 .63 and .67 | Lovett & Forbus 2017 [a22, b06] | One lab; hand-built inputs |
| Corpus relations reach human level on word mapping | LRME 91.5% vs humans 87.6% (N=22, 20 problems) | Turney 2008 [a25, c19] | Replicated by FAME's comparison [c11]; small sets |
| LLM-built relations plus mapper beat a mapper alone but plain GPT-3.5 matches on web-available problems | FAME 85/77.5/77.8 vs GPT-3.5 92/80/44 (":" prompt) | Jacob et al. 2023 [a26, c12] | Older models only; leakage likely |
| LLMs fail far analogies against near distractors | ARN far analogies 39.6% (chance 50%); far analogy vs near distractor 33.9%; humans 94.1% | Sourati et al. 2023 [c07] | Older models only (2023 zero-shot); guided prompting did not help [c08] |
| LLMs trail humans on story analogies | Humans 85.7%; ChatGPT about 30%; davinci-003 37.1%; SME-style method 44.9%; gap 37.7 | Jiayang et al. 2023 [c06, b21] | Older models only |
| GPT-3 worse than students on Gentner stories; GPT-4 better on far | OR=.37 p=.0003; GPT-3 far p=.065; GPT-4 far p=.0039; N=54 | Webb et al. 2023 [c01, c02] | Contested by position bias; about 8 items per condition |
| GPT-4 story accuracy depends on answer position and paraphrase | First 1.00, second 0.72 (humans .78 both); paraphrase .86 to .72 | Lewis & Mitchell 2024 [d01] | Single-source; GPT-4-0613 only; 18 stories |
| Letter-string results do not generalise to counterfactual alphabets | Humans .753; GPT-3 .488; GPT-3.5 .350; GPT-4 .452 | Lewis & Mitchell 2024 [b16, d02] | Replicated by Hodel & West [d14] and Stevenson [b18]; contested explanation |
| Alphabet change collapses models, not people | GPT-4o .85 to .48; Llama-405B .79 to .27; adults .88 to .89 | Stevenson et al. 2024 [b18] | Replicated direction; older models |
| Code execution recovers permuted-alphabet performance | GPT-4+code vs humans P=.92; GPT-4 alone P<2e-16 | Webb et al. 2024/2025 [b17, d03] | Contested; authors' own lab; outside lab found no tool gain on ConceptARC [d06] |
| Analogical prompting beats 0-shot CoT, slightly | GSM8K 75.8 to 77.8; MATH 33.9 to 37.3; Codeforces GPT-4 16 to 19 | Yasunaga et al. 2024 [b22, c17] | Replicated direction but mechanism contested |
| Relevance is not what drives analogical prompting on math | GSM8K relevant 71.5 vs N/A 75.5; MATH 33.3 vs 36.1; irrelevant won 6 of 7 MATH subjects | Qin et al. 2025 [b23] | Contested by Yasunaga; BBH is an exception |
| LLM mapping needs abstraction | Raw events 0.17 (chance .25); abstracted 0.46 / 0.45 vs LLM-only 0.41 / 0.28 | YARN 2026 [a27, c09, c10] | Single-source; 8B models; embedding cosine mapper, not SME |
| Hybrid loses on near analogies, mixed on far | Qwen near 0.79 CoT vs 0.69; far 0.52 vs 0.47; Llama far 0.46 vs 0.42 | YARN [c09] | Contested within the paper |
| Reasoning models collapse under noise where a symbolic solver holds | o3-mini 86.6 to 17.0; R1 80.6 to 23.2; ARLC 98.6 to 88.0; chance 12.5 | Camposampiero et al. 2025 [d04] | Single-source; Raven-style arithmetic rules |
| Right answer, wrong rule in text | o3 and Gemini about 27% of correct answers; Claude 19%; humans 7% | Beger et al. 2025 [d07] | Single-source; ConceptARC |
| Giving the text of earlier solutions barely helps frontier models | Gemini 3 Flash 9.08 to 7.33 attempts only significant; GPT-5.2 15.77 to 17.43; humans +33% (d=0.71) | Xiang et al. 2026 [d11] | Single-source; action sequences |
| Structure mapping from worked example orders the search | Intended procedure first 104/120 (86.7%) vs median 32 (26.7%); 93.8% fewer combinations | Lee et al. 2026 [d13] | Single-source; no LLM; random baseline |
| Run-to-run extraction stability is low for long input | Jaccard 0.55 atomic facts, 0.21 paragraphs (gpt-4.1) | ATOM 2025 [d17] | Proxy only; news text |
| One-to-one assignment beats per-item max similarity | SCAR 400 analogies: GPT-4 about 65-69 vs humans 86 | Yuan et al. 2023 [d09] | Single-source; figure not read numerically |

## 4. Mechanisms and models

This section is written so an engineer can build a small SME for O7.

### 4.1 Representation

A case is a set of **expressions**. Each expression is a term of one of three kinds:

- **Entity**: a constant, such as `sun`, `planet`, `beaker`.
- **Attribute**: a one-place predicate on an entity, such as `hot(coffee)`.
- **Relation**: a predicate over entities or over other expressions, such as `greater(mass(sun), mass(planet))` or `cause(greater(pressure(beaker), pressure(vial)), flow(water, beaker, vial, pipe))`.

Order matters: a relation whose arguments include other relations is **higher order**. Each expression has a **depth**: entities and attributes depth 0 or 1; relation depth = 1 + max depth of its arguments. Keep the nested form. Flat lists lose the higher-order signal and SME then reduces to greedy matching [d08].

Functions (like `mass(sun)`) are matched only if their arguments match; non-commutative relations match argument by argument in order; commutative relations (`and`, `equal`) match in any order [a04].

### 4.2 Step 1: local match hypotheses (MH)

For every base expression `b` and target expression `t`:

- If both are relations with the same predicate and the same number of arguments, create a match hypothesis (b, t). Then create MHs for their argument pairs, recursively. If the arguments are entities, the MH is an entity pairing.
- In analogy mode, never pair attributes. In mere-appearance mode, pair only attributes. In literal-similarity mode, pair both [a08].
- Optional: allow matches between non-identical predicates through a minimal-ascension rule (match if they share a close ancestor in a hierarchy) or through re-representation. The 1983 paper warns this can regress without limits [a01]; Forbus et al. 2017 handle it with match filters and re-representation.
- Mark **ubiquitous predicates** (CAUSE, AND, IMPLIES) so that they do not drive alignment on their own [a18].

Practical size: about c*N hypotheses with c under 5 in the original, 2 to 32 percent of the worst case in the 2017 runs [b01, a18].

### 4.3 Step 2: structural evidence (scoring)

Original rules [a05]:

1. Base evidence: a same-functor match gets 0.5 (attribute/function matches get less in the original rule set; the exact table is not in the sources read).
2. Trickle-down: each MH passes 80 percent of its belief to the MHs of its arguments (its children). Because evidence pools through a relation chain, a deeply nested match gives a high score to everything inside it. This is how systematicity is scored without a separate rule.
3. Mapping SES = sum of match evidence over the MHs in the mapping.

Implementation note: do the trickle-down top-down from roots (MHs with no parent). If an MH has several parents, add the passed evidence. Keep a small constant for each rule; the authors did no sensitivity analysis, so treat all constants as to-be-tuned [a05].

### 4.4 Step 3: build gmaps (merge)

An MH is **inconsistent** with another if they map the same base item to different target items or the same target item to different base items (violates one-to-one). An MH is **supported** only if all MHs for its arguments are in the mapping (parallel connectivity).

1. Find **kernels**: maximal sets of structurally consistent MHs rooted at MHs with no parent, closed under their children.
2. **Merge**. Original SME enumerated all maximal merges (worst-case factorial) [a07]. The 2017 greedy merge [a18]:
   - Sort kernels by score.
   - Start a gmap from the highest-scoring kernel.
   - Add the next kernel if it is consistent with the gmap (no one-to-one violation).
   - Repeat; seed further gmaps from other high-scoring kernels.
   - Return at most 3 gmaps, and only those within 20 percent of the best score (score >= 0.8 * best).
   - Complexity O(n^2 log n). Same best map as exhaustive in 52/56 (93%) [a19]; fails when many large kernels conflict.
3. Optional bounded search (SMTB): beam-style search with width and depth limits; on the 5,845-pair corpus it was 5 to 15 times faster than SME at width 3, depth 1, with mappings scoring higher on the authors' scale [d08]. Not independently tested.

### 4.5 Step 4: candidate inferences

For a gmap: take each base expression that (a) is not matched, and (b) has at least one argument that is matched in the gmap. Substitute the mapped target entities for the matched base entities. If a base argument is unmatched, introduce a new target entity (a "skolem"). The result is a **candidate inference** about the target [a04].

Evaluate each inference [a21, b04, a18]:

- **Support**: the fraction (or the evidence sum) of the inference's structure that sits on matched, high-scoring structure. More support gives a more credible inference.
- **Extrapolation**: how much of the inference is new (skolemised or unmatched). More extrapolation gives a less credible inference.
- Keep the inference as a **defeasible** belief attached to the mapping; retract it if the target contradicts it.

The formulas in 1997 were first-pass and the extrapolation score was never tested on humans [b04]. For our agent, a rule such as "accept if support >= s_min and extrapolation <= e_max, and the inference passes a code check on the target" is a design choice to be tuned, not a published rule.

### 4.6 Re-representation and abstraction

When no good mapping appears, SME-based models re-represent: move a predicate up the hierarchy, or split a predicate into parts, then re-run [b03, a22]. In Raven's, the operations needing re-representation were exactly the ones people found hardest, and the amount of re-representation explained item difficulty [a22]. For an LLM-written input, "re-representation" means asking the model to rewrite one case at a more abstract level (YARN's step) [a27]. In YARN, no abstraction gave 0.17 on the multiple-choice set (below the 0.25 chance); adding conceptual plus evaluative abstraction gave 0.46 with Qwen3-8B [c09, c10].

### 4.7 Two-stage retrieval (MAC/FAC)

For a library of stored cases [a17]:

1. **MAC**: turn each case into a vector counting its predicates (content vector). Rank by dot product with the probe. Keep the top few (the paper used a small number).
2. **FAC**: run SME between the probe and each survivor. Return the best one (and others within a threshold).

MAC is blind to structure, so it behaves like surface retrieval. FAC fixes the order. Runtime was about two orders of magnitude lower than ARCS [a17]. For our memory, MAC is an embedding or tag search and FAC is the code mapper.

### 4.8 Relation extraction without hand-coding

- **LRME** (corpus statistics) [a25]: represent each word pair by a vector of patterns found in a large corpus; map by maximising summed pair similarity under one-to-one; exhaustive search is workable at m=7.
- **FAME** (ConceptNet, Open IE, Quasimodo, GPT-3.5 relation sources + beam search) [a26, c11].
- **YARN** (LLM splits a story into event units, abstracts each, a greedy one-to-one mapper scores with embedding cosine) [a27, c09].
- **SCAR assignment** (greedy or Kuhn-Munkres one-to-one over similarity between concept pairs) [d09].

### 4.9 Why it might fail in an LLM scaffold (mechanism-level)

1. **Input noise.** Extraction of facts from the same text by gpt-4.1 overlapped between runs about 0.55 (atomic facts) and 0.21 (paragraphs) [d17]. A mapper over unstable input gives unstable scores. Mitigation (untested): extract three times, keep relations seen at least twice (K30).
2. **Predicate mismatch.** SME needs identical predicates. Two LLM runs name the same relation differently. Mitigation (untested): a fixed predicate vocabulary given in the prompt; a normalisation step in code.
3. **Flat lists.** Without nesting, no systematicity signal [d08].
4. **Abstraction level.** Mismatched levels give no overlap [b03].
5. **Wrong reason.** A transferred step may succeed through a narrow unintended rule (27 percent of correct text answers for o3 and Gemini) [d07].

### 4.10 Interpretability findings (for completeness)

Mid-to-upper layers hold relational information in correct cases and lack it in wrong cases; patching hidden states repairs up to 38.4 percent of failed cases (Gemma-7B; +32.3 percent Llama-2-13B; +35.6 percent Qwen2.5-14B). A linear probe separating analogical from lexically similar stories averages 82.9 percent on layers 20-30 [c16]. A small set of attention heads carries an invariant concept vector for verbal concepts such as antonym; a model can hold the right internal concept and still answer wrong [d15]. Small Transformers trained on synthetic functor tasks show analogy depending strongly on data, optimisation and size [d16]. None of this can be used in a scaffold.

## 5. What holds up

### 5.1 Replications and consistency

**Replicated or consistent across sources:**

- Systematicity as selection constraint (K01): Clement and Gentner 1991 (3 experiments, N=48 and N=32), plus the 1986 child study and the 1997 review. All from the SME group's labs or reviews; no outside preregistered replication was found (gap 8, d18).
- The soundness-retrieval split (K02): three studies in the 1993 paper and the MAC/FAC simulation. The split also means the structural order is **invisible** to cheap retrieval.
- Analogical encoding (K08): three experiments in Gentner et al. 2003 (47% vs 6%; 48% vs 19%; 90/70/55/37 in face-to-face). Business students and negotiation material. Mason and Tornatora and the Alfieri et al. 2013 meta-analysis of case comparison were identified but not opened (d18).
- Inert knowledge (K09): classic. 3 of 16 used the principle unprompted [b12].
- SME on Raven's (K12): two papers from the same group (a22, b06), plus survey numbers (c23). Same lab.
- LRME to FAME to YARN: three different groups built word- or event-level mappers, with the same lesson: relation quality, not search, is the bottleneck (K25).

**Failed or contested:**

- **Letter-string analogy.** Webb et al. 2023 said GPT-3 beat students [b14]. Hodel and West [b15, d14] (humans N=121, GPT-3 N=50): with synthetic alphabets and larger intervals, only 2 of 6 problem types kept GPT-3 near human accuracy. Lewis and Mitchell [b16, d02]: humans .753 vs GPT-3 .488, GPT-3.5 .350, GPT-4 .452; with 0/1/2/3 generalisations: humans .754/.358/.317/.260 and GPT-4 .452/.271/.219/.195 (263 humans). Stevenson et al. [b18]: Latin/Greek/Symbol, GPT-4o .85/.63/.48, Llama-405B .79/.74/.27, adults .88/.91/.89 (n=62). Webb 2024/2025 reply [b17, d03]: the failure is counting; GPT-4 with code reached human level (P=.92), while the "told not to use code" control scored 22.5 percent vs 21.7 percent for plain GPT-4. 38 percent of GPT-4 errors were valid alternative rules vs 39 percent of human errors. This is a split that is not settled: the code result is the original authors' test of their own claim.
- **Digit matrices** [d02]: with the blank in an alternate position, humans .771 and GPT-3.5/GPT-4 .480/.477 (a fall); with symbols in place of digits humans .704 and models .790/.792 (no fall). So models are not uniformly brittle.
- **Story analogies.** Webb's GPT-3 was worse than students; GPT-4's far-analogy win (p=.0039) rests on about 8 items per condition [critique]. Lewis and Mitchell: GPT-4-0613 1.00 when the correct story was first, 0.72 second [d01]. Inani et al. 2025 [c14] found BERT cosine picks the analogy on 78 percent of the 18 items and item-level correlation with human difficulty r=-0.032 (p=.899); gpt-4o 0.8233 and Llama-3.1-70B 0.8538 with the conventional prompt, up to 0.915 with a hint prompt (cell mapping uncertain), against humans 0.847. So current mid-size models reach human accuracy on this small set, but on different items.
- **Analogical prompting mechanism.** Yasunaga: GSM8K 75.8 to 77.8; MATH 33.9 to 37.3; text-davinci-003 GSM8K 50.3 to 61.0; curie model 2 percent in all arms [b22]. Qin et al. [b23]: irrelevant/N/A examples match or beat relevant ones (GSM8K 71.5 relevant vs 75.5 N/A, 76.3 Randomdiff; MATH average 52.4 vs 55.8). Direction repeated on Llama-2-70B-Chat, Llama-3-8B, Llama-3.1-8B, Qwen2.5-14B and GPT-4o-mini. What matters is that the example is **correct**; relevant examples are harder, so they are wrong more often. BBH is an exception. The baselines of the two papers differ (71.5 vs 77.8 for the same model), so they are not like for like.
- **Hybrid mapper.** YARN: helps Llama on far (0.46 vs 0.42) but not Qwen (0.47 vs 0.52 zero-shot); loses on near [c09].
- **Code tools.** Free-form Python did not raise text ConceptARC accuracy for o3 (77.1 to 75.6), Claude Sonnet 4 (60.2 to 55.0) or Gemini 2.5 Pro (66.0 to 60.4) [d06]. But for visual input, o3 went from 5.6 to 29.2.

### 5.2 Moderators and boundary conditions

| Moderator | Effect | Source |
|---|---|---|
| Surface vs structure similarity | Structure drives soundness; surface drives retrieval | a13 |
| Time pressure | Under about 700-1000 ms, local matches; direction effects need 1,200+ ms | b09, a20 |
| Age | Systematicity benefit only in 8-10 year olds, not 4-6 | a09 |
| Task framing | Rating similarity first raises relational mapping (.69 vs .42) | a15 |
| Instruction | Guided analogy 90% vs comparison 70% vs separate 55% | b11 |
| Representation | Flat vs systematic descriptions: 53 min vs 34 s | b02 |
| Abstraction level | Raw events 0.17 vs abstracted 0.46 | c09 |
| Distance | LLMs near 75.0% vs far 39.6% | c07 |
| Distractor type | Far analogy vs near distractor 33.9% | c07 |
| Alphabet/symbol set | GPT-4o .85 Latin to .48 Symbol | b18 |
| Answer position | GPT-4 1.00 first vs 0.72 second | d01 |
| Prompt wording | SCAR template variation across ten templates | d10 |
| Task type | Relevant examples win on BBH, lose on math | b23 |
| Input noise + range | o3-mini 86.6 to 17.0 | d04 |
| Model size | Larger models about 15 points better on stories | c14 |
| Attribute vs relation correspondences | 60% of consensus alignable differences were attribute-driven | b10 |

### 5.3 What worked and what did not (interventions)

**Worked:**
- Comparing two cases side by side with explicit comparison (human) [b11].
- Rating similarity before mapping (human) [a15].
- Adding an abstraction step before structural mapping (YARN, 8B models) [c09].
- One-to-one assignment over similarity scores (SCAR) [d09].
- A hint prompt on the 18 story set (self-generated hint; Inani et al.) [c14].
- Letting the model write and run code for exact counting on permuted alphabets (original authors only) [d03].
- Chain of thought for GPT-4 on SCAR [d09], and zero-shot CoT beating plain GPT-4 on permuted alphabets (P=.004) though it still trailed humans [d03].

**Did not work or unclear:**
- Prompts asking for system mappings on ARN far analogy vs near distractor stayed at 33.9 percent [c08].
- Chain of thought hurt ChatGPT and InstructGPT-003 on SCAR [d09].
- Evaluative abstraction hurt on ARN near (0.67 to 0.63 for Qwen) and stage abstraction hurt on short stories [c10].
- Free Python on text ConceptARC [d06].
- Giving earlier solutions as text (OpenLock) [d11].
- Self-generated "relevant" examples as a mechanism [b23].
- The 1989 SME paper: no sensitivity analysis of weights [a05].

## 6. Language models

### 6.1 Overview of results

LLMs do well on near analogies, on small analogies they may have seen, and on word-level mappings. They do badly on far analogies against surface distractors, under symbol changes, and when applying a relation to new entities.

| Task | Models | Result | Humans | Source |
|---|---|---|---|---|
| ARN near analogies (proverb narratives) | 2023 zero-shot, average | 75.0% (SBERT alone 77.9%) | 97.9% | b20, c07 |
| ARN far analogies | same | 39.6% (chance 50%) | 94.1% | c07 |
| ARN far analogy vs near distractor | same, with system-mapping prompt | 33.9% | n/a | c07, c08 |
| StoryAnalogy MCQ (4 options) | ChatGPT about 30%; davinci-003 37.1%; SME-style 44.9% | gap 37.7 | 85.7% | b21, c06 |
| Gentner 18 stories | GPT-3 .75 (Webb), GPT-4 first position 1.00, second 0.72 | | .847 | c14, d01 |
| Same, 2025 models | gpt-4o 0.8233; Llama-3.1-70B 0.8538; hint prompt up to 0.915 | | .847 | c14 |
| Letter strings, counterfactual | GPT-3 .488, GPT-3.5 .350, GPT-4 .452 | | .753 | b16 |
| Symbol alphabet | GPT-4o .48; Llama-405B .27 | | adults .89 | b18 |
| Raven-style rules, noisy | o3-mini 17.0%; R1 23.2% | symbolic solver 88.0% | n/a | d04 |
| ConceptARC text | o3 77.1; Gemini 2.5 Pro 66.0; Claude Sonnet 4 60.2; GPT-4 25-33 earlier | | 73-91 | d06, b25, b26 |
| SCAR system accuracy | GPT-4 about 65-69; ChatGPT 57.85 | | 86.03 | d09 |
| Word mapping FAME | GPT-3.5 near 92, far 80, extended 44 | FAME 85, 77.5, 77.8 | | c12 |
| OpenLock transfer | GPT-5.2 15.77 to 17.43 attempts | | humans 20.66 to 13.85 | d11 |
| Cross-field retrieval (CPR) | Best of 11 retrievers Recall@10 0.26; LLM reranker 0.81 | | | d12 |

### 6.2 What changed performance, and by how much

- **Model scale and recency.** GPT-3 to GPT-4 on far story analogies: not above chance (p=.065) to p=.0039 [c01, c02]. Larger models about 15 points better on the 18-story set [c14]. Llama-3.1 8B to 70B in the same set: 0.6528 to 0.8538 under the conventional prompt [c14].
- **Hint prompts.** A self-generated hint raised both families, best 0.915 (cell mapping uncertain) [c14].
- **Abstraction step before structural mapping.** 0.17 to 0.46 (Qwen3-8B MCQ) and an LLM-only 0.28 to 0.45 for Llama [c09].
- **Hybrid.** Helps Llama far (+0.04), hurts Qwen far (-0.05) and hurts near (-0.10 Qwen, -0.03 Llama) [c09].
- **Code execution.** Permuted-alphabet letter strings: GPT-4 alone about 21.7 percent to human level with code [d03]. No gain on ConceptARC text [d06].
- **Chain of thought.** On SCAR, helped GPT-4 but hurt weaker models [d09]. On permuted alphabets, helped GPT-4 a little [d03].
- **Reasoning models.** On ConceptARC text, o3 77.1 beats humans 73 [d06]; but about 27 percent of correct answers rest on a wrong or unintended rule vs 7 percent for humans [d07]. On noisy Raven-style rules, reasoning models fall to 17.0-23.2 percent and use 4,486 to 19,449 tokens per item; a neuro-symbolic solver kept 88.0 percent [d04, d05].
- **Retrieval.** Retrievers built for topic similarity are weak on structural analogy (Recall@10 0.26); an LLM reranker reaches 0.81; fine-tuning on CPR-train (10,573 pairs) reaches up to 0.70 and carries to held-out domains [d12]. Labels are LLM judgments.
- **Order and paraphrase.** Position bias (1.00 vs 0.72) and paraphrase drop (.86 to .72) in GPT-4-0613; none in humans [d01].
- **Structure mapping used without an LLM.** Anchoring the search on a mapping put the intended procedure first for 86.7 percent of 120 numeric changes vs 26.7 percent random, with 93.8 percent fewer combinations tested [d13].
- **Analogical prompting and thought propagation.** +1 to +4 points on GSM8K/MATH [b22]. Thought propagation: shortest-path optimal rate GPT-3.5 0.65 vs IO 0.33, CoT 0.26, ToT 0.22; GPT-4 0.88 vs 0.78; PaLM-2 0.36 vs 0.24; +13% creative writing preference; +15% ALFWorld completion (134 tasks); higher token cost; no control for random examples [c18].

### 6.3 What LLMs appear to do

- Association over structure. Stevenson 2023 (quoted in a 2026 survey, second-hand): proportional-analogy success on A:B::C:? reaches about 7-12 year old children, driven by association between C and D [c24]. SBERT alone gets 77.9 percent on ARN near, above the LLM average of 75.0 percent [b20]. BERT cosine picks the analogous story on 78 percent of the 18 items [c14].
- Models are pulled by hard negatives that share entities [b21]. Chance is 25 percent on 4-way StoryAnalogy; ChatGPT scored about 30 percent.
- Models know the rules in isolation (Next/Previous letter checks; GPT-4 1.0 on successor comprehension checks) yet fail when applying them to a new alphabet [b18, d02]. Interpretability work points to applying relations to new entities as a second bottleneck [c16].
- Item difficulty for models does not track item difficulty for humans: r=-0.032 [c14].
- A survey rating finds no strong evidence for systematicity or explicit inferential projection in LLMs (functional/structural ratio 0.109 vs 0.606) [a28, c23]. Authors' scoring, not an experiment.
- Gentner and Forbus 2025 [a23] call open whether generative AI can do analogical processing without a symbol system.

### 6.4 Coverage gaps

Almost all tests use 2023-2024 models (GPT-3 to GPT-4o, Qwen3-8B, Llama-3.1-8B). **No ARN, StoryAnalogy or Gentner-story run with a 2025-2026 reasoning model was found.** The nearest are ConceptARC (grid puzzles) and noisy Raven-style rules [d04, d06]. Item counts are small (18 stories; about 8 per condition for the GPT-4 far result). Treat the 2023 numbers as a lower bound on current ability and as a guide to the failure type, not as a measure of today's models.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5. Status: **[E]** established (two or more independent sources, or a definitional property of the algorithm), **[S]** single-source, **[C]** contested. "Established" for human findings means established in people; it does not show that the step helps the agent. That is what the tests in section 8 are for (G7).

### Add now (established)

1. **Treat O7 as an impasse and open-mode operator only. Keep it.** (O7/G1) [E]. People rarely use a known analogue unprompted (3 of 16; 19%) [b12, K09]; distant analogues are higher variance (SCHEMA O7, F05). Evidence ids: b12, b11, K09.
2. **When the agent holds two solved cases, put them side by side with an explicit compare step, not a list.** (O7/S2 REPRESENT) [E] in people. 47% vs 6%; 48% vs 19%; 90/70/55/37 [b11]. LLM effect untested, so this goes in as the default format for O7 prompts but must also be run as test T4. Evidence: b11, b12, K08.
3. **Do not use embedding or topic similarity as the evidence that a retrieved case will help.** (memory) [E]. Retrieval follows surface similarity (.78 surface vs .44 analogy), and soundness is uncorrelated with retrieval (r=.15) [a13]. Standard retrievers got Recall@10 0.26 on structural analogy [d12]. Memory rule: log whether a retrieved case actually helped, and never raise a case's trust from retrieval score. Evidence: a13, a17, d12, K02.
4. **Any bench claim that credits "analogy" for a gain must include a random-correct-example control arm.** (G7) [E-ish, C on mechanism]. Qin found irrelevant but correct examples match relevant ones (GSM8K 75.5 N/A vs 71.5 relevant) [b23]; the Yasunaga gain is only 1 to 4 points [b22]. Evidence: b22, b23, K22.
5. **Do not use letter-string or similar toy-analogy scores as evidence that the agent maps well.** (G7) [E]. Models fall from .85 to .48 under an alphabet change; humans stay level [b18]. Use counterfactual variants as controls. Evidence: b14-b18, d02, d14, K18.
6. **Re-check every transferred step on the new problem and judge it by the check, not by the model's story.** (G3, G10, S4) [E] via existing guardrails; supported by wrong-reason rates of 27 percent [d07] and weak transfer of exact solutions [d11] (both single-source in this subfield). Evidence: d07, d11, K33, K34.
7. **Enforce one-to-one in code when a mapping is accepted.** (O7) [E] as a defining constraint of the theory and of every mapper in the sources [a04, a25, a26, d09]; the benefit in LLM-written mappings is untested (T2). Evidence: a04, d09, K06, K36.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T-a | Typed relation lists written by the model, scored by a small SME in code, as the O7 mapping step | O7 | [S] | a04, a06, c09, K26, K37 |
| T-b | Score predicts benefit of the transferred step (the core experiment) | O7, S7 | no evidence, open | b27, d18, K26 |
| T-c | Route by surface overlap: structural step only for far analogues | S0/O7 | [C] | c09, c10, K14 |
| T-d | Abstraction step before mapping | O7 | [S] | a27, c09, K13 |
| T-e | Extract relation lists three times, keep relations seen at least twice | O7 | [S] | d17, K30 |
| T-f | Support/extrapolation gate on candidate inferences | O7/S4 | [S] | a21, b04, K07 |
| T-g | Shuffle candidate order, vote over three orders | O7/G4 | [S] | d01, K29 |
| T-h | MAC/FAC style two-stage retrieval in memory | memory | [S] | a17, a24, K03 |
| T-i | Anchor candidate ordering on the mapping | O7/S4 | [S] | d13, K35 |
| T-j | Code tool for exact counting/matching on relational items | O7 | [C] | b17, d03, d06, K19 |
| T-k | Greedy merge vs bounded search | O7 | [S] | a19, d08, K31 |
| T-l | Right-reason check: ask the model to state the rule, then check rule against held-out cases | S8/G3 | [S] | d07, K33 |
| T-m | "Rate similarity first" step before mapping | O7 | [E] human, untested LLM | a15, K10 |

Details of each test are in sections 8 and in UNKNOWNS.md.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count setup, extraction and mapping tokens; G7). Report the mean and a bootstrap 95% interval over items; use at least 3 seeds per arm because samples from one model are not independent (G4). Every test needs a held-out part (G3). Items come from the bench families named below.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1. Score vs benefit (core) | Problems with a known solved analogue and a mix of structurally good and surface-only analogues (ARC variants, BrainTeaser puzzles, our own 60 pairs with labels from construction) | Transfer the step from an analogue; measure benefit as solved-with-transfer minus plain; correlate with the code SES computed from model-written relation lists; compare with an embedding-similarity predictor | Spearman rho between score and benefit; AUC of SES for predicting "transfer helps"; compare AUC vs embedding cosine | SES AUC at least 0.10 above embedding cosine on far pairs. No effect on near pairs is expected (SBERT already 77.9% near) |
| T2. Code mapper vs model-only mapping | Far-analogy items with surface distractors (ARN-style, StoryAnalogy-style, plus our own), 3+ entities per case | (A) model picks the analogue from a plain prompt; (B) model writes relation lists, code picks by SES with one-to-one; (C) same as A with "use system mappings" prompt (this failed at 33.9% in ARN). Equal tokens: B's extraction tokens are paid out of A's reasoning budget | Accuracy of picking the structural analogue; accuracy on far analogy vs near distractor | B above A by at least 10 points on far vs near distractor; no gain on near-near |
| T3. Routing by distance | Mixed near and far items | (A) always plain; (B) always structural; (C) structural only if surface overlap (embedding cosine or shared-word rate) is below a cut | Accuracy and tokens | C at least as good as the better of A or B on both strata; B worse than A on near (YARN pattern: 0.79 vs 0.69) |
| T4. Analogical encoding in the agent | Pairs of solved cases and a third target of the same principle | (A) both cases listed separately; (B) both cases plus "state what the two share, then solve"; (C) B with a random-correct case replacing the second | Solve rate on the target; rate of citing the principle | B above A; C removes most of the gain if the gain is relational (Qin-style control). Human effect size 47% vs 6% will not carry over as is |
| T5. Abstraction ablation | Same as T2 | Raw relation lists vs lists abstracted one level by the model vs lists with fixed predicate vocabulary | Mapping accuracy; SES gap between correct and spurious mapping | Abstracted above raw (YARN: 0.17 vs 0.46) |
| T6. Relation-list stability | 40 cases | Extract 3 times; compute Jaccard of relations, keep relations seen in at least 2 of 3, compare mapping scores before/after filtering | Jaccard; rank stability of top gmap; accuracy | Jaccard about 0.5 raw (ATOM proxy 0.55 atomic, 0.21 paragraph); filtering raises stability at a token cost x3 on extraction only |
| T7. Inference gating | Candidate inferences from T1 transfers | Accept all; accept if support >= s; accept if code check passes | Rate of wrong steps accepted; final solve rate | Gate lowers wrong-step rate by at least 25% relative with no more than 5% loss of correct steps |
| T8. Order bias | Candidate list selection | Fixed order vs three shuffled orders with majority vote | Accuracy; position gap (correct first minus second) | Position gap near 0 for shuffled; GPT-4-0613 gap was 0.28 [d01]; current models unknown |
| T9. Two-stage retrieval | Case library of 200 solved cases | Embedding top-1; embedding top-5 then SES re-rank; plain recency | Share of retrieved cases that actually help when transferred | Re-rank raises helpful-share on far queries; no change on near |
| T10. Code tool for exact matching | Counterfactual relational items (renamed predicates, permuted alphabets, 3+ entity one-to-one mapping) | No tool vs tool for counting and matching | Accuracy under symbol renaming (b18 style) | Gain only on counting-heavy items (d03); none on ConceptARC-style text (d06) |
| T11. Anchored ordering | Procedure-transfer items (worked example to new numbers) | Model-ordered candidate list vs list ordered by link to the mapped region | Rank of first correct candidate; tests needed | Mirrors d13 (86.7 vs 26.7) only against a random baseline; vs a model-ordered list the effect is unknown |
| T12. Right-reason audit | Subset of T1/T2 with known rules | Accuracy-only vs accuracy plus held-out-case check of the stated rule | Rate of correct-for-wrong-reason | Wrong-reason rate near 27% in text (d07) unless the check catches it |

Operational rule for all of them: add an element to SCHEMA.md only if it wins at equal tokens on at least two different item families (G7), with the threshold stated in UNKNOWNS.md.

## 9. What does not transfer, and why

- **Human retrieval findings do not give us a retrieval design.** The 1993 split (retrieval is surface-driven, soundness is structural) describes people's memory. In the agent, retrieval is something we choose. The finding does tell us what to guard against (surface twins), not what to build.
- **Time-pressure results (500-600 ms, 1,200 ms).** Our agent has no response deadline in that sense. Low priority (K11).
- **Developmental findings (ages 4-6 vs 8-10).** Not applicable to a trained model.
- **Hand-built inputs.** SME results (5.99, 6.03, Raven's 56/60) used representations written by the SME authors or by CogSketch from hand-drawn sketches. They show that the algorithm works on good input. They do not show it works on LLM-written input [a06, a22, K04, K12].
- **SME's exhaustive-merge complexity.** Our case descriptions are small (tens of expressions). Runtime is not our problem; relation quality is (K25, K13).
- **Letter-string and digit-matrix results.** They test a different thing (rule induction over symbol sequences) and are open to training-data and counting explanations. Not a basis for the mapping step (K18).
- **Raven's percentile claims.** Depend on 1993 norms and a one-off conversion; 61st vs 75th percentile are both reported for what is the same system [c21, a22].
- **Cognitive-plausibility rankings** (LLMs 0.109 vs SME 0.606) are the authors' scoring grid, not measurements. They do not tell us whether a scaffold step helps [K28].
- **Mechanistic findings (hidden-state patching, concept vectors, functor Transformers).** Need access to weights. Not testable in a scaffold [K27].
- **Extrapolation to a "pure LLM does no structure mapping" claim.** The evidence is on 2023-2024 models. Do not use it to forecast current reasoning models.
- **The yes/no premise of the Yasunaga prompting gain.** The gain is 1 to 4 points and may be a correct-example effect, not a mapping effect. Not a basis for believing that LLMs "map" [b22, b23].
- **Gain from outside datasets with LLM-made labels** (CPR, StoryAnalogy): the ceiling is capped by annotator agreement (kappa 47% and 42%) and labels made by LLM judgments [b21, d12]. G8 also warns that model judges are poor selectors.

## 10. Open questions

1. Does an SME-style score from LLM-written relation lists predict whether a transferred step helps, at equal tokens? (K26, K37; none found.)
2. How do frontier reasoning models (2025-2026) do on ARN far analogies, StoryAnalogy, and the Gentner 18 stories, with and without a code-side structure step?
3. How much do LLM-written relation lists vary across runs, paraphrase and abstraction level, and how does that move the mapping score? Only the proxy (Jaccard 0.55 and 0.21) exists.
4. Is the structural step useful only for far analogies, so routing by overlap pays? (One paper, YARN.)
5. What is the net token cost of a structured mapping step against side-by-side case comparison?
6. Does analogical encoding reproduce in LLMs, and does a random-correct-case control remove it?
7. Does support-based gating reduce wrong transfers in a model? What threshold? Only a small coaching prototype and a simulation exist.
8. Are the classic human results (Clement and Gentner 1991; Gentner and Toupin 1986; Markman and Gentner 1993) robust in preregistered or many-lab replications? The Alfieri et al. 2013 meta-analysis of case comparison and Mason and Tornatora were identified but not opened.
9. Does a code tool for exact counting fix counterfactual-alphabet failure in an outside lab?
10. Does answer-order and paraphrase sensitivity persist in current models, and does shuffle-and-vote remove it?
11. Do relation lists written by the model contain the higher-order structure SME needs, or do they come out flat (making SME reduce to greedy matching, d08)?
12. When do transferred steps succeed for the wrong reason (27 percent of correct text answers in ConceptARC), and does an SES filter catch them?
13. Which predicate vocabulary (fixed or free) gives the best mapping accuracy?
14. Does SMTB-style bounded search beat greedy merge on LLM-written lists in terms of downstream help (not only mapping score)?

## 11. Sources

[V] = opened and read (page or PDF text) in the research run. [M] = snippet, citation inside another paper, or second-hand only.

**Founding theory and algorithm**
- [V] Gentner 1983, Structure-mapping: a theoretical framework for analogy. https://groups.psych.northwestern.edu/gentner/papers/Gentner83.2b.pdf (a01-a03)
- [V] Falkenhainer, Forbus, Gentner 1989, The Structure-Mapping Engine: algorithm and examples. https://www.qrg.northwestern.edu/papers/Files/smeff2(searchable).pdf (a04-a08, b01-b03, b13)
- [V] Forbus, Ferguson, Lovett, Gentner 2017, Extending SME to handle large-scale cognitive modeling. https://doi.org/10.1111/cogs.12377 and https://groups.psych.northwestern.edu/gentner/papers/ForbusFergusonLovett&Gentner_2017.pdf (a18, c20)
- [M] Forbus and Oblinger 1990, greedy merge, as reported in Forbus et al. 2017 (a19)
- [V] Forbus, Gentner, Everett, Wu 1997, Towards a computational model of evaluating and using analogical inference. https://www.qrg.northwestern.edu/papers/Files/CogSci97_analogical_inference_paper.pdf (a21, b04)
- [V] Forbus, Gentner, Law 1995, MAC/FAC. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_1994/Forbus_1994_MAC_FAC_Model_Similarity-Based_Retrieval_CogSci-v2.pdf (a17, a24; a14 is second-hand from this paper)
- [V] Gentner and Forbus 2025, The Structure-Mapping Engine: a multidecade interaction between psychology and AI. https://doi.org/10.1177/09637214251395678 and https://groups.psych.northwestern.edu/gentner/papers/GentnerForbus-2025-SME.pdf (a23, c21, c28)
- [V] Weitekamp and MacLellan 2026, SMTB. https://arxiv.org/abs/2609.25508 (d08)
- [V] Lee, MacLellan, Weitekamp 2026, Structure-mapping-guided self-explanation. https://arxiv.org/abs/2609.33079 (d13)

**Human studies**
- [V] Gentner and Toupin 1986. https://doi.org/10.1207/s15516709cog1003_2 and https://groups.psych.northwestern.edu/gentner/papers/GentnerToupin86.pdf (a09, b08)
- [V] Gentner and Clement 1988. https://doi.org/10.1016/S0079-7421(08)60042-5 (a10)
- [V] Clement and Gentner 1991. https://doi.org/10.1207/s15516709cog1501_3 (a11, a12)
- [V] Gentner, Rattermann, Forbus 1993. https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf (a13)
- [V] Markman and Gentner 1993. https://groups.psych.northwestern.edu/gentner/newpdfpapers/MarkmanGentner93c.pdf (a15, a16)
- [V] Markman and Gentner 1996. https://groups.psych.northwestern.edu/gentner/papers/MarkmanGentner96.pdf (b10)
- [V] Gentner and Markman 1997. https://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman97.pdf (b09); [M] benchmark list via Forbus 2017 (a30)
- [V] Gentner and Markman 1993, Analogy: watershed or Waterloo (NIPS 5). https://papers.nips.cc/paper/1992/hash/ (a29)
- [V] Gentner, Loewenstein, Thompson 2003. https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf (b11)
- [V] Loewenstein, Thompson, Gentner 1999. https://groups.psych.northwestern.edu/gentner/papers/LoewensteinThompsonGentner99.pdf (b12; Gick and Holyoak and GRF 1993 figures second-hand)
- [M] Wolff and Gentner 2011, via two reviews (a20)
- [V] Lovett, Sagi, Gentner, Forbus 2009. https://www.qrg.northwestern.edu/papers/Files/QRG_Dist_Files/QRG_2009/Analogy09_SimilarityAsAnalogy_Revised.pdf (b07)
- [V] Lovett and Forbus 2017. https://doi.org/10.1037/rev0000039 and https://www.qrg.northwestern.edu/papers/Files/LovettForbus_2017-ProbSolving.pdf (a22, b06)
- [V] Forbus, Liang, Rabkina 2017. https://www.qrg.northwestern.edu/papers/Files/Forbus_Liang_Rabkina-2017-Topics_in_Cognitive_Science.pdf (b05)
- [M] Alfieri, Nokes-Malach, Schunn 2013 (case comparison meta-analysis) and Mason and Tornatora: identified by DOI, publisher 403, not opened (d18)
- [M] Spellman and Holyoak 1996; Hummel and Holyoak 1997; Hammond, Seifert, Gray 1991: named only (b13, b09)

**Computational descendants**
- [V] Turney 2008, LRME. https://doi.org/10.1613/jair.2693 and https://arxiv.org/abs/0812.4446 (a25, c19)
- [V] Jacob, Shani, Shahaf 2023, FAME. https://arxiv.org/abs/2311.01860 (a26, c11, c12)
- [V] Khojasteh et al. 2026, YARN. https://arxiv.org/abs/2603.29997 (a27, c09, c10)
- [V] Donvito and Lieto 2026. https://arxiv.org/abs/2605.01359 (a28, c23); second-hand lines inside: [M] Stevenson 2023 (c24), [M] Wachowiak and Gromann 2023 (c26)
- [M] Nakos and Forbus 2023, Companion with LLMs: citation only. https://doi.org/10.1609/aaaiss.v2i1.27700 (c27)

**LLM studies**
- [V] Webb, Holyoak, Lu 2023. https://arxiv.org/abs/2212.09196 (b14, c01, c02)
- [V] Hodel and West 2023. https://arxiv.org/abs/2308.16118 (b15, d14)
- [V] Lewis and Mitchell 2024 (letter strings and short version). https://arxiv.org/abs/2402.08955 (b16, c03, c04); robustness paper https://arxiv.org/abs/2411.14215 and https://arxiv.org/html/2411.14215v1 (d01, d02)
- [V] Webb, Holyoak, Lu 2024/2025 reply. https://arxiv.org/abs/2404.13070 and https://sites.lifesci.ucla.edu/psych-cvl/wp-content/uploads/sites/162/2025/08/A149.Webb-et-al.PNAS-nesus.pdf (b17, d03)
- [V] Stevenson et al. 2024. https://arxiv.org/abs/2411.02348 (b18)
- [V] Musker et al. 2025. https://arxiv.org/abs/2406.13803 (b19, c13; per-condition values not transcribed)
- [V] Sourati et al. 2023, ARN. https://arxiv.org/abs/2310.00996 (b20, c07, c08)
- [V] Jiayang et al. 2023, StoryAnalogy. https://arxiv.org/abs/2310.12874 (b21, c06)
- [V] Yasunaga et al. 2024. https://arxiv.org/abs/2310.01714 (b22, c17)
- [V] Qin et al. 2025. https://arxiv.org/abs/2404.12728 (b23)
- [V] Hu et al. 2023. https://arxiv.org/abs/2305.17626 (b24)
- [V] Moskvichev, Odouard, Mitchell 2023, ConceptARC. https://arxiv.org/abs/2305.07141 (b25)
- [V] Mitchell, Palmarini, Moskvichev 2023. https://arxiv.org/abs/2311.09247 (b26)
- [V] Inani et al. 2025. https://arxiv.org/abs/2507.10957 (c14, c15)
- [V] Lee et al. 2025, The curious case of analogies. https://arxiv.org/abs/2511.20344 (c16)
- [V] Yu, He, Ying 2024, Thought propagation. https://arxiv.org/abs/2310.03965 (c18)
- [V] Yuan et al. 2023, SCAR. https://arxiv.org/abs/2305.12660 (d09, d10; c25 was second-hand and is replaced)
- [V] Camposampiero et al. 2025. https://arxiv.org/abs/2503.11207 (d04, d05)
- [V] Beger et al. 2025. https://arxiv.org/abs/2510.02125 (d06, d07)
- [V] Xiang et al. 2026, OpenLock transfer. https://arxiv.org/abs/2604.24062 (d11)
- [V] Jung et al. 2026, Cross-pollination retrieval. https://arxiv.org/abs/2610.25678 (d12)
- [V] arXiv 2503.03666, concept vectors (abstract page only). https://arxiv.org/abs/2503.03666 (d15)
- [V] arXiv 2602.01992, analogical reasoning via functors (abstract page only). https://arxiv.org/abs/2602.01992 (d16)
- [V] ATOM, arXiv 2510.22590 (extraction stability). https://arxiv.org/abs/2510.22590 (d17)
- [M] Search coverage and gap logs (c29, d18, b27): notes, not sources.

*Opened:false lines in the evidence files (treat as unverified): a14 (partly checked in critique), a19, a20, a30, c05 (replaced by d14), c22 (numbers re-checked in critique), c24, c25 (replaced by d09), c26, c27, c29.*
