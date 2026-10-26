# Library learning (DreamCoder, LILO and successors): deep document

*Subfield C03.03. Built from evidence_a to evidence_d.jsonl (ids a01 to d23), claims.jsonl (C03.03-K01 to K33) and critique.md in this folder. Corrections from the critique are applied. Where two sources disagree, both are shown.*

## 1. What it is

Library learning means this: a solver keeps a growing set of reusable pieces (functions, lemmas, skills, workflows) taken from problems it already solved. New problems are then solved with those pieces instead of from bare primitives.

Three parts recur in every system:

1. **Wake.** Try to solve tasks with the current library. Keep what a check says is correct.
2. **Compress (abstraction sleep).** Look across the kept solutions. Pull out the parts that repeat. Turn them into named, parameterised helpers. Add them to the library.
3. **Guide.** Learn which helper to try on which problem. In DreamCoder this is a neural recognition model trained on "dreams". In LLM systems it is retrieval plus the model's own judgement.

Why we care. Our schema (SCHEMA.md section 5) has a planned "subgoal library": solved subgoals kept as reusable rules or helper programs, offered by similarity. It is marked [D], a design choice with no evidence. This subfield is the evidence base for that slot. It also touches S9 (look back, one lesson line), S0 (class record), S3 (grounding attempts in retrieved material) and guardrails G3 (verify on something unfitted), G5 (code selects), G7 (pay for itself) and G4 (samples are not independent).

The short answer from the research, stated up front:

- On program-synthesis domains with strong reuse and exact checks, library learning gives very large gains (text editing 3.7% to 79.6%). All of that comes from one research group.
- In LLM-era systems the gains are smaller, uneven, and often explained by something else: more samples, self-correction, or simply showing past verified solutions.
- Independent compute-matched re-tests of two famous LLM library systems (TroVE, LEGO-Prover) found the gain gone or reversed.
- What does survive across several independent sources: verify before storing, keep the store small and pruned, give items readable names and descriptions, retrieve with more than a single embedding, and always compare with a plain resampling arm at equal tokens.

## 2. History and theories in depth

### 2.1 Roots: EC2 (2018) and the idea of learned expertise

EC2 (Ellis, Morales, Sable-Meyer, Solar-Lezama, Tenenbaum, NeurIPS 2018) was the predecessor of DreamCoder. It learned a domain-specific language while training a neural network to guide search, tested on list functions, text editing and symbolic regression (a34, abstract only read). It set the pairing that all later work keeps: a library (what can be said) plus a guide (what to try first).

A human side exists too. Wong et al. (2022) had people describe about 2,000 generated objects. Treating naming as a search over program libraries, human lexicons favoured concise descriptions of each object while keeping the lexicon small (a35, abstract only). That is the same trade the compression objective makes: description length of the library against description length of the solutions. This paper also produced the 2D CAD benchmark that Stitch later used.

### 2.2 DreamCoder (Ellis et al., 2020/2021)

DreamCoder (a01 to a11, b01 to b03, c01, c02, c27) is the core theory. Its claim: expertise is a library of symbolic concepts (a prior over programs) plus a neural recognition model that guides search. Both are learned by alternating three phases.

- **Wake.** Enumerate programs from the library, guided by the recognition net, until one fits each task's examples.
- **Sleep, abstraction.** Choose library additions that minimise the description length of the library plus the description length of the refactored solutions found in waking. The search is over lambda-calculus refactorings, bounded by 3 beta-reduction steps. About 10^14 refactorings in the "map" example are held in a version space of about 10^6 nodes, built in minutes (a02). This compresses reused semantic patterns, not only repeated syntax.
- **Sleep, dreaming.** Draw random programs from the library prior, run them to make fantasy tasks, and train the recognition net to predict the programs. Replays of real solved tasks keep it grounded. Fantasies are called critical for data efficiency (a03).

Framed as Bayesian inference: the library is the prior, the recognition net approximates the posterior.

Domains: list processing, text editing, LOGO graphics, towers, regular expressions, symbolic regression, physics laws, recursive functions. Training sets are 100 to 200 tasks per domain. Each domain starts from a hand-built core (control flow, higher-order functions, types).

Key results (exact numbers in section 3). The library depth correlates with solve rate (r = 0.79, each dot one wake/sleep cycle in one domain, correlational). A recognition model gives better performance at every depth and builds deeper libraries. Recognition-net activations became aligned with the structure of the final programs (a11).

Cost. Training to convergence is about a day on 20 to 100 CPUs. Learning from 1959-Lisp primitives plus the Y-combinator took about five days on 64 CPUs and rediscovered fold, unfold, map, filter, zip, length (a09). The authors say the origami basis took about a year of total CPU time and chose to build in generic primitives instead (b03). Poor abstractions widen the search (LAPS quote, b04).

### 2.3 LAPS: language as a guide (Wong et al., 2021)

LAPS (a22 to a24, b04) adds natural-language task descriptions to DreamCoder. Language guides which abstractions are kept (language-program compression) and trains a neural search model through a translation model. Language is used in training only. Test-time language is optional. This is the first data showing that names and descriptions help choose what to store. The gain survives without text at test time (library alone, graphics: 41.44 for DreamCoder library vs 62.16 for LAPS library).

### 2.4 Stitch and babble: cheap compression (2022 to 2023)

Stitch (Bowers et al., POPL 2023; a12 to a14, b10 to b12, c03, c29) replaces bottom-up version-space compression with corpus-guided top-down search for lambda-abstractions, pruned by an upper bound on achievable compression. It is an anytime algorithm. It is 3 to 4 orders of magnitude faster and 2 orders lighter than DreamCoder's compression, with equal or better compression ratio on DreamCoder's own benchmarks. It runs on corpora where DreamCoder times out (eight 2D CAD domains).

babble (Cao et al., 2023; a33, b13) uses e-graphs and equality saturation, so programs equal under a hand-written equational theory are matched. It reports better compression than DreamCoder orders of magnitude faster. The Stitch paper puts babble at 10 to 100x faster than DreamCoder, Stitch at 1,000 to 10,000x, and notes babble is not anytime. Needs a hand-written domain theory.

These two are the only partly independent confirmation (a different group) that compression-based library learning scales.

### 2.5 LILO: LLM plus Stitch plus documentation (Grand et al., ICLR 2024)

LILO (a15 to a21, b05 to b09, c04 to c07, c24) is the first major bridge to language models. Loop: an LLM (Codex code-davinci-002) plus enumerative search solves tasks, Stitch compresses the solved programs into abstractions, and an LLM (gpt-3.5-turbo) writes names and docstrings (AutoDoc). Names and docs go into the next prompt. The library is re-derived from the base language each iteration, so early bad abstractions are dropped (c29).

Two findings matter most for us. First, raw anonymous abstractions (fn_42) hurt the LLM. Second, asking GPT-4 to do the compression itself failed. Both are in section 3 and 5.

### 2.6 LLM-written libraries (2023 to 2025)

- **LEGO-Prover** (Wang et al., 2023; a32, c11, c26, d22): a growing library of verified Isabelle lemmas. A prover retrieves skills. An evolver creates and transforms lemmas. 22,532 skills generated.
- **TroVE** (Wang, Neubig, Fried, 2024; a28, a29, b18, b19, c10): training-free toolbox induction. The model chooses skip, create or import mode. Periodic trimming. Agreement-based selection.
- **ReGAL** (Stengel-Eskin, Prasad, Bansal, ICML 2024; a30, a31, b14 to b17, c08, c09, c28): cluster training programs, have GPT-3.5 propose helpers by refactoring, verify by running, edit or prune. About 200 training examples.
- **CRAFT** (Yuan et al., 2024; d05, d06): GPT-4 builds a toolset; it is retrieved at test time by three views.
- **Voyager** (Wang et al., 2023; c21, d04): verified JavaScript skills indexed by description embedding, plus automatic curriculum and self-verification, in Minecraft.
- **Agent Workflow Memory** (AWM, 2024; c19, d02, d03) and **ASI** (2025; c20, d01): text workflows and verified executable programs on WebArena.
- **SkillWeaver** (2025; d16): a strong model builds and unit-tests web skills; a weaker model uses them.
- **AbstractBeam** (2024; a36, c16, c30): Stitch-style learning inside neural bottom-up synthesis.
- **TheoryCoder-2** (2026; b28), **LRLL** (2024; b30): cross-environment abstraction reuse and a robot skill library.
- **AWM-style memories on ARC**: ArcMemo (2025; d12, d13).

### 2.7 The sceptical turn (2024 to 2025)

Berlot-Attwell, Rudzicz and Si (a25 to a27, b20 to b25, c12, c13, c25) checked reuse directly in LEGO-Prover and TroVE. Sesterhenn et al. (2025; c14, c15) re-ran TroVE at matched compute. Evo-Memory (Wei et al., 2026; d10, d11) re-tested AWM and Dynamic Cheatsheet. The pattern: published gains often come from sampling volume, self-correction or simple example retrieval, not from reusable abstraction. Section 5 has all numbers.

### 2.8 Human side: prospective compression (2026)

Hernandez Cano et al. (b29): people built helpers that compress future tasks, not only past ones. N = 60 on Prolific. DreamCoder-style retrospective compression and an LLM did not match them when the task sequence changed. Preprint, toy task with 6 primitives.

### 2.9 Two rival routes on ARC

ARC Prize 2024 winners used test-time training (53.5% on the private set) and sampling of thousands of programs (about 42% public). No top entry used library learning (d14). SOAR reached 52% on the public set by fine-tuning on hindsight-relabelled attempts (d15), which needs weight updates and is closed to us.

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, from claims.jsonl), **S** single-source, **C** contested. "Group" means all numbers come from one research group.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Library plus recognition model transforms text editing | 3.7% of 108 SyGuS problems in 10 min (mean 235 s) before learning; 79.6% (mean 40 s) after. CVC4 82.4% at 1 h, 8 CPUs; DreamCoder 84.3% at that budget. Trained on 128 tasks. | DreamCoder (a04, b01); K01 | S (one group; critique confirmed) |
| Both library and guide needed | LOGO and towers: no alternative above 60% held-out, DreamCoder near 100%. 5 runs per curve, 1 sd bars. Mean solve time 54.1 s, median 15.0 s. | a05, b02, c02; K01, K02 | S |
| Compress, do not just memorise | Memorise baselines (whole solutions as primitives) did worse than compression. Values in Fig. S13, not read as numbers. | a06; K02 | S |
| Library depth tracks performance | r = 0.79 across domains and cycles; size effect weaker. Correlational. | a07, c27 | S |
| Physics from generic primitives | 93% of 60 laws after 8 cycles; vector algebra first, then inverse-square schema. | a08 | S |
| Learning a language from near nothing | 20 intro CS tasks all solved; fold, unfold, map, filter, zip, length rediscovered; about 5 days on 64 CPUs. | a09, b03 | S |
| Language lifts library learning | Strings 33.4 to 52.2 (57.0 with mutual exclusivity; 54.6 with compression). Graphics best 49.55 to 98.19, mean 42.64 to 81.98. Scenes 73.9 to 95.9. Human language: 48.6 strings, 58.55 graphics, 95.6 scenes. | LAPS (a23, b04); K23 | S |
| Learned library works with no language at test | Original DSL: 0.06 / 0.00 / 27.8 (strings/graphics/scenes). DreamCoder library 27.2 / 41.44 / 53.6. LAPS library 33.2 / 62.16 / 93.04. | a24 | S |
| Stitch speed and memory | 3 to 4 orders of magnitude faster, 2 orders less memory than DreamCoder compression; equal or better compression. | a12, b10, c03; K03 | E (Stitch + babble) |
| Stitch on large corpora | 8 CAD domains, 50 random 80/20 splits. Test compression 2.55x (castles) to 11.57x (nuts and bolts; train 12.00). DreamCoder found no abstraction with hours and 256 GB. Runtime and memory: "under 2 minutes, under 1 GB" (the paper itself gives two ranges, see section 11 note). | a13, b11; K03 | E |
| Pruning is what makes it tractable | No pruning: no abstraction in any domain within 50 GB and 90 min. No argument-capture pruning: memory limit on over half the domains. | a14, b12 | S |
| babble | Better compression than DreamCoder, orders of magnitude faster, needs equational theory. Per-domain ratios not read. | a33, b13; K03 | E (with Stitch) |
| LILO online solve rates (REGEX / CLEVR / LOGO) | DreamCoder 43.93 / 94.50 / 28.53; LLM Solver 76.13 / 88.67 / 32.13; LLM Solver + Search 76.60 / 96.44 / 37.84; LILO 77.07 / 96.76 / 48.95. 3 seeds. LILO std 14.14 / 3.12 / 9.46 (b05 gives 22.15 for LOGO). | a16, b05, c04, c24; K06 | S |
| Library margin over strongest no-library control | LILO minus LLM Solver + Search: +0.5 REGEX, +0.3 CLEVR, +11.1 LOGO. Minus plain LLM Solver: +0.94, +8.09, +16.82. Most of LILO's gain over DreamCoder is the LLM. | c24, b05; K06 | S |
| Anonymous abstractions hurt | Change vs plain LLM Solver: -30.60 REGEX, -2.91 CLEVR, -11.11 LOGO. | a17, b06, c05; K05 | S |
| AutoDoc recovers part | +9.73 REGEX, +2.27 CLEVR, +0.00 LOGO over the undocumented condition. LOGO docs had semantic errors. | a17, b06; K05 | S |
| LLM cannot do compression | GPT-4: 19.01% valid (998 of 5250); REGEX 24.93%, CLEVR 24.20%, LOGO 4.93%; compression near 1.0x. Stitch 1.5 to 3.5x. | a20, b07, c07; K04 | S |
| Library alone (offline, plain enumeration, no language) | Gain over base DSL: DreamCoder +19.6 / +62.46 / +29.73; LILO +42.27 / +63.43 / +43.24. Absolute: LILO 64.27 / 92.56 / 41.14 vs DreamCoder 41.60 / 91.59 / 30.63. | a18, b08, c06; K07 | S |
| Search inside the loop matters on hard-structure domains | LOGO: LILO 48.95 vs LILO(-Search) 21.02. | a21; K08 | S |
| LILO cost | About 48 CPU-hours per iteration (1800 s search on 96 CPUs). 0.8M to 1.2M GPT tokens per iteration. LILO LLM search $1.77 / $1.87 / $2.01 per iteration. (The $1.16 / $0.71 / $2.07 figures are the enumerative-search cost rows, per the critique.) | a19; K09 | S |
| ReGAL gains by model | CodeLlama-13B: LOGO 45.6 to 57.1 (+11.5), Date 42.8 to 68.9 (+26.1), TextCraft 18.8 to 26.9 (+8.1). GPT-3.5: LOGO 36.9 to 49.3 (+12.4), Date 88.9 to 90.2 (+1.3), TextCraft 15.4 to 18.4 (+3.0), MATH 43.2 to 55.4 (+12.2), TabMWP 87.4 to 89.2 (+1.8). CodeLlama-7B LOGO 34.5 to 34.5. Lemur-70B MATH 14.0 to 13.1, TabMWP 27.5 to 25.7. 13B TabMWP 29.1 to 27.9. | a30, b14, c08; K10 | E (narrow: ReGAL + CRAFT) |
| CRAFT gains by backbone | GPT-3.5: GQA 35.0 to 45.4 (+10.4), OK-VQA 15.4 to 33.4 (+18.0), A-OKVQA 15.6 to 30.8 (+15.2). GPT-4: +4.2, +2.3, +2.5. Toolset built by GPT-4. | d05; K10 | E (with ReGAL) |
| ReGAL ablation | CodeLlama-13B dev, LOGO/Date/TextCraft: full 55.0/77.0/34.12; no retry 48.3/51.9/30.43; no curriculum 36.3/56.6/28.78; no pruning 52.0/65.5/25.26; no editing 53.3/69.6/27.35. | a31, b15, c09; K11 | S |
| ReGAL under shift / less data | TextCraft 13B: +2.56 with 25 demos, +8.45 with about half the data. Unseen objects: primitives 7.8, ReGAL 11.4, plus pruning 14.9, all stages 17.2. | b16, c09 | S |
| ReGAL error modes | 25 cases ReGAL right and baseline wrong (16 baseline reasoning errors, 9 shape errors); 13 the other way (7 connector code, 4 wrong or undefined function, 2 verifier false negatives). | b17, c28 | S |
| TroVE as reported | 30 to 120% relative gain over primitive-only across 7 math sets (CodeLlama-7B); 79 to 98% smaller toolboxes than instance-level. GPT-4 MATH algebra / TabMWP / GQA: TroVE 0.72 / 0.92 / 0.44 with 16 / 38 / 8 tools; CRAFT 0.68 / 0.88 / 0.45 with 282 / 181 / 525 tools. | a28, b18, c10; K12 | S (disputed, see K14) |
| Untrimmed libraries hurt | Instance-level baseline: hundreds to thousands of tools, below primitive-only on most table QA; GQA drop 0.21 with 395 functions, most invalid. Trimming cut size 74 to 90% for a slight accuracy cost. | a29, b18; K12 | E (with AbstractBeam, add-all memory) |
| Reuse is nearly absent | LEGO-Prover: over 20,000 lemmas, 1,233 (6%) reached the prover prompt, 1 reused verbatim once, none twice. TroVE on MATH: 15 functions, 2 reused in correct solutions, 3 successes in 3,201 questions. | a25, a27, b20, b22, c12; K13 | E |
| No-sharing ablation | LEGO-Prover GPT-4o-mini, 12 problems, 50 attempts, 2 trials: 1 problem fewer. TroVE no-reuse vs reproduced: count 0.250 vs 0.236, number 0.290 vs 0.258, geometry 0.050 vs 0.058, intermediate algebra 0.134 vs 0.120 (5 trials). | a26, a27, b21, b22, c25; K13 | E |
| Compute-matched TroVE | MATH K=15: primitive 0.24, TroVE reproduced 0.22, corrected 0.25. Gain about 1 point, not significant. Original primitive baseline 0.12. Bug fix in selection added 3 points. | c14, c15; K14 | E (with LEGO-Prover) |
| Compute-matched LEGO-Prover | miniF2F test equal attempts: 4o-mini baseline 35.9 +/- 0.9 vs LEGO-Prover 25.8 +/- 1.6; gpt-4o 23.1 +/- 1.2 vs 29.3 +/- 3.1; o3-mini 19.4 +/- 2.4 vs 27.8 +/- 4.8. Cost ratio 5.84 / 5.94 / 14.23. At equal compute the baseline was within 1 sd or better in every row. | b23, b24, c13; K14, K15 | E (K14) / C (K15) |
| LEGO-Prover original | miniF2F-valid 48.0 to 57.0, test 45.5 to 50.0 (ChatGPT, 100 attempts). Own text: 52.4 / 45.5 with model-written informal proofs, 55.3 / 50.0 with human-written. Library ablation at 50 attempts: 47.1 vs 50.4. About $300 per 100-attempt run. | a32, c11, d22; K15 | C |
| LEGO-Prover soft reuse | Authors: 24% of solved problems used retrieved skills, 51% direct, 49% rewritten. Replication: verbatim lemma use 2/43, 4/21, 0/20, 13/189; by name 9/43, 6/21, 5/20, 47/189; cross-task reuse 0 verbatim, 1 by name; no survival gap. | c26, b25; K16 | C |
| Verification beats prose, callable adds little | WebArena shopping, claude-3.5-sonnet: unverified text 32.6; verified program in memory 36.4; verified text 39.0; verified program as callable action 40.1. | d01; K26, K27 | E |
| Whole-benchmark skill memory | WebArena: vanilla 32.7, AWM 36.3, ASI 40.4. Steps 5.9 / 5.6 / 5.0. AWM gpt-4 35.5 vs BrowserGym 23.5. ASI skills reused in 42.5% of cases; verification passes on 15.6% of turns. | c19, c20, d01; K17 | C |
| Crude abstraction equals LLM abstraction | WebArena gpt-4: rule-based induction 35.6 (6.3 steps) vs LLM 35.5 (5.9). Workflow actions called in only 18.5% of tasks. | d02; K26 | E |
| Abstract workflow vs concrete example | Mind2Web cross-task gpt-3.5: AWM element accuracy 39.0 vs Synapse 34.0; step success 34.6 vs 30.6. | d03; K26 | S (counter-evidence inside K26) |
| Independent re-test of memory methods | Evo-Memory, Claude 3.7 Sonnet avg success: ReAct 0.57, AWM 0.49, DC-Cu 0.49, DC-RS 0.50, ExpRecent 0.58, ExpRAG 0.63, ReMem 0.78. Gemini 2.5 Flash: ReAct 0.32, AWM 0.30, ExpRAG 0.46, ReMem 0.50. Claude 3.5 Haiku: ReAct 0.27, ExpRAG 0.51. | d10; K17, K26 | C (re-implementations may be weaker) |
| Task similarity predicts gain | ReMem gain vs within-dataset similarity: Pearson 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet). AlfWorld steps 22.6 to 11.5. Easy-to-hard vs hard-to-easy order: 0.77 / 0.92 vs 0.81 / 0.94. | d11 | S |
| Voyager | 63 unique items in 160 iterations, 3.3x baselines. Tech tree: wooden 15.3x, stone 8.5x, iron 6.4x faster; diamond 1 of 3 trials. No library: wooden 7+/-2, stone 9+/-4, iron 29+/-11 vs Voyager 6+/-2, 11+/-2, 21+/-7. No self-verification -73% items; random curriculum -93%; GPT-3.5 writer 5.7x fewer items. | c21, d04 | S |
| Dynamic Cheatsheet: strong model | Claude 3.5 Sonnet AIME 2024 23.3 to 50.0 (DC-Cu), AIME 2025 6.7 to 36.7, GPQA 59.6 to 68.7. GPT-4o Game of 24 10 to 99. | d07; K25 | C |
| Dynamic Cheatsheet: small models | Claude 3.5 Haiku AIME 2024 10.0 to 36.7 but 26.7 with empty memory (instructions only). GPT-4o-mini AIME 2024 16.7 to 13.3. R1 and o1 minimal. | d07; K25 | C |
| DC vs voting, tokens | Sonnet AIME 2024 / 2025: baseline 23.3 / 6.7; vote of 3 on baseline 23.33 / 6.7; DC- 36.7 / 23.3; DC-Cu 50.0 / 36.7. Output tokens per query: baseline 370, DC- 494, DC-RS 1035, DC-Cu 1831. | d08; K32 | E (the not-compute-matched point) |
| Uncurated append hurts | DC full history vs curated: Sonnet 26.7 vs 50.0; GPT-4o 6.7 vs 40.0 (baseline 20.0). | d09; K27 | E |
| Add-all memory hurts, strict filter helps | Success fixed small / add-all / strict: RegAgent 67.53 / 55.48 / 70.95; EHRAgent 16.75 / 13.05 / 38.50; AgentDriver 40.11 / 32.32 / 51.00; CIC-IoT 71.50 / 59.90 / 85.40. Coarse LLM judges EHRAgent 26.19 / 32.21 / 34.66. | d17; K27 | E |
| A measured deletion rule | Delete after at least 5 retrievals if mean utility below 0.3 to 0.7, plus periodic sweep. EHRAgent 38.67 at 1012 records to 42.34 at 248; AgentDriver 51.00 at 1178 to 49.97 at 323; CIC-IoT 85.40 at 904 to 85.50 at 188. Weak GPT-4o-mini judge: helped one, hurt another. | d18; K28 | S |
| Retrieval design | CRAFT GPT-3.5 GQA / OK-VQA / A-OKVQA: full 45.4 / 33.4 / 30.8; no abstraction 37.1 / 31.0 / 28.0; no problem view 42.4 / 32.7 / 29.8; no function-name view 36.4 / 26.8 / 21.7; no docstring view 37.3 / 29.8 / 25.0. SimCSE GQA 36.4, BM25 37.9. ArcMemo embedding retrieval o3-mini 0.26 to 0.22. ToolRet: all retrievers under 52% recall@10 on 43k tools; BM25 above ColBERT; about 10-point pass-rate drop vs oracle tools. | d06, d13, d19; K29 | E |
| SkillWeaver | WebArena GPT-4o 22.6 to 29.8 (+32%); GPT-4o-mini 9.2 to 14.1 (about +54%); live sites 40.2 to 56.2. 160 exploration iterations per site. | d16 | S |
| ATLAS | ministral-8b success: no hints 5.0%, common path 1.7%, minimal 8.3%, guided 8.3%, dynamic (one step at a time) 28.3%. ministral-14b 1.7 / 11.7 / 11.7 / 21.7 / 38.3%. 60 runs per mode. | d21 | S |
| AbstractBeam | Handwritten: 53.6 vs 50.2 (fold 1), 39.6 vs 36.0 (fold 2), p < 0.05; time 2.57 s vs 4.57 s. Synthetic: 52.6 vs 53.8 and 52.4 vs 51.2 (no difference). 5 runs. | a36, c16, c30; K18 | S |
| ARC symmetry subset with compression | 36 tasks, 5 grid primitives: 16 solved, then 17, 19, 22 over rounds. No held-out test. | b26, c17; K20 | S |
| ARC: abstract hypotheses | GPT-4 direct 17%, abstract hypotheses 23%, LLM-summarised 30%, human-selected 33%. 33 of 49 selected hypotheses (67%) gave correct programs. | b27; K19 | S |
| ARC: ArcMemo | 100 tasks, o4-mini, oracle@2, 3 runs: no retry 55.17 (sd 3.18) to 59.33 (PS); one retry 66.67 to 67.33; two retries 69.00 to 70.83 (cheatsheet 71.33). Selection ablation 59.33 vs 55.17 (no retry). Continual update helps only at two retries (67.67 vs 70.00). | d12, d13; K30 | S |
| ARC: library-seeded evolution | 77.1% ARC-AGI-1, 26.0% ARC-AGI-2 semi-private, Grok-4, about 10 calls per task, est. $2.56 per task. Blog post, no library ablation. | c18, a37 (not opened); K21 | S |
| ARC Prize 2024 | Test-time training 53.5% private (winner); Greenblatt about 42% public with thousands of programs; brute-force DSL ensemble 49% private. | d14 | S (report) |
| Stitch on Python | Leroy: 122 student programs, avg 7 lines. 3,123 macro-like, 32 invalid-parameter, about 42,000 under 20 nodes pruned. 1.04x compression; corpus grew 1.2% with the library counted. | d20; K31 | S |
| Prospective compression in people | N = 60. Steps: people 3.93 vs 8.64 raw primitives (E1, t(13) = -3.72, p = 0.0026, dz = -1.00); 4.51 vs 9.56 (E2, t(15) = -5.04, p = 0.00015, dz = -1.26). Success 92.4% (E1), 81.9% (E2). | b29; K22 | S |
| Cross-environment reuse cost | BabyAI combine-skills level 1: 1,961 tokens vs 53,376 for a baseline; Minihack: 0 tokens in the next three rooms after learning move_to. | b28; K24 | S |
| Repeated sampling with a verifier | SWE-bench Lite DeepSeek-Coder-V2: 15.9% with 1 sample to 56% with 250. Voting plateaus near 100 samples. | d23; K32 | E (baseline fact) |

## 4. Mechanisms and models

Written so an engineer can build each piece. Pseudo-steps use our terms: "program" means plain code, "model" means an LLM call.

### 4.1 The wake-sleep loop (DreamCoder), reduced to what an LLM scaffold needs

State: a library L of named helpers, a record of solved tasks T with their verified solutions.

```
for round in 1..R:
    WAKE:   for each task in order (easy first): try to solve with L shown to the model.
            keep only solutions that pass the check (and a held-out check, G3).
    SLEEP-ABSTRACT: program finds repeated sub-structure across kept solutions,
            proposes helpers, scores each by compression gain, keeps the best,
            drops helpers that no solution uses.
    SLEEP-GUIDE: program records, for each solved task, which helpers its solution used;
            this table is the retrieval index (the replacement for the recognition net).
```

What we drop: the neural recognition net and the dreaming step (needs a generative task model, a03). What replaces them: retrieval over helper names and descriptions (section 4.5).

### 4.2 Compression objective (the keep-or-drop rule, in code)

DreamCoder minimises: size(library) + sum of size(each solution rewritten with the library). A helper earns its place only if rewriting the solved tasks with it shortens the total by more than the helper's own size (a02).

Engineer's version:

1. Represent each verified solution as a tree or token list.
2. For a candidate fragment f with holes (parameters), count its occurrences across solutions.
3. Gain(f) = (occurrences x (size of fragment - size of a call to f)) - size(f definition).
4. Keep f if Gain(f) > 0 and occurrences >= 2 across different tasks.
5. Rebuild the whole library from scratch each round (LILO does this; it drops early bad picks, c29).

Stitch's trick for speed: top-down search with an upper bound. Start from the most general pattern (a single hole). Expand it. Prune any branch whose best possible compression is below the best found so far. Without that bound, search finds nothing in budget (a14). It is anytime: stop when the budget is out and keep the best so far.

Limit: compression is a proxy for usefulness. It does not measure future reuse (a02). AbstractBeam shows unused abstractions bloat the search and cancel the gain (c30). So add a second filter: prune by measured use (section 4.6).

### 4.3 Why Stitch is not directly usable on LLM text

Stitch works on typed lambda terms. On Python, most candidates are invalid and compression is 1.04x (Leroy, d20). On prose traces nothing has been tried. What is feasible: a cheap mechanical dedup of repeated sub-steps (K04 test), or restrict the store to tasks that have a small DSL or a function-call trace.

### 4.4 AutoDoc: naming and documenting (LILO)

For each library item the model writes: a name, a one-line purpose, a signature, and one worked example. The raw anonymous item hurts (a17). Naming and docs recover part. Failure: docs can be wrong (LOGO: wrong names for what a function does). So the program must check the doc against behaviour, for example by running the worked example and comparing with the stated result. This is our addition, consistent with G2 and G8. It is not shown in the papers.

### 4.5 Retrieval of helpers without a trained net

Evidence on what works (K29, section 5):

- CRAFT: match on three views, problem text, function name, docstring. Dropping the name view cost 9.0 on GQA and 6.6 on OK-VQA. Single-view SimCSE or BM25 scored 36.4 and 37.9 on GQA vs 45.4.
- ArcMemo: LLM selection of concepts helped at low compute; embedding retrieval of abstract concepts failed (0.26 to 0.22).
- ToolRet: embedding recall is poor on 43k tools; irrelevant at tens of helpers but warns against trust in cosine.
- Voyager: description embeddings plus a top-k.

Engineer's version for a store of 20 to 100 helpers:

1. Candidate set = lexical match (BM25) on name + docstring + the problem text, top 10.
2. A short model call picks 0 to 3 from the candidates given only name, doc and example. It sees no other attempt (S3 isolation).
3. The program logs which were offered and which were called.

No head-to-head of these options exists on one agent store (gap 5).

### 4.6 Verification gate and pruning

Gate (K27): a helper is stored only if (a) it runs, (b) it passes its source task's check, (c) it passes one held-out task or a mutated input (G3). Evidence: ASI unverified text 32.6 vs verified 39.0; Voyager without self-verification -73% items; add-all episodic memory below a small fixed seed memory on 4 of 4 agents (d17).

Pruning rule from the one measured source (d18): after a record has been retrieved at least 5 times, delete it if its mean downstream utility is below a threshold (0.3 to 0.7), and run a periodic sweep every 200 to 500 steps. This cut memory about 4x at equal or better score with an oracle utility. With a weak LLM judge for utility it hurt one of two agents. So the utility must come from code-checked outcomes. This was tested on episodic records, not helper code.

ReGAL also prunes helpers that fail on new data and re-runs (shift result 11.4 to 14.9 to 17.2, b16).

### 4.7 Curriculum and retry

ReGAL ablation (b15): removing the easy-to-hard curriculum dropped LOGO 55.0 to 36.3 (18.7 points); removing retry dropped Date 77.0 to 51.9. Curriculum proxy was mean token length of the query. Voyager's random curriculum cost 93% of items (c21). Evo-Memory found easy-to-hard slightly below hard-to-easy for ReMem (0.77/0.92 vs 0.81/0.94), a mild counter (d11).

### 4.8 What a "call" looks like: callable vs prose

ASI (d01): verified program in memory 36.4; verified text 39.0; verified program exposed as a callable action 40.1. Programs shown in memory were often called and failed because they were not in the action space. AWM: workflow actions called in 18.5% of tasks (d02). So the format matters less than verification. Offer helpers as short text with source plus example first. Make them callable only if a test shows a gain.

### 4.9 Dreaming, as an LLM analogue

Generate practice problems from the library, solve them, record which helper fits which problem shape (a03). Costly in tokens, untested for LLMs. The nearest result is SOAR's hindsight relabelling of failed attempts, which needs fine-tuning (d15); a text version is cheap to test.

### 4.10 Prospective compression

Retrospective compression asks "what repeats in what I solved?" Prospective compression asks "what will repeat in what I will see?" People do the second (b29). For an agent: when the task stream has a known structure (the next items in the same class), ask the model for helpers over the class description, not only over solved items. Untested for LLMs.

### 4.11 Hypothesis-first as library-free abstraction

Wang et al. (b27): write abstract hypotheses in words, then code. ARC subset, GPT-4: 17% to 23% (abstract), 30% (summarised), 33% (human-selected). Per task, no shared store. This is closest to our S2 (candidate rules in plain words) and to O6 (change representation).

## 5. What holds up

### 5.1 Replications and independent re-tests

| Original claim | Re-test | Result |
|---|---|---|
| TroVE: 30 to 120% gain; library helps | Berlot-Attwell et al. 2024 (a27, b22) | Reproduced within 2%. Only 15 functions learned; 3 successful reuses in 3,201 questions. No-reuse ablation equal or better on all four split rows. Authors: self-correction and self-consistency drive the gain. |
| TroVE gain | Sesterhenn et al. 2025 (c14) | Compute-matched primitive baseline 0.24 vs TroVE 0.25; about 1 point, not significant. A bug in the selection step added 3 points to TroVE once fixed. |
| LEGO-Prover: library grows and is reused | Berlot-Attwell et al. 2024 (a25, b20) | 6% of lemmas reached prompts; 1 reused once. No-sharing ablation 1 fewer problem of 12. |
| LEGO-Prover beats baselines | Berlot-Attwell et al. 2025 (b23, b24) | 4o-mini: baseline 35.9 vs 25.8. gpt-4o and o3-mini: LEGO-Prover ahead at equal attempts but costs 5.9x and 14.2x per attempt. At equal compute the baseline matched or won. |
| AWM and Dynamic Cheatsheet help | Evo-Memory 2026 (d10) | On four embodied benchmarks, no better than ReAct; raw experience retrieval (ExpRAG) better. Caveat: the benchmark authors re-implemented them and have their own methods. |
| LAPS DreamCoder baseline on LOGO | LILO authors (K23) | Could not reproduce 42.64; got 28.53. LILO best 73.87 vs LAPS best 92.79. Cross-paper LOGO comparisons are unreliable. |
| DreamCoder results | No independent replication found | All strong numbers come from one group and its direct students. K01, K02, K05 to K10 are single-source. |

LEGO-Prover citation check (d22): the replication's "45.5% (50% with human proofs)" is accurate. The original text gives 52.4 / 45.5 (model-written informal proofs) and 55.3 / 50.0 (human-written). The critique's first suspicion that this was a mis-citation was itself wrong. Subgoal-Learning is 48.0 / 45.5.

### 5.2 What the failures say

1. **Sampling volume masquerades as library benefit.** TroVE's baseline got one generation mode, the method got three, and 15 samples with a vote. LEGO-Prover spent 6 to 14x compute per attempt. Dynamic Cheatsheet spent about 5x output tokens (1831 vs 370) while its comparison vote used 3 samples (d08). Any library claim without a same-token no-library arm is unproven (K14, K32).
2. **Direct reuse is rare.** Library growth does not mean library use (K13). In contrast ASI reports at least one skill reused in 42.5% of cases and AWM workflows are called in 18.5% of tasks. Reuse is high on repeated-template web tasks and near zero on math and proof tasks.
3. **The model often already knows the helpers.** On MATH, libraries formed only for counting, number and prealgebra and reused is_prime and is_perfect_square (c25). LILO REGEX: the plain LLM already gains +32.2 over DreamCoder; the library adds under 1 point over a strong LLM + search. Libraries matter where the vocabulary is not in the weights (LOGO +11 to +17).
4. **Abstractions help only if later tasks use them.** AbstractBeam: gain on handwritten tasks that contain abstractions, none on synthetic out-of-domain tasks (52.6 vs 53.8). 62% of length-7 programs contained them (c30).
5. **Accumulating without a check hurts.** Add-all episodic memory 3.7 to 12.1 points below a small fixed memory on all four agents. Dynamic Cheatsheet full-history append: GPT-4o 6.7 vs baseline 20.0. TroVE instance-level: hundreds of tools, below primitive-only.
6. **A stored wrong item spreads.** Agents copy outputs of retrieved items with similar inputs ("experience-following", d17). Dynamic Cheatsheet: "faulty heuristics that slip into memory can be equally amplified".
7. **Weak verifiers are costly.** Cheap LLM judges of memory quality were mixed (d17, d18). A fine-tuned judge on 300 labelled examples did best in d17. ReGAL had 2 verifier false negatives.

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Base model strength | Gain shrinks as the model gets stronger when someone else builds the library (ReGAL, CRAFT). Contested when the model builds its own memory. | K10 (E), K25 (C) |
| Who builds the library | A strong builder helps a weak user (SkillWeaver +54% vs +32%; ATLAS 5.0 to 28.3%). A weak builder cannot store reliable strategies (Dynamic Cheatsheet: Haiku, GPT-4o-mini). | d07, d16, d21 |
| Task similarity | Gain tracks within-set similarity (Pearson 0.717 and 0.563). Zero gain when later tasks share no structure. | d11, c16 |
| Domain structure | Large on LOGO, text editing, towers, web templates; none on MATH and miniF2F for direct reuse. | multiple |
| Inference compute | ArcMemo gain fades: +4.2, +0.7, +1.8 at 0, 1, 2 retries. | d12 |
| Verifier availability | With a verifier, resampling scales log-linearly; voting plateaus. So the correct no-library baseline is verified resampling. | d23 |
| Library size | Bigger is worse past a point; TroVE 16 tools beat CRAFT 282 at similar accuracy. | b18 |
| Documentation quality | Anonymous items hurt; wrong docs do not help. | a17 |
| Order of learning | Easy-to-hard matters most in ReGAL; slightly reversed in Evo-Memory. | b15, d11 |
| Retrieval design | Multi-view and LLM selection beat single embedding. | K29 |

### 5.4 Interventions that worked and did not

Worked (with evidence):
- Execution verification before storing (ASI +6.4 points on shopping; Voyager).
- Easy-to-hard curriculum (ReGAL +18.7 on LOGO dev).
- Retry of failed refactors (ReGAL +25.1 on Date dev).
- Pruning on new data (ReGAL shift 11.4 to 14.9).
- Naming + docs (LILO +9.73 REGEX).
- Multi-view retrieval (CRAFT).
- Curated rewriting of memory over appending (DC 50.0 vs 26.7).
- Trimming the toolbox (TroVE, 74 to 90% smaller, slight accuracy cost).
- Feeding one stored step at a time to a weak model (ATLAS dynamic 28.3% vs guided 8.3%).

Did not work:
- LLM does the compression (19.01% valid).
- Anonymous items.
- Add-all memory.
- Embedding retrieval over abstract concepts (ArcMemo 0.26 to 0.22).
- Callable exposure as an extra over verified prose (+1.1 points, d01; called in 18.5%).
- Symbolic compression on short Python (1.04x).
- Weak LLM judge to gate or prune (mixed).
- "Memorise" whole solutions as primitives in DreamCoder (worse than compression), though in LLM settings raw experience retrieval is a strong baseline (ExpRAG 0.63 vs AWM 0.49 on Claude 3.7 Sonnet). These two facts coexist: DreamCoder's memorise baseline pollutes the primitive set of an enumerative search, whereas an LLM reads examples in context.

## 6. Language models

### 6.1 How they behave on these tasks

1. **They are weak at compression and good at naming.** GPT-4 produced valid abstractions 19.01% of the time (998 of 5250) with near 1.0x compression. The same family writes useful names and docstrings (+9.73 on REGEX) except where it misreads code (LOGO). Division of labour: code compresses, model names (LILO appendix C.2; a20).
2. **They are hurt by unreadable context.** Raw fn_42 abstractions lowered solve rate by 2.91 to 30.60 points. They "struggled to deploy anonymous abstractions in contextually-appropriate ways" (b06).
3. **They copy retrieved examples.** Experience-following: outputs of retrieved items with similar inputs are copied (d17). Concrete examples bias element choice toward the example (AWM authors, d03). So error and bias propagate.
4. **They use a retrieved item as a template inside one task, not across tasks.** LEGO-Prover verbatim use 2/43 to 13/189 within solutions; cross-task 0 (b25).
5. **They answer faster with fewer steps once memory exists.** AlfWorld 22.6 to 11.5 steps (ReMem), ASI 15.3% fewer steps. But reasoning models used equal or more output tokens with memory (ArcMemo; DC-Cu about 5x).
6. **They sample diverse candidates, which can make selection harder.** TroVE produced 0.74 more distinct candidates per task; selection bug cost 3 points (c14). Diversity helps only with a strong check.

### 6.2 What changed performance, by how much

| Lever | Change | Setting |
|---|---|---|
| Verification before storing | +6.4 (32.6 to 39.0), +1.1 more for callable | WebArena shopping, claude-3.5-sonnet (d01) |
| Curated vs append memory | +23.3 (26.7 to 50.0) Sonnet; +33.3 (6.7 to 40.0) GPT-4o | AIME 2024 (d09) |
| Instruction-only prompt with empty memory | +13.4 (23.3 to 36.7) Sonnet; +16.7 (10.0 to 26.7) Haiku | AIME 2024 (d07, d08). Half or more of the "memory" gain. |
| Memory over instruction-only | +13.3 on both AIME 2024 and 2025 (Sonnet) | d08 |
| AutoDoc | +9.73 REGEX, +2.27 CLEVR, 0 LOGO | LILO (a17) |
| Library over strong LLM + search | +0.5, +0.3, +11.1 | LILO (c24) |
| Library, weak model | +26.1 Date (13B); +10.4 to +18.0 (GPT-3.5, CRAFT) | ReGAL, CRAFT |
| Library, strong model | +1.3 Date (GPT-3.5); +2.3 to +4.2 (GPT-4, CRAFT) | ReGAL, CRAFT |
| Library at matched compute | about +1 (TroVE, n.s.); 0 or negative (LEGO-Prover) | c14, b24 |
| Memory on ARC with o4-mini | +4.2, +0.7, +1.8 at 0, 1, 2 retries, inside sd 1.5 to 3.8 | ArcMemo (d12) |
| Abstract hypotheses on ARC | +6 (17 to 23), +13 summarised, +16 human-selected | GPT-4 (b27) |
| Raw experience retrieval over abstraction | ExpRAG 0.63 vs AWM 0.49 (Claude 3.7 Sonnet) | Evo-Memory (d10) |
| Stepwise strategy hints to small model | 5.0% to 28.3% (8B); 1.7% to 38.3% (14B) | ATLAS (d21) |
| Selection ablation (LLM picks concepts) | +4.2 at no retry, +0.8 at 2 retries | ArcMemo (d13) |

### 6.3 Reasoning models

Dynamic Cheatsheet: R1 and o1 showed minimal or inconsistent gains (d07). ArcMemo used o4-mini and found the gain fades with compute (d12). LEGO-Prover helped o3-mini at equal attempts but not at equal compute (b23). All three point to the same thing for our case: a strong model already does much of what a helper store would do inside its own long reasoning.

### 6.4 Cost data

- LILO: 0.8M to 1.2M GPT tokens per iteration; $1.77 / $1.87 / $2.01.
- LEGO-Prover: about $300 per 100-attempt run (d22); 5.84x to 14.23x per attempt vs baseline.
- SkillWeaver: 160 exploration iterations per site.
- Dynamic Cheatsheet: 1831 vs 370 output tokens per query.
- Cheap-side: Stitch seconds on one CPU; ASI +/- 15% fewer steps; TheoryCoder-2 1,961 vs 53,376 tokens at one level.
- No study gives a break-even curve in tokens (K33).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA.md section 5. Status marks: [E] established, [S] single-source, [C] contested. Evidence ids refer to the jsonl files; K ids refer to claims.jsonl.

### Add now (established)

These are cheap rules that need no new store. They tighten what SCHEMA.md already says, or set the entry conditions for the planned subgoal library.

1. **G7 tightening: every library or memory arm must be compared with a no-library arm that spends the same tokens on verified resampling.** Count library-building and maintenance tokens inside the budget. If a verifier exists, the baseline is verified resampling, not voting. [E] K14, K32; b23, b24, c14, c15, d08, d23.
2. **Memory entry gate (G3 applied to memory): store an item only if it passed its execution check and one unfitted check (held-out task or mutated input).** Never store from the model's own opinion. [E] K27; d01, d04, d09, d17.
3. **Do not accumulate: no append-all memory.** Rewrite and curate; cap size; allow deletion. [E] K12, K27; a29, b18, c10, c30, d09, d17, d18.
4. **Log helper reuse per run (add to section 6 logging): offered, called verbatim, called by name, cross-task.** Credit memory only when reuse is measured and an ablation without the store loses. [E] K13; a25, a27, b20, b22, c12.
5. **Every stored item needs a readable name, a one-line purpose, and a worked example that the program runs and checks against the stated result.** Never store anonymous items. (The documentation-check part is our extension.) The core finding is [S] (K05, LILO only) but the broader principle that raw unreadable items harm is supported by CRAFT's name and docstring views (K29 [E]). Treat the docs requirement as [E] for retrieval keys (d06) and the harm of anonymous items as [S]. Evidence a17, b06, c05, d06.
6. **Compression and counting are done by code, not by the model.** [S] for the specific GPT-4 result (K04), consistent with SCHEMA section 1 and G5, so it is a no-cost rule. Evidence a20, b07, c07.
7. **Retrieval: do not use a single embedding over abstract helper text.** Use lexical match on name + docstring + problem text, then a model pick among at most 10 candidates, as in section 4.5. [E] K29; d06, d13, d19.
8. **Form of stored item: start with verified text plus source and a worked example, not a callable.** The extra gain from a callable is about 1 point and callable workflows were used in 18.5% of tasks. [E] K26; d01, d02, d06, d10.
9. **Order learning easy to hard when building a store from a task stream.** Evidence is ReGAL ablation plus Voyager, with Evo-Memory slightly against. Keep as a default but record it. [S] K11; b15, c09, c21 (so this belongs in "Test first" for strict reading; included here only as a default ordering that costs nothing).

Items 6 and 9 are single-source or mixed; they are listed here because they cost nothing to follow. If strict rules apply, move them to Test first.

### Test first

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | Subgoal library of verified helpers vs verified resampling at equal tokens, on a repeated problem class | memory | [C] | K17, K14; c20, d10, b24 | Central claim; independent re-tests contradict the original papers |
| T2 | Helper offered as callable vs same source as in-prompt example vs random verified example vs no memory (same instructions) | memory | [S] gap | K26; d01, d02, d03 | No study has the random-example control |
| T3 | Dose-response across three model sizes on one task set | memory/G12 | [C] | K10, K25; a30, d05, d07, d11, d16 | Direction depends on who builds the store |
| T4 | Store built by the stronger model, used by the weaker | memory | [S] | d16, d21 | One web study and one pen-test case study |
| T5 | Use-count plus outcome pruning rule on helpers (n >= 5 retrievals, utility threshold) | memory | [S] | K28; d18 | Episodic records only |
| T6 | Doc-check gate (run the worked example, compare to docstring) | memory/G | [S] | K05; a17, b06 | Our extension; LOGO docs were wrong |
| T7 | Hypothesis-first (S2 candidate rules in words, then code) vs more direct samples | S2/O6 | [S] | K19; b27 | ARC subset, small N |
| T8 | Score-weighted softmax sampling of prior solutions vs best-first | memory/S3 | [S] | K21; c18 | Blog result |
| T9 | Prospective helpers: build for the anticipated class, not only solved items | memory | [S] | K22; b29 | Human study only |
| T10 | Stepwise hint feeding from a stored strategy to a weak executor | S3/memory | [S] | d21 | One case study |
| T11 | Retrieval variants head to head on a store of 20 to 100 helpers | memory | [E] direction, no head-to-head | K29; d06, d13, d19 | Gap 5 |
| T12 | Mechanical dedup of repeated sub-steps vs LLM-proposed helpers | memory | [S] | K04, K31; a20, d20 | Symbolic compression on traces is unproven |
| T13 | Hindsight relabel failed attempts as problem-solution pairs (text only) | memory | [S] | d15 | Fine-tuning version works; text version untested |
| T14 | Task-similarity gate: spend on a store only when class similarity is high | S0 | [S] | K18; c16, d11 | Cheap to compute; may save wasted setup |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, including store-building and maintenance. At least 3 seeds. Report mean, sd and the reuse log. The plain arm is verified resampling when a check exists (d23), otherwise vote.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Store vs resampling | Repeated class: a family of ARC-like grid items (or any class with an exact check and shared sub-steps), 100+ items, held-out half | (a) plain, (b) plain + extra verified resamples to match tokens, (c) verified helper store built from the first half | Held-out pass rate; tokens per solved item; cumulative tokens vs items solved (break-even point) | Gain over (b) of 0 to +3 points on strong models, per ArcMemo (+4.2 fading to +0.7 and +1.8). A real effect needs more than the sd (1.5 to 3.8) |
| B2 Callable / example / random / none | Same stream as B1 | (a) helper as callable, (b) same source as example text, (c) random verified example, (d) none with identical instructions | Pass rate; call rate; wrong-call rate | (a) over (b) about +1 (d01); (b) and (a) over (c) unknown; this decides if retrieval matters at all |
| B3 Three model sizes | One task set of 60+ items | Small, mid, strong model; self-built store vs store built by the strongest; empty-memory arm with identical instructions | Gain over the empty-memory arm per size | Expect larger gains for weak users of strong-built stores (SkillWeaver +54% vs +32%); self-built store on a small model may be near 0 or negative (Dynamic Cheatsheet) |
| B4 Verification gate | Same stream | Add-all vs execution-gated vs gated + held-out check | Pass rate; store size; poisoned-item share | Add-all below gated (d17: 3.7 to 12.1 points below a small seed memory, strict filter much higher) |
| B5 Doc quality | Same stream | Helpers with (a) anonymous id, (b) name only, (c) name + doc + example, (d) c + doc-behaviour check | Pass rate | Anonymous below plain (LILO -2.91 to -30.60); doc gain +2 to +10; check adds where docs misread code |
| B6 Prune rule | A long stream (200+ items) | No pruning, random pruning to the same size, rule (n >= 5, utility < threshold) | Pass rate at equal size; store size | Rule at least equal to no pruning at about 4x smaller store (d18) |
| B7 Retrieval | Store of 20 to 100 helpers | BM25 on name + doc + problem; embedding; task-signature match; model pick over BM25 top 10 | Hit rate of the right helper; downstream pass rate | Multi-view and model pick ahead of embedding by 5 to 10 points (CRAFT 8 to 10; ArcMemo 15% drop with embeddings) |
| B8 Hypothesis-first | ARC-style item, 100+ items | (a) direct sampling, (b) abstract hypothesis in words then code, equal tokens | Pass rate | +6 to +13 (b27 17 to 23 and 30); smaller for stronger models |
| B9 Setup break-even | Stream of N items | Cumulative tokens of store arm vs no-store arm | Item count where the curves cross | Unknown; no published curve (K33). If never within the stream, drop the store |
| B10 Task similarity | Mixed streams: high-similarity, low-similarity | Store vs no store | Gain vs measured similarity | Positive correlation (Pearson 0.56 to 0.72, d11); near zero at low similarity (AbstractBeam synthetic) |
| B11 Prospective vs retrospective | Drifting stream | Helpers from solved items only vs helpers also built from class description | Steps or tokens per item | People: about half the steps (3.93 vs 8.64); LLM unknown |
| B12 Hindsight relabel | Stream with many failures | Store only passes vs also store failed attempts relabelled as the problem they actually solve | Pass rate on next items | Unknown; text analogue of SOAR |

Reading rule. Per SCHEMA section 8 item 3, a failing result on our bench overrules the literature. Per G7 the store is kept only if it wins at equal tokens.

## 9. What does not transfer, and why

1. **The neural recognition model and dreaming.** They need a generative model of tasks and thousands of fantasy tasks (a03). Our scaffold does not train weights. Replace with retrieval (section 4.5).
2. **Lambda-calculus refactoring and Stitch on prose.** Stitch needs typed lambda terms. On Python it gave 1.04x (d20). No evidence on free-text traces. Only borrow the idea: a score bound and anytime stopping.
3. **DreamCoder's absolute numbers.** Small synthetic domains, exact I/O specs, hand-built core, 100 to 200 tasks, a day on 20 to 100 CPUs. Text editing 79.6% is a best case. One research group.
4. **Large-scale libraries.** DreamCoder and LILO run to dozens of routines over hundreds of tasks. A single agent session has tens of tasks at most. Setup cost (48 CPU-hours, 0.8M to 1.2M tokens per iteration) would swamp it.
5. **Web and Minecraft skill libraries.** ASI, AWM, Voyager, SkillWeaver work on sites with repeated templates or worlds with repeated structure. Our targets (puzzles, one-off reasoning) repeat less. Evo-Memory ties gain to task similarity.
6. **Math and proof libraries.** TroVE on MATH and LEGO-Prover show near-zero direct reuse. The model already knows the standard helpers (is_prime).
7. **Fine-tuning routes.** SOAR (52% on ARC) and test-time training (53.5%) need weight updates. Closed to us (SCHEMA: scaffold, not training).
8. **Human prospective compression.** A toy task with 6 primitives and 60 people. The mechanism is plausible but unshown for LLMs.
9. **Self-reported ARC numbers.** The 77.1% / 26.0% claim has no library ablation. A plausible reading is that Grok-4 and about 10 feedback-driven calls did the work; the author credits the output-diff feedback (G2).
10. **Reported efficiency in steps.** Step counts fell, but token counts did not for reasoning models. Do not equate fewer steps with fewer tokens.

## 10. Open questions

1. At equal total tokens, does a verified helper store beat verified resampling? Only TroVE and LEGO-Prover were compute-matched and both lost the gain. ReGAL, LILO, ASI, AWM and Voyager were never matched (gap 1).
2. Does the benefit scale down with model strength across three sizes on one task set? Two backbones in CRAFT; ReGAL varies tasks and models together (gap 2).
3. Where does the gain come from if direct reuse is near zero: self-correction, example diversity, soft reuse? A random-example control is missing (gap 3).
4. Does LLM abstraction work on ARC with cross-task transfer? Evidence: a 36-task study, a 100-task study that fades, and a self-reported number (gap 4).
5. What retrieval unit works for a small agent store: description, embedding, task signature? No head-to-head (gap 5).
6. What prune rule and size? One rule exists, for episodic records (gap 6).
7. Does prospective compression beat retrospective for drifting LLM tasks? Only N = 60 humans (gap 7).
8. Does symbolic compression work on an agent's own traces? Only one weak negative (gap 8).
9. How often does a wrong stored helper cause a loss, and does verification prevent it? Counted for episodic memory only (gap 9).
10. What is the break-even in tokens? No curve (gap 10).
11. Is the LILO library margin real? 3 seeds, LILO std 14.14 on REGEX; library margin over the strong control is under 1 point on two of three domains.
12. Does the DreamCoder result replicate outside its group? None found.
13. Is the Stitch memory and runtime range 0.19 to 60.16 s / 714.55 MB or 0.24 to 77.26 s / 683.89 MB? The paper contradicts itself (critique).
14. Is a soft reuse effect present at all? LEGO-Prover authors say 24% of solved problems used retrieved skills; the replication says no survival gap.
15. Do newer reasoning models do compression well? GPT-4 (2023) failed; later models were not tested.

## 11. Sources

[V] = opened and read this session (full text or substantial sections). [M] = snippet or abstract page only.

- [V] Ellis et al. (2021) DreamCoder: growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning. https://arxiv.org/abs/2006.08381 (a01 to a11, b01 to b03, c01, c02, c27)
- [V] Wong, Ellis, Tenenbaum, Andreas (2021) LAPS: Leveraging language to learn program abstractions and search heuristics. https://arxiv.org/abs/2106.11053 (a22 to a24, b04)
- [V] Bowers et al. (2023) Top-down synthesis for library learning (Stitch). https://arxiv.org/abs/2211.16605 (a12 to a14, b10 to b12, c03, c29)
- [V] Grand et al. (2024) LILO: Learning interpretable libraries by compressing and documenting code. https://arxiv.org/abs/2310.19791 (a15 to a21, b05 to b09, c04 to c07, c23, c24)
- [V] Cao et al. (2023) babble: Learning better abstractions with e-graphs and anti-unification. https://arxiv.org/abs/2212.04596 (a33, b13; per-domain ratios not read)
- [M] Ellis et al. (2018) Learning libraries of subroutines for neurally-guided Bayesian program induction (EC2). https://proceedings.neurips.cc/paper/2018/hash/7aa685b3b1dc1d6780bf36f7340078c9-Abstract.html (a34)
- [M] Wong et al. (2022) Identifying concept libraries from language about object structure. https://arxiv.org/abs/2205.05666 (a35)
- [V] Stengel-Eskin, Prasad, Bansal (2024) ReGAL: Refactoring programs to discover generalizable abstractions. https://arxiv.org/abs/2401.16467 (a30, a31, b14 to b17, c08, c09, c28)
- [V] Wang, Neubig, Fried (2024) TroVE: Inducing verifiable and efficient toolboxes. https://arxiv.org/abs/2401.12869 (a28, a29, b18, b19, c10)
- [V] Wang, Xin, Zheng et al. (2023) LEGO-Prover: neural theorem proving with growing libraries. https://arxiv.org/abs/2310.00656 (a32, c11, c26, d22)
- [V] Berlot-Attwell, Rudzicz, Si (2024) Library learning doesn't: the curious case of the single-use library. https://arxiv.org/abs/2410.20274 (a25 to a27, b20 to b22, c12, c25)
- [V] Berlot-Attwell, Rudzicz, Si (2025) LLM library learning fails: a LEGO-Prover case study. https://arxiv.org/abs/2504.03048 (b23 to b25, c13)
- [V] Sesterhenn, Berlot-Attwell, Zenkner, Bartelt (2025) A compute-matched re-evaluation of TroVE on MATH. https://arxiv.org/abs/2507.22069 (c14, c15)
- [V] Zenkner et al. (2024) AbstractBeam: Enhancing bottom-up program synthesis using library learning. https://arxiv.org/html/2405.17514v3 (a36, c16, c30)
- [V] Alford et al. (2021) Neural-guided, bidirectional program search for abstraction and reasoning. https://arxiv.org/abs/2110.11536 (b26, c17)
- [V] Wang et al. (2024) Hypothesis search: inductive reasoning with language models. https://arxiv.org/abs/2309.05660 (b27)
- [V] Ahmed et al. (2026) Learning abstractions for hierarchical planning in program-synthesis agents (TheoryCoder-2). https://arxiv.org/abs/2602.00929 (b28)
- [V] Hernandez Cano et al. (2026) Prospective compression in human abstraction learning. https://arxiv.org/abs/2605.09985 (b29)
- [M] Tziafas and Kasaei (2024) Lifelong robot library learning (LRLL). https://arxiv.org/abs/2406.18746 (b30; abstract and setup only, no numbers)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c19, d02, d03)
- [V] Wang et al. (2025) Inducing programmatic skills for agentic tasks (ASI). https://arxiv.org/abs/2504.06821 (c20, d01; read via an HTML fetch summary per c20)
- [V] Wang et al. (2023) Voyager: an open-ended embodied agent with LLMs. https://arxiv.org/abs/2305.16291 (c21, d04)
- [V] Andrews (2024) Capturing sparks of abstraction for the ARC challenge. https://arxiv.org/abs/2411.11206 (c22; scanned for method and numbers only)
- [V] Yuan et al. (2024) CRAFT: customizing LLMs by creating and retrieving from specialized toolsets. https://arxiv.org/abs/2309.17428 (d05, d06)
- [V] Suzgun, Yuksekgonul, Bianchi, Jurafsky, Zou (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d07 to d09)
- [V] Wei et al. (2026) Evo-Memory: benchmarking LLM agent test-time learning with self-evolving memory. https://arxiv.org/abs/2511.20857 (d10, d11)
- [V] Ho et al. (2025) ArcMemo: abstract reasoning composition with lifelong LLM memory. https://arxiv.org/abs/2509.04439 (d12, d13)
- [V] Chollet, Knoop, Kamradt, Landers (2025) ARC Prize 2024 technical report. https://arxiv.org/abs/2412.04604 (d14)
- [V] Pourcel, Colas, Oudeyer (2025) SOAR: self-improving language models for evolutionary program synthesis. https://arxiv.org/abs/2507.14172 (d15; abstract and method outline only, treated as read for the 52% figure)
- [V] Zheng et al. (2025) SkillWeaver. https://arxiv.org/abs/2504.07079 (d16)
- [V] Xiong et al. (2025) How memory management impacts LLM agents: experience-following behavior. https://arxiv.org/abs/2505.16067 (d17, d18)
- [V] Shi et al. (2025) Retrieval models aren't tool-savvy (ToolRet). https://arxiv.org/abs/2503.01763 (d19; figure label read from garbled text)
- [V] Bellur, Alghamdi, Workneh, Izraelevitz (2024) Leroy: library learning for imperative programming languages. https://arxiv.org/abs/2410.06438 (d20)
- [V] Lopez-Miguel et al. (2026) ATLAS: discovering agent strategies through LLM-guided abstraction and automata learning. https://arxiv.org/abs/2608.14352 (d21)
- [V] Brown, Juravsky, Ehrlich, Clark, Le, Re, Mirhoseini (2024) Large language monkeys. https://arxiv.org/abs/2407.21787 (d23)
- [V] Pang (2025) ARC-AGI-2 SoTA: efficient evolutionary program synthesis. https://ctpang.substack.com/p/arc-agi-2-sota-efficient-evolutionary (c18; blog, not peer reviewed)
- [M] ccocks (2025) arc_agi GitHub project. https://github.com/ccocks/arc_agi (a37; search summary only, unverified)

Notes on source quality:
- Group overlap. DreamCoder, LAPS, Stitch, LILO share authors and benchmarks. Treat their agreement as one source. ASI and AWM share authors (Wang, Neubig); TroVE is the same group.
- Stitch Table 2: the paper gives "0.24 to 77.26 s, 684 MB" in the table and "0.19 to 60.16 s, 714.55 MB" in the text. Use "under 2 minutes, under 1 GB".
- Corrections applied from the critique: LILO costs of $1.16 / $0.71 / $2.07 are enumerative-search rows, not LILO total; GPT-3.5 ReGAL TextCraft is 15.4 to 18.4, LOGO is 36.9 to 49.3; ASI's 23.5% is relative, and the text says 4.2 points where the table gives 3.8; SkillWeaver's 39.8% is the live-site figure; AWM's text says 3.2 where the table shows 3.6 vs 4.8; LEGO-Prover's 52.4 is its own model-proof valid score.
- LILO LOGO std is 9.46 in a16 and 22.15 in b05. Both are recorded; the table cell is not resolved here.
