# Epistemic (complementary) actions: deep document

*Subfield F02.07. Written 2026-11-01 from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b07, d22 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

An epistemic action is an action done mainly to change what the agent knows, not to move it closer to the goal. A pragmatic action is the opposite: it moves the world toward the goal. Kirsh and Maglio (1994) wrote: "actions performed to uncover information that is hidden or hard to compute mentally" (a01).

The classic case is Tetris. A player rotates a falling piece (zoid) more than a plan-first model predicts. The extra rotations show the piece's shape and fit sooner, and they are cheaper than rotating the piece in the head. A physical 90 degree rotation takes about 100 ms (plus about 200 ms to choose the key). Mental rotation of the same piece is estimated at 800 to 1200 ms (b03).

Related terms:
- **Complementary action / complementary strategy.** Kirsh (1995) widened the idea: any organising act that recruits outside elements to cut mental load (pointing, arranging, writing, marking). Coin counting with hands is the pilot (a19).
- **Perceptive action.** The 1992 workshop version framed it as controlling information intake by activity, next to controlling attention and gaze (a12).
- **Interactive skill, thinking with external representations.** Later Kirsh and Maglio work (a21, a22, a18).
- **Epistemic value (active inference).** Friston et al. (2015): expected free energy splits into extrinsic value (utility) and epistemic value (expected information gain). Probe while information gain is positive, then commit (a25, abstract only).
- **Terminology warning.** Neth and Muller (2008) say the epistemic/pragmatic split is confusing, because one action can be both. They propose goal-relative classes: focal vs ancillary, theoretical vs practical (b13). "Epistemic" in philosophy and AI means something else.

For our agent the mapping is this. A **probe** is a tool call whose value is the information it returns: run code on a toy input, print an intermediate state, write a tiny test, inspect a data shape, ask the user. The schema state it touches is **S4 TEST** (and the choice of what to do before a full attempt, S0 to S3). The three payoffs Kirsh and Maglio name are less memory, fewer steps, and lower error probability (a01). For an LLM these become tokens, tool calls and error rate.

The honest status: the human core is one lab with small samples. The LLM literature tests the idea without the name (execution feedback, clarifying questions, reproduction tests). No study tests probe-before-attempt by name at equal tokens (K16, d34, c22).

## 2. History and theories in depth

### 2.1 Roots (1992 to 1995)

- **Kirsh and Maglio c. 1992, Perceptive actions in Tetris** (a12). Four-page workshop paper, 30 subjects mentioned, no statistics. Three phenomena: rotate in midstream, rotate early, translate to verify. The idea started as an attention and perception story.
- **Kirsh and Maglio 1992, Reaction and reflection in Tetris** (a13). RoboTetris, a skill-based player with 6 board features (holes, total height, mountain height, covered holes, filled rows, local fitness) and a weighted sum. Its weights can beat any human, but it behaves unlike humans (too consistent, odd score peaks). The authors propose a reflective layer that biases what the system attends to, rather than overriding outputs. Design hint for us: a monitor that changes the input may beat a monitor that vetoes the output.
- **Kirsh 1995, Complementary strategies** (a19). Coin counting, N=5, hands vs no hands (section 3).
- **Kirsh 1995, The intelligent use of space** (a20). Taxonomy: simplify choice, simplify perception, simplify internal computation. Adds self-cueing (shuffling Scrabble tiles) and the Chambers and Reisberg result: no subject reinterpreted an ambiguous mental image, but 100% could reinterpret their own drawing. This is the best argument for writing a hypothesis down so it can be re-read in a new way.

### 2.2 The founding paper (1994)

Kirsh and Maglio, *Cognitive Science* 18 (a01 to a11, b01 to b06).

- **Paradigm.** Tetris on a 10 by 30 board, 7 zoids, 4 actions (rotate 90 degrees, left, right, drop). Fall speed about 200 ms per square at the start, about 100 ms at the maximum. A newcomer reaches intermediate level in under 10 hours. Shortest inter-keystroke interval about 75 ms, average about 250 ms (a02).
- **Why Tetris.** Every move either brings a piece nearer its final place or not, so pragmatic and non-pragmatic moves are easy to tell apart (b01).
- **Data.** Keystroke and game-state logs, a tachistoscopic mental rotation pilot, and RoboTetris as the classical foil. The number of participants and episodes in the main logs is not stated in the text read (a02).
- **Classical foil (a03).** A four-phase serial model (bitmap, chunked encoding, choose placement, compute motor plan). Under it any action made before planning ends should be random. A cascade or interleaved planner fails too. If players plan first, a 4-orientation zoid should average 1.5 rotations. Observed: every zoid type was rotated more than half its possible rotations (Fig. 6, 95% CIs; bar values not readable). Rotations begin in earnest at 400 to 600 ms and sometimes before 100 ms.
- **Why not false starts (a04).** A false start costs 75 to 750 ms to undo (1 to 3 extra rotations). Some rotations happen before the shape is visible, and early orientation estimates are poor. So early rotation reveals information.

Six proposed uses of epistemic action:
1. **Early rotation to expose a hidden shape** (a05, b04). A zoid is partly hidden as it enters; at medium speed (one square per 150 ms) the full image takes about half a second. Rotating shows the whole shape 150 to 300 ms earlier. Players rotate more when the partial view is ambiguous in both shape and column; they do not rotate more when only shape is ambiguous and the column disambiguates it. Players use column cues they cannot report.
2. **Save mental rotation effort** (a06, b03). Rotate in the world and compare. Pilot of 3 players (intermediate, advanced, expert), Shepard and Metzler style same/mirror task, 8 presentations per pair type; reaction time rose linearly with angle difference from 0 to 180 degrees (about 0.6 to 1.3 s, read off an axis). No flat line even for experts. Kirsh (1995) quotes 1000 to 1800 ms for internal rotation, so the number is soft.
3. **Rotation as a second retrieval cue** (a07). Conjecture: a Boltzmann-machine style attractor settles faster with two cues. Example: 1200 ms with one view vs 1000 ms with two. Untested.
4. **Rotation to shrink an attention decision tree** (a07). At most 3 probes without rotation, at most 2 with it. Untested.
5. **Let perception do the matching** (a07). So mental imagery need not be refreshed every 200 ms. Untested.
6. **Translate to the wall to verify** (a08, b05). In about 1% of drops the player moves the zoid to the nearest wall and back, then drops. This is pragmatically useless. It is used more when the drop is higher, where column judgment is least accurate (Fig. 15). Mean drop distance in squares, ordinary vs after the translate routine: intermediate 13.18 vs 19.04; advanced 13.69 vs 19.33; expert 15.65 vs 20.05; each pair differs at alpha .05.

Theory claims in the paper:
- **State space must pair physical and informational state** (a09). An action sequence that returns the board to its start can still change what the agent knows. Payoff has a physical and an epistemic part, as in Stigler's economics of information.
- **Value depends on the agent's own cognition** (a09, b06). A rotation at 500 ms is worth more than one made later, because the information would have arrived anyway. At great drop height the cost of leaving the goal path is outweighed by error reduction. No fitted model.
- **Skill is more than caching** (a10). Experts do not only chunk faster routines; they learn different tricks (expose early, prime recognition, verify externally). This is set against Newell and Rosenbloom and Logan.
- **Generalisation** (a11). Novice chess players move pieces to see replies, advanced players change viewpoint to break set, people shuffle, annotate and perturb the world. Only Tetris has data in the paper.

### 2.3 Skill (1996 to 2011)

- **Maglio and Kirsh 1996, Epistemic action increases with skill** (a14 to a18). Two novices, about 20 hours each, about 40,000 keystrokes. Speed followed the power law (section 3). Extra rotations rose with skill. Contested later (section 5).
- **Destefano and Gray 2007** (b10, b11) and **Destefano, Lindstedt and Gray 2011** (d18) found the opposite or a hump. Detail in section 5.

### 2.4 Mechanism tests (2000 to 2003)

- **Maglio and Wenger 2000, Two views are better than one** (b07, d01). A preview of a shape primes memory. The mechanism is priming, not mental-rotation substitution.
- **Maglio, Wenger and Copeland 2003, Benefits outweigh costs** (b08, d02). Hazard-function analysis: previews raised capacity about 38%, and benefit exceeded cost at every lag.
- Related work known only second-hand (b14): Neth and Payne 2002 (Tower of Hanoi; epistemic actions help steady-state behaviour and learning; not opened), Gray and Fu 2000 (people trade memory against lookup by access cost; not opened), Kirlik 1998 (short-order cooks; not opened). Maglio et al. 1999 (Scrabble) and 1997 (BBS commentary) were seen as metadata only (a23, a24).

### 2.5 Wider frames

- **Kirsh 2010, Thinking with external representations** (a21). Functions of interacting with a representation: change the cost structure of inference, shareable object of thought, persistent referents, re-representation, more natural structure, more explicit encoding, build arbitrarily complex structure, lower cost of controlling thought. This is the nearest account of why an LLM that could reason in text still gains from running tools: cost structure and re-representation, not new facts.
- **Kirsh 2013, Thinking with the body** (a22). Dancers "mark" a phrase and think through the partial version. Cheap partial versions (dry run, stub, sketch) can anchor thought. Ethnographic.
- **Friston et al. 2015** (a25). Formal twin of the Kirsh-Maglio cost-benefit idea.
- **Liu, Padmanabhan and Viswanathan 2026, Before Agents Decide** (c01 to c04, c23). A NeurIPS 2026 FAST workshop position paper. Three modes of epistemic action for LLM agents: acquiring missing evidence, transforming evidence that is hard to use, probing a system to create a revealing response. Choice rule: e* = argmax over E plus null of (E[V(I_e)|I,e] - c(e)), with commit-now as the null action at cost 0. The scaffold fixes the action set, so a perfect value estimate cannot pick an action the scaffold omits. Proposed benchmark: hold task, model, prompt budget and pragmatic actions fixed; vary which of acquisition, transformation and probing are available; test separately (1) noticing the evidence is inadequate, (2) choosing an action, (3) using the result; compare action suggested vs available only. Traces must record the pending decision, the evidence before and after, and the expected evidential change. No data; not yet run.
- **Wang et al. 2026, Position: invoke tools only when epistemically necessary** (d30). Criterion: call a tool only if the task cannot be done reliably by reasoning over the current context. No data.

## 3. Core findings with exact numbers

Human work first, then LLM work (more in section 6).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Players rotate more than a plan-first model predicts | Expected 1.5 rotations for a 4-orientation zoid if plan-first; every zoid type above half its possible rotations (Fig. 6 and 7, 95% CIs, bar values not in text); rotations start 400 to 600 ms, some under 100 ms | Kirsh and Maglio 1994 (a03, b02) | [S] same lab, observational |
| Physical rotation is much cheaper than mental rotation | Physical about 100 ms (+200 ms key choice); mental estimated 800 to 1200 ms (1994) or 1000 to 1800 ms (1995); pilot N=3, RT linear in angle | a06, b03, a20 | [S] N=3, estimate |
| Early rotation exposes a hidden shape 150 to 300 ms sooner | Full zoid visible after about 0.5 s at 150 ms per square; rotation more when ambiguous in shape and column | a05, b04 | [S] no controlled test |
| Players verify column by translating to the wall, more at greater height | About 1% of drops; mean drop distance 13.18 vs 19.04 (intermediate), 13.69 vs 19.33 (advanced), 15.65 vs 20.05 (expert); each pair p<.05 | a08, b05 | [S] observational |
| Extra rotations rise with skill (two players) | 7% expert, 5% intermediate, 4% beginner of episodes, p about .01; about 0.2 extra rotations per episode; N=2, about 20 h each | Maglio and Kirsh 1996 (a14) | [C] |
| Extra rotations are not slips | Vary by zoid type; mirror vs non-mirror not different at any level (p>.05; rare event, low power) | a16 | [S] |
| Extra-rotation episodes reach the final orientation earlier | 676 vs 1127 ms (SD 149, 99; t(198)=2.82, p=.005); 754 vs 1122 ms (SD 296, 71; t(293)=2.24, p=.026); one player, expert level, slow episodes | a17 | [S] |
| Practice curve stays a power law despite more backtracking | Time between actions r2 power vs linear vs exponential: LA .9108/.7721/.8439; TM .9557/.8117/.8789; 38 points per player | a15 | [S] |
| Complementary actions fall with skill in a large sample | 59 players, 173 games, top scores 867 to 236,305, best game 1,023,941; 25 of 173 games above 100,000; no player above 100,000 points used medium or strict translation in more than 2% of episodes; 1.02M game: 0.08 lenient translation rate, 1 over-rotation, 5 both-direction rotations in 1,281 episodes | Destefano, Lindstedt and Gray 2011 (d18) | [S] log-rule classification |
| Same direction at matched speed (poster) | Time to place, time between actions, first-move latency fell with expertise; N and statistics not given | Destefano and Gray 2007 (b10, b11) | [S] weak |
| Hands cut coin-counting time and errors | Time 22.5 s no hands vs 18.7 s hands; errors 68% (20.3 of 30) vs 42% (12.6 of 30); N=5; 30 images per condition; aggregate p printed as p<.4 (typo); per-subject p<.04 | Kirsh 1995 (a19) | [S] pilot |
| A preview raises accuracy and speed in a memory-priming task | One preview vs none: accuracy .86 vs .53; RT 869 vs 1791 ms; N=30, 3 days x 480 trials; reported t(1,59)=33.85 and t=2.01 (printed in the original, df do not fit N=30); 1 vs 2 previews, retention interval, zoid type: all F<1 | Maglio and Wenger 2000 (b07, d01) | [S] direction fine, statistics unreliable |
| Previews raise processing capacity | RT 528 vs 673 ms, t=5.09, p<.0001; capacity +37.8% (chi2=96.85); lag x presence +33.6; orientation x presence +11.5; benefit/cost ratio above 1 at lags 0, 1, 2, rising with lag, F(2,28)=31.25; N=15; cost = 2x keypress RT on a 4.4 s trial | Maglio, Wenger and Copeland 2003 (b08, d02) | [S] same lab replicates itself |
| Banning physical rotation did not change mental-rotation training transfer | N=13 / 13 / 14 (no physical rotation / standard / control), 5 hourly sessions; neither Tetris group beat control | Kaye 2013 (b12) | [S] thesis, transfer not in-game skill |
| LLM: acting to gather facts beats reasoning without action | ALFWorld best ReAct 71% vs best Act-only 45% vs BUTLER 37%; worst ReAct trial 48%; WebShop 40.0 vs 30.1; HotpotQA hallucination 0% of ReAct failures vs 56% of CoT failures | Yao et al. 2023 (a26, b24) | [E] |
| LLM: execution feedback lifts code | Self-Debug MBPP 61.4/67.6/72.8 to 66.2/69.2/76.4 (Codex/GPT-3.5/GPT-4) with trace only; up to +12% TransCoder, +8% MBPP with unit tests; InterCode-SQL GPT-4 9.1 to 73.7 (oracle stop) | a31, b22, d11 | [E] |
| LLM: own critique alone does not help | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0; with oracle labels GPT-4 GSM8K 95.5 to 97.5 | Huang et al. 2024 (d08) | [E] |
| LLM: the tool is the active ingredient | HotpotQA F1 (davinci/ChatGPT): CoT 46.1/42.8; CRITIC 50.5/52.9; CRITIC without tool 46.1/46.1 | Gou et al. 2024 (d07) | [E] |
| LLM: self-repair at equal compute is about break-even | GPT-4 APPS 1.05x and 0.97x of pass rate at matched samples; repair success 33.30% own vs 52.60% human feedback | Olausson et al. 2024 (b23) | [E] |
| LLM: reproduction tests used to select | Agentless SWE-bench Lite N=300: vote 77 (25.67%), +regression 81 (27.0%), +reproduction 96 (32.0%, +$0.25); $0.70 per issue; upper bound 126 (42.0%) | Xia et al. 2024 (d04) | [E] selection, not steering |
| LLM: reproduction test as input steers repair | 17 of 23 bugs plausibly fixed with test vs 13 of 23; per-run 33% vs 2% when used; oracle-filtered | Cheng et al. 2025 (d22) | [S] |
| LLM: choosing probes by information gain | UoT +38.1% average success; BED-LLM +37.4 points on 20 Questions; EIG-uniform best rank | a29, c08, c10, c11 | [E] simulated oracles |
| LLM: picking the right question is hard outside math | QuestBench GSM-Q/GSME-Q above 80%, Logic-Q and Planning-Q 40 to 50% | a27, b20, c06 | [S] |
| LLM: underspecified multi-turn input hurts | -39% average over six tasks; aptitude -15%, unreliability +112% | Laban et al. 2025 (c14) | [E] |
| LLM: tool overuse and underuse | Unneeded calls over 30% (Llama over 50%); SMART -24% tool use, +37.1% performance; simulator called in under 1% of cases, 15% of rollouts misused, up to -5% when enforced | d13, d20 | [E] |
| LLM: own probes can mislead | Reproducers trigger the bug in 41 to 57%; pass own reproducer but fail real tests: 17 to 30% (open agents) vs 4 to 5% (Agentless) | Ceka et al. 2026 (d21) | [E] |
| LLM: models copy silent tool errors | Accuracy up to 47% below best no-tool; warning line gives up to +30% | Sun et al. 2024 (d25) | [S] 2024 models |
| LLM: masking old probe output is free | Masking beyond 10 turns: over 50% cheaper; Qwen3-Coder 480B 52% cheaper, +2.6 points; summaries lengthened runs | Lindenbauer et al. 2025 (d24) | [E] one scaffold |

## 4. Mechanisms and models

Each is written so an engineer could build it.

### 4.1 Why an epistemic action pays (human accounts)

1. **Cost substitution.** An external step is cheaper and less error-prone than the internal one (rotate: 100 to 300 ms vs 800 to 1800 ms). Implement as: a probe is chosen when `cost(probe) * (1 + error_rate_probe) < cost(internal) * (1 + error_rate_internal)`. Measure both costs per task type; do not assume (b17).
2. **Information exposure.** A hidden part is revealed earlier by acting (early rotation). Implement as: when the view is ambiguous, probe first; when it is not, do not. The Tetris data show ambiguity-sensitivity: rotation rises when shape and column are both ambiguous, not when column alone disambiguates (a05).
3. **Priming or cueing.** A second view reactivates memory (Maglio and Wenger 2000; b07). Benefit did not change with 1 vs 2 previews. Implement as: show the same input in one second form (sorted, tabulated, diffed); do not add a third.
4. **Verification where risk is highest.** Translate-to-wall rises with drop height (a08). Implement as: probe frequency scales with the cost of a wrong attempt.
5. **Re-representation.** External images can be reinterpreted; mental images cannot (a20). Implement as: write the hypothesis as code or a table so it can be re-read.
6. **Time-dependence.** The value of a probe falls as the information would arrive anyway (b06). Implement as: probe early, or not at all.

### 4.2 Value-of-information gate (the formal core)

From Kirsh and Maglio (b06, a09), Friston (a25) and Liu et al. (c02):

```
for each candidate probe e in E (plus null = commit now, cost 0):
    score(e) = E[ V(decision | result of e) ] - V(decision | no probe) - c(e)
commit when max score <= 0
```

Practical estimation for a code agent (b21, c11, a29, c10):
1. Sample k candidate answers or hypotheses (k = 4 to 20) from the model.
2. For each candidate probe, run or simulate it and group the candidates by predicted outcome.
3. Expected information gain = entropy of the candidate distribution minus expected entropy after the outcome. Done in code (G5), not by the model.
4. Cost = tokens for the probe plus tokens to read the output.
5. Run the probe with the highest score if above zero; otherwise attempt.

Notes: EIG-uniform (uniform weights over sampled candidates) ranked better than EIG-logprobs (c11). Implicit Maximisation (ask the model to pick the most informative candidate question) beat Prompt-Only cheaply (c10). The gap between EIG selection and free choice shrinks with stronger models (b21).

### 4.3 Three probe modes (Liu et al., c01)

| Mode | Meaning | Code-agent example |
|---|---|---|
| Acquire | Get missing evidence | Read the file, search the repo, ask the user |
| Transform | Make evidence usable | Sort, tabulate, diff, convert to a graph, print the shape of the data |
| Probe | Perturb the system to create a revealing response | Run the function on a toy input, mutate an input, run a failing test |

A bare tool call does not show purpose (c04). Log: the pending decision, the evidence before, the evidence after, the expected change. Transformations can discard information; probes can introduce artefacts (c04).

### 4.4 The probe-use policy problem

Having a tool is not having a policy (K24). Failures seen:
- Under-use: simulator called in under 1% of cases (d20).
- Over-use: unneeded calls over 30% (d13); ASK actions about twice the planner optimum (0.83 to 1.06 vs 0.43; d26).
- Misuse: 15% of used rollouts misread; enforcement lowered scores up to 5% (d20).

The one cheap gate with data: do an expensive step only after a cheap outside check fails (PaT, d28). Try first, plan only if the check fails: Qwen3-4B Pass@1 76.05 standard, 81.18 plan-first at cost 8.31, 83.13 gated at cost 4.85. A model solved about 76% of standard problems directly. The gated step there is planning, not probing.

Difficulty-adaptive allocation is the other data point: compute-optimal allocation beat best-of-N by over 4x efficiency (d14). The difficulty estimate costs compute itself.

### 4.5 Probe output handling

- Return compact observations, not raw dumps (SWE-agent interface: 12.47% full, 18.00% Lite for GPT-4 Turbo, a 64% relative gain over shell only; a30).
- Mask old output beyond about 10 turns (d24). Do not summarise with a model, because summaries hid failure signals and lengthened runs.
- Summarise exploration history in code, not in the model: only one bandit configuration explored well, GPT-4 with chain of thought and an externally computed summary of history (a28, b19, c05).
- Treat tool output as untrusted (d25, d21). The probe must fail on the known-broken case first (K22).

### 4.6 Steering vs selecting

A probe result can (a) steer the next attempt (put it in the context) or (b) select among attempts (rerank or filter). Agentless, SWT-Bench and Large Language Monkeys measure (b) (d04, d10, d05). BRT measures (a) (d22). SWE-Doctor found a single generated reproduction test given to the agent did not improve patches, but several tests plus runtime diagnosis did: 75.7% on SWE-bench Verified and 59.4% on SWE-bench Pro, averaged over 5 backends, +2.0 and +3.9 over two baselines on Verified (c19). Treat the two uses as separate design choices.

## 5. What holds up

### 5.1 Human side

**Holds (weakly):**
- Extra, non-goal-directed rotations happen and are not random slips: they vary with zoid type, ambiguity and drop height (a05, a08, a16).
- A preview helps in a lab priming task, and the benefit is not explained by the cost (b07, b08, d01, d02).

**Does not hold up, or is thin:**
- **Independent replication: none found.** All preview work is Maglio, Wenger and Copeland; the 2003 paper says it replicates 2000 and 2002 (d02, d03, d33). Absence is partial because Semantic Scholar and OpenAlex were rate-limited.
- **Statistics in Maglio and Wenger 2000 are not reliable.** df=59 for N=30; t=33.85 for accuracy and t=2.01 for a 922 ms RT gap look swapped or mis-pooled. The values are printed in the original (d01), so the error is not ours. Do not cite them. Direction (preview helps) is plausible.
- **Skill direction is contested and moved against the original.** Maglio and Kirsh 1996 (N=2): extra rotations rise with skill (7% / 5% / 4%) (a14). Destefano and Gray 2007 (poster, N not stated): fall with skill at matched speed (b10, b11). Destefano, Lindstedt and Gray 2011 (59 players, 173 games): fall with skill; lenient rules show a hump; strict rules near zero (d18). The authors infer the 1996 players were at the level of their two lowest score bins (about 10,000 points or less). Caveats: classification is by rules on logs, not by intent; goal switching and slips are confounded with lenient rules; early rotations to reveal a half-visible piece are not counted as complementary in the 2011 work, unlike in Kirsh and Maglio. Verdict [C], weight toward "falls or humps". The SUBFIELDS note that a follow-up found a decline is correct, and the 1996 primary paper does say "increase".
- **Kirsh 1995 coin counting:** N=5, same images in both conditions, aggregate p typo (a19).
- **Two numbers for internal rotation** (800 to 1200 vs 1000 to 1800 ms) for the same quantity (a06, a20).
- **Kaye 2013:** removing physical rotation did not change mental-rotation transfer, and Tetris did not beat the control, so the base effect was not reproduced. Boundary condition: epistemic action pays locally, not as a general skill (b12).
- **Mirror null** (a16) is on a rare event (4 to 7% of episodes), so power may be low.
- **Not opened at all:** Neth and Payne 2002, Gray and Fu 2000, Kirlik 1998, Maglio et al. 1999 (a23, b09, b14, b15, b16). Do not cite their content.
- **Competing explanations:** (1) false starts and goal switching (b10); (2) priming rather than computation substitution (b07); (3) physical rotation can help or hurt mental rotation depending on conditions (b18); (4) early arrival simply leaves time to fiddle (a17).

### 5.2 Moderators and boundary conditions (human)

- Ambiguity of the current view (a05).
- Height or cost of a wrong action (a08).
- Time: late probes lose value (b06).
- Lag: benefit-to-cost ratio rises with lag (b08).
- Skill: direction contested (above).
- Measurement: compare probe rate at matched difficulty or speed, never pooled (b11).

### 5.3 LLM side: what works and what does not

**Works:**
- Execution or tool feedback from the outside (K05 [E]).
- Code as the action format: up to 20% higher success and up to 30% fewer actions than JSON or text; higher success for 12 of 17 models (d27, K29).
- Masking old tool output (K26).
- A one-line warning that tools can be wrong, up to +30% (d25).
- Passing a probe result forward rather than only reranking (K21, single study).
- Choosing probes by explicit EIG (K10).
- Gating an expensive step on a failed check (K25, single source).

**Does not work:**
- Intrinsic self-correction without an external signal (K06).
- Self-repair as a free win at equal budget (K07).
- Free in-context exploration (K12).
- A single generated reproduction test as the only input (c19).
- Always-on tool use (K13, K24).
- LLM-written summaries of tool history (d24).
- Prompted re-checks: they flip right answers to wrong ones (d23, d08).

**Contested:**
- Whether probing helps less as models get stronger (K27). CodeAct gains widen with model ability (d27); belief queries gave a saturating model little (d19); LDB gains are large for a weak seed and small for a strong one (GPT-3.5 seed 73.8 +9.1; GPT-4 seed 87.2 +2.4; Reflexion seed 91.5 +3.6; d06); EIG gap shrinks with model strength (b21).
- Whether repair at equal compute pays (Chen vs Olausson vs LDB). The difference is feedback source and budget accounting.

## 6. Language models

### 6.1 Named-term work

| Study | Type | Result |
|---|---|---|
| Liu, Padmanabhan, Viswanathan 2026 (c01 to c04) | Position paper | Three modes; benchmark design; no data |
| Wang et al. 2026, ICML position (d30) | Position paper | Call a tool only when epistemically necessary; no data |
| Kumar et al. 2026, belief-based world model (d19) | Experiments | Belief query (what is known and unknown about hidden state) raised reward within a step budget on ALFWorld, ScienceWorld (24 task types), BabyAI-Text (4 tasks) with Llama-3.1-8B, Qwen3-14B, Claude Sonnet; values in figures only; saturating Sonnet gained little on ALFWorld and ScienceWorld, gained substantially on BabyAI; query answered by an environment-side model; belief hand-built per benchmark |
| Annese et al. 2025 (d26) | Experiments | o3-mini ReAct with ASK actions in perspective-taking tasks; 7 scenarios x 5 trials; 100% first-take accuracy in Perspective, Hidden, Base, Near; 0 to 40% in Far, Not-That, Distractor; ASK 0.83 to 1.06 per run with examples vs 0.43 for the planner; steps 2.97 to 3.26 vs 2.14 planner; planner-derived examples gave no steady gain |
| Wang 2026, Tetris serving benchmark (c21) | Benchmark | Options are pre-simulated, so the rotate-to-see choice is removed; gemma-4-31B scored 76 vs 54 for a decision model; resending history would cost 11 to 12x more uncached. Cannot test epistemic rotation |

There is no experiment that gives an LLM the rotate-to-see choice and counts epistemic vs pragmatic moves (c22, d17, d34). Absence is from capped searches.

### 6.2 Adjacent work, by function

**Acting to get facts (acquire).**
- ReAct (a26, b24): ALFWorld 71 vs 45 vs 37; worst ReAct trial 48% beat both; relative gain over Act 33 to 90%, mean 62% over 6 trials; WebShop 40.0 vs 30.1 vs IL 29.1 vs IL+RL 28.7 vs human expert 59.6; FEVER 60.9 vs 56.3. HotpotQA failures: ReAct reasoning errors 47%, empty search 23%; hallucination 0% vs 56% for CoT. Failure mode: repeated or uninformative actions. Few-shot, 2022 models.
- SWE-agent interface (a30): GPT-4 Turbo 12.47% (286 of 2,294) full, 18.00% (54 of 300) Lite; 64% relative gain over shell only; 6.7x RAG on Lite at 8 to 13x cost; HumanEvalFix 88.3%.
- Programs as the thinking tool (d12): PAL Codex GSM8K 72.0 vs Minerva CoT 65.6; GSM-HARD CoT 65.6 to 20.1, PAL about 61; PAL with voting 80.4. Closest analogue to coin counting with hands.

**Probing code by running it.**
- Self-Debugging (a31, b22): see section 3. One debug turn usually enough (later turns within 0.1%). Without unit tests GPT-3.5 and GPT-4 were overconfident and gained about 1% (3.6% on MBPP for GPT-4). Spider: greedy plus debugging matched the 16-sample baseline; 8 samples plus debugging beat 32 samples.
- Olausson (b23): by difficulty, repair success with own feedback 42.64 / 19.33 / 3.67 (intro, interview, competition) vs 62.21 / 45.67 / 14.67 with human feedback. The 1.05x and 0.97x ratios are example cells, not a headline for all budgets (critique).
- LDB (d06): runtime values step by step beat the model's own dry run; Self-Debugging and repeated sampling stall after 2 to 3 rounds, LDB keeps rising; gains up to 9.8%.
- CRITIC (d07): GSM8K davinci-003 PoT 70.1, CRITIC 72.2, CRITIC without tool 68.3.
- Kamoi survey (d09): no demonstration of successful self-correction from prompted-LLM feedback outside suited tasks; works with reliable external feedback.

**Probing for bugs.**
- Agentless (d04): see section 3; gains from more samples plateau near 40.
- SWT-Bench (d10): test success 15.9 to 18.5% when told to run tests before submitting; tests produced for up to 87% of issues; filtering to fail-to-pass doubled precision to 47.8% at about 20% recall.
- Large Language Monkeys (d05): DeepSeek-Coder-V2 15.9% with 1 sample to 56% with 250 on SWE-bench Lite (then-state of the art single sample 43%); coverage log-linear over four orders of magnitude; voting and reward models plateau beyond several hundred samples without a verifier.
- BRT at Google (d22): 80 bugs; BRT Agent made plausible reproduction tests for 28% vs 10% for LIBRO; 23 plausible bugs; Passerine, Gemini, 20 runs per bug, temperature 0.2; 17 of 23 (74%) vs 13 of 23 (57%); six bugs solved only with the test; ensemble pass rate selected a plausible fix at top-1 in 70% of cases; 11% of plausible patches changed existing tests.
- Ceka et al. (d21): 500 SWE-bench Verified tasks, 5 agents; success 66 to 73% easy vs 4.8 to 19% hard, none on very hard; workflow agents write reproducers for all tasks, open-process agents under 80% except OpenHands with Claude; bug-localization context raised successful reproductions from 614 to 697 of 1,500 samples (13.5% relative) and helped 54% of issues (27 of 50); higher temperature gave more distinct errors (2.08 to 2.76) but lower success. Observational: reproduce-first was not randomised.
- SWE-Doctor (c19): 2026, five backends (GPT-5.4, GPT-5.4-mini, Claude Sonnet 4.6, DeepSeek-V4-Pro, MiMo-V2.5-Pro); uniquely resolves more than twice as many issues as either baseline; authors' own method. Preliminary study: one generated test as input did not help; fail-to-fail tests mislead.
- Agentic test-time scaling (c20): Claude-4.5-Opus 70.9 to 77.6% on SWE-Bench Verified; 46.9 to 59.1% on Terminal-Bench v2.0. Abstract and first page only. The gain is from summarising whole attempts.

**Asking.**
- UoT (a29, c08, c09): +38.1% average over direct prompting on five datasets; +46.6% for Llama3-70B; DX 97.0% (GPT-4); MedDG 81.4% (Gemini-1.5-Pro) and 88.0% (GPT-4); troubleshooting 43.7 to 67.3%; Llama3-70B closed-set 20Q Common 51.4 to 55.9, MedDG 83.7 to 90.4, FloDial 28.8 to 47.1; mean conversation length in MedDG successes 3.5 to 1.0; beats CoT-SC by 33.8% and Reflexion by 29.9%; pruned UoT beat Adapted-ToT by 7.36%; the gain over the strongest baseline is much smaller than over direct prompting; answers from a scripted respondent.
- BED-LLM (c10): +37.4 points average on 20 Questions (ICLR 2026); more than doubled success in over half the setups and never lowered it; Entropy was the strongest alternative.
- Active task disambiguation (b21, c11): 48 coding tasks, 4 elicited requirements, 20 sampled solutions per step, four models (Llama3-8B, Llama3-70B, GPT-3.5, GPT-4o-mini); EIG-uniform ranked best at every step (4.1 vs 6.2 for the worst at step 10 in one model); HumanEval and APPS (48 and 47 tasks after filtering).
- QuestBench (a27, b20, c06, c07): GSME-Q 99.39% and GSM-Q 84.05% on a subset; Logic-Q and Planning-Q 25 to 50%; filtering to problems the model can solve moved question accuracy up to +39 points for some models and about -10 for others.
- Laban et al. (c14, c15): 200,000+ simulated conversations; models guess early and lean on the premature answer; CONCAT control shows the drop comes from multi-turn underspecification.
- Matsnev 2026 (c16): clarification F1 +73% over ReAct+UE on ALFWorld-Clarification (+36% over UAM) with five backbones (GPT-5.1, DeepSeek-v3.2-exp, GLM-4.7, Qwen3.5-35B, GPT-OSS-120B); 50% of tasks made underspecified by the authors; measures the decision to ask, not final success.
- Wu 2023 (c13): vision paper, no numbers.
- SeekBench (d29): 28,493 traces over seven QA benchmarks; RL-trained agents 31.6% accuracy with good evidence vs 8.4% without; overconfident answers 63.1% base, 51.1% few-shot, 35.3% RL-trained.

**Exploring.**
- Krishnamurthy et al. (a28, b19, c05, c24): of all configurations tested only GPT-4 with chain of thought and an externally summarised history explored well; basic GPT-4 prompt had suffix failure in over 60% of 20 replicates (T=500); second failure mode is near-uniform play.
- Samiei et al. 2026 (c17, c18): 102 human adults, 288 LLM trials; humans who chose tests learned conjunctive rules much better than yoked observers; LLMs did not consistently gain from choosing; gpt-5 and deepseek-reasoner near-perfect on disjunctive rules; humans needed about 9.6 tests for conjunctive vs 6.4 disjunctive; gpt-5 adjusts objects per test to the remaining uncertainty.
- BoxingGym (d15): 10 environments, 5 runs; all systems struggle to pick informative experiments; GPT-4o had lowest EIG regret; Qwen2.5 32B beat 7B; instruction-tuned Qwen beat reasoning-tuned OpenThinker; Box's Apprentice did not consistently beat plain GPT-4o.

**Spending budget.**
- Thinking vs doing (d23): Gemma 3 12B prompted on a WebArena subset, 3 runs; action-only 14.76%; CoT 23.81%; check-again 26.14; budget forcing 24.81; best-of-n 25.03; check-again + best-of-n 27.36; action changed after double-check 25% vs 15% under budget forcing; trained TTI gained about 9% and 8% on two benchmarks.
- ReTool (d16): RL for code calls mid-thought; Qwen2.5-32B AIME 2024 67.0% (400 steps) vs text RL 40.0% (1080 steps); AIME 2025 49.3 vs 36.7; responses 40% shorter. Training result, not scaffold-only.
- Snell et al. (d14): adaptive allocation over 4x efficiency over best-of-N.
- Kim et al. 2026 (d31): a bare doubt cue recovers about 15% of failed runs on Qwen3 (AIME24/25, AMC23, MATH500); net effect unknown.
- ThinkCoder (d32): Pass@1 +3.0% over MapCoder at 6.4% of its compute.
- Observation masking (d24): Qwen3-Coder 480B 52% cheaper, +2.6 points.

### 6.3 What changed behaviour, by how much (summary)

| Lever | Size of effect | Caveat |
|---|---|---|
| Real execution feedback vs none | +2 to +12 points on code; much larger in oracle-stopped InterCode | Weak models gain almost nothing (Vicuna 2.6 to 6.3, StarChat 8.9 to 9.7) |
| Explicit EIG probe choice vs free choice | +37 to +38 points (simulated 20 Questions, diagnosis) | Simulated oracles; gap shrinks with model strength |
| Code as action format | up to +20% success, up to -30% actions | 2024 models |
| Reproduction test used to filter | +6.3 points on SWE-bench Lite (25.67 to 32.0) | Selection, not steering |
| Reproduction test fed to repair | 17 vs 13 of 23 bugs | Oracle-filtered, small |
| Gate on tool need | -24% tool use, +37.1% performance (trained agent) | Trained, not prompted |
| Gate on failed check (PaT) | 83.13 vs 81.18 at 4.85 vs 8.31 cost | Gated step is planning |
| Mask old probe output | over 50% cheaper, no loss | One scaffold |
| Tool-may-be-wrong warning | up to +30% | 2024 synthetic perturbations |
| Self-critique without evidence | up to about -37 points (CommonSenseQA, GPT-3.5); -4 to -6 on GSM8K, GPT-4 | 2023 models |

## 7. What our agent should take

### Add now (established)

1. **Revise only from real executed output; no critique round without an executed check.** Schema part: G2 (already stated), S5. Status [E]. Evidence: d08, d07, d09, b23, K06. Action: keep G2 as is. The probe, not the model's opinion, carries the information. Add the cross-reference that the same holds for probes: a probe result must be quoted.
2. **Use code as the probe medium and keep tool output compact.** Schema part: S4, offload (tools), memory. Status [E]. Evidence: d27, d12, a30, K29, K05. Action: probes are code runs with a short observation returned by the harness, not the raw dump.
3. **Mask old probe output after about 10 turns; do not summarise with a model.** Schema part: S4 context handling, memory. Status [E] (one scaffold). Evidence: d24, c21, K26. Action: keep the conclusion line of each probe plus the last 10 turns of raw output.
4. **Do not trust a probe the model wrote itself without a control.** Schema part: G3. Status [E]. Evidence: d21, d25, d08, K22. Action: a reproducer or test must fail on the broken case and pass on a known-good case before its verdict counts; add one line to the prompt that tool output can be wrong (up to +30% in d25); keep the held-out check separate from the probe.
5. **Do not rely on the model to explore freely; structure it.** Schema part: S3/S4, G5. Status [E] for bandits, [S] for code. Evidence: a28, b19, c05, K12. Action: code keeps the history of probes tried and summarises it as sufficient statistics; the model does not retell history.
6. **Pick a probe by information gain in code where the hypotheses can be enumerated.** Schema part: S7 (discriminating test), G5. Status [E] (simulated oracles). Evidence: a29, c08, c10, c11, b21, K10. Action: sample k candidate rules; run the one input that splits them. This is already partly in S7; extend to S2 and S4 when two or more candidates survive.
7. **When the missing information is with the user, ask once; when it is in the world, probe.** Schema part: S1, S4. Status [E]. Evidence: c14, c16, b21, K11. Action: S1 lists what is missing and who holds it. Do not answer early on an underspecified brief (c14: guessing early and leaning on the guess).
8. **Reproduction tests as filters are cheap and sound.** Schema part: S7 select, S8. Status [E]. Evidence: d04, d10, K08. Action: keep as selection; do not claim they steer.
9. **Probe-use gating needs a rule, not just a tool; log each probe.** Schema part: G7, G12, memory (run log). Status [E] that both under-use and over-use happen. Evidence: d13, d20, d26, d30, K24. Action: log every probe with the pending decision, evidence before, evidence after and expected change (c04). Count unneeded and missed probes in the bench so G7 can be applied to the probe step itself.

### Test first

1. **Probe-first vs attempt-first at equal tokens (U1).** S3/S4. No matched-budget study exists. Evidence: d34, d28, d23, K28, K16.
2. **Value-of-information gate vs fixed rule for probing (U2, U4).** S0/S4. [S]. Evidence: c02, b06, a25, d28, d13, K25.
3. **Steering vs selecting (U3).** S4/S7. [S]. Evidence: d22, c19, K21.
4. **Probe rate as a function of task familiarity (U5).** Memory/S0/S9. [C]. Evidence: d18, a14, b10, K02, K23. Prediction: hump or fall; probe more on a new class and less on a familiar one, recorded in S9.
5. **Probe kind ranking (U7).** S4. Open. Evidence: d27 (format only), K29.
6. **Position of the probe: first, or only after the first attempt fails.** S4 vs S5. [S]. Evidence: d28, a04, b06.
7. **Probe output retention policy by probe type (U8).** Memory. [E] on cost, untested for accuracy per probe type. Evidence: d24.
8. **Misleading probe handling (U9).** G3. [E] that harm exists; fix untested on current models. Evidence: d25, d21, d31.
9. **Probe-first by difficulty and model size (U6).** S0/S6. [C]. Evidence: d27, d19, d06, b21, d21.
10. **Transform-mode probes (re-representation),** such as a sorted or tabulated view of the input. S2/O6. [S] human only (priming result b07, reinterpretation a20). Test as an O6 variant.

## 8. Concrete tests on our bench

Common design: both arms get the same token budget (all tokens counted: setup, probes, probe output, reading, attempts). Same items, same seeds, at least 3 seeds. Report accuracy and tokens per solved item. Use items where a cheap probe exists and items where it does not.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Probe-first vs attempt-first | Code tasks with hidden behaviour: an under-specified function with a few hidden tests; ARC-style rule items where a tiny program can be run on the grid | A: run 1 to 3 probes (toy inputs, print state) then one full attempt. B: full attempt first, then revise from executed failure. C: plain k attempts, no probes | Accuracy at fixed total tokens; probes per item | A beats C on hidden-state items by a few points; A loses to B on easy items; the sign flips by difficulty bin |
| T2 Gate vs fixed rule | Mixed easy/hard items | A: always probe. B: never probe. C: probe only if the first quick attempt fails its check (PaT-style). D: probe if sampled candidates disagree (EIG above threshold) | Accuracy, tokens, unneeded probes, missed probes | C and D match A on hard items and B on easy items at lower cost |
| T3 Steer vs select | Bug-fix items with a generated reproduction test | A: probe output fed to attempt 2. B: probe used only to choose among k attempts. Same k and total tokens | Resolve rate | A at least as good as B; gap largest when sampled attempts are alike (G4) |
| T4 Probe kind | Same items | Run code; print intermediate state; tiny assert test; ask-user (simulated); no probe | Accuracy per token | Run code and tiny test top the list on executable tasks; ask-user wins on underspecified briefs only |
| T5 Misleading probe | Toy cases with a silently wrong tool output injected in 20% of probes | A: no guard. B: one-line warning. C: control run on a known-broken and known-good case. D: both | Right-to-wrong flips; accuracy | B and C cut flips; C more than B |
| T6 Retention | Long probe chains (10+ probes) | A: all raw output. B: mask beyond 10 turns. C: model summary. D: conclusion line only | Accuracy; tokens | B, D equal or better than A at under half the tokens; C longest runs |
| T7 Familiarity | Streams of items from one class vs mixed classes | Probe rate and accuracy by order within a class | Probe rate curve | Hump or decline; tests whether early probes pay (G7) |
| T8 Re-representation probe | Rule discovery items | A: model reasons on raw input. B: code first prints sorted/tabulated/diffed view | Accuracy | Small gain on items with hidden structure; none on items with visible structure |
| T9 Ask vs probe | Items with a missing variable, either with the user or in the world | Always ask; always probe; classify first then act | Accuracy; wasted calls | Classify-first best (QuestBench shows classification is hard outside math, so measure it) |
| T10 Named-term replication | Tetris-like game with a hidden or rotated piece, a rotate-to-see action and cost per action | Plain LLM, LLM with a probe prompt, LLM with an EIG gate | Epistemic share of actions; score | Direct LLM test of the Kirsh and Maglio claim; no result published (K16) |

Pre-registration: for T1, T2, T3 state before running that a gain below the threshold in UNKNOWNS.md means no change to SCHEMA.md (G7).

## 9. What does not transfer, and why

- **Speed ratios.** Tetris rotation is 8 to 18 times faster than mental rotation (100 to 300 ms vs 800 to 1800 ms). An LLM probe costs tokens and latency; there is no fixed ratio, and a long model-written chain can cost less than a tool round trip. Measure per task.
- **Mental rotation as a bottleneck.** Spatial imagery has no analogue in a text model. The analogue is arithmetic, enumeration and state tracking, where code beats text (PAL: CoT drops 65.6 to 20.1 on large numbers, PAL stays about 61; d12).
- **Real-time pressure.** In Tetris the piece falls. LLM tasks usually have no clock; the pressure is a token budget.
- **Tiny samples and one lab.** The Tetris effects come from N=2 to N=30 and one group. Treat the human numbers as direction, not size.
- **Pre-simulated options.** The 2026 Tetris benchmark removes the rotate-to-see choice, so nothing there tests epistemic action (c21).
- **Priming.** The preview benefit in Maglio and Wenger is a memory-priming effect with 250 ms displays. An LLM has no memory to prime; the closest analogue is putting a second form of the input in context (an untested guess).
- **Honest worlds.** In Tetris the world never lies. A code probe the model wrote can lie (d21: reproducers trigger the bug in 41 to 57%).
- **Selection confounds.** Many LLM gains (Agentless, SWT-Bench, Large Language Monkeys) are selection gains and need a verifier. They say little about probing before the attempt (critique).
- **Weak models.** Gains are near zero for weak models with execution feedback (InterCode Vicuna, StarChat) and for models that cannot read the feedback (Olausson: the bottleneck is the model's own diagnosis).
- **Human skill curves.** Whether an agent's probe rate should rise or fall with familiarity is a prediction, not data (the human data are contested).
- **Internalised skill.** Experts hold probes in motor routines; an agent does not. A scaffold cannot copy the internalisation described in b17.

## 10. Open questions

1. At equal tokens, does probe-first beat attempt-first for a current model, and on which task types does it lose? (K28, d34; no matched study.)
2. Does probe benefit come from steering or from selection? One steering study, 23 bugs, oracle-filtered (K21).
3. How should an agent decide to probe? No tested value-of-information gate for code probes (K24, K25).
4. Does probing help less as models get stronger? Contested (K27).
5. Which probe kind pays most: run code, print state, tiny test, ask user? Only the format is compared (K29).
6. Is the Maglio-Wenger preview effect real at N above 30 in an independent lab? None found (d33).
7. Does epistemic-action use rise or fall with skill? Weight toward fall or hump; agent version untested (K02, K23).
8. Is there any LLM study using the term with measured results beyond belief-query and ASK experiments? None found (K16).
9. Does carrying probe output forward hurt later reasoning, and does the effect depend on model (K26)?
10. Can an agent tell when a probe is misleading with current models? Evidence is 2024-era (K22).
11. Does a bare doubt cue, which recovers about 15% of failed runs, give a net gain once the right answers it flips are counted? (d31).
12. Do the 2026 position-paper modes (acquire, transform, probe) separate in practice, and does the "noticing, choosing, using" split give a clean diagnostic? (c03).
13. Why do LLMs not gain from choosing their own tests in the Samiei task while humans do (c17)? Is it action selection or hypothesis tracking?
14. What do Neth and Payne 2002, Gray and Fu 2000, Kirlik 1998, Maglio et al. 1999 and the IBM "self priming" paper show? Not opened.

## 11. Sources

[V] = opened and read (this session or in the earlier pass of this study). [M] = snippet, abstract or metadata only.

**Human work**
- [V] Kirsh and Maglio (1994) On distinguishing epistemic from pragmatic action. https://adrenaline.ucsd.edu/kirsh/Articles/CogsciJournal/DistinguishingEpi_prag.pdf
- [V] Kirsh and Maglio (c. 1992) Perceptive actions in Tetris. https://adrenaline.ucsd.edu/kirsh/Articles/Tetris/tetris.pdf
- [V] Kirsh and Maglio (1992) Reaction and reflection in Tetris. https://adrenaline.ucsd.edu/kirsh/Articles/Reaction/reaction.pdf
- [V] Maglio and Kirsh (1996) Epistemic action increases with skill. https://adrenaline.ucsd.edu/kirsh/Articles/Cogsci96/cogsci96.pdf
- [V] Kirsh (1995) Complementary strategies: why we use our hands when we think. https://adrenaline.ucsd.edu/kirsh/Articles/Cogsci95/cogsci95.pdf
- [V] Kirsh (1995) The intelligent use of space. https://adrenaline.ucsd.edu/kirsh/Articles/Space/AIJ.html
- [V] Kirsh (2010) Thinking with external representations. https://adrenaline.ucsd.edu/kirsh/Articles/Interaction/thinkingexternalrepresentations.pdf
- [V] Kirsh (2013) Thinking with the body. https://adrenaline.ucsd.edu/kirsh/Articles/Interaction/thinkingwithbody.pdf
- [V] Maglio and Wenger (2000) Two views are better than one. https://escholarship.org/uc/item/70c0d6x2
- [V] Maglio, Wenger and Copeland (2003) The benefits of epistemic action outweigh the costs. https://escholarship.org/uc/item/5bg5p6bv
- [V] Destefano and Gray (2007) Use of complimentary actions decreases with expertise. https://escholarship.org/uc/item/9v42q8kg
- [V] Destefano, Lindstedt and Gray (2011) Use of complementary actions decreases with expertise (CogSci 33). https://escholarship.org/uc/item/44k7g3vm
- [V] Neth and Muller (2008) Thinking by doing and doing by thinking. https://escholarship.org/uc/item/1zs02852
- [V] Kaye (2013) Tetris and mental rotation, M.A. thesis (repository abstract page). https://researchspace.ukzn.ac.za/handle/10413/9301
- [M] Maglio, Matlock, Raphaely, Chernicky and Kirsh (1999) Interactive skill in Scrabble. https://doi.org/10.4324/9781410603494-62
- [M] Maglio et al. (1997) Beyond embodiment, BBS commentary. https://doi.org/10.1017/s0140525x97361615
- [M] Friston et al. (2015) Active inference and epistemic value. https://doi.org/10.1080/17588928.2015.1020053
- [M] Neth and Payne (2002) Thinking by doing? Epistemic actions in the Tower of Hanoi. https://doi.org/10.4324/9781315782379-154
- [M] Gray and Fu (2000), Kirlik (1998): known only through Maglio et al. 2003. https://escholarship.org/uc/item/5bg5p6bv

**LLM work**
- [V] Liu, Padmanabhan and Viswanathan (2026) Before agents decide: epistemic action in LLM-based systems. https://arxiv.org/abs/2610.00511
- [V] Wang et al. (2026) Position: agents should invoke external tools only when epistemically necessary. https://arxiv.org/abs/2506.00886
- [V] Kumar et al. (2026) Towards a belief-based world model for LLM agents. https://arxiv.org/abs/2609.00455
- [V] Annese et al. (2025) Who sees what? https://arxiv.org/abs/2508.14564
- [V] Wang (2026) Same pieces, different servers: a Tetris benchmark. https://arxiv.org/abs/2603.02348
- [V] Yao et al. (2023) ReAct. https://arxiv.org/abs/2210.03629
- [V] Yang et al. (2024) SWE-agent. https://arxiv.org/abs/2405.15793
- [V] Chen, Lin, Schaerli and Zhou (2023) Teaching LLMs to self-debug. https://arxiv.org/abs/2304.05128
- [V] Olausson et al. (2024) Is self-repair a silver bullet? https://arxiv.org/abs/2306.09896
- [V] Zhong, Wang and Shang (2024) LDB. https://arxiv.org/abs/2402.16906
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? (abstract and introduction) https://arxiv.org/abs/2406.01297
- [V] Xia et al. (2024) Agentless. https://arxiv.org/abs/2407.01489
- [V] Mundler et al. (2025) SWT-Bench. https://arxiv.org/abs/2406.12952
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Cheng et al. (2025) Agentic bug reproduction at Google. https://arxiv.org/abs/2502.01821
- [V] Guo et al. (2026) SWE-Doctor. https://arxiv.org/abs/2607.00990
- [V] Kim et al. (2026) Scaling test-time compute for agentic coding (abstract and first page). https://arxiv.org/abs/2604.16529
- [V] Ceka et al. (2026) Understanding APR agents through traceability. https://arxiv.org/abs/2506.08311
- [V] Yang et al. (2023) InterCode. https://arxiv.org/abs/2306.14898
- [V] Gao et al. (2023) PAL. https://arxiv.org/abs/2211.10435
- [V] Wang et al. (2024) CodeAct. https://arxiv.org/abs/2402.01030
- [V] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Choudhury et al. (2026) BED-LLM. https://arxiv.org/abs/2508.21184
- [V] Kobalczyk et al. (2025) Active task disambiguation with LLMs. https://arxiv.org/abs/2502.04485
- [V] Li, Kim and Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/abs/2505.06120
- [V] Matsnev (2026) Uncertainty decomposition for clarification seeking. https://arxiv.org/abs/2606.19559
- [V] Wu (2023) LLMs should ask clarifying questions. https://arxiv.org/abs/2308.13507
- [V] Krishnamurthy et al. (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371
- [V] Samiei et al. (2026) Human adults and LLMs as scientists. https://arxiv.org/abs/2606.06464
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540
- [V] Qian et al. (2025) SMART: self-aware agent for tool overuse mitigation. https://arxiv.org/abs/2502.11435
- [V] Qian et al. (2026) Current agents fail to leverage world model as tool for foresight. https://arxiv.org/abs/2601.03905
- [V] Sun, Min, Chang and Bisk (2024) Tools fail. https://arxiv.org/abs/2406.19228
- [V] Lindenbauer et al. (2025) The complexity trap. https://arxiv.org/abs/2508.21433
- [V] Shen et al. (2025) Thinking vs. doing. https://arxiv.org/abs/2506.07976
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Feng et al. (2025) ReTool. https://arxiv.org/abs/2504.11536
- [V] Yoon et al. (2026) PaT. https://aclanthology.org/2026.acl-long.1703/
- [V] Shao et al. (2025) SeekBench. https://arxiv.org/abs/2509.22391
- [V] Kim et al. (2026) Strategic information allocation under uncertainty (abstract, introduction, recovery sections). https://arxiv.org/abs/2603.15500
- [V] Zhang et al. (2025) ThinkCoder. https://arxiv.org/abs/2502.17442
- [M] Search records with no source opened: b25, c22, d03, d17, d33, d34 in this folder.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 12 established claims: 8 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F02.07-K05** (reworded: the sources support less). Numbers match, but ReAct vs Act-only compares reasoning-plus-acting against acting without thoughts (not grounded feedback vs reasoning alone), and InterCode Try Again stops when reward=1, which uses an oracle signal. Corrected claim: Grounded feedback from executing code or tools improves LLM agents: CRITIC with an external tool beats the same loop without the tool (HotpotQA F1 50.5 vs 46.1 for text-davinci-003, 52.9 vs 46.1 for ChatGPT); InterCode-SQL GPT-4 rises from 9.1 to 73.7 over up to 10 interactive turns with execution feedback (the loop stops when reward=1, an oracle); and in ALFWorld interleaving reasoning with actions (ReAct, best trial 71%) beats acting without reasoning (Act, 45%).
- **F02.07-K11** (reworded: the sources support less). The 39% drop is real (Laban et al.), but the +73% clarification F1 in Matsnev is the proposed method versus the ReAct+UE baseline, not asking versus not asking; Wu (2023) reports no results. Corrected claim: Missing information is costly: spreading information over multiple turns (underspecified sharded input) drops performance by 39% on average across six generation tasks, and a prompt-only uncertainty-decomposition method for deciding when to ask raised clarification F1 on ALFWorld-Clarification by 73% over a ReAct+UE baseline and 36% over UAM.
- **F02.07-K16** (reworded: the sources support less). Position paper (no experiments), Kumar (cites Kirsh and Maglio, experiments) and Annese (ASK actions, o3-mini) check out, but the Tetris serving benchmark (2603.02348) never mentions epistemic action, Kirsh or Maglio, so it is not a named-term item; the universal negative is only a search record. Corrected claim: In searches on 2026-11-01 no study was found that tests Kirsh and Maglio's epistemic-action hypothesis by name as a probe-before-attempt test on an LLM. Items using the term: a position paper with no data, a belief-query study that cites Kirsh and Maglio (results in figures only), and an ASK-action study with o3-mini; a Tetris serving benchmark was found by the search but does not use the term.
- **F02.07-K22** (reworded: the sources support less). Ceka et al. measure the 17-26% overfitting (18-30% in the reproducer figure) only for SWE-agent and 4-5% for Agentless, not for open-process agents in general; the 41-57% trigger rate and the Sun et al. 47% figure check out; Huang et al. is only loosely related. Corrected claim: A probe the model writes itself can mislead: in Ceka et al.s trace study, patches passing the agent's own reproducer failed the real tests in about 17-30% of cases for SWE-agent versus 4-5% for Agentless, agent-written reproducers trigger the bug only 41-57% of the time, and models copy a silently wrong tool output (accuracy up to 47% below the best no-tool setting, Sun et al.).
