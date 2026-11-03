# Computational chunk models: deep document

*Subfield E16.04. Sources: evidence_a-d.jsonl (ids a01-a26, b01-b27, c01-c27, d01-d18), claims.jsonl (K01-K27), critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. The writer did no new search; numbers are those recorded by the research agents and the 2026-11-03 cross-check.*

## 1. What it is

Computational chunk models are programs that learn a store of small recognised patterns ("chunks") and use it to explain expert memory and expert choice. The main family is EPAM (Feigenbaum and Simon, from the late 1950s), MAPP (Simon and Gilmartin 1973, the first chess recall program), and CHREST (Gobet 1993 onward). A newer member is CogAct (Bennett and Gobet 2025).

The core idea in plain words:
- Memory is a net of tests. Sorting a new input down the net ends at a node: a chunk.
- Learning has two steps. Discrimination adds a test and a node when two things differ. Familiarisation adds detail to an existing chunk.
- Working memory is tiny (about 3 visual chunks in CHREST). But each chunk can stand for many items, so a rich long-term store lets an expert hold a lot in a few slots.
- Big chunks can grow into templates: a stable core plus slots that fill fast.
- The same store also speeds recognition and shortens search (SEARCH model).

Why it matters for our agent: it is the best-tested theory of how a bounded working set plus a large store of reusable units produces expert-level performance. That is a memory design question: what unit to store, how to index it, how big to make the working set, and what a new unit costs against filling a slot. The evidence is human and simulation. The LLM evidence is indirect (section 6). No study found tests chunk theory on an LLM (K22).

## 2. History and theories in depth

**Before the models.** De Groot showed masters recall about 93% of a 25-piece game position seen for 5 s, experts about 72%, Class A about half, novices about 8 pieces (a04). Miller's 7 plus or minus 2 (1956) set the idea of chunks as units of memory.

**Chase and Simon 1973 (a01-a03).** Three players (master, Class A, beginner) did a copy task and a 5 s recall task. A pause of over 2 s between placed pieces was taken as a chunk boundary. Pieces inside a chunk shared many more chess relations (attack, defence, colour, type, proximity) than pieces across a boundary. Over 75% of the master's 77 chunks of two or more pieces were castled king, pawn chains or other familiar clusters. Claims: chunks grow with skill; the number of chunks stays inside the 7 plus or minus 2 span; on random positions skill gives no edge; a master needs about 50,000 chunks (argument: P^7 must exceed the number of possible positions, so P = 50,000 gives about 8x10^32). Simon and Chase's popular account (a04) also described MAPP: with about 1,000 patterns it played recall like a Class A player and placed 51% of the pieces the master placed.

**EPAM lineage (b15, a23, a24).** EPAM began with nonsense-syllable learning (1962), was extended to expertise and concepts (1984), and EPAM IV simulated trained digit-span experts with a retrieval structure (Richman, Staszewski and Simon 1995). CHREST borrowed its time constants from EPAM (section 4). Only secondary descriptions of EPAM were read.

**CHREST 1993 (c01-c03, b07).** Gobet extended MAPP with n-ary nodes, recursive chunking, redundant links, a dynamic STM and a retrieval structure. Nets of 630, 2,175 and 3,646 nodes after 230, 1,538 and 2,843 positions. It reproduced game over random (10.66 pieces vs 7.77, t(99) = 21.92) and fitted 97.4% and 77.5% of Class A data in two experiments. Failure: it recalled random positions too well (7.7 vs about 4 pieces for humans). That failure drove the later work.

**Random positions reopened (b03, a14, a15).** Gobet and Simon (1996) reviewed 13 experiments: every one except Chase and Simon found stronger players recall more on random boards, about one extra piece per 400 Elo points. CHREST without templates matched this: nets of 1k, 10k and 100k nodes gave 10.5%, 15.6%, 20.3% against human 11.7%, 17.0%, 23.7% (Class A, Experts, Masters). Gobet and Waters (2003, N = 36) tested template theory against the constraint attunement hypothesis with truly random boards and found a small reliable effect (r = .34; slope .052 per rating point vs .061 predicted).

**Location specificity (a12, b01, c03).** Holding (SEEK) said abstract, location-free chunks suffice, needing only about 2,500. Gobet and Simon (1996) mirrored and quadrant-swapped positions. Humans (N = 25) lost recall when chunks moved to unusual squares; so did a simplified CHREST. This was taken to reject Holding and support tens of thousands of chunks. Holding's own papers were not opened (a26).

**Templates (a05-a09, a13, b14).** Two problems with plain chunking: (1) masters recalled up to 60 pieces over several boards, far more than 7 chunks of 4-5 pieces; (2) interference tasks hurt recall little. Gobet and Simon (1996) proposed templates. The 1998 computer-display replication found master chunks of 16.8 pieces, not 7. Gobet (1998) scored chunking, SEEK, long-term working memory (Ericsson and Kintsch) and templates against about a dozen findings; templates fitted most. The author is a proponent, so the scoring is not neutral (b05).

**Time course (a10, a11, b04, d02).** Gobet and Simon (2000) varied exposure from 1 to 60 s (N = 20). CHREST with fixed EPAM constants and no refit matched the curves with nets of 500, 10,000 and 300,000 nodes.

**Search and categorisation (a17, d13, c05, a22, a25).** SEARCH (1997) made search depth a function of net size. Smith, Gobet and Lane (2009) simulated check detection. Lane and Gobet (2012) categorised openings at about 85%. CogAct (Bennett and Gobet 2025) learns concepts from raw text, chess and music with the same chunking steps.

**Critics and rivals.** Holding (SEEK, 2,500 chunks); Ericsson and Kintsch (long-term working memory, retrieval structures); Linhares and Freitas (2010, "experience recognition"; content not read, b19); constraint attunement (Vicente); Lane and Chang (2018) favour a conceptual-knowledge account (d11); Saariluoma and Laine (2001) offer a frequency-based learning rule (d12). Gobet, Lane and Lloyd-Kelly (2015) is a review from inside the group (d18).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Recall of game positions rises steeply with skill | 5 s recall of 25 pieces: masters about 93%, experts about 72%, Class A about half, novices about 8 pieces (de Groot, via Simon and Chase). Chase and Simon new positions: B 33%, A 49%, M 81% (N = 3) | a02, a04 | [E] (N = 3 in the 1973 data) |
| 2 s pause marks real chess relations | Chase and Simon 1973; 1998 computer-display replication, N = 26, Elo 1680-2510: copy within-glance r > .89 with 1973 relation probabilities; 2015 repeated-recall method kept the relation pattern (N = 50) | a03, a05, b10, b11 | [E] |
| Chunk size grows with skill; chunk count does not reliably track it | Largest chunk (median per position) Masters 16.8 pieces in recall, 14 in copy vs 7 in 1973. 1973 first chunk 3.8/2.6/2.4 (M/A/B). Gong 2015: count did not correlate with rating (N = 25 rated players) | a05, a01, b11 | size [E]; count [C] |
| Skill edge on random positions: small but real | 13 experiments, about one extra piece per 400 Elo (b03). Truly random: r = .34, N = 36 (a15). The 1973 null was one master, N = 3 | b03, a15, a02 | [E] |
| Same effect across domains | Meta-analysis: k = 28 samples, 24 studies, N = 903, r = .41 [.29, .51], I2 = 63%. Trim-and-fill r = .29 [.17, .41]. Games .42 (k = 11), music .69 (5), programming .36 (6), sports .30 (3, CI crosses 0), other .24 (3, CI crosses 0) | d01, b12 | [E]; bias-adjusted size smaller |
| Recall vs exposure follows P = 100 - B*exp(-c(t-1)) | Game: Class A B = 75.2, c = .033; Experts 66.4, .074; Masters 29.2, .435. Random: B = 90.6/85.3/80.5, c = .006/.012/.018. Masters at 1 s about equal Experts at 10 s. Masters 92.4% at 10 s. Masters' fit r2 = .35; others avg .69 | a10, d02 | [E] (N = 20, 5 Masters; one study) |
| CHREST predicts that curve without refit | Nets 500 / 10,000 / 300,000 nodes, logistic r2 > .95; underestimates Masters by about 8% at 5 s | a11, b04 | [S] model, one group |
| Visual STM of 3-4 chunks fits best | Fit .914 at 3 chunks to .985 at 4 (nets to 300,000). Human chunks per recall 3.3-3.6 | a18, b02, c06 | [E] within model; one group |
| Chunks are location-specific | Normal+horizontal vs vertical+central: Masters 77.3 vs 62.9, Experts 49.7 vs 38.6, Class A 34.5 vs 27.5 (N = 25); skill x type F(2,22) = 3.48. Sim 65.4% vs 63.2% (horizontal), 53.3% and 52.5% (vertical, central) | a12, b01 | [E] |
| Multi-board recall limit | About 4-5 boards at about 60%; a trained master reached 9 boards at over 70% (160 pieces) after months of cue-list practice; baseline 4 boards 50-55%, 2 boards 79.9% | a06, a08, a13, b05 | [E]; trained case N = 1 |
| Interference barely hurts | 30 s filled delay: 6-8% fewer pieces (Charness 1976) | a07, b05 | [E] |
| Chunk store size | 2,500 (Holding), 50,000 (Simon), 100,000, 300,000 nodes in master-level CHREST. None measured | a04, a26, c26, a11 | [C] |
| Training curves are power laws | Largest chunk 39*N^.31 (r2 = .93) and 55*N^.23 (r2 = .81), N = 2 novices, 15 sessions. CHREST: 4,772 chunks / 107 templates and 5,811 / 111. Parameter correlation model vs human .99 (a), .93 (b) | a16, b08 | [S] N = 2 |
| Search depth rises with pattern store, with diminishing returns | Model: under 1 ply with no chunks, 2.5 at 1,000, about 4 at 30,000, over 5 at 100,000. Human: de Groot 4.8 (experts), 5.3 (GM); Charness 2.3/4.1/5.7 at Elo 1300/2000/GM | a17, d13 | [S] model only |
| Bigger net, faster decisions | Check detection: 1705, 1403, 1301, 1068 ms at 100 / 1k / 10k / 100k nodes (r2 = .92); only 8 humans | c05 | [S] |
| Chunk classifier matches an SVM | Opening categorisation about 85% (French vs Sicilian) | a22, a25, c07 | [S] |
| Templates speed scanning | Sternberg task N = 60: experts 3.02 s vs club 3.62 s (600 ms faster); hit ratio .89; load effect F(1,54) = 12.70. Gobet co-author | d14, a20 | [S] |
| Knowledge beyond experience predicts memory | N = 79: chess knowledge r = .67 with recall, 16% unique variance after experience; fluid intelligence adds 13% | d11 | [C] (abstract only) |
| Knowledge, not raw capacity, drives gains (child model) | EPAM-VOC: adding WM growth gave no significant gain over knowledge growth | a19 | [S] |
| Time costs | New chunk about 8 s; familiarise about 2 s; slot fill about 250 ms; STM encode 50 ms | a09, a11, b04 | [S] inherited from EPAM |

## 4. Mechanisms and models

### 4.1 Discrimination net (EPAM, CHREST)
Data structure: a tree. Each internal node holds a test (in chess: is a piece of type X on square Y, within a field of plus or minus 2 squares). Each node holds an "image": the chunk content. CHREST uses n-ary nodes and also adds lateral links between nodes (4 after 100 positions, 20 after 2,843, c01).

Learning on each input:
1. Sort the input down the net until no test applies or a test fails.
2. Compare it with the image at the stopping node.
3. If the image matches but the input has more: discrimination. Add a new test and child node for one new feature. Cost about 8 s of simulated time.
4. If the input holds a detail the image lacks: familiarisation. Add it to the image. Cost about 2 s.
5. Learning only adds. Nothing is deleted. So the net grows with exposure and gives power-law practice curves.

An engineer can implement the net as a trie keyed on (item, location) tuples with images stored as lists.

### 4.2 Perception and working memory
- Perceiver: about 20 fixations in a 5 s exposure (c01). Each fixation sorts what is in view through the net.
- Visual STM: 3 chunk slots (4 in some fits). Placing a chunk costs 50 ms. A slot holds a pointer to a node, not the pieces.
- Recall reads out the images of the chunks held in STM.

### 4.3 Templates
Conditions in CHREST (a11): a node becomes a template if more than 3 nodes share information and the chunk has at least 5 elements. A template has a core (fixed part) and slots (variable parts). Slot fill costs about 250 ms and replaces building a new chunk (8 s). One template pointer per board takes one STM slot, hence the limit of 4-5 boards. In small-N training the slots were rarely used (the first novice placed none in slots, b08).

### 4.4 Recall curve
P = 100 - B*exp(-c(t-1)), t in seconds. B is what is not yet known after 1 s; c is the learning rate. Skill lowers B and raises c. For an agent this gives a measurable shape: fit B and c over exposure budgets per capability tier. Example constants in section 3.

### 4.5 SEARCH (a17, d13)
Recognised patterns propose moves and evaluations. Depth is a power function of net size and flattens (1,000 episodes per net size). Model only.

### 4.6 Concept learning (CogAct, Lane and Gobet 2012)
Hand-made attention heuristics (CHREST) vs raw-data chunking (CogAct). Both reach about 85% on two openings. On music, humans gave 100% confidence on 40 of 122 ratings; CogAct never; the ANN twice (a22).

### 4.7 Rival mechanisms
- Frequency-based learning (Saariluoma and Laine): fits the same curves. Curve fit cannot separate it from proximity-based chunking (d12, d15).
- Long-term working memory with a square-level retrieval structure: predicts a large random-position effect; data show a small one (b27, b05).
- Conceptual knowledge (Lane and Chang): not captured by pure pattern nets (d11).
- Semantic access (b06): chunks must link to semantic memory to explain level-of-processing results.

## 5. What holds up

**Replicated.**
- Large game-position skill effect; small random-position effect (13 experiments, a 36-player study, a 24-study meta-analysis).
- 2 s latency chunk boundaries and their link to chess relations (1973, 1998, 2015).
- Skill raises both the 1 s starting level and the later rate (N = 20; one study, not independently replicated).
- Location specificity (mirror and quadrant tests, human and model).
- Cross-domain random-material advantage (r = .41; .29 after bias adjustment).

**Failed or revised.**
- "Random positions show no skill effect": a low-power null (N = 3).
- "Number of chunks is constant across skill": not supported even in the 1973 data. Later: a hump in Masters (2.9 at 1 s, 4.2 at 4 s, 3.3 at 10 s) and no correlation with rating at brief views (b11, b26).
- "Chunks hold 4-5 pieces" (1973 master largest chunk about 7): replaced by 16.8 pieces (1998). Cause: display method and stronger players.
- Pure chunking with STM of 7 could not explain multi-board recall or interference; templates were added.
- CHREST 1993 over-recalled random positions (7.7 vs about 4 pieces) and showed no mirror cost when an internal board was used (c03).
- CHREST underestimates Master recall on game positions (b26) and chunk-size growth in training (a16).
- CHREST overestimated truly random recall by 12.1% on average (a15).
- Largest-chunk correlations of model and humans on random boards were low (0.20, 0.27, 0.03; a14).

**Moderators and boundary conditions.**
- Exposure time was not a moderator in the meta-analysis (p = .346); domain was borderline (Q(4) = 8.69, p = .069).
- Sports and "other" domains have CIs crossing zero.
- Chunk measurement depends on method: latency (noisy), repeated recall (better predictor, b10), display (mouse adds time).
- Instruction matters: if subjects know they must reconstruct, level-of-processing gaps vanish (Lane and Robertson, b06).
- Where retrieval structures are controlled (digit span), long-term working memory fits better.

**Interventions that worked.**
- Cue-list training raised one master from 4 to 9 boards (N = 1, mixes template and mnemonic effects).
- Practice raised novices' game-position recall on power curves (N = 2 in each of two labs). Ericsson and Harris (1990) reached master-like recall for game but not random positions (second-hand).
- Nothing in this subfield was tested as an intervention on LLMs.

**Independence caveat.** Most validation is by Gobet's group. Independent tests: Gong, Ericsson and Moxley 2015 (mixed: relations held, chunk number did not track rating); Lane and Chang 2018 (favours concepts); Saariluoma and Laine 2001 (N = 2, rival mechanism). The meta-analysis has Gobet as author. Founding data are N = 3. Interventions that did not work: none tested beyond the null results above (emotion priming, ns: Chassy 2023, N = 60).

## 6. Language models

No paper found runs a De Groot-style test (game vs scrambled position) on an LLM or fits CHREST constants to one (K22, b25, d16). What exists is indirect.

**Chess-playing transformers (pattern recall at scale).**
- Ruoss et al. 2024: 270M transformer, 10M Lichess games with Stockfish labels, no search: Lichess blitz Elo 2895 against humans, puzzle accuracy 95.4%; 9M model Elo 2025 and 88.9%; 136M 2259 and 94.5%; GPT-3.5-turbo-instruct 1755 vs bots and 66.5% (b21, c10). Test boards are unseen, so it is not memorising positions.
- Schultz et al. 2024: pretrained model plus search reaches Elo 2923 external; 100 MCTS simulations add 68 internal Elo over searchless (c14). Patterns and search are complements ([S]).
- Karvonen 2024 (COLM): 16-layer GPT, 99.8% legal moves, probe accuracy 99.6% per square vs 74.7% for random-init. Win rate vs Stockfish level 0: 64% (time-limited, headline) and 69.6% (100,000-node limit, Table 3). After 20 random moves: 16.7% (16L) and 15.7% (8L). With a skill vector: 43.2% and 31.3% (up to 2.6x). The 64% and 69.6% are one model under two engine limits (d03). "Random board" means 20 random moves, an out-of-distribution start, not scrambled pieces. The collapse resembles the human game-vs-random gap, but the author does not call it a chunk effect (b20, c11, c12).
- Chess-World-Model 2026: real-game accuracy saturates above 18M parameters; the random-play split stays discriminative to 40M (d16). Karvonen's pattern is the same: scale adds about 20 points on standard boards and about 1 on random starts.
- Toshniwal 2022: GPT-2-small on move strings tracks pieces with enough data; board-state tokens help most on small data (c13).
- McGrath et al. (AlphaZero, PNAS 2022) and Jenner et al. (Leela, 92% probe accuracy for the best move two turns ahead): learned nets hold human concepts and some look-ahead (b22, b23).
- Balogh and Jelasity 2026: no chess sequence model tested is sound; probes often have no causal role (c17).

**Frontier LLMs on transformed boards.** Song et al. 2025: standard-position error vs Stockfish 330 cp (Claude Sonnet 4.5) to 736 cp (Grok 4-1-Fast). 180-degree rotation error: 627 (Claude), 726 (Kimi), 855 (Gemini), 997 (DeepSeek), 1047 (Grok), 2531 (GPT-5.1). Left-right mirror: 196 (Claude), 95 (Kimi), 181 (GPT-5.1), up to 747 (Gemini). Rotation is bad and mirror is tolerated, which the authors read as absolute-square pattern memory (c15, d04, [S]). Mirror tolerance means the human mirror analogy is only partial.

**Order and length sensitivity (memory design).**
- Premise order (Chen et al., ICML 2024), 12 rules, forward vs shuffled: GPT-4-turbo 96.5 to 80.8%, PaLM 2-L 88.0 to 66.5%, Gemini 1.0 Pro 16.5 to 0.2%, GPT-3.5 30.0 to 1.2%. Gap grows with rules (GPT-4-turbo 0.2 to 15.7 points from 4 to 12 rules). R-GSM: 94.1 to 85.0 (GPT-4-turbo) (d06). This is the closest content-preserving scramble found. Numbers read through a page summary.
- Lost in the middle (Liu et al.): accuracy best at the start and end, worse in the middle (abstract only, 2023 models) (d05).
- Input length (Levy et al., FLenQA): mean accuracy 0.92 at 250 tokens to 0.68 at 3,000, padding irrelevant, chain of thought does not remove the drop (d07).
- N-back (Gong, Wan and Wang 2024): ChatGPT d' about 1 at 3-back; chain of thought helps; no chunk manipulation, so it cannot separate a 4-chunk cap from a token cap (c21, d17).

**Memory-management agents (chunk-like use).**
- HiAgent (Hu et al. 2024, GPT-4-turbo, AgentBoard, 5 tasks): success 21% to 42%, progress +23.94, steps -3.8, context -35%, time -19.42%. Decomposition alone gives +30 success points but stays 20 below HiAgent. Success moves in steps of 5-10 points (few episodes). Gripper unchanged (50 vs 50). No comparison with other summarisers. The chunk link is by citation of Miller, not by test (b24, c22, d08; b24 and c22 are one paper).
- Context-Folding (Sun et al. 2025, independent, Seed-OSS-36B, 32K): prompt-only BrowseComp-Plus (N = 150) 0.420 vs summary agent 0.386 vs ReAct 32K 0.286; SWE-Bench (N = 500) 0.492 vs 0.488. With RL: 0.620 and 0.580 (d09). The prompt-only edge over summarising is 3.4 and 0.4 points.
- MEM1 (Zhou et al. 2025, RL-trained): 16-objective QA, 7B with constant-size state EM 1.97 at 10.4 hundred peak tokens vs Qwen2.5-14B 0.567 at 38.4; 27.1% of the peak tokens (d10).
- MemGPT (paging, no numbers read) (c23).
- Michaud, ChessGPT, Maia, vision-language bias: abstract only, no numbers used (c09, c24, c25, c20).

**Chunk models in AI.** CogAct (preprint) is the only modern chunk model paired with a neural baseline. It is not an LLM study (a22, c08).

**What changed performance and by how much.** Scale: +20 points on standard boards, +1 on random starts (Karvonen 8L to 16L). Skill vector: up to x2.6 on random starts. Decomposition plus subgoal-close summary: +21 success points over full history (HiAgent), but only 3.4 points over summarise-when-full in prompt-only Folding. Order: 15-22 points in the 12-rule case. Length: -24 points from 250 to 3,000 tokens.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA.md section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Define the memory unit as a bounded cluster with strong internal relations; log items per retrieved unit.** Part: memory. [E]. Evidence: a03, a05, b10, K02, K03. Chunk size, not count, tracks skill.
2. **Keep the active working set to pointers to rich stored units, not raw items.** Part: G (limit working set), S3/S5 context. [E] for the principle (human and model fit of 3-4 chunks: a18, b02, c06, K05). The LLM-specific number is untested (K27), so adopt the principle and test the cap.
3. **Order context so active items sit at the start or end and facts follow solving order.** Part: memory, S1 input hygiene. [E]. Evidence: d05, d06, K23.
4. **Do not judge a memory design on structured cases alone; include scrambled or novel input.** Part: G7 (bench design). [E]. Evidence: b03, b12, d01, a15, b05.
5. **Do not rely on the 1973 numbers (7 chunks, 50,000 chunks, no random effect).** Part: documentation. [E]. Evidence: a05, b03, K09.
6. **Replace a closed subgoal trace with a short summary unit; keep raw trace retrievable.** Part: S6 subgoal, memory. [E] as a direction (three independent sources: HiAgent, Context-Folding, MEM1); adopt only if it wins at equal tokens (G7). Evidence: b24, d08, d09, d10, K19. Warning: decomposition alone is +30 of HiAgent's +50 points.
7. **Make retrieval keys tolerate surface transformation; do not assume mirror-type invariance.** Part: memory. [E] that human chunks are location-specific (a12, b01); the LLM rotation result is [S] (K20). Store a canonical form plus a relational description (a21).

### Test first (not established; see UNKNOWNS.md)
- Slotted (core plus slots) notes vs flat lessons at equal tokens. Part: memory. [S]. Evidence: a06, a09, b14, K04.
- Working-set cap in chunk units. Part: G. [S]/[C]. Evidence: a18, d07, d17.
- Short cue label per stored item. Part: memory. [S]. Evidence: a08 (N = 1), a13.
- Structured vs scrambled context recall curve on the model. Part: bench. [S]. Evidence: K16, K22.
- Library size vs gain (power law, flattening). Part: memory. [S]. Evidence: a16, b08, a17, d13.
- Pattern store x search budget. Part: S3, G12. [S]. Evidence: c14, b21, a17.
- Chunk-trie index vs embedding retrieval. Part: memory. [S]. Evidence: a22, a25.
- Cache verified results (write cost vs recompute). Part: memory. [S]. Evidence: b26, a09.
- Pattern notes plus concept notes. Part: memory. [C]. Evidence: d11, d12.

## 8. Concrete tests on our bench

All arms at equal total tokens (setup cost counted, G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 De Groot on the model | Fact lists (25-40 items) from a structured domain, vs the same items shuffled; vary context length | Structured vs shuffled; several model tiers | Items recalled; fit B and c over exposure budgets | Structured much higher; shuffled keeps a small edge that grows with model tier |
| T2 Template vs flat notes | Reuse tasks over 5-10 related problems per class | Flat lesson lines vs core-plus-slot notes (same tokens) | Pass rate on later problems; wrong-slot errors | Small gain for slotted notes when problems share structure; none on unrelated problems |
| T3 Subgoal-close summary | Long-horizon items from our bench | Full history vs summarise-when-full vs summarise-on-subgoal-close | Success rate; context tokens | Beats full history; margin over summarise-when-full about 0-4 points |
| T4 Working-set cap | Multi-hop items needing 3-8 stored facts | Cap of 2, 4, 8 and unlimited units | Accuracy; locate the knee | Knee near 3-5 units, if one exists |
| T5 Order | Same facts in solving order, shuffled, reversed; key fact at start, middle, end | The orders | Accuracy | Shuffled -10 to -20 points on 12+ rule items; middle worst |
| T6 Key invariance | Stored cases with paraphrased, reordered, relabelled queries | Surface-key vs relational-key retrieval | Retrieval hit rate; downstream pass | Relational keys lose less |
| T7 Library size | Classes with 10, 30, 100, 300 stored cases | Library sizes | Pass rate; fit power law | Fast early gain, then flattening |
| T8 Pattern vs search | Pattern-rich items | Retrieved patterns x search budget, factorial | Pass rate | Both help; positive interaction |
| T9 Chunk vs embedding retrieval | Class labelling from structured cases | Chunk-trie index vs embedding retrieval | Accuracy | About equal (as in the 85% opening task); win only if cheaper |
| T10 Cue index | 6-9 independent items seen in sequence | With vs without short labels | Retention vs number of items | Labels hold more items past 5 |

## 9. What does not transfer, and why

- **Time constants (8 s, 2 s, 250 ms).** Human learning times. An LLM writes a note in one call. Keep only the ordering: a new unit costs far more than a slot fill (K06).
- **Store sizes (2,500 to 300,000).** Not measured even for humans; the substrate differs.
- **Visual STM of 3-4.** Human visuo-spatial capacity. The LLM has a token window with other failure modes (length, order, middle). The principle transfers; the number does not (d17 cannot separate a chunk cap from a token cap).
- **Mirror and quadrant results.** Humans are location-specific. Frontier LLMs tolerate mirror but not rotation (d04). Partial analogy.
- **Karvonen random start.** It measures play after out-of-distribution openings, not recall of scrambled pieces (d03).
- **Chess pattern strength.** Ruoss's Elo comes from supervised engine labels on 10M games, not from prompting (c10). We do not train.
- **HiAgent and MEM1 headline gains.** Against a full-history baseline; MEM1 is RL-trained; small tasks; one model (b24, d10).
- **Closed ontology.** Games have piece, square, relation. Our tasks are open, so "chunk" needs a definition (b17 warns of definition drift).
- **Single-lab dependence.** Much support comes from one group; treat it as a hypothesis generator.

## 10. Open questions

1. Does an LLM show the game-vs-scrambled gap and the small residual edge, and does it scale with size? (K22)
2. Do slotted notes beat flat notes at equal tokens?
3. What working-set cap (in units) is right? Does exceeding it hurt?
4. How many stored cases before gains flatten (SEARCH: 2.5 plies at 1,000 chunks, over 5 at 100,000)?
5. Is chunk retrieval competitive with embedding retrieval?
6. Do independent labs replicate templates beyond Gong 2015? Lane and Chang say concepts matter.
7. Is chunk count constant, humped or flat? It depends on the method.
8. Does the random-start collapse (Karvonen) transfer to non-chess tasks?
9. What does the Linhares and Freitas (2010) critique actually claim? Never read.

## 11. Sources

[V] opened, [M] snippet or second-hand only.

- [V] Chase and Simon (1973) Perception in chess. https://gwern.net/doc/psychology/chess/1973-chase.pdf (figures not re-opened in the cross-check)
- [V] Simon and Chase (1973) Skill in chess. https://www.gwern.net/doc/psychology/chess/1973-simon.pdf
- [V] Gobet and Simon (1998) Expert chess memory: revisiting the chunking hypothesis. https://bura.brunel.ac.uk/handle/2438/1343
- [V] Gobet and Simon (1996) Templates in chess memory. https://www.Gwern.net/doc/psychology/chess/1996-gobet.pdf
- [V] Gobet and Simon (2000) Five seconds or sixty? https://bura.brunel.ac.uk/bitstream/2438/811/1/Five%20Seconds%20or%20Sixty%20.pdf
- [V] Gobet and Simon (1996) Recall of random and distorted chess positions. https://link.springer.com/content/pdf/10.3758%2FBF03200937.pdf ; https://bura.brunel.ac.uk/handle/2438/1345
- [V] Gobet and Simon (1996) Recall of rapidly presented random positions. https://link.springer.com/content/pdf/10.3758/BF03212414.pdf
- [V] Gobet (1998) Expert memory: a comparison of four theories. https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf
- [V] Gobet (1998) Memory for the meaningless. https://bura.brunel.ac.uk/handle/2438/2131
- [V] Gobet and Waters (2003) The role of constraints in expert memory. https://bura.brunel.ac.uk/handle/2438/803
- [V] Gobet and Jackson (2001) In search of templates. https://bura.brunel.ac.uk/bitstream/2438/770/1/ICCM-2001-Jackson.pdf
- [V] Gobet (1997) Pattern-recognition theory of search. https://bura.brunel.ac.uk/handle/2438/843 ; http://people.brunel.ac.uk/~hsstffg/
- [V] Gobet (1993) A computer model of chess memory. https://bura.brunel.ac.uk/bitstream/2438/2129/1/cogsci-1993.pdf
- [V] Gobet (2001) Comments on Saariluoma and Laine. https://bura.brunel.ac.uk/bitstream/2438/806/1/Saariluoma_Laine_reply.pdf
- [V] Smith, Lane and Gobet (2007) STM capacity and recall. https://bura.brunel.ac.uk/handle/2438/2813
- [V] Smith, Gobet and Lane (2009) Checking chess checks with chunks. https://uhra.herts.ac.uk/id/eprint/18099/1/smith-iccm-2009.pdf
- [V] Jones, Gobet and Pine (2007) EPAM-VOC. https://bura.brunel.ac.uk/handle/2438/1806
- [V] Gobet et al. (2001) What forms the chunks (BBS), abstract. https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/what-forms-the-chunks-in-a-subjects-performance-lessons-from-the-chrest-computational-model-of-learning/10B1B5BBE78D7B43D563DF81D513EB4B
- [V] Gobet, Lane and Lloyd-Kelly (2015) Chunks, schemata, retrieval structures. https://pmc.ncbi.nlm.nih.gov/articles/PMC4657374/
- [V] Lane and Gobet (2011) Commentary on Linhares and Freitas. https://uhra.herts.ac.uk/id/eprint/235/1/904357.pdf
- [V] Lane and Gobet (2012) Using chunks to categorise chess positions (abstract). https://researchonline.lse.ac.uk/id/eprint/102853
- [V] Bennett and Gobet (2025) CogAct. https://arxiv.org/pdf/2512.18665
- [V] Chassy, Lahaye and Gobet (2023) Templates but not emotions. https://www.journalofexpertise.org/articles/volume6_issue1/JoE_6_1_Chassy_etal.pdf
- [V] Gong, Ericsson and Moxley (2015) PLoS ONE. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0118756&type=printable
- [V] Sala and Gobet (2017) meta-analysis. https://link.springer.com/content/pdf/10.3758/s13421-016-0663-2.pdf ; https://pmc.ncbi.nlm.nih.gov/articles/PMC5323477/
- [V] Lane and Chang (2018), abstract. https://doi.org/10.3758/s13421-017-0768-2
- [V] Karvonen (2024) Emergent world models in chess LMs. https://arxiv.org/pdf/2403.15498
- [V] Ruoss et al. (2024) Amortized planning, chess. https://arxiv.org/pdf/2402.04494
- [V] McGrath et al. (2022) AlphaZero (abstract). https://arxiv.org/abs/2111.09259
- [V] Jenner et al. (2024) Learned look-ahead (abstract). https://arxiv.org/abs/2406.00877
- [V] Hu et al. (2024) HiAgent. https://arxiv.org/pdf/2408.09559
- [V] Sun et al. (2025) Context-Folding. https://arxiv.org/abs/2510.11967
- [V] Zhou et al. (2025) MEM1. https://arxiv.org/abs/2506.15841
- [V] Toshniwal et al. (2022) Chess as a testbed. https://arxiv.org/pdf/2102.13249
- [V] Schultz et al. (2024) External and internal planning. https://arxiv.org/pdf/2412.12119
- [V] Song et al. (2025) Geometric stability. https://arxiv.org/pdf/2512.15033
- [V] Walker and Lyons (2026) Chess-World-Model. https://arxiv.org/pdf/2605.30100
- [V] Balogh and Jelasity (2026). https://arxiv.org/pdf/2602.05903
- [V] Junkin and Nathanson (2025). https://arxiv.org/pdf/2510.27009
- [V] Parfenova (2026). https://arxiv.org/pdf/2609.22245
- [V] Vo et al. (2026) VLMs are biased. https://arxiv.org/pdf/2505.23941
- [V] Gong, Wan and Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/pdf/2305.03731
- [V] Liu et al. (2023) Lost in the middle (abstract). https://arxiv.org/abs/2307.03172
- [V] Chen et al. (2024) Premise order matters. https://arxiv.org/abs/2402.08939
- [V] Levy, Jacoby and Goldberg (2024) Same task, more tokens. https://arxiv.org/abs/2402.14848
- [V] Packer et al. (2023) MemGPT (abstract). https://arxiv.org/abs/2310.08560
- [V] Feng et al. (2023) ChessGPT (abstract). https://arxiv.org/abs/2306.09200
- [V] McIlroy-Young et al. (2020) Maia (abstract). https://arxiv.org/abs/2006.01855
- [V] Michaud (2024) Opening the black box of language acquisition (abstract). https://arxiv.org/abs/2402.11681
- [V] EPAM, CHREST, Chunking (Wikipedia). https://en.wikipedia.org/wiki/EPAM ; https://en.wikipedia.org/wiki/CHREST ; https://en.wikipedia.org/wiki/Chunking_(psychology)
- [M] Feigenbaum and Simon (1984) EPAM-like models; Richman, Staszewski and Simon (1995) EPAM IV (via Gobet and Simon).
- [M] Lane and Gobet (2012) full paper (via Bennett and Gobet 2025).
- [M] Holding (1985, 1992) SEEK (via Gobet 1998).
- [M] Linhares and Freitas (2010). https://doi.org/10.1016/j.newideapsych.2009.07.008 (title only).
- [M] Saariluoma and Laine (2001); Ericsson and Harris (1990); Vicente and Wang (1998) (second-hand via Gobet and Jackson, Gobet 2001, Sala and Gobet).
