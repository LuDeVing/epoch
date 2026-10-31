# Case-based reasoning in law: deep document

*Subfield E11.05. Built from evidence_a-d.jsonl, claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids (a01, b05, c07, d03 ...) point to those files. Status marks: [E] established, [S] single-source, [C] contested. Important limits: no human-psychology study of lawyers or judges was opened (section 10), and the original HYPO/CATO/IBP/Aleven evaluations were never opened (K20).*

## 1. What it is

Case-based reasoning (CBR) solves a new problem by using solutions to old ones. The generic cycle is: retrieve similar cases, reuse their solution, revise it to fit, retain the result. Law is the field where this idea is oldest and most formal. Under stare decisis, similar cases should be decided similarly (a01). The doctrine does not say how to measure "similar". Similarity depends on viewpoint and on the outcome the arguer wants (a01).

Legal CBR is not nearest-neighbour retrieval. Bench-Capon (1997) separates the two. Retrieval finds the closest case and copies its outcome. Legal CBR argues about which similarities and differences matter (a06). It sits close to "rules plus judgement": precedents act as priority rules between sets of facts, so cases and rules are not opposed (b19).

Five features make law a good CBR domain (a01): open-textured concepts, varied tasks (advocacy, adjudication, advising), varied knowledge (cases and statutes), rich linked case repositories, and use of hypotheticals.

Why it matters for our agent. Our schema has one analogy operator (O7, map an analogue) and a memory (lessons, class record, subgoal library). Legal CBR is the most developed theory of how to use an old case for a new one: what to compare, which moves to make, how to say a difference does not matter. It also supplies measured LLM results on exactly that skill (section 6).

## 2. History and theories in depth

**Pre-AI roots.** Levi (1949) described law as moving case to case by example, with the rule made by how earlier cases are compared (a24, snippet only).

**HYPO (Rissland and Ashley, 1984-87; Ashley 1990).** The first legal CBR system on real precedents, in US trade secret law (a02, a11). It analyses a new case, retrieves cases, sorts them by "on-pointness" in a claim lattice, picks best cases for each side, and generates three-ply arguments: the proponent cites a case, the opponent responds with a counterexample or distinction, the proponent rebuts. Its key idea is the dimension: a fact pattern that moves a claim stronger or weaker, for example Secrets-Voluntarily-Disclosed (more disclosures weaken a misappropriation claim) (a02). HYPO also builds hypotheticals by altering facts (a01).

**CABARET and GREBE (Rissland and Skalak 1991; Branting).** CABARET interleaves case-based and rule-based reasoning on an agenda in home-office tax deduction law. When all but one rule condition is met (a near miss), cases are used to argue that the condition holds. GREBE was graded blind by a domain expert against law students and "compared favourably", with no scores given in the survey (a04).

**CATO (Aleven and Ashley, 1990s).** Added a factor hierarchy: abstract legal reasons above 26 base factors, so the system can explain why a shared factor favours a side and why a distinction matters (a03, a06). CATO has 8 argument moves (C1 analogise, C2 distinguish, C3 downplay a distinction, C4 emphasise a distinction, C5/C6 cite favourable cases, C7 cite a more-on-point counterexample, C8 cite an as-on-point case) (a06). HYPO could not make two of CATO's moves because it had no hierarchy (a07). Aleven's controlled experiment reportedly found CATO-taught students matched an instructor-taught group; this is recalled from the survey and not checked in the paper (a03, a22; K20).

**IBP (Bruninghaus and Ashley 2003).** Predicts trade-secret outcomes by issue using CATO factors and explains the prediction (a23). The figure "about 91% on 186 cases" is recalled, not verified. Do not cite it.

**Formal turn (1997-2025).**
- Bench-Capon gave an algorithmic account of HYPO and CATO (algorithms DD, DR, 3-Ply) (a06, a07) and showed that Popov v Hayashi gets different arguments under factors, dimensions, theory construction and argumentation schemes (b20).
- Prakken and Sartor modelled precedents as rules that can be broadened or distinguished in a dialogue game (a09, snippet).
- Bench-Capon and Sartor (2003): cases create preferences among values; a new case should keep a theory of value preferences consistent (a10, snippet).
- Prakken, Wyner, Bench-Capon and Atkinson (2013) recast CATO reasoning as argumentation schemes. Scheme CS1: if the shared factors favouring the plaintiff are preferred over the shared defendant factors, decide for the plaintiff. Worked example: Mason v Bryce, plaintiff factors {F6, F21}, defendant factor {F1} (a08).
- Horty and Bench-Capon (2012): a precedent constrains a new case if the new case is at least as strong for the precedent's winner on the shared factors (a25, snippet). Prakken (2020) compares factor and dimension accounts (b17). Prakken and van Woerkom (2025) defend hierarchical result models against Bench-Capon's counterexamples (b18). Liu, Lorini, Rotolo and Sartor (2022) recast factor theory as a classifier logic (b16). Roth's thesis rebuilt HYPO, CABARET, CATO, IBP and GREBE in one formal model (b21).
- Argumentation pyramid (a05): facts at the base, then dimensions and factors, statutory rules, court-made tests, policies and principles. CBR moves between levels.

**What the history shows.** The symbolic systems were validated by worked examples and small expert-graded tests. Surveys and design papers report almost no accuracy (K02, [E]). The formal accounts of precedential constraint still disagree and no empirical test picks between them (K17, [C]).

**Statistical era (2018-2026).** Benchmarks arrived: CaseHOLD (a13), LegalBench (b08), COLIEE retrieval (b10, b11). Then factor-based LLM work from the Pittsburgh group (Zhang, Ashley, Gray, Grabmair, Savelka): faithfulness and abstention (b01-b03), factor discovery (b06), hierarchical distinction tasks (a16), probing (a18). Correction: file c names the first author "Li"; the authors of arXiv 2510.08710 are Li Zhang, Grabmair, Gray and Ashley. Cite as Zhang et al. (critique.md).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Legal CBR uses factors and argument moves, not raw similarity | CATO: 26 factors, 8 moves; HYPO lacked 2 of them | a02, a06, a07, a08 | [E] (K01) |
| Symbolic CBR had almost no quantitative validation | Survey gives no scores; GREBE graded blind, no numbers | a04, a01 | [E] (K02) |
| IBP ~91% on 186 cases; CATO equals instructor | recalled, not opened | a22, a23 | unverified (K20) |
| Frontier LLMs find surface distinctions when factors are given | Task 1: 100%, 6 models, 253 instances | a16, b04, c01 | [S] (K03) |
| Hierarchical support is harder | Task 2: 64.82% (gemini-2.5-flash) to 92.09% (gpt-5) | a16, b04 | [S] (K04) |
| Identifying significant distinctions collapses | Task 3: 11.46% to 33.99% (qwen3-235b-thinking), most under 25% | a16, b04, c22 | [S] (K04) |
| Thinking mode helps a lot | qwen3-235b Task 2: 78.66% thinking vs 30.04% non-thinking; Task 3: 33.99% vs 0.00% | b05, c02 | [S] (K05); confounded with RL post-training |
| More thinking is not better | gpt-5 3,189 tokens for 92.09%; qwen3-thinking 9,596 for 78.66%; gpt-5 wrong answers 4,456 tokens vs 3,081 right (+45%); mean tokens Task 1 487 to Task 3 7,025 | a17, b05, c03 | [S] (K06) |
| Within one question shorter chains win | shortest beats random by up to 18.8 and longest by up to 34.5 points (math, GPQA) | d05, d06 | [E] (K23); not legal |
| LLM arguments are faithful but incomplete | Hallucination accuracy 91.38% to 99.64% (Test 1), 90.26% to 98.15% (Test 2); factor recall 85.22% (GPT-4o) down to 42.47% (GPT-4o-mini); 30 triples | b01, b02 | [S] (K08) |
| Models rarely abstain on non-arguable cases | GPT-4o 86.67%, QwQ-32B 56.67%, Maverick 50.00%, R1-Distill 23.33%, Llama-3-70B 3.33%, three models 0.00%; N=30 | b03 | [S] (K08) |
| Case recall from memory is badly hallucinated | GPT-4 58%, GPT-3.5 69%, PaLM 2 72%, Llama 2 88%; at least 49% even on easy tasks; "do two cases agree" near chance | a15, c13 | [S] (K09) |
| Legal RAG tools still hallucinate | Lexis+ AI ~17%, Ask Practical Law AI ~17%, Westlaw AI-AR ~33%, GPT-4 closed-book ~43%; 202 queries (per-tool values read from a figure with garbled labels) | c12, d01, d02 | [E] (K10, K21) |
| Case retrieval is hard | COLIEE micro-F1: BM25 19.4/21.4, ReaKase-8B 27.0/28.7; internal MRR 0.9711 vs official 0.1414 | b10, b11 | [E] (K11) |
| Case-based RAG gain is small | cosine 0.8967 to 0.9141 (+1.94%); 2,124 QA pairs; 57% of cases cite no act | b09, c05 | [C] (K12) |
| Agent case memory helps modestly | Memento +4.7 to 9.6 points out of distribution; K=0 59.9 F1, K=1 63.6, K=4 64.5, K=8 64.1, K=32 63.9 | c07, c08 | [E] (K13) |
| Rules vs raw cases depends on task | ExpeL insights-only vs retrieval-only: HotpotQA 36 vs 31; ALFWorld 50 vs 55; WebShop 37 vs 38 | c10, d13, d14 | [C] (K14) |
| Relevance of retrieved cases is the main lever | ALFWorld 59.0 task-similar vs 42.5 random vs 40.0 none; LLM insights 39.0 vs hand-written 32.0 on HotpotQA; reflections added: 29.0 | d14, c11 | [S] (K24) |
| Self-generated analogues help strong models | GSM8K text-davinci-003: 0-shot 14, CoT 50, 5-shot fixed 54, retrieved 57, self-generated 61; curie-001 stays 2-3 | d11 | [S] (K25) |
| Best number of analogues is small | self-generated K=1 76.1 vs K=2 77.0 on GSM8K (table column as read); K=3 to 5 best | d12 | [S] (K25, K28) |
| Legal retrieval trades precision for recall | PrivacyQA P@1 14.38%, R@64 84.19%; MAUD P@1 2.65%, R@64 28.28% | d15 | [S] (K28) |
| LLM factor extraction from text is mediocre | GPT-4 F1 .53 / .52 / .51, .57 with updated guidelines; MCC canonical factors llama 0.52, gpt-4o 0.32 vs gold 0.56 | a14, b06 | [E] (K18) |
| Factors are linearly decodable in small models | Best-layer AUC 0.86 to 1.00; medians 0.961/0.972/0.961; 5 random features 0.55 vs 1 selected 0.95; train 3,932 / test 3,961 | a18, b07 | [S] (K07); not causal (K27) |
| Rule induction from analogous cases is weak | LRI-GOLD, 216 sets: micro-F1 GPT-4o 46.92, Claude-3.7 66.67; implicit-rule recall ~25-48%; LoRA on 5,121 sets lifts a 3B model 19.21 to 70.96 | b12 | [S] (K19) |
| LLM judges are persuadable | Advocate quality shifts outcome 8-21%; stronger advocate wins 58-71%; 63% to over 90% strongest vs weakest | b13, b14 | [S] (K16) |
| Larger reasoning models defer more to false context | 1,127 EU-law items; true context adds +27.0 / +29.9 points; POI 43.1% vs 78.2%; no mitigation tested | d03, d04 | [S] (K22) |
| Legal prompting helps on statute entailment | GPT-3, COLIEE 2021: zero-shot CoT 0.6296; best legal prompt +15.79% over winner; 2022 test 0.7064, +5.41% | d10 | [S] (K26) |
| Law pretraining helps on holding-selection | CaseHOLD 53,000+ items; BiLSTM F1 0.4, BERT 0.6, Legal-BERT +7.2 points; easy tasks gain 0.5-1.6 | a13, c15 | [E] |
| LegalBench: applying rules easier than recalling them | GPT-4 category means: issue 82.9, rule-recall 59.2, rule-conclusion 89.9, interpretation 75.2, rhetorical 79.4 | b08 | [E] |

## 4. Mechanisms and models

An engineer can build each of these.

**4.1 Factor representation.** A case is a set of binary factors, each tagged with the side it favours (plaintiff or defendant), plus the outcome. CATO has 26 trade-secret factors. Dimensions are graded factors with a direction (a06). Abstract factors sit above base factors in a hierarchy with positive and negative links (a07). Implementation: a dict of case id to {factors, side of each factor, outcome}. Factors are extracted from text by an LLM step (weak: F1 about .5 to .6, MCC .3 to .5; b06, a14).

**4.2 Comparing a new case to a precedent (the HYPO/CATO core).**
1. Shared factors: intersection of the two factor sets, split by side.
2. Distinctions: factors present in one case and not the other. A distinction matters if it weakens the precedent's applicability to the new case for the side that cites it.
3. Moves: analogise (shared factors favour the same side as the precedent outcome); distinguish (cite a distinction); downplay a distinction (route through the hierarchy to an abstract factor still satisfied by a substitute); emphasise a distinction; cite a counterexample that is more on point.
4. Three-ply output: proponent cites, opponent responds, proponent rebuts (a02, b01).
5. Precedential constraint (Horty): the precedent forces its outcome if the new case is at least as strong for the winner on the shared factors (a25; contested, K17).

**4.3 The three Zhang et al. tasks as a pipeline spec (a16).** T1 list distinctions (flat set difference). T2 for each distinction, say whether it emphasises or downplays, which needs the hierarchy. T3 find the significant distinctions, which means combining T1 and T2 under the hierarchy. LLMs get T1 right 100% and T3 right 11-34%. So the failure is composition, not any single step. A scaffold would run T1 in code (a set difference needs no LLM), call the model for T2 per distinction, and compute T3 in code. This is a design inference, not tested.

**4.4 Retrieval.** BM25 is a strong baseline (19.4/21.4 micro-F1 on COLIEE 2022/2023). Embeddings alone do worse (SAILER 14.0/16.6). Adding extracted facts, issues and reasoning helps (ReaKase 27.0/28.7; ablation NDCG@5 2022: neither 53.8, entities only 51.4, reasoning only 54.5, both 55.6) (b10). Hybrid embeddings with grid-tuned weights gave a small gain in CBR-RAG (b09, c25). Validate on the official split: internal MRR 0.9711 fell to 0.1414 officially (b11).

**4.5 Case memory for agents (Memento).** Store cases (state, action, reward). Retrieve the top K by similarity and put them in the planner prompt. Optionally learn a parametric Q-function to rank cases. The first retrieved case gives most of the gain; K=4 was best (c07, c08). Parametric retrieval beat non-parametric by about 0.6 points in iteration 1 (80.46 vs 79.84), with the gap to no-CBR shrinking from 1.8 to about 1.0 by iteration 5 (c09).

**4.6 Experience distillation (ExpeL).** Collect trajectories, then have an LLM write insights (rules) from success/failure pairs. At test time retrieve similar trajectories and show the insights (c10, c26). Insights from a better model are better (c26).

**4.7 Self-generated analogues.** Ask the model to recall 3 to 5 relevant problems and solve them, then solve the target (d11, d12). Works for strong models, not weak ones.

**4.8 Probing.** Linear probes on hidden layers read each of the 26 factors with AUC 0.86 to 1.00; sparse-autoencoder features carry most of it (a18, b07). This shows the information is present. Nobody has tested that the model uses it (d07).

## 5. What holds up

**Holds.**
- The theory: legal CBR is argument over relevant similarity and difference (K01, [E], three independent sources).
- Retrieval is hard and BM25 is strong; official-test gaps expose leakage (K11, [E]).
- Models hallucinate cases from memory (K09). Reading the text first cuts the rate by about a third to a half (43% to 17-33%) but leaves a floor. The residue is a real case cited for a holding it lacks (K21, [E], d01, d02). Groundedness was only graded for correct responses (d02).
- A few retrieved cases are enough, and relevance matters more than count (K13, K24).
- LLM factor extraction from raw text is mediocre; human-refined or canonical factors help. Fully automatic factor sets were the weakest (K18, b06).

**Single-source, treat with care.** Almost all strong numbers on HYPO/CATO-style reasoning come from one group on synthetic CATO factor sets in one domain (critique.md). Factors are given to the models in most tests. Nobody outside Pittsburgh has replicated them (gap 6 open). LePREC and ACAL are different tasks from different groups, abstract pages only; they are not replications.

**Failures and null results.**
- No replications or failed replications of the legal-CBR LLM results were found, because none appear to have been attempted.
- CBR-RAG gain (+1.94%) is small, measured by embedding cosine on LLM-made questions, with weights tuned on the same data. No correctness metric (K12, [C]).
- Legal RAG still hallucinates 17-33% (K10).
- ExpeL: reflections added to insight writing hurt (29.0 vs 32.0, HotpotQA) (d14).
- Self-generated analogues fail at weak scale (curie-001 2 to 2) (d11).
- Decodable is not used: no intervention test exists (K27).
- Thinking vs non-thinking is one model family and confounded with RL post-training.

**Moderators.**
- Task depth: single-step distinction is solved; chained steps collapse (a16).
- Case prominence: hallucination falls sharply above the 90th percentile of prominence; rises at lower courts (a15, c14).
- Task type for memory: distilled rules win on HotpotQA, raw cases win on ALFWorld (K14).
- Model scale for self-generated analogues (K25).
- Judge identity and party order in persuadability; a three-party setup differs from a two-party one (b14).

**Interventions that worked.** Retrieving text before citation (partly); human-refined factors; legal-step prompts on statute entailment (+15.79% over the COLIEE 2021 winner; d10); LoRA on rule induction for small models (b12); shortest-of-k selection (short-1@k matches majority voting with up to 40% less compute; d06).

**Did not work or untested.** Abstention instructions (7 of 8 models under 60%; b03). Direct prompting for rule induction (K19). Any steelman or verify-source mitigation of authority sycophancy: not tested anywhere (d04).

## 6. Language models

**Distinguishing precedents (Zhang et al. 2026; a16, b04, b05, c22).** Six LLMs (5 reasoning, 1 non-reasoning), 253 pairs per task, 4 factors per case, temperature 0.3, exact set match.
- Task 1: 100% for all.
- Task 2: 64.82% (gemini-2.5-flash) to 92.09% (gpt-5).
- Task 3: 11.46% to 33.99%.
- Qwen3-235B thinking vs non-thinking: 78.66% vs 30.04% (Task 2), 33.99% vs 0.00% (Task 3).
- Thinking tokens: mean 487 on Task 1 up to 7,025 on Task 3. gpt-5 spent 4,456 on wrong and 3,081 on right Task 2 answers.
- Caveat: the extracted token table had misaligned labels; trust the prose. The pairing "gemini-pro 5,144 tokens for 64.82%" conflicts with the prose, which gives 64.82% to gemini-flash. Unverified.

**Writing arguments from factor sets (Zhang et al. 2025; b01-b03).** Eight LLMs, 30 triples. Faithfulness is high (91-99.6%). Completeness is not: factor utilisation recall 42-85%. Abstention on non-arguable cases is poor. Strong generators were not the best abstainers (Llama-3-70B 3.33%); GPT-4o was best (86.67%).

**Finding factors (a14, b06).** GPT-4 reached the level of the better law-student annotator on a 4-label usefulness task, with F1 only .53. Law-student groups split in agreement (above .5 and below .4). Discovered factors need a human edit.

**Recall of cases (a15, c13, d01).** 58-88% hallucination closed-book. Legal RAG 17-33%. A concrete failure: Lexis+ AI cited Casey's undue-burden standard though it had been overruled (c20).

**Rule induction (b12).** Direct prompting: micro-F1 46.92 to 66.67. Small models with LoRA reach the frontier range (3B: 19.21 to 70.96).

**Persuadability and sycophancy (b13, b14, d03, d04).** Judge LLMs are swayed by advocate quality (8-21% average effect). On EU law, true context adds about +27 to +30 points, and larger reasoning models defer more to false context. No mitigation condition was run.

**Probing (a18, d07).** Factors are readable in 1.7B-8B open models. Authors note TF-IDF is also strong, train and test share a generation procedure, and intervention is future work.

**Agent-style case memory (c07-c11, d13, d14).** Memento: GAIA validation 87.88% Pass@3, test 79.40%; HLE 24.4% PM (second to GPT-5 25.32%); case memory +4.7 to 9.6 points out of distribution. ExpeL (gpt-3.5-turbo): ALFWorld task-similar retrieval 59.0, random 42.5, none 40.0. These are not legal-precedent tasks.

**Other legal LLM work.** ACAL multi-agent argumentation graph: Hearsay F1 76.7%, Learned Hands Courts 70.8%, gains of a few points over baselines (a20; abstract level). Legal Syllogism Prompting and precedent-enhanced judgment prediction exist (c17, c18); their tables were not read reliably (K15). LePREC (a19, d08): LLM-extracted factors plus a sparse linear scorer on 769 real cases, 30-40% over GPT-4o (62% precision); abstract only.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Analogy needs a goal and a side as inputs. Similarity is relative to the question asked, not one global score. Give O7 an explicit "what must match for this question" field. | O7 | [E] | a01, a06, K01 |
| Split the analogy into separately checked sub-steps: list shared and differing features (code), judge each difference (model), combine (code). Do not ask for "compare" in one call. | O7, S2 | [E] theory; the collapse number itself is [S] | a06, a07, a16, K01, K04 |
| Never cite a precedent or prior solution from memory alone. Retrieve the text, then check that each cited source supports the stated holding. | G (verify), memory | [E] | d01, d02, a15, K10, K21 |
| Show few analogues, ranked by relevance (3 to 5; the first gives most of the gain). Relevance beats count. | memory | [E] on "few"; [S] on exact K | c08, d12, d14, K13 |
| Retrieve with a lexical baseline first (BM25) and validate on a held-out split, not the tuning split. | memory | [E] | b10, b11, K11 |
| Do not borrow claimed gains from symbolic legal CBR. Measure our own. | G7 | [E] | K02 |
| Within one item, flag an answer that is far longer than its sibling attempts and re-check it. Relative, never absolute. | G11, S8 | [E] shortest-beats-longest (non-legal) | d05, d06, a17, K23 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Explicit analogise/distinguish moves vs "find a similar case" | O7 | [S]; no direct test exists | K01, K26 |
| Extract factors first (S2), then compare, vs direct comparison on raw text | S2 | extraction is weak [E]; scaffold gain untested | K18, b06 |
| Compute set differences in code and give the model only the judgement step | O7, G5 | untested design inference | a16, K04 |
| Explicit "arguable?" check before analogising (abstain on the analogue, not the answer; G6 still holds) | G, O7 | [S] | b03, K08 |
| Distilled lesson vs raw case in memory, per problem class | memory | [C] | c10, d13, K14 |
| Random vs similar analogue in memory | memory | [S] | d14, K24 |
| Model-recalled analogues for strong models, retrieved for weak | O7 | [S] | d11, K25 |
| Abstract-a-rule step vs direct answer | O2/O7 | [S] | b12, K19 |
| Forced steelman or verify-source against false authority | G, S1 | [S] | b13, d03, K16, K22 |

Check against schema section 4b: nothing here proposes self-reflection, debate or confidence-based stopping. The steelman test is one forced check, not debate (G9), and must beat plain at equal tokens (G7).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, same model, same items, at least 3 seeds, paired interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | HYPO-style case pairs with factor sets (Zhang Task 3 format; build from CATO factors) | A plain CoT; B code computes the set difference, model judges each distinction (emphasise/downplay), code combines | Exact-set-match accuracy | A near 25% or less; B well above, since the step that fails is composition. Add if gain is 15 points or more. |
| T2 | Same pairs, raw text instead of factors | A direct comparison; B S2 factor extraction then compare | Accuracy; factor extraction F1 | Extraction caps B near F1 .5-.6; gain uncertain, a null is possible. |
| T3 | Precedent-citation questions with a retrieval corpus | A closed-book; B retrieve text, then check support for the holding | Wrong-case rate and misgrounded rate, graded separately | Cut of a third to a half (K21). |
| T4 | Analogy tasks from our bench (ARC-like, word puzzles) | A "find a similar problem"; B analogise/distinguish with goal field | Task accuracy | Small, probably single digits. Unknown. |
| T5 | Items with a planted false authority | A plain; B steelman the opposite; C verify the source | Rate of following the false authority | Steelman unknown; verify-source likely best. |
| T6 | Memory sweep | K = 0, 1, 3, 5, 8 analogues; random vs similar | Accuracy per token | Plateau by K 3-5; similar beats random by well over 10 points (ALFWorld 59.0 vs 42.5). |
| T7 | Non-arguable pairs (no shared factors) mixed with arguable ones | A no check; B explicit arguability check | Abstention on non-arguable; false abstention on arguable | A under 60%; B higher without losing arguable items. |
| T8 | Same item, k=4 samples | Majority vote vs flag-if-longest then re-check | Accuracy | Gain depends on how often wrong answers are longest (+45% tokens for gpt-5 wrong answers). |
| T9 | Memory type | Raw case vs distilled lesson, by class | Accuracy by class | Class-dependent; ExpeL shows a swing of about 5 points each way. |

## 9. What does not transfer, and why

- **Symbolic accuracy claims.** HYPO/CATO/IBP numbers are unverified (K20) and come from one hand-built domain.
- **Factor sets.** Law supplies a vetted factor list (26 for trade secret). Our tasks have none; building one is the hard part and LLMs do it poorly (b06).
- **Binding precedent.** Stare decisis makes a precedent authoritative. Our past cases are only evidence. The formal constraint theories (a25, b17, b18) do not apply, and even in law they are contested (K17).
- **Adversarial setting.** HYPO argues for a side. Our agent seeks the true answer. "Downplay" and "emphasise" are advocacy moves; use them only to list candidate arguments, then decide by a check (G5, G8).
- **Persuadability results** concern LLMs acting as judges between advocates (b13). Our agent has no advocate. The lesson that carries over is that stated arguments sway models (G4, G10).
- **Probing results** (a18) show decodable information, not use. A prompt-level scaffold cannot act on it.
- **Agent memory studies** (Memento, ExpeL) use game and search tasks with reward signals, not precedent. They transfer by analogy only.
- **Thinking-mode gains** are confounded with RL post-training and may not appear when we hold the model fixed.
- **Self-generated analogue gains** were measured on arithmetic (GSM8K), not law.

## 10. Open questions

1. Does the Task 3 collapse appear with real opinions and extracted factors, and does a scaffold fix it at equal tokens? (Authors name real opinions as the next step; d07.)
2. What do the original IBP, CATO and Aleven evaluations report? All routes were blocked or paywalled (K20).
3. Does read-then-cite cut wrong-holding citations in a controlled ablation? Only the tool vs closed-book comparison exists (d01).
4. Best K and rules vs cases in the legal domain: no direct test (retrieval metrics in K28 do not give the best K for reasoning).
5. Does a forced steelman cut deference to false authority? No study.
6. Independent replication of the Zhang et al. benchmarks: none found.
7. How do human lawyers and judges reason from precedent? No study was opened. Guthrie, Rachlinski and Wistrich (2001) and Englich et al. (2006) were targeted but PDFs were blocked (403). Anchoring on the first-cited case and framing effects in judging are plausible but not documented here.
8. Do models use decodable factor structure (ablation, steering)?
9. Can thinking length act as a stop or re-check trigger across models on legal items?
10. Prompt-level analogise/distinguish vs plain similarity on chat LLMs: untested (K26).
11. Search coverage: web search quota ran out in file c and APIs gave HTTP 429 in file d, so 2020-2026 LLM studies on HYPO/CATO may be missing.

## 11. Sources

[V] = opened this session (full text, or abstract page where noted); [M] = snippet or citation only.

- [V] Rissland, Ashley and Branting (2006) Case-based reasoning and law, KER 20(3). https://folk.idi.ntnu.no/agnar/CBR%20papers/KER/14.%20CBR%20and%20law%20(Rissland,%20Ashley,%20&%20Branting).pdf (a01-a05)
- [V] Bench-Capon (1997) Arguing with Cases, JURIX. https://cgi.csc.liv.ac.uk/~tbc/publications/arguingCases.pdf (a06, a07)
- [V] Prakken, Wyner, Bench-Capon, Atkinson (2013) argumentation schemes for CBR. https://ics-archive.science.uu.nl/research/techreps/repo/CS-2013/2013-002.pdf (a08)
- [M] Prakken and Sartor (1998) precedents in a dialogue game. https://link.springer.com/article/10.1023/A:1008278309945 (a09)
- [M] Bench-Capon and Sartor (2003) theories and values. https://doi.org/10.1016/S0004-3702(03)00108-5 (a10)
- [M] Ashley (1990) Modeling Legal Argument. https://mitpress.mit.edu/9780262011372/ (a11)
- [V] Allen, Bench-Capon, Staniford (c.2000) multi-agent legal argument generator. https://intranet.csc.liv.ac.uk/~tbc/publications/lagen.pdf (a12)
- [V] Zheng et al. (2021) CaseHOLD. https://arxiv.org/abs/2104.08671 (a13, c15)
- [V] Savelka et al. (2023) GPT-4 and legal text analysis. https://arxiv.org/abs/2306.13906 (a14)
- [V] Dahl et al. (2024) Large Legal Fictions. https://arxiv.org/abs/2401.01301 (a15, c13, c14)
- [V] Zhang, Grabmair, Gray, Ashley (2026) Thinking Longer, Not Always Smarter. https://arxiv.org/abs/2510.08710 (a16, a17, b04, b05, c01-c04, c22)
- [V] Zhang and Ashley (2026) Where Do Legal Factors Live in LLMs? https://arxiv.org/abs/2610.28799 (a18, b07, d07)
- [V, abstract page] Wang et al. (2026) LePREC. https://arxiv.org/abs/2604.19464 (a19, d08)
- [V, abstract page] Cao et al. (2026) ACAL. https://arxiv.org/abs/2602.18916 (a20, d09)
- [V] Guha et al. (2023) LegalBench. https://arxiv.org/abs/2308.11462 (a21 was first a snippet; b08, c16)
- [M] Aleven (2003) CATO evaluation. https://doi.org/10.1016/S0004-3702(03)00105-X (a22)
- [M] Bruninghaus and Ashley (2003) IBP. https://doi.org/10.1007/3-540-45006-8_8 (a23, b22)
- [M] Levi (1949) An Introduction to Legal Reasoning. https://press.uchicago.edu/ucp/books/book/chicago/I/bo3637262.html (a24)
- [M] Horty and Bench-Capon (2012) precedential constraint. https://doi.org/10.1007/s10506-012-9125-8 (a25)
- [V] Zhang, Gray, Savelka, Ashley (2025) faithfulness and abstention. https://arxiv.org/abs/2506.00694 (b01-b03)
- [V] Gray, Savelka, Oliver, Ashley (2024) LLMs to discover legal factors. https://arxiv.org/abs/2410.07504 (b06)
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302 (b09, c05, c06, c25)
- [V] Tang et al. (2025) ReaKase-8B. https://arxiv.org/abs/2510.26178 (b10)
- [V] Sha et al. (2026) prior case retrieval study. https://arxiv.org/abs/2610.07437 (b11)
- [V] Fan et al. (2025) legal rule induction. https://arxiv.org/abs/2505.14104 (b12)
- [V] Suttle and Lillis (2026) persuadability. https://arxiv.org/abs/2604.26233 (b13, b14)
- [V] Molfetta et al. (2026) Sycophants in the Courtroom. https://arxiv.org/abs/2608.21409 (b15, d03, d04)
- [V] Liu, Lorini, Rotolo, Sartor (2022) classifiers and legal CBR. https://arxiv.org/abs/2210.11217 (b16)
- [V] Prakken and van Woerkom (2025) hierarchical result models. https://arxiv.org/abs/2512.13505 (b18); Prakken (2020) (b17)
- [V] Bench-Capon (1999; 2004 review of Roth; 2012 Popov v Hayashi) (b19-b21). URLs not recorded in the evidence file.
- [M] Bruninghaus and Ashley IBP, Aleven CATO second records (b22, b23).
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (c07-c09, c24)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (c10, c11, c26, d13, d14)
- [V] Magesh et al. (2024) Hallucination-Free? https://arxiv.org/abs/2405.20362 (c12, c20, d01, d02)
- [V] Wu et al. (2023) precedent-enhanced legal judgment prediction. https://arxiv.org/abs/2310.09241 (c17)
- [V] Jiang and Yang (2023) legal syllogism prompting. https://arxiv.org/abs/2307.08321 (c18)
- [V] Nay et al. (2023) LLMs as tax attorneys. https://arxiv.org/abs/2306.07075 (c19, d16)
- [V] Hatalis et al. (2025) CBR for LLM agents review. https://arxiv.org/abs/2504.06943 (c21)
- [V] Hu et al. (2024) legal argumentation with NLP. https://arxiv.org/abs/2406.10974 (c23)
- [V] Hassid et al. (2025) Don't Overthink It. https://arxiv.org/abs/2505.17813 (d05, d06)
- [V] Yu, Quartey, Schilder (2022) Legal Prompting. https://arxiv.org/abs/2212.01326 (d10)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (d11, d12)
- [V] Pipitone and Alami (2024) LegalBench-RAG. https://arxiv.org/abs/2408.10343 (d15)
- [M] Guthrie, Rachlinski, Wistrich (2001); Englich et al. (2006): targeted, PDFs blocked, no number used.
