# Embedded cognition: deep document

*Subfield A16.02. Written from evidence_a-d.jsonl (a01-a26, b01-b25, c01-c25, d01-d22), claims.jsonl (K01-K24) and critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. Ids like a20 are evidence lines; K04 is a claim.*

## 1. What it is

Embedded cognition is the view that a task has a cognitive load, and that an agent can lower that load by working in a well-designed physical or social setting (SEP, a14). The thinking still happens inside the agent. The setting carries part of the work. This differs from the extended-mind view, where the setting is part of the thinking itself (Wheeler 2013, b21, snippet only).

Two founding papers are named for this subfield. Martin and Schwartz (2005) showed children learn fractions better when they can move and re-arrange physical pieces (a13, b01, d20). Hutchins (1995, 1996) described how a Navy ship's navigation team spreads a computation over people, charts and instruments (a15, a16). Neither paper was read in full by any agent in this study. Martin and Schwartz is known from its abstract; Hutchins from reviews.

Why it matters for our agent: the design view. The program that wraps the model is the model's environment. If the environment can carry load, the program should do exact work (counting, comparing, enforcing rules, keeping a log), show the model short filtered views, and give it cheap ways to probe the world before it commits. This is the theme behind most of the strong LLM evidence below.

Scope note. This subfield is about load moving into the setting. It is not about the claim that using phones or the web harms memory. That family is weak (section 5) and the schema should not rest on it.

## 2. History and theories in depth

**Distributed cognition and the ship (Hutchins).** Hutchins studied the USS Palau at Sea and Anchor Detail. A team of up to ten people runs a fix cycle about every three minutes. Two pelorus operators sight three bearings; the plotter turns them into a triangle on the chart (a15). The computation is in the team, the instruments and the chart, not in one head. Latour's reading, quoted from the book (p.154): a tool does not amplify an ability; it presents the task as a different problem that needs a different organisation of the work (a16). This is the "tools change the task" idea. It is ethnography. No controlled comparison and no error rate exists in what we read (b22; d22 failed because the book text was behind a lending login). A search snippet says the calculator did not help in the power-loss episode; it is unverified (a17).

**Distributed representation (Zhang and Norman 1994).** Four Tower of Hanoi isomorphs share one problem space but code the rules differently. Difficulty differed with representation (a05). When rules were moved from memory into the objects, the puzzle got easier. Subjects made zero errors on externally enforced rules; all errors were on internal rules (a06, a07). Experiment 3 coded two dimensions as size, colour or location; location worked best for the ordinal dimension (a08). This is the cleanest human case that how the rules are represented in the world changes behaviour, with the problem space held fixed.

**Epistemic action (Kirsh and Maglio 1994).** Tetris players rotate and move pieces in ways that do not advance the plan. The authors call these epistemic actions: moves that change the world to make thinking cheaper, faster or more reliable. Pragmatic actions move toward the goal (a01). A plan-then-act model predicts about half the possible rotations; the observed rotations exceed that for every piece type (a01). A physical 90 degree rotation takes about 100 ms (about 300 ms with a button choice). A mental 90 degree rotation takes about 800 to 1200 ms (a02; 3 pilot players only). Players also run a piece to the nearest wall and back to verify its column, more often as drop height rises (a03). The authors argue that chunking and compiled routines do not explain the extra moves (a04). A cost-benefit shape is implied: at great height the cost of leaving the goal column is outweighed by the error it prevents.

**Physically distributed learning (Martin and Schwartz 2005).** Five studies with 9 and 10 year olds on fractions. Handling pieces helped children build a meaning for fractions. In Experiments 4 and 5, children who adapted a loosely structured set of materials transferred better than children given well-structured materials (d20). SEP adds that children did better at 1/4 of 8 when they moved pie pieces than when they only viewed them (a13). Per-study N and effect sizes were not read. The key idea is that adapting the environment lets new interpretations form, which a fixed setting would not.

**Offloading as metacognition (Risko and Gilbert 2016).** Offloading is using physical action to change the information-processing demands of a task. People offload when they believe it helps, so confidence guides it (a10). Follow-up work (a09, b08) measures this directly.

**Embedded versus extended (Wheeler 2013).** Embedded: the environment scaffolds an inner process. Extended: it is part of the process. The tests differ on whether the inner skill survives removal of the scaffold (b21, snippet). For our agent the distinction is practical. Our harness is permanent, so the agent plus harness is the unit that is tested.

**LLM-era lines.**
- Scratchpads and chain of thought (Nye 2021; Wei 2022): writing intermediate steps is external working memory (a19, b09).
- Tool use and program offload (PAL 2022; Toolformer 2023): the interpreter does the exact step (a21, b11, b12).
- Acting in an environment (ReAct 2023; Voyager 2023; Reflexion 2023): observations and verification come from the world (a18, a22, a23).
- Interface design (SWE-agent 2024): the same model does better or worse by interface (a20).
- Framing papers: CoALA (a24), an externalisation review (c17), MetaGPT (c14), MemGPT (c16). These give structure but no new measured results.
- Social setting for LLMs: multi-agent systems and their failures (b17, c04, d03, d05, d07).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Tetris players use epistemic moves; physical rotation is far cheaper than mental | Physical 90 deg about 100 ms (300 ms with button choice) vs mental 800-1200 ms; 3 pilot players. Observed rotations exceed plan-first prediction for every piece type | a01, a02, Kirsh and Maglio 1994 | [S] descriptive |
| Players verify position by running to the wall; more as drop rises | Fig 15 trend over 0-30 rows; no inferential test | a03 | [S] |
| Moving rules into the objects lowers errors | 18 subjects; condition effect p<.05 times/steps, p<.005 errors; all-internal vs 2-external errors p<.001; zero errors on external rules | a06, a07, Zhang and Norman 1994 | [S] |
| Representation changes difficulty at fixed problem space | Exp 1A: 24 students, 4 isomorphs (2, 4, 7, 8 minimum steps); Exp 3: 36 subjects, 9 isomorphs | a05, a08 | [S] |
| People offload more when less confident | N=363; hit rate 88.1% offload-allowed vs 82.7%, F(1,361)=39.1; instructed group offloaded about 53.1% of trials | a09, Boldt and Gilbert 2019 | [E] (related papers) |
| People over-offload; loss framing reduces it | Exp 1 N=141; Exp 2 forced-internal accuracy about two thirds, forced-external near all | b08 | [S] |
| Scratchpad enables multi-step computation | Polynomial evaluation 8.8 vs 20.1 (few-shot), 31.8 vs 50.7 (fine-tuned); program tracing 11/20 direct vs 26.5/41.5 (table partly garbled) | a19, b10 | [E] |
| Many wrong chains are slips | 46% of inspected wrong chains nearly correct; 54% major errors | b09, Wei 2022 | [E] |
| Program executes the exact step | GSM8K PAL 72.0%, about 15 points above PaLM-540B CoT; GSM-Hard CoT 65.6 -> 20.1, PAL 61.5; DIRECT 19.7 -> 5.0 | a21, b11 | [E] |
| Calculator tool lifts a 6.7B model | ASDiv/SVAMP/MAWPS: GPT-J 7.5/5.2/9.9; Toolformer tools off 14.8/6.3/15.0; tools on 40.4/29.4/44.0; GPT-3 175B 14.0/10.0/19.8 | b12 | [S] |
| Thought + action beats either | ALFWorld best ReAct 71% vs Act 45% vs BUTLER 37%; worst ReAct 48%; HotpotQA EM 33.8 vs CoT 28.9 vs standard 27.1 | a18, b13 | [S] |
| Interface alone moves success (GPT-4 Turbo, Lite N=300) | Shell-only 11.0 (7.33 without demo); full ACI 18.0 (54/300). Edit: none 10.3, no lint 15.0, lint 18.0. Search: none 15.7, iterative 12.0, summarised 18.0. Viewer: 30 lines 14.3, 100 lines 18.0, full file 12.7. Context: full history 15.0, last 5 obs 18.0, no demo 16.3 | a20, c02, critique | [C] era-specific |
| Full SWE-bench result | 12.47% (286/2,294) GPT-4 Turbo; Claude 3 Opus 10.46%; HumanEvalFix pass@1 88.3%; 1,185 of 2,294 trajectories (51.7%) had a failed edit | b14, b25, critique | [S] |
| A fixed program-owned pipeline beats tool-choice agents on Lite | Agentless 96/300 (32.00%) at about $0.70; SWE-agent 18.33% (GPT-4o) / 23.00% (Claude 3.5 Sonnet) at $1.62; AutoCodeRover 21.67% | d08 | [S] |
| Bash-only 100-line agent | Reported above 74% on Verified, model not named | d09 | [S] project page |
| Self-correction without outside feedback hurts | GPT-3.5 CommonSenseQA 75.8 -> 38.1 -> 41.8; GSM8K 75.9 -> 75.1 -> 74.7; HotpotQA 26.0 -> 25.0 -> 25.0; oracle CSQA 89.7. GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; keeps first answer 74.7% (GPT-3.5 GSM8K) | b15, b24 | [E] |
| Environment verification matters most in Voyager | No self-verification -73% items; random curriculum -93%; GPT-4 vs GPT-3.5 code 5.7x items; headline 3.3x items, 2.3x distance, milestones up to 15.3x faster. 3 runs, one game | a22, b16, c12 | [S] |
| Reflection tied to outcomes helps | Reflexion HumanEval 91 vs 80; ALFWorld +22 points in 12 trials | a23 | [S] |
| Harness helps strong, not weak, models on games | o3 Tetris 31 -> 42, Sokoban 2 -> 8; o1 Tetris 13 -> 35; gpt-4o 14.7 -> 14.0; Claude 3.7 thinking 13.0 -> 16.3; random 10.2. 13 models, 3 runs (o1, o3: 1 run) | c18 | [S] |
| Multi-agent splits help hard tasks, hurt instruction following | CoThinker LiveBench vs Flash-8B IO=1.00: CoThinker 2.09, DMAD 2.05, MAD 1.92, Pro IO 1.85, CoT 1.79; instruction following Pro 0.95 vs IO 1.03. Under 8192 tokens: Gemini-2.5 reasoning 69.2 vs 31.0 | c04, c06 | [C] no equal-compute control |
| Shared memory is model dependent; role styles help all | Math subset. Qwen3-30B both 81.87, no styles 69.79, no shared memory 76.41. GPT5-Nano 55.97 / 49.02 / 62.36. GPT-OSS-20B 57.15 / 48.21 / 58.37 | c05 | [S] |
| Multi-agent failure taxonomy | 1600+ traces, 14 failure modes, kappa 0.88 human / 0.77 LLM annotator; ChatDev +15.6 from a verification step, +9.4 from prompt fix | b17 | [S] |
| At equal thinking tokens a single chain wins from 1000 tokens | Mean accuracy over 4 models x 2 datasets. 100 tokens: single 0.290, sequential 0.364, debate 0.370. 1000: 0.418 vs 0.379 vs 0.388. 2000: 0.421 vs 0.389 vs 0.403. 5000: 0.427 vs 0.386 vs 0.420. 10000: 0.426 vs 0.387 vs 0.420 | d03, Tran and Kiela 2026 | [E] with K21 |
| Splitting helps when context is corrupted | Gold answer in thoughts: sequential-right/single-wrong 41.7% vs 12.5% (Gemini Flash), 56.7% vs 18.3% (Qwen3) | d04 | [S] |
| Scaling study: 260 configurations | Range +80.8% (structured finance, centralised) to -70.0% (sequential planning); planning -39% to -70% for all multi-agent; capability ceiling beta=-0.236, p=0.004; tool coordination beta=-0.096, p=0.002; 45% single-agent threshold matches 94% of cells | d05, Kim 2026 | [S] strong design |
| Debate rarely beats CoT | 36 configurations; four debate methods beat CoT in about 15% of cases; SoM lost to CoT on all 9 datasets on GPT-4o-mini | d07 | [E] |
| Single agent with a demo nearly matches discussion | Upper bound similar to all discussion frameworks (FOLIO-wiki); exact values not extracted | d06 | [S] |
| Think tool: scratch place helps policy-heavy tasks only | Airline pass^1: baseline 0.332, think alone 0.404, extended thinking 0.412, think + prompt 0.584 (page text says 0.370 vs 0.570; table and text disagree). Retail: think 0.812, extended 0.770, baseline 0.783. SWE-bench +1.6% | d10 | [S] vendor |
| Memory tool + context editing (vendor) | +39% combined, +29% editing alone, 84% fewer tokens in 100-turn search; internal eval | d11 | [S] vendor |
| Multi-turn loss is large; a fresh consolidated message removes it | 39% average drop across 200,000+ conversations; restating recovers 15-20%; GPT-4o and 4o-mini on code, database, math, actions | d12 | [S] |
| Models choose epistemic probes badly | o3-mini, 5 trials per scenario, 7 types; first-take correct 100% base/perspective/near, 0-40% under distractor/hidden/not-that/far; steps about 3.0-3.3 vs planner 2.14 | d13, c19 | [S] |
| Information-gain rule picks better probes | Average success gain 38.1% across LLMs (abstract only; not equal tokens) | d14 | [S] |
| A prompted tool-need check is a weak gate | MetaTool Llama3-8B decision accuracy: always-call 50.0%, self-report 61.9%, P(Yes) 63.5%, MeCo 65.0%; fine-tuned 82.1 / 81.7 / 84.3 | d15 | [S] |
| Tower of Hanoi "collapse" with algorithm given | Collapse near N=7-8 (255 moves at N=8); algorithm in prompt did not move it; first failure about move 40 at N=8 (about 15%); temperature 0 no change | a26, c07, d02 | [C] |
| Hanoi as a function fixes it (critic) | Output about 10 tokens/move, max solvable N about 12-13 at 64k; N=15 as Lua function "very high accuracy"; no counts | c08, d01 | [C] |
| Phone-presence harm is small | Meta: 22 studies, 43 effects, abs g=0.14 (CI 0.03-0.24), I2=61.8%; memory 0.23; attention 0.07; general 0.10 (signs lost in extraction) | b03 | weak |
| Ward 2017 replication null | N=383, OSpan location F(2,377)=0.10, p=.91, partial eta2=.001 | d18 | replication failed |
| 2023 phone meta-analysis | k=56, n=7,093; only working memory significant of six pooled effects | d19 | weak |
| Google Stroop effect fails to replicate | Original N=46. Camerer N=104 then 234 pooled; Hesselmann N=117 tested, 89 analysed, BF01=5.07, easy block 830 vs 901 ms, hard 825 vs 821 ms | d16, d17 | replication failed |
| Social-science replication project | 13 of 21 (62%) replicated; effect about 50% of original | b07, d17 | context |
| Google-effect meta-analysis | 22 studies; pooled abs d about 1.01, CI 0.12-2.13 (implausibly wide) | b06 | weak |
| LLM as the aid reduces recall of own text | 54 participants, 18 per group; 15/18 (83.3%) LLM users could not quote vs 2/18 (11.1%) search and brain-only | b18 | [S] preprint |
| Tools matter for the human-vs-model gap | GAIA: humans 92% (L1 94, L2 92, L3 87) vs GPT-4 with plugins 15% | a25 | context |

## 4. Mechanisms and models

Each mechanism is stated so that it can be built. The evidence tag is in brackets.

**M1. Program-held exact work.** The model decides what to compute; the program computes. Pattern (PAL): the model emits code; a sandbox runs it; the result goes back as text. Gain grows with the number size: CoT falls 65.6 to 20.1 when GSM8K numbers get large, PAL stays at 61.5 (b11). Build: a `run(code)` tool, deterministic, returns stdout and errors verbatim. The model does not do arithmetic, sorting, counting or set comparison in prose. [E, K01]

**M2. Written workspace.** A scratchpad is working memory outside the weights (a19). It lets the model do steps it fails at in one pass. About 46% of wrong written chains are slips that code could fix (b09). Build: the model writes steps; code re-executes each checkable step and flags mismatches. A fixed template is what the think tool offers (d10). An agent-editable workspace is the Martin and Schwartz manipulation and is untested (K16). [E for the scratchpad; S for editable]

**M3. Bounded, filtered views.** The program, not the model, decides what part of the state is shown. SWE-agent: a 100-line viewer beat 30 lines and the full file (18.0 vs 14.3 vs 12.7); summarised search beat iterative search (18.0 vs 12.0); last 5 observations beat full history (18.0 vs 15.0) (c02). Build: a view function with a window size, a summariser for search results, a rolling history that keeps the last k observations plus a program-kept table of verified facts. The numbers are one model, one run per cell, and the era is old (d08, d09), so the direction is plausible and the sizes are not portable. [C, K04; the principle "more raw information can hurt" is K05 [E]]

**M4. Guardrails that reject bad actions.** Lint-on-edit rejects a bad edit before it lands (18.0 vs 15.0, c02). Zhang and Norman: external rules produced zero errors, internal rules all the errors (a07). Build: a validator that checks every proposed move against the rules and returns the exact violation. Do not rely on rules written in the prompt. The effect mixes constraint enforcement and load relief, and the data cannot separate them (K08). [S]

**M5. Epistemic probes.** Cheap actions that reveal state before committing: run it, print the shape, reformat the grid, try the boundary case. Kirsh and Maglio's cost-benefit shape: probe more when the cost of being wrong is high (a03). LLM evidence: models pick probes badly (d13). A program-side rule that scores candidate probes by expected information gain gave +38.1% in Uncertainty of Thoughts (d14, abstract only). Build: the harness proposes N cheap probes, a scorer (information gain over the current hypotheses) picks one, the harness runs it. Budget it inside the token cap. [S, K09/K20]

**M6. Environment-grounded verification.** The signal for revision comes from execution, not from the model rereading itself. Intrinsic self-correction: GSM8K 75.9 to 74.7; CSQA 75.8 to 41.8; apparent gains come from oracle labels (b15). Voyager: removing self-verification cost 73% of items (b16). Build: a check that runs (test, simulator, held-out example) and returns pass/fail plus output; revision prompts quote that output. [E for "no revision without outside signal" (K06); S for the Voyager size (K07)]

**M7. Program-held state, fresh view.** The program holds a table of verified results and rebuilds a short prompt each step, instead of letting the model re-read a long transcript. Support is indirect: multi-turn instructions lose 39% versus one message; a fresh consolidated message removes it; restating recovers 15-20% (d12). Vendor numbers for memory tool plus context editing: +39% (d11). Kosmyna's memory cost is human-side (b18). No direct test at equal tokens (K22). [S]

**M8. Gates on added structure.** Extra voices, splits and tool calls help sometimes and hurt otherwise. Gate rule from Kim 2026: skip the extra agents when the single-agent score is about 45% or higher, or the task is sequential (d05). Tran and Kiela: at equal thinking tokens the single chain wins from 1000 tokens, except under heavy context corruption (d03, d04). A prompted "do I need a tool" check is weak (61.9% vs 50.0% for always-call, d15); a hidden-state gate does a little better (65.0%). Build: estimate the class's plain pass rate (the S0 gate, from the class record) and only then switch on extra structure. [E for the direction, K21; the exact 45% threshold is [S]]

**M9. Program-owned control flow.** A fixed localise, repair, validate pipeline owned by the program matched or beat model-chosen tool loops on Lite: 32.00% at $0.70 vs 18.33-23.00% at $1.62 (d08). This supports the design view: fewer model decisions about the environment. It does not say which feature of SWE-agent mattered. [S, K24]

**M10. Social setting as load split (CoThinker).** Agents get roles, a shared memory, and a split of the sub-problems (c04). Gains on hard tasks, a loss on instruction following (0.95 vs 1.03). Under an 8192-token budget, large gains (c06). The shared memory helped some models and hurt others (c05). No equal-compute control exists in the paper; the equal-compute studies show the single chain wins from 1000 tokens (d03). Treat as a tool for corrupted or very small-budget settings only. [C]

## 5. What holds up

**Replications, meta-analyses, failures.**
- Sparrow 2011 Google Stroop: failed in Camerer 2018 (original N=46; replication N=104 then 234 pooled) and again in Hesselmann 2020 (N=89, BF01=5.07, preregistered t(88)=-1.04, p=.301) (d16, d17). The replications tested Experiment 1 (the Stroop-type test), not the memory experiments. Overall Camerer: 13 of 21 replicated at about half the original effect (d17).
- Ward 2017 brain drain: preregistered Experiment 2 replication N=383, OSpan location F(2,377)=0.10, p=.91; one uncorrected go/no-go interaction at p=.04; moderators did not change the null (d18). Another replication (Acta Psychologica 2022) was not read (b05).
- Meta-analyses: 22 studies, 43 effects, abs g=0.14, I2=61.8% (b03). 56 effects, n=7,093, only working memory significant (d19). Google-effect meta: abs d about 1.01 with CI 0.12-2.13, bias checked by funnel plot only (b06). Original Ward and Sparrow effect sizes were not read, so no original-versus-replication pairs exist here.
- Handwriting advantage: reportedly shrank in replication (b19, snippet; d=0.45 factual, 0.13 conceptual unconfirmed).
- Concrete versus abstract examples: Trninic et al. 2020 reportedly found well-built concrete examples matched or beat abstract ones (b02, abstract). Lesson: the environment arm must be as well built as the control (K19).
- Verdict. The human "technology harms memory" family is weak (K11). The designed-setting family (Zhang and Norman, Kirsh and Maglio, Martin and Schwartz) is old, small-N and has no large replication in what we read.

**Moderators and boundary conditions.**
- Model strength. Harness helped o3 and o1 on games, not gpt-4o (c18). Coordination gains vanish above about 45% single-agent score (d05). No direct weak-model harness-on/off test at equal tokens (K14).
- Task type. Multi-agent hurts sequential planning by 39-70% (d05); hurts instruction following (c04); helps structured finance +80.8% and web navigation decentralised +9.2% in selected cells (d05).
- Context corruption. Splitting wins when the single context is heavily degraded (d04).
- Task simplicity. The think tool is of little use on simple tasks (retail 0.812 vs 0.783, d10).
- Era. The 2024 interface gains in SWE-agent are matched or exceeded by a fixed pipeline (d08) and a minimal bash-only agent (d09). Specific interface sizes may not transfer to current models.
- Feedback quality. Reflexion and Voyager gains rely on informative feedback such as unit tests (a23, a22).
- Region. Brain-drain effect varied by region (Asia 0.39, Europe 0.20, North America 0.03, b03).

**Interventions that worked.**
- Execute exact steps in code (K01). Write intermediate steps (K02). Environment feedback in the loop (K03, single source). Bounded views and guardrails (K04, contested on size). Gate multi-voice structure on strength and task shape (K21). Role styles in CoThinker helped all three models tested (c05).

**Interventions that did not work.**
- Intrinsic self-correction (K06). Debate beating CoT in most configurations (d07). Multi-agent on sequential planning (d05). Iterative search and full-file views (c02). Naive "do I need a tool" prompting (d15). Few-shot planner traces for probe choice (d13). Giving the Hanoi algorithm in the prompt (a26, contested). Phone-presence harm (d18).

**Independence note.** Many LLM lines repeat one paper. ReAct appears as a18, b13, c13. SWE-agent as a20, b14, b25, c01, c02. PAL as a21, b11, c10. Voyager as a22, b16, c11, c12. Each counts once. K01, K02, K05, K06 and K10 are marked established, plus K13 and K21 after the gap search; several rest on related papers, not on one replicated result. Treat as moderate.

## 6. Language models

**What the LLM studies test.** No study measures load. All "environment reduces load" LLM claims are about accuracy (b23). The best direct tests hold the model fixed and change the environment: SWE-agent (c01, c02), PAL (b11), Toolformer on/off (b12), Voyager ablations (b16), the Tetris and Sokoban harness (c18). None holds the tool fixed and varies only whether the agent may edit its own workspace (b23, c24). Searches for LLM versions of Martin and Schwartz, Hutchins and Kirsh found none (c24).

**Where the environment gave big gains.**
- Exact computation. GSM-Hard: CoT 65.6 to 20.1, PAL 61.5 (b11). Toolformer 40.4 with tools vs 14.8 with the same weights and tools off (ASDiv, b12). Scratchpad: 8.8 to 20.1 few-shot (a19).
- Interface. SWE-agent shell-only 11.0 vs 18.0 (c01); no edit tool 10.3 (c02). One model, one run per cell.
- Perception and state. o3 Tetris 31 to 42 with a harness; o1 13 to 35 (c18).
- Verification. Voyager -73% without it (b16).

**Where it gave small gains or none.**
- Weak non-reasoning models on the game harness: gpt-4o 14.7 to 14.0 (c18).
- Simple tasks: think tool on retail (d10).
- Strong single agents: coordination gains vanish above about 45% (d05).
- Many agents: debate beats CoT in about 15% of 36 configurations (d07); the single chain beats five layouts from 1000 thinking tokens (d03).
- Self-correction with no outside signal: down 0.8 to 4.0 points on GSM8K (GPT-3.5 75.9 to 74.7; GPT-4 95.5 to 89.0 is a 6.5 point drop) and down about 34 on CSQA for GPT-3.5 (b15).

**What changed the result, by how much.** Interface in SWE-agent: up to 7.7 points from the edit tool, 6.0 from search style, 5.3 from viewer size, all at GPT-4 Turbo (c02). CoThinker's large wins did not include an equal-compute control; where equal-compute was tested, the single chain won from 1000 tokens (d03, d05). Gating: always-call vs prompted check 50.0% vs 61.9% decision accuracy (d15). Probe choice: o3-mini first-take 100% on easy scenario types, 0-40% when distractors or hidden cases appear (d13). Hanoi: contested; the safe summary is that output format and who executes the procedure matter, and that a model-written program run by a harness has not yet been counted at 8-15 disks (d01, d02).

**Cautions for reading these results.**
- The Hanoi dispute has two sides. Lawsen says the collapse is mostly output limit and grading, and some River Crossing items are unsolvable (c08, d01). Shojaee et al. reply that failures begin about move 40 at N=8, well within limits, and temperature 0 does not change it (d02). Both agree on the design lesson: let the program execute long procedures.
- Cognitive Workspace (c03) reports reuse 54.5% to 59.8% vs 0% for plain RAG, no accuracy, and effect sizes that are not credible (d up to 196). Do not cite it for gains.
- Vendor blog numbers (d10, d11) are internal; the d10 table and text disagree.
- SWE-agent gains are a single run on N=300; noise is a few points.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory (section 5 of SCHEMA.md).

### Add now (established)

1. **Exact work goes to code.** Counting, arithmetic, comparing, sorting, set operations and grid transforms are done by a sandbox, not in prose. Schema: G5 (code selects), widened from selection to computation; S4 runs it. [E] K01. Evidence a21, b11, b12, c10, a19, b10.
2. **Revise only from environment output.** Already G2. Add the strength: intrinsic self-correction lowers accuracy (CSQA 75.8 to 41.8), and oracle labels explain earlier gains (89.7). Schema: G2, G3, S5. [E] K06. Evidence b15, b24.
3. **Do not add extra voices by default; gate them.** Run a multi-voice or split step only if the class's single-pass score is under about 45% or the context is heavily degraded, and never on sequential planning. Schema: G4, G9, S0 gate, G7. [E] for direction (K13, K21); the threshold is [S] from d05. Evidence d03, d04, d05, d06, d07, b17.
4. **Bound what the model sees.** Show filtered, bounded state; do not dump full files, full histories or raw iterative search. Schema: G7 cost accounting, S1 input hygiene extension, context rebuilt per attempt (S3). [E] for "more information can hurt" (K05); sizes [C] (K04). Evidence c02, b14, c04, d03.
5. **Same-model agents are not independent checkers.** Already G4. Add the equal-compute evidence. [E] K13. Evidence d03, d07, b17.
6. **Gate tool calls on a calibrated signal, not on the model's say-so.** Humans over-offload; an LLM self-report gate is weak (61.9% vs 50.0%). Schema: G1, G7. [E] K10 for the human problem; the LLM fix K23 is [S]. Evidence a09, b08, d15.
7. **Do not design on phone/web-harms-memory claims.** The K11 family is weak. Nothing to add. Evidence b03, d16, d17, d18, d19.

### Test first (single-source or contested)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Program-held verified-results table rendered each step instead of the full transcript | memory, S3 | [S] K22 | d11, d12, b18 |
| T2 | Rule validator that rejects illegal moves instead of rules stated in the prompt | G2/G3, S4 | [S] K08 | a06, a07, c02 |
| T3 | Cheap probe actions before the answer commit; harness picks the probe by information gain | new pre-step in S4 | [S] K09, K20 | a01, a03, d13, d14 |
| T4 | Agent-editable scratch workspace versus fixed scratch template | S1/S2, O6 | [S] K16 | d20, d10 |
| T5 | Bounded view size and feedback verbosity (viewer lines, history length) | S3 context | [C] K04 | c02, d08, d09 |
| T6 | Fixed program-owned pipeline versus model-chosen tool loop | design view | [S] K24 | d08, d09 |
| T7 | Verification step removed from the loop only | G3, S8 | [S] K07 | b16, a22 |
| T8 | Code-emitting solution for long procedures (Hanoi 8-15 disks) | G5 | [C] K15 | c08, d01, d02 |
| T9 | Memory of verified failures versus unverified self-notes | memory | [S] K17 | a23, c16, d11 |
| T10 | Voice gate at the 45% single-pass threshold | G9, S0 | [E] direction, [S] threshold, K21 | d05, d03 |
| T11 | Harness on/off on weak versus strong model | design | [S] K14 | c18, d05 |
| T12 | Observation feedback removed from the act-and-observe loop | G2, S4 | [S] K03 | a18, b13 |

Framing only: Hutchins and Latour (K18). They suggest that a tool changes the task, so S0 should classify the task as given the tools, not as the bare task. Not testable as stated.

## 8. Concrete tests on our bench

All arms at equal tokens (setup cost counted, G7), 3 or more seeds, same model, same items. Report mean and paired per-item difference with a bootstrap CI. Pilot every arm first so the environment arm is not weak (K19).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 exact-step ladder | arithmetic and enumeration at 4 number sizes | in-head prose vs code-executed | exact match per size | gap grows with size; PAL pattern 65.6 to 20.1 vs 61.5 |
| E2 scratch + code check | multi-step word problems | scratchpad only vs scratchpad + code recheck of each step | accuracy; slips fixed | fixes a large share of slips (46% of wrong chains were near-correct) |
| E3 self-critique vs execution | checkable tasks (code with tests, ARC with held-out grids) | self-critique round vs execution-feedback round | accuracy | self-critique at or below baseline; execution round above |
| E4 rule enforcement | rule-heavy puzzles (Hanoi isomorphs, constraint puzzles) | rules in prompt vs validator rejecting bad moves | violation rate; success | violations near zero in the validator arm |
| E5 bounded vs full view | long-file or long-state tasks | 30 / 100 lines / full; last 5 vs full history | accuracy; tokens used | middle sizes best; sizes may differ on our model |
| E6 probe vs commit | partially observed tasks | no probe; model-chosen probe; information-gain probe | accuracy; probe tokens | gain-chosen probe beats model-chosen; probing pays only on high-uncertainty items |
| E7 program log vs transcript | multi-step tasks over 10+ steps | full transcript vs program-held verified table rendered fresh | accuracy; tokens | log arm higher; effect grows with length |
| E8 editable vs fixed scratch | representation-sensitive items (ARC-like) | fixed template vs agent-edited scratch files | accuracy on transfer items | unknown; Martin and Schwartz predicts better transfer when adaptable |
| E9 fixed pipeline vs tool loop | repair tasks | program-owned pipeline vs model-chosen tools | accuracy; tokens | pipeline equal or better |
| E10 voice gate | mixed items split by single-pass rate | always-on voice vs gated at 45% vs single | accuracy | gate keeps the wins and drops the losses |
| E11 verification ablation | open-ended agent tasks | full loop vs loop without verification step | items completed | large drop (Voyager -73%) |
| E12 long procedure | Hanoi 8-15 disks | model emits move list vs model emits program the harness runs | exact-solution rate by N | program arm holds beyond N=8 |
| E13 weak vs strong | any above | harness on/off on a small and a larger model | accuracy | gain only on the stronger model (c18) |

## 9. What does not transfer, and why

- **Human load is not model load.** Humans have a small working memory and slow mental rotation; LLMs have a large context and exact language but poor arithmetic and drift. The mechanisms that carry over fix a measured model weakness (exact steps, stale context, no outside signal), not the human story. No LLM study measures load (b23).
- **Body and physical manipulation.** Martin and Schwartz's pie pieces and Tetris's physical rotation have no direct counterpart. The nearest analogues (editable workspace, cheap probes) are untested for LLMs.
- **Social setting.** Hutchins's team has different people with different tools and trained roles. Copies of one model share the same errors (G4). Multi-agent LLM setups do not reliably reduce load (b17, d03, d05, d07).
- **Offloading harms memory.** The phone and Google effects are weak and did not replicate (d16, d17, d18). They do not say a model's skill degrades when it uses tools. The Kosmyna memory cost (b18) is about humans and a small preprint.
- **Ethnography as proof.** Hutchins's ship is a case study without error counts (b22, d22).
- **2024 interface sizes.** SWE-agent's line counts and ablation sizes came from one old model and a single run per cell; later work reports higher scores with simpler setups (d08, d09).
- **Hanoi results as proof of limits.** Contested and format-dependent (c08, d02).
- **Vendor numbers.** Internal evals, model unnamed or table and text mismatch (d10, d11).

## 10. Open questions

1. Does an agent-editable workspace beat a fixed template at equal tokens? The Martin and Schwartz full text is unread (K16).
2. Which SWE-agent features carry the gain when replicated with variance and equal tokens (K04)?
3. Do epistemic probes help at equal tokens, and what gate predicts when probing costs more than it saves (K20)?
4. Does a program-held log beat the model rereading its own prose (K22)? Is there an agent analogue of the Kosmyna memory cost?
5. Does a harness help weak or small current models at all (K14)?
6. Does the Hanoi collapse survive when the model emits a program and the harness runs it at 8-15 disks (K15)?
7. Original effect sizes for Ward 2017 and Sparrow's own per-study rows are unread, so original-versus-replication pairs are missing.
8. Hutchins's calculator claim and any navigation error rate (K18).
9. Why did CoThinker lose on instruction following (0.95 vs 1.03), and is there a measured gate for it?
10. Why does shared memory help GPT5-Nano (62.36 vs 55.97 without) but hurt Qwen3-30B (76.41 vs 81.87 without)? Model strength, or context handling?

## 11. Sources

[V] opened and read this session (per the evidence lines). [M] snippet or abstract only.

- [V] Kirsh and Maglio 1994, On distinguishing epistemic from pragmatic action. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf
- [M] Kirsh and Maglio via PhilArchive, N=13 thesis note. https://philarchive.org/rec/KIRODE
- [V] Zhang and Norman 1994, Representations in distributed cognitive tasks (text garbled; p values partly missing). https://pages.ucsd.edu/~scoulson/203/zhang.pdf
- [V] Boldt and Gilbert 2019, Confidence guides spontaneous cognitive offloading. https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-019-0195-y
- [V] Risko and Gilbert 2016, Cognitive offloading. https://discovery.ucl.ac.uk/1508770/
- [V] Gilbert-lab, framing cognitive offloading as gains or losses (2022). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9288568/
- [M] Martin and Schwartz 2005 (abstract only; full text 403). https://doi.org/10.1207/s15516709cog0000_15
- [V] Stanford Encyclopedia of Philosophy, Embodied Cognition. https://plato.stanford.edu/entries/embodied-cognition/
- [V] Bazerman review of Hutchins 1995 (second hand). https://bazerman.education.ucsb.edu/sites/default/files/docs/Bazerman1995ReviewWildHutchins.pdf
- [M] Hutchins page snippet. https://pages.ucsd.edu/~ehutchins/citw.html
- [M] Hutchins 1995 full text (401). https://archive.org/details/cognitioninwild0000hutc
- [M] Wheeler 2013, Is cognition embedded or extended? https://storre.stir.ac.uk/bitstream/1893/13054/1/wheeler_cognition_embedded_extended_gestures_STORRE.pdf
- [M] Trninic, Kapur and Sinha 2020. https://europepmc.org/article/MED/32588486
- [M] Fyfe et al. 2014; Carbonneau et al. 2013 (not retrieved). https://doi.org/10.1007/s10648-014-9249-3
- [M] Morehead et al. 2019; Urry et al. 2020 on laptop notes. https://doi.org/10.1177/0956797620965541
- [V] Boettger, Poschik and Zierer 2023 brain drain meta-analysis. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10525686/
- [M] Ward et al. 2017 original. https://www.journals.uchicago.edu/doi/10.1086/691462
- [M] Replication of Ward et al., Acta Psychologica 2022. https://doi.org/10.1016/j.actpsy.2022.103717
- [V] Ruiz Pardo and Minda 2021 preprint. https://osf.io/preprints/psyarxiv/5y34g
- [V] Brain drain meta-analysis 2023 (abstract). https://osf.io/preprints/psyarxiv/tnyda
- [V] Google effects on memory meta-analysis 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10830778/
- [V] Hesselmann 2020, PeerJ. https://pmc.ncbi.nlm.nih.gov/articles/PMC7651475/
- [M] Sparrow replication PeerJ page. https://peerj.com/articles/10325
- [V] Camerer et al. 2018. https://www.nature.com/articles/s41562-018-0399-z
- [V] Wikipedia, Google effect (secondary). https://en.wikipedia.org/wiki/Google_effect
- [V] Kosmyna et al. 2025, Your Brain on ChatGPT. https://arxiv.org/abs/2506.08872
- [M] Guingrich et al. 2026, Belief Offloading. https://arxiv.org/pdf/2602.08754
- [V] Yao et al. 2023, ReAct. https://arxiv.org/abs/2210.03629
- [V] Nye et al. 2021, Scratchpads. https://arxiv.org/abs/2112.00114
- [V] Wei et al. 2022, Chain of thought. https://arxiv.org/abs/2201.11903
- [V] Gao et al. 2022, PAL. https://arxiv.org/abs/2211.10435
- [V] Schick et al. 2023, Toolformer. https://arxiv.org/abs/2302.04761
- [V] Yang et al. 2024, SWE-agent (abs and HTML v3). https://arxiv.org/abs/2405.15793 and https://arxiv.org/html/2405.15793v3
- [V] Xia et al. 2024, Agentless. https://arxiv.org/abs/2407.01489
- [V] mini-swe-agent README. https://github.com/SWE-agent/mini-swe-agent
- [V] Wang et al. 2023, Voyager (abs and HTML v2). https://arxiv.org/abs/2305.16291 and https://arxiv.org/html/2305.16291v2
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] Huang et al. 2024, Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Sumers et al. 2024, CoALA. https://arxiv.org/abs/2309.02427
- [V] Mialon et al. 2023, GAIA. https://arxiv.org/abs/2311.12983
- [V] Shojaee et al. 2025, The Illusion of Thinking. https://arxiv.org/abs/2506.06941
- [V] Lawsen 2025, Comment on The Illusion of Thinking. https://arxiv.org/abs/2506.09250
- [V] Cemri et al. 2025, MAST. https://arxiv.org/abs/2503.13657
- [V] CoThinker, United Minds or Isolated Agents (2025). https://arxiv.org/html/2506.06843v2
- [V] Cognitive Workspace (2025). https://arxiv.org/html/2508.13171v1
- [V] Hong et al. 2023, MetaGPT. https://arxiv.org/abs/2308.00352
- [V] Liu et al. 2023, Lost in the Middle. https://arxiv.org/abs/2307.03172
- [V] Packer et al. 2023, MemGPT. https://arxiv.org/abs/2310.08560
- [V] Externalization in LLM Agents (2026). https://arxiv.org/html/2604.08224
- [V] Sokoban and Tetris harness study (2025). https://arxiv.org/html/2505.15146
- [V] Annese et al. 2025, Who Sees What? https://arxiv.org/abs/2508.14564
- [M] Wang et al. 2025, Agents as Tool-Use Decision-Makers. https://arxiv.org/pdf/2506.00886v1
- [M] Unlu 2026, Know When to Trust the Skill (body unreadable). https://arxiv.org/pdf/2604.16753
- [V] Tran and Kiela 2026, single-agent vs multi-agent at equal thinking tokens. https://arxiv.org/abs/2604.02460
- [V] Kim et al. 2026, Towards a Science of Scaling Agent Systems. https://arxiv.org/abs/2512.08296
- [V] Wang et al. 2024, Rethinking the Bounds of LLM Reasoning. https://arxiv.org/abs/2402.18272
- [V] Zhang et al. 2025, Stop Overvaluing Multi-Agent Debate. https://arxiv.org/abs/2502.08788
- [V] Anthropic 2025, The think tool. https://www.anthropic.com/engineering/claude-think-tool
- [V] Anthropic 2025, Managing context. https://claude.com/blog/context-management
- [V] Laban et al. 2025, LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120
- [V] Hu et al. 2024, Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Cheng et al. 2025, MeCo adaptive tool use. https://arxiv.org/abs/2502.12961
