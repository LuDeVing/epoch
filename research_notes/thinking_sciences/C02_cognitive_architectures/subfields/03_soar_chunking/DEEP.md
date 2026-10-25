# Soar chunking and learning from impasses: deep document

*Subfield C02.03. Evidence ids (a01 to d16) point to the evidence_a-d.jsonl files in this folder. Claim ids (K01 to K30) point to claims.jsonl. The cross-check is in critique.md. Related subfields, not covered here: Soar operator selection and impasse types (C02 sibling), means-ends analysis, adaptive stopping, verification design, LLM metacognitive harness.*

## 1. What it is

Chunking is the learning rule of the Soar architecture. When Soar cannot decide what to do, it hits an impasse. It opens a subgoal and reasons there. When the subgoal returns a result to the parent goal, Soar builds one new production rule (a "chunk"). The rule says: if the same facts are present, return this result. Next time, no subgoal is needed. The subgoal's work is compiled into one step.

The subfield covers five things:

1. Soar chunking itself: how a rule is built, what speed-up and transfer it gives, and what goes wrong (over-general chunks, expensive chunks, chunks that never transfer).
2. The power law of practice that chunking was built to explain, and the challenge to it.
3. Close relatives: explanation-based learning (EBL) and ACT-R production compilation.
4. LLM agent analogues: Voyager skill library, Agent Workflow Memory (AWM), Agent Skill Induction (ASI), SkillWeaver, ExpeL, ReasoningBank, SkillsBench, Dynamic Cheatsheet, LATM tool making, Buffer of Thoughts, Agentic Plan Caching, Memp, AutoManual, Agent KB, ACE, Evo-Memory.
5. What a thinking scaffold should store after a solved sub-problem, when to write it, and how to stop it from hurting.

Why it matters for our agent. Schema state S9 (look back) writes one lesson line. Section 5 of the schema plans a subgoal library, marked [D]. S6 (impasse) opens subgoals. Chunking is the oldest worked example of "write a reusable rule only when a subgoal returns a result." The question for us is not "should we have memory." It is: what to write, when, how to key it, how to check it, and when to delete it.

Short answer from the evidence (details below). Stores of verified, compact, per-sub-problem procedures help, mostly on repeated or related items and mostly for models strong enough to write them. Stores that add everything, store long documents, store unverified self-written text, or reuse entries without checking their conditions do not help and often hurt. Nobody has tested the one Soar idea that is most specific: write only on an impasse resolution, keyed by the facts that were actually used.

## 2. History and theories in depth

### 2.1 The power law and the first chunking theory (1926 to 1982)

Snoddy (1926) found that practice time falls as a power function of trial number: T = B N^-a. Newell and Rosenbloom (1981) argued it holds across a wide range of human tasks and proposed chunking as the cause. I did not open the 1981 chapter; it is known through citations (a09, [M]).

Rosenbloom and Newell (1982, a07, a08, b01, b02) gave the chunking theory of learning. It rests on three assumptions.

- Performance: higher-level chunks process faster than their parts. This needs a serial bottleneck plus a parallel component.
- Learning: chunks are acquired at a constant average rate from the patterns met.
- Task structure: the chance that a pattern recurs falls as pattern size grows.

The power law is derived from these three, not fitted to data. Their model of Seibel's 1023-choice reaction task (10 lights, 10 buttons, 1023 patterns, 76,725 human trials showing a power law) used the Xaps2 production system. A chunk was an encode, map and decode production. A chunk was learned with fixed probability 0.01, because learning at every chance would finish the task in about 3 to 4 passes. The full model ran only about nine trials. The long curve (72,633 simulated trials, a straight line on log-log axes) came from a faster meta-model that only simulates which chunks would be made. So the power-law result for long practice rests on a simplification (b02).

### 2.2 Chunking in Soar (1984 to 1987)

Laird, Rosenbloom and Newell (1984, a01 to a06) turned chunking into a general learning mechanism inside a problem-space architecture. Key design points:

- Chunking is "a recorder of goal-based experience." It runs when a subgoal ends. There is no separate analysis step.
- Conditions are the data that existed before the subgoal and were accessed by a rule that fired. Data that might have been used but were not are absent.
- Conditions are variablized, so two variables cannot match the same object.
- Actions are the subgoal results, pruned to what connects to a supergoal.
- One production per terminated subgoal (the earlier psychology model used three).
- Implicit generalisation: only accessed aspects enter the chunk, so irrelevant context is ignored with no generalising algorithm. In Tic-Tac-Toe the chunks detected board symmetry without being told about it, because orientation was never used (a05).
- Claimed four things from one mechanism: speed-up, learning across all aspects of behaviour, transfer, strategy acquisition.

The 1986 journal paper (a19, b32, c30, [M]) analysed the mechanism in more depth and showed macro-operator learning and search-control learning. Only the abstract was read. The 1987 architecture paper (a20) states the uniform learning hypothesis: goal-based chunking is the general learning mechanism, and chunking learns to avoid the impasses that created the subgoals. The same summary lists "recovery from overgeneralized learning" as not yet possible.

Rosenbloom and Aasman (1990, a17) argued chunking is a variant of explanation-based learning that can also do rote memorisation and induction (a version-space learner was built from chunks). Mitchell, Keller and Kedar-Cabelli (1986, a18, abstract only) is the standard EBL statement: explain why one example fits a concept using a domain theory, then generalise the explanation. EBL needs a correct domain theory. Soar's "domain theory" is its own reasoning trace.

### 2.3 The utility problem and expensive chunks (1990 to 1996)

Tambe, Newell and Rosenbloom (1990, a16, b09; abstract only) showed that a single chunk can be so costly to match that total run time gets worse even though steps fall. They proposed restricting the condition language so match cost is bounded. Minton (1990, b12, not read) and Etzioni (1990, b13, abstract) gave the same problem in EBL under the name "utility problem". Etzioni's STATIC, a static program transformer that learns from no runs, matched PRODIGY/EBL in each of Minton's problem spaces. That is a rival explanation: the gain came from the structure of the space, not from experience.

Kim and Rosenbloom (1996, b10, b11) showed the 1990 restriction does not give the bound in every case (Magic Square: a rule reached over 8 million partial matches and ran out of memory).

Doorenbos, Tambe and Newell (1992, a12 to a15) ran Dispatcher-Soar to 10,112 chunks and found average match cost did not grow, against the utility-problem prediction. This remains an unresolved clash (K05).

### 2.4 ACT-R production compilation (1998 to 2003)

Anderson dropped ACT* knowledge compilation (proceduralization, composition, generalisation, specialisation) in 1998 for weak empirical support and "computational misbehavior": loops, early aborts, too many chances to learn faulty rules (a24, b15). Taatgen and colleagues built production compilation in its place. Two rules that fire in sequence, the first retrieving a fact, are merged into one rule with the retrieved fact built in, removing the retrieval (a23). The new rule starts with utility below its parents and extra noise, so it must win a stochastic competition before it takes over. Learning happens only when the parent rules have enough experience. New rules are not built from newly learned rules. The authors claim this avoids the growing macro-rules of Soar and ACT* (b15, c27). That claim comes from the rival theory's authors and was not tested head to head.

### 2.5 Modern Soar: explanation-based chunking (2012 to now)

Soar 9.6 uses explanation-based chunking: it backtraces through the rule firings with identity analysis, so it generalises much more than the old trace-based chunking. In an arithmetic agent, Soar 9.4 learned 1263 specific rules and 9.6 learned 8 general rules (a21, b06). Procedural learning is off by default. Soar refuses to learn in some cases: a rule with no conditions, a result that depends on random choice, and a chunk that would refire on the elements that built it (chunk inhibition) (b08). Seven stop conditions exist; "allow-local-negations" is the only correctness filter in 9.6.0 (a22).

### 2.6 LLM-era analogues (2023 to 2026)

The LLM literature does not cite chunking as a mechanism much. The nearest items, in order of appearance:

- Voyager (2023): an executable skill library, written after a verified success, retrieved by description (a26, a27, b16 to b18, c01 to c03).
- ExpeL (2023): rules ("insights") extracted from success and failure trajectories (b26, c19, c20).
- LATM (2023): a strong model writes a tool; a weak model uses it (d03, d04).
- Buffer of Thoughts (2024): thought templates, written only when novel (d05).
- AutoManual (2024): a rule manual built online (d11).
- AWM (2024): workflows induced from successful web trajectories (a28 to a30, b19 to b21, c04 to c06).
- ASI and SkillWeaver (2025): executable, verified programs (b22 to b25, c07 to c10).
- Dynamic Cheatsheet, Agentic Plan Caching, Memp, Agent KB, ACE, Evo-Memory, ReasoningBank (2025): write, update and prune policies (d01 to d14, b27 to b29).
- SkillsBench, Skills in the wild, Break It Down (2026): benchmarks of whether skills help (b30, b31, c11 to c16).
- CogRec and NL2GenSym (2025): LLM plus real Soar (c22 to c24).
- Fan and Lan (2026, c21): a review saying no current LLM system compiles the dependency structure of a scoped impasse resolution into a reusable rule. This is a position, not a measurement (K21).

## 3. Core findings with exact numbers

Status key: established (E), single-source (S), contested (C), as in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Chunking speeds up one run and reruns (R1-Soar, minimal search control, 232 rules) | 1731 decisions without learning; 485 with learning in the same run (59 new rules); 7 on identical rerun | Laird 1984 (a04) | E (K01), but both sources are the Soar group |
| Same, with 10 hand-written control rules | 150 decisions; 90 with learning; 7 on rerun. Chunking overhead about 15% run time | a04 | E (K01) |
| Dispatcher-Soar scale run | 10,112 chunks from 200 problems; productions 1,819 to 11,931; one chunk per 6.3 decision cycles; 20.5 firings per cycle (130 per chunk); problem 1: 3,143 cycles, 556 chunks | Doorenbos 1992 (a12) | E (K01) |
| Speed-up on held-out probes | factor 7 first to last; repeated identical problem 4 decision cycles; 10 probe problems (3 easy, 3 medium, 4 hard) | a13 | E (K01) |
| Learning curve form | straight on log-log by eye (Soar); Seibel meta-model 72,633 trials straight on log-log; human data: exponential beats power in 40 datasets, 7,910 series, 475 subjects (abstract only) | a13, a08, a11, d15, d16 | C (K02) |
| Most chunks never transfer | 10.3% of 10,112 chunks transferred; 42 of 200 problems needed no database lookup; transfer 0% to 100% by space; 55 chunks in one space never transferred | a13, a15 | S (K03) |
| A single expensive chunk erases savings | linear rule learning 1.42 s per problem vs 0.46 s without learning (3.1x slower); nonlinear 0.34 s; one rule over 8 million partial matches, out of memory | Kim and Rosenbloom 1996 (b10, b11); Tambe 1990 (abstract) | E (K04) |
| Average match cost did not grow | token changes per decision cycle flat or falling over about 65,000 cycles; wall clock 1.28 s per cycle +0.47 s per 10,000 chunks; Rete network 8x | a14 | C (K05) |
| Over-general chunks exist | Tic-Tac-Toe chunk tests squares A,B,C,E,I,G,F but not D or H; fires where the special case should win; Soar lists six causes | a06, a22, b07 | E (K06) |
| ACT-R compilation fits practice | r2 .97 planes landed, .98 land unit task, .91 and .87 for two other levels; 65 students, 18 ten-minute trials, default parameters | Taatgen and Lee 2003 (a24) | S (K07) |
| AWM on WebArena (GPT-4) | 23.5 to 35.5 (+12.0 points, +51.1% relative); about 2 fewer steps; human-workflow baseline SteP 33.0 | Wang 2024 (a28, c04) | C (K08) |
| AWM shrinks with stronger base | Claude-3.5: 32.7 to 36.3 (+3.6); ReasoningBank report: AWM 40.8 vs no-memory 41.7 for Claude-3.7 | b22, b28 | C (K08) |
| AWM step vs task success on Mind2Web | cross-task step success 36.2 to 45.1; task success 2.0 to 4.8; cross-domain step 18.6 to 32.6 offline, 35.5 online; task 1.0 to 0.7 offline, 1.7 online; action F1 60.6 to 57.3 | a29, b20, c05 | S (K09) |
| Verification before storing | ASI Shopping: unverified text 32.6, verified text 39.0, verified program in memory 36.4, verified program as callable action 40.1; 15.6% of program inductions passed vs 31.4% of AWM adds. Voyager no self-verification: items -73%. Xiong strict-add 38.50 vs fixed 16.75 vs add-all 13.05 (EHRAgent) | b23, c08, b18, b27 | E (K10); ASI table inconsistent (text 4.2 vs table 3.8) |
| Add-all is worse than small fixed memory | RegAgent 55.48 vs 67.53; EHRAgent 13.05 vs 16.75; AgentDriver 32.32 vs 40.11; CIC-IoT 59.90 vs 71.50 | Xiong 2025 (b27, c17) | E (K11) |
| Self-written skills | SkillsBench: no skills 24.3, curated 40.6 (+16.2); self-generated mean 21.0 over 5 configs, delta about -1 to -2; 16 of 84 tasks worse with skills; 7,308 trajectories | b30, c11 | C (K12) |
| Skill grain (Break It Down) | 11-model average: task-level none 22.1, text 20.9, code 18.0; sub-task none 24.8, text 26.7, code 25.3; GPT-OSS-120B AppWorld 27.3 to 1.0 with task-level code skills | c15, c16 | S (K13) |
| Skill size (SkillsBench) | detailed +18.8, compact +17.1, standard +10.1, comprehensive -2.9; 1 skill +17.8, 2-3 skills +18.6, 4+ skills +5.9 | b31, c12, c13 | E (K14) |
| Voyager library | wooden 6 vs 7, stone 11 vs 9, iron 21 vs 29 iterations with vs without library; no diamond tool without library; fresh world with library 4 of 4 tasks 3/3, diamond pickaxe 19 vs 36 iterations; random curriculum -93%; no verification -73%; 3 runs per cell | a26, a27, b16 to b18 | S (K15) |
| Libraries can be handed over | AutoGPT + Voyager library: diamond pickaxe 1/3, golden sword 1/3, compass 2/3, lava bucket 0/3 (vs 0/3 alone). Haiku 4.5 with skills 27.7 beats Opus 4.5 without 22.0. LATM GPT-4 tools let GPT-3.5 reach GPT-4 on 5 of 6 tasks | b17, c02, b30, d03 | E (K16) |
| Failures in memory | ReasoningBank 46.5 to 49.7; Synapse 40.6 to 41.7; AWM 44.4 to 42.2 (Gemini-2.5-flash, WebArena Shopping). ExpeL insights: HotpotQA 28.0 to 39.0; ALFWorld 40.0 to 59.0 | b29, b26, c19 | C (K17) |
| Offline and online induction do not add | Mind2Web cross-task task success offline 4.8, online 4.0, both 1.6; workflow utility rate 0.94 and 0.91; coverage 0.40 of test steps | b21 | S (K18) |
| Abstract workflows vs copied sequences | Mind2Web step 45.1 vs 43.4; task 4.8 vs 2.0; WebArena 35.5 vs 35.6 | a30, c06 | S (K19) |
| Soar + LLM on tie impasse (CogRec) | about 500 bootstrap rules; without chunking performance approaches LLM-Direct; call rate falls to a plateau (figures only). NL2GenSym: critic removal -23% overall, -37% hard cases; hard-case success 76.67% vs one-shot 20% | c22 to c24 | S (K20) |
| Plan cache without Soar | cost -50.31%, latency -27.28%, 96.61% of accuracy; FinanceBench $4.03 at 91.0% to $1.86 at 85.5% | Agentic Plan Caching (d06) | S (K20) |
| Write only on a miss or novelty | APC writes after a miss and verified success; BoT writes if similarity under a threshold; no comparison with write-always | d05, d06, d09 | S (K22) |
| Part of a memory gain is prompt effect | Dynamic Cheatsheet Sonnet AIME 2024: baseline 23.3, empty memory with same instructions 36.7, full memory 50.0. Memp random retrieval 74.59 vs best key 76.02 from 71.93 (about 65% of gain) | d01, d09 | S (K23) |
| Authoring cost | cache generation 1.15% of cost (FinanceBench), 1.33% at zero hits; rule manual about $14 for 36 ALFWorld tasks; ACE cut adaptation cost 75 to 84% vs GEPA and Dynamic Cheatsheet | d06, d07, d11, d13 | S (K24) |
| Wrong application | keyword match loosened exact to 0.8 to 0.6: hit rate 46 to 54 to 64%, accuracy 85.5 to 83.0 to 77.0; LATM dispatcher wrong 4 to 5%; Agent KB raw replay 58.18, adapted 61.21, none 55.15 | d04, d07, d11, d12 | E (K25) |
| Admission rule comparison | Memp: error-driven revision beat append-all and success-only (+0.7 reward, 14 fewer steps); AutoManual stops a class after 3 successes in a row | d10, d11, d13 | S (K26) |
| A store tolerates a minority of bad updates | ACE with a harmful update every iteration 66.7 (base 70.7); every 5th 76.1; every 25th 77.8; none 78.3. APC accuracy drifts 92 to 85.5 from 1 to 100 entries | d13, d07 | S (K27) |
| Two gates: writer strength and recurrence | Dynamic Cheatsheet Game of 24 jump 10 to 99 only for the model that found the code routine (Sonnet stayed 12 to 14); Evo-Memory gain correlated with task similarity r = 0.717 and 0.563 | d01, d02, d14 | S (K28) |
| Maker must be strong | LATM: GPT-3.5 as tool maker made 0 of 5 valid tools on hard tasks | d03, d04, d02, d05 | E (K29) |
| Growth curve shape | Game of 24 was a step; plan-cache new-entry rate fell about linearly (75% of queries added an entry in first block, 20% in last); linear fit beat exponential beat power (derived, 5 points) | d02, d07, d08 | S (K30) |

## 4. Mechanisms and models

This section is written so an engineer could build each one.

### 4.1 Soar chunk construction (the reference mechanism)

Inputs: a trace of rule firings in a substate, the set of working-memory elements (WMEs) that existed in the superstate, and the results returned to the superstate.

Steps:

1. When a rule in the substate creates a result (a WME or preference visible in the superstate), the architecture starts building a chunk at once. It does not wait for the subgoal to end (a21, b06).
2. Backtrace. Walk back from the result through the rule firings that produced it. Each firing that matched superstate WMEs adds those WMEs to the condition list. Firings that touched only substate data are traced further back.
3. Identity analysis (9.6): track which variable instances in different rules are the same object, so the chunk generalises the right things and not more.
4. Variablize. Replace constants by variables, keeping distinct variables on distinct objects. Literal values stay only where a rule tested them literally.
5. Prune actions to those connected to the superstate.
6. Add the production. It now fires in the parent goal and the impasse that caused the subgoal does not recur for this situation.

The key property: conditions are what was accessed, not what was true. This yields implicit generalisation (irrelevant context is dropped) and the over-general risk (facts that were nearly used, such as an almost-satisfied exception, are not recorded) (a06).

When Soar does not learn (b08, a22): result depends on random or probabilistic operator selection; chunk would have no conditions; chunk would refire on the elements that built it; local negation on substate data (allowed by default, filter available); recalled semantic or episodic memory treated as local; tests on the existence of an impasse; operator-selection knowledge not tracked unless "add-osk" is on.

How to port to an LLM scaffold (our reading, not from a paper):

- Trigger: S6 subgoal returns a result that passes a code check.
- Record the facts the subgoal actually used. In a scaffold this means the premises the solving trace cites, extracted by a model call and checked by code against the problem text (G10: reasoning text is not evidence, so the check must be on outputs).
- Entry = (accessed facts as slots, operator used, result form, source item id, reuse counter).
- Key = the accessed facts, not the free-text task description (K21 test).
- Reuse = match facts, run a precondition check, then apply (K06, K25).

### 4.2 The power-law mechanism (chunking theory)

T = B N^-a. Derived from: constant chunk acquisition rate, bigger patterns rarer, bigger chunks faster. Early practice learns common small patterns, which pay quickly. Later practice must learn rarer larger patterns, so the gain per trial falls. The curve flattens because the supply of frequently recurring patterns is used up (a07). The same logic predicts for an agent store: early entries pay most; entries for rare impasse types pay little and cost the same to hold.

Competing form: exponential, RT = a e^(-b(P-1)) + c. Heathcote et al. (a10, a11) say averaging many exponentials gives a power curve (aggregation artifact). Rickard (1997, b05, abstract only) finds power laws inside each strategy, with strategy shifts. Evans et al. (2018, b04, d16, abstract only) say a delayed exponential fits most paradigms. These matter for forecasting returns, not for the mechanism itself.

### 4.3 ACT-R production compilation

Two productions fire in sequence: P1 retrieves a chunk from declarative memory, P2 uses it. Compile to P3 = P1 and P2 merged with the retrieved value built in (retrieval removed). Rules:

- P3 gets utility lower than its parents plus extra noise.
- It competes by utility; every successful use raises its utility toward the parents'.
- Compile only when parents have enough experience (an experience threshold).
- No compiling from compiled rules.

Result: a gradual, stochastic takeover that gives U-shaped learning (past tense) and fits practice curves (a23, a24). It explicitly avoids long macro-rules. The agent-side translation: a procedure enters on probation, is used with a precondition check, and gets promoted or dropped by outcome counts.

### 4.4 Utility of a stored rule

Net value per entry = (cost saved per hit x hit rate) - (cost to match or check per use x use rate) - authoring cost / uses. Soar's expensive chunks are entries whose match cost is high (K04). For an LLM, "match cost" is context tokens for the entry plus tokens for the precondition check plus the risk-weighted cost of a wrong application. SkillsBench shows this: comprehensive documents lose (-2.9) where compact ones win (+17.1) (b31).

### 4.5 Store policies seen in LLM systems

| System | Write trigger | Check before write | Key | Update / prune |
|---|---|---|---|---|
| Voyager | after a successful task | execution plus GPT-4 self-check | description embedding | rewrite on failure, up to 4 rounds |
| AWM | after success (offline or online) | LLM judge of success | workflow text | none; dedupe not measured |
| ASI | after success | re-run program on the task, 15.6% pass | action name | add as callable function |
| SkillWeaver | exploration, then practice | test run of the API | website | rewrite from errors |
| LATM | tool-making phase | 3 unit tests, then validation | task family | dispatcher decides new vs reuse |
| BoT | after solving | novelty: max similarity under threshold | problem class template | meta-buffer |
| APC | after a cache miss and a verified run | success of the run | intent keyword | template with entities stripped |
| Memp | after trajectory | none or success filter | fact-averaged key or query | error-driven revision best |
| ACE | after each task | helpful/harmful counters | none (playbook) | small delta edits; full rewrite collapses |
| Dynamic Cheatsheet | after each query | model's own curation | whole cheatsheet | rewrite |

Sources: b16, b19, b23, c10, d03, d05, d06, d09, d10, d13, d01. These columns come from the evidence lines, not from a single comparison paper. No paper tests the Soar-style write rule (resolved impasse only, facts-accessed key) against write-after-every-success (K22).

## 5. What holds up

### 5.1 Solid

- Compiling a verified sub-result into a reusable unit gives large same-task and some cross-task speed-up. In Soar (a04, a12, a13) and in LLM agents (Voyager, AWM, APC). K01, K15, K20.
- Verification before storing helps, in three independent lines: ASI, Voyager, Xiong (K10).
- Add-all hurts. Four agents in one study, plus the Dynamic Cheatsheet GPT-4o full-history append (6.7 vs 20.0 baseline), plus ACE full-rewrite collapse (66.7 to 57.1, 18,282 tokens to 122), plus Memp over-retrieval (K11).
- Long or many skills hurt: comprehensive -2.9; 4+ skills +5.9 vs +18.6 for 2-3 (K14).
- Wrong application of stored entries occurs (K25, five sources), as does over-generality in Soar (K06, four sources).
- A strong model should write and check entries; a weak model can use them (K16, K29).

### 5.2 Contested

- Does the average chunk cost grow with library size? Doorenbos: no average growth in match work over 10,112 chunks, but wall clock grew 0.47 s per 10,000 chunks. Minton and Tambe predicted slowdown (K05). The one thing both camps accept: restrict rule form.
- Power law versus exponential (K02). Soar curves were never refit. The human data side is abstract-level in our notes.
- AWM gain versus base strength (K08). +12.0 on GPT-4, +3.6 on Claude-3.5, negative on Claude-3.7 in another team's report. Baselines differ by paper: AWM reports GPT-4 vanilla 23.5, ASI reports 12.3 on the same benchmark. Absolute numbers are comparable; relative ones are not.
- Self-written skills (K12). SkillsBench says no gain. ASI, SkillWeaver, ExpeL report gains. The difference is probably execution and verification, but no clean experiment holds everything else equal.
- Failures in memory (K17). Helps ReasoningBank and Synapse; hurts AWM; ExpeL insights from failures helped.

### 5.3 Failures, boundary conditions and noise

- Mind2Web whole-task success is 0.7 to 4.8%. Differences of 1 to 3 points on small N are noise (critique).
- Voyager has 3 runs per cell. Diamond tool 1 of 3. Zero-shot transfer is 4 tasks in one game. The library was not the largest ablation (curriculum -93%, verification -73%), though it is the title story.
- AWM cross-task action F1 fell (60.6 to 57.3) while step success rose. Cross-domain task success did not move (1.0 to 0.7 offline).
- Offline and online induction do not combine (K18).
- ASI verification ablation is one site, one run; paper text says +4.2 and its table gives 3.8 (critique).
- Memp: memory raised commonsense and lowered hard-constraint scores on TravelPlanner. Report by constraint type (d09, d10).
- Dynamic Cheatsheet differences between variants sit inside single-run noise: on 30-question sets one question is 3.3 points.
- Most Soar-era claims come from one group (Laird, Rosenbloom, Newell, Tambe). The outside voices (Taatgen, Minton, Etzioni) are partly unread.
- Doorenbos probes: 10 problems from one generator, one dispatching domain.
- No study equalises tokens. Authoring cost is rarely counted.

### 5.4 Interventions that worked and did not

| Worked | Did not work |
|---|---|
| Execution or outcome check before storing (K10) | Add everything (K11) |
| Compact, single skills (K14) | Long documentation, 4+ skills (K14) |
| Per-sub-task grain (K13, single source) | Whole-task code skills (-4.1 average; GPT-OSS 27.3 to 1.0) |
| Error-driven revision of a failed retrieved entry (Memp, K26) | Full rewrite of the store (ACE collapse, K27) |
| Small delta edits with helpful/harmful counters (ACE) | Loose matching to raise the hit rate (K25) |
| Adapted reuse over raw replay (Agent KB +3.0) | Weak model as the writer (K29) |
| Strong writer, weak user (K16) | Unverified self-written text (K12) |
| Restrict rule form so match cost is bounded (Soar) | Learning on random or probabilistic choices (Soar refuses) |

## 6. Language models

How LLMs behave on these tasks, in short:

1. They gain from a store only when they can write correct entries. Dynamic Cheatsheet: Sonnet and GPT-4o gained; Haiku and GPT-4o-mini gained little or lost. LATM: GPT-3.5 as maker produced 0 of 5 valid tools on hard tasks, mostly tools that worked only on the training cases (K28, K29).
2. They copy stored outputs of similar items (experience-following). That is why add-all hurts and why one wrong entry in a store of similar items can be repeated (Xiong; K11).
3. They gain more when the stream repeats structure. Evo-Memory: gain correlated with task similarity (r = 0.717 and 0.563). Single-turn tasks on Claude 3.7 Sonnet: baseline 0.54, most modules 0.48 to 0.59, i.e. no clear gain (K28).
4. The gain shrinks with a stronger base. GPT-4 AWM +12.0; Claude-3.5 +3.6; Claude-3.7 a possible loss (K08). ACE on GPT-5.1 (base 54.2) still gained about +6 to +11.6, so a strong base does not remove the gain when the store is built as a structured playbook.
5. A routine can produce a step change, not a curve. Game of 24 went from 10 to 99 once the model stored a code routine (K30).
6. Part of the "memory gain" is a prompt effect. Same-instruction empty memory gave about half the gain on Sonnet AIME 2024 (36.7 of 50.0 vs 23.3 baseline). Random retrieval gave about 65% of one gain (K23).
7. Self-written skills without a check do not help on average. SkillsBench self-generated about -1 to -2 points versus curated +16.2. Skills also lift small models over large ones: Haiku 4.5 with skills 27.7 vs Opus 4.5 without 22.0.
8. Skill grain matters. Task-level code skills reduced the 11-model average from 22.1 to 18.0; sub-task text skills raised 24.8 to 26.7. One model fell from 27.3 to 1.0 (K13).
9. LLM calls can be cut by compiling decisions. APC: cost -50.31% at 96.61% of full-model accuracy across five non-recommendation workloads, but FinanceBench lost 5.5 points (91.0 to 85.5). CogRec: call frequency fell to a plateau, figures only (K20).
10. Gains differ by metric. Step success moves; whole-task success often does not (K09). Constraint breakdown matters (Memp).

What changed the result, by size where known: execution check (items +73% by avoiding its removal in Voyager; EHRAgent 38.50 vs 13.05 add-all); curated vs none +16.2; compact vs comprehensive +20.0 spread; strong writer vs weak (0 of 5 vs success); error-driven repair over append (+0.7 reward, 14 fewer steps).

No source measures an LLM agent with an impasse-triggered write keyed by accessed facts.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory section 5.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not store everything. Write an entry only when its content passed a code check (re-run on its source item, or an independent outcome check). | memory, G (extends G3) | [E] | K10, K11; b23, b18, b27, c08 |
| A2 | Keep entries compact: one procedure per entry, short. Cap length. Offer at most 2 or 3 entries per problem. | memory | [E] | K14; b31, c12, c13 |
| A3 | A reused entry must pass a precondition check on the current item before it is applied. Log every reuse and whether it was applicable. | memory, S4 | [E] for the failure mode, [S] for the check | K25, K06; d04, d07, d11, d12, a06, a22 |
| A4 | Use a strong model to write and check entries when a weaker model must use them; count that cost. | memory, G7 | [E] | K29, K16; d03, d04, b17, b30 |
| A5 | Log reuse count, wrong-application count, tokens saved and authoring tokens per entry. Drop entries with net negative value. | memory, logging (section 6 of schema) | [E] on the cost shape | K04; a16, b10, b11 |
| A6 | Any memory arm is compared against a same-instruction empty arm and a random-entry arm, and reports step-level and item-level results. | G7 | [E] by design rule | K23, K09; d01, d09, a29 |
| A7 | Store trusted-by-use: a lesson becomes trusted only after it helps on two different problems (already in schema section 5). The ACT-R experience threshold supports it. | memory | [S] | K07; a23 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Write only when an impasse subgoal was resolved and verified (Soar rule), versus write after every verified success. | memory, S6, S9 | [S] | K22, K21; d05, d06, c21 |
| T2 | Key entries by accessed facts, not by task description. | memory | [S] | K21, K22; d09 (about +2.6 points, small) |
| T3 | Per-subgoal grain versus per-task grain on reasoning items. | S, memory | [S] | K13; c15, c16 |
| T4 | Slots instead of literal values in stored procedures (implicit generalisation). | memory | [S] | K19; a30, c06, a03 |
| T5 | Probation then promote (ACT-R style): new entry shown after the first attempt only, promoted after two helped items, demoted by a harm counter. | memory | [S] | K07, K27; a23, d13 |
| T6 | Error-driven repair of an entry that misfired, versus delete, versus append. | memory | [S] | K26; d10, d13 |
| T7 | Cache a resolved impasse decision (class of operator choice) as a rule to cut calls on repeated impasse types. | O, S6 | [S] | K20; c22, d06 |
| T8 | Store failure lessons ("approach X failed because Y") rather than raw traces. | memory, S5 | [C] | K17; b29, b26, d14 |
| T9 | Admission rule: verified success vs novelty only vs count threshold. | memory | [S] | K26; d05, d10, d11 |
| T10 | Library size knee (10, 100, 1000 entries) and curve shape. | memory | [C] | K05, K30, K02 |
| T11 | Does the store help our base model at all (recurrence of impasse classes first)? | memory | [C] | K08, K28 |

Placement notes. Schema section 5 now says lessons are shown after the first attempt and the subgoal library is [D]. The evidence supports keeping that "after the first attempt" rule for lessons; no source tested the ordering directly, so it stays as the schema has it. The Soar picture also suggests S6 should write the entry (not S9), since the impasse resolution is the compile point; test T1 decides this.

## 8. Concrete tests on our bench

All arms use equal total tokens, with authoring and checking tokens counted. At least 3 runs per cell. Each store arm gets a same-instruction empty arm. Report item-level accuracy, step-level success where defined, tokens per item, hit rate, wrong-application rate. With 30 items one question is 3.3 points, so use at least 100 items per cell for effects of 5 points or less.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 impasse-triggered write | stream of 200 ARC or BRAINTEASER-like items with recurring impasse classes | (a) no store with same instruction text; (b) write after every verified success; (c) write only when an S6 subgoal was solved and verified | accuracy, tokens per item, store size, hit rate | (c) matches (b) at far fewer entries; gain over (a) of 2 to 5 points on items in recurring classes, zero on non-recurring |
| E2 key by accessed facts | same stream, variant items (same structure, new surface) | key by task text; key by accessed facts; key by accessed facts plus precondition check | hit rate, wrong-application rate, accuracy | facts key raises hit on variants; check lowers wrong application; about +2 to 3 points |
| E3 admission check | same stream | append-all; verified-on-source; independent outcome check; count threshold (2 successes) | accuracy, store size, tokens | verified beats append-all (Xiong shows large gaps); threshold unknown |
| E4 grain | trajectories from same solved items | whole-solution procedures; per-subgoal procedures; none | accuracy on fresh items | per-subgoal better, small effect (Break It Down +2 to 3 points on text) |
| E5 literal vs slots | variant item set | literal values; slots | accuracy on variants | slots better on variants; tie on identical items |
| E6 wrong-entry injection | store of similar items | inject 0, 5, 10, 25% wrong entries; with and without utility counter | accuracy; false deletions; copy rate | 0 to 10% tolerated (ACE); 25% hurts; counter removes some wrong ones with some false deletions |
| E7 precondition seeding | seeded procedures that miss one precondition | with / without explicit precondition-check step | wrong-application rate | check lowers rate; magnitude unknown |
| E8 maker strength | store built by strong model; user is weak | strong-built; weak-built; none | accuracy of weak model | strong-built wins; weak-built near zero (LATM) |
| E9 length and count caps | same stream | procedures at 3 length tiers; 1, 3, 6 offered | accuracy at equal tokens | compact wins; 4+ entries lose (SkillsBench) |
| E10 cache impasse decision | stream with repeated impasse types | recompute each time vs cached rule | LLM calls per item; accuracy | calls fall; accuracy within 1 to 2 points; larger loss on hard-constraint items |
| E11 failure lessons | failed items | lesson line; raw trace; none | accuracy | lesson line >= raw trace; sign unknown (contested) |
| E12 size knee and curve | stream growing store to 10, 100, 1000 | tokens in context; success | knee location; fit linear, exponential, delayed exponential per run | knee at small size; shape unknown |
| E13 base strength | strong and weak base | store vs no store | gain | larger gain for the weak base if it can write; maybe none for the strong base |

Run E1, E3, E7 first (see UNKNOWNS.md).

## 9. What does not transfer, and why

- Soar's main speed-up is for exact repeated situations in a rule-based system with exact matching. Our items are text. Matching "the same situation" is fuzzy and error-prone, which is exactly where over-general reuse comes from (K25). Do not copy the "7 decisions on rerun" number.
- Chunks are built by backtracing a formal trace. An LLM trace is not a faithful record of what was used (G10). The accessed-facts condition must be rebuilt by code checks, not read off the reasoning text.
- The power law needs a large number of trials in one stable task. Our benches have tens to hundreds of items across several classes. Do not forecast with a power law (K02, K30).
- Soar's match cost is a Rete-network cost. Ours is context tokens and check calls. The utility problem has the same shape but different units.
- Soar learns in every goal by default in older versions, then moved to off by default. We should not run all-goals learning (K06; Soar 9.6 defaults).
- ACT-R fits are to human practice with all declarative knowledge present at the start; useful as design rules, not as results for LLMs (K07, single source, same group).
- Voyager's library depends on a game with deterministic execution checks and an automatic curriculum (random curriculum -93%). Reasoning items often lack a cheap execution check.
- Web-agent gains (AWM, ASI, SkillWeaver) are in environments with repeated interface structure. Our reasoning items may repeat less. Break It Down is tool and code only; whether per-subgoal grain holds on reasoning tasks is unknown.
- CogRec and NL2GenSym use real Soar with symbolic rules. Our scaffold has no rule engine. The point that carries over is "ask the model only at a tie, cache the answer."
- Human practice curves reflect motor and perceptual automatisation; the part that carries over is only the idea of experience thresholds.

## 10. Open questions

1. Does writing only on a resolved impasse beat writing after every verified success at equal tokens? (No test exists; K22.)
2. What does a stored reasoning procedure cost to author and check, and when does the net become positive (20, 50, 200 entries)? (K24; APC break-even near a 1% hit rate is my derivation.)
3. Which admission rule is best: execution-verified, independently outcome-verified, or count threshold? (K26.)
4. Does an explicit precondition check remove wrong application? No study measures this (K25).
5. What grain is right for reasoning tasks? (K13 is tool and code only.)
6. How does a store go stale, and can wrong entries be detected and removed without false deletions? (K27.)
7. Power, exponential or delayed exponential for our store's growth curve? Soar curves never refit; human full texts unread (K02, K30).
8. Does the gain vanish for a stronger base model, on our model? (K08, K28.)
9. How much of a library's value transfers to other task families without rewriting? The nearest number is Agent KB raw vs adapted, 3.0 points (K16).
10. Does a compiled impasse decision cut calls without lowering accuracy outside recommendation tasks? Partly closed by APC for plan templates (K20).
11. Can a lesson store reduce the very impasses it was built from, as the Soar uniform learning hypothesis predicts (chunking learns to avoid the impasses that created subgoals)? Measure impasse rate per class over the stream.
12. Not read: Heathcote 2000, Evans 2018, Rickard 1997, Tambe 1990, Minton 1990, Etzioni 1990 (full), Laird 1986 (full), Newell and Rosenbloom 1981. A damaged CRAFT download (2309.17428) was not read.

## 11. Sources

[V] opened, [M] snippet or abstract only.

**Soar and chunking**
- [V] Laird, Rosenbloom, Newell (1984) Towards chunking as a general learning mechanism. https://cdn.aaai.org/AAAI/1984/AAAI84-049.pdf (a01 to a06)
- [V] Rosenbloom and Newell (1982) Learning by chunking: summary of a task and a model. https://cdn.aaai.org/AAAI/1982/AAAI82-061.pdf (a07, a08, b01, b02)
- [M] Newell and Rosenbloom (1981) Mechanisms of skill acquisition and the law of practice. Via https://en.wikipedia.org/wiki/Power_law_of_practice (a09)
- [V] Wikipedia, Power law of practice (secondary). https://en.wikipedia.org/wiki/Power_law_of_practice (a10)
- [V] Doorenbos, Tambe, Newell (1992) Learning 10,000 chunks: what's it like out there? https://cdn.aaai.org/AAAI/1992/AAAI92-128.pdf (a12 to a15)
- [M] Tambe, Newell, Rosenbloom (1990) The problem of expensive chunks and its solution by restricting expressiveness. https://link.springer.com/article/10.1007/BF00117107 (a16); abstract page https://mlanthology.org/mlj/1990/tambe1990mlj-problem (b09, abstract only)
- [V] Kim and Rosenbloom (1996) learned-rule match cost, Magic Square. https://cdn.aaai.org/AAAI/1996/AAAI96-114.pdf (b10, b11)
- [V] Rosenbloom and Aasman (1990) Knowledge level and inductive uses of chunking. https://cdn.aaai.org/AAAI/1990/AAAI90-123.pdf (a17)
- [M] Laird, Rosenbloom, Newell (1986) Chunking in Soar: the anatomy of a general learning mechanism. https://mlanthology.org/mlj/1986/laird1986mlj-chunking and https://link.springer.com/article/10.1023/A:1022639103969 (a19, b32, c30; abstract only)
- [V] Laird, Newell, Rosenbloom (1987) Soar summary. https://www.jimdavies.org/summaries/laird1987.html (a20; secondary summary)
- [V] Soar Manual 9.6, Procedural Knowledge Learning. https://soar.eecs.umich.edu/soar_manual/04_ProceduralKnowledgeLearning (a21, a22, b06 to b08, c28; first 100,000 characters)
- [M] Minton (1990) Quantitative results concerning the utility of EBL. https://datalearner.com:8443/academic/journal-papers/0004-3702/volumes-and-issues/115/paper-detail/392 (b12)
- [M] Etzioni (1990) Why PRODIGY/EBL works. https://mlanthology.org/aaai/1990/etzioni1990aaai-prodigy (b13, abstract)
- [M] Mitchell, Keller, Kedar-Cabelli (1986) Explanation-based generalization. https://mlanthology.org/mlj/1986/mitchell1986mlj-explanationbased (a18, abstract)

**Power law of practice**
- [M] Heathcote, Brown, Mewhort (2000) The power law repealed. https://link.springer.com/article/10.3758/BF03212979 (a11, b03, d15)
- [M] Evans, Brown, Mewhort, Heathcote (2018) Refining the law of practice. https://dare.uva.nl/id/717fcfb1-edf1-4010-9959-2b0acccb9c8b (b04, d16)
- [M] Rickard (1997) Bending the power law. https://rickardlab.ucsd.edu/pdf/Rickard1997.pdf (b05)

**ACT-R**
- [V] Taatgen and Anderson (2002) Why do children learn to say 'broke'? https://www.ai.rug.nl/~niels/publications/Past-Tense-published.pdf (a23)
- [V] Taatgen and Lee (2003) Production compilation. https://www.ai.rug.nl/~niels/publications/HF-published.pdf (a24, a25, b14, b15, c26, c27)

**LLM agents**
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 and https://arxiv.org/html/2305.16291v2 (a26, a27, b16 to b18, c01 to c03)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (a28 to a30, b19 to b21, c04 to c06)
- [V] Wang, Gandhi, Neubig, Fried (2025) ASI. https://arxiv.org/abs/2504.06821 (b22 to b24, c07 to c09)
- [V] Zheng et al. (2025) SkillWeaver. https://arxiv.org/abs/2504.07079 (b25, c10; a31 was a [M] search summary)
- [V] Zhao et al. (2023) ExpeL. https://arxiv.org/abs/2308.10144 (b26, c19, c20)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (b27, c17, c18)
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/html/2509.25140v1 (b28, b29)
- [V] Li et al. (2026) SkillsBench. https://arxiv.org/html/2602.12670v1 (b30, b31, c11, c12)
- [V] Skills in the wild (2026). https://arxiv.org/abs/2604.04323 (c13, c14)
- [M] More Skills, Worse Agents? (2026), search result only, via https://arxiv.org/abs/2604.04323 (c29)
- [V] Feng et al. (2026) Break It Down, Pass It On. https://arxiv.org/abs/2608.20274 (c15, c16)
- [V] Fan and Lan (2026) From cognitive architectures to language agents. https://arxiv.org/abs/2607.23942 (c21)
- [V] CogRec (2025). https://arxiv.org/abs/2512.24113 (c22; figures only)
- [V] NL2GenSym (2025). https://arxiv.org/abs/2510.09355 (c23, c24)
- [M] Kirk, Wray, Laird (2023) Exploiting language models as a source of knowledge for cognitive agents. https://arxiv.org/abs/2310.06846 (c25)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d01, d02)
- [V] Cai et al. (2024) LATM. https://arxiv.org/abs/2305.17126 (d03, d04)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (d05)
- [V] Zhang et al. (2026) Agentic Plan Caching. https://arxiv.org/abs/2506.14852 (d06 to d08)
- [V] Fang et al. (2026) Memp. https://arxiv.org/abs/2508.06433 (d09, d10)
- [V] Chen et al. (2024) AutoManual. https://arxiv.org/abs/2405.16247 (d11)
- [V] Tang et al. (2025) Agent KB. https://arxiv.org/abs/2507.06229 (d12)
- [V] Zhang et al. (2026) Agentic Context Engineering. https://arxiv.org/abs/2510.04618 (d13)
- [V] Wei et al. (2026) Evo-Memory. https://arxiv.org/abs/2511.20857 (d14)
