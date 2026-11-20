# LLM help in hardware debugging: deep document

*Subfield E08.09. Key work: Hu and Ash 2026 (arXiv 2608.02955). Evidence ids (a01-a26, b01-b25, c01-c27, d01-d17) are lines in evidence_a-d.jsonl in this folder. Claim ids (E08.09-K01 to K28) are in claims.jsonl. Corrections from critique.md are applied: where a number was corrected, the corrected number is used here.*

*Honest summary up front. The field is very young. Almost all of it is 2025-2026 preprints. The key paper is a qualitative study of 17 self-selected chat logs. No study measures whether LLM help changes real hardware repair success or time against a control group. The strong numbers come from HDL/RTL code benchmarks, which are software-like. The "overconfidence" finding for physical circuits rests on a few logged cases. No replication of Hu and Ash exists (d16, d17).*

## 1. What it is

The subfield asks: when a person debugs a physical circuit or board and talks to a chatbot, what happens? Does the model help find the fault? Does it sound sure when it is wrong? Does the person act on it?

It has four strands.

1. **Human-chatbot hardware debugging (the key strand).** Hu and Ash 2026 (a01-a05) let undergraduates use public chatbots in a 30-minute hands-on exam on buggy analog circuits and read the chat logs they chose to share. Ash and Hu 2026 (a06, a07, b01-b03, c01-c03) is a work-in-progress case study of one fourth-year student using GPT-4o on three debugging chats.
2. **Agent benchmarks for hardware bug repair.** HWE-Bench (a13, a14, b07, b08, c04, c05, c22, c23) for repository-level RTL repair; ChipBench, CVDP, VeriPilot, AutoVeriFix+ and others for Verilog debugging (a15, b09-b11, d14, d15); EmbedBench for embedded code plus circuit (a16); EDA Bench for PCB building (c14, c26).
3. **Perception of circuits by multimodal models.** AMSbench, OmniSch, ElectroVizQA, UniPCB (a23-a25, c16, d06, d07). This is where the "image claim" failure in Hu and Ash gets its mechanism.
4. **Confidence, calibration and reliance.** LLM calibration (a17, a18, b14, b16, b17, d08, d09) and how humans use LLM answers and confidence (a19, a20, b15, b19, b20, b21, b22). This is where G10 ("reasoning text is not evidence", plus the 4b rule against using verbal confidence to stop) gets its support.

Why it matters for our agent. Our agent is one model inside a scaffold. Two things from this subfield bear on it directly. First, a model states physical facts it cannot know, with high confidence, from a photo. The schema should force a check before such a claim is used. Second, hardware debugging is a loop of hypothesis, test, report, revise, where a human or a tool is the sensor. That loop is S3-S5 in our schema. The subfield tells us where that loop breaks for LLMs: wrong hypothesis order, symptom-fix instead of root-cause fix, multi-turn drift, and under-use of external verifier output.

Scope notes. Other E08 subfields (cognitive models of troubleshooting, model-based diagnosis, industrial fault detection, efficient diagnosis algorithms) are covered elsewhere. This document only touches them where an LLM study uses them (d10, d12, c17).

## 2. History and theories in depth

### 2.1 Human debugging theory that the key papers build on

- **Katz and Anderson 1987** (a08, [M], via Hu and Ash only). Four steps: understand the system, test it, locate the error, repair. Bug-location strategies: discrepancy detection, topographic search, split-half, exhaustive, trial and error. Ash and Hu map LLM help onto these four steps (b03, c02).
- **Schaafstal, Schraagen and van Berlo 2000** (a21, [M], via Hu and Ash). Troubleshooting as four sub-tasks: problem description, generate causes, test, evaluate. Novices lose track of where they are in the search as the problem space grows. This is a working-memory overflow account.
- **Jonassen and Hung 2006** (a10, [M], via Hu and Ash). A learning architecture: multi-layer system model, a simulator to test hypotheses, a case library. Experts try experience-based diagnosis first.
- **Alaboudi and LaToza 2020** (a09, [M], via Hu and Ash). Programmers write down few hypotheses. When handed a set of candidate hypotheses, their success rate and efficiency rose significantly. No effect size was read by us.
- **Trade claim.** "Over 40% of electronics engineers' time is spent troubleshooting" (b03, c21). It comes from an industry web article, not a study. Do not cite as evidence.

The key idea that Ash and Hu take from this: humans, expert or novice, generate few hypotheses. So the LLM's main value should be to generate many root-cause hypotheses and draft test plans, while the human runs the tests (a07, c02). This is a proposal, not a tested result.

### 2.2 LLM debugging in software, as the baseline

- **ChatDBG** (a12, Levin et al.): a debugger-integrated agent that can call debugger commands. On Python programs a bare "why?" succeeded 57%, a targeted query 67%, and one added follow-up step 85%. For C/C++ crashes 36% of fixes addressed the root cause and 55% only the proximate cause. Tool access and one follow-up matter a lot. The proximate-vs-root split is the same failure as HWE-Bench's symptom-fix problem.
- **Santos and Becker 2024** (d03): N=106 students, six buggy C programs, GPT-4 explanations of compiler errors faster than stock messages in only 1 of 6 tasks. Expert handwritten messages did better. So even in software, LLM explanation does not reliably speed repair.
- **Bo et al. 2025** (a11, a22): n=8 novices, a buggy ML script. Led-by-the-LLM workflows go with over-reliance. F1 tracked a knowledge quiz (r=.93, p<.001), not self-reported experience. Sycophancy named as a reason ChatGPT guides novices poorly.
- **METR 2025** (b21): RCT, 16 experienced developers, 246 real tasks. AI allowed: measured +19% time. Developers forecast 24% faster and afterwards believed 20% faster. Experts predicted 39% (economics) and 38% (ML) shorter. Belief and measurement diverged.
- **Perry et al. 2023** (b22): 47 participants, five security tasks. Assistant users were less correct (67% vs 79%) and less secure (36% vs 50% in one task) while rating their code more secure. Many accepted the AI solution without extra checks.

### 2.3 Calibration and reliance background

- **Kadavath et al. 2022** (a17): large models (up to 52B) are well calibrated on multiple choice and true/false with the right format; P(True) improves with size and with seeing several own samples.
- **Xiong et al. 2024** (a18, b17): verbalised confidence from GPT-3, GPT-3.5, GPT-4, Vicuna, LLaMA 2 is overconfident, clustering at 80-100% in multiples of 5. GPT-4 AUROC for right vs wrong only 62.7%. Sampling consistency beat asking for a number. ECE above 0.377 on average for GPT-3, GPT-3.5, Vicuna; GPT-4 near-optimal ECE 0.064 on GSM8K (93.6% accuracy).
- **Huang et al. 2024** (b18): no external feedback, no gain from self-correction. GPT-3.5 on GSM8K kept its answer 74.7% of the time; among changes, more right answers became wrong than the reverse.
- **Steyvers et al. 2025** (b19): people overestimate LLM accuracy with default explanations. Longer explanations raise confidence without raising accuracy. Matching explanation wording to model confidence narrows the gap. N=301 (284 retained). Model confidence AUC 0.751 / 0.746 / 0.781; human AUC with default explanations 0.589 / 0.602 / 0.592.

### 2.4 The new 2025-2026 wave

All preprints, none replicated. What each added:
- 2023-2025: HDL fault fixing with LLMs (c24), VeriDebug, MEIC (c11, c12, snippets only), AMSbench (a23), EmbedBench (a16), CVDP (b09), Lost in Conversation (d01).
- 2026: ChipBench, HWE-Bench, VeriPilot, VeriBugBench, OmniSch, EDA Bench, the consumer repair benchmark, When LLMs Over-Answer, CoffeeBench, the two Chat-Debugging papers.

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources agree), **S** single source, **C** contested or internally inconsistent. Opened or snippet marks are in section 11.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Hu and Ash: chatbots give sensible hardware knowledge, but nearly all factual errors followed image input | 17 self-selected logs (5 Spring, 12 Fall 2025), 6 buggy circuits, 30-min exam, ECEN 3314 Oklahoma State. Images in 2/5 Spring and 5/12 Fall logs = 7/17 (41%, an upper bound for circuit photos; some images show only the assignment) | a01, a05 | S |
| False pin claim stated at "99% confident" | ChatGPT said op-amp wired to pins 5,6,7; board used 1,2,3. After a second photo it was more convinced and made 3 more false statements (pins 4 and 11 "unconnected") | a04 | S (one case) |
| False wiring claims after 4m 33s of thinking | ChatGPT 5.1: ground clip "on + rail", resistor "not tied to drain". Both wrong. At least 2 false claims in one answer | a03 | S (one case) |
| True cause listed last of four | P3 CE amplifier: cause "no DC biasing" was hypothesis 4 of 4. Student dwelt on the wrong lead and failed in 30 min | a02 | S (one case) |
| Software bugs fixed in about 1 prompt; hardware needs test-and-report loops | Case study N=1: software 11 prompts/30 min; Pi Pico+mux 10 prompts/1 h unresolved; LED+buck 7 prompts/30 min | a06, a07, b02, c01 | S |
| Multi-turn loss for LLMs in general | 15 LLMs; average drop 39% (6 generation tasks); aptitude -15%, unreliability +112%; over 200,000 conversations; reasoning models degrade the same | d01 | S (one lab) |
| Recap helps only partly; temperature does not fix | RECAP and SNOWBALL beat sharded input, still lag full-input; unreliability stays high at temperature 0 | d02 | S |
| Best agent on real hardware bug repair | HWE-Bench 417 tasks, 6 repos, 7 LLMs: GPT-5.4 xhigh 295/417 = 70.7%; Opus 4.6 68.1%; Sonnet 4.6 66.7%; GLM 5.1 63.1%; Qwen3.6 Plus 52.5%; DeepSeek V3.2 52.0%; Kimi K2.5 47.7%. 45/417 (10.8%) unsolved by all | a13, b07, c04 | S |
| Repo difficulty tiers | GPT-5.4: CVA6 34/35 (97.1%), Ibex 32/35 (91.4%), Caliptra 15/16 (93.8%), OpenTitan 157/245 (64.1%), XiangShan 37/54 (68.5%), Rocket Chip 20/32 (62.5%). The "above 90%" holds for the best model only; the text says "over 80%" for proprietary models in general | c22, a13 | S |
| Main failure: fix the symptom file, not the owner | Ibex illegal-instruction bug fixed in controller not fetch stage; XiangShan TLB width bug rewritten in the TLB module, true fix in a package definition | a14, b08, c05 | S (ChatDBG C/C++ 55% proximate vs 36% root is a different-task echo) |
| Cost and style differ at similar accuracy | Sonnet 18.6 tool calls, 714K input tokens, 66.7%; Opus 20.0 calls, 68.1%, $0.51; GPT-5.4 77.7 calls, 4.2M tokens, 70.7%, $1.81. File-level precision GPT-5.4 0.619 vs Opus 0.928 | a14, c05, c23 | S |
| Hardware separates models that software hides | SWE-bench Verified 73-81% cluster; HWE-Bench best 70.7% with wider spread | b25 | S |
| Verilog debugging easier than generation | ChipBench, 89 debug cases: Claude 4.5 Opus 47.45% debugging vs 30.74% generation pass@1 | a15, b10 | S |
| Waveform context inconsistent | One-shot with .vcd beat zero-shot on 8 models, worse on 13 | a15, b10 | S |
| Debug category in CVDP | Claude 3.7 Sonnet 53.0% / 51.0% (two prompt variants), thinking mode 31% / 45%, GPT-4.1 32% / 26%; aggregate non-agentic best 33.56% | b09 | S |
| Reference-model scaffold | VeriPilot GPT-4o 54.3% to 77.1% in body; abstract says 85.71%. Unresolved, cite neither as final | b11 | C |
| Verifier gains stack, but which is largest depends on benchmark | AutoVeriFix+ GPT-4, RTLLM v2.0 pass@1: 51.6 base, +0.8 syntax, +22.2 testbench I/O, +4.4 trace = 79.0. VerilogEval-Human: 43.5, +24.6 syntax, +9.1, +0.9 = 78.1. False positives 28.4% to 2.0% on RTLLM v2.0 | d15 | S |
| Small-model refine loop gives small gain | 50 tasks, up to 5 iterations: syntax 63.3 to 67.8, sim pass 46.1 to 48.9. Internal number conflict (46% vs table) | d14 | C |
| Retrieval plus compiler feedback on embedded code | EmbedBench 126 cases: DeepSeek-R1 55.6% pass@1 with schematic, 50.0% own; 65.1% after RAG plus compiler feedback; reasoning models overthought and ignored knowledge | a16 | S |
| Root-cause analysis of EDA failures | 34 errors, 170 responses: runtime pass@5 GPT-4o 93.3, o3-mini 100, DeepSeek R1 93.3; gpt-3.5 46.7. RAG hurt gpt-3.5 (runtime 33.3 vs 46.7) | c13 | S |
| Verilog security-bug repair (2023) | code-davinci-002 47.4% correct repairs of 10 bugs; detailed pseudo-code fix instruction best | c24 | S |
| LLM perception of schematics is weak | OmniSch 1,854 schematics: symbol F1 Gemini 2.5 Flash 0.66, Gemini 3.1 Pro 0.59, Claude Sonnet 4.6 0.59, GPT-5.2 0.53, human 0.97; best net F1 27.44%, net-name accuracy 25.07% | a24, d06 | E (with AMSbench, ElectroVizQA, UniPCB) |
| Perception degrades with circuit size | AMSbench count accuracy easy to hard: Gemini 0.88 to 0.45; GPT-4o 0.75 to 0.26; Claude 3.7 0.72 to 0.01. Testbench Syntax@5 zero for all but GPT-4o (0.084) | a23, d07 | E |
| Locate-then-verify aid helps perception | OmniSch with ground-truth box: GPT-5.2 symbol F1 0.69 to 0.86; Claude 0.51 to 0.80. Removing text raised Claude 0.62 to 0.72 | d06 | S |
| Image vs text input | ElectroVizQA: GPT-4o 60.39% with image, 72.36% text-only; Claude 3.5 Sonnet 62.27% image, 45.21% text-only. AMSbench function ID Grok-3 0.22 image vs 0.77 text; Gemini 0.94 vs 0.95. Mixed | a25, d07 | C |
| Board design from datasheets is rarely fully right | 300 tasks: fully correct designs Claude Sonnet 4.5 8.15%, GPT-5.2 6.58%, others 4.4-5.16%; static checks mean 71.84% | c15 | S |
| Strict end-to-end PCB task near zero | EDA Bench 35 tasks: 1.48% (archived), 2.18% (fresh). In 99 saved projects wrong pin mapping 76, split nets 73, shorts 70, unpowered parts 18. Agents stopped without running the checks | c14, c26 | S |
| PCB defect inspection by general MLLMs | UniPCB: PCB-GPT (7B tuned) localisation F1 51.1 vs Gemini 2.5 Pro 23.6, GPT-5 20.2; general models over-predict defects | c16 | S |
| Text hardware diagnosis from user reports | FACTO 853 reports, 27 open models plus GPT-4o: best F1 0.767 (gpt-4o CoT); gemma-2-2b 0.727; gains level off near 30B; qwen2.5-1.5b 0.000 zero-shot vs 0.673 few-shot (format failure) | c19, c25, d13 | S |
| Consumer repair advice | 991 Reddit questions, six LLMs: GPT-5.4 best, 0.84 English data recovery; phone repair worst; Claude 4.6, Gemini 3.1, Qwen 3.6 below 0.25 safety on phone repair; completeness did not mean safety; errors include skipped continuity tests | b13, d05 | S |
| LLM answers to HDL questions bury the core | 363 stratified questions, 19 engineers: redundant core 65.7% LLM vs 4.4% human; verbose 69.1% vs 5.8%; full coverage 50.7%; readability preferred LLM 58.3% vs human 35.1%. Debate plus compression: core quality 3.71 to 4.67 (+0.96); core answers 37% shorter | b04, b05, b06 | S |
| Industrial time series | HVAC simulator: LLM F1 0.79-0.85 vs rule baseline 0.85; normal-reference data no consistent effect; summary stats beat raw series | c17, c18 | S |
| LLM plus specialist tool | Tennessee Eastman, 150 runs, 7 LLMs, 1,050 rows: unaided 64.67%, with advice 77.43%, tool alone 83.33%, oracle selector 92.76%. Of 99 LLM-right/tool-wrong rows, 15 (15.2%) flipped to wrong; of 295 tool-only-correct rows 47.5% (140) missed | d12 | S |
| Information-gain question order | UoT on FloDial troubleshooting (894 dialogues, 153 faults, 20 turns), GPT-4: direct 43.7%, UoT 67.3%, ToT 60.3%, CoT 32.8%; mean length in successes 7.8 vs 13.4 turns | d10 | S (simulated, closed fault set) |
| LLMs overconfident | Sun et al.: five LLMs overestimate correctness by 20-60%; 10% lower LLM confidence goes with ~25% lower accuracy (GPT-4o, o1), ~13% Llama 3.1. Ghosh and Panday 24,000 trials: Kimi K2 23.3% accuracy, 95.7% confidence, ECE 0.726; Claude Haiku 4.5 75.4%, 86.0%, 0.122; Gemini 2.5 Pro 80.9%, 99.5%, 0.185 | b14, b16, a18, b17 | E |
| Reasoning models better calibrated on QA | Better on all metrics in 33 of 36 settings; gain from slow-thinking behaviours | d08 | S (QA only) |
| RLVR may bring overconfidence back | Snippet only, no numbers | d09 | S (snippet) |
| LLM advice raises accuracy and overconfidence | Accuracy +5.6 (answer) and +7.1 (answer plus confidence) in the SI regression (not 7.0); bias +4.2 and +7.6 points; accuracy gap between arms p=.213, bias gap p=.011. Low-confidence users: accuracy +8.6/+11.9, bias +7.0/+14.1. Humans 100% sure were 81% right | b14, b15 | S for this lab; direction E with a20, b19, b22 |
| First-person hedge lowers agreement and raises accuracy | N=404 (252 of 656 excluded, 38.4%): agreement 80.9% control, 74.8% first-person, 58.4% no-AI; correct 72.8% first-person vs 63.9% control; general hedge 67.9% not significant. AI right: 88.5% vs 77.9% no-AI; AI wrong: 33.0% vs 64.7% no-AI | a19, b20 | S |
| Reliance interventions cut reliance but not appropriateness | N=400. LSAT: alone right 36.0%; advice right 50%; best team 62.1%. Disclaimer, highlighting, implicit answer reduced reliance overall | a20 | S |
| Self-correction fails without feedback | GPT-3.5 GSM8K 74.7% kept answer; more right-to-wrong | b18 | S here; E in schema |
| Expert slow-down with belief of speed-up | +19% measured, -20% believed, -24% forecast | b21 | S |
| Replication of Hu and Ash | Semantic Scholar citations empty for both papers; none found | d16, d17 | none |

## 4. Mechanisms and models

Each mechanism is written so an engineer could build it. Evidence status is in section 7.

### 4.1 Image-claim hallucination (why Hu and Ash saw it)

**What happens.** A multimodal model gets one photo of a breadboard or PCB. It writes a netlist-like description from pixels. The description is wrong at pin level because of camera angle, bent wires, occlusion and tiny pin numbers. It then reasons on top of the wrong description and states it with high confidence. A second photo can increase confidence in the wrong reading (a04).

**Supporting mechanism evidence.** Perception errors are large and size-dependent (d06, d07): net F1 27.44% at best, count accuracy collapsing for large circuits. Text-only input is sometimes better than image input (a25 for GPT-4o; mixed for others). A locate-then-verify aid lifts symbol F1 (d06).

**Implementation as a pipeline.**
1. Tag every statement the model makes with its source: `image`, `user_text`, `measurement`, `datasheet`, `own_inference`.
2. Code lists all `image`-sourced claims about physical state (connectivity, pin used, polarity, orientation, presence of a part).
3. For each such claim the current hypothesis depends on, the program makes the model emit one cheapest check that would confirm or refute it (continuity, voltage at a named pin).
4. The claim stays "unverified" in a state register until a measurement result is entered. Hypotheses that depend on unverified claims are ranked below ones that do not.
5. Keep the step only if it cuts wrong actions at equal tokens (test T1, section 8).

**Limit.** Hu and Ash give no false-claim rate per image and no control (critique gap 2). The mechanism is plausible and supported by perception benchmarks, but the effect of the fix is untested.

### 4.2 The human-as-sensor loop

Hardware has no compiler. Each hypothesis needs a physical test the person runs and reports. Software chat bugs are usually fixed in about one prompt because the error message is the sensor (a07, b02). In hardware, the model has to plan tests, read terse reports, and keep state across turns.

Failure modes seen:
- Misreading a short question without context (GP15 read as a power input; c03).
- Drifting from the real circuit over a long chat (b02).
- Putting several parts on one rail when handed a whole multi-board setup at once (c03).
- Ordering root causes by its own guess of test difficulty, leading to complex fixes and an unresolved session (c03).

General evidence says multi-turn loss is mostly unreliability, and early wrong assumptions persist (d01). Restating everything helps only part of the gap (d02).

**Implementation: a running state register.** After every turn, the model writes and code stores three lists: `measured` (value, where, how), `ruled_out` (hypothesis, test that killed it), `open` (hypothesis, cheapest discriminating test, cost). The register, not the raw history, is the main context on the next turn. Untested for hardware (critique gap 8; claim K23). CoffeeBench authors suggest explicit episode-state tracking to cut timeouts (d11, abstract only).

### 4.3 Hypothesis ordering and test choice

Alaboudi and LaToza (a09) say giving a set of hypotheses raises debug success. Hu and Ash's case a02 shows a set is not enough: the true cause was 4th of 4 and the student chased a wrong lead.

UoT (d10) gives a way to order: choose the next question or test by simulated expected information gain. On a closed fault set (FloDial, 153 faults) it raised GPT-4 success from 43.7% to 67.3% and shortened successful dialogues from 13.4 to 7.8 turns.

**Implementation.** For the open hypotheses, the model gives a rough prior (low/med/high mapped to numbers in code) and, for each candidate test, which hypotheses it would split and a cost class. Code scores each test by `expected_split / cost` and picks the top. This is classic cost-weighted half-split. The model fills the slots; code ranks. It matches G5 (code selects) and S7 (discriminating test). Not tested on bench hardware.

### 4.4 Root cause vs symptom

HWE-Bench's main failure is localisation: the agent patches where the failure shows (a14, b08). Second failure: patches that compile but break a protocol (state transitions, valid-ready handshakes). Agents leaning on keyword match are most prone.

**Implementation: forced trace-back.** Before any fix, the program requires a short chain: `symptom -> signal that carries it -> driver of that signal -> upstream owner of the behaviour`, each link tied to a file/line or a measurement. The fix must target the last link. Optional check: does the symptom still appear if the owner is patched and the symptom module is not touched? Untested (claim K05).

### 4.5 Verifier use

Two sets of numbers point the same way.
- Feedback stacks in RTL work (d15): testbench I/O feedback +22.2 on RTLLM, syntax feedback +24.6 on VerilogEval-Human. The largest verifier depends on the benchmark. Trace-aware debug added only +0.9 to +4.4.
- Models under-use verifier output (d12): wrong tool labels flipped 15.2% of correct answers, but 47.5% of tool-only-correct cases were missed.

So: cheap verifiers first (compile, then I/O, then trace), and force the agent to act on the result. An agent that requests a measurement but explains it away gains nothing.

EDA Bench (c14, c26) adds the negative case: agents stopped without running connectivity and design-rule checks. Authors propose a typed connector-to-net plan, a required-block checklist, and a repair loop where exact check failures are fed back before stopping. These are proposals, not tested ablations.

### 4.6 Confidence and reliance

Two separate problems.

1. *The model's confidence is a poor guide.* Verbalised confidence is overconfident and weakly correlated with correctness (a18, b16: best r=0.175, not significant for Gemini 2.5 Pro). Sampling consistency does better than asking for a number (a18). Reasoning models do better on QA (d08) but the spread across models is wide (ECE 0.122 to 0.726).
2. *The human's reliance on the model is badly tuned.* LLM advice raises accuracy a few points and raises overconfidence more (b15). Showing numeric LLM confidence raised bias more than showing the answer only. First-person verbal hedges lowered agreement, mostly on wrong answers (a19). General reliance disclaimers cut reliance across the board without improving appropriateness (a20).

Implication. Stated confidence is never used as a gate (G10, 4b). If the agent speaks to a person, how it expresses uncertainty is an output-style choice with a single-source human-study basis (Kim et al.), tested on medical QA, not diagnosis.

## 5. What holds up

### 5.1 Established (two or more independent sources)

- **LLMs read circuit images badly, and worse as circuits grow.** AMSbench, OmniSch, ElectroVizQA, UniPCB, board-level design (a23, a24, a25, c16, c15, d06, d07). Different groups, different tasks, same direction. Established for drawn schematics and PCB schematics; not measured for bench photos (critique gap 2).
- **LLMs are overconfident in stated confidence, worse for weaker models.** Xiong, Kadavath (well calibrated only in special formats), Sun, Ghosh and Panday, Steyvers (a17, a18, b14, b16, b17, b19). QA and reasoning tasks, not diagnosis.
- **Self-correction without external feedback is unreliable.** Huang et al. plus the schema 4b sources (b18). Within this subfield one source; across the schema, established.
- **External feedback helps RTL work.** Several benchmark sources show scaffolds with reference models, testbench feedback or partitioning help by large margins (b09, b10, b11, d15, claims K08). Magnitudes differ by benchmark; all are single-model runs.
- **People over-rely on AI answers and become more confident.** Sun et al., Bo et al. (reliance), Perry et al., METR (b15, a20, b22, b21). Different populations, same direction.

### 5.2 Single-source or contested

- **Hu and Ash's image-claim finding.** n=17, self-selected, qualitative, no accuracy rate, no control. Models differ across logs (ChatGPT-4o, ChatGPT 5.1, Gemini, unknown). "Almost all factual errors came after LLMs analyzed image inputs" is the authors' coding judgment. The 7/17 image rate is a sum over two semesters and includes images that show only the assignment.
- **The WIP companion** has N=1.
- **HWE-Bench numbers.** One benchmark, one group. The top number depends on harness and budget (6 h, 500 iterations). Different agent frameworks were used per model (Codex CLI for GPT-5.4, Claude Code for Claude), so model and framework are confounded.
- **Waveform context.** 8 models helped, 13 hurt (b10). No clear rule. May reflect long raw dumps in context.
- **First-person hedging.** One pre-registered study, N=404 after a 38.4% exclusion rate, medical QA with a fictional tool. Not tested for diagnostic advice.
- **VeriPilot.** 77.1% (body) vs 85.71% (abstract). Unresolved.

### 5.3 Failed or null results

- AI explanations of compiler errors beat stock messages in 1 of 6 tasks (d03).
- METR: experts slower with AI, +19% (b21).
- Vocational electronics quasi-experiment: no clear drop in assembly errors (d04, page not opened; no numbers cited).
- Reliance disclaimers, uncertainty highlighting, implicit answer: lowered reliance, did not improve appropriate reliance (a20).
- Normal-operation reference data: no consistent effect on fault diagnosis F1 (c18).
- RAG hurt weak models and made models ignore a no-code instruction (c13); reasoning models ignored retrieved knowledge (a16).
- Chain-of-thought: small or negative for small models; helps big models in FACTO (d13); did not help consistently in ElectroVizQA (a25).
- Lowering temperature did not fix multi-turn unreliability (d02).
- Small-model refine loops: +2.8 sim-pass points (d14).

### 5.4 Moderators

- **Task type.** HWE-Bench 70.7% vs EDA Bench ~2% vs board design ~8% fully correct. Different tasks and graders. No cross-benchmark comparison is valid.
- **Project scale.** HWE-Bench: above 90% on small cores for the best model, 62-69% on large SoC projects. Rocket Chip has over 40% configuration/integration bugs versus 20-25% elsewhere (c22).
- **Input modality.** Image vs text: mixed across models (a25, d07).
- **Circuit size.** Counting collapses beyond 16 components for some models (d07).
- **Model strength.** Weaker models more overconfident (b16).
- **User knowledge.** Quiz score predicts bug-identification F1 (r=.93, n=8; a11). Students lacked fundamentals and offloaded thinking (a05).
- **Prior confidence.** Low-confidence users gained most accuracy and most bias from LLM advice; high-confidence users did not move (b15).

### 5.5 Interventions that worked (with limits)

- Debugger tools and one follow-up step: ChatDBG 57% to 85% on Python (a12).
- Execution feedback: AutoVeriFix+ +22.2 and +24.6 points on GPT-4 (d15); EmbedBench 50.0% to 65.1% (a16).
- Reference model with signal alignment (b11).
- Information-gain question order (d10).
- First-person hedge in a fictional tool (a19).
- Concise-answer compression (+0.96 core quality on a 5-point judge scale; b06).
- Locate-then-verify aid for schematic reading (d06).

### 5.6 Interventions that did not work

See 5.3. Also general self-reflection (b18) and numeric confidence display (b15).

## 6. Language models

This whole subfield is about language models, so this section collects model-level behaviour on these tasks and what moved it.

**Models seen in the key studies.** Hu and Ash: ChatGPT-4o, ChatGPT 5.1, Gemini, one unknown (a01). Ash and Hu: GPT-4o (a06). HWE-Bench: GPT-5.4 xhigh, Claude Opus 4.6, Sonnet 4.6, GLM 5.1, Qwen3.6 Plus, DeepSeek V3.2, Kimi K2.5 (c04). Several versions cannot be reproduced by us.

**Physical-state claims from images.** Confident, specific, wrong (a03, a04). Thinking time did not prevent it: ChatGPT 5.1 thought 4m 33s and still made at least 2 false claims. A second photo made it more convinced (a04). It also offered to "mark exactly where each connection should go", an offer it cannot back.

**Hypothesis lists.** Lists several candidates in one reply with no sign of which is right (a02). Orders root causes by its own sense of test difficulty (c03).

**Long chats.** Drifts from the real circuit and misreads short questions (b02, c03). General multi-turn data: -39% average, unreliability +112% (d01). Reasoning models no better, replies 33% longer with more assumptions.

**Agents on repair.** Edit the symptom location (a14). Patches that compile but violate the hardware contract (b08). Claude runs mostly read code and rarely built or simulated, yet scored within 3 points of the most exploratory agent (c23). Cost per task: $0.26 (Sonnet), $0.51 (Opus), $1.81 (GPT-5.4). Cost differs by 5x or more at similar accuracy. This supports G12.

**What changed performance, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Debug vs generate (same module) | +16.7 points pass@1 (47.45 vs 30.74) | b10 |
| Testbench I/O feedback | +22.2 (RTLLM v2.0) | d15 |
| Syntax feedback | +24.6 (VerilogEval-Human) | d15 |
| Trace-aware debug | +0.9 to +4.4 | d15 |
| Golden reference model | 54.3 to 77.1 (or 85.71) | b11 |
| RAG plus compiler feedback (embedded) | 50.0 to 65.1 | a16 |
| RAG for weak model | worse: gpt-3.5 runtime 33.3 pass@5 vs 46.7 baseline | c13 |
| Few-shot for 1.5B model | 0.000 to 0.673 F1 (format only) | c25 |
| Information-gain next question | 43.7 to 67.3 | d10 |
| Giving the specialist tool's label | 64.67 to 77.43, still below tool alone 83.33 | d12 |
| Waveform in context | better for 8 models, worse for 13 | b10 |
| Locate-then-verify box in schematic task | symbol F1 +0.17 (GPT-5.2), +0.29 (Claude) | d06 |
| Reasoning model vs non-reasoning twin, calibration | better in 33 of 36 settings | d08 |
| Task split across turns | -39% average | d01 |

**Calibration in 2026.** Mixed. QA calibration improves with reasoning (d08). RLVR may re-create overconfidence (d09, snippet only). Spread across 2026 models is wide (ECE 0.122 to 0.726; b16). No test on diagnostic claims exists.

**Benchmark vs human evidence.** Benchmarks show gains with execution feedback. Human studies show confidence rising faster than accuracy (b24). Both can be true: the model is good with a verifier and poor without one, and the person cannot tell which situation they are in.

## 7. What our agent should take

Schema part key: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status: [E] established, [S] single-source, [C] contested. Evidence ids refer to evidence files; K ids to claims.jsonl.

### Add now (established)

These mostly confirm existing schema rules. None needs a new element. They are listed so the link between this subfield and the schema is explicit.

1. **Stated confidence is not evidence; never gate on it.** Confirms G10 and 4b ("verbal confidence to stop"). Schema G10/4b. [E] a17, a18, b14, b16, b17, b19, d08, d09 (K09). Add to the G10 evidence line: a model said "99% confident" about a false pin claim (a04) and 2026 models range ECE 0.122 to 0.726.
2. **Self-review without external output does not repair.** Confirms G2 and 4b. Schema G2. [E] b18 plus schema sources (K12).
3. **Revise only from real, located output.** Confirms G2/S5. External feedback gave the largest gains in RTL work (+22.2, +24.6) and embedded work (50.0 to 65.1). Schema G2, S4, S5. [E] for direction (K08, K19); magnitude is benchmark-specific. Evidence: b09, b10, b11, d15, a16, c13.
4. **Image-derived structure is perception, and perception is error-prone.** For S2: treat any model-read netlist from an image as a hypothesis with a source tag, not a fact. Schema S2. [E] that perception is unreliable (K17: a23, a24, a25, c15, c16, d06, d07). The effect of a netlist step on diagnosis is not measured, so the step itself goes in "Test first" (T1, T2).
5. **Report accuracy per token, not accuracy alone.** Confirms G7/G12. Costs differed 5x or more at similar accuracy (c05, c23). Schema G12. [S] as a hardware measurement, [E] as a schema rule (K06).

### Test first

Each item below is single-source, human-only, benchmark-only, or untested on hardware. None goes into SCHEMA.md until its test passes (see UNKNOWNS.md).

6. **Measurement-before-physical-claim gate (G10/S2).** Any claim about physical state from an image or unverified description needs a stated check before action. Evidence: a01, a03, a04 (one study, 3 cases), d05 (consumer repair skips continuity tests), d12 (verifiers under-used). [S] (K01, K25).
7. **Source-tagged state register (S4/S5, memory).** Running `measured / ruled_out / open` list replaces raw history in multi-turn loops. Evidence: d01, d02, b02, c03, d11 (abstract). [S] (K02, K23).
8. **Cost-weighted discriminating-test ordering (S3/S7).** Order candidate causes by expected split per cost, in code. Evidence: a02, a09 (not opened), d10, c03. [S] (K03).
9. **Forced symptom-to-owner trace (S3, O5 work backwards).** Evidence: a14, b08, a12 (36% root vs 55% proximate). [S] (K05).
10. **Cheap-verifier-first ordering and forced act-on-result (S4).** Compile, then I/O, then trace; a measured result must change the next hypothesis ranking. Evidence: d15, d12, c14, c26. [S] (K22, K27).
11. **First-person uncertainty phrasing in outputs shown to people (S9).** Output style only; never a gate. Evidence: a19, b20, a20. [S] (K11). Needs a human or simulated reader.
12. **Concise-answer step (S9).** Evidence: b04, b06. [S] (K16). Low cost; metric is a judge scale.
13. **Summarised signals instead of raw dumps (S2).** Evidence: a15, b10, c17. [S] (K07).
14. **Text-first input where possible.** Evidence: a25, d07 (mixed). [C].
15. **Do not rely on RAG for weak models.** Evidence: c13, a16. [S] (K19 part).

## 8. Concrete tests on our bench

All tests use both arms at equal total tokens (setup cost counted, G7). "Plain" means the same model with the same budget and no new step. Items must be built from what our bench can run: text-described faults with a simulated or scripted sensor, netlist and measurement tasks, plus RTL bug items with a simulator. We cannot run bench-photo tasks yet (section 10).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Fault items whose prompt contains an image-derived-style claim, some planted wrong (wrong pin, polarity). Scripted sensor answers continuity/voltage queries | A: plain. B: measurement-before-claim gate (source tags plus one forced check on each image-derived claim the hypothesis depends on) | Wrong-action rate (acts on a planted false claim); turns to root cause; tokens | Wrong-action rate down at least 25% relative; turns not worse by more than 10% |
| T2 | Same items, claims given as model-extracted text netlist vs raw description | A: raw. B: netlist extraction plus consistency check | Resolve rate; wrong-claim count | Small to medium; tests whether the step pays for itself |
| T3 | Multi-turn fault items (6-12 turns, scripted sensor replies) | A: full history. B: model-written state register, code-validated | Turns-to-fix; wrong-commit rate; resolve rate | Fewer turns and wrong commits; reliability (spread over 10 runs) gains more than the mean |
| T4 | Faults with 4-8 hypotheses, cost-annotated tests, one cheap discriminating test | A: model's own order. B: code ranks by expected split / cost from model priors | Tests to root cause; total test cost | 20-40% fewer tests (UoT scale: 13.4 to 7.8 turns) |
| T5 | HWE-Bench subset or our own RTL repair items checked by simulation, stratified by symptom-to-owner distance | A: plain agent. B: forced symptom-to-owner trace before patch | Resolve rate; file-level precision; wrong-module edit rate | Precision up; resolve rate up a few points where the owner is not the symptom file |
| T6 | RTL debug items with three verifiers: compile, testbench I/O, trace | A: plain. B: cheapest-first plus forced act-on-result. C: single verifier | Pass@1 per token; gain per token by verifier | Cheap verifier gives most gain per token; check additivity |
| T7 | Diagnosis items where a tool or sensor label is sometimes wrong | A: plain. B: rule "a measurement must update the ranking; mismatches are logged" | Missed corrections (tool right, agent wrong); false flips (tool wrong, agent flipped) | Missed corrections below the 47.5% reference without false flips above 15.2% |
| T8 | Same fault items, scored for calibration | Agent states probability of final cause; compare verbal number vs agreement over 5 independent samples | ECE; AUROC right vs wrong | Consistency beats verbal (Xiong-scale gap); verbal still overconfident |
| T9 | Hardware-flavoured text QA with a simulated reader (second model picks an answer) | A: plain phrasing. B: first-person hedge on low-evidence claims | Reader agreement with wrong claims; reader accuracy | Agreement with wrong claims down, with a smaller drop on right claims (Kim et al. pattern) |
| T10 | HDL/debug questions | A: plain. B: concise-answer step | Core-answer correctness by blind judge; tokens | Core quality up, tokens down; small |
| T11 | Raw trace dump vs summarised signal table in context | A: raw. B: summary | Pass@1 | Summary at least as good at fewer tokens |
| T12 | Whole suite T1-T7 | Scaffold vs plain at equal tokens | Resolve rate per 1K tokens | G7 check |

Run each arm at least 10 repeats per item (Laban et al. used N=10 simulations) and report mean and spread, since multi-turn effects are mostly unreliability.

## 9. What does not transfer, and why

- **HWE-Bench and Verilog numbers do not transfer to breadboard or PCB faults.** RTL tasks are checked by simulation. Physical faults need a person or sensor. 70.7% resolve says nothing about whether a chat model finds a floating MOSFET body.
- **Hu and Ash's student population.** Undergraduates with limited fundamentals, in an exam, with self-selected logs. Technicians may behave differently. No data.
- **Photo claims on a text bench.** Our bench is text. The image failure can only be modelled by planting false claims, not by testing real perception.
- **Human reliance studies.** Sun et al., Kim et al., Bo et al. measure people reading AI answers. Our agent is the AI. Only the output-style implications transfer. We cannot run a user study on the bench.
- **Calibration studies are QA, not diagnosis.** Xiong, Kadavath, Sun, Ghosh and Panday, Yoon et al. use QA, reasoning and math. Diagnostic claims are partly unfalsifiable until a test is run.
- **Consumer repair LLM-judge scores** (d05) use an LLM judge with technician reference answers. A judge with correlated errors (G4) limits the weight.
- **Industrial time-series diagnosis** (c17, d12) has a closed fault set and numeric data. Our tasks are open.
- **Trade claims** (40% of time spent troubleshooting) are not evidence.
- **Benchmarks with model versions we cannot rerun** (GPT-5.4, Opus 4.6 in HWE-Bench): read for direction only.
- **Fine-tuned small models** (VeriDebug, PCB-GPT): we use no training.
- **The simulated UoT setting** (FloDial) uses a closed fault set and an LLM-simulated answerer. Real bench answers are noisier.

## 10. Open questions

1. Does a forced "request a measurement before accepting a physical-state claim" step reduce wrong actions at equal tokens? No study exists (gap 1).
2. What is the false-claim rate per image input for current multimodal models, with a control set and bench photos? Hu and Ash give anecdotes; OmniSch and AMSbench use drawn schematics (gap 2).
3. Does LLM help change time-to-repair and success in a controlled hardware study? The authors list it as future work. Closest are software (d03) and an unread vocational study (d04) (gap 3).
4. Does first-person hedging transfer from medical QA to diagnostic advice, and does it beat numeric confidence? Numeric confidence raised bias more in Sun et al.; never tested head to head (gap 4).
5. Does ordering by cheapest discriminating test beat the model's own ranking on hardware? UoT is simulated and closed-set (gap 5).
6. Does a symptom-to-root-cause trace step reduce the symptom-fix failure (gap 6)?
7. Which verifier gives the most gain per token, and are gains additive? Only a fixed order and no token data exist (gap 7).
8. Does a model-written running summary help in long hardware chats? Recap helps only partly in general (gap 8).
9. Do Hu and Ash's findings replicate in other courses, with other models, or with technicians? None found (gap 9).
10. Do verbal overconfidence results hold for 2026 reasoning models on diagnostic claims? Mixed on QA; no diagnostic test (gap 10).
11. How much of the METR-style slowdown is verification overhead, and does it apply to hardware?
12. Why does waveform context help some models and hurt others (8 vs 13)?
13. Is the VeriPilot figure 77.1% or 85.71%?
14. Is "almost all factual errors came after image input" stable? Image input appears in 7 of 17 logs, and there is no count of errors per input type, so the claim may reflect where the authors looked.

## 11. Sources

[V] = opened and read (per the evidence `opened` flag, with critique corrections). [M] = snippet or secondary only.

**Key papers**
- [V] Hu and Ash 2026, Chat Debugging: An Exploratory Study of Human-AI Collaboration to Debug Analog Circuits. https://arxiv.org/abs/2608.02955 (a01-a05)
- [V] Ash and Hu 2026, WIP: Chat-Debugging: Large Language Model as a Hardware Debugging Assist. https://arxiv.org/abs/2608.02420 (a06, a07, b01-b03, c01-c03, c21)

**Human debugging theory**
- [M] Katz and Anderson 1987, Debugging: An Analysis of Bug-Location Strategies. https://doi.org/10.1207/s15327051hci0304_2 (a08, via Hu and Ash)
- [M] Alaboudi and LaToza 2020, Using Hypotheses as a Debugging Aid. https://doi.org/10.1109/VL/HCC50065.2020.9127273 (a09)
- [M] Jonassen and Hung 2006, Learning to Troubleshoot. https://doi.org/10.1007/s10648-006-9001-8 (a10)
- [M] Schaafstal, Schraagen and van Berlo 2000, Cognitive Task Analysis and Innovation of Training. https://doi.org/10.1518/001872000779656624 (a21)

**LLM debugging in software, and human studies**
- [V] Bo et al. 2025, Who's the Leader? https://arxiv.org/abs/2505.08063 (a11, a22)
- [V] Levin et al. 2025, ChatDBG. https://arxiv.org/abs/2403.16354 (a12)
- [V] Santos and Becker 2024, Not the Silver Bullet. https://arxiv.org/abs/2409.18661 (d03)
- [V] Becker et al. (METR) 2025. https://arxiv.org/abs/2507.09089 (b21)
- [V] Perry et al. 2023, Do users write more insecure code with AI assistants. https://arxiv.org/abs/2211.03622 (b22)
- [V] O'Brien et al. 2026, User misconceptions of LLM-based code generation. https://arxiv.org/abs/2510.25662 (b23)
- [V] Laban et al. 2025, LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (d01, d02)

**Hardware, RTL and embedded benchmarks**
- [V] Cui et al. 2026, HWE-Bench. https://arxiv.org/abs/2604.14709 and https://arxiv.org/html/2604.14709 (a13, a14, b07, b08, b25, c04, c05, c22, c23)
- [V] Yu et al. 2026, ChipBench. https://arxiv.org/abs/2601.21448 (a15, b10)
- [V] Xu et al. 2025, EmbedAgent / EmbedBench. https://arxiv.org/abs/2506.11003 (a16)
- [V] Pinckney et al. 2025, CVDP. https://arxiv.org/abs/2506.14074 (b09)
- [V] Wang et al. 2026, VeriPilot. https://arxiv.org/abs/2606.23759 (b11)
- [V] Meng et al. 2026, VeriBugBench. https://arxiv.org/abs/2609.18022 (a26, b12)
- [V] Ahmad et al. 2023, Fixing Hardware Security Bugs. https://arxiv.org/abs/2302.01215 (c24)
- [V] Towards LLM-based Root Cause Analysis of Hardware Design Failures, 2025. https://arxiv.org/html/2507.06512v1 (c13)
- [V] Benchmarking LLMs for Verilog design flows, 2026. https://arxiv.org/html/2607.22759 (d14)
- [V] AutoVeriFix+ 2026. https://arxiv.org/html/2603.11489v1 (d15)
- [M] Wang et al. 2025, VeriDebug. https://arxiv.org/abs/2504.19099 (c11)
- [M] MEIC 2024. https://arxiv.org/abs/2405.06840 (c12; 48x speedup and 93%/78% fix rates unverified)
- [M] LLM and attention-based AI for hardware design and security, survey. https://arxiv.org/pdf/2504.08854 (c27)
- [V] Saini 2026, EDA Bench. https://cdn.jsdelivr.net/gh/EDA-bench/eda-bench@master/paper/main.pdf (c14, c26)
- [V] Qiu et al. 2026, board-level schematic design. https://arxiv.org/html/2603.18102v1 (c15)
- [V] CoffeeBench 2026 (abstract only). https://arxiv.org/abs/2610.19291 (d11)

**Perception**
- [V] AMSbench 2025. https://arxiv.org/abs/2505.24138 and https://arxiv.org/html/2505.24138v2 (a23, d07)
- [V] OmniSch 2026. https://arxiv.org/abs/2604.00270 and https://arxiv.org/html/2604.00270v3 (a24, d06)
- [V] ElectroVizQA 2025. https://arxiv.org/abs/2412.00102 (a25)
- [V] UniPCB 2026. https://arxiv.org/html/2601.19222 (c16)

**Diagnosis from text and sensors**
- [V] Caminha et al. 2025, hardware diagnosis from user reports (FACTO). https://arxiv.org/html/2507.00742v1 (c19, c25, d13)
- [V] Lee et al. 2025, LLM-based frameworks for fault diagnosis. https://arxiv.org/abs/2509.23113 (c17, c18)
- [V] When LLMs sit above diagnostic tools, 2026. https://arxiv.org/html/2610.05031 (d12)
- [V] Hu et al. 2024, Uncertainty of Thoughts. https://arxiv.org/html/2402.03271v3 (d10)
- [V] Rahman et al. 2026, consumer device repair. https://arxiv.org/abs/2606.03331 and https://arxiv.org/pdf/2606.03331 (b13, d05)
- [M] Consumer repair summary page. https://themodelwire.com/article/evaluating-llms-effectiveness-on-real-world-consumer-device-repair-questions-01KT5KK2WR189G9DHGRSYQR0DD (c20)
- [M] Vocational electronics quasi-experiment, 2026. https://www.preprints.org/manuscript/202606.1898 (d04; HTTP 403, not read)
- [V] Hu et al. 2026, When LLMs Over-Answer. https://arxiv.org/abs/2607.17063 (b04-b06); [M] mirror https://www.alphaxiv.org/abs/2607.17063 (c10)

**Calibration and reliance**
- [V] Kadavath et al. 2022. https://arxiv.org/abs/2207.05221 (a17)
- [V] Xiong et al. 2024. https://arxiv.org/abs/2306.13063 (a18, b17)
- [V] Kim et al. 2024, I'm Not Sure, But... https://arxiv.org/abs/2405.00623 (a19, b20)
- [V] Bo, Wan and Anderson 2025, To Rely or Not to Rely. https://arxiv.org/abs/2412.15584 (a20)
- [V] Sun et al. 2025, LLMs are overconfident and amplify human bias. https://arxiv.org/abs/2505.02151 (b14, b15)
- [V] Ghosh and Panday 2026, Dunning-Kruger effect in LLMs. https://arxiv.org/abs/2603.09985 (b16)
- [V] Huang et al. 2024, LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b18)
- [V] Steyvers et al. 2025. https://arxiv.org/abs/2401.13835 (b19)
- [V] Yoon et al. 2025, Reasoning models better express their confidence. https://arxiv.org/abs/2505.14489 (d08)
- [M] DCPO 2026, calibration under RLVR. https://arxiv.org/html/2603.09117v1 (d09)

**Checks**
- [V] Semantic Scholar citation lookup for 2608.02955 and 2608.02420, empty (d16). [M] targeted searches (d17).
