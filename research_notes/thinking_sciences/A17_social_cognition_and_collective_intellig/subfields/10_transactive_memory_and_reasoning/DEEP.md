# Transactive memory and reasoning: deep document

*Subfield A17.10. Source files in this folder: evidence_a-d.jsonl (ids a01-d22), claims.jsonl (K01-K31), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. SCHEMA.md version read: 0.2.*

Short version. The human theory says groups work well when members know who knows what. The machine literature mostly borrows the name. The best machine evidence says three things. (1) Splitting facts across several model calls loses facts. (2) A shared pool of past experience helps, but only if what goes in is checked and what comes out is selected well. (3) A code-held table of who is good at what helps when sources truly differ and the feedback is true. For a single agent with a scaffold, the lessons are about memory design, not about teams.

---

## 1. What it is

**Transactive memory** is the idea that a group can hold more than its members hold alone, because each member stores knowledge in a specific area and also knows who else stores what. Wegner (1987) called it a "group mind" in the modest sense of a shared system. The system has two parts:

- **Individual stores.** Each person holds some knowledge in depth.
- **A directory (metamemory about others).** Each person holds labels and locations: "Anna knows tax rules; Ben knows the server."

Wegner described three processes: **encoding** (who gets which item), **storage** (who holds it), **retrieval** (who is asked, and how answers are combined). Later work (Lewis 2003) measures the system in teams through three dimensions: **specialization** (distinct expertise), **credibility** (members trust each other's expertise), **coordination** (smooth work with no wasted talk).

Why it matters for our agent. Our agent is one model inside a scaffold. It has no teammates. But it has memory stores, tools, sub-calls, past lessons and retrieved experience. Each of these is "someone who knows something." The questions carry over as design questions:

1. When knowledge is spread across several stores or calls, what do we lose when we pool it? (HiddenBench, collaborative inhibition.)
2. Does the agent need a directory of what each store or tool is good at, and should it be learned from outcomes? (MetaCogAgent, Sigma-Mem.)
3. Does a shared pool of past trajectories help, and which parts of the gain are real? (MATM, Xiong 2026.)
4. Does the agent use memory when it is available? (Delivery study, MERIT.)

What this document does not claim. No study we found ablates a Wegner-style who-knows-what directory inside an LLM loop at equal tokens (K20, critique gap 1). The "transactive memory" label in machine papers (MATM, CoThinker, LLMA-Mem) is mostly a name, not a test of the theory.

---

## 2. History and theories in depth

**Founding (1985-1995).**
- Wegner, Giuliano and Hertel (1985) and Wegner (1987, "Transactive memory: a contemporary analysis of the group mind") set out the theory. Not opened this session; cited from secondary sources (a21, b07, a24).
- Wegner, Erber and Raymond (1991, JPSP 61:923). Close couples versus strangers paired up. Secondary description (d05): couples recalled more than stranger pairs only when they used their own division of responsibility. When the experimenter assigned categories, strangers recalled more than couples. Primary text paywalled; no counts or effect sizes read (K30).
- Liang, Moreland and Argote (1995, PSPB 21:384). People trained together on assembling a radio recalled more and built better radios than people trained alone and then grouped. Qualitative result from a secondary source only (d05, d07). Mechanism offered: group training builds the directory, not more knowledge per head.
- Stasser and Titus (1985) hidden profiles: groups discuss shared facts and fail to surface facts held by one member. Lu, Yuan and McLeod (2012) meta-analysis of 25 years of hidden profiles exists (c24); not opened, no numbers used here. This is the human ancestor of HiddenBench.

**Measurement and field work (1998-2019).**
- Hollingshead (1998, 2001): retrieval processes and "cognitive interdependence". Abstract-level only (b05, d08). Key idea: partners form convergent expectations about who knows what.
- Lewis (2003) scale for field teams (b06, a26). Abstract level only. It is the standard survey tool, so most human TMS-performance evidence is self-report and cross-sectional.
- Bachrach et al. (2019) meta-analysis of 76 studies: the TMS-performance link varies with context, including culture (b04, abstract only).

**Collaborative inhibition line (separate tradition, meets TMS).** Groups recall less than the pooled recall of the same people alone. The 2024 meta-analysis (a11-a13, b01-b03) is the main quantitative source here. The TMS reading: familiar pairs with an established division of memory lose less, which is a TMS prediction (K02), though not tested directly.

**"Internet as transactive memory" (2011-2024).** Sparrow, Liu and Wegner (2011, Science) proposed that people treat search engines as a transactive partner and remember where, not what. Camerer et al. (2018) and Hesselmann and Gollo (2020) failed to replicate the priming effect (K18). A cautionary tale for anyone reading TMS claims in the AI context.

**Human-AI (2023-2026).** Position papers (Hu, Stegner and Mutlu 2023, b22, c14) map the three Wegner phases onto robots. Interviews (Meske et al. 2026, a19) find human-AI TMS is lopsided. Surveys (a20, b19, c16-c18) are small, cross-sectional, self-report.

**Machine implementations (2024-2026).** iAgents (c19), INMS (c20), Collaborative Memory (c21), LLMA-Mem (a04-a07), CoThinker (a08-a10, b12-b15), MATM (a01-a03, c01-c05), HiddenBench (c06-c10), Consilience (c11-c12), Sigma-Mem (d09-d10), MetaCogAgent (d11-d12). Section 6 gives numbers.

**Competing explanations for the human group-recall loss.** Retrieval disruption (one person's recall order breaks another's), social loafing, and weak monitoring. The meta-analysis supports monitoring (d=0.14 ns when monitoring is present versus d=0.66 when absent; K04), but that moderator rests on few dissertations. A formal model (De Pasquale and Valcher 2022, a18) says honest appraisal and free communication make a team converge to its best member's level and never above it (K21).

---

## 3. Core findings with exact numbers

Status uses the claim status: established (two or more independent sources), single-source, contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Human collaborative inhibition, overall | d=0.54 (95% CI 0.49-0.58); 140 studies, 185 effect sizes, N=19,492. After trim-and-fill for 36 missing studies: d=0.40 (CI 0.33-0.51). Mostly word-list recall. | a11, b01 (Luo et al. 2024 meta-analysis) | single-source (K01) |
| Inhibition falls with familiarity | strangers d=0.75 (k=46); acquaintances 0.45 (k=21); friends 0.18 ns (k=8); couples -0.19 ns (k=9); QB=17.68 | a12, b02 | single-source (K02) |
| Memory monitoring removes the loss | monitoring present d=0.14, p=.20 (k=12) vs absent d=0.66 (k=173) | a13, b03 | single-source (K04) |
| Couples gain on shared knowledge, lose on a word list | 39 couples, age 68-90. Mutual Friends 30.85 to 47.64 (t(38)=10.02); European Countries 26.56 to 29.79; Word List trial 1 13.81 to 11.92 (p<.001); trial 4 20.51 to 20.43 ns | a14 (2018) | single-source (K03) |
| Couples' benefit is a stable trait | correlation across sessions r=.46-.53; strategy use vs benefit r=.37 (Mutual Friends), .35 (Word List T1) | a15 | single-source |
| Real couples hold shared external memory | 58 couples, 113 memory resources: shared 52.1%, wife 27.4%, husband 20.4%; 38% used indirectly through the spouse | a16 | single-source |
| Team curiosity to TMS to performance | 87 teams, 406 members. Curiosity to TMS b=0.42; TMS to performance b=0.67; r(TMS, performance)=.29; curiosity effect only with high formalization (slope 0.70 vs 0.14 ns). Survey, cross-sectional. | a17, b23 | established that TMS correlates with performance (K19); causal reading not supported |
| "Google effect" priming did not replicate | Original Exp 1: r=0.437, t(45)=3.26. Camerer 2018: pooled N=234, 2.89 ms, t(233)=0.76, p=.449. Hesselmann 2020: N=89, BF01=5.07. Camerer overall 13 of 21 (62%) replicated, effects about 50% of original. | d01-d03, a22 | contested (K18) |
| Internet-use meta-analysis | 22 studies. Memory-task subgroup d=0.56, CI -0.15 to 1.28 (includes zero); cognitive load d=0.73; self-esteem d=0.91. No clean pooled "where not what" d. | d04, b10 | contested (K18) |
| LLM groups fail to pool distributed facts | HiddenBench, 65 tasks, 15 models: 30.1% distributed vs 80.7% single agent with all facts. GPT-4.1 accuracy 0.008 pre-discussion, 0.233 post, 0.733 full profile; humans 0.125, 0.385, 0.604 | c06, c24 (verified in critique) | established (K05) |
| The fault is surfacing, not reasoning | Reveal-all: GPT-4.1 0.037 to 0.926; Gemini-2.5-Flash 0.173 to 0.982 (18 tasks) | c07, c09 | single-source (K06) |
| Two-stage exchange-then-decide protocol | GPT-4.1 0.037 to 0.800; Gemini-2.5-Flash 0.173 to 0.727; variants 0.800/0.727/0.743. Consilience controller 0.83 vs 0.26 round-robin (12 models; 15-model means 0.083/0.285/0.731/0.843) | c09, c11, c12 | established (K07), but same benchmark family; transfer untested (K31) |
| More agents or rounds do not fix pooling | HiddenBench communication gain +0.348 at N=3 to +0.006 at N=7 (GPT-4.1). LLMA-Mem 1 to 7 agents: Claude-Sonnet-4.5 task score 77.08 to 78.22 for 53,549 to 344,323 tokens (6.4x) | c08, a07, a10 | established (K08) |
| Forced dissent is model-dependent | One adversary of four: GPT-4.1 0.233 to 0.492; Gemini-2.5-Flash 0.889 to 0.306 | c10 | single-source (K09) |
| Shared trajectory store (MATM) | ALFWorld (274 tasks) success 47.1% none, 55.1% dense retrieval, 64.3% SVMRank reranker; steps 11.77 / 11.18 / 10.35. WebArena (47 tasks) 18.2% to 20.5%. Mean of 5 runs. | a01, b16, c01, c02 | single-source (K10) |
| Retrieval scope in MATM | ALFWorld full 64.6%, same type 63.1%, cross type 59.9%. WebArena 29.8% / 27.7% / 19.15% | a02, b17, c03 | single-source (K11) |
| Oracle ceiling | Exact-task chunks: ALFWorld 20.07 to 38.69; WebArena 16.58 to 40.38 (one consumer, one seed) | a02, c03 | single-source (K11) |
| Producer strength barely matters | 34 producers; capability gap vs gain r about 0.03-0.09 ns. 3 producers made 98.6% of the index but the other 31 supplied 31.8% of retrieved items; effective producers 2.2 in index vs 10.5 in retrieval | a03, c04 | contested (K12) |
| Add-all storage hurts | Xiong 2026, four agents. Fixed good memory vs add-all: RegAgent 67.53 vs 55.48; EHRAgent 16.75 vs 13.05; AgentDriver 40.11 vs 32.32; CIC-IoT 71.50 vs 59.90. Strict-checked additions: 70.95 / 38.50 / 51.00 / 85.40 | d16, d22 | single-source (K11), supported by K28 |
| Retrieved memory can hurt even when correct | MemTrapBench: all five frameworks below no-memory, losses over 10 points; trap case 31.05% vs 94.39% trap-free vs 92.29% no memory. MERIT: agents ignore a correct retrieved fact 45-53% of the time; hybrid store stale harm +0.25 (Holm p=.030). | d17, d18, d16, d19 | established (K28) |
| Agents do not consult memory voluntarily | 0 memory operations in 114 turns despite seeded store; harness injection delivered every time (n=3); 106 of 108 forced compactions lost conversation-only facts | d20 | single-source (K29) |
| Local vs shared memory | LLMA-Mem Coding, Qwen3-32B task score: local 49.68, shared 46.79, hybrid 46.52. Single run, no variance. | a06 | contested (K13) |
| CoThinker TMS summary, per backbone | Math subset TMS on vs off: Qwen3-30B-A3B 81.87 vs 76.41 (helps); GPT5-Nano 55.97 vs 62.36 (hurts); GPT-OSS-20B 57.15 vs 58.37 (hurts). Perplexity of Qwen3-8B reading others: 6.56 baseline, 1.69 with TMS summary. About 19x IO tokens. | a08, a09, b12-b14 | contested (K14) |
| Missing-facts plan helps | iAgents InfoNav: without it no Schedule level above 10%; with it +15-26% on NP and Schedule. Consilience "route" action was the most valuable single action. | c19, c12, c11 | established (K15) |
| Written belief state helps LLM teams | Bomb defusal, 3 agents: GPT-4 28.3 rounds vs 12.3 with belief state (MAPPO 11.0); first-order ToM accuracy 60.0 to 80.1 | c13 | single-source (K16) |
| Competence table from outcomes | MetaCogAgent (700 tasks, 3 GPT-4 agents): 82.4 vs majority vote 77.1 (2,100 calls) vs single agent 65.3; 1,382 calls; static profile -3.2. Sigma-Mem: 46.22 to 71.10 under a reliability shift; improved in 27 of 30 out-of-domain cases | d09-d12 | single-source (K24), two groups |
| The table misleads when feedback is bad | Sigma-Mem CF@50: Qwen3.5-9B 61.94% to 56.91%; at 5% feedback about majority vote | d09, d10 | single-source (K25) |
| Debate between copies wastes tokens | 7-8B models: 2.1-3.4x tokens of isolated self-correction for equal or lower accuracy; modal adoption up to 85.5%; oracle gap up to 32.3 points. Confidence display +0.025 (SE 0.015) ns; team size +0.066 (p<.001) | d13, d14 | single-source (K26, K27) |
| Provenance cuts repeated work | Five simulated users: resource use down up to 61% at 50% query overlap, 59% at 75%; accuracy above 0.90 | c21, c20 | established (K22), simulated users only |
| Reflection first lowers AI credit | N=42, post F(2,38)=5.48, p=.008, partial eta squared .224. GenAI critical thinking runs through division of labour and reworking output (N=891, indirect .211) | b19, b20, a20, c16, c17, d17 | established (K17), self-report |
| Human-AI TMS is lopsided | 14 interviews: humans learn AI skills, AI keeps only temporary track of human expertise | a19, b21, c15 | established (K20) |
| Output decoupled from public exchange after AI coding tools | About 38,000 developers; slope weakened by 0.138 SD after mid-2022 (44% of pre-AI slope) | b25 | single-source, observational |

---

## 4. Mechanisms and models

Each mechanism is stated so that it can be coded.

### 4.1 The Wegner system as three functions
```
encode(item)    -> choose which store owns it        (specialization)
store(item)     -> write into that store + write directory entry: item_key -> owner, confidence
retrieve(query) -> look up directory -> ask owner(s) -> combine answers
```
Directory entry fields that match Lewis's dimensions: topic or skill tag (specialization); credibility score (trust, from outcomes); coordination cost (latency, tokens). LLMA-Mem's transactive memory stores profiles with specialization areas, task-type proficiency, collaboration history and success rate (a04). Its separate effect was not ablated.

### 4.2 Collaborative inhibition and its fix
Cause (human theory): each member's output disrupts others' retrieval. Fix candidates: monitoring (a ledger of what has been said) and a pre-agreed division. Implementation: do not pool recalls by having sources talk. Run each source independently and take the **union in code**. Keep a ledger: item, which source produced it, was it checked. The LLM analogue of the loss is untested (critique gap 9).

### 4.3 Hidden-profile pooling (HiddenBench) and the exchange protocol
Setup: N agents each hold a subset of facts; the correct answer needs the union. Failure: agents discuss facts all hold and anchor on an early front-runner. Protocol (c09):
1. Exchange: each agent states 1-2 facts it holds and one reason the current front-runner may be wrong.
2. Decide: one call sees everything stated and chooses.

Controller (Consilience, c11-c12): code picks one action per turn from {challenge, seek-evidence, route (give the floor to the agent that has not spoken)}, with conformally calibrated thresholds. Route was the most valuable action. Key engineering point: the controller is code, not a model.

### 4.4 Shared trajectory store (MATM)
```
Producers: finish task -> if success, split trajectory into 5-step action chunks
           key = (task text, recent history window) -> embed (E5-Base) -> index
Consumer:  at step t, planner decides whether to query
           retrieve top-20 by dense similarity -> rerank (learned SVMRank over features) -> inject top-1 chunk
```
Only successful trajectories are indexed. One chunk per call. The reranker gave most of the gain on ALFWorld (55.1 to 64.3) and little on WebArena. Oracle exact-task chunks double success, so near-duplicate coverage is a main driver (K11).

### 4.5 Reliability memory (Sigma-Mem, MetaCogAgent)
```
table[source][skill] = running success rate (+ error-correlation between sources)
on each task: pick source(s) by argmax table[source][skill_of(task)], or weight votes by table
after verifier outcome: update table
```
MetaCogAgent adds a delegation threshold (0.5 best; 0.3 gave 78.1, 0.7 gave 79.6) and verbalised confidence. Ablations: self-assessment -6.8, adaptive delegation -5.1, static profiles -3.2, cross-agent evaluation -3.5. Risk: wrong feedback poisons the table (K25). Freeze updates when verifier confidence is low.

### 4.6 Provenance and access (Collaborative Memory, INMS)
Each stored fragment carries: writer, time, permission, a "confirmed by check" flag. Reads filter by permission. Saves repeated tool calls (up to 61%). INMS also built an echo-chamber test: sharing can spread errors.

### 4.7 Delivery
Make lookup a code step, not an optional tool call (d20). The harness injects the entries keyed to the current state. Reason: agents made 0 voluntary memory calls in 114 turns and ignored correct retrieved facts 45-53% of the time (d18).

### 4.8 Bounds
- Honest-appraisal model (a18): team expertise converges to the best member and does not exceed it. For copies of one model, no "team" gain beyond sampling can be credited without a check.
- Budget theory (d15): at equal total tokens, several agents beat the best single one only if the organisation exponent exceeds the single-agent compute exponent, and shared errors cap it. Simulation only.

---

## 5. What holds up

**Replicated or multi-source.**
- Splitting information across LLM calls loses facts, and adding agents or rounds does not fix it (K05, K08). Two sources.
- Quality-gated memory beats add-all, and memory can hurt even when correct (K28). Four independent 2026 sources.
- Open exchange between copies of one model costs 2-3x tokens for no gain when information is not split (K26, K27). Two sources.
- Missing-facts planning and routing help when information is asymmetric (K15). Two sources, each on its own benchmark.
- Human TMS correlates with performance (K19). Self-report, cross-sectional.

**Did not replicate or is weak.**
- Sparrow 2011 priming failed twice (K18). The where-versus-what recall experiments were not replicated by anyone we found.
- Collaborative inhibition shrinks from 0.54 to 0.40 after trim-and-fill. Moderator results (monitoring; familiarity cells with k=2 to 9) rest on few studies.
- CoThinker counts: the appendix "16 of 25 Holm-significant" is inconsistent (13+3 wins and 3 losses = 19). Direction is stable: wins on high-load items, losses on instruction-following (critique correction 2).
- MATM: authors only, two benchmarks, WebArena 47 tasks (one task about 2 points). One reranker (LambdaMART) fell to baseline on WebArena.

**Moderators found.**
- Familiarity (human): strangers lose most, couples none. Applies only when the pair holds distinct knowledge (K03).
- Monitoring (human, few studies).
- Backbone model (LLM): dissent sign (GPT-4.1 up, Gemini down); CoThinker TMS (one up, two down).
- Single-agent context load: CoThinker's largest gains came when single-agent context was constrained (Gemini-2.5 Math 76.3 vs 59.3).
- Feedback quality: reliability tables help when feedback is true and peers differ; they hurt at CF@50.
- Formalization (human teams): curiosity helps TMS only in high-formalization teams.

**Interventions that worked.** Reveal-all fact listing; two-stage exchange-then-decide; code-controlled route and challenge actions; missing-facts plan; written belief state; strict-checked memory admission; reranking retrieved trajectories; deterministic injection; reliability table from verified outcomes; provenance tags.

**Interventions that did not.** Style prompts (cooperative, CoT) did not close the HiddenBench gap. Showing confidence in debate (+0.025 ns). Fixing debate order (+0.002). More agents beyond about 3. Add-all storage. Producer-strength ranking in MATM (r about 0.03-0.09 ns). Rolling TMS summary on two of three backbones.

---

## 6. Language models

**How models behave on distributed-information tasks.** Multi-agent accuracy on HiddenBench is 30.1% versus 80.7% when one agent sees all facts (15 models, 65 tasks). GPT-4.1 goes 0.008 (before discussion) to 0.233 (after) to 0.733 (full profile); humans 0.125, 0.385, 0.604. Discussion helps little, and the model reasons well once it has the facts. Agents mostly repeat shared facts and anchor on an early front-runner. Reveal-all lifts GPT-4.1 to 0.926 and Gemini-2.5-Flash to 0.982. The cure is in the protocol, not the model's reasoning.

**What changed it, and by how much.**
- Fixed exchange-then-decide: +0.763 (GPT-4.1) and +0.554 (Gemini-2.5-Flash) absolute.
- Consilience controller: 0.83 vs 0.26 round-robin; 11 of 12 models improved; +0.13 over the strongest fixed protocol.
- Team size: communication gain +0.348 at N=3 to +0.006 at N=7.
- Dissent: sign flips by model (+0.259 for GPT-4.1, -0.583 for Gemini).
- InfoNav missing-facts plan: +15-26% on NP and Schedule.

**Memory.**
- MATM: +17.2 points on ALFWorld with reranker, +2 to +2.3 on WebArena. 3 of 34 producers supply 98.6% of the index.
- Xiong 2026 (independent): add-all storage below fixed memory on all four agents (RegAgent 55.48 vs 67.53); strict-checked additions above it (70.95).
- MemTrapBench: every framework below no-memory by over 10 points; a prompt warning recovers up to 14.9 points (from a search summary, not re-derived).
- MERIT: memory lifts dependent-task success from 0.00 to 0.55-1.00, but 45-53% of correct retrieved facts are ignored; embedding retrieval gets updated facts right 0.30-0.95 of the time, update-on-write stores 0.70-1.00.
- Delivery: 0 voluntary memory operations in 114 turns.
- LLMA-Mem: gains +0.27 to +5.92 AAS across cells, many within 1 point; token cost 9.4% to 71.7% below MARBLE and A-Mem baselines; no ablation of the transactive module.

**Competence tables.** MetaCogAgent 82.4 vs 77.1 majority vote vs 65.3 single agent, with 35% fewer calls than voting. Sigma-Mem up to +24.9 points under a reliability shift (46.22 to 71.10). Both on authors' own benchmarks; neither at equal tokens against a flat store.

**Debate.** At 7-8B, 2.1-3.4x tokens for equal or lower accuracy; outcome bounded by the strongest reasoner; majority pressure suppresses correction.

**Human-AI.** Interviews (14) and surveys (N=891, N=152, N=42): critical thinking runs through labour division and reworking output; reflecting before using AI lowers credit given to the AI (F(2,38)=5.48). Self-report throughout.

**Naming warning.** "Transactional memory" (Chang 2025, c22) is a software checkpoint idea, not Wegner's. Do not count it as evidence.

---

## 7. What our agent should take

Part tags: G = guardrail, S = state, O = operator, memory = SCHEMA section 5. Evidence ids in the last column. Our agent is one model, so "agents" here usually means sub-calls, stores or tools. Transfer from multi-agent tests to a single scaffold is by analogy.

### Add now (established [E])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| N1 | **Do not split facts across sub-calls.** If a decision needs facts X and Y, put both in one context. Pooling through chat loses facts (30.1% vs 80.7%). Where a split is forced (long documents), use a coded step: each sub-call lists its unique facts, code takes the union, one call decides. | G4, S3 | [E] | c06, c07, c09, c24; K05, K07 |
| N2 | **Do not add sub-calls for a pooling or memory gain.** Gain falls from +0.348 to +0.006 between 3 and 7 agents; 6.4x tokens for +1.1 points. Consistent with G9 and G11. | G9 | [E] | c08, a07; K08 |
| N3 | **Gate admission to any stored experience or lesson on a verified success.** Add-all storage fell below a fixed memory on all four agents. Matches the rule that a lesson is trusted only after it helps on two problems. | memory | [E] | d16, d17, d18, d19; K28 |
| N4 | **Record provenance with every stored item:** source, time, "confirmed by check" flag. | memory | [E] for provenance; ordering retrieval by the flag is [S], see test T4 and U4 | c21, c20; K22 |
| N5 | **Keep any directory in code, not in the model.** Models keep no durable metamemory of other parties. A "which store or tool is good at what" table is scaffold state. | memory, S0 | [E] | a19, b21, c15, a04; K20 |
| N6 | **For tasks with several sources, keep a missing-facts ledger** (what is still unknown, which source could hold it), maintained by code. | S4, O3 | [E] as an analogue; each paper on its own benchmark | c19, c12, c11; K15 |
| N7 | **Form an own answer before reading retrieved memory** (already the rule that lessons come after the first attempt), and check retrieved content before trusting it. | G2, memory | [E] on direction; small human samples | b19, b20, d17, a20; K17 |
| N8 | **Always run a matched-token single-agent baseline** (self-consistency or best-of-N) when testing any exchange or summary compression. | G7 | [E] | d13, d14, d15, a08; K26 |

Confirmed rejects: no open debate between copies (G9; K26, K27); no stated confidence as a credibility signal (d14, also 4b); no dissent voters by default (K09).

### Test first (single-source [S] or contested [C])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Deterministic injection of memory entries by code**, not an optional lookup. | memory, S0 | [S] | d20; K29 |
| T2 | **Competence table per tool, operator or store**, updated from verifier outcomes; read by S0 and by S6 operator choice. | memory, S0, S6 | [S] | d09-d12; K24, K25 |
| T3 | **Experience store of our own solved items** with leakage-controlled retrieval and a reranker. | memory | [S] | a01, b16, c01, c02; K10, K11 |
| T4 | **Source-quality weighting in retrieval** (similarity alone vs similarity times source tag). | memory | [C] | a03, c04, d09, d14; K12 |
| T5 | **Union in code versus chat pooling** for multi-call recall (is the human inhibition loss real for LLMs?). | G4 | [S], human-only | a11, b01, a13; K01, K04 |
| T6 | **Rolling structured summary of consensus and open issues** across sub-calls. | memory | [C] | a08, b12-b14; K14 |
| T7 | **Written model of what each source or sub-call knows** (belief state). | memory | [S], older model (GPT-4) | c13; K16 |
| T8 | **One counter-reason step** with a per-backbone sign check. | O6 | [S] | c10; K09 |
| T9 | **Per-operator (local) memory versus one flat store.** | memory | [C] | a06, a01; K13 |
| T10 | **Pointer-only versus content storage** (the "where not what" idea). | memory | [C] | d01-d04; K18 |
| T11 | **Re-show a coded state summary at every step.** | S0 | [S] | c23; K23 |

---

## 8. Concrete tests on our bench

All tests use equal tokens per arm. Setup tokens count (G7). Report ignore rate and leakage controls wherever memory is involved. Expected effects are guesses from the literature.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Hidden-profile items built from our own facts (4 fact slices, one right answer needing the union), built differently from HiddenBench (K31) | (a) one call with all facts; (b) 4 sub-calls with chat pooling; (c) 4 sub-calls, coded union, then one decide; (d) exchange-then-decide | accuracy; unique facts retained | (a) at or above (c) > (d) > (b). If (a) is not best, the one-agent design needs a second look |
| B2 | Sub-call count sweep 1/3/5/7 on a pooling task | same total tokens | accuracy | flat or falling after 3 |
| B3 | ARC and brainteaser items with a seeded store of earlier solved items | (a) no memory; (b) add-all lessons; (c) add only verified lessons; (d) (c) plus reranker | accuracy, steps, tokens; ignore rate | (c) > (a) > (b), as in Xiong and MemTrapBench. Size unknown |
| B4 | Same as B3 with near-duplicates removed from the store | with vs without near-duplicates | drop in accuracy | most of the gain vanishes if the MATM pattern holds (oracle 20 to 39 points) |
| B5 | Items where the right lesson is in the store | (a) optional lookup tool; (b) code-injected entries | rate of use; accuracy | (b) uses 100%, (a) near 0 for small models (d20 was one task; size unknown) |
| B6 | Mixed-class items where several operators or stores exist | (a) flat selection; (b) competence table updated from verifier outcomes; (c) static table; (d) table fed 50% corrupted feedback | accuracy; operator-choice accuracy | (b) > (a) by a few points; (d) < (a) if K25 holds |
| B7 | Items with a planted wrong lesson, with and without provenance flag | flagged vs unflagged retrieval | rate of copying the wrong lesson | lower with the flag; size unknown |
| B8 | Multi-call recall (long document split into parts, questions needing all parts) | chat pooling vs code union vs code union plus ledger | share of unique facts kept | union and ledger beat chat; replicates or refutes the human inhibition effect |
| B9 | Answer-first versus memory-first, with a misleading retrieved item | order of reading | anchoring errors | answer-first has fewer errors (human N=42 only, so test) |
| B10 | Same items, per backbone | with and without rolling summary; with and without one counter-reason | accuracy per backbone | sign differs by backbone (K09, K14); enable per model only if positive |

---

## 9. What does not transfer, and why

- **The human directory.** Humans build it through shared time (familiarity removes the loss). A single model has no shared time with its own sub-calls. Copies of one model are maximally "familiar", yet HiddenBench shows they still fail to pool. Familiarity alone does not make a directory.
- **Credibility by expertise.** Sub-calls come from one model, so they hold the same knowledge. The formal bound (a18) says a team cannot exceed its best member. Credibility weighting helps only when sources really differ (Sigma-Mem peers were three different small models).
- **Human recall numbers.** Collaborative inhibition is measured on word lists with people. The mechanisms (retrieval disruption, loafing) are not clearly present in LLM calls. The only analogue is context contamination, untested.
- **Google-effect results.** Failed replications. Do not build memory design on "remember where, not what."
- **Human-AI survey findings** (N=891, N=152, N=42). Students and professionals, self-report. They describe how people use AI, not how an agent should be built.
- **Multi-agent gains on shared benchmarks** (HiddenBench, Consilience). Both designed on one family. Not tested on our item types.
- **CoThinker.** About 19x IO tokens, no matched-compute baseline. Gains may be a token effect.
- **LLMA-Mem and MetaCogAgent numbers.** Authors' own benchmarks, single runs, no variance.
- **Open exchange.** With the same information in every copy, exchange cost 2.1-3.4x tokens for no gain (G9 stands).
- **Name collisions.** "Transactional memory" (Chang 2025) is not Wegner's idea.

---

## 10. Open questions

1. Does a code-held directory of competence beat a flat store at equal tokens in an LLM loop? No ablation exists (critique gap 1).
2. What are the exact numbers in Wegner, Erber and Raymond (1991), Liang, Moreland and Argote (1995), and Hollingshead (1998)? Paywalled; not read.
3. Does exchange-then-decide transfer to hidden-profile tasks built another way, and does it beat one call with all facts at equal tokens?
4. How much of the MATM gain survives near-duplicate removal, outside ALFWorld and WebArena, by an independent group?
5. Is CoThinker's gain compression or tokens? Needs best-of-N at the same tokens.
6. Does credibility weighting help against deliberately wrong sources with provenance tags?
7. Can the sign of forced dissent be predicted from a model's baseline pooling accuracy?
8. Is collaborative inhibition reproduced in LLM sampling, and does a monitoring ledger remove it?
9. Does answer-first ordering cut anchoring on retrieved memory in LLMs?
10. Does the Sparrow where-versus-what effect (Experiments 3-4) hold at all? Nobody has replicated those.

---

## 11. Sources

[V] = opened and read this session (full text or a substantial page); [M] = snippet or abstract only, or cited from a secondary source.

**Human studies and reviews**
- [M] Wegner (1987) Transactive memory: a contemporary analysis of the group mind. https://doi.org/10.1007/978-1-4612-4634-3_9 (a24, c26)
- [M] Wegner, Erber, Raymond (1991) Transactive memory in close relationships. https://doi.org/10.1037/0022-3514.61.6.923 (a25, d06)
- [M] Lewis (2003) Measuring transactive memory systems in the field. https://pubmed.ncbi.nlm.nih.gov/12940401/ ; https://doi.org/10.1037/0021-9010.88.4.587 (a26, b06)
- [M] Liang, Moreland, Argote (1995) Group versus individual training. https://doi.org/10.1177/0146167295214009 (a27, d07)
- [M] Hollingshead (1998, 2001). https://pubmed.ncbi.nlm.nih.gov/11761309/ ; https://doi.org/10.1006/jesp.1998.1358 (b05, d08)
- [M] Bachrach et al. (2019) TMS in context, meta-analysis. https://pubmed.ncbi.nlm.nih.gov/30024196/ (b04)
- [M] Stasser and Titus (1985). https://doi.org/10.1037/0022-3514.48.6.1467 (c25)
- [M] Lu, Yuan, McLeod (2012) Twenty-five years of hidden profiles. https://doi.org/10.1177/1088868311417243 (c24)
- [V] Luo et al. (2024) Collaborative inhibition meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC11428894/ (a11-a13, b01-b03)
- [V] Older long-married couples (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC6288253/ (a14, a15)
- [V] Ageing Together (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9010510/ (a16)
- [V] Team curiosity, TMS, formalization (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13154042/ (a17, b23)
- [V] Harris, Barnier, Sutton, Keil (2010) Couples as socially distributed cognitive systems (secondary description). https://www.ida.liu.se/~729G12/mtrl/Harris%20et%20al.%202010.pdf (d05)
- [V] Wikipedia: Transactive memory; Google effect (secondary). https://en.wikipedia.org/wiki/Transactive_memory ; https://en.wikipedia.org/wiki/Google_effect (a21, a22, b07)
- [M] Sparrow, Liu, Wegner (2011). https://doi.org/10.1126/science.1207745 ; https://pubmed.ncbi.nlm.nih.gov/21764755/ (a23, b08)
- [V] Camerer et al. (2018) replication report. https://osf.io/download/84fyw/ ; Nature Human Behaviour page (abstract level) https://www.nature.com/articles/s41562-018-0399-z (d01, d02); abstract https://pubmed.ncbi.nlm.nih.gov/31346273/ (b09, [M])
- [V] Hesselmann and Gollo (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/ (d03)
- [V] Gong and Yang (2024) meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10830778/ ; https://doi.org/10.3389/fpubh.2024.1332030 (b10, d04)
- [V] Akgun and Toker (2025) cognitive self-esteem. https://arxiv.org/abs/2501.10517 (b11)
- [V] Coding alone? AI-assisted software work (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13207591/ (b25)
- [M] Human-AI teaming, TMS and speaking up (2023). https://pubmed.ncbi.nlm.nih.gov/37599773/ (b24)

**Models and theory**
- [V] De Pasquale and Valcher (2022). https://arxiv.org/abs/2204.08519 (a18)
- [V] Hu, Stegner, Mutlu (2023) Knowing who knows what. https://arxiv.org/abs/2305.05115 (b22, c14)
- [V] Phase transition for budgeted multi-agent synergy (2026). https://arxiv.org/abs/2601.17311 (d15)
- [V] Chang (2025) MACI. https://arxiv.org/abs/2512.05765 (c22)
- [V] Chen et al. (2026) Human-human collaboration platform. https://arxiv.org/abs/2509.18008 (c23)

**Human-AI surveys**
- [V] Meske, Hermanns, Brachten (2026) The GenAI who knew too little. https://arxiv.org/abs/2610.28343 (a19, b21, c15)
- [V] Akgun and Toker (2026) When does GenAI use support critical thinking. https://arxiv.org/abs/2610.38910 (a20, b20, c17)
- [V] Islam, Akgun, Billah (2026) Credibility judgments. https://arxiv.org/abs/2603.26522 (b19, c16)
- [V] Annunziata et al. (2026) When AI joins the team. https://arxiv.org/abs/2608.03462 (c18)

**LLM studies**
- [V] Kim et al. (2026) Multi-Agent Transactive Memory (MATM). https://arxiv.org/abs/2606.19911 (a01-a03, b16-b18, c01-c05)
- [V] Wu et al. (2026) LLMA-Mem. https://arxiv.org/abs/2604.03295 (a04-a07)
- [V] Shang et al. (2026) CoThinker. https://arxiv.org/abs/2506.06843 (a08-a10, b12-b15)
- [V] Li, Naito, Shirado (2026) HiddenBench. https://arxiv.org/abs/2505.11556 ; https://proceedings.mlr.press/v306/li26ej.html (c06-c10, d21)
- [V] Babu et al. (2026) Consilience. https://arxiv.org/abs/2608.20564 (c11, c12)
- [V] Li et al. (2023) Theory of mind for multi-agent collaboration. https://arxiv.org/abs/2310.10701 (c13)
- [V] Liu et al. (2024) iAgents. https://arxiv.org/abs/2406.14928 (c19)
- [V] INMS: memory sharing (2024). https://arxiv.org/abs/2404.09982 (c20)
- [V] Collaborative Memory (2025). https://arxiv.org/abs/2505.18279 (c21)
- [V] Feng, Yang, Poria (2026) Sigma-Mem. https://arxiv.org/abs/2607.27958 (d09, d10)
- [V] MetaCogAgent (2026). https://arxiv.org/abs/2605.17292 (d11, d12)
- [V] Bertalanic and Fortuna (2026) The cost of consensus. https://arxiv.org/abs/2605.00914 (d13)
- [V] Can LLM agents really debate? (2025). https://arxiv.org/abs/2511.07784 (d14)
- [V] Xiong et al. (2026) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (d16)
- [V] MemTrapBench (2026). https://arxiv.org/abs/2608.20202 (d17)
- [V] MERIT (2026). https://arxiv.org/abs/2609.05441 (d18)
- [V] Memory manipulation in LLM agents for MCQA (2026). https://arxiv.org/abs/2606.29030 (d19; baseline numbers only)
- [V] Delivery, not storage (2026). https://arxiv.org/abs/2607.20972 (d20)
- [V] Annapureddy and Thamatani (2026) Epistemics of agent memory. https://arxiv.org/abs/2609.33013 (d22; abstract only)

Links to other subfields run in parallel (not covered here): Conformity; Social epistemology; Epistemic diversity; Aggregation and extremizing; ACT-R declarative memory; Working memory; Retrieval-induced forgetting and memory errors; Knowledge networks; Cognitive artifacts.
