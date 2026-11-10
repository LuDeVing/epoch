# Cognitive artifacts: deep document

*Subfield E13.04, cognitive systems engineering. Evidence ids (a01..d19) are in evidence_a-d.jsonl; claim ids (E13.04-K01..K33) are in claims.jsonl; cross-check notes are in critique.md. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A cognitive artifact is a human-made object or interface that holds, shows or computes part of a thinking task. Examples: a speed card in a cockpit, a diagram, a notebook, a calculator, a GPS, a Tetris screen that lets you rotate a piece to see it.

The field asks one question: how do tools and interfaces change thought, for better or worse? It has four lines.

1. **System view.** The artifact does not amplify the person. It changes the task the person faces (Norman 1991). The cockpit as a whole "remembers" its speeds (Hutchins 1995).
2. **Representation view.** Two displays with the same facts can differ in how hard they are to search and read (Larkin and Simon 1987; Zhang and Norman 1994).
3. **Action view.** Acting on the world can be cheaper than thinking about it (Kirsh and Maglio 1994, epistemic action).
4. **Offloading and dependence view.** People hand work to tools, sometimes too eagerly, and may lose the unaided skill (Risko and Gilbert 2016; Ngai and Gilbert 2026; GPS and LLM-essay studies).

Why it matters for our agent. Our agent is a model plus code. The code is the artifact: it lays out state, validates output, hides or shows tools, stores memory, and chooses the output format. The model is the "person" using it. So this subfield is the theory of the interface between code and model. The LLM literature calls it the agent-computer interface (ACI), tool design, or prompt format.

Honest limit. The founding human papers (Norman, Hutchins, Larkin and Simon) were not opened in full. Only Kirsh and Maglio, Zhang and Norman, Clark and Chalmers and Kirsh 1995 were read (critique.md, d19). The human-to-LLM mapping is by analogy only. No source tests a cognitive-artifact prediction directly on a language model. The LLM evidence is about interface engineering, which is close but not the same.

## 2. History and theories in depth

**Clark and Chalmers (1998), the extended mind (a04, opened).** Parity principle: if an outside process does the job an inside process would do, it counts as part of the cognitive process. Test case: Otto, who has Alzheimer's and uses a notebook. Philosophical; no numbers. Design rule for us: treat the code-held state as part of the agent's memory, so it must be as reliable and as available as memory would be.

**Norman (1991), cognitive artifacts (a05, c23; not opened).** Remembered claim: an artifact changes the task. Seen from the person ("personal view") it looks like an amplifier. Seen from the system it is a different task. A to-do list turns "remember" into "read and write a list". Unverified here.

**Hutchins (1995), Cognition in the Wild and "How a cockpit remembers its speeds" (a06, c22; not opened).** Field study of ship navigation and cockpit speed setting. Computation is spread across people and tools: speed card booklet, airspeed bugs, crew talk. No effect sizes; a qualitative case. Unverified here.

**Larkin and Simon (1987), diagram vs sentences (a08; not opened).** Remembered claim: same information, different search and recognition cost. Diagrams index information by location, so related items sit together. Unverified.

**Zhang and Norman (1994), representations in distributed tasks (b01, opened).** Tower of Hanoi isomorphs with the same formal structure. Some rules were put into the external display (physical constraints); others had to be kept in the head. Difficulty ordered by how many rules were internal. In Exp 1B (cup-style isomorphs, 18 students) all errors were on internal rules, none on external rules. Exp 2 used 24 students, Exp 3 used 36 students on nine isomorphs. Moving a rule from head to display lowers error and time. This is the clearest human result for "put the rules in the display". Boundary: small student samples, one puzzle family, no later replication in these files.

**Kirsh and Maglio (1994), epistemic action (a01, a02, d18, opened).** Tetris players rotate a falling piece more than placement needs, to see its shape. Pilot (3 players: intermediate, advanced, expert; 8 presentations per zoid pair): physical rotation takes as few as 100 ms; mental rotation of 90 degrees is estimated at 800-1200 ms. Early rotation reveals the hidden part of a piece 150-300 ms sooner. Keystroke gap at least 75 ms, average about 250 ms. A false start costs 75-750 ms, so acting early is cheap. Claim: people interleave action and thought; they do not plan fully and then act. Boundary: the timing figures come from a three-player pilot and are estimates.

**Kirsh (1995), the intelligent use of space (a03, opened).** Observational classification from video of cooking, assembly and similar work. People arrange the workspace to simplify choice, simplify perception, and save internal computation. No effect sizes.

**Offloading research (Risko and Gilbert 2016, b23, abstract; Ngai and Gilbert 2026, a12, a13, opened; Dupre and Ball 2026, a14, opened).** People decide to offload from their own estimate of memory ability. They offload too often when underconfident. Reminders cut memory errors by an order of magnitude or more in lab tasks (Gilbert et al. 2020, cited in a13). Trusted 100% reliable reminders lead people to stop holding the intention in mind.

**The "digital amnesia" wave (2011-2025), mostly weakened.**
- Sparrow, Liu and Wegner (2011) Google Stroop: failed to replicate (a09, a10, b17, c20).
- Ward et al. (2017) brain drain from phone presence: failed in a pre-registered replication (a11, b18); a meta-analysis is mixed (b19).
- Mueller and Oppenheimer (2014) handwriting beats laptops: not replicated on quiz scores (b20).
- GPS use and spatial memory (b21) and LLM essay writing (a15, b16) are suggestive but small or preprint.
- Fisher et al. (2015): web search inflates felt knowledge, 9 experiments (b22; abstract only).

**The LLM branch (2021-2026).** Scratchpads (Nye 2021), ReAct (2022), PAL (2022), Toolformer, Gorilla, tool documentation (2023), MemGPT, Reflexion, SWE-agent and the ACI idea (2024), CodeAct (2024), format-tax studies (2024-2026), tool-trust studies (2024-2026). SWE-agent named the interface-for-a-model idea outright: the ACI is a cognitive artifact built for a model.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Moving rules from head to display lowers human error | Exp 1B: all errors on internal rules, none on external; N = 18, 24, 36 across experiments | Zhang and Norman 1994 (b01) | [S] |
| Epistemic action is faster than mental work | 100 ms physical vs 800-1200 ms mental rotation (3-player pilot); false start 75-750 ms | Kirsh and Maglio 1994 (a01, d18) | [S] |
| Google Stroop effect does not replicate | N = 89, BF01 = 5.07 for null; original F(1,66) = 5.02, p < .03; Camerer project also failed | Hesselmann 2020 (a09), a10, b17 | Refuted |
| Brain drain from phone presence | Pre-registered replication null (6 conditions); meta-analysis 22 studies, 43 effects, negative overall, high heterogeneity, pooled size missing | b18, b19 | [C] |
| Laptop notes vs longhand | Laptop n = 74, longhand n = 68; more verbatim, no quiz penalty | Urry 2021 (b20) | [S] |
| People over-offload when underconfident; training fixes it | Underconfidence -14.5 to -6.3; Exp 1 N = 164, Exp 2 N = 416 | Ngai and Gilbert 2026 (a12) | [E] |
| Trusted reminders reduce self-maintenance | N = 320; 100% reliability group retrieved less when reminder removed | Dupre and Ball 2026 (a14) | [S] |
| Heavy LLM use lowers recall of own text | Session 1: 15/18 LLM users failed to quote vs 2/18 in each other group; session 4: 7/9 vs 1/9 (n = 9 per cell); preprint | Kosmyna 2025 (a15, b16) | [C] |
| Designed ACI beats plain shell (2024) | SWE-agent GPT-4 Turbo: 18.00% (54/300) Lite vs shell-only 11.00% (7 points, 64% relative); full 12.47% (286/2,294); RAG 2.67% Lite | Yang 2024 (a16, c01) | [C] |
| Designed layer on 2025 models adds little | Verified: GPT-5-Mini 59.8 to 63.0; GPT-5 65.0 to 68.4; Claude 4.5 Sonnet 70.6 to 75.4; Gemini 3 Pro 74.2 to 77.4; hurts GPT-5-Nano (44 to 14, 50 problems) | Live-SWE-agent (d01) | [S] |
| Lint-blocked edits help | Edit + lint 18.0, edit no lint 15.0, no edit tool 10.3; 51.7% (1,185/2,294) of runs had a failed edit | SWE-agent Table 3 (a17, c02, c04) | [S] |
| More interface can hurt | Iterative search 12.0 vs none 15.7 vs summarised 18.0; window 100 lines 18.0, 30 lines 14.3, full file 12.7; last-5 observations 18.0, full history 15.0 | a17, a18, c03 | [S] |
| Fixed pipeline can beat an agent loop | Agentless GPT-4: 32.00% Lite, $0.70 per issue | Xia 2024 (b04) | [C] |
| Think plus act beats act only | ALFWorld ReAct 71 vs Act 45 (best trial); worst ReAct 48; HotpotQA ReAct 27.4 vs CoT 29.4; ReAct to CoT-SC 35.1; FEVER 60.9 vs 56.3 | Yao 2022/2023 (a19, b13) | [E] |
| Offload computation to code | PAL GSM8K 72.0; GSM-HARD 61.2 vs CoT 23.3; SVAMP 79.4 vs 74.8 | Gao 2023 (b12, c07) | [S] |
| Written scratchpad | Polynomial few-shot 8.8 to 20.1; fine-tuned 31.8 to 50.7; program execution few-shot 11 to 26.5; fine-tuned 20 to 41.5 | Nye 2021 (c08) | [S] |
| Code as action format | Up to 20 points higher success, up to 30% fewer actions, 17 LLMs | CodeAct (a21, b05) | [S] |
| Structured output taxes reasoning (2024 models) | gpt-4o-mini GSM8K: NL 94.57, format instructions 87.17, JSON-mode 86.95, JSON-schema 91.71; LLaMA-3-8B Last Letter parse error 0.148% but 38.15% gap | Tam 2024 (a22, b06) | [C] |
| Format tax on 2025-26 models | Strong models near zero (Sonnet 4.6 88.7 JSON vs 89.3 CoT); Haiku 4.5 -36.2 points; Opus 4.7 AIME 96.2 to 91.0; delayed structure recovers to 80-87%; open-weight: 72 of 144 cells taxed; qwen3-8b -9.9 | d11, d12 | [C] |
| Constrained schema with reasoning field first does not hurt | Llama-3.1-8B GSM8K 80.1 to 83.8; up to 4% gain | JSONSchemaBench (d13) | [S] |
| Meaning-neutral format changes | Up to 76 points (LLaMA-2-13B); about 10 average; GPT-3.5 up to 56 over 320 formats, median spread 6.4; up to 40% on code translation (He 2024) | Sclar (b07, c18), He (a23) | [E] |
| Position in context | GPT-3.5 closed-book 56.1, oracle 88.3; below closed-book with 20 docs, answer mid-context | Liu 2023 (a24, b10) | [C] (2023 models) |
| Length alone hurts | Drops 13.9% to 85% within claimed limit; NoLiMa GPT-4o 99.3 base to 69.7 at 32K; 11 of 13 models under 50% of base at 32K | Du 2025 (d02), NoLiMa (d03) | [S] |
| Tool docs beat demos | F1 text-davinci-002: docs 0.37 vs best few-shot 0.05; gpt-3.5: 0.45 vs 0.19; docs + demos about 0.35 / 0.42-0.44 | Hsieh 2023 (b08, c09) | [S] |
| Too many tools hurt selection | RAG-MCP 43.13% vs 13.62% all tools; tokens 1084 vs 2134; bad retriever in Gorilla -21.5 and -47.6 points | b09, c10 | [S] |
| Per-state tool retrieval | Up to 50% fewer tools loaded, same accuracy; parameter schema moves choice more than name or description | d17, d16 | [S] |
| Paged memory | MemGPT deep memory retrieval GPT-4 32.1 to 92.5; GPT-3.5 38.7 to 66.9 | c13 | [S] |
| Stored reflection | Reflexion HumanEval 91 vs 80; but SWE-agent full history worse than last 5 | c14, a17 | [C] |
| Operators as callable tools | GPT-4.1 AIME2024 32.0 to 53.0; cognitive prompting 42.0; gains +4.2 to +27.2 | Ebouky 2025 (c15) | [S] |
| Tool agents are unreliable | tau-bench gpt-4o pass^1 61% retail, 35% airline; pass^8 under 25% retail | b14 | [S] |
| Models over-trust wrong tool output | Adoption 68.0% search, 40.1% sub-agent, 35.5% code executor (14 models); overrode correct answers 26.8-56.4%; warned users in 4.2% of answers; verification instruction lowers adoption | Yang 2026 (d06) | [S] |
| Silent tool errors | Accept/reject F1 60-70 for better models | Sun 2024 (d07) | [S] |
| Tool vs memory conflict | Conflict rate 14.1% (GPT-4o) to 83.2% (Llama-3 8B), mean 49.8%; math accuracy -4.5 points under conflict | Cheng 2026 (d08) | [S] |
| Tool overuse | Llama overuse above 50%; trained agent cut calls 24%, performance up over 37% | SMART (d09) | [S] |
| Acting to gain information beats thinking longer | WebArena 23% to 28% with re-check prompt; budget forcing / best-of-n under 3% | Shen 2025 (d10) | [S] |
| Multi-turn loss, restating helps partly | Average drop 39%; Snowball recovers 15-20% (GPT-4o, 4o-mini) | Laban 2025 (d04) | [S] |
| Scaffold-only control | Rule-based script 96.8 vs about 97.5 for top LLM configs | d14 | [S] |
| Scaffold dependence in fine-tuned models | 49.7% to 20.4% off-scaffold; base models unaffected | DCAS (d15) | [S] |

## 4. Mechanisms and models

Each mechanism is stated so it can be built.

**M1. Rules in the display (Zhang and Norman).** Mechanism: a rule shown at the point of action cannot be forgotten and costs no recall. Implementation: the code renders, in every state prompt, the list of active constraints and the current open checks, produced from a data structure (not typed by the model). Compare with the same rules once in the system prompt. Human prediction: errors fall on exactly the rules that moved. LLM caveat: no direct test; indirect evidence is only that restating helps 15-20% in multi-turn (d04).

**M2. Epistemic action = cheap probe.** Mechanism: a low-cost action returns information that would cost much more to compute mentally. Implementation: before committing, the code allows one probe step (run a test, print a value, run the candidate on a small input). The probe result is shown, then the model decides. Cap probes per state: too many re-checks hurt (d10), and reminders that fire every turn make agents loop (d05).

**M3. Point-of-error feedback (lint guardrail).** Mechanism: invalid actions are blocked and the exact error is shown before they enter state. Implementation: a code validator on each model output; on failure, return the failing output plus the error and let the model retry. SWE-agent: 18.0 vs 15.0 without it. Agents recover from a failed edit more often than not, but each extra failure lowers the odds (c02, c04).

**M4. Display budget.** Mechanism: a view that is too small hides context; one that is too large buries it. Implementation: a window setting per tool with a tested default (SWE-agent: 100 lines beat 30 and full file). Summarise search results; do not iterate them. History: keep the last few observations, not all (last 5 beat full history).

**M5. Format layer.** Mechanism: the format request competes with the reasoning for capacity (d11, d12). Implementation: free reasoning first; then a second call or a reasoning-first field produces the structured output; parse in code. Pick one layout per model by a small test, then freeze it (format sensitivity up to 76 points).

**M6. Tool exposure.** Mechanism: every tool description costs tokens and confuses selection. Implementation: expose only tools relevant to the current state S; write a short manual per tool, not demos (Hsieh). Parameter schema design matters more than names (d16). Retrieval must be good; a poor retriever is worse than none (Gorilla).

**M7. Code as action and as calculator.** Mechanism: code has control flow and data flow, and a real interpreter gives exact results and tracebacks. Implementation: route exact computation to an interpreter (PAL); let multi-tool steps be one code block (CodeAct).

**M8. Tool trust.** Mechanism: models adopt plausible wrong returns (35-68%). Implementation: a verification instruction in the prompt, plus a code-side second independent check when model and tool disagree (conflict rate 14-83%). Reliability labels help only partly.

**M9. Memory artifact.** Mechanism: a paged store the model queries (MemGPT) or a reflection buffer (Reflexion). Implementation: code stores facts and failed-attempt notes; the model gets only what a query returns. Content and amount interact, so test.

**M10. Calibrated offloading.** Mechanism (human): predict own success, get feedback, then choose to offload or not. Implementation for an LLM: before each step the model states whether it can answer without a tool; the code scores that against the outcome and feeds the hit rate back. Untested on prompted models (SMART needed training).

## 5. What holds up

**Replicated or consistent.**
- Think-plus-act beats act-only (ReAct, several tasks). Task-dependent: it lost to CoT on HotpotQA.
- Format sensitivity of prompts: large in two independent papers (Sclar, He).
- Over-offloading when underconfident, fixed by predictions plus feedback: replicated inside the paper (N = 164, then 416).

**Failed.**
- Google Stroop (two failures including the large project; BF01 5.07).
- Phone brain drain in a direct replication.
- Longhand-beats-laptop on quiz scores in a direct replication.
- A designed ACI as a big win on current models: the 7-point 2024 gain shrank to about 3-5 points on 2025 models, and a tool layer hurt GPT-5-Nano.
- Lost-in-the-middle as a clean U-curve on current models is not shown. No 2025-26 model was tested for position, but length itself clearly hurts.

**Moderators.**
- Model capacity: format tax is near zero for strong models and large near the capability limit.
- Baseline strength: interface gains are large against a weak baseline (shell, 2024) and small against a strong one.
- Task type: structured output hurts reasoning, can help classification.
- Tool reliability: trust in reliable reminders moves effort away from self-maintenance (human).
- Working-memory capacity moderates the saving benefit (Buchli and Storm 2025, abstract only).
- Memory amount: reflections help, full history hurts.

**Interventions that worked.** Lint-blocked edits; summarised search; 100-line window; last-5 history; tool docs over demos; per-state tool retrieval; reasoning-then-format; verification instruction against corrupted tools; prediction plus feedback (humans); acting to re-check (web agent).

**Interventions that did not.** Iterative search; full-history context; poor retriever; reliability labels (partial); prompting and RAG for tool-memory conflicts; restating each turn (only 15-20% recovered); every-iteration reminders (loops).

**Weak spots in the evidence.** Single runs. 300-task benchmarks where 1-3 points are noise (SWE-agent's own 6-run Lite spread is about 17.3-18.7). None of the LLM studies hold tokens equal between artifact and no-artifact arms (SWE-agent costs 8-13x more). Founding papers not read.

## 6. Language models

**Interface effects on models are real but shrinking.** On GPT-4 Turbo in 2024 a purpose-built ACI took SWE-bench Lite from 11.00 to 18.00. A fixed pipeline with no tool loop got 32.00 (Agentless), so the baseline was weak. In late 2025 bash-only agents reached 59.8-74.2 on Verified. The added layer was worth 3.2-4.8 points on four models and negative on the smallest (GPT-5-Nano 44 to 14 on 50 problems). Take: a layer is worth testing per model, and may not be worth its tokens.

**Format.** Prompt-layout changes swing accuracy by about 10 points on average and up to 76. Structured output lowers reasoning on 2024 models (gpt-4o-mini GSM8K 94.57 to 86.95 in JSON-mode). On 2025-26 models the cost is near zero for strong ones and large near the limit (Haiku 4.5 -36.2). A reasoning-first field or a reformat pass recovers most. Parsing failures are not the cause.

**Tools as thought aids.** PAL, scratchpads, code actions, and cognitive tools as callable operations all lift scores (PAL +40 on GSM-HARD; cognitive tools GPT-4.1 AIME 32.0 to 53.0). The cognitive-tools result is the nearest direct test of our O1-O8 as tools; single source.

**Trust and calibration.** Models over-trust wrong tool returns (35.5-68.0% adoption), overwrite correct answers (26.8-56.4%), and seldom warn users (4.2%). Tool and memory disagree 14-83% of the time. Tool overuse exceeds 50% in Llama. Fixes by prompting are partial. Calibrated tool use was fixed by training (SMART), not by prompting.

**Context.** Length alone hurts even with perfect retrieval (13.9-85% drops). Effective context is 1-8K for most models on non-literal matching; 11 of 13 models fall below 50% of base at 32K. Multi-turn instruction loss averages 39%; restating recovers 15-20%.

**Scaffold dependence.** A frozen model gains while the scaffold is present and nothing carries over. Fine-tuned models become dependent on their scaffold's conventions (49.7% to 20.4%). A scaffold alone, with no model, can score 96.8 vs 97.5 on one benchmark, so every benchmark needs a scaffold-only control.

**Reliability.** tau-bench: pass^8 under 25% in retail where pass^1 is 61%. Report pass^k.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory.

### Add now (established)

1. **Format sensitivity: choose one layout per model by a small test, then freeze it.** Part: S display. [E]. Evidence: b07, c18, a23.
2. **Think and act interleaved, not act only.** Part: O probe loop. [E] for act-only vs think+act; task-dependent versus CoT. Evidence: a19, b13, c05.
3. **Calibrate tool use with predictions plus feedback (human evidence).** Part: G calibration. [E] in humans only; the LLM version stays in "Test first". Evidence: a12, a13, b23.
4. **Do not rely on any single interface effect from 2024 numbers.** Part: G7 (pays for itself at equal tokens). [E] as a process rule, supported by the weak-baseline finding. Evidence: d01, b04.
5. **Do not add digital-amnesia effects (Google Stroop, brain drain, longhand).** Part: none. [E] that they failed. Evidence: a09, a10, b18, b20.

### Test first (single-source or contested)

| Item | Part | Status | Evidence ids |
|---|---|---|---|
| Rules and open checks re-rendered in each state prompt (Zhang and Norman) | G / S | [S] | b01, d04, d05 |
| Code-side validator with the error shown at the point of failure | G2 / G7 checks | [S] | a17, c02, c04 |
| Limit what the state shows: summary, window of fixed size, last few observations | S | [S] | a17, a18, c03 |
| Reason first, format in a second step | output format | [C] | a22, d11, d12, d13 |
| Cheap probe before commit, capped | O probe | [S] | a01, d10, d05 |
| Show only tools relevant to the current state; one-paragraph manuals | O / tools | [S] | b08, b09, d16, d17 |
| Offload exact computation to code | tool operator | [S] | b12, c07 |
| Verification instruction plus code cross-check when model and tool disagree | G2, G10 | [S] | d06, d07, d08 |
| Predict-then-check for tool vs recall | G calibration | [S] | d09, a12 |
| Operators O1-O8 as separately called steps vs one prompt | O | [S] | c15 |
| Put goals and open checks at start and end of state | S ordering | [C] | a24, d02, d03 |
| Stored reflections vs recent-only memory | memory | [C] | c14, a17 |
| Scripted pipeline vs free loop at equal cost | architecture | [C] | b04, d01 |
| Scaffold-only control arm on each bench item | bench design | [S] | d14 |

## 8. Concrete tests on our bench

All arms use equal total tokens (input plus output, setup counted). Run on our bench items (ARC-style grids, BRAINTEASER-style puzzles, other single-answer items). Report pass@1 and pass^k.

| Item type | Arms | Metric | Expected effect |
|---|---|---|---|
| Constraint-heavy puzzles | A: rules only in system prompt; B: active rules and open checks re-rendered in each state prompt | Constraint violations per run; solve rate | B fewer violations, 10-30% relative, if the human result transfers; none if the model already attends to the system prompt well |
| Code or grid-transform items | A: no validator; B: validator blocks malformed output and shows the error | Invalid-output rate; pass rate | B +2 to +5 points; part of it is retry tokens, so hold tokens equal |
| Long-state items | A: full history; B: last-k observations plus summary | Pass rate; tokens | B equal or better at lower tokens |
| Any reasoning item with a structured answer | A: inline JSON; B: free reasoning, then reformat in code or a second call | Accuracy | B better on small models; equal on strong |
| Mixed-difficulty items | A: plan fully, then act; B: one capped probe (run a check) before committing | Pass rate; tokens to solve | B saves tokens on easy items; may hurt hard ones if probes loop |
| Many-tool items | A: all tools listed; B: tools for current state only | Tool-selection accuracy; prompt tokens | B higher accuracy and fewer tokens |
| Items with tool returns | Inject a wrong return at 20% rate; arms: none, verification instruction, code cross-check | Adoption of wrong return; final accuracy | Instruction lowers adoption; cross-check lowers it more |
| Items the model can answer unaided | A: free tool use; B: predict-then-choose with hit-rate feedback | Unneeded tool calls; accuracy | B fewer calls, same accuracy |
| Any item | C: scaffold with no model or a random model | Score | Should be near chance; if high, the item does not measure the model |
| Long-state items | Key facts and checks at start/end vs middle | Pass rate | Position effect smaller on current models than in 2023; may be near zero |

## 9. What does not transfer, and why

- **Digital-amnesia effects** (Google Stroop, brain drain, longhand). Failed in humans; they concern attention and motivation that a frozen model does not have.
- **Dependence and skill loss** (GPS, Kosmyna). A frozen model has no unaided skill to lose between sessions. Only fine-tuned models show scaffold dependence.
- **Millisecond timings of epistemic action** (100 ms vs 800-1200 ms). Human motor and mental-rotation costs. The principle (a cheap probe can beat reasoning) may transfer; the numbers do not.
- **Human UI conventions.** SWE-agent found iterative search (copied from IDEs) worse than none. Do not copy human interfaces.
- **Ethnographic claims** (Hutchins). No numbers and no testable effect; useful as a design lens only.
- **Fine-tuned-model results** (Toolformer, Gorilla, SMART, DCAS). We do not train.
- **2023 numbers on lost-in-the-middle and format tax.** Models changed; re-measure.

## 10. Open questions

1. At equal tokens on a current model, does a designed interface beat a plain tool, or was the 2024 gain a weak-baseline effect?
2. Does re-rendering rules in every state prompt lower violations for an LLM (Zhang and Norman transfer)?
3. Where should goals and checks sit in code-laid-out state on 2025-26 models?
4. Does an LLM stop checking when its tools are always right (complacency)? Does stating reliability change it?
5. Can prompting plus feedback calibrate tool-vs-recall without training?
6. Does a cheap probe save tokens or just add steps, by task type?
7. Retrieve tools per state, or use a fixed small set, at equal prompt size?
8. Do the exact founding numbers (Larkin and Simon, Norman, Hutchins) hold when read in full?
9. Do the 2025-26 format-tax results hold token-equal?
10. Why did a tool layer hurt GPT-5-Nano? Is there a model-size threshold below which an interface layer costs more than it gives?

## 11. Sources

[V] = opened this session; [M] = snippet or abstract only, or not opened.

- [V] Clark and Chalmers 1998, The extended mind. https://www.alice.id.tue.nl/references/clark-chalmers-1998.pdf (a04)
- [V] Kirsh and Maglio 1994, epistemic vs pragmatic action. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf (a01, a02, d18)
- [V] Kirsh 1995, The intelligent use of space. https://adrenaline.ucsd.edu/kirsh/Articles/Space/AIJ1.html (a03)
- [V] Zhang and Norman 1994, Representations in distributed cognitive tasks. https://pages.ucsd.edu/~scoulson/203/zhang.pdf (b01)
- [M] Norman 1991, Cognitive artifacts. https://doi.org/10.1017/CBO9780511571169 (a05, c23)
- [M] Hutchins 1995, How a cockpit remembers its speeds. https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1903_3 (a06); Cognition in the Wild https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/ (c22)
- [M] Larkin and Simon 1987. https://onlinelibrary.wiley.com/doi/10.1111/j.1551-6708.1987.tb00863.x (a08, d19)
- [V] Hesselmann 2020, Google Stroop replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/ (a09, c20)
- [M] Camerer et al. 2018 via Hesselmann and FORRT atlas. https://osf.io/wmgj9/ ; https://forrt.org/flora-replication-atlas/doi/10.1126/science.1207745/ (a10, b17)
- [M] Ruiz Pardo and Minda 2022, brain drain replication. https://pubmed.ncbi.nlm.nih.gov/36007374/ (a11, b18)
- [M] Boettger et al. 2023, brain drain meta-analysis. https://pubmed.ncbi.nlm.nih.gov/37754029/ (b19)
- [M] Urry et al. 2021, laptop replication. https://pubmed.ncbi.nlm.nih.gov/33539228/ (b20)
- [M] Dahmani and Bohbot 2020, GPS. https://pubmed.ncbi.nlm.nih.gov/32286340/ (b21)
- [M] Fisher, Goddu and Keil 2015. https://pubmed.ncbi.nlm.nih.gov/25822461/ (b22)
- [M] Risko and Gilbert 2016. https://pubmed.ncbi.nlm.nih.gov/27542527/ (b23)
- [V] Ngai and Gilbert 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12982714/ (a12, a13)
- [V] Dupre and Ball 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13486017/ (a14)
- [M] Buchli and Storm 2025. https://pubmed.ncbi.nlm.nih.gov/40879669/ (b24)
- [V] Kosmyna et al. 2025, Your brain on ChatGPT. https://arxiv.org/abs/2506.08872 (a15, b16, c19)
- [V] Yang et al. 2024, SWE-agent. https://arxiv.org/abs/2405.15793 (a16-a18, b02, b03, c01-c04)
- [V] Xia et al. 2024, Agentless. https://arxiv.org/pdf/2407.01489 (b04)
- [V] Jimenez et al. 2024, SWE-bench. https://arxiv.org/abs/2310.06770 (c12)
- [V] Xia et al. 2025, Live-SWE-agent. https://arxiv.org/abs/2511.13646 (d01)
- [V] Yao et al. 2022/2023, ReAct. https://arxiv.org/abs/2210.03629 (a19, b13, c05)
- [V] Schick et al. 2023, Toolformer. https://arxiv.org/abs/2302.04761 (a20, c06)
- [V] Wang et al. 2024, CodeAct. https://arxiv.org/abs/2402.01030 (a21, b05, c11)
- [V] Gao et al. 2023, PAL. https://arxiv.org/abs/2211.10435 (b12, c07)
- [V] Nye et al. 2021, scratchpads. https://arxiv.org/abs/2112.00114 (b11, c08)
- [V] Tam et al. 2024, Let me speak freely. https://arxiv.org/abs/2408.02442 (a22, b06, c17)
- [V] Lee et al. 2026, The Format Tax. https://arxiv.org/abs/2604.03616 (d11)
- [V] Fan 2026, Capacity, not format. https://arxiv.org/abs/2606.09410 (d12)
- [V] Geng et al. 2025, JSONSchemaBench. https://arxiv.org/abs/2501.10868 (d13)
- [V] He et al. 2024, prompt formatting. https://arxiv.org/abs/2411.10541 (a23)
- [V] Sclar et al. 2024. https://arxiv.org/abs/2310.11324 (b07, c18)
- [V] Liu et al. 2023, Lost in the middle. https://arxiv.org/abs/2307.03172 (a24, b10, c16)
- [V] Du et al. 2025, context length alone. https://arxiv.org/abs/2510.05381 (d02)
- [V] Modarressi et al. 2025, NoLiMa. https://arxiv.org/abs/2502.05167 (d03)
- [V] Laban et al. 2025, lost in multi-turn. https://arxiv.org/abs/2505.06120 (d04)
- [V] Terminal coding agent report 2026. https://arxiv.org/abs/2603.05344 (d05)
- [V] Hsieh et al. 2023, tool documentation. https://arxiv.org/abs/2308.00675 (a25, b08, c09)
- [V] Jin et al. 2025, RAG-MCP. https://arxiv.org/pdf/2505.03275 (b09)
- [V] Patil et al. 2023, Gorilla. https://arxiv.org/abs/2305.15334 (b15, c10)
- [M] Qin et al. 2023, ToolLLM. https://arxiv.org/abs/2307.16789 (c24)
- [V] Li et al. 2026, MCP metadata. https://arxiv.org/abs/2610.14334 (d16)
- [V] Gaurav et al. 2025, Dynamic ReAct. https://arxiv.org/abs/2509.20386 (d17)
- [V] Packer et al. 2023, MemGPT. https://arxiv.org/abs/2310.08560 (c13)
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366 (c14)
- [V] Ebouky et al. 2025, cognitive tools. https://arxiv.org/abs/2506.12115 (c15)
- [V] Yao et al. 2024, tau-bench. https://arxiv.org/pdf/2406.12045 (b14)
- [V] Yang et al. 2026, agents' overreliance on unreliable tools. https://arxiv.org/abs/2609.05587 (d06)
- [V] Sun et al. 2024, Tools fail. https://arxiv.org/abs/2406.19228 (d07)
- [V] Cheng et al. 2026, tool-memory conflicts. https://arxiv.org/abs/2601.09760 (d08)
- [V] Qian et al. 2025, SMART. https://arxiv.org/abs/2502.11435 (d09)
- [V] Shen et al. 2025, Thinking vs doing. https://arxiv.org/abs/2506.07976 (d10)
- [V] Zhang et al. 2026, de-scaffolding. https://arxiv.org/abs/2609.09218 (d14)
- [V] Thangarajah et al. 2026, DCAS. https://arxiv.org/abs/2608.06113 (d15)
- [M] Parasuraman and Manzey 2010, complacency (recalled, b27; not opened).

Corrections carried from critique.md: the SWE-agent shell-only gap is 7 points by Table 1 (the paper text says 10.7); HumanEvalFix 87.7 is Python only; Kosmyna session 4 is n = 9 per cell; ReAct 71 vs 45 is best trial only; cite Hesselmann (2020).
