# Structure mapping: deep document

Subfield A11.01. Evidence ids (a01-a27, b01-b27, c01-c25, d01-d19) are in evidence_a-d.jsonl. Claim ids (A11.01-K01 to K24) are in claims.jsonl. Open items are in UNKNOWNS.md.

## 1. What it is

Structure mapping is a theory of how people compare two cases. It says the match is built on relations, not on object features. A relation like "A causes B" in one case is paired with a relation in the other case. The objects in those relations are then paired too.

Three rules constrain the match (a17, a03):
- One-to-one: each element maps to at most one element.
- Parallel connectivity: if two statements match, their arguments must match too.
- Systematicity: prefer a connected system of relations, especially one held together by higher-order relations such as "cause" or "implies", over a pile of isolated matches.

A fourth step is carryover. Statements in the base that are linked to the match but missing in the target become candidate inferences (a03).

The theory is deliberately narrow (a27, a08). It covers the mapping stage only. Retrieval (finding the base) follows surface similarity. Judging the result and re-representing the cases are separate steps. SME deliberately ignores relevance and goals.

Why it matters for our agent: schema operator O7, "map an analogue", asks for a typed mapping checked by code. Structure mapping gives the scoring rule for that check. The theory uses only the form of the representation (types and nesting), not domain knowledge (a01). So a code scorer is faithful to it.

The honest state of the evidence:
- The human selection effect rests on one lab (Gentner group), small N, mostly 1986-1997 (K01, K19).
- The computational model works on hand-built input (a26).
- LLMs do well on easy analogies and fail on far, permuted or counterfactual ones (K09, K11, K16, K21).
- No study shows that a code-scored mapping beats free-text mapping at equal tokens (K20).

## 2. History and theories in depth

**Gentner 1983 (a01, a02).** The founding paper. It claims analogy maps relations, not attributes, and that systematicity selects which relations. It separates analogy, literal similarity and abstraction by how many attributes carry over. It predicts an access asymmetry: analogies are harder to notice than literal matches, because noticing needs relational access. The scan could only be read on the last pages (summary, discussion, references). The core experiments of this paper were never verified (d05). We cite its claims only through later papers.

**Gentner and Gentner 1983, flowing waters (d04).** The empirical anchor. People who hold a "water flow" or "moving crowd" model of electricity solve circuit problems in the pattern the model predicts. Exp 1: 36 students recruited, only 15 kept (7 fluid, 8 crowd) because they showed a consistent model. Model x component interaction F(1,13)=4.53, p<.05. Exp 2 (N=18) supported one prediction (parallel-resistor current: crowd .93 vs .63) and failed another (reservoir group should excel at batteries: .40, ns). The textbook story is stronger than the data. A mapping can only transfer structure the reasoner actually holds (base-domain scores were low, .32 to .42).

**Gentner and Toupin 1986 (a09, a10).** Children (5-7 and 8-10, about 72) acted out stories, then re-acted them with new characters. Transparency (look-alike objects) helped both ages. Systematicity helped only 8-10 year olds, and only when objects were cross-mapped. Systematicity x mapping F(2,136)=3.89, p<.05. Older group t(34)=2.48; younger t(34)=1.08, ns. The age x systematicity interaction was not significant, so the developmental claim is tentative.

**SME, Falkenhainer, Forbus, Gentner 1989 (a03-a08).** The algorithm. See section 4. Key design choices: structural consistency is a hard constraint; systematicity is a soft score; match rules are swappable (analogy, literal similarity, mere appearance, abstraction). Early versions used Dempster's rule to combine evidence, which caused roundoff problems; the final form is a plain sum. The authors argued against Holyoak's purely pragmatic account: without structural consistency the search space explodes, and relevance cannot be required because analogy also explains and notices irrelevant commonalities.

**Holyoak and Thagard 1989, ACME (a24).** The main rival. A constraint-satisfaction network where structure, semantic similarity and pragmatic centrality are soft pressures. It lets non-identical relations map. Run on the Gentner-Toupin stories, it found the right mapping in all conditions except the unsystematic cross-mapped one, where it failed to settle until parameters were changed.

**Clement and Gentner 1991 (d01-d03).** The key human test that systematicity selects among matches. See section 3.

**Markman and Gentner 1993, Gentner and Markman 1997 (a14-a17).** Structural alignment also governs similarity. Alignable differences (tied to the shared structure) are listed more readily than non-alignable ones. Retrieval is surface-driven while soundness judgments are structure-driven.

**Hummel and Holyoak 1997, LISA (a25).** Argues SME and ACME build many local hypotheses then discard most, which is implausible for working memory. LISA uses binding by synchrony and a limit on active bindings, and links access and mapping. The capacity claim is theory; no measured test was read.

**Forbus et al. 1998 (a26).** Reply to Chalmers, French and Hofstadter (1992), who charged SME with hand-coded input. The reply: representations were built by other programs; inputs hold irrelevant matches. Hand-coded input stays a real cost. Chalmers et al. itself was not opened.

**Forbus, Ferguson, Lovett, Gentner 2017 (a19-a23, d06).** SME version 4. Tiered identicality (predicates match if identical, or if they are functions whose match enables a bigger structure). One overall similarity scheme replaced separate rule sets. Greedy merge, polynomial time. Candidate-inference scores (support and extrapolation). The authors admit no consensus on how central systematicity or pragmatics is.

**Neural and fast variants (c17, b13, d07).** AMN (Crouse et al. 2020) trained a graph network on 100,000 synthetic analogies and reached 95-104% of SME structural score. SMTB (Weitekamp and MacLellan 2026) drops the higher-order bias, runs 5-15x faster, and finds about 50% better mappings on large nested domains. It questions systematicity as a hard rule.

**LLM era (2023-2026).** Webb et al. 2023 claimed emergent analogy in GPT-3. Hodel and West, then Lewis and Mitchell, showed it breaks on counterfactual variants. Webb et al. 2024 replied that part of the failure is procedural. Newer work builds hybrids (YARN, PRISM) where an LLM extracts structure and code maps it. See section 6.

## 3. Core findings with exact numbers

Status key: replicated (independent sources agree), single-lab (one lab only), single-source, contested, theory-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Shared-system fact preferred over equally plausible isolated fact (ratings and choice) | Exp 1 N=48: ratings 6.28 vs 4.89 (target-only controls 5.22 vs 5.31); choice 3.17 vs 2.0 of 4, F(1,44)=18.43; per passage 67-92% vs 42-54%; 3 of 4 passages significant | Clement and Gentner 1991 (d01) | single-lab |
| Same, in free prediction | Exp 2 N=32 (16/16): shared .53, different .12 (controls .12/.12); net count 1.63 vs 0, F(1,28)=20.05; without biased passage F(1,28)=13.03 | d02 | single-lab |
| Same, base held in memory | Exp 3 N=48 (24/24): net .92 vs .13, F(1,44)=5.15, p<.05; Passage 2 failed (.54 vs .58) after poor base encoding (42% missed the base) | d03 | single-lab, smaller |
| Mental model predicts reasoning (flowing waters) | Exp 1: 15 of 36 kept; F(1,13)=4.53. Exp 2 N=18: .93 vs .63 (one prediction held, one failed) | Gentner and Gentner 1983 (d04) | single-lab, weak |
| Systematicity helps children only when objects are cross-mapped | About 72 children; Syst x Mapping F(2,136)=3.89; older t(34)=2.48, younger t(34)=1.08 ns | Gentner and Toupin 1986 (a09) | single-lab |
| Cross-mapped pictures: look-alike object chosen until people compare | Control ~65% object match; after similarity rating ~30% object, 70% relational | Markman and Gentner 1993 via Gentner and Kurtz 2006 (a14) | single-lab, second-hand |
| Alignable differences listed more readily | Exp 1: alignable 4.14 vs 3.32, non-alignable 0.62 vs 2.07 (high vs low similarity); 61 of 67 related pairs (91%) were commonality with alignable difference; 1994: similar pairs 11.4 vs 5.9 pairs completed | a15, a16 | single-lab |
| Relation change breaks analogy more than object change | Verb change accepted: synonym .96, near .60, far .14. Noun change: .98, .97, .86. F(2,20)=31.13 interaction | Gentner and Kurtz 2006 (a18) | single-lab |
| Retrieval follows surface; soundness follows structure | Stories recalled 55% on surface match vs 12% on analogical match | Gentner et al. 1993 via Loewenstein 1999 (b21) | second-hand; numbers in subfield 03 |
| Local-to-global time course | At 600 ms, forward and reversed metaphors equally comprehensible; at 1200 ms forward wins | Wolff and Gentner 2011 via Forbus 2017 (a21) | single-lab, second-hand |
| Comparing two cases improves transfer | Meta-analysis 57 experiments: d=.60 (CI .47-.72) at experiment level, .50 at test level; near .52, far .34; I2=59% | Alfieri et al. (d08) | replicated (meta-analysis) |
| Analogical encoding in negotiation | Exp 1 50% vs 19%; Exp 2 contingency contract 48% (13/27) vs 16% (5/31) of dyads; gain about $64,000, t(56)=4.37 | Loewenstein et al. 1999 (b20) | single-lab, one domain |
| Unaided transfer is rare | Radiation problem about 10% unaided, about 85% with analogous story plus hint | Gick and Holyoak via b21 | second-hand |
| Greedy SME matches exhaustive SME | 52 of 56 identical (93%) | Forbus et al. 2017 (d06) | authors' own library |
| SME model on visual oddity | 39 of 45 solved (87%); failures hardest for people | d06 | single-source |
| Exhaustive merge is worst-case O(N!) | One PHINEAS problem 53 min, 34 s after adding systematic structure | a07 | 1989 hardware |
| SMTB faster than SME | Corpus 5,845 pairs: SME 70.95 s, SMTB 5.97 s; large domains 1.80x on SMTB objective, 1.52x on SME objective | d07 | self-reported |
| Rival models also reproduce systematicity effects | ACME failed only on unsystematic cross-mapped case without tuning | a24, a25, b17 | established: data do not single out SME |
| GPT-3 vs humans, digit matrices | OR 1.88 (p=.005, CI 1.21-2.91), humans N=40; multiple choice OR 6.27 | Webb et al. 2023 (c01) | brittle (see below) |
| GPT-3 vs humans, letter strings (standard alphabet) | OR 1.76, p=6.3e-5, humans N=57 | b04 | superseded by counterfactual tests |
| Story analogies (Gentner materials) | GPT-3 near p=.0039, far p=.065 ns; humans N=54, near t(53)=21.5, far t(53)=16.7; GPT-3 vs humans OR=0.37 | b05, c03 | direction replicated (StoryAnalogy, ARN) |
| Counterfactual letter strings | Humans .753; GPT-3 .488; GPT-3.5 .350; GPT-4 .452 (CIs do not overlap); 1,876 human and 6,840 per-model samples | Lewis and Mitchell 2024 (d10) | replicated (Hodel and West, Stevenson) |
| Code execution closes the gap | Humans vs GPT-4: P=8.9e-13; humans vs GPT-4+code: P=0.496; 46% of GPT-4 errors use a valid alternative rule (humans 39%) | Webb et al. 2024 (d09) | single-source, authors' own reply |
| Far-transfer drop in 2024 models | Symbol alphabet: adults .89; Claude-3.5 .46, GPT-4o .48, Llama-405B .27, Gemma-2 27B .14 | Stevenson et al. 2025 (d11) | replicated pattern |
| Permuted relational pairs | Humans unaffected; Claude 3 z=-4.2, GPT-4 z=-4.0, Llama-405B z=-5.5; human cells 15-18 | Musker et al. (b09) | single-source, small human N |
| Story identification (4-way) | Humans 85.7%, best LLM 46.3%, ChatGPT 29.2-35.8% (chance 25%) | StoryAnalogy (c13) | single-source |
| Science analogy mapping (SCAR) | GPT-4 about 73%, best about 77%; humans about 86% (2 raters); one-to-one assignment over embeddings beat max-similarity | Yuan et al. 2023 (b10) | single-source, approximate |
| Long-story analogy | AnaloBench T1 at 1/10/30 sentences: GPT-4 89.1/66.5/60.7; Claude 68.2/30.2/25.9; humans 96.0/72.5/73.3. Retrieval from 200 stories near random | Ye et al. 2024 (d16) | single-source |
| Frontier 2026 models, far analogy | ARCANA pass@3 union: GPT 5.2 48-51%, Gemini 3 Pro 29-43%, Grok 4.1 Fast 19-25%, Claude Opus 4.5 7-9%; humans pass@1 58-69% | Chen et al. 2026 (d13) | single-source, generous to models |
| LLM abstraction plus code mapping | YARN MCQ: Qwen 0.17 without abstraction, 0.46 with (best LLM-only 0.41); Llama 0.16 to 0.45 (LLM-only 0.28); near ARN: CoT 0.79 beats YARN 0.69 | Khojasteh et al. 2026 (d14) | single-source, small open models |
| Code score vs zero-shot | PRISM: 82.5% vs 88.5% on 200 items; 6 vs 18 solo wins, McNemar p=.0227; no role abstraction 24% (chance 25%) | Zeisler et al. 2026 (d15) | single-source, not equal tokens |
| Analogical prompting | GSM8K 75.8 vs 5-shot CoT 75.0; MATH 33.9; Codeforces 13-15% vs 8-11% | Yasunaga et al. 2024 (d18, b24) | contested |
| Relevance not the active ingredient | GPT-3.5 GSM8K relevant 71.5, none 75.5, random-different 76.3; MATH 33.3/36.1/34.1; CSQA 70.8/73.4/72.9; MBPP 58.2/59.8/59.6; GPQA 31.6/34.4/33.1 | Chen et al. 2024 (c12, d17) | contested |
| Decomposition helps Raven-style mapping | GPT-3 Center 77.2 to 80.0; 2x2Grid 87.8; 3x3Grid 93.2; about +20% from component decomposition | Hu et al. 2023 (c10) | single-source |
| LLMs at child level on verbal analogies | 14,006 children, 622 Dutch items; models at 7-11 year level | Stevenson et al. 2024 (c23) | single-source |

## 4. Mechanisms and models

### 4.1 SME, step by step (a03, a04, a19, a20)

Input: two descriptions. Each is a set of typed statements: entities (beaker), attributes (HOT(x)), functions (PRESSURE(x)), and relations (CAUSE(a, b), GREATER(a, b)). Relations can take other relations as arguments. That nesting gives "order".

1. **Match hypotheses (MHs).** For each pair of base and target statements whose predicates match, create an MH. Predicates match if identical, or (SME 4) if they are functions and matching them lets a larger structure match. Also create MHs for their arguments.
2. **Local evidence.** Give each MH a base score (for example 0.5 if the functors are the same, per a04). Weights were chosen by the authors, not fitted.
3. **Structural consistency.** Mark MHs as mutually inconsistent if they break one-to-one (two bases for one target) or parallel connectivity (a statement matches but its arguments do not).
4. **Kernels.** Group MHs into maximal consistent clusters rooted at the top of each matched structure.
5. **Trickle-down.** Pass 80% of a parent MH's belief to its argument MHs (weight 0.8). Entity pairs deep inside a large matched structure end up with high scores. Isolated matches stay low. This is how systematicity is made local.
6. **Merge.** Combine kernels into global mappings (gmaps) that are internally consistent. Exhaustive merge is O(N!) worst case. Greedy merge starts with the best kernel and adds consistent ones; polynomial time; 52 of 56 identical to exhaustive.
7. **Score.** Structural evaluation score (SES) = sum of MH evidence in the gmap. Keep gmaps within 20% of the best, about three.
8. **Candidate inferences.** Base statements linked to matched structure but absent from the target. Score each by support (matched structure backing it) and extrapolation (how far beyond support).

Worked output (a05): solar system to Rutherford atom gave SES 6.03 (nucleus=sun, electron=planet, via the mass inequality; inference "mass difference plus attraction causes revolution"), 4.04 (temperature difference mapped to mass difference), 1.87 (spurious mass swap). In the heat-flow example, isolated relations such as GREATER(diameter(beaker), diameter(vial)) were dropped (a03).

### 4.2 A minimal code scorer for our agent (engineering sketch)

This is our reading of the above, not a published recipe.

- Representation: JSON list of statements, each {id, predicate, args:[ids or entity names], type: entity|attribute|function|relation}. Relation depth is computed by code.
- The model fills the representation for each case. Code validates types and arity.
- The model proposes a mapping: a list of pairs. Code checks one-to-one and parallel connectivity. Violations are returned as a failing output (fits G2: revisions cite real output).
- Code scores: sum over matched statements of local evidence (same predicate 0.5, else a lower value), plus 0.8 x parent score trickled to arguments. Report SES and the fraction of target statements covered.
- Candidate inferences: base statements whose arguments are all mapped but that have no target counterpart. Code lists them. Each is a hypothesis to be checked on the real problem (G3).
- Fallback (from b14, d07): also compute a flat first-order score, so one failed higher-order kernel does not zero every other correspondence.
- Greedy merge is enough for case sizes an LLM can write down (tens of statements).

### 4.3 Alternatives

- **ACME (a24):** a constraint network. Each possible pairing is a unit. Structural, semantic and pragmatic constraints are excitatory or inhibitory links. Iterate to settle. Allows non-identical relations. Needs tuned inhibition.
- **LISA (a25):** role-filler bindings by time-synchrony, with a working-memory cap on active bindings. Predicts mapping gets harder as case size grows.
- **SMTB (b13, d07):** treat mapping as quadratic-assignment-like (NP-hard). Maximise connected relational overlap without a special bonus for higher order. Faster with greedy or limited backtracking (width 3, depth 1-3).
- **AMN (c17):** a graph neural network that imitates SME scores.
- **MAC/FAC (a27):** retrieval. A cheap content-vector scan keeps a few candidates, then SME scores the survivors. Detail is in subfield 03.

### 4.4 LLM hybrids (b12, d14, d15, d13)

Pattern: the LLM turns text into units and abstracts them (roles, relation types); code aligns and scores; the LLM or a check reads the result.
- YARN: split narrative into events, abstract each at one of four levels, map by embedding similarity. Abstraction is the whole gain.
- PRISM: a VLM extracts graphs with semantic roles; code computes a pullback-style relational score with a chain bonus. Removing role abstraction drops the score to chance (24%).
- ConceptSIR (ARCANA): Copycat-style loop with code execution and error-driven mutation; solved 9 of 17 hard tasks in 2.22 loops on average. The authors say it is not general.

The representation step is the weak link (K22). No study reports how well LLM-extracted structure matches human-built structure.

## 5. What holds up

**Holds, with caveats.**
- Direction of the systematicity-selection effect: seen in all three Clement and Gentner experiments, in ratings, choice and free prediction, with a target-only control. But it is one lab, N=32-48; one of three passages failed in Exp 3; two of four passages were non-significant in Exp 2 choice (b02). No independent replication was found (K19). Treat it as a single-lab effect with consistent direction.
- Comparing cases helps learning: the strongest and most independent result in this subfield. d=.50-.60 overall, .34 far transfer (K07). The published moderators (objective, presenting a principle, lag to test; b19) are snippet only. One unverified hint: giving the principle after the comparison helped, and finding only similarities beat similarities plus differences.
- Structural consistency (one-to-one, parallel connectivity) is widely agreed. How central systematicity is, is not (b15, b17).
- LLMs fall on counterfactual and far analogies (K09, K16, K21). Replicated by Hodel and West, Lewis and Mitchell, Stevenson, Musker.

**Weak or failed.**
- Flowing waters is a small, screened sample (15 of 36), and one prediction failed (d04).
- Gentner 1983 core text not read (d05).
- Systematicity in children is conditional and its age interaction is not significant (a09).
- ACME and LISA reproduce the same human effects. The data do not prove SME's mechanism (K06).
- SME's higher-order bias can drop correct local matches (b14). SMTB beats it on its own objective (self-reported, d07). No noise-robustness curve exists (d19).
- The original claim of emergent analogy in GPT-3 (Webb 2023) did not generalise to permuted alphabets (b07, d10). Webb 2024 says it is partly a counting failure (d09). The fix used GPT-4 plus code and does not rescue the far-story result.
- Relevance-based analogical prompting is contested: under 1 point of gain on GSM8K in Yasunaga, a 4-point loss in Chen when the exemplars are relevant (K13).

**Moderators.**
- Object transparency: look-alike objects make mapping easier, cross-mapped ones harder. Relations win at long deadlines; local matches win under 700-1000 ms (a17).
- Base understanding: the effect needs a well-understood base (d03, d04).
- Symbol familiarity: LLMs do worse with unfamiliar alphabets (d10, d11).
- Distance: near analogies work for models, far ones do not (b05, d14, d16).
- Story length: AnaloBench accuracy falls with length for all models, and retrieval from a bank is near random.
- Exemplar correctness matters more than relevance for LLMs: correct-exemplar rates were 62% (relevant), 72% (none), 86% (random same task) (c12).

**Interventions that worked (humans).** Compare two cases before transfer (K07). A similarity rating first moves people from object matches to relational ones (a14). Adding systematic structure to the description cut SME run time from 53 min to 34 s (a07).

**Interventions that did not work.** Labelling the principle added nothing in negotiation Exp 2 (b20). Telling an LLM to recall relevant problems did not beat random ones (c12). Few-shot examples made some newer models worse (GPT-OSS with 2+ examples, d12).

## 6. Language models

**Easy cases pass.** GPT-3 beat 40 students on digit matrices (OR 1.88, p=.005) and 57 on standard-alphabet letter strings (OR 1.76). Four-term word analogies were at or above student level (c04). These need one relation and do not test systematicity. LLMs also match the human error pattern on children's verbal analogies, at roughly 7-11 year level (c23).

**Counterfactual and far cases fail.**
- Lewis and Mitchell (d10): humans .753; GPT-3 .488, GPT-3.5 .350, GPT-4 .452. Later GPT-4 snapshots were no better. Humans were flat across 0-20 permuted letters; GPT falls, with a further drop for symbols. Models pass comprehension checks (c24), so the failure is not misreading. Alternative-valid-rule errors: 38.6% of human errors vs 5.8% (GPT-3) and 22.0% (GPT-4).
- Stevenson et al. (d11), symbol alphabet: Claude-3.5 .46, GPT-4o .48, Llama-405B .27, Gemma-2 .14 vs adults .89.
- Musker et al. (b09): permuted pairs z=-4.0 to -5.5. Default condition not different from humans (GPT-4 p=.097). Prompt wording moved one condition from 20% to 100%.
- Stories (b05): GPT-3 near p=.0039, far p=.065. StoryAnalogy: best LLM 46.3%, ChatGPT 29-36% vs humans 85.7%. Fine-tuned small encoders beat prompted large models. Models generate analogies better than they recognise them (ChatGPT 70-78% judged analogous when generating).
- Long cases: AnaloBench GPT-4 89.1 to 60.7 from 1 to 30 sentences.
- 2026 frontier: ARCANA GPT 5.2 48-51%, Claude Opus 4.5 7-9%, humans 58-69%. Hellwig et al. (d12) report GPT 5.2, Claude Sonnet 4 and GPT-OSS 120B still struggle with some permuted-alphabet transformations, but only in figures. No number was found for a reasoning-model (o1/o3/R1 class) run on the Lewis-Mitchell design.

**What changed the result.**
- Code execution for index conversion: GPT-4 went from far below humans (P=8.9e-13) to no difference (P=0.496). Authors' own reply; the code did counting only (d09).
- Abstraction before mapping: YARN Qwen 0.17 to 0.46; Llama 0.16 to 0.45. Near cases favour plain CoT (0.79 vs 0.69).
- Decomposition: Raven-style sub-tasks about +20% on average; GPT-3 Center 77.2 to 80.0 (c10).
- One-to-one assignment: Kuhn-Munkres over embeddings beat max-similarity on SCAR (b10).
- Code-scored relational score: lost to zero-shot (82.5 vs 88.5) but made different errors (6 vs 18 solo wins, p=.0227). A complement, not a replacement. Without roles, chance (d15).
- Analogical prompting: near zero on GSM8K and MATH. Relevance does not matter (Chen); the correctness of the generated exemplar does.
- Probing (b25, c21): relation information is present in mid-upper layers when the answer is right; failures often mean the relation is not applied to the new entity. Patching hidden states partly fixes it. Abstract-page level only.

**Caveats.** Most studies use GPT-3 to GPT-4 era models. Musker and Stevenson add Claude and Llama-405B. Almost no 2025-2026 reasoning-model number on the counterfactual designs exists. Some human samples are small (15-18 per cell in Musker).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Keep O7 as a scoring heuristic, not a proven mechanism.** [E] K06 (a24, a25, b17). Rival models reproduce the same data. Do not claim SME is the true process. Part: O7.
2. **Keep O7 at impasses and in open mode, not on routine problems.** [E] already in SCHEMA (unaided transfer is rare, b21; distant sources raise spread). This subfield adds that LLM far-analogy accuracy is low (K11, K21). Part: O7, G12.
3. **Use a permuted-symbol regression test on any mapping step.** [E] K09 (d10, d11, b07, b09: several independent groups). LLM mapping that looks fine on familiar surfaces can collapse when symbols are shuffled. The test items belong in the bench, not the schema. Part: G3 (a pass must come from something the answer was not fitted to).
4. **Do not add a free "recall a similar problem" step without an equal-token ablation against random exemplars.** [C] K13 (b24, d17, d18). Consistent with G7. Part: section 4b, G7.
5. **Compare-two-cases is the best-supported learning intervention in humans.** [E for humans] K07 (b18, d08: d=.50-.60, 57 experiments). For LLMs it is untested, so it goes under "Test first", not into the schema. Part: O7, memory.

### Test first

| # | Item | Status | Evidence | Part |
|---|---|---|---|---|
| T1 | Code-scored typed mapping vs free-text mapping vs both, at equal tokens, on permuted-relation tasks | [S] | K10, K20, d09, d15 | O7 |
| T2 | Require relation-first alignment of two worked cases before solving a third | [S for LLM]; human [E] | K07, K01 | O7, memory |
| T3 | Systematicity-based selection among candidate inferences | [S] single-lab | K01, K19, d01-d03 | O7 |
| T4 | Charge relation mismatch more than object mismatch in the scorer | [S] | K18, a18 | O7 |
| T5 | Explicit abstraction of roles before mapping | [S] | K12, K22, d14, d15 | O7, S6 |
| T6 | Flat first-order fallback score next to the higher-order score | [S] argued only | K15, b14, d07, d19 | O7 |
| T7 | Alignable-differences-first in compare steps | [S] | K08, a15, a16 | S4, O7 |
| T8 | Decompose into components before mapping | [S] | K14, c10 | O3 with O7 |
| T9 | Structure-first retrieval of past cases vs embedding retrieval | [C] open | K03, K23, a17, d16 | memory |
| T10 | Code-listed candidate inferences, each checked on the real problem | [S] | a03, a22, K04 | O7, S4 |

Thresholds are in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms use the same model and the same total token budget, setup cost counted (G7). Report per-item solo wins for each arm, not only accuracy.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 permuted relation tasks | Letter-string and symbol-pair analogies with shuffled alphabets, plus a standard-alphabet control | plain; free-text mapping; code-scored mapping; code plus free-text | Accuracy; solo wins; drop from standard to permuted | Plain drops 0.2-0.3 (d10, d11). A mapping arm helps only if it cuts the drop. Expect a small or zero gain with different errors (d15). |
| B2 selection of inferences | Clement-Gentner style: base passage, target passage, two true candidate facts, one in the shared causal system | plain; explicit map-first step; code-scored map | Share choosing the system-linked fact (humans in analogy group .67-.92, controls .42-.54) | Plain LLM may already be near human. Gain only if baseline is below .65. |
| B3 cross-mapped stories | Pairs with look-alike objects in different roles vs object-consistent pairs | plain; typed relation-first map | Accuracy on cross-mapped minus object-consistent | Mapping should help mainly in the cross-mapped case (K02). |
| B4 far vs near story identification | 4-way story pick, near and far, long and short | plain; extract-abstract-then-map; CoT | Accuracy by distance and length | Hybrid wins far, CoT wins near (d14). |
| B5 compare-two-cases | Three-case sets with a shared principle; solve case 3 | two cases separate; two cases with required alignment; alignment plus principle after | Solve rate on case 3; far-transfer case separately | Human d about .5; LLM effect unknown; far smaller (.34). |
| B6 extraction fidelity | 30 hand-built relation graphs from short cases | model extracts graph | Edge precision and recall; downstream mapping accuracy vs hand graph | Shows whether the representation step is the bottleneck (K22). |
| B7 relevance ablation | Impasse problems with a case store | relevant case; random case; no case | Solved rate | Chen suggests no gain from relevance for weak models; test strong ones (K23). |
| B8 retrieval | Same store | embedding top-k; relational-signature top-k; both | Hit rate of structurally right case; solved rate | Humans retrieve by surface (b21); structure-first may help. Links to subfield 03. |
| B9 scorer agreement | 30 hand-built pairs with a human-judged best mapping | nesting-weighted sum scorer | Agreement of top gmap with the human choice | Sanity check that the scorer works at all (K04). |

## 9. What does not transfer, and why

- **Hand-built input.** SME works on predicate descriptions written by people or other programs (a26). Our agent must build them from text. The weak link is extraction, with no measured accuracy (K22).
- **Human selection effect numbers.** The systematicity effect comes from short invented passages read by undergraduates in one lab. It tells us what people prefer, not what is correct. Systematic does not mean true. Both candidate facts in the study were true statements (d01).
- **Human-specific results.** Cross-mapping behaviour in children, response-deadline time courses (600/1200 ms), and the cultural visual-oddity results concern human processing limits. LLMs have no such deadline.
- **Capacity limits (LISA).** Working-memory binding limits do not apply in the same way to a model with a context window.
- **Analogical prompting gains.** The mechanism is not structure mapping. It is recall plus extra sampling. The gain tracks exemplar correctness, not relevance (c12).
- **GPT-3-era results.** Brittleness on permuted alphabets was measured on 2022-2024 models. We do not know the current reasoning-model profile (K21).
- **The 5-15x SMTB speedup and 52 of 56 greedy agreement.** These are compute-cost evidence on SME's own corpus. Our cases are small, so cost is not the problem.
- **Negotiation and education transfer effects (K07).** Human learning from reading two cases is not the same as an LLM using two cases in context. The effect may be stronger, weaker or absent.

## 10. Open questions

1. Does a code-scored typed mapping beat free-text mapping at equal tokens on a current reasoning model? The only direct comparison (PRISM) had the code score lose, 82.5 vs 88.5 (K20).
2. Has anyone independently replicated Clement and Gentner 1991? None found. This may reflect search depth (critique).
3. How do 2025-2026 reasoning models do on counterfactual letter strings and permuted pairs? Only figures, no numbers (K21).
4. How accurate is LLM-extracted relational structure against human-built structure (K22)?
5. Do relevant recalled cases help strong models on non-math tasks? Weak-model evidence says no (K23).
6. Does structure-first retrieval beat embedding retrieval at equal tokens? No study (K23).
7. How robust is a mapping scorer to flat, noisy or wrong representations? No measured curve (d19).
8. What do Gentner's 1983 core experiments show? The scan is unreadable (d05); an OCR copy is needed.
9. How do the Alfieri moderators (objective, principle, lag) apply to LLM in-context use? The published moderator results were not opened (b19).
10. Is systematicity a hard rule? SMTB drops the higher-order bias and wins on its own objective; an independent test is needed.

## 11. Sources

[V] = opened and read in this run. [M] = snippet or abstract only.

- [V] Gentner (1983) Structure-mapping: a theoretical framework for analogy. Only the last pages were readable; core text unverified. https://groups.psych.northwestern.edu/gentner/papers/Gentner83.pdf (a01, a02, d05)
- [V] Gentner and Gentner (1983) Flowing waters or teeming crowds. https://groups.psych.northwestern.edu/gentner/papers/GentnerGentner83.pdf (d04)
- [V] Falkenhainer, Forbus, Gentner (1989) The Structure-Mapping Engine. https://groups.psych.northwestern.edu/gentner/newpdfpapers/FalkenhainerForbusGentner89.pdf (a03-a08)
- [V] Gentner and Toupin (1986) Systematicity and surface similarity. https://groups.psych.northwestern.edu/gentner/papers/GentnerToupin86.pdf (a09, a10)
- [V] Clement and Gentner (1991) Systematicity as a selection constraint. https://groups.psych.northwestern.edu/gentner/papers/ClementGentner91.pdf (a11-a13, b01-b03, d01-d03)
- [V] Markman and Gentner (1993) Splitting the differences. https://groups.psych.northwestern.edu/gentner/papers/MarkmanGentner93b.pdf (a15)
- [V] Gentner and Markman (1997) Structure mapping in analogy and similarity. https://groups.psych.northwestern.edu/gentner/papers/GentnerMarkman97.pdf (a16, a17, a27, b22)
- [V] Gentner and Kurtz (2006) Relations, objects, and the composition of analogies. https://groups.psych.northwestern.edu/gentner/papers/GentnerKurtz06.pdf (a14 gives Markman and Gentner 1993 figures second-hand; a18)
- [V] Forbus, Ferguson, Lovett, Gentner (2017) Extending SME. https://groups.psych.northwestern.edu/gentner/papers/ForbusFergusonLovett&Gentner_2017.pdf (a19-a23, b15-b17, d06)
- [V] Holyoak and Thagard (1989) Analogical mapping by constraint satisfaction. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Holyoak_Thagard.1989.pdf (a24)
- [V] Hummel and Holyoak (1997) LISA. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Hummel-Holyoak.1997.pdf (a25)
- [V] Forbus, Gentner, Markman, Ferguson (1998) Analogy just looks like high level perception. https://www.qrg.northwestern.edu/papers/Files/Analogy_Just_Looks_Like_1998_Gentner.pdf (a26)
- [V] Loewenstein, Thompson, Gentner (1999) Analogical encoding in negotiation. https://groups.psych.northwestern.edu/gentner/papers/LoewensteinThompsonGentner99.pdf (b20, b21)
- [V] Alfieri, Nokes-Malach, Schunn (2011/2013) Learning through case comparisons, 2011 abstract version. https://files.eric.ed.gov/fulltext/ED528947.pdf (b18, d08)
- [M] Alfieri et al. (2013) published moderators. https://www.lrdc.pitt.edu/Schunn/papers/ContrastingCasesMeta-AlfieriEtAl2013.pdf (b19)
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in LLMs. https://arxiv.org/abs/2212.09196 (b04, b05, c01-c04)
- [V] Hodel and West (2023) Response. https://arxiv.org/abs/2308.16118 (b07, c05)
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks. https://arxiv.org/abs/2404.13070 (b08, c06, c25, d09)
- [V] Lewis and Mitchell (2024) Counterfactual tasks. https://arxiv.org/abs/2402.08955 (b06, b27, c07, c24, d10)
- [M] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning, abstract page only. https://arxiv.org/abs/2411.14215 (c08)
- [V] Musker, Duchnowski, Milliere, Pavlick (2025) LLMs as models for analogical reasoning. https://arxiv.org/abs/2406.13803 (b09, c09)
- [V] Stevenson, Pafford, van der Maas, Mitchell (2025) Can LLMs generalize analogy solving. https://arxiv.org/pdf/2411.02348 (d11)
- [V] Stevenson et al. (2024) Do LLMs solve verbal analogies like children do? https://arxiv.org/abs/2310.20384 (c23)
- [V] Hellwig, Zuidema, Stevenson, Lewis (2026) Transformer See, Transformer Do. https://arxiv.org/pdf/2604.06501 (d12; frontier numbers only in figures)
- [V] Chen, Wang, Wang (2026) ARCANA. https://arxiv.org/pdf/2610.29271 (d13)
- [V] Yuan et al. (2023) SCAR. https://arxiv.org/pdf/2305.12660 (b10; table garbled, numbers approximate)
- [M] Jiang et al. (2023) StoryAnalogy. https://arxiv.org/abs/2310.12874 (b11; c13 has the numbers)
- [M] ARN: analogical reasoning on narratives (2023). https://arxiv.org/abs/2310.00996 (c14; prose only)
- [V] Ye et al. (2024) AnaloBench. https://arxiv.org/pdf/2402.12370 (d16)
- [V] Khojasteh et al. (2026) YARN. https://arxiv.org/pdf/2603.29997 (b12, c20, d14)
- [V] Zeisler, Shirekar, Lica, Raman (2026) PRISM. https://arxiv.org/pdf/2610.01383 (d15)
- [V] Weitekamp and MacLellan (2026) SMTB. https://arxiv.org/pdf/2609.25508 (b13, b14, c16, d07, d19)
- [V] Crouse, Nakos, Abdelaziz, Forbus (2020) Neural analogical matching. https://arxiv.org/abs/2004.03573 (c17)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/pdf/2310.01714 (b24, c11, d18)
- [V] Chen et al. (2024) Relevant or random. https://arxiv.org/pdf/2404.12728 (c12, d17)
- [V] Hu, Storks, Lewis, Chai (2023) In-context analogical reasoning. https://arxiv.org/abs/2305.17626 (c10)
- [M] Probing study (2025) The curious case of analogies. https://arxiv.org/abs/2511.20344 (b25, c21; abstract and probing section, no tables)
- [M] Xu, Yan, Zhang (2026) Feature resemblance theory. https://arxiv.org/pdf/2603.05143 (b26; theory only)
- [M] Donvito and Lieto (2026) Minimal Cognitive Grid ranking. https://arxiv.org/abs/2605.01359 (b23, c22; abstract and intro)
- [M] Das and Balke (2025) From prototypical to relational. https://aclanthology.org/2025.inlg-main.28 (c15; snippet, do not cite for numbers)
- [M] Gentner and Forbus (2025) SME review. https://groups.psych.northwestern.edu/gentner/papers/GentnerForbus-2025-SME.pdf (c18; snippet)
- [M] Blass and Forbus (2016) Analogical chaining in Companions. https://www.qrg.northwestern.edu/papers/Files/AQR_Companions_final_v3.pdf (c19; snippet)
- Second-hand only (not opened): Gick and Holyoak radiation problem (via b21); Wolff and Gentner 2011 (via a21); Gentner et al. 1993 Karla the Hawk (via a17, b21); Chalmers, French, Hofstadter 1992 (via a26).
