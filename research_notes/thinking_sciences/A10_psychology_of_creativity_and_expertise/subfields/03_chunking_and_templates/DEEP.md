# Chunking and templates: deep document

*Subfield A10.03. Evidence ids (a01..d17) and claim ids (A10.03-K01..K28) refer to the jsonl files in this folder. [E] established, [S] single-source, [C] contested. [V] = page or PDF text opened, [M] = snippet or abstract only. All LLM numbers are paper-reported by the authors unless stated. Not re-opened in the audit: Chase and Simon 1973 numbers, Gobet and Simon 1996/1998, Gong 2015, Gathercole 2019, fingerprint, bridge, fMRI, AWM, BoT, LILO, DreamCoder (they rest on the evidence agents' reading).*

## 1. What it is

A chunk is a familiar unit in long-term memory that is retrieved and held as one item. Short-term memory is limited by the number of such units, not by the bits inside them (Miller 1956, a01). A person who knows a pattern holds it in one slot. A person who does not know it needs one slot per element.

Four ideas make up the subfield.

1. **Chunk.** A unit recalled as one act. In chess, a cluster of pieces that share relations (attack, defence, proximity, colour, type) (a04).
2. **Capacity in chunks.** Miller said 7 plus or minus 2. Later work says 3 to 5 meaningful items (Cowan, a24). The number moves with how a chunk is defined and how long the display is shown (b21).
3. **Template.** A larger long-term unit: a fixed core of about a dozen items plus slots that fill in about 1 to 2 s, against about 8 s to learn a new chunk (Gobet and Simon 1996, a12).
4. **Retrieval structure.** A deliberate index built by training, such as S.F.'s running-time codes, which took digit span from 7 to about 79 (a25, b16). It stays bound to one kind of material.

Founding observation: masters recall real chess positions far better than novices, but the gap shrinks on random boards (a03, a06). The skill edge is memory for patterns, not a bigger buffer.

Why it matters for our agent: the schema's memory is a library of subgoals and lessons (S9 writes a lesson line). Chunking theory says what such a library should look like (many small reusable units, keyed to context, built from many examples) and how big the working set should be (about 4). The LLM literature (section 6) says when libraries help and when they only look like they help.

Scope note: representational change, transfer of learning, schemas, case-based reasoning, expert-novice differences and case-base maintenance are researched in parallel. Here we only note links.

## 2. History and theories in depth

**Miller (1956) [V, a01, a02].** Absolute-judgment span is limited by bits (about 2.5 bits for pitch, 2.3 for loudness, 3.25 for position; about 6 to 7 categories). Immediate memory span is limited by chunks. Hayes: span about 9 for binary digits but about 5 for monosyllabic words. Recoding: 20 subjects had span 9 binary digits vs 7 octal digits. Smith drilled himself to 12 octal chunks worth 24 bits (2:1 grouping), 36 bits (3:1) and about 40 bits (4:1, 5:1). Miller warned that the recoding must be "almost automatic" or the translation eats the span. He left "chunk" loosely defined. Recoding schemes were tested on 5 subjects each.

**De Groot, then Chase and Simon (1973) [V, a03-a08].** De Groot's masters recalled more than weak players. Chase and Simon tested three players (master M, Class A, beginner B) in a copy task and a 5 s recall task.
- Middle game, trial 1: M about 16 pieces, A about 8, B about 4. Endgame: 8, 7, 4. Random boards: no relation between skill and recall. The master was inactive in chess at the time.
- Chunk boundaries by timing: within a glance, placements came under 2 s apart. Between glances the gap was about 3 s (2.8 / 3.2 / 3.5 s for M / A / B). Model: about 2 s to start a chunk plus about 300 ms per element.
- Within-chunk pairs share chess relations. Between-chunk pairs look like chance. Relation profiles correlated .91 to .95 across subjects.
- The master recalled both more chunks and larger chunks. The theory had predicted constant chunk count. The authors called this surprising (a05).
- Popular summary (American Scientist): master/grandmaster 93% of a 25-piece position, expert 72%, Class A about half, novice about 33% (about 8 pieces). Random boards: 3 to 4 pieces for every level (a06). In one master's protocol there were 77 chunks: 47 pawn chains, 10 castled kings, 27 other same-colour clusters (75% stereotyped).
- Theory: STM of about seven chunk names; a long-term store of patterns reached through an EPAM discrimination net; learning about 5 s per chunk. Recalling over 20 pieces implies chunks of about 3 pieces. Vocabulary estimate about 50,000 chunks (a crude extrapolation from a 1,000-pattern net). Practice estimate 10,000 to 50,000 hours for a master (a07).
- MAPP program (PERCEIVER scan plus EPAM net): with about 1,000 patterns it performed about like a Class A player. It recalled 51% of the pieces the master placed correctly (a08).

**EPAM and CHREST [V, a21].** EPAM (Feigenbaum and Simon) is a discrimination net that grows by learning. CHREST (Gobet) adds eye movements, a visual STM of about 2 to 5 chunks, templates and lateral links. Time parameters from EPAM: 8 s to create a chunk, 4 s to flag a node, 50 ms to put a symbol into STM, 50 ms to compare two symbols, 10 ms per net test. Fit: with STM span 4, random-position recall was 10.5 / 15.6 / 20.3% for nets of 1k / 10k / 100k nodes. Humans scored 11.7 / 17.0 / 23.7% (Class A / expert / master, 10 s or less). The simulation also reproduced the mirror-image cost seen in humans (a20). Later work puts the human master chunk store at over 300,000 chunks (c09, via Bennett and Gobet 2025), above the older 50,000.

**Ericsson, Chase and Faloon (1980), S.F. [M for the primary; a25, b16].** A runner of normal span trained about 230 hours (about 20 months). Digit span rose from 7 to almost 80. He used running times (about 62% of codes) and ages (about 25%), in chunks of 3 to 4 digits, never rehearsing more than 6. Letter span stayed at 7. A second runner, D.D., repeated the feat. The primary paper was not opened (403). The retrieval structure was tree-like, 3 to 4 digits per twig, and built on purpose (a26).

**The capacity debate [V, a24, b21].** Cowan: a central store of 3 to 5 meaningful items. Chen and Cowan: about 3 chunks whether items were singletons or learned word pairs. A 2024 modelling paper (Journal of Cognition) finds capacity estimates higher at 5,000 ms than at 120 ms presentation, read as time for recoding. So 4 vs 7 is mostly chunking opportunity.

**Problems for pure chunking, then templates [V, a09-a13, b09].** Strong players recall several boards past 7 plus or minus 2 chunks. Gobet and Simon (1996): 13 subjects (3 masters, Elo 2453; 4 experts; 6 Class A), 5 s per board, 1 to 5 boards. Chunk counts rose from 2.3 (1 board) to 9.9 (5 boards) for experts and masters, with some people at 13 to 15. Largest chunk 19.7 pieces (masters, one board). Interference barely hurts chess recall: a 30 s delay cost 6 to 8% (Charness 1976). Template theory answers both: a core of about 12 pieces with slots.

**Four-theory comparison [V, a14-a16, b14].** Gobet (1998) compared chunking, SEEK (high-level schemas, no random-board edge), long-term working memory (retrieval structures; the square version predicts a far larger random edge than seen) and template theory. He rates template theory best. He is its author, so this is not an independent ranking. The random-board edge is the discriminating test: chunking and templates predict a small edge, SEEK none.

**Abstract-relations rivals [V, b13, b19].** Linhares and Brum argued experts encode abstract relations. Bilalic and Gobet replied that this reflects task instructions. Gong et al. found only attack and defence relations separated players from non-players. Bridge experts (Liu 2025) use suit grouping (surface familiarity) plus abstract knowledge, which supports a hybrid.

**Computational line, 2020 onward [V, c06-c10].** CogAct (Bennett and Gobet 2025, preprint) learns chunks from raw text, music and chess with one mechanism and no domain features. French vs Sicilian opening classification: 53 of 61 correct (chance 31), about 85%, matching hand-featured CHREST. It held about 3,000 chess chunks, 34,000 literature chunks and 22,000 music chunks. No LLM was run.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Span is limited by chunks, not bits | Judgment about 2.5 bits; binary span 9 vs octal 7 (N=20); Smith up to about 40 bits in 12 chunks | Miller 1956 (a01, a02) | [E] |
| Capacity nearer 3-5 than 7 | About 3 chunks for singles or learned pairs; 3-5 items | Cowan 2010 (a24); 2024 J Cognition (b21) | [E] |
| Presentation time moves capacity | k higher at 5,000 ms than 120 ms | b21 (abstract and intro only) | [E], thin |
| Expert recall of real positions | M about 16 / A about 8 / B about 4 pieces (N=3); 93% / 72% / ~50% / 33% | Chase and Simon 1973 (a03, a06) | [E] |
| 2 s chunk boundary | Within-glance 79.5% under 2 s vs 1.11% between; N=26 | Gobet and Simon 1998 (a17) | [E] replicated |
| Random-board skill edge is small | r=.41 [.29,.51], k=28, N=903, I2=63%; trim-and-fill .29 [.17,.41]; 49 of 55 positive | Sala and Gobet 2017 (a23, b01-b03) | [E] |
| Founding "null on random" was noise | Strongest beat weakest in 12 of 13 experiments, p=.0017; about 1 piece per 400 Elo random vs about 5 per 400 Elo game | Gobet and Simon 1996 (b04) | [E] |
| Not guessing | Commission errors at 5 s: 2.4 / 5.5 / 3.9 (M/E/A), n.s. | b05 | [E] |
| Domain split of random edge | Games .42 (k=11), music .69 (k=5), programming .36 (k=6), sports .30 [-.04,.58] (k=3), other .24 (k=3); moderator p=.069 | Sala and Gobet 2017 (b02) | [E], weak moderator |
| Chunk size depends on method | Master largest chunk about 5 (1973) vs 16.8 recall / 14 copy (1998) vs 14.8 computer, 7.5 board (2004) vs 4.56 (repeated recall, club players) | a18, b10, b11, b12 | [C] |
| Skill effect on chunks is for game positions only | Largest chunk game: M 11.2 / E 7.4 / A 6.2; random 4.1 / 4.3 / 4.1 | Gobet and Simon 1996 (b08) | [E] |
| Repeated-recall method | N=25 players + 25 non-players; chunks 2.74 vs 1.02; largest 4.56 vs 2.60; r=.60 with rating; random n.s. | Gong et al. 2015 (b12) | [E] |
| Chunks are location specific | Masters 77.3% normal/horizontal vs 62.9% vertical/central; skill x type F(2,22)=3.48 | Gobet and Simon 1996 (a19, b07) | [E], semantic confound |
| Multi-board recall exceeds 7 chunks | Chunks 2.3 to 9.9 (1 to 5 boards); up to 15 | Gobet and Simon 1996 (b09) | [S] |
| Gap between boards helps | 1 to 10 s gap: masters +71% (2 boards), +63% (4); experts +40%, +33%; N=5 | a10 | [S], tiny N |
| Retrieval structure scaling | A master reached 9 boards in block 18; 71.82 + 0.58 per block (2 boards) | a11 | [S], N=1 |
| Interference barely hurts | 6-8% loss after 30 s | Charness 1976 via a13 | [S] |
| S.F. digit span | 7 to about 79 (about 230 h); letters stayed 7 | a25, b16 | [E], N=1 then 2 |
| Digit span training does not transfer | Trained digits 406 to 659 (d about 1.60); letters p=.300 | Gathercole 2019 (b17) | [E] |
| Outside games | Fingerprints d=1.76 (44+44), experience r=.01; bridge suit grouping | b18, b19 | [E] / thin |
| Time course on random boards | Masters about 68% (17 of 26) at 60 s; class A 11.7% / expert 17.0% / master 23.7% at 10 s or less | Gobet 1998 (a15, a22) | [E] |
| Legal vs illegal noise | Random legal games about 60% after 25 moves vs about 90% real; random illegal under 20% | Saariluoma via b15 | [S] |

## 4. Mechanisms and models

Explained so an engineer can build them.

**4.1 Chunk store as a discrimination net (EPAM/CHREST).**
- Data structure: a tree. Each node tests one feature of the input and holds an image (the chunk content). Learning adds a test branch when two inputs sort to the same node but differ (discrimination), or adds features to a node's image (familiarisation).
- Costs from the human fit: create a node about 8 s; add to an existing node about 1 s; one net test 10 ms.
- Working buffer: a visual STM of 3 to 5 chunk pointers (best fit 4). Not tokens; pointers to nodes.
- Recall: scan the input, sort each fixation through the net, put the retrieved node in STM, output its image. More nodes means more recall, also on random input (a little), because random material contains accidental small chunks.
- Engineering mapping: store = library of subgoal entries with applicability tests as the net. Buffer = a working set of 3 to 5 active entries in the prompt. Retrieval = sorting the current problem through the tests.

**4.2 Chunk detection by co-occurrence and latency.** A chunk boundary is a gap above a threshold (2 s in chess). Within-chunk items share relations (a04, a17). For a log of agent steps, define a chunk as a run of steps that are always used together and share relations. Cut when pair co-occurrence falls to chance. Do not trust a single size (section 5).

**4.3 Template = core plus slots plus defaults.** About 12 fixed items, slots with default values, filled in 1 to 2 s, and links to other templates (openings, endings) (a12, a26). Implement it as a parametrised routine: fixed steps, typed parameters, default values, pointers to follow-up routines. Slot filling is cheap and creation is costly, so create templates from many instances.

**4.4 Retrieval structure.** An index fixed in advance (S.F.'s tree with 3 to 4 digits per twig; the cue list of champion names for boards). It multiplies capacity but is trained deliberately and is domain-bound (a16, a26). Chess templates are a content network built as a by-product of play. Our library is the second kind plus an explicit index per task family.

**4.5 Compression as chunk selection (DreamCoder, LILO) [V, c16, c17].** Find sub-programs shared by many solved programs, add them as named primitives, retrain a search guide. DreamCoder text editing: 3.7% solved in 10 min before learning, 79.6% after. LILO adds LLM synthesis, Stitch compression and AutoDoc naming.

**4.6 Soar-style chunking [c19].** At an impasse the system makes a subgoal. When it is solved, the system writes a new production that fires directly next time. CoALA places this in procedural memory. This is the classic link between chunking and the schema's S6 impasse.

**4.7 Skill library with write gate (Voyager, SELM).** An executable program is stored after self-verification and retrieved by description. Gate writes by validation, score by utility, prune on negative feedback (d12).

## 5. What holds up

**Replicated, solid.**
- Chunk boundary at about 2 s (a17; 79.5% vs 1.11%).
- Expert advantage on real positions across many studies and fields (b18, b19, a23).
- A small expert edge on random material: r=.41, k=28 (a23). It shrinks to .29 after bias correction. Sports and other domain CIs include 0, and the domain test is p=.069. Cite .41, not the .42 from an earlier abstract.
- Chunk store grows with skill; the computer model matches human recall curves (a21).

**Failed or weakened.**
- Chase and Simon's "no skill effect on random boards" (N=3, inactive master). Pooled later data reject it (12 of 13, p=.0017) (b04).
- Constant chunk count across skill: failed in 1973 itself (a05).
- Fixed chunk size: 5 pieces (1973) vs 14-17 (1998 computer) vs 4.6 (2015) vs 7.5 vs 14.8 (2004 board vs screen). Method, not person, drives it (b10-b12).
- The pure STM-chunk model fails on multi-board recall and interference, hence templates (a09, a13).
- The Gong 2015 independent method found no significant random-board skill effect, unlike the meta-analysis (b12). Small N and club-level players are the likely reason.
- Digit-span training does not transfer to letters (b17), and S.F.'s skill stayed at 7 on letters (b16).

**Moderators.**
- Presentation time and display medium (b11, b21).
- Rule-governed vs scrambled structure: random legal move sequences keep recall, illegal ones do not (b15).
- Domain: music at .69 reflects less random material (b02).
- Reflection: a vertical flip hurts strong players more, but also changes king-side priors (a19, b07).
- Experience did not predict fingerprint accuracy (r=.01) (b18). Selection or training may explain the gap.

**Interventions that worked (humans).** Recoding with a trained code (Miller; S.F.). Longer gaps between boards. A cue-list retrieval structure for one master (single subject; the "9 boards" claim of Cooke was judged dubious by Gobet and Simon).

**Interventions that did not work.** Brief recoding practice for 4:1 and 5:1 ratios (a02). Transfer of trained span across material (b17). Large libraries without gates (section 6).

**Weak spots in the evidence base.** Template theory rests on one lab (the Gobet group); independent replication is thin. The four-theory comparison is written by a proponent. Several sources were seen as abstracts or snippets only (b25-b28, c25, c26).

## 6. Language models

No study gives an LLM the Chase-Simon recall task (meaningful vs shuffled structured input). None tests chunked vs unchunked span (K19). The search was partial, so absence is not proof. The evidence below is a mix of proxies.

**6.1 Familiarity gradient in chess (the nearest analogue) [V, c01-c05, d13, d14].** Pleiss, Schiffer and von Weizsaecker (2026, arXiv 2601.16823), 500 positions per condition (1,500). Task: choose a move; 10 pieces per side on random boards. Familiarity is estimated from Lichess Masters counts (at least 1,000 occurrences), not from known training data.
- Average centipawn loss across GPT-3.5, GPT-4o and GPT-5 was 4.75x higher near-distribution and 7.79x higher on random boards than on familiar ones.
- Illegal moves: 1.46x near, 4.72x random. Overall GPT-3.5 74.7%, GPT-4o 41.6%, GPT-5 33.8%. Claude Opus 4.6: 0.2% / 8.2% / 51.6% (familiar / near / random). Gemini 3 Flash: 2.2% / 17.0% / 72.0%. These two are the authors' own extension, not independent.
- On random boards base models did no better than random legal play (c03). GPT-5 on familiar positions: centipawn loss 26.19, about 4x better than random legal moves.
- Per-generation gain: on random boards 9.08% (3.5 to 4o) and 5.73% (4o to 5); on familiar positions 70.7% and 69.92% (c03). Newer models gain mostly where positions are familiar (c05).
- Reasoning effort: GPT-5 minimal to moderate cut centipawn loss 71.74% overall (85.3% near, 77.25% familiar, 64.69% random). At moderate effort it spent 3,426 / 11,800 / 16,953 tokens on well-known / near / random positions. Relative gain per 1,000 tokens: 22.55% / 7.23% / 3.81% (v3 text, d13). An earlier version (c04, and an earlier critique note) gave about -50% and -89% relative to familiar. Use v3 and flag the version. The direction is the same.
- Limits: move choice, not recall; one lab; chess only; reasoning tested on GPT-5 only.

**6.2 Capacity and internal state.** Gong et al. 2023/24: ChatGPT shows a human-like n-back capacity limit (d' falls to about 1 at 3-back). Prompt strategies did not remove it (c20, c21; abstract-level, d15). That is attention capacity, not chunk use. Karvonen 2024: a GPT trained on real chess games has linear-probe board state (legal move rate 99.8% / 99.6%; probe 99.6% vs 74.7% on a randomised model), but only on real games (c22). Wenliang 2024: a 270M model without search reached Lichess blitz Elo 2895. On Chess960 the 9M model dropped from 2054 to 1539 (c23).

**6.3 Chunk-like libraries for LLM agents.**

| System | Result | Caveat |
|---|---|---|
| Voyager (c11, c12, b22) | 3.3x unique items (63 in 160 iterations), 2.3x distance, tech milestones up to 15.3x faster (wood 15.3x, stone 8.5x, iron 6.4x); random curriculum -93%; no self-verification -73%; GPT-3.5 gives 5.7x fewer items | Library removal only as a plot ("plateaus late"); curriculum confounded |
| Agent Workflow Memory (b24, c15) | WebArena +12.0 points, 51.1% relative; 2.0 fewer steps; Mind2Web +24.6% relative; +8.9 to +14.0 as train-test gap widens | No reuse audit |
| Buffer of Thoughts (c13, c14) | Game of 24: BoT 82.4% vs ToT 74.0% vs GPT-4 3.0%; +11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One; about 12% of multi-query cost; rounds of 50 questions | Authors' own; table values from text extraction |
| LILO (c17) | Raw Stitch abstractions HURT the LLM: -30.60 REGEX, -2.91 CLEVR, -11.11 LOGO. AutoDoc recovered +9.73 / +2.27 / +0.00 | Three small domains |
| DreamCoder (c16) | 3.7% to 79.6% solved | Symbolic, not LLM |
| ASI (d16) | Verified programs +23.5% over static agent, +11.3% over text skills | Abstract only |
| SkillWeaver (d17) | Up to +54.3% for weaker agents using stronger agents' APIs | Abstract only; across agents, not domains |
| ReasoningBank (d03-d05) | WebArena, Gemini-2.5-flash: no memory 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8. +4.3% tokens for +20.5% relative success. Shopping subset: no-memory best-of-5 42.2 vs memory single run 49.7. Retrieve 1 item 49.7, 2: 46.5, 3: 45.5, 4: 44.4 | AWM below no memory for Claude-3.7 (40.8 vs 41.7); one backbone; text strategies |

**6.4 Failed replication and warnings.**
- Berlot-Attwell et al. 2024 (b23) [V, re-opened]: LEGO-Prover learned over 20,000 lemmas. 1,233 (about 6%) reached final prompts, and one lemma was reused, once. TroVE on MATH: 15 learned functions in 3 of 7 splits and 3 reuses in 3,201 questions. A no-reuse ablation beat TroVE on 3 of 4 splits (2 significant). The authors credit self-correction and self-consistency for the gains.
- Add-all memory loses to a small verified one in 4 of 4 agents (Xiong 2025, d01). RegAgent: fixed 67.53, add-all 55.48, strict 70.95. EHRAgent: 16.75 / 13.05 / 38.50. AgentDriver: 40.11 / 32.32 / 51.00. CIC-IoT: 71.50 / 59.90 / 85.40. Wrong items spread by copying (d02). Deletion by later utility helped with a reliable judge and flipped with a weak one.
- SkillEvolBench (d06, d07): 180 tasks, 10 model configurations. Raw-trajectory replay is the strongest baseline (mean RSR 48.2, ESR 37.6). Curated static skills help 2 models, tie 1 and hurt 7 (mean ESR -2.44). Bigger libraries cut ESR (Gemini 3 Flash 35.6 to 27.8; Sonnet 4.5 35.6 to 30.0).
- SELM (d12), SpreadsheetBench, Claude Opus 4.6: full 56.5; no validation gate 42.5; no utility score 46.3; no utility-aware retrieval 49.2; no graveyard 50.4. The 30.0 vs 36.43 baseline in its text is ambiguous.

**6.5 Granularity, surface form, slots.**
- Mixed granularity beat flat on ALFWorld: 51.31 vs AutoSkill/EvoSkill 47.14 vs baseline 45.00 (SkillLens, d08). Evolution tokens 16.41M vs 115.51M for rewrite-all.
- Best skill length depends on model: Qwen3-4B best at about 1,092 tokens; 14B and 32B at about 2,737; Qwen3-8B best with no skill (32.1%) (MASA, d09).
- Retrieval by wording fails under surface change. A layout-structure signal restored reuse: WebArena 45.7 falls to 39.2 without it (no-skill 38.5); Mind2Web cross-domain 59.4 to 55.8 (SkillMigrator, d10). This is not a paraphrase test as such.
- Slot templates are used across sites (d11), but no clean slots vs fixed ablation exists (K26).
- Raw experience vs insight: ExpeL insights-only vs retrieval-only 36% vs 31% on HotpotQA and 50% vs 55% on ALFWorld (c18; row assignment uncertain).

**6.6 CogAct (c06-c10).** A chunking model reaches 85% on opening classification with no domain features. It is not an LLM study.

**What changed LLM behaviour, and by how much (summary).**
1. Verification gate on writes: 14 points in SELM (56.5 vs 42.5); 3 to 22 points in Xiong.
2. Structure key in retrieval: 6.5 points.
3. One retrieved item rather than four: 5.3 points.
4. Executable verified over text: +11.3% relative.
5. Naming and documenting abstractions: +9.73 recovered on REGEX.
6. Model generation: gains concentrate on familiar items (c05).

## 7. What our agent should take

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Size the active working set in chunks, about 4 slots, not in tokens or raw items (as a cap to be tuned) | S (S3/S4 context), memory | [E] for humans | a01, a24, b21 (K01, K02) |
| Do not hard-code a chunk size. Store entries at 2 to 3 sizes and let the retriever choose. Validate on the target model | memory | [E] that size is method-dependent; [C] on best size | a18, b10-b12, d08, d09 (K06, K23) |
| Write a library entry (S9 lesson) only after it passes a check on a case it was not fitted to. Prune on negative utility. No add-all | memory write gate; G2, G3 | [E] | d01, d02, d12, d06 (K20) |
| Retrieve few: default k=1, at most 2 to 3. Never dump the library into the prompt | memory retrieval | [E] | d05, d07 (K21) |
| Key entries to problem class and structure, not wording alone | memory retrieval | [E] for humans; LLM direction [S] | a19, b07, d10 (K07) |
| Log the reuse rate per entry. Credit the library only if a no-reuse arm loses | G7 | [E] warning | b23 (K16) |
| Expect gains on in-pattern classes, not on novel or scrambled ones. Verify outside the familiar region in code | G3, G5, S0 | [E] for humans; LLM [S] | a23, b04, c01-c03 (K03, K04, K13) |
| Name and describe an entry in words, not only code or raw trace | memory | [E] direction; format [C] | c17 (K18), d16 |
| Keep a library per task family. Do not assume transfer | memory scope | [E] | b16, b17, a16 (K09) |

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Library vs no library at equal total tokens, with a zero-reuse arm | memory, G7 | [S]/[C] | b23, d03, d04 (K15, K16) |
| Parametrised templates with slots and defaults vs fixed text entries | memory | [S] | a12, b09, d11 (K08, K26) |
| Less thinking when a library hit is found; cap tokens on library misses | S0 gate, G11, G12 | [S] | d13, c04, d04 (K14, K25) |
| Keep the raw trace beside the distilled entry | memory | [S] | d06 (K22) |
| Working-set size 4 vs 7 vs 12 | S context | untested on LLMs | a24, d05 (K02) |
| Structure-keyed vs text-keyed retrieval under paraphrase and reorder | memory retrieval | [S] | d10 (K24) |
| Named+documented vs code-only vs text-only entries | memory | [C] | c17, d16, d09 (K28) |
| Consolidation budget for storing an entry | S9 | [S], human only | a10 |
| Mixed-granularity retrieval | memory | [C] | d08, d09 (K23) |
| Meaningful-vs-shuffled recall probe on our model | diagnostic | [S] | c24 (K19) |

## 8. Concrete tests on our bench

All arms run at equal total tokens, including setup and library writing.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Task families with repeated structure (ARC-like, BRAINTEASER) in a train/test split | No library; verified library; library with reuse blocked (entries shown but a placeholder swapped in) | Accuracy; reuse rate; gap between library and no-reuse arms | Small gain on in-family items. The gap to the no-reuse arm shows reuse vs self-correction |
| T2 | Same items | Add-all vs gated vs fixed small (about 20 entries) | Accuracy; library size; delete count | Gated beats add-all by several points (Xiong: 3 to 22) |
| T3 | Same items | k = 1, 2, 3, 5 retrieved | Accuracy | Peak at k = 1 to 2 (ReasoningBank 49.7 to 44.4) |
| T4 | Active-set cap | 4 vs 7 vs 12 subgoals in the working set | Accuracy | Flat or falling above about 4 |
| T5 | Held-out variants | Text-keyed vs structure-keyed retrieval on paraphrased, reordered and renamed problems | Hit rate; accuracy | Text-keyed hit rate drops under surface change. A structure key limits the drop (SkillMigrator 6.5 points) |
| T6 | Parametrised routines | Same routines fixed vs slotted with defaults | Accuracy on new instances; tokens per solve | Slots cut tokens and help on new instances |
| T7 | Three granularity sizes | Step vs 3-5 step chunk vs template vs mixed | Accuracy; hit rate | No single winner. Mixed at least ties |
| T8 | Familiarity tiers | Task classes ranked by plain-model pass rate (familiar / near / novel) | Gain per 1,000 thinking tokens by tier | Falling gain per token with novelty (Pleiss: 22.55 / 7.23 / 3.81%) |
| T9 | Budget rule | Uniform budget vs less on library hits and capped on misses | Accuracy per total token | Same accuracy at lower cost |
| T10 | Chase-Simon probe | Structured vs shuffled state descriptions (task states, plans), with and without the library in context | Items recalled; first-error rate | Large gap structured vs shuffled; small residual edge on shuffled |
| T11 | Named/doc entries | Name+description vs code only vs raw trace | Accuracy | Documented beats code-only (LILO direction) |
| T12 | Cross-family transfer | Library from family A tested on family B | Hit rate; accuracy | Near-zero transfer; confirms domain binding |

## 9. What does not transfer, and why

- **Chunk size numbers (3 to 4, 5, 7, 15).** They depend on display, method and definition (b11, b12). An LLM has no 2 s latency. Token order and output limits create different "chunks".
- **The 2 s boundary.** A property of human motor and attention timing. For LLMs use co-occurrence of steps, not time.
- **The human limit of about 4.** LLM context holds thousands of tokens and attends to all of them. The limit that matters is retrieval and distraction (more retrieved items hurt: 49.7 to 44.4), not a buffer of four pointers. "About 4" is a design prior to test, not a fact about LLMs.
- **S.F. and D.D.** Two trained runners. The skill stayed bound to digits. For LLMs the long-term store is outside the weights. Writing an entry takes tokens, not months of practice.
- **Learning time (5 s or 8 s per chunk, 50,000 chunks, 10,000 hours).** LLM library writes cost tokens. The relevant costs are per-write verification and pruning.
- **Eye movements and spatial reflection.** Chess perception effects have no direct text analogue.
- **Implicit acquisition of templates by play.** An agent library is explicit. Entries do not form on their own.
- **fMRI, fingerprint, bridge results.** They show expertise generalises across fields. No design consequence for a text agent.
- **CogAct and EPAM learning from raw exposure.** Our agent will add entries from at most hundreds of examples, far below human-scale stores of 300,000 chunks.
- **The surface vs abstract debate.** For an LLM the retriever sees text. Both layers must be coded explicitly.

## 10. Open questions

1. At equal tokens, does a subgoal library beat no library, and is the gain from reuse? (K15, K16. ReasoningBank partly closes it. No zero-reuse ablation exists.)
2. Which granularity wins: step, 3-5 step chunk, or parametrised template? (d08, d09 show no single winner. No direct sweep.)
3. Does retrieval survive paraphrase and reorder? (d10 is indirect.)
4. Does a template with slots beat a fixed chunk for LLM agents? (K26. No controlled contrast.)
5. Is there any LLM version of Chase-Simon recall or chunked span? (K19. None found; the search was partial.)
6. Independent replication of Pleiss et al., beyond chess and by another team. (d14 is the same team.)
7. Staleness: when do old entries hurt over time? (Direction known; drift not isolated.)
8. Does the 4-slot working-set prior help an LLM at all, given long context?
9. Named and documented vs code-only entries across more than three domains. (c17, d16.)
10. Cross-domain transfer limits of a library. (d17 is cross-agent.)
11. Human template data from a second lab. All come from the Gobet group.

## 11. Sources

[V] opened, [M] snippet or abstract only. Some [V] items were read by evidence agents and not re-opened in the audit (see header).

Human work
- [V] Miller (1956) The magical number seven. https://psychclassics.yorku.ca/Miller/
- [V] Chase and Simon (1973) Perception in chess. https://gwern.net/doc/psychology/chess/1973-chase.pdf
- [V] Chase and Simon (1973) Skill in chess. https://www.Gwern.net/doc/psychology/chess/1973-simon.pdf
- [V] Gobet and Simon (1996) Templates in chess memory. https://www.Gwern.net/doc/psychology/chess/1996-gobet.pdf
- [V] Gobet and Simon (1996) Recall of random and distorted chess positions. https://bura.brunel.ac.uk/handle/2438/1345
- [V] Gobet and Simon (1996) Recall of rapidly presented random chess positions is a function of skill. https://bura.brunel.ac.uk/handle/2438/1346
- [V] Gobet (1998) Expert memory: a comparison of four theories. https://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf
- [V] Gobet and Simon (1998) Expert chess memory: revisiting the chunking hypothesis. https://bura.brunel.ac.uk/handle/2438/1343
- [V] Gobet (1998) Memory for the meaningless (CogSci 20). https://bura.brunel.ac.uk/bitstream/2438/2131/1/PT-Cogsci%20-%201998.pdf
- [V] Gobet and Clarkson (2004) Chunks in expert memory. https://bura.brunel.ac.uk/handle/2438/801
- [V] Gong, Ericsson and Moxley (2015) Recall of briefly presented chess positions. https://pmc.ncbi.nlm.nih.gov/articles/PMC4361603/
- [V] Sala and Gobet (2017) Meta-analysis, expert memory for random material. https://pmc.ncbi.nlm.nih.gov/articles/PMC5323477/
- [V] Cowan (2010) The magical mystery four. https://pmc.ncbi.nlm.nih.gov/articles/PMC2864034/
- [V] Gathercole et al. (2019) Can short-term memory be trained? (reports Ericsson, Chase and Faloon 1980). https://pmc.ncbi.nlm.nih.gov/articles/PMC6647533/
- [V] Wikipedia, Chunking (psychology), second-hand S.F. numbers. https://en.wikipedia.org/wiki/Chunking_(psychology)
- [V] Fingerprint expertise and visual STM (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC10951190/
- [V] Liu et al. (2025) Bridge experts. https://pmc.ncbi.nlm.nih.gov/articles/PMC11852315/
- [V] Expert brain, Nature Communications (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13454291/
- [V] Modelling working memory capacity, J Cognition (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11259112/
- [M] Ericsson, Chase and Faloon (1980) Science 208:1181 (primary blocked, 403).
- [M] Chase and Ericsson (1981), Charness (1976), Frey and Adesman (1976), Saariluoma (1984, 1989, 1991), Holding and Reynolds (1982), Cooke et al. (1993), Richman et al. (1996), Linhares and Brum, Bilalic and Gobet: known only as cited by the sources above.
- [M] Sala and Gobet listing. https://livrepository.liverpool.ac.uk/3004290/

Models
- [V] Bennett and Gobet (2025) CogAct. https://arxiv.org/abs/2512.18665
- [V] Sumers et al. (2024) CoALA. https://arxiv.org/abs/2309.02427
- [V] Ellis et al. (2020) DreamCoder. https://arxiv.org/abs/2006.08381
- [V] Grand et al. (2024) LILO. https://arxiv.org/abs/2310.19791

LLM and agent studies
- [V] Pleiss, Schiffer, von Weizsaecker (2026) chess generalisation vs memorisation. https://arxiv.org/abs/2601.16823
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Berlot-Attwell et al. (2024) Library learning doesn't. https://arxiv.org/abs/2410.20274
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (b25 was abstract only; c13 and c14 read the text)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Gong et al. (2023/24) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731 (abstract and partial text)
- [V] Karvonen (2024) Chess language models. https://arxiv.org/abs/2403.15498
- [V] Wenliang et al. (2024) Amortized planning. https://arxiv.org/abs/2402.04494
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/pdf/2509.25140
- [V] Lei et al. (2026) SkillEvolBench. https://arxiv.org/abs/2605.24117
- [V] Yu et al. (2026) SkillLens. https://arxiv.org/pdf/2605.08386
- [V] Yu et al. (2026) MASA, skill granularity. https://arxiv.org/pdf/2605.30723
- [V] He et al. (2026) SkillMigrator. https://arxiv.org/pdf/2606.17645
- [V] Hu et al. (2026) SELM. https://arxiv.org/pdf/2610.24630
- [M] Wang et al. (2025) ASI. https://arxiv.org/abs/2504.06821 (abstract only)
- [M] Zheng et al. (2025) SkillWeaver. https://arxiv.org/abs/2504.07079 (abstract only)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 9 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A10.03-K10** (reworded: the sources support less). Fingerprint numbers (d=1.76, 44+44) and bridge suit-grouping are verified, but bridge is itself a game and the music r=.69 is a random-material skill effect that Sala and Gobet call an empirical anomaly probably due to less random music stimuli. Corrected claim: The expert memory advantage for domain material is not limited to chess: fingerprint examiners beat matched novices on visual short-term memory for prints (d=1.76, 44 vs 44), bridge experts' hand memory depends on grouping cards by suit, and the random-material skill effect also appears in programming (r=.36) and music (r=.69, though Sala and Gobet treat the music value as an anomaly probably due to less random stimuli).
- **A10.03-K07** (now single-source: only one opened source, code check).
