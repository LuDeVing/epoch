# Vector-space relational similarity: deep document

*Subfield C10.09. Sources: evidence_a-d.jsonl (a01-a25, b01-b26, c01-c25, d01-d18), claims.jsonl (K01-K21), critique.md. Figures were checked in the critique pass unless marked.*

## 1. What it is

Relational similarity asks: how alike are the relations inside two word pairs? Mason:stone and carpenter:wood share a relation (worker to material). They share almost no attributes. Attributional similarity asks how alike two single words are (car and automobile). Turney (2006) drew this line and built a method for the first kind [a01].

The cheap method is simple. Take a word pair. Search a big text corpus for the strings that join the two words (X "cuts" Y, X "made of" Y). Count how often each joining pattern occurs. The pair becomes a vector of pattern counts. Compare two pairs by the cosine of their vectors. Pick the SAT answer whose pair has the highest cosine with the stem pair.

The subfield has three layers:
1. Count-vector methods on pairs (Turney and Littman 2005; Turney 2006 LRA; PairClass; SuperSim).
2. Word-embedding vector offsets (Mikolov 2013: king - man + woman). A cousin, not the same thing.
3. Language-model scoring and relation embeddings (RelBERT, GPT-3 onward), which replaced both for accuracy.

Correction to our own index: SUBFIELDS says "via Wikipedia". That is false. LRA used the Waterloo MultiText web corpus, about 5x10^10 words. Wikipedia only appears in Ethayarajh's frequency counts [critique 7, a01].

Why it matters for our agent: the agent must find analogues for a stuck problem (operator O7, "map an analogue"). Cheap similarity is the retrieval step. The key finding is that general similarity is not analogy similarity. A retriever built for topic closeness returns near neighbours, not same-structure problems [K18, d12, d13].

## 2. History and theories in depth

**Before 2003.** Analogy tests (SAT verbal analogies, 5 choices, chance 20%) were attacked with hand-built systems on WordNet paths. Veale (2004) reached about 42.8% [a02, a24]. Attributional word measures (Lin, Resnik, Jiang-Conrath, PMI-IR) were the default idea: if A is like C and B is like D, then A:B is like C:D.

**2003: Turney, Littman, Bigham, Shnayder.** A 13-module ensemble for synonyms and analogies. On TOEFL synonyms the mix reached 80.2% (log rule 82.0%) against LSA alone 43.8%, PMI-IR 69.0%, thesaurus 69.6%. On the 374 SAT analogies the ensemble scored about 45% (37.0% without the phrase-vector module) [a08, b08, c07]. This paper introduced the 374-item SAT set: 90 from prep sites, 14 ETS, 190 from Claman (2000), 80 from guidebooks.

**2005: Vector Space Model (VSM), Turney and Littman.** A pair becomes a 128-dimensional vector: 64 fixed joining words (from, for, of, in, ...) in both orders, with log(x+1) weighting. Counts came from AltaVista hit counts (about 5x10^11 words). It needed 287,232 queries (374 x 6 pairs x 128), about 17 days at a polite 5 s delay. SAT result: 176 right, 193 wrong, 5 skipped, recall 47.1% [a06]. The same paper classified 600 noun-modifier pairs.

**2005-2006: Latent Relational Analysis (LRA).** Three changes to VSM: (a) learn the patterns from the corpus (4,000 kept, 8,000 columns) instead of fixing 64 words; (b) expand each word with thesaurus synonyms and keep the best alternate pair; (c) smooth with SVD to 300 dimensions. SAT recall 56.1% (210/374; precision 56.8%; F 56.5), about the 57% estimate for the average US college applicant. It took almost nine days [a01, a02, a04]. The "human-level" claim needs care (section 5).

**2008-2013: cheaper supervised variants.** PairClass (2008): 52.1% SAT, TOEFL 76.2%, synonym-antonym 75.0% [a09]. SuperSim (2013): 54.8% (205/374), trained in minutes instead of nine days; SemEval-2012 Task 2 Spearman 0.408, best at the time [a10, c08]. The nine-day cost was not needed. The accuracy ceiling stayed near 52-57%.

**2013-2014: embeddings.** Mikolov et al. (2013) tested offsets on a 19,544-question set (8,869 semantic, 10,675 syntactic). Skip-gram 640-d on 320M words: 55% semantic, 59% syntactic [a12, b10]. Levy and Goldberg (2014) showed explicit sparse count vectors with the right scoring rule (3CosMul) match embeddings: Google set 68.24% explicit vs 66.72% embedding [a13]. That supports Turney's count-vector idea. It also says the gain lies in the scoring rule, not in dense vectors.

**2016-2020: the critique wave.** Linzen (2016), Drozd et al. (2016), Gladkova et al. (2016), Rogers et al. (2017), Chen, Peterson and Griffiths (2017), Ethayarajh et al. (2019), Nissim et al. (2020) showed that offset tests are inflated by artifacts, vary by relation type and frequency, and do not match human relational judgments [a14-a17, b11-b17, c09-c12].

**2020-2026: language models.** GPT-3 few-shot reached 65.2% on SAT [a18]. Fine-tuned RelBERT 69.5-73.6% [b21, d01]. ChatGPT 74.8% zero-shot, 83.7% one-shot in one test [b24]. GPT-4 (2023) SAT 70.3, BATS 90.8 [d01]. Webb et al. (2023) said GPT-3 beats people on several analogy forms; Lewis and Mitchell (2024) found it falls on counterfactual versions where humans stay stable [c15, c16]. Since 2023, work moved to using analogy inside prompts (Yasunaga 2023, Thought Propagation) and to retrieval by shared method (BRIGHT 2025).

**Theories.**
1. Relation is a pattern profile: the words that connect A and B in text tell you the relation (Turney).
2. Relation is a vector difference: the offset is the relation (Mikolov). Ethayarajh et al. gave a condition: offsets work when pair frequency is high and the words differ consistently (countries to capitals 95.4% at median frequency 3,436.5; countries to currencies 9.2% at frequency 19) [b17].
3. Human relational similarity is not a metric: it is asymmetric, breaks the triangle inequality, and depends on relation type (Chen et al.) [a17, b16]. A plain cosine cannot show those features.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LRA solves SAT analogies at about the average-applicant level | 210 right / 160 wrong / 4 skipped of 374. Precision 56.8, recall 56.1, F 56.5. Chance 20. Human est. 57. 95% CI 51.0-61.2 | Turney 2006 [a02, b01] | Established (one test set) |
| "Human-level" is a non-difference, not a win | CI includes 57. Human figure comes from a 78-item test percentile with an equal-difficulty assumption. 190 official items 61.1% vs 51.1% on the other 184 | [a21, b04, c23] | Single-source |
| Relational VSM beats best attributional measures | Attributional F 28.5-35.0; VSM 47.4; LRA 56.5. Always-highest-cooccurrence 11.8 (below chance); lowest 16.8 | [a03, c03, c25] | Single-source (one lab) |
| VSM with 64 fixed patterns | 176/193/5, recall 47.1, precision 47.7, F 47.4. 17 days of queries | Turney and Littman 2005 [a06] | Established |
| Same VSM on a 10x smaller corpus | 47.1 to 38.5 recall; 34 questions skipped (5 for AltaVista) | [a04, b03, c02] | Single-source |
| LRA design ablations | No SVD 53.5 (not significant); no synonyms 49.5 (22 skipped); LRA still beats VSM-WMTS without both | [a04, b02, c05] | Single-source |
| LRA cost | About 9 days for 374 questions; VSM-AV 17 days; VSM-WMTS 1 day; matrix 17,232 x 8,000, density 5.8% | [a01, b03] | Established |
| Noun-modifier classification (600 pairs) | 30 classes: LRA 39.8% (239/600), F 36.6; VSM-AV 27.8% (macro F 26.5); chance F 3.3. 5 classes: LRA 58.0% (348/600), F 54.6; VSM-AV 45.7% (274/600), F 43.2; majority baseline 43.3% (260/600) | [a05, a22, b05] | Established |
| Margin as abstention rule for VSM | Margin +0.11: precision 59.2% at recall 11.2%. Top-1 of 369 candidates 8.4%, top-10 29.5% | [a07] | Single-source |
| Cheaper supervised pair models | PairClass 52.1; SuperSim 54.8 (205/374); SemEval-2012 Task 2 Spearman 0.408 | [a09, a10, c08] | Single-source |
| Offset accuracy inflated by artifacts | Without excluding inputs, nearest neighbour is b in 93% of cases. ONLY-B .42/.36/.33; plurals ONLY-B .70. Reversing direction -0.11 on average | Linzen 2016 [a14, b12, c09] | Established (4 sources) |
| Google vs BATS gap | GloVe 80.4% (Google) vs 28.5% (BATS). Best 3CosAdd on BATS 28.1; LRCos 47.7; 3CosAvg 34.4 | Gladkova, Drozd 2016 [a15, a16, b13] | Established |
| Relation type and frequency dominate offset accuracy | Google categories 10.53-99.41%. Capitals 95.4% (freq 3,436.5) vs currencies 9.2% (freq 19). csPMI vs error r > 0.50 | [a13, a16, b17, c11] | Established |
| Count vectors match embeddings with a good rule | Google: 3CosAdd emb 62.70 vs explicit 45.05; 3CosMul emb 66.72 vs explicit 68.24. MSR 3CosAdd 53.98 vs 29.04; 3CosMul 59.09 vs 56.83 | Levy and Goldberg 2014 [a13, b11] | Established |
| Cosine does not match human relational ratings | Human within-subtype 5.01, between-subtype 4.02, between-type 2.70 (1-7). Order effect 4.76 vs 2.36. Triads 5.44/5.43 vs 2.99, F(2,33)=45.57; models flat (F=1.20, .24). Fails on SIMILAR, CONTRAST, NON-ATTRIBUTE | Chen et al. 2017 [a17, b16, c12] | Single-source |
| GPT-3 on SAT by shots | 53.7 zero / 59.1 one / 65.2 few; about +10 over 13B | Brown 2020 [a18, c13] | Established |
| Fine-tuned relation embeddings | RelBERT SAT 69.5 (test part 70.6), U2 66.2, U4 65.3, Google 92.4, BATS 78.8; Kumar run 73.6/67.5/63.0/80.9/81.4 | Ushio 2021 [b21, d01] | Single-source |
| Other baselines on full SAT | LRA 56.4; FastText 49.7; GloVe 48.9; word2vec 42.8; PMI 23.3; random 20.0 | [b20] | Established |
| GPT-4 vs RelBERT | SAT 70.3/73.6; U2 71.9/67.5; U4 68.8/63.0; BATS 90.8/80.9; Google 99.0/81.4; SCAN 23.5/27.3; E-KAR 51.3/48.7. No CIs (SAT: about +/-4.6) | Kumar and Schockaert 2023 [d01] | Single-source |
| ChatGPT | SAT 74.8 zero-shot, 83.7 one-shot; BATS 92.4; U2 76.3; U4 71.3; embedding baseline SAT 36.7; human SAT 57.0 | Yuan 2023 SCAR [b24] | Single-source |
| Answer-word artifact | RoBERTa SAT 53.4 to 38.6/35.6 with head/tail masked; U2 58.3 to 37.7/37.3; Google 93.6 to 60.6/55.8 | Ushio 2021 [b26, c14] | Single-source |
| Counterfactual brittleness (letter strings) | Humans N=136 0.753 [0.734, 0.773]; GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 (mapping moderately certain) | Lewis and Mitchell 2024 [c16, d06] | Contested |
| Webb et al. | Digit matrices N=40 OR 1.88 (p=.005). Letter strings N=57 OR 1.76. Story analogies N=54: humans better, OR 0.37 (p=.0003) | Webb 2023 [a20, c15] | Contested |
| Relation-embedding confidence predicts correctness | RelBERT avg over 7 sets: 31.1 / 45.5 / 58.7 / 71.2 by bin; GPT-4 59.5 / 60.6 / 65.0 / 72.9. SAT RelBERT 40.7 to 80.6 | [d03] | Single-source |
| Hard-bin chains | Conf <0.25: RelBERT 31.1; chains 42.1-44.5; GPT-4 59.5. Hybrids SAT 73.3-74.5 vs 73.6 (noise); U2 +2.7 to +3.6 | [d04] | Single-source |
| Sentence embeddings track topic, not analogy | Story pairs: correlate 35-53 (x100) with entity/relation similarity, 1.8-6.2 with the human analogy score; DMR 12.6; humans 67.9; ChatGPT about 30% vs humans over 85% | StoryAnalogy [d12] | Established with d08 |
| Untrained BERT near chance on analogy pairs | 0.47-0.52 on SAT/U2/U4/SCAN; FastText 0.50-0.57; SAT about 30% OOV; frequency bias | Petersen and van der Plas 2024 [d08] | Single-source |
| Several plausible relations | GPT-4o/4.1/Llama3: relational overlap 22-36% (chance 25); embedding similarity 43.9-48.4; prototypicality 47.7-52.9 | Das and Balke 2025 [d10, d11] | Single-source |
| Retrieval by shared method is hard | BRIGHT, 1,384 queries: best embedding 18.3 avg (vs 59.0 on an easier benchmark); BM25 14.5; LLM reasoning query up to +12.2 | Su et al. 2025 [d13, d14] | Single-source |
| Self-generated analogues | GSM8K retrieved vs self: davinci-003 57 (or 54) vs 61; davinci-001 11 vs 9; GPT-3.5-turbo 75.0 to 77.8 (5-shot CoT 76.7). Codeforces GPT-4 Acc@1 17 to 19, Acc@10 31 to 37 | Yasunaga 2023 [c20, d15, d16] | Single-source |
| Noisy or unfiltered analogy data | About 63% of unfiltered AnalogyKB points not analogies; KnowledgePrompts zero-shot 45.7, structured 38.3-38.8, targeted 55.25 | [c18, b25] | Established (2 sources) |
| Rare relations cost accuracy | English BATS about 80-87 vs French ALF about 50-60 (ChatGPT-4o-mini EM 84.0 vs 51.11; fastText 11.92) | Petrov 2025 [d18] | Single-source |
| Distant-domain analogies | SCAN MRR: GloVe .022, GPT-2 .057, BERT .044; BATS MRR .099-.207 | Czinczoll 2022 [c17] | Single-source |

## 4. Mechanisms and models

### 4.1 Pattern-count vector for a pair (VSM, the cheap core)
1. Choose joining patterns J (64 words such as "of", "for", "from", "in", "with", "by", "as", "than").
2. For a pair (A, B), build phrase queries "A J B" and "B J A" for each J. That gives 2|J| = 128 features.
3. Get a count for each query from a large corpus.
4. Weight with log(x + 1). Raw counts were worse [a06].
5. Take cosine against each candidate pair. Pick the highest. A question is skipped if all counts are zero.

If you use an LLM instead of a corpus, the count step becomes a model call and the vector becomes an embedding of the text "A : B" (4.5).

### 4.2 LRA: three upgrades
1. **Learned patterns.** For a list of word pairs, find short phrases starting with one word and ending with the other, with wildcard middle words. Keep the most frequent, then score pattern usefulness. LRA kept 4,000 patterns, doubled by order to 8,000 columns. 50 of the 64 hand patterns appear exactly among the learned ones (60 with wildcards) [a23].
2. **Synonym expansion.** For each word, take its top thesaurus neighbours (num_sim 10). Build alternate pairs by swapping. Keep the alternate that gives the best cosine. Dropping this step cost 6.6 points (56.1 to 49.5) and skipped questions rose from 4 to 22 [b02].
3. **SVD.** Matrix 17,232 x 8,000, density 5.8%. Truncate to k = 300. Dropping it (53.5) was not significant [a04].

Parameter sweep: recall stayed 53.5-56.1, best at num_sim 10, k 300, 4,000 patterns [b04]. The 8,000 features are not readable: you need the top 300 to match full-vector accuracy [a04].

### 4.3 Supervised pair models (PairClass, SuperSim)
Features are word-level similarity scores (several corpora, several measures) for the two stem words and the two answer words. Train a classifier on SAT-style quadruples. Extra positives come by symmetry (flip the pair, flip the order). 10-fold cross-validation. SuperSim reached 54.8% SAT in minutes [c08]. A learned combination of cheap features recovers most of LRA's accuracy.

### 4.4 Vector offsets (3CosAdd, 3CosMul, LRCos)
- 3CosAdd: d* = argmax cos(d, b - a + c), excluding a, b, c from candidates. Without the exclusion the nearest word is b in 93% of cases [a14].
- 3CosMul: multiply the shifted cosines so each term counts equally. Better than 3CosAdd for explicit vectors.
- LRCos: train a classifier on example targets of the relation, then rank candidates by classifier probability times similarity to c. 47.7% on BATS vs 28.1% for 3CosAdd [a15].
- Always run two controls: ONLY-B (return the neighbour of b) and IGNORE-A. If a control matches the method, the method does not use the relation.

### 4.5 Relation embedding from a language model (RelBERT)
Put the pair into a prompt template ("Today, I finally discovered the relation between A and B: A is the <mask> of B"). Take the hidden state at the mask. Fine-tune with a contrastive loss on a relation-labelled dataset so same-relation pairs sit close. Score each SAT choice by cosine with the stem pair. Manual prompt 69.5; AutoPrompt 61.0; P-tuning 54.0 [b21]. Confidence = min(informativeness of stem pair, informativeness of chosen pair) [d03].

### 4.6 LM scoring of analogy statements
Build "A is to B what C is to D" for each of the 5 choices. Score by perplexity or log-prob. Pick the best. Order a:b::c:d works best; templates that mix the two pairs (a:c::b:d) hurt most [a19]. Masking head/tail words shows how much is answer-prior [b26].

### 4.7 Margin for abstention
Compute cosine for all candidates. Margin = top minus runner-up. Answer if the margin is above a threshold; else abstain or escalate. Turney and Littman: +0.11 gave 59.2% precision at 11.2% recall; -0.11 (accept two guesses) gave recall 61.5% at precision 34.5% [a07]. Raw cosine scales differ across models (Freestone, Figure 1): set the threshold per model on held-out items.

### 4.8 Relation embedding chains
For items where direct embeddings have low confidence, compose relation embeddings along ConceptNet paths. On conf <0.25 items this lifted RelBERT from 31.1 to 42.1-44.5. GPT-4 there was 59.5. Hybrid routing gave 0 to +0.9 on SAT: noise [d04].

## 5. What holds up

**Holds up (established).**
- Pattern-count vectors for word pairs solve SAT analogies well above chance (47-57% vs 20%), and relational vectors clearly beat attributional word measures [a02, a03, a06]. LRA 56.4 reappears in Ushio's table [b20].
- Offset analogy accuracy is a poor measure of relational knowledge. Four groups agree: Linzen (93% b-neighbour, ONLY-B), Drozd/Gladkova (Google 80.4 to BATS 28.5), Rogers et al., Nissim et al. [a14-a16, b14, b15, c10].
- Accuracy depends on relation type and pair frequency (10.5% to 99.4%; 95.4% vs 9.2%) [a16, b17, c11].
- A prompted large LM beats LRA and word-vector methods on SAT: GPT-3 few-shot 65.2, ChatGPT 74.8-83.7, GPT-4 70.3 [a18, b24, d01]. Fine-tuned RelBERT ties GPT-4 on SAT (69.5-73.6) [b21, d01].
- General sentence embeddings model topical closeness, not analogy [d12, d08].
- Unfiltered analogy data and unfiltered external knowledge hurt [c18, b25].

**Failed replications and critiques.**
- Offsets: Levy and Goldberg found the "magic" of dense embeddings was mostly the scoring rule [a13]. Gladkova and Drozd found the 60-80% headline on Google collapses on a broader set [a15, a16].
- Webb et al. (GPT-3 above humans) vs Lewis and Mitchell (letter strings: humans 0.753, models 0.35-0.49; humans stable on permuted alphabets, models drop). Different task versions and prompts, so not a clean replication. Contested [c15, c16, d06].
- Turney's "human-level" claim: CI contains 57%; the human figure is derived, not measured [a21].
- Contamination: no test for SAT or BATS on any 2023-2026 model. The only probe was a GPT-3 completion check by Webb et al., which found no sign [d05]. The benchmark authors warn GPT-4 may have seen items [d02].

**Moderators.**
- Corpus size: 5x10^11 words 47.1 vs 5x10^10 words 38.5 for the same VSM [a04].
- Item source: LRA 61.1% on 190 official items vs 51.1% on the other 184 [b04].
- Relation type: noun-modifier per-class F from 0% to 64.3% [a22]; Google categories 10.5-99.4% [a16].
- Pair frequency: strong [b17]; BERT has a frequency bias and about 30% OOV on SAT [d08].
- Shots: 53.7 / 59.1 / 65.2 [a18]. Size: 175B about +10 over 13B.
- Language and relation novelty: English BATS 80-87 vs French ALF 50-60 [d18].
- Distance: SCAN (science, metaphor) MRR under .06 for GPT-2 and BERT [c17].

**Interventions that worked.**
- Learned patterns over fixed words (LRA vs VSM-WMTS, significant) [b02].
- Synonym expansion (+6.6) [b02].
- Supervised combination of cheap features (SuperSim 54.8 in minutes) [c08].
- More shots [a18, b24].
- Contrastive fine-tuning on relation data (RelBERT) [b21].
- Targeted knowledge in prompts (55.25 vs 45.7 zero-shot) [b25].
- LLM-written query before retrieval (up to +12.2 nDCG@10) [d14].
- Confidence gating on relation informativeness (31.1 vs 71.2 accuracy across bins) [d03].

**Interventions that did not work.**
- SVD for accuracy (not significant) [a04].
- Ensembling many weak modules on analogies (about 45%) [a08].
- Hybrid chain routing on SAT (+0 to +0.9) [d04].
- Unselected structured knowledge in the prompt (38.3-38.8 vs 45.7 zero-shot) [b25].
- Training on unchecked analogy data [c18].
- Relation-asking prompts for the strongest GPT models (marginal; helped small ones) [d11].
- Whole-text cosine retrieval of similar problems when a strong model can write its own analogues [d15].

## 6. Language models

**Verbal analogies (SAT, 374 items; chance 20, applicant average est. 57).**
- GPT-3 175B: zero-shot 53.7, one-shot 59.1, few-shot 65.2. Smallest sizes 30.5 zero-shot [a18].
- text-davinci-002 zero-shot 37.4; ChatGPT zero-shot 74.8, one-shot 83.7 [b24]. GPT-4 70.3 with a few solved examples and explanations; ChatGPT with CoT 65.8; InstructGPT003 48.9 [d01]. These come from three papers with different prompts. Gaps of 5 to 10 points between them are not comparable. The SAT 95% interval is about +/-5 points.
- Fine-tuned RelBERT 69.5-73.6 [b21, d01]. Tuned PLM scoring on full SAT: BERT 42.8, GPT-2 57.8, RoBERTa 55.8; defaults 32.6/41.4/49.6 [b20].
- Das and Balke re-ran SAT on LLaMA 2 13B/70B, GPT-3.5 and GPT-4o: only a bar chart. The text says GPT-4-class models beat people by a substantial margin; no numbers [d09].

**Other sets (Kumar and Schockaert 2023).** GPT-4: U2 71.9, U4 68.8, BATS 90.8, Google 99.0, SCAN 23.5, E-KAR 51.3. On SCAN GPT-4 is below RelBERT (27.3) and both are low [d01]. Human reference (Yuan): SAT 57.0, U2 87.5, U4 66.7, BATS 84.9, Google 99.4, E-KAR 77.8 [b24].

**What changed accuracy, by how much.**
- Shots: +5.4 (zero to one) and +6.1 (one to few) for GPT-3 on SAT [a18]. ChatGPT one-shot +8.9 over zero-shot [b24].
- Instruction tuning and scale: 37.4 (davinci-002) vs 74.8 (ChatGPT) zero-shot [b24].
- Chain of thought: ChatGPT with CoT 65.8 [d01] vs zero-shot 74.8 [b24]. Different papers, so no clear CoT effect on this task.
- Relation-embedding fine-tuning: GPT-3 zero-shot 53.7 vs RelBERT 69.5 on the same set [b21].
- Targeted knowledge in the prompt 45.7 to 55.25; broad structured knowledge 38.3-38.8 [b25].

**Artifact risk.** RoBERTa SAT 53.4 falls to 38.6 and 35.6 when the head or tail of the candidate is masked; Google 93.6 to 60.6 and 55.8 [b26]. Untrained BERT is at chance (0.47-0.52) [d08]. Encoder results partly reflect the answer word, not the relation.

**Hardness.** RelBERT confidence bins track correctness (31.1 to 71.2). GPT-4 is much flatter (59.5 to 72.9): it keeps the hard items [d03]. GPT-4 on BATS stays at 87-94 in every bin; SCAN is flat for all models (19-36).

**Brittleness.** Letter strings: GPT-3 0.488, GPT-3.5 0.350, GPT-4 0.452 vs humans 0.753; the gap grows on permuted and symbol alphabets [c16, d06]. Webb et al. found GPT-3 above humans on standard forms (OR 1.88 on digit matrices, N=40; 1.76 on letter strings, N=57) and below on story analogies (OR 0.37, p=.0003) [c15]. StoryAnalogy: ChatGPT about 30% vs over 85% for humans [d12].

**Prototype pull.** With several plausible relations, GPT-4o, GPT-4.1 and Llama 3 choose the prototypical or embedding-nearest option. Relational-overlap accuracy 22-36% (chance 25) vs 44-53% on embedding similarity and prototypicality [d10]. Asking the model to rank relations helped small models (Gemma-2B prototypicality 24.8 to 36.9), not strong ones [d11].

**Analogy in prompts (link to subfield 10).** GSM8K: davinci-003 self-generated 61 vs retrieved 57 (or 54); davinci-001 9 vs 11; GPT-3.5-turbo 75.0 to 77.8 [c20, d15]. Codeforces GPT-4 Acc@1 17 to 19, Acc@10 31 to 37 [d16]. Thought Propagation: +12% shortest path, +15% agent planning; extra calls; tasks with defined relations [d17]. No 2025-26 model tested.

**Retrieval.** Embedding retrievers drop to 18.3 nDCG@10 when the match is a shared theorem or algorithm; an LLM reasoning trace as the query gains up to 12.2 [d13, d14].

**Contamination.** Unmeasured for 2023-2026 models on SAT/U2/U4/BATS [K16]. The French ALF vs English BATS gap (about 55 vs 85) is a hint, not a test [d18].

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Do not build a text-statistics relation retriever.** A prompted strong LM beats LRA-style pipelines (65.2 to 83.7 vs 56) and LRA cost nine days. [E] K06, K04. Part: none (a "not to add" note). Ids a02, a18, b24, d01.
2. **O7 retrieval: describe the relation; do not rely on topic closeness.** General sentence embeddings track topic and entity similarity, not analogy (1.8-6.2 vs 67.9 human); embedding retrievers fail on shared-method retrieval (59.0 to 18.3). In O7 the model writes a one-line relation description of the stuck problem and code retrieves with it. [E] for "topic embeddings are not analogy embeddings" (K18, 3 sources); the gain from relation queries inside an agent is untested (U1). Part: O7, memory. Ids d12, d08, d13, d14.
3. **G: every analogy-based method gets a no-relation baseline.** ONLY-B style (answer from the target alone) and candidate-only (question hidden). ONLY-B matched the method on plurals (.70). [E] K07. Part: G3, bench design. Ids a14, b12, b14, b15.
4. **G: stratify and state the boundary.** Report analogy-based results by relation type and pair frequency (95.4 vs 9.2; 10.5 to 99.4). [E] K08. Part: G7, S9 (log the problem class). Ids a13, a16, b17, c11.
5. **G: report intervals.** Binomial 95% CI on 374 items is about +/-5. Claim no win below 5 points. [E] on the arithmetic; K05 is single-source for the "human-level" case. Part: G7. Ids a21, b04.
6. **O7: filter retrieved analogues before use.** Unfiltered analogy data was about 63% non-analogies and training on it hurt; broad knowledge in the prompt dropped accuracy (38.3-38.8 vs 45.7). Code checks the typed mapping of a retrieved analogue before it enters the prompt. [E] K13. Part: O7. Ids c18, b25.
7. **O7 stays at impasse and open mode only.** Cheap similarity is a ranker, not a judge: top-1 of 369 was 8.4%, top-10 29.5%. [S] on the numbers; consistent with the existing O7 rule. Ids a07, a10.

### Test first

1. **Relation-description query vs topic query for analogue retrieval** (O7, memory). [S] K20, indirect only. Ids d13, d14, d15, d12. UNKNOWNS U1.
2. **Margin or confidence gate on analogue choice** (G, O7). [S] K14, K17. Ids a07, d03.
3. **Self-generated vs retrieved analogue, by model strength** (O7). [S] K12. Ids c20, d15, d16.
4. **Order-flip and relation-reversal check** on the LLM judge that picks the analogue (G5). [S] K09. Ids a17, a14.
5. **Perturbed copies of any analogy test** (G3). [C] K11, K16. Ids c16, d06, d02.
6. **Cheap relation scorer first, LLM for low-confidence items.** [S] K15, K17. Ids d01, d03, d04.
7. **State the relation wanted in the retrieval query** (prototype-pull check). [S] K19. Ids d10, d11.
8. **Rare domain relations (code, lab methods).** [S] K21. Ids d18, b17, d08.

## 8. Concrete tests on our bench

All arms get the same token budget, counted including setup (G7). Use 95% binomial or bootstrap CIs. Fix item sets before running.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Held-out problems with a known solved same-structure twin in memory (ARC-like and BRAINTEASER items; 60+) | A: retrieve by embedding of the problem text. B: model writes a one-line relation description, code retrieves by it. C: no retrieval | Solve rate; precision@3 of the retrieved twin | B over A by 5+ points if relation matters; A near C for far twins |
| T2 | SAT/U2/U4/BATS plus perturbed copies (rename words, swap pair order, reword relation) | A: plain prompt. B: relation description first. C: few-shot. Same prompt length | Accuracy on original vs perturbed | Drop under 5 points: little memorisation. Drop of 10+ flags it |
| T3 | Same sets, candidate-only (question hidden) and ONLY-B-style control | Control vs full method | Accuracy above control | Full method 15+ points above control; if not, the item is an artifact |
| T4 | Analogue choice among 4-6 candidates | A: raw LLM choice. B: embedding margin, abstain below a threshold and escalate to the LLM. Threshold from a calibration split | Precision at coverage; tokens | Gate keeps precision and cuts calls; threshold is model-specific |
| T5 | 100 analogy judgments, order flip and relation reversal | Original order vs flipped order | Judgment change rate | Over 20% flips: the judge needs order averaging |
| T6 | GSM8K-style problems with a self-writable analogue | A: no analogy. B: self-generated analogue. C: retrieved solved problem. Split by model size | Accuracy | B over C by 2-4 points only on the strongest model; weak model: B not better |
| T7 | Rare domain relations (code idioms, lab methods; 40+) | A: plain. B: relation first. Per frequency stratum | Accuracy per stratum | The frequent-rare gap sizes the boundary |
| T8 | Two plausible relations (Das and Balke style, 100 items) | A: plain choice. B: "state the relation wanted" first | Relational-overlap accuracy | Small gain on weak models; none on the strongest |

## 9. What does not transfer, and why

- **Corpus-count vectors (VSM, LRA).** Our agent has no terabyte phrase-search corpus, and an LLM already holds the statistics. The corpus was the bottleneck (38.5 vs 47.1) and LRA took nine days [a04, b03].
- **SAT accuracy.** Verbal single-word pairs differ from problems or code. On SCAN (science, metaphor) scores are far lower (MRR .022-.057; GPT-4 23.5) [c17, d01].
- **"Human-level" claims.** The 57% human figure is an estimate and the CI is +/-5 [a21].
- **Offset arithmetic.** Works for frequent, morphological, capital-like relations only [b17]. Not for rare or abstract ones.
- **Static word vectors as agent state.** Frequency bias, OOV (30% on SAT) and model-specific cosine scale make thresholds unportable [d08, Freestone].
- **Letter-string and matrix puzzles.** They test rule induction and are brittle on counterfactuals [c16]. Good for robustness checks, poor for sizing retrieval gains.
- **Fine-tuned relation embeddings (RelBERT).** Need labelled relation data and a training run. Worth it only if T1 and T4 show a cheap scorer pays at equal tokens [d01].
- **SAT-style accuracy gains** do not show that retrieving an analogous solved problem improves agent solve rate. No study tests that [critique gap 1].

## 10. Open questions

1. Does relation-based retrieval of solved problems beat topic retrieval at equal tokens inside an agent? No study isolates it.
2. How much of GPT-3.5, GPT-4 and ChatGPT SAT and BATS accuracy is memorisation of public items? No contamination test exists for 2023-2026 models.
3. What do 2025-2026 frontier models score on SAT, U2, U4, BATS and SemEval-2012 Task 2 zero-shot, with intervals? The record stops at 2023 numbers without CIs; 2025 models appear only as a bar chart [d09].
4. Is the raw cosine margin a calibrated abstention signal for modern embeddings? Only a learned informativeness score has been tested [d03].
5. Do 2024-2026 embedding models still show Chen et al.'s asymmetry and SIMILAR/CONTRAST/NON-ATTRIBUTE failures? Not retested.
6. Fixed relation templates vs model-generated relation descriptions for prompts and retrieval: no direct comparison.
7. Does frequency dependence (95.4 vs 9.2) hold for LLM embeddings and for domain relations in code and science?
8. Do analogy gains survive with no gold relation (open reasoning)? AnalogyKB had 63% non-analogies [c18]; Thought Propagation's gains come from tasks with defined relations [d17].
9. Why does self-generated analogy help text-davinci-003 and not weak models, and does it help current frontier models at all? Yasunaga stops at GPT-3.5-turbo plus a small GPT-4 test.
10. Table mappings for Lewis and Mitchell (0.488/0.350/0.452), Ushio and Freestone come from garbled extractions. Re-open the tables before quoting them.

## 11. Sources

[V] opened (page or PDF text read); [M] snippet or abstract only.

1. [V] Turney (2006) Similarity of semantic relations. https://arxiv.org/abs/cs/0608100
2. [V] Turney and Littman (2005) Corpus-based learning of analogies and semantic relations. https://arxiv.org/abs/cs/0508103
3. [V] Turney (2005) Measuring semantic similarity by Latent Relational Analysis (IJCAI). https://arxiv.org/abs/cs/0508053
4. [V] Turney, Littman, Bigham, Shnayder (2003) Combining independent modules. https://arxiv.org/abs/cs/0309035
5. [V] Turney (2008) PairClass: a uniform approach to analogies, synonyms, antonyms, associations. https://arxiv.org/abs/0809.0124
6. [V] Turney (2013) Distributional semantics beyond words (SuperSim). https://arxiv.org/abs/1310.5042
7. [V] Turney and Pantel (2010) From frequency to meaning. https://arxiv.org/abs/1003.1141
8. [V] Mikolov, Chen, Corrado, Dean (2013) Efficient estimation of word representations. https://arxiv.org/abs/1301.3781
9. [V] Mikolov, Sutskever, Chen, Corrado, Dean (2013) Distributed representations of words and phrases. https://arxiv.org/abs/1310.4546
10. [V] Levy and Goldberg (2014) Linguistic regularities in sparse and explicit word representations. https://aclanthology.org/W14-1618/
11. [V] Linzen (2016) Issues in evaluating semantic spaces using word analogies. https://arxiv.org/abs/1606.07736
12. [V] Drozd, Gladkova, Matsuoka (2016) Word embeddings, analogies, and machine learning. https://aclanthology.org/C16-1332/
13. [V] Gladkova, Drozd, Matsuoka (2016) Analogy-based detection (BATS). https://aclanthology.org/N16-2002/
14. [V] Rogers, Drozd, Li (2017) The (too many) problems of analogical reasoning with word vectors. https://aclanthology.org/S17-1017/
15. [V] Chen, Peterson, Griffiths (2017) Evaluating vector-space models of analogy. https://arxiv.org/abs/1705.04416
16. [V] Ethayarajh, Duvenaud, Hirst (2019) Towards understanding linear word analogies. https://arxiv.org/abs/1810.04882
17. [M] Allen and Hospedales (2019) Analogies explained. https://arxiv.org/abs/1901.09813
18. [M] Nissim, van Noord, van der Goot (2020) Fair is better than sensational (b19: snippet, no numbers; c10 lists a read with some numbers). https://arxiv.org/abs/1905.09866
19. [V] Brown et al. (2020) Language models are few-shot learners. https://arxiv.org/abs/2005.14165
20. [V] Ushio, Espinosa-Anke, Schockaert, Camacho-Collados (2021) BERT is to NLP what AlexNet is to CV. https://arxiv.org/abs/2105.04949
21. [V] Ushio, Camacho-Collados, Schockaert (2021) Distilling relation embeddings (RelBERT). https://arxiv.org/abs/2110.15705 (the 73% journal-version figure is [M], snippet only)
22. [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
23. [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate generality of analogical reasoning. https://arxiv.org/abs/2402.08955
24. [V] Lewis and Mitchell (2024) Evaluating the robustness of analogical reasoning in LLMs. https://arxiv.org/abs/2411.14215
25. [V] Yuan et al. (2023) Analogical structure abduction (SCAR). https://arxiv.org/abs/2305.12660
26. [V] Yuan et al. (2023) AnalogyKB. https://arxiv.org/abs/2305.05994
27. [V] Wijesiriwardene et al. (2024) KnowledgePrompts. https://arxiv.org/abs/2412.00869
28. [V] Czinczoll et al. (2022) Scientific and creative analogies (SCAN). https://arxiv.org/abs/2211.15268
29. [V] Hu et al. (2023) In-context analogical reasoning. https://arxiv.org/abs/2305.17626
30. [V] Yasunaga et al. (2023/2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714
31. [V] Bhavya, Xiong, Zhai (2022) Analogy generation by prompting LLMs. https://arxiv.org/abs/2210.04186
32. [V] Kumar and Schockaert (2023) Solving hard analogy questions with relation embedding chains. https://arxiv.org/pdf/2310.12379
33. [V] Freestone and Karmaker Santu (2024) Word embeddings revisited. https://arxiv.org/pdf/2402.11094
34. [V] Petersen and van der Plas (2024) Can language models learn analogical reasoning? https://arxiv.org/pdf/2310.05597
35. [V] Das and Balke (2025) From prototypical to relational. https://aclanthology.org/2025.inlg-main.28.pdf
36. [V] Jiayang et al. (2023) StoryAnalogy. https://arxiv.org/pdf/2310.12874
37. [V] Su et al. (2025) BRIGHT. https://arxiv.org/pdf/2407.12883
38. [V] Yu, He, Ying (2024) Thought propagation. https://arxiv.org/pdf/2310.03965
39. [V] Petrov et al. (2025) ALF: fine-grained French analogy dataset. https://aclanthology.org/2025.jeptalnrecital-taln.2.pdf
