# Retention policy: deep document

Subfield C08.08. Question: which new cases should a case-based reasoner store? Schema part: S9 LOOK BACK and memory (SCHEMA section 5).
Evidence ids (a01..d20) refer to evidence_a-d.jsonl in this folder. Claim ids (K01..K24) refer to claims.jsonl. Sibling subfields (not repeated here): 07 case-base maintenance, 09 retrieval as a bandit, relevance-based fate of memories, prioritised memory access, replay (Dyna family), consolidation / complementary learning systems.

## 1. What it is

Retention is the fourth R of the case-based reasoning cycle (retrieve, reuse, revise, retain). After a problem is solved, the system decides what to keep, in what form, how to index it, and how to merge it into the case base (a01, Aamodt and Plaza 1994). Four sub-tasks: extract, index, integrate, test.

The policy has two halves.
- Write gate: which new episodes enter the bank. Options: everything (add-all), only verified successes, only novel or uncovered cases, successes plus failures, distilled lessons instead of raw episodes.
- Forget rule: which stored cases leave when the bank is full or harmful. Options: random, by use-utility, by coverage role (competence), by age, by later-retrieval outcome.

Why it matters for a frozen-model agent: the agent cannot train. Its only learning channel is what it writes to a case bank and shows later. A bad write gate fills the bank with wrong or redundant cases. The model copies the nearest stored case (K08), so wrong cases spread.

Scope note. This folder covers the write gate and the forget rule. Retrieval scoring is subfield 09; maintenance of an existing bank (merge, repair) is 07. The two overlap on deletion; we cover deletion only where it is a retention decision.

## 2. History and theories in depth

**1994: the framework.** Aamodt and Plaza (a01) define Retain. It lists what could be stored (problem descriptors, solution, justification, even failures as separate cases) but gives no rule for what to skip. Index strength is raised when a feature led to a good retrieval and lowered when it led to a bad one. No experiments.

**1990: the utility problem.** Minton (a05, known only via Smyth and Keane; original not opened). Learned knowledge costs search time. Utility = (application frequency x average savings) - match cost. Delete items with negative utility.

**1991: instance-based learning.** Aha, Kibler and Albert (a27, memory only, not opened). IB2 stores an instance only if the current memory misclassifies it. IB3 drops instances that prove poor predictors. This is the first "store only if not already covered" rule. Treat as a pointer.

**1995: competence-preserving deletion.** Smyth and Keane (a02, a03, a04, a06). They name the swamping problem (a big bank slows retrieval). They define the competence model: coverage of a case = target problems it can solve; reachability of a target = cases that can solve it. Cases fall in four classes: pivotal (only they cover some problem), auxiliary (fully subsumed by another), spanning (link otherwise separate regions), support (groups that cover the same region). Footprint deletion drops in the order auxiliary, support, spanning, pivotal. Footprint-utility deletion (FUD) uses utility inside each class.

**2001: case addition.** Yang and Zhu (a07, a08). Reverse the view: pick cases to add, greedily by largest extra coverage. A proven coverage bound holds, and it is cheaper than deletion. Needs the whole candidate pool in advance.

**2005: noise breaks pivotal rules.** Pan, Yang, Pan and Li (a09). Rare outliers look pivotal, so Smyth-Keane keeps noisy cases. Their kernel method picks statistically meaningful pivotal cases. Numbers only in figures.

**2023 to 2024: LLM agents with case banks.** Voyager (c24) admits a skill only after code self-verification. ExpeL (a25, b21, c15, c16, d08) keeps successes in a recall store and extracts insights from success/failure pairs. Reflexion (c14) keeps bounded reflections per task. AWM (a23, a24, b22, c13) induces workflows from judged-correct runs and filters duplicates and invalid actions.

**2025: the first retention studies on LLM agents.** Xiong et al. (a16-a19, b05-b08, c05-c09, d10, d11) test add-all, quality-gated add, and three deletion rules on four agents. Memento (a20-a22, b16, b17, c21, c22) stores every case and filters at read time. ReasoningBank (c10-c12, d09) stores distilled strategies from successes and failures with a self-judge. Sarukkai (b11-b13, d15) grows a success-only bank and curates it by later-use utility. Dynamic Cheatsheet (c17, c18) rewrites a compact sheet. ReMe (b09, b10, d13), Evo-Memory (c19, c20, d16), Mem0 (a26, c23), LifelongAgentBench (d17), ACE (d18).

**2026: formal and negative results.** CASCADE (a10-a15, b01-b04, c01-c04, d06, d07) gives a regret theory where retention controls the coverage gap, and a success-only rule. Zhang et al. (b14, b15, d01-d05) show that LLM rewriting of a memory degrades it over a stream. SEDM (d12) admits memory by paired replay. MemRL (d14) learns a Q-value per case. Dual-memory (b18), EvoSC (b19), ExpHarness (b20).

**Competing theories in one line each.**
1. Store only what is verified true (CASCADE, AWM, Voyager). Risk: loses traps, discards failure signal.
2. Store everything and filter at read time (Memento, MemRL). Risk: bank grows; retriever swamped.
3. Store only what is not covered (IB2, Yang and Zhu). Risk: untested on LLMs.
4. Store distilled lessons (ReasoningBank, ExpeL insights, DC). Risk: rewriting decay (Zhang).
5. Store raw episodes and never rewrite (Zhang's recommendation). Risk: unbounded context.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Add-all is worse than a small fixed seed memory on all four agents | RegAgent 67.53 to 55.48; EHRAgent 16.75 to 13.05; AgentDriver 40.11 to 32.32; CIC-IoT 71.50 to 59.90 (drops 3.7 to 12.1 points); memory 4100/2411/2125/1050 records | Xiong 2025, Table 1 (a17, b06, c05) | Established (one paper, four agents; K01) |
| Gate quality orders results: strict oracle > fine-tuned judge C3 > coarse judges C1/C2 | Strict 70.95 / 38.50 / 51.00 / 85.40; C3 67.35 / 34.66 / 47.37 / 79.50; C1 63.18 / 26.19 / 36.92 / 74.00; C2 65.78 / 32.21 / 40.01 / 68.80 (RegAgent / EHR / AgentDriver / CIC-IoT). C3 = judge tuned on only 300 trajectories | Xiong 2025 (a17, c05) | Established (K02) |
| Coarse judges beat a fixed seed bank only half the time | 6 of 12 coarse cells above fixed; strict above fixed in 4 of 4; add-all below fixed in 4 of 4 | Xiong Table 1 recount (d10) | Established as a count; break-even judge accuracy unknown |
| Any success-only bank gives most of the gain; the learned retriever adds about 3 points | Qwen3-32B, 12 tasks, 5 seeds: zero-shot 48.33; NP-CBR (retain successes, similarity retrieval) 63.76; CASCADE 66.68 (+18.35 absolute, 38% relative). Qwen3-8B 43.22/58.44/60.84; Qwen3-14B 48.33/62.81/65.10 | CASCADE (a12, a13, b03) | Established that a bank helps; retention rule itself not ablated (K03) |
| CASCADE gains vary widely per task | +51.2 (MIMIC-IV-MR 12.79 to 63.98), +36.9 (MUD), +25.4 (RCA), +21.1 (CMDL), +20.8 (DDXPlus), +18.0 (Banking77), +13.4, +11.6, +10.5, +5.4, +3.7, +2.1 (LFD). Median +15.7. Abstract "20.9%" undefined in text | CASCADE (d06) | Established (K19). Quote 18.35 points and the spread |
| Always retaining the ground-truth case hurt 4 of 12 tasks | MIMIC-MR, MIMIC-MSR, CMDL, LFD got worse; cause: retriever could not manage the larger diverse bank in limited steps | CASCADE suppl. C.5 (a15, b02, c03, d07) | Established as an observation; cause is the authors' reading |
| Targeted label spending beats random placement | Discovery trigger: +8.83% (exploit), +8.73% (UCB), +5.61% (random) relative to standard CASCADE | CASCADE (d07) | Single source; ground-truth labels, not a self-gate |
| Novelty-only (coverage-greedy) addition is far more compact than random | Towers of Hanoi, 6561 problems: 200 random cases cover 86% (5649); greedy needs 58 for 100%; 1 case 12%, 5 cases 50%, 10 cases 73%, 20 cases 90%, 30 cases 96% | Yang and Zhu 2001 (a07, a08) | Single source, synthetic, pre-LLM (K05) |
| Competence deletion beats utility and random deletion | Limit 75 cases, 160 targets: FD and FUD 100%; random 86%; utility 80%. At limit about 25: FD/FUD about 90% vs about 60% | Smyth and Keane 1995 (a03, a04) | Contested: one run, toy domain, Pan 2005 says noise breaks it (K06) |
| Later-use utility deletion cuts memory a lot at small loss, if the judge is reliable | Periodic deletion cuts 65 to 70%. RegAgent strict: none 70.95 (2938 records), periodic 67.65 (949), history 69.80 (2286). CIC-IoT strict 85.40 (904) vs history 89.60 (788) vs periodic 80.80 (310). Combined deletion with coarse C1: 59.32 vs 63.18 | Xiong Table 2 (a18, b07, c09) | Established with strict judge; noisy judge hurts (K07) |
| Selective addition beats full addition; failure lessons add little; utility deletion adds Pass@4 | ReMe, Qwen3-8B, BFCL-V3, Avg@4 / Pass@4: full addition 40.83/62.00; selective 44.33/64.66 (+3.50/+2.66); plus failure reflection 45.00/64.66; plus utility deletion 45.17/68.00; no memory 24.41/28.50 | ReMe Table 3 (b09, d13) | Single source, row mapping from order (K07, K23) |
| Naive success accumulation helps; curation by later-use Q helps more | gpt-4o-mini, 800 train tasks, 5 seeds. ALFWorld: fixed 0.73, bootstrap 0.89, +DB curation 0.91, +exemplar 0.90, both 0.93. SQL 0.75/0.79/0.78/0.81/0.82. Wordcraft 0.55/0.64/0.64/0.72/0.69. 15-point ALFWorld gain equals a gpt-4o-mini to gpt-4o upgrade | Sarukkai 2025 (b11, d15) | Established across 3 envs; labels from the environment |
| Failures help only when the format can use them | WebArena-Shopping, Gemini-2.5-flash: Synapse 40.6 to 41.7; AWM 44.4 to 42.2 (drop); ReasoningBank success-only 46.5 to 49.7 with failures; no memory 39.0 | ReasoningBank Fig 7 (c11, d09) | Contested (K04); one subset |
| Raw unfiltered failures can wreck a baseline | Evo-Memory ExpRAG Gemini 2.5 Flash ALFWorld 0.59 to 0.25; Claude 3.7 ScienceWorld 0.46 to 0.27, ALFWorld 0.74 to 0.76. ReMem (prunes): 0.66 to 0.57 and 0.92 to 0.92 | Evo-Memory (c19, c20, d16) | Single source; table columns by row order |
| Self-judge noise matters little for strategy memory | Real judge accuracy 72.7%; simulated 100 to 50% accuracy gives success about 47.0 to 52.4 (no-memory 39.0, ReasoningBank 49.7); every level above no memory | ReasoningBank Fig 8 (c12, d09) | Contested vs Xiong (K17) |
| Rewriting memory in place decays it | ARC-AGI Stream GPT-5.4, no-memory pass@1 58.5 +/- 5.4; consolidated epoch 1 55.1; epoch 10 38.5 +/- 5.3. Pass@10 coverage 100% to 66.7% to 60.6%. Table 5 at step 400: default in-place rewrite 43.2; append-only, prior store visible 50.0; add plus delete, no in-place edit 64.0; append-only, store hidden 70.0; raw trajectories 76.6 | Zhang 2026 (b14, b15, d01, d03) | Established across 5 environments; no independent replication (K09) |
| Decay curves over 400 steps | ARC-AGI Stream no-memory / peak / step 400: GPT-5.5 78/80/68; Claude Sonnet 5 40/58/48; GLM 5.2 22/44/22; DeepSeek V4 Pro 28/40/18. WebShop AWM 0.64 (8 examples) to 0.20 (128) = no memory | Zhang 2026 (d01, d04) | Single source |
| Raw trajectory logs beat lesson-style consolidators in most rows | ALFWorld (no memory / all raw / 16 raw): GPT-5.4-Mini 54/90/77; GPT-5-Mini 52/81/67; Claude-Haiku-4.5 79/92/73. AppWorld TGC: Qwen3.5-27B 66/73; GPT-5-Mini 14/23; Haiku 4.5 68/66 | Zhang 2026 Table 4 (d02) | Single source; raw baseline not equal-token |
| One full LLM rewrite can collapse a store | AppWorld: step 60 context 18,282 tokens, accuracy 66.7; next step 122 tokens, 57.1; baseline 63.7. Without incremental updates TGC 67.3 vs 76.2 with | ACE (d18) | Single case study; independent corroboration of Zhang |
| Curation beats full history for strong models; small models lose | AIME 2024 Claude 3.5 Sonnet: base 23.3, full history 26.7, DC 50.0. GPT-4o: base 20.0, full history 6.7, DC-RS 40.0. GPT-4o-mini fell below baseline | Dynamic Cheatsheet (c17, c18) | Established direction; 30-question sets (one item = 3.3 points) (K10) |
| Retrieved-case relevance, not count, drives gain | ExpeL ALFWorld: ReAct 40.0; random successful trajectories 42.5; reasoning-similarity 48.5; task-similarity 59.0 | ExpeL Table 3 (d08, b21) | Established (K20) |
| About 4 retrieved cases is enough | Memento seven QA sets F1/PM: K=0 59.9/72.2; K=1 63.6/77.9; K=2 63.7/78.1; K=4 64.5/78.5; K=8 64.1/78.2; K=32 63.9/78.1. First case gives 5.7 PM points. MemRL inverted-U, best k1=5, k2=3 | Memento, MemRL (b17, c22, d14) | Established (K12) |
| Case-memory gain is small at the end of a long run | Memento DeepResearcher, pass 1 to 5, no-CBR 78.65 to 84.47; non-parametric CBR 79.84 to 84.85; parametric 80.46 to 85.44; CBR gain at pass 5 +0.38 / +0.97 | Memento (a21) | Single source |
| Memory effect per item is two-sided | SEDM controlled HotpotQA: memory turns 73 failures into successes and 32 successes into failures; always-use 0.249 to 0.333; perfect gate 0.399; learned gate 0.329 with 18% fewer input tokens | SEDM (d12) | Single source |
| Paired-replay admission cuts tokens at equal or better accuracy | FEVER: no memory 57; G-Memory 62 (3.62M prompt tokens); plus paired admission 64 (2.19M, 40% fewer) | SEDM (d12) | Single source; confounded with retrieval changes |
| Per-case learned Q predicts usefulness | Q vs success r = 0.861; lowest Q bin 21.5% success, highest 88.1%. Last-epoch success: no memory 0.631, RAG 0.679, Mem0 0.681, MemP 0.736, MemRL 0.772. About 12% of high-Q memories are failure reflections | MemRL (d14) | Single source; 10 epochs on same task set |
| Code-verified gate matters most | Voyager: removing self-verification cut discovered items by 73% | Voyager (c24) | Single source (Minecraft) (K16) |
| Strong backbones gain little from replay | LifelongAgentBench: Llama-3.1-8B DB 0.19 to 0.78 at 64 examples; Llama-3.1-70B 0.81 to 0.90; Qwen2.5-32B 0.82 with no clear gain | d17 | Single source |
| Memory gain tracks task similarity | Evo-Memory ReMem gain vs within-dataset similarity: Pearson 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet). Pruning rate 36.8% (GPQA), 17.5% and 10.8% (AIME) | Evo-Memory (c19) | Correlation over few datasets |

## 4. Mechanisms and models

**4.1 The retention loop (generic).**
```
on task t finished with answer a, signal r:
    candidate = (query q, answer a, reward r, optional lesson)
    if admit(candidate, bank): bank.add(candidate)
    if size(bank) > cap or periodic: forget(bank)
    update per-case stats for the cases retrieved on t   # needed for later-use utility
```

**4.2 Write gates (the admit function).**
1. Add-all: admit always. Baseline that loses (Xiong).
2. Success-only (CASCADE): admit if r == 1. CASCADE's rule is M(t+1) = M(t) union {(q,a,r)} if r = 1 (a10). Needs trusted binary reward.
3. Verified admit: admit only if code or tests pass (Voyager, AWM rule-based filter: dedup, then drop invalid actions) (a24, c24). Strongest gate, available only when a checker exists.
4. Judge-gated: an LLM judge scores the trajectory. Noisy. C3-style: tune the judge on about 300 labelled trajectories (a17).
5. Novelty gate (IB2 / Yang-Zhu): admit only if the nearest stored case does not solve the new query. Implementation: retrieve top-1; run the task with it; admit when that attempt fails and a no-case attempt succeeds, or when similarity to nearest is below a threshold. Not tested on LLMs (K24).
6. Paired-replay gate (SEDM): rerun the task with and without the candidate; admit if reward net of token cost improves (d12). Costs one extra run per candidate.
7. Per-fact write operators (Mem0): ADD, UPDATE, DELETE, NOOP against existing items (a26, c23). Cheap dedup and conflict handling; the decision is an LLM call, so G5 applies.
8. Coverage-greedy addition (Yang-Zhu): offline, pick the case with the largest extra coverage, repeat. Needs a pool.

**4.3 What to store per case.** Query, answer, reward, and for lessons one line (ExpeL, ReasoningBank: at most 3 items per trajectory). Memento stores only the final step to avoid redundancy (c21). Store raw episodes, not rewritten abstracts, if rewriting is in place (Zhang).

**4.4 Forget rules.**
- Periodic: drop never-retrieved records every N steps (Xiong: every 500 steps, cuts 65-70% of memory).
- History-based / later-use utility: after n retrievals (n >= 5; 3 for AgentDriver), drop the record if mean outcome utility is below a threshold (0.5) (b07). ReMe: remove once retrieved at least a threshold number of times if mean contribution u/f is below a threshold (d13). Sarukkai: Q(trajectory) = outcome-weighted success of tasks where it was retrieved (d15). MemRL: Q updated from outcomes after each reuse, re-rank by Q (d14).
- Competence-based (Smyth-Keane): classify cases as pivotal / support / spanning / auxiliary using coverage and reachability sets; delete auxiliary first, pivotal last. Needs a notion of "problem solved by case". With embeddings there is no clean coverage set; untested (K18).
- Cap: Xiong capped at 100 (EHRAgent) and 180 (AgentDriver) records; results converge as the cap rises, so unbounded growth is not needed (a19).

**4.5 Update rule for the lesson store (avoid decay).** From Zhang Table 5 and ACE: append deltas, dedup, never overwrite in place. If condensing is needed, do it as add plus delete, not as an edit of the whole store. Avoid one monolithic rewrite (ACE 18,282 to 122 tokens).

**4.6 Theory: CASCADE's regret split.** Regret = coverage gap (no good case stored) + retrieval regret (a good case exists but is missed). Retention affects only the coverage gap. Bound: O~(T^((d0-1)/d0)) for intrinsic dimension d0 > 1, O~(1) otherwise. Assumptions: Lipschitz (similar queries have similar solutions), model succeeds with probability at least p_min > 0 even with an irrelevant case, queries are i.i.d. (a11, b04). Engineering reading: the coverage gap only shrinks if each query type has some chance of becoming a stored case. If a task type never succeeds, it never enters a success-only bank.

**4.7 Experience following.** The model copies the output of the most similar stored case (Pearson r near 1 on RegAgent with a large bank; lower with a small fixed memory where the model reasons more) (a16, c06). Consequence: a stored error propagates and its descendants get stored too (c07). A write gate is an error firewall.

## 5. What holds up

**Held up (multiple sources or clear direction).**
- Add-all loses to a gated store. Xiong (4 agents), ReMe (+3.50 Avg@4), Evo-Memory (unfiltered failures degrade). Three independent papers. Caveat: small and mid agents, short streams.
- Any bank of verified successes beats no bank, by a lot on mid-size models. CASCADE +18.35, Sarukkai +16 on ALFWorld, AWM +12.0 absolute on WebArena. Caveat: gains shrink with stronger backbones (LifelongAgentBench; Memento's no-CBR curve rises to within 1 point).
- Relevance of retrieved cases drives the gain, not count (ExpeL random 42.5 vs task-similar 59.0).
- Rewriting a store in place decays it (Zhang across 5 environments; ACE collapse). Append and delta updates avoid most of it.
- Later-use outcome is a free label for pruning (Xiong, ReMe, Sarukkai, MemRL).
- About 4 retrieved cases is enough.

**Failed or did not replicate.**
- Smyth-Keane footprint deletion has no LLM replication. Pan 2005 says noisy data break the pivotal rule. One run per policy in the original.
- Aha 1991 IB2 novelty rule: never re-tested with LLM agents.
- Always-retain-the-truth (CASCADE C.5) hurt 4 of 12 tasks.
- Raw failures in success-oriented memories (AWM -2.2, Synapse +1.1) did not help.
- Coarse judges in raw-trace stores fell below fixed memory in 6 of 12 cells.
- Small models with curated cheatsheets (GPT-4o-mini) fell below baseline.
- Zhang 2026 itself has no independent replication.

**Moderators found.**
- Gate quality (oracle > tuned judge > coarse judge). Moderator of whether the gate beats fixed memory.
- Storage format: distilled strategies tolerate judge noise (ReasoningBank), raw traces do not (Xiong). Explanation plausible, never tested head to head (K17, K21).
- Task similarity to the bank (r 0.717 / 0.563).
- Model strength: strong backbones gain little from replay; weak ones gain a lot.
- Retriever capacity: a bigger bank can hurt if the retriever cannot cope (CASCADE C.5).
- Batch heterogeneity: mixed-task batches erode lesson memory faster (Zhang).
- Judge source: CASCADE, Sarukkai and Xiong-strict use ground truth; ReasoningBank and AWM-online use a model judge.

**Interventions that worked.** Fine-tuned judge on 300 labelled trajectories (above coarse C1 in three of four agents). Paired replay admission (40% fewer prompt tokens, +2 accuracy). Utility deletion (ReMe Pass@4 +3.34). Delta updates with dedup (ACE TGC 76.2 vs 67.3). Agent-managed retain/delete with no consolidation (Zhang Auto).

**Interventions that did not.** In-place rewriting. Raw failure trajectories in success-oriented stores. Coarse-judge history deletion (lowered AgentDriver and CIC-IoT). Always retaining correct cases with a weak retriever.

**Evidence quality warnings.** No study ablates the retention rule alone with retrieval and model fixed. Most deletion and addition evidence is on small agents, streams of 1000 to 4000 records and a single task family. Several tables were read from garbled text (ReMe, Evo-Memory, ExpeL, Sarukkai rows mapped by order). Treat those as approximate. Longest stream seen is 400 steps (Zhang) and 800 training tasks (Sarukkai).

## 6. Language models

**Which models and tasks.** Qwen3-4B/8B/14B/32B and Gemini-2.0-flash (CASCADE); GPT-4o, GPT-4o-mini, DeepSeek-V3 (Xiong); Qwen3-8B/14B/32B (ReMe); gpt-4o-mini (Sarukkai); Gemini-2.5-flash, Claude 3.7 (Evo-Memory, ReasoningBank); GPT-5.4, GPT-5.5, Claude Sonnet 5, GLM 5.2, DeepSeek V4 Pro (Zhang); Llama-3.1-8B/70B, Qwen2.5-32B (LifelongAgentBench); GPT-4.1 planner, o3 executor (Memento).

**What changed behaviour, and by how much.**
- Having a success bank: +15.4 points of the 18.4 total in CASCADE (Qwen3-32B); Qwen3-8B +15.2 (43.22 to 58.44).
- Learned retriever on top: about +3 (63.76 to 66.68; Qwen3-8B +2.4; Qwen3-14B +2.3).
- Gating vs add-all: +3.5 (ReMe) up to +25.5 (CIC-IoT strict 85.40 vs add-all 59.90); EHRAgent strict 38.50 vs add-all 13.05.
- Curation on top of success accumulation: +2 to +8 (Sarukkai).
- Failure lessons on top of success-only: +0.7 (ReMe Avg@4), +3.2 (ReasoningBank Shopping).
- Bank vs no bank on a strong backbone: little or none (Qwen2.5-32B; Memento at pass 5 under 1 point; Claude-Haiku-4.5 AppWorld 68 to 66).
- Rewriting memory: ARC-AGI GPT-5.4 pass@1 58.5 to 38.5 by epoch 10; GPT-5.5 78 to 68 at step 400 under agent-managed memory.

**Behavioural facts.**
- LLMs copy the nearest stored case's output (experience following). With a small fixed memory they reason more; with a large bank they copy more.
- Models managing their own memory default to retaining raw episodes and abstract sparingly (Zhang Auto). Auto roughly doubles the accuracy of forced consolidation.
- Memory helps and hurts the same item set: SEDM, 73 failures fixed vs 32 successes broken.
- Models write over-general lessons (a Pick&Place lesson misapplied to Pick-Clean-Place) and hallucinated reflections (ExpeL: adding reflections to insight extraction hurt).
- A curator may write "previous content preserved" and truncate the store (DC).
- Self-judge accuracy on WebArena-Shopping was 72.7% (Gemini-2.5-flash).

**What we do not know in LLMs.** Whether a novelty-only gate matches success-only at equal bank size. Whether any gate result holds on open reasoning items without a checker. Whether anything here survives past 1000 tasks with task-type shift.

## 7. What our agent should take

Our schema forbids model-only judging of correctness (G5, G10), requires every element to win at equal tokens (G7), and keeps lessons one line, shown after the first attempt (SCHEMA section 5). The items below fit those rules.

### Add now (established)

1. **Do not store every episode.** Add-all lost on 4 of 4 agents (3.7 to 12.1 points) and in ReMe (-3.50). [E]. Part: S9 / memory. Evidence: a17, b06, c05, d13, d16 (K01).
2. **Gate writes on code-checked or oracle-like signals first, not on the model's own opinion.** Strict oracle beat tuned judge beat coarse judge. Our S4/S8 checks (held-out example, mutated input) are the gate (matches G3, G5). [E]. Part: G / S9. Evidence: a17, c05, b09, c24 (K02; the Voyager figure alone is K16, single-source).
3. **Never rewrite the lesson store in place. Append one-line lessons, dedup, and prune by delete.** [E] (Zhang across 5 environments, ACE collapse; no independent replication of Zhang itself). Part: memory / S9. Evidence: b14, b15, d01-d05, d18 (K09).
4. **Track per-case retrieval outcomes in code.** Count how many times a case was shown and whether the task then passed. Use it later for pruning and for the SCHEMA rule "lesson trusted after helping on two problems". Free and in code. [E] that later-use utility works with embedding retrieval (ReMe +3.3 Pass@4, MemRL r 0.861, Sarukkai +1 to +8); the exact counter design is [S]. Part: memory / G5. Evidence: b07, d13-d15 (K07, K22).
5. **Retrieve about 4 cases or fewer, picked by task similarity.** [E]. Part: O / memory. Evidence: b17, c22, d08 (K12, K20).
6. **Cap the bank and prune periodically.** Performance converges as the cap rises; periodic deletion cuts 65 to 70% of records with small loss. [E]. Part: memory. Evidence: a19, b07 (K07).
7. **Include a random same-task-examples control in every memory test.** Without it, retention gain is confounded with more few-shot examples. [E] as method. Evidence: d08 (K20).
8. **Quote CASCADE as +18.35 points (38% relative) with a spread of +2.1 to +51.2, not "20.9%".** [E]. Evidence: d06 (K19).

### Test first

1. **Failure lessons as one-line items next to success-only.** [C]. Gains small (+0.7, +3.2); raw failures hurt. Part: S9 / memory. Evidence: c11, d13, d16, d09 (K04, K23).
2. **Novelty gate (store only if nearest case does not solve it).** [S]. Yang-Zhu 58 vs 200 cases for full coverage. Part: S9. Evidence: a07, a08, d19 (K05, K24).
3. **Competence or footprint deletion with embeddings.** [C]. Smyth-Keane 100/86/80 on a toy domain; Pan says noise breaks it. Part: memory. Evidence: a03, a09 (K06, K18).
4. **Paired-replay admission, spending one extra run per candidate.** [S]. SEDM -40% tokens. Part: G7 / S9. Evidence: d12 (K22).
5. **Self-judge gate for lessons versus raw traces.** [C]. Xiong vs ReasoningBank. Part: G5 / S9. Evidence: c12, d09, d10 (K17, K21). Conflicts with G5 unless the judge is only a pre-filter and code decides.
6. **Memory-off switch when similarity to the bank is low.** [S]. Similarity correlation 0.563 to 0.717; SEDM 32 successes broken. Part: S0 / memory. Evidence: c19, d12 (K11).
7. **Success-only bank over 600+ tasks with a mid-stream task-type shift.** [S]. No study. Part: memory. Evidence: d04, d11, d19 (K24).
8. **Retain a verified success only after a second check (right answer for the right reason).** [S]. Xiong "misaligned replay": strict history deletion beat even an error-free memory. Part: G3 / S9. Evidence: b08, c08, d15 (K11).

## 8. Concrete tests on our bench

Common design: frozen model, fixed retrieval (top-4 by task similarity), same prompt template, same total tokens per arm (count write-gate and judge calls in the budget; G7). Five seeds, same task order across arms, report mean and spread. Add a "random same-task examples" arm to every test.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Stream of 300 ARC-like or BRAINTEASER items with a checker | (a) no bank; (b) add-all; (c) success-only (code-verified); (d) novelty-only; (e) success + one-line failure lesson | Final-100-item pass rate; bank size; tokens per item | (c) > (b) by 3 to 10 points; (d) matches (c) at under half the bank; (e) +0 to +3 over (c) |
| T2 | Same stream, noisy gate | Gate accuracy 50, 70, 90, 100% (flip labels in code) for raw-trace bank vs one-line-lesson bank | Pass rate vs gate accuracy | Raw traces fall below no-bank at 70% or lower; lessons stay above no-bank (ReasoningBank pattern) |
| T3 | Plant 5 wrong cases among 100 | Ungated bank vs bank with per-case retrieval-outcome counter and prune rule | Copy rate of wrong case on near neighbours; pass rate | Copy rate drops after the rule prunes cases with retrieval count >= 5 and success < 0.5 |
| T4 | 600-item stream, task-type shift at item 300 | Success-only bank uncapped; capped at 100 with later-use utility deletion; capped at 100 with random deletion; capped at 100 with age | Pass rate on items 301-600; bank size | Utility > random by 2 to 5 points; uncapped decays as the retriever dilutes |
| T5 | Lesson store, 200 items | In-place rewrite every 20 items vs append-only with dedup vs append + delete | Pass rate by step; lesson-store token count | In-place falls toward no-memory; append >= rewrite +10 points by step 200 (Zhang scale: 43.2 vs 64-77) |
| T6 | Items where bank similarity is high vs low | Memory always on vs memory gated by similarity threshold | Per-item flips (fail-to-pass vs pass-to-fail) | Gate removes most pass-to-fail flips at low similarity |
| T7 | Verified-success candidates | Admit all verified vs admit only if paired replay shows gain net of tokens | Pass rate; total tokens | Fewer admitted cases (-30 to -40%) with equal or better accuracy (SEDM scale) |
| T8 | Footprint deletion on embedding bank | Footprint-like (drop cases whose neighbours are all solved by others) vs later-use utility vs random at cap 50 | Pass rate at cap 50 | Unknown; footprint wins only if embedding neighbourhoods approximate coverage |

## 9. What does not transfer, and why

- **Training-based retention (CASCADE vs REINFORCE+LoRA, Memento parametric Q).** We do not train. Use only as justification that a bank can rival fine-tuning (K13).
- **CASCADE's regret theory.** Needs i.i.d. queries and p_min > 0 (every query solvable at some rate). Real streams drift and some types never succeed.
- **Strict oracle gates (Xiong).** Ground-truth error thresholds are not available in open deployment. Only our checks (held-out, mutation) approximate them.
- **Mem0 and LOCOMO.** Conversation facts, and an LLM chooses ADD/UPDATE/DELETE. G5 forbids the model as sole judge.
- **ReasoningBank self-judge.** Works with a 72.7% judge on web tasks; our G5/G10 say the judge's reasoning is not evidence. Use only as a pre-filter.
- **Voyager and AWM code gates.** Strong, but depend on executable environments. Many reasoning items have none.
- **Smyth-Keane and Yang-Zhu numbers.** Toy domains (property valuation, Towers of Hanoi) with exact coverage sets and nearest-neighbour retrieval. LLM prompts have no coverage set.
- **Large lesson stores with strong models.** Gains shrink on strong backbones; our target model may be strong.
- **Leaderboard numbers (Memento GAIA 87.88 / 79.40).** Planner/executor stack and no retention ablation.
- **ARC-AGI Stream decay.** One generator family, one author-built testbed; decay is driven by rewriting, not by success-only retention.

## 10. Open questions

1. Which write gate wins at equal tokens and fixed retrieval: add-all, success-only, novelty-only, success plus failure lessons? (No study runs all four; K24, d20.)
2. What judge accuracy lets a self-judged gate beat a fixed seed bank, for raw traces vs distilled strategies? Xiong gives no percent accuracy.
3. Does a novelty gate replicate Yang-Zhu efficiency with LLMs, and at what bank size does it saturate?
4. Does a success-only bank decay over more than 1000 tasks with distribution shift? Longest seen: 400 steps.
5. Do failure lessons add anything over success-only at equal tokens? Only ReasoningBank and ReMe test it, with small gains and no token control.
6. Does Zhang's rewriting harm replicate independently? Does it hold for one-line lessons by class, as in our design?
7. How to detect a verified success that is right for the wrong reason? Candidate cheap signals: paired replay, per-case outcome counters.
8. Does competence deletion work with embedding retrieval?
9. What does the CASCADE 20.9% mean, and what is the 16-task spread?
10. Gain from retention vs gain from simply more diverse few-shot examples (random control missing in most papers).
11. Is there a model-strength threshold below which memory should not be used at all?

## 11. Sources

[V] = PDF/HTML text read by a research agent this run; [M] = memory or snippet only.

- [V] Aamodt and Plaza (1994). Case-based reasoning: foundational issues. https://www.iiia.csic.es/~enric/papers/AICom.pdf (a01)
- [V] Smyth and Keane (1995). Remembering to forget. https://folk.idi.ntnu.no/agnar/CBR%20papers/smyth-keane-remembering-95.pdf (a02, a03, a04, a06; critique re-checked 50 cases, 160 targets, limit 75, 80/86/100)
- [M] Minton (1990). Quantitative results concerning the utility of explanation-based learning. Known via Smyth and Keane (a05)
- [M] Aha, Kibler, Albert (1991). Instance-based learning algorithms. Machine Learning 6 (a27)
- [M] Racine and Yang; Leake and Wilson, case-base maintenance. https://doi.org/10.1007/3-540-63233-6_529 (b25)
- [V] Yang and Zhu (2001). A case-addition policy for case-base maintenance. https://cse.hkust.edu.hk/~qyang/Docs/2001/cicbr.pdf (a07, a08)
- [V] Pan, Yang, Pan, Li (2005). Competence driven case-base mining. https://cdn.aaai.org/AAAI/2005/AAAI05-037.pdf (a09)
- [V] Guo, Du, Chen, Chang, Wang (2026). CASCADE. https://arxiv.org/abs/2605.06702 (a10-a15, b01-b04, c01-c04, d06, d07; critique re-opened table values)
- [V] Xiong et al. (2025). How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (a16-a19, b05-b08, c05-c09, d10, d11)
- [V] Zhou, Chen et al. (2025). Memento. https://arxiv.org/abs/2508.16153 (a20-a22, b16, b17, c21, c22)
- [V] Wang, Mao, Fried, Neubig (2024). Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (a23, a24, b22, c13)
- [V] Zhao et al. (2023/2024). ExpeL. https://arxiv.org/abs/2308.10144 (a25, b21, c15, c16, d08)
- [V] Chhikara et al. (2025). Mem0. https://arxiv.org/abs/2504.19413 (a26, c23)
- [V] Cao et al. (2025). ReMe. https://arxiv.org/abs/2512.10696 (b09, b10, d13)
- [V] Sarukkai et al. (2025). Self-generated in-context examples. https://arxiv.org/abs/2505.00234 (b11-b13, d15)
- [V] Zhang et al. (2026). Useful memories become faulty when continuously updated by LLMs. https://arxiv.org/abs/2605.12978 (b14, b15, d01-d05)
- [V] Dual-memory framework for long-horizon agents (2026). https://arxiv.org/abs/2604.02734 (b18)
- [V] Yu et al. (2026). Self-Consolidation (EvoSC). https://arxiv.org/abs/2602.01966 (b19)
- [V] Wang et al. (2026). ExpHarness. https://arxiv.org/abs/2605.30712 (b20)
- [V] Ouyang et al. (2025). ReasoningBank. https://arxiv.org/abs/2509.25140 (c10-c12, d09)
- [V] Shinn et al. (2023). Reflexion. https://arxiv.org/abs/2303.11366 (c14)
- [V] Suzgun et al. (2025). Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (c17, c18)
- [V] Evo-Memory (2025). https://arxiv.org/abs/2511.20857 (c19, c20, d16)
- [V] Wang et al. (2023). Voyager. https://arxiv.org/abs/2305.16291 (c24)
- [V] Zheng et al. (2025). LifelongAgentBench. https://arxiv.org/abs/2505.11942 (d17)
- [V] Zhang et al. (2025). ACE. https://arxiv.org/abs/2510.04618 (d18)
- [V] Liu et al. (2026). SEDM. https://arxiv.org/abs/2509.09498 (d12)
- [V] Zhang et al. (2026). MemRL. https://arxiv.org/abs/2601.03192 (d14)
- [M] Gap-search status notes d19, d20 (no new sources; web quota ran out, forward-citation search not possible)
- [M] Smyth and Keane IJCAI version https://www.ijcai.org/Proceedings/95-1/Papers/019.pdf (b23, c25; fetch returned a different paper; do not cite)

Known evidence-file errors: b16 names Memento's first authors as Wang et al.; the correct first authors are Zhou and Chen. Memento's -18.0 F1 delta (a22) is not located to a named ablation step. Xiong EHRAgent coarse C1 is 26.19 in Table 1 and 25.91 in the Table 2 block; use Table 1 for addition and Table 2 for deletion. ReasoningBank 46.5 (success-only) is not the Synapse 46.5 in the Gemini-pro table.
