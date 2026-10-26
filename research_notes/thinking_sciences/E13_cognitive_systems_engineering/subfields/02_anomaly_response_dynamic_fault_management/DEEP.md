# Anomaly response (dynamic fault management): deep document

*Subfield E13.02. Built from evidence_a-d.jsonl, claims.jsonl (K01 to K30) and critique.md in this folder. Evidence ids (a01 to d24) and claim ids (K01 to K30) are cited inline. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single-source, [C] contested.*

**Read this first: three limits on the whole document.**
1. None of the four founding human studies was opened in full (Woods 1994 chapter, Roth, Woods and Pople 1992, NUREG/CR-6208, De Keyser and Woods 1990). The human side rests on one review chapter (Woods and Cook, read in full), two anaesthesia abstracts and blog summaries. See a26, d20.
2. There is no direct test of an impasse detector in an LLM fault task. All detector evidence is indirect.
3. Nine "opened" records (a01 to a03, a07 to a13) were read through one blog's summaries. They are secondhand.

---

## 1. What it is

Anomaly response, also called dynamic fault management, is the work of an operator who supervises a running process (a power plant, an operating room, a web service) when something goes wrong. The process keeps moving while the operator thinks. Time is short. The data are partial and noisy. A fault may have several causes.

Woods (1994) frames the task as two lines of work that run together (a04, not opened; framing from the title and record):
- **Diagnosis**: find the source. This is abduction: pick the best explanation for the findings.
- **Disturbance management**: keep the process safe while diagnosis goes on.

The loop in four phases is: notice, locate, explain, act. This is the same loop that LLM operations benchmarks score (AIOpsLab: detect, localize, root-cause, mitigate; c01).

Why it matters for our agent. Our schema already has a place for it: S6 IMPASSE is the moment a rule-level step fails and the agent has to switch to open reasoning (a07, Rasmussen's skill-rule-knowledge model). The questions this subfield answers are:
- What does a stuck operator look like, and can code see it?
- What breaks a fixation?
- What does a false alarm cost?
- How do current models behave on fault tasks?

Scope note. Fixation as a bias (Heuristics and biases), problem finding, value of information and belief revision are researched in parallel subfields. This document only links to them.

---

## 2. History and theories in depth

### 2.1 Rasmussen's levels (1983)
Three levels of behaviour: skill, rule, knowledge. The knowledge level is used when no rule fits: set a goal, plan, test by thought or by trial and error. Signals, signs and symbols are three ways to read the same display. The abstraction hierarchy lets errors be traced bottom-up and reasons top-down (a07; blog summary). Link to our schema: an impasse is a rule failing and the agent dropping to knowledge-level work.

### 2.2 Fixation errors (De Keyser and Woods 1990; Woods and Cook c.1999)
Fixation is a failure to revise a situation assessment or course of action. Woods and Cook give two tests, and both must hold (b01, d18):
1. **Persistence** over time.
2. **Revision cues were available** that could have started a revision.

The first assessment is usually reasonable. Hindsight makes the fix look obvious. Other names for it: functional fixation, cognitive lockup, cognitive hysteresis (d18).

Garden-path problems (b02, from Johnson, Moen and Thompson 1988). Early cues strongly suggest a plausible wrong answer. Later, weaker cues suggest the right one. Fixation here is a normally good process applied to a bad class of problem, not lack of knowledge.

The opposite failure is **thematic vagabonding** (Dorner 1983): attention that shifts on every signal and never settles. Revision has a cost (b03). No source gives the best switching rate.

Remedies from incident review (Woods et al. 1987, post Three Mile Island; b04, d18):
- a person with a fresh point of view usually breaks a fixation;
- a devil's advocate (cites Schwenk and Cosier 1980);
- better process feedback.

These come from incident reviews, not controlled trials. No effect sizes.

### 2.3 Simulator studies of anaesthesia (1990 to 1992)
- DeAnda and Gaba (1990): 19 simulations, first- and second-year residents, 132 unplanned incidents. Fixation errors were 20.5% of incidents (27 incidents; mean 1.42 per simulation). Human error 65.9%, equipment 3%, unknown 10.6% (d16, opened abstract).
- Schwid and O'Donnell (1992): 30 anaesthesiologists (10 residents, 10 faculty, 10 private practice). 63% made fixation errors or failed to revise a plan when cues disagreed. Correct anaphylaxis diagnosis 40%. Adequate treatment of myocardial ischemia 27%. Cardiac arrest managed per ACLS guideline 30%. All experienced staff diagnosed esophageal intubation; 2 residents did not (b05, d17).

The two rates have different units (share of incidents versus share of people). They cannot be compared. The scoring rule for "failure to revise" is not in either abstract.

### 2.4 Cognitive simulation (Roth, Woods and Pople 1992)
A computer model of operator cognition (CES) was run on simulated plant emergencies to find where intention errors are likely (a05; not opened). It is a precedent for testing a scaffold by running a model of the reasoner through scripted faults.

### 2.5 Procedures and their edge (NUREG/CR-6208, Woods 2006)
Roth, Mumaw and Lewis (1994): operators in nuclear training simulators rely on written procedures. In several of 38 analysed cases (two scenario families, two plants, up to 11 crews per plant), situation assessment and response planning dealt with parts of the emergency the procedures did not cover (a06; catalogue page only, PDF blocked).

Woods and Hollnagel: the context gap. Automation acts on a model of the world. If the model differs from the real situation, it does the right thing for the wrong world. All procedures are brittle. After Three Mile Island, operators were held responsible but could not change incomplete procedures: a double bind (a11, blog summary).

### 2.6 Alarm design and data overload (Woods 1995; Woods, Patterson, Roth 2002)
- Alarms fail as nuisance alarms, ambiguous messages, alarm inflation and status updates. They are densest when load is highest (a02).
- A good preattentive signal has three properties: picked up in parallel, carries partial information, light enough not to interrupt (a03).
- Three kinds of data overload: clutter, workload bottleneck, finding significance. Hiding data, showing only "important" items, letting the machine decide, and statistical cues all fail. Data has meaning only against the observer's goals, context and stage of problem solving (a01).

All of this is case-based, read through blog summaries. No controlled comparison.

### 2.7 Co-occurrence traps and multi-cause faults
Besnard, Greathead and Baxter (2004): a wrong model stays in use while events match expectations. Kegworth 1989: throttling back the right engine stopped the vibration, so the crew kept the wrong diagnosis for about 20 minutes. Partial confirmation is accepted fast; contradiction needs more consistent evidence (a08, a09). Chernobyl: operators held the belief that the plant could not explode and kept looking for other stories even with graphite visible. Fixation can show up as new stories for the same data, not as repeating an action.

SNAFUcatchers (2017): three web-operations incidents. Anomalies came from interactions between components under near-normal conditions. Responders searched iteratively and abandoned hypotheses. A first hypothesis can be right yet insufficient (a13).

### 2.8 The three failure patterns (Woods and Branlat 2011)
Decompensation (capacity to adapt runs out as problems cascade), working at cross-purposes (locally adaptive, globally maladaptive), getting stuck in outdated behaviours (a once-adaptive strategy kept after the world changed). These come from a conceptual chapter on adaptive systems, not from the fault-management studies. They have no measured rates anywhere we could read (d19, K30). Map detector rules by mechanism, not by cited rate.

### 2.9 Automation as team player; cognitive aids
- Klein and Woods (2004): ten challenges. The more adaptable an automated agent, the less predictable. Agents should signal when they struggle (a10).
- Automation bias: found in experts, rises with workload, complexity and time pressure, not removed by training or instructions. Showing information rather than a recommendation reduced it (b07, b08, b09; abstracts).
- Cognitive aids and checklists cut omitted critical steps in crises (b26, b27).

### 2.10 The move to LLM agents (2023 to 2026)
The same shape is now measured in software operations: AIOpsLab (2025), ITBench (2025), RCAgent (2024), SREGym (2026), Cloud-OpsBench (2026). Parallel work studies agent loops (MAST, AgentBench, Reflexion), error location (Who&When, TRAIL, AgentDebug) and learned stuck monitors (Stuck Monitor, FailFast). Section 6 covers them.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. "Human" or "LLM" in the source column marks the population.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Fixation is common in anaesthesia simulators | 63% of 30 anaesthesiologists (10/10/10) made fixation errors or failed to revise; 40% diagnosed anaphylaxis; 27% treated ischemia adequately; 30% ACLS-correct arrest. Separate: fixation 20.5% of 132 incidents (27) in 19 resident simulations | Schwid and O'Donnell 1992; DeAnda and Gaba 1990 (human; b05, d16, d17, d18) | [E] (K01), different units, no same-scoring replication |
| Fixation has a two-part test | Persistence plus available revision cues | Woods and Cook (human review; b01, d18) | [E] definition; no rates |
| A fresh viewpoint usually breaks human fixation | No effect size; incident review | Woods et al. 1987 via Woods and Cook (b04) | [S] (K14) |
| Detect-to-fix drop, AIOpsLab (48 problems) | Detection FLASH 100%, ReAct 76.92%, GPT-4 69.23%, GPT-3.5 23.07%. RCA ReAct 45.45, GPT-4 40.90, FLASH 36.36, GPT-3.5 9.09. Mitigation FLASH 54.55, ReAct 36.36, GPT-4 27.27, GPT-3.5 0. Overall FLASH 59.32, ReAct 55.93, GPT-4 49.15, GPT-3.5 15.25 | Chen et al. 2025 (LLM; a15, b10, c01; critique-corrected) | [E] (K07). Cells about 11 to 13 problems; one problem is 8 to 9 points |
| Detect-to-fix drop, ITBench SRE | 94 scenarios; resolved SRE 13.8%, CISO 25.2%, FinOps 0%. GPT-4o diagnosis 13.81% (SE 1.67), mitigation 11.43% | Jha et al. 2025 (LLM; a18, b13, c15) | [E] (K07) |
| Difficulty and observability cut success | GPT-4o diagnosis easy 36%, medium 7.73%, hard 5.0%; mitigation 21%, 12.27%, 0.0%. Without traces diagnosis 13.81 to 9.52%, mitigation to 2.86% | ITBench (a18, b13, c16) | [S] (K08). Main text 13.81% vs appendix 18.10% with traces: unresolved |
| 2026 frontier models, same shape | ITBench-AA (59 tasks x 3): Opus 4.7 47%, GPT-5.5 46% (31 turns), Gemini 3.1 Pro 30% (83 turns). SREGym (90 problems): diagnosis 38.1 to 72.6%, mitigation 40.4 to 78.5%, best end-to-end 60.7%, new failure types 15.4 to 28.2%. Cloud-OpsBench (754 cases): best Joint RCA Accuracy 0.76, Evidence Closure 0.15 to 0.46 | d08, d04, d01 (LLM) | [E] (K26); ITBench-AA is a vendor article |
| Noise lowers diagnosis for every agent pair | Claude Code + Sonnet-4.6 diagnosis 72.6 to 62.6%; Codex + GPT-5.4 70.0 to 59.3%; Stratus + Sonnet-4.6 61.5 to 51.5% | SREGym (d04) | [S] |
| Right answer without the evidence | Cloud-OpsBench OnlineBoutique: best JRA 0.76 with ECR 0.38; GPT-5 JRA 0.68 with ECR 0.21; TrainTicket GPT-5 JRA 0.68, ECR 0.15 | d01 | [S] |
| Agents anchor on the first plausible anomaly | "treats the first plausible abnormality as a stopping criterion"; in one problem neither agent inspected the faulty component; another named the true cause but kept the wrong one. No prevalence | SREGym (d05); Cloud-OpsBench (d03) | [E] (K27), qualitative, author-selected |
| Wrong diagnosis is often recovered by acting and watching | P(mitigation given right diagnosis) 68 to 89%; given wrong 22 to 62%; Stratus + Sonnet-4.6 3.82 attempts when wrong vs 1.88 when right | SREGym (d06) | [S] (K28) |
| Weak models repeat the same failing call | GPT-3.5: same malformed call up to 14 times in a 20-step case. MAST step repetition 15.7% of failure labels. AgentBench Task Limit Exceeded 23.9, 8.0, 67.9, 0.0, 82.5% (columns inferred) | a16, c03, a21, c06, c17 | [E] (K05) |
| Strong models do not loop on identical calls | Cloud-OpsBench Redundant Action Rate about 0.00 for GPT-5, Claude-Sonnet-4, Gemini-2.5-Pro, DeepSeek-V4-Flash, Qwen3.5-Plus; Qwen3-8B 0.46 (16.01 steps), Qwen3-14B 0.28 | d02 | [S], boundary on K05 |
| Failed call in context raises repeat chance (small models) | 6 models 135M to 1.7B; odds factor 2.8; failed call prob 0.06 to 0.54; greedy repeat 19% vs 0%; ToolShed 0.5B: repeat 31% standard, 24% with "do not repeat" instruction, 80% with clean restart (+49, CI +33 to +64) | Gumaan 2026 (d12) | [S], tiny models |
| More steps stop helping early (ops tasks) | GPT-3.5 no gain past 5 steps; FLASH best 59.32% only at step limit 20 | AIOpsLab (a17, b11, c02) | [S] (K06) |
| Intrinsic self-correction hurts | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1), 41.8 after 2 rounds; HotpotQA GPT-4 49.0 to 43.0. Oracle labels: GPT-3.5 84.3 / 89.7 / 29.0, GPT-4 97.5 / 85.5 / 59.0 (GSM8K / CSQA / HotpotQA) | Huang et al. 2024 (b15 corrected by c10); Kamoi 2024 survey (b16, c11) | [E] (K03) |
| Error location is the weak step, repair the strong one | BIG-Bench Mistake GPT-4 mistake-finding 52.87%; backtracking from true location +18 to +44 points (arithmetic +43.92, Dyck +18.04) on originally wrong answers, 0 to -11 on right ones. Who&When 53.5% agent, 14.2% step, 127 systems. TRAIL best joint 0.183 (GAIA), 0.050 (SWE) | Tyen 2024; Zhang 2025; Patronus 2025 (b17, a22, c09, b24) | [E] (K04) |
| LLM locator with taxonomy works partly | AgentDebug (GPT-4.1): step accuracy 45.0% vs 28.0%; all-correct 24.3% vs 0.3%; kappa 0.55, 200 trajectories. Re-rollout from the found step, ALFWorld: GPT-4o-mini 21 to 55, Qwen3-8B 48 to 74, Qwen3-Next-80B 60 to 84 | Zhu et al. 2025 (b20, d14) | [C] (K21), no replication |
| Locator accuracy falls with log length | Who&When hand-crafted logs of 5 to 130 steps; accuracy falls with length; random baseline step-level 19.06% (algorithm logs), 4.16% (hand-crafted) | d15 | [S]; reconciler of K04 and K21 untested |
| Early commitment, no recovery | 15 models drop 39% on average single-turn to multi-turn (200,000+ conversations, 6 tasks); aptitude -15%, unreliability +112%; snowball recap recovers 15 to 20% | Laban 2025 (b18, b19, c20) | [S] (K02) |
| Tool investigation cuts invention, not error | 97 cases: correct ReAct 35% vs CoT 39% and retrieval 39%; hallucination 4% / 12% / 40%; give-up among wrong 66% / 32% / 18%; 28 of 97 solved by all three | Roy et al. 2024 (a20, b14, c12) | [S] (K09) |
| Structure around the model beats prompting | RCAgent pass within 15 steps 99.38% vs ReAct 86.33%; invalid 7.93% vs 22.82%; nucleus sampling 70.19% pass / 44.80% invalid; SQL tools 65.84% / 70.94%. SWE-agent lint guard 18.0% vs 15.0% (+/-3.0) | a19 (corrected by c14), c19 | [E] (K10) |
| Verification gaps are a big failure group | MAST groups 41.8% design, 36.9% misalignment, 21.3% verification; no verification 8.2%, wrong verification 9.1%; verification step +15.6% on ProgramDev; role clarity +9.4% on ChatDev. 1642 traces, 7 frameworks, kappa 0.88 (human), 0.77 (LLM judge) | Cemri 2025 (a21, c05 to c07, b22, b23) | [S] (K12, K22) |
| Learned stuck monitor beats none and beats fixed-interval | OSWorld: small model alone 43.3%, with monitors + stronger model 58.2% at $0.051 (vs $0.132 for strong model alone, 60.1%). WebArena 30.3% to 58.8%. Fixed interval k=3,5,7 best: 55.1% at $0.07 (OSWorld), 52.5% at $0.24 (WebArena). Detector held-out accuracy 93.9% | Wei et al. 2026 (d11) | [E] with FailFast (K23); gain mixes detection with escalation to a stronger model |
| Step-count rule is a strong baseline; learned monitor is better | Qwen3.6-27B at 5% FPR: recall 30.5% (FailFast), 21.0% (AgentStop), 19.8% (step count), precision 76.1 / 68.6 / 67.3. At 25% FPR: 68.3 / 54.5 / 50.9. Qwen3.5-9B at 5%: tie 34.7 / 35.1 / 34.7 | Wang et al. 2026 (d09) | [S] (K24) |
| False alarms cost real runs; carry-over cuts the cost | Would-have-passed runs lost, Qwen3.6-27B: cold restart 36.4% (10% FPR), 27.5% (25%); with diff overlay 15.2%, 8.8%. Resolve gain at 25% FPR +5.2 (overlay) vs +0.2 (cold). Token overhead +43.8% vs +18.2%. SWE-PRM prompt feedback +4.2 on 9B, -3.2 on 27B | d10 | [S] (K14, K25) |
| Model-judged "should I ask" trigger is unreliable | Ambig-SWE: Sonnet 4 neutral prompt acc 0.74, FP 0.08, FN 0.44; strong-encouragement 0.89, 0.03, 0.18; Qwen 3 Coder FP 0.00, FN 1.00; Llama 3.1 70B FP 0.95, FN 0.09. Interaction gains up to 74% relative; Sonnet 4 reaches 89% of full-spec | Vijayvargiya 2025 (d21) | [S] (K29) |
| Required-step checklists cut omissions (human) | Koers 2020: 33% to 10%, OR 0.63, 25 teams, 75 scenarios per arm. Arriaga 2013: 23% to 6%, adjusted RR 0.28 (0.18 to 0.42), 17 teams, 106 scenarios | b27, b26 | [E] (K11); omissions, not fixation |
| Raw or irrelevant context harms | AIOpsLab failed cases lean on raw telemetry (correlational); GSM-IC one irrelevant sentence cuts accuracy; Lost in the middle: over 20% drop mid-context | b12, c21, c22 | [E] (K16) |
| Automation bias | Review of 74 of 13,821 papers; 40 of 890 in a second review. No pooled effect | b07 to b09 | [E] (K13), abstracts only |

---

## 4. Mechanisms and models

This section turns the findings into rules an engineer could code. Every rule is a hypothesis for the bench until Section 8 tests it.

### 4.1 The fixation test (two criteria)
Source: Woods and Cook (b01, d18). A run is fixated when both hold:
1. **Persistence.** The same top hypothesis H has been held for at least N further steps.
2. **Revision cue available.** Since H was adopted, at least one observation exists that H does not explain, or the symptom H should have removed is still present.

Implementation sketch:
```
state: hypotheses list [{id, text, adopted_at_step}], top = current best
for each step:
    obs = parse(tool_output)            # code, fixed-size record
    for h in hypotheses: h.explains[obs.id] = check(h, obs)   # code check or model slot, cited
    contradictions = [o for o in obs_since(top.adopted_at_step) if not top.explains[o]]
    persists = step - top.adopted_at_step >= N
    symptom_persists = original_failing_check still fails after last action
    if persists and (contradictions or symptom_persists): fire IMPASSE(reason="fixation")
```
Why both tests: a hypothesis that is simply right persists too. Persistence alone would flag it (b01 agent_relevance). The symptom-persists branch comes from SREGym (d06): a wrong first diagnosis is often recovered by acting and watching whether the failure persists, and attempts were twice as many when the diagnosis was wrong.

### 4.2 The loop test (stuck in outdated behaviour)
Source: AIOpsLab (a16, c03), Reflexion trigger (c18), MAST FM-1.3 (c06). Rules, all in code:
- **Repeat rule**: same action and same error text (hash) N times in a row. Reflexion uses more than 3 cycles; its other cap is more than 30 actions.
- **Cap rule**: step cap with no new evidence since step k.
- **No-new-evidence counter**: count of distinct facts in the code-held record; fire when it has not grown in M steps.

The repeat rule is expected to fire mostly on weak models (d02: Redundant Action Rate about 0.00 for strong models, 0.28 to 0.46 for Qwen3 8B and 14B). Fixation in strong models looks like new stories for the same data (a09), not identical calls. A repeat rule alone would miss it. So 4.1 and 4.2 are two separate detectors.

### 4.3 The decompensation test
Mechanism: effort goes in, state does not change. Code signal: tokens or steps spent since the last time any check result changed. Evidence for a flat curve: AIOpsLab GPT-3.5 gained nothing past 5 steps; FLASH peaked at 20 (a17, K06). The FailFast step-count-only control (19.8% recall at 5% FPR) is the nearest quantified version (d09). Rule: spend fraction of budget with no change in the pass/fail vector fires the impasse.

### 4.4 The cross-purposes test
Mechanism: two sub-attempts undo each other. In a single-agent schema this appears as an action that reverts the previous action, or a subgoal result that fails the check the parent had passed. Code: keep a state hash; fire if the state returns to a previously seen hash (oscillation). The Stuck Monitor found loops and oscillation as what the stuck flag catches (d11). No rate is available (K30).

### 4.5 The co-occurrence trap guard (Kegworth)
After a fix, a check must run against the **original failing output**, not against "looks better". Code: store the original failing check; accept a fix only if that check now passes. This is the G3 form of the lesson (a08, K19). Single case study; the guard is cheap.

### 4.6 What crosses a restart (the carry-over rule)
Evidence: cold restart adds +0.2 to +2.6 and loses 27.5 to 36.4% of runs that would have passed; a restart with the interrupted run's code diff as an optional overlay adds +3.0 to +5.2 and loses 8.8 to 15.2% (d10). Small-model evidence: clearing the failed step under greedy decoding raised repeats from 31% to 80% (d12). Gumaan's rule: the context after a failure must differ from the context before it, and the difference must not be the failed action.

Implementation: after an impasse, build the next context from
- the original task text,
- the code-held evidence list (verified facts only, fixed size),
- partial results that passed a check,
- a code-made description of the failure (not the failed action text; d12 found a runtime description removes 76% of the damage),
- never the earlier reasoning.

This is a test, not a settled rule: no study compares "fresh re-derivation from the evidence list" against same-context reflection at equal tokens (gap 3).

### 4.7 Event-driven versus scheduled checks
Fixed-interval checks lose to event-driven ones: OSWorld 55.1% at $0.07 vs 58.2% at $0.05; WebArena 52.5% vs 58.8% (d11). This is the same lesson as G1 (doubt on a signal), now with LLM numbers. A false-positive budget sweep (5, 10, 25%) shows the trade: recall 30.5 to 68.3%, precision 76.1 to 58.8%; on Qwen3.5-9B the resolve gain peaked at 10% FPR (+4.0), with 25% adding nothing more (+3.8) (d09, d10).

Implementation: choose the threshold on a calibration set to hit a target false-alarm rate (5 to 10%), and recalibrate per model (d23: two agent pairs were persistently off by 0.11 to 0.14).

### 4.8 Error location in code
The weak LLM step is locating the error (K04). Code locators available in a fault task: the first failing check, a diff between the last passing and first failing state, the earliest error string in the output (Cloud-OpsBench failure mode: the agent ignores a manifest error already seen; d03), a counter. Give the repair step the code-found location. The AgentDebug 45.0% step accuracy is the best LLM-located figure and still misses over half (d14), so an LLM-located step is a hint to re-check, not a verdict.

### 4.9 Evidence closure scoring
Cloud-OpsBench Evidence Closure Rate (ECR) scores whether the evidence needed to justify the answer was actually gathered (d01). Implementation: for each answer, the schema keeps a list of required evidence items; ECR is the share present. Use it as a logged metric and as a gate: an answer without closure goes to S5.

### 4.10 Rival-hypothesis gate
SREGym's named cause: the first plausible anomaly ends the search (d05). A gate: no action is taken until at least one rival hypothesis and one test that separates the two are written. This is the only anti-anchoring step supported by LLM fault data, and it is qualitative. SCHEMA.md 4b rejects a full competing-hypotheses matrix and ritual debiasing; this gate fires only on the detector (G1), and it is one rival, not a matrix. Test it before adding (UNKNOWNS U4).

### 4.11 Summarise tool output in code
Raw telemetry dumps go with failure (b12, correlational). Code can reduce a tool result to a fixed-size record (counts, top errors, changed fields). SREGym's Stratus (preprocesses) used 1.81x fewer tokens than Claude Code with the same model but diagnosed less (61.5% vs 72.6%; d07). Confounded. Do not claim an accuracy gain.

---

## 5. What holds up

### 5.1 Replications and independence
- **Fixation prevalence in humans.** Two sources with different units (63% of subjects; 20.5% of incidents). No replication with the same scoring (d17). A summary mentioned Rudolph work with 23% and 28% but it could not be traced and is not used. The number you can safely say is "common"; do not quote one rate.
- **Intrinsic self-correction fails.** Huang et al. and Kamoi et al. agree. Kamoi reviews the same literature, so the two are only partly independent (critique.md). Still [E]. Boundary: reasoning tasks, 2023 models; later reasoning models may differ (c11 limits).
- **Error location is weak.** Three independent sources (Tyen, Who&When, TRAIL). One contrary source (AgentDebug), authors' own benchmark (K21 [C]).
- **Detect-to-fix gap.** Five sources over 2024 to 2026 (AIOpsLab, ITBench, ITBench-AA, SREGym, Cloud-OpsBench). Gap persists in frontier models.
- **Repeat loops.** Seen in 2024 era models (AIOpsLab, AgentBench, MAST, Reflexion). **Fails to hold for strong 2025 models** on Cloud-OpsBench (Redundant Action Rate about 0.00). Only weak models loop.
- **Learned monitors help.** Two independent studies (Stuck Monitor, FailFast), different domains. Caveat on each (K23).

### 5.2 Failed or weakened results
- Cold restart with no carry-over: +0.2 to +2.6 only (d10).
- A written "do not repeat" instruction: repeat rate 31% to 24%, a small change, in 0.5B models (d12).
- Role prompt changes: +9.4% on one framework, misalignment stays (K22).
- Recap or snowball repetition in Laban: recovers only 15 to 20% of the lost performance; lowering temperature barely helps multi-turn (b19).
- SWE-PRM prompt feedback: +4.2 on a 9B model, -3.2 on a 27B (d10). Interventions that help a weak model can hurt a strong one.
- Adding discussion comments from past incidents: no significant help (c13).
- Past successful traces or a runbook raise outcome but barely change evidence closure on TrainTicket (ECR 0.18, 0.18, 0.17; d02).
- Anchoring mitigations in LLMs (CoT, reflection, "ignore the anchor"): no removal of bias; weak, small study (b25).

### 5.3 Moderators
- **Model strength**: repeats (above), SWE-PRM sign flip.
- **Observability**: ITBench without traces 13.81 to 9.52%; mitigation to 2.86%.
- **Difficulty**: ITBench easy 36% to hard 5.0%; Cloud-OpsBench TrainTicket JRA mean 0.67 easy, 0.43 medium, 0.08 hard.
- **Noise**: SREGym lowers diagnosis for every agent pair by about 10 points.
- **Novel failure types**: SREGym end-to-end 57.8 to 63.7% on ported problems vs 15.4 to 28.2% on new ones (n=34 vs n=13).
- **Log length**: attribution accuracy falls with length (d15).
- **Time pressure, workload, complexity**: raise automation bias in humans (b08).
- **Step-count baseline strength**: ties the learned monitor on Qwen3.5-9B at 5% FPR; trails it on Qwen3.6-27B (d09).

### 5.4 Interventions that worked (with the size)
- Code-side structure (RCAgent): 99.38 vs 86.33% pass, invalid actions cut from 22.82 to 7.93% (c14).
- Event-driven stuck/failure monitor: +15 points over small model alone (confounded), beats fixed-interval at lower cost (d11).
- Restart with carried-over work: +3.0 to +5.2 (d10).
- Targeted root-cause feedback (AgentDebug, weak locator): ALFWorld +34 / +26 / +24 points across three models (d14).
- Interaction with a human or user: up to 74% relative gain (Ambig-SWE; underspecification, not stalled diagnosis).
- Checklists in human crises: omissions 33 to 10% and 23 to 6%.
- Linting guard in SWE-agent: 18.0 vs 15.0% (wide error bars).

### 5.5 Interventions that did not
See 5.2. Plus: more steps (K06), intrinsic reflection (K03), role prompts, teamwork prompts, temperature lowering for multi-turn.

### 5.6 Internal conflicts in the record
- AIOpsLab mitigation: one record had ReAct and FLASH swapped; checked: FLASH 54.55, ReAct 36.36 (critique).
- Huang oracle numbers: c10 correct; b15 wrong (critique).
- RCAgent ablation: the 33.54% drop with 70.95% invalid is SQL-tools substitution (c14), not removal of JSON regeneration (a19).
- ITBench diagnosis with traces: 13.81% (main text) vs 18.10% (appendix). Open. Quote 13.81% with a flag.
- TRAIL: headline 11% is an average; do not mix it with the 0.183 and 0.050 split numbers.
- Roy et al.: hallucination 4/12/40% is over all cases; 6/18/49% is among incorrect predictions only. Do not mix bases.

---

## 6. Language models

### 6.1 How current models behave on fault tasks
**2024-era (GPT-3.5, GPT-4, GPT-4o)**
- AIOpsLab: detection easy for the best agent (FLASH 100%), but RCA 9 to 45% and mitigation 0 to 55%. False alarms on the two no-fault problems: only GPT-4 said normal (a15; not re-checked). GPT-3.5 repeats a malformed call up to 14 times in 20 steps.
- ITBench: GPT-4o 13.81% diagnosis; Llama-3.3-70B 3.10%; Granite-3.1-8B 3.57%; Llama-3.1-8B 0.99% (c15).
- RCAgent and Roy et al.: production incidents. Tool use cuts invented causes (hallucination 4% vs 40% for plain retrieval) but not error; the ReAct agent gives up in 66% of its wrong answers.

**2025 to 2026 (reasoning and frontier models)**
- SREGym (live, 90 problems): diagnosis up to 72.6%, mitigation up to 78.5%, end-to-end best 60.7%; noise costs about 10 diagnosis points; new failure types drop end-to-end to 15.4 to 28.2% (d04).
- ITBench-AA: Opus 4.7 47%, GPT-5.5 46%, Gemini 3.1 Pro 30% with 83 turns versus 31 turns for GPT-5.5. More turns were not better (d08).
- Cloud-OpsBench: best JRA 0.76; evidence closure only 0.15 to 0.46. Strong models show Redundant Action Rate about 0.00, so the failure is about evidence use, not loops (d01, d02).
- AIOpsLab itself was not re-run on reasoning models in any source found.

**The recurring failure shape**
1. Anchoring on the first or loudest anomaly (d03, d05).
2. Treating an empty result as no evidence (d03).
3. Right answer without the evidence (d01).
4. Over-investigation: listing upstream causes and symptoms as root causes (d08).
5. Early commitment in staged information, with no recovery (b18).

### 6.2 What changed behaviour, by how much
| Change | Effect | Source |
|---|---|---|
| Tool-grounded ReAct vs CoT / retrieval | hallucination 4% vs 12% / 40%; correctness 35% vs 39% | Roy (c12) |
| Code structure (key store, JSON regeneration, voting) | pass 86.33 to 99.38%; invalid 22.82 to 7.93% | RCAgent (c14) |
| Oracle label for self-correction | GSM8K GPT-4 95.5 to 97.5; HotpotQA 49.0 to 59.0 | Huang (c10) |
| No label self-correction | GPT-4 GSM8K 95.5 to 89.0; GPT-3.5 CSQA 75.8 to 41.8 | Huang (c10) |
| Locate the error first, then backtrack | +18 to +44 points | Tyen (b17) |
| Root-cause feedback loop | ALFWorld +24 to +34 points, three models | AgentDebug (d14) |
| Step-level monitor, event-driven | 58.2 vs 55.1% at lower cost (OSWorld) | d11 |
| Restart with diff overlay vs cold | +5.2 vs +0.2 (Qwen3.6-27B, 25% FPR) | d10 |
| Replay of past traces (3 demos) | JRA 0.70 to 0.79 (OnlineBoutique); 0.58 to 0.56 (TrainTicket) | Cloud-OpsBench (d02) |
| Runbook (SOP) | JRA 0.70 to 0.76 and 0.58 to 0.62; ECR 0.39 to 0.61 / 0.18 to 0.17 | d02 |
| Asking the user when underspecified | up to 74% relative gain; false-alarm rates 0.00 to 0.95 by model/prompt | Ambig-SWE (d21) |
| Verification step | +15.6% (ProgramDev) | MAST (c07) |
| Role clarity | +9.4% (ChatDev) | MAST (c07) |
| Recap (snowball) | 15 to 20% of lost performance recovered | Laban (b19) |

### 6.3 What is not measured
- No study measures fixation with a detector in an LLM directly.
- Reflexion's trigger was never ablated against no trigger.
- No false-alarm rate for a code counter in a fault task.
- No equal-token comparison of code counter vs model-judged stuck flag vs no detector.
- No independent replication of AgentDebug.
- No sweep of switching frequency for fault tasks (only for GUI and SWE tasks).

---

## 7. What our agent should take

Schema part key: G = guardrail, S = state, O = operator, memory = Section 5. Evidence ids list claim ids first, then record ids.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Fire S6 from code, not from the model's feeling.** Triggers: failing check with no change in two rounds; same action and same error N times; step or budget cap with no new evidence. The model's own "I am stuck" is not a trigger. Already in SCHEMA.md; this adds support and the strong-model caveat (repeat rule mostly catches weak models). | G1, S6 | [E] | K03, K05, K23; c10, c18, a16, d09, d11, d02 |
| A2 | **Revise only from located, real failing output; code finds the location** (first failing check, diff, earliest error string). Model repairs. | G2, S5 | [E] | K03, K04; b15, c10, b17, a22, b24 |
| A3 | **Code-side action validation** (known tool, valid format, no exact repeat) before a step runs. | G1/G2 | [E] | K10; c14, c19 |
| A4 | **Code-held required-checks list** before an answer is accepted (omitted-step checklist). | G2, S8 | [E] | K11; b26, b27 |
| A5 | **Score and log per phase** (notice, locate, explain, act), and log evidence closure, not only final correctness. Right answers without evidence are common. | S9, section 6 logging | [E] | K07, K26; d01, a15, d04 |
| A6 | **Show evidence, not a proposed answer, to any judge or checker.** | G5 | [E] | K13; b07 to b09 |
| A7 | **Summarise raw tool output in code** into a fixed-size record before the model sees it; put the live summary last in context. | G6/memory | [E] for harm of raw/irrelevant context; the fix itself [S] | K16; b12, c21, c22, d07 |
| A8 | **Do not add**: scheduled doubt, persona or role prompts for a single agent, "be careful" instructions, intrinsic self-reflection. Already in SCHEMA 4b; this adds fault-task numbers. | 4b | [E] | K03, K22; c10, b23 |
| A9 | **Detect anchoring as logged data** (does the final answer's cause appear in the first 3 steps; was a rival ever listed). Logging only, no new step. | section 6 | [E] that anchoring occurs (qualitative) | K27; d05, d03 |

### Test first (single-source, contested or untested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Two-criteria fixation detector** (persistence plus available revision cue or persisting symptom) as a separate impasse trigger from the loop detector. | G1, S6 | [S] (definition [E]; LLM effect untested) | K01, K27, K28; b01, d18, d06, d05 |
| T2 | **Repeat plus no-new-evidence counter in code** vs step cap vs model-judged stuck flag vs none, at equal tokens. | G1, S6 | [S] | K24, K05, K29; d09, d02, d21 |
| T3 | **Carry-over rule at restart**: clean context with evidence list and verified partial work, no old reasoning and no failed action text. | S6, memory | [C] | K14, K25; d10, d12, d13 |
| T4 | **Rival-hypothesis gate**: at an impasse, one rival and one separating test before acting. | S6 (O) | [S] | K27, K18; d05, d03, b02 |
| T5 | **Act-and-watch revise trigger**: same symptom persists after an action. | S5/S6 | [S] | K28; d06 |
| T6 | **False-alarm budget**: threshold set for a 5 to 10% false-alarm rate, recalibrated per model. | G1, S6 | [S] | K15, K25; d09, d10, d23 |
| T7 | **Code locator vs LLM locator** for the repair step; bin by log length. | S5 | [C] | K21, K04; d14, d15, b20 |
| T8 | **Ask trigger from a code stall counter; model only writes the question** (where a human or a tool can supply missing data). | G5, new O-ask | [S] | K29; d21, d22, c13 |
| T9 | **Co-occurrence guard**: accept a fix only if the original failing check passes. | G3, S8 | [S] | K19; a08 |
| T10 | **Evidence-closure gate** before submit. | S8 | [S] | K26; d01 |
| T11 | **Late-weak-evidence re-weighing** on garden-path items. | S5 | [S] | K18; b02 |
| T12 | **Fixed-size summary of tool output vs raw dump at equal tokens.** | memory | [S] | K16; d07, b12 |

---

## 8. Concrete tests on our bench

All tests: both arms use the same total tokens (setup cost counted, G7), the same model for recovery, the same items, and at least 3 seeds. Report per-arm accuracy, tokens, number of detector fires, and for each fire whether the run was a true stall. The bench item types come from the existing harness (ARC, BRAINTEASER, word puzzles, and fault scripts built for this test).

**Item set to build (fault scripts).** About 30 scripted items, each with a tool that returns scripted output:
- 10 "wrong first hypothesis" items: the first plausible cause is wrong; contradicting evidence arrives at step 3 to 6 (garden path).
- 6 "noise anomaly" items: an injected harmless anomaly plus the real fault (SREGym style).
- 6 "co-occurrence" items: a wrong fix makes the visible output look better (Kegworth).
- 4 "no fault" items (false alarm check).
- 4 "masked signal" items: one data source removed (ITBench traces-removed style).
Plus the standard ARC and BRAINTEASER items as a transfer check.

| # | Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 | T2 detector comparison | fault scripts + BRAINTEASER items with a loop-prone model | (a) no detector; (b) step cap only; (c) repeat + no-new-evidence counter in code; (d) model-judged "am I stuck" | recall of true stalls; false-alarm rate; accuracy; tokens | (c) recall above (b) at 5% FPR; (d) worse than (c) on false alarms; gain over (a) of a few points, bigger on the weak model |
| B2 | T1 fixation detector | 10 wrong-first-hypothesis + 6 noise items | detector (persistence + cue) on vs persistence-only vs off | share of runs keeping the first hypothesis for 3+ further steps; accuracy | on cuts fixation share; persistence-only has more false alarms on right hypotheses |
| B3 | T3 restart carry-over | all stalled runs from B1/B2 | (a) same-context reflection; (b) clean restart with task only; (c) clean restart with evidence list; (d) clean restart with evidence list + verified partial work | recovered-stalled runs; wrongly-aborted would-have-passed runs | (d) > (c) > (b) by recovery; (b) loses many would-have-passed runs (27 to 36% in d10); (a) near zero gain (b15) |
| B4 | T4 rival gate | noise + wrong-hypothesis items | gate on at impasse vs off; ritual gate on every run as a control | share of runs inspecting the true faulty component; accuracy; tokens | gate at impasse helps; ritual gate costs tokens, no gain (G1) |
| B5 | T5 act-and-watch | wrong-first-diagnosis items with an action tool | trigger on persisting symptom vs on model doubt vs none | recoveries; attempts per run | trigger on persistence recovers more than model doubt |
| B6 | T6 false-alarm budget | all items including 4 no-fault | detector at 5, 10, 25% false-alarm budget | recall; precision; would-have-passed runs lost; net accuracy | gain peaks near 10% (d10); 25% adds little and costs runs |
| B7 | T7 locator | trajectories of 5 to 130 steps from our own runs | code locator vs LLM locator; repair from each | locator accuracy per length bin; repair success | LLM locator accuracy falls with length; code locator flat |
| B8 | T8 ask trigger | masked-signal items with a simulated human holding the missing value | ask on code counter vs ask on model judgement vs never | accuracy; asks per run; unneeded asks | code trigger with fewer unneeded asks; both beat never-ask |
| B9 | T9 co-occurrence guard | 6 co-occurrence items | original-check guard on vs off | wrong fixes accepted | guard blocks them; cost small |
| B10 | T12 summaries | telemetry-heavy items | fixed-size record vs raw dump | accuracy at equal tokens | no big gain claimed; a drop in cost with equal accuracy would be the pass |
| B11 | T10 evidence closure | masked-signal items | closure gate vs no gate | share of correct answers with full evidence; accuracy | gate raises closure; accuracy flat or small up |
| B12 | Strong vs weak model on loops | any | repeat rule fires on weak and strong model | fire rate by model | fires mostly on the weak model (d02) |

Pass rules and thresholds are in UNKNOWNS.md.

---

## 9. What does not transfer, and why

- **Human stress and fatigue.** Operators face alarm floods, fatigue and team dynamics. A single LLM run does not tire.
- **Time pressure as a driver.** In humans, time pressure raises automation bias (b08). Our agent has a token budget, not a clock; the analogue is budget exhaustion, which is not the same pressure.
- **Rates from anaesthesia simulators.** 63% and 20.5% describe doctors on 1990s PC simulators with unknown scoring. They tell us fixation is common. They do not predict an LLM's rate.
- **The fresh-person remedy.** In humans, a new person brings a different mental model and different knowledge. A fresh context of the same model does not (G4: samples from one model are not independent). Cold restart gave only +0.2 to +2.6 (d10).
- **Devil's advocate.** Human critics bring real disagreement. A persona of the same model is the correlated-sample trap (G4, G9). Not added.
- **Team and handoff designs.** Cook and Long's capacity sharing (a12), Klein and Woods's team-player automation (a10): about multiple people. Useful here only as the idea that escalation should be by a budget rule, not by the stuck party noticing.
- **Alarm display design.** Preattentive signals and spatial displays assume human perception. The transferable part is the principle: a partial, non-interrupting flag with a short reason code.
- **Repeat-loop detection for frontier models.** Strong 2025 models showed near-zero redundant calls (d02). The loop counter is a guard for weak models and cheap tiers, not the main detector for strong ones.
- **Multi-agent failure taxonomies (MAST, Who&When).** They describe multi-agent systems. Our design is single-agent. MAST's role-prompt result (K22) is a reason not to add personas; its verification-gap finding transfers.
- **Production RCA corpora.** Roy et al. and RCAgent use internal company incidents and lexical metrics; the results show direction, not magnitude.
- **Software-operations tasks vs our bench.** Cloud faults have live state, side effects and real-time clocks. Our bench items are static puzzles with scripted tools. The transfer of detector thresholds from SWE-bench or OSWorld (d09, d11) to ARC or puzzle items is untested.

---

## 10. Open questions

1. Does a code-run detector (repeat plus no-new-evidence) beat none and beat a model-judged "am I stuck" at equal tokens? (Gap 1; nearest data: d09 step-count control.)
2. What are the real rates for the three Woods patterns and the exact coding of fixation? (Blocked: NUREG/CR-6208, Woods 1994, De Keyser and Woods 1990 not opened.)
3. Does a fresh re-derivation from the evidence list beat same-context reflection at equal tokens? (Gap 3.)
4. What is the optimal switching or trigger rate? Only fixed-interval sweeps (k = 3, 5, 7) and a false-alarm budget sweep (5 to 25%) exist, on GUI and SWE tasks.
5. Do 2025 to 2026 reasoning models re-run on AIOpsLab and ITBench keep the detect-to-fix gap? (Partly closed by SREGym, ITBench-AA, Cloud-OpsBench.)
6. Why does AgentDebug's LLM locator work while Who&When, Tyen and TRAIL show it failing? Log length is the likely reconciler (d15); untested. No independent replication of AgentDebug.
7. What is the false-alarm rate of a code counter in a fault task, and what does an unneeded interruption cost? Only SWE data (d10) and two AIOpsLab no-fault items.
8. Does the 63% fixation figure replicate under the same scoring? None found.
9. Does fixed-size summarising beat raw dumps at equal tokens? SREGym's comparison is confounded (d07).
10. Do stall rules that ask a human recover more than they cost? Evidence is qualitative (c13) or about underspecification (d21).
11. Does fixation in strong models take the form "new stories for the same data" (a09) and can code see it? No measurement.
12. How does a detector's calibration move when the agent changes? One audit, abstract only (d23).
13. ITBench's 13.81% vs 18.10% with traces: which is right?

---

## 11. Sources

[V] = opened and read this session (full text or abstract page as stated). [M] = snippet, catalogue page or secondhand summary only.

**Founding human work**
- [M] Woods (1994) Cognitive demands and activities in dynamic fault management. https://doi.org/10.1201/9780203481714.pt2 (a04, c24)
- [M] Roth, Woods and Pople (1992) Cognitive simulation as a tool for cognitive task analysis. https://doi.org/10.1080/00140139208967389 (a05, c25)
- [M] Roth, Mumaw and Lewis (1994) NUREG/CR-6208. https://www.nrc.gov/reading-rm/doc-collections/nuregs/contract/cr6208/ (a06, d20; catalogue page only, PDF blocked)
- [M] De Keyser and Woods (1990) Fixation errors. No verified URL (a24)
- [M] Cook and Woods (1996) Adapting to new technology in the operating room. No verified URL (a25)
- [V] Woods and Cook (c.1999) Perspectives on Human Error: Hindsight Biases and Local Rationality. https://complexsystems.fail/citations/Perspectives_on_Human_Error.pdf (b01 to b04, d18)
- [V, abstract] Schwid and O'Donnell (1992) Anesthesiology 76:495. https://pubmed.ncbi.nlm.nih.gov/1550273/ (b05, d17)
- [V, abstract] DeAnda and Gaba (1990) Anesth Analg 71:77. https://pubmed.ncbi.nlm.nih.gov/2363534/ (d16; b06 was a snippet at https://researchexperts.utmb.edu/en/publications/unplanned-incidents-during-comprehensive-anesthesia-simulation/)
- [V, secondhand] Woods and Branlat (2011) Basic patterns in how adaptive systems fail, read through https://en.wikipedia.org/wiki/David_Woods_(safety_researcher) (d19)
- [M] Woods and Hollnagel (2006) Joint Cognitive Systems. https://www.oreilly.com/library/view/joint-cognitive-systems/9781420005684/ (a23)
- [V, secondhand] Blog summaries by Fred Hebert, not the papers: Woods, Patterson, Roth (2002) https://ferd.ca/notes/paper-can-we-ever-escape-from-data-overload.html (a01); Woods (1995) https://ferd.ca/notes/paper-the-alarm-problem-and-directed-attention-in-dynamic-fault-management.html (a02, a03); Rasmussen (1983) https://ferd.ca/notes/paper-skills-rules-and-knowledge.html (a07); Besnard et al. (2004) https://ferd.ca/notes/paper-when-mental-models-go-wrong.html (a08, a09); Klein and Woods (2004) https://ferd.ca/notes/paper-ten-challenges-for-making-automation-a-team-player.html (a10); Woods chapter 11 https://ferd.ca/notes/paper-on-people-and-computers-in-joint-cognitive-systems-at-work.html (a11); Cook and Long (2020) https://ferd.ca/notes/paper-building-and-revising-adaptive-capacity-sharing-for-technical-incident-response.html (a12)
- [V] SNAFUcatchers (2017) STELLA report. https://snafucatchers.github.io/ (a13)
- [V, catalogue] Finin and Morris (1989) Abductive reasoning in multiple fault diagnosis. https://ebiquity.umbc.edu/paper/html/id/751/Abductive-reasoning-in-multiple-fault-diagnosis (a14)

**Human aids and automation bias**
- [V, abstract] Parasuraman and Manzey (2010) Hum Factors. https://pubmed.ncbi.nlm.nih.gov/21077562/ (b07)
- [V, abstract] Goddard, Roudsari and Wyatt (2012) JAMIA. https://pubmed.ncbi.nlm.nih.gov/21685142/ (b08)
- [V, abstract] Lyell and Coiera (2017) JAMIA. https://pubmed.ncbi.nlm.nih.gov/27516495/ (b09)
- [V, abstract] Arriaga et al. (2013) NEJM; trial PMID 23323901 (the b26 URL, PMID 23574138, is a commentary). https://pubmed.ncbi.nlm.nih.gov/23574138/ (b26)
- [V, abstract] Koers et al. (2020) JAMA Surg. https://pubmed.ncbi.nlm.nih.gov/31774483/ (b27)

**LLM fault management and operations**
- [V] Chen et al. (2025) AIOpsLab. https://arxiv.org/abs/2501.06706 (a15 to a17, b10 to b12, c01 to c04)
- [V] Jha et al. (2025) ITBench. https://arxiv.org/abs/2502.05352 (a18, b13, c15, c16)
- [V] Wang et al. (2024) RCAgent. https://arxiv.org/abs/2310.16340 (a19, c14)
- [V] Roy et al. (2024) Exploring LLM-based agents for root cause analysis. https://arxiv.org/abs/2403.04123 (a20, b14, c12, c13)
- [V] Wang et al. (2026) Cloud-OpsBench. https://arxiv.org/abs/2603.00468 (d01 to d03)
- [V] Clark et al. (2026) SREGym. https://arxiv.org/abs/2605.07161 (d04 to d07)
- [V, vendor article] Artificial Analysis and IBM (2026) ITBench-AA. https://artificialanalysis.ai/articles/itbench-aa-launch (d08)

**LLM agents, loops, location and recovery**
- [V] Cemri et al. (2025) MAST. https://arxiv.org/abs/2503.13657 (a21, b22, b23, c05 to c07)
- [V] Zhang et al. (2025) Who&When. https://arxiv.org/abs/2505.00212 (a22, c09, d15)
- [V] Patronus AI (2025) TRAIL. https://arxiv.org/abs/2505.08638 (b24)
- [V] Zhu et al. (2025) AgentDebug. https://arxiv.org/abs/2509.25370 (b20, b21, c08, d14)
- [V] Liu et al. (2024) AgentBench. https://arxiv.org/abs/2308.03688 (c17; table columns inferred)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c18)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (c19; not re-checked)
- [V] Wang et al. (2026) Fail-Fast, Restart-Smart. https://arxiv.org/abs/2608.03222 (d09, d10)
- [V] Wei et al. (2026) Step-level optimization for efficient computer-use agents (Stuck Monitor). https://arxiv.org/abs/2604.27151 (d11)
- [V] Gumaan (2026) Feedback that backfires. https://arxiv.org/abs/2608.23651 (d12)
- [M] Yang (2026) Context-contaminated restart model. https://chatpaper.com/es/paper/278665 (d13)
- [V] Vijayvargiya et al. (2025) Ambig-SWE. https://arxiv.org/abs/2502.13069 (d21)
- [M] Edwards and Schuster (2026) Ask or Assume? https://arxiv.org/abs/2603.26233 (d22)
- [M] Reliability audit of early outcome prediction (2026). https://arxiv.org/abs/2609.25647 (d23)
- [M] AgentStop (2026). https://arxiv.org/abs/2605.15206 (d24)

**LLM self-correction, anchoring, context**
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b15, c10)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (b16, c11)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 (b17)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (b18, b19, c20)
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593 (b25; weak)
- [V, abstract and setup] Echterhoff et al. (2024) BiasBuster. https://arxiv.org/abs/2403.00811 (c23)
- [V] Shi et al. (2023) LLMs can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (c21)
- [V] Liu et al. (2024) Lost in the middle. https://arxiv.org/abs/2307.03172 (c22)

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 11 established claims: 9 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E13.02-K10** (reworded: the sources support less). RCAgent numbers (99.38 vs ReAct 86.33; invalid 7.93 vs 22.82; SQL tools 65.84/70.94) and SWE-agent lint 18.0 vs 15.0 verified, but neither paper compares structure against prompting changes, so 'raises stability more than prompting' is not supported; SWE-agent 15.0 is a plain Table 3 value, not a reported error bar. Corrected claim: Adding structure around the model raised stability or success in two agent systems: RCAgent's full system passed within 15 steps 99.38% vs 86.33% for plain ReAct (invalid actions 7.93% vs 22.82%; swapping in SQL tools gave 65.84% pass and 70.94% invalid), and SWE-agent's linting guard raised SWE-bench Lite success from 15.0% to 18.0% (a small, single-run difference); neither study compares this to prompt changes.
- **E13.02-K23** (reworded: the sources support less). Numbers verified (43.3->58.2 OSWorld, 30.3->58.8 WebArena, 93.9% detector; FailFast 66.6->71.8 at 25% FPR vs cold restart 66.8), but cost is lower only versus fixed-interval checking and the large model alone; the cascade costs more than the small model alone ($0.051 vs $0.022 on OSWorld). Corrected claim: A learned stuck or milestone monitor that escalates to a stronger model raises success over the small model alone (OSWorld 43.3% to 58.2%, WebArena 30.3% to 58.8%; held-out stuck-detector accuracy 93.9%) at lower cost than a fixed-interval large-model check ($0.05 vs $0.07 and $0.21 vs $0.24 per task) and than the large model alone, though costing more than the small model alone; FailFast on SWE-bench Verified raised Qwen3.6-27B resolve from 66.6% to 71.8% at 25% FPR with restart plus diff overlay (cold restart 66.8%). Caveats: the first gain mixes detection with a stronger model taking over; the second is one benchmark with open models only.
- **E13.02-K11** (now single-source: only one opened source, code check).
