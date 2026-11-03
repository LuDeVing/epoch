# Dynamic memory, early CBR: deep document

*Subfield C08.02. Sources: evidence_a-d.jsonl (ids a01-a32, b01-b30, c01-c26, d01-d19), claims.jsonl (K01-K31), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Dynamic memory is the idea that long-term memory is organised by episodes and reorganises itself every time a new episode arrives. It came from Roger Schank's group at Yale around 1979-1983. The key works are Schank (1979, 1982), Kolodner's CYRUS (thesis 1980; Cognitive Science 1983) and Lebowitz's IPP (1983) and UNIMEM (1987). These were the first case-based reasoners (a17, a19, c01).

The core design has four parts.
- A **generalised episode** holds norms (features shared by all its episodes), indices (features that tell its episodes apart) and the episodes themselves (a15, a17).
- A new episode is filed by walking down the index tree. If it shares an index with an old episode, a new sub-node forms. The shared features become provisional norms (a03, a15).
- Later episodes confirm, refine or demote those norms. Memory is never fixed.
- Retrieval needs a cue that names the discriminating index. If it does not, the system elaborates the cue (infers missing features) or follows related events (a06, a07, b03).

Why it matters for our agent: this is the original design for a lesson and case memory that grows without blowing up. SCHEMA.md section 5 already holds "lessons", a "class record" and a planned "subgoal library". This subfield says how to organise, update and retrieve them, and what can go wrong.

**Honest limit.** Early CBR has no quantitative evaluation anywhere. CYRUS, IPP and the AUTHOR program were shown by worked examples on hand-built narrow domains (a01, a16, d10, K01). The numbers in this document come from 2023-2026 LLM-agent papers that re-implement the ideas, not from the founders. The human-data foundations (Bower, Black and Turner 1979; Reiser et al. 1985; Williams and Hollan 1981; Schank 1982 book) were not opened, so no numbers from them are cited (a13, b09, b10, d18).

## 2. History and theories in depth

**Scripts to MOPs (1977-1979).** Schank and Abelson (1977) used scripts: one fixed sequence per situation, such as a restaurant. Bower, Black and Turner (1979) found people confuse stories about a dentist and a doctor. One restaurant-style script cannot explain that (a11, via Schank's report; the original was not opened). Schank (1979, Yale RR-170, 97 pages) replaced monolithic scripts with small shared scenes tied together by memory organisation packets (MOPs). Wikipedia notes scripts "ultimately ended without tangible success" and were too rigid (b08).

**Reminding.** In the 1979 account a script runs scene by scene. When an event breaks the script's expectation, the scene becomes an entry point to memories hung off it. A past episode is recalled exactly when the current one breaks the same expectation. Example: four stored deviations under the restaurant "order" scene, such as banging silverware to get service (a12). This is the first rule for "which past case to show": the one that violated the same expectation.

**Dynamic Memory (Schank 1982).** The book is the base of CYRUS and IPP (a19, c01). It was not opened; a second edition appeared in 1999. What we know of its content comes from Kolodner's thesis and Aamodt and Plaza (1994).

**CYRUS (Kolodner).** Thesis 1980, Yale RR-187, 247 pages (a01). Domain: events in the lives of Secretaries of State Vance and Muskie.
- Events live in episodic MOPs (E-MOPs). Each holds norms plus an index tree that separates events by how they differ from the norms.
- About 10 search strategies, modelled on strategies seen in people. Three MOP classes: scripts, simple MOPs, intentional MOPs. The full list has 9 scripts, 10 simple MOPs, 4 intentional MOPs (a01, a07).
- Design aim: retrieval time should not grow as memory grows. Kolodner states the fan-effect debate openly (Anderson 1974/76: more facts, slower retrieval; Smith, Adams and Schorr 1978: no slowdown when context guides retrieval) (a02).
- Generalised and episodic knowledge sit in one structure, so one process retrieves both. Kolodner argues against a sharp episodic/semantic split (a05).
- CyFr = FRUMP (reads UPI wire news, about 60 sketchy scripts, about 2,300 root words, about 8.5 s CPU per sample article) feeding CYRUS. About 50 Vance stories and about 30 Muskie stories in the thesis; the Dec 1980 report says about 10 Muskie (a07, a09; critique item 6: dates differ, both may be right).
- Hand-coded versus machine-coded input exposed a gap. Hand-coded events named their E-MOPs and implied related events. FRUMP output did not, so a separate program (CYRECV) had to infer the E-MOP and related trips (a10). Lesson: the writer of a memory must supply the discriminating context, or a later step must rebuild it.
- Dates: thesis 1980, journal 1983 (Cognitive Science 7). A course slide says 1984; use 1980 and 1983 (critique item 7).

**IPP (Lebowitz).** Reads news stories (terrorism), uses MOPs, and builds generalisations while reading. After many Italian kidnapping stories with businessman victims, it infers that an unnamed victim in a later story is probably a businessman (a08). Kolodner's comparison: IPP uses generalisations to understand later stories; CYRUS uses them to retrieve episodes. IPP cannot refine a generalisation; it keeps or deletes whole descriptions (d12). Lebowitz (1983) abstract: IPP retrieves examples, builds generalisations, checks them against later evidence (b06; full text blocked 403).

**UNIMEM (Lebowitz 1987, Machine Learning 2:103-138).** Domain-independent follow-up (d10). Run on universities (150 instances, about 20 features), Congressional votes (100 instances) and terrorist events. Spurious two-instance generalisations are repaired by dropping unreliable features over time. Design target: 4 to 12 sub-generalisations per node, instances split roughly equally (d13). The only numeric experiment is a parameter sweep (d11); there is no accuracy.

**Human-data questions (Kolodner and Barsalou, c.1982).** The author and a psychologist list open questions: are events the basic unit, do people elaborate cues as CYRUS does, how is a discriminating feature chosen, is generic structure learned automatically (a14, b01). No data. They cite Williams and Hollan (1981) for elaboration in retrieval from very long-term memory (not opened).

**Applications and neighbours.** Dehn (1981) AUTHOR applies reconstructive retrieval to story invention; reminding is a side effect of memory stored where expectations were violated, "useful but never reliable" (a16, b04). Aamodt and Plaza (1994) formalise the model, call CYRUS the first system that may be called a case-based reasoner, and note the index network can grow explosively, so CYRUS limits the index vocabulary (a04, a17). They contrast it with the category-exemplar model of PROTOS: CYRUS-type systems retrieve on surface similarity, while PROTOS, CASEY, GREBE and CREEK use deeper knowledge (a18). First deployed CBR system: Lockheed CLAVIER (1989). First ICCBR: 1995 (c02).

**The 2023-2026 revival.** LLM agents re-created this design, often without citing it: Memento (case bank, 2025), ExpeL (episodes plus insights), ReasoningBank (strategy items), Agent Workflow Memory, Memp, Dynamic Cheatsheet, Reflexion, Generative Agents, Voyager (a21-a31, b11-b30, c03-c26, d01-d09). Section 6 gives their numbers.

**Cross-links (not covered here).** The 4R cycle, case representation, retrieval and similarity, adaptation, base maintenance, retention policy, bandit retrieval and failure-driven CBR have their own subfields in this series (folders 01, 04-10). This document only notes where they touch.

## 3. Core findings with exact numbers

Early-CBR rows are design facts, not measurements. Other rows are 2023-2026 LLM-agent studies.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Episodes stored under generalised norms with discriminating indices; evaluated only by worked examples | CYRUS: 247-page thesis, about 10 search strategies, 3 MOP classes (9 scripts, 10 simple MOPs, 4 intentional MOPs); no accuracy figure | a01, a09, a10, b01, d10, d12 | [E] (that no test exists) |
| Norm promotion rule: first two episodes sharing an index form an E-MOP; certainty not judged before 6 events; sub-MOPs indexing a large majority collapse into the parent | 6 is an implementation detail, not fitted; "large majority" not numeric | a03, a15, b02 | [S] |
| Index vocabulary must be small and salient; near-universal features stay norms | UNIMEM target fan-out 4-12 per node | a04, a17, d13 | [E] |
| Retrieval fails when the cue lacks the discriminating index; repair by schema triggering, inferring index values, following related events | no rates; inference "can cause false starts" | a06, a07, a15, b03 | [E] as design; untested for LLMs (K31) |
| Case bank raises accuracy (Memento) | DeepResearcher F1/PM 59.9/72.2 to 66.6/80.4; HLE PM 17.4 to 24.4; SimpleQA PM 89.7 to 95.0; GAIA val 87.88 Pass@3 | a21, b11, b12, c03 | [E] |
| Much of the case gain is repeated attempts and tools | no-CBR 78.65 to 84.47 over 5 iterations; CBR adds 1.2-1.8 pts at iter 1 and 0.4-1.0 at iter 5; HLE gain mostly tools plus planner split | a23, b12, b13, c05 | [C] |
| Memory beats no-memory best-of-N at equal rollouts (web) | Shopping k=5: no-memory 39.0 to 42.2 (+3.2); MaTTS 49.7 to 55.1 (+5.4); pass@5 52.4 vs 62.1 | d01, d02, c10 | [S] |
| A few cases are enough | Memento K=0/1/2/4/8/16/32 F1 = 59.9/63.6/63.7/64.5/64.1/63.9/63.9; PM 72.2/77.9/78.1/78.5/78.2/78.1/78.1. DS-Agent: more than one case hurts. CBR-RAG k=3 best. Memp ALFWorld: rise, plateau, decline | a22, b13, c04, c16, c23, d08 | [E] |
| Retrieve by task similarity, not random or reasoning similarity | ExpeL ALFWorld: ReAct 40.0, random 42.5, reasoning-sim 48.5, ExpeL 59.0 | b20, c07 (a26 wrong on random) | [S] |
| Retrieval key from LLM-extracted keywords beats raw query | Memp TravelPlanner GPT-4o: none 71.93, random 74.59, raw query 73.38, keywords 76.02; Claude-3.5 63.49/63.99/64.93/65.76; Qwen2.5-72b 56.57/59.76/61.71/63.41 | d06 | [S] |
| Abstraction plus episodes beats either alone, task dependent | ExpeL insights-only vs retrieval-only: HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38; both: ALFWorld 59, HotpotQA 39 (ReAct 28). Memp ALFWorld GPT-4o: none 42.14, script 56.43, trajectory 74.29, proceduralization 77.86 | a25, b20, c07, d07 | [E] |
| Distilled strategies beat raw trajectories and workflows | WebArena Gemini-2.5-flash: none 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8; Gemini-pro 46.7/47.7/47.6/53.9; Claude-3.7 41.7/42.6/40.8/46.3; SWE-Bench-Verified flash 34.2 to 38.8, pro 54.0 to 57.4; steps 9.7 to 8.3 | a28, b16, c09 | [E] |
| Failures help only with strong distillation | Shopping: ReasoningBank 46.5 to 49.7; AWM 44.4 to 42.2; Synapse 40.6 to 41.7 | a28, b17, c10 | [E] |
| Add-all memory hurts; checked adds help (experience-following) | RegAgent fixed 67.53, add-all 55.48, strict 70.95, coarse judge 63.18. EHRAgent 16.75 / 13.05 / 38.50 / 26.19. AgentDriver 40.11 / 32.32 / 51.00 / 36.92. CIC-IoT 71.50 / 59.90 / 85.40 | b14, c12, b24 | [E] |
| Utility-based deletion shrinks memory about 4x at small cost | RegAgent coarse: 63.18 (3511 records) to 59.32 (951) combined; strict 70.95 (2938) to 66.58 (890); kept records more often correct (EHR 44.1/49.1/54.8 vs 36.3/32.1/48.2 on three judges) | b15, c13 | [S] |
| A coarse LLM judge is nearly as good as an oracle for strategy memory | judge 72.7% accurate; success about 52.4 at best, 47.6 at 50% simulated accuracy; roughly flat from 90 to 70% | d03, c10 | [S] |
| Weak backbone or weak check removes the gain | Reflexion starchat-beta 0.26 vs 0.26; DC GPT-4o-mini AIME24 16.7 to 13.3; AWM on Claude 40.8 vs 41.7; Reflexion MBPP 77.1 vs 80.1 (test false-positive 16.3% vs 1.4% on HumanEval). Counter: Gemma-3-12B 17.1 to 24.1 with ReasoningBank while Synapse falls to 16.0 | b19, c08, b25, c25, d04 | [E] |
| Gain tracks task similarity | Evo-Memory ReMem gain correlation r=0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet) | b23, a29, b25 | [E] |
| Curated rewrite beats full history; big gain when structure is reusable | DC: Claude 3.5 Sonnet AIME24 23.3 to 50.0, AIME25 6.7 to 36.7; GPT-4o Game of 24 10 to 99; Haiku AIME24 10.0 to 36.7; full history GPT-4o AIME24 13.3 vs baseline 20.0; majority vote of 3 on Sonnet gave no gain (23.3) | a29, b25, c18 | [S] |
| Reflection buffer works with a trusted binary signal | Reflexion ALFWorld 130/134 in 12 trials; HumanEval 91.0 vs 80.1; LeetcodeHard 15.0 vs 7.5 | b19, c08 | [S] |
| Skill library of verified programs | Voyager: 63 unique items in 160 iterations (3.3x); diamond pickaxe 19 +/- 3 iterations vs 36; no self-verification -73% items | c15, a30 | [S] |
| Memory stream with reflection raises believability | TrueSkill full 29.89, no reflection 26.88, no reflection/planning 25.64, no memory 21.21; KW chi2(4)=150.29; d=8.16 | b26, c14 | [S] (human-rated, not accuracy) |
| Reading the full context often beats elaborate memory | Mem0: full 72.90, Mem0g 68.44, Mem0 66.88, A-Mem 48.38; p95 latency 17.1 s vs 1.44 s; tokens 26k vs 1.76k. MemoryAgentBench: long context 48.8-60.6 vs agentic memory 18.7-37.7. LongMemEval about 30% drop | b27, b28, c19, c20, c24 | [E] |
| A-Mem gains not reproduced | LoCoMo A-Mem 48.38 vs Mem0g 68.44 (20 points); EvolMem base 52.18 vs A-MEM 44.54, 492.6 s vs 30.2 s for Mem0; FORGETEVAL 70.6% on handled cases, 56.9% overall | a31, b29, c19, d15, d16 | [C] |
| Legal QA with case-structured RAG: tiny gain | cosine 0.8967 to 0.9141 (+1.94%), 2,084 cases, 32 test questions | a24, b22, c06 | [E] (small gain; weak test set) |
| Fallacy CBR helps, but not by copying labels | +2.5-6 F1 in-domain, up to +8 out-of-domain; retrieved/true label overlap 27.7% | b21 | [S] |
| Transformers act as case matchers, not rule users | Llama-2-7B base-9 addition: 30.2% leave-square-out vs 92% random split; rule-following fine-tuning gives over 95% on 12-digit addition | a32, c22 | [E] |
| Q-value on each case needs few tasks | Rememberer: 10 training tasks vs 10,587 for RL; WebShop 0.39 vs ReAct 0.36 | c17 | [S] |
| Explicit CBR loop, Kaggle-style tasks | DS-Agent: avg best rank full 2.08, no ReviseRank 2.58, no CBR 3.41; cost per task down 91.5-92.5% dev to deploy | c16 | [S] |

## 4. Mechanisms and models

### 4.1 Generalised episode (E-MOP) store
Data structure (after a15, a17):
```
GE   { norms: {feature: certainty}, indices: {feature -> child GE or case},
       cases: [case], n_events: int }
Case { situation_features, action/solution, outcome, lesson, quality, uses, utility }
```
Insert(case):
1. Start at the root GE. Pick the node whose norms match most of the case's features.
2. For each salient feature of the case that is an index here, follow it.
3. If the index slot is empty, store the case there.
4. If the slot holds one other case, make a new child GE. Its norms are the features both cases share (provisional). Its indices are the features where they differ.
5. If the slot holds a GE, recurse.
6. Update certainty: a confirming event raises it, a conflicting event lowers it. Do not trust a norm before about 6 events (a03).
7. If a child GE indexes a large majority of its parent's cases, merge it into the parent. If a norm's certainty falls, demote it to an index or drop it (a03, b02).

Rule for what to split on: deviations from the norm are good sub-categories; norms are not (a09). Keep the index vocabulary small (a04). Aim for 4-12 children per node (d13).

### 4.2 Retrieval with cue elaboration
```
retrieve(query):
  cue = extract_situation_features(query)          # LLM slot
  ge  = best matching GE by norms
  loop:
     follow every index named in cue
     if no index fires:                            # failure in a06
        (a) schema trigger: pick another GE the situation resembles
        (b) infer plausible values for missing indices, then follow them
        (c) follow links from related cases (same trip, same negotiation)
  return top k cases (k about 1-4)
```
A cue must name the discriminating index to be traversed (b03). Inference can produce false starts, so keep the original cue and mark inferred features as guesses. Retrieval is by situation features, matching ExpeL's task-similarity result (c07) and Memp's keyword key (d06). The closest tested analogue of elaboration is HyDE: a hypothetical document embedded in place of the query lifts TREC DL19 nDCG@10 from 44.5 (Contriever) to 61.3 and DL20 from 42.1 to 57.9 (d14). That is document retrieval, not episode retrieval.

### 4.3 Abstraction layers
Modern work finds three useful layers; they are the same ladder as CYRUS:
1. Raw trajectory (case): most useful when the new task is close (Memp trajectory 74.29 vs script 56.43 on ALFWorld, d07).
2. Procedure or workflow (a sub-routine shared by several cases): Memp proceduralization 77.86; AWM +12.0 points on WebArena (a27).
3. Strategy or insight (norm): ReasoningBank items with title, description, content; ExpeL insights with ADD, EDIT, UPVOTE, DOWNVOTE, dropped when votes fall (a25, a28).

Keep layers 1 and 3 together. ExpeL shows insights-only wins on HotpotQA and loses on ALFWorld, so offer both (b20).

### 4.4 Write gate
Experience-following means the agent copies the output of the most similar stored record; input and output similarity correlate near 1 (c12). So a wrong record spreads. Gate every write.
- Best: verified success (strict oracle). RegAgent 70.95 vs add-all 55.48.
- A coarse LLM judge is in between on raw-trajectory stores (RegAgent 63.18, EHRAgent 26.19 vs strict 38.50) but nearly as good as the oracle on distilled strategies (judge 72.7% accurate; success flat from 90 to 70% simulated accuracy) (c12, d03). The difference is memory form. Distilled items tolerate label noise; raw trajectories do not.
- Failures may be stored if distilled to "what went wrong and what to do". Raw failure trajectories hurt AWM (44.4 to 42.2) (c10).
- Memp compares vanilla append, validation (keep successes) and adjustment (edit in place when a retrieved memory fails). All beat no memory; numbers are only in plots (d09).

### 4.5 Prune
Rule from Xiong et al.: delete a record if it was retrieved at least 3 times and its mean downstream utility is below a threshold. Periodic deletion cuts memory about 3.5-4x (EHR 1012 to 248) at a cost of about 2-4 points (b15, c13). Rememberer's per-record Q-value is a smoother version (c17). UNIMEM drops unreliable features instead of whole records (d12).

### 4.6 Retention limit k
Show 1-4 cases. Past that, gains are flat or negative (K08). Cap shown cases by tokens as well as count (Memento token cost: GAIA L1 26k in/4.7k out, L3 121k/9.8k; c05).

## 5. What holds up

**Held up across several independent sources.**
- A small number of retrieved cases (1-4) is as good as many (Memento, DS-Agent, CBR-RAG, Memp; four setups, a22, c16, c23, d08).
- Unfiltered writes hurt (Xiong on four domains; Evo-Memory baselines degrade under unfiltered failures; ReasoningBank/AWM table) (b14, b24, c10).
- Memory pays when tasks recur or share structure; it pays little on low-similarity sets such as AIME-25 and GPQA for some models (b23, b25).
- Distilled forms beat raw forms for the same backbone (ReasoningBank, Memp, Dynamic Cheatsheet) (c09, d07, c18).
- Reading all context beats memory systems when the whole history fits (Mem0, MemoryAgentBench, LongMemEval; c19, c20, b27).

**Contested.**
- How much of the gain is just more attempts. Memento: the no-CBR agent climbs 78.65 to 84.47 over five iterations and CBR adds 0.4-1.0 at the end (a23). ReasoningBank: no-memory best-of-5 gains only +3.2 while memory plus best-of-5 reaches 55.1 (d01). Different tasks (research QA vs web shopping); not resolved (K07).
- Whether linked self-organising notes work. A-Mem claims wins on LoCoMo; the Mem0 re-run puts it at 48.38 vs 68.44; EvolMem and FORGETEVAL are third-party and low (K22). No third-party reproduction of AWM exists (d17).

**Failed or null.**
- Reflexion fails with a weak model (starchat-beta 0.26 vs 0.26) and weak checks (MBPP 77.1 vs 80.1) (c08).
- Dynamic Cheatsheet on GPT-4o-mini: 16.7 to 13.3; full history on GPT-4o: 13.3 vs 20.0 (c18).
- AWM on Claude: 40.8 vs 41.7 with no memory (c09).
- CBR-RAG: +1.94% on 32 questions; a weak test (a24).
- Majority vote of 3 on Claude Sonnet AIME24 gave no gain while memory did (b25), so the memory gain is not a voting effect there.

**Moderators.**
- Backbone strength: the threshold depends on memory form. Gemma-3-12B gains 7.0 points with distilled memory; raw-trajectory Synapse falls below baseline (d04).
- Task similarity: r = 0.717 and 0.563 (b23).
- Verifier quality: Reflexion needs a reliable binary signal (b19).
- Task order: ExpRAG easy-to-hard 0.77/0.87/0.37 vs hard-to-easy 0.87/0.92/0.51 (b24; values from text extraction).

**Interventions that worked.** Distilled strategies from success and failure; checked adds; task-keyword keys; two layers (episodes plus insights); utility pruning; per-case Q-values; cases shown with an explanation or counterargument (Sourati: label overlap only 27.7%, so the gain is not label copying) (b21).

**Interventions that did not.** Add-all; raw failure trajectories in AWM; storing full history; many cases; insights extracted from the few-shot examples alone (no gain over ReAct, a26). Random cases still gave a small gain (Memp commonsense 74.59 vs 71.93 none), so part of the effect is generic guidance (d06).

**Evidence quality problems** (critique.md). Single runs and no confidence intervals in most papers. WebArena is shared by ReasoningBank, AWM and Synapse, so "independent" counts papers, not testbeds. Memento's CBR numbers mix tools, planner-executor and cases; only its K sweep and iteration ablation isolate cases.

## 6. Language models

**What models do with stored cases.** They copy. Output similarity follows input similarity (Pearson r near 1, c12). The same fact shows at the arithmetic level: Llama-2-7B base-9 addition gets 92% on a random split but 30.2% when a square of operand pairs is held out. Similar in-context examples beat random ones (p<0.001); zero-shot base addition is 8.8% (a32, c22). A model can look rule-based in distribution and be case-matching. Rule-following fine-tuning fixes it (GPT-3.5 over 95% on 12-digit addition from 100 samples), but we do no fine-tuning, so the lesson is to test held-out regions.

**Agent benchmarks, sorted by lever.**

| Lever | Result | Source |
|---|---|---|
| Case bank on/off (Memento) | DeepResearcher F1 59.9 to 66.6; PM 72.2 to 80.4; HLE PM 17.4 to 24.4; SimpleQA 89.7 to 95.0 | b12, c03 |
| Learned case selector vs embedding | iter 1 79.84 vs 80.46; iter 5 84.85 vs 85.44 (about +0.6) | c05 |
| Out-of-distribution | +4.7 to +9.6 points with 4 cases per query (MuSiQue, Bamboogle, PopQA) | a23, c05 |
| Number of cases | peak K=4 (F1 64.5); K=32 63.9 | c04 |
| Memory form (WebArena flash) | none 40.5, raw 42.1, workflow 44.1, strategy 48.8 | c09 |
| Memory form (ALFWorld, GPT-4o) | none 42.14, script 56.43, trajectory 74.29, proceduralization 77.86 | d07 |
| Memory plus scaling | Shopping k=5: 55.1 with memory vs 42.2 without | d01 |
| Retrieval key | keywords 76.02 vs raw query 73.38 vs none 71.93 | d06 |
| Write gate | strict 70.95 vs add-all 55.48 (RegAgent); EHRAgent strict 38.50 vs add-all 13.05 | c12 |
| Task similarity (ExpeL) | 59.0 vs random 42.5 vs ReAct 40.0 | c07 |
| Test-time rewrite (DC, Claude 3.5 Sonnet) | AIME24 23.3 to 50.0; AIME25 6.7 to 36.7; Haiku AIME24 10.0 to 36.7 | c18, b25 |
| Reusable program stored (DC, GPT-4o) | Game of 24 10 to 99 | c18 |
| Reflexion | ALFWorld 130/134 in 12 trials; HumanEval 91.0 vs 80.1 | c08 |
| Skill library (Voyager) | 3.3x items; 19 vs 36 iterations to diamond pickaxe | c15 |
| Q-values on cases (Rememberer) | WebShop 0.39 vs 0.36 ReAct vs 0.29 LLM-only | c17 |

**Cost.** Dynamic Cheatsheet tokens per item: 370 (baseline) to 1,831 (curated memory) (c18). ReasoningBank steps 9.7 to 8.3 (16% fewer). AWM about 2 fewer steps per example (a27). A-MEM ran 492.6 s per sample vs 30.2 s for Mem0 (d15). DS-Agent per-task cost fell 91.5-92.5% from dev to deploy (c16). Full-context reading cost 17.1 s p95 vs 1.44 s for Mem0 (c19).

**What changes behaviour.** The write gate (about 12-25 points on Xiong's tasks), memory form (4-8 points) and backbone (gain vanishes for weak models with raw stores) are the big levers. Number of cases, selector and exact key are small levers (about 0.6-3 points).

**Missing.** No study tests Kolodner's strategies (cue elaboration, schema triggering, related-event search) on agents (K31). No study measures wrong-lesson rate (K30). No benchmark isolates CBR memory design (K26). Frontier reasoning tasks against equal-token best-of-N are untested (K27 is web only).

## 7. What our agent should take

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Write only verified outcomes. A lesson or case is stored only after a code check or verified success. No add-all. | memory, G2/G3 | [E] | K13: b14, c12, b24 |
| 2 | Show 1 to 4 retrieved cases or lessons, not many; cap by tokens. | memory, S3 | [E] | K08: a22, b13, c04, c16, c23, d08 |
| 3 | Store distilled lessons (one line, with the cause when from a failure) and keep a link to the source case. Do not store raw trajectories alone. | memory, S9 | [E] | K10, K11: c09, d07, a25 |
| 4 | Keep the index vocabulary small: key a case by a few salient situation features (problem class, check type, trap), not all features. Near-universal features go in the class record. | memory, S0 | [E] | K03: a04, a17, d13 |
| 5 | Track counter-evidence and retire or demote lessons that stop helping. Trust a lesson only after it helps on two different problems (already in SCHEMA section 5). | memory | [E] need; threshold [S] | K02, K12, K14: a03, b02, b15 |
| 6 | Do not rely on memory with weak checks or low task similarity. No trusted verifier: write no lesson. No similar stored case: show none. | memory, G | [E] | K15, K16, K18: c08, b23, b25 |
| 7 | Control arm: when the whole history fits, compare against reading it all. Use memory only for what cannot fit or must be cheaper. | memory, G7 | [E] | K21: c19, c20 |
| 8 | Show lessons after the first attempt (already in schema), with the case's explanation or contrast, not only a label. | memory, S5 | [E] | K23: b21 |
| 9 | Test held-out regions of a task family; do not infer rule use from in-distribution success. | G | [E] | K24: a32, c22 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 10 | Cue elaboration: infer missing situation features before searching memory (Kolodner strategy 2). | memory, S0 | [S] indirect | K04, K31: a06, b03, d14 |
| 11 | Two layers: lessons (norms) plus top-1 or top-2 raw cases, vs either alone. | memory | [S] per task | K10: b20, d07 |
| 12 | Promotion threshold: promote a lesson after 2 vs 4 vs 6 confirming episodes; demote on counter-example. Measure wrong-lesson rate. | memory | [S] | K02, K30: a03, d12 |
| 13 | Retrieval key: LLM-extracted keywords vs raw task embedding vs trace. | memory | [S] | K09, K29: c07, d06 |
| 14 | Self-judge as write gate vs oracle vs none, per memory form. | memory, G2 | [S] | K28: d03, c12 |
| 15 | Utility pruning with a use count and mean-utility rule. | memory | [S] | K14: b15 |
| 16 | Failure lessons with a "what went wrong" field. | memory, S9 | [S] | K12: c10 |
| 17 | Gain over best-of-N at equal tokens on reasoning tasks. | memory, G7 | [C] | K07, K27: a23, d01 |
| 18 | Subgoal library of verified helper programs, retrieved by description. | memory, O | [S] | K20: c15, a30 |
| 19 | Do not add note linking (A-Mem) without our own replication. | memory | [C] | K22 |

Link to operators: O7 (map an analogue) and the subgoal library are the same retrieval problem. Follow SCHEMA S3: in direct and checked modes show memory after the first attempt to avoid fixation; in open mode retrieved analogues may ground some attempts.

## 8. Concrete tests on our bench

All arms get the same total token budget (retrieval, shown text and extra attempts counted) and the same number of attempts. Streams are ordered item sequences from the same class family, plus a held-out low-similarity set.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Memory vs best-of-N | reasoning items (word puzzles, ARC-style), stream of 100+ | A: best-of-N no memory; B: best-of-N with lesson memory; C: one attempt plus lessons | accuracy at equal tokens; right-to-wrong flips | B beats A by 3-8 points if the class recurs; about zero on low-similarity items |
| T2 Write gate | same stream | verified-only vs self-judge vs add-all | accuracy at item 50 and 100; memory size; wrong-lesson share | verified > judge > add-all; add-all loses 5-15 points (Xiong) |
| T3 Wrong-lesson rate | lessons promoted from episodes | promote at 2, 4, 6 confirmations | share of lessons failing on held-out items; accuracy | 2 gives a high wrong-lesson rate; 4 near best |
| T4 Cue elaboration | items with thin cues | raw query key vs LLM-inferred feature key vs both | top-3 hit rate on a labelled "right lesson" set; accuracy | hit rate up 3-10 points; accuracy small |
| T5 Layers | recurring classes | raw cases only; lessons only; both | accuracy per class type | both best on some classes; differs by class (ExpeL) |
| T6 k sweep | same stream | k = 0, 1, 2, 4, 8 at fixed total context | accuracy, tokens | plateau at 3-4 |
| T7 Random control | same stream | matched lessons vs random lessons vs none | accuracy | random gives 1-3 points; matched beats random by more |
| T8 Weak model | small backbone | raw trajectories vs distilled lessons | accuracy | distilled helps; raw flat or negative |
| T9 Full context | streams short enough to fit | full history vs memory | accuracy, tokens | full history ties or wins on recall tasks |
| T10 Pruning | after 200 items | no prune vs use-plus-utility prune | accuracy, memory size | about 4x smaller memory at 0-3 points lower |
| T11 Held-out regions | task family with systematic holes | in-distribution vs held-out region | accuracy gap | memory-driven success drops in the holes (the 30.2 vs 92 pattern) |

## 9. What does not transfer, and why

- **Early CBR numbers.** None exist. CYRUS and IPP worked on hand-built domains with hand-coded or script-parsed input (a09, a10). No accuracy claim can be carried to our agent.
- **E-MOP index machinery as such.** CYRUS needed hand-built MOP classes and a tiny index vocabulary. With an LLM the situation features are free text. What survives: a few salient features as keys, norms as separate summaries, revision on counter-evidence (c26).
- **Surface-similarity retrieval.** CYRUS-type systems used surface similarity (a18). An LLM can use deeper similarity, but ExpeL found reasoning-similarity retrieval worse than task-similarity (48.5 vs 59.0), so deeper is not automatically better.
- **Fan effect and human retrieval claims.** Whether human retrieval slows with memory size, and whether events are the unit, were left as questions (a14). They do not bear on an LLM store.
- **Web and tool results to reasoning tasks.** ReasoningBank, AWM, Synapse and Memento are agentic and recurring (WebArena, ALFWorld, GAIA). Our bench is reasoning items. Memento's HLE gain mostly came from tools and the planner split (b12).
- **Huge gains on structured tasks.** GPT-4o Game of 24 from 10 to 99 came from storing one reusable Python solution (c18). It will not repeat on tasks without a reusable program.
- **Believability gains.** Generative agents' TrueSkill is human-rated believability, not accuracy (b26).
- **Conversation recall.** Mem0, LongMemEval and MemoryAgentBench test recall of facts from chats. Our problem is reusable know-how. Same tool, different job (K21).
- **Fine-tuning fixes.** Rule-following fine-tuning is out of scope for a scaffold-only agent.

## 10. Open questions

1. At equal tokens and equal attempts, how much of case-memory gain remains over no-memory best-of-N for a frontier model on reasoning tasks? (Gap 1: only web answered, d01.)
2. How often do LLM-written lessons from two episodes turn out wrong? (Gap 2: UNIMEM shows the failure but gives no rate, d12.)
3. What is the best index for diverse, non-recurring tasks: situation features, task embedding or reasoning trace? (Gap 3: only recurring benchmarks tested.)
4. Which write gate keeps add-all degradation away cheaply, by memory form? (Gap 4: simulated flips only.)
5. Does cue elaboration raise hit rate for agents? (Gap 5: only HyDE for documents.)
6. What do the primary human studies report in numbers? (Gap 6: unopened.)
7. Is the plateau at 3-4 cases robust across model strength and case length? (Gap 7: Memp optimum k not stated.)
8. Is there an independent AWM replication? (Gap 9: none found.)
9. Is there a measurable capability threshold for memory by form? (Gap 10: the Gemma-3-12B result suggests form matters more than size.)
10. Do Lebowitz's later systems have accuracy figures? (Gap 8: closed negative for UNIMEM.)

## 11. Sources

[V] = opened and read. [M] = snippet or abstract only. [N] = not opened (named in the literature).

- [V] Kolodner (1980) Retrieval and organizational strategies in conceptual memory (Yale RR-187). https://archive.org/download/DTIC_ADA093084/DTIC_ADA093084_djvu.txt (a01-a08)
- [V] Schank, Kolodner and DeJong (1980) Conceptual information retrieval (Yale RR-190). https://archive.org/download/DTIC_ADA095372/DTIC_ADA095372_djvu.txt (a09, a10)
- [V] Schank (1979) Reminding and memory organization: an introduction to MOPs (Yale RR-170). https://archive.org/download/DTIC_ADA080200/DTIC_ADA080200_djvu.txt (a11, a12)
- [V] Kolodner and Barsalou (c.1982) Psychological issues raised by an AI model of reconstructive memory. https://journalpub.escholarship.org/cognitivesciencesociety/article/30257/galley/20111/download (a14, a15, b01-b03)
- [V] Dehn (1981) Memory in story invention. https://journalpub.escholarship.org/cognitivesciencesociety/article/20867/galley/10600/download (a16, b04)
- [V] Aamodt and Plaza (1994) Case-based reasoning: foundational issues. https://www.iiia.csic.es/~enric/papers/AICom.pdf (a17, a18)
- [V] Lebowitz (1987) Experiments with incremental concept formation: UNIMEM. https://link.springer.com/content/pdf/10.1007/BF00114264.pdf (d10-d13)
- [M] Kolodner (1983) Maintaining organization in a dynamic long-term memory, Cognitive Science 7(4); abstract via Crossref, full text 403 (b05)
- [M] Lebowitz (1983) Generalization from natural language text, Cognitive Science 7(1); abstract via Crossref (b06). Also Lebowitz 1983 Memory-based parsing, Artificial Intelligence 21:363-404 (named in a19)
- [N] Schank (1982) Dynamic Memory (Cambridge UP); Schank and Abelson (1977) Scripts, plans, goals and understanding
- [N] Bower, Black and Turner (1979) Scripts in memory for text, Cognitive Psychology 11 (a13, b09)
- [N] Reiser, Black and Abelson (1985) Knowledge structures in the organization and retrieval of autobiographical memories (b10)
- [N] Williams and Hollan (1981); Anderson (1974, 1976); Smith, Adams and Schorr (1978); Reder and Anderson (1980) (named in a02, a14)
- [V] Wikipedia: Case-based reasoning https://en.wikipedia.org/wiki/Case-based_reasoning (a19, b07, c02); Roger Schank https://en.wikipedia.org/wiki/Roger_Schank (c01); Script theory https://en.wikipedia.org/wiki/Script_theory (b08); course slides, Watson, Univ. of Auckland https://www.cs.auckland.ac.nz/~ian/CBR/cbr01.pdf (a20). Dates only.
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 and https://arxiv.org/html/2508.16153v2 (a21-a23, b11-b13, c03-c05)
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302 (a24, b22, c06)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (a25, a26, b20, c07)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (a27, b18, c11)
- [V] Ouyang et al. (2025/2026) ReasoningBank. https://arxiv.org/abs/2509.25140 and https://arxiv.org/pdf/2509.25140 (a28, b16, b17, c09, c10, d01-d05)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (a29, b25, c18)
- [V] Sumers et al. (2024) CoALA. https://arxiv.org/abs/2309.02427 (a30, b30)
- [V] Xu et al. (2025) A-Mem. https://arxiv.org/abs/2502.12110 (a31, b29)
- [V] Hu et al. (2024) Case-based or rule-based: how do transformers do the math? https://arxiv.org/abs/2402.17709 (a32, c22)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (b14, b15, c12, c13)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b19, c08)
- [V] Sourati et al. (2023) CBR with language models for fallacy classification. https://arxiv.org/abs/2301.11879 (b21)
- [V] Wei et al. (2025/2026) Evo-Memory. https://arxiv.org/abs/2511.20857 (b23, b24)
- [V] Park et al. (2023) Generative agents. https://arxiv.org/abs/2304.03442 (b26, c14)
- [V] Wu et al. (2025) LongMemEval. https://arxiv.org/abs/2410.10813 (b27)
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413 (b28, c19)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/html/2305.16291 (c15)
- [V] Guo et al. (2024) DS-Agent. https://arxiv.org/html/2402.17453 (c16)
- [V] Zhang et al. (2023) Rememberer. https://arxiv.org/html/2306.07929 (c17)
- [V] Hu et al. (2025) MemoryAgentBench. https://arxiv.org/html/2507.05257 (c20)
- [V] Hatalis et al. (2025) Review of CBR for LLM agents. https://arxiv.org/html/2504.06943v2 (c21)
- [V] Fang et al. (2025) Memp. https://arxiv.org/pdf/2508.06433 (d06-d09)
- [V] Gao et al. (2023) HyDE. https://arxiv.org/pdf/2212.10496 (d14)
- [V] Shen et al. (2026) EvolMem. https://arxiv.org/pdf/2601.03543 (d15)
- [V] Yang (2026) FORGETEVAL-Adv. https://arxiv.org/pdf/2606.15903 (d16)
- [M] Search summary on AWM replication. https://sotaverified.org/papers/agent-workflow-memory (d17)

Id corrections (critique.md): ExpeL "random" is 42.5, not 40.0 (use b20/c07, not a26). The first author of 2402.17709 is Yi Hu, not "Hua". Memento is Zhou et al. (a21, b11 say Wang). ReasoningBank's first author is Ouyang (c09 says Zhao). The A-Mem ">25 points" figure is category-level; the overall LoCoMo gap to Mem0g is about 20.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 15 established claims: 8 confirmed as written, 7 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C08.02-K01** (reworded: the sources support less). The 1980-82 CYRUS reports show worked examples on narrow Vance/Muskie data and list the human validity of E-MOPs as an open question, but 'no quantitative test exists' is a universal negative not shown by these sources, the authors cite existing human evidence (Williams and Hollan) for its elaboration-style retrieval, and UNIMEM (a follow-up system) was evaluated with parameter sweeps; nothing opened covers IPP's own evaluation. Corrected claim: In the sources read, early dynamic-memory CBR (CYRUS E-MOPs) organised episodes under generalised norms with discriminating indices and was demonstrated through worked examples on a narrow hand-built domain (events in the lives of two US Secretaries of State); its authors list the psychological validity of E-MOPs as open, and no quantitative accuracy or human test of CYRUS or IPP was found in these sources.
- **C08.02-K04** (now single-source: the sources are not independent). Kolodner thesis and Kolodner & Barsalou are the same author/lab and both describe CYRUS; the only other source (HyDE, numbers verified) is a dense-retrieval analogue that does not support the CYRUS claim itself.
- **C08.02-K06** (now single-source: the sources are not independent). All four evidence lines are the same Memento paper (arXiv 2508.16153; numbers 59.9/72.2 to 66.6/80.4 and HLE 17.4 to 24.4 verified); one study, so the general claim has no independent support.
- **C08.02-K11** (now single-source: the sources are not independent). Three evidence lines are the same ReasoningBank paper (numbers 48.8/44.1/42.1/40.5 verified, author list mislabelled 'Zhao'); AWM paper is a baseline and never compares against ReasoningBank, so only one independent source.
- **C08.02-K16** (reworded: the sources support less). r=0.717/0.563 and the AIME-25/GPQA remark verified in Evo-Memory only; Dynamic Cheatsheet does not report a similarity correlation and itself shows large gains on AIME-25 (+30) and GPQA-Diamond (+9) for Claude 3.5 Sonnet, so the recurring-structure/low-similarity generalisation is not supported across sources. Corrected claim: In Evo-Memory, ReMem's gain over the History baseline correlates with within-dataset task similarity (Pearson r=0.717 on Gemini 2.5 Flash, 0.563 on Claude 3.7 Sonnet), and low-similarity datasets such as AIME-25 and GPQA show smaller gains there.
- **C08.02-K24** (now single-source: the sources are not independent). Both evidence lines are the same paper (Hu et al., arXiv 2402.17709; 30.2% vs 92% and RFFT >95% on 12-digit verified, but no second study).
- **C08.02-K26** (reworded: the sources support less). Hatalis et al. only say comprehensive benchmarks for CBR-augmented agents remain an open challenge and report only DS-Agent 100%/99%; Wikipedia says nothing on benchmarks, so a universal 'no benchmark yet' rests on one 2025 review. Corrected claim: A 2025 review (Hatalis et al.) states that comprehensive benchmarks for the distinctive capabilities of CBR-augmented LLM agents remain an open challenge, and reports only one figure (DS-Agent 100% development success, 99% one-pass deployment, taken from Guo et al.).
