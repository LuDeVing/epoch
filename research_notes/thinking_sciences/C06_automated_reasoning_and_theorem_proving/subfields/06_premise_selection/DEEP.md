# Premise selection: deep document

*Subfield C06.06. Sources in this folder: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c28, d01-d17), claims.jsonl (K01-K27), critique.md. Evidence ids in brackets refer to those files. Numbers re-checked against paper text by the critique pass are marked "re-checked".*

## 1. What it is

A premise is a known fact that a prover may use: a lemma, a theorem, a definition. A library holds many of them. Mizar has about 58,000 theorems. Lean's Mathlib has about 100,000 (LeanDojo benchmark: 98,734 theorems). Flyspeck has about 14,000 theorems on top of HOL Light.

Premise selection is the step before proving. Given a goal, pick a small set of library facts to show the prover. The prover then works only with that set.

Why it exists. Provers get slower and weaker as the fact set grows. The whole library cannot be dumped in. The selector decides what the prover can see. A bad selector hides the key lemma. A bad cutoff buries it in noise.

Three framings appear in the literature.

- **Pair ranking.** Score each (goal, fact) pair. The prover gets the top k. This is the classic setting (Alama 2014, DeepMath, Mizar, Flyspeck).
- **Step-wise retrieval.** At each proof state, retrieve facts for the next step (ReProver, Magnushammer, Rango).
- **Global retrieval.** Retrieve the whole set of facts a full proof will need before proving starts (LeanSearch v2, DRIFT).

Measures used. Recall@k (is the needed fact in the top k), MRR, nDCG@10, and the one that counts: how many goals the downstream prover solves. Critique finding: recall numbers differ between papers because the definition of the upper bound differs. Never compare recall across papers (c26).

Why it matters for our agent. Our agent will keep a library of solved subgoals. At each new problem it must choose which stored items to put in front of the model. That is the same task. The evidence says what a good chooser looks like, how many items to show, how to calibrate it, and what to measure.

Honest limit up front. Almost every study here uses a symbolic prover (ATP, hammer) or a fine-tuned retriever on a formal library. Almost none tests a frozen general language model choosing from a library of its own past subgoals. The step to our agent is by analogy. No paper reports equal-token comparisons between retrieval and no retrieval. The frozen-LLM studies we found (section 6) are about text passages, tool lists or code skills, not subgoals.

## 2. History and theories in depth

### 2.1 Rule-based filters (before 2010)

- SInE selects facts by symbol trigger rules. It is the standard filter in Vampire.
- MePo (Meng and Paulson, 2009) is the Isabelle/Sledgehammer filter. It ranks facts by shared symbols with the goal. MaSh (Kuhlwein et al., 2012) is the learned selector in Isabelle. We did not open the originals (a27). We read only their use as baselines.
- Both rule filters are cheap and need no training. All later learned methods are measured against them.

### 2.2 Learning from proofs (2011-2014)

- Alama, Heskes, Kuhlwein, Tsivtsivadze and Urban (arXiv 1108.3446) founded learned premise selection. They mined minimal proof dependencies from Mizar. They trained naive Bayes (SNoW) and a kernel multi-output ranker (MOR). Benchmark MPTP2078: 2,078 problems. Premises per problem: 1,976.5 unpruned, 74 heuristically pruned, 31.5 with precise dependencies (a06).
- Vampire/SInE solved 548. SNoW-70 solved 556 (+1.5%). Another SNoW run solved 722 (+31.8%). MOR-70 solved 795 (+45.1%). Combined runs +44% and +50% (a07, b05). Ideal pruning to true dependencies let Vampire solve 1,105, which is 8% above heuristic pruning (a08). Top-50 recall: MOR 88%, SNoW about 80%.
- Kaliszyk and Urban (2013, MizAR 40 for Mizar 40): learned selection plus many prover strategies proved 40.6% of 58,000 Mizar theorems in 30 s on 14 CPUs, no user advice. Best single method 27.3%. Older whole-library result: 18% (a11).
- MizAR also showed iteration. Retrain the selector on proofs found in the last round. Re-proved theorems rose 48.0%, 51%, 53.4%, 54.6%, 55.3%, 55.6% over six rounds. Gains flatten after round 4 (a12).
- Kaliszyk and Urban (2014, Flyspeck, arXiv 1211.7012). Chronological test: prove each theorem using only earlier ones. 39% of 14,185 theorems in 30 s (re-checked). 50% if true HOL Light dependencies are given. Union of all experiments 56.5% with Isabelle, 54.7% without (a09, b03). Z3 fell from 12.4% at 256 premises to 6.2% at 740 (re-checked; a10 wrote "one prover", b04 fixed it).

### 2.3 Deep learning (2016-2019)

- Irving, Szegedy, Alemi, Een, Chollet and Urban (2016, DeepMath, arXiv 1606.04442) was the first deep premise selector. Character, word and definition-embedding CNNs scored (conjecture, premise) pairs. Pairwise scoring avoids picking a subset directly. Conjecture embeddings can be cached (a05). Corpus: 57,917 Mizar theorems; 32,524 (56.2%) have an E-prover proof used for training; an earlier 14-method portfolio proved 40%, best single method 27.3% (re-checked). The paper's "perfect selection" bound is "at least 56%" instead of 40% (b01).
- The neural gain over a strong k-NN baseline is large at small k and small at large k. Top-16: k-NN 674 of 2,742 (24.6%), def+char-CNN 835 (30.5%). Largest cutoff: 65.1% vs 67.9%. Different selectors solve different theorems, so unions beat any one method (80.9% for all methods).
- Hard-negative mining was called crucial. Add as negatives the non-premises the current model scores high. About 25% of negatives were mined, the rest random. The paper text gives 61.3% to 66.4% (union over cutoffs). One evidence line said mining "doubled" top-16 proofs. The critique could not confirm that and it is not used here.
- HolStep (Kaliszyk, Chollet, Szegedy 2017): 2,013,046 training and 196,030 test examples from 11,400 HOL Light proofs; classify each step as useful or not. Models did not benefit from seeing the conjecture (a13, a14, b07). Only 0.8% of statements appear as both positive and negative, so the test rewards statement-only cues (b07). FormulaNet (Wang et al. 2017) reached 90.3% conditional and 90.0% unconditional (prior best 83%). With zero graph steps it still scored 81.5%, so most signal is constant names. Variable renaming caused a large drop (b08, c05).
- Stateful selection (Piotrowski and Urban 2020, RNN picks premises one at a time): best NMT ATP score 0.40 vs XGBoost 0.31 (c04). XGBoost looked better on similarity to human proofs but worse in real proving. This is the first sign that offline metrics can mislead.
- ATPboost (Piotrowski and Urban 2018): train the selector on feedback from real prover runs. Mizar split 29,271 train / 3,253 test: 58.78% proved vs k-NN 50.81%, a 15.7% relative gain (c06). The earlier deep gain over k-NN was 4.3% relative (c06; matches DeepMath 65.1 vs 67.9).
- Bansal et al. (2020): RL prover with a large premise pool. Zero-human RL with tf-idf exploration of premises 56.3% (64.2% cumulative) vs human-based RL 59.9% (69.1%) vs pure imitation 49.95%. Without tf-idf exploration the zero-human run collapsed to 7.0% (c07).

### 2.4 Language-model era (2022-2026)

- Thor (Jiang et al. 2022): a language model prover calls Sledgehammer as one action. PISA test (3,000 theorems): LM alone 39.0%, Sledgehammer 25.7%, union 48.8%, Thor 57.0% (re-checked). The LM naming premises inside its own step advanced the proof 1.9% of the time, vs 28.2% for steps with no premises (a16, b10).
- Magnushammer (Mikula et al. 2024): contrastive transformer retriever plus reranker. PISA single-step 59.5% vs Sledgehammer 38.3%, BM25 30.6%, TF-IDF 31.8%, OpenAI ada-002 36.1% (re-checked). Inside Thor: 57.0% to 71.0%.
- LeanDojo / ReProver (Yang et al. 2023): dense retriever over accessible premises feeding a ByT5 tactic generator. Introduced the novel_premises split.
- Lean-native tools: Lean random forest (Piotrowski et al. 2023), LeanCopilot (Song et al. 2025), LeanHammer / LeanPremise (Zhu et al. 2026), GNN add-on (Petrovcic 2025), a lightweight contrastive retriever (Tao et al. 2025).
- Natural-language and global retrieval (2025-2026): Lean Finder, LeanSearch v2, DRIFT, RocqStar. These use an LLM to rewrite, decompose or judge before retrieving.
- Outside theorem proving, frozen-LLM agents use the same idea. LEGO-Prover and Voyager keep a growing skill library and retrieve from it (d11, d15). RAG-MCP does it for tool lists (d14).

### 2.5 Competing explanations for why selection works

- **Prover capacity.** Provers choke on large fact sets, so a smaller set helps (Flyspeck premise-count curves). For LLM readers the analogue is distraction (section 5).
- **Label quality.** Cleaner "what was truly needed" labels give better selectors (minimal dependencies, a08; false-negative fix, b13).
- **Complementarity.** Different selectors find different premises, so a union helps (DeepMath, LeanPremise with MePo).
- **Memorisation.** Retrievers partly memorise which premises were used before. Gains shrink on novel premises (c13).
- **Division of labour.** The language model plans and a separate tool picks facts (Thor). The model is bad at naming facts itself.

## 3. Core findings with exact numbers

Status: established = at least two independent sources agree; single = one source; contested = sources disagree. "Re-checked" = verified against paper text in the critique pass.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Learned selector beats rule filter (SInE) | Vampire/SInE 548 solved; MOR-70 795 (+45.1%); best combined +50% | Alama 2014 (a07, b05) | established |
| Perfect premises give a big jump | Flyspeck 39% vs 50% with true dependencies; LeanHammer 33.3 vs 43.0; Mizar 56.2% ATP-provable vs 40% | a09, a23, a01, b27 | established |
| Neural vs k-NN gain is large at tiny k, small at large k | top-16: 24.6 vs 30.5%; largest cutoff 65.1 vs 67.9% (N=2,742) | DeepMath (a02), re-checked | established |
| Union of selectors beats any one | DeepMath all methods 80.9% vs best single 67.9%; LeanPremise + MePo 37.6 vs 33.3 | a03, b17 | established (compute not equal) |
| Too many premises hurts provers | Z3 12.4% (256) vs 6.2% (740); Vampire 18.1 vs 12.9; E over 20% at 512, 15.6% at 2048 | Flyspeck (a10, b04), re-checked | established |
| FormalML: performance falls from M=10 to M=20 candidates | exact table figures not extracted | c24 | single |
| Trained retriever beats BM25 and Sledgehammer | PISA 59.5 vs BM25 30.6 vs Sledgehammer 38.3; LeanDojo R@10 38.4 vs 17.2 | a17, a20, b11, b15 | established |
| General embedder is weak on formal text | ada-002 36.1 vs 59.5 trained (PISA); LeanDojo random split embedders 25-27 R@10 vs 36.7 ReProver | b11, c17 | contested (see next row) |
| General embedders beat ReProver on novel premises | R@10 23.8-24.7 vs 19.48 | Tao 2025 (c17) | single, workshop paper |
| Retrieval helps proving modestly for a trained prover | ReProver 51.2 vs 47.6 no retrieval; novel 26.3 vs 23.2 | LeanDojo (a21, b14) | established |
| Retrieval plus hammer lifts an LLM prover a lot | Thor 39.0 to 57.0; + Magnushammer 71.0 (PISA) | a16, a18 | established |
| LM-named premises rarely advance the proof | 1.9% vs 28.2% of steps | Thor (a16, b10, c09) | single (diagnostic, not controlled) |
| Unseen premises are the weak spot | pass@1 51.2 to 26.3; R@10 38.4 to 27.6; GPT-4 29.0 to 7.4 | LeanDojo (a21, c13) | established |
| Hard negatives matter | DeepMath 61.3 to 66.4; LeanDojo in-file negatives 2.7 R@1, 5.3 R@10; LeanPremise loss mask and extraction 5-13 points recall@32 | a04, a20, b15, b18 | established |
| Pretraining helps when data is scarce | 0.1% data (about 4K samples): 39.2 vs 16.8 without pretraining; full data 56.3 vs 53.0; 920K-param model 40.7 | Magnushammer (a19, b12, c11) | established |
| Structure gives small gains | HolStep 81.5% with zero graph steps vs 90.3%; Lean GNN ablations about 1 point; CSLib structure reranker +0.0175 MRR over BM25, +0.0037 over BM25+symbol (CI -0.0103 to +0.0173) | b08, c05, a25, b22 | established (small) |
| GNN over dependency graph helps retrieval | R@1 17.98 (+33.98% rel.), R@10 50.04 (+26.36%) vs 13.42 / 39.60 | Petrovcic (a25, c16) | single |
| Offline metrics do not always predict proving | XGBoost better on similarity, 0.31 vs 0.40 on ATP success | c04 | established with c26 |
| Label noise | 48.2% (462/958) of proxy links appear in elaborated terms; human-only labels 54.0 vs augmented 56.3 | b22, b13 | single |
| Reasoning-style retrieval beats fixed embedding | group recall@10 46.1% vs 38.0% vs 9.3%; downstream 4/16/20% (n=100) | LeanSearch v2 (a26, b21, c19, c20) | established as retrieval; downstream n small |
| Reasoning rewrite helps outside maths | BRIGHT BM25 14.5 to 27.0 nDCG@10; ReasonIR 24.4 to 29.9; Rank1-7B 27.5 vs 17.5 without chains | d08, d09, d10 | established; tokens uncharged |
| Decompose then retrieve | ConNF BEq+@1 54.84 full; 46.72 no decomposition; 4.47 no retrieval | DRIFT (c23) | single |
| Retrieval gain is small for strong whole-proof models | Lean Finder +0.4 miniF2F (Goedel-SFT); ProofNet DeepSeek-V1.5-RL pass@1 4.3 to 6.5 | c21, d13 | single |
| Iteration keeps adding | MizAR 48 to 55.6% over 6 rounds | a12, c07 | established |
| Full context vs RAG (frozen LLM) | Gemini: LC 49.70, RAG 37.33, Self-Route 46.41 at 38.39% of tokens; GPT-4o: LC 48.67, RAG 32.60, Self-Route 48.89 at 61.40% | Li 2024 (d01) | established as a conflict |
| Retrieval beats full context in one study | Llama3.1-70B: 16K retrieved tokens F1 44.43 vs 117K full 34.26; peak 16K (8B), 32-48K (70B) | OP-RAG (d02) | contested vs d01 |
| Near-miss distractors hurt readers | Llama2 NQ: gold only 0.5642; 1 distractor 0.4586; 4: 0.2745; 18: 0.2348; up to -25% for one, -67% for many | Power of Noise (d03) | established (old models) |
| Stronger retriever can lower end accuracy at large k | e5 negatives hurt more than BM25 or random; Gemini-1.5-Pro robust to random, not hard negatives | Jin 2024 (d06) | established |
| Position and amount matter | GPT-3.5 closed-book 56.1, oracle 88.3; gold in the middle drops over 20%; at 20-30 documents worst case is below closed-book | Lost in the Middle (d05) | established (2023 models) |
| Irrelevant items break reasoning | of problems solved by the baseline, at most 18% stay solved under every distractor type | GSM-IC (d04) | single |
| Distractors in logic stories | GPT-4o hard: 50.0 with distractors shuffled vs 62.4 clean ordered | ProverQA (b24) | single |
| Tool list crossover | RAG-MCP: retrieval 43.13% vs all-in-prompt 13.62% vs keyword filter 18.20%; success above 90% under 30 tools, mostly failing past about 100 | d14 | single preprint |
| Growing library helps a frozen LLM | LEGO-Prover 50.4 vs 47.1 (50 attempts, miniF2F-valid); Voyager 18-21 vs 26-36 iterations | d11, d15 | established (weak stats) |
| Proof-state keyed retrieval of earlier solved goals | Rango: proof retriever +47%, lemma retriever +3%; BM25 +46% over CodeBERT dense | d12 | single |
| Plain-language gloss triples recall@1 on state text | Lean Finder 24.6 vs 8.3 | d13 | single, self-reported |
| Oracle gap in QA | BRIGHT with Claude-3.5-Sonnet: none 77.7, best retriever 79.6, oracle 81.8 (46% of gap) | d08 | established (non-formal) |
| Positive-aware negatives | NV-Retriever TopK-PercPos 0.5856 vs naive top-k 0.5407 vs random 0.5248 | d16 | single |
| Selection is rarely the main failure in a full hammer | 33.1% succeeded, 43.6% translated but not proven, 21.7% not translated (one setting) | LeanHammer (b19) | single |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it.

### 4.1 Symbol-overlap filter (SInE, MePo style)

1. Index every library item by its set of symbols (constants, operators, names).
2. Take the goal's symbols. Score each item by shared symbols, weighted by how rare each symbol is in the library.
3. Take items above a threshold. Add the symbols of selected items to the pool and repeat for a few rounds (MePo does this).
4. Cost: near zero. No training. Use it as the baseline and as a union partner.

### 4.2 Lexical retrieval over text (BM25, TF-IDF)

1. Tokenize goal text and item text. Score with BM25.
2. For proof states, BM25 over the state text beat CodeBERT dense retrieval by 46% (Rango, d12). With reasoning-step queries BM25 scored 27.0 on BRIGHT, above many dense models on raw queries (d08).
3. It is weak on formal premise tasks without help: PISA 30.6 vs 59.5 trained; LeanDojo R@10 17.2 vs 38.4.
4. Fix for our case: store a short plain-language gloss with each item, and rewrite the query before lookup.

### 4.3 Feature-based learned rankers (k-NN, random forest, boosted trees)

1. Features: names in the statement, bigrams of names. Trigrams overfit (c14).
2. k-NN: find the most similar earlier goals and take the premises their proofs used. Random forest matched or beat k-NN (Cover 0.57 vs 0.52 on the easy filter, 0.29 vs 0.25 source filter) at 0.28 s vs 5.65 s per theorem (c14).
3. Train online as the library grows. Cheap enough to retrain each batch.
4. Set the target carefully. The "all" filter counts trivial rfl-type lemmas and inflates scores. On real proof-state data (91,292 examples, 1.57 premises each) Cover is only 0.09 (a15).

### 4.4 Pairwise neural scorer (DeepMath)

1. Encode the goal and each premise with a CNN over characters, words or definition-expanded text.
2. Concatenate the embeddings, pass through a small network, output a relevance score.
3. Cache premise embeddings. Compute the goal embedding once. Query time is scoring only.
4. Train on pairs from proofs. Mine hard negatives: every few epochs, score non-premises and add the top ones (about 25% of negatives; the rest random).
5. Rank, take top k, run the prover. Pick k to fit the consumer (section 5).

### 4.5 Contrastive dense retriever plus reranker (Magnushammer, ReProver)

1. Two stages. SELECT: an embedding model scores all candidates by dot product (fast). RERANK: a cross-encoder rescores the top few hundred (adds about 2 points; select-only 54.2% vs 56.3% with rerank, b12).
2. Training pairs: (state, premises used by the real proof). In-batch negatives plus hard negatives. ReProver adds in-file premises as hard negatives (worth +2.7 R@1, +5.3 R@10, b15).
3. Restrict candidates to what is legal in the current context. ReProver cut candidates from 128K to 33K and gained about 1.8 R@1 (13.5 vs 11.7) (a22, b15).
4. Pretraining helps most with little data. About 4K samples were enough to beat Sledgehammer, and a 920K-parameter model reached 40.7% (b12).
5. False negatives: premises that were not used in the human proof but would work. Add alternative proofs found by a tool (human-only 54.0 vs augmented 56.3, b13).

### 4.6 Stateful selection and ATP feedback

1. Stateful (c04): an RNN emits premises one at a time, conditioning on those chosen. This reduces redundancy.
2. ATPboost (c06): after each round, run the prover on the top-k, label premises of successful proofs as positive and others as negative, retrain. This ties the ranker to real success. Cost: many prover runs.
3. Bansal RL (c07): mix in premises picked by tf-idf during exploration, or the policy never finds useful ones (7.0% vs 56.3%).

### 4.7 Hammer coupling (Thor, LeanHammer)

1. The language model proposes steps. When a step needs library facts, it emits a "call hammer" action.
2. The hammer's selector picks premises, an external prover tries, and the result is checked.
3. Thor got 57.0% vs 39.0% (LM alone) by this split. A variant where the LM learns to call the hammer by keywords scored 55.4% (-1.6). Each 1000 problems cost about 50 TPU hours.
4. LeanHammer: selector (LeanPremise, 82M parameters), translation to external provers, reconstruction. The selector sees the live context, including user-local lemmas.

### 4.8 Global retrieval with reasoning (LeanSearch v2, DRIFT)

1. An LLM writes a proof sketch or splits the goal into sub-queries.
2. Retrieve for each sub-query. Rerank with an LLM judge. Reflect: if gaps remain, rewrite and retrieve again (up to 3 revisions; 46 of 69 sketches accepted, 33.3% failed, c19).
3. DRIFT adds "illustrate": show usage examples of retrieved premises. Removing "illustrate" cost 18.9 BEq+@1 points (54.84 to 35.90); removing decomposition 8.1 points (c23).
4. Cost: several LLM calls per query. No paper charges these tokens to a budget.

### 4.9 Frozen-LLM library agent (LEGO-Prover, Voyager)

1. After each solved subgoal or skill, verify it and add it to a vector store.
2. At a new task, the LLM writes a short request; embed it; take the top 5. Voyager recall at 5 was 96.5%, top-1 80.2% (d15).
3. Show the retrieved items in the prompt. The model reuses them directly or writes a new item by imitation (LEGO-Prover: of 135 solved problems, 24% used retrieved skills; 51% of those reused directly, 49% imitated, d11).
4. The library grows during the run. The gain widens as the library fills.

### 4.10 Cheap router for context size (Self-Route)

1. Retrieve top-k chunks. Ask the model to answer or say "unanswerable".
2. If it answers, stop. Otherwise give it the full context.
3. Result: close to full-context accuracy at 38-61% of tokens. k=5 cheapest on average (d01).

### 4.11 Negative selection rule (NV-Retriever)

1. Score all non-positives with a teacher.
2. Drop those scoring above 95% of the positive score (likely unlabeled positives).
3. Keep the rest of the top ranks as hard negatives. Skip the very top few ranks.
4. Gain: 0.5856 vs 0.5407 (naive top-k) NDCG@10 (d16).

## 5. What holds up

### 5.1 Replications and cross-checks

- Same ordering in several settings: lexical < general embedding < task-trained retriever (PISA, LeanDojo, Rango, BRIGHT, Lean Finder). The order is consistent; the size of the gap is not (b16).
- DeepMath, Magnushammer, LeanDojo, Thor and Flyspeck headline numbers were all re-checked against paper text by the critique pass. They match.
- "More premises hurts" appears in provers (Flyspeck, three provers), small LLMs (FormalML M=10 to 20) and QA readers (Power of Noise, Lost in the Middle, Jin). It is the most replicated result here.
- Complementarity is replicated: DeepMath unions (80.9%), LeanPremise plus MePo (37.6 vs 33.3 cumulative), and LeanSearch v2 versus the baselines.
- Iteration with a growing library helps in provers (MizAR) and frozen LLMs (LEGO-Prover, Voyager).

### 5.2 Failures, nulls and weak results

- Conjecture conditioning on HolStep did not help (Siamese 0.71 to 0.83 vs unconditioned 0.71 to 0.83). Graph model: conditional 90.3 vs unconditional 90.0 (b07, b08). Premise-conditioned scoring adds little there.
- Structure: CSLibPremiseBench (Ji 2026) found a graph-lexical reranker +0.0175 MRR over BM25, with the 95% CI [+0.0016, +0.0335]. Against BM25+symbol the gain is +0.0037 with CI spanning zero. This is the closest thing to a failed replication of the "structure helps" idea. The GNN paper (Petrovcic) reports +34% relative R@1, but its own ablations move R@10 by only about 1 point.
- Small downstream retrieval gains for strong provers: Lean Finder +0.4 (miniF2F, Goedel-SFT) and +2.2 (ProofNet pass@1 for DeepSeek-V1.5-RL; 4.3 to 6.5); PutnamBench inconsistent (c21).
- HybridProver and DRIFT miniF2F (seen as snippets, b25, b26): on miniF2F most theorems need no external premises, so extra retrieved context mostly distracts. DRIFT gives 0.43 library dependencies per miniF2F item. The snippets are unverified; DRIFT's own opened text confirms miniF2F gains were smallest (+2.08 F1) (c23).
- Z3 premise-count collapse is a limit of the 2014 prover, not a failed replication.
- ReProver retrieval adds only 3.6 and 3.1 points of pass@1 over no retrieval, though its R@10 is more than double BM25's.
- XGBoost: better on similarity metrics, worse on ATP success (c04).
- No independent reproduction of LeanSearch v2, LeanPremise or Lean Finder headline numbers was found. All three are 2026 self-reports on the authors' own benchmarks (critique gap 6).

### 5.3 Contradictions to keep in view

- Retrieval value: +3.6 and +3.1 (ReProver), +0.4 to +2.2 (Lean Finder) vs +14 (Magnushammer in Thor) and +16 (LeanSearch v2, n=100). The gain depends on whether retrieval is paired with a hammer or a reasoning step.
- Full context vs retrieval for frozen LLMs: Self-Route says full context wins (49.70 vs 37.33), OP-RAG says a retrieved 16K beats 117K (44.43 vs 34.26). The review (d17) explains the conflict: full context wins when needed facts sit together; retrieval wins when facts are scattered and short. A subgoal library is the scattered case.
- Embedders: ada-002 loses to trained retrievers on PISA yet beats ReProver on novel premises (c17). "General embedders are weak" is contested.
- Retrieval recall for ReProver differs by paper: 13.5 / 38.4 (LeanDojo), 13.42 / 39.60 (Petrovcic), 11.79 / 36.69 (Tao). Do not compare across papers.
- Cumulative proof-rate numbers for LeanPremise differ across agent readings (34.5 vs 37.3). Safe numbers: 33.3 (single 82M, cumulative) and 43.0 (oracle).

### 5.4 Moderators

- **Cutoff k.** Neural gain large at k=16, small at k=1024 (a02). For LLM readers the peak is lower (5.5).
- **Library familiarity.** Gains drop on novel items (c13). Rango retrieval of earlier proofs cut the penalty from not having project files in training: gain from project files in the weights was 15% and 11% with proof retrieval vs 26% and 43% without (d12).
- **Easy problems.** iProver solves 86% of one subset with no selection (c08). miniF2F items need few premises. Selection gains are bounded there.
- **Label definition.** What counts as a premise changes scores about 2x (a15).
- **Reader strength.** Strong whole-proof models gain little. Weak or older models gain more.
- **Query form.** Raw proof state is hard (R@1 8.3). Natural-language statement is easier (64.2). State plus gloss: 24.6 (d13).

### 5.5 Interventions that worked

- Hard-negative mining (DeepMath, LeanDojo, LeanPremise).
- Union of lexical and learned selectors.
- Restricting to accessible premises (ReProver).
- Handing premise choice to a tool (Thor).
- Pretraining on little data (Magnushammer).
- Reasoning query rewrite (BRIGHT, ReasonIR, LeanSearch v2).
- Re-training on own successes (MizAR rounds).
- Retrieval of earlier solved goals keyed by current state (Rango).
- Stored library growing during the run (LEGO-Prover, Voyager).
- Robustness: NLI filter, fine-tuning on mixed relevant and irrelevant context with about 1,000 examples (Yoran, d07). Fine-tuning does not apply to us; the filter idea might.

### 5.6 Interventions that did not work, or did little

- Conditioning the scorer on the conjecture (HolStep).
- Trigram features (overfit, c14).
- Heavier structure on a clean library (CSLib).
- Easy synthetic queries (ReasonIR, added nothing) and budget forcing for rerankers (Rank1, no help).
- Reordering retrieved items helps only at large counts (Jin, d06).
- Combining two selection strategies inside Vampire (b05, "not productive").
- LM naming premises inside its own step (1.9% vs 28.2%).
- Parametric recall of library names by the LLM itself: lost 40-55 points on ConNF in DRIFT (c23).

## 6. Language models

### 6.1 Frozen LLM as chooser of facts

- The language model is poor at naming library facts itself. In Thor, steps naming premises advanced the proof 1.9% of the time vs 28.2% for steps without (a16). Parametric retrieval in DRIFT lost 40-55 points on the ConNF library.
- GPT-4 zero-shot on LeanDojo: 29.0% pass@1 vs ReProver 51.2%; on novel premises 7.4% vs 26.3% (a21). GPT-4 may have seen the data. It still lost.
- With the retrieval tool done outside the model, the whole agent improves a lot. Thor: 39.0 to 57.0. With a better retriever (Magnushammer): 57.0 to 71.0, with no larger model.
- LeanSearch v2 used Claude Sonnet 4.5 as a frozen prover for 8 rounds. FATE-H (n=100): no retrieval 4, Lean Finder 12, INF-X 7, v2 standard 16, v2 reasoning 20. MathlibMPR-Prop (n=50): 2 / 5 / 5 / 5 / 7 solved. One problem is 1 to 2 points. No confidence intervals (b21, c20).

### 6.2 Frozen LLM with a growing library

- LEGO-Prover (frozen ChatGPT/GPT-4, Isabelle): miniF2F-valid 57.0% and test 50.0% with 100 attempts. At 50 attempts on valid: 50.4% with library vs 47.1% without. The gap starts near zero and widens as the library fills. About 300 USD per 100-attempt experiment. Single run, handful of problems out of 244 (d11).
- Voyager (frozen GPT-4, Minecraft): retrieval recall top-1 80.2 +/- 3.0, top-5 96.5 +/- 0.3 over 309 samples. Zero-shot unseen tasks need 18-21 iterations with the library and 26-36 without. Three trials per task (d15).
- RAG-MCP (frozen qwen-max): 43.13% with retrieval vs 13.62% with all tool descriptions in the prompt (d14).

### 6.3 Frozen LLM as reader of retrieved items

- Distractors. Power of Noise (Llama2, MPT, Phi-2, Falcon): one hard distractor costs up to 25%; many up to 67% (d03). These are small, old models.
- Lost in the Middle (2023 models): gold document in the middle drops accuracy by more than 20%; at 20-30 documents the worst case is below closed-book (d05).
- Jin et al. (2024, Gemini-1.5-Pro among the models): with a strong retriever, accuracy rises then falls with k; hard negatives are the cause (d06).
- GSM-IC: at most 18% of problems stay solved under every distractor type (GPT-3 era, d04).
- ProverQA (GPT-4o): hard problems drop from 62.4 (no distractors, ordered) to 50.0 (distractors, shuffled) (b24).
- Newer models are more robust, but the effect persists. Frontier-model size of effect is not measured here.

### 6.4 Full context versus retrieval (frozen LLM)

- Self-Route (9 datasets): Gemini LC 49.70, RAG 37.33, Self-Route 46.41 using 38.39% of tokens. GPT-4o LC 48.67, RAG 32.60, Self-Route 48.89 using 61.40%. GPT-3.5-Turbo LC 32.07, RAG 30.33, Self-Route 35.32. RAG and LC give the same answer on 63% of queries (d01).
- OP-RAG (Llama3.1-70B): full context 117K tokens F1 34.26 vs 16K retrieved 44.43, 24K 45.45, 48K 47.25. Peak at 16K (8B) and 32-48K (70B). Keeping retrieved chunks in document order beat score order (d02).
- Review over 12 datasets after filtering: LC correct on 56.3% of questions, RAG 49.0%. LC alone correct on more than 2,000, RAG alone on about 1,300 (d17).
- Corpora are long documents, not libraries of short items.

### 6.5 Reasoning retrievers

- BRIGHT: best retriever 24.3 nDCG@10; a top MTEB model scored 59.0 on BEIR but 18.3 on BRIGHT. BM25 14.5 on original queries vs 27.0 with GPT-4 reasoning-step queries (Claude-written 26.8) (d08).
- ReasonIR: 24.4 original, 29.9 with GPT-4 rewritten queries, 36.9 with an LLM reranker. Over 200x less test-time compute than Rank1-32B by the authors' FLOPs estimate (d09).
- Rank1-7B 27.5 vs 17.5 trained without chains vs 13.9 RankLLaMA-7B. Chains under 1,000 tokens each. Reranking 100 candidates could cost up to 100K output tokens (d10).
- End-to-end QA with Claude-3.5-Sonnet: no retrieval 77.7, BM25 78.3, SBERT 79.0, Qwen embedding 79.6, oracle 81.8. The best retriever closed 46% of the oracle gap (d08).
- Rewriting tokens are not charged to any budget in these papers.

### 6.6 What changed results, by how much (summary)

| Change | Size of change | Source |
|---|---|---|
| Rule filter to learned selector | +45% solved (Mizar, 2014 prover) | a07 |
| Lexical to trained retriever | +21 to +29 points (PISA 38.3/30.6 to 59.5) | a17 |
| Hammer coupling | +18 points (39.0 to 57.0) | a16 |
| Better retriever in same agent | +14 points (57.0 to 71.0) | a18 |
| Retrieval inside ReProver | +3.6 / +3.1 points | a21 |
| Growing library, frozen LLM | +3.3 points | d11 |
| Reasoning mode retrieval, frozen prover | +4 points over the next retriever, +16 over none (n=100) | b21 |
| All tools in prompt to retrieval of one | 13.62% to 43.13% | d14 |
| Hard distractor present | up to -25% | d03 |

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA section 5 (planned subgoal library). Status: [E] established, [S] single-source, [C] contested. Honest note: even [E] items are established on provers or text readers, not on a frozen LLM choosing subgoals. Anything that adds cost still needs the equal-token test in section 8 before going into the schema (G7).

### Add now (established)

1. **Retrieve a small top-k from the subgoal library by goal match. Do not paste the whole library.** Schema: memory, S3. [E] K01, K20, K24. Evidence a07, b05, a02, a17, d11, d14, d15, d01. Note: d01 says full context wins on accuracy when it fits; this rule applies once the library no longer fits or is scattered.
2. **Cap the number of retrieved items. Start at 3 to 10. Do not exceed about 20 without a test.** Schema: memory. [E] K02, K23. Evidence a10, b04, c24, d02, d05, d06. The peak is model-dependent and lower for LLM readers than for provers.
3. **Merge two views, a lexical match and an embedding match, into one list of fixed size.** Schema: O/memory. [E] K03. Evidence a03, b02, c02, a23, b17. Note: evidence unions use more compute than a single run; we test at equal item count.
4. **Score the selector by solve rate, not by retrieval recall.** Schema: G7 (equal tokens), memory. [E] K13. Evidence c04, c26, a01, b13.
5. **Never pad the prompt with near-miss items.** Similar but unhelpful items hurt much more than random ones. Place the best match first or last. Schema: G/memory. [E] K22, K23. Evidence d03, d06, d04, d07, d05.
6. **Measure the oracle gap before building more retrieval.** Inject the ground-truth needed subgoals and compare with own retrieval. If the gap is under about 3 points, stop. Schema: memory. [E] K04, K26. Evidence a09, b03, a23, b27, a01, d08, d05.
7. **Test retrieval on held-out library items the agent has not used before, separately from seen ones.** Schema: memory. [E] K08. Evidence a21, c13, b15, d11, d12.
8. **Put each newly solved and verified subgoal back into the library, and re-measure.** Schema: memory, S9. [E] K18, K24. Evidence a12, c07, d11, d15, d12.
9. **When calibrating any scorer on the library, include near-miss negatives.** Skip negatives that score above about 95% of the true match. Schema: memory. [E] K10 (negatives matter); the 95% rule is [S] K27 (d16). Evidence a04, b02, a20, b15, b18, d16.
10. **Log what each solved subgoal actually used (usage labels).** Cheap; no behaviour change. Label quality bounds retrieval quality. Schema: S9, memory. [S] K14. Evidence a08, b13, b22.

### Test first

| Item | Schema | Status | Evidence | Why test |
|---|---|---|---|---|
| Retrieval vs no library vs whole library, frozen LLM, equal tokens | memory | [S] analogy | K07, K20, K21, d01, d02 | No direct test. Core question. |
| Query rewrite (LLM writes reasoning steps) before lookup | O/S | [E] gain, [C] net of cost | K15, d08, d09, d10 | Gains documented; tokens not charged. |
| Two-step lookup: top-5 first, widen only if the agent says it cannot answer | O/memory | [E] on documents | K20, d01 | Not tested on subgoals. |
| Library size where no-retrieval falls behind | memory | [S] | K21, d14, d15 | One short preprint. |
| Gloss per stored subgoal plus BM25 | memory | [S] | K25, d12, d13 | Self-reported, different task. |
| Key by goal state, return earlier solved goals with solutions | memory | [S] | K25, d12 | One system. |
| Decompose goal, retrieve per sub-goal | S/O3 | [S] | K16, c23 | One benchmark. |
| Off-the-shelf embedder vs tuned scorer, split seen/unseen | memory | [C] | K06, b11, c17 | Contested. |
| Retrieval as a tool/operator vs model naming items itself | O | [S] | K09, a16, b10, c09 | Diagnostic only. |
| Structure (dependency links) vs plain symbol overlap | memory | [E] small | K12, a25, b22 | Small gains, noisy. |
| Entailment filter on retrieved items | G/memory | [S] | d07 | Trade-off with recall. |
| Strong base agent may not need retrieval on easy items | S0 | [S] | K17, K19, c21, c08 | Skip retrieval when plain pass rate is high. |

## 8. Concrete tests on our bench

Common setup. Build a subgoal library from earlier runs on the bench (solved, verified subgoals with a short gloss). Split items into families so some test items have no close library match. Both arms get the same total token budget per item, including retrieval, rewrite, router and filter tokens. Report solve rate with a confidence interval, and tokens used. Use at least 100 items per test; below that, one item is a full point (the LeanSearch tests had n=100 and 50).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Retrieve vs none vs whole library | items with a library built on other items of the same class | no library; top-k retrieved; whole library truncated to budget | solve rate with CI | top-k beats none by 3+ points, beats whole library by 2+ points (guess; ReProver gives +3.6, LEGO +3.3) |
| T2 k sweep | same | k = 0, 4, 8, 16, 32, 64 with one selector | solve rate by k | interior peak; k=64 below peak |
| T3 Lexical + embedding union | same | BM25 only; embedding only; merged list at same item count | solve rate; recall of the used items | union beats both by 1 to 3 points |
| T4 Oracle gap | items with known needed subgoals | own retrieval; ground-truth items injected | solve rate gap | gap of 3 to 10 points (Flyspeck 11, LeanHammer 9.7, BRIGHT 4.1) |
| T5 Query rewrite | same | direct lookup; one rewrite call then lookup, rewrite tokens counted | solve rate per token | gain survives only if rewrite is under about 300 tokens |
| T6 Two-step fallback | same | full library in context; top-5 only; top-5 then widen if "cannot answer" | solve rate; tokens | fallback within 1 point of full context at 40-60% of tokens (Self-Route) |
| T7 Library size crossover | libraries of 10, 30, 100, 300 items | whole library in prompt vs top-k | solve rate by size | whole-library arm falls behind past 30 to 100 items (RAG-MCP) |
| T8 Seen vs novel items | items whose needed subgoal was never used before vs used before | same retriever | retrieval hit rate and solve rate | novel hit rate roughly 25% lower (R@10 38.4 to 27.6) |
| T9 Gloss + BM25 vs embedding | state-like queries | raw text BM25; embedding; BM25 over text + gloss | recall@1, solve rate | gloss arm several times better at rank 1 than raw (24.6 vs 8.3); may equal embedding |
| T10 Near-miss harm and filter | items with k near-miss distractors added | no distractors; distractors; distractors with entailment filter | solve rate; recall lost | distractors cost points; filter recovers more than it loses |
| T11 Empty vs prefilled library | stream of items in order | empty library growing; prefilled frozen library; none | solve rate vs items seen | growing arm gap widens with items stored |
| T12 Best-match position | k=8 prompts | best match first; middle; last | solve rate | middle worst; first or last better |

## 9. What does not transfer, and why

- **Prover capacity curves.** Z3 and Vampire peak near 256 premises. An LLM reader degrades at much smaller counts, and our subgoals are short text, not clauses. Do not copy the 256 figure.
- **Fine-tuned retrievers.** Magnushammer, ReProver, LeanPremise, Lean Finder need training data and GPU hours (ReProver about 120 GPU hours). We do not train. Only the design lessons (hard negatives, accessible set) transfer.
- **Hammer coupling.** Thor's gain comes from an external prover that can try hundreds of fact sets. Our bench has no such symbolic engine for ARC or puzzles. The division of labour (model plans, code selects, G5) transfers; the numbers do not.
- **Formal exactness.** In Lean a premise either type-checks or not. A stored subgoal is a looser object. Recall of "the needed fact" is not as crisp as here.
- **Recall metrics across papers.** Definitions differ (c26).
- **Benchmark leakage and label noise.** Mathlib premises were seen in pretraining; CSLib has 48.2% of proxy links elaborated. Numbers are optimistic.
- **Document-QA results.** Self-Route, OP-RAG, Power of Noise and Lost in the Middle use long text or Wikipedia passages, not libraries of short items. The direction transfers; the exact k does not.
- **Old and small models.** Power of Noise (Llama2 era) and GSM-IC (GPT-3 era) exaggerate distractor harm for current frontier models.
- **Reasoning-retriever gain.** BRIGHT and LeanSearch v2 do not charge reasoning tokens. Under G7 this may erase the gain.
- **Task mix.** Many bench items (ARC grids, puzzles) have no named lemmas. What is retrieved may be rule fragments or helper programs. Whether the gloss-and-lexical findings carry over there is open.

## 10. Open questions

1. Does library retrieval help a frozen LLM at equal total tokens over putting a small library fully in context? Where is the crossover? (Partly closed by RAG-MCP and Self-Route; not for subgoals.)
2. What is the best number of items for an LLM reader, in items not tokens? Start at 3 to 10.
3. How much of the reasoning-retriever gain remains after charging reasoning tokens? Still open.
4. Which retriever degrades least on items added during the run?
5. Goal-state keyed retrieval vs problem-statement retrieval on the same agent. Rango and Lean Finder point to different things.
6. Independent reproduction of LeanSearch v2 (n=100), LeanPremise and Lean Finder headline numbers.
7. Oracle gap for our agent. BRIGHT gives 4.1 points; Flyspeck 11; LeanHammer 9.7.
8. Is symbol overlap or BM25 enough when items are in natural language? CSLib suggests structure adds little; Lean Finder suggests a trained dense model wins by a lot.
9. How many examples are needed to calibrate a selector on a small library? Magnushammer: about 4K with pretraining.
10. Do current frontier models show the distractor harm seen in 2023-2024 models?
11. Do usage labels (what a solved subgoal really used) improve retrieval enough to justify logging them?

## 11. Sources

[V] opened and read (by the research agents or in the critique pass); [M] snippet only.

- [V] Irving, Szegedy, Alemi, Een, Chollet, Urban (2016) DeepMath. https://arxiv.org/abs/1606.04442 (a01-a05, b01, b02, c01, c02)
- [V] Alama, Heskes, Kuhlwein, Tsivtsivadze, Urban (2014) Premise selection for mathematics by corpus analysis and kernel methods. https://arxiv.org/abs/1108.3446 (a06-a08, b05, b06, c03; c03 abstract and intro only)
- [V] Kaliszyk and Urban (2014) Learning-assisted automated reasoning with Flyspeck. https://arxiv.org/abs/1211.7012 (a09, a10, b03, b04)
- [V] Kaliszyk and Urban (2013) MizAR 40 for Mizar 40. https://arxiv.org/abs/1310.2805 (a11, a12)
- [V] Kaliszyk, Chollet, Szegedy (2017) HolStep. https://arxiv.org/abs/1703.00426 (a13, a14, b07)
- [V] Wang, Tang, Wang, Deng (2017) Premise selection for theorem proving by deep graph embedding. https://arxiv.org/abs/1709.09994 (b08, c05)
- [V] Piotrowski and Urban (2020) Stateful premise selection by recurrent neural networks. https://arxiv.org/abs/2004.08212 (c04)
- [V] Piotrowski and Urban (2018) ATPboost. https://arxiv.org/abs/1802.03375 (c06)
- [V] Bansal, Szegedy, Rabe, Loos, Toman (2020) Learning to reason in large theories without imitation. https://arxiv.org/abs/1905.10501 (c07)
- [V] Holden and Korovin (2023) Graph sequence learning for premise selection. https://arxiv.org/abs/2303.15642 (c08)
- [V] Piotrowski, Fernandez Mir, Ayers (2023) Machine-learned premise selection for Lean. https://arxiv.org/abs/2304.00994 (a15, b09, c14)
- [V] Jiang et al. (2022) Thor. https://arxiv.org/abs/2205.10893 (a16, b10, c09)
- [V] Mikula et al. (2024) Magnushammer. https://arxiv.org/abs/2303.04488 (a17-a19, b11-b13, b16, c10, c11)
- [V] Yang et al. (2023) LeanDojo. https://arxiv.org/abs/2306.15626 (a20-a22, b14, b15, c12, c13)
- [V] Zhu, Clune, Avigad, Jiang, Welleck (2026) Premise selection for a Lean hammer. https://arxiv.org/abs/2506.07477 (a23, a24, b17-b19, c15, c26)
- [V] Petrovcic et al. (2025) Combining textual and structural information for premise selection in Lean. https://arxiv.org/abs/2510.23637 (a25, b20, c16)
- [V] Gao et al. (2026) LeanSearch v2. https://arxiv.org/abs/2605.13137 (a26, b21, c19, c20; not re-opened in the critique pass)
- [V] Ji (2026) CSLibPremiseBench. https://arxiv.org/abs/2605.14549 (b22, c25)
- [V] Song, Yang, Anandkumar (2025) Lean Copilot. https://arxiv.org/abs/2404.12534 (b23)
- [V] Dai et al. (2025) ProverQA. https://arxiv.org/abs/2502.06563 (b24)
- [V] Tao et al. (2025) Learning an effective premise retrieval model for Lean. https://arxiv.org/abs/2501.13959 (c17)
- [V] Ju and Dong (2025) MIRB. https://arxiv.org/abs/2505.15585 (c18; dataset statistics only)
- [V] Kozyrev et al. (2026) RocqStar. https://arxiv.org/abs/2505.22846 (c22)
- [V] Zhang et al. (2026) DRIFT. https://arxiv.org/abs/2510.10815 (c23; b25 was a snippet)
- [V] Yang et al. (2025) FormalML. https://arxiv.org/abs/2510.02335 (c24)
- [V] Li et al. (2024) A survey on deep learning for theorem proving. https://arxiv.org/abs/2404.09939 (c27)
- [V] Li et al. (2024) Retrieval augmented generation or long-context LLMs? https://arxiv.org/abs/2407.16833 (d01)
- [V] Yu, Xu, Akkiraju (2024) In defense of RAG in the era of long-context language models. https://arxiv.org/abs/2409.01666 (d02)
- [V] Cuconasu et al. (2024) The power of noise. https://arxiv.org/abs/2401.14887 (d03)
- [V] Shi et al. (2023) Large language models can be easily distracted by irrelevant context. https://arxiv.org/abs/2302.00093 (d04)
- [V] Liu et al. (2023) Lost in the middle. https://arxiv.org/abs/2307.03172 (d05)
- [V] Jin, Yoon, Han, Arik (2024) Long-context LLMs meet RAG. https://arxiv.org/abs/2410.05983 (d06)
- [V] Yoran, Wolfson, Ram, Berant (2023) Making retrieval-augmented language models robust to irrelevant context. https://arxiv.org/abs/2310.01558 (d07)
- [V] Su et al. (2024) BRIGHT. https://arxiv.org/abs/2407.12883 (d08)
- [V] Shao et al. (2025) ReasonIR. https://arxiv.org/abs/2504.20595 (d09)
- [V] Weller et al. (2025) Rank1. https://arxiv.org/abs/2502.18418 (d10)
- [V] Wang et al. (2023) LEGO-Prover. https://arxiv.org/abs/2310.00656 (d11)
- [V] Thompson et al. (2025) Rango. https://arxiv.org/abs/2412.14063 (d12)
- [V] Lu et al. (2026) Lean Finder. https://arxiv.org/abs/2510.15940 (c21, d13)
- [V] Gan and Sun (2025) RAG-MCP. https://arxiv.org/abs/2505.03275 (d14)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (d15)
- [V] Moreira et al. (2024) NV-Retriever. https://arxiv.org/abs/2407.15831 (d16)
- [V] Li, Cao, Ma, Sun (2024) Long context vs. RAG for LLMs. https://arxiv.org/abs/2501.01880 (d17)
- [M] Meng and Paulson (2009) MePo; Kuhlwein et al. (2012) MaSh. https://www.cl.cam.ac.uk/~lp15/papers/Automation/ (a27, baselines only)
- [M] HybridProver (2025). https://arxiv.org/abs/2505.15740 (b26, snippet)
- [M] Natural language premise selection: finding supporting statements. https://arxiv.org/abs/2004.14959 (c28, seen in search only)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 18 established claims: 13 confirmed as written, 5 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C06.06-K08** (now single-source: the sources are not independent). All three supporting lines (a21, c13, b15) are the same LeanDojo paper; the numbers (51.2 to 26.3, R@10 38.4 to 27.6, GPT-4 29.0 to 7.4) are correct but rest on one source; LEGO-Prover and Rango listed here say nothing about unseen premises.
- **C06.06-K10** (number corrected). The LeanPremise ablation is mislabelled: on Mathlib-valid (medium baseline recall@32 71.9) naive data extraction costs 5.1 points (66.8), removing negatives costs 12.4 (59.5), and removing the loss mask costs only 2.3 (69.6). Corrected claim: Negative mining and hard negatives matter: DeepMath mining raised proved theorems 61.3 to 66.4 percent (union over cutoffs); LeanDojo in-file negatives are worth 2.7 R@1 and 5.3 R@10; in LeanPremise, removing sampled negatives costs 12.4 points recall@32 (71.9 to 59.5), naive data extraction costs 5.1 (to 66.8), and removing the loss mask costs 2.3 (to 69.6).
- **C06.06-K12** (reworded: the sources support less). Headline 'small, noisy gains' ignores that the same sources report large gains from structure (FormulaNet 83 to 90.3 percent; Lean GNN R@10 39.6 to 50.0, R@1 +34 percent relative); only single-graph ablations move R@10 by about 1 point, and those ablated runs scored higher than the no-ablation run. Corrected claim: Structure gives uneven gains, and names carry much of the signal: on HolStep names alone give 81.5% at zero graph steps vs 90.3% full; adding a GNN raises ReProver-style Lean retrieval R@10 from 39.6 to 50.0, yet ablating the context or premise graph individually moves R@10 by only about 1 point (ablated runs even scored above the no-ablation run); the CSLibPremiseBench structure reranker adds +0.0175 MRR over BM25 but not over BM25+symbol (+0.0037, CI crosses zero); in Rango, BM25 over proof states proved 46% more theorems than CodeBERT dense retrieval.
- **C06.06-K13** (reworded: the sources support less). LeanPremise recall differs from Yang 2023 because the ground-truth premise definition differs (premises of the whole proof vs the next tactic), not an 'upper-bound definition'; the upper-bound footnote concerns the random-forest baseline; this point is also about metric definitions, not offline-vs-prover mismatch. Corrected claim: Offline metrics may not predict prover success: XGBoost looked better on similarity metrics but worse on ATP success (0.31 vs 0.40 for the NMT model); labels from ATP proofs vs human proofs differ (Magnushammer human-only labels 54.0 vs augmented 56.3); and LeanPremise recall numbers are not comparable with Yang 2023 because ground-truth premises are defined over the whole proof rather than the next tactic.
- **C06.06-K15** (reworded: the sources support less). ReasonIR does charge the rewriting cost: it estimates test-time FLOPs for rewriting and reranking scenarios (200x less than Rank1-32B), and Rank1 studies test-time compute, so 'not charged in these papers' is false. Corrected claim: Reasoning-style retrieval (LLM rewrites query, sketches, judges candidates) beats fixed-embedding retrieval on informal-to-formal queries: group recall@10 46.1 vs 38.0 vs 9.3. Outside formal maths, BRIGHT shows the same: BM25 14.5 to 27.0 nDCG@10 with GPT-4 reasoning-step queries. The BRIGHT and LeanSearch numbers do not charge the extra LLM reasoning tokens against a budget; ReasonIR does estimate that compute.
