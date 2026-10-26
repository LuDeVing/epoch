# Analogy and categorisation research: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl. "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap (section 7). Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most human numbers come from one research tradition (Gick and Holyoak, Gentner and colleagues) and were seen in restatements or abstracts; most LLM numbers are from 2023-25 models and the authors' own benchmarks. Read every row as a design hint to test on our model (section 5), not as proof.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 Analogical access (retrieval) | [DEEP](subfields/03_analogical_access/DEEP.md) | 27 | 12 |
| 04 Schema induction | [DEEP](subfields/04_schema_induction/DEEP.md) | 33 | 10 |
| **Total** | | **60** | **22** |

Contested claims: 10 (03: 4, 04: 6). Single-source claims: 28 (03: 11, 04: 17). Each subfield has a UNKNOWNS.md with 15 test rows (30 in all).

**Not yet researched** (from SUBFIELDS.md): structure mapping and its scoring; analogical inference; connectionist and hybrid mapping models (ACME, LISA, Copycat); logic and philosophy of analogical arguments; category learning (rule, prototype, exemplar); category learning (clustering, explanation-based, Bayesian); comparison and relational language. Seven of the nine listed topics have no DEEP.md. The mapping step of O7 (how a mapping is built and scored) is the biggest hole; both researched subfields lean on it without studying it.

## 2. Established findings, merged

For the agent, "yes" means SCHEMA.md already has the element. Many rows are human results.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | People often fail to use a studied analogue unaided (about 20 to 30% on the radiation problem, about 10% with no source) and reach about 75 to 80% after a plain hint. The failure is access, not storage or mapping. Business replications show a weaker, problem-dependent hint effect. The no-hint rate ranges 10 to 43% by experiment. | A11.03-K01 | G1, S6 | partly (O7 says unaided analogy rarely transfers [E]; S6 fires on an impasse signal; no rule that a stored case is surfaced at S6) |
| F2 | Retrieval follows shared objects and surface content, not relational structure (reminding: literal .56, surface .53, analogy .12, relations-only .09). Embedding lookup anchors on wording: on paraphrases the right item is usually in the top 10 and almost never first (hard tier Hit@1 0.0%). Reasoning-heavy retrieval benchmarks show the same weakness. | A11.03-K02, A11.03-K07 | memory | partly (section 5 plans a subgoal library "offered by similarity"; no warning that similarity is surface) |
| F3 | Retrieve-then-rerank closes part of the gap, but the gain depends on the judge and domain. Deeper reranking did not reliably pay. A naive lexical or web-trained reranker can hurt. | A11.03-K08 | memory | no |
| F4 | Choosing few-shot exemplars by structure beats choosing by text embedding in maths (all four sizes 0.5B to 72B), and gains shrink as models grow. Inside agent loops, memory built from past trajectories helps, and the retrieval key changes the result (task-similarity key 59.0 vs reasoning-step key 48.5 vs random 42.5 on ALFWorld). | A11.03-K09, A11.03-K15 | memory | no |
| F5 | Rewriting the probe before lookup works without training (reasoning-step queries lifted BRIGHT retrieval by up to 12.2 points; a problem distiller helps template lookup). The evidence is for answer-like and element-and-constraint rewrites, not relation restating specifically. | A11.03-K23 | memory, S1 | partly (S1 restates the task for solving, not as a lookup query) |
| F6 | Loosened retrieval causes false transfer, and "ignore it if it does not fit" does not stop it. A forced approximate top-1 cut success 16.7 to 11.4%; all 50 skills in context gave 11.4% vs 28.1% with none; a progress-blind text key took WebShop 31.0 to 18.4. | A11.03-K20 | G7, memory | partly (G7 says the schema must pay; O7 mapping step is [S]; no no-match outcome) |
| F7 | Showing a decoy and a structural match side by side does not fix it for 2023-era models: far analogy vs near decoy 29.1% (chance 50), and a decoy that reverses cause and effect cut GPT-4 from 95.5 to 83.2%. People stayed at 96 to 100%. | A11.03-K19 | S6, G7 | partly (O7 [E] note; mapping step [S]) |
| F8 | Comparing two analogous cases and stating what they share raises unaided transfer (45 vs 21%, 47 vs 16%, 48 vs 19%; meta-analytic d about .50 across 57 experiments, abstract only). | A11.03-K04, A11.04-K01 | S2, memory | partly (S2 already says study how examples differ; no forced "state what they share" step) |
| F9 | Comparison works only when it is effortful, aligned and directed. Listed correspondences and directive questions beat bare comparison (90% vs 70% vs 55% separate vs 37% baseline; good schemas 26% to 86% with questions). Only 16 to 18% of separate-case learners linked the cases, vs 88 to 100% of comparers. Teams did no better than solo. | A11.04-K08, A11.04-K22 | S2 | no |
| F10 | Even with comparison, most people do not transfer unaided in most lab conditions (40 to 48%); 70 to 90% needs heavy scaffolding. Schema quality predicts transfer, but only as a correlation in small samples. | A11.04-K02, A11.04-K05 | G7, S2 | partly (G7 and G3 cover "do not assume it is used"; no rule-quality check) |
| F11 | A stated principle added to one analogue adds nothing (about 30%); added to a pair it helps (62 vs 40% noticing). Static diagrams or a principle alone do not raise access from one source. | A11.03-K17 | S2, O7 | no |
| F12 | Write-time abstraction of solved cases beats storing raw cases: abstract workflows over retrieved examples (+5.0 element accuracy), a matched parameterised skill 49.3 vs 41.0%. Stores of abstractions built from solved tasks raise same-family accuracy (Buffer of Thoughts, AWM, ReasoningBank, ExpeL), but only when a manager updates them, and the benchmarks are the authors' own and in-family. | A11.03-K24, A11.04-K13 | memory | partly (section 5 lists a planned subgoal library [D]; lessons are one line, not abstractions) |
| F13 | Memory form ladder: curated, runnable routines and distilled strategies beat raw reuse (WebArena: none 40.5, raw 42.1, workflows 44.1, strategies 48.8; Game of 24: raw retrieval 6 vs curated code-based memory 93 to 99 vs baseline 10). Part of each gain comes from other changes. | A11.04-K31 | memory | no |
| F14 | For models, a few cases are enough and more can hurt: K=1 worst, K=3 to 5 stable for self-generated exemplars; best retrieved agent memory count was 1 and success fell with 4. | A11.04-K28 | S2, memory | no |
| F15 | Abstraction is rarely the failing step. After step-back, over 90% of errors are in reasoning; Self-Discover finds 87.5% of structures correct, 74.7% of failures in computation. | A11.04-K11 | G2, S4 | no |
| F16 | Surface changes hurt models unevenly (digit matrices 0.813 original, 0.790 with symbols, 0.480 with the blank moved; story analogies 89% when the right answer is first, 61% second; o1-preview lost 17.5 points to one irrelevant clause). | A11.04-K30 | G3, S1 | partly (G3 mutated input; S1 input hygiene) |

## 3. Contradictions between subfields

| # | Where they disagree | How to resolve |
|---|---|---|
| C1 | **Does memory help or hurt?** Helps: A11.03-K15, A11.03-K24, A11.04-K13, A11.04-K31. Hurts: A11.03-K20 (forced top-1, all skills in context, progress-blind key), and raw retrieval at 6 vs baseline 10 on Game of 24 (A11.04-K31). | Not a real conflict: curated, abstracted, gated memory helps; raw or loosely keyed memory hurts. Build the no-match gate first (T3), then test memory form (T5). |
| C2 | **Can people judge what they cannot retrieve?** A11.03-K03 (single-source) says people rate structural matches as most sound while failing to retrieve them. A11.03-K19 (established) says 2023-era LLMs fail the side-by-side choice too. | The human split between good judgement and poor retrieval is not the LLM pattern. Do not rely on "show both and let the model pick" (T3). |
| C3 | **Do separate cases help?** A11.04-K03 (contested): 22 vs 23% baseline in one study, 55 vs 37% in another. A11.03-K04 and A11.04-K01 treat comparison as the active ingredient. | Keep the comparison step as the unit of test; include a "cases summarised separately" arm (T4). |
| C4 | **How weak is "passes the shown examples"?** A11.04-K20 (contested): 45.4% of train-passing list-function programs fail ground truth; ARC rules that passed almost always passed the test. A01 F11 (A01.09-K22): about 9% of train-fitting ARC samples fail. | Domain and example count decide it. Keep SCHEMA G3 (unfitted check) regardless; do not weaken it on the ARC result. |
| C5 | **Do prompt scaffolds help a reasoning-trained model?** Gains reported for step-back, Self-Discover, analogical prompting, LEAP on older models (A11.04-K10, A11.04-K23, A11.03-K10, A11.04-K27). Against: A11.04-K24 (about +3 or less on o3-mini, o4-mini), A11.03-K26 (R1 degrades with few-shot, no numbers; ThinkRetrieve gain falls from +10 at 1.7B to +1 to 3 at 8B), A11.03-K11 (single-source: relevance of self-made exemplars is not the driver). Same tension as A01 C2 and A02 T13. | No frontier-model test exists in this field. Run terse-reasoning plain as the control (T7, T9) and keep a step only if it beats it at equal tokens (G7). |
| C6 | **Is abstraction a bottleneck?** A11.04-K10 (single-source) says step-back gives large gains on principle-recall tasks. A11.04-K11 (established) says abstraction is rarely the failing step and most errors come after it. | Compatible: gains appear where recall of a principle is the need, errors elsewhere are in execution. Gate abstraction by class (T2, T7) and spend checking tokens on execution. |
| C7 | **How firm is the hint effect for people?** A02 synthesis (A02.04-K06) puts "analogy transfer depends on noticing, hint vs no hint" at single-lab status. A11.03-K01 lists it as established with 3 sources, but the sources are the Gick and Holyoak line plus weaker business-problem replications and restatements. | Treat A11.03-K01 as one tradition with partial replication. It supports a failure-triggered cue as a design hint only. |
| C8 | **Where to insert a retrieved case.** SCHEMA section 5 shows lessons after the first attempt. A11.03-K21 (single-source) found retrieval at mid-trace boundaries gave gains while start-only gave none (88.80 vs 89.07). A02 T10 tests attempt-first vs retrieve-first. | Open. Test with T2 (arm: case at S5 vs S3). Until then keep SCHEMA section 5. |
| C9 | **Does a dissimilar pair help?** A11.04-K06 (single-source): dissimilar trended better (39 vs 52%, not significant). A11.03-K02 says surface overlap drives retrieval, which favours similar pairs for access. | Different stages (induction vs retrieval). Test pair type only after the comparison step is shown to work (T4). |
| C10 | **Judge a model-written rule by wording or by running it?** A11.04-K29 (contested): running is best. A11.04-K05 (established, human): rule quality predicts transfer. | Humans were graded by people; for models only running is shown to work. Keep code-run checks (G3); log judged quality as a side test (T8). |

## 4. Recurring mechanisms

| Mechanism | Subfields and claims | What it means for the agent |
|---|---|---|
| **Surface wins at retrieval time** | 03 (A11.03-K02, K07, K19, K20); 04 (A11.04-K30; single-source K07, K18) | Lookup by wording returns the lexical neighbour, not the structural match. Key the memory by relation tags and rewrite the probe first; never trust top-1 alone (T1, T3). |
| **Comparison builds the schema** | 03 (A11.03-K04, K17); 04 (A11.04-K01, K08, K22; single-source 03-K05, 04-K26) | Two cases, forced alignment, a stated shared structure. One case or a free summary is much weaker. Gate by step cost (T4). |
| **Abstract at write time, curate the store** | 03 (A11.03-K24); 04 (A11.04-K13, K31) | Store parameterised routines or distilled strategies, written only after a G3 pass, not raw trajectories (T5). |
| **Loosened retrieval means false transfer** | 03 (A11.03-K20, K19); 04 (single-source K18) | A no-match outcome and a mapping check before using any retrieved case (T3). |
| **Few cases, directed use** | 04 (A11.04-K28, K22, K02); 03 (A11.03-K17) | Cap at 2 to 3. Directive output beats open reading. Do not assume the rule will be used unaided. |
| **Extra prompting shrinks as models strengthen** | 03 (A11.03-K09; single-source K21, K26); 04 (single-source K10, K24, K25, K33) | Every scaffold step needs a terse-reasoning control at equal tokens (G7, T7). |
| **Errors sit after abstraction** | 04 (A11.04-K11; single-source K12, K20) | Check execution, not the abstract step. Keep the plain answer as a candidate next to the abstracted one (T7). |

## 5. Merged tests

All tests: same base model in every arm, equal total tokens (counting tagging, restating, lookup, mapping and write passes), paired items, flips right-to-wrong and wrong-to-right logged. "Memory" is a store of the agent's own solved, G3-checked subgoals. Most tests need a store built from passed runs; log every G3-passed subgoal with its abstract form and tags from the first bench run (SCHEMA section 6).

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1. Probe rewrite and structure key | A11.03-U1, A11.03-U3, A11.03-U10, A11.04-U10 | On a paraphrase set with a lexical decoy, compare raw probe, free restatement and relation-tag abstraction for Hit@1 and Hit@5; then tag key vs embedding top-3 inside the loop; check tag consistency over 5 writes. | High |
| T2. Retrieval trigger and gate | A11.03-U2, A11.03-U9, A11.03-U11, A11.03-U12, A11.04-U3 | Arms: none, always-on at S3, lookup only when S6 fires, one case at S5; split by class pass-rate band; vary memory size and rerank depth; also gate induction by pass rate. Accuracy per token. | High |
| T3. No-match gate and mapping check | A11.03-U4, A11.03-U7, A11.03-U15 | Items with 40%+ no analogue and a decoy. Arms: forced top-1, no-match option, no-match plus code-checked one-to-one mapping; count decoy use and loss vs none. Include a no-mapping arm for current models. | High |
| T4. Forced two-case comparison | A11.04-U1, A11.04-U5, A11.04-U9 | Plain, 1 case, 2 cases free, 2 cases with correspondence list, 2 cases summarised separately, self-made K=3; also principle before/after and pair type; new surface form, several classes. | High |
| T5. Memory form and write-time abstraction | A11.03-U5, A11.03-U14, A11.04-U7, A11.04-U8, A11.04-U11 | Raw cases vs single-case abstraction vs two-case schema vs code-built routines vs model templates (plus near-miss and per-class structure arms); write gated by G3 vs self-grade; held-out class to detect leakage. | High |
| T6. Sibling problem | A11.03-U6, A11.04-U6 | Write a sibling problem with the same structure, solve both under one shared-strategy instruction, vs target alone vs 2-sample vote; also use the sibling schema as the lookup probe. | Med |
| T7. Abstraction step vs terse plain | A11.04-U2, A11.04-U4, A11.04-U14, A11.04-U15 | Terse plain (about 40 tokens a step) vs step-back vs abstract-then-concrete vs contrast lesson; plain answer kept as a second candidate selected by check; log flips. | High |
| T8. Test raw rules before summarising | A11.04-U12, A11.04-U13 | Summarise-first vs test-all-raw on ARC items; log judged rule quality next to held-out result. | Med |
| T9. Vetted exemplar bank vs self-recall | A11.03-U8 | 0-shot vs self-recall K=3 vs fixed bank of 5 vetted examples, easy and hard items. | Med |
| T10. Distant grounding in open mode | A11.03-U13 | NoveltyBench-type items: no grounding vs surface-near vs domain-masked distant analogues; distinct answers vs quality. | Med |

Run order (from the subfields): T1 offline Hit@1 first (cheapest, needs no solving), then T3, then T2 with T1's tag-key arm on the same store. Then T4 and T7, then T5.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Showing a retrieved case next to a decoy and letting the model choose | 2023-era models pick the decoy; the human judgement-over-retrieval gap does not carry over | A11.03-K19 |
| Retrieving a forced top-1, or dumping the whole store into context | Forced approximate hints and full dumps lowered success below no memory; "ignore if it does not fit" did not help | A11.03-K20 |
| Lookup by plain text embedding or wording as the only key | Top-1 almost never right on paraphrases; the lexical winner is picked in 95 to 99.8% of misses | A11.03-K07 |
| A lexical or web-trained reranker on analogue or math retrieval | Naive lexical reranker hurt math; web-trained cross-encoder fell below BM25 on BRIGHT | A11.03-K08 |
| Storing raw trajectories or raw solved cases as the memory | Abstracted, curated routines beat them; raw retrieval did worse than baseline on Game of 24 | A11.03-K24, A11.04-K31 |
| Using the agent's own reflections as stored insights | Insights from success-failure pairs need real experience and were worse with the agent's own reflections added | A11.03-K24 |
| Validating the abstraction step with extra tokens | Over 90% of step-back errors, and 74.7% of Self-Discover failures, come after abstraction | A11.04-K11 |
| More than 2 to 3 cases in a comparison or exemplar set | K=1 is worst; K=3 to 5 stable; 4 retrieved experiences lowered success | A11.04-K28 |
| Comparison without a directed, aligned output | Only 16 to 18% of separate-case learners linked the cases; bare comparison trails guided | A11.04-K22, A11.04-K08 |
| Assuming a derived schema will be applied unaided | Even after comparison, 40 to 48% transfer in most lab conditions | A11.04-K02 |
| Presenting a principle with one analogue | No gain; helps only with a pair | A11.03-K17 |

## 7. Gaps

- **Single-source or contested but tempting.** Do not add until tested: comparison at retrieval time (A11.03-K05); two-stage MAC/FAC as the best retriever (A11.03-K06, contested); self-generated analogues (A11.03-K10 contested, K11, K12); mid-trace retrieval (A11.03-K21); failure-triggered cue vs always-on (A11.03-K22); retrieval depth and memory size (A11.03-K25); principle after comparison (A11.04-K04); step-back, Self-Discover, AoT, Chain of Draft and LEAP (A11.04-K10, K12, K15, K16, K23, K24, K25, K27); near-miss contrast cases (A11.04-K21); sibling-problem comparison (A11.04-K26); skipping induction when the plain pass rate is high (A11.04-K33, a design inference).
- **Primary human sources unread.** Gick and Holyoak 1980/1983, Holyoak and Koh 1987, Novick and Holyoak 1991, Catrambone and Holyoak 1989 and the Alfieri 2013 moderators were seen only in restatements or abstracts. Replication status is thin (A11.04-K32).
- **No frontier-model data** on access, analogical prompting or induction scaffolds. All LLM results are 2023 to 2025 models with the authors' benchmarks, and none is equal-token.
- **Untested combinations.** Nobody compared a zero-training structural key with an embedding key at equal tokens in a loop (A11.03-K15); nobody tested the full recipe of two cases, forced alignment, derived rule and new instance on a model (A11.04-K27); nobody compared writing a two-case schema with read-time sibling comparison (A11.03-K24); tag consistency across writes was never measured (A11.03-K27).
- **Seven subfields unresearched** (section 1), especially structure mapping and mapping scores (SME, ACME, LISA), analogical inference, and category learning. The S0 gate's problem classes could draw on category learning.
- **Leakage.** Buffer of Thoughts, AWM and ReasoningBank gains are in-family; held-out class tests are ours to build.
- **Recent 2025 to 2026 literature** was only partly covered because search quotas ran out; absence of a paper means not found.
