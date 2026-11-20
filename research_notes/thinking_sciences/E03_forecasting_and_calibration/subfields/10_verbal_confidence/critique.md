# Critique: Verbal confidence (E03.10), cross-check

## Re-opened this session (full PDF text, numbers grepped)
Tian 2023 (Table 1), Xiong 2024 (text and tables), Lin 2022 (Tables 1 and 4), Zhou 2024 Relying on the Unreliable, Yona 2024, Damani 2026 RLCR, Steyvers 2025. About 10 numbers confirmed.

Confirmed: Tian gpt-3.5 TriviaQA ECE 0.140 vs 0.068/0.050/0.054; SciQ 0.256 vs 0.234 (top-1) and 0.065 (top-4); TruthfulQA 0.451 vs 0.389 and 0.203. Xiong: ECE above 0.377, AUROC 62.7%, 22.2% gain, 0.522 vs 0.605, GPT-4 GSM8K 93.6% accuracy with ECE 0.064 from all-100% answers, AUROC 54.8 to 92.7 with M=5. Zhou: strengtheners 20%, weakeners 14%, 53% correct, 17% of errors, 81% reliance vs 66% correct, 73% on wrong confident answers, reward scores 4.03/0.82/-1.86. Yona: best 0.63 (GPT-4), 0.70 (Gemini Ultra). Damani: ECE 0.37 to 0.03 (HotpotQA, with analysis), 0.09 without analysis; accuracy 61.7 vs 63.0. Steyvers: N=301 (284 kept), AUC 0.751/0.746/0.781 vs 0.589/0.602/0.592.

## Corrections
1. a05 (Lin) had garbled baseline rows from table extraction. Correct Table 1 (MSE/MAD, lower better): Multi-answer: verbalized 22.0/16.4, answer logit 37.4/33.7, indirect logit 33.7/38.4, constant 34.1/31.1. Multiply-divide: verbalized 15.5/19.0, answer logit 10.4/9.4, indirect logit 11.7/7.1, constant 15.3/8.5. So verbalized wins clearly only on Multi-answer. On Multiply-divide it is WORST by MAD and by MSE (except tie with constant). Lin's "generalizes well" claim is narrower than a05/c03 suggested.
2. a07 pairs label-prob SciQ 0.256 with verbalized 0.065. 0.065 is the top-4 variant. Top-1 is 0.234. Same for TruthfulQA (top-4 0.203, top-1 0.389). The "over 50% cut" holds only for top-k prompts. Claim K02 states both.
3. a09/b07 attribute 62.7% as GPT-4 average AUROC. Confirmed in text, but the nearby table value 62.7 also appears as a LLaMA 2 cell; the text sentence is the reliable source.
4. Zhou et al. is cited as "Zhou, Hwang, Ren, Sap" in a-file and "Zhou, Jurafsky, Hashimoto" in c-file. Same paper family; authors differ between versions. Use the paper title.
5. Yona a14 said cMFG "close to 0.5"; c08 says vanilla is 0.52-0.57. Table values agree with c08.

## Contradictions
- Reasoning helps calibration (Yoon 33 of 36; Zeng AIME ECE 0.752 to 0.240) but Mei finds no change on easy tasks and Zeng finds small models' ECE rises past about 10k tokens. Marked contested.
- Tian says verbalized beats token probabilities. Kadavath says token probabilities are well calibrated for lettered options. Different formats (RLHF chat vs base model, option letters vs free text), not a true conflict.
- Xiong: white-box beats black-box only slightly (0.605 vs 0.522); Kumaran shows verbal confidence is not a read-out of log-probs. Consistent: both channels are weak.

## Weak spots
- Many claims rest on one benchmark family (TriviaQA, SciQ, GSM8K). Almost nothing on forecasting questions with real resolution.
- Cacioli 2026 (saturation) and Zeng 2025 are single, recent, possibly non-peer-reviewed preprints; not re-opened here.
- Agent-level results (AUQ, BrowseConf, Hathidara) are single-lab, baselines vary.
- Classic human numbers (a21) came from a Wikipedia summary, not the original papers. Lichtenstein 1982, Moore and Healy 2008, Wallsten 1986 (b25-b27) were not checked.
- a19 and a22 were search snippets only (opened:false).
- Exact ECE values for Kadavath are in figures only.
- Not re-opened: Kumaran, Zhao, Wang (RiskEval), Kapoor, Band, Leng, Mielke, Belem, Kim, Jang, Zeng, Mei, Cacioli, AUQ, Hathidara. Their numbers are as the evidence files record them.

## GAPS
1. Does stated confidence from a frontier 2026 model, after a scaffold with reasoning, have AUROC clearly above 0.7 on open forecasting questions that later resolve (not trivia)?
2. At equal tokens, does 5-sample agreement beat one sample with stated confidence plus verification, for failure prediction?
3. Does a fixed 5-bin verbal vocabulary with numeric anchors avoid the saturation (95%+) seen in small models, and does it hold for frontier models?
4. Does an explicit abstain/retry rule driven by stated confidence raise utility under error penalties, given that models ignore penalties (Wang 2026)?
5. Does asking confidence before versus after reasoning change ECE and AUROC (contested reasoning-model results)?
6. Do hedge words in the final answer track correctness in current models, and does forcing wording to match a calibrated number change reader reliance?
7. Does confidence calibrated on one task type transfer to another without training (Lin Multiply-divide failure; Kapoor topic transfer)?
8. Is there any prompt-only method that reproduces the RLCR gain (ECE 0.37 to 0.03), or is training required?
9. Original sources for human verbal-probability variability and overconfidence (Wallsten 1986, Lichtenstein 1982) were not read; do the numbers hold and do they apply to LLMs?

## Gap search results (evidence_d.jsonl, d01-d17)
Search tools were rate-limited (WebSearch budget spent, arXiv API and OpenAlex returned 429). Sources came from the arXiv search page, abs pages, PDFs and Crossref. Full text read for 2606.29490, 2610.25846, 2605.06308, 2604.13271, 2603.25052, 2609.32470, 2508.14390, 2510.24505, 2607.20526, 2402.18563. Others abstract only.

1. OPEN (partly informed). No paper found that measures AUROC of stated confidence from a 2026 frontier model on later-resolving forecasting questions. Halawi 2024 (Brier .179 vs crowd .149) and ForecastBench show forecasts need retrieval and ensembling. On closed benchmarks frontier verbal AUROC is 0.58-0.79 (Boubnovski, d07), only 3 of 6 settings above 0.7. Claim K16 marked open.
2. PARTLY CLOSED. Agreement beats one stated confidence in small models (Ghosh: resolution 0.0637 vs 0.0316, Brier .1465 vs .1713) and a trace-judged K=4 score beats SC@8 on Gemini 3.1 Pro and Claude Sonnet 4.6 (AUC 0.78 vs 0.71) at about half the cost of SC@10. The exact test (5 samples vs 1 sample plus verification at equal tokens) is not in the literature found. K04 now established.
3. PARTLY CLOSED. Saturation confirmed for open 0.5-8B and reasoning models (under 5% of responses below 0.5; 13,121 of 15,000 at 90+). Frontier models in ConfidenceBench are not saturated (Brier 0.103). No test of a fixed 5-bin numeric-anchored vocabulary found; Ghosh shows formats correlate poorly (-0.07 to +0.25). K05 now contested.
4. OPEN. Kumaran 2026: stated confidence predicts the model own abstain choice better than correctness (median AUROC gap +0.16). No study of utility under priced error penalties beyond Wang 2026 (c22, not re-opened). K10 remains single-source.
5. PARTLY CLOSED. Separate blind rating pass beats same-prompt confidence in Gemma-3 (ECE gains 17-88%), and same-prompt reasoning contaminates the confidence direction in open 7B models (cosine +0.26 to -0.63). No before-versus-after test on frontier reasoning models. K18 single-source.
6. OPEN. No new evidence on hedge words or forced wording-number matching beyond a-file Zhou and Kim.
7. PARTLY CLOSED (negative). Fine-tuned confidence degrades out-of-distribution; critique training gives small gains (CritiCal). No prompt-only transfer test. K20 single-source.
8. PARTLY CLOSED. Prompt-only methods cut ECE (REHEARSE 58% average, Twin-Pass up to 88%) but do not lead on AUROC and none matches RLCR on a like-for-like basis. RL calibration rewards can also be hacked. K19 contested.
9. OPEN. DTIC PDFs for Lichtenstein 1982 (ADA101986) and Wallsten 1986 (ADA196944) were blocked. Only the Moore and Healy 2008 abstract was read. K13 and the human numbers stay unverified.

Caveats on new sources: nearly all are 2026 preprints, many single-lab; Ghosh and Wang use 0.5-8B open models; ConfidenceBench is a 200-item private set; Kumaran is single-author. Treat as leads, not settled facts.
