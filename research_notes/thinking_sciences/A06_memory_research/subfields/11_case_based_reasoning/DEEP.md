# Case-based reasoning: deep document

*Subfield A06.11. Built from evidence_a-d.jsonl (ids a01-a32, b01-b32, c01-c26, d01-d18), claims.jsonl (K01-K28) and critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested. "Own-group" means the paper was written by the people who proposed the method.*

## 1. What it is

Case-based reasoning (CBR) solves a new problem by finding a similar solved problem, reusing its solution, fixing it where it does not fit, and storing the result. The idea came from Roger Schank and Janet Kolodner in the late 1970s and 1980s. The standard four-step form is Retrieve, Reuse, Revise, Retain (Aamodt and Plaza 1994; not opened this session: a32, b30, c24). The older six-step form is: assign indexes, retrieve, modify, test, store if it worked, explain-repair-test if it failed (Slade 1991, a02).

Two claims sit at the core.
- Memory and reasoning are one process. Remembering a past case is how you reason about the new one (a01).
- Failure is the learning trigger. A failed case, once explained, changes how future problems are indexed (a02, a03).

Why it matters for our agent: our schema wants a subgoal library (S9 record, retrieval by similarity). CBR is the oldest theory of that library. 2023-2026 LLM-agent papers are now building it under other names (workflow memory, strategy memory, skill library, in-context experience replay).

What we found, in one paragraph. Retrieving a few similar, verified, solved cases usually beats no memory and beats random cases. The key used to retrieve matters a lot. Wrong cases are copied and re-stored, so the Retain gate matters more than the Retrieve step. Gains are large on templated tasks and small or negative on structurally new ones. No study tests a library of solved subgoals at equal tokens on reasoning benchmarks. That is the gap we should fill.

Scope notes. Recognition-primed decisions, analogical retrieval (MAC/FAC), transfer of learning, case-base maintenance and retrieval as a bandit are researched in parallel subfields. We refer to them only where they touch.

## 2. History and theories in depth

### 2.1 Origins: scripts, MOPs, reminding (1977-1989)
- Schank's scripts grew into Memory Organization Packets (MOPs). The claim: reminding and learning are one memory process. People are reminded across domains when two events share an abstract expectation failure, not surface features (the steak and the haircut example) (a01, a05). The evidence was anecdotes Schank collected from colleagues and students. No sample size, no control (a05).
- Kolodner's CYRUS (1980) held an episodic memory of events about one official and answered questions by indexed retrieval (a04).
- Named early systems: CYRUS 1980, IPP, MEDIATOR 1985, JUDGE 1986, CHEF 1984-89, HYPO 1987 (a01). All were narrow-domain demonstrations. The review gives no baseline comparisons and no success rates (a01, a03, a04).

### 2.2 The six-step cycle and four knowledge stores (Riesbeck and Bain 1987, via Slade 1991)
Steps: assign indexes, retrieve, modify, test, assign and store (if it worked), explain-repair-test (if it failed). Four knowledge structures: indexing rules, modification rules, repair rules, case memory (a02). In early systems the first three were hand-built. The theory said they should be learned from cases. The early systems did not do it (a02).

### 2.3 CHEF: failure-driven planning (Hammond 1984-89)
CHEF plans recipes. It retrieves the old recipe that matches the most new goals, modifies it, simulates it with causal rules about cooking, explains goal failures, repairs, and stores the repair indexed by the failure it learned about. Worked example: a strawberry souffle adapted from vanilla fails to rise from excess liquid. The repair adds whipped egg whites. The lesson later helps a raspberry souffle (a03). No success rates are in the review. The CHEF primary paper was not opened (c25).

### 2.4 MEDIATOR and rejecting a retrieved case
MEDIATOR picked the Korean territory split as a precedent. The proposal failed on the Sinai case because the goals differed. The failure explanation led to a different precedent (a04). Lesson: a case can match on the surface and be wrong on goals. Reject and re-retrieve.

### 2.5 The indexing problem
"Determining the significant input features is a persistent problem" (Slade, a05). Kolodner (1991) took a pragmatic line. The right index depends on which reasoning task the case serves and which description of the old case explains its outcome. Sometimes surface features are right, sometimes abstract ones (a08). She also noted that machines can retrieve cases novices miss, and can show failed cases with explanations so users do not discount them (a08).

### 2.6 Human use of cases (Kolodner 1991, second-hand)
People use cases naturally, most when uncertain and when learning. They retrieve poorly, reuse without validating, and are biased by cases (a06). Experts (mechanics, physicians, architects, caterers) recall, merge and adapt old cases. Klein and colleagues found analogs beat abstract rules in naturalistic decisions (a07). Both summaries are second-hand and have no numbers. Recognition-primed decision making is a parallel subfield.

### 2.7 Adaptation-guided retrieval (Smyth and Keane 1998)
Argued that the most similar case is not always the most adaptable. Retrieve by cost of adaptation. Not opened (sciencedirect returned 403); known from memory (c26). It has not been tested on LLM agents in any source we found (critique gap 8).

### 2.8 Fielded CBR
Compaq SMART/QuickSource (1993): about 20 percent fewer calls for the printer line than a comparison product. Estimated saving 10 to 20 million dollars a year, extrapolated. About 500 cases audited, a one-week sample, error margin about 5 percent, exact figures withheld. The comparison was between two product lines adjusted by expert judgement. A vendor report, not a controlled trial (a09, K19).

### 2.9 The human retrieval-gap literature
- Gick and Holyoak (1980, 1983): the fortress story and the Duncker radiation problem. People rarely use a solved analog unless told it is relevant. As quoted in Loewenstein et al. (1999): about 41 percent apply the convergence solution spontaneously after the fortress story, about 85 percent after a hint. The originals were not opened. An older "10 percent alone" figure was not on any opened page (critique correction 3; a10, b31).
- Gentner, Rattermann, Forbus (1993), as quoted: surface-matched probes cued recall 55 percent, purely relational matches 12 percent. Original not opened (a11).
- Ross (1984, 1987, 1989): remindings by surface features shape later problem solving. Not opened (b32).
- Loewenstein, Thompson, Gentner (1999), opened: negotiation cases (a12-a14, section 3).
- 2026 re-tests, opened: Raynal et al. (d01) and a Barcelona Fortress-to-Radiation re-run (d02). See section 5.

### 2.10 The LLM wave (2022-2026)
Five families:
1. Nearest-neighbour example selection: KATE 2022, EPR 2022, Skill-KNN 2023 (b18, d16, d10).
2. Trajectory and skill memory: Voyager 2023, Synapse, ExpeL, Sarukkai 2025, Memento 2025, CASCADE 2026 (a21, a20, a16, b21, c01, c04).
3. Distilled-unit memory: Agent Workflow Memory, ReasoningBank, Memp, Buffer of Thoughts, Dynamic Cheatsheet (a19, a27, b05, d18, d17).
4. Explicit CBR-cycle systems: DS-Agent 2024, CBR-RAG 2024, CBR-LLM driving 2025, CASCADE 2026 (c08, a15, a24, c04).
5. Memory-safety and benchmark work: Xiong 2025 on experience-following, MINJA, AgentPoison, Evo-Memory (a22, d06, d07, c19).

## 3. Core findings with exact numbers

Status uses the claims.jsonl label.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Without training, people are reminded of a prior case but do not use its principle | N=16. 15/16 wrote a compromise. 3/16 used the tradeoff principle. 10/16 said they were reminded of a prior case | Loewenstein, Thompson, Gentner 1999 Exp 1A (a12) | [S], opened |
| Intensive comparison training raises use of the trained principle, and only that principle | N=32 (16 per cell). Tradeoff 38% vs 19% baseline. Contingency contract 69% vs 6% and 0%. Overall 50% vs 19% | Same, Exp 1B (a13) | [S] (K02) |
| A light prompt to compare two cases beats reading them in turn | Contingency contract 13/27 compare dyads (48%) vs 5/31 (16%), p < .01. Schema quality above 1.0: 63% vs 19% of dyads, chi-square N=45, p < .005. Abstract label added nothing (30% vs 32%) | Same, Exp 2 (a14; critique correction 4) | [S] (K02) |
| Spontaneous use of a solved analog is low, hinted use is high | About 41% spontaneous after the fortress story, about 85% after a hint (second-hand quote) | Gick and Holyoak 1980/83 via Loewenstein 1999 (a10) | [C] (K01), originals unopened |
| Story recall is driven by surface similarity | Surface-matched probes 55% vs relational-only 12% (second-hand quote) | Gentner et al. 1993 (a11) | [C] (K01), original unopened |
| Large new test: surface wins when both match types exist | Exp 1, N=133, 502 memories. Close analogs 0.47 vs distant 0.09 per participant, t(132)=14.45, d=0.84. 85.66% of recalls had surface overlap | Raynal et al. 2026 (d01) | [C] against a universal claim |
| But pure structure beats pure surface when the cue is a familiar relational category | Exp 2, N=81. Distant analogs 0.46 vs surface-only 0.04, t(80)=12.06, d=0.82. 83.60% of 311 recalls had no surface overlap | Raynal et al. 2026 (d01) | [S] |
| Fortress-to-Radiation re-run did not reproduce 41% / 85% | N=128, one story. 5% (3/64) spontaneous, 36% (23/64) after hint. Story without spatial cues 6% and 20% | Barcelona team 2026 (d02) | [S]; not a failed replication, design differs |
| Inventing an analogous situation first raises spontaneous success | 63% (25/40) vs 43% (17/40), chi2(1)=3.23, p=.072. Totals 75% vs 60% | Same, Study 3 (d02) | [S] (K27); p above .05 |
| Poor comprehension of the source story kills transfer | 0% vs 31% solved, chi2(1)=6.93 | Same (d02) | [S] |

### 3.2 LLM agents: does retrieval help, and how

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Task-similarity retrieval beats no memory and random (ALFWorld, gpt-3.5) | ReAct 40.0; random 42.5; reasoning-step similarity 48.5; task similarity (ExpeL) 59.0. Mean of 4 folds | ExpeL Table 3 (a17, b01); checker confirmed | [E] (K03, K04) |
| ExpeL on other tasks | HotpotQA 28.0 to 39.0. FEVER: Act 58, ReAct 63, ExpeL transfer 65, with task demos 70 | ExpeL (a16, a18) | [E], own-group |
| Insights and raw retrieval are complementary | Insights-only vs retrieval-only: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38 | ExpeL (b02) | [S] |
| Insights need real experience | Insights extracted only from the seed few-shot examples gave no gain over ReAct | ExpeL (b03) | [S] |
| Memento: few cases are best | DeepResearcher avg F1/PM: K=0 59.9/72.2; K=1 63.6/77.9; K=2 63.7/78.1; K=4 64.5/78.5 (best); K=8 64.1/78.2; K=32 63.9/78.1 | Memento (c02, b07) | [E] (K08); K tuned on test data |
| Memento CBR vs no CBR | HLE 26.7/24.4 vs 22.2/17.4. SimpleQA 84.7/95.0 vs 81.0/89.7. DeepResearcher 66.6/80.4 vs 59.9/72.2 | Memento (b07) | [S]; authors flag contamination |
| Memento headline | GAIA validation 87.88% Pass@3 (GPT-4.1 planner, o3 executor); test 79.40% with the validation-built bank | Memento (c01, b09) | [E] as reported; not single-shot |
| Learned retrieval beats similarity only slightly | Iter 1 to 5 PM: no CBR 78.65 to 84.47; similarity 79.84 to 84.85; Q-learned 80.46 to 85.44. Margin over no CBR +1.2 shrinking to +0.4 | Memento (c03, b08) | [E] (K11) |
| Bandit retrieval | CASCADE 66.68 vs 63.76 plain similarity on Qwen3-32B; +20.9% macro over zero-shot across 16 tasks | CASCADE 2026 (c04) | [E] with Memento (K11); own-group |
| Memory vs weight updates | Beat REINFORCE+LoRA on 9/12 tasks at k=1, 12/12 at k=4. Fails when the base model never succeeds (MIMIC-IV, Qwen3-4B) | CASCADE (c05) | [S] (K21) |
| Self-generated trajectories | gpt-4o-mini, 5 seeds: ALFWorld 73 to 89; Wordcraft 55 to 64; InterCode-SQL 75 to 79; curated ALFWorld 93 vs AutoManual 79. Most of the gain in the first 25% of added tasks | Sarukkai 2025 (b21, c16) | [E] on direction |
| Utility curation | ALFWorld fixed DB 0.72; bootstrap about 0.91 at 3500 tasks; curated up to 0.93 | Sarukkai (b22) | [E] (K06) |
| Voyager skill library | 63 items in 160 iterations, 3.3x best baseline. Skill retrieval top-1 80.2 (SD 3.0), top-5 96.5 (SD 0.3), 309 samples. Random curriculum -93% | Voyager (a21, b25) | [E]; Minecraft; verified code |
| Synapse | MiniWoB++ mean success 99.2%, 64 tasks. Exemplar mismatch cost 2% on click-tab-2-hard | Synapse (a20) | [S]; templated |
| DS-Agent | Dev: GPT-4 100% over 12 tasks. Deploy (18 tasks, 10 runs): 99.44% one-pass GPT-4, 85% GPT-3.5, +25 over zero-shot Mixtral. Cost $1.60 dev, $0.13 deploy | DS-Agent (c08) | [S]; own benchmark |
| Revision from feedback | Average best rank: full 2.08; without ReviseRank 2.58; without CBR 3.41 (lower is better; 5 repeats) | DS-Agent (c09, d15) | [S] (K15); bundle ablation |
| Driving cases | Similarity beat random for every model. Random 1-shot often below zero-shot. DeepSeek-R1 14B worse with more examples. Llama3.3-70B micro-accuracy 0.937 / 0.941 | Gan et al. 2025 (a24) | [E] on direction (K03) |
| KATE | IMDB GPT-3: random 87.95 +- 2.74; KATE 91.99; tuned on SST-2 93.43. +41.9% ToTTo, +45.5% Natural Questions over random | Liu 2022 (b18) | [E]; 2021 model |
| Legal CBR-RAG | Cosine 0.8967 no-RAG vs 0.9141 hybrid AnglEBERT k=3 (+1.94%). 32 test questions | Wiratunga 2024 (a15, b26) | [S]; weak |
| Case capture on MMLU | Llama-3.1-8B history 76.9 to 82.1; math 58.0 to 60.9 (single round), 63.9 (double). gpt-3.5 math 66.9 to 64.3. Double round lower in 6 trials | Yin and Leake 2026 (b27) | [S]; workshop paper |

### 3.3 Retain, noise, harm

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Add-all hurts, strict addition helps (fixed / add-all / strict) | RegAgent 67.53 / 55.48 / 70.95. EHRAgent 16.75 / 13.05 / 38.50. AgentDriver 40.11 / 32.32 / 51.00. CIC-IoT 71.50 / 59.90 / 85.40. Add-all memory grew to 4,100 / 2,411 / 2,125 / 1,050 records | Xiong 2025 (a22) | [E] (K05) |
| Agents copy the nearest case | Pearson r near 1 between input similarity and output similarity | Xiong (b10, c13) | [E] |
| History-based deletion beats keeping all, if the judge is reliable | Delete a record retrieved 3 or 5 times with poor downstream score. CIC-IoT 85.4 vs 89.6 for one method. Coarse judge: degraded | Xiong (a23, b12) | [E] (K06); table scrambled in extraction |
| Failures stored raw erase the retrieval gain | Gemini 2.5 Flash ALFWorld: ExpRAG 0.59 success-only to 0.25 with failures; ExpRecent 0.37 to 0.22; ReMem 0.66 to 0.57; no-memory baseline 0.12 | Evo-Memory (d13) | [E] (K05) |
| Failures help only in a usable format | WebArena-Shopping: Synapse 40.6 to 41.7; AWM degraded; ReasoningBank 46.5 to 49.7 | ReasoningBank (b14) | [E] (K10) |
| Judge-noise tolerance | Judge 72.7% accurate; simulated 50-100% gave success about 47 to 49.7 | ReasoningBank (b15) | [C] (K07) vs Xiong |
| Memory injection | Injection success 98.2%, attack success 76.8%. Benign utility drop under 2% on three sets, -10.0% on MMLU | MINJA (d06) | [S]; adversarial |
| Poison needs few entries | About 80% attack success with under 0.1% poisoned; under 1% benign drop | AgentPoison (d07) | [S]; adversarial |
| Similar but unhelpful context hurts | GSM-IC: one distractor leaves under 30% of base problems consistently solved. RAG: high-score no-answer passages cut accuracy up to 0.38 (-67%); random passages added to the retrieved set raised Llama2 by up to 0.07 (+35%) | Shi 2023; Cuconasu 2024 (d08, d09) | [E] (K24); older models |
| Memory can lower hard-constraint score | TravelPlanner GPT-4o hard-constraint 12.88 no memory; 6.72 random; 8.95 key=query; 8.25 key=AveFact. Commonsense 71.93 to 79.94 | Memp (b04) | [S] (K16) |

### 3.4 Keys, units, K, gates

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Keys that say what a case does beat keys that say how it looks | Spider: Skill-KNN 78.3 vs 74.6 best raw key; oracle 78.6. Best non-oracle on 5 datasets, 6 models | Skill-KNN (d10) | [E] (K23, K04); semantic parsing |
| Keys ranked by measured usefulness beat similarity | BREAK: EPR 31.9 vs BM25 26.0, CBR baseline 25.7, SBERT 21.6, random 1.7. One-shot 23.0 vs 15.2. MTOP 64.2 vs 52.9. SMCalFlow 54.3 vs 46.1 | EPR (d16) | [E] (K23) |
| Verified subgoal library: small gain | miniF2F-valid, 50 attempts: 50.4% with vs 47.1% without. Only 24% of 135 solved problems used a skill (51% copied, 49% imitated). Best run 57.0% valid, 50.0% test | LEGO-Prover (d03) | [E] (K22); compute not matched |
| Helper functions beat whole retrieved programs | CodeLlama-13B LOGO 45.6 to 57.1. GPT-3.5 MATH +11.8. TextCraft 22.2 to 30.8. Ablations LOGO/Date/TextCraft: full 55.0/77.0/34.12; no retry 48.3/51.9/30.43; no curriculum 36.3/56.6/28.78; no prune 52.0/65.5/25.26; no edit 53.3/69.6/27.35. Lemur-70B on math: equal within SE | ReGAL (d04) | [E] (K22) |
| Distilled units over raw: own-group wins | WebArena: AWM 35.5 vs 23.5. ReasoningBank (flash) none 40.5 / Synapse 42.1 / AWM 44.1 / RB 48.8 / +MaTTS 51.8. Memp ALFWorld GPT-4o: none 42.14 / script 56.43 / trajectory 74.29 / both 77.86 | AWM; ReasoningBank; Memp (a19, b13, b05) | [C] (K09) |
| Distilled units over raw: independent runs disagree | ReasoningBank's run of AWM: +3.6 (flash), +0.9 (pro), -0.9 (Claude). Evo-Memory (flash, 4 embodied sets) success/progress: baseline 0.27/0.46; History 0.30/0.53; AWM 0.30/0.53; ExpRecent 0.39/0.59; ExpRAG 0.46/0.63; ReMem 0.50/0.64 | ReasoningBank (b16); Evo-Memory (d12) | [C] (K09) |
| Raw retrieval can fall below no memory | Columns BL / DC- (no memory) / DR (raw retrieval) / DC-Cu / DC-RS. GPT-4o AIME 2024: 20.0 / 36.7 / 26.7 / 36.7 / 40.0. GPT-4o MMLU-Pro Eng: 53.2 / 51.6 / 48.8 / 44.0 / 51.2. Full history on AIME 2024: 6.7 vs 20.0 | Dynamic Cheatsheet (d17, b24) | [C] (K09) |
| Gain tracks task sameness | Pearson r = 0.717 (Gemini 2.5 Flash), 0.563 (Claude 3.7 Sonnet). Big on PDDL, ALFWorld; small on AIME-25, GPQA. BabyAI success 0.52-0.56 vs 0.61 baseline | Evo-Memory (c19, d14, d12) | [E] (K12) |
| Largest gains sit on one-algorithm tasks | Game of 24: GPT-4o 10 to 99 (stored Python solver); GPT-4 3.0 to 82.4 with BoT while PAL alone 64.0. Checkmate-in-One 36.4 to 86.4 | DC; BoT (d17, d18) | [E] (K28) |
| Filtered examples change the K curve | MATH500, Gemini 1.5 Pro: human solutions peak near 125 then fall; correct-filtered model solutions plateau near 25 at about +5 and do not fall | Many-shot ICL (d11) | [S] (K26) |
| A retrieval gate can beat always-retrieve (large models) | PopQA: retrieval hurt 10% of questions, fixed 17%. GPT-3 adaptive 46.5%, +5.3 over any non-adaptive. Models under 10B gain little | Mallen 2023 (d05) | [S] (K25) |
| Self-recalled analogs | GSM8K GPT-3.5: 0-shot CoT 75.8; 5-shot 76.7; self-generated 77.8. MATH 34.9 to 37.3. Codeforces GPT-4 16 vs 16 | Yasunaga 2024 (a28, b20) | [S] (K14) |
| Do weak models benefit? | Self-recall fails weak models. DS-Agent GPT-3.5 one-shot no better than zero-shot. DeepSeek-R1 14B worse with examples. Evo-Memory says small models gain most | a28, c09, a24, c19 | [C] (K13) |
| Models act case-based inside their weights | Leave-Square-Out: random split near 100%, held-out block collapses. RFFT trained on 1-5 digits reaches 12 digits above 95% | Hu et al. 2024 (a29) | [S] (K20); not external CBR |

### 3.5 Caution on all LLM numbers
Almost every LLM-CBR result comes from the method's authors (critique). Independent re-runs exist only for AWM and Synapse. Many test sets are tiny: 32 legal questions, 30 questions per AIME set (one question = 3.3 points). ReasoningBank has one run per cell and no intervals. The Memento K sweep was tuned on test data. Treat these as direction, not size (K17).

## 4. Mechanisms and models

Each model is described so it can be coded.

### 4.1 Case record
A case = (problem description, solution, outcome, index keys, provenance). Memento stores (state, action, reward) (c01). Our version for S9: subgoal text, plan or code, verified result, the check that passed, key description, failing-output note, retrieval-outcome counter.

### 4.2 The Retrieve-Reuse-Revise-Retain loop
1. Index: build the key for the new subgoal (4.3).
2. Retrieve: top-K by key similarity, K small (1 to 4).
3. Reuse: place the case in the prompt marked "reference, may not apply". Force an explicit adapt-and-run step. People get reminded and still fail to apply the case (a12).
4. Revise: run it. If the check fails, revise from the real failing output only (G2). DS-Agent does this with execution feedback (c09).
5. Retain: admit only if a check on something the answer was not fitted to passes (G3). Add an outcome counter.
6. On failure, explain and add an index. This is the old CHEF/Slade rule that a failure should change how the case is keyed (a02, a03).

### 4.3 Key construction (options tested in the literature)
- Raw problem-text embedding. Weakest, surface-biased (d10).
- LLM-written description of what the case does, without surface words (Skill-KNN). Beat raw by 3.7 points on Spider (d10). Voyager and AWM also embed descriptions (a21, a19).
- Usefulness-trained rank (EPR). Train a retriever on whether including the case raised the model's probability of the right output. +5.9 over BM25 on BREAK (d16). Needs thousands of labelled pairs. A cheap online version ranks by observed verified success when retrieved (Sarukkai, b22).
- ExpeL: the task statement beats the current reasoning step as a key (59.0 vs 48.5) (a17).
- Humans: a cue that carries a familiar relation label retrieves distant analogs (d01).

### 4.4 Utility curation (Sarukkai)
Score of a case = outcomes of tasks where it was retrieved, weighted by retrieval frequency. Keep the best, drop the worst. Best beat worst at every database size on ALFWorld and Wordcraft, and only at small sizes on SQL (c17). Needs many tasks for stable estimates (b22).

### 4.5 History-based deletion (Xiong)
Remove a record retrieved at least 3 or 5 times whose average downstream score is poor. Thresholds are set per agent. Works with a strict judge, hurts with a coarse one (a23, c14).

### 4.6 Bandit retrieval (CASCADE, Memento)
Treat retrieval as a contextual bandit with binary reward. Explore cases of uncertain value, exploit proven ones. Memento uses a Q-function over case embeddings. Gain over plain similarity: about 3 points (CASCADE), 0.4 to 1.0 late (Memento) (c03, c04). Not worth building before a plain library works (K11).

### 4.7 Distillation (AWM, ReasoningBank, Memp, BoT)
Induce a description-plus-steps unit from solved runs. Online induction uses the model's own runs and an automatic judge, so wrong workflows can be made (b17). ReasoningBank also writes strategy items from failures (b14). Evidence is contested (K09).

### 4.8 Gate on lookup
Mallen's gate skips retrieval where the model likely knows the answer, using popularity (d05). Subgoals have no popularity. Candidate signals: similarity of the nearest case below a threshold, or a cheap self-solve attempt that already passes its check. Untested (K25).

### 4.9 Experience-following and its controls
Output similarity tracks input similarity (b10). Controls: verified admission, small K, "may not apply" label, per-case outcome counter, relevance check on near misses (K24).

## 5. What holds up

### 5.1 Replications and failed replications
- Retrieval gap in humans: survives in part. Raynal et al. 2026 (N=133, N=81) reproduce surface dominance when both match types exist (0.47 vs 0.09). Pure structure beats pure surface (0.46 vs 0.04) when the cue is a familiar relational category. So "people retrieve by surface only" is not universal (d01, K01 contested).
- Fortress-to-Radiation: a 2026 re-run (N=128) found 5% spontaneous and 36% hinted, not 41% and 85%. The design differs (one story, written summary, translation, different scoring), so it is not a failed replication. No Many-Labs-scale replication was found (d02, K27).
- Loewenstein et al. 1999 compare effect: small N (27 + 31 dyads; 16 per cell), one lab. No independent replication in our sources.
- AWM +12: ReasoningBank's independent run gave +3.6, +0.9, -0.9. Evo-Memory's port put AWM at History level (0.30/0.53), below raw ExpRAG (0.46/0.63). Caveat: Evo-Memory ported AWM itself (b16, d12).
- ExpeL's text says reasoning-similarity retrieval "slightly drops". The table gap is 10.5 points (critique correction 6).
- Memento's CBR margin shrinks across rounds, and the no-CBR arm itself gains 5.8 points (b08).

### 5.2 Meta-analyses
None for CBR in LLM agents. The one review (Hatalis 2025, b29, c07) has no new measurements and says benchmarks are missing. No human meta-analysis was found.

### 5.3 Moderators and boundary conditions
- Task sameness. Gain correlates with within-dataset similarity (r=0.717, 0.563). Large on ALFWorld, PDDL, Game of 24, MiniWoB++. Small on AIME-25, GPQA. Negative on BabyAI (d14, d12). AWM and ReasoningBank gains vanish on cross-website subsets (K12).
- Model strength. Self-recalled analogs and one-shot cases fail for weak models (a28, c09). CASCADE fails when the base model never succeeds (c05). Evo-Memory reports the opposite (small models gain most). Contested (K13). Mallen: the gate helps only above about 10B parameters (d05).
- Judge reliability. A strict judge makes deletion and addition work. A coarse judge hurts (Xiong). ReasoningBank says 50-100% accurate judges give similar results. Contested (K07).
- Cue wording. A familiar relation label in the cue unlocks structural retrieval in humans (d01).
- Comprehension. If the source story was not understood, transfer is 0% vs 31% (d02).
- Verification. Verified code or formal proof makes library entries safe (Voyager, LEGO-Prover). Where entries are unverified text, errors propagate (a21, d03, a22).

### 5.4 Interventions that worked
- Strict, verified admission (a22; K05, K06).
- Similarity or description keys over random (a17, d10, d16).
- Small K (c02) and filtered examples (d11).
- Utility-based curation (b22, c17).
- Comparing two cases, in humans (a13, a14).
- Generating your own analog before the hint (d02).
- Helper-function libraries with a retry loop and curriculum (d04).
- Storing failures as lessons (b14).

### 5.5 Interventions that did not work, or hurt
- Add-all memory (a22). Appending full history (b24; AIME 2024 GPT-4o 6.7 vs 20.0).
- Random cases, which sometimes fall below no memory (Memp 6.72 vs 12.88; Gan; Dynamic Cheatsheet) (K03).
- Raw failure traces (d13: 0.59 to 0.25).
- An abstract label alone (a14). A second feedback round in case capture (b27).
- Reflections inside insight extraction (a17). Insights extracted from seed examples only (b03).
- Pruning and editing the library mattered less than retry and curriculum in ReGAL (d04).
- Many cases, as in many-shot prompting. CBR does not benefit from more cases (c02).

## 6. Language models

How they behave.
- They copy the nearest case, right or wrong (experience-following, r near 1) (b10).
- A similar-looking wrong case acts like a distractor. GSM-IC and the RAG study show near misses hurt more than random text (d08, d09).
- Raw retrieval can be worse than none on some models and tasks (Dynamic Cheatsheet GPT-4o AIME 26.7 vs 36.7; MMLU-Pro Eng 48.8 vs 51.6; BabyAI) (d17, d12).
- Their internal behaviour on rule tasks is case-like: interpolation, not rule use (a29). For rule-governed subgoals, give the rule and a code step.
- Asking a model to recall its own analogs adds about 1 to 2.4 points for strong models (GSM8K 75.8 to 77.8; MATH 34.9 to 37.3), nothing for GPT-4 on Codeforces (16 vs 16), and fails for weak ones (a28, b20).
- Reasoning models may be hurt by examples (DeepSeek-R1 14B was worse with more examples) (a24).

What changed the results, and by how much.
- Similar vs random: +16.5 on ALFWorld (59.0 vs 42.5) (a17).
- Similar vs none, on templated tasks: ExpeL +19.0; Sarukkai +16 (73 to 89, equal to a model upgrade); Memp GPT-4o 42.14 to 77.86; Evo-Memory ExpRAG 0.12 to 0.59 (a17, b21, b05, d13).
- Gain on non-templated reasoning is small: Memento CBR +4.5 to +6.7 F1 on hard QA, shrinking to +0.4 to 1.0 late in training; Yin and Leake MMLU up to +5.2 for some models and negative for others; CBR-RAG +1.94% on a saturated metric (c03, b27, a15).
- Strict vs add-all admission: RegAgent +15.5, EHRAgent +25.5, AgentDriver +18.7, CIC-IoT +25.5 (a22).
- Description key vs raw key: +3.7 (d10). Usefulness rank vs BM25: +5.9 (d16).
- Verified library vs none, proofs: +3.3 (d03). Helper functions vs retrieved programs: +11.5 on LOGO (d04).
- Bandit retrieval vs similarity: about +3 (c04); Memento late +0.4 to +1.0 (c03).
- Revision from feedback: rank 2.58 to 2.08 (c09).
- Memory vs LoRA: wins 9/12, then 12/12 at k=4 (c05).

Not measured anywhere: any of the above at equal total tokens on a reasoning benchmark with a subgoal-level library. The closest tests (LEGO-Prover, ReGAL) do not match compute (K22).

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = the S9 record and library.

### Add now (established)

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Admit a library entry only after a check on something the answer was not fitted to (code run, answer check, formal proof). Never on model self-judgement alone | G2, G3, memory | [E] | a22, b11, c14, d03, a21, K05, K06 |
| A2 | Retrieve by similarity, never random. Random can fall below no memory | memory | [E] | a17, b04, a24, K03 |
| A3 | Make the retrieval key describe what the case does, not how it looks: an LLM-written description plus the goal, raw text as fallback. Direction is proven on semantic parsing, not subgoals; the size of our gain goes to U1 | memory | [E] on direction | a17, d10, d16, K04, K23 |
| A4 | Keep retrieved K small: default 2 to 4, chosen on a dev split | memory, G11 | [E] | c02, b06, K08 |
| A5 | Mark retrieved cases "reference, may not apply" and require an adapt-and-check step. Do not trust a case because it is similar | G2, G10 | [E] | b10, d08, d09, a12, K24 |
| A6 | Store failures as short lessons tied to the failing output, not as raw traces to imitate | G2, memory | [E] | b14, d13, K10 |
| A7 | Keep an outcome counter per case. Drop cases that score poorly over repeated retrievals (needs a reliable check) | memory | [E] | b22, c17, a23, K06 |
| A8 | Expect gains mainly where tasks share structure. Report templated and new-structure items separately | G7, G12 | [E] | d14, d12, d17, d18, K12, K28 |
| A9 | Do not append full history or add every run | memory | [E] | a22, b24, K05 |
| A10 | Track hard-check scores separately from soft scores. Memory raised one and lowered the other | G3, G7 | [S], cheap | b04, K16 |

### Test first (not established; each is a row in UNKNOWNS.md)

| # | Item | Part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Subgoal-level library (solved subgoals, not whole tasks) vs no library vs whole-task library at equal tokens | memory, O3, S9 | [S] | d03, d04, K22 |
| T2 | Restate the subgoal in library vocabulary (generate an analog) before lookup | O7 | [S] | d02, d01, K27 |
| T3 | Compare two stored cases and store the shared structure as the key | O7, memory | [S] | a13, a14, K02 |
| T4 | Similarity-threshold gate on lookup | G12 | [S] | d05, d12, K25 |
| T5 | Distilled strategy vs raw trace vs both | memory, O3 | [C] | K09 |
| T6 | Revise from failing output vs copy | S5, G2 | [S] | c09, d15, K15 |
| T7 | Key by goal plus failure signature | memory | [S] | a08, a03, K18 |
| T8 | Dose-response of wrong cases, and whether code admission removes it | G2, G10 | [C] | K07 |
| T9 | Self-recall of analogs vs stored cases | O7 | [S] | a28, K14 |
| T10 | Adaptation-guided retrieval | memory | open | c26 |

## 8. Concrete tests on our bench

All arms get the same total tokens, with library-build and setup cost counted (G7). Use at least 5 seeds and paired tests (K17). Choose K and thresholds on a dev split, not the test split.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Subgoal library | Math word problems, ARC-like grids, short code tasks with checkers | A no library; B random verified subgoals; C similarity subgoals; D whole-task retrieval | Pass rate on held-out items; hard-check rate | C beats A by 2 to 4 points (LEGO-Prover +3.3); B near or below A; C at least D |
| B2 Key type | Same | Raw-text key; LLM-written "what it does" key; success-weighted rank | Pass rate; top-1 retrieval relevance | Description key +2 to 4 (Skill-KNN +3.7); rank adds a little |
| B3 Admission gate | Same, library seeded with known-wrong entries at 0, 10, 30, 50% | Code-verified admission vs model-judged admission vs add-all | Accuracy loss vs the 0% library; copy rate of wrong entries | Verified admission stays flat; the other two lose several points, growing with share |
| B4 Distilled vs raw | Templated items and cross-domain items scored separately | Raw traces; one-line strategies; both | Pass rate per item type | Distilled helps cross-domain and raw helps templated, or a null (Evo-Memory) |
| B5 K sweep | Dev split | k = 1, 2, 4, 8 at fixed total tokens | Pass rate | Peak at 2 to 4; flat or decline beyond |
| B6 Lookup gate | Items binned by similarity to the nearest case | Always retrieve; skip if similarity below t; skip if a self-solve passes | Pass rate per bin; tokens | Gate saves tokens and avoids harm in the low-similarity bin |
| B7 Analog restatement | Same | Raw-text cue; restate in library vocabulary then cue | Lookup hit rate; pass rate | Hit rate up (humans 43% to 63% spontaneous) |
| B8 Compare two | Library with pairs of related cases | Single-case entries; merged shared-structure entries | Pass rate on new items of the same principle | Gain on principle-matched items (humans 48% vs 16%) |
| B9 Revise vs copy | Items where the retrieved case fails its check | Copy; revise from real failing output; both with a retry cap | Pass rate at equal tokens | Revise beats copy (rank 2.08 vs 2.58) |
| B10 Structure split | Held-out structurally new items and post-cutoff items | Library vs none | Gain by split | Gain shrinks on new structure (r of 0.56 to 0.72 with task sameness) |
| B11 Model size | One small and one strong model | Library vs none | Gain per model | Contested; report both |

## 9. What does not transfer, and why

- Human reminding studies. They measure unaided recall by students. Our retrieval is code. The finding that people fail to retrieve supports putting retrieval in code. It says nothing about embedding recall quality (a10, a11, d01).
- The very large gains on Game of 24, ALFWorld, MiniWoB++, PDDL and Checkmate-in-One. The task is templated or has one reusable algorithm. PAL alone gets 64.0 of the 82.4 on Game of 24 (d17, d18, K28).
- Voyager and Synapse. The entries are verified executable code or fixed templates. Most reasoning subgoals cannot be executed that way (a21, a20).
- AWM and ReasoningBank web numbers. Web navigation with self-judged success. Judge errors are not isolated (a27).
- DS-Agent. Cases are expert Kaggle write-ups with a code runner (c08).
- Memento GAIA. Pass@3 on validation with a bank built on that validation, plus heavy tool use (b09).
- Learned or bandit retrieval. Needs many tasks to learn and gains about 3 points or less (K11). Fails G7 until the plain library works.
- "Case-based" in Hu et al. 2024 means interpolation in weights, not an external store (a29).
- Mallen's gate uses Wikipedia page views, an external popularity signal that subgoals do not have (d05).
- Compaq SMART. A vendor report on a call-centre process (a09).
- CASCADE vs LoRA. Our agent does not train (c05).
- Early CBR systems (CHEF, MEDIATOR). Hand-built repair rules in narrow domains (a03, a04).

## 10. Open questions

1. Does a library of solved subgoals (not tasks) retrieved by similarity beat no library at equal tokens on math, ARC-like and code? No paper tests it (critique gap 1).
2. Which key works for subgoals: problem text, plan, or relation description? (gap 2)
3. How large is the harm from 10, 30 and 50 percent wrong cases, and does code-verified admission remove it? (gap 3)
4. Do distilled strategies beat raw solved cases when run by third parties? (gap 4)
5. What is the best K at equal total tokens, and does it move with model size? (gap 5)
6. Does a similarity-threshold gate beat always-retrieve? (gap 6)
7. Do the Gick and Holyoak, Gentner 1993 and Ross 1984 originals replicate at modern sample sizes? They are unopened (gap 7).
8. Does adaptation-guided retrieval beat nearest neighbour for LLM agents? (gap 8)
9. Does revision from real failing output beat copying, outside DS-Agent? (gap 9)
10. Do memory gains survive removing contamination and templated tasks? (gap 10)
11. Do weak models gain or lose from a case library? Sources disagree (K13).
12. How does a library interact with long-chain reasoning models, where examples may hurt (a24)?

## 11. Sources

[V] = opened and read this session (by the research agents or the checker). [M] = snippet or memory only.

Founding and review
- [V] Slade (1991) Case-Based Reasoning: A Research Paradigm. https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/883
- [V] Kolodner (1991) Improving Human Decision Making through Case-Based Decision Aiding. https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/895
- [V] Nguyen, Czerwinski, Lee (1993) COMPAQ QuickSource. https://www.aaai.org/Papers/IAAI/1993/IAAI93-012.pdf
- [M] Aamodt and Plaza (1994) Foundational issues. https://doi.org/10.3233/AIC-1994-7104
- [M] Hammond (1986) CHEF. https://aaai.org/papers/00267-AAAI86-044/
- [M] Smyth and Keane (1998) Adaptation-guided retrieval. https://doi.org/10.1016/S0004-3702(98)00059-X
- [V] Hatalis et al. (2025) Review of CBR for LLM Agents. https://arxiv.org/abs/2504.06943

Human studies
- [V] Loewenstein, Thompson, Gentner (1999). https://groups.psych.northwestern.edu/gentner/papers/LoewensteinThompsonGentner99.pdf
- [M] Gick and Holyoak (1980) Analogical problem solving. https://doi.org/10.1016/0010-0285(80)90013-4 (the 1983 paper is also unopened; figures come via Loewenstein 1999)
- [M] Gentner, Rattermann, Forbus (1993), quoted via Loewenstein 1999.
- [M] Ross (1984) Remindings. https://doi.org/10.1016/0010-0285(84)90017-3
- [V] Raynal, Clement, Gros, Sander (2026) Bridging the retrieval gap, Memory & Cognition 54. https://pmc.ncbi.nlm.nih.gov/articles/PMC13719747/
- [V] Barcelona team (2026) Spatial structures and analogical problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC13253581/

LLM agents and CBR systems
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Zheng et al. (2024) Synapse. https://arxiv.org/abs/2306.07863
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Gan, Dao, Zettsu (2025) CBR-LLM driving. https://arxiv.org/abs/2506.20531
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153
- [V] Ouyang et al. (2025/26) ReasoningBank. https://arxiv.org/abs/2509.25140
- [V] Fang et al. (2026) Memp. https://arxiv.org/abs/2508.06433
- [V] Guo et al. (2026) CASCADE. https://arxiv.org/abs/2605.06702
- [V] Guo et al. (2024) DS-Agent. https://arxiv.org/abs/2402.17453
- [V] Wei et al. (2025/26) Evo-Memory. https://arxiv.org/abs/2511.20857
- [V] Sarukkai et al. (2025) Self-generated in-context examples. https://arxiv.org/abs/2505.00234
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302
- [V] Yin and Leake (2026) Capturing LLM cases for RAG reuse. https://ceur-ws.org/Vol-4255/lake.pdf
- [V, abstract and introduction only] Tang et al. (2025) Agent KB. https://arxiv.org/abs/2507.06229
- [V, abstract and introduction only] Zeng et al. (2024) Structural memory of LLM agents. https://arxiv.org/abs/2412.15266
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714
- [V] Hu et al. (2024) Case-based or rule-based. https://arxiv.org/abs/2402.17709

Subgoal, key, gate and harm studies
- [V] Wang et al. (2023) LEGO-Prover. https://arxiv.org/abs/2310.00656
- [V] Stengel-Eskin, Prasad, Bansal (2024) ReGAL. https://arxiv.org/abs/2401.16467
- [V] An et al. (2023) Skill-KNN. https://arxiv.org/abs/2305.14210
- [V] Rubin, Herzig, Berant (2022) EPR. https://arxiv.org/abs/2112.08633
- [V] Liu et al. (2022) KATE. https://arxiv.org/abs/2101.06804
- [V] Agarwal et al. (2024) Many-shot ICL. https://arxiv.org/abs/2404.11018
- [V] Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511
- [V] Shi et al. (2023) Easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093
- [V] Cuconasu et al. (2024) The power of noise. https://arxiv.org/abs/2401.14887
- [V] Dong et al. (2025) MINJA. https://arxiv.org/abs/2503.03704
- [V] Chen et al. (2024) AgentPoison. https://arxiv.org/abs/2407.12784

Checker corrections applied (critique.md): Memento first author is Zhou; K=1 is 63.6/77.9 and K=2 is 63.7/78.1; Gick and Holyoak is 41% to 85% (not 10% to 85%); the chi-square p < .005 belongs to schema quality; ExpeL ReAct+Reflexion is 40.3 to 54.4 and retrieve-only is 54.5 to 60.4.
