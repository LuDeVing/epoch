# Resilience engineering: deep document

*Subfield E13.08. Written from evidence_a-d.jsonl, claims.jsonl (K01-K25) and critique.md in this folder. Evidence ids (a01, b05, d03 ...) point to lines in the evidence files. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Short version: the field gives us a vocabulary and a few good questions. It gives us almost no tested effect sizes. The useful numbers come from LLM agent studies that borrow its words.*

## 1. What it is

Resilience engineering studies how complex systems cope with surprise. It started in safety science. It treats accidents as a failure of adaptation, not as "human error". People work under finite resources, goal conflicts and time pressure. They trade off. Most of the time the trade-offs work. Sometimes they do not. (a01, a04)

Two lists carry most of the field.

**Hollnagel's four potentials.** A resilient system can:
- respond to what happens,
- monitor critical developments,
- anticipate future threats and opportunities,
- learn from past events, including successes.

Hollnagel says they must be seen together. A Resilience Assessment Grid asks questions per potential. No validation data for the grid was found. (a01, a20; a20 not opened)

**Woods's three patterns of adaptive breakdown.** (a02, a19, b21, b22)
- *Decompensation.* Automatic compensation hides a growing disturbance until the compensating capacity runs out. Then the system collapses fast.
- *Working at cross purposes.* Each unit acts in a way that is locally adaptive and globally maladaptive.
- *Stuck in outdated behaviour.* The world changes. The system keeps a strategy that used to work. Related patterns from the EUROCONTROL report: failure to revise assessments as evidence accumulates, and taking past success as a reason for confidence. (b22)

Woods also names four concepts of resilience (a13): rebound from trauma, robustness (handling anticipated disturbances), graceful extensibility (extending capacity when surprise hits the boundary), and sustained adaptability (adapting over long periods).

Why it matters for our agent. The schema (S6 impasse, S9 look back) already borrows two ideas: look back at what happened, and notice when you are stuck. This subfield asks which of the borrowed ideas have numbers behind them. Answer: few. The three Woods patterns are descriptive. No rate, no controlled test, no timing prediction was found. (K01, K20)

## 2. History and theories in depth

**Roots (before 2004).**
- Rasmussen (1997) drift model: work practices migrate under economic and workload pressure toward the edge of acceptable performance. (a22, not opened; known through citing papers)
- Carlson and Doyle (2000) "highly optimised tolerance": systems tuned for designed perturbations are robust to those and fragile to unexpected ones. Woods cites this as the formal root of "robust yet fragile". It is the closest thing to a mathematical model under the field, and it comes from outside the field. (a23, a04; not opened)
- Competing traditions: Perrow's normal accident theory, high-reliability organisations, Reason's error model, Amalberti's "paradox of almost total safety". (a24, not opened)
- Westrum (2004) typology of cultures: pathological, bureaucratic, generative, by how information flows. Descriptive. The author says evidence is not definitive. (a10, abstract only)

**Founding events.**
- First symposium: October 2004, Soderkoping, Sweden, 14 researchers. Second: November 2006, Sophia Antipolis, 80 participants. Volume: Woods, Hollnagel and Leveson (eds) 2006 "Resilience Engineering: Concepts and Precepts". (a01, a21)
- Woods and Branlat (2011) "Basic patterns in how adaptive systems fail" gives the three patterns, from healthcare, mission control, military operations and urban firefighting. Not opened (403). (a19, b21)
- Hollnagel, Paries, Woods and Wreathall (2011) "Resilience Engineering in Practice". Hollnagel (2014) "Safety-I and Safety-II". Not opened. (a20)

**Theory development.**
- Woods (2015) four concepts of resilience. Paywalled; read through citing papers. (a13)
- Woods (2018) theory of graceful extensibility: 10 proto-theorems in 3 subsets. Subset A (S1-S3) manages risk of saturation. B (S4-S6) covers networks of adaptive units. C (S7-S10) covers outmanoeuvring constraints. Key claims: every unit has bounds; events occur outside the bounds; no single unit is enough; neighbours can monitor and shift each other's capacity; behaviour near saturation differs from behaviour far from it. The theory is verbal, not mathematical. Primary text closed access. (a05, d14)
- Cook and Rasmussen (2005) "going solid": hospitals were loosely coupled and absorbed surges. Efficiency drives removed the buffers. Then one area depends on small events in distant areas. Conceptual; abstract only read. (a09)
- Woods (2019) lecture slides: SNAFU is the natural state; people are hidden SNAFU catchers who supply extra adaptive capacity; optimising for known conditions raises brittleness. Cases: high-frequency trading, a 27 April 2018 exchange outage, NASA "faster, better, cheaper". Selected stories, no base rates. (a02-a04)

**Application and critique (2020-2025).**
- Iflaifel et al. (2020) systematic review of resilient health care: 872 records, 74 full texts, 36 included; mostly qualitative; no intervention effects measured; five studies built on the four capabilities. (b12)
- Braithwaite et al. (2024) synthesis of 8 case studies into four themes: responsiveness, adaptiveness, local adoption of policy, interventional consequentiality. Authors belong to the network that wrote the sources. (a11, a12)
- Herrera, Praetorius, Degerman, Wiig (2025) 20-year review: resilience moved "from a property (2004) to a verb (2024)". Empirical work began only about 2015. Calls for evidence that measures improve work as done. (b14)
- Cooper (2022) critique "The Emperor has no clothes": no peer-reviewed proof that Safety-II or resilience ideas cut injuries. A Safety-I advocate; injuries not complex-system anomalies; contested. (b13)
- Moerman et al. (2022): first empirical pattern test of the proto-theorems, one train case. See section 3. (a06, b11)

**Where the field meets LLM agents.** Two preprints apply Woods's vocabulary directly: Liu et al. (2026) turn rebound, stability and graceful extensibility into metrics for embodied agents (a16), and a 2026 FRAM/STPA analysis of a coding agent finds four resonance patterns (c24). A search found no other study applying graceful extensibility or Safety-II to LLM agent evaluation (c28, snippets only). Much other agent work uses the same ideas without the words: failure taxonomies (MAST), loop detectors, reliability metrics (pass^k), learn-from-failure memory (Reflexion, Sentry, EDV).

## 3. Core findings with exact numbers

Status here is evidence status, not theory status. "Single" means one independent source group.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Woods's three patterns are case descriptions, no rates | NASA 1999 (3 failures), Columbia 2003, urban firefighting; no counts | Woods 2019 slides, Woods and Branlat 2011 (a02, a19, b21) | [S] single source, descriptive |
| Only quantitative test of graceful extensibility: one train case | 21 of 24 sub-patterns matched; 176 coded items; subset shares 31% / 46% / 23%; S1 and S8 2% each, S6 18%; no evidence for base vs extended capacity (S7.1); one coder | Moerman et al. 2022 (a06, b11) | [S] pattern matching, not a test |
| Cockpit talk changed after autopilot disconnect (AF447) | 3 agents; 3-person events 10% normal vs 61% emergency; about 268 vs 177 events (garbled table) | David and Schraagen 2018 (a08) | [S] preliminary, one incident |
| Simulation before opening found latent threats | 37 latent safety threats in 24 sessions (8 centre, 16 in situ); no control | Braithwaite et al. 2024 (a12) | [S] no control |
| Evidence base for RE as an intervention is thin | review: 36 included studies, no intervention effects; empirical work from about 2015; critic says no peer-reviewed proof | Iflaifel 2020, Herrera 2025, Cooper 2022 (b12-b14) | [E] three sources agree it is thin |
| Success rate hides recovery behaviour | Reflexion 56.3% vs CoPAL 55.8% success; recovery cost 57.3 vs 11.9 (4.8x); ReAct 38.5% success, lowest cost 6.5; cost rises with perturbation (Spearman 0.82); physical perturbation 11.6 to 36.3 | Liu et al. 2026 (a16, b17, c21) | [S] one author group, own metrics |
| Resilience aspects trade off | extensibility fix: recovery cost 36.70 to 99.59 (+171%); rebound fix 59.11 to 33.73 (-42.9%); stability fix 51.01 to 43.01; step instability 0.3185 to 0.2552 | Liu et al. 2026 (a17, b18, c22) | [S] |
| Agents solve tasks inconsistently | gpt-4o retail pass^1 61.2, airline 35.2, pass^8 below 25% (retail); outcome consistency about 0.52-0.86 across 15 models (read from garbled figure); gpt-4.1 pass^1 74/56/34% retail/airline/telecom, pass^k falls with k | tau-bench, Rabanser 2026, tau2-bench (b05, b03, d11) | [E] three sources |
| Capability gains bring small reliability gains | 15 models, 2 benchmarks, 12 metrics, about 24 months; small gain, tau-bench moderate, GAIA barely | Rabanser 2026 (b01) | [S] authors note benchmark difficulty may explain |
| Tool faults are easy, paraphrase is hard | fault injection p=0.2, 5 paraphrases, medium format change; fault and format robustness near ceiling; prompt paraphrase the main differentiator | Rabanser 2026 (b02) | [S] ceiling effect |
| Multi-turn loss is unreliability | 39% average drop, 200,000+ conversations, 6 tasks; aptitude loss about 15%; unreliability +112%; CONCAT keeps 95.1% of FULL; RECAP and SNOWBALL stay below FULL; temp 0 no help for GPT-4o-mini sharded, GPT-4o +15-20% | Laban 2025 (b08, b09) | [S] simulated user, generation tasks |
| Blind self-correction hurts older models | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GSM8K 75.9 to 75.1 to 74.7; GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-4 CommonSenseQA 82.0 to 79.5/80.0; Llama-2 GSM8K 62.0 to 43.5 to 36.5; GPT-4 HotpotQA flat in round 1 | Huang et al. 2024 (b10, c10) | [E] with d02, d03, d10 |
| Oracle feedback helps | GPT-3.5 GSM8K 75.9 to 84.3; GPT-4 HotpotQA 49 to 59 | Huang 2024 (c10) | [E] |
| Newer models gain little blind | o3-mini +3.4 pp, Claude Opus 4.6 +0.6, o4-mini 0, GPT-5 and 4 others lost; verify-first GPT-4o-mini error introduction 2% to 0%, -6.2 to +0.2 pp (McNemar p<1e-4) | Liu and Meng 2026 (c09, abstract only) | [C] abstract only |
| Blind self-verification breaks answers | single check breaks 10.9% of correct, fixes 6.2% of wrong; any-vote 21.4% / 8.1%; unanimous 6.0% / 3.5%; locate-first-wrong-step with confidence exit net +3.9% (2.5% broken, 6.4% fixed); without exit -49.3%; 8 open models 3B-120B, 6 datasets | Thought-ICS (d03) | [C] open models only |
| Blind review across five non-thinking models | 1,340 problems; 342 worsened vs 233 improved, net -2.1%; cause: false problem identification 69.6%; e.g. DeepSeek-V3 67.02 to 62.83 | MatSciBench (d10) | [S] domain-specific |
| Strong model fixes least of its own errors | N=500 each; DeepSeek-Chat 94.0% acc, fixes 16.7% (5/30); GPT-3.5 66.4%, 26.8% (45/168); Claude-3-Haiku 70.4%, 29.1% (43/148); detect own error 56.7 / 81.5 / 10.1% | Decomposing self-correction (d02) | [S] three models, small error counts |
| Debate does not beat sampling | GSM8K GPT-3.5: self-consistency 82.5 (3), 85.3 (6), 88.2 (9); debate 83.2 (6), 83.0 (9); standard 76.7 | Huang 2024 (c11) | [S] here; [E] in SCHEMA G9 with other sources |
| Repetition and loops are a leading failure | MAST step repetition 15.7% (paper) vs 40.4% of 1642 traces (released data); unaware of termination 12.4%; LoopBench worst 62.00% (17.14% numeric, 44.86% statement), gemini-2.5-pro 7.43%, AIME25 max 10.0%; MIRAGE utility 0.57-0.63 after 3 or 6 repeats | Cemri 2025, d01, LoopBench, MIRAGE (b06, c02, c16, c07, d01) | [E] four sources |
| MAST category split depends on version and unit | paper: 44.2/32.3/23.5 (Figure 1) or 41.8/36.9/21.3 (later figure); released data by mode 37.0/33.3/29.9; by trace 58.1/53.3/55.2; 1237 of 1642 traces with at least one mode; failure rates by system 41%-86.7%; kappa 0.88 human | Cemri 2025 + recount (c01-c04, d01) | [S] cite version and counting unit |
| Verification step helps; prompt fixes help little | role spec +9.4% (ChatDev, GPT-4o); objective verification step up to +15.6% (ProgramDev); modes: incorrect verification 9.1%, none 8.2%, premature termination 6.2% | Cemri 2025 (b07, c05, c04) | [S] small sets, easy task |
| LLM annotator can label traces | few-shot accuracy 0.94, kappa 0.77, F1 0.80; zero-shot 0.89, kappa 0.58; out-of-domain kappa 0.79 | Cemri 2025 (c06) | [S] |
| LLM loop monitors are contested | repetition Jaccard 0.367 to 0.176 (-52%) on one task; overall +0.014 +/- 0.723; probe d +0.471 +/- 0.893 vs LLM +0.047 +/- 0.658; layer 28 AUROC 0.84 on 35 examples; 1B-1.5B models 0.000 change; overhead about 11% | Cognitive Companion (c13-c15) | [C] tiny runs |
| Hidden-state loop onset detection works early | CUSUM on probe: early detection 0.64-0.76, false positive 0.24-0.34, lead 36-52 sentences (about 1,300-1,900 tokens); without persistence false positives 0.40-0.62; 7B model loops 92.07% at T=0.1 | LoopBench (c16, c17) | [S] needs open weights |
| Failure layer changes behaviour | paired local recovery 33.5% to 60.5% on 200 forks; 85.8% of 113 interventions helpful; tokens 1.54x base; WebShop reward 0.170 to 0.468 (rule-based 0.258); AppWorld 25.59 to 38.53 (rule-based 25.09); SWE-bench Lite 0.20 to 0.30 | Sentry (d04, d05, d16) | [S] Qwen3.5-9B, own setup |
| Ungated trigger hurts | removing need-check: WebShop 0.468 to 0.136, AppWorld 38.53 to 23.70; interventions 227 to 347 and 187 to 310; progress failures recover least (64.0%; 34.0% on SWE-bench Lite) | Sentry (d05) | [S] |
| Incident rules cut repeats | incidents 54 to 6 to 0 (code), 67 to 5 to 2 (embodied), 8 to 1 to 0 (computer use); 9, 11, 6 rules; 0 of 50 and 0 of 35 false positives; detection, remediation, eradication above 90% | AIR (b16, c19) | [S] own task sets, no baselines |
| Self-invented remedy loses to rule-specified | embodied 80.95% vs 92.31%, 28.7 s vs 22.2 s; computer use 76.60% vs 97.73%, 34.6 s vs 25.9 s | AIR (c20) | [S] no replication |
| Written lesson does not beat raw transcript | 75 BugsInPy bugs, 181 failed attempts; plain 29.8%; HISTORY +9.4 [-0.5,+18.9]; REFLECT +7.2 [-2.3,+17.4]; BOTH +9.9 [+1.5,+19.1], Holm p 0.17; lesson minus transcript -1.7 [-8.7,+4.9]; replication gpt-5.4, 85 failures: plain 43.5%, HISTORY +10.6 [-8.9,+29.3] | Repair-agent study (d06) | [S] same 75 tasks |
| Unverified lessons store the agent's own errors | tau2-bench pass@1: no memory 76.4, self-reflection 77.7, RB-MaTTS 82.3, EDV 86.6; trap rate 22.0% / 16.0% / 11.0% / 5.0% | EDV (d08) | [S] no significance tests |
| Verified memory beats write-all | ALFWorld 402 held-out, Qwen3.5-27B: ReAct 61.19, write-all 73.38, magnitude test 74.88, Anchor 96.27; Qwen2.5-14B 87.06 vs 72.64; WebShop 73.50 vs 62.74; 41% fewer cards | Anchor (d09) | [S] needs log-probs |
| Fetch lesson on failure beats always-in-context | held-out WebShop: no playbook 0.251, frozen 0.364, always in context 0.296, full Sentry 0.495; Mind2Web 0.533 / 0.651 / 0.599 / 0.729 | Sentry (d15) | [S] |
| Reflexion has a boundary | AlfWorld 130 of 134 tasks in 12 trials; ReAct-only plateaued at trials 6-7 with hallucination near 22%; WebShop no gain after 4 trials; HumanEval 91% vs 80% | Reflexion (d13, c27) | [E] boundary documented in the primary paper |
| Memory from successes and failures helps | WebArena +8.3, +7.2, +4.6 points over no-memory across three backbones; up to 2.1 fewer steps (26.9% relative); 17.1% to 24.1% compact setting | ReasoningBank (d12) | [S] LLM-judge labels |
| Learned control-flow update at a recurring decision | AppWorld Test-Normal n=168: 13.7% to 79.2% (110 improved, 0 regressed); Test-Challenge n=417: 6.7% to 70.0% (270 improved, 6 regressed); same instruction at first step solved 5 of 16 dev tasks, at the recurring step 14; no update accepted in six other domains | EvoCUE (d07) | [S] one model, one fix |
| Root-cause step feedback | +17% step accuracy, +24% all-correct accuracy, up to 26% relative task gain | AgentDebug (c26) | [S] abstract only |
| Time to recover is not quality of recovery | 200 semi-simulated runs; median 6.21 s (SD 2.14, P90 10.73); tool-retry 4.46 s (n=42), auto-replan 5.94 (n=93), rollback 6.99 (n=44), human-approve 12.22; about 8% of runtime | MTTR-A (b15, c18) | [S] synthetic |
| Redundancy raises resilience to random failure | error rates 0 to 1; resilience = area under accuracy-vs-error curve; more agents and links help; cost rises | ResMAS (b19) | [C] random failures, not cognitive |
| LLM agents adapted where PPO agents did not | Commons Harvest, 9 apple-removal scenarios, 5 episodes; LLM above RL in all 3 bot experiments | Cooperative resilience 2024 (c23) | [S] preliminary |
| Livelock and text-action gap | 3 or more identical consecutive tool calls flagged; 4 scenarios, 7 models; turns capped at 10 | Yu et al. 2026 (b20) | [S] tiny sample |
| Experts do worse in unexpected situations | ship crews, 3 experience groups; most experienced best overall, poor in unexpected cases | Bergstrom 2009 via a15 (a25) | [S] second-hand |
| Failures emerge in operation, not in trials | V250 services cancelled after 2 months; TRAXX failures emerged after one week | Moerman 2022 (a07) | [S] case |

## 4. Mechanisms and models

These are written so an engineer could build them. All are code-side. None needs the model to judge itself (G1, G5, G10).

### 4.1 Capacity, saturation and decompensation (Woods)
Model: each unit has a range of adaptive capacity with a boundary. Demand rises. Compensation hides the rise. When demand passes the boundary the unit saturates and fails fast. Woods gives no formula and no unit of measure. (a03, a05)

Agent reading (our own, untested): "capacity" is the remaining budget plus the room to change approach. Decompensation looks like a run where every step keeps working around a growing error (patches, retries) until the budget is gone. Observable signals a program can count: patches per step, distance between the current output and the last passing one, tokens left. No source tests this. (K01)

Implementation sketch: log tokens used, rounds used and number of distinct operators tried. Flag "saturation risk" when more than half of budget is gone and no check has improved. This is a design choice [D].

### 4.2 Stuck in outdated behaviour = repetition detector (S6)
Evidence that the failure is common: MAST step repetition 15.7% (paper) to 40.4% (released traces); LoopBench 62.0% for a 7B distilled model, 7.43% for gemini-2.5-pro; MIRAGE agents keep the failed action after 3 or 6 repeats. (b06, d01, c16, c07)

Detector options, cheapest first:
1. Hash each tool call or each candidate answer. Fire on the same hash twice, or 3 identical consecutive calls (the livelock rule in b20 and AgentGuard in d05: same action 3 times, no-progress rate above 0.75).
2. A no-progress counter: no change in check result for 2 rounds.
3. An LLM monitor. Result: mean effect about zero over tasks (+0.014 +/- 0.723), 11% overhead. (c13)
4. A hidden-state probe plus CUSUM with a persistence rule. Early detection 0.64-0.76 at false positives 0.24-0.34. Needs open weights. (c17)

Gate it. Sentry shows an ungated trigger drops reward (0.468 to 0.136). Fire only when a need-check says the agent is not progressing. (d05)

Response: the trigger must lead to a different operator, not a note. Reflexion stalls where success needs varied exploration (WebShop, no gain after 4 trials). (d13)

### 4.3 Monitor and fetch pattern (Sentry-style loop)
Outside the agent: detect repeat or stall, fetch the one lesson matching the failure type, inject it, check whether the next step changed, store the lesson only if recovery worked. Paired local recovery 33.5% to 60.5% at 1.54x tokens. Fetch-on-trigger (0.364 frozen playbook, 0.495 full) beat playbook always in context (0.296). (d04, d15, d16)

### 4.4 Gated lesson memory (S9)
- Write only after a check: verified lessons (EDV, Anchor) avoid storing the agent's own errors (trap rate 22.0% self-reflection vs 5.0% EDV). (d08, d09)
- Keep the raw failed attempt as an option. A written lesson did not beat re-reading the transcript (-1.7 [-8.7,+4.9]). (d06)
- Retrieve on a trigger, not by default. (d15)
- Promote a lesson only after it helps on two different problems (already in SCHEMA section 5).

### 4.5 Located-failure revise (S5), not blind review
Blind "check your answer" breaks 10.9% of correct answers and fixes 6.2% of wrong ones. Locating the first wrong step by code, resampling from the clean prefix, and exiting when confidence is high gave net +3.9%. Without the exit -49.3%. Mechanism: the exit protects correct answers. (d03) Verify-first prompts reduce harm on older models (error introduction 2% to 0%). (c09)

### 4.6 Recovery cost metric
Recovery cost = extra steps (or tokens) spent after a failed check, among eventually successful runs. It separates arms with equal accuracy: 57.3 vs 11.9 at 56.3% vs 55.8% success. It moves with stress (Spearman 0.82) and trades off against stress capacity. (a16, a17) Time to recover (MTTR-A) is a weaker metric: speed without correctness. (b15)

### 4.7 Consistency: pass^k
pass^k is the chance that all k repeated trials succeed. A scaffold may keep pass@1 and still be erratic. Report both. (b05, d11)

### 4.8 Input hygiene and restatement (S1)
Laban's CONCAT keeps 95.1% of full-prompt score. Incremental turns lose 39%. So give the full task each round. RECAP and SNOWBALL recover only part. (b08, b09)

### 4.9 Incident rule loop (AIR)
Detect an incident in code, contain or recover by a rule-specified step, then write a guardrail rule that blocks the same class. Rule-specified remedy beat the agent's own invented remedy (92.31 vs 80.95; 97.73 vs 76.60). Rules were tested on the distribution they were learned from. (b16, c20)

### 4.10 What the field's mechanisms predict but nobody tested
Drift (Rasmussen), going solid (Cook and Rasmussen) and loss of buffers predict that steps per solved item rise as slack is removed. No test exists for LLM agents. (K18) We can check it on our long logs.

## 5. What holds up

**Replicated or agreed by several independent sources.**
- Success on one clean run says little about repeated behaviour: tau-bench, tau2-bench, Rabanser, Laban agree. (K06 [E])
- Blind self-correction does not help and often hurts models up to 2024-25 generation: Huang, Decomposing self-correction, Thought-ICS, MatSciBench agree. (K08 [E])
- Loops and repetition are a leading failure class: MAST, MAST-Data recount, LoopBench, MIRAGE, Yu et al. (K10 [E])
- The empirical base of resilience engineering is thin: three reviews and critiques agree. (K02 [E])
- Reflexion's boundary: gains need a clean signal between trials and varied exploration. (K24 [E])
- Simple prompt-level patches give partial recovery only (MAST +9.4%, RECAP below FULL). (K12 [E])
- No controlled LLM test of Woods's four potentials or three patterns exists. (K20 [E])

**Failures, boundary conditions and corrections.**
- MAST totals depend on version and counting unit. Paper splits 44.2/32.3/23.5 and 41.8/36.9/21.3 are both in print. Recount of the released data: 37.0/33.3/29.9 by mode; 58.1/53.3/55.2 by trace. Step repetition 15.7% in the paper, 40.4% in the data. Cite version and unit. (d01)
- GPT-4 CommonSenseQA fell only from 82.0 to 79.5 and 80.0, and GPT-4 HotpotQA was flat in round 1. "Self-correction collapses accuracy" is mostly a GPT-3.5 and Llama-2 result. (b10 with critique)
- Newer models: o3-mini +3.4 pp, Opus 4.6 +0.6, others lose (abstract only). No frontier reasoning model was tested in blind review mode in the sources opened. (c09, d17) Contested for 2026 models.
- Accuracy-correction paradox: the strongest model (94.0%) fixed 16.7% of its own errors, weaker models 26.8% and 29.1%, but only 30 errors for the strongest. (d02)
- LLM monitors: one task -52%, mean zero, 1B-1.5B models no effect, probe trained on 35 proxy-labelled examples. (c13-c15)
- Rule-based detector (AgentGuard) +52% on WebShop and nothing on AppWorld; Sentry's LLM detector did better but was never ablated against code. (d05)
- Written lessons: transcript beat lesson by 1.7 points (not significant). Detecting a 7-point effect needs about 100+ tasks. Held-out transfer shown once (Sentry, 50 to 50 tasks). (d06, d15)
- EvoCUE: one learned instruction raised AppWorld from 13.7% to 79.2%, yet no update was accepted in six other domains. A fix tied to one recurring decision. (d07)
- Resilience trade-offs: fixing graceful extensibility raised recovery cost +171%. (c22)
- Tool-fault robustness is near ceiling; paraphrase is the live weakness. (b02)
- Redundancy helps against random failures (ResMAS) but G9 and Huang say debate does not beat sampling at matched cost. Both can hold: different measurements. (K16)

**Interventions that worked (with caveats).**
- Verification step: +15.6% ProgramDev (easy task). (b07)
- Located-failure revise with confidence exit: net +3.9%. (d03)
- Failure-triggered lesson fetch: recovery 33.5% to 60.5%. (d16)
- Verified memory: ALFWorld 96.27% vs write-all 73.38%. (d09)
- Rule-specified remediation over self-invented. (c20)
- Feedback-guided recovery: recovery cost 59.11 to 33.73. (b18)

**Interventions that did not work.**
- Blind review. Prompt-only role changes (+9.4% only). Ungated triggers. LLM monitors on small models. Debate. Unverified self-written lessons. Lowering temperature in multi-turn (no gain for GPT-4o-mini sharded).

## 6. Language models

**Failure behaviour.**
- Multi-turn: 39% average drop, mostly unreliability (+112%), aptitude -15%. (b08)
- Consistency: low across 15 models; same action types, different order. (b03)
- Loops: 7B distilled reasoning model 62.0%; gemini-2.5-pro 7.43%; at T=0.1 the 7B model reached 92.07%. Standard benchmarks show low loop rates (AIME25 max 10.0%). (c16)
- Repetition after 3 or 6 failed repeats: utility 0.57-0.63 for strong and 7B models alike (GPT-4o 0.572, Claude-3.7-Sonnet 0.624, Qwen2.5-7B 0.595). (c07, c08)
- Multi-agent traces: failure rates 41% to 86.7% by system. (c01)
- Safety drift: refusal in text then unsafe action; tiny sample. (b20)
- Rule violations on tau-bench fell for newest models; wrong charges or refunds stayed the most common. (b24)

**What changed behaviour, by how much.**

| Change | Effect | Source |
|---|---|---|
| Outside feedback (oracle) vs blind | GSM8K 75.9 to 84.3 vs 75.1 | b10, c10 |
| Verify-first prompt | GPT-4o-mini -6.2 pp to +0.2 pp | c09 |
| Locate first wrong step + exit | net +3.9% vs -49.3% without exit | d03 |
| Full-task restatement (CONCAT) | 95.1% of FULL vs a 39% average drop when split over turns | b08 |
| Objective verification step | +15.6% (ProgramDev) | b07 |
| Failure trigger plus lesson fetch | recovery 33.5% to 60.5% | d16 |
| Verified memory | ALFWorld 73.38 to 96.27 | d09 |
| Gate on lesson writing | trap rate 22.0% to 5.0% | d08 |
| Rule-specified remedy | +11.4 and +21.1 points over self-invented | c20 |
| Feedback-guided recovery | recovery cost 59.11 to 33.73 | b18 |
| Retrieval on failure vs always in context | WebShop 0.296 to 0.364 (frozen) | d15 |

**Model-scale boundary.** LLM monitor did nothing for 1B and 1.5B models. Self-correction gains appear for a few newer models and not others. (c15, c09)

**Evidence quality.** Almost every agent number above comes from the authors' own benchmark, simulated users or LLM judges (tau-bench simulated users; MAST judge kappa 0.77; MIRAGE judge; Liu et al. LLM judge). Preprints from one group: Liu et al., AIR, Cognitive Companion, MTTR-A, Sentry. None replicated. (critique)

**Not tested in LLMs at all:** Hollnagel's four potentials as an intervention; Woods's decompensation timing; drift and buffer loss. (K20, K18)

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Nothing here is a new element. Items map onto existing schema parts and mostly confirm or sharpen them.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Do not import resilience-engineering interventions on authority. Admit an element only if it wins at equal tokens. | G7 | [E] | K02; b12-b14 |
| 2 | Report pass^k beside pass@1 for every arm. One clean run is not robustness. | G4, section 6 log | [E] | K06; b05, b03, b08, d11 |
| 3 | Revise only from real located output. Do not add blind "review your answer" passes. (Already G2 and section 4b; evidence now larger.) | G2, S5 | [E] | K08; b10, c10, d02, d03, d10 |
| 4 | Repetition is a top failure class, so keep a code-side repeat counter (hash of attempt or tool call, repeat 2x or 3x) feeding S6. Prefer code to an LLM monitor (G5). | S6 | [E] that the failure is common; trigger design [D] | K10; b06, c07, c16, d01 |
| 5 | A prompt-only patch is unproven until it beats plain at equal tokens. | G7 | [E] | K12; c05, b07, b09 |
| 6 | At an impasse require a different operator, not only a note about the failure. | S6, O1-O8 | [E] boundary documented | K24; d13 |
| 7 | Treat Woods's four potentials and three patterns as vocabulary for labelling our logs, not as a tested model. | none | [E] | K20; K01 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 8 | Log recovery cost (extra tokens and steps after a failed check) as a metric that separates arms of equal accuracy. | S9, section 6 | [S] | K04; a16, b17, c21 |
| 9 | Gate S9 lesson writes behind a check; fetch lessons at the S6 trigger only. | S9, M | [C] | K22, K14; d06, d08, d09, d15 |
| 10 | Located-failure S5 with a confidence exit versus blind review. | S5 | [C] | K21; d03, d10 |
| 11 | Code-side S6 trigger versus LLM trigger; measure fire rate, fire step and change rate. | S6 | [C] | K13, K23; c13, c17, d05, d16 |
| 12 | Final objective-level S8 check. | S8 | [S] | K11; b07, c05 |
| 13 | S1 full-task restatement each round instead of incremental feedback. | S1 | [S] | K07; b08, b09 |
| 14 | Paraphrase robustness: 3 paraphrases per item, answer agreement. | S1 | [S] | K17; b02 |
| 15 | Rule-specified remedy vs self-invented remedy at S6. | S6, O | [S] | K14; c20 |
| 16 | Stored-lesson reuse on held-out items of the same class. | M | [C] | K14, K22 |
| 17 | Drift check: steps or tokens per solved item across a long session. | G7, S9 | [S] | K18 |
| 18 | Label stuck-run traces with Woods's three patterns and count. | S6 | [S] | K01, K20 |

## 8. Concrete tests on our bench

Every test: two arms at equal total tokens (setup, monitors and extra calls counted). Report pass@1, pass^k (k=4 at least), tokens, and a flip table (right-to-wrong, wrong-to-right). Use items with a check where possible. Item sets: our ARC subset, BrainTeaser-style puzzles, and the nano loop problems. Seeds fixed; same items in both arms. For a 7-point effect plan 100+ items (d06 gives the sample-size warning).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Impasse trigger audit: our existing traces, no new runs | log only: fire rate of "same error twice" and "no change for 2 rounds"; fire step; change rate after operator | fire rate; median fire step as share of budget; output-change rate | change rate near Sentry's 60.5%; if fire step is late (past 70% of budget), the trigger is worthless |
| T2 | Items that have a check and a first failure | A: S5 revise with located failing output. B: blind "review your answer" at same tokens | net flips (wrong-to-right minus right-to-wrong); accuracy | A net positive, B net negative or zero (Thought-ICS: -49.3 vs +3.9 for the exit) |
| T3 | Same items | A: located revise with confidence exit (stop when answer matches the check or all attempts agree). B: located revise with no exit | right-to-wrong count | exit lowers right-to-wrong; confirm the 2.5% vs large-loss pattern |
| T4 | Mixed items, 4 repeats each | A: plain. B: scaffold, same tokens | pass^4 and pass@1 | scaffold pass^4 gain larger than pass@1 gain, or no reason to keep it |
| T5 | Items where plain fails once | A: code repeat trigger (hash, 2x). B: LLM monitor call at each round. C: no trigger | change rate; accuracy at equal tokens; extra token share | A at least equal to B at lower cost (Cognitive Companion average about zero; overhead about 11%) |
| T6 | Failed attempts on problem class X, test on held-out items of class X | A: no memory. B: raw failed transcript. C: written lesson, ungated. D: verified lesson fetched at trigger | held-out accuracy; trap rate (lessons that restate the agent's own error) | D beats C and B; B at least equals C (d06: -1.7) |
| T7 | Sequential run on 100 items | A: plain. B: scaffold | tokens per solved item over item index; slope | no rising slope in B; if slope rises, drift or buffer loss is real |
| T8 | Items with an objective check available | A: final S8 objective check then one revise. B: no final check, same tokens | caught wrong answers; accuracy | A +5 to +15% on items where plain errs (MAST +15.6% on an easy task) |
| T9 | Same items, 3 paraphrases each | plain vs scaffold | answer agreement across paraphrases; accuracy | scaffold agreement not lower than plain; plain paraphrase swing visible (b02) |
| T10 | Failed runs | A: operator forced different from last. B: lesson note then same operator allowed | share of stuck runs that change approach; solve rate | A higher change rate and solve rate than B |
| T11 | Recovery cost | both arms from T2/T4 | extra tokens after first failed check among eventual successes | different arms with equal accuracy show different recovery cost; if not, the metric adds nothing |
| T12 | Stuck traces | hand label 50 stuck runs: decompensation, outdated behaviour, cross purposes (multi-call only), other | label counts; inter-rater agreement | if "other" over 40% or kappa under 0.6, drop the mapping |

## 9. What does not transfer, and why

- **Cross purposes and networks of adaptive units (proto-theorems S4-S6).** They need several units with different goals. Our agent is one agent. The "inter-agent" part of MAST (32.3% to 36.9%) applies only if the scaffold uses several role-bound calls. A single scaffold with fresh-context attempts is not a team. (c03, K16)
- **Redundancy and topology (ResMAS).** Failures there are random agent failures. Our failures are correlated, cognitive ones, and G4 says samples from one model are not independent. (b19)
- **Human organisational culture (Westrum), safety culture, simulation in a hospital.** No mechanism that maps to a prompt. Evidence is case counts without control. (a10, a12)
- **Time metrics (MTTR-A).** Semi-simulated, speed only. (b15)
- **Graceful extensibility theory as a model.** One coded case, one coder, 21 of 24 matches. No prediction we can check. (a06)
- **Hidden-state probes (CUSUM, probe monitors).** Need open weights; probes trained on 35 proxy-labelled examples. Not usable on a closed API model. (c14, c17)
- **Human "SNAFU catchers" and adaptation under hours of fatigue.** Our agent has no fatigue; its limits are context and budget.
- **Large lift numbers from author-built agent benchmarks** (EvoCUE 13.7% to 79.2%, Anchor 96.27%). Baselines are weak, tasks are narrow, and one instruction fixed one failure. Do not expect these sizes. (d07, d09)
- **Resilience framing itself.** No study shows that using the words changes agent behaviour. Only the mechanisms (trigger, check, gated memory) have numbers. (K20)

## 10. Open questions

1. Does the S6 trigger fire early enough, and does the chosen operator change output? Nobody reports fire timing. (Gap 1)
2. Does a scaffold raise pass^k at equal tokens, or only pass@1? No source tests it. (Gap 2)
3. Is code-side loop detection at least as good as an LLM monitor or probe? No ablation exists. (Gap 3)
4. Do 2026 frontier reasoning models still lose accuracy under blind review? Only abstract-level evidence. (Gap 4)
5. Does a written lesson, reused later, cut repeat failures on held-out problems? Does a self-invented remedy lose to a rule remedy outside the AIR authors' tasks? (Gap 5)
6. Does recovery cost separate arms with equal accuracy on our data? (Gap 6)
7. Do the primary texts (Woods 2018, Woods and Branlat 2011, Hollnagel's grid) state testable timing predictions for decompensation? Closed or blocked. (Gap 7)
8. Do the three Woods patterns separate cleanly in single-agent traces, or collapse into loops and stale assumptions? (Gap 9)
9. Does stress or long-run drift appear for our agent, as Rasmussen and Cook predict? (Gap 10)
10. Which MAST split is right? Recounting shows it depends on version and unit; label by version. (Gap 8, closed with caveat)
11. How much of the Sentry-type gain survives on a strong model? All results use Qwen3.5-9B or similar bases that start weak (WebShop 0.17).

## 11. Sources

[V] = opened and read this session (full text or substantial part). [M] = abstract, snippet or secondary only.

**Resilience engineering, theory and cases**
- [V] Wikipedia, Resilience engineering. https://en.wikipedia.org/wiki/Resilience_engineering (a01)
- [V] Woods (2019) Outmaneuvering complexity in worlds of surprise, Carderock lecture slides. https://faculty.nps.edu/dlalders/docs/Woods-Carderock-Complexity-2019.pdf (a02-a04)
- [V] Moerman, Pilot, Kroes et al. (2022) Graceful extensibility in asset management. https://link.springer.com/content/pdf/10.1007/s10111-021-00666-z.pdf ; TNO copy https://publications.tno.nl/publication/34638091/ohXHMB/moerman-2022-g (a05-a07, a13, a26, b11)
- [V] David and Schraagen (2018) Analysing communication dynamics (AF447). https://link.springer.com/content/pdf/10.1007%2Fs10111-018-0506-y.pdf (a08)
- [V, abstract only] Cook and Rasmussen (2005) Going solid. https://pmc.ncbi.nlm.nih.gov/articles/PMC1743994/ (a09)
- [V, abstract only] Westrum (2004) A typology of organisational cultures. https://pmc.ncbi.nlm.nih.gov/articles/PMC1765804/ (a10)
- [V] Braithwaite et al. (2024) Resilient health care performance in the real world. https://pmc.ncbi.nlm.nih.gov/articles/PMC11483974/ (a11, a12)
- [V, partly] Cartography of accident causation models (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12516668/ (a14)
- [V] The need for general adaptive capacity (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12369295/ (a15)
- [V] Iflaifel et al. (2020) Resilient Health Care systematic review. https://bmchealthservres.biomedcentral.com/ (b12)
- [V] Cooper (2022) The Emperor has no clothes. https://safety4sea.com/wp-content/uploads/2022/04/The-Emperoro-has-no- (b13)
- [V] Herrera, Praetorius, Degerman, Wiig (2025) Resilience Engineering 20 years. https://rpsonline.com.sg/proceedings/esrel-sra-e2025/ (b14)
- [V] Woods et al. (2014) EUROCONTROL Patterns in How People Think and Work. https://www.skybrary.aero/sites/default/files/bookshelf/5987.pdf (b22)
- [M] Woods and Branlat (2011) Basic patterns in how adaptive systems fail (403). https://www.oreilly.com/library/view/resilience-engineering-in/9781317 (a19, b21)
- [M] Hollnagel (2014) Safety-I and Safety-II; Hollnagel et al. (2011). https://www.taylorfrancis.com/books/9781315201023 (a20)
- [M] Woods, Hollnagel, Leveson (2006) Concepts and Precepts. https://en.wikipedia.org/wiki/Resilience_engineering (a21)
- [M] Rasmussen (1997) Risk management in a dynamic society. https://doi.org/10.1016/S0925-7535(97)00052-0 (a22)
- [M] Carlson and Doyle (2000) Highly optimized tolerance. https://doi.org/10.1103/PhysRevLett.84.2529 (a23)
- [M] Perrow (1984); Reason (2000); Amalberti (2001), as cited in a08. (a24)
- [M] Dekker (2011); Wears et al. (2008); Bergstrom (2009), as cited in a15. (a25)
- [M] Woods (2018) The theory of graceful extensibility, closed access. https://doi.org/10.1007/s10669-018-9708-3 (d14)
- [M] Woods (2015) Four concepts for resilience, read through citing papers (a13)

**LLM and agent studies**
- [V] Liu, Zhai, Gong et al. (2026) Resilience Matters for Embodied Agents System. https://arxiv.org/pdf/2608.23839 (a16, a17, b17, b18, c21, c22)
- [V] Owotogbe (2025) Robustness of LLM-based multi-agent systems through chaos engineering. https://arxiv.org/pdf/2505.03096 (a18)
- [V] Rabanser et al. (2026) Towards a Science of AI Agent Reliability. https://arxiv.org/pdf/2602.16666 (b01-b04, b24)
- [V] Yao et al. (2024) tau-bench. https://arxiv.org/pdf/2406.12045 (b05)
- [V] Barres et al. (2025) tau2-bench. https://arxiv.org/pdf/2506.07982 (d11)
- [V] Cemri et al. (2025) Why Do Multi-Agent LLM Systems Fail? https://arxiv.org/pdf/2503.13657 and https://arxiv.org/html/2503.13657v3 (b06, b07, c01-c06)
- [V] Cemri et al. MAST-Data recount. https://huggingface.co/datasets/mcemri/MAST-Data (d01)
- [V] Laban et al. (2025) LLMs Get Lost in Multi-Turn Conversation. https://arxiv.org/pdf/2505.06120 (b08, b09)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798 (b10, c10, c11)
- [M] Liu and Meng (2026) Self-Correction as Feedback Control. https://arxiv.org/abs/2604.22273 (c09)
- [V] Decomposing LLM Self-Correction. https://arxiv.org/html/2601.00828 (d02)
- [V] Thought-ICS. https://arxiv.org/html/2602.02416v1 (d03, d17)
- [V] MatSciBench. https://arxiv.org/pdf/2510.12171 (d10)
- [V] Or (2025) MTTR-A. https://arxiv.org/pdf/2511.20663v5 (b15, c18)
- [V] Xiao, Sun, Chen (2026) AIR. https://arxiv.org/pdf/2602.11749 (b16, b25, c19, c20)
- [V] Zhou et al. (2026) ResMAS. https://arxiv.org/pdf/2601.04694 (b19)
- [V] Yu, Bentley, Carroll (2026) Operational Hallucination and Safety Drift. https://arxiv.org/pdf/2607.18366 (b20)
- [V] Zhang et al. (2025) MIRAGE-Bench. https://arxiv.org/pdf/2507.21017 (c07, c08)
- [V] Cognitive Companion (2026). https://arxiv.org/html/2604.13759 (c13-c15)
- [V] LoopBench, Circular Reasoning (2026). https://arxiv.org/html/2601.05693v1 (c16, c17)
- [V] Cooperative Resilience in AI Multiagent Systems (2024). https://arxiv.org/html/2409.13187v2 (c23)
- [V] Systems-theoretic analysis of loss of control (2026). https://arxiv.org/html/2606.13474 (c24)
- [M] Self-Healing Framework for Reliable LLM-Based Autonomous Agents (2026). https://www.alphaxiv.org/abs/2605.06737 (c25)
- [M] Wang et al. (2025) AgentDebug. https://arxiv.org/abs/2509.25370 (c26)
- [M] Shinn et al. (2023) Reflexion abstract. https://arxiv.org/abs/2303.11366 (c27)
- [V] Reflexion full text. https://arxiv.org/pdf/2303.11366 (d13)
- [M] Practitioner pages on agent resilience (AWS blog and vendor posts), snippets. https://aws.amazon.com/blogs/architecture/ (c28)
- [V] Sentry (2026). https://arxiv.org/html/2610.02994 (d04, d05, d15, d16)
- [V] Repair-agent memory study. https://arxiv.org/html/2610.41433 (d06)
- [V] EvoCUE. https://arxiv.org/html/2609.34988 (d07)
- [V] EDV, Execute-Distill-Verify. https://arxiv.org/html/2606.24428 (d08)
- [V] Anchor. https://arxiv.org/html/2611.10382 (d09)
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/pdf/2509.25140 (d12)
