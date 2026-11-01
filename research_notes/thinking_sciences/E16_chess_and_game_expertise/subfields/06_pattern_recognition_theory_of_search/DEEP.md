# Pattern-recognition theory of search: deep document

*Subfield E16.06. Sources: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K26), critique.md in this folder. Status marks: [E] established, [S] single-source, [C] contested. [V] = source opened, [M] = snippet only.*

## 1. What it is

The theory says expert search is steered by recognition. A player sees a position. Stored patterns fire. Each pattern is tied to plausible moves, plans and partial evaluations. Search starts from those moves, not from all legal moves. Each new position reached in the mind's eye is recognised again, so recognition works at every node, not only at the root.

Two effects of recognition on search pull in opposite directions (Gobet 1997, d01):
- Recognition makes deep search cheaper than weak methods (fast move generation, fast evaluation).
- Recognition also removes the need for deep search, because a recognised evaluation is more reliable than a deep line.

These partly cancel. That is why depth differs only a little with skill on easy positions.

Correction from the full text (d01-d03, K18): Gobet 1997 does NOT claim templates cut node counts. The subfield blurb "templates guide and shorten search" is too strong. The paper claims templates (1) store information fast in long-term memory, (2) allow search in template space as well as move space, and (3) make up for the small short-term memory that loses the mind's-eye board.

Why it matters for our agent: S0 (gate). The theory is the human model of a fast first pass that proposes candidates, followed by slow verification. It also warns that the fast pass can block better answers (Einstellung). Links to parallel subfields: Chunking and templates; Computer chess and game AI; Einstellung effect; Recognition-primed decision making; Bounded rationality, anytime; Expert-novice differences; Test-time compute scaling.

## 2. History and theories in depth

**de Groot (1946/1965) [M, b17].** Thought-and-choice studies of grandmasters. Search statistics (moves examined, depth, speed) did not separate grandmasters from ordinary players. Even grandmasters seldom look at more than about 100 continuations (a06). What separated them was the quality of the first moves considered and memory for positions. Simon and Chase (1973) report that grandmasters and masters recalled about 93% of a 25-piece master-game position, experts about 72%, Class A about half, novices about 8 pieces (33%) (a01).

**Simon and Chase (1973) [V].** Statement of the theory (a03): patterns on the board are tied to plausible moves and trigger the heuristics that start search. Masters notice good moves at a glance, then analyse for minutes, sometimes finding the first impulse wrong. They estimated about 50,000 patterns (a P^7 > N argument, about 8x10^32 positions). Tournament moves average 3 to 4 minutes, up to half an hour. Eye movements (Tichomirov and Poznyanskaya, one expert): about 20 fixations in 5 s, mostly on occupied squares, many saccades from a piece to a piece it attacks or defends. This fits perception of relations, not a tree walk (a02). Masters' success in simultaneous play at a few seconds per move is explained by patterns tied to moves, and some tied to whole solutions such as traps (a04). Authors guessed many hundreds of patterns carry a full solution (no data). PERCEIVER and MATER programs simulate this.

**Chase and Simon chunk method, replicated by Gobet and Simon 1998 [V].** The 2-second gap between placements marks chunk boundaries. Replication with more players and a mouse: 79.5% of within-chunk latencies under 2 s versus 1.11% of between-chunk; 89.3% versus 4.4% under 2.5 s. 74.6% of pieces in a chunk shared 3 or more relations (67.6% in 1973) (a10). Masters used larger chunks than the 1973 master, who was inactive.

**Holding (1985, 1992) SEEK [M, b20].** Rival: skill is search plus evaluation, with knowledge. Holding and Reynolds (1982): skill (1000 to 2200 Elo) did not correlate with recall of random positions but did correlate with the quality of search for the best move in them (a08). Gobet and Simon reply that Holding read the theory as recognition only at the root, and that SEEK has no mechanism for retrieving knowledge; pattern recognition supplies one (a08, a09).

**Charness (1981) [M, b19].** Think-aloud: depth and breadth rose little with skill. Depth gain about 0.5 half-move per 200 Elo (a06). Regression used by Gobet: 2.3 ply at 1300 Elo, 4.1 at 2000, 5.7 at grandmaster (d02).

**Gobet and Simon (1996) [V].**
- Kasparov simultaneous play (a05): with one quarter to one eighth of the normal time per move, against 4 to 8 opponents (almost all masters or grandmasters), his estimated performance fell only about 100 Elo (worked example: 2450 + 400(4.5-1.5)/6 = 2650 versus about 2750 usual). No correlation between number of boards and performance. Reading: recognition carries most of the strength.
- Calderwood, Klein and Crandall (1988) (a07): a grandmaster-rated move quality showed no big drop between regular play (2.25 min per move) and blitz (5 min per game, about 6 s per move).
- Templates (a11-a14, b01-b06): a core of about a dozen pieces plus slots for extra pieces, squares, openings, plans, moves and links to other templates. Recognition by an EPAM-style discrimination net. Slots fill in about 1 s in the model; bound from Saariluoma (1989) is 2 s or less at 60%+ accuracy. New chunks are learned at 5 to 10 s each.
- Random and distorted positions (a15-a17): a discrimination net up to 70,000 nodes, 20 random fixations (about 5 s of viewing), reproduces human recall. Recall rises with the log of node count (over 98% of variance). The classic "experts lose their edge on random positions" is overstated: skill still separates levels on random positions (e.g. F(3,17) = 10.35, p < .05 in one reviewed study), only much less than for game positions.

**Gobet (1997) [V, Brunel preprint] (d01-d03).** The SEARCH program: 1,000 episodes per net size; time per heuristic move 20 s, per heuristic evaluation 10 s, per mental move 2 s. Mean depth under 1 ply with no chunks, about 2.5 ply at 1,000 chunks, about 4 ply at 30,000 (expert), over 5 ply above 100,000 (grandmaster). About 75% of episodes end by recognised evaluation. Parameters set by the author. It tests the one anomaly in human data: Saariluoma (1990) found masters (about 2200) searched 52 nodes at average depth 5.1, IMs and GMs 23 nodes at 3.6. The model gives such dips only with small samples (50 episodes), so the author calls the anomaly sampling noise.

**Campitelli and Gobet (2004) [V] (d04, d05).** N = 4 (GM 2550, IM 2500, CM 2100, class B 1750), think-aloud on three very hard positions (solutions needing 52, 60, 70+ nodes, up to 23-35 ply). Search grew with Elo. Mean depth 13.8, 10.5, 7.4, 2.8 ply; nodes 370, 405, 153, 88; rate 12.3, 13.5, 6.8, 3.2 nodes/min. Regressions: depth = -18.3 + 0.012 Elo (r = .97); nodes = -645 + 0.4 Elo (r = .96). Second block: 10-second decisions on easy positions (depth 6.4 ply, 10.4 nodes): correct GM 23 (46.9%), IM 18 (36.9%), CM 4 (8.2%), CB 2 (4.1%); recall of game positions 83.2%, 85%, 54%, 47%. So "flat search" is a feature of easy positions and verbal protocols (K01).

**Einstellung line [V] (d06, d07).** Bilalic, McLeod and Gobet (2008): candidate masters who found the familiar five-move smothered mate said they were hunting for a shorter mate, but kept fixating the familiar squares. The familiar-solution group stopped at about 37 s (SD 20), then found the 3-move mate in a mean 148 s (SD 90) versus 79 s (SD 25) for players who saw only the one-solution problem. Gaze: time x squares interaction F(5,20) = 11.9 (no-Einstellung group) versus F(5,20) = 0.6 (Einstellung group). The cost equals about 3 SD of skill (about 600 Elo). Sheridan and Reingold (2013) replicated with N = 34 (17 experts mean 2223 CFC, 17 novices): 8 of 17 experts and 8 of 17 novices chose the familiar suboptimal move; the effect vanished when the familiar move was a blunder; experts looked at the target region sooner (407 ms versus 719 ms, p < .01).

**Modern AI line.** Programs that mimic recognition without search (Section 6): Ruoss 2024, Jenner 2024, Schultz 2024, Maia.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Search statistics do not separate masters from ordinary players on easy positions | Experts rarely over 100 continuations; masters = weaker players in max depth (Gobet 1994) | de Groot; Gobet & Simon 1996 (a06) | [C] (K01) |
| Search does grow with skill on hard positions | Nodes 88/153/405/370; depth 2.8/7.4/10.5/13.8 ply; N = 4 | Campitelli & Gobet 2004 (d04) | [S] small N |
| Memory for game positions rises with skill | GM/M about 93%, expert about 72%, Class A about 50%, novice 33% | Simon & Chase 1973 (a01) | [E] |
| Random-position recall is low and nearly flat, not zero effect | Random board: masters 21.1%, experts 17.7%; game board: masters 92.3%, experts 64.5% | Gobet & Simon 1996 (b03, a17) | [E] (K03) |
| Chunks are recalled fast | 79.5% within-chunk latencies under 2 s vs 1.11% between | Gobet & Simon 1998 (a10) | [E] (K04) |
| Templates explain multi-board recall | 1-5 boards, 5 s each, N = 13; masters up to about 60 pieces; gap 1 to 10 s: +71% (2 boards), +63% (4) masters; +40%, +33% experts | Gobet & Simon 1996 (a11, b02, b03) | [S] (K05) |
| Trained single subject extends boards | 5 to 9 boards over about 150 sessions, up to 178 pieces correct | Gobet & Simon 1996 Exp 3 (a12, b04) | [S] one subject |
| Mirror distortion costs recall; favours exact-location chunks | Net: normal 65.4%, horizontal 63.2%, vertical 53.3%, central 52.5%. Humans (N = 25): 77.3/49.7/34.5% vs 62.9/38.6/27.5% | Gobet & Simon 1996 (a15, a16) | [S] |
| Recall rises with log of net size | log fit over 98% of variance; random positions only to 23.4% | Gobet & Simon 1996 (a15) | [S] model |
| Kasparov time-pressure cost | About 100 Elo lost at 1/4 to 1/8 of the time | Gobet & Simon 1996 (a05) | [S] natural experiment |
| SEARCH model depth by net size | 2.5 ply (1,000 chunks), 4 (30,000), over 5 (100,000+); about 75% end by recognised evaluation | Gobet 1997 (d02) | [E] as model output; params author-set |
| Concurrent load cuts recall | Strong players -60% (visuospatial), -48% (executive), tactics about -37%; verbal none; skill x load F = 1.08 ns | Robbins et al. 1996 (d08) | [C] (K06) |
| Delay after presentation costs little | 30 s delay: 6-8% drop | Charness 1976 (a14, d09) | [C] (different paradigm) |
| Einstellung cost | About 3 SD (about 600 Elo); 8/17 experts and 8/17 novices chose familiar suboptimal move; gone when familiar move is a blunder | Bilalic 2008; Sheridan & Reingold 2013 (d06, d07) | [E] (K19) |
| Einstellung is an attention bias | Gaze F(5,20) = 0.6 vs 11.9 | Bilalic 2008 (d07) | [E] (K20) |
| Searchless transformer reaches GM level | 270M: tournament Elo 2299, blitz 2895 vs humans (2299 vs bots), puzzles 95.4%; 136M 2259/94.5%; 9M 2025/88.9% | Ruoss 2024 (a20, b07, c06) | [E] (K08) |
| Policy-only lags search | Leela policy 2292/88.6% vs 400 sims 2858/99.6%; AlphaZero policy 56.1%, value 82.0%, 400 sims 95.6% | Ruoss 2024 (b10, c05) | [E] (K09) |
| Small search over a recognition model adds a lot | 100 MCTS sims: +68 internal Elo; about +300 overall; log growth in sims; searchless MAV 2923/2875 | Schultz 2024 (a24, c09) | [E] (K10) |
| A policy net holds a future move | Probe 92% for move 2 turns ahead; patch cuts log-odds 1.88 +/- 0.04; attention entry large in 29.8% of puzzles | Jenner 2024 (a22, b11, c01-c03) | [S] (K11) |
| Models trained on moves build a board | Legal move 99.8%/99.6%; win vs Stockfish L0 46%/64%; legal rate 41% to 92% by board edit; skill edit 2x/2.6x | Karvonen 2024 (a25, b12) | [E] (K12) |
| Engine strength is not human-likeness | Stockfish depth 1-15 matches humans 33-41%; Leela 46%; Maia 46-52%+; +10 rollouts hurts Maia | McIlroy-Young 2020 (b14, c11, d11) | [E] (K13, K26) |
| Plain language models are weak at chess | GPT-3.5-turbo-instruct 66.5%, Elo 1755 vs bots | Ruoss 2024 (a21) | [E] (K14) |
| Reasoning models far ahead of non-reasoning | Win rate vs random 45.4% vs 0.7%; instruction errors 24.4% vs 71.9% | Kolasani 2025 (c18) | [E] (K14) |
| Expert notes as cues | o1-mini +14 (strategy), +24 (tactic), +34 (both); gpt-4o +30 (both) | Wang 2024 MATE (c15) | [S] (K15) |
| Search beats policy-only on hard items only | MATH: beam worse than best-of-N at levels 1-2, better at 3-4; difficulty allocation about 4x less compute | Snell 2024 (d15) | [E] (K21) |
| Search over reasoning steps | Game of 24: CoT 4.0%, ToT b=1 45%, b=5 74%; CoT best-of-100 49% | Yao 2023 (d16) | [E] (K21) |
| Gated fast-then-slow agent | Tokens per action 757 vs ReAct 1,971, Reflexion 2,983 | SwiftSage (d18) | [S] (K22) |
| Retrieved thought templates | Game of 24 82.4% vs ToT 74.0%, CoT 11.0%; about 12% of multi-query cost | Buffer of Thoughts (d17) | [S] (K22, K23) |
| LLM chess: effort helps, parallel does not | Effort +15% (low to medium), +20% (low to high); 3x/5x MoA flat; best Elo about 758 | Kolasani 2025 (d12) | [E] (K24) |
| RL for chess plateaus | 25-30% puzzle accuracy; board-state probe accuracy 0.0% in six models | Hwang 2025 (c20, d14) | [S] |

## 4. Mechanisms and models

**4.1 Discrimination net (EPAM, CHREST style).** Build it as a decision tree over features. Each node tests one feature (piece on square, relation). Leaves hold chunks. Learning adds a node when two inputs reach the same leaf but differ. Model cost: 5 to 10 s per chunk. Recall quality grows with the log of node count (a15). Perception: about 20 random fixations (5 s of viewing). Retrieval from a chunk returns links to moves, plans and a partial evaluation.

**4.2 Template = core plus slots.** Core: about 12 fixed items. Slots: variable items (extra pieces, squares) plus pointers (opening, plan, candidate moves, other templates). Slot fill time under 1 s in the model, bounded at 2 s or less with 60% accuracy. Predicts about 7 +/- 2 positions held, not more (a13). In software: a typed record with default values, a key (the core), and slot fillers extracted from the instance.

**4.3 SEARCH program (Gobet 1997).** Loop:
1. Perceive the position; retrieve chunks and templates from the net.
2. Candidate moves = moves attached to retrieved patterns (about 2 s if by recognition, 20 s if heuristic). Template-space search is also allowed: jump to a linked template (a new plan) without making moves.
3. Make a mental move (2 s). Re-perceive the new position. Recognition returns new moves and an evaluation.
4. Stop on: recognised evaluation (about 75% of episodes), a heuristic evaluation (10 s), or time out.
5. Output the best evaluated line.
Depth follows a power law in chunk count (2.5, 4, over 5 ply). Free parameters were author-set, so the shape is a qualitative prediction.

**4.4 Two-pass control for an agent (our reading, [D]).** Pass 1, recognition: retrieve the class record and templates, propose candidate answers. Pass 2, verification: run checks on each candidate. Escalate to search only when pass 1 signals trouble (check fails, candidates disagree). SwiftSage (d18) is a working example: the fast policy acts by default, the planner is called only on hard states, 757 tokens per action versus 1,971.

**4.5 Policy plus limited search (AlphaZero, Leela, MAV).** Policy proposes, value evaluates, a small MCTS refines. Gain per simulation is logarithmic (a24). In Schultz 2024 the model also writes its own tree in context and builds the requested tree shape 99.6% of the time (5,980 positions) (c10): internal search costs tokens and strength rises with tokens.

**4.6 Amortised planning.** Ruoss 2024 trains a transformer to copy Stockfish action values from 10M games (15.3B action values). Planning moves into the weights. 270M parameters give 2299 tournament Elo with no test-time search. Scale and data both matter; with 10K games, models of 7M+ parameters overfit (b08).

**4.7 Einstellung as a model.** The first recognised solution biases attention toward its features. Alternative search then keeps visiting the same features (gaze F = 0.6). In design terms the second pass must be forced onto new cues (squares or features not in the first answer).

## 5. What holds up

**Holds (several sources, direct evidence):**
- Recall advantage is strong for game positions, much smaller for random ones (K03). The vanishing-expertise claim is overstated (a17).
- Chunk boundaries by latency replicate in 1998 (K04).
- Patterns drive early move proposals; masters verify for minutes (K02). Evidence is eye movements, de Groot, simultaneous play: indirect but consistent.
- Fast pattern matches block better solutions even in experts (two labs) (K19, K20).
- Searchless networks reach master level; search still adds a margin (K08-K10).
- Search helps most on hard items and can hurt on easy ones in LLMs (K21).

**Contested:**
- Recognition or search as the source of skill (K07). No single test splits them. Kasparov (-100 Elo), blitz (little loss) and Holding and Reynolds each fit parts of both.
- Flat search with skill (K01): holds for easy positions, fails for hard ones (N = 4).
- Dual-task (K06): Bradley, via Gobet and Simon, reports a drop of over two thirds in recall; Charness 6-8%; Robbins 48-60% recall and about 37% tactics. Different paradigms (concurrent load versus post-delay), so not a failed replication. "Over two thirds" was not reproduced. Robbins found no skill x load interaction (power about 20%), so a recall/search resource split is not supported.
- Training LLMs on traces (K16): long-game supervision +350 Elo (ChessLLM), but puzzle accuracy plateaus at 25-30% for RL and reasoning SFT (Hwang).

**Weak spots:**
- Human data are small: templates N = 13 and N = 25; one-subject training study; Campitelli and Gobet N = 4.
- Gobet and Simon 1996 numbers are partly second-hand (paywalled); several 1990s citations (b17-b25) were not verified.
- No AI study tests the human claim that patterns shorten search. Nearest: Schultz (search added to a searchless model) and Snell (search gated by difficulty).
- SEARCH parameters are author-set, not fitted.
- Maia loses agreement with humans when tree search is added (d11): human choice is closer to policy than to search.

**Interventions that worked:** expert notes as cues (+34 on o1-mini, K15); retrieved thought templates (82.4% Game of 24, K22); gated fast/slow agent (757 tokens per action); difficulty-based compute allocation (about 4x); distilling engine reasoning into short chain-of-thought (C1 48.1% vs teacher 40.8%, c21); engine-reading 4B model (QU: 1782 to 2697 Elo in seven rounds, c22, single source, 2026).

**Interventions that did not work:** mixture-of-agents parallel samples (flat); RL with dense chess reward (plateau 25-30%); SFT on o3 traces (ceiling unchanged; Llama3.1-8B fell); adding rollouts to Maia (agreement lower); beam search on easy MATH items (worse as budget grew).

## 6. Language models

**General LLMs on chess.**
- GPT-3.5-turbo-instruct: puzzles 66.5%, Elo 1755 vs bots (Ruoss, a21). The specialised searchless transformer: 95.4% and 2299.
- LLM Chess (Kolasani 2025, 50+ models vs a random opponent): reasoning models win 45.4% on average (top near 100%), non-reasoning 0.7% (best 3.3%). Instruction-following errors 24.4% vs 71.9%. o4-mini (medium) picks the best move 19.5% of plies versus 4.1% for GPT-4.1-mini; blunders 4.2% versus 31.3%. Best adjusted Elo about 758 against engine skill levels (chess.com average 611). Reasoning effort: +15% win rate (low to medium), +20% (low to high). Board format: for o4-mini (low), changing format raised performance by over 15% (FEN reached 95%); another ablation lowered Grok 3 Mini (low) by almost 30%. Mixture-of-agents 3x and 5x: no clear gain.
- ChessArena (Liu 2026, 13 LLMs, 800+ games): none beat Maia-1100 (Glicko 2220). o3 1830, Doubao-Seed-1-6-Thinking 1776, Gemini-2.5-Pro 1699, fine-tuned Qwen3-8B-Chess 1686, GPT-4.1 1583. Puzzles: Stockfish 98.4%, Maia-1100 74.6%, o3 55.6%, all other LLMs under 15%. Banning visible thinking (Bullet mode) made nearly all models play badly. Token caps 4,096 (non-thinking) and 16,384 (thinking): budgets are not equal.
- Hwang 2025: dense action-value reward beat sparse reward; plateau 25-30% puzzle accuracy against 66.5% for a searchless 1800-Elo net; board-state probe accuracy 0.0% in six base/instruct models, MATE accuracy 12.7-53.7%. Authors point to missing chess knowledge (a store problem), not missing reasoning.
- ChessLLM (Zhang 2025): 3B model on complete games: Elo 1788 vs Stockfish with 10 samples; wins 61% vs skill 0, 56% skill 1, 30% skill 2; long-game supervision +350 Elo over short-round data.
- C1 (Tang 2026): 4B model, 48.1% from near zero; teacher Gemini-3-Flash 40.8%; 19.3% at 8k samples, 29.7% at 16k, 40.9% at 39k; full fine-tuning 40.9% vs LoRA 32.1% (rank 16) and 38.8% (rank 64).
- QU (Bhaskar 2026): 4B model reading a strong engine's encoder, 1782 to 2697 Elo; beats the strongest frontier model by over 600 points; picks a different top move from Leela in 538 of 1,000 positions.
- Rationales: Dionisopoulos 2026: best-move training gives the strongest RL results but reasoning that does not match the move; hallucinated token share 0.04% (factual board answering) to 12.69% (rejection sampling). Parfenova 2026 (200 endgame puzzles): random plausible explanations lower correct-move probability; explanations add little once move hints are masked. Kshirsagar 2026: swapping latent thoughts for matched noise left performance unchanged. Written reasoning is not evidence of how the move was chosen (supports G10).
- Shen 2026: pretraining loss predicts post-RL performance (5M-1B params); RL on hard puzzles surfaces moves nearly absent before; on easy puzzles RL amplifies what SFT preferred. Stored pattern knowledge limits what reasoning can reach.
- Wang 2024 MATE: expert notes as cues: o1-mini +34 with both notes, gpt-4o +30 over no notes; fine-tuned LLaMA-3-8B beat the best commercial model.
- ChessQA (Wen 2025): five levels (Structural, Motifs, Short Tactics, Position Judgment, Semantic); weaknesses in all five; no model numbers read.

**Searchless and internal-search networks.** Ruoss 2024 (above). Jenner 2024: Leela's policy net encodes moves two turns ahead (probe 92%, log-odds drop 1.88). Karvonen 2024: GPT on move text builds a board (99.6% probe) and estimates skill. Toshniwal 2022: piece-location accuracy 91.3% (small data) to perfect (large, with RAP); legal-move accuracy above 97%. McGrath 2022: human concepts become decodable in AlphaZero (many start rising near 32,000 steps; piece values converge after about 128,000). Schut 2023: four top grandmasters improved after seeing AlphaZero concept examples (N = 4).

**Compute allocation in general LLM reasoning.**
- Snell 2024 (MATH): beam search with a process verifier worse than best-of-N on levels 1-2, better on 3-4, no progress on level 5; difficulty-aware allocation matches best-of-N with up to about 4x less compute.
- Yao 2023 ToT: IO 7.3%, CoT 4.0%, CoT-SC (k=100) 9.0%, ToT b=1 45%, b=5 74%, CoT best-of-100 49%, IO best-of-100 33%. Cost: ToT 5.5k completion + 1.4k prompt tokens, $0.74 for 74%; CoT best-of-100 6.7k + 2.2k, $0.47, 49%.
- Buffer of Thoughts: Game of 24 GPT-4 3.0%, CoT 11.0%, PAL 64.0%, ToT 74.0%, GoT 73.2%, Meta-prompting 67.0%, BoT 82.4%. +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One. About 12% of multi-query cost. Llama3-8B + BoT 78.4 vs Llama3-70B 73.4.
- SwiftSage: 757.07 tokens per action vs SayCan 1,855.84, ReAct 1,971.03, Reflexion 2,983.46.
- Searchformer: 93.7% unseen Sokoban, up to 26.8% fewer search steps than A*; A* traces 34.3% longer after 3 rounds; 10x smaller data.

**Reading.** Stored knowledge sets the ceiling; search adds most where there is a foothold and the item is hard. No study compares recognition-first with escalation against always-search at equal tokens on single-answer reasoning. That test is ours to run (UNKNOWNS U1).

## 7. What our agent should take

### Add now (established)
| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Keep S0 as a recognition step: retrieve the class record and propose candidates first; verify by code after. Log whether the verified answer came from the first-pass list. | S0/S3 | [E] for the human pattern; agent form [S] | K02; a03, a02, a05 |
| Spend search by difficulty and foothold: skip or cut it where the first pass is likely right; use it where items are hard and there is some success. Already G12; new evidence agrees. | G12/S0 | [E] | K21, K09; d15, d16, b10, c05 |
| Do not cap search depth by rule. Stop on checks and budget. | G11/S4 | [E] | K01, K07; d04 |
| Keep an explicit state and restate the problem structure. | S1/S2 | [E] | K03, K12; b03, a25, b12 |
| Do not read written reasoning as evidence of how an answer was chosen (confirms G10). | G10 | [E] | c23, c24, c25 |
| Compare any new element at equal tokens; token caps and effort levels differ across studies. | G7 | [E] | K24; d12, d13 |

### Test first
| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Recognition-first with escalation versus always-search at equal tokens | S0 | [S] | K22, K21; d18, d15 |
| One alternative-search step with a different cue after a plausible first answer. Conflicts with G1 unless fired by a signal (disagreement, failed check, trap flag). | S0/S6/O8 | [C] (human only) | K19, K20; d06, d07 |
| Slot-based template store (core plus slots) for problem classes; test on unseen instances and families | memory | [S] | K05, K23; a13, d17 |
| Retrieved hint notes (strategy, tactic) shown after the first attempt | memory | [S] | K15; c15 |
| Search traces distilled into a short quick pass | S3/O3 | [S] | K17, c21; b15, c27 |
| Difficulty-estimating gate that routes items to direct, short or search modes | S0/G12 | [E] direction, [S] our cost | K21 |
| Lessons and templates after the first attempt versus before it (fixation check) | memory | [S] | K19 |

## 8. Concrete tests on our bench

All arms at equal tokens; setup cost counted (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Recognition-first with escalation | Single-answer reasoning and puzzle items with a check (math, ARC-style, code with tests) | (a) always-search, (b) direct only, (c) quick candidate pass then verify, search only on failure | Accuracy at fixed tokens; tokens to first correct | (c) matches (a) on hard items and beats it on easy ones; the gain is in tokens |
| T2 Familiar-wrong trap | Items with a common, plausible, suboptimal or wrong answer | (a) first pass, (b) first pass plus forced new-cue second pass, (c) second pass only on signal | Accuracy; right-to-wrong flips | (b) gains on trap items and loses on non-trap; (c) keeps the gain without the loss (G1) |
| T3 Difficulty gate | Mixed-difficulty set | Uniform search vs gate by class pass rate vs gate by first-pass agreement | Accuracy per token | Up to about 4x saving (Snell); smaller for small models |
| T4 Template store with slots | Problem families with parameters | (a) no store, (b) slots, (c) flat examples; held-out instances and held-out families | Accuracy; transfer gap | (b) over (c) on instances; both drop on new families |
| T5 Hint notes | Domain tasks with candidate sets | None / strategy / tactic / both, after versus before first attempt | Accuracy; flips | Gains like MATE (+14 to +34) only when notes are accurate; before-attempt placement anchors |
| T6 Structured vs shuffled state | State-tracking items | Structured state vs shuffled state restatement | Restatement accuracy | Larger gap for structured state in stronger models |
| T7 Search foothold | Items bucketed by plain pass rate | Search vs no search per bucket | Marginal gain per bucket | Near zero at low and high ends, largest in the middle |

## 9. What does not transfer, and why

- **Human memory limits.** Template theory fixes a 5 s viewing time and about 7 +/- 2 chunks. Our agent has no such short-term bottleneck, so memory relief does not apply. Only retrieval and slot filling transfer.
- **Chunk counts.** 50,000 chunks and ten years of play are not a target. Our store holds at most a few hundred problem classes.
- **Perception and eye movements.** Fixation and visual span do not exist for a text model. Einstellung attention bias transfers only as a rule: the second pass must use new cues.
- **Dual-task findings.** Concurrent visuospatial load does not map onto token budgets. K06 is human working memory only.
- **Training-time findings.** Searchless transformers (Ruoss, Maia, Searchformer) need weights trained on millions of games. We cannot train. Their lesson is the ceiling set by stored knowledge, not a method we can copy.
- **Chess is closed and exact.** It has perfect information, a fixed move set, and a checkable evaluator. Many of our items have none. Search gains in chess may not carry to open problems (G8, open mode).
- **The 2.5/4/5 ply curve** comes from a model with author-set parameters. Do not use it as a depth cap.
- **Expert notes (MATE)** were written for a fixed candidate set. Free retrieval of notes can anchor (S5 memory rule).
- **Internal look-ahead (Jenner)** is a fact about weights, not about a prompt.

## 10. Open questions

1. LLM Einstellung cost: how large is the loss when a pattern-matched first answer blocks a better one? No study found; search quotas ran out, so this is untested, not shown absent.
2. Equal-token comparison of recognition-first with escalation against always-search on math or code. None exists.
3. Do templates with slots beat flat examples for LLMs? No slot ablation exists (Buffer of Thoughts has none).
4. Do patterns shorten search in LLMs (nodes, depth, stop reason), not just token cost?
5. A large-N human study separating search quality from recall (modern eye tracking, think-aloud). Campitelli and Gobet is N = 4.
6. Gobet and Simon 1996, Charness 1976 and Bradley 1987 originals were not fully opened.
7. The policy-only Lichess 2600+ bot is reported but not independently measured (K25).
8. Does imitating human experts beat engine supervision for a scaffold's quick pass beyond move matching?
9. Which 2025-2026 LLM chess results survive equal token budgets?
10. Does the SEARCH stop rule (recognised evaluation, about 75% of episodes) have an analogue in LLM stop signals, and how reliable is it?

## 11. Sources

URLs as recorded in the evidence files.

- [V] Simon and Chase (1973) Skill in Chess. https://www.gwern.net/doc/psychology/chess/1973-simon.pdf (a01-a04)
- [V] Gobet and Simon (1996) Roles of recognition processes and look-ahead search in time-constrained expert problem solving. https://bura.brunel.ac.uk/bitstream/2438/1338/1/FullText.pdf (a05-a07, a27)
- [V] Gobet and Simon (1998) Expert chess memory: revisiting the chunking hypothesis. https://bura.brunel.ac.uk/bitstream/2438/1343/1/Copy-Task-NEW-BJP.pdf (a08-a10)
- [V] Gobet and Simon (1996) Templates in chess memory. https://www.gwern.net/doc/psychology/chess/1996-gobet.pdf ; https://doi.org/10.1006/cogp.1996.0011 (a11-a14, b01-b06)
- [V] Gobet and Simon (1996) Recall of random and distorted chess positions. https://www.gwern.net/doc/psychology/chess/1996-gobet-2.pdf (a15, a16)
- [V] Gobet and Simon (1996) Recall of rapidly presented random chess positions is a function of skill. https://bura.brunel.ac.uk/bitstream/2438/1346/1/FullText.pdf (a17)
- [V] Richman, Staszewski and Simon (1995) EPAM IV. https://www.gwern.net/doc/psychology/chess/1995-richman.pdf (a18)
- [V] Gobet (1997) A pattern-recognition theory of search in expert problem solving. https://bura.brunel.ac.uk/bitstream/2438/843/1/Templates_and_search.pdf (d01-d03); [M] DOI page https://doi.org/10.1080/135467897394301 (a19, b16)
- [V] Campitelli and Gobet (2004) Adaptive expert decision making. https://bura.brunel.ac.uk/bitstream/2438/825/1/Gobet_Search_ICGA.pdf (d04, d05)
- [V] Bilalic, McLeod and Gobet (2008) Why good thoughts block better ones. https://bura.brunel.ac.uk/bitstream/2438/2276/1/Einstellung-Cognition.pdf (d07)
- [V] Sheridan and Reingold (2013) Einstellung in chess. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3790829/ (d06)
- [V] Robbins et al. (1996) Working memory in chess. http://link.springer.com/content/pdf/10.3758/BF03197274.pdf (d08)
- [M] Charness (1976) Memory for chess positions. https://doi.org/10.1037/0278-7393.2.6.641 (d09)
- [M] de Groot (1946/1965); Chase and Simon (1973); Charness (1981); Holding (1985, 1992); Reingold et al. (2001); Gobet and Simon (2000); Linhares and Brum (2007); Campitelli and Gobet citations (b17-b25; no URL recorded)
- [V] Ruoss et al. (2024) Amortized planning with large-scale transformers. https://arxiv.org/abs/2402.04494
- [V] Jenner et al. (2024) Evidence of learned look-ahead in a chess-playing neural network. https://arxiv.org/abs/2406.00877
- [V] McGrath et al. (2022) Acquisition of chess knowledge in AlphaZero. https://arxiv.org/abs/2111.09259
- [V] Schultz et al. (2024) Mastering board games by external and internal planning with language models. https://arxiv.org/abs/2412.12119
- [V] Karvonen (2024) Emergent world models in chess-playing language models. https://arxiv.org/abs/2403.15498
- [V] Toshniwal et al. (2022) Chess as a testbed for language model state tracking. https://arxiv.org/abs/2102.13249
- [V] McIlroy-Young et al. (2020) Aligning superhuman AI with human behavior. https://arxiv.org/abs/2006.01855
- [V] Lehnert et al. / Meng et al. (2024) Searchformer. https://arxiv.org/abs/2402.14083
- [V] Monroe and Chalmers (2024) Mastering Chess with a Transformer Model. https://arxiv.org/abs/2409.12272
- [V] Schut et al. (2023) Bridging the human-AI knowledge gap. https://arxiv.org/abs/2310.16410
- [V] Wang et al. (2024) MATE. https://arxiv.org/abs/2411.06655
- [V] Zhang et al. (2025) ChessLLM. https://arxiv.org/abs/2501.17186
- [V] Liu et al. (2026) ChessArena. https://arxiv.org/abs/2509.24239
- [V] Kolasani et al. (2025) LLM Chess. https://arxiv.org/abs/2512.01992
- [V] Hwang et al. (2025) Strategic reasoning from learning chess. https://arxiv.org/abs/2507.00726
- [V] Tang et al. (2026) C1. https://arxiv.org/abs/2603.20510
- [V] Bhaskar, Cheng and Chen (2026) QU. https://arxiv.org/abs/2610.03695
- [V] Dionisopoulos et al. (2026) How reasoning evolves from post-training data. https://arxiv.org/abs/2604.05134
- [V] Parfenova (2026) Do chess explanations reflect model decisions? https://arxiv.org/abs/2609.22245
- [V] Kshirsagar (2026) The weight of silence. https://arxiv.org/abs/2607.20952
- [V] Shen et al. (2026) Understanding reasoning from pretraining to post-training. https://arxiv.org/abs/2607.16097
- [V] Wen, Tang and Anderson (2025) ChessQA. https://arxiv.org/abs/2510.23948
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Wang et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 7 established claims: 6 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E16.06-K21** (reworded: the sources support less). Snell et al. numbers are right (more than 4x compute saving; beam search over-optimizes on the easy bins 1-2 and helps on bins 3-4) but the bins are model-specific pass@1 quantiles, not MATH levels; Yao et al. Table 7 shows ToT's 74% costs about as many tokens as 100 CoT trials, whose best-of-100 reaches 49%, so setting 74% against single-sample CoT's 4% is not a matched-budget comparison. Corrected claim: In LLM reasoning, search beats best-of-N on harder items but not easier ones: on MATH, PRM-guided beam search was worse than best-of-N in the two easiest model-specific difficulty bins and better in bins 3-4, and choosing the method by estimated difficulty cut test-time compute by more than 4x; on Game of 24, Tree of Thoughts (b=5) reached 74% at about the completion tokens of 100 CoT samples, versus 49% for best-of-100 CoT (single-sample CoT: 4%).
- **E16.06-K03** (now single-source: only one opened source, code check).
- **E16.06-K04** (now single-source: only one opened source, code check).
- **E16.06-K08** (now single-source: only one opened source, code check).
- **E16.06-K09** (now single-source: only one opened source, code check).
- **E16.06-K10** (now single-source: only one opened source, code check).
- **E16.06-K13** (now single-source: only one opened source, code check).
- **E16.06-K18** (now single-source: only one opened source, code check).
- **E16.06-K26** (now single-source: only one opened source, code check).
