# The 4R cycle: deep document

*Subfield C08.01. Retrieve, reuse, revise, retain. Built from evidence_a-d.jsonl, claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids (a01, b12, c05, d03 ...) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The 4R cycle is a four-step loop for solving a problem from past experience.

1. **Retrieve** the most similar past case or cases.
2. **Reuse** what they contain to build a solution for the new problem.
3. **Revise** the proposed solution: test it, and repair it if it fails.
4. **Retain** the useful parts of the new experience in the case base.

Aamodt and Plaza (1994) gave it as a general framework, not as a tested model (a01). Their paper has no experiments. It describes older systems (CHEF, CASEY, PROTOS, CREEK). A case is a rich record: problem, solution, and often the reasoning, the outcome and the reason for failure (a10).

The key claim is that learning is a by-product of solving. Each solved or failed problem is kept, so the system gets better with use (a02).

Why it matters for our agent:
- It is the closest classical match to a memory for a language-model agent: a library of solved subgoals offered by similarity, with a rule for what to keep.
- Retrieve, reuse and revise map onto states we already have (S0/S2 lookup, S3 generate, S4/S5 test and revise).
- **Retain** is the part a single-run schema lacks. It only matters across tasks. It is also the part with the most traps (bad cases spread, banks grow, judges are noisy).

What the evidence says in one paragraph. Putting a few verified, similar cases in the prompt helps modern agents by about 4 to 19 points on agentic tasks (K01). Gains are smaller than the gain from scaffolding or planning (K03). One to four cases is enough (K02). Keeping everything is worse than keeping selectively (K05), and the judge that decides what to keep is the weak point (K06). Retrieved cases can hurt, mostly on hard items (K29). The explain-the-failure revise step does not beat plain resampling at equal tokens unless the failure signal comes from outside the model (K27). No paper has yet compared a case library with an empty-library scaffold at equal total tokens (K26).

## 2. History and theories in depth

### 2.1 Roots in cognitive science (1977-1989)

- Schank and Abelson (1977) built story understanding on scripts. Schank (1982) proposed **dynamic memory**: Memory Organization Packets (MOPs) that hold generalized episodes and give remindings that can cross contexts. When expectations fail, the system recalls a prior explanation (SWALE). (a12)
- Human-side citations in Aamodt and Plaza: Ross 1989 (specific past situations drive reasoning), Anderson 1983 (people use past cases as models early in learning), Rouse via Kolodner 1985 (experts rely on past cases). No effect sizes are given (a03). The 4R cycle is an engineering framework with a psychological motivation. It is not proven human cognition.
- Gick and Holyoak's radiation-problem work set the human baseline for spontaneous analogue reuse: about 10% unaided (b35). See section 5.4.

### 2.2 The classical memory models (1980s)

Aamodt and Plaza describe two (a06):
- **Dynamic memory (Schank, Kolodner)**: a discrimination network of generalized episodes (norms) with indices. A new case is pushed down the network. Shared parts of two cases form a new generalized episode. Index count can explode, so CYRUS allows only a small index vocabulary.
- **Category-exemplar (Bareiss, Porter, PROTOS)**: categories, with exemplars ranked by prototypicality, linked by feature, case and difference links.

### 2.3 Instance-based learning and nearest neighbour (1967-1991)

- Cover and Hart (1967): in the large-sample limit, the 1-nearest-neighbour error is at most twice the Bayes error (R* <= R <= 2R*(1-R*)). This is the formal reason that reusing the closest past case can work. It holds only when cases are dense, labels are reliable, and similar problems have similar answers (a19).
- Aha, Kibler and Albert (1991): IB1 stores everything. IB2 stores only what it got wrong. IB3 adds a per-case pass/fail record with a significance test. (a17, a18, b37, b38). This is the first controlled evidence on **what to retain**.

### 2.4 The Aamodt and Plaza task-method decomposition (1994)

(a05, a07-a11)
- **Retrieve** = identify features, initially match, search, select. Two-stage matching: cheap candidate set, then a costlier select that builds explanations. Knowledge-poor (surface) vs knowledge-intensive (explanation-based) retrieval.
- **Reuse** = copy or adapt. Two forms: *transformational* (apply operators to the old solution) and *derivational* (replay the old method, including subgoals and failed paths).
- **Revise** = evaluate (real world, teacher, or simulation) then repair (explain the failure, then modify). CHEF did this with an internal causal model and learned failure situations by explanation-based learning. Unevaluated cases may be stored but must be marked.
- **Retain** = extract (problem, solution, justification, trace, failures), index, integrate (adjust index strengths by success or failure). Indexing is called "a central and much focused problem".
- The partitions are claimed complete; control over subtasks is left open. The paper says it is usually easier to retain a concrete experience than to generalize from it (c25).

### 2.5 The utility problem and maintenance (1990-2005)

- Minton (1990) showed in explanation-based learning that learned speed-up rules can slow a system down. Smyth and Cunningham (1996) carried this to CBR: retrieval time grows with case-base size while adaptation savings per new case shrink, so past a critical size efficiency falls (a14).
- The early view that every episode should be kept proved naive (c02). Maintenance became a field: Hart's condensed NN (1968) removes redundancy; Wilson's edited NN (1972) removes noise (a15). Smyth and Keane (1995) ranked cases by competence (coverage) and deleted the least critical first (b06). Wilson and Leake (2001) split maintenance policy into data gathering, triggering and operations (a16).
- Adaptation-guided retrieval (Smyth and Keane 1994-98): the most similar case may be impossible to adapt; score adaptability during retrieval. "Effective retrieval is not simply a matter of finding cases that are similar but cases that are usefully similar" (a13).

### 2.6 The LLM era (2021-2026)

- Prompt-level retrieval: KATE (Liu 2021) showed nearest-neighbour in-context examples beat random ones (b24).
- Agent memory: Reflexion (2023), ExpeL (2023/24), Voyager (2023), Buffer of Thoughts (2024), DS-Agent (2024), Agent Workflow Memory (2024), Dynamic Cheatsheet (2025), Memento (2025, the most explicit 4R mapping), ReasoningBank (2025/26), Agent KB (2025), Evo-Memory (2026), Online Boundary-Aware Memory (2026).
- Critical work: Huang 2023 and Kamoi 2024 on self-correction, Olausson 2024 on self-repair, Kapoor 2024 on cost, Xiong 2025 on memory management, Hu 2026 on cross-task transfer.
- Memento (Definition 3.2 and Algorithm 1) maps the cycle exactly: retrieve = case-selection policy, reuse and revise = the LLM acting on state plus retrieved case, evaluation = environment reward, retain = append (state, action, reward) to the bank (c22). Revise is left to the model.

## 3. Core findings with exact numbers

Status uses the claim status in claims.jsonl: established, single-source, contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Retrieved cases help agents over no memory | Memento +6.7 F1 DeepResearcher; ExpeL ALFWorld 40.0 to 59.0; Sarukkai ALFWorld 73 to 89 (gpt-4o-mini); ReasoningBank WebArena 40.5 to 48.8; AWM WebArena 23.5 to 35.5; Agent KB GAIA pass@3 55.2 to 73.9 | a21, a25, b40, a26, a28, c16 (K01) | [E] |
| Few cases are best | Memento K=0/1/4/8/16/32 F1: 59.9/63.6/64.5/64.1/63.9/63.9. OBAM: 1 case loses 7-8 points, saturates at 5. Bertsch: retrieval edge over random 51.5 points at 1 shot, 4.9 at 1,500 | a22, d02, d10 (K02, K31) | [E] |
| Memory adds less than scaffolding | Memento: CBR +4.5 / +3.7 / +6.7 F1 (HLE/SimpleQA/DeepResearcher); planning without CBR +11.0 / +32.5 / +29.1 F1. Dynamic Cheatsheet: empty scaffold 23.3 to 36.7 on AIME 2024 before any cases | a21, c04, b20 (K03) | [E] |
| Part of the learning curve is not from cases | Memento no-CBR 78.65 to 84.47 over five passes; CBR gap at pass 5 only +0.38 and +0.97 | a23 (K04) | [S] |
| Retain-all is worse than selective retain | Xiong add-all 55.48/13.05/32.32/59.90 vs strict 70.95/38.50/51.00/85.40 (RegAgent/EHRAgent/AgentDriver/CIC-IoT). Fixed memory (67.53/16.75/40.11/71.50) beats add-all on all four | b02, b05 (K05) | [E] |
| Retain filter quality decides the outcome | Judge tuned on 300 trajectories (C3) beat add-all on all four. Same-model judge of graph colouring: accepted 30 of 500, right 5 times (precision about 17%). Self-critique loop 1/100 vs 16% baseline | b02, d11 (K06) | [E] |
| Agents copy retrieved cases, so bad cases spread | Output similarity tracks input similarity (Pearson r near 1 at large memory). Errors in stored cases widen the gap to error-free memory; strict evaluator closes it after about 2000 executions | b01, b03, d14 (K07) | [E] |
| Harm from a retrieved case is concentrated on hard items | Hu: raw memory across tasks -26.1 points on items failed alone (ALFWorld, n=46). Mallen: 10% of PopQA questions turned wrong. DC: GPT-4o MMLU-Pro Eng 53.2 to 44.0. Yoran: random passages cut accuracy over 10 points | d03, d06, d15, d08 (K29) | [E] |
| Deleting low-utility cases can help | EHRAgent 38.67 to 42.06 (memory 1012 to 784); AgentDriver strict 51.00 to 51.81 (1178 to 846); RegAgent combined deletion 70.95 to 66.58 (2938 to 890); noisy judge hurt CIC-IoT 74.00 to 68.80 | b04 as corrected in critique (K08) | [S] |
| Coverage-based deletion beats random | Smyth and Keane, 50 cases: footprint 100% vs random 86% vs utility 80%. Pan 2005: footprint is noise-sensitive | b06, b08 (K09) | [C] |
| Pass/fail record per case fixes noise | Hungarian heart IB1 58.7, IB2 55.9 (36.0% stored), IB3 80.5 (7.5% stored), C4 78.2. At 10% noise 26.3% of IB2's saved cases were noisy | a17, b38 (K10) | [S] |
| Failures help only in the right memory form | Shopping: ReasoningBank 46.5 to 49.7; AWM 44.4 to 42.2; Synapse 40.6 to 41.7 | a27, b18 (K11) | [E] |
| Distilled vs raw cases | WebArena flash: distilled 48.8 vs raw (Synapse) 42.1 vs AWM 44.1 vs none 40.5. Hu: cross-task Insight +6.5 vs Raw -9.5; within task Raw 80.5 vs Insight 65.5 | a26, d03 (K12) | [C] |
| Concrete cases and abstract insights help different tasks | ExpeL gpt-3.5: ALFWorld retrieval-only 55 vs insights-only 50; HotpotQA 31 vs 36; both 59 and 39 | a25, b17 (K13) | [S] |
| Indexing matters | ExpeL ALFWorld: task-similarity 59.0, reasoning-similarity 48.5, random successes 42.5, ReAct 40.0. KATE NQ EM 28.6 random to 40.0-41.6 | b17, c07, b24 (K14) | [E] |
| Human retrieval follows surface similarity | Gentner 1993 recall: surface + first-order 52%, object-only 17%, pure analogy 7%. Reminding ratings 2.36 / 1.48 / 0.86. Recognition picked literal match 82% | b28-b30 (K15) | [E] |
| Human spontaneous reuse is low without help | About 10% unaided; comparing two analogues 71% vs 41% (C&H 1989); delay 65% vs 42%; animation 81% vs verbal 55% (Kubricht 2015, N=126) | b32-b35 (K15) | [E] |
| Part of gain is format and label priming | Min 2022: random labels cost 0-5% (avg 2.6% / 1.7%). MATH500: problems-only matched ground-truth solutions | b25, d13 (K16) | [E] |
| Gains depend on task-stream similarity | Evo-Memory r = 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet). Memento claims +4.7 to +9.6 out of distribution | b39, a24 (K18) | [C] |
| Memory depends on model strength | DC Claude 3.5 Haiku AIME 2025: 13.3 empty scaffold, 10.0 with memory. Mallen adaptive retrieval +5.3 points. OBAM +10.9 on DDXPlus vs +1.9 on CaseHOLD | c13, d06, d02 (K19) | [E] |
| Self-correction without outside signal fails | GPT-3.5 CommonSenseQA 75.8 to 38.1 (Huang). Reflexion HumanEval 91.0 vs 80.1 but MBPP 77.1 vs 80.1; false-positive tests 16.3% (MBPP) vs 1.4% (HumanEval) | b21, b22 (K20) | [E] |
| Explanation helps only if accurate | Repair success: GPT-4 own explanation 33.30% vs human 52.60% (Olausson). Tyen: true location gains 18.04-43.92 on wrong traces; random location 5.16-21.57 | d09, d12 (K27) | [E] |
| False flags have a price | True location: right-answer traces lose 0-11.43; random location: lose 6.67-15.91 (Tyen) | d12 (K28) | [S] |
| Own verified successes can seed the library | Sarukkai ALFWorld 73 to 89, Wordcraft 55 to 64, InterCode-SQL 75 to 79; curated 93. GSM8K self-generated 61 vs retrieved 57 (davinci-003); small models: retrieved wins (curie-001 3 vs 2) | b40, b26 (K21) | [E] |
| Skipping retrieval for easy items pays | Mallen: adaptive retrieval 46.5%, 5.3 points above any non-adaptive method | d06 (K32) | [S] |
| Online retention beat frozen | Re4: +2.75% (DCN), +10.08% (SP) FF1 over CBR+SFT. Naive CBR 64.01 vs SFT 49.46 FF1 | b10, b11 (K23) | [S] |
| Library size past a peak lowers results | MATH500 ground-truth ICL peaks near 125 then falls. DC full-history GPT-4o AIME 2024 6.7 vs 20.0 baseline | d13, d15 (K24) | [E] |
| Case memory can cost tokens with no gain | Stocker 2026: prompt tokens +49% (929k vs 625k) for 0.8147 vs 0.8098 (p=0.11); NOMAD worse (0.0632 vs 0.0608); 4 seeds | d01 (K33) | [S] |
| Complex loops do not beat retry at counted cost | HumanEval: no significant gap between retry baseline and best agent; Reflexion and LDB cost over 50% more; LATS over 50x | d04, d09, d11 (K26) | [E] |
| Template reuse can give very large gains in task families | Buffer of Thoughts Game of 24 GPT-4 3.0 vs 82.4; Checkmate-in-One 36.4 vs 86.4. DC GPT-4o Game of 24 10 to 99 | c19, b20 (K25) | [C] |
| Retrieval-only case use adds little where the model knows the domain | CBR-RAG: 0.8967 to 0.9141 (+1.94%), 32 test cases | a29, b14 (K22) | [E] |
| Models trained on arithmetic behave as case matchers | Llama-2-7B from scratch 30.2% on held-out square vs 92% random split; GPT-3.5 fine-tuned 97.5% on square; rule-following fine-tuning over 95% at 12 digits | a30, b23 (K17) | [S] |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it.

### 4.1 The case record

Store one record per solved or failed problem. Fields:
- `problem`: the task text, plus the class label from S0.
- `index_key`: the text that retrieval matches on. Task-similarity beat reasoning-similarity by 10.5 points on ALFWorld (b17). Choose it on purpose.
- `solution`: the answer, and optionally the path (derivational reuse, a08).
- `outcome`: pass or fail, and **who verified it** (code check, held-out test, none). Mark unverified cases as such (a09).
- `lesson`: one line on the trick or trap. Distilled lessons are safer across tasks (d03).
- `failure_reason`: for failed cases, why (a10). ReasoningBank gains from failures only when they are distilled (a27).
- `meta`: date, model version, usage counts (retrieved, helped, harmed).

### 4.2 Retrieve: two stages

- Stage 1, cheap scan: embedding or BM25 over the index key. MAC/FAC (Gentner) returned about 3.3 items per probe and reproduced the human retrievability order (b31).
- Stage 2, structural fit check: a relational match of the case to the new problem, done by code where possible. Surface similarity is what people and embeddings retrieve, not same-structure cases (b28, b29). Adaptation-guided retrieval (a13) is the same idea: rank by whether the case can be applied.
- k: 1 to 4 (a22, b13). Memento peaks at 4; DS-Agent finds 1 best; Sarukkai uses 6; OBAM saturates at 5.
- Skip rule: do not retrieve when the no-memory pass rate for the class is high (K32, K22). Mallen used entity popularity as proxy.
- Disagreement gate (Agent KB): a retrieved case is a hint, and does not override the agent when they conflict (c16).

### 4.3 Reuse

- Transformational: edit the old solution (needs an operator model).
- Derivational: replay the old path, trying successful steps first and avoiding failed ones; fall back to full search when the replay fails (a08, a11). Store paths with their checked outcome and treat them as hints (G10).
- Show cases after the first attempt, not before, to avoid fixation (SCHEMA section 5). This is a schema choice, not a tested result here.
- The model copies near cases (b01). So the nearest case acts as a template. Put distilled strategy lines in the prompt rather than long raw traces when the case comes from a different task (d03).

### 4.4 Revise

- Evaluate: run the real check. Self-judged revise loses accuracy (b21).
- Repair: show the failing output, locate the fault with code, then fix. Tyen shows models fix well when given the location (gain 18 to 44 points on wrong traces) and find faults poorly (52.87% GPT-4 step accuracy) (d12).
- Cost rule: compare against plain resampling at equal tokens. Stechly found 15 samples with a sound verifier matched every feedback style at about 40% (d11). Olausson found marginal self-repair gains at equal tokens (d09).
- Break-even for a flagging judge: gain on true flags (g) times precision p must exceed loss on false flags (l) times (1-p). With Tyen's ranges (gain 18-44, loss 7-11 for a random location) the break-even precision is roughly 0.2 to 0.4, but this has not been measured for case retention (K28). This is our arithmetic from d12 numbers, not a result from the paper.

### 4.5 Retain: the gate, the probation, the forget rule

1. **Gate by verification.** Keep only cases confirmed by a code check or held-out test. A strict evaluator gave 70.95 vs add-all 55.48 on RegAgent (b02). Aha's IB2 shows that keying on your own errors lets noise in (26.3% of saved cases noisy at 10% noise) (b38).
2. **Probation.** A new case starts on trial. Promote it only after it helps later tasks (IB3 logic: accept if its accuracy interval is significantly above the class frequency; drop if significantly below) (a18). Sarukkai prunes by empirical utility, but the dips at small sizes warn against pruning on few observations (c24).
3. **Redundancy rule.** Skip a new case if a near-identical one exists (condensed NN). Drop a case whose neighbours disagree with its label (edited NN) (c26).
4. **Size cap.** Cap the bank. Memento shows saturation at K=4; DC full-history append is the worst arm (d15). Delete by coverage after correctness is gated, because footprint keeps noisy outliers as pivotal (b08).
5. **Aging.** Stamp cases with date and model version. In changing environments check that the problem-solution regularity still holds (a16). Under task shift, periodic deletion was the more stable (b04, c23).
6. **Re-test.** Re-enter the stored problem as a retention test (a10).

### 4.6 The control loop around the four Rs

Code decides every transition; the model fills slots (SCHEMA section 1). Suggested wiring:
S0 looks up the class record and decides whether to retrieve at all. Retrieval runs after the first attempt. S4 and S5 do revise with real output. S9 does retain: code records outcome, model writes one lesson line, and the case enters on probation.

## 5. What holds up

### 5.1 Replicated or multi-source

- **Retrieved cases help agents** (7+ independent agent papers, K01). But almost all share benchmarks (ALFWorld, WebArena, HotpotQA), so independence is partial (critique).
- **Few cases are enough** (4 sources, K02, K31).
- **Selective retain beats retain-all** (Xiong 2025 plus Aha 1991 plus Smyth and Keane 1995 in direction, K05).
- **Self-correction needs an outside check** (5 sources, K20).
- **Harm from retrieved text** (5 sources, K29).
- **Model strength moderates memory** (3 sources, K19).
- **Part of the gain is priming** (2 sources, K16).

### 5.2 Failed, null or contested results

- **Memento out-of-distribution gain vs Evo-Memory similarity correlation** point in opposite directions (K18). Definitions of similarity and baselines differ. No similarity threshold has been measured.
- **Distilled vs raw** (K12): ReasoningBank says distilled wins. Hu 2026 says only across tasks; within a task raw was better (80.5 vs 65.5).
- **Failures**: ReasoningBank gained 3.2 points from them. AWM lost 2.2. Synapse gained 1.1 (K11). One benchmark, one backbone family.
- **Deletion**: helped on EHRAgent and AgentDriver, hurt on RegAgent combined deletion (-4.4) and CIC-IoT with a noisy judge (-5.2) (K08).
- **Footprint deletion**: perfect in one toy base, sensitive to noise in the follow-up (K09).
- **Reflexion on MBPP Python**: worse than baseline (77.1 vs 80.1). WebShop: no significant gain over ReAct (b22).
- **Combining offline and online AWM workflows**: no gain (44.5) (b19).
- **Workflow actions** were called in only 18.5% of tasks; Mind2Web task success stayed at 1 to 5% (b19).
- **CBR agent on data science** (Stocker 2026): no significant score difference, +49% prompt tokens, NOMAD worse; the reuse check passed all 108 retrievals so it never prevented anything (d01).
- **Reflection-built insights** hurt ExpeL on HotpotQA (29.0 vs 32.0) (c07).
- **Dynamic Cheatsheet** harm: GPT-4o MMLU-Pro Eng 53.2 to 44.0; Claude 3.5 Haiku AIME 2025 no gain over empty scaffold (K19).

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Model strength | Strong models curate and gain; small ones fill memory with flawed strategies | c13, d06 |
| Zero-shot weakness | Gain largest where base is weak (DDXPlus +10.9) and small where strong (CaseHOLD +1.9) | d02 |
| Task similarity | Gain rises with within-stream similarity (r 0.56-0.72); cross-task raw reuse can hurt | b39, d03 |
| Item difficulty | Harm concentrated on items the agent cannot already solve | d03 |
| Existence of a reusable procedure | Huge gains when working code or a template exists (Game of 24); small otherwise | c12, c19 |
| Check quality | Retain, delete and revise all depend on judge precision | b02, b04, d11 |
| Distractor overlap | Topic or role overlap makes irrelevant context worse (in-topic 63.1 vs off-topic 80.7) | d07 |
| Reasoning type | Implicit reasoning QA is where retrieval hurt most | d08 |
| Learner ability (humans) | Animation helped low-Raven people most | b36 |

### 5.4 Human evidence, in detail

- Gentner, Rattermann, Forbus (1993): college students, written recall of old stories from new cues, about one week delay. Quality-of-reminding ratings 2.36 (surface plus first-order matches), 1.48 (true analogies), 0.86 (relations only). Recalled: 52%, 17%, 7%. Analogy had the top soundness rating (4.40 of 5). At recognition the literal match beat the surface-only match 82% of the time. So the structure was encoded, but retrieval did not use it. (b28-b30)
- Catrambone and Holyoak (1989): baseline about 10%. Exp 1: two analogues 71% vs one analogue plus control 41%; comparison group 16% before hint to 53% after. Exp 2: with hint 65% at 30 minutes vs 42% at one week; before hint nothing beat 10%. Schema quality predicted transfer (40% vs 6%; 32% vs 12%; 68% vs 39% hint-aided), but it was correlational with n = 7 to 20 per cell. (b32-b34)
- Kubricht, Lu, Holyoak (2015): 126 participants, 42 per cell. Spontaneous transfer 55% verbal, 50% verbal plus diagram, 81% animation; chi-square 6.60, p = .01. Total after hint 83%, 69%, 90%. (b35)
- Limits: lab stories and puzzles, one lab each, cell sizes not re-read. It concerns people retrieving stories, not an agent retrieving subgoals.

### 5.5 What worked as an intervention

- Retrieve 1 to 4 similar, verified cases (K02).
- Gate retain by a strict or fine-tuned judge (C3: 300 trajectories) (K06).
- Pass/fail record per stored case (IB3: 7.5% stored, 80.5 vs 58.7) (K10).
- Distilled lessons from failures (ReasoningBank) (K11).
- Index by task similarity, not by current reasoning (K14).
- Seed the library from the agent's own verified successes (K21).
- Comparing two cases to build a schema (humans, K15).

### 5.6 What did not work

- Retain everything (K05).
- Retain on a same-model judge (K06).
- Many cases (K02, K31).
- Raw failure traces in success-only memories (K11).
- Self-judged revise (K20).
- Explain-the-failure from the same model at equal tokens (K27).
- Uncurated full history (K24).
- Reflection-built insights in ExpeL (c07).

## 6. Language models

### 6.1 Systems that implement the cycle

| System | What it does for each R | Headline | Honest read |
|---|---|---|---|
| Memento (2025) | Retrieve: SimCSE cosine or learned soft Q. Reuse/revise: planner-executor. Retain: append (state, action, reward) | GAIA val 87.88 Pass@3, test 79.40; DeepResearcher 66.6 F1 / 80.4 PM | Memory adds +3.7 to +6.7 F1; planning adds more; test bank built on validation; K=4 peak (a20-a24, b15, b16, c03-c05) |
| ExpeL (2023/24) | Retain trajectories, extract insights with ADD/UPVOTE/DOWNVOTE/EDIT, retrieve similar successes | ALFWorld 40.0 to 59.0; HotpotQA 28.0 to 39.0; WebShop 0.665 to 0.701 | gpt-3.5, four-fold; transfer HotpotQA to FEVER 63 to 70 (a25, b17, c06, c07) |
| ReasoningBank (2025/26) | Distilled strategies from successes and failures, LLM-judged | WebArena 40.5 to 48.8 (51.8 with scaling); gains +8.3/+7.2/+4.6 across backbones; SWE-Bench-Verified flash 34.2 to 38.8, pro 54.0 to 57.4 | Judge accuracy 72.7%; results held for simulated judge accuracy 70-90%; steps 9.7 to 8.3 (a26, a27, b18, c14, c15) |
| Agent Workflow Memory (2024) | Workflows induced offline or online | WebArena 23.5 to 35.5 (+12.0); gap widens 8.9 to 14.0 as train-test distance grows | Success-only; Mind2Web task success 1-5% (a28, b19, c09, c27) |
| Sarukkai (2025) | Retain own successes, retrieve by cosine | ALFWorld 73 to 89, curated 93 | Five trials differ visibly; first 25% of tasks give most of the gain (b40, c11, c24) |
| Dynamic Cheatsheet (2025) | Self-curated text memory, optional retrieval | AIME 2024 Claude 3.5 Sonnet 23.3 to 50.0; Game of 24 10 to 99 | Empty scaffold already 36.7; harm on MMLU-Pro Eng (b20, c12, c13, d15) |
| DS-Agent (2024) | Case retrieval plus ReviseRank for data science | Deployment one-pass GPT-3.5 85% vs best baseline 56%; cost cut 91.5-92.5% | 30 tasks; one case best (b12, b13) |
| Re4 (2025) | Full 4R with a 7B model, human revise | CBR+Re4 70.11/61.92 FF1 vs naive SFT 49.46/38.71 | One run; stored cases verified by engineers (b10, b11) |
| Agent KB (2025) | Shared cross-framework bank, two-stage retrieval, disagreement gate | GAIA pass@3 55.2 to 73.9; SWE-bench pass@1 24.3 to 28.3 | Abstract and intro only (c16) |
| Buffer of Thoughts (2024) | Meta-buffer of thought templates | Game of 24 3.0 to 82.4 | Repeated template families (c19) |
| OBAM (2026) | Boundary-aware storage, 5 runs | Claude Sonnet 4: DDXPlus 0.753 zero-shot to 0.862 plain case memory to 0.919 OBAM; CaseHOLD 0.788 / 0.807 / 0.825 | Authors' own method; classification with ground-truth labels (d02) |
| CBR-RAG (2024) | Retrieve only, structured cases | 0.8967 to 0.9141 | 32 test cases, embedding cosine as the metric (a29, b14, c17) |
| Stocker (2026) | CBR-augmented R&D agent, Gemma 4 31B | +49% prompt tokens, non-significant | Exploratory, n=4 per cell (d01) |

### 6.2 How models behave

- **They copy.** Output similarity follows input similarity (b01). A wrong stored case misleads the next task.
- **They interpolate cases rather than apply rules.** Small transformers fail inside a held-out region (Llama-2-7B from scratch 30.2% vs 92% random split). Pretrained Llama-2-7B on base-9 addition showed no obvious holes, so this is uncertain for large models. Rule-following fine-tuning fixed it (a30, b23, critique correction).
- **They are primed by format.** Random labels cost 0 to 5%; problems-only prompts matched solutions on MATH500 (b25, d13).
- **They are distracted by relevant-looking text.** In-topic distractors 63.1 vs off-topic 80.7; fewer than 30% of base problems stayed solved across all distractor variants (d07).
- **They cannot judge themselves.** Same-model judge precision about 17% on graph colouring; GPT-3.5 CommonSenseQA 75.8 to 38.1 after self-correction (d11, b21).
- **They fix well when shown the fault.** Wrong traces gain 18.04 to 43.92 points with the true location (d12).
- **Small models gain little from memory.** They fill it with flawed strategies (c13) and cannot know when to skip retrieval (d06).
- **Deliberation hurt.** Memento GAIA validation: deliberative planner 63.03 vs fast 70.91 (b16).

### 6.3 What changed results, by how much

| Change | Size | Evidence |
|---|---|---|
| Any retrieved cases vs none | +4 to +19 points | K01 |
| Adding CBR on top of planning | +3.7 to +6.7 F1 | a21 |
| Fine-tuning the retain judge on 300 trajectories | +11.9 / +21.6 / +15.1 / +19.6 points vs add-all (RegAgent 55.48 to 67.35; EHRAgent 13.05 to 34.66; AgentDriver 32.32 to 47.37; CIC-IoT 59.90 to 79.50) | b02 |
| Strict evaluator vs add-all | +15.5 / +25.5 / +18.7 / +25.5 | b02 |
| Task-similarity index vs random successes | 59.0 vs 42.5 | c07 |
| Distilled vs raw (cross-task) | +6.5 vs -9.5 | d03 |
| Test-time scaling on top of ReasoningBank | 48.8 to 51.8 (best-of-5: 55.1 from 49.7 on a subset) | a26, b18 |
| Curation of Sarukkai's bank | 89 to 93 | c11 |
| Task-family template reuse | up to +83 (Game of 24) | K25 |

### 6.4 What is missing

- No paper compares a case library with an empty-library scaffold at equal total tokens (K26). Memento reports 26k, 48k, 121k tokens per task by level but no no-memory token cost (critique).
- Almost all agent results are single runs. Sarukkai's five trials differ by about 0.06 on InterCode-SQL.
- No paper reports harm per retrieved case.
- No paper tests CHEF-style explain-then-repair with an external check in an LLM.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Revise only from an executable or independent check. Never retain, revise or delete on the model's own judgement. | G2 (already), S5, S9 | [E] | K20, K27; b21, b22, d05, d09, d11, d12 |
| A2 | Retain only cases verified by a code check or held-out test. Store the verifier with the case. | S9, memory | [E] | K05, K06; b02, b05, b38 |
| A3 | Keep the library small and capped; never append raw full history. | memory | [E] | K05, K24; b02, d13, d15 |
| A4 | Retrieve few cases: 1 to 4. | S3, memory | [E] | K02, K31; a22, b13, d02, d10 |
| A5 | Index by task or problem-class similarity, not by the current reasoning text. | memory | [E] | K14; c07, b24 |
| A6 | Log harm and help per retrieved case (retrieved, answer changed, direction). Needed for every later decision. | log (SCHEMA section 6) | [E] as a need; no harm counts exist | K07, K29; d14 |
| A7 | Always run an empty-library arm with the same scaffold and credit memory only for the difference. | G7, bench | [E] | K03, K26; a21, b20 |
| A8 | Treat a retrieved case as a hint, never as proof. | G4, G10 | [E] | K07; b01, c16 |
| A9 | Store failures only as distilled "what went wrong" lines, not raw traces. | S9 | [E] | K11; a27, b18 |
| A10 | Seed the library from the agent's own verified successes before using outside cases (strong models). | memory | [E] | K21; b40, b26 |
| A11 | Skip retrieval for problem classes the model already solves. (The direction is established; the threshold is not, see U5.) | S0 | [E] direction | K19, K22; b14, d02, d06 |

Where these touch the schema now: the current memory section already says lessons are shown after the first attempt, one line each, trusted after helping on two problems, and a class record in code. A2, A3, A6, A9 fit that and could be made explicit. SCHEMA.md changes only under its section 8 rules, and the writer of this document does not edit it.

### Test first

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | Library arm vs empty-library scaffold at equal total tokens | memory | [S]-level (no cost-matched test exists) | K26, K33; d01, d04 | The single most decision-relevant gap |
| T2 | Probation and use-record per case (IB3-style) | S9 | [S] | K10; a17, a18 | 1991 data; LLM version untested |
| T3 | Distilled lesson vs raw solved-subgoal record | memory | [C] | K12; a26, d03 | Direction depends on task distance |
| T4 | Similarity floor: do not reuse below a threshold | S0, memory | [C] | K18, K32; b39, a24, d03 | No threshold is known |
| T5 | Structural check at reuse (relational match, Gentner style) | memory, S3 | [S] | K15, K30; b28, d08 | Could cut harm; may cut recall |
| T6 | Format-matched irrelevant-case control | memory | [E] that priming exists; size for agents unknown | K16; b25, d13 | Separates priming from reuse |
| T7 | Size sweep with distractors | memory | [E] that a peak exists; location unknown | K24, K31 | Sets the cap |
| T8 | Judge precision on our own labels, then break-even | S9 | [S] | K28; d11, d12 | Tells when a model judge may gate retain |
| T9 | Explain-the-failure revise vs retry vs raw failure message | S5 | [S] | K27 | Equal-token test absent |
| T10 | Both a concrete case store and an abstract lesson store, by task type | memory | [S] | K13; a25 | One lab, one model |
| T11 | Coverage-based vs random vs recency deletion with noisy cases | memory | [C] | K09; b06, b08 | Old, small domain |
| T12 | Frozen verified bank vs growing bank on a stream | S9 | [S] | K23, K05; b05, b11 | Frozen is a strong baseline |
| T13 | Derivational reuse: store the path and replay it | S3, O7 | [D] (no LLM test found) | a08, a11 | Untested for LLMs |
| T14 | Compare two cases to build an abstract rule before storing (Catrambone) | S2, S9 | [S] human-only | K15; b32, b34 | Humans only |

## 8. Concrete tests on our bench

All arms at equal total tokens, retrieved text and any judge calls counted. Use at least 5 seeds (Sarukkai's spread is about 0.06) and report the interval. Items: our ARC-like and BRAINTEASER-like suites and the NoveltyBench open items, split into a seed stream, a held-out stream and a shifted stream.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 library vs empty | Held-out items from classes seen in the seed stream | (a) scaffold with an empty library; (b) scaffold with a verified library, k=2; (c) plain model with extra samples to match tokens | Accuracy per 1,000 tokens and pass rate | Library +2 to +6 points over empty scaffold if Memento's size holds; may vanish at equal tokens (Stocker, Kapoor) |
| T2 probation | Task stream of 200 items with 20% mislabelled cases injected | add-on-pass vs add-on-pass with probation and prune | Accuracy, bank size, share of bad cases kept | Probation keeps fewer bad cases; IB3 kept 7.5% with +21.8 points on one noisy set |
| T3 distilled vs raw | Same-class and cross-class items | raw solved-subgoal record vs one-line lesson vs both | Accuracy split by nearest-case similarity | Raw wins within class; lesson wins across classes (Hu) |
| T4 similarity floor | Items binned by similarity to nearest stored case | retrieve always vs retrieve above floor f in {0.5, 0.7, 0.85} | Accuracy per bin, harm rate | Harm in the lowest bin; floor removes it |
| T5 structural check | Items where the nearest embedding case differs in structure | embedding only vs embedding plus code-checked structure match | Harm count, helpful cases dropped | Fewer harmful reuses, some recall loss (Yoran NLI pattern) |
| T6 priming control | Items from classes with a fixed answer format | relevant cases vs format-matched irrelevant cases vs none | Accuracy | If irrelevant matches relevant on more than half the gain, treat the gain as priming |
| T7 size sweep | Streams with 10, 50, 250 stored cases plus distractors | k fixed at 2, token budget fixed | Accuracy vs size | Peak then decline |
| T8 judge precision | 300 labelled pass/fail trajectories | same-model judge vs code check vs fine-tuned small judge | Precision, recall, break-even precision | Same-model judge too low (graph colouring 17%) |
| T9 revise | Items with an executable check | resample vs retry with raw failure message vs retry with explanation | Accuracy at equal tokens | No gain from explanation unless the check is exact (Olausson, Stechly) |
| T10 concrete vs abstract | Reasoning vs action-sequence classes | cases only, lessons only, both | Accuracy by class type | Cases win on action classes, lessons on reasoning (ExpeL) |
| T11 deletion | Bank at fixed cap with noisy cases | random, recency, coverage, use-record deletion | Accuracy at fixed size | Coverage fails with noise; use-record wins |
| T12 frozen vs growing | Shifting stream | frozen verified bank vs add-on-pass | Accuracy over time | Frozen verified is a strong baseline (Xiong) |
| Control for repeat passes | Same items replayed 5 times | memory on vs memory off | Gap by pass | Gap shrinks (Memento +0.38 at pass 5) |

Every run logs the harm count: retrieved case present and answer worse than the paired no-memory run.

## 9. What does not transfer, and why

- **Large case bases with hand-built indices** (CYRUS, PROTOS, MOPs). Our store is small, and the index is the text we match on.
- **Footprint and competence models** need a notion of which problems a case solves. Easy in classification, hard in open-ended tasks; noise-sensitive (a15, b08).
- **Human-subject retrieval results** (Gentner, Catrambone, Kubricht) are for people recalling stories after delay. They justify a structural check; they do not give effect sizes for agents.
- **Competence results on 1991 UCI sets and a 50-case property domain** show direction, not size.
- **The Memento GAIA numbers** are Pass@3 with a bank grown on the validation set. Treat them as upper bounds (a20).
- **Leaderboard-level agent tasks with live environments** have rewards for free. Our open mode has no ground truth; the retain gate has nothing to check against there.
- **Game of 24 and Checkmate-in-One gains** come from repeated task families and stored code; they do not predict gains where items differ (K25).
- **Model-trained-on-arithmetic evidence** (Hu 2024) is about small fine-tuned models. We cannot test it by scaffold (K17).
- **Fine-tuned judges and learned Q-retrieval** (C3 judge, Memento parametric) need training. Our rule is no training. Memento's non-parametric version is within about 0.6 point at iteration 5 (b15).
- **CBR-RAG** only implements Retrieve and its metric is embedding cosine, so it says nothing about revise or retain (a29).
- **Human-written explanations** (Olausson: 52.60% repair) are not available to an agent.
- **Oracle evaluators** (Xiong's strict filter) are not available in real use; the result is a ceiling.

## 10. Open questions

1. At equal total tokens, does a verified case library beat the same scaffold with an empty library, and by how much? (gap 1)
2. What is the break-even library size and k, plotted against distractors? (gap 2)
3. What is the minimum judge precision at which add-selective beats add-nothing? (gap 3, K28)
4. How often does a retrieved case hurt per retrieval, and can a structural check cut it? (gap 4)
5. Is there a similarity threshold below which cases should not be reused? Memento and Evo-Memory disagree in direction. (gap 5)
6. Does a CHEF-style explain-then-repair with an external check beat plain retry at equal tokens? (gap 6)
7. Is distilled better than raw once the distiller is the same model, and how does the answer move with task distance? (gap 7)
8. Do the results hold without an environment check (math, ARC-like)? Dynamic Cheatsheet shows both gains and harm. (gap 8)
9. How much of the gain is format priming? (gap 9)
10. What no-memory success rate should trigger skipping retrieval? (gap 10)
11. Does the anchoring seen in Stocker (generating hypotheses near the retrieved level) show up as lower diversity in open mode? This is a post hoc explanation by one author (d01).
12. Is the Memento learning curve repetition, retries or noise? (a23)
13. CASCADE (arXiv 2605.06702) was not covered by any evidence line. Hatalis 2025 is a review with no numbers.

## 11. Sources

[V] = page or PDF text opened and read this session. [M] = abstract, snippet or second-hand only.

**Founding and review**
1. Aamodt and Plaza (1994) Case-based reasoning: foundational issues, methodological variations, and system approaches. AI Communications 7(1):39-59. https://www.cs.auckland.ac.nz/~ian/CBR/AICom.pdf [V]
2. Lopez de Mantaras et al. (2005) Retrieval, reuse, revision and retention in case-based reasoning. Knowledge Engineering Review 20(3):215-240. https://rgu-repository.worktribe.com/OutputFile/294314 [V]; abstract page https://research.ucc.ie/en/publications/retrieval-reuse-revision-and-retention-in-case-based-reasoning/ [M]; doi:10.1017/S0269888906000646. Smyth and Cunningham 1996, Minton 1990, Hart 1968, Wilson 1972, Bergmann 2001, Wilson and Leake 2001 and Leake and Wilson 1999 are known only through this review [M].
3. Hatalis et al. (2025) Review of case-based reasoning for LLM agents. https://arxiv.org/abs/2504.06943 [V]; no numbers.
4. Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 [V]
5. Kapoor et al. (2024) AI Agents That Matter. https://arxiv.org/abs/2407.01502 [V]

**Classic instance-based and case-base maintenance**
6. Aha, Kibler, Albert (1991) Instance-based learning algorithms. Machine Learning 6:37-66. https://link.springer.com/content/pdf/10.1007/BF00153759.pdf [V]
7. Cover and Hart (1967) Nearest neighbor pattern classification. https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf [V]
8. Smyth and Keane (1995) Remembering to forget. https://folk.idi.ntnu.no/agnar/CBR%20papers/smyth-keane-remembering-95.pdf [V] (numbers not re-opened in the cross-check)
9. Pan, Yang, Pan, Li (2005) Competence driven case-base mining. https://cdn.aaai.org/AAAI/2005/AAAI05-037.pdf [V]

**Human studies**
10. Gentner, Rattermann, Forbus (1993) The roles of similarity in transfer. https://groups.psych.northwestern.edu/gentner/papers/GentnerRattForbus93.pdf [V]
11. Catrambone and Holyoak (1989) Overcoming contextual limitations on problem-solving transfer. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Catrambone_Holyoak1989.pdf [V]
12. Kubricht, Lu, Holyoak (2015) Animation facilitates source understanding and spontaneous analogical transfer. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Kubricht_etal.cogsci.2015.pdf [V]
13. Gick and Holyoak 1980/1983, Ross, Anderson, Schank, Kolodner, Rouse. Cited second-hand only [M].

**LLM agent memory**
14. Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 and https://arxiv.org/html/2508.16153 [V]
15. Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 and https://arxiv.org/html/2308.10144 [V] (Table 3 row labels rest on a garbled extraction)
16. Ouyang et al. (2025/2026) ReasoningBank. https://arxiv.org/abs/2509.25140 and https://arxiv.org/html/2509.25140 [V]
17. Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 [V]
18. Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 [V]
19. Sarukkai et al. (2025) Self-generated in-context examples. https://arxiv.org/abs/2505.00234 [V]
20. Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 [V]
21. Wei et al. (2026) Evo-Memory. https://arxiv.org/pdf/2511.20857 [V] (tables garbled; text claims only)
22. Guo et al. (2024) DS-Agent. https://arxiv.org/html/2402.17453 [V]
23. Re4 (KDD 2025). https://arxiv.org/html/2503.20576v2 [V]
24. Tang et al. (2025) Agent KB. https://arxiv.org/abs/2507.06229 [M] abstract and introduction only
25. Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 [M] abstract and method only, no numbers
26. Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 [V]
27. Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302 [V]
28. Dong and Shang (2026) Online Boundary-Aware Memory (OBAM), ICML 2026. https://cdn.amazon.science/1e/ff/dd26bf194f67bc92b0d772feac1f/scipub-approval152129-48072329-online-boundaryaware-memory-for-casebased-reasoning-agents.pdf [V]
29. Hu, Long, Wang (2026) When continual learning moves to memory. https://arxiv.org/abs/2604.27003 [V]
30. Stocker (2026) Towards persistent case-based memory for autonomous data science. https://arxiv.org/abs/2606.05250 [V]

**Prompting, retrieval and self-correction**
31. Hu, Tang, Yang, Zhang (2024) Case-based or rule-based: how do transformers do the math? https://arxiv.org/abs/2402.17709 and https://arxiv.org/html/2402.17709 [V]
32. Liu et al. (2021) KATE. https://arxiv.org/html/2101.06804 [V]
33. Min et al. (2022) Rethinking the role of demonstrations. https://arxiv.org/html/2202.12837 [V] (not re-opened in the gap pass)
34. Yasunaga et al. (2023) Large language models as analogical reasoners. https://arxiv.org/html/2310.01714 [V]
35. Huang et al. (2023) LLMs cannot self-correct reasoning yet. https://arxiv.org/html/2310.01798v2 [V]
36. Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 and https://arxiv.org/html/2303.11366 [V]
37. Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511 [V]
38. Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 [V]
39. Yoran et al. (2024) Making retrieval-augmented language models robust to irrelevant context. https://arxiv.org/abs/2310.01558 [V]
40. Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896 [V]
41. Bertsch et al. (2025) In-context learning with long-context models. https://arxiv.org/abs/2405.00200 [V]
42. Stechly, Marquez, Kambhampati (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/abs/2310.12397 [V]
43. Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 [V]
44. Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/abs/2404.11018 [V]

**Not found / snippet only:** Wilkerson and Leake "20 to 28 percent" [M]; CASCADE arXiv 2605.06702 [M, no evidence line].

**Corrections applied from critique.md:** AgentDriver strict is 51.00 (memory 1178) and history-based deletion 51.81 (846), a gain of 0.8; the 85.40 vs 89.60 pair is CIC-IoT. The 30.2% figure is Llama-2-7B from scratch; the 81.5% training share belongs to a different GPT-3.5 run whose held-out square accuracy was 97.5%. "Almost zero accuracy" on held-out squares is unsupported. First author of the case-or-rule paper is Yi Hu. The 16.3% vs 1.4% false-positive rates are MBPP Python vs HumanEval Python. Memento, ExpeL and ReasoningBank each appear in several evidence lines but count as one source each.
