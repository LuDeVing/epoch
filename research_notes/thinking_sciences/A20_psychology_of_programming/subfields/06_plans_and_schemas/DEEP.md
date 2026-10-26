# Plans and schemas: deep document

*Subfield A20.06 of the psychology of programming. Focus: stereotyped code plans and their composition (Soloway and Ehrlich 1984). Built from evidence_a-d.jsonl (ids a01-a33, b01-b35, c01-c28, d01-d16), claims.jsonl (A20.06-K01 to K30) and critique.md in this folder. Where the critique corrected a number, the corrected number is used. Human evidence is mostly 1983 to 1994, small N, and the founding TSE 1984 paper was never opened. LLM evidence is 2021 to 2026, mostly on older models and HumanEval-style benchmarks.*

## 1. What it is

A programming plan is a stored chunk of knowledge about a stereotyped piece of code. It holds the critical facts of a common action sequence. Examples: a running-total loop, a counter, a skip guard, "read, then process, until a sentinel" (a01, a07).

Plans come in two kinds (a01):
- Control-flow plans: running-total loop, skip guard, search loop.
- Variable plans: counter variable, running-total variable. A variable is told apart by its role (what it holds and how it is updated), not by its syntax.

A plan is a frame with slots: variables, set-up, body, context. It links to other plans in two ways: specialization ("is a kind of") and implementation ("uses") (a07). A program is a tree of goals. Each leaf goal is met by a plan (a08).

Plan composition is how plans are combined: abutted (side by side), nested, interleaved, or merged (one piece of code serves two plans). Soloway and Ehrlich's key claim: what makes a program plan-like or unplan-like is not which plans it uses but how they are composed (a01, a02).

Why it matters for our agent. A plan is a solved subgoal stored with its role and context. Our schema has a planned subgoal library (SCHEMA section 5, marked [D]). This subfield says what an entry should hold, how experts retrieve and fall back, where stored plans cause errors, and what LLM studies measured when they reused solved parts.

Scope. Worked examples, functional decomposition, structure mapping, MDL on ARC, value of information and other neighbours are researched in parallel. They are linked in section 7, not covered.

## 2. History and theories in depth

### 2.1 Before plans (1976-1983)
- Shneiderman (1976): experts recall ordered programs better than novices, but the gap vanishes for scrambled lines. Adelson (1981): experts group program parts by function, novices by syntax. McKeithen et al. (1981) and Barfield (1986) found similar expert chunking (a27, a12). These are secondary summaries.
- Soloway, Bonar and Ehrlich (1983): people prefer a read-then-process loop plan. 80% of written English plans were read/process. A language whose loop fits that plan (Pascal-L with loop-exit-when) gave more correct programs than standard Pascal: 52% vs 33%. Experienced Pascal programmers shifted toward process/read, so training shapes the stored plan (a30, b01, b02). Only a synopsis was read; N is missing.

### 2.2 The founding work (1984)
- Soloway, Ehrlich and Gold (1984), "Reading a program is like reading a story". Defines plans and two composition rules that make a program unplan-like: (1) vary how typical the composed plans are, (2) bend a typical plan so it does double duty. Three versions of a sentinel-averaging program: A standard (read before WHILE, count guard), B less typical (REPEAT loop plus skip guard), C most atypical (counter and total initialised to -1 and -99999 to cancel the sentinel). Typicality was the authors' judgement, not measured on a corpus (a01-a04).
- Core experiment: fill in one blanked line. Advanced students (end of at least second semester, not experts), problem not stated. Plan-like Alpha: 37 correct, 10 incorrect (n=47). Unplan-like Beta (right answer Count := -1): about 5 correct and 41 incorrect (n about 46; the scan is garbled). Chi-square 47.7, p<0.001. Wrong answers were the typical plan value. Reading time about 2.3 min (Alpha) vs about 4.0 min (Beta), F(1,91)=4.60, p<0.05. Software metrics (lines, Halstead volume, nesting) predict the opposite, since Beta is shorter and flatter (a03, a04).
- Soloway and Ehrlich (1984, IEEE TSE): the full paper claims experts hold two kinds of knowledge, plans and rules of discourse (conventions such as names showing function). Experts do better on plan-like programs; novices show no such effect. Not opened. Per-group numbers unknown (a05, b28, d15). Detienne's later reading calls the participants "experts"; the opened 1984 text says advanced students (critique, correction 3).
- Soloway (1984) methodology note: observe programmers, find where they struggle, explain by knowledge structures, then design tools to fit (a31).

### 2.3 Plan failures and composition bugs (1985-1986)
- Spohrer, Soloway and Pope (1985), goal/plan analysis of buggy Pascal programs: bugs come largely from plan composition, especially merged plans that omit a subplan. Nine kinds of composition problem. PROUST reportedly finds about 75% of such bugs (snippet only, unverified). Not opened (a21, a22, b32).
- Letovsky and Soloway (1986), delocalized plans: plans compose by abutting, interleaving, nesting, merging. Recognition falls when a plan's lines are spread out. Protocol study: six maintainers (4 expert, 2 junior), 300-line Fortran 77, 15 routines. 3 of 6 finished the feature in 90 minutes. Local reading caused errors: NCHNGE=NCHNGE+1 copied into RESTORE (dirty-bit plan misread), IREC=0 in DELETE read as "not found" (it disabled a search cache). 4 of 6 visibly reacted to IREC=0. Documentation gave a variable's role, not its goal. Prescription (goal comments, comment non-normal updates) was not tested (a15-a17).
- Rist (1986): novices do not design top-down. They pick one goal, expand it locally, and build the program from goal solutions. 7 novices, 30 programs, about 50 hours of protocol. Focus on one goal makes the pieces but causes bugs when pieces are combined. Stage taxonomies: sum plan 6 stages, selection plan 5, read plan 9 fix types for the 99999 bug (a18, a19). Retrieved wrong plans occurred (a taught Y/N loop plan used where a sentinel was needed).

### 2.4 The retrieval and creation model (1989-1995)
- Rist (1989, 1991, 1995): plan retrieval is top-down and forward when a schema exists. Plan creation is bottom-up and backward from a focus line when none exists. Experts shift to retrieval but fall back to creation on hard problems. Rist's 1995 memory model indexes nodes by (role, goal, object) with four ports (use, make, obey, control) and was implemented as a Pascal generator. All second-hand (a20, b33).
- Detienne (1990 chapter): plan activation works both ways. Cues (a variable I of integer type, initialised I:=1) evoke Counter_Variable and predict I:=I+1. 269 production rules grouped into 47 general rules, from think-aloud studies, N not stated. Expectation errors: experts missed deviations when they strongly expected a value. Recall distortions: counter I recalled for J, while-not-V for repeat-until-V, a creation function that was never in the program. When no cue evokes a plan, experts execute code mentally (a09-a11, a14).
- Fix, Wiedenbeck and Scholtz (1993): 20 novices vs 20 experts (median 7 years) studied a 135-line Pascal program for 15 minutes. Complex plan labels (of 4): experts 3.7, novices 1.7, F(1,38)=57.58. Simple plans: 4.0 vs 3.7, n.s. Experts also described procedure goals better (5.2 vs 2.8 of 7) and methods (2.90 vs 0.85 of 4). No gap on overall program goal (6.15 vs 5.50) (a24, a25).

### 2.5 Challenges
- Pennington (1987): control-flow units form the first representation. Function and plan knowledge appears later, with more time or a modification goal. 80 and 40 professional programmers (DTIC snippet only). Detienne's reconciliation: schemas can also hold syntactic units; the mix depends on language, task and reader (a12, a13).
- Gilmore and Green (1988): the expert advantage with plan structure may depend on notation (direction unverified). Davies (1990): programmers with design training use plan cues, so plan use may come from design training, not expertise alone. Vessey (1987): knowledge structures vary a lot and are not standard scripts (a26, b29).
- Burkhardt, Detienne and Wiedenbeck (1997): plan models were built on short procedural programs. In object-oriented code a plan spans several classes. Detienne (1995): N=8 professionals; the hypotheses about OOP beginners were not supported (a28, a29).

### 2.6 Rainfall and its replications (1986-2020)
- The Rainfall problem (average the non-negative numbers before a sentinel 99999) became the standard composition task. Soloway cited: under 60% of first- and second-term novices finished any of three loop programs (b05).
- Ebrahimi (1994): 20 LISP students: 50% missing if-guards, 40% misplaced updates, 40% malformed updates, 40% spurious output (second-hand, b30).
- Simon (2013): 149 C# students, input given in a structure: 36% no pertinent code, 40% ignored negatives, 0% guarded the division (second-hand via Fisler, b31).
- Fisler (2014), functional-first CS1: 218 solutions, five courses, four schools. Of 187 with a clear structure: Clean First 87, Single Loop 38, Clean Multiple 43. Only 5% (12 of 218) had no evident plan; 14% unclear. Between-task composition errors: 25 in all data, 3 in clear-structure solutions. Zero-error share: Single Loop 74%, Clean First 66%, Clean Multiple 46%. A Java arrays course (N=51): 50 single loop. Fisler ties structure to what was taught. The re-check download failed, so numbers stand as recorded (b06-b10, d16).
- Fisler and Castro (2017): 13 talk-alouds (4 narratives), Racket, week 7. Students pick the schema they know best and cannot adapt it (d14, b11, b12). Castro and Fisler (2020): 22 think-aloud participants. Students who moved back and forth between naming tasks and writing code ended near-correct. None of the code-only or one-way students got correct solutions. Stuck students did not return to the taught design steps (b13-b15).
- Fisler, Krishnamurthi and Siegmund (2016) modernised plan-composition tasks (c18). Crichton et al. (2021): structures can be classified automatically, up to 91% accuracy with 108 training programs (d06).

### 2.7 The LLM turn (2022-2026)
Plans reappear as: model-written plans (Self-planning, SCoT, PlanSearch), decomposition with tests (Parsel), libraries of solved parts (CodeChain, ReGAL, LILO, DreamCoder), skill and workflow memory (Voyager, AWM, Buffer of Thoughts), plan recognition (Demirtas), and plan checking (Rivera, LPW). See section 6.

## 3. Core findings with exact numbers

Status: established = two or more independent sources; single = one source; contested = sources disagree. Human data is 1983-1994 unless noted.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Plan-like programs are easier to complete than unplan-like (fill-in-the-blank, advanced students) | Alpha 37/47 correct; Beta about 5/46 (garbled scan); chi-square 47.7, p<.001; wrong answers are the typical plan value | Soloway, Ehrlich, Gold 1984 (a03, a06) | single, no replication found |
| Unplan-like is slower to read | about 2.3 vs 4.0 min; F(1,91)=4.60 | same (a04) | single |
| Expert-novice gap only on non-trivial plans | complex labels 3.7 vs 1.7 of 4, F(1,38)=57.58; simple 4.0 vs 3.7 n.s.; N=20+20 | Fix et al. 1993 (a24, a25) | established (with Davies, Rist) |
| Experts retrieve top-down when a schema exists, create bottom-up when not | Icon: 3 of 5 built bottom-up, all 3 worked; find-A plan retrieved forward more than any other | Scholtz, Wiedenbeck 1992; Rist; Detienne 1995 (b03, b04, b33, a29) | established in direction, tiny N |
| Strong expectation causes missed deviations and recall distortion | I recalled for J; while-not for repeat-until; N not given | Detienne 1990 (a10, a11) | single |
| Composition is the main source of novice bugs | several hundred bugs, over 200 programs; PROUST about 75% (unverified) | Spohrer et al. 1985 (a21, a22) | contested |
| Composition errors rare in a functional-first course | 3 of 187 clear-structure solutions; 5% no plan; Simon 36% no pertinent code | Fisler 2014 (b06, b08, b09) | contested |
| Chosen structure follows teaching | Clean First 87, Single Loop 38, Clean Multiple 43 of 187; Java 50/51 single loop | Fisler 2014 (b07, b10) | single |
| Language fit to preferred plan raises correctness | 52% vs 33%; 80% read/process | Soloway, Bonar, Ehrlich 1983 (a30, b01) | single, N missing |
| Cycling between task naming and code goes with near-correct solutions | 22 participants; no one-way student correct | Castro, Fisler 2020 (b13) | single |
| Control flow may come first, plans later | Study 1 N=80, Study 2 N=40 (snippet) | Pennington 1987 (a13) | contested |
| Self-planning beats direct and code CoT | HumanEval Pass@1 48.1 / 53.9 / 60.3; ground-truth plan 74.4; MBPP 49.8 / 54.5 / 55.7 / 65.1 | Jiang 2023 (c01, c02, b18) | established (SCoT, PlanSearch, LPW agree in direction) |
| Plan gain grows with difficulty | complexity 1: 65.2 to 71.2; complexity 3: 31.1 to 50.2 | Jiang 2023 (c03) | single |
| Planning hurts small models | 6.7B: direct 34.0, self-planning 30.1; 13B: 48.1 vs 50.0 | Jiang 2023 (b19) | single |
| Plan delivery matters | multi-turn 28.2, one-phase 62.8, two-phase 60.3; zero-shot CoT one phase 18.0 vs two-phase 50.6 | Jiang 2023 (c04) | single |
| A fixed small plan vocabulary beats free text | SCoT 60.64 vs CoT 53.29 (HumanEval, ChatGPT); no structures 55.67; no IO 59.65; pseudocode 55.23 | Li 2023 (b20, c05, c06) | established (two models, three benchmarks) |
| Plan search beats repeated sampling at pass@200; often lowers pass@1 | pass@1 / pass@200 / PlanSearch@200: GPT-4o-mini 39.0/53.3/64.9; GPT-4o 41.3/60.6/73.0; DeepSeek-Coder-V2 41.4/53.2/70.3; Claude 3.5 Sonnet 40.3/55.6/77.0 | Wang 2024 (b22) | established in direction |
| The idea is the bottleneck | 10-token sketch helps; per-sketch solve rates near 0 or 100% | Wang 2024 (b21, c12) | single paper, oracle |
| Compose-and-test gives the gain, not the plan alone | Parsel 25.5% vs 6% for same plans straight to Python (100 APPS problems), strict subset; APPS 14.5 to 25.5; HumanEval GPT-4 67 to 85 | Zelikman 2023 (b27, c07, c08) | single |
| Fixed flow beats one prompt | AlphaCodium GPT-4 pass@5 19% to 44% | Ridnik 2024 (b23) | single |
| Reusing solved sub-modules helps, more for weaker models | CodeChain APPS 22.33 to 30.24; competition 5.42 to 12.38; centroid sub-modules 35.11 vs random whole 30.16; ReGAL CodeLlama-13B LOGO +11.5, Date +26.1; GPT-3.5 Date +1.3 | Le 2024; Stengel-Eskin 2024 (b24-b26, c09, c10, c13) | established |
| Anonymous library entries hurt; names and docs restore | change vs baseline: REGEX -30.60, CLEVR -2.91, LOGO -11.11; AutoDoc +9.73, +2.27, +0.00 | Grand 2024 LILO (d08, c14) | single |
| Verified skill memory helps agents | Voyager wooden 6+-2 vs 92+-72 (AutoGPT); no library: iron 29+-11 vs 21+-7, diamond 0/3; AWM WebArena 23.5 to 35.5 | Wang 2023; Wang 2024 (c19, c20, c26) | established |
| Wrong induced workflows can hurt | Mind2Web cross-task step success 36.2 to 45.1 but action F1 60.6 to 57.3 | AWM (d09) | single |
| Retrieval helps where the model lacks knowledge | ODEX-hard +20.3 to +40.1; DeepSeekCoder-7B no gain on MBPP | CodeRAG-Bench (d07) | established with ReGAL |
| LLMs recognise classic plans in student code | micro-F1 GPT-4o 0.778, rules 0.588, kNN 0.550; with syntax errors 0.726 vs 0.178; passers use plans 77.17% vs 61.40% | Demirtas 2025 (a32, c16, c17) | single |
| LLM composition collapses with depth; worked composition repairs synthetic tasks | DP 72.0 to 98.0; 82.3% of right multiplication answers had a graph error | Chen 2024; Dziri 2023 (c23, c24) | contested |
| Self-feedback limits repair | GPT-4 feedback 33.30% vs human 52.60% overall | Olausson 2024 (c28) | single |
| Changed convention collapses models | 1-based HumanEval subset (53 tasks): GPT-4 82.5 to 40.5; GPT-3.5 68.9 to 25.1; Claude 47.6 to 15.7 | Wu 2023 (d01) | single, indirect |
| Likely-bug context ruins completion | CodeGen-2B 54.9% to 3.1% | Dinh 2023 (d02) | single, indirect |
| Wrong hints cost frontier models | CodeCrash drop 23.2% (13.8% with CoT), 2-3x reasoning tokens; XYEval up to 46.7%, SWE-bench Verified Claude 90.0 to 75.5 | Lam 2025; Wu 2026 (d03, d04) | established (hints, not plans) |
| Plan-to-code checking fills in missing plan parts | 12 of 13 false-positive plans scored 0/5 or 1/5; one plan 4/5 then 0/5; cost over USD 200 | Rivera 2024 (b16, d05) | single |
| At equal tokens, many cheap samples with a check beat one long thought, except code pass@1 | o1 high 29.1% at USD 1,400 vs low 27.3% at 43% less cost | Ma 2025; Cuadron 2025 (d10, d11) | established |
| Up-front planning alone misses implementation issues | 61.0 to 70.3; no-upfront ablation -2.8 (trained 7B) | Think Anywhere 2026 (d12) | single, needs training |

## 4. Mechanisms and models

### 4.1 Plan frame (Detienne, Rist)
A library entry should hold:
- A short semantic name and a goal sentence ("keep a running count of valid items").
- The role of each variable (counter, accumulator, flag).
- Slots: init, update, guard, loop context, exit condition.
- Links: "is a kind of" and "uses". Example: Running_Total_Loop specializes into total-, counter- and new-value-controlled forms (a07).
- More than one filler per goal (fixation evidence, K30).
- Provenance: verified by run or not, and how often it helped.

### 4.2 Retrieval and creation (Rist)
- Index nodes by (role, goal, object). A cue like (find, average, rainfall) retrieves nodes (a20).
- If a node matches, expand it in execution order, forward (top-down).
- If none matches, pick the focus goal, write that code first, and grow outward as new goals appear (bottom-up, backward).
- Experts fall back to creation on hard or unfamiliar problems. For a far language, bottom-up beat whole-plan recall (b04, tiny N).
- Implementation: a router in code. Library hit above a similarity threshold means expand the stored plan. No hit means seed from the focus goal. Compare with always-top-down (T4).

### 4.3 Two-way activation and its risk (Detienne)
- Bottom-up: cues (names, types, initialisations) evoke a plan. Top-down: the evoked plan predicts missing parts (update, guard, loop context).
- Risk: the prediction replaces what is on the page (I recalled for J). Implementation: code tags every value that came from the plan's prediction as "expected". The model must point to the line that confirms it, or the value is tested by a run.
- Experts check plan interactions by simulation (a14). The check should be a run, not a re-read.

### 4.4 Composition rules (Soloway, Letovsky)
- Composition kinds: abut, nest, interleave, merge. Merged plans omit a subplan more often (a21).
- A plan is a rewrite rule from goal to subgoals when writing code, reversible when reading (a15).
- Practical check: after composing, list each plan's slots and mark every variable written by more than one plan (a "non-normal update"). Run a case where each plan alone would give a different value. Non-normal updates are where delocalized plans hide (a17).

### 4.5 Plan-then-implement with checks
- Self-planning: numbered plan, then code, in separate phases. Two-phase 60.3 vs multi-turn 28.2 (c04).
- SCoT: plan in a fixed vocabulary of sequence, branch, loop, plus input-output (c05, c06).
- Parsel: tree of function descriptions; several implementations per function; tests pick a combination (c07).
- PlanSearch: list observations about the problem, build plans from them, code each plan (b22). The pass@200 numbers need about 200 samples.
- LPW: check the plan against visible tests first, then use the verified plan for repair (c22, abstract and method only).
- ADaPT: split a step further only when the executor fails (c27, abstract only). This matches G1.

### 4.6 Solved-subgoal library mechanics
- Write only after a run confirms success (Voyager, AWM, ReGAL). Refactor into helpers and check outputs are unchanged (ReGAL). Cluster sub-modules across samples and keep centroids (CodeChain).
- Document each entry with a name and role sentence (LILO AutoDoc).
- Order matters: ReGAL random curriculum cost 18.7 points on LOGO; Voyager random curriculum cut unique items by 93%.
- Prune and edit: ReGAL ablations without pruning or editing were lower by 2 to 9 points on TextCraft and Date.
- Retrieval: dense retrievers beat BM25 on code (d07). Tree-edit distance works with few examples but confuses plans that differ in where filtering happens (d06). No head-to-head of role text vs code vs label exists.

## 5. What holds up

### 5.1 Replications
- The 1984 fill-in-the-blank effect has no human replication in this folder. Fix 1993 and Detienne's recall errors agree in spirit but are not repeats. Davies and Vessey qualify the story.
- Rainfall shows difficulty depends on population and teaching: Simon (2013) 36% no pertinent code; Fisler (2014) 5%. "Composition is the main bug source" is not universal.
- No LLM replication of the Soloway task. Only indirect analogues (d01-d04).

### 5.2 Meta-analyses
None on plans in programming. Reviews (Robins 2003, Bidlake 2020 appendix) call evidence on plan teaching thin (a23).

### 5.3 Failures and moderators
- Expertise: the effect shows for complex plans only (a24).
- Language and notation: plan preference changes with language (a30); Gilmore and Green suggest partial artifact (unverified).
- Teaching: the structure chosen follows what was taught (b07, b10); students stay with the pattern they know (d14).
- Paradigm: plan theory fits OOP only in part (a28, a29).
- Task: control flow first for some tasks (Pennington).
- Model size: planning lost 3.9 points on a 6.7B model (b19). Library gain shrinks with a stronger model: ReGAL Date +11.5 for CodeLlama-13B vs +1.3 for GPT-3.5 (b26). Retrieval helps where knowledge is missing (d07).
- pass@1 vs pass@k: plan search lowers pass@1 for some models (b22). CoT Pass@10 68.6 is below direct 75.0 (b19). SCoT gain at Pass@5 falls to 2.38% (b20).
- Oracle effects: ground-truth plan 74.4 comes from reference code (c02). Sketch results come from back-translated passing code (c12).

### 5.4 Interventions that worked
- Two-phase plan then code (c04). Fixed plan vocabulary (c06). Compose-and-test (c08). Verified library with names and docs (c13, d08). Execution-gated skill commit (c20). LLM plan-to-code feedback for students: median 4 and 2 submissions vs 1 without feedback (d05).
- Naming the exact distractor beat a generic warning (d04).
- Cycling between task-level and code-level thinking in humans, correlational (b13).

### 5.5 Interventions that did not work, or hurt
- Modular prompting alone, without the revision loop (b24).
- Anonymous library abstractions (d08). Random curricula (c13, c20).
- Plans translated straight to code: 6% vs 25.5% (c08).
- Self-repair on self-feedback: marginal at equal budget (c28).
- A generic warning about bad advice: only partial (d04).
- Explicit plan teaching: no clean trial (a23, b34).
- Unverified induced workflows: AWM action F1 fell in all three Mind2Web splits while step success rose (d09).

### 5.6 Contradictions left open
- Plans first (Soloway, Detienne) vs control flow first (Pennington).
- Composition as main bug source vs Fisler's 3 of 187.
- Planning helps vs lowers pass@1 or diversity in places, and hurts small models.
- Composition collapses with depth (Faith and Fate) vs near-perfect after a worked composition (SKiC). Different tasks and old models.

## 6. Language models

### 6.1 Plan-then-code on code models
- code-davinci-002, HumanEval Pass@1: direct 48.1, few-shot 52.6, CoT 53.9, self-planning 60.3 (+25.4% relative), ground-truth plan 74.4. Pass@10: 75.0 / 68.6 / 76.3 / 89.1. MBPP-sanitized: 49.8 / 54.5 / 55.7 / 65.1 (c01, c02, b19). The MBPP gain over few-shot is about 2 points.
- By difficulty, gain over direct: +6.0 (complexity 1), +19.1 (2), +19.1 (3) (c03).
- ChatGPT, structured CoT vs CoT: HumanEval 60.64 vs 53.29, MBPP 46.98 vs 41.83, MBCPP 57.06 vs 53.51. Codex 49.82 vs 43.79 (c05).
- All on old models. Whether a current reasoning model still gains is not measured (section 10).

### 6.2 Searching over plans
- PlanSearch numbers are in section 3. The critique corrects c11: Claude 3.5 Sonnet is 40.3 pass@1 and 55.6 repeated-sampling pass@200; 41.4 and 60.6 belong to DeepSeek-Coder-V2 and GPT-4o. With public-test filtering PlanSearch reached 77.1% after 20 submissions.
- MapCoder (recall similar problems, plan, code, debug): dropping debugging loses 17.5 points, dropping planning 16.7 on average (c21). All roles are prompts of one model; recall was not isolated.
- AlphaCodium: 19% to 44% pass@5 (b23).
- LPW with GPT-4o: HumanEval 98.2, MBPP 84.8, LiveCode 59.3 (c22).
- Cost: PlanSearch needs about 200 samples. Equal-token comparisons are mostly missing.

### 6.3 Compose, reuse, remember
- Parsel, CodeChain, ReGAL, LILO, DreamCoder (3.7% to 79.6% on text editing, no LLM), Voyager, AWM, BoT. Numbers in section 3.
- Library gain shrinks as the model gets stronger (b26, d07). Wrong entries harm (d09). Names matter (d08).
- Voyager without the library: early speed similar (iron 29+-11 vs 21+-7), later stages plateau (diamond 0/3) (c19, c20).
- BoT: +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One, authors' runs, abstract level (c25).

### 6.4 Recognition and composition
- Plan recognition in student code: GPT-4o 0.778 vs AST rules 0.588; with syntax errors 0.726 vs 0.178. Models over-predicted a plan instead of UNKNOWN (a32, c16, c17).
- Composition: accuracy falls toward zero with graph size on GPT-3, ChatGPT, GPT-4 (Dziri). SKiC repairs synthetic tasks (DP 72.0 to 98.0; last-letter 72.5 to 100.0; GSM8K 73.0-74.4 to 86.9-87.8; MATH only to 40.6) (c23, c24).
- Rainfall: Codex on seven wordings, 350 programs, average near 50%, weak on empty input. No plan-structure coding (d13).

### 6.5 Expectation and bad hints
- 1-based indexing, 53-task HumanEval subset: GPT-4 82.5 to 40.5, GPT-3.5 68.9 to 25.1, Claude 47.6 to 15.7, PaLM-2 29.2 to 7.4. Full 164 tasks GPT-4 87.4 to 68.2 (d01).
- Buggy context: CodeGen-2B 54.9% to 3.1%; below 5% for all variants tested; matching-bug completions in about 90% of instances (d02).
- CodeCrash: 17 LLMs, 1,279 questions, drop 23.2% (13.8% with CoT); reasoning models spent 2 to 3 times the tokens on plausible wrong hints; raising o3-mini effort made the drop worse (d03).
- XYEval, five 2026 models, six suites: up to 46.7% relative drop (Gemini 3.1 Pro Terminal-Bench 67.4 to 36.0); Claude on SWE-bench Verified 90.0 to 75.5 (-16.1%); models were more susceptible on easier benchmarks. One model gained 2.4% on SWE-bench Pro. Naming the exact distractor helped much more than a generic warning (d04).
- These are hints in a user turn or comments, not retrieved plans. A retrieved wrong plan should pull the same way, but nobody measured it.

### 6.6 Does thinking already plan?
- NoThinking: under about 3,000 tokens, many cheap samples beat one thought at every k. On LiveCodeBench Thinking stayed ahead at pass@1 (d10).
- Overthinking: reasoning models had overthinking scores nearly three times higher; o1 high 29.1% at USD 1,400, low 27.3% at 43% lower cost; choosing the lowest-overthinking of two runs gave 30.3% with 15% less compute (d11).
- Think Anywhere: up-front planning misses issues found during implementation; trained 7B 61.0 to 70.3, no-upfront ablation 66.6 against 69.4 (d12).
- So on current reasoning models an explicit plan stage may add little. Untested at equal tokens.

### 6.7 Plan checking
GPT-4 as a plan-to-code translator gives false positives because it fills in details. Removing the problem statement from the prompt cut them. 13 wrong plans passed, 12 of them with 0/5 or 1/5 tests. One plan scored 4/5 then 0/5. Over USD 200 for two feedback rounds (d05).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Library entries are written only after a run confirms success on an unfitted check (G3). No unverified plans stored. | memory, G3 | [E] | c20, c26, c13, d09, K16 |
| A2 | Spend library entries on non-trivial plans only. Skip counter-level plans. | memory | [E] | a24, a25, K02 |
| A3 | Retrieve first; when nothing matches, create bottom-up from a focus goal. Never force top-down. | S1, memory | [E] in direction | b04, b33, a29, K03 |
| A4 | Where a plan step is used, ask for a short numbered plan in a small fixed vocabulary (sequence, branch, loop, input-output), in a phase separate from code. | O3 | [E] on older models | b18, b20, c04, c06, K10, K12 |
| A5 | Expect the library gain to depend on the tier: little on tasks the model already solves, more on hard tiers and weaker models. Measure per tier before keeping it. | G7, G12, memory | [E] | b26, d07, K15, K26 |
| A6 | Any stored plan or hint enters as a marked hint, never as part of the task text, and is checked by a run before it is trusted. | S1 (input hygiene), G2, G3 | [E] for hints in general | d03, d04, K24 |
| A7 | At equal tokens, prefer several short attempts with a check over one long plan, except code at pass@1. | G11 | [E] | d10, d11, K27 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Name and role sentence on every entry (A/B vs anonymous) | memory | [S] | d08, K25 |
| T2 | Retrieval key: role sentence vs code text vs LLM plan label | memory | [S] | d08, d06, a32, K25 |
| T3 | Plan slots (role, init, update, guard) vs free-prose plan | O3, memory | [S] | b20, a01, a07, K12, K21 |
| T4 | Route by library hit (retrieve vs create bottom-up) vs always top-down | S1 | [S] for agent gain | K03 |
| T5 | Wrong stored plan with vs without a run-and-compare check | G2, G3 | [S], rate unmeasured | d09, d03, K24 |
| T6 | Compose-and-test step vs plan translated straight to code | O3 | [S] | c08, b24, b23, K14 |
| T7 | Plan-if-hard vs plan-always | G12, S0 | [S] | c03, b19, K11 |
| T8 | Re-plan trigger during coding vs plan-once | S5, S6 | [S] | d12, c27, K28 |
| T9 | Run stored plans from plan text alone, 3 runs, keep 2 of 3 | memory, G3 | [S] | d05, K29 |
| T10 | Plan-like vs unplan-like fill-in, with and without a retrieved plan hint | G (new guardrail) | [S], indirect | d01, d02, a03, K04, K23 |
| T11 | Interleaved vs abutted composition error rate | O3 | [C] | a21, b08, K05, K06 |
| T12 | Worked composition example vs none at rising depth | O3 | [C] | c23, c24, K18 |
| T13 | Two or more variants per goal, chosen against constraints | memory | [S] | d14, K30 |
| T14 | Alternate plan-naming and code steps vs plan-then-code | S, O | [S] | b13, K08 |
| T15 | Tool whose call order matches the natural plan vs reversed | O (interface) | [S] | a30, b01, K09 |
| T16 | Plan search (N plans) vs N code samples at equal tokens on the agent's model | O3 | [E] on old models | b22, K13, K27 |
| T17 | Control-flow trace stored beside the plan label | memory | [C] | a13, K20 |

Links to subfields researched in parallel (not covered here): worked-example research (T12), functional decomposition (O3), structure mapping and MDL program synthesis on ARC (library of solved parts), value of information and expected value of control (T7), problem-solution co-evolution and anomaly response (T8), outside view and base rates (T5 rates), cue overload and fan effect (large libraries), attentional capture and bias (T10), question wording and presupposition (hint framing in T5, T10), generation versus evaluation (T9).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, including library build and retrieval cost (G7). Report pass@1 and pass@k, per tier, with at least 3 seeds. Log per SCHEMA section 6.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Library on/off (A1, A5) | solved-subgoal tasks in easy and hard tiers (coding items, ARC-style program items) | no library; verified library; verified plus unverified entries | pass@1, tokens, harm rate (right to wrong) | verified: small gain on hard tier, none on easy; unverified: harm on some items |
| B2 Retrieval key (T2) | one library, one task set | role sentence; code text; LLM plan label | retrieval hit rate, downstream pass | role sentence or label beats code text when wording differs; size unknown |
| B3 Names (T1) | one library | anonymous entries; named entries with role sentence | pass rate | named wins; LILO shows -3 to -31 points for anonymous |
| B4 Plan slots (T3) | coding items, mid difficulty | free-prose plan; slot plan | pass@1 | +2 to +6 points; SCoT gave +7.3 on old models, likely smaller on a strong model |
| B5 Wrong stored plan (T5) | 20 tasks, one planted wrong plan each | no check; run-and-compare before use | pass rate, tokens | no check loses 14 to 23% relative (CodeCrash scale); check removes most of the loss |
| B6 Soloway fill-in (T10) | canonical vs bent programs (Count := -1 style) | no hint; plan hint; plan hint plus simulate-the-interaction check | rate of default-value answers | hint raises default answers on bent programs; the check lowers them |
| B7 Plan-then-code vs direct vs best-of-N vs plan search (T16) | our coding items | direct; plan then code; N plans; best-of-N code | pass@1, pass@k | on a reasoning model, plan gain near zero at pass@1; plan search helps at k above 1 |
| B8 Plan gate (T7) | mixed difficulty | plan-always; plan-if-hard (from S0 estimate) | pass at equal tokens | plan-if-hard wins by saving tokens on easy items |
| B9 Re-plan trigger (T8) | multi-step coding items | plan-once; re-plan on failed test or surprise | pass rate | gain on items where the first plan misses implementation issues |
| B10 Interleaved vs abutted (T11) | same subgoals composed two ways (Rainfall variants) | plain; slot check of shared variables | composition error rate | interleaved has more errors; tells us if composition is a weak spot at all |
| B11 Variants per goal (T13) | tasks with a constraint that rules out the default variant | one variant; two or more | pass rate | more variants win only on constraint-breaking items |
| B12 Plan execution check (T9) | stored plans run from text alone | single run; 3 runs keep 2 of 3 | false-positive rate of stored plans | fewer false stored plans, more tokens |
| B13 Worked composition (T12) | tasks of rising composition depth | none; worked composition in context | accuracy by depth | gain grows with depth |
| B14 Compose-and-test (T6) | decomposable tasks | plan to code directly; plan, parts, tests, compose | pass rate | compose-and-test wins (Parsel 25.5 vs 6 on old models) |

## 9. What does not transfer, and why

- The human memory story. Plans chunk information for limited human memory. A language model has no such limit in the same form. The benefit is about steering and cost, not capacity.
- Expert-novice contrast. It was drawn from students and professionals on short Pascal programs. An LLM has no expertise axis in this sense. Model strength plays the role, and it runs the other way: the weaker the model, the more a library helps, yet the smallest models may lose from planning (b19, b26).
- Rainfall results. They depend on the course and the I/O form (Simon vs Fisler). They do not predict LLM weak points. The only LLM data (Codex, near 50%, weak on empty input) was not coded for structure (d13).
- Plan-like vs unplan-like as a trained expectation. The human effect came from years of seeing typical code. In an LLM the analogue is the pretraining prior. Indirect evidence says the pull is strong (d01, d02) but the human effect size does not carry over.
- Delocalization. Humans read local lines. A model reads the whole file in context. Delocalization may matter less for short context and more for a large codebase. Untested.
- Reading times (2.3 vs 4.0 min). The only cost for us is tokens.
- Teaching plans to students. This is a curriculum issue, not a scaffold one. Library entries are not a course.
- Old-model gains. Gains of 7 to 25 points came from Codex-era models. Current models already plan in their thinking (d10, d11).
- Think Anywhere needs training, so it is not a scaffold result. Only the lesson (re-plan during coding) transfers.
- 1984 materials. Typicality was the authors' judgement. Our agent could measure typicality on its own library.

## 10. Open questions

1. Does a library of stereotyped plans (role, init, update, guard) beat free planning on a current strong model at equal tokens? No direct test (K15, K26).
2. Does an LLM show the plan-like vs unplan-like effect? The Soloway fill-in has not been run on a model.
3. What are the token cost and the pass@1 vs pass@k tradeoff of plan search on 2025-2026 reasoning models?
4. Is composition a real failure source for LLMs? No Rainfall study with structure coding exists.
5. Which retrieval key works best: role text, code text, or LLM plan label (Demirtas micro-F1 0.778)?
6. How often does a wrong stored plan hurt, split by verification strength?
7. What do Soloway and Ehrlich 1984 TSE and Spohrer 1985 report exactly? What is the basis for PROUST's 75%?
8. Does explicit plan teaching or prompting help humans or models on transfer (de Raadt not opened)?
9. Do plans transfer across paradigms (Burkhardt, Detienne 1995, N=8)? Should entries be paradigm-neutral?
10. What are the real numbers in Gilmore and Green (1988) and Pennington (1987)? Do they weaken the role-slot design?
11. Fisler 2014 and Voyager numbers should be re-checked against the PDFs.
12. Does a plan stage help on top of a model that already thinks?

## 11. Sources

[V] = opened and read this session. [M] = snippet or second-hand only.

Human studies and reviews
- [V] Soloway, Ehrlich, Gold (1984) Reading a program is like reading a story. https://journalpub.escholarship.org/cognitivesciencesociety/article/30320/galley/20174/download
- [M] Soloway and Ehrlich (1984) Empirical studies of programming knowledge, IEEE TSE SE-10(5). https://doi.org/10.1109/TSE.1984.5010283
- [V] Detienne (1990) Expert programming knowledge: a schema-based approach. https://arxiv.org/pdf/cs/0702003
- [V] Detienne (1995) Design strategies and knowledge in object-oriented programming. https://arxiv.org/pdf/cs/0612008
- [V] Burkhardt, Detienne, Wiedenbeck (1997) Mental representations constructed by experts and novices in object-oriented program comprehension. https://arxiv.org/pdf/cs/0612018
- [V] Letovsky and Soloway (1986) Delocalized plans and program comprehension. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/letovsky-1986-software.pdf
- [V] Rist (1986) Focus and learning in program design. https://journalpub.escholarship.org/cognitivesciencesociety/article/30492/galley/20341/download
- [M] Rist (1989, 1991, 1995) plan retrieval and creation models (through Scholtz and Wiedenbeck, Robins)
- [V] Robins, Rountree, Rountree (2003) Learning and teaching programming. https://www.cs.auckland.ac.nz/courses/compsci747s2c/lectures/robins-learning-cse-03.pdf
- [M] Spohrer, Soloway, Pope (1985) A goal/plan analysis of buggy Pascal programs. https://dl.acm.org/doi/10.1145/317456.317465
- [V] Fix, Wiedenbeck, Scholtz (1993) Mental representations of programs by novices and experts. https://www.cs.kent.edu/~jmaletic/cs69995-PC/papers/fix-1993.pdf
- [V] Bidlake et al. (2020) Online appendix, systematic review of program comprehension. https://www.cs.unb.ca/~lbidlak1/ExtendedOnlineAppendix.pdf
- [V] Soloway, Bonar, Ehrlich (1983) Cognitive strategies and looping constructs (synopsis only). https://research.cs.queensu.ca/home/cordy/cisc860/Biblio/drb/CS/soloway83.pdf
- [V] Soloway (1984) A cognitively-based methodology (reviewer abstract only). https://research.cs.queensu.ca/home/cordy/cisc860/Biblio/hurd/misc/soloway84.pdf
- [V] Scholtz and Wiedenbeck (1992) Novice programmers learning a second language. https://ppig.org/files/1992-PPIG-4th-Scholtz.pdf
- [V] Fisler (2014) The recurring rainfall problem (numbers as recorded; the re-check download failed). https://cs.brown.edu/~kfisler/Pubs/icer14-rainfall.pdf
- [V] Fisler and Castro (2017) Sometimes, Rainfall accumulates. https://cs.brown.edu/~kfisler/Pubs/icer17-rainfall.pdf
- [V] Castro and Fisler (2020) Movements between task-level and code-level thinking. https://cs.brown.edu/~kfisler/Pubs/castro-fisler-sigcse2020.pdf
- [V] Fisler, Krishnamurthi, Siegmund (2016) Modernizing plan-composition studies. https://www.se.cs.uni-saarland.de/publications/docs/FKS16.pdf
- [V] Crichton, Sampaio, Hanrahan (2021) Automating program structure classification. https://arxiv.org/abs/2101.10087
- [M] Pennington (1987); Gilmore and Green (1988) https://doi.org/10.1080/02724988843000005; Ebrahimi (1994) https://doi.org/10.1006/ijhc.1994.1069; Simon (2013) https://doi.org/10.1109/latice.2013.44; de Raadt et al.; Ginat, Menashe, Taya (2013); all through citing papers
- [M] Adelson 1981, Shneiderman 1976, McKeithen 1981, Barfield 1986, Davies 1990, Vessey 1987 (through the Bidlake appendix and Detienne)

LLM and AI studies
- [V] Jiang et al. (2023) Self-planning code generation. https://arxiv.org/abs/2303.06689
- [V] Li et al. (2023) Structured chain-of-thought prompting. https://arxiv.org/abs/2305.06599
- [V] Wang et al. (2024) Planning in natural language improves LLM search (PlanSearch). https://arxiv.org/abs/2409.03733
- [V] Ridnik et al. (2024) AlphaCodium. https://arxiv.org/abs/2401.08500
- [V] Zelikman et al. (2023) Parsel. https://arxiv.org/abs/2212.10561
- [V] Le et al. (2024) CodeChain. https://arxiv.org/abs/2310.08992
- [V] Stengel-Eskin et al. (2024) ReGAL. https://arxiv.org/abs/2401.16467
- [V] Grand et al. (2024) LILO. https://arxiv.org/abs/2310.19791
- [V] Ellis et al. (2021) DreamCoder (intro and results only). https://arxiv.org/abs/2006.08381
- [V] Demirtas et al. (2025) Planning feedback for open-ended programming exercises. https://arxiv.org/abs/2504.08958
- [V] Rivera et al. (2024) Iterative student program planning with GPT-4 feedback. http://cs.brown.edu/~sk/Publications/Papers/Published/rsfk-planning-w-gpt-feedback/paper.pdf and https://doi.org/10.1145/3649217.3653607
- [V] Wang et al. (2023) Voyager (numbers not re-checked by the critique). https://arxiv.org/abs/2305.16291
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Islam et al. (2024) MapCoder. https://arxiv.org/abs/2405.11403
- [V, abstract and method only] Lei et al. (2025) Planning-Driven Programming (LPW). https://arxiv.org/abs/2411.14503
- [V, abstract and introduction only] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V, abstract and introduction only] Prasad et al. (2024) ADaPT. https://arxiv.org/abs/2311.05772
- [V] Chen et al. (2024) Skills-in-Context prompting. https://arxiv.org/abs/2308.00304
- [V] Dziri et al. (2023) Faith and Fate. https://arxiv.org/abs/2305.18654
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896
- [V] Wu et al. (2024) Reasoning or reciting? Counterfactual tasks. https://arxiv.org/abs/2307.02477
- [V] Dinh et al. (2023) Large language models of code fail at completing code with potential bugs. https://arxiv.org/abs/2306.03438
- [V] Lam et al. (2025) CodeCrash. https://arxiv.org/abs/2504.14119
- [V] Wu et al. (2026) XYEval. https://arxiv.org/abs/2609.23939
- [V] Wang et al. (2024) CodeRAG-Bench. https://arxiv.org/abs/2406.14497
- [V] Ma et al. (2025) Reasoning models can be effective without thinking. https://arxiv.org/abs/2504.09858
- [V] Cuadron et al. (2025) The danger of overthinking. https://arxiv.org/abs/2502.08235
- [V] Think Anywhere in Code Generation (2026). https://arxiv.org/abs/2603.29957
- [V] Denny et al. (2023/2024) Computing education in the era of generative AI. https://arxiv.org/abs/2306.02608

The critique re-opened Jiang, PlanSearch, Parsel, Olausson, CodeChain and AWM and confirmed their numbers.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 7 established claims: 3 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A20.06-K02** (reworded: the sources support less). Numbers match Fix, Wiedenbeck and Scholtz 1993 (20 vs 20; 3.7 vs 1.7, F(1,38)=57.58; 4.0 vs 3.7 n.s.), but it is one study with one 'moderately complex' and one 'very simple' recurring-pattern question, so a general 'only for non-trivial plans' and the label 'complex' are too strong; the review appendix actually shows mixed findings (Davies 1990: plan use may come from design training). Corrected claim: In one study (Fix, Wiedenbeck and Scholtz 1993; 20 novices vs 20 experts), experts labelled a moderately complex recurring plan far better than novices (3.7 vs 1.7 of 4, p=.0001) but did not differ on a very simple plan (4.0 vs 3.7, n.s.); other studies on plan knowledge are mixed.
- **A20.06-K15** (reworded: the sources support less). CodeChain APPS 22.33 to 30.24 and ReGAL +11.5 (LOGO, CodeLlama-13B) vs +1.3 (Date, GPT-3.5) verified, but in the CodeChain ablation (Table 3, CoT + public-test filter) the 30.16 row is centroid whole programs, not random whole programs; the comparison actually shown is centroid sub-modules 35.11 vs centroid whole programs 30.16 and random sub-modules 32.87. Corrected claim: Reusing solved sub-modules or abstractions helps, with more for weaker models: CodeChain APPS pass@1 22.33 to 30.24 (GPT-3.5); ReGAL +11.5 on LOGO for CodeLlama-13B vs +1.3 on Date for GPT-3.5; in the CodeChain ablation, centroid sub-modules (35.11) beat both centroid whole programs (30.16) and random sub-modules (32.87).
- **A20.06-K26** (number corrected). CodeRAG-Bench reports ODEX-hard gains of 20.3-40.1 percent RELATIVE (e.g. GPT-3.5-turbo 17.2 to 24.1 with BM25 = +6.9 points = 40.1%), not +20.3 to +40.1 points; DeepSeekCoder-7B no gain on MBPP (60.8 baseline vs 56.4-60.6 with retrieval) is correct; the last sentence about plan libraries is an inference from ReGAL. Corrected claim: Retrieval into the prompt helps most where the model lacks knowledge and little where it already knows: on ODEX-hard (rare libraries) retrieved documents improved results by 20.3 to 40.1 percent relative for most retrievers (GPT-3.5-turbo baseline 17.2, up to 24.1), while DeepSeekCoder-7B did not gain on MBPP (60.8 baseline vs 56.4 to 60.6 with retrieval). With a strong model, a small gain from a plan library on tasks it already solves is expected (ReGAL GPT-3.5 Date +1.3).
- **A20.06-K27** (reworded: the sources support less). NoThinking claim and LiveCodeBench pass@1 exception verified, but the Overthinking paper does not show that more effort lowers agentic scores: o1 high effort is 29.1% at about USD 1,400, single low effort is 21.0% at USD 400, and the 27.3% at 43% lower cost (USD 800) is two low-effort samples with the lowest-overthinking-score selected. Corrected claim: At equal tokens, many cheap samples with a check beat one long thought, except for code at pass@1 (NoThinking: LiveCodeBench pass@1 favors Thinking). Reasoning models already plan inside their thinking, and on SWE-bench Verified selecting the lower-overthinking of two low-effort o1 runs gave 27.3% at USD 800, against 29.1% for one high-effort run at about USD 1,400 (43% less cost; single low effort scored 21.0% at USD 400).
- **A20.06-K10** (now single-source: only one opened source, code check).
- **A20.06-K12** (now single-source: only one opened source, code check).
- **A20.06-K13** (now single-source: only one opened source, code check).
