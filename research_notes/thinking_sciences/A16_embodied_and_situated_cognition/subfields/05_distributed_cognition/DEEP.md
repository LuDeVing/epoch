# Distributed cognition: deep document

*Subfield A16.05. Writer pass, 2026-11-03. Built from evidence_a-d.jsonl (a01-a27, b01-b25, c01-c27, d01-d18), claims.jsonl (K01-K24) and critique.md in this folder. Evidence ids in brackets. Where critique.md corrected an evidence line, the corrected number is used here.*

## 1. What it is

Distributed cognition (DC) is a way of studying thinking. The unit of analysis is the whole system that does the work, not the head of one person. The system can be a ship's navigation team, an airliner cockpit, a person with a notepad, or a program with a model inside it. A cognitive process is defined by how information is transformed and passed between the parts of the system, not by where the parts sit (skull or skin) [a01].

Hollan, Hutchins and Kirsh (2000) name three kinds of distribution [a02]:

1. Across the members of a social group.
2. Between internal structure (memory, skill) and external structure (tools, displays, layout).
3. Through time, so that earlier products change later events.

Hutchins' strongest claim: a system larger than one person can have cognitive properties of its own that cannot be reduced to the properties of the persons in it [a04]. Social organisation is itself a cognitive architecture, because it fixes who sees what and when [a02].

What this is NOT:
- It is not a controlled-experiment field. Its founding evidence is ethnography (Hutchins) plus a few small lab studies (Zhang and Norman 1994; Kirsh and Maglio 1994). There are almost no effect sizes for the central claim.
- It is not the same as the "extended mind" thesis in philosophy. The Stanford Encyclopedia treats Hutchins as an example of embedded cognition only [a15].
- No LLM paper found tests Hutchins' own predictions (how a representational state propagates and changes across a system). LLM work tests architecture variants and uses DC as a design metaphor [c26, K19].

Why it matters to us. Our schema already takes the design view: the program decides every transition, keeps state, counts, compares and runs checks; the model fills one slot at a time (SCHEMA section 1). That is a distributed system by Hutchins' definition. The field gives us a vocabulary (what is written, in which medium, who reads it, how long it lasts) and a checklist of what to put outside the model. The LLM literature gives the measured part: what externalisation and multi-agent splitting actually buy, at what token cost.

## 2. History and theories in depth

### 2.1 Roots (1980s-1995)

- **Blackboard systems (Hearsay-II, Erman et al. 1980).** Independent knowledge sources write partial solutions to a shared blackboard. A control shell schedules them [c24]. Only a secondary source was read, and it has no accuracy numbers. This is the AI ancestor of shared-notes designs. Our S-states and operators act like knowledge sources, and the program is the control shell.
- **Hutchins, Cognition in the Wild (1995).** Ethnography of navigation on a Navy ship. Navigating a large vessel exceeds any one person's capacity, so the task is done by a team plus charts and instruments [a14, a15]. The book was NOT opened. It is known only through SEP and Hollan et al.
- **Hutchins (1995), "How a cockpit remembers its speeds."** The main primary source read [a04-a07, b09]. Case: setting landing-speed references in an MD-80 cockpit. Details in section 4.
- **Zhang and Norman (1994).** The only controlled lab test of the "same task, different place for the rules" idea [a08-a11].
- **Kirsh and Maglio (1994).** Epistemic action in Tetris [a12, a13, b07].
- **Wegner (1985-91), transactive memory.** Groups, especially close pairs, divide memory labour and keep an index of who knows what. Known only second-hand [a16, a17].

### 2.2 Consolidation (1995-2011)

- Hollan, Hutchins and Kirsh (2000) turned the case studies into a programme for HCI [a01-a03]. Three questions for groups: how individual-mind processes are implemented in a group; how group properties differ from member properties; how membership changes individual minds.
- Norman's "cognitive artifact" idea: an artifact does not make the person smarter, it changes the task. A recent LLM review quotes this: "Cognitive artifacts do not change human capabilities. They change the task." [c01]
- Sparrow, Liu and Wegner (2011), "Google effects on memory": people who expect to have a fact saved remember the fact less and its location more [b02]. The paper was not opened. Its Stroop-priming study failed to replicate (section 5).
- Woolley et al. (2010): a collective intelligence factor c for groups. Contested (section 5) [b10].

### 2.3 Offloading psychology (2016-2026)

- Risko and Gilbert (2016) is the standard review of when people offload and what it costs [b25]. It could not be opened (403). A pointer only.
- Gilbert's optimal-offloading task: people choose between using an external reminder and relying on memory, with points at stake. Across six or more studies people over-use reminders. The bias is stable within a person. Low confidence drives reminder use even when confidence is unrelated to accuracy [b04].
- Ngai and Gilbert (2026) showed the bias can be trained (section 5) [b03].
- Human-side warnings about offloading to LLMs: Kosmyna et al. 2025, Lee et al. 2025, Zhu et al. 2026 [b05, b06, c21, c22]. All weak causal evidence.

### 2.4 LLM era (2023-2026)

Three strands use DC ideas without testing the theory:

1. **Multi-agent collectives** (debate, mixture-of-agents, role teams). Founding positive result Du et al. 2023 [a19]. Then a run of matched-compute re-tests that mostly deflate it (section 6).
2. **Externalised state and interfaces** (memory streams, trajectory stores, agent-computer interfaces). Generative Agents, SWE-agent, MATM [c03, c19, c16].
3. **Reviews that adopt the vocabulary.** Zhou et al. 2026 argue that agent progress comes from moving cognitive burden into memory, skills, protocols and a harness [c01, c02]. Rosenbacke et al. 2026 propose a human-LLM "joint reasoning system" with reflection checkpoints but report no results [c23].

### 2.5 Competing views

- **Strong DC / extended mind:** the system is the thinker. No test separates it from the weak reading.
- **Weak (embedded) reading:** a person uses tools. This is all our engineering needs.
- **Individual-memory theory:** Hutchins argues it explains why a system needs external parts, not how the system works [a07]. Fair, but this is an argument, not data.

## 3. Core findings with exact numbers

Status key: replicated / single-source / failed / contested / human-only / older models only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Moving rules from memory into the display lowers errors, steps and time (Tower of Hanoi isomorphs) | Exp 2, N=18: all-internal vs all-external errors p<.001; main effect p<.05 time and steps, p<.005 errors. No errors at all on external rules. Solution times of easiest vs hardest problem differ up to 1 to 10. | Zhang and Norman 1994 [a09, a10] | Single lab, small N; human-only |
| Difficulty order depends on where the constraints live | 1A (N=24, all internal): II < II3 < II234 ~ II23. 1B (N=24, external): II < II-E3 <= II-E23 <= II-E234 | Zhang and Norman 1994 [a10] | Single lab; human-only |
| Same dimension shown by location beats size or colour | Exp 3, N=36. Nominal: size vs location times p<.003, errors p<.0001. Location vs colour times p<.016, errors p<.007. Steps mostly n.s. | Zhang and Norman 1994 [a11] | Single lab; colour ordering may have been too easy |
| External presentation raises completion but not move quality | Completion 100% computer vs 91% mental, chi-sq(1)=4.45, p=.03. Progress 4.00 vs 3.61, t(35)=2.44, p=.02. Move count difference n.s., p=.26. Time between moves 14.04 s mental vs 7.58 s computer, p<.001. N=123-135 | Fansher, Shah, Helie ~2020 preprint [a18, b08] | Preprint; different manipulation from Z and N |
| Cockpit memory is spread over card, booklet, bugs, callouts and pilots; redundancy catches a wrong weight | Card speeds e.g. 227 kt (no flaps), 152 (flaps 15), 128 (flaps 40). Callout when airspeed varies by more than 5 kt. More than 100 flights observed. No statistics. | Hutchins 1995 [a04-a06] | Single-source, ethnographic |
| Epistemic actions: players rotate Tetris pieces more than needed | Rotation starts within 400-600 ms, sometimes under 100 ms. Early rotation shows the piece 150-300 ms sooner than waiting. Physical rotation as fast as ~100 ms vs ~800-1200 ms mental (pilot estimate, N=3). | Kirsh and Maglio 1994 [a12, a13, b07] | Single-source; few experts; no controlled replication |
| Google Stroop priming does not replicate | Round 1 p=.2647; pooled p=.4493. Same sign, not significant | Camerer et al. 2018 via FLoRA [b01] | Failed (Study 1 only) |
| Close couples recall more only with their own memory division; assigned roles hurt | N=118 individuals (snippet only). With imposed categories strangers recalled more | Wegner, Erber, Raymond 1991 via Harris 2011 [a16] | Contested; second-hand |
| Older couples: both collaborative inhibition and facilitation | 12 couples, married 26-60 years. Word list: 9.50 (SD 1.08) nominal vs 8.92 (SD 2.11) collaborative | Harris et al. 2011 [a17] | Small N, mixed method |
| Collective intelligence factor c | Original: 192 groups of 3-5, c explains ~43-44% of variance. Mean member IQ vs c r=0.15. Rowe 2021 meta: r from -0.05 to 0.34. Graf 2019 meta: 3 factors not 1. | Woolley 2010 and critics [b10] | Contested; read second-hand |
| In 105 dyads on structured tasks, member intelligence and confidence predict best | N=210. Social sensitivity beta=0.39, p<.001. Equal turn-taking did not replicate. Final R2 up to 0.60-0.63 | Dyad study 2025 [b11] | Single study; students; 2-person groups |
| People over-use reminders; predict-then-feedback reduces it | Exp 1 N=164: d=.347 (p=.01 one-tailed). Exp 2 N=416: pattern replicated; predictions without feedback did not help. Metacognitive-bias benefit gone by post-task (d=.022) | Ngai and Gilbert 2026 [b03, b04] | Replicated within paper; small to medium |
| Handing core thinking to AI tracks lower motivation | N=589, three-wave survey | Zhu et al. 2026 [b05] | Correlational; self-report |
| LLM essay users recall less of their own text | 54 participants, 18 per group. 83.3% (15/18) of LLM group could not give a correct quote vs 11.1% (2/18) in each other group. Crossover N=18 | Kosmyna et al. 2025 [b06, c21] | Preprint; weak |
| More trust in AI goes with less critical-thinking effort | 319 workers, 936 examples | Lee et al. 2025 [c22] | Self-report |
| Debate beat single, reflection, majority (ChatGPT, 3 agents, 2 rounds) | Arithmetic 81.8 vs 67.0 / 72.1 / 69.0. GSM8K 85.0 vs 77.0 / 75.0 / 81.0. Chess pawn score 122.9 vs 91.4 / 102.1 / 102.2. MMLU 71.1 vs 63.9 (reflection 57.7). Biographies 73.8 vs 66.0. | Du et al. 2023 [a19, c05, c06] | Not reproduced at matched compute |
| Debate rarely beats CoT or self-consistency at matched compute | 5 methods x 9 benchmarks x 4 models = 36 settings. No method wins more than 20%; four win about 15%. SoM below CoT on all 9 sets on GPT-4o-mini. Claude-3.5-haiku MMLU: only AgentVerse +0.85%, others at least -3.60% | Zhang et al. 2025 [a21, b15, c08, d04] | Replicated (3 papers); small/mid models |
| Majority vote gets most of debate's gain | Qwen2.5-7B, 5 agents, 7 benchmarks: single 0.7205; debate T=2/3/5 0.7377/0.7112/0.7050; centralized T=2 0.6551; vote 0.7691. Arithmetic: single 0.814, debate T=5 0.67, vote 0.99 | Choi, Zhu, Li 2025 [d01] | Replicated; small models; no verifier |
| Plain debate leaves expected correctness unchanged (martingale) | Vanilla 0.7332; Conformist 0.7625; Follower 0.7629; oracle 0.8236; all non-oracle still below vote 0.7691 | Choi et al. 2025 [d02] | Theory plus one model family |
| No debate method clearly beats strong baselines when tuned | MedQA best: Medprompt 0.65, SoM 0.64, Ensemble Refinement 0.64, ChatEval 0.60, SC 0.60, single 0.60, Multi-Persona 0.58. MMLU: SC 0.78, single 0.76, SoM 0.73 | Smit et al. 2024 [d03] | GPT-3.5 class; gaps 0.01-0.05, no CIs |
| Sample-and-vote scales with sample count | GSM8K +12 to +24, MATH +6 to +10, MMLU +5 to +11, HumanEval +4 to +9, Chess +1 to +4. Llama2-13B 59% vs Llama2-70B 54% on GSM8K | Li et al. 2024 [a20, b19] | Single paper; gains shrink at high base accuracy |
| Mixing different models in debate helps | Heter-SoM +6.4% over SoM average; Heter-EoT +8.2%; up to +5.8% over CoT average | Zhang et al. 2025 [c09] | Two-model mixes only; conflicts with Self-MoA |
| Resampling the best model beats mixing models | AlpacaEval 2.0: Self-MoA 65.7 vs mixed 59.1 (+6.6). MMLU, CRUX, MATH average +3.8%. Quality coefficient larger than diversity, R2 ~0.7 | Li et al. 2025 [b20, d16] | Open 2024 models |
| Mixed teams: sign flips with team size | BBH N=100: 3 agents homogeneous 0.86 vs LLM-hetero 0.81; 5 agents 0.79 vs 0.85 | AgentNet 2025 [d17] | Within noise (s.e. ~3.5 pts) |
| Self-correction without an external signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8. GPT-4 GSM8K 95.5 to 91.5 to 89.0. GPT-3.5 GSM8K 75.9 to 75.1 to 74.7. Oracle-label GPT-4 GSM8K 97.5 | Huang et al. 2024 [b18] | Replicated direction; 2 rounds only |
| Finding the error is the bottleneck, fixing is easy | GPT-4 52.87 overall locating the first wrong step. With true location: wrong-trace gains +43.92 (arithmetic), +36.86 (Dyck), +23.53, +18.06; random location roughly half (+20.39, +21.57, +11.76, +5.16). Correct traces lose 6-16 points | Tyen et al. 2024 [d05, d06] | 2023 models; row labels partly garbled |
| Tool-based critique beats tool-free | HotpotQA EM/F1: CoT 33.7/46.1; CRITIC 38.7/50.5; CRITIC without tool 34.9/46.1. GSM8K PoT 70.1; CRITIC 72.2; without tool 68.3 | Gou et al. 2024 [d07] | 2023 models; TabMWP gain without tool also large |
| Multi-agent systems fail by design and coordination | 41% to 86.7% failure across 7 frameworks; 1600+ traces; kappa 0.88 (human), 0.77 (LLM judge). System design 41.8%, misalignment 36.9%, verification 21.3%. Step repetition 15.7%, reasoning-action mismatch 13.2% | Cemri et al. 2025 [a23, b12, c10] | Single study; open frameworks |
| Cheap structural fixes help modestly | ChatDev ProgramDev: 25.0% to 34.4% (better prompts) to 40.6% (new topology). +9.4% roles; +15.6% added verifier. HumanEval 89.6 / 90.3 / 91.5. Authors call them not substantial | Cemri et al. 2025 App. H [b13, c11] | Small task set (32) |
| Task structure decides the sign of multi-agent gain | 260 configurations. +80.8% (Finance, centralized) to -70.0% (PlanCraft, independent). All variants hurt planning -39% to -70%. Ceiling beta=-0.236, p=0.004 above ~45% single-agent score. Error amplification 17.2x independent vs 4.4x centralized | Kim et al. 2026 [a24, b14, d11, d12] | Single study; threshold empirical |
| A rough architecture predictor exists, but not pre-run | Cross-validated R2=0.373 (0.413 with capability index). Picks best architecture for 87% of held-out configs vs 20% random, 54% capability-only. Tool-count penalty beta=-0.096, p=0.002 | Kim et al. 2026 [d11] | Predictors come from traces |
| Interface design moves results (SWE-agent) | SWE-bench Lite (300), GPT-4 Turbo: SWE-agent 18.0% vs shell-only 11.0% (+7.0, 64% relative; corrected by critique). Full benchmark 12.47% (286/2294). HumanEvalFix 87.7 / 89.7 / 87.9 (Py/JS/Java) | Yang et al. 2024 [c19, d09] | Single model; tuned on Lite; 2024 |
| Interface ablations | No edit action 10.3; no lint 15.0; lint 18.0. Window 30 lines 14.3; 100 lines 18.0; whole file 12.7. Summarised search 18.0; iterative 12.0; none 15.7. Last 5 observations 18.0; full history 15.0 | Yang et al. 2024 Table 3 [c20, d08] | Differences of 2-3 pts inside noise |
| Lint-rejected edits are common | 1,185 of 2,294 (51.7%) had at least one failed edit, median 3, max 33. Of 286 resolved, 113 (31.5%) had one | Yang et al. 2024 [d09] | Descriptive |
| Interface gain may have shrunk | README claims a ~100-line bash-only agent scores above 74% on SWE-bench Verified | mini-SWE-agent README [d10] | README only; model unnamed; different subset |
| Memory, reflection and planning drive believability | TrueSkill: full 29.89; no reflection 26.88; no reflection or planning 25.64; crowdworkers 22.95; all removed 21.21. Kruskal-Wallis chi2(4)=150.29 | Park et al. 2023 [c03] | Believability rating, not task success |
| Facts spread with conversation as the only channel | Candidacy known to 1 agent (4%) then 8 (32%); party news 1 (4%) then 13 (52%) in 2 days, 25 agents | Park et al. 2023 [c04] | Includes hallucinated embellishment |
| Shared trajectory store raises success | ALFWorld (274 tasks) 0.4708 to 0.5511 (dense) to 0.6431 (best reranker, steps 10.35 vs 11.77). WebArena 0.1818 to 0.2045 (steps 21.99 to 20.26). Tokens per successful episode down 11-34%. Same-type retrieval 0.6314 vs cross-type 0.5985 (ALFWorld); 0.2766 vs 0.1915 (WebArena) | MATM 2026 [a26, c16, d13] | WebArena gain tiny; gating untested |
| Role-local memory beats shared memory | MultiAgentBench, 4 models. Consolidation interval 5 best. Token cost 9.4%-71.7% below baselines. Gains vs no memory +0.27 to +5.92; one cell lost | LLMA-Mem 2026 [c14, c15] | Preprint; small gains |
| Gated retrieval beats always-retrieve (with an external gate) | PopQA 14k, davinci-003: 46.5%, +5.3 over any non-adaptive method; retrieved for 40% (BM25). Models under ~10B gained little | Mallen et al. 2023 [d14] | Gate was popularity, not self-judged |
| Tool over-use is measurable in LLM agents | Llama overuse above 50%. SMARTAgent: tool use -24%, performance +37% (relative to base), one-fifth of tool calls on GSM8K/MINTQA | Qian et al. 2025 [d15] | Needs training |
| Probes ground reasoning | HotpotQA failures: CoT hallucination 56% vs ReAct 0%; ReAct reasoning errors 47% vs CoT 16%. ALFWorld: ReAct 71% vs Act 45%. WebShop 40.0 vs 30.1 | Yao et al. 2023 [d18] | PaLM-540B; tokens not matched |
| Split-load design helps only at high load | Gemini-1.5-Pro Math: IO 60.9, CoT 62.4, MAD 69.4, DMAD 70.0, CoThinker 75.3. Flash-8B: IO 33.8, MAD 38.6, CoThinker 37.7. Pooled loss 3.8% on instruction following (p<0.001) | Shang et al. 2026 [a25, b22, c18] | Authors' own method; messy tables |
| Group size hurts in LLM coordination game | Each extra member lowers success odds ~8% (OR=0.92); temperature OR=1.50 | Riedl 2026 [b21] | One toy task |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it. "Status" means evidence for the mechanism in LLM agents, not in humans.

### 4.1 Representational propagation (Hutchins' cockpit)

The cockpit computes landing-speed references through a chain of representation changes [a05]:

1. Read gross weight from the fuel/weight display.
2. Use weight to select a card in the booklet (weight filters the booklet).
3. The card gives speeds for each flap setting.
4. Set speed bugs on the airspeed dial. The computation now becomes a perceptual match: needle against bug.
5. The second pilot cross-checks with spoken callouts. The card also states the weight it assumed, so a wrong weight shows up against the panel.

Key properties:
- **Transform to a cheaper operation.** A numeric comparison becomes a visual one.
- **Redundant media.** Card, spoken words, bug position. Each differs in lifetime, sense used and vulnerability [a06, a07].
- **Memory is in the process, not in any one part.** "Speed bugs do not help pilots remember speeds; rather, they are part of the process by which the cockpit system remembers speeds." [a05]

Implementation for an agent:
```
artifact = {value, medium, producer, checked_by, lifetime}
log every artifact; for each key intermediate result keep TWO forms
  (prose claim + executable check, or table + summary)
compare forms in code; a mismatch is an impasse signal (feeds S6)
```
Status: the mechanism is from one ethnography. The LLM test of "inject an error in one of two forms, see if the other catches it" does not exist [K19, K21].

### 4.2 Where the rules live (Zhang and Norman)

Same abstract task (Tower of Hanoi isomorphs), four rules, each either internal (stated, memorised for 2 minutes, recited) or external (built into the objects, e.g. cup sizes that physically block illegal moves) [a08]. Result: external rules are close to error-proof; all errors fell on internal rules [a09].

Implementation:
- Rule held in the prompt = internal. The model must remember and obey it.
- Rule held in code = external. A legality checker rejects or repairs an illegal action before it counts.
- Rule: if a constraint can be written as a check, write it as a check and show the model only the violation (matches G2 and SWE-agent's linter [c20]).

Boundary: more constraints are not always easier. When all rules were internal the middle problem was hardest, because of working-memory load; with external rules difficulty tracked the number of rules [a10]. The load explanation is post hoc.

### 4.3 Epistemic action (Kirsh and Maglio)

An epistemic action changes the world to make the next judgement cheaper, faster or more reliable [a12]. Tetris players rotate more than needed to place a piece. Early rotation reveals the shape 150-300 ms sooner [b07]. Plan-then-act predicts about 1.5 rotations for a four-orientation piece; the data show more [a12].

LLM translation: a probe (run the code on an input, query a tool, reformat the data) is an epistemic action. The decision rule would be: when a cheap probe exists whose result discriminates between candidates, do it before reasoning more. ReAct supports the direction: probe-based runs had 0% hallucination as a failure cause on sampled HotpotQA failures vs 56% for CoT [d18]. The equal-token comparison is missing [K24].

### 4.4 Priced offloading (Gilbert paradigm)

The human result is that offload choice is driven by confidence, and confidence is poorly calibrated, so people over-offload. The fix that worked: predict your own memory performance, then get feedback, over five trials [b03]. Predictions alone did nothing.

Implementation:
```
before calling a tool / writing a note / retrieving:
  predict p_correct_without_tool (model gives a number)
  after: compare with the actual result (code)
  keep per-class calibration table (S0/S9 class record)
call the tool iff expected gain * (1 - p_calibrated) > cost
```
Status: tool over-use is measured in LLM agents (>50% for Llama [d15]), but prompt-level predict-then-check has no LLM test. Note G-rule tension: stated model confidence is a weak stop signal (4b), so the calibration table must come from measured outcomes, not from the model's stated number.

### 4.5 Transactive memory at agent scale

Wegner's idea: keep an index of who knows what rather than everything. MATM builds the machine version: a shared store of other agents' trajectories, a planner that decides per step whether to retrieve, top-20 candidates then one reranked unit given to the agent [c17, d13].

Implementation for a single agent: the subgoal library and lessons in SCHEMA section 5, indexed by problem class, retrieval capped at one unit, gated. Relevance matters: same-type retrieval beat cross-type (0.6314 vs 0.5985 on ALFWorld; 0.2766 vs 0.1915 on WebArena) [d13]. Role-local stores beat shared stores in LLMA-Mem [c14].

### 4.6 Centralised check over several workers (Kim et al.)

Independent agents amplified errors 17.2x vs 4.4x for centralized coordination [a24]. The mechanism is a single verifier gate that stops one worker's error from entering the others' inputs. Pre-run rule of thumb from d11-d12:

```
if single_agent_score > ~0.45 on this class: do not add agents
elif subtasks are independent and separately checkable: parallel workers + one verifier
else (strict sequence, e.g. planning): single agent
```
Decomposability is the authors' own judgement over six benchmarks, not an automatic measure.

### 4.7 Debate as a belief update (Choi et al.)

Debate is a process where each agent updates its answer after reading the others. Choi et al. prove that without an outside signal the expected probability of a correct answer stays flat (a martingale) [d02]. Biasing updates toward the current majority recovers some gain (Conformist 0.7625; Follower 0.7629), but both stay below plain voting (0.7691) on Qwen2.5-7B. Only an oracle that keeps correct answers helps a lot (0.8236). So: a debate-like step is worth something only when something outside it pushes beliefs toward the truth: a verifier, a test, a vote.

### 4.8 Interface as artifact (SWE-agent)

Design rules read from the ablations [c20, d08, d09]:
- Small action set; one edit command with built-in lint check (lint on 18.0 vs off 15.0).
- A viewer window of 100 lines (30 lines 14.3; whole file 12.7).
- Summarised search (18.0) beat iterative (12.0).
- Short history: last 5 observations (18.0) beat full history (15.0).
- Count failed edits per trajectory as a stuck-loop signal (median 3, max 33).

Caveat: this is GPT-4 Turbo on SWE-bench Lite. Run-to-run noise is 3-7 points, so 2-3 point steps are not safe. A bash-only agent is now claimed above 74% on Verified [d10], so the effect size for current models is unknown.

## 5. What holds up

### 5.1 Replications and failures (human work)

| Claim | Outcome |
|---|---|
| Google effect, Stroop priming (Sparrow 2011) | Failed to replicate. Same direction, p=.2647, pooled p=.4493 [b01]. A second non-replication (Hesselmann 2020) is reported but the page could not be opened. |
| Content-vs-location memory (Sparrow 2011) | No large preregistered replication found in the sources read. Unconfirmed [b02]. |
| Close couples remember better with their own division of labour (Wegner 1991) | Original paper not opened. Harris 2011 found both inhibition and facilitation in 12 older couples [a17]. Contested. |
| Collective intelligence factor c | Weak support: less variance explained, low task reliability, failure to replicate in virtual groups, multiple factors (Graf 2019: 3 factors; LePine 2008: 138 studies, 3 team-process factors) [b10]. In 105 dyads, social sensitivity partly replicated (beta=0.39) but equal turn-taking did not [b11]. |
| Zhang and Norman external-rule advantage | Never directly replicated in the sources read. A related test (Fansher) found the effect was on completion, not move quality, and mental solving gave goal-recursion strategy on the next problem [b08]. |
| Hutchins' cockpit claim | Not testable as stated. No replication exists. |
| Kirsh and Maglio epistemic action | No controlled replication found. Mental-rotation timing is a pilot with N=3 [a13]. |
| Offloading bias (Gilbert paradigm) | Consistent over six or more studies; training effect replicated within the Ngai and Gilbert paper (N=164, then N=416) but decayed by post-task [b03, b04]. |

### 5.2 Replications and failures (LLM work)

- **Debate.** Du et al. 2023 is the only large positive. Four independent re-tests (Smit 2024, Zhang 2025, Choi 2025, and MAST's own comment that multi-agent gains are often minimal against single-agent or best-of-N) find no reliable edge at matched compute [a21, a22, c07, c08, d01, d03, c25]. Du et al. themselves note that models stayed confident when wrong [c05]. This is the best-supported negative result in the folder (K05, K20, established). The disagreement is mainly about the baseline: Du compared with a single sample, reflection and majority vote at unspecified token cost; Zhang matched cost against self-consistency [critique].
- **Heterogeneity.** Unresolved. Zhang 2025 says mixing models is the one fix that works [c09]. Self-MoA says one strong model resampled wins [d16]. AgentNet is mixed and inside noise [d17]. A likely reconciler: mixing helps when the added models are about as good (the quality gap decides). Tokens are not matched across the studies.
- **Self-correction.** Without an external signal it hurts (Huang). Tool-based critique helps (CRITIC). Locating the error is the weak point (Tyen) [b18, d05-d07].
- **SWE-agent.** Single-source; critique.md corrected the shell-only baseline from 7.3% to 11.00% [c19].
- **MAST interventions.** Structured fixes help but modestly [b13].
- **CoThinker.** Big gains on high-load tasks, a pooled 3.8% loss on instruction following, weak on small models [a25, c18].
- **Evidence duplication.** Many evidence lines describe the same paper (Du, Kim, MAST, Zhang, MATM). Independent-source counts in claims.jsonl count papers, not lines.

### 5.3 Moderators that recur

| Moderator | Direction | Evidence |
|---|---|---|
| Single-agent accuracy above ~45% | Extra agents hurt | [a24, d11] |
| Sequential vs decomposable task | Sequential: multi-agent -39% to -70%. Decomposable: up to +80.8% | [b14, d12] |
| Task load | Coordination pays at high load, costs at low (-3.8% pooled on instruction following) | [a25, c18] |
| Model size | Small models gain little from gated retrieval or from CoThinker's shared memory | [d14, a25] |
| Relevance of what is shared | Same-type trajectories beat cross-type | [d13] |
| Scope of memory | Role-local beats shared | [c14] |
| External signal in the loop | Decides whether debate or critique helps at all | [d02, d07] |
| Team size | Non-monotonic; each extra member -8% odds in a coordination game | [a27, c15, b21] |
| Capability gap, producer to consumer | Small and not significant in MATM | [d13] |

### 5.4 Interventions that worked

- External check that returns a location (true location gives +18 to +44 points on wrong traces) [d06].
- Tool-based critique over tool-free [d07].
- Sample-and-vote at matched tokens [a20, d01].
- Verification of the actual task objective in a multi-agent flow (+15.6% on ProgramDev) [c11].
- Linter guardrail and windowed view in an agent-computer interface [c20].
- Relevant, reranked, one-unit trajectory retrieval [d13].
- Feedback-based calibration of offloading (humans) [b03].

### 5.5 Interventions that did not work

- Debate between copies of one model, at matched compute [c08, d01].
- Forced disagreement (Multi-Persona devil agent lowered performance vs the first agent alone) [c07].
- Reflection on its own answer without a signal [b18; reflection took Du's MMLU from 63.9 to 57.7, c06].
- Always-retrieve (inferior to gated retrieval when a good gate exists) [d14].
- Predictions about one's own memory without feedback [b03].
- Fixed role splits imposed from outside, in human couples (assigned categories made couples worse than strangers) [a16, second-hand].
- Full history in the observation window (15.0 vs 18.0) [c20].

## 6. Language models

### 6.1 Behaviour on multi-voice tasks

- **Copies agree for the wrong reasons.** In Du et al.'s own words, models "would confidently affirm that their answer is correct" even when wrong [c05]. Debates converged but not always to the truth.
- **Voting captures the gain.** Qwen2.5-7B, 5 agents: vote 0.7691 vs best debate 0.7377 vs single 0.7205 (+4.9 points for the vote over single). On arithmetic, vote 0.99 vs single 0.814 vs debate T=5 0.67 [d01]. Longer debate got worse in that case (T=2 0.7377, T=3 0.7112, T=5 0.7050).
- **Token view.** Debate costs T times a voting round. Self-consistency converts extra tokens into accuracy; debate frameworks show no trend or stay below it [d04]. In 34 of 45 GPT-4o-mini conditions CoT-style baselines beat the debate variants.
- **Scaling the number of agents** by plain sampling: GSM8K +12 to +24, MATH +6 to +10 [a20]. Same-model samples are correlated, so returns diminish (G4).
- **Group size** in a coordination game: -8% odds per added member [b21].
- **Failures are structural.** 41-86.7% failure across 7 multi-agent frameworks. The biggest clusters: system design 41.8%, misalignment 36.9%. A single agent with an external program avoids the misalignment cluster by construction [b12].

### 6.2 Behaviour on self-checking

- Self-correction without an oracle lowered accuracy: CommonSenseQA 75.8 to 38.1 [b18].
- Error location is the hard part: GPT-4 52.87 overall on locating the first wrong step [d05].
- With the right location, repair is strong; with a random location, the gain halves and harm to correct traces grows [d06]. A locator at 60-70% accuracy already gives net gain on most tasks.
- A tool in the loop makes the difference (HotpotQA F1 50.5 vs 46.1 without tool) [d07].
- Caveat: all of this is 2023-24 models (GPT-3.5, GPT-4, PaLM 2, text-davinci-003). Current reasoning models have not been tested in these sources.

### 6.3 What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Custom interface (lint, window, summarised search) | +7.0 points on SWE-bench Lite (11.0 to 18.0, GPT-4 Turbo) | [c19] |
| Removing lint | -3.0 | [c20] |
| Verifier on task objective (ChatDev ProgramDev) | +15.6% | [c11] |
| Role-clarifying prompts (ChatDev) | +9.4%; ProgramDev 25.0 to 34.4 | [b13] |
| Shared trajectory retrieval, ALFWorld | +8.0 points dense; up to +17.2 with reranker | [d13, b23] |
| Shared trajectory retrieval, WebArena | +2 points | [c16] |
| Memory/reflection/planning (believability) | 21.21 to 29.89 TrueSkill | [c03] |
| Heterogeneous debate over homogeneous | +6.4% (SoM), +8.2% (EoT) | [c09] |
| Resample best model over mixing | +6.6 on AlpacaEval 2.0 | [d16] |
| Majority-conform update in debate | 0.7332 to 0.7625 | [d02] |
| Tool use in critique (HotpotQA F1) | +4.4 | [d07] |
| True error location in backtracking | +18 to +44 on wrong traces | [d06] |
| Self-aware tool use (trained) | -24% tool calls, +37% relative performance | [d15] |
| Centralized debate topology (Qwen 7B) | 0.6551, worse than single agent 0.7205 | [d01] |

### 6.4 Interface effect for current models

The SWE-agent gain was measured with GPT-4 Turbo. A bash-only agent is claimed above 74% on SWE-bench Verified [d10], which suggests stronger models absorbed much of the interface advantage. This is a README claim with an unnamed model and a different subset, so it is not a controlled comparison. The right reading is: interface design had a large effect in 2024, and its size for current models is unknown.

### 6.5 What is missing

- No LLM study tests Hutchins' propagation prediction [c26].
- No LLM study injects errors into one of two redundant representations [K21].
- No study matches tokens between probing and long deliberation [K24].
- No study tests predict-then-check before tool calls [K16].
- No test of gated vs always-retrieve with a self-judged gate [K23].
- Frontier reasoning models are mostly absent from the debate re-tests (they use 7B-70B, GPT-4o-mini, Claude-3.5-haiku).

## 7. What our agent should take

Status marks: [E] established (at least two independent sources, or already established in the schema), [S] single-source, [C] contested.

### Add now (established)

1. **No debate operator; single agent plus code-side vote and verifier.** Part: G9, G4, section 4b (already there). [E] Evidence: a21, b15, c08, d01, d03, d04, d02 (K05, K20). Nothing new to add; suggested update to the G9 evidence column: vote 0.7691 vs best debate 0.7377 vs single 0.7205 (Qwen2.5-7B, 5 agents, 7 benchmarks), and the martingale result that debate without an outside signal leaves expected correctness unchanged.
2. **Self-review without an outside signal does not help; a check should return a failing step location.** Part: G2, G3, S4, S5, S8. [E] for "no-signal self-review hurts": b18, c06, d05. Already in the schema. Strengthen G2 with d06: true location gives +18 to +44 points on wrong traces, random location about half. The wider claim "tool critique beats tool-free" is single-source (see Test first).
3. **Rules that can be checked live in code, not only in the prompt.** Part: G2, S4, S0 state. [E] in humans for the direction (a08-a10, a18); for LLMs support is indirect (c20 linter, c11 verifier; K01). Design principle already followed; tag it "external rule = checker" in the run log.
4. **Scoped, relevant, capped memory retrieval.** Part: memory (lessons, subgoal library), S9. [E] Evidence: a26, c16, d13, c14, c03 (K12). Rules: one retrieved unit per use; same problem class only; store per class or role rather than one pool. The gate (retrieve only on a signal) is [S].
5. **Do not use the Google-effect priming, collective factor c, social sensitivity or turn-taking as design guides.** Part: none. [E, as negative] Evidence: b01, b10, b11.
6. **Log per-class tool-call usefulness.** Part: S9 class record. [E] that offloading is a biased choice in humans (b03, b04; K16). Cost is zero, and it creates the data for U3 (predict-then-check).

### Test first (single-source or contested)

Each item names its part, status and evidence ids. Tests are in section 8 and UNKNOWNS.md.

1. **Sample-and-vote as the best-of-N baseline arm** (S3, S7). [S] a20, b19, d01, K07. Measure marginal gain per token against the scaffold.
2. **Verifier that returns a step location, using tool output** (G2, S4, S5). [S] d05, d06, d07, K08, K21.
3. **Redundant second representation with code-side mismatch check** (G3, S8). [S, Hutchins analogy only] a05, a06, K02, K19, K21.
4. **Probe-before-reason operator** (O, S3/S4). [S] a12, a13, b07, d18, K03, K24.
5. **Predict-then-check before a tool call or retrieval** (G, S0). [S, human only] b03, d15, K16.
6. **Gated vs always-retrieve of past cases** (memory). [S/C] d13, d14, K23.
7. **Single-vs-split router: single score above 45% means stay single; split only if subtasks are independent** (S0). [S] a24, d11, d12, K10, K22.
8. **Observation shaping: windowed view, linter feedback, short history** (S4 harness). [S, 2024 models] c20, d08, d10, K11.
9. **Heterogeneous mixing vs resampling the best model** (S3). [C] c09, d16, d17, K06. Lean: resample the best model first.
10. **Typed artifact format (claim, source, check status) vs free-text notes** (S0/S9, memory). [S] c01, c02, c12, a03. Weak: conceptual review plus MetaGPT with garbled tables.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (prompt plus output including setup, per G7). Report per-arm pass rate with 95% interval; at least 100 items per class or a paired design. Use items with a runnable check.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Tasks with checkable answers (ARC-style program tasks, code with tests, arithmetic) | (a) k independent samples + code vote; (b) 2-round critic with no tool; (c) 2-round critic given test output | Accuracy; margin over (a) | (a) at least equal to (b). (c) beats (a) only if the test gives step location. Prior: d01, d04. |
| T2 | Items where we inject a known error (wrong number, wrong step) into an intermediate table paired with a prose summary | (a) same-text re-read; (b) code-side mismatch between table and prose; (c) run the test | Catch rate; false-alarm rate on clean items | (b) and (c) above (a). Direction from d05, d07; the mismatch arm is new. |
| T3 | Code tasks where a probe is cheap (run function on one input) | (a) k cheap probe runs then answer; (b) one long reasoning pass | Accuracy at equal tokens; probe count | (a) better where the probe separates candidates. ReAct-type prior, d18. |
| T4 | Tool-call decisions (calculator, search, code) on items the model can partly answer alone | (a) always call; (b) never call; (c) predict-then-check with per-class calibration | Tool calls per item; accuracy; tokens | (c) cuts calls with no accuracy loss. Prior: d15 (trained), b03 (human). |
| T5 | Repeated problem classes with a stored case library | (a) no retrieval; (b) always retrieve one case; (c) retrieve only on impasse or low-agreement signal | Pass rate; tokens | (c) at least equal to (b) with fewer tokens; (b) beats (a) only if same-class. Prior: d13, d14. |
| T6 | 40 items labelled sequential or parallel before running | (a) single agent; (b) 3 workers + central verifier | Sign of (b) minus (a); correlation with label | Label predicts sign. Prior: d12. Run only on items where single score is below 45%. |
| T7 | Tool-loop tasks (code edit or file task) | (a) raw tool output; (b) windowed view (100 lines) + lint feedback + last 5 observations | Resolve rate; failed edits per trajectory | (b) ahead on weak models; small or none on current frontier model. Prior: c20, d10. |
| T8 | Single-answer reasoning items | (a) N samples from best model; (b) N samples spread over 2-3 models | Accuracy at equal tokens | (a) ahead if quality gap is large. Prior: d16 vs c09. |
| T9 | Multi-step tasks with typed notes | (a) free-text scratchpad; (b) typed record (claim, source, check status) | Error carry-over rate; tokens | (b) lower carry-over. Weak prior: c01, c12. |

Pre-registration notes: fix the analysis before running; report move or step counts as well as solve rate (Fansher found external support raises completion but may leave move quality flat [a18]).

## 9. What does not transfer, and why

- **Social-group findings (collective intelligence c, turn-taking, social sensitivity, couples' transactive memory).** They concern humans with different knowledge and motives. Copies of one model share errors (G4). Also contested in humans [b10, b11, a17].
- **The Google effect.** Priming result failed to replicate [b01]. Our agent has no attention that tool-related words capture.
- **Epistemic action timing numbers (100 ms vs 800-1200 ms).** Human perception and motor speeds. Only the principle (probe before simulating) carries over, and the LLM token trade-off is unmeasured.
- **Cultural history of artefacts (Hutchins' navigation).** An agent's artefacts are designed in advance, not accumulated by a community over years.
- **Human cost of offloading (cognitive debt, EEG).** Small, preprint, correlational [b06, c21, c22, b05]. The agent has no skill to lose. The useful residue: keep human checkpoints active, not passive.
- **Multi-agent debate and role-play teams.** Tested and found weak; also against G4, G9.
- **SWE-agent numbers.** Tuned for GPT-4 Turbo on Lite; current models differ (d10). Keep the principle, not the percentages.
- **CoThinker's transactive-memory component.** Less effective on newer models that refuse to expose step-by-step reasoning [a25]. We also hold that reasoning text is not evidence (G10).
- **Zhang and Norman layouts (location beats size/colour).** Perceptual encoding in humans. Text-in, text-out models may handle tables and prose differently; the format effect for LLMs is untested.

## 10. Open questions

1. Does a critic or debate step beat self-consistency at equal tokens on current frontier reasoning models, with an external verifier present? (d01-d04 only cover small and mid models.)
2. Do redundant representations catch injected errors in an LLM agent better than a single self-check? (No direct study.)
3. How much of the SWE-agent interface gain survives with current models, and does it hold outside code?
4. Can decomposability be judged before running? (Kim's 87% held-out accuracy uses trace-measured predictors.)
5. Does predict-then-check cut tool and retrieval over-use in an LLM agent without hurting accuracy?
6. What is the LLM analogue of the Tetris gap: probes versus deliberation at equal tokens?
7. Does shared trajectory memory transfer to our tasks, and does a self-judged gate beat always-retrieve?
8. Does the Sparrow location-memory result replicate (humans), and would an index-only memory help an agent?
9. Heterogeneous mixing vs best-model resampling at matched tokens?
10. Exact Zhang and Norman 1994 numbers were not re-opened after the first pass; Hutchins' book, Wegner 1991, Sparrow 2011 and Risko and Gilbert 2016 were never opened.
11. HumanEvalFix: the text says 88.3, the table gives 87.7 / 89.7 / 87.9 (mean 88.4). The aggregation is not stated.
12. Where is the break-even between a free-text scratchpad and a typed artifact contract?

## 11. Sources

[V] = opened this session (full text or page text). [M] = snippet only or not opened.

Human DC and offloading
- [V] Hollan, Hutchins, Kirsh (2000) Distributed cognition: toward a new foundation for HCI research. https://hci.ucsd.edu/hollan/Pubs/tochi-revised.pdf (a01-a03; b24 lists the same paper as not read in depth)
- [V] Hutchins (1995) How a cockpit remembers its speeds. https://courses.ischool.berkeley.edu/i290-3/s05/papers/How_a_cockpit_remembers_its_speeds.pdf ; https://doi.org/10.1207/s15516709cog1904_1 (a04-a07, b09)
- [V] Zhang and Norman (1994) Representations in distributed cognitive tasks. https://pages.ucsd.edu/~scoulson/203/zhang.pdf (a08-a11; not re-opened by the critique pass)
- [V] Kirsh and Maglio (1994) On distinguishing epistemic from pragmatic action. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf ; https://doi.org/10.1207/s15516709cog1804_1 (a12, a13, b07)
- [M] Hutchins (1995) Cognition in the Wild. https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/ (a14)
- [V] Stanford Encyclopedia of Philosophy, Embodied Cognition. https://plato.stanford.edu/entries/embodied-cognition/ (a15; first 100000 of 114500 characters)
- [M] Wegner, Erber, Raymond (1991) Transactive memory in close relationships (via Harris et al.) (a16)
- [V] Harris, Keil, Sutton, Barnier, McIlwain (2011) We remember, we forget. https://www.ida.liu.se/~729G12/mtrl/Harris%20et%20al.%202010.pdf (a17)
- [V] Fansher, Shah, Helie (~2020 preprint) Effect of mode of presentation on Tower of Hanoi problem solving. https://ccn.psych.purdue.edu/papers/Fansher-TOH.pdf (a18, b08)
- [V] Camerer et al. (2018) via FLoRA atlas record of Sparrow 2011. https://forrt.org/flora-replication-atlas/doi/10.1126/science.1207745/ (b01)
- [M] Sparrow, Liu, Wegner (2011) Google effects on memory. https://doi.org/10.1126/science.1207745 (b02)
- [V] Ngai and Gilbert (2026) Metacognitive training facilitates optimal cognitive offloading. https://pmc.ncbi.nlm.nih.gov/articles/PMC12982714/ (b03, b04)
- [V] Zhu, Li, Dong, Chang, Fan (2026) Dependent vs autonomous cognitive offloading to generative AI. https://pmc.ncbi.nlm.nih.gov/articles/PMC13420724/ (b05)
- [V] Kosmyna et al. (2025) Your Brain on ChatGPT. https://arxiv.org/abs/2506.08872 (b06, c21)
- [V] Lee et al. (2025) The Impact of Generative AI on Critical Thinking. https://doi.org/10.1145/3706598.3713778 (c22)
- [V] Collective intelligence literature as summarised in a 2025 paper (Woolley 2010; Credé and Howardson 2017; Barlow and Dennis 2016; Bates and Gupta 2017; Rowe 2021; Graf 2019; LePine 2008) and the 2025 dyad study. https://pmc.ncbi.nlm.nih.gov/articles/PMC12460217/ (b10, b11). The primary papers are [M], read through the summary.
- [M] Risko and Gilbert (2016) Cognitive offloading. https://doi.org/10.1016/j.tics.2016.07.002 (b25; 403)
- [V] Wikipedia: Blackboard system. https://en.wikipedia.org/wiki/Blackboard_system (c24)

LLM and AI
- [V] Du et al. (2023) Multiagent debate. https://arxiv.org/abs/2305.14325 (a19, b17, c05, c06)
- [V] Li et al. (2024) More agents is all you need. https://arxiv.org/abs/2402.05120 (a20, b19)
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate. https://arxiv.org/abs/2502.08788 (a21, b15, c08, c09, d04)
- [V] Smit et al. (2024) Should we be going MAD? https://arxiv.org/abs/2311.17371 (a22, b16, c07, d03)
- [V] Choi, Zhu, Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536 (d01, d02)
- [V] Cemri et al. (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657 (a23, b12, b13, c10, c11, c25)
- [V] Kim et al. (2026) Towards a science of scaling agent systems. https://arxiv.org/abs/2512.08296 (a24, b14, d11, d12)
- [V] Shang et al. (2026) United minds or isolated agents? (CoThinker). https://arxiv.org/abs/2506.06843 (a25, b22, c18)
- [V] Kim et al. (2026) Multi-Agent Transactive Memory. https://arxiv.org/abs/2606.19911 (a26, b23, c16, c17, d13)
- [V] Wu et al. (2026) Scaling teams or scaling time? LLMA-Mem. https://arxiv.org/abs/2604.03295 (c14, c15; a27 had abstract-level numbers only)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b18)
- [V] Li, Lin, Xia, Jin (2025) Rethinking Mixture-of-Agents. https://arxiv.org/abs/2502.00674 (b20, d16)
- [V] Riedl (2026) Emergent coordination in multi-agent language models. https://arxiv.org/abs/2510.05174 (b21)
- [V] Zhou et al. (2026) Externalization in LLM agents. https://arxiv.org/abs/2604.08224 (c01, c02, c26)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c03, c04)
- [V] Hong et al. (2023) MetaGPT. https://arxiv.org/abs/2308.00352 (c12; table layout garbled)
- [V] Wang et al. (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692 (c13)
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793 (c19, c20, d08, d09)
- [V] mini-SWE-agent README. https://github.com/SWE-agent/mini-swe-agent (d10)
- [V] Rosenbacke et al. (2026) From consumption to reflection. https://arxiv.org/abs/2606.11195 (c23; conceptual)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516 (d05, d06)
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d07)
- [V] Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511 (d14)
- [V] Qian et al. (2025) SMART. https://arxiv.org/abs/2502.11435 (d15)
- [V] Yang et al. (2025) AgentNet. https://arxiv.org/abs/2504.00587 (d17)
- [V] Yao et al. (2023) ReAct. https://arxiv.org/abs/2210.03629 (d18)
