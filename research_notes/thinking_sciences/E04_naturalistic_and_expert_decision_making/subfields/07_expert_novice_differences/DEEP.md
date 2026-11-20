# Expert-novice differences: deep document

*Subfield E04.07. Focus: chunks and cues (de Groot; Chase and Simon 1973). Evidence ids a01-a29, b01-b28, c01-c28, d01-d16 are in evidence_a-d.jsonl. Claim ids K01-K24 are in claims.jsonl (full id E04.07-Kxx). Corrections are in critique.md. Sources not opened are marked so; numbers from them are second-hand.*

## 1. What it is

This subfield asks one question. What do experts have that novices lack, and can a language-model agent get it through a scaffold, with no training?

The founding answer is from de Groot (1946, 1965) and Chase and Simon (1973). Experts do not think deeper or search more. They see more. After a few seconds they recall a real chess position almost perfectly (about 93 percent for the best players, about 25 pieces). On the same pieces shuffled at random, the gap shrinks to a small residual. The explanation is chunking: experts hold a very large store of familiar patterns (chunks), and a glance at a real position retrieves a few big chunks that cover many pieces.

Three ideas matter for us.

1. **Skill is mostly a store of domain patterns plus fast retrieval.** It is not general memory span and not mainly general intelligence.
2. **Retrieval is cue-driven and specific.** A chunk fires on exact surface features (which piece on which square). Small layout changes hurt even experts.
3. **Search is secondary.** Experts get a good first candidate from recognition and then search a little.

For the agent this maps to: a library of verified domain cases, indexed retrieval with slots, a cheap first pass to find salient structure, a small search budget, and code-side checks when the input is unfamiliar (pattern knowledge fails there, in humans and in models).

What the field has not done: run the classic recall test on an LLM, measure chunk size in an LLM, or show that a retrieval library beats plain reasoning at equal tokens with a size curve. Nearly all LLM evidence is chess (K11, K22, K23).

## 2. History and theories in depth

**de Groot (1946/1965).** Thought and Choice in Chess. Read here only through secondary reports (a06). He found no gross difference between masters and weaker players in number of moves considered, depth or heuristics. The difference was in which moves came to mind and in recall of briefly shown positions (2 to 15 s view). Best players: about 93 percent correct on about 25 pieces. The 2011 replication (Connors, Burns, Campitelli; d13, abstract only; 6 GMs, 5 IMs, 6 Experts, 5 Class A; two positions each) kept the pattern-recognition conclusion. GMs and IMs searched faster than weaker players, and all searched faster than in earlier studies. So "no difference in search" is revised for speed, not for depth.

**Chase and Simon (1973), Perception in Chess (a01-a05).** Three players (master, Class A, beginner) rebuilt 20 game positions after a 5 s view, with repeated trials. Chunks were defined two ways: in a copy task, one glance is one chunk; in a memory task, a gap of 2 s or more between placed pieces marks a boundary. Pieces inside a chunk share relations (attack, defence, adjacency, same colour, same type); pawn chains were clearest. Random positions: no link between skill and recall. The master did no better on positions he recognised in 1 s (83 vs 79 percent). Chunk size was about 2.5 pieces (master) and 2.1 (Class A). Weaknesses: N=3, the master was rusty, positions were non-quiet, a physical board limited hand grasp (b05, b19).

**Simon and Chase (1973), Skill in Chess (a07).** Popular statement: short-term memory holds about 7 chunks, a new chunk takes about 5 s to learn, a master needs a large repertoire (the 50,000 figure traces to Simon and Gilmartin 1973).

**Challenges to pure chunking (a08, b09).** Interference studies (Charness 1976: only 6-8 percent loss after a 30 s delay; Bradley 1987: visuospatial load cut recall by more than two thirds); level-of-processing studies (confounded with viewing time); blindfold and multi-board play (recall far above 7 chunks).

**Rival accounts.** Long-term working memory (Ericsson and Kintsch 1995, b28, not opened): skilled memory uses retrieval structures, so working memory is effectively larger. Gobet implemented it (2000) and got recall from 10 to 100 percent depending on parameters, so the verbal theory was nearly unfalsifiable (a20). Constraint attunement (Vicente and Wang 1998, b27, not opened): the expert advantage depends on domain structure and should vanish on truly random material. Search accounts (Holding and Reynolds 1982: random recall did not correlate with skill, quality of move search did; b06).

**Template theory (Gobet and Simon 1996; a08, a12, b08).** Big frequent chunks become templates: a fixed core of about 12 pieces plus slots (pieces, squares, opening, plan, move) with links to other templates. Filling a slot takes under 1 s (250 ms in CHREST). A new chunk takes about 8 s. This explains multi-board recall. A random position rarely evokes templates, so the master edge shrinks but does not vanish.

**CHREST and EPAM (a14, a19, c14, a20).** CHREST learns a discrimination net from 20 random fixations. Recall = a + b log(nodes), over 98 percent of variance across four position types; nets grew to 70,000 nodes. It predicted a small skill effect on random positions, later confirmed (Gobet and Waters 2003). EPAM IV added retrieval structures and reproduced a digit-span expert (DD) at 104 digits after about 865 sessions.

**Later lines.** Skill and intelligence: weak link (Burgoyne 2016, b12, b13). Deliberate practice: large but limited share of variance (Macnamara 2014; Ericsson 2019; b17, b18, K09). Eye movements: experts fixate half as often (a22, b15). LLM era (2022-2026): state tracking in small GPTs (c09, c10), emergent board models (a26, c06-c08), amortised planning (a25, c12), distribution-shift collapse (a28, c01-c04), persona nulls (b25, d09, d10), agent memory libraries (a29, c24, d01-d04).

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single = one source; contested = sources disagree.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Experts recall real positions far better | Best players about 93% on about 25 pieces (de Groot, second-hand). Masters 92.3% vs Experts 64.5% on one game position. Game recall: GMs 83.7%, masters/experts 61.3%, Class A/B 55.1%, Class C/D 40.1% | a06, a10, a16, K01 | established |
| Chase-Simon first-trial recall (N=3) | Middle game: M about 16, A about 8, B about 4 pieces. Quiet positions, single 5 s trial: B/A/M 33/49/81% vs 18/34/62% on the first set | a01, a02 | established (small N) |
| Gap shrinks on random positions, does not vanish | Chase-Simon: no skill effect (Master 2.0 vs novice 3.0 pieces). Re-analysis of 13 experiments: stronger players recall more on random boards. Random recall: GMs 18.3, 17.0, 14.1, 12.3%; fully random 14.8, 16.3, 13.7, 12.0%. Fully random r=.34, slope 0.052 per rating point (about 5.2% per 100 points) | a03, b04, a15, a16, K02 | established |
| Game vs random contrast, one study | N=25. Game vs random F(1,22)=291.51; skill x type F(2,22)=16.50; skill effect on random alone F(2,22)=0.18, ns | b01 | established (low power) |
| Mirror and layout changes hurt recall | Masters 77.3 / Experts 49.7 / Class A 34.5% (normal, horizontal) vs 62.9 / 38.6 / 27.5% (vertical, central). Mean drop 10.3% humans vs 11.4% CHREST. No condition fell to random level | a13, b02 | single |
| Largest chunk grows with skill on game positions only | Game: Masters 11.2, Experts 7.4, Class A 6.2 pieces. Random: 4.1, 4.3, 4.1. Rating vs largest chunk: r=.60 game, .15 random (25 rated, 25 non-players) | b03, b14 | established |
| Chunks per recall are few but big | Fewer than 3 chunks in most conditions; random 1.3-2.1; Masters up to 15 pieces on screen. Multi-board: 2.3 chunks (one board) to 9.9 (five boards) | a09, a18, b07, K03 | established |
| Chunk size and count depend on method | Chunk size 2.5/2.1 (1973), 3.6/2.7 (Freyhoff), 11.2 (1996), up to 15 (2004). Test-retest of chunk count: .65 (repeated recall) vs .36 (timing) on game positions, about .14 random | b05, a18, d11, K21 | contested |
| Multi-board recall needs retrieval structures | 3 Masters: 95% (1 board) to 39% (5 boards). At 10 s gap, four boards (100 pieces): Masters 82.9 pieces, Experts 44.9. Gain 1 s to 10 s: Masters 71% (2 boards), Experts 40%. Chessmaster, about 150 sessions: 160+ pieces on 9-10 boards | a09, a10, a11, b08, K05 | established |
| Time budget helps experts differently | Masters reach ceiling after about 3 s; weaker players improve over 60 s. Masters' chunk count 4.5 at 10 s, 2.9 at 60 s. CHREST: 50 ms to STM, 250 ms template slot, 8 s new chunk | a17, b26 | single (b26 not opened) |
| Store size | 50,000 (Simon and Gilmartin; CHREST 70,000 nodes); 10,000-100,000 vs 300,000 (Gobet and Simon 2000); direct archival count about 100,000 opening moves (76,562 games) | a07, a14, b16, d12, K04 | contested |
| Recall follows log of store size | Recall = a + b log(nodes), over 98% of variance across four position types (simulation) | a14 | single (model only) |
| Random-material skill effect across domains | r=.41 [.29,.51], k=28, I2=63%. Games .42 (k=11), music .69 (k=5), programming .36 (k=6), sports .30 (ns), other .24 (ns). Trim-and-fill r=.29 [.17,.41]. Domain p=.069 (a21) or .116 (b11, k=26); exposure time p=.420 | a21, b10, b11, K06 | single (one meta-analysis) |
| Eye movements | 24 players. Time 11.7 vs 23.4 s; correct 4.75 vs 3.33 of 5; fixations 44.3 vs 83.6; duration 253 vs 244 ms (ns); on salient pieces .80 vs .64 | a22, b15, K07 | single |
| Intelligence matters modestly | Gf r=.24, Gc .22, Gsm .25, Gs .24. Youth .32 vs adult .11. Higher-rated samples r=-.10 vs lower-rated .10 (ns, p=.159) | b12, b13, a23, K08 | established |
| Deliberate practice share of variance | Games 26%, music 21%, sports 18%, education 4%, professions under 1%, overall 14%. Ericsson strict re-analysis: 29% and 61% after attenuation correction | b17, b18, K09 | contested |
| Expertise reversal | 176 effect sizes, 60 experiments, 5,924 participants. Low-knowledge learners gain from high assistance d=0.505; high-knowledge do better with low assistance d=-0.428 | b20 (abstract only), K10 | single |
| LLM skill collapses off-distribution (chess) | 500 positions per condition. ACPL GPT-3.5 807.97, GPT-4o 540.38, GPT-5 463.5 (illegal = 1000). GPT-5 familiar CPL 26.19. Legal-move rate 25.3 / 58.4 / 66.2%. Illegal on OOD: GPT-3.5 74.7%, GPT-4o 41.6%, GPT-5 33.8%. Claude Opus ACPL 14.0 / 207.2 / 728.6; Gemini 34.8 / 434.1 / 829.7 | a28, b21, c01, c02, K11 | single (one preprint) |
| Reasoning tokens help least where priors are sparse | Reasoning cut ACPL 71.74%. Per-token relative gain 22.55% (familiar), 7.23% (near), 3.81% (OOD). GPT-5 tokens 3,426 / 11,800 / 16,953; gain per token 9.9e-4, 4.92e-4, 1.13e-4. Still above 10% illegal OOD | c03, d05, b22, K12 | single |
| Scale helps familiar positions most | ACPL improvement GPT-3.5 to 4o: 70.7% (familiar), 35.16% (near), 9.08% (OOD); 4o to 5: 69.92%, 10.77%, 5.73% | c04 | single |
| Search-free transformer plays at expert level | 270M: puzzles 95.4%, blitz Elo 2895 vs humans, tournament Elo 2299 vs bots (GPT-3.5-turbo-instruct 1755, same column; puzzle 66.5%). 9M: 88.9% puzzles; 136M: 94.5%. Only 1.33% puzzle overlap with training | a25, b23, c12, K13 | single |
| Chess GPT holds a board and a skill estimate | Legal moves 99.8% (16 layer), 99.6% (8 layer); win vs Stockfish level 0 64% / 46% (text). Probes: square 99.6%, Elo 90.5%. Intervention 92.0% legal vs about 41%. Random-start boards (5,000 games; standard board 69.6%/49.6%, a different sample): win rate 16.7% to 43.2% with skill vector | a26, b24, c06-c08, K14 | single |
| Persona role labels do not help | 162 personas, 2,410 MMLU questions: no gain. Six models, GPQA Diamond (4,950 runs per model-prompt) and MMLU-Pro (7,500): no expert gain, nine significant negatives. 1,140 open questions: baseline 4.390 vs retrieval 4.382, all d under 0.12 | b25, d09, d10, K15 | established (role labels only) |
| LLM simulating novices is miscalibrated | Cosine .16-.19; calibration bias +.325 to +.468; AUC .528. GPT-4 94.8% on grade-school maths, 61.7% at choosing a misconception-linked wrong option | c17, c18, c19, K16 | established |
| Hierarchical memory and skill libraries help agents | HiAgent success 42 vs 21%, steps down 3.8. Voyager 63 items, 3.3x baselines, diamond only for Voyager; 3/3 vs 0/3 on zero-shot new tasks | a29, c24, K17 | established |
| Memory needs a quality gate | Add-all vs fixed 100 records: RegAgent 55.48 vs 67.53; EHRAgent 13.05 vs 16.75; AgentDriver 32.32 vs 40.11; CIC-IoT 59.90 vs 71.50. Strict addition: 70.95, 38.50, 51.00, 85.40. ExpeL 28.0 to 39.0 on HotpotQA | d02, d03, d01, K20 | established |
| Scaffold uplift tracks headroom | GPT-5.4-mini 0.488 to 0.750 (+0.262); Gemini-3.5-flash 0.761 to 0.871 (+0.110); r=0.75; strong target regressed in 9/20 builder-benchmark cases. GSM8K N=1,317 GPT-5: 94.00 / 96.36 / 94.00 (zero-shot / CoT / constrained) | d07, d08, K19 | single |
| Many-shot examples peak then decline | MATH peaks near 125 shots; XSum near 50; reinforced ICL plateaus near 25 (+5%); Bemba +15.3% at 997 examples; repeating 25 examples to 1,000 nearly flat | d04 | single |
| LLM chess with agents | Reasoning models average win 45.4% vs a random opponent; instruction errors 71.9% (non-reasoning) vs 24.4%; best Elo estimate about 758 | c11, K18 | contested |
| LLM working-memory limit | n-back d' falls to about 1 at n=3 for ChatGPT; GPT-4 far above open models | c16 | single |

## 4. Mechanisms and models

### 4.1 Chunking (Chase and Simon, EPAM, CHREST)
A chunk is a long-term-memory node standing for a group of items that co-occur. Working memory holds labels (pointers) to chunks, not the items.

Implementable version:
- Input is a set of items with relations (attacks, supports, depends-on, same-type).
- A discrimination net sorts each item (or item group) down tests until it reaches a node. Learning adds a test or child node when an item does not fit. (Humans pay about 8 s per new node; an agent does not need this cost.)
- Recall of a new input = the items covered by the few chunks retrieved at the first look, plus guesses.
- Size law: recall grows with log of node count (a14). Diminishing returns.
- Chunk boundary test (for analysis): relations inside a chunk are dense (74.6 percent of within-chunk pairs shared 3 or more relations; near chance across boundaries; b05).

### 4.2 Templates (Gobet and Simon 1996)
A template is a chunk with a core and slots. Engineer reading: a record type with fixed fields (the core, about 12 items) and typed slots filled at read time (under 1 s each). Templates link, so retrieval can hop. This explains up to about 160 pieces over 9 boards: each board is bound to a template, not stored piece by piece.

### 4.3 Retrieval structures (EPAM IV, the Chessmaster; a11, a19)
An explicit index with stable cues. The Chessmaster used 13 world champions as cue slots, each tied to a board. DD's digit structure had four levels (digits, chunks, supergroups, clusters), leaves holding 3-4 digits. Capacity grew over 150 sessions (chess) and 865 sessions (digits), not by a larger buffer. Plateau near 123 pieces in the multi-board task. Agent version: a code-held state file with named slots; the model fills a slot, code reads and writes it. Bounded notes per slot.

### 4.4 Cue-based first pass (eye movements, a22)
Experts use fewer, longer fixations and look at relevant pieces and empty squares (configuration, not single pieces). Agent version: one cheap pass over the whole input that tags salient structure (code or short model call) before detailed reasoning. Untested on an agent (K07, single-source).

### 4.5 Pattern store feeding search (a06, b06)
Recognition proposes candidates; a small search checks them. de Groot and Connors support this. Agent version: retrieve the top few similar verified cases, use them as first candidates, test in code (S4), keep search shallow.

### 4.6 Experience-following (d02)
Agents copy the output of the most similar stored case (Pearson r near 1 between input and output similarity in RegAgent). This is the LLM analogue of cue-driven retrieval, with a risk: a wrong stored case is copied. So admission needs a gate (verified only) and some deletion helps (EHRAgent 42.06 at 784 records vs 38.67 at 1,012).

### 4.7 Distribution-shift failure (Pleiss, a28; Karvonen, c07)
Skill depends on how much the input looks like training data. On random boards the chess GPT reads the game as a weak player (its Elo probe labelled 99.4 percent of 4,000 random-start games low skill) and plays weaker; a skill vector restores part of it. Pleiss: more reasoning gives less per token as priors thin. Implication: detect unfamiliarity and shift weight to external checks and retrieved precedent.

### 4.8 Expertise reversal (b20, d07, d08)
Guidance that helps novices costs experts. Agent version: scaffold strength as a function of the model's baseline pass rate on the task class (this is S0 GATE). Evidence is indirect and small.

## 5. What holds up

**Replications and meta-analyses.**
- de Groot's recall result: replicated by Chase and Simon on quiet positions (a02, within-paper, not independent), Gobet and Simon 1998 (b05; chunk structure and the 2 s rule with computer display and more players), and Connors 2011 (d13, abstract only). Robust.
- Random-position effect: the Chase-Simon null (N=3) was wrong in detail. 13-experiment re-analysis (b04); Gobet and Waters, 36 players, r=.34 on fully random (a15); meta-analysis r=.41 across 28 effects (a21). After trim-and-fill r=.29, so publication bias may inflate it. The effect is small (about 5 percent per 100 rating points) but real.
- Templates predicted multi-board recall and the random-position effect; data confirmed both (a09, a15).
- Intelligence: weak link, stronger in youth, none in elite samples (b12, b13, a23).
- Persona labels: three independent nulls (b25, d09, d10).

**Failures and contested points.**
- Store size: 10,000 to 300,000, all indirect. d12 gives about 100,000 for opening moves, but those are rote sequences, not perceptual chunks.
- Chunks per recall: 7 (1973) vs under 3 (2004) vs Cowan's 4. Depends on the 2 s rule, display medium and hand grasp.
- Chunk-count reliability is low (.65 / .36 / about .14 random). Not a usable metric (K21).
- Fixation duration: de Groot and Gobet found shorter fixations for experts; Reingold et al. 2001 did not (a22).
- Long-term working memory theory: fits some data but nearly unfalsifiable as implemented (a20). Not closed.
- Interference studies and multi-board play show a fixed STM-chunk story is too narrow (a08).
- Deliberate practice share: contested between Macnamara and Ericsson (b17).
- LLM chess: a Elo 758 estimate for prompted reasoning models (c11) vs 2895 blitz for a search-free transformer trained on 15 billion engine labels (a25). Different regimes (prompting vs training).

**Moderators.**
- Typicality of stimuli (a02): non-quiet positions cut master scores (62 vs 81 percent).
- Domain: games .42, music .69, programming .36, sports ns (a21); moderator test not significant (p=.069 or .116).
- Exposure time: not significant in the meta-analysis, but masters saturate near 3 s while weaker players gain to 60 s (a17).
- Skill range: intelligence matters in youth and lower-skill samples, not in elite samples.
- Display and method change chunk size (b05, a18).

**Interventions that worked (humans).** Long structured practice built a retrieval structure (Chessmaster, DD). More time between boards helped masters far more than experts (71 vs 40 percent gain, a10).

**Interventions that did not work, or are untested.** Persona labels (section 6). Chunk count as a metric. Working-memory training transfer is covered in a parallel subfield.

## 6. Language models

**Chess is the only domain with solid numbers.** No study re-runs the Chase-Simon recall test on an LLM, and none measures chunk size in LLMs (c25, c27, c28). Ciancarini and Pareschi 2026 (abstract only) mapped 84 study families and found LLM work centres on state representation and generalization.

**Familiar vs unfamiliar (Pleiss et al. 2026; a28, c01-c04, d05).** 500 positions per condition: familiar (at least 1,000 Lichess master occurrences), near (10 random moves per side), out-of-distribution (ten pieces per side at random). Quality falls with unfamiliarity. GPT-5 on familiar positions: CPL 26.19 (SD 49.53). On OOD no base model beats random. Illegal moves on OOD: 33.8 to 74.7 percent (GPT), 51.6 (Claude Opus), 72.0 (Gemini). Humans slow down but keep following rules (Reingold and Sheridan 2023, error under 1 percent in both notations; c05, second-hand). What changed it: reasoning cut ACPL 71.74 percent overall, but per-token gain falls from 22.55 to 7.23 to 3.81 percent; model upgrades improve familiar positions by about 70 percent but OOD by only 6 to 9 percent. Limits: one preprint with inconsistencies, GPT-heavy, no human baseline, OOD boards also change tactics, no scaffold arm.

**Internal state (Karvonen; a26, c06-c08).** A GPT trained on game text keeps a linear board and a skill estimate. Random starts read as low skill; a skill vector lifts win rate 16.7 to 43.2 percent. Small custom model. Jiao et al. 2026 (c13): a human-move model set to novice keeps the chess knowledge (concept probes stay accurate) but plays badly. Retraining a concept head lifts best-move accuracy in the lowest band from 14.4 to 82.8 percent; SAE steering to 42.7 percent. Not a prompt-level result.

**Amortised expertise (Ruoss; a25).** Search-free 270M model: blitz Elo 2895 vs humans; tournament Elo 2299 vs bots (9M and 136M give 2025 and 2259 in the first column; GPT-3.5-turbo-instruct 1755 is in the same column as 2299). QUEEN (c26, abstract only): a 4B LM joined to an expert encoder, Elo 1782 to 2697.

**Prompted LLM chess (c11).** Over 50 models vs a random opponent. Reasoning models win 45.4 percent on average; best Elo estimate about 758.

**Personas.** Role labels give no gain: 162 personas on 2,410 MMLU questions (b25); six models on GPQA Diamond and MMLU-Pro (d09); retrieved role prompts no better than none, 4.390 vs 4.382 (d10). Role plus domain facts: untested.

**Novice simulation.** LLMs are too coherent, wordy and confident (c17); GPT-4 is poor at choosing misconception-linked wrong answers (61.7 percent best zero-shot, c18); prompted novices drift into expert text and unlearning is needed (c19). A prompt does not remove knowledge.

**Working memory.** ChatGPT shows a human-like n-back limit that falls with noise (c16).

**Agent memory (the closest tests of a "store of chunks").**
- HiAgent (a29): subgoal summaries as chunks, success 42 vs 21 percent.
- Voyager (c24): skill library, 3.3x more items; without the library it is slower and less reliable.
- Decocted experience (d01): distilled lessons beat raw trajectories; an intermediate memory size can beat full memory. Figure only, no equal-token control.
- Memory management (d02): add-all hurts, verified-only helps (RegAgent 55.48 vs 70.95).
- ExpeL (d03): 28.0 to 39.0.
- Many-shot (d04): gains peak then decline in some tasks; not retrieval, not equal-token.
- No paper gives a token-matched curve of gain vs library size (K20: the gate is established, the log law is open).

**Scaffold headroom (d07, d08).** Uplift tracks headroom (r=0.75); a strong target regressed in 9 of 20 cases; full GPT-5 on GSM8K: constrained prompt 94.00 vs CoT 96.36. Both are preprints.

**Non-chess shuffle tests.** Scrambled Bench (d15): GPT-4 recovers 93.76 to 95.94 percent of letter-scrambled sentences; not an analogue (language is redundant). OrderProbe (d16): zero-shot exact recovery of reordered four-character CJK expressions only 12.167 to 31.062 percent, 62.238 with CoT. Chunks as an interpretability tool (c20, c21, c22): extracted from LLaMA3-8B activations; research tools, not scaffold steps. Synthetic CoT-mirage study (d06, abstract only): CoT breaks under distribution shift.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory. Evidence ids in parentheses.

### Add now (established)

1. **Retrieve verified cases, gate admission, and key on concrete surface features as well as abstract schema.** Memory / S2 / S3. [E] (K20: d01, d02, d03, d04; K17: a29, c24; K01: a01-a16; b02 for cue specificity). Admit a case only after a code check passes: strict addition beat add-all (RegAgent 70.95 vs 55.48), and a fixed 100-record memory beat 4,100 records (67.53). Allow deletion of low-value cases. Why: expert skill is a store, and agents copy the nearest stored case, so wrong cases get copied.
2. **Do not use persona or expert role labels.** G4 (already in the schema). [E] (K15: b25, d09, d10). Three independent studies show no accuracy gain. Real expertise must come from retrieved patterns and checks.
3. **Hold state in code, in named slots, with bounded content per slot.** Memory / S1 / O3. [E] (K03, K05, K17: a09, a11, a12, a18, b08, a29, c10). Working capacity is small (under 3 chunks) but units can be big and slot-filled. A window of the last 50 tokens loses board state (c10). HiAgent summaries of finished subgoals gave 42 vs 21 percent.
4. **Run rule and legality checks in code on every output, most of all on unfamiliar input.** G2 / G3 / S4. [E] for "code selects" (already in the schema); the LLM size of the problem is [S] (K11: c02). Illegal-move rate rose to 33.8-74.7 percent OOD while the rules stayed the same.
5. **Do not hard-code chunk counts or store sizes, and do not use chunk count as an agent metric.** Metric design. [C] on the numbers (K04); reliability finding [S] (K21: d11). Use accuracy gaps.
6. **Test expertise effects on typical, well-formed cases.** Bench design. [E] (a02: master 81 vs 62 percent depending on the position set).
7. **Spend by difficulty, not by length.** G11 / G12 (already there). Supported by c03: per-token gain falls from 22.55 to 3.81 percent as priors thin, so more tokens do not replace missing patterns. Evidence here is [S]; the schema rule itself is [E] from other fields.

### Test first

8. **Familiarity gate at S0 and a lighter scaffold on familiar problems.** S0 / G7. [S] (K10, K19: b20, d07, d08; K11: a28). Expertise reversal is a meta-analysis in humans (d=0.505 vs -0.428, abstract only). LLM evidence is two small preprints.
9. **Library size curve (log law) at equal tokens.** Memory. [C] (K04: a14 model only; d01 sweet spot; d04 peak then decline).
10. **Slot-filled templates vs raw notes for stored cases.** Memory / S1. [S] (K05: human evidence only).
11. **Cue-first salience pass before detailed reading.** S1 / O2. [S] (K07: a22, b15).
12. **Structure-level shuffle test to detect unfamiliar input.** S0 / G3. [C] (K22: d15, d16; K23: d05, d06).
13. **Expert-context cues paired with retrieved facts.** Memory / S1. [S] (K14: c07 latent skill estimate; c13 head retraining; role labels alone fail).
14. **Hierarchical subgoal summaries.** S1 / O3. [E] in the cited agent tasks (a29, c24); confirm at equal tokens on our bench.
15. **Precedent retrieval at impasses ahead of more reasoning tokens when the problem is unfamiliar.** S6 / O7. [S] (K12: c03, d05).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup, retrieval and checks counted, G7); at least 3 seeds; report the paired difference with a confidence interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with checks (code or maths); library size 0 / 10 / 100 / 1,000 | Plain vs retrieve-top-k at each size; admission add-all vs verified-only | Accuracy vs log size; slope; best size | Verified-only beats add-all by several points on near-duplicate classes; gain rises with log size then flattens or dips (K20, d01, d04) |
| T2 | Structured items (ordered proof steps, code lines, plan steps) vs the same items with steps shuffled | Plain vs scaffold, structured vs shuffled | Accuracy gap (structured minus shuffled) by model size | A gap exists and grows with model strength; mirrors the human recall gap (K22, K01) |
| T3 | Familiar vs novel items (split by similarity to the library or prior pass rate) | Plain, full scaffold, light scaffold | Accuracy per split; uplift vs baseline headroom | Full scaffold helps on novel, light wins on familiar; uplift correlates with headroom (r near .75 in d07) |
| T4 | Library cases re-presented with surface changes (paraphrase, reorder) | Retrieval keyed on surface only, abstract only, both | Retrieval hit rate; accuracy | Both-keyed wins; surface-only drops on reorder (a13: 10.3 percent human drop) |
| T5 | OOD items with a code legality or format check | Plain, plain plus check, scaffold plus check | Invalid-output rate; accuracy | Check drives invalid rate toward zero; gain larger OOD than in-distribution (K11, c02) |
| T6 | Open questions needing domain facts | Plain, role label only, role plus retrieved facts, facts only | Accuracy or rubric score | Role label alone equals plain (d09, d10); facts-only about equals role plus facts |
| T7 | Long multi-step tasks | Flat history vs closed-subgoal summaries with on-demand recall | Success; steps; tokens | Gain largest when baseline success is low (a29: 42 vs 21 percent) |
| T8 | Items with mixed salient and irrelevant detail | One-line salience pass then solve vs direct solve | Accuracy; tokens to correct | Equal or faster; likely no gain on easy items (K07) |
| T9 | Any chunk-like metric, 5 reruns on the same items | Same arm repeated | Test-retest r | Expect under .65 (d11); if so, drop the metric |

## 9. What does not transfer, and why

- **Short-term memory span and 7 plus or minus 2.** An LLM has a context window and degraded recall, not a 7-slot buffer. ChatGPT n-back falls to d' of about 1 at n=3 (c16), but that measures updating, not chunking.
- **Chunk count and timing measures.** Pause rules and glance counts have no agent equivalent; reliability is low even in humans (.65 / .36).
- **Chess as a model of reasoning.** Perfect information, closed rules, a huge corpus. All LLM numbers are chess, and Pleiss's OOD positions are tactical and unnatural (a28). Open tasks may behave differently (K23).
- **Time to build chunks.** Humans need about 8 s per chunk and thousands of hours. The agent loads a verified library in seconds; the constraint is library quality.
- **Persona as expertise.** A label does not install patterns (b25, d09, d10).
- **Matching novice behaviour.** LLMs cannot reliably play a novice (c17, c18, c19); not core to our agent.
- **Search-free play from training.** The 270M model used 15 billion labels (a25); we are not training.
- **Interpretability chunking (c20, c21).** Research tools on small models; not a scaffold step.
- **Eye movements.** Visual salience is not text salience; a salience pass is an analogy only.
- **Deliberate practice effect sizes.** Not testable on the agent (K09).

## 10. Open questions

1. Does a retrieved library of verified cases improve accuracy at equal tokens, and what is the size curve (log, plateau or peak)? No token-matched curve exists (K20).
2. Does OOD collapse appear outside chess, and does a scaffold narrow it (K23)?
3. Does an LLM show the human game-vs-random recall gap on structured text, and how large (K22)? No one has run the classic recall test on LLMs (c27).
4. Should scaffold strength fall when a task is familiar (K19)? Evidence is two small preprints and an abstract-only human meta-analysis.
5. Does persona plus domain facts help when role labels alone do not (K15)?
6. Is the true chunk count nearer 3, 4 or 7, and is the store 50,000 or 300,000 (K03, K04)? Method-dependent.
7. Is there a prompt-level analogue of Karvonen's skill vector and Jiao's head retraining (K14)?
8. Does core-plus-slots template memory beat raw notes for LLMs?
9. Can a retrieval structure of named cue slots extend an LLM's effective capacity as it did for the Chessmaster (a11)?
10. Do the abstract-only sources (b20, d13, c26, c22, d06, c25) change any answer? The expertise reversal meta-analysis (b20) matters most.

## 11. Sources

[V] = opened (full text or page read). [M] = snippet or abstract only.

**Founding and chunk theory**
- [V] Chase and Simon (1973) Perception in Chess. https://www.gwern.net/doc/psychology/chess/1973-chase.pdf (a01-a05)
- [M] Chase and Simon (1973), DOI page. https://doi.org/10.1016/0010-0285(73)90004-2 (b19, c27; numbers from opened secondary papers)
- [M] de Groot (1946/1965) Thought and Choice in Chess; book not opened, read through Chase and Simon and Charness et al. 2001. https://www.gwern.net/doc/psychology/chess/1973-chase.pdf (a06)
- [V] Simon and Chase (1973) Skill in Chess. https://www.gwern.net/doc/psychology/chess/1973-simon.pdf (a07; scan partly scrambled)
- [V] Gobet and Simon (1996) Templates in chess memory. https://www.gwern.net/doc/psychology/chess/1996-gobet.pdf (a08-a12)
- [V] Gobet and Simon (1996) Templates in chess memory: a mechanism for recalling several boards. http://bura.brunel.ac.uk/bitstream/2438/1339/1/Multiple_boards.pdf (b08)
- [V] Gobet and Simon (1996) Recall of random and distorted chess positions. https://www.gwern.net/doc/psychology/chess/1996-gobet-2.pdf and https://link.springer.com/content/pdf/10.3758/BF03200937.pdf (a13, a14, b01-b03)
- [V] Gobet and Simon (1996) Recall of rapidly presented random chess positions is a function of skill. https://link.springer.com/content/pdf/10.3758/BF03212414.pdf (b04)
- [V] Gobet and Simon (1998) Expert chess memory: revisiting the chunking hypothesis. http://bura.brunel.ac.uk/bitstream/2438/1343/1/Copy-Task-NEW-BJP.pdf (b05, b06)
- [V] Gobet (1998) Expert memory: a comparison of four theories. http://bura.brunel.ac.uk/bitstream/2438/815/1/FullText.pdf (b09)
- [V] Gobet and Waters (2003) The role of constraints in expert memory. http://bura.brunel.ac.uk/bitstream/2438/803/1/GobetWatersChessMemoryJEPLMC-R2.pdf (a15, a16)
- [V] Gobet and Simon (2000) Five seconds or sixty? http://bura.brunel.ac.uk/bitstream/2438/811/1/Five%20Seconds%20or%20Sixty%20.pdf (a17); [M] https://doi.org/10.1207/s15516709cog2403_4 (b26)
- [V] Gobet and Clarkson (2004) Chunks in expert memory. http://bura.brunel.ac.uk/bitstream/2438/801/1/GobetClarkson.pdf (a18, b07)
- [V] Richman, Staszewski and Simon (1995) EPAM IV. https://www.gwern.net/doc/psychology/chess/1995-richman.pdf (a19)
- [V] Gobet, Lane and Lloyd-Kelly (2015) Chunks, schemata and retrieval structures. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4657374/fullTextXML and https://doi.org/10.3389/fpsyg.2015.01785 (a20, c14, c15)
- [V] Gong, Ericsson and Moxley (2015) Recall of briefly presented chess positions. https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0118756&type=printable (b14, d11)
- [V] Chassy and Gobet (2011) Measuring chess experts' single-use sequence knowledge. https://pmc.ncbi.nlm.nih.gov/articles/PMC3217924 (d12)
- [M] Vicente and Wang (1998) Constraint attunement thesis. https://doi.org/10.1037/0033-295X.105.1.33 (b27)
- [M] Ericsson and Kintsch (1995) Long-term working memory. https://doi.org/10.1037/0033-295X.102.2.211 (b28)

**Meta-analyses and individual differences**
- [V] Sala and Gobet (2017) random-material meta-analysis. https://link.springer.com/content/pdf/10.3758/s13421-016-0663-2.pdf (a21, b10, b11)
- [V] Charness, Reingold, Pomplun and Stampe (2001) eye movements. https://link.springer.com/content/pdf/10.3758/BF03206384.pdf (a22, b15, b16)
- [V] Bilalic, McLeod and Gobet (2007) Does chess need intelligence? http://bura.brunel.ac.uk/bitstream/2438/642/1/Does%20Chess%20Need%20Intelligence-revision-finalINT.pdf (a23)
- [V] Burgoyne et al. (2016) cognitive ability and chess skill. http://eprints.lse.ac.uk/102241/1/INTELL_2016_117_The_Relationship_between_Cognitive_Ability_and_Chess_Skill_a_Comprehensive_Meta_Analysis.pdf (b12, b13)
- [V] Ericsson (2019) Deliberate practice and proposed limits. https://www.frontiersin.org/articles/10.3389/fpsyg.2019.02396/pdf (b17)
- [M] Macnamara, Hambrick and Oswald (2014). https://doi.org/10.1177/0956797614535810 (b18)
- [M] Expertise reversal meta-analysis (2025). https://doi.org/10.1016/j.learninstruc.2025.102142 (b20)
- [M] Connors, Burns and Campitelli (2011). https://doi.org/10.1111/j.1551-6709.2011.01196.x (a24, d13)
- [M] McGrath et al. (2022) AlphaZero, abstract page. https://arxiv.org/abs/2111.09259 (a27); [V] full text https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706 (d14)
- [M] Reingold and Sheridan (2023), via Pleiss appendix C.7. https://arxiv.org/abs/2601.16823 (c05)

**Language models and agents**
- [V] Pleiss, Schiffer and von Weizsaecker (2026) Trapped in the past? https://arxiv.org/html/2601.16823v1 and https://arxiv.org/pdf/2601.16823 (a28, b21, b22, c01-c04, d05)
- [V] Ruoss et al. (2024) Amortized planning. https://arxiv.org/pdf/2402.04494 (a25, b23, c12)
- [V] Karvonen (2024) Emergent world models in chess LMs. https://arxiv.org/pdf/2403.15498 (a26, b24, c06-c08)
- [V] Toshniwal et al. (2022) Chess as a testbed for LM state tracking. https://doi.org/10.1609/aaai.v36i10.21390 (c09, c10)
- [V] Kolasani et al. (2025) LLM CHESS. https://arxiv.org/abs/2512.01992 (c11)
- [V] Jiao et al. (2026) Playing dumb. https://arxiv.org/abs/2611.03439 (c13)
- [V] Gong, Wan and Wang (2024) Working memory capacity of ChatGPT. https://arxiv.org/abs/2305.03731 (c16)
- [V] Borchers et al. (2026) LLMs as students who think aloud. https://arxiv.org/abs/2602.01015 (c17)
- [V] Liu et al. (2023) Novice learner and expert tutor. https://arxiv.org/abs/2310.02439 (c18)
- [V] Song, Guo and Lin (2026) Simulating novice students. https://arxiv.org/abs/2603.26142 (c19)
- [V] Wu et al. (2025) Discovering chunks in neural embeddings. https://arxiv.org/abs/2502.01803 (c20); [V] Concept-guided interpretability via neural chunking. https://arxiv.org/abs/2505.11576 (c21)
- [M] Zhong et al. (2026) Semantic chunking and the entropy of language. https://arxiv.org/abs/2602.13194 (c22)
- [V] Sumers et al. (2023) CoALA. https://arxiv.org/abs/2309.02427 (c23)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (c24)
- [M] Ciancarini and Pareschi (2026) chess mapping. https://arxiv.org/abs/2609.18286 (c25)
- [M] Bhaskar et al. (2026) QUEEN. https://arxiv.org/abs/2610.03695 (c26)
- [V] Hu et al. (2024) HiAgent. https://arxiv.org/pdf/2408.09559 (a29)
- [V] Zheng et al. (2024) Personas in system prompts. https://arxiv.org/pdf/2311.10054 (b25)
- [V] Basil et al. (2025) Playing pretend. https://arxiv.org/pdf/2512.05858 (d09)
- [V] Xiao et al. (2026) When does persona prompting help? https://arxiv.org/pdf/2605.29420 (d10)
- [V] Shen et al. (2026) Decocted experience. https://arxiv.org/html/2604.04373v1 (d01)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/html/2505.16067v2 (d02)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/html/2308.10144v3 (d03)
- [V] Agarwal et al. (2024) Many-shot in-context learning. https://arxiv.org/html/2404.11018v3 (d04)
- [M] Zhao et al. (2025) Is chain-of-thought a mirage? https://arxiv.org/abs/2508.01191 (d06)
- [V] Qian et al. (2026) AI4AI at test time. https://arxiv.org/pdf/2608.12307 (d07)
- [V] The Prompting Inversion (2025). https://arxiv.org/html/2510.22251v1 (d08)
- [V] Scrambled Bench (2023). https://arxiv.org/html/2311.18805v1 (d15)
- [V] OrderProbe (2026). https://arxiv.org/html/2601.08626v2 (d16)
