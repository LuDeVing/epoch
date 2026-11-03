# Soar: other memories and RL: deep document

*Subfield C02.04. Scope: Soar's episodic memory, semantic memory and reinforcement learning (operator preference learning), and what LLM-agent memory work shows about the same ideas. Built from evidence_a-d.jsonl (ids a01 to d19), claims.jsonl (K01 to K24) and critique.md in this folder. Pages marked [V] were opened in full or in part; [M] were seen only as snippets or citations. Related subfields researched in parallel and not covered here: Dynamic memory and early CBR, Failure-driven CBR, Map versus value replay, Learned refinement and self-verification, ACT-R production selection, MDPs and POMDPs, Cognitive maps, Semantic networks and spreading activation, Count-based exploration.*

## 1. What it is

Soar (Laird, Newell, Rosenbloom) is a cognitive architecture. Its core is a decision cycle. Rules propose operators, preferences rank them, one operator is applied. When the preferences cannot decide, Soar hits an impasse and opens a substate. That part is covered in other documents. This document covers the three long-term stores added in Soar 9 (Laird 2012, the MIT Press book, [M] only; see c05, c06, c17, c26):

1. **Episodic memory.** An automatic record of what happened. After each decision, a snapshot of the top state goes into the store. Only changes are stored. The agent cannot read it freely. It must build a cue (a partial state), and the best match is rebuilt in a reserved area of working memory. It can then step to the next or previous episode. (a01, a15, a16, b04, c01)
2. **Semantic memory.** Context-free facts, kept as graphs in the same form as working memory. Retrieval is by cue. The winner has the highest activation: base-level activation (recency, frequency, noise) plus spreading activation from working memory. Nothing is learned automatically; the agent stores facts on purpose. (a13, a14, b03, c01)
3. **Reinforcement learning (RL).** Numeric preferences on operators, held in rules. Their values are updated by temporal difference learning (Sarsa or Q-learning) from reward. RL only changes the choice among operators that rules already proposed. (a11, a12, b01, b02, c02)

Why these matter for our agent. The schema (SCHEMA.md) has a thin memory: one-line lessons by problem class, a class record in code (plain pass rate, agreement record, which operators solved subgoals), and a planned subgoal library. S0 reads the class record. S9 writes a lesson and updates it. Soar's three stores are a worked-out design for exactly these pieces:

| Soar part | Schema counterpart |
|---|---|
| Episodic store (automatic write, deliberate cue read) | S9 write / S0 read of the class record |
| Semantic store (distilled facts, separate from episodes) | Lessons, kept apart from raw records |
| Operator preference RL (tie-break only, safety rules in charge) | Operator choice at S6 under guardrails G1 to G12 |

Honest limit. The Soar evidence is old (2004 to 2013), from toy worlds (Eaters, TankSoar, Well World, Flip), mostly shown as graphs, with small n. The numbers for LLM agents come from 2023 to 2026 papers, many on GPT-4-era models. No published study runs Soar memory against an LLM-agent memory on one benchmark (c27, K17). Links are by analogy (CoALA, Pink 2025, Wray 2025).

## 2. History and theories in depth

### 2.1 Episodic memory in Soar

- **2004, Soar-EM (Nuxoll and Laird, ICCM).** First model. Each state has 31 to 36 features and only 2 decide the right move. Five iterations of 1500 internal decisions (about 130 world actions) per run, five runs averaged. Matching by count of shared features gave only a small gain over random. Biasing by working-memory activation (recency and frequency of use) lifted the eater to the level of a greedy agent. The authors estimated over 1 quadrillion possible inputs. Worst-case retrieval is linear in the number of episodes. (a06)
- **2012, Nuxoll and Laird, Cognitive Systems Research.** The mature design. Snapshot per action, only changes stored, elements under an activation threshold left out. Recording every cycle instead of every action "had little impact on performance". Match score = cardinality of shared elements plus activation of matched elements; in the Soar 9 manual this is `balance x cardinality + (1 - balance) x activation`, with a second structural graph match for perfect-cardinality hits. Below a threshold, retrieval fails, and that failure is a signal the agent can use. The authors state the memory has no forgetting, no consolidation, no generalisation across episodes, no model of time. Soar 9 later dropped activation-biased retrieval for speed and defaults to recency. (a01, a15, b04)
- **Use cases shown in 2012** (all toy, all graphs): action modelling in Eaters (cue with state plus proposed move, fetch the best match, then step to the next episode and read the score change); decision making in TankSoar (retrieve a similar episode, replay up to ten following episodes, score the net change in game score with a discount; three tactics emerged: dodge short-range missiles, back away while firing, break line of sight when losing); retroactive learning (act randomly, pause, query episodes for every neighbour-cell pattern, chunk rules, then act near ideal); boosting chunking (chunk the result of episodic decisions, removing later retrievals); virtual sensing (blind tank chains remembered paths to the battery, about ten times faster than random search). (a02 to a05)
- **2009/2011, Gorski and Laird.** RL can learn when to retrieve, which cue to use, whether to step to the next episode, and how to build a cue from several features, while learning the task. Plain RL cannot solve these tasks. Well World rewards: external action -1, internal action -0.1, thirsty step -2, safety +2, satisfied thirst +8; 250 trials averaged. Single-cue task reached the optimum, slower with 5 distracter cues; temporal task reached its asymptote after about 4,500 actions, often not fully optimal; conjunctive cues reached the optimum, slower with 2 distracters. Every trial in the temporal task converged to the optimal policy or to a "toggle a bit" policy that uses retrieval as a flag. (a07) The convergence table (a08) was unparseable and must not be cited.
- **2009/2012, scaling (Derbinsky and Laird; Derbinsky, Li, Laird).** Cost of retrieval grows with the age of the thing sought. A new cue-matching index keeps retrieval real time: over 100 cues, 44 instances of 12 planning domains, word-sense disambiguation, 3 video games and a robot. Robot, 12 hours: baseline stored over 58 million episodes and passed 50 ms in under 12 hours; the variant stored nearly 109 million, max cue-match time grew 3.6x slower (before a task shift) and 4.9x slower (after), projected under 50 ms to about 694 million episodes (over 3 days). Boundary: depends on cue type and whether distinct structures grow over the agent's life; the goal-management cue still slowed. An earlier version reported about 50 ms with 1M episodes over 14 hours ([M] snippet, b25). (a10, b05, b06)
- **2013, ZigguSoar (Wallace, Dickinson, Nuxoll).** A cheap hash of recent history replaces full episodic recall. When an operator rule's reward variance shows hidden state, the rule is specialised on a short history. In the Flip environment (20 runs, first 10,000 steps) baseline Soar RL learned only the deterministic Up prediction; ZigguSoar learned both Up and Left. The rule count grows without bound, since no finite history suffices. Assumes a deterministic world, one small environment. (a09, b07, b08)
- **2022, Phujus (Lane et al.).** Episodes stored as rules chained by internal sensors, for perceptual aliasing and noise. Initial evidence only; no numbers captured; rule database grows exponentially. (a20)

### 2.2 Semantic memory in Soar

Facts as graphs, cue-based retrieval, activation as in ACT-R (Petrov approximation of base-level; spreading activation additive on top, flowing along stored graph links). The reason for a separate store: the cost of rule matching rises with the amount of knowledge in working memory, so context-free facts go to a store with cheap cue retrieval. There is no automatic learning; storage is a deliberate act. (a13, a14, b03) Spreading activation is covered by a parallel subfield. The point for us is the split: episodes are specific and stay raw; distilled facts and lessons live apart. (K07)

### 2.3 Reinforcement learning in Soar

- **Design (Nason and Laird 2005, [M]; manual; Laird 2022).** An RL rule has one numeric-indifferent preference on a proposed operator. Q for an operator is the sum of all matching RL rules: a linear approximator with binary features. Defaults: learning rate alpha 0.3, discount gamma 0.9, eligibility traces off (decay 0), softmax exploration by default (manual advises epsilon-greedy or Boltzmann). Update: delta = alpha [r + gamma Q(s',a') - Q(s,a)] for Sarsa. Learning applies in every substate with independent rewards, so planning in a substate gives model-based RL and the top state gives model-free RL. Reward is summed from rule-created reward structures; there is no built-in intrinsic reward; rates are fixed at agent start. (a11, b01, b02, c02)
- **Key design rule.** RL influences selection only when other preferences cannot decide. Hard-coded safety knowledge stays in charge. That cuts risk and speeds learning. (a12, c02, K04)
- **Chunking meets RL.** Chunking can create RL rules whose starting value comes from substate evaluation; experience then tunes them. Chunking can also compile the result of a semantic or episodic retrieval. In stochastic settings the eager learner can compile wrong answers from the episodic store. (c04, a04)
- **Papers not opened:** Nason and Laird 2005 (a18, b24, c05), Laird 2012 (a17, c26), Derbinsky and Laird 2013 on forgetting (a19). Claims about them rest on the manual and Laird 2022.

### 2.4 The bridge to LLM agents

- Sumers, Yao et al. (CoALA, 2023) map language agents onto Soar's memories (working, episodic, semantic, procedural) and say writing to episodic or semantic memory is much safer than writing to procedural memory. They note that learning of retrieval is not studied in recent language agents. (b10, c10, c11)
- Pink et al. (2025) argue LLM agents need episodic memory with five properties: long-term storage, explicit reasoning over it, single-shot learning, instance-specific content, contextual relations. Position paper, no experiment. (a21, c12)
- Wray, Kirk, Laird (2025) compare Generative Agents memory with Nuxoll and Laird's list. It is only partly automatic, not episodically segmented, not deliberately cued, and relevance uses semantic similarity, not encoding specificity. Reflexion caches lessons within a task, little across tasks. (a22)
- Fan and Lan (2026) review 10 architectures and 42 modern systems. Modern agents rebuilt adaptive memory and failure recovery by independent convergence, not documented inheritance from Soar. (b22)
- The Soar group's own LLM work uses the architecture as a vetting layer (see 6.5): Kirk et al. (STARS), Yuan et al. (NL2GenSym), Wray et al. 2021. (a31, a32, a33, c07 to c09)

## 3. Core findings with exact numbers

Status: E = established (2 or more independent sources), S = single source, C = contested. Sources are evidence ids.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Episodic memory alone gives action models, outcome evaluation and virtual sensing in toy domains | Eaters: failure rate falls toward perfect prediction (graph only). TankSoar: margin of victory from negative to positive, 10 repetitions. Battery search about 10x faster than random | a01 to a05, c03 | E (toy, graphs only) |
| Count-only matching is near random; activation or recency bias is needed | 31-36 features, 2 relevant; unbiased slightly above random; biased near greedy bound | a06, a15, a07 | E |
| Soar RL can learn when and how to retrieve | Well World, 250 trials; temporal task asymptote about 4,500 actions, sometimes a "toggle" policy | a07 | S |
| RL only breaks ties; safety rules stay in charge | Defaults alpha 0.3, gamma 0.9 | a11, a12, b01, c02 | E |
| Hidden state breaks plain RL; a short recent-history hash fixes it in a toy world | Flip, 20 runs, 10,000 steps: baseline 1 of 2 predictions, ZigguSoar 2 of 2 | a09, b07 | S |
| Retrieval cost scales with lifespan; index keeps it real time | 3.6x and 4.9x slower growth; 58M vs 109M episodes in 12 h; 50 ms limit projected to 694M | a10, b05, b06 | S |
| Episodic memory has no generalisation or forgetting; semantic store holds facts | Author statements | a01, b04, a13, b03 | E |
| Reflexion: written lessons from failed tries lift repeated-trial performance | ALFWorld (134 tasks) +22% absolute in 12 trials, 130 of 134 solved; HotPotQA +20%; HumanEval pass@1 91% vs 80% (GPT-4); memory size 3; ReAct-only hallucination plateau 22% | a24, b11, c13 | E |
| Reflection adds over the raw last trajectory | HotPotQA, 100 questions, ground-truth context: +8% absolute over episodic-only | c14 | S |
| A lesson step without a trustworthy test hurts | HumanEval Rust, 50 hardest: base 60%, no tests 52%, no reflection 60%, full 68%. False-positive test rate 16.3% (MBPP Python) vs 1.4% (HumanEval Python) | b12 | S |
| Agents copy the most similar stored record (error propagation, misaligned replay) | 4 agents; add-all opens a gap to error-free memory that grows; strict admission plus history-based deletion beats error-free memory on AgentDriver after about 2000 executions; coarse evaluator removes the gain | a27, b20, b21, c19 | S |
| Distilled lessons beat raw trajectories (not token matched) | WebArena (684 tasks) Gemini-2.5-flash: none 40.5, raw Synapse 42.1, AWM 44.1, ReasoningBank 48.8, +MaTTS 51.8. Pro: 46.7/47.7/47.6/53.9/56.3. Claude-3.7: 41.7/42.6/40.8/46.3/48.8. SWE-Bench-Verified flash 34.2/35.4/38.8; pro 54.0/53.4/57.4 | d01, d04 | S |
| Learning from failures needs an extractor built for it | Synapse 40.6 (success only) to 41.7 (with failures); ReasoningBank 46.5 to 49.7 | d02 | S |
| Raw full history can be worse than no memory | GPT-4o AIME 2024: baseline 20.0, full history 6.7, curated cheatsheet 40.0 (DC-RS). Claude 3.5 Sonnet: 23.3, 26.7, 50.0 | d07, d08 | S (one paper, two models) |
| Success-only workflow memory can fall below none on transfer | WebArena Multi (29 tasks), flash: none 10.3, AWM 3.4, ReasoningBank 13.8; Claude overall 41.7, 40.8, 46.3 | d05 | S |
| Write gating works with a modest judge | Judge 72.7% accurate; simulated 70 to 90% similar (about 47 to 53 vs 39.0 none on WebArena-Shopping); best at 100%; ACE without labels +14.8 over ReAct using execution success as signal | d03, d11 | E |
| Whole-memory rewrite collapses it | AppWorld: 18,282 tokens at 66.7 accuracy to 122 tokens at 57.1, below baseline 63.7 | d10 | S |
| Cue quality is a large lever | ALFWorld task-similarity retrieval 59.0 vs random 42.5; LongMemEval (Gemini-1.5-Flash) RAG GTE 63.6, RMM 70.4, oracle retrieval 90.2 | d06, d15, a06 | E |
| Index design helps recall | LongMemEval fact-augmented keys +9.4% recall@k, +5.4% accuracy; time-aware query +11.3% recall (rounds), +6.8% (sessions). Right retrieval, wrong generation: 15 to 19% of instances (40 to 50% of errors) | b15 | S |
| Long chat memory is hard | LongMemEval: GPT-4o oracle 0.870 vs 0.606 on long version (30.3% drop); Llama 3.1 8B 0.660 vs 0.342 (48.1%); ChatGPT 0.5773; offline reading 0.9184. LoCoMo: human F1 87.9, best model 32.4 | a29, b14, b16, c20 | E |
| Structured stores often do not beat long context (vendor) | LoCoMo J: full context 72.90 at 26,031 tokens (p95 17.1 s); Mem0g 68.44; Mem0 66.88 (p95 1.44 s); Zep 65.99; LangMem 58.10; OpenAI 52.90; A-Mem 48.38; best plain RAG 60.97 | a26, b18 | S |
| Structured stores can lose to the plain backbone (independent) | Overall: GPT-4o-mini 42.3; BM25 RAG 41.5; HippoRAG-v2 41.6; Mem0 21.1; Cognee 20.6; Zep 24.0; GPT-5-mini long context 60.6; multi-hop update at most 28% | b19 | S (in tension with vendor paper) |
| Self-managed paging lifts retrieval | Deep memory retrieval: GPT-3.5 38.7 to 66.9; GPT-4 32.1 to 92.5; GPT-4 Turbo 35.3 to 93.4 | b17, c16 | S |
| Believability falls when memory, reflection, planning are ablated | TrueSkill 29.89 full, 26.88 no reflection, 25.64 no reflection or planning, 22.95 crowdworker, 21.21 fully ablated; d = 8.16; 100 raters | a23, b13, c15 | S (ratings, not accuracy) |
| RL on memory operations beats scripts (needs training) | LoCoMo, LLaMA-3.1-8B, 152 training pairs: Memory-R1-GRPO F1/J 45.02/62.74 vs Mem0 30.41/45.68, A-Mem 29.20/44.76, RAG 11.41/13.62 | a28, c24, c25, d17 | S |
| LLMs do not explore reliably in context | Bandits: 1 of 168 configs worked (GPT-4 + hint + code-computed per-arm averages + CoT) | d13 | S |
| Memory gains persist on a 2025 model; not on R1/o1 for reasoning tasks | GPT-5.1 AppWorld base 54.2, online ACE 65.8 (+11.6), offline +7.1; DC on R1/o1 minimal or inconsistent | d12, d09 | S |
| Vetting LLM knowledge in the architecture raises success | STARS 77.5/94.4/92.9 vs template 52.5/66.7/35.7; NL2GenSym 86% with critic, ablating critic -23% | c08, c09, a32 | S |
| Skill library of verified code plus self-verification | Voyager: 63 items, 3.3x baselines; no self-verification -73%; random curriculum -93% | a25, c18 | S |

Do not cite: Gorski and Laird Table 1 numbers (a08). Not re-verified in the cross-check: Derbinsky 2012 scaling numbers, STARS percentages, Memory-R1, ExpeL, Voyager, A-Mem figures.

## 4. Mechanisms and models

Each mechanism is written so it can be built as code around a model, with no weight training.

### 4.1 Episodic record (write, cue, read)

1. **Write.** After each attempt, code (not the model) writes one record: problem class, the state features that were visible, the operator or mode used, the outcome (pass/fail from a check), tokens spent. Only changes from the previous record need storing. Recording every cycle instead of every action made little difference in Soar, so write per attempt, not per token.
2. **Cue.** A cue is a partial state: a few features plus the proposed operator. Build it on purpose. In Soar the cue "state plus proposed move" is what makes outcome prediction work (a02).
3. **Match.** Score = balance x (shared features) + (1 - balance) x (recency or activation). Count alone is near random when most features are irrelevant (a06). Add a recency term. Break ties by most recent. Return nothing if the score is below a threshold. Treat "nothing found" as a signal (a01).
4. **Step.** After a hit, read the next record (what happened after) to get the outcome. That is the action-model pattern.
5. **Never rewrite.** Edit by append and counter, never by whole rewrite (d10).

### 4.2 Separate lesson store (semantic analogue)

Distilled lessons, one line each, live apart from raw records. A lesson is created from a record only after verification (4.4). Keep counters (helped, hurt) per lesson; ExpeL's up/down votes prune bad insights (d06). ACE: append small delta items with counters; a detailed playbook beat a short summary (d10).

### 4.3 Operator preference without weights

Soar RL: Q(s,a) = sum of matching rule values, updated by delta = alpha [r + gamma Q(s',a') - Q(s,a)] with alpha 0.3, gamma 0.9. In-context version for us:

1. Keep per-class, per-operator counts in code: tries, solved subgoals, tokens spent.
2. At S6, code ranks untried-or-promising operators from the counts (an epsilon-greedy or optimistic rule written in code). The model never computes it, because LLMs do not explore reliably in context and only a code-computed per-option summary worked (d13).
3. Guardrails veto first. Learned preference only breaks ties among operators the schema already allows (K04).
4. If outcomes differ on identical visible state, add a short history feature to the key (the ZigguSoar idea, b07).

### 4.4 Write gating

A record or lesson is committed only when a verifier has run. Order of reliability: a programmatic check or execution result; a held-out or fresh-input test (G3); a modest LLM judge (72.7% accurate was enough in d03); nothing (memory can degrade, d11, b12). Soar-group work shows the same pattern: STARS and NL2GenSym run LLM output inside the architecture before storing it (c08, a32).

### 4.5 Retrieval policy

Let code decide when to retrieve. Options: always retrieve at S0 (cheap, from the class record); retrieve on demand when an impasse fires. MemGPT-style self-managed paging helped (b17) but costs model calls and was tested on GPT-4-era models. Soar RL learning when to retrieve works in toy tasks, but needs thousands of trials (a07).

### 4.6 Cost control

Cap record size. Soar needed an index only past millions of episodes; our records number in hundreds, so a flat list in code is enough (K06).

## 5. What holds up

**Replicated or multi-source (treat as reliable):**
- Cue and retrieval quality decide whether memory helps. Three independent lines: Soar-EM (count vs activation, a06), ExpeL (59.0 vs 42.5 random, d06), LongMemEval and RMM (63.6 vs 90.2 oracle, d15, b15).
- A verifier gates whether memory helps. Reflexion's Rust ablation (b12), Xiong's evaluator quality (b20, c19), ReasoningBank judge study (d03), ACE feedback signal (d11), Voyager self-verification (a25).
- Raw history is not a safe default. Dynamic Cheatsheet on two models (d08), AWM on transfer (d05), ReasoningBank raw trajectories gaining only 1.6 on WebArena flash and losing to none on SWE-Bench pro (d01, d04).
- Plain long context is a strong baseline when the history fits: Mem0 paper (a26), Hu et al. (b19), LongMemEval (b14).
- RL is a tie-breaker under hard rules: Soar manual, Laird 2022 (K04).

**Failures and tensions:**
- Mem0 paper (extracted memory close to full context, far cheaper) versus Hu et al. (Mem0 21.1 vs backbone 42.3). Different benchmarks, different backbones, vendor versus independent. Treat vendor numbers as upper bounds. Not reconciled (critique).
- Reflexion's reflection step: +8 on 100 HotPotQA questions with ground-truth context, but no gain over base in the Rust ablation (60 = 60). Value is task-dependent. Wray et al. 2025: lessons carry little across tasks.
- ExpeL: insights-only and retrieve-only each lose to the full system, and which matters more changes with the task (HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38) (d06).
- Dynamic Cheatsheet gains are large when one reusable trick exists (GPT-4o Game of 24: 10 to 99) and small or negative elsewhere; R1 and o1 gained little (d07, d09).
- Believability results (Generative Agents) are ratings, not task success; they do not tell us about accuracy (c15).

**Boundary conditions:**
- Soar results assume consistent outcomes. Where outcomes were unreliable, behaviour was more variable (a03). Eager chunking from episodes can compile wrong answers in stochastic settings (a04).
- ZigguSoar assumes a deterministic world.
- Reflexion assumes the same task repeats with a clear pass/fail signal.
- Scaling results depend on cue type (b06).

**Interventions that worked:** distilled strategy items with failures included (ReasoningBank); counters and delta edits (ACE); strict selection before writing plus history-based deletion (Xiong, with a strict evaluator); fact-augmented keys and time-aware query (LongMemEval); code-computed outcome summaries for exploration (d13); programmatic verification before storing (Voyager).

**Interventions that did not work:** adding every run (error propagation); full rewrites of the memory (collapse, d10); raw full history on GPT-4o (6.7 vs 20.0); success-only workflows on transfer (AWM 3.4 vs 10.3); count-only cue matching; deletion with a coarse evaluator; LLM self-exploration in bandits (167 of 168 configs failed).

## 6. Language models

### 6.1 Reflexion-style retry memory
GPT-4-era models. ALFWorld +22 points in 12 trials; HotPotQA +20; HumanEval 91 vs 80. The lesson step added 8 points over just keeping the last trajectory (N=100). Rust ablation shows the lesson step alone brought nothing when test generation was dropped (60), and removing tests gave 52. So the gain needs a trustworthy signal. (a24, b11, b12, c14)

### 6.2 Distilled memory across tasks
ReasoningBank on three backbones (Gemini-2.5-flash, Gemini-2.5-pro, Claude-3.7-sonnet): +8.3, +7.2, +4.6 points over no memory on WebArena; on SWE-Bench-Verified +4.6 (flash) and +3.4 (pro). Raw trajectories gave +1.6, +1.0, +0.9 on WebArena and +1.2 (flash) and -0.6 (pro) on SWE-Bench. ExpeL transfers HotpotQA to FEVER (ReAct 58%, ExpeL 65 to 70%). AWM: +24.6% relative on Mind2Web, +51.1% relative on WebArena; online +8.9 to 14.0 absolute as train-test gap widens. No study here is token matched. (d01, d04, c17, d14)

### 6.3 Curated versus raw context
Dynamic Cheatsheet: Claude 3.5 Sonnet AIME 2024 23.3 baseline, 26.7 full history, 50.0 cheatsheet; GPT-4o 20.0, 6.7, 40.0 (retrieval-synthesis). Uncurated retrieval of raw pairs: GPT-4o 26.7 vs 40.0. (d07, d08)

### 6.4 Newer and reasoning models
ACE with GPT-5.1 on AppWorld: 54.2 to 65.8 (+11.6). Gains across four model families are mostly 5 to 12 points. R1 and o1 gained minimal or inconsistent amounts from a cheatsheet. Nobody has run memory with extended thinking on and off. (d12, d09, K23)

### 6.5 Verification layers (the Soar-group view)
STARS: template prompting 52.5, 66.7, 35.7% (kitchen, groceries, office); with vetting inside Soar 77.5, 94.4, 92.9%. Over 70% of raw LLM responses were not viable; for one task only 13% were situationally relevant. Accepted proposed goals under oversight rose 33 to 69, 62 to 94, 18 to 73%. NL2GenSym (water jug): Gemini-Flash with framework 86% success; ablate critic -23% (-37% on hard cases), basic knowledge base -17%, case knowledge base -14%. Kirk et al. 2022 (GPT-3, human judged): over 60% of responses relevant and interpretable for tidying a room, over 80% at the best setting. Verification of LLM-proposed knowledge before storage pays off, on old or narrow setups. (c08, c09, a32, a31)

### 6.6 Chat memory systems
Long-context models lose 30 to 60% at about 115k tokens (LongMemEval). LoCoMo: best model F1 32.4 vs human 87.9, 56% gap overall, 73% temporal. gpt-3.5-turbo-16K adversarial F1 2.1. Product memories (ChatGPT 0.5773, Coze 0.3299 on GPT-4o) lose heavily against offline reading (0.9184). Mem0 versus independent re-test: see section 5. MemGPT paging: +60 points for GPT-4. A-Mem: LoCoMo multi-hop ROUGE-L 44.27 vs 18.09 for the LoCoMo baseline. RULER: effective context lengths are shorter than claimed (GPT-4: 96.6 at 4K, 87.0 at 64K, 81.2 at 128K; effective 64K). (a29, b14 to b19, c23, d16)

### 6.7 Exploration and operator preference
Krishnamurthy et al.: GPT-3.5 and Llama2 had 48 configs each and GPT-4 had 72; only GPT-4 with a suggestive hint, history summarised into per-arm averages by code, and zero-shot CoT worked (T=200, N=40). The basic GPT-4 prompt failed in over 60% of runs. So Soar-RL-style learning must be done by counting outside the model. (d13)

### 6.8 RL on memory
Memory-R1 (training needed): GRPO beat PPO by about 4 F1 on LLaMA-8B; removing the learned manager lowers scores; gains held over 3B to 14B. Outside our no-training rule; it only shows that memory-operation quality matters. (a28, c24, c25, d17)

## 7. What our agent should take

Schema part key: G guardrail, S state, O operator, memory = Section 5 of SCHEMA.md.

### Add now (established)

1. **Class record keeps per-operator counts and is written by code after a verified outcome.** Part: memory / S9 write, S0 read. [E] K01, K04. Ev: a01 to a05, a11, a12, c02.
2. **Retrieval cue = state features + proposed operator, with a recency tie-break; "no match" is a signal, not an error.** Part: memory / S0. [E] K02, K21. Ev: a06, a15, d06, d15, b15.
3. **Write gating: store a record or lesson only after a programmatic or held-out check; a weak judge is acceptable if lessons are abstractions.** Part: G (extends G3, G7) / memory / S9. [E] K20. Ev: d03, d11, b12, b20, a25.
4. **Keep lessons (distilled) apart from raw records (episodic).** Part: memory. [E] K07. Ev: a01, b04, a13, b03.
5. **Learned operator preference only breaks ties; guardrails and hard rules veto first.** Part: G / O / S6. [E] K04. Ev: a11, a12, b01, c02.
6. **Do not default to dumping full history into context; compare any record with the plain model at equal tokens (already G7).** Part: G7 / memory. [E] K11, K19. Ev: d08, b19, a26, b14.
7. **Edit memory by append and counter, never by full rewrite.** Part: memory. [S] K24, but low risk, so adopt. Ev: d10.
8. **Retries (S5 loop) carry a written lesson only when a real failing output exists.** Already G2; Reflexion supports it. [E] K08. Ev: a24, b11, b12, c13, d01.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Distilled class record vs raw prior solutions vs no record at equal tokens | memory / S0 | [S] K18 | d01, d02, d04, d07, d10 |
| Verifier-quality threshold: how bad can the gate be before memory hurts? | G / memory | [S] K10, K20 | d03, d11, b12, a27 |
| Counts-based operator ranking at S6 vs fixed order | O / S6 | [S] K22 | d13, a11 |
| Short recent-history feature when outcomes differ on identical visible state | memory | [S] K05 | a09, b07 |
| Cue ablation: state only vs state + operator vs + recency | memory / S0 | [E] K21 (our form of cue is new) | a06, d06, d15 |
| Deletion or demotion of records with bad later utility | memory / G | [S] K10 | a27, b21, c19 |
| Memory with extended thinking on vs off | memory / G11 | [S] K23 | d09, d12 |
| Self-managed retrieval (agent decides when to query) vs always-retrieve | memory / S0 | [S] K13 | b17, c16 |
| Lesson shown after first attempt vs before (fixation) | memory | [D] in SCHEMA | no direct evidence here |
| Lesson trust rule (helps on two different problems) | memory | [S] | d06 votes |

Not for the agent: learned retrieve/skip policy by RL (K03, too slow, a07), RL training of memory managers (K15), episodic scaling indexes (K06), believability metrics (K14).

## 8. Concrete tests on our bench

All arms use equal total tokens including setup (G7). Items come from the existing benches (ARC portfolio, BRAINTEASER, NoveltyBench where relevant). Every run logs path, tokens per state, record hits.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Repeated problem classes, 3 to 5 items per class, run in sequence | (a) no record, (b) raw earlier solutions in context, (c) distilled class record with counts | Pass rate on items 2 to N of each class | (c) > (a) by a few points; (b) near (a) or below (as 1.6 vs 8.3 points in ReasoningBank, 6.7 vs 40 in DC) |
| T2 | Same stream, record writes gated | (a) add-all, (b) programmatic-verifier writes only, (c) verifier writes with a degraded judge (flip 20, 30, 40% of labels), (d) verified + demotion | Pass rate over first 100 items; error-propagation rate (wrong record reused) | (b) best; (c) holds at 70-90% accuracy, drops near 50-60%; (a) opens a gap that grows |
| T3 | Items where operator choice matters (S6 impasses, ARC) | (a) fixed operator order, (b) random, (c) code-computed success counts, epsilon-greedy | Subgoal-solved rate per impasse; tokens to first pass | (c) > (a) once a class has 10+ impasses; none if classes are too small |
| T4 | Items with outcome variance on the same visible features | (a) key = visible features, (b) key + last two outcomes | Accuracy of predicting operator success; pass rate | (b) better only where variance exists (ZigguSoar pattern) |
| T5 | Retrieval cue ablation | (a) problem text only, (b) state features, (c) features + proposed operator, (d) + recency | Hit rate of the useful record (oracle labels); pass rate | (c)/(d) > (a); gap size unknown; ExpeL's gap was 16.5 points |
| T6 | Memory with thinking on / off | record on/off x thinking on/off | Pass rate and tokens | Smaller record gain with thinking on (R1/o1 hint); if the gain vanishes, drop the record for those modes |
| T7 | History that fits in context | (a) full history, (b) record, (c) RAG | Accuracy and tokens | Full history wins when it fits and the model is strong; find the length crossover (RULER effective length) |
| T8 | Lesson placement | (a) lesson after first attempt, (b) lesson before | Pass rate; diversity of first attempts | (a) avoids fixation; effect size unknown |
| T9 | Retrieval policy | (a) always retrieve at S0, (b) retrieve only at impasse, (c) model decides | Pass rate, tokens | (a) or (b) cheapest; (c) only if clearly better |

## 9. What does not transfer, and why

- **Weight-based RL.** Soar-RL updates numbers in rules by TD. A model with no training has no such place. Only the counting part transfers (4.3). Memory-R1 needs training and is out of scope.
- **Million-episode scaling.** Soar's index work solves a problem we do not have; a flat list suffices. (K06)
- **Automatic per-cycle snapshot of the whole working memory.** A model's working memory is the context; the snapshot would be the prompt. We store a compact record per attempt instead.
- **Learning a retrieval policy by trial and error (Gorski and Laird).** Needs thousands of actions and a stable reward; our items are few and heterogeneous.
- **Spreading activation and base-level decay as such.** Without a graph store, a recency term is the only part we use. Covered by the semantic-network subfield.
- **Believability ratings.** Not task accuracy.
- **Chat-memory benchmarks (LongMemEval, LoCoMo).** They test personal-fact recall over sessions; our items are problem solving. Only the lessons on index design and the long-context baseline carry over.
- **Hidden-state RL results.** ZigguSoar assumes a deterministic world; our verifier outputs are noisy.
- **GPT-4-era numbers.** Reflexion, Generative Agents, Voyager and MemGPT were not retested on current models; effect sizes may shrink.

## 10. Open questions

1. At equal tokens, does a distilled class record beat raw earlier solutions or full history on current models? (Partly closed by ReasoningBank and DC; none is token matched.)
2. What is the minimum verifier accuracy below which memory hurts? (70% was fine; below that, unmeasured.)
3. Does a cue of state plus proposed operator change the hit rate? No LLM measurement exists.
4. Where is the crossover between full context and a store, in tokens, for agent memory? The Mem0 paper and Hu et al. disagree.
5. Can Soar-RL-style operator preference be approximated in context from counts, and does it beat fixed order?
6. Do short recent-history cues fix hidden-state failures in LLM agents? No LLM study found.
7. What do forgetting and deletion policies do beyond the four agents Xiong tested? Memory-R1 and MemoryBank have no isolated deletion ablation.
8. What are the true numbers in Gorski and Laird Table 1 and Nason and Laird 2005? Primary PDFs not reachable.
9. Do memory benefits persist for strong reasoning models with extended thinking?
10. Do lessons carry across tasks, or only within a task (Wray et al. 2025 say little)?

## 11. Sources

[V] = opened this session (full text or major part). [M] = snippet or citation only.

- [V] Nuxoll & Laird (2012) Enhancing intelligent agents with episodic memory, Cognitive Systems Research 17-18:34-48 - https://web.eecs.umich.edu/~soar/sitemaker/docs/pubs/1-s2.0-S1389041711000428-main.pdf (ids a01, a02, a03, a04, a05)
- [V] Nuxoll & Laird (2004) A cognitive model of episodic memory integrated with a general cognitive architecture, ICCM - https://users.cs.northwestern.edu/~mek802/papers/not-mine/cog-arch/nuxoll-2004-ICCM-epmem.pdf (ids a06)
- [V] Gorski & Laird (2011) Learning to use episodic memory, Cognitive Systems Research 12:144-153 (ICCM 2009 version read) - https://iccm-conference.neocities.org/2009/proceedings/cd/papers/122/paper122.pdf (ids a07, a08)
- [V] Wallace, Dickinson & Nuxoll (2013) Hashing for lightweight episodic recall, AAAI Spring Symposium on Lifelong Machine Learning - https://www.aaai.org/ocs/index.php/SSS/SSS13/paper/view/5764 (ids a09)
- [V] Derbinsky, Li & Laird (2012) Algorithms for scaling in a general episodic memory, AAMAS extended abstract - https://www.ifaamas.org/Proceedings/aamas2012/ (ids a10)
- [V] Soar Manual 9.6+ (2017-), chapter 5 Reinforcement Learning - https://soar.eecs.umich.edu/soar_manual/05_ReinforcementLearning/ (ids a11)
- [V] Laird (2022) Introduction to the Soar Cognitive Architecture - https://arxiv.org/abs/2205.03854 (ids a12, a13, a16, b01, b02, b03, b04, c01, c02, c03, c04)
- [V] Soar Manual, chapter 6 Semantic Memory (activation and retrieval) - https://soar.eecs.umich.edu/soar_manual/06_SemanticMemory/ (ids a14)
- [V] Soar Manual, chapter 7 Episodic Memory - https://soar.eecs.umich.edu/soar_manual/07_EpisodicMemory/ (ids a15)
- [M] Laird (2012) The Soar Cognitive Architecture, MIT Press - https://mitpress.mit.edu/books/soar-cognitive-architecture (ids a17)
- [M] Nason & Laird (2005) Soar-RL: integrating reinforcement learning with Soar, Cognitive Systems Research 6:51-59 - https://www.semanticscholar.org/paper/533804e6b267efb30ab754fe94e826a94eb163e6 (ids a18)
- [M] Derbinsky & Laird (2013) Effective and efficient forgetting in Soar's working and procedural memories; Derbinsky, Laird & Smith (2010) large declarative memories - https://www.sciencedirect.com/science/article/pii/S1389041712000320 (ids a19)
- [V] Lane, Morgan, Vickers, Woods & Nuxoll (2022) Towards an artificial, general episodic memory via learning in noisy, perceptually-aliased environments, ACS 10 - https://advancesincognitivesystems.github.io/acs2022/data/acs22_paper-7339.pdf (ids a20)
- [V] Pink et al. (2025) Position: Episodic memory is the missing piece for long-term LLM agents - https://arxiv.org/abs/2502.06975 (ids a21, b09, c12)
- [V] Wray, Kirk & Laird (2025) Applying cognitive design patterns to general LLM agents - https://arxiv.org/abs/2505.07087 (ids a22)
- [V] Park et al. (2023) Generative Agents: interactive simulacra of human behavior - https://arxiv.org/abs/2304.03442 (ids a23, b13, c15)
- [V] Shinn et al. (2023) Reflexion: language agents with verbal reinforcement learning - https://arxiv.org/abs/2303.11366 (ids a24, b11, b12, c13, c14)
- [V] Wang et al. (2023) Voyager: an open-ended embodied agent with LLMs - https://arxiv.org/abs/2305.16291 (ids a25, c18)
- [V] Chhikara et al. (2025) Mem0: production-ready AI agents with scalable long-term memory (LoCoMo) - https://arxiv.org/abs/2504.19413 (ids a26, b18, c22)
- [V] Xiong et al. (2025) How memory management impacts LLM agents: experience-following - https://arxiv.org/abs/2505.16067 (ids a27, b20, b21, c19)
- [V] Yan et al. (2026) Memory-R1: managing and using memory with reinforcement learning - https://arxiv.org/abs/2508.19828 (ids a28, c24, c25, d17)
- [V] Wu et al. (2025) LongMemEval: benchmarking chat assistants on long-term interactive memory (ICLR) - https://arxiv.org/abs/2410.10813 (ids a29, b14, b15, c20, c21)
- [V] Sumers, Yao, Narasimhan & Griffiths (2024) Cognitive architectures for language agents (CoALA), TMLR - https://arxiv.org/abs/2309.02427 (ids a30, b10, c10, c11)
- [V] Kirk, Wray, Lindes & Laird (2022) Improving language model prompting in support of semi-autonomous task learning - https://arxiv.org/abs/2209.07636 (ids a31)
- [V] Yuan et al. (2025) NL2GenSym: natural language to generative symbolic rules for Soar via LLMs - https://arxiv.org/abs/2510.09355 (ids a32)
- [V] Wray, Kirk & Laird (2021) Language models as a knowledge source for cognitive agents - https://arxiv.org/abs/2109.08270 (ids a33, c07)
- [V] Derbinsky, Li, Laird (2012) Algorithms for Scaling in a General Episodic Memory (AAMAS extended abstract) - https://ifmas.csc.liv.ac.uk/Proceedings/aamas2012/papers/Z6_3.pdf (ids b05, b06)
- [V] Wallace, Dickinson, Nuxoll (2013) Hashing for Lightweight Episodic Recall (AAAI Spring Symposium) - https://cdn.aaai.org/ocs/5756/5756-24542-1-PB.pdf (ids b07, b08)
- [V] Maharana et al. (2024) Evaluating Very Long-Term Conversational Memory of LLM Agents (LoCoMo) - https://arxiv.org/abs/2402.17753 (ids b16)
- [V] MemGPT (Packer et al. 2023) MemGPT: Towards LLMs as Operating Systems - https://arxiv.org/abs/2310.08560 (ids b17, c16)
- [V] Hu, Wang, McAuley (2026) Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (MemoryAgentBench, ICLR 2026) - https://arxiv.org/abs/2507.05257 (ids b19)
- [V] Fan, Lan (2026) From Cognitive Architectures to Language Agents: A Mechanism-Level Review - https://arxiv.org/abs/2607.23942 (ids b22)
- [M] Gorski, Laird (2011) Learning to use episodic memory (Cognitive Systems Research) - no URL recorded (ids b23)
- [M] Nason, Laird (2005) Soar-RL: Integrating reinforcement learning with Soar - no URL recorded (ids b24)
- [M] Derbinsky, Laird (2009) Efficiently implementing episodic memory (ICCBR) - no URL recorded (ids b25)
- [M] Nason and Laird (2005) Soar-RL: integrating reinforcement learning with Soar - no URL recorded (ids c05)
- [M] Nuxoll and Laird (2012) Enhancing intelligent agents with episodic memory - no URL recorded (ids c06)
- [V] Kirk, Wray, Lindes, Laird (2024) STARS: improving knowledge extraction from LLMs through agent analysis - https://arxiv.org/abs/2306.06770 (ids c08, c09)
- [V] Zhao et al. (2024) ExpeL: LLM agents are experiential learners - https://arxiv.org/abs/2308.10144 (ids c17, d06)
- [V] Xu et al. (2025) A-Mem: agentic memory for LLM agents - https://arxiv.org/abs/2502.12110 (ids c23)
- [M] Laird (2012) The Soar Cognitive Architecture (book) - no URL recorded (ids c26)
- [M] Gap note: Soar episodic memory or Soar-RL versus LLM-agent memory - no URL recorded (ids c27)
- [V] Zhang et al. (2025/2026) ReasoningBank: Scaling Agent Self-Evolving with Reasoning Memory - https://arxiv.org/abs/2509.25140 (ids d01, d02, d03, d04, d05)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory - https://arxiv.org/abs/2504.07952 (ids d07, d08, d09)
- [V] Zhang et al. (2026) Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (ICLR 2026) - https://arxiv.org/abs/2510.04618 (ids d10, d11, d12)
- [V] Krishnamurthy, Harris, Foster, Zhang, Slivkins (2024) Can Large Language Models Explore In-Context? (NeurIPS 2024) - https://arxiv.org/abs/2403.15371 (ids d13)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory - https://arxiv.org/abs/2409.07429 (ids d14)
- [V] Tan et al. (2025) In Prospect and Retrospect: Reflective Memory Management for Long-term Personalized Dialogue Agents - https://arxiv.org/abs/2503.08026 (ids d15)
- [V] Hsieh et al. (2024) RULER: What is the Real Context Size of Your Long-Context Language Models? - https://arxiv.org/abs/2404.06654 (ids d16)
- [V] Zhong et al. (2024) MemoryBank: Enhancing Large Language Models with Long-Term Memory (AAAI 2024) - https://arxiv.org/abs/2305.10250 (ids d18)
- [M] Gorski and Laird (2011) Learning to use episodic memory; Nason and Laird (2005) Soar-RL - no URL recorded (ids d19)
