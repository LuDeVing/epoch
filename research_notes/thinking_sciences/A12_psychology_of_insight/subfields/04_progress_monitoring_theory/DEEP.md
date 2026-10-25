# Progress monitoring theory: deep document

*Subfield of A12 Psychology of insight. Evidence ids (a01 to d18) refer to evidence_a-d.jsonl in this folder; claim ids (K01 to K25) refer to claims.jsonl; critique.md holds the cross-check. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Human-study numbers were recomputed from reported counts in the cross-check because the PDFs could not be re-opened. The founding paper (MacGregor, Ormerod and Chronicle 2001) was never opened; its numbers are second-hand.*

---

## 1. What it is

Progress monitoring theory is an account of why some problems are hard and when a solver gives up the current line of attack. It comes from MacGregor, Ormerod and Chronicle (2001) and was named the criterion of satisfactory progress (CSP) theory in Chronicle, MacGregor and Ormerod (2004). The authors work inside a means-ends analysis frame. They claim insight problems are not a special kind. They are ordinary search problems where the usual search rule happens to point away from the answer.

The theory has four parts.

1. **Maximisation.** The solver picks the move that looks like the most progress toward the goal. In the nine-dot problem that means a line through as many dots as possible. In the six-coin problem it means putting as many coins as possible on the ring.
2. **Progress monitoring.** The solver checks each move against a criterion: the work still to do divided by the moves still allowed. A move that closes at least that much passes.
3. **Criterion failure.** When no move passes, the solver knows the current approach cannot finish in the moves left. Only then does the solver relax the demand and consider non-maximal moves, including moves outside the first representation.
4. **Lookahead.** The solver tests moves a few steps ahead before committing. Depth varies by person, from zero to about four. Deeper lookahead detects criterion failure sooner.

In the nine-dot problem the criterion at the start is 9 dots / 4 lines = 2.25 dots per line, so a line through 3 dots passes (b01, a02). A solver who keeps drawing 3-dot lines inside the square only discovers failure at the fourth line, which is too late. The same loop that makes the problem hard (greedy progress) also creates the conditions for the insightful move (criterion failure forces a search for something else). The authors state this in one sentence (a01).

**Why it matters for our agent.** It gives a code-checkable definition of an impasse. The program can compute distance left and budget left, take the ratio, and compare. That is a trigger for state S6 that does not depend on the model's feelings. It also supplies a warning: the move that looks best by visible progress may be the trap. The theory does not say what to do after criterion failure. For that we need representational change (see links in section 2.6 and in the sibling subfield "Representational change: constraint relaxation and chunk decomposition").

**Scope of this document.** We cover the CSP theory, its experiments, its rivals, its combined accounts, an engineering reading of the mechanism, and LLM work on progress estimation and stuck detection. We do not repeat the general theory of impasse or representational change (see the earlier A12 documents and the 00_FIELDS.md list). Links only to sibling subfields in this run: Means-ends analysis; Accuracy and dissociation of monitoring; LLM metacognitive harness; Representational change; Adaptive stopping and metareasoning; Soar impasses; Anomaly handling and fixation.

---

## 2. History and theories in depth

### 2.1 Background: why nine dots?

The nine-dot problem is the classic insight task. Join nine dots in a 3x3 grid with four straight lines without lifting the pen. Almost nobody solves it. Under 5% of undergraduates solve it in a few minutes (b10, a13). Nobody solved it in 10 minutes in Burnham and Davis (1969) or in 100 attempts in Weisberg and Alba (1981) (a20). Telling people to go outside the square makes all of them draw outside, yet only a small minority solve (a19, b10).

The older Gestalt reading said people wrongly assume lines must stay inside the square. The "outside the box" failure of that reading is the opening that the information-processing account fills.

### 2.2 MacGregor, Ormerod and Chronicle 2001: the process model

The founding paper (a01, b22, abstract only; numbers second-hand) has five experiments. Experiments 1 and 2 test whether the model predicts performance on the nine-dot problem and its variants. Experiment 3 extends it to the insightful moves. Experiments 4 and 5 are critical tests against earlier accounts. Four opened papers describe the model the same way (b22):

- (a) draw each line through as many dots as possible;
- (b) value a line by dots picked up relative to dots left and lines left;
- (c) look ahead 1 to 4 lines;
- (d) if every line leads to insufficient progress, consider lines outside the figure with some probability (a13).

Second-hand numbers: the estimated lookahead mix is about 32% / 32% / 36% for lookahead 1 / 2 / 3 (via Jones 2003; a20, b08) and 0% for four (a26). Simplified variants were solved by 80 to 93% while no one solved the nine-dot (cited in a30). The model predicted differences across variants, for example that a diagonal first line aids more than a horizontal outward line because it forces criterion failure sooner (a20).

### 2.3 Chronicle, MacGregor and Ormerod 2004: coin problems

This is the main source for move-level evidence (a02 to a10, b01 to b06). The coin problems have a small state space where every legal move can be counted, so move statistics can be compared with the model. Four experiments:

- **Exp 1, six-coin problem** (rearrange six coins into a ring in three moves). N=40, 19 analysed in the Ring condition. 177 first moves; 20 were correct (11.3%) against 11% predicted by a one-lookahead hill climber and 8.3% by chance. Of the 20 correct first moves, 6 had a correct second move (30% vs 33% predicted). All 6 then had a correct third move (100% vs 100%). Mean coins on the ring after move 1 was 4.42 against a chance value of 4.08 (SD 0.49), t(18)=3.02, p<.01. Of 12 distinct first moves, 2 give 5 on the ring (they meet the criterion, trap a coin, and guarantee failure), 9 give 4, 1 gives 3. In the abstract-goal condition (goal stated only in words), 74% said they pictured a ring. Zero ring solutions in the abstract condition against 6 in the ring condition (Fisher p<.01). The two-group solution was found by 5 of 19, close to the chance expectation of 2.2 (power .38).
- **Exp 2, start layout.** Two-move task, N=54, 3 min. Partial-ring start 4/27 (15%) solved; straight-line start 11/27 (41%); chi2(1,54)=4.52, p<.05. The goal and the moves were the same; only the start looked more or less like the tempting ring.
- **Exp 3, goal examples.** N=42. Two-group solvers: Abstract 3/11 (27%), Ring example 3/11 (27%), Two-group example 8/9 (89%), Both examples 10/11 (91%); chi2(3,42)=16.84. The right goal example sped attempts (F(1,20)=18.08, p<.001). The ring example slowed them (F(1,20)=6.92, p<.02).
- **Exp 4, six-coin vs ten-coin.** N=50, 48 usable. Solved within 5 min: six-coin 10 (20.8%), ten-coin 36 (75%); Wilcoxon z=2.67, p=.008. First-attempt solve 0% vs 19%. In the ten-coin problem 69% of first moves fit hill climbing against 17% by chance; 56% of classifiable correct solutions fit hill climbing and 24% fit the "rotational" insight pattern. The authors say CSP predicts the ten-coin is easier (the greedy path lies nearer the answer), and a restructuring account would not.

Side results. Solvers often could not reproduce a ring solution right after finding it: only 2 of 6 reproduced it within a minute; after a demonstration 13 of 19 failed at first (a09). The authors argue part of the "aha" feeling is after-the-fact recoding.

### 2.4 Related coin and nine-dot work from the same group

- **Ormerod, Chronicle and MacGregor (2002), eight-coin problem.** Starting layouts that offer many "strategic" moves (a coin touching three others) lower solving, because these moves look like progress and guarantee failure. Visual hints about the right first move were ignored when such moves were on offer (a11, b23, d08). Abstract only; no numbers.
- **Chronicle, Ormerod and MacGregor (2001), failure of cues.** Shading cues, relevance hints, and both together gave little or no help. Practice drawing the solution shape did not transfer (a12).
- **Ormerod, Chronicle and MacGregor (2001), added dots.** Adding dots that make an arrow shape made the nine-dot easy on the first trial: 73% (13 dots), 60% (12), 50% (11) and 0% (9 dots) first-trial solvers. The authors concede that a perceptual (figural) route is also needed and that dot-turn constraints and CSP cannot explain the first-trial gap (a16).
- **Ormerod et al. (2013), "Act first, think later".** A formal CSP: maximisation picks moves, minimisation limits the space, a criterion evaluates them, lookahead counts the steps tested mentally. New: lookahead zero (take the maximising move untested). Weighing puzzle, N=80: solved 7-ball 9/26 (35%), 8-ball 5/28 (18%), 9-ball 2/26 (8%), chi2(2)=6.01, p=.049. Observed vs predicted frequency over 18 weigh categories r=.96, slope 1.02. 37% of nine-ball participants chose the uninformative 5 v 4 weigh (zero lookahead). Part of the fit is circular for the nine-ball, because lookahead estimates come from Simmel (1953) (a26, a27).

### 2.5 The challengers

**Representational change theory** (Knoblich, Ohlsson and Raney 2001; Ollinger, Jones and Knoblich) says the solver starts with a representation that carries wrong constraints. An impasse follows, and the solution comes when the constraint is relaxed or a chunk is decomposed. See the sibling subfield on representational change. It makes different predictions from CSP about what makes a problem hard: constraint depth, not distance to goal.

**Kershaw and Ohlsson (2001, 2004).** Nine-dot difficulty has several causes (perception, knowledge, process). Their rival account is a habit of turning only on dots and not crossing lines. Training on non-dot turns raised success: facilitating 19/30 (63%), hindering 8/30 (27%), none 11/30 (37%), chi2(2,90)=8.836, p<.05. Within the facilitating group, those who completed training correctly solved 17/19 (89%) versus 2/11 (18%) for those who did not; this split is post hoc (a13 to a15, b09). Removing a single cause moves rates only a little (a32, abstract).

**Perceptual and figural accounts** (Chronicle, Ormerod, MacGregor 2001; Ormerod, Chronicle, MacGregor 2001). The failure of cues and the effect of added dots point to a perceptual component CSP does not cover (a12, a16).

### 2.6 Head-to-head and combined tests

**Jones (2003), the only direct head-to-head test of CSP and representational change in a single study** (a20 to a25, b07, b08, d03). Task: car-park (Rush Hour type) problem solved by moving the taxi first. N=39, 13 per condition: normal, rotated 90 degrees, easy practice. Eye tracking at 50 Hz; 37 usable. Impasse defined as a fixation on a move at or above the participant's own mean plus 2 SD.

- Solved unaided: normal 7/13 (54%), rotated 12/13, easy practice 12/13. Rotated and easy together 24/26 (92%) vs 7/13; Fisher p=.0098 (recomputed). CSP predicts no effect of rotation or practice, since distance to goal is unchanged. Representational change predicts a gain. A gain appeared.
- Lookahead from impasse time: 20 (54%) lookahead one or two, 11 (30%) lookahead three, against 64% / 36% predicted. Deeper lookahead solved faster (92 s vs 43 s; 37 moves vs 21).
- All 30 solvers hit an impasse before the taxi move. Solvers looked at the key region more (24% vs 9% of fixations).
- Jones's verdict: both theories get some support; representational change predicts better. He proposes a merge: progress monitoring says when to leave the current search; representational change says how (a25).

Two limits matter. First, Jones notes that criterion failure is defined from a minimum distance to goal given the moves left, so it is never reached in an unlimited-move task (d03). The test is therefore weak against CSP as stated. Second, lookahead was inferred from the same impasse data used to predict outcomes (a22).

**Ollinger, Jones and Knoblich (2006), matchstick arithmetic** (d04 to d06). N=120. Whether the solution move reduces or increases the distance between the two sides did not change solving (F(1,118)=1.54 ns). Constraint depth did (F(1,118)=37.47, p<.001). Giving a constraint-relaxing move as a partial solution helped far more than giving a value move (F(1,116)=45.15, p<.001). Yet move choice was greedy: of 509 valid equations, 435 (85.46%) reduced distance, 45 (8.85%) were neutral and 29 (5.69%) increased it. So hill climbing describes the move choice but not the difficulty. The authors suggest representational change comes first, then heuristics on the new space; with a larger space heuristics matter more (Kaplan and Simon 1990).

**Ollinger, Jones, Faber and Knoblich (2013), eight-coin.** Six new versions; difficulty came from the 2D constraint and perceptual groupings, and move choice followed the established representation, not the heuristics. Abstract only (a31, b24).

**Ollinger, Fedor, Brodt and Szathmary (2017), ten-penny problem** (a28, a29, b14, b15). N=120 in four groups of 30; 116 analysed. Hints at 5 min; 15 min limit. Solved: control 3/30 (10%), lines hint 2/29 (7%), lines + intersections 6/28 (21%), maximisation hint 21/29 (72%). Maximisation vs control chi2(1,59)=23.80, phi=.64. A constraint relaxation hint alone did nothing. Adding the search criterion lifted solving. This is the cleanest test of the combined account.

### 2.7 Execution as code: ACT-R and PRODIGI

- **Banks, Ormerod, Rusconi and MacGregor (2015).** An ACT-R model of the nine-dot with CSP as a search part and a mechanism that widens the move set. Reproduces impasse, fixation, an aha moment, and relative difficulty of variants. Abstract only (c01).
- **PRODIGI** (Ormerod, MacGregor, Banks, Rusconi 2024; unpublished manuscript under review). Read only through a chapter by Ormerod and Ross (2024) (d01, d02). Progress monitoring stays: hill climbing with a criterion, the ratio of work remaining to resources available. Impasse means no move meets the current criterion. A second heuristic, idea discovery, runs only after impasse. It compares properties of earlier moves (line length, angle, trajectory) with how much progress each move made, learns which property variation changes progress, and tries new values. The nine-dot is solved by finding a property whose variation widens the move set, not by the idea that lines may leave the grid. It has no visual module; it uses a library of properties. The chapter gives a qualitative claim of close fit to human nine-dot performance with no figures. A search summary of Ormerod (2024) in the SAGE journal says PRODIGI replaces CSP; the chapter says it extends it. The chapter is the better source (a33 vs d01).

### 2.8 Other mechanism evidence

- **Move variation.** In the ten-penny task solvers varied attempts more (rate .59 vs .43, t(114)=3.10, d=.67), repeated less, and made fewer attempts (8.41 vs 10.93, d=.62). 47% of solvers used the key feature (intersections) before the hint against 26% of non-solvers (chi2(1,116)=4.56, phi=.20) (b15).
- **Lookahead and working memory** (Chein, Weisberg, Streeter and Kwok 2010). Spatial working memory, a stand-in for lookahead, predicted drawing outside the grid and solving a hint-aided version. Verbal working memory did not. Exp 1: N=51, only 7 (14%) drew outside, 6 of them in the high-spatial group (chi2=4.15, p=.04); 5 solved. Exp 2: N=54, spatial r=.452 (p<.001) vs verbal r=.199 (p=.148), difference one-tailed p=.046 (a17, a18, b11). Indirect, and the standard problem is at floor.
- **Warmth ratings.** Self-rated closeness to the solution stays flat for minutes and jumps only 15 s before the solution (N=25, interaction F=20.60) (b12, replicating Metcalfe and Wiebe 1987, b13). Graf et al. (2023) report both sudden and incremental patterns in other studies, so the dichotomy is not clean (b17).
- **Reinforcement-learning fit.** N=325; people who react positively to negative outcomes did better on eight-coin; success on nine-dot predicted eight-coin success (b21). Indirect.

### 2.9 A timeline of the debate

| Year | Event |
|---|---|
| 1969, 1981 | Nine-dot unsolved in 10 min and in 100 attempts; "go outside the box" fails alone (a20) |
| 2001 | MacGregor, Ormerod, Chronicle: process model; Kershaw and Ohlsson rival; cue failure and added-dot work |
| 2002 | Eight-coin: strategic moves lower solving |
| 2003 | Jones: representational change fits better in car-park task |
| 2004 | Chronicle et al.: coin problems and CSP statement; Kershaw and Ohlsson multiple causes |
| 2006 | Ollinger et al.: greedy move choice, no effect on difficulty in matchsticks |
| 2010 | Chein et al.: spatial working memory and lookahead |
| 2013 | Ormerod et al.: formal CSP with lookahead zero; Ollinger et al. eight-coin |
| 2015 | ACT-R model of CSP |
| 2017 | Ollinger et al.: ten-penny, criterion plus relaxation |
| 2019 | Spiridonov et al.: motor activity, dot-turn training |
| 2023 | Graf et al.: sudden and incremental solution patterns |
| 2024 | PRODIGI (extends CSP, unpublished) |
| 2025 to 2026 | LLM work on stuck detection, progress reports, shifts (section 6) |

No independent replication of the Chronicle 2004 move statistics was found (d07). The main CSP evidence comes from one group.

---

## 3. Core findings with exact numbers

Status uses the schema marks. Numbers are as reported; recomputed ones are marked (r).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Solvers hill-climb on visible progress (six-coin) | first move correct 20/177 = 11.3% vs 11% predicted (8.3% chance); second 6/20 = 30% vs 33%; third 6/6 vs 100%; coins on ring 4.42 vs 4.08, t(18)=3.02; N=19 | a03, a04, b02 (Chronicle 2004 Exp 1) | [S] K01 |
| Inferred goal drives search | 74% pictured a ring from an abstract goal; 0 ring solutions abstract vs 6 ring; separated coins in 6/124 final states (4.8%) vs 16.1% possible | a05, b03 | [S] K02 |
| Start layout alone changes difficulty | partial ring 4/27 (15%) vs straight line 11/27 (41%), chi2(1,54)=4.52 (r) | a06, b04 | [S] (group size inferred) |
| Correct goal example helps; wrong one does not | 3/11, 3/11, 8/9, 10/11; chi2(3,42)=16.84 (r) | a07, b05 | [S] K02 |
| Ten-coin easier than six-coin | within 5 min 36/48 (75%) vs 10/48 (20.8%); z=2.67, p=.008; first attempt 19% vs 0% | a08, b06 | [S] |
| Trap moves lower solving (eight-coin) | numbers not read; many strategic moves = lower solving | a11, b23, d08 | [E] K03 (with Chronicle layout and ten/six-coin) |
| Hints that say "go outside" or give visual cues do not help nine-dot | base rate under 5%; shading and verbal hints minimal gain | a12, b10, a19, a17 | [E] K04 |
| Lookahead mix | 32% / 32% / 36% (depth 1/2/3); weighing 37% zero, 31.5% one or two, 21% three | a20, a26, a27 | [C] K05 (second-hand, reused across tasks) |
| Jones: easy practice and rotation raise solving | 7/13 vs 24/26; Fisher p=.0098 (r); N=39 | a23, b07 | [S] K06 |
| Impasse precedes the key move | 30/30 solvers; mean + 2 SD threshold | a21, a24, b08, b18 | [E] K09 |
| Combined account: criterion plus relaxation | control 3/30, lines 2/29, intersections 6/28, maximisation 21/29 = 10%, 7%, 21%, 72% (r) | a28, b14 | [E] K07 (with eight-coin and Jones merge) |
| Solvers vary more, repeat less | variation .59 vs .43, d=.67; attempts 8.41 vs 10.93; 47% vs 26% early key use | a29, b15 | [S] K08 |
| Spatial working memory predicts going outside the grid | 6 of 7, chi2=4.15, p=.04; r=.452 vs .199 | a17, a18, b11 | [C] K05 |
| Warmth is flat until about 15 s before solution | N=25, F=20.60 | b12 | [E] K10 |
| Training on non-dot turns | Kershaw 63% vs 27% vs 37%; Spiridonov 37.5% (dot) vs 78.1% (non-dot), chi2=10.83 | a14, a30 | [C] K11 |
| Hands-on action benefit did not replicate | N=105/88/74; interactive vs static 0.91/0.87/0.59/0.67 vs 0.94/0.80/0.59/0.69; CrI (-0.73, 0.82) | b20 | [S] |
| Matchstick: greedy moves but difficulty by constraint depth | 85.46% of 509 moves reduce distance; value type F=1.54 ns; depth F=37.47; partial-solution type F=45.15 | d04, d05 | [S] K21 |
| Weighing puzzle fits CSP with lookahead zero | 9/26, 5/28, 2/26 solved; r=.96; 37% chose uninformative weigh | a27 | [S] |
| LLM progress reports fail mid-task | 7 of 11 models comply 93.2 to 100%; 4 comply 0.6 to 10.1%; right 90.6 to 99.4% pre-action; mid-task 5.8 to 11.5% (gpt-4.1, gpt-5.5) | c22 | [E] K13 |
| Uncertainty signals work only at the end | AUROC .85 at completion; <=.60 at 50%; <.70 at 90% | c23 | [E] K14 |
| Token entropy does not predict when a shift helps | pooled OR 0.77, CI [0.58, 1.02], p=.070, N=723,200 | c12 | [E] K14 |
| Spontaneous shifts are rare and go with failure | 6.31% of traces; 2.57% vs 16.44% accuracy (pooled, N=723,200) | c11 | [E] K15 |
| Forced reconsideration helps on math | Math 32.21% to 40.62% (+8.41 pp); crosswords +0.45; Rush Hour +0.01 | c11 | [E] K15 |
| Reflections mostly confirm | >90% confirmatory, <2% corrective; 16.8 to 47.8% of tokens for 1.4 to 3.5 points | d11 | [E] K15 |
| Wrong answers switch more | +225% tokens, +418% switches | c13 | [E] K16 |
| Penalising switch words | AIME24 QwQ 38.3 to 44.1; R1-Distill 61.4 to 64.1; R1 73.8 to 74.8 | c14 | [E] K16 |
| Looping falls with size | 76% (1.5B) vs 37% (32B) at low temperature | c15 | [E] K16 |
| Counter-based stuck rules help | SWE-bench Verified 33.5% vs 28.5% (+5.0 pp); ALFWorld +40.3 pp (Qwen-3-8B), +41.8 pp (GPT-5) | c19, c20 | [E] K17 (bundled) |
| Thresholds are unvalidated | vendor defaults 2/3/6, 3/6, 0.85, 3/20, 4+/3+/6+; no ablation | c18, d15, d16, d17 | [E] K24 |
| Per-step scoring beats final scoring | verbalised AUC .556; trained regression .843 to .907; tree + step value 0.309 vs random tree 0.215 | b26, c21 | [S] K18 |
| Hidden-state probe predicts early | AUC 0.84 at 4 tokens vs 0.59 entropy + length; mostly item difficulty | d09, d10 | [S] K23 |
| Models write the right answer and reject it | 5.23 to 39.34% of wrong answers (4 models) | c05, c06 | [S] K20 |
| No LLM CSP study exists | 0 hits in about 22 searches | c28, d18 | [E] K19 |

---

## 4. Mechanisms and models

This section turns the theory into pieces an engineer can build. Where a value is a guess, it says so.

### 4.1 The CSP ratio

For a task with a countable progress variable and a move or step budget:

```
distance_left   = goal_measure - current_measure          (e.g. dots left, coins to put on ring)
moves_left      = budget - moves_used                      (explicit; set by the harness)
criterion       = distance_left / moves_left               (progress needed per move)
move_gain(m)    = measure_after(m) - measure_now           (progress the move makes)
passes(m)       = move_gain(m) >= criterion
criterion_fail  = no legal move passes  (or, with lookahead k: no k-step path passes)
```

Worked examples from the papers: nine-dot start, 9 dots / 4 lines = 2.25, so a line through 3 dots passes. Six-coin ring: 2 coins short in 3 moves = 0.67 per move, and since coins are whole, the first move must put 5 on the ring (b01). That is the very move that traps a coin and guarantees failure. Notice the structure: the move that meets the criterion at step 1 is the trap, and the criterion failure at a later step is the signal that the representation is wrong.

**Budget denominator.** The ratio needs moves left. In an unlimited-move task it never fires (Jones 2003, d03). In an agent, the harness must set a budget in steps, tool calls or tokens and track it (K22). Our default: steps, with a token cap as a second denominator.

### 4.2 The progress variable

CSP assumes a measure the solver reads off the problem. For an agent that is the hard part. Options, in order of trust:

1. **Exact cost-to-go from a solver.** CAST scores each Rush Hour action by the drop in exact minimum remaining moves from a reverse-BFS table (d13). Possible only for toy puzzles.
2. **Counted checks.** Number of tests passing, number of constraints satisfied, number of grid cells matching, cells filled. The harness counts these. This is the practical analogue of coins-on-ring.
3. **Task-stage markers from state.** Completed subgoals, changed task state, plan revision (d17 says the marker must be external and neither too fine nor too coarse).
4. **Model-estimated progress.** A separate call predicting a residual delta (c21). The weakest; use only with a count behind it.

Do not use the model's own mid-task report as the progress variable (c22, c23, b26, K13, K14).

### 4.3 Goal inference

Chronicle et al. show the solver builds the progress test from goal properties inferred from the text, not from a known goal state (a02). 74% pictured a ring from "each coin touches exactly two others" (a05). The test is only as good as the inferred goal. If the inferred goal is wrong, the criterion measures the wrong thing, and greedy progress points the wrong way. Engineering reading: state the goal property that the progress counter measures, in S1, and keep a rival goal reading. Showing the right goal example is the strongest known aid (89 to 91% vs 27%), and showing the tempting goal hurts (a07).

### 4.4 Lookahead as a budgeted cost

Lookahead depth k means simulating k moves before committing. In people it varies about equally over 1 to 3 (a20). A deeper search sees criterion failure sooner. For an agent, lookahead is a cost in tokens, not a free gift. A policy that buys depth only after the criterion fails (cheap checks first, expensive simulation second) is untested (K05, critique gap 5). In a text puzzle with a state simulator, lookahead can be done in code, not by the model: the harness expands k plies and returns the best progress reachable.

### 4.5 Impasse detection

CSP defines impasse as no move meeting the current criterion (d01). Behavioural correlates: inactivity and repeated candidate solutions (b18); the longest fixation of the run precedes the key move in every solver, using a per-person mean + 2 SD cut (a21, a24). For an agent:

```
impasse := criterion_fail
        OR repeated_state(n)            # same action or same state n times
        OR progress_flat(m)             # progress variable unchanged for m steps
        OR outlier_burst(mean + 2 SD)   # token or latency burst relative to this run
```

The counter parts are what deployed systems use: same action 3 to 4+ times, 5 low-progress scores in a row, nonzero return codes, one file edited too often (c17 to c20). None of the thresholds has been validated (K24).

### 4.6 What to do at impasse: the combined account

The best-supported design from section 2.6: progress monitoring fires; a re-representation step runs; then the criterion is applied again in the new space.

1. **Trigger.** Criterion failure with explicit budget.
2. **Change.** Force a change of representation or a drop of a constraint (O6, O4). The Ollinger tasks favour this for symbolic problems (K07, K21).
3. **PRODIGI step.** Look at logged moves and their progress gains. Find a move property that was never varied (angle, size, order, object type). Propose moves that vary it. This is a code-friendly idea because the harness already keeps a move log (d02).
4. **Re-score.** After the change, recompute the criterion. If the search space is larger, add heuristics back (d06).

Evidence that the second step needs the first: relaxing a constraint without a criterion gave no benefit (7% vs 10%), but a criterion with relaxation gave 72% (b14). Evidence that the first needs the second: the maximisation hint alone is an almost-partial answer, so this is not a pure test (b14 limits).

### 4.7 A reading of the causal chain

```
goal text  ->  inferred goal properties  ->  progress variable
                                                |
            greedy move choice  <-------------- +
                    |
                    v
          criterion check each step (distance_left / moves_left)
                    |            \
                  pass            fail -> impasse -> relax demand / widen move set
                    |                                      |
                 continue                       representation change or property variation
```

The most important engineering point is that the loop has two places where it can fail. The goal can be wrong (stage 1) and the progress measure can mislead (stage 2). Criterion failure alone fixes neither; it only says that the current approach cannot finish.

### 4.8 Neural and RL models

A neural model of the four-tree problem names inactivity and repeated candidates as impasse correlates and shows primed-but-not-pretrained was best (b18). A Q-learning fit shows reaction to negative outcomes predicts success on eight-coin and nine-dot (b21). Both indirect.

---

## 5. What holds up

### 5.1 Replications and independent confirmation

- **Trap moves lower solving.** The finding that layouts with many progress-looking trap moves reduce solving is supported by Chronicle (partial-ring vs straight-line; six-coin vs ten-coin) and Ormerod 2002 (eight-coin). Two groups of papers, one lab. Marked [E] in K03 on the count of tasks, but the independent-lab count is still low.
- **Hints that give no content do not help.** Consistent across Burnham and Davis, Weisberg and Alba, Chronicle 2001, Kershaw and Ohlsson (K04). Three or more groups.
- **Maximisation plus relaxation.** Ollinger 2017 (ten-penny) and Ollinger 2013 (eight-coin) and Jones's merge (K07). An outside group, with a clean ablation.
- **Impasse before the key move.** Jones 2003 and a neural model (K09).
- **Felt progress is flat.** Metcalfe and Wiebe 1987 and Chein 2010 (K10). Graf et al. 2023 show sudden and incremental patterns both occur.

### 5.2 Failures, boundary conditions, competing explanations

| Issue | What happened | Source |
|---|---|---|
| No independent replication of the move statistics | 30 Europe PMC citing records, none repeats the 11.3% / 30% / 100% test; wider citation APIs were rate-limited | d07 |
| CSP's own fit used free parameters | lookahead mix was fitted; weighing fit uses estimates from other tasks | b02, a27 |
| Jones 2003 favours representational change | easy practice and rotation raised solving though distance to goal was unchanged | a23, b07 |
| Same test is weak against CSP | criterion failure cannot fire in an unlimited-move task | d03 |
| Matchsticks reverse the balance | greedy move had no effect on difficulty; constraint depth did | d04 |
| Eight-coin | new versions point to the 2D constraint and groupings | a31 |
| Dot-turn training goes both ways | Spiridonov: dot-turn training 37.5% vs non-dot 78.1%; Kershaw: hindering training not significantly worse than control (27% vs 37%) | a30, a14 |
| Perceptual route needed | added dots make nine-dot easy on trial 1; 73% to 0% | a16 |
| Hands-on benefit | not reproduced in three experiments | b20 |
| Lookahead as working memory | Lavric 2000 and Fleck 2008 find no working-memory role in insight problems; Chein disputes for nine-dot | a19 |
| Chein is indirect | span as stand-in for lookahead; the standard problem is at floor (5/51 solved) | a17 |
| Sample sizes | N=19 per cell in the key test; N=39 in the only head-to-head test | a03, a23 |
| Founding paper | never opened | a01 |

### 5.3 Moderators

- **Task type.** Spatial puzzles with tight budgets (nine-dot, coins, weighing) favour CSP. Symbolic tasks (matchsticks) favour representational change. Larger spaces bring heuristics back (d06). Unlimited-move tasks break the ratio (d03).
- **Lookahead depth.** About one-third each at 1, 2, 3; spatial capacity relates to success (K05).
- **Goal conception.** Start layout, goal example and the stated goal all move results (K02).
- **Expertise, culture.** No moderator found. Samples are undergraduates in the UK, USA, Germany and Japan (b30).
- **Hints and timing.** The ten-penny hint came at 5 min, which confounds timing and content (b14).

### 5.4 Interventions that worked and did not

| Worked | Did not work |
|---|---|
| Showing the correct goal example (89 to 91% vs 27%) (b05) | Showing the tempting goal (27%, slowed search) (b05) |
| Maximisation hint with relaxation (72% vs 10%) (b14) | Relaxation hints alone (7%) (b14) |
| Non-dot-turn training (63% vs 37%) (a14) | Generic "go outside the box" or visual cues (a12, b10) |
| Added dots / arrow shape (a16) | Practice drawing the solution shape (a12) |
| Rotation or easy practice in car park (92% vs 54%) (a23) | Hands-on interaction (b20) |
| Giving a constraint-relaxing partial move (matchstick F=45.15) (d04) | Giving a greedy value move (d04) |

### 5.5 Overall evidence quality

No meta-analysis exists. Direct tests have 39 to 120 people (b30). The strongest independent outcome is that a criterion for progress plus a change of representation beats either alone. The weakest links are the move-statistics fit (single lab) and the lookahead mix (second-hand).

---

## 6. Language models

### 6.1 Direct tests of CSP on LLMs

None. About 22 searches across both passes found no study that gives an LLM the nine-dot, coin or matchstick problems with a progress measure, tests a lookahead budget against greedy traps, or tests goal inference from an abstract statement (c28, d18, K19). Everything below is indirect.

### 6.2 How LLMs do on insight-like tasks

- BRAINTEASER: best model about 63% (sentence) and 53% (word) against 25% random and 92% human (102 items); multiple choice, 2023 models (c08).
- NazoNazo (201 Japanese riddles, 38 models): humans 52.9% (n=126), non-reasoning models 7.6%, reasoning models 17.6%. Verification failures: the model writes the right answer in its thoughts and then moves on, 5.23 to 39.34% of wrong answers across four models (Gemini 2.5 Flash Preview lowest, Grok 4 highest). Opus 4: 61 correct and 35 failures of 201 (c05). Reasoning-inclusive demonstrations improved all four models, significantly in two (c06).
- ChatGPT on 30 verbal insight problems: 7/15 practice, 5/15 transfer; tiny human sample (c03).
- Mental set: GPT-4o took the long route; zero-shot chain of thought gave 3 steps in every cell; six problems per cell (c07).
- Black Stories (summary only): GPT-4 fixated on details and summarised too early (c09).

None of these is instrumented for progress.

### 6.3 Progress reports

Wang, Wang and Wu (2026), "Unreliable Progress Bar", verified against the full text (c22): in tau2-bench telecom, 11 models. Seven follow the reporting duty at 93.2 to 100% of checkpoints; four at 0.6 to 10.1%. gpt-4.1 and gpt-5.5 are right at 90.6 to 99.4% of pre-action checkpoints and 87.3 to 88.9% after completion, but only 5.8 to 11.5% mid-task. 82 to 90% of mid-task errors name a state the agent has already left; 10 to 18% claim completion too early. Three newer models reach 74 to 100% mid-task but only 48 to 64% at completion. The stage tag is a lifecycle stage, not a problem-solving progress.

Li et al. (2026), "Last Step Matters" (c23): verbal confidence at completion gives mean AUROC 0.85 over 15 model-benchmark pairs. At 50% of the trajectory no metric exceeds 0.60; at 90% all stay under 0.70. Path switches are common (86.8% of BrowseComp trajectories, 8.5 each). Late confidence rises 15 points in successes and falls 6 in failures.

Mavi et al. (2025) (b26): per-step scoring beats final scoring; verbalised confidence is near chance (AUC .556 on GSM8K); a trained regression scorer reaches .843 to .907. Llama-3.2-11B; workshop paper.

Reading: the model's own progress claim is acceptable at the start and the end and poor in the middle, which is where CSP needs it. Compute progress from task state.

### 6.4 Strategy shifts and aha

Illusion of Insight (2026; c11, c12). Over 11M traces from GRPO-trained small models. Mid-trace shifts occur in 6.31% of traces; formal aha moments fire on about 1.79% of samples. Pooled accuracy with a shift 2.57% vs 16.44% without (N=723,200). The Qwen2.5-1.5B all-domain row differs: 7.65% shifted, 3.95% vs 20.42%. Forced reconsideration: Math 32.21% to 40.62% (+8.41 pp; 50,574 wrong-to-right against 23,500 right-to-wrong); crosswords +0.45 pp; Rush Hour +0.01 pp. Token entropy did not predict when a shift helps (pooled OR 0.77, p=.070). The detector is a lexical filter plus a GPT-4o judge (kappa 0.73 to 0.79). Correction from the cross-check: the "pooled 6.6% vs 29.0%" figure was not found in the text and is dropped.

First Try Matters (d11): across eight reasoning models on math, over 90% of reflections after a first answer are confirmatory, under 2% corrective, using 16.8 to 47.8% of tokens for a 1.4 to 3.5 point gain. Early stopping saves 24.5% of reasoning tokens at up to 2.9% accuracy loss. No closed frontier model.

Switching and looping: wrong answers use 225% more tokens and 418% more thought switches (c13). Penalising switch words raised AIME24 pass@1 for QwQ from 38.3 to 44.1, R1-Distill from 61.4 to 64.1, R1 from 73.8 to 74.8 (c14). A prompt version did not help R1. Looping at low temperature is 76% in Qwen-1.5B against 37% in Qwen-32B (c15); a CUSUM change-point on early signals predicts loops (c16, abstract only).

Reconciling the switch results: forced reconsideration helps while reducing spontaneous switching also helps. The most likely explanation is that timing and trigger matter, not switch frequency. Untested (critique).

### 6.5 Stuck detection in deployed agents

| System | Rule | Result | Isolated? |
|---|---|---|---|
| Reflexion (c17) | same action and response more than 3 cycles, or more than 30 actions | 130 of 134 ALFWorld tasks | no ablation of thresholds |
| OpenHands (c18) | same action and observation 4+; same error 3+; 3+ empty messages; alternation 6+ cycles | docs only | no |
| Zhang 2026 (c19) | nonzero return codes, over-edited file, repeated normalised action | SWE-bench Verified 33.5% vs 28.5% (+5.0 pp); plan-only 148.7, memory-only 150.7, both 167.3 resolved | no, bundled |
| ReflexGrad (c20) | 5 low-progress scores in a row open a slow diagnosis gate | ALFWorld 35.1% to 75.4% (Qwen-3-8B), 46.3% to 88.1% (GPT-5) | not read beyond abstract |
| OpenRouter (d15) | observe at 2, block at 3, stop at 6 | none | no |
| DeepEval (d16) | repetition 3 (score 0.5), 6 (0.0); similarity 0.85 / 0.95 | none | no |
| OneUptime (d17) | repeat 3, action cap 20, external progress marker | none | no |
| Cognitive Companion (d12) | LLM check every 2 steps; probe at 0.55 | repetition Jaccard 0.367 to 0.176 on one task; small models improved 0 of 6 | no; labels from the same model |

The gains are real but bundled with planning, memory, or reflection. No head-to-head of counter, entropy and criterion triggers exists (K24).

### 6.6 Progress estimators

- Residual delta critic (BAVT, c21): parallel 0.268, tree with random choice 0.215, tree + step value 0.309, full budget-aware 0.388 (OSS-20B, four multi-hop QA sets). Delta values are the model's opinion.
- Tree of Thoughts (c24): Game of 24 7.3% (IO), 4.0% (CoT), 9.0% (CoT-SC k=100), 45% (ToT b=1), 74% (b=5), 49% (best of 100 CoT). Pruning dead ends with an evaluator. The evaluator is the same model.
- CAST (d13): exact cost-to-go deltas on Rush Hour 6x6 with 7 vehicles. Qwen3-4B ReAct 1.1% in-domain; GRPO 53.8%; CAST 64.7%. Gemini 2.5 Pro 92.0%; Opus 4.6 92.6%. Training paper, not a monitoring study, and it does not analyse greedy traps.
- MentisOculi (d14): with a text transcription of Rush Hour, Gemini 3 and GPT-5.1 match humans; sub-chance results are blamed on early termination and under-used budget, not greedy traps.
- Hidden-state probes (d9, d10): AUC 0.84 at 4 tokens against 0.59 for entropy + length on Qwen3-8B, 1,500 prefixes; mostly tracks item difficulty; horizon is about one step on compositional tasks. Needs open weights.
- ProgRouter, path deviation index, Sophia loops (b27 to b29): abstracts only; need logits or activations; no numbers.

Takeaway for design: frontier models solve standard 6x6 text Rush Hour at about 92%, so the traps for a test must be harder than standard boards (d13, d14).

### 6.7 What changed behaviour and by how much

- Forced external reconsideration at a computed point: +8.41 pp on math for small models; near zero on crosswords and Rush Hour (c11).
- Hard-coded progress gate and slow diagnosis: +40 pp ALFWorld (c20; large gain over a weak baseline).
- Planning + memory + stuck rule: +5.0 pp SWE-bench (c19).
- Switch penalty in decoding: +1.0 to +5.8 points AIME (c14), needs logits.
- Reasoning-inclusive demonstrations: improved all four models on NazoNazo, significantly for two (c06).
- Verbal "be careful" or reflection prompts: no help; see SCHEMA 4b and d11.

---

## 7. What our agent should take

Schema part key: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Do not use the model's mid-task self-report of progress or its verbal confidence as a trigger.** Reports are fine at start and end; mid-run they fail (5.8 to 11.5% right mid-task; AUROC at most .60 at 50%). Compute progress from task state. This extends G10 (reasoning text is not evidence) and the "verbal confidence to stop" row of 4b to mid-run monitoring | G10 / 4b | [E] | c22, c23, b26, b12 (K10, K13, K14) |
| A2 | **Impasse detector uses counted signals.** Fire S6 on code-computed signals only: repeated action or state, flat progress, outlier burst. Same-action counters are the deployed standard (+5.0 pp SWE-bench, bundled) | S5/S6 | [E] | c17 to c20, a21, a24, b08 (K09, K17) |
| A3 | **Impasse is a per-run outlier, not an absolute number.** Use the run's own mean + 2 SD for latency or token bursts; in humans, 30/30 solvers had the longest fixation before the key move | S6 | [E] | a21, a24, b08 (K09) |
| A4 | **Generic reset prompts do not help.** "Go outside the box", "think differently", or visual cues alone gave under 5% in the nine-dot. A hint helps only if it gives content. At impasse the operator must carry content (a named constraint to drop, a named representation) | S6 / O4 / O6 | [E] | a12, b10, a19 (K04); consistent with 4b |
| A5 | **At impasse, the combined step: a progress criterion plus a forced change of representation.** Relaxation alone gave 7% against 10%; a criterion with relaxation gave 72% | S6 / O4 | [E] | a28, b14, a25, b24 (K07) |
| A6 | **Forced external reconsideration beats waiting for a spontaneous aha.** Shifts occur in 6.31% of traces and go with failure; forced reconsideration gave +8.41 pp on math. Do not rely on, or reward, spontaneous "wait" pivots | G1 / S5 | [E] for small open models on math | c11, c12, d11 (K15) |
| A7 | **Treat excess switching and looping as failure signals, detected from text and actions by code.** Wrong answers use 418% more switches; loops reach 76% in a 1.5B model | S6 / G11 | [E] | c13, c14, c15, c16 (K16) |
| A8 | **Keep a move log and mark trap risk.** Layouts with progress-looking trap moves lower solving. Log, per step, the progress gain of the move taken. Do not treat the greedy-best move as safe on a problem with a known trap class | G1 / S3 | [E] | a08, b04, b06, a11 (K03) |
| A9 | **Do not calibrate any agent parameter on the human move rates (11%, 30%, 100%, 32/32/36 lookahead).** Single lab, N=19, second-hand mix | none | [E] (as a prohibition) | d07, a03 (K25) |

### Test first (single-source, contested, or no LLM evidence)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **CSP ratio computed by the harness (distance left / budget left) as the impasse trigger**, against a counter trigger and an entropy trigger | S6 | [S] | a02, b01, d01, d03, c22 (K01, K22, K24) |
| T2 | **Criterion failure triggers forced re-representation (O6, O4) before lookahead**, vs trigger plus extra lookahead | S6 / O4 / O6 | [C] (human tasks disagree: Jones, Ollinger 2006 vs Chronicle) | a23, d04, d06 (K06, K21) |
| T3 | **PRODIGI step**: after impasse, find a move property never varied in the log and force variation | S6 / O5 (variation) | [S] | d02, b15 (K08, K12) |
| T4 | **Variation-rate monitor** (distinct approaches per attempt); low variation precedes failure | S3 / S6 | [S] | a29, b15 (K08) |
| T5 | **Explicit step or token budget stated to the model and tracked in code** (needed for any ratio) | S0 / G12 | [S] | d03, d01 (K22) |
| T6 | **Goal-property restatement in S1**: name the inferred goal property that the progress counter measures, and a rival | S1 | [S] | a05, b05 (K02) |
| T7 | **Goal example for the true goal vs the tempting goal** (S1/S2 input) | S1 | [S] | b05 (K02) |
| T8 | **Lookahead budget bought only after criterion failure** | S4 / G12 | [C] | a22, a27, a17 (K05) |
| T9 | **Residual-delta progress call from a separate critic**, compared with random pruning | S2 / S5 | [S] | c21, b26, d13 (K18) |
| T10 | **Answer-recognition step** that checks whether a rejected intermediate answer was correct | S4 | [S] | c05, c06 (K20); already covered by S4 harvesting |
| T11 | **Content-specific worked example of the key move type** vs generic examples | memory | [C] | a14, a30, a15 (K11) |
| T12 | **Threshold sweep** for repeats (2, 3, 4, 6) and window size, with false-positive logging | S6 | [S] | d15 to d17, c18 (K17, K24) |

---

## 8. Concrete tests on our bench

All tests give both arms the same total token budget, counting setup and monitor calls (G7). Items are text versions run through the harness (bench skill). Report solve rate with a binomial interval, tokens per solve, and false-positive rate of any trigger.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| **B1** Does the agent take the greedy trap? | Text six-coin and ten-coin problems, text nine-dot with a fixed 4-line budget, plus the eight-coin trap family; a simulator returns progress counts | one arm, observational: log first-move progress gain | rate of the maximising move; time to solve; compared with a one-step maximiser | If above 50%, the trap structure transfers to the model. Unknown; no prior (K19) |
| **B2** Trap-density knob | Puzzle family with trap density 0, low, high (eight-coin style strategic moves; sliding-block boards harder than standard 6x6) | plain vs plain + criterion check | solve rate vs density | Solve rate falls with density (as in humans); check restores part of it |
| **B3** Trigger comparison | B2 items with a known trap | (a) counter trigger (same state 3x, flat 4 steps); (b) entropy or verbal-confidence trigger; (c) computed criterion failure with explicit budget; all fire the same intervention | resolved rate; tokens per solve; false-positive rate on solved-fast items; time-to-fire | (c) at least equal to (a), both beat (b). Expect (b) near no-trigger (c12, c23) |
| **B4** Re-representation vs lookahead at criterion failure | Symbolic items (matchstick-like equations as text, ten-penny-style counting puzzles) and spatial text items | (a) trigger + forced O6/O4; (b) trigger + k-step simulated lookahead; (c) trigger + both in sequence | resolved rate by item type | Symbolic: (a) > (b) (d04). Spatial text with trap: (b) may catch up (a02) |
| **B5** Criterion alone vs relaxation alone vs both | Two-obstacle puzzles (ten-penny-like: wrong constraint plus wrong objective) | relaxation prompt; criterion prompt; both | resolved rate | Both > either (b14: 72% vs 7% and 21%) |
| **B6** Self-report vs computed progress | B2 items, checkpoint every 3 steps | model-reported "how close" vs harness count | AUROC for eventual success at 25, 50, 75% of the run | Computed > reported at 25 and 50% (c23) |
| **B7** Budget denominator | B2 items with and without a stated step budget | no budget vs budget in prompt and tracker | time of first ratio over 1; solve rate | Budget arm fires earlier; may help only on tight puzzles (d03) |
| **B8** Goal-example effect | Text coin items with an abstract goal | abstract goal; true-goal example; tempting-goal example; both | solve rate; goal the agent states | True example gives large gain; tempting example hurts (b05). Check whether the model also infers a ring |
| **B9** Variation forcing | Items where agents repeat a pattern | (a) no forcing; (b) force a never-varied move property when variation rate drops below the run median (PRODIGI); (c) generic "try something different" | resolved rate; distinct-approach count | (b) > (c) = (a) (a12 for the (c) null) |
| **B10** Threshold sweep | Mixed task set | repeat thresholds 2, 3, 4, 6; windows | resolved rate; false positives | Find the knee; likely varies with difficulty |
| **B11** Lookahead budget after failure | B2 high-density items | lookahead from step 1; lookahead only after failure; none | tokens per solve | After-failure is cheaper at equal solve rate |
| **B12** Spontaneous vs forced | Math and puzzle items | no intervention; harness reconsideration at computed impasse; forced reconsideration every n steps (G1 control) | resolved rate; tokens | Computed impasse > fixed schedule (G1); both > none on math (c11) |

Run B1 and B3 on frontier models, not only small ones (critique gap 10: spontaneous revision in frontier models is untested).

---

## 9. What does not transfer, and why

- **The exact numbers.** The 11%, 30%, 100% and 32/32/36 figures come from undergraduates on tiny spatial puzzles with N=19 per cell. A model has different lookahead (it can enumerate) and different memory (it can write the log). Do not calibrate to them (K25).
- **Lookahead as working memory capacity.** Human lookahead is limited by spatial span (r=.452). An LLM has no spatial span; its limit is attention and tokens. Chein's result does not say what limits the model.
- **Hand-drawn nine-dot.** The perceptual and motor routes (arrow shape, 73% to 0%; motor activity) have no counterpart in a text agent.
- **Felt warmth.** Human warmth ratings are flat until 15 s before solving. The model's report fails mid-task for different reasons (it names a state already left, 82 to 90% of errors). Same conclusion (compute progress), different cause.
- **The "aha" itself.** The Illusion of Insight work shows that a model's visible aha is rare and linked to failure. Do not look for or reward an aha in the trace (G10).
- **Insight as sudden change.** Graf et al. show both sudden and incremental patterns; the dichotomy is not clean. An engineer should not design for a sudden jump.
- **Unlimited-move tasks.** The ratio is undefined. Many open agent tasks (research, writing) have no clean distance. For these, use the counters and external markers (d17); CSP cannot be computed.
- **Open-ended tasks without a progress variable.** The Cognitive Companion ran on essay-like tasks and gave no usable result (d12).
- **Hidden-state probes and logit penalties.** Strong signals (AUC 0.84 at 4 tokens; +5.8 AIME points) but need open weights. Not for an API-only agent (d09, c14, b27, b28).
- **Training-based methods.** CAST and the GRPO papers train; we do not.
- **Easy boards.** Frontier models solve 6x6 text Rush Hour at about 92% (d13). Standard boards will not show a trap effect.
- **Small samples from one lab.** The CSP evidence is weak on independent sources, so claims of "how people think" are held loosely.

---

## 10. Open questions

1. Does the CSP ratio computed from the agent's own state predict stuck and success better than token signals? No LLM study exists (critique gap 1).
2. Does a harness-computed criterion failure, used as the trigger for forced re-representation, beat a counter and entropy at equal tokens? This is the main design decision for S5/O4 (gap 2).
3. Can an independent lab reproduce the Chronicle 2004 move statistics? Is a Bayesian reanalysis available? (gap 3)
4. What does the PRODIGI paper itself say? Does idea discovery change what the monitor computes? Only the chapter was read (gap 4).
5. Does explicit lookahead budget change falls into greedy traps in LLMs? Should lookahead be bought only after criterion failure? (gap 5)
6. What goal does an LLM infer from an abstract statement, and does a true-goal example fix it? (gap 6)
7. Which trigger thresholds are best, and do they shift with difficulty? Current values 2, 3, 4, 6 are hand-chosen, no ablation (gap 7).
8. Can mid-run progress be estimated from the model at all via API (separate-call, residual delta, external critic)? (gap 8)
9. Does the matchstick result (representational change leads) transfer to verbal tasks? Jones is spatial; Ollinger 2006 is symbolic; neither is prose (gap 9).
10. Do spontaneous revisions help in frontier models, and does the 6% shift rate hold? The studies cover small and open models, math (gap 10).
11. Does reducing switching (TIP) conflict with forcing reconsideration? Likely timing, not frequency. Untested.
12. Is the founding MacGregor 2001 paper consistent with the second-hand numbers (lookahead mix, Exp 1 and 2 solve rates)?
13. What progress variable is available in open tasks (code, research)? Test counts and external markers.
14. How should a stuck rule balance false positives (interrupting a good run) against recall? No data in any deployed system.

---

## 11. Sources

[V] opened (page or full text read this session); [M] snippet, abstract or search summary only.

**Human studies**

- [M] MacGregor, Ormerod, Chronicle (2001) Information processing and insight: a process model of performance on the nine-dot and related problems. https://doi.org/10.1037/0278-7393.27.1.176 ; https://eprints.lancs.ac.uk/id/eprint/3614 (a01, b22)
- [V] Chronicle, MacGregor, Ormerod (2004) What makes an insight problem? Roles of heuristics, goal conception and solution recoding in knowledge-lean problems. https://eprints.lancs.ac.uk/id/eprint/558/2/Chronicle_et_alJEP_LM%26C_03.pdf ; https://doi.org/10.1037/0278-7393.30.1.14 (a02 to a10, b01 to b06, c02 abstract)
- [V, abstract page] Ormerod, Chronicle, MacGregor (2002) Dynamics and constraints in insight problem solving. https://eprints.lancs.ac.uk/id/eprint/3613/ (a11, b23, d08)
- [V, abstract page] Chronicle, Ormerod, MacGregor (2001) When insight just won't come: the failure of visual cues in the nine-dot problem. https://eprints.lancs.ac.uk/id/eprint/10441/ (a12)
- [V] Kershaw, Ohlsson (2001) Training for insight: the case of the nine-dot problem. https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/0489.pdf (a13 to a15, b09, b10)
- [M] Kershaw, Ohlsson (2004) Multiple causes of difficulty in insight: the case of the nine-dot problem. https://doi.org/10.1037/0278-7393.30.1.3 (a32)
- [V] Ormerod, Chronicle, MacGregor (2001) Facilitation in variants of the nine-dot problem: perceptual or cognitive? https://journalpub.escholarship.org/cognitivesciencesociety/article/32517/galley/23582/download (a16)
- [V] Chein, Weisberg, Streeter, Kwok (2010) Working memory and insight in the nine-dot problem. https://link.springer.com/content/pdf/10.3758/MC.38.7.883.pdf ; https://doi.org/10.3758/MC.38.7.883 (a17 to a19, b11, b12)
- [M] Metcalfe, Wiebe (1987) Intuition in insight and noninsight problem solving; reported in Chein 2010. https://doi.org/10.3758/MC.38.7.883 (b13)
- [V] Jones (2003) Testing two cognitive theories of insight. https://irep.ntu.ac.uk/id/eprint/18103/ ; https://ntu.eprints-hosting.org/id/eprint/18103/1/196105_RUNNING%20HEAD%20v2%20%28Item%20Ref.%20330%20Jones%20PrePublisher%29.pdf (a20 to a25, b07, b08, d03; pre-publication copy)
- [V] Ormerod, MacGregor, Chronicle, Dewald, Chu (2013) Act first, think later: the presence and absence of inferential planning in problem solving. https://link.springer.com/article/10.3758/s13421-013-0318-5 (a26, a27)
- [V] Ollinger, Fedor, Brodt, Szathmary (2017) Insight into the ten-penny problem: guiding search by constraints and maximization. Psychological Research 81, 925-938. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5533865/ (a28, a29, b14, b15; b16 for the 2014 Ollinger, Jones, Knoblich paper cited in it, [M])
- [V] Spiridonov, Loginov, Ivanchei, Kurgansky (2019) The role of motor activity in insight problem solving (nine-dot). https://www.frontiersin.org/articles/10.3389/fpsyg.2019.00002/pdf (a30, b19)
- [M] Ollinger, Jones, Faber, Knoblich (2013) Cognitive mechanisms of insight: the role of heuristics and representational change in solving the eight-coin problem. https://doi.org/10.1037/a0029194 (a31, b24)
- [V] Ollinger, Jones, Knoblich (2006) Heuristics and representational change in two-move matchstick arithmetic tasks. https://ntu.eprints-hosting.org/id/eprint/25198/1/197400_2107%20Jones%20Publisher.pdf (d04 to d06; b25 [M] repository abstract at https://irep.ntu.ac.uk/id/eprint/25198/)
- [V] Graf, Danek, Vaci, Bilalic (2023) Tracing cognitive processes in insight problem solving: GAMs and change-point analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (b17)
- [V] Spiridonov, Erofeeva, Klowait, Morozov, Ardislamov (2025) Sources of difficulty in interactive matchstick problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC12862482/ (b20)
- [V] Kobe University Q-learning study (2023) of insight problem solving and loss. https://pmc.ncbi.nlm.nih.gov/articles/PMC10800724/ (b21)
- [V, partial] Europe PMC citation list for Chronicle et al. 2004. https://www.ebi.ac.uk/europepmc/webservices/rest/MED/14736293/citations?format=json&pageSize=100 (d07)

**Models**

- [V, abstract] Banks, Ormerod, Rusconi, MacGregor (2015) Modelling insight: the case of the nine-dot problem. https://journalpub.escholarship.org/cognitivesciencesociety/article/25864/galley/15488/download (c01)
- [V] Fedor, Zachar, Szilagyi, Ollinger, de Vladar, Szathmary (2017) Cognitive architecture with evolutionary dynamics solves insight problem. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.00427/pdf (b18)
- [V] Ormerod, Ross (2024) Modelling insight as a creative domain: process or phenomenology? https://repository.londonmet.ac.uk/9827/8/Ormerod%20and%20Ross%20chapter_final%20%281%29%20%281%29.pdf (d01, d02)
- [M] Ormerod (2024) How many heuristics are enough? Testing a parsimonious theory of possibility generation in problem solving. https://journals.sagepub.com/doi/full/10.1177/27538699241237321 (a33; search summary only; publisher page blocked)

**LLM studies and tools**

- [V] Orru, Piarulli, Conversano, Gemignani (2023) Human-like problem-solving abilities in large language models using ChatGPT. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10244637/ (c03)
- [V] Speed (2023) Assessing the nature of large language models: a caution against anthropocentrism. https://arxiv.org/pdf/2309.07683 (c04)
- [V] Mizumoto et al. (2025) The Metacognitive Bottleneck (NazoNazo). https://arxiv.org/pdf/2509.14704 (c05, c06)
- [V] Haq et al. (2025) Is your LLM trapped in a Mental Set? https://arxiv.org/pdf/2501.11833 (c07)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/pdf/2310.05057 (c08)
- [M] Leiden CogSci study of GPT-4 vs humans on Black Stories. https://escholarship.org/uc/item/38m599bg (c09)
- [V, abstract] LatEval (2023). https://arxiv.org/abs/2308.10855 (c10)
- [V] The Illusion of Insight in Reasoning Models (2026). https://arxiv.org/html/2601.00514v1 (c11, c12)
- [V] Wang et al. (2025) Thoughts Are All Over the Place. https://arxiv.org/pdf/2501.18585 (c13, c14)
- [V] Pipis et al. (2025/2026) Wait, wait, wait... Why do reasoning models loop? https://arxiv.org/pdf/2512.12895 (c15)
- [V, abstract] Duan et al. (2026) Circular Reasoning. https://arxiv.org/abs/2601.05693 (c16)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/pdf/2303.11366 (c17)
- [V] OpenHands SDK docs, agent stuck detector. https://docs.openhands.dev/sdk/guides/agent-stuck-detector (c18)
- [V] Zhang et al. (2026) Coupling planning with episodic memory in LLM agents for software issue resolution. https://arxiv.org/pdf/2608.06811 (c19)
- [V, abstract] ReflexGrad (2025). https://arxiv.org/abs/2511.14584 (c20)
- [V] Li, Deng, Li, Li (2026) Budget-Aware Value Tree search. https://arxiv.org/pdf/2603.12634 (c21)
- [V] Wang, Wang, Wu (2026) The Unreliable Progress Bar. https://arxiv.org/pdf/2609.08589 (c22)
- [V] Li et al. (2026) Last Step Matters. https://arxiv.org/pdf/2608.29685 (c23)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/pdf/2305.10601 (c24)
- [M] Notion note on action looping and entropy collapse. https://torpid-telephone-b59.notion.site/Detecting-and-Controlling-Action-Looping-in-LLM-Agents-via-Entropy-Collapse-2f1cfa5f227d806f99befa51e29c2f2c (c25)
- [M] pydantic-deepagents stuck-loop detection (search summary) (c26)
- [M] InsightBench thesis and Logic-RL findings. https://dataspace.princeton.edu/handle/88435/dsp01mg74qq49s (c27)
- [V] Mavi, Jaroria, Sun (2025) Self-evaluating LLMs for multi-step tasks. https://arxiv.org/abs/2511.07364 (b26)
- [M] Sophia self-loop steering (2026). https://arxiv.org/abs/2607.18100 (b27)
- [M] Reasoning path deviation monitoring (2026). https://arxiv.org/abs/2603.14251 (b28)
- [M] ProgRouter (2026). https://arxiv.org/abs/2608.25992 (b29)
- [V] David (2025) Temporal Predictors of Outcome in Reasoning Language Models. https://arxiv.org/pdf/2511.14773 (d09)
- [V] Xu et al. (2026) How Far Ahead Do LLMs Plan? https://arxiv.org/pdf/2602.02103 (d10)
- [V] Kang et al. (2025) First Try Matters. https://arxiv.org/pdf/2510.08308 (d11)
- [V] Cognitive Companion (2026). https://arxiv.org/abs/2604.13759 (d12)
- [V, first 100k characters] CAST (2026). https://arxiv.org/abs/2607.25308 (d13)
- [V] MentisOculi (2026). https://arxiv.org/abs/2602.02465 (d14)
- [V] OpenRouter doom loop detection docs. https://openrouter.ai/docs/agent-sdk/call-model/doom-loop-detection.md (d15)
- [V] DeepEval agent loop detection metric docs. https://deepeval.com/docs/metrics-agent-loop-detection (d16; c26 [M])
- [V] OneUptime (2026) Detect tool-call loops. https://oneuptime.com/blog/post/2026-09-12-detect-tool-loops-dead-ends-production-agents/markdown (d17)
- [M] Gap search record (c28, d18): about 22 searches and arXiv API queries; zero direct hits.

**Notes on checking.** Cross-check recomputed human counts (see critique.md). LLM numbers for c22, c12, c11 were checked against the arXiv text. c05, c06, c13 to c16 were not re-read in the cross-check. 2026 preprint model names and dates could not be sanity-checked beyond the two verified.
