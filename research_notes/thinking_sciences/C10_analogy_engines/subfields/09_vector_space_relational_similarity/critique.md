# C10.09 Vector-space relational similarity: cross-check critique

## Corrections made (sources re-opened this session: Turney 2006, Turney and Littman 2005, Linzen 2016, Ethayarajh 2019, Ushio 2021, Ushio 2021b RelBERT, Lewis and Mitchell 2024, Brown 2020)
1. c03 says VSM-AV 5-class noun-modifier accuracy was "43.3% (260/600)". Wrong. 43.3% (260/600) is the always-majority-class baseline. VSM-AV got 45.7% (274/600). a05/b05/a22 are right.
2. c04 gives VSM-AV 30-class F as 27.9. In Turney 2006 Table 20, 27.9 is recall; F is 26.8 (macro 26.5). Small, but do not cite 27.9 as F.
3. a14 says Linzen IGNORE-A was .41/.29/.36. Table 2 gives .41/.29/.26 (b12 is right). ONLY-B .42/.36/.33 is right.
4. a19 lists FastText about 57.8 on full SAT. Table 4 order is LRA 56.4, FastText 49.7, GloVe 48.9, word2vec 42.8 (b20 right). The 57.8 is a tuned LM-row cell, not FastText.
5. a19 "BERT up to 56.9, GPT-2 66.7, RoBERTa 68.1" are averages over five datasets in Table 3, which is scored on the SAT test split, not full SAT. Do not mix with the 374-item numbers.
6. a02 note "Veale 42.8%" and a11 "43%" are the same figure rounded. Fine.
7. SUBFIELDS says "via Wikipedia". Confirmed false: LRA used the Waterloo web corpus (about 5x10^10 words); Wikipedia appears only in Ethayarajh's frequency counts.
8. Confirmed unchanged: LRA 210/160/4, precision 56.8, recall 56.1, F 56.5; VSM-AV 176/193/5, 47.1; VSM-WMTS 144/196/34, 38.5; 17,232 x 8,000 matrix; almost nine days; 190 official items 61.1% vs 51.1% on 184; LRA 30-class 39.8% (239/600), 5-class 58.0% (348/600); Brown GPT-3 53.7/59.1/65.2; Ethayarajh 95.4% vs 9.2%; Linzen 93%; RelBERT 69.5/70.6/66.2; Lewis and Mitchell subject count 136.

## Contradictions between sources
- LRA SAT score appears as 56.1 recall (journal 2006), 56.4 (2005 conference version and Ushio's table), 56.8 (precision). Same system, different metric. Cite as "about 56%".
- 2005 conference LRA paper reports VSM-AV 47.3 and VSM-WMTS 40.3 (F); 2006 journal gives 47.4 and 40.3 F and 38.5 recall. Metric mixing, not disagreement.
- Webb et al. 2023 (GPT-3 above humans) versus Lewis and Mitchell 2024 (drops on counterfactual versions; humans stable). Different task versions, so partly reconcilable. Marked contested.
- Ushio 2021: fine-tuned LMs near or below LRA on full SAT, but GPT-3 few-shot (65.2) and ChatGPT (74.8, 83.7 one-shot in SCAR) well above. Prompt format, example count and the SAT-contamination risk differ.
- Levy and Goldberg 2014: explicit sparse vectors match embeddings with 3CosMul (Google 68.24 vs 66.72). This supports Turney's count-vector idea but also says the "embedding magic" is mostly the scoring rule.

## Weak spots
- Most founding numbers rest on one 374-item set; 95% interval about +/-5 points. Differences below that (LRA vs SuperSim 54.8, PairClass 52.1) are not resolved.
- Human 57% is an estimate, not a measured sample on these items.
- SAT items are public and probably in LLM training data. No source tested contamination for GPT-3, ChatGPT or Webb's 374-item set.
- Lewis and Mitchell table 0.753/0.488/0.350/0.452: pdftotext shifted the row labels. The human 0.753 is consistent with the text, but the mapping of 0.488/0.350/0.452 to GPT-3/3.5/4 comes from a garbled table and is only moderately certain.
- Ushio Table 3/4 columns are partly garbled; tuned-row mapping not fully recoverable.
- Nothing here tests a scaffold that uses vector similarity for retrieval inside an agent. All agent-relevance lines are inferences.

## Only seen in snippets or abstract
- b18 Allen and Hospedales 2019 (abstract only), b19 Nissim et al. (no numbers; c10 has some).
- b21 note that a journal RelBERT version reports 73% on SAT: snippet only.

## GAPS (most decision-relevant first)
1. Does retrieving analogous solved problems by embedding of the relation (not topic) improve an LLM agent at equal tokens versus topic-similarity retrieval? No study isolates this.
2. How much of GPT-3.5/4/ChatGPT SAT and BATS accuracy is memorisation of public items? Needed: a contamination test on 2024-2026 models with fresh or perturbed items.
3. What do 2025-2026 frontier models score on SAT, U2, U4, BATS and SemEval-2012 Task 2 zero-shot, with CIs? The record here stops at GPT-3.5/ChatGPT-era numbers.
4. Is cosine margin between candidate analogues a calibrated abstention signal for LLM embeddings (as it was for VSM: 59.2% precision at 11.2% recall)?
5. Do modern sentence-embedding models handle relation similarity with asymmetry and the SIMILAR/CONTRAST/NON-ATTRIBUTE failures shown by Chen et al. 2017?
6. Does the fixed-pattern versus learned-pattern lesson (64 vs 4,000 patterns) carry over to prompting: fixed analogy templates versus model-generated relation descriptions?
7. Frequency dependence (95.4% vs 9.2%): does it hold for LLM embeddings and for rare domain relations in a real agent task (code, science)?
8. Do analogy-retrieval gains survive in domains with no gold relation (open reasoning), where AnalogyKB found about 63% of automatic pairs were not analogies?
9. Why does self-generated analogy help text-davinci-003 but not weak models, and does it help current strong models at all (Yasunaga 2023 stops at GPT-3.5-turbo)?

## Gap search results (evidence_d.jsonl, d01-d18; claims K15-K21 added)
Method: 18 papers' PDFs opened and read (Kumar and Schockaert 2023, Webb 2023 supplement, Lewis and Mitchell 2024, Freestone 2024, Petersen and van der Plas 2024, Das and Balke 2025, StoryAnalogy, BRIGHT, Yasunaga 2024, Thought Propagation, ALF 2025). Only one WebSearch returned results (budget exhausted); arXiv API was rate-limited, so coverage is limited to papers I could name.

1. Relation vs topic retrieval at equal tokens: STILL OPEN. Indirect support only: BRIGHT (embedding retrievers fall 59.0 to 18.3 nDCG@10 when the match is shared theorem or algorithm; LLM-written query beats them), StoryAnalogy (embeddings fit literal not analogical similarity), Yasunaga (cosine-retrieved exemplars lose to self-generated on strong models). No study compares a relation embedding against a topic embedding inside an agent.
2. Contamination of SAT/BATS: STILL OPEN. Only the 2022 GPT-3 completion probe (Webb S3) and a "may have seen it" warning from Kumar and Schockaert. Perturbation evidence exists only for letter strings (Lewis and Mitchell). ALF vs BATS (about 85 vs 55) is a hint, not a test.
3. 2025-26 frontier scores: PARTLY CLOSED. GPT-4 (2023): SAT 70.3, U2 71.9, U4 68.8, BATS 90.8 (no CIs; SAT 374 items gives about +/-4.6). 2025 GPT-4o/4.1 exist only as a bar chart or other task. Still missing: any model after mid-2025, SemEval-2012 Task 2, and intervals.
4. Cosine margin as abstention signal: PARTLY CLOSED for relation embeddings. RelBERT informativeness-based confidence separates easy from hard (31.1% to 71.2% average accuracy; GPT-4 also tracks it, 59.5 to 72.9). Not the raw cosine margin, and no precision/recall at a threshold. Raw cosine scale differs between models (Freestone Figure 1), so thresholds must be set per model.
5. Modern embeddings vs Chen et al. 2017 failures: PARTLY CLOSED. StoryAnalogy shows OpenAI-ada and SimCSE track literal similarity, not analogy (1.8-6.2 vs 67.9 human, x100). Asymmetry, SIMILAR/CONTRAST/NON-ATTRIBUTE were not retested on 2024-26 embeddings.
6. Fixed vs generated relation templates: STILL OPEN, weak hints. Relation-asking prompts help weak models, not GPT-4-class (Das and Balke); LLM-written retrieval queries beat plain queries (BRIGHT). No direct fixed vs generated comparison.
7. Frequency dependence for LLM embeddings and rare domain relations: PARTLY CLOSED. BERT cosine has a frequency/OOV bias (Petersen); rarer French relations cost about 30 points (ALF). Nothing on code or science relations.
8. Gains without a gold relation: STILL OPEN. Das and Balke show models default to the prototypical option when relations compete; Thought Propagation gains come from tasks with a defined relation.
9. Self-generated analogy and model strength: PARTLY CLOSED. Mechanism as stated by Yasunaga (needs recall ability); GPT-4 on Codeforces gains +2 Acc@1 and +6 Acc@10 (small set, no CIs). No 2025-26 test.

Corrections and cautions from this pass:
- Yasunaga Table 4 extraction is scrambled: retrieved CoT on davinci-003 is 54 or 57 (K12 says 57; d15 flags 54). Treat the 4-7 point gap as uncertain.
- Freestone Table 1 row labels are shifted; the ADA/PaLM/LLaMA mapping in d07 is inferred from the text ranking, not read.
- Das and Balke's text says LLaMA-2 70B 22.1 to 31.1, which matches the table row labelled Llama3 70B. Label inconsistency in the paper or extraction.
- Lewis and Mitchell mapping (0.488/0.350/0.452 to GPT-3/3.5/4) is still unresolved; the task is letter strings, not verbal analogy.
- IWCS 2025 (Li and Venant, lexical functions) was only skimmed, not used.
