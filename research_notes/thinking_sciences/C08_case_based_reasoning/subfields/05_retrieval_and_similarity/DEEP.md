# Retrieval and similarity: deep document

*Subfield C08.05 of case-based reasoning (CBR). Key works named in the brief: Weber; Richter. Evidence base: evidence_a-d.jsonl (a01-a30, b01-b25, c01-c26, d01-d19), claims.jsonl (K01-K31), critique.md. About 25 distinct papers sit behind about 100 evidence lines (many papers were read two or three times). Most LLM-era retrieval numbers come from 2021-2024 models (GPT-Neo, GPT-J, GPT-3, Codex). The Weber and Richter classic papers were never opened. That is the largest hole against the brief, and it is stated again in sections 2, 10 and 11.*

## 1. What it is

Retrieval is the step in the CBR cycle (retrieve, reuse, revise, retain) that picks which stored past cases to show the solver for a new problem. A case is a problem, its solution, and often its outcome. The question of the subfield: how should "nearest" be defined, and does nearest mean most useful?

Three layers matter for our agent.

1. **The key.** What text or structure is compared: the raw problem, an abstract of the problem's structure, the plan, or the outcome.
2. **The score.** Surface similarity (word overlap, embedding cosine), structured similarity (weighted attributes, local-global measures), learned usefulness (a retriever trained on which cases helped a model), or adaptation cost (how hard the case is to turn into a solution).
3. **The set.** One case or several. Top-k by score, or a set chosen for relevance plus diversity. How many. In which order. Whether to retrieve at all.

The classic CBR claim is that similar problems have similar solutions. The LLM-era findings (section 3) keep part of it. Similarity beats random by a wide margin. Plain similarity is not the best score, though. Learned usefulness and diversity beat it on hard or compositional tasks, and retrieval can hurt when no stored case is truly close.

Where this lands in our schema: the Memory section (lessons, class record, planned subgoal library), the S0 gate (when to retrieve), S9 (what to store), and O7 (map an analogue, whose source must be found by retrieval).

## 2. History and theories in depth

**Nearest-neighbour theory (1967).** Cover and Hart proved that with unlimited stored cases, the 1-nearest-neighbour rule has error at most about twice the Bayes error: R* <= R <= 2R*(1-R*) for two classes, and R* <= R <= R*(2 - M R*/(M-1)) for M classes (a01, opened). It holds for any metric in the limit of infinite sample. It says nothing about small case bases, irrelevant features, or which metric is right. Our case banks have tens to hundreds of items, so the guarantee does not apply.

**Instance-based learning (1991).** Aha, Kibler and Albert compared ways to build a case base (a02-a04, opened). IB1 stores everything. IB2 stores only cases it misclassifies. IB3 adds a per-case accuracy record with a significance test and drops cases that perform poorly. Averaged over 50 trials: Voting 91.8/90.9/91.6 (IB1/IB2/IB3) with storage 100/11.1/7.4 percent; Cleveland 75.7/71.4/78.0 (storage 100/30.4/7.7); Hungarian 58.7/55.9/80.5 (C4 78.2); Primary Tumor 34.7/32.9/38.6 with storage 100/71.3/16.4. With 10 percent noise, IB2 kept 76 instances of which 20 were noisy (26.3 percent), while IB3 kept 25 and none were noisy. Lesson: keeping only what you got wrong stores noise. A per-case record of how the case performed when used fixes this.

**Similarity as a theory (human side).** Tversky's 1977 contrast model (a06, snippet only) says similarity is feature-based and can be asymmetric (people judge North Korea as more like China than China like North Korea). Ontanon's 2020 survey (a05, opened) gives the usable formula: Tversky index = |X and Y| / (|X and Y| + alpha |X-Y| + beta |Y-X|). Jaccard is the case alpha = beta = 1 (as printed in the survey text). Cosine differs from Minkowski distances by ignoring vector length. Gentner and Forbus's MAC/FAC (a12, not opened) is the two-stage human-inspired model: a cheap content-vector filter (many are called) then a structure-mapping stage (few are chosen). It is covered by the parallel subfield "Analogical retrieval (MAC/FAC)"; we only note the link.

**The classic CBR retrieval programme (Weber, Richter, and others) was not read.** What we know only from snippets and citations (a07-a11, a30 all opened:false):
- Aamodt and Plaza (1994) fixed the four-step cycle.
- Richter (1995) argued that similarity measures hold much of a system's knowledge, and Richter and Weber (2013) is the textbook that systematises it.
- Bergmann and others developed local-global similarity: a local score per attribute, a weight per attribute, and a global score as the weighted sum. This is what "Weber and Richter style" means in practice.
- Lenz and Burkhard (1996) built case retrieval nets, a spreading-activation index for fast retrieval.
- Smyth and Keane (1998) argued that similarity is the wrong target. Retrieve the case that is cheapest to adapt.

We have no number from any of these except the Smyth and Keane technical report (below). Do not claim they are confirmed or refuted for LLM agents.

**Adaptation-guided retrieval (AGR).** The Smyth and Keane report (d01, d02, opened) is the one classic retrieval experiment we read. Domain: case-based design with a symbolic adapter. Experiment 1, 45 target problems: AGR picked the most adaptable case 100 percent of the time, standard similarity 70 percent (chi-squared(1)=14.3) with 45 cases. With 120 cases across 8 models the similarity rate fell to 12 percent. Experiment 3, 100 cases, 45 problems: AGR solved in mean 2.07 s per problem against 6.22 s for similarity, about 3x faster. This is one group's test in a symbolic design system with a hand-built adaptation-cost estimator. No LLM-era test exists in our evidence (d03, d19).

**In-context example selection (2021 onward).** The field moved from classic CBR into prompt demonstration selection. KATE (Liu 2021) showed nearest neighbours beat random for GPT-3. EPR (Rubin 2022) trained a retriever on which examples helped a language model. CEIL (Ye 2023), UDR (Li 2023), LLM-R (Wang 2023) extended it. Diversity papers (Levy 2023, Xiao 2025, Kapuriya 2025) showed pure top-k fails on compositional tasks. Min et al. (2022) argued that labels in fixed demos matter little. Yoo et al. (2022) contested that.

**Agent case memory (2023 onward).** ExpeL, Voyager, Generative Agents, DS-Agent, AWM, Memento, ReasoningBank, CASCADE and the memory-management study of Xiong et al. apply retrieval to experience stores. These are the closest to our use. Most compare against no memory, not against a random-memory control (critique.md weak spots).

**Retrieval-quality and use theory.** BEIR (Thakur 2021) shows lexical BM25 is a hard baseline out of domain. BRIGHT (Xiao 2025) shows embeddings fail when relevance needs reasoning. Steck et al. (2024) show that cosine similarity of learned embeddings can be arbitrary in theory (linear models only). Lost in the Middle (Liu 2023), GSM-IC (Shi 2023), Power of Noise (Cuconasu 2024) and Yoran et al. (2024) study how retrieved text is used or misused.

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, direction agrees), **S** single source, **C** contested. Model era is stated where it limits the claim.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| 1-NN error is at most about twice the Bayes error (infinite sample) | R <= 2R*(1-R*), two classes | Cover and Hart 1967 (a01) | S, asymptotic only |
| Keeping only misclassified cases stores noise; a per-case record fixes it | 10% noise: IB2 26.3% noisy kept, IB3 0; Hungarian 55.9 vs 80.5; storage 7.4-16.4% for IB3 | Aha et al. 1991 (a02-a04) | S |
| Nearest-neighbour demos beat random for GPT-3 | IMDB 91.99 vs 87.95 +-2.74 random; NQ EM about 41 vs 28.6; ToTTo BLEU 40.3 vs 28.4; nearest-10 EM 46.0 vs farthest-10 31.0 (100 NQ questions) | KATE, Liu 2021 (a13, a14, b01, c01) | S (direction replicated, see next row) |
| Direction replicated elsewhere | Random on structured outputs very low: BREAK 1.7, MTOP 7.3, SMCalFlow 8.9 vs BM25 26.0/52.9/46.1 (GPT-Neo 2.7B, dev). CEIL 12-dataset mean: Random 30.68 vs TopK-BM25 45.84 | EPR (b04); CEIL (a17) | E |
| Random demo sets vary a lot | SST-2 five random sets: 94.6, 95.0, 95.8, 93.9, 86.9; IMDB random sd 2.74 | KATE (c01) | S |
| Encoder choice matters; mismatched tuning can hurt | IMDB: tuned on SST-2 93.43; roberta 91.99; NLI 90.40; NLI+STS-B 90.20 | KATE (b02) | S |
| Plain kNN label voting is near chance, so the LLM reading the cases does the work | IMDB kNN-roberta 50.20 vs KATE 91.99; ToTTo BLEU kNN 14.1 | KATE (c02, b02) | S |
| Larger candidate pool gives larger gain | NQ pool 1k to about 70k, gain grows | KATE (b03) | S |
| BM25 beats dense SBERT for structured-output case retrieval; learned dense wins on open QA | Dev BREAK/MTOP/SMCalFlow: SBERT 21.6/48.7/43.6 vs BM25 26.0/52.9/46.1. BEIR: BM25+cross-encoder beats BM25 on 16 of 18 datasets; ColBERT on 9 of 18 | EPR (a16, b04), BEIR (b20), RAG (a23) | E, task-dependent |
| Retriever trained on LM-scored usefulness beats surface similarity | Dev BREAK 31.9 vs 26.0, MTOP 64.2 vs 57.0 (CBR-style retriever), SMCalFlow 54.3 vs 51.4. Test BREAK 23.9, MTOP 64.4, vs BM25 17.6/49.0 | EPR (a15, b05, c03) | E |
| EPR matches or beats an oracle that sees the gold output | BM25-oracle BREAK 32.3 (EPR 31.9, tie), MTOP 58.9 (EPR 64.2), SMCalFlow 47.3 (EPR 54.3) | EPR (b06) | S |
| Retriever trained on GPT-Neo transfers to other LMs | 2-8 points over BM25 and CBR on GPT-J, GPT-3, Codex. GPT-J BREAK 31.5 vs 33.6 (own-trained). Codex 29.5 vs 29.3 | EPR (c04) | S |
| More learned retrievers: UDR, LLM-R | UDR unseen: Twitter 56.8 vs BM25 50.0; QNLI 74.4 vs 54.1; Ruby 19.6 vs 9.2. LLM-R avg: SBERT 62.1, EPR 63.5, LLM-R 65.7 (1 iter), 66.5 (2), 66.4 (3) | a19, a20 | E (with EPR) |
| Set-level selection beats one-by-one | 12-dataset mean: CEIL 56.76, EPR 53.37, TopK-BM25 45.84, Random 30.68 (GPT-Neo 2.7B). Gain <1 point on CommonsenseQA and HellaSwag; >20 on NLI | CEIL (a17, c05) | S (one group) |
| Selective annotation of what to store beats random | Relative gain 11.4% (budget 100), 12.9% (budget 18); absolute 5.2 and 5.8 points; random retrieval did not benefit | vote-k, Su 2022 (a18) | S |
| Diversity helps when no single stored case is close | SMCalFlow-CS 32-C: top-K 50.3 to Cover-LS 73.5 (Codex, 100-example test subset); wins on 7 of 8 compositional splits | Levy 2023 (c06) | E (with Xiao) |
| Diversity boundaries | Cover-LS 0.3 vs top-K 17.0 on zero-shot 0-C split; COVR-10 random 69.4 beat top-K 61.8 | Levy 2023 (read in the paper, critique item 3) | S |
| Diversity is not free | Llama-3.1-8B k=4: SST-2 TopK 94.13 vs TopK-Div 92.75 vs Div 91.50; SQuAD 73.28 vs 77.71; CsQA 72.57 vs 72.77; GSM8K 81.74 vs 82.98 | Xiao 2025 (b09, b10) | E |
| MMR rerank helps in most configurations, by small margins | Beats or matches standard ICL in about 70% of configurations; COLA up to +9.7%; SST-2 +0.0 to 1.2% | Kapuriya 2025 (b07, b08) | S |
| Labels in fixed random demos matter little | Drop 0-5% absolute; mean 2.6 (classification), 1.7 (multi-choice); 12 models; k=16, 5 seeds | Min 2022 (a22, b12, c07) | C |
| Label correctness matters in some setups | Gap depends on template and model size | Yoo 2022 (d18, per-model values not transcribed) | C |
| Models copy from top retrieved examples | MTOP: 84.5% of outputs abstractly matched a retrieved prompt; EM 71.6 on that subset vs 64.2 overall. Agents: output similarity rises with input similarity | EPR (c04); Xiong 2025 (d05) | E |
| Add-all agent memory hurts vs fixed small memory | RegAgent 55.48 vs 67.53 fixed; EHRAgent 13.05 vs 16.75; AgentDriver 32.32 vs 40.11; CIC-IoT 59.90 vs 71.50 | Xiong 2025 (d06) | S |
| Strict quality filter helps | RegAgent 70.95; EHRAgent 38.50; AgentDriver 51.00; CIC-IoT 85.4 | Xiong 2025 (d06) | S |
| Pruning needs enough retrieval history | History deletion needs at least 5 retrievals, utility threshold 0.5 (0.3-0.7). RegAgent strict: no deletion 70.95 (2938 records), periodic 67.65 (949), history 69.80 (2286) | Xiong 2025 (d07) | S |
| Best k in agents is small | Memento F1/PM: K=0 59.9/72.2; 1 63.6/77.9; 2 63.7/78.1; 4 64.5/78.5; 8 64.1/78.2; 32 63.9/78.1. ReasoningBank WebArena-Shopping: k=0 39.0, 1 49.7, 2 46.0, 3 45.5, 4 44.4 | a26, c10, c12 | E |
| Case memory helps most out of distribution | Memento OOD +4.7 to +9.6; in distribution at iteration 5 +0.4 (non-parametric), +1.0 (parametric); saturates near 3k items. PM at iteration 5: no CBR 84.47, non-param 84.85, param 85.44 | Memento (a25, b22, c09) | S |
| Self-generated successful trajectories help | ALFWorld 73 to 89 (93 with curation); Wordcraft 55 to 64; InterCode-SQL 75 to 79 (gpt-4o-mini). Efficiency falls as bank grows | Sarukkai 2025 (b13-b15) | S |
| Task-similarity retrieval beats random and step-similarity in ExpeL | ALFWorld: ReAct 40.0 +-0.3; random successes 42.5 +-0.8; step-similarity 48.5 +-2.1; task-similarity 59.0 +-0.3 | ExpeL (c13) | S |
| Store distilled content, not raw traces | AWM +4.0 step success over Synapse on Mind2Web (+24.6% relative Mind2Web, +51.1% WebArena); ReasoningBank gains +8.3, +7.2, +4.6 over memory-free on three backbones | c11, c14 | E |
| Learned or adaptive selection adds a few points | CASCADE 66.68 vs NP-CBR 63.76 (12 tasks, Qwen3-32B, preprint); Memento parametric +0.6 at iteration 5; DS-Agent re-rank average rank 2.58 to 2.08 | a27, a25, c16 | E (small) |
| LLM-written structure abstracts make better keys | Spider: Skill-KNN 78.3 vs best raw-input 74.6 (oracle Target-KNN 78.6) | An 2023 (d12); Buffer of Thoughts (d14) | S |
| Semantic embeddings fail on reasoning-heavy relevance | BRIGHT: best MTEB model 59.0 nDCG@10 gets 18.3; reasoning-rewritten queries add up to 12.2 | c23 (theory c22) | E |
| Position matters for long context | Lost in the Middle: GPT-3.5 down more than 20 points (worst case under closed-book 56.1; oracle 88.3) | a29, b18, c19 | E (2023 models, long context) |
| Irrelevant text hurts | GSM-IC: at most 18% of solved base problems stay solved across distractor types; Yoran: random passage cuts Llama-2-13B more than 10 points; top-1 Google hurts on StrategyQA and Fermi | b16, c21, d10 | E |
| Random documents sometimes help | Up to +35% (abstract); +0.08 (+36%) in the best near setting | Cuconasu 2024 (c20) | S, mechanism unknown |
| Example order swings accuracy | 4 examples, 24 permutations: about 50% to over 85% (SST-2, Subj). GPT2-XL SST-2 variance: Random 0.90, TopK 0.56, TopK+ConE 0.26 | Lu 2022 (d16); Peng 2024 (d17) | E (old models) |
| A retrieval gate has measurable value (QA) | PopQA: retrieval wrong on 10% of questions otherwise right; popularity gate +5.3 points; FLARE plateau at about 60% of sentences retrieved | d08-d11 | E (QA only) |
| Self-generated analogues vs retrieved | davinci-003 GSM8K 5-shot: fixed 54, retrieved 57, self-generated 61. GPT-3.5-turbo self-generated: K=1 76.1 vs K=5 77.8 (GSM8K); MATH 34.8 vs 37.1 | Yasunaga 2024 (d13) | S |
| Many-shot ICL keeps improving on some tasks | Bemba +15.3%, Kurdish +4.5% over 1-shot; degrades at 250 shots on one task | Agarwal 2024 (c08) | S |
| Case-based RAG with hand-set weights | +1.94% cosine over no-RAG (0.8967 to 0.9141), weights [0.25, 0.40, 0.35], k=3, 32 test cases | CBR-RAG (b21, c15, d15) | S, weak |
| Single-case feedback in small open models | Llama-3.1-8B history 76.9 to 82.1; gains 0 to 1 point for 70B and 32B models | Yin and Leake 2026 (d04) | S |
| Recency-importance-relevance scoring | Never ablated term by term; full 29.89 vs no reflection 26.88 TrueSkill | Generative Agents (c17) | S, gap |

## 4. Mechanisms and models

Each model below is described so it can be coded.

**4.1 Embedding top-k (KATE).**
1. Encode every stored problem with one encoder. Encode the new problem.
2. Take the k stored problems with highest cosine (or lowest L2 in FAISS).
3. Put their (problem, solution) pairs in the prompt. Order is data-dependent: reverse order (most similar last) helped on NQ, default order was slightly better on WQ and TriviaQA.
4. Pick the encoder with the task in mind. An encoder tuned on a related task helped; one tuned on a dissimilar task (NLI, STS-B) slightly hurt on IMDB and ToTTo.
The LLM, not the vote, does the work: plain kNN labels scored 50.2 on IMDB.

**4.2 BM25 key.** Tokenise the problem text, compute BM25 against stored problems. It costs no model tokens and needs no embedding call. On structured-output tasks it beat SBERT (BREAK 26.0 vs 21.6). It is the right first baseline for our bench.

**4.3 Learned usefulness retriever (EPR, UDR, LLM-R).**
1. Candidate generation: for each training item, take top candidates by BM25.
2. Scoring: run the LM with each candidate as the demo and record the probability of the gold output.
3. Labels: top-scored are positives, low-scored are hard negatives.
4. Train a bi-encoder with a contrastive loss. At test time embed and take top-k.
LLM-R iterated this: 65.7, 66.5, 66.4 over three iterations, so the gain saturates after two. The light version for our agent is an outcome log: for each stored case, count how often showing it preceded a verified solve, and add that to the similarity score. It needs no training, but it needs enough retrievals per case (Xiong et al. used at least 5).

**4.4 Set-level and diversity selection.**
- MMR: pick items one at a time, maximising lambda * relevance(item, query) minus (1 - lambda) * max similarity(item, already chosen). Best lambda mostly 0.5 or more (b08).
- Cover-LS (Levy): choose demos that together cover the local structures (sub-program pieces) of the predicted output. It needs a first-pass guess of the output structure.
- CEIL: a determinantal point process model (relevance times diversity) trained with LM feedback.
- Rule of thumb from the data: plain top-k when a near-duplicate exists; a covering or diverse set when each stored case covers only part of the new problem.

**4.5 Adaptation-guided retrieval.**
1. Take the top n (say 5) similar cases.
2. For each, estimate the cost to turn its solution into a solution for the new problem. The classic system used a rule-based count of adaptation steps. An LLM version would use LLM-judged edit effort or an edit distance between the old solution and a draft new one.
3. Retrieve the lowest-cost case.
The classic test showed 100 percent vs 70 percent (45 cases) and 12 percent (120 cases) at choosing the most adaptable case. The LLM version is untested.

**4.6 Two-stage retrieval (MAC/FAC shape).** Stage one: cheap vector or BM25 filter to a short list. Stage two: structural comparison by a model or code on the short list. EPR, Skill-KNN and the BRIGHT query-rewriting results all have this shape: a cheap pass over text, then a more expensive judgement of structure.

**4.7 Structure-abstract key (Skill-KNN, Buffer of Thoughts).** Ask the model once per stored case to write an abstract of the problem structure (what is asked, what kind of reasoning is needed), and index on that. Do the same for the new problem. Spider: 78.3 vs 74.6. It costs one model call per case on insert and one per query.

**4.8 Local-global similarity (Weber, Richter, Bergmann; not read).** Sim(query, case) = sum over attributes of weight_i * local_sim_i(query_i, case_i). Local similarity is per attribute (numeric distance, taxonomy distance, string overlap). We have no verified numbers on its benefit. CBR-RAG used hand-set weights [0.25, 0.40, 0.35] over three text fields with an AnglEBERT embedding and got +1.94% cosine over no retrieval, without an ablation of the weights.

**4.9 Retrieval gate.** Skip retrieval if (a) top similarity is below a threshold, (b) a cheap first attempt is confident, or (c) a router judges the problem easy. Measured gates exist only for QA: a popularity gate +5.3 points on PopQA (d08), a confidence-threshold sweep that plateaus (d09), a trained complexity router (d11). Nobody has measured a similarity-threshold gate for case reuse.

**4.10 Quality-gated store (Xiong et al., Voyager).** Store a run only after an external check passes. Voyager adds skills only after running the code. Xiong et al. show strict filtering beats add-all in four agents. Deletion rules (periodic, history-based) cut memory about 3x for a 1 to 4 point loss on RegAgent (d07).

**4.11 Position control.** Put the best case last (nearest the question) or first, and run a reverse-order check. Old evidence (d16, d17) shows large order effects for small models. The 2025-26 effect for 1 to 4 short cases is unknown.

## 5. What holds up

**Replicated and robust (direction)**
- Similarity-ranked demonstrations beat random ones. KATE (GPT-3) is single-lab, but EPR, CEIL, UDR, ExpeL and Sarukkai reproduce the direction with other models and tasks. Random baselines on structured outputs are very low (1.7 to 8.9 in EPR; 30.68 mean in CEIL). No exact replication of KATE exists.
- Learned usefulness beats surface similarity (EPR, UDR, LLM-R, CEIL): about 3 to 11 points over the best similarity baseline.
- Small k wins in agent memory (Memento K=1 gives 3.7 F1 of the 4.6 gained at K=4; ReasoningBank k=1 best).
- Verified-only storage beats add-all (Xiong 2025; Voyager design; IB3 vs IB2 in 1991).
- Distilled content beats raw traces (AWM, ReasoningBank).
- Irrelevant retrieved text hurts (GSM-IC, Yoran, Lost in the Middle).

**Failed, null or weak**
- Zero-shot diversity: Cover-LS 0.3 vs top-K 17.0 on the 0-C split. Diversity can collapse when there is no related data.
- COVR-10 random (69.4) beat top-K (61.8) in Levy et al.
- Easy tasks: SST-2 diversity gains 0.0 to 1.2 points, and TopK beat TopK-Div (94.13 vs 92.75).
- Memento in distribution: +0.4 and +1.0 only. Parametric over non-parametric: +0.6.
- Larger k in agent memory is flat or worse past 1 to 4.
- CEIL under 1 point on CommonsenseQA and HellaSwag.
- BM25 beats dense on structured output, but dense wins on open QA. No retriever is best everywhere.
- Fine-tuning an encoder on a dissimilar task slightly hurt (KATE).
- Cosine on learned embeddings can be arbitrary (Steck, linear models only).

**Contested**
- Do labels in demonstrations matter? Min et al.: 0-5 points (mean 2.6). Yoo et al.: depends on template and model size. Both used fixed demos. For retrieved near-duplicates, EPR and Xiong show copying. Nobody ran corrupted labels on retrieved cases with a frontier model.
- Random noise documents: Power of Noise says up to +35%, GSM-IC and Yoran say irrelevant text hurts. Different models, tasks and placement.
- Best k: Memento K=4 vs ReasoningBank k=1. Plans vs strategies; no variance reported.

**Moderators found**
- Task difficulty (easy: similarity enough; compositional: diversity).
- Presence of a close case (zero-shot split collapse).
- In vs out of distribution (Memento).
- Encoder-task match (KATE).
- Model size (Yasunaga: small models gain more from retrieval than from self-generation; Yin and Leake: 70B and 32B gain 0 to 1 point from one retrieved case).
- Bank size (larger pool helped KATE; bank saturates near 3k in Memento; Sarukkai marginal value falls).
- Position (old models).

**Interventions that worked:** outcome-based re-ranking; verified-only storage; strict filters; distilled strategies; LLM-written structure keys (single source); small k; popularity or confidence gates (QA).
**Interventions that did not work or are unproven:** keep-the-failures storage under noise (IB2); add-all memory; high-k retrieval; hand-set attribute weights (no ablation); diversity at zero cross-domain data.

**Weak spots in the evidence (critique.md):** about 25 independent papers; most ICL results use 2021-23 models; no random-memory control in Memento, ReasoningBank, Sarukkai, CASCADE; tiny test sets (NQ 100 questions, CBR-RAG 32 cases, Levy 100 examples); few confidence intervals; CASCADE is a 2026 preprint; the Huawei paper (a28) was not opened.

## 6. Language models

**Older models (GPT-Neo 2.7B, GPT-J, GPT-3, Codex, Llama-2).** Retrieval of similar demonstrations gives large gains over random, especially on structured outputs (BREAK 1.7 random vs 26.0 BM25 vs 31.9 EPR). Trained retrievers add 3 to 11 points over BM25 or SBERT. Order matters a lot for small models (50 to 85 percent across permutations of four examples). Distractors cut accuracy (GSM-IC at most 18 percent stably solved; Llama-2-13B more than 10 points with a random passage).

**Newer models (Llama-3.1-8B, GPT-4-class, Qwen3-32B, Gemini-2.5-flash, GPT-4o-mini).**
- Diversity: Llama-3.1-8B shows small differences. GSM8K Rand 81.99, TopK 81.74, Div 82.81, TopK-Div 82.98. When zero-shot is already high, headroom for retrieval is small.
- Agents: Memento (GAIA validation 87.88 Pass@3, test 79.40; DeepResearcher F1 66.6, PM 80.4) gains +4.5 F1 / +7.0 PM on HLE, +3.7/+5.3 on SimpleQA, +6.7/+8.2 on DeepResearcher over no-CBR. ReasoningBank gains +8.3, +7.2, +4.6 on WebArena. Sarukkai: gpt-4o-mini ALFWorld 73 to 89, a bigger gain than upgrading to gpt-4o. All of these are against no-memory, never against random-memory.
- Strong models gain less: Yin and Leake (MMLU, k=1 case, bge-small, FAISS L2): Llama-3.1-8B history 76.9 to 82.1, and gains of 0 to 1 point for 70B and 32B models.
- Self-generated examples: gpt-3.5-turbo does better with more analogues (K=5) than with K=1. This is the opposite pattern from agent case retrieval.
- Experience following: across four agents (GPT-4o and DeepSeek-V3 among the backbones), output similarity rises with input similarity, so models copy the nearest stored run and its errors (d05, d06).
- Retrieval can hurt: on PopQA (GPT-3 era) retrieval made the model wrong on 10 percent of questions it had right. Top-1 retrieval hurt on StrategyQA and Fermi (d10).
- Reasoning-heavy relevance: BRIGHT, best embedder 59.0 on MTEB gets 18.3; reasoning-rewritten queries add up to 12.2.
- Many-shot with fixed examples kept improving on some tasks to about 125 shots and degraded at 250 on one.

**What changed performance, by how much (among tests we read):**
1. Learned vs similarity ranking: +2.9 to +11.3 points over the best baseline (EPR).
2. Diverse set vs top-K when no case is close: up to +23 points (Levy).
3. Verified vs add-all memory: 8 to 12 points of agent success (Xiong).
4. k=1 vs none in agents: +3.7 F1 (Memento), +10.7 success points (ReasoningBank, 39.0 to 49.7).
5. k beyond 1 to 4: 0 to -5 points.
6. Weighted attributes: +1.94% cosine, unablated.
7. Position and order: tens of points for old small models; unmeasured for new models with short context.

**What no study gives us:** a frontier model, multi-step reasoning, k=1, with a random-solved-case arm and a no-case arm at equal tokens. Closest: Yin and Leake (no random arm), Yasunaga (k=5, davinci era), Peng (GPT2-XL).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Include a random-case control and a no-case control in every retrieval test.** G7 (pay for itself at equal tokens). [E] Evidence: a13, a15, a17, b04, c13; the missing control is the main gap in the agent papers.
2. **Keep k small: default k=1, never above 4.** Memory (retrieval size), S3. [E] Evidence: a26, c10, c12.
3. **Store only verified outcomes, not everything.** Memory, S9 (the lesson line is written only after S8 verify passed). Keep a per-case record of success when shown. [E] Evidence: d06, a02, a03, c18. This fits the existing rule that a lesson is trusted only after it helps on two problems; the per-case record is the IB3 idea.
4. **Store distilled lessons or strategies, not raw traces.** Memory. [E] Evidence: c11, c14, c13.
5. **Keep the rule that lessons are shown after the first attempt.** Models copy the nearest retrieved case (experience following), so early display would fix the attempt on it. Protects G4 and S3 independence. [E] Evidence: c04, d05. Do not loosen this rule.
6. **Treat retrieved cases as untrusted text.** Irrelevant or wrong cases hurt (GSM-IC, Yoran, Xiong). A case is a hint checked by code (G2, G3, G10), never evidence. [E] Evidence: b16, c21, d10, d06.
7. **Use BM25 as the first, token-free key.** Memory. [E] for structured-output tasks. Evidence: a16, b04, c03. Dense retrieval is a second arm, not the default.
8. **Log which cases were shown and whether the run passed.** Schema section 6. This is the data for outcome-weighted retrieval later. [E] as a log; using it is a test (below).

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Outcome-weighted re-rank: similarity plus success-count bonus | memory | [S] trained retrievers gain 3-11 points; light version untested | a15, a16, b05, d07 |
| LLM-written structure abstract as the key vs raw text | memory, S1 | [S] 78.3 vs 74.6 on Spider (2023 model) | d12, d14, c23 |
| Similarity-threshold gate: skip case retrieval when top score is low | S0 | [S] QA gates only | d08-d11, c06 (0-C collapse) |
| Diverse set (MMR or cover) when no case is close | memory, S3 | [E] compositional, [C] easy tasks | c06, b09, b10 |
| Adaptation-cost ranking of top-5 | memory, O7 | [S] symbolic only | d01, d02 |
| Corrupted-label retrieved cases (does the agent copy wrong solutions?) | G2, G10, memory | [C] | a22, d18, c04, d05 |
| Self-generated analogue arm | O7 | [S] | d13 |
| Order and position of 1-4 cases | memory | [E] old models, no data for new | d16, d17, a29 |
| Per-case pruning after 5 retrievals | memory | [S] | d07 |
| Weighted multi-field similarity (Weber/Richter style) | memory | [S] weak, no ablation | b21, c26 |
| Distant-analogue source retrieval for O7 | O7 | [S] | a12 (not opened), c23 |

## 8. Concrete tests on our bench

All arms get the same total token budget (case text counts). Report mean and an interval over at least 5 seeds. Cases come from a bank built on separate problems (no test leakage).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and BrainTeaser items with a stored bank of verified solved items | none / random-1 / nearest-1 (BM25) / nearest-1 (embedding) | pass rate; fraction of answers copying the case | nearest above random by 3+ points; random about equal to none or worse; copy rate high |
| T2 | Same, split into seen-class and unseen-class items | none vs nearest-1, by split | gain per split | gain larger on unseen, as in Memento (+4.7 to +9.6 vs +0.4) |
| T3 | Same, 30 percent of stored solutions corrupted | nearest-1 clean / nearest-1 corrupted / none | pass rate drop | if corrupted falls below none, the agent copies; then verification must reject |
| T4 | Same | key = raw text / LLM structure abstract / plan text / outcome summary, k=1 | pass rate | abstract above raw by 2+ points (Skill-KNN: +3.7) |
| T5 | Same | k in {0,1,2,4,8} | pass rate at equal tokens | most gain at k=1; flat or lower past 4 |
| T6 | Same | top-3 similarity / MMR-3 / top-1, by item difficulty | pass rate by difficulty | MMR above top-k on hard items, ties or loses on easy |
| T7 | Same | always retrieve / retrieve only if top score >= tau (sweep) | accuracy against retrieval rate | a tau exists that beats always-retrieve; harm region at low scores |
| T8 | Same | similarity rank / success-weighted rank / adaptation-cost rank (top-5, LLM-judged) | pass rate; extra tokens | success-weighted +1 to +3; adaptation rank unknown |
| T9 | Same | nearest-1 in order A vs reverse; best case first vs last | pass rate gap | gap under 1 point means position can be ignored |
| T10 | Long runs with a growing bank | add-all / verified-only / verified plus pruning after 5 retrievals | pass rate at bank size 10, 30, 100, 300 | verified-only beats add-all by 5+ points at 100 or more |
| T11 | Same | stored-case retrieval vs self-generated analogue (no bank) | pass rate; tokens | self-generated catches up for strong models |

## 9. What does not transfer, and why

- **Cover and Hart bound.** It needs unbounded cases. Our banks have tens to hundreds.
- **EPR, UDR, CEIL training.** These need thousands of labelled items and many LM calls to score candidates. Our online bank is far smaller. Only the idea (score by usefulness) transfers, as a success counter.
- **Most ICL numbers.** They come from GPT-Neo 2.7B, GPT-J, GPT-3 and Codex on parsing and QA tasks. A 2025-26 frontier model has higher zero-shot scores, so headroom is smaller (Yin and Leake: 0 to 1 points for 70B and 32B).
- **Lost in the Middle.** It covers 10 to 30 long documents. We show 1 to 4 short cases. The position effect may be tiny. Also, the 56.1 vs 56.0 figures in b19 are closed-book columns and are not evidence about reading the middle (critique item 2).
- **Retrieval gates from QA (popularity, FLARE).** They gate fact lookup, not case reuse. The principle (retrieval can hurt) transfers, the threshold does not.
- **Power of Noise.** The result is for RAG on NQ with specific placement. Do not use random documents as a trick.
- **Weber and Richter local-global weights.** Typed attributes exist in symbolic CBR. Our cases are free text. Weights over hand-made fields would add set-up cost with no measured gain (G7).
- **Classic AGR numbers.** The adapter was a rule system with cost estimates. An LLM adapter can adapt almost anything, so cost differences may shrink.
- **Memento and ReasoningBank gains.** They are against no-memory, in web or research agents, with single runs. They show the memory idea, not retrieval quality.
- **Human similarity theory (Tversky).** Asymmetry and feature contrast describe people. We have no measured effect on an LLM retriever.

## 10. Open questions

1. At equal tokens, does k=1 nearest solved case beat a random solved case and no case for a 2025-26 frontier model on multi-step reasoning?
2. Do retrieved near-duplicates with wrong solutions pull a frontier model to the wrong answer? How much does a verify step undo?
3. Does LLM-judged adaptation cost beat similarity as a ranking? (Smyth and Keane: 100% vs 70% and 12% in a symbolic system.)
4. Which key works best: raw text, structure abstract, plan, outcome? No paper compares plan or outcome as keys.
5. What is a good skip-retrieval gate for cases? What similarity threshold marks the harm region?
6. How does a tiny online bank (tens of cases) behave with outcome-weighted ranking? Pruning needs 5 or more retrievals per case.
7. What do Weber, Richter and Bergmann weights buy over one embedding? The classic works are unread.
8. Is the 20 to 28 percent agreement between LLM-chosen and k-NN-chosen cases (Wilkerson and Leake, as cited in project notes) real? The source was not located in two searches. Does LLM-chosen retrieval beat embedding retrieval downstream?
9. Do position effects persist for 1 to 4 short cases in 2025-26 models?
10. How does bank size affect quality, noise and forgetting (links: Case-base maintenance, Retention policy)?
11. Why do random documents sometimes help (Power of Noise) while distractors hurt?
12. Why does the best k differ (Memento 4, ReasoningBank 1)? Case type, task, or noise?

## 11. Sources

[V] = opened and read (page or PDF text). [M] = snippet or citation only.

- [V] Cover and Hart (1967) Nearest neighbor pattern classification. https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf (a01)
- [V] Aha, Kibler, Albert (1991) Instance-based learning algorithms. https://link.springer.com/content/pdf/10.1007/BF00153759.pdf (a02-a04)
- [V] Ontanon (2020) Distance and similarity functions for structured data. https://arxiv.org/abs/2002.07420 (a05)
- [M] Tversky (1977) Features of similarity. https://doi.org/10.1037/0033-295X.84.4.327 (a06)
- [M] Aamodt and Plaza (1994) CBR: foundational issues. https://doi.org/10.3233/AIC-1994-7104 (a07)
- [M] Richter (1995) The knowledge contained in similarity measures; Richter and Weber (2013) Case-Based Reasoning: A Textbook. https://doi.org/10.1007/978-3-642-40167-1 (a08, a09)
- [M] Smyth and Keane (1998) Adaptation-guided retrieval. https://doi.org/10.1016/S0004-3702(98)00017-4 (a10; the 1994/95 tech report below was opened)
- [M] Lenz and Burkhard (1996) Case retrieval nets. https://doi.org/10.1007/3-540-61020-X_85 (a11)
- [M] Gentner and Forbus (1991) MAC/FAC. https://www.qrg.northwestern.edu/papers/Files/MACFAC.pdf (a12)
- [V] Liu et al. (2021) KATE. https://arxiv.org/abs/2101.06804 (a13, a14, b01-b03, c01, c02)
- [V] Rubin, Herzig, Berant (2022) EPR. https://arxiv.org/abs/2112.08633 (a15, a16, b04-b06, c03, c04)
- [V] Ye et al. (2023) CEIL. https://arxiv.org/abs/2302.05698 (a17, b23, c05)
- [V] Su et al. (2022) Selective annotation (vote-k). https://arxiv.org/abs/2209.01975 (a18)
- [V] Li et al. (2023) UDR. https://arxiv.org/abs/2305.04320 (a19)
- [V] Wang, Yang, Wei (2023) LLM-R. https://arxiv.org/abs/2307.07164 (a20)
- [V] Luo et al. (2023) Dr.ICL. https://arxiv.org/abs/2305.14128 (a21; qualitative only)
- [V] Min et al. (2022) Rethinking the role of demonstrations. https://arxiv.org/abs/2202.12837 (a22, b12, c07)
- [V] Yoo et al. (2022) Ground-truth labels matter. https://arxiv.org/abs/2205.12685 (d18; abstract and intro only)
- [V] Lewis et al. (2020) RAG. https://arxiv.org/abs/2005.11401 (a23)
- [V] Das et al. (2021) CBR for queries over knowledge bases. https://arxiv.org/abs/2104.08762 (a24)
- [V] Zhou et al. (2025) Memento. https://arxiv.org/abs/2508.16153 (a25, a26, b22, c09, c10)
- [V] Guo et al. (2026) CASCADE. https://arxiv.org/abs/2605.06702 (a27)
- [M] Huawei group (2025) CBR+Re4 test script generation. https://arxiv.org/abs/2503.20576 (a28; not opened)
- [V] Liu et al. (2023) Lost in the Middle. https://arxiv.org/abs/2307.03172 (a29, b18, b19, c19)
- [M] Wilkerson and Leake, LLM retrieval vs k-NN (as cited in project notes). C08_case_based_reasoning/SUBFIELDS.md (a30, d19; figure unverified)
- [V] Kapuriya et al. (2025) Diversity in example selection. https://arxiv.org/abs/2505.01842 (b07, b08)
- [V] Xiao, Zhao, Huang (2025) The role of diversity in ICL. https://arxiv.org/abs/2505.19426 (b09-b11)
- [V] Sarukkai, Xie, Fatahalian (2025) Self-generated in-context examples. https://arxiv.org/abs/2505.00234 (b13-b15)
- [V] Shi et al. (2023) Distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (b16, b17, c21)
- [V] Thakur et al. (2021) BEIR. https://arxiv.org/abs/2104.08663 (b20)
- [V] Wiratunga et al. (2024) CBR-RAG. https://arxiv.org/abs/2404.04302 (b21, c15, c26, d15)
- [V] Levy, Bogin, Berant (2023) Diverse demonstrations. https://arxiv.org/abs/2212.06800 (c06)
- [V] Agarwal et al. (2024) Many-shot ICL. https://arxiv.org/abs/2404.11018 (c08)
- [V] Ouyang et al. (2025) ReasoningBank. https://arxiv.org/abs/2509.25140 (c11, c12)
- [V] Zhao et al. (2023) ExpeL. https://arxiv.org/abs/2308.10144 (c13)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c14)
- [V] Wang et al. (2024) DS-Agent. https://arxiv.org/abs/2402.17453 (c16)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c17)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (c18)
- [V] Cuconasu et al. (2024) The power of noise. https://arxiv.org/abs/2401.14887 (c20)
- [V] Steck, Ekanadham, Kallus (2024) Is cosine similarity really about similarity? https://arxiv.org/abs/2403.05440 (c22)
- [V] Xiao et al. (2025) BRIGHT. https://arxiv.org/abs/2407.12883 (c23)
- [V] Smyth and Keane (1994/95) Experiments on adaptation-guided retrieval, TCD-CS-94-17. https://publications.scss.tcd.ie/tech-reports/reports.94/ (d01, d02)
- [V] Hatalis et al. (2025) Review of CBR for LLM agents. https://arxiv.org/abs/2504.06943 (d03)
- [V] Yin and Leake (2026) Capturing LLM cases for RAG reuse (PRIM). https://ceur-ws.org/Vol-4255/lake.pdf (d04)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (d05-d07)
- [V] Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511 (d08)
- [V] Jiang et al. (2023) FLARE. https://arxiv.org/abs/2305.06983 (d09)
- [V] Yoran et al. (2024) Robust RALMs to irrelevant context. https://arxiv.org/abs/2310.01558 (d10)
- [V] Jeong et al. (2024) Adaptive-RAG. https://arxiv.org/abs/2403.14403 (d11)
- [V] An et al. (2023) Skill-KNN. https://arxiv.org/abs/2305.14210 (d12)
- [V] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (d13)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/abs/2406.04271 (d14)
- [V] Lu et al. (2022) Fantastically ordered prompts. https://arxiv.org/abs/2104.08786 (d16)
- [V] Peng et al. (2024) Revisiting demonstration selection. https://arxiv.org/abs/2401.12087 (d17)
