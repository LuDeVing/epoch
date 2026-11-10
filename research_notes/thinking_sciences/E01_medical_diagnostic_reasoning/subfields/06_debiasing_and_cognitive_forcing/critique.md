# E01.06 Debiasing and cognitive forcing: cross-check critique

Cross-checker pass over evidence_a, evidence_b, evidence_c (81 lines). 26 claims written to claims.jsonl (K01-K26).

## Numbers re-opened (source text or abstract read this session)

Confirmed unchanged:
1. Sherbino 2014 (PubMed 24423999 abstract): n=191 (145 vs 46); 52% vs 48% (p=0.91); 54% vs 48% (p=0.13); false-positive 64% vs 77% (p=0.12); availability 45% vs 45% (p=0.98). Students, not residents.
2. Norman 2014 (PubMed 24362377): 44.5% vs 45.0%; 69 s vs 89 s; wrong cases 17 s longer; n=96 and 108.
3. Mamede 2020 (PMC7362774): 0.40 vs 0.24, diff 0.16 (0.05-0.27), p=0.004; unbiased 0.36 vs 0.41, p=0.45; n=91.
4. Staal 2022 (PMC9685706): 29 studies, 2732 people, I2 70% to 38%, g=0.20 (0.10-0.29). The overall g=0.28 (0.14-0.43) is not in the abstract and was not re-seen.
5. Sibbald 2019 (PubMed 30694452): n=61 (40 + 21), 20 ECGs, no checklist beat control, F=96.9 for bias-built ECGs.
6. Goh 2024 (PMC11519755): 50 physicians, 76% vs 74%, difference 2 points (-4 to 8), p=.60.
7. Ke 2024 JMIR (PMC11615553): initial 0/80, framework 4-C 61/80 (76%).
8. Bucinca 2021 (arXiv 2102.09692 full text): N=199, MTurk, three forcing designs vs two XAI designs vs no-AI baseline; forcing reduced overreliance but did not remove it.
9. Shimizu 2013 (PubMed 23228085): n=188 (91/97); 8.25 vs 8.77 (p=0.01); 7.21 vs 7.96 (p=0.001); general debiasing checklist no gain.
10. Croskerry 2003 abstract (PubMed 12514691): proposal only, no data. Also re-read: Schmidgall 2024 (full text), Savage 2024 (full text), Huang 2023 (full text); corrections for these are below.

## Corrections made

- **Huang 2023 (c14, c28) oracle numbers are wrong.** The evidence lines say oracle self-correction reached GSM8K 95.5 for GPT-3.5 and 97.5 for GPT-4. The table (arXiv 2310.01798 Tables 2 and 3) shows 95.5 is GPT-4 standard prompting. GPT-3.5: standard 75.9, oracle 84.3; CommonSenseQA 75.8 to 89.7; HotpotQA 26.0 to 29.0. GPT-4: standard 95.5, oracle 97.5; with unaided self-correction GPT-4 falls 95.5 to 91.5 to 89.0 (GSM8K) and HotpotQA 49.0 to 43.0. The GPT-3.5 CommonSenseQA drop 75.8 to 38.1 (41.8 round two) and the 74.7% retained-answer figure are correct. Also c28's "CommonSenseQA GPT-3.5 oracle 82.0, HotpotQA 49.0" are GPT-4 standard numbers.
- **Schmidgall 2024 (a15) per-model "mean drop" figures (GPT-4 -5.1, Mixtral -7.7, GPT-3.5 -17.8, Llama2 -20.1, PMC -9.6) are not in the arXiv text.** The paper gives GPT-3.5 average drop 37.4%, GPT-4 worst case 14.0% (false consensus) and 0.2% (confirmation). The drops are relative: 0.727 to 0.625 is 10.2 points but 14.0% relative. Use c01 and c02, not a15. The cross-model bias means (24.9, 18.2, 12.9, 8.1) are confirmed.
- **Savage 2024 (a18) intuitive-prompt p-value**: a18 says p=0.4; arXiv v1 text says P=0.9 (CI -1.6 to 5.1). The published version may differ. The GPT-4 numbers in c15 are confirmed (76, 77, 78, 78, 72).
- **Ke 2024**: three different figures sit in the files (a20/b22: 61/80 top-2 in the JMIR paper; c07: 57/80 top-1 and 64/80 top-2 for an earlier preprint setup). They are two versions of one study, not two sources.
- **Bucinca (b26)**: six conditions confirmed (three forcing, two XAI, no-AI).

## Duplicates that inflate apparent independence

Same study, listed more than once: Sherbino 2014 (a03 is the pilot, a04 = b01); Norman 2014 (a05 = b02); Norman 2017 (a06 = b03); Ely 2011 (a02 = b06); Sibbald 2019 (a11 = b08); Schmidgall (a15 = b21 = c01-c03 = c17); Echterhoff (a16 = b25 = c04 = c05 = c23); Degany o1 (a17 = b24); Ke (a20 = b22 = c07 = c18); Savage (a18 = c15 = c25); Huang (c14 = c28); Yan 2026 (a23 = b27); AI Timeouts (a24 = b28). Independent source counts in claims.jsonl are by study, not by line.

## Contradictions between sources

- Reflection: Mamede 2008/2012/2023 (helps residents on hard cases) vs Costa Filho 2019 (helps students on dermatology) vs the 2018 replication (no gain with novices on strict scoring). Case difficulty, expertise and scoring rule all vary at once.
- Checklists: Sibbald 2013/2015 (verify-time key-variable list helps experts) vs Sibbald 2019 (neither checklist helps) vs Chew 2017 (helps first half only). Same lab, different tasks.
- Debate: G9 says multi-agent debate does not beat voting at matched cost; Ke 2024 and Catfish report large gains but neither matches sampling cost.
- Self-review: Huang says intrinsic self-review hurts; Echterhoff "self-help" (the model rewrites a biased prompt) cut framing bias to 0.01. These are different operations (reasoning answer vs input rewrite) and should not be pooled.
- Bias warnings help GPT-4 but not smaller or medical models; example prompts change plain accuracy.

## Weak spots

- Almost all human data are vignette or exam tasks with students and residents; Staal found only 2 patient-based studies. Real-practice effect is unknown.
- The strongest negative human trial (Sherbino 2014) tested one teaching intervention on novices with 6 test cases (4 bias-prone, 2 false-positive). It does not show that CFS cannot work for experts.
- LLM bias work injects a sentence into exam stems. That is a prompt-bias test, not a test of the Croskerry mechanisms (search satisficing, premature closure arising from the model's own reasoning).
- Ke 2024 starts every case at 0% by selection; 80 runs are 16 cases x 5 repeats, so the effective n is 16.
- Most 2026 items (c09-c13, c19, c21, c22, c26, c27, a22, b27) are preprints or recent papers; I did not re-open them. Their numbers are as the first agents recorded them.
- Several 2026 leads were seen as titles or summaries only: a23/b27 (Yan), a24/a25/b28 (AI Timeouts, hypothesis cue), a22 (Qazi, opened:false).
- Lines marked opened:false in the evidence files that I checked only at abstract level: a01, a04/b01, a05/b02, a09, a11/b08, b17 (partly), b13. Never opened by anyone and not checked by me: a03 (2011 pilot, n=56), a22, a23/b27, a24/a25/b28, b07, b09, b10, b14, b15, a02/b06.
- Evidence on LLM-specific "slow down" is thin: nothing found that compares forced extra thinking with a bias warning at equal tokens.

## GAPS

1. At equal tokens, does any debiasing element (bias warning, alternatives list, devil's advocate pass) beat a plain model plus extra independent samples with code voting, on bias-injected items from our own task set? No source here controls for tokens.
2. Does a signal-triggered check (completeness gate, disagreement between samples) beat a scheduled check? Only one source (Srivastava 2026, N=150, one model) has both gate and sample-disagreement, and the gate alone hurt.
3. Do forced alternatives help on hard items and hurt on easy items for LLMs, as in human data (Shimizu, Mamede)? No LLM study splits by difficulty.
4. What is the effect size of a verify-time key-variable checklist for an LLM, when the checklist is built by code from the case? Human data (Sibbald 2013, 2015) come from one lab with n of 15 and 16.
5. How much of LLM bias in a deployed agent is prompt-injected (BiasMedQA style) vs self-generated premature closure? Only the 2026 information-seeking studies address the second, and I have not re-opened them.
6. Does answer-before-advice (commit first, then read tool or critic output) reduce acceptance of wrong advice in LLM agents, as it does in people (Bucinca 2021; Yan 2026)? No LLM test found.
7. Is the Ke 2024 gain from the roles or from simply taking five samples and a top-2 score? Needs a matched-sampling control; also test with different models to break correlated errors (G4).
8. Does knowledge-based immunisation (Mamede 2020: store discriminating features of look-alike options) transfer to an LLM with memory, and does it beat a bias warning?
9. Do reasoning models (o1 and later) remove the need for any debiasing step? Degany 2025 found 7 of 10 vignettes bias-free but a full failure on Occam's razor; no comparison at matched tokens with a prompted debiasing step.
10. Which of Croskerry's 2003 specific forcing rules (named pitfall, named counter-move) have any outcome test beyond Sherbino 2014's two bias types? Most of the 30+ pitfalls have no test.

## Gap search results

Evidence in evidence_d.jsonl (d01-d18; 12 opened in full or in the relevant sections, 6 snippet-only and marked opened:false). Claims K17, K22, K18, K07 updated; K27-K33 added. The 2026 numbers come from one paper each and have not been replicated.

1. Equal tokens, debiasing vs sampling: PARTLY CLOSED for debate and roles, OPEN for bias warnings and alternatives lists. Three reviews (Smit 2024, Wang 2024, Zhang 2025; d01-d03) find debate rarely beats self-consistency or a good single prompt at comparable cost. No study found tests a bias warning or alternatives list against extra samples on bias-injected items. Oh 2025 (d11) shows parallel samples beat a bigger token budget for short-reasoning medical 7B models.
2. Signal-triggered vs scheduled check: LEANS YES, one source. REGAR 2026 (d06): disagreement/entropy-triggered reflection beat always-on reflection and budget-matched self-consistency on math (65.2 vs 60.8, MATH-500, Qwen3-8B). Kamoi 2024 (d04) says free-form self-feedback does not work. Not tested clinically; stays single-source (K28).
3. Hard vs easy for LLMs: PARTLY CLOSED. Extra revision hurt on easy PubMedQA and wasted tokens on easy math (d05, d11); helped on harder items. No clinical diagnosis study splits by difficulty (K29, contested).
4. Key-variable checklist effect size for an LLM: STILL OPEN. Only a snippet-level structured-prompt result (+4.1 points, d14, not opened).
5. Injected vs self-generated bias: PARTLY CLOSED. Kenaston 2025 (d07) shows GPT-4 on real notes has self-generated confirmation and anchoring errors (23.1%). No share-of-error estimate for an agent, and no mitigation tested.
6. Answer-before-advice for LLMs: STILL OPEN, with indirect support. SycEval (d09): pre-answer rebuttals flip more than post-commit (61.75% vs 56.52%), yet committed answers still flip. Christophe 2026 (d10): thinking models rationalise expert-labelled wrong hints. No direct commit-first vs advice-first test of critic output.
7. Ke 2024 roles vs five samples: LARGELY CLOSED as a prior, not as a test. Matched-cost reviews say role/debate gain is usually not there, and heterogeneous models are the lever (d03). Ke's own matched control is still not run.
8. Knowledge-based immunisation in LLM memory: STILL OPEN. Nothing found. m1 (d12) agrees extra thinking without knowledge adds little.
9. Reasoning models and debiasing: PARTLY CLOSED. R1 audit (d08): 93% on 100 MedQA, errors still include anchoring; a BiasMedQA preprint (d13) says reasoning does not protect, but its full text was blocked, so numbers are missing. No matched-token comparison with a debiasing prompt.
10. Outcome tests of Croskerry's specific rules: STILL OPEN. Nothing new found beyond Sherbino 2014.

Caveats: APIs (arXiv, Semantic Scholar, OpenAlex) rate-limited all searches; 8 WebSearch calls used; a few extracted tables (REGAR, Christophe) were garbled so only text-stated figures were used.
