# Distributed cognition theory: deep document

*Subfield F02.01. Evidence ids (a01 to d16) point to evidence_a-d.jsonl; claim ids (F02.01-K01 to K30) point to claims.jsonl; critique.md holds the cross-check. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Distributed cognition (DC) says that thinking is not only in the head. The unit of analysis is a whole functional system: people, tools, written records and the rules that link them. The system "remembers", "computes" and "decides". The same questions (what is represented, how is it transformed, how does it move) are asked of the system as a whole.

Two principles define it (a01, Hollan, Hutchins and Kirsh 2000):
1. The boundary of the system is set by functional relations among parts, not by skin or skull.
2. Cognitive events are not all inside individuals. They include handling objects and passing representations between people and artefacts.

Three kinds of distribution (a01, b01): across people; between internal and external structure; across time (earlier products change later events).

The authors' own line: "A process is not cognitive simply because it happens in a brain, nor is a process non-cognitive simply because it happens in the interactions among many brains." (a01)

Central hypothesis (a03): the cognitive and computational properties of a system can be explained by how constraints are organised and propagated. There is no gulf between "inside" and "outside" that must be bridged by translating the world into internal symbols.

Status of the theory itself. It is a framing and a method, not a falsifiable claim. Hutchins says no experiment could prove or disprove the perspective, because the perspective makes no empirical claims; hypotheses inside it (for example extended cognition) can be tested (a15). The founding papers give no effect sizes (a01, a07, b02). So everything below about "what works" comes from component studies: human offloading work, and engineering ablations on language-model agents, read through the DC lens. No paper we found tests DC predictions directly on an LLM agent. None of 11 key AI papers cites Hutchins (c21, c22; K20, K30).

Why it matters for our agent. It gives a licence to treat "model + program + checks + notes" as one system whose parts must be coupled, and to ask where each piece of work should sit. The evidence says most of the gain comes from three kinds of external part: an exact executor, a persistent store, and an outside signal (c23). Gains from the model talking to itself or to copies of itself are small or fragile.

## 2. History and theories in depth

**Roots.** Gibson's ecological psychology, Bateson's ecology of mind and Soviet cultural-historical activity theory (a18). Bateson's blind man with a stick: draw the system boundary so that no pathway carrying difference is cut. Wikipedia lists earlier lineage (Roberts 1964) and later variants: Salomon 1997 (shared cognition vs off-loading); Sutton 2006 (five domains: external tools and symbols, natural environment, social scaffolding, embodied skills, internalised artefacts) (a20, tertiary source).

**Hutchins 1995, "How a cockpit remembers its speeds" (a07 to a09).** Cognitive Science 19, 265-288. The cockpit is the unit. Memory for approach speeds is held in speed cards, speed bugs on the airspeed dial, the pilots' speech and the pilots' heads. The speed bug does not make the pilot remember better. It reconfigures the task. Without a bug the pilot must recall the target speed, read the scale and compare numbers. With the bug set, the task becomes a judgment of spatial adjacency between needle and bug. Media differ in persistence (card permanent, speech ephemeral, bug state robust against interruption, pilot memory unknown). The system holds redundant storage and processing. The author observed over 100 flights and never saw a crew fail to compute and set approach speeds. No error rates, no raw tables; the account is "somewhat stylized". A second example (a04): round airspeed dials work as a material anchor for a space of speeds, and glass-cockpit speed tapes from four manufacturers lost that feature. That claim rests on ethnography only.

**Kirsh and Maglio 1994, epistemic vs pragmatic action (a10 to a12, d14).** Pragmatic action moves toward the goal. Epistemic action changes the world to make thinking easier, faster or more reliable. In Tetris, players rotate a piece more than placement needs. A plan-then-act model predicts 1.5 rotations for a 4-orientation piece. Observed counts were above that for every piece type (exact means only in figures). Physical rotation takes as little as 100 ms (plus about 200 ms of button time), against an estimated 800-1200 ms for mental rotation. That estimate comes from a pilot with 3 players (d14). Early rotation also exposes hidden parts 150-300 ms earlier than waiting (a piece falls one square per 150 ms at medium speed and takes about half a second to appear in full). The authors list five epistemic uses; only some are backed by data in the paper. They admit one cannot always tell epistemic from pragmatic action. No independent replication found.

**Hollan, Hutchins and Kirsh 2000, HCI foundation (a01 to a06, b01, b02).** Guiding principles: people establish and coordinate structure in the environment; coordination takes effort; people offload effort to the environment whenever practical; social organisation gives better load balancing (a02). Proposed research loop: principles guide ethnography; ethnography suggests experiments and designs; designs create new workplaces (a05). Kirsh's space studies (cooking, assembly, packing, Tetris) say spatial arrangement simplifies choice, perception and internal computation. The authors say the conjecture was "strongly confirmed" but give no counts (a06). They admit cognitive ethnography is at times underconstrained by data and propose "ethnographically natural" experiments (b02).

**Clark and Chalmers 1998, extended mind (a13, a14).** Philosophical. Parity principle: if a part of the world works as a process we would call cognitive were it done in the head, it is cognitive. Four conditions for external storage to count as belief (Otto's notebook): a constant in the agent's life; directly available; automatically endorsed on retrieval; endorsed in the past (condition 4 is "arguable"). Critics (Adams and Aizawa, Rupert) were not read. Hutchins separates DC from extended mind: DC makes no claim about where "the mind" is (a15).

**Later Hutchins (a15 to a19).** 2010, cognitive ecology. 2012 and 2013: communities of connectionist networks (Hutchins and Hazlehurst 1991, 1995) in which language-like shared patterns emerge with no teacher; these are existence demonstrations, not fits to human data (a16, a17). 2009: automation surprise in cockpits explained as a gap in allocation of attention (attention on control functions neglects guidance parameters and the reverse); five case studies, no rates (a19).

**Zhang and Norman 1994, representations in distributed tasks (a21).** Tower of Hanoi isomorphs: performance depends on how the task is spread over internal and external representations. NOT opened (publisher blocked). No number from it may be cited.

**Interactivity programme, Vallee-Tourangeau (a22 to a24).** Lab experiments showing that moving physical tokens helps arithmetic under memory load and helps insight problems. See Section 3.

**Collective intelligence and transactive memory (b06 to b08).** Woolley 2010: a group factor c (192 groups, 699 people). Riedl 2021 meta-analysis. Ren and Argote 2011 on transactive memory. All three seen only as snippets, not opened. Recorded as pointers.

**Modern restatement (a33).** Clark 2025 (Nature Communications comment): humans are extended minds; fear of AI offloading repeats the old fear of writing. Opinion, no data.

## 3. Core findings with exact numbers

Human and conceptual studies first, then AI component studies.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Cockpit memory is held by cards, bugs, speech and heads; the bug turns recall into a visual adjacency check | Over 100 flights observed; no failures to set speeds seen; no error rates | a07, a08, a09 (Hutchins 1995) | [S] qualitative |
| Players act on the world to think (Tetris rotations) | Observed rotations above the expected 1.5 for all pieces; 100 ms physical vs 800-1200 ms mental per 90 deg; mental rotation pilot n=3 | a10, a11, d14 (Kirsh and Maglio 1994) | [S] descriptive |
| Interactivity cushions a working-memory load | N=52; correct, low interactivity: 56.0% no suppression, 26.9% with; high interactivity (tokens): 63.5% vs 44.6%. Interaction p<.05. Digits not re-verified | a22 (Vallee-Tourangeau 2016) | [S] one lab |
| Physical materials raise insight solving | Exp 1 N=63: 12/28 (43%) solved with chains vs 2/35 (6%) with paper. Exp 2 N=55. Earlier work cited: under 3% vs 30% in 10 min | a23 (Henok 2020) | [S] one lab; Chuderski 2021 reportedly mixed (a24, second-hand) |
| Google-effect priming did not replicate | Original N=46; Camerer N=104 (+130) failed; this study 117 tested, 89 analysed, BF01=5.07 for null; RT 825 vs 821 ms | b03, b04 (Hesselmann and Gollo 2020) | [C] priming claim failed; offloading itself not refuted |
| Social-science replication base rate | 13/21 (62%) replicated; effect about 50% of original | a25 (Camerer 2018; b05 figures from memory) | [S] |
| Trusting an external list lowers internal memory | N=40; recall t(38)=7.22, d=2.28; category access d=1.85; clustering d=1.04 | d15 (Magen and Tomer-Offen 2025) | [S] |
| LLM-assisted writing weakens recall of own text | N=54 (18/group); failed to quote own essay 15/18 vs 2/18 vs 2/18, p<.001 | a31, c20 (Kosmyna 2025, preprint) | [S] human only |
| Real interpreter is the source of program-aided gain | GSM8K Codex: direct 19.7, CoT 65.6, PAL 72.0, model-simulated execution 23.2. (Paper text says "4.5 above direct"; the arithmetic gap is 3.5.) | a26, a27, c02, b22 (Gao 2022), critique | [S] one paper |
| Executor stays accurate with large numbers | GSM-HARD: PAL about 61 (61.2 or 61.5); CoT 20.1 to 23.1 depending on spot in paper | a26, c01, c04 | [S] |
| Weak coder gets no PAL gain | text-davinci-001 worse with PAL than CoT | a27 | [S] |
| Calculator tool helps little vs full interpreter | Codex +2.3, PaLM-540B +1.7 vs PAL +6.4 (cross-setup) | c03 | [S] |
| Tool-integrated RL on hard math | AIME24: Qwen2.5-Math-7B Instruct 10.0, TIR 26.7, SimpleRL-Zero 33.3, ToRL-7B 43.3; 1.5B: 10.0, 13.3, ToRL 26.7. Rows differ in training recipe | d08 (ToRL 2025) | [S] not a clean ablation |
| Code emulator hybrid | BBH 23 tasks, davinci-003: direct 55, CoT 72, CoC 84; PaLM-2-S*: 49, 61, 78; GPT-4 CoC 91; human 68. Python-only fails non-algorithmic tasks | d09 (Chain of Code) | [S] 2023 models |
| Written scratchpad helps multi-step computation | Polynomials: few-shot 8.8 to 20.1, fine-tuned 31.8 to 50.7. Execution: 11 to 26.5* few-shot (relaxed scoring), 20 to 41.5 fine-tuned. Addition 9-10 digits OOD: complete failure without. Real MBPP: 5% scratchpad vs 10% direct | a28, c05, c06 (Nye 2021) | [S] |
| Intrinsic self-correction fails | GPT-4 GSM8K 95.5/91.5/89.0 over rounds; GPT-3.5 GSM8K 75.9/75.1/74.7; CSQA 75.8/38.1/41.8; GPT-4 HotpotQA 49.0/49.0/43.0 | a29, b19, c07 (Huang 2024) | [E] for prompted self-feedback on non-reasoning models |
| Oracle signal makes correction work | GPT-4 GSM8K 95.5 to 97.5; CSQA 82.0 to 85.5; HotpotQA 49.0 to 59.0. GPT-3.5 GSM8K 75.9 to 84.3; CSQA 75.8 to 89.7 | c08 | [E] but the oracle is an upper bound |
| Self-correction blind spot | 14 non-reasoning models: 64.5% blind spot; Claude Sonnet 4 41.4%; Claude 3.5 Haiku 52.5%; "Wait" cuts it 89.3% and lifts accuracy 156% (DeepSeek-V3 0.567 to 0.902); reasoning-trained models about zero | d06 (Tsui 2025) | [S] injected errors |
| Debate gain is mostly extra samples | Du: arithmetic 67.0 single, 72.1 reflection, 69.0 majority, 81.8 debate; GSM8K 77.0/75.0/81.0/85.0; chess 91.4/102.1/102.2/122.9. Later cost-matched work: gain gone. Token-matched 2026: single 0.418 vs debate 0.388 at 1000 tokens | b23, c10, c09, b09, b10, b11, d01 | [E] |
| Reflection can lower accuracy | Du MMLU 63.9 to 57.7; Reflexion Leetcode-Hard 77.1 vs 80.1 (GPT-4) | c11, c12 | [E] |
| Voting gain grows with difficulty | GSM8K +12 to +24; MATH +6 to +10; MMLU +5 to +11; HumanEval +4 to +9; Chess +1 to +4; Llama2-13B at 59% matched 70B | b24 (Li 2024) | [S] |
| Multi-agent systems fail often | 7 systems, 41% to 86.7% failure; 14 modes in 3 groups (design 41.8%, misalignment 36.9%, verification 21.3%); kappa 0.88; 150 traces for taxonomy, 1642 total; repetition 15.7%, reasoning-action mismatch 13.2%, missed completion 12.4%, spec disobedience 11.8%; premature end 6.2%, no verification 8.2%, wrong verification 9.1% | b13, c15, c17 (Cemri 2025) | [S] LLM-annotated, 94% agreement with humans |
| Cheap structural fixes | ChatDev: role fix +9.4%; high-level verification step +15.6% | b14, c16 | [S] one system |
| Gains depend on task structure | 260 configs, 6 benchmarks; range +80.8% (finance) to -70.0% (sequential planning); finance centralized 0.631 vs single 0.349; planning -39% to -70%; web decentralised +9.2%; SWE-bench single 0.522, hybrid -2.1%, centralized -3.1%, decentralised -5.4%, independent -14.9%; cap beta -0.236 (p=.004); R2cv 0.373/0.413 | b15, b16, b18, d02 (Kim 2025/2026) | [S] correlational |
| Error spread | Independent 17.2x vs centralized 4.4x (decentralised 7.8, hybrid 5.1); but amplification as regressor beta 0.014, p=.658 | b17, critique | [S] descriptive only |
| Single agent wins at matched thinking tokens | Mean at 1000 tokens: single 0.418, debate 0.388, roles 0.381, sequential 0.379, subtask-parallel 0.369, ensemble 0.333; at 5000: single 0.427, debate 0.420. Four model families, FRAMES and MuSiQue | d01 (Tran and Kiela 2026) | [E] with b09-b11, d11 |
| Parallel vs extended thinking | Parallel up to 20% above extended; per-prompt compute split gives over 4x efficiency vs best-of-N | d12, d13 (abstract level) | [S] |
| Verifier loop lifts planning | Autonomous GPT-4 about 12%; Blocks World 82% (up to 15 backprompts); Logistics 70%; Mystery BW about 10% | a30 (Kambhampati 2024, cited results) | [S] |
| Execution feedback in memory loop | Reflexion HumanEval 91.0 vs 80.1; ALFWorld +22 pts (134 tasks); HotpotQA +20 | c12 | [S] relies on test signal |
| Skill library as memory | Voyager: 63 unique items, 3.3x baselines; random curriculum cut items 93%; GPT-4 needed; 3 runs | c13 | [S] Minecraft only |
| Memory paging (authors' benchmark) | MemGPT deep-memory retrieval GPT-4 32.1% to 92.5%; GPT-3.5 38.7% to 66.9% | c14 | [S] author benchmark, LLM judge |
| Independent memory benchmark | GPT-5-mini long context 60.6; Claude-3.7 49.6; GPT-4o 48.8; BM25 RAG 41.5; MemGPT 28.3; MIRIX 26.2; Mem0 21.1; BM25 on accurate retrieval 60.5 vs 49.2 | d10 (MemoryAgentBench) | [S] |
| Reasoning text is not a faithful trace | Biasing features cut accuracy up to 36% over 13 BBH tasks, unmentioned (older models). Claude 3.7 25% and R1 39% verbalise hint use; reward hacks verbalised under 2% in 5 of 6 environments | c19, d03, d04 | [E] |
| Cognitive Workspace claims | 58.6% reuse, d of 23 to 196, GPT-3.5, 8 documents | a32 | Do not use |

## 4. Mechanisms and models

Each mechanism is stated so an engineer can build it.

**M1. Offload to an exact executor.** The model writes a program. A real interpreter runs it. The output (not the model's guess of the output) is the answer or the evidence. Coupling is the key: when the model "runs" its own code in text, PAL falls from 72.0 to 23.2 (a27). Requirements: the model can write correct code (a weak coder gets no gain); the task has a computable core; a fallback exists for lines code cannot express (Chain of Code lets the model simulate only the lines the interpreter cannot run, d09). Implementation: sandboxed interpreter, timeout, return stdout and exceptions to the model, count code and output tokens as spend.

**M2. Check from outside.** A verifier that is not the same generation process: unit test, rule-based validator (VAL in LLM-Modulo), held-out example, ground-truth label. Loop: propose, run verifier, backprompt with the verifier's actual output, cap the rounds (LLM-Modulo used up to 15; a30). Without a signal, a self-review round adds cost and can hurt (K04, K06). Reflexion's gain comes from test results (c12).

**M3. Externalise intermediate state (scratchpad, notes).** A visible buffer lets the model carry state it cannot hold in one pass (a28). Gain is large on long arithmetic and trace execution, absent on real MBPP (5% vs 10%). Treat the buffer as a working store, not as proof (see M7).

**M4. Epistemic action: probe to think.** The Tetris analogue is a cheap action whose only purpose is to reveal information: run a small test, print a value, try an example. Cost asymmetry drives it (100 ms vs 800-1200 ms). Rule for the agent: use an external probe when its token cost is below the cost of reasoning out the same fact. Evidence for LLMs is indirect only (K17).

**M5. Persistent store across time.** Distribution through time: earlier products shape later events. Forms: a skill library of verified code (Voyager), an episodic buffer of reflections (Reflexion), paged memory (MemGPT), a notes file. Independent evidence says long context often beats memory add-ons, and RAG wins on exact retrieval (d10). Organise notes by relation, not as a flat list (d15 human result, K29).

**M6. Coordination structure across several agents.** Worth it only when subtasks are independent. Centralised verification contains error spread (4.4x vs 17.2x for independent agents). Fixes that worked in one system: explicit roles (+9.4%), a high-level verification step (+15.6%). Rule of thumb from Kim: once the single agent is above about 45%, extra agents give negative returns. It is a fitted prior (K23). The default at equal thinking tokens is a single agent (d01).

**M7. Trace as non-authoritative.** Verbalised reasoning omits the real cause (25% and 39% faithful on current reasoning models). So claims must be tied to executed outputs. Implementation: the answer record cites a run id or check result, never a sentence of reasoning.

**M8. Re-entry cue.** Models fix an error placed in the user turn but not the same error in their own turn (64.5% blind spot). A cue such as "Wait", or a role flip (present own output as someone else's), cut the blind spot 89.3% in non-reasoning models (d06). It is a cheap layer before the external check. Reasoning-trained models show near-zero blind spot, so the cue may be redundant there.

**M9. Budget split.** Spend by difficulty (d12). Parallel short chains with a vote can beat one long chain (d13). Kim's own mechanism: a fixed budget split across agents leaves each too little to reason (budget fragmentation, d02).

**Computational model from DC itself (a16, a17).** Communities of connectionist networks. Each pairing produces a shared public structure while each net adapts. Interesting as theory, not directly usable; results are existence demonstrations.

## 5. What holds up

**Held up.**
- Intrinsic self-correction without a signal does not help non-reasoning models; with an external signal it does (Huang 2024, Kamoi survey, SCoRe, Self-Correction Bench). [E]
- Debate beats nothing once samples are equal (Huang, Smit, Wang, Tran and Kiela 2026). At 1000 thinking tokens single 0.418 beats debate 0.388. [E]
- Reasoning traces are partly unfaithful, on old and current models (Turpin 2023, Chen 2025). [E]
- Reflection can lower accuracy (Du MMLU, Reflexion Leetcode-Hard). [E]
- Real code execution adds accuracy on harder tasks than GSM8K (ToRL, Chain of Code), though neither is an equal-token real-vs-simulated ablation. [S]
- On an independent benchmark no memory add-on wins everywhere. [S]

**Failed or contested.**
- Google-effect priming did not replicate (BF01 = 5.07; also failed in Camerer). This is a failure of one lab effect, not of offloading. [C]
- Cognitive Workspace (a32) is unusable evidence.
- The original Du et al. debate headline shrinks at equal responses. Du used about 100-problem sets with one model playing every agent.
- Interactivity effects (Vallee-Tourangeau) come from one lab; Chuderski 2021 is reportedly mixed (second-hand). The Camerer base rate suggests halving single-lab effects (K21).
- Kim's 45% threshold was derived and tested on the same six benchmarks (94% match), per-cell CI about 20 points. Not tested outside. [S]
- Kim says multi-agent hurts on sequential tasks; Li (More Agents) says more agents help on most tasks. These are compatible if independent voting is separated from interacting agents. No head-to-head test exists.

**Moderators.**
- Code skill of the model (weak coder: PAL worse than CoT).
- Task type: sequential vs decomposable; difficulty (voting gain grows with it); size of the numbers (GSM-HARD).
- Prompt strength: with a strong single prompt (worked example), a single agent matches the best discussion framework (Wang 2024). Agreement intensity moved Multi-Persona from worst to best (+15% on 376 USMLE items; Smit).
- Context corruption: multi-agent leads only under heavy corruption or at 100 tokens (d01).
- Model generation: reasoning-trained models show about zero self-correction blind spot.

**Interventions that worked:** real interpreter; external verifier loop; test-result reflection; verification step (+15.6%); role clarity (+9.4%); "Wait" cue (non-reasoning models); skill library (Minecraft).

**Interventions that did not:** self-review with no signal; debate at equal samples; persona or role multi-agent at equal tokens; memory add-ons versus long context; model-simulated execution; a calculator alone.

**Human-side warnings.** Offloading lowered internal recall (d=2.28) and recall of own AI-assisted text (15/18 failed to quote). These are costs to humans, not to an agent. They bound any claim that offloading is free.

## 6. Language models

No paper tests DC theory on an LLM agent. What exists is component evidence.

- **Program-aided reasoning.** Codex GSM8K 72.0 (PAL) vs 65.6 (CoT). With larger numbers CoT collapses to about 20-23 while PAL stays near 61. Real execution vs model-simulated: 72.0 vs 23.2 (+48.8 points). Newer: AIME24 7B 10.0 plain, 26.7 TIR, 43.3 ToRL; BBH Chain of Code 84 vs CoT 72 (davinci-003), GPT-4 91.
- **Scratchpads.** Help on long arithmetic and synthetic traces. No help on real MBPP output prediction.
- **Self-correction.** GPT-4 GSM8K drops 95.5 to 89.0 in two rounds; an oracle gives 97.5. Non-reasoning models have a 64.5% own-error blind spot; reasoning-trained models about none. "Wait" removes 89.3% of it.
- **Multi-agent.** Debate, roles and ensembles lose to a single agent at matched thinking tokens (0.418 vs 0.388 at 1000; 0.427 vs 0.420 at 5000). MAST: 41% to 86.7% failure across 7 frameworks; verification-related modes about 23.5% of annotated failures; one verification step gave +15.6%. Kim: sequential planning -39% to -70% for every multi-agent variant; finance centralized 0.631 vs 0.349.
- **Voting.** Gains scale with difficulty: GSM8K +12 to +24, chess +1 to +4.
- **Memory.** MemGPT 32.1% to 92.5% on its own benchmark. On an independent benchmark MemGPT 28.3 and Mem0 21.1 trail long-context GPT-4o 48.8.
- **Traces.** Claude 3.7 verbalises hint use 25%, R1 39%. Reward hacks verbalised under 2% in 5 of 6 settings.
- **Planning.** LLM-Modulo: 12% autonomous to 82% (Blocks World) with a rule-based verifier. Numbers are cited from other papers.

Caveat: many figures come from 2022-2024 models (Codex, GPT-3.5, GPT-4). Transfer to current reasoning models is unknown, except where 2025-2026 papers (Tsui, Chen, Tran and Kiela, Kim, ToRL, MemoryAgentBench) speak to it.

## 7. What our agent should take

Each item: schema part, status, evidence ids.

### Add now (established)

1. **External signal for every revision.** A revision must cite the failing output of a program, test or ground-truth check, never the model's own opinion. Part: G2, G10 (already stated); verify state. [E] a29, b19, c07, c08, b21, d05, d06, d07 (K04).
2. **No debate; single chain or independent samples by default.** Part: G9, G4. [E] b09, b10, b11, c09, d01, d11 (K05, K22). Confirms existing G9.
3. **Check only when a verifier exists; keep a no-check arm.** Part: G1. [E] c10, c11, c12, a29 (K06).
4. **Treat reasoning text as non-authoritative; tie claims to executed output.** Part: G10, memory trace. [E] c19, d03, d04 (K14, K24). Confirms existing G10.
5. **Framing: benchmark component ablations, not the theory.** Part: none (framing). [E] a01, a15, c21, c22 (K20).

### Test first

6. **Real interpreter beats model-simulated execution at equal tokens.** Part: O tool/check step. [S] a26, a27, c01, c02, d08, d09 (K01, K28). Big effect in one paper (48.8 points); no 2025 ablation.
7. **Execute and compare on large-number or long-chain items.** Part: O tool step. [S] a26, c01, c04 (K02).
8. **External rule-based verifier loop vs model self-critique.** Part: G external critic loop. [S] a30, c12 (K11).
9. **Explicit final verification step in the loop.** Part: S verify state. [S] b14, c16, c17 (K08, K09).
10. **Re-entry cue ("Wait", role flip) before the external check.** Part: O verify. [S] d06 (K25).
11. **Scratch field on trace-execution and long arithmetic.** Part: S working notes. [S] a28, c05, c06 (K03).
12. **Probe-to-think: cheap external action vs thought.** Part: O act/probe. [S] a10, a11, d14 (K17). Human analogy only.
13. **Routing: single thread on sequential tasks; decompose only on independent subtasks.** Part: O decompose, G12. [S] b15-b18, d02, d16 (K10, K23). The 45% figure is a prior only.
14. **Sample-and-vote vs one long chain by difficulty tier.** Part: G11, G12. [S] b24, d12, d13 (K07, K27).
15. **Memory: plain long context vs notes file vs retrieval; flat vs relation-organised notes.** Part: memory. [S] c14, d10, d15 (K12, K26, K29).
16. **Stored reusable routines on repeated task families.** Part: memory. [S] c13 (K13).
17. **Log MAST-style failure modes in our runs: repetition, missed completion, missing verification.** Part: G. [S] b13, c15 (K08).

Not to use: a32 (Cognitive Workspace), priming-based offloading evidence (K16), Kosmyna as agent evidence (K15), the cockpit study as a measured effect (K19).

## 8. Concrete tests on our bench

All arms at equal total tokens (code, tool output and verifier calls counted). One fixed item set per test. Report the mean and a paired bootstrap interval, at least 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Math word problems with computation (GSM8K-like plus a large-number variant), code-trace items | (a) CoT; (b) program run by a real interpreter; (c) program written, result simulated by the model | Exact-match accuracy; tokens per item | (b) clearly above (c) and (a); (c) near (a). If (b) minus (c) is under 5 points on current models, drop the claim |
| T2 | Same, numbers scaled up | CoT vs code plus interpreter | Accuracy drop from original to scaled | CoT drop large (about 40 points in the Codex era), code drop small |
| T3 | Tasks with a checkable answer (code with tests, constraint puzzles) | (a) no review; (b) same-model self-review; (c) review plus real test output; (d) "Wait" cue only | Accuracy; calls | (c) > (a) >= (b); (d) between (a) and (c) on non-reasoning models |
| T4 | Planning (Blocks World style) | model self-critique vs rule-based verifier backprompt, equal calls | Plan validity | Verifier arm far above self-critique |
| T5 | Mixed tasks, sequential and decomposable | single chain; self-consistency N; debate N x rounds; centralised decomposition | Accuracy at fixed tokens, by task type | Single or voting best on sequential; decomposition may win only on independent subtasks |
| T6 | Same set as T5 | with and without an explicit final verification step | Accuracy; premature-stop rate | Small gain where a verifier exists; none without |
| T7 | Long-chain arithmetic and trace items | hidden reasoning vs visible scratch field | Accuracy | Scratch helps on long chains; null on real-code output |
| T8 | Items with an injected hint | check whether scratch notes mention the hint when the answer shifts | Verbalisation rate | About 25-40%; confirms G10 |
| T9 | Long-conversation recall plus selective-forgetting items | full context; notes file; retrieval; flat vs relation-organised notes | Retrieval and forgetting scored separately | Long context strong; retrieval wins exact lookup; relation notes help related recall |
| T10 | Repeated task families | with and without stored verified routines | Accuracy and tokens on later items | Gain grows with repetition; none on one-off items |
| T11 | Easy vs hard tiers | one long chain vs N short chains plus vote at fixed tokens | Accuracy by tier | Voting gains grow with difficulty; none on easy |
| T12 | Tasks where a cheap probe exists (test run, print) | think-only vs probe allowed, equal tokens | Accuracy; probes used | Probe arm wins when the probe costs less than the reasoning it replaces |

## 9. What does not transfer, and why

- **Human embodiment results.** Tetris rotation timings (100 ms vs 800-1200 ms), token-moving, necklace chains. An LLM has no motor cost or visuospatial buffer. Only the cost-asymmetry idea transfers.
- **Human memory costs of offloading** (d=2.28; 15/18 quote failures). An agent's notes do not weaken its weights. The agent's risks are different: stale or wrong notes, and context bloat.
- **Group-level collective intelligence** (Woolley c factor, transactive memory). Based on people with different knowledge and social sensitivity. Copies of one model share errors (G4), so these effects do not carry over.
- **Cockpit redundancy.** Crew members are independent; samples from one model are not. Redundancy only helps if the checks are independent (an executor, a test).
- **The theory itself.** It makes no falsifiable claim (a15), so there is nothing to confirm or refute on an agent. Use it as a design heuristic.
- **Priming-based offloading evidence** (Google Stroop). Did not replicate.
- **Debate-style "social" scaffolds.** Human group deliberation can pool distinct knowledge; same-model agents cannot.
- **Reflexion and Voyager gains.** They depend on an environment that returns a signal (tests, game state). They do not show that self-talk helps.
- **Old-model numbers.** Self-correction and debate figures from GPT-3.5 and GPT-4 may not hold for reasoning models.

## 10. Open questions

1. Real vs simulated execution at equal tokens on 2025-2026 models and non-math tasks.
2. Does a cheap second sample or program check restore self-correction gains on current reasoning models?
3. Break-even among self-consistency, debate and a long chain per task type (Tran and Kiela partly close it; the per-task table is missing).
4. Is Kim's 45% threshold stable outside the six benchmarks?
5. Which memory design helps long tasks on an independent benchmark (second half of MemoryAgentBench not read)?
6. Original human numbers: Zhang and Norman 1994 not opened; Vallee-Tourangeau digits not re-verified; Chuderski 2021 not opened; no independent replication of interactivity found.
7. Which MAST failure modes (termination, verification) does a fixed non-LLM harness cure, and by how much?
8. Does any paper test DC or extended-mind predictions (coupling, offloading threshold) directly on LLM agents? Search was rate-limited; the absence is weakly supported.
9. Is there an offloading threshold for agents: when should a step go to code instead of staying in thought?
10. Do notes organised by relation help an agent as they help humans (d15)?
11. Camerer figures (b05) were from memory; Woolley, Riedl and Ren and Argote were not opened.

## 11. Sources

[V] = opened and read this session; [M] = snippet or memory only.

- [V] Hollan, Hutchins, Kirsh 2000. https://hci.ucsd.edu/hollan/Pubs/tochi-revised.pdf ; mirror https://perso.lisn.upsaclay.fr/mbl/Stanford/CS477/papers/DistributedCognition-TOCHI.pdf
- [V] Hutchins 1995, How a cockpit remembers its speeds. https://pages.ucsd.edu/~ehutchins/documents/CockpitSpeeds.pdf
- [V] Kirsh and Maglio 1994. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf ; http://csjarchive.cogsci.rpi.edu/1994v18/i04/p0513p0549/MAIN.PDF
- [V] Clark and Chalmers 1998. http://consc.net/papers/extended.html
- [V] Hutchins 2013, cultural ecosystem. https://pages.ucsd.edu/~ehutchins/documents/publishedCulturalEcosystemHumanCog.pdf
- [V] Hutchins 2012, collective intelligence. https://pages.ucsd.edu/~ehutchins/documents/collective-intelligence.pdf
- [V] Hutchins 2010, cognitive ecology. https://pages.ucsd.edu/~ehutchins/documents/CognitiveEcology.pdf
- [V] Hutchins 2009, expectation and surprise. https://pages.ucsd.edu/~ehutchins/documents/Hutchins-AutomationSurprise.pdf
- [V] Wikipedia, Distributed cognition (tertiary). https://en.wikipedia.org/wiki/Distributed_cognition
- [M] Zhang and Norman 1994. https://doi.org/10.1207/s15516709cog1801_3
- [V, digits not re-confirmed] Vallee-Tourangeau, Sirota, Vallee-Tourangeau 2016. https://doi.org/10.1186/s41235-016-0027-2
- [V] Henok et al. 2020. https://doi.org/10.1007/s00426-018-0992-9
- [M] Chuderski et al. 2021. doi 10.1111/bjop.12442
- [V abstract, figures from memory] Camerer et al. 2018. https://www.nature.com/articles/s41562-018-0399-z
- [V] Hesselmann and Gollo 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/
- [V] Magen and Tomer-Offen 2025. https://doi.org/10.1186/s41235-025-00647-0
- [V] Kosmyna et al. 2025. https://arxiv.org/abs/2506.08872
- [V] Clark 2025. https://www.nature.com/articles/s41467-025-59906-9
- [M] Woolley et al. 2010. https://doi.org/10.1126/science.1193147
- [M] Riedl et al. 2021. https://doi.org/10.1073/pnas.2005737118
- [M] Ren and Argote 2011. https://doi.org/10.5465/19416520.2011.590300
- [V] Gao et al. 2022, PAL. https://arxiv.org/abs/2211.10435
- [V] Nye et al. 2021, scratchpads. https://arxiv.org/abs/2112.00114
- [V] Huang et al. 2024, self-correction. https://arxiv.org/abs/2310.01798
- [V abstract] Kamoi et al. 2024. https://arxiv.org/abs/2406.01297
- [V abstract] Kumar et al. 2024, SCoRe. https://arxiv.org/abs/2409.12917
- [V] Tsui 2025, Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Kambhampati et al. 2024, LLM-Modulo. https://arxiv.org/abs/2402.01817
- [V] Du et al. 2023, debate. https://arxiv.org/abs/2305.14325
- [V] Smit et al. 2024. https://arxiv.org/abs/2311.17371
- [V abstract] Wang et al. 2024. https://arxiv.org/abs/2402.18272
- [V] Li et al. 2024, More agents. https://arxiv.org/abs/2402.05120
- [V] Cemri et al. 2025, MAST. https://arxiv.org/abs/2503.13657
- [V] Kim et al. 2025/2026, scaling agent systems. https://arxiv.org/abs/2512.08296
- [V] Tran and Kiela 2026. https://arxiv.org/abs/2604.02460
- [V] Riedl 2026, emergent coordination. https://arxiv.org/abs/2510.05174
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291
- [V] Packer et al. 2023, MemGPT. https://arxiv.org/abs/2310.08560
- [V] Hong et al. 2023, MetaGPT. https://arxiv.org/abs/2308.00352
- [V] Turpin et al. 2023. https://arxiv.org/abs/2305.04388
- [V] Chen et al. 2025. https://arxiv.org/abs/2505.05410
- [V abstract] Korbak et al. 2025. https://arxiv.org/abs/2507.11473
- [V] Sumers et al. 2023, CoALA. https://arxiv.org/abs/2309.02427
- [V] Li et al. 2025, ToRL. https://arxiv.org/abs/2503.23383
- [V] Li et al. 2023, Chain of Code. https://arxiv.org/abs/2312.04474
- [V] Hu et al. 2025, MemoryAgentBench. https://arxiv.org/abs/2507.05257
- [V abstract] Snell et al. 2024. https://arxiv.org/abs/2408.03314
- [V abstract] arXiv 2506.04210 (parallel vs extended thinking; authors not confirmed). https://arxiv.org/abs/2506.04210
- [V, weak] Cognitive Workspace, arXiv 2508.13171. https://arxiv.org/abs/2508.13171

Links to parallel subfields (not covered here): Joint cognitive systems; Chain-of-thought prompting; Learned refinement and self-verification; Tool manufacture and use; Consensus and premature agreement; Confidence and metacognition. Earlier F02 folders: 03_cognitive_offloading, 05_cognitive_artefacts_and_cockpit_studies, 06_external_representations, 07_epistemic_actions.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F02.01-K22** (number corrected). All accuracy figures match Table 1 of Tran and Kiela, but the paper covers three model families (Qwen3, DeepSeek-R1-Distill-Llama, Gemini 2.5; four models since Flash and Pro are both Gemini), not four families. Corrected claim: At matched thinking tokens a single agent is the best default on multi-hop QA across three model families (four models: Qwen3-30B, R1-Distill-Llama-70B, Gemini-2.5-Flash and Pro): mean accuracy at 1000 tokens single 0.418 vs debate 0.388, roles 0.381, sequential 0.379, subtask-parallel 0.369, ensemble 0.333; multi-agent leads only at 100 tokens or under heavy context corruption.
