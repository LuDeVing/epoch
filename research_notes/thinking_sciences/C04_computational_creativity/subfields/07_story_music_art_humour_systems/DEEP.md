# Story, music, art, humour systems: deep document

*Subfield C04.07. Sources: evidence_a to d.jsonl (ids a01 to d21), claims.jsonl (K01 to K20), critique.md. Background-level relevance for the agent: the schema is for single-answer reasoning, and this subfield is about open-ended creative output. The value is in methods warnings and a few testable scaffolds.*

## 1. What it is

This subfield covers programs that make stories, music, pictures and jokes. It has two eras.

**Era 1: hand-built symbolic systems (1970s to 2010s).**
- TALE-SPIN (Meehan 1976, 1977): stories from a simulated world with goals and plans.
- MINSTREL (Turner 1994): King Arthur tales built by recalling and adapting old stories.
- AARON (Cohen, 1972 to 2016): a drawing program with hand-coded rules.
- EMI (Cope, from 1981): recombines patterns from a composer's pieces.
- JAPE (Binsted and Ritchie 1994): punning riddles from a lexicon, schemata and templates.

**Era 2: language models (2021 to 2026).**
- Hierarchical co-writing (Dramatron), plan-draft-rewrite loops (Re3), multi-agent writing (Agents' Room, StoryWriter, COMIC).
- Evaluation work: New Yorker caption benchmarks, Torrance-style tests of stories, joke diversity, homogeneity studies, human-vs-AI detection for poems, images and music.

**Why it matters to us.** We build a scaffold for reasoning, not for art. Three things carry over.
1. Creative output has no code-checkable pass. So the "code selects" and "judge by running" guardrails (G5, G8) face their hardest case here.
2. LLM samples collapse onto a few modes. That bears directly on G4 (samples from one model are not independent).
3. The old systems show what happens when a "creative" step has no filter: lots of output, mostly nonsense (MINSTREL), and what hand-built knowledge fixes (TALE-SPIN).

**Evidence quality warning.** The historic systems have almost no controlled human evaluation (K14). The modern figures are mostly 2022 to 2024 models and often small samples. See section 9.

## 2. History and theories in depth

### 2.1 TALE-SPIN (Meehan 1977) [a01 to a04, opened]
- Idea: a story is the trace of a simulated rational character solving problems.
- World model: plans in Schank-Abelson Conceptual Dependency; four bodily "sigma-states" (hunger, thirst, rest, sex) that start top-level goals; physical maps; relationships (competition, dominance, familiarity, affection, trust, deceit, indebtedness); personality traits (kindness, vanity, honesty, intelligence).
- Meehan splits "rational narration" from "story". Rational but boring ("He ate the honey next to him") is not a story. Something interesting must happen. Difficulty is partly set by the user via character relationships.
- Aesop morals ("never trust flatterers") were turned into initial world settings so that reasonable behaviour yields the moral. Only a handful were done.
- Seven "mis-spun tales" are printed. Each exposed a missing piece of common knowledge. Joe Bear threatens Irving Bird because the program does not see that an indirect answer is an answer. Henry Ant drowns because being in water blocks speech and nobody was asked for help. Each fix was a new rule or fact.
- Fixing created new bugs. After "noticing" was added, the crow noticed the cheese in its mouth, got hungry and ate it, so the fox had nothing to trick. One tale looped (ask for a worm to get honey, then for a worm to learn where worms are, and so on). Fix: never push a goal already on the stack, and mark a failed goal instead of removing it.
- No human evaluation. Fables only.
- Lesson: coherence came from an explicit state (goal stack, world facts) enforced by code. Failures were located in the trace and fixed by a specific rule. That is G2 in spirit (revise from real output).

### 2.2 MINSTREL (Turner 1994) and its tests [a08 to a13, a32]
- Idea: creativity is analogy by adapted recall. Transform-Recall-Adapt Methods (TRAMs) turn a failed search query into a nearby one, recall a story that fits it, and adapt it back. Turner defined creativity as the number and quality of differences from similar works.
- MINSTREL wrote about 200-word King Arthur tales from hand-built Lisp frames (Peinado and Gervas 2006, a12). It has 25 TRAM heuristics (a13). The original code was not available; reconstructions exist (Minstrel Remixed, Skald).
- First formal test: Tearse, Mawhorter, Mateas and Wardrip-Fruin (2011, a08 to a11). They rebuilt it and ran 1000 trials per condition on one main query with a 16-story library (mean 11.5 nodes, 4 nouns) and 7 TRAMs.
  - Only 35.2% of results were sensible. Expected difference between two results about 6.90 fields. 68.8 unique stories per 1000 trials, 21.0 sensible. Unique ratio 0.439. Sensible-to-nonsense ratio 0.544.
  - A more constrained query: sense ratio 0.947 (unique) and 3.103 (total), but expected differences fell to about 3.5 from 7.
  - Removing the two most liberal TRAMs (SimilarOutcomes, GeneralizeConstraint) also raised sense and cut variation (differences about 3 vs 7).
  - Depth limits 3 to 6 were equivalent. Depth 2 gave far fewer results. Most results sit at depth 2.
  - Removing 8 of 16 stories cut unique results and the sense ratio. Unique results fell less than proportionally; sensible ones fell proportionally.
- Skald (Tearse) weights TRAM choice instead of picking at random. Harmon and Jhala (2015, a13): search failure 19% (Minstrel Remixed) vs 3.5% (Skald); TRAMs tried per search 58 vs 16; TRAMs used when no direct match 2.4 vs 1.4. This is a speed and retrieval measure, not a story-quality rating.
- Lesson: novelty and sense trade off by construction. Variety is cheap, sense is not. Better search (indexing, weighting) cut cost without changing the transform step.

### 2.3 AARON (Cohen 1972 to 2016) [a29, a33, b03, c20; Wikipedia only]
- Started from Cohen's 1979 question: what are the minimum conditions for marks to function as an image (a33, not opened).
- Stages: abstract drawing (1970s), rocks and plants, people (1980s), interior scenes, colour. Moved from C to Lisp in the early 1990s.
- It could not learn. Cohen hand-coded each new skill. Source never released. Output follows a recognisable formula (citation-needed tag).
- No evaluation data in any source we opened. Treat AARON as a historical example of expert knowledge encoded as rules, not as evidence.

### 2.4 EMI (Cope, from 1981) [a30, b01, b02, c22, d20; Wikipedia only]
- Recombines patterns analysed from a composer's work. Started after composer's block on an opera commission. About 20,000 lines of Lisp by 2001. Applied to Bach, Mozart, Chopin, Bartok, Brahms and others. 5,000 Bach-style MIDI pieces were published. Cope deleted the database in 2005.
- The one audience claim: in Hofstadter's lecture tours, audiences did no better than chance at telling real Chopin from EMI Chopin-style. No N, no counts, informal. Ariza (2009), the likely primary review, returned HTTP 403. Hofstadter 2001 not opened.
- Output is recombination of a human corpus in a known style. No independent replication is described.
- Status: unverified (K20). Do not cite for numbers.

### 2.5 JAPE and successors [a05 to a07, b04, c21]
- Binsted and Ritchie (1994): JAPE-1 builds punning riddles from a humour-independent lexicon with two layers. Schemata fix the word relations (a fake word made from a homonym or substitution). Templates give the surface question-answer form. Six schemata. Example: "What do you get when you cross a sheep and a kangaroo? A woolly jumper." Only noun-phrase punchlines.
- Lexical entries were written by volunteers, so no hand-tuning to humour.
- Evaluation: 188 jokes, 14 judges, 0 to 5 scale. Mean 1.5. Most scored 1. Nine jokes got a 5 from one judge while the other judge gave the same jokes 0 (3 jokes), 1 (3) and 2 (3). Some output duplicated known jokes ("A cereal killer"). Authors say it was not statistically rigorous: few judges, no control group, jokes seen before.
- Template choice mattered a lot. A weak template ("use syn") gave non-jokes ("What do you use to hit a waiting line? A pool queue."). A better template scored about 2 on average.
- Binsted, Pain and Ritchie (1997, secondary summary only): children aged 8 to 11 rated JAPE riddles, human riddles and non-jokes. JAPE riddles were seen as jokes, rated less funny on average than human riddles, but some matched. No numbers read.
- STANDUP (2007) was tested with children with communication disabilities and showed improvement on some language tests (Wikipedia only).
- Lesson: humour quality depends on the surface template and on judges who disagree a lot. A model-only judge was not an option then, and it is a poor one now (section 6).

### 2.6 Theory frame
- Boden's value, novelty and surprise applied to LLMs (Franceschelli and Musolesi 2024, c11): conceptual, no measurements.
- Ritchie's empirical criteria (typicality, quality, novelty ratios; a34, cited only) are the formal basis for the "differences times quality" measures the 2011 MINSTREL test used.
- Two dividing lines run through all later work: (1) product vs process (is the output good, or was the way it was made creative), and (2) individual vs population (one output can be original while a set of outputs is homogeneous).

## 3. Core findings with exact numbers

Status key: E established (two or more independent sources agree), S single-source, C contested, U unverified.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| TALE-SPIN failures were knowledge gaps, each fixed by a rule or fact; loops stopped by no-repeat goal rule | 7 mis-spun tales; no counts | Meehan 1977 (a01-a04) | S |
| MINSTREL-style recall gives variety but mostly nonsense | 35.2% sensible; 68.8 unique and 21.0 sensible per 1000 trials; 16-story library | Tearse 2011 (a09) | S (one rebuild) |
| Tighter query raises sense, halves variation | sense/nonsense 0.947 vs 0.544; differences about 3.5 vs 6.9 | Tearse 2011 (a10) | S |
| Weighted TRAM search cuts failure and cost | failure 19% to 3.5%; TRAMs tried 58 to 16 | Harmon and Jhala 2015 (a13) | S; K02 counted E on two reads |
| JAPE riddles rated low with judge disagreement | mean 1.5 of 5, 188 jokes, 14 judges | Binsted and Ritchie 1994 (a06) | S |
| ChatGPT joke collapse | 909 of 1008 samples match one of 25 jokes (917 in another passage); top 4 over 50% | Jentzsch and Kersting 2023 (a16, b09) | E (K04) |
| 2025 frontier models still collapse on jokes | direct diversity 17.4 to 30.4 vs 60.2 to 67.2 with verbalized sampling; Rouge-L overlap about 62 to about 17 | Zhang 2025 (d03) | S for new models |
| Hivemind: same-prompt similarity high; cross-model similar | same-prompt above 0.8 usually; cross-model 0.71 to 0.82; min-p leaves 61.2% of pairs above 0.8; 70+ models, 26K queries | Jiang 2025 (d04) | S |
| LLM creative output is homogeneous at population level | AUT variability 0.459 vs 0.738; FF 0.534 vs 0.835; DAT 0.665 vs 0.819; individual originality 0.711 vs 0.696 | Wenger and Kenett 2025 (c14) | E (K05) |
| Model ideas raise each story but make stories alike | 293 writers, 600 raters; novelty +6.7% (b=0.259), usefulness +6.4%; 5 ideas +8.1% and +9.0%; similarity b=0.871 (1 idea), 0.718 (5 ideas); cosine +4.29 points | Doshi and Hauser 2024 (d07, d08) | E with Anderson |
| Group homogenisation, individual not | 33 participants, 1271 ideas; distance to centroid 0.24 vs 0.28, d=0.47, p=0.038; individual p=0.352 | Anderson 2024 (d09) | E (K17) |
| Co-writing with InstructGPT lowers diversity | Rouge-L key-point homogenisation 0.1536 solo, 0.1578 GPT-3, 0.1660 InstructGPT; 300 essays | Padmakumar and He 2024 (b16, b17) | S |
| Sui Generis novelty lower for LLM stories | 100 stories, K=20; score correlates 0.55 with human surprise; other measures 0.46, 0.50 | Xu 2025 (b18, b19) | S |
| Verbalized sampling raises diversity, flat quality on jokes | 1.6 to 2.1 times; human diversity (1 to 4) poem 1.90 to 2.39, story 2.74 to 3.06, joke 1.83 to 3.01; 90 lay annotators; story quality down 5 to 7 points | Zhang 2025 (d01 to d03) | S (K15) |
| Professional stories beat LLM stories on expert tests | New Yorker 84.7% pass (11.9 of 14) vs 8.7 to 30.0% LLM; 48 stories, 10 experts; kappa 0.41; aggregate Pearson 0.69 | Chakrabarty 2024 (a23, b13, c03) | C vs Gomez-Rodriguez |
| GPT-4 beat student writers on a rubric | GPT-4 80.2 overall vs best open 60.0; p=0.00031 on individual metrics; kappa 0.48; 65 stories; one prompt | Gomez-Rodriguez 2023 (a22, b11, c02) | C |
| Novelist beat GPT-4 Turbo | Pron creativity mean 1.94 (about 2x GPT-4); style originality 1.70 vs 0.36 (ES), 0.63 (EN); human titles lifted GPT-4 style originality 57% | Marco 2024 (a25, a26) | S |
| LLM stories lack late turning points | Climax and setback 14.6% and 9.3% in human vs 1.3% and 1.7% in GPT-4; 440 narratives, 16 annotators | Tian 2024 (a27, b20) | S (K09) |
| Arc-aware prompting helps | diversity +45%, suspense and engagement +40% | Tian 2024 (c09) | S |
| Plan-draft-rewrite loop beats rolling window | coherent 60.0 vs 45.7%; relevant 64.0 vs 44.0%; interesting 54.3 vs 45.0%; judged human 83.3 vs 74.0% | Yang 2022, Re3 (c08) | S |
| Planner plus writer agents beat one-pass, still lose to humans | 9,900 pairwise ratings; length preference 0.51; kappa 0.46 | Huot 2025 (c10, d10) | S |
| Persona critics on plan | Interesting 85.00 vs 57.56; Creative 84.33 vs 57.33; Coherent 77.89 vs 67.33; Relevant 96.00 vs 95.11 (ns); text: Creative 89.33 vs 70.67 | Bai 2024, CritiCS (d12) | S |
| New Yorker caption matching | CLIP 62% vs human 94%; GPT-4 5-shot with human descriptions 84.5% | Hessel 2023 (a18, b05) | S |
| Caption quality vs human top-10 | Claude-3-Opus preferred 34 to 35.4% by crowd, 1.6% by a former New Yorker editor; GPT-judged win rate 54.4%; 250M ratings, 2.2M captions | Zhang 2024 (a20, b07, c05) | E (K06) |
| Humour vs lay baseline | ChatGPT 2.63 vs human 2.20 of 6; 69.5% preferred AI; 105 writers, 200 raters | Gorenz and Schwarz 2024 (d13) | S |
| Humour vs professional baseline | Onion 2.49 vs ChatGPT 2.37, p=.14; 217 students | Gorenz and Schwarz 2024 (d14) | S (null, not equivalence) |
| LLM puns and unfunned headlines less funny than human | detector holdout 99% (GPT-4 unfun), 98%, 92% (human); English-Hindi edited text rated humorous 3.6% vs 48% original | Horvitz 2024 (c12) | S |
| Lay readers cannot spot AI poems | 46.6% accuracy; 1,634 participants study 1; 16,340 judgments; AI-labelled poems rated lower | Porter and Machery 2024 (c23) | C vs expert result |
| Experts spot AI stories | GPT-3.5 and GPT-4 stories attributed to AI over 80% | Chakrabarty 2024 (b15) | S |
| Images: general users near chance, artists better | professional artists 75.32% accuracy; experts 83.44% vs best detector 87.76% | Ha 2024 (d17) | S |
| Suno music at chance in random pairs | random pairs 0.53; similar pairs 0.66; similar with lyrics 0.75; 308 participants | Figueiredo 2025 (d18) | S |
| LLM judge reliability varies by setting | story TTCW judge near 0; Agents' Room rho 0.62 by system, 0.41 by item; images r .57 to .68; sketches r .29 to .68; multi-step direct PCC 0.31, CreaEval QWK 0.64 | a24, d11, d15, d16 | C (K07, K19) |
| Dramatron co-writing | 15 professionals, 13 surveys; 92% surprised; 84% helpful; 77% enjoyed; over half low ownership | Mirowski 2022 (a14) | S |
| Comedians' view | 20 comedians; "cruise ship comedy material from the 1950s, but a bit less racist" | Mirowski 2024 (c07) | S |
| EMI audience at chance | no N | Wikipedia (b01, d20) | U |

## 4. Mechanisms and models

### 4.1 Goal-stack story simulator (TALE-SPIN)
Implementation sketch.
1. State: world facts (who is where, who knows what), character records (traits, relationships, bodily states), a goal stack per character.
2. Loop: pick a character with an active goal; expand the goal with a plan from a plan library (preconditions, steps); if a precondition fails, push a sub-goal; execute a step; update facts; emit a sentence.
3. Loop guards: refuse to push a goal already on the stack; mark failed goals as failed so they are not retried; cap depth.
4. Story filter: a "rational narration" becomes a story only if an event that is hard for the character occurs (conflict). Meehan implemented difficulty through relationship settings, so that a request can be refused.
5. Every wrong story is a missing fact or rule. Debug by reading the trace.

For an LLM agent: keep the goal stack and fact list in code or a structured scratch, not in prose. Enforce no-repeat goals in code.

### 4.2 Transform-Recall-Adapt (MINSTREL, Skald)
1. Library of solved cases, each a small structured graph (nodes, typed links).
2. Query: a partial case with a gap (for example "knight must be injured by another knight").
3. Direct recall. If it fails, apply a TRAM: a typed rewrite of the query (generalise a constraint, swap an outcome, change an actor). Recurse to a depth limit.
4. Recall with the transformed query, then adapt the recalled case back to the original constraints.
5. Variation comes from the number of TRAMs and their liberality. Sense comes from the constraint on the query and the library size.
6. Skald improvement: weight TRAM choice by past success instead of random choice; this cut tried TRAMs from 58 to 16 and failures from 19% to 3.5%.
7. Measures to copy: sensible fraction, unique fraction, expected difference between two outputs. Report all three. A single number hides the trade-off.

### 4.3 Schema-and-template humour (JAPE)
- Schema: a relation among lexical items (homonym, substitution) that generates a candidate "fake word".
- Template: a question-answer surface form. Template choice decided funniness more than the schema.
- Filter by judges; keep only schema-template pairs that score. A code-side dedup against known jokes would have removed "A cereal killer".

### 4.4 Plan, draft, rewrite, edit (Re3)
- Plan: premise to setting, characters, outline. Draft: write each passage with the plan and recent text. Rewrite: rerank candidate continuations by premise relevance and coherence, then rewrite. Edit: fix long-range factual contradictions with a detector.
- The Re3 ablation: Plan and Rewrite mattered. Edit did little. The detector had only moderate ROC-AUC.
- Related: Dramatron fixes log line, characters, plot beats, locations, then dialogue per scene. Parallel scene writing caused scene-to-scene inconsistency (a15).

### 4.5 Arc-aware prompting (Tian 2024)
- Annotate or generate an arc label (Rags to Riches, Oedipus and others) and turning points (climax, setback). Put them into the prompt with required placement. Reported diversity +45% and suspense and engagement +40%.
- Gains are on diversity, suspense and arousal measures, not general quality, and the arc was model-generated.

### 4.6 Multi-agent writers and critics
- Agents' Room: planner agents (plot, characters, setting) plus writer agents, orchestrated; rated by writer-annotators (9,900 pairwise ratings). Better than one-pass and two-stage baselines. Human stories still best on every dimension; gap smallest in language use.
- CritiCS: persona critics revise the plan, then the text, over 3 rounds. Pairwise win figures in section 3. Costs extra tokens, not controlled.
- COMIC: role agents plus critics aligned to YouTube preferences plus island evolution of scripts. Win rate 0.44 vs 0.30 without refinement; win rate rose until generation 4. Within-pool ratings, not absolute funniness.
- StoryWriter: outline, planning and writing agents with a sliding window over history.
- Token costs are higher than baselines in all of these. None is at equal tokens.

### 4.7 Diversity repair
- Verbalized sampling: ask for k outputs with probabilities in one call. Raises diversity 1.6 to 2.1 times. The authors blame typicality bias in human preference data for mode collapse. Larger models gain 1.5 to 2 times more than small ones.
- Min-p decoding does not fix it (61.2% of pairs above 0.8, d04).
- Tulu-70B: diversity falls after SFT and DPO; VS keeps more (d01).
- Cost warning: story quality fell 5 to 7 rubric points; joke quality stayed flat.

### 4.8 Metrics worth reusing
- Population variability: mean cosine distance across responses (AUT 0.459 vs 0.738).
- Sui Generis score: novelty of each segment against K=20 model continuations; correlates 0.55 with human surprise.
- Torrance-based tests (TTCW): 14 binary tests on fluency, flexibility, originality, elaboration.
- Pairwise comparison with Bradley-Terry strengths; check order-swap consistency (Agents' Room 90.2%).
- Two-stage judging (CreaEval): extract evidence, then score with memory.

## 5. What holds up

### 5.1 Solid
- **Collapse onto a few modes.** Four lines agree: Jentzsch (25 jokes), Wenger and Kenett (cosine), Jiang (similarity above 0.8, cross-model 0.71 to 0.82), Zhang (joke diversity 17 to 30 for 2025 models). It holds for 2025 frontier models on jokes. The exact "25 jokes cover 90%" was not re-run.
- **Individual gain, collective loss.** Doshi and Hauser (randomised, 293 writers) and Anderson (within-subject, 33) agree. Anderson's individual-level test was not significant; the group-level d was 0.47.
- **Lay raters cannot separate AI from human art.** Poems 46.6%, images near chance for general users, Suno 0.53 for random pairs. Professional artists reach 75.32%. Matching pairs raised music detection to 0.66.
- **Humour is the weakest creative skill for models, against skilled humans.** Caption study: 1.6% (expert) and 35.4% (crowd) preferences for the model over human top-10. The picture changes with a weak baseline: ChatGPT beat lay humans (2.63 vs 2.20) and tied The Onion (p=.14).
- **Retrieval search cost depends on indexing** (MINSTREL vs Skald), not only on the transform step.

### 5.2 Contested
- **LLM-as-judge for creativity.** Near zero for stories per item (TTCW). rho 0.62 by system but 0.41 by item (Agents' Room). r .57 to .68 for zero-shot image creativity, but edge density alone gave r=.64 on sketches, so the judge may track visual complexity. Direct judging of multi-step tasks PCC 0.31; two-stage 0.64 QWK. Judges lose agreement on similar-quality pairs and on items where humans disagree (d06). The GPT judge gave Claude 54.4% while humans gave 35.4% and 1.6%. Agreement among LLM judges (Kendall tau 0.889, HumorRank) is stability, not validity.
- **Do LLMs beat human writers?** Chakrabarty (professional baseline, expert raters, 2023 models): no, 3 to 10 times fewer tests passed. Gomez-Rodriguez (student baseline, one prompt, 5 human stories): GPT-4 ahead on 8 of 10 items. Baseline and rater decide.
- **Lay vs expert detection.** Lay readers cannot tell AI poems apart; experts attribute GPT-3.5 and GPT-4 stories to AI over 80% of the time.

### 5.3 Interventions that worked
- Plan plus rewrite (Re3: +14 points coherent, +20 relevant).
- Arc and turning-point guidance (diversity +45%, suspense +40%).
- Planner plus writer agents (preferred by writer-annotators, human still wins).
- Persona critics on a plan (Interesting 85.0 vs 57.6).
- Verbalized sampling for jokes (diversity 17 to 60, quality flat).
- Human-chosen titles lifted GPT-4 stories (style originality +57%, anthology suitability +45%).
- Better retrieval indexing (MINSTREL to Skald).
- Few-shot or description help on caption tasks (GPT-4 5-shot 84.5% with human descriptions).

### 5.4 Interventions that did not work, or backfired
- Min-p decoding for diversity (61.2% of pairs still above 0.8).
- Plain chain-of-thought on Oogiri humour (no fix). Plain fine-tuning on Oogiri data helped little. Training on structured thought leaps did help (+4.3 to +10.4 points; +4.55 and +5.91 vs LLaMA3-70B and GPT-4o), but that is training, outside our scope.
- SFT on top-1000 captions hurt; RLHF gave less than best-of-N; PPO moved the wrong way; DPO helped the best-pick win rate (a20, c05).
- More model ideas: five ideas gave more novelty (+8.1%) but did not remove homogenisation. High-creativity writers did not gain from ideas.
- Few-shot prompts for LLM TTCW judges for a couple of tests did not help.
- Simply writing longer (length preference 0.51).
- Verbalized sampling cost 5 to 7 rubric points on stories.
- Instruction tuning (InstructGPT) increased co-writing homogenisation more than GPT-3.

### 5.5 Moderators
- Baseline (lay vs professional), rater expertise (lay vs expert), unit (individual vs population), model era (2022 to 2025), and prompt shape (list or distribution vs single).
- Domain: puns and edited headlines are weaker than stories. Humour was the lowest rubric item (mean 3.4 of 10; best 6.5).
- Volume asymmetry in Gorenz and Schwarz: ChatGPT made 20 jokes per prompt, humans 1, so the AI figure comes from a sampled set and not from a single try.

## 6. Language models

### 6.1 How they behave
- **Stories.** Fluent, coherent, uniformly positive, low tension, turning points too early or missing (climax 1.3% vs 14.6%). Experts pass LLM stories 3 to 10 times less often (8.7%, 27.9%, 30.0% vs 84.7%). Experts also attribute them to AI over 80% (GPT-3.5, GPT-4). Models were 2023; no frontier 2025 to 2026 story test with matched tokens exists in our set.
- **Jokes.** Mode collapse, then confident explanations of non-jokes (explained 23 of 25 valid jokes; invented explanations for invalid ones). Detection by surface form: removing one feature split classification about evenly; removing two gave 0 of 25 as jokes in sets B and D.
- **Puns.** GPT-4-Turbo and Claude-3-Opus rival prior systems on success rate (prior state of the art 56% homographic, 47% heterographic) but fall into lazy pun patterns and are weaker on heterographic puns. CoT improved recognition accuracy.
- **Captions.** Below top human captions; fine-tuning and preference training gave small or negative gains; best-of-N on a reward model beat PPO.
- **Oogiri (2025).** GPT-4.1, Gemini 2.5 Pro and Claude Sonnet 4 write at the level of low to mid-tier humans, weakest on Empathy. LLM judges weight Novelty, humans weight Empathy.
- **Improv (2026).** Multi-agent scenes are coherent but too polite and positive.
- **Co-writing.** Professionals find output surprising (92% of 13) and helpful, but low ownership, bias, plagiarism concerns, stock tropes; safety filters erased minority perspectives (comedians).
- **Images and music.** Lay detection near chance; professional artists 75.32%; detectors best but fragile. Suno songs at chance in random pairs.

### 6.2 What changed output, by how much
| Change | Effect | Cost or caveat |
|---|---|---|
| Plan and rewrite loop (Re3) | coherent +14.3 pts, relevant +20.0 | extra calls; GPT-3 era |
| Arc or turning-point prompt | diversity +45%, suspense +40% | model-made arcs; not overall quality |
| Hierarchical prompts (Dramatron) | long coherent scripts; 84% helpful | no control arm |
| Planner plus writers (Agents' Room) | preferred by writers; human still best | more tokens |
| Plan critique (CritiCS) | Interesting 85.0 vs 57.6 | gpt-3.5; in-house raters; 3 rounds of extra tokens |
| Critic population (COMIC) | win rate 0.44 vs 0.30 | within-pool |
| Verbalized sampling | diversity 1.6 to 2.1x; jokes 17 to 60 | stories lose 5 to 7 points |
| Human-chosen titles | style originality +57% | human in loop |
| Model ideas to writers | novelty +6.7%; more alike across writers | lay writers |
| Min-p decoding | little diversity gain | n/a |
| Larger model with VS | 1.5 to 2x more gain than small | |

### 6.3 Model-as-judge
See 5.2. Use it to rank systems over many items, not to pick one best draft. Two-stage evidence-then-score is better than direct scoring on multi-step tasks. Order-swap consistency is 90.2%, so it is stable but not valid.

## 7. What our agent should take

Relevance is background (the schema targets checkable reasoning problems). Most items are cautions that support existing guardrails. None of these requires new schema parts now.

### Add now (established)

1. **Population diversity is lower than it looks, so do not count same-model or cross-model samples as independent.** Schema: G4 (already present). Status [E]. Evidence: a16, b09, c14, d03, d04, d07 to d09. Use: when S3 produces N attempts, measure pairwise embedding similarity in code and drop near-duplicates before S7. Cross-model swaps give 0.71 to 0.82 similarity, so a model swap is not an independence source (K16, [S], d04).
2. **Never let the generating model pick the best creative output.** Schema: G8, G5. Status [E] for "model judges unreliable per item" in stories (a24, d11 at 0.41), but the overall status of LLM judges is [C] (K07). Use: for open-ended tasks, selection goes to code (dedup, constraint checks, rule tests) or a human panel. Where a judge is used, use it to compare methods across many items (system-level rho 0.62) and use a two-stage evidence-then-score form.
3. **Report the trade-off, not one number, for any variety-generating step.** Schema: G7. Status [E]. Evidence: a09 to a11 (sense vs variation), d03 (diversity up, story quality down). Use: whenever an operator raises variety, record the check-pass fraction and the distinct fraction at equal tokens.
4. **Revise from located failures in a state trace.** Schema: G2, S5. Status [S] from TALE-SPIN (a02, a03) but consistent with established G2. Use: keep goal and fact state in code; stop loops with a no-repeat rule on goals or operators; mark failed goals instead of deleting them. This matches S6 (impasse fired by code).
5. **Evaluate with matched baseline and expert raters; lay indistinguishability is not quality.** Schema: G8 (evaluation hygiene for our bench). Status [E] on the method lesson (K11, K18; K08 is contested on results). Evidence: c23, b15, d13, d14, d17, d18.
6. **Retrieval cost depends on indexing.** Schema: O7, memory. Status [E] (two reads, one rebuild and one follow-up). Evidence: a09 to a13. Use: library lookups for analogues should be typed and weighted by past success, and report the sensible fraction.

### Test first (not established; none goes into SCHEMA.md until its test passes)

1. **Plan-then-write with critique beats plain long generation at equal tokens.** O3, G7. [S]. c08 (Re3), c10, d10, d12. No equal-token test exists.
2. **Explicit arc and turning-point plan.** O3, S6. [S]. a27, c09.
3. **Verbalized-distribution prompt vs k independent attempts plus code-side diversity selection.** G4, G5, S3. [S]. d01 to d03, d04.
4. **Fresh context per attempt, no prior candidates visible (counter to the homogenisation seen when models see ideas).** S3, G4. [S]. d07 to d09. Tests whether the schema's S3 rule holds for idea generation.
5. **Two-stage judge (evidence then score) for any soft rubric.** G8, G5. [C]. d16, d11, d15.
6. **Typed retrieval from solved cases with adaptation (MINSTREL, Skald) for LLM creative tasks.** O7, memory. [S]. a13; no LLM evidence yet.
7. **Frame-switch step ("propose a different frame, not a variation") when later candidates drift toward earlier ones.** O8, G4. [S]. d07 to d09, d04.
8. **Short leap-prompt for humour or association tasks.** G11. [S]. b22 to b24 (training only). Likely not worth testing unless a cheap prompt form is available.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (setup cost counted). Items are open-ended tasks with a code-side or blind-human score. "Plain" means the same model with one direct prompt, best of the equal-token budget by random pick.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 30 short-story prompts (about 300 words) with 4 hidden requirements (must include object X, a reversal in the last third, named turning points) | Plain long write vs plan (arc and turning points) then write then one critique-and-rewrite | Code-checked hit rate for the hard requirements; blind expert pairwise preference (3 raters, order-swapped) | Plan arm better on requirement hit rate by 10 to 20 points (Re3 scale: +14 to +20); preference gain uncertain |
| T2 | 20 prompts "Write a joke about X" and 20 "name a product for Y" | (a) k independent attempts, random pick; (b) k attempts plus code-side embedding dedup and farthest-point pick; (c) one verbalized-distribution call returning k | Distinct count among 50 samples; mean pairwise cosine; blind lay diversity and quality ratings (30 raters) | (b) and (c) raise distinct count and drop similarity; quality flat for jokes; watch a 5 to 7 point story quality drop |
| T3 | 15 prompts per type from T2 | Each attempt in a fresh context vs attempt shown prior candidates ("do something different") | Pairwise similarity to earlier candidates; novelty by embedding distance | Visible-candidate arm moves toward earlier candidates (Doshi b about 0.7 to 0.9); fresh-context arm stays apart |
| T4 | 60 pairs of story or joke outputs with expert labels (or a small expert panel on 60 items) | Direct judge vs two-stage evidence-then-score judge vs random | Spearman with expert panel per item; agreement on near-equal pairs | Per-item rho for direct judge about 0.4 (Agents' Room); two-stage higher; neither above 0.7 |
| T5 | 20 joke prompts, one pass each at 3 temperatures and 3 phrasing sets | Plain default vs list-of-k prompt | Fraction of outputs matching top-5 jokes (recount of the 25-joke collapse on our model) | If top-25 still covers above 50%, collapse persists on our model |
| T6 | 20 tasks needing an analogue from a library of solved cases (hardware debug or story gaps) | No retrieval vs untyped retrieval vs typed filtered retrieval (weights by past success) | Sensible fraction; unique fraction; cost in calls | Typed filter raises sensible fraction (MINSTREL 0.544 to 0.947 sense ratio under a tight query) and halves variation |
| T7 | 40 story prompts | Goal-stack scaffold with no-repeat rule vs plain | Rate of looping, contradictions and dead-end scenes (code and blind count) | Fewer loops and contradictions; no gain in interestingness |
| T8 | 20 caption or one-liner tasks with a real human top-10 baseline | Plain vs best-of-N with code filters for duplicates and reward model | Pairwise preference vs the human top-10 by an expert plus crowd | Remain below 50% with an expert rater (Claude-3-Opus 1.6%); use only as a ceiling check |

## 9. What does not transfer, and why

- **No checkable answer.** Our schema wins by code checks on held-out examples (G3). Creative tasks have no such check. That is why the evidence for scaffold gains here uses rater preferences with kappa 0.19 to 0.52.
- **The historic systems give no effect sizes.** TALE-SPIN, AARON and EMI have no controlled evaluation. Only MINSTREL (2011 rebuild) and JAPE (1994, 14 judges, authors call it not rigorous) have numbers. EMI's "chance-level" claim has no N.
- **Hand-built world models.** TALE-SPIN's gains came from hand-written rules for each missing fact. A language model already holds much of that knowledge. The transferable part is the control structure (goal stack, no-repeat rule), not the facts.
- **Rater and baseline differences.** Results swing from "GPT-4 beats students" to "3 to 10 times worse than professionals." Our own bench has neither a professional baseline nor expert raters, so effect sizes here cannot be ported.
- **Model era.** Most numbers are GPT-3, GPT-3.5, GPT-4, Claude 1.3 to 3. The 2025 evidence confirms jokes only. Frontier 2025 to 2026 models were not tested on stories with matched tokens.
- **Diversity measures.** Embedding similarity is not human-rated sameness (Jiang). Short answers and lists inflate similarity.
- **Training-time methods.** CLoT, SFT, RLHF and DPO results do not apply under our no-training rule.
- **Population vs individual.** Our agent returns one answer. Homogenisation is about collections of outputs; it matters for us only when the agent is asked to produce several candidates (G4) or when many users share one model.
- **Co-writing and ownership results.** Small samples (n=13 survey, 33, 20 comedians). Outside agent design.
- **Music and art as targets.** Evidence is detection and survey, not scaffolds. No usable evidence for our agent.

## 10. Open questions

1. Does plan plus critique beat plain sampling at equal tokens, rated blind by experts against a skilled-human baseline? (Agents' Room and CritiCS show gains over baselines with extra tokens, not at equal tokens.)
2. Does a code-side similarity selector over N independent attempts raise human-rated novelty without lowering quality? (Verbalized sampling raises diversity, flat on jokes, minus 5 to 7 on stories; no selector study.)
3. Is the story turning-point gap (1.3% vs 14.6%) still present in 2025 to 2026 models?
4. EMI test counts and Cope's later blind listening studies: only an unquantified Wikipedia line. Need Hofstadter 2001 or Ariza 2009.
5. Humour with an average baseline on current models, and with expert raters.
6. Does retrieval from a library of solved cases with typed adaptation help LLM creative tasks, and what fraction is sensible? No LLM study with numbers found.
7. Human preference ratings for AI art and music at scale: not found. Only detection.
8. Does best-of-N or temperature fix co-writing homogenisation for newer instruction-tuned models? Not tested in Doshi or Anderson.
9. What explains the judge split: is a creativity judge tracking a real quality or a surface feature (edge density gave r=.64 on sketches)?
10. Can the Sui Generis score (0.55 with human surprise) serve as a code-side novelty filter, and at what cost?
11. Does volume asymmetry (20 AI jokes vs 1 human joke per prompt) explain part of AI wins against lay writers?
12. Source gaps: a21, c13 to c19 not fully re-opened; a31 to a34, c24, c25 never opened; b22 to b25 numbers partial; Sarmento 2024 read for abstract and method only.

## 11. Sources

[V] opened (full text or page); [M] snippet or secondary summary only.

- [V] Meehan (1977) TALE-SPIN, an interactive program that writes stories. https://www.ijcai.org/Proceedings/77-1/Papers/013.pdf (a01 to a04)
- [M] Meehan (1976) The Metanovel. https://dspace.mit.edu/handle/1721.1/16081 (c24, recalled)
- [V] Binsted and Ritchie (1994) An implemented model of punning riddles. https://arxiv.org/abs/cmp-lg/9406022 (a05 to a07)
- [M] Binsted, Pain and Ritchie (1997) children's judgments of JAPE riddles, secondary summary. https://www.futilitycloset.com/2014/04/25/the-pun-also-rises/ (b04)
- [V] Tearse, Mawhorter, Mateas and Wardrip-Fruin (2011) Experimental results from a rational reconstruction of MINSTREL. https://kt.ijs.si/senja_pollak/CC_resources/corpus/Proc_folders/2011/2011_11.txt.txt (a08 to a11)
- [V] Peinado and Gervas (2006) Minstrel Reloaded. https://www.fdi.ucm.es/profesor/fpeinado/publications/2006-peinado-minstrel.pdf (a12)
- [V] Harmon and Jhala (2015) Imaginative recall with story intention graphs. https://drops.dagstuhl.de/storage/01oasics/oasics-vol045_cmn2015/OASIcs.CMN.2015.72/OASIcs.CMN.2015.72.pdf (a13)
- [M] Turner (1994) The Creative Process. https://doi.org/10.4324/9780203773581 (a32, c25)
- [M] Cohen (1979) What is an image? https://www.ijcai.org/Proceedings/79-2/ (a33)
- [M] Ritchie (2007) Empirical criteria for attributing creativity to a computer program. https://link.springer.com/article/10.1007/s11023-007-9066-2 (a34)
- [V] Wikipedia, AARON. https://en.wikipedia.org/wiki/AARON (a29, b03, c20)
- [V] Wikipedia, David Cope and Experiments in Musical Intelligence. https://en.wikipedia.org/wiki/Experiments_in_Musical_Intelligence and https://en.wikipedia.org/wiki/David_Cope (a30, b01, b02, c22, d20)
- [V] Wikipedia, Computational humor. https://en.wikipedia.org/wiki/Computational_humor (c21)
- [M] Hofstadter (2001) Staring Emmy straight in the eye (via Wikipedia). https://en.wikipedia.org/wiki/Experiments_in_Musical_Intelligence (a31)
- [M] Ariza (2009) The Interrogator as Critic. https://direct.mit.edu/comj/article/33/2/48/94232 (d21, HTTP 403)
- [V] Mirowski et al. (2022/2023) Co-writing screenplays and theatre scripts with language models (Dramatron). https://arxiv.org/abs/2209.14958 (a14, a15, c06)
- [V] Mirowski et al. (2024) A Robot Walks into a Bar. https://arxiv.org/abs/2405.20956 (c07)
- [V] Wordcraft (2021). https://arxiv.org/abs/2107.07430 (b25)
- [V] Jentzsch and Kersting (2023) ChatGPT is fun, but it is not funny. https://arxiv.org/abs/2306.04563 (a16, a17, b09, b10, c01)
- [V] Hessel et al. (2023) Do androids laugh at electric sheep? https://arxiv.org/abs/2209.06293 (a18, a19, b05, b06, c04)
- [V] Zhang et al. (2024) Humor in AI. https://arxiv.org/abs/2406.10522 (a20, b07, b08, c05)
- [V] Horvitz et al. (2024) Getting serious about humor. https://arxiv.org/abs/2403.00794 (a21, c12)
- [V] Gomez-Rodriguez and Williams (2023) A Confederacy of Models. https://arxiv.org/abs/2310.08433 (a22, b11, b12, c02)
- [V] Chakrabarty et al. (2024) Art or Artifice? https://arxiv.org/abs/2309.14556 (a23, a24, b13 to b15, c03)
- [V] Marco, Gonzalo and Mateo-Girona (2024) Pron vs Prompt. https://arxiv.org/abs/2407.01119 (a25, a26)
- [V] Tian et al. (2024) Are LLMs capable of generating human-level narratives? https://arxiv.org/abs/2407.13248 (a27, a28, b20, b21, c09)
- [V] Padmakumar and He (2024) Does writing with language models reduce content diversity? https://arxiv.org/abs/2309.05196 (b16, b17)
- [V] Xu et al. (2025) Echoes in AI (Sui Generis). https://arxiv.org/abs/2501.00273 (b18, b19)
- [V] Zhong et al. (2024) Leap-of-Thought (CLoT) for Oogiri. https://arxiv.org/abs/2312.02439 (b22, b23)
- [V] Humor reasoning-path training (ICLR 2025). https://arxiv.org/abs/2410.10370 (b24)
- [V] Yang et al. (2022) Re3. https://arxiv.org/abs/2210.06774 (c08)
- [V] Huot et al. (2025) Agents' Room. https://arxiv.org/abs/2410.02603 (c10, d10, d11)
- [V] Franceschelli and Musolesi (2024) On the creativity of large language models. https://arxiv.org/abs/2304.00008 (c11)
- [V] Xu et al. (2024) A good pun is its own reword. https://arxiv.org/abs/2404.13599 (c13)
- [V] Wenger and Kenett (2025) We're different, we're the same. https://arxiv.org/abs/2501.19361 (c14)
- [V] Oogiri multi-dimensional analysis (2025). https://arxiv.org/abs/2511.09133 (c15)
- [V] HumorRank (2026). https://arxiv.org/abs/2604.19786 (c16)
- [V] COMIC (2026). https://arxiv.org/abs/2603.11048 (c17)
- [V] Spotting the Artificial (2026). https://arxiv.org/abs/2611.00492 (c18)
- [V] StoryWriter (2025). https://arxiv.org/abs/2506.16445 (c19)
- [M] Porter and Machery (2024) AI-generated poetry is indistinguishable from human-written poetry. https://doi.org/10.1038/s41598-024-76900-1 (c23; critique.md reports it was later opened and 46.6% and 1,634 participants confirmed)
- [V] Zhang et al. (2025) Verbalized Sampling. https://arxiv.org/abs/2510.01171 (d01 to d03)
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954 (d04 to d06)
- [V] Doshi and Hauser (2024) Generative AI enhances individual creativity but reduces collective diversity. https://arxiv.org/abs/2312.00506 (d07, d08)
- [V] Anderson, Shah and Kreminski (2024) Homogenization effects of LLMs. https://arxiv.org/abs/2402.01536 (d09)
- [V] Bai et al. (2024) Collective Critics for Creative Story Generation. https://arxiv.org/abs/2410.02428 (d12)
- [V] Gorenz and Schwarz (2024) How funny is ChatGPT? https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0305364 (d13, d14)
- [V] Orwig and Beaty (2026) How LLMs see creativity. https://arxiv.org/abs/2606.29672 (d15)
- [V] Wang et al. (2026) CreaEval. https://arxiv.org/abs/2609.03432 (d16)
- [V] Ha et al. (2024) Organic or Diffused. https://arxiv.org/abs/2402.03214 (d17)
- [V] Figueiredo et al. (2025) Echoes of Humanity (Suno). https://arxiv.org/abs/2509.25601 (d18)
- [V, abstract and method only] Sarmento, Loth and Barthet (2024) Between the AI and Me. https://arxiv.org/abs/2407.21615 (d19)
