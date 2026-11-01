# Cognitive offloading: deep document

*Subfield F02.03. Sources in this folder: evidence_a-d.jsonl (ids a01-a27, b01-b26, c01-c25, d01-d20), claims.jsonl (K01-K30), critique.md. The cross-check corrections are applied (Toolformer table, PAL same-model delta, TIM date). The founding works (Salomon 1997, Risko and Gilbert 2016, Kirsh and Maglio 1994, Salomon et al. 1991, Dunn and Risko 2016) were never opened. Human numbers below come from the Gilbert-lab and Grinschgl-lab studies that were opened.*

## 1. What it is

Cognitive offloading is the use of physical action or an external tool to cut the mental work a task needs. Examples: tilting your head to read rotated text, setting a phone reminder, writing a list, using a calculator, rotating a Tetris piece on screen to see where it fits (a01, a16, b24).

Two strands meet here.

1. Human psychology. People offload when they judge it cheaper than relying on themselves. That judgement comes from beliefs about their own ability, and the beliefs can be wrong (a01, a24, a25).
2. Distributed cognition. Salomon, Perkins and Globerson (1991) and Salomon (1997) separate the effect WITH a tool (performance while using it) from the effect OF a tool (lasting change in the person after use) (a17, c19, d20). Not opened.

For our agent the question is concrete. A language model is a poor register machine. It loses count, slips on big-number arithmetic and keeps no state between calls. Code does these things exactly. The rule under test: put state, counts, sums and lists in code, and keep the model for judgement. This document asks when that helps, when it hurts, and who should decide to offload (the program or the model).

Vocabulary.
- Forced offloading: the program or experimenter requires the tool at set steps.
- Chosen offloading: the agent decides whether to use the tool.
- Effect with vs effect of: gain while the tool is present vs change after it is removed.
- Epistemic action: an action taken to learn something (rotate a piece) rather than to progress (place a piece) (a16).

## 2. History and theories in depth

**1991-1997, distributed cognition.** Salomon, Perkins and Globerson (1991) "Partners in cognition" split the effect with a tool from the effect of a tool. Salomon (1997) "Distributed Cognitions" gathers the view that cognition lives across people and artefacts (a17, c19). Only definitions were seen. Gap: what they measured about lasting change is unknown to us.

**1994, epistemic action.** Kirsh and Maglio, from Tetris: players rotate and move pieces on screen to find out what fits, which cuts mental computation (a16, c21). Not opened.

**2011, Google effects.** Sparrow, Liu and Wegner reported that expecting future access lowers recall of facts and raises recall of where to find them. Their Exp 1 was a "Google Stroop": hard trivia questions primed computer words, interaction F(1,66)=5.02, p<.03 (a10). It failed to replicate twice (section 5). Nothing in our design depends on it (K13).

**2015, saving-enhanced memory.** Storm and Stone: saving one body of material raised memory for the next, but only if the saved item was trusted (a13, b11). Follow-ups named in a search summary (Runge et al. 2019, Fellers and Storm 2024, Buchli and Storm 2025) were not read.

**2015-2016, strategic offloading and the metacognitive account.** Gilbert (2015) introduced the circle-dragging task: people set reminders on their own, more when load is high or an interruption is likely (a03). Risko and Gilbert (2016) gave the review and cost-benefit frame (a01, b24). Dunn and Risko (2016) argued that choice follows the person's view of their ability, not true ability (a24).

**2019-2023, why people offload wrongly.** Boldt and Gilbert (2019): confidence guides spontaneous offloading (a06). Gilbert et al. (2020): a points task shows people over-use reminders even when internal memory pays more (a04, b02). Engeler and Gilbert (2020) tried to train metacognition (a05). Grinschgl et al. (2021) showed the memory cost of offloading and its boundary condition (a09, b04, b05). Chiu and Gilbert (2023): the effort of setting a reminder changes how much people offload (a02).

**2022-2026, new strands.**
- Meta-analyses: smartphone presence (Boettger et al. 2023, b09); forced vs chosen offloading (Burnett and Richmond 2026, a08, d01; abstract only).
- Dependence on stores: Florean et al. 2026 and "Let it go" 2026 (a14, a15, b12, b15).
- Offloading to AI: Kosmyna 2025, Liu 2026, Zhu 2026 (a23, b22, b23).
- Metacognitive training: Ngai and Gilbert 2026 (b01).

**2021-2026, the machine side.** Scratchpads (Nye 2021, c06). PAL and Program of Thoughts (c01-c04). Toolformer (c05). Chain of Code (c08). ToRA (c09). CodeAct (d12). MemGPT (c15). In 2025 the first papers that name over-calling a cognitive offloading failure of models (OTC-PO c14, SMART d09) and describe "tool-induced myopia" (c10-c13, d05-d07).

**The one formal model.** Offload if reward(offload) x P(correct | offload) beats reward(unaided) x P(correct | unaided). In the points task the unaided reward is 10, the reminder reward is 1 to 9, and forced-trial accuracy is about 50-56% internal and about 96% external, a 40-46 point gap. The indifference point follows from these (a25). People deviate toward too many reminders.

## 3. Core findings with exact numbers

Status is from claims.jsonl: Established, Single-source, Contested, Refuted.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Code beats in-model text arithmetic on large numbers (LLM) | GSM-HARD (same problems, big numbers): direct 19.7 to 5.0; CoT (Codex) 65.6 to 20.1; PAL 72.0 to 61.5. 16 of 25 inspected CoT thoughts identical on both versions, so the failure is arithmetic | PAL (c01, c02, b17, a18) | Established (K01) |
| PAL headline gain mixes models | 72.0 (Codex PAL) vs 56.9 (PaLM-540B CoT) = +15. Same model: vs Codex CoT 65.6 it is +6.4. Minerva-540B CoT 58.8 | PAL (a18, critique) | Single-source (K02) |
| PAL on counting and state tasks | Object counting PAL 96.7 (CoT 23.7 below); repeat copy +21.8 over CoT; colored objects +8.8; penguins +15; date +14.1 | PAL (b16, a18) | Single-source |
| Program of Thoughts | Mean gain about 12% over CoT on 8 sets; math word problems about 8% few-shot, financial about 15%; zero-shot GSM8K PoT 57.0 vs CoT 40.5 (GPT-3 175B); AQuA stays about 58% | PoT (a19, b18, c03) | Established with PAL (K01); AQuA limit single-source (K04) |
| Calculator patch on CoT text helps much less than a program | Mild gain over CoT, well behind PoT | PoT ablation (c04, b18) | Single-source |
| Small model with calculator beats big model without | ASDiv/SVAMP/MAWPS: Toolformer 40.4/29.4/44.0; GPT-3 175B 14.0/10.0/19.8; OPT-66B 6.0/4.9/7.9; GPT-J 7.5/5.2/9.9; Toolformer with calls disabled 9.6/5.0/9.3; calculator used on 97.9% of examples (corrected table) | Toolformer (c05, critique) | Single-source (K03). Part of the gain is tool-trace finetuning |
| Multi-step computation in the model degrades with size | 3-digit by 3-digit multiplication: ChatGPT 55%, GPT-4 59%; near zero at larger sizes; scratchpad finetuning helps in distribution only | Faith and Fate (a21, c17) | Established (K05) |
| Scratchpads help | Polynomial evaluation 8.8% (few-shot) and 31.8% (finetuned) vs scratchpad 20.1% and 50.7%; 9-10 digit addition out of distribution fails without scratchpad | Nye et al. (c06) | Established with c17 (K05) |
| Run what is runnable, simulate the rest | BIG-Bench Hard 84% (+12 over CoT) with text-davinci-003, 91% with GPT-4; code-only fails non-algorithmic tasks | Chain of Code (a22, b19, c08) | Single-source (K06) |
| Exact symbolic arithmetic in one pass | OccamLlama 100.0 vs GPT-4o + Code Interpreter 99.8 vs GPT-4o 39.5; GPT-4o+code used over 50x more generation tokens | OccamLLM (c07) | Single-source (K22); needs weights |
| Code as the action format | Code beat text/JSON on 12 of 17 models in success and turns; up to 20% higher success; gpt-4-1106 +20.7 points on M3ToolEval | CodeAct (d12) | Single-source |
| Forced code vs chosen code, same model | GPT-4o: question only 80.6, all text 79.9, all code (forced) 80.3, Code Interpreter (chosen) 83.5. GPT-4o-mini: 67.6, 75.9, 77.4, 80.8. GPT-3.5: 65.3, 65.3, 68.1, 64.5. Forced code beat text on average, 77.2 vs 73.9 | Chen et al. 2025 (d10) | Single-source (K23). Chosen beat forced for 2 of 3 |
| Models mis-route code vs text in the middle range | GPT-4o uses text for easy and code for very large multiplication, misses code in between | Chen 2025 (d11) | Single-source |
| Tool access lifts accuracy, lowers reasoning quality | PYMATH, 1,679 problems. o4-mini 45.1 to 64.4 (+19.3); GPT-4.1 24.6 to 27.0; GPT-4.1-mini 30.0 to 28.7. Step accuracy (PRM) 93.0 to 88.9, 88.6 to 85.9, 73.6 to 67.9. Non-tool model wins pairwise reasoning up to 41.5% more. Myopia in 54.3% of audited high-risk cases | Tool-Induced Myopia, arXiv 2511.10899 (c10, d05, d06) | Single-source (K18, K24) |
| Tool use rates | Claude-Opus-4 99.8%, GPT-5 73.7%; thinking models call code on about 49.7% more problems | TIM (c11, c13, d06) | Single-source |
| Prompt-only TIM fix gives back the gain | GPT-4.1: tool 27.0; tool + hint-only prompt 25.1; tool + DPO 27.6; reasoning win rate 45.6 to 52.7 (prompt); step accuracy 85.9 to 82.9 (prompt), 83.3 (DPO), base 88.6 | TIM Table 3 (d07, c12) | Single-source (K25) |
| Over-calling is measurable; trained fixes cut it | OTC-PO up to 68.3% fewer calls, tool productivity +215.4%, accuracy comparable (Qwen2.5-3B, NQ); SMART tool use down 24%, about one-fifth the calls on GSM8K | OTC-PO (c14, d08), SMART (d09) | Single-source (K19, K26); all fixes trained |
| Paging memory | MemGPT deep memory retrieval: GPT-3.5 38.7 to 66.9; GPT-4 32.1 to 92.5; GPT-4 Turbo 35.3 to 93.4 | MemGPT (c15) | Single-source (K20); self-reported benchmark |
| Compact rewritten state | MEM1-7B 3.5x performance and 3.7x less memory than Qwen2.5-14B on 16-objective multi-hop QA; MemAct 14B matches 16x larger models with 51% shorter context | MEM1 (d18), MemAct (d19) | Single-source; trained |
| Context clearing plus memory tool (vendor) | +29% context editing; +39% with memory tool; 84% fewer tokens in a 100-turn search evaluation; N not stated | Anthropic blog (d17) | Single-source (K28) |
| Corrupted memory is followed | MINJA: injection success 98.2%, attack success 76.8%; experience-following copies the most similar record, so errors propagate | MINJA (d15), experience-following study (d16) | Established (K27) |
| Algorithm in the prompt did not rescue reasoning models | Hanoi and Checker Jumping: collapse at about the same N with the algorithm given. Reply: token limits and unsolvable cases. Lua generator for N=15 reported working on 4 frontier models in under 5,000 tokens, unquantified | Illusion of Thinking (c16, d13), Lawsen (d14) | Contested (K21, K30) |
| Humans over-use reminders | Control group underconfident: internal d=-0.90, external d=-0.68. Forced accuracy 50-56% internal vs 96% external. Training removed the confidence error but not the over-use | Engeler and Gilbert 2020 (a05, a04, b02) | Established (K08) |
| Confidence drives spontaneous reminders | 363 kept of 435. Phase 2 instructed 90.5% vs spontaneous 86.0%, p=.06, BF01=1.6 | Boldt and Gilbert 2019 (a06) | Established with a05 |
| True-feedback training helps slightly | Exp 1 N=164, d=0.26 (p=.048 one-tailed); Exp 2 N=416, d=0.26; performance feedback vs control d=0.35 (p=.006); prediction-only null | Ngai and Gilbert 2026 (b01) | Contested (K09) |
| Fake feedback and single statements do not change offloading | Confidence moved, offloading did not (2020); no gain on three measures (2025) | Grinschgl (b03) | With K09 |
| Load, delay, reward and effort drive reminders | N=52: load on accuracy F(1.81,92.5)=47.13, partial eta2=.48; condition F=38.90, eta2=.43; load x condition F=13.19, eta2=.21. Cheap reminders remove the load penalty. Gilbert 2015: 4 experiments, N=1196, externalizing 3 vs 1 target F(1,98)=43, eta2=.31 | Chiu and Gilbert 2023 (a02), Gilbert 2015 (a03), b14, a26 | Established (K10) |
| Offloading speeds the task, weakens later memory | Pattern Copy Task, N=172 per experiment. Model opened 3.61 vs 2.31 times; time 49.33 vs 55.06 s (p=.001); errors 0.19 vs 0.21; bindings 5.91 vs 7.07 of 12 (p=.009). Forced offloading with a known test almost removes the cost (Exp 3) | Grinschgl 2021 (a09, b04, b05) | Contested (K11) |
| Photo-taking impairs memory for paintings | Observe vs 5-photo d=0.62 [0.40, 0.84]; observe vs 1-photo d=0.35; 1 vs 5 d=0.26. Lectures mixed: online benefit 0.31 vs 0.26 (p=.009) | Replication 2022 (b06), Snap and Write (b08) | Contested (K12) |
| Removing an aid costs more than adding one helps | Pen to no-pen groups planned longer routes, t(132)=2.99, d=.52; group x block F(3,132)=8.42, eta2=.16 | Florean 2026 (a14, b15) | Established with b12 (K16) |
| Trusted reliable store reduces internal upkeep | N=320. After 100% reliable support: fewer prospective-memory thoughts vs none (d=0.63) and vs 50% (d=0.40); worse retrieval when withdrawn | "Let it go" 2026 (a15, b12) | Established with a14 (K16) |
| Unexpected loss of notes | Recall poorer than shallow encoding (Exps 1-3); no effect sizes read | Burnett et al. 2026 (d02) | Single-source |
| Forced beats chosen (meta-analysis) | Direction only; k, effect size and gap unread. Within-subject designs larger than between. Modality not a moderator | Burnett and Richmond 2026 (a08, d01) | Single-source (K29); size unknown |
| Required offloading equalises capacity groups | Different working-memory groups perform more alike | d04 | Single-source |
| Google Stroop failed twice | Hesselmann: 89 analysed, hard accuracy 60%, RT easy 830/901 ms, hard 825/821 ms, BF01=5.07 (BF0+=16.43 against original) | Camerer 2018 (a11), Hesselmann 2020 (a12) | Refuted (K13) |
| Smartphone presence | 22 studies, 43 effects, g=-0.14 [-0.24, -0.03], I2=61.8%; memory g=-0.23; attention -0.07 ns; Asia -0.39, Europe -0.20 ns, North America -0.03 ns | Boettger 2023 (b09) | Single-source (K14) |
| Offloading to an LLM costs recall of own work | N=54 (18 per group): could not quote 83.3% (15/18) LLM vs 11.1% (2/18) search and brain-only; full ownership LLM 9/18 vs brain-only 16/18 | Kosmyna 2025 (a23, b21) | Contested (K17) |
| Direct adoption of AI lowers later unaided reasoning | 900 randomised, 659 analysed; dependent vs no-AI -0.38 on a 1-7 scale, d=-0.28, p=.0002; self-generation-first not below baseline | Liu 2026 (b22) | Single-source |
| Alarms raise on-time action, not recall | On time: reminder 0.84, scheduled email 0.92, none 0.37; recall F(2,84)=1.12, p=.331 | b13 | Single-source |

## 4. Mechanisms and models

### 4.1 The cost-benefit rule

Offload when `R_off * P_ok_off > R_self * P_ok_self`, counting tokens and latency as costs.

Implementation: do not take P_self from the model's stated confidence. Keep a table, per task type, of measured accuracy in-model vs offloaded, updated from every run. The program reads the table and routes. Reason: humans choose from confidence, confidence is biased, and fixing confidence did not fix over-use (a05, b02, K08).

### 4.2 Why offloading helps: exactness and capacity

1. Exactness. A transformer does long multi-step computation by pattern matching, so accuracy decays with size (3-digit multiplication 55-59%, near zero larger) (a21). An interpreter does not decay. In PAL the big-number failures were arithmetic, not logic (16 of 25 identical thoughts) (b17).
2. Capacity. In humans, load lowers accuracy and reminders remove the penalty (a02). The context analogue is transcript length and noise, plus loss of mid-context items (c24, snippet only).

Implementation: a code-side state object (counters, lists, running totals, visited sets, best-so-far). The model emits operations ("append x", "increment c"). The program applies them and returns only the value needed.

### 4.3 Division of labour: model decomposes, code computes

PAL and PoT: the model writes a program where variables hold intermediate values, and the interpreter executes it (c01, c03). Chain of Code: run what is executable; where a line cannot execute (a semantic call), the model simulates it while variable state stays explicit (c08, a22). Rule: route per sub-step. Executable steps go to code. Judgement steps go to the model. Pure code fails non-algorithmic tasks (b19). Formulation-bound problems gain little (AQuA stays about 58%) (a19).

### 4.4 Who decides: forced vs chosen

Human meta-analysis direction: forced beats chosen (d01, size unread). LLM same-model data are mixed: chosen code beat forced code for GPT-4o (83.5 vs 80.3) and GPT-4o-mini (80.8 vs 77.4), reversed for GPT-3.5 (64.5 vs 68.1) (d10). Both can hold. The model mis-routes in the mid range (d11), but a rule that forces code everywhere loses the benefit of text for easy and semantic steps. Working design: a program rule per step type, set from measured error, with an optional model override that is logged.

### 4.5 Tool-induced myopia

Tool output replaces derivation. The answer improves while reasoning steps get worse (PRM step accuracy falls for all three models), errors move from arithmetic to logic and assumptions, and more calls mean a bigger reasoning gap (d05, d06). A one-sentence prompt to treat output as hints recovered reasoning quality but lost most of the accuracy gain (27.0 to 25.1 vs base 24.6) (d07).

Implementation idea: limit the tool to state and counting, have the model write the derivation first, then compare with the code result. Untested (open question 3).

### 4.6 Memory architecture

- Paging (MemGPT): small context plus recall and archival stores through function calls (c15).
- Constant-size rewritten state (MEM1): one compact state rewritten each turn (d18; trained).
- Clearing (vendor): drop stale tool results and keep a memory tool (d17).
- Store integrity: records are copied by similarity and wrong ones spread (d15, d16). So writes need a program check (type, range, source) and reads should cite a record id.

### 4.7 Human memory effects as design cautions

Saving frees capacity only if the store is trusted (a13). A reliable store stops internal upkeep, and people fail when it is withdrawn (a15). Removal costs more than addition gains (a14). Agent analogue: build the store from step 1, never drop it silently, and keep a re-read path after clearing.

## 5. What holds up

**Consistent across sources**
- Code or program offloading beats in-model arithmetic on big numbers. PAL, PoT, Toolformer, Chain of Code, ToRA and CodeAct all agree, on Codex to GPT-4-era models (K01).
- Model failure on growing multi-step computation (Faith and Fate, scratchpads, PAL error analysis) (K05).
- Human over-use of reminders from biased confidence: Gilbert 2020, Ball 2022, Froscher 2022, Kirk 2021, Sachdeva and Gilbert 2020/2024 (cited in b02). One lab dominates, so independence is overstated.
- Load, delay, reward and effort shape offloading (K10).
- Removing a store costs (Florean 2026; "Let it go" 2026) (K16).
- Wrong memory propagates (MINJA; experience-following) (K27).

**Failed replications**
- Google Stroop: Camerer 2018 (a11) and Hesselmann 2020 (a12) both null (BF01 about 5 and 9). The original author objected to word repetition, block-wise load and obsolete terms. Hesselmann fixed these and still got a null. The where-vs-what recall half is untested.
- Snap and Write: the Exp 1 interaction did not replicate in Exp 2, and online Exp 3 reversed to a photo benefit (b08).
- Metacognitive routes: confidence training fixed the confidence error but not over-use (a05). Fake feedback and single statements did nothing (b03).

**Contested**
- Memory cost of offloading: Grinschgl found worse memory, Storm and Stone found better memory for later material. Learning goal and trust are the proposed resolution, never tested in one design (K11, K15).
- TIM: large gain for o4-mini only; GPT-4.1 +2.4 and GPT-4.1-mini -1.3. One paper, one benchmark (hard competition math). Per-bin dose-response values are in a figure only.
- Illusion of Thinking: the reply cites token limits and unsolvable instances (d14). Lawsen's Lua result is unquantified and preliminary.
- Kosmyna: N=54, preprint, EEG not read.

**Moderators seen** (b25): learning goal, trust in the store, reliability, task type (action vs recall), modality (in person vs online), region (Asia g=-0.39 vs North America -0.03), who makes the first attempt, working-memory capacity, effort of the offloading act, delay, reward.

**Interventions that worked**
- True performance feedback after predictions (d about .26-.35) (b01).
- Telling people the memory test is coming, with forced offloading (Grinschgl Exp 3) (b05).
- Self-generation first, then AI (Liu 2026: not below baseline) (b22).
- A cheap offloading act (a02).
- Trained call penalties for models (OTC-PO, SMART) (d08, d09).

**Interventions that did not work**
- Predictions alone, fake feedback, single feedback statements (b01, b03).
- Calibrating confidence alone (a05).
- Giving the algorithm in text to reasoning models (c16).
- A prompt-only TIM fix, which gave back most of the tool gain (d07).
- A calculator patch on CoT text (c04).

## 6. Language models

**Arithmetic and counting (older models, 2022-24).**
- GSM-HARD: CoT 65.6 to 20.1, PAL 72.0 to 61.5 (Codex) (c02). The same-model PAL gain on original GSM8K is +6.4 (72.0 vs 65.6), not +15 (critique).
- Object counting PAL 96.7 (b16).
- Toolformer (GPT-J 6.7B) 40.4/29.4/44.0 vs GPT-3 175B 14.0/10.0/19.8. The disabled-calls row (9.6/5.0/9.3) shows finetuning is part of the story (c05).
- OccamLlama 100.0 vs GPT-4o 39.5 on an arithmetic average (c07).
- Chain of Code 84% on BBH, 91% with GPT-4 (b19).

**Same-model code interpreter on newer models (2025).** The effect is not uniform: o4-mini +19.3, GPT-4.1 +2.4, GPT-4.1-mini -1.3 (d05). This is hard competition math, not counting. No 2026 test of pure counting or state tasks on frontier models was found.

**Choice of code vs text.** GPT-4o skips code in the mid-complexity range (d11). Chosen code beat forced for GPT-4o (83.5 vs 80.3) and GPT-4o-mini (80.8 vs 77.4), not for GPT-3.5 (64.5 vs 68.1) (d10). Thinking models call code on about 50% more problems (d06). Claude-Opus-4 used code on 99.8% of PYMATH problems and GPT-5 on 73.7% (c11).

**Over-calling.** Models call tools for questions they could answer (d09). RL on correctness alone raises call counts (c14). Trained fixes work. Prompt-only budgets are unmeasured.

**Reasoning quality.** Tool access shifts errors from arithmetic to logic, assumption and creativity (c10). The hint-only prompt: reasoning win rate 45.6 to 52.7, accuracy 27.0 to 25.1 (d07). DPO on matched pairs: accuracy 27.6, win rate 58.2%, but step accuracy 83.3 stays below base 88.6.

**Algorithms in text vs code.** Giving the full Hanoi algorithm did not raise accuracy in reasoning models (c16, d13). Lawsen reports a 15-disk generator function succeeds on four frontier models (d14). Unquantified. A state-tracking loop executed by code has not been measured.

**Memory systems.** MemGPT GPT-4 deep memory retrieval 32.1 to 92.5 (c15, self-reported). Vendor: +29%, +39%, 84% fewer tokens (d17, no N). MEM1 and MemAct are trained (d18, d19). None is a controlled equal-token test of a program-forced store.

**Memory safety.** Agents follow stored records: injection 98.2%, attack success 76.8% (d15). Whether an agent detects a corrupted store on its own has not been measured.

**Human cost when the LLM is the store.** Not model behaviour, but relevant: 83.3% could not quote their own essay (a23); d=-0.28 on later unaided reasoning after direct adoption (b22).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory (SCHEMA.md section 5). Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Counts, sums and running totals live in code, never in prose.** Part: G5 (code selects) and memory. [E] K01, K05. Evidence a18, b16, b17, c02, a19, c03, a21, c17, c06. Size it honestly: the same-model gain at ordinary numbers is small (+6.4, PAL vs Codex CoT); the robust gain is on large numbers and counting. It does not apply where the hard part is formulation (a19).
2. **No self-confidence gating of offloading. Trigger on measured error.** Part: G. [E] K08. Evidence a05, b02, a04, b03. Calibrating human confidence did not remove over-use. The full "program decides every transition" rule is in Test first, because the LLM evidence is mixed.
3. **Build the store from step 1; verify it before relying on it; never drop it silently.** Part: memory, G. [E] K16. Evidence a14, b15, a15, b12. Human evidence; the machine analogue costs little.
4. **Write state always when load is high, rather than on demand.** Part: memory. [E] K10. Evidence a02, a03, b14, a26. Code writes cost few tokens.
5. **Program-checked writes and cited reads for any store.** Part: memory. [E] K27. Evidence d15, d16. A wrong record is copied by similarity. Check type and range on write; log record ids on read.

### Test first

| Item | Part | Status | Evidence ids | Why not yet |
|---|---|---|---|---|
| Forced code store vs model-chosen store in multi-turn runs | G, O | [C] K07, K29 | d10, d11, a08, d01 | No direct LLM test at equal tokens |
| Route executable sub-steps to code, semantic to the model | O | [S] K06 | a22, b19, c08 | One group, older models |
| Restrict the tool to state and counts to avoid TIM | G | [S] K18, K25 | c10, d05, d07 | Dose-response is on solution code, not state |
| Prompt-only call cap (0, 1, 2, 4, unlimited) | O | [S] K19, K26 | c14, d08, d09 | All fixes trained |
| Clear context after write, with and without forced re-read | memory | [S] K15, K28 | d17, a13, a15, d02 | Vendor figure, no N |
| Show the agent its measured tool-vs-self error table | O | [C] K09 | b01, b03 | Small human effect; fake feedback null |
| Corrupt the store and measure detection | memory | [S] K27 | d15, d16 | No detection data |
| Execute algorithms in code, not text (Hanoi at growing n) | G | [C] K21, K30 | c16, d13, d14 | Disputed, unquantified |
| Told-to-code vs free choice in the mid range | O | [S] K23 | d10, d11 | One paper, older models |
| Score reasoning quality as well as the final answer | G | [S] K18 | c10, d06 | Needs a step grader |

Do not add: exact symbolic arithmetic modules (K22, needs weights), trained call-budget methods (K19), Google-effects reasoning (K13), screen-time effects (K14).

## 8. Concrete tests on our bench

All arms at equal tokens, with setup and tool tokens counted (G7). Report same-model deltas, never cross-model. At least 3 seeds. Paired by item.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Counting and list-keeping over a long sequence (30 to 200 events), plus a large-number variant (GSM-HARD style) | A: model CoT only. B: model emits ops, program holds counters and sums | Exact-match accuracy; tokens per item | B above A, gap growing with size, small gap at small size (K01, K05) |
| T2 | Same items, state needed across 5 to 20 turns | A: state in transcript. B: state in a code store, program-applied. C: store with model-chosen writes | Final accuracy; tokens | B above A; B vs C unknown (K07) |
| T3 | Items tagged calculation-bound vs formulation-bound | A: text. B: code-routed | Gain per tag | Gain on calculation-bound, near zero on formulation-bound (K04) |
| T4 | Mixed executable and semantic sub-steps | A: all code. B: all text. C: per-step routing | Accuracy | C above both (K06) |
| T5 | Hard competition-style math | A: no code. B: free code. C: code restricted to state and counts, derivation required | Final accuracy and step-level score | B raises the answer and lowers the step score; C narrows the step loss (K18, K25) |
| T6 | Tool-optional items | Call caps 0, 1, 2, 4, unlimited | Accuracy vs tokens curve; calls per correct answer | Accuracy flat beyond a low cap (K26) |
| T7 | Long-context multi-step runs | A: keep all. B: clear after write, no re-read. C: clear after write, forced re-read | Later-step accuracy; tokens | C near A at fewer tokens; B worse (K15, K28) |
| T8 | Runs with a planted wrong value in the store | A: unchecked store. B: program-checked write and cited read | Rate the wrong value reaches the answer; detection rate | B lower (K27) |
| T9 | Store from start vs added mid-run vs removed mid-run | Three arms | Recovery accuracy | Removal costs more than late addition gains (K16) |
| T10 | Hanoi, n = 6 to 15 | A: algorithm in text. B: code executes it, model only calls it | Successes per n | B holds at high n (K21, K30) |
| T11 | Items with a measured error table | A: no table. B: table in context. C: program routes by table | Routing accuracy | C above B above A; B vs A small (K09) |
| T12 | Mid-range counting or multiplication | A: told to use code. B: free choice | Code-use rate; accuracy | A above B in the mid range (K23) |

## 9. What does not transfer, and why

- **Memory cost of offloading (Grinschgl, Kosmyna).** These concern a person's later memory of offloaded content. A model has no lasting memory to degrade. Its state is its context or store, so the analogue is a re-read path, not memory training.
- **Google effects.** Refuted twice and tied to human retrieval (K13).
- **Photo-taking and smartphone presence.** Attention and encoding in people. No agent analogue (K12, K14).
- **Metacognitive training with true feedback.** The human effect is small (d about .26-.35). An in-context error table is a different intervention. Test it, do not assume.
- **Effort of the offloading act.** In humans effort changes behaviour. For an agent the cost is tokens and latency, which we set.
- **OccamLLM.** Needs weight access (K22).
- **OTC-PO, SMART, MEM1, MemAct, DPO for TIM.** All trained. Our agent is a frozen API model plus scaffold.
- **Dependent vs autonomous offloading to AI (Zhu 2026, Liu 2026).** About human agency and motivation.
- **The Salomon "effect of a tool".** Measurable in a scaffold only by removing the scaffold mid-run. No study did this for models.

## 10. Open questions

1. Does a program-forced code store beat a model-chosen store at equal tokens in multi-turn runs? No direct LLM test.
2. What is the same-model effect of code offloading on frontier 2025-2026 models for plain counting and state? Existing same-model data are hard competition math.
3. Does tool-induced myopia occur when code only holds state? Per-bin values are in a figure.
4. What are the k, effect sizes and forced-minus-chosen gap in Burnett and Richmond 2026?
5. Does clearing content after writing help or hurt, with and without a re-read step?
6. What did Salomon, and Salomon, Perkins and Globerson, report? Is there an "effect of" in LLM scaffolds once removed?
7. How do call budgets trade accuracy against tokens for frozen API models controlled by prompt only?
8. Are models more reliable at following an instructed offloading strategy than inventing one? Human: 90.5% vs 86.0%, p=.06. No LLM equivalent.
9. Do agents detect a corrupted store on their own?
10. Does the Illusion of Thinking collapse survive when code executes the algorithm? Lawsen's result is unquantified.
11. Does the picture differ for thinking models, which call code on about 50% more problems?

## 11. Sources

[V] opened, [M] snippet or secondhand only. Evidence ids in brackets.

**Human studies and reviews**
- [M] Risko and Gilbert (2016) Cognitive offloading. https://discovery.ucl.ac.uk/id/eprint/1508770/ and https://doi.org/10.1016/j.tics.2016.07.002 [a01, b24, c20]
- [V] Chiu and Gilbert (2023) Physical effort of reminder-setting. https://discovery.ucl.ac.uk/10176285/1/chiu-gilbert-2023-express-influence-of-the-physical-effort-of-reminder-setting-on-strategic-offloading-of-delayed.pdf [a02, a07, a26]
- [V] Gilbert (2015) Strategic offloading of delayed intentions. https://pmc.ncbi.nlm.nih.gov/articles/PMC4448673/ [a03, a27]
- [M] Gilbert et al. (2020) Optimal use of reminders. https://doi.org/10.1037/xge0000652 [a04]
- [V] Engeler and Gilbert (2020) Metacognitive training. https://pmc.ncbi.nlm.nih.gov/articles/PMC7584199/ [a05, a25]
- [V] Boldt and Gilbert (2019) Confidence guides spontaneous offloading. https://pmc.ncbi.nlm.nih.gov/articles/PMC6889107/ [a06]
- [M] Burnett and Richmond (2026) meta-analyses, abstract only. https://doi.org/10.3758/s13421-025-01743-8 and https://europepmc.org/article/MED/40500483 [a08, d01]
- [V] Grinschgl et al. (2021) Consequences of cognitive offloading. https://pmc.ncbi.nlm.nih.gov/articles/PMC8358584/ [a09, b04, b05]
- [M] Sparrow, Liu and Wegner (2011). https://www.science.org/doi/10.1126/science.1207745 [a10, b10, c22]
- [M] Camerer et al. (2018). https://osf.io/wmgj9/ [a11]
- [V] Hesselmann et al. (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/ [a12]
- [M] Storm and Stone (2015). https://doi.org/10.1177/0956797614559285 [a13, b11]
- [V] Florean et al. (2026) Get the unbalance right. https://pmc.ncbi.nlm.nih.gov/articles/PMC13022156/ [a14, b15]
- [V] "Let it go" (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13486017/ [a15, b12]
- [M] Kirsh and Maglio (1994). https://doi.org/10.1207/s15516709cog1804_1 [a16, c21]
- [M] Salomon, Perkins and Globerson (1991). https://doi.org/10.3102/0013189X020003002 [a17, d20]
- [M] Salomon (1997) Distributed Cognitions (book) [c19, d20]
- [M] Dunn and Risko (2016). https://doi.org/10.1111/cogs.12273 [a24]
- [V] Ngai and Gilbert (2026). https://europepmc.org/article/PMC/PMC12982714 [b01, b02, b03]
- [V] Photo-taking replication, Psychon Bull Rev 2022. https://europepmc.org/article/PMC/PMC9296013 [b06]
- [M] Henkel (2014), via the 2022 replication. https://europepmc.org/article/PMC/PMC9296013 [b07]
- [V] Snap and Write (2025). https://europepmc.org/article/PMC/PMC12109291 [b08]
- [V] Boettger et al. (2023) brain drain meta-analysis. https://europepmc.org/article/PMC/PMC10525686 [b09]
- [V] Alarms and scheduling. https://europepmc.org/article/PMC/PMC13296345 [b13]
- [V] Time-based reminder setting (2025). https://europepmc.org/article/PMC/PMC12589243 [b14]
- [V] Burnett et al. (2026) consequences of offloading. https://europepmc.org/article/MED/42622798 [d02]
- [V] Age and partial offloading. https://europepmc.org/article/MED/41538170 [d03]
- [V] Individual differences in offloading. https://pmc.ncbi.nlm.nih.gov/articles/PMC12263121/ [d04]
- [V] Kosmyna et al. (2025) Your brain on ChatGPT. https://arxiv.org/abs/2506.08872 [a23, b21, c18]
- [V] Liu et al. (2026) Borrowed or kept. https://europepmc.org/article/PMC/PMC13616768 [b22]
- [V] Zhu et al. (2026) Not all offloading is equal. https://europepmc.org/article/PMC/PMC13420724 [b23]

**LLM and AI studies**
- [V] Gao et al. PAL. https://arxiv.org/abs/2211.10435 [a18, b16, b17, c01, c02]
- [V] Chen et al. Program of Thoughts. https://arxiv.org/abs/2211.12588 [a19, b18, c03, c04]
- [V] Schick et al. Toolformer. https://arxiv.org/abs/2302.04761 [a20, b20, c05]
- [V] Dziri et al. Faith and Fate. https://arxiv.org/abs/2305.18654 [a21, c17]
- [V] Li et al. Chain of Code. https://arxiv.org/abs/2312.04474 [a22, b19, c08]
- [V] Nye et al. Scratchpads. https://arxiv.org/abs/2112.00114 [c06]
- [V] Dugan et al. OccamLLM. https://arxiv.org/abs/2406.06576 [c07]
- [V] Gou et al. ToRA. https://arxiv.org/abs/2309.17452 [c09]
- [V] Bayat et al. Tool-Induced Myopia ("From Proof to Program"). https://arxiv.org/abs/2511.10899 and https://arxiv.org/pdf/2511.10899v2 [c10-c13, d05-d07]
- [V] Wang et al. OTC-PO. https://arxiv.org/abs/2504.14870 [c14, d08]
- [V] Qian et al. SMART. https://arxiv.org/abs/2502.11435 [d09]
- [V] Packer et al. MemGPT. https://arxiv.org/abs/2310.08560 [c15]
- [V] Shojaee et al. Illusion of Thinking. https://arxiv.org/abs/2506.06941 [c16, d13]
- [V] Lawsen, Illusion of the Illusion of Thinking. https://arxiv.org/abs/2506.09250 [d14; c23 was snippet only]
- [M] Liu et al. Lost in the Middle. https://arxiv.org/abs/2307.03172 [c24]
- [M] Qian et al. tool overuse [c25]
- [V] Chen et al. (2025) Steering LLMs between code and text. https://arxiv.org/pdf/2410.03524 [d10, d11]
- [V] Wang et al. CodeAct. https://arxiv.org/pdf/2402.01030 [d12]
- [V] MINJA. https://arxiv.org/pdf/2503.03704 [d15]
- [V] Experience-following and error propagation. https://arxiv.org/pdf/2505.16067 [d16]
- [V] Anthropic context management post. https://claude.com/blog/context-management [d17]
- [V] MEM1. https://arxiv.org/abs/2506.15841 [d18]
- [V] MemAct. https://arxiv.org/abs/2510.12635 [d19]

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 7 established claims: 3 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F02.03-K05** (reworded: the sources support less). Numbers (55%, 59%) match, but 'scratchpads help in distribution only' is too strong: Nye et al. report scratchpad-trained models improve on out-of-distribution 9-10 digit addition with scale; Faith and Fate only find the scratchpad boost diminishes to zero as complexity grows. Corrected claim: Models fail multi-step computation held in the model as size grows (3-digit multiplication 55% ChatGPT, 59% GPT-4; accuracy decays toward zero on larger sizes); explicit scratchpads help, but in Faith and Fate the gain shrinks to zero as complexity grows and fine-tuned GPT-3 does not generalise, whereas Nye et al. find scratchpad-trained models improve out-of-distribution on 9-10 digit addition as model size increases.
- **F02.03-K07** (reworded: the sources support less). Human half holds (Burnett and Richmond abstract: benefit larger when forced; Engeler and Gilbert / Ngai and Gilbert: reminder over-use). But the LLM comparison in Chen et al. is mixed: model-chosen Code Interpreter beat forced all-code for GPT-4o (83.5 vs 80.3) and GPT-4o-mini (80.8 vs 77.4) and lost only for GPT-3.5 (64.5 vs 68.1). Corrected claim: In humans, a meta-analysis (abstract only) finds the offloading benefit larger when forced than when chosen, and people over-use reminders from biased confidence. For LLMs the evidence is mixed: forced code usually beats text, model-chosen code (Code Interpreter) beat forced all-code for GPT-4o and GPT-4o-mini but not GPT-3.5, and a program-controlled code+text+summary combination was best overall in Chen et al.
- **F02.03-K16** (reworded: the sources support less). Let it go (N=320) shows people given a 100% reliable reminder reduced (not stopped) intention-related thoughts and retrieved worse when it was withdrawn; the removal-costs-more result comes from one route-planning task (Florean et al.), not offloading in general. Corrected claim: In a prospective-memory experiment (N=320), people who had experienced a 100% reliable reminder reduced intention-related thinking and retrieved worse when it was unexpectedly withdrawn; in two route-planning experiments, removing an offloading aid hurt performance more than introducing one helped.
- **F02.03-K27** (now single-source: the sources are not independent). MINJA (Dong, He, Tang, Xiang et al.) and the experience-following paper (Xiong, He, Tang, Xiang et al.) share authors Pengfei He, Jiliang Tang and Zhen Xiang, so they are one research group; numbers 98.2% and 76.8% do match MINJA.
