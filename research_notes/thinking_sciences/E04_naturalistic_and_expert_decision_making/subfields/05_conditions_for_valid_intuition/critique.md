# Critique: E04.05 Conditions for valid intuition (cross-check)

Scope: evidence_a, evidence_b, evidence_c (82 lines). Claims in claims.jsonl (K01-K18).
Sources re-opened this session (PDF text under D:/research_scratch/E04.05, to be deleted): Kuncel 2013, Aegisdottir 2006, K&K 2009, Tetlock 2014, Huang 2023, Tian 2023, Lacombe 2025 (arXiv 2508.15050), ReASC (arXiv 2601.02970).

## Numbers re-checked (10 and more)
Confirmed:
1. Kuncel 2013: 25 samples in 17 studies; 2,263 mechanical and 2,027 clinical worker predictions; job performance .44 vs .28; advancement .42 vs .36; training .31 vs .16; GPA .58 vs .48; 25% fewer correct hires at the stated selection ratio. Confirmed.
2. Aegisdottir 2006: 67 studies, 92 effects; 69 studies and 173 effects with Goldberg and Oskamp; strict set 41 studies, 48 effects; 25 (52%) favour statistical, 18 (38%) no difference, 5 (10%) clinical. More than 35,000 articles, 4,617 coded, 1,135 met inclusion. Confirmed.
3. K&K 2009 reading of Grove 2000: 136 studies, mechanical better 63, tie 65, clinical better 8. Confirmed in K&K text. Note K&K say Grove excluded non-human outcomes (horse races, weather). The b12 range "mechanical clearly better in 33-47%, clinical 6-16%" is consistent (63/136 = 46%, 8/136 = 6%).
4. K&K: chess masters 50,000-100,000 patterns, 10,000 hours; anchoring expected gap $35,000; bat-and-ball about 50% error at top schools vs 90% at less selective schools. Confirmed.
5. Tetlock 2014: 86.2% right side of 50/50; beat control mean by 60% and other teams by 40%; recruitment about 10%, debiasing training about 10%. Confirmed. Caution: 86.2% is a direction-of-forecast rate, not a Brier gain.
6. Huang 2023: oracle GSM8K GPT-3.5 75.9 to 84.3, GPT-4 95.5 to 97.5; intrinsic round 2 (5 calls) GPT-4 GSM8K 89.0, CSQA 80.0, HotpotQA 43.0; GPT-3.5 74.7 / 41.8 / 25.0. Confirmed (table text garbled in extraction; read by column order).
7. Tian 2023: GPT-4 TruthfulQA label-prob ECE .445, best verbalised .082 with AUC .632; ChatGPT label-prob ECE .451; TriviaQA GPT-4 .078 to .024. Confirmed.
8. ReASC: GSM8K Gemma-3-4B SC k=16 92.12 at 32.67 TF; ReASC offline 92.04 at 9.45 TF (-71.1%); stage-1 accept 51.18% at 97.78% accuracy (offline), 33.28% at 98.41% (online). Confirmed.
9. Lacombe 2025: accuracy 41.7% single step, peak 45.0%, 35.7% at 768 tokens, 41.7% at 24,576; overconfidence reaching +21.3% on the IPCC dataset; search model 89.3% vs 48.7% reasoning. Confirmed.

Corrections and clarifications:
- a23 said the TruthfulQA AUC of most confidence methods stays in about 0.2-0.55. That holds for ChatGPT and Claude but GPT-4 reaches .63 (c05 has it right). Use c05.
- a15 writes d+ = -.12 and b10 writes d+ = .12 for the same result. Same size; sign is a coding convention (negative = statistical better). Claims use the magnitude.
- c08 labels the dataset ClimateX; the paper text calls the same curve the IPCC dataset. Treat as the same data.
- ReASC headline -71.1% is against SC k=16; against earlier adaptive baselines (ESC, ASC) the saving is smaller (ASC -62.5%). Added to K15.
- Kadavath (a22, b22, c03) was cited with some figures only from the abstract; not re-opened beyond the downloaded text for numbers. No number is used in a claim from it.

## Contradictions between sources
- Verbalised confidence: Tian (better than token probability, ECE halved) vs Xiong (overconfident, clustered at 80-100%, GPT-4 AUROC 62.7%). Differences are metric (ECE vs AUROC), model and dataset. Both can be true: calibration on average, little discrimination per item. Kept together as K11 (contested).
- Reasoning models vs thinking budget: Michael 2026 says reasoning models are far better calibrated (ECE .037 vs .150) while Lacombe 2025 and Gema 2025 say more tokens can worsen calibration. Different manipulations (model type vs budget on one model). Unresolved.
- Familiarity: K&K say practice with feedback is what builds valid intuition; Aegisdottir finds clinicians no better on familiar-setting data. Those studies lack feedback, which fits K&K, but nobody tested it directly.
- Klein vs Kahneman on how often experts overreach is left open by K&K themselves.
- Mellers 2015 (stable superforecasters) vs a 2025 reanalysis seen only as a snippet; a small replication (Katsagounos) supports identification but weakly supports training.
- Fast diagnosis is correct more often (b18) vs the standard hope that slowing helps; b18's bias induction failed, so neither side is tested.

## Weak spots
- The core rule (two conditions) comes from one position paper; the independent support is a book review of Hogarth. No quantified thresholds for "adequate practice" or "rapid feedback".
- Meehl, Goldberg, Karelaia and Hogarth 2001 and Shanteau 1992 were never opened; claims leaning on them are single-source or via K&K.
- Grove 2000 itself was not opened; only K&K's and citing papers' reading.
- Clinical-vs-actuarial studies are mostly humans and a few cues; transfer to an LLM agent with free text is argued, not shown. Copus (c24) suggests an LLM can beat an actuarial baseline in one parole task, abstract only, versions disagree.
- Almost no source tests a track-record gate on an LLM agent. K01 and K07 are the core ideas and have no direct LLM evidence.
- Agreement-based early exit evidence is math-heavy (GSM8K); non-math is thin.
- Router/CoT results use 7-8B models and own-data training.

## Seen only in snippets or abstracts
a18, a19, a20 (not opened); b12, b16, c03, c10, c13, c19, c20, c24, c26, c27, c28, c29 (abstract, snippet or summary only). Their numbers should not be cited without a re-open.

## GAPS
1. How many cases and what hit-rate floor make a task-class record trustworthy enough to skip deliberation (no source gives thresholds)? Look for sequential-testing or calibration-sample-size work on LLM selective prediction.
2. Does an outcome-based task-class hit rate predict first-answer correctness better than verbalised confidence or sample agreement, at equal tokens, for an LLM agent? No direct test found.
3. How does an agent judge "validity" of a new task class before it has feedback (K&K say this is hard; Tetlock needed 15 years)? Find work on estimating cue validity or predictability from a handful of cases.
4. How much of the formula edge survives when the agent itself fills the rubric (LLM as cue-reader plus fixed combination)? Look for LLM-as-feature-extractor plus linear model studies.
5. What does feedback delay or ambiguity do to LLM in-context learning of a task class (the K&K "rapid and unequivocal" condition)? Any experiments with delayed or noisy labels.
6. Is there replicated evidence that checking an intuition (premortem, slow second look) improves outcomes in humans? K&K cite none; a12 has no outcome data.
7. Do reasoning-mode vs direct-mode choices follow task validity in practice (CoT hurts implicit learning)? Need a per-task-class map for current frontier models, not 2024 models.
8. Superforecaster persistence: what does the 2025 reanalysis of Mellers et al. actually conclude, and does the ability effect survive controls?
9. Noise: how large is the within-agent disagreement on identical items for current models, and does decomposition (Noise book remedy) reduce it? No LLM study found.
10. Anomaly detection: how well can an agent detect that an item is out of its task class (the Klein defence), and what is the false-alarm cost?


## Gap search results

Scope note. Web search quota was exhausted at the start, and arXiv search, Semantic Scholar and OpenAlex returned rate-limit errors, so I could not search for new sources. I opened papers by direct arXiv link plus two abstract pages. Evidence is in `evidence_d.jsonl` (d01-d15). New claims K19-K24; K10 moved to contested; K02, K08, K11, K15, K16 got extra evidence ids.

1. Sample size and hit-rate floor. PARTLY CLOSED. Kapoor 2024: about 1000 graded examples beat simple baselines, and gains flatten after about 5000 (fine-tuned 7B models, MMLU). No sequential-test threshold for skipping deliberation was found. Open for scaffold-only agents.
2. Outcome-based hit rate vs verbal confidence vs sample agreement at equal tokens. STILL OPEN. Kapoor gives a three-way comparison, but with a trained correctness classifier rather than a per-class hit rate, and without equal tokens. Sampling agreement discriminated very weakly there, which is a warning for K15.
3. Validity of a new class with no feedback. STILL OPEN. Only people-based proxies (r about 0.20, abstract only).
4. LLM as cue reader plus fixed rule. NOT SEARCHED (no search quota). Open.
5. Delayed, sparse or ambiguous labels. PARTLY CLOSED. Random labels cost 0-5% on classification (Min 2022); noise hurts clearly on generation (Gao 2024). Delay was not tested by any source I could reach.
6. Premortem or slow second look improves outcomes in humans. NOT REACHED (no search quota). Open.
7. Mode choice by task validity for current models. PARTLY CLOSED. A complexity map exists (Shojaee 2025, contested by rebuttals I did not open); no map by cue validity.
8. 2025 reanalysis of Mellers et al. CLOSED at abstract level. It is a Psychological Science item-response-theory reanalysis: teaming and training effects shrank, vanished or reversed after controls. It does not directly test persistence of superforecaster skill. Full text not read, so K10 is now contested, not refuted.
9. Within-agent noise on identical items. PARTLY CLOSED. Atil 2025: up to 15% accuracy change across runs at temperature 0, task dependent. No test of whether decomposing the judgment reduces it. Open.
10. Out-of-class detection and false-alarm cost. PARTLY CLOSED on detection, OPEN on cost. R-Tuning and Kapoor show trained signals transfer; the abstention survey says out-of-distribution abstention is weak. No false-alarm cost figures.

Not opened: the Apple-paper rebuttals, the full 2025 reanalysis, Brahman et al. 2024. Evidence lines d11, d12 and d14 rest on abstracts or survey text only.
