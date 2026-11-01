# Mathematical problem solving and heuristic method: deep document

Scope: Polya's heuristics (specialise, generalise, work backwards, analogy, auxiliary problem), Schoenfeld's control and monitoring, Brown and Walter's problem posing, and every LLM study found that tests or uses them. Evidence ids (a01 to d19) point to evidence_a-d.jsonl. Claim ids (K01 to K30) point to claims.jsonl. Status words: [E] established, [S] single-source, [C] contested.

Read this first: the human side is thin. The primary Schoenfeld 1985 book, Polya's book, Brown and Walter, and Hembree 1992 were never opened. Only Schoenfeld 1979 and 1982, Rott 2013, Rott and Gawlick 2014 and Kuzle 2019 were read. Most LLM results come from the 2022 to 2024 model era. Treat every effect size here as a prior, not as a fact about current reasoning models.

## 1. What it is

Mathematical problem solving research asks how people (and now models) solve problems for which they have no ready procedure. Three traditions matter for our agent.

1. Polya (1945). A descriptive taxonomy. Four phases: understand the problem, devise a plan, carry out the plan, look back. Heuristics serve the planning phase: specialise, generalise, work backwards, use an analogy, introduce an auxiliary problem (a01, c20). The book reports no experiment and gives no rule for when to pick a heuristic.
2. Schoenfeld (1979 to 1985). The empirical test of Polya. Four ingredients of success: resources (knowledge), heuristics, control (monitoring and resource management) and belief systems (a02). His key claim is that Polya's labels are descriptions, not procedures, and that control, not knowledge or heuristics, often separates experts from novices (a03; b26 and b27 are recalled, not opened).
3. Brown and Walter (1983). "What-if-not": list the attributes of a problem, negate each, pose new problems. It extends heuristics from solving to posing (a24, not opened).

Mapping to the schema (SCHEMA.md): O1 Specialise, O2 Generalise, O3 Decompose, O4 Drop a constraint (the what-if-not move), O5 Work backwards, and S6 IMPASSE as the control layer. Polya's four phases line up with S1 (understand), operator choice at S6/S3 (plan), S3/S4 (execute) and S8/S9 (look back).

The LLM literature rarely uses the Polya words. The same moves appear under other names: step-back (generalise), least-to-most (decompose/simplify), plan-and-solve (plan), analogical prompting (related problem), FOBAR and RevThink (work backwards), Self-Discover (heuristic selection) and Enumerate-Conjecture-Prove (specialise) (a28).

## 2. History and theories in depth

### 2.1 Polya's heuristics (1945)
- Structure: four phases, each with questions to ask ("Do you know a related problem?", "Can you solve a special case?", "Can you work backwards?"). Second-hand description only (a01).
- Strength: a complete vocabulary of moves. Weakness: no selection rule and no control. Polya tells the solver what moves exist, not when to switch.
- The LLM paper Llama-Polya (a14, 2026) fine-tuned Llama-3.1-8B on synthetic GSM8K tutoring dialogues in Polya's four stages. It measured stage conformity, not solve rate (see section 6).

### 2.2 Begle and the 1970s null results
Reviews of 1970s studies found that teaching generic heuristics rarely improved problem solving (b28, recalled, not opened). This motivated Schoenfeld: the labels were too vague to teach. Treat as background.

### 2.3 Schoenfeld's programme
- 1979 (d01, opened). Seven upper-division college students. Four got explicit heuristic training, three were controls. All four trained students outscored all three controls on the posttest (chance 1 in 35, p<.05). Mean net gain: controls 0, heuristic group more than 2 problems. Five heuristics were trained together, so no per-heuristic effect exists. Posttest problems were cut off at 20 minutes. Problems were chosen to fit the taught heuristics.
- 1980/1985 (b26, recalled). Training worked only when the heuristics were broken into specific operational strategies, not left as Polya's headings. Transfer far from the taught problems was weak. This is the most useful design lesson: a heuristic needs a procedure, a trigger and a stop rule.
- 1982 (a03, a04, opened). Three recorded protocols (two student pairs, one mathematician). Students picked a direction on a geometry construction problem, calculated until the 20-minute tape ran out, and could not say what the answer would be good for. The expert started with less relevant knowledge but monitored and re-planned. This is the origin of the "wild goose chase". Case studies, no statistics. Pairs may behave differently from solo solvers.
- Awareness levels (a04): unaware, aware but non-reflective, locally aware and reflective, reflexive abstraction. A taxonomy, not a measured scale.
- Wild-goose-chase figures. About 60% of university students showed wild-goose-chase behaviour; after a course where the teacher kept asking three questions the share fell to about 20% (a07). Second-hand: this is Schoenfeld as quoted by Rott 2013. The primary paper was not opened. One teacher's classes, no control group stated. Use as motivation only.
- Three monitoring questions (as described in the sources): what are you doing, why are you doing it, how will it help. This is the only concrete control intervention in the human literature we have.

### 2.4 Replications and extensions
- Lester, Garofalo and Kroll (1989), as quoted in Rott: in two Grade 7 classes better solvers monitored and regulated more (a10). Correlational; knowledge is a confound.
- Rott (2013, a08, opened). Replicated the wild-goose-chase link in Grade 5. 45 children, 88 processes. 32 wild-goose-chase processes: 27 reached none/basic access to a solution, 5 advanced/full. 56 other processes: 16 none/basic, 40 advanced/full. Chi-square 25.378, p<0.0001 (table; text says p<0.001). 10 of 19 "Squares on a Chessboard" processes were excluded. Caveat: Rott's operational rule defines a wild goose chase as only analysis and exploration episodes, with no planning or verification. So part of the link to success is built into the definition.
- Rott (2013, a09): about 25% of processes were double-coded with a second scheme; in almost all cases the junctures between episodes carried metacognitive activity (focus of attention, reflective checks). No exact count.
- Rott and Gawlick (2014, d02, opened). N=28 German student teachers: 9 explicit heuristic training, 10 practice-only, 9 no training. Posttest ANOVA F=3.853, p=.035. Explicit vs practice-only p=.043 (Bonferroni). Gain scores F=6.307, p=.006; explicit vs no training p=.005. Corrected d: explicit vs practice 0.786, explicit vs none 1.438, practice vs none 0.640. Caveats: small groups, short training, posttest slightly harder than pretest (the no-training group fell), effect sizes from an online calculator.
- Kuzle (2019, a12): 14 Grade 5 students, about a year of working-backward training. Before training almost all used working backward intuitively but struggled with complex reversing tasks. After training 10 solved a bridge-crossing task partly or fully (8 had been at the two lowest levels before). No control group. Post-test content did not match the curriculum.
- Asmus (2010), Amit and Portnov-Neeman (2016) as reviewed in Kuzle (a13): reversal is not present from the start. Grade 2 gifted N=182: at least 9% correct on an unknown-start-state problem, 35% reasonable approach; Grade 4: 36% correct. Gifted samples; second-hand.
- Unread: Hembree 1992 meta-analysis (b29, d03), Mevarech and Kramarski IMPROVE 1997 and Kramarski and Mevarech 2003 (a11, b30, d04), Sinha and Kapur 2021 on productive failure (b31, recalled g about 0.36), Kirschner, Sweller and Clark 2006 (b32). Do not cite any effect size from these.

### 2.5 Brown and Walter and problem posing
Only background (a24). No empirical results were found, in humans or in prompting-only LLM work. The closest LLM evidence is training-time self-proposed tasks (Absolute Zero, d19).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Heuristic training beat controls (humans) | N=7, 4 vs 3; all trained beat all controls; p=1/35 | Schoenfeld 1979 (d01) | [S] tiny N |
| Explicit heuristic training beat practice-only and none | N=28; d=0.79 (vs practice), d=1.44 (vs none); practice vs none d=0.64 | Rott and Gawlick 2014 (d02) | [S] small groups |
| Wild goose chase linked to failure | 5 of 32 (16%) advanced access vs 40 of 56 (71%); chi-sq 25.378, p<0.0001 | Rott 2013 (a08) | [S] partly circular definition |
| Questioning cut wild goose chase | about 60% to about 20% | Schoenfeld via Rott (a07) | [S] second-hand, no control |
| Step-back on knowledge-heavy tasks (PaLM-2L) | MMLU Physics 66.4 to 73.2 (CoT 65.0); Chemistry 70.9 to 81.8 (CoT 75.3); TimeQA 41.5 to 66.0 | Zheng 2024 (a15, b05, c01, c02) | [S] |
| Step-back gain shrinks with model strength | GPT-4 Physics CoT 82.9 vs step-back 84.5; Chemistry 85.3 vs 85.6 | Zheng 2024 (a15) | [S] |
| Step-back on GSM8K: no gain | 84.3 vs CoT 84.4 | Zheng 2024 (a16, b06) | [S] |
| Step-back fixes and breaks | fixes 20.5% of baseline errors, introduces 11.9% (MMLU Physics); TimeQA fixes 39.9%, causes 5.6%; over 90% of remaining errors are reasoning errors | Zheng 2024 (a16, c03) | [S] |
| Least-to-most length generalisation | SCAN length split 99.7% vs CoT 16.2% vs standard 16.7%; last-letter length 12: 74.0 vs 31.8 | Zhou 2023 (a17, c07) | [S] synthetic, hand-built exemplars |
| Least-to-most on real maths | GSM8K 62.39 vs 60.87 (prose says 60.97); 5+ step problems 39.07 to 45.23 | Zhou 2023 (a18) | [S] small |
| Plan-and-Solve | six arithmetic sets: CoT 70.4, PS 73.5, PS+ 76.7, 8-shot manual CoT 77.6; GSM8K 56.4 to 59.3 | Wang 2023 (b14, c06) | [S] old model |
| Plan-and-Solve error mix (46 wrong GSM8K) | calculation 7%, missing step 12%, semantic misunderstanding 27%; with PS+: 5%, 7%, 27% | Wang 2023 (b14, c05) | [S] corrected; a19 wrongly said 27% for missing step |
| Self-generated analogues | GSM8K GPT-3.5 75.0 to 77.8; MATH 33.0 to 37.3; of 50 correct: 35 relevant and correct, 9 relevant but wrong, 6 irrelevant | Yasunaga 2024 (c08, c09) | [S] tables partly garbled |
| Self-Discover | beats CoT on 21 of 25 tasks (PaLM 2-L); MATH PaLM 45/42/49/50.5 (base/CoT/PS/SD), GPT-4 70.5/71/70/73 on 200 problems; 74.7% of MATH failures are computation, 25.3% structure; 10-40x less compute than self-consistency | Zhou 2024 (a21, b19, c10, d18) | [S] MATH gain near noise |
| Skill-labelled exemplars | MATH +11.6% over CoT, +3.5% over Complex CoT, +4.0% over CoT-SC | Didolkar 2024 (b17) | [S] |
| Backward verification (FOBAR) vs voting | average over six sets: davinci 81.4 to 83.5; GPT-3.5 85.5 to 86.6; GPT-4 91.1 to 91.4; GSM8K GPT-4 94.8 to 95.4 | Jiang 2024 (b07, c12) | [E] direction, [S] size; GPT-4 gain is noise |
| FOBAR not always ahead | davinci+ComplexCoT GSM8K SC 79.1 vs FOBAR 78.7; GPT-4 ComplexCoT SC 91.6 vs FOBAR 91.9 | Jiang 2024 (b07, critique) | [S] |
| Self-verification by backward masking | disagreeing-candidate subsets: GSM8K CoT 53.4 to 58.9; MultiArith 71.2 to 89.0 | Weng 2023 (c13) | [S] |
| RevThink (training with backward questions) | avg +13.53% over student zero-shot, +6.84% over best distillation; Mistral 50.55 to 63.23; MATH 10.42 to 15.28; GSM8K 54.71 to 60.88 | Chen 2025 (a22, b08, c11) | [S] training method; maths gain small |
| Intrinsic self-correction fails (2023 models) | GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; GPT-4 95.5 to 91.5 to 89.0; CommonSenseQA 75.8 to 38.1 | Huang 2024 (b21, c14) | [S] older models |
| R1-class models recover from planted errors | R1 671B about 90 recovery; other models average 61.6-point drop | Silver 2025 (d08) | [S] synthetic errors |
| Process checking beats outcome checking | best-of-1860 on MATH subset: process 78.2, outcome 72.4, majority 69.6 | Lightman 2024 (b22) | [S] needs 800K labels |
| Brittleness to irrelevant clause | GSM-NoOp: Phi-3-mini up to -65; o1-preview -17.5; o1-mini -29.1; GPT-4o-mini -40.0 | Mirzadeh 2025 (b10, d14) | [E] (five sources) |
| Brittleness to number changes and contamination | GSM8K score more than 1 SD above GSM-Symbolic centre for 21 of 25 models; GSM1k drops up to 8% | b09, b23 | [E] |
| Premise order | R-GSM: GPT-4-turbo 94.1 to 85.0; PaLM 2-L 86.4 to 79.5; Gemini 1.0 Pro 80.5 to 69.1; GPT-3.5 67.3 to 51.8 | Chen 2024 (b13) | [S] |
| Irrelevant context | GSM-IC: under 30% of base problems solved consistently | Shi 2023 (b12) | [S] 2022 models |
| Restate/regenerate step | S2A on GSM-IC 51.7 to 61.3 (LLaMA-2-70B, 100 problems); 'ignore' instruction no consistent gain | Weston 2023 (d12) | [S] small |
| Ignore instruction on a small model | Llama-3.1-8B attack success 37.5% to 9.9% | Rajeev 2025 (d13) | [S] one model |
| Irrelevant trigger on reasoning models | more than 300% more wrong answers for R1 and R1-distill-Qwen-32B | Rajeev 2025 (d13) | [S] proxy-selected triggers |
| Cognitive behaviours drive RL gain | Countdown: Qwen-2.5-3B about 60%, Llama-3.2-3B about 30%; priming Llama with verification, backtracking, subgoals, backward chaining lets it match or beat Qwen | Gandhi 2025 (b01, c17) | [S] one task |
| Not just length | empty-CoT and length-matched placeholder: Llama stays 30-35% | Gandhi 2025 (b02, d11) | [S] |
| Behaviour matters, not answer correctness | incorrect-but-behavioural priming comparable to correct priming | Gandhi 2025 (b03, c18) | [S] paper says "comparable", not identical |
| Behaviour transfer is counts not accuracy | GPQA: subgoal setting 6.5 vs 0.7 per question; accuracy about 12% both | Gandhi 2025 App. H (d11) | [S] |
| Olympiad proofs | USAMO 2025: Gemini-2.5-Pro 24.4%, all others under 5%; same wrong strategy repeated across attempts | Petrov 2025 (c15, c16, d10) | [S] |
| Underthinking | wrong answers use 225% more tokens and 418% more thought switches; switch penalty: QwQ AIME24 38.3 to 44.1; stay-on-one-thought prompt did not help R1 (72.4 vs 73.8) | Wang 2025 (d09) | [S] correlational |
| Forced plan-monitor-evaluate (Think2) | Llama-3-8B GSM8K 80.71 standard to 69.55; Qwen-3-8B thinking 91.72 vs 91.65; seeded-error funnel 12 of 24 (50%) vs 7 of 43 (16.3%) | Elenjical 2026 (d07) | [S] 8B models, tiny funnel |
| Generic CoT on reasoning models | GPQA: o3-mini +2.9 (p=.024), o4-mini +3.1 (p=.003), Gemini Flash 2.5 -3.3 (p=.005); time +20 to 80% | Meincke 2025 (d06) | [E] with K21 |
| CoT gain lives in maths and symbols | up to 95% of MMLU gain on questions with "="; GSM8K gain up to 66.9, MATH up to 41.6 | Sprague 2025 (b16) | [E] |
| Specialise then conjecture | ConstructiveBench: gpt-4.1-mini 14.54 to 45.06; deepseek-v3 19.06 to 43.81; post-cutoff 5.43 to 31.52; PutnamBench 15.13 to 23.15 | Sun 2025 (d05) | [S] |
| Verification beats voting at scale | Consistency@50 equals Consistency@10,000 on AIME (Gemini 1.5 Pro); Verification@k keeps scaling | Zhao 2025 (d15) | [S] |
| Forced "Wait" re-check | s1-32B AIME24 50% to 57% after up to 6 repeats; more causes loops | Muennighoff 2025 (d17) | [S] |
| Chain-of-thought needs scale | PaLM 540B GSM8K about 18% to about 57% (approximate, from figure) | Wei 2022 (b20) | [E] |
| Zero-shot CoT | text-davinci-002 MultiArith 17.7 to 78.7; GSM8K 10.4 to 40.7 | Kojima 2022 (c04) | [E] for old models |

## 4. Mechanisms and models

Each mechanism below is stated so an engineer could build it. None is a validated controller; they are readings of the evidence.

### 4.1 Schoenfeld's episode model (the control layer)
- Episodes: read, analyse, explore, plan/implement, verify (a02).
- Failure signature, "wild goose chase": the trace has only analyse and explore episodes, no plan and no verify, until time runs out.
- Detector (implementable in code): label each chunk of a trace by episode with a small classifier or a cheap model call. Fire an alert when N consecutive chunks (or a budget fraction) contain no plan and no verify episode. This is Rott's operational rule (a08).
- Intervention: at the alert, ask the three monitoring questions (what are you doing, why, how will it help). If the answers are empty or circular, stop the line and pick a new operator.
- Evidence the detector is predictive: Rott 2013 only, with a partly circular definition. Evidence the intervention works on models: none. See U1.

### 4.2 Operator selection as a policy
- Polya gives moves, not a policy. Self-Discover is the only tested selector: one planning call picks and composes reasoning modules per task, then the same structure is applied to every item (a21, d18). It selects per task, not per item.
- A per-item selector would be: an S0/S6 call returns one of {specialise, generalise, decompose, drop constraint, work backward, analogue}; code logs the choice and the outcome; a table of past (class, operator, success) tunes the choice. Nothing tested (K28).
- Rule from Schoenfeld: each operator is a procedure with a trigger and a stop rule. For "specialise" this is: tabulate n=1,2,3,4, write the pattern, test on n=5 (d05).

### 4.3 Step-back (generalise)
Two calls. Call 1: "State the principle or concept behind this question." Call 2: solve with the principle in context (a15). Code gate: use only when the failure is a missing principle. Gain is near zero on arithmetic (a16).
- Error accounting: fixes 20.5% of baseline errors, introduces 11.9%. So keep the original answer as a candidate and let a check decide, rather than overwrite (K06).

### 4.4 Least-to-most (decompose)
Call 1: list the sub-questions in order. Calls 2..k: answer each, feeding earlier answers forward (a17). Gain scales with chain length; on short chains it is small (a18). Prompts were hand-built per task in the paper.

### 4.5 Plan-and-Solve
One prompt: "Devise a plan, extract variables, then carry out the plan, calculating intermediate results" (b14). Targets missing-step errors (12% to 7% of errors); semantic misunderstanding stayed at 27% (c05), which is why S1 restating matters.

### 4.6 Working backward as verification (FOBAR, self-verification)
- FOBAR: take the question, mask one number, substitute the candidate answer, ask the model to recover the masked number. Score the candidate by how often the recovery matches. Combine with the forward vote (b07).
- Boundary: needs a numeric slot. Fails on proofs and non-numeric answers (a23).
- Code-based variant (cheaper and closer to G2/G3): where the answer can be executed, plug it back in with code. The model only writes the check.
- RevThink is the training-time version: train on forward reasoning plus a backward question and backward reasoning (a22). Not a scaffold.

### 4.7 Specialise-then-conjecture (Enumerate-Conjecture-Prove)
Enumerate answers for small cases (by code), ask the model for a closed-form conjecture, then verify in Lean (d05). The verifier is formal, so there is a real check. Without a checker the conjecture would be unverified and G3 forbids accepting it.

### 4.8 Analogical recall
Ask the model to write 3 to 5 related solved problems, then solve the target (c08). Wrong-but-relevant exemplars were present in 9 of 50 correct cases (c09). The mapping must be checked by code (O7).

### 4.9 Restate-and-strip (input hygiene)
Regenerate the problem with only the relevant context, then solve from the regeneration (System 2 Attention, d12). Ties to S1 input hygiene. A plain "ignore irrelevant text" sentence has mixed value: no consistent gain on LLaMA-2-70B (d12), large gain on Llama-3.1-8B (d13).

### 4.10 Cognitive-behaviour account (Gandhi)
Four behaviours: verification, backtracking, subgoal setting, backward chaining. Their presence in a base model predicts RL improvement; priming a base model with them closes the gap; length-matched empty CoT does not (b01, b02). Reading for scaffolds: the behaviours are plausible contents of S6 and S8, but the evidence is for training, not prompting.

### 4.11 Budget and halting rules seen in the data
- Forced "Wait" up to about 6 times helps; more gives loops (d17).
- Reasoning models switch too much (418% more switches in wrong answers) yet USAMO failures show too little switching. Rule suggestion: a bounded depth on one approach, a stated failed check, then a different approach (K23). Untested.

## 5. What holds up

### 5.1 Replications and meta-analyses
- Wild goose chase and success: one replication (Rott 2013, Grade 5), with a definition that partly builds in the result. No independent replication in other labs found.
- Explicit heuristic training: Schoenfeld 1979 (N=7) and Rott and Gawlick 2014 (N=28) agree in direction. Both are tiny. The pooled Hembree 1992 estimate was never read.
- Brittleness of LLM maths: replicated across five lines (GSM-Symbolic, GSM-IC, premise order, GSM1k, adversarial triggers) [E].
- CoT helps mainly on maths and symbolic tasks: meta-analysis of 100+ papers plus 20 datasets and 14 models (b16) [E].
- Generic "think step by step" adds little on reasoning models (d06) [E].

### 5.2 Failures and nulls
- Step-back on GSM8K: 84.3 vs 84.4 (a16).
- Least-to-most on distractor maths: lower macro accuracy than CoT for text-davinci-003 (b15, b12).
- FOBAR with ComplexCoT: voting edges FOBAR on davinci GSM8K (79.1 vs 78.7); on GPT-4 the 0.3 gap is within noise.
- Free self-correction hurts: GPT-3.5 CommonSenseQA 75.8 to 38.1 (c14).
- Always-on plan-monitor-evaluate hurts a non-reasoning 8B model: GSM8K 80.71 to 69.55 (d07).
- Behaviour transfer to GPQA: behaviour counts rise, accuracy does not (d11).
- "Stay on one thought" prompt: no gain for R1 (d09).
- Few-shot examples did not fix GSM-NoOp (d14).
- RevThink: training on backward questions alone hurts, sometimes below zero-shot (a22). Maths gain is small against Answer Augmentation (b08).

### 5.3 Moderators
- Model strength: step-back +1.6 on GPT-4 physics vs +7 to +11 on PaLM-2L; FOBAR gain 2.1, 1.1, 0.3 points as the model gets stronger (davinci, GPT-3.5, GPT-4).
- Task type: gain is large where the failure is structural (principle recall, length generalisation, missing steps) and small on GSM8K-style arithmetic where errors are calculation (a28). Self-Discover: 74.7% of MATH failures are computation, so structure helps little.
- Chain length: least-to-most gains grow with length (74.0 vs 31.8 at length 12; 39.07 to 45.23 at 5+ steps).
- Reasoning vs non-reasoning: CoT adds +13.5 and +11.7 on non-reasoning models (Flash 2.0, Sonnet 3.5) but only about +3 on reasoning models, and -3.3 on Flash 2.5 (d06). Against the default no-prompt condition the gains mostly vanish.
- Human age and task: working backward is not present at Grade 2 for unknown-start problems (a13).

### 5.4 Interventions that worked
Step-back on knowledge-heavy items (older models); least-to-most on long chains; specialise-then-conjecture on answer construction (with a formal checker); restate/regenerate on distractor items (older models); verification over voting at large budgets; process-level checking over outcome-level checking (needs labels); planted-error recovery in R1-class models without a prompt (d08).

### 5.5 Interventions that did not
Free "review your answer" loops (2023 models); always-on forced metacognitive cycle on a small non-reasoning model; stay-on-one-thought prompt; few-shot fixes for distractors; always-on generic CoT on reasoning models.

### 5.6 Competing explanations
- Gandhi: the gain may come from behaviours, from the format of the traces, or from the teacher model's knowledge. The empty-CoT control rules out length only.
- Rott: wild goose chase may predict failure because failing solvers have no plan, not because monitoring is the cause.
- Self-Discover: gain may come from a better prompt format, not from heuristic choice. No ablation separates the two.
- Step-back: the TimeQA gain is retrieval-like (45% of remaining errors are retrieval failures), so it is not a maths effect.

## 6. Language models

### 6.1 Direct tests of Polya-style moves (2022 to 2024 models)
Step-back, least-to-most, plan-and-solve, analogical prompting, Self-Discover, FOBAR: section 3 gives the numbers. The pattern is consistent: big gains on weak models and structural tasks, small or nil gains on strong models and arithmetic. All come from the authors' own prompts and benchmarks. Compute is rarely equalised: Self-Discover compares calls, FOBAR adds backward chains on top of the same forward chains.

### 6.2 Control and monitoring
- No LLM study tests Schoenfeld-style episode monitoring directly (a27, critique gap 1).
- Think2 (d07, 2026) is the nearest: forced plan-monitor-evaluate on every query. Llama-3-8B GSM8K falls 80.71 to 69.55. Qwen-3-8B thinking is flat (91.72 vs 91.65). AIME 4.82 to 5.89 (noise near 5%). MBPP: CoT best. Seeded-error self-correction 12 of 24 vs 7 of 43. Generation capped at 2,048 tokens; no token-matched control.
- Huang (b21): intrinsic self-correction harms 2023 models. Silver (d08): R1 recovers about 90% from planted errors unprompted, so the reasoning model already monitors inside its chain.
- Wang (d09): reasoning models switch thoughts too much; wrong answers have 418% more switches. A decode-time switch penalty gave +0 to +6 points (QwQ AIME24 38.3 to 44.1, R1-distill-32B 61.4 to 64.1). Needs logit access.
- Petrov (c16): on USAMO each model often tried the same wrong strategy across all attempts; Flash-Thinking tried several strategies but each shallowly.
- Muennighoff (d17): forced "Wait" up to 6 repeats helps, then loops.

### 6.3 Behaviours
Gandhi (b01 to b04, d11): the four behaviours predict and cause RL gains on Countdown at 3B scale. Pretraining data rarely contains verification and backtracking (200,000 documents classified with Qwen-2.5-32B). Transfer to GPQA is in counts only.

### 6.4 Working backward
FOBAR (backward verification), RevThink (backward training), Gandhi (backward chaining behaviour), premise order (b13: GPT-4-turbo prefers backward order, PaLM 2-L does worst with backward order). Backward ordering helps some models and hurts others.

### 6.5 Specialise
Only Enumerate-Conjecture-Prove (d05): 14.54 to 45.06 on gpt-4.1-mini. Not token-matched; CoT limited to 2,048 tokens; Pass@32 proving; no ablation of enumeration alone vs conjecture.

### 6.6 What changed it, by how much
- Model strength: gains shrink from tens of points (PaLM-2L, davinci) to 0 to 2 points (GPT-4, reasoning models).
- Training instead of prompting: RevThink +13.53% average; Gandhi 30% to about 60% on Countdown. These move the model itself and do not transfer to a frozen model.
- Tools and formal checks: Lean in ECP; a symbolic solver beats CoT for both planning and execution (b16).
- Verification scaling: Verification@k scales when voting saturates at about 50 samples (d15).

### 6.7 Where models still fail
GSM-NoOp (-17.5 to -65 points), premise reorder (up to -15 points on R-GSM), contamination (up to 8% on GSM1k), USAMO proofs (24.4% best, under 5% for the rest), Tower of Hanoi complexity cliffs (b24; disputed: Lawsen b25 says output-token limits and impossible instances explain much of it, no table of numbers given).

## 7. What our agent should take

### Add now (established)
1. **[E] Apply the heavy schema only to maths and symbolic items; skip it elsewhere.** Part: S0. Evidence: K18; b16, b20, c04. Reason: CoT gains concentrate there (up to 95% of the MMLU gain on "=" questions).
2. **[E] Every scaffold step must beat a bare reasoning-model run at matched tokens.** Part: G7 (already present; this adds quantitative support). Evidence: K21; d06 (o3-mini +2.9, o4-mini +3.1, Flash 2.5 -3.3 at 20 to 80% more time).
3. **[E] Expect brittleness to distractors and number changes; keep input hygiene in S1.** Part: S1 / G. Evidence: K15; b09, b10, b12, b13, b23, d12 to d14. The S1 restate step quotes the original and lists what is irrelevant, code-checked where possible. The restate remedy itself is [S] (see Test first).
4. **[E] Backward checks help as one check type, but a gain over extra samples is unproven.** Part: O5 / S8. Evidence: K12 (a22, a23, b07, b08, c11 to c13). Use plug-the-answer-back by code where the answer can be executed. FOBAR-style masking stays a test candidate (U2).
5. **[S, consistent with G2] No free "review your answer" loop.** Part: S5 / G2. Evidence: K13; b21, c14, d08. Revisions need a failing output from code. 2023 models only; R1-class models self-recover unprompted.
6. **[S, consistent with G1] Fire the monitor on a signal, not always.** Part: S6 / G1. Evidence: K20; d07. Always-on cost 11 points on a non-reasoning 8B model.
7. **[S] Cap forced re-checks at a small number and stop on a loop signature.** Part: S6 / G11. Evidence: K27; d17.
8. **[S] Do not trust per-model gain sizes from papers; measure per model.** Part: G7. Evidence: K05, K12; a15, b07.

### Test first (not established)
- **[S] Juncture monitor, conditional.** Part: S6. Trigger on stall or at episode ends, not always. Evidence: K01, K02, K03, K20; a03, a07, a08, d07. Test: U1.
- **[S] Backward check vs extra forward sample at equal tokens.** Part: O5 / S8. Evidence: K12, K26; b07, c12, d15, d16. Test: U2.
- **[S] Gate step-back on item type.** Part: O2 / S0. Evidence: K04, K05, K06; a15, a16, c01 to c03. Test: U3.
- **[S] Specialise operator (tabulate small cases, conjecture, verify) on find-the-formula items.** Part: O1. Evidence: K22; d05. Test: U4.
- **[open] Per-item heuristic choice with oracle baseline.** Part: S6 operator pick. Evidence: K28; d18. Test: U5.
- **[S] Restate-and-strip vs plain ignore sentence.** Part: S1. Evidence: K25; d12, d13. Test: U6.
- **[S] Decompose on long-chain items only.** Part: O3. Evidence: K07; a17, a18. Test: U7.
- **[C] Forced strategy switch after a failed attempt.** Part: S6 / O1. Evidence: K17, K23; c16, d09, d10. Contested: reasoning models over-switch, others under-switch. Test: U8.
- **[S] Plan-first prompt on a current model.** Part: O3 / S3. Evidence: K08; b14, c05, c06. Expect a small gain. Test: U9.
- **[S] Self-recalled analogue before attempt.** Part: O7. Evidence: K10; c08, c09. Test: U10.
- **[S] Step-level check vs final-answer check.** Part: S4 / S8. Evidence: K14; b22. Test: U11.
- **[open] Problem posing (what-if-not).** Part: O4. Evidence: K29; d19. Low priority. Test: U12.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (count setup and every call). At least 3 seeds. Include a bare-model arm as reference (G7). Run on two models: one non-reasoning, one reasoning.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Conditional monitor | maths word problems with 3+ steps; proof-lite puzzles | none vs always-on (every N steps) vs conditional (on stall or episode end) | solve rate; dead-end runs (no plan or verify episode in N chunks) | conditional >= none; always-on lower on non-reasoning models (d07: -11 points on Llama-3-8B); about 0 on reasoning model |
| T2 Backward vs sample | numeric-answer maths (GSM8K-style, MATH level 1-3) | k forward samples + vote vs k-m forward + m backward checks (mask a number) vs code plug-back where possible | solve rate at equal tokens | within 0.5 to 1 point on strong models (b07, d16); code plug-back arm should beat both |
| T3 Step-back gate | physics/chemistry/knowledge items vs arithmetic items | CoT vs step-back always vs step-back gated by item type; keep original as candidate | solve rate; fix rate and break rate (compare 20.5% / 11.9%) | +5 to +10 on knowledge items for a non-reasoning model; about 0 on arithmetic; gated >= always |
| T4 Specialise | find-the-formula and sequence-pattern items with a code checker | CoT vs enumerate small cases by code, conjecture, test on held-out n | solve rate; conjectures failing held-out n | large gain on non-reasoning model (d05 about +30 points); small on reasoning model |
| T5 Per-heuristic ablation | one mixed set of 100+ contest-maths items | each of {specialise, generalise, decompose, drop constraint, work backward, analogue} forced vs model-chosen vs oracle best-of-6 vs bare | solve rate per heuristic; gap model-chosen vs oracle | oracle >> any single heuristic; model-chosen between bare and oracle |
| T6 Distractor strip | GSM-NoOp-style and GSM-IC-style variants | plain vs "ignore irrelevant" sentence vs restate-and-strip | accuracy drop vs clean version | restate beats ignore on weak models; both near 0 on reasoning models (d13 suggests the attack persists, so check) |
| T7 Decompose by length | chain length 2-3 vs 6+ steps | flat CoT vs least-to-most | solve rate by length bucket | gain grows with length (a18: about +6 at 5+ steps) |
| T8 Switch rule | olympiad-lite or hard maths with a grader | no rule vs bounded-depth-then-switch vs forced switch after each failed check | distinct strategies per item; solve rate; tokens | unclear; tells us which failure dominates our model |
| T9 Plan-first | multi-step arithmetic | zero-shot CoT vs PS+ prompt | solve rate; missing-step error share | +0 to +3 non-reasoning; 0 reasoning |
| T10 Self-analogue | MATH level 3-5 | CoT vs recall 3 related problems then solve; relevance checked by code | solve rate; wrong-exemplar rate | +2 to +4 for weak models |
| T11 Step-level check | multi-step maths with intermediate checks by code | final-answer check vs step check by code (not model) | solve rate; tokens | step-level >= final-level (b22 gap was 5.8 points, with a trained reward model) |
| T12 Problem posing | open tasks only | plain vs what-if-not rewrite | task success; novelty by running (G8) | unknown; low priority |

## 9. What does not transfer, and why

- **Human training effects do not transfer to a frozen model.** Schoenfeld's students learned over weeks; the model has no memory across items except what the schema stores. The human results justify explicit operators, not any effect size.
- **Training-time results (RevThink, Gandhi, Absolute Zero) do not transfer to a scaffold.** They change weights. RevThink's backward question only helps because the student is trained on it; at test time the student reasons forward only (c11).
- **Countdown-only results.** Gandhi's behaviours work on a narrow arithmetic game at 3B. Transfer to GPQA was seen in counts, not accuracy (d11).
- **Old-model gains.** Step-back, PS+, least-to-most, FOBAR and analogical gains were measured on text-davinci, PaLM-2L, GPT-3.5 and similar. On GPT-4 and reasoning models most shrink to under 2 points.
- **FOBAR on non-numeric tasks.** The mask-a-number template needs a numeric slot (a23, c12).
- **Human wild-goose-chase detection from episode labels** needs a labeller; in a model trace the "episodes" are text chunks, and reasoning models mix them. The detector is untested.
- **Premise order.** Backward order helps GPT-4-turbo but hurts PaLM 2-L (b13). No single order rule transfers.
- **Hanoi/puzzle cliffs.** Contested (b24, b25); do not use as a design input until the output-length confound is settled.
- **Productive failure and discovery learning** (b31, b32) are human instruction designs, not agent mechanisms. Unread.

## 10. Open questions

1. Does a forced juncture-monitoring step change solve rate or dead-end rate of a current model at equal tokens? (K01, K20)
2. Can a model choose the right heuristic per item better than chance? Is there an oracle gap worth closing? (K28)
3. Do prompt-level heuristic gains survive on current long-CoT reasoning models? Step-back and Polya-style prompts were not re-tested on them.
4. Does specialise (small cases, then conjecture) work on proofs and on reasoning models, at equal tokens? (K22)
5. What is the pooled human effect of heuristic training (Hembree 1992, IMPROVE)? Unread.
6. Does forced strategy switching help? Evidence points both ways (K23).
7. Do Gandhi's behaviours transfer from Countdown RL to maths word problems and proofs, and to scaffolding alone? (K24)
8. Is backward verification better than an extra independent sample at matched tokens on strong models? (K26)
9. How much of the maths brittleness is removed by a restate-and-strip step on reasoning models? (K25)
10. Do Brown and Walter problem-posing moves help an agent on open tasks? (K29)
11. Is the 60% to 20% wild-goose-chase drop in Schoenfeld's data real? Primary source unread (K02).
12. Does the Lawsen rebuttal (b25) overturn the Hanoi cliff? No numbers were read.

## 11. Sources

[V] opened this session; [M] snippet, abstract or recalled only.

- [V] Schoenfeld (1979) Explicit heuristic training as a variable in problem-solving performance. https://www.ime.usp.br/~alpereir/cursosdosemestre/resprob/schoenfeld_heuristics_79.pdf (d01). The ERIC abstract https://files.eric.ed.gov/fulltext/EJ202121.pdf was [M] (a05).
- [M] Schoenfeld (1980) Teaching problem-solving skills. https://files.eric.ed.gov/fulltext/EJ239376.pdf (a06)
- [V] Schoenfeld (1982) Beyond the purely cognitive. https://files.eric.ed.gov/fulltext/ED219433.pdf (a02, a03, a04)
- [M] Schoenfeld (1985) Mathematical Problem Solving (Heuristics and Control chapters). https://doi.org/10.1016/b978-0-12-628870-4.50009-8 ; https://doi.org/10.1016/b978-0-12-628870-4.50010-4 ; https://www.sciencedirect.com/book/9780126288704/mathematical-problem-solving (b26, b27, c21)
- [V] Rott (2013) Process regulation in the problem-solving processes of fifth graders. https://files.eric.ed.gov/fulltext/EJ1129557.pdf (a07 to a10; a07 and a10 are quotes inside it)
- [V] Rott and Gawlick (2014) Explizites oder implizites Heurismentraining. https://journals.ub.uni-koeln.de/index.php/mathematica_didactica/article/download/1126/1080/3141 (d02)
- [V] Kuzle (2019) Working backward strategy materials. https://files.eric.ed.gov/fulltext/EJ1239972.pdf (a12, a13)
- [M] Mevarech and Kramarski (1997) IMPROVE (cited in Rott) (a11, d04); Kramarski and Mevarech (2003) https://doi.org/10.3102/00028312040001281 (b30)
- [M] Hembree (1992) meta-analysis. https://doi.org/10.2307/749120 (b29, d03)
- [M] Begle (1979); Lester (1994). https://doi.org/10.2307/749318 (b28)
- [M] Sinha and Kapur (2021). https://doi.org/10.3102/00346543211019105 (b31)
- [M] Kirschner, Sweller and Clark (2006). https://doi.org/10.1207/s15326985ep4102_1 (b32)
- [M] Polya (1945) How to Solve It. https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it (c20); second-hand via Lee et al. 2026
- [M] Brown and Walter (1983) The Art of Problem Posing. https://www.routledge.com/The-Art-of-Problem-Posing/Brown-Walter/p/book/9780805848663 (a24, c22)
- [M] Newell and Simon (1972) Human Problem Solving. https://en.wikipedia.org/wiki/Human_Problem_Solving (a25)
- [V] Lee et al. (2026) Llama-Polya. https://arxiv.org/abs/2602.10597 (a01, a14)
- [V] Zheng et al. (2024) Take a step back. https://arxiv.org/abs/2310.06117 (a15, a16, b05, b06, c01 to c03, c19, c25)
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 (a17, a18, b15, c07)
- [V] Wang et al. (2023) Plan-and-Solve prompting. https://arxiv.org/abs/2305.04091 (a19, b14, c05, c06)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (a20, b18, c08, c09)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (a21, b19, c10, c24, d18)
- [V] Chen et al. (2025) Reverse thinking makes LLMs stronger reasoners. https://arxiv.org/abs/2411.19865 (a22, b08, c11, c26)
- [V] Jiang et al. (2024) FOBAR. https://arxiv.org/abs/2308.07758 (a23, b07, c12, d16)
- [V] Weng et al. (2023) Self-verification. https://arxiv.org/abs/2212.09561 (c13)
- [V] Gandhi et al. (2025) Cognitive behaviors that enable self-improving reasoners. https://arxiv.org/abs/2503.01307 (b01 to b04, c17, c18, d11)
- [V] Mirzadeh et al. (2025) GSM-Symbolic. https://arxiv.org/abs/2410.05229 (b09 to b11, d14)
- [V] Shi et al. (2023) Irrelevant context. https://arxiv.org/abs/2302.00093 (b12)
- [V] Chen et al. (2024) Premise order matters. https://arxiv.org/abs/2402.08939 (b13)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 (b16)
- [V] Didolkar et al. (2024) Metacognitive capabilities of LLMs in maths. https://arxiv.org/abs/2405.12205 (b17)
- [V] Wei et al. (2022) Chain-of-thought prompting. https://arxiv.org/abs/2201.11903 (b20; figure values approximate)
- [V] Kojima et al. (2022) Zero-shot reasoners. https://arxiv.org/abs/2205.11916 (c04)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b21, c14)
- [V] Lightman et al. (2024) Let's verify step by step. https://arxiv.org/abs/2305.20050 (b22)
- [V] Zhang et al. (2024) GSM1k. https://arxiv.org/abs/2405.00332 (b23)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (b24)
- [V] Lawsen (2025) The illusion of the illusion of thinking. https://arxiv.org/abs/2506.09250 (b25; no numbers)
- [V] Petrov et al. (2025) Proof or bluff. https://arxiv.org/abs/2503.21934 (c15, c16, d10)
- [V] Sun et al. (2025) Enumerate-Conjecture-Prove. https://arxiv.org/abs/2505.18492 (d05)
- [V] Meincke et al. (2025) Prompting Science Report 2. https://arxiv.org/abs/2506.07142 (d06)
- [V] Elenjical et al. (2026) Think2. https://arxiv.org/abs/2602.18806 (d07)
- [V] Silver et al. (2025) Single-utterance self-correction. https://arxiv.org/abs/2506.15894 (d08)
- [V] Wang et al. (2025) Underthinking of o1-like LLMs. https://arxiv.org/abs/2501.18585 (d09)
- [V] Weston and Sukhbaatar (2023) System 2 Attention. https://arxiv.org/abs/2311.11829 (d12)
- [V] Rajeev et al. (2025) Cats confuse reasoning LLM. https://arxiv.org/abs/2503.01781 (d13)
- [V] Zhao, Awasthi and Gollapudi (2025) Sample, scrutinize and scale. https://arxiv.org/abs/2502.01839 (d15)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393 (d17)
- [V] Zhao et al. (2025) Absolute Zero. https://arxiv.org/abs/2505.03335 (d19)
