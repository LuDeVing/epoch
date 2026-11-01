# Case-base maintenance: deep document

*Subfield C08.07. Writer pass over evidence_a-d.jsonl, claims.jsonl (K01-K30) and critique.md. Evidence ids (a01 ... d20) point to the jsonl files in this folder. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Almost all LLM deletion evidence is single-source (one paper, one backbone); read every number with that in mind.*

## 1. What it is

Case-base maintenance is the set of policies that decide what a case-based reasoner keeps, adds, edits, merges and deletes, so that later retrieval stays fast and stays correct. In case-based reasoning (CBR) a "case" is a stored problem with its solution. A system that only adds cases will grow without limit. Maintenance is the other half of learning: what to forget.

Two quantities are traded off:

- **Efficiency.** More cases cost more search time. This is the utility problem (Minton 1990) or swamping problem (Francis and Ram 1993): stored knowledge can cost more to use than it saves.
- **Competence.** The share of target problems the system can solve. Deleting the one case that covers some region of problems loses competence silently (a01).

Leake and Wilson (1998, 2001) frame maintenance along dimensions: what is changed (cases, indexes, similarity, adaptation knowledge), when (continuous, periodic, on demand), and online or offline (a27, b11; snippet only [M]).

For our agent this maps to the Memory section of SCHEMA.md (lessons, class record, planned subgoal library) and to the retain decision in S9 LOOK BACK. The question: when a run ends, what goes in the bank, what comes out, and how do we know the bank still helps? Short answer from the evidence: gate writes on an outcome check, prefer a small curated bank over a growing raw one, and do not trust a model to judge its own reasoning.

Scope. Retrieval and similarity, adaptation, analogical retrieval, and reflection or replay are other subfields in this run. This document covers prune, dedupe, edit, retain and forget policies only.

## 2. History and theories in depth

**Utility problem (1990-1993).** Minton (1990) found that explanation-based learning in PRODIGY produced control rules whose match cost could exceed their search savings, so a system that learned more could run slower. The original paper was not opened. We have it second-hand from a book review and Minton's own reply (d01, d02): rules were monitored at run time and dropped if match cost exceeded estimated savings; utility = average search saved minus cost of use; about 20% of generated rules were kept; speed-ups were 2-3x across three domains (block stacking, robot-and-rooms, job-shop scheduling). Minton said the speed-ups look modest because he capped solve time. Dropping the compression step or the utility evaluation each hurt a lot. Francis and Ram (1993) carried the idea to CBR as swamping; the text was not found online (d03 is a reference line only).

**Competence-preserving deletion (Smyth and Keane 1995).** The founding CBR maintenance paper (a01-a06). Selective retention (delete for good) is separated from selective utilisation (hide at query time). The competence model:

- Coverage(c): the set of target problems that case c solves.
- Reachable(c): the set of cases that can solve c.
- Pivotal: nothing else reaches it. Auxiliary: its coverage lies inside another case's coverage. Support: members of a group with identical coverage. Spanning: links regions that other cases cover.

Deletion order: auxiliary first, then support (largest group first), then spanning, pivotal last (footprint deletion, FD). FUD uses a utility score only to break ties within a class. The footprint is the smallest subset with the same competence as the whole base. The authors state the key assumption: the case distribution must approximate the target distribution, or the model is unreliable (a06).

**Competence models refined (1999-2001).** Smyth and McKenna extended this with coverage groups and relative coverage, and gave an efficient incremental update (b01-b04, c25). Zhu and Yang (1999) argued that FD has no guarantee, and gave a greedy addition policy with a proven bound (c24). Smyth and McKenna's journal version (b12) and Leake and Wilson's framework (b11) were seen as listings only [M].

**Instance reduction in machine learning.** The nearest-neighbour community worked on the same problem as "instance selection": condensation (CNN, IB2) keeps boundary points; editing (ENN, RENN, All k-NN) removes noisy points; Wilson and Martinez (2000) combined both in DROP1-5 (a07-a10). Brighton and Mellish (2002) proposed ICF with reachability and coverage sets (a29, [M]). Delany and Cunningham (2004) applied editing to spam filtering and added concept drift (b10, [M]). Leake and Schack (2018) tried exploration versus exploitation in maintenance, probably with records of deleted cases to test the cost of a deletion later (a30, [M], method inferred from the title).

**LLM era (2023-2026).** Agent memory papers rebuilt the same machinery without naming it. Voyager adds a skill only after self-verification and never prunes (a19). Generative agents never delete and rank by recency, relevance and importance (a25). MemoryBank uses an Ebbinghaus curve (a24). ExpeL edits insights with ADD, EDIT, UPVOTE, DOWNVOTE (a17). Mem0 and Memory-R1 choose ADD, UPDATE, DELETE, NOOP per fact (a22, d10). ACE keeps a playbook with counters and non-LLM dedup (b24). The first controlled study of add and delete rules for LLM agents is Xiong et al. (2025) (a11-a16). The two traditions have barely met: no study compares footprint or coverage pruning with utility pruning on an LLM agent bank (b35; d11 and d12 use coverage only at query time).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Competence-aware deletion beats random and utility-only (property CBR, toy domain) | 50 starting cases, 160 targets, swamping limit 75. Final competence: FD 100%, FUD 100%, random 86%, utility-only 80%. | Smyth and Keane 1995 (a04, c23) | [S] human-era, toy scale |
| Case-base anatomy and minimum base | 20 pivotal, 5 auxiliary, 25 support (7 groups), 0 spanning; minimal competent base 27 cases. At a limit near 25 cases: footprint about 90%, random and utility about 60%. | Smyth and Keane 1995 (a05) | [S] |
| Competence model must match the real task distribution | Assumption stated by authors. | a06 | [S] |
| Greedy competence-based addition is bounded; coverage is concentrated | At least 63% of optimal coverage (set-cover reduction, NP-complete). Travel domain: about 15% of cases give about 50% coverage; 50% of cases give about 85%. | Zhu and Yang 1999 (c24) | [S] |
| Competence model update is cheap | Check only the nearest footprint cases (k). About 5x fewer comparisons at 1400 cases with k=1 (20%). k=5 gives 100% accuracy; k=3 gives 99.6% at 1400 cases. | Smyth and McKenna 2000 (b02, b03) | [S] |
| Utility problem in explanation-based learning | About 20% of rules kept; 2-3x speed-up; utility = savings minus cost; solve-time cap shapes the result. Second-hand. | Minton 1990 via d01, d02 | [S] (original not read) |
| Instance reduction keeps a small share at small loss | 31 datasets, k=3, 10-fold CV. kNN 82.11. DROP3 81.14 at 14.31% storage; DROP2 81.07 (14.03%); DROP5 81.39 (16.09%); CNN 76.48 (26.69%); IB2 76.58; DROP1 72.65 at 8.41%. | Wilson and Martinez 2000 (a08) | [S] older ML, k-NN |
| Reduction under noise | 10% uniform class noise: kNN 82.11 to 78.93. DROP3 80.00 (11.49% kept); DROP2 79.99; CNN 68.14; IB2 67.80; All k-NN 79.98 (64.58% kept). | a09, a10 | [S] |
| Add-all hurts LLM agents vs a small fixed memory | RegAgent 55.48 vs 67.53; EHRAgent 13.05 vs 16.75; AgentDriver 32.32 vs 40.11; CIC-IoT 59.90 vs 71.50. Add-all sizes 4100/2411/2125/1050; fixed 100/100/180/50. GPT-4o-mini. | Xiong 2025 (a11, c01) | [S] for numbers; direction [E] with b31, d04 |
| Strict (outcome-checked) add beats both | strict 70.95 / 38.50 / 51.00 / 85.40 (sizes 2938/1012/1178/904). | Xiong 2025 (a11, c02) | [S] |
| Coarse judges lose most of the gain, sometimes go below fixed | C1/C2/C3: EHRAgent 26.19/32.21/34.66; AgentDriver 36.92/40.01/47.37; CIC-IoT 74.00/68.80/79.50; RegAgent C1 63.18, C2 65.78 (below fixed 67.53), C3 67.35. | Xiong 2025 (b14, c02) | [C] with K03 |
| Experience-following | Output similarity tracks input similarity, Pearson r about 1 under add-all in RegAgent. | Xiong 2025 (a12, b15) | [S] |
| Error propagation | Gap to an error-free memory opens at once and widens over 2000-4000 runs; strict add passes error-free memory in AgentDriver after about 2000 runs. | Xiong 2025 (a13, c03) | [S] |
| History-based deletion with a strict judge | EHRAgent 38.67 to 42.06 (1012 to 784); CIC-IoT 85.40 to 89.60 (904 to 788); AgentDriver 51.00 to 51.81 (1178 to 846); RegAgent 70.95 to 69.80 (2938 to 2286). Rule: delete after n=5 retrievals with low mean downstream utility. | Xiong 2025 (a14, c04) | [S] |
| Periodic pruning | Strict: RegAgent 67.65 (949); EHRAgent 38.59 (302); AgentDriver 50.94 (467); CIC-IoT 80.80 (310). Memory down 60-90%; accuracy flat on two agents, down 3.3 (Reg) and 4.6 (IoT). Combined: EHRAgent 42.34 at 248; CIC-IoT 85.50 at 188. | Xiong 2025 (a14, c05; layout fixed per critique) | [S] |
| Retained records are more accurate than deleted ones | C1 EHRAgent retained 44.1% correct vs deleted 36.3%; C3 54.8 vs 48.2; CIC-IoT C1 78.9 vs 56.7. | Xiong 2025 (b17) | [S] |
| Hard cap and distribution shift | Caps 100/180 records: managed memory still beat fixed; performance converges as cap grows. Shift: strict add stays near no-shift level. | Xiong 2025 (a16, b18) | [S] |
| Curated cheatsheet beats full-history append | AIME 2024 (30 items; 1 item = 3.3 points): Claude 3.5 Sonnet baseline 23.3, full-history 26.7, retrieval-only 43.3, DC-RS 46.7, DC-Cu 50.0. GPT-4o baseline 20.0, full-history 6.7, DC-Cu 36.7, DC-RS 40.0. | Suzgun 2025 (b31, c10; critique corrections) | [S] |
| Curation gains are model dependent | Haiku AIME 10.0 to 36.7 (Cu) and 30.0 (RS); GPT-4o GPQA-Diamond flat (table 57.1; text 58.1, inconsistent). Loosely related retrieval confuses. | Suzgun 2025 (b32, c11) | [S] |
| Unfiltered failures hurt plain memory; a refining method stays robust | Baselines lost accuracy with success+failure storage; ReMem (Refine step) stayed best. Gemini 2.5 Flash single-turn ReMem avg 0.65, ExpRAG about equal. | Evo-Memory (c13, d04) | [S] |
| Failure lessons help when distilled | WebArena-Shopping, Gemini-2.5-flash: ReasoningBank 46.5 (success only) to 49.7 (with failures); AWM 44.4 to 42.2; Synapse 40.6 to 41.7. Overall +8.3/+7.2/+4.6 over no memory on three backbones. | ReasoningBank (b26, c21) | [S] |
| In-place revision beats append and success-only | Reflexion-style adjustment beat the second-best update policy by +0.7 reward and 14 fewer steps at the last group. | Memp (c15, d09) | [S] |
| Insight votes (ExpeL) | New insight starts at 2; removed at 0. HotpotQA: ReAct 28.0, hand-crafted 32.0, with reflections 29.0, gpt-3.5 insights 32.0, full 39.0. ALFWorld: ReAct 40.0, random retrieval 42.5, reasoning-similarity 48.5, task-similarity 59.0. Vote pruning itself not ablated. | ExpeL (a17, c16) | [S] |
| Insights-only vs retrieval-only | HotpotQA 36 vs 31 vs full 39; ALFWorld 50 vs 55 vs full 59; WebShop 37 vs 38. | ExpeL (a18) | [S] |
| Outcome-weighted curation of self-made trajectories | ALFWorld 0.73 to 0.89 (bootstrap), 0.91 (+database curation), 0.93 (+exemplar). Wordcraft 0.55 to 0.64 to 0.72 (exemplar). InterCode-SQL 0.75 to 0.79 to 0.82. Most gain in first 25% of added tasks. | Sarukkai 2025 (c07-c09) | [S] |
| Rewriting a whole context collapses it | ACE on AppWorld: 18,282 tokens at 66.7, next step 122 tokens at 57.1 (baseline 63.7). | ACE (b23) | [S] |
| Delta updates with non-LLM dedup | AppWorld: ReAct 63.7; ACE offline 72.0; incremental vs none 70.3 vs 56.9 (base 53.3). | ACE (b24, d14) | [S] |
| Dedup threshold and prune trigger are flat on a non-agent task | FiNER: base 70.7; dedup 50/70/90% gives 77.0/73.9/78.6; prune trigger 10K/50K/100K tokens gives 78.6/78.4/78.3. No on/off arm. | ACE (d14) | [S] |
| Bank size saturates early | Memento DeepResearcher F1: K=0 59.9, K=1 63.6, K=4 64.5, K=8 64.1, K=32 63.9. No learning-curve drop over about 3k items. OOD gain 4.7-9.6 points. | Memento (a23, b29, b30) | [S] |
| Neighbour update at insert time beats append | A-Mem LoCoMo multi-hop F1 27.02 vs 21.35 without evolution vs 9.65 without links and evolution. | A-Mem (d13) | [S] |
| Memory systems trade accuracy for cost | LoCoMo judge: RAG about 61, Mem0 67, Mem0g 68+, full context about 73. p95 latency 1.44 s vs about 17 s (about 91-92% lower); over 90% fewer tokens. | Mem0 (a22, b33) | [S] |
| Learned manager beats prompted manager | LLaMA-3.1-8B PPO: F1 41.0 vs 34.5; GRPO 45.0 vs 37.5. Distilling 60 retrieved memories +1.7 (PPO) and +4.0 (GRPO) F1. | Memory-R1 (d10) | [S] |
| Wrong demo labels: harmful for generation, mild for classification | Generation (Llama-2-7B-Chat): SciQ 60% noise TopK EM 29.31 to 48.06 after local-perplexity filter (+18.75); NQ random 28.21 to 42.00 (+13.79). Classification: random labels cost 0-5%, average 2.6%; multi-choice 1.7%. | Gao 2024 (d06); Min 2022 (d07) | [E] on the split by task type |
| Selection matters less with many shots | Banking-77: BM25 gain over random 51.5 points (1-shot) to 4.9 (1500-shot). SAMSum: retrieval sometimes worse than random. | Bertsch 2024 (d08) | [S] |
| Many shots can overwrite priors | Flipped and abstract labels approach default-label performance as shots grow. | Agarwal 2024 (d20) | [S] |
| Coverage-style selection works at query time | Set-level BSR beats independent ranking by up to 17 points on compositional tasks; vote-k beats random pool by 12.9% (18 shots) and 11.4% (100) relative. | Gupta 2023 (d11); Su 2022 (d12) | [S] each; query-time only |
| Outcome-grounded judges are usable | Judge accuracy vs oracle 74-93% (WebArena GPT-4V 80.6, Qwen-VL 68.0); gains up to 29% relative (WebArena), about 75% (iOS). | Pan 2024 (d18) | [S] |
| Same-model self-judging of reasoning is unreliable | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1. | Huang 2024 (d19) | [E] with SCHEMA G2 sources |
| Forgetting rules are unablated | MemoryBank (R = exp(-t/S)), SAGE, MemoryOS (heat eviction, cap 100): none compares against recency or no forgetting. SAGE compares memory vs none only. | d15, d16, d17 | untested |
| Retrieval speed is not the limit | A-Mem 0.31 us at 1k to 3.70 us at 1M notes. Best-case embedding capacity: 500k docs at 512 dims; 4M at 1024. Real models fail LIMIT earlier. | d13, d05 | [S] |
| Generative agents reflection | TrueSkill: full 29.89; no reflection 26.88; none of memory, planning, reflection 21.21 (N=100 raters). Not a maintenance claim. | Park 2023 (a25) | [S] |

## 4. Mechanisms and models

Written so an engineer can build each piece.

### 4.1 Competence model (Smyth and Keane)

Needs: a set of cases C, a set of probe problems P that approximates future tasks, and a function solves(c, p) that says whether case c solves p.

1. For each case c, Coverage(c) = {p in P : solves(c, p)}.
2. Reachable(p) = {c in C : solves(c, p)}. Reachable(c) for a case treats c itself as a probe.
3. Classify:
   - pivotal: Reachable(c) minus c is empty.
   - auxiliary: another reachable case has a coverage superset of c.
   - support: c shares identical coverage with others (group them).
   - spanning: everything else.
4. To shrink to size N: delete auxiliary first; then support, taking from the largest group and keeping one per group; then spanning; pivotal last. If a pivot must go, drop the one with the largest reachable set or smallest coverage.
5. FUD: inside a class, break ties by a utility score (retrieval count times outcome).

For an LLM bank, "solves" is expensive: it means re-running the model with the case in context on each probe. Cheap proxy: embedding coverage (BERTScore-Recall set coverage, d11) against a held-out query set. Nobody has tested this proxy for deletion (K27). The exact version costs |C| x |P| model calls; sample P.

### 4.2 Verified retain gate (Xiong "strict" add)

At end of a run, retain the (task, trajectory, result) record only if an outcome signal says it was correct. Signals ranked by reliability in the evidence: ground truth or unit test (strict); a judge fine-tuned on about 300 correct trajectories (C3, close to strict); a prompted judge (C1/C2, can fall below no memory).

```
on_run_end(task, traj, answer):
    ok = verifier(task, answer)                      # code or ground truth where it exists
    if ok is None: ok = tuned_judge(task, traj) >= tau   # only if calibrated
    if ok: bank.add(task, traj, answer, uses=0, wins=0)
```

### 4.3 History-based deletion (utility after use)

Keep per record: n_retrieved and the sum of downstream utility (did the run that used it succeed). Delete when n_retrieved >= 5 and mean utility is below a threshold. This is Smyth and Keane's utility term made outcome-based. Xiong used it with a strict evaluator. With a coarse evaluator the effect was mixed (EHRAgent C1 25.91 to 33.55, CIC-IoT C1 74.00 to 73.70). Sarukkai's version: Q(traj) = mean outcome of tasks where it was retrieved, weighted by retrieval frequency; keep the best per task (c09).

### 4.4 Periodic deletion

Every window, delete records retrieved fewer than a threshold number of times. Cuts memory 60-90% with small loss in some agents (a14). Cheap, no judge needed. Risk: removes rarely used pivotal cases (the Smyth and Keane failure mode); IoT lost 4.6 points.

### 4.5 Case editing for noise (Wilson and Martinez; Gao)

Remove or relabel a case whose label disagrees with its nearest neighbours (ENN / All k-NN). LLM version (Gao's local perplexity ranking): replace each retrieved candidate by a cleaner neighbour. Recovery on generation with 60% noise: +13.8 to +18.8 EM (d06). Use only for generation or free-form reasoning; for classification the model is robust to wrong labels (d07).

### 4.6 Insight store with votes (ExpeL)

Records: text insight, importance count starting at 2. Operators after each batch: ADD, EDIT (+1), UPVOTE (+1), DOWNVOTE (-1). Remove at 0. The authors say this guards against lessons built from lucky successes (a17). Vote pruning has not been ablated.

### 4.7 Delta update, not rewrite (ACE)

Never ask the model to rewrite the whole notes file. Keep items with ids and counters. The model proposes small deltas. Code merges, bumps counters and removes near-duplicates by embedding similarity. Prune only when length passes a trigger. Rewrites caused the collapse from 18,282 to 122 tokens (b23).

### 4.8 Merge at insert (Mem0 / A-Mem)

For each new fact, retrieve top-k similar stored items; decide ADD, UPDATE (merge), DELETE (contradicted), NOOP (duplicate). A-Mem also rewrites the neighbours' context. Gains: A-Mem multi-hop 27.02 vs 21.35. Mem0 buys cost, not accuracy (full context still best, 73 vs 67). Memory-R1 shows a prompted manager misreads additions as contradictions and issues wrong deletes; a trained one avoids it (d10).

### 4.9 Utility = savings minus cost (Minton), in LLM terms

A stored item costs something each time it is in the prompt (tokens, distraction, copied errors) and saves something when it helps. Keep an item only if measured mean saving exceeds measured cost. The mapping is plausible but unmeasured for LLMs (K20).

### 4.10 Competence concentration

Zhu and Yang: a small core carries most coverage (about 15% of cases give about 50%). Greedy selection by marginal coverage gain is within 63% of optimum. Engineering use: rank cases by marginal coverage on a probe set, find the knee of the curve, stop adding there.

## 5. What holds up

**Supported by two or more sources.**
- Do not append raw experience without a gate. Xiong (add-all below fixed), Dynamic Cheatsheet (full history 6.7 vs baseline 20.0 on GPT-4o), Evo-Memory (unfiltered failures hurt plain baselines) point the same way, on different tasks and backbones. [E] for the direction, [S] for each size.
- Wrong stored answers get copied. Xiong's experience-following (r about 1) and Dynamic Cheatsheet's error clusters ("one bad heuristic poisons neighbours", c11) describe the same effect. Gao shows it in in-context learning for generation tasks.
- Small banks saturate. Memento (K=4 best, no gain beyond), Memp (retrieving too many lowers performance), Xiong (caps 100-180 near unbounded), ACE (10K vs 100K prune trigger 78.6 vs 78.3), Bertsch (selection gap shrinks to 4.9 at 1500 shots). [E] that bigger is not better beyond a small number.
- Same-model judging of reasoning is unreliable (Huang); outcome-grounded judges are usable (Pan). Consistent with SCHEMA G2 and G5.

**Contested.**
- Sensitivity to retain-judge accuracy. Xiong: coarse judges lose 4-12 points vs strict, and can fall below fixed. ReasoningBank: success stayed in a narrow band (about 47.6-53) as simulated judge accuracy fell from 100% to 50%, with a real judge at 72.7%. Plausible reconciliation: ReasoningBank stores distilled strategies, Xiong stores raw trajectories that get copied. Not tested at fixed task (K03).
- Whether deletion helps. History-based deletion helped EHRAgent and CIC-IoT, and was neutral or negative on RegAgent. Periodic pruning hurt IoT (strict). No policy dominates (K04, K05).
- Whether size causes swamping. Memento saw none up to about 3k items; Xiong saw damage at 2k-4k records from add-all. The difference is the quality gate, not size (critique).
- Whether wrong labels matter. Min: no (classification). Gao: yes (generation). Resolved by task type.

**Failures and weak spots.**
- Dedup threshold: 77.0 / 73.9 / 78.6 at 50/70/90%. A dip at 70% shows noise the size of the claimed effects (d14).
- Forgetting by Ebbinghaus decay, heat or usage: no ablation in MemoryBank, SAGE or MemoryOS (K22, K30). Unproven.
- Curation on GPQA-Diamond for GPT-4o is flat; small models curate badly (Haiku mixed). AIME 2024 has 30 items; no confidence intervals.
- No study at equal prompt tokens. Added memory means added tokens in nearly every paper.
- Classic CBR numbers (Smyth and Keane, Wilson and Martinez, Zhu and Yang) were not re-checked by the cross-checker. The Smyth and Keane base has 50 cases.
- Xiong is the single source for LLM deletion: one backbone (GPT-4o-mini), four agents, one lab.
- Dynamic Cheatsheet and ExpeL use the model as curator. Whether gains come from curation or from extra tokens is not separated.

**Worked:** strict retain gate; history-based deletion with a strict judge; delta updates with non-LLM dedup; distilled failure lessons (ReasoningBank); in-place revision (Memp); neighbour-consistency filtering for noisy generation banks (Gao); outcome-weighted exemplar curation (Sarukkai).

**Did not work or untested:** add-all; prompted coarse judges; full rewrite of notes (collapse); raw failure trajectories appended to plain baselines; pruning without a quality judge (IoT -4.6); Ebbinghaus forgetting (untested); skill-library pruning (never studied).

## 6. Language models

- **They copy the nearest stored output.** In Xiong's RegAgent, output similarity tracked input similarity at r about 1 with a large memory. A bad stored record is a bad answer waiting. A small fixed memory kept the agent relying on its own reasoning.
- **The quality gate swings results by tens of points.** EHRAgent: add-all 13.05, fixed 16.75, strict 38.50. AgentDriver: 32.32 / 40.11 / 51.00. CIC-IoT: 59.90 / 71.50 / 85.40.
- **A judge fine-tuned on 300 correct trajectories nearly matches ground truth** (EHR 34.66 vs 38.50; AgentDriver 47.37 vs 51.00; IoT 79.50 vs 85.40). A prompted judge does not.
- **Appending history can be worse than nothing.** GPT-4o on AIME 2024: baseline 20.0, full history 6.7, curated 36.7-40.0. Claude 3.5 Sonnet: 23.3, 26.7, 50.0.
- **Distilled beats raw, but raw retrieval is a hard baseline.** Evo-Memory (AIME, GPQA, MMLU-Pro, ToolBench; Gemini 2.5 and Claude 3.7; shared top-4 retriever): plain ExpRAG is about equal to the best evolving method on single-turn sets; gains moderate; gain tracks task similarity (r 0.56-0.72). Claude 3.7 single-turn averages sit at 0.48-0.59, with Mem0 lowest at 0.49 against baseline 0.54. On multi-turn embodied tasks refinement wins (AlfWorld 0.92 vs ExpRAG 0.74).
- **Raising K stops helping early.** Memento K=4 best; more is flat or slightly worse.
- **Weak models curate badly.** Haiku and GPT-4o-mini gained less than Sonnet in Dynamic Cheatsheet. Memory built by a stronger model helped a weaker one (Memp).
- **Whole-context rewrite is dangerous.** ACE: 18,282 to 122 tokens, accuracy 66.7 to 57.1, below the 63.7 baseline.
- **Self-judgment is poor; outcome-checks are fine.** Huang: GPT-4 GSM8K falls 95.5 to 89.0 over two self-correction rounds. Pan: judges are 74-93% accurate against oracle checks and give large downstream gains.
- **Wrong labels depend on task.** Classification barely moves (0-5%). Generation drops hard; Gao's local filter recovers 13.8-18.8 EM points on Llama-2-7B-Chat. Newer, larger models were not tested; Agarwal shows many shots can overwrite priors, which cuts both ways.
- **Selection matters less as shots grow.** BM25 over random: 51.5 points at 1-shot, 4.9 at 1500-shot.
- **Cost.** Mem0 about 67% vs full context about 73% judge score, but 91-92% lower p95 latency and over 90% fewer tokens. Pruning is a cost tool first.
- **Learned managers beat prompted ones.** Memory-R1: +6.5 F1 (PPO) and +7.5 F1 (GRPO) from a trained manager; the untrained one issues false DELETEs.

Caveat across all of the above: single runs, no intervals, small test sets, mostly one model family per paper.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| **No ungated writes.** Nothing enters the lesson store or bank unless an outcome signal passed (code check, unit test, held-out example, ground truth). Failed or unchecked runs may be stored only as distilled lessons marked "failure", never as raw trajectories. | memory + S9 + G3 | [E] direction (Xiong, Dynamic Cheatsheet, Evo-Memory); sizes [S] | a11, c01, c02, b31, c10, c13, d04 |
| **Never let the model judge its own reasoning to decide retention.** Gate on code or a verifier; a model judge is only a hint. Matches G2 and G5. | memory + G5 | [E] | d19, d18, a11, c02 |
| **Keep the bank small and curated; do not grow it for its own sake.** Cap lessons per class; expect saturation near a handful of retrieved items (K about 4). | memory | [E] | a23, b29, d09, a16, d14, d08 |
| **Update by delta, never by full rewrite.** Notes are edited by small operations with ids; code merges and dedupes. | memory + S9 | [S] (ACE); cheap, consistent with G5, adopt as engineering rule | b23, b24 |
| **Lessons shown after the first attempt** (already in SCHEMA) stays; loosely related retrieval confuses. | memory | [E] with fixation literature | c11, d04 |
| **Log per-item use and outcome** (n_retrieved, wins when used). Every deletion rule below needs it and it costs nothing. | memory + run log | [D] enabler | a14, c09 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| History-based deletion: drop a lesson after n=5 retrievals if mean downstream win rate is below threshold | memory | [S] | a14, c04 |
| Competence-style deletion: protect pivotal lessons, delete auxiliary and support lessons first | memory | [S] human-era toy; untested on LLMs | a02-a05, K07 |
| Judge strictness: add-if-verified with a verifier vs a model judge vs none | memory + G5 | [C] | K03, a11, b27, d18 |
| Failure lessons vs success-only under a size cap, and the share of failures to keep | memory | [S] | b26, c13, d09 |
| In-place revision of a lesson on failure (Memp style) vs append | memory + S5/S9 | [S] | c15, d09 |
| Neighbour-consistency filter on a bank with wrong cases (generation items) | memory | [S] | d06, d07 |
| Votes on lessons (ExpeL) vs append-only | memory | [S] | a17 |
| Cheap rule-based abstraction vs LLM abstraction of lessons | memory | [S] | a20 |
| Dedup/merge on vs off | memory | [S]; effect may be only cost | d14, a22 |
| Decay or usage forgetting vs recency vs none | memory | untested | d15-d17 |
| Cached fixed set vs per-query retrieval at equal tokens | memory | [S] | d08 |

## 8. Concrete tests on our bench

All arms get the same total prompt tokens (lessons included); count setup and curation calls as spent tokens (G7). Each test uses at least 3 seeds and reports a bootstrap interval. Stream order is shuffled per seed.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Stream of 300+ ARC-style or BRAINTEASER items with a code check; bank used after the first attempt | (a) add-all lessons, (b) fixed 20-lesson window, (c) add-if-verified | Accuracy on a held-out last third; lesson tokens in prompt | c > b > a by several points; a may fall below no-memory (Xiong, Dynamic Cheatsheet pattern) |
| T2 | Same stream | Retain judge: verifier vs model self-judge vs tuned or cross-model judge vs none | Accuracy; retained-lesson precision | Verifier best; self-judge near add-all (Huang). Settles K03 |
| T3 | Stream with 20% injected wrong lessons | No cleaning vs neighbour-consistency edit (Gao) vs history deletion | Accuracy; share of wrong lessons left | Cleaning recovers part of the loss on free-form items; little on multiple-choice |
| T4 | Stream of 1000+ items, cap sweep 25/50/100/unbounded | add-if-verified at each cap | Accuracy vs bank size (find the knee) | Flat above about 50-100 lessons |
| T5 | Same stream, cap fixed at 50 | recency eviction, usage/heat eviction, history-based deletion, competence-style (embedding coverage on probe set), random | End accuracy; retained-pivotal share | Utility and competence beat random; difference to recency small |
| T6 | Same stream | success-only vs distilled failure lessons vs raw failures; failure share 0/25/50% | Accuracy | Distilled failures help a little; raw failures hurt |
| T7 | Notes file edited by the model | Full rewrite vs delta update + code merge | Accuracy; notes length over time | Rewrite collapses at some step; delta stable |
| T8 | Stream | Dedup on vs off, 5 seeds | Accuracy; tokens | No accuracy difference; cost saving |
| T9 | Non-agentic reasoning set (AIME / GPQA slice) | Plain top-k retrieval of all cases vs pruned bank at same k (Evo-Memory style) | Accuracy | Pruned >= plain; if not, plain retrieval stays the default |
| T10 | Bank grown 10x and 100x with synthetic near-duplicates | Plain retrieval vs retrieval with dedup | Retrieval precision at k; accuracy | Precision decays with size; dedup restores it (swamping beyond 3k) |

## 9. What does not transfer, and why

- **Footprint deletion's 100% competence.** It came from a 50-case toy property domain where coverage is exactly computable by nearest neighbour. For an LLM, "solves" is a stochastic model run, and the case distribution does not mirror future tasks. The guarantee does not carry over; only the idea (protect pivotal cases) does.
- **Retrieval-speed motivation.** Swamping in the 1990s meant slow linear search. Vector indexes keep latency flat (0.31 us to 3.70 us from 1k to 1M notes). For LLMs the cost is prompt tokens and distraction, not search time.
- **DROP storage figures (14%).** k-NN classifiers with fixed features and a distance metric. Our model reads cases; it does not match them by k-NN.
- **Minton's speed-ups.** A search-control setting with match-cost accounting, second-hand, with a time cap that shapes the numbers.
- **Mem0, MemoryBank and MemoryOS results.** Dialogue-memory benchmarks (LoCoMo): facts about people and time. Our items are problem-solving lessons. Their forgetting rules also lack ablations.
- **Voyager's unbounded library.** Embodied code skills verified by execution; the library never needed pruning in a 160-iteration run.
- **Xiong's memory sizes (1000-4000 records).** Our lesson bank is one line per class, likely tens to hundreds. The swamping regime may never be reached; the gate matters more than the delete rule.
- **Human-expert maintenance.** Leake and Wilson's dimensions presume a human maintainer and long deployment; our bank is rebuilt per benchmark run.
- **Wrong-label robustness in classification (Min).** Does not carry to free-form reasoning (Gao).
- **Generative agents' reflection ablation.** Believability of a social simulation, not a maintenance result.

## 10. Open questions

1. At equal prompt tokens, does verified-retain with deletion beat a plain fixed-size window on a non-agentic reasoning benchmark? No one has run it.
2. How accurate must the retain judge be before add-if-verified beats fixed memory? Reconcile Xiong and ReasoningBank on one task.
3. Do competence rules (delete auxiliary and support, keep pivotal) work with embedding-defined coverage? Needs a cheap definition of "solves".
4. Does swamping appear at 10x to 100x bank size, and how does retrieval precision decay? Memento stops near 3k; speed is not the limit; accuracy is unmeasured.
5. Is Delany-Cunningham case editing or Brighton-Mellish instance selection useful for LLM few-shot banks with wrong labels, beyond Gao's mechanism?
6. Does Leake and Schack exploration-versus-exploitation maintenance, or usage-based forgetting, beat recency and Ebbinghaus decay?
7. Does merge/dedup change accuracy or only cost?
8. Do Xiong's results reproduce with a stronger backbone and a different agent family? Nobody re-ran add-all vs strict vs fixed.
9. How many failures to keep under a cap? In-place revision vs append?
10. Do Minton's utility numbers map to LLM context cost? Francis and Ram 1993 is unread.
11. Is the gain from curation (Dynamic Cheatsheet, ExpeL) the curation, or the extra tokens? Neither paper controls tokens.
12. Do the judge results hold at 2026 frontier scale? All judge-sensitivity data is from small or mid models.

## 11. Sources

[V] opened and read; [M] snippet, listing or second-hand only.

- [V] Smyth and Keane (1995) Remembering to forget. https://www.ijcai.org/proceedings/1995/50 ; copy https://folk.idi.ntnu.no/agnar/CBR%20papers/smyth-keane-remembering-95 (a01-a06, c23, c26; not re-opened by the cross-checker)
- [V] Smyth and McKenna (2000) Efficient procedure for updating a competence model. https://rd.springer.com/content/pdf/10.1007/3-540-45164-1_37.pdf
- [V] Zhu and Yang (1999) Remembering to add. https://ijcai.org/proceedings/1999/35 (not re-opened by the cross-checker)
- [V] Wilson and Martinez (2000) Reduction techniques for instance-based learning algorithms. https://link.springer.com/content/pdf/10.1023/A:1007626913721.pdf (figures not re-verified)
- [V] Zito-Wolf (1991) Review of Minton. https://link.springer.com/content/pdf/10.1007/BF00114164.pdf
- [V] Minton (1991) Reply. https://link.springer.com/content/pdf/10.1023/A:1022662621851.pdf
- [V] Ram and Leake (1995) Goal-driven learning (draft; reference line only). https://sites.cc.gatech.edu/fac/ashwin/papers/er-95-03.pdf
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413
- [V] Zhang et al. (2025/2026) Agentic Context Engineering (ACE). https://arxiv.org/abs/2510.04618
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Park et al. (2023) Generative agents. https://arxiv.org/abs/2304.03442
- [V] Zhong et al. (2024) MemoryBank. https://arxiv.org/abs/2305.10250
- [V] Sarukkai et al. (2025) Self-generated in-context examples. https://arxiv.org/abs/2505.00234
- [V] Wei et al. (2026) Evo-Memory. https://arxiv.org/abs/2511.20857
- [V] Fang et al. (2025) Memp. https://arxiv.org/abs/2508.06433
- [V] Xu et al. (2025) A-Mem. https://arxiv.org/abs/2502.12110
- [V] Review of CBR for LLM agents (2025). https://arxiv.org/abs/2504.06943
- [V] Weller et al. (2026) Theoretical limitations of embedding-based retrieval. https://arxiv.org/abs/2508.21038
- [V] Gao et al. (2024) Noise robustness of ICL for text generation. https://arxiv.org/abs/2405.17264
- [V] Min et al. (2022) Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837
- [V] Bertsch et al. (2024) ICL with long-context models. https://arxiv.org/abs/2405.00200
- [V] Yan et al. (2025) Memory-R1. https://arxiv.org/abs/2508.19828
- [V] Gupta, Gardner, Singh (2023) Coverage-based example selection. https://arxiv.org/abs/2305.14907
- [V] Su et al. (2022) Selective annotation (vote-k). https://arxiv.org/abs/2209.01975
- [V] Zhang et al. (2025) SAGE. https://arxiv.org/abs/2409.00872
- [V] Kang et al. (2025) MemoryOS. https://arxiv.org/abs/2506.06326
- [V] Pan et al. (2024) Autonomous evaluation and refinement of digital agents. https://arxiv.org/abs/2404.06474
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/abs/2404.11018
- [M] Minton (1990) Quantitative results concerning the utility of EBL. https://doi.org/10.1016/0004-3702(90)90001-U
- [M] Francis and Ram (1993) The utility problem in CBR. https://www.aaai.org/ (text not found)
- [M] Leake and Wilson (1998) Categorizing case-base maintenance (EWCBR)
- [M] Leake and Wilson (2001) Maintaining case-based reasoners. https://doi.org/10.1111/0824-7935.00162
- [M] Smyth and McKenna (1999) Building compact competent case-bases (ICCBR)
- [M] Smyth and McKenna (2001) Competence models and the maintenance problem. https://doi.org/10.1111/0824-7935.00162
- [M] Brighton and Mellish (2002) Advances in instance selection for instance-based learning algorithms
- [M] Delany and Cunningham (2004) Case-base editing in a spam filtering system. https://typeset.io/pdf/an-analysis-of-case-base-editing-in-a-spam-filt
- [M] Leake and Schack (2018) Exploration vs. exploitation in case-base maintenance (title only)
