# ACT-R: production compilation: deep document

*Subfield C02.07. Sources: evidence_a-d.jsonl (a01-a29, b01-b26, c01-c27, d01-d15), claims.jsonl (K01-K28), critique.md. Corrections from the critique pass are applied: Exp 1 medium difficulty is p=.062 (not .031); LATM Dyck is 20.4 to 92.2 and word sorting is 59.2 to 98.3. Almost everything on compilation itself is model fitting by one lab. The LLM literature tests looser ideas (verify, store, reuse), not compilation proper.*

## 1. What it is

Production compilation is the learning rule in ACT-R (Anderson, Taatgen and colleagues) that turns slow, instruction-following behaviour into fast, task-specific rules.

- A person starts with instructions held as facts in declarative memory. General rules read each fact and act on it, one retrieval at a time. This is slow and error-prone.
- When two rules fire in sequence, the system builds one new rule that does the work of both. If the first rule retrieved a fact and the second used it, the fact is baked into the new rule and the retrieval disappears. [a01, b13]
- The new rule starts with very low utility. It wins over its parents only after it has been re-created many times. So only frequent patterns become routine. [a05, b05]
- Results: speed-up, fewer errors, and strategy shifts as a by-product of speed. [b09]

Plain example (Table 3 in Taatgen et al. 2008, a01): rule 1 retrieves "in this state, press key K". Rule 2 presses the key. Compiled rule: "if the state is X, press K". One step, no retrieval.

Why it matters for our agent: it is the cognitive-science model of "lesson to routine". Our schema has S9 (one lesson line) and a memory section (lessons, class record, planned subgoal library). Compilation says three things about that memory: promote slowly, keep the parent path alive, and never merge steps that depend on fresh perception or the same module. The LLM literature adds a sharper point: a routine write needs a verification gate (K12, K22).

Honest scope: no LLM paper found implements ACT-R-style compilation (co-firing counts, low initial utility). The closest analogues commit after one verified success [K20]. That is an absence claim from limited search.

## 2. History and theories in depth

**Fitts and Anderson: three stages.** Cognitive, associative, autonomous (Fitts 1964). Anderson (1982, 1987) recast them as a shift from declarative knowledge interpreted by general rules (weak methods such as analogy) to compiled procedural knowledge. Anderson 1982 treated the log-linear power law as the signature of skill. [a22, b24; second-hand, not opened]

**ACT\* had four mechanisms.** Proceduralization, composition, generalisation and discrimination. They were judged too unconstrained: too many invalid and low-utility rules, produced too fast to evaluate. ACT-R 5 replaced proceduralization plus composition with one constrained mechanism. [a13, b07]

**The ACT-R constraint.** Each production may make only one declarative access, split in two steps (request in one rule, use in the next). Adding three numbers takes 1 rule in ACT\* or Soar but 3 in ACT-R. [a13]

**Rivals, mainly differing in grain size** [a25, b07]:
- Instance theory (Logan 1988): store whole solved problems; retrieval races the general algorithm; no rules are built.
- Chunking (Newell and Rosenbloom 1981; Soar): store results of solved subgoals, learned at an impasse from one trace.
- Compilation: merge single steps.
Taatgen's complaint: none addresses flexibility or robustness directly, and specialisation implies old knowledge fails on unseen cases. No experiment found separates the accounts. The Logan, Newell and Anderson originals were not opened.

**Taatgen and Lee 2003.** First full single-mechanism account. One ACT-R model with default parameters learned the Kanfer-Ackerman air traffic controller task from instructions. [a08, b08, c01]

**Taatgen and Anderson 2002.** Past-tense U-shape without feedback, from retrieval competing with a rule built by analogy and compilation. [a11, b11]

**Taatgen 2005.** Perfect time-sharing in dual tasks; rules for what can be merged; gradual utility learning for new rules; weak hierarchy of instructions (rules fire top-down and bottom-up). [a04-a06, b05, b06]

**Taatgen et al. 2008.** Instruction format changes what compilation produces; context (pre/post-condition) instructions give robust, flexible skill. [a01-a03, b01-b04]

**Taatgen 2013 (PRIMs).** Productions split into primitive elements that only compare or copy slot values. Compilation merges primitives that fire in sequence. Task-general rules give transfer. [a15-a19]

**Critical thread: the law of practice.** Heathcote, Brown and Mewhort (2000) re-fit unaveraged data and found the exponential beats the power law. This weakens the classic target compilation was built to explain. It does not refute the mechanism. [a20, d01]

**Recent drift.** Ji, van Rij and Taatgen (2025) set automatic compilation aside and learn procedures through operator-to-context association strength. Gianferrara et al. (2021) use compilation as a fixed part and never switch it off. Compilation is rarely ablated. [a26, a27, d02, K10]

**Bridge to LLM agents.** Wray, Kirk and Laird (2025) name "knowledge compilation" as a design pattern and cite ACT-R and Soar as origin. They say caching LLM reasoning in natural language is not yet widely researched. CoALA (Sumers et al.) frames agents as production systems and warns that writing to procedural memory is riskier than to episodic or semantic memory. The 2026 SoK and the Fan and Lan review map ACT-R's declarative/procedural split to skills and list typed impasse-to-rule compilation as an unfilled bundle. [c03, c04, c15, d15, b23]

## 3. Core findings with exact numbers

Status: E = established (2+ independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Context (pre/post-condition) instructions beat step lists, Exp 1 | N=31 (15 list, 16 context). Accuracy 77.0% vs 91.1%, F(1,29)=7.09, p=.014. Easy 90.4 vs 93.8 (ns). Medium 77.0 vs 91.0, t(18.9)=1.99, p=.062. Hard 70.4 vs 89.9, t(17.9)=2.6, p=.018. Time 28.7 vs 24.8 s, p=.022 | Taatgen et al. 2008 [a02, b01] | C (one lab) |
| Same, Exp 2 (half-done procedures, some with an error) | N=40 (20 per group). 78.8% vs 89.0%, F(1,38)=4.5, p=.040. Time 27.2 vs 23.0 s, p=.065 (marginal) | Taatgen et al. 2008 [b02] | C |
| Same, Exp 3: effect shrinks | N=100 (25 per group, four conditions, random order). Difficulty interaction gone. Example contrasts 26.0 vs 26.9 s and 77.6 vs 82.1%, both p>.10. Extended list no better than simple list; graphic mental model no extra gain. Model predicted 90.9% context and 80.8% list; people less accurate; context accuracy fit R2=.44 | Taatgen et al. 2008 [b03] | C |
| Model fit and prediction | Exp 1 fit R2 .90 accuracy, .89 log latency (a03); context accuracy R2 .82 (b04). Exp 2 predicted R2 .74/.76 (a03) or .66-.75 (b02): treat as about .7. Parameters fitted on Exp 1 only | [a03, b02, b04] | S |
| Compilation fits a complex skill (air traffic control) | N=65, 18 trials of 10 min, trials 1-10 compared, 5 model runs. Planes landed r2=.97; land unit task .98; queue unit task .91; keystrokes .87. Default parameters | Taatgen and Lee 2003 [a08, b08, c01] | E (one lab, model fit) |
| Dual-task cost vanishes with practice | Cost on Day 2 (aural-vocal task), none by Day 5. A new rule saves 100 ms; builds from about 100 experiences, peaks near 150, then wins about 95%; parent chosen under 1% | Schumacher 2001 via Taatgen 2005 [a06, b05] | E (model fit, graphs only) |
| Individual differences as one parameter | 5 of 11 people had almost no residual cost. Motor-start rule time 0.15 s reproduced them; 0.35 s reproduced 4 with large costs (default 0.2 s) | Taatgen 2005 [b06] | S (post-hoc, 11 people) |
| Merge limits | Same-module rules and perception-request plus its user cannot merge. Learned rules end as perception-to-action steps | Taatgen 2005, 2006 [a04, b13] | E |
| Single-example over-generalisation | One DC-10 short-runway landing compiles "DC-10 means short runway", sometimes wrong. Authors blame the reuse strategy, not compilation | Taatgen and Lee 2003 [a09, a14, c02] | E |
| Past-tense U-shape | Model frequency correlation -0.59, child -0.34 (Marcus 1996). 478 verbs (89 irregular). Overregularisation 4.2% preschool, 2.5% grade 1, 1% grade 4. Model fades; two children do not fade in the window | Taatgen and Anderson 2002 [a11, a12, b11] | E (modelling) |
| Practice curve shape | 40 data sets, 7,910 series, 475 subjects, 24 experiments. Exponential better in 82.2% of series (range 64-93%); averaging biases to power | Heathcote et al. 2000 [a20, d01] | E |
| Text-editor transfer (PRIMs) | Move to line, human / identical productions / PRIMs: ED to EDT 87/68/81; EDT to ED 91/75/90; line to Emacs 61/39/66. Plan edit, line to Emacs 62/27/57. Singley and Anderson observed 62% line-to-screen vs 33% by identical productions | Taatgen 2013 [a17, a24] | S (confounds, second-hand) |
| Video-game speed transfer | N=80, 20 per cell. To high speed: humans median 131%, model 68%; to low: 76% vs 82%. Two trackers RMSE 304 (BIC 686) vs 479 (BIC 741) | Gianferrara et al. 2021 [a26, d02] | S |
| Verified programmatic skills beat text workflows (WebArena, Claude) | Vanilla 32.7% / 5.6 steps; AWM 36.3% / 5.9; ASI 40.4% / 5.0. Steps cut 10.7-15.3% | Wang et al. 2025 ASI [c12] | E (with GRASP) |
| Agent Workflow Memory | WebArena GPT-4: 35.5% vs 23.5% BrowserGym (+12.0 pts, +51.1% rel). SteP margin 7.6% (text) / 7.9% (abstract). Callable-action variant +1.3 step-success only; called in 18.5% of tasks | Wang et al. 2024 [b16, c07, c22] | E |
| ReasoningBank | WebArena Gemini-2.5-flash success / steps: none 40.5 / 9.7; Synapse 42.1 / 9.2; AWM 44.1 / 9.0; ReasoningBank 48.8 / 8.3; +MaTTS 51.8 / 7.9. Pro: none 46.7, AWM 47.6. AWM multi-site 3.4 vs 10.3 none (flash) | Ouyang et al. 2025 [c11] | E |
| Voyager skill library | Iron tool 21 +/-7 vs 29 +/-11 iterations; diamond 1/3 runs (102 iterations) with vs 0/3 without; wooden 6 vs 7, stone 11 vs 9 (no early gain). Unseen tasks: diamond pickaxe 19 +/-3 (3/3) vs 36 (2/3). No self-verification -73% items; random curriculum -93%. 3 runs per cell | Wang et al. 2023 [b15, c05, c06] | S |
| Mixed-granularity procedural memory (Memp) | ALFWorld GPT-4o test: none 42.14, script 56.43, trajectory 74.29, both 77.86; steps 23.76 to 15.01. Dev: 39.28 to 87.14. TravelPlanner hard-constraint score: none 12.88, script 5.50, both 9.76 | Fang et al. 2025 [b17, c09, c24] | C |
| Memory content can hurt | ExpeL heat tasks: insights 87 / retrieval 74 / full 43. Reflections added to insight generation hurt | Zhao et al. 2024 [b18, c08, c23] | S |
| Skills in context degrade some tasks | 8 models: 15% of tasks degrade (7% Opus 4.6, 25% Qwen3-30B); 17% unchanged. 39 of 49 SWE skills no gain, 3 hurt | Chen et al. 2026 SkVM [c16, c25] | E (with d03-d05) |
| Self-written skills hurt | SkillsBench, 87 tasks: curated +16.6 pp (33.9 to 50.5); self-generated -8.1, -11.3, -11.5 pp. 13 of 87 tasks negative (worst -7.4) | Li et al. 2026 [d03, d04] | E |
| Skill count and length | 1 skill +18.0, 2-3 +19.0, 4+ +10.1 pp. Compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 pp | [d04] | S |
| Skill use is fragile in realistic settings | Claude: force-loaded 55.4, agent-chosen 51.2, distractors 43.5, retrieved 40.1, no curated 38.4. Kimi 19.8 vs 21.8 baseline; Qwen 19.7 vs 20.5 (both below). Rewrite: Claude 40.1 to 48.2, Qwen 26.7 to 30.8, Kimi 33.5 to 26.7. Only 49% of Claude runs loaded all curated skills | Liu et al. 2026 [d05] | S |
| Commit gate drives skill gains | GRASP MedAgentBench gpt-oss-120b: none 40.6; GRASP 88.8; no gate K=4 63.5, K=1 40.1; best of 5 baselines 67.8; matched probe budget ignoring verdicts 70.8 / 67.2; no regression budget 81.8; no failure grouping 84.4. 3 seeds, large SDs OOD | Moll et al. 2026 [d10] | S |
| Ungated consolidation decays | GPT-5.4 solved 19 ARC problems with no memory; after consolidation from ground truth it failed 54%. ScienceWorld peaks near step 20, then falls. WebShop AWM 0.64 (8 examples) to 0.20 (128), none 0.20. Free choice (retain/delete/consolidate) about doubles forced consolidation | Zhang 2026 [d11, d12] | E with d10 (partly project-page numbers) |
| Applicability gating | EffectMem ScienceWorld Qwen3-8B: baseline SR 15% / score 33.8 / 44.0 steps; +gated routing SR 51% / 71.4 / 30.1; +execution correction SR 65% / 76.0 / 25.9 | Yin et al. 2026 [d13] | S |
| Evidence-gated crystallisation | EvoAgentBench: flat memory vs MSCE Pass@1 -15.38 (IR), -16.00 (Math), -19.23 (SE); no crystallisation -6.15 to -11.54; gain p0 to p100 +17.00 / +15.39 / +13.84 | Tang et al. 2026 [d14] | S |
| Strong model writes tool for weak one (LATM) | GPT-3.5 CoT to LATM: logical deduction 66.4 to 79.7; shuffled objects 61.6 to 99.6; Dyck 20.4 to 92.2; word sorting 59.2 to 98.3; Chinese remainder 0 to 100; schedule meeting 18.9 to 100. GPT-4 user: logical deduction 88.8 to 86.6; Dyck 63.6 to 87.5. GPT-4 call over 15x cost | Cai et al. 2024 [b20, c13] | S |
| Distilling slow reasoning fails on CoT maths | Last letter 30.0 to 98.0; coin flip 56.1 to 75.69; GSM8k CoT 36.39 vs distilled 7.13 (direct 7.58-9.40). Fine-tuning | Yu et al. 2024 [b19] | S |
| Code actions merge steps | CodeAct: up to 20% higher success, up to 30% fewer actions | Wang et al. 2024 [c18] | E (with ASI) |
| Skill pruning | 55,315 skills: 26.4% lack routing descriptions, over 60% of body non-actionable. 600 skills: 39% body compression, +2.8% quality | Gao et al. 2026 [d07] | S |

## 4. Mechanisms and models

### 4.1 ACT-R production compilation, step by step

Data structures: a production is (conditions on buffers, actions on buffers). A declarative chunk is a fact. Each production has a utility U.

Compile trigger: production P1 fires, then P2 fires next, and they are compatible (limits below).

Build rule P3:
1. Conditions of P3 = conditions of P1, plus conditions of P2 not already satisfied by P1's actions.
2. Actions of P3 = actions of P1 and P2 merged.
3. If P1 requested a retrieval and P2 used the retrieved chunk, delete the retrieval and write the chunk's slot values into P3 as constants. This is the baked-in fact. [a01, b13]

Limits [a04, b13, K05]:
- Two rules that call the same module (same hand, same buffer) cannot merge.
- A rule that asks perception for something cannot merge with the rule that uses the result.
- Each rule may make only one declarative access, split over two rules. [a13]
- Net: learned rules step from one perceptual input or motor output to the next. They are state-independent and cued by the world (bottom-up). [a04]

### 4.2 Gradual utility (why only frequent patterns win)

A new rule starts at very low utility. Each time the same rule is re-created, its prior is raised. Utility blends prior and experience:

U = (m * U_prior + n * U_experienced) / (m + n), with m = 10 by default. [a05]

Selection among competing rules is noisy, so the parent still wins sometimes (under 1% at expert level in the dual-task model). In that model the new rule builds up from about 100 experiences, peaks near 150, then wins about 95% of the time. [b05] Without the slow start, expert behaviour would arrive in a few trials, which contradicts data (author's argument, citing Anderson, Fincham and Douglass 1997, not opened). [a05, a23]

Utility update rule used in the game model: U(n) = U(n-1) + a[R - U(n-1)]. [d02]

### 4.3 Learning from instruction format (Taatgen 2008)

- Instructions live in declarative memory as operators. Each operator had a 25% chance of being forgotten. [b04]
- Context instructions encode "in situation S, do A, expect outcome O". Step lists encode only "do A, then B".
- Rules compiled from context instructions keep their conditions, so they work on non-literal problems and allow recovery when the world differs from the list. Rules compiled from lists lack the conditions.
- Three parameters were fitted on Exp 1, then used to predict Exp 2 and 3. [b04]

### 4.4 PRIMs (Taatgen 2013)

Rules are made of primitives: 1,188 condition PRIMs and 504 action PRIMs; 10 input, 7 output and 14 in/out workspace slots; 1,430,586 possible pairs and 805,896,780 triples. Compilation merges sequences. Specifics sit in slots, so compiled rules are task-general and transfer. Counting (Init, Step, Final) and semantic reasoning share an iterate-through-memory structure, so after counting the semantic model needs one more compile step. [a15, a16] Limits: PRIM set fixed by hand, operator retrieval uses hand-set associations, never tested with compilation off. [a19]

### 4.5 Soar chunking (for contrast)

On an impasse Soar makes a subgoal, solves it, and stores a chunk from the trace after one success. No count threshold. CogRec uses this with an LLM: at an impasse Soar asks the LLM, converts the answer to a production, and chunking stores it. [d08]

### 4.6 How LLM agents implement the analogue

Common pattern: do task, check success, induce routine, store, retrieve by similarity, reuse. Differences from ACT-R [c21]:
- Trigger: verified success (Voyager, ASI), LLM judge (online AWM), stronger-model write-up (LATM, SkillWeaver), evidence-estimated gain (MSCE), held-out probe plus regression check (GRASP). ACT-R merges automatically with a count threshold and no verification.
- Unit: whole workflows, programs, tools. ACT-R: single steps.
- Verification: every LLM system that works adds a check that ACT-R lacks.

### 4.7 An engineering sketch for our agent (not yet tested)

Routine store keyed by problem class (from S0).
1. Candidate: at S9, code records (class, trigger conditions, action pattern, outcome) from a verified pass. The raw verified episode is kept as is. [d11, d12]
2. Promotion: a candidate gets count 1 and low utility u0. Each later verified use or co-occurrence adds 1. Promote to routine when count >= k and a regression check on earlier solved cases does not fail. k is the unknown (see UNKNOWNS U1).
3. Retrieval: only routines whose stated conditions match, shown after the first attempt (schema memory rule), at most about 3, each short. [d04, d05]
4. The parent path stays available: a routine is a shortcut, never a replacement. The plain path runs when the check fails or conditions do not match.
5. Demotion: if a routine is used and the check fails, lower its utility; remove at a floor.
6. Do not cache anything that depended on fresh tool output. [K05]

## 5. What holds up

**Held up**
- The merge mechanism is well specified and reproduces human speed-up across complex tasks, always from the same lab. [K01, K09]
- Only frequent patterns become routine, via low start utility. One model, one data set (dual task): plausible, single-source. [K02]
- Gating routine writes by verification: ASI vs AWM, GRASP, MSCE and Voyager's ablations point the same way, and ungated writing fails (SkillsBench, Zhang 2026). [K12, K22, K23]
- Stored skills can hurt, especially for weak models; fewer and shorter is better. [K16, K25]
- Over-generalisation from one example is real in the model and appears in LLM stores. [K06]
- Exponential beats power law on raw practice data. [K08]

**Did not hold up, or is weak**
- The instruction-format effect shrinks in Exp 3 (accuracy fit R2 .82 to .44; interaction gone). One lab only. [b03]
- Compilation speed as a person parameter: 11 people, post-hoc. [K04]
- PRIMs transfer: model-only, fitted learning amount and speed; the Singley and Anderson design has confounds. [a17]
- Model-human mismatches: model faster than people on trial 1; too little transfer to high speed (68% vs 131%); no error recovery; reset spike at transfer; past-tense correlation too strong; no fading in two children. [a03, a26, a12, a11]
- The far-transfer prediction (count span drops after reactive training) was not found in human data. [a18]
- Nobody ablates compilation. [K10]

**Moderators found**
- Difficulty (context benefit mostly on hard problems), practice (gap shrinks), blocked vs random order (Exp 3 removed the interaction). [a02, b03]
- Model strength: LATM and Memp gains largest for weak models; SkVM harm 25% for Qwen3-30B vs 7% for Opus 4.6. [b20, c25]
- Task type: Memp (hard constraints) and ExpeL (heat) hurt. [b17, b18]
- Time in run: Voyager gains late; MSCE gains grow; ungated consolidation peaks near step 20 then falls. [c06, d14, d11]
- Realistic retrieval: benefit falls from 55.4 to 38.4 as selection, distractors and retrieval are added. [d05]

**Interventions that worked**: verification gate; regression budget; applicability and postcondition contracts; self-verification; compact skills (1-3); strong-model-written tools for weak users; mixed granularity (ALFWorld); query-specific rewrite (Claude, Qwen).

**Did not work**: self-written skills made before the task; ungated consolidation; more than 3 skills; comprehensive skills; rewrite for Kimi; script-only or mixed memory under hard constraints; callable-workflow actions (+1.3); distilling CoT maths; abstraction-level wording alone (+0.7 / -6.7, CIs cross zero). [d06]

## 6. Language models

No paper tests ACT-R compilation proper in an LLM [K20]. What exists is a family of verify, store, reuse systems. Their measured effects:

**Web and embodied agents**
- AWM (GPT-4, WebArena): 23.5 to 35.5%. Gain grows with train-test gap (8.9 to 14.0 points). [c07]
- ASI vs AWM vs vanilla (Claude): 40.4 / 36.3 / 32.7%, steps 5.0 / 5.9 / 5.6. [c12]
- ReasoningBank (Gemini flash): 40.5 to 48.8, steps 9.7 to 8.3. On Gemini pro AWM gained only +0.9. [c11]
- Memp: ALFWorld 42.14 to 77.86; Claude test 53.59 / 71.78 / 74.72; value moves from strong to weak models (numbers not extracted). [c09, c10]
- Voyager: 3.3x items, later-stage gains. [c05, c06]
- SkillWeaver: +31.8% WebArena, +39.8% real sites, up to +54.3% for weaker agents (relative, from low baselines; headline numbers differ across paper parts). [c14, b22]
- EffectMem: Qwen3-8B ScienceWorld SR 15 to 65%. [d13]
- MSCE: gains grow along the lifelong curve. [d14]

**What changed the sign**
- No verification: GRASP no gate 40.1 vs 88.8; Voyager no self-verification -73%. [d10, c06]
- Self-written skills: -8.1 to -11.5 pp. [d03]
- Weak model plus general skills: below no-skill. [d05]
- Ungated abstract consolidation: below no-memory after about step 20. [d11]
- Hard constraints under script memory: TravelPlanner 12.88 to 5.50. [b17]

**Efficiency (latency and tokens, not accuracy)**
- SkVM JIT solidification: up to 40% fewer tokens, 19-50x lower latency. [c16]
- NeSyPr (trained): large latency and token cuts; removing the procedure book: CSR 65.2 to 47.9. [d09]
- ASI thought text 87.9 to 13.4 tokens per step in induction data. [c12]
- CodeAct up to 30% fewer actions. [c18]
- CogRec: LLM call rate falls with chunking, stays high without. [d08]

**Compile by training (outside our constraint)**: Distilling S2 to S1 (last letter 30.0 to 98.0; fails on GSM8k), Dualformer (mazes, 59.9% fewer steps in auto mode), LLM-ACTR (ACT-R traces into adapters, accuracy 0.6576). [b19, b21, c19]

**LLM as ACT-R model builder**: EVisiTor turns 14 instructions into ACT-R declarative chunks (94.6% and 92.3% target accuracy for two LLMs, 281 structures). The LLM does not write productions. Excel RMSE 29.19 to 17.37 s. No compilation result. [a29]

**Comparability caveat**: different benchmarks, models, baselines. No paper compares at equal total tokens. The write cost is rarely counted. [K28]

## 7. What our agent should take

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Commit a lesson or routine only after a code-run check (re-run with it, held-out check). Never commit on the model's say-so | G, S9, memory | [E] | K12, K22, K23; c12, d10, d03, c06 |
| A2 | Do not rewrite or merge stored lessons after every task. Keep raw verified episodes; gate any abstraction | memory | [E] | K23; d11, d12, d03 |
| A3 | Never cache a step that depended on fresh tool output as a fixed routine | memory | [E] | K05; a04, b13 |
| A4 | Single-example routines over-generalise: store conditions with every routine and match them before reuse | memory, S9 | [E] | K06; a09, c02, d11, d13 |
| A5 | Keep routines few and short: at most about 3 loaded, each compact (three sources on harm; the size numbers are single-source) | memory | [E] on harm, [S] on size | K16, K25; c25, d04, d05 |
| A6 | Log every routine use with outcome and tokens per model size, and drop routines that do not help | memory, logging | [E] | K16; c16, d03, d05 |
| A7 | Count induction (write) tokens in any routine test | G7 | [E] (our own rule; the literature lacks it) | K28 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Promotion threshold: commit after 1, 3 or 10 verified confirmations | memory | [S] | K02, K20; a05, b05, d10, d14 |
| T2 | Context-style lesson format (conditions, action, postcondition) vs plain steps | S9, memory | [C] | K03, K27; b01-b03, d13, d06 |
| T3 | Routine store on vs off over a long sequence, early vs late items | memory | [C] | K11, K24; c06, d14, d11 |
| T4 | Regression check before a routine becomes default | G, memory | [S] | K22; d10 |
| T5 | Applicability check before reuse (match stated conditions) | S0, memory | [S] | K27, K26; d13, d05 |
| T6 | Routine as shortcut with parent path always kept, demotion on failed check | memory | [D] | a05, b05 |
| T7 | Strong-model-written routines for a weaker solver | memory | [S] | K17; b20, c14 |
| T8 | Granularity: script vs trajectory vs both, hard-constraint score separate | memory | [C] | K14; b17, c24 |
| T9 | Wrong procedural note vs wrong episodic note, damage per type | G | [S] | K21; c04 |
| T10 | Macro-actions at S3/S4 | O | [E] on steps, [S] on our tasks | K19; c18, c12 |
| T11 | Task-general vs task-specific routine level, transfer to a related family | memory | [S] | K07; a15-a17 |

## 8. Concrete tests on our bench

All arms get the same total token budget, including induction (write) calls. Three or more seeds. Items arrive as a sequence within one problem class (or a few), split into position buckets (first, middle, last third).

| Test | Items | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 promotion threshold (T1) | 60 sequential items per class, ARC-style and puzzle classes | k=1 verify-once; k=3; k=10; no store | pass rate by bucket; wrong-reuse rate on near-miss items; total tokens | k=1 gains early but more wrong reuse; k=3 best net; k=10 too slow. Gain 2-5 points over no store, late buckets only |
| B2 lesson format (T2) | 40 hard held-out items (plain model fails about half) | plain step lesson; condition-action-outcome lesson; same reuse check in both | pass rate on hard items; tokens | Gap small if Xu and Wu hold (CIs cross zero); if Taatgen holds, about +10 points on hard items, shrinking with repeats |
| B3 store on/off (T3) | 80 sequential items | store off; store on gated; store on ungated | accuracy by bucket; tokens; late-minus-early gain | gated gains late; ungated falls after about 20 items (Zhang 2026) |
| B4 regression gate (T4) | 50 items plus 10 earlier solved items as probes | write with gate; write without; matched probe spend ignoring verdicts | pass rate; regressions on earlier solved items | gate wins by 10+ points over matched-spend control (GRASP 88.8 vs 70.8 is the upper bound) |
| B5 applicability check (T5) | near-miss items (same class, one condition differs) | reuse by similarity only; reuse with condition match; no reuse | wrong-reuse rate; pass rate | wrong reuse falls with condition match |
| B6 model size (T7, A6) | same stream with 2 model sizes | routines from strong model; self-written; none | pass rate per model; harm rate (items worse than no routine) | weak model gains most from strong-written; harm of 15-25% of items possible with unfiltered routines |
| B7 granularity (T8) | items with a hard-constraint check | script; trajectory; both | pass rate and constraint score separately | script may hurt the constraint score |
| B8 wrong-note damage (T9) | 30 items, inject one wrong note | wrong routine; wrong episodic lesson; no note | accuracy drop | procedural wrong note worse (CoALA claim, unmeasured) |
| B9 routine load size (A5) | same stream | 0, 1, 3, 6 routines loaded | pass rate; tokens | peak at 1-3 |

## 9. What does not transfer, and why

- **Automatic merging without verification.** ACT-R compiles after any two rules fire in sequence. LLM systems that skip verification fall to no-memory level. Our agent also has no reliable record of which steps fired in text. [c21, d10]
- **Step-level grain.** ACT-R merges single production steps (tens of milliseconds). Our units are lessons or programs. Retrieval cost is not our bottleneck; context length and mismatch are. [a25]
- **The 100-150 experience slow start.** Human practice counts are in the hundreds of trials, far above our item counts. k must be rescaled by test, not copied. [b05]
- **Model-fit evidence.** R2 with fitted parameters shows plausibility, not necessity. No ablation exists. [K09, K10]
- **Human timing parameters** (motor start time, retrieval latency). LLM cost is tokens. [b06]
- **Distillation and training-based compiling** (S2 to S1, NeSyPr, LLM-ACTR, Dualformer). Outside our no-training constraint. [b19, d09, c19, b21]
- **Strategy shift as a by-product of speed.** The model has speed pressure; an LLM has none unless we impose a token cap. [b09]
- **The human instruction effect.** Taatgen 2008 used students and about an hour of practice. The one closest LLM test found small wording effects. [b01, d06]
- **The over-generalisation defence.** Taatgen blames the reuse strategy, not compilation. For us the distinction does not matter; the wrong-reuse rate does. [a09]

## 10. Open questions

1. Does ACT-R-style promotion (low start, promote after repeated co-firing) beat verify-once at equal tokens? Nobody has swept a count.
2. Early-vs-late benefit of a store with several seeds and controlled tokens (Voyager used 3 runs).
3. Wrong-reuse rate from 1 vs several examples on near-miss tasks.
4. Does context-style wording beat plain steps in LLMs, and does the gain shrink with practice as in Exp 3?
5. Which model sizes and task types are harmed by routines, and is there a cheap predictor? None validated.
6. Script vs trajectory under hard constraints.
7. Is a wrong procedural entry worse than a wrong episodic one?
8. Do Zhu and Reid (Soar productions from LLM reasoning) report numbers? Not located.
9. Total tokens including write cost.
10. Taatgen 2013 PRIMs transfer numbers from the journal version (the tutorial copy was read; the journal version was not).
11. How much of the human fit is due to compilation, as opposed to the rest of the architecture? No ablation.
12. Does the Taatgen 2008 effect replicate outside the lab? No outside replication found.

## 11. Sources

[V] = opened and read; [M] = snippet or second-hand only.

- [V] Taatgen, Huss, Dickison and Anderson (2008) The acquisition of robust and flexible cognitive skills, JEP:General. https://www.ai.rug.nl/~niels/publications/FMSpublished.pdf [a01-a03, b01-b04]
- [V] Taatgen (2005) Modeling parallelization and flexibility improvements in skill acquisition, Cognitive Science. https://www.ai.rug.nl/~niels/publications/parallel-flexible-published.pdf [a04-a07, b05-b07]
- [V] Taatgen and Lee (2003) Production compilation: a simple mechanism to model complex skill acquisition, Human Factors. https://www.ai.rug.nl/~niels/publications/HF-published.pdf [a08-a10, b08-b10, c01, c02, c27]
- [V] Taatgen and Anderson (2002) Why do children learn to say 'broke'?, Cognition. https://www.ai.rug.nl/~niels/publications/Past-Tense-published.pdf [a11, a12, b11, b12]
- [V] Taatgen (2000, 2002) Learning rules and productions, Encyclopedia of Cognitive Science. https://www.ai.rug.nl/~niels/publications/LearningRules.pdf [a13, b14]
- [V] Taatgen, Lebiere and Anderson (2006) Modeling paradigms in ACT-R. https://www.ai.rug.nl/~niels/publications/taatgenLebiereAnderson.pdf [a14, b13]
- [V] Taatgen (2013) The nature and transfer of cognitive skills, Psychological Review (tutorial copy). https://raw.githubusercontent.com/ntaatgen/PRIMs-Tutorial/master/Papers/ [a15-a19]; [M] journal listing https://www.ai.rug.nl/~niels/publications.html [b26]
- [V] Heathcote, Brown and Mewhort (2000) The power law repealed, Psychonomic Bulletin and Review. https://link.springer.com/content/pdf/10.3758/BF03212979.pdf [a20, d01]
- [M] Newell and Rosenbloom (1981) Mechanisms of skill acquisition and the law of practice (via Heathcote) [a21]
- [M] Anderson (1982) Acquisition of cognitive skill; Anderson (1987) Skill acquisition: compilation of weak-method problem solving. https://doi.org/10.1037/0033-295x.94.2.192 [a22, b24]
- [M] Anderson, Fincham and Douglass (1997) The role of examples and rules. https://doi.org/10.1037/0278-7393.23.4.932 [a23]
- [M] Singley and Anderson (1985) The transfer of text-editing skill (via Taatgen 2013) [a24]
- [M] Logan (1988) Toward an instance theory of automatization (via Taatgen) [a25, b25]
- [V] Gianferrara, Betts and Anderson (2021) Cognitive and motor skill transfer across speeds. https://pmc.ncbi.nlm.nih.gov/articles/PMC8509974/ [a26, d02]
- [V, first part only] Ji, van Rij and Taatgen (2025) Simulating procedural discovery in early language acquisition. https://www.cambridge.org/core/product/identifier/S0305000925100159/type/journal [a27]
- [V, first pages only] Taatgen (2017) Towards cognitive architectures with multiple levels of abstraction. https://raw.githubusercontent.com/ntaatgen/PRIMs-Tutorial/master/Papers/ [a28]
- [V] AI-augmented ACT-R modeling in real interfaces (EVisiTor, 2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13625840/ [a29]
- [V] Wang et al. (2023) Voyager. https://arxiv.org/pdf/2305.16291 [b15, c05, c06, c26]
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/pdf/2409.07429 [b16, c07, c22]
- [V] Fang et al. (2025) Memp. https://arxiv.org/pdf/2508.06433 [b17, c09, c10, c24]
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/pdf/2308.10144 [b18, c08, c23]
- [V] Yu et al. (2024) Distilling System 2 into System 1. https://arxiv.org/pdf/2407.06023 [b19]
- [V] Cai et al. (2024) LATM. https://arxiv.org/pdf/2305.17126 [b20, c13]
- [V] Su et al. (2025) Dualformer. https://arxiv.org/pdf/2410.09918 [b21]
- [V] Zheng et al. (2025) SkillWeaver. https://arxiv.org/pdf/2504.07079 [b22, c14]
- [V] Sumers, Yao, Narasimhan and Griffiths (2024) CoALA. https://arxiv.org/pdf/2309.02427 [b23, c04]
- [V] Wray, Kirk and Laird (2025) Applying cognitive design patterns to general LLM agents. https://arxiv.org/pdf/2505.07087 [c03, c20]
- [V] Jiang et al. (2026) SoK: Agentic Skills. https://arxiv.org/pdf/2602.20867 [c15]
- [V] Chen et al. (2026) SkVM. https://arxiv.org/pdf/2604.03088 [c16, c25]
- [V] Ellis et al. (2021) DreamCoder. https://arxiv.org/pdf/2006.08381 [c17]
- [V] Wang et al. (2024) CodeAct. https://arxiv.org/pdf/2402.01030 [c18]
- [V] LLM-ACTR (2024). https://arxiv.org/pdf/2408.09176 [c19]
- [V] Wang, Gandhi, Neubig and Fried (2025) ASI. https://arxiv.org/pdf/2504.06821 [c12, c21]
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/pdf/2509.25140 [c11]
- [V] Li et al. (2026) SkillsBench. https://arxiv.org/abs/2602.12670 [d03, d04]
- [V] Liu et al. (2026) How well do agentic skills work in the wild. https://arxiv.org/abs/2604.04323 [d05]
- [V] Xu and Wu (2026) Skill availability and presentation granularity. https://arxiv.org/abs/2605.31408 [d06]
- [V] Gao et al. (2026) SkillReducer. https://arxiv.org/abs/2603.29919 [d07]
- [V] CogRec (2025). https://arxiv.org/abs/2512.24113 [d08]
- [V] NeSyPr (2025). https://arxiv.org/abs/2510.19429 [d09]
- [V] Moll et al. (2026) GRASP. https://arxiv.org/abs/2605.29668 [d10]
- [V, partly project page] Zhang (2026) Useful memories become faulty when continuously updated by LLMs. https://arxiv.org/abs/2605.12978 [d11, d12]
- [V] Yin et al. (2026) EffectMem. https://aclanthology.org/2026.findings-emnlp.859.pdf [d13]
- [V] Tang et al. (2026) From memory to skills (MSCE). https://arxiv.org/abs/2607.16621 [d14]
- [V] Fan and Lan (2026) From cognitive architectures to language agents. https://arxiv.org/abs/2607.23942 [d15]
