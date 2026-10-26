# Chess thought process and progressive deepening: deep document

*Subfield E16.01. Written 2026-10-26 from evidence_a-d.jsonl, claims.jsonl (K01-K23) and critique.md in this folder. Evidence ids (a01, b05, d08 ...) point to those files. Numbers that the cross-check corrected are given in corrected form. Status marks: [E] established, [S] single-source, [C] contested.*

Neighbouring subfields (links only, not covered here): Recognition-primed decision and mental simulation; Chunking and template theory; Conditions for valid intuition; Anytime search and restarts; Resource-rational analysis; Library learning; Conflict-driven clause learning; Go-Explore and archives; Proofs and refutations.

---

## 1. What it is

This subfield asks how a strong human thinks through a hard choice, and what that says about a scaffold for a language model.

The base work is Adriaan de Groot, *Thought and Choice in Chess* (1946 Dutch, 1965 and 1978 English). He had chess players of different strength think aloud on the same positions and coded the tapes.

Four ideas matter for us.

1. **Phases.** A long think splits into orientation, exploration, investigation and proof (a02).
2. **Progressive deepening.** The player takes up the same move or line again and calculates it further than before. The return can be at once or after other moves (a01, a09). It is not a fresh candidate. It is the same candidate at greater depth.
3. **Flat search statistics.** On the position de Groot used most (position A, solvable within about 9 plies), grandmasters did not search deeper or wider than experts. They found much better moves (a06). So the difference lies in what gets selected, not in how much is searched.
4. **Skill lives in recognition.** What separated the groups was recall of positions after a few seconds (a07), not search volume.

Later work tested these claims. Gobet (1998) replicated de Groot with 48 players (a10-a12). Campitelli and Gobet (2004) used hard positions and found steep skill effects in depth (a14). Bilalic and colleagues (2008) showed that the first good idea can block a better one (a25, a26).

On the language-model side, the same questions come back in new words. Is it better to revisit a candidate or to switch? Does a second look help or hurt? How should the depth budget scale with difficulty? When should the loop stop? We have measured results for most of these (section 6). We have no study that compares revisit policies on outcome at equal tokens, for humans or for models. That is the biggest gap (critique, GAP 1).

Scope limit: nearly all human data come from one easy position (de Groot's A). The hard-position evidence is four people.

---

## 2. History and theories in depth

### 2.1 de Groot (1946/1978): the thought process

**Method.** Subjects ranged from world-class players (Euwe among them) to weak club players. They thought aloud, 10 to 30 minutes per position. Protocols were split into "solving propositions": episodes that name a base move under study (a04). A few dozen subjects; 49 protocols in the main series with mean duration 14.6 min (range 0 to 35).

**Counting variables (a04).**

- N = fresh starts. n = successive solving propositions. n0 = different base moves considered.
- c = N - n, the immediate re-investigations. r = n - n0, the non-immediate ones.
- Position A, 19 protocols: N 8.4, n 6.2, n0 4.8 out of 56 legal moves.
- All main series: N 9.2, n 6.8, n0 4.5.
- So returns (c + r) averaged almost 4, about equal to the number of different moves. A thought process looks at few different moves and goes back to them often. Only 2 protocols had no return at all.
- The first phase took 23.5% of lines, about 3.2 minutes. De Groot warns this is partly a set-up artefact.

**The four phases (a02).**

1. Orientation: look at the position, form a first judgement, note possibilities.
2. Exploration: try sample variations a few moves deep. If poor, put the move aside.
3. Investigation: deeper, more directed and more exhaustive.
4. Proof: check and recapitulate, build a convincing argument.

**The driver (a02, a03).** De Groot's explanation is the *proving power* the player demands. A move is dropped only when its result falls below the maximal expectancy, and the shortfall must be convincing. How convincing depends on how complete the analysis is, how big the shortfall is, how uncertain the end-position evaluation is, and how reliable the expectation is. The demand rises with the phase. That rising demand is what produces progressive deepening. Risky, calculation-heavy lines are put off early to avoid a large calculation.

**Two kinds of return (a09).**

- Immediate re-investigation mostly clarifies a result just reached.
- Non-immediate re-investigation, after other moves, mostly serves overall deepening.
- Triggers: a detected error, lowered expectations for other moves, or a wish to strengthen or confirm.
- Worked example: the string g-a-e-a-a-k-a-i-a-a for subject M1, where "a" is 1.BxN/5.
- In 15% of protocols the move played was not the last one investigated. In position A it was 1 of 19 (5%).

**Weak players (a05).** Subject W2 passed many moves in review but never returned to one (r = 0 in two protocols, 28 min and 20 min). De Groot calls that a shortcoming of thought organisation. Position C, which cannot be solved by one plan and needs comparing tried moves, produced the most returns: c = 4.2 against 2.4 overall, r = 3.8 against 1.9.

**Grandmaster versus expert on position A (a06).** Five grandmasters against five experts:

| Variable | Grandmasters | Experts |
|---|---|---|
| Mean time (min) | 9.6 | 12.8 |
| Fresh starts N | 6.6 | 6.4 |
| Different first moves n0 | 4.2 | 3.4 |
| Max depth (plies) | 6.8 | 6.6 |
| Moves mentioned | 35.0 | 30.8 |
| Moves per minute | 3.5 | 2.5 |
| Different first moves per min | 0.49 | 0.29 |
| Move quality (scale to 9) | 8.2 | 5.2 |
| Immediate returns c | 1.8 | 2.0 |
| Non-immediate returns r | 0.6 | 1.0 |

(The Gobet 1998 republication shows about 3.6 and 2.4 moves per minute in the same cells. Treat that cell as plus or minus 0.1; critique correction 4.)

Conclusion in his words: depth of calculation cannot be the prime distinguishing mark between grandmaster and expert. He puts the difference in the first seconds, in what the player sees (a07: 93% reproduction for grandmasters and masters, 68% for experts, 51% for class players; one subject per class).

**Programming advice (a08).** De Groot argued that chess programs need cyclic progressive deepening with a changing goal, and that the old rule "a move is investigated only once" must be dropped. This is the historic root of the idea in AI. Computer chess then went by another road, brute-force alpha-beta with iterative deepening, which is a different thing: it re-searches from the root to a larger fixed depth, with no change in the goal.

### 2.2 Newell and Simon (1972): the problem behaviour graph

Source of the vocabulary (episode, base move, node) and of three rules later built into SEARCH: prefer normal moves early and unusual ones late; continue an episode if the result is favourable and switch if not; stop when an expectation is met (a30, second-hand).

### 2.3 Chase and Simon, Holding, and the search-versus-recognition quarrel

- Pattern-recognition models (Chase and Simon 1973, Gobet and Simon) predict small search differences between skill levels.
- Holding's SEEK (Search, Evaluation, Knowledge) predicts large ones. From de Groot's data Holding computed mean depth of 4.8 plies for experts and 5.3 for grandmasters (a29, a19). SEEK was never formal enough for sharp prediction (a22).
- Gobet argues the contrast is false. Recognition proposes moves and evaluates positions during search, and search creates new patterns (a13, a22, b11). In his framing, "the critical question is not how to search as deep as possible but when to stop searching" (a13).

### 2.4 Charness (1981) and Saariluoma (1990)

Second-hand through Gobet (a28, b25, b26).

- Charness: players of 1284 to 2004 Elo, four positions, 10-minute limit. About 0.5 ply of mean depth per 200 Elo, about 1.5 ply for max depth. No effect on search rate. He suggested depth plateaus above candidate-master level.
- Saariluoma: inverted U. Masters (about 2200) had 52 nodes at 5.1 plies; IMs and GMs 23 nodes at 3.6 plies.
- Charness (1989) followed one player from 1600 to 2300 Elo over nine years and found no significant depth increase (a20).

### 2.5 Gobet (1997): the SEARCH model

SEARCH is a probabilistic simulation (a18, a19). Moves come from recognition (fast) or weak heuristics (slow). A move is made in the "mind's eye", then recognition runs on the new image. Evaluation happens at terminal positions only.

Costs: 2 s per move in the mind's eye, 10 s per heuristic evaluation.

Rules for the next base move: re-search a line if its evaluation was unreliable; re-search it to store it in long-term memory; prefer normal base moves early and unusual ones late; continue if favourable, switch if not.

Stop rules: error risk too high (forgetting, interference), expectation met, or a decisive event.

Prediction: mean depth is a slow power function of the number of chunks. Under 1 ply with none, 2.5 plies at 1,000 chunks, about 4 plies at roughly 30,000, above 5 plies beyond 100,000. Fitted curve y = 1.073 x^0.133, r2 = 0.945. This fits the small slopes on easy positions. It underestimates the steep slope on hard positions (a19).

Gobet and Charness (2006) name two reasons for progressive deepening: to make up for memory limits and to pass information from one branch to another (a20).

### 2.6 Gobet (1998): the replication

See section 3 and 5. It is the main empirical anchor.

### 2.7 Campitelli and Gobet (2004): difficulty as moderator

Four players, three hard positions. The result reversed the "depth does not matter" reading for hard items (a14, b07, d01). See section 3.

### 2.8 Kotov (1971) against de Groot

Kotov's trainer method: list the candidates, analyse each to one evaluation, never repeat a variation or jump between branches. De Groot saw that everyone jumps. In 2004 the class B player and the candidate master jumped with no list. The GM also jumped but kept an expanding list and called himself undisciplined. The IM followed Kotov and had the best move quality by 0.4 points (4.7 against 4.3). Both top players had read Kotov. The authors conclude that search "can be under strategic control" (a16, b09, d02). No study compares the outcomes of the two policies.

### 2.9 Einstellung (Bilalic, McLeod and Gobet 2008)

A familiar solution blocks a better one (a25, a26, b12-b14). See sections 3 and 4.

### 2.10 Time pressure

- Gobet and Simon (1996): Kasparov's performance fell only about 100 Elo when he played simultaneous matches with one quarter to one eighth of the usual move time (a23).
- Chabris and Hearst (2003): blunders per 1,000 moves 5.02 at classical rates, 6.85 at rapid (about 6 times less time), 7.63 blindfold (a24, b10).
- The two camps read the same data in opposite directions (Gobet 2003 reply, b11).
- Van Harreveld et al. (2007) found skill predicts results less well as time tightens, which supports slow processes mattering for strong players (b23, abstract only).
- Burns (2004): blitz and standard ratings share 81% of variance (b24, second-hand).

---

## 3. Core findings with exact numbers

Status uses claims.jsonl: established, single-source, contested. "N" is the sample.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Humans revisit the same move at greater depth | de Groot: 49 protocols, returns about 4 per protocol, n0 4.5; only 2 had none. Gobet N=48 (12 each Master 2317, Expert 2101, Class A 1903, Class B 1699) shows the same structure; Swiss sample not different from de Groot on any pooled variable | a04, a12, b06 (K01) | [E] |
| Four phases, with first phase 23.5% of lines | Most long protocols split into four phases; worked case has 78 lines, 5 deepening phases | a01, a02, a04 | [E] (descriptive; boundaries partly subjective) |
| Skill and type of return | Max immediate returns rise with skill, F(3,44)=5.91, p<.005. Max non-immediate returns fall, F(3,44)=3.71, p<.02 (Masters differ only from Class A). Total returns ns, F=0.67. Pooled immediate 3.2 (Swiss) vs 2.4 (de Groot); non-immediate 1.6 vs 1.2. De Groot's W2: r = 0 in two protocols | a05, a12, b04 (K02) | [C] |
| Easy position: search stats barely separate skill | Gobet nodes 58.0/58.3/56.8/33.9 (F=1.11, ns); max depth 9.1 Masters vs 8.0 others (ns); time 11.3 vs 16.7 min (ns). Mean depth 5.0/4.6/3.7/2.9 (F(3,44)=2.9, p<.05, only Master vs Class B). Slope -2.638 + 0.003 x Elo = 0.6 ply per 200 Elo (Charness 0.5) | a06, a10, b01, b02 (K03) | [E] |
| Move quality does separate skill on the easy position | de Groot G 8.2 vs E 5.2 of 9. Best move chosen by about one third of players in both samples. Swiss Masters like de Groot GMs on quality, t(15)=0.58, ns | a06, b06 | [E] |
| Selectivity: Masters look at fewer base moves, spend less time in orientation | Base moves 3.2 (Masters), 6.5 (Class A), 4.8 (Experts and Class B), F=2.94, p<.05. 58% of Masters tried only 1 to 3 base moves, 41% of Class A tried 9 to 11. First phase 1.1/2.3/1.6/4.2 min (F=4.22, p=.01). De Groot GMs mentioned more moves per minute (3.5 vs 2.5) and more different first moves per minute (0.49 vs 0.29). Saariluoma: inverted U | a06, a10, b03, b26 (K07) | [C] |
| Hard positions: depth scales steeply with skill | N=4 (GM 2550, IM 2500, CM 2100, B 1750). Mean depth 13.8/10.5/7.4/2.8; max depth 25/23.7/17.7/10.5; nodes 370/405/152.7/88; nodes per min 12.3/13.5/6.8/3.2. Mean depth = -18.3 + 0.012 x Elo (2.4 plies per 200 Elo, r(4)=.97, one-tailed p<.02). Max depth 3.6 plies per 200 Elo. Positions need 52/60/70 nodes and 23/25/35 plies; de Groot's A needs 17 nodes and 9 plies. Top players searched about 10x more nodes than earlier studies (387.5 vs 38.6) | a14, b07, d01 (K04) | [S] |
| Skill beyond search | After removing mean depth, max depth and nodes, Elo still explains 17.6% of move-quality variance (p<.005). Regression on time, depth and max returns: R2 = 35.1%; Elo alone 29.2%. Elo explains 72.3% of 5 s recall variance. 4-player study: 10 s decisions on 49 positions GM 46.9%, IM 36.9%, CM 8.2%, B 4.1% (r=.94); 5 s recall 83.2/85/54/47%. 63 players, 5 s evaluation: skill explains 44% of error variance, no skill effect on response time | a11, b05, a15, b08, b20 (K05) | [E] |
| Part of skill is stored sequences | 76,562 games, 1600 to 2399 Elo; mean game 78.73 plies, 16.76 plies of theory (about 21.3%); about 100,000 opening moves memorised (estimate) | b21 | [S] |
| Einstellung | 2-solution problem: GMs all found the short mate; IMs 50%, Masters 18% (two Masters), candidate masters 0%. Logistic regression B=.013, p=.004; odds fall by 3.67 per 100 Elo; model probabilities .64 (2550), .32 (2450), .12 (2350), .01 (2150). Experts guessed 86/74/59% for IM, Master, CM. Skill cut to that of players about 3 SD (600 Elo) lower. Eye tracking: no shift in gaze across six periods on the 2-solution problem, F(5,20)=0.6; the control group shifted, F(5,20)=11.9, p<.001, partial eta2 .75. Times: familiar found in 37 s (SD 20); control optimal in 79 s (SD 25); stuck group 148 s (SD 90), t(8)=1.67, p=.13, d=1.2. Set effect lingers: fresh players solved in about half the time, t(44)=2.16, p=.036, d=.65 | a25, a26, b12-b14 (K08) | [S] (two papers, one lab) |
| Time pressure | Kasparov about 100 Elo lost at 1/4 to 1/8 time. Blunders per 1,000 moves 5.02 / 6.85 / 7.63 (36.5% rise for rapid). SEARCH predicts a larger rise if search mattered most | a23, a24, b10, b11 (K06) | [C] |
| Disciplined (Kotov) vs free search | N=4, one per level; IM disciplined, best quality 4.7 vs GM 4.3. No outcome study | a16, b09, d02 (K16) | [S] |
| SEARCH model fits | 2.5 plies at 1,000 chunks; 4 at about 30,000; above 5 at over 100,000. 150,000 chunks: 15% of moves from heuristics, 23% from chunks, 62% from templates | a18, a19, b11 (K17) | [S] (model) |
| Revisit triggers | Error found, lowered expectancy, need to confirm. Played move was not the last investigated in 15% of protocols (5% in A) | a03, a09 (K15) | [S] |
| Intrinsic self-revision in LLMs hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; GSM8K 75.9/75.1/74.7. GPT-4 GSM8K 95.5 to 91.5 to 89.0. Llama-2 62.0 to 43.5 to 36.5. GPT-3.5 kept its first answer 74.7% of the time; changes went more often right to wrong. With oracle labels GPT-4 reaches 97.5 | b15, c08, c24 (K09) | [E] |
| Revisit that adds information helps | AIME 2025, Qwen3-1.7B: plain sequential 22.2, random retrieval 27.8, relevant retrieval 35.6. R1-1.5B GSM8K sequential fell 83% to 52% at 22K tokens; retrieval stayed 84% | d08, d07 (K18) | [S] (two sources, one with weak design on this variable) |
| Underthinking | Wrong answers use 225% more tokens and 418% more thought switches. Over 70% of wrong answers hold a correct thought. Switch penalty: dev accuracy 35.2 to 39.8; R1 switch tokens on AIME24 13.8 to 5.7 | b16, b17 (K10) | [C] |
| Forced "Wait" | s1-32B AIME24 50.0 / 53.3 (2 Waits) / 56.7 (4 Waits); GPQA 57.6 to 59.6; MATH500 flat 93.0. Gain is 1 or 2 of 30 problems | b18 (K10) | [C] |
| Tree search with backtracking beats flat CoT | Game of 24: IO 7.3, CoT 4.0, CoT-SC (k=100) 9.0, ToT b=1 45, b=5 74. Equal-cost view: IO best-of-100 33% ($0.13), CoT best-of-100 49% ($0.47), ToT 74% ($0.74); 5.5k vs 6.7k completion tokens. Crosswords (word level): ToT 60%, no pruning 41.5%, no backtracking 20% | c07, c25 (K11) | [E] |
| Search added to a language model | 2.7B chess model: external MCTS 100 sims +68 internal Elo (1435 vs 1367); about +300 with 2000 sims (1707 vs 1367 internal). 99.6% of 5,980 internal search trees well formed | c04, c23 (K11) | [E] |
| Training on messy traces | Countdown: 51.27% vs 25.73% (SoS); about 36% of previously unsolved solved after self-improvement; Sokoban optimal 86.8 / 90.8 / 93.7 (Searchformer) | b19, c05, c06 (K14) | [E] (training only) |
| LLM chess is weak without help | MATE two-candidate choice: o1-preview 76.6, gpt-4 60.0, claude-3.5-sonnet 54.9, gemini-1.5-pro 52.6 (chance 50); fine-tuned Llama-3-8B 95.2. ChessQA: thinking +14.7 points on average, GPT-5 79.3 vs 44.0, 9,142 vs 1,236 tokens; short tactics 17.4%. ChessArena: o3 Glicko 1948 vs Maia-1100 2220; random 1524 | c01, c09, c10, c12 (K12) | [E] |
| LLM written branches are shallow and weakly used | Four-in-a-row, 27 models: mean max depth 1.78 plies (humans 4 to 6 inferred). Deleting chosen branch changes the move 32.0%; largest unchosen branch 1.2% | c13 (K13) | [S] |
| Trace reliance varies by task | Chain changes the answer under 10% on three tasks, over 60% on AQuA. Planning and backtracking sentences have highest counterfactual weight (14B model, 20 problems) | d16, d17 (K19) | [E] |
| Stop at the best point | OTBench: 64.3% of tokens after earliest best prefix; full thinking 9.03 points below it (MATH 1.83, AIME 4.88, LCB 12.42, GPQA 16.98). Oracle matches full accuracy at 14.2% of budget (fixed cap 35.0%). DEER: length cut 19.1% to 80.1%, accuracy +0.3 to +5.0, 11 models | d14, d15 (K20) | [S] |
| Adaptive spending | Disagreement of 4 samples: +2.3% over uniform, up to +5.5%, 14 of 15 settings, 9 of 15 significant. Snell: matches best-of-N with up to 4x less compute (estimate cost uncounted, 2048 samples per question) | d04, d05, d12, d13 (K21) | [E] |
| Same line or restart | Snell: sequential revision narrowly beats parallel at equal generations with a fine-tuned reviser; easy items fully sequential, hard items mixed. Mirtaheri: one long chain beats many short voted ones on serial-depth graphs. Chen: iterative deepening AIME-24 pass@1 72.6 vs 75.5, cons@32 83.3 vs 86.7, about 7 to 9% more wall-clock at alpha 2.0 | d04, d10, d11 (K22) | [C] |
| Case library vs extra sampling | Reasoning Memory: 0.580 vs 0.500 average, +8.9% over compute-matched baseline at the higher budget, 34 of 36 wins | d08, d09 (K23) | [S] |

---

## 4. Mechanisms and models

Each mechanism is written as steps an engineer can code.

### 4.1 De Groot's loop as a state machine

State kept in code, per run:

- `candidates`: list of base moves (or candidate answers), each with `best_line`, `depth_done`, `eval`, `status` (open, set-aside, dropped, leader).
- `expectancy`: the best value found so far (the maximal expectancy).
- `required_proof`: a number that starts low and rises by phase.
- `log`: the letter string of base moves visited, for example a-b-a-c-a.

Loop:

1. **Orientation.** Restate the state exactly (from code). List up to K candidates from a cheap recognition pass. Set `required_proof = 1`.
2. **Exploration.** For each candidate, run a shallow probe (depth d1). If its value is below `expectancy` by more than the proof threshold, set it aside. Otherwise keep it open.
3. **Investigation.** Pick the open candidate with the highest value. Re-enter it with depth `d2 > d1` (immediate return) or after trying another (non-immediate return). Raise `required_proof`.
4. **Proof.** Check the leader on a part the answer was not fitted to (this is G3). If the check fails, go back to step 3 with the failing output.
5. **Stop.** When the leader's proof meets `required_proof` and no open candidate beats it, or the budget ends. Output the best-so-far, not the last explored (de Groot: the played move was not the last one investigated in 15% of protocols).

Drop rule (a03): drop a candidate only with a written shortfall against `expectancy`, and require the shortfall to grow with proof demand. Score only quiet end positions (no pending captures). For an LLM task the "quiet" analogue is a branch ended at a checked result, not mid-argument.

Two return operators:

- **Extend** (immediate): continue the current branch with the new information just obtained.
- **Return** (non-immediate): go back to the old leader after other branches, carrying what the other branches taught.

### 4.2 Why returns happen (SEARCH, a18)

A line is revisited because its first evaluation was unreliable, or to store it. The mind's eye decays, so re-making a line from a clean restatement is cheaper than trusting a memory. For an LLM the analogue is context drift: restate the line and its result in a fresh short context before extending it.

### 4.3 Recognition first, search second

Evidence: a15, b05, b08, b20. A fast pass whose quality depends on stored knowledge, then search where the item is complex. The 4-player 2004 data and Chassy et al. 2023 argue that the two interleave. They do not run in strict order (fast first, slow second). Implementation: a gate that routes items by the plain pass rate of the class (S0), a retrieval step that offers solved neighbour cases before and during search (K23), and search whose budget scales with the difficulty signal (K21).

### 4.4 Difficulty-scaled depth (K04, K21)

Easy item: slope of 0.5 to 0.6 ply per 200 Elo, flat stats. Hard item: 2.4 plies per 200 Elo. In code:

1. Draw 3 to 4 cheap first passes.
2. Compute disagreement (vote entropy on comparable answers, or pairwise mismatch).
3. Set the remaining budget in proportion to disagreement, with a floor so the hardest items are not starved (SelfBudgeter's 7B model collapsed on AIME 2025, 6.67 against 28.89).
4. If the first passes already agree and a check passes, stop.

### 4.5 Einstellung and the forced different revisit (K08)

Mechanism: once a familiar solution is found, gaze (attention) stays on its features even while the player says he is looking for something else (F(5,20)=0.6). A second look in the same context re-reads the same material. The fix has to change the material:

- restart in a fresh context that does not show the first answer (G4), or
- mask the first answer's key elements and require a different mechanism, or
- run a discriminating test that the first answer cannot pass by accident.

Not tested in any LLM study (critique, GAP 5).

### 4.6 What makes a revisit useful for a model (K09, K18)

The working rule from three sources (Huang, Kamoi, ThinkRetrieve): a revisit helps if it adds information the first pass did not have. Sources of new information, from weakest to strongest evidence in our files:

1. a fresh independent sample (no direct test of the revisit role),
2. a different representation (no direct test),
3. a tool or executable check (Kamoi: external feedback works),
4. a retrieved solved neighbour case (ThinkRetrieve, Reasoning Memory).

Payload and trigger are separate. The trigger is code-fired (check fails, branches disagree, impasse). The payload is the new information. A revisit with a trigger and no payload is the case that hurts.

### 4.7 Stop rules (K20)

Two published stop tests that need no training:

- **DEER:** at a step transition, ask for a trial answer with confidence. Stop if confidence is high.
- **Keep best-so-far:** at each transition store the best checked answer. OTBench shows the last state is on average 9.03 points below the best prefix, but the oracle prefix is chosen on the same probes, so the true loss is smaller.

Risk: the confidence is the model's own, and confident wrong answers end early. In our schema the stop should rest on a code check when one exists and on sample agreement otherwise (G4, G5).

### 4.8 Make the deep line count (K13, K19)

If the written branches do not drive the choice, the scaffold wastes tokens. In code: score each branch's leaf by a check or a vote, store the scores, and let a code step pick the answer from the scores. Do not let the model "conclude" from its own prose (G5, G10). ChessQA's error analysis shows sound analysis followed by a wrong final move (c27).

### 4.9 Iterative deepening sampling (Chen et al., d10)

Concrete schedule: give each sample a token budget b0. If the sample has not finished at b0, append a trigger sentence and let it run to b0 x alpha. Repeat. A finished answer is not revisited. alpha = 2.0 recommended. Wall-clock overhead 1.07 to 1.39 depending on alpha. Reported benefit is 3 points on 30 problems, so it is not proven.

---

## 5. What holds up

### 5.1 Replicated

- **Progressive deepening exists.** de Groot (1938-1943 data) and Gobet (1986 data, published 1998) agree on the macro-structure. The Swiss sample did not differ from de Groot's on any pooled variable (b06). Two independent samples, 40 years apart, different recording. [E]
- **On easy positions, search statistics are flat across skill; move quality is not.** de Groot, Gobet 1998 and Charness 1981 agree in direction. Slopes: 0.5 and 0.6 ply per 200 Elo. [E]
- **Skill has a non-search part.** Elo explains 17.6% of quality after search is removed; 44% of 5 s evaluation error. Four sources. [E]
- **Self-revision without outside signal does not help LLMs.** Huang, Kamoi, ThinkRetrieve. [E]
- **Tree search with backtracking and pruning beats flat CoT on look-ahead tasks.** ToT plus the chess search results. [E]

### 5.2 Contradictions and failed or partial replications

1. **Do weak players return less or more?** de Groot's W2 never returned (r = 0, two protocols). Gobet found that non-immediate returns fall with skill, so weaker players return more in the delayed form. Two weak subjects against 48 players; Gobet wins on size. But the recording differed (audio against notes), and Gobet himself flags that 3.2 against 2.4 immediate returns may be an artefact (b04). (K02)
2. **Selectivity.** de Groot's GMs mention more moves and more different first moves per minute. Gobet's Masters look at fewer base moves. Saariluoma sees an inverted U. Skill ranges and positions differ. (K07)
3. **Depth slope.** 0.5 (Charness), 0.6 (Gobet), 2.4 (Campitelli and Gobet). The only resolution offered is position difficulty, and the large number is N=4. (K04)
4. **Time pressure.** Same data, opposite readings (Gobet against Chabris and Hearst). Van Harreveld and Burns point opposite ways. No LLM token-budget sweep on this exists. (K06)
5. **LLM revisit.** No-signal revision hurts (Huang). Forced Wait helps a little (s1). Fewer switches helps (TIP). All three can hold if the key variable is whether the revisit adds information. Nobody isolated that except ThinkRetrieve, on retrieved math examples only. (K10, K18)
6. **Plateau claim.** Charness suggested depth plateaus above expert level. The 2004 data contradict it on hard positions. The nine-year case study found no depth gain from 1600 to 2300. (a20, a28, a14)

### 5.3 Moderators

- **Position difficulty** (easy: flat; hard: steep). Confounded in 2004 with an instruction to find the unique solution.
- **Time cap.** Charness and Saariluoma used 10 minutes, 2004 used 30. Caps shape observed depth, as a token cap will.
- **Instruction.** "Find the shortest solution" (Bilalic) differs from "choose a move" (de Groot).
- **Skill range and population.** Skill inflation over 40 years; no world-class group in Gobet; young players in 2004.
- **Task type for LLMs.** Budget curves are flat on MATH but not on GPQA or code (OTBench). Sequential scaling peaked near 15K tokens for Qwen3-32B on MATH-500 and then fell (ThinkRetrieve). Trace reliance ranges from under 10% to over 60%.
- **Model strength.** GM resistance to Einstellung held on easy items, not hard ones. High-effort reasoning models resist traps better (mARC: 0.751 against physicians 0.66; 55% against 36% on items physicians missed). Older models (2023) hurt more by revising.

### 5.4 Interventions that worked

- Tree of Thoughts with evaluation, pruning and backtracking (Game of 24: 74% against 49% for CoT best-of-100 at similar tokens). The equal-cost comparison is the reliable one, not the 74 against 4.
- Retrieval of relevant solved examples per step (ThinkRetrieve) and procedural memory (Reasoning Memory).
- Four-sample disagreement to allocate budget (+2.3%).
- External feedback or a verifier for revision (Kamoi), but Snell's gains also needed a fine-tuned revision model.
- A decoding penalty on switch words (TIP): small, needs logits, too much hurts.
- Forced Wait (s1): small, fine-tuned model, one or two problems.
- Iterative deepening sampling (Chen): small, noise-level.
- Stopping at a confident trial answer (DEER): shorter chains, accuracy +0.3 to +5.0.
- Legal-move lists and exact board state from code (ChessArena: GPT-4.1 legal rate 97.5% against 71.6%; o3 top-move 62.0% against 43.5% blindfold).
- Written strategy or tactic notes per candidate (MATE: o1-mini +14/+24/+34 points).

### 5.5 Interventions that did not work

- Intrinsic "review your answer" (Huang, Valmeekam snippet).
- Plain forced Wait at larger budgets (ThinkRetrieve: stalled or fell).
- Rejection sampling for short answers (s1: inverse scaling).
- Debate at 6 responses (83.2) against self-consistency (85.3), GPT-3.5 GSM8K (Huang).
- More candidates: MATE accuracy fell with three candidates (fine-tuned model 40.0 N, 56.1 S).
- Beam search with a learned verifier on easy items: gets worse with budget (Snell).
- Chess instruction transfer to general cognition: weak and mostly uncontrolled (Sala and Gobet, snippet only, d about 0.34 overall).
- Post-training RL for chess on small base models plateaued at 25 to 30% (Hwang): no new knowledge from longer reasoning alone.

---

## 6. Language models

### 6.1 How they do on chess decisions

- General chat models are weak. MATE two-candidate choice: o1-preview 76.6%, gpt-4 60.0%, claude-3.5-sonnet 54.9%, gemini-1.5-pro 52.6%, chance 50% (c01). The paper's 24.2% headline gain for a fine-tuned 8B model is relative; it is 18.6 points absolute (c21).
- Thinking helps a lot but costs tokens. ChessQA: +14.7 points on average; GPT-5 79.3% with thinking against 44.0% without; 9,142 against 1,236 tokens per task; short tactics averaged 17.4% (c09).
- No LLM beats a weak engine. ChessArena (13 LLMs, over 800 games): o3 1948 Glicko, Maia-1100 2220, random 1524. Puzzles: Stockfish 98.4%, Maia-1100 74.6%, o3 55.6%, Gemini-2.5-Pro 14.0%. Play degrades beyond 90 turns for some thinking models (c10). SPIN-Bench: draw rate 0% for all models against the solver; top-3 move match from 52.8% (o3-mini) down to 25.4% (Llama-3.3-70b) (c12).
- Board-state errors lead the failures (c09, c27, c11: board-state accuracy 0.0% for all small RL models).
- A searchless 270M transformer trained on 15.3B Stockfish labels reaches 2895 Lichess blitz Elo against humans (corrected table: 2299 tournament Elo against bots, 95.4% puzzle accuracy; AlphaZero policy-only 1777, AlphaZero with 400 simulations 2470, Stockfish 16 at 50 ms 2711; GPT-3.5-turbo-instruct 1755 and 66.5% held) (c03, critique correction 1). Depth is amortised into weights. A prompt-only agent cannot copy it.
- A 2.7B model given external MCTS gains about 300 internal Elo at 2000 simulations; 100 simulations give +68 (c04).

### 6.2 Do they deepen?

- Written trees are shallow. Four-in-a-row, 27 models, 1,404 games: mean max depth 1.78 plies (range 1.00 to 3.48) against 4 to 6 for humans (inferred). Win rate rises with breadth (beta 0.075, p=0.0025) and not with depth (beta -0.015, p=0.82). Deleting the chosen move's branch changes the move in 32.0% of cases, the largest unchosen branch in 1.2%, the final paragraph in 2.1% (c13). One game, a GPT-5 judge extracted the trees, not replicated (single-source).
- Chess explanations mostly mirror the chosen move. Recovering the generated move from a masked explanation: top-1 0.379 to 0.398. Human transcripts averaged 560 words (n=3) against 47.5 to 128.3 for LLM conditions (c14). Written reasoning is not a record of the decision (this supports G10).
- Trace reliance depends on the task (d16) and backtracking and planning sentences carry most causal weight in math (d17).
- Go life-and-death (TsuGO): longer chains do not mean better search; strong models give the right candidate early attention and keep it; weak ones spread effort over shallow wrong branches. Easy tier accuracy / search efficiency, K=4 against K=None: Gemini-3.1-Pro 80.0/47.3 against 65.0/46.6; Kimi-K2.5 52.0/39.9 against 27.8/26.4; MCTS/UCT 33.0/35.8 against 5.0/13.1; KataGo 97.0/96.9 against 49.0/53.3 (c19).

### 6.3 What changed behaviour, by how much

| Change | Effect | Source |
|---|---|---|
| Self-revision with no signal | -1 to -39 points (GPT-3.5 CSQA 75.8 to 41.8; GPT-4 GSM8K 95.5 to 89.0) | b15 |
| Oracle label in revision | looks like gain (GPT-4 97.5) but the label leaks | c08 |
| Forced Wait x2 / x4 (fine-tuned) | AIME24 +3.3 / +6.7 points (1 or 2 of 30) | b18 |
| Plain Wait at 22K tokens | GSM8K 83% to 52% (R1-1.5B) | d08 |
| Relevant retrieval per step | AIME25 22.2 to 35.6 (Qwen3-1.7B) | d08 |
| Procedural memory | +8.9% over compute-matched baseline; 34 of 36 wins | d09 |
| Switch penalty (TIP) | 35.2 to 39.8 dev | b17 |
| Tree search over chain | 74 vs 49 (Game of 24, best-of-100 CoT, 5.5k vs 6.7k tokens) | c07 |
| Thinking on in chess QA | +14.7 points, about 7x tokens | c09 |
| Legal moves given | legal rate 71.6 to 97.5 (GPT-4.1) | c26 |
| Difficulty-based allocation | +2.3% average (4 samples) | d12 |
| Iterative deepening sampling | pass@1 72.6 vs 75.5 (3 points, 30 problems) | d10 |
| Early exit (DEER) | length -19.1% to -80.1%, accuracy +0.3 to +5.0 | d15 |
| Training on search traces | 25.73% to 51.27% (from scratch, toy) | b19 |

### 6.4 Cautions

- Most LLM tests report accuracy, not accuracy at equal tokens. Only ToT has a cost table.
- 2026 preprints (ThinkRetrieve, Reasoning Memory, OTBench, Nguyen) often use 30-problem AIME sets; a few points are within noise.
- Chess benchmarks score the first move on puzzles (under 6 plies). They say little about revisiting inside a long deliberation.
- Ciancarini and Pareschi (2026): of 84 chess study families, planning, explanation and metacognition are under-studied. We found no study that measures progressive deepening as such in LLM chess play (c15, abstract only).

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established [E])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | A revisit step needs a code-fired trigger (check failed, branches disagree, impasse) and a payload of new information (the failing output, a tool result, a retrieved neighbour case). A bare "look again" is banned. This restates G1 and G2 with a mechanism. | G1, G2, S5 | [E] | K09: b15, c08, c24, d07; K18 supports d08 |
| A2 | Allow re-entry to an already-explored candidate with a larger depth budget, in addition to expanding new ones. Humans do this in 47 of 49 protocols. The current tree rule (3 children, depth 2, 2 expansions) stays as the cap; re-entry spends the same cap rather than adding to it. | S4, S5, tree rules | [E] that humans do it (K01); the benefit for a model is untested, so the cap stays | a01, a04, a12, b06 |
| A3 | Tree search that keeps a branch record, backtracks and prunes beats flat chain at comparable tokens. Keep backtrack and prune as separate operators. | S4, S5, O | [E] | K11: c07, c25, c04, c23 |
| A4 | Spend more on items where a few cheap first passes disagree; spend less where they agree and a check passes. Keep a floor for items that look hard. | G12, S0, S4 | [E] | K21: d04, d05, d12, d13 |
| A5 | Do not use depth or length as a quality signal, and do not use "deeper search" as the copy of expert skill. On easy items search stats are flat while quality differs. | G7, G11 | [E] | K03, K05: a06, a10, b01, b05 |
| A6 | Give the model exact state from code (board, legal moves, parsed task) before any search. Reject malformed branches in code (value minus infinity). | S1, S2, S4 | [E] (several chess benchmarks) | K12: c09, c10, c26; c23 |
| A7 | The final choice is a code step over scored candidates. The written trace is not evidence of how the model decided. | G5, G10, S7 | [E] | K19: d16, d17; c14 |
| A8 | Keep failed branches in the record (what was tried, why dropped) and show them to later steps. Search traces with dead ends beat clean solutions in training. As a prompt-time exemplar style this is only a hint. | S9, memory | [E] for training only | K14: b19, c06, c05 |
| A9 | A cheap first pass whose quality rests on stored knowledge, followed by search only on complex items. Recognition and search interleave. | S0, S2 | [E] | K05: b20, a15, b08 |

### Test first ([S] or [C])

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Retrieval of a solved neighbour case as the payload of a revisit, at equal tokens, against extra search passes. | memory, S5 | [S] | K18, K23: d08, d09 |
| T2 | Forced different revisit after the first valid answer: exclude the first answer's key elements or restart fresh, against a plain "check again". | G1, G4, S5, O6 | [S] | K08: a25, a26, b14, d18 |
| T3 | Revisit policy: free re-entry (de Groot) against finish-each-candidate (Kotov) against restart. Report by difficulty tier. | S3, S4, S5 | [C] | K02, K16, K22: a12, a16, d02, d04, d10, d11 |
| T4 | Stay-on-line gate: do not switch away from a line until a depth quota or a check is met (the anti-underthinking rule, in code). | S5, G | [C] | K10: b16, b17, b18 |
| T5 | Stop rule: trial answer with confidence at each branch boundary; keep best-so-far. | S5, G6 | [S] | K20: d14, d15 |
| T6 | Candidate width: 2 against 3 against 5 first candidates at equal total tokens, by difficulty. | S3 | [C] | K07: a06, b03, c02, d06 |
| T7 | Difficulty-scaled depth budget against a fixed one. | G12, S4 | [S] for the human half (K04), [E] for the LLM half (K21) | a14, d12 |
| T8 | Branch ablation on our own traces: does deleting the deepest unchosen branch or a revisit step change the answer? Use to prune useless steps. | S4, logging | [S] | K13, K19 |
| T9 | Token-budget sweep (1x, 1/2, 1/4, 1/8) for plain and scaffold. | G11, G12 | [C] | K06: a23, b10 |
| T10 | Explicit revisit triggers (branch conflict, low confidence) against unconditional revisits. | S5 | [S] | K15: a03, a09 |
| T11 | Few-shot exemplars with explored-and-abandoned branches against clean solutions. | S3 | [S] | K14 |
| T12 | Iterative deepening sampling schedule (budget x2 per round, finished answers kept). | G11, S3 | [S] | d10 |
| T13 | Per-candidate short note before comparing candidates. | S4 | [S] | c02 |

Nothing in "Test first" goes into SCHEMA.md until it passes its test (see UNKNOWNS.md).

---

## 8. Concrete tests on our bench

Bench types available: ARC items, BRAINTEASER items, and any item set with an exact checker. All arms use the same total tokens (prompt plus generated, retrieved text counted), the same model and temperature, and at least 3 seeds. For small sets report per-item flips (right to wrong, wrong to right), not only accuracy. Treat gains under 3 points on fewer than 100 items as noise.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | ARC items with a held-out example (checkable); BRAINTEASER | (a) plain "review your answer"; (b) revisit triggered by a failing check with the failing output shown; (c) fresh independent resample | accuracy; right-to-wrong and wrong-to-right counts | (a) near 0 or negative; (b) positive; (c) between. Replicates K09 on our bench |
| B2 | Hard ARC items (plain pass rate under 40%) | (a) deepen the first line; (b) restart with excluded-first-answer rule; (c) 50/50 mix | accuracy by difficulty tier | (a) better on easy, (b) and (c) better on hard (K22) |
| B3 | Items with a shorter or better solution than the obvious one (BRAINTEASER with a trap answer) | (a) "check again"; (b) mask first answer's key elements and demand a different mechanism; (c) fresh context without the first answer | rate of finding the better answer; rate of repeating the first | (b) and (c) above (a) by 5 to 10 points |
| B4 | Mixed difficulty set | (a) uniform budget; (b) 4 first passes, disagreement sets the rest with a floor | accuracy; tokens used | +2 points or same accuracy at fewer tokens (K21) |
| B5 | Items with a solved-case library (leave-one-out by class) | (a) extra search passes; (b) retrieved neighbour case at each revisit; (c) both; (d) empty-library control | accuracy | (b) over (a) by 3+ points; (d) equals (a) |
| B6 | Items with a checker | (a) free switching; (b) stay on line until check or depth quota; (c) forced re-check | accuracy; switch count; tokens | (b) over (a) if underthinking applies; no gain on easy items |
| B7 | Items with an exact check | (a) always-last answer; (b) best-so-far by check; (c) DEER-style stop on trial answer confidence | accuracy; tokens to answer | (b) over (a) by 1 to 4 points; (c) fewer tokens, same accuracy |
| B8 | Any set, logged traces | delete deepest unchosen branch; delete each revisit step; replace with filler | rate the final answer changes | reveals which steps are decoration; if under 5% for revisit steps, remove them |
| B9 | Whole bench | token budget 1x, 1/2, 1/4, 1/8, plain and scaffold | accuracy curve | flat curve means retrieval dominates; steep means search matters; scaffold should dominate plain at low budget |
| B10 | Chess puzzles with a known best move (external check domain, optional) | plain thinking against scaffold, exact board and legal moves from code | first-move accuracy | scaffold gain; use to compare with ChessQA numbers |
| B11 | Hard items | candidate width 2, 3, 5 at fixed tokens | accuracy | best width rises with difficulty (K07) |
| B12 | Any set | few-shot exemplars with abandoned branches against clean | accuracy | small or none; a cheap check of K14 |

Logging for all arms: the letter string of candidates visited (a-b-a-c-a), tokens per state, revisit type, trigger, and whether the final answer equals the last explored.

---

## 9. What does not transfer, and why

- **Human time scale and memory limits.** A human re-searches a line because the mind's eye decays and short-term memory holds about seven chunks (a22). A model with a long context has a different failure: drift and anchoring. The reason for a return differs even when the behaviour looks the same.
- **Chunk acquisition.** Masters hold 10,000 to 100,000 chunks, learned over thousands of hours (a15: 6,890 study hours for the GM). A prompt-only agent cannot learn them. It can only retrieve a library (K23).
- **Single easy position.** Nearly all of the human numbers come from de Groot's position A. Do not copy 4 distinct candidates or 4 returns as a target.
- **Four-person hard-position slope.** 2.4 plies per 200 Elo is N=4.
- **Search depth in plies.** A ply is a chess unit. For open tasks "depth" has no direct meaning; the analogue is the number of dependent steps checked by code.
- **Elo as skill.** Models are not on one scale; the Elo-to-budget slope cannot be moved over.
- **Engine ground truth.** Chess has an exact evaluation (Stockfish) and perfect information. Many bench tasks have neither. Blunder rates need a reference.
- **Brute-force alpha-beta.** Computer-chess iterative deepening re-searches from the root with a fixed goal. De Groot's deepening changes the goal and the proof demand. Only the second maps to our states.
- **Trained search (SoS, Searchformer, Ruoss).** These need a symbolic solver or engine labels and weight updates. We have a scaffold only.
- **Fine-tuned revision (Snell).** The revision model was fine-tuned; the result does not show a prompt-only revisit rule works.
- **Decoding penalties (TIP).** Need logit access.
- **Chess-instruction transfer.** Even in children, benefits to general thinking are weak and mostly uncontrolled (b28, snippet). Do not expect chess-style habits to carry to other tasks by instruction.
- **Time pressure literature.** Human blunder rates under time cuts do not give an LLM budget curve; OTBench shows the curve depends on task.

---

## 10. Open questions

1. Does a revisit policy change outcomes at equal tokens? No study compares free re-entry with finish-each-candidate on result quality, in humans or LLMs (GAP 1).
2. What makes a revisit useful? New information is the best current answer. Verifier, different sampled path and different representation have not been compared head to head (GAP 2).
3. Is there a larger replication of the 2.4 plies per 200 Elo slope? Connors et al. (2011, 22 players, two positions) is paywalled and its abstract stresses speed. If its depth numbers match, the hard-position claim moves from [S] toward [E] (GAP 3, GAP 8).
4. How much of expert quality can a retrieval library replace? ThinkRetrieve and Reasoning Memory say a lot in math, but both are 2026 preprints with imperfect token matching (GAP 4).
5. Can a forced second pass that excludes the first answer break fixation in a strong LLM? Only mARC touches this; it varies effort, not the second pass (GAP 5).
6. Are LLM trace branches causally used? The 32.0% against 1.2% result is one game and one judge. Related tests (Lanham, Thought Anchors) point to task-dependence (GAP 6).
7. Candidate width: is the best number difficulty-dependent for LLMs? Human data conflict (GAP 7).
8. Stopping: how often is the final answer not the last one explored in LLM agents, and does best-so-far beat last? (GAP 9)
9. What is the shape of the accuracy against token-budget curve for a scaffold? (GAP 10)
10. Do immediate and delayed returns differ in outcome? In humans, Masters made more immediate and fewer delayed returns, but nothing links either to quality after controlling for skill.
11. Why does an N=4 hard-position study show the IM above the GM on quality (4.7 against 4.3)? Noise, or a real benefit of discipline? Untestable at this size.
12. Does the human "proof" phase correspond to something an LLM can do reliably, or is verifier independence the real requirement (G3, G4)?

---

## 11. Sources

[V] = opened and read this session or in an earlier pass of this study. [M] = snippet, abstract or second-hand only; do not cite numbers.

**Human thought-process literature**

- [V] de Groot (1978) *Thought and Choice in Chess*, 2nd ed. https://archive.org/details/adriaan_d._de_groot_-_thought_and_choice_in_chess_2nd_ed._1978 (a01-a09)
- [V] Gobet (1998) Chess players' thinking revisited. Swiss J. Psychology 57, 18-32. https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf (a10-a13, b01-b06)
- [V] Campitelli and Gobet (2004) Adaptive expert decision making. ICGA Journal 27(4). https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf (a14-a16, b07-b09, d01, d02)
- [M] Connors, Burns and Campitelli (2011) Expertise in complex decision making. Cognitive Science 35(8). https://ro.ecu.edu.au/ecuworks2011/610 and https://researchers.mq.edu.au/en/publications/expertise-in-complex-decision-making-the-role-of-search-in-chess-/ (abstract only; a17, b22, d03)
- [V] Gobet (1997) A pattern-recognition theory of search in expert problem solving. https://bura.brunel.ac.uk/bitstream/2438/843/1/Templates_and_search.pdf (a18, a19)
- [V] Gobet and Charness (2006) Expertise in chess. https://bura.brunel.ac.uk/bitstream/2438/1475/1/Gobet-Charness-CUP-chess%20expertise.pdf (a20, a21)
- [V] Gobet and Simon (1998) Pattern recognition makes search possible. https://bura.brunel.ac.uk/bitstream/2438/816/1/Paper_on_Holding.pdf (a22)
- [V] Gobet and Simon (1996) Recognition processes and look-ahead search in time-constrained problem solving. Psych Science 7. https://bura.brunel.ac.uk/bitstream/2438/1338/1/FullText.pdf (a23)
- [V] Gobet (2003) reply to Chabris and Hearst. https://bura.brunel.ac.uk/bitstream/2438/1391/1/Chabris_Hearst_Reply.pdf (a24, b10, b11)
- [V] Bilalic, McLeod and Gobet (2008) Inflexibility of experts. Cognitive Psychology. https://bura.brunel.ac.uk/bitstream/2438/641/1/Flexibility_Cog%20Psy_revisionFINAL.pdf (a25)
- [V] Bilalic, McLeod and Gobet (2008) Why good thoughts block better ones. Cognition. https://bura.brunel.ac.uk/bitstream/2438/2276/1/Einstellung-Cognition.pdf (a26, b12-b14)
- [V] Chassy, Lahaye, Didierjean and Gobet (2023) Intuition in chess. https://researchonline.lse.ac.uk/id/eprint/118812/1/s00426_023_01823_x.pdf (b20; not re-checked in the cross-check)
- [V] Chassy and Gobet (2011) Single-use sequence knowledge. https://bura.brunel.ac.uk/bitstream/2438/6145/2/Fulltext.pdf (b21; abstract, introduction, methods only)
- [M] Kotov (1971) Think Like a Grandmaster, via Campitelli and Gobet (a27)
- [M] Charness (1981) Search in chess, via Gobet (a28, b25)
- [M] Holding (1985, 1992), via Gobet and Simon (a29)
- [M] Newell and Simon (1972) Human Problem Solving, via Gobet (a30)
- [M] Saariluoma (1990), via Gobet (b26)
- [M] Chabris and Hearst (2003), via Gobet's reply (b10)
- [M] Van Harreveld, Wagenmakers and Van der Maas (2007) Effects of time pressure on chess skill. https://link.springer.com/article/10.1007/s00426-006-0076-0 (b23)
- [M] Burns (2004) Effects of speed on skilled chess performance, via Campitelli and Gobet (b24)
- [M] Sunde, Zegners and Strittmatter (2026) PNAS, via news report. https://siliconcanals.com/t-professional-chess-faster-decisions-better-moves-uncertainty/ (b27)
- [M] Sala and Gobet (2016) chess instruction meta-analysis. https://researchonline.lse.ac.uk/id/eprint/102237 (b28)

**LLM and agent studies**

- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798 (b15, c08, c24)
- [V] Wang et al. (2025) Thoughts are all over the place (underthinking). https://arxiv.org/pdf/2501.18585 (b16, b17)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/pdf/2501.19393 (b18); abstract page https://arxiv.org/abs/2501.19393v2 (c17, M)
- [V] Gandhi et al. (2024) Stream of Search. https://arxiv.org/pdf/2404.03683 (b19, c06)
- [V] Wang et al. (2025) MATE chess testbed. https://arxiv.org/html/2411.06655 (c01, c02, c21)
- [V] Ruoss et al. (2024) Amortized planning, chess. https://arxiv.org/html/2402.04494v1 (c03, c22; corrected figures used)
- [V] Schultz et al. (2025) External and internal planning with language models. https://arxiv.org/html/2412.12119v3 (c04, c23)
- [V] Lehnert et al. (2024) Searchformer. https://arxiv.org/html/2402.14083v2 (c05; not re-checked)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/html/2305.10601v2 (c07, c25)
- [V] Wen, Tang and Anderson (2025) ChessQA. https://arxiv.org/html/2510.23948 (c09, c27; not re-checked)
- [V] Liu et al. (2025) ChessArena. https://arxiv.org/html/2509.24239 (c10, c26; not re-checked)
- [V] Hwang et al. (2025) Strategic reasoning from chess post-training. https://arxiv.org/html/2507.00726 (c11)
- [V] Zhou et al. (2025) SPIN-Bench. https://arxiv.org/html/2503.12349 (c12; not re-checked)
- [V] Extracting search trees from LLM reasoning traces (2026). https://arxiv.org/html/2605.06840 (c13; not re-checked)
- [V] Do chess explanations reflect model decisions? (2026). https://arxiv.org/html/2609.22245 (c14)
- [M] Ciancarini and Pareschi (2026) systematic mapping of chess research. https://arxiv.org/abs/2609.18286 (c15; abstract only)
- [M] Valmeekam et al. (2023) self-critiquing plans. https://arxiv.org/html/2310.08118v1 (c16)
- [M] Deep Self-Evolving Reasoning. https://arxiv.org/pdf/2510.17498 (c18)
- [V] TsuGO: search efficiency on Go life-and-death (2026). https://arxiv.org/html/2608.13221 (c19; not re-checked)
- [M] LessWrong, Reasoning is not search: a chess example. https://lesswrong.com/posts/qtPjow35uJ7E2ELCc/reasoning-is-not-search-a-chess-example (c20)
- [V] Snell et al. (2024) Scaling test-time compute optimally. https://arxiv.org/pdf/2408.03314 (d04-d06)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/pdf/2406.01297 (d07)
- [V] Singh et al. (2026) ThinkRetrieve. https://arxiv.org/pdf/2608.10928 (d08)
- [V] Wu et al. (2026) Procedural knowledge at scale (Reasoning Memory). https://arxiv.org/pdf/2604.01348 (d09)
- [V] Chen, Koenig and Dilkina (2025) Iterative deepening sampling. https://arxiv.org/pdf/2502.05449 (d10)
- [V] Mirtaheri et al. (2025) A long chain of thought can be worth exponentially many short ones. https://arxiv.org/pdf/2505.21825 (d11)
- [V] Nguyen, Gupta and Le (2026) Uncertainty-aware budget allocation. https://arxiv.org/pdf/2605.26849 (d12)
- [V] Li et al. (2025) SelfBudgeter. https://arxiv.org/pdf/2505.11274 (d13)
- [V] Guan et al. (2026) OTBench. https://arxiv.org/pdf/2610.13570 (d14)
- [V] Yang et al. (2025) DEER. https://arxiv.org/pdf/2504.15895 (d15)
- [V] Lanham et al. (2023) Measuring faithfulness in chain-of-thought. https://arxiv.org/pdf/2307.13702 (d16)
- [V] Bogdan et al. (2025) Thought anchors. https://arxiv.org/pdf/2506.19143 (d17)
- [V] Shidara et al. (2026) mARC. https://arxiv.org/pdf/2601.11866 (d18)
