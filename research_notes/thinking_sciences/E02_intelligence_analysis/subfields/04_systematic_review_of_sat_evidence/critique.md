# Critique: Systematic review of SAT evidence (E02.04)

## Corrections made (numbers re-opened this session)
Re-opened: Mandel 2018 (JDM html), AgentCDM PDF, Huang 2024 PDF, Karvetski and Mandel 2020 PDF, Karvetski/Mandel/Irwin 2020 PDF, Dhami 2024 (PMC XML).

1. a09 Mandel 2018: control MAE .21 vs ACH .26 confirmed (p=.14). Effect size is d=0.43, not 0.45. Usefulness r .68 vs .17 (d=1.59), unitarity 1.54 vs 1.77, coherentizing 0.23 to 0.15 (35%), averaging 0.09 (61%), experience 14.08 months (SD 29.5, so skewed): all confirmed. Per-arm N of 25 is inferred, not stated.
2. a24 Huang: the oracle line is wrong. "GPT-3.5 GSM8K 95.5, HotpotQA 26 to 49" mixes GPT-3.5 and GPT-4. Correct: GPT-3.5 oracle GSM8K 84.3, CommonsenseQA 89.7, HotpotQA 29.0; GPT-4 standard 95.5/82.0/49.0, oracle 97.5/85.5/59.0. c16 has the right numbers. CSQA 75.8 to 38.1, GPT-4 GSM8K 95.5 to 89.0 (5 calls), debate 83.2 vs self-consistency 85.3 at 6 responses: confirmed.
3. c02/a-lines on AgentCDM: the text extract is misaligned. The statement "ACH beat Informed Dictatorial by 1.9 points" is the authors' own text, but the column I could align is 82.9 = Homogeneous ACH, 82.2 = Qwen-7B-Instruct ACH, 87.6 = Qwen-7B-R1 ACH, 88.4 = AgentCDM; the Informed Dictatorial All Average cell was not recoverable (about 81.0 by implication). So "informed dictatorial 82.9" in c02 is wrong. Ablation (72.6/52.5/89.0 vanilla; 68.1/49.4/84.0 scaffold-only) and 67.9 vs 55.9 confirmed. Note the model is trained, so the 1.9-point zero-shot gain is the only pure-prompt result.
4. b06 (MAD .22 vs .18, d=.20, N=227, t(218)=1.14 p=.25 d=.15 for the other contrast) confirmed. a12 describes the same experiment (graffiti task).
5. b07: "just over 1 SD reduction in error" confirmed; N=147 is from Wilcox and Mandel (a11 lacked it).
6. b08 Dhami 2024: 61.8% / 39.2% / 67.3% and cell counts sum to N=161. Confirmed (chi2 not re-read).

Not re-opened (publisher or PubMed bot walls, WebFetch returned nothing): De Wit 2012, De Dreu 2003, Martin 2025 (stats still second-hand from earlier agents), Schwenk 1990, Mullen 1991, Coulthart 2017, Du 2023, Sharma 2024 (the 98% / 42% / 27% figures in b25 are unverified).

## Contradictions between sources
- Debate: Du 2023 (large gains) vs Smit 2024, Huang 2024, Zhang 2025 (no gain at equal compute). Resolved in favour of the later equal-compute work.
- Conflict: De Dreu 2003 (task conflict harms) vs De Wit 2012 (not replicated, moderator-dependent) vs Coulthart ("conflict improves quality"). All three differ in construct and task; no clean reading.
- ACH helps diagnosticity ratings (Mandel 2018) yet hurts diagnosticity in two other studies (Wilcox and Mandel table 3). Count is 1 positive, 2 negative.
- Lehner N: a08 says 5 vs 7, a15 gives smallest sample 12; consistent (5+7).
- Dhami 2019 and Mandel 2018 are the same 50 analysts, so they are one source, not two. a09/b05/a10/b09 should not be counted as independent. Same for a04/a05/b17 (one Martin preprint).
- Opposite claims on Wang 2024: b22 shows MAD (3 agents) weakest; a25's column labels unclear. Ordering only trusted.

## Weak spots
- The founding claim (over 2,000 studies) was never read beyond its abstract; method is vote counting on mostly non-intelligence studies.
- Most ACH tests have N under 60 for analysts; the large ones use lay samples.
- LLM debate studies use GPT-3.5/GPT-4 era models and unequal compute; few use current frontier models. Only Zhong 2026 (a30) tests SAT skills on 2026 models.
- No LLM study tests brainstorming, key assumptions check, pre-mortem or red team as measured scaffolds on analyst tasks.
- Claims graded "single-source" often mean one team, not one paper.

## Seen only in snippets or second-hand
a03, a08, a10-a14 (via Wilcox and Mandel), a18, a19, a20, a31 (abstract and intro only), c21 (rates not transcribed), c23, b24, b25, b28.

## GAPS
1. Does a code-scored Bayesian hypothesis matrix (code sets weights, model only rates each item) beat a plain judge and a prompt-only ACH on current models at equal tokens, on items with known answers?
2. What per-technique effect sizes and study counts does Coulthart (2017) actually report for ACH, devil's advocacy and brainstorming, and how many studies are intelligence-like?
3. Are Schwenk 1990 and Mullen 1991 effect sizes as remembered, and have they replicated with LLM "teams" (independent-then-merge vs shared-context generation)?
4. At equal token cost, does assigned dissent (critic that sees no proposed answer) beat self-consistency on current frontier models, and on which task types (counterintuitive vs routine)?
5. What signal predicts when a critic or matrix step helps (disagreement between samples, low margin, tie), so it can be triggered instead of always on?
6. Does weighing evidence beat seeking disconfirming evidence for an LLM? No controlled test exists; design one with planted misleading and correlated evidence.
7. How does an LLM handle correlated or duplicate evidence in a matrix (double counting as in Karvetski 2020), and does code-side dependence handling fix it?
8. Do pre-mortem, key assumptions check and red-team prompts have any measured effect on current LLMs on analyst-style forecasting or investigation tasks?
9. What are the exact flip rates in Wynn 2025 and are they reduced by independent-first sampling or by mixing model families?
10. Does hypothesis-layout (rows vs columns) in a prompt change LLM anchoring, as it did for humans in Dhami 2024?


## Gap search results (evidence_d.jsonl, d01-d17; claims K29-K34 added)
Search limits: arXiv API and OpenAlex rate-limited, Semantic Scholar empty, publisher and Pitt/CORE pages blocked by bot walls (not bypassed). 3 of 6 WebSearch calls used before the shared budget ran out.

1. Code-scored matrix vs plain judge vs prompt-only ACH at equal tokens: PARTLY CLOSED. LEAP (d08, d09) shows per-item ratings plus code Bayes update beats a plain judge at matched tokens (FX .6512 to .7284) on 5 models, but on forecasting, with no prompt-only ACH arm. PRISM (d06, d07) shows a structured pipeline beats direct and self-consistency on known-answer items (58.1 to 71.3 vs SC 63.2) but its LLM-judged ACH step added only +0.8 and tokens were not matched. No study has all three arms. Still open.
2. Coulthart per-technique numbers: OPEN. Abstract only (d01): random sample of over 2,000 studies, 21-student experiment. The PDF and the IJIC article are blocked. Critics quote it as 'highly credible evidence base' (d02) and call that unwarranted. Count of intelligence-like studies unknown.
3. Schwenk 1990 and Mullen 1991 numbers and LLM replication: OPEN. Publisher pages blocked; no LLM brainstorming-teams study found. Nearest: independent diverse starts beat shared starts (d13).
4. Assigned dissent vs self-consistency at equal tokens: OPEN for dissent specifically. Generic debate beats SC by 1.3 points at matched compute in one 2026 study (d11) while Wynn (d03) and DynaDebate (d13) find debate at or below independent majority vote. Task type: gains concentrate on hard items (d12, d13). No test of a critic that sees no answer.
5. Trigger signal: PARTLY CLOSED. Low agreement among independent samples (hard bin) marks where structure pays (d12); DynaDebate calls a verifier only on disagreement (d13). No direct trigger-vs-always-on comparison.
6. Weighing vs seeking evidence for an LLM: OPEN. Design (not run): items with planted misleading, duplicated and correlated evidence; arms = (a) code-weighted matrix, (b) matrix plus forced disconfirmation search, (c) plain judge; equal tokens; score on known answers and calibration.
7. Correlated or duplicate evidence: PARTLY CLOSED. Code-side source-key grouping helps (d09, +1.9 points, ECE .158 to .088); models discount exact repeats but not shown for paraphrases (d10). Dedupe key came from the LLM.
8. Pre-mortem, key assumptions check, red team on analyst tasks: OPEN. Only a prompt-only pre-mortem on safety (d14, harm 3.22 to 2.19) and a data-free position paper (d15).
9. Wynn 2025 flip rates: PARTLY CLOSED. Table 1 accuracies recorded (d03); flip rates exist only in figures (d04). Independent-first majority is the baseline and beats debate in most mixed groups; mixing model families did not fix it.
10. Layout rows vs columns for LLMs: OPEN. Only option-position bias found (d16).

Not verified this session: all Schwenk, Mullen, De Dreu, De Wit and Martin numbers. Wynn row labels were garbled in text extract, so group identities are inferred. Newly cited 2026 papers (LEAP, Kawada, Wunderlich, PRISM) are single preprints or papers, not replicated.
