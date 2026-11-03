# Failure-driven CBR: deep document

*Subfield C08.10. Key works: Schank, Hammond, Riesbeck, Kolodner [M]. Evidence in this folder: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K28), critique.md. Cross-checked 2026-11-03. Related subfields researched in parallel (links only, not covered here): Dynamic memory, early CBR; Incremental mapping; Analogical problem solving; Self-explanation; Learned refinement and self-verification; Confidence and metacognition; Debiasing by training; Pruning of decision trees; Chain-of-thought prompting.*

## 1. What it is

Failure-driven CBR keeps failures as first-class cases. A failure is stored with an explanation of why it happened. It is indexed so that it comes back when the same trap is about to be met again. The stored thing is not "the answer was wrong". It is "in situations with features F, doing X causes Y, because Z; the repair is R".

The classical idea has four parts:
1. **Detect** a failure (a simulator, a contradicted expectation, a test).
2. **Explain** it with a causal chain, and pick out which input features caused it.
3. **Repair** the plan, using a repair strategy chosen by the type of the explanation.
4. **Store and index** the failure under the features that predict it, so a later, different-looking task with the same abstract features is warned before it plans.

The modern LLM version is looser. After a failed trial, the model writes a verbal reflection. The reflection goes into a small memory and is shown on the next try (Reflexion). Later systems distil lessons across many tasks (ExpeL, ReasoningBank, Mistake Notebook Learning, MemGuard).

Why it matters for our agent: the schema has a "Lessons" memory (SCHEMA section 5) that holds one line per problem class. Failure-driven CBR is the research on what such a line should contain, when it should fire, how to stop wrong lessons from spreading, and whether it beats just trying again. The answer is mixed. The classical design is elegant but was never measured. The LLM versions give gains of a few points up to 20 points, mostly with an outside outcome signal, and on small models they lose to plain resampling at equal cost.

## 2. History and theories in depth

### 2.1 Riesbeck 1981: failure-driven reminding (a06, a07)
Riesbeck's ALFRED program (IJCAI-81) is the first formal use. When a comprehension rule fails, the program does not change the rule. It stores the failure and its fix as an **exception episode** attached to the rule. Later failures of that rule retrieve the stored episodes. The rule is rewritten only when the exceptions can be grouped into a class.

Worked example: "$55 billion" is judged large, then shown to be small next to $1.23 trillion. Later "100,000 barrels" is judged large, then shown small next to 6 million barrels per day. Reminded of the first error, the learner caught the second. With more expertise the everyday rule ("big number = big effect") becomes a cautious rule: "do not assume, find out". The rule stays in use after its first failure and is questioned only when another case contradicts it (anomaly-driven doubt). This matches our guardrail G1: doubt on a signal, not on a schedule.

Limits: preliminary program, hand-analysed input, no classification scheme for exceptions, no quantitative test. The author notes a rule with known problems can still produce plausible wrong beliefs. The lesson is domain-scoped: the everyday rule stays valid outside economics.

### 2.2 Schank 1982: dynamic memory (a08, c21; not opened)
Schank's claim: memory is failure-driven. When an expectation fails, the failure is noted, a reminding of an earlier similar failure is triggered, and the memory structure is reorganised. Understanding and learning are one process. It is a theory book with no experiments. We did not open it; the account is from secondary sources. See the parallel subfield "Dynamic memory, early CBR".

### 2.3 Hammond 1986: CHEF (a01-a05, b24, b25, c18, c19)
CHEF is the canonical failure-driven case-based planner. Domain: Szechwan cooking, with a simulated world and hand-written causal rules. Six processes: anticipation, retrieval, modification, repair, credit assignment, storage.

The founding example, beef and broccoli:
- CHEF adapts a plan for beef and green beans to broccoli. The simulation shows soggy broccoli, because liquid from the beef wets it.
- It builds a causal explanation by back-chaining from the failed state to the steps that caused it.
- The explanation selects one of **20 known TOPs** (Thematic Organization Packets) of repair strategies. The soggy failure maps to SIDE-EFFECT:DISABLED-CONDITION:CONCURRENT. **Three strategies** attach: SPLIT-AND-REFORM, ALTER-PLAN:SIDE-EFFECT, ADJUNCT-PLAN. Only SPLIT-AND-REFORM was feasible: stir-fry the parts apart and join at the end.
- Credit assignment uses the explanation to decide which input features to blame. Only those are linked to the failure memory (marker-passing demons under MEAT and VEGETABLE). One failure produced two demons: "meat sweats when stir-fried" and "stir-frying in too much liquid makes crisp vegetables soggy".
- The index is **three goal features**: include meat, include a crisp vegetable, make a stir-fry. Later a chicken and snow peas request has the same abstract features, so CHEF is reminded of the failure and plans around it before it plans. Retrieval found the repaired beef-and-broccoli plan, not the surface-closer chicken-and-green-beans plan.
- A repaired plan is stored under the goals it meets and the problems it avoids ("avoids soggy vegetable").

The key design insight: **index by the abstract conditions that cause the trap, not by the surface topic.** Surface similarity would have picked the wrong plan.

Limits: one worked example, no test set, no error rates. The feature vocabulary was hand-chosen to capture the interaction. Repair quality depends on the hand-built causal rule base. Failure detection was by a simulator. Multi-cause failures have no single item to blame, and some repairs are too complex to reuse (b24). Credit assignment is only as good as the causal model: a wrong explanation indexes the lesson under the wrong features and it mis-fires later (a04). Hammond's thesis and 1990 journal paper were not opened (a11, a12); the IJCAI-87 abstract was (b25).

### 2.4 Schank and Leake 1989: SWALE (a09, a10)
SWALE explains anomalies (the racehorse Swale died after a light gallop). It retrieves old explanation patterns (XPs) from other deaths, tweaks them to fit, evaluates and stores the best. Failed tweaks are kept as a resource because they open new options. Three example remindings gave six explanations: Jim Fixx (1), Janis Joplin (2), "too much sex will kill you" (3). Some were "quite fanciful or can be ruled out". A tiny demonstration; quality was judged by program heuristics. Lesson: **reminding produces candidate explanations, not truths. They need a filter.** The full PDF was blocked.

### 2.5 Kolodner 1993 and micro CHEF (a13, a14)
The standard text treats failure as a retention trigger: store the failed case with its explanation, repair and the indices that would have predicted the failure. Not opened; treat as unverified. A secondary page on micro CHEF reports that a chatbot gave plausible causes of soggy broccoli but missed the broth explanation. Anecdote only.

### 2.6 The modern line
- **Reflexion** (Shinn et al. 2023; a15-a18, b01-b05, c01-c03): verbal reflection after failure, stored in a window of 1 to 3 items.
- **ExpeL** (Zhao et al. 2024; a19, a20, b06-b08): insights extracted by comparing a failed and a successful run of the same task.
- **ReasoningBank** (Ouyang et al. 2025; a21, a22, b09-b11, c06-c08): strategy items distilled from successes and failures.
- **Memento** (Zhou et al. 2025; a23, c09): a case bank of (state, action, reward) triples.
- **AgentDebug** (Zhu et al. 2025; a28, b23, c17, d16): a failure taxonomy and root-cause feedback.
- **Mistake Notebook Learning** (a30), **trajectory-informed memory** (a29), **MemGuard** (d09, d10), **ConMem** (d11), **U-Mem** (d05, d06).
- **Critics of reflection**: Huang (a25, b16, c12), Kamoi (b17, d14), Li (c13), Xing (c14), Mirzaei (d01), Verma (d02), VRL-Bench (d04).
- **Memory hazards**: Xiong (b14, b15, d08), Zhang (d07), Dixit (c15, c16), Cheng (d15).

A review (c24) maps the CBR cycle (retrieve, reuse, revise, retain) onto LLM agents and notes that introspection can tell retrieval failure from adaptation failure. It has no new measurements.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources agree), S = single source, C = contested. Numbers marked "corrected" were fixed in critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| CHEF: failure indexed by 3 abstract goal features warns before planning | 3 index features; 20 TOPs; 3 repair strategies for the soggy case; 2 demons from 1 failure. No test set | a01-a05, b24 (Hammond 1986) | S, design only (K01) |
| Failure-driven reminding: store exception, keep rule, rewrite only when exceptions group | 2 worked examples; no evaluation | a06, a07 (Riesbeck 1981) | S, design only (K02) |
| SWALE remindings give fanciful explanations that need a filter | 3 remindings gave 6 explanations | a10 | S |
| Reflexion: verbal reflection raises repeated-trial success with an outside signal | ALFWorld 130 of 134 solved in 12 trials (+22 points); HotPotQA +20 points (100 q); HumanEval pass@1 91 vs 80 (GPT-4) | a15, b01, c01 | S (K03) |
| Reflection text beats raw failed trajectory | HotPotQA CoT(GT) +8 points over episodic memory only (100 q) | a16, b02 | S (K04) |
| Reflection needs a test signal; tests need reflection | Rust, 50 hardest, GPT-4: base 0.60; no tests 0.52; tests, no reflection 0.60; both 0.68 | a17, b03, c02 | S (K04) |
| False-positive self-tests cap the loop | false pass 16.3% MBPP vs 1.4% HumanEval; Reflexion lost to plain GPT-4 on MBPP | a17, b05 | S (K05) |
| Reflexion gives no gain on WebShop | 100 envs, 4 trials, no improvement | b04, c03 | S (K05) |
| Hallucination loop | 22% of ALFWorld runs, 134 tasks | a18 | S (K05) |
| Confabulated lessons freeze the agent | 0 of 121 reflections named the blocking object; frozen envs 7.6 trials vs 1.5; r = 0.808; frozen share ALFWorld 16/50, WebShop 55/67, HotpotQA 46/100, HumanEval 4/23 | c15 (Dixit 2026) | S (K06) |
| Quote-the-trace mitigation | object mention 0% to 86% (134/156); repeat ratio 0.64 to 0.10; solved only 3/16 vs 2/16 no memory | c16 | S (K06) |
| ExpeL insights vs raw retrieval | insights-only vs retrieve-only: HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38 | a19, b06 | S (K07) |
| ExpeL vs Reflexion (corrected) | ALFWorld ExpeL one attempt 59.0 vs ReAct+Reflexion R0-R3 40.3, 47.8, 52.2, 54.4. ExpeL+Reflexion 54.5 to 60.4 (retrieve-only) and 59.0 to 64.2 (full). HotpotQA ExpeL 40 vs Reflexion 39 | b06, critique item 2 | S |
| ExpeL retrieval ablation | ALFWorld ReAct 40.0, random 42.5, reason-similarity 48.5, task-similarity 59.0 | b08 | E (K08, with Memento and Xiong) |
| ExpeL extractor ablation | HotpotQA ReAct 28.0, hand-crafted 32.0, insights built with reflections 29.0, gpt-3.5 extractor 32.0, full (gpt-4) 39.0 | b07, a20 | S |
| ReasoningBank: failures help only with the right design | Shopping, Gemini-2.5-flash: no memory 39.0; Synapse 40.6 to 41.7; AWM 44.4 to 42.2; ReasoningBank 46.5 to 49.7. WebArena +8.3/+7.2/+4.6 over no memory (3 backbones) | a21, b09, b10, c07 | S (K09) |
| Noisy success judge | real judge 72.7%; success flat across 70-90% simulated accuracy; about 50.6 at top vs 47.6 at 50% (Shopping only) | a22, b11, c08 | S (K10) |
| Memento: small K, shrinking gain | best K=4; DeepResearcher F1 59.9 (K=0) to 63.6 (K=1), flat 63.9-64.5 for K=4 to 32; GAIA 87.88 val / 79.40 test; CBR gain under 1 point by iteration 5 | a23, c09 | S |
| Intrinsic self-correction hurts (corrected) | GPT-3.5 CSQA 75.8 to 38.1 (3 calls) / 41.8 (5 calls); GSM8K 75.9 to 75.1 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0. Oracle: GPT-3.5 GSM8K 84.3, CSQA 89.7, HotpotQA 29.0; GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0 | a25, b16, critique 1 | E (K11) |
| Error location is the bottleneck | GPT-4 52.87% on 2186 traces (BIG-Bench Mistake); backtracking with the location fixes 23.53%, breaks 11.11% (word sorting); gains exceed losses at roughly 60-70% finding accuracy | b18 | E (K12) |
| Blind spot to own errors | 64.5% average over 14 open non-reasoning models; 179.5% more correction markers for external errors; "Wait" cuts it 89.3%; LoRA on 5,306 traces cuts it 76.0%; Claude 3.5 Haiku 52.5%, Sonnet 4 41.4% | b19, d12 | E (K12) |
| Reasoning models: small or negative blind spot | DeepSeek-V3-0324 0.567 to 0.902 with Wait; R1-0528 0.908 | d12, d13 | S (K27) |
| Explanation quality bounds repair | APPS, GPT-4 own feedback 33.30% vs human 52.60%; competition 3.67% vs 14.67%; interview 19.33% vs 45.67%; introductory 42.64% vs 62.21% | a24 | S (K13) |
| Negative training data: quality decides | +8.74 (high-quality negatives, 7B, 2k positives) vs -3.16 (low-quality); 13B with 5k positives +0.52; action error 4.01% vs 15.33% | a26, b20 | E (K14) |
| LEMA correction data | LLaMA-2-70B GSM8K 83.5 vs 81.4; MATH 25.0 vs 23.6 (29.3 with correction-centric evolution); CSQA 85.3 vs 84.2; equal-size gain holds for 4 of 5 models, not LLaMA-2-7B | a27, b22, c11 | E (K14) |
| Step-level failure attribution (AgentDebug) | all-correct 24.3% vs 0.3%; step accuracy 45.0 vs 28.0; ALFWorld GPT-4o-mini 21 to 55, Qwen3-8B 48 to 74, Qwen3-Next-80B 60 to 84; up to 26% relative | a28, b23, c17, d16 | S (K15) |
| Clustered mistake notes | KaggleDBQA 24.0 to 64.0 with 514 tokens vs ACE 54.0 with 9406 tokens; Qwen3-8B 19.0 to 28.0; Qwen3-Max 40.0 to 46.0 | a30 | S (K16) |
| Reflection fails when cause is exploration or missing knowledge | Reflexion@5 = re-execute@5 on Android cross-app; count-based hint +27% on Camera app; hindsight about 4 points below exploration-only on HotpotQA (GPT-3.5) | c13, c14 | C (K17) |
| Trajectory-informed tips | AppWorld test-normal task goal 73.2 vs 69.6; scenario goal 64.3 vs 50.0; top-3 restriction fell to 66.7/48.2; tips hurt tasks at 100% baseline (to 94.4%) | a29 | S (not re-verified) |
| Memory pollution | Add-all or weak evaluator: flat or declining; strict selective add kept improving and passed error-free memory after about 2000 executions (AgentDriver). AWM online workflows can degrade | b13, b14, b15, d08 | E (K18) |
| LLM consolidation erodes memory | GPT-5.4 failed 54% of ARC-AGI problems it solved with no memory; raw trajectories hold up better than AWM-distilled | d07 | S (K18, K25) |
| Equal-token: reflect-and-retry loses to resampling (small models) | 7 methods, 1.5B/3B/7B, 36 paired comparisons: 0 beat self-consistency, 10 worse, 26 tied (Holm); Self-Refine and forced Reflexion 3.6 to 10.1 points below self-consistency at 7B; code self-repair loses 6.1 points at 1.5B (p=0.006), ties at 7B with 2.5x to 5.5x more tokens | d01, d02 | S (K21) |
| Anchoring on own failed attempt | near-identical retry in 33-68% of retries vs 2-14% blind; execution feedback adds nothing beyond "wrong"; retrieved solutions to other tasks within 3.5 points | d02 | S (K22) |
| Richer reflection beats thin one (with oracle flag) | GPT-4 on previously wrong items: baseline 0.786, retry 0.827, keywords 0.832, advice 0.840, instructions 0.849, explanation 0.876, solution 0.925, composite 0.932, answer leaked 0.971; GPT-3.5 0.596, retry 0.686, explanation 0.802, solution 0.831 | d03 | S (K23) |
| Failure guards vs governance | MemGuard Qwen-3.5-Plus full 67.4/83.6/58.4/51.8; without failure memories 66.1/82.2/56.5/50.7 (drops 1.1 to 1.9); without governance 63.7/79.8/52.0/46.8 (drops 4 to 7) | d09 | S (K24) |
| Failure-only vs success-only vs hybrid | HotpotQA Qwen2.5-7B: 51.60 / 50.80 / 52.40 (std 0.45 to 1.12; within noise) | d05 | S (K24) |
| K inverted U | U-Mem K=1 50.20, K=3 52.40, K=5 50.80, K=10 48.80; pool 0 to 1000 tasks 37.80 to 52.40 | d06 | S (K25) |
| Verifier accuracy | MemGuard verifier 86% and 83% agreement with inspection; 88.1% balanced accuracy; 9.3% false positives; governance blocks 38 of 60 false accepts | d10 | S (K10) |
| Replay of reflections (VRL-Bench) | ALFWorld full replay 76.1% at trial 3, partial replay 81.3%, none 74.6%; each method beats memory-free retry in some settings and loses in others; an explore/exploit scheduler was positive in all 6 settings | d04 | S (K17) |
| Double feedback is not monotone | double beat single in 3 trials, lost in 6 (not significant); 687 questions | c22 | S (K19) |
| Learned reflection writer | Retroformer HotPotQA +18%, AlfWorld +36%, WebShop +4%; Reflect-Retry-Reward up to +34.7% Countdown, +18.1% APIGen | c23, b21 | S (K20), training |
| No modern CHEF replication found | ICCBR 2025 and CBR-LLM workshop: nothing measures failure-indexed retrieval | d18 (snippets) | S (K28) |

## 4. Mechanisms and models

### 4.1 CHEF as a pipeline an engineer could build
1. **Input**: goal set G (features of the task, in a fixed vocabulary).
2. **Anticipate**: look up failure memories whose index features are all in G. For each hit, add the goal "avoid failure F" to G. CHEF does this before planning.
3. **Retrieve and modify**: take the closest plan that satisfies the goals including the added avoid-goals. Adapt it.
4. **Simulate or test**: run the plan against a checker.
5. **On failure, explain**: build a causal chain from the failed state back to the steps. Classify the chain into a failure type (CHEF's TOP).
6. **Repair**: each failure type holds a short list of repair strategies. Try them in order; keep the first that passes the check.
7. **Credit assignment**: from the chain, pick only the input features on the causal path. These become the index of the new failure memory. Generalise them (beef to meat, broccoli to crisp vegetable).
8. **Store**: write the failure memory (index features -> warning + cause), and store the repaired plan under goals met and problems avoided.

What makes it work: a **feature vocabulary** for traps, a **causal explainer**, and a **small library of repair strategies per failure type**. In 1986 all three were hand-built. With an LLM the vocabulary and explainer can be written by the model, but nobody has measured whether that works.

### 4.2 Riesbeck's exception store
Rule R stays. Each failure of R stores an episode E = (input, expected, actual, fix). On a new failure of R, retrieve episodes and show them. If the retrieved episodes share a feature, promote it to a new rule or a rule split. Cheap: a per-rule list with a promote step.

### 4.3 Reflexion loop
```
for trial in 1..T:
    attempt = actor(task, memory[-3:])
    signal = evaluator(attempt)        # test, env reward, or LLM judge
    if signal.pass: break
    memory.append(reflector(task, attempt, signal))
```
Needs a repeatable task, a signal, and a window of 1 to 3 reflections. It fails or hurts if the signal is unreliable (false-positive tests 16.3%), if the reflection is a wrong diagnosis (0 of 121 right), or if the real cause is missing exploration (WebShop).

### 4.4 ExpeL insight list
Collect success and failure trajectories on training tasks. For tasks with both, ask a strong model to compare the pair and emit operations ADD, EDIT, UPVOTE, DOWNVOTE on a global insight list. At test time put the list in the prompt and retrieve similar successful trajectories by task similarity. Use the strong model for extraction (gpt-4 39.0 vs gpt-3.5 32.0 on HotpotQA). Do not feed raw reflections into the extractor (29.0).

### 4.5 ReasoningBank item format
Each trajectory yields at most 3 items of (title, description, content). A judge labels success or failure; failure items are written as preventive lessons. Retrieval is by embedding. Memory-aware test-time scaling (MaTTS) contrasts parallel attempts to get better items. The judge was 72.7% accurate on Shopping and performance was flat from 70 to 90% simulated accuracy.

### 4.6 Governance (MemGuard and Xiong)
Write path: admission (a verifier must accept), dedupe, staleness, conflict resolution, and a cap of at most 2 failure guards next to up to 5 positive records. Delete path: periodic deletion plus history-based deletion (drop records whose later use gave poor results). Governance is worth 4 to 7 points; the separate failure channel 1 to 2 points. Deletion helps only if the utility evaluator is reliable.

### 4.7 ConMem firing rule
A negative card fires only if expected avoided loss exceeds false-suppression loss plus context cost. The claims file writes the test as p > (G+c)/(L+G), with p the probability the card applies, G the gain from avoiding the trap, L the loss from wrongly suppressing a good move, c the context cost. Use it to decide whether a warning is shown at all. Failure-ablation sizes were only in charts, so the benefit is not quantified.

### 4.8 AgentDebug
Annotate each failed trajectory by module (memory, reflection, planning, action, system) and find the earliest root-cause step, because early errors cascade. Feed back targeted feedback about that step and retry. Root-cause finding is still weak (24.3% all-correct) and small models do it badly.

### 4.9 Mistake Notebook Learning
Cluster failures in a batch, write a shared note per cluster, apply the memory update only if batch accuracy improves, otherwise roll back. The accept-if-better gate is the useful part. It matches SCHEMA section 5 ("trusted only after it helps on two different problems").

## 5. What holds up

### 5.1 Established (two or more independent sources)
- **Intrinsic self-correction without an external signal does not help and often hurts** (Huang, Kamoi, Li, Tsui, Olausson; K11). Gains in earlier work were inflated by oracle labels. Reasoning models partly change this (small or negative blind spot) but add little (CorrectBench).
- **Finding the error is the weak step; fixing it once located works** (Tyen 52.87% location; fix 23.53% vs break 11.11%; Tsui 64.5% blind spot; Olausson 33.30% self vs 52.60% human feedback; K12, K13).
- **Retrieval quality and small memory size matter** (ExpeL 59.0 vs 42.5 random; Memento K=4; U-Mem K=3; Xiong strict capped memory; K08, K25).
- **Unverified writes pollute memory** (Xiong, AWM, ReasoningBank baselines, Zhang; K18).
- **Negative training examples help only when high quality and tagged** (Wang; LEMA; K14).

### 5.2 Single-source or contested
- Reflexion's headline gains are real inside its setup (outcome signal, small samples) and contested elsewhere. Xing found no gain over plain re-execution; Li found a 4-point loss on HotpotQA; VRL-Bench found mixed results; Kamoi flagged Reflexion's HotpotQA setup as unfair (exact-match feedback). Plausible resolution: reflection helps when the failure is an understandable execution error with a reliable signal, and not when the cause is exploration or missing knowledge. Status contested (K17).
- ExpeL: insights vs raw cases is task-dependent (HotpotQA insights win 36 vs 31, ALFWorld raw wins 55 vs 50).
- Failure memory beats success memory by 0.8 points (U-Mem) and a failure channel adds 1 to 2 points (MemGuard). Both small.

### 5.3 Failures and null results
- WebShop: no gain after 4 trials (Reflexion).
- Frozen wrong diagnoses: 0 of 121.
- Hallucination loop 22%.
- Insights built from raw reflections: 29.0 vs 39.0 (ExpeL).
- AWM with failures added: 44.4 to 42.2.
- Tips hurt tasks already at 100% (94.4%, a29).
- Reflection at equal tokens loses to resampling at 1.5B to 7B (Mirzaei, Verma).
- Showing a model its own failed code makes it anchor: 33-68% near-identical retries.

### 5.4 Moderators
- **Signal quality**: external test or env reward helps; self-judge is risky. Specific feedback (unit tests) yields less freezing than binary pass/fail (Dixit).
- **Failure cause**: execution error helps; exploration or knowledge gap does not.
- **Base accuracy**: reflection helps most when first answers are mostly wrong and the question is hard; it harms when half or more are right (Li).
- **Model size and type**: small models (1.5B-7B) lose to resampling; non-reasoning models have a large blind spot; reasoning models a small one.
- **Memory size and granularity**: inverted U in K; raw episodes beat consolidated lessons over time.
- **Explanation author**: a stronger model or human explanation beats self-explanation.

### 5.5 Interventions
Worked: quote the trace step (object mention 0 to 86%); governance (4 to 7 points); small K; accept-if-better gate; Wait trigger on non-reasoning models (0.567 to 0.902); step-level root-cause feedback; clustering failures into short notes (514 tokens). Did not work or unproven: giving reflections to the insight extractor; adding failures to success-only memory designs; double feedback; replaying all reflections (VRL-Bench full vs partial replay).

## 6. Language models

**How they behave.** Without an outside signal, LLMs revise correct answers into wrong ones about as often as the reverse (GPT-3.5 CSQA 75.8 to 41.8). With a reliable outcome signal, a written reflection plus retry raises success on repeatable tasks (Reflexion +22 ALFWorld, +20 HotPotQA; AgentDebug ALFWorld 21 to 55 for GPT-4o-mini). Models self-diagnose badly: they find the first error in only 52.87% of cases (GPT-4), and in the frozen-environment logs they named the true blocking object 0 of 121 times. They anchor on their own previous failure.

**What changed it, by how much.**
- External or oracle signal: GPT-3.5 GSM8K 75.9 to 84.3; GPT-4 HotpotQA 49.0 to 59.0.
- Better explainer: human feedback 52.60% vs self 33.30% (APPS).
- Informative reflection: GPT-4 0.827 (bare retry) to 0.925 (solution), with an oracle wrong-flag; 0.971 when the answer leaked.
- Parsed trace facts instead of free diagnosis: object mention 0 to 86%.
- Root-cause step feedback: ALFWorld Qwen3-8B 48 to 74.
- Distilled strategy items with failures: WebArena +4.6 to +8.3.
- Compact clustered notes: KaggleDBQA 24.0 to 64.0 at 514 tokens.
- "Wait" appended: blind spot -89.3% on non-reasoning models.
- Governance +4 to +7 points; failure-guard channel +1 to +2.

**Scale and era caveats.** Most positive results use GPT-3.5 or GPT-4-class models (2023). Equal-token tests (Mirzaei, Verma) use 1.5B to 7B open models and show reflection loses to resampling. Frontier models are untested at equal tokens. Reasoning models show a small blind spot; extra correction loops give marginal gains. For Claude, Tsui reports blind spots of 52.5% (3.5 Haiku) and 41.4% (Sonnet 4) on synthetic injected errors.

**Cost.** Almost no study matches tokens. Reflexion retries are extra samples. Only Mistake Notebook Learning (514 vs 9406 tokens) and LEMA's equal-size ablation report cost.

**CHEF-style indexing on LLMs.** Not measured. The nearest analogues (ConMem signed cards, MemGuard failure guards) were ablated only as bundled components.

## 7. What our agent should take

Tags: schema part G / S / O / memory. Status [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Gate memory writes on a verified outcome (memory, G).** Do not store a lesson from an unverified failure or success. [E] K18, K11. Evidence b13, b14, b15, d08, d07, a25, b16.
2. **Revise only when a check or outside signal marks the failure (G2; restate for lessons).** No self-revision without a signal. [E] K11. Evidence a25, b16, b17, d14, b19.
3. **Give the revision step the located error, not a request to find it (S5, O-verify).** Code, not the model, locates the failing output. [E] K12. Evidence b18, b19, a24.
4. **Keep the lesson store small and selected by task similarity (memory).** Few lessons per attempt, ranked by similarity of the task, not by reasoning similarity. [E] K08. Evidence b08, a23, c09, b14, b15. The exact K is [S]; see Test first.
5. **Quality-filter stored lessons (memory).** Only lessons from verified failures with a causal explanation tied to a trace step. [E] K14, K18. Evidence a26, b20, a27, b22.

### Test first (single-source or contested)
6. **CHEF-style lesson entry (memory).** Entry = trigger features + cause + repair, indexed by abstract conditions, not topic. [S] K01, K28. Evidence a01-a05, b24. Never measured on LLMs.
7. **Quote-the-trace rule (G, O-reflect).** Each lesson must quote the trace step that supports it. [S] K06. Evidence c15, c16.
8. **Warnings vs recipes (memory).** Cap warnings at 2, label with trigger, show after the first attempt (already in SCHEMA section 5). [S] K24. Evidence d09, d05, d11.
9. **Equal-token resample arm (G7, O-retry).** Always compare reflect-and-retry with plain resampling. [S] K21, K22. Evidence d01, d02.
10. **Failure-type router (S6, O-explore vs O-reflect).** Classify as execution, knowledge, exploration or bad plan before choosing. [C] K17, K15. Evidence c13, c14, d04, a28.
11. **Wait trigger (G, S8).** Forced re-check after a failed check, on non-reasoning bases. [S] K27. Evidence b19, d12, d13.
12. **Governance and expiry (memory).** Dedupe, staleness, conflict, admission; periodic plus history-based deletion. [S] K24, K26. Evidence d09, d08, d05.
13. **Clustered short notes (memory).** [S] K16. Evidence a30.
14. **Accept-if-better gate on memory updates (memory).** [S] K16 (a30); schema section 5 already requires two problems.
15. **Raw episodes vs consolidated lessons (memory).** [S] K25. Evidence d07, b07.
16. **Strong-model lesson writer (memory).** Lessons written by a stronger model beat self-written. [S] K13. Evidence a24, b07 (gpt-4 extractor 39.0 vs 32.0).
17. **Provenance on every lesson (memory).** Store trace id, the outcome check used, count of uses and wins. [S] a29, d09.

Not to add: reflection-fed insight extraction (ExpeL 29.0 vs 39.0); free-form self-diagnosis without a trace quote; full reflection replay; double feedback; training a reflection writer (needs training; K20).

## 8. Concrete tests on our bench

All arms at equal total tokens (count lesson-writing and retry calls). Report paired differences with a confidence interval. Log whether a lesson fired on a non-matching task.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Held-out trap families: several items per family sharing a hidden trap, different surface topic (ARC-style and BrainTeaser-style items) | (a) no lesson, (b) plain "what went wrong" note, (c) CHEF-style entry: trigger features + cause + repair, (d) equal-token resample only | pass rate on later items of the same family; false-fire rate on other families | (c) > (b) by 3 to 8 points if the claim holds; (d) may tie (b) |
| T2 | Same items; lessons by free reflection vs forced trace quote | free vs quote | lesson names the true cause (rate); downstream pass rate; repeated-lesson ratio | quote raises correct-cause rate sharply; downstream gain 2 to 5 points |
| T3 | Items with a reliable check vs items with only a self-judge | reflect-retry vs best-of-N vs resample | pass rate; per-item flips right-to-wrong and wrong-to-right | reflect-retry wins only with the check; loses or ties with self-judge |
| T4 | Mixed failure types (execution slip, missing knowledge, needs exploration) | always reflect vs always explore vs type router | pass rate by failure type | router beats both by 2 to 5 points overall |
| T5 | Stream of 100+ items; inject 20-30% wrong lessons | add-all vs verified-only vs governance + expiry | pass rate over time | add-all drifts down; governed store gains |
| T6 | Same stream | K in {2, 4, 8} x {raw episodes, insights, clusters} | pass rate; prompt tokens | inverted U; K about 3 to 4 best |
| T7 | Items our scaffold fails at S4 | warning only vs recipe only vs both vs none | pass rate; false suppression on non-matching items | both about equal to warning-only; warnings must pass the ConMem firing rule |
| T8 | Non-reasoning base and reasoning base | with and without a Wait-style forced re-check after a failed check | fixed vs broken answers | gain on non-reasoning base, none on reasoning base |
| T9 | Judge-accuracy sweep | simulated outcome-judge accuracy 100/90/80/70/60% | lesson-store gain over no memory | break-even around 70% (not yet found) |
| T10 | Lesson author | self-written vs stronger-model-written lessons | downstream pass rate | stronger writer +3 to +10 points (Olausson gap) |

## 9. What does not transfer, and why

- **CHEF's hand-built world.** Cooking with a simulator and hand-written causal rules. Our tasks have no complete simulator; the causal explanation must come from the model, which explains its own failures badly.
- **Reflexion's repeated trials.** They need the same task again with a trustworthy signal. Many of our items are one-shot and our checks are partial (G3).
- **Retry with the failed attempt in view.** Anchoring (33-68% near-identical retries) conflicts with S3's fresh-context attempts. Lessons should state the trap, not replay the failed output.
- **Training-time results** (negative-aware tuning, LEMA, Retroformer, Reflect-Retry-Reward). We do not train.
- **Long-horizon agent benchmarks** (WebArena, ALFWorld). Some gain comes from memory of site layouts and tool use; our tasks are reasoning puzzles.
- **Small-model equal-token results** (1.5B-7B). They may not hold for frontier models, so they argue for always having the resample arm, not for dropping lessons.
- **Trust and safety findings** (d15) concern memory misevolution, not accuracy.
- **Classical claims.** No quantitative test exists for the founding work, so its effect size is unknown.

## 10. Open questions

1. Does a lesson with trigger features, cause and repair beat a plain reflection at equal tokens on held-out trap families? Never measured.
2. Do trap warnings transfer better or worse than recipes, and how often do they fire wrongly?
3. At what judge accuracy does a lesson store start to hurt, especially with confabulated rather than random-flip noise?
4. How does reflect-and-retry compare with best-of-N on frontier models with external signals?
5. Can a cheap classifier route failures to reflect vs explore?
6. Joint sweep of lesson granularity and K.
7. Do the 2023 negatives hold on 2025-2026 reasoning models with natural errors?
8. Does the quote-the-trace rule help outside ALFWorld and HumanEval?
9. Which expiry rule is best at equal memory size for failure lessons?
10. Is there any independent modern replication of failure-indexed retrieval (ICCBR 2020-2026)? Snippets only.
11. Can an LLM write the feature vocabulary and causal explainer that CHEF needed by hand?

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Hammond (1986) CHEF: A Model of Case-based Planning. https://cdn.aaai.org/AAAI/1986/AAAI86-044.pdf (a01-a05)
- [V] Hammond (1986) AAAI abstract page. https://aaai.org/?p=41593 (c19)
- [V] Hammond (1987) Explaining and repairing plans that fail, IJCAI-87, abstract. https://mlanthology.org/ijcai/1987/hammond1987ijcai-explaining (b25)
- [V] Davies summary of Hammond (1989/1990). https://www.jimdavies.org/summaries/hammond1989a.html (b24, c18)
- [M] Hammond (1986) Yale thesis (DTIC ADA180271). https://apps.dtic.mil/sti/pdfs/ADA180271.pdf (a11)
- [M] Hammond (1990) Explaining and repairing plans that fail, Artificial Intelligence (a12, c20)
- [V] Riesbeck (1981) Failure-driven reminding for incremental learning. https://ijcai.org/Proceedings/81-1/Papers/024.pdf (a06, a07)
- [M] Schank (1982) Dynamic Memory. https://www.cambridge.org/core/books/dynamic-memory/ (a08, c21)
- [M] Schank and Leake (1989) Creativity and learning in a case-based explainer. https://www.datalearner.com/academic/journal-papers/0004-3702/volumes-and-issues/110/paper-detail/376 ; https://folk.idi.ntnu.no/agnar/CBR%20papers/Schank-Leake-89.pdf (a09, c21)
- [V] Leake, SWALE project page. https://homes.luddy.indiana.edu/leake/projects/swale (a10)
- [M] Kolodner (1993) Case-Based Reasoning. https://shop.elsevier.com/books/case-based-reasoning/kolodner/978-1-55860-237-3 (a13)
- [V] Riesbeck and Schank, micro CHEF page. https://www.entish.org/deeptext/posts/chef/ (a14)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (a15-a18, b01-b05, c01-c03)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (a19, a20, b06-b08, c04, c05)
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/abs/2509.25140 (a21, a22, b09-b11, c06-c08)
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (a23, c09)
- [V] Olausson et al. (2024) Is self-repair a silver bullet. https://arxiv.org/abs/2306.09896 (a24)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a25, b16, c12)
- [V] Wang et al. (2024) Negative-aware training. https://arxiv.org/abs/2402.11651 (a26, b20)
- [V] An et al. (2024) LEMA. https://arxiv.org/abs/2310.20689 (a27, b22, c11)
- [V] Zhu et al. (2025) AgentDebug / AgentErrorBench. https://arxiv.org/abs/2509.25370 (a28, b23, c17, c25, d16)
- [V] Fang et al. (2026) Trajectory-informed memory generation. https://arxiv.org/abs/2603.10600 (a29; not re-verified)
- [V] Su et al. (2026) Mistake Notebook Learning. https://arxiv.org/abs/2512.11485 (a30)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (b12, b13, c10)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (b14, b15, d08)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes. https://arxiv.org/abs/2406.01297 (b17, d14)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (b18)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (b19, d12)
- [V] Bensal et al. (2025) Reflect, Retry, Reward. https://arxiv.org/abs/2505.24726 (b21)
- [V] Li, Yang and Ettinger (2024) When hindsight is not 20/20. https://arxiv.org/abs/2404.09129 (c13)
- [V] Xing et al. (2024) Understanding the weakness of LLM agents within a complex Android environment. https://arxiv.org/abs/2402.06596 (c14); [M] d17 was a snippet of the same paper
- [V] Dixit, Kamal and Oates (2026) Honest lying. https://arxiv.org/abs/2605.29463 (c15, c16)
- [V] Yin and Leake (2026) Capturing LLM cases for RAG reuse. https://ceur-ws.org/Vol-4255/lake.pdf (c22; not re-verified)
- [V] Wang et al. (2023) Retroformer. https://arxiv.org/abs/2308.02151 (c23)
- [V] Hatalis et al. (2025) Review of CBR for LLM agents. https://arxiv.org/abs/2504.06943 (c24); [M] d18 searched ICCBR and CBR-LLM listings
- [V] Mirzaei (2026) Sample More, Reflect Less. https://arxiv.org/abs/2607.28576 (d01)
- [V] Verma (2026) Try Again, Don't Look Back. https://arxiv.org/abs/2607.26117 (d02)
- [V] Renze and Guven (2024) Self-Reflection in LLM Agents. https://arxiv.org/abs/2405.06682 (d03)
- [V] VRL-Bench (2026). https://arxiv.org/abs/2609.12404 (d04)
- [V] Wu et al. (2026) U-Mem. https://arxiv.org/abs/2602.22406 (d05, d06)
- [V] Zhang et al. (2026) Useful Memories Become Faulty When Continuously Updated. https://arxiv.org/abs/2605.12978 (d07)
- [V] Wang et al. (2026) MemGuard. https://arxiv.org/abs/2608.21867 (d09, d10)
- [V] ConMem (2026). https://arxiv.org/abs/2606.08702 (d11)
- [V] Zhang et al. (2025) CorrectBench. https://arxiv.org/abs/2510.16062 (d13)
- [V] Cheng et al. (2026) TAME / Trust-Memevo (abstract and introduction only). https://arxiv.org/abs/2602.03224 (d15)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C08.10-K18** (number corrected). Zhang et al.'s abstract says GPT-5.4 'fails on 54%' but the body (intro and results) says accuracy fell from 100% to 54% on a 19-problem slice, i.e. it failed on 46%; the claim repeats the abstract's misstatement. Corrected claim: Memory pollution and drift: online AWM workflows from unverified trajectories can degrade results, and add-all memory with a weak evaluator is flat or declining. Gap search: LLM consolidation itself erodes memory (GPT-5.4 dropped from 100% to 54% accuracy, i.e. failed 46% of a 19-problem ARC-AGI slice it solved without memory), and history-based deletion with a reliable evaluator helps.
