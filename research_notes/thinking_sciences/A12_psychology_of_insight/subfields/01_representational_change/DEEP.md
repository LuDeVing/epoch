# Representational change: constraint relaxation and chunk decomposition: deep document

*Written 2026-10-26 from evidence_a-d.jsonl (ids a01-a28, b01-b30, c01-c28, d01-d19), claims.jsonl (K01-K32) and critique.md in this folder. Numbers follow the critique's corrections. Status marks: [E] established, [S] single-source, [C] contested. Links to other subfields are notes only: progress monitoring theory (04_progress_monitoring_theory, same field), verification design (C01), adaptive stopping (C01), LLM metacognitive harness (A04).*

## 1. What it is

Representational change theory says this. A solver reads a problem and builds a first representation from prior knowledge. That first representation is built from what the solver already knows, so it is the wrong one for insight problems. It makes the solution unlikely. The solver reaches an impasse. The impasse breaks only when the representation changes. Then the solution is easy.

The theory names two change mechanisms (a01):

- **Constraint relaxation.** The solver drops an assumption that was blocking the solution. In matchstick arithmetic: "numbers stay as they are", "the operator sign cannot change", "the statement must not be a tautology".
- **Chunk decomposition.** The solver splits a unit that was seen as one piece into parts. In matchstick arithmetic: a Roman X is one unit, but it is two crossed sticks and can become V.

Two ideas make the theory testable.

1. **Constraints sit on levels.** A change on a higher level is a wider revision. It is less likely to be tried, so the problem is harder (a02).
2. **Chunks have tightness.** Loose chunks (composite numerals such as IV) are easy to split. Tight chunks (I, V, X, the minus) are hard to split (a03).

The main task family is matchstick arithmetic. A false Roman-numeral equation is given. The solver moves one stick to make it true.

Why it matters for us. The theory gives the S6 IMPASSE state a mechanism. The stuck state is a bad representation, not too little search (a01). The two exits map to operators: O4 (drop a constraint) and O6 (change representation). The theory also warns that the exit must be routed, and that checking and selection are separate jobs from re-representing.

Scope warning. The strong human evidence is one task family and one lab group. The authors say they have no independent evidence that knowledge is stored as constraints and chunks (a01, critique section 4). Treat "re-representation" as a plausible operator to test, not as a proven law (b05).

## 2. History and theories in depth

### 2.1 Roots

- Gestalt psychology (Duncker, Kohler, Wertheimer) described restructuring but gave no mechanism. Knoblich et al. say Gestalt reorganisation "has no mechanism" (a08).
- Kaplan and Simon (1990), "In search of insight", offered the main rival: the impasse comes from an incomplete initial representation. The exit is to notice more features, especially invariants, not to drop constraints. Tested on the mutilated checkerboard. Known only second-hand here (a22, [M]). Knoblich et al. 2001 note that it is unclear which invariants exist in matchstick arithmetic, so the two accounts were not separated.
- Ohlsson (1992), "Information-processing explanations of insight and related phenomena" (pp. 1-44): the founding formal statement. Activation retrieves a misleading representation. Impasses resolve by re-encoding, elaboration, or constraint relaxation. Full text not found (a20, [M]). The three exits map to O6, an add-information operator we lack, and O4.

### 2.2 The core test: Knoblich, Ohlsson, Haider, Rhenius (1999)

Four experiments, all matchstick arithmetic with one-stick moves (a01-a08). Problem types:

| Type | What must change | Level |
|---|---|---|
| A | value only (loose chunk) | value |
| B | value and operator | operator |
| C | operator and tautology (two constraints) | tautology |
| D | value, but a tight chunk (X to V) | chunk |

Predictions: A easiest; B and C harder; C hardest on constraints; D hard because of tightness. The authors cannot rank D against B or C (a02). The hierarchy was a design hypothesis fitted to the task.

They argued against rivals (a08): Gestalt reorganisation (no mechanism), variation-selection (cannot say why some moves take longer or why transfer differs), gradual transformation (implausible for single-step problems solved in seconds), functional fixedness (explains blockage, not release), mental ruts (predicts no recovery without a pause, yet solvers recovered), remote associations and differential recall (need extra assumptions). These were arguments, not direct tests. Jones 2003 and Oellinger 2008 later tested rivals directly.

No runnable model of the full theory exists (a24). The theory is stated as rules about the probability of considering a move. The nearest formal sketch is the two-process model of Oellinger et al. 2008.

### 2.3 Eye-movement evidence: Knoblich, Ohlsson, Raney (2001)

Three predictions: fixations lengthen at impasse; early attention goes to values, not operators; attention shifts to the crucial element before success (a09-a12, b01-b05). All three held. See section 3 for numbers. The authors argue only representational change explains the whole pattern (b05). That is argument by conjunction on N=24 and one task family. It was never tested against a rival model fitted to the same data.

### 2.4 Rival tests and extensions

- **Jones (2003)**, car park sliding-block puzzle (a14, a15). Head to head with the progress monitoring theory of MacGregor, Ormerod, Chronicle (2001) (a23, second-hand). Both theories got some support. Constraint-relaxation manipulations moved performance; progress monitoring predicted no change. The lookahead split did not match the 64% that progress monitoring predicts.
- **Oellinger, Jones, Knoblich (2006)**, two-move matchstick problems (a16). Degree of constraint relaxation drove difficulty. Hill-climbing (distance to goal) had minimal effect. Their model: representational change is the condition for heuristics to work on the right representation. Spelling: the author is Oellinger (earlier Ollinger).
- **Oellinger, Jones, Knoblich (2008)**, mental set (a17). A two-process model: representational change selects a procedure; proceduralisation then reinforces it and can block a different relaxation later. The ACT-R-style mechanism is speculative and not implemented.
- **Graf, Danek, Vaci, Bilalic (2023)**, change-point re-analysis of eye data (a13, b16). Tests whether the shift is sudden. See section 5.
- **Danek, Wiley, Oellinger (2016)** (b21, d05). The more constraints must be relaxed, the less often solvers report an Aha. Many solved without Aha. So a solved insight item is not proof of a sudden event.
- **Miller, Wiley, Ohlsson (2025)** (b22, d03). Tests whether the two mechanisms are independent by cueing. See section 5.
- **Korovkin (2021, doctoral summary)** (a28). Representation is built from hierarchical mental schemes. Change can be weakening of automated schemes, high-level search for a scheme by analogy, or analysis of contradictions between schemes. Gives a third trigger: a consistency check between two partial readings.

### 2.5 Ohlsson 2011

*Deep Learning: How the Mind Overrides Experience*, ch. 4, "Creative insight: the redistribution theory", pp. 87-129 (a21, d06). It recasts the theory as redistribution of activation. Only the chapter opening is public. It states a "Raisins in the Dough" principle: a creative project needs several short insights spread through mostly analytical work. It sets three tasks: describe analytical thinking, explain insight, explain how insight extends analytical thinking. The redistribution steps are NOT visible. Any operational reading (change which knowledge is active rather than add more search) is a hypothesis. Nothing here can be used for LLM memory retrieval (K32).

### 2.6 Competing explanations still alive

- Progress monitoring (MacGregor et al. 2001): solvers hill-climb, compare progress to moves left, and search for alternatives when the goal looks unreachable. Assumed lookahead split 32% one, 32% two, 36% three. Gives a code-side trigger (a23).
- Misunderstanding theory (Macchi et al. 2026): restructuring is fixing a mis-framed goal (b11).
- Search-based accounts: wide jumps in concept space and de-fixation (Chao, Hsieh, Wu 2025, b24, [M]).
- Dual factors (Tseng et al. 2014) and negative-transfer work (Kershaw et al.), titles only (d19).

## 3. Core findings with exact numbers

Status here is the finding's status in claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Difficulty order A < B < C, D hard, in frequency and especially time | Exp 1A N=20: type F(3,57)=7.11 p<.001; times A<B T=12, B<C T=41, A<D T=10 | Knoblich 1999 (a04) | [E] K01 |
| Replication with new problem versions | Exp 1B N=38: F(4,144)=10.03 p<.001; version effect F(1,36)=0.39 p=.52; A vs B frequency p=.12 (ceiling); times A<B T=107, A<D T=96 | a05 | [E] K01 |
| Difficulty gap vanishes on second encounter | Exp 1A block F(1,19)=14.41 p<.01; "always disappeared" in all four experiments | a04, d02 | [E] |
| Transfer follows initial difficulty, not surface similarity | Exp 2 N=78: type F(4,222)=46.45; block F(1,74)=177.97; type x block F(4,222)=39.99; similarity effect on time only Type C H=11.05 p<.05, D H=6.88 p=.08. Transfer size followed difficulty | a06 | [S] K04 |
| Type D transfer is time only | Frequency 75% to 90% not significant (p=.13); time significant (p<.05). Frequency transfer significant for B (p<.05) and C (p<.001) | a04 with critique correction | [E] |
| Constraint relaxation is causal (tautology test) | Exp 3 N=34: regular Type C 61% vs tautological 100%, chi2(1)=12.59 p<.001; regular-first group C 61% to 100%, chi2=13.85 p<.001; Type D 61% vs 69% p=.64; Type A 94% vs 97% | a07, d01 | [E] K03 |
| Type D time gain after tautology exposure | U=65, Z=2.71, p<.01 (C: U=8, Z=4.67). Likely practice: tautology set held a tautological D item needing decomposition | d01 (inference) | [E] K03, partial |
| Eye tracking: solved by type | N=24, 1000 Hz, 5 min: A 23/24, C 18/24, B 9/24; A vs B chi2(1)=18.38 p<.001; A vs C chi2=4.18 p<.05; B vs C chi2=4.78 p<.05. Median time A 22 s, C 136 s, B 300 s | Knoblich 2001 (a09, b01) | [E] K01 |
| Fixations longer on hard problems and grow with time | problem F(2,44)=3.49 p<.05 (B, C > A); interval F(2,44)=8.58 p<.001; interaction F(4,88)=1.54 p=.20 | a10, b02 | [E] K05 |
| Fixation duration does not separate solvers from non-solvers | no difference between successful and unsuccessful; interaction n.s. | a10 | [S] K07 |
| Early attention on values, away from + and = | long fixations: element F(3,63)=24.02 p<.001; problem p=.42; interaction F(6,126)=2.06 p=.06; chance share 20% | a11, b03 | [E] K05 |
| Late shift to the critical element in solvers only | Problem B long: success x interval F(1,22)=7.91 p<.01. Problem C long: interval F(2,42)=5.31 p<.01, success x interval F(2,42)=5.08 p<.05. C short: marginal F(1,21)=3.09 p=.09 | a12, b04 | [E] K05 |
| Shift is sudden (about the 90% time bin) | N=61, 34% solved unaided, 11% more after hint; GAM from 90% bin; ANOVA 80% bin | Graf 2023 (a13, b16) | [S] K06 |
| Car park: impasse before first taxi move | N=39 (13 per condition); 31 solved unaided; normal vs rotated/easy Fisher p=.01; taxi-move fixation F(2,58)=5.40 p<.01; right-hand block fixation solvers 24% vs non-solvers 9% F(1,39)=6.50 p<.05 | Jones 2003 (a14) | [C] K09 |
| Relaxing once is not enough | 5 of 8 non-solvers moved taxi (about 2 times each), always returned it; time in right area at impasse solvers 19% vs 8%, F(1,39)=5.56 p<.05 | a15 | [S] K08 |
| Two-move problems: relaxation depth drives difficulty | N=120; approx. value-value 90%, hybrid 75%, operator 60%, tautology 25% (bands only); type F(1,118)=37.47 p<.001; value-type F(1,118)=1.54 n.s.; partial solution F(1,116)=45.15 p<.001; of 509 equations 60.89% value, 22.47% hybrid, 16.64% operator | Oellinger 2006 (a16) | [C] K09 |
| Pooled difficulty (Bayesian) | vs A (intercept 1.81 log-odds): B -1.59, C -2.95, D -1.93; pooled N about 266 (105+88+73) | Spiridonov (b10) | [E] K01 |
| Tight chunks cost decomposition, not regrouping | Wu 2017 N=60: radical 98.4%, 1,797 ms vs stroke 90.0%, 3,070 ms; reorganisation 49.8%/4,730 ms vs 49.2%/4,245 ms; RT F(1,24)=45.77 p<.001, eta2=0.66 | b07 | [E] K02 |
| Pure regrouping fails about 4 in 10 even with pieces given | accuracy 62.2% vs 64.2% t(25)=0.79 p=.44; RT 6,405 vs 5,602 ms p=.002 d=0.56 | b08 | [E] K02 |
| Showing parts raises solving | Macchi 2026 Exp 2 N=59: 46.7% (14/30) vs real-sticks photo 79.3% (23/29), chi2(1)=6.72 p=.010 V=.337 | b11 | [S] |
| Interactivity: failed replication | Spiridonov Exp 1 N=105, Exp 2 N=88, Exp 3 N=73; most intervals span zero; movements A 0.56, B 1.70, C 1.91, D 8.26; Macchi Exp 1 N=87 paper 27.3% vs interactive 32.6%, chi2=0.290 p=.590 | b09, b11, a18 | [E] K11 |
| Cathodal stimulation helps two-constraint Type C | N=60 (20 per group): Type C 32% vs 5% vs 5%, chi2=7.02 p=.030 | Luft 2017 (b14) | [S] K12 |
| Cue the matching mechanism only | CD cue helped CD only; CR cue helped CR only; both together no better, sometimes worse; Study 2 CR cue did not raise CR solutions. N not available | Miller, Wiley, Ohlsson 2025 (d03) | [S] K13 |
| Mental set | Exp 1 N=108 no set effect for any test type; Exp 2 controls solved CR3 more, chi2(1,N=36)=7.26 p<.01; Exp 3 different-procedure group solved more CR1, chi2(1,N=36)=13.85 p<.001 | Oellinger 2008 (a17) | [C] K10 |
| Wrong motor pattern harms nine-dot | N=64: dot-turn training 37.5% vs non-dot-turn 78.1%, chi2(1)=10.83 p=.001 | Spiridonov 2019 (b19) | [E] K15 |
| False hint lowers anagram success; true hint adds only feeling of insight | false hint beta=-0.269 SE=0.129 p<.05; true hint on insight judgment OR=1.87 [1.18, 2.95] | Ammalainen 2022 (b17) | [E] K15 |
| Garden-path repair predicts creative problem solving | partial r(95)=0.41 p<.001; delta R2=0.09 (creative), 0.00-0.02 (analytic); Exp 1 N=85, Exp 2 N=97 | Dygert 2026 (b18) | [S] K14 |
| Aha falls as constraints stack | direction only (abstract) | Danek 2016 (d05) | [S] |
| LLMs far below humans on re-representation riddles | NazoNazo 201 riddles; human subset n=126 mean 52.9% (CI 46.6-59.2); 38 LLMs: non-reasoning 7.6%, reasoning 17.6% (subset); full set 9.42% vs 19.25%, OR 2.29 (CI 1.99-2.64) | Mizumoto 2025 (c01) | [E] K16 |
| Verification failure | gold answer in the thought log: Gemini 2.5 Flash 5.23%, Claude Opus 4 25.00%, DeepSeek-R1-0528 30.57%, Grok 4 39.34% of wrong answers | c02 | [E] K17 |
| More than 70% of wrong o1-like responses hold a correct thought | 418% more thought switching and 225% more tokens in wrong responses | Wang 2025 (d11) | [E] K17 |
| Spontaneous LLM shifts rare, usually worse | pooled shift rate 6.31%; pooled correctness 16.44% (no shift) vs 2.57% (shift), N=723,200 traces; Qwen 1.5B math 0.327 vs 0.144; Qwen 7B math 0.661 vs 0.282; crosswords 1.5B 0.096 vs 0.201 | d'Aliberti & Ribeiro 2026 (c04) | [E] K18 |
| External reconsider cue | Math 32.21 to 40.62 (+8.41); crosswords 9.70 to 10.15 (+0.45); Rush Hour about 0. Second aggregation: math +7.74, high-entropy math +15.38 | c05, d15 | [S] K19 |
| Reflection mostly confirms | 8 models, 5 math sets, 3,427 rollouts each; over 90% confirmatory; wrong-to-right mostly under 2%; truncating after first candidate saves 24.5% tokens for 2.9% drop | Kang 2025 (c06) | [E] K20 |
| Step-back | PaLM-2L Physics 66.4 to 73.2, Chemistry 70.9 to 81.8, TimeQA 41.5 to 66.0; GPT-4 Physics CoT 82.9 vs step-back 84.5; fixes 20.5%, breaks 11.9% | Zheng 2024 (c20) | [E] K21 |
| MathSticks: sign-change items harder | o3 51.45 vs 65.19; Gemini-2.5-Pro 38.91 vs 49.09; o4-mini 21.15 vs 26.95 (text); human 91.72; 1-move vs 2-move o3 82.50 vs 52.88 | Ji 2025 (d07) | [S] K23 |
| Tokenisation shapes chunk tightness | GPT-4 F: insertion .368, deletion .277, replacement .558 vs human 1.0/1.0/.971 | Shin & Kaneko 2024 (d08) | [S] K29 |
| Code-side object re-encoding on ARC | GPT-4 solved 13 of 50 easiest tasks; object representation nearly doubled | Xu 2023 (d16, abstract) | [S] K30 |
| Failed early turn persists | -39% average multi-turn drop, unreliability +112%, aptitude -15% | Laban 2025 (d09) | [S] K28 |
| Own-output blind spot; Wait cue | blind spot 64.5% in 14 models; Wait cuts it by 89.3%, accuracy +156% | Tsui 2026 (d10) | [S] K26 |
| LLM problem reframing for designers: no gain | N=280, three LLM conditions | Liu 2025 (c22, abstract) | [S] K22 |

## 4. Mechanisms and models

This section is written so an engineer can build the pieces. The literature has no runnable model (a24), so everything here is our own design reading of the theory, marked as such.

### 4.1 The representation as constraints and chunks

State: a problem is held as three things.

- `units`: the list of things the first reading treats as atomic (tokens, numbers, words, cells).
- `constraints`: a list of assumptions, each with a level (value, operator, whole-statement, in order of depth) and a flag `active`.
- `moves`: the move set generated under the current active constraints and units.

Theory in code terms (a01-a03):

- The chance of considering a move falls with the depth of the constraint it violates. Value-level violations are considered first, operator-level later, whole-statement last.
- The chance of splitting a unit falls with tightness: loose, intermediate, tight.
- An impasse is a state where all moves generated under the current constraints and units fail the check.
- Exit: toggle one constraint to inactive (O4) or replace one unit by its parts (O6), regenerate moves, search again.

### 4.2 Two change operations, kept separate

- **Relax (O4).** Input: the problem and a list of its stated and implied constraints. Output: the problem with one named constraint removed, plus a statement of what the relaxation now allows. Code regenerates the move set under the relaxed rule and tests every move.
- **Decompose (O6).** Input: a list of units the first reading treated as atomic. Output: the same problem with one named unit replaced by its parts, listed by code where possible (spell out characters, list digits; d08). Then a separate regroup step: search for a new grouping. Wu et al. show decomposition and regrouping are separate steps with separate failure rates (b07, b08).

Why separate. Cuing one mechanism helps its own item type; cuing both together does not beat one and sometimes lowers solving (d03, single source, abstract). Solving a tautology variant first removed the relaxation difficulty but not the chunk difficulty in solution rates (a07, d01).

### 4.3 Ordering of what to try

From the difficulty ladder (a02, a16, b10): try the shallowest constraint first, then deeper ones.

1. Value-level assumptions (numbers, tokens, quantities are fixed).
2. Operator-level assumptions (the operation or relation is fixed).
3. Whole-statement assumptions (the statement has to be non-trivial, the goal has to be what it looks like).

Expected cost grows with depth: pooled log-odds vs A were -1.59 (B), -2.95 (C) (b10). Budget for the deepest constraint to cost the most.

### 4.4 Relaxation is necessary, not sufficient

Jones 2003: non-solvers did move the taxi, then put it back (a15). So O4 must be followed by a step that states what the relaxation opens and a code run under the relaxed rule (K08). Oellinger 2006: a first move that relaxes the deeper constraint helped more than a value move (a16). A hint works best when it hands over the relaxed move.

### 4.5 Impasse signal and who fires what

Eye data show impasse as staring (longer fixations) and bias to value elements, then a late shift to the neglected element (a09-a12). The LLM mapping is a hypothesis:

- staring: near-identical repeated attempts, counted by code;
- value bias: the attempt quotes or uses only the data-like elements and never the glue elements (operators, connectives, the goal clause);
- late shift: a later attempt touches an element earlier attempts ignored.

Two limits. Fixation length does not separate solvers from non-solvers early on (a10), and it is predicted by every rival theory (b02). So an impasse signal says "try a new representation", not which one. Per G1 the trigger must be a code-visible failure; output statistics are logged, not trusted (K27).

### 4.6 Candidate output-side signals and what is known

| Signal | Evidence | Problem |
|---|---|---|
| Thought-switch rate | 418% higher in wrong answers (d11) | marks scatter, the opposite of fixation |
| First-pass entropy | cue gain larger when entropy high; odds ratio 2.21 per SD (d15, row alignment uncertain) | needs logprobs; small models |
| Answer stability across resamples | early exit works (d13) | stable-and-wrong looks like stable-and-right |
| Trace confidence | filters traces for voting (d14) | no test on fixation |
| Hidden-state correctness probe | AUC above 0.7 (d12) | needs weights |

### 4.7 Code-side re-encoding as the preferred form

Where the unit to split or the structure to expose can be computed, code should do it. Evidence: object-based grid encoding nearly doubled GPT-4 ARC solves (d16, abstract); tokenisation decides which chunks are tight for a model (d08); the Li et al. situation-puzzle fix has code end a chat after K questions or a wrong guess, rewrite the puzzle with confirmed facts as hints, and restart a fresh session (a25: best setting K=5, M=3, 4 wins of 5 puzzles, 5 puzzles only). Code does the re-representation; the model fills one slot.

### 4.8 Mental set and fresh context

Oellinger 2008 two-process model (a17): representational change picks a procedure, proceduralisation reinforces it, reinforced procedure can block a different relaxation. Agent reading: if a past fix is reused and fails, the next operator must differ. LLM-side support is indirect: a failed early turn persists (d09), and a model corrects the same error far less when it is its own output (d10). So the default re-attempt runs in a fresh context with a code-written summary of what failed (K28). Not yet tested on insight items.

## 5. What holds up

### 5.1 Solid

- **Difficulty by depth of change.** Replicated in 1A, 1B, 2 (Knoblich 1999), in the eye study (A 23/24, C 18/24, B 9/24), in Oellinger 2006 (about 90, 75, 60, 25%) and in Spiridonov's Bayesian pooled estimates (b10). Times show it more reliably than frequencies because of ceilings (a05, d02).
- **Gap closes on a second encounter** in all four 1999 experiments (d02). Big practical point: any test of a cue must use fresh items.
- **Eye-movement pattern** (longer fixations on hard items, value bias, late shift to the critical element) with the caveat that every rival predicts the first part (b02).
- **Chunk tightness costs decomposition, not regrouping** (b07, b08), but one task family plus a Chinese-character study.
- **Misleading cues harm.** False hints lower anagram success (b17), the wrong motor pattern lowers nine-dot solving 78.1% to 37.5% (b19), red herrings lower LLM scores (c13). Helpful hints help less reliably than false hints hurt (b17: true hint did not raise accuracy).
- **Machines fail at these tasks** (K16): NazoNazo, BrainTeaser, Only Connect, MathSticks, M-ARC, rebus.

### 5.2 Failures, replications that did not work, boundary conditions

- **Interactivity.** Weller et al. 2011 reported that real sticks erase the A-vs-B gap (second-hand only, a19). Spiridonov et al. failed to replicate in three experiments (N=105, 88, 73); participants rarely moved sticks. Interactivity raised success for A (odds up 860%, p=.028) and lowered it for B and C (odds down 88%, p=.034, .031); movement interfered with relaxing higher-level constraints. Exception: interactive sticks helped Type D (Exp 2) and VR sticks in Exp 3. Macchi et al. found no pencil gain (27.3% vs 32.6%, p=.590), but a photo of overlapping real sticks gave 46.7% to 79.3%. Control rates swing across labs: cheap necklace 3% vs 43%; triangle of coins 22%, 85%, 43% (b12, second-hand). Reading: unstable [E] as a non-lever.
- **Sudden shift.** Graf et al.: change point near the 90% bin, N=61, one problem, 34% solved. One page-summary note says the plotted data may have been simulated and the original data showed a gradual shift (a13); this is unverified. Danek 2016 adds that Aha falls as constraints stack. Keep single-source [S].
- **Hill-climbing vs relaxation vs progress monitoring.** Oellinger 2006 favours relaxation, but about 85% of moves reduced distance to the goal, so both have a part (a16). Jones 2003: lookahead split about even, not 64/36; non-solvers moved the taxi, which fits neither theory alone (a14). Contested [C]. Detail belongs to the progress monitoring subfield (04_progress_monitoring_theory).
- **Mental set.** Repeating non-insight set problems did not hurt insight problems (a17). Wrong motor training did hurt (b19). Possible reason: motor training primes the very move that must be dropped. Contested for humans [C].
- **Ceiling effects.** Over 75% of Type B solved in Exp 1B and over 80% in Exp 2; A vs B frequency was n.s. in 1B (p=.12) and A>D p=.13 in 1A. Use times and tokens as well as pass rates.
- **Reversals in Exp 2.** Types C and D were solved faster than A and B in Block 2, which the theory did not predict; authors gave ad hoc reasons (a06).
- **Type D separation.** Frequencies show separation, times do not, but the time gain is probably practice (d01, our inference). The paper's own wording is that tautological form does not affect initial difficulty and transfer in frequency (critique).
- **Cuing both mechanisms.** Combined cue no better than one, sometimes worse (d03). In Study 2 the relaxation cue did not raise relaxation solutions at all. Abstract only; N unknown.
- **Brain stimulation.** Cathodal tDCS helped only Type C (32% vs 5% vs 5%, p=.030, N=60); B and D no group difference (b14). Not an agent lever.
- **Type labels differ** between the 1999 and 2001 papers (in 2001: A loose-chunk value change, B operator change, C tight-chunk value change). Do not merge rates across the two (critique).

### 5.3 Interventions that worked (human)

- Solving the tautology version first (61% to 100% on regular Type C).
- Showing that the plus can be taken apart (a photo, +32 points; mechanism may be perception or chunk decomposition; rival is misunderstanding theory).
- Cuing the matching mechanism (single-source, abstract).
- Hand over a partial solution that relaxes the deeper constraint (a16, F(1,116)=45.15).
- Reformulating the question to state the real goal: bat-and-ball style item 10% to 90% (b13, second-hand, source study unidentified).

### 5.4 Did not work (human)

- Real sticks and movement (above).
- Helpful hints for accuracy in anagrams (b17).
- Training on the lure movement (b19).

### 5.5 Evidence quality warnings

- Triple counting: Mizumoto appears in seven evidence lines, Knoblich 2001 in nine, Graf in two, Spiridonov in two. In claims.jsonl each paper counts once.
- Knoblich 2001: three items, one per type, so type and item are confounded; one trial per problem; null interaction p=.20 with no power analysis.
- Many LLM sources were opened only to the abstract (see section 11).

## 6. Language models

### 6.1 How models behave

- **Large gaps to humans.** NazoNazo: human 52.9%, reasoning models 17.6%, non-reasoning 7.6% (subset); only GPT-5 within the human range; parameter count did not predict accuracy, release date did (c01). BrainTeaser: human about 92%, ChatGPT 53% and 63% on the two subtasks; 45% and 61% of originals it solved fail in context-reconstructed form (c07). SemEval-2024 BrainTeaser: human 0.920, ChatGPT 0.627; more than 80% of systems lose 2.5 to 34 points under rewording (c08). Only Connect Wall: humans about 71% of groups, best GPT-4 13.8% (c13). MathSticks: human 91.72%, best model o3 60.00% with text, 38.50% visual (c18, d07). M-ARC: physicians 66%, most LLMs under 50% (b29). Rebus: GPT-5 60.42%, o3 54.56%, Claude 3.7 Sonnet 10.20%, expert human 76.4% (c17).
- **Fixation by lure.** Removing red herrings raised GPT-3.5 and GPT-4 scores; more in-context examples did not help (b28, c13). The M-ARC follow-up reports the strongest reasoning models reaching human level by January 2026 (d18, abstract). Fixation moves with model strength.
- **Reasoning versions beat base versions.** Seed-1.6-Thinking 21.50 vs Seed-1.6 3.25 on MathSticks text; o3 60.00 vs GPT-4o 0.00 (c19; pairs not always matched).
- **Operator edits are hardest.** Sign-changed items are 8 to 14 points harder in text (d07). The paper asserts a digit-edit bias but gives no per-edit counts. Errors seen: perception, illegal edits, arithmetic not rechecked (9-3=5 turned into 9-2=5), operator handling, format.
- **Tokenisation decides what is a tight chunk** (d08).
- **Run-to-run variance is large.** RAT GPT-3.5 9-45% across four administrations; GPT-4 50% and 59% (c15, tiny sets, preprint). Orru et al. claimed "human-like" riddle solving on 30 old riddles with inconsistent statistics (c16): treat as weak. Use many seeds.

### 6.2 Where the failure sits: generation or endorsement

- Verification failure: 5.23% to 39.34% of wrong answers contained the gold answer in the thought log (c02; literal string match, so it can over-count).
- More than 70% of wrong o1-like responses contain a correct thought (d11).
- Humans verify better than models: stumpers, humans 100% when they had solved it, 63.8% when they had failed; most models below chance, mean 41% (c14).
- Gemini 2.5 Pro confirms its wrong answers over 95% of the time (true-negative rate 4.34%) (c21).
- Hidden states encode correctness: AUC above 0.7 (d12).
- Model "Oh!" language is common and mostly wrong: Claude Opus 4 more than 100 "Oh! I just..." lines (b26). A confident wrong reinterpretation is a second failure mode (c03).

Reading: for many items a code check over all harvested candidates comes before any new representation operator. This share is not measured on our sets (K31).

### 6.3 What changed results, by how much

| Intervention | Effect | Source |
|---|---|---|
| Step-back (abstract first) | +6.8 Physics, +10.9 Chemistry, +24.5 TimeQA (PaLM-2L); GPT-4 +1.6 and +0.3 over CoT; fixes 20.5%, breaks 11.9% | c20 |
| Structure-matched examples (RISCORE) | Llama3-70B 2+2 shot 0.833 vs 0.792 (similarity 4-shot); Mistral-7B 0.567 vs 0.458; automated +2 to +10 | c09 |
| One worked questioning transcript (SPLAT) | BrainTeaser word: Llama3-8B 46.20 to 58.07, 70B 71.20 to 79.54, GPT-4 64.39 to 69.69; RiddleSense GPT-4 +0.4 | c11 |
| Code restart with confirmed facts rewritten (Li) | 4 of 5 puzzles won at best setting | a25 |
| Object re-encoding by code (ARC) | about 13 to about 26 of 50 | d16 |
| External reconsider cue | math +8.41, crosswords +0.45, Rush Hour about 0 | c05 |
| Wait marker on own output | blind spot -89.3%, accuracy +156% (non-reasoning models) | d10 |
| Truncate reflection after first candidate | -24.5% tokens, -2.9% accuracy | c06 |
| Skill hint (rebus) | +1.6 to +2.0 (o4-mini +1.61, GPT-4o +2.04); GPT-4o-mini -0.44 | c17 |
| One in-context example (rebus) | o4-mini 48.16 to 45.83 | c17 |
| Few-shot demos (BrainTeaser) | no clear effect; commonsense-adapted models worse on sentence puzzles | c07 |
| CoT on harder Missed Connections | GPT-4-Turbo 25.56% vs with CoT 23.46%; standard game 29.2% to 38.93% | c12 |
| Prompting style on Indian riddles | Gemini 2.5 Pro zero-shot 41.52% vs 2-shot random 42.11%; no consistent gain | c21 |
| Thinking in the puzzle's language | Grok 4 Japanese 29.5% vs English 48.8%, p=.0071; others n.s. | c03 |
| LLM-assisted designer reframing | no gain over control, N=280 | c22 |
| Thought-switch penalty (TIP) | AIME24 QwQ 38.3 to 44.1 (table baseline disagrees with 46.7) | d11 |

Pattern (c27): restating at another level, structure-matched examples and worked transcripts give about 2 to 15 points. Skill hints, plain few-shot and generic reflection give about 0 to 3. Telling a model which re-representation is needed does not make it do it (c17). Caveat: mixed models, mixed benchmarks, baselines differ, many gains un-replicated.

### 6.4 Gaps in the LLM evidence

- No study runs Knoblich's A-D types with tightness labels on LLMs (K23, c28).
- No head-to-head of a named-constraint or named-unit cue against a generic reconsider cue on LLM insight items (K25, d17). Absence from a thin search is not proof of absence.
- Reconsider cue (c05) has no neutral-resample arm in the part read; pass 2 is also a second sample.
- Reflection results (c06) are math, where re-representation is seldom needed.
- No LLM test of progress monitoring on car park or matchstick (gap 10).
- Goal relaxation with a planner check: +52.45% over an LLM-plus-PDDL baseline (c25, snippet only, robotics). Design matches the schema (relax, verify by code); source unchecked.

## 7. What our agent should take

Each item: schema part, status, evidence ids. "Add now" items rest on at least two independent sources and fit existing guardrails; they do not need a new test to be written into the schema as constraints on how O4/O6 are used. "Test first" items are single-source or contested.

### Add now (established)

1. **Difficulty by constraint depth: try shallow first, budget more for deep.** Part: S6 operator ordering (O4, O6). [E]. Ids: a02, a04, a05, a16, b10 (K01). Add as an ordering rule: value-level, then operator-level, then whole-statement assumptions.
2. **O6 must name the unit being treated as atomic and split it by code where possible.** Part: O6, S2. [E] for tight vs loose chunk cost; code-side splitting [S]. Ids: a03, b07, b08 (K02), d08.
3. **Regrouping is a separate step from splitting; pieces given is not enough (about 4 in 10 regroup failures).** Part: O6 then S3/S4. [E]. Ids: b07, b08 (K02).
4. **Harvest every candidate from the trace and test each by code (already S4).** Strengthens S4 and G5. [E]. Ids: c02, d11, d12, c14, c21 (K17). Do this before adding any representation operator on a new class.
5. **Never accept or switch on insight words ("Oh!", "I see").** Part: G10. [E]. Ids: c04, b26 (K18).
6. **Trigger re-representation from outside the trace, on a code-visible failure.** Part: G1, S6. [E]. Ids: c04, c06, d09 (K18, K20); reflection inside the trace is mostly confirmation (over 90%).
7. **Cap in-trace reflection after the first candidate; spend the savings on an operator or on fresh attempts.** Part: G11. [E]. Ids: c06, c04 (K20). Saves 24.5% tokens for 2.9% drop.
8. **Do not add a build-it-physically or "act on it" step; acting on material does not reliably help and can interfere with relaxing deep constraints.** Part: none (a "not to add" entry). [E]. Ids: a18, b09, b11, b12 (K11). The one positive result (photo of overlapping real sticks) is a perception effect.
9. **Misleading frames cost more than right hints gain; keep restatements free of lure wording; put suggestive material in the marked block.** Part: S1 input hygiene. [E]. Ids: b17, b19, b28, c13 (K15).
10. **When reporting step-back or any restate operator, report the break rate (new errors), not only the fix rate.** Part: G7 measurement, O2/O6. [E]. Ids: c20, c09, c11, c27 (K21): fixes 20.5%, breaks 11.9%.
11. **Use time-to-solution or tokens as well as pass rate, and fresh items for each cue test.** Part: bench design. [E]. Ids: a05, d02.

### Test first

12. **O4 as a named step: list the constraints, relax one, state what the relaxation allows, run code under the relaxed rule.** Part: O4. [S]. Ids: a15, a16, c18, c25 (K08, K24). Relaxing without exploring the relaxed space failed in humans.
13. **O4 and O6 as separate operators with a router; never fire both prompts at once.** Part: S6 router. [S]. Ids: d03, b22, a07 (K03, K13). Human only, abstract only for the cue result.
14. **Named-constraint / named-unit cue beats a generic reconsider cue (and a Wait-style cue and a neutral resample).** Part: O4/O6 vs G1 cue. [S]. Ids: K25, K26, d10, c05. Open question; decides the router design.
15. **Fresh context with a code-written summary of what failed beats continuing in context.** Part: G3/O8, S6 re-entry. [S]. Ids: d09, d10, a25 (K28). Indirect support only.
16. **Code-side re-encoding (object lists, digit/character spelling) before a model-side reframe.** Part: O6, G5. [S]. Ids: d16, d08, a25 (K29, K30).
17. **Easy sibling first: solve a variant without the constraint, then restore it.** Part: new O4 variant (relax-then-restore). [S]. Ids: a07 (K03). Human one-experiment result (61% to 100%).
18. **Structure-matched example retrieval at an impasse, indexed by the constraint relaxed.** Part: memory, O7. [S]. Ids: a06, c09, c11 (K04). Index by relaxed constraint, not surface text; the human similarity result is one experiment (N=78).
19. **Step back to a general principle (O2/O6 first-line restate).** Part: O2/O6. [E] on non-insight sets; untested on insight items. Ids: c20 (K21). Listed here because insight transfer is untested.
20. **Require the attempt to touch elements earlier attempts ignored (glue elements: operators, connectives, goal clause).** Part: S6, O6. [S]. Ids: a11, a12, b03, b04 (K05 is [E] for humans; the LLM mapping is a hypothesis).
21. **Different-operator rule: if a reused fix fails, the next operator differs.** Part: S6 / memory. [C]. Ids: a17, b19, d09, d10 (K10).
22. **Lower rule-priority prompt only at high constraint depth.** Part: O4. [S]. Ids: b14 (K12). Analogy only; expect harm elsewhere.
23. **Lure-removed twin and reworded twin of each item to separate fixation from plain difficulty (consistency check as G3 on riddles).** Part: G3, bench. [S]. Ids: c07, c08, c13, c26.
24. **Gate on first-pass entropy where logprobs exist, log thought-switch and stability statistics.** Part: S6 logging. [S]. Ids: d11, d13, d14, d15 (K27). Log only; no gate until false-trigger rate known.

## 8. Concrete tests on our bench

Common rules for all tests: both arms get equal total tokens (G7), setup cost counted; at least 5 seeds per item (run-to-run variance is large, c15); report pass rate, tokens per solved item, and net gain = fixed minus broken versus the plain arm; use fresh items for each condition (gaps vanish on a second encounter, d02).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Cue specificity. Two item sets: constraint items (assumption to drop) and chunk items (unit to split). BrainTeaser sentence/word subsets, a MathSticks sample, hand-built riddles | (a) plain resample, (b) generic Wait/reconsider cue, (c) named-constraint cue (O4), (d) named-unit cue (O6), (e) both named at once | pass rate by item type, net gain, break rate | (c) beats (b) on constraint items only, (d) beats (b) on chunk items only, (e) no better than best single (d03). If (b) matches (c)/(d) within 2 points, the router is not worth building |
| T2 | Share of wrong answers whose log holds the gold answer, on each target set (BrainTeaser, MathSticks, ARC-type, NoveltyBench items with checks) | (a) final answer only, (b) all harvested candidates checked by code | verification-failure share; pass rate difference | If share above 15%, selection fixes more than a representation operator (K31); expect 5 to 39% (c02) |
| T3 | Failed-frame carry-over. Items where the plain model's first answer is wrong | (a) continue in same context, (b) failed attempt relabelled as a user draft, (c) fresh context with code-written summary of what failed | pass rate on second attempt | (c) above (a) by several points (d09, d10); (b) between |
| T4 | Depth ladder. MathSticks-style equations built in 3 depths (value only, operator change, whole-statement/tautology), 2 chunk types (digit vs operator edit); exact arithmetic check by code | plain vs O4/O6 routed by depth, reported per type | pass rate and tokens per type | Plain failure rises with depth (K01); operator items 8 to 14 points lower than digit-only items (d07); routed arm gains most at depth 2 and 3 |
| T5 | Chunk items where the key move splits a unit shown as atomic (words, numbers, tokens) | plain vs "list the parts of each unit first" vs code-side spelling of characters/digits | pass rate | Code-side spelling beats model self-split for character-level edits (d08) |
| T6 | O4 follow-through. Items where relaxing once is not enough (car park style, multi-step) | O4 then free continuation vs O4 then "state what is now allowed" plus code search under relaxed rule | pass rate | Second arm higher (a15) |
| T7 | Step-back on insight items | plain vs step-back vs neutral resample | fix rate and break rate | Fix rate up, break rate about 10% (c20); net gain small on insight items |
| T8 | Relax-then-restore (easy sibling) | plain vs solve constraint-free sibling then restore | pass rate on the hard version | Gain mostly on whole-statement items (a07) |
| T9 | ARC object re-encoding | plain text grid vs code object list vs model-side "restate the grid" | solved tasks | code object list first (d16) |
| T10 | Impasse signals. Log thought-switch rate, first-pass entropy, candidate repeat count, element coverage per attempt | no arm; logged on all runs | AUC of each signal for "will fail"; false trigger rate if used as a gate | only entropy and code-visible failure expected to carry signal (d11, d15) |
| T11 | Reworded and lure-removed twins | plain vs best operator, on originals and twins | accuracy drop original to twin | A real reframe keeps its gain on reworded twins; a surface effect loses it (c07, c08) |

## 9. What does not transfer, and why

- **Eye movements and fixation duration.** No LLM counterpart; fixation length cannot choose an operator even in people (a10, b02).
- **Interactive and physical manipulation.** Models have no hands; acting on the material is unreliable even in people (K11). Running code is the analogue and works only if it checks against the relaxed rule (b09 warns that moving can lock in the old frame).
- **Sudden insight as a signal.** The sudden shift is one dataset (K06); the Aha feeling is an unreliable marker even in people (d05); model "Aha" text is mostly wrong (K18).
- **Incubation and sleep.** Not in the theory and not in the schema (a08, 4b).
- **Brain stimulation** (b14), working memory capacity (b20), individual-difference results (b18): they describe people, not prompts.
- **Chunk tightness as defined for people.** Tight for a person (single stroke, Roman X) is not tight for a model; the tokenizer decides (d08).
- **The theory's claim about knowledge storage.** The authors have no independent evidence that knowledge is stored as constraints and chunks (a01). The operators work as engineering moves, not as a model of the LLM.
- **Time-limited, one-trial human data.** LLM tests can be run many times, so human effect sizes (small N, p-values near .05) only set expectations.
- **Contamination.** NazoNazo, BrainTeaser and the Ansburg riddles are public; high scores can be recall (c07, c16).
- **Effects that shrink with model strength.** Fixation on learned patterns shrinks as models improve (d18); a 2024 effect may not hold on the model we use.

## 10. Open questions

1. Does a named-constraint or named-unit cue beat a generic reconsider/Wait cue on LLM insight items at equal tokens? No study (K25).
2. Can an impasse be detected from output alone without false triggers? Candidates exist, none tested as a fixation detector; stable-and-wrong looks like stable-and-right (K27).
3. What do Knoblich A-D types look like for LLMs? Does failure rise with constraint depth and chunk tightness? Only MathSticks as a proxy (K23).
4. How big is the verification-failure share on our sets? (K31)
5. Is separation of relaxation and decomposition real for LLMs? The human cue result is one abstract; its N and wording are unknown (K13).
6. Does the failed-frame carry-over exist inside one LLM context on insight items? Clean-context vs reframe untested (K28).
7. Do the operators transfer from insight puzzles to ARC and NoveltyBench? Step-back is the only strong generic result and breaks 11.9% (K30).
8. What does Ohlsson 2011 say that we miss? Redistribution of activation as a retrieval rule for LLM memory is unverified (K32).
9. Is the late sudden shift replicated outside Graf et al.? Candidates: Tseng et al. 2014, Kershaw et al. (d19).
10. Does progress monitoring or representational change better predict LLM failure on search-like items? Passed to the progress monitoring subfield.
11. Is the Type D time gain really practice? That is our inference from the Method (d01).
12. Do models fail by not generating the relaxed problem, or by generating it and not exploring it (Jones's taxi problem)?
13. What are the Miller, Wiley, Ohlsson sample sizes, effect sizes and instruction wording? Full text blocked (403).

## 11. Sources

[V] = full text or page opened this session. [M] = abstract, snippet or second-hand only.

**Human representational change**
- [V] Knoblich, Ohlsson, Haider, Rhenius (1999) Constraint relaxation and chunk decomposition in insight problem solving. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (a01-a08, a24, b06 [M] copy, c24 [M] copy, d01, d02)
- [V] Knoblich, Ohlsson, Raney (2001) An eye movement study of insight problem solving. https://link.springer.com/content/pdf/10.3758/BF03195762.pdf (a09-a12, b01-b05). Note: critique did not re-open this paper; its numbers come from two agents reading the same paper, so one source.
- [V] Jones (2003) Testing two cognitive theories of insight (preprint). https://ntu.eprints-hosting.org/id/eprint/18103/1/196105_RUNNING%20HEAD%20v2%20%28Item%20Ref.%20330%20Jones%20PrePublisher%29.pdf (a14, a15)
- [V] Oellinger, Jones, Knoblich (2006) Heuristics and representational change in two-move matchstick arithmetic tasks. https://ntu.eprints-hosting.org/id/eprint/25198/1/197400_2107%20Jones%20Publisher.pdf (a16; c23 [M] abstract copy: https://irep.ntu.ac.uk/id/eprint/25198/)
- [V] Oellinger, Jones, Knoblich (2008) Investigating the effect of mental set on insight problem solving. https://ntu.eprints-hosting.org/id/eprint/23048/1/193183_1563%20Jones%20Postprint.pdf (a17)
- [V] Graf, Danek, Vaci, Bilalic (2023) Tracing cognitive processes in insight problem solving: GAMs and change point analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (a13, b16; a13 read through a page summary)
- [V] Wu, He, Zhou, Xiao, Luo (2017) Decomposing a chunk into its elements and reorganizing them as a new chunk. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5694466/ (b07, b08)
- [V] Spiridonov, Erofeeva, Klowait, Morozov, Ardislamov (2025/2026) The modulating role of sources of difficulty in interactive matchstick algebra. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12862482/ and https://digital.ub.uni-paderborn.de/hs/download/pdf/8202463 (a18, b09, b10). Use the b09 Ns (105/88/73).
- [V] Macchi, Inglese, Caravona et al. (2026) Does physical interaction with insight problems really affect the solution rate? https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13208192/ (b11-b13; b12 and b13 second-hand content)
- [V] Luft, Zioga, Banissy, Bhattacharya (2017) Relaxing learned constraints through cathodal tDCS on the left DLPFC. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462743/ (b14, b15 second-hand part)
- [V] Ammalainen, Moroshkina (2022) Where does Eureka come from? https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9703963/ (b17)
- [V] Dygert, Jarosz (2026) Navigating the garden path. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13412464/ (b18)
- [V] Spiridonov, Loginov, Ivanchei, Kurgansky (2019) The role of motor activity in insight problem solving. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6352738/ (b19)
- [V] Danek, Wiley, Oellinger (2016) Solving classical insight problems without Aha! experience. https://docs.lib.purdue.edu/jps/vol9/iss1/4 (d05, abstract page; b21 [M] via https://doi.org/10.7771/1932-6246.1183)
- [V] Korovkin (2021) Mental schemes in insight problem solving, doctoral summary. https://www.ranepa.ru/upload/iblock/a7c/uydt1879wx55mw6027083lb81r80nhxo.pdf (a28; year is a guess)
- [V] Ohlsson (2011) ch. 4, publisher page only. https://www.cambridge.org/core/books/deep-learning/creative-insight-the-redistribution-theory/9EE905B96C5FF28F6182D7A8BB01046F (a21, d06; chapter opening only, so mechanism unverified)
- [V, abstract] Miller, Wiley, Ohlsson (2025) Testing the independence of representational change theory processes, Thinking & Reasoning. https://doi.org/10.1080/13546783.2025.2535758 (b22 [M], d03: full abstract read, full text 403)
- [M] Ohlsson (1992) Information-processing explanations of insight (a20). No URL.
- [M] Kaplan and Simon (1990) In search of insight (a22), via Knoblich 2001.
- [M] MacGregor, Ormerod, Chronicle (2001) (a23), via Jones 2003.
- [M] Weller, Villejoubert, Vallee-Tourangeau (2011) Interactive insight problem solving (a19), via Spiridonov.
- [M] Xing, Lu, Hu (2019) working memory updating and spatial insight. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6491639/ (b20)
- [M] Oellinger, Szathmary, Fedor (2023) card sorting games. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10196050/ (b23)
- [M] Chao, Hsieh, Wu (2025) Long-distance exploration. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11947100/ (b24)
- [M] Xing et al. (2013) logogriph tasks, Acta Psychologica Sinica 45(10). https://journal.psych.ac.cn/acps/EN/Y2013/V45/I10/1061 (d04)
- [M] Tseng, Chen, Chen (2014) Thinking Skills and Creativity. https://doi.org/10.1016/j.tsc.2014.04.004 ; Kershaw et al. (2010, 2011) (d19, titles only)

**Language models and reasoning**
- [V] Mizumoto et al. (2025) The Metacognitive Bottleneck (NazoNazo). https://arxiv.org/abs/2509.14704 and https://arxiv.org/pdf/2509.14704 (a26, b25-b27, c01-c03)
- [V] d'Aliberti, Ribeiro (2026) The Illusion of Insight in Reasoning Models. https://arxiv.org/abs/2601.00514 (c04, c05, d15; the final 50k characters were not read)
- [V] Kang et al. (2025) First Try Matters. https://arxiv.org/abs/2510.08308 (c06)
- [V] Jiang, Ilievski, Ma, Sourati (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057 (c07; b30 [M] abstract copy)
- [V] Jiang, Ilievski, Ma (2024) SemEval-2024 Task 9. https://arxiv.org/abs/2404.16068 (c08)
- [V] Panagiotopoulos et al. (2024) RISCORE. https://arxiv.org/abs/2409.16383 (c09)
- [V] Huang et al. (2024) LatEval. https://arxiv.org/abs/2308.10855 (c10)
- [V] Chen et al. (2024) SPLAT. https://arxiv.org/abs/2410.06733 (c11)
- [V] Todd et al. (2024) Missed Connections. https://arxiv.org/abs/2404.11730 (c12)
- [V] Naeini et al. (2023) Only Connect Wall. https://arxiv.org/abs/2306.11167 (b28, c13)
- [V] Goldstein et al. (2023) Decoding Stumpers. https://arxiv.org/abs/2310.16411 (c14)
- [V] Speed (2023) caution against anthropocentrism. https://arxiv.org/abs/2309.07683 (c15)
- [V] Orru et al. (2023) Human-like problem-solving abilities in LLMs using ChatGPT. https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2023.1199350/full (c16; a27 [M] abstract copy)
- [V] Lee et al. (2025) Puzzled by Puzzles (rebus). https://arxiv.org/abs/2505.23759 (c17)
- [V] Ji et al. (2025) MathSticks. https://arxiv.org/abs/2510.00483 (c18, c19, d07)
- [V] Zheng et al. (2024) Take a Step Back. https://arxiv.org/abs/2310.06117 (c20)
- [V] Abhinav P M et al. (2025) The Riddle of Reflection. https://arxiv.org/abs/2511.00960 (c21)
- [V] M-ARC authors (2025) Limitations of LLMs in clinical problem-solving. https://arxiv.org/abs/2502.04381 (b29, d18) and follow-up https://arxiv.org/abs/2601.11866 (d18, abstract only)
- [V] Li et al. (2025) Solving Situation Puzzles with LLM and External Reformulation. https://arxiv.org/pdf/2503.18394v1 (a25)
- [V] Shin, Kaneko (2024) LLMs lack understanding of character composition of words. https://arxiv.org/abs/2405.11357 (d08)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120 (d09)
- [V] Tsui (2026) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d10)
- [V] Wang et al. (2025) Thoughts are all over the place. https://arxiv.org/abs/2501.18585 (d11)
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419 (d12)
- [V, abstract] Fu et al. (2025) Certaindex. https://arxiv.org/abs/2412.20993 (d13)
- [V, abstract] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d14)
- [V, abstract] Xu et al. (2023, rev. 2024) LLMs and the ARC. https://arxiv.org/abs/2305.18354 (d16)
- [M] Liu, Lee et al. (2025) No Evidence for LLMs Being Useful in Problem Reframing. https://arxiv.org/abs/2503.01631 (c22)
- [M] ContextMatters (2025) goal relaxation with a planner. https://arxiv.org/abs/2506.15828 (c25; also named: LLM-Flax 2604.26569, AutoCO 2509.12643)
- [V] Gap-search log, arXiv listing scans (d17). https://arxiv.org/search/?query=hints+large+language+models+reasoning+hint+levels&searchtype=abstract
