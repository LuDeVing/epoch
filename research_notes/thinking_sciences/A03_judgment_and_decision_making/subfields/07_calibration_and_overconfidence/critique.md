# Cross-check: Calibration and overconfidence (A03.07)

Checker pass. Sources re-opened this session as PDF text (arXiv): Xiong 2306.13063, Tian 2305.14975, Lin 2205.14334, Guo 1706.04599, Steyvers 2401.13835, Zhou 2302.13439, Schoenegger 2402.19379, Halawi 2402.18563, and Moore and Healy 2008 (archived PDF). 28 claims written to claims.jsonl.

## Numbers re-checked (10)
1. Xiong: GPT-4 AUROC 62.7%, mean ECE above 0.377, ECE 0.064 at 93.6% accuracy by saying 100%, 0.522 to 0.605 white/black gap, ECE as low as 0.028. All confirmed.
2. Xiong: GSM8K AUROC 54.8% to 92.7%. Confirmed in the text. Label problem: in Table 3 the 92.7 sits on the "Prompt (M=5)" row (Self-Random is 88.6), but the appendix labels 92.7 "Self-Random+Consistency (M=5)" and 88.6 "Misleading+Cons". The value is solid, the row name is not. The 54.8 baseline is the M=1 CoT row in the appendix and the text calls it "akin to random guessing". It is one model (GPT-3.5) on one arithmetic set.
3. Tian gpt-3.5 (Table 1): label prob ECE .140/.256/.451; top-4 verbalized .054/.065/.203; top-1 .068/.234/.389; 2S CoT .110/.323/.419; AUC .869 vs .896 on TriviaQA. Confirmed.
4. Tian GPT-4 (Table 2): label .078/.219/.445; top-1 .024/.201/.350; top-4 .041/.056/.198; TruthfulQA AUC .462 vs .622 (c08 says "0.62"; fine). Confirmed. Claude-1 numbers in a21 confirmed. b15 says "Claude 2" for the third model; the Table 3 caption says Claude-1 (footnote cites Claude 2 model card). Minor labelling error in b15.
5. Lin Table 1: the extracted layout is garbled, which is why a19 and b12 disagree. Reading the row order, the correct values are: verbalized finetune 22.0/16.4 (Multi-answer), 15.5/19.0 (Multiply-divide); zero-shot answer logit 37.4/33.7 and 10.4/9.4; indirect logit 33.7/38.4 and 11.7/7.1; constant 34.1/31.1 and 15.3/8.5. c06 is right. CORRECTION: a19 wrongly calls 22.0/16.4 "indirect logit" and quotes constant baseline 33.7/38.4; b12 wrongly gives indirect logit 22.0 and constant 37.4/11.7. Appendix Table 4 (verbalized numbers EV 22.0/16.4, 15.5/19.0) supports c06. Consequence: verbalized confidence wins under the Multi-answer shift but on Multiply-divide its MSE (15.5) is no better than a constant (15.3) and worse than the zero-shot logit (10.4). (Row identity depends on layout inference; mark medium confidence.)
6. Guo: CIFAR-100 ResNet-110 16.53% to 1.26%; Birds ResNet-50 9.19% to 1.85% (matrix scaling 21.13%); CIFAR-10 LeNet 3.02% to 0.93%. Confirmed. CIFAR-10 ResNet-110 4.6% to 0.83% not re-seen.
7. Steyvers: 301 participants, 350 questions, accuracy 55% and 50%, AUC .751/.746/.781 vs .589/.602/.592. Confirmed. CORRECTIONS: a25 says "GPT-4o mini"; the text says GPT-4o. The 350 questions were sampled across model-confidence levels, not random, which matters for any claim about base rates.
8. Zhou: 21 of 28 "100%" templates lower than "90%"; 57% correct after "I'm 90% sure" with ECE 0.30-0.50; 7% drop; over 80% spread. Confirmed. Note that the 57% result is in the paper's section on real-text (corpus) analysis of "I'm 90% sure"-type phrases as well as the prompt experiments; do not read it as a clean calibration test.
9. Moore and Healy: 90.5% confidence vs 73.1% hit rate; hit rates 55.1% / 85.6% / 84.4% by phase. Confirmed.
10. Schoenegger: Brier 0.20 (SD .12) vs 0.19 (SD .19), t(60)=0.19, p=.850, 925 humans, 31 questions. Halawi: 0.179 vs 0.149 test, 71.5% vs 77.0%. Confirmed. Halawi's 0.199 vs 0.246 mid-range figure not re-found.

## Contradictions between sources
- Kadavath says base models are well calibrated on logits and RLHF is fixed by T=2.5. Tian says logits from RLHF chat models are poor and verbalized beats them. Leng 2025 says RLHF itself causes verbalized overconfidence. Not truly contradictory (different models, formats), but there is no study testing all three on one modern model.
- Tian: verbalized ECE good. Xiong: verbalized ECE above 0.377 for GPT-3, GPT-3.5, Vicuna. Tian used one-stage top-k prompts on easy trivia; Xiong used plain prompts on 8 mixed tasks. The ECE gap is a prompt and dataset effect.
- Xiong reports a ranking problem hiding behind low ECE (constant 100% gets 0.064). Tian's ECE gains come with small AUC gains, so ECE-only reading is misleading in both.
- Overprecision: Moore and Healy say it is the robust form; Li-Hale-Moore 2025 says different precision measures correlate only r=.11. So "overprecision" as one trait is itself weak.
- Hard-easy: a08 (Plous) treats it as a real effect; b06 (Merkle) shows it follows from noise. Both stand; the mechanism claim does not.

## Weak spots
- Founding Fischhoff 1977 and Gigerenzer 1991 and Juslin 1994 and Brenner 1996 were not opened. The central dispute (does representative sampling remove overconfidence?) is therefore unresolved here (claim K11 is "contested").
- Koriat 1980 table values were not recovered; only the narrative and correlations.
- Plous figures are second-hand; Wikipedia figures (Alpert and Raiffa 50%, Adams 1960) are encyclopedia-level.
- Most LLM evidence is 2022-2023 models (GPT-3, gpt-3.5, Claude-1, LLaMA-2). Almost nothing on 2025-2026 frontier chat or reasoning models except Yoon 2025 and the 2026 Kale preprint.
- Agreement-based confidence has only been tested on QA and arithmetic. No study here tests it inside an agent loop with tools.
- Samples from one model are correlated, so agreement can be confidently wrong (Xiong notes this; no measured rate).
- Kale (arXiv 2607.07626) and DINCO are single preprints; not independently replicated.

## Seen only in snippets or abstracts
a10 (Fischhoff 1977), a12 (Gigerenzer), a13 (Juslin), a14 and b25 (Moore and Healy Bayesian version), c23 (Tao 2025), c24 (Mielke 2022), c27 (DeepConf). b17/c12 Kuhn: exact AUROC values never extracted. a24/b16/c19 Kapoor: tables not read. c13 Wang and c14 Chen-Mueller figures not re-opened.

## GAPS
1. Does agreement across N independent samples still beat verbalized confidence for current frontier and reasoning models (2025-2026), at equal tokens, and where does the gain flatten (N=3, 5, 9)?
2. How often is sample agreement confidently wrong (correlated errors from one model), and does varying prompt framing or persona across samples reduce this?
3. Does representative-sampling really remove overconfidence for LLMs (Gigerenzer/Juslin dispute): how large is the gap on random draws from a real task mix versus hand-picked hard sets?
4. Does a "strongest counter-case" step (Koriat 1980) improve LLM calibration over no step and over a balanced pro/con step, at equal tokens, measured by AUROC and not only ECE?
5. Is post-attempt confidence (after checks, tests, tool use) better than pre-attempt confidence in an agent loop, and how much of the gain comes from test results versus reflection?
6. How much outcome feedback in context (examples of graded past runs, per task class) is needed before an LLM's stated confidence is usable, and does it transfer to a new task class (Lichtenstein-Fischhoff training failed to transfer in humans)?
7. Do ordinal verbal levels beat 0-100 numbers for frontier models (Tao 2025 abstract), and what is the best number of levels?
8. What are the exact original numbers from Fischhoff-Slovic-Lichtenstein 1977 and Koriat 1980 Table results (N, hit rates per bin) to use as human baselines?
9. How does a certainty phrase in the user's message (anchoring) affect current chat models' accuracy and stated confidence; does S1 input stripping recover the loss?
10. Can a cheap one-parameter recalibration (Guo-style temperature on logged outcomes) fitted in code transfer across task classes, or must it be refit per class (Li-Hale-Moore suggests per class)?

## Gap search results (evidence_d.jsonl, d01-d17; claims K29-K36 added)

Sources opened as PDF text this pass: Del 2603.19118, Ding 2607.08065, Denisov-Blanch 2603.06612, Upravitelev 2603.22103, Kaddour 2602.06948, Barkan 2512.24661, Michael 2605.23909, Sicilia 2410.14746, Tao 2505.23854, Jin 2608.07419, plus the Koriat 1980 text already on disk. The arXiv API returned 429, so six WebSearch calls were used for discovery.

Closed or mostly closed:
- Gap 1 (sampling vs verbalized, 2025-2026): mostly closed for reasoning models. Verbalized confidence beats self-consistency at equal K and the hybrid beats both (d01, d02). The knee is K=2 for the hybrid and about K=5 for averaged stated confidence outside maths. Caveat: open mid-size models, no frontier closed models, and tokens are matched only per sample count.
- Gap 2 (correlated errors): closed in direction. Same-model agreement is often confidently wrong (d03, d04), errors are correlated across families (d05), and 87% three-model agreement was only 13% correct on agent tasks (d09). Persona variation helps only a little (d06, different task, no AUROC). Prompt reframing changed agreement more than personas did.

Partly closed:
- Gap 4 (counter-case): the "find bugs" step cut ECE on 3 of 3 models and raised AUROC for 2 of 3 (d08). No pro/con arm or equal-token control, so the Koriat comparison is not yet done.
- Gap 5 (post-attempt vs pre-attempt): reflection without test results did not beat pre-attempt (d07) and mid-run confidence got worse for Claude models (d11). Test results versus reflection were never separated. K25 changed to contested.
- Gap 6 (feedback in context): 8 outcomes in the same task class did not make confidence usable (d10). No transfer test, no dose curve.
- Gap 8 (human baselines): Koriat 1980 design and N confirmed (d16). Per-bin hit rates sit in image tables and were not read. Fischhoff 1977 still unopened.
- Gap 9 (certainty phrase): user confidence on a wrong suggestion moves accuracy 21-45 points in 2024 open models and hedging helps larger ones (d14). Not a frontier model test and stripping untested.

Still open:
- Gap 3 (representative sampling): the 2026 Michael et al. study shows 88% vs 79% and a hard-easy pattern (d12, d13), but with benchmark sets, not random draws. Gigerenzer 1991, Juslin 1994 and Brenner 1996 remain unopened. K11 stays contested.
- Gap 7 (ordinal levels): Tao 2025 is now opened and tests hedge words scored by a judge, not a few fixed levels. K27 reworded. No study sweeps the number of levels (d15).
- Gap 10 (recalibration transfer): no direct measurement (d17 only asserts it). Keep per-class refit as the default.

Corrections to earlier notes: K27 "ordinal levels" overstated what Tao tested. Search-snippet claims about 2608.18795 and 2607.10139 were not opened in full and are not used as evidence.
