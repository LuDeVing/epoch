# Extended and situated mind: deep document

*Subfield D06.09. Written 2026-11-20 from evidence_a-d.jsonl (a01-a29, b01-b25, c01-c25, d01-d20), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids are cited as a01, b15 and so on. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The extended mind thesis says that thinking is not always inside the head. Some tools, notes and surroundings can be part of the thinking system itself. They are not only inputs or outputs. The founding paper is Clark and Chalmers (1998, a01-a03, b22).

Related ideas sit under the same heading:

- **Extended mind.** A notebook, phone or computer can be part of a person's memory or belief system, if it is used in the right way.
- **Situated and embodied cognition.** Thought is shaped by the body and the setting, not run as a pure inner program.
- **Epistemic action.** Changing the world to make a mental task easier, such as rotating a falling block instead of imagining the rotation (a04-a07).
- **Distributed cognition and transactive memory.** Groups and artefacts hold memory and do computation (Hutchins 1995, Wegner 1987; both [M] only, a27-a28).
- **Cognitive offloading.** The empirical side: when and why people hand mental work to tools (Risko and Gilbert 2016, a17, b23, not opened).

Why it matters for our agent. Our agent is a language model with a scaffold. Its "mind" is already a mix of weights, a context window, notes, tools and code. The research here asks three practical questions.

1. Which external stores and tools actually raise reasoning quality, and by how much?
2. What makes an external store safe to trust? Clark and Chalmers say a store counts as part of the thinker only if its content is trusted on retrieval. For an agent, blind trust is a hazard.
3. When does offloading hurt? The human offloading literature suggests it might, but most of that evidence is weak.

Two limits up front. First, the philosophical claim (parity, constitution versus causation) has never been tested on a language model with numbers (critique.md). Second, almost all the LLM evidence comes from the authors' own benchmarks on 2022-2023 models. The human cognitive-offloading evidence is mostly small and partly failed replications, so it should not drive design.

## 2. History and theories in depth

### 2.1 Clark and Chalmers (1998)

The paper (a01) gives an argument from functional role. It has four pieces.

- **Parity principle.** If a part of the world works as a process which, were it done in the head, we would call cognitive, then it is part of cognition.
- **Otto and Inga (a02).** Inga hears of an exhibition at the Museum of Modern Art. She recalls the museum is on 53rd Street and walks there. Otto has Alzheimer's disease and consults a notebook. It says the museum is on 53rd Street. The authors argue Otto believed this before he looked, in the same way Inga did. In a twin case the notebook says 51st Street and Otto goes there. The point is that the notebook entry plays the belief role.
- **Coupling conditions (a03).** The resource must be reliably available and typically invoked, its content automatically endorsed (not questioned), and easily accessible. A fourth condition: the information was consciously endorsed in the past. The first three carry the main weight. The criteria are graded, not sharp.
- **Epistemic action (a04).** They borrow Kirsh and Maglio's Tetris data as support (see 2.2).

No data in the 1998 paper. The test is intuition about what we would call a belief.

### 2.2 Kirsh and Maglio (1994): the empirical anchor

Kirsh and Maglio (a05-a07) logged Tetris play. Epistemic actions change the world to reduce mental work. Pragmatic actions move toward the goal.

- Only four actions exist: left, right, rotate, drop.
- Rotation begins in earnest 400-600 ms after a block appears. Shortest time between keystrokes is about 75 ms; mean about 250 ms.
- A physical 90-degree rotation can take about 100 ms. Mental rotation of a block through 90 degrees is estimated at 800-1200 ms. This rests on three players (intermediate, advanced, expert), 8 presentations per pair, and the mental figure is an estimate. Even adding 200 ms to choose the key, the gap is large.
- A verification routine (move to the nearest wall and back) happens in a small share of drops and rises with drop height.

Limits: video game with fully determinate effects, tiny pilot. The authors state that planning needs a redefined state space that includes epistemic moves. The idea is sound; the number is weak.

### 2.3 Critics (not opened)

- **Adams and Aizawa (2001), Rupert (2004).** The standard replies are that causal coupling does not show constitution, and that extended processes differ from inner ones. Listed in a29 as [M] only. The critique file says no claim about them should be made. We record only that rival predictions were not found (K20).
- **Clark (2025), "Extending minds with generative AI" (c25, Nature Communications).** Snippet only.
- **Smart, Clowes and Clark (2025), Synthese (d06, d07, c23).** Opened. A qualitative case study that a language model plus retrieval store might count as an extended system. See 2.4.

### 2.4 Is an LLM plus a store an extended system? (Smart, Clowes and Clark 2025)

They built four conditions: GPTDEFAULT, GPTMODIFIED (same persona prompt, no retrieval), DAPARAGRAPHS and DASECTIONS (retrieval over the authors' own writing, chunked two ways). One run, 26 Dec 2023, first responses only, judged by reading, no scores. The model was gpt-3.5.

Findings that matter:

- GPTDEFAULT did not know "wideware". GPTMODIFIED knew "wideware" and "Otto" already. The weights held the facts. This is the **redundancy problem**: a store that adds nothing beyond the weights cannot be said to extend anything.
- In their app, the application code, not the model, decides when to call the store. This is the **agency problem**: the model does not itself decide when to consult it. The authors say the effect on the extension claim is unclear.
- Paragraph chunks found different material than section chunks, so retrieval granularity matters.

What we gain: two testable conditions (K25), not a formal criterion. No numbers. Perrier (2025, d17) proposes formal metrics for extended cognition in corporate knowledge systems, with a reliability-threshold idea, but only the abstract and introduction were read.

### 2.5 The empirical offloading line (humans)

- **Google effects (Sparrow, Liu, Wegner 2011).** People who expect to look something up recall less of it. See sections 3 and 5.
- **Brain drain (Ward et al. 2017).** A phone merely present lowers working memory and fluid intelligence scores. See section 5; the pooled effect is about zero.
- **Confidence guides offloading (Boldt and Gilbert 2019).** People offload when they doubt their memory.
- **Cognitive debt (Kosmyna et al. 2025).** Essay writers using an LLM could not quote their own essay.
- **Skill formation (Shen and Tamkin 2026; Maier et al. 2026; Bastani et al. 2025).** Whether AI help reduces learning.

### 2.6 The AI side: externalisation as engineering

Zhou et al. (2026, c21-c22) review externalisation in LLM agents. They name memory (state across time), skills (procedures) and protocols (interaction), unified by a harness. It is a framing, not an experiment, and adds no numbers. The extended mind link in most LLM papers is a name or an analogy. "Extended Mind Transformers" (b15, c03) borrows the name only.

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. Rows that rest on an unopened source are not listed as findings.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Physical rotation is faster than mental rotation (Tetris) | about 100 ms vs 800-1200 ms estimated; 3 players | Kirsh and Maglio 1994 (a05, a06) | [S] human, tiny pilot |
| Computer words slow Stroop after hard questions | 712 ms vs 591 ms, t(68)=3.26 (N=69); easy questions 603 vs 559, t(68)=2.98 | Sparrow et al. 2011 Exp 1 (a08) | [C] failed replications |
| Believing a fact is saved lowers recall | erase .31, erase+remember .29, save .22, save+remember .19; F(3,56)=2.80, p<.05; paired contrasts within erase and within save not significant | Sparrow Exp 2 (a09) | [C] |
| People recall where a fact is saved better than the fact | folder .49 vs statement .23, t(31)=6.70 (N about 33) | Sparrow Exp 4 (a10) | [S]; the 0.93 recognition figure from Exp 3 was not found in the text, unverified |
| Sparrow replication failed | round 1 p=.2647; pooled rounds p=.4493; of 21 studies in the project 13 (62%) replicated, replication samples about 5x larger | Camerer et al. 2018 (a11, b02) | [C]; original authors gave no materials and noted design differences afterwards |
| Google-effects meta-analysis | 22 articles, 35 comparisons, N=30,889; cognitive load d=0.73 [0.22,1.24]; self-esteem 0.91 [0.23,1.59]; behavioural 0.39 [0.16,0.61]; cognitive measurement 0.56 [-0.15,1.28] ns | Gong and Yang 2024 (a12, b04) | [C]; pools heavy-internet-use studies, not the saved-versus-erased design |
| Brain drain overall is near zero | 4,368 participants, 33 studies, 166 effects: d=-0.02 [-0.06,0.01] | Hartanto et al. 2024 (d01) | [E] null |
| Brain drain: only working-memory span shows a small effect and it is biased | OSPAN 8 studies d=-0.13 [-0.25,-0.02]; Egger p=.045; bias-adjusted d=-0.04, p=.580 | Hartanto 2024 (d02) | [E] |
| Brain drain, other meta-analysis | 22 studies, 43 effects: g=-0.14 [-0.24,-0.03]; memory g=-0.23; attention -0.07 ns; Asia -0.39, Europe -0.20 ns, N America -0.03 ns | Boettger et al. 2023 (d03) | [C]; pools use and presence |
| One small positive brain-drain study | N=42; attention 108.95 vs 99.71, F(1,40)=6.17, p=.017, eta2=.134 | Skowronek et al. 2023 (a16) | [S] |
| People offload when unsure and it helps | hit rate 82.7% (no reminders) to 88.1% (reminders), F(1,361)=39.1; N=363 analysed | Boldt and Gilbert 2019 (a13) | [S] human |
| LLM essay users cannot quote own essay | 15/18 (83.3%) vs 2/18 (11.1%) in search and brain-only; N=54 | Kosmyna et al. 2025 (a26, b10) | [C] preprint; critique by Stankovic 2026 (b11) |
| AI help lowered quiz score | d=0.738, p=.01, n=52; conceptual inquiry about 65% vs delegation about 39% | Shen and Tamkin 2026 (b13) | [C] |
| Larger test found no unaided deficit | control 0.65 vs AI-only 0.62, OR 0.80 [0.42,1.51], p=.244; N=704; +10 points of answer offloading gave OR 0.68 on test items | Maier et al. 2026 (b12) | [C] |
| Unguarded GPT tutor hurt exam results | nearly 1,000 students; practice +48% (base), +127% (tutor); exam -17% (base), tutor about equal to control | Bastani et al. 2025 (d05, b14) | [S]; only a Wharton summary read |
| Scratchpad raises multi-step computation | polynomial evaluation 8.8% to 20.1% (few-shot 137B), 31.8% to 50.7% (fine-tuned 8B); program execution 11% to 26.5% few-shot, 20% to 41.5% fine-tuned | Nye et al. 2021 (c14) | [E] with ToT (c20) |
| Search over thoughts | Game of 24: GPT-4 CoT 4% vs Tree of Thoughts 74% | Yao et al. 2023 (c20) | [S]; many more calls |
| Tools lift math and fact lookup | math ASDiv/SVAMP/MAWPS 40.4/29.4/44.0 vs 14.8/6.3/15.0 (GPT-3 175B) and 7.5/5.2/9.9 (GPT-J); LAMA 33.8/11.5/53.5 vs 26.8/7.0/39.8; calculator used on 97.9% of math items | Toolformer (a18, c13) | [S]; table columns ambiguous in extraction |
| Tool gap persists across sizes tested | 124M to 1.6B; calendar tool used 54.8% | Toolformer (a19) | [S] |
| ReAct versus CoT on HotpotQA | Standard 28.7, CoT 29.4, CoT-SC 33.4, Act 25.7, ReAct 27.4, CoT-SC to ReAct 34.2, ReAct to CoT-SC 35.1 (PaLM-540B, exact match) | Yao et al. (a20, b18, critique 5) | [S]. Correction: ReAct alone is worse than CoT on HotpotQA |
| ReAct on FEVER | CoT 56.3, ReAct 60.9, CoT-SC to ReAct 64.6 | same | [S] |
| ReAct failure types | CoT hallucination 56% of failures, ReAct 0%; ReAct reasoning error 47%, search-result error 23%; hallucinated false positives CoT 14% vs ReAct 6% (50 right and 50 wrong cases per method) | same (a21, b18) | [S] author-labelled |
| ReAct in environments | ALFWorld best 71% vs Act 45% vs BUTLER 37%, worst ReAct 48%, mean relative gain 62% (33-90%); WebShop 40.0 vs 30.1 | same (a22) | [S]; best-of-6 trials |
| Paged memory | deep memory retrieval GPT-4 32.1% to 92.5%; GPT-3.5 38.7% to 66.9%; GPT-4 Turbo 35.3% to 93.4% | MemGPT (a23, b17) | [S] author benchmark |
| Nested key-value lookup | fixed-context GPT-3.5 0% at 1 level; GPT-4 and Turbo 0% by 3 levels; MemGPT (GPT-4) unaffected | MemGPT (a24, c06) | [S] synthetic |
| Verbal reflection | +8% absolute over episodic memory alone (100 questions); HumanEval pass@1 91% vs GPT-4 80.1%; Leetcode Hard 77.1 vs 80.1 | Reflexion (b19, c09, c10) | [S] needs a signal |
| Skill library | 63 unique items in 160 iterations, 3.3x best baseline; random curriculum cut items by 93%; plateau without library; 3 runs each | Voyager (b20, c11, c12) | [E] with generative agents |
| Memory, reflection, planning raise believability | TrueSkill: full 29.89, no reflection 26.88, no reflection or planning 25.64, human crowd 22.95, none 21.21; 100 raters | Park et al. 2023 (c07) | [S]; rated believability, not accuracy |
| Interface design of tools | purpose-built interface solved 10.7 points more on 300 SWE-bench Lite items than a default shell; 12.5% pass@1 SWE-bench; 87.7% HumanEvalFix; Claude 2 with BM25 retrieval 1.96% | SWE-agent; SWE-bench (c15-c17) | [E] |
| Position in context | relevant passage in the middle cut GPT-3.5 multi-doc QA by over 20 points, below closed-book 56.1% | Liu et al. 2023 (c19) | [S] 2023 models |
| Extended Mind Transformers | 7B: 38.59/37.95/36.00/33.54% at 2k/4k/8k/16k; plain Chat Llama2 42.74/41.96/33.50/17.68%; 70B+RAG 59.34/53.13/53.00/50.00 vs GPT-4 52.28/50.00/46.00/43.29 | Klett and Ahle 2024 (c03, c04) | [S]; extended model worse at 2k and 4k (corrects b15) |
| Cognitive Workspace | reuse 54.52% (4 rounds), 57.1% (10 rounds) vs 0% RAG; 3.3x more operations; net efficiency 17-18%; d=195.66, t(18)=69.60 | An 2025 (c01, c02) | [C] 8 documents; the statistic is meaningless |
| A-Mem | about 1,200 tokens per operation vs 16,900 full context; multi-hop F1 at least 2x baselines | Xu et al. 2025 (c18) | [S] |
| Notes versus full context, when it fits | LoCoMo memory 57.68 vs long-context 92.85 (GPT-5-mini) and 81.69 (GPT-OSS-120B); LongMemEval 49.00 vs 82.40; PersonaMem 62.48 vs 69.75; memory cheaper after about 10 turns at 100k | Pollertlam and Kornsuwannawit 2026 (d11) | [E] with Terranova |
| Memory on unanswerable questions | GPT-4o-mini adversarial: A-Mem 77.64, RAG 64.93, full context 52.94; about 969 vs 23,132 tokens | Terranova et al. 2025 (d12) | [E] |
| Memory design matters | 23,440 episodes; no memory 0.00 on dependent tasks; hard tier replay 1.00/0.95/1.00, retrieval 0.70/0.35/0.45, summary 1.00/0.70/1.00, fact store 0.95/0.75/1.00, hybrid 0.80/0.60/0.50; agents act on a correctly retrieved value only 55% of the time; swapping implementation moved success up to 60 points | Mishra and Mishra 2026 MERIT (d09) | [S] pilot scale |
| Stale memory harms | corruption 0.3: hybrid +0.25 harm (Holm p=.030); LLM-extracted fact store +0.20 (raw p=.013, ns after Holm) | MERIT (d10) | [S] |
| Write gating | add-all and coarse-evaluator additions: flat or declining success; strict selective addition keeps improving; one agent passed the ground-truth-retrieval variant after about 2,000 runs | Xiong et al. 2025 (d08) | [S] simulated streams |
| Looping | CodeGym Qwen3-8B loops 29.0% (full history), 57.3% (4,096-token compression); looping runs fail 59.5% vs 33.4%; action log cuts repeats 3.3% vs 48.8%; exact-duplicate blocker 71.3% vs 69.8% | DeLoop (d14, d15) | [S] |
| Tool loop at matched tokens | Qwen3-8B AIME24/25/Beyond: SC 73.3/56.7/35.0 vs PruneTIR 72.7/60.9/35.4; pruning costs 1.38x tokens so SC given 2 samples | Zhang et al. 2026 (d13) | [S] |
| Shared trajectory store | ALFWorld 47% to 55% (64.3% with reranker); WebArena 18% to 20%; full-index retrieval 0.298 vs task-type-matched 0.599 | MATM (d16) | [S] |

## 4. Mechanisms and models

Each model below is written so an engineer could build it.

### 4.1 Coupling test for an external store (Clark and Chalmers, adjusted)

Treat the store as part of the agent only when all hold.

1. **Available and invoked.** A tool `read_notes(query)` is in the loop every step. Log the read rate.
2. **Accessible.** Fetch cost is one call, with trimmed output (see 4.5).
3. **Trusted on retrieval.** The original says automatic endorsement. Our change: trust is conditional. Every note carries a timestamp and a source (tool output id, or "model claim"). On read, a note marked "model claim" or older than N steps is re-verified by code before an action depends on it. No study tested a read-time re-verification rule (critique GAP 2). Write-time verification has support (d08).
4. **Added by the agent.** Notes come from the agent's own earlier steps, or from code that ran its checks.

### 4.2 The two extension tests (Smart, Clowes, Clark 2025)

- **Redundancy test.** Run the item set with the store and with the store ablated. Split items by whether the bare model already knows the fact (probe closed-book first). The store only extends the agent where the ablated arm fails. Score the gain on "unknown" items, not on all items.
- **Agency test.** Two arms. Code decides when to read (fixed schedule or app-triggered) versus the model decides by a tool call. Compare accuracy and read count at equal tokens. The 2025 paper did not score either.

### 4.3 Epistemic action as tool call

Kirsh and Maglio's idea: when a sub-step is cheap to do in the world and costly to imagine, do it in the world. Engineering form: for each sub-step the router asks whether a tool computes it exactly (calculator, code run, table, sort). If yes, call it. Evidence: Toolformer maths (a18) and scratchpad (c14). The model's inner estimate is replaced by an exact external one.

### 4.4 Scratchpad (Nye 2021)

The model writes each intermediate state to the context before the final answer. For program execution the pad is the trace of variable states. Engineering: the program asks for a step-by-step state table, the model fills it, code reads only the last row. Count pad tokens against the budget (G7).

### 4.5 Tool interface (SWE-agent)

Concise, windowed output, a linter that rejects bad edits before they apply, and a small command set. The 10.7-point gain over a plain shell is the measured effect. Engineering: wrap every tool so output is capped, errors are short and specific, and malformed calls are rejected with a one-line reason.

### 4.6 Tiered memory (MemGPT, A-Mem, MERIT)

- **Main context:** the live prompt, fixed budget.
- **Archive:** key-value or vector store, searched by the model with a tool call.
- **Rules from MERIT and Xiong:** write only after a check passes; on update, overwrite the old value and keep a timestamp (append-only stores gave stale harm); fact store or summary beat raw retrieval on hard dependent tasks (retrieval 0.35 on D2 against 0.75 for fact store, small cells).
- **Replay** (full log in context) is the accuracy ceiling in MERIT but cost 2.7x tokens; overwriting stores match it.

### 4.7 Action log and loop guard (DeLoop)

Keep a visible list of past actions and results in the prompt. This cut repeated proposals to 3.3% from 48.8%. Do not rely on an exact-duplicate blocker: the model still proposed duplicates in 71.3% of tasks with it versus 69.8% without. Engineering: log plus a code check that a repeated (action, input) with the same output triggers the impasse state, not a silent block.

### 4.8 Reflection store (Reflexion)

On a failed attempt with a real signal (tests, environment reward), write a short lesson to memory and prepend it to the next attempt. Gain: +8% absolute over episodic memory alone. Without a signal reflections can mislead, which fits G2.

### 4.9 Skill library (Voyager)

When a sub-procedure passes its check, save it as named code with a description. Retrieve by description similarity. Voyager plateaus without it. Index by task type, not one flat index (MATM: 0.298 flat versus 0.599 matched).

### 4.10 Placement

Context position matters (c19). Engineering: put the key note first or last, or re-surface it by retrieval at the step where it is needed.

## 5. What holds up

### 5.1 Human offloading

- **Google effect: contested.** Original numbers confirmed in the text (a08-a10). The Camerer 2018 replication failed (pooled p=.4493). A 2020 Stroop replication reported no conclusive evidence, but only a snippet was seen (b03). Caveats: the original authors said the replication used outdated stimuli, and design differences exist (b02, critique 4). The 2024 meta-analysis supports effects on self-report and behaviour measures, but it pools heavy internet use studies, not the memory-for-saved-items design, and cognitive measurement is not significant. So it does not rescue Exp 2.
- **Brain drain: not supported overall.** Hartanto 2024: d=-0.02. Only OSPAN shows an effect and it is publication-biased. Boettger 2023 shows g=-0.14 but pools use and presence. Two direct replications found nothing (a15, b06, abstract only). A positive study (a16, N=42) is small. Hesselmann Stroop numbers were never found. A rival explanation in classroom data: separation anxiety (b09).
- **Offloading is guided by confidence** (a13) and is useful when memory is poor. This is the most solid human result, one study, N=363.
- **Skill and AI.** Three studies disagree in size. Shen and Tamkin d=0.738 (n=52); Maier N=704 no significant unaided deficit; Bastani about 1,000 students with a clear guardrail effect, but read from a summary. Consistent theme: mode of use matters. Delegation (asking for the answer) is worse than conceptual inquiry. A guarded tutor removed the exam penalty. Design lesson for human-facing modes only.
- **Cognitive debt.** 83.3% vs 11.1% failure to quote; 18 per group; preprint; a methodological comment was published.

### 5.2 LLM tools and memory

What held up across more than one source:

- **Scratchpad and thought search help** on tasks the model cannot do in one pass (c14, c20).
- **A persistent library of solved procedures helps** (Voyager, generative agents).
- **Tool interface design matters** (SWE-agent plus SWE-bench baseline).
- **Memory architectures cut tokens a lot** (A-Mem 1,200 vs 16,900; Terranova over 90% cut) and help on unanswerable questions.
- **When history fits, full context beats extracted notes on recall** (d11, d12).

What did not hold or is unreplicated:

- **ReAct alone does not beat CoT on multi-hop QA.** It cuts hallucination and adds new failure modes.
- **MemGPT and Cognitive Workspace**: no independent replication found. Rival-author tables put Letta near full-context on LoCoMo (74.0 vs 72.9, snippet only, d20).
- **Exact-duplicate blockers do not stop repeats** (d14).
- **Add-all memory** flattens or lowers success (d08).

### 5.3 Moderators and boundary conditions

- Reflection needs a reliable success signal.
- Retrieval must be matched to task type (MATM).
- Notes win when history is long (after about 10 turns at 100k) and lose on recall when it fits.
- Memory implementation can swing success by up to 60 points (MERIT), so "has memory" is not one condition.
- Agents act on a correctly retrieved value only 55% of the time in MERIT. Retrieval is not the bottleneck; use is.
- Region moderates the human brain-drain effect (Asia g=-0.39).

## 6. Language models

How models behave, what changed it, by how much. All numbers are from section 3.

- **Without tools, models are weak on exact tasks.** GPT-3 175B scored 14.8/6.3/15.0 on maths; Toolformer with a calculator 40.4/29.4/44.0, calculator used in 97.9% of items. Old models.
- **Write the working out.** A scratchpad more than doubles few-shot polynomial accuracy (8.8 to 20.1) and raises program execution from 11 to 26.5.
- **Interleaving thought and action** removed hallucination as a failure mode (CoT 56% of failures vs ReAct 0%) but ReAct's own failures are reasoning errors (47%) and empty search (23%). ReAct plus self-consistency was best (35.1 EM on HotpotQA with PaLM-540B).
- **A tool loop at matched tokens** roughly ties self-consistency on a small modern model (Qwen3-8B AIME25 60.9 vs 56.7; AIME24 72.7 vs 73.3). Not ReAct, not search.
- **Long context is used unevenly.** Middle position cut GPT-3.5 by over 20 points, below closed-book (c19). Fixed-context models fail nested lookups (0%); a paging agent with GPT-4 does not.
- **Stored notes mislead when wrong.** Stale entries raised harm by 0.25 in a hybrid store; add-all writing reduces success. Agents use a correct retrieved value only 55% of the time.
- **Loops.** Qwen3-8B repeats an identical call in 29.0% of tasks, 57.3% with compressed history. Gemini 3.1 Pro fails 48% of looping runs vs 12% loop-free; Qwen3-8B 85% vs 68%.
- **Weaker models use memory worse.** GPT-4 Turbo and GPT-3.5 still dropped at 2 nesting levels; the failure was too few lookups, not wrong lookups (c06).
- **Memory versus context.** GPT-5-mini long-context scored 92.85 on LoCoMo against 57.68 for extracted memory, and 82.40 vs 49.00 on LongMemEval. Memory is far cheaper and better on unanswerable items.
- **Philosophy on an LLM.** Smart et al. used gpt-3.5, one run, no scores. Nothing measures parity.
- **Weakness of the whole table.** Mostly authors' own benchmarks, 2022-2023 models, tokens rarely matched (critique). The 2026 papers (MERIT, DeLoop, Pollertlam, PruneTIR) are newer but small-model or pilot scale.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5.

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Offload exact sub-steps (arithmetic, tables, state traces) to a tool or written scratch; count the scratch tokens | O (externalise working state), S3/S4 | [E] | c14, c20, a18, a19 |
| Keep a persistent skill and solved-procedure library, written only after a check passes | memory | [E] | b20, c11, c12, c07, d16, d08 |
| Wrap tools: capped, trimmed output, short specific errors, reject malformed calls | G | [E] | c15, c16, c17 |
| When history is long, keep short notes plus a searchable raw log; do not rely on notes alone when the whole history fits | memory | [E] | d11, d12, c18 |
| Place key notes first or last in the prompt, or re-surface them at the step that needs them (low cost; one 2023 study) | memory | [S] adopt as default | c19 |
| Do not use human offloading findings (Google effect, brain drain) as design inputs | none | [E] that they are unsettled | d01, d02, d03, b02 |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Overwrite on update and timestamp every note, versus append-only | memory | [S] | d09, d10 |
| Write-gate: store a note only when a checker or test has passed | G, memory | [S] | d08 |
| Read-time re-verification of old or "model claim" notes before they drive an action (our replacement for automatic endorsement) | G, memory | [S] untested | a03, d06-d10 |
| Action log in the prompt, a repeat triggers the impasse state, not a silent block | G, S6 | [S] | d14, d15, b18 |
| Reflection note stored after a failed attempt with a real signal | O, memory | [S] | b19, c10 |
| Tool loop plus self-consistency versus self-consistency alone at equal tokens | S3/S4 | [S] | a20, b18, d13 |
| Redundancy test: score store gain only on items the bare model fails | memory design | [S] conceptual | d06, d07 |
| Agency test: model-decided reads versus code-scheduled reads | memory design | [S] conceptual | d06, d07 |
| Task-type indexing of the library versus a flat index | memory | [S] | d16 |
| Paged memory with search tool versus fixed context on long histories | memory | [S] | a23, a24, c05, d20 |
| Questions about the agent's own earlier output with notes hidden (guards against hollow offloading) | G | [C] | a26, b10, b11 |

## 8. Concrete tests on our bench

All arms at equal total tokens, with notes, setup and tool-call tokens counted (G7). Run 3 seeds where cost allows. Report tokens per arm beside the metric.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-step arithmetic and state-trace items | scratch/tool on vs in-head | accuracy per token | scratch wins; Nye saw 8.8 to 20.1 on an old model, a modern model may show less |
| T2 | Checkable items, stream of 30+ tasks | write-gate vs write-all vs no notes | success over the stream | gate keeps rising; write-all flat (d08) |
| T3 | Same stream with 20% injected stale or wrong notes | trust notes vs read-time re-verification vs no notes | wrong-action rate and accuracy | re-verification cuts wrong actions; token cost measured |
| T4 | Long histories (20+ turns) with unanswerable items | full context vs short notes plus raw log search | accuracy, correct abstention on unanswerable, tokens | full context ahead on recall; notes ahead on unanswerable and on tokens past about 10 turns |
| T5 | Multi-hop QA with a search tool | CoT vs tool loop vs CoT-SC vs tool loop plus SC | accuracy | hybrid best; tool loop alone near CoT (a20) |
| T6 | Tool-heavy tasks | raw tool output vs trimmed and linted output | accuracy, tokens | several points gain (SWE-agent 10.7) |
| T7 | Multi-step tasks prone to loops | no log vs action log vs log plus duplicate blocker | repeat rate, accuracy | log cuts repeats (3.3% vs 48.8%); blocker adds nothing |
| T8 | Items split into known and unknown to the bare model | store ablated vs store on | accuracy on each split | gain only on unknown items (redundancy) |
| T9 | Same items | code-scheduled reads vs model-decided reads | accuracy, read count | unknown; tests the agency condition |
| T10 | Repeated task families | flat index vs task-type index vs no library | accuracy on later tasks | type-matched about 2x flat success (0.599 vs 0.298 in d16) |
| T11 | Failed attempts with a test signal | retry vs retry plus stored reflection | pass rate | about +8 points (b19) |
| T12 | Questions on the agent's own earlier output | notes visible vs hidden | accuracy | measures hollow offloading; no strong prior |

## 9. What does not transfer, and why

- **Phone presence and brain drain.** Pooled effect about zero, and no mechanism that maps to a model (K16).
- **Google effect.** Contested in humans, and a model has no feeling that it can look something up later. Measure agent recall directly instead (K15).
- **Cognitive self-esteem, separation anxiety, EEG engagement.** Human states.
- **Tetris timings.** Three players, a game with no hidden state. Use the principle (exact external beats inner estimate), not the numbers.
- **Parity and constitution.** The philosophical dispute is about what counts as belief. For our agent the only question is whether the store improves results at equal tokens.
- **Automatic endorsement.** Fine for Otto, whose notebook he wrote carefully. Wrong for an agent, whose notes may be stale or a model claim.
- **Human skill-loss studies.** They concern learners. Use them only as a design caution for any human-facing mode.
- **Cohen's d from Cognitive Workspace.** 195.66 comes from a bookkeeping count over 8 documents.
- **Author benchmarks on old models.** MemGPT's 92.5% and EMT's lead may shrink on current models, where context is longer and notes lose on recall (d11).

## 10. Open questions

1. At equal total tokens, does a persistent notes file plus search beat full context on multi-step reasoning with a 2025-2026 model? No clean test (GAP 1).
2. How much does read-time re-verification cut stale-note errors, and at what token cost? Not tested anywhere (GAP 2).
3. Does a trimmed, linted tool interface help on non-code reasoning? Only code results exist (GAP 3).
4. Is there a formal, testable criterion for when LLM plus store is extended, and what do Adams and Aizawa or Rupert predict instead? Smart et al. give two tests but no scores (GAP 5).
5. Does ReAct plus self-consistency still beat plain self-consistency on modern models at matched tokens? Only a pruned tool loop on a small math model was matched (GAP 6).
6. Does the Bastani 2025 guardrail effect replicate, and what are its standard errors? Only a summary was read (GAP 7).
7. Are MemGPT and Cognitive Workspace gains independent of the authors' benchmarks? (GAP 8)
8. What is the token cost of a loop guard? (GAP 9)
9. Do Hutchins and Wegner give numbers that apply to multi-agent LLM setups? MATM (d16) is the only multi-agent memory result found (GAP 10).
10. The Hesselmann Stroop replication numbers and the Parry and four-level meta-analyses were not read in full.

## 11. Sources

[V] opened, [M] snippet or abstract only.

- [V] Clark and Chalmers (1998) The Extended Mind. https://consc.net/papers/extended.html (a01-a04)
- [M] Clark and Chalmers (1998), Analysis 58:7. https://doi.org/10.1093/analys/58.1.7 (b22)
- [V] Kirsh and Maglio (1994) Epistemic and pragmatic action. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/Distinguishin (a05-a07; URL as truncated in evidence file)
- [V] Sparrow, Liu, Wegner (2011) Google effects on memory. https://dtg.sites.fas.harvard.edu/DANWEGNER/pub/Sparrow%20et%20al.%202 (a08-a10); [M] https://doi.org/10.1126/science.1207745 (b01)
- [V] Camerer et al. (2018) https://osf.io/download/4hmb6/ (a11); [V] atlas page https://forrt.org/flora-replication-atlas/doi/10.1126/science.1207745/ (b02, b25)
- [M] Hesselmann (2020) https://peerj.com/articles/10325 (b03)
- [V] Gong and Yang (2024) Google effects meta-analysis, Frontiers in Public Health (a12, b04); URL as recorded in evidence_a and evidence_b
- [V] Boldt and Gilbert (2019) https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/ (a13; URL as truncated)
- [M] Ward et al. (2017) https://doi.org/10.1086/691462 (b05); read secondhand in Skowronek 2023 (a14)
- [V, secondary] Skowronek, Seifert, Lindberg (2023) https://www.nature.com/articles/s41598-023-36256-4.pdf (a14-a16)
- [M] Ruiz Pardo and Minda (2022) replication, Acta Psychologica https://doi.org/10.1016/j.actpsy.2022.103717 (b06)
- [M] Boettger meta-analysis abstract https://doi.org/10.3390/bs13090751 (b07); [V] full text https://pmc.ncbi.nlm.nih.gov/articles/PMC10525686/ (d03)
- [M] Four-level meta-analysis title https://doi.org/10.1037/tmb0000123 (b08); [V] Hartanto et al. (2024) https://researchonline.jcu.edu.au/91280/1/2024-31279-001.pdf (d01, d02)
- [M] High-school classroom study https://doi.org/10.5817/cp2025-4-1 (b09); [M] Parry summary https://pubmed.ncbi.nlm.nih.gov/36007374/ (d04)
- [M] Risko and Gilbert (2016) https://doi.org/10.1016/j.tics.2016.07.002 (a17, b23); [M] Storm and Stone (2015) https://doi.org/10.1177/0956797614563338 (b24)
- [V] Kosmyna et al. (2025) https://arxiv.org/abs/2506.08872 (a26, b10); [V] Stankovic et al. (2026) https://arxiv.org/abs/2601.00856 (b11)
- [V] Maier et al. (2026) https://arxiv.org/abs/2609.20143 (b12); [V] Shen and Tamkin (2026) https://arxiv.org/abs/2601.20245 (b13)
- [M] Bastani et al. (2025) PNAS https://doi.org/10.1073/pnas.2422633122 (b14); [V, summary page only] https://knowledge.wharton.upenn.edu/article/without-guardrails-generat (d05; URL as truncated)
- [V] Schick et al. (2023) Toolformer https://arxiv.org/abs/2302.04761
- [V] Yao et al. (2022) ReAct https://arxiv.org/abs/2210.03629
- [V] Packer et al. (2023) MemGPT https://arxiv.org/abs/2310.08560
- [V] Graves, Wayne, Danihelka (2014) Neural Turing Machines https://arxiv.org/pdf/1410.5401
- [V] Klett and Ahle (2024) Extended Mind Transformers https://arxiv.org/abs/2406.02332
- [V] An (2025) Cognitive Workspace https://arxiv.org/abs/2508.13171
- [V] Shinn et al. (2023) Reflexion https://arxiv.org/abs/2303.11366
- [V] Wang et al. (2023) Voyager https://arxiv.org/abs/2305.16291
- [V] Park et al. (2023) Generative Agents https://arxiv.org/abs/2304.03442
- [V] Nye et al. (2021) Scratchpads https://arxiv.org/abs/2112.00114
- [V] Yang et al. (2024) SWE-agent https://arxiv.org/abs/2405.15793; [V] Jimenez et al. (2024) SWE-bench https://arxiv.org/abs/2310.06770
- [V] Xu et al. (2025) A-Mem https://arxiv.org/abs/2502.12110
- [V] Liu et al. (2023) Lost in the Middle https://arxiv.org/abs/2307.03172
- [V] Yao et al. (2023) Tree of Thoughts https://arxiv.org/abs/2305.10601
- [V] Zhou et al. (2026) Externalization in LLM Agents https://arxiv.org/abs/2604.08224
- [V] Smart, Clowes, Clark (2025) Synthese https://link.springer.com/content/pdf/10.1007/s11229-025-05046-y.pdf (d06, d07); [M] https://eprints.soton.ac.uk/502110/1/s11229-025-05046-y.pdf (c23)
- [M] Clark (2025) Nature Communications https://www.nature.com/articles/s41467-024-46048-z (c25)
- [M] Normal Computing blog (2023) https://normalcomputing.com/blog-posts/supersizing-transformers-going- (c24; URL as truncated)
- [V] Xiong et al. (2025) https://arxiv.org/pdf/2505.16067 (d08)
- [V] Mishra and Mishra (2026) MERIT https://arxiv.org/pdf/2609.05441 (d09, d10)
- [V] Pollertlam and Kornsuwannawit (2026) https://arxiv.org/pdf/2603.04814 (d11)
- [V] Terranova, Ross, Birch (2025) https://arxiv.org/pdf/2510.23730 (d12)
- [V] Zhang et al. (2026) PruneTIR https://arxiv.org/pdf/2605.09931 (d13)
- [V] Chen et al. (2026) DeLoop https://arxiv.org/pdf/2610.19376 (d14, d15)
- [V] Kim et al. (2026) MATM https://arxiv.org/pdf/2606.19911 (d16)
- [V, first page only] Perrier (2025) https://arxiv.org/pdf/2510.16193 (d17)
- [M] Baek and Pradel (2026) https://arxiv.org/pdf/2602.10046 (d18); [M] Wang et al. (2024) budget-aware evaluation https://arxiv.org/abs/2406.06461 (d19); [M] Mnemon, Memanto, MemUse rival-author tables https://arxiv.org/pdf/2609.36059 (d20)
- [M] Hutchins (1995) https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/ (a27); [M] Wegner (1987) https://doi.org/10.1007/978-1-4612-4634-3_9 (a28); [M] Adams and Aizawa (2001) and Rupert (2004) https://doi.org/10.1111/j.1747-9991.2008.00126.x (a29)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 5 established claims: 4 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D06.09-K23** (reworded: the sources support less). Numbers verified, but Terranova et al. report memory methods are competitive or superior to full context on LoCoMo (GPT-4o-mini A-Mem average F1 rank 1.80 vs full context 3.40; Qwen too), so 'do not beat full context on factual recall' holds only for the Mem0 system in Pollertlam et al. and for Llama; the 90% token saving is from Terranova's A-Mem, not Mem0. Corrected claim: On LoCoMo, a Mem0-style fact memory scored 57.68 vs 92.85 for full long context with GPT-5-mini (Pollertlam et al.), but in a separate study (Terranova et al.) memory methods using over 90% fewer tokens were competitive with or better than full context for some models (GPT-4o-mini A-Mem average-F1 rank 1.80 vs 3.40 for full context) and much better on adversarial questions (77.64 vs 52.94); Pollertlam et al. find memory cheaper after about 10 turns at 100k context.
