# Soar: operator selection, impasses and impasse types: deep document

*Subfield C02.01. Built from evidence_a-d.jsonl (ids a01-a35, b01-b27, c01-c31, d01-d17), claims.jsonl (K01-K31) and critique.md in this folder. Written for the single-agent thinking schema (`research_notes/single_agent/SCHEMA.md`: guardrails G1-G12, states S0-S9, operators O1-O8). Status marks follow the schema: [E] established (two or more independent sources), [S] single source, [C] contested.*

*Honest scope note. The Soar mechanics come from one research group (Laird 2022, Soar Manual 9.6, Laird 2021). That is good enough to describe a design. It is not evidence that the design improves performance. The LLM-hybrid results (CogRec, NL2GenSym, STARS) are single-lab, single-run, toy or simulated, and none has an equal-token control. Laird 2012 (book) and Laird, Newell, Rosenbloom 1987 (founding paper) could not be opened in this run.*

---

## 1. What it is

Soar is a cognitive architecture. Its control is built around one loop, the decision cycle, and one trigger for extra thinking, the impasse.

**The decision cycle (Laird 2022, a01, a13).** Five phases:

1. Input: new perception arrives.
2. Elaboration: rules fire in parallel until nothing more fires (quiescence). Some rules propose operators ("this operator is available"). Others add evaluations ("this one is better than that one").
3. Operator selection: a fixed decision procedure reads all the preferences and picks one operator, or fails to.
4. Application: rules that match the selected operator change the state.
5. Output: motor commands go out.

Control is operator-centric. Knowledge is in rules. A fixed procedure, not a learned judge, picks the operator (a01). About 50 ms per cycle is the real-time target for the architecture (c13).

**Preferences (a02, a10).** Preferences are the data that decide selection.

- Acceptable: the operator is available.
- Reject, prohibit: the operator must not be chosen.
- Require: the operator must be chosen.
- Better, worse (relative), best, worst (absolute).
- Indifferent (unary or binary): the operator is as good as another.
- Numeric: an expected reward value, used last (a08).

Proposal effects are retracted when their match disappears (i-support). Application effects persist (o-support) (a16).

**The eight-step filter (Soar Manual 9.6, a10, a11).** Selection runs through fixed steps: RequireTest, AcceptableCollect, ProhibitFilter, RejectFilter, BetterWorseFilter, BestFilter, WorstFilter, IndifferentFilter. Five steps can end in a winner or an impasse. This is plain, ordered, code-checkable arbitration.

**The impasse (a03, a09, b04).** If the preferences do not single out one operator, no operator is selected and an impasse arises. A fixed architectural rule applied to the preference outcome raises it. The system does not judge its own progress. This is the key point for us.

**Impasse types.** The count depends on the source (section 2.4). The Manual 9.6 detailed section lists:

| Type | Raised when | Resolved by (Manual 9.6, a12) |
|---|---|---|
| Tie | two or more acceptable operators, preferences do not separate them | add preferences that prefer one, reject others, or make all indifferent |
| Conflict | at least two operators have contradictory better/worse preferences and none is rejected, prohibited or required | require one, or reject/prohibit the others |
| Constraint-failure | more than one required value, or a value both required and prohibited | not resolvable by more preferences; change the rules so fewer require/prohibit preferences arise, or let the substate retract all but one |
| State no-change | no operator proposed | create acceptable or require preferences for some operator |
| Operator no-change | the selected operator stays selected across decisions (cannot apply, or the action just takes time in the world) | apply it, change the state so its proposal no longer matches, or prefer another operator |

**Substates (a04, a14, b05).** An impasse creates a substate linked to the superstate. The substate has its own preference memory and runs the same decision cycle, so it can itself have impasses (a stack). It reads the superstate. It returns only results. When the superstate can decide, the impasse is resolved, and the substate and all non-result structure are deleted. The substate does not touch the outside world directly. Perception and motor go through the topstate.

**Why this matters for us.** Laird argues that this one mechanism gives meta-reasoning, planning and look-ahead without separate modules (a05, c15). Deliberate reasoning is bought only when quick knowledge fails. That is our G1 ("doubt only on a signal") with a hardware-like definition of the signal. Our S6 IMPASSE state and the SUBGOAL arrow back to S1 are the same idea in a text scaffold.

---

## 2. History and theories in depth

### 2.1 Origins: universal subgoaling

Soar (Laird, Newell, Rosenbloom 1987) was built on two ideas. Problem spaces: all behaviour is search through states with operators. Universal subgoaling: any decision can be the object of goal-directed attention, and goals arise only automatically from impasses. A 1988 NASA secondary report (a31) states the early design plainly: when a stage lacks information a subgoal is created to collect it, and it pops when the information is available. Listed traits: problem spaces, universal subgoaling, and "no conflict resolution mechanism in SOAR". The system refuses to settle ambiguity with a fixed tiebreaker and spends effort only when ambiguity arises.

Not read: the 1987 AI Journal paper (a32, opened:false) and the 1986 chunking paper (a34). Claims about the weak methods that "emerge" from impasse types (search method follows from the knowledge available) come from Laird 2022 (a06) and are not checked against the 1987 text.

### 2.2 Chunking and learning from impasses

Chunking turns the result of substate reasoning into a rule, so the same impasse does not recur. What is learned depends on the impasse type (a07, c15):

| Impasse | Chunk learned |
|---|---|
| state no-change | operator proposal rule |
| tie or conflict | operator evaluation rule (search control; numeric ones become RL rules) |
| operator no-change | operator application rule |
| any | elaboration rules |

Boundary conditions found:

- Chunking needs deterministic substate decisions. If the substate used random, numeric or RL selection, no rule is added (a07, a15).
- The Soar 9.6 chunking rewrite (explanation-based behavior summarization) cut an arithmetic agent from 1263 learned rules (9.4) to 8 (9.6) because old chunks were over-specific (a15). One agent, no benchmark.
- Rules learned from tie impasses can be wrong unless the knowledge behind the operator preferences is included. That option is off by default (a15).
- Expensive chunks: chunking can cut steps and still make total run time worse, because some learned rules are costly to match (Tambe, Newell, Rosenbloom 1990, abstract only, b26).

Deep treatment of chunking belongs to the parallel subfield "Soar chunking and learning from impasses". This file only notes the links.

### 2.3 Soar-RL and the order of authority

Reinforcement learning in Soar (Nason and Laird 2005, a35, not opened) tunes numeric preferences. They act only when other preferences leave the choice open (a08). Order of authority: hard rules and symbolic preferences first, learned value last.

### 2.4 How many impasse types? A naming problem, not a fact

| Source | Count | Note |
|---|---|---|
| Laird 2022 main text (b01) | 3 | state no-change, operator tie/conflict, operator no-change |
| Laird 2022 glossary (b01, c14) | 4 | state no-change, operator no-change, tie, conflict |
| Manual 9.6 contents (b02) | 4 | tie, conflict, constraint-failure, no-change |
| Manual 9.6 overview paragraph (b02) | 3 | contradicts its own contents |
| Manual 9.6 detail (a09) | 5 if no-change is split | constraint-failure present |
| NL2GenSym critic output (b03, a23) | 5 | all five named |

Constraint-failure has zero mentions in Laird 2022. No source is wrong. The count depends on grouping. For us the lesson is simple (K02, established): type impasses by what our own checks can detect, not by Soar's count.

### 2.5 Laird 2021 and the comparison with ACT-R

Laird (2021, a17) points out that in Soar failures to propose, select or apply all become impasses, and the substate records the impasse type. That gives "module status data" that supports metacognition. ACT-R has no automatic substate. A port would need an extra buffer holding impasse information. The Standard Model of the Mind (b27, not opened) came from mapping ACT-R, Sigma and Soar. Whether impasse-driven subgoaling is in the shared core was not confirmed. It may be Soar-specific, not a field consensus.

### 2.6 Bridges to language models

In order of time:

- Wray, Kirk, Laird 2021 (a30): a cognitive agent can use an LLM as a knowledge source. Accuracy and relevance are the main challenges. The agent must check what it gets.
- Romero et al. 2023 (c31): exploratory CMU proposal; no impasse tests.
- Joshi and Ustun 2023 (b23): a proposal. An impasse opens a substate whose goal is to query the LLM. Chunking turns the answer into a rule that prevents the impasse. The architecture, not the LLM, should choose the final action. Zero experiments.
- Kirk, Wray, Laird 2023 (a26) and STARS, Kirk et al. 2024 (a27, b12-b14, c21-c23): a Soar agent checks and repairs LLM answers with its own knowledge.
- CoALA, Sumers et al. 2024 (a18, a19, b21, b22, c16, c17): the main LLM-agent blueprint. It describes Soar's impasse in two sentences, then drops it. Its cycle is propose, evaluate, select, execute. Selection can reject all and loop back. No typed impasse. No substate with a typed result.
- Zhu and Simmons 2024 (c24): a task stack inspired by Soar impasses, asking an LLM for an action plus a production rule.
- NL2GenSym 2025 (a20-a23, b03, b09-b11, c01-c05): an LLM writes Soar rules, a critic reads real Soar traces.
- CogRec 2025 (a24, a25, b15, b16, c06-c09): a Soar impasse calls an LLM; chunking stores the answer.
- Fan and Lan 2026 (a29, c10-c12): a mechanism-level review of 42 agent systems. The Soar bundle (typed impasse + isolated substate + typed result return + condition-safe compilation) is not delivered by any reviewed system.

### 2.7 Human side

Brown and VanLehn 1980 repair theory (b25, opened:false): a student with an incomplete procedure hits an impasse and applies a repair. Different repairs at the same impasse give different bugs. Checked against a large database of subtraction bugs, but only seen in snippets. NL-Soar (Lehman, Lewis, Newell 1991, b24): impasses on a comprehend operator open subgoals, chunking turns the search into recognition, a snip operator repairs wrong earlier choices. A model with no effect size. The human side is thin here. Ohlsson's impasse work is covered in the parallel representational-change subfield.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| An impasse is raised by a fixed rule on the preference outcome, not by self-judgement | Eight-step filter; five exits to winner or impasse; one impasse type per level at a time | a09, a10, a11, b04 (Manual 9.6, Laird 2022) | [E] for the design (same group), K01 |
| Impasse type count varies | 3 (Laird main), 4 (glossary, Manual contents), 5 (split no-change, NL2GenSym) | b01, b02, a09, b03 | [E] K02 |
| Constraint-failure is not resolvable by more preferences; Laird 2022 fn 4 says any selection impasse can be | Manual: "cannot be resolved by additional preferences" | b07, a12 | [C] K03 |
| Constraint-failure outranks tie and conflict in detection | if both occur only constraint-failure is detected | a09 | [S] K04 |
| Substates are isolated and return results only | Non-result data deleted; results justified by the superstate elements they used | a04, a13, a14, b05 | [E] mechanics (same group), K05 |
| Chunk type follows impasse type | 3 mappings (proposal, evaluation, application) | a07, c15 | [S] K06 |
| Operator no-change is ambiguous (stuck vs slow) | no rate given | a03, b04 | [S] K07 |
| Time-bounded substate fallback is stated, not specified | no numbers | a06, b06 | [S] K08 |
| Impasse-triggered LLM calls compiled to rules cut later LLM use | CogRec: call frequency falls to a low plateau only with chunking (figure only). Zhu and Simmons: find 15/15, 12/15 with no LLM call, query tokens 917 vs 54,754 (table scrambled); slice and clear 0 tokens vs 102,807 and 18,925 | c08, c24, a28 | [E] by 3 sources, all toy or figure only, K09 |
| Accuracy gain from impasse-triggered LLM queries is small | CogRec ML-1M HR@10: 0.3124 vs LLM-Direct 0.2901 (+7.7% rel.), GPT4Rec 0.2956 (+5.7%), SASRec 0.2815, pure Soar (about 20 hand rules) 0.0511. Gains over best baseline 4.1 to 9.1% across 12 columns. Yelp HR@10 0.2247 vs 0.2053. No seeds or significance | a25, b15, c07 | [S] K10 |
| Raw LLM answers are mostly unusable for a grounded agent | Unviable: over 70% kitchen, 58% groceries, 85% office. Situationally relevant: 13%, 14%, 5% | a26, a27, b14, c22 | [S] K11 |
| Agent-side analyse-repair-select lifts completion | Kitchen 52.5 to 77.5, groceries 66.7 to 94.4, office 35.7 to 92.9 (%). Tokens 41,407 to 139,871; 17,078 to 61,808; 12,992 to 76,056 (3.4x, 3.6x, 5.9x). 10 runs for STARS only: means 77.5, 93.89, 92.14, SD 2.04, 1.76, 2.26 | a27, b12, b14, c21 | [S] K12 |
| STARS ablation by stage | ST 50.0/66.7/21.4; STS 40.0/66.7/21.4; STAR 77.5/77.8/64.3; STARS 77.5/94.4/92.9 (kitchen/groceries/office). A wider tree alone gives no gain. Selection adds 0 in kitchen (+13,785 tokens), +16.6 groceries, +28.6 office | b13, critique | [S] |
| Context facts fix a selector failure | Three added facts: kitchen 77.5 to 92.5 | c23 | [S] |
| Reasoning without outside feedback does not self-correct | GPT-3.5 GSM8K 75.9 to 74.7; CommonSenseQA 75.8 to 41.8; HotpotQA 26.0 to 25.0. GPT-4: 95.5 to 89.0; 82.0 to 80.0; 49.0 to 43.0 | b20, d13, d03 | [E] K13 |
| Execution-grounded critic is the main ingredient in LLM-writes-Soar-rules | Critic removed: -23 overall, -37 hard and variant; basic KB removed -17; case KB removed -14 (paper says "% reduction"; points vs relative not stated). Cycles above 1000x minimum without critic | a21, a22, b11, c03 | [S] K14 |
| NL2GenSym headline | N=100 (25 easy, 25 medium, 30 hard, 20 three-jug). Flash+framework 86% SR, 1.76x optimal cycles; qwen-max+framework 91%, 1.98x; manual 84% (3,390x optimal, 46.67% on hard); one-shot 55% Gemini Pro (20% on hard), 66% qwen; zero-shot 0%. Cap 500,000 cycles = fail | a21, b09, b10, c01, c02 | [S] |
| Small model with loop beats large model one-shot | Flash 86% vs Pro one-shot 55%; hard-case +56.67 over one-shot. Token cost of loop not reported | c04 | [S] K15 |
| Tie-style lookahead beats sampling at near-equal tokens on a search task | Game of 24, GPT-4: IO 7.3, CoT 4.0, CoT-SC k=100 9.0, CoT best of 100 49, ToT b=1 45, b=5 74. 5.5k vs 6.7k completion tokens; $0.74 vs $0.47. Crosswords: 60% word-level, 4 of 20 games; no backtracking 20% | b17, b18, c18, c19 | [S] K16 |
| Gating search on need saves cost | 75 to 85% fewer tokens, calls, runtime; GSM8K 0.98 to 0.97, Math500 0.87 to 0.86 (Qwen3-32B, 100 items). Weak evaluator (LLaMA3-8B): Math500 0.27 vs 0.39 for CoT | b19 | [S] K17 |
| No LLM agent has the whole Soar bundle | 42 systems, 10 architectures, 8 runtime families | a29, c10, c16, a18, b21, c20, c29 | [E] K18 |
| Typing the impasse is untested for LLM agents | Only typed-recovery number: PALADIN 89.68% vs CRITIC 76.34%, ToolBench 32.76%, vanilla 23.75% (Gemma-3 12B, simulated tool failures, fine-tuned, GPT-5 as simulator and grader) | c25, c10, c11 | [S] K19 |
| Diagnosis quality is the bottleneck of repair loops | Human feedback: GPT-4 repair success 33.3% to 52.6% (1.58x). Stronger-model feedback beats own feedback at every budget | d02, d13 | [E] K22 |
| Repair vs resample at equal budget is conditional | GPT-4 APPS: 10 samples + 1 repair each = 1.05x pass@20; 2 samples + 10 repairs each = 0.97x pass@22. GPT-3.5 gains marginal. Snell MATH: revision narrowly beats parallel only with fine-tuned reviser + verifier; per-question mix up to 4x less compute; naive revision turned 38% of correct answers wrong | d01, d03 | [C] K23 |
| Earlier failed attempts hurt later ones | Lost-in-conversation: 39% average drop (6 tasks, 200,000+ conversations); aptitude -15%, unreliability +112%; answers 20 to 300% longer; restating facts recovers only 15 to 20% | d04, d03 | [S] K24 |
| Isolated subtask contexts that return short results work | Context-Folding: 32K active window, 10 branches, no nesting; after RL 62.0% BrowseComp-Plus (N=150), 58.0% SWE-Bench Verified (N=500). THREAD Llama-3-8b ALFWorld 71.6 vs ReAct 20.1, ADaPT 30.6, Reflexion 25.4; CodeLlama-7b 91.0 vs 23.1. GPT-3.5, 5 runs: ALFWorld 95.7 (SE 0.28) | d05, d06 | [S] K25 |
| Code-fired stuck detectors are standard | OpenHands: 4 identical action-observation pairs; 3 identical erroring actions; 3 repeated messages; 6-step alternation; 10 context condensations; at least 3 filtered events. Reflexion: same action and response more than 3 cycles, or after 30 actions | d09, c20 | [S] K26 |
| Reflexion results | ReAct+Reflexion solved 130 of 134 ALFWorld tasks; +22% ALFWorld, +20% HotPotQA, +11% HumanEval; HumanEval 91% vs GPT-4 80% | c20 | [S] |
| Model-side stuck signals are unreliable | Missing-premise questions: 2x to 4x tokens (over 3,000 vs about 1,000) and mostly no abstention. Wrong answers contain more thought switches (underthinking score AIME24: QwQ 65.0, R1-Preview 75.7, R1-671B 37.0) | d10, d11 | [E] K27 |
| Stored routines help later tasks but can be wrong | AWM: +24.6% rel. Mind2Web, +51.1% rel. WebArena; online +8.9 to 14.0 points; authors warn about incorrect workflows | d07 | [S] K28 |
| Loop-like failures are common in multi-agent traces | MAST: step repetition 15.7%, missed completion 12.4%, reasoning-action mismatch 13.2%, premature termination 6.2%, no/incomplete verification 8.2%, incorrect verification 9.1%; kappa 0.88; 1600+ traces, 7 frameworks | d08 | [S] K29 |
| Depth or token cap for recursion is unmeasured | Context-Folding depth 1, 10 branches; THREAD max depth 6 to 10, uncapped; s1 30K cap slightly better (AIME24 N=30, caption) | d05, d06, d12 | [S] K30 |
| No replication of CogRec, NL2GenSym, STARS found | NL2GenSym citations 0 in index; other lookups rate-limited | d14 | [S] K31 |
| Impasse-driven grounding failure turns into an instructor query; learning is fast | colors 100% after about 1 example each; sizes 100% after 1.5; shapes 96% after 12.9; prepositions 93.98% of 144 arrangements after 3.17; verbs 1.26 examples per command | a28 | [S] |
| A diagnosis that names the step and cites evidence beats a generic failure summary | AgentDebugX: Who&When strict 28.8% (qwen3.5-9b) vs 21.7%; GAIA vanilla 55.8%, level-2 48.8 to 61.6 after one re-run | c27 | [S] |
| Cheap fork and return of a trial attempt is practical | Fork 134 to 143 ms (2 to 3% of a turn); cache hit about 95%; CooperBench 28.8% to 54.7% with runtime supervisor | c28 | [S] |

---

## 4. Mechanisms and models

Each mechanism is explained as an engineer would build it in a text scaffold.

### 4.1 Ordered arbitration with explicit exits [decision procedure]

Soar runs candidates through fixed filters in this order: required, acceptable, prohibited, rejected, comparisons, best, worst, indifferent (a10). Each filter can end in a winner or an impasse (a11).

A scaffold version, in code:

```
candidates = proposals (attempts, operators, answers)
1. hard constraints: if two requirements contradict -> CONSTRAINT-FAILURE
2. drop candidates failing a hard check (reject)
   -> if empty: NO-CHANGE (nothing left)
3. pairwise or ranked comparisons by code-run evidence
   -> if all candidates lose to another: CONFLICT
4. best / worst markers
5. tie-break by indifference: if several remain and nothing separates them: TIE
   -> else winner
```

Rules to copy:

- Hard constraints are checked before ranking (K04, single-source).
- The impasse record carries the candidate set and the cause (a11: "returning the set of all candidates passed into this filter"). Our record: which attempts, which evidence clashed. It feeds the subgoal prompt (G2).
- Only one impasse type is active per level at a time (a09). Give each subgoal level one type.

### 4.2 Impasse detectors [architectural rules]

All code-fired. None needs the model to say it is stuck.

| Soar impasse | Detector in a scaffold | Soar basis |
|---|---|---|
| State no-change | no candidate attempt produced, or all candidates dropped by hard checks | a03, a11 |
| Tie | several candidates pass the check and nothing separates them (same group by behaviour, equal score) | a09 |
| Conflict | two checks or two attempts give contradictory verdicts and neither is ruled out | a09 |
| Constraint-failure | two hard requirements cannot both hold (for example two required outputs) | a09, a12 |
| Operator no-change | the same attempt or operator is retried with no change in the check output over two rounds | a03, b04 |

Two cautions.

1. **Operator no-change is ambiguous** (a03, b04). It fires when knowledge is missing, and also when an action just takes several cycles. Laird's answer for the slow case is to wait. A counter without a progress test gives false alarms. Add a progress test (check output changed, new content in the tool trace). OpenHands uses thresholds of 3 and 4 repeats with no published precision or recall (d09). Our "same error twice" is more aggressive.
2. **Loops need a guard.** Generated Soar control hit state-no-change infinite loops; hand-coded baselines hit the 500,000-cycle cap on hard cases (a23, b03, c05). Keep a hard cap on rounds and a no-change counter (d12: a 30K thinking-token cap with a forced best guess was slightly better than none).

### 4.3 Typed response table [impasse resolution]

From the Manual (a12), translated:

| Impasse | Soar resolution | Scaffold response (a candidate, not tested) |
|---|---|---|
| Tie | add preferences to separate | compare the tied candidates: find the input where they differ and run it (S7 discriminating test), or make all indifferent and pick by a logged rule |
| Conflict | require one or reject others | find an outside check that rules one side out; do not ask the model to reconsider (b20) |
| Constraint-failure | change the rules; retract all but one | relax or drop one constraint (O4), or fall back to best attempt (G6) |
| State no-change | create operators | generate new candidates: reframe, retrieve, change representation (O6, O7) |
| Operator no-change | apply it, change the state, or prefer another | decompose the step (O3), or change the attempt; wait if progress is real |

Whether the typed version beats one generic recovery operator is untested (K19). Olausson (d02) says diagnosis quality decides success. A typed operator is worth keeping only if it makes the diagnosis more accurate.

### 4.4 Subgoal with isolation and typed return [substate]

Soar rules, from a04, a13, a14, b05:

1. The substate reads the superstate, nothing else.
2. It has its own preference memory and runs the same cycle.
3. It returns results only. All scratch data is deleted.
4. It ends the moment the parent can decide, even if the substate has more to say.
5. It does not act on the world. Actions go through the parent.
6. Soar records which superstate elements the result depended on (a justification). If those elements change, the substate is "regenerated": thrown away and rebuilt, and no learning happens from it.

Scaffold version:

```
subgoal(parent_state, impasse_record, operator):
    ctx = fresh context
    ctx.load(task text, impasse_record)       # no failed-attempt transcript
    result = run operator under a token budget B
    return {result, depends_on: [parent facts or check ids], type: impasse type}
parent: accept result only if depends_on still holds; else discard and learn nothing
stop the subgoal as soon as the parent check passes
```

Closest LLM evidence: Context-Folding, THREAD, Shepherd's fork/revert (d05, d06, c28). None isolates the isolation factor.

### 4.5 Bounded deliberation [time-bounded substates]

Laird says substate time can be monitored and a non-optimal or random decision made when time is short (a06, b06). Not specified, not measured (K08). A scaffold needs an explicit token budget per impasse, a forced best-guess answer on exhaustion (G6), and a depth cap. Starting points seen in the literature: depth 1 with 10 branches (d05); a 30K thinking-token cap (d12). No sweep exists (K30).

### 4.6 Preference authority order

Code checks > symbolic preferences > numeric or learned value (a08, a02). For us: executed checks first, then rules from the class record, then any learned score only to break remaining ties. A model judge never overrides a check (G5).

### 4.7 Lazy versus always-on deliberation

Soar starts look-ahead only after a tie (a06). Many LLM agents (ToT, RAP) run propose-evaluate at every step (a19, c17). Chain-in-Tree (b19) gates branching on need and cut cost 75 to 85% with small accuracy loss on math, but only with a strong evaluator. CoALA lists metareasoning (when to plan) as open (b22).

### 4.8 Chunk analogue: store the fix with its reason

After a solved subgoal, keep the fix keyed by the impasse type plus the problem class (a07). Boundaries to enforce:

- Do not store a fix from a tie settled by a sampled or voted choice (a07, a15: Soar adds no rule in that case).
- Store the reason for the choice, not only the choice (a15).
- Cap library size and count retrieval cost (b26, d07).
- Test a stored fix on a second problem before trusting it (c24: a reused rule forced each object into its own empty cabinet and slowed clearing, p=0.001).

---

## 5. What holds up

### 5.1 Holds up (two or more independent lines)

1. **Doubt and revision need external feedback.** Huang et al. (b20), Kamoi et al. survey (d13), Snell (d03: 38% of correct answers broken by naive revision), Olausson (d02: diagnosis is the bottleneck). Executor-grounded or knowledge-grounded checks help: NL2GenSym critic (-23 without it), STARS (+25 to +57 points). K13, K22 established.
2. **Code-fired triggers beat model-stated stuck.** Soar's design (a09-a11), Reflexion's counter (c20), OpenHands detector (d09), model-side signals poor (d10, d11). K01, K27 established. Caveat: nobody has published precision or recall for any code trigger.
3. **LLM agents rarely have a typed impasse.** CoALA, Fan and Lan (42 systems), Reflexion, agentic cognitive depth paper (c29). K18 established.
4. **Stored shortcuts cut later calls.** CogRec (figure), Zhu and Simmons (917 vs 54,754 tokens), STARS repeat run (100% with no LLM call, c21), Mohan 2012 (fast learning). K09. All toy or simulated.
5. **Impasse type count is a naming choice.** K02.

### 5.2 Single-source, own-group, or not equal-token

- NL2GenSym, STARS, CogRec share one weakness. Single run per condition in the main table (STARS repeated only its own arm 10 times). No equal-token best-of-N control. No ablation by impasse type. No replication found (K31, weak evidence of absence).
- STARS has no impasse mechanism at all. A Soar agent calls the LLM when a goal is unknown. It is a check-and-repair pipeline inside a Soar agent (b12).
- CogRec's example is a tie. The results are not split by impasse type. The gain over a plain LLM is small (+7.7% rel. on ML-1M HR@10). Pure Soar with about 20 rules scores 0.0511. Its baseline rule counts are inconsistent (20 hand rules, 5 without bootstrap, about 500 full).
- NL2GenSym's manual baseline was deliberately basic with no search control. The 84% and 3,390x are a floor, not an expert bar.
- PALADIN (89.68% recovery) needs fine-tuning on 50,000+ trajectories, simulated tool failures, GPT-5 as simulator and grader. A 2026 snippet (c26, unverified) says a logistic-regression controller matched annotated recovery decisions 63.6% vs 43% for PALADIN's own retrieval on 16,163 real events. If it holds, learned failure typing adds little over a simple classifier.

### 5.3 Contradictions and weak transfers

| Item | Detail |
|---|---|
| Laird 2022 fn 4 vs Manual | footnote: all selection impasses can be removed by more preferences. Manual: constraint-failure cannot. Manual is later and more specific. [C] |
| Repair vs resampling | Olausson: repair often equal or worse at equal budget. Snell: revision wins with a trained reviser and verifier. NL2GenSym and STARS: untested. [C] |
| Self-correction | Earlier positive reports used oracle stopping signals (b20, d13). |
| ToT | wins on tasks chosen so search helps (Game of 24, crosswords). Authors say it may be unnecessary where GPT-4 already does well. Its cost edge is only in completion tokens, not dollars ($0.74 vs $0.47). With a weak evaluator, tree-gating work falls toward CoT (b19). |
| STARS selection step | adds 0 points in kitchen for +13,785 tokens (b13). A model chooser needs world facts. |
| Prompt-only folding agent | did not match long-context ReAct (d05). The big wins used RL training. |
| Soar chunk quality | 1263 rules to 8 after the 9.6 redesign (a15). Old chunks were over-specific. |
| Stored workflows | can degrade results; offline workflows can mismatch the test distribution (d07). |
| Reused production rule | quietly changed behaviour (c24). |

### 5.4 Moderators

- Reliability of the external feedback (d13, d02).
- Whether the task is search-shaped with some baseline success (b17, G12).
- Strength of the evaluator used to decide branching (b19; c19: GPT-4 generation + GPT-3.5 evaluation 64%, GPT-3.5 generation + GPT-4 evaluation 31%, so generation was the bottleneck).
- Whether a verifier gates revision (d03).
- World facts available to a selector (c23: 77.5 to 92.5).

### 5.5 Interventions that worked

Execution-grounded critic; agent-side check and repair of LLM answers; code-fired repeat counters (Reflexion, OpenHands); storing validated fixes; fork-and-return of a trial; forced best guess at a cap (weak).

### 5.6 Interventions that did not work or are not shown to

Asking the model to reconsider its own answer; wider candidate trees without a check; a model selector without task context; always-on branching on easy steps; restating facts after a failed attempt (recovers only 15 to 20%, d04).

---

## 6. Language models

### 6.1 How LLMs behave on impasse-like tasks

- **Writing Soar control knowledge.** Zero-shot: 0% for both Gemini-2.5-Pro and Qwen-max on Water Jug (c02). One-shot: 55% (Gemini Pro, 20,344 mean cycles) and 66% (Qwen, 20,670 cycles). Without feedback the models cannot write working impasse-handling rules. They loop. A critic message in the appendix names a state no-change loop caused by a syntax error that left too few rules loaded (c05).
- **Answering as a knowledge source.** Over 70% of raw GPT-3 goal responses were unviable for the embodied agent (kitchen), 58% (groceries), 85% (office) (a26, c22).
- **Self-correction.** Without outside feedback accuracy falls, sometimes sharply (CommonSenseQA 75.8 to 41.8 for GPT-3.5) (b20).
- **Unsolvable problems.** Reasoning models spend 2x to 4x more tokens on missing-premise questions and mostly fail to abstain (d10). Wrong answers show more switching between lines of thought (d11). Model-side "I am stuck" is not a safe trigger.
- **Failed attempts in context.** Models lean on earlier wrong attempts; answers grow longer; they do not recover (d04). Naive revision broke 38% of correct answers (d03).
- **Selection among candidates.** A GPT-4 selector showed a small recency bias (b13). A weak LLM as branch decider drops accuracy toward CoT (b19).

### 6.2 What changed behaviour, by how much

| Change | Effect | Source |
|---|---|---|
| Execution-grounded critic added to rule writing | removal cost -23 overall, -37 hard/variant | b11 |
| Smaller model + critic loop vs bigger model one-shot | 86% vs 55% | c04 |
| Agent-side analysis and repair of LLM goals | +25.0, +27.7, +57.2 points completion | a27 |
| Added three world facts to the selector prompt | 77.5 to 92.5 | c23 |
| Propose-evaluate-backtrack (ToT, b=5) vs best of 100 CoT | 74 vs 49 at 5.5k vs 6.7k tokens | b17, c19 |
| Gate branching on need | 75 to 85% cost cut, about 1 point accuracy loss (strong evaluator) | b19 |
| Reflexion counter-triggered reflection | ALFWorld 130/134 tasks | c20 |
| Human diagnosis of code errors | GPT-4 repair success 33.3% to 52.6% | d02 |
| Stored workflows | +24.6% and +51.1% relative | d07 |
| Stored production rules in a Soar-inspired agent | 54,754 to 917 query tokens | c24 |
| Branch-and-fold subtask contexts (with RL) | 62.0% / 58.0% at 32K window | d05 |
| Recursive child threads (prompt only) | ALFWorld 71.6 vs 20.1 (Llama-3-8b) | d06 |
| Run-level diagnosis then one re-run | GAIA level-2 48.8 to 61.6 | c27 |

### 6.3 What is not known for LLMs

The central question for us (K19): does the type of the impasse change the best response, and does a typed subgoal beat one generic recovery step at equal tokens? No source tests it. The only typed-recovery number (PALADIN) is for tool errors with fine-tuning. The review that checked 42 systems (a29) found that no one tested the Soar bundle as a whole.

Net: the evidence supports code-fired triggers, grounded feedback, a fresh typed-return subgoal as a plausible design, and an equal-token best-of-N control. It does not yet support impasse typing as a source of gain.

---

## 7. What our agent should take

Each item gives: schema part, status, evidence ids. Statuses reflect the strength of evidence for the claim, not for the Soar design.

### Add now (established)

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Fire S6 only from code-visible events (no pass after rounds, same error twice with no change, no candidates, disagreeing checks, budget fraction). Never from the model saying it is stuck. Already in the schema; keep it and do not weaken it. | G1, S6 | [E] | a09, a10, a11, b04, d10, d11, c20, d09; K01, K27 |
| A2 | Revise only from real output. Resolve a conflict between two attempts by running a check, not by asking the model to reconsider. | G2, S5 | [E] | b20, d13, d03, d02, b11, a27; K13, K22 |
| A3 | Type an impasse by what our checks can detect (no candidate, several equal passers, contradicting verdicts, no change in check output), not by copying Soar's count of types. | S6 | [E] | b01, b02, a09, b03; K02 |
| A4 | Log, for every S6 fire: trigger, impasse type, candidate set, cause, tokens spent after, and whether progress followed. No behaviour change. This gives the base rates and trigger false-alarm rate (gaps 3 and 7). | Section 6 logging, S6 | [E] that nobody has the numbers | d09, d08, d14; K26, K29 |
| A5 | Keep a hard round cap and a no-change counter so an impasse loop cannot run forever. Submit the best attempt on exhaustion. | G6, G11, S6 | [E] (loops are a real failure of generated control) | a23, b03, c05, d12 |
| A6 | Test every new element in this file against best-of-N plus a code check at equal total tokens before it enters SCHEMA.md. | G7 | [E] (matched-budget evidence is mixed) | d01, d03, b14; K23 |
| A7 | Do not count on typing alone for accuracy. Expect small effects; measure accuracy and tokens together. | G7 | [E] by absence of evidence | a25, c07; K10, K19 |

### Test first

| # | Take | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Typed vs generic recovery: impasse-typed operator choice (tie: compare; no-change: reframe or retrieve; conflict: discriminating test; constraint-failure: relax or abandon) vs one generic recovery operator. Score by diagnosis accuracy first. | S6 operator choice | [S] | a12, d02, c25; K19, K22 |
| T2 | Isolation: a subgoal in a fresh context holding only the typed impasse record and returning one typed result, vs the same step in the shared context with failed attempts visible. | SUBGOAL, G3 | [S] benefit; [E] mechanics | a04, a14, d04, d03, d05, d06; K05, K24, K25 |
| T3 | Repair loop vs best-of-N plus check vs mix at equal tokens, per difficulty bin. | S5, G7, G12 | [C] | d01, d03, a27, c01; K12, K15, K23 |
| T4 | Hard-constraint check before ranking in S6, and a constraint-failure exit (two contradictory requirements) that goes to the best attempt (G6) instead of looping. | S6 order, G6 | [C] for the claim, [S] for the order | a09, a12, b07, d10; K03, K04 |
| T5 | Impasse-gated branching (tie lookahead only on a tie) vs always-on propose-evaluate at equal tokens, with a weak and a strong evaluator. | S3, G1, G12 | [S] | a19, b19, b17; K16, K17 |
| T6 | Return a dependency list with each subgoal result. Discard the result and learn nothing if a listed fact changes. | SUBGOAL, S9 | [S] | a13, a14, a16 |
| T7 | Typed lessons in S9, keyed by impasse type and class. Exclude lessons that rested on sampled or voted choices. Add a size cap. | S9, memory | [S] | a07, a15, b26, d07, c24; K06, K09, K21, K28 |
| T8 | Subgoal budget and depth cap with forced best-guess exit. | G6, G7, S6 | [S] | a06, d05, d06, d12; K08, K30 |
| T9 | Stall detector with a progress test (stuck vs slow): precision and recall of "same error twice" against hand labels. | S6 trigger | [S] | a03, b04, d09; K07, K26 |
| T10 | Recursive same-schema subgoal vs a separate meta-prompt controller. | S6 design | [S] | a05, c15; K20 |
| T11 | A model selector needs world facts. Test selection quality with and without a short task-fact block. | S7, G5 | [S] | b13, c23 |

---

## 8. Concrete tests on our bench

All arms get the same total token budget per item (G7). Report accuracy, tokens, trigger counts, and per-bin results (easy, mid, hard by plain pass rate, G12). At least 3 seeds. Run through the existing harness (`bench` skill).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 base rates (A4) | all current bench items, plain scaffold with logging on | no arms; count events per class | share of items with tie, no-change, conflict, constraint-failure; trigger fires per item; fires followed by progress | Impasse is rare on easy classes; no-change dominates. If ties plus conflicts are under about 5% of items, typing will not pay. |
| E2 trigger precision (T9) | items with tool or check output; 100+ stall events hand-labelled stuck / slow / unclear | "same error twice" vs "no change 2 rounds" vs "no change 3 rounds" vs with progress test vs model-stated stuck | precision, recall, wasted tokens per false alarm | Code triggers beat model-stated. A progress test raises precision. Two rounds fires more false alarms than 3 (OpenHands uses 3 and 4). |
| E3 typed vs generic (T1) | items where S5 failed and S6 fired (from E1 logs), plus seeded cases of each type | generic recovery (one prompt) vs typed operator table vs random-typed control | end accuracy; diagnosis accuracy against code-derived ground truth | If typing helps, it helps via diagnosis. Random-typed should be worse than correct-typed or the label does nothing. Expect a small effect (CogRec size, 4 to 9%) at best. |
| E4 isolation (T2) | S6 events on checked-mode items | fresh context + typed record vs shared context with failed attempts vs no subgoal | accuracy on the retry; rate of repeating the earlier failed answer | Fresh context cuts repeats of the earlier wrong answer. Gain if d04's anchoring carries to agents; restating facts alone recovers only 15 to 20%. |
| E5 repair vs resample (T3) | checked-mode items, binned by plain pass rate | best-of-N + check; analyse-repair loop; mix (resample first, repair near-misses) | accuracy per bin at equal tokens | Repair ties or loses on easy bins; wins only on mid bins when the check gives a precise trace. Mix wins overall (Snell: up to 4x). |
| E6 seeded contradiction (T4) | 30 items with two contradictory hard requirements, plus 30 matched solvable twins | no handling; G6 fallback only; hard-constraint check before ranking with constraint-failure exit | loop rate; tokens before exit; accuracy on solvable twins (no loss) | No handling loops and burns 2x to 4x tokens (d10). The exit saves most of those tokens with no loss on twins. |
| E7 gated vs always-on branching (T5) | items with a branching foothold (non-trivial plain pass rate) and items without | impasse-gated lookahead vs every-step lookahead vs no lookahead | accuracy; tokens | Gated matches always-on at far fewer tokens (b19: 75 to 85%). With a weak evaluator both fall toward plain. |
| E8 fix library (T7) | stream of 50+ items from 3 classes with repeated impasse types | no library; typed library; typed library with size cap; library including lessons from voted picks | tokens per item including retrieval; accuracy on later items; wrong-fix rate | Typed library cuts tokens on later items of the same class. Voted-pick lessons add wrong fixes. An uncapped library slows retrieval (expensive-chunk effect). |
| E9 dependency discard (T6) | items where the problem is restated or a check result is replaced mid-run | result kept vs result discarded when listed facts change | stale-result error rate | Fewer stale results used; small token cost. |
| E10 depth and token cap (T8) | items that trigger nested subgoals | depth cap 1, 2, 3; token cap per subgoal at 5%, 15%, 30% of item budget; no cap | accuracy; tokens; share of runs hitting the cap | Depth 1 or 2 captures most of the gain (Context-Folding used depth 1). Uncapped wastes tokens on unsolvable items. |
| E11 selector with task facts (T11) | tie cases where candidates are viable but differ in fit | model selector without facts; with a 3-fact block; code selector | selection accuracy; cost | Facts help (c23: 77.5 to 92.5). A code selector wins where a check exists (G5). |
| E12 recursive vs meta controller (T10) | S6 events | same-schema subgoal vs separate meta prompt that decides what to do | accuracy; tokens; code complexity | Little difference; keep the simpler. Low priority. |

---

## 9. What does not transfer, and why

| Soar feature | Why it does not transfer |
|---|---|
| The rule base and parallel rule firing | Soar has thousands of hand or learned rules (TacAir-Soar over 8,000, c13). We have a model and a few code checks. Elaboration to quiescence has no counterpart. |
| Fixed preference semantics as a complete knowledge base | Preferences come from rules with exact conditions. Ours would come from check results or model judgments, which are noisy. A model-made "better than" is an opinion (G5, G10). |
| Automatic impasse detection from preference structure | The structure is exact in Soar. For us the detector is only as exact as our checks. A tie between "equally plausible" attempts is not a crisp set. |
| Truth maintenance (automatic retraction) | Soar retracts proposals when conditions vanish (a16) and tracks the superstate facts a result used (a13). A scaffold has no dependency tracking unless we build it. |
| Chunking as exact explanation-based learning | Needs deterministic substate decisions (a07). LLM substates are sampled. Correct chunk conditions need a trace of what was needed; we have only text lessons. Soar adds no rule when random or numeric selection was used. |
| Universal subgoaling to arbitrary depth | Stack depth is unbounded in principle (a04). Context and token cost make deep stacks costly; Context-Folding forbids nesting (d05). |
| Impasse-gated cost model | Soar substate reasoning costs time. Our cost is tokens, and the first pass is already expensive. G11 says think briefly by default. |
| Operator no-change as a clean signal | In Soar the architecture knows an operator was selected and for how long. In an LLM loop "same operator" is vague text. Use output equality and check output instead. |
| "Wait" as the answer to slow actions | Right for a slow external tool. In a text scaffold with no external process the waiting case is rarer, but slow tool calls exist. |
| Laird's claim that meta-reasoning needs no separate module (K20) | A design argument. For us the program is already a separate controller by design (SCHEMA section 1). |
| Human-style speed data (50 ms cycle, System 1/2 mapping) | Laird himself hedges the System 1/2 mapping (b08). Do not cite as human evidence for escalation. |
| The sizes of the Soar-hybrid wins | Simulated domains (kitchen, Water Jug), a recommender with a tiny gain, single runs. Do not carry the sizes to reasoning benchmarks. |

---

## 10. Open questions

1. Does the type of the impasse matter for an LLM agent? (K19, central.)
2. At equal tokens, does generate-run-critique or analyse-repair-select beat best-of-N plus check? Neither NL2GenSym nor STARS has the control; STARS cost 3.4x to 5.9x the tokens.
3. How good are code triggers at precision and recall, and how often is a fired trigger a false alarm (stuck vs slow)?
4. What does isolation buy in itself? Anchoring on earlier failures vs saved context.
5. Does storing the fix from a subgoal help later items at equal tokens, and where does retrieval cost or over-general fixes erase it?
6. Replication of CogRec, NL2GenSym and STARS with seeds and other domains.
7. What is the base rate of each impasse type in LLM reasoning traces? MAST has loop-like labels at about 12 to 16% but no tie or conflict category.
8. What do Laird 2012 and the 1987 paper say about universal subgoaling and the claimed link between impasse type and search method? Not opened.
9. Does "all impasses can be resolved by more preferences" hold in practice for LLM agents, or do contradictory hard constraints need a fallback beyond G6?
10. Is time- or token-bounded subgoal reasoning better than unbounded at equal tokens, and what depth cap is right?
11. Does a simple classifier match a typed taxonomy (c26 snippet)? If yes, the typed table is not worth its cost.
12. How often does an LLM scaffold reach a true impasse rather than a plain wrong answer? (SCHEMA S6 notes Ohlsson: impasse may be only about 8% of problems.)
13. Check the Soar 9.6 text on constraint-failure and the time-bound fallback in full (partly read).

---

## 11. Sources

[V] opened and read this run; [M] snippet, abstract or search summary only.

**Soar primary and reviews**

- [V] Laird (2022) Introduction to the Soar Cognitive Architecture. https://arxiv.org/pdf/2205.03854 (a01-a08, b01, b04-b08, c13-c15)
- [V] Laird et al. (2017) Soar Manual 9.6, ch. 2 The Soar Architecture. https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/ (a09-a14, a16, b02)
- [V] Laird et al. (2017) Soar Manual 9.6, ch. 4 Procedural Knowledge Learning. https://soar.eecs.umich.edu/soar_manual/04_ProceduralKnowledgeLearning/ (a15)
- [V] Laird (2021) An Analysis and Comparison of ACT-R and Soar. https://arxiv.org/pdf/2201.09305 (a17)
- [V] Allen (1988) Production System Chunking in Soar (NASA JSC report). https://ntrs.nasa.gov/api/citations/19890010689/downloads/19890010689.pdf (a31; secondary, poor OCR)
- [V] Lehman, Lewis, Newell (1991) NL-Soar. https://public.websites.umich.edu/~rickl/pubs/lehman-lewis-newell-1991-cogsci-conf.pdf (b24)
- [M] Laird, Newell, Rosenbloom (1987) SOAR: An architecture for general intelligence. https://apps.dtic.mil/sti/pdfs/ADA188742.pdf (a32, d15; downloads blocked)
- [M] Laird (2012) The Soar Cognitive Architecture, MIT Press. https://mitpress.mit.edu/9780262122960/ (a33)
- [M] Laird, Rosenbloom, Newell (1986) Chunking in Soar. https://doi.org/10.1023/A:1022639103969 (a34)
- [M] Nason and Laird (2005) Soar-RL. https://doi.org/10.1016/j.cogsys.2004.09.006 (a35)
- [M] Tambe, Newell, Rosenbloom (1990) The problem of expensive chunks. https://link.springer.com/article/10.1007/BF00117107 (b26)
- [M] Laird, Lebiere, Rosenbloom (2017) A Standard Model of the Mind. https://ojs.aaai.org/index.php/aimagazine/article/view/2744 (b27)
- [M] Brown and VanLehn (1980) Repair Theory. https://www.lri.fr/~mbl/Stanford/CS477/papers/RepairTheory-SeelyBrown.pdf (b25)
- [V] Mohan, Mininger, Kirk, Laird (2012) Acquiring Grounded Representations of Words with Situated Interactive Instruction. https://arxiv.org/pdf/2502.20754 (a28; not re-opened by the cross-checker)

**LLM agents with Soar or impasse structure**

- [V] Sumers, Yao, Narasimhan, Griffiths (2024) CoALA. https://arxiv.org/pdf/2309.02427 (a18, a19, b21, b22, c16, c17)
- [V] Yuan et al. (2025) NL2GenSym. https://arxiv.org/pdf/2510.09355 (a20-a23, b03, b09-b11, c01-c05; numbers re-checked)
- [V] CogRec (2025) CogRec: A Cognitive Recommender Agent Fusing LLMs and Soar. https://arxiv.org/abs/2512.24113 and https://arxiv.org/html/2512.24113 (a24, a25, b15, b16, c06-c09; ablations in figures only)
- [V] Kirk, Wray, Laird (2023) Exploiting Language Models as a Source of Knowledge for Cognitive Agents. https://arxiv.org/pdf/2310.06846 (a26; not re-opened)
- [V] Kirk, Wray, Lindes, Laird (2024) STARS. https://arxiv.org/abs/2306.06770 and https://arxiv.org/html/2306.06770v4 (a27, b12-b14, c21-c23)
- [V] Wray, Kirk, Laird (2021) Language Models as a Knowledge Source for Cognitive Agents. https://arxiv.org/pdf/2109.08270 (a30; abstract and passages)
- [V] Zhu and Simmons (2024) Bootstrapping Cognitive Agents with a Large Language Model. https://arxiv.org/abs/2403.00810 (c24; table scrambled)
- [V] Joshi and Ustun (2023) Augmenting Cognitive Architectures with Large Language Models. https://ojs.aaai.org/index.php/AAAI-SS/article/download/27689/27462/31740 (b23)
- [V] Romero et al. (2023) Synergistic Integration of LLMs and Cognitive Architectures. https://arxiv.org/abs/2308.09830 (c31)
- [V] Fan and Lan (2026) From Cognitive Architectures to Language Agents: A Mechanism-Level Review. https://arxiv.org/pdf/2607.23942 and https://arxiv.org/abs/2607.23942 (a29, c10-c12)
- [V] Agentic Cognitive Depth (2026). https://arxiv.org/abs/2610.04168 (c29)

**Search, self-correction, repair, recovery**

- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/pdf/2305.10601 (b17, b18, c18, c19)
- [V] Chain-in-Tree (2025) Back to Sequential Reasoning in LLM Tree Search. https://arxiv.org/html/2509.25835v1 (b19; page-fetch summary)
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (b20)
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297 (d13; abstract and first pages)
- [V] Olausson et al. (2024) Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896 (d01, d02)
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314 (d03)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c20; not re-opened)
- [V] Vuddanti et al. (2025) PALADIN. https://arxiv.org/abs/2509.25238 (c25)
- [M] Recovery Is a Decision, But Whose? (NeurIPS 2026). https://neurips.cc/virtual/2026/166916 (c26; snippet only)
- [V] Zhu et al. (2026) AgentDebugX. https://arxiv.org/abs/2607.18754 (c27; not re-opened)
- [V] Yu et al. (2026) Shepherd. https://arxiv.org/abs/2605.10913 (c28; not re-opened)

**Context, memory, stopping, base rates**

- [V] Laban et al. (2025) LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (d04)
- [V] Sun, Lu, Ling et al. (2025) Context-Folding. https://arxiv.org/abs/2510.11967 (d05; table scrambled, text numbers used)
- [V] Schroeder et al. (2025) THREAD. https://arxiv.org/abs/2405.17402 (d06)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (d07)
- [V] Cemri et al. (2025) Why Do Multi-Agent LLM Systems Fail? (MAST). https://arxiv.org/abs/2503.13657 (d08; percentages from text)
- [V] OpenHands controller stuck.py, release 0.30.0. https://github.com/All-Hands-AI/OpenHands/blob/0.30.0/openhands/controller/stuck.py (d09)
- [V] Fan, Li, Sun, Zhou (2025) Missing Premise exacerbates Overthinking. https://arxiv.org/abs/2504.06514 (d10)
- [V] Wang et al. (2025) Thoughts Are All Over the Place (underthinking). https://arxiv.org/abs/2501.18585 (d11)
- [V] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (d12; caption level)
- [M] Illusion of Thinking (2025). https://arxiv.org/abs/2506.06941 (c30; abstract only)
- [V] Semantic Scholar citation lookup for NL2GenSym (negative result). https://api.semanticscholar.org/graph/v1/paper/arXiv:2510.09355/citations (d14)

**Cross-links to parallel subfields** (not covered here): Soar chunking and learning from impasses; Means-ends analysis; Representational change (constraint relaxation, chunk decomposition); Adaptive stopping and metareasoning; LLM metacognitive harness; Verification design; Progress monitoring theory; Consistency-based diagnosis and conflict generation.
