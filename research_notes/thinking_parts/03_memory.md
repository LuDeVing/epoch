# 03. Memory: what is kept, consolidated, retrieved, forgotten, and what reaches whom

*2026-10-13. Part 3 of the thinking decomposition. The shared web-search budget ran out after two searches; the rest was read from primary pages (abstract-only reads marked "abs"). Grades: **strong** = two or more independent controlled studies or a meta-analysis; **medium** = one controlled study or ablation with numbers; **weak** = self-reported, vendor, single run or abstract only. Other-domain numbers are analogs, not forecasts.*

## 1. Bottom line

1. **Volume is the best-supported negative.** Add-all fell below a small fixed memory on all four agents tested (55.5 vs 67.5 success on RegAgent) [23]. A wholesale rewrite collapsed a context from 18,282 to 122 tokens and accuracy from 66.7 to 57.1, under the 63.7 no-adaptation baseline [18]. A full outcome dump gave a judge 70.8% selective accuracy against 83.5% for focused retrieval [29]. Nano pastes whole blocks, so shrink and focus first.
2. **Both controlled studies of experiment memory use measured, scoped outcome records.** Rehearse: one line per row at cosine >= 0.40 beat a full dump, and failure reasons hurt a selector [29]. CMU: lineage written by the evaluator, not the agents, sliced per role: 16 valid improvements vs 3 [30].
3. **Consolidate by incremental delta operations with counters; keep raw rows immutable** [18][17]. LLM-only conflict handling is near zero on multi-hop updates (best 28%, most at or under 5%) [5], so supersede by script.
4. **Push versus pull is unsettled** [5][7][8][9]. Make it an arm.
5. **Human memory transfers as architecture**: a fast immutable store plus a slow integrated one with interleaved replay [39]; retrieval, not re-exposure, strengthens memory [40]; utility-ranked replay [42][43]. Spacing does not transfer [41].
6. **The store is empty** (2 mock ledger rows), so schema fixes are free now.

## 2. Memory in the loop today, and nine leaks found in the code

Store: `ledger.jsonl` has 2 rows (both mock), `verified_by_hash.json` the same 2 hashes, `memory/research/` one 2-day-old brief.

- **Briefs cache** (`research.py` 141, `loop.py` 229): one web-research blob per planner part id, 7-day TTL from file mtime. **L1** Keyed by id alone, though planner ids differ between runs (comment in `inject_ledger`) and lenses rotate: a hit can return a brief for another frame; a miss re-pays a 40-turn web agent per part plus one for analogies. **L2** `merge_facts` (194) rewrites the file and resets the mtime, so a brief that keeps receiving facts never expires; interrogation claims join `known` at parity with sourced literature.
- **Ledger injection** (`loop.py` 290, `research.py` 161): every row of this baseline version goes to every part. **L3** `stackable` rows are dropped (only verified, fail, close_call, promising are mapped) though they feed compose; mock and control rows pass. **L4** Each row prints twice (TRIED, then KNOWN/FAILED) and sits first in `known`, so the `adapt` card's `known[:3]` (loop 428) and the premortem evidence pack's first 30 lines (loop 712) fill with own-ledger lines after 15-20 rows. **L5** No cap or ranking.
- **`history_text`** (909): last 40 builds of this run, with reasons and prediction checks, to every round-2+ sketcher, interrogation call, replan and control arm. **L6** Recency, not relevance; one block for all consumers.
- **`knowledge_text`** (`deepen.py` 132): facts then Q&A under 4,000 characters. **L7** The cap cuts from the end, so answered questions go first.
- **Hash memory** (loop 1177-1197): exact normalised source to ladder record. **L8** Key lacks arm, boundary and learn-steps; one single-run record per hash is overwritten and replayed as truth, soft rung-3 failures included.
- **Promotion** (`promote.py`). **L9** Briefs drop every old-version row while the novelty gate (loop 515) keeps all of them: a v1 failure is invisible to ideation yet blocks its own retry on v2 (bar the 10% audit share). No agent reads BASELINES.md; no lesson is written.

Reach today: round-1 sketchers see outcomes only through the research and adapt cards; the builder sees facts, Q&A and objections, not history; premortem critics see the idea, script and one pack.

## 3. Evidence

### 3.1 Architectures
- The 2025 survey sorts memory into factual, experiential and working functions and token, parametric and latent forms [1]; the 2026 survey frames a write-manage-read loop and lists continual consolidation, learned forgetting and causally grounded retrieval as open [2]; MemGPT pages its own tiers [16] (medium; surveys).
- Gains shrink under control. Mem0 scored 66.9 J vs 72.9 for full context (p95 1.4 s vs 17.1 s, 1.8k vs 26k tokens) [6]; a graph system's lead vanished at a fixed retrieval budget [4]; one system's memory writes failed format checks unnoticed, 17.9% on gpt-4o-mini and 30.4% on a 3B model [3] (medium). A grep-over-files agent beat Mem0's graph, 74.0% vs 68.5% [7] (weak; vendor).
- Removing reflection, planning and memory cost 8.7 TrueSkill points [12] (medium). Removing self-verification before storing cut Voyager's discovered items 73% [13] (medium). Structuring episodes into semantic and procedural units: 62.8 to 75.1 on LongMemEval [22] (weak; self-reported).

### 3.2 Retrieval
- **Focused beats full and recent.** Rehearse retrieves same-task attempts executed earlier at cosine >= 0.40 (worse at 0.35), one line each. Judge accuracy: no memory 56.9, full dump 70.8, LLM summary 80.9, focused 83.5; top-1 only 80.5; adding failure reasons 80.6 [29] (medium; five seeds; reasons tested on a selector only).
- **Length hurts by itself**: 13.9-85% drops despite perfect retrieval [11]; ~300-token focused inputs beat ~113k-token full inputs on 306 LongMemEval prompts [10] (medium).
- **Similarity is not utility**: learned Q-values correlated with success at r = 0.861 and beat similarity RAG, 0.772 vs 0.679 [21] (weak-medium); prioritized replay beat uniform on 41 of 49 Atari games [42] (abs).
- **Push vs pull**: vendors back just-in-time loading (+39%, internal set) [8][9] (weak). Controlled work splits: retrieval wins pinpoint facts, long context wins test-time learning [5]; AIDE's memory summary left medals "nearly identical" [31]; accurately pushed state was not reliably used [28] (medium/weak).

### 3.3 Consolidation and contradiction
- ACE (helpful/harmful counters, script-merged deltas): +10.6% on agent benchmarks, latency -86.9% [18]. ExpeL (ADD, EDIT, UPVOTE, DOWNVOTE; drop at zero): ALFWorld 59% vs 40%; insights beat retrieved trajectories on HotpotQA (36 vs 31) and lost on ALFWorld (50 vs 55) [17]. ReasoningBank (successes and failures distilled): +4.6 to +8.3 WebArena points [19] (medium).
- Tiers (events, phase summaries, cross-task wisdom): 54.5% medals without wisdom vs 72.7%, one run [35] (weak). Sleep-time precompute: same accuracy at ~5x less test-time compute, less when queries are unpredictable [24] (medium).
- Mem0 deletes or invalidates, Zep keeps a temporal graph, A-Mem updates old notes [6][25][26] (abs, weak). Measured, every method failed multi-hop updates (<= 28%, most <= 5%) [5] (medium).

### 3.4 Forgetting, interference, memory that hurt
- Deletion helps: periodic deletion 1,012 to 302 records at 38.67 vs 38.59 accuracy; history-based deletion +0.8 to +4.2; strict admission beat add-all by 15-26 points [23] (medium).
- Unfiltered failures hurt (Claude: ExpRecent 0.48, ExpRAG 0.52 vs 0.81 for a refining design) [20]; failure items helped ReasoningBank (46.5 to 49.7) and hurt AWM (44.4 to 42.2) [19] (medium).
- Errors in context breed errors, and scale does not cure it [27]; self-correction without external feedback does not reliably help [15] (abs); nano's feedback is measured, the Reflexion case [14].
- One failure stored as a ban blocked the winning direction (-0.006 +- 0.006 vs -0.009 +- 0.002, n=3) [38]; shared notes did not stop fixation on one parameter [37] (weak).

### 3.5 Research-agent experiment memory
- Rehearse [29]: 10.7% vs 7.1% vanilla gain, five seeds.
- CMU [30]: evaluator-written lineage (hypothesis, diff summary, score, status, runtime, crash reason) shown as leaderboard, curated tree, last 10 rows, own and adjacent slices: 16 valid improvements vs 3, cap hits 19.0% vs 61.5%; one window per arm (medium-weak).
- AIRA-dojo, AIRA2 [31][32]: hidden consistent evaluation outweighed a shared population (59.9/71.8/76.0 vs 43.4/56.8/56.3 at 3/24/72 h), so only consistently evaluated results should enter memory (medium). DeepScientist and Kosmos keep a findings memory and a shared world model, neither ablated [33][34]; AutoSOTA adds a score ledger, idea library and failure signatures [36] (weak).

### 3.6 Human memory: what transfers
- **Complementary learning systems** [39] (strong): structure is found only when learning is gradual and interleaved, while a fast store absorbs new items. Transfers as two stores with different write rules, and consolidation that replays old lessons with new rows; a wholesale rewrite is the LLM analogue of that interference [18].
- **Testing effect** [40] (strong): restudy won at 5 minutes (81% vs 75%), testing at 2 days (68 vs 54) and 1 week (56 vs 42), though restudy raised confidence. Frozen weights do not learn from retrieval; the carry-over is to strengthen entries by use with outcome and to judge memory by held-out prediction of ledger rows, not by feel. **Spacing** [41] (strong) has no stateless analogue.
- **Replay by gain times need** [43] (weak-medium; theory, partial data): rank by similarity (need) times decision-changing potential (gain). Catalogue also: audit generative abstractions against raw rows (weak), keep a blind share against retrieval narrowing (contested), gate edits on prediction misses (preprint).

## 4. Improvement ideas for this part (status: have / partial / new; effects are analogs)

**I1. Repair the ledger-to-brief path** (have, with defects; 2 h). Map `stackable` to known; skip `mock*` runs and `control` rows; print each row once in a "MEASURED HERE" block after the literature, max 12 lines; age from the brief's own `ts`, which `merge_facts` leaves alone; mark interrogation claims CLAIMED until corroborated. Fixes L2-L5. Effect: literature back in the `adapt` card and premortem pack; no phantom priors from the mock rows. Measure: unit test on a synthetic 30-row ledger (lines per prompt, literature share).

**I2. Focused outcome retrieval** (partial; 0.5 day). Reuse `novelty.Index` (TF-IDF). Per call retrieve rows (any version) at cosine >= 0.40 to part frame plus sketch, one line each ("change -> worked / did not, delta, n seeds, vN"), no reasons or prediction text, max 10, plus the 3 latest of this run; rank by similarity times informativeness (close calls and stackables over clear failures). Replaces the ledger block and the 40-line history; `knowledge_text` keeps build-relevant Q&A first (L7). Effect: shorter prompts, fewer repeated failures; analog 7.1% to 10.7% [29]. Measure: arm at matched tokens; sketches within 0.5 cosine of a ledger failure, effective clusters per 100 sketches, rung-1 pass rate, wins per 100 GPU-h. Basis [29][10][11].

**I3. Brief cache as an entry store** (new; 1 day). Entries (name, mechanism, effect, URL, kind, source, last_verified, uses) keyed by hash(name + URL); a part's view is the top-k by similarity to frame plus assumptions, so lens changes stop invalidating it; TTL by kind (literature 60 days, open directions 14, claims until corroborated) from `last_verified`; research only where fewer than 4 entries clear the threshold. Effect: fewer web agents, no frame mismatch (L1). Measure: hit rate, research tokens per run, a 20-hit frame audit. Basis [22][35][4].

**I4. Scoped, versioned, superseding verdicts; config-keyed hash memory** (partial; 1 day). Rows get scope (node, `changed_symbols`, direction), tier, n, version. Script rules: a replicate with more seeds supersedes; a fail never blocks the opposite direction; at promotion, rows whose `changed_symbols` overlap the promoted diff turn stale, the rest carry at half weight, and stale rows appear only as "untested on the current baseline" (feeding brief 11's re-queue); briefs and novelty gate share the rule (L9). Hash memory keyed by (hash, version, boundary, learn-steps) keeps replicates and memoises only deterministic rung 0-1 failures (L8). Measure: re-run 5 stale failures on the new baseline (flip rate); misapplied-memory rate over 30 retrieved lines. Basis [5][6][25][38].

**I5. Sleep-time lessons list** (new; 1 day; after about 30 real rows). Overnight, one call reads new rows, predictions against outcomes and confirmed or refuted objections, and emits ADD/EDIT/UPVOTE/DOWNVOTE operations, each citing row ids, on at most 30 one-line lessons. A script merges (TF-IDF dedup, counters, drop at zero); raw rows are never rewritten; every fifth pass a fresh agent re-derives each lesson from its cited rows and flags unsupported ones; only prediction misses trigger EDIT or DOWNVOTE. Lessons reach prompts through I2; a promotion triggers one pass that records why the winner won. Effect: hundreds of rows become a page; analog +10.6% [18]. Measure: lessons on/off at matched tokens; harmful-counter and unsupported-lesson rates. Basis [18][17][19][24][39].

**I6. Verified patch library for builders** (new; 1 day). After a candidate passes rung 1, store its minimal diff and mechanism line (cap 100); the builder receives the top 3 by mechanism similarity; delete entries retrieved 3+ times followed by 2+ rung 0-1 failures. Effect: fewer build failures and tokens per build; risk: homogenised code, copied flaws. Measure: rung 0-1 pass rate, tokens per build, diff similarity against a no-library control at equal builds. Basis [13][22][23].

**I7. Provenance episodes and memory-id logging** (partial; 2 h). `cands/*.jsonl` already hold card, operator, seed, parents. Add lens, analogue id, interrogation question ids behind the facts used, memory ids shown (I2), prediction and outcome, plus unbuilt sketches with selection score and reason (a dormant archive reopened at promotion or replan). Effect: yield by card and question for part 10; MemRL-style credit to the memories shown [21]. Measure: field coverage >= 95%; does "memory id present" predict rung pass?

**I8. Exposure matrix, blind share, pull arm** (partial; 0.5 day). A config matrix of consumers (sketchers by round, interrogators, critic, builder, selector, replanner) by memory class (literature, outcomes, lessons, patches, claimed facts, objections). Defaults: r1 sketchers see no outcomes; critics none of the proponent's reasoning; builders facts and patches, not history; 20-25% of sketch contexts per round memory-blind. One cell flips per arm; one arm swaps the pasted block for `lookup(query, class)`, queries logged. Effect: memory's effect on diversity and yield becomes measurable; fixation is bounded. Basis: independent generation then pooling (synthesis C6); fixation despite shared notes [37]; identical repeats, up to 22 consecutive discards [38]; [27][28]. Measure: effective clusters, ledger-duplicate rate, wins per sketch blind vs fed; lookup use.

**I9. Retention policy** (new; 0.5 day). Per-part cap of 60 entries; delete never-retrieved entries after 30 days and entries retrieved 5+ times with harmful ratio over 0.5; archive ledger rows from default retrieval after 3 baseline versions or when 5 newer rows share their scope. Effect: bounded prompts; analog: 75% fewer records at higher accuracy [23]. Measure: store size; prune regret (a pruned item re-derived by research); wins per GPU-hour with and without pruning.

**Keep / compress / drop.** Keep measured rows, provenance, sourced literature. Compress rows into lessons, diffs into patches. Drop from prompts failure reasons, unsourced claims, history dumps.

**Order.** Now, while the store is empty: I1, I7, I4. First two real nights: I2, I8 as arms. After about 30 real rows: I5, I6, I9. I3 if research tokens dominate cost.

**Not settled by reading.** Pull vs push; lessons vs focused raw outcomes (ACE's gains were against no memory); whether exposure narrows or widens proposals here (lineage credited in [30], isolation by the pooling literature); what a promotion should do to memory (no source tests it). Gaps: no 2026 search on forgetting or adaptive retrieval; four human-memory classics (Tse, Kumaran, Richards, Anderson) were blocked and are not cited.

## Sources

[1] Memory in the Age of AI Agents, https://arxiv.org/abs/2512.13564
[2] Memory for Autonomous LLM Agents (abs), https://arxiv.org/abs/2603.07670
[3] Anatomy of Agentic Memory, https://arxiv.org/abs/2602.19320
[4] Beyond Memory Leaderboards, https://arxiv.org/abs/2607.16848
[5] MemoryAgentBench, https://arxiv.org/abs/2507.05257
[6] Mem0, https://arxiv.org/abs/2504.19413
[7] Letta, filesystem benchmark, https://www.letta.com/blog/benchmarking-ai-agent-memory
[8] Anthropic, context engineering, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
[9] Anthropic, context management, https://claude.com/blog/context-management
[10] Chroma, Context Rot, https://www.trychroma.com/research/context-rot
[11] Context length alone hurts, https://arxiv.org/abs/2510.05381
[12] Generative Agents, https://arxiv.org/abs/2304.03442
[13] Voyager, https://arxiv.org/abs/2305.16291
[14] Reflexion (abs), https://arxiv.org/abs/2303.11366
[15] LLMs cannot self-correct (abs), https://arxiv.org/abs/2310.01798
[16] MemGPT (abs), https://arxiv.org/abs/2310.08560
[17] ExpeL, https://arxiv.org/abs/2308.10144
[18] ACE, https://arxiv.org/abs/2510.04618
[19] ReasoningBank, https://arxiv.org/abs/2509.25140
[20] Evo-Memory, https://arxiv.org/abs/2511.20857
[21] MemRL, https://arxiv.org/abs/2601.03192
[22] PlugMem, https://arxiv.org/abs/2603.03296
[23] How memory management impacts LLM agents, https://arxiv.org/abs/2505.16067
[24] Sleep-time compute, https://arxiv.org/abs/2504.13171
[25] Zep (abs), https://arxiv.org/abs/2501.13956
[26] A-MEM (abs), https://arxiv.org/abs/2502.12110
[27] Self-conditioning on errors (abs), https://arxiv.org/abs/2509.09677
[28] Task state and LLM agents, https://arxiv.org/abs/2609.25686
[29] Rehearse, https://arxiv.org/abs/2607.27687
[30] Auto Research with Specialist Agents, https://arxiv.org/abs/2605.05724
[31] AIRA-dojo, https://arxiv.org/abs/2507.02554
[32] AIRA2, https://arxiv.org/abs/2603.26499
[33] DeepScientist, https://arxiv.org/abs/2509.26603
[34] Kosmos, https://arxiv.org/abs/2511.02824
[35] ML-Master 2.0, https://arxiv.org/abs/2601.10402
[36] AutoSOTA, https://arxiv.org/abs/2604.05550
[37] Multi-agent autoresearch, https://arxiv.org/abs/2603.29632
[38] Bilevel autoresearch, https://arxiv.org/abs/2603.23420
[39] McClelland, McNaughton, O'Reilly 1995, https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf
[40] Roediger and Karpicke 2006, https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf
[41] Cepeda et al. 2006, https://www.gwern.net/doc/psychology/spaced-repetition/2006-cepeda.pdf
[42] Prioritized experience replay (abs), https://arxiv.org/abs/1511.05952
[43] Local: mechanism catalogue MEM-07, 11, 14, 16, 17 (cites Mattar and Daw 2018, https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620) in research_notes/catalog_parts/05_memory.md; briefs 04, 09, 11, 12 and 00_SYNTHESIS.md in research_notes/idea_generation/
