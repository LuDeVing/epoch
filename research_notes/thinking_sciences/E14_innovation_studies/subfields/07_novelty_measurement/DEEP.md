# Novelty measurement: deep document

*Subfield E14.07, "Atypical combinations in papers and patents". Built from evidence_a to d.jsonl (a01-a28, b01-b27, c01-c28, d01-d17), claims.jsonl (K01-K35) and critique.md in this folder. Ten key numbers were re-opened and checked in the critique pass. Status tags: [E] established (two or more independent sources), [S] single source, [C] contested.*

## 1. What it is

Novelty measurement asks one question: how do you put a number on "this work combines things in a way that is new"? The founding answer is Uzzi, Mukherjee, Stringer and Jones (2013). They looked at the list of references in a paper. Each pair of references sits in a pair of journals. They asked how often that journal pair is cited together, compared with how often a random citation network would put it together. That gives a z-score per journal pair. Negative z means atypical. Positive z means conventional. Each paper then gets two summary numbers: the median z (how conventional it is on average) and the 10th-percentile z (how atypical its most unusual pairs are).

The same idea has been applied to patents (class pairs), to chemistry (entity pairs), to words (surprisal and embedding distance), and, since 2023, to LLM-generated research ideas, where the question is now "is this idea new relative to the literature?" and "can a model tell?"

Four uses matter for us:
1. As a theory of what good novelty looks like: mostly conventional, plus a small atypical part.
2. As a warning about proxies: cheap novelty scores track expert judgment only weakly.
3. As a source of LLM tests: novelty before and after execution, LLM judges of novelty, diversity of model output.
4. As a design hint for open mode (schema S3 and selection): one distant element in a known frame.

Our agent is a scaffold around one model. The schema (SCHEMA.md) already says: G8 novelty is judged by running, not by a model's opinion; G4 samples from one model are not independent; S3 open mode uses isolated attempts, history, grounded analogues, many draws then code selects. This document tests those lines against the novelty-measurement literature and adds what is new.

## 2. History and theories in depth

**Before Uzzi.** Recombination theory says new things are new combinations of old things (Fleming 2001 [M]). Fleming's patent work (as cited by Bornmann, not opened) said new combinations raise the variance of outcomes and lower the mean. Foster, Rzhetsky and Evans (2015) [M] measured chemistry novelty as new combinations of chemical entities and found a tension between tradition and innovation. Krenn and Zeilinger (2020) built a concept network from 750,000 quantum-physics papers and trained a network to predict new links (ROC AUC about 0.85 for the 2017 state, read off a figure label).

**Uzzi et al. 2013 (the founding study).** Data: 17.9 million Web of Science papers, 15,613 journals, over 122 million possible journal pairs. Null model: a switching algorithm that rewires citation links while keeping each paper's reference count and each paper's citation count. Only 10 rewired networks were used. Worked example from the SOM: one journal pair had 469 observed co-citations against a null mean of 3,147 (atypical); another had 454 observed against a much smaller null mean (conventional).

**Rival measures.**
- Wang, Veugelers and Stephan (2017) [M]: count only new journal pairs that later get co-cited. Novel papers get fewer citations at first and more after several years (as reported; exact odds not read). Mairesse and Pezzoni (2018) [M] agree on French data.
- Lee, Walsh and Wang (2015) [M]: revised the z-score into a per-paper score U to split novelty from impact in teams.
- Kim, Cerigo, Jeong and Youn (2016): Uzzi-style z on US patent classes (8,884,909 patents). Patenting gets more conventional over time.
- He and Chen (2018): temporal embeddings of terms, predicting topic growth for more than ten years (713,912 observations).
- Lin, Evans and Wu (2022): rebuild atypicality as distance between journal embeddings (word2vec, 50 dimensions). Correlation with the z-score r=0.74.
- Wang H. (2024): content-based novelty as the average token surprisal under GPT-2.
- Shibayama, Yin and Matsumoto (2021): embedding distance between documents, checked against authors' own newness ratings.

**Critique and validity work.** Authors of landmark papers said their ideas were not necessarily inspired by their references (Tahamtan and Bornmann 2018, as cited). Bornmann, Tekles, Zhang and Ye (2019) ran the first quantitative convergent-validity test against expert F1000Prime tags. A corrigendum exists (J. Informetrics, DOI 10.1016/j.joi.2024.101544); we could not open it, so we do not know whether the numbers changed. Wang H. (2024) lists the standard objections: coarse knowledge units, citations for non-intellectual reasons, and missing context.

**From citations to outcomes.** Lin et al. (2022) tied atypicality to disruption and "Sleeping Beauty" late citations. Park, Leahey and Funk (2023) [M] argued that papers and patents are becoming less disruptive. Liu et al. (2025) and Kwon and Yang (2025) [M] looked at AI and output.

**The LLM turn (2022-2026).** Three lines grew:
1. LLMs as idea generators judged by humans (SciMON 2024, Si et al. 2024, Co-Scientist 2025, Gu and Krenn 2026).
2. LLMs as novelty judges, and benchmarks of that (RINoBench, NovBench, NovGauge, Sinhahajari et al., Shahid et al., Liu et al.).
3. Diversity of model output as a novelty floor (NoveltyBench, Artificial Hivemind, Doshi and Hauser).

**Competing explanations for why mixed novelty pays.**
- Anchoring: a conventional base lets readers accept the paper; the atypical part gives the new thing (Uzzi's reading).
- Team knowledge: larger teams bring more varied knowledge (Uzzi's team result).
- Delayed recognition: highly atypical work is cited late (Wang 2017; Lin 2022).
- Selection: journals and reviewers may favour or punish novelty (not tested in what we opened).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hit rate (top 5% citations in 8 years) is highest for papers with high median conventionality plus an atypical tail | 9.11 per 100 (high median, atypical tail); 5.82 (high median, no tail); 5.33 (low median, atypical tail); 2.05 (low on both). Baseline 5. About 2x | Uzzi 2013 (a03; critique re-checked) | [S] K01 |
| Most science is conventional | Median z below zero: 3.54% (1980s), 2.67% (1990s). 10th-percentile z below zero: 40.8% and 40.7% | Uzzi 2013 (a02); Lin 2022 (a14) | [E] K02 |
| Peak impact at very high conventionality | Peak at 85th-95th percentile of median conventionality, 11 bins, field fixed effects | Uzzi 2013 (a04) | [S] |
| Hit finding robust in WoS | Field fixed effects (243 subfields), top-1% cut, reference-count control; tail cuts 1st-20th percentile hold; vanishes at 30th percentile and above. Null = 10 rewired networks | Uzzi SOM (d14) | [S] K33 |
| Larger teams add atypical pairs | High tail novelty: 36.1% (solo), 39.8% (2), 49.7% (3+); +37.7% for 3+ vs solo. The paper prints 36.2 / 39.9 in a second passage | Uzzi 2013 (a05) | [S] K03 |
| Validation of the z-score is thin | Only 40.1% of interdisciplinary journal pairs have z<0 in the 1990s | Uzzi 2013 (a07) | [S] |
| Score U weakly tracks expert "new finding" tags | +1 SD in U: +7.47% "new finding"; +17.71% another novelty tag; +58.78% "novel drug target"; confirmation -13.45%; refutation -19.86%; pseudo R2 0.33% overall (0.58-2.84% per model); n=23,206 papers; standardized coefficient about 0.12 | Bornmann 2019 (a08, a09, b01, b03) | [S] K04 |
| Score W failed convergent validity | Only some tags matched; authors advise using U, doubt W | Bornmann 2019 (b02) | [S] K05 |
| Atypical papers more often in a disruptive class, but r is tiny | 61% vs 36% (extreme groups); r=-0.05 with disruption D; r=0.08 with Sleeping Beauty Index; 87.9M articles, 1.04B citations | Lin, Evans, Wu 2022 (a14, b04-b06) | [S] K06 |
| Highly atypical papers are rare and falling | 2.3% overall; 3.9% (1970) to 1.4% (2000); embedding vs z r=0.74 | Lin 2022 (a14, a16, b07) | [S] K07 |
| Patent atypicality: small positive hit effect | 8,884,909 patents, 80.3% with 2+ codes; high median-z small effect on top-5% 5-year citations | Kim 2016 (b11) | [S] K09 |
| Content surprisal separates expert-labelled novel papers | Welch t=2.6, p=0.005, 25 of 80 novel; false alarms on maths-heavy or odd-style text | Wang H. 2024 (c01, c02) | [S] K08 |
| Embedding novelty has a small link to self-rated newness | r=.170, p<.01, N=2,081 scientists (321 biomedical) | Shibayama 2021 (d13) | [S] K34 |
| Uzzi-style score is near chance as a binary detector | Accuracy URPC 0.55 (Marketing) / 0.48 (NLP); cited-reference embeddings 0.60 / 0.52; direct LLM judge MOOSE 0.64 / 0.59; RAG-KD 0.7453 / 0.7474 | Liu 2025 (c05-c07) | [S] K17 |
| AI ideas rated more novel than expert ideas (before execution) | Novelty 4.84 human (n=119) vs 5.64 AI (n=109, p<0.01) vs 5.81 AI+rerank (n=109); 49 ideas per condition; 79 reviewers; 298 reviews. Excitement 4.55 vs 5.19 (p<0.05). Feasibility 6.61 vs 6.34 (n.s.) | Si 2024 (a21, b13, b14, c10) | [S] K10 |
| The edge disappears after execution | Novelty change: human -0.010, AI -1.049 (FDR p=0.025). Excitement human +0.078 vs AI -1.760; effectiveness -0.052 vs -1.879; overall -0.628 vs -1.976. N=43 executors (19 human, 24 AI ideas), 58 reviewers. Execution-stage means: novelty 4.903 vs 4.729 (n.s.) | Si 2025 (a23, a24, c12) | [S] K11 |
| Reviewer novelty judgments are noisy | Inter-reviewer agreement 56.1% vs 66.0% (NeurIPS 2021) and 71.9% (ICLR 2024) | Si 2024 (a22, b14) | [S] K12 |
| LLM judges fail on novelty | Best macro-F1 17.2 (GPT-5) on 1,381 ICLR ideas; 0.0 F1 on "not novel" for all models; models avoid extremes (predict 3 or 4) | RINoBench (b18, c08, c09) | [S] K13 |
| LLM judges favour LLM text and disagree with experts | Human-LLM agreement as low as 22%, expert-expert 60%, LLM-LLM 52%; gpt-5.5 non-obviousness win 27.2% standalone, 49.1% comparative | Sinhahajari 2026 (b16, b17) | [E] K14 |
| Self-preference mechanism | GPT-4 picks own text 73.5% against two LLMs and humans; self-preference score 0.520 for GPT-4 of 8 judges; judges favour low-perplexity text | Panickssery 2024; Wataoka 2024 (d01, d02) | [E] K27 |
| LLM pairwise ranking of ideas is near human noise | Claude-3.5 pairwise 53.3% vs human 56.1% on idea ranking; 71.4% on accepted-vs-rejected papers (different task) | Si 2024 (a22, b15, c11) | [C] K15 |
| Retrieval-grounded checking beats zero-shot | "Not novel" accuracy 89.66% full pipeline vs 10.34-13.79% for ablations; TextGrad 0.78 acc vs zero-shot 0.68; only 51 labelled items in the prior public evaluation set | Shahid 2025 (b22, c15, c16, c28) | [S] K16 |
| Best K in retrieval is 5-10 | K=20 not better; 5-level rubric 0.0-1.0 | Liu 2025 (c07) | [S] K17 |
| Hierarchical scoring beats one-shot | RMSE down 35.4% (0.916 to 0.592, DeepSeek) and 17.3% (0.770 to 0.634, GPT) | Tan 2025 HSPIM (b21) | [S] K18 |
| Fine-grained benchmarks expose hollow reasons | 619 paper pairs, 18 LLMs; hallucination 0-39%; only 5 of 54 model-dimension cells keep half their raw F1 | NovGauge (b20) | [S] |
| AI idea generators are homogeneous | 200 of 4,000 seed ideas non-duplicate; within-prompt similarity 0.821; cross-model similarity 71-82%; 61.2% of pairs above 0.8 even at min-p, temperature 2.0 | Si 2024; Jiang 2025 (a22, c22, d08) | [E] K19 |
| In-context regeneration restores diversity | Three models roughly match human writers; GPT-4o and Gemini 2.0 Pro exceed human cumulative utility. 20 models, 1,100 prompts | NoveltyBench (c21, d09) | [E] K31 |
| Iterative novelty boosting | +54.4%, +55.6%, +47.8%, +46.7% of ideas rated more novel (4 variants, iteration 1); +57.8% iteration 2; 88.9% substantially different; ground truth judged more novel 85% | SciMON (a20, c17) | [S] K20 |
| Citation-chosen concept pairs do not raise interest | Mean interest 2.350 (high-citation) vs 2.446 (random) vs 2.414 (titles only); 4,400+ ideas; 84.3% completion; AUC 67.44 (GPT-4o), 60.39 (GPT-3.5), 63.20 (network) | Gu and Krenn 2026 (a25, a26) | [S] K21 |
| GenAI raises individual novelty but homogenises | Novelty +6.7% (b=0.259); +8.1% with 5 ideas (b=0.311); +10.7% for low-creativity writers; stories 5.2% more similar to the AI idea | Doshi and Hauser 2024 (c20) | [E] K23 |
| Many "novel" agent outputs are not | 24.0% of 50 documents plagiarised (14% one-to-one, 10% close); AI Scientist checker marked all 10 ideas novel | Gupta and Pruthi 2025; Beel 2025 (c13, c14) | [E] K24 |
| Pre-execution scores barely predict post-execution | AI-idea excitement r about -0.32; trained predictor with retrieval 64.4% vs experts 48.9% (NLP); 77% full test set; 1,585 test pairs | Si 2025; Wen 2025 (d03, d04) | [S] K28 |
| Far-mechanism, near-purpose inspiration (the Uzzi pattern in an experiment) | 46% good ideas vs 37% random vs 30% TF-IDF near-domain; strict 38% vs 22% vs 21%; mixed model 0.71 vs 0.28 vs 0.27; 749 ideas; kappa 0.51 | Hope 2017 (d06, d07) | [S] K29 |
| Diverse multi-agent teams with a leader | +0.46 (Qwen3 judge), +0.44 (o1-mini); leader +0.57; all-junior 7.73 vs solo 7.75; flat past 3 agents; human blind A/B 87.5% of 40 pairs | Chen 2025 (d05) | [S] K30 |
| Path novelty in code and maths is costly | Correct-and-novel falls with each constraint; only MCTS raised divergence; GPT-4o 76.6% MATH but novel/correct under 50%; capability vs idea originality r=0.357 (p=0.038, 41 models) | Lu 2025; Ye 2024; Ruan 2024 (d10-d12) | [E] K32 |
| Post-ChatGPT novelty drop in IS journals | -0.176 SD (about 7 percentile points); 13,847 articles, 44 journals | Safari and Babaei 2026 (c03) | [S] K25 |
| A shared strategy list made later human ideas less original | H(2)=9.14, p=0.010; Dunn p=0.009; 460 participants | Kumar 2025 (d15) | [S] K35 |
| Co-Scientist expert novelty 3.64/5 on 11 of 15 goals | Small, subjective | Gottweis 2025 (a28) | [S] K26 |

## 4. Mechanisms and models

### 4.1 The Uzzi z-score (build it)
1. Take a citation database. For each paper, list its references, and map each reference to a journal.
2. For each journal pair (i, j), count co-citations: the number of papers that cite both.
3. Build a null: rewire citation links with a switching algorithm (swap the targets of two links) so that each citing paper keeps its number of references and each cited paper keeps its citation count. Uzzi used 10 synthetic networks; use more. Keep time structure by restricting swaps to the same year.
4. z(i,j) = (observed - null mean) / null SD.
5. Per paper, collect z over all its reference pairs. Report median z and 10th-percentile z.
6. Atypical tail = 10th-percentile z below zero. Conventional = high median z. The "hit" model: high median plus atypical tail.

Failure points: journals are coarse labels; only WoS-covered references count; 10 null networks is thin; conventional pairs dominate (half of 1990s papers have median z above 99.5).

### 4.2 Embedding distance (the cheaper rebuild)
Train word2vec skip-gram on journal co-citation sequences (dimension 50, negative sampling 5, window 10). Atypicality = distance between journal vectors. It reproduces z at r=0.74 and tracks time (the 2000 space had 8,009 journals vs 2,429 in 1970). For text: embed abstracts (SPECTER2) and take the distance to the nearest recent papers (Safari and Babaei), or the distance between a document and its references (Shibayama; r=.170 with self-rated newness).

### 4.3 Token surprisal (cheapest)
Average per-token surprisal under a small language model (GPT-2 124M on 6.5M Wikipedia docs). Higher surprisal means more unusual wording. It separates expert-novel from other papers (t=2.6) but flags maths-heavy text and odd style. Control: score matched paraphrases to subtract style.

### 4.4 Retrieve-then-judge novelty check (what works best for LLMs)
1. Extract facets from the idea: purpose, mechanism, evaluation (Scideator, Shahid).
2. Retrieve candidate prior papers per facet (embedding filter, then keyword search).
3. Rerank by facet relevance (RankGPT-style; dropping this fell "not novel" accuracy to 13.79%).
4. Judge with a rubric: 0.0 no novelty to 1.0 very high, anchored on overlap (0.3 subset of an existing idea, 0.5 about 50% overlap, 0.7 small overlap, 1.0 distinct). Retrieve K = 5 to 10.
5. Output a binary label with the overlapping papers cited. A different model family should do the judging.

### 4.5 Execution check
Si's executed-ideas design: assign each idea to an expert, give 100+ hours, rate before and after. The mechanism is that ideas look new but the implemented version collapses toward known methods. For an agent, "execute" means running code, a solver, or a held-out test, not rating the text.

### 4.6 Diversity measure (distinct-k)
Sample k answers. Classify each pair as functionally equivalent or not (a trained classifier reached 79% against human labels). distinct-k is the number of equivalence classes. Use it as a floor: if k samples give 1 class, novelty selection has nothing to select from.

### 4.7 Denial prompting for path novelty
Take a problem with known solutions. List the techniques in them. Forbid those, ask again, check correctness by running it. Repeat with more constraints. Correct-and-novel rate falls with each constraint.

## 5. What holds up

**Replicated or confirmed by an independent source.**
- Most work is conventional (Uzzi; Lin on a different database, 87.9M MAG articles). [E]
- Hit rate rises with a conventional-plus-atypical profile: Uzzi in WoS; Lin's Fig 1d confirms it in MAG; Kim 2016 shows a small positive patent effect. This is the closest to a replication, but all use the same journal-pair method. [S for the mechanism]
- LLM idea generators produce duplicates and cross-model homogeneity: Si, NoveltyBench, Hivemind. [E]
- LLM judges are self-preferring: Panickssery, Wataoka, Sinhahajari. [E]
- Plagiarism and false "novel" labels in agent output: Gupta and Pruthi, Beel. [E]
- GenAI lifts individual novelty and homogenises: Doshi and Hauser, with Kumar's human-after-LLM result and Hivemind. [E]
- Reasoning scaffolds raise correctness and not divergence (code, maths, ideas). [E]

**Failures and weak validity.**
- Bornmann: R2 0.33%, standardized effect 0.12. Score W failed.
- Lin: r=-0.05 with disruption. The 61% vs 36% is an extreme-group contrast.
- Liu 2025: URPC accuracy 0.55 and 0.48 on binary novelty (chance or worse).
- Embedding novelty vs self-rated newness: r=.170.
- Gu and Krenn: citation-predicted pairs were not more interesting than random (2.350 vs 2.446).
- RINoBench: F1 0.0 on the "not novel" class for every model.

**Boundary conditions.**
- Uzzi's hit result vanishes when the tail is cut at the 30th percentile or higher; it holds for the 1st to 20th. Peak near the 85th percentile of conventionality.
- Novelty pays late: novel papers get cited less at first (Wang 2017, Mairesse 2018; both [M]). Lin: the effect takes about ten years.
- Fields: Lin's field check covered only 11 fields in the 1970 cohort (45,677 of 87,475 papers matched).
- Measurement depends on journal labels, WoS coverage, and period (pairs atypical in 1970 were ordinary by 2000).
- Human-rated novelty is noisy (agreement 56.1%).

**Interventions that worked.**
- Retrieval before judging (89.66% vs 10-14% ablation on "not novel"; RAG-KD 0.7453 vs MOOSE 0.64). One source family.
- Hierarchical decomposition (RMSE -17.3% to -35.4%).
- Asking judges explicitly about narrowness or source-boundedness (gpt-5.5 lose rate 71.7% to 85.4%); diagnostic framing recovered agreement with experts.
- Showing earlier answers in context (NoveltyBench).
- Near-purpose, far-mechanism inspiration for humans (46% vs 30-37%).
- Diverse team with a leader (+0.46), flat past 3 agents.

**Interventions that did not work.**
- Zero-shot LLM novelty judging; reasoning text that sounds right (RINoBench: reasons match humans, labels do not).
- Retrieval alone for predicting outcomes: o3 stayed near random (Wen 2025).
- Citation-based concept selection (Gu and Krenn).
- A novelty-check tool in a user study: about 6 uses, no significant change in confidence (n=17).
- Paraphrase and system-prompt tricks for diversity: marginal.
- Pooling several models for diversity (71-82% similar).
- Self-correction and planning for divergence (they cut it).
- A fixed LLM strategy list for later human originality (worse).

**Moderators.** Writer ability (low-creativity writers gain 10.7%), team seniority mix, number of agents, constraint count, whether retrieval is in the loop, and whether the judge shares a family with the generator.

## 6. Language models

**As idea generators.** In blind review, AI ideas beat expert ideas on novelty (5.64 vs 4.84) before execution. After execution by experts (100+ hours each), AI ideas lose 1.049 novelty points, and the AI-versus-human drop is significant on all four metrics (FDR p 0.001 to 0.025); human ideas lose about nothing. Execution-stage means do not differ significantly, and humans are numerically higher on most. Si's 4,000 seed ideas contained 200 non-duplicates. Gu and Krenn found that citation-predicted concept pairs did not raise expert interest. SciMON's novelty-boost loop raised novelty in about half the ideas per iteration but added generic terms; ground-truth ideas were judged more novel in 85% of pairs. Agent tournaments (Co-Scientist) report 3.64/5 expert novelty; the study is small.

**As novelty judges.**
- RINoBench: best macro-F1 17.2; 0.0 on "not novel"; predictions cluster at 3 and 4; reasoning models only slightly better; written reasons look like human reasons.
- NovBench (1,684 paper-review pairs): limited understanding; review-tuned models often fail.
- NovGauge: hallucinated evidence 0-39%.
- Sinhahajari: a "novelty mirage". LLM judges give LLM questions 82% / 52% win rates against references that experts rate 78% / 56% (two separate annotators). Asking for narrowness recovers agreement.
- Pairwise ranking: Claude-3.5 53.3% vs human 56.1%. Contested: 71.4% on a different task.
- Mechanism: self-recognition (GPT-4 73.5%) and low-perplexity preference.
- What changed it: retrieval (RAG-KD 0.7453; 89.66% on "not novel"), decomposition (RMSE -17% to -35%), narrowness framing, TextGrad prompt (0.78 vs 0.68). A trained predictor with retrieval reached 64.4% vs experts 48.9% on which idea wins after execution. Frontier models alone were near random there.

**As diverse samplers.** 20 models give less diversity than 8 human authors; bigger models are often less diverse. Cross-model similarity 71-82%. Temperature 2.0 with min-p still left 61.2% of pairs above 0.8. In-context regeneration brings three models to human level. For humans, AI help raises novelty 6.7-8.1% and cuts between-story variety.

**On path novelty.** Reasoning strategies raise correctness and cut divergence; only MCTS raised divergence (on a 7B model). MATH accuracy does not predict novelty. LiveIdeaBench: originality vs general score r=0.357. No planning or puzzle study found.

**Post-2022 shift.** Novelty scores in 44 IS journals fell about 0.176 SD for one paper group after ChatGPT. This is a timing shift, not proof of LLM cause.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| The judge of novelty must be a different model family from the generator, see no authorship, and be length-normalised. G5 and G8 already say the generator never selects; add self-recognition as the reason and require a different-family judge | G5, G8 | [E] K14, K27 | b16, b17, d01, d02 |
| Candidates from one model are homogeneous across families; pooling models adds little. Reinforces G4: diversity must come from structure (different frames, code-kept history of tried directions), not from more samples or more models | G4, S3 | [E] K19, K31 | a22, c22, d08, d09, c21 |
| In open mode, generate sequentially with earlier candidates shown to the generator, then let code select. This narrows the "fresh context" rule of S3 for open mode only, and needs test T6 to confirm it at equal tokens before wording changes | S3 (open mode) | [E] K31 | c21, d09 |
| Run a prior-work check before accepting a "novel" claim and log how many pass; agent novelty claims are often not novel (24.0% plagiarism; 10 of 10 marked novel) | S4/S8, memory | [E] K24 for the problem; the retrieval fix is [S] (see Test first) | c13, c14 |
| Reasoning scaffolds (planning, self-correction) raise correctness and cut divergence. Keep verification out of the generating step in open mode | S3, S5 | [E] K32 | d10, d11, d12 |

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| One distant element in a known frame (near purpose, far mechanism) beats all-near and all-far candidate sets in open mode | S3 grounding, O7 | [S] K01, K29 | a03, d06, d14 |
| Prior-work retrieval check (K=5 to 10, facet rerank) before accepting a novel candidate cuts the false "novel" rate | S4/S8, memory | [S] K16, K17 | b22, c05-c07, c15, c16 |
| Rate novelty before and after a verification step; check whether the pre-step rating predicts the post-step one | G3, S8 | [S] K11, K28 | a23, c12, d03, d04 |
| Decomposed (per-facet) rating vs one-shot rating | O3 | [S] K18 | b21 |
| Ask a judge "how narrow or source-bound is this?" rather than "how novel?" | G5 | [S] K14 | b17 |
| An explicit "make more novel" revision pass | O8, S5 | [S] K20 | a20, c17 |
| Cheap proxies (surprisal, embedding distance) as a weak prior only | S3/S4 | [S] K08, K34, K04 | c01, c02, d13, a08 |
| 3 mixed-persona samples plus an integrating step vs one agent at equal tokens | S3, G9 | [S] K30 | d05 |
| Denial prompting (name the standard method, then forbid it) for maths and planning | O4, O8 | [S] partly [E] K32 | d10 |
| Is there a distance threshold where novelty stops paying? | S3 | [S] K06 | a14, b05 |
| Do not select by a citation-style prior (caution, not an add) | G8 | [S] K21 | a25 |
| Keep 3 or more raters and report agreement; single ratings are noisy | logging | [S] K12 | a22, b14 |
| Avoid handing the same fixed strategy list to every sample | G4 | [S] K35 | d15 |

Note on G9: Chen 2025 (d05) is not an equal-token test, so G9 stays in force until T8 passes.

## 8. Concrete tests on our bench

All arms get the same total token budget, counting setup. Each item is scored by 3 blind raters or by code where a checker exists. Report win rate with a confidence interval and rater agreement.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Open-mode idea or solution-path tasks | (a) all-near candidates; (b) all-far; (c) near frame plus one distant element; (d) plain best-of-N | Blind novelty and correctness; distinct-k; correct-and-novel rate | (c) beats (a) and (b) on correct-and-novel by 5 to 10 points (Hope: 46% vs 30-37%) |
| T2 | Self-generated "novel" claims on prompts with known prior work | (a) no check; (b) retrieval check K=5; (c) K=10; (d) K=20 | False "novel" rate against known-prior-work labels; tokens per accepted idea | (b)/(c) cut false-novel rate by more than 20 points; K=20 no better than K=10 |
| T3 | Tasks with an execution check (code, maths, ARC-style) | Rate novelty before and after running the check | Drop in novelty rating; pre-post correlation | Larger drop for self-generated than baseline candidates; pre-post r below 0.3 |
| T4 | Same items as T1 | Judge: same family as generator vs different family vs mixed panel | Agreement with blind human labels; own-vs-other candidate gap | Same-family judge favours own candidates by more than 10 points; different family reduces it |
| T5 | Items with 3 to 5 known solutions | Plain retry vs denial ("name the standard method, then forbid it") | Correct-and-novel rate; correctness alone | Denial raises correct-and-novel; correctness alone falls a little |
| T6 | NoveltyBench-style prompts | Parallel sampling vs sequential with earlier candidates visible | distinct-k at equal tokens | Sequential reaches human-level distinct-k |
| T7 | Open-mode tasks | One-shot novelty rating vs per-facet rating vs narrowness rating | F1 on the "not novel" class vs blind human labels | Facet or narrowness lifts "not novel" F1 from 0.0 to above 0.3 |
| T8 | Open-mode tasks | 1 agent vs 3 mixed-frame samples plus integrator | Blind novelty plus distinct-k | Gain only if distinct-k rises; otherwise G9 stands |
| T9 | Candidate sets at near, middle and far distance | Distance bins on our task bank | Quality by bin | Locate the threshold; Lin hints only the extreme end pays |

## 9. What does not transfer, and why

- **Journal-pair z-scores.** They score a finished paper's reference list. Our agent has no reference list for an answer. The score is correlational and has R2 0.33% against expert tags.
- **Citation hit as the outcome.** Our outcome is a correct or useful answer, not citations. Impact is a social process with delays of years.
- **Team size as diversity.** Human team members bring independent knowledge. LLM samples are 71-82% similar across families, so a "team" of one model's samples has little independent knowledge (G4).
- **Rated novelty before execution.** Si's data show it does not survive execution. Rated novelty of text is not a quality signal for the agent.
- **LLM-as-judge for novelty.** Self-preference and zero F1 on "not novel" mean we cannot use a model as novelty selector (G8).
- **Human crowd results (Hope).** Crowd workers on product design may not transfer to a scaffolded LLM; "far" was tuned by hand.
- **Research-idea benchmarks.** Almost all LLM studies cover NLP or ML ideas with small expert panels. Our tasks are maths, planning and puzzles where novelty is solution-path novelty.
- **Population trends.** Declines in disruption and the post-ChatGPT drop describe science as a system, not an agent's behaviour.
- **Multi-agent discussion.** Chen 2025's gain is not at equal tokens, so it does not override G9.

## 10. Open questions

1. Does adding one distant element to a near frame raise blind-rated novelty and correctness for an LLM agent at equal tokens?
2. Which cheap proxy best matches blind labels, and does any beat chance on the "not novel" class?
3. What is the token cost of retrieval-grounded novelty checking, and what is the best K?
4. Does the ideation-to-execution drop appear in a scaffolded agent with a verify step, and can a pre-commit check predict it?
5. Does Uzzi's hit result replicate outside WoS (OpenAlex, patents, preprints) with a better null than 10 networks? What is the effect size beyond the 2x2 hit cut?
6. Does multi-sample or multi-persona diversity beat one agent at equal tokens when diversity is measured by distinct-k?
7. Is the gpt-5.5 favouring in Sinhahajari driven by self-preference? Plausible, not shown.
8. Where does distance stop paying? Lin's extremes (61% vs 36%) against r=-0.05.
9. Does any of this transfer to maths, planning and puzzles?
10. Did the Bornmann 2024 corrigendum or Veugelers and Wang (2019) change any validity number? Both pages returned 403.
11. What does the January 2026 correction to Shibayama 2021 change? Not read.

## 11. Sources

[V] = opened and read this run. [M] = snippet or second-hand only.

- [V] Uzzi, Mukherjee, Stringer, Jones (2013) Atypical combinations and scientific impact. https://www.kellogg.northwestern.edu/faculty/jones-ben/htm/atypical_combinations_and_scientific_impact.pdf
- [V] Uzzi et al. (2013) Supplementary Online Material. https://www.science.org/doi/10.1126/science.1240474
- [V] Bornmann, Tekles, Zhang, Ye (2019) Do we measure novelty when we analyze unusual combinations of cited references? https://arxiv.org/abs/1910.03233
- [V] Lin, Evans, Wu (2022) New directions in science emerge from disconnection and discord. https://arxiv.org/abs/2103.03398
- [V] Kim, Cerigo, Jeong, Youn (2016) Technological novelty profile and invention's future impact. https://arxiv.org/abs/1512.06169
- [V] He and Chen (2018) Predictive effects of novelty measured by temporal embeddings. https://arxiv.org/abs/1801.09121
- [V] Krenn and Zeilinger (2020) Predicting research trends with semantic and neural networks. https://arxiv.org/abs/1906.06843
- [V] Wang Q. et al. (2024) SciMON. https://arxiv.org/abs/2305.14259
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? https://arxiv.org/abs/2409.04109
- [V] Si, Hashimoto, Yang (2025) The ideation-execution gap. https://arxiv.org/abs/2506.20803
- [V] Gu and Krenn (2026) Generating interesting scientific ideas using knowledge graphs and LLMs. https://arxiv.org/abs/2405.17044
- [V] Radensky et al. (2024) Scideator. https://arxiv.org/abs/2409.14634
- [V] Gottweis et al. (2025) Co-Scientist. https://arxiv.org/abs/2502.18864
- [V] Sinhahajari, Majumder, Poria (2026) On the limits of LLM-as-judge for scientific questions. https://arxiv.org/abs/2606.12071
- [V] Schopf and Faerber (2026) RINoBench. https://arxiv.org/abs/2603.10303
- [V] Wu et al. (2026) NovBench. https://arxiv.org/abs/2604.11543
- [V] Zhang et al. (2026) NovGauge. https://arxiv.org/abs/2609.11234
- [V] Tan et al. (2025) HSPIM. https://arxiv.org/abs/2504.14620
- [V] Shahid et al. (2025) Literature-grounded novelty assessment. https://arxiv.org/abs/2506.22026
- [V] Wang H. (2024) A content-based novelty measure for scholarly publications. https://arxiv.org/abs/2401.03642
- [V] Safari and Babaei (2026) Research novelty in IS journals after ChatGPT. https://arxiv.org/abs/2603.22510
- [V] Liu et al. (2025) Harnessing LLMs for scientific novelty detection. https://arxiv.org/abs/2505.24615
- [V] Gupta and Pruthi (2025) All that glitters is not novel. https://arxiv.org/abs/2502.16487
- [V] Beel et al. (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297
- [V] Li et al. (2024) Chain of Ideas. https://arxiv.org/abs/2410.13185
- [V] Hu et al. (2024) Nova. https://arxiv.org/abs/2410.14255
- [V] Doshi and Hauser (2024) Generative AI enhances individual creativity but reduces collective diversity. https://arxiv.org/abs/2312.00506
- [V] Zhang et al. (2025) NoveltyBench. https://arxiv.org/abs/2504.05228
- [V] Jiang et al. (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Panickssery, Bowman, Feng (2024) LLM evaluators recognize and favor their own generations. https://arxiv.org/abs/2404.13076
- [V] Wataoka, Takahashi, Ri (2024) Self-preference bias in LLM-as-a-judge. https://arxiv.org/abs/2410.21819
- [V] Wen et al. (2025) Predicting empirical AI research outcomes. https://arxiv.org/abs/2506.00794
- [V] Chen et al. (2025) Beyond brainstorming. https://arxiv.org/abs/2508.04575
- [V] Hope et al. (2017) Accelerating innovation through analogy mining. https://arxiv.org/abs/1706.05585
- [V] Hope et al. (2021) Scaling creative inspiration with fine-grained functional aspects. https://arxiv.org/abs/2102.09761
- [V] Lu et al. (2025) Benchmarking language model creativity: code generation. https://arxiv.org/abs/2407.09007
- [V] Ye et al. (2024) Assessing the creativity of LLMs in proposing novel solutions to mathematical problems. https://arxiv.org/abs/2410.18336
- [V] Ruan et al. (2024) LiveIdeaBench. https://arxiv.org/abs/2412.17596
- [V] Shibayama, Yin, Matsumoto (2021) Measuring novelty in science with word embedding. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0254034
- [V] Kumar et al. (2025) Human creativity in the age of LLMs. https://arxiv.org/abs/2410.03703
- [M] Wang, Veugelers, Stephan (2017) Bias against novelty in science. https://doi.org/10.1016/j.respol.2017.06.006
- [M] Lee, Walsh, Wang (2015) Creativity in scientific teams. https://doi.org/10.1016/j.respol.2014.10.007
- [M] Foster, Rzhetsky, Evans (2015) Tradition and innovation in scientists' research strategies (no URL; cited in Lin 2022)
- [M] Mairesse and Pezzoni (2018). https://doi.org/10.1016/j.respol.2018.06.005
- [M] Veugelers and Wang (2019) Scientific novelty and technological impact. https://doi.org/10.1016/j.respol.2019.01.019 (403)
- [M] New and atypical combinations, Research Policy 2020, Crossref metadata only. https://doi.org/10.1016/j.respol.2020.104063
- [M] Fleming (2001) Recombinant uncertainty in technological search. https://doi.org/10.1287/mnsc.47.1.117.10671
- [M] Bornmann corrigendum, J. Informetrics. https://doi.org/10.1016/j.joi.2024.101544 (403)
- [M] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292
- [M] Park, Leahey, Funk (2023) Papers and patents are becoming less disruptive (cited in LLM papers)
- [M] Kobak et al. (2025); Kwon and Yang (2025), as cited in Safari and Babaei 2026
