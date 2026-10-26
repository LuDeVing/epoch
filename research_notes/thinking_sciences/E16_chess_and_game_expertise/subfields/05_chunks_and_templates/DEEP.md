# Chunking and template theory: deep document

*Subfield E16.05. Source files in this folder: evidence_a-d.jsonl (ids a01-a34, b01-b30, c01-c27, d01-d22), claims.jsonl (K01-K26), critique.md. Evidence ids are cited in brackets. "Opened" means the page or PDF text was read in this series; snippet-only sources are marked in section 11.*

## 1. What it is

Chunking and template theory asks one question: what do experts store, and how does what they store cue what they do next?

The answer from chess is this. Experts hold a very large store of familiar patterns in long-term memory (order of 10,000 to 100,000, often quoted as 50,000). A pattern is recognised fast. Recognition does two things. It lets the expert take in a lot at a glance (recall). It also calls up a short list of candidate moves (action). Search then checks that short list. The expert does not search more than a weaker player. The expert searches fewer, better branches. [a07, a08, a26]

Three layers of theory have been built:

1. **Chunking theory** (Chase and Simon, 1973). Skill is a big indexed store of small chunks. Short-term memory holds about 7 of them. Each chunk is also the condition of a production, so seeing it triggers an action.
2. **Template theory** (Gobet and Simon, 1996). Some very frequent chunks grow into templates: a fixed core (about a dozen pieces) plus slots with default values, linked to other templates. Slots fill in under a second. This explains how a master holds many boards at once.
3. **Computer models**: MAPP, CHREST (discrimination net, 3-chunk visual short-term memory, simulated eye movements), SEARCH, CHUMP. They turn the verbal theory into numbers that can fail. [a07, a13, a21, c06]

Why this matters for our agent. We build one language-model agent that thinks through a scaffold, not by training. The agent analogue is a memory of solution templates or patterns, retrieved by a cue, that propose candidate answers or operators. Code then checks them. Most of the chess story maps onto four design questions:

- What is the unit of memory (small fragment, or core plus slots)?
- How is it indexed (surface form, or abstract roles)?
- How many items should be retrieved at once?
- What should be allowed into the store, and what should be thrown out?

The chess evidence answers the first two weakly (human data, one lab). The LLM-agent literature (2023 to 2026) answers the last two better. The link between them is by function, not by mechanism (critique.md). A template in an LLM agent is a retrieved text or code block. It is not a perceptual chunk.

## 2. History and theories in depth

### 2.1 De Groot to Chase and Simon (1946 to 1973)

De Groot found that grandmasters did not search deeper or wider than weaker players. They found the right moves earlier. A grandmaster chose the best move about 93% of the time after 2 to 5 s; the weakest subject (Class A level) about 50%. Masters seldom looked at more than 100 continuations. [a08]

Chase and Simon (1973) turned this into a method. Three players (a master, a Class A player, a beginner) did two tasks on the same positions: copy a board in plain view, and de Groot's 5 s memory task. Glances and pauses cut output into chunks. [a01]

Main findings:

- **Real vs random positions.** The master placed about 16 pieces right in middle-game positions, the Class A player about 8, the beginner about 4. On random boards all three did worse than the beginner did on real boards, and there was no relation to skill. [a02, b01]
- **The 2 s boundary.** Pieces placed within one glance came fast (modal gap half a second or less) and had many chess relations (defence, proximity, same colour, same type). Pieces after a glance back came slower and were related near chance. [a04]
- **Small chunks.** About 2 to 4 pieces. Pieces per chunk in the memory task: 2.5, 2.1, 1.9 (master, Class A, beginner). The master's first recalled chunk had 3.8. [a05]
- **Chunk content.** 77 chunks in 14 positions. 47 held a pawn chain. 27 were same-colour clusters (9 back-rank, 9 connected rooks or queen with rooks). 17 could not be classified. So 60 of 77 (78%) fit the three families. Of 18 strong attacks, 11 were chunked. [a06, critique]
- **An anomaly.** The master recalled more chunks (7.7 per trial, middle game, against 5.7 and 5.3), which the equal-chunk-number idea had not predicted. The authors suspected higher-level organisation. [a05]
- **Exact game recognition did not help.** The master recognised 4 of 9 puzzle positions in the first second; recall was 83% recognised vs 79% not. N is tiny. [a03]

Limits already visible in 1973: one subject per skill level; the master got about 16 of 25 where de Groot's masters got 23 to 24; de Groot noted that guessing the average master position gives about 44%. [a02, b01]

### 2.2 Problems for the original theory (1976 to 1998)

- **Interference.** Charness (1976): a 30 s delay with an interfering task cut recall by only 6 to 8%. If chunks lived only in short-term memory, a distracting task should wipe them out. Frey and Adesman (1976) found a small loss for two boards plus counting backward. [a14, b06]
- **Several boards.** Masters can rebuild 5 boards, and one trained master reached 9. Seven chunks of 4 to 5 pieces (about 35 pieces) cannot hold that. [a09, a10, b29]
- **Random positions.** The textbook "no skill effect" came from 3 subjects. Reviews found the strongest group beat the weakest in 12 of 13 comparisons. [a18, b05]
- **Chunk size.** Later work found masters' chunks were far bigger than 5 pieces (section 3, K03). [b14, b22]

### 2.3 Template theory (Gobet and Simon, 1996)

A template is a long-term chunk with a stable core and slots. The core is about a dozen pieces. Slots hold variable information (piece, square, opening, plan, move) with default values. Templates link to other templates. Costs in CHREST: build a new net node about 8 s; add to an existing chunk about 2 s; fill a slot about 250 ms (under 1 s in the verbal theory). [a13, a21, c09]

Predictions that were tested:

1. Recall of several boards rises with the pause between boards (slots can be filled and learning can occur). Confirmed: gain from 1 s to 10 s gap was +71% (2 boards) and +63% (4 boards) for Masters; +40% and +33% for Experts. [a11, b08]
2. Few large chunks, about 3, not 7 small ones. Partly confirmed on a computer display (section 3). [a23, b13]
3. A small skill effect on truly random positions (chance matches with a big store). Confirmed with slope 0.052 per rating point. [b17]
4. A pointer limit of 7 plus or minus 2 boards in short-term memory. The trained master plateaued near that. [a12]

The single-retrieval-structure alternative failed on four counts (location data, random positions predicted too well, one piece per square, too little interference). [a13]

### 2.4 Rival theories

- **SEEK / abstract schemas (Holding).** Chunks are abstract and location-free, perhaps 2,500 schemas. Mirror-image data and a CHREST simulation rejected the extreme version. [a16, b04]
- **Long-term working memory (Ericsson and Kintsch).** Predicts a very large edge on random boards and needs about 160 ms per piece for the square version. Judged too vague to give numbers. In a CHREST implementation recall ranged from 10 to 100% depending on parameters. [a29, c06]
- **Constraint attunement (Vicente and Wang 1998).** Skill is attunement to the domain's constraints. It predicts zero edge on truly random positions. Gobet and Waters (2003) found a small reliable edge. [b17]
- **Abstract roles (Linhares and Brum 2007).** Players see similarity between very different positions if pieces keep the same roles. Abstract only was read. [d21]

### 2.5 The pattern-recognition theory of search

Chase and Simon's "mind's eye": chunks activated by the board trigger potential moves, which go into short-term memory for further examination. Gobet's proposal (1998): patterns link to moves and to move sequences, making search more selective and deeper. Templates also carry evaluations that cut search. Links between templates act like macro-operators. This is stated as a hypothesis, not a result. [a08, a27]

The debate over how much is recognition and how much is search is not closed (section 5.4). [a28, d20]

### 2.6 Computer models

| Model | What it did | Source |
|---|---|---|
| MAPP (Simon and Gilmartin 1973) | Simulated a Class A player's recall | a07 |
| CHREST (Gobet 1993) | Net of chunks, short-term memory of pointers, eye fixations; nets of 630, 2175, 3646 nodes after 230, 1538, 2843 positions | a25, c10 |
| CHREST with templates (Gobet and Simon 2000; Gobet and Waters 2003) | Nets of 500 / 10,000 / 300,000 nodes fit Class A / Expert / Master recall; r2 = 0.889 over 20 human cells with no fitted parameters in the 2003 test | a21, c08 |
| CHREST in imagery test (Waters and Gobet 2008) | Out-of-sample test with pieces on square intersections | b16 |
| SEARCH (Gobet 1997) | With 150,000 chunks: moves generated 15% by heuristics, 23% by chunks, 62% by templates (model output) | d20 |
| CHUMP (Gobet and Jansen 1994) | Learned piece patterns and the moves that followed; proposals matched actual moves better after learning. No numbers found. | a32 (not opened) |

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, claims.jsonl), **S** single source, **C** contested. "Human" rows are chess players; "LLM" rows are language-model studies.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Expert recall depends on meaningful structure (1973 core result) | Master about 16 vs Class A about 8 vs beginner about 4 pieces, middle game, 5 s. On random boards all below beginner on real boards | Chase and Simon 1973 [a02, b01] | E (K01) |
| Edge on random boards is small but real, not zero | Strongest beat weakest in 12 of 13 comparisons. Masters 5.5 pieces vs 2.6 at 5 s. One piece per 400 Elo (random) vs about five (game) | Gobet and Simon 1996 review [a18, b05] | E (K01) |
| Cross-domain meta-analysis of random-material recall | r = .41 [.29,.51], k = 28, N = 903, I2 = 63%. After trim-and-fill (8 studies) r = .29 [.17,.41]. Experts better in 49 of 55 experiments. Domain Q(4) = 8.69, p = .069 (music r = .69); exposure time Q(1) = 0.89, p = .346 | Sala and Gobet 2017 [b19, b20, d03, d04] | E (K01, K18) |
| Skill slope on truly random positions | 0.052 per rating point (SE .016), p < .005; theory predicted 0.061. Game slope 0.35. 100 rating points = 5.2% = about 1.25 pieces. Random, 3/3 and 2/3 slopes not separable (F = 0.11, 0.25) | Gobet and Waters 2003 [b17, b18, c08] | C (K08) |
| CHREST with no fitted parameters predicts human cells | r2 = 0.889, RMSD 6.71 over 20 cells (4 skill groups x 5 position types); r2 = 0.885 without game positions | Gobet and Waters 2003 [c08] | S |
| Chunks found by a 2 s gap | Physical board: 95% of within-glance gaps below 2 s vs 42.6% of between-glance (means 0.64 s vs 2.43 s) | Gobet and Clarkson 2004 [a24] | E (K02) |
| Master chunks are mostly three families | 47 of 77 pawn chain; 27 same-colour cluster; 17 unclassified | Chase and Simon 1973 [a06] | S (one master) |
| Chunk size depends on display medium | Masters' median largest chunk: 14.8 (recall) and 12.9 (copy) on screen vs 7.5 and 3.8 on board. Chase and Simon master median 5; 1998 screen replication 16.8 | Gobet and Clarkson 2004; Gobet and Simon 1998 [a23, b14, b22] | E (K03) |
| Few large chunks | On screen fewer than 3 chunks recalled; 67% / 41% / 12% of copy chunks (view under 3 s) had 4+ pieces (Masters / Class B / novices). N = 12 | Gobet and Clarkson 2004 [a23, b15] | S (K06) |
| Chunk number does not rise with skill; size does | Masters 2.9 chunks (1 s), 4.2 (4 s), 3.3 (10 s); chunk number by skill ns at 10 s or less F(2,16) = 0.40; Experts' largest chunk 9 to 10 rising to about 17 at 60 s | Gobet and Simon 2000 [a20] | S |
| Original STM-only theory fails on interference | 6 to 8% loss after 30 s with distraction (Charness 1976) | [a14, b06] | E (K04) |
| Multi-board recall | Exp 1: 13 players; Masters up to 60 pieces, Experts about 40, Class A about 20 (up to 5 boards). Percentage falls (three Masters about 95% to 39% for 1 to 5 boards) | Gobet and Simon 1996 [a10, b09] | E (K04) |
| Pause between boards helps | Masters +71% (2 boards), +63% (4 boards) from 1 s to 10 s gap; Experts +40%, +33%. N = 5. At 10 s gap with 4 boards: Masters 82.9 pieces, Experts 44.9 | Gobet and Simon 1996 Exp 2 [a11, b08] | C (K05) |
| Capacity claims overread | De Groot guessing baseline 43.7%; five-board masters at 39% are near it. Cooke et al.: about 90% (1 board), about 50% (5), about 40% (9) | [b09, b29] | E on the caveat |
| Trained master reaches 9 boards | 150 sessions, cue list of world champions, peak 152 pieces, plateau about 123 per block | Gobet and Simon 1996 Exp 3 [a12, b10] | S (N = 1, an author) |
| Location is encoded | Mirror distortion costs about 10 points: normal+horizontal 77.3 / 49.7 / 34.5 vs vertical+central 62.9 / 38.6 / 27.5 (Masters / Experts / Class A, N = 25); simulation 11.4. Interaction F(6,66) = 2.41 | Gobet and Simon 1996 [a15, a16, b02] | E (K07), rivals alive |
| Game vs random chunk structure | Largest chunk, game 11.2 / 7.4 / 6.2 vs random 4.1 / 4.3 / 4.1. Game vs random F(1,22) = 291.51 | Gobet and Simon 1996 [a17, b03] | S |
| Speed of recognition | Masters at 1 s match Experts at 10 s; Masters saturate near 3 s; Class A keeps growing to 60 s. Game-position rate c: 2x (Experts), 15x (Masters) vs Class A; random-vs-game ratio about 25x for Masters | Gobet and Simon 2000 [a19, a22, b11] | S (K09) |
| Exact game recognition gives no recall gain | 83% vs 79% (one master, 4 positions) | [a03] | S (K19) |
| Search size does not rise with skill, selectivity does | N = 48. Nodes 58.0, 58.3, 56.8, 33.9 (ns). Base moves Masters 3.2 vs Class A 6.5 (F(3,44) = 2.94). Depth 5.0, 4.6, 3.7, 2.9 plies. Elo explains 29.2% of move quality | Gobet 1998 replication of de Groot [a26] | C (K10) |
| Speed pressure raises blunders modestly | Per 1,000 moves: 5.02 classical, 6.85 rapid, 7.63 blindfold. 6x less time gives +36.5% blunders. Kasparov simultaneous median 2682 Elo | Chabris and Hearst via Gobet 2003 [a28, d20] | C (K10) |
| Machine analogue: policy-only vs with search | Leela policy 2292 vs 2858 with 400 MCTS sims (+566); AlphaZero 1777 vs 2470 (+693). 270M transformer, no search: Lichess blitz 2895 vs humans, tournament 2299 vs bots; puzzles 95.4% | Ruoss et al. 2024 [c11, d19] | E (K13), contested use (K10) |
| Template sources in SEARCH | 62% of moves from templates, 23% chunks, 15% heuristics (150,000 chunks) | Gobet 1997 via d20 | S (K11), model output |
| Retrieved thought templates raise LLM accuracy | BoT (GPT-4): Game of 24 3.0 to 82.4; Checkmate-in-One 36.4 to 86.4; cost 12% of multi-query. DC: Claude AIME 2024 23.3 to 50.0 (DC-Cu); AWM: WebArena 35.5 vs 23.5 (+12.0) | [b25, c17, c19, c23] | E (K14), with caveats |
| Curated memory beats raw history | GPT-4o AIME 2024: baseline 20.0, full history 6.7, DC-RS 40.0. Claude: full history 26.7 vs 50.0 | Dynamic Cheatsheet [c20] | E (K15) |
| Self-written skills hurt | SkillsBench v4: self-generated -8.1 / -11.3 / -11.5 pp vs curated +18.2 / +19.7 / +24.8; earlier version -1.3. Skills never read in 10 of 12 audited trajectories | [d05, c26] | E (K15) |
| Admission by outcome check works | Strict check 70.95 vs add-all 55.48 vs fixed 67.53 (RegAgent). Randomized block curation 66.9 vs whole playbook 55.5 vs none 54.1 vs agent's own tags 53.8. No-gate 100% in-sample vs 66.7% test | [d08, d10, d11] | E (K20) |
| Retrieval accuracy is weak and separable from end gain | BM25 Recall@1 7.0 to 57.2; Recall@10 36.1 to 80.7. Oracle skill +16.6 pp (Llama-70B); top-1 injection captures about 30%, LLM selection about 70% | SRA-Bench [d12] | E (K21) |
| Same-task effect can be negative while aggregate lift is positive | Math500 Llama-70B +14.2 aggregate vs -39.4 same-task | Skill Following [d14] | S as one paper; part of E (K21) |
| Few items beat many | ReasoningBank: 0 items 39.0, 1 item 49.7, 2 46.5, 3 45.5, 4 44.4. SkillsBench: 1 skill +18.0, 2-3 +19.0, 4+ +10.1 pp | [d06, d15] | E (K23), not equal-token |
| Transfer gains are small and positive | ExpeL HotpotQA to FEVER 58 to 70; EvoSkill SealQA skill on BrowseComp 43.5 to 48.8; MSCE +2.56 to +5.13 (mean +3.93); ReasoningBank Mind2Web +4.6 / +2.2 / +4.7 | [c24, c25, d16, d18] | E (K16) |
| Abstract insights and concrete trajectories complement each other | HotpotQA insights-only 36 vs retrieval-only 31; ALFWorld 50 vs 55 | ExpeL [c24] | S (K17) |
| LLM quality falls with unfamiliarity | ACPL 4.75x higher near-distribution, 7.79x out-of-distribution. OOD illegal moves GPT-3.5 74.7%, GPT-4o 41.6%, GPT-5 33.8% | Pleiss et al. 2026 [c01, c02] | S (K12) |
| Thinking tokens pay less on unfamiliar positions | GPT-5: ACPL falls 85.3% (ND), 77.25% (WD), 64.69% (OOD); gain per 1,000 tokens 22.55% (WD), 7.23% (ND), 3.81% (OOD); tokens 3,426 / 11,800 / 16,953 | [c03, d01] | S (K12) |
| Slot-filled templates vs plain snippets | AWM abstracted 35.5 vs rule-based concrete 35.6 (WebArena); element accuracy 50.6 vs 49.5. SkillsBench low vs high abstraction +0.7 / -6.7 pp (CIs cross zero) | [d07, d17] | C (K22) |

## 4. Mechanisms and models

This section is written so that an engineer can build each part. Parameters come from the sources. Anything marked [D] is our design choice, not a measured value.

### 4.1 The chunk store (discrimination net)

CHREST stores chunks in a tree. Each node tests one feature (here: a piece on a square). A pattern is sorted from the root to the deepest node it matches. A node holds an "image": the chunk found so far. [a07, a25]

Learning rules (Gobet and Simon 2000):

- A test at a node costs about 10 ms. [a07]
- Learning a new node: about 8 s.
- Adding an element to an existing chunk (familiarisation): about 2 s.
- Filling a template slot: about 250 ms. [a21, c09]

Growth is slow. Redundant links grew from 4 after 100 positions to 20 after all positions. A small net is sparse and helps only on near-exact matches. [c10]

Implementation sketch for an agent: an index of past solved cases keyed on features of the problem. Each entry has a core (the stable part of the solution) and a list of slots. Lookup returns the deepest matching entry. Matching by a multi-feature condition, not a single feature.

### 4.2 Recall as a function of store size

- Recall = a + b log(nodes); the log fit explained over 98% of variance in one simulation. Random positions rose only to 23.4%. [a15]
- Nets of 500, 10,000 and 300,000 nodes were chosen to match Class A, Expert and Master recall. [a21]
- Net-size effect on recall (per position type, Waters and Gobet 2008): game 0.173, 1/3 randomised 0.092, 2/3 0.050, random 0.051, fully random 0.057. [b16]

Use: predicted curve for library-size sweeps. Expect slow, roughly logarithmic gain with library size in-distribution and a small, nearly flat gain off-distribution.

### 4.3 Template creation rule

A node becomes a template when: more than 3 nodes below it share the same piece, square or sub-chunk, and the base node has at least 5 elements. Slot types in CHREST: piece kind, location, chunk. Small nets rarely find templates even in game positions. [c09]

Agent version [D]: when 3 or more solved cases share a core step sequence and differ in some named values (numbers, names, entities), promote the shared part to a template and make the varying parts slots with defaults. Do not promote on fewer than 3 cases. Admission needs a held-out check (section 7).

### 4.4 Short-term memory as a pointer list

CHREST holds 3 visual chunks (pointers, not contents). With templates, each held board is one pointer into a template, plus filled slots. The limit of 7 plus or minus 2 boards comes from this. [a13, a21]

Agent version: the working context holds a short list of pointers to retrieved templates (3 to 4), with slots filled, rather than the full text of many past cases. Evidence for the cap is indirect (K23).

### 4.5 Retrieval structure plus templates

Experiment 3: a trained master used a prelearned cue list (names of world champions), one position per name, and reached 9 boards. Two layers: a deliberate index and the templates behind it. [a12] A hierarchy (digits, chunks, super-groups, clusters) allowed 106 digits in EPAM-IV. [c07]

Agent version: an explicit index of solved cases keyed by a short label, plus the case bodies. Voyager does a similar thing with description embeddings and top-5 retrieval. [c21]

### 4.6 Recognition proposes, search checks

The mind's eye loop. [a08]

1. Perceive the position; chunks fire.
2. Each fired chunk proposes candidate moves into short-term memory.
3. Selective search examines those candidates.
4. Choose.

Measured effect on the candidate set: Masters looked at 3.2 base moves vs 6.5 for Class A; first phase 1.1 vs 4.2 min. [a26]

CHUMP: store (pattern, following move) pairs in the net; at test time return the move linked to the recognised pattern. Reported to match actual moves better after learning; no numbers found. [a32]

Agent version: a table from problem pattern to operator or first candidate. Rank by past success. Return the top 3, not the top 1 (Voyager: top-1 80.2%, top-3 93.2%, top-5 96.5% retrieval success). [c21] Then code checks each candidate.

### 4.7 Cost model for the schema

From CHREST: lookup is cheap when the core matches (about 10 ms per test), slot fill is cheaper than learning a new chunk (250 ms vs 8 s), and learning a new chunk is slow. So the agent should:

- try cheap retrieval first;
- build a new template only after the problem is solved and checked (a post-hoc step, not part of the live solve);
- fall back to generic search when no multi-element match exists.

Boundary: singleton retrievals are mostly guesses (on screen 21 of 194 single pieces on random trials were placed singly, 6 correct, 28.6%). Require a multi-element match before using a retrieved pattern as a cue. [b15, a24]

## 5. What holds up

### 5.1 Replicated and robust

- **Real vs random.** Large expert edge for real positions; small for random. Found in Gobet's group, Chase and Simon, Saariluoma, Cooke, and in the cross-domain meta-analysis. The shape (large in-structure, small off-structure) is robust. [K01]
- **Fast LTM access.** Interference barely hurts recall (Charness 6 to 8%), so storage cannot be short-term only. Cooke et al. independently replicated that more boards give more pieces but a lower percentage. [K04]
- **Chunk boundary by gap.** Holds on physical boards (95% vs 42.6%). Absolute size depends on the instrument. [K02, K03]
- **Expert edge in other domains.** Go, gomoku, bridge, music, circuits, programs, basketball. High heterogeneity (I2 63%). [K18]
- **Admission by outcome check.** Four independent LLM studies agree: strict or held-out checks keep memory useful; self-judgment and add-all do not. [K20]
- **Curated beats raw.** Five sources. [K15]

### 5.2 Corrections and failures

- **"Zero edge on random boards" is wrong.** It came from three subjects. After bias correction r = .29 survives. [K01]
- **Chunk size 5 and 7 chunks are not stable.** Master median largest chunk was 5 in 1973, 16.8 on screen in 1998, 14.8 on screen vs 7.5 on board in 2004. Part is a hand-movement artifact. [K03]
- **Exposure time moderator.** Gobet and Simon 2000 found the skill effect grows with time on random positions; the meta-analysis found no exposure-time effect (Q(1) = 0.89). Do not build a rule that longer thinking helps experts more. [K25]
- **Multi-board capacity.** Part of the apparent capacity is what guessing from a typical master position gives (43.7%). [b09]
- **Mirror-image result.** About 10 points of loss, matching a simulation (11.4). But hybrid positions with real locations are recalled nearly as well as game positions (Saariluoma, second-hand) and an abstract-roles rival exists. [K07]
- **Template vs constraint attunement.** The graded prediction was only weakly separated: the fully-random slope (0.052) is not significantly different from the two-thirds slope (0.063). Only "game vs everything else" is cleanly supported. [K08]
- **Capacity of the self-trained master.** N = 1 and an author. [a12]

### 5.3 Moderators

- Display medium: screen vs physical board changes chunk size about 2x.
- Domain: music r = .69 outlier; sports and other include zero.
- Randomness: effect size is inversely related to how random the material is. [d04]
- Viewing time in copy tasks: with views over 3 s, chunk size correlates with viewing time (r = .71 Masters); not under 3 s. So long copy views inflate chunks by learning. [b14]
- Net size: matters more for game positions than random ones (0.173 vs 0.051). [b16]

### 5.4 Search vs recognition: not settled

- For recognition: no search-size effect with skill; selectivity and depth do; Kasparov's simultaneous play median 2682; policy-only networks reach 2292 (Leela) or 2299 (transformer) tournament Elo. [a26, d19]
- For search: blunders rise with time pressure (5.02 to 6.85 to 7.63 per 1,000); search adds 566 to 693 Elo to the same policy networks. [d19, d20]
- Both sides agree both matter. Gobet reads +36.5% blunders for 6x less time as modest. The original Chabris and Hearst paper was not opened. [K10]

### 5.5 Interventions that worked and did not (LLM agents)

| Intervention | Result | Source |
|---|---|---|
| Curated skills | +16.6 pp average (SkillsBench v4); range +4.1 to +25.7 | [d05] |
| Self-generated skills | -8.1 to -11.5 pp vs none | [d05] |
| Strict held-out gate (RSEA) | Never significantly worse than ReAct; ALFWorld 69.3 vs 64.6 (p = 0.015) | [d10] |
| No gate (DC on WebShop) | 0.136 vs 0.429 plain ReAct | [d10] |
| Random-inclusion block curation | 66.9 vs 55.5 whole vs 54.1 none | [d11] |
| Agent's own helpful/harmful tags | 53.8, no better than none; one lesson tagged helpful 123 times, harmful 0 times lowered success | [d11] |
| Token budget for playbook | 40% beat 20% and 60% | [d11] |
| Add-all memory | 4 to 12 points below fixed memory in four agents | [d08] |
| Delete by reuse count and utility (retrieved at least 5 times, mean utility below 0.3 coarse or 0.7 strict) | Helps when judge is reliable; hurt AgentDriver with a GPT-4o-mini judge | [d09] |
| Fewer items | 1 item 49.7 vs 4 items 44.4 | [d15] |
| Longer skills | compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 pp | [d06] |
| Skills hurt on 13 of 87 tasks (largest -7.4 pp) | A single heavy pipeline with no fallback | [d06] |
| Training on 12 to 36 examples (EvoSkill) | 63.4, 65.8, 64.5; plateau after 10% | [c25] |
| Online induction under shift (AWM) | Offline-vs-online gap widens with domain gap | [d17] |

## 6. Language models

### 6.1 How LLMs behave on chess-like pattern tasks

- **Quality tracks familiarity.** ACPL is 4.75x higher near-distribution and 7.79x higher out-of-distribution. Generation-to-generation progress slows most where patterns are scarce: ACPL improvement GPT-3.5 to GPT-4o is 70.7% (WD), 35.16% (ND), 9.08% (OOD); GPT-4o to GPT-5 is 69.92%, 10.77%, 5.73%. [c01, c04]
- **Rule-following fails off-distribution.** OOD illegal-move rates: GPT-3.5 74.7%, GPT-4o 41.6%, GPT-5 33.8%. Claude Opus 0.2% / 8.2% / 51.6% illegal (WD / ND / OOD, with 14.4% syntactically invalid output overall). Gemini 2.2% / 17.0% / 72.0%. GPT-5 with moderate reasoning is still above 10% illegal OOD at about 5x the reasoning tokens. [c02, d02]
- **More thinking helps, less per token when priors are scarce.** GPT-5 relative gain per 1,000 reasoning tokens: 22.55% (WD), 7.23% (ND), 3.81% (OOD). Caveat: OOD uses 5x more tokens, so the per-token figure is partly an artifact; the total drop is not monotone (ND 85.3% > WD 77.25% > OOD 64.69%). Authors state association, not cause. No retrieval arm, no replication. [d01, d02]
- **Trained-from-scratch models build a world model.** Karvonen: board probe 99.6% (16-layer) and 99.1% (8-layer) vs 74.7% and 75.0% for random-weight baselines; skill probe 90.5% vs 69.3%; legal-move rate 99.8% and 99.6%; win rate vs Stockfish level 0 of 46% (8-layer) and 64% (16-layer). After 20 random opening moves the model reads the game as low skill and plays worse; a skill-vector intervention raises win rate 2x (8-layer) and 2.6x (16-layer). The model infers its regime from the input. [b24, c13]
- **Pattern memory can replace search inside the training distribution.** A 270M transformer with no search reaches Lichess blitz Elo 2895 vs humans (2299 vs bots); puzzle accuracy 95.4% (270M), 94.5% (136M), 88.9% (9M); GPT-3.5-turbo-instruct 66.5%; under 1.41% of puzzle boards overlap training. [c11, c12]
- **State tracking.** ChessGPT-Base BIG-bench tracking: real 99.5 / 97.7 / 98.1 vs synthetic 94.2 / 94.6 / 92.8; LLaMA-7B real 29.5 / 39.3 / 53.0, synthetic 31.3 / 39.9 / 45.8. Toshniwal: legal-move accuracy over 97%; explicit board-state tokens help most with small data. [c14, c15]
- **Literature gap.** In a map of 84 study families, candidate generation is among the least studied stages (12 of 84). No study found tests pattern-cued candidate moves in LLMs. [c16]

### 6.2 Retrieved templates and memories: what changed accuracy

| System | Task | Plain | With memory | Note |
|---|---|---|---|---|
| Buffer of Thoughts (GPT-4) | Game of 24 | 3.0 | 82.4 | ToT 74.0 |
| | Checkmate-in-One | 36.4 | 86.4 | meta prompting 57.2 |
| | Geometric Shapes | 52.6 | 93.6 | |
| | Python Puzzles | 31.1 | 52.4 | |
| | Sonnet Writing | 79.6 (near tie) | 80.0 | creativity: gain limited |
| Dynamic Cheatsheet (GPT-4o) | Game of 24 | 10 | 99 (DC-RS) | one reused Python solver |
| Dynamic Cheatsheet (Claude) | AIME 2024 | 23.3 | 50.0 (DC-Cu) | 30 questions; 1 question = 3.3 points |
| | AIME 2025 | 6.7 | 36.7 | |
| | GPQA-Diamond | 59.6 | 68.7 | GPT-4o 57.1 to 58.1 |
| Agent Workflow Memory | WebArena | 23.5 | 35.5 | +12.0, 51.1% relative |
| Voyager | Minecraft tech tree | 1x | 3.3x items, wooden 15.3x faster | no skill library: plateau late |
| EvoSkill (Opus 4.5) | OfficeQA | 60.6 | 67.9 | |
| | SealQA | 26.6 | 38.7 | |
| ReasonFlux (trained 32B, 500 templates) | MATH | - | 91.2 | trained, not scaffold only |

BoT cost: about 12% of multi-query methods. ReasoningBank: about +4.3% total tokens for +20.5% performance vs no memory. [b25, c17, c19, c21, c23, c25, c27, d15]

Reading the table with care:

- The Game of 24 jumps come from discovering and reusing a Python solver. They measure code reuse, not pattern cueing. [critique]
- BoT's templates come from the same task families as the test, so train-test overlap is close; no test on unseen task families. [c17]
- None of these papers scores whether the retrieved template was the right one or splits the gain into "right template cued" and "extra reasoning from the template". [d22, K21]
- No equal-token comparison is established by any source seen. [critique]

### 6.3 Retrieval quality and use

- SRA-Bench: 5,400 test instances, 636 gold skills hidden among 26,262, six datasets. BM25 Recall@1 / Recall@10: TheoremQA 57.2 / 80.7; LogicBench 12.0 / 36.1; ToolQA 7.0 / 55.1; CHAMP 13.2 / 36.1; MedCalc 29.3 / 69.2; BigCodeBench 23.6 / 61.1. [d12]
- Average accuracy, direct / oracle / top-1 full injection / LLM selection: Llama-3.3-70B 47.8 / 64.4 / 52.7 / 59.2; Llama-3.1-8B 29.8 / 44.5 / 32.7 / 37.0; Qwen3-4B 38.8 / 61.6 / 45.5 / 53.3. [d12]
- Models load skills whether or not a good one exists. Load rate with gold in BM25 top-50 vs not: GPT-5.4 36.6% vs 3.6%; GLM-5.1 43.5% vs 8.2%; Qwen3-235B 57.8% vs 35.3%; Llama-8B 73.7% vs 64.1%; Llama-70B 10.4% vs 14.5% (wrong direction). [d13]
- Full-skill injection helps at small k then falls (inter-skill interference). Progressive disclosure (names first) stays stable. [d13]
- Skill Following (17 LLMs): aggregate retrieval lift can be positive while the same-task effect is negative (Math500 Llama-70B +14.2 vs -39.4; Gemini-2.5-Flash-lite +13.2 vs -11.0). Negative effect stayed with normal, random, corrupted and filler returned content. [d14]

### 6.4 Self-written memory

Curated skills help. Self-written skills hurt: SkillsBench v4 -8.1 (Claude Code + Opus 4.7, 43.0 to 34.9), -11.3 (Codex + GPT-5.5, 46.8 to 35.5), -11.5 (Gemini CLI + Gemini 3.1 Pro, 36.0 to 24.5). Reasons: skills never read (10 of 12 Codex/Gemini trajectories), authoring displaces solving, confident wrong assumptions become load-bearing (a unit conversion off by three orders of magnitude). [d05]

A playbook can fall up to 69.6 points below no playbook. The agent's own tags did not pick good lessons. [d11]

### 6.5 Transfer by distance

| Test | Numbers | Source |
|---|---|---|
| ExpeL HotpotQA to FEVER | ReAct 58; transfer without task demos 63; with 70 | [c24] |
| EvoSkill SealQA to BrowseComp | 43.5 to 48.8 | [c25] |
| MSCE six cross-domain pairs | +2.56 to +5.13, mean +3.93 | [d18] |
| ReasoningBank Mind2Web step success (cross-task / website / domain) | 40.3 / 31.7 / 31.9 to 44.9 / 33.9 / 36.6 | [d16] |
| AWM offline, step success | 45.1 / 33.7 / 32.6 vs MindAct 36.2 / 30.1 / 18.6 | [c23, d17] |
| AWM element accuracy at the same levels | 46.3 / 39.1 / 33.3, below no-memory at website and domain | [d16] |

Gains are small and do not fall off a cliff over three coarse levels. All tests are among agent-task neighbours. There is no chess-to-maths test and no similarity-measured curve. [K16]

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. Status marks as in SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Admit a stored template only on an outcome check on cases it was not written from.** A held-out gate (keep-better), not model self-grading and not add-all. | memory (lessons and future subgoal library); links to G3 | [E] | K20, K15; d05, d08, d10, d11 |
| A2 | **Never let the agent write a skill or lesson and trust it unchecked.** Self-written memory is neutral to harmful (-8.1 to -11.5 pp; add-all 4 to 12 points below fixed). Keep the existing rule "a lesson becomes trusted only after it helps on two different problems", and make the check an outcome test. | memory | [E] | K15, K20 |
| A3 | **Curate, do not dump history.** Cap the memory block and keep each item compact. Full history fell to 6.7% on GPT-4o AIME 2024 vs 20.0% baseline. | memory | [E] | K15; c20 |
| A4 | **Cap retrieved items at about 3, each compact.** Gain peaks at 1 to 3 items and falls at 4 or more. (Not an equal-token result; treat the number as a default, not a law.) | memory, S3 | [E] on direction; the "3 rich vs 8 small" claim is untested | K23; d06, d15 |
| A5 | **Log retrieval and use separately.** Per problem: was a template retrieved, was it the right one (oracle label offline), was it read and used, did the answer change. Report same-problem paired effects (memory on vs off), not retrieved-vs-skipped averages. | section 6 logging | [E] | K21; d12, d14 |
| A6 | **Matched-structure fallback.** When no multi-element match is found, do not force a template. Go to generic generation (S3 normal path). | S0 / S3 | [E] (the control; retrieved singletons are mostly guesses) | K01, K07; a17, b15 |
| A7 | **Keep the check after the cue.** A retrieved template proposes; code verifies (G3). Legality or constraint checks stay on in unfamiliar states, because extra thinking does not remove illegal outputs (above 10% OOD at 5x tokens). | G3, S4 | [E] for the structure (recognition proposes, check disposes); the OOD rate is [S] | K10, K13; a08, d02 |
| A8 | **Retire by reuse count and reuse success.** Delete a template that was retrieved at least n times (n = 5 in the source) and whose mean utility is low, only if the utility signal is reliable. | memory | [E] with a reliability condition | K20; d09 |
| A9 | **Offer several cued candidates, not one.** Retrieval top-1 80.2% vs top-3 93.2% vs top-5 96.5% (Voyager). Pass 3 candidates to the test step. | S3 to S4 | [S] (one system, description similarity) but consistent with SRA-Bench | c21, d12 |
| A10 | **Do not claim templates beat plain notes.** Treat "core plus slots" as untested. | process rule | [E] (K22 shows no win) | d07, d17 |

### Test first

| # | Item | Part | Status | Evidence | Why test first |
|---|---|---|---|---|---|
| T1 | Core-plus-slots template vs flat solved example vs plain snippet at equal retrieved tokens | memory | [C] | K05, K22; a13, d07, d17 | Only direct analogue of template theory; nobody has tested typed slots |
| T2 | Cap of 3 rich items vs 7-8 small items at equal tokens | memory, S3 | [S] | K06, K23 | All existing evidence grows tokens with k |
| T3 | Hit rate of the correct operator or template in the top 3 cues; split of gain into "right template cued" vs "extra reasoning" | O (S6), memory | [S] | K11, K21 | No published split for BoT or DC |
| T4 | Pattern-to-operator table at S6: past (problem pattern, operator that solved a subgoal) pairs ranked for the impasse | O1-O8 / S6 | [S] | K10, K11; a08, a27 | The "pattern cues candidate" link is thin even in chess |
| T5 | Abstract-role retrieval key vs surface key under surface changes | memory | [C] | K07, K26; b02, d21, d16 | Humans conflict; LLM evidence is indirect |
| T6 | Familiar vs unfamiliar split: log gain per 1,000 thinking tokens on each; add retrieval-on arm | G11, G12, S0 | [S] | K12; d01 | Single paper, one model, no retrieval arm |
| T7 | Tell the agent the regime ("familiar" or "unusual") and switch to checked search on unusual | S0 | [S] | K12, K13; c13 | Karvonen's skill-vector effect is a model-internal result |
| T8 | Transfer vs distance curve from family A to B | memory | [E] on small positive gains; the curve is unmeasured | K16 | Need a distance measure |
| T9 | Search-off arm: first candidate from retrieval only, vs retrieval then checked lookahead | S3/S4, O | [C] | K10; d19 | Settles how much the check adds |
| T10 | Rule + one worked example per template vs rule only vs example only, by task type | memory | [S] | K17 | One paper (ExpeL) |
| T11 | Template-building as a post-solve step (3 or more similar solved cases promote a template) vs live building | memory, S9 | [D] | a13, c09 | Design from CHREST's rule, no LLM test |

## 8. Concrete tests on our bench

All tests: two or more arms at equal total tokens (retrieval, memory block, reasoning and checks all counted, setup cost included, G7). Paired by problem. Report downside against the plain agent. Use the existing bench (ARC and BRAINTEASER items, plus NoveltyBench where relevant).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Stream of 60 to 100 problems with about 30% repeated structure (same solution skeleton, changed values), ARC-style transformations and brainteasers | (a) no memory, (b) raw history of solved cases, (c) curated templates admitted by held-out gate, (d) templates admitted by model self-grade | Accuracy; downside (problems where memory arm loses to plain); tokens | (c) above (a) on repeat-structure items; (b) and (d) at or below (a). Based on K15, K20; expect +3 to +10 points for (c), but this is a guess [D] |
| B2 | Same stream; split into repeat-structure and structure-shuffled items | memory on vs off | Gain on each split | Large gain on repeat items, small residual on shuffled (K01 predicts a small gain, about a third to half of the in-structure one by analogy to slopes 0.052 vs 0.35; [D]) |
| B3 | Repeat-structure items with surface changes (renamed objects, reordered examples, changed numbers) | (a) flat solved example, (b) plain snippet, (c) core plus typed slots; equal retrieved tokens | Accuracy on changed-surface items; retrieval hit rate | (c) at least equal to (a) and (b); the AWM result suggests the gap will be 0 to 3 points, so the test needs enough items (at least 100 paired) to see it |
| B4 | Same items | retrieval key: (a) surface text, (b) abstract role description written by the model, (c) both | Top-3 hit rate on surface-changed items; accuracy | (b) or (c) above (a) after surface change; mirrors Linhares vs Gobet and Simon |
| B5 | Items with a known correct template (label offline) | arms: oracle template, retrieved top-1, retrieved top-3, none | Top-3 hit rate; accuracy; gain captured vs oracle | Oracle gain upper bound; expect retrieval to capture 30 to 70% of it (SRA-Bench range) |
| B6 | Same items | memory on vs memory off, only on problems where retrieval fired | Paired same-problem effect | Compare with the aggregate lift; a negative paired effect with positive aggregate means the gain is selection (Skill Following) |
| B7 | Items at 3 difficulty tiers set by plain pass rate (high / mid / low) | plain, plain + 2x thinking, template + plain, template + 2x thinking | Accuracy; gain per 1,000 thinking tokens by tier | Thinking gain per token falls on the low-familiarity tier (d01: 22.55% to 3.81%); template may restore it (untested) |
| B8 | Retrieval top-k sweep at a fixed 1,500-token memory budget [D] | k = 1 rich, 3 medium, 8 small | Accuracy; hit rate; tokens used | Peak at k = 1 to 3 (K23); if 8 small matches 3 rich, the cap is not worth keeping |
| B9 | Impasse items (S6 reached) | operator chosen by (a) free model choice, (b) table of past (pattern, operator) pairs, top-3 offered to the model, (c) random unused operator | Subgoal solved rate; operators tried per problem | (b) above (c); (b) vs (a) unknown; log which operator solved which class (already planned in S9) |
| B10 | Unfamiliar items (shuffled structure) | (a) trust first candidate, (b) first candidate plus code check, (c) template cue plus code check | Illegal or failed-check rate; accuracy | (b) and (c) lower failure than (a); mirrors d02 (illegal moves persist under longer thinking) |
| B11 | Memory growth | library size 0, 5, 20, 80 admitted templates | Accuracy vs log(size) | Slow gain roughly in log(size) in-distribution (CHREST fit, a15); flat or negative past some size (c20); find the peak |
| B12 | Retired vs kept templates | with and without a retire rule (retrieved at least 5 times, mean utility below threshold) | Accuracy after 100 problems; memory size | Equal or better accuracy with a smaller memory (d09) |

## 9. What does not transfer, and why

- **Perceptual chunks to text.** CHREST chunks are piece-on-square patterns found in parallel by the eye. An LLM reads text in sequence. The 2 s gap, the 3-chunk visual store and the hand-movement artifact have no direct agent counterpart. [K02, K03]
- **Chunk counts and sizes as design constants.** Seven chunks, four chunks, three chunks: all depend on the instrument and the 2 s rule. Do not hard-code a working-memory size from chess. [b13, a23]
- **Training time and expertise growth.** Ten years of practice, 50,000 chunks, 150 sessions: the agent has no persistent weights. Our memory is a retrieved text store, so the "learning" is admission and retrieval, not consolidation.
- **Slots as perceptual variables.** Template slots in CHREST are typed (piece kind, location, chunk) and filled by the eye in 250 ms. In BoT, DC and AWM a template is a retrieved instruction or code block with named variables. The analogy is by function, not mechanism. No direct LLM test of slots exists. [critique]
- **Recall as the dependent variable.** The chess results measure recall and reconstruction of positions. What we need is a better first candidate and a better final answer. Very few chess results (de Groot, Gobet 1998) measure move choice, and LLM memory papers report final accuracy only. [critique]
- **Human independence of evidence.** Nearly all human data come from Gobet's group (plus Chase, Simon, Saariluoma, Cooke). Samples are small (3, 5, 12, 13, 20, 25, 36). Many multi-experiment numbers are model fits tuned to the same data. [critique]
- **Gains on code-reuse tasks.** The Game of 24 jump (10% to 99%) came from a reused Python solver. It says memory of a script works when a script solves the class; it does not say pattern cues help reasoning. [critique]
- **Human robustness to novelty.** Humans keep applying fixed rules when patterns fail (speed fell, accuracy did not; error rates below 1% for both groups with unfamiliar notation, second-hand). LLMs lose legality. This means the code-side check matters more for LLMs than the chess analogy implies. [c05, d02]
- **Direct training effects.** A transformer reaching 2895 Elo from 15 billion labelled examples shows pattern knowledge can replace search, but only with training. A training-free agent cannot copy that mechanism. [c11]
- **Creative tasks.** BoT reports limited gain on tasks needing human-like creativity (Sonnet Writing 79.6 vs 80.0). Templates are a poor fit for open mode (G8 and S3 open mode); keep them for routine and checked modes, as G12 and O7's note on analogues already imply. [b25, b26]

## 10. Open questions

1. Does a slot-filled template beat a flat solved example or plain snippet at equal retrieved tokens? Nearest data: AWM abstracted vs rule-based 35.5 vs 35.6; SkillsBench granularity CIs crossing zero. No typed-slot test. [K22]
2. How much of the BoT and DC gains come from the right template being cued, and how much from the extra reasoning it triggers? No oracle-template arm exists. [K21]
3. Is the 3-to-4 item cap with rich items better than 7-8 small items at equal tokens? [K23, K06]
4. How far does template transfer reach? All tests are on agent-task neighbours. No far-domain curve. [K16]
5. Does retrieval restore the thinking-token gain on unfamiliar problems (Pleiss et al.)? Needs a replication and a retrieval arm. [K12]
6. Does a CHUMP-style pattern-to-move table give a measured held-out hit rate? No numbers found for CHUMP in anything opened. [K11]
7. Are abstract role keys better than surface keys for LLM memory? The Linhares and Brum full text was not available. [K26]
8. How should the search-vs-recognition split be measured with a search-off arm? The original Chabris and Hearst paper was not opened. [K10]
9. What is the right admission rule when no ground-truth outcome exists? Strict ground-truth checks gave the best results (RegAgent strict 70.95), but our agent often has no such check; held-out agreement is weaker. [d08]
10. How does the effect of memory scale with library size in a training-free agent? CHREST predicts logarithmic gain; no LLM sweep exists beyond ReasonFlux's 500 templates (trained). [a15, c27]
11. Does expert recall edge on random material come mostly from chance matches with a large store (template/chunk account) or from constraint attunement? Not settled (K08).
12. Do templates formed by the model itself from several solved cases (promotion rule) outperform templates written once from one case? No data.

## 11. Sources

**[V]** opened and read (text or PDF); **[M]** snippet, abstract page or second-hand only. Evidence ids in brackets.

### Human chess and expertise

- [V] Chase and Simon (1973) Perception in chess. https://www.gwern.net/doc/psychology/chess/1973-chase.pdf [a01-a06, b01]
- [V] Gobet and Simon (1996) Templates in chess memory: a mechanism for recalling several boards. https://bura.brunel.ac.uk/bitstream/2438/1339/1/Multiple_boards.pdf and https://www.Gwern.net/doc/psychology/chess/1996-gobet.pdf [a09-a14, b08-b10]
- [V] Gobet and Simon (1996) Recall of random and distorted chess positions: implications for the theory of expertise. https://bura.brunel.ac.uk/bitstream/2438/1345/1/Mirror_image.pdf [a15-a17, b02-b04]
- [V] Gobet and Simon (1996) Recall of rapidly presented random chess positions is a function of skill. https://bura.brunel.ac.uk/handle/2438/1346 [a18]
- [V] Gobet and Simon (2000) Five seconds or sixty? Presentation time in expert memory. https://bura.brunel.ac.uk/bitstream/2438/811/1/Five%20Seconds%20or%20Sixty%20.pdf [a19-a22, b11, b12]
- [V] Gobet and Clarkson (2004) Chunks in expert memory: evidence for the magical number four... or is it two? https://bura.brunel.ac.uk/bitstream/2438/801/1/GobetClarkson.pdf [a23, a24, b13-b15, b23]
- [V] Gobet and Waters (2003) The role of constraints in expert memory. https://bura.brunel.ac.uk/bitstream/2438/803/1/GobetWatersChessMemoryJEPLMC-R2.pdf [b17, b18, c08, c09]
- [V] Gobet (1998) Expert memory: a comparison of four theories. https://bura.brunel.ac.uk/handle/2438/1343 [a07, a08, a29, a34, b05-b07]
- [V] Gobet (1998) Chess players' thinking revisited. https://bura.brunel.ac.uk/bitstream/2438/822/4/1791.pdf [a26, a27]
- [V] Gobet (2003) Forward search, pattern recognition and visualization in expert chess: a reply to Chabris and Hearst. https://bura.brunel.ac.uk/bitstream/2438/1391/1/Chabris_Hearst_Reply.pdf [a28, d20]
- [V] Gobet (1993) A computer model of chess memory. https://bura.brunel.ac.uk/bitstream/2438/2129/1/cogsci-1993.pdf [a25, c10]
- [V] Waters and Gobet (2008) Mental imagery and chunks: empirical and computational findings. https://bura.brunel.ac.uk/bitstream/2438/1618/1/Mental%20imagery%20and%20chunks.pdf [b16]
- [V] Gobet, Lane and Lloyd-Kelly (2015) Chunks, schemata, and retrieval structures: past and current computational models. https://pmc.ncbi.nlm.nih.gov/articles/PMC4657374/ [c06, c07]
- [V] Sala and Gobet (2017) Experts' memory superiority for domain-specific random material generalizes across fields of expertise: a meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC5323477 [b19, b20 were first seen as page summary; full text read later in d03, d04]
- [M] Linhares and Brum (2007) Understanding our understanding of strategic scenarios: what role do chunks play? https://doi.org/10.1080/03640210701703725 (abstract only; publisher page 403) [b21, d21]
- [M] Saariluoma (1991, 1994) dictation and quadrant experiments, as reported in Gobet (1998) and Gobet and Simon (1996). https://bura.brunel.ac.uk/handle/2438/1343 [a30, a31, b30]
- [M] Gobet and Jansen (1994) CHUMP; Chess Programming Wiki summary. https://www.chessprogramming.org/CHUMP [a32]
- [M] Gobet and Simon (1996) Roles of recognition processes and look-ahead search in time-constrained expert problem solving (Kasparov simultaneous games). https://bura.brunel.ac.uk/handle/2438/1338 [a33]
- [M] Gobet and Simon (1998) Expert chess memory: revisiting the chunking hypothesis, via Gobet and Clarkson (2004) [b22]
- [M] Cooke et al. (1993) nine-board recall, via Gobet and Simon (1996) [b29]
- [M] Reingold and Sheridan (2023) double-check detection, via Pleiss et al. [c05]
- [M] Chabris and Hearst (2003), via Gobet (2003); original PDF not retrievable [a28, d20]
- [M] Cross-domain studies (Reitman, Eisenstadt and Kareev, Engle and Bukstel, Charness, Sloboda, Egan and Schwartz, McKeithen, Allard) as listed in Gobet (1998) [a34]

### Language models and agents

- [V] Pleiss, Schiffer and von Weizsaecker (2026) Disentangling generalization and memorization in large language models using chess. https://arxiv.org/abs/2601.16823 [c01-c04, d01, d02]
- [V] Ruoss et al. (2024) Amortized planning with large-scale transformers: a case study on chess. https://arxiv.org/abs/2402.04494 [c11, c12, d19]
- [V] Karvonen (2024) Emergent world models and latent variable estimation in chess-playing language models. https://arxiv.org/abs/2403.15498 [b24, c13]
- [V] Toshniwal et al. (2022) Chess as a testbed for language model state tracking. https://arxiv.org/abs/2102.13249 [c14]
- [V] Zhu et al. (2023) ChessGPT: bridging policy learning and language modeling. https://arxiv.org/abs/2306.09200 [c15]
- [V] Ciancarini and Pareschi (2026) What counts as strategic reasoning? https://arxiv.org/abs/2609.18286 [b27, c16]
- [M] Schut et al. (2023/2025) Bridging the human-AI knowledge gap: concept discovery and transfer in AlphaZero. https://arxiv.org/abs/2310.16410 [b28] (abstract page only)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 [b25, b26, c17, c18, d22]
- [V] Suzgun et al. (2025) Dynamic Cheatsheet: test-time learning with adaptive memory. https://arxiv.org/abs/2504.07952 [c19, c20]
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 [c21, c22]
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 [c23, d17]
- [V] Zhao et al. (2024) ExpeL: LLM agents are experiential learners. https://arxiv.org/abs/2308.10144 [c24]
- [V] Provenzano et al. (2026) EvoSkill. https://arxiv.org/abs/2603.02766 [c25]
- [V] SoK: Agentic skills beyond tool use in LLM agents (2026). https://arxiv.org/abs/2602.20867 [c26] (SkillsBench figures second-hand there; later read directly in d05)
- [V] Yang et al. (2025) ReasonFlux. https://arxiv.org/abs/2502.06772 [c27] (abstract and top results table)
- [V] Li et al. (2026) SkillsBench v4. https://arxiv.org/abs/2602.12670 [d05, d06]
- [V] Xu and Wu (2026) Skill availability and presentation granularity: a controlled SkillsBench study. https://arxiv.org/abs/2605.31408 [d07]
- [V] How memory management impacts LLM agents: experience-following behavior (2025). https://arxiv.org/abs/2505.16067 [d08, d09]
- [V] Nguyen, Nguyen and Vuong (2026) Recursive self-evolving agents via held-out selection (RSEA). https://arxiv.org/abs/2606.28374 [d10]
- [V] Pham et al. (2026) Reliable memory from unstable growth (RBC). https://arxiv.org/abs/2610.18427 [d11]
- [V] SRA-Bench (2026) Skill retrieval augmentation for agentic AI. https://arxiv.org/abs/2604.24594 [d12, d13]
- [V] Skill Following (2026) Retrieval-invoked actual-use effect. https://arxiv.org/abs/2609.00549 [d14]
- [V] ReasoningBank (2025) Scaling agent self-evolving with reasoning memory. https://arxiv.org/abs/2509.25140 [d15, d16]
- [V] Tang et al. (2026) From memory to skills (MSCE). https://arxiv.org/abs/2607.16621 [d18]

### Notes on source status

- The Pleiss et al. paper could not be re-found after the reopening in the gap pass; its numbers were confirmed against the paper and no replication exists.
- Several tables were garbled in PDF extraction (Gobet and Waters slopes; ExpeL rows; SkillsBench rows). Deltas were taken from the text, not the table rows (critique.md items 1 to 5).
