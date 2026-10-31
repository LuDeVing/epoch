# Case representation: deep document

*Subfield C08.04, what a case stores: problem, solution, outcome. Built from evidence_a-d.jsonl (a01-a38, b01-b27, c01-c35, d01-d17), claims.jsonl (K01-K31) and critique.md in this folder. Links to the 4R cycle (retrieve, reuse, revise, retain) are in `../01_the_4r_cycle`. Not covered here: impasse-driven chunking, structure mapping, self-consistency, scoring rules, debugging strategies and the other parallel subfields; they are only noted where a link exists.*

## 1. What it is

A case is a record of one experience that can be reused later. In classic case-based reasoning (CBR) a case holds three things. The problem (the situation and its features). The solution (what was done). The outcome (what happened, including failure). Many designs add a fourth: an explanation of why the solution worked or failed, and metadata such as time, source and conditions.

Case representation is three linked choices (Aamodt and Plaza 1994, a06): what to put in a case, how to structure the content, and how to organise and index the case memory. For our agent this is the design of the S9 record: which fields, in what shape, with which retrieval labels, and which records are allowed in.

The LLM-agent literature has converged on the same core under different names:

| Source | Case form | Ids |
|---|---|---|
| Kolodner / Aamodt-Plaza | problem descriptors + solution + outcome + explanation | a01, a07 |
| Memento (2025) | (state, action, reward) = task, plan, success flag | a14, b01, c20 |
| Hatalis et al. review (2025) | (P, S, O, M) = problem, solution, outcome, metadata | a37, c31 |
| CBR-RAG (2024) | (Q, S, E, A) = question, support text, entities, answer | a24, c06 |
| ReasoningBank (2025) | title + one-sentence description + 1-3 sentence strategy | a19, b21, c17 |
| TextBFGS (2026) | pre-edit text, error description, abstract fix rule, post-edit text | c27 |
| Springdrift (2026) | problem-solution-outcome + Laplace utility score | c29 |
| Agent KB (2025) | task embedding, goal-constraint predicates, action-reasoning pairs, metadata | b24 |
| Evo-Memory ExpRAG (2025) | (input, output, feedback) | b26, d13 |

Key point for the agent: no LLM study ablates the individual fields (K21, K30). We know whole designs, not which field earns its tokens.

## 2. History and theories in depth

**Schank and Kolodner: dynamic memory.** CBR grew out of Schank's dynamic memory work (CYRUS and relatives). Memory is a tree of generalised episodes. Each node holds norms (features shared by its cases), the cases, and indices (features that tell cases apart). If two cases share an index, a new generalised episode is made to separate them (Aamodt and Plaza, a08). Memory reorganises itself as cases arrive.

**Kolodner 1993: the indexing problem.** Kolodner (a01-a05) says memory has two parts: putting cases in and recalling them. She calls this the indexing problem and splits it in two. At store time, label each experience with when it will be useful (anticipation). At recall time, elaborate the new situation until it carries the labels it would have had (assessment). Three more rules from the same editorial:
- Failures are worth storing, indexed so the failure is recognised before it recurs. If a repair is found, store it inside the case (a03).
- Cases can be re-indexed after use. A recalled case that proved wrong loses the label that fetched it. A missed case gains the missing label (a04).
- Admission is controlled. A case belongs only if it lets the system do something it could not, or do it faster (a05).
This is a position paper. It has no experiments and no numbers.

**Porter and Bareiss: category-exemplar model (PROTOS).** Cases are exemplars of categories. Three link types: remindings (feature to case or category), exemplar links (category to cases, ordered by prototypicality) and difference links (a09). Retrieval is a path through a category graph, not a flat search.

**Aamodt and Plaza 1994: the 4R cycle and the retain step.** Retrieve, reuse, revise, retain. Retain (a10) decides what to extract (descriptors, solution, explanation, solving method), how to index, and how to integrate. Failures from revise can be kept as a way to avoid a past mistake. Index selection is a knowledge-acquisition problem (a11). The trivial answer is to index on all input features. CASEY indexes in two steps: causal states first, then the rest. CASEY keeps all observed features plus a causal explanation of the diagnosis (a07).

**Aha, Kibler and Albert 1991: instance-based learning.** The only classic numeric base in this set (a12, a13). IB1 stores everything. IB2 stores only what IB1 misclassified. IB3 adds a success record per stored instance and drops cases that do badly. This is the origin of admission control and utility eviction in later LLM work (Xiong, Springdrift).

**Watson 2024 and Hatalis 2025: the bridge to LLMs.** Watson (c32) argues for a case base as persistent LLM memory and notes that 1990s case bases were small (a travel base of 1,100 cases) while million-case bases appeared only in the 2010s. Hatalis et al. (a37) give the (P, S, O, M) tuple and propose dense plus sparse indices. Neither reports measurements. Feng et al. (a38, c33) propose case repositories for alignment: a seed question, expert-defined dimensions, LLM variations; no accuracy numbers.

**The LLM turn (2023-2026).** Four design families:
1. Whole trajectories as exemplars (Synapse, ExpeL retrieval).
2. Reusable sub-routines from successes (AWM).
3. Distilled strategy items from successes and failures (ReasoningBank, Dynamic Cheatsheet, Buffer of Thoughts, ACE).
4. Mixed stores that keep both case and lesson (ExpeL, Memp, Agent KB).
The live dispute is abstract versus concrete (K03, K04, K22).

## 3. Core findings with exact numbers

Status: established / single-source / contested, as in claims.jsonl. Numbers marked (cross-checked) were re-read from the full text in the critique pass.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Case = problem + solution + outcome (+ why) is the shared core | 4 independent lines of source | Kolodner, Aamodt-Plaza, Memento, Hatalis (a01, a07, a14, a37) | established (K01) |
| Strategy-level items beat raw trajectories and workflows | WebArena, Gemini-2.5-flash, 684 tasks: no memory 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8 (cross-checked). Gains over no memory +8.3 / +7.2 / +4.6 (flash / pro / Claude-3.7) | ReasoningBank (a20, d05) | established (K03) |
| Abstract workflow beats concrete exemplars on Mind2Web | AWM gpt-3.5 element acc 39.0 vs Synapse 34.0 (+5.0); step SR 34.6 vs 30.6 (+4.0). WebArena 23.5 to 35.5 (+12.0 abs, +51.1% rel), 812 tasks, GPT-4 | AWM (b05, b06) | established (K03) |
| Curated short memory beats full history | AIME 2024 Sonnet: 23.3 base, 26.7 full history, 50.0 Dynamic Cheatsheet. GPT-4o 20.0, 13.3, 40.0. AIME 2025 Sonnet 6.7 / 6.7 / 36.7. GPQA Sonnet 59.6 / 63.6 (verbatim retrieval) / 68.7 | Dynamic Cheatsheet (a36, b19) | established (K03) |
| Concrete beats abstract on some tasks | ExpeL success, insights-only vs retrieval-only: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38. DS-Agent: paired (task, script) cases above text insights on nearly all 18 tasks (bars only, no averages) | ExpeL, DS-Agent (a30, c02) | contested (K04) |
| Both together beat either | Memp GPT-4o ALFWorld test: none 42.14, script 56.43, trajectory 74.29, both 77.86. Qwen2.5-72B 41.25 / 61.88 / 69.57 / 77.19. Claude on TravelPlanner is an exception | Memp (d10) | single-source (K22) |
| Failures help only if the format can use them | WebArena Shopping: ReasoningBank 46.5 to 49.7; Synapse 40.6 to 41.7; AWM 44.4 to 42.2. CER whole WebArena: success-only 33.5 vs success+failure 31.4 | ReasoningBank (a21), CER (d16) | established (K02), with CER as a counterpoint |
| Few retrieved cases is enough | Memento DeepResearcher avg F1/PM: K=0 59.9/72.2; K=1 63.6/77.9; K=4 64.5/78.5; K=32 63.9/78.1 (cross-checked). ReasoningBank Shopping: 1 item 49.7, 2 46.5, 3 45.5, 4 44.4, none 39.0. DS-Agent: performance falls as cases rise | a15, a22, c03 | established (K05) |
| Case memory gain shrinks over passes | Memento accuracy iter 1 to 5: no CBR 78.65, 80.93, 82.62, 83.53, 84.47; parametric 80.46 to 85.44; non-parametric 79.84 to 84.85. Gap about 1.8 down to 1.0 (cross-checked). Bank saturates near 3k items | Memento (a17, b03) | single-source (K06) |
| CBR adds on top of planning | DeepResearcher +6.7 F1 / +8.2 PM; HLE 22.2/17.4 to 26.7/24.4; SimpleQA 81.0/89.7 to 84.7/95.0. Out-of-distribution +4.7 to 9.6. Tools alone -18.0 F1 / -2.1 PM; planning +29.1 / +11.5. GAIA val 87.88, test 79.40 | Memento (a16, a18, b04, c22) | single-source (K06) |
| Agents copy retrieved cases (experience-following) | Output similarity tracks input similarity, Pearson r near 1 at high input similarity, four agents | Xiong (a33, b14) | established (K07) |
| Add-all is worse than a small fixed bank; a strict filter wins | Fixed / add-all / strict: RegAgent 67.53 / 55.48 / 70.95; EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40 (cross-checked). Coarse judges C1-C3 land between, sometimes below fixed | Xiong (a33, a34, d01) | established (K08) |
| Utility-based deletion helps with a reliable evaluator | Strict addition, EHR/AgentDriver/CIC-IoT: no deletion 38.67/51.00/85.40 at 1012/1178/904 records; history-based 42.06/51.81/89.60 at 784/846/788; combined 42.34/49.97/85.50 at 248/323/188. Noisy judge: unreliable | Xiong (b16, d03) | established (K09) |
| Outcome-label accuracy needed is disputed | ReasoningBank judge 72.7% accurate; success 47.6-50.6 across simulated judge accuracy 100 to 50% vs 39.0 none (read from a plot). ACE FiNER: base 70.7, clean 78.3, harmful update every 5 steps 76.1, every step 66.7. DeMem LoCoMo 91.1 / 90.2 / 88.9 at 0 / 10 / 20% flipped | a23, d04, d06, d17 | contested (K10, K24) |
| Error-keyed index transfers; problem-keyed does not | TextBFGS cross-domain MBPP Plus: error-keyed 74.36 vs problem-keyed 58.12, baseline 48.72. HumanEval-Hard cross-domain 97.78 vs 95.56. In-domain problem-keyed slightly better (97.56 vs 96.34). Small sets (about 45 items) | TextBFGS (c27, c28) | single-source (K11) |
| Masked skeleton retrieval beats plain RAG | MIMICSQL exec acc 0.894 vs 0.860; EHRSQL 0.895 vs 0.818. With under 10% training data the EHRSQL gap grows to 11.9 and 10.2 points | CBR-to-SQL (c30) | single-source |
| Multi-part case retrieval, small gain | CBR-RAG cosine 0.9141 vs 0.8967 no retrieval (+1.94%), p<0.05 one-tailed, 32 test cases, 2,124 pairs (1,183 = 57% had no act reference) (cross-checked) | CBR-RAG (a25, a26, c07) | single-source (K12) |
| Retrieval key matters less than having memory | Memp TravelPlanner commonsense, GPT-4o: none 71.93, random 74.59, query key 73.38, keyword key 76.02. Claude-3.5 63.49 / 63.99 / 64.93 / 65.76. Qwen2.5-72B 56.57 / 59.76 / 61.71 / 63.41 | Memp (d11) | single-source (K23) |
| Retrieved workflow must be adapted | Agent KB GAIA pass@1 (GPT-4.1): baseline 55.15; full 61.21; raw workflow 58.18; without Refine 55.15; without Retrieve 57.58; without Reason 60.00 | Agent KB (b24, d14) | single-source (K29) |
| Repeated trials improve the stored lesson | ReasoningBank Shopping parallel k=1 49.7 to k=5 55.1; sequential 49.7 to 54.5; without memory 39.0 to 42.2 parallel, 37.4 to 40 sequential | ReasoningBank MaTTS (c19) | established (K17) |
| Memory and sampling look complementary | CER Forum: sampling+rerank 43.1, memory 37.7, both 52.6. Sampling used more tokens | CER (d16) | single-source (K25) |
| Own successful runs lift the agent | gpt-4o-mini ALFWorld 0.73 to 0.89 (0.91 to 0.93 with curation, by variant); SQL 0.75 to 0.79 (0.81 with exemplar curation); Wordcraft 0.55 to 0.64. After 3,500 tasks ALFWorld +20 vs +15 from upgrading to gpt-4o | Sarukkai (b12, b13, c25) | single-source (K16) |
| Short verbal lesson after failure | Reflexion ALFWorld 130 of 134; HotpotQA self-reflection +8 abs over most-recent-trajectory memory; HumanEval pass@1 91 vs 80 | Reflexion (b11, c35) | single-source (K18) |
| Gain depends on task similarity | Evo-Memory gain vs within-dataset similarity r = 0.717 (Gemini-2.5-flash), 0.563 (Claude-3.7); small gains on AIME-25 and GPQA. ALFWorld steps 22.6 to 11.5 | Evo-Memory (b26, d13) | single-source (K26) |
| Gain vs model size is unclear | ReasoningBank +8.3 / +7.2 / +4.6. Haiku AIME 2024 10.0 to 36.7 but AIME 2025 only to 13.3. QwQ-32B WebWalkerQA 27.5 to 25.5. Qwen3-32B AIME 29.1/19.5 to 33.5/25.4. GPT-4o memory raised Qwen2.5-14B task completion 5% | b20, d05, d12, d15 | contested (K19, K27) |
| Planted/misleading cases are followed | MINJA injection above 95%; attack success above 70% in half the configurations, above 90% for GPT-4 on eICU and GPT-4o on WebShop. AgentPoison about 80% attack success at under 0.1% poison, about 1% or less benign loss | MINJA, AgentPoison (d08, d09) | established (K28) |
| IB2 vs IB3 admission | Stored %: IB2 7.5-71%. 26.3% of IB2's stored instances noisy at 10% attribute noise. Hungarian IB1 58.7, IB2 55.9 (36.0% stored), IB3 80.5 (7.5% stored), C4 78.2. Voting IB1 91.8 (100%), IB3 91.6 (7.4%), C4 95.5 | Aha 1991 (a12, a13) | single-source (K15) |
| Models match cases, not rules | Leave-square-out: 100% on random split, accuracy collapses inside the held-out region; rule-following fine-tuning repairs digit-length generalisation (Llama-2-7B, 6 to 9 digit addition) | Hu et al. (c08, c09) | single-source (K14) |
| Mixed memory formats (documents) | Iterative retrieval mixed memory HotpotQA F1 82.11, 2Wiki 68.15; no single format wins | Zeng et al. (b18) | single-source (K13) |
| Bank size is small in LLM agents | Memento saturates near 3k; Agent KB 100 examples useful, 500 better on code; Xiong caps of 100 and 180 beat a frozen bank | a17, d03, d14 | contested (K20, K31) |

## 4. Mechanisms and models

This section is written so an engineer can build an S9 store.

### 4.1 The record

One record per finished attempt. Minimum fields:
- `id`, `created`, `source_model`, `provenance` (who or what produced it).
- `problem`: short text plus labels (see 4.3).
- `solution`: the approach actually used. Either a short plan or a runnable script or both.
- `outcome`: `success | fail | partial`, with `verified_by` (external check, self-judge, none).
- `lesson`: one line saying why it worked or failed and when it applies.
- `util`: counters `retrieved`, `helped`.
Optional: `trace` (raw trajectory, truncated), `context` (task family, tools, model).

Evidence for each field: problem, solution, outcome are in every source (K01). The lesson field is supported by Reflexion (+8 over trajectory-only memory, b11), ExpeL and ReasoningBank. The value of `trace` is supported by Memp (both beats either, d10), ExpeL ALFWorld (retrieval beat insights, a30) and DS-Agent (script cases, c02). `context`/`metadata` rests only on the Hatalis review (a37) and Agent KB's predicates (b24). Treat it as unproven.

### 4.2 Three record shapes seen in the literature

1. **Raw case.** Task plus full trajectory or script (Synapse, DS-Agent, Memento). Strength: exact, runnable, strong when tasks repeat. Weakness: biases the agent toward example-specific details (AWM, c15), eats tokens.
2. **Distilled item.** Title, description, short content (ReasoningBank). Strength: short, transfers, uses failures. Weakness: lossy, depends on a good distiller.
3. **Pair.** Distilled lesson plus the concrete case it came from (ExpeL, Memp "both", Agent KB). Best in Memp ALFWorld (77.86 vs 74.29 vs 56.43). Costs more tokens per hit; no equal-token test exists.

### 4.3 Indexing (Kolodner's two halves)

Write time: label the record with when it applies. Candidate label sets, from the sources:
- Problem class or structure with entities masked to their role (CBR-to-SQL skeleton, c30; AWM placeholders, c14).
- Error type or failed operator (TextBFGS, c27).
- Goal-constraint predicates (Agent KB, b24).

Read time: build the same labels for the new problem first (Kolodner's assessment step), then match. Do both semantic and lexical match. Springdrift's six-signal fusion (inverted index 0.25, embedding 0.40, field score 0.10, recency 0.05, domain 0.10, utility 0.10, K capped at 4) beat dense-only on its synthetic test (P@4 0.883 vs 0.796 on hard queries), but its ground truth was keyword overlap, so that favours the lexical part (c29).

Re-index after use (Kolodner, a04): when a retrieved case did not help, drop or weaken the label that fetched it. When a case that should have been fetched was missed, add the label.

### 4.4 Retrieval and use

- Retrieve 1 to 4. One item gets most of the gain (Memento, ReasoningBank). Stop at about 4.
- Optionally let the model re-rank candidates using the last run's feedback (DS-Agent ReviseRank: avg best rank 2.08 full vs 2.58 without, a29).
- Adapt before use. Agent KB loses 3 points when a raw workflow is replayed instead of refined (d14). Add an explicit adapt step: "what in this case matches, what differs, what to change".
- Tell the model the record is a hint with a verification status, because it will copy it (K07).

### 4.5 Retain: admission, update, eviction

Admission (Xiong, Kolodner, IB3): write only after an external check. If no external check exists, store the lesson but mark `verified_by: self` and do not use it as a demonstration. Add-all lost 12 points on RegAgent.

Update: revise a record after a failed use rather than append (Memp: Reflexion-style update best, d12). Merge near-duplicates. Do not rewrite the whole memory each step: ACE's rewrite collapsed an 18,282-token context to 122 tokens (accuracy 66.7 to 57.1, below the 63.7 baseline, d07). Use small incremental edits (ExpeL's ADD, EDIT, UPVOTE, DOWNVOTE style, a30).

Eviction: keep a Laplace-smoothed utility `(helped+1)/(retrieved+2)` as Springdrift does (c29). Delete low-utility records only when the helped/not-helped label comes from a reliable check (Xiong d03).

### 4.6 Test-time scaling feeds the bank

ReasoningBank MaTTS: run k attempts, then distill from the contrast between them. Parallel k=5 reached 55.1 vs 49.7 at k=1. Without memory the same extra attempts reached only 42.2 (c19). ExpeL says the same: experience gathered with retries beats single-attempt experience (b10).

## 5. What holds up

**Holds up across several independent sources**
- Fields: problem, solution, outcome, plus a reason (K01).
- Few retrieved cases. Three independent studies show a cap near 1 to 4 (K05).
- Distilled short items beat full history and raw trajectories on knowledge-heavy and web tasks (K03).
- Admission control. Add-all hurts in four agent types (K08).
- Experience-following and its attack surface: Xiong, MINJA, AgentPoison (K07, K28).
- Retries produce better memory (K17).

**Single-source, treat as hypotheses**
- Memento's learning curve and its near-convergence with no-CBR by pass five (K06).
- Error-keyed indexing (TextBFGS, tiny benchmarks) (K11).
- Pair beats either alone (Memp) (K22).
- Adapt-before-use (Agent KB) (K29).

**Failed or contradictory**
- AWM lost 2.2 points on Shopping when failures were added (44.4 to 42.2). Cross-site tasks: AWM gave no gain and degraded (b23).
- CER: success-only 33.5 beat success+failure 31.4 on whole WebArena. This conflicts with the failure-helps line and fits the "only if the format can use them" reading.
- ExpeL: reflections added to insight extraction hurt; few-shot-only insights gave no gain over ReAct (b09, b10).
- GPT-4o full history on AIME 2024 fell 20.0 to 13.3 (b19). Training-Free GRPO: directly generated, unchecked experiences did slightly worse than ReAct on AIME (79.8/67.3 vs 80.0/67.9, d15). QwQ-32B fell 27.5 to 25.5.
- Dynamic Cheatsheet on Game of 24 with Sonnet: 12 to 14 only (b20).
- Memento: tools alone were negative (-18.0 F1). Case memory's gain is smaller than planning's (c22).
- Hu et al.: models trained on examples match cases, not rules (c08). A reason surface-similar cases can mislead.

**Moderators**
- Task similarity (r 0.56 to 0.72, Evo-Memory). Repeated templates (WebArena, ALFWorld) show the biggest gains. WebArena templates repeat up to five times (d16).
- Format: strategy items tolerate noise better than raw demos (K24).
- Evaluator quality: decides whether growth and deletion help.
- Model: not monotone in size (K19, K27).
- Domain: problem-keyed retrieval wins in-domain, error-keyed across domains (c27).

**Interventions that worked**: strict admission, short curated items, adapt step, utility deletion with a reliable judge, merge/dedupe, retry-then-distill, cap near 1-4, revise-on-failure.
**Interventions that did not**: add-all, full-history append, whole-memory rewrite, success-only workflows with failures added, reflections inside insight prompts, history-based deletion under a noisy judge, many retrieved cases.

**Weak spots in the whole base (critique.md)**: single runs with no variance (exceptions: ExpeL standard errors 0.3 to 2.1, Sarukkai 3 seeds). WebArena effects of 2-4 points are within plausible noise. Small test sets (CBR-RAG 32 queries; TextBFGS about 45 items; AIME 30 problems per year). Several papers evaluate their own method (Evo-Memory ReMem, Training-Free GRPO, DeMem). The founding CBR texts have no experiments.

## 6. Language models

How LLMs behave with case memory:

1. **They copy.** Output similarity follows input similarity (Xiong, r near 1). With GPT-4 and GPT-4o, planted records were followed: MINJA injection above 95%, AgentPoison about 80% attack success from under 0.1% poison. No test on current frontier models.
2. **A few records suffice.** One record gives most of the gain (Memento +3.7 F1 at K=1 of +4.6 total; ReasoningBank 49.7 at 1 item).
3. **Format moves results by single digits to double digits.** Distilled strategies +4.6 to +8.3 on WebArena over no memory. Workflows +12.0 on WebArena for AWM (different base agent, so not comparable to ReasoningBank). Pair vs script in Memp: +21 points (77.86 vs 56.43 GPT-4o ALFWorld test).
4. **Memory vs just doing more.** Planning alone gave +29.1 F1 in Memento against +6.7 for CBR. Best-of-N without memory gave +3.2 (39.0 to 42.2); with memory +5.4 from the same k. Gains from memory and sampling add (CER 52.6 vs 43.1 and 37.7), but sampling cost more tokens (K25).
5. **Learning from own runs works with a check.** Sarukkai: 3,500 tasks of self-generated examples beat a model upgrade on ALFWorld (+20 vs +15 points). Without an external signal, ACE and Dynamic Cheatsheet can fall below baseline (d07).
6. **Noise tolerance depends on the format.** ReasoningBank: 47.6 to 50.6 for judge accuracy 100 to 50%. ACE: one bad update in five still +5.4 over base; every step -4.0. Xiong: coarse judge with raw demos lost to a frozen bank. DeMem: 91.1 to 88.9 at 20% flipped (conversational memory, not case memory).
7. **Model size.** Mixed. ReasoningBank gain fell as the backbone got stronger (+8.3, +7.2, +4.6). Evo-Memory says smaller models benefit most. A weak model (Haiku) gained on AIME 2024 and not 2025. A strong model's memory helped a 14B model (+5% completion). A 32B reasoning model lost.
8. **Puzzles.** No ARC or brainteaser memory study was found. Indirect: small gains where tasks do not repeat (AIME-25, GPQA in Evo-Memory). Training-Free GRPO still gave +2.7 and +5.4 on AIME24/25 for a 671B model from 100 samples, but that is within a few points on 30 problems.
9. **Old models dominate the base.** Most studies use gpt-3.5, GPT-4, GPT-4o, Gemini-2.5, Claude-3.5/3.7. Transfer to current Claude is unmeasured.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = S9 store. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| S9 record has problem, solution, outcome (success/fail/partial) and a one-line "why/when it applies" | memory S9 | [E] | K01; a01, a06, a07, a14, a37, b01, c29, c31 |
| Store failures with a distilled lesson. A failure without a lesson is not enough | memory S9 | [E] | K02; a03, a21, b22, c18 |
| Keep the stored item short and strategy-level (title, one line, 1-3 sentences). Do not append full history | memory S9 | [E] | K03; a20, b06, b19, b21 |
| Retrieve at most 1 to 4 records (default 2) | memory S9 / O retrieve | [E] | K05; a15, a22, c03, b02 |
| Write a record only after an external check; unverified records are flagged and never shown as demonstrations | G (anti-anchoring) + memory admission | [E] | K08, K07, K28; a05, a13, a33, a34, d01 |
| Treat retrieved cases as hints the model will copy: show verification status, and run an adapt step before use | G + O reuse | [E] for the copy risk, [S] for the adapt step | K07; a33, b14, d02, d08, d09; K29; b24, d14 |
| Track a utility count per record; delete low-utility ones only when the helped/not-helped label is reliable | memory eviction | [E] | K09; b16, c24, d03, c29 |
| Small incremental edits and merge/dedupe; never rewrite the whole bank in one pass | memory update | [E] | K28; d06, d07, a30 |
| After retries, distill the contrast between the failed and successful attempts into a record | O retry + memory | [E] | K17; c19, b10, b24 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Field ablation: which of problem, solution, outcome, why, context earns its tokens | memory S9 | [S], nothing found | K21, K30 |
| Record = lesson + one concrete worked example (pair) vs lesson-only vs case-only | memory S9 | [C] | K04, K22; a30, c02, d10 |
| Index on error type or failed operator rather than task wording | memory index | [S] | K11, K23; c27, c28, d11 |
| Memory vs equal-token retries or best-of-N | memory value | [S] | K25, K06; d16, b03, b23 |
| Outcome-label noise tolerance for lesson-style vs raw records | memory outcome label | [C] | K10, K24; a23, d04, d06, a34 |
| Adapt step between retrieve and use | O reuse | [S] | K29; b24, d14 |
| Gain vs task similarity on reasoning puzzles | memory scope | [S] | K26; d13, d15 |
| Gain across model sizes, and strong-written records read by a weak model | memory S9 | [C] | K19, K27 |
| Bank size and eviction at 50, 200, 1000 records | memory size | [C] | K20, K31 |
| Re-indexing after use (Kolodner) | memory index | [S] | a04; no LLM test found |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (prompt plus generation, including memory tokens and the cost of writing records). Fixed slice of ARC and BrainTeaser items, at least 3 seeds, report mean and spread. A split into "seen-structure" and "novel-structure" items is required for every test because gain tracks task similarity (K26).

1. **Field ablation.** Items: ARC and BrainTeaser slice with a solved-run bank of about 100 records. Arms: full record; minus outcome; minus lesson; minus solution; minus context; problem + lesson only. Metric: accuracy at equal tokens, plus tokens per hit. Expected: lesson and outcome carry most value; context adds nothing (unproven).
2. **Pair vs lesson vs case.** Arms: lesson-only; one concrete worked example only; lesson + example. Metric: accuracy by task type. Expected: pair best on seen-structure items (Memp +3.6 over trajectory, +21 over script); lesson-only closer on novel items.
3. **Memory vs retries.** Arms: no memory with N tries; memory with 1 try; memory with N tries. Equal tokens means N is set so arm 1 and arm 3 match. Metric: accuracy. Expected: memory with fewer tries is no worse than N tries without memory on seen-structure items, and equal or worse on novel items.
4. **Label noise.** Inject 0, 10, 20, 50% flipped outcome labels into the bank. Arms: lesson-style records vs raw-case records. Metric: accuracy slope against noise. Expected: lesson-style flatter (ReasoningBank, ACE), raw records steeper (Xiong).
5. **Index key.** Arms: task-wording key; error-type/operator key; both. Items: in-domain and cross-domain splits. Metric: accuracy and retrieval precision@2. Expected: error key wins cross-domain, wording wins in-domain (TextBFGS).
6. **Misleading case.** Plant a similar case with a wrong outcome. Arms: no flag; flagged unverified; flagged plus adapt step. Metric: copy rate of the wrong answer, accuracy. Expected: copy rate high with no flag; flag plus adapt lowers it.
7. **Retrieval cap.** Arms: 0, 1, 2, 4, 8 records at fixed memory-token budget. Metric: accuracy. Expected: peak at 1 to 4.
8. **Eviction.** Arms: no eviction; utility eviction with ground-truth labels; utility eviction with self-judged labels. Bank 50, 200, 1000. Metric: accuracy, bank size. Expected: ground-truth eviction no worse and smaller; self-judged unstable.
9. **Model size.** Same bank on one weak and one strong backbone; also strong-written bank read by weak model. Metric: gain over no memory. Expected: inconsistent; the test decides.
10. **Admission.** Arms: write-all; write after external check; fixed small seed set. Metric: accuracy over a stream of 200+ items. Expected: check beats write-all (Xiong +3 to +15 points).

## 9. What does not transfer, and why

- **WebArena and ALFWorld gains.** Tasks come from repeated templates, so a stored case often matches a later task. ARC and brainteaser items rarely repeat. Expect smaller gains (Evo-Memory r 0.56 to 0.72; small on AIME-25 and GPQA).
- **Large banks.** LLM-agent banks saturate at about 3k records and often work at 100 to 500. Classic CBR millions-of-cases results do not carry over.
- **Aha et al. numbers.** They are for attribute-vector classification with a class label, not rich problem-solution cases. The admission logic transfers, the numbers do not.
- **Memento's training-based part.** The parametric Q-function needs training. We do not train. Only the non-parametric part (79.84 to 84.85) applies, and its gap to no CBR is small by pass five.
- **Hu et al. (case matching in trained transformers).** About models trained on examples, not prompted agents. It is a warning about surface similarity, not a design rule.
- **Zeng et al. memory formats.** Document QA, not agent experience.
- **Springdrift and CBR-RAG numbers.** Synthetic keyword ground truth; 32 test questions in legal QA. Use the design, not the effect size.
- **Review papers** (Hatalis, Watson, Feng): definitions only, no measurements.
- **Safety attacks.** MINJA and AgentPoison assume an open or shared memory. Our bank is private, so poisoning risk is lower, but the same copy behaviour means our own wrong records act as poison.
- **Human CBR theory.** Kolodner's indexing and re-indexing ideas have no human or LLM measurements in this base. Use as design hints.

## 10. Open questions

1. Which case field earns its tokens? No study ablates fields at equal tokens (K21, K30).
2. When does abstract beat concrete, and does a pair beat both at equal tokens? Memp says yes on repeated templates; ExpeL and DS-Agent lean concrete; ReasoningBank, AWM and Dynamic Cheatsheet lean abstract (K04, K22).
3. Does memory still add value against equal-token retries or best-of-N? Memento's curve converges; CER says complementary; none tested at equal tokens (K06, K25).
4. How noisy can labels be before memory hurts, with variance reported? Studies disagree and use single runs (K10, K24).
5. Which retrieval key generalises? One benchmark per key study (K11, K23).
6. Do misleading cases harm current frontier models, and by how much? Tested only on GPT-4 class (K28).
7. Bank size and eviction beyond about 4k items or 5 passes (K31).
8. Do results hold on puzzles where problems rarely repeat? No ARC study found (K26).
9. How does the benefit scale with model size (K27)?
10. Does Kolodner-style re-indexing after use help an LLM store? No test found.
11. Does the explanation field (the "why") help beyond the lesson line? Untested.

## 11. Sources

[V] = opened and read (opened:true in the evidence files). The cross-check pass re-read the Memento, ReasoningBank, ExpeL, AWM, Dynamic Cheatsheet, Xiong, CBR-RAG and Sarukkai numbers. Not re-read in the cross-check (first-pass reading only): Aha et al., Kolodner, Aamodt-Plaza, TextBFGS, Springdrift, CBR-to-SQL, DomAgent, Hu et al., Zeng et al., Evo-Memory, Agent KB, Buffer of Thoughts.

- [V] Kolodner (1993) Introduction to the special issue on case-based reasoning. Machine Learning 10:195-199. https://link.springer.com/content/pdf/10.1023/A:1022618509614.pdf
- [V] Aamodt and Plaza (1994) Case-based reasoning: foundational issues, methodological variations, and system approaches. https://www.iiia.csic.es/~enric/papers/AICom.pdf
- [V] Aha, Kibler and Albert (1991) Instance-based learning algorithms. Machine Learning 6:37-66. https://link.springer.com/content/pdf/10.1007/BF00153759.pdf
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153
- [V] Ouyang et al. (2025/2026) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302
- [V] Guo et al. (2024) DS-Agent. https://arxiv.org/abs/2402.17453
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang, Mao, Fried and Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Hatalis et al. (2025) Review of case-based reasoning for LLM agents. https://arxiv.org/abs/2504.06943
- [V] Feng et al. (2023) Case repositories. https://arxiv.org/abs/2311.10934
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Sarukkai et al. (2025) Self-generated in-context examples. https://arxiv.org/abs/2505.00234
- [V] Zheng et al. (2024) Synapse. https://arxiv.org/abs/2306.07863
- [V] Zeng et al. (2024) On the structural memory of LLM agents. https://arxiv.org/abs/2412.15266
- [V] Tang et al. (2025) Agent KB. https://arxiv.org/abs/2507.06229
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Wei et al. (2025/2026) Evo-Memory. https://arxiv.org/abs/2511.20857
- [V] Hu et al. (2024) Case-based or rule-based: how do transformers do the math? https://arxiv.org/abs/2402.17709
- [V] Zhang et al. (2026) TextBFGS. https://arxiv.org/abs/2602.00059
- [V] Springdrift (2026) persistent runtime with case-based memory. https://arxiv.org/abs/2604.04660
- [V] CBR-to-SQL (2026). https://arxiv.org/abs/2603.05569
- [V] Watson (2024) A case-based persistent memory for a large language model. https://arxiv.org/abs/2310.08842
- [V] Wang and Feldt (2026) DomAgent. https://arxiv.org/abs/2603.21430
- [V] Dong et al. (2025) MINJA. https://arxiv.org/abs/2503.03704
- [V] Chen et al. (2024) AgentPoison. https://arxiv.org/abs/2407.12784
- [V] Zhang et al. (2026) Agentic Context Engineering (ACE). https://arxiv.org/abs/2510.04618
- [V] Fang et al. (2025) Memp. https://arxiv.org/abs/2508.06433
- [V] Youtu-Agent Team (2025) Training-Free GRPO. https://arxiv.org/abs/2510.08191
- [V] Liu et al. (2025) Contextual Experience Replay (CER). https://arxiv.org/abs/2506.06698
- [V] Zou et al. (2026) DeMem. https://arxiv.org/abs/2605.10870

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 9 established claims: 5 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C08.04-K01** (reworded: the sources support less). Sources support the problem/solution/outcome core (Aamodt-Plaza, Memento (s,a,r), Hatalis (P,S,O,M)), but the explanation-of-why is only in Aamodt-Plaza/Kolodner (Memento and Hatalis tuples hold no explanation), and the (Q,S,E,A) tuple appears in none of the listed sources. Corrected claim: A case worth storing carries problem description, solution and outcome (including failures); classic CBR (Kolodner, Aamodt-Plaza) can also store an explanation of why the solution works or failed, but the LLM-agent tuples (Memento state,action,reward; Hatalis P,S,O,M with metadata) hold only the problem-solution-outcome core and no explanation.
- **C08.04-K08** (reworded: the sources support less). Numbers are right (55.48 vs 67.53, strict 70.95), but Kolodner and Aha IB3 do not give 'the same' rule: Kolodner admits a case only if it adds capability or efficiency, IB3 drops stored instances with poor classification records as a noise filter. Corrected claim: Admission control matters: adding every run gave worse results than a small fixed memory when the filter is weak (RegAgent add-all 55.48 vs fixed 67.53); a strict filter reached 70.95. Kolodner (admit a case only if it adds capability or efficiency) and Aha IB3 (drop instances with poor success records as a noise filter) point the same way, though they are different rules.
- **C08.04-K17** (reworded: the sources support less). Numbers are correct (49.7 to 55.1; 39.0 to 42.2; Refine removal -6.06), but the paper measures task success rising with more trials when memory is present, not memory quality directly, and the Agent KB Refine ablation says nothing about repeated trials. Corrected claim: With memory, more trials per task raise success (ReasoningBank MaTTS parallel k=1 49.7 to k=5 55.1; without memory 39.0 to 42.2, not monotone). Separately, Agent KB shows that removing its Refine/adapt step gives the largest drop (61.21 to 55.15 pass@1 on GAIA).
- **C08.04-K28** (reworded: the sources support less). MINJA, AgentPoison and Xiong numbers check out, but merge-and-dedupe is only asserted by ACE's authors as a 'first line of defense' (ACE tolerated harmful reflections but its dedup threshold study did not test mitigation), and benign density lowered ASR on EHR/MIMIC (68.9 to 31.1) but barely on Webshop. Corrected claim: Misleading cases are followed by GPT-4-class models: MINJA injection above 95 percent, attack success above 70 percent in half the configurations; AgentPoison about 80 percent attack success with poison below 0.1 percent. Measured mitigations: more benign records in memory (lowered MINJA attack success on EHR, little effect on Webshop), strict admission, and utility-based deletion (Xiong et al.); ACE's merge-and-dedupe is proposed by its authors as a defense but was not measured as one.
