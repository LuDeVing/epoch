# Language agents as architectures: deep document

Scope: what happens when Soar and ACT-R parts are mapped onto LLM agents, and what the measured evidence says about each part. Key work: Fan and Lan (2026), arXiv 2607.23942. Evidence ids (a01-a28, b01-b27, c01-c25, d01-d20) and claim ids (C02.10-K01 to K22) refer to the files in this folder. Corrections from critique.md are applied: the Reflexion 77.1 vs 80.1 pair is MBPP Python (Leetcode Hard Python is 7.5 vs 15.0), and the Huang et al. oracle numbers are the corrected ones below.

Overlap notes: impasse-driven subgoaling and chunking are covered in depth in sibling subfields 01_soar_operator_selection_and_impasses and 03_soar_chunking, and in parallel runs (Impasse-driven subgoaling and chunking; Sampling and voting; Heuristic search; Metacognition and control). Here they appear only as mapping targets and as agent-side measurements.

## 1. What it is

Two older lines meet here.

1. Cognitive architectures (Soar, ACT-R and others) are fixed programs that hold memory, a decision cycle and learning. Their mechanisms are coupled: memory access, action choice, failure handling and learning feed each other.
2. LLM agents (ReAct, Reflexion, Voyager, MemGPT, Generative Agents, Tree of Thoughts) wrap a stateless model with memory, planning, reflection and tools.

The subfield asks: which architecture parts have been copied into agents, which have not, and does copying a part help?

The key paper is Fan and Lan (2026) [b01, a01, c01]. It maps 10 historical architectures (ACT-R, Soar, CLARION, LIDA, Hearsay-II, BDI, MIDCA, ICARUS, EPIC, Sigma) to 8 agent runtime families and 42 mechanism-focused systems. It is a review. It makes no performance claim and no completeness claim [b01]. The coding was two passes by the same authors with no second coder [a24, c05].

Why it matters to us: our schema is a thinking scaffold where code decides and the model fills slots. This is the split the review proposes. The review is a design checklist, not proof that any part helps. The measured evidence lives in the agent papers it cites. Most of those were not designed as tests of an architecture idea.

## 2. History and theories in depth

### 2.1 Founding architectures
- Newell (1990), Unified Theories of Cognition: one architecture should embody a theory of cognition. Soar was built to test it [a26]. Known only through citations here (not opened).
- Soar decision cycle (Laird 2022) [a10]: elaboration, operator proposal, selection by preferences, application. Three impasse types: state no-change, operator tie or conflict, operator no-change. An impasse makes a substate with local reasoning. Results return to the superstate.
- Chunking [a11]: whenever a substate makes a result, Soar traces which superstate structures it depended on and writes a rule. Slow sequential reasoning becomes fast rule firing. Laird says overhead is small. The source we read gives no numbers. The 1986 paper [a27] and Assanie (2022) were not read.
- Soar hypothesis [a12]: knowledge is mostly symbolic, with numeric metadata biasing retrieval and learning.
- ACT-R (Anderson 2004) [a28, not opened]: memory activation sets retrieval accessibility and latency. Production utility sets action value [a04, c02]. We lack the activation equation and fit numbers (see UNKNOWNS.md).
- Common Model of Cognition extension (Laird et al. 2025) [c23]: substate mechanisms exist in Soar and Sigma but not ACT-R. Metacognition is proposed as reasoning over explicit representations of the agent's own cognition.

### 2.2 Bridge papers
- CoALA (Sumers, Yao, Narasimhan, Griffiths 2023/24) [b07, a06-a09, c06]. An LLM is a probabilistic production system over strings. Memory: working, episodic, semantic, procedural. Action space: external grounding plus internal retrieval, reasoning, learning. Decision cycle: planning (propose, evaluate, select) then execution. Learning is a chosen action. Procedural-memory writes are flagged as riskier than episodic or semantic writes [a09]. LLMs are stateless, so every memory is written outside the model [b08]. It tests nothing. It is a taxonomy.
- Wray, Kirk, Laird (2025) cognitive design patterns [b24, a22, a23]: observe-decide-act, commitment and reconsideration, memory, knowledge compilation. They say ReAct lacks an explicit commitment step and ask whether adding one helps. No experiment.
- Kirk, Wray, Laird (2023) [a20, c07]: use the LLM as a knowledge source that the architecture queries and checks. Three integration patterns.

### 2.3 The 2026 mechanism-level review
Coding scheme [b01, a01]:
- Evidence relation: E1 source cites lineage; E2 implemented structure; E3 comparable control with a different build; E4 convergence without transfer.
- Migration depth: D0 concept; D1 interface; D2 explicit state; D3 trigger runs the control step by itself; D4 outcomes update future control policy.

Four equivalence tests stop shallow mappings [b02]. A message bus is not a global workspace. A checkpoint is not a Soar impasse substate. A handoff is not BDI commitment. A guardrail is not MIDCA diagnosis.

Findings:
- Modern agents copied much of the memory, planning and reflection substrate [a01].
- Six candidate gaps. One closed (skill governance, B5): GraSP already has calibrated skill choice, node verification, bounded repair and replanning, rated E3/D4. Five residual bundles remain [b03, a02, c04]:
  1. Activation + latency + utility in one law (ACT-R). Adaptive memory systems (AgeMem, Memory-R1, MemCon, DeltaMem, A-MAC, CURATOR) reach E3/D4 by learning memory operations from outcomes. None joins the three [b04, a04, c02].
  2. Typed impasse + isolated substate + typed return + compiling the resolution (Soar). PALADIN and AgentDebugX (error typing, E3/D3), Shepherd (reversible branches, E2/D3), Reflexion and AgentHER (learn from failure, E3/D4) each cover a piece [b05, a03, c03].
  3. Bounded content competition with broadcast (global workspace style).
  4. Persistent intention with reconsideration (BDI).
  5. Uncertainty with resource allocation and stopping.
- Three limits on migration [a05]: runtimes split state, tools and memory across interfaces, so couplings break. LLM-written summaries and reflections have unstable meaning, unlike typed chunks. Evaluation rewards local capability, not cross-component invariants.
- Formalism [b06]: durable state x=(intention, workspace, memory, skills, uncertainty, budget, failure substate). p_t = LLM(w,i,q); a_t = G(x_t,p_t). The model proposes. An external governor G picks the transition. Current runtimes leave G implicit in code or hand it to another model call.
- Authors' admitted limits [c05, a24]: no second coder, no comparison of residual bundles against D3/D4 baselines, no search-recall estimate, 0 experiments on the 5 bundles. Corpus frozen 26 Jul 2026. "Residual" means not found composed in the corpus. It does not mean shown to matter.

### 2.4 Soar-group LLM work
STARS (Kirk, Wray, Lindes, Laird 2024) [b23], Wray et al. problem specifications (2024) [b25], and NL2GenSym (2025) [b26, b27, c10, c11] use an LLM inside or beside a real cognitive architecture. They are the closest direct tests of "LLM proposes, architecture checks". Each comes from one group, on small custom benchmarks.

## 3. Core findings with exact numbers

Status: E established (3+ independent sources or replicated), S single-source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Review maps old architectures to agents; 5 residual coupling bundles | 10 architectures, 8 runtime families, 42 systems; 6 gaps, 1 closed, 5 open; 0 experiments, 0 second coders | Fan and Lan 2026 [b01-b03, c05] | S (one coder, no test) |
| Thought-then-act beats act-only on state tracking | ALFWorld best ReAct 71% vs Act 45% vs BUTLER 37%; worst ReAct trial 48%; relative gain 33-90%, mean 62% (6 trials, PaLM-540B); WebShop +10 abs | ReAct [b09, a13] | S |
| ReAct is not best on knowledge QA | HotpotQA EM: CoT 29.4, ReAct 27.4, CoT-SC 33.4, CoT-SC->ReAct 34.2, ReAct->CoT-SC 35.1; FEVER: ReAct 60.9, CoT-SC->ReAct 64.6 | ReAct [b10] | S (K16) |
| Reflection helps with a reliable external signal | Reflexion ALFWorld 130/134 over 12 trials; +22 ALFWorld, +20 HotPotQA, +11 HumanEval; HumanEval Python 80.1 to 91.0 | Reflexion [b11, a14] | E for the rule (K02) |
| Reflection fails with a weak signal | MBPP Python 80.1 to 77.1; test false-positive 16.3% (MBPP) vs 1.4% (HumanEval); Rust no test generation 52% vs base 60% vs full 68%; Leetcode Hard Python 7.5 to 15.0 | Reflexion [a14, c13] | S (K09) |
| Intrinsic self-correction lowers accuracy (2023-24 models) | GPT-3.5 CSQA 75.8 to 38.1 (one round) to 41.8; GSM8K 75.9 to 75.1 to 74.7; HotpotQA 26.0 to 25.0; GPT-4 GSM8K 95.5 to 91.5 to 89.0; HotpotQA 49 to 49 to 43; 74.7% unchanged on GSM8K | Huang et al. [b13, b14, c14] | E (K03) |
| Oracle labels give the gain | GPT-3.5 standard/oracle: GSM8K 75.9/84.3, CSQA 75.8/89.7, HotpotQA 26.0/29.0. GPT-4: 95.5/97.5, 82.0/85.5, 49.0/59.0 (corrected, critique item 2) | Huang et al. Table 2 [b13, c15] | E |
| Self-critique worse than a sound verifier | GPT-4, 100 instances: Game of 24 standard/self-critique/sound verifier 5/3/38; Graph coloring 16/2/37; Blocksworld 40/55/87; Mystery BW 4/0/8. LLM verifier FP/FN: G24 10.4/20.7; coloring 6.5/95.8; BW 18.55/15.48; Mystery BW 0.5/97.09 | Stechly et al. [d01] | E (independent replication) |
| Self-Refine gives about 0 on math | GPT-3.5 64.1 to 64.1; ChatGPT 74.8 to 75.0; GPT-4 92.9 to 93.1; "looks good" on 94% of ChatGPT instances; oracle trigger 68.9/76.2/93.8. Soft tasks: sentiment GPT-4 3.8 to 36.2; code optimisation 27.3 to 36.0 | Madaan et al. [d08] | S |
| Tool feedback beats a no-tool loop | ChatGPT HotpotQA F1 52.9 vs 46.1; AmbigNQ 74.9 vs 67.3; GSM8K 78.2 vs 77.0; TabMWP 89.0 vs 87.0 | CRITIC [d09] | S |
| Survey: no prompted-LLM self-correction without external feedback | Qualitative; fine-tuning methods use 20K-274K instances | Kamoi et al. [b15, d02] | S (not independent measurement) |
| Finding the first wrong step is the bottleneck | BIG-Bench Mistake, 2,186 traces: GPT-4 direct step 52.87, CoT step 43.40, GPT-3.5 14.31. Oracle location on wrong traces +18.04 to +43.92; on right traces 0 to -11.43. Break-even about 60-70% (simulation, read from figure) | Tyen et al. [d03] | S (K18) |
| Blind spot on non-reasoning models; small on reasoning models | 14 models: 64.5% blind spot; own errors caught 4.3-10.8%; "Wait" cuts blind spot 89.3%; DeepSeek-V3-0324 0.567 to 0.902; R1-0528 0.908 | Tsui [d05] | S (K17) |
| Reflection words do not imply accuracy | Nearly half of reflective R1-Zero answers no more accurate; Dr. GRPO 7B AIME24 43.3 | Liu et al. [d06] | S |
| Prompt-only self-correction fails; RL fixes it | MATH Gemini 1.5 Flash delta: base -11.2; Self-Refine -1.0; STaR +0.4; Pair-SFT +1.8; SCoRe +4.4; correct-to-incorrect 15.8% vs 1.4% | SCoRe [d07] | S (needs training) |
| Bounded "Wait" continuation | s1-32B AIME24 50.0 to 56.7 (4x Wait; 53.3 with 2x); MATH500 92.6 to 93.0; GPQA 56.6 to 59.6; AIME24 has 30 items (1 item = 3.3 pts) | s1 [d16] | S (K15, K17) |
| LLM as checked knowledge source | STARS completion 77.5/94.4/92.9% vs template 52.5/66.7/35.7%; 100% with oversight; over 70% of raw responses not viable in one task | STARS, Kirk et al. [b23, a20] | E (K05; 3 sources, one group) |
| Execution-grounded critic is the key part | NL2GenSym: Gemini-2.5 one-shot 55 vs framework 86; qwen-max 66 vs 91; manual rules 84; zero-shot 0; remove critic -23% overall, -37% hard; remove basic KB -17%; remove case KB -14% | NL2GenSym [b26, b27, c10, c11] | C (K12; one group) |
| Specs without search control cost orders of magnitude more steps | Qualitative, preliminary | Wray et al. 2024 [b25] | C |
| Skill library of verified code | Voyager: 63 unique items in 160 iterations, 3.3x; wooden/stone/iron 15.3x/8.5x/6.4x faster; map 2.3x; only agent to reach diamond. Ablations: random curriculum -93%; no self-verification -73%; GPT-3.5 coder gives 5.7x fewer items; no skill library plateaus | Voyager [b17, b18, a16, c16, c17] | E in K06 (with AWM, ExpeL, Zhu); baselines re-interpreted, 3 runs |
| Workflow induction | AWM: WebArena +12.0 points (+51.1% relative); +7.6% relative over SteP; Mind2Web cross-task +24.6% relative | AWM [c18] | S |
| Training-free experience reuse | ExpeL: HotpotQA 28.0 to 39.0; ALFWorld 40.0 to 59.0; retrieval by task similarity 59.0, reasoning similarity 48.5, random 42.5; insights-only 36/50; retrieve-only 31/55; HotpotQA to FEVER 63 to 70 | ExpeL [d19] | S |
| Rule bootstrapping cuts LLM calls | Zhu and Simmons: find 14/15 vs 15/15; steps not different (p=0.446, 0.347); test cost about $120 vs under $40 (token columns garbled) | [a21] | S (K07) |
| Memory stream + reflection + planning raises believability | TrueSkill mu: 29.89 full; 26.88 no reflection; 25.64 no reflection/planning; 22.95 crowdworker; 21.21 none; d=8.16; Kruskal-Wallis chi2(4)=150.29, p<0.001; 100 raters | Generative Agents [b16, a15, c19] | S (not task success) |
| Paged memory beats truncation | DMR: GPT-3.5 38.7 to 66.9; GPT-4 32.1 to 92.5; GPT-4 Turbo 35.3 to 93.4 | MemGPT [b19, a18, c20] | S (self-built benchmark) |
| Independent memory benchmark | Long context best (GPT-5-mini 60.6; worst Cognee 20.6); accurate retrieval GPT-5-mini 74.4, HippoRAG-v2 65.1, BM25 60.5, Qwen3-Embedding-4B 54.7; selective forgetting all at most 28% | MemoryAgentBench [d17] | S |
| Extracted memory vs full context | LLM-judge J: full 72.90; Mem0g 68.44; Mem0 66.88; Zep 65.99; best RAG 60.97; OpenAI memory 52.90; A-Mem 48.38. Tokens/query 26,031 vs 1,764; p95 latency 17.1 s vs 1.44 s | Mem0 [d18] | S (vendor) |
| Search over thoughts on puzzles | Game of 24, GPT-4: IO 7.3, CoT about 4, CoT-SC k=100 9.0, ToT b=1 45, b=5 74 | ToT [b20, a17] | S |
| Search loses at matched budget outside puzzles | Cap 20 queries or 10k tokens, 100 questions x 6 datasets: SC regularly beats Reflexion, debate, ToT; Reflexion worst of three. G24 GPT-4 ToT b=5 0.74 ($159.87), b=1 0.65 ($49.9), CoT x100 top-1 0.17 | Wang et al. budget-aware [d10] | C (K08) |
| MCTS vs sampling at equal FLOPs | MATH500 weighted vote: Mistral-7B REBASE 45.0 at 1.36e14 vs sampling 42.8 at 8.70e14; Llemma-34B 49.2 at 7.08e14 vs 46.7 at 12.1e14; MCTS under-performs sampling | Wu et al. [d13] | S |
| LATS | HumanEval GPT-4 92.7 (Reflexion 91.0, base 80.1); GPT-3.5 83.8 vs Reflexion 68.1; HotpotQA GPT-3.5 0.63 vs ReAct 0.32; no LM value -0.26, no reflection -0.05, DFS 0.42; tokens on success LATS 173,290 vs ToT 210,215; WebShop 75.9 | LATS [b21, d11] | S (no best-of-N at equal tokens) |
| Web tree search | VisualWebArena GPT-4o 18.9 to 26.4; Llama-3-70B 7.6 to 16.7; WebArena 15.0 to 19.2; budget c=0/5/20: 24.5/32.0/37.0; value fn GPT-4o 1/5/20 samples 28.5/32.5/37.0, ground truth 43.5; reranking plateaus about 30; up to 20x calls | Koh et al. [d12] | S (K22) |
| Selection is the bottleneck | MATH Llama-3-8B coverage 82.9% at 100 to 98.44% at 10,000 samples; majority vote and reward model 40.50 to 41.41; SWE-bench Lite 15.9% to 56% at 250 samples | Large Language Monkeys [d15] | S (K19) |
| Difficulty-aware compute | MATH PaLM 2-S*: 64 compute-optimal revisions match 256 best-of-N; PRM search 16 match 64; beam worse than best-of-N on levels 1-2 at large budgets | Snell et al. [d14] | S (K20) |
| Planning abilities of plain LLMs (old) | About 3% of plans executable; human blocksworld 39/50 valid | Valmeekam et al. [b22] | S (old models) |
| ACT-R trace injection by fine-tuning | Accuracy 0.6576 vs 0.3564 (NLL 0.6534 vs 1.1330; chance 0.4826); multi-facet 0.42; concatenation 0.71 vs 0.71 | LLM-ACTR [c08, c09] | S (K13, fine-tuning) |
| Learned memory and agent design | Memory-R1: +28% F1 vs Mem0 (LLaMA-3.1-8B), 152 training pairs; ADAS: DROP +13.6 F1, MGSM +14.4%, GSM8K transfer +25.9% | [c21, c22] | S (needs training; K14) |

## 4. Mechanisms and models

Each item says what the part does in the old architecture, how an agent builds it, and what is measured. The program (code) holds state and picks transitions. The model fills slots [b06].

### 4.1 Decision cycle with a governor
- State record x = (intention, workspace, memory, skills, uncertainty, budget, failure substate).
- Loop: the model proposes candidate actions or answers. Code applies rules: validity, preference, budget. Code selects. The model applies the chosen operator. Code checks the result. This is the Soar cycle (propose, select, apply) with the LLM in the proposal and application slots. It also matches CoALA's three planning stages [a08].
- Evaluation can be a heuristic, an LLM value, a learned value, or LLM votes [a08]. Measured: removing the LM value in LATS costs 0.26 on HotpotQA [d11]. A ground-truth value beats a 20-sample GPT-4o value by 6.5 points on web tasks [d12]. Evaluator quality caps the gain.

### 4.2 Typed impasse and scoped substate (built by no one as a whole)
Implementation sketch:
1. Detector in code. Three types, copied from Soar [a10]: no candidate (state no-change); tie or conflict among candidates; the chosen operator makes no progress (operator no-change). Agent equivalents: an empty proposal list; disagreeing samples or equal scores; the check fails twice with the same output.
2. On an impasse, open a child record with its own small context: the parent goal, the failing output, the impasse type. Call the model with only that context. Do not share the parent's whole history.
3. Return a typed result (a candidate, a ranking, a counter-example, or "none"), not free text. Code merges it.
4. Compile: if the result was verified by a check, store it with the conditions it depended on (see 4.4).

Status: pieces exist (error typing, reversible branches, learn-from-failure [b05]). The full chain is untested. The nearest equal-budget evidence is that self-consistency beats Reflexion, debate and ToT at 20 queries [d10]. So the baseline to beat is voting, not retry.

### 4.3 Reflection as episodic memory plus learning
Reflexion [b11]: after a failed trial, the model writes a short verbal lesson. The last 3 are kept and prepended to the next trial. Trigger: a success signal or heuristic. Implementation: keep lessons one line each; trigger only when a check fails; log the check's false-positive rate. Rule from data: reflection helps when the signal is external and reliable (ALFWorld environment state; HumanEval tests with 1.4% false positives). It hurts when it is not (MBPP 16.3% false positives; Rust without test generation) [a14, c13].

### 4.4 Chunking analogue: compile verified results
Soar traces dependencies and writes a rule. Agent versions:
- Voyager: store verified code as a skill, indexed by description, retrieved by similarity [b17].
- AWM: induce workflows from successful trajectories [c18].
- ExpeL: extract insights and keep successful trajectories, retrieved by task similarity [d19].
- Zhu and Simmons: when no production applies, ask the LLM for an action and a rule. Later runs fire the rule with no LLM call [a21].

Implementation: store (problem class, conditions of reuse, solution, check that passed). Offer by similarity. Re-run the check on reuse. Risk: procedural writes can add bugs [a09], and LLM-written summaries have unstable meaning, unlike typed chunks [a05]. Write only after a code check passes.

### 4.5 ACT-R style memory scoring
ACT-R base-level activation rises with frequency and recency and falls with time. Retrieval latency falls with activation. Production utility is learned from reward [a04]. Generative Agents use a rough analogue: score = recency + importance + relevance [a15]. Implementation: score each memory item by recency, use count, similarity and cost; retrieve top k within a token cap. Evidence of a gain over plain similarity or BM25 is absent [d17, d18]. We did not read the activation equation itself.

### 4.6 Tiered memory
MemGPT: a small main context plus recall and archival stores. The model issues function calls to page items [b19]. This is a few tools (search, write, evict). The gain is against truncation. Against long context, memory systems lose when everything fits [d17]. Extracted memory trades about 6 judge points for about 15x fewer tokens [d18].

### 4.7 Commitment and reconsideration
Persistent intention, dropped only on a defined trigger (a check failure, a budget breach, a new observation that contradicts a premise). The Soar group says ReAct lacks this [a22]. No equal-token test exists.

### 4.8 Search control
Tree search needs an evaluator and a stopping rule. Wray 2024: specs listing operators but omitting search control cost orders of magnitude more steps [b25]. The prompt-scaffold analogue is untested.

### 4.9 Resource allocation and stopping
Spend by difficulty [d14]. Stop on a budget or when the check passes. Bounded "Wait" continuation flattens after about 4 [d16].

## 5. What holds up

### 5.1 Replicated or multi-source
- External signal needed for correction (K02): Huang [b13], Kamoi [b15, d02], Stechly [d01], CRITIC [d09], Reflexion ablation [c13], Tyen [d03], SCoRe [d07], Self-Refine [d08]. This is the most solid result in the folder.
- Intrinsic self-correction hurts 2023-24 models (K03): Huang, Stechly and Kumar independently.
- A checked LLM knowledge source beats an unchecked one (K05).
- Compiled verified solutions help where an executable check exists (K06): Voyager, AWM, ExpeL, Zhu. These are different tasks and none counts total tokens.

### 5.2 Failures, contradictions, weak spots
- Reflexion wins (+22, +20, +11) but loses on MBPP Python. Huang says intrinsic correction fails. The reconciliation is "reliable external signal". But Reflexion's HotpotQA setup used ground-truth correctness, so part of that gain is an oracle gain.
- The oracle gain is modest for GPT-3.5 (+8.4 GSM8K, +3.0 HotpotQA) and +2.0 / +10.0 for GPT-4 (corrected b13).
- Kamoi is a survey, not independent measurement beyond Huang.
- Kirk, Wray, Laird papers share authors. STARS and the Wray results are one group. NL2GenSym is one group on its own benchmark.
- Fan and Lan: one preprint, one coder, no experiment. All gaps are hypotheses.
- Generative Agents and MemGPT measure believability and a self-built retrieval task, not reasoning gain.
- Voyager baselines were re-interpreted by the authors; 3 runs each.
- Zhu and Simmons token column is garbled; only the cost sentence is reliable.
- Mem0 is a vendor paper [d18].
- ExpeL has no accounting of experience-gathering tokens [d19].

### 5.3 Moderators
- Signal quality: the check's false-positive rate (1.4% vs 16.3%) [a14]. Finder accuracy break-even about 60-70% [d03].
- Task type: soft metrics gain (sentiment, code optimisation), math does not [d08]. Puzzles with strong value functions gain from search, others do not [d10, d13].
- Model type: non-reasoning models have a large blind spot, reasoning-trained ones almost none [d05].
- Budget: the edge of search disappears at matched budget [d10, d13].
- Difficulty: revision on easy items, sampling or search on hard [d14].
- Reversibility: search in a live environment risks destructive actions [d12].

### 5.4 Interventions that worked
Code-run checks (Reflexion HumanEval; Voyager self-verification, -73% when removed; NL2GenSym critic, -23% when removed). Sound verifiers (Game of 24 from 5 to 38). Tool-interactive critique (CRITIC). Task-similarity retrieval (ExpeL 59.0 vs random 42.5). Curriculum ordering (Voyager -93% when random). Difficulty-aware compute. Bounded "Wait" (modest). Self-consistency at matched budget.

### 5.5 Interventions that did not
Model-only critique on reasoning tasks. Self-Refine on math. Reflexion without tests. ToT or debate at matched budget outside puzzles. Fine-tuned ACT-R traces on multi-facet targets. Memory systems beating long context. ACT-R-flavoured memory beating plain retrieval (never shown).

## 6. Language models

- 2022-24 models (PaLM-540B, GPT-3.5, GPT-4, Gemini 1.0/1.5): plain self-correction is flat or negative. GPT-4 GSM8K falls 95.5 to 89.0 over five calls [b13]. A sound verifier raises Game of 24 from 5 to 38 [d01].
- What changed results: an external signal (oracle or code) [b13, d01]; tools [d09]; sampling at matched budget [d10]; on-policy RL fine-tuning (SCoRe +4.4 on MATH vs -11.2 base) [d07]; reasoning-trained models [d05].
- 2025 reasoning models: little blind spot (Tsui). Reflection words in R1-Zero are not evidence of accuracy (Liu). A "Wait" nudge gives a small bounded gain (s1: +6.7 points on AIME24, which is 2 items of 30). No direct replication of Huang et al. on reasoning models was found.
- Size inversion: a small model with a framework can beat a larger one-shot (NL2GenSym Flash 86 vs Pro one-shot 55) [b26]. GPT-4 as coder gives 5.7x more Voyager items than GPT-3.5 [b18].
- Planning: raw LLM plans were executable about 3% of the time in 2023 [b22]. Newer reasoning models score far higher; do not use this number as current.
- Raw answers as knowledge: over 70% of raw LLM responses were not viable for an embodied agent in one task [a20].
- Memory: long-context GPT-5-mini beats agentic memory methods overall [d17].
- Caveat: most numbers come from 2023-24 models. The most recent direct measurements (d05, d06, d16, d17) are small or indirect.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **G2 / G3: revise only from external, real output; gate reflection on a measured check.** [E] K02, K03. Evidence a14, b11-b15, c13-c15, d01, d02, d03, d08, d09. The schema already says this. This research confirms it from five sources. Keep the guard; nothing new to add.
2. **G5: code validates every model proposal before use.** [E] K05. Evidence a20, b23, c07 (STARS 77.5/94.4/92.9 vs 52.5/66.7/35.7). Already in G5. Strengthen: a proposal that fails the check is repaired or discarded, never passed on.
3. **Memory: write lessons and library entries only after a code check passes.** [E] K06 (Voyager self-verification -73%; NL2GenSym critic -23%). Evidence b17, b18, b27, c17. Matches the current rule for lessons and the planned subgoal library.
4. **Section 1 design: model proposes, scaffold decides.** [E for direction] b06, b23, a20. Already our design.
5. **G7: equal-token comparison for every added element.** [E] d10, d13: complex strategies lose to self-consistency at matched budget. Do not relax it for tree search or reflection.

### Test first
1. **Typed impasse trigger with scoped sub-call, vs plain retry and vs self-consistency.** S6 control / G1. [S] K04; gap 1 open. Evidence a03, b05, c03, d10, d14. The schema's S6 slot already names Soar impasse-driven subgoaling.
2. **Gate reflection on a measured check false-positive rate.** G2. [S] K09, K18. Evidence a14, d03, d01.
3. **Compile verified solutions with reuse conditions (subgoal library) at equal total tokens.** Memory. [E that it works where a check exists; payback unmeasured] K06, K07. Evidence a21, c18, d19.
4. **Commit and reconsider step.** G1 / S. [S] K15. Evidence a22, d16.
5. **ACT-R scoring (recency, frequency, similarity) vs plain similarity or BM25.** Memory. [S; no positive evidence] K21. Evidence d17, d18.
6. **Difficulty-triggered switch between resample and revise.** G12. [S] K20. Evidence d14, d13.
7. **Hybrid ReAct plus self-consistency with a method switch.** O (act). [S] K16. Evidence b10.
8. **Search control stated explicitly in a spec.** S6 / O. [C] K12. Evidence b25.
9. **Search with a value-function accuracy check, only where actions are reversible.** G12 / O-search. [C] K08, K22. Evidence d11, d12, d13.
10. **Bounded "Wait" nudge vs outer critique loop on reasoning models.** G2 / G11. [S] K17. Evidence d05, d16.
11. **Use executable checks to pick among many samples.** G5. [S] K19. Evidence d15.

Out of scope (SCHEMA section 4b, no training): Memory-R1, AgeMem, ADAS, SCoRe, LLM-ACTR [c08, c21, c22, d07]. Cite only as upper-bound context (K13, K14).

## 8. Concrete tests on our bench

All arms get equal total tokens; setup and caching cost counted (G7). Report flips: right-to-wrong and wrong-to-right.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Typed impasse | Multi-step reasoning and code items where the first attempt fails (ARC-like, puzzles) | (a) plain model + retry; (b) self-consistency; (c) typed impasse trigger + scoped sub-call; (d) reflection | Accuracy at equal tokens; share of impasses resolved | (c) over (a) by a few points; unlikely to beat (b) except when sample agreement is low (inferred from d10) |
| T2 Check gate | Items with a code check of known false-positive rate | Reflection always; reflection only when check FP is below threshold; no reflection | Net flips; accuracy | Gated beats always when FP is high (Reflexion 16.3% vs 1.4%) |
| T3 Model-only vs code-run critique | Code and math items with a runnable check | Same loop with model critique vs code-run feedback | Round-by-round accuracy | Code-run gains; model-only flat or negative (d01, d09) |
| T4 Chunking cache | Two sequential item sets of one class | No cache; cache verified solutions with conditions; cache without conditions check | Accuracy on set 2 at total tokens including set 1 | Wins only if reuse rate is high; conditions check lowers wrong reuse (ExpeL task-similarity 59.0 vs random 42.5) |
| T5 Commit/reconsider | Multi-step tool or state-tracking tasks | ReAct; ReAct + explicit commitment with code-defined drop triggers | Success; tokens | Small gain or none; fewer thrashing steps |
| T6 Activation scoring | Multi-session memory questions | Similarity only; similarity + recency + frequency; BM25 | Accuracy; tokens | Likely no gain (d17); keep if over 2 points |
| T7 Difficulty switch | Mixed-difficulty math and puzzles | Uniform resample; uniform revise; difficulty-triggered switch | Accuracy at equal tokens | Up to 2-4x efficiency in d14; smaller without a trained reward model |
| T8 Hybrid ReAct + SC | Knowledge QA | ReAct; CoT-SC; CoT-SC then ReAct fallback | EM | Hybrid +1 to +2 over SC (b10) |
| T9 Search control in spec | Planning items | Spec with operators only vs with search-control hints | Steps/tokens to solution | Large saving if Wray 2024 carries over; unknown |
| T10 Wait nudge | Reasoning-model items | Plain; bounded Wait (2-4); outer critique | Accuracy; tokens | Small gain from Wait; critique adds little (d05, d16) |
| T11 ToT vs best-of-N | Non-puzzle items | ToT/LATS-like vs best-of-N at same tokens | Accuracy | No edge (d10, d13) outside puzzles with strong value |

## 9. What does not transfer, and why

- The review's gaps as proof: "residual" means not found in the corpus. It is not evidence that the missing coupling would help.
- Reflexion's headline gains: they come from environments or tests that give a reliable signal. Without it there is no gain, and sometimes a loss.
- Generative Agents' believability gain (d=8.16): rater judgment in a 2-day simulation. Not reasoning gain.
- MemGPT's DMR gain: against truncation, on a self-built task. Long context beats it when everything fits.
- ToT's Game of 24 result: a bounded puzzle with checkable states and many more calls.
- Voyager: Minecraft, GPT-4, re-interpreted baselines, 3 runs. Skill code is verified by environment state.
- ACT-R activation and latency: human reaction-time fits have no meaning for a stateless model whose cost is tokens. Only the idea of one cost-aware score may carry.
- Soar chunking's automatic dependency tracing: LLM context is not a symbolic working memory, so which conditions supported a result is not observable. Conditions must be written explicitly and verified.
- Learning-based items (Memory-R1, ADAS, SCoRe, LLM-ACTR): need training or design-time search. Out of scope.
- Global-workspace broadcast and bounded content competition: no measurement. A single-agent scaffold has no competing modules to broadcast between.
- The message-bus, checkpoint, handoff and guardrail equivalences are rejected by the review itself [b02]. Do not claim them.

## 10. Open questions

1. Does a typed impasse with a scoped sub-call beat plain retry or self-consistency at equal tokens? (gap 1, no study)
2. Does a commit/reconsider step help at equal tokens? (gap 2)
3. What check reliability makes reflection pay with current reasoning models? (gap 3; only a 2023 simulation: 60-70%)
4. Does intrinsic self-correction still fail on 2025-26 reasoning models, and which verifier types restore it? (gap 4)
5. Does chunking-style caching pay at equal total tokens? Laird 1986 data unread. (gap 5)
6. What are the ACT-R activation equation and fit numbers, and does recency/frequency/context beat similarity at equal tokens? (gap 6)
7. Do independent coders and other 2025-26 surveys agree with Fan and Lan? (gap 7)
8. Does search keep an edge over best-of-N at the same budget off puzzles? (gap 8; leans no)
9. Does omitted search control cost orders of magnitude in prompt scaffolds? (gap 9)
10. Are there controlled studies of LLM-in-Soar or LLM-in-ACT-R beyond the three tasks in STARS?

Limits of this pass: the web search budget ran out early. arXiv, Semantic Scholar and OpenAlex returned HTTP 429. Gap-pass pages were read through a fetch summariser, with long pages cut at 100000 characters. Newell 1990, Laird 1986, ACT-R 2004 and Assanie 2022 were not read.

## 11. Sources

[V] opened, [M] snippet only or not read.

- [V] Fan and Lan (2026) From Cognitive Architectures to Language Agents: A Mechanism-Level Review. https://arxiv.org/abs/2607.23942
- [V] Sumers, Yao, Narasimhan, Griffiths (2023/24) CoALA. https://arxiv.org/abs/2309.02427
- [V] Laird (2022) Introduction to the Soar Cognitive Architecture. https://arxiv.org/abs/2205.03854
- [V] Yao et al. (2022) ReAct. https://arxiv.org/abs/2210.03629
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Packer et al. (2023) MemGPT. https://arxiv.org/abs/2310.08560
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Zhou et al. (2023/24) LATS. https://arxiv.org/abs/2310.04406
- [V] Valmeekam et al. (2023) On the Planning Abilities of LLMs. https://arxiv.org/abs/2302.06706
- [V] Wei et al. (2022) Chain-of-thought prompting. https://arxiv.org/abs/2201.11903
- [V] Kirk, Wray, Lindes, Laird (2024) STARS. https://arxiv.org/abs/2306.06770
- [V] Kirk, Wray, Laird (2023) Exploiting Language Models as a Source of Knowledge. https://arxiv.org/abs/2310.06846
- [V] Wray, Kirk, Laird (2025) Applying Cognitive Design Patterns to General LLM Agents. https://arxiv.org/abs/2505.07087
- [V] Wray, Kirk, Laird (2024) Eliciting Problem Specifications via LLMs. https://arxiv.org/abs/2405.12147
- [V] Yuan et al. (2025) NL2GenSym. https://arxiv.org/abs/2510.09355
- [V] Zhu and Simmons (2024) Bootstrapping Cognitive Agents with a Large Language Model. https://arxiv.org/abs/2403.00810
- [V] Wu et al. (2024) LLM-ACTR. https://arxiv.org/abs/2408.09176
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Yan et al. (2026) Memory-R1. https://arxiv.org/abs/2508.19828
- [V] Hu, Lu, Clune (2025) ADAS. https://arxiv.org/abs/2408.08435
- [V] Laird, Lebiere, Rosenbloom, Stocco (2025) Extend the Common Model of Cognition. https://arxiv.org/abs/2506.07807
- [V] Stechly, Valmeekam, Kambhampati (2024) On the Self-Verification Limitations of LLMs. https://arxiv.org/abs/2402.08115
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516
- [V] Tsui (2025) Self-Correction Bench. https://arxiv.org/abs/2507.02778
- [V] Liu et al. (2025) Understanding R1-Zero-Like Training. https://arxiv.org/abs/2503.20783
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Wang et al. (2024) Reasoning in Token Economies. https://arxiv.org/abs/2406.06461
- [V] Koh et al. (2024/26) Tree Search for Language Model Agents. https://arxiv.org/abs/2407.01476
- [V] Wu et al. (2025) Inference Scaling Laws. https://arxiv.org/abs/2408.00724
- [V] Snell et al. (2024) Scaling LLM Test-Time Compute Optimally. https://arxiv.org/abs/2408.03314
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/abs/2501.19393
- [V] Hu et al. (2025) Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions. https://arxiv.org/abs/2507.05257
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Foundation Agents survey, 48 authors (2025), first 100000 of 468617 characters only. https://arxiv.org/abs/2504.01990
- [M] Always-On Agents survey (2026). https://arxiv.org/abs/2606.30306
- [M] Joshi and Ustun (2024) Comparing LLMs for Prompt-Enhanced ACT-R and Soar. https://ojs.aaai.org/index.php/AAAI-SS/article/view/27710
- [M] Newell (1990) Unified Theories of Cognition (book; via citations). No URL.
- [M] Laird, Rosenbloom, Newell (1986) Chunking in Soar. No URL.
- [M] Anderson et al. (2004) An integrated theory of the mind (ACT-R). No URL.
- [M] Assanie (2022), cited by Laird 2022; not opened.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 4 established claims: 2 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C02.10-K05** (now single-source: the sources are not independent). Numbers match Kirk et al. Table 2 (STARS 77.5/94.4/92.9 vs TBP 52.5/66.7/35.7; over 70% unviable in one task), but both supporting papers are the same Soar group (Kirk, Wray, Laird) and the evidence is one simulation study, one run per condition; Zhu and Simmons does not test this.
- **C02.10-K06** (reworded: the sources support less). Numbers check out (ExpeL 40.0 to 59.0; task-similarity 59.0 vs random 42.5; Voyager; AWM +12.0 pts), but no source tests the 'only where a cheap executable check exists' condition, and ExpeL stores text insights and trajectories, not compiled rules or code. Corrected claim: Reusing experience from earlier episodes helps in Voyager (verified code skills), AWM (workflows from successful trajectories), ExpeL (text insights plus retrieved successes; ALFWorld 40.0 to 59.0, task-similarity retrieval 59.0 vs random 42.5) and bootstrapped agents; Voyager's ablations show self-verification matters most, which suggests (not shown) that a cheap executable check is needed. Payback at equal total tokens is unmeasured; Laird 1986 chunking data unread.
