# Representational change theory: deep document

*Subfield A02.05. Evidence ids (a01..d15) are in evidence_a-d.jsonl; claim ids (K01..K25) are in claims.jsonl; the cross-check is in critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Representational change theory (RCT) says that some problems are hard because the solver starts with the wrong representation. The solver is not short of search effort. The search space simply does not contain the answer. The solver hits an impasse. The impasse is broken only when the representation changes. Then search resumes in a new space and the answer comes quickly. [a01]

RCT names two ways to change the representation:

- **Constraint relaxation.** An assumed rule is dropped (for example "numerals are fixed, only operators move", or "lines must turn on a dot").
- **Chunk decomposition.** A perceptual unit is split into parts (for example the Roman numeral X becomes two crossed sticks).

The theory is specific. It predicts the difficulty order of single problems: wider constraints are harder to drop, and tighter chunks are harder to split. [a02, a03]

Why it matters for our agent. It gives O4 (drop a constraint) and O6 (change representation) a mechanism. A failed run is explained by a wrongly active constraint or chunk, not only by lack of search. It also says when these operators should fire: at an impasse (G1, S6), not on a schedule.

Scope warning. All human RCT data comes from a few task families (Roman-numeral matchsticks, nine-dot, eight-coin, five-square), mostly one lab family. Which constraints and chunks are active is stipulated by the authors and never measured. [a01, a26]

## 2. History and theories in depth

**Roots.** Gestalt psychology said insight is a sudden restructuring. Ohlsson (1984, 1992) turned this into an information-processing account. Knowledge is a set of constraints. An impasse occurs when active constraints exclude the solution. Three processes can change the representation: elaboration (add information), re-encoding (reinterpret elements), and constraint relaxation. Search runs before the impasse. (The Ohlsson 1992 and 2011 books were not found online. This is from secondary descriptions and the 1999 paper. [a19, d14, M])

**Earlier support.** Knoblich & Haider (1996) and Knoblich & Wartenberg (1998) showed that matchstick arithmetic is unsolvable if arithmetic constraints are kept, and that chunk decomposition needs a change in the perceptual parse. Ohlsson & Rees (1991) gave the idea that knowledge consists of constraints. [a27, not opened]

**Founding paper: Knoblich, Ohlsson, Haider & Rhenius (1999).** Matchstick arithmetic in Roman numerals: move one stick to make a false equation true. Five-minute limit per problem. [a01]

- Constraint relaxation is ordered by the scope of the constraint. The value constraint (numerals) is narrowest. The operator constraint (+, -) is wider. The tautology constraint (the equation must not become X = X) is widest. Predicted ease: Type A (change a value) > Type B (change an operator) > Type C (tautology). [a02]
- Chunk decomposition is ordered by tightness. A loose chunk has parts that are themselves chunks (VII = V + I + I). A tight chunk has parts that mean nothing alone (X split into two slanted sticks). Type D (tight chunk) should be harder than Type A (loose chunk). Plus and equal signs are intermediate. [a03]
- Transfer hypothesis: once a constraint is relaxed or a chunk is split, it stays that way, so difficulty differences shrink in the second block. [a04]
- Competitors weighed and rejected by argument: Gestalt reorganization (too vague for single-problem predictions), blind variation and selection (cannot predict move order or differential transfer), functional fixedness (explains the impasse, not its end), mental ruts (predicts recovery only after a pause), gradual transformation of experience (implausible here). The comparison is by elimination and fit, not a head-to-head model fit. [a08]

**Eye-movement follow-up: Knoblich, Ohlsson & Raney (2001).** Three predictions: fixations lengthen at impasse; early attention goes to values, not operators; late attention moves to the crucial element only in solvers. Rival impasse accounts predict only the first. [a09, a29, b06]

**Nine-dot and eight-coin line.** Kershaw & Ohlsson (2001, 2004) split nine-dot difficulty into perceptual, knowledge and process sources. Training that removes the hidden constraint (you may turn at a non-dot point) helps. [a14, b12, d11] Ollinger, Jones, Faber & Knoblich (2013) found two sources of difficulty in the eight-coin problem (assuming a 2D space; breaking perceptual groups) and say move choice follows the current representation, not heuristics. [a18, b18, abstract only]

**Two-move extension.** Ollinger, Jones & Knoblich (2006), N=120: the amount of representational change required predicts solution rates; heuristics matter little. Their model makes representational change a precondition for heuristics to work. [a16, d13; abstract only, so K08 is unverified]

**The rival: progress monitoring.** MacGregor, Ormerod & Chronicle (2001): solvers pick moves that reduce the distance to the goal. Insight is sought when the goal looks unreachable in the moves left. This explains solving without relaxing anything. Jones (2003) pitted the two against each other with eye movements. The abstract says both got support and the problem manipulations favoured RCT. Full text not opened. [b17, a17] Ormerod & MacGregor (2020) is the only independent matchstick replication we opened (section 5). [a12, a13, d03, d04]

**The stage question.** Fedor, Szathmary & Ollinger (2015) found that most solvers do not follow the four-stage order (search, impasse, insight, search). Search and impasse recur. [b15]

**The timing question.** Graf et al. (2023): whether insight looks sudden depends on the statistical model. [b07, b09]

**Machine side.** NazoNazo (2025) explicitly frames its riddles on Knoblich 1999 and Ohlsson 1992. [a23] No LLM paper tests the chunk or constraint-scope orderings directly. [d15]

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Difficulty follows constraint scope (value < operator < tautology) | Exp 1A N=20: type effect F(3,57)=7.11, p<.001. Exp 2 N=78: type effect F(4,222)=46.45, p<.001; B<C p<.001. Order never violated; non-significant cases attributed to ceiling | Knoblich 1999 [a02, a05, a08, b01] | [E] (with 2026 sample) |
| Same order on a new online sample | N=189: value-loose-chunk 80.7% correct, tautological 19.2%; overall 47.5% (449/945) | Nasvytis & Fan 2026 [a22, b10] | [E] |
| Tight chunk (D) harder than loose chunk (A) | Exp 1A: D solved 75% block 1, 90% block 2. Exp 2: D < A p<.001. Time: A<D T=10 p<.001 (1A), T=96 p<.001 (1B) | Knoblich 1999 [a04, a05, a07] | [E] partly replicated |
| A vs B (value vs operator) gap is weak in frequency | Not significant in Exp 1B (p=.12) and Exp 2 (p=.14); significant in time (1A T=12, 1B T=107, both p<.001). Type B over 80% solved in Exp 2 (ceiling) | Knoblich 1999 [a05, a07, a28] | [S] (K02) |
| Transfer is by changed representation, not surface | Exp 2: block 1 66%, block 2 96%. Similarity effect F(3,74)=0.34 n.s.; block 1 by similarity 67/64/64/71% | Knoblich 1999 [a05, b02] | [E] |
| Transfer is specific to what was changed | Exp 3 N=34: tautology exposure helped Type C (regular C 61%, tautological C 100%) but not Type D (61% vs 69%, chi2(1)=0.22, p=.64; block 2 92% vs 94%) | Knoblich 1999 [a06, b03] | [S] one study |
| Same-type repetition transfers; mixed types do not | N=189, 5 trials: Same group 0.32 to 0.75; Same vs Different on later problems 83.7% vs 44.0%; later solve time 89.9 s vs 179.0 s | Nasvytis & Fan 2026 [a22, b10, c24] | [E] (human; with 1999 specificity) |
| Naming the problem type appears after first success | Categorisation utterances 0.3% to 2.1% (about 7x, +1.8 pp, CI .007 to .030); distinct candidate moves fell by 2.11 (Same) and 2.24 (Different) | Nasvytis 2026 [b11] | [S]; classifier accuracy about .64 |
| Long fixations favour values early | N=24. Long fixations element effect F(3,63)=24.02, p<.001; short F(3,63)=2.82, p<.05. Plus and equal signs got less than the 20% chance share | Knoblich 2001 [a09, a10] | [S] (K04) |
| Solved rates in the eye study | A 23/24, B 9/24, C 18/24. A vs B chi2=18.38 p<.001; A vs C chi2=4.18 p<.05; B vs C chi2=4.78 p<.05 | Knoblich 2001 [a09, b04] | [S] |
| Solvers shift attention to the crucial element late | Problem B success x interval F(1,22)=7.91 p<.01; Problem C F(2,42)=5.08 p<.05; main effect of success F(1,21)=3.09 p=.09 n.s. | Knoblich 2001 [a11, b05] | [S], modest, post hoc intervals |
| Progress monitoring can erase the chunk penalty | N=121 of 129: low-value loose 77% (23/30), tight 43% (13/30); high-value loose 90% (28/31), tight 77% (24/31). Chi2(3)=21.6 p=.001; chunking Wald 8.12 p=.004; value Wald 8.65 p=.003; interaction n.s. | Ormerod & MacGregor 2020 [a12, d03] | [C] (K06) |
| Number disparity moves tautology solving | N=133 of 144: standard tautology low-value 4/32 (12%), high-value 21/34 (62%); reverse tautology 72% vs 77%. Tautology Wald 19.33; value Wald 11.12; interaction Wald 5.26 p=.022 | Ormerod & MacGregor 2020 [a13, d04] | [C]; a confound for any difficulty-order test (K24) |
| Nine-dot: removing the hidden constraint helps | N=90 (30 per group): facilitating 63% (19/30), hindering 27% (8/30), none 37% (11/30); chi2(2)=8.836 p<.05; facilitating vs none chi2(1)=4.267 p<.05; hindering vs none n.s. Completers of training 89% (17/19) vs non-completers 18% (2/11) | Kershaw & Ohlsson 2001 [a14, b12] | [E] (with Kershaw 2004) |
| Unaided nine-dot is near 0%; trained groups 30 to 97% | 11-dot 97%, 10-dot 80%, displaced nine-dot 50%, nine-dot 40%, three-turn 30% (Kershaw & Ohlsson 2004). Exp 1 N=150: 83/60/38/40/50%. 83% (99/120) drew outside the dots | Kershaw 2004 [d11] | [E]; baselines second-hand |
| Most solvers skip the classic stage order | Five-square, N=129 recruited (101 used for the insight split). Insight reported by 74% of solvers (29/39) vs 10% of non-solvers (6/62). Repetition 0.5 vs 0.3, t(99)=5.13, p<.0001. Impasse button 8/24 vs 34/43 | Fedor 2015 [b15, b16] | [S] (K09) |
| Suddenness depends on the analysis method | N=61: 34% solved in 5 min, 45% after the hint "you can change the operators, too". GAM and change-point models find a late burst near the 90% bin; ANOVA on 10 bins hides it | Graf 2023 [b07, b08, b09] | [S] (K05) |
| LLMs far below humans on restructuring riddles | NazoNazo, 38 models, 201 riddles. Non-reasoning 7.6%, reasoning 17.6% on the 120-item subset; humans 52.9% (95% CI 46.6 to 59.2, n=126). Odds ratio 2.29 (CI 1.99 to 2.64). GPT-5 inside the human CI (descriptive) | Mizumoto 2025 [a23, c01, b22, d09] | [C] (K10) |
| LLMs find the answer and do not commit | Verification failures as a share of wrong answers: DeepSeek-R1-0528 30.57% (48), Gemini 2.5 Flash 5.23% (9), Claude Opus 4 25.00% (35), Grok 4 39.34% (48). Ceiling: Grok 4 37% to 62% | Mizumoto v3 [c02, b23, d08] | [S] (K11) |
| BRAINTEASER: ChatGPT (2023) vs humans | Sentence: original 60.77, semantic 59.33, context 67.94, all three 39.71, overall 62.68. Word: 56.10, 52.44, 51.83, all three 29.27, overall 53.46. Humans 91.98 and 91.67. Original to all-three drop: ChatGPT -21.1 pp (sentence), -26.8 pp (word); humans -1.9, -2.1 | Jiang 2023 [d01, d02, c04, c05] | [E] for 2023 ChatGPT only |
| Red herrings fixate LLMs | GPT-4 0-shot: 6/239 correct groups (original), 59/595 (randomized), 471/1926 (no herrings; knowledge also changes). Humans 285/494 walls. 1 to 10 shot examples did not help. NYT Connections: best model solves 18% of games; experts over 60% | Naeini 2023; Samadarshi 2024 [c07, c08, c09] | [E] (K13) |
| MathSticks (VLMs) | o3 60.00% with text, 38.50% without; Gemini-2.5-Pro 45.25 / 22.50; Flash 26.50; Claude Sonnet 4 2.25; GPT-4o 0.00; humans 91.72 (3 people). o3 sign-changed 51.45 vs 65.19 unchanged (text). 82.01% of items need two sticks | Ji 2025 [a24, c10, c11, d10] | [S] (K14) |
| Spontaneous "Aha" shifts in small RL models are rare and hurt | 1M+ traces; shifts in 6.31% of traces; accuracy 2.57% shifted vs 16.44% not (N=723,200). Formal Aha events about 1.09 to 2.99% | d'Aliberti & Horta Ribeiro 2026 [a21, b25, b26, c12] | [S] (K12) |
| Forced reconsideration cue helps on math, not elsewhere | Math 32.21 to 40.62 (+8.41 pp; 50,574 wins vs 23,500 losses; N=320,000). Crosswords 9.70 to 10.15 (+0.45; 5,380 vs 5,004; N=83,200). Rush Hour +0.01. High-entropy math +15.38 vs low +5.82 | same [c13, d06, d07] | [S]; no cue-free second sample |
| LLM constraint relaxation in optimisation | AutoCO: 24.7% mean optimality-gap reduction vs LLM methods. Agent proposing alternative constraint models improved 1028/1500 (68.5%); out of 150: single-shot 64, best-of-5 101, ReAct agent 102.8 | Liu 2026; Voboril & Szeider 2026 [c21, c22] | [E] that relaxation works, but the agent only matches best-of-5 |
| External reformulation | Situation puzzles: 4/5 vs 2/5 wins (5 puzzles). Rewording wrongly answered math items: up to +15.5 pp, no resample control | c18, c19 | [C] (K16) |

## 4. Mechanisms and models

RCT has no executable model in any source we opened. [a26, K20] Predictions are rank orders. Below is what an engineer can build from the theory as written. Parts we had to stipulate are marked.

### 4.1 Problem state

A problem is a tuple (elements, constraints, chunks, goal test).

- Elements: the things that can change.
- Active constraints: rules the solver assumes. Each has a scope level.
- Chunks: groupings of elements treated as one unit. Each has a tightness level.
- Search space: all states reachable while the active constraints and chunks hold.

### 4.2 Impasse

Impasse means the search space is exhausted or the solver is not progressing, and the goal test has not passed. The theory says impasse is the trigger for restructuring. In humans, fixation time rises as impasse sets in. [a09, b04] For our agent the code-checked analogue is the S6 trigger: no pass, two rounds with no change, the same error twice, or a budget fraction spent.

### 4.3 Constraint relaxation (O4)

1. List the active constraints, one line each.
2. Rank them by scope. Narrow ones (this value, this number) are relaxed first. Wide ones (whole-statement rules such as "the statement must stay non-tautological") are relaxed last. In Knoblich's data, ease fell as scope rose: A > B > C. [a02]
3. Relax one constraint. Search again in the enlarged space.
4. Test with the goal check. If it fails, restore the constraint and try the next.

Stipulated: the scope scale is an ordering by the authors' analysis, with no interval scale. [a02] "Relax in increasing scope" is therefore a heuristic, not a measured rule.

### 4.4 Chunk decomposition (O6)

1. Parse the input into units (the default chunking).
2. Rank units by tightness. Loose units (their parts are themselves chunks) split first. Tight units (parts meaningless alone) split last. [a03]
3. Split one unit into parts and re-parse. Search again.

The authors say chunk decomposition is not under conscious control, so it is hard to induce on purpose. [a03] For text tasks the analogue is re-tokenising: reading a word as letters, a phrase as a pun, a number as digits. This analogue is our extension, not tested.

### 4.5 Transfer (memory)

After a change succeeds, the new representation persists. Transfer is by representation type. In 1999, similarity of numerals or order did not matter (F(3,74)=0.34). [a05] In 2026, same-type repetition lifted accuracy 0.32 to 0.75, and mixed types did not. [b10] Implementation: store "representation change that worked" keyed by change type (for example "operator was variable", "tight chunk split"), not by surface features. Offer it only after the first attempt (the SCHEMA memory rule; it avoids fixation).

### 4.6 The rival mechanism: progress monitoring

At each step choose the move that most reduces a distance-to-goal measure. When the remaining moves cannot reach the goal at the current rate, loosen the move-selection criterion. [b17, d05] In Ormerod & MacGregor, moves that reduce number disparity lay on the solution path, which made hard items easy. [d05] Implementation: a distance score and a stall detector that switches strategy. It is cheap and compatible with G1.

### 4.7 Heuristics plus representation (Ollinger 2006)

Representation decides which heuristics apply, and heuristics run only inside the current space. [a16, abstract only] Implementation: representation choice in an outer loop, search in an inner loop. This matches the S2 to S3 structure.

### 4.8 Machine-side triggers and commits

- Entropy trigger (d'Aliberti): when token entropy is high on pass 1, append a reconsideration cue and run a second pass. [c13, d07] Needs logprobs.
- Commit rule (NazoNazo): collect every candidate string in the thought log and test it. [d08] This is S4 harvesting.
- External reformulation: the program, not the model, rebuilds the problem from the story plus selected answers. [c18]

## 5. What holds up

**Replicated.**

- The difficulty order (value / operator / tautology; loose / tight) held in four human samples: Exp 1A, 1B, 2 (1999) and N=189 online (2026), with 80.7% vs 19.2% at the extremes. [a05, a22]
- Tight-chunk problems were harder than loose-chunk ones in Ormerod & MacGregor (low-value 43% vs 77%). [a12]
- Standard tautologies were harder than reverse tautologies at low value (12% vs 72%). [a13]
- Training that removes a hidden constraint helps nine-dot (63% vs 37%; trained groups 30 to 97%). [b12, d11]
- Representation-specific transfer: Knoblich Exp 3 and Nasvytis 2026. [a06, b10]
- Red herrings fixate LLMs across three sources. [c07, c08, c09]

**Partly replicated or contested.**

- Ormerod & MacGregor (2020) is the only independent matchstick replication. The chunk effect replicated. A large value disparity nearly erased it and raised standard tautology solving from 12% to 62%. The interaction was not significant in Exp 1 and was significant in Exp 2. Their claim that relaxation is unnecessary is an interpretation with no model. [a12, a13, d03, d04, d05]
- Jones (2003): the abstract says both theories received support and the manipulations favoured RCT. Not opened. [b17]
- "Heuristics have minimal effect" (Ollinger 2006, 2013) is known from abstracts only. [a16, a18, K08]

**Failures and weak points.**

- A vs B is not reliably significant in frequency. [a05]
- Knoblich Exp 3: an unexpected slowdown on tautological Type A items, explained ad hoc. [a06]
- Graf 2023: only 34% solved in 5 min on one hard problem. The sudden-burst claim depends on method. [b07, b09]
- Fedor 2015: the staged model is not followed. Impasse-button reports did not rise during behaviourally defined impasse stages. [b15]
- Eye-movement effects are modest. The main effect of success was n.s. [b05]
- Mental set (Ollinger 2008, abstract only): sets of non-insight problems gave no set effect on later insight problems. Sets of insight problems gave facilitation or inhibition depending on type. [b20]
- Misleading nine-dot training did not lower solving below control (probable floor). [b12]
- The control rate in Kershaw & Ohlsson 2001 was 37%, while unaided nine-dot is about 0% elsewhere, so the groups differ. [d11]

**Moderators.** Number disparity (largest). Ceiling on easy types. One-lab samples. Online vs lab. Think-aloud may change strategy. [d03, d04, b10]

**Interventions that worked (humans).** Removing a hidden constraint in training (63% vs 37%). Same-type repetition (0.32 to 0.75). A hint ("you can change the operators, too") solved a further 11 points of the sample, but only for some. [b08] Incremental hints (route, meeting dot, non-dot points) gave faster representational change and more solutions (Ollinger 2014, abstract only). [d12]

**Interventions that did not.** Telling people to go outside the square helped only when combined with hints that gave away part of the solution (second-hand). [b13] Misleading training did not lower solving. [b12] Tautology exposure did not help tight chunks. [a06] Surface similarity of the second problem did not help. [a05]

**Insight as a feeling.** Insight reports (74% of solvers vs 10% of non-solvers) measure feeling, not restructuring. [b16]

## 6. Language models

**Human-vs-model gaps on restructuring items.**

- NazoNazo (Japanese riddles, 38 models): reasoning models beat non-reasoning ones (17.6% vs 7.6% on 120 items; odds ratio 2.29, CI 1.99 to 2.64; 19.25% vs 9.42% on all 201). Humans 52.9%. GPT-5 sat inside the human 95% CI (46.6 to 59.2), a descriptive overlap only. Parameter count did not predict accuracy; release date did. [c01, d09]
- BRAINTEASER (2023 ChatGPT): 62.68 sentence, 53.46 word, against human 91.98 and 91.67. Chance is 24.4 and 25.3. Consistency across reworded versions collapses: 60.77 down to 39.71 (sentence), 56.10 down to 29.27 (word). Humans lose about 2 points. This says the model matched surface form. [d01, d02] ChatGPT did best on famous word puzzles, which suggests memorisation. [d02]
- SemEval-2024 Task 9: 182 teams, 483 submissions. Top word-puzzle team 0.983 overall. Baselines: humans 0.920/0.917, ChatGPT 0.627/0.535. 60% of participants fine-tuned. The authors say the task is not solved and shortcut learning of recurring patterns is likely. Few-shot prompting helped consistency on word puzzles but not sentence puzzles. [c06]
- MathSticks: o3 60.00% with text and 38.50% without; humans 91.72% (3 people); many models at 0 to 2%. Sign-changed items are harder (o3 51.45 vs 65.19). The benchmark uses seven-segment digits, so it does not test chunk theory. [d10]
- Classic verbal insight (Orru 2023): ChatGPT 12/30 (7/15 practice, 5/15 transfer), single run, famous items. [c15] On a rebus representational-change task, GPT-4o (estimate 0.31) and GPT-4-turbo (0.46) were below humans (p<.001). Correct trials used reasoning (GPT-4o 68.88%, GPT-4-turbo 71.26%) where humans used transformation (72.41%). [c16]
- Red herrings: GPT-4 6/239 correct groups rising to 471/1926 when herrings are removed. More examples did not help. NYT Connections: the best model fully solves 18%. In a 2024 text-classification version the best model reaches 40.25% vs humans 60.67% (hinted), and 11% vs 39.33% (unhinted). Chain of thought and self-consistency give diminishing returns as red-herring difficulty rises. [c07, c08, c09]
- Mental set (Haq 2025): 6 problems per cell. Anecdote only. [c17]

**Where the failure lies.**

- Generation vs commitment. In four models, 5.23% to 39.34% of wrong answers had the gold string in the thought log before the final answer. Upper-bound recovery: Grok 4 37% to 62%, Claude Opus 4 30% to 48%, DeepSeek-R1 21% to 45%, Gemini 14% to 19%. The count is by literal string match, appears only in v3, and was not preregistered. [d08]
- Language of reasoning is not the bottleneck: Grok 4 29.5% (Japanese) vs 48.8% (English), p=.0071, but Claude Opus 4 36.7% vs 28.7%, p=.356. The model chose the language. [c03]
- Spontaneous restructuring is rare. In small RL models, lexicalised mid-trace shifts occur in 6.31% of traces and go with 2.57% accuracy against 16.44%. DeepSeek-R1 shifts 0.00 to 0.25% and GPT-4o 0.88 to 2.21% in the main table (math-only external table: 0.96 to 1.83% and 2.98 to 7.31%). GPT-4o on MATH-500: shifted 63.2% vs non-shifted 64.9%. Unlexicalised changes may be missed. [c12, d07]

**What changed performance, and by how much.**

- Reasoning mode: odds ratio 2.29 on NazoNazo, but absolute accuracy stays low (19.25% on 201). [c01]
- External forced reconsideration: +8.41 pp on math (32.21 to 40.62), +0.45 pp on crosswords, +0.01 pp on Rush Hour, mainly in the Qwen2.5-1.5B family. Pass 2 costs about twice the tokens. No cue-free second sample was run, so we cannot say the cue beats a plain resample. The +15.38 gain in the high-entropy bucket is partly selection (regression to the mean; our inference). [d06, d07]
- External reformulation: 4/5 vs 2/5 situation-puzzle wins (5 puzzles, one run). Variants K=10/M=6 and wrong-guess-only gave 3/5. [c18] Rewording wrong math items recovered up to 15.5 pp, with no resample control. [c19]
- Machine constraint relaxation in optimisation: an LLM agent proposing alternative constraint models improved 68.5% of cases, but best-of-5 gave 101/150 vs the agent's 102.8/150. [c21] AutoCO's 24.7% gap reduction was against other LLM methods. Its ablations cost 14.10 to 23.73%. [c22]
- Two-agent GPT-4o teams on situation puzzles asked more varied questions and solved worse than solo. 47% of the deficit came through fewer host questions (indirect -0.370, CI [-0.560, -0.183]) and 53% was direct (beta=-0.415, p=.005). This supports G9. [c14]
- More in-context examples did not help on Connections. [c07]

**Not known.** No LLM study tests Roman-numeral chunk theory, the Knoblich order in LLM solve rates, an explicit list-and-relax step against best-of-k on matchsticks, or typed memory by change type. [d15] This is absence in a limited search. The search budget ran out.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

Few items reach [E] here. These are small and consistent with existing guardrails.

1. **Keep O4 and O6 inside S6 only, never on a schedule.** Part: G1, S6. [E] for the trigger principle (G1 is already [E] in SCHEMA.md). Do not hard-code one impasse-then-restructure order; allow looping. Evidence: a01, a09, b15.
2. **Key any "what representation change worked" lesson by change type, not by surface features.** Part: memory (lessons). [E] for humans (K03: Knoblich 1999 and Nasvytis 2026). Evidence: a05, a06, a28, b10, c24. Still shown after the first attempt only. The LLM benefit is untested (test T4), so this enters as a memory design note, not a claim of gain.
3. **Always include a best-of-k arm at equal tokens when testing O4 or O6.** Part: G7. [E] (K17). Evidence: c21 (agent 102.8 vs best-of-5 101 of 150).
4. **Report group consistency (original plus rewordings), not mean accuracy, when testing reframing.** Part: bench harness, G7. [E] for 2023 ChatGPT (K21). Evidence: d01, d02, c05.
5. **Log time or tokens-to-solve per operator, not only accuracy.** Part: logging (SCHEMA section 6). [S] (K02) but free. Evidence: a05, a07, a28.
6. **Control number disparity or item-level cues when testing difficulty order.** Part: bench design. [S] (K24). Evidence: d03, d04.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Constraint-list-then-relax-one (O4 with a listing step: name active assumptions, rank narrow to wide, drop one at a time) | O4, S6 | [S] | a02, a03, a08, b01, K01 |
| Name the hidden constraint ("which assumption is hidden?") vs a generic hint | O4 | [E] for humans, untested for LLMs | a14, b12, d11, K07 |
| Chunk decomposition for text: re-tokenise (letters, digits, pun readings) as a named O6 move | O6 | [S] | a03, a23, c01, K08 |
| Candidate-harvest-and-commit over the thought log | S4, S7 | [S] | b23, c02, d08, K11 |
| Entropy-triggered reconsideration cue vs plain resample | S6 trigger | [S] | c13, d06, d07, K12 |
| Progress-monitoring trigger (switch on stall) vs O6 | G1, S6 | [C] | a12, a13, d03, d04, K06, K22 |
| Typed memory of representation change vs surface-similar retrieval | memory | [S] for LLMs | a22, b10, c24, K03, K23 |
| Scaffold-driven reformulation (program rebuilds the problem) vs plain resample | O6, S1 | [C] | c18, c19, K16 |
| Anti-fixation step: name the tempting frame, then exclude it | S1, S3, O6 | [S] | c07, c08, c09, K13 |
| Order check: do LLM solve rates follow value < operator < tautology and loose < tight? | diagnostic | untested | a02, a03, d15, K01, K23 |

Each row is expanded in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms get equal total tokens (setup, prompts and any second pass included; G7). Use at least 50 items per cell. Report accuracy, tokens to first pass, and consistency across reworded versions.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Roman-numeral matchstick items tagged by type (A, B, C, D) with number disparity held fixed (adapt the public MathSticks generator to Roman numerals) | (a) plain, (b) best-of-k, (c) list constraints then relax one, (d) chunk-split prompt | Solve rate per type; tokens to solve | (c) beats (a) and (b) on types B and C by a few points; no gain on A. Flat solve rates across types mean the model is not using constraint structure |
| T2 | NazoNazo-style riddles (blind split of 159) and BRAINTEASER word and sentence puzzles with semantic and context rewrites | (a) plain reasoning, (b) harvest candidates from the log and test them, (c) harvest plus commit rule | Accuracy; group consistency | (b) recovers part of the 5 to 39% verification failures. Ceiling for Grok-4-like models is 37 to 62%, so expect a few points, not the ceiling |
| T3 | MATH-500-style items plus a non-math puzzle set (crossword, Rush Hour) | (a) single pass, (b) plain second sample, no cue, (c) second sample with reconsideration cue, (d) cue only when entropy is high | Accuracy at equal tokens | (c) vs (b) isolates the cue. The +8.41 pp on math should shrink; non-math gains stay near zero (+0.45, +0.01) |
| T4 | Same matchstick set as T1, five trials per run | (a) no memory, (b) lesson keyed by change type, (c) lesson keyed by surface similarity | Accuracy on trials 2 to 5 | (b) beats (c), as same-type repetition did in people (0.32 to 0.75) |
| T5 | Connections-style grouping with and without red herrings | (a) plain, (b) "name the tempting wrong frame, then exclude it", (c) best-of-k | Fully solved games | (b) closes part of the gap to the no-herring version; size unknown |
| T6 | Matchstick items crossing disparity (low, high) with chunk tightness | (a) plain, (b) progress-monitoring switch on stall (code-measured), (c) O6 at impasse | Success; label each trace for stall-then-switch and for changed representation | Tests K22. If (b) matches (c), drop O6 for matchstick-type tasks |
| T7 | Hidden-constraint items (nine-dot style, eight-coin style, text versions) | (a) generic hint, (b) targeted "what assumption is hidden", (c) none | Solve rate | (b) beats (a), as 63% vs 37% in people |

Run T3 and T2 first (cheapest, data and code exist). T1 needs a generator.

## 9. What does not transfer, and why

- **Eye-movement signatures** (K04). The agent has no gaze. The nearest analogue is whether it treats operators as fixed when it lists assumptions. [a09]
- **Insight feeling and suddenness** (K05, K09). Aha reports measure feeling, and suddenness depends on analysis method. The agent has no use for either. If we ever detect restructuring in traces, use change-point models, not binned means. [b09, b16]
- **"Chunk decomposition is not under conscious control"** (a03). A human-only fact. A program can split a chunk by rule.
- **Human working-memory moderators** (Chein & Weisberg 2014: verbal working memory and attention control explained variation on compound remote associates; N=27 and 26). Different substrate. [b21]
- **Spontaneous Aha in small RL models** (d'Aliberti). It says those models do not restructure by themselves. It does not say a scaffold cannot make them. The study used mostly Qwen2.5-1.5B GRPO checkpoints and detected only lexicalised shifts. [a21]
- **Team effects** (Qiu 2026). Two-agent coordination hurt. Relevant only as support for G9. Our agent is single. [c14]
- **Human-calibrated difficulty orders.** The Knoblich order is human difficulty. A model may find tautology easy and chunk splitting hard. We need the order check (T1) before using it to schedule operators.
- **Machine constraint relaxation** (AutoCO, constraint models). This is explicit optimisation with a solver as validator. It shows relaxation can work with a verifier. The verifier is the transferable part. [c21, c22]
- **The MathSticks benchmark as chunk evidence.** It uses seven-segment digits. A seven-segment "chunk" is not the Roman X. [a24]
- **Mental-set LLM results** (Haq 2025). Six items per cell and no inference. [a20]

## 10. Open questions

1. Does an explicit list-and-relax step beat plain sampling and best-of-k at equal tokens? Nothing tests this. [d15]
2. Do LLM solve rates follow the Knoblich order, and does a scaffold change the order? [K23]
3. How much of the NazoNazo and BRAINTEASER gap is generation and how much is verification? Does a commit rule recover it? [K11]
4. Is d'Aliberti's reconsideration gain larger than a plain second sample at equal tokens, and does it extend to non-math restructuring tasks? [K12]
5. Which explains LLM trace outcomes better: progress monitoring or representation change? [K22]
6. Do Ohlsson (1992, 2011), Ollinger (2006, 2013, 2014) and Jones (2003) report numbers that support K08? Full texts were not obtained. [K25]
7. Is there an executable RCT simulator? Ohlsson (2011) gives only a partial spreading-activation specification. [K20]
8. Does typed memory by representation-change type help LLM agents? [K23]
9. Do the results hold on uncontaminated insight items? NazoNazo has 159 blind items. Classic items (ChatGPT 12/30) may be memorised. [d09, c15]
10. What do 2025 reasoning models score on BRAINTEASER with reconstruction consistency? [d02]
11. Can constraint scope and chunk tightness be measured independently of difficulty, so that "active constraint" is not circular?
12. Why did Grok 4 do worse reasoning in Japanese while Claude Opus 4 did not? Language choice was not randomised. [c03]

## 11. Sources

Marks: [V] opened this session (text read), [M] snippet or abstract only.

- [V] Knoblich, Ohlsson, Haider & Rhenius (1999). Constraint relaxation and chunk decomposition in insight problem solving. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (a01-a08, a26-a28, b01-b03, c23)
- [V] Knoblich, Ohlsson & Raney (2001). An eye movement study of insight problem solving. https://link.springer.com/content/pdf/10.3758/BF03195762.pdf (a09-a11, a29, b04-b06)
- [V] Ormerod & MacGregor (2020). The complementary roles of knowledge and strategy in insight problem-solving. https://cognitivesciencesociety.org/cogsci20/papers/0067/0067.pdf and https://escholarship.org/uc/item/8m02w9c6 (a12, a13, d03-d05)
- [V] Kershaw & Ohlsson (2001). Training for insight: the case of the nine-dot problem. https://conferences.inf.ed.ac.uk/cogsci2001/pdf-files/0489.pdf (a14, b12-b14)
- [M] Kershaw & Ohlsson (2004). Multiple causes of difficulty in insight. https://pubmed.ncbi.nlm.nih.gov/14736292 (a15)
- [V] Kershaw (2004). Key actions in insight problems. https://escholarship.org/uc/item/2df86832 (d11)
- [M] Ollinger, Jones & Knoblich (2006). Heuristics and representational change in two-move matchstick arithmetic. https://irep.ntu.ac.uk/id/eprint/25198/ and https://doaj.org/article/0984fa1657b949aa835a5950d1cd286a (a16, b19, c25, d13)
- [V, abstract only] Jones (2003). Testing two cognitive theories of insight. https://pubmed.ncbi.nlm.nih.gov/14516232/ ; also https://irep.ntu.ac.uk/18103/ [M] (b17; a17, c26)
- [V, abstract only] Ollinger, Jones, Faber & Knoblich (2013). Cognitive mechanisms of insight: eight-coin problem. https://pubmed.ncbi.nlm.nih.gov/22799283/ (a18, b18)
- [V, abstract only] Ollinger et al. (2014). The dynamics of search, impasse and representational change. https://link.springer.com/doi/10.1007/s00426-013-0494-8 (d12)
- [M] Ollinger, Jones & Knoblich (2008). Effect of mental set on insight problem solving. https://irep.ntu.ac.uk/id/eprint/23048/ (b20)
- [M] Ohlsson (1992) chapter and (2011) book. https://www.cambridge.org/core/books/abs/emergence-of-insight/introduction/A6562 ; https://doi.org/10.4324/9781315783239 (a19, d14)
- [V] Fedor, Szathmary & Ollinger (2015). Problem solving stages in the five square problem. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.0105 (b15, b16)
- [V] Graf et al. (2023). Tracing cognitive processes in insight problem solving. https://eprints.whiterose.ac.uk/199182/1/jintelligence-11-00086-v2.pdf (b07-b09)
- [V, abstract-level numbers] Chein & Weisberg (2014). Working memory and insight in verbal problems. https://link.springer.com/content/pdf/10.3758/s13421-013-0343-4.pdf (b21)
- [V] Nasvytis & Fan (2026). Leveraging speech to identify signatures of insight and transfer. https://arxiv.org/pdf/2605.12970 and https://cogtoolslab.github.io//pdf/nasvytis_cogsci_2026.pdf (a22, b10, b11, c24)
- [M] Frontiers in Psychology (2025), interactive matchstick algebra. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg (c27)
- [V] Mizumoto et al. (2025-2026). The Metacognitive Bottleneck: Japanese riddles (NazoNazo). https://arxiv.org/pdf/2509.14704 and https://arxiv.org/pdf/2509.14704v3 (a23, b22-b24, b27, c01-c03, d08, d09)
- [V] Jiang et al. (2023). BRAINTEASER. https://arxiv.org/pdf/2310.05057 (a25, c04, c05, d01, d02)
- [V] Jiang et al. (2024). SemEval-2024 Task 9. https://arxiv.org/pdf/2404.16068 (c06)
- [V] Naeini et al. (2023). LLMs are fixated by red herrings. https://arxiv.org/pdf/2306.11167 (c07)
- [V] Samadarshi et al. (2024). Connecting the Dots: NYT Connections. https://arxiv.org/pdf/2406.11012 (c08)
- [V] NYT-Connections benchmark (2024). A deceptively simple text classification task. https://arxiv.org/pdf/2412.01621 (c09)
- [V] Ji et al. (2025). MathSticks. https://arxiv.org/pdf/2510.00483 (a24, c10, c11, d10, d15)
- [V] d'Aliberti & Horta Ribeiro (2026). The Illusion of Insight in Reasoning Models. https://arxiv.org/pdf/2601.00514 (a21, b25, b26, c12, c13, d06, d07)
- [V] Haq et al. (2025). Is your LLM trapped in a Mental Set? https://arxiv.org/pdf/2501.11833 (a20, c17)
- [V] Qiu, Zhou & Schooler (2026). The cost of coordination. https://escholarship.org/uc/item/2sh4x44p (c14; the cross-check could not match the 47%/53% mediation split)
- [V] Orru et al. (2023). Human-like problem-solving abilities in LLMs using ChatGPT. https://www.frontiersin.org/journals/artificial-intelligence/articles/ (c15)
- [V] Zhang et al. (2025). AI delivers creative output but struggles with thinking processes. https://arxiv.org/pdf/2503.23327 (c16)
- [V] Solving situation puzzles with LLM and external reformulation (2025). https://arxiv.org/abs/2503.18394 (c18)
- [V] Williamson et al. (2025). Syntactic blind spots. https://arxiv.org/pdf/2510.01831 (c19)
- [V, abstract and intro only] Zhang et al. (2025). RM-PoT. https://arxiv.org/pdf/2502.12589 (c20; no benchmark numbers recorded)
- [V] Voboril & Szeider (2026). Improving constraint models with LLM agents. https://arxiv.org/pdf/2608.08127 (c21)
- [V] Liu et al. (2026). Learn to Relax with LLMs: AutoCO. https://arxiv.org/pdf/2509.12643 (c22)
- [M] Cited second-hand only, never opened: Knoblich & Haider (1996); Knoblich & Wartenberg (1998); Ohlsson & Rees (1991); MacGregor, Ormerod & Chronicle (2001); Ormerod, MacGregor & Chronicle (2002); Burnham & Davis (1969); Weisberg & Alba (1981); Lung & Dominowski (1985); DeCaro (2016).
