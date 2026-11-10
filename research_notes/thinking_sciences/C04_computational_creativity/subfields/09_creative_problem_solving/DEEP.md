# Creative problem solving: deep document

*Subfield C04.09. Focus: insight and incubation in architectures; impasse and restructuring. Evidence ids (a01..d16) refer to evidence_a-d.jsonl in this folder; claim ids (K01..K29) refer to claims.jsonl (full id C04.09-Knn). Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single-source, [C] contested. Items marked "second-hand" were not opened this session.*

## 1. What it is

Creative problem solving here means solving a problem whose first approach fails and whose solution needs a change in how the problem is represented. Psychology calls the moment of failure an impasse and the change a restructuring. The sudden sense of seeing the answer is the "Aha". The pause that sometimes helps is called incubation.

Four questions matter for our agent.

1. Why do solvers get stuck? (Wrong constraints, tight chunks, hill-climbing on a bad progress signal.)
2. What gets them unstuck? (Constraint relaxation, chunk decomposition, a fresh look, acting on the material, a break.)
3. Is any of this a special process, or ordinary search with ordinary memory? (Mostly the second; the evidence leans "business as usual".)
4. Do language models show the same stuck-then-restructure pattern, and does a scaffold fix it? (They are stuck in a different way: they often reach the answer and fail to commit, and spontaneous "wait" shifts are not restructuring.)

Scope. Other C04 subfields cover productive failure, calibration, scaffolding, search over thoughts, Tree of Thoughts, conceptual change and epistemic curiosity. This document links to them and does not redo them. The human insight literature in A12 (psychology of insight) is the parent. Here we add the incubation meta-analyses, the architecture-level models, and the LLM tests of 2023 to 2026.

## 2. History and theories in depth

**Gestalt era.** Duncker (1945) proposed that solving needs restructuring of the representation. His candle problem shows functional fixedness: the tack box is seen as a container, not a shelf (a25, second-hand via Wikipedia, a11). Wallas's four stages (preparation, incubation, illumination, verification), refined by Hadamard, are the folk model. Metcalfe and Wiebe (1987) found that "warmth" ratings predicted progress on non-insight problems but not on insight problems (a11, via Wikipedia).

**The fixation challenge.** Weisberg and Alba (1981) tested the nine-dot problem. Telling people to go outside the square did not solve it for most. In their data 5 of 12 failed five months after seeing the solution, and 8 of 23 failed after one week (a26, second-hand through Ormerod et al. 2006). They argued that prior knowledge, not a special restructuring process, explains the difficulty. This started the "business as usual" tradition.

**Search accounts.** Kaplan and Simon (1990) treat insight as search at the level of the problem representation: solvers notice invariants and use them as cues for moves (a27, second-hand).

**Representational Change Theory (RCT).** Knoblich, Ohlsson, Haider and Rhenius (1999) on matchstick arithmetic (a01 to a05). Prior knowledge sets constraints and tight chunks. Persistent failure triggers two repair operations: constraint relaxation (the wider the constraint's scope, the harder) and chunk decomposition (the tighter the chunk, the harder). RCT predicted and found the difficulty order C > B > A and D > A. Numbers in section 3.

**Progress monitoring theory (CSPT).** MacGregor, Ormerod and Chronicle (2001) (a08, read through later reports). Solvers hill-climb: they choose moves that maximise apparent progress to the goal. Insight problems are hard because progress-maximising moves lie off the solution path. When no move meets a progress criterion (criterion failure), the solver tries other moves, sometimes outside the usual range. Test: nine-dot with a given first line, diagonal inside the array 47% vs horizontal outside 28% (Expt 4), 65% vs 43% (Expt 5, N=103).

**Complementary roles.** Ormerod and MacGregor (2020) (a06, a07) showed that chunk tightness matters as RCT says, but equation value cues also matter, which RCT does not predict. Both knowledge and strategy are needed.

**Incubation theories.** Gilhooly (2016) (a15, b06 to b10, b26) lists accounts: unconscious work, intermittent conscious work, beneficial forgetting (of misleading cues), and fresh look (any break lets the solver restart). Sio and Ormerod (2009) say no single mechanism explains all results (b05). Ritter and Dijksterhuis (2014) advocate an unconscious contribution but concede many studies cannot separate it from mere distraction (b11).

**Special process versus business as usual.** Chein and Weisberg (2014) found that insight-rated solving uses the same working memory and attention control as analytic solving (b15, b16). The "Aha" is a report, not a separate engine.

**Architecture and complexity models.** CLARION (Helie and Sun 2010; Helie, Sun and Xiong c.2008) has an explicit top level and an implicit bottom level; incubation is mainly implicit, bottom-level work (a16, a17, a18). An ACT-R model of matchstick problems with chunk decomposition and constraint relaxation (Jones 2003) exists (c30, from memory only, not opened). Wareham (2012) proved that RCT-style restructuring is NP-hard in general and tractable only under small restrictions (a19).

**The LLM era.** Benchmarks arrive from 2023 (BrainTeaser, Only Connect, MacGyver, LatEval, SPLAT) and reach 2026 (NazoNazo, CresOWLve). A new debate: does the "aha moment" in reasoning models show real restructuring? d'Aliberti and Horta Ribeiro (2026) say no (b23).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RCT: difficulty follows constraint scope and chunk tightness | Exp 1A N=20: problem type F(3,57)=7.11 p<.001; C harder than B harder than A; D harder than A; block effect F(1,19)=14.41 | Knoblich et al. 1999 (a02) | [E] |
| Order replicated in same-lab samples | Exp 1B N=38 (ceiling: 96% A, 90% B); Exp 2 American students, B vs A p=.14 | Knoblich 1999 (a03) | [E], same lab |
| Second encounter removes the difficulty gap (transfer) | Interaction found in all 4 experiments; surface similarity no effect, F(3,74)=0.34 | Knoblich 1999 (a04) | [E] |
| Showing the tautology removes only the constraint difficulty | Type C: 61% solved in block 1 without, all with. Type D block 1: 61% vs 69%, chi2(1,N=34)=0.22 p=.64. Median time C 175 s vs 11 s; D 193 s vs 46 s | Knoblich 1999 (a05) | [E] |
| Value cues matter beyond RCT | N=121: low-value loose 77%, low-value tight 43%, high-value loose 90%, high-value tight 77%. Value Wald=8.65 p=.003 | Ormerod and MacGregor 2020 (a06) | [E] |
| Standard tautology is hard only without a value cue | N=133: 12% (4/32) low-value vs 62% (21/34) high-value; interaction Wald=5.26 p=.022 | Ormerod and MacGregor 2020 (a07) | [E] |
| Hill-climbing explains nine-dot difficulty | Diagonal 47% vs horizontal 28%; 65% vs 43% (N=103) | MacGregor et al. 2001 (a08, second-hand) | [S] |
| Knowing the solution does not ensure re-solving | Nine-dot: 5/12 failed after 5 months, 8/23 after 1 week. Necklace N=50: hint group 5 solved, control 6. many restated the hint but could not apply it (see note below the table) | Weisberg and Alba 1981; Ormerod et al. 2006 (a09, a10, a26) | [E] |
| Incubation gives a small average gain | 117 effects, weighted mean d=0.29, CI 0.21 to 0.39, Q=173.99, variance .0834; median 0.26 | Sio and Ormerod 2009 (a12, b01) | [E] |
| Task type moderates the gain | Linguistic 0.22 (65 studies), visual 0.26 (35), creative 0.29 (14); visual vs linguistic z=1.25 ns | Sio and Ormerod 2009 (a13, b02) | [C] |
| Break content: low-demand filler beats rest only on linguistic problems | Low load 0.52, rest 0.46, high load 0.24 overall; linguistic low vs rest beta=.54 p<.05 | Sio and Ormerod 2009 (a13, b04) | [C] |
| Longer preparation, larger gain (visual, creative) | Visual r(35)=.40 p=.02; creative r(14)=.60 p=.03; linguistic r(65)=.04 p=.75 | Sio and Ormerod 2009 (a14, b03) | [S] |
| Cues in the break not significant moderators | Misleading present 0.35 vs absent 0.32; relevant present 0.24 vs absent 0.34 | Sio and Ormerod 2009 (a13, b05) | [S] |
| Incubation helped in most published experiments | 29 of 39 experiments significant | Dodds, Ward and Smith 2003 (a29, second-hand) | [S] |
| Immediate incubation (break before any work) also helps | g=0.224 over 92 decision studies | Strick et al. 2011 via Gilhooly (b07) | [S] |
| Fresh look: any break helps after impasse | Break vs none significant; 4 vs 12 min and crossword vs browsing no difference | Segal 2004 via Gilhooly (b09) | [S], second-hand |
| Unconscious thought advantage fails in a large replication | Meta-analysis k=61, g=0.15 CI [0.03, 0.26]; trim-and-fill g=0.018 CI [-0.10, 0.14]. Replication N=399: deliberation 58.2% vs distraction 61.9%, chi2=1.09 p=.30, BF=7.83 for null | Nieuwenstein et al. 2015 (d05, d06) | [E] on decisions; no insight tasks (d07) |
| Time, not REM, explains repeated-item gains on RAT | N=77; group difference on repeated items P=0.67 | Cai et al. 2009 (b14) | [S], small cells |
| Distraction helps selecting, not generating, ideas | N about 112: idea count F(2,109)=5.43; creativity F<1; selection chi2(2)=11.15 p<.01 | Ritter et al. 2012 (b12) | [S] |
| Insight uses ordinary working memory | N=53: solved 24.75/60; verbal WM beta=.40 (insight .39); antisaccade R2 .19 to .39; insight 10.14 s vs analytic 21.74 s; think-aloud no cost | Chein and Weisberg 2014 (b15, b16) | [S] |
| Acting on material lifts solving severalfold | Time 1: 43% (12) vs 6% (2), chi2(1,N=63)=12.42. Exp 2: switch to hands-on at time 2 gave 61% (14/23) vs 5% (1/20) switching to paper | Henok et al. 2020 (b18, b19) | [S] |
| Aha feeling is not a reliable sign of correctness | 47 items, 42.4% solved; Aha rating lowest for false insights (3.6) | Kizilirmak et al. 2021 (b17) | [S] |
| Insight restructuring is computationally hard | NP-hard even with 0 constraint relaxations or 0 de-chunkings; tractable under small parameter bounds | Wareham 2012 (a19) | [S] |
| LLMs far below humans on new insight riddles | Humans 52.9% (n=126, 120-item subset); non-reasoning 7.6%; reasoning 17.6%; all 201 items 9.42% vs 19.25%, OR 2.29 (CI 1.99 to 2.64) | Mizumoto et al. 2025, NazoNazo (a20, c01) | [S] |
| LLMs write the right answer and do not commit | Verification failure share of wrong answers: Gemini 2.5 Flash 5.23% (9), Claude Opus 4 25.00% (35), DeepSeek-R1 30.57% (48), Grok 4 39.34% (48) | NazoNazo (a21, c02) | [S] |
| Spontaneous "wait/aha" shifts are rare and go with lower accuracy | 1M+ traces; shifts about 6.31%; formal Aha criteria 1.79%; Qwen2.5-1.5B 2.57% shifted vs 16.44% non-shifted, N=723,200 | d'Aliberti and Horta Ribeiro 2026 (b23, c05) | [S]; supported by Liu et al. 2025 (d11) |
| Forced reconsideration gated on uncertainty helps math, not crosswords | Math 0.3221 to 0.4062 (+8.41 pp, N=320,000 pairs; appendix +7.74 pp, N=464,000); crosswords +0.45 pp; Rush Hour +0.01 pp | d'Aliberti and Horta Ribeiro 2026 (b24, c06) | [E] for math (with d08, d13); no insight-item test |
| Ungated self-review lowers accuracy | GPT-4 GSM8K 95.5 to 91.5 to 89.0 over two rounds; GPT-3.5 CommonSenseQA 75.8 to 38.1 | Huang et al. 2024 (d08) | [E] (with F07, F11, F12) |
| Equal tokens: fresh samples beat extending one trace with "Wait" | Up to 22 pts at same budget; R1-Distill-1.5B GSM8K: "Wait" to 16K tokens -11.8% vs standard; parallel at 16K +10.1% | Ghosal et al. 2025 (d09) | [S], math only |
| Pre-computing offline cuts test-time compute | About 5x less compute for same accuracy; up to +13% (GSM-Symbolic), +18% (AIME) | Lin et al. 2025 (c26) | [S] |
| Lateral-thinking benchmarks show a large human gap | BrainTeaser: humans about 92%, ChatGPT 62.68 sentence / 53.46 word; SPLAT GPT-4 41.70% (easy 70.96, medium 36.88, hard 17.27) | Jiang 2023; Chen 2024 (c10, c14) | [E] |
| Models are inconsistent under rewrites | ChatGPT and RoBERTa-L fail 45% and 61% of original or semantic-variant puzzles whose context version they answer | Jiang 2023 (c11) | [S] |
| Red herrings drive failure | Only Connect, GPT-4 10-shot: original 6 walls / 239 groups; WordNet variant 471 / 1,926; randomized 59 / 595 | Naeini et al. 2023 (c19, c20) | [S] |
| For tool-use creativity, errors are infeasibility, not fixation | GPT-4 efficient 18.9%, infeasible 37.5%; wrong tool 42.4% of errors; self-reflect -9.7 infeasible, div-conv -4.3 | Tian et al. 2024 MacGyver (c16 to c18) | [S] |
| 2026 frontier models still fail expert insight puzzles | 2,061 items; non-thinking under 30%; GPT-5.4 9.4% to 17.8% (EN) no thinking to medium; creative-vs-factual drop 6.08 to 17.21 pts | Ismayilzada et al. 2026 CresOWLve (d01, d02) | [S] |
| Old public puzzle sets are contaminated | Gemini-3.1-Pro picks true item 73% vs 25% chance; +15 to +18 pts higher on RU than EN | CresOWLve (d03) | [S] |
| Failure modes of strong models: missing connection and misread clues | 1,087 GPT-5.4 errors, 150 hand-labelled; retrieval errors rare | CresOWLve (d04) | [S], per-column values not verified |
| Hidden-state probe predicts correctness | ROC-AUC above 0.7, ECE below 0.1; early exit saves up to 24% tokens | Zhang et al. 2025 (d10) | [S], needs model internals |
| Rebus puzzles: models below experts; feedback retry plateaus | GPT-5 60.42/69.44, o3 54.56, gpt-4o 18.75, claude-3.7-sonnet 10.20; expert humans 76.4 to 80.80 | Lee et al. 2025 (d13) | [S] |

Note on the "knowing the solution" row: in the nine-dot data re-analysed by Ormerod et al. (2006), 10 solved on attempt 1, 7 on attempt 2, 16 failed in two attempts and 11 failed all 10 (a09). Of the 16 early failures, 2 stayed within the array, 5 went outside, 8 were mixed.

Corrections carried over from the critique. The "0.04" in Sio and Ormerod is a standard error, not a standard deviation. The d'Aliberti MATH-500 "14.4% vs 32.7%" and the crosswords "20.1% vs 9.6%" are overall pass-1 accuracies in the appendix, not shifted vs non-shifted; do not cite them. Use "1M+" traces, not "11M".

## 4. Mechanisms and models

Each model is written so an engineer can implement it as code around a language model.

**4.1 Representational Change Theory as a loop.** State: a representation R = (constraints C, chunks K, allowed moves). Search under R. If the failure criterion is met, pick a constraint in C and widen it (narrow-scope constraints are easier to relax, so try them first), or pick a chunk in K and split it (loose chunks first; tight chunks are slow). Re-run search under the new R. Implementation: a ledger "assumptions I am making" (constraints) and "units I treat as indivisible" (chunks); an operator step asks the model to drop one assumption or split one unit; code reruns the check. Prediction to use: a fix that removes a constraint helps constraint problems and gives nothing for chunk problems (a05).

**4.2 Progress monitoring (CSPT).** State: current best distance to goal. Rule: take the move that most reduces distance. Trigger: if no move meets a progress criterion (say, a required gain per step), declare criterion failure and widen the move set, accepting moves that look worse. Implementation: an impasse detector in code that tracks a numeric progress score (checks passed, partial credit). A stall for n steps fires S6. It needs a progress score, which only some tasks have.

**4.3 Fresh look as a context reset.** The solver's history biases later steps. A break lets the bias decay. Implementation: drop the failed attempt from the context and re-sample, optionally with a one-line failure note. Evidence: any break works after impasse and length does not matter (b09); equal-token fresh samples beat extending one trace on math (d09). The cheapest version needs no model call beyond the new attempt.

**4.4 Unconscious work (not implementable as such).** The account says background associative processing continues during the break. CLARION's implicit layer is the nearest architecture: explicit rule search plus implicit associative learning with bottom-up and top-down links (a16, a18). A distractor harms incubation only if it uses the same modules as the main task (a16). In free recall of 50 drawings over a 10-minute gap, reminiscence was 7.26 for doing nothing, 4.9 for no incubation, 2.47 for syllogisms, 2.26 for dynamic control; F(5,108)=10.65 (a17). That is recall, not problem solving. A stateless model does nothing between calls, so there is no analogue. The nearest working analogue is sleep-time compute (c26): precompute derived facts about the context before the question. It is directed preparation, not distraction.

**4.5 Selection, not generation.** A distraction helped pick the most creative idea, not produce more (b12). The schema already separates generation (S3) from code-selected choice (S7). Do not expect a reset to raise idea count.

**4.6 Externalised state.** People who could handle chain pieces solved 43% vs 6%; after incubation, being able to act again mattered more than the wait (b18, b19). Implementation: give the agent a scratch object it can change and re-read (code execution, a state table). The agent sees the result of an action instead of imagining it.

**4.7 Complexity bound.** Restructuring is NP-hard in general and tractable under small bounds (a19). Bound the restructuring moves per attempt, the active chunks and the constraints considered. The schema's tree rule (3 children, depth 2, 2 expansions) is consistent with this.

**4.8 Gated reconsideration.** A second pass is triggered when the first pass looks uncertain (token entropy in d'Aliberti; sample disagreement as an outside proxy for an API-only agent). The pass is forced from outside. Gains were measured on math only (b24). A hidden-state probe is better calibrated but needs model internals (d10).

**4.9 Candidate ledger and commit by check.** NazoNazo's verification failures show a last-mile problem: the correct string appears in the thought log and the answer line differs (a21). Code extracts every candidate string from every attempt, tests each on the check, and commits the one that passes. This is S4 "harvest" in the schema. The open question is the false-commit cost.

## 5. What holds up

**Replications and meta-analyses.**

- Sio and Ormerod (2009): 117 effects, d=0.29, CI 0.21 to 0.39 (a12). Funnel plot judged symmetric, so no correction applied; that is weak evidence against bias. Q=173.99 shows heterogeneity. Mostly short lab breaks of minutes. It is the only insight-relevant meta-analysis in our files.
- Strick et al. (2011) immediate incubation g=0.224 (b07), second-hand.
- Nieuwenstein et al. (2015): the unconscious thought advantage on decisions falls from g=0.15 to g=0.018 after bias correction, and an N=399 replication built to favour the effect found none (d05, d06). This is about decisions. It does not show that incubation on insight problems is zero (the critique asks that K02 not be read that way).
- Cai et al. (2009): on repeated RAT items, passage of time helped as much as REM sleep (b14). N=77, cells of 6 to 28.
- Gilhooly's tests: filler tasks were not impaired, and thought sampling found no target-related thoughts predicting gain (b06). Immediate incubation helped, which rules out forgetting of a fixation that never formed (b07).
- RCT's within-paper replications (Exp 1B, Exp 2) are same-lab. We found no independent test of the tautology/chunk dissociation.
- Ormerod and MacGregor (2020): value cues change results, so RCT alone is not enough (a06, a07).

**Failures and non-effects.**

- Olton and Johnson (1976): seven distractor activities, no incubation effect on insight problems (a16).
- Dodds et al. (2003): 29 of 39 significant, so about 10 were not (a29, second-hand). Publication bias possible.
- Distraction did not raise the number or creativity of ideas (b12).
- Hints and seen solutions did not transfer: necklace hint group 5 vs control 6 solved (a10).
- Thinking aloud did not hurt insight solving (b16).

**Moderators.**

- Task type (linguistic 0.22, visual 0.26, creative 0.29): modest; "creative gains most" is contested.
- Preparation length: bigger gains for visual and creative, none for linguistic (a14).
- Filler demand: low-demand beats rest only for linguistic (b04). Segal found no filler effect after impasse (b09). These two are in tension.
- Dissimilar filler helps more than similar filler (b08); the forgetting account predicts the opposite.
- Interactivity: acting on physical material raised solving (b18); the restart context mattered more than the wait (b19).
- Working memory: verbal WM predicts insight as it predicts analytic solving (b15).

**Interventions that worked.**

- A break after impasse (small, d about 0.2 to 0.3, high spread).
- Tautology exposure for constraint problems (a05).
- Value cues in the problem (a07).
- Hands-on material (b18).
- Forced second pass gated on uncertainty (math, +7.7 to +8.4 pp) (b24).
- Fresh samples over extending one trace at equal tokens (d09, math).
- Divergent-convergent prompting for tool problems (MacGyver, helped all three models) (c18).

**Interventions that did not work.**

- Conceptual hints for transfer (a10).
- Telling people to go outside the square (a26).
- Spontaneous "wait" in reasoning traces (b23, d11).
- Ungated self-review (d08).
- Task information in object-replacement tests, mostly detrimental (b25).
- Distraction for the sake of unconscious work (K02, contested).

## 6. Language models

**Overall level.** LLMs sit far below humans on new insight-style items. The gap shrinks mainly with reasoning mode and release date.

| Benchmark | Models | Result | Source |
|---|---|---|---|
| NazoNazo (201 riddles, 120-item human subset) | 38 LLMs 2023-2025 | Humans 52.9%. Non-reasoning 7.6%, reasoning 17.6%. Only GPT-5 in the human CI (descriptive). Parameter count did not predict accuracy; release date did | a20, c01 |
| BrainTeaser (1.1K) | ChatGPT | 62.68 sentence, 53.46 word; humans about 92%; random 25% | c10 |
| SPLAT (975 multi-turn puzzles) | GPT-4 | 41.70% average; easy 70.96, hard 17.27 | c14 |
| Only Connect walls (494 test walls) | GPT-4 10-shot | 6 walls solved; human connection accuracy 80% | c19 |
| MacGyver (1,600+) | GPT-4 | 18.9% efficient, 37.5% infeasible; majority-correct humans 79.3% vs GPT-4 73.3% | c16 |
| CresOWLve (2,061 items, 2026) | thinking models | Non-thinking all under 30%; GPT-5.4 9.4% to 17.8% (EN), no thinking to medium effort | d01, d02 |
| Rebus puzzles (432) | GPT-5, o3, others | GPT-5 60.42/69.44 vs expert humans 76.4 to 80.80 | d13 |
| Chinese verbal insight and RAT | GPT-3.5/4/4o | Models beat humans on RAT (GPT-4o +0.35); on rebus humans beat models (+0.46 over GPT-4-turbo) | c21, c22 |
| ChatGPT on 30 verbal insight problems | GPT-3.5 era | Matched the most probable human outcome | c24 |

**The contradiction and its likely cause.** Zhang 2025, Orru 2023 and Raz 2024 say models match or beat humans on verbal insight. NazoNazo, BrainTeaser, Only Connect and CresOWLve say models are far below. The likely cause is old public easy items against new items. Contamination is measured for one 2026 model (Gemini-3.1-Pro: 73% vs 25% chance; +15 to +18 pts on the Russian original, d03). Contamination in Orru and Zhang is unmeasured. Other causes are not ruled out.

**How models behave.**

- Strategy: in the Chinese rebus task, correct model answers used reasoning 68.88% (4o) and 71.26% (turbo); humans used transformation 72.41% (c22). Models reach classic answers more by deduction than by reframing.
- Wrong answers stay closer to the stimulus words than humans' wrong answers (c23).
- Failure is often last-mile: verification failures are 5.23% to 39.34% of wrong answers (a21). Wrong reinterpretations are held with confidence ("false insight").
- On expert puzzles, missing connections and misread clues dominate; recall errors are rare (d04).
- Removing red herrings lifted GPT-4 from 6 to 471 solved walls, but the variants differ in more than red herrings (c20).
- Tool problems: the main error is infeasibility and constraint violation (wrong tool 42.4%, constraint-related 26.4%) (c17).
- Mental set: Haq et al. (2025) found complex-first sometimes helped, the opposite of human Einstellung; 6 items per cell, no stats (c08). Chain-of-thought took 3 steps where the shortcut takes 1 (c09).

**What changed performance, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Reasoning mode vs none | NazoNazo 7.6% to 17.6%, OR 2.29; CresOWLve GPT-5.4 9.4 to 17.8% | a20, d02 |
| Gated forced second pass | Math +7.7 to +8.4 pp; crosswords +0.45 pp; Rush Hour +0.01 pp | b24 |
| Spontaneous aha shift | 2.57% vs 16.44% accuracy; harmful | b23 |
| Ungated self-review | GPT-4 GSM8K 95.5 to 89.0 | d08 |
| "Wait" extension at equal tokens | -11.8% for a 1.5B model on GSM8K; parallel +10.1% | d09 |
| Divergent-convergent (MacGyver) | +6.5 pts efficient (GPT-4); helps all three models | c18 |
| Self-reflection (MacGyver) | -9.7 pts infeasible, only GPT-4; no gain for Claude2 or Llama2-13B | c18 |
| Few-shot reasoning demos (NazoNazo) | Improved all 4 tested models, significant in 2 | b20 |
| More clues up front (LatEval) | Strong models gain, weak do not (figure only) | d12 |
| Compressed hints (SemEval) | Beat no hint and long hints in several settings; submission log, not an ablation | c12 |
| Question-asking traces as prompts | +0.4 to +5 points on other lateral benchmarks | c15 |
| Sleep-time compute | About 5x less test-time compute on predictable context | c26 |
| Reasoning language (Japanese vs English) | Grok 4 29.5% vs 48.8% (p=.0071); other models ns; self-selected | a22 |

**Aha tokens.** DeepSeek-R1's "aha moment" claim (c28) was one qualitative example plus a word count, with no accuracy comparison. Liu et al. found self-reflection keywords already in the base model and not positively correlated with accuracy (d11). d'Aliberti found shifts in about 6.3% of traces, falling to 0.00 to 0.25% for DeepSeek-R1 on MATH-500, and lower accuracy when a shift occurs (c07). Aha tokens are not evidence of restructuring.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory.

### Add now (established)

| # | Item | Part | Status | Evidence | Why |
|---|---|---|---|---|---|
| A1 | Trigger and score on checks, never on "wait/aha" text. Do not count aha tokens as success. | G10 (reinforce) | [E] via G10; the specific 2.57% vs 16.44% figure is [S] | b23, c05, c07, d11 (K14) | Spontaneous shifts are rare and go with lower accuracy. |
| A2 | Any forced reconsideration needs an outside gate (failed check, sample disagreement, stalled progress score). No ungated "review your answer". | G1 (reinforce) | [E] | d08, d13, b24, c06 (K15, K24) | Ungated review lowered accuracy; gated second pass gave +7.7 to +8.4 pp on math. SCHEMA already has G1 and 4b; add the figures. |
| A3 | Keep O4 (drop a constraint) and O6 (change representation) as separate operators; phrase O4 as "name the assumption you made, then widen it" and add "split the unit" to O3. | O3, O4, O6 | [E] for the human mechanism; LLM benefit untested | a01 to a07 (K06, K07) | Constraint relaxation and chunk decomposition are separable mechanisms. |
| A4 | Store the procedure that solved a twin problem, not only the insight statement. | M (S9) | [E] | a09, a10, a26 (K08) | Hints were restated but not applied in humans. A memory line "go outside the square" is not enough; keep a worked example or code. |
| A5 | Evaluate on fresh items and on rewrites; do not rely on old public insight sets. | S (bench) | [E] for the gap; contamination size [S] | c10, c11, c21, d03 (K17, K21) | Old sets are partly contaminated; models fail 45% and 61% of rewrite-inconsistent puzzles. |
| A6 | Keep divergent-convergent generation (generate many, code picks) and a feasibility and constraint re-read in creative tool tasks. | S3, S7 | [S] for the size; already inside the schema | c16 to c18 (K20) | Main error is infeasibility. No new element needed. |
| A7 | Keep "no incubation by distraction" in 4b, and say it concerns hidden-work steps; a plain context reset is a separate operator to test. | 4b | [E] on decisions; [C] on insight | b13, d05, d06, b14 (K02) | The replication evidence is on decisions. |

### Test first (not yet established)

| # | Item | Part | Status | Evidence | Note |
|---|---|---|---|---|---|
| T1 | Context reset after impasse: drop the failed attempt, resample fresh, optionally with a one-line failure note. | O (new, near S6) | [S] | d09, a12, b09 (K01, K25) | No direct LLM insight test. Human prior d about 0.2 to 0.3. |
| T2 | Candidate ledger and commit-by-check across attempts. | S4 | [S] | a21, c02 (K13) | False-commit cost unmeasured. |
| T3 | Impasse trigger: stalled progress score vs step count vs sample disagreement. | S6 | [S] | a08, b24, d10 (K03, K07) | No head-to-head found. |
| T4 | Name-and-widen-constraints operator vs generic retry on text analogues of matchstick items. | O4 | [S] | a05 (K06) | Does the tautology/chunk dissociation transfer? |
| T5 | Externalise state: code or scratch object. | O (new) | [S] | b18, b19 (K10) | Henok effect was one human problem. |
| T6 | Short vs long hints and short restructure prompts. | O (hint) | [C] | c12, d12 (K19, K29) | Only an uncontrolled log. |
| T7 | Name the tempting frame, then test alternatives. | O8, S3 | [S] | c19, c20 (K18) | Variants confounded. |
| T8 | Connection-forcing step and clue re-read on fresh expert puzzles. | O6 | [S] | d01, d04 (K26) | Errors are missing connections and misread clues. |
| T9 | Delay the reset until k failed attempts. | S6 | [S] | a14, b03 (K03) | Correlational across studies. |
| T10 | Sleep-time precomputation on reused context. | M | [S] | c26 (K16) | Only where context is reused. |
| T11 | Cap restructuring moves per attempt. | G | [S] | a19 (K23) | Theory only. |
| T12 | Confidence after a reframe vs an independent check. | G | [C] | b17, d10, d11 (K11, K28) | Sample disagreement as proxy. |

## 8. Concrete tests on our bench

All arms run at equal total tokens. Setup cost counts (G7). Use items not in public sets, written after the model cutoff where possible. Where public sets are used, add a rewrite set. Log per-item flips right to wrong and wrong to right.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 reset | NazoNazo-style riddles; Only Connect walls; BrainTeaser rewrites; fresh word puzzles | (a) one long attempt; (b) attempt then continue ("wait"); (c) attempt, drop it, fresh sample; (d) as (c) plus a one-line failure note | Accuracy; share flipped wrong to right | Small gain for (c) or (d) over (b), about d 0.2 to 0.3 as in humans |
| T2 ledger | NazoNazo-type items with logs | (a) final answer as given; (b) code harvests every candidate and tests it; (c) harvest, model picks | Recovered share of verification failures; false-commit rate | Recovers part of the 5% to 39% of wrong answers; false commits unknown |
| T3 trigger | Items with a numeric progress score (matchstick text, constraint puzzles) | Reset trigger: step count, sample disagreement, progress stall, no gate | Accuracy; tokens to solve | Progress stall beats step count if hill-climbing is the cause |
| T4 constraint | Matchstick and rule puzzles in text, constraint and chunk variants | (a) generic retry; (b) "name your assumptions, widen one"; (c) "split the unit, try the parts" | Accuracy by item type | (b) helps constraint items; (c) helps chunk items; (b) no help on chunk items |
| T5 externalise | Physical-process and sequence puzzles | Text only vs code or scratch-state tool | Accuracy | Large gain if the effect transfers; none if state is already in text |
| T6 hint | Lateral puzzles with a hint bank | None; short trick-type; long; compressed | Accuracy; hint-following rate | Short and compressed beat long; strong models gain more |
| T7 red herring | Only Connect-like walls | Plain vs "list the tempting grouping, then test alternatives" | Walls solved; groups correct | Gain if fixation on the obvious grouping is the cause |
| T8 connection | Fresh expert puzzles | Plain vs connection-forcing step vs higher thinking effort | Accuracy | Beats higher effort only if the failure is search, not knowledge |
| T9 preparation | Same items as T1 | Reset at once vs after k attempts | Accuracy | Later reset gains more on visual and creative items; none on linguistic |
| T12 aha calibration | Fresh puzzles | Verbal "aha" after reframe vs independent check | AUC of aha against correctness | Near 0.5 if the human false-insight result carries over |

## 9. What does not transfer, and why

- **Unconscious work during a pause.** A language model does nothing between calls. Only sleep-time compute has a machine analogue, and it is directed precomputation (c26).
- **The felt Aha as a signal.** Human Aha is a report, partly confounded with speed (b16). For models, aha text is a token pattern that exists in base models and does not go with accuracy (d11).
- **Forgetting a misleading cue.** A fresh context gives the same effect on purpose and cheaply; the slow-decay account is not needed.
- **Filler-task content.** Crossword or browsing fillers mean nothing to a model with no tired state.
- **Sleep and REM effects.** No analogue (b14).
- **Matchstick-specific numbers.** RCT's sizes come from Roman numeral arithmetic with strong priors. The mechanism is general; the sizes are not.
- **Math gains for insight items.** The +7.7 to +8.4 pp is on math with a checkable answer; crosswords and Rush Hour gained about zero.
- **Hidden-state probes.** Calibrated, but need model internals (d10), which an API does not give.
- **Human hands-on gain.** One problem with physical pieces (b18). Models already see text state.
- **Old puzzle sets.** Orru, Zhang and similar results cannot be read as insight ability without a contamination check (d03).

## 10. Open questions

1. Does a gated forced reconsideration help a strong 2026 model on genuine insight items at equal tokens? (d'Aliberti shows near zero on crosswords and Rush Hour.)
2. How much of the NazoNazo gap can a candidate ledger plus commit-by-check recover, and at what false-commit cost?
3. Do fresh items (post-cutoff, other languages) and 2026 models reproduce the NazoNazo gap?
4. Does the human tautology/chunk dissociation transfer to LLMs, and does a named-constraint operator beat generic retry?
5. What is the effect of a context reset after impasse for LLMs? No direct test found.
6. Are there large replications of incubation on insight problems since 2015? Search was blocked, so absence is not shown (d07).
7. Does externalised state raise LLM insight scores?
8. Which impasse trigger is best: step count, disagreement, entropy, progress stall?
9. Is verbalised "aha" after a reframe calibrated against correctness?
10. Do short targeted hints beat long ones in a controlled ablation?
11. Is the claim "creative tasks gain most from incubation" true? The authors' own test showed a modest difference.

## 11. Sources

[V] opened this session, [M] snippet or second-hand only.

- [V] Sio and Ormerod (2009), Does incubation enhance problem solving? Psych Bull 135, 94-120. https://www.gwern.net/doc/psychology/writing/2009-sio.pdf
- [V] Knoblich, Ohlsson, Haider and Rhenius (1999), Constraint relaxation and chunk decomposition in insight problem solving. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf
- [V] Ormerod and MacGregor (2020), The complementary roles of knowledge and strategy in insight problem-solving. https://escholarship.org/uc/item/8m02w9c6
- [V] Ormerod, Fioratou, Chronicle and MacGregor (2006), The Remnants of Insight (CogSci 28). https://escholarship.org/uc/item/509348f5
- [M] MacGregor, Ormerod and Chronicle (2001), Information processing and insight; read through later reports. https://escholarship.org/uc/item/509348f5
- [V] Gilhooly (2016), Incubation and intuition in creative problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/ and https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01076/pdf
- [V] Ritter and Dijksterhuis (2014), Creativity: the unconscious foundations of the incubation period. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2014.00215/pdf
- [V] Ritter, van Baaren and Dijksterhuis (2012), Creativity: the role of unconscious processes in idea generation and idea selection. https://scottbarrykaufman.com///wp-content/uploads/2012/11/Ritter-et-al.-2012.pdf
- [V] Helie, Sun and Xiong (c.2008), Mixed effects of distractor tasks on incubation. https://ccn.psych.purdue.edu/papers/pp772-helie.pdf
- [M] Helie and Sun (2010), Incubation, insight, and creative problem solving: a unified theory and a connectionist model. https://www.sciencedaily.com/releases/2010/12/101201124345.htm
- [V] Wareham (2012), What can (and can't) make problem solving by insight possible? https://iccm-conference.neocities.org/2012/proceedings/papers/0033/paper0033.pdf
- [V] Chein and Weisberg (2014), Working memory and insight in verbal problems. https://link.springer.com/content/pdf/10.3758/s13421-013-0343-4.pdf
- [V] Kizilirmak et al. (2021), Insight is not always the same. https://pub.dzne.de/record/155581/files/19597.pdf
- [V] Henok, Vallee-Tourangeau and Vallee-Tourangeau (2020), Incubation and interactivity in insight problem solving. https://link.springer.com/content/pdf/10.1007/s00426-018-0992-9.pdf
- [V] Cai et al. (2009), REM, not incubation, improves creativity by priming associative networks (summary page). https://pmc.ncbi.nlm.nih.gov/articles/PMC2700890
- [V] Nieuwenstein et al. (2015), On making the right choice. https://jbaron.org/journal/14/14321/jdm14321.html and https://research.tilburguniversity.edu/en/publications/on-making-the-right-choice-a-meta-analysis-and-large-scale-replic/
- [V] Wikipedia, Insight. https://en.wikipedia.org/wiki/Insight
- [M] Duncker (1945); Weisberg and Alba (1981); Kaplan and Simon (1990); Dodds, Ward and Smith (2003); Segal (2004); Smith (1995); Strick et al. (2011); Danek and Wiley (2017); Wiley and Danek (2024): second-hand through the sources above.
- [V] Mizumoto et al. (2025), NazoNazo benchmark. https://arxiv.org/abs/2509.14704
- [V] d'Aliberti and Horta Ribeiro (2026), The Illusion of Insight in Reasoning Models. https://arxiv.org/abs/2601.00514
- [V] Haq et al. (2025), Is your LLM trapped in a Mental Set? https://arxiv.org/abs/2501.11833
- [V] Jiang et al. (2023), BRAINTEASER. https://arxiv.org/abs/2310.05057
- [V] Sadeghi et al. (2024), uTeBC-NLP at SemEval-2024 Task 9. https://arxiv.org/abs/2404.02474
- [V] Chen et al. (2024), SPLAT. https://arxiv.org/abs/2410.06733
- [V] Tian et al. (2024), MacGyver. https://arxiv.org/abs/2311.09682
- [V] Naeini et al. (2023), LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167
- [V] Zhang et al. (2025), AI delivers creative output but struggles with thinking processes. https://arxiv.org/abs/2503.23327
- [V] Orru et al. (2023), Human-like problem-solving abilities in large language models using ChatGPT (abstract only). https://doi.org/10.3389/frai.2023.1199350
- [M] Raz et al. (2024), via Zhang et al. https://arxiv.org/abs/2503.23327
- [V] Nair, Gizzi and Sinapov (2024), Creative problem solving in large language and vision models. https://arxiv.org/abs/2405.01453
- [V] Lin et al. (2025), Sleep-time compute. https://arxiv.org/abs/2504.13171
- [V] Muennighoff et al. (2025), s1. https://arxiv.org/abs/2501.19393
- [V] DeepSeek-AI (2025), DeepSeek-R1. https://arxiv.org/abs/2501.12948
- [M] Jones (2003), Testing two cognitive theories of insight. https://doi.org/10.1037/0278-7393.29.5.1017
- [V] Ismayilzada et al. (2026), CresOWLve. https://arxiv.org/abs/2604.03374
- [V] Huang et al. (2024), LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Ghosal et al. (2025), Does thinking more always help? https://arxiv.org/abs/2506.04210
- [V] Zhang et al. (2025), Reasoning models know when they're right. https://arxiv.org/abs/2504.05419
- [V] Liu et al. (2025), Understanding R1-Zero-like training. https://arxiv.org/abs/2503.20783
- [V] Huang et al. (2024), LatEval. https://arxiv.org/abs/2308.10855
- [V] Lee et al. (2025), Puzzled by puzzles. https://arxiv.org/abs/2505.23759
- [V] Liu, Karimnazarov and White (2025), Trapped by expectations (human study; ruled out as evidence). https://arxiv.org/abs/2504.02074
